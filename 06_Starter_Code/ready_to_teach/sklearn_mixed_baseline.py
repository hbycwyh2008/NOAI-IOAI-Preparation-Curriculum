"""Leakage-safe mixed-type classification baseline.

Example:
    python sklearn_mixed_baseline.py practice_data/tabular_practice.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import GroupShuffleSplit, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_pipeline(numeric: list[str], categorical: list[str]) -> Pipeline:
    numeric_pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="median", add_indicator=True)),
            ("scale", StandardScaler()),
        ]
    )
    categorical_pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocess = ColumnTransformer(
        [
            ("numeric", numeric_pipe, numeric),
            ("categorical", categorical_pipe, categorical),
        ],
        remainder="drop",
    )
    return Pipeline(
        [
            ("preprocess", preprocess),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]
    )


def split_data(
    data: pd.DataFrame,
    target: str,
    group: str | None,
    seed: int,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    features = data.drop(columns=[target])
    labels = data[target].astype(int)

    if group:
        if group not in data.columns:
            raise ValueError(f"Group column not found: {group}")
        splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=seed)
        train_idx, val_idx = next(splitter.split(features, labels, groups=data[group]))
        return features.iloc[train_idx], features.iloc[val_idx], labels.iloc[train_idx], labels.iloc[val_idx]

    return train_test_split(
        features,
        labels,
        test_size=0.25,
        random_state=seed,
        stratify=labels,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path)
    parser.add_argument("--target", default="target")
    parser.add_argument("--group", default="school_id")
    parser.add_argument("--id", default="student_id")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    data = pd.read_csv(args.csv)
    if args.target not in data.columns:
        raise ValueError(f"Target column not found: {args.target}")
    if data[args.target].isna().any():
        raise ValueError("Training labels contain missing values.")

    X_train, X_val, y_train, y_val = split_data(data, args.target, args.group or None, args.seed)
    drop_columns = [column for column in [args.id, args.group] if column and column in X_train.columns]
    X_train = X_train.drop(columns=drop_columns)
    X_val = X_val.drop(columns=drop_columns)

    categorical = X_train.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    numeric = [column for column in X_train.columns if column not in categorical]
    if not numeric and not categorical:
        raise ValueError("No usable feature columns remain.")

    model = build_pipeline(numeric, categorical)
    model.fit(X_train, y_train)
    predictions = model.predict(X_val)

    print(f"Rows: train={len(X_train)}, validation={len(X_val)}")
    print(f"Macro F1: {f1_score(y_val, predictions, average='macro'):.4f}")
    print(classification_report(y_val, predictions, digits=4, zero_division=0))


if __name__ == "__main__":
    main()
