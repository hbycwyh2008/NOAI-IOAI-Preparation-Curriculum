from __future__ import annotations

import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = (MISSIONS / "_Lesson_Library").resolve()
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SESSION_ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")


def split_target(raw: str) -> tuple[str, str]:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        raw = raw[1 : raw.index(">")] + raw[raw.index(">") + 1 :]
    path, marker, anchor = raw.partition("#")
    return path.strip(), (f"#{anchor}" if marker else "")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def slugify(text: str) -> str:
    text = re.sub(r"[`*_]", "", text.lower())
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if not text:
        text = "lesson"
    return text[:72].rstrip("-")


def relative_target(target: Path, start: Path) -> str:
    return os.path.relpath(target, start=start).replace(os.sep, "/")


def choose_destination(entries: list[dict[str, object]], preferred_parent: Path | None) -> Path:
    if preferred_parent is not None:
        for entry in entries:
            destination = entry["destination"]
            assert isinstance(destination, Path)
            if destination.parent == preferred_parent:
                return destination
    ordered = sorted(entries, key=lambda item: int(item["session"]))
    destination = ordered[0]["destination"]
    assert isinstance(destination, Path)
    return destination


def rewrite_links_for_copy(
    text: str,
    source_file: Path,
    destination_file: Path,
    source_to_entries: dict[Path, list[dict[str, object]]],
) -> str:
    def replace(match: re.Match[str]) -> str:
        label, raw_target = match.groups()
        if is_external(raw_target):
            return match.group(0)
        path_part, anchor = split_target(raw_target)
        if not path_part:
            return match.group(0)
        resolved = (source_file.parent / path_part).resolve()
        if resolved in source_to_entries:
            new_target_path = choose_destination(
                source_to_entries[resolved], destination_file.parent
            )
        else:
            new_target_path = resolved
        new_target = relative_target(new_target_path, destination_file.parent) + anchor
        return f"[{label}]({new_target})"

    return LINK_RE.sub(replace, text)


def rewrite_links_in_existing_file(
    text: str,
    current_file: Path,
    source_to_entries: dict[Path, list[dict[str, object]]],
) -> str:
    def replace(match: re.Match[str]) -> str:
        label, raw_target = match.groups()
        if is_external(raw_target):
            return match.group(0)
        path_part, anchor = split_target(raw_target)
        if not path_part:
            return match.group(0)
        resolved = (current_file.parent / path_part).resolve()
        if resolved not in source_to_entries:
            return match.group(0)
        new_target_path = choose_destination(
            source_to_entries[resolved], current_file.parent
        )
        new_target = relative_target(new_target_path, current_file.parent) + anchor
        return f"[{label}]({new_target})"

    return LINK_RE.sub(replace, text)


def collect_entries() -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    used_destinations: set[Path] = set()

    phase_dirs = sorted(
        path
        for path in MISSIONS.iterdir()
        if path.is_dir() and re.match(r"^\d{2}_", path.name)
    )

    for phase_dir in phase_dirs:
        launcher = phase_dir / "SESSION_LAUNCHER.md"
        if not launcher.exists():
            continue
        for line in launcher.read_text(encoding="utf-8").splitlines():
            session_match = SESSION_ROW_RE.match(line)
            if not session_match:
                continue
            session = int(session_match.group(1))
            seen_sources_for_session: set[Path] = set()
            for link_match in LINK_RE.finditer(line):
                label, raw_target = link_match.groups()
                if is_external(raw_target):
                    continue
                path_part, _anchor = split_target(raw_target)
                if not path_part:
                    continue
                source = (launcher.parent / path_part).resolve()
                try:
                    source.relative_to(LIBRARY)
                except ValueError:
                    continue
                if source.suffix.lower() != ".md" or not source.exists():
                    continue
                if source in seen_sources_for_session:
                    continue
                seen_sources_for_session.add(source)

                base_slug = slugify(label)
                destination = phase_dir / f"session-{session:02d}-{base_slug}.md"
                suffix = 2
                while destination in used_destinations or destination.exists():
                    destination = phase_dir / f"session-{session:02d}-{base_slug}-{suffix}.md"
                    suffix += 1
                used_destinations.add(destination)
                entries.append(
                    {
                        "session": session,
                        "phase": phase_dir,
                        "source": source,
                        "destination": destination,
                        "label": label,
                    }
                )

    return entries


def remove_moved_rows_from_library_readmes(
    text: str, readme: Path, moved_sources: set[Path]
) -> str:
    output: list[str] = []
    removed = False
    for line in text.splitlines():
        linked_moved_source = False
        for _label, raw_target in LINK_RE.findall(line):
            if is_external(raw_target):
                continue
            path_part, _anchor = split_target(raw_target)
            if not path_part:
                continue
            resolved = (readme.parent / path_part).resolve()
            if resolved in moved_sources:
                linked_moved_source = True
                break
        if linked_moved_source:
            removed = True
            continue
        output.append(line)

    result = "\n".join(output).rstrip() + "\n"
    if removed and "Canonical session lesson bodies have moved" not in result:
        note = (
            "\n> Canonical session lesson bodies have moved into their numbered Phase "
            "folders. This module now indexes only remaining remediation, extension, or "
            "reference material. Use the Phase session launcher for scheduled teaching.\n"
        )
        heading = "## Lessons\n"
        if heading in result:
            result = result.replace(heading, heading + note + "\n", 1)
        else:
            result += note
    return result


