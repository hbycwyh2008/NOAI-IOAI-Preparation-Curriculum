from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"

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

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SESSION_ROW = re.compile(r"^\|\s*(\d+)\s*\|", re.MULTILINE)


def internal_link_errors(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split()[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(
                f"Broken internal link in {path.relative_to(ROOT)}: {raw_target}"
            )
    return errors


def main() -> int:
    errors: list[str] = []

    usage = MISSIONS / "HOW_TO_USE_CLASS_MISSIONS.md"
    if not usage.exists():
        errors.append("Missing 02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md")
    else:
        usage_text = usage.read_text(encoding="utf-8")
        for marker in (
            "Teachers and students should **not browse `_Lesson_Library` manually**",
            "→ open SESSION_LAUNCHER.md",
            "Source-of-Truth Rule",
        ):
            if marker not in usage_text:
                errors.append(f"Missing usage marker '{marker}'")
        errors.extend(internal_link_errors(usage))

    mission_readme = MISSIONS / "README.md"
    if not mission_readme.exists():
        errors.append("Missing 02_Class_Missions/README.md")
    else:
        text = mission_readme.read_text(encoding="utf-8")
        for marker in (
            "Class Missions — Start Here",
            "Do not browse `_Lesson_Library`",
            "Canonical 78-Session Route",
        ):
            if marker not in text:
                errors.append(f"Missing Class Missions marker '{marker}'")
        errors.extend(internal_link_errors(mission_readme))

    observed_sessions: list[int] = []

    for phase_name, start, end in PHASES:
        phase = MISSIONS / phase_name
        readme = phase / "README.md"
        launcher = phase / "SESSION_LAUNCHER.md"

        if not readme.exists():
            errors.append(f"Missing phase README: {readme.relative_to(ROOT)}")
            continue
        if not launcher.exists():
            errors.append(f"Missing session launcher: {launcher.relative_to(ROOT)}")
            continue

        readme_text = readme.read_text(encoding="utf-8")
        if "## Start Here" not in readme_text:
            errors.append(f"Phase README lacks Start Here: {readme.relative_to(ROOT)}")
        if "SESSION_LAUNCHER.md" not in readme_text:
            errors.append(f"Phase README does not link launcher: {readme.relative_to(ROOT)}")
        if "## Lesson Library" in readme_text or "## Lesson Library Modules" in readme_text:
            errors.append(f"Phase README still exposes library navigation: {readme.relative_to(ROOT)}")
        errors.extend(internal_link_errors(readme))

        launcher_text = launcher.read_text(encoding="utf-8")
        for marker in ("Open this lesson", "Required evidence", "Phase Gate"):
            if marker not in launcher_text:
                errors.append(
                    f"Launcher missing '{marker}': {launcher.relative_to(ROOT)}"
                )

        sessions = [int(value) for value in SESSION_ROW.findall(launcher_text)]
        expected = list(range(start, end + 1))
        if sessions != expected:
            errors.append(
                f"Launcher session rows incorrect for {phase_name}: "
                f"expected {expected}, found {sessions}"
            )
        observed_sessions.extend(sessions)
        errors.extend(internal_link_errors(launcher))

    expected_all = list(range(1, 79))
    if observed_sessions != expected_all:
        errors.append(
            "Canonical launcher coverage is not exactly Sessions 1–78 in order: "
            f"found {observed_sessions}"
        )

    if errors:
        print("Class Missions launcher validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Class Missions launcher validation passed.")
    print("Canonical launcher coverage: Sessions 1–78 exactly once")
    print("Phase folders: 9")
    print("Normal delivery path: Phase → Session Launcher → exact lesson")
    print("Manual Lesson Library browsing: not required")
    print("Launcher and Phase README internal links: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
