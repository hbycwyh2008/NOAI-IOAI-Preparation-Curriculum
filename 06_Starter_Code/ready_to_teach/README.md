# Ready-to-Teach Starter Code

These files are executable teaching scaffolds. They include validation and error handling but deliberately leave the lesson-specific modelling decision to the student.

## Core Utilities

- `metrics_from_counts.py` — hand-checkable binary metrics.
- `generate_practice_data.py` — reproducible tabular, text, and diagram-caption practice data.
- `sklearn_mixed_baseline.py` — leakage-safe mixed-type baseline with group-aware option.
- `pytorch_training_template.py` — device-safe train/validate/checkpoint scaffold.
- `validate_submission.py` — row/schema/range/identifier validation.

## Competition Sprint Utilities

- `competition_sprint_experiment_log.py` — create, append, validate, and summarize a controlled-experiment CSV log.
- `manual_tuning_template.py` — executable one-variable-at-a-time scikit-learn tuning example that keeps the test split out of tuning.
- `optuna_tuning_template.py` — small local Optuna study using cross-validation and a documented search space.

## Example Commands

```bash
python 06_Starter_Code/ready_to_teach/competition_sprint_experiment_log.py init \
  --path /tmp/experiment_log.csv

python 06_Starter_Code/ready_to_teach/manual_tuning_template.py \
  --output /tmp/manual_tuning_results.json

python 06_Starter_Code/ready_to_teach/optuna_tuning_template.py \
  --trials 3 \
  --output /tmp/optuna_tuning_results.json
```

Run scripts from the repository root. Generated data are practice data only; scored-mock hidden labels remain teacher-only.

Automated tuning must not be used before students can explain the metric, validation split, baseline, manual tuning result, and search-space rationale.