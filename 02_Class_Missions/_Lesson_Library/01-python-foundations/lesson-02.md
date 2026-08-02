# Mission 01.2 — Input/Output, Types, Conversion, and Debugging

**Duration:** 75 minutes  
**Pre-class required viewing:** assigned Harvard course segments below

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Complete a type-conversion and exception retrieval task based on the pre-class viewing. |
| 8–15 min | Talk Robin 1 | Pair discussion: where input enters, where conversion happens, and where errors appear. |
| 15–22 min | Entry Check | Predict type, value, and possible exception for short snippets. |
| 22–35 min | Core Pattern | Teacher explains input → convert → validate → handle error → output. |
| 35–53 min | Guided Practice | Trace five short programs and repair three broken programs. |
| 53–67 min | Independent Rebuild | Write a validated input-process-output program without copying the guided example. |
| 67–75 min | Talk Robin 2 + Evidence | Submit code, trace, debugging record, and explanation. |

## Pre-Class Required Resource

**Harvard CS50’s Introduction to Programming with Python on edX**  
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned Segments

| Week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 0 — Functions, Variables | Type conversion | 01:06:25–01:14:36 | Explain why `input()` produces strings and why conversion is needed. |
| Week 0 — Functions, Variables | Floating-point values | 01:14:36–01:19:18 | Predict the value and type after `float(...)`. |
| Week 0 — Functions, Variables | Numeric formatting | 01:19:18–01:22:47 | Explain one formatted numeric output. |
| Week 3 — Exceptions | SyntaxError | 00:00:52–00:03:29 | Identify parsing errors before runtime. |
| Week 3 — Exceptions | ValueError | 00:03:29–00:08:52 | Explain failed conversion. |
| Week 3 — Exceptions | try, except | 00:08:52–00:14:18 | Mark the risky line and the handler. |
| Week 3 — Exceptions | else | 00:18:35–00:22:40 | Explain the clean success path. |
| Week 3 — Exceptions | Reprompting, break | 00:22:40–00:29:50 | Explain repeated validation. |
| Week 3 — Exceptions | get_int | 00:29:50–00:35:48 | Identify helper-function structure for robust input. |

Complete the assigned segments before class or in a separately scheduled resource session. The full package does not fit inside the eight-minute Skill Warm-Up.

## 1. Skill Warm-Up

For one supplied snippet, record:

```text
Raw input type:
Conversion attempted:
Possible exception:
Validation rule:
Safe output:
```

## 2. Talk Robin 1

Partner prompt: which line can fail, what exception would appear, and what evidence proves the fix works?

## 3. Entry Check

1. Predict the type of `input("Age: ")`.
2. Explain why `int("3.5")` fails.
3. Identify the risky line inside a `try` block.

## 4. Core Pattern

```text
Raw input string → explicit conversion → validation check → exception handling → safe output
```

## 5. Guided Practice

Trace five short programs and repair three broken programs.

## 6. Independent Rebuild

Write a validated input-process-output program without copying the guided example.

## 7. Talk Robin 2 + Evidence

Submit:

- pre-class viewing note;
- one type-conversion trace;
- one repaired error;
- one robust input function;
- one explanation of why the program no longer crashes on ordinary bad input.