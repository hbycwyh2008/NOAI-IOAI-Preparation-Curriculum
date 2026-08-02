# Public Repository Readiness Dashboard

This dashboard prevents one percentage from hiding different kinds of readiness.

## Current Dimension Status

| Dimension | Public-repository target | Current claim after validator passes | Evidence source | Can the public repo prove it alone? |
|---|---:|---|---|---|
| Canonical pathway and navigation | 100% | structurally complete | `02_Class_Missions/README.md`, course map, pacing guide | yes |
| Class Missions click path | 100% | nine Phase launchers cover Sessions 1–78 exactly once and link to exact lessons | `HOW_TO_USE_CLASS_MISSIONS.md`, Phase launchers, launcher validator | yes |
| Scheduled-phase teacher guidance | 100% | complete when every phase has a delivery entry and gate | Phase READMEs, launchers, and Ready-to-Teach pack | yes |
| Student-facing lesson/resource bank | 100% | 155 mainline + 16 Bohrium resource lessons | lesson-distribution audit | yes |
| Phase 04 reading curriculum | 100% | eight English seminars, teacher pack, evidence template, and rubric | Phase 04 folder and linked artifacts | yes |
| Andrew ML mathematics transition | 100% | Sessions 41–43 bridge, just-in-time map, teacher pack, evidence template, and rubric | Phase 05 folder and linked artifacts | yes |
| Internal links, counts, naming, and source boundaries | 100% | complete when strict validators pass | three public validators | yes |
| Maintained notebooks and starter code | 100% of maintained assets | complete when release workflow passes | Ready-to-Teach workflow output | yes, for CI environment |
| Required public links | 100% HTTP reachability | complete when link checker passes | link-check workflow output | partly; authenticated access needs manual evidence |
| Student runtime qualification | cohort-specific | pending until exact environment is tested | `Student_Runtime_Qualification_Record.md` | no |
| Authenticated course access | cohort-specific | pending until student/teacher accounts are tested | `External_Access_Verification_Record.md` | no |
| Assessment security | deployment-specific | pending until private teacher repository is inspected | teacher-key manifest and release gates | no |
| Representative classroom pilots | cohort-specific | pending until real students produce evidence | representative pilot matrix and reports | no |
| Full-pathway classroom evidence | cohort-specific | pending until a real cohort completes the selected path | versioned pilot reports | no |
| Current competition-year alignment | year-specific | pending until official rules are rechecked | annual-rule verification record | no |

## Allowed Claims

When automated checks pass, the repository may state:

> **100% public file-structure and internal-consistency coverage for the maintained curriculum assets.**

The launcher validator additionally establishes complete scheduled-session navigation coverage:

> **Nine Phase launchers cover Sessions 1–78 exactly once and resolve to valid lesson files.**

It may also state, separately, which maintained notebooks, scripts, and links passed on the release commit.

It must not state “100% operationally ready” unless the named cohort, runtime, authenticated resources, private assessment system, representative pilots, full pathway, and current competition-year rules have all passed their separate release gates.

## Public-Repository Completion Checklist

- [ ] all overview documents use the 78-session pathway;
- [ ] Class Missions has one documented normal path: Phase → Session Launcher → exact lesson;
- [ ] nine launchers cover Sessions 1–78 exactly once;
- [ ] every launcher’s internal lesson links resolve;
- [ ] Phase READMEs expose the launcher as the primary entry point;
- [ ] normal delivery does not require manual `_Lesson_Library` browsing;
- [ ] Phase 04 is AI History and Thinking Humans, not a standalone Kaggle phase;
- [ ] Kaggle is documented as embedded Andrew ML practice;
- [ ] Andrew ML has an explicit mathematics transition and model-by-model mathematics evidence;
- [ ] every scheduled phase has purpose, prerequisites, sequence, evidence, and gate;
- [ ] Phase 04 has eight complete lesson files, a teacher pack, student evidence template, and rubric;
- [ ] all 155 mainline and 16 Bohrium resource lessons are indexed;
- [ ] internal links and selected-content paths resolve;
- [ ] the validators require the current source-of-truth files;
- [ ] Ready-to-Teach automation executes maintained notebooks and starter code;
- [ ] required public links pass the blocking link check;
- [ ] public/private assessment boundaries are explicit;
- [ ] release, runtime, access, pilot, annual-rule, and security records exist;
- [ ] stale pathway counts and obsolete phase labels are rejected by validation.

## External Evidence Still Required

Use these records rather than changing the public-completeness percentage:

- [Release Readiness Gates](Release_Readiness_Gates.md)
- [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](External_Access_Verification_Record.md)
- [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md)
- [Representative Pilot Matrix](../09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md)
- [Annual Competition Rule Verification](Annual_Competition_Rule_Verification.md)

## Release Rule

A release note must name the exact commit and report each dimension separately. Missing real-world evidence is recorded as **pending**, not converted into a guessed percentage.