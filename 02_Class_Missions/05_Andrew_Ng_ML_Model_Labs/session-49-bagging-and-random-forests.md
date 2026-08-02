# Mission 11.2 — Bagging and Random Forests

**Duration:** 75 minutes  
**Pre-class required viewing:** 14 minutes

## Pre-Class Required Resource

**Course 2 — Advanced Learning Algorithms**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/advanced-learning-algorithms  
Week 4 — Decision Trees

| Video | Duration | Student action |
|---|---:|---|
| Using Multiple Decision Trees | 4 min | explain why several trees can be more reliable than one tree |
| Sampling with Replacement | 4 min | simulate one bootstrap sample |
| Random Forest Algorithm | 6 min | identify bootstrap sampling and random feature selection |

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Build one bootstrap sample and predict how two trees may differ. |
| 8–15 min | Talk Robin 1 | Explain how diversity among trees can reduce variance. |
| 15–22 min | Entry Check | Distinguish bagging from a single decision tree and identify the extra randomness in a random forest. |
| 22–35 min | Core Pattern | Teacher models bootstrap samples → diverse trees → aggregate vote/mean → lower variance. |
| 35–53 min | Guided Practice | Compare one tree and one random forest using train/validation evidence. |
| 53–67 min | Independent Rebuild | Design a controlled comparison on a new dataset. |
| 67–75 min | Talk Robin 2 + Evidence | Defend the chosen model and submit evidence. |

## Learning Targets

- explain bootstrap sampling;
- explain how bagging can reduce variance;
- identify the extra feature randomness used by random forests;
- compare one decision tree with a random forest;
- identify when the added complexity does not produce a meaningful validation gain.

## Core Pattern

```text
Training data → bootstrap samples → diverse decision trees → vote or mean → validation comparison
```

## Guided Practice

Students record train score, validation score, model size, runtime, and dominant errors for one decision tree and one random forest.

## Independent Rebuild

Submit:

```text
Task and metric:
Single-tree settings:
Random-forest settings:
What remains fixed:
Training result:
Validation result:
Runtime difference:
Error difference:
Keep / reject decision:
```

## Talk Robin 2 + Evidence

Submit the pre-class viewing note, bootstrap demonstration, comparison table, independent experiment record, and one explanation of why “more trees” is not automatically the best next experiment.
