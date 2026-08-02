from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
runpy.run_path(str(ROOT / "scripts/apply_repository_cleanup_v2.py"), run_name="__main__")


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


write(
    "08_Public_Documents/Competition_Pathway.md",
    """# NOAI / IOAI Competition Preparation Pathway

The curriculum develops competition readiness through the canonical 78-Session dependency path rather than asking students to jump directly into advanced models.

```text
orientation and evidence
→ CS50P Python
→ NumPy, Pandas, and visualisation
→ Bohrium ML foundations
→ AI history and critical reading
→ Andrew Ng ML + mathematics + embedded practice
→ Andrew Ng DL + PyTorch + domain tasks
→ model comparison + EDA + evaluation
→ diagnosis-first tuning + ensembling + competition simulation
```

## Canonical Pathway

| Phase | Sessions | Competition contribution |
|---:|---:|---|
| 0 | 1–2 | environment, evidence, Git, and responsible assistance |
| 1 | 3–12 | Python code reading, testing, debugging, and independent programs |
| 2 | 13–18 | data inspection, transformation, and visual reasoning |
| 3 | 19–32 | machine-learning concept foundation |
| 4 | 33–40 | AI history, claim auditing, understanding, and limitations |
| 5 | 41–58 | classical models, mathematics, task recognition, and tabular workflows |
| 6 | 59–70 | PyTorch, image, text, audio, and multimodal tasks |
| 7 | 71–74 | model comparison, EDA, features, validation, metrics, and error analysis |
| 8 | 75–78 | tuning, ensembling, full simulation, and postmortem |

A shortened cohort route may reduce breadth, but it must not redefine canonical Session numbers or claim full-pathway readiness.

## Competition Habits

- formalise `X`, `y` or required output, metric, prediction-time boundary, constraints, and submission schema;
- inspect data quality and prevent target, identity, duplicate, group, temporal, and preprocessing leakage;
- preserve a simple baseline under one validation protocol;
- keep feature generation reproducible;
- compare model families from evidence;
- analyse errors before tuning;
- record controlled experiments;
- validate final artifacts from a fresh environment.

## Final Phase

Sessions 75–78 cover:

1. diagnosis-first tuning and bounded search;
2. valid held-out or out-of-fold ensembling;
3. a full competition simulation from task reading to valid submission;
4. a postmortem and evidence-based readiness decision.

```text
data quality
→ valid split and baseline
→ feature engineering
→ model comparison
→ error diagnosis
→ tuning
→ ensembling
→ fresh-runtime submission validation
```

Optuna and broad automated search are optional tools inside Session 75. They do not replace model understanding, validation independence, reproducibility, or submission checks.

## Readiness Standard

A sophisticated model is not competition-ready unless the student can defend the task, data, split, baseline, metric, experiment history, final artifact, fresh run, and characteristic limitations.
""",
)

write(
    "10_Ready_to_Teach_Pack/Phase_8_Competition_Sprint.md",
    """# Canonical Phase 8 — Tuning, Ensembling, and Competition

**Sessions:** 75–78  
**Canonical entry:** [Phase 8 Session Launcher](../02_Class_Missions/08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md)

This phase begins only after students can defend data quality, validation, model selection, and error analysis.

## Four-Session Sequence

| Session | Focus | Required outcome |
|---:|---|---|
| 75 | diagnosis-first tuning | baseline, diagnosed limitation, controlled experiments, justified parameter decision |
| 76 | model ensembling | aligned held-out or OOF predictions, diversity evidence, best-single comparison, leakage check |
| 77 | full competition simulation | complete workflow, valid artifact, fresh-environment execution, recovery plan |
| 78 | postmortem and readiness conference | evidence-based readiness decision, failure taxonomy, dated next actions |

## Canonical Workflow

```text
task definition
→ data quality and validation
→ reproducible feature pipeline
→ stable baseline and model comparison
→ error diagnosis
→ controlled tuning
→ valid ensembling
→ fresh-runtime submission validation
→ postmortem
```

## Session 75 Rules

- preserve default parameters as the reference;
- state the diagnosed problem before changing a parameter;
- run one controlled manual change at a time;
- record runtime, spread, and keep/reject decision;
- use automated search only after the manual cycle;
- use the [Hyperparameter-Tuning Resource Map](../05_Resources/Hyperparameter_Tuning_Resource_Map.md).

## Session 76 Rules

An ensemble counts only when base models are individually valid, predictions align to identical held-out rows or valid OOF generation, diversity is measured, and the ensemble is compared with the best single model beyond expected validation noise.

## Session 77 Rules

Use the target competition duration. The simulation must include task and schema reading, data/leakage audit, frozen validation, baseline, reproducible pipeline, controlled improvement, error analysis, fresh execution, submission validation, and backup/recovery procedure.

## Session 78 Rules

The student explains what worked, what failed, which evidence is trustworthy, which risk remains highest, and the next three dated actions.

## Non-Negotiable Boundaries

1. Never tune on the hidden test or repeatedly reused final holdout.
2. Tuning follows diagnosis and a stable baseline.
3. Stacking uses out-of-fold predictions.
4. Rejected experiments remain in the record.
5. Complexity stops early enough for fresh-runtime and submission validation.
6. Current official competition rules override repository suggestions.

## Phase Gate

The student independently completes the workflow, produces a valid and reproducible submission, explains major decisions, demonstrates no critical leakage or split failure, and identifies the next improvement without hidden-test feedback.
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

## DeepLearning.AI PyTorch Placement

| Need | Canonical placement |
|---|---|
| tensors, devices, Dataset, DataLoader, and `nn.Module` | [Sessions 59–60](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| autograd and training/validation loops | [Sessions 61–62](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| CNNs, TorchVision, and transfer learning | [Sessions 63–65](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| sequence models, attention, and domain tasks | [Sessions 66–70](../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) |
| optional advanced architecture or deployment material | assign through a named [resource](../05_Resources/README.md) and record the added cohort time |

## Evidence Rule

Students record the exact assigned section, then produce a fresh-run artifact, shape/device evidence, validation result, error analysis, and AI-use note. Passive viewing or copied notebook execution is not completion.
""",
)

print("Removed final obsolete extension-library references.")
