# Class Mission Resource Architecture

This document explains the large-scale structure of `02_Class_Missions` and identifies which learning resources support each module.

The curriculum is **not** organised as one complete external course followed from beginning to end. It is organised around the NOAI A/B/C/D skill requirements and NOAI/IOAI task demands. External courses are selected by topic and used only where they strengthen a specific mission.

## Resource Priority

Use resources in this order:

1. **Official NOAI / IOAI rules, syllabus, tasks, and competition environment** — define the required knowledge, allowed tools, task format, and competition workflow.
2. **Official-aligned structured courses** — 北京市十一学校《中学机器学习十五讲》、台湾大学李宏毅《机器学习》内容精选版、Harvard CS50’s Introduction to Programming with Python、Machine Learning Specialization、Deep Learning Specialization，以及 DeepLearning.AI PyTorch for Deep Learning Professional Certificate。
3. **Implementation resources and official documentation** — Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow、scikit-learn User Guide、PyTorch official tutorials、NumPy、Pandas、Matplotlib、Hugging Face、Qwen、OpenCV 和 torchvision 官方文档。
4. **Concept-clarification resources** — StatQuest、3Blue1Brown Neural Networks、Google Machine Learning Crash Course，以及教师精选的补充讲解。

One ordinary lesson should normally have **one required resource**. The tables below list the available resource set for each module; they do not mean students use every listed resource in every lesson.

## Full Resource Names

| Full resource name | Role in the curriculum |
|---|---|
| Current official NOAI handbook, syllabus, rules, and task repositories | Round 1/2 scope, rules, task forms, and permitted tools |
| IOAI official syllabus, rules, academy materials, and task repositories | international-task style, open-ended workflow, and multimodal extension |
| 北京市十一学校《中学机器学习十五讲》 on Bohrium | official-aligned Round 1 A/B artificial-intelligence and machine-learning concept formation |
| 台湾大学李宏毅《机器学习》内容精选版 on Bohrium | machine-learning and deep-learning conceptual bridge for Round 2 C/D |
| Harvard CS50’s Introduction to Programming with Python on edX | Python syntax, functions, conditionals, loops, exceptions, libraries, and files |
| AI for Everyone on Coursera | optional AI-literacy, capability, ethics, risk, and society support |
| Machine Learning Specialization on Coursera | selected traditional machine-learning explanations: learning paradigms, regression, classification, trees, and ensembles |
| Google Machine Learning Crash Course | concise reinforcement for regression, classification, metrics, generalisation, and data features |
| Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | practical scikit-learn workflow, preprocessing, evaluation, model comparison, and project habits |
| StatQuest | statistics, distributions, metrics, trees, ensembles, and model-evaluation clarification |
| 3Blue1Brown Neural Networks | neural-network, gradient-descent, and backpropagation intuition |
| Deep Learning Specialization on Coursera | selected deep-learning concepts: optimisation, convolutional neural networks, project strategy, and sequence models |
| PyTorch: Fundamentals on Coursera | main structured PyTorch foundation course |
| PyTorch: Techniques and Ecosystem Tools on Coursera | selected transfer learning, TorchVision, Hugging Face, tuning, and efficient-training content |
| PyTorch: Advanced Architectures and Deployment on Coursera | optional advanced architecture, compression, export, and deployment extension |
| scikit-learn User Guide | current scikit-learn APIs, pipelines, metrics, cross-validation, and tuning |
| PyTorch official tutorials | current PyTorch APIs and implementation verification |
| OpenCV official documentation and courses | classical image preprocessing and structural baselines |
| Hugging Face LLM Course and documentation | tokenisation, Transformers, text classification, and fine-tuning |
| Hugging Face Audio Course and documentation | waveforms, spectrograms, audio classification, automatic speech recognition, and text-to-speech |
| Current official Qwen documentation | local inference, multimodal processing, quantisation, and deployment checks |

---

