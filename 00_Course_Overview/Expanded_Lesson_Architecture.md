# Expanded Lesson Architecture

This repository has moved beyond the original two-lesson-per-module skeleton into a dense NOAI/IOAI preparation curriculum bank.

## Current Architecture

- **155 mainline mission lessons** across Modules 00–26 and Module 28.
- **16 optional Bohrium resource lessons** in Module 27.
- **75-session recommended full competition pathway**: 67 core sessions plus eight competition-sprint sessions.

The lesson bank is intentionally larger than the scheduled pathway. Teachers select additional lessons for prerequisite repair, deeper practice, alternative explanations, domain extension, and stronger evidence.

## Design Rule

Each ordinary lesson follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

A module should not stop at two lessons unless it is only an orientation module. Most competition modules need **4–7 lessons**, and major assessment/sprint modules may require more.

## Round 1 A/B Lesson Density

| Module | Target lessons | Current role |
|---|---:|---|
| 01 Python foundations | 5–6 | syntax, functions, input/output, tracing, errors, code reading |
| 02 Control flow and data structures | 5–6 | branches, loops, strings, lists, dictionaries, tuples, nested structures |
| 03 Libraries, sorting, searching | 4–5 | modules, packages, files, documentation, sorting and searching |
| 04 Artificial-intelligence foundations and ethics | 4 | artificial-intelligence schools, Turing Test, bias, privacy, safety, responsibility |
| 05 Learning paradigms | 5–6 | supervised, unsupervised, reinforcement learning, task identification |
| 06 Linear regression | 4 | regression, loss, fitting, interpretation, paper calculations |
| 07 Logistic regression | 4 | classification, probability, threshold, decision boundary, misconceptions |
| 08 Statistics, probability, distance | 5 | distribution, mean, variance, standard deviation, distance, scaling |
| 09 Model evaluation | 5–6 | confusion matrix, precision, recall, F1, ROC/AUC, cross-validation, metric choice |
| 10 Generalisation and regularisation | 4 | underfitting, overfitting, regularisation, validation curves |
| 11 Trees and ensembles | 4 | decision trees, impurity, bagging, random forest, boosting |
| 12 Neural-network foundations | 5–6 | perceptron, multilayer perceptron, activations, loss, forward pass, parameter count |
| 13 Backpropagation and optimisation | 5–6 | gradient descent, backpropagation, Adam/AdamW, convergence, training-cycle reasoning |
| 14 Convolutional-neural-network foundations | 5–6 | convolution, pooling, shape calculation, architecture, output functions |
| 15 Round 1 exam training | 8–10 | multiple choice, distractors, code tracing, calculations, short answers, mocks, correction |

## Round 2 C/D Lesson Density

| Module | Target lessons | Current role |
|---|---:|---|
| 16 NumPy, Pandas, and Matplotlib | 6 | arrays, DataFrames, grouping, missing values, visualisation, reporting |
| 17 Data cleaning and feature engineering | 6 | cleaning, leakage, encoding, scaling, windows/lags, domain features |
| 18 Scikit-learn workflow | 6 | split, baseline, Pipeline, ColumnTransformer, cross-validation, tuning, submission |
| 19 PyTorch foundations | 7 | tensors, devices, Dataset, DataLoader, nn.Module, autograd, loops, checkpoints |
| 20 Computer vision | 6 | image arrays, preprocessing, augmentation, convolutional neural networks, transfer learning, error analysis |
| 21 Natural-language processing and sequence models | 6 | tokenisation, vocabulary, padding, recurrent neural networks, long short-term memory networks, Transformers |
| 22 Audio and speech | 5 | waveform, spectrogram, Mel features, classification, automatic speech recognition, text-to-speech |
| 23 Large language models and multimodality | 5 | prompting, API use, Qwen/local models, multimodal inputs, verification |
| 24 Round 2 project workflow | 6–8 | task reading, baseline, validation, experiments, ablation, prompt log, submission |
| 25 Past-paper reproduction | 4 | reproduce official tasks, compare approaches, write postmortems |
| 26 Timed mock contests | 4–5 | Round 1 and Round 2 simulations, correction, final readiness |

## Competition Sprint Density

| Module | Target lessons | Current role |
|---|---:|---|
| 28 Competition sprint: task recognition, data engineering, and hyperparameter tuning | 8 | unfamiliar-task recognition, baseline/metric choice, data audit, leakage prevention, feature engineering, classical tuning, deep-learning tuning, PyTorch/Optuna tuning, full sprint simulation |

Module 28 is a late-stage integration chapter. It does not replace foundational modules and should not be assigned before students can already build a valid baseline.

## Bohrium Resource Hub

Module 27 contains:

- two full-video hub missions;
- fourteen 70-minute lessons for 北京市十一学校《中学机器学习十五讲》.

It is a resource hub and is not automatically added to the scheduled pathway.

## Current Implementation Rule

1. Maintain module READMEs and lesson links together.
2. Keep one exact required resource segment per ordinary lesson.
3. Preserve the classroom flow and evidence requirement.
4. Keep the 75-session scheduled pathway separate from the 155-lesson mainline bank.
5. Use optional lessons only when evidence justifies reteaching or extension.
6. Run link, notebook, script, and runtime validation after meaningful changes.
7. Keep answer keys, hidden labels, private test data, and scored-assessment packages outside the public repository.
8. Recheck official rules, package versions, model permissions, and platform constraints before every cohort.

## Non-Negotiable Rule

A dense lesson bank is useful only when the teacher can identify what is required, selected, optional, or a resource-hub alternative. Do not return to a two-lesson-per-module skeleton, and do not automatically schedule every available lesson.