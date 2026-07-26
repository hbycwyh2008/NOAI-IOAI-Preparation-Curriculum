# Lesson 06 — Dataset/DataLoader Rebuild and Device-Safe Training Loop

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect a Dataset/DataLoader example. |
| 8–15 min | Talk Robin 1 | Explain what the Dataset returns and what the DataLoader batches. |
| 15–22 min | Entry Check | Identify device movement points. |
| 22–35 min | Core Pattern | Teacher models Dataset → DataLoader → batch → device → model. |
| 35–53 min | Guided Practice | Complete supported device-safe loop. |
| 53–67 min | Independent Rebuild | Rebuild a minimal custom Dataset/DataLoader. |
| 67–75 min | Talk Robin 2 + Evidence | Submit code and shape/device ledger. |

## Core Pattern

```text
Dataset item → DataLoader batch → move tensors to device → forward/loss/update → validation check
```

## Evidence

Submit Dataset sketch/code, batch-shape ledger, device-safe loop, and one debugging note.
