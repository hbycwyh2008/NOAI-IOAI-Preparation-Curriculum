# Lesson 03 — Function Decomposition and Return-Value Tracing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Read a short multi-function program and mark each function call. |
| 8–15 min | Talk Robin 1 | Explain where the value enters, changes, and returns. |
| 15–22 min | Entry Check | Trace two function calls by hand. |
| 22–35 min | Core Pattern | Teacher models call → parameter → local variable → return → caller. |
| 35–53 min | Guided Practice | Complete a trace table for a three-function program. |
| 53–67 min | Independent Rebuild | Write and trace a new two-function program. |
| 67–75 min | Talk Robin 2 + Evidence | Explain one return-value path and submit evidence. |

## 1. Skill Warm-Up

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

Submit the trace table, the rebuilt program, and one explanation of a common return-value mistake.
