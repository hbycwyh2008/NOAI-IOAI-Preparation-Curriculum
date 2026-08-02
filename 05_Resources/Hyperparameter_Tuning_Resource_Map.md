# Hyperparameter-Tuning Resource Map

**Canonical placement:** Session 75  
**Rule:** tuning begins only after task definition, split design, preprocessing, baseline, metric, and error analysis are trustworthy.

## Required Concept Sources

| Need | Preferred source | Student evidence |
|---|---|---|
| bias/variance and diagnosis | Andrew Ng Machine Learning Specialization and the Phase 5 model-diagnosis work | learning-curve or error diagnosis |
| regularisation and optimisation intuition | Deep Learning Specialization, Course 2 — Improving Deep Neural Networks | one parameter hypothesis and predicted effect |
| scikit-learn search and pipelines | current scikit-learn User Guide | leakage-safe search space and cross-validation plan |
| PyTorch tuning | PyTorch official tutorials and the maintained starter code | controlled training log and stopping rule |
| optional automated search | Optuna documentation and `06_Starter_Code/ready_to_teach/optuna_tuning_template.py` | bounded search, seed, budget, and held-out confirmation |

## Session 75 Sequence

```text
error analysis
→ one hypothesis
→ one controlled manual change
→ compare validation evidence
→ define a bounded search space
→ optional automated search
→ confirm on untouched evidence
→ record runtime and limitations
```

## Non-Negotiable Boundaries

- Do not tune on the test set or public leaderboard repeatedly.
- Do not compare trials that use different splits or preprocessing unless that is the controlled experiment.
- Do not use automated search to hide a missing baseline or invalid validation design.
- Record compute budget, failed trials, seed, metric direction, and stopping rule.
- Prefer a stable simpler model when the improvement is small, expensive, or not reproducible.

## Required Evidence

- diagnosis before tuning;
- manual tuning table;
- bounded search-space rationale;
- validation protocol;
- runtime/compute record;
- final parameter choice and rejected alternatives;
- untouched confirmation or explicit statement that none is available;
- limitations and next action.

Use [Session 75 classical tuning](../02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-classical-model-tuning.md), [Session 75 deep-learning tuning](../02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-deep-learning-tuning.md), and the [Phase 8 launcher](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md).
