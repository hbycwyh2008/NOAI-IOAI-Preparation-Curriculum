from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AI_HISTORY_LESSONS = (
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-01-what-counts-as-intelligence.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-02-neural-networks-and-ai-cycles.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-03-how-machines-recognise-images.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-04-what-did-the-model-learn.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-05-reward-games-and-reinforcement-learning.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-06-language-processing-and-understanding.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-07-common-sense-abstraction-and-analogy.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-08-how-intelligent-is-ai.md",
)

CANONICAL_TEACHER_OVERVIEWS = (
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_0_Orientation_and_Evidence.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_1_CS50P_Python.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_2_NumPy_Pandas_Visualisation.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_3_Bohrium_ML_Foundations.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_4_AI_History_and_Thinking_Humans.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_5_Andrew_Ng_ML_Model_Labs.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_6_Andrew_Ng_DL_PyTorch.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_7_Model_Comparison_EDA_Evaluation.md",
    "09_Teacher_Planning/Phase_Overviews/Canonical_Phase_8_Tuning_Ensembling_Competition.md",
)

REQUIRED_FILES = (
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/README.md",
    *AI_HISTORY_LESSONS,
    "03_Templates/AI_History_Reading_Evidence_Template.md",
    "04_Assessment/AI_History_Phase_Rubric.md",
    "05_Resources/Kaggle_Learn_Refresh_Map.md",
    "09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md",
    "09_Teacher_Planning/Phase_Overviews/README.md",
    *CANONICAL_TEACHER_OVERVIEWS,
    "10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
    "10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md",
    "10_Ready_to_Teach_Pack/External_Access_Verification_Record.md",
    "10_Ready_to_Teach_Pack/Release_Readiness_Gates.md",
    "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md",
)

AUTHORITATIVE_MARKERS = {
    "README.md": ("78 sessions", "AI history", "embedded Kaggle practice"),
    "MANIFEST.md": ("Sessions 1–78", "validate_readiness_contract.py", "embedded Kaggle practice"),
    "02_Class_Missions/README.md": (
        "Canonical 78-Session Route",
        "AI History and Thinking Humans",
        "41–58",
        "75–78",
    ),
    "02_Class_Missions/_Curriculum_Governance/Class_Mission_Resource_Architecture.md": (
        "AI History and Thinking Humans",
        "embedded workflow rehearsal inside Andrew ML model labs",
        "78 scheduled sessions",
    ),
    "02_Class_Missions/_Curriculum_Governance/Lesson_Distribution_Audit.md": (
        "78 scheduled sessions across nine phases",
        "eight AI History seminars",
        "171 total reusable public lesson/resource files",
    ),
    "00_Course_Overview/README.md": (
        "Detailed 78-Session Sequence",
        "AI History and Thinking Humans",
        "embedded Kaggle practice",
    ),
    "00_Course_Overview/Course_Map.md": ("78 scheduled sessions", "33–40", "75–78"),
    "00_Course_Overview/Pacing_Guide.md": ("Total: 78 sessions", "AI History and Thinking Humans"),
    "00_Course_Overview/Detailed_Lesson_Sequence.md": (
        "78 scheduled sessions",
        "Phase 4 — AI History and Thinking Humans",
        "Kaggle Learn is embedded",
    ),
    "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md": (
        "Sessions 1–78",
        "AI History and Thinking Humans",
        "selected embedded practice inside Andrew ML model labs",
    ),
    "00_Course_Overview/Expanded_Lesson_Architecture.md": (
        "78-session canonical pathway",
        "Eight scheduled AI History seminars",
        "171 reusable public lesson/resource files",
    ),
    "00_Course_Overview/Curriculum_Completeness_Audit.md": (
        "Canonical scheduled pathway | 78 sessions",
        "100% public file-structure and internal-consistency coverage",
        "validate_readiness_contract.py",
    ),
    "05_Resources/Kaggle_Learn_Refresh_Map.md": (
        "Kaggle Learn is not a separate scheduled phase",
        "Embedded Practice Touchpoints",
        "| 57 | integrated tabular workflow",
    ),
    "08_Public_Documents/Competition_Pathway.md": (
        "canonical 78-session dependency path",
        "AI history and critical reading through Melanie Mitchell",
        "Sessions 75–78",
    ),
    "09_Teacher_Planning/75min_After_School_Club_Implementation.md": (
        "AI History reading seminars are named 70-minute exceptions",
        "Sessions 33–40",
        "Representative_Pilot_Matrix.md",
    ),
    "09_Teacher_Planning/Phase_Overviews/README.md": (
        "Sessions 1–78",
        "Canonical_Phase_4_AI_History_and_Thinking_Humans.md",
        "Legacy Thematic Summaries",
    ),
    "10_Ready_to_Teach_Pack/README.md": (
        "canonical 78-session pathway",
        "AI History and Thinking Humans",
        "Phase_4_AI_History_and_Thinking_Humans.md",
    ),
    "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md": (
        "Canonical scheduled pathway | 78",
        "100% public file-structure and internal-consistency coverage",
        "Real classroom evidence | Not complete",
    ),
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md": (
        "100% public file-structure and internal-consistency coverage",
        "must not state “100% operationally ready”",
    ),
}

