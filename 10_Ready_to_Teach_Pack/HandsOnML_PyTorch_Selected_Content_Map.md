# Hands-On ML and DeepLearning.AI PyTorch Selected Content Map

This file clarifies how two practical resources are used in the NOAI / IOAI preparation curriculum:

1. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** by Aurélien Géron.
2. **PyTorch for Deep Learning Professional Certificate** by DeepLearning.AI on Coursera, taught by Laurence Moroney.

The purpose is not to make students complete both resources end-to-end. The purpose is to select the parts that directly strengthen NOAI Round 2 C/D and IOAI-style applied problem solving.

## Resource Codes

| Code | Resource | Coursera / source link | Main use |
|---|---|---|---|
| HML | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | https://github.com/ageron/handson-ml3 | sklearn workflow, data pipelines, evaluation, model comparison, trees/ensembles, end-to-end project habits |
| DLAI-PT | DeepLearning.AI PyTorch for Deep Learning Professional Certificate | https://www.coursera.org/professional-certificates/pytorch-for-deep-learning | PyTorch tensors, datasets, dataloaders, neural networks, training pipelines, transfer learning, vision, NLP, optimisation, and selected deployment topics |
| DLAI-PT1 | PyTorch: Fundamentals | https://www.coursera.org/learn/pytorch-fundamentals | required PyTorch foundation course for the selected repo lessons |
| DLAI-PT2 | PyTorch: Techniques and Ecosystem Tools | https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools | selected transfer learning, TorchVision, Hugging Face, tuning, and efficient training content |
| DLAI-PT3 | PyTorch: Advanced Architectures and Deployment | https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment | optional advanced extension: architectures, Transformers, compression, export, and deployment |
| PT | PyTorch official tutorials | https://docs.pytorch.org/tutorials/ | current API reference and implementation verification |

## Important Boundary

Hands-On Machine Learning is used mainly for **scikit-learn, end-to-end ML workflow, evaluation, and practical model iteration**.

The DeepLearning.AI PyTorch certificate is the repo's main structured PyTorch video/course series. PyTorch official tutorials remain the source of truth for current APIs.

Students do not need to complete the entire three-course certificate before competing. The teacher assigns selected modules that match the repo lesson targets.

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

## DLAI-PT Course 1 — PyTorch: Fundamentals

**Status:** selected mainline resource.

| Topic | Repo placement | Lesson use |
|---|---|---|
| Tensors, tensor math, broadcasting | `19-pytorch-foundations/lesson-01.md` | tensor audit, shape ledger, dtype/device reasoning |
| Dataset and DataLoader | `19-pytorch-foundations/lesson-02.md`, `lesson-06-dataloader-device-safe-loop.md` | batching, data pipeline, custom dataset rebuild |
| Neural-network building blocks | `19-pytorch-foundations/lesson-02.md`, `lesson-05-loss-optimizer-gradient-debug.md` | nn.Module, forward pass, activation and loss |
| Complete training pipeline | `19-pytorch-foundations/lesson-03.md`, `lesson-06-dataloader-device-safe-loop.md` | forward, loss, backward, optimiser, validation |
| Monitoring and evaluation | `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md` | metrics, checkpoint, fresh-runtime evidence |

Approximate Course 1-supported use: **6–8 lessons**.

## DLAI-PT Course 2 — Techniques and Ecosystem Tools

**Status:** selected Round 2 support.

| Topic | Repo placement | Lesson use |
|---|---|---|
| TorchVision and image pipelines | `20-computer-vision/lesson-02.md`, `lesson-04-image-datasets-and-transforms.md` | image datasets, transforms, augmentation |
| Transfer learning and fine-tuning | `20-computer-vision/lesson-05-transfer-learning-finetuning.md` | pretrained model adaptation under time limits |
| Hugging Face and text workflows | `21-nlp-sequence-models/` | selected text preprocessing and model adaptation |
| Hyperparameter tuning and optimisation | `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md` | controlled experiments and evidence-driven improvement |
| Efficient training pipelines | `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md`, `24-round-2-project-training/` | reproducibility, validation, and runtime checks |

Approximate Course 2-supported use: **4–6 lessons**.

## DLAI-PT Course 3 — Advanced Architectures and Deployment

**Status:** optional IOAI / advanced-student extension.

Use selected content only for:

- ResNet, DenseNet, Siamese networks, and advanced architecture comparison;
- Transformers and generative-model architecture awareness;
- pruning and quantisation;
- ONNX / MLflow / deployment preparation;
- performance and efficiency trade-offs.

Possible placements:

- `20-computer-vision/` extension;
- `21-nlp-sequence-models/` extension;
- `23-llm-generative-ai/` extension;
- `24-round-2-project-training/` advanced experiment;
- IOAI elite extension tasks.

This course is not required for ordinary NOAI Round 1 preparation and should not displace baseline, validation, or submission training.

## When to Use HML vs DLAI-PT

| Teaching need | Use |
|---|---|
| sklearn pipeline, preprocessing, cross-validation, model comparison | HML + sklearn User Guide |
| tabular Round 2 baseline | HML + sklearn User Guide |
| PyTorch tensors, Dataset, DataLoader, nn.Module | DLAI-PT1 + PyTorch official tutorials |
| complete PyTorch training and validation loop | DLAI-PT1 + starter notebook |
| CNN, TorchVision, transfer learning | DLAI-PT2 + PyTorch/torchvision tutorials |
| selected advanced architecture or deployment | DLAI-PT3 as optional extension |
| error analysis and competition iteration | HML + DLAI-PT + NOAI/IOAI task notes |

## Student Instruction

Students should not passively watch long videos or copy notebook code. For every selected HML or DLAI-PT segment, students must produce:

1. guided notes naming the exact course, module, lesson, and assigned segment;
2. an Entry Check response;
3. a Core Pattern statement;
4. a Guided Practice artifact;
5. an Independent Rebuild artifact;
6. evidence of a fresh run when code is involved;
7. an AI-use note when AI assistance was used.

## Recommended Mainline

For most students, use this order:

1. BML15 for Round 1 A/B concept formation.
2. Andrew Ng's Machine Learning Specialization selected content for traditional ML concepts.
3. HML selected chapters for sklearn and practical ML workflow.
4. DLS selected content for deep-learning concepts.
5. DLAI-PT Course 1 and selected Course 2 modules for PyTorch implementation.
6. PyTorch official tutorials for API correctness.
7. Hugging Face and Qwen resources for NLP, LLM, audio, and multimodal extension.
8. NOAI / IOAI official tasks for timed reproduction and competition readiness.
