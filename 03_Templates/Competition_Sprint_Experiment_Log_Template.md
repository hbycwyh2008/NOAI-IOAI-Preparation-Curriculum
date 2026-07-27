# Competition Sprint Experiment Log Template

Use one row per controlled experiment. Do not combine unrelated changes in one row.

## Task Context

```text
Task name:
Task type:
Input modality:
Target/output:
Competition metric:
Validation metric:
Validation design:
Baseline score:
Time remaining:
Compute/runtime constraints:
```

## Experiment Table

| Experiment ID | Hypothesis | Single change | Everything held constant | Validation result | Runtime | Decision | Next action |
|---|---|---|---|---:|---:|---|---|
| E00 Baseline |  | no tuning; simplest valid baseline |  |  |  | keep | establish error categories |
| E01 |  |  |  |  |  | keep / reject / investigate |  |
| E02 |  |  |  |  |  | keep / reject / investigate |  |
| E03 |  |  |  |  |  | keep / reject / investigate |  |

## Required Diagnosis Before Tuning

```text
Is the metric correct?
Is the split trustworthy?
Is there leakage?
Does the baseline run from a fresh environment?
Are labels and predictions aligned?
What is the largest error category?
Is the current problem mainly data, features, model capacity, optimisation, threshold, or runtime?
```

## Manual Tuning Record

```text
Variable selected:
Why this variable:
Search values:
Why this scale/range:
Best value:
Reliable gain over baseline:
Evidence that the gain is not split noise:
```

## Automated Search Record

Complete only after a manual cycle.

```text
Search tool:
Objective metric:
Search space:
Number of trials:
Sampler/strategy:
Compute budget:
Best parameters:
Best validation result:
Gain over manual tuning:
Additional runtime cost:
Was automated search worth the cost? Why?
```

## Stop Decision

```text
Expected gain from another tuning cycle:
Remaining submission risk:
Remaining fresh-runtime risk:
Remaining time:
Decision: continue tuning / freeze model / fix pipeline / validate submission
Reason:
```

## Evidence Checklist

- [ ] baseline preserved;
- [ ] one variable changed per manual experiment;
- [ ] no test-set tuning;
- [ ] metric and split recorded;
- [ ] runtime recorded;
- [ ] rejected experiments retained in the log;
- [ ] best configuration rerun from a fresh environment;
- [ ] final submission schema checked;
- [ ] artificial-intelligence assistance recorded and verified.