# Phase 0 — Competition Orientation

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `00-course-overview` | NOAI Round 1/2 structure, baseline thinking, evidence, GitHub/Bohrium workflow | Current official NOAI handbook, syllabus, rules, and task repositories; IOAI official syllabus, rules, academy materials, and task repositories | official platform and runtime documentation |

# Phase 1 — Python Foundations for Round 1 A

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `01-python-foundations` | values, types, functions, input/output, return values, debugging | Harvard CS50’s Introduction to Programming with Python: Week 0 and Week 3; exact sections and timestamps in `05_Resources/CS50P_edX_Timestamp_Map.md` | Python official documentation; teacher code-tracing tasks |
| `02-control-flow-and-data-structures` | conditionals, Boolean logic, loops, strings, lists, dictionaries, tuples, nested structures | Harvard CS50’s Introduction to Programming with Python: Week 1 and Week 2; exact timestamps in the CS50P map | teacher Round 1 tracing and code-completion sets |
| `03-libraries-sorting-searching` | modules, packages, files, CSV, exceptions, documentation use, search and simple sorting | Harvard CS50’s Introduction to Programming with Python: Week 4 and Week 6 for libraries/files; teacher-selected CS50 algorithms material for search/sort | Python official documentation; NOAI-style paper traces |

**Phase rule:** Harvard CS50’s Introduction to Programming with Python is the main Python course. Students use only the assigned week, topic, and timestamp range; they do not browse or complete the whole course during class.

# Phase 2 — Artificial Intelligence and Machine-Learning Foundations for Round 1 B

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `04-ai-foundations-and-ethics` | AI schools, Turing Test, capability boundaries, bias, privacy, and risk | 北京市十一学校《中学机器学习十五讲》; current official NOAI syllabus | AI for Everyone on Coursera as optional support |
| `05-learning-paradigms` | supervised learning, unsupervised learning, reinforcement learning; regression/classification/clustering task recognition; training versus inference | 北京市十一学校《中学机器学习十五讲》 | selected modules from Machine Learning Specialization; official NOAI scenario questions |
| `06-linear-regression` | prediction, residual, cost, gradient descent, one-feature and multi-feature reasoning | 北京市十一学校《中学机器学习十五讲》; selected linear-regression modules from Machine Learning Specialization | Google Machine Learning Crash Course; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide |
| `07-logistic-regression` | sigmoid, probability, threshold, decision boundary, and log loss | 北京市十一学校《中学机器学习十五讲》; selected classification modules from Machine Learning Specialization | Google Machine Learning Crash Course; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide |
| `08-statistics-probability-distance` | mean, variance, standard deviation, probability, normal distribution, distance, and standardisation | StatQuest | 北京市十一学校《中学机器学习十五讲》; NumPy official documentation; teacher calculation sets |
| `09-model-evaluation` | confusion matrix, accuracy, precision, recall, specificity, F1, ROC/AUC, thresholds, and cross-validation | Google Machine Learning Crash Course; StatQuest | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide; 北京市十一学校《中学机器学习十五讲》 where aligned |
| `10-generalization-regularization` | underfitting, overfitting, train/validation/test, regularisation, and learning curves | 北京市十一学校《中学机器学习十五讲》; selected modules from Machine Learning Specialization | Google Machine Learning Crash Course; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; selected explanations from Course 2 of Deep Learning Specialization |
| `11-trees-and-ensembles` | decision trees, impurity/information gain, bagging, random forest, and boosting | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; selected tree and ensemble modules from Machine Learning Specialization | StatQuest; scikit-learn User Guide |

**Phase rule:** 北京市十一学校《中学机器学习十五讲》 is the official-aligned Round 1 concept spine. Machine Learning Specialization, Google Machine Learning Crash Course, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, and StatQuest are selected reinforcement resources; they do not replace official NOAI scope.

