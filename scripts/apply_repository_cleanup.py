from __future__ import annotations

import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def replace(relative: str, pairs: list[tuple[str, str]]) -> None:
    path = ROOT / relative
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def remove(relative: str) -> None:
    path = ROOT / relative
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").replace("-", " ").title()


# ---------------------------------------------------------------------------
# 1. Remove files that are superseded, historically inert, or misleading.
# ---------------------------------------------------------------------------

for relative in [
    "PUBLISH_TO_GITHUB.md",
    "10_Ready_to_Teach_Pack/Completion_Audit_90.md",
    "10_Ready_to_Teach_Pack/Link_Verification_2026-07-19.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_0_Setup.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_1_Python.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_2_ML_Foundations.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_3_Neural_Networks.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_4_Round_1.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_5_Data_and_Sklearn.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_6_PyTorch_and_Domains.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_7_Competition.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_8_Competition_Sprint.md",
    "10_Ready_to_Teach_Pack/Phase_0_1_Setup_Python.md",
    "10_Ready_to_Teach_Pack/Phase_2A_ML_Foundations.md",
    "10_Ready_to_Teach_Pack/Phase_2B_Evaluation_Trees.md",
    "10_Ready_to_Teach_Pack/Phase_3_Neural_Networks.md",
    "10_Ready_to_Teach_Pack/Phase_4_Round_1.md",
    "10_Ready_to_Teach_Pack/Phase_5_Data_Sklearn.md",
    "10_Ready_to_Teach_Pack/Phase_6A_PyTorch_Vision.md",
    "10_Ready_to_Teach_Pack/Phase_6B_NLP_Audio_LLM.md",
    "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
]:
    remove(relative)

remove("scripts/v1_chunks")

# Move the pilot evidence record into the Pilot folder.
old_pilot_record = ROOT / "09_Teacher_Planning/Pilot_Lesson_Evidence_Record.md"
new_pilot_record = ROOT / "09_Teacher_Planning/Pilot/Pilot_Lesson_Evidence_Record.md"
if old_pilot_record.exists():
    new_pilot_record.parent.mkdir(parents=True, exist_ok=True)
    if new_pilot_record.exists():
        new_pilot_record.unlink()
    shutil.move(str(old_pilot_record), str(new_pilot_record))

# ---------------------------------------------------------------------------
# 2. Replace exact duplicate canonical lessons with phase-specific lessons.
# ---------------------------------------------------------------------------

write(
    "02_Class_Missions/07_Model_Comparison_EDA_Evaluation/session-72-split-safe-cleaning.md",
    """# Session 72 — Systematic EDA, Data Quality, and Distribution Shift

**Duration:** 75 minutes  
**Prerequisite:** Session 17 basic missing-value and split-safe cleaning practice

## Required Mastery

Students must be able to:

1. separate exploratory questions from preprocessing actions;
2. audit schema, target quality, duplicates, missingness, outliers, groups, and time;
3. distinguish missing completely at random, conditionally missing, and potentially informative missingness at an intuitive level;
4. compare training and validation distributions without using validation labels to design target-derived features;
5. identify target leakage, group leakage, temporal leakage, duplicate leakage, and preprocessing leakage;
6. decide whether a random, grouped, stratified, or time-aware split is defensible;
7. document a data-quality risk without silently “fixing” it;
8. connect an EDA finding to a controlled modelling decision.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Classify eight observations as schema, quality, shift, leakage, or modelling evidence. |
| 8–15 | **Talk Robin 1** | Explain why the same cleaning rule can be valid before deployment but invalid when fitted on all labelled rows. |
| 15–22 | **Entry Check** | Select the correct split strategy for random, grouped, and temporal tasks. |
| 22–35 | **Core Pattern** | Build a question-driven audit before choosing transformations. |
| 35–53 | **Guided Practice** | Audit a dataset containing repeated entities, time drift, missingness, and a suspicious feature. |
| 53–67 | **Independent Rebuild** | Produce a complete EDA and data-risk plan for a new task. |
| 67–75 | **Talk Robin 2 + Evidence** | Defend the highest-risk finding and the next controlled experiment. |

## Core Pattern

```text
task and unit of prediction
→ schema and target audit
→ split boundary
→ train/validation distribution comparison
→ leakage and quality risks
→ train-fitted transformations
→ baseline evidence
→ controlled next step
```

## Guided Practice Questions

- What is one row, and can the same entity appear in more than one split?
- Is time part of the prediction setting?
- Which columns could only exist after the target event?
- Are missing values associated with source, group, time, or target prevalence?
- Do rare categories or outliers represent errors, valid extremes, or a different population?
- Which observations justify a transformation, and which require more evidence?

## Independent Rebuild

Submit a one-page audit containing:

- unit of prediction and target definition;
- proposed split and justification;
- schema and data-quality table;
- at least two distribution comparisons;
- leakage risk register;
- train-only preprocessing plan;
- one baseline and one controlled next experiment;
- one limitation that EDA cannot resolve.

## Evidence

The evidence package is the audit page, two labelled plots or tables, a leakage-risk register, and a short defence of the split strategy.

## Gate

The student does not pass by listing cleaning operations. The student must show that the split, audit, preprocessing, and modelling decisions form one leakage-safe protocol.
""",
)

