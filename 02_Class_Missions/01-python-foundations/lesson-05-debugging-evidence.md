# Lesson 05 — Error Messages, Defensive Checks, and Debugging Evidence

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P debugging and exception segments, then read three common Python errors. |
| 8–15 min | Talk Robin 1 | Explain what the error message is pointing to. |
| 15–22 min | Entry Check | Match error types to fixes. |
| 22–35 min | Core Pattern | Teacher models reproduce → locate → explain → fix → verify. |
| 35–53 min | Guided Practice | Debug a small broken program with a record. |
| 53–67 min | Independent Rebuild | Create and fix a small bug intentionally. |
| 67–75 min | Talk Robin 2 + Evidence | Submit debug log and verification. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 0 — Functions, Variables | Bugs and debugging | 00:07:35–00:09:54 | Explain why bugs are normal evidence, not failure. |
| Week 3 — Exceptions | SyntaxError | 00:00:52–00:03:29 | Identify syntax errors before runtime. |
| Week 3 — Exceptions | ValueError | 00:03:29–00:08:52 | Explain failed conversion. |
| Week 3 — Exceptions | try, except | 00:08:52–00:14:18 | Mark the risky line and handler. |
| Week 3 — Exceptions | NameError | 00:14:18–00:18:35 | Explain undefined-name errors. |
| Week 3 — Exceptions | Reprompting, break | 00:22:40–00:29:50 | Explain repeated validation. |
| Week 3 — Exceptions | pass | 00:35:48–00:41:32 | Explain deliberate no-op and why silent failure is risky. |

Students inspect `NameError`, `TypeError`, `IndexError`, and `ValueError` examples.

## 2. Talk Robin 1

Prompt: what does the error message tell you, and what does it not tell you?

## 3. Entry Check

1. What is the first line you should read in a traceback?
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

Submit the CS50P segment notes, debug log, fixed code, and one defensive check that would prevent the bug.