BANNED_AUTHORITATIVE_TEXT = (
    "Canonical 75-Session",
    "Detailed 75-Session Sequence",
    "75 scheduled sessions",
    "Sessions 1–75",
    "Recommended full pathway | 75 sessions",
    "67 core sessions plus eight competition-sprint sessions",
    "Kaggle workflow refresh\n→ Andrew Ng ML",
    "Phase 4 | 33–40 | Kaggle Learn workflow refresh",
    "Kaggle Learn | required short workflow refresh",
    "five-session workflow refresh after the Bohrium foundation sequence",
    "| 33 | Pandas:",
)

LESSON_MARKERS = (
    "## Required Mastery",
    "## Misconceptions to Reject",
    "## Core Pattern",
    "## 70-Minute Learning Cycle",
    "## Exit Evidence",
    "## Gate",
)

OVERVIEW_MARKERS = (
    "## Purpose",
    "## Entry Conditions",
    "## Delivery Priorities",
    "## Required Evidence",
    "## Exit Gate",
)


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing readiness-contract file: {relative}")

    obsolete = ROOT / "02_Class_Missions/04_Kaggle_ML_Refresh"
    if obsolete.exists():
        errors.append("Obsolete standalone Kaggle Phase 04 still exists")

    for relative, markers in AUTHORITATIVE_MARKERS.items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing authoritative document: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"Missing '{marker}' in {relative}")
        for banned in BANNED_AUTHORITATIVE_TEXT:
            if banned in text:
                errors.append(f"Stale pathway text '{banned}' in {relative}")

    phase = ROOT / "02_Class_Missions/04_AI_History_and_Thinking_Humans"
    lesson_files = sorted(phase.glob("lesson-*.md")) if phase.exists() else []
    if len(lesson_files) != 8:
        errors.append(f"Expected 8 AI History lesson files, found {len(lesson_files)}")

    for path in lesson_files:
        text = path.read_text(encoding="utf-8")
        for marker in LESSON_MARKERS:
            if marker not in text:
                errors.append(f"Missing '{marker}': {path.relative_to(ROOT)}")
        if "**Class duration:** 70 minutes" not in text:
            errors.append(f"Missing 70-minute duration: {path.relative_to(ROOT)}")
        if "Required reading before class" not in text:
            errors.append(f"Missing pre-class reading assignment: {path.relative_to(ROOT)}")

    for relative in CANONICAL_TEACHER_OVERVIEWS:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in OVERVIEW_MARKERS:
            if marker not in text:
                errors.append(f"Missing '{marker}': {relative}")
        if "**Sessions:**" not in text or "**Canonical folder:**" not in text:
            errors.append(f"Missing session or canonical-folder metadata: {relative}")

    teacher_pack = ROOT / "10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md"
    if teacher_pack.exists():
        text = teacher_pack.read_text(encoding="utf-8")
        for marker in (
            "Required Teacher Preparation",
            "Session Map",
            "Phase Gate",
            "Reteaching Triggers",
            "Representative_Pilot_Matrix.md",
        ):
            if marker not in text:
                errors.append(f"Missing '{marker}' in Phase 4 teacher pack")

    rubric = ROOT / "04_Assessment/AI_History_Phase_Rubric.md"
    if rubric.exists():
        text = rubric.read_text(encoding="utf-8")
        for marker in ("24/32", "Task Formalisation", "Claim and Evidence", "Capability–Limitation Analysis"):
            if marker not in text:
                errors.append(f"Missing '{marker}' in AI History rubric")

    dashboard = ROOT / "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md"
    if dashboard.exists():
        text = dashboard.read_text(encoding="utf-8")
        if "External Evidence Still Required" not in text:
            errors.append("Readiness dashboard does not preserve external evidence gates")

    if errors:
        print("Readiness contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Readiness contract validation passed.")
    print("Canonical pathway: 78 sessions")
    print("AI History phase: 8 complete English seminars")
    print("Canonical teacher overviews: 9")
    print("High-traffic pathway documents: current and internally consistent")
    print("Kaggle practice map: embedded in Andrew ML model labs")
    print("Public readiness artifacts: present and internally consistent")
    print("Operational readiness remains cohort-, runtime-, security-, access-, and year-specific")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
