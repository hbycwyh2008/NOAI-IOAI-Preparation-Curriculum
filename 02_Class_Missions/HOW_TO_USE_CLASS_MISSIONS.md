# How to Use Class Missions

## The Only Normal Teaching Path

```text
02_Class_Missions
→ open the assigned Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the linked lesson packet
→ collect the named evidence
```

Teachers and students should **not browse `_Lesson_Library` manually** during normal delivery.

## What Each Layer Means

| Layer | Who uses it | Purpose |
|---|---|---|
| numbered Phase folder | teacher and student | canonical teaching order |
| `SESSION_LAUNCHER.md` inside each Phase | teacher and student | exact session-by-session entry point |
| linked lesson file | teacher and student | classroom cycle, tasks, evidence, and gate |
| `_Lesson_Library` | curriculum maintainer; teacher only for remediation or extension | storage bank for reusable lesson bodies |
| `_Curriculum_Governance` | curriculum maintainer | audits, counts, architecture, and maintenance |

## Normal Class Workflow

1. The teacher announces the Phase and Session number.
2. Everyone opens the Phase folder.
3. Everyone clicks `SESSION_LAUNCHER.md`.
4. The teacher opens the exact linked lesson for that Session.
5. Students use only the resources and templates linked by that lesson.
6. The teacher collects the evidence named in the launcher and lesson.
7. The class advances only after the session or phase gate is satisfied.

## What Not to Do

Do not:

- open `_Lesson_Library` and choose a lesson by guessing;
- schedule every lesson-bank file;
- treat a module number such as `06-linear-regression` as a course-session number;
- teach from the governance documents;
- jump from a Phase README to unrelated lesson-bank modules;
- add an extension lesson to the canonical schedule without recording the change.

## Why Lesson Links May Display `_Lesson_Library`

The canonical launcher may open a file whose URL contains `_Lesson_Library`. That is intentional: the lesson body is stored once in the reusable bank, while the launcher decides where it belongs in the scheduled route.

The user should not navigate upward or select neighbouring library files. Use the browser Back button to return to the Phase launcher.

## When a Teacher May Open the Lesson Library Directly

Only for:

- reteaching after a failed gate;
- additional practice;
- a different explanation of the same concept;
- domain extension;
- competition reproduction or mock work;
- curriculum maintenance.

## Source-of-Truth Rule

- **Schedule:** numbered Phase folders and their launchers.
- **Lesson body:** exact file linked by the launcher.
- **Extra material:** `_Lesson_Library`.
- **Teacher planning and release evidence:** `09_Teacher_Planning` and `10_Ready_to_Teach_Pack`.

When two documents conflict, follow the current Phase launcher and fix the stale document.