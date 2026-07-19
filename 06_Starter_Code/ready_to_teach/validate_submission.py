"""Validate competition submission schema, IDs, and prediction values.

Examples:
    python validate_submission.py test.csv submission.csv \
        --id-column student_id --prediction-column prediction --kind binary
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def validate_submission(
    test_path: Path,
    submission_path: Path,
    id_column: str,
    prediction_column: str,
    kind: str,
) -> None:
    test = pd.read_csv(test_path)
    submission = pd.read_csv(submission_path)

    if id_column not in test.columns:
        raise ValueError(f"Test file has no ID column {id_column!r}.")
    expected_columns = [id_column, prediction_column]
    if submission.columns.tolist() != expected_columns:
        raise ValueError(
            f"Submission columns/order must be {expected_columns}, "
            f"not {submission.columns.tolist()}."
        )
    if len(submission) != len(test):
        raise ValueError(f"Expected {len(test)} rows, found {len(submission)}.")
    if submission[id_column].isna().any() or submission[prediction_column].isna().any():
        raise ValueError("Submission contains missing IDs or predictions.")
    if submission[id_column].duplicated().any():
        raise ValueError("Submission contains duplicate IDs.")
    if submission[id_column].tolist() != test[id_column].tolist():
        raise ValueError("Submission IDs or order do not exactly match the test file.")

    values = pd.to_numeric(submission[prediction_column], errors="coerce")
    if values.isna().any() or not np.isfinite(values.to_numpy()).all():
        raise ValueError("Predictions must be finite numeric values.")

    if kind == "binary":
        unique = set(values.astype(int).tolist())
        if not np.allclose(values, values.astype(int)) or not unique.issubset({0, 1}):
            raise ValueError("Binary predictions must be integer 0 or 1.")
    elif kind == "probability":
        if ((values < 0) | (values > 1)).any():
            raise ValueError("Probabilities must lie in [0, 1].")
    elif kind == "regression":
        pass
    else:
        raise ValueError(f"Unsupported prediction kind: {kind}")

    print("VALID SUBMISSION")
    print(f"Rows: {len(submission)}")
    print(f"Prediction minimum: {values.min():.6f}")
    print(f"Prediction maximum: {values.max():.6f}")
    print(f"Unique predictions: {values.nunique()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("test", type=Path)
    parser.add_argument("submission", type=Path)
    parser.add_argument("--id-column", required=True)
    parser.add_argument("--prediction-column", required=True)
    parser.add_argument("--kind", choices=["binary", "probability", "regression"], required=True)
    args = parser.parse_args()
    validate_submission(
        args.test,
        args.submission,
        args.id_column,
        args.prediction_column,
        args.kind,
    )


if __name__ == "__main__":
    main()
