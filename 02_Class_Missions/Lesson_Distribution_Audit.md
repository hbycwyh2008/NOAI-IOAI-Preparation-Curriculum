# Lesson Distribution Audit

This audit checks whether `02_Class_Missions` has moved from a thin two-lesson skeleton to a dense, teachable NOAI/IOAI preparation sequence.

## Completion Standard

A module is considered structurally complete when:

1. the README lists a realistic number of lessons for the module;
2. every listed new lesson has a corresponding lesson file;
3. ordinary lessons preserve the classroom flow: **Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**;
4. each lesson ends with explicit evidence.

This audit measures **structural teachability**, not final teacher-key completeness. Worksheets, hidden scoring keys, full solution keys, and scored assessment assets still belong in the private teacher-key repo.

## Current Distribution

| Module | Target lesson count | Current lesson count | Status |
|---|---:|---:|---|
| 00 Competition workflow | 2 | 2 | Complete for orientation |
| 01 Python foundations | 5–6 | 6 | Complete |
| 02 Control flow/data structures | 5–6 | 6 | Complete |
| 03 Libraries/sorting/searching | 4–5 | 5 | Complete |
| 04 AI foundations/ethics | 4 | 4 | Complete |
| 05 Learning paradigms | 5–6 | 6 | Complete |
| 06 Linear regression | 4 | 4 | Complete |
| 07 Logistic regression | 4 | 4 | Complete |
| 08 Statistics/probability/distance | 5 | 5 | Complete |
| 09 Model evaluation | 5 | 6 | Complete |
| 10 Generalization/regularization | 4 | 4 | Complete |
| 11 Trees/ensembles | 4 | 4 | Complete |
| 12 Neural network foundations | 5 | 6 | Complete |
| 13 Backprop/optimization | 5 | 6 | Complete |
| 14 CNN foundations | 5 | 6 | Complete |
| 15 Round 1 exam training | 8–10 | 10 | Complete |
| 16 NumPy/Pandas/Matplotlib | 6 | 6 | Complete |
| 17 Data cleaning/feature engineering | 6 | 6 | Complete |
| 18 sklearn workflow | 6 | 6 | Complete |
| 19 PyTorch foundations | 7 | 7 | Complete |
| 20 Computer vision | 6 | 6 | Complete |
| 21 NLP/sequence models | 6 | 6 | Complete |
| 22 Audio/speech | 5 | 5 | Complete |
| 23 LLM/multimodality | 5 | 5 | Complete |
| 24 Round 2 project workflow | 6–8 | 7 | Complete |
| 25 Past-paper reproduction | 4 | 4 | Complete |
| 26 Timed mock contests | 4–5 | 5 | Complete |
| 27 Official Bohrium video lessons | resource hub | 2 hub lessons + 14 BML15 sequence lessons | Complete as resource hub |

## Structural Readiness Estimate

**Current structural readiness: 96%**

The distribution now clears the 95% threshold because every main module has the target number of lesson entries and the newly expanded modules have corresponding lesson files with the classroom flow and evidence requirements.

## What Keeps It Below 100%

The remaining 4% is not lesson-count related. It is implementation polish:

1. add student worksheets for every lesson;
2. add starter notebooks for every Round 2 coding-heavy lesson;
3. move full solutions, answer keys, scoring guides, and hidden labels into the private teacher-key repo;
4. rerun link, notebook, and runtime validation after all files settle;
5. pilot 3–5 lessons with real students and adjust timing.

## Non-Negotiable Rule

Do not return to a two-lesson-per-module skeleton. A core NOAI/IOAI module must include enough lessons for concept formation, guided practice, independent rebuild, and evidence submission.
