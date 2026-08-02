# Canonical Phase 6 — Andrew Ng DL, Selected D2L Bridges, and PyTorch

**Sessions:** 59–70  
**Canonical folder:** `02_Class_Missions/06_Andrew_Ng_DL_PyTorch/`

## Purpose

Use Andrew Ng as the concept spine, selected *Dive into Deep Learning* sections as the concept-to-code bridge, and PyTorch as the implementation spine. Students must reconstruct the assigned mechanism rather than submit copied external notebooks.

## Entry Conditions

Students can recognise classical task types, build a valid baseline, use a validation split, and explain overfitting and generalisation.

## Delivery Priorities

- tensors, shapes, dtypes, devices, modules, losses, and complete training loops;
- forward propagation, autograd, backpropagation, optimisation, initialisation, regularisation, BatchNorm, and Dropout;
- required D2L bridges in Sessions 61, 62, 63, 65, 66, and 68;
- CNNs, transfer learning, augmentation, RNN/LSTM, embeddings, attention, and Transformers;
- image, text/time-series, audio, or multimodal tasks;
- simple or classical baseline retained for every domain task;
- compute-aware experiment design, checkpointing, and error analysis.

## D2L Boundary

Use the [D2L selective reading map](../../05_Resources/D2L_Selective_Reading_Map.md). Assign only the named PyTorch sections. Every required bridge follows:

```text
selected fragment
→ equations, shapes, and assumptions
→ guided reproduction
→ close the source
→ independent rebuild
→ failure test and correction
```

Do not assign the entire book inside the 78-session route.

## Required Evidence

- fresh PyTorch training/validation loop;
- tensor-shape and dtype explanations;
- selected D2L bridge calculations and independent reconstructions;
- learning curves and overfitting diagnosis;
- saved best checkpoint and reproducible reload;
- baseline-versus-deep-model comparison;
- domain-specific error slices and cost/limitation record.

## Exit Gate

The student can build and debug a complete PyTorch system from a fresh environment, explain the training mechanism, reconstruct the required D2L bridge mechanisms, diagnose common failure modes, and defend whether the deep model is justified over a simpler baseline.