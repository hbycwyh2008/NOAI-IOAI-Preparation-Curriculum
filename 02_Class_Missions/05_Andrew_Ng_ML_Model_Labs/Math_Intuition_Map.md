# Mathematics Intuition Map for Andrew Ng ML

Mathematics is learned in two layers:

1. a deliberate transition during Sessions 41–43;
2. just-in-time mathematics paired with each model during Sessions 44–58.

See the [Andrew ML Mathematics Transition Bridge](Andrew_ML_Mathematics_Bridge.md) for the diagnostic, three-session sequence, evidence, gate, and remediation rules.

## Mathematical Translation Routine

For every new model, students move through:

```text
task meaning
→ symbols and shapes
→ prediction rule
→ loss or objective
→ update or decision rule
→ graph or geometric interpretation
→ code
→ limitations
```

Students must not manipulate an equation before identifying what its objects mean in the current task.

## Transition Mathematics — Sessions 41–43

| Session | Required mathematics | Required transfer |
|---:|---|---|
| 41 | algebraic notation, functions, scalar/vector/matrix, `m` examples, `n` features, shapes, parameters, predictions, loss, metric | task language ↔ notation ↔ NumPy-style code |
| 42 | weighted sums, dot products, slope, intercept, residuals, squared error, mean squared error | hand prediction ↔ graph ↔ vectorised implementation |
| 43 | feature scale, cost surfaces, contours, derivative, partial derivative, gradient, learning rate, update rule | graph direction ↔ supplied-gradient update ↔ implementation loop |

The transition gate uses the [Andrew ML Mathematics Bridge Rubric](../../04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md).

## Just-in-Time Model Mathematics

| Model/topic | Mathematical objects | Required intuition and evidence | Best support |
|---|---|---|---|
| Linear regression | vectors, weights, bias, dot product, residual, MSE | compute prediction/loss; predict slope/intercept effects; connect equation to vectorised code | 3Blue1Brown for vectors/calculus; StatQuest for regression |
| Multiple regression and gradient descent | matrix-shaped `X`, feature scale, contour, partial derivative, gradient | state shapes; interpret contours; complete one update; diagnose learning rate and scaling | 3Blue1Brown + Andrew Ng |
| Logistic regression | exponential, sigmoid, probability, threshold, logarithm, log loss | separate score/probability/class/loss/metric; explain confident wrong penalties | StatQuest + Andrew Ng |
| Classification metrics | counts, rates, ratios, threshold curves | calculate confusion-matrix metrics and justify metric/threshold choice | StatQuest |
| Regularisation | parameter magnitude, L1/L2 norms, penalty, bias and variance | predict shrinkage effects; explain why lower training loss is not the only goal | StatQuest |
| Neural-network bridge | matrix multiplication, weighted sums, activation composition, chain-rule intuition | annotate tensor/array shapes and trace a small forward pass | 3Blue1Brown + Andrew Ng |
| Decision trees | proportions, impurity, entropy, information gain | calculate a small split score and explain uncertainty reduction | StatQuest |
| Random forests and bagging | sampling, averaging, variance | explain how averaging unstable learners can reduce variance | StatQuest |
| Boosting | residuals, weighted errors, additive correction | explain how a new learner focuses on previous mistakes | StatQuest + Andrew Ng |
| KNN | coordinates, Euclidean distance, scale, neighbourhood voting | calculate distances; show how scaling changes neighbours | StatQuest |
| SVM | boundary, perpendicular distance, margin, support points | explain maximum-margin geometry and sensitivity to scale | StatQuest / Bohrium |
| K-means | mean, centroid, squared distance, iterative objective | complete one assignment/update cycle and explain objective decrease | StatQuest |
| PCA | centring, projection, variance direction, eigenvector/eigenvalue intuition | project a small point; explain retained versus discarded variation | 3Blue1Brown + StatQuest |
| Anomaly detection | mean, variance, normal-density intuition, threshold | explain low-density detection and threshold trade-offs | StatQuest |
| Recommenders | vectors, dot product, similarity, latent factors, matrix structure | compute a similarity/prediction and explain latent representation limits | 3Blue1Brown + Andrew Ng |
| Model comparison | validation mean/spread, runtime, error categories | compare models under one protocol without treating tiny score differences as certainty | prior Phase 5 evidence |

## Required Mathematical Evidence for Every Model

At least one of the following must appear in the model record:

- hand prediction or decision calculation;
- annotated shape ledger;
- graph or geometric interpretation;
- small loss/objective calculation;
- parameter-effect prediction;
- equation-to-code translation;
- mathematical explanation of a limitation or failure mode.

A notebook output alone is not mathematical evidence.

## Depth Rule

Students do not need large symbolic derivations before modelling. They must be able to:

- explain what each mathematical object represents;
- state its shape, range, or units where relevant;
- perform a small representative calculation;
- predict the effect of a change;
- connect the mathematics to model behaviour and code;
- distinguish what the mathematics optimises from what the competition or real task actually values;
- state what a good mathematical fit does not prove about generalisation, causality, understanding, or safety.
