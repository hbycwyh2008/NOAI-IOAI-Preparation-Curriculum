# Student Start Here

Your teacher assigns one documented route, one Phase, and one Session at a time.

```text
confirm your assigned route
→ review your private progress report
→ open Class Missions and the assigned launcher
→ complete the lesson and evidence
→ update the mastery dashboard
→ record completion, Red debt, or recheck
```

Start at [Class Missions](02_Class_Missions/README.md). Canonical lessons are stored directly inside their numbered Phase folders. Your assigned route may be the NOAI Round 1 route, NOAI Round 2 project route, IOAI full-extension route, or the complete 78-Session route.

## Learning Route

```text
CS50P Python
→ NumPy / Pandas / visualisation
→ Bohrium ML foundations
→ AI history and critical reading
→ Andrew Ng ML mathematics + models + embedded practice
→ Andrew Ng DL + PyTorch
→ model comparison, EDA, features, and evaluation
→ tuning, ensembling, and competition
```

A compressed route does not mean random skipping. It lists exact Session IDs and explains what you will not yet be qualified to do. Round 1 completes Session 57 before Session 58. Students moving to Round 2 or IOAI may receive named recovery Sessions before continuing.

## Private Progress Ledger

Your teacher creates one schema-v2 JSON ledger in your private course repository. It uses a pseudonymous ID, not your name or email address. It records:

- completed Session attempts;
- unresolved Red Sessions;
- pathways that passed an inspected exit gate;
- one daily drill assignment per date;
- task-family accuracy;
- baseline/metric accuracy;
- total score percentage;
- whether and when the fresh private secured set passed.

The ledger helps generate assignments and reports, but it is not the evidence itself. Your notebook, code, explanation, tests, correction notes, and delayed recheck remain the evidence. Never place protected answers, credentials, hidden labels, or secured-set content in the ledger.

## Modeling Workflow

For every substantial modeling task, use this order:

```text
task formalisation
→ data quality
→ feature engineering
→ model selection and baseline
→ diagnosis and controlled tuning
→ ensembling
→ reproducibility check and postmortem
```

Use the [Workflow Competency Crosswalk](00_Course_Overview/Workflow_Competency_Crosswalk.md) to see the evidence required at each gate.

## Daily Model-Recognition Practice

Complete one generated five-scenario worksheet on every assigned study day:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/YYYY-MM-DD.md
```

Rerunning the same recorded date restores the same worksheet. A different second assignment on that date is rejected. The worksheet contains no public answer key. Do not edit the ledger to obtain an easier set or delete a difficult assignment.

Before naming a model, write:

- one row/sample;
- X/features and y/target;
- whether labels exist during training;
- the exact required output;
- task family;
- simplest valid baseline;
- metric and error cost;
- validation split;
- two candidate model families;
- leakage, shift, or failure risk;
- output/submission checks.

## Recognition Eligibility and Mastery

A daily set counts toward public eligibility only when teacher review records:

- task-family accuracy of at least 90%; and
- baseline/metric accuracy of at least 90%.

You need five qualifying reviewed sets in a row. That public streak does **not** award mastery. After the streak, you must pass a fresh private secured set that is not copied from the public bank. The teacher records only the pass date, not the protected questions or answers.

After confirmation, complete two qualifying mixed maintenance sets in each seven-day window. Memorising public scenarios is never mastery; you must explain and transfer the reasoning.

Your teacher can generate a report showing route progress, Red debt, pending review, current streak, secured-confirmation status, and maintenance due. The report is based only on the ledger and does not replace evidence inspection.

## Ordinary Class Cycle

1. Skill Warm-Up
2. Talk Robin 1
3. Entry Check
4. Core Pattern
5. Guided Practice
6. Independent Rebuild
7. Talk Robin 2 + Evidence
8. Mastery dashboard and progress update

Watching, reading, or running an example once is not completion. You must explain, reconstruct, test, modify, analyse errors, and record evidence.

## Mastery Record

Copy the [Student Mastery Dashboard](01_Student_Start/07_Mastery_Dashboard.md) into your own course repository. A mastery level counts only when it links to evidence that you can explain and reconstruct.

After each Session:

1. link the named evidence;
2. record your independence level from 0–4;
3. name the error or misconception you found;
4. record the correction and a future retrieval date;
5. ask whether the progress ledger should show complete, Red, or pending review.

## Special Evidence

- Sessions 33–40 require pre-class reading evidence from Melanie Mitchell’s book.
- Sessions 41–43 require equation, graph, hand-calculation, shape, and code translation evidence.
- Every model task begins by identifying sample, `X`, `y`, output, labels, baseline, metric, validation, and limitations.
- Sessions 71–74 must establish the pre-tuning evidence gate.
- Sessions 75–78 require diagnosis-first tuning, ensemble-diversity evidence, fresh-environment reproducibility, and a postmortem.

## First Steps

Open the [Student Setup and Evidence Index](01_Student_Start/README.md), complete the assigned setup records, copy the mastery dashboard and model-recognition answer record, confirm the location of your private progress ledger, generate today’s assigned worksheet, then open today’s Phase launcher.
