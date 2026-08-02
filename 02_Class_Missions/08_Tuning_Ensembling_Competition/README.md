# 08 — Tuning, Ensembling, and Competition

**Scheduled sessions:** 75–78

## Start Here

[**Open the Phase 8 Session Launcher**](SESSION_LAUNCHER.md)

The launcher selects the four canonical sessions. Do not schedule the entire eight-lesson sprint bank unless it is explicitly used as an extension.

## Fixed Order

```text
diagnose a limitation
→ tune a selected model
→ compare stable single models
→ ensemble only complementary valid models
→ run from a fresh environment
→ validate the submission
→ write the postmortem
```

## Rules

- Never tune on the test set or public leaderboard.
- Automated tuning follows a justified manual cycle.
- Stacking uses out-of-fold base predictions.
- An ensemble must beat the best single model by more than validation noise.
- Complexity stops when expected gain is smaller than reproducibility or submission risk.

## Gate

Students complete a trustworthy end-to-end competition workflow and defend whether tuning or ensembling produced a real, reproducible improvement.