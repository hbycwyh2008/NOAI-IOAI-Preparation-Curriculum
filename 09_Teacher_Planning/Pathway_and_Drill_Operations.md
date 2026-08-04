# Pathway and Daily-Drill Operations

This guide turns the pathway documents and mastery records into repeatable teacher actions. The scripts produce planning artifacts; they do not award mastery or replace inspection of student evidence.

## 1. Select the Declared Pathway

Choose exactly one current route:

- `noai_round1` — 45 scheduled Sessions plus daily model-recognition practice;
- `noai_round2` — 22 additional Sessions after inspected Round 1 qualification;
- `ioai_full` — Sessions 1–78, including every recovery Session omitted by a compressed route.

Do not combine pathway claims. A student may complete a compressed route without completing the full canonical route.

## 2. Generate the Next-Session Plan

### Round 1 from the beginning

```bash
python scripts/plan_learning_path.py \
  --pathway noai_round1 \
  --limit 6
```

### Round 1 with completed work and prerequisite debt

```bash
python scripts/plan_learning_path.py \
  --pathway noai_round1 \
  --completed 1-18,24-31 \
  --red 17,25 \
  --limit 5
```

Red Sessions appear first and block dependent advancement. Remove a Red Session only after delayed retrieval or changed-task evidence passes.

### Round 2 after inspected Round 1 qualification

```bash
python scripts/plan_learning_path.py \
  --pathway noai_round2 \
  --completed-pathway noai_round1 \
  --entry-qualified \
  --limit 6
```

The first recommendations should be the deferred bridge Sessions 32 and 47, followed by Session 59.

### IOAI transition from compressed Round 1

```bash
python scripts/plan_learning_path.py \
  --pathway ioai_full \
  --completed-pathway noai_round1 \
  --limit 15
```

The planner exposes every omitted Session from 1–58 before moving into Session 59. Do not manually jump to deep learning and hide the recovery debt.

## 3. Generate the Daily Model-Recognition Set

```bash
python scripts/generate_daily_model_drill.py \
  --date 2026-08-04 \
  --level mixed \
  --output daily-drills/2026-08-04.md
```

- the same date, level, and count produce the same set;
- `mixed` balances levels rather than drawing only easy cases;
- the output contains no answer key;
- every scenario requires task, baseline, metric, validation, model-family, limitation, and leakage/shift reasoning.

Use `--level 1`, `--level 2`, or `--level 3` when a cohort needs targeted difficulty.

## 4. Review and Record

For every generated set:

1. score the public answer fields;
2. compare with the private teacher key and acceptable alternatives;
3. record the reasoning error, not only the corrected category;
4. set a recheck date;
5. update the student mastery dashboard;
6. return to daily practice after two task-family errors in one week.

A deterministic set ID prevents accidental substitution of an easier set after feedback.

## 5. Weekly Planning Cycle

```text
export current mastery evidence
→ run the pathway planner
→ resolve Red prerequisite debt
→ generate daily recognition sets
→ inspect reconstruction and transfer
→ update next Sessions and recheck dates
```

The teacher may override a generated recommendation only with a written reason tied to current evidence, official rules, access, runtime, or scheduling constraints.

## 6. Validation and Troubleshooting

Run:

```bash
python scripts/validate_curriculum_spec.py
python scripts/plan_learning_path.py --self-test
python scripts/generate_daily_model_drill.py --self-test
```

Common errors:

- **entry blocker:** the prior pathway has not been marked as inspected evidence;
- **Session outside range:** a completed or Red value is not between 1 and 78;
- **descending range:** use `3-12`, not `12-3`;
- **scenario bank below minimum:** one or more Level files are missing or headings were changed;
- **document/spec mismatch:** an Exact Session Route table drifted from `curriculum_spec.json`.

## 7. Evidence Boundary

These tools establish route consistency and produce repeatable assignments. They do not establish student-device qualification, authenticated resource access, private assessment security, representative pilot success, current-year rule alignment, or full competition readiness.
