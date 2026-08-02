# Lesson 03 — CSV Reading, Schema Checks, and Row-Wise Processing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P CSV segments and inspect a small CSV sample. |
| 8–15 min | Talk Robin 1 | Discuss what can go wrong in file reading. |
| 15–22 min | Entry Check | Identify header, row, type, and missing value issues. |
| 22–35 min | Core Pattern | Teacher models open → read → validate schema → process row → summarize. |
| 35–53 min | Guided Practice | Complete a CSV audit table. |
| 53–67 min | Independent Rebuild | Design a new row-wise processor. |
| 67–75 min | Talk Robin 2 + Evidence | Explain schema check and submit evidence. |

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 6 — File I/O | Comma-Separated Values | 00:29:31–00:46:37 | Identify rows, headers, and columns. |
| Week 6 — File I/O | csv Library | 00:57:13–01:02:17 | Explain why a CSV library is used. |
| Week 6 — File I/O | csv.reader | 01:02:17–01:07:49 | Trace list-style row reading. |
| Week 6 — File I/O | csv.DictReader | 01:07:49–01:14:05 | Trace dictionary-style row reading. |

## 2. Talk Robin 1

Prompt: what assumptions does the code make about columns, types, and missing values?

## 3. Entry Check

Identify header, row, type, and missing-value issues.

## 4. Core Pattern

```text
File → columns → row types → validation checks → row-wise processing → summary output
```

## 5. Guided Practice

Complete a CSV audit table.

## 6. Independent Rebuild

Design a new row-wise processor.

## 7. Talk Robin 2 + Evidence

Submit CS50P segment notes, a schema audit, row-processing pseudocode, and one file-reading risk note.
