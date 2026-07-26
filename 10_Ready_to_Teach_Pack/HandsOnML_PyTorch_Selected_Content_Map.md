# Hands-On Machine Learning and DeepLearning.AI PyTorch Selected Content Map

This file clarifies how two practical resources are used in the NOAI / IOAI preparation curriculum:

1. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** by Aurélien Géron.
2. **DeepLearning.AI PyTorch for Deep Learning Professional Certificate** on Coursera, taught by Laurence Moroney.

The purpose is not to make students complete both resources end-to-end. The purpose is to select the parts that directly strengthen NOAI Round 2 C/D and IOAI-style applied problem solving.

## Full Resource Names and Links

| Full resource name | Coursera / source link | Main use |
|---|---|---|
| Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow | https://github.com/ageron/handson-ml3 | scikit-learn workflow, data pipelines, evaluation, model comparison, trees/ensembles, and end-to-end project habits |
| DeepLearning.AI PyTorch for Deep Learning Professional Certificate | https://www.coursera.org/professional-certificates/pytorch-for-deep-learning | PyTorch tensors, datasets, dataloaders, neural networks, training pipelines, transfer learning, vision, natural-language processing, optimisation, and selected deployment topics |
| Course 1 — PyTorch: Fundamentals | https://www.coursera.org/learn/pytorch-fundamentals | required PyTorch foundation course for selected repo lessons |
| Course 2 — PyTorch: Techniques and Ecosystem Tools | https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools | selected transfer learning, TorchVision, Hugging Face, tuning, and efficient-training content |
| Course 3 — PyTorch: Advanced Architectures and Deployment | https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment | optional advanced extension: architectures, Transformers, compression, export, and deployment |
| PyTorch official tutorials | https://docs.pytorch.org/tutorials/ | current API reference and implementation verification |

## Important Boundary

Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow is used mainly for **scikit-learn, end-to-end machine-learning workflow, evaluation, and practical model iteration**.

The DeepLearning.AI PyTorch for Deep Learning Professional Certificate is the repo's main structured PyTorch video/course series. PyTorch official tutorials remain the source of truth for current APIs.

Students do not need to complete the entire three-course certificate before competing. The teacher assigns selected modules that match the repo lesson targets.

## Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow Placement

| Topic | Repo placement | Lesson use |
|---|---|---|
| End-to-end machine-learning project workflow | `18-sklearn-workflow/`, `24-round-2-project-training/` | task reading, data audit, baseline, validation, and submission report |
| Data cleaning and preprocessing | `16-numpy-pandas-matplotlib/`, `17-data-cleaning-feature-engineering/` | missing values, categories, scaling, and leakage-safe transformations |
| scikit-learn pipelines | `18-sklearn-workflow/lesson-04-columntransformer-pipeline-leakage.md` | ColumnTransformer, Pipeline, and reproducibility |
| Model evaluation and cross-validation | `09-model-evaluation/`, `18-sklearn-workflow/` | metric decision, cross-validation design, and validation memo |
| Linear and logistic regression | `06-linear-regression/`, `07-logistic-regression/` | practical comparison after paper calculations |
| Trees, random forests, and boosting | `11-trees-and-ensembles/` | impurity, ensemble comparison, and model-selection evidence |
| Error analysis and iteration | `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md` | ablation, controlled experiments, and postmortem |

Approximate mainline use supported by Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: **18–25 lessons**, mostly in Round 2 C/D and selected Round 1 machine-learning modules.

## Course 1 — PyTorch: Fundamentals

**Status:** selected mainline resource.

