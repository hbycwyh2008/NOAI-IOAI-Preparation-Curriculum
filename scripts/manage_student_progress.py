from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "curriculum_spec.json"
SET_ID_RE = re.compile(r"^[0-9a-f]{10}$")
SCENARIO_ID_RE = re.compile(r"^L[1-3]-D\d{2}$")
ALLOWED_LEVELS = {"1", "2", "3", "mixed"}


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def parse_sessions(value: str) -> set[int]:
    sessions: set[int] = set()
    value = value.strip()
    if not value:
        return sessions
    for token in value.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_text, end_text = token.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            if start > end:
                raise ValueError(f"Invalid descending range: {token}")
            sessions.update(range(start, end + 1))
        else:
            sessions.add(int(token))
    return sessions


def compact_ranges(values: Iterable[int]) -> str:
    ordered = sorted(set(values))
    if not ordered:
        return "none"
    result: list[str] = []
    start = previous = ordered[0]
    for value in ordered[1:]:
        if value == previous + 1:
            previous = value
            continue
        result.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = value
    result.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(result)


def new_progress(student_id: str, pathway: str, spec: dict) -> dict:
    if pathway not in spec["pathways"]:
        raise ValueError(f"Unknown pathway: {pathway}")
    if not student_id.strip():
        raise ValueError("student_id must be a non-empty pseudonymous identifier")
    if "@" in student_id:
        raise ValueError("student_id must be pseudonymous and must not be an email address")
    return {
        "schema_version": 1,
        "student_id": student_id.strip(),
        "pathway": pathway,
        "completed_sessions": [],
        "red_sessions": [],
        "qualified_pathways": [],
        "drill_history": [],
        "last_updated": date.today().isoformat(),
    }


def validate_progress(data: dict, spec: dict) -> list[str]:
    errors: list[str] = []
    pathways = set(spec.get("pathways", {}))
    canonical = set(range(1, int(spec["canonical_sessions"]) + 1))

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")

    student_id = data.get("student_id")
    if not isinstance(student_id, str) or not student_id.strip():
        errors.append("student_id must be a non-empty string")
    elif "@" in student_id:
        errors.append("student_id must be pseudonymous and must not be an email address")

    if data.get("pathway") not in pathways:
        errors.append(f"pathway must be one of: {', '.join(sorted(pathways))}")

    session_fields: dict[str, set[int]] = {}
    for field in ("completed_sessions", "red_sessions"):
        values = data.get(field)
        if not isinstance(values, list) or any(type(value) is not int for value in values):
            errors.append(f"{field} must be a list of integer Session IDs")
            session_fields[field] = set()
            continue
        if len(values) != len(set(values)):
            errors.append(f"{field} contains duplicate Session IDs")
        invalid = sorted(set(values) - canonical)
        if invalid:
            errors.append(f"{field} contains Sessions outside 1-{len(canonical)}: {invalid}")
        session_fields[field] = set(values)

    if not session_fields.get("red_sessions", set()).issubset(session_fields.get("completed_sessions", set())):
        errors.append("red_sessions must be a subset of completed_sessions")

    qualified = data.get("qualified_pathways")
    if not isinstance(qualified, list) or any(not isinstance(value, str) for value in qualified):
        errors.append("qualified_pathways must be a list of pathway names")
    else:
        if len(qualified) != len(set(qualified)):
            errors.append("qualified_pathways contains duplicates")
        unknown = sorted(set(qualified) - pathways)
        if unknown:
            errors.append(f"qualified_pathways contains unknown pathways: {unknown}")

    try:
        date.fromisoformat(str(data.get("last_updated", "")))
    except ValueError:
        errors.append("last_updated must be an ISO date")

    history = data.get("drill_history")
    if not isinstance(history, list):
        errors.append("drill_history must be a list")
        history = []

    seen_set_ids: set[str] = set()
    for index, record in enumerate(history):
        prefix = f"drill_history[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{prefix} must be an object")
            continue
        try:
            date.fromisoformat(str(record.get("date", "")))
        except ValueError:
            errors.append(f"{prefix}.date must be an ISO date")
        set_id = record.get("set_id")
        if not isinstance(set_id, str) or not SET_ID_RE.fullmatch(set_id):
            errors.append(f"{prefix}.set_id must be ten lowercase hexadecimal characters")
        elif set_id in seen_set_ids:
            errors.append(f"duplicate drill set_id: {set_id}")
        else:
            seen_set_ids.add(set_id)
        if str(record.get("level")) not in ALLOWED_LEVELS:
            errors.append(f"{prefix}.level must be 1, 2, 3, or mixed")
        scenario_ids = record.get("scenario_ids")
        if not isinstance(scenario_ids, list) or any(
            not isinstance(value, str) or not SCENARIO_ID_RE.fullmatch(value) for value in scenario_ids
        ):
            errors.append(f"{prefix}.scenario_ids must contain valid public scenario IDs")
        elif len(scenario_ids) != len(set(scenario_ids)):
            errors.append(f"{prefix}.scenario_ids contains duplicates")
        for numeric_field in ("task_family_accuracy", "score_percent"):
            value = record.get(numeric_field)
            if value is not None and (not isinstance(value, (int, float)) or not 0 <= float(value) <= 1):
                errors.append(f"{prefix}.{numeric_field} must be null or a number from 0 to 1")
        if not isinstance(record.get("reviewed", False), bool):
            errors.append(f"{prefix}.reviewed must be boolean")

    return errors


