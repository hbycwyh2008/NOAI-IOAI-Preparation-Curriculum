# NOAI / IOAI Preparation Curriculum

A mastery-focused artificial-intelligence curriculum for secondary-school students preparing for NOAI China and later IOAI-style open-ended tasks.

## Start Here

- [Teacher Start Here](TEACHER_START_HERE.md)
- [Student Start Here](STUDENT_START_HERE.md)
- [Class Missions](02_Class_Missions/README.md)
- [Detailed 78-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)
- [Workflow Competency Crosswalk](00_Course_Overview/Workflow_Competency_Crosswalk.md)
- [Machine-Readable Curriculum Specification](curriculum_spec.json)

## Choose an Executable Route

- [NOAI Round 1 Compressed Path](00_Course_Overview/NOAI_Round1_Compressed_Path.md) — exact 45-Session selection plus daily model-recognition practice.
- [NOAI Round 2 Project Path](00_Course_Overview/NOAI_Round2_Project_Path.md) — exact 22-Session continuation after Round 1 qualification, including deferred bridge Sessions 32 and 47.
- [IOAI Full Extension Path](00_Course_Overview/IOAI_Full_Extension_Path.md) — Sessions 1–78 plus current-rule-controlled extension sprints.
- [Canonical Full Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md) — all 78 Sessions in dependency order.

Do not build an undocumented route from vaguely “selected” lessons. Every compressed route states exact Session IDs, prerequisites, assessments, exit evidence, and capability limits.

## Operational Tools

Generate an evidence-aware next-Session plan:

```bash
python scripts/plan_learning_path.py \
  --pathway noai_round1 \
  --completed 1-18 \
  --red 17
```

Generate a deterministic answer-key-free daily model-recognition set:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed
```

See [Pathway and Daily-Drill Operations](09_Teacher_Planning/Pathway_and_Drill_Operations.md). These tools schedule and document work; they do not award mastery or replace evidence review.

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
→ Andrew Ng Deep Learning
   + selected Dive into Deep Learning concept-to-code bridges
   + PyTorch implementation and independent reconstruction
→ model comparison, EDA, features, and evaluation
→ tuning, ensembling, and competition simulation
```

## Modeling Workflow Backbone

Every substantial data or model task uses the same evidence-backed decision loop:

```text
task formalisation
→ data quality
→ feature engineering
→ model selection and baseline
→ diagnosis and controlled tuning
→ ensembling
→ reproducibility check and postmortem
```

The five core competition stages are **data quality → feature engineering → model selection → tuning → ensembling**. They are introduced gradually and then integrated in Sessions 71–78. See the [Workflow Competency Crosswalk](00_Course_Overview/Workflow_Competency_Crosswalk.md).

## Mastery Execution System

- Students maintain the [Student Mastery Dashboard](01_Student_Start/07_Mastery_Dashboard.md) and link every claimed level to reproducible evidence.
- Students complete the [Model Recognition Daily Drills](04_Assessment/Model_Recognition_Drills/README.md): 36 public scenarios, deterministic five-scenario sets, a 15-minute daily protocol, a five-day mastery streak, and a fresh secured confirmation set.
- Teachers use the [Cohort Mastery Review Protocol](09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md) to distinguish completion, reconstruction, and transfer.
- Phase completion does not erase prerequisite debt. Red prerequisites receive a named intervention and delayed recheck.
- Tuning begins only after a trustworthy split, baseline, and written diagnosis. Ensembling begins only after stable single-model evidence.

## Storage Model

```text
numbered Phase
→ SESSION_LAUNCHER.md
→ phase-local lesson packet
```

All canonical lesson bodies for Sessions 1–78 live directly inside their numbered Phase folders. Supporting material lives in the named setup, template, assessment, resource, public-document, teacher-planning, and Ready-to-Teach directories. There is no parallel lesson schedule or canonical storage location.

## Current Architecture

- **78 canonical Sessions** across nine numbered Phases;
- **101 unique phase-local canonical packets** linked by the Session launchers;
- a machine-readable specification validated against launchers, exact routes, recovery bridges, and operational tools;
- three executable NOAI/IOAI routes with exact Session IDs and no duplicated continuation Sessions;
- 36 public daily model-recognition scenarios with deterministic worksheet generation and secured-key rules;
- six required D2L bridge packets embedded inside Phase 6 without adding Sessions;
- eight English AI History seminars in Sessions 33–40;
- an explicit Andrew ML mathematics transition in Sessions 41–43;
- a workflow crosswalk, student mastery dashboard, and cohort review protocol;
- permanent structure, specification, readiness, launcher, hygiene, notebook, code, link, planner, and drill-generator validation.

## Evidence Standard

Watching, reading, or running supplied code is not mastery. Students must recognise, explain, reconstruct, calculate, implement, debug, evaluate, analyse errors, and submit reproducible evidence. D2L code may be used for guided study, but a copied notebook does not satisfy an independent-reconstruction gate.

## Readiness Boundary

Passing repository checks establishes **100% public file-structure and internal-consistency coverage** for maintained assets. It does not establish named-cohort runtime, authenticated account access, legal book/model/data access, private assessment security, representative pilots, full-cohort evidence, or final competition-task alignment. See the [Public Repository Readiness Dashboard](10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md).