write(
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/session-52-svm-and-margin-lesson.md",
    """# Session 52 — Support Vector Machines: Margin, Scaling, and Model Behaviour

**Duration:** 75 minutes  
**Prerequisite:** Bohrium Session 29 margin intuition and Phase 5 mathematics bridge

## Required Mastery

Students must be able to:

1. identify a binary classification task appropriate for a linear support-vector baseline;
2. distinguish the decision boundary, margin, support vectors, and predicted class;
3. explain why only points near the boundary determine the maximum-margin solution;
4. describe the effect of the regularisation parameter `C` on margin violations and model flexibility;
5. explain why feature scaling changes distance and margin geometry;
6. distinguish a linear boundary from a kernel-induced nonlinear boundary;
7. compare SVM strengths and limitations with logistic regression, KNN, and trees;
8. train a leakage-safe scikit-learn pipeline and interpret validation evidence.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Mark boundary, margins, and support points on two diagrams. |
| 8–15 | **Talk Robin 1** | Explain how scaling one feature can rotate or distort the effective margin. |
| 15–22 | **Entry Check** | Predict the effect of increasing `C` in a noisy dataset. |
| 22–35 | **Core Pattern** | Connect signed boundary score, distance, margin, violations, and classification. |
| 35–53 | **Guided Practice** | Compare scaled linear SVM, logistic regression, and KNN under one split. |
| 53–67 | **Independent Rebuild** | Build and justify an SVM baseline for a new two-feature task. |
| 67–75 | **Talk Robin 2 + Evidence** | Defend model choice, `C`, scaling, metric, and one limitation. |

## Core Pattern

```text
scaled features
→ candidate separating boundary
→ margin and violations
→ support vectors
→ fitted decision function
→ threshold at zero
→ validation evidence
```

## Mathematics and Code Bridge

For a supplied linear score `f(x) = w · x + b`, students:

- calculate scores for small examples;
- identify the predicted class from the sign;
- compare which examples lie closest to the boundary;
- explain why rescaling a feature changes `w · x` and the geometry;
- locate `StandardScaler`, `SVC` or `LinearSVC`, and the metric in a scikit-learn pipeline.

## Independent Rebuild

The submission must include:

- task formalisation (`X`, `y`, metric, split);
- a scaled linear SVM baseline;
- a controlled comparison with one alternative model;
- a small `C` comparison table;
- support-vector or boundary interpretation where available;
- runtime and scaling notes;
- a model card naming failure modes and when not to use an SVM.

## Evidence

Submit the hand score/margin calculation, pipeline code, comparison table, boundary or support-point explanation, and model card.

## Gate

The student must explain model behaviour rather than report a score. A valid answer connects scaling, margin, `C`, support points, validation, and limitations.
""",
)

write(
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-60-forward-propagation.md",
    """# Session 60 — PyTorch Forward Pass: `nn.Module`, Logits, and Shape Debugging

**Duration:** 75 minutes  
**Prerequisite:** Session 47 conceptual forward propagation and Session 59 tensor/device work

## Required Mastery

Students must be able to:

1. implement a small network as an `nn.Module`;
2. explain what belongs in `__init__` and what belongs in `forward`;
3. track batch, feature, hidden, and output shapes through every layer;
4. distinguish logits, probabilities, predictions, targets, and loss;
5. match the final layer and loss function to regression, binary classification, or multiclass classification;
6. recognise when a softmax or sigmoid should not be inserted before a logits-based loss;
7. diagnose a matrix-shape, dtype, or device mismatch from an error message;
8. verify the forward pass with a small batch before training.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Predict shapes for a batch passing through two `nn.Linear` layers. |
| 8–15 | **Talk Robin 1** | Explain the difference between conceptual layer equations and a PyTorch `forward` method. |
| 15–22 | **Entry Check** | Match task type, output shape, and loss function. |
| 22–35 | **Core Pattern** | Trace batch → module → logits → loss-ready output. |
| 35–53 | **Guided Practice** | Repair a model with an incorrect input width, activation placement, and target dtype. |
| 53–67 | **Independent Rebuild** | Implement and test a fresh `nn.Module` from a shape specification. |
| 67–75 | **Talk Robin 2 + Evidence** | Explain the forward trace and one repaired failure. |

## Core Pattern

```text
input batch
→ shape assertion
→ linear transformation
→ activation
→ hidden representation
→ output layer
→ logits or regression output
→ loss function
```

## Guided Practice

Students annotate and repair:

```python
class Classifier(torch.nn.Module):
    def __init__(self, n_features: int, n_classes: int) -> None:
        super().__init__()
        self.hidden = torch.nn.Linear(n_features, 16)
        self.output = torch.nn.Linear(16, n_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.hidden(x))
        return self.output(x)
```

The class must state the expected shape and dtype before and after each operation and explain why the returned tensor is logits.

## Independent Rebuild

Create a module from a supplied task card. Include:

- constructor parameters;
- shape comments;
- a deterministic synthetic batch;
- assertions for output shape and finite values;
- the matching loss function;
- one intentionally introduced failure and its diagnosis;
- CPU-safe execution evidence.

## Evidence

Submit the shape ledger, tested module, output/loss interpretation, repaired error record, and one explanation of why a correct forward pass is necessary but not sufficient for a correct training system.

## Gate

The module must run on a fresh process, produce the required output shape, use a compatible loss, and be explained without relying on trial-and-error execution.
""",
)

# ---------------------------------------------------------------------------
# 3. Create concise indexes and one canonical tuning resource map.
# ---------------------------------------------------------------------------

write(
    "01_Student_Start/README.md",
    """# Student Setup and Evidence Index

Complete these files in order before or during the opening sessions:

1. [How This Course Works](00_How_This_Course_Works.md)
2. [Set Up the Student GitHub Repository](01_Set_Up_Student_GitHub_Repo.md)
3. [Set Up Python and Jupyter](02_Set_Up_Python_Jupyter.md)
4. [Set Up Bohrium](03_Set_Up_Bohrium.md)
5. [How to Submit Evidence](04_How_To_Submit_Evidence.md)
6. [AI Use Policy](05_AI_Use_Policy.md)
7. [Competition Notebook Rules](06_Competition_Notebook_Rules.md)

The canonical class entry point remains [Class Missions](../02_Class_Missions/README.md).
""",
)


