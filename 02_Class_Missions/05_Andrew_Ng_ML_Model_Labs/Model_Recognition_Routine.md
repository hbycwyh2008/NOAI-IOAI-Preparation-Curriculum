# Model Recognition Routine

Use this routine in every model lesson and in the daily mixed-drill system at `04_Assessment/Model_Recognition_Drills/`.

## Reasoning Order

Do not name a model first. Answer in this order:

1. What is one row, sample, sequence, image, clip, user, query, state, or episode?
2. What is the input X?
3. What is the target y, if one exists?
4. Are labels available during training, and at what granularity?
5. What must the system output: number, class, probability, multiple tags, mask, ranking, embedding, sequence, generated object, action, or policy?
6. What task family follows from labels and output: regression, classification, multilabel classification, segmentation, ranking/retrieval, clustering, dimensionality reduction, anomaly detection, recommendation, reinforcement learning, generation, or another explicitly defined task?
7. What is the simplest valid baseline?
8. Which metric reflects the real error cost and output structure?
9. Which validation split matches deployment: random, stratified, grouped, time-based, source-based, or another justified design?
10. Which two model families are reasonable candidates?
11. What assumption, leakage path, distribution shift, resource limit, or failure mode could invalidate each candidate?
12. How will the required output or submission be validated?

## Required Answer Format

```text
one row/sample:
X/features:
y/target:
labels available during training:
required output:
task family:
simplest valid baseline:
primary metric:
why the metric matches error cost:
validation split/design:
candidate model family 1:
candidate model family 2:
leakage or shift risk:
likely limitation/failure mode:
submission/output checks:
```

## Daily Practice

- Complete one public scenario per study day for 15 minutes.
- Record confidence before feedback and the reasoning error after feedback.
- Do not use a public answer key; detailed solutions and calibration examples remain private.
- After mastery, complete two mixed maintenance drills per week.

## Mastery Standard

Mastery requires:

- at least 90% task-family accuracy for five consecutive daily sets;
- valid baseline and metric choices for at least 90% of scenarios;
- no repeated confusion between features, labels, output, task, metric, and model;
- one realistic validation/leakage/shift risk identified;
- a final fresh secured mixed set that was not published in the practice bank.

Do not select a model from keywords alone. Decide from sample structure, label availability, required output, deployment conditions, validation design, and error cost.
