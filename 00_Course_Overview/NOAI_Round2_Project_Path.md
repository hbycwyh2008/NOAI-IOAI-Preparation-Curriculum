# NOAI Round 2 Project Path

This route turns first-round knowledge into a reproducible application-practice project. It assumes the learner has met the exit standard of the NOAI Round 1 compressed path or has equivalent evidence.

## Entry Standard

Before starting, the student must independently:

- read and audit an unfamiliar tabular dataset;
- train and evaluate one leakage-safe scikit-learn baseline;
- explain the selected metric and validation design;
- use Git, notebooks, relative paths, and the repository evidence format;
- pass the model-recognition mastery rule.

## Exact Session Route

| Block | Required Sessions | Purpose | Suggested pace |
|---|---|---|---|
| tabular project rehearsal | 57–58 | end-to-end pipeline, controlled improvement, postmortem, mixed assessment | 2 sessions |
| deep-learning implementation | 59–70 | tensors, training loops, CNN, transfer learning, RNN/LSTM, attention, audio/multimodal, capstone | 12 sessions |
| diagnosis and evaluation | 71–74 | model comparison, EDA/data quality, feature engineering, validation, calibration, error analysis | 4 sessions |
| competition workflow | 75–78 | tuning, ensembling, timed simulation, readiness conference | 4 sessions |

**Additional route length:** 22 scheduled sessions after Round 1 qualification.

A cohort with a strictly tabular official task may defer Sessions 63–70 only when the teacher records the omitted capability and the current official rules do not require those domains. Sessions 71–78 remain required for any project route.

## Project Milestones

1. **Problem contract:** row/sample, target, output, metric, constraints, submission schema.
2. **Data audit:** schema, missingness, duplicates, groups/time, leakage, shift, class balance.
3. **First valid baseline:** simple, reproducible, timed, and saved with seed/version information.
4. **Feature/model experiment:** one change per experiment with a hypothesis and fixed validation.
5. **Deep-model comparison:** only when the modality and data volume justify it.
6. **Error analysis:** slices, confusion/disagreement cases, failure examples, and next action.
7. **Tuning and ensemble:** diagnosis first; no blind search or unvalidated stacking.
8. **Submission rehearsal:** fresh environment, relative paths, runtime limit, validated output file.
9. **Postmortem:** what improved, what failed, what remains uncertain, and what would be tried next.

## Exit Standard

A student exits this route only when:

- the complete project runs from a clean checkout or clean hosted account;
- the baseline, validation split, metric, and submission format are justified in writing and orally;
- every preprocessing step is fit inside the correct training boundary;
- at least three controlled experiments are logged and interpreted;
- one simple and one stronger model are compared under the same validation design;
- fresh-kernel execution and submission validation pass;
- hidden labels, private tests, credentials, and restricted data are absent from the public repository;
- the secured Round 2 mock/project rubric meets the teacher-defined threshold;
- the student can rebuild the core pipeline without following a step-by-step tutorial.

## Capability Boundary

Completion qualifies only the named project modality, runtime, ruleset, and cohort environment. It does not prove access to every official platform, legality of every external asset, performance on unseen IOAI tasks, or readiness for all modalities. Those claims require the IOAI full extension route and the release-evidence gates.
