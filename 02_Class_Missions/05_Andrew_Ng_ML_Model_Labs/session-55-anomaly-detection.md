# Session 55 — Anomaly Detection

**Class duration:** 75 minutes  
**Task family:** rare-event or low-density detection

## Required Mastery

Students must be able to:

1. identify normal examples, anomalies, features, and the intended alert output;
2. explain why anomaly detection may use mostly or only normal training data;
3. calculate or interpret mean and variance for a feature;
4. explain low probability or low density as evidence of unusual behaviour;
5. distinguish anomaly detection from ordinary supervised classification;
6. select a threshold using validation evidence rather than the test set;
7. explain precision/recall trade-offs under rare anomalies;
8. identify sensitivity to scaling, correlated features, distribution shift, and contaminated training data;
9. compare a statistical baseline with a simple supervised baseline when labels exist;
10. state the operational cost of false alarms and missed anomalies.

## Core Pattern

```text
model normal behaviour
→ calculate an anomaly score or density
→ choose a validation-based threshold
→ flag low-density or extreme examples
→ inspect false alarms, misses, and distribution shift
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | classify scenarios as regression, classification, clustering, or anomaly detection |
| 8–15 | Talk Robin 1 | compare the cost of a false alarm with a missed anomaly |
| 15–22 | Entry Check | interpret mean, variance, and one extreme observation |
| 22–35 | Core Pattern | normal model → score → threshold → alert |
| 35–53 | Guided Practice | choose a threshold from a small validation table |
| 53–67 | Independent Rebuild | implement a simple anomaly baseline and analyse flagged cases |
| 67–75 | Talk Robin 2 + Evidence | defend the threshold and one deployment warning |

## Required Evidence

- task-recognition card;
- feature mean/variance or score calculation;
- threshold table;
- precision/recall or error-cost explanation;
- flagged-case inspection;
- distribution-shift and contamination warning.

## Gate

The student can distinguish anomaly detection from classification, explain the score and threshold, and defend an alert policy using validation evidence and error costs.