from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/README.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-01-what-counts-as-intelligence.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-02-neural-networks-and-ai-cycles.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-03-how-machines-recognise-images.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-04-what-did-the-model-learn.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-05-reward-games-and-reinforcement-learning.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-06-language-processing-and-understanding.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-07-common-sense-abstraction-and-analogy.md",
    "02_Class_Missions/04_AI_History_and_Thinking_Humans/lesson-08-how-intelligent-is-ai.md",
    "03_Templates/AI_History_Reading_Evidence_Template.md",
    "04_Assessment/AI_History_Phase_Rubric.md",
    "09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md",
    "10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
    "10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md",
    "10_Ready_to_Teach_Pack/External_Access_Verification_Record.md",
    "10_Ready_to_Teach_Pack/Release_Readiness_Gates.md",
    "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md",
)

AUTHORITATIVE_MARKERS = {
    "README.md": ("78 sessions", "AI history", "embedded Kaggle practice"),
    "02_Class_Missions/README.md": (
        "Canonical 78-Session Route",
        "AI History and Thinking Humans",
        "41–58",
        "75–78",
    ),
    "00_Course_Overview/Course_Map.md": ("78 scheduled sessions", "33–40", "75–78"),
    "00_Course_Overview/Pacing_Guide.md": ("Total: 78 sessions", "AI History and Thinking Humans"),
    "00_Course_Overview/Detailed_Lesson_Sequence.md": (
        "78 scheduled sessions",
        "Phase 4 — AI History and Thinking Humans",
        "Kaggle Learn is embedded",
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
    "Phase 4 | 33–40 | Kaggle Learn workflow refresh",
)

LESSON_MARKERS = (
    "## Required Mastery",
    "## Misconceptions to Reject",
    "## Core Pattern",
    "## 70-Minute Learning Cycle",
    "## Exit Evidence",
    "## Gate",
)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


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
    print("Public readiness artifacts: present and internally consistent")
    print("Operational readiness remains cohort-, runtime-, security-, access-, and year-specific")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
