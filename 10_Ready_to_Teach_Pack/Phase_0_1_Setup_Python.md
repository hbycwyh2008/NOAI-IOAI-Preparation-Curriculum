# Phase 0–1 Ready-to-Teach Pack

Sessions 1–8. Standard sessions are 90 minutes and use the routine in this directory's README.

---

## Session 1 — Competition Workflow and Baseline Thinking

### Required resource

Official NOAI syllabus: competition format and A–D knowledge areas; IOAI Academy Study Plan: **First 90 Minutes** and **Decisions Under Constraint** overview.

### Learning outcomes

Students can distinguish Round 1 from Round 2, define a valid baseline, explain why a valid submission comes before optimisation, and identify evidence required for mastery.

### Teacher input

1. Round 1 measures concept knowledge, calculations, code reading, and concise explanation.
2. Round 2 measures problem interpretation, data inspection, validation, modelling, iteration, and submission reliability.
3. A baseline is the simplest valid end-to-end solution that produces the official output and metric.
4. A high score without valid local validation is weak evidence.
5. Competition order: understand task → inspect data → choose metric/split → baseline → validate → analyse errors → controlled improvement → final submission check.

### Entry check

1. What is the difference between a model and a complete competition solution?
2. Why is a valid low-scoring submission better than an unfinished advanced model?
3. Name one risk that could invalidate a leaderboard result.

### Guided practice

Given a binary image-classification task, students sort 12 action cards into the correct order. Cards include reading the metric, inspecting labels, training a large model, creating a validation split, checking submission columns, and reviewing errors.

### Worksheet

1. Define *baseline* in one sentence.
2. Explain why the test set must not influence model selection.
3. Put these in order: error analysis, task reading, final submission validation, baseline, data audit.
4. A model obtains 0.94 training accuracy and 0.61 validation accuracy. What is the immediate concern?
5. A leaderboard score rises after using a feature created from the target column. Is the improvement valid? Explain.
6. Write a 20-minute emergency plan for obtaining the first valid submission.

### Independent transfer

Create a one-page personal competition workflow and a risk register containing at least five risks, warning signs, and prevention actions.

### Exit ticket

The teacher gives one unfamiliar task statement. The student states the problem type, metric to inspect, first validation decision, and minimum baseline.

---

## Session 2 — Evidence System, GitHub, and Bohrium Readiness

### Required resource

Course files: `01_Student_Start/00_How_This_Course_Works.md`, `01_Set_Up_Student_GitHub_Repo.md`, `04_How_To_Submit_Evidence.md`, and Bohrium setup guide.

### Learning outcomes

Students can create the required repository structure, run a notebook from a clean environment, make meaningful commits, and distinguish final output from learning evidence.

### Teacher input

- A screenshot is evidence that something appeared, not evidence that the process is reproducible.
- Good evidence includes source files, inputs, environment notes, outputs, error logs, and revision history.
- A meaningful commit describes the learning change: `add confusion-matrix calculations`, not `update`.
- Every notebook must run top-to-bottom after kernel restart.

### Guided practice

Students create the repository structure, add `environment.md`, run a package-version cell, intentionally cause one import error, repair it, and commit both the error record and working file.

### Worksheet

1. Which three files would best prove that a model experiment is reproducible?
2. Rewrite `final update` as a meaningful commit message.
3. Explain why notebook cells run out of order are dangerous.
4. What should never be committed to GitHub?
5. Write the command or interface action used to restart and run all notebook cells.
6. Record one difference between local Python and the Bohrium runtime.

### Independent transfer

From a new empty folder, reproduce the environment check and repository structure without following the guided steps line by line.

### Exit ticket

Show the teacher a clean-run notebook, one meaningful commit, and an error log entry.

---

## Session 3 — Functions, Variables, Expressions, and Output

### Required resource

CS50P: **Week 0 — Functions, Variables**, sections on functions, arguments, return values, variables, strings, integers, floats, and formatted strings.

### Learning outcomes

Students can trace expressions, distinguish printing from returning, define small functions, and predict values and types.

### Teacher input

- Assignment binds a value to a name; equality testing uses `==`.
- `print` creates output; `return` sends a value back to the caller.
- Function parameters are local names.
- Type conversion should be explicit at input boundaries.
- Evaluate nested expressions from the innermost operation outward.

