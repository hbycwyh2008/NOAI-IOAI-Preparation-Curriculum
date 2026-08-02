from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = MISSIONS / "_Lesson_Library"

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
    "Talk Robin 1",
    "Entry Check",
    "Core Pattern",
    "Guided Practice",
    "Independent Rebuild",
    "Talk Robin 2",
    "Evidence",
)

SPECIAL_LONG_OR_CONFERENCE_FILES = {
    "15-round-1-exam-training/lesson-04.md",
    "25-past-paper-reproduction/lesson-01.md",
    "25-past-paper-reproduction/lesson-02.md",
    "25-past-paper-reproduction/lesson-03.md",
    "26-mock-contests/lesson-01.md",
    "26-mock-contests/lesson-02.md",
    "26-mock-contests/lesson-03.md",
    "26-mock-contests/lesson-04.md",
    "26-mock-contests/lesson-05-mock-correction-retake-readiness.md",
    "28-competition-sprint-task-data-tuning/lesson-08-full-sprint-simulation.md",
}

REQUIRED_FILES = (
    "00_Course_Overview/README.md",
    "00_Course_Overview/Course_Map.md",
    "00_Course_Overview/Pacing_Guide.md",
    "00_Course_Overview/Detailed_Lesson_Sequence.md",
    "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md",
    "00_Course_Overview/Curriculum_Completeness_Audit.md",
    "02_Class_Missions/_Curriculum_Governance/Class_Mission_Resource_Architecture.md",
    "02_Class_Missions/00_Orientation_and_Evidence/README.md",
    "02_Class_Missions/01_CS50P_Python/README.md",
    "02_Class_Missions/02_NumPy_Pandas_Visualisation/README.md",
    "02_Class_Missions/03_Bohrium_ML_Foundations/README.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/README.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-01-what-counts-as-intelligence.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-02-neural-networks-and-ai-cycles.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-03-how-machines-recognise-images.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-04-what-did-the-model-learn.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-05-reward-games-and-reinforcement-learning.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-06-language-processing-and-understanding.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-07-common-sense-abstraction-and-analogy.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-08-how-intelligent-is-ai.md",
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/README.md",
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Math_Intuition_Map.md",
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Model_Recognition_Routine.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/README.md",
    "02_Class_Missions/07_Model_Comparison_EDA_Evaluation/README.md",
    "02_Class_Missions/08_Tuning_Ensembling_Competition/README.md",
    "02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Optional_Automated_Tuning_Extension.md",
    "03_Templates/Competition_Sprint_Experiment_Log_Template.md",
    "03_Templates/Competition_Sprint_Model_Ensembling_Record.md",
    "03_Templates/Competition_Sprint_Submission_Checklist.md",
    "05_Resources/CS50P_edX_Timestamp_Map.md",
    "06_Starter_Code/ready_to_teach/competition_sprint_experiment_log.py",
    "06_Starter_Code/ready_to_teach/manual_tuning_template.py",
    "06_Starter_Code/ready_to_teach/model_ensembling_template.py",
    "06_Starter_Code/ready_to_teach/optuna_tuning_template.py",
    "09_Teacher_Planning/Phase_Overviews/README.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_8_Competition_Sprint.md",
    "09_Teacher_Planning/Public_Repo_100_Percent_Readiness_Definition.md",
    "09_Teacher_Planning/Teacher_Key_Private_Repo_Manifest.md",
    "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
    "10_Ready_to_Teach_Pack/Phase_8_Competition_Sprint.md",
    "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md",
    "MANIFEST.md",
    "scripts/v1_chunks/README.md",
)

PRECLASS_DELIVERY_FILES = {
    "01-python-foundations/lesson-01.md": "Pre-class required viewing",
    "01-python-foundations/lesson-02.md": "Pre-class required viewing",
    "01-python-foundations/lesson-03-function-decomposition-tracing.md": "Pre-class required viewing",
    "01-python-foundations/lesson-04-modules-imports-docs.md": "Pre-class required viewing",
    "01-python-foundations/lesson-05-debugging-evidence.md": "Pre-class required viewing",
    "01-python-foundations/lesson-06-round1-python-code-reading.md": "Pre-class review",
    "06-linear-regression/lesson-02.md": "Pre-class required viewing",
    "07-logistic-regression/lesson-02.md": "Pre-class required viewing",
    "11-trees-and-ensembles/lesson-02.md": "Pre-class required viewing",
    "12-neural-network-foundations/lesson-02.md": "Pre-class required viewing",
    "28-competition-sprint-task-data-tuning/lesson-05-classical-model-tuning.md": "Pre-class required viewing",
    "28-competition-sprint-task-data-tuning/lesson-06-deep-learning-tuning.md": "Pre-class required viewing",
    "28-competition-sprint-task-data-tuning/Optional_Automated_Tuning_Extension.md": "Pre-class required viewing",
}

