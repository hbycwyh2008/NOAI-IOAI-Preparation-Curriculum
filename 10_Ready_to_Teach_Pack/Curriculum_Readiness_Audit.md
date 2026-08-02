# Curriculum Readiness Audit

**Audit scope:** public structure, teaching specificity, resource delivery, executable assets, runtime checks, assessment security, classroom evidence, and annual competition alignment.

## Current Status

| Area | Current status | Evidence | Remaining condition |
|---|---|---|---|
| Canonical pathway | Complete by design | nine dependency-based phases and 75 scheduled sessions | pilot the actual sequence with students |
| Class Missions navigation | Rebuilt | scheduled phase folders are separated from `_Lesson_Library` and `_Curriculum_Governance` | maintain the separation when adding content |
| Mainline lesson bank | Structurally complete | 155 mainline lesson files | select by phase need rather than assign all files |
| Bohrium foundation bank | Structurally complete | 16 resource lessons, including the fourteen-session 70-minute sequence | verify authenticated access and current video structure |
| Python and data tools | High readiness | CS50P spine followed by NumPy, Pandas, and visualisation | calibrate pacing and diagnostics |
| Classical machine learning | High readiness | Andrew Ng ML spine, mathematics intuition, model recognition, and typical tasks | verify exact selected external sections before each cohort |
| Deep learning | High readiness | Andrew Ng DL paired with PyTorch and domain tasks | validate compute and student runtime |
| Synthesis and competition | Structurally integrated | comparison, EDA, features, evaluation, tuning, ensembling, simulation, and postmortem | complete realistic pilot and secure assessment runs |
| Starter notebooks and code | Automated checks exist | twelve fresh-kernel notebooks and maintained smoke tests | confirm checks on the release commit |
| External links | Blocking automated check | required-link failures fail the workflow | manually verify authenticated resources |
| Teacher keys and hidden assessment | Boundary defined | private-repository manifest and public/private rules | confirm private repository security |
| Annual rules | Maintenance required | annual-rule records exist | recheck whenever organisers change rules or tooling |
| Real classroom evidence | Not complete | pilot protocols exist | conduct representative and full-cohort pilots |

## What “100%” Means

The repository may report **100% public file-structure coverage** and internal consistency only when the strict validator confirms expected files, lesson counts, links, classroom-flow markers, durations, resource-delivery labels, and source-of-truth boundaries.

It must not be described as fully **Operational** or competitively ready until the selected pathway has real-classroom evidence, the student runtime is verified, current official rules are incorporated, authenticated resource access works, and private assessment materials are secured.

## Current Curriculum Counts

| Category | Count | Meaning |
|---|---:|---|
| Canonical scheduled pathway | 75 | actual recommended order |
| Mainline lesson files | 155 | selectable lesson bank |
| Bohrium resource lessons | 16 | resource and foundation bank |
| Total public lesson/resource files | 171 | total available material, not required schedule |

## Release Validation

For the release commit:

1. run `python scripts/validate_curriculum_structure.py`;
2. execute all twelve starter notebooks from fresh kernels;
3. smoke-test maintained starter code;
4. run `python scripts/check_required_links.py` without ignoring failures;
5. verify authenticated course access manually;
6. run code in the exact student environment;
7. verify current official competition rules;
8. confirm private-assessment security;
9. pilot representative lesson types and record actual timing.

## Release Decision

The repository is suitable for curriculum development, structural validation, and teacher dry runs when the automated checks pass. Formal graded use remains conditional on runtime, privacy, annual-rule, authenticated-access, and classroom-pilot evidence.
