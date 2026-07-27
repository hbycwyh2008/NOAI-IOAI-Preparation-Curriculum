# Phase 8 — Competition Sprint: Task Recognition, Data Engineering, and Hyperparameter Tuning

This phase converts the full curriculum into a repeatable late-stage competition workflow. It is taught after the student can already build a valid scikit-learn or PyTorch baseline.

## Phase Outcome

By the end of the eight-session sprint, students should be able to:

1. recognise the task type, input, output, labels, metric, and constraints from an unfamiliar task statement;
2. choose the simplest valid baseline and justify the model family;
3. audit data, design a valid split, and detect leakage;
4. improve the data pipeline before increasing model complexity;
5. diagnose bias, variance, optimisation, and data problems before tuning;
6. tune classical and deep-learning systems using controlled experiments;
7. use schedulers and Optuna only after a manual tuning cycle is understood;
8. complete a full sprint simulation with error analysis, fresh-runtime validation, and submission checks.

## Required Module

Open:

`02_Class_Missions/28-competition-sprint-task-data-tuning/`

Use the exact lessons and evidence requirements from that module.

## Eight-Session Sequence

| Session | Mission | Required resource | Required evidence |
|---:|---|---|---|
| 68 | Task recognition from unfamiliar competition statements | current official NOAI or IOAI task statement | task-recognition sheet identifying modality, input, output, label, metric, constraints, and risks |
| 69 | Baseline, metric, and model-family selection | Course 2 — Advanced Learning Algorithms, selected Week 3 material | baseline and metric decision memo |
| 70 | Data audit, validation split, and leakage prevention | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide | data-audit table, split diagram, and leakage checklist |
| 71 | Data cleaning and feature engineering under time limits | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; task-specific documentation | feature-engineering hypothesis table and before/after validation result |
| 72 | Classical machine-learning tuning | Course 2 — Advanced Learning Algorithms, Week 3: Advice for Applying Machine Learning | diagnosis-first tuning log with one-variable experiments |
| 73 | Deep-learning tuning | Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization | learning-rate, regularisation, batch-size, and optimiser decision record |
| 74 | PyTorch schedulers, automated tuning, and efficiency | Course 2 — PyTorch: Techniques and Ecosystem Tools, Module 1: Hyperparameter Optimization | manual-to-automated tuning comparison, Optuna search-space rationale, efficiency record |
| 75 | Full competition sprint simulation and postmortem | current official task format and permitted tools | full notebook/script, submission validation, fresh-runtime record, and postmortem |

## Hyperparameter-Tuning Video Assignments

Use:

`02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md`

### Session 72 — Classical Machine-Learning Tuning

Required videos from Course 2 — Advanced Learning Algorithms, Week 3:

- Deciding what to try next — 4 minutes;
- Model selection and training/cross validation/test sets — 14 minutes;
- Diagnosing bias and variance — 11 minutes;
- Iterative loop of machine-learning development — 8 minutes.

Required video time: **37 minutes**.

### Session 73 — Deep-Learning Tuning

Required videos from Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization:

- Basic Recipe for Machine Learning — 6 minutes;
- Adam Optimization Algorithm — 7 minutes;
- Learning Rate Decay — 7 minutes;
- Tuning Process — 7 minutes;
- Using an Appropriate Scale to Pick Hyperparameters — 9 minutes;
- Hyperparameters Tuning in Practice: Pandas vs. Caviar — 7 minutes.

Required video time: **43 minutes**.

### Session 74 — PyTorch Tuning and Optuna

Required videos from Course 2 — PyTorch: Techniques and Ecosystem Tools, Module 1:

- Learning Rate Schedulers — 5 minutes;
- Tuning Hyperparameters — 7 minutes;
- Hyperparameter Optimization with Optuna — 10 minutes;
- Optimizing Model Efficiency — 11 minutes.

Required video time: **33 minutes**.

## Competition Tuning Order

```text
Metric and validation
→ baseline
→ error analysis
→ data pipeline
→ model family or capacity
→ learning rate
→ regularisation
→ batch size and optimiser
→ scheduler
→ automated search
→ efficiency and submission risk
```

## Non-Negotiable Rules

1. Do not tune before a valid baseline exists.
2. Do not tune on the test set.
3. Do not change the data pipeline, model family, metric, and several hyperparameters in one experiment.
4. Record the hypothesis, single change, validation result, runtime, and decision.
5. Automated search must not hide leakage, a wrong metric, a broken baseline, or weak task recognition.
6. Stop tuning early enough to complete error analysis, fresh-runtime execution, and submission validation.

## Phase Gate

A student passes the phase only when they can independently explain:

- why the task is a particular learning problem;
- why the selected metric matches the competition objective;
- why the validation strategy is trustworthy;
- which data-engineering change produced the largest reliable gain;
- which hyperparameter was tuned and why;
- why the final model is preferred over the baseline;
- what remains the largest failure mode;
- whether the final code runs from a fresh environment.