PATH_REFERENCE_FILES = (
    "10_Ready_to_Teach_Pack/DLS_Selected_Content_Map.md",
    "10_Ready_to_Teach_Pack/HandsOnML_PyTorch_Selected_Content_Map.md",
)

BANNED_VISIBLE_RESOURCE_LABELS = (
    "Andrew Ng MLS",
    "DLS Course",
    "LHY-ML",
    "DLAI-PT",
)

LINK_PATTERN = re.compile(r"\(([^)]+\.md(?:#[^)]+)?)\)")
CODE_PATH_PATTERN = re.compile(r"`([^`\n]+\.md)`")
DURATION_PATTERN = re.compile(r"\*\*(?:Class duration|Duration):\*\*", re.IGNORECASE)


def lesson_files(folder: Path) -> list[Path]:
    return sorted(folder.rglob("lesson-*.md"))


def linked_lesson_files(module_folder: Path) -> set[Path]:
    linked: set[Path] = set()
    for readme in module_folder.rglob("README.md"):
        text = readme.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target:
                continue
            resolved = (readme.parent / target).resolve()
            if resolved.name.startswith("lesson-") and resolved.suffix == ".md":
                linked.add(resolved)
    return linked


def validate_module(module: str, expected: int, errors: list[str]) -> int:
    folder = LIBRARY / module
    if not folder.exists():
        errors.append(f"Missing module folder: {module}")
        return 0

    files = lesson_files(folder)
    if len(files) != expected:
        errors.append(f"{module}: expected {expected} lesson files, found {len(files)}")

    actual = {path.resolve() for path in files}
    linked = linked_lesson_files(folder)

    for path in sorted(linked - actual):
        errors.append(f"Broken lesson link in {module}: {path}")
    for path in sorted(actual - linked):
        errors.append(
            f"Lesson file is not linked from a README in {module}: {path.relative_to(ROOT)}"
        )

    for path in files:
        relative = path.relative_to(LIBRARY).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if not lines or not lines[0].startswith("# "):
            errors.append(f"Missing H1 title: {relative}")
        if not DURATION_PATTERN.search(text):
            errors.append(f"Missing explicit duration: {relative}")
        if "Evidence" not in text and "evidence" not in text:
            errors.append(f"Missing evidence requirement: {relative}")

        if relative in SPECIAL_LONG_OR_CONFERENCE_FILES:
            continue

        for marker in FLOW_MARKERS:
            if marker not in text:
                errors.append(f"Missing classroom-flow marker '{marker}': {relative}")

        if "## Timeline" not in text and "## 1. Skill Warm-Up" not in text:
            errors.append(f"Missing timeline or numbered seven-step flow: {relative}")

    return len(files)


def require_text(path: str, markers: tuple[str, ...], errors: list[str]) -> None:
    file_path = ROOT / path
    if not file_path.exists():
        errors.append(f"Missing required document: {path}")
        return
    text = file_path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            errors.append(f"'{marker}' not found in {path}")


def resolve_code_path(document: Path, raw_path: str) -> Path | None:
    raw_path = raw_path.strip()
    if "://" in raw_path or "/" not in raw_path:
        return None

    candidate = Path(raw_path)
    if raw_path.startswith("../") or raw_path.startswith("./"):
        return (document.parent / candidate).resolve()

    first = candidate.parts[0]
    if first in EXPECTED_MAINLINE_COUNTS or first == RESOURCE_HUB:
        return (LIBRARY / candidate).resolve()

    return (ROOT / candidate).resolve()


def validate_selected_content_paths(errors: list[str]) -> None:
    for relative in PATH_REFERENCE_FILES:
        document = ROOT / relative
        if not document.exists():
            errors.append(f"Missing selected-content map: {relative}")
            continue
        text = document.read_text(encoding="utf-8")
        for raw_path in CODE_PATH_PATTERN.findall(text):
            resolved = resolve_code_path(document, raw_path)
            if resolved is not None and not resolved.exists():
                errors.append(f"Broken referenced path in {relative}: {raw_path}")


