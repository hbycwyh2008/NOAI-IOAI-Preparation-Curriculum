from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from manage_student_progress import validate_progress

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "curriculum_spec.json"
MISSIONS = ROOT / "02_Class_Missions"
SESSION_ROW = re.compile(r"^\|\s*(\d{1,3})\s*\|")
LOCAL_MD_LINK = re.compile(r"\[[^\]]+\]\(([^)#]+\.md)(?:#[^)]+)?\)")
SCENARIO_HEADING = re.compile(r"^###\s+(?:Day|Scenario)\s+(\d+)\b", re.MULTILINE)
SECTION_HEADING = re.compile(r"^##\s+", re.MULTILINE)


def fail(errors: list[str]) -> int:
    print("Curriculum specification validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def expand_session_text(value: str) -> list[int]:
    cleaned = value.replace("–", "-").replace("—", "-").replace("`", "")
    sessions: list[int] = []
    for match in re.finditer(r"\b(\d{1,3})(?:\s*-\s*(\d{1,3}))?\b", cleaned):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start > end:
            raise ValueError(f"Descending Session range: {start}-{end}")
        sessions.extend(range(start, end + 1))
    return sessions


def exact_route_sessions(document: Path) -> list[int]:
    text = document.read_text(encoding="utf-8")
    marker = "## Exact Session Route"
    if marker not in text:
        return []
    section = text.split(marker, 1)[1]
    next_heading = SECTION_HEADING.search(section)
    if next_heading:
        section = section[: next_heading.start()]

    sessions: list[int] = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"Block", "Stage"} or set(cells[0]) <= {"-", ":"}:
            continue
        sessions.extend(expand_session_text(cells[1]))
    return sessions


def validate_progress_contract(spec: dict, errors: list[str]) -> None:
    contract = spec.get("student_progress", {})
    schema_path = ROOT / str(contract.get("schema", ""))
    example_path = ROOT / str(contract.get("example", ""))

    if not schema_path.exists():
        errors.append("Missing student progress JSON schema")
    else:
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid student progress JSON schema: {error}")
            schema = {}

        declared = contract.get("schema_version")
        actual = schema.get("properties", {}).get("schema_version", {}).get("const")
        if actual != declared:
            errors.append("Student progress schema version does not match curriculum_spec.json")

        required = set(schema.get("required", []))
        for marker in ("student_id", "drill_history", "recognition_confirmation"):
            if marker not in required:
                errors.append(f"Student progress schema must require {marker}")

        drill_items = schema.get("properties", {}).get("drill_history", {}).get("items", {})
        drill_required = set(drill_items.get("required", []))
        if "baseline_metric_accuracy" not in drill_required:
            errors.append("Student progress drill records must require baseline_metric_accuracy")

        confirmation_required = set(
            schema.get("properties", {}).get("recognition_confirmation", {}).get("required", [])
        )
        if confirmation_required != {"passed", "date"}:
            errors.append("Recognition confirmation schema must require exactly passed and date")

    if not example_path.exists():
        errors.append("Missing student progress example")
    else:
        try:
            example = json.loads(example_path.read_text(encoding="utf-8"))
            errors.extend(f"Student progress example: {error}" for error in validate_progress(example, spec))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid student progress example JSON: {error}")

    if contract.get("privacy_rule") != "pseudonymous identifier only; no name or email address":
        errors.append("Student progress privacy rule must forbid names and email addresses")
    if contract.get("red_must_be_completed") is not True:
        errors.append("Student progress contract must require Red Sessions to be completed attempts")
    if contract.get("one_daily_assignment_per_date") is not True:
        errors.append("Student progress contract must enforce one daily assignment per date")
    if contract.get("migration_command") != "python scripts/manage_student_progress.py migrate --path PATH":
        errors.append("Student progress contract must declare the supported migration command")


