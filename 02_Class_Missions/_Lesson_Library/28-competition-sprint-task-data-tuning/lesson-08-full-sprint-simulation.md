# Lesson 08 — Full Competition Sprint Simulation and Postmortem

**Duration:** 150–360 minutes depending on the selected task. This is a special timed session, not an ordinary 75-minute lesson.

## Learning Target

Students can execute the complete competition workflow under a fixed time budget and make evidence-based decisions in the correct order:

```text
Task definition
→ data quality
→ feature engineering
→ model selection and baseline
→ error analysis
→ tuning
→ model ensembling when justified
→ fresh-runtime and submission validation
```

## Required Resource

One unsolved or reset official NOAI / IOAI-style task selected by the teacher, with current competition constraints reproduced as closely as possible.

## Timed Workflow

| Competition block | Required action | Evidence |
|---|---|---|
| First 10–15 minutes | formalise task, metric, prediction-time boundary, and constraints | task card |
| Next 20–30 minutes | audit data, choose split, test leakage, freeze validation | quality report and split memo |
| Next 20–40 minutes | build minimum reproducible preprocessing and feature pipeline | pipeline record and raw-feature reference |
| Next 30–60 minutes | run constant/rule, simple, and contrasting baselines | model-comparison table and valid submission-shaped output |
| Middle block | inspect error categories and run controlled feature/model experiments | experiment log with one named change per run |
| Tuning block | manual diagnosis-first tuning; optional limited automated search | parameter log, search rationale, runtime record |
| Fusion block | compare strong models and test simple averaging/voting or OOF stacking when justified | diversity table and best-single-versus-ensemble comparison |
| Final 30–45 minutes | freeze system, fresh run, schema/order checks, and submission validation | final configuration and submission record |

## Mandatory Checkpoints

### Checkpoint 1 — Task Definition Before Modelling

```text
Task type:
Input X:
Target/output y:
Metric and direction:
Prediction-time boundary:
Independent unit:
Major constraint:
Submission schema:
```

### Checkpoint 2 — Data-Quality Gate

Do not engineer features or compare models until all are true:

- split unit and method are defensible;
- obvious target, duplicate, group, identity, temporal, and preprocessing leakage have been checked;
- labels, IDs, row order, missingness, duplicates, and distribution are recorded;
- validation is frozen and expected to resemble the hidden test.

### Checkpoint 3 — Feature-Pipeline Gate

Do not compare model families until all are true:

- training and inference use the same reproducible pipeline;
- every learned transform is fitted on training data only;
- a minimum/raw feature version exists;
- each added feature group has a hypothesis and a validation test.

### Checkpoint 4 — Baseline and Model-Selection Gate

Do not tune until all are true:

- constant or rule baseline preserved;
- simple trainable baseline completed;
- at least one contrasting model evaluated under the same protocol;
- train and validation scores, spread, runtime, and memory are recorded;
- one major error category or diagnosed limitation is identified;
- submission-shaped predictions can be generated.

### Checkpoint 5 — Controlled Experiment Gate

Every feature, model, or tuning experiment must record:

```text
Hypothesis:
Single named change:
Everything held fixed:
Validation result and spread:
Runtime/memory effect:
Error-category effect:
Decision:
```

### Checkpoint 6 — Ensemble Gate

Do not ensemble unless all are true:

- at least two single models are independently strong;
- predictions exist on identical held-out rows or as valid OOF predictions;
- error overlap or prediction correlation has been inspected;
- the best single model remains the comparison reference;
- simple averaging or voting is tested before stacking;
- any stacking meta-model is trained only on OOF predictions.

### Checkpoint 7 — Stop-Complexity Gate

Stop feature search, tuning, or ensembling when:

- remaining time threatens fresh-runtime validation;
- improvements are within validation noise;
- the next action is no longer hypothesis-driven;
- the best system cannot be reproduced;
- runtime, memory, checkpoint, or submission risk is unresolved;
- a simpler system has nearly equal performance with lower risk.

## Postmortem

Complete immediately after the simulation:

```text
1. Did I formalise X, y, metric, prediction-time boundary, and constraints correctly?
2. Did the data audit reveal any issue that should have changed the plan earlier?
3. Did the validation design match the hidden-test structure?
4. Which feature group produced the largest reliable gain?
5. Which model family gave the largest reliable gain over the simple baseline?
6. Which error category directed the highest-value tuning action?
7. Which tuning experiment had the best gain per minute?
8. Were candidate models complementary enough for ensembling?
9. Did the ensemble beat the best single model by more than validation noise?
10. Which experiment wasted the most time and why?
11. Was the final system reproducible from a fresh runtime?
12. What is the single highest-value skill to retrain before the next mock?
```

## Required Evidence

- task-definition card;
- data-quality audit, frozen split, and leakage memo;
- reproducible preprocessing/feature pipeline;
- raw-feature reference and at least one feature ablation;
- constant/rule, simple, and contrasting model results;
- error-analysis table;
- controlled feature and tuning log;
- optional automated-search rationale when used;
- saved held-out or OOF predictions for any ensemble;
- best-single-model versus ensemble comparison;
- final configuration;
- fresh-runtime record;
- validated submission file;
- postmortem and next-practice decision.

## Readiness Standard

A student is competition-ready only when they can:

- protect validation quality before chasing score;
- build a valid baseline early;
- improve data and features before increasing model complexity;
- tune only a diagnosed model limitation;
- ensemble only strong, complementary models;
- stop complexity early enough to preserve reproducibility and submission reliability.