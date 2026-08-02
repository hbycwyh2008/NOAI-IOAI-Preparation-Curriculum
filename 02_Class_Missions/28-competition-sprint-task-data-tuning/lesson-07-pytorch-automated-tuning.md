# Optional Extension — PyTorch Schedulers, Optuna, and Efficiency Constraints

**Status:** Optional extension; not one of the eight scheduled competition-sprint sessions.  
**Suggested duration:** 75 minutes after Lesson 06, or independent enrichment.  
**Pre-class viewing:** up to 33 minutes.

## Why This Is Optional

Automated search can improve an already valid system, but it is lower priority than:

1. data quality and leakage prevention;
2. a reproducible feature pipeline;
3. model selection and baseline comparison;
4. manual diagnosis-first tuning;
5. model ensembling and submission reliability.

Students should use this extension only when they can already explain a manual controlled experiment and the competition has enough compute and time budget.

## Learning Target

Students can design a small automated search with a fixed validation protocol, justified ranges, strict resource limits, pruning rules, and an efficiency-aware selection decision.

## Pre-Class Resource

**Course 2 — PyTorch: Techniques and Ecosystem Tools**, part of the **DeepLearning.AI PyTorch for Deep Learning Professional Certificate**  
Coursera: https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools  
Module 1 — Hyperparameter Optimization

1. Learning Rate Schedulers — 5 min
2. Tuning Hyperparameters — 7 min
3. Hyperparameter Optimization with Optuna — 10 min
4. Optimizing Model Efficiency — 11 min

## Entry Gate

Automated tuning is allowed only when all are true:

- a valid baseline and selected model exist;
- data and feature pipelines are frozen;
- the metric and validation protocol are fixed;
- at least one manual tuning cycle is documented;
- the student can state what each searchable parameter controls;
- the trial, time, GPU, memory, and checkpoint budget is explicit.

## Core Pattern

```text
Manual Tuning Evidence
→ Justified Search Space
→ Fixed Validation Protocol
→ Trial and Time Budget
→ Pruning / Invalid-Trial Rules
→ Score + Runtime + Memory Comparison
→ Confirm the Winner Outside the Search Loop
```

## Search-Space Rules

- use logarithmic scales for learning rate and weight decay;
- use small categorical sets for optimisers and schedulers;
- tightly bound architecture choices;
- keep data, features, folds, metric, and seed policy fixed;
- save configuration, checkpoint, best epoch, metric history, runtime, and rejection reason;
- reject configurations that exceed memory, latency, or submission limits even if their validation score is high.

## Required Search Specification

| Item | Decision |
|---|---|
| Objective metric and direction |  |
| Fixed validation protocol |  |
| Searchable parameters |  |
| Fixed parameters |  |
| Learning-rate scale/range |  |
| Weight-decay scale/range |  |
| Batch-size choices |  |
| Optimiser/scheduler choices |  |
| Maximum trials |  |
| Time/GPU budget |  |
| Pruning rule |  |
| Invalid-trial rule |  |
| Final confirmation procedure |  |

## Implementation Evidence

Use `06_Starter_Code/ready_to_teach/optuna_tuning_template.py` or an equivalent wrapper that records:

```text
trial number
configuration
best epoch
validation metric
training time
peak memory or batch feasibility
checkpoint path
keep / reject reason
```

## Exit Standard

The student must explain:

- why the search space follows from prior evidence;
- why the budget is safe;
- why the best trial is not automatically the final model;
- how the selected configuration was rerun or confirmed;
- whether automated search produced enough gain to justify its cost.

Return to the scheduled sprint sequence at:

[Lesson 07 — Model Ensembling](lesson-07-model-ensembling.md).