### Worked example

Trace:

```python
def score(correct, total):
    ratio = correct / total
    return round(ratio * 100, 1)

result = score(17, 20)
print(f"Score: {result}%")
```

Students annotate parameter binding, intermediate value, return value, type, and printed output.

### Worksheet

1. State the value and type of `7 // 2`, `7 / 2`, `7 % 2`, and `str(7) + "2"`.
2. Explain the difference between `print(x)` and `return x`.
3. Trace:
   ```python
   x = 4
   y = x * 3
   x = y - 2
   print(x, y)
   ```
4. Complete a function `mean(a, b, c)` that returns the arithmetic mean.
5. Find and repair the error: `age = input("Age: "); next_age = age + 1`.
6. Write a function converting Celsius to Fahrenheit and test two cases.

### Guided practice

Pairs trace four short functions before running them, then compare predictions with execution.

### Independent transfer

Build a three-function grade-summary program: input validation, percentage calculation, and formatted report. No copied full solution.

### Exit ticket

Cold trace of a function with two parameters and one local variable.

---

## Session 4 — Input, Types, Conversion, Exceptions, and Debugging

### Required resource

CS50P: **Week 0 — Functions, Variables** input/type conversion and **Week 3 — Exceptions**, `try`, `except`, `else`, loops for repeated input.

### Learning outcomes

Students can identify common exceptions, validate input, read a traceback from the final line upward, and repair type/value errors.

### Teacher input

- Syntax errors prevent parsing; runtime exceptions occur during execution; logic errors produce wrong results.
- The final traceback line names the exception and message.
- Catch only expected exceptions and keep the protected block small.
- Validation checks meaning after conversion; conversion alone is not validation.

### Worksheet

1. Classify each as syntax, runtime, or logic error.
2. What information is in the final line of a traceback?
3. Repair:
   ```python
   number = int(input("Positive integer: "))
   print(100 / number)
   ```
   so invalid text, zero, and negative values are handled deliberately.
4. Explain why `except:` is usually weaker than `except ValueError:`.
5. Predict which line fails and why:
   ```python
   values = [3, 5]
   print(values[2])
   ```
6. Write a repeated-input function that returns a float from 0 through 1.

### Guided practice

Students rotate through three broken programs: type conversion, invalid index, and division by zero. They must first write a diagnosis, then edit.

### Independent transfer

Create a robust command-line metric calculator that rejects impossible confusion-matrix counts and never crashes on ordinary bad input.

### Exit ticket

Given a traceback, identify exception, failing line, likely cause, and minimal repair.

---

## Session 5 — Conditionals and Boolean Logic

### Required resource

CS50P: **Week 1 — Conditionals**, comparison operators, `if/elif/else`, `and`, `or`, `not`, chained comparisons, and match where appropriate.

### Learning outcomes

Students can trace branching, simplify Boolean expressions, identify unreachable branches, and design mutually exclusive cases.

### Teacher input

- Conditions are evaluated top-to-bottom; the first true branch in an `if/elif/else` chain runs.
- Independent `if` statements may all run.
- Boundary values must be tested explicitly.
- De Morgan's laws help reason about negation.

### Worksheet

1. Trace output for scores 59, 60, 79, 80, and 101 in a supplied grade chain.
2. Explain the difference between two `if` statements and `if` followed by `elif`.
3. Simplify `not (x < 0 or x > 1)`.
4. Find the unreachable branch:
   ```python
   if x >= 0:
       ...
   elif x >= 10:
       ...
   ```
5. Write a condition for a valid probability.
6. Design decision rules for classifying model status as underfit, overfit, or plausible using training and validation scores.

### Guided practice

Students complete a boundary-value table before writing code. The teacher withholds execution until predictions are recorded.

### Independent transfer

Write a metric recommendation function based on class balance and the relative cost of false positives and false negatives.

### Exit ticket

One Boolean equivalence and one boundary-case trace.

---

## Session 6 — Loops, Strings, Lists, Dictionaries, and Tuples

### Required resource

CS50P: **Week 2 — Loops**, `while`, `for`, `range`, list/dictionary iteration; relevant CS50P notes on strings and collections.

### Learning outcomes

