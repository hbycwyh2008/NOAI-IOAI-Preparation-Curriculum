# Resource Map and NOAI Syllabus Crosswalk

This document maps the 2026 NOAI China A–D syllabus structure to teaching sessions, required resources, student evidence, and major assessments. Resource titles are used instead of fragile timestamps unless a verified timestamp map exists. The teacher must verify URLs, access terms, annual competition rules, model restrictions, and package availability before each cohort begins.

## Resource Selection Rules

1. One required resource per ordinary lesson.
2. When a full Bohrium video is assigned, use `02_Class_Missions/shared/full-bohrium-video-classroom-flow.md`.
3. When a course segment is assigned, name the exact course, module/week, topic, and segment; do not assign an entire playlist during class.
4. Use Coursera links for Coursera-hosted DeepLearning.AI resources.
5. Official documentation replaces videos for APIs that change frequently.
6. A resource is not evidence; the worksheet, guided practice, independent rebuild, oral defence, and fresh-run record are evidence.
7. Annual NOAI/IOAI rules override this repository.

## Official-Aligned Bohrium Resources

| Code | Resource | Link | Official-aligned use |
|---|---|---|---|
| BML15 | 北京市十一学校《中学机器学习十五讲》 | https://www.bohrium.com/courses/5963419225/content?file=8496 | Round 1 A/B concepts and paper-test preparation |
| LHY-ML | 台湾大学李宏毅《机器学习》内容精选版 | https://www.bohrium.com/courses/7890895681/content?file=2496 | Round 2 C/D ML/DL concept reinforcement before or after implementation |

## Practical Selected Resources

| Code | Resource | Link | Use rule |
|---|---|---|---|
| CS50P | Harvard CS50's Introduction to Programming with Python | https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f | Main Python resource; assign exact verified segments |
| AIF | AI for Everyone | https://www.coursera.org/learn/ai-for-everyone | Optional AI literacy, ethics, limits, and society |
| MLS | Machine Learning Specialization | https://www.coursera.org/specializations/machine-learning-introduction | Selected traditional ML concept reinforcement |
| DLS | Deep Learning Specialization | https://www.coursera.org/specializations/deep-learning | Selected conceptual support for optimisation, CNNs, and sequence models |
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | https://github.com/ageron/handson-ml3 | Main practical sklearn and end-to-end ML workflow resource |
| DLAI-PT | PyTorch for Deep Learning Professional Certificate | https://www.coursera.org/professional-certificates/pytorch-for-deep-learning | Main structured PyTorch course series |
| DLAI-PT1 | PyTorch: Fundamentals | https://www.coursera.org/learn/pytorch-fundamentals | PyTorch foundations and complete training pipeline |
| DLAI-PT2 | PyTorch: Techniques and Ecosystem Tools | https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools | TorchVision, Hugging Face, transfer learning, tuning, efficient pipelines |
| DLAI-PT3 | PyTorch: Advanced Architectures and Deployment | https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment | Optional advanced architecture, compression, export, and deployment extension |
| SK | scikit-learn User Guide | https://scikit-learn.org/stable/user_guide.html | Current sklearn API and workflow reference |
| PT | PyTorch Tutorials | https://docs.pytorch.org/tutorials/ | Current PyTorch API reference |

## Primary Resource Index

| Code | Resource | Assigned scope |
|---|---|---|
| NOAI | Current official NOAI handbook, FAQ, syllabus, and authorised task repositories | format, rules, past tasks, permitted environment |
| IOAI | IOAI Academy / official task repositories | open-ended, multimodal, small-data, and competition workflow |
| BML15 | 中学机器学习十五讲 | Round 1 A/B concept spine |
| LHY-ML | 李宏毅机器学习精选 | ML/DL concept reinforcement |
| CS50P | CS50 Python | Python foundations and code reading |
| MLS | Andrew Ng Machine Learning Specialization | selected regression, classification, clustering, trees, ensembles, ML development concepts |
| DLS | Andrew Ng Deep Learning Specialization | selected deep-learning concepts, not a full five-course route |
| HML | Hands-On Machine Learning | sklearn, preprocessing, model evaluation, end-to-end workflow |
| DLAI-PT | DeepLearning.AI PyTorch certificate | structured PyTorch implementation path |
| SK / PT | Official framework documentation | current API correctness |
| SQ | StatQuest | statistics, metrics, trees, ensembles clarification |
| 3B1B | 3Blue1Brown Neural Networks | neural-network, gradient-descent, and backprop intuition |
| MLCC | Google Machine Learning Crash Course | regression, classification metrics, generalisation, feature handling |
| CV | OpenCV official/free-course resources | classical image preprocessing and structural baselines |
| HF-L | Hugging Face LLM Course | tokenisation, transformers, classification, fine-tuning |
| HF-A | Hugging Face Audio Course | waveforms, spectrograms, classification, ASR/TTS |
| QWEN | Current Qwen/Hugging Face documentation | local inference, multimodality, quantisation |

