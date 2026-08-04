# Model Recognition Daily Drills

Use one scenario per study day for 15 minutes. These drills train task formalisation before model selection; they are not a keyword-matching quiz and they intentionally contain no public answer key.

## Daily Procedure

1. Read the scenario once without naming a model.
2. Complete every field in `Answer_Record.md`.
3. State the label availability and required output before naming the task family.
4. Choose the simplest valid baseline and one metric tied to the real error cost.
5. Name two reasonable model families and one likely failure mode for each.
6. Compare with teacher feedback, correct the reasoning, and record the correction cause.

## Levels

- [Level 1 — Foundations](Level_1_Foundations.md): 12 clear single-task scenarios.
- [Level 2 — Mixed and Ambiguous Tasks](Level_2_Mixed_Tasks.md): 12 scenarios with misleading keywords, groups, time, imbalance, or multiple plausible outputs.
- [Level 3 — Competition and Multimodal Tasks](Level_3_Competition_Tasks.md): 12 end-to-end, deep-learning, recommendation, generation, and IOAI-style scenarios.
- [Answer Record](Answer_Record.md): one reusable student response sheet.
- [Teacher Key Protocol](Teacher_Key_Protocol.md): private-key and feedback rules.

## Mastery Rule

Mastery requires all of the following:

- at least 90% task-family accuracy for five consecutive daily sets;
- no confusion between labels, features, output, metric, and model;
- a valid baseline and metric for at least 90% of scenarios;
- candidate models justified from data and output structure rather than keywords;
- one realistic limitation or leakage risk identified;
- corrections explain the reasoning error, not only the final category.

After mastery, continue two mixed maintenance drills per week. Any two task-family errors in one week return the student to daily practice.

## Scoring

Each scenario is scored out of 10:

| Component | Points |
|---|---:|
| sample, X, y, label availability | 2 |
| output and task family | 2 |
| baseline | 1 |
| metric and error-cost explanation | 2 |
| two candidate families | 1 |
| limitations, leakage, or validation risk | 2 |

The teacher stores detailed solutions, alternative acceptable answers, and calibration examples outside the public repository.
