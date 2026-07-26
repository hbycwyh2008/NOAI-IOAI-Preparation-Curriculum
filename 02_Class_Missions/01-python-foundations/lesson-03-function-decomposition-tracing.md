# Lesson 03 — Function Decomposition and Return-Value Tracing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P function segments and mark each function call. |
| 8–15 min | Talk Robin 1 | Explain where the value enters, changes, and returns. |
| 15–22 min | Entry Check | Trace two function calls by hand. |
| 22–35 min | Core Pattern | Teacher models call → parameter → local variable → return → caller. |
| 35–53 min | Guided Practice | Complete a trace table for a three-function program. |
| 53–67 min | Independent Rebuild | Write and trace a new two-function program. |
| 67–75 min | Talk Robin 2 + Evidence | Explain one return-value path and submit evidence. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 0 — Functions, Variables | Multiple function arguments | 00:25:05–00:31:01 | Trace how each argument binds to a parameter. |
| Week 0 — Functions, Variables | Defining functions | 01:26:14–01:39:01 | Mark function header, parameter names, and body. |
| Week 0 — Functions, Variables | Scope | 01:39:01–01:41:17 | Explain why local variables do not exist everywhere. |
| Week 0 — Functions, Variables | Return values | 01:41:17–01:45:11 | Trace the return value back to the caller. |

Students inspect a short program with `main`, a helper function, and a return value.

## 2. Talk Robin 1

Partner prompt: where does the original input go, and which function returns the final answer?

## 3. Entry Check

1. What is the difference between printing a value and returning a value?
2. What is a local variable?
3. In one sentence, explain why helper functions make code easier to test.

## 4. Core Pattern

```text
Input → function call → parameters → local work → return value → caller uses result
```

## 5. Guided Practice

Students complete a trace table with columns: line, function, parameter value, local variable, return value, printed output.

## 6. Independent Rebuild

Write a new two-function program that converts raw input into a final answer. Then trace it without running it.

## 7. Talk Robin 2 + Evidence

Submit the CS50P segment notes, trace table, rebuilt program, and one explanation of a common return-value mistake.
