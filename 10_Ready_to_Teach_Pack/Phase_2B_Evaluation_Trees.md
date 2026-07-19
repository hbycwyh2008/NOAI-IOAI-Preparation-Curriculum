# Phase 2B — Evaluation, Generalisation, Trees, and Ensembles

Sessions 19–26. Standard duration: 90 minutes.

---

## Session 19 — Confusion Matrix, Accuracy, Precision, and Recall

### Resource segment

Google ML Crash Course: **Classification — Accuracy, Precision, Recall**.

### Essential teaching content

- TP, TN, FP, and FN are defined relative to the chosen positive class.
- Accuracy can mislead on imbalanced data.
- Precision asks: among predicted positives, how many are correct?
- Recall asks: among actual positives, how many are found?
- Metric interpretation must include the operational cost of errors.

### Worked example

For TP=36, TN=50, FP=10, FN=4, calculate accuracy, precision, and recall and interpret each in one sentence.

### Worksheet

1. Complete a confusion matrix from 12 supplied predictions and labels.
2. Calculate accuracy, precision, and recall.
3. Which metric emphasises avoiding missed positives?
4. Which metric emphasises trust in positive alerts?
5. A fraud dataset is 99% non-fraud. Why can 99% accuracy be useless?
6. Reverse the positive class and explain which counts change names.
7. Write one scenario where a false positive is more costly and one where a false negative is more costly.

### Guided practice

Teams solve three scenarios—spam, medical screening, and defective-parts inspection—and defend the primary metric.

### Independent task

Write a reusable confusion-matrix calculator from lists of binary labels and predictions; compare with sklearn output.

---

## Session 20 — F1, Specificity, ROC/AUC, and Metric Selection

### Resource segment

Google ML Crash Course: **Classification — F1, ROC and AUC**; StatQuest ROC/AUC overview.

### Essential teaching content

- F1 is the harmonic mean of precision and recall.
- Specificity measures the true-negative rate.
- ROC plots TPR against FPR across thresholds.
- AUC measures ranking quality, not performance at one deployed threshold.
- For severe imbalance, precision-recall analysis may be more informative than ROC alone.

### Worksheet

1. Calculate F1 for precision `.8` and recall `.5`.
2. Calculate specificity from TN=90 and FP=10.
3. Explain why the harmonic mean punishes one weak component.
4. Interpret AUC=.5, .8, and 1.0.
5. Can a model with higher AUC have worse recall at the chosen threshold? Explain.
6. Choose metrics for cancer screening, spam filtering, and rare-defect discovery.
7. Explain macro versus micro averaging at an introductory level.

### Guided practice

Students compare two models using accuracy, F1, recall, specificity, and AUC, then select one for a stated operational goal.

### Independent task

Produce a one-page metric decision memo that states positive class, error costs, validation metric, reporting metrics, and threshold policy.

---

## Session 21 — Cross-Validation and Evaluation Design

### Resource segment

Scikit-learn User Guide: **Cross-validation: evaluating estimator performance**; Google MLCC dataset split sections.

### Essential teaching content

- A single split can be unstable, especially with small data.
- K-fold cross-validation rotates held-out folds and aggregates results.
- Stratification preserves class proportions approximately.
- Grouped data requires group-aware splitting.
- Time-dependent data requires chronological validation.
- Preprocessing must be fitted within each training fold through a pipeline.

### Worksheet

1. In 5-fold CV, what fraction is validation in each fold?
2. Why is random splitting unsafe when multiple rows belong to one patient?
3. Why should future observations not predict the past during validation?
4. Explain leakage caused by scaling before cross-validation.
5. Choose KFold, StratifiedKFold, GroupKFold, or TimeSeriesSplit for four scenarios.
6. Interpret CV scores `[.72,.75,.74,.60,.76]`.
7. State one reason a high mean with high variance is concerning.

### Guided practice

Groups receive dataset descriptions and design splits. Other groups try to identify leakage or mismatch.

### Independent task

Implement two valid CV strategies on provided synthetic data and explain why one better matches the data-generating process.

---

## Session 22 — Train, Validation, Test, and Learning Curves

### Resource segment

Google ML Crash Course: **Datasets, Generalization, and Overfitting**; **Interpreting Loss Curves**.

### Essential teaching content

- Training data fits parameters; validation data selects models and thresholds; test data estimates final performance once.
- Repeated test-set use turns the test set into validation data.
- Learning curves compare train and validation performance as data size or training time changes.
- Distribution mismatch can make all splits misleading.

### Worksheet

1. Assign these decisions to train, validation, or test: weight update, hyperparameter choice, final report.
2. Why is checking the test score after every experiment invalid?
3. Interpret high training and low validation performance.
4. Interpret low training and low validation performance.
5. What pattern suggests that more data may help?
6. What pattern suggests model capacity or features are insufficient?
7. Give one example of train/production distribution mismatch.

### Guided practice

Students annotate six learning-curve diagrams with diagnosis, evidence, and next experiment.

