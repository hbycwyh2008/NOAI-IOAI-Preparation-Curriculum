# Mission 03.1 — Libraries, Files, Sorting, and Searching

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Watch assigned CS50P libraries and file I/O segments. |
| 8–15 min | Talk Robin 1 | Pair discussion: what module/file operation was used and what could fail. |
| 15–22 min | Entry Check | Check imports, file paths, CSV rows, and exception risk. |
| 22–35 min | Core Pattern | Teacher explains import/read/validate/process/write. |
| 35–53 min | Guided Practice | Read file-processing code and compare search/sort strategies. |
| 53–67 min | Independent Rebuild | Implement a small file-reading utility without copying. |
| 67–75 min | Talk Robin 2 + Evidence | Summarize, explain, and submit proof of learning. |

## Learning Target

By the end of this mission, you can explain the core ideas in **modules, CSV, file I/O, linear search, binary search, simple sorts** and demonstrate them through a paper-based or computational task.

## 1. Skill Warm-Up

### Required Resource

CS50P edX learning page:
https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

### Assigned CS50P segments

| CS50P week | Topic | Timestamp range | Student action |
|---|---|---:|---|
| Week 4 — Libraries | Libraries / Modules | 00:00:24–00:03:13 | Explain why modules are used. |
| Week 4 — Libraries | import | 00:03:13–00:07:35 | Trace imported namespace usage. |
| Week 4 — Libraries | from | 00:07:35–00:11:23 | Compare `import` vs `from`. |
| Week 6 — File I/O | File I/O | 00:00:24–00:01:17 | Explain file input/output. |
| Week 6 — File I/O | open | 00:05:54–00:13:55 | Identify file open/read/write behavior. |
| Week 6 — File I/O | with | 00:13:55–00:21:39 | Explain context-manager pattern. |
| Week 6 — File I/O | Comma-Separated Values | 00:29:31–00:46:37 | Identify header, row, and column structure. |
| Week 6 — File I/O | csv Library | 00:57:13–01:02:17 | Explain why the csv library is safer than manual string splitting. |

Use only the assigned segments above. Do not browse the entire course during class.

## 2. Talk Robin 1

Prompt: what does the program import, what file does it read, and what check should happen before processing?

## 3. Entry Check

1. Compare `import math` and `from math import sqrt`.
2. Explain the purpose of `with open(...) as file:`.
3. Identify one CSV schema risk.

## 4. Core Pattern

```text
Need module/file → import/open → read data → validate schema → process row → produce output
```

## 5. Guided Practice

Read file-processing code and compare search/sort strategies.

## 6. Independent Rebuild

Implement a small file-reading utility without copying a full solution.

## 7. Talk Robin 2 + Evidence

Submit CS50P segment notes, file-processing trace, independent utility, one documented bug, and a meaningful Git commit.
