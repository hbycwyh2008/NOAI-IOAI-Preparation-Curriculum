# Lesson 05 — Transfer Learning and Fine-Tuning under Time Limits

**Duration:** 70 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Compare training from scratch with fine-tuning. |
| 8–15 min | Talk Robin 1 | Discuss why fine-tuning helps under limited data/time. |
| 15–22 min | Entry Check | Identify frozen layers, classifier head, and learning rate. |
| 22–35 min | Core Pattern | Teacher explains pretrained model → replace head → train/fine-tune → validate. |
| 35–53 min | Guided Practice | Choose a fine-tuning strategy for three scenarios. |
| 53–67 min | Independent Rebuild | Write a fine-tuning plan for a new task. |
| 67–70 min | Talk Robin 2 + Evidence | Submit plan and rationale. |

## Core Pattern

```text
Pretrained features → Task-specific head → Frozen/unfrozen layers → Training budget → Validation evidence
```

## Required Evidence

1. Fine-tuning strategy table.
2. One model-capacity/time-budget decision.
3. One transfer-learning plan.
