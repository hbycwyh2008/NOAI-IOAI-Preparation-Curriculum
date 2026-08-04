# Model Recognition Daily Drills

Use one generated set per study day for approximately 15 minutes. These drills train task formalisation before model selection; they are not a keyword-matching quiz and they intentionally contain no public answer key.

## Generate Today’s Set

The default creates a deterministic five-scenario mixed set:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed
```

To save the worksheet:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --output daily-drills/YYYY-MM-DD.md
```

The same date, level, and count produce the same Set ID and scenario selection. This makes feedback, resubmission, and teacher records auditable. Use `--level 1`, `--level 2`, or `--level 3` for targeted difficulty.

## Daily Procedure

1. Read each scenario once without naming a model.
2. Complete every reasoning field in the generated worksheet or `Answer_Record.md`.
3. State label availability and required output before naming the task family.
4. Choose the simplest valid baseline and one metric tied to the real error cost.
5. State a validation design that respects groups, time, repeated entities, or shift.
6. Name two reasonable model families and one likely failure mode for each.
7. Identify one leakage, distribution-shift, or submission risk.
8. Compare with teacher feedback, correct the reasoning, and record the correction cause.

## Levels

- [Level 1 — Foundations](Level_1_Foundations.md): 12 clear single-task scenarios.
- [Level 2 — Mixed and Ambiguous Tasks](Level_2_Mixed_Tasks.md): 12 scenarios with misleading keywords, groups, time, imbalance, or multiple plausible outputs.
- [Level 3 — Competition and Multimodal Tasks](Level_3_Competition_Tasks.md): 12 end-to-end, deep-learning, recommendation, generation, and IOAI-style scenarios.
- [Answer Record](Answer_Record.md): one reusable student response sheet.
- [Teacher Key Protocol](Teacher_Key_Protocol.md): private-key and feedback rules.

## Mastery Rule

Mastery requires all of the following:

- at least 90% task-family accuracy for five consecutive daily sets;
- no confusion between labels, features, output, metric, validation, and model;
- a valid baseline and metric for at least 90% of scenarios;
- candidate models justified from data and output structure rather than keywords;
- one realistic limitation plus one leakage or shift risk identified;
- corrections explain the reasoning error, not only the final category;
- a fresh secured mixed set confirms the result.

After mastery, continue two mixed maintenance sets per week. Any two task-family errors in one week return the student to daily practice.

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

The teacher stores detailed solutions, alternative acceptable answers, and calibration examples outside the public repository.

## Tool Validation

```bash
python scripts/generate_daily_model_drill.py --self-test
```

The self-test verifies deterministic selection, unique scenarios, mixed-level coverage, minimum bank size, and answer-key-free output.
