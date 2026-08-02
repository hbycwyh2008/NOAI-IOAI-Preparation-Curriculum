# Competition Sprint Model Ensembling Record

Use this template only after at least two single models have passed the same validation protocol.

## Entry Gate

```text
Task:
Metric:
Validation design:
Prediction rows used for ensemble selection:
Best single model:
Best single-model validation result:
Validation noise or fold/seed spread:
Available time, memory, and inference budget:
```

Confirm:

- [ ] every base model uses the same task definition and metric;
- [ ] every base model has been evaluated on identical held-out rows or by valid OOF prediction;
- [ ] no test labels or public-leaderboard iteration were used to choose the ensemble;
- [ ] in-sample predictions will not be used to train a stacking meta-model;
- [ ] runtime and memory constraints are known.

## Base-Model Evidence

| Model ID | Feature representation | Model family | Validation score | Fold/seed spread | Runtime | Main error category | Saved prediction path |
|---|---|---|---:|---:|---:|---|---|
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |

## Diversity Analysis

| Pair | Prediction correlation/agreement | Errors shared | Errors unique to first | Errors unique to second | Complementary enough? |
|---|---:|---:|---:|---:|---|
| A / B |  |  |  |  |  |
| A / C |  |  |  |  |  |
| B / C |  |  |  |  |  |

Describe why the selected models should be complementary:

```text
Different model family / seed / fold / feature representation / architecture:
Observed complementary cases:
Reason fusion should reduce bias or variance:
```

## Ensemble Ladder

Test the simplest valid combination first.

| Ensemble ID | Members | Method | Weights or meta-model | Validation score | Spread | Added runtime/memory | Decision |
|---|---|---|---|---:|---:|---:|---|
| E00 | best single model | none | 1.0 |  |  | 0 | reference |
| E01 |  | mean / vote |  |  |  |  |  |
| E02 |  | weighted mean |  |  |  |  |  |
| E03 |  | stacking, OOF only |  |  |  |  |  |

## Leakage and Reproducibility Check

```text
How were held-out or OOF predictions generated?
Were base models trained without seeing the rows they predict for ensemble selection?
How were weights selected?
How was repeated weight searching limited?
How will test predictions be generated consistently?
Can the ensemble be reproduced from saved configs and checkpoints?
```

## Final Decision

```text
Best single-model result:
Best ensemble result:
Absolute and relative gain:
Is the gain larger than validation noise?
Additional compute and submission risk:
Chosen final system: single model / ensemble
Reason:
Rejected ensemble attempts and why:
```

## Exit Checklist

- [ ] best single model remains the comparison reference;
- [ ] diversity was measured, not assumed;
- [ ] simple averaging or voting was tested before stacking;
- [ ] stacking, when used, relies on OOF predictions;
- [ ] ensemble weights were not tuned on the hidden test or leaderboard;
- [ ] gain is stable across folds or seeds;
- [ ] final runtime, memory, checkpoint, and submission logic are documented;
- [ ] rejected ensembles remain in the evidence record.