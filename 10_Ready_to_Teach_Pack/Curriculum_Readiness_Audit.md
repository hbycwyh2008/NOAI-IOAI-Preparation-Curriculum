# Curriculum Readiness Audit

**Audit scope:** public curriculum structure, teaching content, resources, executable assets, assessment security, classroom validation, and annual competition alignment.

## Current Status

| Area | Current status | Evidence | Remaining condition |
|---|---|---|---|
| Public module structure | Complete | Modules 00–28 are indexed; Module 27 is an optional resource hub; Module 28 contains eight sprint lessons | repeat the structural audit after any new module or rename |
| Mainline lesson bank | Complete as a curriculum bank | 155 mainline mission lessons across Modules 00–26 and 28 | teachers must select a pathway rather than assign every lesson |
| Bohrium resource bank | Complete as an optional hub | two full-video hub missions and fourteen 70-minute lessons for 北京市十一学校《中学机器学习十五讲》 | verify access and video structure before each cohort |
| Recommended scheduled pathway | Complete | 67-session core pathway plus eight-session competition sprint | pilot the full 75-session pathway in a real cohort |
| Round 1 teaching content | High readiness | Python, artificial-intelligence foundations, machine-learning concepts, calculations, code tracing, short answers, and mocks | run live timing and difficulty calibration |
| Round 2 teaching content | High readiness | data engineering, scikit-learn, PyTorch, computer vision, natural-language processing, audio, large language models, projects, reproductions, and mocks | validate against the final student runtime and current official rules |
| Competition sprint | Structurally complete; pilot pending | task recognition, data engineering, classical tuning, deep-learning tuning, PyTorch tuning, Optuna, and full simulation | verify current Coursera segments; run the tuning notebooks/labs in the final environment; pilot timing |
| Starter notebooks | Existing validation record | twelve student-facing notebooks and `Runtime_Validation_Record.md` | rerun after dependency, runtime, dataset, or notebook changes |
| Automated checks | Present | GitHub Actions workflow and link-validation scripts | confirm the latest workflow run passes after curriculum changes |
| Teacher keys and hidden assessments | Boundary defined | private-package manifest and public/private rules | the teacher-key repository must be private before sensitive files are uploaded |
| Real classroom evidence | Not complete | pilot protocols exist | conduct small-group and full-cohort pilots and record actual timings |
| Annual rules | Maintenance required | annual-rules record and maintenance checklist exist | recheck whenever organisers publish new rules or platform constraints |

## What “100%” Means Here

The public repository may be described as **100% structurally complete** when every public module has the intended lesson files, templates, resource maps, evidence requirements, and public/private boundaries.

It must **not** be described as professionally or operationally 100% ready until all of the following are true:

1. the complete selected pathway has been taught to a real cohort;
2. ordinary lesson blocks fit the recorded 75-minute schedule;
3. the fourteen-video 北京市十一学校《中学机器学习十五讲》 sequence fits its recorded 70-minute schedule;
4. every required notebook and script runs in the exact student environment;
5. current official NOAI/IOAI rules and permitted tools have been incorporated;
6. the teacher-key repository is private and assessment-sensitive assets are protected;
7. formal simulations use newly generated hidden data and secure scoring packages;
8. broken links, moved course modules, and changed APIs have been corrected.

## Current Curriculum Counts

| Category | Count | Scheduling meaning |
|---|---:|---|
| Mainline mission lessons | 155 | curriculum bank; not all are automatically required |
| Optional Bohrium resource lessons | 16 | alternatives, concept reinforcement, or full-video sequences |
| Total public mission/resource lessons | 171 | total available lesson files |
| Core scheduled pathway | 67 | compressed full NOAI foundation and competition path |
| Competition sprint | 8 | late-stage task recognition, data engineering, and tuning |
| Recommended full scheduled pathway | 75 | 67 core sessions plus eight sprint sessions |

## Validation Required After This Update

Because Module 28 and the 75-session pathway were added after earlier validation records, the next release should run:

1. internal-link validation for all Module 28 lesson links;
2. external-link validation for the three Coursera tuning courses;
3. fresh-runtime execution for any new Optuna, scheduler, tuning, or efficiency notebook/lab;
4. a dry run of Sessions 68–75;
5. a full check that the main README, pacing guide, detailed sequence, Ready-to-Teach Pack, resource crosswalk, and lesson-distribution audit report the same pathway and counts.

## Release Decision

The repository is suitable for continued curriculum development and teacher dry runs. Formal graded use still requires the privacy, runtime, annual-rule, and pilot conditions above.

Do not use a single percentage to hide the distinction between:

- structural completeness;
- teaching-content quality;
- runtime validation;
- assessment security;
- classroom evidence;
- annual competition compliance.