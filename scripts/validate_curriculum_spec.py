from __future__ import annotations

import json
import re
import sys
from pathlib import Path

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


def main() -> int:
    errors: list[str] = []
    if not SPEC_PATH.exists():
        return fail(["Missing curriculum_spec.json"])

    try:
        spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return fail([f"Invalid curriculum_spec.json: {error}"])

    if int(spec.get("schema_version", 0)) < 2:
        errors.append("curriculum_spec.json must use schema_version 2 or later")

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
        errors.append("Phase ranges in curriculum_spec.json must cover every canonical Session exactly once")
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
            errors.append(f"{name}: duplicate Session IDs in curriculum_spec.json")
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
            errors.append(
                f"{name}: documented Exact Session Route does not match curriculum_spec.json; "
                f"document={documented}, spec={sessions}"
            )

        recovery = [int(value) for value in pathway.get("recovery_sessions", [])]
        if not set(recovery).issubset(set(sessions)):
            errors.append(f"{name}: recovery_sessions must be included in the pathway route")

        required_name = pathway.get("requires_pathway")
        if required_name:
            if required_name not in pathways:
                errors.append(f"{name}: unknown requires_pathway {required_name}")
            else:
                overlap = set(sessions) & set(pathways[required_name]["sessions"])
                if overlap:
                    errors.append(f"{name}: continuation repeats prior-pathway Sessions: {sorted(overlap)}")

    if "noai_round1" in pathways:
        round1 = [int(value) for value in pathways["noai_round1"]["sessions"]]
        if 57 not in round1 or 58 not in round1 or round1.index(57) > round1.index(58):
            errors.append("NOAI Round 1 must complete Session 57 before Session 58")

    if "noai_round2" in pathways:
        round2 = pathways["noai_round2"]
        if [int(value) for value in round2.get("recovery_sessions", [])] != [32, 47]:
            errors.append("NOAI Round 2 recovery bridge must be Sessions 32 and 47")

    if "ioai_full" in pathways:
        ioai = [int(value) for value in pathways["ioai_full"]["sessions"]]
        if ioai != list(range(1, expected_sessions + 1)):
            errors.append("IOAI full pathway must contain Sessions 1–78 exactly once and in order")
        if "noai_round1" in pathways:
            round1_set = set(int(value) for value in pathways["noai_round1"]["sessions"])
            expected_recovery = [session for session in range(1, 59) if session not in round1_set]
            declared_recovery = [
                int(value) for value in pathways["ioai_full"].get("recovery_sessions_from_noai_round1", [])
            ]
            if declared_recovery != expected_recovery:
                errors.append(
                    "IOAI recovery_sessions_from_noai_round1 must equal the exact Sessions 1–58 omitted by Round 1"
                )

    checkpoints = spec.get("workflow_checkpoints", [])
    checkpoint_sessions = [int(item["session"]) for item in checkpoints]
    if checkpoint_sessions != sorted(set(checkpoint_sessions)):
        errors.append("workflow_checkpoints must use unique ascending Session IDs")
    if set(checkpoint_sessions) - canonical_set:
        errors.append("workflow_checkpoints contain Sessions outside the canonical range")

    for tool_name, relative in spec.get("operational_tools", {}).items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing operational tool {tool_name}: {relative}")
        elif "--self-test" not in path.read_text(encoding="utf-8"):
            errors.append(f"Operational tool lacks --self-test support: {relative}")

    recognition = spec["model_recognition"]
    routine = ROOT / recognition["routine"]
    drill_index = ROOT / recognition["drill_index"]
    if not routine.exists():
        errors.append(f"Missing model-recognition routine: {recognition['routine']}")
    if not drill_index.exists():
        errors.append(f"Missing model-recognition drill index: {recognition['drill_index']}")

    scenario_ids: list[str] = []
    global_scenario_numbers: list[int] = []
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
        global_scenario_numbers.extend(numbers)
        scenario_ids.extend(f"L{level}-D{number:02d}" for number in numbers)
        if numbers:
            expected_local = list(range(numbers[0], numbers[0] + len(numbers)))
            if numbers != expected_local:
                errors.append(f"Scenario numbering must be internally consecutive in {relative}: {numbers}")

    minimum = int(recognition["minimum_public_scenarios"])
    if scenario_count < minimum:
        errors.append(f"Model-recognition scenarios below minimum: {scenario_count} < {minimum}")
    if global_scenario_numbers != list(range(1, scenario_count + 1)):
        errors.append(
            "Model-recognition scenario files must collectively cover one globally consecutive sequence from Day 1"
        )
    if len(scenario_ids) != len(set(scenario_ids)):
        errors.append("Model-recognition scenario IDs are not unique")
    if int(recognition.get("daily_set_size", 0)) < 1:
        errors.append("model_recognition.daily_set_size must be at least 1")

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
    print("Operational planning and daily-drill tools: present")
    print(f"Model-recognition scenario bank: {scenario_count} unique scenarios, globally numbered 1-{scenario_count}")
    print("Repository evidence and real-world evidence boundaries: explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
