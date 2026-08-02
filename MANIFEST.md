# Repository Architecture Manifest

The authoritative structural check is:

```bash
python scripts/validate_curriculum_structure.py
```

## Current Counts

| Category | Expected count |
|---|---:|
| Canonical scheduled pathway | 78 sessions |
| Mainline lesson files in `_Lesson_Library` | 155 |
| Bohrium resource lessons | 16 |
| Total public lesson/resource files | 171 |

## Canonical Content Roots

| Path | Responsibility |
|---|---|
| `00_Course_Overview/` | canonical phases, Sessions 1–75, pacing, and cohort decisions |
| `01_Student_Start/` | student setup and policy |
| `02_Class_Missions/00_...` to `08_...` | scheduled phase navigation, resource roles, and gates |
| `02_Class_Missions/_Lesson_Library/` | reusable lesson bank, remediation, alternatives, deeper practice, and extensions |
| `02_Class_Missions/_Curriculum_Governance/` | architecture, counts, and audits |
| `03_Templates/` | worksheets, experiment logs, model records, and submission checks |
| `04_Assessment/` | public rubrics, evidence, and readiness gates |
| `05_Resources/` | external-course maps, exact resource selection, and source guides |
| `06_Starter_Code/` | executable scaffolds and validators |
| `06_Starter_Notebooks/` | generated student-facing notebooks |
| `07_Competition_Projects/` | project briefs by modality |
| `09_Teacher_Planning/` | implementation, timing, pilot, and privacy guidance |
| `10_Ready_to_Teach_Pack/` | delivery, assessment, resource, and validation records |
| `scripts/` | non-destructive validators and asset utilities |
| `.github/workflows/` | structure, notebook, code, runtime, and link validation |

## Canonical Source Priority

1. `00_Course_Overview/Detailed_Lesson_Sequence.md` for scheduled order;
2. `02_Class_Missions/README.md` and phase folders for prerequisites, resource roles, and gates;
3. `_Lesson_Library` for lesson bodies and evidence;
4. `00_Course_Overview/Pacing_Guide.md` for timing policy;
5. `10_Ready_to_Teach_Pack/` for teacher delivery and validation records.

A lesson-library module must not silently become a second scheduled pathway.

## Learning Dependency

```text
CS50P
→ NumPy / Pandas / Matplotlib
→ Bohrium ML foundations
→ AI history and critical-reading phase
→ Andrew Ng ML + mathematics intuition + model labs
→ Andrew Ng DL + PyTorch + domain tasks
→ comparison + EDA + features + evaluation
→ tuning + ensembling + competition
```

## Public/Private Boundary

The public repository may contain lesson plans, starter assets, templates, public rubrics, and validation procedures. It must not contain answer keys, full teacher solutions, hidden labels, private tests, secure scoring packages, or pre-use calibration examples.

## Release Check

```bash
python scripts/validate_curriculum_structure.py
python scripts/check_required_links.py
```

The Ready-to-Teach workflow must also execute all maintained notebooks and starter-code smoke tests. Passing establishes repository consistency, not automatic real-classroom or annual-competition readiness.
