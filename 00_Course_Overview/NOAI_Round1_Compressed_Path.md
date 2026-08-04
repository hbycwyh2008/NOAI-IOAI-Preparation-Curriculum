# NOAI Round 1 Compressed Path

This is the default compressed route for a cohort preparing primarily for the NOAI first-round knowledge and reasoning assessment. It is a selection from the canonical 78-Session curriculum; Session numbers and lesson files are not duplicated or renumbered.

## Entry Standard

Students should be able to use a browser, manage files, type short Python programs, and complete the evidence workflow in Sessions 1–2. Students who cannot yet trace assignment, condition, loop, and function state complete Sessions 3–12 without acceleration.

## Exact Session Route

| Block | Required Sessions | Purpose | Suggested pace |
|---|---|---|---|
| orientation and evidence | 1–2 | rules, platforms, evidence, responsible AI use | 2 sessions |
| Python core | 3–12 | syntax, tracing, data structures, files, exceptions, tests | 10 sessions |
| data tools | 13–18 | NumPy, Pandas, cleaning, grouping, visualisation | 6 sessions |
| ML foundations | 24–31 | workflow, classification, optimisation, neural networks, KNN/Bayes, SVM, trees/ensembles, unsupervised/RL | 8 sessions |
| AI reasoning boundary | 33 and 40 | what intelligence means and whole-book claim audit | 2 sessions |
| mathematical model language | 41–46 | notation, regression, gradient descent, logistic regression, metrics, regularisation | 6 sessions |
| classical model recognition | 48–56 | trees, forests, boosting, KNN, SVM, K-means, PCA, anomaly detection, recommenders | 9 sessions |
| controlled workflow and assessment | 57–58 | end-to-end tabular workflow followed by mixed recognition, calculation, explanation, and correction | 2 sessions |

**Total:** 45 scheduled sessions, plus the daily 15-minute model-recognition routine.

Session 57 is required before Session 58. A mixed capstone cannot be treated as valid evidence when the learner has not first completed the controlled end-to-end workflow that the capstone assesses.

## Daily Practice Contract

From the first use of Session 24 onward, complete one generated set from `04_Assessment/Model_Recognition_Drills/` every study day. Use the public answer record; do not look for a public answer key. A teacher checks task family, baseline, metric, validation design, model candidates, assumptions, leakage risk, and correction quality.

Generate a deterministic five-scenario set with:

```bash
python scripts/generate_daily_model_drill.py --level mixed --date YYYY-MM-DD
```

## Assessment Checkpoints

1. After Session 12: Python trace/debug checkpoint.
2. After Session 18: unfamiliar-table audit and interpretation checkpoint.
3. After Session 31: mixed supervised/unsupervised task recognition.
4. After Session 46: regression/classification mathematics and metric checkpoint.
5. After Session 56: mixed model-family comparison.
6. Session 57: controlled tabular workflow with fixed validation and one justified improvement.
7. Session 58: Round 1 readiness decision using the Round 1 rubric and a secured mock.

## Exit Standard

A student exits this route only when all of the following are true:

- Python tracing/debugging accuracy is at least 85% on two different sets;
- data-audit assertions and interpretations are correct without tutorial copying;
- model-recognition accuracy is at least 90% for five consecutive daily sets;
- the student can distinguish regression, classification, clustering, dimensionality reduction, anomaly detection, recommendation, reinforcement learning, and generation from labels and required output;
- hand calculations, code meaning, metric choice, and one limitation are explained for each major classical model family;
- the Session 57 workflow runs with a trustworthy split, baseline, one controlled change, and a postmortem;
- the secured Round 1 mock meets the teacher-defined passing threshold and every error has a correction note.

## Capability Boundary

This route does **not** establish deep-learning implementation, computer-vision, NLP, audio, multimodal, competition-runtime, or IOAI full-pathway readiness. It supports a first-round knowledge/reasoning goal and one controlled tabular workflow only. Students advancing to project or international preparation continue with the named Round 2 or IOAI route rather than claiming completion of Sessions 1–78.
