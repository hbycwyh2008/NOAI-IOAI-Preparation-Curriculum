# Round 1 and Round 2 Pathway

This page is a high-level comparison. The executable sources are the [NOAI Round 1 Compressed Path](NOAI_Round1_Compressed_Path.md), [NOAI Round 2 Project Path](NOAI_Round2_Project_Path.md), and `curriculum_spec.json`.

## Round 1 — Paper-Based Mastery Plus Controlled Workflow

The route contains 45 Sessions and daily model-recognition practice. Students must be able to:

- define and distinguish concepts;
- calculate simple statistics and evaluation metrics;
- trace Python and ML code;
- complete short code fragments;
- identify sample, X, y, labels, output, task, baseline, metric, validation, and limitations;
- complete Session 57’s controlled tabular workflow before Session 58’s secured mixed checkpoint;
- explain model behaviour in realistic scenarios;
- answer within the current official time window.

Round 1 completion is not equivalent to completion of Sessions 1–58. The compressed route omits named breadth and carries an explicit capability boundary.

## Round 2 — Applied AI Practice

Round 2 is an additional 22-Session continuation after inspected Round 1 qualification. It does not repeat Session 58.

The route first recovers:

```text
Session 32 — deep-network bridge
Session 47 — neural-network introduction
```

It then continues with Sessions 59–78. Students must be able to:

- inspect an unfamiliar dataset;
- establish a simple baseline quickly;
- choose a valid metric and validation design;
- reconstruct a complete training loop;
- train and compare simple and stronger models;
- use documentation and AI tools responsibly;
- analyse errors before tuning;
- manage time, GPU/CPU memory, local assets, and submission format;
- produce a valid prediction file before optimising further;
- reproduce the project from a clean environment.

## Promotion Rule

The teacher marks the Round 2 entry gate only after inspecting Round 1 exit evidence. Generate the continuation plan with:

```bash
python scripts/plan_learning_path.py \
  --pathway noai_round2 \
  --completed-pathway noai_round1 \
  --entry-qualified
```

Planner output does not replace the secured assessment, mastery dashboard, or teacher decision.
