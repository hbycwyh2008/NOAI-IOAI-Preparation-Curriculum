# Teacher-Key Private Repository Manifest

This public student-facing repo must not contain full solutions, hidden labels, scoring keys, or official answer keys.

Use a separate private repository for teacher-only assets.

Recommended private repo:

```text
NOAI-IOAI-Preparation-Teacher-Keys
```

## Required Private Assets

| Asset type | Must be private? | Reason |
|---|---|---|
| Full worksheet solutions | Yes | Prevents students from copying evidence. |
| Round 1 answer keys | Yes | Preserves assessment validity. |
| MCQ distractor explanations | Yes, if used for grading | Prevents memorisation of test forms. |
| Scoring rubrics with exact point allocation | Yes | Needed for teacher calibration, not student preview. |
| Hidden validation labels | Yes | Required for fair leaderboard-style evaluation. |
| Private test labels | Yes | Required for A/B leaderboard simulation. |
| Model solutions and notebooks | Yes | Prevents solution leakage. |
| Postmortem exemplars | Usually | Can be released later after assessment. |

## Suggested Private Repo Structure

```text
teacher_keys/
├── round1/
│   ├── mcq_answer_keys/
│   ├── code_trace_solutions/
│   ├── calculation_solutions/
│   └── short_answer_rubrics/
├── round2/
│   ├── hidden_labels/
│   ├── private_test_sets/
│   ├── baseline_solution_notebooks/
│   ├── scoring_scripts/
│   └── leaderboard_records/
├── bml15_sequence/
│   ├── teacher_notes/
│   ├── expected_entry_check_answers/
│   └── misconception_bank/
└── calibration/
    ├── sample_student_work/
    ├── scoring_examples/
    └── pilot_revision_notes/
```

## Public Repo Boundary

Allowed in this public repo:

- lesson plans;
- starter worksheets;
- starter notebooks;
- evidence checklists;
- student-facing rubrics without hidden answers;
- prompt-log templates;
- validation instructions.

Not allowed in this public repo:

- answer keys;
- hidden labels;
- full teacher solutions;
- private test data;
- exact scored mock solutions before use.

## Readiness Rule

The public repo can be marked structurally 100% only when the teacher-key boundary is explicit. Actual teacher-key content should be completed in the private repo before live graded use.
