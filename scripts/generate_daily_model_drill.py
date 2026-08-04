from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from manage_student_progress import load_progress, new_progress, record_drill_assignment, save_progress

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "curriculum_spec.json"
HEADING_RE = re.compile(r"^###\s+(?:Day|Scenario)\s+(\d+)\s+[—-]\s+(.+?)\s*$", re.MULTILINE)
LEVEL_RE = re.compile(r"Level_(\d)_")


@dataclass(frozen=True)
class Scenario:
    identifier: str
    level: int
    number: int
    title: str
    body: str
    source: str


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def parse_file(relative: str) -> list[Scenario]:
    path = ROOT / relative
    match = LEVEL_RE.search(path.name)
    if not match:
        raise ValueError(f"Cannot infer level from {relative}")
    level = int(match.group(1))
    text = path.read_text(encoding="utf-8")
    headings = list(HEADING_RE.finditer(text))
    scenarios: list[Scenario] = []
    for index, heading in enumerate(headings):
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        number = int(heading.group(1))
        title = heading.group(2).strip()
        body = text[start:end].strip()
        if not body:
            raise ValueError(f"Empty scenario body in {relative}: {number}")
        scenarios.append(
            Scenario(
                identifier=f"L{level}-D{number:02d}",
                level=level,
                number=number,
                title=title,
                body=body,
                source=relative,
            )
        )
    return scenarios


def load_scenarios(spec: dict) -> list[Scenario]:
    files = spec["model_recognition"]["scenario_files"]
    scenarios = [scenario for relative in files for scenario in parse_file(relative)]
    identifiers = [scenario.identifier for scenario in scenarios]
    if len(identifiers) != len(set(identifiers)):
        duplicates = sorted({item for item in identifiers if identifiers.count(item) > 1})
        raise ValueError(f"Duplicate scenario identifiers: {', '.join(duplicates)}")
    minimum = int(spec["model_recognition"]["minimum_public_scenarios"])
    if len(scenarios) < minimum:
        raise ValueError(f"Scenario bank below minimum: {len(scenarios)} < {minimum}")
    return scenarios


