from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"

SPECIAL = {
    "15-round-1-exam-training/lesson-04.md": ("150 minutes", [
        ("0–5 min", "Rules and setup", "Confirm permitted resources and section timing."),
        ("5–105 min", "Timed Round 1 paper", "Complete independently under official-style conditions."),
        ("105–115 min", "Review pass", "Check unanswered items, calculations, and code traces."),
        ("115–120 min", "Submission", "Submit the untouched final paper."),
        ("120–135 min", "Initial error coding", "Mark knowledge, reasoning, calculation, and time errors."),
        ("135–150 min", "Correction plan", "Select the three highest-priority corrections."),
    ]),
    "25-past-paper-reproduction/lesson-01.md": ("180 minutes", []),
    "25-past-paper-reproduction/lesson-02.md": ("180 minutes", []),
    "25-past-paper-reproduction/lesson-03.md": ("180 minutes", []),
    "26-mock-contests/lesson-01.md": ("120 minutes", [
        ("0–5 min", "Rules and setup", "Confirm allowed materials and paper structure."),
        ("5–100 min", "Timed mock", "Complete the paper independently."),
        ("100–112 min", "Review pass", "Check calculations, code traces, and unanswered items."),
        ("112–120 min", "Submission", "Submit paper and timing log before discussion."),
    ]),
    "26-mock-contests/lesson-02.md": ("240 minutes", []),
    "26-mock-contests/lesson-03.md": ("360 minutes", []),
    "26-mock-contests/lesson-04.md": ("45 minutes per student", [
        ("0–5 min", "Evidence selection", "Identify strongest and weakest evidence."),
        ("5–15 min", "Oral defence", "Answer concept, mechanism, debugging, and transfer questions."),
        ("15–25 min", "Mock-performance review", "Review scores, timing, reliability, and recurring errors."),
        ("25–35 min", "Gap prioritisation", "Select no more than three high-impact gaps."),
        ("35–42 min", "Action plan", "Define tasks, dates, evidence, and success criteria."),
        ("42–45 min", "Commitment check", "Restate the plan and schedule the first checkpoint."),
    ]),
}

CODING_FOLDERS = {
    "01-python-foundations", "02-control-flow-and-data-structures",
    "03-libraries-sorting-searching", "16-numpy-pandas-matplotlib",
    "17-data-cleaning-feature-engineering", "18-sklearn-workflow",
    "19-pytorch-foundations", "20-computer-vision",
    "21-nlp-sequence-models", "22-audio-speech",
    "23-llm-generative-ai", "24-round-2-project-training",
}


def seven_step_flow(kind: str = "concept"):
    if kind == "coding":
        return "75 minutes", [
            ("0–8 min", "Skill Warm-Up", "Use a short code fragment, guide, or notebook cell to meet the idea."),
            ("8–15 min", "Talk Robin 1", "Pair discussion: what ran, what failed, and what is confusing."),
            ("15–22 min", "Entry Check", "Check basic understanding of values, shapes, APIs, or workflow before going deeper."),
            ("22–35 min", "Core Pattern", "Teacher explains the key coding method, pattern, or workflow clearly."),
            ("35–53 min", "Guided Practice", "Practice with teacher support. Ask questions, run checks, and improve."),
            ("53–67 min", "Independent Rebuild", "Recreate the pattern on your own with less help."),
            ("67–75 min", "Talk Robin 2 + Evidence", "Summarize, explain, and submit proof of learning."),
        ]
    if kind == "assessment":
        return "75 minutes", [
            ("0–8 min", "Skill Warm-Up", "Use a short mixed set or correction prompt to meet the idea."),
            ("8–15 min", "Talk Robin 1", "Pair discussion: what was solved and what is confusing."),
            ("15–22 min", "Entry Check", "Check basic understanding before timed or deeper work."),
            ("22–35 min", "Core Pattern", "Teacher explains the key reasoning, calculation, or distractor pattern clearly."),
            ("35–53 min", "Guided Practice", "Practice with teacher support. Ask questions and improve."),
            ("53–67 min", "Independent Rebuild", "Recreate the reasoning or solution pattern on your own with less help."),
            ("67–75 min", "Talk Robin 2 + Evidence", "Summarize, explain, and submit proof of learning."),
        ]
    return "75 minutes", [
        ("0–8 min", "Skill Warm-Up", "Use a video, guide, or task to meet the idea."),
        ("8–15 min", "Talk Robin 1", "Pair discussion: what was done and what is confusing."),
        ("15–22 min", "Entry Check", "Check basic understanding before we go deeper."),
        ("22–35 min", "Core Pattern", "Teacher explains the key method or pattern clearly."),
        ("35–53 min", "Guided Practice", "Practice with teacher support. Ask questions and improve."),
        ("53–67 min", "Independent Rebuild", "Recreate the pattern on your own with less help."),
        ("67–75 min", "Talk Robin 2 + Evidence", "Summarize, explain, and submit proof of learning."),
    ]


