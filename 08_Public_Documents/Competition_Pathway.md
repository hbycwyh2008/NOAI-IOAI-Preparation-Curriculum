# NOAI / IOAI Competition Preparation Pathway

The curriculum develops competition readiness through the canonical 78-Session dependency path rather than asking students to jump directly into advanced models.

```text
orientation and evidence
→ CS50P Python
→ NumPy, Pandas, and visualisation
→ Bohrium ML foundations
→ AI history and critical reading
→ Andrew Ng ML + mathematics + embedded practice
→ Andrew Ng DL + PyTorch + domain tasks
→ model comparison + EDA + evaluation
→ diagnosis-first tuning + ensembling + competition simulation
```

## Canonical Pathway

| Phase | Sessions | Competition contribution |
|---:|---:|---|
| 0 | 1–2 | environment, evidence, Git, and responsible assistance |
| 1 | 3–12 | Python code reading, testing, debugging, and independent programs |
| 2 | 13–18 | data inspection, transformation, and visual reasoning |
| 3 | 19–32 | machine-learning concept foundation |
| 4 | 33–40 | AI history, claim auditing, understanding, and limitations |
| 5 | 41–58 | classical models, mathematics, task recognition, and tabular workflows |
| 6 | 59–70 | PyTorch, image, text, audio, and multimodal tasks |
| 7 | 71–74 | model comparison, EDA, features, validation, metrics, and error analysis |
| 8 | 75–78 | tuning, ensembling, full simulation, and postmortem |

A shortened cohort route may reduce breadth, but it must not redefine canonical Session numbers or claim full-pathway readiness.

## Competition Habits

- formalise `X`, `y` or required output, metric, prediction-time boundary, constraints, and submission schema;
- inspect data quality and prevent target, identity, duplicate, group, temporal, and preprocessing leakage;
- preserve a simple baseline under one validation protocol;
- keep feature generation reproducible;
- compare model families from evidence;
- analyse errors before tuning;
- record controlled experiments;
- validate final artifacts from a fresh environment.

## Final Phase

Sessions 75–78 cover:

1. diagnosis-first tuning and bounded search;
2. valid held-out or out-of-fold ensembling;
3. a full competition simulation from task reading to valid submission;
4. a postmortem and evidence-based readiness decision.

```text
data quality
→ valid split and baseline
→ feature engineering
→ model comparison
→ error diagnosis
→ tuning
→ ensembling
→ fresh-runtime submission validation
```

Optuna and broad automated search are optional tools inside Session 75. They do not replace model understanding, validation independence, reproducibility, or submission checks.

## Readiness Standard

A sophisticated model is not competition-ready unless the student can defend the task, data, split, baseline, metric, experiment history, final artifact, fresh run, and characteristic limitations.
