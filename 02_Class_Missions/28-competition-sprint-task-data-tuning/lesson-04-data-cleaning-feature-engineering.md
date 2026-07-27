# Lesson 04 — Data Cleaning and Feature Engineering under Time Limits

**Duration:** 75 minutes

## Learning Target

Students can choose the highest-value data-engineering action for a competition task without creating leakage or uncontrolled complexity.

## Required Resources

- **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** — selected preprocessing, pipeline, and feature-engineering sections.
- **scikit-learn User Guide** — Pipeline and ColumnTransformer documentation.
- For PyTorch data pipelines: **Course 1 — PyTorch: Fundamentals**, Module 3 — Data Management in PyTorch:
  - Introduction to Data Pipelines — 3 min
  - Data Access — 6 min
  - Transform Pipelines — 7 min
  - DataLoader — 6 min
  - Bugproof Pipelines — 7 min

## 1. Skill Warm-Up — 0–8 min

Inspect one real dataset and rank its three largest data problems.

## 2. Talk Robin 1 — 8–15 min

Partners compare whether the next gain is more likely to come from cleaning, representation, augmentation, more data, or a different model.

## 3. Entry Check — 15–22 min

Classify each candidate action as cleaning, preprocessing, feature engineering, augmentation, or leakage.

## 4. Core Pattern — 22–35 min

```text
Largest Error Source
→ Lowest-Risk Data Fix
→ Pipeline-Safe Implementation
→ Controlled Validation Test
→ Keep or Revert
```

Priority order:

1. broken labels, corrupt rows, wrong types, duplicates;
2. missing values and category handling;
3. scaling or normalisation where the model needs it;
4. domain features with a clear hypothesis;
5. augmentation or pretrained representations;
6. expensive feature search only after simpler actions fail.

## 5. Guided Practice — 35–53 min

Complete the experiment plan:

| Data issue | Proposed action | Leakage risk | Expected effect | Validation test |
|---|---|---|---|---|
| Missing values |  |  |  |  |
| Rare categories |  |  |  |  |
| Imbalanced classes |  |  |  |  |
| Image/audio variation |  |  |  |  |
| Text length/noise |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

Implement or design one data-engineering change and record:

```text
Hypothesis:
Exact change:
What remains fixed:
Validation score before:
Validation score after:
Runtime before/after:
New failure risk:
Decision: keep / revert / investigate
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit the ranked data-problem list, experiment table, and one reproducible pipeline change.

## Exit Standard

A data-engineering improvement must be fitted only on training data, reproducible in a fresh runtime, and supported by validation evidence.