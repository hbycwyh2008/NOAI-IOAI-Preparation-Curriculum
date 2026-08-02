# NOAI / IOAI Preparation Curriculum

A mastery-focused curriculum for secondary-school students preparing for NOAI China and later IOAI-style open-ended artificial-intelligence tasks.

## Canonical Learning Path

```text
CS50P Python
→ NumPy, Pandas, and visualisation
→ 北京市十一学校《中学机器学习十五讲》 on Bohrium
→ AI history and critical reading through
   Melanie Mitchell, Artificial Intelligence: A Guide for Thinking Humans
→ Andrew Ng Machine Learning Specialization
   + StatQuest
   + 3Blue1Brown
   + embedded Kaggle practice
   + model-recognition drills
   + typical model tasks
→ Andrew Ng Deep Learning Specialization
   + PyTorch
   + image, text, audio, and multimodal tasks
→ model comparison
→ EDA and data quality
→ feature engineering
→ model evaluation and error analysis
→ tuning
→ model ensembling
→ full competition simulation
```

The final **Competition sprint** integrates diagnosis-first tuning, model ensembling, fresh-runtime execution, submission validation, and postmortem practice.

## Curriculum Layers

| Layer | Count | Purpose |
|---|---:|---|
| Canonical scheduled pathway | 78 sessions | the actual recommended learning order |
| Scheduled AI History phase | 8 seminars | Sessions 33–40 within the canonical pathway |
| Mainline lesson bank | 155 lessons | deeper practice, remediation, alternatives, and domain extension |
| Bohrium resource bank | 16 lessons | two resource-hub missions plus the fourteen-session Chinese foundation sequence |
| Total public lesson/resource bank files | 171 | selectable material; not an instruction to schedule everything |

## Start Here

- [Students](STUDENT_START_HERE.md)
- [Teachers](TEACHER_START_HERE.md)
- [Class Missions canonical pathway](02_Class_Missions/README.md)
- [Detailed 78-session sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)
- [Course map](00_Course_Overview/Course_Map.md)
- [Pacing guide](00_Course_Overview/Pacing_Guide.md)
- [Phase 04 teacher pack](10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md)
- [Public repository readiness dashboard](10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md)
- [Release readiness gates](10_Ready_to_Teach_Pack/Release_Readiness_Gates.md)

## Validation

For public file-structure and internal-consistency coverage, run:

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
```

The Ready-to-Teach workflow additionally executes all twelve maintained notebooks from fresh kernels, smoke-tests maintained starter code, and checks required public links.

Passing these checks supports the claim:

> **100% public file-structure and internal-consistency coverage for maintained curriculum assets.**

It does not by itself prove exact-student-runtime qualification, authenticated resource access, private assessment security, real-cohort timing, current competition-year alignment, or guaranteed competition performance.

## Classroom Flow

Ordinary classes use:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

The fourteen Bohrium foundation lessons and the eight Melanie Mitchell reading seminars use named 70-minute formats. Long mocks use competition-realistic durations.

## Evidence Standard

Watching a video, finishing a chapter, or running supplied code is not mastery. Students must recognise, explain, reconstruct, debug, apply, analyse errors, and produce reproducible evidence.

## Licensing

Educational materials are copyright © 2026 Wang Morgan. All Rights Reserved. Source-code examples are licensed under the MIT License. See [LICENSE.md](LICENSE.md).
