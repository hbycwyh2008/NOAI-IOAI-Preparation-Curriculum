# Lesson 03 — Data Audit, Validation Split, and Leakage Prevention

**Duration:** 75 minutes

## Learning Target

Students can audit a competition dataset, identify the correct split unit, and prevent target, group, temporal, identity, and preprocessing leakage.

## Required Resources

- **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** — selected end-to-end project and data-preparation sections.
- **scikit-learn User Guide** — model selection and preprocessing documentation.
- For PyTorch tasks: **Course 1 — PyTorch: Fundamentals**, Module 3 — Data Management in PyTorch.

## 1. Skill Warm-Up — 0–8 min

Inspect the files, columns, shapes, sample identifiers, labels, missing values, class counts, and possible grouping variables.

## 2. Talk Robin 1 — 8–15 min

Discuss:

1. What is the true independent unit?
2. Could two rows come from the same person, source, experiment, speaker, patient, document, or image?
3. Is time order meaningful?
4. Which feature may secretly reveal the target?

## 3. Entry Check — 15–22 min

Complete:

```text
Number of rows/samples:
Target column or hidden target:
Unique groups:
Time variable:
Missing-value pattern:
Duplicate risk:
Class imbalance:
Proposed split unit:
```

## 4. Core Pattern — 22–35 min

```text
Audit → Define Independent Unit → Choose Split Strategy → Fit Preprocessing on Training Only → Verify No Leakage
```

Leakage checklist:

- target-derived feature;
- duplicate across train and validation;
- same group in both splits;
- future information in past prediction;
- scaling/encoding fitted before splitting;
- augmentation applied to validation;
- hidden label encoded in filename or metadata.

## 5. Guided Practice — 35–53 min

For three datasets, choose random, stratified, grouped, or time-based splitting and explain why.

| Dataset | Independent unit | Split strategy | Leakage risk | Test |
|---|---|---|---|---|
| Tabular |  |  |  |  |
| Image/audio |  |  |  |  |
| Time series |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

Create a validation memo:

```text
Split unit:
Split method:
Random seed:
Stratification/group/time rule:
Preprocessing fit boundary:
Leakage tests:
Why the validation score should predict competition performance:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit the audit table, leakage checklist, and validation memo. Explain one leakage case that would produce a falsely high score.

## Exit Standard

No model comparison or tuning result is valid until the split and leakage checks are defensible.