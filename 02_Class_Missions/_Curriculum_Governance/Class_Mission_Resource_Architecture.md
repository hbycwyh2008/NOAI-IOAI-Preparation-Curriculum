# Class Mission Resource Architecture

## Canonical Teaching Layer

```text
02_Class_Missions/00_... through 08_...
→ SESSION_LAUNCHER.md
→ phase-local lesson packet
```

Sessions 1–78 are the only canonical schedule. The launchers currently reference 95 unique phase-local Markdown packets. No canonical launcher enters `_Lesson_Library`.

## Optional Resource Layer

`_Lesson_Library` contains 96 remaining lesson files for remediation, extension, alternative explanations, reproductions, mocks, and optional competition practice.

## Governance Layer

`_Curriculum_Governance` contains architecture, distribution, and maintenance records. It is not used for student delivery.

## Change Rule

A new scheduled lesson must be created inside its numbered Phase and linked from the launcher. A file placed only in `_Lesson_Library` is optional by definition.