| Topic | Repo placement | Lesson use |
|---|---|---|
| Tensors, tensor mathematics, and broadcasting | `19-pytorch-foundations/lesson-01.md` | tensor audit, shape ledger, and data-type/device reasoning |
| Dataset and DataLoader | `19-pytorch-foundations/lesson-02.md`, `lesson-06-dataloader-device-safe-loop.md` | batching, data pipeline, and custom-dataset rebuild |
| Neural-network building blocks | `19-pytorch-foundations/lesson-02.md`, `lesson-05-loss-optimizer-gradient-debug.md` | nn.Module, forward pass, activation, and loss |
| Complete training pipeline | `19-pytorch-foundations/lesson-03.md`, `lesson-06-dataloader-device-safe-loop.md` | forward pass, loss, backward pass, optimiser, and validation |
| Monitoring and evaluation | `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md` | metrics, checkpoint, and fresh-runtime evidence |

Approximate Course 1-supported use: **6–8 lessons**.

## Course 2 — PyTorch: Techniques and Ecosystem Tools

**Status:** selected Round 2 support.

| Topic | Repo placement | Lesson use |
|---|---|---|
| TorchVision and image pipelines | `20-computer-vision/lesson-02.md`, `lesson-04-image-datasets-and-transforms.md` | image datasets, transforms, and augmentation |
| Transfer learning and fine-tuning | `20-computer-vision/lesson-05-transfer-learning-finetuning.md` | pretrained-model adaptation under time limits |
| Hugging Face and text workflows | `21-nlp-sequence-models/` | selected text preprocessing and model adaptation |
| Hyperparameter tuning and optimisation | `24-round-2-project-training/lesson-06-ablation-error-analysis-report.md` | controlled experiments and evidence-driven improvement |
| Efficient training pipelines | `19-pytorch-foundations/lesson-07-pytorch-mini-project-validation.md`, `24-round-2-project-training/` | reproducibility, validation, and runtime checks |

Approximate Course 2-supported use: **4–6 lessons**.

## Course 3 — PyTorch: Advanced Architectures and Deployment

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

## Which Resource to Use

| Teaching need | Use |
|---|---|
| scikit-learn pipeline, preprocessing, cross-validation, and model comparison | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow + scikit-learn User Guide |
| tabular Round 2 baseline | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow + scikit-learn User Guide |
| PyTorch tensors, Dataset, DataLoader, and nn.Module | Course 1 — PyTorch: Fundamentals + PyTorch official tutorials |
| complete PyTorch training and validation loop | Course 1 — PyTorch: Fundamentals + starter notebook |
| convolutional neural networks, TorchVision, and transfer learning | Course 2 — PyTorch: Techniques and Ecosystem Tools + PyTorch/torchvision official tutorials |
| selected advanced architecture or deployment | Course 3 — PyTorch: Advanced Architectures and Deployment as an optional extension |
| error analysis and competition iteration | Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow + DeepLearning.AI PyTorch for Deep Learning Professional Certificate + official NOAI/IOAI task notes |

## Student Instruction

Students should not passively watch long videos or copy notebook code. For every selected section from Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow or the DeepLearning.AI PyTorch for Deep Learning Professional Certificate, students must produce:

1. guided notes naming the exact course, module, lesson, and assigned segment;
2. an Entry Check response;
3. a Core Pattern statement;
4. a Guided Practice artifact;
5. an Independent Rebuild artifact;
6. evidence of a fresh run when code is involved;
7. an AI-use note when AI assistance was used.

## Recommended Mainline

For most students, use this order:

1. 北京市十一学校《中学机器学习十五讲》 for Round 1 A/B concept formation.
2. Selected content from Machine Learning Specialization for traditional machine-learning concepts.
3. Selected chapters from Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow for scikit-learn and practical machine-learning workflow.
4. Selected content from Deep Learning Specialization for deep-learning concepts.
5. Course 1 — PyTorch: Fundamentals and selected modules from Course 2 — PyTorch: Techniques and Ecosystem Tools for PyTorch implementation.
6. PyTorch official tutorials for API correctness.
7. Hugging Face and Qwen resources for natural-language processing, large language models, audio, and multimodal extension.
8. Official NOAI / IOAI tasks for timed reproduction and competition readiness.