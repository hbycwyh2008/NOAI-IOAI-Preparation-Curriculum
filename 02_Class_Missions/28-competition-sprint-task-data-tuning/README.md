# 28 — Competition Sprint: From Data Quality to Model Ensembling

This module is used during the final competition-sprint period. It turns previously learned knowledge into a fast, repeatable, evidence-based competition workflow.

It does **not** replace the foundation modules. Students should enter this chapter only after they can already use Python and build a basic scikit-learn or PyTorch model. The sprint then retrains the order of decisions so students do not jump from task recognition directly to a favourite model.

## Canonical Sprint Workflow

```text
Read and Formalise the Task
→ Audit Data Quality and Freeze Validation
→ Build a Reproducible Feature Pipeline
→ Select and Compare Baselines
→ Run Error Analysis
→ Tune the Selected Model
→ Ensemble Only Strong, Complementary Models
→ Validate the Submission and Fresh Runtime
```

The fixed modelling sequence is:

> **data quality → feature engineering → model selection → tuning → model ensembling**

Task definition comes before the five stages. Error analysis is used throughout, especially before tuning and ensembling.

## Eight Scheduled Lessons

1. [Lesson 01 — Task recognition from unfamiliar competition statements](lesson-01-task-recognition.md)
2. [Lesson 02 — Data quality, validation design, and leakage prevention](lesson-02-data-quality-validation.md)
3. [Lesson 03 — Feature engineering and reproducible pipelines](lesson-03-feature-engineering.md)
4. [Lesson 04 — Model selection, baseline ladder, and error analysis](lesson-04-model-selection-baseline.md)
5. [Lesson 05 — Classical machine-learning tuning: diagnose before searching](lesson-05-classical-model-tuning.md)
6. [Lesson 06 — Deep-learning tuning: learning rate, batch size, regularisation, and optimiser](lesson-06-deep-learning-tuning.md)
7. [Lesson 07 — Model ensembling: voting, averaging, and stacking](lesson-07-model-ensembling.md)
8. [Lesson 08 — Full competition sprint simulation and postmortem](lesson-08-full-sprint-simulation.md)

## Optional Automated-Tuning Extension

Optuna and broader automated search are useful only after students can explain a controlled manual tuning cycle. They are no longer a required scheduled session because automated search must not displace model ensembling or submission validation.

Use:

- [Optional PyTorch schedulers, Optuna, and efficiency extension](lesson-07-pytorch-automated-tuning.md)
- [Hyperparameter-Tuning Video Resource Map](Hyperparameter_Tuning_Video_Resource_Map.md)
- `06_Starter_Code/ready_to_teach/optuna_tuning_template.py`

The teacher may assign this extension to students who have already passed the manual-tuning gate and have sufficient compute budget.

## Video Delivery Protocol for Lessons 05–06

The required tuning video packages are longer than the eight-minute classroom Skill Warm-Up. They are assigned as **pre-class preparation** or a separately scheduled resource session.

| Lesson | Pre-class required viewing | In-class Skill Warm-Up |
|---:|---:|---|
| 05 | 37 minutes | an eight-minute diagnosis task using one classical-model result |
| 06 | 43 minutes | an eight-minute training-curve diagnosis |

The former 33-minute Optuna package is optional extension work, not a required part of Lesson 07.

## Stage Gates

| Stage | Required evidence before moving on |
|---|---|
| Task definition | input, output, labels, metric, constraints, prediction-time boundary |
| Data quality | audit, frozen split, leakage tests, distribution and label checks |
| Feature engineering | reproducible pipeline, hypothesis, before/after result, ablation |
| Model selection | constant baseline, simple model, contrasting model, error analysis |
| Tuning | default-parameter reference, controlled search log, stable gain |
| Model ensembling | identical held-out or OOF predictions, diversity evidence, best-single-model comparison |
| Submission | fresh-runtime run, schema validation, final configuration, postmortem |

## Executable Sprint Assets

Use these public starter files from `06_Starter_Code/ready_to_teach/`:

- `competition_sprint_experiment_log.py` — create and validate a controlled-experiment log;
- `manual_tuning_template.py` — practise one-variable-at-a-time tuning without touching the test split;
- `optuna_tuning_template.py` — optional comparison after manual tuning is understood;
- `validate_submission.py` — verify output row count, schema, identifiers, ranges, and missing values.

These files are scaffolds, not complete competition solutions. Students must adapt the metric, split, model, search space, feature logic, ensemble rule, and error analysis to the actual task.

## Student Templates

Use:

- [`Competition Sprint Experiment Log Template`](../../03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [`Competition Sprint Model Ensembling Record`](../../03_Templates/Competition_Sprint_Model_Ensembling_Record.md)
- [`Competition Sprint Submission Checklist`](../../03_Templates/Competition_Sprint_Submission_Checklist.md)
- [`Round 2 Notebook Lab Template`](../../03_Templates/Round_2_Notebook_Lab_Template.md)

## Resource Structure

| Sprint component | Primary resources |
|---|---|
| Task recognition | official NOAI and IOAI task statements; prior task-recognition lessons in Modules 05 and 24 |
| Data quality and validation | Hands-On Machine Learning; scikit-learn model-selection and preprocessing documentation; PyTorch data-management resources |
| Feature engineering | Hands-On Machine Learning; scikit-learn `Pipeline` and `ColumnTransformer`; task-specific domain documentation |
| Model selection and baseline | Advanced Learning Algorithms, Week 3; classical-model lessons from earlier curriculum phases |
| Classical tuning | Advanced Learning Algorithms, Week 3; scikit-learn model-selection documentation |
| Deep-learning tuning | Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization |
| Model ensembling | earlier ensemble lessons; scikit-learn voting and stacking documentation; task-specific OOF practice |
| Optional automated tuning | PyTorch Techniques and Ecosystem Tools, Module 1; Optuna documentation |
| Final simulation | current official NOAI / IOAI tasks and competition constraints |

## Sprint Rules

1. Do not compare models before the validation split and leakage checks are defensible.
2. Do not add model complexity before a reproducible feature pipeline exists.
3. Preserve a constant or rule baseline and a simple trainable baseline.
4. Do not tune before the selected model has a diagnosed limitation.
5. Do not tune on the test set or public leaderboard.
6. Change one controlled variable or one named feature group at a time.
7. Record every experiment with hypothesis, change, validation result, runtime, and decision.
8. Use Optuna only after the student can explain a manual controlled experiment and a justified search space.
9. Ensemble only models that are individually valid and show complementary errors.
10. Use out-of-fold predictions for stacking; never train the meta-model on in-sample base predictions.
11. Stop increasing complexity when expected gain is smaller than reproducibility and submission risk.
12. Reserve time for fresh-runtime execution and submission-file checking.

## Minimum Evidence

Students must submit:

- a completed task-recognition sheet;
- a data-quality report, frozen split, and leakage checklist;
- a reproducible feature pipeline with at least one ablation;
- a constant baseline, a simple model, and a contrasting model comparison;
- an error-analysis table;
- a classical or deep-learning tuning log as appropriate;
- the search-space rationale when Optuna is used;
- saved held-out or OOF predictions for any ensemble;
- a best-single-model versus ensemble comparison;
- a final submission validation record;
- a fresh-runtime record;
- a postmortem identifying the highest-value next action.

## Legacy Paths

The former Lesson 02–04 files remain as compatibility pointers so old links do not break. The canonical teaching order is the eight-lesson sequence above.