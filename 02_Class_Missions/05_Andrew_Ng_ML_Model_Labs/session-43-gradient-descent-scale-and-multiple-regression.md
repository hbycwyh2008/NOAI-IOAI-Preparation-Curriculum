# Mission 06.2 — Gradient Descent and Multiple Linear Regression

**Duration:** 75 minutes  
**Pre-class required viewing:** 31 minutes

## Pre-Class Required Resource

**Course 1 — Supervised Machine Learning: Regression and Classification**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/machine-learning  
Week 2 — Regression with Multiple Input Variables

| Video | Duration | Student action |
|---|---:|---|
| Multiple Features | 10 min | identify the feature vector and parameter vector |
| Gradient Descent for Multiple Linear Regression | 8 min | trace one parameter-update cycle |
| Feature Scaling Part 1 | 7 min | explain why unequal feature scales slow optimisation |
| Checking Gradient Descent for Convergence | 6 min | identify stable, slow, and divergent learning curves |

Optional review: Choosing the Learning Rate — 6 min.

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Complete one multiple-feature prediction and identify one convergence pattern. |
| 8–15 min | Talk Robin 1 | Explain which feature scale or learning-rate issue is most likely. |
| 15–22 min | Entry Check | Trace one gradient-descent update and state what remains fixed. |
| 22–35 min | Core Pattern | Teacher models features → prediction → residual → cost → gradient → update → convergence check. |
| 35–53 min | Guided Practice | Compare scaled and unscaled feature tables and interpret learning curves. |
| 53–67 min | Independent Rebuild | Design and justify a multiple-regression experiment on a new dataset. |
| 67–75 min | Talk Robin 2 + Evidence | Explain the result and submit evidence. |

## Learning Targets

- distinguish one-feature and multiple linear regression;
- explain one gradient-descent update;
- interpret learning rate and convergence;
- explain why feature scaling matters;
- connect the hand-worked pattern to a scikit-learn baseline.

## Core Pattern

```text
Feature vector → weighted prediction → residual → cost → gradient → parameter update → convergence evidence
```

## Guided Practice

Students compare scaled and unscaled training behaviour, calculate one prediction and residual, and diagnose two learning curves.

## Independent Rebuild

Choose a small regression dataset and write:

```text
Target:
Features:
Feature scales:
Scaling decision:
Baseline model:
Convergence evidence:
Validation metric:
One controlled next experiment:
```

## Talk Robin 2 + Evidence

Submit the pre-class viewing note, calculation trace, scaled-versus-unscaled comparison, independent experiment plan, and one explanation of a learning-rate mistake.
