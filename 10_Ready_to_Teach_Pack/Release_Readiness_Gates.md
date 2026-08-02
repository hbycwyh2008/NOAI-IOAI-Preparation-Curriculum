# Release Readiness Gates

This document defines the evidence required before the curriculum may be described as fully evidenced for a specific competition year, runtime, and student cohort.

A percentage must never combine structural completeness with unverified classroom, runtime, security, access, or annual-rule claims.

## Gate 1 — Public Repository Structure

- [ ] `python scripts/validate_curriculum_structure.py` passes on the release commit.
- [ ] `python scripts/validate_readiness_contract.py` passes on the release commit.
- [ ] Required lesson counts, the 78-session pathway, source-of-truth rules, and internal links are consistent.
- [ ] Phase 04 contains eight complete English seminars plus its teacher pack, evidence template, and rubric.
- [ ] No obsolete generator or standalone Kaggle Phase 04 can overwrite or confuse maintained content.

Evidence:

- Release commit SHA:
- Validation date:
- Validator output or workflow URL:
- Reviewer:

## Gate 2 — External Links, Authenticated Resources, and Reading Access

- [ ] `python scripts/check_required_links.py` passes.
- [ ] CS50P, Bohrium, Kaggle, Coursera, StatQuest, 3Blue1Brown, PyTorch, and other assigned resources have been opened using intended teacher and student accounts.
- [ ] Exact modules, videos, chapters, and timestamps still match lesson assignments.
- [ ] Every student has legal access to Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans* before Session 33.
- [ ] Caption, language, regional, payment, enrolment, and school-network constraints have a verified solution.
- [ ] `External_Access_Verification_Record.md` is complete for the cohort.

Evidence:

- Verification date:
- Account types tested:
- Region/network tested:
- Broken or changed resources:
- Replacement or offline mapping:

## Gate 3 — Student Runtime

- [ ] A clean student environment can be installed from documented instructions.
- [ ] Root `requirements.txt` is present and matches the maintained validation environment.
- [ ] All maintained starter notebooks execute from fresh kernels.
- [ ] Classical machine-learning, PyTorch, Optuna, data-generation, metric, and submission-validation scripts pass smoke tests.
- [ ] CPU/GPU assumptions, memory limits, package versions, storage, downloads, and school-network restrictions are recorded.
- [ ] The exact competition submission format can be produced and validated.
- [ ] `Student_Runtime_Qualification_Record.md` is complete for the exact cohort environment.

Evidence:

- Operating system and platform:
- Python and dependency versions:
- Hardware tested:
- Notebook execution record:
- Script smoke-test record:
- Known limitations and workarounds:

## Gate 4 — Assessment Security

- [ ] The teacher-key repository is private.
- [ ] Only authorised teachers have access.
- [ ] Public history contains no answer keys, hidden labels, private tests, scoring packages, secrets, or restricted data.
- [ ] Formal mocks use hidden or freshly generated evaluation data.
- [ ] Student-facing materials cannot reconstruct protected answers from public files.
- [ ] Public rubrics do not reveal protected calibration examples or secure scoring logic.

Evidence:

- Visibility verified on:
- Authorised reviewers:
- History/security review result:
- Hidden-test storage location:

## Gate 5 — Representative Classroom Pilots

Complete every row in `09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md`, including:

- [ ] orientation/evidence workflow;
- [ ] CS50P Python;
- [ ] NumPy/Pandas/visualisation;
- [ ] early and late Bohrium foundation lessons;
- [ ] one AI History reading seminar from Sessions 33–40;
- [ ] regression/classification and tree/unsupervised Andrew ML labs;
- [ ] one full PyTorch training-loop lesson;
- [ ] one computer-vision, NLP, audio, or multimodal lesson;
- [ ] evaluation and tuning lessons;
- [ ] full competition simulation or equivalent timed reproduction.

Each pilot records actual duration, entry accuracy, guided and independent completion, common errors, technical failures, language/access support, teacher intervention, exit evidence, and required revisions.

Evidence:

- Cohort and dates:
- Number of students:
- Pilot records reviewed by:
- Revisions completed in commit:

## Gate 6 — Phase 04 Reading Qualification

- [ ] Students can complete the assigned reading workload before each seminar.
- [ ] English-language support does not replace the evidence and reasoning goals.
- [ ] At least 70% of pilot students pass representative entry checks.
- [ ] At least 50% independently reconstruct the required artifact within the seminar.
- [ ] Students distinguish author claim, textual evidence, supported conclusion, and personal judgement.
- [ ] The public phase rubric produces consistent teacher decisions.
- [ ] The final Thinking Human’s AI Brief gate identifies ready, reteach, and not-yet-ready students.

Evidence:

- Sessions piloted:
- Reading completion rate:
- Entry-check accuracy:
- Independent-rebuild completion:
- Rubric calibration notes stored privately:
- Revisions:

## Gate 7 — Full Pathway Evidence

- [ ] The selected pathway has been delivered to a real cohort.
- [ ] Ordinary lessons fit the declared 75-minute structure or have documented exceptions.
- [ ] The fourteen-session Bohrium sequence and eight-session AI History sequence fit their declared 70-minute structures.
- [ ] Phase gates identify students who are ready, need reteaching, or should not advance.
- [ ] Student evidence shows independent rebuilding rather than tutorial copying.
- [ ] Retention and transfer are checked after the initial phase gate.

Evidence:

- Cohort dates:
- Sessions delivered:
- Completion, retention, and transfer data:
- Phase-gate results:
- Major curriculum revisions:

## Gate 8 — Current Competition-Year Alignment

- [ ] Official NOAI rules, stages, registration requirements, scoring, permitted tools, package constraints, model/API policy, hardware/runtime limits, and submission format have been rechecked for the active year.
- [ ] Official IOAI regulations, syllabus, task format, resource policy, and team/selection requirements have been rechecked for the active year.
- [ ] Any uncertainty is explicitly marked rather than presented as fact.
- [ ] The dated record is completed in `Annual_Competition_Rule_Verification.md`.

Evidence:

- Active competition year:
- Verification date:
- Official sources reviewed:
- Curriculum changes made:

## Gate 9 — Release Decision

A release can be labelled **fully evidenced for the named year, cohort, runtime, and account environment** only when Gates 1–8 are complete and supported by inspectable evidence.

Until then, use dimension-specific language such as:

- 100% public file-structure and internal-consistency coverage;
- maintained assets pass CI runtime checks;
- exact student runtime qualified;
- authenticated access verified;
- representative pilots complete;
- assessment security verified;
- annual rules verified;
- full-cohort evidence pending.

Never use “100% ready” as a substitute for missing real-world evidence.
