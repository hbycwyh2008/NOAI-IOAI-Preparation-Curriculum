# Resource Map and NOAI Syllabus Crosswalk

This document maps the 2026 NOAI China A–D syllabus structure to the 67 teaching sessions, required resources, student evidence, and major assessments. Resource titles are deliberately used instead of fragile timestamps. The teacher must verify URLs, access terms, annual competition rules, model restrictions, and package availability before each cohort begins.

## Resource Selection Rules

1. One required resource segment per ordinary lesson.
2. Students use only the named chapter/module, not an entire playlist during class.
3. Official documentation replaces videos for APIs that change frequently.
4. A resource is not evidence; the worksheet, independent task, and oral defence are evidence.
5. Annual NOAI/IOAI rules override this repository, especially for internet access, pretrained models, package versions, local deployment, and AI-assistant use.

## Primary Resource Index

| Code | Resource | Assigned scope |
|---|---|---|
| CS50P | Harvard CS50's Introduction to Programming with Python | Functions/Variables; Conditionals; Loops; Exceptions; Libraries; File I/O |
| AIF | DeepLearning.AI AI for Everyone | What AI Can/Cannot Do; AI and Society |
| MLS | DeepLearning.AI Machine Learning Specialization | supervised/unsupervised/RL; regression; classification; trees/ensembles |
| MLCC | Google Machine Learning Crash Course | linear/logistic regression; classification metrics; generalisation; overfitting; numerical/categorical data |
| SQ | StatQuest | statistics; normal distribution; metrics; trees/ensembles clarification |
| 3B1B | 3Blue1Brown Neural Networks | neural-network intuition; gradient descent; backpropagation calculus |
| DLS | Deep Learning Specialization | optimisation; CNN operations; sequence models |
| SK | scikit-learn User Guide | pipelines; preprocessing; metrics; CV; tuning |
| PT | PyTorch Learn the Basics/Tutorials | tensors; datasets; models; autograd; optimisation; save/load; transfer learning; detection |
| CV | OpenCV University/official documentation | preprocessing; thresholding; morphology; contours; Hough methods |
| HF-L | Hugging Face LLM Course | tokenisation; padding; transformer classification; fine-tuning |
| HF-A | Hugging Face Audio Course | waveforms; preprocessing; classification; ASR; TTS |
| QWEN | Current official Qwen/Hugging Face documentation | local/offline inference; processors; quantisation; multimodality |
| IOAI | IOAI Academy Study Plan and official task repositories | competition workflow; decision under constraint; multimodal/open-ended tasks |
| NOAI | Current official NOAI handbook, FAQ, syllabus, and authorised task repositories | format, annual rules, past tasks, allowed environment |

---

# A. General Computer Skills

| Syllabus item | Sessions | Required resource | Required evidence | Assessed in |
|---|---:|---|---|---|
| Python values, expressions, input/output | 3–4 | CS50P Functions/Variables; Exceptions | trace tables, robust input program | Mock A/B Section B |
| Sequence, selection, iteration | 5–6 | CS50P Conditionals; Loops | boundary table, loop trace, frequency program | Mock A/B MCQ/code |
| Strings, lists, dictionaries, tuples | 6 | CS50P Loops/collections notes | collection-choice explanations and program | cold code trace |
| Functions | 3–4 | CS50P Functions | independent multi-function program | oral defence |
| Modules and packages | 7 | CS50P Libraries | imports and environment record | setup evidence |
| Files and CSV | 7, 39–40 | CS50P File I/O; Pandas tutorials | CSV audit utility and report | Round 2 baseline |
| Exceptions and debugging | 4, 47 | CS50P Exceptions; PyTorch debug tasks | error log, traceback diagnosis | code-completion assessment |
| Sorting and searching | 8 | CS50 algorithms excerpt | paper traces and independent implementations | Round 1 mixed set |

# B. AI Foundations

