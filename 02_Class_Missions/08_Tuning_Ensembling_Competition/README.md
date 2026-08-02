# 08 — Tuning, Ensembling, and Competition

**Scheduled sessions:** 72–75

## Fixed Order

```text
diagnose a limitation
→ tune a selected model
→ compare stable single models
→ ensemble only complementary valid models
→ run the full task from a fresh environment
```

## Sequence

1. **Diagnosis-first tuning** — default reference, controlled manual experiments, justified search space, Grid/Random Search, learning-rate and regularisation decisions.
2. **Model ensembling** — voting, probability averaging, weighted averaging, bagging, boosting, and out-of-fold stacking.
3. **Full competition simulation** — task reading, EDA, validation, feature pipeline, baseline ladder, error analysis, tuning, optional fusion, submission, and runtime checks.
4. **Postmortem and readiness conference** — decisions, failure modes, evidence, reliability, and the next highest-value action.

## Lesson Library Modules

`24-round-2-project-training`, `25-past-paper-reproduction`, `26-mock-contests`, and the full eight-lesson `28-competition-sprint-task-data-tuning` bank.

## Rules

- Never tune on the test set or public leaderboard.
- Automated tuning is optional and follows a justified manual cycle.
- Stacking uses out-of-fold base predictions.
- An ensemble must beat the best single model by more than validation noise.
- Complexity stops when expected gain is smaller than reproducibility or submission risk.