### Independent task

Generate learning curves for two model capacities and write an evidence-based diagnosis.

---

## Session 23 — Underfitting, Overfitting, and Regularisation

### Resource segment

Google ML Crash Course: **Overfitting** and **L2 Regularization**.

### Essential teaching content

- Underfitting: model cannot fit important training structure.
- Overfitting: model captures training-specific noise and fails to generalise.
- Regularisation constrains complexity; L2 penalises large weights, L1 encourages sparsity.
- Early stopping, data augmentation, simpler models, and more representative data can also improve generalisation.
- Regularisation strength is a hyperparameter selected on validation evidence.

### Worksheet

1. Diagnose three train/validation score pairs.
2. Explain how increasing model capacity can first help and later hurt validation performance.
3. Calculate an L2 penalty for weights `[2,-1,3]` before multiplying by lambda.
4. Compare the qualitative effect of L1 and L2.
5. Why can excessive regularisation cause underfitting?
6. Select two remedies for overfitting and explain expected evidence.
7. Explain early stopping using training and validation loss.

### Guided practice

Students tune polynomial degree and regularisation on synthetic data, recording train/validation errors rather than choosing by appearance alone.

### Independent task

Run one controlled regularisation experiment. Change only one factor, preserve the split, and decide keep/reject with evidence.

---

## Session 24 — Decision Trees and Information Gain

### Resource segment

Machine Learning Specialization, Course 2: **Decision Trees**; StatQuest decision-tree basics.

### Essential teaching content

- A tree recursively partitions feature space.
- Classification splits seek purer child nodes.
- Entropy and Gini impurity quantify class mixture.
- Deep trees have low training bias but high overfitting risk.
- Trees handle nonlinear interactions and require less feature scaling than distance/gradient methods.

### Worksheet

1. Calculate Gini impurity for class proportions `.5/.5`, `1/0`, and `.8/.2`.
2. Which node is pure?
3. Given two candidate splits with child counts, identify the better weighted impurity reduction.
4. Explain why a unique ID feature can create misleading splits.
5. Predict the effect of increasing `max_depth`.
6. Why is feature scaling usually unnecessary for ordinary decision trees?
7. Draw a three-node tree for a simple pass/fail rule.

### Guided practice

Manually choose the first split for a small table, then compare with a fitted sklearn tree.

### Independent task

Train trees at depths 1, 3, and unrestricted; compare training/validation performance and explain the chosen depth.

---

## Session 25 — Bagging and Random Forests

### Resource segment

Machine Learning Specialization: **Tree Ensembles**; StatQuest random forests.

### Essential teaching content

- Bagging trains models on bootstrap samples and averages/votes.
- Random forests add feature randomness to reduce correlation between trees.
- Ensembles reduce variance when component errors are not perfectly correlated.
- Out-of-bag samples can provide an internal performance estimate.
- Feature importance can be misleading and is not causal.

### Worksheet

1. Explain bootstrap sampling with replacement.
2. Why can the same row appear multiple times in one bootstrap sample?
3. How does random feature selection increase tree diversity?
4. What problem does bagging mainly address?
5. Why does averaging correlated models help less?
6. Interpret an out-of-bag score.
7. State two cautions when interpreting feature importance.

### Guided practice

Students simulate five tiny tree votes and compare a single unstable tree with majority voting under changed samples.

### Independent task

Compare one decision tree and one random forest using the same split, metric, and preprocessing. Include runtime, validation score, and error overlap.

---

## Session 26 — Boosting and Ensemble Comparison

### Resource segment

Machine Learning Specialization: **Boosted Trees**; StatQuest AdaBoost and gradient boosting overview.

### Essential teaching content

- Boosting builds learners sequentially, focusing later learners on earlier errors or residuals.
- AdaBoost reweights examples; gradient boosting fits residual-like targets.
- Learning rate and number of estimators interact.
- Boosting can be powerful but sensitive to noise, leakage, and poorly chosen validation.
- Bagging primarily reduces variance; boosting often reduces bias while controlling variance.

### Worksheet

1. Contrast parallel bagging with sequential boosting.
2. In AdaBoost, what happens to repeatedly misclassified examples?
3. In gradient boosting regression, what is the next learner trying to predict conceptually?
4. Predict the effect of a very large learning rate.
5. Compare random forest and gradient boosting for training speed, tuning sensitivity, and interpretability.
6. Why can boosting overfit noisy labels?
7. Design a fair experiment comparing logistic regression, random forest, and gradient boosting.

### Guided practice

Students update residuals through two rounds of a toy boosting example and interpret the combined prediction.

### Independent task

Run a controlled three-model comparison with cross-validation. Select a model using metric, variance, runtime, and failure analysis—not score alone.

### Phase 2B exit gate

Without notes, students must calculate a confusion matrix and core metrics, choose a valid split, diagnose learning curves, explain regularisation, trace a tree split, and compare bagging with boosting.