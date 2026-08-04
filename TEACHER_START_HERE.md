# Teacher Start Here

## Select the Cohort Route First

Before assigning a Session, choose and record one executable route:

- [NOAI Round 1 Compressed Path](00_Course_Overview/NOAI_Round1_Compressed_Path.md)
- [NOAI Round 2 Project Path](00_Course_Overview/NOAI_Round2_Project_Path.md)
- [IOAI Full Extension Path](00_Course_Overview/IOAI_Full_Extension_Path.md)
- the complete [78-Session canonical sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)

Do not use an undocumented “selected lesson” plan. Record exact Session IDs, prerequisites, pacing, assessment points, exit standard, and capability boundary.

## Normal Teaching Workflow

```text
select the documented route
→ open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the phase-local lesson
→ collect the named evidence
→ review mastery and assign the next action
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

Compressed routes preserve this dependency logic while explicitly omitting named Sessions and limiting the resulting readiness claim.

## Daily Model-Recognition System

From the first model-workflow lesson onward:

1. assign one 15-minute scenario from [Model Recognition Daily Drills](04_Assessment/Model_Recognition_Drills/README.md);
2. require the complete answer record before discussing models;
3. keep detailed solutions and calibration examples private;
4. score sample/X/y/labels, output/task, baseline, metric, candidate families, and validation/leakage risk;
5. require 90% for five consecutive daily sets plus one fresh secured set;
6. after mastery, assign two maintenance drills per week.

Do not accept a model name without output, labels, baseline, metric, validation design, and limitation reasoning.

## Mastery Review Rules

- Distinguish **completion**, **reconstruction**, and **transfer**. Submission alone is not mastery.
- Require each student to maintain the [Student Mastery Dashboard](01_Student_Start/07_Mastery_Dashboard.md).
- Do not average away a Red prerequisite with unrelated strengths.
- When a student advances with unresolved prerequisite debt, name the debt, intervention, recheck task, and due date.
- Run workflow gate reviews at Sessions 18, 24, 41, 57, 58, 70, 74, 77, and 78.
- Do not begin tuning before the student has a trustworthy split, baseline, and written diagnosis.
- Do not retain an ensemble without stable components, diversity evidence, and comparison with the best single model.

## Before Each Cohort

1. archive and review current official NOAI/IOAI rules;
2. run the student diagnostic and select the route;
3. confirm legal book/model/data and authenticated course access;
4. qualify the exact student runtime;
5. pilot every representative lesson type;
6. keep solutions, hidden labels, tests, and calibration material private;
7. complete the release-readiness gates;
8. state external evidence as pending until the actual record is complete.

## Special Phase Rules

- **Sessions 33–40:** assigned reading occurs before class; preserve the full seminar cycle.
- **Sessions 41–43:** use the mathematics bridge from task meaning through symbols, graphs, calculations, code, model behaviour, and limitations.
- **Sessions 71–74:** require the full pre-tuning evidence gate: split, data audit, baseline, feature ledger, ablation, model comparison, and written error diagnosis.
- **Sessions 75–78:** tuning follows diagnosis; ensembling follows stable single-model evidence; the final simulation must run from a fresh environment.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_curriculum_spec.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

Passing automated checks establishes repository-controlled coverage, not named-cohort runtime, authenticated access, representative-pilot, security, or final competition-task evidence.
