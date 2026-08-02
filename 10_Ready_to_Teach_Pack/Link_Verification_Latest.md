# Required Resource Link Verification

This file is a persistent release record and is overwritten by `scripts/check_required_links.py` on validated main-branch runs.

No release result has been recorded for this branch snapshot yet. See the Ready-to-Teach workflow for the current pull-request check result.

## Interpretation

- Automated checks establish public URL reachability.
- `401`, `403`, and `429` responses may indicate a reachable host with authentication or rate limits.
- Teacher and student account access, regional availability, enrolment, payment, exact course structure, and legal access to the Phase 04 book require the separate `External_Access_Verification_Record.md`.

## Release Rule

Do not treat this placeholder as a passing result. A release is link-verified only when the generated record names the release check time and lists every required resource result.
