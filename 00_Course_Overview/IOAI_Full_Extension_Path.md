# IOAI Full Extension Path

This is the international-preparation route. It preserves the complete canonical pathway and adds task-specific extension sprints only after the relevant prerequisites and annual-rule checks are complete.

## Entry Standard

Students enter through one of two routes:

- complete the full canonical Sessions 1–58 and pass the secured mixed assessment; or
- complete the NOAI Round 1 compressed route, then recover every omitted prerequisite before Session 59.

The compressed-route recovery set is exactly:

```text
Sessions 19–23, 32, 34–39, and 47
```

These Sessions restore the omitted AI foundations, deep-network bridge, reading-and-claim-analysis seminars, and neural-network introduction. A compressed Round 1 completion must not be described as completion of Sessions 1–58.

No student skips validation, reproducibility, error analysis, or the annual-rule check merely because they already know a model API.

## Exact Session Route

| Stage | Required Sessions | Purpose |
|---|---|---|
| foundations and classical ML | 1–58 | Python, data tools, ML foundations, AI reasoning, mathematical model language, classical models, controlled workflow, mixed assessment |
| deep learning and modalities | 59–70 | PyTorch, CNN, transfer learning, sequence models, attention, audio/multimodal, capstone |
| competition diagnosis | 71–74 | comparison, EDA, feature engineering, validation, calibration, error analysis |
| competition execution | 75–78 | tuning, ensembling, full simulation, postmortem and readiness conference |

**Canonical requirement:** Sessions 1–78 exactly once and in order.

For a student coming from the compressed Round 1 route, use the pathway planner to expose the omitted prerequisites before assigning Session 59:

```bash
python scripts/plan_learning_path.py \
  --pathway ioai_full \
  --completed-pathway noai_round1
```

## Extension Sprints

Extension sprints do not create new canonical Session numbers. Each sprint uses current official tasks, authorised datasets, permitted local assets, and official framework documentation.

| Sprint | Minimum prerequisite | Required output |
|---|---|---|
| E1 — at-home task reproduction | Sessions 1–74 | clean reproduction, asset manifest, metric match, error analysis |
| E2 — Contest 1 continuation | Sessions 75–78 and E1 | controlled improvements under the same task family and rules |
| E3 — novel-task rapid baseline | Sessions 1–78 | task contract and first valid baseline under a fixed time budget |
| E4 — modality depth | relevant Session 63–69 | CV, NLP, audio, time-series, scientific-ML, or multimodal comparison |
| E5 — offline/runtime rehearsal | Gate 3 evidence | clean environment, local assets, package list, memory/runtime record |
| E6 — secured full simulation | Gates 2–4 evidence | private scoring, timed submission, appeal/review record, postmortem |

## Annual Alignment Contract

Before every scored sprint, record:

- current official syllabus and contest-rule access date;
- task stage: At-Home, Contest 1 continuation, Contest 2 novel task, Team Challenge, or other official track;
- internet, website, AI-assistant, API, pretrained-model, package, hardware, storage, and submission rules;
- authorised datasets and locally supplied assets;
- runtime and scoring constraints;
- differences from the previous year and resulting curriculum changes.

Historical rules are examples only. The dated official documents for the active event override this repository.

## Exit Standard

IOAI full-extension readiness requires:

- completion or equivalent inspected evidence for Sessions 1–78;
- completion of every recovery Session when entering from a compressed pathway;
- model-recognition mastery across classical, deep-learning, modality, and generation tasks;
- at least one clean at-home-task reproduction and one novel-task rapid baseline;
- fresh-environment execution with exact permitted assets and packages;
- secured timed simulations for continuation and novel-task conditions;
- task-family, metric, validation, baseline, improvement, error-analysis, and reproducibility explanations;
- completed runtime, authenticated-access, assessment-security, representative-pilot, and current-year rule gates for the named cohort;
- a readiness conference that records ready, conditional, and blocking evidence rather than a single percentage.

## Capability Boundary

This route is not a guarantee of selection, medal, score, or compatibility with future rules. Readiness applies only to the named year, cohort, environment, accounts, authorised assets, and evidence date. New official clarifications, task packages, or platform changes reopen the affected gates.
