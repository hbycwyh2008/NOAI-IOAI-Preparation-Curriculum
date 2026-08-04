# Ready-to-Teach Pack Index

Canonical teaching begins in [Class Missions](../02_Class_Missions/README.md). This folder contains delivery support, evidence boundaries, and release records, not a second lesson sequence.

## Canonical Delivery Packs

- [Phase 4 — AI History and Thinking Humans](Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew ML Mathematics Bridge](Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md)
- [Phase 8 — Tuning, Ensembling, and Competition](Phase_8_Competition_Sprint.md)

## Resource Crosswalks

- [Resource and Syllabus Crosswalk](Resource_Map_and_Syllabus_Crosswalk.md)
- [Deep Learning Specialization Selected Content](DLS_Selected_Content_Map.md)
- [Hands-On ML and PyTorch Selected Content](HandsOnML_PyTorch_Selected_Content_Map.md)
- [Starter Notebooks and Datasets](Starter_Notebooks_and_Datasets.md)

## Assessment and Mock Security

- [Round 1 Mock B](Round_1_Mock_B.md)
- [Round 2 Mock Pack](Round_2_Mock_Pack.md)
- [Hidden Mock Sealing Protocol](Hidden_Mock_Sealing_Protocol.md)

## Readiness Records

- [Public Repository Readiness Dashboard](Public_Repository_Readiness_Dashboard.md)
- [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md)
- [Release Readiness Gates](Release_Readiness_Gates.md)
- [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](External_Access_Verification_Record.md)
- [Committed Runtime Validation Snapshot](Runtime_Validation_Record.md)
- [Committed Link Verification Snapshot](Link_Verification_Latest.md)
- [Repository Cleanup Audit](Repository_Cleanup_Audit.md)

## Annual Rules and Event Review

- [Annual Competition Rule Verification Template](Annual_Competition_Rule_Verification.md)
- [2026 Rules Verification Record](Annual_Rules_2026_Verification.md)
- [IOAI 2026 Post-Event Review](IOAI_2026_Post_Event_Review.md)

## Automation Boundary

Automated curriculum checks run in GitHub Actions. Curriculum audits publish results in the workflow summary and retain complete logs as temporary artifacts. Ready-to-Teach validation:

- validates structure, readiness contracts, launchers, repository hygiene, and the machine-readable curriculum specification;
- regenerates the twelve starter notebooks through the deterministic wrapper;
- fails when generated content differs from the committed notebooks;
- executes all twelve notebooks from fresh kernels;
- smoke-tests maintained starter code;
- checks required public links;
- stores volatile runtime and link reports as temporary Actions artifacts.

Validation workflows are read-only. They do **not** commit notebooks, timestamps, audit reports, runtime reports, or link reports to `main`. A mismatch must be fixed deliberately in a pull-request branch and reviewed.

## Evidence Boundary

Public repository checks do not replace:

- named-cohort student-device qualification;
- authenticated teacher/student account verification;
- legal reading and asset access;
- private assessment and hidden-test security;
- representative classroom pilots;
- full-cohort timing, retention, and transfer evidence;
- dated official-rule review and post-event task/environment comparison.

Use dimension-specific status language. Do not describe the curriculum as fully evidenced for a cohort, platform, or competition year until the corresponding records are complete.
