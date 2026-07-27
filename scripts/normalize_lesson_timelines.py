"""Legacy compatibility entry point.

This script previously rewrote every lesson timeline and regenerated the pacing and
sequence documents from a hard-coded 67-file assumption. The curriculum now has a
75-session scheduled pathway, a 155-lesson mainline bank, and an optional 16-lesson
Bohrium resource hub. Automatic bulk rewriting would destroy lesson-specific video
timings and curated overview documents.

The command is therefore intentionally validation-only. Use
`scripts/validate_curriculum_structure.py` for the current structural check. Edit
lesson timelines deliberately in their source files instead of mass-normalising them.
"""

from __future__ import annotations

from validate_curriculum_structure import main


if __name__ == "__main__":
    print(
        "normalize_lesson_timelines.py is now validation-only; "
        "no curriculum files will be rewritten."
    )
    raise SystemExit(main())
