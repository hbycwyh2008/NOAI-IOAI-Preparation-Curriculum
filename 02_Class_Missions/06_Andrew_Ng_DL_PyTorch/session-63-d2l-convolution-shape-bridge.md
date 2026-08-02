# Session 63 — D2L Convolution and Shape-Reasoning Bridge

**Placement:** embedded inside Session 63; this packet does not add another scheduled session.  
**Role:** connect convolution equations and image structure to correct PyTorch tensor shapes.

## Assigned D2L Sections

- [6.1 From Fully Connected Layers to Convolutions](https://zh.d2l.ai/chapter_convolutional-neural-networks/why-conv.html)
- [6.2 Image Convolution](https://zh.d2l.ai/chapter_convolutional-neural-networks/conv-layer.html)
- [6.3 Padding and Stride](https://zh.d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html)
- [6.4 Multiple Input and Output Channels](https://zh.d2l.ai/chapter_convolutional-neural-networks/channels.html)
- [6.5 Pooling](https://zh.d2l.ai/chapter_convolutional-neural-networks/pooling.html)
- [6.6 LeNet](https://zh.d2l.ai/chapter_convolutional-neural-networks/lenet.html)

Use the PyTorch tab. The teacher may split the reading between Sessions 63 and 64, but all shape and convolution evidence belongs to Session 63.

## Required Mastery

Students must be able to:

1. explain local connectivity and parameter sharing;
2. compute a small two-dimensional cross-correlation by hand;
3. calculate output height and width from kernel, stride, padding, and dilation settings;
4. track batch, channel, height, and width dimensions;
5. explain how multiple input and output channels affect kernel shape;
6. distinguish convolution, activation, pooling, flattening, and classification-head roles;
7. verify calculations with PyTorch instead of using PyTorch as a substitute for calculation.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read D2L 6.1–6.3 and annotate one convolution diagram. |
| Entry Check | Calculate one output element and one output spatial size without code. |
| Core Pattern | Trace `N × C × H × W` through convolution, activation, pooling, flattening, and a linear layer. |
| Guided Practice | Complete a multi-channel shape ledger and verify it with `nn.Conv2d`. |
| Independent Rebuild | Implement a tiny CNN from a supplied architecture card, then repair one channel or flatten-size error. |

## Shape Rule

For each convolution or pooling layer, record:

```text
input N × C_in × H_in × W_in
→ kernel / stride / padding / dilation
→ output N × C_out × H_out × W_out
→ parameter count
```

## Independent Task

1. calculate a 2D cross-correlation for a small matrix and kernel;
2. calculate every layer shape in a tiny CNN;
3. calculate the convolutional parameter count;
4. implement the network in PyTorch;
5. compare calculated and observed shapes with assertions;
6. intentionally use an incorrect input-channel or flatten dimension;
7. diagnose and repair the failure from the error and shape ledger.

## Required Evidence

- hand convolution calculation;
- complete CNN shape ledger;
- parameter-count calculation;
- PyTorch assertions that confirm the ledger;
- one repaired channel or flattening error;
- explanation of why a CNN encodes a more suitable inductive bias for images than a fully connected network.

## Gate

The student passes only when all shapes and parameter counts are predicted before execution and the implemented model matches those predictions.