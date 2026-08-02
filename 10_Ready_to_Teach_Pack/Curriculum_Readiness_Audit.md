# Curriculum Readiness Audit

**Audit scope:** public structure, teaching specificity, resource delivery, executable assets, runtime checks, assessment security, classroom evidence, and annual competition alignment.

## Current Status

| Area | Current status | Evidence | Remaining condition |
|---|---|---|---|
| Canonical pathway | Complete by design | nine dependency-based phases and 78 scheduled sessions | pilot the actual sequence with students |
| Class Missions navigation | Rebuilt | scheduled phase folders are separated from `_Lesson_Library` and `_Curriculum_Governance` | maintain the separation when adding content |
| Mainline lesson bank | Structurally complete | 155 mainline lesson files | select by phase need rather than assign all files |
| Bohrium foundation bank | Structurally complete | 16 resource lessons, including the fourteen-session 70-minute sequence | verify authenticated access and current video structure |
| AI History and Thinking Humans | Public package complete | eight English seminars, teacher pack, evidence template, phase rubric, and phase gate | verify book access, reading load, language support, and seminar timing with students |
| Python and data tools | High readiness | CS50P spine followed by NumPy, Pandas, and visualisation | calibrate pacing and diagnostics |
| Classical machine learning | High readiness | Andrew Ng ML spine, mathematics intuition, embedded Kaggle practice, model recognition, and typical tasks | verify exact selected external sections before each cohort |
| Deep learning | High readiness | Andrew Ng DL paired with PyTorch and domain tasks | validate compute and student runtime |
| Synthesis and competition | Structurally integrated | comparison, EDA, features, evaluation, tuning, ensembling, simulation, and postmortem | complete realistic pilot and secure assessment runs |
| Starter notebooks and code | Automated checks exist | twelve fresh-kernel notebooks and maintained smoke tests | confirm checks on the release commit and qualify the exact student environment |
| External links | Blocking automated check | required-link failures fail the workflow | manually verify authenticated resources and legal access to the Phase 04 book |
| Teacher keys and hidden assessment | Boundary defined | private-repository manifest and public/private rules | confirm private repository security and protected asset completeness |
| Annual rules | Maintenance required | annual-rule records exist | recheck whenever organisers change rules or tooling |
| Real classroom evidence | Not complete | pilot protocol and representative pilot matrix exist | conduct representative and full-cohort pilots |

## What “100%” Means

The repository may report **100% public file-structure and internal-consistency coverage** only when both strict validators confirm:

- the 78-session pathway and nine phases;
- required phase and lesson files;
- 155 mainline lessons and 16 Bohrium resource lessons;
- internal links, classroom-flow markers, durations, and resource-delivery labels;
- the eight-session AI History phase and its teacher, student-evidence, and assessment artifacts;
- current source-of-truth boundaries;
- absence of stale 75-session and standalone-Kaggle Phase 04 claims.

It must not be described as fully **Operational** or competitively ready until the selected pathway has real-classroom evidence, the student runtime is qualified, current official rules are incorporated, authenticated resource access works, and private assessment materials are secured.

## Current Curriculum Counts

| Category | Count | Meaning |
|---|---:|---|
| Canonical scheduled pathway | 78 | actual recommended order |
| Scheduled AI History seminars | 8 | Sessions 33–40 within the canonical pathway |
| Mainline lesson files | 155 | selectable lesson bank |
| Bohrium resource lessons | 16 | resource and foundation bank |
| Total public lesson/resource bank files | 171 | available reusable material, not the required schedule |

## Public Repository Evidence

The public repository now includes:

- the [Public Repository Readiness Dashboard](Public_Repository_Readiness_Dashboard.md);
- the [Phase 4 Teacher Pack](Phase_4_AI_History_and_Thinking_Humans.md);
- the [AI History Reading Evidence Template](../03_Templates/AI_History_Reading_Evidence_Template.md);
- the [AI History Phase Rubric](../04_Assessment/AI_History_Phase_Rubric.md);
- the [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md);
- the [External Access Verification Record](External_Access_Verification_Record.md);
- the [Representative Pilot Matrix](../09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md);
- the [Release Readiness Gates](Release_Readiness_Gates.md).

## Release Validation

For the release commit:

1. run `python scripts/validate_curriculum_structure.py`;
2. run `python scripts/validate_readiness_contract.py`;
3. execute all twelve starter notebooks from fresh kernels;
4. smoke-test maintained starter code;
5. run `python scripts/check_required_links.py` without ignoring failures;
6. complete authenticated-access verification with intended accounts;
7. qualify code in the exact student environment;
8. verify current official competition rules;
9. confirm private-assessment security;
10. pilot representative lesson types and record actual timing.

## Release Decision

The repository is suitable for curriculum development, structural validation, teacher dry runs, and a controlled pilot when the automated checks pass.

Formal graded use remains conditional on runtime, privacy, annual-rule, authenticated-access, and classroom-pilot evidence. Missing external evidence is reported as **pending**, not converted into a guessed percentage.
