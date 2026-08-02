# Lesson 01 — Task Recognition and Task Formalisation

**Duration:** 75 minutes

## Learning Target

By the end of this lesson, students can convert an unfamiliar task statement into a precise modelling and evaluation specification before inspecting models or writing training code.

## Required Resource

One official NOAI or IOAI task statement selected by the teacher. Do not use a solved version.

## 1. Skill Warm-Up — 0–8 min

Read only the task statement, data description, metric, constraints, and submission format.

Mark:

- input unit;
- required output;
- whether labels exist;
- task type;
- evaluation metric and direction;
- prediction-time boundary;
- runtime and package constraints;
- submission-file requirements.

## 2. Talk Robin 1 — 8–15 min

Partners compare answers to:

1. What exactly is one sample?
2. What must the system produce for one sample?
3. Which sentence reveals the task type?
4. What information genuinely exists at prediction time?
5. Which sentence creates the greatest competition risk?

## 3. Entry Check — 15–22 min

Complete without coding:

```text
Task type:
Input X:
Output/target y:
Target or hidden structure:
Training signal:
Official metric and direction:
Submission unit and schema:
Prediction-time boundary:
Possible independent/group unit:
Main constraint:
```

## 4. Core Pattern — 22–35 min

Use this task-formalisation pattern:

```text
Input X
→ Output/Target y
→ Training Signal
→ Task Type
→ Metric and Direction
→ Prediction-Time Boundary
→ Independent Unit
→ Constraints
→ Submission Schema
→ Data Questions to Audit Next
```

Recognition rules:

- continuous numeric output → regression;
- discrete label output → classification;
- no labels, group assignment → clustering;
- sequence output → sequence modelling;
- image mask or bounding boxes → segmentation or detection;
- action and reward loop → reinforcement learning;
- text/image/audio combination → multimodal task.

Do **not** select the final model family in this lesson. Model selection occurs only after data quality, validation, and feature representation are understood.

## 5. Guided Practice — 35–53 min

Classify four short competition scenarios and justify each using evidence from the wording.

| Scenario | Task type | Input/output evidence | Metric | Prediction-time boundary | First data-quality question |
|---|---|---|---|---|---|
| A |  |  |  |  |  |
| B |  |  |  |  |  |
| C |  |  |  |  |  |
| D |  |  |  |  |  |

## 6. Independent Rebuild — 53–67 min

For a new task statement, produce a one-page task card:

```text
Problem in one sentence:
One sample is:
Input X is:
The required output/target y is:
The learning paradigm is:
The task type is:
The metric rewards:
The metric punishes:
Prediction-time information is limited to:
The independent or grouping unit may be:
The submission must contain:
The largest data/validation risk is:
The first three data questions to investigate are:
```

## 7. Talk Robin 2 + Evidence — 67–75 min

Submit the task card and explain one model-selection decision that must wait until after the data and feature stages.

## Exit Standard

A student is ready for the data-quality lesson only when the input, output, task type, metric, prediction-time boundary, independent-unit hypothesis, constraints, and submission schema are unambiguous.

The student is **not** yet expected to choose the final baseline model.