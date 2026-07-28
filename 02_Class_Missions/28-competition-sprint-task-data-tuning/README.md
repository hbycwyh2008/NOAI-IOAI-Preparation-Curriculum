# 28 — Competition Sprint: Task Recognition, Data Engineering, and Hyperparameter Tuning

This module is used during the final competition-sprint period. It turns previously learned knowledge into a fast, repeatable competition workflow.

It does **not** replace the foundation modules. Students should enter this chapter only after they can already build a valid baseline with scikit-learn or PyTorch.

## Core Sprint Workflow

```text
Read the Task
→ Identify Input, Output, Labels, Metric, and Constraints
→ Choose the Simplest Valid Baseline
→ Audit and Split the Data
→ Improve the Data Pipeline
→ Tune One Variable at a Time
→ Run Error Analysis
→ Validate the Submission and Fresh Runtime
```

## Lessons

1. [Lesson 01 — Task recognition from unfamiliar competition statements](lesson-01-task-recognition.md)
2. [Lesson 02 — Baseline, metric, and model-family selection](lesson-02-baseline-metric-model-selection.md)
3. [Lesson 03 — Data audit, validation split, and leakage prevention](lesson-03-data-audit-split-leakage.md)
4. [Lesson 04 — Data cleaning and feature engineering under time limits](lesson-04-data-cleaning-feature-engineering.md)
5. [Lesson 05 — Classical machine-learning tuning: diagnose before searching](lesson-05-classical-model-tuning.md)
6. [Lesson 06 — Deep-learning tuning: learning rate, batch size, regularisation, and optimiser](lesson-06-deep-learning-tuning.md)
7. [Lesson 07 — PyTorch tuning with schedulers, Optuna, and efficiency constraints](lesson-07-pytorch-automated-tuning.md)
8. [Lesson 08 — Full competition sprint simulation and postmortem](lesson-08-full-sprint-simulation.md)

## Hyperparameter-Tuning Video Map

Use the dedicated resource map:

[Hyperparameter-Tuning Video Resource Map](Hyperparameter_Tuning_Video_Resource_Map.md)

The map gives the exact Coursera course, week or module, video title, duration, and use in Lessons 05–07.

## Video Delivery Protocol for Lessons 05–07

The required video packages are longer than the eight-minute classroom Skill Warm-Up. They are therefore assigned as **pre-class preparation**, not played in full during the 75-minute lesson.

| Lesson | Pre-class required viewing | In-class Skill Warm-Up |
|---:|---:|---|
| 05 | 37 minutes | an eight-minute retrieval task using one diagnosis example from the assigned videos |
| 06 | 43 minutes | an eight-minute training-curve diagnosis using concepts from the assigned videos |
| 07 | 33 minutes | an eight-minute scheduler/search-space check using concepts from the assigned videos |

Students submit a short pre-class viewing note before entry to the lesson. The teacher may replace pre-class viewing with a separate resource session, but must not claim that 33–43 minutes of video fit inside an eight-minute warm-up.

## Executable Sprint Assets

Use these public starter files from `06_Starter_Code/ready_to_teach/`:

- `competition_sprint_experiment_log.py` — create and validate a controlled-experiment log;
- `manual_tuning_template.py` — practise one-variable-at-a-time tuning without touching the test split;
- `optuna_tuning_template.py` — compare manual tuning with a small, justified Optuna search;
- `validate_submission.py` — verify output row count, schema, identifiers, ranges, and missing values.

These files are scaffolds, not complete competition solutions. Students must adapt the metric, split, model, search space, and error analysis to the actual task.

## Student Templates

Use:

- [`Competition Sprint Experiment Log Template`](../../03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [`Competition Sprint Submission Checklist`](../../03_Templates/Competition_Sprint_Submission_Checklist.md)
- [`Round 2 Notebook Lab Template`](../../03_Templates/Round_2_Notebook_Lab_Template.md)

## Resource Structure

| Sprint component | Primary resources |
|---|---|
| Task recognition | official NOAI and IOAI task statements; prior task-recognition lessons in Modules 05 and 24 |
| Baseline and metric selection | Course 2 — Advanced Learning Algorithms from the Machine Learning Specialization, Week 3: Advice for Applying Machine Learning |
| Data engineering | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide; Course 1 — PyTorch: Fundamentals, Module 3: Data Management in PyTorch |
| Classical machine-learning tuning | Course 2 — Advanced Learning Algorithms, Week 3; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide |
| Deep-learning tuning | Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization |
| PyTorch automated tuning and efficiency | Course 2 — PyTorch: Techniques and Ecosystem Tools, Module 1: Hyperparameter Optimization |
| Final sprint simulation | current official NOAI / IOAI tasks and competition constraints |

## Sprint Rules

1. Do not tune before a valid baseline exists.
2. Do not tune on the test set.
3. Do not change the data pipeline, model family, metric, and several hyperparameters at the same time.
4. Record every experiment with hypothesis, single change, validation result, runtime, and decision.
5. Prefer a reproducible improvement over an unexplained leaderboard jump.
6. Stop tuning when the expected gain is smaller than the remaining submission and validation risk.
7. Always reserve time for fresh-runtime execution and submission-file checking.
8. Use Optuna only after the student can complete and explain a manual controlled experiment.
9. Record rejected experiments; do not keep only the winning configuration.
10. Compare accuracy gain with runtime, memory, and submission risk.

## Minimum Evidence

Students must submit:

- a completed task-recognition sheet;
- a baseline and metric decision memo;
- a data-audit and leakage checklist;
- a feature-engineering table;
- a classical-model tuning log;
- a deep-learning or PyTorch tuning log when relevant;
- the search-space rationale when Optuna is used;
- an error-analysis table;
- a final submission validation record;
- a fresh-runtime record;
- a postmortem identifying the highest-value next action.