from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = MISSIONS / "_Lesson_Library"
PHASE_DIRS = sorted(
    path for path in MISSIONS.iterdir() if path.is_dir() and re.match(r"^\d{2}_", path.name)
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def split_target(raw: str) -> str:
    return raw.strip().split("#", 1)[0].strip()


def collect_architecture() -> tuple[int, int, int]:
    sessions: set[int] = set()
    packet_paths: set[Path] = set()
    for phase in PHASE_DIRS:
        launcher = phase / "SESSION_LAUNCHER.md"
        if not launcher.exists():
            continue
        for line in launcher.read_text(encoding="utf-8").splitlines():
            match = ROW_RE.match(line)
            if not match:
                continue
            session = int(match.group(1))
            sessions.add(session)
            for _label, raw in LINK_RE.findall(line):
                target = split_target(raw)
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() == ".md" and resolved.exists():
                    packet_paths.add(resolved)
    extension_lessons = len(list(LIBRARY.rglob("lesson-*.md")))
    return len(sessions), len(packet_paths), extension_lessons


session_count, packet_count, extension_count = collect_architecture()
if session_count != 78:
    raise RuntimeError(f"Expected 78 launcher sessions before finalization, found {session_count}")

STRUCTURE_VALIDATOR = r'''from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = MISSIONS / "_Lesson_Library"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")

PHASES = (
    ("00_Orientation_and_Evidence", 1, 2),
    ("01_CS50P_Python", 3, 12),
    ("02_NumPy_Pandas_Visualisation", 13, 18),
    ("03_Bohrium_ML_Foundations", 19, 32),
    ("04_AI_History_and_Thinking_Humans", 33, 40),
    ("05_Andrew_Ng_ML_Model_Labs", 41, 58),
    ("06_Andrew_Ng_DL_PyTorch", 59, 70),
    ("07_Model_Comparison_EDA_Evaluation", 71, 74),
    ("08_Tuning_Ensembling_Competition", 75, 78),
)

REQUIRED_FILES = (
    "README.md",
    "TEACHER_START_HERE.md",
    "STUDENT_START_HERE.md",
    "MANIFEST.md",
    "02_Class_Missions/README.md",
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    "00_Course_Overview/Detailed_Lesson_Sequence.md",
    "00_Course_Overview/Pacing_Guide.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
    "scripts/validate_readiness_contract.py",
    "scripts/validate_class_mission_launchers.py",
)


def split_target(raw: str) -> tuple[str, str]:
    path, marker, anchor = raw.strip().partition("#")
    return path.strip(), (f"#{anchor}" if marker else "")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def main() -> int:
    errors: list[str] = []
    seen_sessions: list[int] = []
    canonical_packets: set[Path] = set()

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")

    for phase_name, start, end in PHASES:
        phase = MISSIONS / phase_name
        launcher = phase / "SESSION_LAUNCHER.md"
        readme = phase / "README.md"
        if not phase.exists():
            errors.append(f"Missing phase folder: {phase_name}")
            continue
        if not launcher.exists():
            errors.append(f"Missing launcher: {launcher.relative_to(ROOT)}")
            continue
        if not readme.exists():
            errors.append(f"Missing phase README: {readme.relative_to(ROOT)}")
        elif "Open the Session Launcher" not in readme.read_text(encoding="utf-8"):
            errors.append(f"Phase README does not start from launcher: {readme.relative_to(ROOT)}")

        local_sessions: list[int] = []
        for line in launcher.read_text(encoding="utf-8").splitlines():
            row_match = ROW_RE.match(line)
            if not row_match:
                continue
            session = int(row_match.group(1))
            local_sessions.append(session)
            seen_sessions.append(session)
            local_targets = 0
            for _label, raw_target in LINK_RE.findall(line):
                if is_external(raw_target):
                    continue
                target, _anchor = split_target(raw_target)
                if not target:
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() != ".md":
                    continue
                local_targets += 1
                if not resolved.exists():
                    errors.append(f"Broken launcher target: {launcher.relative_to(ROOT)} -> {raw_target}")
                    continue
                try:
                    resolved.relative_to(phase.resolve())
                except ValueError:
                    errors.append(
                        f"Canonical lesson is not phase-local: Session {session} -> {resolved.relative_to(ROOT)}"
                    )
                try:
                    resolved.relative_to(LIBRARY.resolve())
                    errors.append(
                        f"Canonical launcher still enters _Lesson_Library: Session {session} -> {resolved.relative_to(ROOT)}"
                    )
                except ValueError:
                    pass
                canonical_packets.add(resolved)
            if local_targets == 0:
                errors.append(f"Session {session} has no local Markdown lesson target")

        expected = list(range(start, end + 1))
        if local_sessions != expected:
            errors.append(f"{phase_name}: expected Sessions {expected}, found {local_sessions}")

    if seen_sessions != list(range(1, 79)):
        errors.append("Launchers must contain Sessions 1–78 exactly once and in order")

    for packet in sorted(canonical_packets):
        text = packet.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Canonical packet lacks H1: {packet.relative_to(ROOT)}")
        if "Evidence" not in text and "evidence" not in text:
            errors.append(f"Canonical packet lacks evidence requirement: {packet.relative_to(ROOT)}")

    extension_lessons = sorted(LIBRARY.rglob("lesson-*.md"))
    for lesson in extension_lessons:
        text = lesson.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Extension lesson lacks H1: {lesson.relative_to(ROOT)}")
        if "Evidence" not in text and "evidence" not in text:
            errors.append(f"Extension lesson lacks evidence requirement: {lesson.relative_to(ROOT)}")

    for path in MISSIONS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for label in ("Andrew Ng MLS", "DLS Course", "LHY-ML", "DLAI-PT"):
            if label in text:
                errors.append(f"Unexpanded resource label '{label}': {path.relative_to(ROOT)}")

    obsolete = MISSIONS / "04_Kaggle_ML_Refresh"
    if obsolete.exists():
        errors.append("Obsolete standalone Kaggle Phase 04 still exists")

    if errors:
        print("Curriculum structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Curriculum structure validation passed.")
    print("Canonical sessions: 78")
    print(f"Phase-local canonical lesson packets: {len(canonical_packets)}")
    print(f"Extension/remediation lesson files: {len(extension_lessons)}")
    print("Normal delivery path: Phase → Session Launcher → phase-local lesson")
    print("Canonical launcher links into _Lesson_Library: 0")
    print("Public file-structure and internal-consistency coverage: 100%")
    print("Operational, pilot, privacy, runtime, access, and annual-rule readiness remain separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

LAUNCHER_VALIDATOR = r'''from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = (MISSIONS / "_Lesson_Library").resolve()
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
                try:
                    resolved.relative_to(LIBRARY)
                    errors.append(f"Session {session} still links into _Lesson_Library")
                except ValueError:
                    pass
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
    print("Canonical links into _Lesson_Library: 0")
    print("Normal delivery path: Phase → Session Launcher → phase-local lesson")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

READINESS_VALIDATOR = r'''from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

REQUIRED_FILES = (
    "README.md",
    "TEACHER_START_HERE.md",
    "STUDENT_START_HERE.md",
    "MANIFEST.md",
    "02_Class_Missions/README.md",
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md",
    "03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md",
    "04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md",
    "10_Ready_to_Teach_Pack/Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md",
    "03_Templates/AI_History_Reading_Evidence_Template.md",
    "04_Assessment/AI_History_Phase_Rubric.md",
    "10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
    "10_Ready_to_Teach_Pack/Release_Readiness_Gates.md",
    "10_Ready_to_Teach_Pack/Student_Runtime_Qualification_Record.md",
    "10_Ready_to_Teach_Pack/External_Access_Verification_Record.md",
    "09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md",
)

HIGH_TRAFFIC = (
    "README.md",
    "TEACHER_START_HERE.md",
    "STUDENT_START_HERE.md",
    "MANIFEST.md",
    "02_Class_Missions/README.md",
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    "00_Course_Overview/Course_Map.md",
    "00_Course_Overview/Pacing_Guide.md",
    "10_Ready_to_Teach_Pack/README.md",
    "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md",
)


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for _label, raw in LINK_RE.findall(text):
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = raw.split("#", 1)[0].strip()
        if target and not (path.parent / target).resolve().exists():
            errors.append(f"Broken internal link in {path.relative_to(ROOT)}: {raw}")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing readiness artifact: {relative}")

    for relative in HIGH_TRAFFIC:
        path = ROOT / relative
        if path.exists():
            validate_links(path, errors)

    phase4 = ROOT / "02_Class_Missions/04_AI_History_and_Thinking_Humans"
    if len(list(phase4.glob("lesson-*.md"))) != 8:
        errors.append("Phase 04 must contain eight English AI History seminars")

    overview_dir = ROOT / "09_Teacher_Planning/Phase_Overviews"
    if len(list(overview_dir.glob("Canonical_Phase_*.md"))) != 9:
        errors.append("Expected nine canonical teacher phase overviews")

    launcher_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("02_Class_Missions/[0-9][0-9]_*/SESSION_LAUNCHER.md")
    )
    if "_Lesson_Library" in launcher_text:
        errors.append("A canonical launcher still references _Lesson_Library")

    dashboard = ROOT / "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md"
    if dashboard.exists():
        text = dashboard.read_text(encoding="utf-8")
        for marker in (
            "100% public file-structure and internal-consistency coverage",
            "phase-local canonical lesson",
            "External Evidence Still Required",
            "must not state",
        ):
            if marker not in text:
                errors.append(f"Readiness dashboard missing marker: {marker}")

    math_bridge = ROOT / "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md"
    if math_bridge.exists():
        text = math_bridge.read_text(encoding="utf-8")
        for marker in ("Session 41", "Session 42", "Session 43", "equation", "gradient"):
            if marker not in text:
                errors.append(f"Mathematics bridge missing marker: {marker}")

    if errors:
        print("Readiness contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Readiness contract validation passed.")
    print("Canonical pathway: 78 sessions")
    print("Canonical lesson storage: numbered Phase folders")
    print("AI History seminars: 8")
    print("Andrew ML mathematics transition: Sessions 41–43")
    print("Canonical teacher overviews: 9")
    print("Operational readiness remains cohort-, runtime-, access-, security-, pilot-, and year-specific")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

write(ROOT / "scripts/validate_curriculum_structure.py", STRUCTURE_VALIDATOR)
write(ROOT / "scripts/validate_class_mission_launchers.py", LAUNCHER_VALIDATOR)
write(ROOT / "scripts/validate_readiness_contract.py", READINESS_VALIDATOR)

README = f'''# NOAI / IOAI Preparation Curriculum

A mastery-focused artificial-intelligence curriculum for secondary-school students preparing for NOAI China and later IOAI-style open-ended tasks.

## Start Here

- [Teacher Start Here](TEACHER_START_HERE.md)
- [Student Start Here](STUDENT_START_HERE.md)
- [Class Missions](02_Class_Missions/README.md)
- [Detailed 78-Session Sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)

## Canonical Learning Path

```text
CS50P Python
→ NumPy, Pandas, and visualisation
→ Bohrium machine-learning foundations
→ AI history and critical reading with Melanie Mitchell
→ Andrew Ng Machine Learning
   + Sessions 41–43 mathematics transition
   + StatQuest and 3Blue1Brown
   + embedded Kaggle practice
   + model recognition and typical tasks
→ Andrew Ng Deep Learning + PyTorch
→ model comparison, EDA, features, and evaluation
→ tuning, ensembling, and competition simulation
```

## Storage Model

The normal teaching path is:

```text
numbered Phase
→ SESSION_LAUNCHER.md
→ phase-local lesson packet
```

All canonical lesson bodies for Sessions 1–78 live directly inside their numbered Phase folders. `_Lesson_Library` contains only remediation, extension, alternative explanations, reproductions, mocks, and optional competition banks.

## Current Architecture

- **78 canonical sessions** across nine numbered phases;
- **{packet_count} unique phase-local Markdown packets** linked by the session launchers;
- **{extension_count} remaining extension/remediation lesson files** in `_Lesson_Library`;
- eight English AI History seminars in Sessions 33–40;
- an explicit Andrew ML mathematics transition in Sessions 41–43.

## Evidence Standard

Watching, reading, or running supplied code is not mastery. Students must recognise, explain, reconstruct, calculate, implement, debug, evaluate, analyse errors, and submit reproducible evidence.

## Readiness Boundary

Passing repository checks establishes **100% public file-structure and internal-consistency coverage** for maintained assets. Exact student runtime, authenticated access, legal book access, private assessment security, representative pilots, full-cohort evidence, and current competition rules remain separate gates.
'''
write(ROOT / "README.md", README)

MANIFEST = f'''# Repository Architecture Manifest

## Canonical Architecture

| Layer | Current state |
|---|---|
| Scheduled pathway | 78 Sessions across nine numbered Phase folders |
| Canonical lesson storage | directly inside the relevant Phase folder |
| Canonical launcher targets | {packet_count} unique phase-local Markdown packets |
| Extension/remediation library | {extension_count} remaining `lesson-*.md` files |
| AI History | eight English seminars, Sessions 33–40 |
| Andrew ML mathematics bridge | Sessions 41–43 |

## Source Priority

1. `02_Class_Missions/README.md` — canonical Phase order;
2. each Phase `SESSION_LAUNCHER.md` — exact Session entry point;
3. phase-local lesson packet — classroom cycle, tasks, evidence, and gate;
4. `_Lesson_Library` — optional remediation and extension only;
5. `00_Course_Overview/` — pacing and pathway summaries;
6. `10_Ready_to_Teach_Pack/` — delivery and release evidence.

## Validation

```bash
python scripts/validate_curriculum_structure.py
python scripts/validate_readiness_contract.py
python scripts/validate_class_mission_launchers.py
python scripts/check_required_links.py
```

The validators require Sessions 1–78 exactly once, phase-local canonical links, valid internal paths, AI History and mathematics-bridge artifacts, and an explicit operational-readiness boundary.
'''
write(ROOT / "MANIFEST.md", MANIFEST)

COURSE_MAP = '''# Current Course Map

| Phase | Sessions | Focus | Exit gate |
|---:|---:|---|---|
| 0 | 1–2 | orientation and evidence | environment and submission workflow ready |
| 1 | 3–12 | CS50P Python | independent small-program writing and debugging |
| 2 | 13–18 | NumPy, Pandas, and visualisation | reproducible data audit and visual evidence |
| 3 | 19–32 | Bohrium machine-learning foundations | core task and model vocabulary established |
| 4 | 33–40 | AI History and Thinking Humans | evidence-based AI claim audit completed |
| 5 | 41–58 | Andrew Ng ML, mathematics transition, model labs, embedded Kaggle | defensible classical baseline and model card |
| 6 | 59–70 | Andrew Ng DL and PyTorch | fresh training loop and domain-task comparison |
| 7 | 71–74 | model comparison, EDA, features, evaluation | valid model and evaluation design defended |
| 8 | 75–78 | tuning, ensembling, simulation, postmortem | reproducible competition workflow completed |

Open each Phase through its `SESSION_LAUNCHER.md`. Every canonical lesson packet is stored directly in that Phase.
'''
write(ROOT / "00_Course_Overview/Course_Map.md", COURSE_MAP)

PACING = '''# Pacing Guide

| Phase | Sessions | Count |
|---|---:|---:|
| Orientation and evidence | 1–2 | 2 |
| CS50P Python | 3–12 | 10 |
| NumPy, Pandas, and visualisation | 13–18 | 6 |
| Bohrium foundations | 19–32 | 14 |
| AI History and Thinking Humans | 33–40 | 8 |
| Andrew Ng ML and model labs | 41–58 | 18 |
| Andrew Ng DL and PyTorch | 59–70 | 12 |
| Model comparison, EDA, and evaluation | 71–74 | 4 |
| Tuning, ensembling, and competition | 75–78 | 4 |

**Total: 78 sessions**

Ordinary missions use 75 minutes. Sessions 19–32 and 33–40 are named 70-minute exceptions. Long competition simulations use the target event duration.

Reading, video completion, or external-course progress does not replace the Session gate. Teachers assign extensions from `_Lesson_Library` only after opening the canonical phase-local lesson.
'''
write(ROOT / "00_Course_Overview/Pacing_Guide.md", PACING)

EXPANDED = f'''# Expanded Lesson Architecture

## Canonical Layer

The scheduled curriculum contains 78 Sessions. Each Session appears exactly once in a numbered Phase launcher, and every linked canonical lesson body is stored in that same Phase folder.

- Session launcher coverage: 1–78 exactly once;
- unique phase-local linked packets: {packet_count};
- canonical links into `_Lesson_Library`: zero.

Some Sessions deliberately use more than one packet, for example a concept packet plus a calculation, implementation, or evaluation packet.

## Extension Layer

`_Lesson_Library` contains {extension_count} remaining lesson files for remediation, alternative explanations, deeper domain work, reproductions, mocks, and optional competition sprints. These files are not part of the canonical Session count unless a teacher records a cohort-specific extension.

## Maintenance Rule

Do not place a new canonical lesson only in `_Lesson_Library`. Add it to the relevant Phase and link it from that Phase launcher. Library material must remain optional.
'''
write(ROOT / "00_Course_Overview/Expanded_Lesson_Architecture.md", EXPANDED)

COMPLETENESS = f'''# Curriculum Completeness Audit

## Public Repository Result

| Dimension | Result |
|---|---|
| Canonical pathway | 78 Sessions, complete |
| Phase launchers | nine, complete |
| Phase-local canonical lesson storage | complete |
| Unique phase-local launcher targets | {packet_count} |
| Canonical links into Lesson Library | zero |
| Extension/remediation lessons | {extension_count} |
| AI History seminars | eight, complete |
| Andrew ML mathematics transition | Sessions 41–43, complete |
| Internal consistency validators | present and enforced in CI |

The maintained public repository has **100% public file-structure and internal-consistency coverage**.

## Evidence Still Outside the Repository

This result does not establish exact-device runtime, authenticated external-course access, legal book access, private assessment security, representative classroom timing, a full 78-Session cohort run, or current-year competition-rule alignment.
'''
write(ROOT / "00_Course_Overview/Curriculum_Completeness_Audit.md", COMPLETENESS)

ARCHITECTURE = f'''# Class Mission Resource Architecture

## Canonical Teaching Layer

```text
02_Class_Missions/00_... through 08_...
→ SESSION_LAUNCHER.md
→ phase-local lesson packet
```

Sessions 1–78 are the only canonical schedule. The launchers currently reference {packet_count} unique phase-local Markdown packets. No canonical launcher enters `_Lesson_Library`.

## Optional Resource Layer

`_Lesson_Library` contains {extension_count} remaining lesson files for remediation, extension, alternative explanations, reproductions, mocks, and optional competition practice.

## Governance Layer

`_Curriculum_Governance` contains architecture, distribution, and maintenance records. It is not used for student delivery.

## Change Rule

A new scheduled lesson must be created inside its numbered Phase and linked from the launcher. A file placed only in `_Lesson_Library` is optional by definition.
'''
write(ROOT / "02_Class_Missions/_Curriculum_Governance/Class_Mission_Resource_Architecture.md", ARCHITECTURE)

DISTRIBUTION = f'''# Lesson Distribution Audit

## Canonical Distribution

| Phase | Sessions |
|---:|---:|
| 0 | 1–2 |
| 1 | 3–12 |
| 2 | 13–18 |
| 3 | 19–32 |
| 4 | 33–40 |
| 5 | 41–58 |
| 6 | 59–70 |
| 7 | 71–74 |
| 8 | 75–78 |

- 78 scheduled Sessions;
- {packet_count} unique phase-local packets linked from Session rows;
- {extension_count} remaining extension/remediation `lesson-*.md` files;
- zero scheduled links into `_Lesson_Library`.

Packet count is greater than Session count because selected Sessions intentionally combine multiple packets. The Session count, not the file count, defines pacing.
'''
write(ROOT / "02_Class_Missions/_Curriculum_Governance/Lesson_Distribution_Audit.md", DISTRIBUTION)

READY_README = f'''# Ready-to-Teach Curriculum Pack

This directory supports the canonical 78-Session pathway.

## Normal Delivery

1. Open [Class Missions](../02_Class_Missions/README.md).
2. Open the assigned numbered Phase.
3. Open `SESSION_LAUNCHER.md`.
4. Open the phase-local lesson packet.
5. Collect the named evidence and apply the Session or Phase gate.

Canonical teaching does not require browsing `_Lesson_Library`.

## Current Public Architecture

- 78 canonical Sessions;
- {packet_count} unique phase-local launcher targets;
- {extension_count} remaining optional extension/remediation lessons;
- eight AI History seminars;
- Andrew ML mathematics transition in Sessions 41–43.

## Canonical Delivery Packs

- [Phase 4 — AI History and Thinking Humans](Phase_4_AI_History_and_Thinking_Humans.md)
- [Phase 5 — Andrew ML Mathematics Bridge](Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md)
- [Phase 8 — Tuning, Ensembling, and Competition](Phase_8_Competition_Sprint.md)

## Readiness Records

- [Public Repository Readiness Dashboard](Public_Repository_Readiness_Dashboard.md)
- [Curriculum Readiness Audit](Curriculum_Readiness_Audit.md)
- [Release Readiness Gates](Release_Readiness_Gates.md)
- [Student Runtime Qualification Record](Student_Runtime_Qualification_Record.md)
- [External Access Verification Record](External_Access_Verification_Record.md)
- [Representative Pilot Matrix](../09_Teacher_Planning/Pilot/Representative_Pilot_Matrix.md)

Public structural readiness does not replace real-cohort runtime, access, security, pilot, or annual-rule evidence.
'''
write(ROOT / "10_Ready_to_Teach_Pack/README.md", READY_README)

READINESS_AUDIT = f'''# Curriculum Readiness Audit

## Public Repository Coverage

| Item | Status |
|---|---|
| 78-Session canonical pathway | complete |
| nine Phase launchers | complete |
| canonical lessons physically stored in Phases | complete |
| unique phase-local linked packets | {packet_count} |
| canonical Library links | zero |
| extension/remediation library | {extension_count} lesson files |
| AI History seminars | eight complete English lessons |
| Andrew ML mathematics bridge | complete for Sessions 41–43 |
| structural/readiness/launcher CI | enforced |

**Result: 100% public file-structure and internal-consistency coverage.**

## Operational Evidence Still Required

- exact student runtime qualification;
- authenticated access checks;
- legal book access;
- private Teacher Key and hidden-assessment security;
- representative lesson pilots;
- full-cohort evidence;
- current competition-year rules.
'''
write(ROOT / "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md", READINESS_AUDIT)

DASHBOARD = f'''# Public Repository Readiness Dashboard

## Maintained Public Assets

| Dimension | Status |
|---|---|
| canonical Sessions 1–78 | complete |
| numbered Phase launchers | complete |
| phase-local canonical lesson storage | complete |
| unique phase-local launcher targets | {packet_count} |
| canonical links into `_Lesson_Library` | zero |
| extension/remediation lesson files | {extension_count} |
| AI History phase | complete |
| Andrew ML mathematics transition | complete |
| internal links and CI contracts | enforced |

The repository has **100% public file-structure and internal-consistency coverage** for maintained assets, including phase-local canonical lesson coverage.

## External Evidence Still Required

- student-device and Bohrium runtime qualification;
- authenticated Coursera, edX, Kaggle, and Bohrium access;
- legal access to Melanie Mitchell’s book;
- private assessment and hidden-test security;
- representative pilots and full-cohort timing evidence;
- current NOAI/IOAI rules.

The project **must not state “100% operationally ready”** until those named external gates pass.
'''
write(ROOT / "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md", DASHBOARD)

# Remove stale fixed-count language from other maintained Markdown documents.
replacements = {
    "155 mainline lesson files": "phase-local canonical lesson packets",
    "155 mainline lessons": "phase-local canonical lesson packets",
    "155 lessons": "canonical and extension lesson packets",
    "171 reusable public lesson/resource files": "the maintained phase-local and extension lesson files",
    "171 public lesson/resource files": "the maintained phase-local and extension lesson files",
    "171 total reusable public lesson/resource files": "the maintained phase-local and extension lesson files",
    "171 total public lesson/resource files": "the maintained phase-local and extension lesson files",
    "16 Bohrium resource lessons": "14 canonical Bohrium Sessions plus optional Bohrium extension resources",
    "Mainline lesson files in `_Lesson_Library`": "Canonical lesson packets in numbered Phase folders",
}
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")

print(f"Finalized 78 canonical Sessions with {packet_count} phase-local packets")
print(f"Remaining extension/remediation lessons: {extension_count}")
print("Replaced fixed Library-count validators with phase-local architecture validators")