def long_timeline(minutes: int):
    if minutes == 180:
        return [
            ("0–15 min", "Task reading and rules", "Identify target, metric, files, constraints, and submission schema."),
            ("15–35 min", "Data audit", "Inspect shapes, labels, missing values, modality, and leakage risks."),
            ("35–60 min", "Baseline plan", "Choose the simplest valid method and validation design."),
            ("60–105 min", "Baseline build", "Produce the first working model and predictions."),
            ("105–120 min", "First submission check", "Validate order, shape, dtypes, and metric."),
            ("120–150 min", "Controlled improvement", "Run one justified improvement."),
            ("150–170 min", "Error analysis", "Inspect failures and select the next step."),
            ("170–180 min", "Submission and post-mortem", "Save notebook, predictions, experiment log, and reflection."),
        ]
    if minutes == 240:
        return [
            ("0–15 min", "Task reading", "Identify target, metric, files, constraints, and schema."),
            ("15–40 min", "Data audit and validation", "Inspect data and define a leakage-safe split."),
            ("40–90 min", "Baseline build", "Produce the first valid model and predictions."),
            ("90–105 min", "Submission validation", "Check order, shape, types, and local metric."),
            ("105–175 min", "Controlled experiments", "Run a limited set of justified improvements."),
            ("175–205 min", "Final training", "Train the selected model and generate predictions."),
            ("205–225 min", "Robustness checks", "Fresh-run critical cells and inspect edge cases."),
            ("225–240 min", "Submission and log", "Submit notebook, predictions, experiment table, and timing record."),
        ]
    return [
        ("0–20 min", "Task reading", "Identify modality, target, metric, files, constraints, and schema."),
        ("20–55 min", "Data/modality audit", "Inspect samples, labels, corrupt items, shapes, and leakage."),
        ("55–120 min", "First baseline", "Build the simplest valid structural or pretrained baseline."),
        ("120–140 min", "First submission check", "Validate and save a working submission."),
        ("140–245 min", "Controlled improvements", "Run prioritised experiments with written hypotheses."),
        ("245–300 min", "Final model", "Train the selected configuration and generate predictions."),
        ("300–330 min", "Error and robustness checks", "Inspect failures and fresh-run critical cells."),
        ("330–350 min", "Final submission", "Validate schema and submit final output."),
        ("350–360 min", "Post-mortem notes", "Record decisions, lost time, and immediate lessons."),
    ]


def timeline_for(relative: str):
    if relative in SPECIAL:
        duration, rows = SPECIAL[relative]
        if rows:
            return duration, rows
        minutes = int(duration.split()[0])
        return duration, long_timeline(minutes)
    folder = relative.split("/", 1)[0]
    if folder == "15-round-1-exam-training":
        return seven_step_flow("assessment")
    if folder in CODING_FOLDERS:
        return seven_step_flow("coding")
    return seven_step_flow("concept")


def render(duration: str, rows):
    lines = [f"**Duration:** {duration}", "", "## Timeline", "", "| Time | Block | Student output |", "|---|---|---|"]
    lines.extend(f"| {time} | {block} | {output} |" for time, block, output in rows)
    return "\n".join(lines)