def make_index(directory: str, title: str, intro: str) -> None:
    folder = ROOT / directory
    items: list[str] = []
    for path in sorted(folder.glob("*.md")):
        if path.name == "README.md":
            continue
        items.append(f"- [{heading(path)}]({path.name})")
    write(f"{directory}/README.md", f"# {title}\n\n{intro}\n\n" + ("\n".join(items) if items else "- No files."))


make_index(
    "03_Templates",
    "Student and Teacher Templates",
    "Use only the template named by the current Session, assessment, or teacher plan. Templates do not create additional scheduled lessons.",
)
make_index(
    "04_Assessment",
    "Public Assessment Index",
    "These public rubrics and checklists define visible evidence expectations. Protected answers, hidden tests, and calibration examples remain private.",
)
make_index(
    "05_Resources",
    "Resource Index",
    "Resource maps support the canonical Sessions. Current official documentation and competition rules override stale screenshots, timestamps, or historical assumptions.",
)
make_index(
    "08_Public_Documents",
    "Public Programme Documents",
    "Use these concise documents for students, parents, and programme communication. They do not replace Class Missions or current official competition rules.",
)

write(
    "09_Teacher_Planning/Pilot/README.md",
    """# Pilot Evidence Index

- [Pilot Protocol](Pilot_Protocol.md)
- [Representative Pilot Matrix](Representative_Pilot_Matrix.md)
- [Pilot Lesson Evidence Record](Pilot_Lesson_Evidence_Record.md)

A repository check cannot replace a real pilot. Record actual timing, student errors, reteaching decisions, and lesson revisions.
""",
)
write(
    "09_Teacher_Planning/Diagnostic_Guides/README.md",
    """# Diagnostic Guides

- [Initial Diagnostic](Initial_Diagnostic.md)

Use diagnostics to select remediation; do not renumber or reorder the canonical pathway without recording the cohort decision.
""",
)
write(
    "09_Teacher_Planning/Resource_Selection_Notes/README.md",
    """# Resource Selection Notes

- [English-First Policy](English_First_Policy.md)

Resource policy supplements the exact assignments in Class Missions. It does not create a parallel syllabus.
""",
)

# Regenerate a concise extension-library index and simple module indexes from files that remain.
library = ROOT / "02_Class_Missions/_Lesson_Library"
module_rows: list[str] = []
if library.exists():
    for module in sorted(path for path in library.iterdir() if path.is_dir()):
        lesson_files = sorted(module.rglob("lesson-*.md"))
        other_md = sorted(
            path for path in module.glob("*.md")
            if path.name != "README.md" and not path.name.startswith("lesson-")
        )
        listed = sorted(set(lesson_files + other_md))
        if not listed:
            remove(str(module.relative_to(ROOT)))
            continue
        module_title = module.name.replace("-", " ").title()
        entries = [
            f"- [{heading(path)}]({path.relative_to(module).as_posix()})"
            for path in listed
        ]
        write(
            str((module / "README.md").relative_to(ROOT)),
            f"# {module_title}\n\nThis module is extension or remediation material. It is not part of the canonical 78-Session schedule unless a teacher explicitly assigns it.\n\n" + "\n".join(entries),
        )
        module_rows.append(f"| [{module.name}]({module.name}/README.md) | {len(lesson_files)} | extension/remediation |")

write(
    "02_Class_Missions/_Lesson_Library/README.md",
    """# Lesson Library — Extension and Remediation Only

Canonical Sessions 1–78 live directly inside the numbered Phase folders. Use this library only when a Session or teacher plan assigns remediation, deeper practice, reproduction work, a mock, or an optional extension.

| Module | Lesson files | Role |
|---|---:|---|
""" + "\n".join(module_rows) + "\n\nReturn to [Class Missions](../README.md) for the scheduled pathway.",
)

write(
    "05_Resources/Hyperparameter_Tuning_Resource_Map.md",
    """# Hyperparameter-Tuning Resource Map

**Canonical placement:** Session 75  
**Rule:** tuning begins only after task definition, split design, preprocessing, baseline, metric, and error analysis are trustworthy.

## Required Concept Sources

| Need | Preferred source | Student evidence |
|---|---|---|
| bias/variance and diagnosis | Andrew Ng Machine Learning Specialization and the Phase 5 model-diagnosis work | learning-curve or error diagnosis |
| regularisation and optimisation intuition | Deep Learning Specialization, Course 2 — Improving Deep Neural Networks | one parameter hypothesis and predicted effect |
| scikit-learn search and pipelines | current scikit-learn User Guide | leakage-safe search space and cross-validation plan |
| PyTorch tuning | PyTorch official tutorials and the maintained starter code | controlled training log and stopping rule |
| optional automated search | Optuna documentation and `06_Starter_Code/ready_to_teach/optuna_tuning_template.py` | bounded search, seed, budget, and held-out confirmation |

## Session 75 Sequence

```text
error analysis
→ one hypothesis
→ one controlled manual change
→ compare validation evidence
→ define a bounded search space
→ optional automated search
→ confirm on untouched evidence
→ record runtime and limitations
```

## Non-Negotiable Boundaries

- Do not tune on the test set or public leaderboard repeatedly.
- Do not compare trials that use different splits or preprocessing unless that is the controlled experiment.
- Do not use automated search to hide a missing baseline or invalid validation design.
- Record compute budget, failed trials, seed, metric direction, and stopping rule.
- Prefer a stable simpler model when the improvement is small, expensive, or not reproducible.

## Required Evidence

- diagnosis before tuning;
- manual tuning table;
- bounded search-space rationale;
- validation protocol;
- runtime/compute record;
- final parameter choice and rejected alternatives;
- untouched confirmation or explicit statement that none is available;
- limitations and next action.

Use [Session 75 classical tuning](../02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-classical-model-tuning.md), [Session 75 deep-learning tuning](../02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-deep-learning-tuning.md), and the [Phase 8 launcher](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md).
""",
)

