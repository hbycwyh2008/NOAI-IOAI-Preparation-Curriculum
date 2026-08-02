# Kaggle Learn Embedded Practice Map

Kaggle Learn is not a separate scheduled phase. Selected material is embedded inside Andrew Ng Machine Learning model labs when students need a short workflow rehearsal on a realistic tabular task.

Students do not complete every Kaggle micro-course from beginning to end, and Kaggle does not replace the model-theory, mathematics-intuition, task-recognition, or error-analysis cycle.

## Official Courses

- [Pandas](https://www.kaggle.com/learn/pandas) — optional retrieval when a tabular operation needs repair
- [Data Visualization](https://www.kaggle.com/learn/data-visualization) — optional diagnostic-plot retrieval
- [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — baseline, validation, trees, and random forests
- [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) — missing values, categorical variables, pipelines, cross-validation, and leakage

## Embedded Practice Touchpoints

| Canonical session | Andrew ML context | Selected Kaggle material | Required student action | Evidence |
|---:|---|---|---|---|
| 41 | workflow and model-recognition routine | Intro to Machine Learning: exploration, first model, model validation | identify `X`, `y`, IDs, output, metric, split, and a simple baseline before choosing a model | task-formalisation sheet, baseline score, and split diagram |
| 48 | decision trees and split criteria | Intro to Machine Learning: underfitting/overfitting and decision trees | reproduce a tree baseline, vary one complexity control, and explain the validation pattern | controlled comparison and overfit/underfit diagnosis |
| 49 | random forests and bagging | Intro to Machine Learning: random forests | compare the tree and forest under the identical split and metric | model-comparison record and error differences |
| 50 | boosting and reproducible preprocessing | Intermediate Machine Learning: missing values, categorical variables, pipelines, cross-validation, leakage | place preprocessing inside a pipeline and identify at least one leakage trap | pipeline, cross-validation result, and leakage note |
| 57 | integrated tabular workflow | selected Intro and Intermediate Machine Learning review | complete read → audit → split → preprocess → baseline → one controlled improvement → predict → submission check | fresh-run notebook, experiment log, valid submission, and postmortem |

## Optional Repair Touchpoints

Use Pandas or Data Visualization only when evidence shows a missing prerequisite. These repairs do not create additional canonical sessions and should not displace the current model lab.

Examples:

- Pandas selection/grouping repair before a tabular baseline;
- data-type and missing-value repair before pipeline construction;
- distribution or relationship plots before error diagnosis;
- category-comparison plots before encoding decisions.

## Required Boundaries

- Kaggle is practical workflow rehearsal, not the theory spine.
- The student formalises the task before opening a preferred model notebook.
- Every exercise preserves a simple baseline and one validation protocol.
- Preprocessing is fitted on training data only.
- Public leaderboard movement is not accepted as validation evidence.
- Broad automated search is deferred until diagnosis-first tuning.
- Feature engineering is justified through controlled tests and ablation.
- Session 57 must run from a fresh kernel or equivalent clean environment.

## Completion Standard

Kaggle practice is complete when the student can reproduce the selected workflow on a new tabular dataset, explain each step, identify leakage risks, compare models under one protocol, and produce a valid submission without relying on notebook state.
