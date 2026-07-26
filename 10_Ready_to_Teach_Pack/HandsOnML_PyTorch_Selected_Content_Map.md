# Hands-On ML and PyTorch Selected Content Map

This file clarifies how two practical resources are used in the NOAI / IOAI preparation curriculum:

1. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** by Aurélien Géron.
2. **Learn PyTorch for Deep Learning / PyTorch for Deep Learning Bootcamp: Zero to Mastery** by Daniel Bourke / Zero to Mastery.

The purpose is not to make students complete both resources end-to-end. The purpose is to select the parts that directly strengthen NOAI Round 2 C/D and IOAI-style applied problem solving.

## Resource Codes

| Code | Resource | Main use |
|---|---|---|
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | practical sklearn workflow, data pipelines, evaluation, model comparison, trees/ensembles, end-to-end project habits |
| DB-PT | Daniel Bourke / Zero to Mastery Learn PyTorch for Deep Learning | PyTorch implementation practice: tensors, datasets, dataloaders, nn.Module, training loops, vision transfer learning |
| JP-PT | Jose Portilla PyTorch / Deep Learning Bootcamp | optional backup video resource if a student needs a slower alternate explanation |

## Important Boundary

Hands-On Machine Learning is useful in this repo mainly for **Scikit-learn, end-to-end ML workflow, evaluation, and practical model iteration**.

It is not the main PyTorch resource. PyTorch implementation should use:

1. official PyTorch tutorials;
2. Daniel Bourke / Zero to Mastery Learn PyTorch for Deep Learning;
3. teacher starter notebooks;
4. NOAI / IOAI-style project tasks.

## HML Selected Placement

| HML topic | Repo placement | Lesson use |
|---|---|---|
| End-to-end ML project workflow | `18-sklearn-workflow/`, `24-round-2-project-training/` | task reading, data audit, baseline, validation, submission report |
| Data cleaning and preprocessing | `16-numpy-pandas-matplotlib/`, `17-data-cleaning-feature-engineering/` | missing values, categories, scaling, leakage-safe transformations |
| sklearn pipelines | `18-sklearn-workflow/lesson-04-columntransformer-pipeline-leakage.md` | ColumnTransformer, Pipeline, reproducibility |
| Model evaluation and cross-validation | `09-model-evaluation/`, `18-sklearn-workflow/` | metric decision, CV design, validation memo |
| Linear and logistic regression | `06-linear-regression/`, `07-logistic-regression/` | practical comparison after paper calculations |
| Trees, random forests, boosting | `11-trees-and-ensembles/` | impurity, ensemble comparison, model-selection evidence |
| Error analysis and iteration | `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md` | ablation, controlled experiments, postmortem |

Approximate HML-supported mainline use: **18–25 lessons**, mostly in Round 2 C/D and selected Round 1 ML modules.

## DB-PT Selected Placement

| PyTorch topic | Repo placement | Lesson use |
|---|---|---|
| Tensor basics and shapes | `19-pytorch-foundations/lesson-01.md` | tensor audit, shape ledger, dtype/device checks |
| Dataset and DataLoader | `19-pytorch-foundations/lesson-02.md` | dataset class, batching, train/validation split |
| nn.Module and forward pass | `19-pytorch-foundations/lesson-02.md`, `19-pytorch-foundations/lesson-05-model-class-rebuild.md` | model rebuild without copying |
| Autograd and training loop | `19-pytorch-foundations/lesson-03.md`, `19-pytorch-foundations/lesson-06-training-loop-debugging.md` | forward, loss, backward, optimiser, validation |
| Computer vision workflow | `20-computer-vision/lesson-02.md`, `20-computer-vision/lesson-05-transfer-learning-finetuning.md` | CNN baseline, transfer learning, augmentation decisions |
| Experiment tracking and error analysis | `20-computer-vision/lesson-06-image-error-analysis-submission.md`, `24-round-2-project-training/` | evidence-driven model improvement |

Approximate DB-PT-supported mainline use: **8–12 lessons**, mainly in PyTorch foundations and computer vision.

## When to Use HML vs DB-PT

| Teaching need | Use |
|---|---|
| sklearn pipeline, preprocessing, cross-validation, model comparison | HML + sklearn User Guide |
| tabular Round 2 baseline | HML + sklearn User Guide |
| PyTorch tensors, Dataset, DataLoader, nn.Module | DB-PT + PyTorch official tutorials |
| CNN / transfer-learning implementation | DB-PT + PyTorch/torchvision tutorials |
| error analysis and competition iteration | HML + DB-PT + NOAI/IOAI task notes |

## Student Instruction

Students should not passively watch long videos or copy notebook code. For every selected HML or DB-PT resource, students must produce:

1. a guided-notes section;
2. an Entry Check response;
3. a Core Pattern statement;
4. a Guided Practice artifact;
5. an Independent Rebuild artifact;
6. evidence of a fresh run when code is involved;
7. an AI-use note when AI assistance was used.

## Recommended Mainline

For most students, use this order:

1. BML15 for Round 1 A/B concept formation.
2. HML selected chapters for sklearn and practical ML workflow.
3. DB-PT selected lessons for PyTorch implementation.
4. PyTorch official tutorials for API correctness.
5. Hugging Face and Qwen resources for NLP, LLM, audio, and multimodal extension.
6. NOAI / IOAI official tasks for timed reproduction and competition readiness.
