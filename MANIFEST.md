# Repository Architecture Manifest

The authoritative structural checks are:

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
```

## Current Counts

| Category | Expected count |
|---|---:|
| Canonical scheduled pathway | 78 sessions |
| Scheduled Phase folders | 9 |
| Phase session launchers | 9 |
| Scheduled AI History seminars | 8 within Sessions 33–40 |
| Mainline lesson files in `_Lesson_Library` | 155 |
| Bohrium resource lessons | 16 |
| Total public lesson/resource bank files | 171 |

## Canonical Content Roots

| Path | Responsibility |
|---|---|
| `00_Course_Overview/` | canonical phases, Sessions 1–78, pacing, and cohort decisions |
| `01_Student_Start/` | student setup and policy |
| `02_Class_Missions/README.md` | single start page for all scheduled teaching |
| `02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md` | usage contract: Phase → Session Launcher → exact lesson |
| `02_Class_Missions/00_...` to `08_.../SESSION_LAUNCHER.md` | exact session-by-session teaching entry points |
| `02_Class_Missions/04_AI_History_and_Thinking_Humans/` | eight scheduled English reading seminars |
| `02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/` | Andrew ML mathematics transition, model sessions, and capstone |
| `02_Class_Missions/_Lesson_Library/` | reusable lesson-body storage, remediation, alternatives, deeper practice, and extensions |
| `02_Class_Missions/_Curriculum_Governance/` | architecture, counts, and audits |
| `03_Templates/` | worksheets, reading evidence, mathematics evidence, experiment logs, model records, and submission checks |
| `04_Assessment/` | public rubrics, evidence standards, and readiness gates |
| `05_Resources/` | external-course maps, exact resource selection, and source guides |
| `06_Starter_Code/` | executable scaffolds and validators |
| `06_Starter_Notebooks/` | generated student-facing notebooks |
| `07_Competition_Projects/` | project briefs by modality |
| `09_Teacher_Planning/` | implementation, timing, pilot, and privacy guidance |
| `10_Ready_to_Teach_Pack/` | delivery, assessment, resource, access, runtime, pilot, and validation records |
| `scripts/` | non-destructive validators and asset utilities |
| `.github/workflows/` | structure, readiness, launcher, notebook, code, runtime, and link validation |

## Normal Delivery Path

```text
02_Class_Missions/README.md
→ assigned Phase
→ SESSION_LAUNCHER.md
→ exact linked lesson
→ required evidence
```

Teachers and students do not browse `_Lesson_Library` manually during normal delivery. A launcher link may open a lesson stored there, but the launcher has already selected the correct file.

## Canonical Source Priority

1. `02_Class_Missions/README.md` for the assigned Phase;
2. the Phase `SESSION_LAUNCHER.md` for the assigned Session and exact lesson;
3. the linked lesson file for classroom cycle, task, evidence, and gate;
4. `00_Course_Overview/Detailed_Lesson_Sequence.md` for whole-course overview;
5. `_Lesson_Library` only for reusable lesson storage, remediation, alternatives, and extensions;
6. `00_Course_Overview/Pacing_Guide.md` for timing policy;
7. `10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md` for dimension-specific readiness claims;
8. `10_Ready_to_Teach_Pack/` for teacher delivery and validation records.

A lesson-library module must not silently become a second scheduled pathway.

## Learning Dependency

```text
CS50P
→ NumPy / Pandas / Matplotlib
→ Bohrium ML foundations
→ AI history and critical-reading phase
→ Andrew Ng ML mathematics transition + models + embedded Kaggle practice
→ Andrew Ng DL + PyTorch + domain tasks
→ comparison + EDA + features + evaluation
→ tuning + ensembling + competition
```

## Public/Private Boundary

The public repository may contain lesson plans, starter assets, templates, public rubrics, and validation procedures. It must not contain answer keys, full teacher solutions, hidden labels, private tests, secure scoring packages, secrets, restricted data, or pre-use calibration examples.

## Release Check

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/check_required_links.py
```

The Ready-to-Teach workflow must also execute all maintained notebooks and starter-code smoke tests. Passing establishes 100% public file-structure and internal-consistency coverage for maintained assets, not automatic real-classroom, authenticated-access, security, runtime, or annual-competition readiness.