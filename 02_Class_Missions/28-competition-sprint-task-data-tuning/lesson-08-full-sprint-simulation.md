# Lesson 08 — Full Competition Sprint Simulation and Postmortem

**Duration:** 150–360 minutes depending on the selected task. This is a special timed session, not an ordinary 75-minute lesson.

## Learning Target

Students can execute the complete competition-sprint workflow under a fixed time budget and make evidence-based decisions about task recognition, data engineering, and tuning.

## Required Resource

One unsolved or reset official NOAI / IOAI-style task selected by the teacher, with the current competition constraints reproduced as closely as possible.

## Timed Workflow

| Competition block | Required action | Evidence |
|---|---|---|
| First 15 minutes | task recognition | input/output/metric/constraint card |
| Next 20 minutes | data audit and split design | audit and leakage checklist |
| Next 30–60 minutes | end-to-end baseline | valid local score and submission-shaped output |
| Middle block | data engineering and controlled experiments | experiment table with one change per run |
| Tuning block | manual or limited automated tuning | justified search space and trial log |
| Final 30–45 minutes | error analysis, retraining decision, fresh run, submission check | final validation and submission record |

## Mandatory Checkpoints

### Checkpoint 1 — Before Coding

```text
Task type:
Input:
Output:
Metric:
Split unit:
Baseline:
Major constraint:
```

### Checkpoint 2 — Baseline Gate

Do not tune until all are true:

- code runs end to end;
- validation score is generated correctly;
- submission shape is correct;
- split is defensible;
- one error category has been inspected;
- runtime is known.

### Checkpoint 3 — Experiment Gate

Every experiment must record:

```text
Hypothesis:
Single controlled change:
Validation score:
Runtime:
Error-category effect:
Decision:
```

### Checkpoint 4 — Stop-Tuning Gate

Stop tuning when:

- remaining time threatens fresh-runtime validation;
- improvements are within noise;
- the search is no longer hypothesis-driven;
- the best model cannot be reproduced;
- submission-format or environment risk remains unresolved.

## Postmortem

Complete immediately after the simulation:

```text
1. Did I identify the task correctly?
2. Did the validation design match the hidden-test structure?
3. Which data-engineering action produced the largest gain?
4. Which tuning experiment had the best gain per minute?
5. Which experiment wasted the most time and why?
6. What error category remained largest?
7. Was the final model reproducible from a fresh runtime?
8. What is the single highest-value skill to retrain before the next mock?
```

## Required Evidence

- task-recognition card;
- data audit and split memo;
- baseline result;
- experiment and tuning log;
- error-analysis table;
- final configuration;
- fresh-runtime record;
- validated submission file;
- postmortem and next-practice decision.

## Readiness Standard

A student is competition-ready only when they can finish a valid baseline early, improve it through controlled evidence, and still reserve enough time for reproducibility and submission validation.