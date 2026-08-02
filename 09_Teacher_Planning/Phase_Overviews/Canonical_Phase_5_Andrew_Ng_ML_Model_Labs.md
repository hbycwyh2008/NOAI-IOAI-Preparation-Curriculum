# Canonical Phase 5 — Andrew Ng ML Model Labs

**Sessions:** 41–58  
**Canonical folder:** `02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/`

## Purpose

Teach classical machine-learning models one by one through task recognition, an explicit mathematics transition, implementation, typical tasks, error analysis, and model cards.

## Entry Conditions

Students pass the AI History phase gate and can distinguish demonstrated capability from unsupported claims. Before Session 41, students complete the mathematics-bridge diagnostic so notation, shape, graph, loss, gradient, probability, and distance gaps are visible.

## Delivery Priorities

### Sessions 41–43 — Mathematics Transition

Students move from verbal concepts and data arrays into Andrew Ng’s mathematical language:

```text
task
→ notation and shapes
→ prediction function
→ loss or objective
→ gradient or model rule
→ metric
→ code
→ limitations
```

The three bridge sessions cover:

1. task formalisation, scalar/vector/matrix objects, `m`, `n`, `X`, `y`, parameters, predictions, loss, metric, and equation-to-code translation;
2. weighted sums, dot products, slope, intercept, residuals, squared error, and mean squared error;
3. feature scale, cost surfaces, derivatives, partial derivatives, gradients, learning rate, and gradient descent.

Use the [Andrew ML Mathematics Transition Bridge](../../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md) and the [Phase 5 Mathematics Teacher Pack](../../10_Ready_to_Teach_Pack/Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md).

### Sessions 44–58 — Model-by-Model Mathematics

For every model, preserve this loop:

```text
recognise the task
→ identify X, y, labels, output, baseline, metric, symbols, and shapes
→ learn the required mathematical intuition
→ study the Andrew Ng lesson
→ use StatQuest or 3Blue1Brown for targeted clarification
→ translate equation to code and code back to mathematics
→ implement the model
→ complete a typical task
→ analyse errors and limitations
→ update the model card
```

Cover regression, logistic classification, regularisation, trees, random forests, boosting, KNN, SVM, K-means, PCA, anomaly detection, recommender systems, and the Machine Learning Specialization neural-network bridge.

Kaggle Learn is embedded as short workflow rehearsal for Pandas, splitting, pipelines, cross-validation, leakage prevention, and tabular baselines. It is not a separate scheduled phase.

## Required Evidence

- mathematics-bridge diagnostic;
- notation and shape ledger;
- equation-to-words and equation-to-code translation;
- hand prediction, loss, distance, impurity, or other representative calculation;
- graph, contour, or geometric explanation;
- one correct gradient or model-rule explanation;
- model-recognition record before implementation;
- reproducible baseline and validation protocol;
- one controlled improvement;
- error analysis and limitations;
- model card comparing fit, assumptions, mathematical behaviour, cost, and failure modes.

## Exit Gate

Given an unfamiliar task, the student identifies `X`, `y`, label availability, output type, task family, baseline, metric, candidate models, and likely limitations. The student then:

- states the type and shape of the main mathematical objects;
- translates the model rule into task language and code;
- performs a small representative calculation;
- explains the objective and, where relevant, update direction;
- distinguishes training loss from evaluation evidence;
- implements and evaluates a defensible classical baseline.

The mathematics transition requires at least **24/32** on the public rubric, with no critical shape, loss, or gradient-direction error.
