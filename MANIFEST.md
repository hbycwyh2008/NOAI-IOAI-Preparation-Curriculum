# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Machine-readable source of truth | `curriculum_spec.json` schema version 3 |
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 101 unique phase-local Markdown packets |
| Executable pathway layer | exact NOAI Round 1, NOAI Round 2, and IOAI full-extension routes with recovery dependencies |
| Student progress layer | pseudonymous JSON ledger, schema, example, manager, route state, Red debt, qualifications, and drill history |
| Operational planning layer | ledger-aware next-Session planner and deterministic recent-repeat-aware daily-drill generator |
| Daily model-recognition layer | 36 public scenarios, generated five-scenario worksheets, reusable answer record, private-key protocol, mastery rule |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| Modeling workflow backbone | task formalisation → data quality → feature engineering → model selection → tuning → ensembling → reproducibility and postmortem |
| Mastery execution layer | workflow crosswalk, student mastery dashboard, progress ledger, daily drills, and cohort review protocol |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |
| D2L concept-to-code bridge | six required packets embedded in Sessions 61, 62, 63, 65, 66, and 68 |

## Source Priority

1. `curriculum_spec.json` — counts, Phase ranges, exact route Sessions, continuation dependencies, workflow checkpoints, operational tools, progress contract, and evidence boundaries;
2. `student_progress.schema.json` — machine-readable student-state shape and privacy-safe fields;
3. `02_Class_Missions/README.md` — canonical Phase order;
4. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
5. phase-local Session packet — classroom cycle, task, evidence, and gate;
6. selected executable pathway document — exact Session subset/extension for the named goal;
7. linked templates, assessments, daily drills, and resource maps — supporting material;
8. `00_Course_Overview/Workflow_Competency_Crosswalk.md` — recurring modeling decisions and evidence gates;
9. `01_Student_Start/07_Mastery_Dashboard.md` — human-readable student evidence and independence record;
10. the student’s private progress ledger — route state, Red debt, qualifications, assignments, and reviewed score metadata;
11. `09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md` — cohort remediation and promotion decisions;
12. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning, evidence boundaries, and release records.

The executable routes, progress records, workflow crosswalk, drills, and mastery records support the canonical pathway; they do not create parallel canonical Sessions or replace launchers.

## Pathway Dependency Contract

- NOAI Round 1 contains 45 Sessions and completes Session 57 before the Session 58 checkpoint.
- NOAI Round 2 does not repeat Sessions already credited by Round 1. It recovers Sessions 32 and 47, then continues through Sessions 59–78.
- IOAI full preparation contains Sessions 1–78 exactly once. A student entering from compressed Round 1 must recover Sessions 19–23, 32, 34–39, and 47 before Session 59.
- A pathway document and `curriculum_spec.json` must declare the same ordered Session list. Drift fails CI.

## Student Progress Contract

- Every ledger uses schema version 1 and a pseudonymous `student_id`; names and email addresses are prohibited.
- `red_sessions` is always a subset of `completed_sessions`: Red means attempted evidence with unresolved prerequisite debt, not “never seen.”
- `qualified_pathways` records only inspected exit-gate decisions, not attendance or self-report.
- `drill_history` records assigned Set IDs, scenario IDs, level, reviewed status, and compact scores; it does not contain protected answers.
- The public example is structural only. Real student ledgers remain in private course repositories.
- The human-readable mastery dashboard remains the evidence index; the ledger is operational state, not proof of mastery.

## Repository Automation Contract

- Validation and audit workflows are read-only. They may generate temporary files and Actions artifacts, but they must not commit or push to `main`.
- `scripts/validate_curriculum_spec.py` verifies launchers, packet counts, exact route tables, continuation/recovery dependencies, workflow checkpoints, progress schema/example, operational tools, drill IDs, repeat policy, and evidence boundaries.
- `scripts/manage_student_progress.py` creates, validates, updates, and scores private progress ledgers without storing answers.
- `scripts/plan_learning_path.py` reads ledger state and produces evidence-aware next-Session plans. It never changes mastery data or bypasses an entry gate.
- `scripts/generate_daily_model_drill.py` produces deterministic answer-key-free worksheets, avoids the configured recent assignment window when possible, and mutates a ledger only with explicit `--record-progress`.
- All three operational tools expose `--self-test`; all validation workflows execute those tests.
- `scripts/generate_ready_notebooks.py` defines notebook content. `scripts/generate_ready_notebooks_deterministic.py` is the CI entry point: it preserves IDs for unchanged cells and assigns content-derived IDs to new cells.
- Generated starter notebooks must exactly match the stable generation pipeline. A mismatch fails CI and must be corrected in the pull-request branch.
- Timestamped runtime and link-verification reports remain Actions artifacts rather than Git history.
- After a same-repository pull request is merged, its source branch is deleted automatically. Closed but unmerged branches and fork branches are preserved.
- The default branch is never a cleanup candidate.

## Evidence Contract

- Repository-controlled assets may be marked complete only when CI passes on the relevant commit.
- Ledger state and planner output are operational records; neither is a mastery decision.
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
python scripts/manage_student_progress.py --self-test
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/generate_ready_notebooks_deterministic.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, 101 phase-local canonical packets, valid internal paths and anchors, distinct canonical packets, exact executable routes, non-duplicated continuation routes, declared recovery bridges, a privacy-safe valid progress example, 36 unique recognition scenarios, recent-repeat control, deterministic operational tools, explicit external-evidence boundaries, stable notebook generation, read-only validation workflows, and merged-branch cleanup safeguards.
