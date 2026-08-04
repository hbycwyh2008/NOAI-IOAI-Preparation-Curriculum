from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
CODE_PATH_RE = re.compile(r"`((?:00_|01_|02_|03_|04_|05_|06_|08_|09_|10_|scripts/|README\.md|MANIFEST\.md|TEACHER_START_HERE\.md|STUDENT_START_HERE\.md|curriculum_spec\.json|student_progress\.schema\.json)[^`\n]*)`")

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

REQUIRED_OPERATIONAL_FILES = (
    "curriculum_spec.json",
    "student_progress.schema.json",
    "03_Templates/Student_Progress.example.json",
    "scripts/manage_student_progress.py",
    "scripts/plan_learning_path.py",
    "scripts/generate_daily_model_drill.py",
    "09_Teacher_Planning/Pathway_and_Drill_Operations.md",
    "00_Course_Overview/NOAI_Round1_Compressed_Path.md",
    "00_Course_Overview/NOAI_Round2_Project_Path.md",
    "00_Course_Overview/IOAI_Full_Extension_Path.md",
)

REQUIRED_WORKFLOWS = (
    ".github/workflows/audit-curriculum.yml",
    ".github/workflows/validate-ready-to-teach.yml",
    ".github/workflows/normalise-lesson-timelines.yml",
    ".github/workflows/cleanup-merged-branches.yml",
)

OBSOLETE_PATHS = (
    "PUBLISH_TO_GITHUB.md",
    "scripts/v1_chunks",
    "02_Class_Missions/_Lesson_Library",
    ".github/workflows/attach-final-course-tree.yml",
    "10_Ready_to_Teach_Pack/Automated_Curriculum_Audit_Latest.md",
    "10_Ready_to_Teach_Pack/Completion_Audit_90.md",
    "10_Ready_to_Teach_Pack/Phase_0_1_Setup_Python.md",
    "10_Ready_to_Teach_Pack/Phase_7_Competition_Practice.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_0_Setup.md",
    "09_Teacher_Planning/Phase_Overviews/Phase_8_Competition_Sprint.md",
)

DEPRECATED_ACTION_REFS = (
    "actions/checkout@v4",
    "actions/setup-python@v5",
    "actions/upload-artifact@v4",
    "actions/github-script@v7",
)

