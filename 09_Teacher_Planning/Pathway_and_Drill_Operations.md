# Pathway and Daily-Drill Operations

This guide turns pathway documents, mastery evidence, and daily recognition practice into repeatable teacher actions. The scripts produce planning records; they do not award mastery or replace inspection of student evidence.

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
- assigned drill Set IDs and scenario history;
- reviewed drill scores.

The contract is defined by `student_progress.schema.json`; `03_Templates/Student_Progress.example.json` is an example only and must not be reused as a real student record.

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

The planner reports entry blockers, Red debt, route recovery, the next unresolved Sessions, and the next workflow checkpoint. A teacher override requires a written evidence-based reason.

## 4. Generate a No-Recent-Repeat Daily Drill

```bash
python scripts/generate_daily_model_drill.py \
  --date 2026-08-04 \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/student-001/2026-08-04.md
```

The generator:

- produces the same set for the same date, level, count, and history state;
- balances Level 1–3 when `mixed` is selected;
- avoids the most recent 15 assigned scenario IDs when possible;
- reintroduces the oldest previously seen item first only when the pool is insufficient;
- records the assigned Set ID and scenarios only when `--record-progress` is used;
- never includes a public answer key.

Use `--history-window 0` only for a deliberate unrestricted diagnostic. Use `--level 1`, `--level 2`, or `--level 3` for targeted remediation.

## 5. Review and Score the Set

After teacher review, record two values from 0 to 1:

```bash
python scripts/manage_student_progress.py score-drill \
  --path student-progress/student-001.json \
  --set-id 0123456789 \
  --task-family-accuracy 0.8 \
  --score-percent 0.75
```

The public worksheet still carries the detailed correction record. The ledger stores only compact assignment and score metadata; protected solutions and calibration examples remain private.

## 6. Weekly Operating Cycle

```text
inspect evidence
→ update the progress ledger
→ run the pathway planner
→ resolve Red prerequisite debt
→ generate and record daily drills
→ score reviewed sets
→ inspect reconstruction and transfer
→ schedule delayed rechecks
```

Do not place real names, email addresses, private answers, hidden labels, credentials, or protected assessment material in the public curriculum repository.

## 7. Validation and Troubleshooting

Run:

```bash
python scripts/validate_curriculum_spec.py
python scripts/manage_student_progress.py --self-test
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
python scripts/manage_student_progress.py validate \
  --path student-progress/student-001.json
```

Common errors:

- **invalid progress ledger:** a required field, date, Set ID, pathway, or Session value is malformed;
- **Red not completed:** every Red Session must also be recorded as a completed attempt;
- **entry blocker:** the required earlier pathway is not listed under `qualified_pathways`;
- **Session outside range:** a completed or Red value is not between 1 and 78;
- **descending range:** use `3-12`, not `12-3`;
- **record-progress requires progress:** assignment history cannot be written without a ledger;
- **document/spec mismatch:** an Exact Session Route table drifted from `curriculum_spec.json`.

## 8. Evidence Boundary

These tools establish route consistency, preserve assignment history, and produce repeatable next actions. They do not establish student-device qualification, authenticated resource access, private assessment security, representative pilot success, current-year rule alignment, or full competition readiness.
