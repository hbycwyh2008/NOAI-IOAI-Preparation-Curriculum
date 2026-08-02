# Class Mission Resource Architecture

## Design Principle

The curriculum is organised by **learning dependency**, not by a flat list of topics or external resources.

```text
CS50P Python
→ NumPy / Pandas / Matplotlib
→ Bohrium Chinese ML foundations
→ Kaggle workflow refresh
→ Andrew Ng ML + mathematics intuition + model recognition + typical tasks
→ Andrew Ng DL + PyTorch + domain tasks
→ model comparison + EDA + feature engineering + evaluation
→ tuning + ensembling + competition simulation
```

## Separation of Responsibilities

| Location | Responsibility |
|---|---|
| phase folders | scheduled route, prerequisites, gates, and resource roles |
| `_Lesson_Library` | reusable lessons, remediation, alternatives, deeper practice, and extensions |
| `_Curriculum_Governance` | architecture, counts, auditing, and maintenance |
| `03_Templates` | student evidence templates |
| `05_Resources` | external-course maps and resource details |
| `06_Starter_Code` / `06_Starter_Notebooks` | executable scaffolds |
| `09_Teacher_Planning` | implementation and pilot decisions |
| `10_Ready_to_Teach_Pack` | delivery and readiness records |

## External Resource Roles

| Resource | Role |
|---|---|
| Harvard CS50’s Introduction to Programming with Python | Python spine |
| NumPy, Pandas, Matplotlib documentation | data-tool source of truth |
| 北京市十一学校《中学机器学习十五讲》 | pre-Andrew Chinese concept sequence |
| Kaggle Learn | short workflow refresh |
| Machine Learning Specialization | classical ML spine |
| StatQuest | model/statistics intuition |
| 3Blue1Brown | linear-algebra/calculus intuition |
| Deep Learning Specialization | deep-learning concept spine |
| PyTorch courses and documentation | deep-learning implementation spine |
| official NOAI/IOAI tasks and rules | assessment format, constraints, and competition integration |

A resource title is not a curriculum phase. Every resource needs a placement, student action, and evidence requirement.
