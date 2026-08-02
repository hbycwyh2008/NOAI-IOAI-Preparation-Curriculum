# Session 72 — Systematic EDA, Data Quality, and Distribution Shift

**Duration:** 75 minutes  
**Prerequisite:** Session 17 basic missing-value and split-safe cleaning practice

## Required Mastery

Students must be able to:

1. separate exploratory questions from preprocessing actions;
2. audit schema, target quality, duplicates, missingness, outliers, groups, and time;
3. distinguish missing completely at random, conditionally missing, and potentially informative missingness at an intuitive level;
4. compare training and validation distributions without using validation labels to design target-derived features;
5. identify target leakage, group leakage, temporal leakage, duplicate leakage, and preprocessing leakage;
6. decide whether a random, grouped, stratified, or time-aware split is defensible;
7. document a data-quality risk without silently “fixing” it;
8. connect an EDA finding to a controlled modelling decision.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Classify eight observations as schema, quality, shift, leakage, or modelling evidence. |
| 8–15 | **Talk Robin 1** | Explain why the same cleaning rule can be valid before deployment but invalid when fitted on all labelled rows. |
| 15–22 | **Entry Check** | Select the correct split strategy for random, grouped, and temporal tasks. |
| 22–35 | **Core Pattern** | Build a question-driven audit before choosing transformations. |
| 35–53 | **Guided Practice** | Audit a dataset containing repeated entities, time drift, missingness, and a suspicious feature. |
| 53–67 | **Independent Rebuild** | Produce a complete EDA and data-risk plan for a new task. |
| 67–75 | **Talk Robin 2 + Evidence** | Defend the highest-risk finding and the next controlled experiment. |

## Core Pattern

```text
task and unit of prediction
→ schema and target audit
→ split boundary
→ train/validation distribution comparison
→ leakage and quality risks
→ train-fitted transformations
→ baseline evidence
→ controlled next step
```

## Guided Practice Questions

- What is one row, and can the same entity appear in more than one split?
- Is time part of the prediction setting?
- Which columns could only exist after the target event?
- Are missing values associated with source, group, time, or target prevalence?
- Do rare categories or outliers represent errors, valid extremes, or a different population?
- Which observations justify a transformation, and which require more evidence?

## Independent Rebuild

Submit a one-page audit containing:

- unit of prediction and target definition;
- proposed split and justification;
- schema and data-quality table;
- at least two distribution comparisons;
- leakage risk register;
- train-only preprocessing plan;
- one baseline and one controlled next experiment;
- one limitation that EDA cannot resolve.

## Evidence

The evidence package is the audit page, two labelled plots or tables, a leakage-risk register, and a short defence of the split strategy.

## Gate

The student does not pass by listing cleaning operations. The student must show that the split, audit, preprocessing, and modelling decisions form one leakage-safe protocol.
