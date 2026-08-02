from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Run the main cleanup migration first.
runpy.run_path(str(ROOT / "scripts/apply_repository_cleanup.py"), run_name="__main__")


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


# The phase-local migration left no maintained lesson bodies in the former library.
# Do not recreate a misleading empty layer.
library = ROOT / "02_Class_Missions/_Lesson_Library"
if library.exists():
    import shutil
    shutil.rmtree(library)

write(
    "README.md",
    """# NOAI / IOAI Preparation Curriculum

A mastery-focused artificial-intelligence curriculum for secondary-school students preparing for NOAI China and later IOAI-style open-ended tasks.

## Start Here

- [Teacher Start Here](TEACHER_START_HERE.md)
- [Student Start Here](STUDENT_START_HERE.md)
- [Class Missions](02_Class_Missions/README.md)
- [Detailed 78-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)

## Canonical Learning Path

```text
CS50P Python
→ NumPy, Pandas, and visualisation
→ Bohrium machine-learning foundations
→ AI history and critical reading with Melanie Mitchell
→ Andrew Ng Machine Learning
   + Sessions 41–43 mathematics transition
   + StatQuest and 3Blue1Brown
   + embedded Kaggle practice
   + model recognition and typical tasks
→ Andrew Ng Deep Learning + PyTorch
→ model comparison, EDA, features, and evaluation
→ tuning, ensembling, and competition simulation
```

## Storage Model

```text
numbered Phase
→ SESSION_LAUNCHER.md
→ phase-local lesson packet
```

All canonical lesson bodies for Sessions 1–78 live directly inside their numbered Phase folders. Supporting material lives in the named setup, template, assessment, resource, public-document, teacher-planning, and Ready-to-Teach directories. There is no parallel lesson-library schedule.

## Current Architecture

- **78 canonical Sessions** across nine numbered Phases;
- **95 unique phase-local Markdown packets** linked by the Session launchers;
- eight English AI History seminars in Sessions 33–40;
- an explicit Andrew ML mathematics transition in Sessions 41–43;
- permanent structure, readiness, launcher, hygiene, notebook, code, and link validation.

## Evidence Standard

Watching, reading, or running supplied code is not mastery. Students must recognise, explain, reconstruct, calculate, implement, debug, evaluate, analyse errors, and submit reproducible evidence.

## Readiness Boundary

Passing repository checks establishes **100% public file-structure and internal-consistency coverage** for maintained assets. Exact student runtime, authenticated access, legal book access, private assessment security, representative pilots, full-cohort evidence, and current competition rules remain separate gates.
""",
)

write(
    "02_Class_Missions/README.md",
    """# Class Missions — Start Here

## Normal Use

```text
choose the assigned Phase
→ open its Session Launcher
→ click the assigned Session
→ teach or complete that lesson
→ submit the named evidence
```

Read [How to Use Class Missions](HOW_TO_USE_CLASS_MISSIONS.md) once before teaching the course.

## Canonical 78-Session Route

| Phase | Sessions | Open this launcher | Main outcome |
|---:|---:|---|---|
| 0 — Orientation and Evidence | 1–2 | [Launch Sessions 1–2](00_Orientation_and_Evidence/SESSION_LAUNCHER.md) | tools, workflow, evidence, and baseline discipline |
| 1 — CS50P Python | 3–12 | [Launch Sessions 3–12](01_CS50P_Python/SESSION_LAUNCHER.md) | independent Python programming, testing, debugging, and CSV work |
| 2 — NumPy, Pandas, and Visualisation | 13–18 | [Launch Sessions 13–18](02_NumPy_Pandas_Visualisation/SESSION_LAUNCHER.md) | arrays, DataFrames, data quality, plots, and a fresh-run audit notebook |
| 3 — Bohrium ML Foundations | 19–32 | [Launch Sessions 19–32](03_Bohrium_ML_Foundations/SESSION_LAUNCHER.md) | Chinese-language ML concept foundation |
| 4 — AI History and Thinking Humans | 33–40 | [Launch Sessions 33–40](04_AI_History_and_Thinking_Humans/SESSION_LAUNCHER.md) | AI history, claim auditing, evidence, and conceptual limits |
| 5 — Andrew Ng ML and Model Labs | 41–58 | [Launch Sessions 41–58](05_Andrew_Ng_ML_Model_Labs/SESSION_LAUNCHER.md) | mathematics transition, classical models, embedded practice, and model cards |
| 6 — Andrew Ng DL and PyTorch | 59–70 | [Launch Sessions 59–70](06_Andrew_Ng_DL_PyTorch/SESSION_LAUNCHER.md) | deep-learning concepts paired with PyTorch and domain tasks |
| 7 — Model Comparison, EDA, and Evaluation | 71–74 | [Launch Sessions 71–74](07_Model_Comparison_EDA_Evaluation/SESSION_LAUNCHER.md) | model selection, systematic EDA, features, validation, and error analysis |
| 8 — Tuning, Ensembling, and Competition | 75–78 | [Launch Sessions 75–78](08_Tuning_Ensembling_Competition/SESSION_LAUNCHER.md) | tuning, ensembling, full simulation, and readiness decision |

## Supporting Areas

- [Student setup and evidence](../01_Student_Start/README.md)
- [Templates](../03_Templates/README.md)
- [Assessment](../04_Assessment/README.md)
- [Resources](../05_Resources/README.md)
- [Teacher planning](../09_Teacher_Planning/README.md)
- [Ready-to-Teach records](../10_Ready_to_Teach_Pack/README.md)
- [Repository Architecture Manifest](../MANIFEST.md)

These supporting areas do not create a second teaching order.
""",
)

