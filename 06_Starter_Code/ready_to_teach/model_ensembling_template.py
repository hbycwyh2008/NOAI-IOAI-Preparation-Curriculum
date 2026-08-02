#!/usr/bin/env python3
"""Leakage-safe model-ensembling teaching scaffold.

This example demonstrates:

1. preserving a final holdout that is not used for model or weight selection;
2. generating out-of-fold (OOF) probabilities for two base models;
3. measuring individual performance and prediction correlation;
4. testing a deliberately small weighted-average ladder;
5. fitting the selected base models on all training rows;
6. using the final holdout once as a confirmation check.

Students must adapt the data, split, metric, models, and ensemble rule to the
actual task. In a competition, hidden test labels are unavailable and must never
be used for weight selection.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.base import clone
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demonstrate leakage-safe OOF probability averaging."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/tmp/model_ensembling_results.json"),
        help="JSON output path.",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--folds", type=int, default=5)
    return parser.parse_args()


def build_models(seed: int) -> dict[str, Any]:
    return {
        "logistic": Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "model",
                    LogisticRegression(
                        max_iter=2000,
                        class_weight="balanced",
                        random_state=seed,
                    ),
                ),
            ]
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=250,
            max_depth=8,
            min_samples_leaf=3,
            class_weight="balanced",
            random_state=seed,
            n_jobs=-1,
        ),
    }


def generate_oof_predictions(
    models: dict[str, Any],
    X: np.ndarray,
    y: np.ndarray,
    folds: int,
    seed: int,
) -> dict[str, np.ndarray]:
    if folds < 2:
        raise ValueError("folds must be at least 2")

    splitter = StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed)
    oof = {name: np.full(len(y), np.nan, dtype=float) for name in models}
    prediction_counts = np.zeros(len(y), dtype=int)

    for train_idx, valid_idx in splitter.split(X, y):
        prediction_counts[valid_idx] += 1
        for name, estimator in models.items():
            fitted = clone(estimator)
            fitted.fit(X[train_idx], y[train_idx])
            probabilities = fitted.predict_proba(X[valid_idx])[:, 1]
            oof[name][valid_idx] = probabilities

    if not np.all(prediction_counts == 1):
        raise RuntimeError("Every training row must receive exactly one OOF prediction.")

    for name, predictions in oof.items():
        if np.isnan(predictions).any():
            raise RuntimeError(f"OOF predictions for {name} contain missing values.")

    return oof


def select_small_weight_ladder(
    y: np.ndarray,
    prediction_a: np.ndarray,
    prediction_b: np.ndarray,
) -> tuple[float, list[dict[str, float]]]:
    # Keep the ladder intentionally small to reduce validation overfitting.
    weights_for_a = [0.25, 0.50, 0.75]
    results: list[dict[str, float]] = []

    for weight_a in weights_for_a:
        ensemble = weight_a * prediction_a + (1.0 - weight_a) * prediction_b
        results.append(
            {
                "weight_a": weight_a,
                "weight_b": 1.0 - weight_a,
                "oof_roc_auc": float(roc_auc_score(y, ensemble)),
            }
        )

    best = max(results, key=lambda row: row["oof_roc_auc"])
    return float(best["weight_a"]), results


def main() -> None:
    args = parse_args()

    X, y = make_classification(
        n_samples=1200,
        n_features=24,
        n_informative=10,
        n_redundant=6,
        weights=[0.72, 0.28],
        class_sep=1.0,
        flip_y=0.025,
        random_state=args.seed,
    )

    X_train, X_holdout, y_train, y_holdout = train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=args.seed,
    )

    models = build_models(args.seed)
    oof = generate_oof_predictions(
        models=models,
        X=X_train,
        y=y_train,
        folds=args.folds,
        seed=args.seed,
    )

    oof_scores = {
        name: float(roc_auc_score(y_train, predictions))
        for name, predictions in oof.items()
    }
    prediction_correlation = float(
        np.corrcoef(oof["logistic"], oof["random_forest"])[0, 1]
    )

    best_weight_logistic, weight_ladder = select_small_weight_ladder(
        y=y_train,
        prediction_a=oof["logistic"],
        prediction_b=oof["random_forest"],
    )

    fitted_models: dict[str, Any] = {}
    holdout_predictions: dict[str, np.ndarray] = {}
    for name, estimator in models.items():
        fitted = clone(estimator)
        fitted.fit(X_train, y_train)
        fitted_models[name] = fitted
        holdout_predictions[name] = fitted.predict_proba(X_holdout)[:, 1]

    ensemble_holdout = (
        best_weight_logistic * holdout_predictions["logistic"]
        + (1.0 - best_weight_logistic)
        * holdout_predictions["random_forest"]
    )

    holdout_scores = {
        name: float(roc_auc_score(y_holdout, predictions))
        for name, predictions in holdout_predictions.items()
    }
    holdout_scores["selected_ensemble"] = float(
        roc_auc_score(y_holdout, ensemble_holdout)
    )

    best_single_oof = max(oof_scores.values())
    best_ensemble_oof = max(row["oof_roc_auc"] for row in weight_ladder)

    result = {
        "seed": args.seed,
        "folds": args.folds,
        "selection_data": "OOF predictions on training partition only",
        "confirmation_data": "final holdout used once after selection",
        "oof_scores": oof_scores,
        "prediction_correlation": prediction_correlation,
        "weight_ladder": weight_ladder,
        "selected_weights": {
            "logistic": best_weight_logistic,
            "random_forest": 1.0 - best_weight_logistic,
        },
        "oof_gain_over_best_single": best_ensemble_oof - best_single_oof,
        "holdout_scores_for_confirmation_only": holdout_scores,
        "decision_rule": (
            "Keep the ensemble only if its OOF gain is larger than expected "
            "validation noise and its runtime, memory, and submission risk are acceptable."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