# ---------------------------------------------------------------------------
# 4. Rewrite resource maps around the current phase-local architecture.
# ---------------------------------------------------------------------------

write(
    "10_Ready_to_Teach_Pack/DLS_Selected_Content_Map.md",
    """# Deep Learning Specialization — Selected Content Map

The Deep Learning Specialization is a just-in-time concept resource, not a second scheduled curriculum. The canonical sequence remains Sessions 1–78 in Class Missions.

## Placement

| Deep Learning Specialization content | Canonical use | Repository entry |
|---|---|---|
| Course 1 — Neural Networks and Deep Learning | forward propagation and representation review | [Session 47](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/session-47-multilayer-networks-and-forward-propagation.md) and [Session 60](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-60-forward-propagation.md) |
| Course 2 — Improving Deep Neural Networks | regularisation, optimisation, learning-rate reasoning, and tuning | [Session 62](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md), [Session 75](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md), and the [tuning map](../05_Resources/Hyperparameter_Tuning_Resource_Map.md) |
| Course 3 — Structuring Machine Learning Projects | split design, metric choice, error analysis, and iteration strategy | [Phase 7 launcher](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/SESSION_LAUNCHER.md) |
| Course 4 — Convolutional Neural Networks | convolution, shapes, transfer learning, and image error analysis | [Sessions 63–65](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| Course 5 — Sequence Models | RNN/LSTM and attention intuition | [Sessions 66–68](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |

## Assignment Rule

For every selected segment, the teacher names the exact course/week/video and the student submits:

1. a concept statement;
2. an entry-check response;
3. a hand trace, diagram, or shape ledger;
4. an independent implementation or explanation;
5. a limitation or misconception correction.

Concept videos never replace the phase-local Session packet, current framework documentation, or evidence gate.
""",
)

write(
    "10_Ready_to_Teach_Pack/HandsOnML_PyTorch_Selected_Content_Map.md",
    """# Hands-On Machine Learning and PyTorch — Selected Content Map

These resources support implementation. They do not create additional scheduled phases.

## Hands-On Machine Learning Placement

| Need | Canonical placement |
|---|---|
| end-to-end tabular workflow and baseline | [Sessions 41 and 57](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md) |
| preprocessing, pipelines, and leakage control | [Session 57](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md) and [Sessions 72–74](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/SESSION_LAUNCHER.md) |
| model comparison, trees, and ensembles | [Sessions 48–50](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md) |
| error analysis and controlled iteration | [Phase 7](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/README.md) and [Phase 8](../02_Class_Missions/08_Tuning_Ensembling_Competition/README.md) |

## DeepLearning.AI PyTorch Certificate Placement

| Need | Canonical placement |
|---|---|
| tensors, devices, Dataset, DataLoader, and `nn.Module` | [Sessions 59–60](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| autograd and training/validation loops | [Sessions 61–62](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| CNNs, TorchVision, and transfer learning | [Sessions 63–65](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| sequence models, attention, and domain tasks | [Sessions 66–70](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| optional advanced architectures or deployment | [Lesson Library](../02_Class_Missions/_Lesson_Library/README.md) only when explicitly assigned |

## Evidence Rule

Students must record the exact assigned section, then produce a fresh-run artifact, shape/device evidence, validation result, error analysis, and AI-use note. Passive viewing or copied notebook execution is not completion.
""",
)

write(
    "10_Ready_to_Teach_Pack/Resource_Map_and_Syllabus_Crosswalk.md",
    """# Resource and NOAI / IOAI Syllabus Crosswalk

This crosswalk uses the canonical nine phases and Session ranges. Current official rules and syllabi override this repository.

## Resource Roles

| Resource | Role | Main placement |
|---|---|---|
| Harvard CS50’s Introduction to Programming with Python | Python spine | Sessions 3–12 |
| NumPy, Pandas, and Matplotlib documentation | data-tool implementation | Sessions 13–18 and 71–74 |
| 北京市十一学校《中学机器学习十五讲》 | Chinese ML concept foundation | Sessions 19–32 |
| Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* | AI history, claims, and limitations | Sessions 33–40 |
| Andrew Ng Machine Learning Specialization | classical-model spine | Sessions 41–58 |
| StatQuest and 3Blue1Brown | just-in-time statistics and mathematics intuition | Sessions 41–58 |
| Kaggle Learn | embedded workflow rehearsal | selected tasks inside Sessions 41–57 |
| Hands-On Machine Learning and scikit-learn User Guide | practical tabular workflow | Sessions 41–58 and 71–75 |
| Andrew Ng Deep Learning Specialization | deep-learning concepts | Sessions 59–70 |
| DeepLearning.AI PyTorch certificate and PyTorch tutorials | deep-learning implementation | Sessions 59–70 |
| Hugging Face, torchaudio, OpenCV, and Qwen documentation | domain extensions | Sessions 64–70 and assigned library extensions |
| current official NOAI / IOAI documents | scope, tools, runtime, and submission rules | every cohort and scored mock |

## Syllabus Crosswalk

| Syllabus capability | Canonical coverage | Required evidence |
|---|---|---|
| Python, control flow, collections, exceptions, files, and testing | [Phase 1](../02_Class_Missions/01_CS50P_Python/SESSION_LAUNCHER.md) | code trace, tested program, CSV processing, error record |
| arrays, tables, visualisation, and data quality | [Phase 2](../02_Class_Missions/02_NumPy_Pandas_Visualisation/SESSION_LAUNCHER.md) and [Phase 7](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/SESSION_LAUNCHER.md) | audit notebook, plots, leakage-safe plan |
| AI schools, learning paradigms, ethics, and limitations | [Phases 3–4](../02_Class_Missions/README.md) | concept map, claim audit, evidence-based argument |
| regression, classification, evaluation, trees, ensembles, clustering, PCA, anomaly detection, and recommenders | [Phase 5](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md) | hand calculation, baseline, comparison, model card |
| neural networks, optimisation, CNNs, sequences, attention, and PyTorch | [Phase 6](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) | shape ledger, training loop, domain task, fresh run |
| model comparison, EDA, feature work, validation, and error analysis | [Phase 7](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/SESSION_LAUNCHER.md) | defensible protocol and error-analysis memo |
| tuning, ensembling, timed workflow, and postmortem | [Phase 8](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md) | experiment log, ensemble evidence, valid submission, postmortem |

## Selection Boundary

External courses provide explanations and examples. Class Missions define the scheduled task, classroom cycle, required evidence, and advancement gate. Do not assign an entire external course unless a cohort-specific plan explicitly records the added time and capability goal.
""",
)

