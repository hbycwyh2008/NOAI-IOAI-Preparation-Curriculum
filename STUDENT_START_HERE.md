# Student Start Here

Your teacher assigns one documented route, one Phase, and one Session at a time.

```text
confirm your assigned route
→ open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ complete the lesson and evidence
→ update the mastery dashboard
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

A compressed route does not mean random skipping. It lists exact Session IDs and explains what you will not yet be qualified to do. Round 1 completes Session 57 before the Session 58 checkpoint. Students moving to Round 2 or IOAI may receive named recovery Sessions before continuing.

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
  --output daily-drills/YYYY-MM-DD.md
```

The same date, level, and count produce the same Set ID, so corrections and rechecks can be verified. The worksheet contains no public answer key.

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

Mastery requires at least 90% for five consecutive daily sets and one fresh secured set. Memorising the public scenarios is not mastery; you must explain and transfer the reasoning.

## Ordinary Class Cycle

1. Skill Warm-Up
2. Talk Robin 1
3. Entry Check
4. Core Pattern
5. Guided Practice
6. Independent Rebuild
7. Talk Robin 2 + Evidence
8. Mastery dashboard update

Watching, reading, or running an example once is not completion. You must explain, reconstruct, test, modify, analyse errors, and record evidence.

## Mastery Record

Copy the [Student Mastery Dashboard](01_Student_Start/07_Mastery_Dashboard.md) into your own course repository. A mastery level counts only when it links to evidence that you can explain and reconstruct.

After each Session:

1. link the named evidence;
2. record your independence level from 0–4;
3. name the error or misconception you found;
4. record the correction and a future retrieval date.

## Special Evidence

- Sessions 33–40 require pre-class reading evidence from Melanie Mitchell’s book.
- Sessions 41–43 require equation, graph, hand-calculation, shape, and code translation evidence.
- Every model task begins by identifying sample, `X`, `y`, output, labels, baseline, metric, validation, and limitations.
- Sessions 71–74 must establish the pre-tuning evidence gate.
- Sessions 75–78 require diagnosis-first tuning, ensemble-diversity evidence, fresh-environment reproducibility, and a postmortem.

## First Steps

Open the [Student Setup and Evidence Index](01_Student_Start/README.md), complete the assigned setup records, copy the mastery dashboard and model-recognition answer record, generate today’s worksheet, then open today’s Phase launcher.
