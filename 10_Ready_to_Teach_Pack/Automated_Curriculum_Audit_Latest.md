# Automated Curriculum Audit

- Commit: `7e40710e0c419fbfb1b2911e260b53e93273e9bd`
- Runner: GitHub Actions / Python 3.12
- Exit code: `1`

```text
Curriculum structure validation passed.
Canonical sessions: 78
Phase-local canonical lesson packets: 95
Extension/remediation lesson files: 0
Normal delivery path: Phase → Session Launcher → phase-local lesson
Canonical launcher links into the-former-extension-library: 0
Public file-structure and internal-consistency coverage: 100%
Operational, pilot, privacy, runtime, access, and annual-rule readiness remain separate.
Readiness contract validation failed:
- Broken internal link in 02_Class_Missions/README.md: ./the-former-extension-library/README.md
- Broken internal link in 02_Class_Missions/README.md: ./_Curriculum_Governance/README.md
Class Missions launcher validation passed.
Canonical launcher coverage: Sessions 1–78 exactly once
Phase-local lesson links: 95
Canonical links into the-former-extension-library: 0
Normal delivery path: Phase → Session Launcher → phase-local lesson
```
