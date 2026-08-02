# Ready-to-Teach Starter Code

These files are executable teaching scaffolds. They include validation and error handling but deliberately leave the lesson-specific modelling decision to the student.

## Core Utilities

- `metrics_from_counts.py` — hand-checkable binary metrics.
- `generate_practice_data.py` — reproducible tabular, text, and diagram-caption practice data.
- `sklearn_mixed_baseline.py` — leakage-safe mixed-type baseline with group-aware option.
- `pytorch_training_template.py` — device-safe train/validate/checkpoint scaffold.
- `validate_submission.py` — row/schema/range/identifier validation.

## Competition Sprint Utilities

Use them in workflow order:

1. `competition_sprint_experiment_log.py` — create, append, validate, and summarize a controlled-experiment CSV log.
2. `manual_tuning_template.py` — executable one-variable-at-a-time scikit-learn tuning example that keeps the test split out of tuning.
3. `model_ensembling_template.py` — generate leakage-safe OOF predictions, measure prediction diversity, test a small probability-weight ladder, and confirm on a final holdout.
4. `validate_submission.py` — check the final output before submission.

Optional extension:

- `optuna_tuning_template.py` — small local Optuna study using cross-validation and a documented search space. Use only after a manual tuning cycle is understood.

## Example Commands

```bash
python 06_Starter_Code/ready_to_teach/competition_sprint_experiment_log.py init \
  --path /tmp/experiment_log.csv

python 06_Starter_Code/ready_to_teach/manual_tuning_template.py \
  --output /tmp/manual_tuning_results.json

python 06_Starter_Code/ready_to_teach/model_ensembling_template.py \
  --output /tmp/model_ensembling_results.json

python 06_Starter_Code/ready_to_teach/optuna_tuning_template.py \
  --trials 3 \
  --output /tmp/optuna_tuning_results.json
```

Run scripts from the repository root. Generated data are practice data only; scored-mock hidden labels remain teacher-only.

## Stage Rules

- Do not compare models before the validation design and leakage checks are defensible.
- Do not tune before a constant/rule, simple, and contrasting model comparison exists.
- Do not use automated tuning before students can explain the metric, split, model-selection result, manual tuning result, and search-space rationale.
- Do not train stacking meta-models on in-sample base predictions; use OOF predictions.
- Do not keep an ensemble merely because it contains more models. Compare it with the best single model and account for validation noise, runtime, memory, and submission risk.