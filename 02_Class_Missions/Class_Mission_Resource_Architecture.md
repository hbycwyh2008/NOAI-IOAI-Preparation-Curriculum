# Class Mission Resource Architecture

This document explains the large-scale structure of `02_Class_Missions` and identifies which learning resources support each module.

The curriculum is **not** organised as one complete external course followed from beginning to end. It is organised around the NOAI A/B/C/D skill requirements and NOAI/IOAI task demands. External courses are selected by topic and used only where they strengthen a specific mission.

## Resource Priority

Use resources in this order:

1. **Official NOAI / IOAI rules, syllabus, tasks, and competition environment** — define the required knowledge, allowed tools, task format, and competition workflow.
2. **Official-aligned structured courses** — BML15, LHY-ML, CS50P, Machine Learning Specialization, Deep Learning Specialization, and the DeepLearning.AI PyTorch certificate.
3. **Implementation resources and official documentation** — Hands-On Machine Learning, scikit-learn, PyTorch, NumPy, Pandas, Matplotlib, Hugging Face, Qwen, OpenCV, and torchvision documentation.
4. **Concept-clarification resources** — StatQuest, 3Blue1Brown, Google Machine Learning Crash Course, and selected supplementary explanations.

One ordinary lesson should normally have **one required resource**. The table below lists the available resource set for the module; it does not mean students use every listed resource in every lesson.

## Resource Codes

| Code | Resource | Role in the curriculum |
|---|---|---|
| NOAI | Current official NOAI handbook, syllabus, rules, and task repositories | Round 1/2 scope, rules, task forms, permitted tools |
| IOAI | IOAI official syllabus, rules, academy materials, and task repositories | international-task style, open-ended workflow, multimodal extension |
| BML15 | 北京市十一学校《中学机器学习十五讲》 on Bohrium | official-aligned Round 1 A/B AI and ML concept formation |
| LHY-ML | 李宏毅《机器学习》内容精选版 on Bohrium | ML/DL conceptual bridge for Round 2 C/D |
| CS50P | Harvard CS50's Introduction to Programming with Python on edX | Python syntax, functions, conditionals, loops, exceptions, libraries, files |
| AIF | AI for Everyone on Coursera | optional AI-literacy, capability, ethics, risk, and society support |
| MLS | Machine Learning Specialization on Coursera | selected traditional ML explanations: paradigms, regression, classification, trees, ensembles |
| MLCC | Google Machine Learning Crash Course | concise reinforcement for regression, classification, metrics, generalisation, and data features |
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | practical sklearn workflow, preprocessing, evaluation, model comparison, project habits |
| SQ | StatQuest | statistics, distributions, metrics, trees, ensembles, and model-evaluation clarification |
| 3B1B | 3Blue1Brown Neural Networks | neural-network, gradient-descent, and backpropagation intuition |
| DLS | Deep Learning Specialization on Coursera | selected deep-learning concepts: optimisation, CNNs, project strategy, sequence models |
| DLAI-PT1 | PyTorch: Fundamentals on Coursera | main structured PyTorch foundation course |
| DLAI-PT2 | PyTorch: Techniques and Ecosystem Tools on Coursera | selected transfer learning, TorchVision, Hugging Face, tuning, efficient training |
| DLAI-PT3 | PyTorch: Advanced Architectures and Deployment on Coursera | optional advanced architecture, compression, export, and deployment extension |
| SK | scikit-learn User Guide | current sklearn APIs, pipelines, metrics, CV, tuning |
| PT | PyTorch official tutorials | current PyTorch APIs and implementation verification |
| CV | OpenCV official documentation / courses | classical image preprocessing and structural baselines |
| HF-L | Hugging Face LLM Course and documentation | tokenisation, transformers, text classification, fine-tuning |
| HF-A | Hugging Face Audio Course and documentation | waveforms, spectrograms, audio classification, ASR, TTS |
| QWEN | Current official Qwen documentation | local inference, multimodal processing, quantisation, deployment checks |

---

# Phase 0 — Competition Orientation

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `00-course-overview` | NOAI Round 1/2 structure, baseline thinking, evidence, GitHub/Bohrium workflow | NOAI, IOAI, course evidence guides | official platform/runtime documentation |

