# Round 2 Starter Notebook Coverage Map

This file maps coding-heavy Round 2 C/D modules to the starter notebook pattern students should use.

The public repo should provide starter structure, reproducibility habits, and evidence expectations. It should not provide full winning solutions, hidden labels, or answer keys.

## Notebook Pattern

Every Round 2 starter notebook should include:

1. environment check;
2. data audit;
3. split strategy;
4. baseline model;
5. validation metric;
6. controlled experiment;
7. error analysis;
8. submission validation;
9. fresh-run record;
10. AI-use note when applicable.

## Module Coverage

| Module | Notebook type | Required starter sections |
|---|---|---|
| 16 NumPy/Pandas/Matplotlib | data audit notebook | array/dataframe inspection, missing values, plots, summary table |
| 17 Data cleaning/feature engineering | feature notebook | leakage check, encoding, scaling, feature experiment |
| 18 sklearn workflow | tabular baseline notebook | split, pipeline, ColumnTransformer, CV, model comparison, submission |
| 19 PyTorch foundations | training loop notebook | tensor/device, Dataset, DataLoader, nn.Module, loop, checkpoint |
| 20 Computer vision | image baseline notebook | transforms, CNN/transfer baseline, augmentation memo, error grid |
| 21 NLP/sequence models | text baseline notebook | tokenization, vocabulary/padding, baseline, sequence model, metric |
| 22 Audio/speech | audio baseline notebook | waveform, spectrogram/Mel, classifier baseline, error analysis |
| 23 LLM/multimodality | LLM/multimodal verification notebook | prompt/input audit, API/local model record, verification table |
| 24 Round 2 project workflow | competition notebook | task reading, baseline, validation, ablation, submission, postmortem |
| 25 Past-paper reproduction | reproduction notebook | official task summary, baseline, reproduction notes, comparison |
| 26 Timed mock contests | timed notebook | time boxes, checkpoint log, final submission check |

## Student Notebook Header

Each notebook must begin with:

```text
Task:
Student:
Date:
Runtime:
Allowed resources:
AI-assistant use allowed? yes / no / restricted
Metric:
Submission format:
```

## Completion Rule

A Round 2 notebook is complete only when it can be rerun from a fresh runtime and produces the required evidence without manual hidden steps.
