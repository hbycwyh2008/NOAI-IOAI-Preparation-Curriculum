# Lesson 05 — Time/Window Features, Moments, and Leakage Traps

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect examples of lag, rolling mean, and moment features. |
| 8–15 min | Talk Robin 1 | Discuss when a feature accidentally uses the future. |
| 15–22 min | Entry Check | Mark safe and leaking window features. |
| 22–35 min | Core Pattern | Teacher models event time → allowed history → window statistic → leakage check. |
| 35–53 min | Guided Practice | Complete supported feature-design table. |
| 53–67 min | Independent Rebuild | Design safe features for a new task. |
| 67–75 min | Talk Robin 2 + Evidence | Submit feature plan and leakage warning. |

## Core Pattern

```text
Prediction time → available history → window definition → statistic/moment → leakage test
```

## Evidence

Submit feature table, safe/unsafe labels, and one leakage explanation.