def validate_recognition_contract(spec: dict, errors: list[str]) -> tuple[int, int]:
    recognition = spec["model_recognition"]
    routine = ROOT / recognition["routine"]
    drill_index = ROOT / recognition["drill_index"]
    if not routine.exists():
        errors.append(f"Missing model-recognition routine: {recognition['routine']}")
    if not drill_index.exists():
        errors.append(f"Missing model-recognition drill index: {recognition['drill_index']}")

    scenario_ids: list[str] = []
    global_numbers: list[int] = []
    scenario_count = 0
    for relative in recognition.get("scenario_files", []):
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing model-recognition scenario file: {relative}")
            continue
        level_match = re.search(r"Level_(\d)_", path.name)
        if not level_match:
            errors.append(f"Cannot infer scenario level from file name: {relative}")
            continue
        level = int(level_match.group(1))
        numbers = [int(value) for value in SCENARIO_HEADING.findall(path.read_text(encoding="utf-8"))]
        scenario_count += len(numbers)
        global_numbers.extend(numbers)
        scenario_ids.extend(f"L{level}-D{number:02d}" for number in numbers)
        if numbers:
            expected_local = list(range(numbers[0], numbers[0] + len(numbers)))
            if numbers != expected_local:
                errors.append(f"Scenario numbering must be internally consecutive in {relative}: {numbers}")

    minimum = int(recognition["minimum_public_scenarios"])
    if scenario_count < minimum:
        errors.append(f"Model-recognition scenarios below minimum: {scenario_count} < {minimum}")
    if global_numbers != list(range(1, scenario_count + 1)):
        errors.append("Model-recognition scenario files must collectively cover one sequence from Day 1")
    if len(scenario_ids) != len(set(scenario_ids)):
        errors.append("Model-recognition scenario IDs are not unique")

    daily_set_size = int(recognition.get("daily_set_size", 0))
    repeat_window = int(recognition.get("recent_repeat_window", 0))
    if daily_set_size < 1:
        errors.append("model_recognition.daily_set_size must be at least 1")
    if repeat_window < daily_set_size:
        errors.append("model_recognition.recent_repeat_window must be at least one daily set")
    if repeat_window >= scenario_count:
        errors.append("model_recognition.recent_repeat_window must leave unseen scenarios available")

    if int(recognition.get("mastery_consecutive_days", 0)) != 5:
        errors.append("Model-recognition public mastery eligibility must require five consecutive reviewed sets")
    for field in ("mastery_minimum_accuracy", "mastery_minimum_baseline_metric_accuracy"):
        value = recognition.get(field)
        if type(value) not in (int, float) or not 0 < float(value) <= 1:
            errors.append(f"model_recognition.{field} must be a number from 0 exclusive to 1 inclusive")
    if int(recognition.get("maintenance_sets_per_week", 0)) != 2:
        errors.append("Model-recognition maintenance must require two sets per week")
    if recognition.get("secured_confirmation_required") is not True:
        errors.append("A fresh private secured confirmation must remain required")

    return scenario_count, repeat_window


