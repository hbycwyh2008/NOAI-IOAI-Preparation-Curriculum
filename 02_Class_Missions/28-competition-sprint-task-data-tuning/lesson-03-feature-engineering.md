# Lesson 03 — Feature Engineering and Reproducible Pipelines

**Duration:** 75 minutes

## Learning Target

Students can transform audited raw data into model-ready representations, test one feature hypothesis at a time, and build a training/inference pipeline that does not leak information.

## Required Resources

- **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** — selected preprocessing, pipeline, and feature-engineering sections.
- **scikit-learn User Guide** — `Pipeline`, `ColumnTransformer`, encoders, imputers, and feature selection.
- For PyTorch tasks: **Course 1 — PyTorch: Fundamentals**, Module 3 — transform pipelines, `Dataset`, and `DataLoader`.

## 1. Skill Warm-Up — 0–8 min

Given one audited dataset, rank the three highest-value representation problems:

```text
Problem:
Why the current representation is weak:
Lowest-risk fix:
Leakage risk:
Expected validation evidence:
```

## 2. Talk Robin 1 — 8–15 min

Partners compare whether the next gain is most likely to come from:

- repairing types or missing values;
- scaling or encoding;
- domain-derived features;
- aggregation or temporal features;
- augmentation;
- pretrained representations;
- more data rather than more features.

## 3. Entry Check — 15–22 min

Classify each proposed action as **preprocessing**, **feature engineering**, **augmentation**, **representation learning**, or **leakage**.

Examples:

- median imputation fitted inside a pipeline;
- future seven-day mean used to predict tomorrow;
- TF-IDF n-grams;
- image flips used only in training;
- target mean encoding calculated on all rows;
- user-level frequency calculated from past records only.

## 4. Core Pattern — 22–35 min

```text
Frozen Validation Protocol
→ Identify the Largest Representation Limitation
→ State a Feature Hypothesis
→ Implement It Inside a Reproducible Pipeline
→ Change One Feature Group at a Time
→ Compare Validation Mean, Variance, Runtime, and Error Categories
→ Keep, Revert, or Investigate
```

### High-value feature families

| Data type | Baseline representation | Higher-value candidates | Main risk |
|---|---|---|---|
| Numeric/tabular | imputation + raw values | ratios, differences, interactions, grouped aggregates, log transforms | target or group leakage |
| Categorical | one-hot or ordinal encoding | frequency, rare-category grouping, cross features | unseen categories and target encoding leakage |
| Date/time | raw timestamp excluded or decomposed | elapsed time, day/week cycles, lags, rolling statistics | using future information |
| Text | TF-IDF + linear model | n-grams, pretrained embeddings, transformer features | fitting vocabulary or selection on all data |
| Image | resize + normalise | augmentation, pretrained features, crop strategy | augmenting validation or changing label semantics |
| Audio | spectrogram or handcrafted features | augmentation, pretrained audio embeddings | speaker/source leakage |

## 5. Guided Practice — 35–53 min

Complete the experiment table:

| Feature group | Hypothesis | Pipeline implementation | What remains fixed | Leakage test | Validation result | Keep? |
|---|---|---|---|---|---:|---|
| Raw baseline | reference |  |  |  |  | yes |
| Group A |  |  |  |  |  |  |
| Group B |  |  |  |  |  |  |

For tabular tasks, sketch or implement:

```python
preprocess = ColumnTransformer([
    ("num", numeric_pipeline, numeric_columns),
    ("cat", categorical_pipeline, categorical_columns),
])

pipeline = Pipeline([
    ("preprocess", preprocess),
    ("model", model),
])
```

## 6. Independent Rebuild — 53–67 min

Implement or design one feature group and record:

```text
Feature hypothesis:
Exact columns or transform:
Training-only fit boundary:
Baseline validation result:
New validation result:
Cross-fold or seed variation:
Runtime/memory change:
Error categories improved or harmed:
Decision: keep / revert / investigate
```

Then perform an ablation: remove the feature group and confirm whether the claimed gain disappears.

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit:

- a reproducible preprocessing pipeline;
- one feature-hypothesis record;
- before/after validation evidence;
- one ablation result;
- one rejected feature experiment and the reason for rejection.

## Exit Standard

Students may enter model selection only when:

- training and inference use the same pipeline;
- every learned transform is fitted on training data only;
- a raw-feature reference and at least one engineered-feature version have been compared;
- kept features have validation and ablation evidence;
- rejected experiments remain documented.