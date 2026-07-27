# Competition Sprint Submission Checklist

Use this checklist before the final submission is produced and again before it is uploaded.

## 1. Task and Metric

- [ ] I can state the task type in one sentence.
- [ ] I identified the exact prediction target or output format.
- [ ] I confirmed whether the metric is maximised or minimised.
- [ ] My local validation metric matches the competition metric or I documented the approximation.
- [ ] I did not optimise a convenient metric that differs from the competition objective without justification.

## 2. Data and Split

- [ ] Training, validation, and test roles are separated.
- [ ] The competition test set was not used for tuning.
- [ ] Group, time, source, patient, speaker, image-family, or duplicate constraints were checked.
- [ ] Preprocessing was fitted only on training data.
- [ ] Label leakage and target-derived features were checked.
- [ ] Duplicate or near-duplicate samples across splits were checked.
- [ ] Missing, corrupt, or out-of-range items were handled consistently.

## 3. Baseline and Experiments

- [ ] The simplest valid baseline is saved and reproducible.
- [ ] Every experiment has a written hypothesis.
- [ ] Manual tuning changed one main variable at a time.
- [ ] Automated search was used only after manual tuning and validation checks.
- [ ] Rejected experiments remain in the log.
- [ ] The selected model shows a reliable validation improvement, not only a leaderboard jump.
- [ ] Runtime, memory, and inference cost fit the competition constraints.

## 4. Error Analysis

- [ ] I inspected representative false positives, false negatives, or high-error samples.
- [ ] I grouped errors into meaningful categories.
- [ ] The final improvement targets a documented error category or bottleneck.
- [ ] I know the largest remaining failure mode.
- [ ] I know what I would try next if more time were available.

## 5. Prediction File

- [ ] Row count matches the required test rows.
- [ ] Identifier values and row order are correct.
- [ ] Column names match the required schema exactly.
- [ ] Data types are correct.
- [ ] No values are missing unless the format explicitly permits them.
- [ ] Probabilities or scores are in the required range.
- [ ] Class labels use the required encoding.
- [ ] No index column was added accidentally.
- [ ] The output filename is correct.
- [ ] The file opens successfully after saving.

## 6. Fresh Runtime

- [ ] The final notebook or script starts from a clean environment.
- [ ] Required files and relative paths are present.
- [ ] Random seeds and package versions are recorded.
- [ ] Training and inference complete without hidden notebook state.
- [ ] The final prediction file can be regenerated from the saved code.
- [ ] The saved model/checkpoint loads successfully when required.

## 7. Competition Rules and Artificial-Intelligence Assistance

- [ ] Internet, API, pretrained-model, and package permissions were checked.
- [ ] All external models, data, or tools are permitted.
- [ ] Artificial-intelligence assistance is recorded according to the rules.
- [ ] Suggested code was tested, understood, and verified.
- [ ] No hidden label, private test information, or prohibited data source was used.

## 8. Final Time Decision

```text
Time remaining:
Current validated score:
Largest unresolved risk:
Expected gain from further tuning:
Expected time required:
Decision: tune / fix / freeze / submit
Reason:
```

## Required Final Evidence

- [ ] final code or notebook;
- [ ] final prediction/submission file;
- [ ] validation result;
- [ ] experiment log;
- [ ] error-analysis table;
- [ ] fresh-runtime record;
- [ ] artificial-intelligence-use note;
- [ ] postmortem.