# Phase 1 — Python Foundations for Round 1 A

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `01-python-foundations` | values, types, functions, input/output, return values, debugging | CS50P Week 0, Week 3; exact sections and timestamps in `05_Resources/CS50P_edX_Timestamp_Map.md` | Python documentation; teacher code-tracing tasks |
| `02-control-flow-and-data-structures` | conditionals, Boolean logic, loops, strings, lists, dictionaries, tuples, nested structures | CS50P Week 1 and Week 2; exact timestamps in the CS50P map | teacher Round 1 tracing and code-completion sets |
| `03-libraries-sorting-searching` | modules, packages, files, CSV, exceptions, documentation use, search and simple sorting | CS50P Week 4 and Week 6 for libraries/files; teacher-selected CS50 algorithms material for search/sort | Python documentation; NOAI-style paper traces |

**Phase rule:** CS50P is the main Python course. Students use only the assigned week, topic, and timestamp range; they do not browse or complete the whole course during class.

# Phase 2 — AI and Machine-Learning Foundations for Round 1 B

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `04-ai-foundations-and-ethics` | AI schools, Turing Test, capability boundaries, bias, privacy, risk | BML15, official NOAI syllabus | AIF on Coursera as optional support |
| `05-learning-paradigms` | supervised, unsupervised, reinforcement learning; regression/classification/clustering task recognition; training vs inference | BML15 | MLS selected modules; official NOAI scenario questions |
| `06-linear-regression` | prediction, residual, cost, gradient descent, one-feature and multi-feature reasoning | BML15; MLS selected linear-regression modules | MLCC, HML, SK |
| `07-logistic-regression` | sigmoid, probability, threshold, decision boundary, log loss | BML15; MLS selected classification modules | MLCC, HML, SK |
| `08-statistics-probability-distance` | mean, variance, standard deviation, probability, normal distribution, distance, standardisation | SQ | BML15, NumPy documentation, teacher calculation sets |
| `09-model-evaluation` | confusion matrix, accuracy, precision, recall, specificity, F1, ROC/AUC, thresholds, cross-validation | MLCC, SQ | HML, SK, BML15 where aligned |
| `10-generalization-regularization` | underfitting, overfitting, train/validation/test, regularisation, learning curves | BML15; MLS selected modules | MLCC, HML, DLS Course 2 selected explanations |
| `11-trees-and-ensembles` | decision trees, impurity/information gain, bagging, random forest, boosting | HML; MLS selected tree/ensemble modules | SQ, SK |

**Phase rule:** BML15 is the official-aligned Round 1 concept spine. MLS, MLCC, HML, and StatQuest are selected reinforcement resources; they do not replace official NOAI scope.

# Phase 3 — Neural Networks and Deep-Learning Concepts

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `12-neural-network-foundations` | perceptron, neuron, weights, bias, activation, MLP, forward pass, parameter/shape reasoning | LHY-ML, 3B1B | DLS Course 1 selected explanation; BML15 |
| `13-backprop-optimization` | gradient descent, computational graph, backpropagation, learning rate, Adam/AdamW, convergence | LHY-ML, 3B1B | DLS Course 2 selected modules; DLAI-PT1/PT for implementation grounding |
| `14-cnn-foundations` | convolution, filters, padding, stride, pooling, output shapes, activation/loss roles | LHY-ML; DLS Course 4 selected modules | DLAI-PT1/DLAI-PT2, PT/torchvision, 3B1B where useful |

**Phase rule:** DLS is selected conceptual support, not a complete five-course route. PyTorch implementation begins formally in Module 19.

# Phase 4 — Round 1 Paper-Test Preparation

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `15-round-1-exam-training` | MCQ reasoning, distractor analysis, calculations, code tracing/completion, short-answer writing, timed paper practice | official NOAI syllabus/tasks, BML15 review sequence | CS50P, MLS, HML, SQ, 3B1B, DLS selected review as needed |

**Phase rule:** the assessment form is driven by official NOAI requirements. External courses provide review material, not the exam format.

# Phase 5 — Data and Scikit-Learn Workflow for Round 2 C

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `16-numpy-pandas-matplotlib` | arrays, vectorisation, DataFrames, data audit, plotting, summary statistics | NumPy, Pandas, Matplotlib documentation | HML selected chapters; teacher starter notebooks |
| `17-data-cleaning-feature-engineering` | missing values, categories, scaling, leakage, one-hot encoding, windows/lags, image/text features | HML, SK | MLCC, official task notes, NumPy/Pandas documentation |
| `18-sklearn-workflow` | split, preprocessing, baseline, Pipeline, ColumnTransformer, metrics, CV, tuning, reproducibility | HML, SK | LHY-ML conceptual bridge; official NOAI/IOAI tasks |

