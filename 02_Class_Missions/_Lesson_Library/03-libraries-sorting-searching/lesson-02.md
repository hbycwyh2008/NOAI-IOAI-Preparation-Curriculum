# Mission 03.2 — Search and Sorting

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Review assigned CS50P sorting segments and a teacher-selected CS50 search/sort excerpt. |
| 8–15 min | Talk Robin 1 | Pair discussion: what precondition is required and what state changes. |
| 15–22 min | Entry Check | Check linear search, binary search, and simple sort traces. |
| 22–35 min | Core Pattern | Teacher explains state-table tracing for search and sort. |
| 35–53 min | Guided Practice | Trace algorithms on paper and count comparisons. |
| 53–67 min | Independent Rebuild | Implement and test linear search plus selection sort without built-in shortcuts. |
| 67–75 min | Talk Robin 2 + Evidence | Submit trace tables and implementation evidence. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

Teacher-selected CS50 algorithms excerpt: linear search, binary search, selection sort, and bubble sort.

### Assigned CS50P support segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 6 — File I/O | sorted | 00:21:39–00:29:31 | Explain what `sorted(...)` does in Python. |
| Week 6 — File I/O | Sort Keys | 00:46:37–00:53:01 | Explain how a key chooses the comparison value. |
| Week 6 — File I/O | Lambda Functions | 00:53:01–00:57:13 | Recognize a short key function. |

## 2. Talk Robin 1

Prompt: why does binary search require sorted input, and what changes after each comparison?

## 3. Entry Check

1. Compare linear and binary search.
2. State the precondition for binary search.
3. Trace one pass of selection sort.

## 4. Core Pattern

```text
Initial list → current index/range → comparison → update state → final found/order result
```

## 5. Guided Practice

Trace algorithms on paper and count comparisons.

## 6. Independent Rebuild

Implement and test linear search plus selection sort without built-in search/sort shortcuts.

## 7. Talk Robin 2 + Evidence

Submit CS50P segment notes, search/sort trace tables, implementation evidence, and one misconception explanation.
