# Lesson 05 — Error Messages, Defensive Checks, and Debugging Evidence

**Duration:** 75 minutes  
**Pre-class required viewing:** assigned Harvard course segments below

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Read three Python errors and identify exception type, likely line, and first debugging action. |
| 8–15 min | Talk Robin 1 | Explain what the error message is pointing to. |
| 15–22 min | Entry Check | Match error types to fixes. |
| 22–35 min | Core Pattern | Teacher models reproduce → locate → explain → fix → verify. |
| 35–53 min | Guided Practice | Debug a small broken program with a record. |
| 53–67 min | Independent Rebuild | Create and fix a small bug intentionally. |
| 67–75 min | Talk Robin 2 + Evidence | Submit debug log and verification. |

## Pre-Class Required Resource

**Harvard CS50’s Introduction to Programming with Python on edX**  
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned Segments

| Week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 0 — Functions, Variables | Bugs and debugging | 00:07:35–00:09:54 | Explain why bugs are evidence for revision, not a final result. |
| Week 3 — Exceptions | SyntaxError | 00:00:52–00:03:29 | Identify syntax errors before runtime. |
| Week 3 — Exceptions | ValueError | 00:03:29–00:08:52 | Explain failed conversion. |
| Week 3 — Exceptions | try, except | 00:08:52–00:14:18 | Mark the risky line and handler. |
| Week 3 — Exceptions | NameError | 00:14:18–00:18:35 | Explain undefined-name errors. |
| Week 3 — Exceptions | Reprompting, break | 00:22:40–00:29:50 | Explain repeated validation. |
| Week 3 — Exceptions | pass | 00:35:48–00:41:32 | Explain deliberate no-op and why silent failure is risky. |

Complete the assigned segments before class or in a separately scheduled resource session. The full package does not fit inside the eight-minute Skill Warm-Up.

## 1. Skill Warm-Up

For each supplied error, record:

```text
Exception type:
Likely failure line:
What the message proves:
What it does not prove:
First test or inspection:
```

## 2. Talk Robin 1

Prompt: what does the error message tell you, and what does it not tell you?

## 3. Entry Check

1. Which part of a traceback should you inspect first?
2. Why should you reproduce the bug before fixing it?
3. What evidence proves that a fix worked?

## 4. Core Pattern

```text
Reproduce → locate → explain cause → make smallest fix → test again → record evidence
```

## 5. Guided Practice

Students debug a program with three bugs and complete a table: symptom, line, cause, fix, verification.

## 6. Independent Rebuild

Students create one intentional bug, exchange with a partner, fix it, and record the debugging process.

## 7. Talk Robin 2 + Evidence

Submit:

- pre-class viewing note;
- debug log;
- fixed code;
- one defensive check that would prevent the bug;
- fresh-run evidence showing the fix works.
