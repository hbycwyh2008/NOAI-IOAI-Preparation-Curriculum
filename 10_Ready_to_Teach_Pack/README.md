# Ready-to-Teach Curriculum Pack

This directory supplies teacher-facing delivery, assessment, runtime, and resource records for the canonical 75-session pathway.

## Canonical Delivery Structure

| Phase | Sessions | Main spine |
|---:|---:|---|
| 0 | 1–2 | orientation and evidence |
| 1 | 3–12 | CS50P Python |
| 2 | 13–18 | NumPy, Pandas, and Matplotlib |
| 3 | 19–32 | 北京市十一学校《中学机器学习十五讲》 on Bohrium |
| 4 | 33–37 | Kaggle Learn workflow refresh |
| 5 | 38–55 | Andrew Ng Machine Learning Specialization + StatQuest + 3Blue1Brown + model labs |
| 6 | 56–67 | Andrew Ng Deep Learning Specialization + PyTorch + domain tasks |
| 7 | 68–71 | model comparison, EDA, feature engineering, evaluation, and error analysis |
| 8 | 72–75 | tuning, ensembling, full simulation, and postmortem |

The authoritative order is the [Detailed 75-Session Sequence](../00_Course_Overview/Detailed_Lesson_Sequence.md). The [Class Missions phase navigation](../02_Class_Missions/README.md) defines prerequisites, resource roles, and gates.

## Curriculum Bank

The repository preserves:

- 155 mainline lesson files;
- 16 Bohrium resource lessons;
- 171 public lesson/resource files in total.

The complete bank now lives under [`02_Class_Missions/_Lesson_Library`](../02_Class_Missions/_Lesson_Library/README.md). It supports remediation, deeper practice, alternative explanations, domain extensions, and competition preparation; it is not a second scheduled route.

## What Is Included

- exact phase and session navigation;
- entry checks, guided practice, independent rebuilds, and evidence requirements;
- Round 1 paper-test work and mock forms;
- Round 2 tabular, image, text, audio, scientific, and multimodal work;
- model-recognition routines and model-comparison evidence;
- competition experiment, ensembling, and submission templates;
- generated starter notebooks and executable starter code;
- syllabus and resource crosswalks;
- runtime, link, annual-rule, pilot, privacy, and licensing records.

Assessment-sensitive teacher keys, hidden labels, private tests, secure scoring packages, and calibration examples remain in the private teacher-key repository.

## Resource Maps

- [CS50P exact timestamp map](../05_Resources/CS50P_edX_Timestamp_Map.md)
- [Kaggle Learn refresh map](../05_Resources/Kaggle_Learn_Refresh_Map.md)
- [Andrew Ng ML mathematics intuition map](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Math_Intuition_Map.md)
- [Deep Learning Specialization selected-content map](DLS_Selected_Content_Map.md)
- [Hands-On ML and PyTorch selected-content map](HandsOnML_PyTorch_Selected_Content_Map.md)
- [Resource map and NOAI syllabus crosswalk](Resource_Map_and_Syllabus_Crosswalk.md)

## Competition Integration

Use:

- [Phase 8 teacher pack](Phase_8_Competition_Sprint.md)
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

Automated tuning is optional and follows a justified manual tuning cycle. Stacking requires out-of-fold base predictions.

## Classroom Flow

Every ordinary 75-minute class follows:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

The fourteen-session Bohrium sequence is a named 70-minute exception. Long competitions and reproductions use their stated realistic durations.

## Minimum Evidence Per Lesson

- completed notes or worksheet section;
- one independently produced artifact;
- one documented error, misconception, or revision;
- one oral or written explanation;
- an artificial-intelligence-use record when assistance was used;
- a meaningful Git commit;
- fresh-runtime evidence when the mission produces competition code.

Before formal graded use, read the [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md). Structural consistency, runtime validation, assessment security, annual-rule alignment, authenticated resource access, and classroom evidence are separate readiness decisions.
