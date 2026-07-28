# Curriculum Completeness and Consistency Audit

## Scope

This audit distinguishes repository completeness from classroom and competition readiness.

A repository can have **100% public file-structure coverage** while still requiring runtime validation, current-rule verification, private assessment assets, and real classroom pilots.

## Current Repository Structure

| Layer | Current count | Meaning |
|---|---:|---|
| Mainline Class Mission bank | 155 lessons | Modules 00–26 and Module 28; includes required, selected, remediation, and extension lessons |
| Optional Bohrium resource hub | 16 lessons | two full-video hub missions plus the fourteen-session 70-minute sequence for 北京市十一学校《中学机器学习十五讲》 |
| Total public lesson/resource files | 171 | available lesson bank, not an automatic teaching schedule |
| Core scheduled pathway | 67 sessions | orientation through competition practice and final readiness |
| Competition sprint | 8 sessions | task recognition, data engineering, diagnosis-first tuning, automated search, and final simulation |
| Recommended full pathway | 75 sessions | 67 core sessions plus eight competition-sprint sessions |

## Current Source of Truth

1. `02_Class_Missions/` — canonical lesson content, evidence, and lesson-specific duration.
2. `00_Course_Overview/Detailed_Lesson_Sequence.md` — canonical scheduled Sessions 1–75.
3. `00_Course_Overview/Pacing_Guide.md` — pathway selection and timing policy.
4. `10_Ready_to_Teach_Pack/` — teacher-facing phase indexes, assessment packs, and resource crosswalks.
5. `scripts/validate_curriculum_structure.py` — automated file-count, link, lesson-flow, naming, and consistency checks.

Phase summaries and public overview documents must link to these sources rather than maintain competing lesson bodies.

## Public File-Structure Coverage Standard

The public repository has 100% file-structure coverage only when:

- every indexed module and lesson file exists;
- every lesson is linked from its module README;
- ordinary lessons identify duration, classroom flow, required evidence, and a specific learning target/task;
- long mocks and reproductions identify their special duration and deliverables;
- required internal Markdown paths resolve;
- current resource maps use complete course names;
- video packages longer than the classroom warm-up are labelled pre-class or separate-session work;
- the obsolete V1 generator cannot overwrite the current curriculum;
- the 67-session, eight-session, 75-session, 155-lesson, and 16-resource counts agree across overview documents;
- public/private assessment boundaries are explicit.

## What 100% File-Structure Coverage Does Not Prove

It does not prove that:

- every lesson fits its recorded timing with real students;
- the full pathway has been taught to a complete cohort;
- every current external link is accessible from every student account or region;
- every notebook runs in the exact Bohrium or competition image;
- current NOAI/IOAI rules permit every package, model, API, or external asset;
- the teacher-key repository is private and complete;
- hidden assessment data and scoring packages are secure;
- the curriculum guarantees a competition result.

## Required Release Checks

Before a teaching release:

1. run `python scripts/validate_curriculum_structure.py`;
2. run the Ready-to-Teach GitHub Actions workflow;
3. confirm `Link_Verification_Latest.md` and `Runtime_Validation_Record.md` were generated for the current release;
4. test authenticated course access from a student account;
5. run notebooks and starter scripts in the actual student environment;
6. verify current official competition rules and permitted tools;
7. confirm the teacher-key repository is private before uploading sensitive assets;
8. pilot representative ordinary, video-heavy, project, mock, and sprint lessons.

## Current Claim

The target of this repository-maintenance cycle is **100% public file-structure and internal-consistency coverage**.

Operational, classroom, assessment-security, and annual-rule readiness remain separate evidence-based decisions. See [`10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md`](../10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md).