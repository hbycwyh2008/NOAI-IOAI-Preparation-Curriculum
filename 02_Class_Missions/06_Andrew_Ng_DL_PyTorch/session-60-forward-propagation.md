# Mission 12.2 — Multilayer Networks and Forward Propagation

**Duration:** 75 minutes  
**Pre-class required viewing:** 28 minutes

## Pre-Class Required Resource

**Course 2 — Advanced Learning Algorithms**, part of the **Machine Learning Specialization**  
Coursera: https://www.coursera.org/learn/advanced-learning-algorithms  
Week 1 — Neural Networks

| Video | Duration | Student action |
|---|---:|---|
| Neural Network Layer | 10 min | identify inputs, weights, bias, activation, and output of one layer |
| More Complex Neural Networks | 8 min | distinguish input, hidden, and output layers |
| Inference: Making Predictions (Forward Propagation) | 5 min | trace information through the network |
| Forward Propagation in a Single Layer | 5 min | calculate one small layer output |

Optional extension: General Implementation of Forward Propagation — 8 min.

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Calculate one neuron output and label the tensor shapes. |
| 8–15 min | Talk Robin 1 | Explain how the output of one layer becomes the input of the next. |
| 15–22 min | Entry Check | Identify layers, parameters, and activations in a small diagram. |
| 22–35 min | Core Pattern | Teacher models input → affine transformation → activation → next layer → output. |
| 35–53 min | Guided Practice | Calculate a two-layer forward pass with teacher support. |
| 53–67 min | Independent Rebuild | Calculate and diagram a new two-layer network. |
| 67–75 min | Talk Robin 2 + Evidence | Explain one complete forward path and submit evidence. |

## Learning Targets

- distinguish input, hidden, and output layers;
- calculate a small forward pass;
- track vector and matrix shapes;
- explain why nonlinear activations matter;
- match sigmoid, rectified-linear-unit, and linear outputs to tasks.

## Core Pattern

```text
Input vector → weighted sum + bias → activation → hidden representation → output layer → prediction
```

## Guided Practice

Students calculate a two-layer network and complete a table:

| Item | Shape | Numerical result or role |
|---|---|---|
| input |  |  |
| first-layer weights |  |  |
| first-layer bias |  |  |
| hidden activation |  |  |
| output-layer weights |  |  |
| final output |  |  |

## Independent Rebuild

Calculate and diagram a new two-layer network, including tensor shapes, activation choices, output interpretation, and one likely shape error.

## Talk Robin 2 + Evidence

Submit the pre-class viewing note, guided forward-pass table, independent network diagram and calculation, and one explanation of why removing every nonlinear activation changes what the network can represent.
