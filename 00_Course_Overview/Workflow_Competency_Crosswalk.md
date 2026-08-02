# Workflow Competency Crosswalk

This document makes the modeling workflow explicit across the full 78-session curriculum. It is not a new Phase and does not replace any Session launcher. It is the recurring decision framework students use whenever they encounter a data or model task.

## Canonical Modeling Workflow

```text
task formalisation
→ data quality
→ feature engineering
→ model selection and baseline
→ diagnosis and controlled tuning
→ ensembling
→ reproducibility check and postmortem
```

The five core competition stages are **data quality → feature engineering → model selection → tuning → ensembling**. Task formalisation comes before them, and reproducibility plus postmortem close the loop.

## Non-Negotiable Rules

1. **Define the task before touching a model.** Identify `X`, `y`, output type, label availability, groups, time order, constraints, and the competition metric.
2. **Protect the validation design before inspecting results.** Split logic must reflect groups, time, repeated entities, or distribution shift.
3. **Build a simple baseline before adding complexity.** A baseline provides a reference point for every later claim.
4. **Change one major factor at a time.** Every experiment records a hypothesis, the controlled change, the result, and the next decision.
5. **Tune only after diagnosis.** Search is not a substitute for understanding data, errors, leakage, or model mismatch.
6. **Ensemble only stable and meaningfully different models.** More models do not automatically create a better system.
7. **Count only reproducible evidence.** A result is not complete until it can be rebuilt from a fresh environment and explained.

## Curriculum Crosswalk

| Phase | Sessions | Primary contribution to the workflow | Recurring evidence | Promotion gate |
|---|---:|---|---|---|
| 0 — Orientation and Evidence | 1–2 | Competition constraints, repository discipline, evidence rules, reproducibility | environment record, repository structure, evidence checklist | student can locate the assigned Session, submit named evidence, and explain the AI-use boundary |
| 1 — CS50P Python | 3–12 | Reliable implementation, decomposition, debugging, files, tests, defensive programming | independent rebuilds, traced outputs, tests, debugging notes | student can reconstruct a small data-oriented program without copying |
| 2 — NumPy, Pandas, and Visualisation | 13–18 | Data inspection, shapes, types, missing values, duplicates, summaries, visual evidence | data-quality audit and mini-EDA | student can identify and justify treatment of common data defects |
| 3 — Bohrium ML Foundations | 19–32 | Task recognition, supervised versus unsupervised learning, baseline model families, optimization concepts | `X`/`y`/output/labels/baseline/metric classification for each task | student chooses the correct learning paradigm and a defensible first baseline |
| 4 — AI History and Thinking Humans | 33–40 | Critical interpretation, limits, dataset and benchmark skepticism, model-behavior reasoning | reading evidence, claims-and-limitations analysis | student distinguishes demonstrated capability from unsupported inference |
| 5 — Andrew Ng ML and Model Labs | 41–58 | Mathematical model language, classical models, validation, model comparison, embedded Kaggle workflow | equations, shapes, hand calculations, baseline notebook, controlled improvement, postmortem | student can build, evaluate, compare, and explain a classical-ML pipeline |
| 6 — Andrew Ng DL and PyTorch | 59–70 | Tensor reasoning, training loops, deep-model baselines, regularization, transfer learning | reproducible training loop, learning curves, baseline-versus-deep comparison | student can justify when a deep model is appropriate and diagnose basic training behavior |
| 7 — Model Comparison, EDA, and Evaluation | 71–74 | Full workflow integration: data quality, leakage, feature engineering, ablation, validation, metrics, calibration, error analysis | data audit, feature ledger, ablation table, error slices, model comparison | no tuning begins until the student has a trustworthy split, baseline, and written diagnosis |
| 8 — Tuning, Ensembling, and Competition | 75–78 | Diagnosis-first search, ensemble diversity, timed execution, fresh-environment rebuild, postmortem | experiment log, ensemble record, submission checklist, mock report | final system is reproducible, evidence-backed, and explainable under competition constraints |

## Workflow Evidence Gates

### Gate 1 — Data Quality

Required evidence:

- row and column meaning;
- target definition and label source;
- missingness, duplicates, invalid types, impossible values, outliers, imbalance, groups, and time-order checks;
- leakage risks and split decision;
- written treatment decisions, including what was deliberately left unchanged.

A student does not pass this gate by producing plots alone. The student must connect each finding to a modeling decision.

### Gate 2 — Feature Engineering

Required evidence:

- feature hypothesis;
- train-only fitting for learned transformations;
- pipeline or equivalent reproducible transformation path;
- before/after comparison on a fixed validation design;
- ablation showing whether the feature helped;
- cost, leakage, fairness, and interpretability considerations.

A feature is not credited merely because it increases dimensionality or training score.

### Gate 3 — Model Selection and Baseline

Required evidence:

- simple baseline;
- at least two justified model families when appropriate;
- fixed metric and validation design;
- comparison of performance, stability, cost, interpretability, and failure modes;
- selection rationale tied to the task rather than popularity.

The best single score is not automatically the selected model.

### Gate 4 — Diagnosis-First Tuning

Required evidence:

- written diagnosis from errors, learning curves, residuals, calibration, or slice analysis;
- bounded search space linked to that diagnosis;
- controlled search method and budget;
- cross-validation or repeated validation summary where appropriate;
- comparison against the untuned baseline;
- decision to keep, reject, or revise the model.

Tuning without a diagnosis is recorded as exploration, not mastery evidence.

### Gate 5 — Ensembling

Required evidence:

- individually stable component models;
- diversity evidence from architecture, features, seeds, folds, or error correlation;
- validation-safe blending, voting, bagging, or out-of-fold stacking;
- comparison against the best single model;
- complexity and runtime cost;
- fallback plan if the ensemble cannot be reproduced.

An ensemble that cannot beat or reliably match the best single model is not automatically retained.

## Repeated Student Decision Routine

For every substantial modeling task, students answer these questions in order:

1. What are the samples, features, target, output, labels, groups, and time constraints?
2. What could make the data invalid, misleading, or leaky?
3. What is the simplest meaningful baseline and why?
4. Which metric reflects the real objective, and what does it ignore?
5. What do the first errors reveal?
6. Which feature or model change follows from that evidence?
7. Did the controlled change improve validation performance and stability?
8. Is tuning justified yet?
9. Are multiple strong models different enough to ensemble?
10. Can the full result be rebuilt and explained from a fresh environment?

## Checkpoints

Use the following spiral checkpoints rather than waiting until the final Phase:

- **Session 18:** first complete data-quality and EDA audit;
- **Session 24:** first formal task-recognition and workflow explanation;
- **Session 41:** first complete `X`/`y`/output/baseline/metric/mathematics record;
- **Session 57:** first end-to-end controlled tabular improvement;
- **Session 58:** classical-ML workflow checkpoint;
- **Session 70:** baseline-versus-deep-model checkpoint;
- **Session 74:** full pre-tuning workflow gate;
- **Session 77:** timed competition execution and fresh-environment rebuild;
- **Session 78:** final evidence conference and remediation plan.

## Teacher Use

Use this crosswalk when planning retrieval questions, checking evidence, and deciding whether a student may advance. Phase completion alone does not prove workflow mastery. Promotion requires the named evidence gate at the expected level of independence.
