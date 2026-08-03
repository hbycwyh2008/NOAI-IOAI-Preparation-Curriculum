# Cohort Mastery Review Protocol

Use this protocol to convert student evidence into instructional decisions. It does not replace Session assessments or formal competition-readiness gates. It creates a regular review cycle so that completion does not hide unresolved prerequisites.

## Review Cadence

Run a brief review after every three ordinary Sessions, at the end of each Phase, and at Sessions 18, 24, 41, 57, 58, 70, 74, 77, and 78.

Recommended rhythm:

```text
collect evidence
→ verify reconstruction
→ identify recurring misconceptions
→ group students by next need
→ assign one controlled intervention
→ recheck after spaced retrieval
```

## Evidence Sources

Use at least two evidence types before assigning a mastery level:

- student mastery dashboard;
- named Session evidence;
- independent rebuild;
- retrieval check completed after a delay;
- oral explanation or whiteboard trace;
- tests, data checks, or fresh-environment run;
- error log, experiment log, model card, or postmortem.

Self-report, attendance, watched-video completion, or a single successful run is not sufficient.

## Three Core Indicators

For each target skill, record:

1. **Completion:** Was the required artifact submitted and accessible?
2. **Reconstruction:** Can the student reproduce the central pattern without copying?
3. **Transfer:** Can the student choose and apply the skill in a changed task, explain tradeoffs, and identify limitations?

A student who has completion without reconstruction remains below independent mastery.

## Status Rules

| Status | Operational definition | Teacher action |
|---|---|---|
| Red | missing evidence, major misconception, or level 0–1 on a prerequisite | pause dependent advancement; assign a guided rebuild and immediate feedback |
| Amber | evidence exists but independence or transfer is inconsistent; level 2 | allow limited advancement with targeted retrieval and one controlled transfer task |
| Green | independent reconstruction and explanation; level 3 | advance and schedule spaced retrieval |
| Blue | reliable transfer under constraints; level 4 | extend complexity or use peer explanation after evidence verification |

Do not average away a Red prerequisite with unrelated strengths.

## Weekly Cohort Review

### Step 1 — Select the Few Skills That Matter

Choose no more than three current priority skills. Prefer prerequisite bottlenecks and recurring workflow decisions over isolated vocabulary.

Examples:

- distinguish samples, features, and target;
- decide whether labels exist and choose the learning paradigm;
- design a leakage-safe split;
- select a baseline and metric;
- change one experimental factor at a time;
- use errors to justify tuning;
- verify ensemble diversity.

### Step 2 — Verify a Sample, Not Just Submission Counts

For each priority skill:

- inspect every missing artifact;
- inspect all Red students;
- inspect a representative sample of Amber and Green evidence;
- run a short reconstruction check for students whose artifact quality and explanation do not match.

### Step 3 — Record Misconceptions Precisely

Use observable descriptions rather than broad labels such as “weak in ML.”

Good examples:

- treats the target column as an input feature;
- chooses classification because the prompt contains categories even though the output is continuous;
- uses random splitting despite repeated entities;
- fills missing values before the train/validation split;
- changes preprocessing and model family in one experiment;
- tunes a wide search space without a written diagnosis;
- ensembles highly correlated models and assumes model count guarantees improvement.

### Step 4 — Build the Intervention Queue

| Priority | Student or group | Blocking misconception | Evidence | Intervention | Recheck task | Due |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |

Interventions should be small and testable. Typical options:

- five-minute model-recognition drill;
- one annotated example followed by an independent rebuild;
- split-design comparison using the same dataset;
- feature ablation with a fixed baseline;
- error-slice analysis before any tuning;
- reproduce a result from a clean environment;
- oral explanation using `X`, `y`, output, labels, baseline, metric, and limitation.

### Step 5 — Recheck After Delay

Do not close an intervention because the student succeeds immediately with the example open. Recheck after a delay or with a changed task. Record the new evidence in the student dashboard.

## Phase Promotion Gate

Before a student enters the next Phase, confirm:

- all named prerequisite evidence is present;
- no Red prerequisite remains unresolved;
- at least one independent reconstruction has been verified;
- the student can state a limitation or failure mode;
- the next Phase can be attempted without substituting teacher prompts for missing foundations.

When schedule constraints require the class to move on, mark the student as **advancing with dependency debt** and assign a dated remediation plan. Do not relabel the prerequisite as mastered.

## Workflow Gate Reviews

Use the [Workflow Competency Crosswalk](../00_Course_Overview/Workflow_Competency_Crosswalk.md) to review the following gates:

### Sessions 17–18 — Data Quality Gate

Check data types, missingness, duplicates, invalid values, imbalance, leakage risks, and the connection between findings and decisions.

### Sessions 24–32 — Task and Baseline Gate

Check `X`, `y`, output type, label availability, task family, metric, and a defensible simple baseline.

### Sessions 41–58 — Classical-ML Integration Gate

Check equations and shapes, reproducible preprocessing, validation design, model comparison, controlled improvement, and postmortem.

### Sessions 59–70 — Deep-Learning Gate

Check tensor shapes, training-loop reconstruction, learning-curve interpretation, regularization decisions, and baseline-versus-deep justification.

### Sessions 71–74 — Pre-Tuning Gate

Require a trustworthy split, data audit, baseline, feature ledger, ablation, model comparison, and written error diagnosis before tuning begins.

### Sessions 75–78 — Competition Gate

Check bounded tuning, ensemble diversity, time management, submission validation, fresh-environment reproducibility, and evidence-backed postmortem.

## Cohort Dashboard Template

| Priority skill | Red count | Amber count | Green count | Blue count | Dominant misconception | Planned response | Recheck date |
|---|---:|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |

## Decision Rules

- When more than 25% of the cohort is Red on the same prerequisite, reteach the concept to the cohort using a different representation.
- When errors differ, use targeted groups instead of whole-class repetition.
- When submission completion is high but reconstruction is low, reduce new content and increase independent rebuild time.
- When validation scores rise but reasoning quality falls, audit leakage, split design, and uncontrolled experiments.
- When a student is consistently Green in familiar tasks but Amber in transfer, assign changed-context practice rather than more of the same exercise.
- When an ensemble is proposed, require evidence that component models are both strong and meaningfully different.

## End-of-Cycle Record

At the end of each Phase, save:

- cohort status counts;
- top three misconceptions;
- interventions used;
- recheck results;
- students advancing with dependency debt;
- changes recommended for the next delivery of the Phase.

The goal is not to produce more paperwork. The goal is to make the next instructional decision traceable to evidence.