Students can trace iteration, choose an appropriate collection, accumulate results, count frequencies, and avoid off-by-one errors.

### Teacher input

- A loop needs a clear invariant: what is true before and after each iteration?
- `range(stop)` excludes `stop`.
- Use a list for ordered mutable values, tuple for fixed records, dictionary for key-value lookup, set for uniqueness.
- Initialise accumulators before the loop and update exactly once per intended item.

### Worksheet

1. Write the sequence produced by `range(2, 10, 3)`.
2. Trace the final values of `total` and `count` in a supplied loop.
3. Choose list, tuple, set, or dictionary for four scenarios and justify each.
4. Repair an off-by-one loop that skips the final item.
5. Count labels in `['cat','dog','cat','bird','dog','cat']` using a dictionary.
6. Explain why modifying a list while iterating over it can be unsafe.
7. Write code to calculate the mean without calling `sum`.

### Guided practice

Build a label-frequency report and compare two implementations: repeated `list.count` versus one dictionary pass.

### Independent transfer

Read a list of prediction/label pairs and produce TP, TN, FP, FN counts using one loop.

### Exit ticket

Select a data structure and trace one accumulation loop.

---

## Session 7 — Libraries, Files, CSV, and Exceptions

### Required resource

CS50P: **Week 4 — Libraries** and **Week 6 — File I/O**, imports, third-party packages, `with open`, CSV reader/writer, and exception-safe file access.

### Learning outcomes

Students can import modules correctly, read/write CSV data, use context managers, distinguish file paths from file contents, and validate column names.

### Teacher input

- `import module` and `from module import name` create different namespaces.
- A context manager closes files even when an exception occurs.
- Data files require schema checks: columns, types, missing values, duplicates.
- Never silently continue after loading the wrong file.

### Worksheet

1. Compare `import math` with `from math import sqrt` in the call syntax.
2. Explain the purpose of `with open(...) as file:`.
3. Repair a CSV program that treats every numeric value as a string.
4. What checks should occur immediately after reading a competition CSV?
5. Write code that raises a clear error when `target` is absent.
6. Explain relative versus absolute paths.
7. Given three exception messages, identify missing file, permission error, and malformed data.

### Guided practice

Students load a deliberately flawed CSV containing a missing column, duplicate row, nonnumeric value, and blank field. They produce an audit table before cleaning.

### Independent transfer

Write a reusable `load_and_audit_csv(path, required_columns)` function returning the data and an audit dictionary.

### Exit ticket

Explain one schema check and one reason a file may work on one machine but fail on another.

---

## Session 8 — Linear Search, Binary Search, and Simple Sorting

### Required resource

Teacher-selected CS50 Algorithms excerpt: linear search, binary search, selection sort, and bubble sort. Python implementation is secondary to paper tracing.

### Learning outcomes

Students can state the precondition for binary search, trace comparisons, explain worst-case growth informally, and implement linear search plus one elementary sort.

### Teacher input

- Linear search works on unsorted data and may inspect every item.
- Binary search requires sorted data and repeatedly halves the remaining interval.
- Selection sort chooses the next minimum; bubble sort swaps adjacent out-of-order items.
- Correctness and preconditions matter more than memorising complexity labels.

### Worksheet

1. Trace linear search for `8` in `[4, 1, 8, 3]`; count comparisons.
2. Trace binary search for `23` in `[3, 7, 11, 15, 19, 23, 27]`.
3. Why is binary search invalid on `[2, 9, 4, 7]`?
4. Complete one pass of bubble sort on `[5, 2, 4, 1]`.
5. Complete the first two selections of selection sort on the same list.
6. State a case where sorting before one search is not worth the extra work.
7. Implement linear search without `in` or `.index`.
8. Implement selection sort without `sorted` or `.sort`.

### Guided practice

Groups trace the same search with different targets: first, middle, last, absent. They compare the number of comparisons and explain rather than merely report.

### Independent transfer

Build and test both searches. The program must reject binary search on unsorted input or explicitly sort a copy and disclose that decision.

### Phase exit gate

Without notes, the student must:

- trace short Python programs accurately;
- write functions, conditions, loops, and collection operations;
- load and validate a CSV;
- diagnose a traceback;
- implement linear search and one simple sort;
- explain every submitted line selected by the teacher.