def main() -> int:
    errors: list[str] = []
    if not SPEC_PATH.exists():
        return fail(["Missing curriculum_spec.json"])

    try:
        spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return fail([f"Invalid curriculum_spec.json: {error}"])

    if int(spec.get("schema_version", 0)) < 4:
        errors.append("curriculum_spec.json must use schema_version 4 or later")

    expected_sessions = int(spec["canonical_sessions"])
    expected_packets = int(spec["canonical_packets"])
    canonical_set = set(range(1, expected_sessions + 1))
    phases = spec["phases"]

    covered: list[int] = []
    launcher_sessions: list[int] = []
    packets: set[Path] = set()
    for phase in phases:
        start = int(phase["start"])
        end = int(phase["end"])
        covered.extend(range(start, end + 1))
        folder = MISSIONS / str(phase["path"])
        launcher = folder / "SESSION_LAUNCHER.md"
        if not launcher.exists():
            errors.append(f"Missing launcher declared by spec: {launcher.relative_to(ROOT)}")
            continue

        local: list[int] = []
        for line in launcher.read_text(encoding="utf-8").splitlines():
            match = SESSION_ROW.match(line)
            if not match:
                continue
            session = int(match.group(1))
            local.append(session)
            launcher_sessions.append(session)
            for target in LOCAL_MD_LINK.findall(line):
                resolved = (launcher.parent / target).resolve()
                if resolved.exists():
                    packets.add(resolved)
        if local != list(range(start, end + 1)):
            errors.append(f"Spec/launcher mismatch for {phase['path']}: expected {start}-{end}, found {local}")

    if covered != list(range(1, expected_sessions + 1)):
        errors.append("Phase ranges must cover every canonical Session exactly once")
    if launcher_sessions != covered:
        errors.append("Launcher Session order does not match curriculum_spec.json")
    if len(packets) != expected_packets:
        errors.append(f"Canonical packet count mismatch: spec={expected_packets}, repository={len(packets)}")

    pathways = spec.get("pathways", {})
    required_pathways = {"noai_round1", "noai_round2", "ioai_full"}
    if set(pathways) != required_pathways:
        errors.append(f"Pathway keys must be exactly {sorted(required_pathways)}")

    for name, pathway in pathways.items():
        sessions = [int(value) for value in pathway["sessions"]]
        expected_count = int(pathway["expected_count"])
        document = ROOT / pathway["document"]
        if len(sessions) != expected_count:
            errors.append(f"{name}: expected_count={expected_count}, actual={len(sessions)}")
        if len(sessions) != len(set(sessions)):
            errors.append(f"{name}: duplicate Session IDs")
        invalid = sorted(set(sessions) - canonical_set)
        if invalid:
            errors.append(f"{name}: Sessions outside canonical range: {invalid}")
        if not document.exists():
            errors.append(f"Missing executable pathway document: {pathway['document']}")
            continue

        text = document.read_text(encoding="utf-8")
        for marker in ("## Exact Session Route", "## Exit Standard", "## Capability Boundary"):
            if marker not in text:
                errors.append(f"{pathway['document']} missing required section: {marker}")
        try:
            documented = exact_route_sessions(document)
        except ValueError as error:
            errors.append(f"{pathway['document']}: {error}")
            documented = []
        if documented != sessions:
            errors.append(f"{name}: documented route does not match curriculum_spec.json")

        recovery = [int(value) for value in pathway.get("recovery_sessions", [])]
        if not set(recovery).issubset(set(sessions)):
            errors.append(f"{name}: recovery_sessions must be included in the route")
        required_name = pathway.get("requires_pathway")
        if required_name:
            if required_name not in pathways:
                errors.append(f"{name}: unknown requires_pathway {required_name}")
            else:
                overlap = set(sessions) & set(pathways[required_name]["sessions"])
                if overlap:
                    errors.append(f"{name}: continuation repeats prior-pathway Sessions: {sorted(overlap)}")

    round1 = [int(value) for value in pathways.get("noai_round1", {}).get("sessions", [])]
    if 57 not in round1 or 58 not in round1 or round1.index(57) > round1.index(58):
        errors.append("NOAI Round 1 must complete Session 57 before Session 58")

    round2 = pathways.get("noai_round2", {})
    if [int(value) for value in round2.get("recovery_sessions", [])] != [32, 47]:
        errors.append("NOAI Round 2 recovery bridge must be Sessions 32 and 47")

    ioai = [int(value) for value in pathways.get("ioai_full", {}).get("sessions", [])]
    if ioai != list(range(1, expected_sessions + 1)):
        errors.append("IOAI full pathway must contain Sessions 1–78 exactly once and in order")
    if round1:
        expected_recovery = [session for session in range(1, 59) if session not in set(round1)]
        declared_recovery = [
            int(value)
            for value in pathways.get("ioai_full", {}).get("recovery_sessions_from_noai_round1", [])
        ]
        if declared_recovery != expected_recovery:
            errors.append("IOAI compressed-route recovery set does not match actual Round 1 omissions")

    checkpoints = spec.get("workflow_checkpoints", [])
    checkpoint_sessions = [int(item["session"]) for item in checkpoints]
    if checkpoint_sessions != sorted(set(checkpoint_sessions)):
        errors.append("workflow_checkpoints must use unique ascending Session IDs")
    if set(checkpoint_sessions) - canonical_set:
        errors.append("workflow_checkpoints contain Sessions outside the canonical range")

    expected_tools = {
        "progress_manager",
        "progress_report",
        "pathway_planner",
        "daily_drill_generator",
    }
    if set(spec.get("operational_tools", {})) != expected_tools:
        errors.append(f"Operational tool keys must be exactly {sorted(expected_tools)}")
    for tool_name, relative in spec.get("operational_tools", {}).items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing operational tool {tool_name}: {relative}")
        elif "--self-test" not in path.read_text(encoding="utf-8"):
            errors.append(f"Operational tool lacks --self-test support: {relative}")

    validate_progress_contract(spec, errors)
    scenario_count, repeat_window = validate_recognition_contract(spec, errors)

    required_readiness_markers = {
        "10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md": "NOT QUALIFIED until this record is completed",
        "10_Ready_to_Teach_Pack/External_Access_Verification_Record.md": "NOT VERIFIED until this record is completed",
        "09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md": "NO PILOT CLAIM may be made until real delivery evidence is recorded",
        "10_Ready_to_Teach_Pack/IOAI_2026_Post_Event_Review.md": "Status: pending official post-event evidence",
    }
    for relative, marker in required_readiness_markers.items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing readiness boundary document: {relative}")
        elif marker not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative} missing explicit evidence boundary")

    if errors:
        return fail(errors)

    print("Curriculum specification validation passed.")
    print(f"Canonical Sessions: {expected_sessions}")
    print(f"Canonical packets: {expected_packets}")
    print("Exact pathway routes and continuation dependencies: valid")
    print("Student progress schema v2, migration, privacy, and one-set-per-date rules: valid")
    print("Operational progress, report, planning, and daily-drill tools: present")
    print(f"Model-recognition scenario bank: {scenario_count} unique scenarios")
    print(f"Recent-repeat window: {repeat_window} scenario assignments")
    print("Five-set dual-threshold eligibility, secured confirmation, and maintenance rules: valid")
    print("Repository evidence and real-world evidence boundaries: explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
