# Teacher Start Here

## Select the Cohort Route First

Before assigning a Session, choose and record one executable route:

- [NOAI Round 1 Compressed Path](00_Course_Overview/NOAI_Round1_Compressed_Path.md) — 45 Sessions;
- [NOAI Round 2 Project Path](00_Course_Overview/NOAI_Round2_Project_Path.md) — 22 additional Sessions after inspected Round 1 qualification;
- [IOAI Full Extension Path](00_Course_Overview/IOAI_Full_Extension_Path.md) — Sessions 1–78 plus rule-controlled extension sprints;
- the complete [78-Session canonical sequence](00_Course_Overview/Detailed_Lesson_Sequence.md).

Do not use an undocumented “selected lesson” plan. Record exact Session IDs, prerequisites, pacing, assessment points, exit standard, and capability boundary.

## Create or Migrate the Student Progress Ledger

Use one pseudonymous ledger in each student’s private course repository:

```bash
python scripts/manage_student_progress.py init \
  --path student-progress/student-001.json \
  --student-id student-001 \
  --pathway noai_round1
```

For a schema-v1 ledger:

```bash
python scripts/manage_student_progress.py migrate \
  --path student-progress/student-001.json
```

The schema-v2 ledger records route state, Red debt, qualifications, one daily assignment per date, dual accuracy scores, total score, and private-confirmation status. Never store a real name, email address, private answer key, credential, hidden label, or secured-set content.

## Generate the Current Progress Report

After reviewing evidence and updating the ledger:

```bash
python scripts/report_student_progress.py \
  --progress student-progress/student-001.json \
  --output reports/student-001-progress.md
```

The report separates pathway progress, Red debt, pending reviews, public streak eligibility, secured confirmation, and maintenance. It calculates eligibility from declared ledger evidence; it does not inspect answers or award pathway qualification.

## Generate the Next-Session Plan

```bash
python scripts/plan_learning_path.py \
  --progress student-progress/student-001.json \
  --limit 6
```

The planner exposes entry blockers, Red debt, deferred recovery Sessions, and the next workflow checkpoint. See [Pathway and Daily-Drill Operations](09_Teacher_Planning/Pathway_and_Drill_Operations.md).

## Normal Teaching Workflow

```text
select the documented route
→ inspect evidence and update the progress ledger
→ generate the progress report and next-Session plan
→ open Class Missions and the Phase launcher
→ teach the phase-local lesson
→ collect named evidence
→ record completion or Red debt
→ schedule delayed retrieval
```

Begin at [Class Missions](02_Class_Missions/README.md) and read [How to Use Class Missions](02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md). Use the [canonical teacher phase overviews](09_Teacher_Planning/Phase_Overviews/README.md) for planning summaries; they do not replace Session launchers.

Use the [Workflow Competency Crosswalk](00_Course_Overview/Workflow_Competency_Crosswalk.md) to keep the modeling decision process visible across all Phases. Use the [Cohort Mastery Review Protocol](09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md) to convert evidence into remediation, promotion, and spaced-retrieval decisions.

## Canonical Order

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and visualisation — Sessions 13–18
4. Bohrium ML foundations — Sessions 19–32
5. AI History and Thinking Humans — Sessions 33–40
6. Andrew Ng ML, mathematics, model labs, and embedded practice — Sessions 41–58
7. Andrew Ng DL and PyTorch — Sessions 59–70
8. Model comparison, EDA, features, and evaluation — Sessions 71–74
9. Tuning, ensembling, simulation, and postmortem — Sessions 75–78

Compressed routes preserve dependency logic while explicitly omitting named Sessions and limiting readiness claims. Round 1 completes Session 57 before Session 58. Round 2 first recovers Sessions 32 and 47, then continues with 59–78.

## Daily Model-Recognition System

Generate and record one worksheet per assigned study day:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/student-001/YYYY-MM-DD.md
```

The same recorded date always restores the same assignment; a different second set on that date is rejected.

After review, record both required dimensions:

```bash
python scripts/manage_student_progress.py score-drill \
  --path student-progress/student-001.json \
  --set-id 0123456789 \
  --task-family-accuracy 0.9 \
  --baseline-metric-accuracy 0.9 \
  --score-percent 90
```

Recognition mastery requires:

1. five consecutive reviewed sets with task-family accuracy ≥90%;
2. the same five sets with baseline/metric accuracy ≥90%;
3. a fresh private secured set administered after the streak;
4. `confirm-recognition` recorded only after that private pass;
5. two qualifying mixed maintenance sets per seven-day window after confirmation.

Do not accept a model name without output, labels, baseline, metric, validation design, and limitation reasoning. Public streak evidence is eligibility for secured confirmation, not mastery by itself.

## Mastery Review Rules

- Distinguish **completion**, **reconstruction**, **transfer**, **public eligibility**, and **private confirmation**.
- Require the [Student Mastery Dashboard](01_Student_Start/07_Mastery_Dashboard.md) and schema-v2 private ledger.
- Do not average away a Red prerequisite with unrelated strengths.
- When a student advances with unresolved debt, name the debt, intervention, recheck task, and due date.
- Run workflow gate reviews at Sessions 18, 24, 41, 57, 58, 70, 74, 77, and 78.
- Do not begin tuning before a trustworthy split, baseline, and written diagnosis.
- Do not retain an ensemble without stable components, diversity evidence, and comparison with the best single model.

## Before Each Cohort

1. archive and review current official NOAI/IOAI rules;
2. run the student diagnostic and select the route;
3. create pseudonymous private progress ledgers;
4. confirm legal book/model/data and authenticated course access;
5. qualify the exact student runtime;
6. pilot every representative lesson type;
7. keep solutions, hidden labels, tests, and calibration material private;
8. complete the release-readiness gates;
9. state external evidence as pending until the actual record is complete.

## Special Phase Rules

- **Sessions 33–40:** assigned reading occurs before class; preserve the full seminar cycle.
- **Sessions 41–43:** translate task meaning through symbols, graphs, calculations, code, model behaviour, and limitations.
- **Sessions 71–74:** require split, data audit, baseline, feature ledger, ablation, model comparison, and written error diagnosis.
- **Sessions 75–78:** tuning follows diagnosis; ensembling follows stable single-model evidence; final simulation runs from a fresh environment.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_curriculum_spec.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/manage_student_progress.py --self-test
python scripts/report_student_progress.py --self-test
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/check_required_links.py
```

Passing automated checks establishes repository-controlled coverage, not named-cohort runtime, authenticated access, representative-pilot, security, or final competition-task evidence.
