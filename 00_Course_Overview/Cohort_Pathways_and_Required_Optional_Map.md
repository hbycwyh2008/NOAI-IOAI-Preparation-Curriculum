# Cohort Pathways and Required / Optional Map

This repository is a **curriculum bank**, not a requirement that every cohort complete every lesson file.

## Current Size

- **155 mainline mission lessons** across Modules 00–26 and Module 28.
- **16 Bohrium resource lessons** in Module 27: two full-video hub missions plus the fourteen-session 70-minute sequence for 北京市十一学校《中学机器学习十五讲》.
- **171 total student-facing mission/resource lesson files** when the optional Bohrium hub is included.

The recommended competition pathway is **75 scheduled sessions**:

```text
67-session core pathway
+ 8-session competition sprint
= 75-session full competition pathway
```

The remaining mission files provide reteaching, deeper practice, alternative resources, domain extensions, and additional evidence opportunities.

## Pathway 1 — NOAI Round 1 Preparation

**Recommended core:** Sessions 1–38 from `Detailed_Lesson_Sequence.md`.

Main modules:

- `00-course-overview`
- `01-python-foundations`
- `02-control-flow-and-data-structures`
- `03-libraries-sorting-searching`
- `04-ai-foundations-and-ethics`
- `05-learning-paradigms`
- `06-linear-regression`
- `07-logistic-regression`
- `08-statistics-probability-distance`
- `09-model-evaluation`
- `10-generalization-regularization`
- `11-trees-and-ensembles`
- `12-neural-network-foundations`
- `13-backprop-optimization`
- `14-cnn-foundations`
- `15-round-1-exam-training`

### Required resources

- Harvard CS50’s Introduction to Programming with Python on edX.
- 北京市十一学校《中学机器学习十五讲》 on Bohrium.
- Current official NOAI syllabus, rules, and task materials.

### Selected support resources

- Machine Learning Specialization on Coursera.
- Deep Learning Specialization on Coursera.
- StatQuest.
- 3Blue1Brown Neural Networks.
- Google Machine Learning Crash Course.
- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.

### Exit gate

Students should be able to:

1. trace and complete Python code without an interpreter;
2. identify the task type, input, output, label, and metric;
3. complete core calculations for regression, classification metrics, trees, neural networks, and convolutional shapes;
4. explain common distractors and misconceptions;
5. complete a timed Round 1 mock and correction cycle.

## Pathway 2 — Full NOAI Round 1 and Round 2 Preparation

**Recommended core:** Sessions 1–67 from `Detailed_Lesson_Sequence.md`.

Add these modules after the Round 1 foundation:

- `16-numpy-pandas-matplotlib`
- `17-data-cleaning-feature-engineering`
- `18-sklearn-workflow`
- `19-pytorch-foundations`
- `20-computer-vision`
- `21-nlp-sequence-models`
- `22-audio-speech`
- `23-llm-generative-ai`
- `24-round-2-project-training`
- `25-past-paper-reproduction`
- `26-mock-contests`

### Required implementation resources

- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.
- scikit-learn User Guide.
- Course 1 — PyTorch: Fundamentals.
- Course 2 — PyTorch: Techniques and Ecosystem Tools.
- PyTorch official tutorials.
- NumPy, Pandas, Matplotlib, OpenCV, torchvision, Hugging Face, and Qwen official documentation as the task requires.
- Current official NOAI and IOAI task repositories.

### Exit gate

Students should be able to:

1. audit an unfamiliar dataset;
2. create a valid train/validation strategy without leakage;
3. build and verify the simplest valid baseline;
4. implement a reproducible scikit-learn or PyTorch pipeline;
5. run a controlled experiment and error analysis;
6. validate a submission file and execute from a fresh runtime;
7. complete a timed Round 2 simulation.

## Pathway 3 — Competition Sprint

**Recommended core:** Sessions 68–75, corresponding to Module 28.

Module:

- `28-competition-sprint-task-data-tuning`

Sequence:

```text
Task recognition
→ baseline and metric selection
→ data audit and validation
→ data cleaning and feature engineering
→ classical machine-learning tuning
→ deep-learning tuning
→ PyTorch schedulers and automated tuning
→ full sprint simulation
```

Students enter this pathway only after they can already build a valid baseline.

### Required tuning resources

- Course 2 — Advanced Learning Algorithms, Week 3: Advice for Applying Machine Learning.
- Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization.
- Course 2 — PyTorch: Techniques and Ecosystem Tools, Module 1: Hyperparameter Optimization.
- `02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md`.

### Exit gate

Students should be able to identify the highest-value next experiment instead of tuning randomly, maintain an experiment log, stop unproductive searches, and reserve enough time for error analysis, fresh-runtime execution, and submission validation.

## Pathway 4 — IOAI Advanced Extension

This is not a fixed session count. Select lessons according to the student’s readiness and the target task.

Recommended extensions:

- additional lessons from Modules 20–23;
- official IOAI tasks and academy materials;
- Course 3 — PyTorch: Advanced Architectures and Deployment;
- advanced transfer learning, multimodal, small-data, semi-supervised, generated-data, and model-efficiency tasks;
- additional past-paper reproductions and six-hour simulations;
- selected Module 27 Bohrium resource lessons when conceptual reinforcement is needed.

## Required, Selected, and Optional Meanings

| Label | Meaning |
|---|---|
| Required | Necessary for the stated pathway and its exit gate. |
| Selected | Teacher assigns only the exact module, chapter, video, or task needed for the lesson. |
| Optional | Used for reteaching, enrichment, an alternative explanation, or an advanced extension. |
| Resource hub | Supports other modules and is not automatically added to the scheduled lesson count. |

## Teacher Scheduling Rule

Before the cohort begins, create a schedule that identifies:

1. the chosen pathway;
2. required lessons;
3. optional lessons reserved for reteaching or extension;
4. assessment gates;
5. long simulations that do not fit the ordinary 75-minute period;
6. the exact required resource segment for each lesson;
7. the contingency plan when a student fails an entry or phase gate.

Do not schedule all 171 lesson files automatically. Assign the shortest pathway that still reaches the required competition standard, then add lessons based on evidence.