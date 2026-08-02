# Lesson 04 — Text Preprocessing and Leakage-Safe Train/Test Split

**Duration:** 70 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect raw text examples and labels. |
| 8–15 min | Talk Robin 1 | Discuss what preprocessing may help or harm. |
| 15–22 min | Entry Check | Identify leakage risks in text data. |
| 22–35 min | Core Pattern | Teacher explains raw text → clean/tokenize → split → vectorize → validate. |
| 35–53 min | Guided Practice | Audit a text preprocessing workflow. |
| 53–67 min | Independent Rebuild | Write a leakage-safe text workflow for a new task. |
| 67–70 min | Talk Robin 2 + Evidence | Submit workflow and risk note. |

## Core Pattern

```text
Raw text → Cleaning decision → Split before fitting → Tokenization/vectorization → Evaluation
```

## Required Evidence

1. Preprocessing decision table.
2. Leakage-risk explanation.
3. One safe text workflow plan.
