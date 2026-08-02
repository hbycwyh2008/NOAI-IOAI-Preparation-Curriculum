# Canonical Phase 8 — Tuning, Ensembling, and Competition

**Sessions:** 75–78  
**Canonical folder:** `02_Class_Missions/08_Tuning_Ensembling_Competition/`

This phase converts the curriculum into a repeatable late-stage competition workflow. It begins only after students can defend data quality, validation, model selection, and error analysis.

## Phase Outcome

By the end of Phase 8, students can:

1. diagnose the dominant limitation before tuning;
2. run controlled manual experiments with a stable baseline;
3. justify any automated search space;
4. ensemble only individually valid and complementary models;
5. use identical held-out rows or valid out-of-fold predictions;
6. complete a full competition workflow from a fresh environment;
7. produce and validate the submission artifact;
8. write a postmortem that identifies decisions, failures, and the next highest-value action.

## Canonical Four-Session Sequence

| Session | Focus | Required outcome |
|---:|---|---|
| 75 | Diagnosis-first tuning and controlled search | baseline reference, diagnosed limitation, hypothesis, one-variable experiments, justified keep/reject decisions |
| 76 | Model ensembling | diversity analysis, held-out or OOF prediction record, best-single-versus-ensemble comparison, leakage checks |
| 77 | Full competition simulation | task formalisation, data audit, validation, features, baseline ladder, controlled improvement, optional ensemble, fresh-runtime submission |
| 78 | Postmortem and readiness conference | evidence-based readiness decision, failure taxonomy, dated next actions, release-gate review |

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

## Session 75 — Diagnosis-First Tuning

Students must preserve default parameters as the reference and state the diagnosed problem before changing a parameter.

Required evidence:

- current baseline and validation spread;
- dominant limitation: underfitting, overfitting, optimisation, feature/data, class imbalance, or compute;
- parameter hypothesis and expected effect;
- one controlled manual experiment at a time;
- runtime and stability record;
- keep, reject, or investigate decision;
- optional automated-search rationale only after the manual cycle.

Use the reusable tuning lessons and resource maps under:

`02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/`

The optional Optuna extension remains optional and must not replace diagnosis or manual evidence.

## Session 76 — Model Ensembling

An ensemble counts only when:

- each base model is independently valid and sufficiently strong;
- predictions correspond to identical held-out rows or valid OOF generation;
- model diversity is measured through errors or prediction correlation;
- the ensemble is compared with the best single model, not only a weak baseline;
- improvement exceeds expected validation noise;
- added complexity does not create unacceptable runtime or submission risk.

Required evidence:

- base-model score, spread, runtime, and error profile;
- prediction-alignment check;
- weighting or stacking rationale;
- leakage check;
- ensemble ladder;
- best-single-versus-ensemble decision.

## Session 77 — Full Competition Simulation

Use the target competition duration, not an artificial 75-minute compression.

The simulation must include:

1. task and submission-schema reading;
2. input `X`, target/output `y`, modality, metric, and prediction-time boundary;
3. data-quality and leakage audit;
4. frozen validation protocol;
5. constant or rule baseline plus a simple trainable baseline;
6. reproducible feature or preprocessing pipeline;
7. one controlled improvement;
8. error analysis;
9. optional tuning and ensembling only if earlier gates pass;
10. fresh-environment execution;
11. submission-format validation;
12. backup submission and failure-recovery procedure.

## Session 78 — Postmortem and Readiness Conference

The student must explain:

- what the real task was;
- why the validation design was trustworthy;
- which data-quality risk mattered most;
- which model or feature decision produced reliable value;
- which experiments were rejected and why;
- whether tuning followed a diagnosis;
- whether an ensemble genuinely beat the best single model;
- whether the final system reproduced from a clean environment;
- which failure category remains highest risk;
- what the next three dated actions are.

## Reusable Eight-Lesson Extension Bank

The full eight-lesson bank under `02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/` remains available for deeper practice:

1. task recognition;
2. data quality and validation;
3. feature engineering;
4. model selection and baseline;
5. classical-model tuning;
6. deep-learning tuning;
7. model ensembling;
8. full sprint simulation.

These are reusable lesson options, not canonical Sessions 79–86 and not a replacement for the four-session Phase 8 map.

## Non-Negotiable Rules

1. Protect validation quality before chasing score.
2. Do not tune on the hidden test, public leaderboard, or reused final holdout.
3. Do not tune before a valid baseline, model comparison, and error analysis exist.
4. Record hypothesis, named change, held constants, validation result, spread, runtime, and decision.
5. Automated search is optional and follows a manual cycle.
6. Stacking uses OOF predictions; in-sample base predictions are forbidden.
7. Preserve rejected experiments and failed ensembles.
8. Stop complexity early enough to complete fresh-runtime and submission validation.
9. Current official competition rules override all resource suggestions.

## Phase Gate

A student passes only when the student independently completes the full workflow, produces a valid and reproducible submission, explains each major decision, demonstrates no critical leakage or split failure, and identifies the highest-value next improvement without relying on hidden-test feedback.
