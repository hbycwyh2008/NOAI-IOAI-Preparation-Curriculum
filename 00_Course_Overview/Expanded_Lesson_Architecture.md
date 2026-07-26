# Expanded Lesson Architecture

This file upgrades the curriculum from a thin two-lesson-per-module skeleton into a dense NOAI/IOAI preparation sequence.

The old structure was useful as a map, but it was not sufficient for actual teaching. A serious NOAI/IOAI preparation curriculum must provide enough lessons for concept formation, paper-test practice, coding practice, independent rebuild, and timed evidence.

## Design Rule

Each normal lesson must still follow the classroom flow:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

A module should not stop at two lessons unless it is only an orientation module. Most competition modules need **4–7 lessons**.

## Round 1 A/B Lesson Density

| Module | Minimum lessons | Reason |
|---|---:|---|
| 01 Python foundations | 5–6 | Python syntax, functions, input/output, tracing, errors, code reading |
| 02 Control flow and data structures | 5–6 | Branches, loops, strings, lists, dictionaries, tuples, nested structures |
| 03 Libraries, sorting, searching | 4–5 | Modules, packages, files, sorting/searching, documentation use |
| 04 AI foundations and ethics | 4 | AI schools, Turing Test, data/privacy/bias/responsibility, case reasoning |
| 05 Learning paradigms | 5–6 | Supervised, unsupervised, reinforcement learning, task identification, BML15 bridge |
| 06 Linear regression | 4 | Regression concept, loss, fitting, interpretation, paper calculations |
| 07 Logistic regression | 4 | Classification, probability, threshold, decision boundary, misconceptions |
| 08 Statistics, probability, distance | 5 | Distribution, mean/variance/std, residual/bias, distance, scaling |
| 09 Model evaluation | 5 | Confusion matrix, precision, recall, F1, cross-validation, metric choice |
| 10 Generalization and regularization | 4 | Underfitting, overfitting, regularization, validation curves |
| 11 Trees and ensembles | 4 | Decision tree, impurity/entropy, bagging/random forest, boosting |
| 12 Neural network foundations | 5 | Perceptron, MLP, activations, loss, forward pass, parameter count |
| 13 Backprop and optimization | 5 | Gradient descent, backprop, Adam/AdamW, local/global optimum, training loop concept |
| 14 CNN foundations | 5 | Convolution, pooling, fully connected layers, shape calculation, CNN explanation |
| 15 Round 1 exam training | 8–10 | MCQ, distractors, code tracing, short answer, calculations, timed mocks, correction |

## Round 2 C/D Lesson Density

| Module | Minimum lessons | Reason |
|---|---:|---|
| 16 NumPy/Pandas/Matplotlib | 6 | Arrays, dataframe operations, grouping, missing values, visualization, reporting |
| 17 Data cleaning and feature engineering | 6 | Cleaning, leakage, encoding, scaling, windows/lags, domain features |
| 18 sklearn workflow | 6 | Split, baseline, pipeline, CV, tuning, submission, LHY bridge |
| 19 PyTorch foundations | 7 | Tensor, device, Dataset, DataLoader, nn.Module, autograd, loop, checkpoint, mixed precision |
| 20 Computer vision | 6 | Image arrays, augmentation, CNN, transfer learning, error analysis, submission |
| 21 NLP and sequence models | 6 | Tokenization, vocabulary, padding, RNN/LSTM, classification, evaluation |
| 22 Audio and speech | 5 | Waveform, spectrogram, Mel features, audio classification, ASR/TTS awareness |
| 23 LLM and multimodality | 5 | Prompting, API use, Qwen/local model awareness, multimodal inputs, verification |
| 24 Round 2 project workflow | 6–8 | Task reading, baseline, validation, ablation, prompt log, leaderboard submission |
| 25 Past-paper reproduction | 4 | Reproduce official tasks, compare solution paths, write postmortems |
| 26 Timed mock contests | 4–5 | 2h paper mock, 6h practice mock, A/B leaderboard mock, correction conference |

## Implementation Order

1. Expand module README files into realistic lesson sequences.
2. Create concrete lesson files for the most important new lessons.
3. Keep the full classroom flow in every normal lesson.
4. Add worksheets and starter notebooks only after lesson outcomes are stable.
5. Keep teacher keys and scoring rubrics outside the public student-facing repo.

## Non-Negotiable Rule

A module with only two lessons should be treated as incomplete unless it is an orientation-only module. The target state is a dense, teachable sequence where students repeatedly learn, practise, rebuild, and submit evidence.
