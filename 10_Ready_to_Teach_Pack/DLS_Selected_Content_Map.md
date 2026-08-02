# Deep Learning Specialization Selected Content Map

This file clarifies how the **Deep Learning Specialization** is used in this NOAI / IOAI preparation curriculum.

The Deep Learning Specialization is **not** a full five-course route in this repository. The curriculum remains official NOAI / IOAI first, with 北京市十一学校《中学机器学习十五讲》、台湾大学李宏毅《机器学习》内容精选版、Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow、the scikit-learn User Guide、the DeepLearning.AI PyTorch for Deep Learning Professional Certificate、PyTorch official tutorials、Hugging Face、Qwen, and official competition tasks as the main route. The Deep Learning Specialization is used selectively when students need clearer deep-learning concepts before implementation.

## Placement Rule

Do **not** ask students to complete the full Deep Learning Specialization during this course.

Use selected content when:

1. the official syllabus item requires deeper neural-network understanding;
2. a lesson needs a clearer explanation of optimisation, convolutional neural networks, or sequence models;
3. students need conceptual preparation before a PyTorch implementation lesson;
4. advanced students need enrichment beyond 北京市十一学校《中学机器学习十五讲》 or 台湾大学李宏毅《机器学习》内容精选版;
5. competition-sprint students need a diagnosis-first tuning framework.

A video is not evidence. Students must still submit guided notes, checks, practice, an independent rebuild, and an explanation.

## Summary

| Deep Learning Specialization course | Use level | Estimated selected lesson use | Main placement |
|---|---:|---:|---|
| Course 1 — Neural Networks and Deep Learning | Optional / mostly replaced | 0–2 lessons | `12-neural-network-foundations/`; 台湾大学李宏毅《机器学习》内容精选版 and 3Blue1Brown Neural Networks remain preferred for first intuition |
| Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization | Selected | 3–5 lessons | `10-generalization-regularization/`, `13-backprop-optimization/`, `19-pytorch-foundations/`, `28-competition-sprint-task-data-tuning/lesson-06-deep-learning-tuning.md` |
| Course 3 — Structuring Machine Learning Projects | Light optional support | 1–2 lessons | `18-sklearn-workflow/`, `24-round-2-project-training/`, `25-past-paper-reproduction/`, `26-mock-contests/` |
| Course 4 — Convolutional Neural Networks | Selected | 3–4 lessons | `14-cnn-foundations/`, `20-computer-vision/` |
| Course 5 — Sequence Models | Selected / partial | 1–2 lessons | `21-nlp-sequence-models/`; Transformers and large language models use Hugging Face and Qwen resources |

Approximate supported use: **8–13 selected lessons**, including the competition-sprint tuning lesson.

## Course 1 — Neural Networks and Deep Learning

**Status:** optional conceptual support.

Use only when students need extra explanation of:

- neuron and shallow-network intuition;
- forward propagation;
- basic backpropagation intuition;
- the difference between parameters, activations, outputs, and losses.

Repo placements:

- `12-neural-network-foundations/lesson-01.md`
- `12-neural-network-foundations/lesson-02.md`
- `12-neural-network-foundations/lesson-05-forward-pass-trace.md`

Preferred first resources remain 台湾大学李宏毅《机器学习》内容精选版 and 3Blue1Brown Neural Networks. Implementation follows later through the DeepLearning.AI PyTorch for Deep Learning Professional Certificate and PyTorch official tutorials.

## Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization

**Status:** selected conceptual and competition-sprint support.

Use selected content for:

- train / validation / test thinking;
- bias / variance diagnosis;
- regularisation;
- initialisation;
- batch normalisation;
- optimisation algorithms;
- Adam and learning-rate decay;
- hyperparameter search scales and process.

Repo placements:

- `10-generalization-regularization/`
- `13-backprop-optimization/lesson-03.md`
- `13-backprop-optimization/lesson-04-training-cycle.md`
- `13-backprop-optimization/lesson-05-convergence-and-learning-rate.md`
- `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md`
- `28-competition-sprint-task-data-tuning/lesson-06-deep-learning-tuning.md`

The exact sprint video package and timing are defined in `02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md`.

Concept explanation may come from this course; implementation should use the DeepLearning.AI PyTorch for Deep Learning Professional Certificate plus PyTorch official tutorials.

## Course 3 — Structuring Machine Learning Projects

**Status:** light optional support.

Use only for:

- error analysis;
- metric choice;
- development/test split reasoning;
- iteration strategy;
- avoiding leaderboard overfitting.

Repo placements:

- `18-sklearn-workflow/lesson-05-model-selection-validation-memo.md`
- `24-round-2-project-training/lesson-04-task-reading-problem-simplification.md`
- `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md`
- `25-past-paper-reproduction/lesson-04-cross-task-postmortem-patterns.md`
- `26-mock-contests/lesson-05-mock-correction-retake-readiness.md`

## Course 4 — Convolutional Neural Networks

**Status:** selected conceptual support.

Use selected content for:

- convolution operation intuition;
- padding, stride, and pooling;
- convolutional-neural-network architecture;
- transfer learning;
- image error analysis.

Repo placements:

- `14-cnn-foundations/lesson-01.md`
- `14-cnn-foundations/lesson-02.md`
- `14-cnn-foundations/lesson-04-cnn-shape-calculations.md`
- `14-cnn-foundations/lesson-05-cnn-design-choices.md`
- `20-computer-vision/lesson-05-transfer-learning-finetuning.md`

Course 4 explains the concepts; Course 2 — PyTorch: Techniques and Ecosystem Tools plus PyTorch and torchvision official tutorials provide the implementation route.

## Course 5 — Sequence Models

**Status:** selected / partial.

Use selected content for:

- recurrent-neural-network and long-short-term-memory intuition;
- sequence length and hidden-state reasoning;
- text sequence modelling.

Repo placements:

- `21-nlp-sequence-models/lesson-02.md`
- `21-nlp-sequence-models/lesson-05-sequence-shapes-and-debugging.md`
- `21-nlp-sequence-models/lesson-06-nlp-round2-reproduction.md`

Do not use Course 5 as the main Transformer or large-language-model resource. Use Hugging Face and Qwen for Transformer classification, large language models, and multimodal workflows.

## Teacher Decision Rule

Use the Deep Learning Specialization to clarify a specific concept. Do not turn it into a second full curriculum.

Recommended route:

**Official NOAI / IOAI tasks → 北京市十一学校《中学机器学习十五讲》 / 台湾大学李宏毅《机器学习》内容精选版 → selected Machine Learning Specialization content → selected Hands-On Machine Learning chapters → selected Deep Learning Specialization concepts → selected DeepLearning.AI PyTorch Professional Certificate modules → PyTorch official tutorials → Hugging Face / Qwen → competition tasks.**