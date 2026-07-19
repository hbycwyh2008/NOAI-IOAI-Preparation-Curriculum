# Phase 5 — Data Analysis and Scikit-Learn Workflows

Sessions 39–44. Standard duration: 90 minutes.

---

## Session 39 — NumPy Arrays, Shapes, Indexing, and Broadcasting

### Resource segment

NumPy official quickstart: array creation, dimensions, indexing, axis operations, reshaping, and broadcasting; IBM Data Analysis with Python: NumPy introduction.

### Essential teaching content

- `shape` describes axis lengths; `ndim` counts axes; `dtype` controls representation.
- Vectorised operations act elementwise without explicit Python loops.
- Axis choice changes the meaning of reductions.
- Broadcasting aligns trailing dimensions when sizes are equal or one.
- Views and copies behave differently under mutation.

### Worksheet

1. State shape, ndim, and size for an array shaped `(4,3,2)`.
2. For a 3×4 array, identify the result shape of `a[1]`, `a[:,2]`, and `a[1:3,1:]`.
3. Calculate row means and column means for a supplied 2×3 matrix.
4. Reshape 24 values into three valid shapes.
5. Is broadcasting valid for `(8,1,4)` plus `(3,4)`? State the output shape.
6. Explain why `b=a[:]` may not be an independent copy.
7. Vectorise the operation `2*x+1` for a list of 1,000 values.

### Guided practice

Students maintain a shape ledger while performing slice, reshape, transpose, concatenate, and reduction operations. They predict before executing.

### Independent task

Implement min-max scaling and z-score scaling with NumPy, including zero-variance handling and tests.

---

## Session 40 — Pandas Data Audit and Visualisation

### Resource segment

Pandas official getting-started tutorials: read/write tabular data, selection, summary statistics, grouping, reshaping; Matplotlib quickstart.

### Essential teaching content

A competition audit must report:

- row/column counts;
- target distribution;
- dtypes and suspicious parsing;
- missingness by column and pattern;
- duplicates and potential entity overlap;
- unique counts and likely IDs;
- numerical ranges/outliers;
- train/test schema differences;
- plots chosen to answer a question.

### Worksheet

1. Write code for shape, dtypes, missing counts, duplicates, and target counts.
2. Explain the difference between `.loc` and `.iloc`.
3. Find rows where `age` is missing and `score > 50`.
4. Group by class and calculate mean feature values.
5. Why can a histogram reveal information that a mean cannot?
6. Identify a likely ID column from unique-count evidence.
7. Choose a plot for class balance, numerical distribution, two-feature relation, and missingness.

### Guided practice

Audit a deliberately flawed dataset. Every observation must be paired with a possible modelling consequence and next check.

### Independent task

Create `data_audit.ipynb` that produces a reproducible audit report and saves at least three figures with meaningful titles and labels.

---

## Session 41 — Cleaning, Missing Values, Categories, and Leakage Prevention

### Resource segment

Google MLCC: **Datasets, Generalization, and Overfitting** data-quality sections; scikit-learn imputation and preprocessing documentation.

### Essential teaching content

- Cleaning decisions depend on how data were generated; do not replace values mechanically.
- Common strategies: drop, constant fill, median/mode, group-based fill, model-based imputation, missing indicator.
- Categorical encoding must handle unseen categories.
- Fit all data-dependent transformations on training data only.
- Leakage can occur through target-derived features, future information, duplicate entities, global aggregates, and preprocessing before splitting.

### Worksheet

1. For five missing-data scenarios, choose drop/impute/indicator and justify.
2. Why can mean imputation distort a skewed feature?
3. Explain `handle_unknown='ignore'` in one-hot encoding.
4. Identify leakage in a feature “final exam grade” used to predict course completion at week 2.
5. Identify leakage when patient records appear in both train and validation.
6. Explain why duplicate removal must consider entity semantics, not only identical rows.
7. Design a `ColumnTransformer` for numeric and categorical columns.

### Guided practice

Students inspect a pipeline with four planted leakage paths and rewrite it as split-first, pipeline-based validation.

### Independent task

Build a robust preprocessing pipeline that handles missing numeric/categorical values and unseen categories. Test on a small validation table containing a new category.

---

## Session 42 — Feature Engineering Across Tabular, Time, Image, and Text Data