BANNED_TEXT = (
    re.compile(r"\b75[- ]session|\b75 sessions\b", re.IGNORECASE),
    re.compile(r"67\s*\+\s*8|67 core", re.IGNORECASE),
    re.compile(r"155 mainline|171 public lesson|171 reusable", re.IGNORECASE),
    re.compile(r"04_Kaggle_ML_Refresh", re.IGNORECASE),
    re.compile(r"_Lesson_Library", re.IGNORECASE),
    re.compile(r"former extension library", re.IGNORECASE),
    re.compile(r"\blesson[- ]library\b", re.IGNORECASE),
    re.compile(r"\b96\s+(?:remaining\s+)?(?:lesson|extension|remediation)", re.IGNORECASE),
    re.compile(r"extension/remediation\s+(?:lesson files|library)", re.IGNORECASE),
    re.compile(r"canonical\s+Library\s+links", re.IGNORECASE),
    re.compile(r"exact\s+44[- ]Session", re.IGNORECASE),
    re.compile(r"\b44\s+scheduled\s+sessions\b", re.IGNORECASE),
    re.compile(r"complete\s+Sessions\s+1[–-]58\s+with\s+the\s+NOAI\s+Round\s+1\s+exit\s+standard", re.IGNORECASE),
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


def require_markers(path: Path, markers: tuple[str, ...], errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"Missing required workflow: {path.relative_to(ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            errors.append(f"{path.relative_to(ROOT)} missing required marker: {marker}")
    return text


def main() -> int:
    errors: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))

    for relative in REQUIRED_INDEXES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing repository index: {relative}")

    for relative in REQUIRED_OPERATIONAL_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required operational file: {relative}")

    for relative in REQUIRED_WORKFLOWS:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required workflow: {relative}")

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Obsolete path still exists: {relative}")

    operational_tools = (
        ROOT / "scripts/manage_student_progress.py",
        ROOT / "scripts/plan_learning_path.py",
        ROOT / "scripts/generate_daily_model_drill.py",
    )
    for path in operational_tools:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for marker in ("--self-test", "curriculum_spec.json"):
                if marker not in text:
                    errors.append(f"Operational tool missing required marker: {path.relative_to(ROOT)} -> {marker}")

    progress_example = ROOT / "03_Templates/Student_Progress.example.json"
    if progress_example.exists():
        try:
            example = json.loads(progress_example.read_text(encoding="utf-8"))
            if "@" in str(example.get("student_id", "")):
                errors.append("Public progress example must not use an email address")
            forbidden_keys = {"name", "email", "answer", "answers", "solution", "solutions", "credential", "password"}
            found_forbidden = forbidden_keys & set(example)
            for record in example.get("drill_history", []):
                if isinstance(record, dict):
                    found_forbidden |= forbidden_keys & set(record)
            if found_forbidden:
                errors.append(f"Public progress example contains forbidden identity/answer keys: {sorted(found_forbidden)}")
        except json.JSONDecodeError as error:
            errors.append(f"Invalid public progress example JSON: {error}")

    common_tool_markers = (
        "python scripts/manage_student_progress.py --self-test",
        "python scripts/manage_student_progress.py validate --path 03_Templates/Student_Progress.example.json",
        "python scripts/plan_learning_path.py --self-test",
        "python scripts/generate_daily_model_drill.py --self-test",
    )

    audit_workflow = ROOT / ".github/workflows/audit-curriculum.yml"
    audit_text = require_markers(
        audit_workflow,
        (
            "contents: read",
            "actions/checkout@v6",
            "actions/setup-python@v6",
            "actions/upload-artifact@v6",
            *common_tool_markers,
        ),
        errors,
    )
    for marker in ("contents: write", "git push", "git commit", "Automated_Curriculum_Audit_Latest.md"):
        if marker in audit_text:
            errors.append(f"Audit workflow must not mutate the repository: found {marker}")

    ready_workflow = ROOT / ".github/workflows/validate-ready-to-teach.yml"
    ready_text = require_markers(
        ready_workflow,
        (
            "contents: read",
            "actions/checkout@v6",
            "actions/setup-python@v6",
            "actions/upload-artifact@v6",
            *common_tool_markers,
            "Verify generated notebooks are current",
            "git status --porcelain -- 06_Starter_Notebooks/ready_to_teach",
            "Upload volatile validation reports",
        ),
        errors,
    )
    for marker in (
        "contents: write",
        "git push",
        "git commit",
        "Commit generated notebooks on main",
        "github-actions[bot]",
        "10_Ready_to_Teach_Pack/Runtime_Validation_Record.md",
        "10_Ready_to_Teach_Pack/Link_Verification_Latest.md",
    ):
        if marker in ready_text:
            errors.append(f"Ready-to-Teach workflow must be read-only: found {marker}")

    fast_workflow = ROOT / ".github/workflows/normalise-lesson-timelines.yml"
    require_markers(
        fast_workflow,
        (
            "contents: read",
            "actions/checkout@v6",
            "actions/setup-python@v6",
            "python scripts/validate_curriculum_spec.py",
            *common_tool_markers,
        ),
        errors,
    )

    cleanup_workflow = ROOT / ".github/workflows/cleanup-merged-branches.yml"
    cleanup_text = require_markers(
        cleanup_workflow,
        (
            "types: [closed]",
            "contents: write",
            "pull-requests: read",
            "actions/github-script@v9",
            "pull.merged",
            "pull.head.repo.full_name",
            "defaultBranch",
            "github.rest.git.deleteRef",
            "closedPulls.data.some((pull) => pull.merged_at)",
        ),
        errors,
    )
    if "branches: [main]" not in cleanup_text:
        errors.append("Merged-branch cleanup bootstrap must be scoped to main")
    if ".github/workflows/cleanup-merged-branches.yml" not in cleanup_text:
        errors.append("Merged-branch cleanup bootstrap must run only when its workflow is introduced or changed")

    workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
    for workflow in workflows:
        text = workflow.read_text(encoding="utf-8")
        for marker in DEPRECATED_ACTION_REFS:
            if marker in text:
                errors.append(f"Deprecated GitHub Action runtime in {workflow.relative_to(ROOT)}: {marker}")

        if workflow == cleanup_workflow:
            continue
        for marker in ("git push", "git commit", "contents: write"):
            if marker in text:
                errors.append(
                    f"Only merged-branch cleanup may mutate repository refs: {workflow.relative_to(ROOT)} contains {marker}"
                )

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
    print("Obsolete pathway, parallel lesson, migration, and generator files: absent")
    print("Pseudonymous progress schema/example and protected-answer boundary: enforced")
    print("Progress manager, planner, and recent-repeat drill generator: present and self-tested in all validation workflows")
    print("Corrected pathway counts and recovery dependencies: stale language blocked")
    print("Validation workflows: read-only and Node 24 compatible")
    print("Volatile validation reports in repository history: disabled")
    print("Merged same-repository branches: automatic cleanup enabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