# Phase 3 — Neural Networks and Deep-Learning Concepts

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `12-neural-network-foundations` | perceptron, neuron, weights, bias, activation, multilayer perceptron, forward pass, and parameter/shape reasoning | 台湾大学李宏毅《机器学习》内容精选版; 3Blue1Brown Neural Networks | selected explanations from Course 1 of Deep Learning Specialization; 北京市十一学校《中学机器学习十五讲》 |
| `13-backprop-optimization` | gradient descent, computational graph, backpropagation, learning rate, Adam/AdamW, and convergence | 台湾大学李宏毅《机器学习》内容精选版; 3Blue1Brown Neural Networks | selected modules from Course 2 of Deep Learning Specialization; PyTorch: Fundamentals and PyTorch official tutorials for implementation grounding |
| `14-cnn-foundations` | convolution, filters, padding, stride, pooling, output shapes, and activation/loss roles | 台湾大学李宏毅《机器学习》内容精选版; selected modules from Course 4 of Deep Learning Specialization | PyTorch: Fundamentals; PyTorch: Techniques and Ecosystem Tools; PyTorch official tutorials; torchvision official documentation; 3Blue1Brown Neural Networks where useful |

**Phase rule:** Deep Learning Specialization is selected conceptual support, not a complete five-course route. Formal PyTorch implementation begins in Module 19.

# Phase 4 — Round 1 Paper-Test Preparation

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `15-round-1-exam-training` | multiple-choice reasoning, distractor analysis, calculations, code tracing/completion, short-answer writing, and timed paper practice | current official NOAI syllabus and tasks; 北京市十一学校《中学机器学习十五讲》 review sequence | Harvard CS50’s Introduction to Programming with Python; Machine Learning Specialization; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; StatQuest; 3Blue1Brown Neural Networks; selected Deep Learning Specialization review as needed |

**Phase rule:** the assessment form is driven by official NOAI requirements. External courses provide review material, not the exam format.

# Phase 5 — Data and Scikit-Learn Workflow for Round 2 C

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `16-numpy-pandas-matplotlib` | arrays, vectorisation, DataFrames, data audit, plotting, and summary statistics | NumPy, Pandas, and Matplotlib official documentation | selected chapters from Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; teacher starter notebooks |
| `17-data-cleaning-feature-engineering` | missing values, categories, scaling, leakage, one-hot encoding, windows/lags, image/text features | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide | Google Machine Learning Crash Course; official task notes; NumPy and Pandas official documentation |
| `18-sklearn-workflow` | split, preprocessing, baseline, Pipeline, ColumnTransformer, metrics, cross-validation, tuning, and reproducibility | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; scikit-learn User Guide | 台湾大学李宏毅《机器学习》内容精选版 as a conceptual bridge; official NOAI/IOAI tasks |

**Phase rule:** Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow supplies the practical project workflow; the scikit-learn User Guide is the source of truth for current APIs.

# Phase 6 — PyTorch and Domain Applications for Round 2 D

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `19-pytorch-foundations` | tensors, devices, shapes, Dataset/DataLoader, nn.Module, autograd, training/validation loops, checkpoints, and debugging | PyTorch: Fundamentals on Coursera | PyTorch official tutorials; 台湾大学李宏毅《机器学习》内容精选版 as a conceptual bridge; selected concepts from Course 2 of Deep Learning Specialization |
| `20-computer-vision` | OpenCV baseline, image datasets/transforms, convolutional-neural-network baseline, augmentation, transfer learning, detection/segmentation, and error analysis | PyTorch: Techniques and Ecosystem Tools; PyTorch and torchvision official tutorials; OpenCV official documentation and courses | selected modules from Course 4 of Deep Learning Specialization; 台湾大学李宏毅《机器学习》内容精选版; official image-task repositories |
| `21-nlp-sequence-models` | tokenisation, vocabulary, sequence shapes, recurrent neural networks, long short-term memory networks, Transformer classification, and natural-language-processing reproduction | Hugging Face LLM Course and documentation; selected text and Hugging Face content from PyTorch: Techniques and Ecosystem Tools | selected modules from Course 5 of Deep Learning Specialization; 台湾大学李宏毅《机器学习》内容精选版; PyTorch official tutorials |
| `22-audio-speech` | waveform, sampling, spectrogram/Mel features, audio classification, automatic speech recognition, and text-to-speech | Hugging Face Audio Course and documentation | PyTorch and torchaudio official documentation; official NOAI audio-style task materials |
| `23-llm-generative-ai` | large-language-model principles, prompting, structured output, APIs, Qwen local deployment, multimodality, and validation | current official Qwen documentation; Hugging Face LLM Course and documentation; current official API documentation | PyTorch: Advanced Architectures and Deployment as an optional Transformer/deployment extension; current official annual rules |