def load_progress(path: Path, spec: dict | None = None) -> dict:
    spec = spec or load_spec()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Progress file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid progress JSON: {error}") from error
    errors = validate_progress(data, spec)
    if errors:
        raise ValueError("Invalid progress file:\n- " + "\n- ".join(errors))
    return data


def save_progress(path: Path, data: dict, spec: dict | None = None) -> None:
    spec = spec or load_spec()
    data["completed_sessions"] = sorted(set(int(value) for value in data["completed_sessions"]))
    data["red_sessions"] = sorted(set(int(value) for value in data["red_sessions"]))
    data["qualified_pathways"] = sorted(set(str(value) for value in data["qualified_pathways"]))
    data["last_updated"] = date.today().isoformat()
    errors = validate_progress(data, spec)
    if errors:
        raise ValueError("Refusing to save invalid progress:\n- " + "\n- ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def record_drill_assignment(
    data: dict,
    *,
    day: str,
    set_id: str,
    level: str,
    scenario_ids: list[str],
) -> None:
    if any(record.get("set_id") == set_id for record in data["drill_history"]):
        return
    data["drill_history"].append(
        {
            "date": day,
            "set_id": set_id,
            "level": level,
            "scenario_ids": scenario_ids,
            "task_family_accuracy": None,
            "score_percent": None,
            "reviewed": False,
        }
    )


def score_drill(data: dict, set_id: str, task_family_accuracy: float, score_percent: float) -> None:
    for record in data["drill_history"]:
        if record.get("set_id") == set_id:
            record["task_family_accuracy"] = task_family_accuracy
            record["score_percent"] = score_percent
            record["reviewed"] = True
            return
    raise ValueError(f"Unknown drill set_id: {set_id}")


def run_self_test() -> None:
    spec = load_spec()
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "progress.json"
        data = new_progress("student-001", "noai_round1", spec)
        data["completed_sessions"] = [1, 2, 3]
        data["red_sessions"] = [3]
        data["qualified_pathways"] = ["noai_round1"]
        record_drill_assignment(
            data,
            day="2026-08-04",
            set_id="0123456789",
            level="mixed",
            scenario_ids=["L1-D01", "L2-D13"],
        )
        save_progress(path, data, spec)
        loaded = load_progress(path, spec)
        assert loaded["red_sessions"] == [3]
        score_drill(loaded, "0123456789", 0.9, 0.8)
        save_progress(path, loaded, spec)
        assert load_progress(path, spec)["drill_history"][0]["reviewed"] is True

        invalid = new_progress("student-002", "noai_round1", spec)
        invalid["red_sessions"] = [4]
        assert any("subset" in error for error in validate_progress(invalid, spec))

    print("Student progress manager self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create, validate, and update a pseudonymous student progress ledger.")
    parser.add_argument("--self-test", action="store_true")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--path", type=Path, required=True)
    init_parser.add_argument("--student-id", required=True)
    init_parser.add_argument("--pathway", choices=("noai_round1", "noai_round2", "ioai_full"), required=True)
    init_parser.add_argument("--force", action="store_true")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--path", type=Path, required=True)
    update_parser.add_argument("--complete", default="")
    update_parser.add_argument("--mark-red", default="")
    update_parser.add_argument("--clear-red", default="")
    update_parser.add_argument("--qualify", choices=("noai_round1", "noai_round2", "ioai_full"), action="append")
    update_parser.add_argument("--pathway", choices=("noai_round1", "noai_round2", "ioai_full"))

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--path", type=Path, required=True)

    score_parser = subparsers.add_parser("score-drill")
    score_parser.add_argument("--path", type=Path, required=True)
    score_parser.add_argument("--set-id", required=True)
    score_parser.add_argument("--task-family-accuracy", type=float, required=True)
    score_parser.add_argument("--score-percent", type=float, required=True)

    args = parser.parse_args()
    if args.self_test:
        run_self_test()
        return 0
    if not args.command:
        parser.error("choose a command or use --self-test")

    try:
        spec = load_spec()
        if args.command == "init":
            if args.path.exists() and not args.force:
                raise ValueError(f"Progress file already exists: {args.path}; use --force to replace it")
            save_progress(args.path, new_progress(args.student_id, args.pathway, spec), spec)
            print(f"Created progress ledger: {args.path}")
        elif args.command == "validate":
            data = load_progress(args.path, spec)
            print(f"Progress ledger valid for {data['student_id']} on {data['pathway']}.")
        elif args.command == "update":
            data = load_progress(args.path, spec)
            completed = set(data["completed_sessions"])
            red = set(data["red_sessions"])
            newly_completed = parse_sessions(args.complete)
            newly_red = parse_sessions(args.mark_red)
            completed.update(newly_completed | newly_red)
            red.update(newly_red)
            red.difference_update(parse_sessions(args.clear_red))
            data["completed_sessions"] = sorted(completed)
            data["red_sessions"] = sorted(red)
            if args.qualify:
                data["qualified_pathways"] = sorted(set(data["qualified_pathways"]) | set(args.qualify))
            if args.pathway:
                data["pathway"] = args.pathway
            save_progress(args.path, data, spec)
            print(
                f"Updated {args.path}: completed={compact_ranges(completed)}, red={compact_ranges(red)}, "
                f"qualified={', '.join(data['qualified_pathways']) or 'none'}"
            )
        elif args.command == "score-drill":
            data = load_progress(args.path, spec)
            score_drill(data, args.set_id, args.task_family_accuracy, args.score_percent)
            save_progress(args.path, data, spec)
            print(f"Recorded reviewed scores for drill set {args.set_id}.")
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Student progress operation failed: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
