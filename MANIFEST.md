# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 101 unique phase-local Markdown packets |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| Modeling workflow backbone | task formalisation → data quality → feature engineering → model selection → tuning → ensembling → reproducibility and postmortem |
| Mastery execution layer | workflow crosswalk, student mastery dashboard, and cohort review protocol |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |
| D2L concept-to-code bridge | six required packets embedded in Sessions 61, 62, 63, 65, 66, and 68 |

## Source Priority

1. `02_Class_Missions/README.md` — canonical Phase order;
2. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
3. phase-local Session packet — classroom cycle, task, evidence, and gate;
4. linked templates, assessments, and resource maps — supporting material;
5. `00_Course_Overview/Workflow_Competency_Crosswalk.md` — recurring modeling decisions and evidence gates;
6. `01_Student_Start/07_Mastery_Dashboard.md` — student evidence and independence record;
7. `09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md` — cohort remediation and promotion decisions;
8. other `00_Course_Overview/` files — pacing and pathway summaries;
9. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning and release evidence.

The workflow crosswalk and mastery records support the scheduled pathway; they do not create parallel Sessions or replace launchers.

## Repository Automation Contract

- Validation and audit workflows are read-only. They may generate temporary files and Actions artifacts, but they must not commit or push to `main`.
- Generated starter notebooks are checked against `scripts/generate_ready_notebooks.py`. A mismatch fails CI and must be corrected in the pull-request branch.
- Timestamped runtime and link-verification reports remain Actions artifacts rather than Git history.
- After a same-repository pull request is merged, its source branch is deleted automatically. Closed but unmerged branches and fork branches are preserved.
- The default branch is never a cleanup candidate.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, phase-local canonical links, valid internal paths and anchors, distinct canonical packets, current indexes, an explicit operational-readiness boundary, read-only validation workflows, and merged-branch cleanup safeguards.
