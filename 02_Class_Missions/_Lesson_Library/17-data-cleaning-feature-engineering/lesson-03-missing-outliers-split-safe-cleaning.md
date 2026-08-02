# Lesson 03 — Missing Values, Outliers, and Split-Safe Cleaning

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect missing values and outliers in a table. |
| 8–15 min | Talk Robin 1 | Discuss why cleaning before splitting can leak information. |
| 15–22 min | Entry Check | Mark safe and unsafe cleaning actions. |
| 22–35 min | Core Pattern | Teacher models split → fit cleaning rule on train → apply to validation/test. |
| 35–53 min | Guided Practice | Complete supported split-safe cleaning decisions. |
| 53–67 min | Independent Rebuild | Design a cleaning plan for a new task. |
| 67–75 min | Talk Robin 2 + Evidence | Submit cleaning memo. |

## Core Pattern

```text
Raw data → split boundary → train-only cleaning rule → apply consistently → verify no leakage
```

## Evidence

Submit missing/outlier audit, split-safe cleaning plan, and leakage warning.
