from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "02_Class_Missions").glob("[0-9][0-9]-*/lesson-*.md"))
errors = []

if len(paths) != 67:
    errors.append(f"Expected 67 lesson files, found {len(paths)}")

for path in paths:
    text = path.read_text(encoding="utf-8")
    if "**Duration:**" not in text:
        errors.append(f"Missing duration: {path.relative_to(ROOT)}")
    if "## Timeline" not in text:
        errors.append(f"Missing timeline: {path.relative_to(ROOT)}")
    if "| Time | Block | Student output |" not in text:
        errors.append(f"Missing timeline table: {path.relative_to(ROOT)}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(paths)} lesson files with explicit durations and timelines.")
