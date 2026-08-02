# Canonical Phase 8 — Tuning, Ensembling, and Competition

**Sessions:** 75–78  
**Canonical entry:** [Phase 8 Session Launcher](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md)

This phase begins only after students can defend data quality, validation, model selection, and error analysis.

## Four-Session Sequence

| Session | Focus | Required outcome |
|---:|---|---|
| 75 | diagnosis-first tuning | baseline, diagnosed limitation, controlled experiments, justified parameter decision |
| 76 | model ensembling | aligned held-out or OOF predictions, diversity evidence, best-single comparison, leakage check |
| 77 | full competition simulation | complete workflow, valid artifact, fresh-environment execution, recovery plan |
| 78 | postmortem and readiness conference | evidence-based readiness decision, failure taxonomy, dated next actions |

## Canonical Workflow

```text
task definition
→ data quality and validation
→ reproducible feature pipeline
→ stable baseline and model comparison
→ error diagnosis
→ controlled tuning
→ valid ensembling
→ fresh-runtime submission validation
→ postmortem
```

## Session 75 Rules

- preserve default parameters as the reference;
- state the diagnosed problem before changing a parameter;
- run one controlled manual change at a time;
- record runtime, spread, and keep/reject decision;
- use automated search only after the manual cycle;
- use the [Hyperparameter-Tuning Resource Map](../05_Resources/Hyperparameter_Tuning_Resource_Map.md).

## Session 76 Rules

An ensemble counts only when base models are individually valid, predictions align to identical held-out rows or valid OOF generation, diversity is measured, and the ensemble is compared with the best single model beyond expected validation noise.

## Session 77 Rules

Use the target competition duration. The simulation must include task and schema reading, data/leakage audit, frozen validation, baseline, reproducible pipeline, controlled improvement, error analysis, fresh execution, submission validation, and backup/recovery procedure.

## Session 78 Rules

The student explains what worked, what failed, which evidence is trustworthy, which risk remains highest, and the next three dated actions.

## Non-Negotiable Boundaries

1. Never tune on the hidden test or repeatedly reused final holdout.
2. Tuning follows diagnosis and a stable baseline.
3. Stacking uses out-of-fold predictions.
4. Rejected experiments remain in the record.
5. Complexity stops early enough for fresh-runtime and submission validation.
6. Current official competition rules override repository suggestions.

## Phase Gate

The student independently completes the workflow, produces a valid and reproducible submission, explains major decisions, demonstrates no critical leakage or split failure, and identifies the next improvement without hidden-test feedback.
