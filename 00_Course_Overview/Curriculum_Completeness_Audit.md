# Curriculum Completeness and Consistency Audit

## Scope

This audit distinguishes repository completeness from classroom and competition readiness.

A repository can have **100% public file-structure and internal-consistency coverage** while still requiring runtime qualification, authenticated-access verification, current-rule verification, private assessment assets, and real classroom pilots.

## Current Repository Structure

| Layer | Current count | Meaning |
|---|---:|---|
| Canonical scheduled pathway | 78 sessions | the recommended dependency-based teaching order |
| Mainline Class Mission bank | 155 lessons | required, selected, remediation, and extension lessons stored in `_Lesson_Library` |
| Bohrium resource hub | 16 lessons | two full-video hub missions plus the fourteen-session 70-minute foundation sequence |
| AI History scheduled phase | 8 seminars | Sessions 33–40 based on Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans* |
| Total public lesson/resource files | 171 | available reusable lesson bank; the eight scheduled reading seminars are tracked separately from the preserved bank count |

## Current Source of Truth

1. `02_Class_Missions/README.md` — canonical nine-phase navigation and session ranges.
2. `00_Course_Overview/Detailed_Lesson_Sequence.md` — canonical scheduled Sessions 1–78.
3. `00_Course_Overview/Pacing_Guide.md` — timing policy, named exceptions, and phase gates.
4. `02_Class_Missions/04_AI_History_and_Thinking_Humans/` — eight scheduled reading seminars.
5. `02_Class_Missions/_Lesson_Library/` — preserved 155-mainline plus 16-resource bank.
6. `10_Ready_to_Teach_Pack/` — teacher delivery, runtime, access, assessment, pilot, and release records.
7. `scripts/validate_curriculum_structure.py` — lesson-bank and structural validation.
8. `scripts/validate_readiness_contract.py` — current pathway, Phase 04, readiness-artifact, and stale-label validation.

Phase summaries and public overview documents must link to these sources rather than maintain competing lesson bodies.

## Public Coverage Standard

The public repository has 100% public file-structure and internal-consistency coverage only when:

- the nine scheduled phases and all 78 session positions are represented consistently;
- Phase 04 contains exactly eight English reading seminars with required reading, mastery targets, misconceptions, the 70-minute cycle, independent reconstruction, exit evidence, and a gate;
- the Phase 04 teacher pack, reading-evidence template, and public rubric exist;
- every indexed lesson-bank file exists and is linked from its module README;
- ordinary lessons identify duration, classroom flow, required evidence, and a specific task;
- long mocks and reproductions identify special duration and deliverables;
- required internal Markdown paths resolve;
- video packages longer than the classroom warm-up are labelled pre-class or separate-session work;
- Kaggle Learn is documented as embedded Andrew ML practice rather than a standalone scheduled Phase 04;
- obsolete generators and obsolete phase folders cannot overwrite or confuse the current curriculum;
- the 78-session, 155-mainline, 16-resource, and 171-bank counts agree across authoritative documents;
- public/private assessment boundaries are explicit;
- runtime, access, pilot, annual-rule, and release-evidence records exist;
- both strict validators pass.

## What Public 100% Does Not Prove

It does not prove that:

- every lesson fits its recorded timing with real students;
- the full pathway has been taught to a complete cohort;
- every authenticated external resource is accessible from every student account or region;
- every notebook runs in the exact Bohrium, school, or competition image;
- current NOAI/IOAI rules permit every package, model, API, pretrained asset, or external dataset;
- the teacher-key repository is private and complete;
- hidden assessment data and scoring packages are secure;
- the curriculum guarantees a competition result.

## Required Release Checks

Before a teaching release:

1. run `python scripts/validate_curriculum_structure.py`;
2. run `python scripts/validate_readiness_contract.py`;
3. run the Ready-to-Teach GitHub Actions workflow;
4. confirm runtime and link records were generated for the release commit;
5. complete `Student_Runtime_Qualification_Record.md` in the exact student environment;
6. complete `External_Access_Verification_Record.md` using intended teacher and student accounts;
7. verify current official competition rules and permitted tools;
8. confirm the teacher-key repository and protected assets are secure;
9. complete the representative pilot matrix and versioned pilot reports;
10. report each readiness dimension separately in release notes.

## Current Claim

When both validators and the maintained-asset workflow pass, the repository may claim:

> **100% public file-structure and internal-consistency coverage for maintained curriculum assets.**

Operational, classroom, access, assessment-security, runtime, and competition-year readiness remain separate evidence-based decisions. See [`10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md`](../10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md) and [`10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md`](../10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md).
