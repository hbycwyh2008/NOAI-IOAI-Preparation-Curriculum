# Lesson 01 — Task Recognition from Unfamiliar Competition Statements

**Duration:** 75 minutes

## Learning Target

By the end of this lesson, students can convert an unfamiliar task statement into a precise modelling specification before writing code.

## Required Resource

One official NOAI or IOAI task statement selected by the teacher. Do not use a solved version.

## 1. Skill Warm-Up — 0–8 min

Read only the task statement, data description, metric, constraints, and submission format.

Mark:

- input unit;
- required output;
- whether labels exist;
- task type;
- evaluation metric;
- runtime and package constraints;
- submission-file requirements.

## 2. Talk Robin 1 — 8–15 min

Partners compare answers to:

1. What exactly is one sample?
2. What must the model produce for one sample?
3. Which sentence reveals the task type?
4. Which sentence creates the greatest competition risk?

## 3. Entry Check — 15–22 min

Complete without coding:

```text
Task type:
Input:
Output:
Target or hidden structure:
Training signal:
Metric:
Submission unit:
Main constraint:
```

## 4. Core Pattern — 22–35 min

Use this task-recognition pattern:

```text
Input → Output → Training Signal → Metric → Constraints → Candidate Model Families
```

Recognition rules:

- continuous numeric output → regression;
- discrete label output → classification;
- no labels, group assignment → clustering;
- sequence output → sequence modelling;
- image mask or bounding boxes → segmentation or detection;
- action and reward loop → reinforcement learning;
- text/image/audio combination → multimodal task.

## 5. Guided Practice — 35–53 min

Classify four short competition scenarios and justify each using evidence from the wording.

| Scenario | Task type | Recognition signal | Metric | Candidate baseline |
|---|---|---|---|---|
| A |  |  |  |  |
| B |  |  |  |  |
| C |  |  |  |  |
| D |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

For a new task statement, produce a one-page task card:

```text
Problem in one sentence:
One sample is:
The required prediction is:
The learning paradigm is:
The task type is:
The metric rewards:
The metric punishes:
The simplest valid baseline is:
The largest implementation risk is:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit the task card and explain one rejected model family.

## Exit Standard

A student is not ready to code until the input, output, metric, split unit, and baseline are unambiguous.