# Lesson 04 — ColumnTransformer, Pipeline, and Leakage-Safe Preprocessing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect a mixed-column dataset. |
| 8–15 min | Talk Robin 1 | Explain which columns need which transformer. |
| 15–22 min | Entry Check | Choose preprocessing for numeric and categorical columns. |
| 22–35 min | Core Pattern | Teacher models ColumnTransformer inside Pipeline. |
| 35–53 min | Guided Practice | Complete supported pipeline design. |
| 53–67 min | Independent Rebuild | Rebuild pipeline plan for a new dataset. |
| 67–75 min | Talk Robin 2 + Evidence | Submit pipeline and leakage note. |

## Core Pattern

```text
Column audit → transformer groups → ColumnTransformer → Pipeline → fit on train only → validate
```

## Evidence

Submit column mapping, pipeline sketch/code, and one leakage-safe explanation.