**Phase rule:** HML supplies the practical project workflow; scikit-learn documentation is the source of truth for current APIs.

# Phase 6 — PyTorch and Domain Applications for Round 2 D

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `19-pytorch-foundations` | tensors, devices, shapes, Dataset/DataLoader, nn.Module, autograd, training/validation loops, checkpoints, debugging | DLAI-PT1 | PT official tutorials; LHY-ML conceptual bridge; DLS Course 2 selected concepts |
| `20-computer-vision` | OpenCV baseline, image datasets/transforms, CNN baseline, augmentation, transfer learning, detection/segmentation, error analysis | DLAI-PT2, PT/torchvision, CV | DLS Course 4, LHY-ML, official image-task repositories |
| `21-nlp-sequence-models` | tokenisation, vocabulary, sequence shapes, RNN/LSTM, transformer classification, NLP reproduction | HF-L; DLAI-PT2 selected text/Hugging Face content | DLS Course 5, LHY-ML, PT official tutorials |
| `22-audio-speech` | waveform, sampling, spectrogram/Mel features, audio classification, ASR, TTS | HF-A | PyTorch/torchaudio documentation; official NOAI audio-style task materials |
| `23-llm-generative-ai` | LLM principles, prompting, structured output, APIs, Qwen local deployment, multimodality, validation | QWEN, HF-L, current official API documentation | DLAI-PT3 optional deployment/Transformer extension; official annual rules |

**Phase rule:** the DeepLearning.AI PyTorch certificate is the main structured PyTorch series. Course 1 supports the PyTorch foundation module, Course 2 supports selected vision/NLP/project lessons, and Course 3 is optional advanced extension. PyTorch official tutorials remain the source of truth for current APIs.

# Phase 7 — Competition Integration

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `24-round-2-project-training` | task reading, data audit, validation, baseline, controlled experiments, ablation, error analysis, AI-use verification, submission checks | official NOAI/IOAI tasks, HML | DLS Course 3 selected strategy, DLAI-PT2, SK/PT/HF/Qwen documentation as task requires |
| `25-past-paper-reproduction` | reproduce official tasks, rebuild baseline, compare experiments, write postmortem, transfer lessons | NOAI and IOAI official task repositories | all task-specific framework resources |
| `26-mock-contests` | timed Round 1 and Round 2 simulations, reliability, fresh-runtime checks, final readiness conference | current official rules and task format | all selected resources only for permitted preparation/review |

**Phase rule:** Modules 24–26 are task-driven. The resource is chosen by the task modality; no external course overrides the official rules or competition constraints.

# Official Bohrium Resource Hub

| Module | Purpose | Resources |
|---|---|---|
| `27-official-bohrium-video-lessons` | resource hub for complete official-aligned Bohrium videos and the BML15 70-minute sequence | BML15 and LHY-ML |

Module 27 is a **resource hub**, not an additional independent curriculum phase. Its lessons are linked into the appropriate Round 1 and Round 2 modules.

---

# Simplified Mainline

```text
00          Official NOAI / IOAI orientation
01–03       CS50P Python foundation
04–11       BML15 + selected MLS / MLCC / HML / StatQuest
12–14       LHY-ML + 3B1B + selected DLS
15          Official Round 1 paper-test preparation
16–18       HML + NumPy/Pandas/Matplotlib + scikit-learn docs
19          DeepLearning.AI PyTorch Course 1 + PyTorch docs
20–21       DeepLearning.AI PyTorch Course 2 + vision/NLP official resources
22–23       Hugging Face Audio/LLM + Qwen/current official docs
24–26       Official NOAI / IOAI tasks, reproductions, and mocks
27          BML15 / LHY-ML Bohrium resource hub
```

# Teacher Assignment Rule

For every lesson, the teacher must name:

1. the exact required resource;
2. the exact course/module/chapter or timestamp range;
3. what students must extract from the resource;
4. what Guided Practice follows;
5. what students must rebuild independently;
6. what evidence must be submitted.

Do not write only a broad resource name such as `CS50P`, `MLS`, `DLS`, or `PyTorch`. Every lesson must identify the precise assigned portion.