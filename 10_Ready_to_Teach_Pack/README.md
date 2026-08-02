# Ready-to-Teach Curriculum Pack

This directory supplies teacher-facing delivery, assessment, runtime, access, pilot, and release records for the **canonical 78-session pathway**.

## How to Start a Class

```text
Class Missions
→ assigned Phase
→ SESSION_LAUNCHER.md
→ exact linked lesson
→ required evidence
```

Use [Class Missions — Start Here](../02_Class_Missions/README.md) and [How to Use Class Missions](../02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md). Do not browse `_Lesson_Library` to choose a scheduled class.

## Canonical Delivery Structure

| Phase | Sessions | Main spine |
|---:|---:|---|
| 0 | 1–2 | orientation and evidence |
| 1 | 3–12 | CS50P Python |
| 2 | 13–18 | NumPy, Pandas, and Matplotlib |
| 3 | 19–32 | 北京市十一学校《中学机器学习十五讲》 on Bohrium |
| 4 | 33–40 | AI History and Thinking Humans through Melanie Mitchell |
| 5 | 41–58 | Andrew Ng ML mathematics transition + models + StatQuest + 3Blue1Brown + embedded Kaggle practice |
| 6 | 59–70 | Andrew Ng Deep Learning + PyTorch + domain tasks |
| 7 | 71–74 | model comparison, EDA, feature engineering, evaluation, and error analysis |
| 8 | 75–78 | tuning, ensembling, full simulation, and postmortem |

The [Detailed 78-Session Sequence](../00_Course_Overview/Detailed_Lesson_Sequence.md) is the whole-course overview. The Phase launchers are the exact teaching entry points.

## Curriculum Bank

The repository preserves:

- 155 mainline lesson files;
- 16 Bohrium resource lessons;
- 171 public lesson/resource files in the reusable bank;
- nine Phase launchers covering Sessions 1–78 exactly once;
- eight scheduled AI History reading seminars;
- an explicit Andrew ML mathematics transition in Sessions 41–43.

The reusable bank lives under [`02_Class_Missions/_Lesson_Library`](../02_Class_Missions/_Lesson_Library/README.md). It supports remediation, deeper practice, alternative explanations, domain extensions, and competition preparation; it is not a second scheduled route.

## Canonical Phase Delivery Packs

- [Phase 4 — AI History and Thinking Humans](Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew ML Mathematics Transition](Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md)
- [Phase 8 — Tuning, Ensembling, and Competition](Phase_8_Competition_Sprint.md)

The canonical Phase 7 teacher overview is [Model Comparison, EDA, and Evaluation](../09_Teacher_Planning/Phase_Overviews/Canonical_Phase_7_Model_Comparison_EDA_Evaluation.md).

## Phase 4 Evidence and Assessment

- [AI History Reading Evidence Template](../03_Templates/AI_History_Reading_Evidence_Template.md)
- [AI History Phase Rubric](../04_Assessment/AI_History_Phase_Rubric.md)

## Phase 5 Mathematics Evidence and Assessment

- [Andrew ML Mathematics Transition Bridge](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md)
- [Mathematics Intuition Map](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Math_Intuition_Map.md)
- [Mathematics Bridge Evidence Template](../03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md)
- [Mathematics Bridge Rubric](../04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md)

## Reusable Competition Practice

- [Extended Competition Practice Teacher Index](Phase_7_Competition_Practice.md)
- [Competition Workflow Lesson Bank](../02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/README.md)

These resources provide longer reproductions, mocks, and an eight-lesson sprint bank. They do not define additional canonical sessions after Session 78.

## Readiness and Release Records

- [Public Repository Readiness Dashboard](Public_Repository_Readiness_Dashboard.md)
- [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md)
- [Release Readiness Gates](Release_Readiness_Gates.md)
- [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](External_Access_Verification_Record.md)
- [Runtime Validation Record](Runtime_Validation_Record.md)
- [Latest Link Verification](Link_Verification_Latest.md)
- [Annual Competition Rule Verification](Annual_Competition_Rule_Verification.md)
- [Representative Pilot Matrix](../09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md)

## What Is Included

- exact Phase and Session launchers;
- entry checks, guided practice, independent rebuilds, and evidence requirements;
- eight AI-history reading seminars with a teacher pack and rubric;
- Andrew ML mathematics transition, just-in-time mathematics map, teacher pack, template, and rubric;
- model-recognition routines and model-comparison evidence;
- Round 1 paper-test work and mock forms;
- Round 2 tabular, image, text, audio, scientific, and multimodal work;
- competition experiment, ensembling, and submission templates;
- generated starter notebooks and executable starter code;
- runtime, link, annual-rule, pilot, privacy, licensing, and authenticated-access records.

Assessment-sensitive teacher keys, hidden labels, private tests, secure scoring packages, and calibration examples remain in the private teacher-key repository.

## Resource Maps

- [CS50P exact timestamp map](../05_Resources/CS50P_edX_Timestamp_Map.md)
- [Kaggle Learn embedded-practice map](../05_Resources/Kaggle_Learn_Refresh_Map.md)
- [Deep Learning Specialization selected-content map](DLS_Selected_Content_Map.md)
- [Hands-On ML and PyTorch selected-content map](HandsOnML_PyTorch_Selected_Content_Map.md)
- [Resource map and NOAI syllabus crosswalk](Resource_Map_and_Syllabus_Crosswalk.md)

## Competition Integration

Use:

- [Canonical Phase 8 teacher pack](Phase_8_Competition_Sprint.md)
- [Extended competition practice index](Phase_7_Competition_Practice.md)
- [Competition workflow lesson bank](../02_Class_Missions/_Lesson_Library/28-competition-sprint-task-data-tuning/README.md)
- [Experiment log](../03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [Model ensembling record](../03_Templates/Competition_Sprint_Model_Ensembling_Record.md)
- [Submission checklist](../03_Templates/Competition_Sprint_Submission_Checklist.md)

The required order is:

```text
diagnose the limitation
→ tune a selected model
→ compare stable single models
→ ensemble only valid complementary models
→ execute from a fresh environment
→ validate the submission
→ write the postmortem
```

## Classroom Flow

Every ordinary 75-minute class follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

The fourteen-session Bohrium sequence and eight-session AI History sequence are named 70-minute exceptions. Long competitions and reproductions use their stated realistic durations.

## Minimum Evidence Per Lesson

- completed notes, reading evidence, or worksheet section;
- one independently produced artifact;
- one documented error, misconception, or revision;
- one oral or written explanation;
- an artificial-intelligence-use record when assistance was used;
- a meaningful Git commit when code or repository work is produced;
- fresh-runtime evidence when the mission produces competition code.

Before formal graded use, read the [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md). Structural consistency, runtime qualification, assessment security, annual-rule alignment, authenticated resource access, and classroom evidence are separate readiness decisions.