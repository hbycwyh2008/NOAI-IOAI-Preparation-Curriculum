# Resource Map and NOAI Syllabus Crosswalk

This document maps the 2026 NOAI China A–D syllabus structure to the 67 teaching sessions, required resources, student evidence, and major assessments. Resource titles are deliberately used instead of fragile timestamps. The teacher must verify URLs, access terms, annual competition rules, model restrictions, and package availability before each cohort begins.

## Resource Selection Rules

1. One required resource per ordinary lesson. The required resource may be a full Bohrium video when the lesson is explicitly marked as a full-video lesson.
2. When a full Bohrium video is assigned, use `02_Class_Missions/shared/full-bohrium-video-classroom-flow.md`: students watch the full assigned video, complete guided notes, and then complete Talk Robin, Entry Check, Core Pattern, Guided Practice, Independent Rebuild, and Evidence.
3. When a short segment is assigned, students use only the named chapter/module, not an entire playlist during class.
4. Official documentation replaces videos for APIs that change frequently.
5. A resource is not evidence; the worksheet, independent task, guided notes, independent rebuild, and oral defence are evidence.
6. Annual NOAI/IOAI rules override this repository, especially for internet access, pretrained models, package versions, local deployment, and AI-assistant use.
7. For Coursera-hosted video courses, use the Coursera course/specialization link rather than a DeepLearning.AI marketing-page link.

## Official-Aligned Bohrium Resources

| Code | Resource | Link | Official-aligned use |
|---|---|---|---|
| BML15 | 北京市十一学校《中学机器学习十五讲》 | https://www.bohrium.com/courses/5963419225/content?file=8496 | Round 1 A/B: Python-related reasoning, AI foundations, machine-learning concepts, paper-test preparation |
| LHY-ML | 台湾大学李宏毅《机器学习》内容精选版 | https://www.bohrium.com/courses/7890895681/content?file=2496 | Round 2 C/D: machine-learning and deep-learning understanding before or after sklearn/PyTorch practice |

## Practical Selected Resources

| Code | Resource | Link | Use rule |
|---|---|---|---|
| CS50P | Harvard CS50's Introduction to Programming with Python | https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f | Main Python resource for functions, variables, conditionals, loops, exceptions, libraries, file I/O, and code reading. Use only assigned sections. |
| AIF | AI for Everyone | https://www.coursera.org/learn/ai-for-everyone | Optional AI-literacy resource for what AI can/cannot do, AI in society, ethics, risk, and organisational thinking. |
| MLS | Machine Learning Specialization | https://www.coursera.org/specializations/machine-learning-introduction | Optional concept reinforcement for supervised/unsupervised/RL, regression, classification, trees, ensembles, and ML development habits. |
| DLS | Deep Learning Specialization | https://www.coursera.org/specializations/deep-learning | Selected support for optimisation, CNNs, and sequence models. Do not assign the full five-course sequence as the main route. |
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | https://github.com/ageron/handson-ml3 | Use selected chapters for sklearn workflow, preprocessing, evaluation, model comparison, trees/ensembles, and end-to-end project habits. Do not use as the PyTorch mainline. |
| DB-PT | Daniel Bourke / Zero to Mastery Learn PyTorch for Deep Learning | https://www.learnpytorch.io/ | Main PyTorch video/hands-on resource for tensors, Dataset, DataLoader, nn.Module, training loops, computer vision, transfer learning, and reproducible experiments. |
| JP-PT | Jose Portilla PyTorch / Deep Learning Bootcamp | teacher-selected course link | Optional backup video resource for students who need a slower alternate PyTorch explanation. |

## Primary Resource Index

| Code | Resource | Assigned scope |
|---|---|---|
| NOAI | Current official NOAI handbook, FAQ, syllabus, and authorised task repositories | format, annual rules, past tasks, allowed environment |
| BML15 | 北京市十一学校《中学机器学习十五讲》 | Round 1 A/B official-aligned concept and machine-learning preparation |
| LHY-ML | 台湾大学李宏毅《机器学习》内容精选版 | Round 2 C/D official-aligned machine-learning and deep-learning preparation |
| CS50P | Harvard CS50's Introduction to Programming with Python — edX learning page listed above | Functions/Variables; Conditionals; Loops; Exceptions; Libraries; File I/O |
| AIF | AI for Everyone — Coursera link listed above | What AI Can/Cannot Do; AI and Society |
| MLS | Machine Learning Specialization — Coursera link listed above | supervised/unsupervised/RL; regression; classification; trees/ensembles |
| MLCC | Google Machine Learning Crash Course | linear/logistic regression; classification metrics; generalisation; overfitting; numerical/categorical data |
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | practical sklearn workflow; preprocessing; evaluation; cross-validation; trees/ensembles; end-to-end projects |
| SQ | StatQuest | statistics; normal distribution; metrics; trees/ensembles clarification |
| 3B1B | 3Blue1Brown Neural Networks | neural-network intuition; gradient descent; backpropagation calculus |
| DLS | Deep Learning Specialization — Coursera link listed above | selected optimisation; CNN operations; selected sequence-model explanations |
| DB-PT | Daniel Bourke / Zero to Mastery Learn PyTorch for Deep Learning | PyTorch implementation: tensors; datasets; dataloaders; nn.Module; training loops; vision; transfer learning |
| JP-PT | Jose Portilla PyTorch / Deep Learning Bootcamp | optional alternate PyTorch video explanation |
| SK | scikit-learn User Guide | pipelines; preprocessing; metrics; CV; tuning |
| PT | PyTorch Learn the Basics/Tutorials | tensors; datasets; models; autograd; optimisation; save/load; transfer learning; detection |
| CV | OpenCV University/official documentation | preprocessing; thresholding; morphology; contours; Hough methods |
| HF-L | Hugging Face LLM Course | tokenisation; padding; transformer classification; fine-tuning |
| HF-A | Hugging Face Audio Course | waveforms; preprocessing; classification; ASR; TTS |
| QWEN | Current official Qwen/Hugging Face documentation | local/offline inference; processors; quantisation; multimodality |
| IOAI | IOAI Academy Study Plan and official task repositories | competition workflow; decision under constraint; multimodal/open-ended tasks |

