# Teacher Start Here

## Use One Teaching Order

Begin at [Class Missions — Canonical Learning Pathway](02_Class_Missions/README.md). The phase folders define the scheduled route; `_Lesson_Library` is a bank for selection and remediation, not an alternative sequence.

Use the [canonical teacher phase overviews](09_Teacher_Planning/Phase_Overviews/README.md) for concise planning summaries. Legacy thematic overview files do not define session ranges.

## Required Order

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and Matplotlib — Sessions 13–18
4. 北京市十一学校《中学机器学习十五讲》 on Bohrium — Sessions 19–32
5. AI history and critical reading through Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans* — Sessions 33–40
6. Andrew Ng Machine Learning Specialization with StatQuest, 3Blue1Brown, embedded Kaggle practice, model recognition, and typical tasks — Sessions 41–58
7. Andrew Ng Deep Learning Specialization paired with PyTorch and domain tasks — Sessions 59–70
8. Model comparison, EDA, data quality, feature engineering, evaluation, and error analysis — Sessions 71–74
9. Diagnosis-first tuning, model ensembling, competition simulation, and postmortem — Sessions 75–78

## Planning Steps

1. Archive current official NOAI/IOAI rules and permitted-tool information.
2. Run the student diagnostic.
3. Use the [Detailed 78-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md).
4. Review the [Public Repository Readiness Dashboard](10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md).
5. Ensure that students have legal access to the Melanie Mitchell book before Sessions 33–40.
6. Use the [Phase 4 Teacher Pack](10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md), reading template, and rubric.
7. Select remediation or extension only from linked lesson-library modules.
8. Complete the [External Access Verification Record](10_Ready_to_Teach_Pack/External_Access_Verification_Record.md).
9. Complete the [Student Runtime Qualification Record](10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md).
10. Run both public validators and the Ready-to-Teach workflow.
11. Collect one evidence package per mission.
12. Record representative pilots using the [Representative Pilot Matrix](09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md).
13. Keep solutions, hidden labels, private tests, and calibration material in the private teacher-key repository.
14. Complete the [Release Readiness Gates](10_Ready_to_Teach_Pack/Release_Readiness_Gates.md) before formal graded use.

## Reading-Seminar Rule

Sessions 33–40 assume that assigned pages are read before class. Do not replace the learning cycle with seventy minutes of silent reading. The seminar must preserve retrieval, discussion, entry checking, claim analysis, guided practice, independent reconstruction, and evidence.

## Resource Boundaries

- CS50P is the Python spine.
- Bohrium foundations are completed before the AI-history phase.
- Melanie Mitchell’s book supplies historical context, conceptual boundaries, and evidence-based judgement.
- Kaggle is embedded practice within Andrew Ng ML, not a separate theory phase.
- Andrew Ng ML is paired with just-in-time StatQuest and 3Blue1Brown intuition.
- Model recognition and typical tasks are continuous.
- Andrew Ng DL concepts are paired immediately with PyTorch implementations.
- EDA and evaluation are introduced inside tasks, then systematised after the model curriculum.
- Tuning follows diagnosis; ensembling follows stable single models.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/check_required_links.py
```

Passing automated checks establishes public repository coverage for maintained assets. It does not replace exact-environment qualification, authenticated access, assessment security, current competition rules, or real-classroom evidence.

## Core Delivery Rule

Every ordinary lesson follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

Do not schedule all 171 reusable lesson/resource files.
