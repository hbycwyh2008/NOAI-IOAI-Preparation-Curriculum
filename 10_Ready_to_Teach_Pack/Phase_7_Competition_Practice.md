# Phase 7 — Competition Practice

Sessions 58–67 integrate Round 2 workflow, official-style reproductions, timed mocks, and final readiness decisions.

This file is a **teacher-facing phase index**. It does not duplicate complete lesson bodies.

## Canonical Source Rule

- `02_Class_Missions/` is the source of truth for lesson content, evidence, and lesson-specific duration.
- `00_Course_Overview/Detailed_Lesson_Sequence.md` is the source of truth for the scheduled Sessions 1–75.
- This phase file explains sequencing, prerequisites, and teacher decisions only.

When a summary conflicts with a Class Mission, use the Class Mission and correct the summary.

## Session Map

| Session | Duration | Canonical Class Mission | Required outcome |
|---:|---:|---|---|
| 58 | 75 minutes | [`24-round-2-project-training/lesson-01.md`](../02_Class_Missions/_Lesson_Library/24-round-2-project-training/lesson-01.md) | defensible data audit, validation split, leakage analysis, and validation memo |
| 59 | 75 minutes | [`24-round-2-project-training/lesson-02.md`](../02_Class_Missions/_Lesson_Library/24-round-2-project-training/lesson-02.md) | first valid baseline, local metric, valid submission, and fresh-runtime evidence |
| 60 | 75 minutes | [`24-round-2-project-training/lesson-03.md`](../02_Class_Missions/_Lesson_Library/24-round-2-project-training/lesson-03.md) | one controlled experiment, keep/reject decision, and leaderboard-risk explanation |
| 61 | 180 minutes | [`25-past-paper-reproduction/lesson-01.md`](../02_Class_Missions/_Lesson_Library/25-past-paper-reproduction/lesson-01.md) | natural-language-processing reproduction with baseline, sequence route, validation, and postmortem |
| 62 | 180 minutes | [`25-past-paper-reproduction/lesson-02.md`](../02_Class_Missions/_Lesson_Library/25-past-paper-reproduction/lesson-02.md) | tabular or AI4Science reproduction with group-aware validation and multiple baselines |
| 63 | 180 minutes | [`25-past-paper-reproduction/lesson-03.md`](../02_Class_Missions/_Lesson_Library/25-past-paper-reproduction/lesson-03.md) | audio or image reproduction with source-aware split and shortcut analysis |
| 64 | 120 minutes | [`26-mock-contests/lesson-01.md`](../02_Class_Missions/_Lesson_Library/26-mock-contests/lesson-01.md) | closed-note Round 1 mock, confidence coding, and later correction evidence |
| 65 | 240 minutes | [`26-mock-contests/lesson-02.md`](../02_Class_Missions/_Lesson_Library/26-mock-contests/lesson-02.md) | timed Round 2 tabular mock with valid submission and fresh run |
| 66 | 360 minutes | [`26-mock-contests/lesson-03.md`](../02_Class_Missions/_Lesson_Library/26-mock-contests/lesson-03.md) | timed Round 2 multimodal mock with single-modality baselines, fusion, and stress tests |
| 67 | 45 minutes per student | [`26-mock-contests/lesson-04.md`](../02_Class_Missions/_Lesson_Library/26-mock-contests/lesson-04.md) | evidence-based readiness status and three dated next actions |

## Entry Gate

Students enter Phase 7 only when they can already:

1. identify task type, target, official metric, and submission schema;
2. create a leakage-safe train/validation split;
3. build a simple valid baseline before advanced modelling;
4. generate a valid submission from a fresh runtime;
5. record one controlled experiment and explain the decision;
6. use documentation and artificial-intelligence assistance without submitting work they cannot explain.

## Teacher Decisions

Before each reproduction or mock, confirm:

- current official rules and permitted tools;
- dataset and task licensing;
- whether internet, APIs, pretrained models, and external data are allowed;
- runtime, memory, storage, and submission limits;
- which answer keys, hidden labels, and calibration materials remain private.

## Exit Gate

A student is ready to continue to the eight-session competition sprint only when evidence shows:

- no critical validation or leakage failure;
- no repeated invalid-submission failure;
- a reproducible baseline in at least two task modalities;
- disciplined experiment logging;
- sufficient Round 1 reliability;
- a clear time-management and backup-submission routine.

Use [`Phase_8_Competition_Sprint.md`](Phase_8_Competition_Sprint.md) only after this gate is met.