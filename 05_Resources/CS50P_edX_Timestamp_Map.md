# Harvard CS50’s Introduction to Programming with Python — edX Timestamp Map

Primary edX learning-page link:

https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f

This file records the exact lecture sections used by the Python foundation modules.

## Timestamp Basis and Delivery Rule

- The ranges below match the official Harvard CS50 OpenCourseWare lecture files used to build this map.
- The current edX player may require enrolment or may present a different player interface. Verify the section title and range from a student account before the cohort.
- Tables containing more than eight minutes of assigned video are **pre-class viewing**, not content that can fit inside an eight-minute Skill Warm-Up.
- During class, the Skill Warm-Up uses one exact excerpt, retrieval question, code fragment, or trace task lasting no more than eight minutes.
- Students should not browse the full course during class.

## Week 0 — Functions, Variables

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| hello.py / basic printed output | 00:00:24–00:03:19 | first contact with output and `print` |
| Command-line interface | 00:03:19–00:04:00 | environment awareness only |
| Python interpreter | 00:04:00–00:05:06 | environment awareness only |
| Functions, arguments, side effects | 00:05:06–00:07:35 | function concept and `print(...)` as an action |
| Bugs and debugging | 00:07:35–00:09:54 | debugging mindset |
| Return values and variables | 00:12:16–00:19:56 | variables, assignment, return-value idea |
| Multiple function arguments | 00:25:05–00:31:01 | function calls with more than one input |
| Named parameters | 00:31:01–00:40:48 | keyword arguments and output formatting |
| Escaping characters | 00:40:48–00:43:10 | string-output detail |
| f-Strings | 00:43:10–00:45:04 | formatted output |
| String methods | 00:45:04–00:54:43 | string processing |
| split | 00:57:50–00:59:35 | input parsing |
| Integers and operators | 00:59:35–01:03:13 | arithmetic and operators |
| calculator.py | 01:03:13–01:06:25 | input-process-output program |
| Type conversion | 01:06:25–01:14:36 | `input`, `int`, `float`, conversion errors |
| Floating-point values | 01:14:36–01:19:18 | decimal numbers |
| Numeric formatting | 01:19:18–01:22:47 | output formatting |
| Division | 01:22:47–01:26:14 | arithmetic and rounding context |
| Defining functions | 01:26:14–01:39:01 | `def`, parameters, helper functions |
| Scope | 01:39:01–01:41:17 | local variables |
| Return values | 01:41:17–01:45:11 | `return` versus `print` |

## Week 1 — Conditionals

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| Conditionals | 00:00:24–00:02:47 | condition concept |
| if | 00:02:47–00:09:56 | basic branching |
| elif | 00:09:56–00:15:06 | mutually exclusive branches |
| else | 00:15:06–00:18:30 | fallback branch |
| or | 00:18:30–00:22:06 | compound condition |
| Not Equal | 00:22:06–00:24:17 | comparison operator |
| Indentation, colons | 00:24:17–00:25:13 | syntax and block structure |
| and | 00:25:13–00:28:48 | compound condition |
| Chaining comparison operators | 00:28:48–00:32:20 | boundary checks |
| Bugs | 00:32:20–00:34:16 | branch-bug diagnosis |
| Modulo | 00:34:16–00:40:00 | even/odd and divisibility patterns |
| Boolean | 00:40:00–00:44:10 | Boolean return and condition values |
| Pythonic expressions | 00:44:10–00:48:15 | concise conditional expression |
| match | 00:48:15–00:55:41 | pattern-style branching |

## Week 2 — Loops

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| Loops and repeated actions | 00:00:24–00:16:29 | why loops exist and while-loop reasoning |
| for loops | 00:16:29–00:36:14 | `for`, iteration, range/list iteration |
| Lists and iteration over collections | 00:36:14–00:41:41 | loop through list data |
| len | 00:41:41–00:52:55 | index/count reasoning |
| Dictionaries, nested loops, and final synthesis | 00:52:55–01:20:47 | dictionary iteration, key/value reasoning, nested loops, and decomposition |

## Week 3 — Exceptions

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| Exceptions | 00:00:24–00:00:52 | what can go wrong |
| SyntaxError | 00:00:52–00:03:29 | parsing errors |
| ValueError | 00:03:29–00:08:52 | failed conversion |
| try, except | 00:08:52–00:14:18 | protected risky operation |
| NameError | 00:14:18–00:18:35 | undefined names |
| else | 00:18:35–00:22:40 | clean success path |
| Reprompting, break | 00:22:40–00:29:50 | repeated input validation |
| get_int | 00:29:50–00:35:48 | helper function for robust input |
| pass | 00:35:48–00:41:32 | deliberate no-op in exception handling |
| Function arguments | 00:41:32–00:43:52 | function-design detail |

## Week 4 — Libraries

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| Libraries | 00:00:24–00:00:54 | why libraries exist |
| Modules | 00:00:54–00:03:13 | module concept |
| import | 00:03:13–00:07:35 | `import module` |
| from | 00:07:35–00:11:23 | `from module import name` |
| randint, shuffle | 00:11:23–00:17:01 | random examples |
| statistics | 00:17:01–00:19:13 | mean/statistics examples |
| Command-line arguments, sys | 00:19:13–00:32:59 | `sys.argv` |
| sys.exit | 00:32:59–00:40:55 | safe program exit |
| Slices | 00:40:55–00:44:41 | sequence slicing |
| Packages, PyPI, pip | 00:44:41–00:47:10 | third-party packages |
| cowsay | 00:47:10–00:53:26 | package-use example |
| APIs, requests, JSON | 00:53:26–01:10:06 | API and JSON workflow |
| Making Your Own Libraries and `__name__` | 01:10:06–01:17:28 | custom modules, import side effects, and guarded `main` calls |

## Week 6 — File I/O

| Topic | Timestamp range | Use in repo |
|---|---:|---|
| File I/O | 00:00:24–00:01:17 | file input/output concept |
| lists | 00:01:17–00:05:54 | starting with in-memory data |
| open | 00:05:54–00:13:55 | opening files |
| with | 00:13:55–00:21:39 | context-manager pattern |
| sorted | 00:21:39–00:29:31 | sorting loaded data |
| Comma-Separated Values | 00:29:31–00:46:37 | CSV concept and row data |
| Sort Keys | 00:46:37–00:53:01 | key-based sorting |
| Lambda Functions | 00:53:01–00:57:13 | short key functions |
| csv Library | 00:57:13–01:02:17 | library overview |
| csv.reader | 01:02:17–01:07:49 | list-style row reading |
| csv.DictReader | 01:07:49–01:14:05 | dictionary-style row reading |
| csv.writer | 01:14:05–01:16:28 | writing rows |
| csv.DictWriter | 01:16:28–01:23:00 | dictionary-style row writing |

## Rule for Lessons

Each Python lesson must name:

1. the full course name;
2. the week;
3. the exact topic name;
4. the timestamp range;
5. whether viewing is pre-class or in-class;
6. what students must do with the segment.

Do not write only an abbreviation or paste only the course homepage.