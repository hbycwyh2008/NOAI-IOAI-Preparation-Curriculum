# Lesson 02 — Baseline, Metric, and Model-Family Selection

**Duration:** 75 minutes

## Learning Target

Students can choose the simplest valid baseline, justify the evaluation metric, and reject unnecessarily complex model families.

## Required Video Resource

**Course 2 — Advanced Learning Algorithms**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/advanced-learning-algorithms  
Week 3 — Advice for Applying Machine Learning:

- Establishing a Baseline Level of Performance — 9 min
- Evaluating a Model — 10 min
- Error Metrics for Skewed Datasets — 12 min when the task is imbalanced

## 1. Skill Warm-Up — 0–8 min

Watch the assigned baseline video and write:

```text
What is the baseline?
Why is it valid?
What result would count as meaningful improvement?
```

## 2. Talk Robin 1 — 8–15 min

Compare two candidate baselines and discuss which one creates faster reliable evidence.

## 3. Entry Check — 15–22 min

For the assigned task, identify:

- official metric;
- a secondary diagnostic metric;
- naive baseline;
- simple model baseline;
- one model family that is currently unjustified.

## 4. Core Pattern — 22–35 min

```text
Metric → Split → Naive Baseline → Simple Model → Error Analysis → More Complex Model Only If Needed
```

Baseline ladder:

1. constant or majority prediction;
2. simple statistical or rule-based baseline;
3. simple linear/tree/classical model;
4. small neural-network baseline;
5. pretrained or multimodal model only after evidence supports it.

## 5. Guided Practice — 35–53 min

Complete the decision table:

| Candidate | Expected strength | Cost | Risk | Use now? Why? |
|---|---|---|---|---|
| Constant baseline |  |  |  |  |
| Linear/logistic model |  |  |  |  |
| Tree ensemble |  |  |  |  |
| Neural network |  |  |  |  |
| Pretrained model |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

Write a baseline memo:

```text
Official metric:
Validation design:
Naive baseline:
First trainable baseline:
Why it matches the task:
Expected runtime:
Failure condition:
Evidence required before increasing complexity:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Defend the baseline in 60 seconds. Submit the decision table and memo.

## Exit Standard

The baseline must run end to end, produce the correct submission shape, and create a trustworthy reference score before tuning begins.