# Phase 8 — Competition Sprint: Data Quality to Model Ensembling

This phase converts the full curriculum into a repeatable late-stage competition workflow. It is taught after students can use Python and train a basic scikit-learn or PyTorch model.

The sprint deliberately retrains decision order. Students may not jump from recognising a task directly to choosing or tuning a favourite model.

## Phase Outcome

By the end of the eight-session sprint, students should be able to:

1. formalise input `X`, target/output `y`, task type, metric, prediction-time boundary, constraints, and submission schema;
2. audit schema, labels, missingness, duplicates, groups, time, distribution, and leakage before model comparison;
3. freeze a validation protocol that reflects the likely hidden-test structure;
4. build a reproducible preprocessing and feature pipeline with hypothesis-based feature experiments and ablations;
5. preserve a constant or rule baseline, compare a simple trainable model with a contrasting model, and analyse errors;
6. tune classical or deep-learning models only after diagnosing the dominant limitation;
7. ensemble only individually strong models with complementary errors, using identical held-out rows or valid OOF predictions;
8. complete a full sprint simulation with fresh-runtime and submission validation.

## Canonical Workflow

```text
Task definition
→ data quality and validation
→ feature engineering
→ model selection and baseline
→ error analysis
→ tuning
→ model ensembling
→ fresh-runtime and submission validation
```

The fixed five-stage modelling sequence is:

> **data quality → feature engineering → model selection → tuning → model ensembling**

## Required Module

Open:

`02_Class_Missions/28-competition-sprint-task-data-tuning/`

The Class Mission files are the source of truth for lesson content, classroom flow, evidence, and exit standards.

## Eight-Session Sequence

| Session | Mission | Required resource | Required evidence |
|---:|---|---|---|
| 68 | Task recognition and task formalisation | current official NOAI or IOAI task statement | task card identifying X, y, modality, metric, prediction-time boundary, constraints, and risks |
| 69 | Data quality, validation design, and leakage prevention | Hands-On Machine Learning; scikit-learn model-selection/preprocessing documentation | quality audit, frozen split, split diagram, and leakage checklist |
| 70 | Feature engineering and reproducible pipelines | Hands-On Machine Learning; scikit-learn Pipeline/ColumnTransformer; task documentation | feature-hypothesis table, pipeline, before/after result, and ablation |
| 71 | Model selection, baseline ladder, and error analysis | Advanced Learning Algorithms, selected Week 3 material; prior model lessons | constant/rule, simple, and contrasting model comparison plus error-analysis memo |
| 72 | Classical machine-learning tuning | Advanced Learning Algorithms, Week 3: Advice for Applying Machine Learning | diagnosis-first tuning log with one-variable experiments |
| 73 | Deep-learning tuning | Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization | learning-rate, regularisation, batch-size, optimiser, and scheduler decision record |
| 74 | Model ensembling: voting, averaging, and stacking | prior ensemble lessons; scikit-learn ensemble documentation; saved validation/OOF predictions | diversity table, ensemble ladder, leakage checks, and best-single-versus-ensemble decision |
| 75 | Full competition sprint simulation and postmortem | current official task format and permitted tools | full notebook/script, stage-gate evidence, submission validation, fresh-runtime record, and postmortem |

## Tuning Video Assignments

Use:

`02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md`

### Session 72 — Classical Machine-Learning Tuning

Required videos from Course 2 — Advanced Learning Algorithms, Week 3:

- Deciding What to Try Next — 4 minutes;
- Model Selection and Training/Cross Validation/Test Sets — 14 minutes;
- Diagnosing Bias and Variance — 11 minutes;
- Iterative Loop of Machine-Learning Development — 8 minutes.

Required viewing time: **37 minutes**.

### Session 73 — Deep-Learning Tuning

Required videos from Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization:

- Basic Recipe for Machine Learning — 6 minutes;
- Adam Optimization Algorithm — 7 minutes;
- Learning Rate Decay — 7 minutes;
- Tuning Process — 7 minutes;
- Using an Appropriate Scale to Pick Hyperparameters — 9 minutes;
- Hyperparameters Tuning in Practice: Pandas vs. Caviar — 7 minutes.

Required viewing time: **43 minutes**.

### Optional Automated-Tuning Extension

PyTorch schedulers, Optuna, and efficiency resources remain available as an optional extension after Session 73. They are not a required scheduled session and do not replace Session 74 model ensembling.

Use:

- `02_Class_Missions/28-competition-sprint-task-data-tuning/Optional_Automated_Tuning_Extension.md`;
- `06_Starter_Code/ready_to_teach/optuna_tuning_template.py`.

The optional video package takes **33 minutes** and must not be replayed inside the eight-minute classroom warm-up.

## Stage Gates

### Data-Quality Gate

No feature or model result counts until:

- the independent unit and split are defensible;
- obvious target, duplicate, identity, group, time, and preprocessing leakage have been checked;
- metric, validation protocol, labels, IDs, and prediction order are fixed.

### Feature Gate

No model-family comparison counts until:

- training and inference use one reproducible pipeline;
- all learned transforms are fitted on training data only;
- kept feature groups have a hypothesis, controlled result, and ablation.

### Model-Selection Gate

No tuning is allowed until:

- constant/rule, simple, and contrasting baselines have been compared under one protocol;
- train score, validation mean/spread, runtime, and error categories are recorded;
- the selected model has a diagnosed limitation.

### Tuning Gate

No ensemble is allowed until:

- default parameters remain as reference;
- parameter changes follow the diagnosis;
- improvements are stable across folds or seeds;
- best configurations have been rerun or confirmed.

### Ensembling Gate

An ensemble counts only when:

- base models are independently valid and sufficiently strong;
- predictions come from identical held-out rows or valid OOF generation;
- diversity is measured rather than assumed;
- the ensemble is compared with the best single model;
- gain exceeds validation noise and remains operationally safe.

## Non-Negotiable Rules

1. Protect validation quality before chasing score.
2. Do not compare models before the data-quality gate.
3. Do not increase model complexity before the feature pipeline is reproducible.
4. Do not tune before a valid model-selection comparison and error analysis exist.
5. Do not tune on the hidden test, public leaderboard, or reused final holdout.
6. Record hypothesis, named change, held constants, validation result, spread, runtime, and decision.
7. Automated search is optional and follows a manual cycle.
8. Stacking uses OOF predictions; in-sample base predictions are forbidden.
9. Preserve rejected experiments and failed ensembles.
10. Stop complexity early enough to complete fresh-runtime and submission validation.

## Required Student Evidence

Students submit:

- task-definition card;
- data-quality report and frozen validation memo;
- leakage checklist;
- reproducible feature pipeline and at least one ablation;
- constant/rule, simple, and contrasting model comparison;
- error-analysis table;
- manual tuning log and optional search rationale;
- saved held-out or OOF predictions for any ensemble;
- completed model-ensembling record;
- valid submission and fresh-runtime records;
- postmortem with the highest-value next action.

## Phase Gate

A student passes only when they can independently explain:

- why the task is a particular learning problem;
- why the metric and validation design are trustworthy;
- which data-quality risk mattered most;
- which feature group produced the largest reliable gain;
- why the selected model family beat the simpler baseline;
- which error category guided tuning;
- which parameter was tuned and why;
- whether model errors were complementary enough for fusion;
- whether the ensemble truly beat the best single model;
- whether the final system runs from a fresh environment and produces a valid submission.