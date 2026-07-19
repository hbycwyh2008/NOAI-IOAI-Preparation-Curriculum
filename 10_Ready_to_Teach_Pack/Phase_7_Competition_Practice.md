# Phase 7 — Competition Practice

Sessions 58–67. These sessions use realistic durations and produce complete competition evidence.

---

## Session 58 — Round 2 Data Audit and Validation Strategy

**Duration:** 90 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–10 | Read task/metric and write assumptions |
| 10–30 | Audit files, schema, labels, groups, and possible leakage |
| 30–42 | Talk round: defend problem type and split |
| 42–55 | Teacher challenge of validation design |
| 55–72 | Implement split and minimum audit report |
| 72–84 | Independent leakage test |
| 84–90 | Submit validation memo |

### Required output

A `validation_memo.md` containing task type, target, official metric, unit of independence, split method, leakage risks, class/target distribution, train/test differences, and limitations.

### Worksheet

1. What is one row, one entity, and one prediction in this task?
2. Are multiple rows linked by patient, speaker, source file, time, or original image?
3. Which information is available at prediction time?
4. Which split best simulates deployment?
5. What baseline score could be achieved by majority/mean prediction?
6. Which slices must be reported even if they are not the official metric?
7. Name three ways public-leaderboard feedback could mislead model selection.

### Independent task

Given an unfamiliar dataset folder, complete the audit and create a split without training a model. The teacher reviews only the reasoning and code reproducibility.

---

## Session 59 — Baseline-First Development and Submission Validation

**Duration:** 90 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–8 | Restate metric, split, and first-valid-output goal |
| 8–20 | Choose the simplest defensible baseline |
| 20–50 | Build end-to-end pipeline |
| 50–62 | Calculate local metric and inspect errors |
| 62–75 | Generate submission |
| 75–83 | Run validator and fresh-runtime test |
| 83–90 | Commit baseline report |

### Baseline requirements

- runs from a fresh environment;
- uses only permitted data/assets;
- has a valid local split;
- produces the official row count, ID order, columns, types, and prediction range;
- records runtime, seed, metric, and known limitations;
- does not depend on notebook state.

### Worksheet

1. Define the minimum baseline for tabular, image, text, and audio tasks.
2. Which failure is more urgent: weak score or invalid submission? Why?
3. List eight automatic submission checks.
4. Why must test IDs be preserved independently from feature preprocessing?
5. Explain why a constant baseline remains useful.
6. State one condition under which a sophisticated model should be abandoned during a contest.

### Independent task

Produce the first valid local score and submission in 45 minutes. Any improvement attempted before validator success is logged as a process error.

---

## Session 60 — Controlled Experiments, Leaderboard Reasoning, and Post-Mortem

**Duration:** 90 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–10 | Review baseline and dominant errors |
| 10–20 | Write one experiment hypothesis |
| 20–45 | Run one controlled experiment |
| 45–55 | Compare result and uncertainty |
| 55–65 | Analyse public/private leaderboard risks |
| 65–78 | Decide keep/reject and choose next experiment |
| 78–90 | Write experiment record and post-mortem |

### Essential teaching content

An experiment record must contain hypothesis, single main change, fixed factors, validation score/distribution, runtime, error-slice changes, decision, and next step. Leaderboard changes are secondary evidence; repeated adaptation to a public board can overfit it.

### Worksheet

1. Rewrite “try a bigger model” as a testable hypothesis.
2. Identify confounded experiments in three logs.
3. Why should seeds/folds remain fixed for a direct comparison?
4. A local CV gain is .001 with fold SD .015. How strong is the evidence?
5. Public leaderboard rises while local validation falls. List possible causes.
6. Explain model ensembling only after individual validation is trustworthy.
7. Write a stopping rule based on remaining time and submission reliability.

### Independent task

Run exactly two experiments within a fixed 50-minute budget and justify the final model using more than the best single score.

---

## Session 61 — Past-Paper Reproduction: NLP Sequence Task