# ---------------------------------------------------------------------------
# 5. Clean navigation, stale wording, and broken references.
# ---------------------------------------------------------------------------

write(
    "00_Course_Overview/README.md",
    """# Course Overview

The canonical 78-Session route is organised by learning dependency.

## Core Pathway Documents

- [Course Map](Course_Map.md)
- [Detailed 78-Session Sequence](Detailed_Lesson_Sequence.md)
- [Pacing Guide](Pacing_Guide.md)
- [Cohort Pathways and Required / Optional Map](Cohort_Pathways_and_Required_Optional_Map.md)
- [Round 1 and Round 2 Pathway](Round_1_and_Round_2_Pathway.md)
- [Learning Outcomes](Learning_Outcomes.md)
- [Course Implementation Checklist](Course_Implementation_Checklist.md)
- [NOAI 2026 Syllabus Map](NOAI_2026_Syllabus_Map.md)

## Architecture and Readiness

- [Expanded Lesson Architecture](Expanded_Lesson_Architecture.md)
- [Curriculum Completeness and Consistency Audit](Curriculum_Completeness_Audit.md)
- [Repository Architecture Manifest](../MANIFEST.md)
- [Class Missions](../02_Class_Missions/README.md)
- [Public Repository Readiness Dashboard](../10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md)

```text
CS50P Python
→ NumPy / Pandas / visualisation
→ Bohrium ML foundations
→ AI History and Thinking Humans
→ Andrew Ng ML + mathematics + embedded practice
→ Andrew Ng DL + PyTorch
→ model comparison + EDA + evaluation
→ tuning + ensembling + competition
```

Canonical lesson bodies live inside numbered Phase folders. `_Lesson_Library` contains extension and remediation material only.
""",
)

write(
    "09_Teacher_Planning/Phase_Overviews/README.md",
    """# Canonical Teacher Phase Overviews

These nine files summarise the canonical 78-Session pathway. They identify purpose, entry conditions, delivery priorities, evidence, and exit gates without copying complete lesson bodies.

## Source Priority

1. [Class Missions](../../02_Class_Missions/README.md)
2. each Phase `SESSION_LAUNCHER.md`
3. phase-local Session packet
4. [Pacing Guide](../../00_Course_Overview/Pacing_Guide.md)
5. these concise planning summaries

## Phase Files

- [Phase 0 — Orientation and Evidence](Canonical_Phase_0_Orientation_and_Evidence.md)
- [Phase 1 — CS50P Python](Canonical_Phase_1_CS50P_Python.md)
- [Phase 2 — NumPy, Pandas, and Visualisation](Canonical_Phase_2_NumPy_Pandas_Visualisation.md)
- [Phase 3 — Bohrium ML Foundations](Canonical_Phase_3_Bohrium_ML_Foundations.md)
- [Phase 4 — AI History and Thinking Humans](Canonical_Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew Ng ML Model Labs](Canonical_Phase_5_Andrew_Ng_ML_Model_Labs.md)
- [Phase 6 — Andrew Ng DL and PyTorch](Canonical_Phase_6_Andrew_Ng_DL_PyTorch.md)
- [Phase 7 — Model Comparison, EDA, and Evaluation](Canonical_Phase_7_Model_Comparison_EDA_Evaluation.md)
- [Phase 8 — Tuning, Ensembling, and Competition](Canonical_Phase_8_Tuning_Ensembling_Competition.md)

When a summary conflicts with a Session packet, correct the summary and teach from the Session packet.
""",
)

write(
    "09_Teacher_Planning/README.md",
    """# Teacher Planning Index

## Pathway and Phase Planning

- [Class Missions](../02_Class_Missions/README.md)
- [Canonical teacher phase overviews](Phase_Overviews/README.md)
- [Detailed 78-Session Sequence](../00_Course_Overview/Detailed_Lesson_Sequence.md)
- [Pacing Guide](../00_Course_Overview/Pacing_Guide.md)
- [Cohort Pathways](../00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md)
- [Repository Architecture Manifest](../MANIFEST.md)

## Special Delivery Packs

- [Phase 4 — AI History](../10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew ML Mathematics Bridge](../10_Ready_to_Teach_Pack/Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md)
- [Phase 8 — Competition](../10_Ready_to_Teach_Pack/Phase_8_Competition_Sprint.md)
- [Hyperparameter-Tuning Resource Map](../05_Resources/Hyperparameter_Tuning_Resource_Map.md)
- [75-Minute After-School Club Implementation](75min_After_School_Club_Implementation.md)
- [Bohrium 70-Minute Split](BML15_70min_Lesson_Split.md)

## Diagnostics, Resources, and Pilots

- [Diagnostic Guides](Diagnostic_Guides/README.md)
- [Resource Selection Notes](Resource_Selection_Notes/README.md)
- [Pilot Evidence](Pilot/README.md)

## Readiness and Security

- [Public Repository Readiness Dashboard](../10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md)
- [Release Readiness Gates](../10_Ready_to_Teach_Pack/Release_Readiness_Gates.md)
- [Validation and Pilot Checklist](Validation_and_Pilot_Checklist.md)
- [Teacher-Key Private Repository Manifest](Teacher_Key_Private_Repo_Manifest.md)
- [Student Runtime Qualification Record](../10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](../10_Ready_to_Teach_Pack/External_Access_Verification_Record.md)

Before formal graded use, verify current rules, exact student runtime, authenticated access, legal book access, private assessment security, and representative pilots.
""",
)

