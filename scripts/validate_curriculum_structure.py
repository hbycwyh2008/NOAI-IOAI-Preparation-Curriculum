from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"

EXPECTED_MAINLINE_COUNTS = {
    "00-course-overview": 2,
    "01-python-foundations": 6,
    "02-control-flow-and-data-structures": 6,
    "03-libraries-sorting-searching": 5,
    "04-ai-foundations-and-ethics": 4,
    "05-learning-paradigms": 6,
    "06-linear-regression": 4,
    "07-logistic-regression": 4,
    "08-statistics-probability-distance": 5,
    "09-model-evaluation": 6,
    "10-generalization-regularization": 4,
    "11-trees-and-ensembles": 4,
    "12-neural-network-foundations": 6,
    "13-backprop-optimization": 6,
    "14-cnn-foundations": 6,
    "15-round-1-exam-training": 10,
    "16-numpy-pandas-matplotlib": 6,
    "17-data-cleaning-feature-engineering": 6,
    "18-sklearn-workflow": 6,
    "19-pytorch-foundations": 7,
    "20-computer-vision": 6,
    "21-nlp-sequence-models": 6,
    "22-audio-speech": 5,
    "23-llm-generative-ai": 5,
    "24-round-2-project-training": 7,
    "25-past-paper-reproduction": 4,
    "26-mock-contests": 5,
    "28-competition-sprint-task-data-tuning": 8,
}

RESOURCE_HUB = "27-official-bohrium-video-lessons"
EXPECTED_RESOURCE_HUB_COUNT = 16
EXPECTED_MAINLINE_TOTAL = 155
EXPECTED_PUBLIC_TOTAL = 171

FLOW_MARKERS = (
    "Skill Warm-Up",
    "Entry Check",
    "Core Pattern",
    "Guided Practice",
    "Independent Rebuild",
    "Evidence",
)

SPECIAL_LONG_OR_CONFERENCE_FILES = {
    "15-round-1-exam-training/lesson-04.md",
    "25-past-paper-reproduction/lesson-01.md",
    "25-past-paper-reproduction/lesson-02.md",
    "25-past-paper-reproduction/lesson-03.md",
    "25-past-paper-reproduction/lesson-04-postmortem-and-transfer.md",
    "26-mock-contests/lesson-01.md",
    "26-mock-contests/lesson-02.md",
    "26-mock-contests/lesson-03.md",
    "26-mock-contests/lesson-04.md",
    "26-mock-contests/lesson-05-mock-correction-retake-readiness.md",
    "28-competition-sprint-task-data-tuning/lesson-08-full-sprint-simulation.md",
}

LINK_PATTERN = re.compile(r"\(([^)]+\.md)\)")


def lesson_files(folder: Path) -> list[Path]:
    return sorted(folder.rglob("lesson-*.md"))


def markdown_links(readme: Path) -> set[Path]:
    linked: set[Path] = set()
    text = readme.read_text(encoding="utf-8")
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.split("#", 1)[0].strip()
        if not target or "://" in target:
            continue
        resolved = (readme.parent / target).resolve()
        if resolved.name.startswith("lesson-") and resolved.suffix == ".md":
            linked.add(resolved)
    return linked


def validate_module_links(module: str, errors: list[str]) -> None:
    folder = MISSIONS / module
    actual = {path.resolve() for path in lesson_files(folder)}
    linked: set[Path] = set()
    for readme in folder.rglob("README.md"):
        linked.update(markdown_links(readme))

    missing_targets = sorted(path for path in linked if not path.exists())
    orphaned = sorted(actual - linked)

    for path in missing_targets:
        errors.append(f"Broken lesson link in {module}: {path}")
    for path in orphaned:
        errors.append(f"Lesson file is not linked from a README in {module}: {path.relative_to(ROOT)}")


def validate_lesson_content(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(MISSIONS).as_posix()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or not lines[0].startswith("# "):
        errors.append(f"Missing H1 title: {relative}")

    if "Evidence" not in text and "evidence" not in text:
        errors.append(f"Missing evidence requirement: {relative}")

    if relative in SPECIAL_LONG_OR_CONFERENCE_FILES:
        return

    for marker in FLOW_MARKERS:
        if marker not in text:
            errors.append(f"Missing classroom-flow marker '{marker}': {relative}")


def require_text(path: str, required: tuple[str, ...], errors: list[str]) -> None:
    file_path = ROOT / path
    if not file_path.exists():
        errors.append(f"Missing required document: {path}")
        return

    text = file_path.read_text(encoding="utf-8")
    for marker in required:
        if marker not in text:
            errors.append(f"'{marker}' not found in {path}")


def main() -> int:
    errors: list[str] = []

    mainline_total = 0
    for module, expected in EXPECTED_MAINLINE_COUNTS.items():
        folder = MISSIONS / module
        if not folder.exists():
            errors.append(f"Missing module folder: {module}")
            continue

        files = lesson_files(folder)
        actual = len(files)
        mainline_total += actual
        if actual != expected:
            errors.append(f"{module}: expected {expected} lesson files, found {actual}")

        validate_module_links(module, errors)
        for path in files:
            validate_lesson_content(path, errors)

    resource_folder = MISSIONS / RESOURCE_HUB
    resource_files = lesson_files(resource_folder) if resource_folder.exists() else []
    if len(resource_files) != EXPECTED_RESOURCE_HUB_COUNT:
        errors.append(
            f"{RESOURCE_HUB}: expected {EXPECTED_RESOURCE_HUB_COUNT} lesson files, "
            f"found {len(resource_files)}"
        )
    else:
        validate_module_links(RESOURCE_HUB, errors)

    public_total = mainline_total + len(resource_files)
    if mainline_total != EXPECTED_MAINLINE_TOTAL:
        errors.append(
            f"Expected {EXPECTED_MAINLINE_TOTAL} mainline lesson files, found {mainline_total}"
        )
    if public_total != EXPECTED_PUBLIC_TOTAL:
        errors.append(
            f"Expected {EXPECTED_PUBLIC_TOTAL} total public lesson files, found {public_total}"
        )

    require_text(
        "README.md",
        ("75 sessions", "155 lessons", "Competition sprint"),
        errors,
    )
    require_text(
        "00_Course_Overview/Pacing_Guide.md",
        ("75 sessions", "155 lessons", "70-Minute Bohrium Exception"),
        errors,
    )
    require_text(
        "00_Course_Overview/Detailed_Lesson_Sequence.md",
        ("75 scheduled sessions", "Phase 8 — Competition Sprint"),
        errors,
    )
    require_text(
        "02_Class_Missions/README.md",
        ("28 — Competition Sprint",),
        errors,
    )
    require_text(
        "10_Ready_to_Teach_Pack/README.md",
        ("Phase_8_Competition_Sprint.md", "Curriculum_Readiness_Audit.md"),
        errors,
    )
    require_text(
        "10_Ready_to_Teach_Pack/Resource_Map_and_Syllabus_Crosswalk.md",
        ("Competition Sprint Crosswalk", "Hyperparameter Optimization with Optuna"),
        errors,
    )

    if errors:
        print("Curriculum structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Curriculum structure validation passed.")
    print(f"Mainline lesson files: {mainline_total}")
    print(f"Optional Bohrium resource lesson files: {len(resource_files)}")
    print(f"Total public lesson files: {public_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
