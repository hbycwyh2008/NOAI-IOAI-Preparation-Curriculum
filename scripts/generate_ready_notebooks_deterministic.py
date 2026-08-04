from __future__ import annotations

from collections import defaultdict, deque
from hashlib import sha256
from pathlib import Path
import runpy

import nbformat

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts/generate_ready_notebooks.py"
OUT = ROOT / "06_Starter_Notebooks/ready_to_teach"
EXPECTED_NOTEBOOKS = 12


def source_text(cell: nbformat.NotebookNode) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source)


def semantic_key(cell: nbformat.NotebookNode) -> tuple[str, str]:
    return str(cell.get("cell_type", "")), source_text(cell)


def deterministic_id(path: Path, index: int, cell: nbformat.NotebookNode, salt: int = 0) -> str:
    payload = "\0".join(
        (
            path.name,
            str(index),
            str(cell.get("cell_type", "")),
            source_text(cell),
            str(salt),
        )
    )
    return sha256(payload.encode("utf-8")).hexdigest()[:8]


def capture_existing_ids() -> dict[str, dict[tuple[str, str], deque[str]]]:
    captured: dict[str, dict[tuple[str, str], deque[str]]] = {}
    for path in sorted(OUT.glob("*.ipynb")):
        notebook = nbformat.read(path, as_version=4)
        pools: dict[tuple[str, str], deque[str]] = defaultdict(deque)
        for cell in notebook.cells:
            cell_id = str(cell.get("id", "")).strip()
            if cell_id:
                pools[semantic_key(cell)].append(cell_id)
        captured[path.name] = pools
    return captured


def stabilise_notebook(path: Path, pools: dict[tuple[str, str], deque[str]]) -> None:
    notebook = nbformat.read(path, as_version=4)
    used: set[str] = set()

    for index, cell in enumerate(notebook.cells):
        cell_id = ""
        candidates = pools.get(semantic_key(cell))
        while candidates:
            candidate = candidates.popleft()
            if candidate not in used:
                cell_id = candidate
                break

        salt = 0
        while not cell_id or cell_id in used:
            candidate = deterministic_id(path, index, cell, salt)
            salt += 1
            if candidate not in used:
                cell_id = candidate

        cell["id"] = cell_id
        used.add(cell_id)

    if len(used) != len(notebook.cells):
        raise RuntimeError(f"Duplicate cell IDs remain in {path}")

    nbformat.write(notebook, path)


def main() -> int:
    existing = capture_existing_ids()
    runpy.run_path(str(GENERATOR), run_name="__main__")

    notebooks = sorted(OUT.glob("*.ipynb"))
    if len(notebooks) != EXPECTED_NOTEBOOKS:
        raise RuntimeError(f"Expected {EXPECTED_NOTEBOOKS} notebooks, found {len(notebooks)}")

    for path in notebooks:
        stabilise_notebook(path, existing.get(path.name, defaultdict(deque)))

    print(f"Generated and stabilised {len(notebooks)} notebooks in {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
