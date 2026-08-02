# Phase 6 Session Launcher

**Sessions:** 59–70  
**Concept spine:** Andrew Ng Deep Learning Specialization  
**Concept-to-code bridge:** selected *Dive into Deep Learning* sections  
**Implementation spine:** PyTorch

Open the exact session link below. Do not browse the lesson-bank modules or the whole D2L book manually.

| Session | Focus | Open this lesson | Required evidence |
|---:|---|---|---|
| 59 | deep-learning map, tensor shapes, devices, and baseline discipline | [Tensors, devices, and shapes](session-59-tensors-devices-and-shapes.md) | tensor/shape ledger, device-safe code, baseline statement |
| 60 | forward propagation, `nn.Module`, Dataset/DataLoader, and autograd setup | [Dataset, DataLoader, nn.Module, and autograd](session-60-dataset-dataloader-nn-module-and-autograd.md) and [forward propagation](session-60-forward-propagation.md) | forward-pass trace and module/data pipeline |
| 61 | backpropagation, autograd, and complete training loop | [Training cycle](session-61-training-cycle.md), [training/validation loops](session-61-training-validation-loops.md), and [D2L autograd/backpropagation bridge](session-61-d2l-autograd-backprop-bridge.md) | full loop, gradient note, checkpoint, validation record, independent autograd rebuild |
| 62 | initialisation, optimisers, learning rate, BatchNorm, Dropout, and regularisation | [Optimisers](session-62-optimisers.md), [convergence/learning rate](session-62-convergence-learning-rate.md), and [D2L regularisation/optimisation bridge](session-62-d2l-regularisation-optimisation-bridge.md) | curve diagnosis, controlled intervention, and justified optimiser/regularisation decision |
| 63 | CNN concepts, kernels, padding, stride, pooling, and shapes | [CNN shapes](session-63-cnn-shapes.md), [output-size calculations](session-63-output-size-calculations.md), and [D2L convolution/shape bridge](session-63-d2l-convolution-shape-bridge.md) | hand convolution, layer-role explanation, shape table, parameter count, PyTorch verification |
| 64 | PyTorch image classification | [CNN baseline, augmentation, and transfer](session-64-cnn-baseline-augmentation-and-transfer.md) | image baseline, validation result, and error table |
| 65 | transfer learning, fine-tuning, and augmentation | [Transfer learning and fine-tuning](session-65-transfer-learning-and-fine-tuning.md) and [D2L augmentation/fine-tuning bridge](session-65-d2l-fine-tuning-bridge.md) | freeze/unfreeze decision, transform audit, controlled comparison, augmentation memo |
| 66 | RNN and LSTM sequence modelling | [RNN and LSTM](session-66-rnn-and-lstm.md) and [D2L RNN/LSTM bridge](session-66-d2l-rnn-lstm-bridge.md) | recurrent calculation, sequence-shape ledger, baseline comparison, gate explanation |
| 67 | PyTorch text or time-series classification | [NLP Round 2 reproduction](session-67-nlp-round-2-reproduction.md) | simple baseline, sequence model, metric, error analysis |
| 68 | attention and Transformer intuition | [Attention and Transformers](session-68-attention-transformers.md) and [D2L attention/Transformer bridge](session-68-d2l-attention-transformer-bridge.md) | hand attention calculation, Q/K/V shape ledger, masked PyTorch trace, limitation |
| 69 | audio or multimodal task | [Mel-spectrogram image bridge](session-69-mel-spectrogram-image-bridge.md) or [multimodal collaboration evidence](session-69-multimodal-collaboration-evidence.md) | modality baseline, representation explanation, leakage/error note |
| 70 | deep-learning capstone: simple baseline versus deep model | [PyTorch mini-project and fresh-runtime validation](session-70-pytorch-mini-project-and-fresh-runtime-validation.md) plus [domain error analysis](session-70-domain-error-analysis.md) | baseline/deep comparison, costs, errors, checkpoint, fresh run, model card |

## Required Phase Resources

- [D2L selective reading map](../../05_Resources/D2L_Selective_Reading_Map.md)
- Official PyTorch tutorials and documentation assigned in each packet
- Current official NOAI / IOAI rules and task documents

## D2L Boundary

D2L is embedded only where it closes a concept-to-code gap. Students use the PyTorch tab, complete the selected fragment, close the source, and independently rebuild the essential mechanism. Copying a complete D2L notebook is not mastery evidence and does not replace the Session gate.

## Phase Gate

Students write a fresh PyTorch training/validation loop, reason about tensor shapes and dtypes, diagnose overfitting or optimisation failure, save the best checkpoint, and compare a deep model with a trustworthy simple baseline. Students must also complete the required D2L bridges for Sessions 61, 62, 63, 65, 66, and 68.