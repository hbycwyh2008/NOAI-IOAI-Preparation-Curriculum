# Lesson 04 — Image Datasets, Transforms, and Train/Validation Leakage

**Duration:** 70 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect an image dataset split and transform list. |
| 8–15 min | Talk Robin 1 | Discuss possible leakage or transform mistakes. |
| 15–22 min | Entry Check | Identify safe and unsafe transforms. |
| 22–35 min | Core Pattern | Teacher explains dataset → split → transform → loader → validation. |
| 35–53 min | Guided Practice | Audit an image workflow for leakage. |
| 53–67 min | Independent Rebuild | Write a safe image data plan for a new task. |
| 67–70 min | Talk Robin 2 + Evidence | Submit audit and data plan. |

## Core Pattern

```text
Images → Labels → Split → Transform policy → DataLoader → Validation check
```

## Required Evidence

1. Leakage audit.
2. Safe transform policy.
3. One image data workflow plan.
