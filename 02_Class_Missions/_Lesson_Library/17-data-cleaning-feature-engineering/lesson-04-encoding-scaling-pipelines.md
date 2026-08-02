# Lesson 04 — Encoding, Scaling, and Pipeline-Safe Preprocessing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect numeric and categorical columns. |
| 8–15 min | Talk Robin 1 | Explain which columns need encoding or scaling. |
| 15–22 min | Entry Check | Choose preprocessing for each column type. |
| 22–35 min | Core Pattern | Teacher models column type → transformer → pipeline → validation. |
| 35–53 min | Guided Practice | Complete supported preprocessing design. |
| 53–67 min | Independent Rebuild | Build a preprocessing plan for a new dataset. |
| 67–75 min | Talk Robin 2 + Evidence | Submit pipeline memo. |

## Core Pattern

```text
Column audit → numeric/categorical choice → encoder/scaler → pipeline boundary → validation check
```

## Evidence

Submit column plan, pipeline sketch, and one explanation of why preprocessing must be inside the validation workflow.
