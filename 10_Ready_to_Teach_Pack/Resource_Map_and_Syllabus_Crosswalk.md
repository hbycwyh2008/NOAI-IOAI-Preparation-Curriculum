# Resource Map and NOAI Syllabus Crosswalk

This document maps the NOAI China A–D syllabus areas to Class Mission modules, full resource names, student evidence, and assessments.

It uses **module paths instead of legacy session numbers** so that the crosswalk remains valid when the lesson bank expands.

The teacher must verify URLs, access terms, annual competition rules, model restrictions, package versions, and platform availability before each cohort begins.

## Resource Selection Rules

1. Use one required resource per ordinary lesson.
2. Write the complete resource name in student and teacher instructions.
3. Name the exact course, week, module, chapter, video, task, or timestamp range.
4. Use Coursera links for Coursera-hosted DeepLearning.AI courses.
5. Use official documentation as the source of truth for changing APIs.
6. Watching a resource is not evidence; students must practise, rebuild, explain, and submit proof.
7. Current official NOAI/IOAI rules override this repository.
8. Automated tuning is used only after task recognition, validation, data engineering, and a valid baseline are correct.

## Full Resource Names and Links

| Full resource name | Link | Main role |
|---|---|---|
| 北京市十一学校《中学机器学习十五讲》 | https://www.bohrium.com/courses/5963419225/content?file=8496 | official-aligned Round 1 A/B artificial-intelligence and machine-learning concept spine |
| 台湾大学李宏毅《机器学习》内容精选版 | https://www.bohrium.com/courses/7890895681/content?file=2496 | machine-learning and deep-learning conceptual bridge for Round 2 C/D |
| Harvard CS50’s Introduction to Programming with Python | https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f | Python foundations and code reading; assign exact timestamps |
| AI for Everyone | https://www.coursera.org/learn/ai-for-everyone | optional artificial-intelligence literacy, capability limits, ethics, and society |
| Machine Learning Specialization | https://www.coursera.org/specializations/machine-learning-introduction | selected traditional machine-learning concepts and development strategy |
| Course 2 — Advanced Learning Algorithms | https://www.coursera.org/learn/advanced-learning-algorithms | trees, ensembles, bias/variance diagnosis, learning curves, error analysis, and iterative development |
| Deep Learning Specialization | https://www.coursera.org/specializations/deep-learning | selected deep-learning concepts; not a second full curriculum |
| Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization | https://www.coursera.org/learn/deep-neural-network | regularisation, optimisation, learning-rate decay, Batch Normalization, and hyperparameter tuning |
| Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | https://github.com/ageron/handson-ml3 | practical scikit-learn workflow, preprocessing, evaluation, trees/ensembles, and end-to-end projects |
| DeepLearning.AI PyTorch for Deep Learning Professional Certificate | https://www.coursera.org/professional-certificates/pytorch-for-deep-learning | main structured PyTorch course series |
| Course 1 — PyTorch: Fundamentals | https://www.coursera.org/learn/pytorch-fundamentals | tensors, datasets, dataloaders, neural networks, and training pipelines |
| Course 2 — PyTorch: Techniques and Ecosystem Tools | https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools | TorchVision, Hugging Face, transfer learning, tuning, Optuna, and efficient pipelines |
| Course 3 — PyTorch: Advanced Architectures and Deployment | https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment | optional advanced architectures, compression, export, and deployment |
| Google Machine Learning Crash Course | https://developers.google.com/machine-learning/crash-course | concise regression, classification, metrics, generalisation, and feature reinforcement |
| StatQuest Video Index | https://statquest.org/video-index/ | statistics, distributions, metrics, trees, ensembles, and clarification |
| 3Blue1Brown Neural Networks | https://www.3blue1brown.com/topics/neural-networks | neural-network, gradient-descent, and backpropagation intuition |
| Scikit-Learn User Guide | https://scikit-learn.org/stable/user_guide.html | current preprocessing, Pipeline, metrics, cross-validation, and tuning APIs |
| PyTorch Tutorials | https://docs.pytorch.org/tutorials/ | current PyTorch API and implementation reference |
| Hugging Face LLM Course | https://huggingface.co/learn/llm-course/en/chapter1/1 | tokenisation, Transformers, classification, and fine-tuning |
| Hugging Face Audio Course | https://huggingface.co/learn/audio-course/en/chapter0/introduction | waveforms, spectrograms, audio classification, automatic speech recognition, and text-to-speech |
| OpenCV Free Courses | https://opencv.org/university/free-courses/ | classical image preprocessing and structural baselines |
| Current official Qwen documentation | teacher verifies current official documentation before the cohort | local inference, multimodality, quantisation, and deployment verification |
| Current official NOAI and IOAI rules, syllabi, and task repositories | teacher archives the current official sources before the cohort | competition scope, task format, allowed tools, runtime, and assessment constraints |

