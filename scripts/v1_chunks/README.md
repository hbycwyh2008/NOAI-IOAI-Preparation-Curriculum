# Legacy V1 Generator Chunks

This directory contains compressed source fragments from an obsolete curriculum generator.

They are retained only for historical recovery and must not be used to rebuild or overwrite the current curriculum.

The former GitHub Actions workflow that reconstructed and executed these fragments has been removed because it could overwrite the current 75-session pathway, Module 28, curated lesson timings, resource mappings, and validation rules.

## Current Source of Truth

Use these maintained files instead:

- `02_Class_Missions/` — canonical lesson content and lesson-specific duration;
- `00_Course_Overview/Detailed_Lesson_Sequence.md` — scheduled Sessions 1–75;
- `00_Course_Overview/Pacing_Guide.md` — pathway and timing policy;
- `10_Ready_to_Teach_Pack/` — teacher-facing phase summaries and assessment packs;
- `scripts/validate_curriculum_structure.py` — current consistency validator.

Do not add an executable workflow that decodes or runs these fragments. Any future recovery work must occur on a separate archival branch and must never write directly to `main`.