# Model Recognition Daily Drills

Use one generated set per study day for approximately 15 minutes. These drills train task formalisation before model selection; they are not a keyword-matching quiz and intentionally contain no public answer key.

## Generate Today’s Set

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/YYYY-MM-DD.md
```

The generator reads the private schema-v2 progress ledger, avoids the most recent 15 scenario assignments when possible, and records one assignment per date. Rerunning a recorded date restores the same Set ID and scenarios; a different second assignment on that date is rejected.

Without `--progress`, selection remains deterministic but cannot use assignment history. Use `--history-window 0` only for a deliberate unrestricted diagnostic. Use `--level 1`, `--level 2`, or `--level 3` for targeted difficulty.

## Daily Procedure

1. Read each scenario once without naming a model.
2. Complete every reasoning field in the generated worksheet or `Answer_Record.md`.
3. State label availability and required output before naming the task family.
4. Choose the simplest valid baseline and one metric tied to the real error cost.
5. State a validation design that respects groups, time, repeated entities, or shift.
6. Name two reasonable model families and one likely failure mode for each.
7. Identify one leakage, distribution-shift, or submission risk.
8. Compare with teacher feedback, correct the reasoning, and record the correction cause.
9. Record reviewed task-family accuracy, baseline/metric accuracy, and total score.

## Levels

- [Level 1 — Foundations](Level_1_Foundations.md): 12 clear single-task scenarios.
- [Level 2 — Mixed and Ambiguous Tasks](Level_2_Mixed_Tasks.md): 12 scenarios with misleading keywords, groups, time, imbalance, or multiple plausible outputs.
- [Level 3 — Competition and Multimodal Tasks](Level_3_Competition_Tasks.md): 12 end-to-end, deep-learning, recommendation, generation, and IOAI-style scenarios.
- [Answer Record](Answer_Record.md): one reusable student response sheet.
- [Teacher Key Protocol](Teacher_Key_Protocol.md): private-key and feedback rules.

## Review and Score

```bash
python scripts/manage_student_progress.py score-drill \
  --path student-progress/student-001.json \
  --set-id 0123456789 \
  --task-family-accuracy 0.9 \
  --baseline-metric-accuracy 0.9 \
  --score-percent 90
```

- task-family accuracy is a fraction from 0 to 1;
- baseline/metric accuracy is a fraction from 0 to 1;
- total score is a percentage from 0 to 100.

Detailed reasoning, correction notes, and recheck dates remain in the worksheet or answer record. Protected solutions and calibration material remain outside the public repository.

## Public Eligibility Rule

A set qualifies for the public streak only when:

- teacher review is complete;
- task-family accuracy is at least 90%;
- baseline/metric accuracy is at least 90%.

The student needs five qualifying reviewed sets in a row. A high total score cannot compensate for either failed accuracy dimension. Migrated legacy records with missing baseline/metric accuracy remain visible but cannot count toward the streak until properly rescored.

Generate the current status report with:

```bash
python scripts/report_student_progress.py \
  --progress student-progress/student-001.json \
  --output reports/student-001-progress.md
```

## Private Confirmation Rule

The five-set public streak creates eligibility only. After the streak, administer a fresh private secured mixed set. If it passes, record only the result date:

```bash
python scripts/manage_student_progress.py confirm-recognition \
  --path student-progress/student-001.json \
  --date YYYY-MM-DD
```

The confirmation date must be on or after the latest qualifying public set. Never store secured questions, protected answers, hidden labels, or detailed keys in the ledger.

## Maintenance Rule

After confirmed mastery, complete two qualifying mixed maintenance sets per seven-day window. The progress report marks maintenance due after a full week when fewer than two qualifying mixed sets appear in the current window. Any material regression returns the student to targeted or daily practice.

## Scoring

Each scenario is scored out of 12:

| Component | Points |
|---|---:|
| sample, X, y, label availability | 2 |
| output and task family | 2 |
| baseline | 1 |
| metric and error-cost explanation | 2 |
| validation design | 1 |
| two candidate families | 1 |
| limitations, leakage, shift, or submission risk | 3 |

The teacher stores detailed solutions, alternative acceptable answers, secured sets, and calibration examples outside the public repository.

## Tool Validation

```bash
python scripts/manage_student_progress.py --self-test
python scripts/report_student_progress.py --self-test
python scripts/generate_daily_model_drill.py --self-test
```

The self-tests verify schema migration, score ranges, one-set-per-date integrity, dual-threshold streak calculation, secured-confirmation order, maintenance status, recent-repeat avoidance, mixed-level coverage, and answer-key-free output.
