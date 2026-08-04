# Pathway and Daily-Drill Operations

This guide turns pathway documents, mastery evidence, and daily recognition practice into repeatable teacher actions. The scripts produce planning and eligibility records; they do not replace inspection of student evidence.

## 1. Create One Pseudonymous Progress Ledger

Create one ledger in the student’s private course repository. Use a pseudonymous ID, never a name or email address.

```bash
python scripts/manage_student_progress.py init \
  --path student-progress/student-001.json \
  --student-id student-001 \
  --pathway noai_round1
```

The ledger stores:

- current pathway;
- completed Session attempts;
- blocking Red Sessions;
- inspected pathway qualifications;
- one daily drill assignment per date;
- task-family and baseline/metric accuracy;
- total score percentage;
- whether and when a fresh private secured recognition set passed.

The contract is defined by `student_progress.schema.json`; `03_Templates/Student_Progress.example.json` is structural only and must not be reused as a real record.

### Migrate a Schema-v1 Ledger

```bash
python scripts/manage_student_progress.py migrate \
  --path student-progress/student-001.json
```

Migration preserves earlier assignment and score history, adds `baseline_metric_accuracy: null`, and adds an unpassed recognition-confirmation record. Legacy reviewed sets with a missing baseline/metric value remain visible but cannot count toward the new eligibility streak until properly rescored.

## 2. Update Evidence State

Record completed attempts and unresolved prerequisite debt:

```bash
python scripts/manage_student_progress.py update \
  --path student-progress/student-001.json \
  --complete 1-18,24-31 \
  --mark-red 17,25
```

After a delayed recheck passes:

```bash
python scripts/manage_student_progress.py update \
  --path student-progress/student-001.json \
  --clear-red 17
```

When an exit gate has been inspected and passed:

```bash
python scripts/manage_student_progress.py update \
  --path student-progress/student-001.json \
  --qualify noai_round1 \
  --pathway noai_round2
```

A Red Session remains a completed attempt but blocks dependent advancement. Do not clear Red debt from attendance, video completion, or immediate imitation.

## 3. Generate the Next-Session Plan

Use the ledger instead of repeatedly typing completed and Red Session lists:

```bash
python scripts/plan_learning_path.py \
  --progress student-progress/student-001.json \
  --limit 6 \
  --output plans/student-001-next.md
```

To inspect a future transition before changing the stored pathway:

```bash
python scripts/plan_learning_path.py \
  --progress student-progress/student-001.json \
  --pathway ioai_full \
  --limit 15
```

The planner reports entry blockers, Red debt, route recovery, next Sessions, and the next workflow checkpoint. A teacher override requires a written evidence-based reason.

## 4. Generate One Daily Drill

```bash
python scripts/generate_daily_model_drill.py \
  --date 2026-08-04 \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/student-001/2026-08-04.md
```

The generator:

- produces the same recorded set whenever the same date is rerun;
- refuses a second different assignment on the same date;
- balances Level 1–3 when `mixed` is selected;
- avoids the most recent 15 assigned scenario IDs when possible;
- reintroduces the oldest previously seen item first only when reuse is unavoidable;
- records only the Set ID and scenario IDs;
- never includes a public answer key.

Use `--history-window 0` only for a deliberate unrestricted diagnostic. Use `--level 1`, `--level 2`, or `--level 3` for targeted remediation.

## 5. Review and Score the Set

After teacher review, record both required accuracy dimensions:

```bash
python scripts/manage_student_progress.py score-drill \
  --path student-progress/student-001.json \
  --set-id 0123456789 \
  --task-family-accuracy 0.8 \
  --baseline-metric-accuracy 0.9 \
  --score-percent 75
```

- task-family accuracy uses 0–1;
- baseline/metric accuracy uses 0–1;
- total score uses 0–100.

A set counts toward public mastery eligibility only when both accuracy dimensions are at least 90%. Total score remains diagnostic and does not replace either threshold.

## 6. Generate the Mastery-Eligibility Report

```bash
python scripts/report_student_progress.py \
  --progress student-progress/student-001.json \
  --as-of 2026-08-04 \
  --output reports/student-001-progress.md
```

The report distinguishes:

- insufficient reviewed evidence;
- public streak in progress;
- five qualifying reviewed sets completed;
- private secured confirmation still required;
- confirmation recorded before the qualifying streak and therefore invalid;
- recognition mastery confirmed;
- two-set weekly maintenance due.

The report also shows route completion, Red debt, pending review, incomplete legacy records, and the next operational action. It never reads protected answer content.

## 7. Record the Private Secured Confirmation

Only after the five-set public streak is complete, administer a fresh private secured mixed set. If it passes, record only the result and date:

```bash
python scripts/manage_student_progress.py confirm-recognition \
  --path student-progress/student-001.json \
  --date 2026-08-10
```

Do not store the secured questions, hidden labels, detailed key, or protected answers in the ledger. If the confirmation was entered incorrectly or later invalidated:

```bash
python scripts/manage_student_progress.py clear-recognition-confirmation \
  --path student-progress/student-001.json
```

A confirmation dated before the latest qualifying public set does not confirm mastery.

## 8. Maintenance Rule

After confirmed mastery, assign two qualifying mixed sets per seven-day window. The report marks maintenance as due after the first full week when fewer than two qualifying mixed sets appear in the current window.

Maintenance does not erase Red Session debt, replace pathway gates, or establish competition readiness.

## 9. Weekly Operating Cycle

```text
inspect evidence
→ update the private progress ledger
→ generate the progress report
→ run the pathway planner
→ resolve Red prerequisite debt
→ generate one daily recognition set
→ score both accuracy dimensions
→ administer secured confirmation only after eligibility
→ maintain two mixed sets per week after confirmation
```

Do not place real names, email addresses, private answers, hidden labels, credentials, or protected assessment material in the public curriculum repository.

## 10. Validation and Troubleshooting

Run:

```bash
python scripts/validate_curriculum_spec.py
python scripts/manage_student_progress.py --self-test
python scripts/report_student_progress.py --self-test
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/manage_student_progress.py validate \
  --path student-progress/student-001.json
```

Common errors:

- **schema version:** run `manage_student_progress.py migrate` for a v1 ledger;
- **invalid progress ledger:** a required field, date, Set ID, pathway, or Session value is malformed;
- **Red not completed:** every Red Session must also be recorded as a completed attempt;
- **duplicate daily assignment:** the ledger already has a drill for that date; rerun the recorded assignment instead;
- **entry blocker:** the required earlier pathway is not listed under `qualified_pathways`;
- **score range:** both accuracy fields use 0–1; total score uses 0–100;
- **incomplete reviewed record:** a migrated legacy record lacks baseline/metric accuracy and cannot count toward the streak;
- **confirmation out of order:** the secured confirmation date precedes the completed public streak;
- **document/spec mismatch:** an Exact Session Route table drifted from `curriculum_spec.json`.

## 11. Evidence Boundary

These tools establish route consistency, preserve assignment history, calculate eligibility, and produce repeatable next actions. They do not establish student-device qualification, authenticated resource access, private assessment security, representative pilot success, current-year rule alignment, or full competition readiness.
