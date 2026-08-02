# Hyperparameter-Tuning Video Resource Map

This file lists the exact video sections used during the competition-sprint tuning lessons.

The required scheduled tuning packages apply to **Lessons 05 and 06**. PyTorch schedulers, Optuna, and broader automated search are an **optional extension**, because the scheduled Lesson 07 is now model ensembling.

Course structures can change. Verify titles and durations before each cohort.

## Delivery Rule

Required packages are pre-class viewing or separately scheduled resource sessions. They are not played in full during the eight-minute Skill Warm-Up.

Before class, students submit:

1. video titles completed;
2. one decision rule from each video;
3. one point they cannot yet apply;
4. one question to test during the lesson.

---

## A. Classical Machine-Learning Diagnosis and Tuning — Required for Lesson 05

**Course:** Course 2 — Advanced Learning Algorithms, part of the Machine Learning Specialization  
**Coursera:** https://www.coursera.org/learn/advanced-learning-algorithms  
**Section:** Week 3 — Advice for Applying Machine Learning

| Video | Duration | Sprint use |
|---|---:|---|
| Deciding What to Try Next | 4 min | prevents random tuning |
| Evaluating a Model | 10 min | confirms evaluation before tuning |
| Model Selection and Training/Cross Validation/Test Sets | 14 min | prevents split misuse and test tuning |
| Diagnosing Bias and Variance | 11 min | chooses capacity, regularisation, feature, or data actions |
| Establishing a Baseline Level of Performance | 9 min | defines meaningful improvement |
| Learning Curves | 12 min | tests whether more data may help |
| Iterative Loop of Machine-Learning Development | 8 min | structures controlled experiments |
| Error Analysis | 8 min | points to the largest error category |

### Required Selection

1. Deciding What to Try Next — 4 min
2. Model Selection and Training/Cross Validation/Test Sets — 14 min
3. Diagnosing Bias and Variance — 11 min
4. Iterative Loop of Machine-Learning Development — 8 min

**Required viewing time:** 37 minutes.

Optional review:

- Learning Curves — 12 min
- Error Analysis — 8 min

### In-Class Retrieval

Students inspect one train/validation result and identify:

- the dominant failure mode;
- one parameter family worth testing;
- one action that should wait;
- the validation evidence required before keeping a change.

---

## B. Deep-Learning Diagnosis and Tuning — Required for Lesson 06

**Course:** Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization, part of the Deep Learning Specialization  
**Coursera:** https://www.coursera.org/learn/deep-neural-network

### Useful Sections

| Video | Duration | Sprint use |
|---|---:|---|
| Train / Dev / Test Sets | 12 min | split design |
| Bias / Variance | 9 min | diagnosis before tuning |
| Basic Recipe for Machine Learning | 6 min | next-action selection |
| Regularization | 10 min | overfitting control |
| Normalizing Inputs | 5 min | optimisation stability |
| Mini-Batch Gradient Descent | 11 min | batch-size reasoning |
| Adam Optimization Algorithm | 7 min | optimiser reasoning |
| Learning Rate Decay | 7 min | scheduler decisions |
| Tuning Process | 7 min | tuning order |
| Using an Appropriate Scale to Pick Hyperparameters | 9 min | sensible ranges |
| Hyperparameters Tuning in Practice: Pandas vs. Caviar | 7 min | compute-aware strategy |

### Required Selection

1. Basic Recipe for Machine Learning — 6 min
2. Adam Optimization Algorithm — 7 min
3. Learning Rate Decay — 7 min
4. Tuning Process — 7 min
5. Using an Appropriate Scale to Pick Hyperparameters — 9 min
6. Hyperparameters Tuning in Practice: Pandas vs. Caviar — 7 min

**Required viewing time:** 43 minutes.

The remaining videos are assigned only when the task shows the corresponding problem.

### In-Class Retrieval

Students classify one training curve as:

- optimisation failure;
- underfitting;
- overfitting;
- unstable validation;
- data-pipeline or metric failure.

They then identify the first parameter to change and what must remain fixed.

---

## C. PyTorch Schedulers, Optuna, and Efficiency — Optional Extension

**Course:** Course 2 — PyTorch: Techniques and Ecosystem Tools, part of the DeepLearning.AI PyTorch for Deep Learning Professional Certificate  
**Coursera:** https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools  
**Section:** Module 1 — Hyperparameter Optimization

| Video | Duration | Extension use |
|---|---:|---|
| Evaluation Metrics | 5 min | confirms the objective |
| Introduction to Optimization | 4 min | frames systematic search |
| Learning Rate Schedulers | 5 min | implements schedules |
| Tuning Hyperparameters | 7 min | selects variables and ranges |
| Flexible Architecture Design | 7 min | exposes bounded architecture choices |
| Hyperparameter Optimization with Optuna | 10 min | introduces automated search |
| Optimizing Model Efficiency | 11 min | balances score, memory, latency, and cost |

### Suggested Optional Package

1. Learning Rate Schedulers — 5 min
2. Tuning Hyperparameters — 7 min
3. Hyperparameter Optimization with Optuna — 10 min
4. Optimizing Model Efficiency — 11 min

**Optional viewing time:** 33 minutes.

Use the [optional automated-tuning extension](lesson-07-pytorch-automated-tuning.md) only after the student has completed and explained a manual tuning cycle.

### Optional Implementation Labs

- Hyperparameter Tuning: Learning Rate and Metrics — 60 min
- Schedulers in PyTorch — 60 min
- Hyperparameter Optimization with Optuna — 60 min
- Efficiency vs Performance Metrics — 60 min

Use at most one lab during a competition sprint unless extra curriculum time has been explicitly allocated.

---

## D. PyTorch Foundation Review Before Tuning

**Course:** Course 1 — PyTorch: Fundamentals  
**Coursera:** https://www.coursera.org/learn/pytorch-fundamentals  
**Section:** Module 2 — The PyTorch Workflow

| Video | Duration | Sprint use |
|---|---:|---|
| Loss | 5 min | confirms what training minimises |
| Optimizers and Gradients | 6 min | reviews parameter updates |
| Image Classification — Part 2: Training and Evaluating the Model | 4 min | reviews train/evaluate separation |

Assign these only when a student cannot explain the training loop before tuning.

## Tuning Order Used in This Repo

```text
Frozen metric and validation
→ selected baseline model
→ error analysis
→ manual parameter diagnosis
→ learning rate or basic capacity
→ regularisation
→ batch size and optimiser
→ scheduler
→ optional automated search
→ confirmation rerun
→ efficiency and submission risk
```

After tuning, return to the required sprint sequence:

```text
strong single models
→ model-diversity analysis
→ simple averaging or voting
→ OOF stacking only when justified
→ best-single-model versus ensemble decision
```

Do not use automated search to hide weak task recognition, data leakage, an invalid metric, a broken feature pipeline, or an unjustified model family.