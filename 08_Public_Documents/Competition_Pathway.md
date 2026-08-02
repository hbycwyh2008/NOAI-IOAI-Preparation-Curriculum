# NOAI / IOAI Competition Preparation Pathway

The curriculum develops competition readiness through the canonical 78-session dependency path rather than asking students to jump directly into advanced models.

```text
orientation and evidence habits
→ CS50P Python
→ NumPy, Pandas, and visualisation
→ Bohrium machine-learning foundations
→ AI history and critical reading through Melanie Mitchell
→ Andrew Ng Machine Learning
   + StatQuest
   + 3Blue1Brown
   + embedded Kaggle practice
   + model recognition
   + typical tasks
→ Andrew Ng Deep Learning + PyTorch + domain tasks
→ model comparison + EDA + feature engineering + evaluation
→ diagnosis-first tuning + ensembling + competition simulation
```

## Canonical Scheduled Pathway

| Phase | Sessions | Competition contribution |
|---:|---:|---|
| 0 | 1–2 | environment, evidence, Git, and responsible assistance |
| 1 | 3–12 | Python code reading, tracing, testing, debugging, and programs |
| 2 | 13–18 | data inspection, transformation, and visual reasoning |
| 3 | 19–32 | Chinese-language machine-learning concept foundation |
| 4 | 33–40 | AI history, claim auditing, understanding, and limitations |
| 5 | 41–58 | classical models, maths intuition, task recognition, and tabular workflows |
| 6 | 59–70 | PyTorch, image, text, audio, and multimodal tasks |
| 7 | 71–74 | model comparison, EDA, features, validation, metrics, and error analysis |
| 8 | 75–78 | tuning, ensembling, full simulation, and postmortem |

Students preparing for a narrower competition stage may use a cohort-specific shortened route, but no public overview may redefine the canonical session numbering.

## Competition Integration

Competition habits begin early:

- define the real task, input `X`, output or target `y`, metric, prediction-time boundary, constraints, and submission schema;
- inspect data quality and prevent target, duplicate, identity, group, temporal, and preprocessing leakage;
- preserve a simple baseline under one validation protocol;
- keep feature generation reproducible;
- compare model families from evidence;
- analyse errors before tuning;
- record every controlled experiment;
- validate final artifacts from a fresh environment.

## Final Competition Phase

Sessions 75–78 focus on:

1. diagnosis-first tuning and controlled search;
2. model ensembling with valid held-out or out-of-fold predictions;
3. a full competition simulation from task reading to valid submission;
4. a postmortem and readiness decision based on evidence.

The reusable eight-lesson competition-sprint bank remains available for deeper practice under `02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/`. It is not an additional automatic eight-session block after Session 78.

## Fixed Modelling Order

```text
data quality
→ valid split and baseline
→ feature engineering
→ model selection
→ error diagnosis
→ tuning
→ model ensembling
→ fresh-runtime submission validation
```

Optuna and broad automated search are optional extensions after a manual tuning cycle. They do not replace model understanding, validation independence, reproducibility, or submission checks.

## Core Principle

A sophisticated model is not competition-ready unless the student can:

- explain the task and prediction-time boundary;
- defend data quality and validation;
- reproduce the feature pipeline;
- preserve and beat a simple baseline under one protocol;
- connect tuning changes to visible evidence;
- prove that an ensemble beats the best single model beyond validation noise;
- produce a valid submission;
- run the final system from a fresh environment;
- explain characteristic failure modes and limitations.
