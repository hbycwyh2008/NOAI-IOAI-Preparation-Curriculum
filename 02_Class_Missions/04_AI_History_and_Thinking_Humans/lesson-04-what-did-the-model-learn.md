# Session 36 — What Did the Model Actually Learn?

**Class duration:** 70 minutes  
**Required reading before class:** Chapters 6–7  
**Essential question:** Why can a highly accurate system still be unreliable?

## Required Mastery

Students must be able to:

1. Explain that a model may learn task-relevant features, accidental correlations, collection artefacts, backgrounds, or watermarks.
2. Explain shortcut learning.
3. Explain distribution shift between training conditions and deployment conditions.
4. Describe what adversarial examples reveal about model fragility.
5. Distinguish accuracy, robustness, fairness, interpretability, and safety.
6. Explain how aggregate metrics can hide failures in particular groups or situations.
7. Explain that datasets, labels, metrics, and deployment boundaries contain human choices.
8. Identify human responsibility for data collection, model selection, deployment, monitoring, and stopping rules.
9. Propose tests that would reveal whether a model depends on a shortcut.

## Misconceptions to Reject

- A high validation score is sufficient evidence for deployment.
- Every failure can be fixed by making the model larger.
- Data is a complete and neutral copy of the real world.
- Fairness can be established from one overall accuracy number.

## Core Pattern

```text
training data
→ learned correlation
→ evaluation protocol
→ deployment environment
→ failure mode
→ affected people
```

## 70-Minute Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–7 | **Skill Warm-Up** | Classify examples as relevant features, shortcuts, distribution shift, or adversarial manipulation. |
| 7–14 | **Talk Robin 1** | Compare one model success with one hidden dependency from the reading. |
| 14–20 | **Entry Check** | Explain why validation accuracy and deployment reliability are different claims. |
| 20–32 | **Core Pattern** | Trace how training correlations become deployment failures. |
| 32–48 | **Guided Practice** | Analyse a hospital model that performs well at one hospital and poorly at another. Consider equipment, populations, labels, and workflows. |
| 48–62 | **Independent Rebuild** | Produce an AI trust checklist covering data origin, label quality, deployment shift, subgroup results, extreme inputs, error costs, human review, and stop conditions. |
| 62–70 | **Talk Robin 2 + Evidence** | Apply the checklist to the hospital case and defend the highest-priority test. |

## Exit Evidence

Given a system with high accuracy, ask at least five questions that accuracy alone cannot answer.

## Gate

The student must identify at least one plausible learned shortcut, one distribution-shift risk, and one human monitoring responsibility.