def update_architecture_documents(moved_copy_count: int, unique_source_count: int) -> None:
    how_to_use = MISSIONS / "HOW_TO_USE_CLASS_MISSIONS.md"
    how_to_use.write_text(
        """# How to Use Class Missions

## The Only Normal Teaching Path

```text
02_Class_Missions
→ open the assigned numbered Phase
→ open SESSION_LAUNCHER.md
→ click the assigned Session
→ teach the phase-local lesson packet
→ collect the named evidence
```

Every canonical lesson body for Sessions 1–78 is stored directly inside its numbered Phase folder. Teachers and students do not open `_Lesson_Library` during normal delivery.

## What Each Layer Means

| Layer | Who uses it | Purpose |
|---|---|---|
| numbered Phase folder | teacher and student | canonical order and canonical lesson bodies |
| `SESSION_LAUNCHER.md` | teacher and student | exact session-by-session entry point |
| phase-local session file | teacher and student | classroom cycle, tasks, evidence, and gate |
| `_Lesson_Library` | teacher or maintainer | remediation, extension, alternatives, and competition banks only |
| `_Curriculum_Governance` | curriculum maintainer | audits, counts, architecture, and maintenance |

## Normal Class Workflow

1. The teacher announces the Phase and Session number.
2. Everyone opens the numbered Phase folder.
3. Everyone clicks `SESSION_LAUNCHER.md`.
4. Everyone opens the linked phase-local session packet.
5. Students use only the resources and templates linked by that packet.
6. The teacher collects the named evidence.
7. The class advances only after the session or phase gate is satisfied.

## What Not to Do

Do not:

- browse `_Lesson_Library` to locate a scheduled lesson;
- schedule every extension lesson;
- treat a legacy module number as a canonical Session number;
- teach from governance documents;
- add an extension to the canonical schedule without recording the change.

## When to Use the Lesson Library

Open `_Lesson_Library` only for reteaching, extra practice, an alternative explanation, a domain extension, reproduction work, mock contests, or curriculum maintenance.

## Source-of-Truth Rule

- **Schedule and canonical lesson bodies:** numbered Phase folders.
- **Exact entry point:** each Phase `SESSION_LAUNCHER.md`.
- **Extra material:** `_Lesson_Library`.
- **Teacher planning and release evidence:** `09_Teacher_Planning` and `10_Ready_to_Teach_Pack`.
""",
        encoding="utf-8",
    )

    library_readme = MISSIONS / "_Lesson_Library/README.md"
    library_readme.write_text(
        f"""# Lesson Library — Extensions and Remediation Only

Canonical lesson bodies for Sessions 1–78 now live directly in their numbered Phase folders. This directory is no longer the storage location for scheduled lessons.

Use this library only for:

- reteaching after a failed gate;
- extra practice;
- alternative explanations;
- domain extensions;
- past-paper reproduction;
- mock contests;
- optional competition sprints;
- curriculum maintenance.

The migration created {moved_copy_count} phase-local canonical lesson packets from {unique_source_count} unique former library lesson files. A source used by more than one canonical Session was copied into each relevant Phase before the former library source was removed.

Start normal teaching from [`02_Class_Missions/README.md`](../README.md), then open the Phase `SESSION_LAUNCHER.md`.
""",
        encoding="utf-8",
    )


def main() -> int:
    entries = collect_entries()
    if not entries:
        raise RuntimeError("No canonical launcher links into _Lesson_Library were found")

    source_to_entries: dict[Path, list[dict[str, object]]] = defaultdict(list)
    for entry in entries:
        source = entry["source"]
        assert isinstance(source, Path)
        source_to_entries[source].append(entry)

    moved_sources = set(source_to_entries)
    original_contents = {
        source: source.read_text(encoding="utf-8") for source in moved_sources
    }

    # Create one phase-local canonical packet per scheduled Session/link.
    for entry in entries:
        source = entry["source"]
        destination = entry["destination"]
        assert isinstance(source, Path)
        assert isinstance(destination, Path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = rewrite_links_for_copy(
            original_contents[source], source, destination, source_to_entries
        )
        destination.write_text(content.rstrip() + "\n", encoding="utf-8")

    # Rewrite every maintained Markdown link that previously targeted a moved file.
    markdown_files = list(ROOT.rglob("*.md"))
    for path in markdown_files:
        if path.resolve() in moved_sources:
            continue
        text = path.read_text(encoding="utf-8")
        if LIBRARY in path.resolve().parents and path.name == "README.md":
            text = remove_moved_rows_from_library_readmes(
                text, path, moved_sources
            )
        rewritten = rewrite_links_in_existing_file(
            text, path, source_to_entries
        )
        if rewritten != path.read_text(encoding="utf-8"):
            path.write_text(rewritten.rstrip() + "\n", encoding="utf-8")

    # Remove former library sources only after all copies and links are ready.
    for source in sorted(moved_sources):
        source.unlink()

    # Remove empty legacy directories where possible, but preserve non-empty extension modules.
    for directory in sorted(LIBRARY.rglob("*"), reverse=True):
        if directory.is_dir():
            try:
                directory.rmdir()
            except OSError:
                pass

    update_architecture_documents(len(entries), len(moved_sources))

    print(f"Created {len(entries)} phase-local canonical lesson packets")
    print(f"Removed {len(moved_sources)} unique canonical sources from _Lesson_Library")
    print("Rewrote maintained Markdown links")
    print("Lesson Library now contains remediation and extension material only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
