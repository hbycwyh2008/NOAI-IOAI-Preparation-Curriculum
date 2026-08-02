# Lesson 04 — Sorting Keys, Stability Intuition, and Ranking Tasks

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P sorting-key segments and sort a small table by different fields. |
| 8–15 min | Talk Robin 1 | Explain what the key function chooses. |
| 15–22 min | Entry Check | Predict sorted order for two examples. |
| 22–35 min | Core Pattern | Teacher models records → key → order → tie handling. |
| 35–53 min | Guided Practice | Solve supported ranking tasks. |
| 53–67 min | Independent Rebuild | Create a ranking task with a custom key. |
| 67–75 min | Talk Robin 2 + Evidence | Explain key choice and tie handling. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 6 — File I/O | sorted | 00:21:39–00:29:31 | Explain the difference between original data and sorted result. |
| Week 6 — File I/O | Sort Keys | 00:46:37–00:53:01 | Explain how key functions choose ranking values. |
| Week 6 — File I/O | Lambda Functions | 00:53:01–00:57:13 | Recognize a short ranking key. |

## 2. Talk Robin 1

Prompt: what value is used for sorting, and what should happen when two records tie?

## 3. Entry Check

Predict sorted order for two examples.

## 4. Core Pattern

```text
Records → choose comparison key → sort order → tie rule → ranked result
```

## 5. Guided Practice

Solve supported ranking tasks.

## 6. Independent Rebuild

Create a ranking task with a custom key.

## 7. Talk Robin 2 + Evidence

Submit CS50P segment notes, one sorted table, one key-function explanation, and one ranking-task rebuild.