---

# A. General Computer Skills

| Syllabus area | Class Mission modules | Required resources | Required evidence | Main assessment |
|---|---|---|---|---|
| Python values, expressions, variables, and input/output | `01-python-foundations` | Harvard CS50’s Introduction to Programming with Python: exact Week 0 segments | trace tables, type/conversion explanation, robust input/output program | Round 1 code reading and multiple choice |
| Functions, parameters, return values, and scope | `01-python-foundations` | Harvard CS50’s Introduction to Programming with Python: Functions and Variables segments | multi-function program, return-versus-print explanation, function trace | cold trace and oral defence |
| Sequence, selection, Boolean logic, and iteration | `02-control-flow-and-data-structures` | Harvard CS50’s Introduction to Programming with Python: Conditionals and Loops segments | boundary table, branch trace, loop trace, independent rebuild | Round 1 code questions |
| Strings, lists, dictionaries, tuples, and nested structures | `02-control-flow-and-data-structures` | Harvard CS50’s Introduction to Programming with Python: exact collection segments | transformation, frequency table, nested-structure trace | code completion |
| Exceptions and debugging | `01-python-foundations`, `03-libraries-sorting-searching`, `19-pytorch-foundations` | Harvard CS50’s Introduction to Programming with Python: Exceptions; PyTorch debugging tasks | traceback diagnosis, debug log, corrected code | code-completion and runtime gate |
| Modules, packages, and documentation | `03-libraries-sorting-searching` | Harvard CS50’s Introduction to Programming with Python: Libraries; Python official documentation | import record, environment note, documentation-use explanation | setup evidence |
| Files and comma-separated-value data | `03-libraries-sorting-searching`, `16-numpy-pandas-matplotlib` | Harvard CS50’s Introduction to Programming with Python: File I/O; Pandas documentation | file/CSV reader, data-audit table | Round 2 baseline |
| Sorting and searching | `03-libraries-sorting-searching` | teacher-selected CS50 algorithms material; official NOAI-style paper tasks | paper traces and independent implementation | Round 1 mixed set |

# B. Artificial-Intelligence and Machine-Learning Foundations

| Syllabus area | Class Mission modules | Required resources | Required evidence | Main assessment |
|---|---|---|---|---|
| Artificial-intelligence schools, Turing Test, capability boundaries | `04-ai-foundations-and-ethics` | 北京市十一学校《中学机器学习十五讲》; current official NOAI syllabus | capability-claim analysis and example/non-example table | short answer |
| Ethics, bias, privacy, safety, and responsibility | `04-ai-foundations-and-ethics` | current official syllabus; 北京市十一学校《中学机器学习十五讲》; AI for Everyone optional | structured case analysis | Round 1 scenario |
| Supervised, unsupervised, and reinforcement learning | `05-learning-paradigms` | 北京市十一学校《中学机器学习十五讲》; selected Machine Learning Specialization content | task-type sorting, label/evidence diagram, state/action/reward design | concept check and scenario explanation |
| Regression | `06-linear-regression` | 北京市十一学校《中学机器学习十五讲》; selected Machine Learning Specialization content | paper calculations, residual/cost explanation, baseline model | Round 1 calculations and Round 2 project |
| Classification and logistic regression | `07-logistic-regression` | 北京市十一学校《中学机器学习十五讲》; selected Machine Learning Specialization content | sigmoid/threshold table, decision-boundary explanation, logistic workflow | code and project |
| Probability, statistics, normal distribution, and distance | `08-statistics-probability-distance` | StatQuest; selected 北京市十一学校《中学机器学习十五讲》 content | hand calculations and raw-versus-standardised comparison | Round 1 calculations |
| Confusion matrix, accuracy, precision, recall, specificity, F1, ROC/AUC | `09-model-evaluation` | Google Machine Learning Crash Course; StatQuest; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | confusion-matrix worksheet and metric decision memo | Round 1 and Round 2 metric gate |
| Cross-validation and evaluation design | `09-model-evaluation`, `18-sklearn-workflow` | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; Scikit-Learn User Guide | split diagram, cross-validation result, reliability memo | Round 2 gate |
| Underfitting, overfitting, learning curves, and regularisation | `10-generalization-regularization`, `28-competition-sprint-task-data-tuning` | selected Machine Learning Specialization content; Course 2 — Advanced Learning Algorithms; Course 2 — Improving Deep Neural Networks | bias/variance diagnosis and controlled remedy | short answer and tuning log |
| Decision trees, bagging, random forests, and boosting | `11-trees-and-ensembles` | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; selected Machine Learning Specialization content; StatQuest | impurity calculation and model-comparison table | Round 1 and model selection |
| Perceptrons, neurons, multilayer perceptrons, and forward propagation | `12-neural-network-foundations` | 台湾大学李宏毅《机器学习》内容精选版; 3Blue1Brown Neural Networks; selected Deep Learning Specialization content | numerical neuron, parameter count, hand forward pass | Round 1 short answer |
| Gradient descent and backpropagation | `13-backprop-optimization` | 台湾大学李宏毅《机器学习》内容精选版; 3Blue1Brown Neural Networks; selected Deep Learning Specialization content | computational-graph trace and gradient explanation | Round 1 and oral defence |
| Adam, AdamW, learning-rate decay, and optimisation choices | `13-backprop-optimization`, `19-pytorch-foundations`, `28-competition-sprint-task-data-tuning` | Course 2 — Improving Deep Neural Networks; Course 1 — PyTorch: Fundamentals; PyTorch Tutorials | controlled optimiser/learning-rate experiment | implementation and tuning log |
| Convolutional-neural-network concepts and shapes | `14-cnn-foundations` | 台湾大学李宏毅《机器学习》内容精选版; Course 4 — Convolutional Neural Networks from the Deep Learning Specialization | convolution and output-shape calculations | Round 1 short answer |