---

# A. General Computer Skills

| Syllabus item | Sessions | Required resource | Required evidence | Assessed in |
|---|---:|---|---|---|
| Python values, expressions, input/output | 3–4 | CS50P exact Week 0 segments | trace tables, robust input program | Round 1 code/MCQ |
| Sequence, selection, iteration | 5–6 | CS50P Conditionals and Loops segments | boundary table, loop trace | Round 1 code |
| Strings, lists, dictionaries, tuples | 6 | CS50P Loops/collections segments | transformation and frequency programs | cold trace |
| Functions | 3–4 | CS50P Functions segments | multi-function program and return trace | oral defence |
| Modules and packages | 7 | CS50P Libraries + documentation | import/environment record | setup evidence |
| Files and CSV | 7, 39–40 | CS50P File I/O; HML/Pandas | CSV audit utility | Round 2 baseline |
| Exceptions and debugging | 4, 47 | CS50P Exceptions; PyTorch debug tasks | traceback diagnosis and debug log | code completion |
| Sorting and searching | 8 | teacher-selected CS50 algorithms excerpt | paper traces and implementations | Round 1 mixed set |

# B. AI Foundations

| Syllabus item | Sessions | Resource | Required evidence | Assessment |
|---|---:|---|---|---|
| AI schools and Turing Test | 9 | BML15 + official syllabus; AIF optional | capability-claim evaluation | short answer |
| Ethics, bias, privacy, risk | 10 | BML15 + official syllabus; AIF optional | structured case analysis | Round 1 scenario |
| Supervised learning | 11, 13–16 | BML15; MLS optional | task classification and baseline choice | mocks/projects |
| Unsupervised learning | 11 | BML15; MLS optional | clustering/anomaly task design | concept check |
| Reinforcement learning | 12 | BML15; MLS Course 3 intro optional | state/action/reward design | concept question |
| Regression | 13–14 | BML15; MLS/HML/MLCC | calculations and sklearn model | calculation/project |
| Classification | 15–16 | BML15; MLS/HML/MLCC | threshold table and logistic workflow | code/project |
| Clustering | 11 + extension | BML15; MLS optional | cluster interpretation and limitations | oral defence |
| Probability/statistics/normal distribution | 17–18 | SQ; BML15 when aligned | hand calculations | Round 1 calculations |
| Distance and standardisation | 18, 39 | SQ/NumPy/HML | raw vs scaled comparison | Round 1/2 |
| Accuracy, precision, recall, specificity, F1 | 19–20 | MLCC/SQ/HML | confusion-matrix worksheet | Round 1 |
| ROC/AUC and threshold choice | 20 | MLCC/SQ/HML | metric decision memo | multimodal mock |
| Cross-validation | 21, 44 | SK/HML | split design and CV report | Round 2 |
| Under/overfitting | 22–23 | BML15; MLS/HML/MLCC | curve diagnosis | short answer |
| Regularisation | 23 | MLS/DLS/HML | controlled experiment | Round 1/2 |
| Decision trees | 24 | MLS/HML/SQ | impurity and depth experiment | Round 1 |
| Bagging/random forest | 25 | MLS/HML/SQ | tree vs forest comparison | short answer |
| Boosting | 26 | MLS/HML/SQ | three-model comparison | model selection |
| Perceptron/neuron | 27 | LHY-ML/3B1B/DLS selected | numerical neuron and XOR explanation | Round 1 |
| MLP/forward propagation | 28 | LHY-ML/3B1B/DLS selected | hand forward pass | Round 1 |
| Gradient descent/backpropagation | 29–30 | LHY-ML/3B1B/DLS selected | computational-graph derivation | Round 1 |
| Optimisers Adam/AdamW | 31 | LHY-ML/DLS/DLAI-PT1/PT | controlled optimiser comparison | oral/implementation |
| CNN concepts | 32–34 | LHY-ML/DLS | convolution calculation and shape reasoning | Round 1 |
| Activation, output, loss functions | 27, 33–34 | LHY-ML/3B1B/DLS/DLAI-PT1 | role comparison and correct loss code | Round 1/PyTorch |
| Train/validation/test and cleaning | 21–23, 39–43 | BML15/MLS/HML/SK | validation memo and pipeline | Round 2 gate |
| LLM principles | 56–57 | HF-L/QWEN + official syllabus | structured-output and offline package | concept + Round 2 |

