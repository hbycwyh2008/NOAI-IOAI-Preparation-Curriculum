# Session 68 — D2L Attention and Transformer Bridge

**Placement:** embedded inside Session 68; this packet does not add another scheduled session.  
**Role:** connect the hand calculation already required in Session 68 to Q/K/V tensor operations and a minimal PyTorch attention trace.

## Assigned D2L Sections

- [10.1 Attention Cues](https://zh.d2l.ai/chapter_attention-mechanisms/attention-cues.html)
- [10.3 Attention Scoring Functions](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html)
- [10.5 Multi-Head Attention](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html)
- [10.6 Self-Attention and Positional Encoding](https://zh.d2l.ai/chapter_attention-mechanisms/self-attention-and-positional-encoding.html)
- [10.7 Transformer](https://zh.d2l.ai/chapter_attention-mechanisms/transformer.html)

Use the PyTorch tab. A complete machine-translation Transformer implementation is not required.

## Required Mastery

Students must be able to:

1. identify queries, keys, values, scores, masks, normalised weights, and outputs;
2. calculate a small dot-product or scaled dot-product attention example;
3. record batch, head, sequence, and feature dimensions;
4. explain self-attention and multi-head attention without saying only that the model “focuses”;
5. explain why positional information is required;
6. distinguish padding masks from causal masks;
7. trace residual, normalisation, and feed-forward components at a high level;
8. identify quadratic sequence-length cost and task-specific reliability limits.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read D2L 10.1, 10.3, and 10.6; create a Q/K/V glossary. |
| Entry Check | Match Q, K, V, score, softmax, mask, and output to their roles and shapes. |
| Core Pattern | Calculate a tiny attention matrix and weighted output by hand. |
| Guided Practice | Reproduce the calculation with PyTorch tensor operations and verify each intermediate shape. |
| Independent Rebuild | Close D2L and implement a minimal single-head attention trace, including one mask. |

## Shape Ledger

Use explicit symbols before execution:

```text
Q: batch × heads × query_length × head_width
K: batch × heads × key_length × head_width
V: batch × heads × value_length × value_width
scores: batch × heads × query_length × key_length
weights: batch × heads × query_length × key_length
output: batch × heads × query_length × value_width
```

## Independent Task

1. calculate one attention example by hand;
2. reproduce it with PyTorch operations;
3. add either a padding mask or a causal mask and explain its effect;
4. show how multiple heads change the shape ledger;
5. identify where positional information enters;
6. trace one simplified Transformer block;
7. explain one computational limitation and one reliability limitation;
8. reject at least one incorrect interpretation of an attention weight.

## Required Evidence

- hand score, softmax, and weighted-sum calculation;
- complete Q/K/V and multi-head shape ledger;
- masked PyTorch trace;
- recurrence-versus-attention comparison;
- Transformer-block diagram;
- cost and reliability limitation note;
- one misconception and correction.

## Gate

The student passes only when the hand result and PyTorch result agree, every tensor dimension is explained, and the student avoids treating attention weights as automatic proof of human-like reasoning or faithful explanation.