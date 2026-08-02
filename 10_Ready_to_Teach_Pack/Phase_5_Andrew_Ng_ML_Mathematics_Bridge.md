# Phase 5 Teacher Pack — Andrew ML Mathematics Transition

**Canonical placement:** Sessions 41–43, with just-in-time mathematics continuing through Session 58  
**Phase:** Andrew Ng Machine Learning and Model Labs  
**Primary bridge:** [Andrew ML Mathematics Transition Bridge](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md)

## Purpose

Students have already used Python, NumPy, Pandas, visualisation, Chinese machine-learning concept videos, and AI-history claim analysis. This bridge changes the mode of thinking from primarily verbal concepts to mathematical model descriptions without turning Phase 5 into a disconnected mathematics course.

The teaching goal is mathematical modelling fluency:

```text
task
→ notation and shapes
→ prediction function
→ objective
→ update or model rule
→ evaluation
→ code
→ limitations
```

## Required Teacher Preparation

Before Session 41:

- assign the [Mathematics Bridge Evidence Template](../03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md) as a cold diagnostic;
- classify errors into notation, algebra/functions, shapes, graph reading, loss, gradients, probability, or distance/scale;
- prepare one small dataset that can be used for all three transition sessions;
- prepare hand calculations with numbers small enough to check without a calculator;
- prepare one graph, one contour plot, and one short NumPy implementation;
- review the [Mathematics Bridge Rubric](../04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md);
- identify students who need a parallel remediation packet rather than delaying the entire cohort.

## Entry Diagnostic

The diagnostic is not a memory test for formulas. It checks whether students can:

- identify `X`, `y`, rows, features, outputs, and metrics;
- read a simple function graph;
- calculate a dot product, residual, mean squared error, and Euclidean distance;
- reason about slope direction;
- interpret a supplied gradient update;
- connect an equation to code.

Use the result to form temporary support groups:

| Profile | Main need | Immediate response |
|---|---|---|
| notation weak | symbols have no task meaning | rebuild one notation ledger from a familiar dataset |
| shape weak | rows/features/parameters are confused | require a visible shape ledger beside every operation |
| graph weak | calculations are possible but behaviour is not predictable | use parameter changes and hand-drawn graphs before formulas |
| gradient weak | update rule is memorised without direction reasoning | return to slope signs and contour movement |
| probability weak | score, probability, class, loss, and metric collapse together | use one logistic example with all five objects shown separately |
| code-only | code runs but mathematics cannot be explained | require equation-to-code and code-to-equation translation |

## Canonical Session Map

### Session 41 — Mathematical Language of ML

Required focus:

- `m`, `n`, `X`, `y`, examples, features, parameters, predictions, loss, metric;
- scalar, vector, matrix, row, column, and shape;
- equation-to-words and equation-to-code translation;
- one embedded Kaggle baseline after the task and notation are formalised.

Required evidence:

- completed task formalisation;
- notation ledger;
- shape ledger;
- one translated equation;
- baseline result and explanation.

Teacher gate:

Students do not move into model fitting while they cannot state what one row means, what `y` means, and what shape the model expects.

### Session 42 — Linear Prediction and Loss

Required focus:

- weighted sums and dot products;
- slope and intercept;
- predictions, residuals, squared error, and mean squared error;
- graph changes when parameters change;
- NumPy implementation of the same calculation.

Required evidence:

- hand prediction;
- residual and loss calculation;
- parameter-effect graph;
- code/equation mapping.

Teacher gate:

Students must distinguish a prediction error from the aggregate training objective and from the final evaluation metric.

### Session 43 — Gradient Descent and Cost Surfaces

Required focus:

- feature scale;
- derivative as local change;
- partial derivative and gradient;
- contours and downhill direction;
- learning rate;
- one supplied-gradient parameter update;
- implementation-loop connection.

Required evidence:

- graph slope signs;
- contour interpretation;
- one correct update;
- explanation of slow convergence and overshooting;
- code connection.

Teacher gate:

A student cannot pass while moving parameters in the wrong direction or describing the gradient as the updated parameter itself.

## Standard 75-Minute Structure

| Time | Block | Mathematics-bridge use |
|---:|---|---|
| 0–8 | Skill Warm-Up | one retrieval or hand-calculation task |
| 8–15 | Talk Robin 1 | explain symbols or graph behaviour aloud |
| 15–22 | Entry Check | cold transfer using new values |
| 22–35 | Core Pattern | one mathematical translation pattern only |
| 35–53 | Guided Practice | hand calculation, graph, and code side by side |
| 53–67 | Independent Rebuild | new task or numbers without copied steps |
| 67–75 | Talk Robin 2 + Evidence | oral explanation and evidence submission |

## Just-in-Time Continuation

After Session 43, do not stop teaching mathematics. Revisit only the mathematics required by the current model:

- logistic regression: exponentials, sigmoid, thresholds, logs, log loss;
- regularisation: L1/L2 norms, bias, variance;
- neural-network bridge: matrices, composition, chain-rule intuition;
- trees and ensembles: proportions, impurity, entropy, averaging, residual correction;
- KNN/SVM/K-means: distance, scale, margin, centroid;
- PCA: centring, projection, variance direction, eigen-intuition;
- anomaly detection: mean, variance, density, threshold;
- recommenders: vectors, dot products, similarity, latent factors.

Use the expanded [Mathematics Intuition Map](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Math_Intuition_Map.md).

## Mathematics Gate

Use the public rubric. Recommended passage requires:

- at least **24/32**;
- no critical shape error;
- no confusion between loss and evaluation metric;
- correct gradient-descent direction;
- successful equation-to-code and code-to-equation translation;
- transfer to new numbers or a new task.

A student who misses the gate may continue watching Andrew Ng material only with assigned remediation. The student should not be credited with model mastery until the mathematical evidence is repaired.

## Reteaching Triggers

Reteach when students:

- use symbols without task meanings;
- cannot predict array shapes;
- treat a low training loss as proof of generalisation;
- can calculate but cannot explain a graph;
- can run scikit-learn but cannot state the prediction function or objective;
- memorise the gradient-descent formula but choose the wrong direction;
- confuse probability, threshold, predicted class, loss, and metric;
- ignore scaling in optimisation or distance-based models.

## Non-Negotiable Boundary

Do not spend weeks completing abstract algebra, calculus, or linear-algebra chapters before modelling. Also do not skip mathematics and reduce Andrew Ng ML to `.fit()` and `.predict()`. The required middle ground is enough mathematical fluency to predict model behaviour, diagnose errors, and connect equations to code.