### Resource segment

Google MLCC numerical/categorical data modules; IOAI Academy feature-construction topics; teacher examples of windows, moments, token counts, and image patches.

### Essential teaching content

- A feature should be available at prediction time.
- Tabular: ratios, counts, logs, interactions, group aggregates, domain transformations.
- Time series: lags, rolling windows, trends, seasonality—always aligned to prevent future leakage.
- Images: pixels, histograms, edges, patches, pretrained embeddings.
- Text: token counts, lengths, n-grams, embeddings.
- Audio: duration, energy, spectral statistics, Mel features.
- Feature engineering must be validated by controlled experiments.

### Worksheet

1. Label each proposed feature as valid, risky, or leaked.
2. Construct lag-1 and rolling-3 features for a six-step series using past values only.
3. Calculate mean, variance, skew-direction description, min, and max for a small window.
4. Explain one-hot encoding versus embeddings.
5. Explain image patching and how patch size changes sequence length.
6. Create three text features that do not require a pretrained model.
7. Design an experiment testing one feature family while holding model and split fixed.

### Guided practice

Teams receive the same raw sensor dataset and propose feature families. They critique availability time, scale, redundancy, leakage, and expected mechanism.

### Independent task

Create a feature table with at least three justified original features and compare the baseline before/after with the same validation split.

---

## Session 43 — Complete Scikit-Learn Baseline Pipeline

### Resource segment

Scikit-learn: `Pipeline`, `ColumnTransformer`, model selection, preprocessing, and metrics examples.

### Essential workflow

1. Read task and official metric.
2. Audit data and isolate identifiers.
3. Define `X`, `y`, and valid split.
4. Build preprocessing inside a pipeline.
5. Choose a simple baseline model.
6. Fit training data.
7. Predict validation data.
8. Calculate official and diagnostic metrics.
9. Analyse errors and slices.
10. Refit deliberately and create a checked submission.

### Worksheet

1. Explain why pipeline steps prevent fold-level leakage.
2. Complete a `ColumnTransformer` with median imputation/scaling and most-frequent imputation/one-hot encoding.
3. Add `LogisticRegression` or `RandomForestClassifier` to a pipeline.
4. Write code for stratified splitting.
5. Check prediction length and class/probability range.
6. Create a submission DataFrame preserving test IDs.
7. List six submission-schema checks.
8. Explain why a baseline score must be recorded before tuning.

### Guided practice

Build one end-to-end baseline from a fresh runtime. Teacher pauses at every boundary and asks what data are being fitted, transformed, or evaluated.

### Independent task

Rebuild the entire pipeline on a second dataset within 45 minutes and produce a valid submission plus baseline report.

---

## Session 44 — Model Comparison, Cross-Validation, and Tuning

### Resource segment

Scikit-learn model-selection guide: cross-validation, `cross_validate`, `GridSearchCV`, `RandomizedSearchCV`, and evaluation metrics.

### Essential teaching content

- Compare models with identical folds and metrics.
- Report mean, spread, runtime, and failure slices.
- Hyperparameter tuning searches a defined space; it does not guarantee meaningful improvement.
- Nested or final holdout evaluation protects against over-optimising CV when stakes justify it.
- Simpler models may be preferable when performance is similar.

### Worksheet

1. Why must model comparisons use the same CV folds?
2. Interpret mean F1 `.78 ± .02` versus `.80 ± .11`.
3. Choose grid or random search for a small discrete space versus many continuous parameters.
4. Explain why searching 10,000 settings on a tiny dataset can overfit validation.
5. Design a search space for logistic regression and random forest.
6. State when a 0.002 score increase is not worth a 50× runtime increase.
7. Write a model-selection table containing score, variance, runtime, complexity, and error notes.

### Guided practice

Compare logistic regression, decision tree, random forest, and gradient boosting using one repeated evaluation object. Students must recommend a model for both “highest score” and “best competition reliability.”

### Independent task

Run one documented search with a fixed budget. Submit search space, best parameters, CV distribution, validation confirmation, runtime, and a decision to accept or reject the tuned model.

### Phase 5 exit gate

Within 60 minutes, students must audit a new CSV, identify a valid split, build a leakage-safe mixed-type pipeline, produce a valid baseline, calculate the metric, and state the next experiment using evidence.