**Phase rule:** the DeepLearning.AI PyTorch for Deep Learning Professional Certificate is the main structured PyTorch series. PyTorch: Fundamentals supports the PyTorch foundation module; PyTorch: Techniques and Ecosystem Tools supports selected computer-vision, natural-language-processing, and project lessons; PyTorch: Advanced Architectures and Deployment is an optional advanced extension. PyTorch official tutorials remain the source of truth for current APIs.

# Phase 7 — Competition Integration

| Module | Main content | Primary resources | Supporting resources |
|---|---|---|---|
| `24-round-2-project-training` | task reading, data audit, validation, baseline, controlled experiments, ablation, error analysis, AI-use verification, and submission checks | official NOAI and IOAI tasks; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | selected project-strategy content from Course 3 of Deep Learning Specialization; PyTorch: Techniques and Ecosystem Tools; scikit-learn, PyTorch, Hugging Face, and Qwen documentation as the task requires |
| `25-past-paper-reproduction` | reproduce official tasks, rebuild baseline, compare experiments, write postmortem, and transfer lessons | official NOAI and IOAI task repositories | all task-specific framework resources |
| `26-mock-contests` | timed Round 1 and Round 2 simulations, reliability, fresh-runtime checks, and final readiness conference | current official rules and task format | all selected resources only for permitted preparation and review |

**Phase rule:** Modules 24–26 are task-driven. The resource is chosen by the task modality; no external course overrides official rules or competition constraints.

# Official Bohrium Resource Hub

| Module | Purpose | Resources |
|---|---|---|
| `27-official-bohrium-video-lessons` | resource hub for complete official-aligned Bohrium videos and the 14-session 70-minute sequence | 北京市十一学校《中学机器学习十五讲》 and 台湾大学李宏毅《机器学习》内容精选版 |

Module 27 is a **resource hub**, not an additional independent curriculum phase. Its lessons are linked into the appropriate Round 1 and Round 2 modules.

---

# Simplified Mainline

```text
00          Official NOAI / IOAI orientation
01–03       Harvard CS50’s Introduction to Programming with Python
04–11       北京市十一学校《中学机器学习十五讲》 + selected Machine Learning Specialization / Google Machine Learning Crash Course / Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow / StatQuest
12–14       台湾大学李宏毅《机器学习》内容精选版 + 3Blue1Brown Neural Networks + selected Deep Learning Specialization
15          Official Round 1 paper-test preparation
16–18       Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow + NumPy/Pandas/Matplotlib + scikit-learn User Guide
19          PyTorch: Fundamentals + PyTorch official tutorials
20–21       PyTorch: Techniques and Ecosystem Tools + official computer-vision and natural-language-processing resources
22–23       Hugging Face Audio Course / Hugging Face LLM Course + Qwen and current official documentation
24–26       Official NOAI / IOAI tasks, reproductions, and mock contests
27          北京市十一学校《中学机器学习十五讲》 / 台湾大学李宏毅《机器学习》内容精选版 Bohrium resource hub
```

# Teacher Assignment Rule

For every lesson, the teacher must name:

1. the exact full resource name;
2. the exact course, module, chapter, or timestamp range;
3. what students must extract from the resource;
4. what Guided Practice follows;
5. what students must rebuild independently;
6. what evidence must be submitted.

Do not write only an abbreviation or internal code. Do not write only a broad resource name such as `Machine Learning Specialization`, `Deep Learning Specialization`, or `PyTorch`. Every lesson must identify the precise assigned course portion.