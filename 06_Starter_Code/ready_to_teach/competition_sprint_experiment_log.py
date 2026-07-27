from __future__ import annotations

import argparse
import csv
import math
from dataclasses import asdict, dataclass
from pathlib import Path

FIELDS = (
    "experiment_id",
    "hypothesis",
    "single_change",
    "metric_name",
    "metric_value",
    "runtime_seconds",
    "decision",
    "notes",
)


@dataclass(frozen=True)
class ExperimentRecord:
    experiment_id: str
    hypothesis: str
    single_change: str
    metric_name: str
    metric_value: float
    runtime_seconds: float
    decision: str
    notes: str = ""

    def validate(self) -> None:
        if not self.experiment_id.strip():
            raise ValueError("experiment_id must not be empty")
        if not self.hypothesis.strip():
            raise ValueError("hypothesis must not be empty")
        if not self.single_change.strip():
            raise ValueError("single_change must describe exactly what changed")
        if not self.metric_name.strip():
            raise ValueError("metric_name must not be empty")
        if not math.isfinite(self.metric_value):
            raise ValueError("metric_value must be finite")
        if not math.isfinite(self.runtime_seconds) or self.runtime_seconds < 0:
            raise ValueError("runtime_seconds must be finite and non-negative")
        if self.decision not in {"keep", "reject", "investigate"}:
            raise ValueError("decision must be keep, reject, or investigate")


def initialise(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()


def append_record(path: Path, record: ExperimentRecord) -> None:
    record.validate()
    initialise(path)
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writerow(asdict(record))


def read_records(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Experiment log not found: {path}")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def print_summary(path: Path) -> None:
    records = read_records(path)
    print(f"Experiments: {len(records)}")
    for row in records:
        print(
            f"{row['experiment_id']}: "
            f"{row['metric_name']}={row['metric_value']} | "
            f"decision={row['decision']} | change={row['single_change']}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create and maintain a competition-sprint experiment log."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create an empty CSV log")
    init_parser.add_argument("--path", type=Path, required=True)

    add_parser = subparsers.add_parser("add", help="Append one controlled experiment")
    add_parser.add_argument("--path", type=Path, required=True)
    add_parser.add_argument("--experiment-id", required=True)
    add_parser.add_argument("--hypothesis", required=True)
    add_parser.add_argument("--single-change", required=True)
    add_parser.add_argument("--metric-name", required=True)
    add_parser.add_argument("--metric-value", type=float, required=True)
    add_parser.add_argument("--runtime-seconds", type=float, required=True)
    add_parser.add_argument(
        "--decision", choices=("keep", "reject", "investigate"), required=True
    )
    add_parser.add_argument("--notes", default="")

    summary_parser = subparsers.add_parser("summary", help="Print the log summary")
    summary_parser.add_argument("--path", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "init":
        initialise(args.path)
        print(f"Initialised experiment log: {args.path}")
        return

    if args.command == "add":
        record = ExperimentRecord(
            experiment_id=args.experiment_id,
            hypothesis=args.hypothesis,
            single_change=args.single_change,
            metric_name=args.metric_name,
            metric_value=args.metric_value,
            runtime_seconds=args.runtime_seconds,
            decision=args.decision,
            notes=args.notes,
        )
        append_record(args.path, record)
        print(f"Added experiment {record.experiment_id} to {args.path}")
        return

    print_summary(args.path)


if __name__ == "__main__":
    main()
