# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 95 unique phase-local Markdown packets |
| Supporting assets | indexed setup, templates, assessments, resources, public documents, teacher planning, and readiness records |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |

## Source Priority

1. `02_Class_Missions/README.md` — canonical Phase order;
2. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
3. phase-local Session packet — classroom cycle, task, evidence, and gate;
4. linked templates, assessments, and resource maps — supporting material;
5. `00_Course_Overview/` — pacing and pathway summaries;
6. `09_Teacher_Planning/` and `10_Ready_to_Teach_Pack/` — planning and release evidence.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, phase-local canonical links, valid internal paths and anchors, distinct canonical packets, current indexes, and an explicit operational-readiness boundary.
