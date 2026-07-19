# Curriculum Pilot Protocol

A written curriculum cannot reach professional 100% validation without use by real students. This protocol converts the remaining pilot work into a controlled evidence cycle.

## Stage 1 — Teacher dry run

For every lesson before first delivery:

1. run the required resource segment and verify access;
2. complete the entry check without notes;
3. solve the worksheet and independent task;
4. run the starter notebook from a fresh kernel;
5. record actual time for each block;
6. identify prerequisite assumptions and likely misconceptions;
7. confirm that the exit evidence can be completed within the final minutes.

A teacher dry run passes when the full lesson fits within **80–95 minutes**, all files execute, and the independent task remains genuinely independent.

## Stage 2 — Small-group pilot

Use 3–6 students with mixed readiness.

Record for each lesson:

- number finishing the entry check independently;
- resource minutes actually used;
- misconceptions revealed in the talk round;
- guided-task completion rate;
- independent-task completion rate;
- number and type of technical failures;
- number needing language support;
- median submission time;
- exit-ticket accuracy;
- student confidence before and after;
- teacher intervention minutes.

## Stage 3 — Revision rule

Revise a lesson when any of the following occurs:

- more than 25% cannot start because a prerequisite is missing;
- fewer than 70% complete the guided task;
- fewer than 50% complete the independent transfer;
- the median lesson overruns by more than 10 minutes;
- the exit question reveals a shared misconception;
- technical setup consumes more than 10% of lesson time;
- students can run code but cannot explain the mechanism.

Do not lower the mastery standard. Adjust prerequisites, examples, scaffolding, resource length, dataset size, or task sequencing.

## Stage 4 — Full-cohort validation

A phase is validated only when:

- at least one full cohort completes the phase;
- lesson timing has been recorded rather than estimated;
- all assessed files match the current teacher keys;
- notebook/runtime failures are documented and fixed;
- mock-contest reliability is measured;
- changes are committed with a versioned pilot report.

## Pilot log template

| Session | Students | Planned min | Actual min | Guided completion | Independent completion | Exit accuracy | Technical failures | Required revision |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| | | | | | | | | |

## Student feedback prompts

1. Which instruction was unclear before you started?
2. Where did you first become stuck?
3. Which example changed your understanding?
4. Could you rebuild the method without the notebook?
5. What consumed time without improving learning?
6. Which AI assistance did you use, and what did you verify yourself?

## Versioning

Store each completed pilot report as:

```text
09_Teacher_Planning/Pilot/reports/YYYY-MM-DD_phase-name.md
```

Link the report to the curriculum commit tested and list every resulting file change.
