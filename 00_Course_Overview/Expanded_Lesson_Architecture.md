# Expanded Lesson Architecture

This repository has moved beyond the original two-lesson-per-module skeleton into a dense NOAI/IOAI preparation curriculum with a separate scheduled pathway and reusable lesson bank.

## Current Architecture

- **78-session canonical pathway** across nine dependency-based phases.
- **Eight scheduled AI History seminars** in Sessions 33–40.
- **155 mainline mission lessons** across reusable Modules 00–26 and Module 28.
- **16 Bohrium resource lessons** in reusable Module 27.
- **171 reusable public lesson/resource files** in `_Lesson_Library`.

The reusable bank is intentionally larger than the scheduled pathway. Teachers select additional lessons for prerequisite repair, deeper practice, alternative explanations, domain extension, and stronger evidence.

## Scheduled Pathway

| Phase | Sessions | Role |
|---:|---:|---|
| 0 | 1–2 | orientation and evidence |
| 1 | 3–12 | CS50P Python |
| 2 | 13–18 | NumPy, Pandas, and visualisation |
| 3 | 19–32 | Bohrium ML foundations |
| 4 | 33–40 | AI History and Thinking Humans |
| 5 | 41–58 | Andrew Ng ML, mathematics intuition, embedded Kaggle practice, and model labs |
| 6 | 59–70 | Andrew Ng DL, PyTorch, and domain tasks |
| 7 | 71–74 | model comparison, EDA, feature engineering, and evaluation |
| 8 | 75–78 | tuning, ensembling, full simulation, and postmortem |

## Design Rule

Each ordinary lesson follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

A module should not stop at two lessons unless it is only an orientation module. Most competition modules need **4–7 lessons**, and major assessment or project modules may require more.

The fourteen Bohrium lessons and eight AI History seminars use named 70-minute exceptions. Long mocks and reproductions use competition-realistic durations.

## Round 1 and Foundations Bank

| Module | Target lessons | Current role |
|---|---:|---|
| 01 Python foundations | 5–6 | syntax, functions, input/output, tracing, errors, code reading |
| 02 Control flow and data structures | 5–6 | branches, loops, strings, lists, dictionaries, tuples, nested structures |
| 03 Libraries, sorting, searching | 4–5 | modules, packages, files, documentation, sorting and searching |
| 04 Artificial-intelligence foundations and ethics | 4 | AI schools, Turing test, bias, privacy, safety, responsibility |
| 05 Learning paradigms | 5–6 | supervised, unsupervised, reinforcement learning, task identification |
| 06 Linear regression | 4 | regression, loss, fitting, interpretation, paper calculations |
| 07 Logistic regression | 4 | classification, probability, threshold, decision boundary, misconceptions |
| 08 Statistics, probability, distance | 5 | distribution, mean, variance, standard deviation, distance, scaling |
| 09 Model evaluation | 5–6 | confusion matrix, precision, recall, F1, ROC-AUC, cross-validation, metric choice |
| 10 Generalisation and regularisation | 4 | underfitting, overfitting, regularisation, validation curves |
| 11 Trees and ensembles | 4 | decision trees, impurity, bagging, random forest, boosting |
| 12 Neural-network foundations | 5–6 | perceptron, MLP, activations, loss, forward pass, parameter count |
| 13 Backpropagation and optimisation | 5–6 | gradient descent, backpropagation, Adam/AdamW, convergence, training-cycle reasoning |
| 14 CNN foundations | 5–6 | convolution, pooling, shape calculation, architecture, output functions |
| 15 Round 1 exam training | 8–10 | multiple choice, distractors, code tracing, calculations, short answers, mocks, correction |

## Round 2 and Domain Bank

| Module | Target lessons | Current role |
|---|---:|---|
| 16 NumPy, Pandas, and Matplotlib | 6 | arrays, DataFrames, grouping, missing values, visualisation, reporting |
| 17 Data cleaning and feature engineering | 6 | cleaning, leakage, encoding, scaling, windows/lags, domain features |
| 18 Scikit-learn workflow | 6 | split, baseline, Pipeline, ColumnTransformer, cross-validation, tuning, submission |
| 19 PyTorch foundations | 7 | tensors, devices, Dataset, DataLoader, nn.Module, autograd, loops, checkpoints |
| 20 Computer vision | 6 | image arrays, preprocessing, augmentation, CNNs, transfer learning, error analysis |
| 21 NLP and sequence models | 6 | tokenisation, vocabulary, padding, RNN, LSTM, Transformers |
| 22 Audio and speech | 5 | waveform, spectrogram, Mel features, classification, ASR, TTS |
| 23 Large language models and multimodality | 5 | prompting, local/API models, multimodal inputs, verification |
| 24 Round 2 project workflow | 6–8 | task reading, baseline, validation, experiments, ablation, prompt log, submission |
| 25 Past-paper reproduction | 4 | reproduce official tasks, compare approaches, write postmortems |
| 26 Timed mock contests | 4–5 | Round 1 and Round 2 simulations, correction, final readiness |

## Competition Integration Bank

| Module | Target lessons | Current role |
|---|---:|---|
| 28 Competition sprint | 8 | task recognition, data audit, leakage prevention, feature engineering, classical tuning, deep-learning tuning, ensembling, full sprint simulation |

Module 28 is a late-stage reusable integration chapter. It does not replace foundational modules and is not automatically scheduled after Session 78.

## Bohrium Resource Hub

Module 27 contains:

- two full-video hub missions;
- fourteen 70-minute lessons for 北京市十一学校《中学机器学习十五讲》.

The fourteen-lesson sequence supplies Phase 3. The two full-video missions remain optional resource alternatives.

## Current Implementation Rule

1. Maintain canonical phase navigation and reusable lesson READMEs separately.
2. Keep one exact required resource segment or reading assignment per ordinary lesson.
3. Preserve classroom flow and evidence requirements.
4. Keep the 78-session scheduled pathway separate from the 171-file reusable bank.
5. Treat Phase 04 as eight scheduled reading seminars with a teacher pack, evidence template, rubric, and pilot gate.
6. Use Kaggle only as embedded Andrew ML practice.
7. Use optional lessons only when evidence justifies reteaching or extension.
8. Run structure, readiness-contract, link, notebook, starter-code, and runtime validation after meaningful changes.
9. Keep answer keys, hidden labels, private tests, secure scoring, and calibration examples outside the public repository.
10. Recheck official rules, package versions, model permissions, resource access, and platform constraints before every cohort.

## Non-Negotiable Rule

A dense lesson bank is useful only when the teacher can identify what is required, selected, optional, or a resource alternative. Do not return to a two-lesson-per-module skeleton, do not reintroduce a standalone Kaggle phase, and do not automatically schedule every available lesson.
