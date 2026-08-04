# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Machine-readable source of truth | `curriculum_spec.json` schema version 4 |
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 101 unique phase-local Markdown packets |
| Executable pathway layer | exact NOAI Round 1, NOAI Round 2, and IOAI full-extension routes with recovery dependencies |
| Student progress layer | pseudonymous schema-v2 ledger with migration, route state, Red debt, qualifications, one assignment per date, scores, and private-confirmation metadata |
| Operational decision layer | progress manager, mastery-eligibility report, ledger-aware pathway planner, and recent-repeat-aware daily-drill generator |
| Daily model-recognition layer | 36 public scenarios, generated five-scenario worksheets, dual-threshold public streak, private confirmation, and weekly maintenance |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| Modeling workflow backbone | task formalisation → data quality → feature engineering → model selection → tuning → ensembling → reproducibility and postmortem |
| Mastery execution layer | workflow crosswalk, student dashboard, private ledger, eligibility report, daily drills, and cohort review protocol |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |
| D2L concept-to-code bridge | six required packets embedded in Sessions 61, 62, 63, 65, 66, and 68 |

## Source Priority

1. `curriculum_spec.json` — counts, Phase ranges, exact routes, dependencies, checkpoints, operational tools, progress contract, mastery thresholds, and evidence boundaries;
2. `student_progress.schema.json` — private student-state shape and privacy-safe fields;
3. `02_Class_Missions/README.md` — canonical Phase order;
4. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
5. phase-local Session packet — classroom cycle, task, evidence, and gate;
6. selected executable pathway document — exact Session subset/extension for the named goal;
7. linked templates, assessments, daily drills, and resource maps — supporting material;
8. `00_Course_Overview/Workflow_Competency_Crosswalk.md` — recurring modeling decisions and evidence gates;
9. `01_Student_Start/07_Mastery_Dashboard.md` — human-readable evidence and independence record;
10. the student’s private progress ledger — operational state and compact reviewed metadata;
11. generated progress report — route, Red-debt, streak, confirmation, and maintenance status derived from the ledger;
12. `09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md` — human remediation and promotion decisions;
13. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning, evidence boundaries, and release records.

The executable routes, progress records, reports, drills, and mastery records support the canonical pathway; they do not create parallel canonical Sessions or replace launchers.

## Pathway Dependency Contract

- NOAI Round 1 contains 45 Sessions and completes Session 57 before Session 58.
- NOAI Round 2 recovers Sessions 32 and 47, then continues through Sessions 59–78 without repeating Round 1 Sessions.
- IOAI full preparation contains Sessions 1–78 exactly once. A student entering from compressed Round 1 recovers Sessions 19–23, 32, 34–39, and 47 before Session 59.
- A pathway document and `curriculum_spec.json` must declare the same ordered Session list. Drift fails CI.

## Student Progress Contract

- Every current ledger uses schema version 2 and a pseudonymous `student_id`; names and email addresses are prohibited.
- Schema-v1 ledgers migrate through `scripts/manage_student_progress.py migrate`; missing legacy baseline/metric scores remain null rather than being fabricated.
- `red_sessions` is always a subset of `completed_sessions`: Red means attempted evidence with unresolved debt, not “never seen.”
- `qualified_pathways` records only inspected exit-gate decisions.
- `drill_history` permits one assignment per date and records Set ID, scenario IDs, level, reviewed status, task-family accuracy, baseline/metric accuracy, and total score.
- `recognition_confirmation` stores only pass status and date for a fresh private secured set; protected content remains outside the ledger.
- The public example is structural only. Real student ledgers remain in private course repositories.
- The human-readable mastery dashboard remains the evidence index; the ledger and report are operational state, not proof by themselves.

## Model-Recognition Mastery Contract

- A public set qualifies only when teacher review records task-family accuracy ≥90% and baseline/metric accuracy ≥90%.
- Five qualifying reviewed daily sets in a row establish public eligibility only.
- A fresh private secured confirmation must pass after the public streak.
- A confirmation dated before the latest qualifying public set is invalid.
- After confirmation, two qualifying mixed maintenance sets are required per seven-day window.
- Total score is diagnostic and cannot compensate for failure of either required accuracy dimension.

## Repository Automation Contract

- Validation and audit workflows are read-only. They may generate temporary files and Actions artifacts, but they must not commit or push to `main`.
- `scripts/validate_curriculum_spec.py` verifies launchers, packet counts, exact routes, recovery dependencies, progress schema/example, migration and one-date rules, mastery thresholds, tools, drill IDs, repeat policy, and evidence boundaries.
- `scripts/manage_student_progress.py` creates, migrates, validates, updates, scores, and records private-confirmation status without storing answers.
- `scripts/report_student_progress.py` calculates route progress, Red debt, public eligibility, confirmation order, and weekly maintenance without inspecting protected content.
- `scripts/plan_learning_path.py` reads ledger state and produces evidence-aware next-Session plans without changing mastery data.
- `scripts/generate_daily_model_drill.py` restores the recorded set for an existing date, avoids recent assignments for a new date, and mutates a ledger only with explicit `--record-progress`.
- All four operational tools expose `--self-test`; all validation workflows execute those tests.
- `scripts/generate_ready_notebooks.py` defines notebook content. `scripts/generate_ready_notebooks_deterministic.py` preserves IDs for unchanged cells and assigns content-derived IDs to new cells.
- Generated starter notebooks must exactly match the stable generation pipeline. A mismatch fails CI.
- Timestamped runtime, link, and example progress reports remain Actions artifacts rather than Git history.
- After a same-repository pull request is merged, its source branch is deleted automatically. Closed but unmerged and fork branches are preserved.
- The default branch is never a cleanup candidate.

## Evidence Contract

- Repository-controlled assets may be marked complete only when CI passes on the relevant commit.
- Ledger state, generated reports, and planner output are operational records; teacher evidence inspection remains required.
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
python scripts/report_student_progress.py --self-test
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/generate_ready_notebooks_deterministic.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, 101 phase-local canonical packets, valid internal paths and anchors, exact routes, non-duplicated continuations, recovery bridges, a privacy-safe schema-v2 example, supported migration, one assignment per date, dual-threshold streak logic, private confirmation ordering, weekly maintenance, 36 unique scenarios, recent-repeat control, deterministic tools, stable notebooks, read-only workflows, and merged-branch cleanup safeguards.