| Syllabus item | Sessions | Resource | Required evidence | Assessment |
|---|---:|---|---|---|
| AI schools and Turing Test | 9 | AIF + official syllabus | capability-claim evaluation | short answer |
| Ethics, bias, privacy, risk | 10 | AIF AI and Society | structured case analysis | Mock A/B Section D |
| Supervised learning | 11, 13–16 | MLS/MLCC | task classification and baselines | all mocks/projects |
| Unsupervised learning | 11 | MLS | clustering/anomaly task design | concept assessment |
| Reinforcement learning | 12 | MLS Course 3 intro | environment/reward design | Round 1 concept question |
| Regression | 13–14 | MLCC/MLS | paper calculations and sklearn model | Mock calculations/project |
| Classification | 15–16 | MLCC/MLS | threshold table and logistic pipeline | Mock code/project |
| Clustering | 11 and extension project | MLS | cluster interpretation and limitations | oral defence |
| Probability/statistics/normal distribution | 17–18 | SQ | hand calculations and functions | Mock calculations |
| Distance and standardisation | 18, 39 | SQ/NumPy | distance comparison raw/scaled | Round 1/2 |
| Accuracy, precision, recall, specificity, F1 | 19–20 | MLCC | confusion-matrix worksheet | Mock A/B |
| ROC/AUC and threshold choice | 20 | MLCC/SQ | metric decision memo | multimodal mock |
| Cross-validation | 21, 44 | SK | split design and CV report | Round 2 |
| Under/overfitting | 22–23 | MLCC | curve diagnosis and controlled remedy | Mock short answer |
| Regularisation | 23 | MLCC/MLS | controlled experiment | Round 1/2 |
| Decision trees | 24 | MLS/SQ | impurity calculation and depth experiment | Mock A/B |
| Bagging/random forest | 25 | MLS/SQ | single tree vs forest comparison | Mock short answer |
| Boosting | 26 | MLS/SQ | three-model CV comparison | Mock B/model selection |
| Perceptron/neuron | 27 | 3B1B | numerical neuron and XOR explanation | Round 1 |
| MLP/forward propagation | 28 | 3B1B | full hand forward pass | Round 1 |
| Gradient descent/backpropagation | 29–30 | 3B1B | computational-graph derivation | Mock A/B |
| Optimisers Adam/AdamW | 31 | DLS/PT | controlled optimizer comparison | oral/implementation |
| CNN | 32–34 | DLS/PT | convolution calculation and working CNN | Mock shapes/Round 2 |
| Activation, output, loss functions | 27, 33–34 | 3B1B/PT | role comparison and correct loss code | Round 1/PyTorch |
| LLM principles | 56–57 | HF-L/QWEN | structured-output tool and offline package | concept + Round 2 |
| Train/validation/test and cleaning | 21–23, 39–43 | MLCC/SK | validation memo and pipeline | Round 2 gate |

# C. Advanced Computer Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| NumPy arrays and vectorisation | 39, 45 | NumPy/PT | scaling utility and shape ledger | coding gate |
| Pandas data manipulation | 40–43 | Pandas/SK | reproducible audit notebook | tabular mock |
| Matplotlib visualisation | 40, projects | Matplotlib | labelled diagnostic figures | report rubric |
| Missing values and categories | 41, 43 | SK | robust mixed-type pipeline | tabular mock |
| Feature engineering | 42 | MLCC/teacher tasks | controlled before/after feature experiment | Round 2 |
| Windows, lags, moments | 42, 62 | teacher/IOAI task notes | leak-free feature table | AI4Science mock |
| Image augmentation | 49 | PT/torchvision | augmentation policy experiment | image project |
| Tokenisation and vocabulary | 51 | HF-L | collator and shape tests | NLP project |
| Embeddings | 42, 51–53 | MLCC/HF-L | embedding workflow explanation | oral defence |
| Image patching | 42, 57 | QWEN/multimodal docs | patch/sequence-length calculation | multimodal task |
| Reproducible notebook workflow | all coding sessions | official docs | fresh-run evidence | notebook rubric |

# D. Advanced AI Skills

| Syllabus item | Sessions | Resource | Evidence | Assessment |
|---|---:|---|---|---|
| PyTorch tensors/devices | 45 | PT Tensors | tensor audit utility | PyTorch gate |
| Dataset/DataLoader/nn.Module | 46 | PT Basics | independent rebuild | PyTorch gate |
| Autograd/training loop | 46–47 | PT Autograd/Optimization | full train/validate loop | Round 2 |
| CPU/GPU movement | 45–47 | PT | device-safe code | fresh-run check |
| Mixed precision | 47 | PT AMP | controlled AMP test or explanation | oral defence |
| Initialisation/batch normalisation | 31, 34, extension | DLS/PT | architecture comparison | advanced extension |
| CNN/computer vision | 48–50 | CV/PT | classical baseline + transfer model | image mock |
| Detection/segmentation | 50 | PT tutorial | IoU/error analysis | extension task |
| RNN/LSTM | 52 | DLS/PT | sequence model and shape ledger | NLP reproduction |
| NLP/transformer classification | 51–53 | HF-L | simple vs pretrained comparison | NLP project |
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