# Mission 16.2 — Pandas Data Audit and Visualisation

**Duration:** 75 minutes

## Learning Target

Students can inspect an unfamiliar comma-separated-value dataset, identify quality risks, produce a reproducible audit table, and create one diagnostic visualisation whose claim and limitation are stated precisely.

## Required Resources

Use the current official documentation as the source of truth:

1. **Pandas User Guide — 10 Minutes to Pandas**  
   https://pandas.pydata.org/docs/user_guide/10min.html
2. **Pandas User Guide — Working with Missing Data**  
   https://pandas.pydata.org/docs/user_guide/missing_data.html
3. **Pandas User Guide — Group By: Split-Apply-Combine**  
   https://pandas.pydata.org/docs/user_guide/groupby.html
4. **Matplotlib — Pyplot Tutorial**  
   https://matplotlib.org/stable/tutorials/pyplot.html

Teacher-assigned sections only:

| Documentation section | Student extraction |
|---|---|
| Object creation, viewing data, and selection | identify rows, columns, index, shape, and data types |
| Missing-data operations | distinguish missing-value detection from an imputation decision |
| GroupBy aggregation | create one grouped diagnostic table without losing the grouping meaning |
| Basic plotting | label axes/title and state what the figure does not prove |

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect a supplied `DataFrame.info()` result, missing-value summary, and one misleading plot. |
| 8–15 min | Talk Robin 1 | Explain the highest-risk column and what evidence is still missing. |
| 15–22 min | Entry Check | Identify shape, target, identifier candidates, data types, duplicate risk, and missing-value risk. |
| 22–35 min | Core Pattern | Teacher models load → inspect schema → validate rows/keys → quantify missingness/duplicates → group/slice → visualise → state limits. |
| 35–53 min | Guided Practice | Audit a small mixed-type dataset and create one grouped table and one diagnostic figure. |
| 53–67 min | Independent Rebuild | Audit and visualise a new comma-separated-value file from a fresh notebook without copying the guided cells. |
| 67–75 min | Talk Robin 2 + Evidence | Defend the main data-quality finding and submit reproducible evidence. |

## 1. Skill Warm-Up

Complete:

```text
Rows and columns:
Likely target:
Possible identifier:
Unexpected data type:
Column with most missing values:
Duplicate or repeated-entity risk:
What the supplied plot appears to show:
What the plot cannot prove:
```

## 2. Talk Robin 1

Partner prompt: which finding could invalidate a model or split, and what additional check is required?

## 3. Entry Check

1. What is the difference between `DataFrame.shape`, `DataFrame.info()`, and `DataFrame.describe()`?
2. Why is `dropna()` not an automatic solution?
3. Why can duplicate rows or repeated entities create leakage?
4. What must be labelled on a diagnostic plot?

## 4. Core Pattern

```text
Load
→ Confirm schema and unit of observation
→ Inspect data types and ranges
→ Quantify missing values and duplicates
→ Check identifiers, groups, labels, and leakage clues
→ Aggregate meaningful slices
→ Visualise one diagnostic relationship
→ Record finding, limitation, and next action
```

## 5. Guided Practice

Students create an audit table with:

| Check | Code or method | Result | Risk | Next action |
|---|---|---|---|---|
| shape/schema |  |  |  |  |
| data types |  |  |  |  |
| missing values |  |  |  |  |
| duplicates/repeated entities |  |  |  |  |
| target distribution |  |  |  |  |
| grouped slice |  |  |  |  |
| train/test or time/source clue |  |  |  |  |

Then create one plot with a title, labelled axes, readable units, and a one-sentence limitation.

## 6. Independent Rebuild

From a fresh notebook and unfamiliar comma-separated-value file:

1. load the data without hidden notebook state;
2. produce the complete audit table;
3. create one grouped diagnostic table;
4. create one appropriate plot;
5. write the highest-priority data risk;
6. propose one next check without modifying the data prematurely.

## 7. Talk Robin 2 + Evidence

Submit:

- `data_audit.ipynb` or equivalent reproducible notebook;
- schema and missing-value table;
- duplicate/repeated-entity check;
- grouped diagnostic table;
- labelled figure;
- one finding, one limitation, and one next action;
- fresh-kernel run evidence.