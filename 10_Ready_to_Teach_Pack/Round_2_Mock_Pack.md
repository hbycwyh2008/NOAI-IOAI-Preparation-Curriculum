# Round 2 Mock Pack

This pack contains two scored simulations and one shorter rehearsal. Hidden test labels and scoring scripts belong in the private teacher pack, never in the student repository.

---

# Mock R2-A — Tabular Student Persistence

**Duration:** 240 minutes  
**Primary metric:** macro F1  
**Submission:** `student_id,prediction` where prediction is integer `0` or `1`.

## Scenario

An online learning programme wants to identify students who may not complete the next course phase. The goal is to offer additional human support, not to deny access. Students must consider subgroup performance and responsible use.

## Distributed files

- `train.csv`: labels included;
- `test.csv`: labels removed;
- `data_dictionary.md`;
- `sample_submission.csv`;
- `validate_submission.py`.

## Columns

| Column | Type | Meaning |
|---|---|---|
| `student_id` | string | unique prediction ID; never a feature |
| `school_id` | string | grouping variable; students from one school are correlated |
| `device` | category | primary access device |
| `course` | category | programme track |
| `age` | numeric | may contain missing values |
| `weekly_hours` | numeric | recent average study time |
| `assignments_completed` | integer | completed tasks in the observation window |
| `forum_posts` | integer | posts/replies in the observation window |
| `late_ratio` | numeric | proportion of submitted work that was late |
| `target` | binary | 1 means did not complete; train only |

## Required constraints

1. Validation must keep each `school_id` entirely in one split.
2. `student_id` must not be used as a predictive feature.
3. No external personal data.
4. Preprocessing must be fitted on training folds only.
5. The final report must include school-level and class-level performance.
6. The system must be described as a support flag, not an automatic punishment decision.

## Minimum student deliverables

- `solution.ipynb` or equivalent scripts;
- `validation_memo.md`;
- `baseline_report.md`;
- `experiments.csv`;
- `error_analysis.md`;
- `submission.csv`;
- `validator_log.txt`;
- `environment.md`;
- `ai_usage_note.md`;
- meaningful commit history.

## Required baseline ladder

1. Majority/constant prediction.
2. Logistic regression mixed-type pipeline.
3. Tree ensemble.
4. Threshold tuning on validation only.
5. At most two additional controlled experiments before the final model is chosen.

## Mandatory analysis questions

1. Why is a random row split weaker than a school-group split?
2. Which class has lower recall and what harm can follow?
3. Does the model fail disproportionately for one device/course/school slice?
4. Which feature families are available at the real prediction time?
5. Would you deploy this model alone? State required human and monitoring controls.

## Scoring rubric — 100 points

| Area | Points |
|---|---:|
| valid group-aware validation | 15 |
| reproducible baseline pipeline | 15 |
| valid submission produced early | 10 |
| metric and threshold analysis | 15 |
| controlled experiments | 15 |
| error/subgroup analysis | 15 |
| engineering/fresh run | 10 |
| responsible-use explanation | 5 |

A high hidden score cannot compensate for leakage, invalid output, or a notebook that does not run.

---

# Mock R2-B — Diagram–Caption Consistency

**Duration:** 360 minutes  
**Primary metric:** ROC AUC  
**Diagnostic metric:** macro F1 at a documented validation-selected threshold  
**Submission:** `sample_id,probability`, finite probability in `[0,1]`.

## Scenario

Each example contains a simple diagram and a caption. Predict whether the caption correctly describes the diagram. Some source generators differ in style; source-specific shortcuts are deliberately present and must be audited.

## Distributed files

- `train.csv`: `sample_id,caption,source,label`;
- `test.csv`: `sample_id,caption,source`;
- `images/`;
- `sample_submission.csv`;
- `validate_submission.py`.

## Required routes

Students must establish all three before choosing a final solution:

1. **Text-only:** TF-IDF/logistic or an allowed local encoder.
2. **Image-only:** structural image features, small CNN, or allowed local image embeddings.
3. **Fusion:** combine single-modality probabilities/features using a validation-safe method.

## Mandatory stress tests

- source-held-out or source-stratified evaluation;
- shuffled image–caption pairs;
- metadata-only baseline;
- short versus long caption slices;
- confidence analysis and 15 high-confidence errors;
- ablation comparing text-only, image-only, and fusion.

## Prohibited shortcuts

- reading hidden labels or teacher files;
- using filenames/paths that encode labels;
- using source as the only decision rule;
- downloading models or calling APIs when the mock is designated offline;
- selecting threshold or fusion weights using test labels.

## Minimum deliverables

- full audit and validation memo;
- three modality baselines;
- fusion experiment;
- stress-test table;
- annotated error gallery;
- final inference script;
- validated submission;
- offline fresh-runtime log;
- model card and AI-use note.

## Scoring rubric — 100 points

| Area | Points |
|---|---:|
| task/data/source audit | 10 |
| valid validation and stress tests | 15 |
| text baseline | 10 |
| image baseline | 10 |
| fusion and ablation | 15 |
| experiment quality | 10 |
| error/confidence analysis | 10 |
| valid submission and engineering | 15 |
| explanation/responsible use | 5 |

---

# Mock R2-C — 90-Minute Baseline Rehearsal

This is not scored by hidden labels. The purpose is to reduce time to first valid baseline.

## Timeline

| Time | Output |
|---|---|
| 0–10 | task/metric/split statement |
| 10–25 | audit and constant baseline |
| 25–55 | first model pipeline |
| 55–68 | local metric and errors |
| 68–78 | submission creation |
| 78–85 | validator and fresh-run check |
| 85–90 | post-mortem |

Success means a valid, reproducible submission by minute 78—not the highest score.

---

# Teacher Distribution Procedure

1. Generate practice assets locally or use authorised task files.
2. Split train/test and store test labels only in the private teacher location.
3. Inspect class/group/source distributions before release.
4. Run the sample baseline and validators in the same runtime students will use.
5. Package inputs without generator code that reveals hidden labels.
6. Record SHA-256 hashes for distributed files.
7. Disable network access when simulating offline conditions.
8. Start all students from identical package versions and compute limits.
9. Collect submissions at fixed checkpoints and at the end.
10. Evaluate hidden labels only after the session closes.

# Submission Validation Commands

Binary tabular:

```bash
python 06_Starter_Code/ready_to_teach/validate_submission.py \
  test.csv submission.csv \
  --id-column student_id \
  --prediction-column prediction \
  --kind binary
```

Multimodal probability:

```bash
python 06_Starter_Code/ready_to_teach/validate_submission.py \
  test.csv submission.csv \
  --id-column sample_id \
  --prediction-column probability \
  --kind probability
```

# Post-Mock Conference Questions

1. When did you produce the first valid submission?
2. Which validation decision mattered most?
3. Which experiment consumed time without useful evidence?
4. What was the dominant error slice?
5. What would you remove from your workflow next time?
6. What must be cached/tested before an offline event?
7. Can you explain every component of the final pipeline without the notebook open?