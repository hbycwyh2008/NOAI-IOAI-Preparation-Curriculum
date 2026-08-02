# Session 52 — Support Vector Machines: Margin, Scaling, and Model Behaviour

**Duration:** 75 minutes  
**Prerequisite:** Bohrium Session 29 margin intuition and Phase 5 mathematics bridge

## Required Mastery

Students must be able to:

1. identify a binary classification task appropriate for a linear support-vector baseline;
2. distinguish the decision boundary, margin, support vectors, and predicted class;
3. explain why only points near the boundary determine the maximum-margin solution;
4. describe the effect of the regularisation parameter `C` on margin violations and model flexibility;
5. explain why feature scaling changes distance and margin geometry;
6. distinguish a linear boundary from a kernel-induced nonlinear boundary;
7. compare SVM strengths and limitations with logistic regression, KNN, and trees;
8. train a leakage-safe scikit-learn pipeline and interpret validation evidence.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Mark boundary, margins, and support points on two diagrams. |
| 8–15 | **Talk Robin 1** | Explain how scaling one feature can rotate or distort the effective margin. |
| 15–22 | **Entry Check** | Predict the effect of increasing `C` in a noisy dataset. |
| 22–35 | **Core Pattern** | Connect signed boundary score, distance, margin, violations, and classification. |
| 35–53 | **Guided Practice** | Compare scaled linear SVM, logistic regression, and KNN under one split. |
| 53–67 | **Independent Rebuild** | Build and justify an SVM baseline for a new two-feature task. |
| 67–75 | **Talk Robin 2 + Evidence** | Defend model choice, `C`, scaling, metric, and one limitation. |

## Core Pattern

```text
scaled features
→ candidate separating boundary
→ margin and violations
→ support vectors
→ fitted decision function
→ threshold at zero
→ validation evidence
```

## Mathematics and Code Bridge

For a supplied linear score `f(x) = w · x + b`, students:

- calculate scores for small examples;
- identify the predicted class from the sign;
- compare which examples lie closest to the boundary;
- explain why rescaling a feature changes `w · x` and the geometry;
- locate `StandardScaler`, `SVC` or `LinearSVC`, and the metric in a scikit-learn pipeline.

## Independent Rebuild

The submission must include:

- task formalisation (`X`, `y`, metric, split);
- a scaled linear SVM baseline;
- a controlled comparison with one alternative model;
- a small `C` comparison table;
- support-vector or boundary interpretation where available;
- runtime and scaling notes;
- a model card naming failure modes and when not to use an SVM.

## Evidence

Submit the hand score/margin calculation, pipeline code, comparison table, boundary or support-point explanation, and model card.

## Gate

The student must explain model behaviour rather than report a score. A valid answer connects scaling, margin, `C`, support points, validation, and limitations.
