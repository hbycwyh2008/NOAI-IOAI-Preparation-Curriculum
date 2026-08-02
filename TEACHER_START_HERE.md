# Teacher Start Here

## Normal Teaching Workflow

```text
open Class Missions
→ choose the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the phase-local lesson
→ collect the named evidence
```

Begin at [Class Missions](02_Class_Missions/README.md) and read [How to Use Class Missions](02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md). Use the [canonical teacher phase overviews](09_Teacher_Planning/Phase_Overviews/README.md) for planning summaries; they do not replace Session launchers.

## Required Order

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and visualisation — Sessions 13–18
4. Bohrium ML foundations — Sessions 19–32
5. AI History and Thinking Humans — Sessions 33–40
6. Andrew Ng ML, mathematics, model labs, and embedded practice — Sessions 41–58
7. Andrew Ng DL and PyTorch — Sessions 59–70
8. Model comparison, EDA, features, and evaluation — Sessions 71–74
9. Tuning, ensembling, simulation, and postmortem — Sessions 75–78

## Before Each Cohort

1. archive current official NOAI/IOAI rules;
2. run the student diagnostic;
3. confirm legal book and authenticated course access;
4. qualify the exact student runtime;
5. pilot representative lesson types;
6. keep solutions, hidden labels, tests, and calibration material private;
7. complete the release-readiness gates.

## Special Phase Rules

- **Sessions 33–40:** assigned reading occurs before class; preserve the full seminar cycle.
- **Sessions 41–43:** use the mathematics bridge from task meaning through symbols, graphs, calculations, code, model behaviour, and limitations.
- **Sessions 75–78:** tuning follows diagnosis; ensembling follows stable single-model evidence; the final simulation must run from a fresh environment.

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

Passing automated checks establishes public repository coverage, not cohort-specific operational readiness.