---

# A. General Computer Skills

| Syllabus item | Sessions | Required resource | Required evidence | Assessed in |
|---|---:|---|---|---|
| Python values, expressions, input/output | 3–4 | CS50P Functions/Variables; Exceptions; BML15 when aligned | trace tables, robust input program | Mock A/B Section B |
| Sequence, selection, iteration | 5–6 | CS50P Conditionals; Loops | boundary table, loop trace, frequency program | Mock A/B MCQ/code |
| Strings, lists, dictionaries, tuples | 6 | CS50P Loops/collections notes | collection-choice explanations and program | cold code trace |
| Functions | 3–4 | CS50P Functions | independent multi-function program | oral defence |
| Modules and packages | 7 | CS50P Libraries | imports and environment record | setup evidence |
| Files and CSV | 7, 39–40 | CS50P File I/O; Pandas/HML when aligned | CSV audit utility and report | Round 2 baseline |
| Exceptions and debugging | 4, 47 | CS50P Exceptions; PyTorch debug tasks | error log, traceback diagnosis | code-completion assessment |
| Sorting and searching | 8 | CS50 algorithms excerpt | paper traces and independent implementations | Round 1 mixed set |

# B. AI Foundations

| Syllabus item | Sessions | Resource | Required evidence | Assessment |
|---|---:|---|---|---|
| AI schools and Turing Test | 9 | BML15 + official syllabus; AIF optional | capability-claim evaluation | short answer |
| Ethics, bias, privacy, risk | 10 | BML15 + official syllabus; AIF optional | structured case analysis | Mock A/B Section D |
| Supervised learning | 11, 13–16 | BML15; MLS/MLCC/HML optional | task classification and baselines | all mocks/projects |
| Unsupervised learning | 11 | BML15; MLS optional | clustering/anomaly task design | concept assessment |
| Reinforcement learning | 12 | BML15; MLS Course 3 intro optional | environment/reward design | Round 1 concept question |
| Regression | 13–14 | BML15; HML/MLCC/MLS optional | paper calculations and sklearn model | Mock calculations/project |
| Classification | 15–16 | BML15; HML/MLCC/MLS optional | threshold table and logistic pipeline | Mock code/project |
| Clustering | 11 and extension project | BML15; MLS optional | cluster interpretation and limitations | oral defence |
| Probability/statistics/normal distribution | 17–18 | SQ; BML15 when aligned | hand calculations and functions | Mock calculations |
| Distance and standardisation | 18, 39 | SQ/NumPy | distance comparison raw/scaled | Round 1/2 |
| Accuracy, precision, recall, specificity, F1 | 19–20 | MLCC; HML; BML15 when aligned | confusion-matrix worksheet | Mock A/B |
| ROC/AUC and threshold choice | 20 | MLCC/SQ/HML | metric decision memo | multimodal mock |
| Cross-validation | 21, 44 | SK/HML | split design and CV report | Round 2 |
| Under/overfitting | 22–23 | BML15; HML/MLCC optional | curve diagnosis and controlled remedy | Mock short answer |
| Regularisation | 23 | BML15; HML/MLCC/MLS optional | controlled experiment | Round 1/2 |
| Decision trees | 24 | HML/MLS/SQ | impurity calculation and depth experiment | Mock A/B |
| Bagging/random forest | 25 | HML/MLS/SQ | single tree vs forest comparison | Mock short answer |
| Boosting | 26 | HML/MLS/SQ | three-model CV comparison | Mock B/model selection |
| Perceptron/neuron | 27 | LHY-ML or 3B1B | numerical neuron and XOR explanation | Round 1 |
| MLP/forward propagation | 28 | LHY-ML or 3B1B | full hand forward pass | Round 1 |
| Gradient descent/backpropagation | 29–30 | LHY-ML or 3B1B | computational-graph derivation | Mock A/B |
| Optimisers Adam/AdamW | 31 | LHY-ML/DLS/PT/DB-PT | controlled optimizer comparison | oral/implementation |
| CNN | 32–34 | LHY-ML/DLS/PT/DB-PT | convolution calculation and working CNN | Mock shapes/Round 2 |
| Activation, output, loss functions | 27, 33–34 | LHY-ML/3B1B/PT/DB-PT | role comparison and correct loss code | Round 1/PyTorch |
| LLM principles | 56–57 | HF-L/QWEN + official syllabus | structured-output tool and offline package | concept + Round 2 |
| Train/validation/test and cleaning | 21–23, 39–43 | BML15/MLCC/SK/HML | validation memo and pipeline | Round 2 gate |

