from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LIBRARY = MISSIONS / "_Lesson_Library"
GOVERNANCE = MISSIONS / "_Curriculum_Governance"

MODULES = [
    "00-course-overview",
    "01-python-foundations",
    "02-control-flow-and-data-structures",
    "03-libraries-sorting-searching",
    "04-ai-foundations-and-ethics",
    "05-learning-paradigms",
    "06-linear-regression",
    "07-logistic-regression",
    "08-statistics-probability-distance",
    "09-model-evaluation",
    "10-generalization-regularization",
    "11-trees-and-ensembles",
    "12-neural-network-foundations",
    "13-backprop-optimization",
    "14-cnn-foundations",
    "15-round-1-exam-training",
    "16-numpy-pandas-matplotlib",
    "17-data-cleaning-feature-engineering",
    "18-sklearn-workflow",
    "19-pytorch-foundations",
    "20-computer-vision",
    "21-nlp-sequence-models",
    "22-audio-speech",
    "23-llm-generative-ai",
    "24-round-2-project-training",
    "25-past-paper-reproduction",
    "26-mock-contests",
    "27-official-bohrium-video-lessons",
    "28-competition-sprint-task-data-tuning",
    "shared",
]

GOVERNANCE_MOVES = {
    "02_Class_Missions/Class_Mission_Resource_Architecture.md":
        "02_Class_Missions/_Curriculum_Governance/Class_Mission_Resource_Architecture.md",
    "02_Class_Missions/Lesson_Distribution_Audit.md":
        "02_Class_Missions/_Curriculum_Governance/Lesson_Distribution_Audit.md",
}

TEXT_SUFFIXES = {".md", ".py", ".txt", ".yml", ".yaml", ".json", ".html"}
LINK_PATTERN = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def normalise(path: PurePosixPath) -> str:
    return os.path.normpath(path.as_posix()).replace("\\", "/")


def build_path_map() -> dict[str, str]:
    path_map: dict[str, str] = {}
    for name in MODULES:
        old_root = MISSIONS / name
        if not old_root.exists():
            raise RuntimeError(f"Expected Class Mission directory is missing: {old_root}")
        for path in old_root.rglob("*"):
            if path.is_file():
                old_rel = path.relative_to(ROOT).as_posix()
                new_rel = (LIBRARY / name / path.relative_to(old_root)).relative_to(ROOT).as_posix()
                path_map[old_rel] = new_rel

    for old_rel, new_rel in GOVERNANCE_MOVES.items():
        if not (ROOT / old_rel).exists():
            raise RuntimeError(f"Expected governance file is missing: {old_rel}")
        path_map[old_rel] = new_rel
    return path_map


def move_content() -> dict[str, str]:
    path_map = build_path_map()
    LIBRARY.mkdir(parents=True, exist_ok=True)
    GOVERNANCE.mkdir(parents=True, exist_ok=True)

    for name in MODULES:
        run("git", "mv", str(MISSIONS / name), str(LIBRARY / name))
    for old_rel, new_rel in GOVERNANCE_MOVES.items():
        run("git", "mv", old_rel, new_rel)
    return path_map


def rewrite_moved_markdown_links(path_map: dict[str, str]) -> None:
    reverse_map = {new: old for old, new in path_map.items()}

    for new_rel, old_rel in reverse_map.items():
        path = ROOT / new_rel
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")

        def replace_link(match: re.Match[str]) -> str:
            prefix, raw_target, suffix = match.groups()
            target = raw_target.strip()
            if (
                not target
                or target.startswith("#")
                or target.startswith("/")
                or "://" in target
                or target.startswith("mailto:")
                or target.startswith("data:")
            ):
                return match.group(0)

            target_path, separator, anchor = target.partition("#")
            old_source = PurePosixPath(old_rel)
            old_target = normalise(old_source.parent / target_path)
            new_target = path_map.get(old_target, old_target)
            new_source = PurePosixPath(new_rel)
            rewritten = os.path.relpath(
                new_target,
                start=new_source.parent.as_posix(),
            ).replace("\\", "/")
            if separator:
                rewritten += "#" + anchor
            return f"{prefix}{rewritten}{suffix}"

        updated = LINK_PATTERN.sub(replace_link, text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def replace_explicit_repo_paths() -> None:
    replacements = {
        f"02_Class_Missions/{name}": f"02_Class_Missions/_Lesson_Library/{name}"
        for name in MODULES
    }
    replacements.update(GOVERNANCE_MOVES)

    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or ".git" in path.parts
            or path.suffix.lower() not in TEXT_SUFFIXES
        ):
            continue
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def write_governance_architecture() -> None:
    architecture = GOVERNANCE / "Class_Mission_Resource_Architecture.md"
    architecture.write_text(
        """# Class Mission Resource Architecture

## Design Principle

The curriculum is organised by **learning dependency**, not by a flat list of topics or external resources.

```text
CS50P Python
→ NumPy / Pandas / Matplotlib
→ Bohrium Chinese ML foundations
→ Kaggle workflow refresh
→ Andrew Ng ML + mathematics intuition + model recognition + typical tasks
→ Andrew Ng DL + PyTorch + domain tasks
→ model comparison + EDA + feature engineering + evaluation
→ tuning + ensembling + competition simulation
```

## Separation of Responsibilities

| Location | Responsibility |
|---|---|
| phase folders | scheduled route, prerequisites, gates, and resource roles |
| `_Lesson_Library` | reusable lessons, remediation, alternatives, deeper practice, and extensions |
| `_Curriculum_Governance` | architecture, counts, auditing, and maintenance |
| `03_Templates` | student evidence templates |
| `05_Resources` | external-course maps and resource details |
| `06_Starter_Code` / `06_Starter_Notebooks` | executable scaffolds |
| `09_Teacher_Planning` | implementation and pilot decisions |
| `10_Ready_to_Teach_Pack` | delivery and readiness records |

## External Resource Roles

| Resource | Role |
|---|---|
| Harvard CS50’s Introduction to Programming with Python | Python spine |
| NumPy, Pandas, Matplotlib documentation | data-tool source of truth |
| 北京市十一学校《中学机器学习十五讲》 | pre-Andrew Chinese concept sequence |
| Kaggle Learn | short workflow refresh |
| Machine Learning Specialization | classical ML spine |
| StatQuest | model/statistics intuition |
| 3Blue1Brown | linear-algebra/calculus intuition |
| Deep Learning Specialization | deep-learning concept spine |
| PyTorch courses and documentation | deep-learning implementation spine |
| official NOAI/IOAI tasks and rules | assessment format, constraints, and competition integration |

A resource title is not a curriculum phase. Every resource needs a placement, student action, and evidence requirement.
""",
        encoding="utf-8",
    )

    audit = GOVERNANCE / "Lesson_Distribution_Audit.md"
    text = audit.read_text(encoding="utf-8")
    if "## Navigation Status" not in text:
        text = text.replace(
            "# Class Mission Lesson Distribution and File-Structure Audit\n",
            "# Class Mission Lesson Distribution and File-Structure Audit\n\n"
            "## Navigation Status\n\n"
            "The counted lesson files live under `02_Class_Missions/_Lesson_Library`. "
            "The scheduled route is defined by the phase folders; file coverage is not a teaching sequence.\n\n",
        )
        audit.write_text(text, encoding="utf-8")


