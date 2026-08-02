# Public Repository 100 Percent Coverage Definition

The repository has **100% public file-structure and internal-consistency coverage** when all maintained canonical and support assets satisfy the contracts below. This is not a blanket claim of operational readiness.

## Public Coverage Contract

1. Nine numbered phases contain Sessions 1–78 exactly once.
2. Every Phase README links to its Session launcher.
3. Every canonical Session links only to existing phase-local packets.
4. Canonical packets state duration, task, evidence, and gate.
5. Phase 4 contains eight English AI History seminars and its teacher/template/rubric package.
6. Phase 5 contains the Andrew ML mathematics transition and model-recognition/task resources.
7. Kaggle practice is embedded in Andrew ML rather than scheduled as a separate phase.
8. Phase 6 pairs deep-learning concepts with PyTorch implementation.
9. Phases 7–8 cover systematic EDA, evaluation, tuning, ensembling, simulation, and postmortem.
10. the former extension library contains extension/remediation material only and has a current index.
11. Student setup, templates, assessments, resources, public documents, teacher planning, and Ready-to-Teach records have clear indexes.
12. Internal Markdown links and anchors resolve.
13. Canonical Session packets are not exact duplicates.
14. Obsolete generator fragments, legacy phase summaries, and superseded delivery packs are absent.
15. Current validators pass:

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
```

## Separate Operational Gates

Public coverage does not prove:

- successful execution in the exact student environment;
- authenticated access to external courses or legal access to the Phase 4 book;
- current permission for packages, APIs, models, external data, or internet use;
- assessment-security completion;
- representative classroom timing and comprehension;
- full 78-Session cohort delivery;
- current-year competition alignment;
- competition performance.

Use the [Public Repository Readiness Dashboard](../10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md), [Release Readiness Gates](../10_Ready_to_Teach_Pack/Release_Readiness_Gates.md), and open operational-readiness Issue for those decisions.
