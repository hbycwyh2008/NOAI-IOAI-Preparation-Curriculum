# Lesson 07 — PyTorch Tuning with Schedulers, Optuna, and Efficiency Constraints

**Duration:** 75 minutes  
**Pre-class required viewing:** 33 minutes

## Learning Target

Students can move from manual controlled experiments to limited automated search without wasting the competition compute budget.

## Pre-Class Required Video Resource

**Course 2 — PyTorch: Techniques and Ecosystem Tools**, part of the **DeepLearning.AI PyTorch for Deep Learning Professional Certificate**  
Coursera: https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools  
Module 1 — Hyperparameter Optimization

1. Learning Rate Schedulers — 5 min
2. Tuning Hyperparameters — 7 min
3. Hyperparameter Optimization with Optuna — 10 min
4. Optimizing Model Efficiency — 11 min

**Pre-class required viewing time:** 33 minutes.

Before class, submit a note identifying the optimisation objective, one justified search range, one efficiency constraint, and one reason a trial should be stopped or rejected.

See [Hyperparameter-Tuning Video Resource Map](Hyperparameter_Tuning_Video_Resource_Map.md).

## 1. Skill Warm-Up — 0–8 min

Do not replay the full 33-minute package. Complete this retrieval check:

```text
Objective metric and direction:
Fixed validation protocol:
One logarithmic parameter range:
One categorical parameter set:
Maximum trials or time budget:
Invalid-trial rule:
Stopping rule:
```

## 2. Talk Robin 1 — 8–15 min

Discuss what should be manually understood before an automated search is allowed.

## 3. Entry Check — 15–22 min

Answer:

1. What metric will the search optimise?
2. What validation split will every trial use?
3. Which parameters are searchable?
4. Which parameters must remain fixed?
5. What is the trial/time/GPU budget?
6. What makes a trial invalid?

## 4. Core Pattern — 22–35 min

```text
Manual Baseline
→ Justified Search Space
→ Fixed Validation Protocol
→ Trial Budget
→ Pruning / Early Stop
→ Score + Runtime + Memory Comparison
→ Refit or Confirm
```

Search-space rules:

- use logarithmic scales for learning rate and weight decay;
- use small categorical sets for optimisers and schedulers;
- bound architecture choices tightly;
- save the seed, configuration, checkpoint, and metric history;
- do not optimise only for score when runtime or memory can invalidate the submission.

## 5. Guided Practice — 35–53 min

Design an automated-search specification:

| Item | Decision |
|---|---|
| Objective metric |  |
| Direction | maximise / minimise |
| Learning-rate range |  |
| Weight-decay range |  |
| Batch-size choices |  |
| Optimiser choices |  |
| Maximum trials |  |
| Time limit |  |
| Pruning rule |  |
| Invalid-trial rule |  |

## 6. Independent Rebuild — 53–67 min

Use `06_Starter_Code/ready_to_teach/optuna_tuning_template.py` or write pseudocode for a small search wrapper that records:

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

Then choose one configuration using both performance and efficiency.

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit:

- pre-class viewing note;
- Skill Warm-Up search specification;
- justified search-space table;
- trial log or pseudocode;
- one explanation of why the highest validation score may not be the best competition model.

## Exit Standard

Automated tuning is allowed only after students can explain the baseline, search space, objective, budget, and stopping rule.