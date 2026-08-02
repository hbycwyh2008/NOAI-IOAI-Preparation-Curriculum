# Class Mission Lesson Distribution and File-Structure Audit

## Navigation Status

The counted reusable lesson files live under `02_Class_Missions/_Lesson_Library`. The scheduled route is defined by the numbered phase folders; file coverage is not a teaching sequence.

The eight Phase 04 AI History seminars are scheduled lessons outside the preserved 171-file reusable bank and are validated by `scripts/validate_readiness_contract.py`.

## Coverage Standard

A reusable lesson-bank module contributes to public file-structure coverage when:

1. its README lists a realistic lesson sequence;
2. every listed lesson has a corresponding file;
3. every lesson file is linked from a README;
4. ordinary lessons preserve the classroom flow: **Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**;
5. every lesson identifies required evidence;
6. public worksheet, notebook, experiment, and submission templates exist;
7. the private teacher-key boundary is explicit;
8. automated validation and pilot checklists exist.

This audit measures public file-structure coverage of the reusable bank. It does not certify runtime, real-class timing, annual competition rules, authenticated access, private-assessment security, or student outcomes.

## Current Reusable-Bank Distribution

| Module | Target lesson count | Current lesson count | File-structure status |
|---|---:|---:|---|
| 00 Competition workflow | 2 | 2 | Covered |
| 01 Python foundations | 5–6 | 6 | Covered |
| 02 Control flow/data structures | 5–6 | 6 | Covered |
| 03 Libraries/sorting/searching | 4–5 | 5 | Covered |
| 04 Artificial-intelligence foundations/ethics | 4 | 4 | Covered |
| 05 Learning paradigms | 5–6 | 6 | Covered |
| 06 Linear regression | 4 | 4 | Covered |
| 07 Logistic regression | 4 | 4 | Covered |
| 08 Statistics/probability/distance | 5 | 5 | Covered |
| 09 Model evaluation | 5–6 | 6 | Covered |
| 10 Generalisation/regularisation | 4 | 4 | Covered |
| 11 Trees/ensembles | 4 | 4 | Covered |
| 12 Neural-network foundations | 5–6 | 6 | Covered |
| 13 Backpropagation/optimisation | 5–6 | 6 | Covered |
| 14 Convolutional-neural-network foundations | 5–6 | 6 | Covered |
| 15 Round 1 exam training | 8–10 | 10 | Covered |
| 16 NumPy/Pandas/Matplotlib | 6 | 6 | Covered |
| 17 Data cleaning/feature engineering | 6 | 6 | Covered |
| 18 Scikit-learn workflow | 6 | 6 | Covered |
| 19 PyTorch foundations | 7 | 7 | Covered |
| 20 Computer vision | 6 | 6 | Covered |
| 21 Natural-language processing/sequence models | 6 | 6 | Covered |
| 22 Audio/speech | 5 | 5 | Covered |
| 23 Large language models/multimodality | 5 | 5 | Covered |
| 24 Round 2 project workflow | 6–8 | 7 | Covered |
| 25 Past-paper reproduction | 4 | 4 | Covered |
| 26 Timed mock contests | 4–5 | 5 | Covered |
| 27 Official Bohrium video resource hub | resource hub | 2 hub lessons + 14 sequence lessons | Covered as resource hub |
| 28 Competition sprint: task recognition, data engineering, and hyperparameter tuning | 8 | 8 | Covered |

## Current Public Coverage

**Current target result: 100% public file-structure and internal-consistency coverage, subject to both automated validators passing on the current commit.**

The expected reusable public bank is:

- 155 mainline mission lessons across Modules 00–26 and Module 28;
- 16 Bohrium resource lessons in Module 27;
- 171 total reusable public lesson/resource files.

The canonical scheduled pathway is separate:

- 78 scheduled sessions across nine phases;
- eight AI History seminars in Sessions 33–40;
- Kaggle practice embedded inside Andrew Ng ML rather than scheduled as a standalone phase.

## Required Supporting Coverage

The public structure also includes:

1. the fourteen concrete 70-minute lessons for 北京市十一学校《中学机器学习十五讲》;
2. the eight concrete 70-minute AI History and Thinking Humans seminars;
3. the Phase 04 teacher pack, reading-evidence template, phase rubric, and pilot requirement;
4. exact Harvard CS50’s Introduction to Programming with Python timestamp mapping;
5. embedded Kaggle practice mapping and selected Andrew Ng/StatQuest/3Blue1Brown resources;
6. public worksheet, Round 1, reading-evidence, notebook-lab, experiment-log, and submission-check templates;
7. starter notebooks and executable starter code;
8. a current resource/syllabus crosswalk;
9. explicit teacher-key boundaries;
10. link, runtime, authenticated-access, annual-rule, release, and pilot procedures;
11. non-destructive curriculum and readiness-contract validators;
12. nine canonical teacher phase overviews matching Sessions 1–78.

## Not Public by Design

The following remain private:

- full solution keys;
- answer keys;
- hidden labels;
- private test sets;
- secure scoring packages;
- protected pre-use scoring logic and calibration examples;
- teacher calibration responses;
- secrets and restricted competition data.

## Non-Negotiable Rules

- Do not return to a two-lesson-per-module skeleton.
- Do not schedule all 171 reusable files automatically.
- Do not reintroduce a standalone Kaggle Phase 04.
- Do not label public coverage as blanket operational readiness.
- Do not use automated tuning before task recognition, validation, data engineering, and a valid baseline are correct.
- Do not upload assessment-sensitive assets until the teacher-key repository is confirmed private.
