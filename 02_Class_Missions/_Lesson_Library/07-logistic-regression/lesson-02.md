# Mission 07.2 — Thresholds, Logistic Loss, and Scikit-Learn

**Duration:** 75 minutes  
**Pre-class required viewing:** 33 minutes

## Pre-Class Required Resource

**Course 1 — Supervised Machine Learning: Regression and Classification**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/machine-learning  
Week 3 — Classification

| Video | Duration | Student action |
|---|---:|---|
| Logistic Regression | 10 min | connect a linear score to a probability |
| Decision Boundary | 11 min | explain how a threshold creates predicted classes |
| Cost Function for Logistic Regression | 12 min | explain why the loss penalises confident wrong predictions |

Optional review: Regularized Logistic Regression — 6 min.

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Convert supplied probabilities to classes under two thresholds and identify changed errors. |
| 8–15 min | Talk Robin 1 | Explain the relationship among probability, threshold, predicted class, and error type. |
| 15–22 min | Entry Check | Interpret one decision boundary and one loss comparison. |
| 22–35 min | Core Pattern | Teacher models score → sigmoid probability → threshold → class → metric/error trade-off. |
| 35–53 min | Guided Practice | Vary the threshold and calculate false-positive and false-negative changes. |
| 53–67 min | Independent Rebuild | Train or simulate a logistic-regression baseline and justify a threshold for a new scenario. |
| 67–75 min | Talk Robin 2 + Evidence | Defend the threshold and submit evidence. |

## Learning Targets

- explain why ordinary squared error is not the standard logistic-regression loss;
- connect probability, threshold, and predicted class;
- identify how threshold changes false positives and false negatives;
- train and evaluate `LogisticRegression`;
- justify a threshold using the task metric and error costs.

## Core Pattern

```text
Features → linear score → sigmoid probability → threshold → predicted class → confusion matrix / metric
```

## Guided Practice

Students complete a table for thresholds 0.3, 0.5, and 0.7, recording predicted classes, false positives, false negatives, precision, recall, and the practical consequence.

## Independent Rebuild

Use a new classification scenario and submit:

```text
Positive class:
Probability output:
Default threshold:
Alternative threshold:
Metric or error cost:
Chosen threshold:
Why:
One limitation:
```

## Talk Robin 2 + Evidence

Submit the pre-class viewing note, threshold table, scikit-learn or hand-simulated baseline, independent threshold memo, and one explanation of a tempting threshold misconception.