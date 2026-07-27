# Hyperparameter-Tuning Video Resource Map

This file lists the exact video sections used during the competition-sprint tuning lessons. Use the full course names in all student instructions.

The durations below are the current Coursera-listed video lengths checked on 2026-07-27. Course structures may change, so verify the page before each cohort.

## A. Classical Machine-Learning Diagnosis and Tuning

**Course:** Course 2 — Advanced Learning Algorithms, part of the Machine Learning Specialization  
**Coursera link:** https://www.coursera.org/learn/advanced-learning-algorithms  
**Section:** Week 3 — Advice for Applying Machine Learning

| Video | Duration | Sprint use |
|---|---:|---|
| Deciding what to try next | 4 min | prevents random tuning |
| Evaluating a model | 10 min | establishes valid evaluation before tuning |
| Model selection and training/cross validation/test sets | 14 min | prevents test-set tuning and split misuse |
| Diagnosing bias and variance | 11 min | decides whether to add capacity, regularisation, features, or data |
| Establishing a baseline level of performance | 9 min | defines what improvement means |
| Learning curves | 12 min | distinguishes data shortage from model limitation |
| Iterative loop of machine-learning development | 8 min | structures controlled competition experiments |
| Error analysis | 8 min | directs the next experiment toward the largest error category |
| Adding data | 14 min | decides whether more or better data is worth the time |
| Full cycle of a machine-learning project | 9 min | integrates task, data, model, evaluation, and deployment decisions |

### Required selection for Lesson 05

Watch these four videos:

1. Deciding what to try next — 4 min
2. Model selection and training/cross validation/test sets — 14 min
3. Diagnosing bias and variance — 11 min
4. Iterative loop of machine-learning development — 8 min

**Required video time:** 37 minutes.

Use `Learning curves` and `Error analysis` as optional review or pre-class work.

---

## B. Deep-Learning Diagnosis, Optimisation, and Hyperparameter Search

**Course:** Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization, part of the Deep Learning Specialization  
**Coursera link:** https://www.coursera.org/learn/deep-neural-network

### Week 1 — Practical Aspects of Deep Learning

| Video | Duration | Sprint use |
|---|---:|---|
| Train / Dev / Test sets | 12 min | correct split design |
| Bias / Variance | 9 min | diagnosis before tuning |
| Basic Recipe for Machine Learning | 6 min | chooses the next intervention |
| Regularization | 10 min | controls overfitting |
| Normalizing Inputs | 5 min | improves optimisation stability |
| Weight Initialization for Deep Networks | 6 min | improves convergence |

### Week 2 — Optimization Algorithms

| Video | Duration | Sprint use |
|---|---:|---|
| Mini-batch Gradient Descent | 11 min | batch-size and update-frequency reasoning |
| Gradient Descent with Momentum | 9 min | optimiser comparison |
| RMSprop | 8 min | adaptive update intuition |
| Adam Optimization Algorithm | 7 min | practical default optimiser reasoning |
| Learning Rate Decay | 7 min | scheduler decisions |

### Week 3 — Hyperparameter Tuning, Batch Normalization and Programming Frameworks

| Video | Duration | Sprint use |
|---|---:|---|
| Tuning Process | 7 min | orders the tuning process |
| Using an Appropriate Scale to Pick Hyperparameters | 9 min | designs sensible search spaces |
| Hyperparameters Tuning in Practice: Pandas vs. Caviar | 7 min | adapts tuning strategy to compute and dataset changes |
| Normalizing Activations in a Network | 9 min | introduces batch normalisation |
| Fitting Batch Norm into a Neural Network | 13 min | places batch normalisation correctly |
| Why Does Batch Norm Work? | 12 min | explains its stabilising effect |
| Batch Norm at Test Time | 6 min | prevents inference mistakes |

### Required selection for Lesson 06

Watch these six videos:

1. Basic Recipe for Machine Learning — 6 min
2. Adam Optimization Algorithm — 7 min
3. Learning Rate Decay — 7 min
4. Tuning Process — 7 min
5. Using an Appropriate Scale to Pick Hyperparameters — 9 min
6. Hyperparameters Tuning in Practice: Pandas vs. Caviar — 7 min

**Required video time:** 43 minutes.

The remaining videos are assigned only when the task shows the corresponding problem.

---

## C. PyTorch Hyperparameter Optimisation and Efficiency

**Course:** Course 2 — PyTorch: Techniques and Ecosystem Tools, part of the DeepLearning.AI PyTorch for Deep Learning Professional Certificate  
**Coursera link:** https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools  
**Section:** Module 1 — Hyperparameter Optimization

| Video | Duration | Sprint use |
|---|---:|---|
| Evaluation Metrics | 5 min | confirms the optimisation target |
| Introduction to Optimization | 4 min | frames systematic improvement |
| Learning Rate Schedulers | 5 min | implements learning-rate schedules |
| Tuning Hyperparameters | 7 min | selects tunable variables and ranges |
| Flexible Architecture Design | 7 min | exposes architecture choices safely |
| Hyperparameter Optimization with Optuna | 10 min | introduces automated search |
| Optimizing Model Efficiency | 11 min | balances score, memory, inference time, and training cost |

### Required selection for Lesson 07

Watch these four videos:

1. Learning Rate Schedulers — 5 min
2. Tuning Hyperparameters — 7 min
3. Hyperparameter Optimization with Optuna — 10 min
4. Optimizing Model Efficiency — 11 min

**Required video time:** 33 minutes.

### Optional implementation labs

- Hyperparameter Tuning: Learning Rate and Metrics — 60 min
- Schedulers in PyTorch — 60 min
- Hyperparameter Optimization with Optuna — 60 min
- Efficiency vs Performance Metrics — 60 min

Use at most one lab during the competition sprint. Do not assign all four before students can complete a manual controlled experiment.

---

## D. PyTorch Foundation Review Before Tuning

**Course:** Course 1 — PyTorch: Fundamentals  
**Coursera link:** https://www.coursera.org/learn/pytorch-fundamentals  
**Section:** Module 2 — The PyTorch Workflow

| Video | Duration | Sprint use |
|---|---:|---|
| Loss | 5 min | confirms what training minimises |
| Optimizers and Gradients | 6 min | reviews parameter updates |
| Image Classification — Part 2: Training and Evaluating the Model | 4 min | reviews train/evaluate separation |

Assign these only when a student cannot explain the training loop before tuning.

## Tuning Order Used in This Repo

```text
Metric and Validation
→ Baseline
→ Error Analysis
→ Data Pipeline
→ Model Capacity or Model Family
→ Learning Rate
→ Regularisation
→ Batch Size and Optimiser
→ Scheduler
→ Automated Search
→ Efficiency and Submission Risk
```

Do not use automated search to hide weak task recognition, leakage, an invalid metric, or a broken baseline.
