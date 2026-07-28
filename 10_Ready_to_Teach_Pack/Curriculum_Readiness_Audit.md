# Curriculum Readiness Audit

**Audit scope:** public file structure, teaching-content specificity, resource delivery, executable assets, runtime checks, assessment security, classroom validation, and annual competition alignment.

## Current Status

| Area | Current status | Evidence | Remaining condition |
|---|---|---|---|
| Public module structure | Complete by design | Modules 00–28 are indexed; Module 27 is an optional resource hub; Module 28 contains eight sprint lessons | strict validator must pass on the release commit |
| Mainline lesson bank | Complete as a curriculum bank | 155 mainline mission lessons across Modules 00–26 and 28 | teachers must choose a pathway rather than assign every lesson |
| Bohrium resource bank | Complete as an optional hub | two full-video hub missions and fourteen 70-minute lessons for 北京市十一学校《中学机器学习十五讲》 | verify authenticated access and current video structure before each cohort |
| Recommended scheduled pathway | Complete as a schedule | 67-session core pathway plus eight-session competition sprint | pilot the selected pathway with real students |
| Round 1 teaching content | High readiness | Python, artificial-intelligence foundations, machine-learning concepts, calculations, code tracing, short answers, mocks, and correction structures | live timing and difficulty calibration |
| Round 2 teaching content | High readiness | data engineering, scikit-learn, PyTorch, computer vision, natural-language processing, audio, large language models, projects, reproductions, and mocks | exact student-runtime and current-rule validation |
| Competition sprint | Structurally integrated | task recognition, data engineering, classical tuning, deep-learning tuning, PyTorch tuning, Optuna, efficiency, and full simulation | execute current starter assets and pilot Sessions 68–75 |
| Video delivery | Explicit | long Harvard/Coursera packages are marked pre-class or separate-resource-session work; in-class warm-ups remain eight minutes | verify course access and listed section structure before teaching |
| Starter notebooks | Automated workflow exists | twelve notebooks are generated and executed from fresh kernels | confirm the workflow result for the current release commit |
| Sprint starter code | Automated smoke tests exist | experiment log, manual tuning, Optuna tuning, metrics, data generation, and submission validation | confirm current workflow result and final student-environment compatibility |
| External links | Blocking automated check | required-link failures now fail the Ready-to-Teach workflow | authenticated edX/Coursera/Bohrium access still requires manual testing |
| Legacy overwrite risk | Removed | obsolete V1 builder workflow deleted; archived chunks marked inert | do not restore an executable decoder on `main` |
| Teacher keys and hidden assessments | Boundary defined | private-package manifest and public/private rules | confirm the teacher-key repository is private and complete before sensitive uploads |
| Real classroom evidence | Not complete | pilot protocols and timing rules exist | conduct representative and full-cohort pilots |
| Annual rules | Maintenance required | annual-rule records and maintenance instructions exist | recheck whenever organisers update rules, packages, models, APIs, or platform constraints |

## What “100%” Means

The repository may report **100% public file-structure and internal-consistency coverage** only when the strict validator passes and all expected public files, links, lesson-flow markers, durations, resource-delivery labels, counts, and source-of-truth boundaries are consistent.

It must not be described as operationally, pedagogically, or competitively 100% ready until all of the following are evidenced:

1. the selected pathway has been taught to a real cohort;
2. ordinary lessons fit the recorded 75-minute schedule;
3. the fourteen-video 北京市十一学校《中学机器学习十五讲》 sequence fits the recorded 70-minute schedule;
4. required notebooks and scripts run in the exact student environment;
5. current official rules and permitted tools have been incorporated;
6. the teacher-key repository is private and assessment-sensitive assets are protected;
7. formal simulations use secure hidden data and scoring packages;
8. authenticated external-course access is confirmed;
9. changed APIs, packages, model permissions, and runtime constraints are addressed.

## Current Curriculum Counts

| Category | Count | Scheduling meaning |
|---|---:|---|
| Mainline mission lessons | 155 | curriculum bank; not all automatically required |
| Optional Bohrium resource lessons | 16 | alternatives, concept reinforcement, and full-video sequence |
| Total public mission/resource lessons | 171 | total available lesson files |
| Core scheduled pathway | 67 | full foundation and competition-practice route |
| Competition sprint | 8 | late-stage task recognition, data engineering, and tuning |
| Recommended full scheduled pathway | 75 | 67 core sessions plus eight sprint sessions |

## Release Validation

For the release commit:

1. run `python scripts/validate_curriculum_structure.py`;
2. execute all twelve starter notebooks from fresh kernels;
3. smoke-test the competition-sprint starter code, including Optuna;
4. run `python scripts/check_required_links.py` without ignoring failures;
5. verify authenticated course access manually;
6. run the coding assets in the exact student environment;
7. verify current official competition rules;
8. confirm private-assessment security;
9. pilot representative lesson types and record actual timing.

## Release Decision

The repository is suitable for curriculum development, structural validation, and teacher dry runs when the strict automated checks pass.

Formal graded use remains conditional on runtime, privacy, annual-rule, authenticated-access, and classroom-pilot evidence. No single percentage may hide those distinctions.