def stable_seed(day: str, level: str, count: int) -> int:
    digest = hashlib.sha256(f"{day}|{level}|{count}".encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big")


def recent_scenario_ids(progress: dict | None, window: int) -> list[str]:
    if progress is None or window <= 0:
        return []
    ordered: list[str] = []
    for record in reversed(progress.get("drill_history", [])):
        for scenario_id in reversed(record.get("scenario_ids", [])):
            if scenario_id not in ordered:
                ordered.append(scenario_id)
            if len(ordered) >= window:
                return ordered
    return ordered


def prioritise_pool(pool: list[Scenario], rng: random.Random, recent_ids: list[str]) -> list[Scenario]:
    recent_position = {identifier: index for index, identifier in enumerate(recent_ids)}
    unseen = [scenario for scenario in pool if scenario.identifier not in recent_position]
    seen = [scenario for scenario in pool if scenario.identifier in recent_position]
    rng.shuffle(unseen)
    # recent_ids is newest first, so larger positions are older and may return first when reuse is unavoidable.
    seen.sort(key=lambda scenario: recent_position[scenario.identifier], reverse=True)
    return unseen + seen


def select_scenarios(
    scenarios: list[Scenario],
    day: str,
    level: str,
    count: int,
    recent_ids: list[str] | None = None,
) -> list[Scenario]:
    if count < 1:
        raise ValueError("--count must be at least 1")
    if count > len(scenarios):
        raise ValueError(f"Requested {count} scenarios but only {len(scenarios)} exist")
    recent_ids = recent_ids or []
    rng = random.Random(stable_seed(day, level, count))

    if level != "mixed":
        requested_level = int(level)
        pool = [scenario for scenario in scenarios if scenario.level == requested_level]
        if count > len(pool):
            raise ValueError(f"Requested {count} scenarios but Level {requested_level} has only {len(pool)}")
        return prioritise_pool(pool, rng, recent_ids)[:count]

    by_level = {
        value: prioritise_pool([scenario for scenario in scenarios if scenario.level == value], rng, recent_ids)
        for value in (1, 2, 3)
    }
    selected: list[Scenario] = []
    start = stable_seed(day, level, count) % 3
    cycle = [1, 2, 3]
    cycle = cycle[start:] + cycle[:start]
    positions = {1: 0, 2: 0, 3: 0}

    while len(selected) < count:
        made_progress = False
        for current_level in cycle:
            position = positions[current_level]
            pool = by_level[current_level]
            if position < len(pool):
                selected.append(pool[position])
                positions[current_level] += 1
                made_progress = True
                if len(selected) == count:
                    break
        if not made_progress:
            raise ValueError(f"Requested {count} scenarios but only {len(scenarios)} are available")
    return selected


def build_set_id(day: str, selected: list[Scenario]) -> str:
    return hashlib.sha256(
        (day + "|" + "|".join(scenario.identifier for scenario in selected)).encode("utf-8")
    ).hexdigest()[:10]


def render(day: str, level: str, selected: list[Scenario], minutes: int, history_window: int) -> str:
    set_id = build_set_id(day, selected)
    lines = [
        "# Daily Model-Recognition Drill",
        "",
        f"- Date: {day}",
        f"- Set ID: `{set_id}`",
        f"- Level: `{level}`",
        f"- Target time: {minutes} minutes",
        f"- Recent-repeat window: {history_window} scenario assignments",
        "- Public answer key: none",
        "",
        "Complete the reasoning fields before naming a model. Record teacher feedback and the correction cause after submission.",
        "",
    ]

    for index, scenario in enumerate(selected, 1):
        lines += [
            f"## {index}. {scenario.identifier} — {scenario.title}",
            "",
            scenario.body,
            "",
            "```text",
            "sample:",
            "X:",
            "y:",
            "labels available during training:",
            "required output:",
            "task family:",
            "simplest valid baseline:",
            "metric and error cost:",
            "validation design:",
            "candidate model family 1 + limitation:",
            "candidate model family 2 + limitation:",
            "leakage / shift / submission risk:",
            "```",
            "",
        ]

    lines += [
        "## End-of-set correction record",
        "",
        "| Scenario | Correct task family | Baseline/metric valid | Main reasoning error | Corrected rule | Recheck date |",
        "|---|---|---|---|---|---|",
    ]
    for scenario in selected:
        lines.append(f"| {scenario.identifier} |  |  |  |  |  |")
    lines += [
        "",
        "Mastery is not awarded from one set. Use the repository mastery rule: at least 90% task-family accuracy for five consecutive daily sets plus a fresh secured confirmation set.",
    ]
    return "\n".join(lines) + "\n"


def run_self_test() -> None:
    spec = load_spec()
    scenarios = load_scenarios(spec)
    assert len(scenarios) >= 36
    first = select_scenarios(scenarios, "2026-08-04", "mixed", 5)
    second = select_scenarios(scenarios, "2026-08-04", "mixed", 5)
    assert first == second
    assert len({scenario.identifier for scenario in first}) == 5
    assert len({scenario.level for scenario in first}) >= 2

    with tempfile.TemporaryDirectory() as folder:
        progress_path = Path(folder) / "progress.json"
        progress = new_progress("student-001", "noai_round1", spec)
        first_id = build_set_id("2026-08-04", first)
        record_drill_assignment(
            progress,
            day="2026-08-04",
            set_id=first_id,
            level="mixed",
            scenario_ids=[scenario.identifier for scenario in first],
        )
        save_progress(progress_path, progress, spec)
        loaded = load_progress(progress_path, spec)
        recent = recent_scenario_ids(loaded, 15)
        next_set = select_scenarios(scenarios, "2026-08-05", "mixed", 5, recent)
        assert not ({scenario.identifier for scenario in first} & {scenario.identifier for scenario in next_set})
        record_drill_assignment(
            loaded,
            day="2026-08-04",
            set_id=first_id,
            level="mixed",
            scenario_ids=[scenario.identifier for scenario in first],
        )
        assert len(loaded["drill_history"]) == 1

    text = render("2026-08-04", "mixed", first, int(spec["model_recognition"]["daily_minutes"]), 15)
    assert "Public answer key: none" in text
    assert "candidate model family 2 + limitation" in text
    assert "Recent-repeat window" in text
    print("Daily model-recognition drill generator self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a deterministic answer-key-free daily model-recognition set.")
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD; controls deterministic selection")
    parser.add_argument("--level", choices=("1", "2", "3", "mixed"), default="mixed")
    parser.add_argument("--count", type=int, help="Number of scenarios; defaults to curriculum_spec.json")
    parser.add_argument("--progress", type=Path, help="Use recent assignments from a student progress ledger")
    parser.add_argument("--history-window", type=int, help="Recent scenario assignments to avoid when possible")
    parser.add_argument("--record-progress", action="store_true", help="Append the assigned set to --progress after output succeeds")
    parser.add_argument("--output", type=Path, help="Write Markdown to this path instead of stdout")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        return 0

    try:
        date.fromisoformat(args.date)
        spec = load_spec()
        scenarios = load_scenarios(spec)
        count = args.count or int(spec["model_recognition"]["daily_set_size"])
        history_window = args.history_window
        if history_window is None:
            history_window = int(spec["model_recognition"].get("recent_repeat_window", 15))
        if history_window < 0:
            raise ValueError("--history-window must be zero or greater")
        if args.record_progress and not args.progress:
            raise ValueError("--record-progress requires --progress")

        progress = load_progress(args.progress, spec) if args.progress else None
        recent = recent_scenario_ids(progress, history_window)
        selected = select_scenarios(scenarios, args.date, args.level, count, recent)
        text = render(
            args.date,
            args.level,
            selected,
            int(spec["model_recognition"]["daily_minutes"]),
            history_window,
        )
        set_id = build_set_id(args.date, selected)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Daily drill generation failed: {error}", file=sys.stderr)
        return 2

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote daily model-recognition drill to {args.output}")
    else:
        print(text, end="")

    if args.record_progress and args.progress and progress is not None:
        record_drill_assignment(
            progress,
            day=args.date,
            set_id=set_id,
            level=args.level,
            scenario_ids=[scenario.identifier for scenario in selected],
        )
        save_progress(args.progress, progress, spec)
        print(f"Recorded drill set {set_id} in {args.progress}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
