# Class Mission Resource Architecture

## Design Principle

The curriculum is organised by **learning dependency**, not by a flat list of topics or external resources.

```text
CS50P Python
→ NumPy / Pandas / Matplotlib
→ Bohrium Chinese ML foundations
→ AI History and Thinking Humans
→ Andrew Ng ML + mathematics intuition + embedded Kaggle practice + model recognition + typical tasks
→ Andrew Ng DL + PyTorch + domain tasks
→ model comparison + EDA + feature engineering + evaluation
→ tuning + ensembling + competition simulation
```

## Separation of Responsibilities

| Location | Responsibility |
|---|---|
| numbered phase folders | scheduled route, prerequisites, gates, resource roles, and phase evidence |
| `04_AI_History_and_Thinking_Humans` | eight scheduled English reading seminars in Sessions 33–40 |
| `_Lesson_Library` | reusable lessons, remediation, alternatives, deeper practice, and extensions |
| `_Curriculum_Governance` | architecture, counts, auditing, and maintenance |
| `03_Templates` | student evidence templates, including AI History reading evidence |
| `04_Assessment` | public rubrics and evidence standards |
| `05_Resources` | external-course maps and resource details |
| `06_Starter_Code` / `06_Starter_Notebooks` | executable scaffolds |
| `09_Teacher_Planning` | canonical phase overviews, implementation, and pilot decisions |
| `10_Ready_to_Teach_Pack` | delivery, runtime, access, security, pilot, and release records |

## External Resource Roles

| Resource | Role |
|---|---|
| Harvard CS50’s Introduction to Programming with Python | Python spine |
| NumPy, Pandas, and Matplotlib documentation | data-tool source of truth |
| 北京市十一学校《中学机器学习十五讲》 | pre-Andrew Chinese concept sequence |
| Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* | AI history, conceptual boundaries, claim auditing, and understanding/limitation analysis |
| Machine Learning Specialization | classical ML spine |
| Kaggle Learn | embedded workflow rehearsal inside Andrew ML model labs, not a standalone phase |
| StatQuest | model, statistics, probability, and evaluation intuition |
| 3Blue1Brown | linear-algebra and calculus intuition |
| Deep Learning Specialization | deep-learning concept spine |
| PyTorch courses and documentation | deep-learning implementation spine |
| official NOAI/IOAI tasks and rules | assessment format, constraints, and competition integration |

A resource title is not automatically a curriculum phase. Every resource needs a placement, student action, evidence requirement, and access verification.

## Scheduled-versus-Reusable Rule

- The canonical pathway contains 78 scheduled sessions.
- The reusable bank contains 155 mainline lessons and 16 Bohrium resource lessons.
- Phase 04 contains eight scheduled reading seminars outside the preserved 171-file bank count.
- Module 28 remains a reusable competition-integration bank and is not automatically scheduled after Session 78.
- Cohort compression may select less content, but it must not redefine canonical session numbers.

## Readiness Rule

Public structure and maintained assets are validated by:

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
```

Exact student runtime, authenticated access, private assessment security, current competition rules, and classroom evidence remain separate release gates.
