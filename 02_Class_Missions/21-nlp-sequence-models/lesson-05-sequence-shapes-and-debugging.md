# Lesson 05 — Sequence Length, Padding, Batching, and Shape Debugging

**Duration:** 70 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect tokenized sequences of different lengths. |
| 8–15 min | Talk Robin 1 | Discuss why padding and batching are needed. |
| 15–22 min | Entry Check | Predict tensor shapes after padding. |
| 22–35 min | Core Pattern | Teacher explains sequence length → padding → batch tensor → model input shape. |
| 35–53 min | Guided Practice | Complete a shape ledger for NLP batches. |
| 53–67 min | Independent Rebuild | Debug a new sequence-shape problem. |
| 67–70 min | Talk Robin 2 + Evidence | Submit shape ledger and fix. |

## Core Pattern

```text
Tokens → Sequence length → Padding/truncation → Batch tensor → Model shape requirement
```

## Required Evidence

1. Sequence-shape ledger.
2. One padding/truncation decision.
3. One corrected shape bug.
