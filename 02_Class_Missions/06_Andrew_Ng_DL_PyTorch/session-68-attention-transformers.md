# Session 68 — Attention and Transformer Intuition

**Class duration:** 75 minutes

## Required Mastery

Students must be able to:

1. explain why fixed-length sequence summaries can lose relevant information;
2. identify query, key, value, attention score, normalised weight, and weighted output;
3. state the shapes of a small attention example;
4. calculate a simple dot-product attention score and weighted combination;
5. explain self-attention as tokens attending to other tokens in the same sequence;
6. distinguish attention from recurrence;
7. explain positional information and why token order must be represented;
8. describe the high-level Transformer block: attention, residual connection, normalisation, feed-forward network;
9. identify quadratic sequence-length cost, context limits, data demand, and hallucination as limitations;
10. connect the concept to PyTorch tensor operations without treating a library call as understanding.

## Core Pattern

```text
represent tokens
→ compute query/key compatibility
→ normalise scores into weights
→ combine values
→ apply residual/feed-forward transformations
→ repeat across layers
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | compare recurrent and attention-based sequence handling |
| 8–15 | Talk Robin 1 | explain which earlier token matters for a short ambiguous sentence |
| 15–22 | Entry Check | identify query, key, value, and output shapes |
| 22–35 | Core Pattern | score → weights → weighted sum |
| 35–53 | Guided Practice | calculate a tiny attention example by hand |
| 53–67 | Independent Rebuild | implement or trace a small self-attention operation in PyTorch |
| 67–75 | Talk Robin 2 + Evidence | explain attention behaviour and one limitation |

## Required Evidence

- shape ledger;
- hand attention calculation;
- attention-weight interpretation;
- PyTorch trace or small implementation;
- recurrence-versus-attention comparison;
- cost and reliability limitation note.

## Gate

The student can calculate and explain a small attention operation, identify tensor shapes, and distinguish the mechanism from claims that the model necessarily understands or reasons like a person.