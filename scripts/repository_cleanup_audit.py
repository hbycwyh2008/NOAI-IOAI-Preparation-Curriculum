from __future__ import annotations

import hashlib
import os
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "10_Ready_to_Teach_Pack/Repository_Cleanup_Audit.md"

EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".json", ".toml", ".ini", ".cfg", ".csv"}
LINK_RE = re.compile(r"!?(?:\[([^\]]*)\])\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BACKTICK_PATH_RE = re.compile(r"`([^`\n]+(?:\.md|\.py|\.ipynb|\.yml|\.yaml|\.csv|/README\.md))`")

STALE_PATTERNS = {
    "old 75-session pathway": re.compile(r"\b75[- ]session|\b75 sessions\b", re.IGNORECASE),
    "old 67+8 pathway": re.compile(r"67\s*\+\s*8|67 core", re.IGNORECASE),
    "old fixed lesson-bank count": re.compile(r"155 mainline|171 public lesson|171 reusable", re.IGNORECASE),
    "obsolete standalone Kaggle phase": re.compile(r"04_Kaggle_ML_Refresh|Sessions?\s+33[–-]37.*Kaggle", re.IGNORECASE),
    "canonical browsing of Lesson Library": re.compile(r"browse .*_Lesson_Library|choose .*_Lesson_Library", re.IGNORECASE),
}

TEMP_NAME_RE = re.compile(r"(?:^|[-_.])(old|backup|bak|copy|tmp|temp|draft|deprecated)(?:[-_.]|$)", re.IGNORECASE)
GENERATED_NAME_RE = re.compile(r"(?:Latest|Generated|Automated).*\.(?:md|json|txt)$", re.IGNORECASE)


def files() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        result.append(path)
    return sorted(result)


def text_files(all_files: list[Path]) -> list[Path]:
    return [p for p in all_files if p.suffix.lower() in TEXT_SUFFIXES]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def github_anchor(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text.strip().lower())
    text = re.sub(r"[^\w\-\u4e00-\u9fff ]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def anchors(path: Path) -> set[str]:
    values: set[str] = set()
    counts: defaultdict[str, int] = defaultdict(int)
    for line in read_text(path).splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = github_anchor(match.group(2))
        if not base:
            continue
        count = counts[base]
        counts[base] += 1
        values.add(base if count == 0 else f"{base}-{count}")
    return values


def split_target(raw: str) -> tuple[str, str]:
    raw = raw.strip().strip("<>")
    if "#" in raw:
        path, anchor = raw.split("#", 1)
        return path.strip(), anchor.strip().lower()
    return raw, ""


def is_external(raw: str) -> bool:
    return raw.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> None:
    all_files = files()
    all_text = text_files(all_files)
    markdown = [p for p in all_text if p.suffix.lower() == ".md"]

    broken_links: list[str] = []
    broken_anchors: list[str] = []
    incoming: defaultdict[Path, list[str]] = defaultdict(list)
    backtick_missing: list[str] = []

    for document in markdown:
        text = read_text(document)
        for _label, raw in LINK_RE.findall(text):
            raw = raw.strip()
            if not raw or is_external(raw):
                continue
            target_raw, anchor = split_target(raw)
            target = document if not target_raw else (document.parent / target_raw).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                broken_links.append(f"`{rel(document)}` → `{raw}` escapes the repository")
                continue
            if not target.exists():
                broken_links.append(f"`{rel(document)}` → `{raw}`")
                continue
            incoming[target].append(rel(document))
            if anchor and target.suffix.lower() == ".md" and anchor not in anchors(target):
                broken_anchors.append(f"`{rel(document)}` → `{raw}`")

        for raw in BACKTICK_PATH_RE.findall(text):
            raw = raw.strip()
            if raw.startswith(("http://", "https://")) or " " in raw:
                continue
            candidates = [(document.parent / raw).resolve(), (ROOT / raw).resolve()]
            if not any(candidate.exists() for candidate in candidates):
                backtick_missing.append(f"`{rel(document)}` mentions `{raw}`")

    duplicate_groups: defaultdict[str, list[Path]] = defaultdict(list)
    for path in all_text:
        content = read_text(path).strip()
        if len(content) < 80:
            continue
        duplicate_groups[hashlib.sha256(content.encode("utf-8")).hexdigest()].append(path)
    exact_duplicates = [group for group in duplicate_groups.values() if len(group) > 1]

    stale_hits: defaultdict[str, list[str]] = defaultdict(list)
    for path in markdown:
        for number, line in enumerate(read_text(path).splitlines(), start=1):
            for label, pattern in STALE_PATTERNS.items():
                if pattern.search(line):
                    stale_hits[label].append(f"`{rel(path)}:{number}` — {line.strip()}")

    empty_or_tiny = [p for p in all_text if len(read_text(p).strip()) < 100]
    temp_candidates = [p for p in all_files if TEMP_NAME_RE.search(p.name)]
    generated_candidates = [p for p in all_files if GENERATED_NAME_RE.search(p.name)]

    # Markdown files with no incoming Markdown link. Exclude conventional entry points and
    # intentionally direct-use directories from deletion recommendations; still report them.
    unlinked_markdown: list[Path] = []
    for path in markdown:
        if path == REPORT:
            continue
        if path.name in {"README.md", "SESSION_LAUNCHER.md"}:
            continue
        if path not in incoming:
            unlinked_markdown.append(path)

    workflow_text = "\n".join(read_text(p) for p in all_text if p.suffix.lower() in {".yml", ".yaml"})
    document_text = "\n".join(read_text(p) for p in markdown)
    orphan_scripts: list[Path] = []
    for script in sorted((ROOT / "scripts").rglob("*.py")):
        name = script.name
        if name == Path(__file__).name:
            continue
        if name not in workflow_text and name not in document_text:
            orphan_scripts.append(script)

    lines: list[str] = [
        "# Repository Cleanup Audit",
        "",
        "This report is generated from the repository-cleanup branch. A reported item is a review candidate, not automatic proof that deletion is safe.",
        "",
        "## Summary",
        "",
        f"- repository files scanned: **{len(all_files)}**",
        f"- Markdown files scanned: **{len(markdown)}**",
        f"- broken local Markdown links: **{len(broken_links)}**",
        f"- invalid local Markdown anchors: **{len(broken_anchors)}**",
        f"- missing path-like backtick references: **{len(backtick_missing)}**",
        f"- exact duplicate text groups: **{len(exact_duplicates)}**",
        f"- Markdown files with no incoming Markdown link: **{len(unlinked_markdown)}**",
        f"- scripts not named by workflows or Markdown: **{len(orphan_scripts)}**",
        f"- tiny text files under 100 characters: **{len(empty_or_tiny)}**",
        f"- temporary/backup filename candidates: **{len(temp_candidates)}**",
        "",
        "## Broken Local Markdown Links",
        "",
    ]

    lines.extend(f"- {item}" for item in broken_links) if broken_links else lines.append("- None")
    lines += ["", "## Invalid Local Markdown Anchors", ""]
    lines.extend(f"- {item}" for item in broken_anchors) if broken_anchors else lines.append("- None")
    lines += ["", "## Missing Path-Like References in Backticks", ""]
    lines.extend(f"- {item}" for item in sorted(set(backtick_missing))) if backtick_missing else lines.append("- None")

    lines += ["", "## Stale Architecture Language", ""]
    if stale_hits:
        for label, hits in stale_hits.items():
            lines += [f"### {label}", ""]
            lines.extend(f"- {hit}" for hit in hits)
            lines.append("")
    else:
        lines.append("- None")

    lines += ["", "## Exact Duplicate Text Groups", ""]
    if exact_duplicates:
        for index, group in enumerate(exact_duplicates, start=1):
            lines.append(f"### Group {index}")
            lines.append("")
            lines.extend(f"- `{rel(path)}`" for path in group)
            lines.append("")
    else:
        lines.append("- None")

    lines += ["", "## Unlinked Markdown Candidates", ""]
    lines.extend(f"- `{rel(path)}`" for path in unlinked_markdown) if unlinked_markdown else lines.append("- None")

    lines += ["", "## Scripts Not Named by Workflows or Markdown", ""]
    lines.extend(f"- `{rel(path)}`" for path in orphan_scripts) if orphan_scripts else lines.append("- None")

    lines += ["", "## Tiny Text Files", ""]
    lines.extend(f"- `{rel(path)}`" for path in empty_or_tiny) if empty_or_tiny else lines.append("- None")

    lines += ["", "## Temporary or Backup Filename Candidates", ""]
    lines.extend(f"- `{rel(path)}`" for path in temp_candidates) if temp_candidates else lines.append("- None")

    lines += ["", "## Generated/Audit Files to Review for Redundancy", ""]
    lines.extend(f"- `{rel(path)}`" for path in generated_candidates) if generated_candidates else lines.append("- None")

    lines += [
        "",
        "## Safe-Cleanup Policy",
        "",
        "Delete only when at least one condition is met:",
        "",
        "1. the file is an exact duplicate and no distinct path contract requires it;",
        "2. the file is obsolete, unreferenced, and superseded by a named canonical source;",
        "3. the file is a one-time migration artifact or temporary backup;",
        "4. every inbound link is updated and the full repository validators remain green.",
        "",
        "Do not delete a file merely because it has no incoming Markdown link; templates, assessment records, workflow inputs, and teacher-only artifacts may be opened directly.",
    ]

    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
