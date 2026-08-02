# Ready-to-Teach Curriculum Pack

This directory converts the curriculum architecture into a directly teachable after-school competition course.

## Delivery Structure

- **67-session core pathway** — orientation, Python, artificial-intelligence and machine-learning foundations, Round 1, data/scikit-learn, PyTorch/domain tasks, projects, reproductions, mocks, and final readiness.
- **8-session competition sprint** — task formalisation, data quality, feature engineering, model selection, diagnosis-first tuning, model ensembling, and a full sprint simulation.
- **75-session recommended full competition pathway** — the 67-session core plus the eight-session sprint.
- **155-lesson mainline mission bank** — deeper practice, alternatives, reteaching, and extension.

See [Cohort Pathways and Required / Optional Map](../00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md).

## What Is Included

- lesson-specific teaching points rather than generic placeholders;
- an explicit teaching cycle for every ordinary lesson;
- entry checks, guided practice, independent work, evidence submission, and oral explanation;
- student worksheet questions embedded under lessons;
- exact resource module, week, video, chapter, or timestamp assignments;
- Round 1 paper-test drills and two mock forms;
- Round 2 baseline, validation, experiment, submission, and timed-mock workflows;
- an eight-session workflow sprint using data quality → feature engineering → model selection → tuning → model ensembling;
- stage gates for leakage, validation, feature evidence, model comparison, tuning, ensembling, and submission reliability;
- starter-notebook specifications and reproducible dataset generators;
- executable metrics, scikit-learn, PyTorch, data-generation, and submission-validation scripts;
- a syllabus crosswalk and readiness audit;
- selected-resource maps for Deep Learning Specialization, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, and the DeepLearning.AI PyTorch for Deep Learning Professional Certificate.

Assessment-sensitive teacher keys belong in a separate private package. They must not be uploaded until the teacher-key repository is confirmed private.

## Core Phase Files

1. `Phase_0_1_Setup_Python.md` — Sessions 1–8
2. `Phase_2A_ML_Foundations.md` — Sessions 9–18
3. `Phase_2B_Evaluation_Trees.md` — Sessions 19–26
4. `Phase_3_Neural_Networks.md` — Sessions 27–34
5. `Phase_4_Round_1.md` — Sessions 35–38 and Round 1 Mock A
6. `Phase_5_Data_Sklearn.md` — Sessions 39–44
7. `Phase_6A_PyTorch_Vision.md` — Sessions 45–50
8. `Phase_6B_NLP_Audio_LLM.md` — Sessions 51–57
9. `Phase_7_Competition_Practice.md` — Sessions 58–67
10. `Phase_8_Competition_Sprint.md` — Sessions 68–75

## Assessment and Resource Files

- `Round_1_Mock_B.md` — independent parallel Round 1 form
- `Round_2_Mock_Pack.md` — tabular and multimodal scored simulations
- `Resource_Map_and_Syllabus_Crosswalk.md`
- `DLS_Selected_Content_Map.md`
- `HandsOnML_PyTorch_Selected_Content_Map.md`
- `Starter_Notebooks_and_Datasets.md`
- `Curriculum_Readiness_Audit.md`

`Completion_Audit_90.md` is retained only as a compatibility pointer to the current readiness audit.

Executable scaffolds are in `06_Starter_Code/ready_to_teach/`.

## Competition-Sprint Evidence Files

- [Phase 8 — Competition Sprint](Phase_8_Competition_Sprint.md)
- [Module 28 — Competition Sprint Lessons](../02_Class_Missions/28-competition-sprint-task-data-tuning/README.md)
- [Competition Sprint Experiment Log](../03_Templates/Competition_Sprint_Experiment_Log_Template.md)
- [Competition Sprint Model Ensembling Record](../03_Templates/Competition_Sprint_Model_Ensembling_Record.md)
- [Competition Sprint Submission Checklist](../03_Templates/Competition_Sprint_Submission_Checklist.md)

PyTorch schedulers, Optuna, and broader automated search remain optional extension material after a manual tuning cycle. They do not replace Session 74 model ensembling.

## Selected Resource Maps

- [Deep Learning Specialization Selected Content Map](DLS_Selected_Content_Map.md) — explains that the five-course specialization is selected conceptual support, not a second full curriculum.
- [Hands-On Machine Learning and DeepLearning.AI PyTorch Selected Content Map](HandsOnML_PyTorch_Selected_Content_Map.md) — maps practical scikit-learn and PyTorch implementation resources.
- [Resource Map and NOAI Syllabus Crosswalk](Resource_Map_and_Syllabus_Crosswalk.md) — maps full resource names to NOAI A–D areas and Class Mission modules.
- [Competition Sprint Hyperparameter-Tuning Video Map](../02_Class_Missions/28-competition-sprint-task-data-tuning/Hyperparameter_Tuning_Video_Resource_Map.md) — gives exact required and optional Coursera sections, video titles, durations, and sprint use.

## 75-Minute After-School Club Classroom Flow

Every ordinary class follows this exact learning cycle.

**WE LEARN. PRACTICE. REBUILD. SHARE.**

| Step | Teaching block | Time | Required output |
|---:|---|---:|---|
| 1 | **Skill Warm-Up** | 0–8 | Use the exact assigned video, guide, document, or task segment. |
| 2 | **Talk Robin 1** | 8–15 | Explain what was learned and what remains confusing. |
| 3 | **Entry Check** | 15–22 | Demonstrate prerequisite understanding before deeper work. |
| 4 | **Core Pattern** | 22–35 | Extract the reusable method, decision rule, or reasoning pattern. |
| 5 | **Guided Practice** | 35–53 | Apply the pattern with teacher support. |
| 6 | **Independent Rebuild** | 53–67 | Recreate or transfer the pattern without copying the example. |
| 7 | **Talk Robin 2 + Evidence** | 67–75 | Explain, submit, and record evidence. |

The goal is not just to finish the task. The goal is to **rebuild and explain it independently**.

The fourteen-session sequence for 北京市十一学校《中学机器学习十五讲》 is a named 70-minute exception. Long contest sessions use their stated competition-realistic timelines.

## Minimum Evidence Per Lesson

- completed worksheet section;
- one independently produced artifact;
- one documented error, misconception, or revision;
- one oral explanation selected by the teacher;
- an artificial-intelligence-use record when assistance was used;
- a meaningful Git commit;
- fresh-runtime evidence when the lesson produces competition code.

## Implementation Rule

The teacher may shorten a resource segment or provide language support, but may not remove **Independent Rebuild** or **Talk Robin 2 + Evidence**. Students receive support to reach the same standard, not a different standard.

Before formal graded use, read [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md) and confirm runtime, privacy, annual-rule, link, and pilot conditions.