# C. Advanced Computer Skills

| Syllabus area | Class Mission modules | Required resources | Required evidence | Main assessment |
|---|---|---|---|---|
| NumPy arrays and vectorisation | `16-numpy-pandas-matplotlib`, `19-pytorch-foundations` | NumPy documentation; Course 1 — PyTorch: Fundamentals | vectorised utility and tensor/array shape ledger | coding gate |
| Pandas data manipulation and audit | `16-numpy-pandas-matplotlib`, `28-competition-sprint-task-data-tuning` | Pandas documentation; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | reproducible audit notebook and missing-value table | tabular mock |
| Matplotlib visualisation | `16-numpy-pandas-matplotlib` and project modules | Matplotlib documentation; Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | labelled diagnostic figures | report rubric |
| Missing values, categorical data, scaling, and leakage-safe preprocessing | `17-data-cleaning-feature-engineering`, `18-sklearn-workflow`, `28-competition-sprint-task-data-tuning` | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; Scikit-Learn User Guide | Pipeline/ColumnTransformer and leakage checklist | Round 2 gate |
| Feature engineering | `17-data-cleaning-feature-engineering`, `28-competition-sprint-task-data-tuning` | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; task-specific official documentation | feature hypothesis, before/after validation result | project and sprint |
| Image augmentation and transforms | `20-computer-vision` | Course 2 — PyTorch: Techniques and Ecosystem Tools; PyTorch/torchvision tutorials | augmentation policy and controlled experiment | image project |
| Tokenisation, vocabulary, padding, and embeddings | `21-nlp-sequence-models` | Hugging Face LLM Course; Course 2 — PyTorch: Techniques and Ecosystem Tools | tokenizer/collator tests and shape ledger | natural-language-processing project |
| Audio features and spectrograms | `22-audio-speech` | Hugging Face Audio Course; torchaudio documentation | waveform/spectrogram pipeline | audio reproduction |
| Reproducible notebook workflow | all coding modules | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; official framework documentation | fresh-runtime evidence, environment record, AI-use note | notebook rubric |

# D. Advanced Artificial-Intelligence Skills

