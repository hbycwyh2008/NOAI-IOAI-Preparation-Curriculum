# Canonical Phase 8 — Tuning, Ensembling, and Competition

**Sessions:** 75–78  
**Canonical folder:** `02_Class_Missions/08_Tuning_Ensembling_Competition/`

## Purpose

Integrate diagnosis-first tuning, controlled experimentation, valid ensembling, fresh-environment execution, submission validation, and postmortem practice.

## Entry Conditions

Students can defend a validation design, identify leakage, compare model families, and produce stable single-model baselines.

## Delivery Priorities

```text
diagnose the limitation
→ state a hypothesis
→ change one controlled factor
→ compare against the baseline
→ keep stable complementary models
→ ensemble only with valid held-out or out-of-fold predictions
→ execute from a fresh environment
→ validate the submission
→ write the postmortem
```

- tune only after identifying underfitting, overfitting, optimisation, data, or feature limitations;
- use manual controlled experiments before broad automated search;
- preserve validation independence and never tune on the test set or public leaderboard;
- require ensemble diversity and improvement beyond validation noise;
- stop adding complexity when expected gain is smaller than runtime or reproducibility risk.

## Required Evidence

- experiment log with hypothesis and single change;
- baseline and tuned-model comparison;
- optional search-space justification;
- ensemble record with held-out or out-of-fold predictions;
- fresh-runtime execution record;
- valid submission artifact;
- postmortem identifying decisions, failures, and next actions.

## Exit Gate

The student completes a full competition workflow within the target duration, produces a valid and reproducible submission, explains every major decision, and identifies the highest-value improvement without relying on hidden test feedback.
