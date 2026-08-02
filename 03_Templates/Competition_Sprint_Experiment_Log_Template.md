# Competition Sprint Experiment Log Template

Use this record in the fixed order:

```text
Task definition
→ data quality
→ feature engineering
→ model selection
→ tuning
→ model ensembling
→ submission validation
```

Do not skip a stage because a familiar model is available. Use one row per controlled experiment and retain rejected runs.

## 1. Task Definition

```text
Task name:
Task type:
Input modality and X:
Target/output and y:
Prediction-time boundary:
Competition metric:
Secondary diagnostic metric:
Constraints:
Submission schema:
```

## 2. Data-Quality and Validation Gate

```text
Number of rows/samples:
Independent unit:
Group/identity fields:
Time variable and direction:
Missing-value pattern:
Duplicate/near-duplicate risk:
Label-quality risk:
Class/target distribution:
Train/hidden-test drift risk:
Suspicious leakage features:
Frozen validation design:
Random seed or time boundary:
Preprocessing fit boundary:
Why the validation design matches the hidden test:
```

Confirm:

- [ ] obvious target, duplicate, identity, group, time, and preprocessing leakage checked;
- [ ] metric and split frozen before model comparison;
- [ ] labels, IDs, rows, and prediction order aligned;
- [ ] data-quality uncertainties documented.

## 3. Feature-Engineering Record

| Feature experiment | Hypothesis | Named feature group or transform | Everything held fixed | Leakage check | Validation result | Spread | Runtime | Keep/reject |
|---|---|---|---|---|---:|---:|---:|---|
| F00 Raw baseline | reference | minimum valid preprocessing |  |  |  |  |  | keep |
| F01 |  |  |  |  |  |  |  |  |
| F02 |  |  |  |  |  |  |  |  |

Ablation evidence for kept features:

```text
Feature group removed:
Result after removal:
Does the claimed gain disappear?
Conclusion:
```

## 4. Model-Selection Record

Use the same data version, feature pipeline, folds, metric, and seed policy.

| Model ID | Role | Model family | Key defaults | Train score | Validation mean | Spread | Runtime | Main error category | Decision |
|---|---|---|---|---:|---:|---:|---:|---|---|
| M00 | constant/rule floor |  |  |  |  |  |  |  | keep |
| M01 | simple trainable baseline |  |  |  |  |  |  |  |  |
| M02 | contrasting nonlinear/modality model |  |  |  |  |  |  |  |  |

```text
Selected model for tuning:
Why this family:
Dominant failure mode:
Evidence that tuning is more appropriate than another data/feature change:
```

## 5. Controlled Experiment Table

| Experiment ID | Stage | Hypothesis | Single controlled change | Everything held constant | Validation result | Spread | Runtime | Error-category effect | Decision | Next action |
|---|---|---|---|---|---:|---:|---:|---|---|---|
| E00 | baseline | reference | no change |  |  |  |  |  | keep | diagnose |
| E01 | tuning |  |  |  |  |  |  |  | keep/reject/investigate |  |
| E02 | tuning |  |  |  |  |  |  |  | keep/reject/investigate |  |
| E03 | tuning |  |  |  |  |  |  |  | keep/reject/investigate |  |

## 6. Manual Tuning Record

```text
Variable selected:
What the variable controls:
Why this variable follows from the diagnosis:
Search values:
Why this scale/range:
Best value:
Gain over default parameters:
Cross-fold or cross-seed stability:
Runtime/memory effect:
Evidence the gain is not validation noise:
```

## 7. Optional Automated Search Record

Complete only after a manual cycle and only when compute/time justify it.

```text
Search tool:
Objective metric and direction:
Fixed validation protocol:
Search space and rationale:
Number of trials:
Sampler/strategy:
Pruning and invalid-trial rules:
Compute budget:
Best parameters:
Best search result:
Confirmed rerun result:
Gain over manual tuning:
Additional runtime cost:
Was automated search worth the cost? Why?
```

## 8. Model-Ensembling Record

Use the dedicated [Competition Sprint Model Ensembling Record](Competition_Sprint_Model_Ensembling_Record.md) for full evidence.

Summary:

| Ensemble ID | Base models | Method/weights | Prediction source: held-out or OOF | Validation result | Spread | Added cost | Decision |
|---|---|---|---|---:|---:|---:|---|
| EN00 | best single model | none |  |  |  | 0 | reference |
| EN01 |  | mean/vote |  |  |  |  |  |
| EN02 |  | weighted/stacking |  |  |  |  |  |

```text
Why the models are complementary:
Best single-model result:
Best ensemble result:
Is the gain larger than validation noise?
Leakage checks for OOF/stacking:
Final choice: single model / ensemble
```

## 9. Stop Decision

```text
Expected gain from another data/feature/model/tuning/fusion cycle:
Largest remaining error category:
Remaining submission risk:
Remaining fresh-runtime risk:
Remaining time:
Decision: continue / freeze model / simplify / fix pipeline / validate submission
Reason:
```

## 10. Final Evidence Checklist

- [ ] task definition and prediction-time boundary recorded;
- [ ] data-quality report and frozen validation design completed;
- [ ] preprocessing fitted on training data only;
- [ ] feature experiments include hypotheses and ablations;
- [ ] constant, simple, and contrasting model baselines preserved;
- [ ] training and validation scores, spread, runtime, and errors recorded;
- [ ] one variable changed per manual tuning experiment;
- [ ] no test-set or leaderboard tuning;
- [ ] rejected experiments retained;
- [ ] automated search, when used, follows a manual cycle;
- [ ] ensemble, when used, relies on identical held-out or valid OOF predictions;
- [ ] final configuration rerun from a fresh environment;
- [ ] submission schema and row order checked;
- [ ] artificial-intelligence assistance recorded and independently verified.