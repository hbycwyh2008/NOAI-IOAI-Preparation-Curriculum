# Session 61 — D2L Autograd and Backpropagation Bridge

**Placement:** embedded inside Session 61; this packet does not add another scheduled session.  
**Role:** connect the Andrew Ng backpropagation explanation to an independently rebuilt PyTorch training cycle.

## Assigned D2L Sections

1. [2.5 Automatic Differentiation](https://zh.d2l.ai/chapter_preliminaries/autograd.html)
2. [4.7 Forward Propagation, Backpropagation, and Computational Graphs](https://zh.d2l.ai/chapter_multilayer-perceptrons/backprop.html)

Use the PyTorch tab. Read only the assigned sections and the teacher-selected code cells.

## Required Mastery

Students must be able to:

1. distinguish parameters, activations, loss, gradients, and optimiser state;
2. explain why a scalar loss is differentiated with respect to trainable parameters;
3. trace a small computational graph from input to loss;
4. inspect `.grad` after `backward()` and explain gradient accumulation;
5. place `zero_grad`, forward, loss, backward, and optimiser step in the correct order;
6. identify where validation differs from training;
7. rebuild a minimal loop without copying D2L or PyTorch tutorial code.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read D2L 2.5 and the conceptual diagrams in 4.7; write one question and one gradient misconception. |
| Core Pattern | Trace `x → linear → activation → prediction → loss` and identify the values cached for backpropagation. |
| Guided Practice | Run a two-parameter example, predict gradient signs, call `backward()`, and compare the prediction with `.grad`. |
| Failure Test | Omit `zero_grad()` for two iterations and explain the observed accumulation. |
| Independent Rebuild | Close D2L and implement one epoch of a tiny classifier with explicit train and validation phases. |

## Core Pattern

```text
clear old gradients
→ forward pass
→ scalar loss
→ backward pass
→ inspect or clip gradients when justified
→ optimiser step
→ record evidence
```

## Independent Task

From a blank file or notebook cell:

1. create a deterministic synthetic binary-classification dataset;
2. define a one-layer or two-layer `nn.Module`;
3. run one batch manually and record every tensor shape;
4. predict the sign of at least one gradient before calling `backward()`;
5. complete three training iterations;
6. run validation under `torch.no_grad()`;
7. intentionally produce one incorrect loop and repair it.

## Required Evidence

- annotated computational graph;
- parameter/gradient table before and after `backward()`;
- correct training-cycle order;
- gradient-accumulation failure and correction;
- independently rebuilt code;
- fresh-runtime output;
- oral or written explanation of why autograd computes derivatives but does not decide the model, loss, validation protocol, or learning rate.

## Gate

The student passes only when the loop runs from a fresh process and the student can explain, without executing code, what each gradient represents and why the update order is correct.