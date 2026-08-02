# Release Readiness Gates

This document defines the evidence required before the curriculum may be described as fully ready for a specific competition year and student cohort.

A percentage must never combine structural completeness with unverified classroom, runtime, security, or annual-rule claims.

## Gate 1 — Repository Structure

- [ ] `python scripts/validate_curriculum_structure.py` passes on the release commit.
- [ ] Required lesson counts, pathway counts, source-of-truth rules, and internal links are consistent.
- [ ] No obsolete generator can overwrite maintained lesson content.

Evidence:

- Release commit SHA:
- Validation date:
- Validator output or workflow URL:
- Reviewer:

## Gate 2 — External Links and Authenticated Resources

- [ ] `python scripts/check_required_links.py` passes.
- [ ] Harvard, Coursera, Bohrium, and other authenticated resources have been manually opened using the intended teacher/student accounts.
- [ ] Exact modules, videos, chapters, and timestamps still match the lesson assignments.

Evidence:

- Verification date:
- Account type tested:
- Broken or changed resources:
- Replacement mapping:

## Gate 3 — Student Runtime

- [ ] A clean student environment can be installed from the documented instructions.
- [ ] Root `requirements.txt` is present and matches the validation environment.
- [ ] All maintained starter notebooks execute from fresh kernels.
- [ ] Classical machine-learning, PyTorch, Optuna, data-generation, metric, and submission-validation scripts pass their smoke tests.
- [ ] CPU/GPU assumptions, memory limits, package versions, and download requirements are recorded.
- [ ] The exact competition submission format can be produced and validated.

Evidence:

- Operating system:
- Python version:
- Dependency lock or environment file:
- Hardware tested:
- Notebook execution record:
- Script smoke-test record:
- Known limitations:

## Gate 4 — Assessment Security

- [ ] The teacher-key repository is private.
- [ ] Only authorized teachers have access.
- [ ] Public history contains no answer keys, hidden labels, private tests, scoring packages, secrets, or restricted data.
- [ ] Formal mocks use hidden or freshly generated evaluation data.
- [ ] Student-facing materials cannot reconstruct protected answers from public files.

Evidence:

- Visibility verified on:
- Authorized reviewers:
- History/security review result:
- Hidden-test storage location:

## Gate 5 — Representative Classroom Pilots

At least one pilot must be completed for each lesson type below:

- [ ] Round 1 concept, calculation, or code-tracing lesson.
- [ ] Tabular Round 2 lesson.
- [ ] Deep-learning or PyTorch lesson.
- [ ] Computer-vision, NLP, audio, or multimodal lesson.
- [ ] Competition-sprint lesson.
- [ ] Timed mock or reproduction.

Each pilot must record actual duration, completion rate, common errors, support required, independent-rebuild success, and required revisions using `Pilot_Lesson_Evidence_Record.md`.

Evidence:

- Cohort and dates:
- Number of students:
- Pilot records reviewed by:
- Revisions completed in commit:

## Gate 6 — Full Pathway Evidence

- [ ] The selected pathway has been delivered to a real cohort.
- [ ] Ordinary lessons fit the declared 75-minute structure or have documented exceptions.
- [ ] The fourteen-session machine-learning video sequence fits the declared 70-minute structure.
- [ ] Phase gates identify students who are ready, need reteaching, or should not advance.
- [ ] Student evidence shows independent rebuilding rather than tutorial copying.

Evidence:

- Cohort dates:
- Sessions delivered:
- Completion and retention data:
- Phase-gate results:
- Major curriculum revisions:

## Gate 7 — Current Competition-Year Alignment

- [ ] Official NOAI rules, stages, registration requirements, scoring, permitted tools, package constraints, model/API policy, hardware/runtime limits, and submission format have been rechecked for the active year.
- [ ] Official IOAI regulations, syllabus, task format, resource policy, and team/selection requirements have been rechecked for the active year.
- [ ] Any uncertainty is explicitly marked instead of being presented as fact.
- [ ] The dated record is completed in `Annual_Competition_Rule_Verification.md`.

Evidence:

- Active competition year:
- Verification date:
- Official sources reviewed:
- Curriculum changes made:

## Gate 8 — Release Decision

A release can be labelled **fully evidenced for the named year and cohort** only when Gates 1–7 are complete and supported by inspectable evidence.

Until then, use dimension-specific language such as:

- structurally complete;
- runtime validated;
- representative pilots complete;
- security verified;
- annual rules verified;
- full-cohort evidence pending.

Never use “100% ready” as a substitute for missing evidence.
