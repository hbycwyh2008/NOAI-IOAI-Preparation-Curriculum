# Lesson 07 — Model Ensembling: Voting, Averaging, and Stacking

**Duration:** 75 minutes

## Learning Target

Students can decide whether model fusion is justified, measure error diversity using out-of-fold or held-out predictions, and build a simple ensemble that is reliably better than the best single model without leaking validation information.

## Required Prior Evidence

Students must already have:

- a frozen validation protocol;
- at least two independently evaluated strong models;
- saved out-of-fold or held-out predictions;
- runtime and memory measurements;
- an error-analysis table for each candidate model.

Automated tuning is not a prerequisite. A well-understood pair of manually tuned models is sufficient.

## 1. Skill Warm-Up — 0–8 min

Given two models, record:

```text
Model A validation score:
Model B validation score:
Prediction correlation or agreement:
Examples A gets right and B gets wrong:
Examples B gets right and A gets wrong:
Expected reason fusion may or may not help:
```

## 2. Talk Robin 1 — 8–15 min

Partners compare:

- two similarly scored models with highly correlated predictions;
- a strong model and a slightly weaker but clearly different model;
- two seeds of the same architecture;
- models trained on different feature representations.

Decide which pair has the highest expected ensemble value and why.

## 3. Entry Check — 15–22 min

Classify each proposal as **valid**, **weak**, or **leaky**:

- average probabilities from two models evaluated on the same held-out rows;
- train a stacking meta-model on predictions made for the same rows used to train the base models;
- use out-of-fold predictions to train a meta-model;
- add a very weak model only to increase model count;
- average a linear model and a tree model whose errors are complementary;
- tune ensemble weights repeatedly against the public leaderboard.

## 4. Core Pattern — 22–35 min

```text
Two or More Strong Single Models
→ Save Predictions on Identical Validation Rows
→ Measure Score, Prediction Correlation, and Error Overlap
→ Start with Simple Mean or Majority Vote
→ Test a Small Number of Justified Weights
→ Use OOF Predictions for Stacking
→ Compare Ensemble Gain, Variance, Runtime, Memory, and Submission Risk
→ Keep Only a Reproducible Improvement
```

### Fusion methods

| Method | Inputs | Strength | Main risk |
|---|---|---|---|
| Majority voting | predicted classes | simple and robust | discards confidence information |
| Probability averaging | class probabilities | strong default for classification | probabilities may be poorly calibrated |
| Weighted averaging | probabilities or continuous predictions | can favour the stronger model | validation overfitting through repeated weight search |
| Seed/fold averaging | same architecture across seeds/folds | reduces variance | compute cost and low model diversity |
| Stacking | out-of-fold base predictions | learns nonlinear combinations | severe leakage if OOF construction is wrong |

## 5. Guided Practice — 35–53 min

Complete:

| Candidate | Single-model score | Correlation/agreement | Unique correct cases | Runtime | Ensemble role |
|---|---:|---:|---:|---:|---|
| Model A |  |  |  |  | anchor |
| Model B |  |  |  |  | complement / reject |
| Model C |  |  |  |  | complement / reject |

Test a limited ensemble ladder:

| Ensemble | Weights/method | Validation score | Spread across folds/seeds | Runtime/memory cost | Keep? |
|---|---|---:|---:|---:|---|
| A only | 1.0 |  |  |  | reference |
| A + B | 0.5 / 0.5 |  |  |  |  |
| A + B | one justified alternative |  |  |  |  |
| Stacking | OOF only, when justified |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

Implement or specify one ensemble and record:

```text
Base models:
Why their errors should be complementary:
Prediction rows used to select the ensemble:
Fusion rule:
Weight-selection rule:
Best single-model result:
Ensemble result:
Cross-fold/seed stability:
Additional training and inference cost:
Leakage checks:
Decision: keep / reject / simplify
```

For averaging:

```python
ensemble_prediction = 0.5 * prediction_a + 0.5 * prediction_b
```

For stacking, the meta-model may be trained only on out-of-fold base predictions, never on in-sample base predictions.

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit:

- the model-diversity table;
- saved validation or OOF predictions;
- the ensemble comparison table;
- the fusion decision memo;
- one explanation of why a strong ensemble is not simply a collection of many models.

## Exit Standard

Students pass only when:

- every base model is independently valid under the same evaluation protocol;
- fusion uses identical held-out rows or correctly generated OOF predictions;
- the ensemble is compared with the best single model, not only a weak baseline;
- gain is stable enough to exceed validation noise;
- runtime, memory, reproducibility, and submission risk remain acceptable;
- rejected models and weight choices are documented.