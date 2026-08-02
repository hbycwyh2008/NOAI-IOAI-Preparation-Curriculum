# Public Repository 100 Percent Coverage Definition

This file defines what **100% public file-structure and internal-consistency coverage** means for the student-facing NOAI / IOAI preparation repository.

For compatibility with existing validator terminology, this standard includes **100% public file-structure coverage**. The current contract is stricter because it additionally requires pathway, readiness-artifact, and source-of-truth consistency.

It deliberately does not use the phrase “100% ready” as a blanket claim. Runtime reliability, authenticated access, current-rule alignment, private assessment security, and real classroom evidence are evaluated separately.

## Public Coverage Is 100% When

1. The canonical pathway contains nine dependency-based phases and 78 scheduled sessions.
2. Every scheduled phase has a clear role, prerequisites, sequence, evidence, and advancement gate.
3. Phase 04 is the eight-session **AI History and Thinking Humans** reading sequence.
4. Each Phase 04 lesson identifies required reading, required mastery, misconceptions, the 70-minute learning cycle, independent reconstruction, exit evidence, and a gate.
5. Phase 04 has a teacher delivery pack, student reading-evidence template, public rubric, and representative pilot requirement.
6. Kaggle Learn is positioned as embedded Andrew ML practice rather than a separate scheduled Phase 04.
7. Every mainline lesson-bank module has a realistic lesson sequence.
8. Every listed lesson has a corresponding student-facing file and is linked from its module README.
9. Every ordinary lesson identifies its duration and uses the classroom flow:

   **Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

10. Every lesson states required evidence and a specific student task.
11. Long contest sessions state competition-realistic duration and deliverables.
12. Full-video Bohrium lessons have explicit single-session, two-session, or named-exception handling.
13. 北京市十一学校《中学机器学习十五讲》 is split into fourteen concrete 70-minute resource lessons.
14. Round 1 preparation includes code reading, calculation, distractor, short-answer, timed-mock, and correction structures.
15. Round 2 preparation includes data audit, validation, baseline, controlled experiment, error analysis, submission, fresh-runtime, and postmortem structures.
16. The competition sprint includes task recognition, data engineering, classical tuning, deep-learning tuning, optional automated search, efficiency constraints, ensembling, and a full simulation.
17. Worksheet, reading-evidence, experiment-log, notebook-lab, and submission-check templates exist.
18. Public assessment rubrics exist for the maintained student-facing evidence types.
19. Starter notebooks and executable starter-code coverage exist for coding-heavy work.
20. Internal Markdown links and selected-content-map file paths resolve.
21. Required resource instructions use complete course names and exact sections, chapters, videos, pages, or timestamps.
22. Resource packages longer than an in-class warm-up are marked as pre-class or separate-session work.
23. The obsolete V1 generator and obsolete standalone Kaggle phase cannot rewrite or confuse the current curriculum.
24. The public/private teacher-key boundary is explicit.
25. Validation, runtime, authenticated-access, link, annual-rule, pilot, and release records exist.
26. All authoritative overview documents report the same 78-session pathway and the same 155-mainline, 16-resource, and 171-bank counts.
27. `scripts/validate_curriculum_structure.py` passes.
28. `scripts/validate_readiness_contract.py` passes.

## Assets That Remain Private

These are required for live graded use but must not be placed in the public student-facing repository:

- answer keys;
- full solutions and model notebooks;
- hidden labels;
- private test sets;
- protected scored-assessment rubrics or calibration examples before use;
- teacher calibration examples;
- secure scoring and leaderboard packages;
- secrets, tokens, and restricted competition data.

## Separate Readiness Decisions

A 100% public-coverage result does not prove:

- successful execution in the exact student environment;
- authenticated access to every external course or legal access to the Phase 04 book;
- current official permission for packages, APIs, pretrained models, external data, or internet use;
- successful real-cohort timing and English reading load;
- assessment-security completion;
- full-pathway delivery;
- guaranteed competition performance.

Use `10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md` and `10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md` for those decisions.

## Validation Rule

`02_Class_Missions/_Curriculum_Governance/Lesson_Distribution_Audit.md`, `scripts/validate_curriculum_structure.py`, and `scripts/validate_readiness_contract.py` may report 100% **public file-structure and internal-consistency coverage** only. They must not convert that result into a blanket operational-readiness claim.
