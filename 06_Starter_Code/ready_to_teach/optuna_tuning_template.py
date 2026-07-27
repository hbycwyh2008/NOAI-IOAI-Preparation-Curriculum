from __future__ import annotations

import argparse
import json
from pathlib import Path

import optuna
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_dataset(seed: int):
    features, labels = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=8,
        n_redundant=4,
        weights=[0.7, 0.3],
        class_sep=1.0,
        random_state=seed,
    )
    return features, labels


def objective_factory(features, labels, seed: int):
    splitter = StratifiedKFold(n_splits=4, shuffle=True, random_state=seed)

    def objective(trial: optuna.Trial) -> float:
        c_value = trial.suggest_float("C", 1e-3, 1e2, log=True)
        penalty = trial.suggest_categorical("penalty", ["l1", "l2"])

        model = Pipeline(
            steps=[
                ("scale", StandardScaler()),
                (
                    "model",
                    LogisticRegression(
                        C=c_value,
                        penalty=penalty,
                        solver="liblinear",
                        class_weight="balanced",
                        max_iter=1000,
                        random_state=seed,
                    ),
                ),
            ]
        )

        scores = cross_val_score(
            model,
            features,
            labels,
            cv=splitter,
            scoring="f1",
            n_jobs=1,
        )
        return float(scores.mean())

    return objective


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Run a small local Optuna study after a manual tuning cycle. "
            "This template uses cross-validation and never touches a competition test set."
        )
    )
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("optuna_tuning_results.json"),
    )
    args = parser.parse_args()

    if args.trials < 1:
        raise ValueError("--trials must be at least 1")

    optuna.logging.set_verbosity(optuna.logging.WARNING)
    features, labels = build_dataset(seed=args.seed)

    sampler = optuna.samplers.TPESampler(seed=args.seed)
    study = optuna.create_study(direction="maximize", sampler=sampler)
    study.optimize(
        objective_factory(features=features, labels=labels, seed=args.seed),
        n_trials=args.trials,
    )

    payload = {
        "metric": "mean_cross_validated_f1",
        "direction": "maximize",
        "trials": args.trials,
        "best_value": float(study.best_value),
        "best_params": study.best_params,
        "test_set_used_for_tuning": False,
        "search_space_rationale": {
            "C": "log scale because useful regularisation values may span several orders of magnitude",
            "penalty": "compare sparse l1 and dense l2 regularisation under the same solver",
        },
        "student_next_step": (
            "Compare the Optuna result with the manual tuning baseline, inspect error categories, "
            "and decide whether the extra search cost produced a reliable gain."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("Optuna tuning complete.")
    print(f"Trials: {args.trials}")
    print(f"Best cross-validated F1: {study.best_value:.4f}")
    print(f"Best parameters: {study.best_params}")
    print(f"Results written to: {args.output}")
    print("The competition test set must never be used for this search.")


if __name__ == "__main__":
    main()
