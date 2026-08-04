from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "curriculum_spec.json"


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def parse_sessions(value: str) -> set[int]:
    sessions: set[int] = set()
    value = value.strip()
    if not value:
        return sessions
    for token in value.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_text, end_text = token.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            if start > end:
                raise ValueError(f"Invalid descending range: {token}")
            sessions.update(range(start, end + 1))
        else:
            sessions.add(int(token))
    return sessions


def compact_ranges(values: Iterable[int]) -> str:
    ordered = sorted(set(values))
    if not ordered:
        return "none"
    ranges: list[str] = []
    start = previous = ordered[0]
    for value in ordered[1:]:
        if value == previous + 1:
            previous = value
            continue
        ranges.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = value
    ranges.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(ranges)


def pathway_sessions(spec: dict, pathway_name: str) -> list[int]:
    pathways = spec.get("pathways", {})
    if pathway_name not in pathways:
        choices = ", ".join(sorted(pathways))
        raise ValueError(f"Unknown pathway '{pathway_name}'. Choose one of: {choices}")
    return [int(value) for value in pathways[pathway_name]["sessions"]]


def build_plan(
    spec: dict,
    pathway_name: str,
    completed: set[int],
    red: set[int],
    limit: int,
    entry_qualified: bool,
) -> str:
    pathway = spec["pathways"][pathway_name]
    route = pathway_sessions(spec, pathway_name)
    canonical = set(range(1, int(spec["canonical_sessions"]) + 1))

    invalid = (completed | red) - canonical
    if invalid:
        raise ValueError(f"Sessions outside the canonical range: {compact_ranges(invalid)}")
    if limit < 1:
        raise ValueError("--limit must be at least 1")

    required_pathway = pathway.get("requires_pathway")
    entry_blocker = bool(required_pathway and not entry_qualified)

    route_set = set(route)
    completed_on_route = completed & route_set
    red_on_route = red & route_set
    remaining = [session for session in route if session not in completed_on_route or session in red_on_route]

    if red_on_route:
        red_in_order = [session for session in route if session in red_on_route]
        first_red_index = route.index(red_in_order[0])
        before_or_at_blocker = [
            session
            for session in route[: first_red_index + 1]
            if session not in completed_on_route or session in red_on_route
        ]
        recommendations = (red_in_order + before_or_at_blocker)[:limit]
        recommendations = list(dict.fromkeys(recommendations))
    elif entry_blocker:
        recommendations = []
    else:
        recommendations = remaining[:limit]

    checkpoints = [
        item
        for item in spec.get("workflow_checkpoints", [])
        if int(item["session"]) in route_set and int(item["session"]) not in completed_on_route
    ]
    next_checkpoint = checkpoints[0] if checkpoints else None

    lines = [
        "# Learning Path Plan",
        "",
        f"- Pathway: `{pathway_name}`",
        f"- Pathway document: `{pathway['document']}`",
        f"- Route length: {len(route)} Sessions",
        f"- Completed on route: {len(completed_on_route)}",
        f"- Remaining on route: {len(remaining)}",
        f"- Capability boundary: {pathway['claim_boundary']}",
        "",
    ]

    if entry_blocker:
        lines += [
            "## Entry blocker",
            "",
            f"This route requires qualification through `{required_pathway}` or equivalent inspected evidence.",
            "Run again with `--entry-qualified` only after that evidence has been reviewed.",
            "",
        ]

    lines += ["## Prerequisite debt", ""]
    if red_on_route:
        lines.append(f"Blocking Red Sessions: **{compact_ranges(red_on_route)}**.")
        lines.append("Dependent advancement remains conditional until a delayed recheck passes.")
    else:
        lines.append("No Red prerequisite debt was supplied for this plan.")
    lines.append("")

    lines += ["## Next assigned Sessions", ""]
    if recommendations:
        for position, session in enumerate(recommendations, 1):
            reason = "repair and delayed recheck" if session in red_on_route else "next unresolved route Session"
            lines.append(f"{position}. **Session {session}** — {reason}")
    elif not remaining and not entry_blocker:
        lines.append("The declared pathway Sessions are complete. Use the exit gate and capability boundary before making a readiness claim.")
    else:
        lines.append("No Session should be assigned until the entry blocker is resolved.")
    lines.append("")

    lines += ["## Next workflow checkpoint", ""]
    if next_checkpoint:
        lines.append(f"Session **{next_checkpoint['session']}** — `{next_checkpoint['gate']}`")
    else:
        lines.append("No unresolved checkpoint remains on this pathway.")
    lines.append("")

    recovery = pathway.get("recovery_sessions") or []
    if recovery:
        unresolved_recovery = [session for session in recovery if session not in completed]
        lines += ["## Required bridge recovery", ""]
        if unresolved_recovery:
            lines.append(f"Complete before the main continuation: **{compact_ranges(unresolved_recovery)}**.")
        else:
            lines.append("All declared bridge-recovery Sessions are complete.")
        lines.append("")

    lines += [
        "## Evidence rule",
        "",
        "A Session is complete only when its named evidence is accessible and the student can reconstruct or explain the central pattern. Running code once or marking a video complete does not remove prerequisite debt.",
    ]
    return "\n".join(lines) + "\n"


def run_self_test() -> None:
    spec = load_spec()
    round1 = set(pathway_sessions(spec, "noai_round1"))

    plan = build_plan(spec, "noai_round1", set(), set(), 3, False)
    assert "Session 1" in plan and "Session 3" in plan

    plan = build_plan(spec, "noai_round2", round1, set(), 4, True)
    assert "Session 32" in plan and "Session 47" in plan and "Session 59" in plan

    plan = build_plan(spec, "ioai_full", round1, {19}, 4, True)
    assert "Blocking Red Sessions: **19**" in plan

    try:
        parse_sessions("8-3")
    except ValueError:
        pass
    else:
        raise AssertionError("Descending ranges must fail")

    print("Learning-path planner self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an evidence-aware next-Session plan from curriculum_spec.json.")
    parser.add_argument("--pathway", choices=("noai_round1", "noai_round2", "ioai_full"))
    parser.add_argument("--completed", default="", help="Completed Sessions, for example 1-18,24-31")
    parser.add_argument("--completed-pathway", choices=("noai_round1", "noai_round2", "ioai_full"))
    parser.add_argument("--red", default="", help="Blocking Red Sessions")
    parser.add_argument("--limit", type=int, default=6, help="Maximum number of next Sessions")
    parser.add_argument("--entry-qualified", action="store_true", help="Confirm that a required earlier pathway has inspected evidence")
    parser.add_argument("--output", type=Path, help="Write Markdown to this path instead of stdout")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        return 0
    if not args.pathway:
        parser.error("--pathway is required unless --self-test is used")

    try:
        spec = load_spec()
        completed = parse_sessions(args.completed)
        if args.completed_pathway:
            completed.update(pathway_sessions(spec, args.completed_pathway))
        red = parse_sessions(args.red)
        text = build_plan(spec, args.pathway, completed, red, args.limit, args.entry_qualified)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Pathway planner failed: {error}", file=sys.stderr)
        return 2

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote learning path plan to {args.output}")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
