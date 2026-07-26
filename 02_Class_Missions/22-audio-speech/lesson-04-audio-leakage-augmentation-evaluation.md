# Lesson 04 — Audio Dataset Leakage, Augmentation, and Evaluation

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect audio metadata and speaker/source groups. |
| 8–15 min | Talk Robin 1 | Discuss source leakage and augmentation risks. |
| 15–22 min | Entry Check | Mark safe and unsafe splits. |
| 22–35 min | Core Pattern | Teacher models source-aware split → augmentation → evaluation. |
| 35–53 min | Guided Practice | Complete supported split/evaluation plan. |
| 53–67 min | Independent Rebuild | Design leakage-safe audio validation. |
| 67–75 min | Talk Robin 2 + Evidence | Submit validation plan. |

## Core Pattern

```text
Audio source metadata → group-aware split → augmentation policy → classifier → metric + leakage check
```

## Evidence

Submit leakage warning, augmentation decision, and evaluation design.