write(
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    """# How to Use Class Missions

## The Only Normal Teaching Path

```text
02_Class_Missions
→ open the assigned numbered Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the phase-local lesson packet
→ collect the named evidence
```

Every canonical lesson body for Sessions 1–78 is stored directly inside its numbered Phase folder.

## What Each Layer Means

| Layer | Who uses it | Purpose |
|---|---|---|
| numbered Phase folder | teacher and student | canonical order and lesson bodies |
| `SESSION_LAUNCHER.md` | teacher and student | exact Session entry point |
| phase-local Session file | teacher and student | classroom cycle, tasks, evidence, and gate |
| setup/templates/assessment/resources | teacher and student when linked | supporting material only |
| teacher-planning and Ready-to-Teach folders | teacher or maintainer | planning, pilots, security, release evidence, and maintenance |

## Normal Class Workflow

1. The teacher announces the Phase and Session number.
2. Everyone opens the numbered Phase folder.
3. Everyone opens `SESSION_LAUNCHER.md`.
4. Everyone opens the linked phase-local Session packet.
5. Students use only the resources and templates linked by that packet.
6. The teacher collects the named evidence.
7. The class advances only after the Session or Phase gate is satisfied.

## What Not to Do

- Do not invent a second Session order from resource maps or teacher notes.
- Do not treat a historical module number as a canonical Session number.
- Do not teach from architecture or readiness records.
- Do not add optional material to the canonical schedule without recording the cohort decision.

## Source-of-Truth Rule

- **Schedule and lesson bodies:** numbered Phase folders.
- **Exact entry point:** each Phase `SESSION_LAUNCHER.md`.
- **Supporting material:** the named setup, template, assessment, resource, and teacher directories.
- **Architecture and validation:** [Repository Architecture Manifest](../MANIFEST.md).
""",
)

write(
    "TEACHER_START_HERE.md",
    """# Teacher Start Here

## Normal Teaching Workflow

```text
open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the phase-local lesson
→ collect the named evidence
```

Begin at [Class Missions](02_Class_Missions/README.md) and read [How to Use Class Missions](02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md). Use the [canonical teacher phase overviews](09_Teacher_Planning/Phase_Overviews/README.md) for planning summaries; they do not replace Session launchers.

## Required Order

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and visualisation — Sessions 13–18
4. Bohrium ML foundations — Sessions 19–32
5. AI History and Thinking Humans — Sessions 33–40
6. Andrew Ng ML, mathematics, model labs, and embedded practice — Sessions 41–58
7. Andrew Ng DL and PyTorch — Sessions 59–70
8. Model comparison, EDA, features, and evaluation — Sessions 71–74
9. Tuning, ensembling, simulation, and postmortem — Sessions 75–78

## Before Each Cohort

1. archive current official NOAI/IOAI rules;
2. run the student diagnostic;
3. confirm legal book and authenticated course access;
4. qualify the exact student runtime;
5. pilot representative lesson types;
6. keep solutions, hidden labels, tests, and calibration material private;
7. complete the release-readiness gates.

## Special Phase Rules

- **Sessions 33–40:** assigned reading occurs before class; preserve the full seminar cycle.
- **Sessions 41–43:** use the mathematics bridge from task meaning through symbols, graphs, calculations, code, model behaviour, and limitations.
- **Sessions 75–78:** tuning follows diagnosis; ensembling follows stable single-model evidence; the final simulation must run from a fresh environment.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

Passing automated checks establishes public repository coverage, not cohort-specific operational readiness.
""",
)