write(
    "10_Ready_to_Teach_Pack/README.md",
    """# Ready-to-Teach Pack Index

Canonical teaching begins in [Class Missions](../02_Class_Missions/README.md). This folder contains delivery support and release evidence, not a second lesson sequence.

## Canonical Delivery Packs

- [Phase 4 — AI History and Thinking Humans](Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew ML Mathematics Bridge](Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md)
- [Phase 8 — Tuning, Ensembling, and Competition](Phase_8_Competition_Sprint.md)

## Resource Crosswalks

- [Resource and Syllabus Crosswalk](Resource_Map_and_Syllabus_Crosswalk.md)
- [Deep Learning Specialization Selected Content](DLS_Selected_Content_Map.md)
- [Hands-On ML and PyTorch Selected Content](HandsOnML_PyTorch_Selected_Content_Map.md)
- [Starter Notebooks and Datasets](Starter_Notebooks_and_Datasets.md)

## Assessment and Mock Security

- [Round 1 Mock B](Round_1_Mock_B.md)
- [Round 2 Mock Pack](Round_2_Mock_Pack.md)
- [Hidden Mock Sealing Protocol](Hidden_Mock_Sealing_Protocol.md)

## Readiness Records

- [Public Repository Readiness Dashboard](Public_Repository_Readiness_Dashboard.md)
- [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md)
- [Release Readiness Gates](Release_Readiness_Gates.md)
- [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](External_Access_Verification_Record.md)
- [Runtime Validation Record](Runtime_Validation_Record.md)
- [Latest Link Verification](Link_Verification_Latest.md)
- [Latest Automated Curriculum Audit](Automated_Curriculum_Audit_Latest.md)
- [Repository Cleanup Audit](Repository_Cleanup_Audit.md)

## Annual Rules

- [Annual Competition Rule Verification Template](Annual_Competition_Rule_Verification.md)
- [2026 Rules Verification Record](Annual_Rules_2026_Verification.md)

Public repository checks do not replace cohort-specific runtime, access, privacy, pilot, or current-rule evidence.
""",
)

write(
    "09_Teacher_Planning/Public_Repo_100_Percent_Readiness_Definition.md",
    """# Public Repository 100 Percent Coverage Definition

The repository has **100% public file-structure and internal-consistency coverage** when all maintained canonical and support assets satisfy the contracts below. This is not a blanket claim of operational readiness.

## Public Coverage Contract

1. Nine numbered phases contain Sessions 1–78 exactly once.
2. Every Phase README links to its Session launcher.
3. Every canonical Session links only to existing phase-local packets.
4. Canonical packets state duration, task, evidence, and gate.
5. Phase 4 contains eight English AI History seminars and its teacher/template/rubric package.
6. Phase 5 contains the Andrew ML mathematics transition and model-recognition/task resources.
7. Kaggle practice is embedded in Andrew ML rather than scheduled as a separate phase.
8. Phase 6 pairs deep-learning concepts with PyTorch implementation.
9. Phases 7–8 cover systematic EDA, evaluation, tuning, ensembling, simulation, and postmortem.
10. `_Lesson_Library` contains extension/remediation material only and has a current index.
11. Student setup, templates, assessments, resources, public documents, teacher planning, and Ready-to-Teach records have clear indexes.
12. Internal Markdown links and anchors resolve.
13. Canonical Session packets are not exact duplicates.
14. Obsolete generator fragments, legacy phase summaries, and superseded delivery packs are absent.
15. Current validators pass:

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
```

## Separate Operational Gates

Public coverage does not prove:

- successful execution in the exact student environment;
- authenticated access to external courses or legal access to the Phase 4 book;
- current permission for packages, APIs, models, external data, or internet use;
- assessment-security completion;
- representative classroom timing and comprehension;
- full 78-Session cohort delivery;
- current-year competition alignment;
- competition performance.

Use the [Public Repository Readiness Dashboard](../10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md), [Release Readiness Gates](../10_Ready_to_Teach_Pack/Release_Readiness_Gates.md), and open operational-readiness Issue for those decisions.
""",
)

write(
    "03_Templates/Error_Log_Template.md",
    """# Error Log Template

Use one row per meaningful error, misconception, failed experiment, or reproducibility problem.

| Date / Session | Error or Wrong Idea | Evidence / Symptom | Root Cause | Fix Tested | Prevention Rule | Retest Result |
|---|---|---|---|---|---|---|
| | | | | | | |

## Required Reflection

For the most important entry, answer:

1. What did I initially believe?
2. What evidence showed that belief was wrong or incomplete?
3. What was the smallest test that isolated the cause?
4. What change fixed the problem?
5. How will I detect or prevent the same class of error next time?

A screenshot without a diagnosis, tested fix, and retest result is not a complete error record.
""",
)

# Focused text replacements.
replace(
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md",
    [
        (
            "Andrew_ML_Mathematics_Bridge.md#session-41--mathematical-language-of-machine-learning",
            "Andrew_ML_Mathematics_Bridge.md#session-41-mathematical-language-of-machine-learning",
        ),
        (
            "This launcher is the scheduled route. Open the exact session link; do not choose a lesson by browsing `_Lesson_Library`.",
            "Open the exact Session link below.",
        ),
    ],
)

