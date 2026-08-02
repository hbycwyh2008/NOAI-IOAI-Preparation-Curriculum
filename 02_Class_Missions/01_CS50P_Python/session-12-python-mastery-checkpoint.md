# Session 12 — Unit Tests, Classes, and Python Mastery Checkpoint

**Class duration:** 75 minutes  
**Primary resource:** CS50P selected Unit Tests and Object-Oriented Programming content from the exact timestamp map

## Required Mastery

Students must be able to:

1. write a small function from a specification;
2. write positive, boundary, and invalid-input tests;
3. explain the difference between a returned value, printed output, and changed object state;
4. define a simple class with `__init__`, attributes, and one method;
5. read a CSV and create structured records or objects;
6. handle one invalid input or malformed row;
7. debug a failing test without deleting the test;
8. explain the final program without relying on copied code.

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | predict the output and state changes of a short class/function example |
| 8–15 | Talk Robin 1 | compare one useful test and one weak test |
| 15–22 | Entry Check | write one boundary test and explain what failure would mean |
| 22–35 | Core Pattern | specification → function/class → tests → failure → repair → evidence |
| 35–53 | Guided Practice | build and test a small experiment-record or dataset-row class |
| 53–67 | Independent Rebuild | complete a new CSV-processing mini-program with tests |
| 67–75 | Talk Robin 2 + Evidence | explain one failure, repair, and remaining limitation |

## Independent Rebuild Specification

Create a small program that:

- reads a CSV;
- validates required columns;
- converts at least one field safely;
- stores each valid row in a dictionary or simple object;
- computes one summary;
- includes at least four tests;
- reports malformed rows without silently discarding them.

## Required Evidence

- source code;
- tests and test results;
- one debugging record;
- one example of invalid input handling;
- a short explanation of state and return values;
- fresh-run evidence.

## Phase Gate

The student passes Phase 1 only when the program works from a fresh run and the student can explain every function, class attribute, test, and error-handling decision.