# NOAI / IOAI Competition Preparation Pathway

The curriculum develops competition readiness in stages rather than asking students to jump directly into advanced models.

```text
Competition orientation and evidence habits
→ Python code reading, tracing, debugging, and small programs
→ artificial-intelligence and machine-learning foundations
→ neural-network and convolutional-neural-network reasoning
→ NOAI Round 1 paper-test preparation
→ data audit, feature engineering, and scikit-learn workflow
→ PyTorch and computer-vision / natural-language-processing / audio / large-language-model tasks
→ official-style reproductions and timed Round 2 mocks
→ competition sprint: task definition → data quality → feature engineering → model selection → tuning → model ensembling → reliable submission
→ selected IOAI-style advanced tasks
```

## Scheduled Options

| Pathway | Sessions | Best use |
|---|---:|---|
| Round 1 preparation | 1–38 | students preparing mainly for the paper-based stage |
| Full NOAI preparation | 1–67 | students preparing for Round 1 and Round 2 |
| Full competition pathway | 1–75 | full NOAI preparation plus the eight-session competition sprint |
| IOAI extension | selected after Session 75 | students who meet data, validation, modelling, reproducibility, and mock-readiness gates |

## Competition Sprint

The final eight sessions focus on:

1. formalising the real task, input `X`, output/target `y`, metric, prediction-time boundary, constraints, and submission schema;
2. auditing data quality, freezing the validation split, and preventing target, duplicate, identity, group, temporal, and preprocessing leakage;
3. building a reproducible feature pipeline and proving feature value through controlled tests and ablations;
4. preserving a constant or rule baseline, comparing a simple model with a contrasting model, and analysing error categories;
5. tuning a classical model only after diagnosing its dominant limitation;
6. tuning deep-learning training in a disciplined order;
7. ensembling only individually strong, complementary models using identical held-out or valid out-of-fold predictions;
8. completing a full simulation with configuration freeze, submission validation, fresh-runtime evidence, and a postmortem.

## Fixed Modelling Order

```text
data quality
→ feature engineering
→ model selection
→ tuning
→ model ensembling
```

Optuna and broad automated search are optional extensions after a manual tuning cycle. They do not replace model ensembling, reproducibility, or submission validation.

## Core Principle

A sophisticated model is not competition-ready unless the student can:

- explain the task and prediction-time boundary;
- defend data quality and validation;
- reproduce the feature pipeline;
- preserve and beat a simple baseline under one protocol;
- connect tuning changes to visible evidence;
- prove that an ensemble beats the best single model rather than only a weak baseline;
- produce a valid submission;
- run the final system from a fresh environment.