# Deep Learning Specialization Selected Content Map

This file clarifies how the **Deep Learning Specialization (DLS)** is used in this NOAI / IOAI preparation curriculum.

DLS is **not** a full five-course route in this repository. The curriculum remains official NOAI / IOAI first, with BML15, LHY-ML, Hands-On Machine Learning, sklearn, the DeepLearning.AI PyTorch for Deep Learning Professional Certificate, PyTorch official tutorials, Hugging Face, Qwen, and official task repositories as the main spine. DLS is used selectively when students need clearer deep-learning concepts before implementation.

## Placement Rule

Do **not** ask students to complete the full Deep Learning Specialization during this course.

Use DLS selectively when:

1. the NOAI / IOAI syllabus item requires deeper neural-network understanding;
2. the lesson needs a clearer explanation of optimisation, CNNs, or sequence models;
3. students need conceptual preparation before a PyTorch implementation lesson;
4. advanced students need enrichment beyond BML15 / LHY-ML.

A DLS resource is not evidence. Students must still submit guided notes, checks, practice, independent rebuild, and explanation.

## Summary: How Much DLS Is Used

| DLS course | Repo use level | Estimated mainline lesson use | Main repo placement |
|---|---:|---:|---|
| Course 1 — Neural Networks and Deep Learning | Optional / mostly replaced | 0–2 selected lessons | `12-neural-network-foundations/`; LHY-ML and 3B1B remain preferred for first intuition |
| Course 2 — Improving Deep Neural Networks | Selected | 2–3 lessons | `10-generalization-regularization/`, `13-backprop-optimization/`, `19-pytorch-foundations/` |
| Course 3 — Structuring Machine Learning Projects | Light optional support | 1–2 lessons | `18-sklearn-workflow/`, `24-round-2-project-training/`, `25-past-paper-reproduction/`, `26-mock-contests/` |
| Course 4 — Convolutional Neural Networks | Selected | 3–4 lessons | `14-cnn-foundations/`, `20-computer-vision/` |
| Course 5 — Sequence Models | Selected / partial | 1–2 lessons | `21-nlp-sequence-models/`; transformers and LLMs use Hugging Face and Qwen resources |

Approximate total DLS-supported use: **7–11 lessons**, mostly selected or optional.

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

Preferred first resources remain LHY-ML and 3B1B. Implementation follows later through the DeepLearning.AI PyTorch certificate and PyTorch official tutorials.

## Course 2 — Improving Deep Neural Networks

**Status:** selected support resource.

Use selected content for:

- train / validation / test thinking;
- bias / variance diagnosis;
- regularisation;
- initialisation;
- batch normalisation;
- optimisation algorithms;
- Adam / AdamW comparison.

Repo placements:

- `10-generalization-regularization/`
- `13-backprop-optimization/lesson-03.md`
- `13-backprop-optimization/lesson-04-training-cycle.md`
- `13-backprop-optimization/lesson-05-convergence-and-learning-rate.md`
- `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md`

Concept explanation may come from DLS; implementation should use the DeepLearning.AI PyTorch certificate plus PyTorch official tutorials.

## Course 3 — Structuring Machine Learning Projects

**Status:** light optional support.

Use only for:

- error analysis;
- metric choice;
- dev/test split reasoning;
- iteration strategy;
- avoiding leaderboard overfitting.

Repo placements:

- `18-sklearn-workflow/lesson-05-model-selection-validation-memo.md`
- `24-round-2-project-training/lesson-04-task-reading-problem-simplification.md`
- `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md`
- `25-past-paper-reproduction/lesson-04-postmortem-and-transfer.md`
- `26-mock-contests/lesson-05-final-readiness-conference.md`

## Course 4 — Convolutional Neural Networks

**Status:** selected conceptual support.

Use selected content for:

- convolution operation intuition;
- padding, stride, pooling;
- CNN architecture;
- transfer learning;
- image error analysis.

Repo placements:

- `14-cnn-foundations/lesson-01.md`
- `14-cnn-foundations/lesson-02.md`
- `14-cnn-foundations/lesson-04-cnn-shape-calculations.md`
- `14-cnn-foundations/lesson-05-cnn-design-choices.md`
- `20-computer-vision/lesson-05-transfer-learning-finetuning.md`

DLS explains the concepts; the DeepLearning.AI PyTorch certificate Course 2 and PyTorch/torchvision tutorials provide the implementation route.

## Course 5 — Sequence Models

**Status:** selected / partial.

Use selected content for:

- RNN / LSTM intuition;
- sequence length and hidden-state reasoning;
- text sequence modelling.

Repo placements:

- `21-nlp-sequence-models/lesson-02.md`
- `21-nlp-sequence-models/lesson-05-sequence-shapes-and-debugging.md`
- `21-nlp-sequence-models/lesson-06-nlp-round2-reproduction.md`

Do not use DLS Course 5 as the main transformer or LLM resource. Use Hugging Face and Qwen for transformer classification, LLM, and multimodal workflows.

## Teacher Decision Rule

Use DLS to clarify a specific concept. Do not turn it into a second full curriculum.

Recommended route:

**NOAI / IOAI official tasks → BML15 / LHY-ML → Andrew Ng Machine Learning Specialization selected content → Hands-On ML selected chapters → DLS selected concepts → DeepLearning.AI PyTorch for Deep Learning Professional Certificate selected modules → PyTorch official tutorials → Hugging Face / Qwen → competition tasks.**