# C. Advanced Computer Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| NumPy arrays and vectorisation | 39, 45 | NumPy/HML/DLAI-PT1/PT | scaling utility and shape ledger | coding gate |
| Pandas data manipulation | 40–43 | Pandas/HML/SK | reproducible audit notebook | tabular mock |
| Matplotlib visualisation | 40 + projects | Matplotlib/HML | diagnostic figures | report rubric |
| Missing values and categories | 41, 43 | HML/SK | mixed-type pipeline | tabular mock |
| Feature engineering | 42 | HML/MLCC | before/after experiment | Round 2 |
| Windows, lags, moments | 42, 62 | teacher/IOAI notes | leak-free feature table | AI4Science mock |
| Image augmentation | 49 | DLAI-PT2/PT/torchvision | augmentation experiment | image project |
| Tokenisation and vocabulary | 51 | HF-L/DLAI-PT2 selected | collator and shape tests | NLP project |
| Embeddings | 42, 51–53 | HF-L/DLAI-PT2 | embedding workflow explanation | oral defence |
| Image patching | 42, 57 | QWEN/multimodal docs | patch/sequence calculation | multimodal task |
| Reproducible notebook workflow | all coding sessions | HML/DLAI-PT/PT/SK | fresh-run evidence | notebook rubric |

# D. Advanced AI Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| PyTorch tensors/devices | 45 | DLAI-PT1/PT | tensor audit utility | PyTorch gate |
| Dataset/DataLoader/nn.Module | 46 | DLAI-PT1/PT | independent rebuild | PyTorch gate |
| Autograd/training loop | 46–47 | DLAI-PT1/PT | full train/validate loop | Round 2 |
| CPU/GPU movement | 45–47 | DLAI-PT1/PT | device-safe code | fresh-run check |
| Mixed precision | 47 | PT AMP; DLAI-PT selected | controlled AMP test | oral defence |
| Initialisation/batch normalisation | 31, 34 + extension | DLS/DLAI-PT1/PT | architecture comparison | extension |
| CNN/computer vision implementation | 48–50 | DLAI-PT2/PT/CV | classical baseline + transfer model | image mock |
| Detection/segmentation | 50 | PT tutorials; DLAI-PT3 optional | IoU/error analysis | extension task |
| RNN/LSTM | 52 | LHY-ML/DLS/PT | sequence model and shape ledger | NLP reproduction |
| NLP/transformer classification | 51–53 | HF-L/DLAI-PT2 | simple vs pretrained comparison | NLP project |
| Audio classification | 54–55 | HF-A | source-aware classifier | audio reproduction |
| ASR/TTS | 55 | HF-A | pipeline evaluation | domain task |
| Generative AI/LLM API | 56 | HF-L/current API docs | validated structured-output utility | Round 2 |
| Qwen local deployment | 57 | QWEN docs + annual rules | offline smoke test | readiness gate |
| Multimodality | 57, 66 | QWEN/IOAI | modality baseline comparison | six-hour mock |
| Advanced architecture/deployment | extension | DLAI-PT3/PT official docs | efficiency/export/deployment memo | IOAI extension |
| Competition workflow | 1, 58–67 | IOAI/NOAI | baseline, validation, experiments, submission | timed mocks |

---

# Assessment Coverage Matrix

| Assessment | Main competencies |
|---|---|
| Entry checks | retrieval, misconceptions, prerequisite readiness |
| Lesson worksheets | definitions, calculations, code tracing, scenario reasoning |
| Independent rebuilds | implementation without copying |
| Oral defence | conceptual ownership and AI-use accountability |
| Round 1 mocks | broad A/B coverage, code, calculations, explanations |
| Tabular mock | audit, validation, pipeline, threshold, submission |
| Multimodal mock | single-modality baselines, fusion, stress tests, offline execution |
| Final conference | cold knowledge, code defence, reproducibility, time management |

# Maintenance Checklist Before Every Cohort

- [ ] archive the current official syllabus and rules;
- [ ] confirm Round 1/2 duration and permitted tools;
- [ ] confirm internet, API, AI-assistant, and pretrained-model rules;
- [ ] confirm package/runtime/GPU limits;
- [ ] verify every required resource link and access requirement;
- [ ] verify exact course modules and assigned segments;
- [ ] run every starter environment from a fresh account/runtime;
- [ ] keep hidden labels and scoring keys outside the student repository;
- [ ] confirm the teacher-key repository is private;
- [ ] update the crosswalk when the official syllabus changes.
