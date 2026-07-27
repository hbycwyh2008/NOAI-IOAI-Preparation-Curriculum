# Lesson 06 — Deep-Learning Tuning: Learning Rate, Batch Size, Regularisation, and Optimiser

**Duration:** 75 minutes

## Learning Target

Students can tune a deep-learning baseline in a disciplined order and distinguish optimisation failure from overfitting, underfitting, and data-pipeline problems.

## Required Video Resource

**Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization**, part of the **Deep Learning Specialization**  
Coursera: https://www.coursera.org/learn/deep-neural-network

Required videos:

1. Basic Recipe for Machine Learning — 6 min
2. Adam Optimization Algorithm — 7 min
3. Learning Rate Decay — 7 min
4. Tuning Process — 7 min
5. Using an Appropriate Scale to Pick Hyperparameters — 9 min
6. Hyperparameters Tuning in Practice: Pandas vs. Caviar — 7 min

**Required video time:** 43 minutes.

See [Hyperparameter-Tuning Video Resource Map](Hyperparameter_Tuning_Video_Resource_Map.md).

## 1. Skill Warm-Up — 0–8 min

Watch the first assigned segment and classify one training curve as optimisation failure, underfitting, overfitting, or unstable validation.

## 2. Talk Robin 1 — 8–15 min

Discuss which hyperparameter has the highest expected value to tune first and which should remain fixed.

## 3. Entry Check — 15–22 min

Complete:

```text
Current learning rate:
Batch size:
Optimiser:
Weight decay or other regularisation:
Training-loss pattern:
Validation pattern:
Dominant failure mode:
First parameter to change:
```

## 4. Core Pattern — 22–35 min

```text
Verify Data and Metric
→ Stabilise the Training Loop
→ Tune Learning Rate
→ Check Capacity and Regularisation
→ Tune Batch Size and Optimiser
→ Add Scheduler
→ Recheck Error Categories and Runtime
```

Default sprint priority:

1. learning rate;
2. model capacity only when bias is evident;
3. weight decay/dropout only when variance is evident;
4. batch size based on stability, memory, and update frequency;
5. optimiser and scheduler;
6. augmentation or transfer-learning choices;
7. architecture search only when time and evidence justify it.

## 5. Guided Practice — 35–53 min

Design a five-run tuning ladder:

| Run | Changed variable | Value | Expected effect | Failure signal |
|---|---|---:|---|---|
| Baseline | none |  | reference |  |
| 1 | learning rate |  |  |  |
| 2 | learning rate |  |  |  |
| 3 | regularisation/capacity |  |  |  |
| 4 | batch size/optimiser |  |  |  |

## 6. Independent Rebuild — 53–67 min

Using a new training curve or mini-project, write:

```text
Diagnosis:
Highest-priority parameter:
Search scale: linear / logarithmic / categorical
Values tested:
Best validation evidence:
Runtime and memory effect:
Decision:
Next experiment:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit the tuning ladder and explain why the search order is safer than tuning all parameters simultaneously.

## Exit Standard

A student must be able to connect every parameter change to a visible training, validation, runtime, or memory hypothesis.