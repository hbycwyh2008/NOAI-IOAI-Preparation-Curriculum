# Dive into Deep Learning — Selective Reading Map

This map places selected sections of *Dive into Deep Learning* (D2L) inside Phase 6. D2L is a **concept-to-code bridge** between the Andrew Ng Deep Learning Specialization and the official PyTorch tutorials. It is not a new phase, a replacement for PyTorch documentation, or an instruction to complete the whole book.

## Source Boundary

- Use the Chinese online edition: <https://zh.d2l.ai/>.
- Use the **PyTorch** tab in every executable section.
- Teachers assign only the sections listed below.
- Current official NOAI / IOAI rules, allowed libraries, runtime, and submission constraints override all book examples.
- Students may inspect D2L code during guided work, but the required independent rebuild must be completed without copying a full solution.

## Session Placement

| Session | D2L placement | Status | Required capability and evidence |
|---:|---|---|---|
| 59 | [2.1 Data Manipulation](https://zh.d2l.ai/chapter_preliminaries/ndarray.html); [5.6 GPUs](https://zh.d2l.ai/chapter_deep-learning-computation/use-gpu.html) | Optional reference | tensor operations, shape/device ledger, CPU-safe fallback |
| 60 | [5.1 Layers and Blocks](https://zh.d2l.ai/chapter_deep-learning-computation/model-construction.html); [5.2 Parameter Management](https://zh.d2l.ai/chapter_deep-learning-computation/parameters.html); [5.4 Custom Layers](https://zh.d2l.ai/chapter_deep-learning-computation/custom-layer.html) | Optional reference | explain `nn.Module`, parameters, forward flow, and one custom component |
| 61 | [2.5 Automatic Differentiation](https://zh.d2l.ai/chapter_preliminaries/autograd.html); [4.7 Forward Propagation, Backpropagation, and Computational Graphs](https://zh.d2l.ai/chapter_multilayer-perceptrons/backprop.html) | **Required bridge** | hand trace, gradient inspection, correct zero/backward/step order, fresh rebuild |
| 62 | [4.5 Weight Decay](https://zh.d2l.ai/chapter_multilayer-perceptrons/weight-decay.html); [4.6 Dropout](https://zh.d2l.ai/chapter_multilayer-perceptrons/dropout.html); [4.8 Numerical Stability and Initialisation](https://zh.d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html); [7.5 Batch Normalisation](https://zh.d2l.ai/chapter_convolutional-modern/batch-norm.html) | **Required bridge** | controlled regularisation or initialisation comparison and curve diagnosis |
| 62 | [11.1 Optimisation and Deep Learning](https://zh.d2l.ai/chapter_optimization/optimization-intro.html); [11.6 Momentum](https://zh.d2l.ai/chapter_optimization/momentum.html); [11.10 Adam](https://zh.d2l.ai/chapter_optimization/adam.html); [11.11 Learning-Rate Scheduling](https://zh.d2l.ai/chapter_optimization/lr-scheduler.html) | Optional extension | justify an optimiser and learning-rate decision from evidence |
| 63 | [6.1 From Fully Connected Layers to Convolutions](https://zh.d2l.ai/chapter_convolutional-neural-networks/why-conv.html); [6.2 Image Convolution](https://zh.d2l.ai/chapter_convolutional-neural-networks/conv-layer.html); [6.3 Padding and Stride](https://zh.d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html); [6.4 Multiple Input and Output Channels](https://zh.d2l.ai/chapter_convolutional-neural-networks/channels.html); [6.5 Pooling](https://zh.d2l.ai/chapter_convolutional-neural-networks/pooling.html); [6.6 LeNet](https://zh.d2l.ai/chapter_convolutional-neural-networks/lenet.html) | **Required bridge** | manual convolution, channel/shape ledger, PyTorch verification, tiny CNN rebuild |
| 64 | [7.6 ResNet](https://zh.d2l.ai/chapter_convolutional-modern/resnet.html) | Optional reference | identify a residual connection and compare a simple CNN with a stronger image backbone |
| 65 | [13.1 Image Augmentation](https://zh.d2l.ai/chapter_computer-vision/image-augmentation.html); [13.2 Fine-Tuning](https://zh.d2l.ai/chapter_computer-vision/fine-tuning.html) | **Required bridge** | train-only augmentation, replace head, freeze/unfreeze plan, controlled comparison |
| 66 | [8.4 Recurrent Neural Networks](https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn.html); [8.6 Concise RNN Implementation](https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn-concise.html); [8.7 Backpropagation Through Time](https://zh.d2l.ai/chapter_recurrent-neural-networks/bptt.html); [9.2 LSTM](https://zh.d2l.ai/chapter_recurrent-modern/lstm.html) | **Required bridge** | recurrence trace, sequence-shape ledger, gate explanation, sequence classifier rebuild |
| 67 | [8.2 Text Preprocessing](https://zh.d2l.ai/chapter_recurrent-neural-networks/text-preprocessing.html); [9.7 Sequence-to-Sequence Learning](https://zh.d2l.ai/chapter_recurrent-modern/seq2seq.html) | Optional reference | task-specific preprocessing and sequence-model choice; no full seq2seq implementation required |
| 68 | [10.1 Attention Cues](https://zh.d2l.ai/chapter_attention-mechanisms/attention-cues.html); [10.3 Attention Scoring Functions](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html); [10.5 Multi-Head Attention](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html); [10.6 Self-Attention and Positional Encoding](https://zh.d2l.ai/chapter_attention-mechanisms/self-attention-and-positional-encoding.html); [10.7 Transformer](https://zh.d2l.ai/chapter_attention-mechanisms/transformer.html) | **Required bridge** | hand attention calculation, Q/K/V shape ledger, masked PyTorch trace, limitation note |
| 69 | No required D2L section | — | use torchaudio, Hugging Face, OpenCV, Qwen, or task-specific official documentation |
| 70 | Revisit only the sections needed to explain the capstone model | Reference only | independent baseline/deep comparison, checkpoint, error analysis, fresh-runtime evidence |

## Required Bridge Lessons

The following packets embed D2L into existing sessions without increasing the 78-session schedule:

- [Session 61 — Autograd and Backpropagation Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-61-d2l-autograd-backprop-bridge.md)
- [Session 62 — Regularisation, Initialisation, and Optimisation Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-62-d2l-regularisation-optimisation-bridge.md)
- [Session 63 — Convolution and Shape Reasoning Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-63-d2l-convolution-shape-bridge.md)
- [Session 65 — Augmentation and Fine-Tuning Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-65-d2l-fine-tuning-bridge.md)
- [Session 66 — RNN, BPTT, and LSTM Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-66-d2l-rnn-lstm-bridge.md)
- [Session 68 — Attention and Transformer Bridge](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-68-d2l-attention-transformer-bridge.md)

## Instruction Rule

For every required bridge, students must move through this sequence:

```text
read or run the assigned D2L fragment
→ annotate equations, tensor shapes, and assumptions
→ reproduce one small result with teacher support
→ close the source
→ rebuild the essential mechanism in PyTorch
→ test one failure case
→ explain the result and limitation
```

A completed notebook copied from D2L is not mastery evidence. Credit requires an independent rebuild, shape or calculation evidence, an error-and-correction record, and a meaningful Git commit.