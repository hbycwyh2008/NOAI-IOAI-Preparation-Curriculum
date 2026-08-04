# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Machine-readable source of truth | `curriculum_spec.json` schema version 2 |
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 101 unique phase-local Markdown packets |
| Executable pathway layer | exact NOAI Round 1, NOAI Round 2, and IOAI full-extension routes with recovery dependencies |
| Operational planning layer | evidence-aware next-Session planner and deterministic daily-drill generator |
| Daily model-recognition layer | 36 public scenarios, generated five-scenario worksheets, reusable answer record, private-key protocol, mastery rule |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| Modeling workflow backbone | task formalisation → data quality → feature engineering → model selection → tuning → ensembling → reproducibility and postmortem |
| Mastery execution layer | workflow crosswalk, student mastery dashboard, daily drills, and cohort review protocol |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |
| D2L concept-to-code bridge | six required packets embedded in Sessions 61, 62, 63, 65, 66, and 68 |

## Source Priority

1. `curriculum_spec.json` — counts, Phase ranges, exact route Sessions, continuation dependencies, workflow checkpoints, tools, and evidence boundaries;
2. `02_Class_Missions/README.md` — canonical Phase order;
3. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
4. phase-local Session packet — classroom cycle, task, evidence, and gate;
5. selected executable pathway document — exact Session subset/extension for the named goal;
6. linked templates, assessments, daily drills, and resource maps — supporting material;
7. `00_Course_Overview/Workflow_Competency_Crosswalk.md` — recurring modeling decisions and evidence gates;
8. `01_Student_Start/07_Mastery_Dashboard.md` — student evidence and independence record;
9. `09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md` — cohort remediation and promotion decisions;
10. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning, evidence boundaries, and release records.

The executable routes, workflow crosswalk, drills, and mastery records support the canonical pathway; they do not create parallel canonical Sessions or replace launchers.

## Pathway Dependency Contract

- NOAI Round 1 contains 45 Sessions and completes Session 57 before the Session 58 checkpoint.
- NOAI Round 2 does not repeat Sessions already credited by Round 1. It recovers Sessions 32 and 47, then continues through Sessions 59–78.
- IOAI full preparation contains Sessions 1–78 exactly once. A student entering from compressed Round 1 must recover Sessions 19–23, 32, 34–39, and 47 before Session 59.
- A pathway document and `curriculum_spec.json` must declare the same ordered Session list. Drift fails CI.

## Repository Automation Contract

- Validation and audit workflows are read-only. They may generate temporary files and Actions artifacts, but they must not commit or push to `main`.
- `scripts/validate_curriculum_spec.py` verifies that the machine-readable specification matches launchers, packet counts, exact route tables, continuation/recovery dependencies, workflow checkpoints, operational tools, drill IDs, and evidence boundaries.
- `scripts/plan_learning_path.py` produces evidence-aware next-Session plans. It never changes mastery data or bypasses an entry gate.
- `scripts/generate_daily_model_drill.py` produces deterministic answer-key-free worksheets from the maintained public scenario bank.
- Both operational tools expose `--self-test`; all validation workflows execute those tests.
- `scripts/generate_ready_notebooks.py` defines notebook content. `scripts/generate_ready_notebooks_deterministic.py` is the CI entry point: it preserves IDs for unchanged cells and assigns content-derived IDs to new cells.
- Generated starter notebooks must exactly match the stable generation pipeline. A mismatch fails CI and must be corrected in the pull-request branch.
- Timestamped runtime and link-verification reports remain Actions artifacts rather than Git history.
- After a same-repository pull request is merged, its source branch is deleted automatically. Closed but unmerged branches and fork branches are preserved.
- The default branch is never a cleanup candidate.

## Evidence Contract

- Repository-controlled assets may be marked complete only when CI passes on the relevant commit.
- Planner output is a recommendation based on declared evidence; it is not a mastery decision.
- Student runtime remains unqualified until tested on the exact named cohort environment.
- External access remains unverified until tested with intended account types, region, and network.
- Pilot claims require real student delivery evidence for every representative row.
- Annual alignment requires a dated review of current official material.
- Post-event task/environment alignment remains pending until inspectable official evidence is reviewed.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_curriculum_spec.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/generate_ready_notebooks_deterministic.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, 101 phase-local canonical packets, valid internal paths and anchors, distinct canonical packets, exact executable routes, non-duplicated continuation routes, declared recovery bridges, 36 unique recognition scenarios, deterministic operational tools, explicit external-evidence boundaries, stable notebook generation, read-only validation workflows, and merged-branch cleanup safeguards.
