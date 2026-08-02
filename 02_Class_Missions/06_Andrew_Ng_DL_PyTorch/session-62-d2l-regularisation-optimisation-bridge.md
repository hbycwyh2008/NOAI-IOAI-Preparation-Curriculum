# Session 62 — D2L Regularisation, Initialisation, and Optimisation Bridge

**Placement:** embedded inside Session 62; this packet does not add another scheduled session.  
**Role:** turn named techniques into diagnosis-first experimental decisions.

## Assigned D2L Sections

### Required

- [4.5 Weight Decay](https://zh.d2l.ai/chapter_multilayer-perceptrons/weight-decay.html)
- [4.6 Dropout](https://zh.d2l.ai/chapter_multilayer-perceptrons/dropout.html)
- [4.8 Numerical Stability and Initialisation](https://zh.d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html)
- [7.5 Batch Normalisation](https://zh.d2l.ai/chapter_convolutional-modern/batch-norm.html)

### Optional extension

- [11.1 Optimisation and Deep Learning](https://zh.d2l.ai/chapter_optimization/optimization-intro.html)
- [11.6 Momentum](https://zh.d2l.ai/chapter_optimization/momentum.html)
- [11.10 Adam](https://zh.d2l.ai/chapter_optimization/adam.html)
- [11.11 Learning-Rate Scheduling](https://zh.d2l.ai/chapter_optimization/lr-scheduler.html)

Use the PyTorch tab and only the teacher-assigned cells.

## Required Mastery

Students must be able to:

1. distinguish optimisation failure from generalisation failure;
2. explain weight decay as a parameter penalty and Dropout as training-time stochastic regularisation;
3. explain why Dropout and BatchNorm behave differently during training and evaluation;
4. recognise exploding, vanishing, dead, or unstable activations from evidence;
5. justify an initialisation, optimiser, and learning-rate choice for a baseline;
6. change one controlled factor at a time;
7. reject a higher validation score when the comparison protocol is invalid.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read the required sections and complete a technique → mechanism → expected symptom table. |
| Entry Check | Classify six curves or logs as likely underfitting, overfitting, unstable optimisation, or insufficient evidence. |
| Guided Experiment | Train the same small network under a controlled pair of settings, such as no regularisation versus weight decay or no Dropout versus Dropout. |
| Behaviour Check | Compare outputs in `model.train()` and `model.eval()` for a model containing Dropout or BatchNorm. |
| Independent Decision | Write a diagnosis and next experiment for an unseen training/validation curve. |

## Controlled Comparison Rule

```text
same data split
+ same metric
+ same epoch or compute budget
+ same random-seed policy
+ one intended change
→ defensible comparison
```

## Independent Task

Complete one controlled experiment and one diagnosis task:

1. select one intervention: initialisation, weight decay, Dropout, BatchNorm, optimiser, or learning rate;
2. state the failure hypothesis before running;
3. preserve all non-target conditions;
4. record training and validation curves;
5. report whether the evidence supports the hypothesis;
6. identify one confound or limitation;
7. propose the next smallest informative experiment.

## Required Evidence

- mechanism table for weight decay, Dropout, BatchNorm, and initialisation;
- train/eval behaviour check;
- controlled experiment log;
- curve diagnosis;
- rejected invalid comparison;
- independent recommendation with an explicit uncertainty statement.

## Gate

The student passes only when the recommendation follows from controlled evidence. Naming Adam, Dropout, BatchNorm, or a scheduler without a diagnosed problem does not satisfy the gate.