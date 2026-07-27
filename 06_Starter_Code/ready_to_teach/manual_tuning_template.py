from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_dataset(seed: int):
    features, labels = make_classification(
        n_samples=1200,
        n_features=20,
        n_informative=8,
        n_redundant=4,
        weights=[0.7, 0.3],
        class_sep=1.0,
        random_state=seed,
    )
    train_features, holdout_features, train_labels, holdout_labels = train_test_split(
        features,
        labels,
        test_size=0.4,
        stratify=labels,
        random_state=seed,
    )
    validation_features, test_features, validation_labels, test_labels = train_test_split(
        holdout_features,
        holdout_labels,
        test_size=0.5,
        stratify=holdout_labels,
        random_state=seed,
    )
    return (
        train_features,
        validation_features,
        test_features,
        train_labels,
        validation_labels,
        test_labels,
    )


def make_model(c_value: float, seed: int) -> Pipeline:
    return Pipeline(
        steps=[
            ("scale", StandardScaler()),
            (
                "model",
                LogisticRegression(
                    C=c_value,
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=seed,
                ),
            ),
        ]
    )


def evaluate_candidate(
    c_value: float,
    seed: int,
    train_features,
    validation_features,
    train_labels,
    validation_labels,
) -> dict[str, float]:
    start = time.perf_counter()
    model = make_model(c_value=c_value, seed=seed)
    model.fit(train_features, train_labels)
    predictions = model.predict(validation_features)
    runtime_seconds = time.perf_counter() - start
    return {
        "C": c_value,
        "validation_f1": float(f1_score(validation_labels, predictions)),
        "runtime_seconds": runtime_seconds,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Demonstrate diagnosis-first, one-variable-at-a-time tuning on a "
            "local synthetic dataset. The test split is deliberately not used for tuning."
        )
    )
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("manual_tuning_results.json"),
    )
    args = parser.parse_args()

    (
        train_features,
        validation_features,
        _test_features,
        train_labels,
        validation_labels,
        _test_labels,
    ) = build_dataset(seed=args.seed)

    candidates = [0.01, 0.1, 1.0, 10.0]
    results = [
        evaluate_candidate(
            c_value=c_value,
            seed=args.seed,
            train_features=train_features,
            validation_features=validation_features,
            train_labels=train_labels,
            validation_labels=validation_labels,
        )
        for c_value in candidates
    ]

    best = max(results, key=lambda item: item["validation_f1"])
    payload = {
        "metric": "validation_f1",
        "tuned_variable": "LogisticRegression.C",
        "test_set_used_for_tuning": False,
        "results": results,
        "best_candidate": best,
        "student_next_step": (
            "Explain why C was selected, inspect validation errors, and decide whether "
            "the next experiment should target data, features, threshold, or model family."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("Manual tuning complete.")
    print(f"Best validation F1: {best['validation_f1']:.4f}")
    print(f"Best C: {best['C']}")
    print(f"Results written to: {args.output}")
    print("The test split was not used for tuning.")


if __name__ == "__main__":
    main()
