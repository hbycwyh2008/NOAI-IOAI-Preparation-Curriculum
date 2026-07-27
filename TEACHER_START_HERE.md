# Teacher Start Here

This curriculum is organised around the NOAI syllabus and IOAI-style task demands rather than around any single textbook or video course.

The repository is a curriculum bank. Choose a pathway before scheduling individual lessons.

## Start Here

1. Read [Course Overview](00_Course_Overview/README.md).
2. Choose a route using [Cohort Pathways and Required / Optional Map](00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md).
3. Review the [Pacing Guide](00_Course_Overview/Pacing_Guide.md) and [Detailed 75-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md).
4. Review the [Class Mission Resource Architecture](02_Class_Missions/Class_Mission_Resource_Architecture.md).
5. Read the [Curriculum Readiness Audit](10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md).

## Core Design Rules

- Every ordinary 75-minute after-school club lesson follows: **Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**.
- The fourteen-session 北京市十一学校《中学机器学习十五讲》 sequence is a named 70-minute exception.
- Long mocks and reproductions use competition-realistic durations.
- Use one exact required resource segment per ordinary mission.
- Write the complete course name, exact module/week/video/chapter/timestamp, and required student action.
- Official NOAI/IOAI rules and tasks determine scope and constraints.
- 北京市十一学校《中学机器学习十五讲》 and 台湾大学李宏毅《机器学习》内容精选版 are used where they align strongly with the competition pathway; English resources and official documentation are selected where they provide stronger implementation or clarification.
- Round 1 lessons must include paper-based questions, concept explanations, calculations, code reading, or code completion.
- Round 2 lessons must produce executable code, valid evaluation evidence, error analysis, and reproducibility records.
- Complete solutions, hidden labels, private test data, scoring keys, and calibration examples remain in the private teacher-key repository.

## Curriculum Layers

| Layer | Count | Use |
|---|---:|---|
| Core scheduled pathway | 67 sessions | compressed full NOAI route |
| Competition sprint | 8 sessions | task recognition, data engineering, tuning, and full simulation |
| Recommended full pathway | 75 sessions | core plus sprint |
| Mainline mission bank | 155 lessons | deeper practice, reteaching, alternatives, and extension |
| Optional Bohrium resource hub | 16 lessons | full-video and 70-minute sequence resources |

Do not schedule all lesson files automatically.

## Recommended Implementation Order

1. Archive the current official rules, syllabus, task format, and permitted-tool information.
2. Run the student diagnostic and identify Python, mathematics, and modelling prerequisites.
3. Select the Round 1, full NOAI, full competition, or IOAI-extension pathway.
4. Mark required lessons, optional remediation lessons, phase gates, and long simulations.
5. Verify every external course segment and authenticated link.
6. Run starter notebooks and scripts in the exact student environment.
7. Assign one class mission at a time and collect evidence.
8. Use the [Evidence System](04_Assessment/Evidence_System.md) and [Readiness Checklist](04_Assessment/Readiness_Checklist.md).
9. Schedule Round 1 and Round 2 mocks.
10. Finish with [Module 28 — Competition Sprint](02_Class_Missions/28-competition-sprint-task-data-tuning/README.md) when students can already build a valid baseline.

## Competition Sprint

Use:

- [Phase 8 — Competition Sprint](10_Ready_to_Teach_Pack/Phase_8_Competition_Sprint.md)
- [Hyperparameter-Tuning Video Resource Map](02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md)
- [Competition Sprint Experiment Log Template](03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [Competition Sprint Submission Checklist](03_Templates/Competition_Sprint_Submission_Checklist.md)
- [Competition Sprint Starter Code](06_Starter_Code/ready_to_teach/README.md)

Do not permit automated tuning before students can justify the metric, split, baseline, manual experiment, and search space.

## Separation of Repositories

- **Curriculum repository:** student-facing missions, resources, templates, starter code, public validation records.
- **Teacher-key repository:** answers, reference implementations, hidden labels, private test data, scoring notes, and secure assessment packages.

Confirm the teacher-key repository is private before uploading sensitive materials.