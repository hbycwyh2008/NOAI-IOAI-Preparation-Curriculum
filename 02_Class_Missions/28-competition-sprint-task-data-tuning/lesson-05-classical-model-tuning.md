# Lesson 05 — Classical Machine-Learning Tuning: Diagnose before Searching

**Duration:** 75 minutes

## Learning Target

Students can diagnose the dominant failure mode and tune a classical machine-learning model using controlled experiments instead of random parameter changes.

## Required Video Resource

**Course 2 — Advanced Learning Algorithms**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/advanced-learning-algorithms  
Week 3 — Advice for Applying Machine Learning:

1. Deciding What to Try Next — 4 min
2. Model Selection and Training/Cross Validation/Test Sets — 14 min
3. Diagnosing Bias and Variance — 11 min
4. Iterative Loop of Machine-Learning Development — 8 min

**Required video time:** 37 minutes.

Optional review:

- Learning Curves — 12 min
- Error Analysis — 8 min

See [Hyperparameter-Tuning Video Resource Map](Hyperparameter_Tuning_Video_Resource_Map.md).

## 1. Skill Warm-Up — 0–8 min

Watch the first assigned segment and write one reason random tuning is inefficient.

## 2. Talk Robin 1 — 8–15 min

Partners compare the current training and validation results and state whether the main problem is high bias, high variance, metric mismatch, data quality, or insufficient evidence.

## 3. Entry Check — 15–22 min

Complete:

```text
Baseline model:
Training score:
Validation score:
Gap:
Dominant failure mode:
Most likely useful intervention:
One intervention that should not be tried yet:
```

## 4. Core Pattern — 22–35 min

```text
Valid Split
→ Baseline
→ Bias/Variance Diagnosis
→ Choose One Parameter Family
→ Small Search Space
→ Cross-Validated Comparison
→ Error Analysis
→ Keep or Revert
```

Classical tuning order:

1. model family and basic capacity;
2. regularisation strength;
3. tree depth, minimum samples, number of trees, or boosting rate;
4. class weights or decision threshold when metric-sensitive;
5. feature set;
6. broader automated search only after the search space is justified.

## 5. Guided Practice — 35–53 min

Design one controlled search:

| Item | Decision |
|---|---|
| Parameter being changed |  |
| Values to test |  |
| Why this range |  |
| What stays fixed |  |
| Validation method |  |
| Metric |  |
| Stop rule |  |

## 6. Independent Rebuild — 53–67 min

Run or simulate three parameter settings and complete:

| Run | Hypothesis | Parameter value | Validation score | Runtime | Decision |
|---|---|---:|---:|---:|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## 7. Talk Robin 2 + Evidence — 67–75 min

Explain why the selected setting is better than the alternatives and why the next experiment follows from evidence.

## Exit Standard

Students must be able to state what the parameter controls, why the tested range is sensible, and whether the gain is stable across validation folds or seeds.