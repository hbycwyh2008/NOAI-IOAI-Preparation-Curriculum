# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | 95 unique phase-local Markdown packets |
| Extension/remediation library | 96 remaining `lesson-*.md` files |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |

## Source Priority

1. `02_Class_Missions/README.md` — canonical Phase order;
2. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
3. phase-local lesson packet — classroom cycle, tasks, evidence, and gate;
4. `_Lesson_Library` — optional remediation and extension only;
5. `00_Course_Overview/` — pacing and pathway summaries;
6. `10_Ready_to_Teach_Pack/` — delivery and release evidence.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, phase-local canonical links, valid internal paths, AI History and mathematics-bridge artifacts, and an explicit operational-readiness boundary.