# C. Advanced Computer Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| NumPy arrays and vectorisation | 39, 45 | NumPy/PT/HML | scaling utility and shape ledger | coding gate |
| Pandas data manipulation | 40–43 | Pandas/SK/HML | reproducible audit notebook | tabular mock |
| Matplotlib visualisation | 40, projects | Matplotlib/HML | labelled diagnostic figures | report rubric |
| Missing values and categories | 41, 43 | SK/HML | robust mixed-type pipeline | tabular mock |
| Feature engineering | 42 | HML/MLCC/teacher tasks | controlled before/after feature experiment | Round 2 |
| Windows, lags, moments | 42, 62 | teacher/IOAI task notes | leak-free feature table | AI4Science mock |
| Image augmentation | 49 | PT/torchvision/DB-PT | augmentation policy experiment | image project |
| Tokenisation and vocabulary | 51 | HF-L | collator and shape tests | NLP project |
| Embeddings | 42, 51–53 | MLCC/HF-L | embedding workflow explanation | oral defence |
| Image patching | 42, 57 | QWEN/multimodal docs | patch/sequence-length calculation | multimodal task |
| Reproducible notebook workflow | all coding sessions | official docs/HML/DB-PT | fresh-run evidence | notebook rubric |

# D. Advanced AI Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| PyTorch tensors/devices | 45 | PT/DB-PT | tensor audit utility | PyTorch gate |
| Dataset/DataLoader/nn.Module | 46 | PT/DB-PT | independent rebuild | PyTorch gate |
| Autograd/training loop | 46–47 | PT/DB-PT | full train/validate loop | Round 2 |
| CPU/GPU movement | 45–47 | PT/DB-PT | device-safe code | fresh-run check |
| Mixed precision | 47 | PT AMP | controlled AMP test or explanation | oral defence |
| Initialisation/batch normalisation | 31, 34, extension | LHY-ML/DLS/PT/DB-PT | architecture comparison | advanced extension |
| CNN/computer vision | 48–50 | LHY-ML/CV/PT/DB-PT | classical baseline + transfer model | image mock |
| Detection/segmentation | 50 | PT tutorial | IoU/error analysis | extension task |
| RNN/LSTM | 52 | LHY-ML/DLS/PT | sequence model and shape ledger | NLP reproduction |
| NLP/transformer classification | 51–53 | LHY-ML/HF-L | simple vs pretrained comparison | NLP project |
| Audio classification | 54–55 | HF-A | source-aware classifier | audio reproduction |
| ASR/TTS | 55 | HF-A | pipeline evaluation | domain task |
| Generative AI/LLM API | 56 | HF-L/current API docs | validated structured-output utility | Round 2 |
| Qwen local deployment | 57 | current QWEN docs + annual rules | offline smoke-test package | readiness gate |
| Multimodality | 57, 66 | QWEN/IOAI | text-only/image-only/fusion comparison | six-hour mock |
| Competition workflow | 1, 58–67 | IOAI/NOAI | validation memo, baseline, experiments, submissions | timed mocks |

---

# Assessment Coverage Matrix

| Assessment | Main competencies |
|---|---|
| Entry checks | retrieval, misconceptions, prerequisite readiness |
| Lesson worksheets | definitions, calculations, code tracing, scenario reasoning |
| Independent rebuilds | implementation without copying |
| Oral defence | conceptual ownership and AI-use accountability |
| Round 1 Mock A | broad A/B coverage, code, calculations, explanations |
| Round 1 Mock B | independent parallel form and reliability check |
| Tabular Mock | audit, group validation, pipeline, threshold, submission |
| Multimodal Mock | single-modality baselines, fusion, source stress tests, offline execution |
| Final conference | cold knowledge, code defence, reproducibility, time management |

# Maintenance Checklist Before Every Cohort

- [ ] download and archive the current official syllabus and rules;
- [ ] confirm Round 1/2 duration and permitted tools;
- [ ] confirm whether internet, APIs, AI assistants, and pretrained models are allowed;
- [ ] confirm package/runtime/GPU limits;
- [ ] verify every required resource link and access requirement;
- [ ] run every starter environment from a fresh account/runtime;
- [ ] regenerate mock datasets and keep hidden labels outside the student repository;
- [ ] confirm teacher-key repository is private;
- [ ] update the crosswalk when the official syllabus changes.
