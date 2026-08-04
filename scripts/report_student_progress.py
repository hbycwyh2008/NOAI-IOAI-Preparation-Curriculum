"""Generate evidence-bounded progress reports using thresholds from curriculum_spec.json."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

from manage_student_progress import (
    compact_ranges,
    load_progress,
    load_spec,
    new_progress,
    record_drill_assignment,
    save_progress,
    score_drill,
    set_recognition_confirmation,
)


def _is_number(value: object) -> bool:
    return type(value) in (int, float)


def record_is_qualifying(record: dict, task_threshold: float, baseline_threshold: float) -> bool:
    task = record.get("task_family_accuracy")
    baseline = record.get("baseline_metric_accuracy")
    return bool(
        record.get("reviewed")
        and _is_number(task)
        and _is_number(baseline)
        and float(task) >= task_threshold
        and float(baseline) >= baseline_threshold
    )


def analyse_progress(data: dict, spec: dict, as_of: date) -> dict:
    pathway = spec["pathways"][data["pathway"]]
    route = [int(value) for value in pathway["sessions"]]
    completed = set(int(value) for value in data["completed_sessions"])
    red = set(int(value) for value in data["red_sessions"])
    resolved = completed - red
    resolved_on_route = [session for session in route if session in resolved]
    remaining = [session for session in route if session not in resolved]

    recognition = spec["model_recognition"]
    streak_required = int(recognition["mastery_consecutive_days"])
    task_threshold = float(recognition["mastery_minimum_accuracy"])
    baseline_threshold = float(recognition["mastery_minimum_baseline_metric_accuracy"])
    maintenance_required = int(recognition["maintenance_sets_per_week"])

    all_history = list(data["drill_history"])
    history = [record for record in all_history if date.fromisoformat(record["date"]) <= as_of]
    future_records = [record for record in all_history if date.fromisoformat(record["date"]) > as_of]
    reviewed = [record for record in history if record.get("reviewed")]
    pending = [record for record in history if not record.get("reviewed")]
    incomplete_reviewed = [
        record
        for record in reviewed
        if not _is_number(record.get("task_family_accuracy"))
        or not _is_number(record.get("baseline_metric_accuracy"))
    ]

    streak = 0
    streak_records: list[dict] = []
    for record in reversed(reviewed):
        if not record_is_qualifying(record, task_threshold, baseline_threshold):
            break
        streak += 1
        streak_records.append(record)
    streak_records.reverse()

    public_streak_met = streak >= streak_required
    latest_streak_date = date.fromisoformat(streak_records[-1]["date"]) if public_streak_met else None

    confirmation = data["recognition_confirmation"]
    confirmation_recorded = bool(confirmation["passed"])
    confirmation_date = date.fromisoformat(confirmation["date"]) if confirmation_recorded else None
    confirmation_effective = bool(
        confirmation_recorded and confirmation_date is not None and confirmation_date <= as_of
    )
    confirmation_after_streak = bool(
        public_streak_met
        and confirmation_effective
        and latest_streak_date is not None
        and confirmation_date is not None
        and confirmation_date >= latest_streak_date
    )
    mastery_confirmed = public_streak_met and confirmation_after_streak

    if mastery_confirmed:
        recognition_status = "CONFIRMED"
    elif public_streak_met and confirmation_recorded and not confirmation_effective:
        recognition_status = "CONFIRMATION_NOT_YET_EFFECTIVE"
    elif public_streak_met and confirmation_effective and not confirmation_after_streak:
        recognition_status = "CONFIRMATION_OUT_OF_ORDER"
    elif public_streak_met:
        recognition_status = "PUBLIC_STREAK_ELIGIBLE_FOR_SECURED_CONFIRMATION"
    elif reviewed:
        recognition_status = "PUBLIC_STREAK_IN_PROGRESS"
    else:
        recognition_status = "INSUFFICIENT_REVIEWED_EVIDENCE"

    maintenance_window_start = as_of - timedelta(days=6)
    maintenance_sets = [
        record
        for record in reviewed
        if record.get("level") == "mixed"
        and record_is_qualifying(record, task_threshold, baseline_threshold)
        and maintenance_window_start <= date.fromisoformat(record["date"]) <= as_of
        and (confirmation_date is None or date.fromisoformat(record["date"]) >= confirmation_date)
    ]
    maintenance_due = bool(
        mastery_confirmed
        and confirmation_date is not None
        and as_of >= confirmation_date + timedelta(days=7)
        and len(maintenance_sets) < maintenance_required
    )

    required_pathway = pathway.get("requires_pathway")
    entry_qualified = not required_pathway or required_pathway in set(data["qualified_pathways"])

    return {
        "route_length": len(route),
        "resolved_on_route": resolved_on_route,
        "remaining": remaining,
        "completion_percent": 100.0 * len(resolved_on_route) / len(route),
        "red": sorted(red),
        "entry_qualified": entry_qualified,
        "required_pathway": required_pathway,
        "reviewed_count": len(reviewed),
        "pending_count": len(pending),
        "future_record_count": len(future_records),
        "incomplete_reviewed_count": len(incomplete_reviewed),
        "current_streak": streak,
        "streak_required": streak_required,
        "task_threshold": task_threshold,
        "baseline_threshold": baseline_threshold,
        "public_streak_met": public_streak_met,
        "recognition_status": recognition_status,
        "confirmation_recorded": confirmation_recorded,
        "confirmation_effective": confirmation_effective,
        "confirmation_date": confirmation_date,
        "mastery_confirmed": mastery_confirmed,
        "maintenance_sets": len(maintenance_sets),
        "maintenance_required": maintenance_required,
        "maintenance_due": maintenance_due,
        "recent_reviewed": reviewed[-5:],
    }


def render_report(data: dict, spec: dict, as_of: date) -> str:
    analysis = analyse_progress(data, spec, as_of)
    remaining = analysis["remaining"]
    next_sessions = remaining[:6]

    lines = [
        "# Student Progress Report",
        "",
        f"- Student ID: `{data['student_id']}`",
        f"- Pathway: `{data['pathway']}`",
        f"- Ledger schema: `{data['schema_version']}`",
        f"- Report date: `{as_of.isoformat()}`",
        f"- Ledger last updated: `{data['last_updated']}`",
        "",
        "## Pathway Status",
        "",
        f"- Resolved route Sessions: **{len(analysis['resolved_on_route'])}/{analysis['route_length']}** ({analysis['completion_percent']:.1f}%)",
        f"- Unresolved Red debt: **{compact_ranges(analysis['red'])}**",
        f"- Next unresolved Sessions: **{compact_ranges(next_sessions)}**",
    ]

    if analysis["required_pathway"]:
        status = "qualified" if analysis["entry_qualified"] else "blocked"
        lines.append(f"- Entry gate `{analysis['required_pathway']}`: **{status}**")

    lines += [
        "",
        "## Model-Recognition Evidence",
        "",
        f"- Reviewed daily sets through report date: **{analysis['reviewed_count']}**",
        f"- Pending review through report date: **{analysis['pending_count']}**",
        f"- Future-dated ledger records excluded: **{analysis['future_record_count']}**",
        f"- Reviewed legacy/incomplete records: **{analysis['incomplete_reviewed_count']}**",
        f"- Current qualifying streak: **{analysis['current_streak']}/{analysis['streak_required']}**",
        f"- Task-family threshold: **{analysis['task_threshold']:.0%}**",
        f"- Baseline/metric threshold: **{analysis['baseline_threshold']:.0%}**",
        f"- Secured confirmation recorded: **{'yes' if analysis['confirmation_recorded'] else 'no'}**",
        f"- Secured confirmation effective by report date: **{'yes' if analysis['confirmation_effective'] else 'no'}**",
        f"- Recognition status: **{analysis['recognition_status']}**",
        "",
        "A public streak is only eligibility for the private secured confirmation. Future-dated evidence is excluded and cannot establish mastery early.",
        "",
        "### Most Recent Reviewed Sets",
        "",
        "| Date | Set ID | Level | Task family | Baseline/metric | Total score | Qualifying |",
        "|---|---|---|---:|---:|---:|---|",
    ]

    if analysis["recent_reviewed"]:
        for record in analysis["recent_reviewed"]:
            task = record.get("task_family_accuracy")
            baseline = record.get("baseline_metric_accuracy")
            score = record.get("score_percent")
            qualifying = record_is_qualifying(
                record,
                analysis["task_threshold"],
                analysis["baseline_threshold"],
            )
            lines.append(
                "| {date} | `{set_id}` | {level} | {task} | {baseline} | {score} | {qualifying} |".format(
                    date=record["date"],
                    set_id=record["set_id"],
                    level=record["level"],
                    task="—" if task is None else f"{float(task):.0%}",
                    baseline="—" if baseline is None else f"{float(baseline):.0%}",
                    score="—" if score is None else f"{float(score):.1f}%",
                    qualifying="yes" if qualifying else "no",
                )
            )
    else:
        lines.append("| — | — | — | — | — | — | no reviewed evidence |")

    lines += [
        "",
        "## Maintenance",
        "",
        f"- Qualifying mixed sets in the current seven-day window: **{analysis['maintenance_sets']}/{analysis['maintenance_required']}**",
        f"- Maintenance currently due: **{'yes' if analysis['maintenance_due'] else 'no'}**",
        "",
        "## Next Action",
        "",
    ]

    if analysis["future_record_count"]:
        lines.append("1. Verify the report date and future-dated ledger records; they are excluded from current evidence decisions.")
    elif analysis["pending_count"]:
        lines.append("1. Review and score the pending daily set before using it in any mastery decision.")
    elif analysis["red"]:
        lines.append(f"1. Repair and recheck Red prerequisite debt: **{compact_ranges(analysis['red'])}**.")
    elif not analysis["entry_qualified"]:
        lines.append(f"1. Inspect and record qualification for `{analysis['required_pathway']}` before continuation.")
    elif remaining:
        lines.append(f"1. Assign the next unresolved route Sessions: **{compact_ranges(next_sessions)}**.")
    elif not analysis["public_streak_met"]:
        lines.append("1. Continue one reviewed daily set per assigned study day until the five-set public streak is complete.")
    elif analysis["recognition_status"] == "CONFIRMATION_NOT_YET_EFFECTIVE":
        lines.append("1. Do not claim confirmed mastery before the recorded private-confirmation date.")
    elif not analysis["mastery_confirmed"]:
        lines.append("1. Administer a fresh private secured confirmation set after the completed public streak.")
    elif analysis["maintenance_due"]:
        lines.append("1. Assign enough qualifying mixed maintenance sets to reach two in the current seven-day window.")
    else:
        lines.append("1. Preserve spaced maintenance and continue pathway evidence review; no automatic promotion claim is created.")

    lines += [
        "",
        "## Evidence Boundary",
        "",
        "This report evaluates only declared ledger evidence through the report date. It does not inspect private answers, prove classroom delivery, qualify devices or accounts, or establish current-year competition readiness. Teacher inspection remains required before pathway qualification or readiness claims.",
    ]
    return "\n".join(lines) + "\n"


def run_self_test() -> None:
    spec = load_spec()
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "progress.json"
        data = new_progress("student-report-001", "noai_round1", spec)
        for index, day in enumerate(("2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04", "2026-08-05"), 1):
            set_id = f"{index:010x}"
            record_drill_assignment(
                data,
                day=day,
                set_id=set_id,
                level="mixed",
                scenario_ids=[f"L1-D{index:02d}"],
            )
            score_drill(data, set_id, 0.9, 0.9, 90)
        save_progress(path, data, spec)
        loaded = load_progress(path, spec)
        before = analyse_progress(loaded, spec, date(2026, 8, 6))
        assert before["recognition_status"] == "PUBLIC_STREAK_ELIGIBLE_FOR_SECURED_CONFIRMATION"

        set_recognition_confirmation(loaded, "2026-08-06")
        save_progress(path, loaded, spec)
        confirmed = load_progress(path, spec)
        historical = analyse_progress(confirmed, spec, date(2026, 8, 5))
        assert historical["recognition_status"] == "PUBLIC_STREAK_ELIGIBLE_FOR_SECURED_CONFIRMATION"
        assert historical["confirmation_effective"] is False

        after = analyse_progress(confirmed, spec, date(2026, 8, 14))
        assert after["mastery_confirmed"] is True
        assert after["maintenance_due"] is True
        text = render_report(confirmed, spec, date(2026, 8, 14))
        assert "Recognition status: **CONFIRMED**" in text
        assert "Maintenance currently due: **yes**" in text
        assert "private secured confirmation" in text

        future_data = new_progress("student-report-002", "noai_round1", spec)
        record_drill_assignment(
            future_data,
            day="2026-08-10",
            set_id="000000000a",
            level="mixed",
            scenario_ids=["L1-D10"],
        )
        score_drill(future_data, "000000000a", 1.0, 1.0, 100)
        future_analysis = analyse_progress(future_data, spec, date(2026, 8, 9))
        assert future_analysis["reviewed_count"] == 0
        assert future_analysis["future_record_count"] == 1

    print("Student progress report self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an evidence-bounded pathway and model-recognition progress report.")
    parser.add_argument("--progress", type=Path)
    parser.add_argument("--as-of", default=date.today().isoformat(), help="ISO report date")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        return 0
    if not args.progress:
        parser.error("--progress is required unless --self-test is used")

    try:
        as_of = date.fromisoformat(args.as_of)
        spec = load_spec()
        data = load_progress(args.progress, spec)
        text = render_report(data, spec, as_of)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Student progress report failed: {error}", file=sys.stderr)
        return 2

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote student progress report to {args.output}")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
