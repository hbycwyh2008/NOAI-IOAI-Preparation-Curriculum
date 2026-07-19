"""Binary-classification metrics with explicit validation.

Use this file to compare hand calculations with sklearn.  The positive class
must be defined before interpreting the results.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import sqrt


@dataclass(frozen=True)
class BinaryMetrics:
    accuracy: float
    precision: float
    recall: float
    specificity: float
    f1: float
    mcc: float


def _safe_divide(numerator: float, denominator: float) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def metrics_from_counts(tp: int, tn: int, fp: int, fn: int) -> BinaryMetrics:
    """Calculate common binary metrics from non-negative integer counts."""
    counts = {"tp": tp, "tn": tn, "fp": fp, "fn": fn}
    if any(not isinstance(value, int) for value in counts.values()):
        raise TypeError("TP, TN, FP, and FN must be integers.")
    if any(value < 0 for value in counts.values()):
        raise ValueError("Confusion-matrix counts cannot be negative.")
    total = tp + tn + fp + fn
    if total == 0:
        raise ValueError("At least one example is required.")

    precision = _safe_divide(tp, tp + fp)
    recall = _safe_divide(tp, tp + fn)
    specificity = _safe_divide(tn, tn + fp)
    f1 = _safe_divide(2 * precision * recall, precision + recall)
    mcc_denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return BinaryMetrics(
        accuracy=(tp + tn) / total,
        precision=precision,
        recall=recall,
        specificity=specificity,
        f1=f1,
        mcc=_safe_divide(tp * tn - fp * fn, mcc_denominator),
    )


def main() -> None:
    example = metrics_from_counts(tp=30, tn=50, fp=10, fn=10)
    for name, value in asdict(example).items():
        print(f"{name:>12}: {value:.4f}")


if __name__ == "__main__":
    main()