for relative in [
    "02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-classical-model-tuning.md",
    "02_Class_Missions/08_Tuning_Ensembling_Competition/session-75-deep-learning-tuning.md",
]:
    replace(
        relative,
        [
            (
                "../_Lesson_Library/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md",
                "../../05_Resources/Hyperparameter_Tuning_Resource_Map.md",
            )
        ],
    )

replace(
    "05_Resources/English_Video_Resource_Map.md",
    [
        (
            "../02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md",
            "Hyperparameter_Tuning_Resource_Map.md",
        ),
        (
            "02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md",
            "05_Resources/Hyperparameter_Tuning_Resource_Map.md",
        ),
    ],
)

replace(
    "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md",
    [("Do not assign all 171 reusable public files automatically.", "Do not assign every extension or remediation file automatically.")],
)

replace(
    "STUDENT_START_HERE.md",
    [
        (
            "Do **not** browse `_Lesson_Library` and choose a file yourself. A linked lesson may be stored there, but the Phase launcher has already selected the correct file. Use the browser Back button to return to the launcher.",
            "All canonical lessons are stored inside their numbered Phase folders. Use `_Lesson_Library` only when your teacher assigns an extension or remediation task.",
        ),
        (
            "1. Read [How This Course Works](01_Student_Start/00_How_This_Course_Works.md).",
            "1. Open the [Student Setup and Evidence Index](01_Student_Start/README.md).",
        ),
    ],
)

replace(
    "TEACHER_START_HERE.md",
    [
        (
            "Do **not** browse `_Lesson_Library` to choose a class. The library is a storage bank for lesson bodies, remediation, extension, and maintenance; the Phase launchers define the scheduled route.",
            "Canonical lessons are phase-local. Use `_Lesson_Library` only for explicitly selected remediation or extension.",
        ),
        (
            "python scripts/validate_class_mission_launchers.py\npython scripts/check_required_links.py",
            "python scripts/validate_class_mission_launchers.py\npython scripts/validate_repository_hygiene.py\npython scripts/check_required_links.py",
        ),
    ],
)

replace(
    "02_Class_Missions/README.md",
    [
        (
            "- [`_Curriculum_Governance`](./_Curriculum_Governance/README.md) — audits, counts, architecture, and maintenance.",
            "- [Repository Architecture Manifest](../MANIFEST.md) — source priority, validation, and maintenance contract.",
        )
    ],
)
replace(
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    [
        (
            "| `_Curriculum_Governance` | curriculum maintainer | audits, counts, architecture, and maintenance |",
            "| [Repository Architecture Manifest](../MANIFEST.md) | curriculum maintainer | source priority, validation, and maintenance |",
        ),
        (
            "- teach from governance documents;",
            "- teach from architecture or readiness records;",
        ),
    ],
)

for relative, pairs in {
    "02_Class_Missions/00_Orientation_and_Evidence/README.md": [
        ("Use the launcher to select Session 1 or 2. Do not browse `_Lesson_Library` manually.", "Open the Session Launcher to select Session 1 or 2.")
    ],
    "02_Class_Missions/01_CS50P_Python/README.md": [
        ("The launcher maps every scheduled session to the exact lesson file and required evidence. Do not choose lessons by browsing `_Lesson_Library`.", "The launcher maps every scheduled Session to its phase-local lesson and required evidence.")
    ],
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/README.md": [
        ("The launcher maps every scheduled model session to the exact lesson packet, mathematical evidence, typical task, Kaggle practice, and gate. Do not browse `_Lesson_Library` manually.", "The launcher maps every scheduled model Session to its lesson packet, mathematical evidence, typical task, embedded practice, and gate.")
    ],
}.items():
    replace(relative, pairs)

# ---------------------------------------------------------------------------
# 6. Add permanent repository-hygiene validation and wire it into CI.
# ---------------------------------------------------------------------------