| Syllabus area | Class Mission modules | Required resources | Required evidence | Main assessment |
|---|---|---|---|---|
| PyTorch tensors, devices, datasets, dataloaders, neural-network modules, autograd, and loops | `19-pytorch-foundations` | Course 1 — PyTorch: Fundamentals; PyTorch Tutorials | tensor audit, custom Dataset/DataLoader, complete train/validate loop | PyTorch gate |
| Computer vision and transfer learning | `20-computer-vision` | Course 2 — PyTorch: Techniques and Ecosystem Tools; PyTorch/torchvision tutorials; OpenCV resources | classical baseline, neural baseline, transfer model, image error analysis | image mock |
| Detection and segmentation | `20-computer-vision` | PyTorch official tutorials; Course 3 — PyTorch: Advanced Architectures and Deployment optional | intersection-over-union and failure analysis | extension task |
| Recurrent neural networks and long short-term memory networks | `21-nlp-sequence-models` | 台湾大学李宏毅《机器学习》内容精选版; Course 5 — Sequence Models from the Deep Learning Specialization; PyTorch Tutorials | sequence-shape ledger and reproduction | natural-language-processing reproduction |
| Transformer text classification | `21-nlp-sequence-models` | Hugging Face LLM Course; Course 2 — PyTorch: Techniques and Ecosystem Tools | simple-versus-pretrained comparison | project |
| Audio classification, automatic speech recognition, and text-to-speech | `22-audio-speech` | Hugging Face Audio Course | source-aware classifier and pipeline evaluation | audio project |
| Large-language-model API and structured output | `23-llm-generative-ai` | Hugging Face LLM Course; current official API documentation | validated structured-output utility | Round 2 task |
| Qwen local deployment and multimodality | `23-llm-generative-ai` | current official Qwen documentation; current official rules | offline smoke test and modality-baseline comparison | readiness gate and multimodal mock |
| Advanced architecture, compression, export, and deployment | selected extensions in Modules 20–24 | Course 3 — PyTorch: Advanced Architectures and Deployment; official PyTorch documentation | efficiency/export/deployment memo | IOAI extension |

# Competition Sprint Crosswalk

| Sprint skill | Module 28 lessons | Required resources | Required evidence |
|---|---|---|---|
| Task recognition | Lessons 01–02 | current official NOAI/IOAI task statements; Course 2 — Advanced Learning Algorithms selected material | task-recognition sheet and baseline/metric memo |
| Data audit and validation | Lesson 03 | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; Scikit-Learn User Guide | audit table, split design, leakage checklist |
| Data cleaning and feature engineering | Lesson 04 | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow; task-specific documentation | feature hypothesis and before/after result |
| Classical machine-learning tuning | Lesson 05 | Course 2 — Advanced Learning Algorithms, Week 3: Advice for Applying Machine Learning | diagnosis-first experiment log |
| Deep-learning tuning | Lesson 06 | Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization | learning-rate, regularisation, batch-size, and optimiser record |
| PyTorch schedulers, Optuna, and efficiency | Lesson 07 | Course 2 — PyTorch: Techniques and Ecosystem Tools, Module 1: Hyperparameter Optimization | manual-versus-automated comparison, search-space rationale, efficiency record |
| Full sprint simulation | Lesson 08 | current official task format and permitted tools | full solution package, fresh-runtime record, submission validation, postmortem |

Use the exact video assignments in:

`02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md`

---

# Assessment Coverage Matrix

| Assessment | Main competencies |
|---|---|
| Entry checks | retrieval, misconceptions, and prerequisite readiness |
| Lesson worksheets | definitions, calculations, code tracing, and scenario reasoning |
| Independent rebuilds | implementation or reasoning without copying |
| Oral defence | conceptual ownership and artificial-intelligence-use accountability |
| Round 1 mocks | broad A/B coverage, code, calculations, and explanations |
| Tabular mock | audit, validation, pipeline, metric, threshold, and submission |
| Domain projects | computer vision, natural-language processing, audio, large language models, and multimodality |
| Competition sprint | task recognition, data engineering, diagnosis-first tuning, efficiency, and submission risk |
| Final conference | cold knowledge, code defence, reproducibility, and time management |

# Maintenance Checklist Before Every Cohort

- [ ] archive the current official NOAI and IOAI syllabus and rules;
- [ ] confirm Round 1 and Round 2 duration and permitted tools;
- [ ] confirm internet, API, artificial-intelligence-assistant, and pretrained-model rules;
- [ ] confirm package, runtime, GPU, storage, and submission limits;
- [ ] verify every required resource link and access requirement;
- [ ] verify exact course modules, videos, durations, chapters, and timestamps;
- [ ] rerun starter notebooks and scripts in the final student environment;
- [ ] validate Module 28 Optuna, scheduler, and efficiency activities;
- [ ] keep hidden labels, answer keys, and scoring packages outside the public repository;
- [ ] confirm the teacher-key repository is private;
- [ ] update this crosswalk whenever the official syllabus or curriculum architecture changes.