# Public Assessment Index

These public rubrics, practice scenarios, and checklists define visible evidence expectations. Protected answers, hidden tests, fresh mastery sets, scoring packages, and calibration examples remain private.

## Daily Skill Systems

- [Model Recognition Daily Drills](Model_Recognition_Drills/README.md) — 36 public scenarios across foundation, mixed, and competition levels.
- [Model Recognition Answer Record](Model_Recognition_Drills/Answer_Record.md)
- [Model Recognition Teacher Key Protocol](Model_Recognition_Drills/Teacher_Key_Protocol.md)
- `scripts/generate_daily_model_drill.py` — deterministic answer-key-free five-scenario worksheet generation.

Generate a mixed set with:

```bash
python scripts/generate_daily_model_drill.py --date YYYY-MM-DD --level mixed
```

The Set ID is stable for the same date, level, and count. This supports auditable feedback and correction without publishing an answer key.

## Rubrics and Evidence

- [AI History and Thinking Humans — Phase Rubric](AI_History_Phase_Rubric.md)
- [Andrew ML Mathematics Bridge Rubric](Andrew_ML_Mathematics_Bridge_Rubric.md)
- [Evidence System](Evidence_System.md)
- [Mock Contest Rubric](Mock_Contest_Rubric.md)
- [Notebook Rubric](Notebook_Rubric.md)
- [Oral Explanation Rubric](Oral_Explanation_Rubric.md)
- [Readiness Checklist](Readiness_Checklist.md)
- [Round 1 Rubric](Round_1_Rubric.md)
- [Round 2 Rubric](Round_2_Rubric.md)

Public drill completion is practice evidence, not formal mastery by itself. Final mastery confirmation uses a fresh secured set stored outside the public repository.
