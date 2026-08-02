# Lesson 04 — Model Selection, Baseline Ladder, and Error Analysis

**Duration:** 75 minutes

## Learning Target

Students can select model families only after the data and feature pipeline are trustworthy, establish a baseline ladder, and use training/validation evidence plus error analysis to decide whether greater model complexity is justified.

## Required Video Resource

**Course 2 — Advanced Learning Algorithms**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/advanced-learning-algorithms  
Week 3 — Advice for Applying Machine Learning:

- Establishing a Baseline Level of Performance — 9 min;
- Evaluating a Model — 10 min;
- Error Metrics for Skewed Datasets — 12 min when the task is imbalanced;
- Error Analysis — 8 min as optional review.

## 1. Skill Warm-Up — 0–8 min

For one task, complete:

```text
Output form:
Task type:
Official metric:
Frozen validation design:
Constant or rule baseline:
Simplest trainable baseline:
One stronger contrasting model:
One model family that is currently unjustified:
```

## 2. Talk Robin 1 — 8–15 min

Partners defend two different candidate models. The defence must refer to:

- data size;
- feature type and dimensionality;
- linearity or non-linearity;
- interpretability;
- training/inference cost;
- competition constraints;
- expected failure mode.

## 3. Entry Check — 15–22 min

Match each task to a sensible first comparison:

| Task | Simple baseline | Contrasting model |
|---|---|---|
| Imbalanced tabular classification | logistic regression with class-aware metric | tree ensemble or gradient boosting |
| Tabular regression | mean + linear regression | random forest or gradient boosting regressor |
| Sparse text classification | TF-IDF + logistic regression / linear SVM | pretrained transformer when justified |
| Image classification | constant + small/pretrained CNN baseline | alternative pretrained architecture |
| Clustering | K-means with scaling | DBSCAN or hierarchical clustering when structure supports it |
| Anomaly detection | rule/statistical baseline | Isolation Forest or autoencoder when justified |

## 4. Core Pattern — 22–35 min

```text
Frozen Data and Feature Pipeline
→ Constant or Rule Baseline
→ Simple Interpretable Model
→ One Contrasting Nonlinear or Modality-Specific Model
→ Compare Train Score, Validation Mean, Validation Variance, Runtime, and Memory
→ Inspect Error Categories
→ Select the Smallest Model That Explains a Reliable Gain
```

### Baseline ladder

1. constant, majority, mean, persistence, or simple rule;
2. linear/logistic/statistical baseline;
3. shallow tree, KNN, SVM, or another simple contrasting model;
4. random forest or gradient boosting for tabular data;
5. small or pretrained modality-specific network;
6. larger architecture only after the previous level exposes a clear limitation.

## 5. Guided Practice — 35–53 min

Use the same folds, metric, feature pipeline, and seed policy for every candidate:

| Model | Why this model | Train score | Validation mean | Validation spread | Runtime | Main error category | Decision |
|---|---|---:|---:|---:|---:|---|---|
| Constant/rule | floor |  |  |  |  |  | keep as reference |
| Simple model | baseline |  |  |  |  |  |  |
| Contrasting model | test nonlinearity/modality |  |  |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

Write a model-selection memo:

```text
Task and metric:
Frozen validation protocol:
Data/feature version:
Constant baseline:
Simple trainable baseline:
Contrasting model:
Best reliable result:
Training-validation gap:
Largest error category:
Is the current system underfitting, overfitting, unstable, or pipeline-limited?
Why the chosen model should enter tuning:
What evidence would justify a more complex family:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit:

- the completed comparison table;
- predictions or confusion/error examples from the same validation split;
- the model-selection memo;
- one rejected model and the evidence-based rejection reason.

## Exit Standard

Students may enter tuning only when:

- a constant or rule baseline is preserved;
- at least one simple model and one contrasting model have been evaluated under one protocol;
- training and validation results, spread, runtime, and error categories are recorded;
- the selected model family has a specific diagnosed limitation to tune;
- model complexity is justified by reliable gain, not reputation or leaderboard guesswork.