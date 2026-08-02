# 19 — PyTorch Foundations

This module prepares students for Round 2 deep-learning tasks. It includes tensor/device reasoning, Dataset/DataLoader, nn.Module, autograd, training loops, validation, checkpoints, and debugging.

## Primary Structured Resource

**DeepLearning.AI PyTorch for Deep Learning Professional Certificate on Coursera**  
https://www.coursera.org/professional-certificates/pytorch-for-deep-learning

Use **Course 1 — PyTorch: Fundamentals** as the main structured resource for this module:  
https://www.coursera.org/learn/pytorch-fundamentals

Use PyTorch official tutorials to verify current APIs:  
https://docs.pytorch.org/tutorials/

Students do not complete the full professional certificate during this module. The teacher assigns the exact Course 1 module and lesson needed for each mission.

## Lessons

- [Lesson 01 — Tensors, devices, shapes, and GPU movement](lesson-01.md) — Course 1 — PyTorch: Fundamentals: tensors, tensor mathematics, broadcasting, and device reasoning
- [Lesson 02 — Dataset, DataLoader, nn.Module, and autograd](lesson-02.md) — Course 1 — PyTorch: Fundamentals: datasets, dataloaders, and neural-network building blocks
- [Lesson 03 — Training/validation loops, checkpoints, and mixed precision](lesson-03.md) — Course 1 — PyTorch: Fundamentals: complete training pipeline; PyTorch official tutorials for automatic mixed precision and checkpoints
- [Lesson 04 — 台湾大学李宏毅《机器学习》内容精选版完整视频：Deep Learning to PyTorch Bridge](lesson-04-lhy-ml-dl-bridge.md) — conceptual bridge before implementation
- [Lesson 05 — Loss functions, optimiser step, and gradient-debug checklist](lesson-05-loss-optimizer-gradient-debug.md) — Course 1 — PyTorch: Fundamentals: loss, optimisation, and model learning
- [Lesson 06 — Dataset/DataLoader rebuild and device-safe training loop](lesson-06-dataloader-device-safe-loop.md) — Course 1 — PyTorch: Fundamentals independent rebuild
- [Lesson 07 — PyTorch Round 2 mini-project and fresh-runtime validation](lesson-07-pytorch-mini-project-validation.md) — Course 1 — PyTorch: Fundamentals integration plus competition validation

## Resource Boundary

- Deep Learning Specialization explains selected deep-learning concepts.
- Course 1 — PyTorch: Fundamentals provides the main implementation sequence.
- Course 2 — PyTorch: Techniques and Ecosystem Tools supports later computer-vision, natural-language-processing, transfer-learning, and tuning lessons.
- Course 3 — PyTorch: Advanced Architectures and Deployment is an optional advanced architecture/deployment extension.
- PyTorch official tutorials remain the source of truth for current APIs.

## Official-Aligned Video Placement

Use Lesson 04 when the teacher wants students to watch the full 台湾大学李宏毅《机器学习》内容精选版 Bohrium video and connect conceptual machine-learning and deep-learning explanations to tensors, nn.Module, forward pass, loss, backpropagation, optimiser step, and validation.

## Minimum Evidence

Students should submit a tensor-shape ledger, device-safe code, custom Dataset/DataLoader, train/validate loop, gradient-debug note, checkpoint, and fresh-runtime validation record.