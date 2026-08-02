# Lesson 02 — Data Quality, Validation Design, and Leakage Prevention

**Duration:** 75 minutes

## Learning Target

Students can decide whether a competition dataset is trustworthy enough for modelling, choose a validation design that matches the hidden test, and block target, identity, group, temporal, and preprocessing leakage.

## Required Resources

- **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** — selected end-to-end project and data-preparation sections.
- **scikit-learn User Guide** — model selection, preprocessing, `Pipeline`, `GroupKFold`, and time-series split documentation.
- For PyTorch tasks: **Course 1 — PyTorch: Fundamentals**, Module 3 — Data Management in PyTorch.

## 1. Skill Warm-Up — 0–8 min

Inspect the task files before discussing a model. Record:

```text
Rows or samples:
Input columns or modalities:
Target or hidden output:
IDs and possible groups:
Time variables:
Missing values:
Duplicates or near-duplicates:
Class or target distribution:
Suspicious answer-revealing fields:
```

## 2. Talk Robin 1 — 8–15 min

Partners answer:

1. What is the true independent unit: row, user, patient, speaker, document, experiment, image source, or time period?
2. Which information will genuinely exist at prediction time?
3. What difference between training and hidden-test data is most likely?

## 3. Entry Check — 15–22 min

Classify each issue as **data quality**, **split design**, **leakage**, or **acceptable variation**:

- one user appears in many rows;
- the scaler was fitted before the split;
- a filename contains the class label;
- 18% of one sensor column is missing;
- the task predicts the future but the split is random;
- a rare class appears only twice in validation.

## 4. Core Pattern — 22–35 min

```text
Define X, y, Metric, and Prediction Time
→ Audit Schema, Missingness, Duplicates, Labels, and Distribution
→ Define the Independent Unit
→ Choose Random, Stratified, Grouped, or Time-Based Validation
→ Fit Every Learned Preprocessing Step on Training Only
→ Run Leakage and Split-Sanity Tests
→ Freeze the Validation Protocol
```

### Data-quality priority order

1. wrong labels, corrupt samples, impossible values, and schema errors;
2. exact and near-duplicate leakage;
3. incorrect split unit or time direction;
4. missingness and category coverage;
5. class imbalance and rare-group coverage;
6. train/validation/test distribution drift.

## 5. Guided Practice — 35–53 min

Complete one row for each supplied dataset:

| Dataset | Independent unit | Main quality risk | Split strategy | Leakage test | Why it matches hidden test |
|---|---|---|---|---|---|
| Tabular |  |  |  |  |  |
| Image/audio |  |  |  |  |  |
| Time series |  |  |  |  |  |

Then write a minimal audit in code or pseudocode:

```python
print(data.shape)
print(data.dtypes)
print(data.isna().mean().sort_values(ascending=False).head(20))
print(data.duplicated().sum())
print(data[target].value_counts(dropna=False, normalize=True))
# Add group, time, label, and suspicious-column checks for the actual task.
```

## 6. Independent Rebuild — 53–67 min

Create a one-page validation memo:

```text
Prediction-time boundary:
Independent unit:
Split method:
Random seed or time boundary:
Stratification/group/time rule:
Preprocessing fit boundary:
Leakage tests performed:
Largest remaining data-quality uncertainty:
Why this validation score should predict hidden-test performance:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit:

- the data-quality audit;
- the split diagram or code;
- the leakage checklist;
- the validation memo;
- one example of a falsely high score that the chosen checks would prevent.

## Exit Standard

Students may enter feature engineering only when:

- the validation split is frozen and defensible;
- obvious target, duplicate, group, temporal, identity, and preprocessing leakage has been checked;
- missingness, labels, duplicates, and distribution have been recorded;
- the evaluation metric and prediction-time boundary are explicit.

No baseline comparison, tuning result, or ensemble result is valid before this gate is passed.