def validate_preclass_delivery(errors: list[str]) -> None:
    for relative, marker in PRECLASS_DELIVERY_FILES.items():
        path = LIBRARY / relative
        if not path.exists():
            errors.append(f"Missing pre-class-delivery lesson: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            errors.append(f"Missing '{marker}' delivery label: {relative}")
        if "0–8 min" not in text:
            errors.append(f"Missing eight-minute in-class warm-up boundary: {relative}")


def validate_naming(errors: list[str]) -> None:
    for path in MISSIONS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for label in BANNED_VISIBLE_RESOURCE_LABELS:
            if label in text:
                errors.append(
                    f"Unexpanded course/resource label '{label}': {path.relative_to(ROOT)}"
                )


def validate_legacy_boundaries(errors: list[str]) -> None:
    obsolete_workflow = ROOT / ".github/workflows/build-complete-course-v1.yml"
    if obsolete_workflow.exists():
        errors.append("Obsolete destructive V1 builder workflow still exists")

    legacy_readme = ROOT / "scripts/v1_chunks/README.md"
    if not legacy_readme.exists():
        errors.append("Legacy V1 chunks are not marked inert with a README")
    else:
        text = legacy_readme.read_text(encoding="utf-8")
        if "must not be used to rebuild or overwrite" not in text:
            errors.append("Legacy V1 chunk boundary is not explicit")


def validate_exact_timestamp_map(errors: list[str]) -> None:
    path = ROOT / "05_Resources/CS50P_edX_Timestamp_Map.md"
    if not path.exists():
        errors.append("Missing Harvard Python timestamp map")
        return
    text = path.read_text(encoding="utf-8")
    if "–end" in text or "-end" in text:
        errors.append("Harvard Python timestamp map still contains an open-ended range")
    for marker in ("00:52:55–01:20:47", "01:10:06–01:17:28", "pre-class"):
        if marker not in text:
            errors.append(f"Harvard Python timestamp map missing '{marker}'")


def main() -> int:
    errors: list[str] = []

    mainline_total = sum(
        validate_module(module, expected, errors)
        for module, expected in EXPECTED_MAINLINE_COUNTS.items()
    )

    resource_total = validate_module(
        RESOURCE_HUB,
        EXPECTED_RESOURCE_HUB_COUNT,
        errors,
    )

    if mainline_total != EXPECTED_MAINLINE_TOTAL:
        errors.append(
            f"Expected {EXPECTED_MAINLINE_TOTAL} mainline lesson files, found {mainline_total}"
        )
    if mainline_total + resource_total != EXPECTED_PUBLIC_TOTAL:
        errors.append(
            f"Expected {EXPECTED_PUBLIC_TOTAL} total public lesson files, "
            f"found {mainline_total + resource_total}"
        )

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")

    validate_selected_content_paths(errors)
    validate_preclass_delivery(errors)
    validate_naming(errors)
    validate_legacy_boundaries(errors)
    validate_exact_timestamp_map(errors)

    require_text("README.md", ("78 sessions", "155 lessons", "Competition sprint"), errors)
    require_text(
        "00_Course_Overview/Pacing_Guide.md",
        ("78 sessions", "155 lessons", "70-Minute Bohrium Exception"),
        errors,
    )
    require_text(
        "00_Course_Overview/Detailed_Lesson_Sequence.md",
        ("78 scheduled sessions", "Phase 8 — Tuning, Ensembling, and Competition"),
        errors,
    )
    require_text(
        "00_Course_Overview/Course_Map.md",
        ("Phase", "75–78", "155 mainline lesson files", "16 Bohrium resource lessons"),
        errors,
    )
    require_text(
        "00_Course_Overview/Curriculum_Completeness_Audit.md",
        ("100% public file-structure coverage", "171", "Operational"),
        errors,
    )
    require_text("02_Class_Missions/README.md", ("CS50P", "Bohrium", "AI History", "Andrew Ng Machine Learning", "Andrew Ng Deep Learning", "Model Comparison"), errors)
    require_text(
        "02_Class_Missions/_Lesson_Library/shared/full-bohrium-video-classroom-flow.md",
        ("at least **five** pieces of evidence", "Named 70-Minute Exception"),
        errors,
    )
    require_text(
        "02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/README.md",
        ("pre-class preparation", "37 minutes", "43 minutes", "33 minutes"),
        errors,
    )
    require_text(
        "02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Optional_Automated_Tuning_Extension.md",
        ("Pre-class required viewing", "33 minutes", "0–8 min"),
        errors,
    )
    require_text(
        "03_Templates/Competition_Sprint_Model_Ensembling_Record.md",
        ("out-of-fold", "best single model"),
        errors,
    )
    require_text(
        "09_Teacher_Planning/Public_Repo_100_Percent_Readiness_Definition.md",
        ("100% public file-structure coverage", "Separate Readiness Decisions"),
        errors,
    )
    require_text(
        "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
        ("source of truth", "75 minutes", "180 minutes", "360 minutes"),
        errors,
    )
    require_text(
        "10_Ready_to_Teach_Pack/README.md",
        ("Phase_8_Competition_Sprint.md", "Curriculum_Readiness_Audit.md"),
        errors,
    )
    require_text(
        "10_Ready_to_Teach_Pack/Resource_Map_and_Syllabus_Crosswalk.md",
        ("Competition Sprint Crosswalk", "Optuna"),
        errors,
    )
    require_text(
        "MANIFEST.md",
        ("Repository Architecture Manifest", "171", "Canonical Source Priority"),
        errors,
    )

    if errors:
        print("Curriculum structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Curriculum structure validation passed.")
    print(f"Mainline lesson files: {mainline_total}")
    print(f"Optional Bohrium resource lesson files: {resource_total}")
    print(f"Total public lesson files: {mainline_total + resource_total}")
    print("Public file-structure and internal-consistency coverage: 100%")
    print("Operational, pilot, privacy, runtime, and annual-rule readiness remain separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())