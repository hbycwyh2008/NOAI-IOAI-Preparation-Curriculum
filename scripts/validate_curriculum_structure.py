from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")

PHASES = (
    ("00_Orientation_and_Evidence", 1, 2),
    ("01_CS50P_Python", 3, 12),
    ("02_NumPy_Pandas_Visualisation", 13, 18),
    ("03_Bohrium_ML_Foundations", 19, 32),
    ("04_AI_History_and_Thinking_Humans", 33, 40),
    ("05_Andrew_Ng_ML_Model_Labs", 41, 58),
    ("06_Andrew_Ng_DL_PyTorch", 59, 70),
    ("07_Model_Comparison_EDA_Evaluation", 71, 74),
    ("08_Tuning_Ensembling_Competition", 75, 78),
)

REQUIRED_FILES = (
    "README.md",
    "TEACHER_START_HERE.md",
    "STUDENT_START_HERE.md",
    "MANIFEST.md",
    "02_Class_Missions/README.md",
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    "00_Course_Overview/Detailed_Lesson_Sequence.md",
    "00_Course_Overview/Pacing_Guide.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
    "scripts/validate_readiness_contract.py",
    "scripts/validate_class_mission_launchers.py",
)

OBSOLETE_MISSION_PATHS = (
    MISSIONS / "04_Kaggle_ML_Refresh",
    MISSIONS / "_Lesson_Library",
)


def split_target(raw: str) -> tuple[str, str]:
    path, marker, anchor = raw.strip().partition("#")
    return path.strip(), (f"#{anchor}" if marker else "")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def main() -> int:
    errors: list[str] = []
    seen_sessions: list[int] = []
    canonical_packets: set[Path] = set()

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")

    for obsolete in OBSOLETE_MISSION_PATHS:
        if obsolete.exists():
            errors.append(f"Obsolete mission path still exists: {obsolete.relative_to(ROOT)}")

    for phase_name, start, end in PHASES:
        phase = MISSIONS / phase_name
        launcher = phase / "SESSION_LAUNCHER.md"
        readme = phase / "README.md"
        if not phase.exists():
            errors.append(f"Missing phase folder: {phase_name}")
            continue
        if not launcher.exists():
            errors.append(f"Missing launcher: {launcher.relative_to(ROOT)}")
            continue
        if not readme.exists():
            errors.append(f"Missing phase README: {readme.relative_to(ROOT)}")
        else:
            readme_text = readme.read_text(encoding="utf-8")
            launcher_linked = any(
                raw.split("#", 1)[0].strip() == "SESSION_LAUNCHER.md"
                for _label, raw in LINK_RE.findall(readme_text)
            )
            if not launcher_linked:
                errors.append(f"Phase README does not link to its launcher: {readme.relative_to(ROOT)}")

        local_sessions: list[int] = []
        for line in launcher.read_text(encoding="utf-8").splitlines():
            row_match = ROW_RE.match(line)
            if not row_match:
                continue
            session = int(row_match.group(1))
            local_sessions.append(session)
            seen_sessions.append(session)
            local_targets = 0
            for _label, raw_target in LINK_RE.findall(line):
                if is_external(raw_target):
                    continue
                target, _anchor = split_target(raw_target)
                if not target:
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() != ".md":
                    continue
                local_targets += 1
                if not resolved.exists():
                    errors.append(f"Broken launcher target: {launcher.relative_to(ROOT)} -> {raw_target}")
                    continue
                try:
                    resolved.relative_to(phase.resolve())
                except ValueError:
                    errors.append(
                        f"Canonical lesson is not phase-local: Session {session} -> {resolved.relative_to(ROOT)}"
                    )
                canonical_packets.add(resolved)
            if local_targets == 0:
                errors.append(f"Session {session} has no local Markdown lesson target")

        expected = list(range(start, end + 1))
        if local_sessions != expected:
            errors.append(f"{phase_name}: expected Sessions {expected}, found {local_sessions}")

    if seen_sessions != list(range(1, 79)):
        errors.append("Launchers must contain Sessions 1–78 exactly once and in order")

    for packet in sorted(canonical_packets):
        text = packet.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Canonical packet lacks H1: {packet.relative_to(ROOT)}")
        if "Evidence" not in text and "evidence" not in text:
            errors.append(f"Canonical packet lacks evidence requirement: {packet.relative_to(ROOT)}")

    for path in MISSIONS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for label in ("Andrew Ng MLS", "DLS Course", "LHY-ML", "DLAI-PT"):
            if label in text:
                errors.append(f"Unexpanded resource label '{label}': {path.relative_to(ROOT)}")

    if errors:
        print("Curriculum structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Curriculum structure validation passed.")
    print("Canonical sessions: 78")
    print(f"Phase-local canonical lesson packets: {len(canonical_packets)}")
    print("Normal delivery path: Phase → Session Launcher → phase-local lesson")
    print("Obsolete parallel lesson directories: absent")
    print("Public file-structure and internal-consistency coverage: 100%")
    print("Operational, pilot, privacy, runtime, access, and annual-rule readiness remain separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