def remove_existing_timeline(text: str) -> str:
    text = re.sub(r"\n?\*\*Duration:\*\*[^\n]*\n?", "\n", text, count=1)
    text = re.sub(r"\n## Timeline\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    return text.strip() + "\n"


def normalise(path: Path):
    relative = path.relative_to(MISSIONS).as_posix()
    original = remove_existing_timeline(path.read_text(encoding="utf-8"))
    lines = original.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing H1 title: {relative}")
    duration, rows = timeline_for(relative)
    updated = "\n".join([lines[0], "", render(duration, rows), ""] + lines[1:]).replace("\n\n\n", "\n\n")
    path.write_text(updated.strip() + "\n", encoding="utf-8")


def phase_for(folder: str) -> str:
    number = int(folder.split("-", 1)[0])
    if number == 0: return "Phase 0 — Setup"
    if number <= 3: return "Phase 1 — Python"
    if number <= 11: return "Phase 2 — AI and Machine Learning Foundations"
    if number <= 14: return "Phase 3 — Neural Networks"
    if number == 15: return "Phase 4 — Round 1 Training"
    if number <= 18: return "Phase 5 — Data and Scikit-learn"
    if number <= 23: return "Phase 6 — PyTorch and Domain Tasks"
    return "Phase 7 — Competition Practice"


def update_overview(paths):
    grouped = {}
    for path in paths:
        relative = path.relative_to(MISSIONS).as_posix()
        folder = relative.split("/", 1)[0]
        title = path.read_text(encoding="utf-8").splitlines()[0].split(" — ", 1)[-1]
        duration, _ = timeline_for(relative)
        grouped.setdefault(phase_for(folder), []).append((title, duration))

    sequence = ["# Detailed Lesson Sequence", "", f"The curriculum contains **{len(paths)} scheduled lessons/sessions**. Ordinary lessons use the seven-step 75-minute after-school club flow.", ""]
    count = 1
    for phase, items in grouped.items():
        sequence.extend([f"## {phase}", ""])
        for title, duration in items:
            sequence.append(f"{count}. **{title}** — {duration}")
            count += 1
        sequence.append("")
    (ROOT / "00_Course_Overview" / "Detailed_Lesson_Sequence.md").write_text("\n".join(sequence), encoding="utf-8")

    pacing = f"""# Pacing Guide

The repository contains **{len(paths)} scheduled lessons/sessions**.

- Standard concept and coding lessons: **75 minutes** using the seven-step after-school club classroom flow.
- Integrated Round 1 mock and correction: 150 minutes.
- Past-paper reproduction sessions: 180 minutes each.
- Timed Round 1 mock: 120 minutes.
- Timed Round 2 tabular mock: 240 minutes.
- Timed Round 2 multimodal mock: 360 minutes.
- Final readiness conference: 45 minutes per student.

Every ordinary lesson uses the same cycle: **Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**.

Long simulations must not be compressed into a nominal 75-minute club lesson.

See [Detailed Lesson Sequence](Detailed_Lesson_Sequence.md).
"""
    (ROOT / "00_Course_Overview" / "Pacing_Guide.md").write_text(pacing, encoding="utf-8")

    audit = f"""# Curriculum Completeness Audit

## Verified Structure

- Lesson/session files found: **{len(paths)}**.
- Ordinary lessons use the seven-step 75-minute after-school club classroom flow.
- Long mocks use realistic durations rather than a universal 75-minute claim.

## Still Required Before the Curriculum Is Fully Packaged

1. Exact video chapter/timestamp or page range for every required resource.
2. Actual student worksheets and question sets for every lesson.
3. Starter notebooks and datasets for every coding lesson.
4. Full teacher answer keys and scoring notes.
5. Authorised past-paper files or official links.
6. Link testing and fresh-runtime validation of starter code.
7. Complete mock-contest packages and hidden tests.
8. A line-by-line official-syllabus crosswalk to lessons and assessments.

The repository is currently a detailed course architecture plus ready-to-teach pack. Classroom delivery should follow the seven-step flow.
"""
    (ROOT / "00_Course_Overview" / "Curriculum_Completeness_Audit.md").write_text(audit, encoding="utf-8")


def main():
    paths = sorted(MISSIONS.glob("[0-9][0-9]-*/lesson-*.md"))
    if len(paths) != 67:
        raise SystemExit(f"Expected 67 lesson files, found {len(paths)}")
    for path in paths:
        normalise(path)
    update_overview(paths)


if __name__ == "__main__":
    main()
