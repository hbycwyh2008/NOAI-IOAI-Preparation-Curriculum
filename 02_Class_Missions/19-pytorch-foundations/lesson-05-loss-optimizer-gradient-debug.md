# Lesson 05 — Loss Functions, Optimizer Step, and Gradient-Debug Checklist

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect a minimal PyTorch training step. |
| 8–15 min | Talk Robin 1 | Discuss where loss, backward, and optimizer step occur. |
| 15–22 min | Entry Check | Order `zero_grad`, `loss.backward`, and `optimizer.step`. |
| 22–35 min | Core Pattern | Teacher models forward → loss → backward → update → verify. |
| 35–53 min | Guided Practice | Complete supported gradient-debug checklist. |
| 53–67 min | Independent Rebuild | Rebuild a training step without copying. |
| 67–75 min | Talk Robin 2 + Evidence | Submit trace and debug note. |

## Core Pattern

```text
Batch → forward → loss → zero_grad → backward → optimizer.step → metric/check
```

## Evidence

Submit ordered training-step trace, gradient-debug checklist, and rebuilt training step.
