# Session 65 — D2L Augmentation and Fine-Tuning Bridge

**Placement:** embedded inside Session 65; this packet does not add another scheduled session.  
**Role:** convert transfer-learning terminology into a leakage-safe, time-aware experimental workflow.

## Assigned D2L Sections

- [13.1 Image Augmentation](https://zh.d2l.ai/chapter_computer-vision/image-augmentation.html)
- [13.2 Fine-Tuning](https://zh.d2l.ai/chapter_computer-vision/fine-tuning.html)

Use the PyTorch tab and the teacher-selected experiment cells.

## Required Mastery

Students must be able to:

1. separate deterministic validation preprocessing from stochastic training augmentation;
2. explain why augmentation should preserve the task label;
3. replace a pretrained classifier head for a new number of classes;
4. freeze and unfreeze parameters deliberately;
5. use different learning rates for pretrained parameters and a new head when justified;
6. compare training from scratch, frozen-feature extraction, and fine-tuning under the same split and metric;
7. identify domain mismatch, class imbalance, and augmentation leakage risks.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read D2L 13.1–13.2 and extract the four fine-tuning steps. |
| Entry Check | Sort transformations into label-preserving, risky, or task-dependent categories. |
| Core Pattern | Trace pretrained backbone → replace head → freeze or unfreeze → choose learning rates → validate. |
| Guided Practice | Inspect parameter groups and confirm which parameters have `requires_grad=True`. |
| Independent Comparison | Run one controlled comparison between two strategies under the same data and compute budget. |

## Core Pattern

```text
source model
→ task-compatible preprocessing
→ new output head
→ freeze/unfreeze decision
→ learning-rate groups
→ controlled validation
→ class-wise error analysis
```

## Independent Task

Choose a small image-classification dataset and complete:

1. a no-pretraining or simple-CNN baseline;
2. a pretrained model with the classifier head replaced;
3. one frozen-backbone run;
4. one partial or full fine-tuning run when compute allows;
5. identical validation data and metrics for every run;
6. an error table containing at least five wrong predictions;
7. one augmentation ablation or justification for not using augmentation.

## Required Evidence

- train/validation transform table;
- model-head replacement code and shape check;
- frozen/unfrozen parameter report;
- learning-rate and compute-budget rationale;
- controlled comparison table;
- class-wise or example-level error analysis;
- limitation note covering domain shift or data size.

## Gate

The student passes only when the preferred strategy is supported by a valid comparison. A higher score from a different split, metric, epoch budget, or validation transform is not acceptable evidence.