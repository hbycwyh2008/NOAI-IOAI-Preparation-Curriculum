# Phase 8 — Competition Sprint

## Scheduled Sessions

Sessions 68–75.

## Purpose

Students compress previously learned skills into one reliable competition workflow:

```text
Task definition
→ data quality and validation
→ feature engineering
→ model selection and baseline
→ error analysis
→ diagnosis-first tuning
→ model ensembling
→ fresh-runtime and submission validation
→ full simulation and postmortem
```

The required modelling order is:

> **data quality → feature engineering → model selection → tuning → model ensembling**

This phase corrects a common competition mistake: choosing or tuning a model before the data, split, and feature pipeline are trustworthy.

## Canonical Files

- [Phase 8 Competition Sprint Index](../../10_Ready_to_Teach_Pack/Phase_8_Competition_Sprint.md)
- [Module 28 — Competition Sprint](../../02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/README.md)
- [Hyperparameter-Tuning Video Resource Map](../../02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md)
- [Competition Sprint Experiment Log Template](../../03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [Competition Sprint Model Ensembling Record](../../03_Templates/Competition_Sprint_Model_Ensembling_Record.md)
- [Competition Sprint Submission Checklist](../../03_Templates/Competition_Sprint_Submission_Checklist.md)
- [Competition Sprint Starter Code](../../06_Starter_Code/ready_to_teach/README.md)

The Class Mission files are the source of truth for lesson content and duration.

## Session Sequence

| Session | Required focus |
|---:|---|
| 68 | task recognition and formalisation |
| 69 | data quality, validation split, and leakage prevention |
| 70 | feature engineering and reproducible pipelines |
| 71 | baseline ladder, model comparison, and error analysis |
| 72 | classical diagnosis-first tuning |
| 73 | deep-learning tuning |
| 74 | model ensembling using held-out or OOF predictions |
| 75 | full competition simulation and postmortem |

PyTorch schedulers, Optuna, and broader automated search are optional extension material after Session 73. They are not a required replacement for Session 74 model ensembling.

## Entry Gate

A student enters Phase 8 only when they can already:

1. use Python and the relevant library stack;
2. train a basic scikit-learn or PyTorch model;
3. identify a metric and produce prediction-shaped output;
4. run code from a fresh runtime;
5. record one controlled experiment.

The sprint does not assume that students already make these decisions in the correct order; enforcing the order is the purpose of the phase.

## Teaching Emphasis by Stage

### Sessions 68–69 — Protect the Problem Definition and Evidence

Do not discuss favourite models until students have defined `X`, `y`, the metric, prediction-time boundary, independent unit, split, and leakage risks.

### Session 70 — Representation Before Complexity

Require a reproducible feature pipeline, a named feature hypothesis, a controlled result, and an ablation. More columns do not automatically mean better features.

### Session 71 — Baseline Ladder and Error Analysis

Require:

- constant or rule baseline;
- simple trainable baseline;
- one contrasting nonlinear or modality-specific model;
- train/validation comparison;
- spread, runtime, and error categories.

### Sessions 72–73 — Tune a Diagnosed Limitation

The tuning video packages are pre-class work or separately scheduled resource sessions:

- classical machine-learning diagnosis and tuning: 37 minutes;
- deep-learning tuning: 43 minutes.

The in-class eight-minute Skill Warm-Up is a retrieval or diagnosis task. Full video packages are not replayed in the warm-up.

### Session 74 — Fusion Requires Diversity

Students must save predictions on identical held-out rows or generate valid OOF predictions. Start with averaging or voting. Permit stacking only when the meta-model is trained on OOF base predictions.

### Session 75 — Stop Complexity in Time

The full simulation must reserve a final block for:

- configuration freeze;
- fresh-runtime execution;
- row order and schema validation;
- submission checks;
- postmortem.

## Exit Standard

Students submit:

- task-definition card;
- data-quality audit and frozen split;
- leakage checklist;
- feature pipeline, controlled feature result, and ablation;
- constant, simple, and contrasting model comparison;
- error-analysis and manual tuning logs;
- optional automated-search rationale when used;
- held-out or OOF predictions for any ensemble;
- best-single-model versus ensemble decision;
- valid submission and fresh-runtime records;
- postmortem with a highest-value next action.

A high score without reproducibility, valid validation, stage-gate evidence, or submission reliability does not meet the exit standard.