from __future__ import annotations

import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
CODE_PATH_RE = re.compile(r"`((?:00_|01_|02_|03_|04_|05_|06_|08_|09_|10_|scripts/|README\.md|MANIFEST\.md|TEACHER_START_HERE\.md|STUDENT_START_HERE\.md)[^`\n]*)`")

REQUIRED_INDEXES = (
    "01_Student_Start/README.md",
    "03_Templates/README.md",
    "04_Assessment/README.md",
    "05_Resources/README.md",
    "08_Public_Documents/README.md",
    "09_Teacher_Planning/README.md",
    "09_Teacher_Planning/Phase_Overviews/README.md",
    "09_Teacher_Planning/Pilot/README.md",
    "10_Ready_to_Teach_Pack/README.md",
)

OBSOLETE_PATHS = (
    "PUBLISH_TO_GITHUB.md",
    "scripts/v1_chunks",
    "10_Ready_to_Teach_Pack/Completion_Audit_90.md",
    "10_Ready_to_Teach_Pack/Phase_0_1_Setup_Python.md",
    "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_0_Setup.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_8_Competition_Sprint.md",
)

BANNED_TEXT = (
    re.compile(r"\b75[- ]session|\b75 sessions\b", re.IGNORECASE),
    re.compile(r"67\s*\+\s*8|67 core", re.IGNORECASE),
    re.compile(r"155 mainline|171 public lesson|171 reusable", re.IGNORECASE),
    re.compile(r"04_Kaggle_ML_Refresh", re.IGNORECASE),
    re.compile(r"_Lesson_Library", re.IGNORECASE),
)


def anchor(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text.strip().lower())
    text = re.sub(r"[^\w\-\u4e00-\u9fff ]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def anchors(path: Path) -> set[str]:
    result: set[str] = set()
    counts: defaultdict[str, int] = defaultdict(int)
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = anchor(match.group(1))
        if not base:
            continue
        index = counts[base]
        counts[base] += 1
        result.add(base if index == 0 else f"{base}-{index}")
    return result


def main() -> int:
    errors: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))

    for relative in REQUIRED_INDEXES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing repository index: {relative}")

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Obsolete path still exists: {relative}")

    for document in markdown:
        text = document.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("# "):
            errors.append(f"Markdown file lacks H1: {document.relative_to(ROOT)}")

        for raw in LINK_RE.findall(text):
            raw = raw.strip().strip("<>")
            if not raw or raw.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            if raw.startswith("#"):
                target = document
                fragment = raw[1:]
            else:
                path_part, marker, fragment = raw.partition("#")
                target = (document.parent / path_part).resolve()
                if not target.exists():
                    errors.append(f"Broken Markdown link: {document.relative_to(ROOT)} -> {raw}")
                    continue
            if fragment and target.suffix.lower() == ".md" and fragment.lower() not in anchors(target):
                errors.append(f"Broken Markdown anchor: {document.relative_to(ROOT)} -> {raw}")

        for raw in CODE_PATH_RE.findall(text):
            raw = raw.strip()
            if " " in raw or "*" in raw:
                continue
            path_part = raw.split("#", 1)[0]
            candidate = (ROOT / path_part).resolve()
            if not candidate.exists():
                errors.append(f"Missing repository path in code span: {document.relative_to(ROOT)} -> {raw}")

        if "Repository_Cleanup_Audit.md" not in document.as_posix():
            for pattern in BANNED_TEXT:
                if pattern.search(text):
                    errors.append(f"Stale architecture language in {document.relative_to(ROOT)}: {pattern.pattern}")

    groups: defaultdict[str, list[Path]] = defaultdict(list)
    for phase in sorted((ROOT / "02_Class_Missions").glob("[0-9][0-9]_*/")):
        for packet in sorted(list(phase.glob("session-*.md")) + list(phase.glob("lesson-*.md"))):
            content = packet.read_text(encoding="utf-8").strip()
            groups[hashlib.sha256(content.encode("utf-8")).hexdigest()].append(packet)
    for group in groups.values():
        if len(group) > 1:
            errors.append("Exact duplicate canonical packets: " + ", ".join(str(p.relative_to(ROOT)) for p in group))

    if errors:
        print("Repository hygiene validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository hygiene validation passed.")
    print(f"Markdown files checked: {len(markdown)}")
    print("Internal Markdown links and anchors: valid")
    print("Exact duplicate canonical packets: 0")
    print("Obsolete pathway and generator files: absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
