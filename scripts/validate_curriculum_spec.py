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
SCENARIO_HEADING = re.compile(r"^###\s+(?:Day|Scenario)\s+\d+\b", re.MULTILINE)


def fail(errors: list[str]) -> int:
    print("Curriculum specification validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main() -> int:
    errors: list[str] = []
    if not SPEC_PATH.exists():
        return fail(["Missing curriculum_spec.json"])

    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    expected_sessions = int(spec["canonical_sessions"])
    expected_packets = int(spec["canonical_packets"])
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

    for relative in spec["required_pathway_documents"]:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing executable pathway document: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in ("## Exact Session Route", "## Exit Standard", "## Capability Boundary"):
            if marker not in text:
                errors.append(f"{relative} missing required section: {marker}")

    recognition = spec["model_recognition"]
    routine = ROOT / recognition["routine"]
    drill_index = ROOT / recognition["drill_index"]
    if not routine.exists():
        errors.append(f"Missing model-recognition routine: {recognition['routine']}")
    if not drill_index.exists():
        errors.append(f"Missing model-recognition drill index: {recognition['drill_index']}")
    else:
        drill_root = drill_index.parent
        scenarios = 0
        for path in sorted(drill_root.glob("Level_*.md")):
            scenarios += len(SCENARIO_HEADING.findall(path.read_text(encoding="utf-8")))
        minimum = int(recognition["minimum_public_scenarios"])
        if scenarios < minimum:
            errors.append(f"Model-recognition scenarios below minimum: {scenarios} < {minimum}")

    required_readiness_markers = {
        "10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md": "NOT QUALIFIED until this record is completed",
        "10_Ready_to_Teach_Pack/External_Access_Verification_Record.md": "NOT VERIFIED until this record is completed",
        "09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md": "NO PILOT CLAIM may be made until real delivery evidence is recorded",
        "10_Ready_to_Teach_Pack/IOAI_2026_Post_Event_Review.md": "Status: pending official post-event evidence"
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
    print("Executable pathway documents: present")
    print("Model-recognition scenario bank: meets minimum")
    print("Repository evidence and real-world evidence boundaries: explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
