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
→ competition sprint: task recognition, data engineering, tuning, reliable submission, and postmortem
→ selected IOAI-style advanced tasks
```

## Scheduled Options

| Pathway | Sessions | Best use |
|---|---:|---|
| Round 1 preparation | 1–38 | students preparing mainly for the paper-based stage |
| Full NOAI preparation | 1–67 | students preparing for Round 1 and Round 2 |
| Full competition pathway | 1–75 | full NOAI preparation plus the eight-session competition sprint |
| IOAI extension | selected after Session 75 | students who meet baseline, validation, reproducibility, and mock-readiness gates |

## Competition Sprint

The final eight sessions focus on:

1. identifying the real task, input, output, labels, metric, and constraints;
2. choosing the simplest valid baseline and model family;
3. auditing data, designing the validation split, and preventing leakage;
4. performing time-bounded cleaning and feature engineering;
5. diagnosing classical-model problems before searching parameters;
6. tuning deep-learning training in a disciplined order;
7. using PyTorch schedulers and Optuna only after manual experiments are understood;
8. completing a full simulation with submission validation, fresh-runtime evidence, and a postmortem.

## Core Principle

A sophisticated model is not competition-ready unless the student can explain the task, defend the validation, reproduce the baseline, record controlled experiments, produce a valid submission, and run the solution from a fresh environment.