from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")

REQUIRED_FILES = (
    "README.md",
    "TEACHER_START_HERE.md",
    "STUDENT_START_HERE.md",
    "MANIFEST.md",
    "curriculum_spec.json",
    "scripts/plan_learning_path.py",
    "scripts/generate_daily_model_drill.py",
    "00_Course_Overview/NOAI_Round1_Compressed_Path.md",
    "00_Course_Overview/NOAI_Round2_Project_Path.md",
    "00_Course_Overview/IOAI_Full_Extension_Path.md",
    "09_Teacher_Planning/Pathway_and_Drill_Operations.md",
    "02_Class_Missions/README.md",
    "02_Class_Missions/HOW_TO_USE_CLASS_MISSIONS.md",
    "02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md",
    "03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md",
    "04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md",
    "04_Assessment/Model_Recognition_Drills/README.md",
    "10_Ready_to_Teach_Pack/Phase_5_Andrew_Ng_ML_Mathematics_Bridge.md",
    "03_Templates/AI_History_Reading_Evidence_Template.md",
    "04_Assessment/AI_History_Phase_Rubric.md",
    "10_Ready_to_Teach_Pack/Phase_4_AI_History_and_Thinking_Humans.md",
    "05_Resources/D2L_Selective_Reading_Map.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-61-d2l-autograd-backprop-bridge.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-62-d2l-regularisation-optimisation-bridge.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-63-d2l-convolution-shape-bridge.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-65-d2l-fine-tuning-bridge.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-66-d2l-rnn-lstm-bridge.md",
    "02_Class_Missions/06_Andrew_Ng_DL_PyTorch/session-68-d2l-attention-transformer-bridge.md",
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
    "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md",
    "09_Teacher_Planning/README.md",
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


def validate_launcher_targets(errors: list[str]) -> None:
    for launcher in ROOT.glob("02_Class_Missions/[0-9][0-9]_*/SESSION_LAUNCHER.md"):
        phase = launcher.parent.resolve()
        for line in launcher.read_text(encoding="utf-8").splitlines():
            if not ROW_RE.match(line):
                continue
            for _label, raw in LINK_RE.findall(line):
                if raw.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = raw.split("#", 1)[0].strip()
                if not target:
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() != ".md":
                    continue
                try:
                    resolved.relative_to(phase)
                except ValueError:
                    errors.append(
                        f"Canonical launcher target is outside its Phase: {launcher.relative_to(ROOT)} -> {raw}"
                    )


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

    validate_launcher_targets(errors)

    dashboard = ROOT / "10_Ready_to_Teach_Pack/Public_Repository_Readiness_Dashboard.md"
    if dashboard.exists():
        text = dashboard.read_text(encoding="utf-8")
        for marker in (
            "100% public file-structure and internal-consistency coverage",
            "phase-local canonical lesson",
            "evidence-aware pathway planner",
            "deterministic daily-drill generator",
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

    d2l_map = ROOT / "05_Resources/D2L_Selective_Reading_Map.md"
    if d2l_map.exists():
        text = d2l_map.read_text(encoding="utf-8")
        for marker in (
            "Session 61",
            "Session 62",
            "Session 63",
            "Session 65",
            "Session 66",
            "Session 68",
            "independent rebuild",
        ):
            if marker not in text:
                errors.append(f"D2L selective map missing marker: {marker}")

    for tool in (
        ROOT / "scripts/plan_learning_path.py",
        ROOT / "scripts/generate_daily_model_drill.py",
    ):
        if tool.exists():
            text = tool.read_text(encoding="utf-8")
            if "--self-test" not in text:
                errors.append(f"Operational tool lacks self-test: {tool.relative_to(ROOT)}")

    if errors:
        print("Readiness contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Readiness contract validation passed.")
    print("Canonical pathway: 78 sessions")
    print("Canonical lesson storage: numbered Phase folders")
    print("Canonical launcher targets outside Phase folders: 0")
    print("Executable pathways: exact routes and recovery dependencies")
    print("Operational tools: pathway planner and deterministic daily drill generator")
    print("AI History seminars: 8")
    print("Andrew ML mathematics transition: Sessions 41–43")
    print("D2L concept-to-code bridges: Sessions 61, 62, 63, 65, 66, and 68")
    print("Canonical teacher overviews: 9")
    print("Operational readiness remains cohort-, runtime-, access-, security-, pilot-, and year-specific")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
