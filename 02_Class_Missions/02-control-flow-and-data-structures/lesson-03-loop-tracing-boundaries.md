# Lesson 03 — Loop Tracing and Boundary Conditions

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P loop segments and read two loops to predict iteration count. |
| 8–15 min | Talk Robin 1 | Discuss where the boundary mistake occurs. |
| 15–22 min | Entry Check | Complete a loop trace for start, stop, and update. |
| 22–35 min | Core Pattern | Teacher models initialise → condition → body → update → stop. |
| 35–53 min | Guided Practice | Trace `for` and `while` examples. |
| 53–67 min | Independent Rebuild | Write one boundary-sensitive loop and trace it. |
| 67–75 min | Talk Robin 2 + Evidence | Explain one off-by-one error. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 2 — Loops | Loops and repeated actions | 00:00:24–00:16:29 | Explain loop purpose and while-loop risk. |
| Week 2 — Loops | for loops | 00:16:29–00:36:14 | Count iterations and trace loop variables. |
| Week 2 — Loops | len | 00:41:41–00:52:55 | Trace index boundaries and avoid off-by-one errors. |

## 2. Talk Robin 1

Prompt: where does the loop start, what changes each time, and why does it stop?

## 3. Entry Check

Complete a trace table with columns: iteration, condition, loop variable, body effect, final value.

## 4. Core Pattern

```text
Initial state → condition check → body effect → update → next condition → final state
```

## 5. Guided Practice

Trace `for` and `while` examples.

## 6. Independent Rebuild

Write one boundary-sensitive loop and trace it.

## 7. Talk Robin 2 + Evidence

Submit CS50P segment notes, a loop trace table, a boundary table, one rebuilt loop, and one off-by-one explanation.