def update_validator() -> None:
    path = ROOT / "scripts/validate_curriculum_structure.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        'MISSIONS = ROOT / "02_Class_Missions"\n',
        'MISSIONS = ROOT / "02_Class_Missions"\nLIBRARY = MISSIONS / "_Lesson_Library"\n',
    )
    text = text.replace("folder = MISSIONS / module", "folder = LIBRARY / module")
    text = text.replace("path.relative_to(MISSIONS)", "path.relative_to(LIBRARY)")
    text = text.replace(
        "return (MISSIONS / candidate).resolve()",
        "return (LIBRARY / candidate).resolve()",
    )
    text = text.replace("path = MISSIONS / relative", "path = LIBRARY / relative")
    text = text.replace(
        '("75 scheduled sessions", "Phase 8 — Competition Sprint")',
        '("75 scheduled sessions", "Phase 8 — Tuning, Ensembling, and Competition")',
    )
    text = text.replace(
        '("Phase", "68–75", "155 lessons", "16 lessons")',
        '("Phase", "72–75", "155 mainline lesson files", "16 Bohrium resource lessons")',
    )
    text = text.replace(
        'require_text("02_Class_Missions/README.md", ("28 — Competition Sprint",), errors)',
        'require_text("02_Class_Missions/README.md", ("CS50P", "Bohrium", "Andrew Ng Machine Learning", "Andrew Ng Deep Learning", "Model Comparison"), errors)',
    )

    anchor = '    "02_Class_Missions/_Curriculum_Governance/Class_Mission_Resource_Architecture.md",\n'
    additions = "".join(
        f'    "{item}",\n'
        for item in [
            "02_Class_Missions/00_Orientation_and_Evidence/README.md",
            "02_Class_Missions/01_CS50P_Python/README.md",
            "02_Class_Missions/02_NumPy_Pandas_Visualisation/README.md",
            "02_Class_Missions/03_Bohrium_ML_Foundations/README.md",
            "02_Class_Missions/04_Kaggle_ML_Refresh/README.md",
            "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/README.md",
            "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Math_Intuition_Map.md",
            "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Model_Recognition_Routine.md",
            "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/README.md",
            "02_Class_Missions/07_Model_Comparison_EDA_Evaluation/README.md",
            "02_Class_Missions/08_Tuning_Ensembling_Competition/README.md",
        ]
    )
    if anchor in text and additions not in text:
        text = text.replace(anchor, anchor + additions)
    path.write_text(text, encoding="utf-8")


def update_notebook_sessions() -> None:
    path = ROOT / "scripts/generate_ready_notebooks.py"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    mapping = {
        "N01": "3-12",
        "N02": "68-71",
        "N03": "38-43",
        "N04": "45-47",
        "N05": "13-18, 69-70",
        "N06": "33-37, 69-72",
        "N07": "56-59",
        "N08": "60-62",
        "N09": "60-62",
        "N10": "63-65",
        "N11": "66",
        "N12": "65-67",
    }
    for lesson_id, sessions in mapping.items():
        pattern = rf'("id": "{lesson_id}", "file": [^\n]+?"sessions": ")[^"]+("\s*,)'
        text, count = re.subn(pattern, rf'\g<1>{sessions}\g<2>', text)
        if count != 1:
            raise RuntimeError(f"Could not update notebook session metadata for {lesson_id}: {count}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    path_map = move_content()
    rewrite_moved_markdown_links(path_map)
    replace_explicit_repo_paths()
    write_governance_architecture()
    update_validator()
    update_notebook_sessions()


if __name__ == "__main__":
    main()