write(
    "STUDENT_START_HERE.md",
    """# Student Start Here

Your teacher assigns one Phase and one Session at a time.

```text
open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ complete the lesson and evidence
```

Start at [Class Missions](02_Class_Missions/README.md). Canonical lessons are stored directly inside their numbered Phase folders.

## Learning Route

```text
CS50P Python
→ NumPy / Pandas / visualisation
→ Bohrium ML foundations
→ AI history and critical reading
→ Andrew Ng ML mathematics + models + embedded practice
→ Andrew Ng DL + PyTorch
→ model comparison, EDA, features, and evaluation
→ tuning, ensembling, and competition
```

## Ordinary Class Cycle

1. Skill Warm-Up
2. Talk Robin 1
3. Entry Check
4. Core Pattern
5. Guided Practice
6. Independent Rebuild
7. Talk Robin 2 + Evidence

Watching, reading, or running an example once is not completion. You must explain, reconstruct, test, modify, analyse errors, and record evidence.

## Special Evidence

- Sessions 33–40 require pre-class reading evidence from Melanie Mitchell’s book.
- Sessions 41–43 require equation, graph, hand-calculation, shape, and code translation evidence.
- Every model task begins by identifying `X`, `y`, output, labels, baseline, metric, mathematical objects, and limitations.

## First Steps

Open the [Student Setup and Evidence Index](01_Student_Start/README.md), complete the assigned setup records, then open today’s Phase launcher.
""",
)

write(
    "MANIFEST.md",
    """# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 95 unique phase-local Markdown packets |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |

## Source Priority

1. `02_Class_Missions/README.md` — canonical Phase order;
2. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
3. phase-local Session packet — classroom cycle, task, evidence, and gate;
4. linked templates, assessments, and resource maps — supporting material;
5. `00_Course_Overview/` — pacing and pathway summaries;
6. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning and release evidence.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, phase-local canonical links, valid internal paths and anchors, distinct canonical packets, current indexes, and an explicit operational-readiness boundary.
""",
)

write(
    "10_Ready_to_Teach_Pack/Repository_Cleanup_Audit.md",
    """# Repository Cleanup Audit

## Scope

The cleanup reviewed files, navigation, internal links and anchors, duplicate canonical lessons, stale architecture language, historical branches, and open Issues.

## Changes Applied

- removed two merged historical agent branches;
- removed obsolete generator fragments and pre-publication instructions;
- removed legacy phase summaries and old Ready-to-Teach lesson copies;
- removed the empty former lesson-library layer and every maintained reference to it;
- repaired discovered internal links and the Andrew ML mathematics anchor;
- replaced three exact duplicate canonical packets with phase-specific lessons;
- added concise indexes for setup, templates, assessment, resources, public documents, diagnostics, pilots, and readiness records;
- centralised hyperparameter-tuning resources;
- rewrote selected-content maps for current phase-local paths;
- added permanent repository-hygiene validation to CI.

## Current Navigation

```text
Phase
→ SESSION_LAUNCHER.md
→ phase-local Session packet
```

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

Repository hygiene does not replace exact runtime qualification, authenticated access, private assessment security, representative pilots, full-cohort evidence, or current competition-year verification.
""",
)

# Remove remaining stale lesson-library language from maintained Markdown files.
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8", errors="replace")
    if "_Lesson_Library" not in text:
        continue
    text = text.replace("`_Lesson_Library`", "the former extension library")
    text = text.replace("_Lesson_Library", "the-former-extension-library")
    path.write_text(text, encoding="utf-8")

# Correct the hygiene contract for the fully phase-local architecture.
hygiene = ROOT / "scripts/validate_repository_hygiene.py"
text = hygiene.read_text(encoding="utf-8")
text = text.replace('    "02_Class_Missions/_Lesson_Library/README.md",\n', "")
text = text.replace(
    '    re.compile(r"04_Kaggle_ML_Refresh", re.IGNORECASE),\n',
    '    re.compile(r"04_Kaggle_ML_Refresh", re.IGNORECASE),\n    re.compile(r"_Lesson_Library", re.IGNORECASE),\n',
)
hygiene.write_text(text, encoding="utf-8")

# Ensure coverage definition and current overview contain no obsolete extension-layer contract.
replace(
    "09_Teacher_Planning/Public_Repo_100_Percent_Readiness_Definition.md",
    [
        (
            "10. `_Lesson_Library` contains extension/remediation material only and has a current index.\n11.",
            "10. Supporting setup, template, assessment, resource, planning, and readiness directories have current indexes.\n11.",
        )
    ],
)

print("Applied fully phase-local cleanup corrections.")
