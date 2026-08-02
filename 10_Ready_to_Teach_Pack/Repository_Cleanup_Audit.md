# Repository Cleanup Audit

## Scope

The cleanup reviewed files, navigation, internal links and anchors, duplicate canonical lessons, stale architecture language, historical branches, and open Issues.

## Changes Applied

- removed two merged historical agent branches;
- removed obsolete generator fragments and pre-publication instructions;
- removed legacy phase summaries and old Ready-to-Teach lesson copies;
- removed the empty former lesson-library layer and every maintained reference to it;
- repaired discovered internal links and the Andrew ML mathematics anchor;
- replaced three exact duplicate canonical packets with phase-specific lessons;
- added concise indexes for setup, templates, assessment, resources, public documents, diagnostics, pilots, and readiness records;
- centralised hyperparameter-tuning resources;
- rewrote selected-content maps for current phase-local paths;
- added permanent repository-hygiene validation to CI.

## Current Navigation

```text
Phase
→ SESSION_LAUNCHER.md
→ phase-local Session packet
```

## Validation Commands

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/validate_repository_hygiene.py
python scripts/check_required_links.py
```

Repository hygiene does not replace exact runtime qualification, authenticated access, private assessment security, representative pilots, full-cohort evidence, or current competition-year verification.
