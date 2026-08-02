# Session 56 — Recommender Systems

**Class duration:** 75 minutes  
**Task family:** ranking or preference prediction

## Required Mastery

Students must be able to:

1. identify users, items, interactions, available features, and the required output;
2. distinguish rating prediction, top-k ranking, and retrieval;
3. explain a user–item interaction matrix and missing entries;
4. calculate and interpret a dot product as compatibility between latent vectors;
5. distinguish popularity, content-based, and collaborative-filtering baselines;
6. explain embeddings or latent factors without claiming that every dimension has a simple human meaning;
7. identify cold-start, popularity bias, feedback loops, sparse data, and temporal shift;
8. design a split that respects time or user/item boundaries when required;
9. choose evaluation evidence appropriate to ranking or prediction;
10. compare recommendation quality with diversity, novelty, fairness, and operational constraints.

## Core Pattern

```text
user/item/interactions
→ baseline
→ representation or similarity
→ score candidate items
→ rank or predict
→ evaluate under realistic boundaries
→ inspect bias and feedback effects
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | distinguish ranking, classification, regression, and retrieval outputs |
| 8–15 | Talk Robin 1 | explain why a popular-item baseline is necessary |
| 15–22 | Entry Check | calculate one small dot-product score |
| 22–35 | Core Pattern | matrix → latent vectors → score → ranking |
| 35–53 | Guided Practice | compare popularity, content similarity, and collaborative recommendations |
| 53–67 | Independent Rebuild | build or simulate a small recommender baseline with a defensible split |
| 67–75 | Talk Robin 2 + Evidence | defend evaluation and identify one feedback-loop risk |

## Required Evidence

- task/output definition;
- user–item matrix or interaction table;
- dot-product or similarity calculation;
- popularity baseline;
- split/evaluation memo;
- cold-start and bias analysis;
- model card with limitations.

## Gate

The student can distinguish recommendation outputs, explain a baseline and vector score, design a defensible evaluation boundary, and identify cold-start and feedback-loop risks.