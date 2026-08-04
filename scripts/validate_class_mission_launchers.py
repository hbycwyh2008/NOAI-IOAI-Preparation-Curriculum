from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")
PHASES = sorted(path for path in MISSIONS.iterdir() if path.is_dir() and re.match(r"^\d{2}_", path.name))


def main() -> int:
    errors: list[str] = []
    sessions: list[int] = []
    packet_count = 0

    for phase in PHASES:
        launcher = phase / "SESSION_LAUNCHER.md"
        if not launcher.exists():
            errors.append(f"Missing launcher: {phase.relative_to(ROOT)}")
            continue
        for line in launcher.read_text(encoding="utf-8").splitlines():
            match = ROW_RE.match(line)
            if not match:
                continue
            session = int(match.group(1))
            sessions.append(session)
            local_md = 0
            for _label, raw in LINK_RE.findall(line):
                if raw.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = raw.split("#", 1)[0].strip()
                if not target:
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() != ".md":
                    continue
                local_md += 1
                packet_count += 1
                if not resolved.exists():
                    errors.append(f"Broken Session {session} link: {raw}")
                    continue
                try:
                    resolved.relative_to(phase.resolve())
                except ValueError:
                    errors.append(f"Session {session} target is outside its Phase: {resolved.relative_to(ROOT)}")
            if local_md == 0:
                errors.append(f"Session {session} has no phase-local Markdown packet")

    if sessions != list(range(1, 79)):
        errors.append(f"Expected Sessions 1–78 exactly once; found {sessions}")

    if errors:
        print("Class Missions launcher validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Class Missions launcher validation passed.")
    print("Canonical launcher coverage: Sessions 1–78 exactly once")
    print(f"Phase-local lesson links: {packet_count}")
    print("Canonical launcher targets outside Phase folders: 0")
    print("Normal delivery path: Phase → Session Launcher → phase-local lesson")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
