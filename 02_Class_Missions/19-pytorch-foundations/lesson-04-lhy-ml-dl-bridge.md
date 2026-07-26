# Lesson 04 — LHY-ML Full Video: Deep Learning to PyTorch Bridge

**Duration:** 75 minutes, or two 75-minute sessions if the assigned Bohrium video is longer than 45 minutes.

**Official-aligned resource:** 台湾大学李宏毅《机器学习》内容精选版

**Bohrium link:** https://www.bohrium.com/courses/7890895681/content?file=2496

**Placement:** This lesson belongs after basic PyTorch foundations when students need to connect conceptual deep-learning explanations to tensors, modules, losses, optimizers, and training loops.

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–40 min | Skill Warm-Up | Watch the full assigned Bohrium video and complete deep-learning guided notes. If the video exceeds 45 minutes, split into two sessions. |
| 40–47 min | Talk Robin 1 | Explain one concept from the video and where it appears in PyTorch code. |
| 47–53 min | Entry Check | Answer PyTorch readiness questions. |
| 53–61 min | Core Pattern | Convert the video explanation into a PyTorch training-loop pattern. |
| 61–68 min | Guided Practice | Annotate or complete a supported PyTorch training-loop skeleton. |
| 68–72 min | Independent Rebuild | Rebuild the conceptual pipeline without copying the example. |
| 72–75 min | Talk Robin 2 + Evidence | Explain and submit evidence. |

## 1. Skill Warm-Up

Watch the full assigned Bohrium video.

While watching, complete:

```text
Video topic:

Three key terms:
1.
2.
3.

Deep-learning concept explained by the teacher:

Where this appears in PyTorch code:
- tensor / dataset:
- model:
- loss:
- optimizer:
- training loop:

One point I need to test by coding:
```

## 2. Talk Robin 1

Partner discussion:

```text
The video explains ...
In PyTorch, that corresponds to ...
The part I still cannot code independently is ...
```

## 3. Entry Check

Answer individually:

1. What is the input tensor?
2. What does the model output?
3. What loss function would fit the task?
4. What does the optimizer update?
5. What must be verified before trusting training results?

## 4. Core Pattern

Teacher extracts the PyTorch bridge pattern:

```text
Tensor/DataLoader → nn.Module → Forward Pass → Loss → Backward Pass → Optimizer Step → Validation
```

## 5. Guided Practice

Annotate a training loop:

```text
Where is the forward pass?
Where is the loss computed?
Where are gradients cleared?
Where is backpropagation called?
Where are parameters updated?
Where is validation separated from training?
```

## 6. Independent Rebuild

Rebuild the training-loop pattern using a new task.

```text
Task:
Input tensor shape:
Model output:
Loss:
Optimizer:
Training evidence:
Validation evidence:
Possible failure mode:
```

## 7. Talk Robin 2 + Evidence

Submit:

1. completed video notes;
2. Entry Check answers;
3. annotated PyTorch pattern;
4. Independent Rebuild pattern;
5. one explanation of how the video connects to real code.
