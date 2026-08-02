# Phase 6 Session Launcher

**Sessions:** 59–70  
**Concept spine:** Andrew Ng Deep Learning Specialization  
**Implementation spine:** PyTorch

Open the exact session link below. Do not browse the lesson-bank modules manually.

| Session | Focus | Open this lesson | Required evidence |
|---:|---|---|---|
| 59 | deep-learning map, tensor shapes, devices, and baseline discipline | [Tensors, devices, and shapes](../_Lesson_Library/19-pytorch-foundations/lesson-01.md) | tensor/shape ledger, device-safe code, baseline statement |
| 60 | forward propagation, `nn.Module`, Dataset/DataLoader, and autograd setup | [Dataset, DataLoader, nn.Module, and autograd](../_Lesson_Library/19-pytorch-foundations/lesson-02.md) and [forward propagation](../_Lesson_Library/12-neural-network-foundations/lesson-02.md) | forward-pass trace and module/data pipeline |
| 61 | backpropagation, autograd, and complete training loop | [Training cycle](../_Lesson_Library/13-backprop-optimization/lesson-04-training-cycle.md) and [training/validation loops](../_Lesson_Library/19-pytorch-foundations/lesson-03.md) | full loop, gradient note, checkpoint, validation record |
| 62 | initialisation, optimisers, learning rate, BatchNorm, Dropout, and regularisation | [Optimisers](../_Lesson_Library/13-backprop-optimization/lesson-03.md) and [convergence/learning rate](../_Lesson_Library/13-backprop-optimization/lesson-05-convergence-and-learning-rate.md) | curve diagnosis and controlled optimiser/regularisation decision |
| 63 | CNN concepts, kernels, padding, stride, pooling, and shapes | [CNN shapes](../_Lesson_Library/14-cnn-foundations/lesson-02.md) and [output-size calculations](../_Lesson_Library/14-cnn-foundations/lesson-04-cnn-shape-calculations.md) | layer-role explanation and shape table |
| 64 | PyTorch image classification | [CNN baseline, augmentation, and transfer](../_Lesson_Library/20-computer-vision/lesson-02.md) | image baseline, validation result, and error table |
| 65 | transfer learning, fine-tuning, and augmentation | [Transfer learning and fine-tuning](../_Lesson_Library/20-computer-vision/lesson-05-transfer-learning-finetuning.md) | freeze/unfreeze decision, augmentation memo, comparison |
| 66 | RNN and LSTM sequence modelling | [RNN and LSTM](../_Lesson_Library/21-nlp-sequence-models/lesson-02.md) | sequence-shape ledger and recurrent-model explanation |
| 67 | PyTorch text or time-series classification | [NLP Round 2 reproduction](../_Lesson_Library/21-nlp-sequence-models/lesson-06-nlp-round2-reproduction.md) | simple baseline, sequence model, metric, error analysis |
| 68 | attention and Transformer intuition | [Attention and Transformers](session-68-attention-transformers.md) | hand attention calculation, shape ledger, PyTorch trace, limitation |
| 69 | audio or multimodal task | [Mel-spectrogram image bridge](../_Lesson_Library/22-audio-speech/lesson-03-mel-spectrogram-image-bridge.md) or [multimodal collaboration evidence](../_Lesson_Library/23-llm-generative-ai/lesson-05-multimodal-human-ai-collaboration.md) | modality baseline, representation explanation, leakage/error note |
| 70 | deep-learning capstone: simple baseline versus deep model | [PyTorch mini-project and fresh-runtime validation](../_Lesson_Library/19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md) plus [domain error analysis](../_Lesson_Library/20-computer-vision/lesson-06-image-error-analysis-submission.md) | baseline/deep comparison, costs, errors, checkpoint, fresh run, model card |

## Phase Gate

Students write a fresh PyTorch training/validation loop, reason about tensor shapes and dtypes, diagnose overfitting or optimisation failure, save the best checkpoint, and compare a deep model with a trustworthy simple baseline.