**Duration:** 180 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–15 | Read historical task without solution |
| 15–35 | Audit text/labels and choose split |
| 35–65 | Simple baseline: length/TF-IDF or token statistics |
| 65–105 | Sequence-model or pretrained-model baseline |
| 105–125 | Error analysis and one controlled change |
| 125–150 | Final valid predictions and reproducibility check |
| 150–170 | Compare with authorised reference approach |
| 170–180 | Post-mortem |

### Reproduction task specification

Students receive sentences with a boundary label for each character/token and must predict segmentation boundaries. Required routes:

- baseline: frequency/rule or logistic features around each position;
- sequence route: embedding plus BiLSTM/RNN or approved compact transformer;
- evaluation: boundary-level precision, recall, and F1;
- split: prevent duplicate sentence leakage;
- output: one prediction sequence per input with exact length matching.

### Worksheet

1. Define input unit and output unit.
2. Why is ordinary sentence-level accuracy insufficient?
3. How does padding affect sequence labels?
4. State two useful contextual features for a position-level baseline.
5. Explain why prediction length must exactly match source length.
6. Design three error categories: unknown words, punctuation, and ambiguous boundaries.

### Deliverables

Audit, baseline, sequence model, validation report, prediction validator, ten annotated errors, and comparison with reference only after independent completion.

---

## Session 62 — Past-Paper Reproduction: Tabular / AI4Science Task

**Duration:** 180 minutes

### Task specification

Predict a continuous scientific target from mixed numerical/categorical descriptors. Data contain missing values, nonlinear interactions, repeated experimental groups, and one misleading identifier.

### Timeline

| Time | Activity |
|---|---|
| 0–20 | Task/metric/schema audit |
| 20–40 | Group-aware validation design |
| 40–65 | Constant and linear baselines |
| 65–100 | Tree-ensemble baseline |
| 100–125 | Feature/transform experiment |
| 125–145 | Residual and group-slice analysis |
| 145–165 | Final submission and validator |
| 165–180 | Post-mortem |

### Required modelling routes

- mean prediction;
- regularised linear model with pipeline;
- random forest or gradient boosting;
- optional domain-inspired ratio/log/interaction features;
- metric: RMSE plus group-wise MAE report.

### Worksheet

1. Why might random row splitting overestimate scientific generalisation?
2. Identify identifier leakage and target-derived aggregate leakage.
3. Explain when log-transforming a positive skewed feature may help.
4. Compare residuals by experimental group.
5. State why a lower overall RMSE can still hide one failed regime.
6. Write the exact output-schema checks.

### Deliverables

Group-aware split, three baselines, experiment log, residual plots, group slice table, submission, validator result, and model card.

---

## Session 63 — Past-Paper Reproduction: Audio or Image Task

**Duration:** 180 minutes

### Task specification

Detect synthetic speech from short audio clips or classify Mel-spectrogram images. The data intentionally include speaker/source imbalance and recording artifacts.

### Timeline

| Time | Activity |
|---|---|
| 0–20 | Audio/source audit |
| 20–40 | Speaker/source-aware split |
| 40–70 | Log-Mel or simple spectral baseline |
| 70–110 | CNN/pretrained-audio baseline |
| 110–135 | Error/source-slice analysis |
| 135–155 | One shortcut-reduction experiment |
| 155–170 | Submission and offline test |
| 170–180 | Post-mortem |

### Worksheet

1. What evidence suggests source leakage?
2. Why can file format or duration identify the class accidentally?
3. Compare clip-level and speaker-level splitting.
4. Define positive class and threshold policy.
5. Name three audio augmentations and their label-preservation assumptions.
6. Design a source-held-out stress test.

### Deliverables

Audio audit, source-aware baseline, model comparison, threshold analysis, class/source confusion matrices, 12 reviewed errors, valid submission, and reproducible inference.

---

## Session 64 — Timed Round 1 Mock B

**Duration:** 120 minutes, closed-note

### Timeline

| Time | Activity |
|---|---|
| 0–5 | Instructions and answer-sheet check |
| 5–105 | 100-point paper |
| 105–115 | Independent review |
| 115–120 | Confidence coding and submission |

Use `Round_1_Mock_B.md`. Correction occurs separately using the private teacher key. Students must retain at least ten minutes for checking.

