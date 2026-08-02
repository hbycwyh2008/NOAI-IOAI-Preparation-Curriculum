# Teacher Start Here

## Normal Teaching Workflow

```text
open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the exact linked lesson
→ collect the named evidence
```

Begin at [Class Missions — Start Here](02_Class_Missions/README.md) and read [How to Use Class Missions](02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md).

Do **not** browse `_Lesson_Library` to choose a class. The library is a storage bank for lesson bodies, remediation, extension, and maintenance; the Phase launchers define the scheduled route.

Use the [canonical teacher phase overviews](09_Teacher_Planning/Phase_Overviews/README.md) for planning summaries. They do not replace the session launchers.

## Required Order

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and Matplotlib — Sessions 13–18
4. 北京市十一学校《中学机器学习十五讲》 on Bohrium — Sessions 19–32
5. AI history and critical reading through Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans* — Sessions 33–40
6. Andrew Ng Machine Learning, mathematics transition, StatQuest, 3Blue1Brown, embedded Kaggle practice, model recognition, and typical tasks — Sessions 41–58
7. Andrew Ng Deep Learning paired with PyTorch and domain tasks — Sessions 59–70
8. Model comparison, EDA, data quality, feature engineering, evaluation, and error analysis — Sessions 71–74
9. Diagnosis-first tuning, model ensembling, competition simulation, and postmortem — Sessions 75–78

## Planning Steps

1. Archive current official NOAI/IOAI rules and permitted-tool information.
2. Run the student diagnostic.
3. Open the assigned Phase launcher rather than selecting a lesson-bank module.
4. Use the [Detailed 78-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md) only as an overview.
5. Review the [Public Repository Readiness Dashboard](10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md).
6. Confirm legal book access before Sessions 33–40 and use the [Phase 4 Teacher Pack](10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md).
7. Before Session 41, run the mathematics diagnostic and use the [Phase 5 Mathematics Teacher Pack](10_Ready_to_Teach_Pack/Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md).
8. Select remediation or extension from `_Lesson_Library` only after a launcher/lesson identifies the need.
9. Complete the [External Access Verification Record](10_Ready_to_Teach_Pack/External_Access_Verification_Record.md).
10. Complete the [Student Runtime Qualification Record](10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md).
11. Collect one evidence package per session.
12. Record representative pilots using the [Representative Pilot Matrix](09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md).
13. Keep solutions, hidden labels, private tests, and calibration material in the private teacher-key repository.
14. Complete the [Release Readiness Gates](10_Ready_to_Teach_Pack/Release_Readiness_Gates.md) before formal graded use.

## Special Phase Rules

### Sessions 33–40 — Reading Seminars

Assigned pages are read before class. Preserve retrieval, discussion, entry checking, claim analysis, guided practice, independent reconstruction, and evidence.

### Sessions 41–43 — Andrew ML Mathematics Transition

Do not add a disconnected university-mathematics prerequisite and do not skip mathematics. Use the bridge:

```text
task
→ notation and shapes
→ prediction
→ loss/objective
→ gradient or rule
→ metric
→ code
→ limitations
```

Students must translate equations into task language and code, perform small calculations, and explain gradient direction and scale effects.

## Resource Boundaries

- CS50P is the Python spine.
- Bohrium foundations precede the AI-history and Andrew ML phases.
- Melanie Mitchell supplies historical context and evidence-based judgement.
- Kaggle is embedded practice inside Andrew ML, not a separate phase.
- StatQuest and 3Blue1Brown are selected just in time.
- Andrew Ng DL concepts are paired immediately with PyTorch.
- Tuning follows diagnosis; ensembling follows stable single models.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/check_required_links.py
```

Passing automated checks establishes public repository coverage for maintained assets. It does not replace exact-environment qualification, authenticated access, assessment security, current competition rules, or real-classroom evidence.

## Core Delivery Rule

Every ordinary lesson follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**