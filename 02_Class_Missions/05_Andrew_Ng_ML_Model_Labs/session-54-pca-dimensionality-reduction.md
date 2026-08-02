# Session 54 — PCA and Dimensionality Reduction

**Class duration:** 75 minutes  
**Task family:** unsupervised representation and dimensionality reduction

## Required Mastery

Students must be able to:

1. explain why PCA normally uses `X` without a target `y`;
2. centre features before projection;
3. explain variance as spread and a principal component as a direction of large variation;
4. interpret projection onto a direction;
5. distinguish principal components from original features;
6. explain explained-variance ratio at an intuitive level;
7. identify uses such as visualisation, compression, denoising, and preprocessing;
8. explain why PCA does not automatically improve a predictive model;
9. fit PCA only on training data inside a leakage-safe pipeline;
10. identify limitations involving scaling, interpretability, nonlinear structure, and low-variance predictive signals.

## Core Pattern

```text
centre and usually scale X
→ find directions of large variance
→ project examples onto selected directions
→ inspect retained variance and information loss
→ evaluate the downstream purpose
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | identify high-dimensional tasks and possible reasons to reduce dimensions |
| 8–15 | Talk Robin 1 | distinguish original features from component coordinates |
| 15–22 | Entry Check | interpret one 2D projection diagram |
| 22–35 | Core Pattern | centre → direction → projection → retained variation |
| 35–53 | Guided Practice | project a small set of centred points onto a supplied direction |
| 53–67 | Independent Rebuild | compare a baseline pipeline with and without PCA under one validation protocol |
| 67–75 | Talk Robin 2 + Evidence | explain retained variance, score change, and information loss |

## Required Evidence

- task and shape record;
- projection sketch or small calculation;
- explained-variance table;
- leakage-safe pipeline;
- baseline versus PCA comparison;
- interpretation and limitation note.

## Gate

The student can explain PCA as projection onto variance directions, distinguish it from feature selection and classification, and justify whether it helps the specific task.