---

## Session 65 — Timed Round 2 Tabular Mock

**Duration:** 240 minutes

### Task: Student Persistence Risk

Predict whether a student will fail to complete an online programme. Training data include numeric engagement features, categorical course/device fields, missing values, repeated school groups, and timestamps. Test labels are hidden.

### Rules

- metric: macro F1;
- split must respect `school_id` groups;
- prohibited: target-derived features or external personal data;
- submission columns: `student_id,prediction`;
- prediction must be integer 0/1;
- all code must run offline from a fresh environment.

### Timeline

| Time | Activity |
|---|---|
| 0–20 | Read task and audit schema |
| 20–45 | Group split and constant/simple baseline |
| 45–90 | Leakage-safe sklearn pipeline |
| 90–125 | Error analysis and threshold table |
| 125–165 | Two controlled experiments |
| 165–190 | Select model and refit deliberately |
| 190–215 | Create/validate submission |
| 215–230 | Fresh-runtime reproduction |
| 230–240 | Final report and backup submission |

### Required evidence

Time to first valid baseline, validation design, baseline score, experiment table, class/school slices, threshold decision, submission validator log, final file hash, and post-mortem.

---

## Session 66 — Timed Round 2 Multimodal Mock

**Duration:** 360 minutes

### Task: Diagram–Caption Consistency

Each example contains a short caption, a small diagram/image, and metadata. Predict whether the caption correctly describes the diagram. Students may use approved offline image/text models or independent modality baselines.

### Files

- `train.csv`: `sample_id,caption,source,label`;
- `test.csv`: same without label;
- `images/`: PNG files named by sample ID;
- output: `sample_id,probability` with values in `[0,1]`;
- metric: ROC AUC; diagnostic metric: macro F1 at a documented threshold.

### Timeline

| Time | Activity |
|---|---|
| 0–30 | Audit text/image/source pairs |
| 30–60 | Source-aware split and constant baseline |
| 60–110 | Text-only baseline |
| 110–160 | Image-only structural/CNN baseline |
| 160–210 | Multimodal fusion baseline |
| 210–250 | Error and source-slice analysis |
| 250–290 | Two controlled improvements |
| 290–320 | Final fit/inference |
| 320–340 | Submission validation and fresh run |
| 340–360 | Post-mortem, hashes, backups |

### Minimum routes

1. Text TF-IDF/logistic or allowed local encoder.
2. Image colour/shape features or CNN embeddings.
3. Late fusion by concatenating calibrated probabilities/features.
4. Compare single-modality versus fusion errors.

### Stress tests

- shuffle images relative to captions;
- evaluate held-out sources;
- evaluate short versus long captions;
- verify whether source metadata alone predicts labels;
- inspect high-confidence wrong pairs.

---

## Session 67 — Final Readiness Conference

**Duration:** 45 minutes per student

### Timeline

| Time | Activity |
|---|---|
| 0–5 | Student states current readiness and evidence |
| 5–15 | Cold Round 1 questions: one calculation, trace, concept |
| 15–25 | Cold Round 2 defence of validation, model, and error analysis |
| 25–32 | Repository and reproducibility inspection |
| 32–38 | Review mock reliability and time management |
| 38–43 | Agree three highest-priority actions |
| 43–45 | Sign readiness status and next checkpoint |

### Readiness statuses

- **Ready:** meets all minimum gates and has no critical reliability failure.
- **Conditionally ready:** one bounded gap with a dated repair plan.
- **Not yet ready:** missing baseline/reproducibility, unsafe validation, repeated invalid submissions, or major Round 1 gaps.

### Minimum evidence reviewed

- two Round 1 mocks at/above threshold;
- one clean sklearn pipeline;
- one clean PyTorch training/inference pipeline;
- tabular, image, text, and audio exposure;
- at least two valid timed Round 2 submissions;
- experiment and error logs;
- offline-environment smoke test;
- oral ability to explain submitted work and disclosed AI use.

### Final action plan

Each student records exactly three priorities, practice method, evidence of completion, deadline, and likely failure condition. Generic goals such as “study more” are rejected.