write(
    "scripts/validate_repository_hygiene.py",
    r'''from __future__ import annotations

import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
CODE_PATH_RE = re.compile(r"`((?:00_|01_|02_|03_|04_|05_|06_|08_|09_|10_|scripts/|README\.md|MANIFEST\.md|TEACHER_START_HERE\.md|STUDENT_START_HERE\.md)[^`\n]*)`")

REQUIRED_INDEXES = (
    "01_Student_Start/README.md",
    "02_Class_Missions/_Lesson_Library/README.md",
    "03_Templates/README.md",
    "04_Assessment/README.md",
    "05_Resources/README.md",
    "08_Public_Documents/README.md",
    "09_Teacher_Planning/README.md",
    "09_Teacher_Planning/Phase_Overviews/README.md",
    "09_Teacher_Planning/Pilot/README.md",
    "10_Ready_to_Teach_Pack/README.md",
)

OBSOLETE_PATHS = (
    "PUBLISH_TO_GITHUB.md",
    "scripts/v1_chunks",
    "10_Ready_to_Teach_Pack/Completion_Audit_90.md",
    "10_Ready_to_Teach_Pack/Phase_0_1_Setup_Python.md",
    "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_0_Setup.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_8_Competition_Sprint.md",
)

BANNED_TEXT = (
    re.compile(r"\b75[- ]session|\b75 sessions\b", re.IGNORECASE),
    re.compile(r"67\s*\+\s*8|67 core", re.IGNORECASE),
    re.compile(r"155 mainline|171 public lesson|171 reusable", re.IGNORECASE),
    re.compile(r"04_Kaggle_ML_Refresh", re.IGNORECASE),
)


def anchor(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text.strip().lower())
    text = re.sub(r"[^\w\-\u4e00-\u9fff ]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def anchors(path: Path) -> set[str]:
    result: set[str] = set()
    counts: defaultdict[str, int] = defaultdict(int)
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = anchor(match.group(1))
        if not base:
            continue
        index = counts[base]
        counts[base] += 1
        result.add(base if index == 0 else f"{base}-{index}")
    return result


def main() -> int:
    errors: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))

    for relative in REQUIRED_INDEXES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing repository index: {relative}")

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Obsolete path still exists: {relative}")

    for document in markdown:
        text = document.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("# "):
            errors.append(f"Markdown file lacks H1: {document.relative_to(ROOT)}")

        for raw in LINK_RE.findall(text):
            raw = raw.strip().strip("<>")
            if not raw or raw.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            if raw.startswith("#"):
                target = document
                fragment = raw[1:]
            else:
                path_part, marker, fragment = raw.partition("#")
                target = (document.parent / path_part).resolve()
                if not target.exists():
                    errors.append(f"Broken Markdown link: {document.relative_to(ROOT)} -> {raw}")
                    continue
            if fragment and target.suffix.lower() == ".md" and fragment.lower() not in anchors(target):
                errors.append(f"Broken Markdown anchor: {document.relative_to(ROOT)} -> {raw}")

        for raw in CODE_PATH_RE.findall(text):
            raw = raw.strip()
            if " " in raw or "*" in raw:
                continue
            path_part = raw.split("#", 1)[0]
            candidate = (ROOT / path_part).resolve()
            if not candidate.exists():
                errors.append(f"Missing repository path in code span: {document.relative_to(ROOT)} -> {raw}")

        if "Repository_Cleanup_Audit.md" not in document.as_posix():
            for pattern in BANNED_TEXT:
                if pattern.search(text):
                    errors.append(f"Stale architecture language in {document.relative_to(ROOT)}: {pattern.pattern}")

    groups: defaultdict[str, list[Path]] = defaultdict(list)
    for phase in sorted((ROOT / "02_Class_Missions").glob("[0-9][0-9]_*/")):
        for packet in sorted(list(phase.glob("session-*.md")) + list(phase.glob("lesson-*.md"))):
            content = packet.read_text(encoding="utf-8").strip()
            groups[hashlib.sha256(content.encode("utf-8")).hexdigest()].append(packet)
    for group in groups.values():
        if len(group) > 1:
            errors.append("Exact duplicate canonical packets: " + ", ".join(str(p.relative_to(ROOT)) for p in group))

    if errors:
        print("Repository hygiene validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository hygiene validation passed.")
    print(f"Markdown files checked: {len(markdown)}")
    print("Internal Markdown links and anchors: valid")
    print("Exact duplicate canonical packets: 0")
    print("Obsolete pathway and generator files: absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
''',
)

# Update workflow triggers and audit execution.
audit_workflow = ROOT / ".github/workflows/audit-curriculum.yml"
text = audit_workflow.read_text(encoding="utf-8")
text = text.replace(
    '      - "scripts/validate_class_mission_launchers.py"\n',
    '      - "scripts/validate_class_mission_launchers.py"\n      - "scripts/validate_repository_hygiene.py"\n',
)
text = text.replace(
    "          python scripts/validate_class_mission_launchers.py >> /tmp/audit.log 2>&1\n          launcher_code=$?\n\n          if [ \"$structure_code\" -ne 0 ] || [ \"$readiness_code\" -ne 0 ] || [ \"$launcher_code\" -ne 0 ]; then",
    "          python scripts/validate_class_mission_launchers.py >> /tmp/audit.log 2>&1\n          launcher_code=$?\n          python scripts/validate_repository_hygiene.py >> /tmp/audit.log 2>&1\n          hygiene_code=$?\n\n          if [ \"$structure_code\" -ne 0 ] || [ \"$readiness_code\" -ne 0 ] || [ \"$launcher_code\" -ne 0 ] || [ \"$hygiene_code\" -ne 0 ]; then",
)
audit_workflow.write_text(text, encoding="utf-8")

ready_workflow = ROOT / ".github/workflows/validate-ready-to-teach.yml"
text = ready_workflow.read_text(encoding="utf-8")
text = text.replace(
    '      - "scripts/validate_class_mission_launchers.py"\n',
    '      - "scripts/validate_class_mission_launchers.py"\n      - "scripts/validate_repository_hygiene.py"\n',
)
text = text.replace(
    "      - name: Install validation environment\n",
    "      - name: Validate repository hygiene\n        run: python scripts/validate_repository_hygiene.py\n\n      - name: Install validation environment\n",
)
ready_workflow.write_text(text, encoding="utf-8")

# ---------------------------------------------------------------------------
# 7. Write a concise final cleanup record.
# ---------------------------------------------------------------------------

write(
    "10_Ready_to_Teach_Pack/Repository_Cleanup_Audit.md",
    """# Repository Cleanup Audit

## Scope

This cleanup reviewed repository files, navigation, internal Markdown links and anchors, canonical lesson duplication, stale architecture language, historical branches, and open Issues.

## Changes Applied

- removed two merged historical agent branches;
- removed obsolete V1 generator fragments and the pre-publication GitHub instruction;
- removed legacy teacher phase summaries superseded by nine canonical phase overviews;
- removed old Ready-to-Teach packs that copied an obsolete session structure;
- removed a legacy percentage pointer and a superseded dated link-verification snapshot;
- repaired all discovered internal Markdown links and the Andrew ML mathematics anchor;
- replaced three exact duplicate canonical lessons with phase-specific learning targets;
- added concise indexes for student setup, extension lessons, templates, assessments, resources, public documents, diagnostics, pilots, and Ready-to-Teach records;
- centralised hyperparameter-tuning resources;
- rewrote selected-content maps to use current phase-local Session paths;
- added permanent repository-hygiene validation to CI.

## Current Navigation Contract

```text
Phase
→ SESSION_LAUNCHER.md
→ phase-local Session packet
```

`_Lesson_Library` is extension/remediation only.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

## Boundary

Repository hygiene and public structural completeness do not replace exact student-runtime qualification, authenticated access, private assessment security, representative pilots, full-cohort evidence, or current competition-year verification.
""",
)

print("Repository cleanup applied.")
