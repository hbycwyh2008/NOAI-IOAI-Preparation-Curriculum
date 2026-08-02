from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
OLD_PHASE = MISSIONS / "04_Kaggle_ML_Refresh"
NEW_PHASE = MISSIONS / "04_AI_History_and_Thinking_Humans"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def replace(path: Path, replacements: list[tuple[str, str]]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


if OLD_PHASE.exists():
    shutil.rmtree(OLD_PHASE)
NEW_PHASE.mkdir(parents=True, exist_ok=True)

LESSONS = [
    {
        "file": "lesson-01-what-counts-as-intelligence.md",
        "title": "What Counts as Intelligence?",
        "reading": "Prologue and Chapter 1",
        "question": "What evidence is required before a machine should be described as intelligent?",
        "mastery": [
            "Explain that artificial intelligence is a research field rather than one single technique.",
            "Describe the basic ambition of early artificial-intelligence research.",
            "Explain the symbolic-AI intuition: represent knowledge with symbols and manipulate those symbols with rules or search.",
            "Explain what the Turing test attempts to measure and what it cannot prove.",
            "Distinguish intelligent behaviour, human-like behaviour, understanding, and consciousness.",
            "Identify when the term AI is being used as a field, a system, a capability, or a marketing label.",
            "Separate an observable system behaviour from a larger unsupported claim about its internal understanding.",
        ],
        "misconceptions": [
            "Conversational fluency proves human-like understanding.",
            "Artificial intelligence began only with modern deep learning.",
            "Passing one behavioural test proves consciousness.",
        ],
        "pattern": "AI claim → observable behaviour → test conditions → evidence → supported conclusion → unsupported conclusion",
        "guided": "Audit the claim: ‘A system can sustain a convincing conversation, therefore it understands language in the same way a person does.’",
        "rebuild": "Create a concept map connecting problem solving, learning, perception, language, reasoning, understanding, and consciousness. Mark which relationships are evidence-based and which remain open questions.",
        "exit": "Explain in two minutes why completing an intelligent task does not by itself prove human-like intelligence.",
    },
    {
        "file": "lesson-02-neural-networks-and-ai-cycles.md",
        "title": "Neural Networks, Machine Learning, and AI Cycles",
        "reading": "Chapters 2–3",
        "question": "Why has artificial intelligence repeatedly moved through periods of optimism and disappointment?",
        "mastery": [
            "Explain that artificial neural networks are inspired by biology but are not accurate replicas of brains.",
            "Identify inputs, weights, weighted combinations, outputs, errors, and parameter updates.",
            "Distinguish hand-written rules from parameters learned from data.",
            "Formalise supervised learning with input X, label y, prediction, error, and update.",
            "Explain why early neural-network approaches were limited.",
            "Explain how data, computing power, and algorithmic improvements contributed to later success.",
            "Describe AI spring and AI winter as interactions among technical results, promises, funding, and public expectations.",
            "Distinguish symbolic AI, machine learning, and deep learning.",
        ],
        "misconceptions": [
            "Neural networks think exactly like biological brains.",
            "More data guarantees that every problem can be solved.",
            "Deep learning has replaced every other AI method.",
        ],
        "pattern": "early success → broad promise → hidden limitation → real-world failure → reduced confidence → new technical conditions",
        "guided": "Compare a medical decision system built from explicit expert rules with one trained from labelled patient records.",
        "rebuild": "Build a two-track timeline: technical developments on one track and public expectations, investment, or disappointment on the other.",
        "exit": "Explain why a major benchmark improvement does not by itself show that human-level general intelligence is near.",
    },
    {
        "file": "lesson-03-how-machines-recognise-images.md",
        "title": "How Machines Recognise Images",
        "reading": "Chapters 4–5",
        "question": "Is image classification a form of seeing, understanding, or sophisticated pattern matching?",
        "mastery": [
            "Formalise image classification: pixels as input, class labels as y, and class scores or probabilities as output.",
            "Distinguish training, validation, and test data.",
            "Explain the intuition of local receptive fields, learned filters, feature hierarchies, and convolution.",
            "Explain why convolutional structure is useful for images.",
            "Describe the role of large labelled datasets and shared benchmarks such as ImageNet.",
            "Distinguish object classification, detection, scene description, contextual reasoning, and causal understanding.",
            "Explain why high benchmark accuracy supports only a bounded claim under a particular data and evaluation protocol.",
            "Recognise that label categories and dataset construction involve human decisions.",
        ],
        "misconceptions": [
            "Recognising the label cat proves that a model understands what a cat is.",
            "High test accuracy guarantees performance on every real-world image.",
            "Dataset labels are fully objective descriptions of reality.",
        ],
        "pattern": "pixels → local learned features → feature hierarchy → class scores → predicted label",
        "guided": "Compare cat–dog classification, danger detection in a photograph, and explaining why people in a scene are running.",
        "rebuild": "Construct a capability ladder from pixel processing to classification, detection, scene description, contextual reasoning, and causal understanding. Give one test and one limitation for each level.",
        "exit": "Identify X, y, prediction, and metric in an image-classification task, then explain why correct recognition is not full scene understanding.",
    },
    {
        "file": "lesson-04-what-did-the-model-learn.md",
        "title": "What Did the Model Actually Learn?",
        "reading": "Chapters 6–7",
        "question": "Why can a highly accurate system still be unreliable?",
        "mastery": [
            "Explain that a model may learn task-relevant features, accidental correlations, collection artefacts, backgrounds, or watermarks.",
            "Explain shortcut learning.",
            "Explain distribution shift between training conditions and deployment conditions.",
            "Describe what adversarial examples reveal about model fragility.",
            "Distinguish accuracy, robustness, fairness, interpretability, and safety.",
            "Explain how aggregate metrics can hide failures in particular groups or situations.",
            "Explain that datasets, labels, metrics, and deployment boundaries contain human choices.",
            "Identify human responsibility for data collection, model selection, deployment, monitoring, and stopping rules.",
        ],
        "misconceptions": [
            "A high validation score is sufficient evidence for deployment.",
            "Every failure can be fixed by making the model larger.",
            "Data is a complete and neutral copy of the real world.",
        ],
        "pattern": "training data → learned correlation → evaluation protocol → deployment environment → failure mode → affected people",
        "guided": "Analyse a hospital model that performs well at one hospital and poorly at another. Identify possible shifts in equipment, populations, labels, and workflows.",
        "rebuild": "Produce an AI trust checklist covering data origin, label quality, deployment shift, subgroup results, extreme inputs, error costs, human review, and stop conditions.",
        "exit": "Given a system with high accuracy, ask at least five questions that accuracy alone cannot answer.",
    },
    {
        "file": "lesson-05-reward-games-and-reinforcement-learning.md",
        "title": "Reward, Games, and Reinforcement Learning",
        "reading": "Chapters 8–10",
        "question": "Does winning a game demonstrate intelligence that transfers to the real world?",
        "mastery": [
            "Identify agent, environment, state, action, reward, and policy.",
            "Distinguish supervised labels from reinforcement-learning rewards.",
            "Explain exploration versus exploitation.",
            "Distinguish immediate reward from long-term return.",
            "Explain how reward design shapes learned behaviour.",
            "Explain reward hacking or specification gaming.",
            "Explain why games provide clear rules, measurable outcomes, repeated simulation, and bounded action spaces.",
            "Contrast game environments with incomplete, changing, socially consequential real environments.",
            "Distinguish search, learning, and self-play.",
            "Distinguish superhuman performance in one closed task from general intelligence.",
        ],
        "misconceptions": [
            "A task without human labels is free of human design choices.",
            "Maximising a written reward guarantees the intended human outcome.",
            "Game mastery automatically transfers to real-world decision making.",
        ],
        "pattern": "state → action → environment response → reward → policy update",
        "guided": "Design a reward for a classroom-cleaning robot and identify behaviours that could maximise the score while violating the real goal.",
        "rebuild": "Specify a reinforcement-learning task with state, actions, reward, episode boundary, likely reward loophole, and at least one safety constraint.",
        "exit": "Explain why achieving the specified reward does not prove that a machine understands the designer’s true intention.",
    },
    {
        "file": "lesson-06-language-processing-and-understanding.md",
        "title": "Language Processing and Understanding",
        "reading": "Chapters 11–13",
        "question": "When a machine produces fluent language, what has it demonstrated?",
        "mastery": [
            "Explain the intuition that words appearing in similar contexts can receive similar representations.",
            "Explain the purpose of word vectors or embeddings.",
            "Describe translation as input-sequence encoding, internal representation, and output-sequence decoding.",
            "Identify ambiguity, reference, irony, implied meaning, culture, and world knowledge as language challenges.",
            "Distinguish grammatical generation, common-pattern completion, contextual reasoning, and understanding of speaker intent.",
            "Explain how question-answering systems may use statistical patterns, retrieval clues, or learned associations.",
            "Explain why fluency can cause people to overestimate factual reliability and understanding.",
            "Design counterexamples, paraphrases, and context changes to test a language system.",
            "Avoid the opposite error of assuming that a system without human-like understanding has no useful capabilities.",
        ],
        "misconceptions": [
            "Fluent language is necessarily factually correct.",
            "A correct answer proves understanding of the reasoning process.",
            "Language meaning can be reduced to word order without world knowledge.",
        ],
        "pattern": "linguistic form → contextual representation → generated or selected output → apparent meaning → understanding test",
        "guided": "Design three questions: one answerable by common text patterns, one requiring reference resolution, and one requiring physical or social common sense.",
        "rebuild": "Build a language-capability ladder from word association through grammatical generation, translation, question answering, contextual reasoning, and grounded understanding. Add a test and an unsupported claim for each level.",
        "exit": "Explain how an answer can be correct while still providing insufficient evidence that the system understood the question.",
    },
    {
        "file": "lesson-07-common-sense-abstraction-and-analogy.md",
        "title": "Common Sense, Abstraction, and Analogy",
        "reading": "Chapters 14–15",
        "question": "What additional abilities are involved in human-like understanding?",
        "mastery": [
            "Explain why understanding cannot be captured by one simple metric.",
            "Distinguish memorisation, interpolation, generalisation, transfer, and abstraction.",
            "Explain the grounding problem: how symbols or words connect to experience and the world.",
            "Identify physical, social, intentional, causal, and situational common sense.",
            "Explain abstraction as preserving transferable structure while ignoring irrelevant surface detail.",
            "Explain analogy as mapping relations between different domains rather than matching appearances.",
            "Identify where an analogy works and where it breaks.",
            "Explain why success on a nearby test distribution is not unlimited transfer.",
            "Recognise the roles of prior knowledge, small-sample learning, and embodied experience in human learning.",
        ],
        "misconceptions": [
            "Because understanding has no perfect definition, it cannot be studied.",
            "Memorising many examples necessarily creates an abstract concept.",
            "Analogy is only surface similarity.",
        ],
        "pattern": "surface features → relational structure → abstraction → transfer → new situation",
        "guided": "Compare a surface-association problem with a relational analogy and identify the background knowledge required by each.",
        "rebuild": "Choose an analogy and identify its source domain, target domain, relation mapping, transferable structure, and failure boundary.",
        "exit": "Give distinct examples of pattern recognition, generalisation, abstraction, analogy, and understanding.",
    },
    {
        "file": "lesson-08-how-intelligent-is-ai.md",
        "title": "Whole-Book Synthesis: How Intelligent Is AI?",
        "reading": "Chapter 16 and whole-book review",
        "question": "How should a careful thinker evaluate claims about the intelligence of an AI system?",
        "mastery": [
            "Construct a timeline of symbolic AI, neural networks, machine learning, deep learning, reinforcement learning, AI springs, and AI winters.",
            "Compare symbolic AI, supervised learning, deep learning, and reinforcement learning.",
            "Explain the conditions supporting modern data-driven AI success.",
            "Summarise strengths in large-scale pattern recognition, bounded optimisation, high-speed computation, and data processing.",
            "Summarise limitations involving distribution shift, shortcut learning, common sense, causality, abstraction, transfer, and goal alignment.",
            "Distinguish narrow-task performance, general intelligence, autonomy, understanding, and consciousness.",
            "Evaluate optimistic and pessimistic AI claims using evidence rather than rhetoric.",
            "Identify overgeneralisation from one benchmark, fluency-as-truth, prediction-as-causality, and unlimited extrapolation of progress.",
            "Connect the book to task definition, data, model, loss, training, evaluation, generalisation, and limitations in Andrew Ng Machine Learning.",
            "State a defensible position and identify evidence that could change it.",
        ],
        "misconceptions": [
            "One benchmark establishes general intelligence.",
            "Rapid progress in one area proves unlimited progress everywhere.",
            "One failure invalidates an entire technical approach.",
        ],
        "pattern": "task → input/output → training experience → metric → test conditions → failure boundary → supported claim",
        "guided": "Audit the claim: ‘A system achieved a high score on a difficult examination, therefore it has human-level general intelligence.’",
        "rebuild": "Produce a Thinking Human’s AI Brief containing a historical map, a capability–limitation matrix, and an evidence-based position using at least three cases from the book plus one counterargument.",
        "exit": "Use the ten-question AI Claim Audit on a new AI product or news claim without teacher prompting.",
    },
]

LESSON_TEMPLATE = """# Session {session} — {title}

**Class duration:** 70 minutes  
**Required reading before class:** {reading} from Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*  
**Essential question:** {question}

## Required Mastery

Students must be able to:

{mastery}

## Misconceptions to Reject

{misconceptions}

## Core Pattern

```text
{pattern}
```

## 70-Minute Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–7 | **Skill Warm-Up** | Retrieve the chapter’s people, ideas, cases, or claims without reopening the book. |
| 7–14 | **Talk Robin 1** | Compare one central claim, one supporting case, and one unresolved question. |
| 14–20 | **Entry Check** | Demonstrate that the assigned reading was completed and understood. |
| 20–32 | **Core Pattern** | Extract the transferable reasoning structure for this lesson. |
| 32–48 | **Guided Practice** | {guided} |
| 48–62 | **Independent Rebuild** | {rebuild} |
| 62–70 | **Talk Robin 2 + Evidence** | Explain the rebuilt artifact and submit evidence. |

## Reading Evidence Required Before Class

- one-sentence statement of the author’s central claim;
- one case or example used as evidence;
- one unresolved question;
- one AI claim that should be tested rather than accepted at face value.

A plot summary alone does not count. Students must distinguish the author’s claim, the evidence in the text, and their own judgement.

## Exit Evidence

{exit}

## Gate

A student does not pass by remembering names or chapter summaries alone. The student must use evidence, identify the boundary of a claim, and independently reconstruct the lesson’s reasoning pattern.
"""

for index, item in enumerate(LESSONS, start=33):
    mastery = "\n".join(f"{i}. {point}" for i, point in enumerate(item["mastery"], start=1))
    misconceptions = "\n".join(f"- {point}" for point in item["misconceptions"])
    write(
        NEW_PHASE / item["file"],
        LESSON_TEMPLATE.format(
            session=index,
            mastery=mastery,
            misconceptions=misconceptions,
            **item,
        ),
    )

lesson_links = "\n".join(
    f"{i}. [Session {32+i} — {item['title']}]({item['file']})"
    for i, item in enumerate(LESSONS, start=1)
)

write(
    NEW_PHASE / "README.md",
    f"""# 04 — AI History and Thinking Humans

**Scheduled sessions:** 33–40  
**Core text:** Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*  
**Role:** historical, conceptual, and critical-thinking bridge between the Bohrium foundation sequence and Andrew Ng Machine Learning

This is an eight-session reading-and-reasoning sequence. Reading is completed before class. Classroom time is used to retrieve, discuss, test claims, reconstruct arguments, and produce evidence. The book is not copied into this repository; students use a legally obtained copy.

## Eight Sessions

{lesson_links}

## Phase Outcomes

By the end of the phase, students can:

- explain the major historical shifts among symbolic AI, machine learning, deep learning, and reinforcement learning;
- distinguish task performance from broad claims about intelligence or understanding;
- analyse how data, objectives, benchmarks, and deployment conditions limit a system;
- distinguish recognition, prediction, generation, reasoning, abstraction, analogy, and understanding;
- audit a new AI claim using task, evidence, evaluation conditions, failure modes, and unsupported conclusions;
- connect the book’s ideas to the modelling concepts they will meet in Andrew Ng Machine Learning.

## Phase Gate

Students must submit a **Thinking Human’s AI Brief** containing:

1. a historical map;
2. a capability–limitation matrix;
3. an evidence-based position on the intelligence of current AI;
4. at least three cases from the book;
5. one serious counterargument;
6. a statement of what new evidence could change the student’s position.

Students who cannot distinguish benchmark success from general intelligence return to the relevant lesson before entering Andrew Ng Machine Learning.

## Kaggle Placement

Kaggle Learn is no longer a separate scheduled phase. Selected Kaggle exercises are embedded inside the Andrew Ng Machine Learning model labs as short workflow rehearsals and typical-task implementations. See [Kaggle Learn Refresh Map](../../05_Resources/Kaggle_Learn_Refresh_Map.md).
""",
)

write(
    MISSIONS / "README.md",
    """# Class Missions — Canonical 78-Session Pathway

Use the numbered phase folders in order. They are the scheduled route. `_Lesson_Library` contains remediation, alternatives, deeper practice, and competition extensions; it is not a second schedule.

| Phase | Sessions | Purpose |
|---:|---:|---|
| [00 — Orientation and Evidence](00_Orientation_and_Evidence/README.md) | 1–2 | environment, evidence, and competition expectations |
| [01 — CS50P Python](01_CS50P_Python/README.md) | 3–12 | programming independence |
| [02 — NumPy, Pandas, and Visualisation](02_NumPy_Pandas_Visualisation/README.md) | 13–18 | data handling and basic visual analysis |
| [03 — Bohrium ML Foundations](03_Bohrium_ML_Foundations/README.md) | 19–32 | Chinese-language machine-learning concept foundation |
| [04 — AI History and Thinking Humans](04_AI_History_and_Thinking_Humans/README.md) | 33–40 | AI history, claims, evidence, understanding, and limits |
| [05 — Andrew Ng ML Model Labs](05_Andrew_Ng_ML_Model_Labs/README.md) | 41–58 | classical models, mathematics intuition, model recognition, Kaggle practice, and typical tasks |
| [06 — Andrew Ng DL and PyTorch](06_Andrew_Ng_DL_PyTorch/README.md) | 59–70 | deep-learning concepts paired with implementation |
| [07 — Model Comparison, EDA, and Evaluation](07_Model_Comparison_EDA_Evaluation/README.md) | 71–74 | model limits, data quality, features, validation, and error analysis |
| [08 — Tuning, Ensembling, and Competition](08_Tuning_Ensembling_Competition/README.md) | 75–78 | diagnosis-first tuning, ensembling, simulation, and postmortem |

## Canonical Dependency Order

```text
CS50P Python
→ NumPy / Pandas / visualisation
→ Bohrium machine-learning foundations
→ AI history and critical reading with Melanie Mitchell
→ Andrew Ng Machine Learning
   + StatQuest
   + 3Blue1Brown
   + embedded Kaggle practice
   + model recognition
   + typical tasks
→ Andrew Ng Deep Learning + PyTorch
→ model comparison + EDA + evaluation
→ tuning + ensembling + competition simulation
```

## Supporting Areas

- [`_Lesson_Library`](./_Lesson_Library/README.md) — selectable lessons and extensions
- [`_Curriculum_Governance`](./_Curriculum_Governance/README.md) — architecture, counts, and maintenance
""",
)

write(
    ROOT / "00_Course_Overview/Course_Map.md",
    """# Current Course Map

| Phase | Sessions | Focus | Exit gate |
|---:|---:|---|---|
| 0 | 1–2 | orientation, evidence, environment | student can use the course workflow and evidence rules |
| 1 | 3–12 | CS50P Python | student can write, trace, test, and debug small programs independently |
| 2 | 13–18 | NumPy, Pandas, Matplotlib | student can inspect, transform, summarise, and visualise data |
| 3 | 19–32 | Bohrium machine-learning foundations | student can identify supervised, unsupervised, and reinforcement-learning tasks and explain core model ideas |
| 4 | 33–40 | Melanie Mitchell reading sequence | student can explain AI history and audit claims about intelligence, understanding, and limitations |
| 5 | 41–58 | Andrew Ng ML model labs | student can recognise tasks, select baselines, implement classical models, and explain their mathematical intuition and limits |
| 6 | 59–70 | Andrew Ng DL + PyTorch | student can implement and debug deep-learning training for representative tasks |
| 7 | 71–74 | model comparison, EDA, features, evaluation | student can design a valid modelling and evaluation protocol |
| 8 | 75–78 | tuning, ensembling, competition | student can complete a reproducible end-to-end competition workflow |

## Repository Scale

- 78 scheduled sessions;
- 155 mainline lesson-bank files;
- 16 Bohrium resource lessons;
- 171 public lesson/resource files in the reusable bank.
""",
)

write(
    ROOT / "00_Course_Overview/Pacing_Guide.md",
    """# Pacing Guide

## Standard Path

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

## Duration Policy

- Ordinary club mission: 75 minutes.
- Bohrium foundation lessons: named 70-minute exception.
- AI History and Thinking Humans lessons: named 70-minute reading-seminar exception.
- Full competition simulation: target competition duration.
- Readiness conference: scheduled separately or inside Session 78.

## Reading Policy

The Melanie Mitchell phase assumes that assigned reading is completed before class. Classroom time preserves retrieval, discussion, entry checking, concept extraction, guided analysis, independent reconstruction, and evidence. If reading must occur entirely in class, add reading periods rather than removing the learning cycle.

## Gate Policy

- No NumPy/Pandas phase before basic CS50P independence.
- No Andrew Ng ML before the Bohrium concept sequence and the AI-history claim-audit gate.
- No Andrew Ng DL before classical model recognition and baseline practice.
- No tuning before validation, model comparison, and error analysis.
- No stacking without out-of-fold predictions.
- No final readiness claim without a fresh-runtime competition simulation.

## Lesson Bank Policy

The repository contains 155 mainline lessons and 16 Bohrium resource lessons. Use extra files for remediation, deeper practice, alternative modalities, or extension; do not schedule all 171 files automatically.
""",
)

sessions = [
    (1, "Course orientation and competition map"),
    (2, "Evidence, GitHub, notebook, and responsible-AI workflow"),
    (3, "CS50P: functions, variables, input, and output"),
    (4, "CS50P: conditionals and Boolean reasoning"),
    (5, "CS50P: loops and iteration"),
    (6, "CS50P: exceptions, debugging, and defensive input"),
    (7, "CS50P: libraries and documentation"),
    (8, "CS50P: unit tests and assertions"),
    (9, "CS50P: file I/O and CSV processing"),
    (10, "CS50P: regular expressions and text processing"),
    (11, "CS50P: classes and data-oriented objects"),
    (12, "CS50P independent data-processing mini-project"),
    (13, "NumPy arrays, shapes, dtypes, and indexing"),
    (14, "NumPy vectorisation and broadcasting"),
    (15, "Pandas DataFrames and schema inspection"),
    (16, "Pandas filtering, grouping, joins, and missingness"),
    (17, "Matplotlib and question-driven plots"),
    (18, "Data-tools mini-project and phase gate"),
]

bohrium_titles = [
    "Bohrium: course map and evidence",
    "Bohrium: definitions and boundaries of AI",
    "Bohrium: AI history and schools",
    "Bohrium: connectionism and machine learning",
    "Bohrium: object-oriented programming, libraries, and scikit-learn",
    "Bohrium: the training paradigm",
    "Bohrium: classification and logistic regression",
    "Bohrium: optimisation theory",
    "Bohrium: neural networks and backpropagation",
    "Bohrium: KNN and Bayesian reasoning",
    "Bohrium: support vector machines and margin",
    "Bohrium: entropy, trees, and ensembles",
    "Bohrium: unsupervised learning and reinforcement learning",
    "Bohrium: deep neural networks and phase synthesis",
]
for n, title in enumerate(bohrium_titles, start=19):
    sessions.append((n, title))

for n, item in enumerate(LESSONS, start=33):
    sessions.append((n, f"AI History: {item['title']}"))

later = [
    "Andrew ML model-lab routine, task formalisation, and embedded Kaggle baseline",
    "Linear regression: prediction, cost, and gradient intuition",
    "Multivariable regression, scaling, and regression task",
    "Logistic regression, probability, threshold, and classification task",
    "Regularisation, bias, variance, and diagnostic evidence",
    "K-nearest neighbours, distance, scaling, and task recognition",
    "Decision trees, splitting, interpretability, and tabular task",
    "Random forests, bagging, variance, and comparison",
    "Boosting, sequential correction, and controlled experiment",
    "Support vector machines, margin, kernels, and limitations",
    "K-means clustering and unsupervised task recognition",
    "PCA, projection, variance, and dimensionality reduction",
    "Anomaly detection and threshold selection",
    "Recommender systems, similarity, and embeddings intuition",
    "Classical-model comparison under one validation protocol",
    "Embedded Kaggle tabular workflow: pipeline, baseline, and one improvement",
    "Mixed model-recognition cases and misconception correction",
    "Andrew ML synthesis, model cards, and phase gate",
    "Andrew DL: neural-network concepts and PyTorch tensors",
    "PyTorch modules, losses, forward pass, and complete training loop",
    "Optimisation, initialisation, regularisation, and learning curves",
    "CNN concepts and PyTorch image classification",
    "Transfer learning, augmentation, and image error analysis",
    "Sequence modelling, recurrence, and temporal tasks",
    "Embeddings, RNN/LSTM implementation, and text task",
    "Attention intuition and sequence-to-sequence reasoning",
    "Transformers and PyTorch implementation patterns",
    "Computer-vision domain task with baseline comparison",
    "NLP or audio domain task with baseline comparison",
    "Deep-learning synthesis, model card, and phase gate",
    "Model comparison: assumptions, strengths, costs, and limitations",
    "Systematic EDA, data quality, leakage, and distribution shift",
    "Feature engineering, pipelines, and ablation evidence",
    "Evaluation design, metrics, cross-validation, thresholds, and error analysis",
    "Diagnosis-first manual tuning",
    "Deep-learning tuning and compute-aware stopping",
    "Model ensembling with held-out or out-of-fold predictions",
    "Full competition simulation, fresh-runtime validation, and postmortem",
]
for n, title in enumerate(later, start=41):
    sessions.append((n, title))

sequence_lines = "\n".join(f"| {n} | {title} |" for n, title in sessions)
write(
    ROOT / "00_Course_Overview/Detailed_Lesson_Sequence.md",
    f"""# Detailed Lesson Sequence

**Canonical schedule:** 78 scheduled sessions

| Session | Focus |
|---:|---|
{sequence_lines}

## Phase 04 Reading Rule

Sessions 33–40 require pre-class reading from Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans*. The lesson files specify the reading range, required mastery, misconceptions, guided analysis, independent reconstruction, and exit evidence.

## Kaggle Rule

Kaggle Learn is embedded inside the Andrew Ng Machine Learning model labs rather than scheduled as a separate phase. Students use selected exercises to rehearse Pandas, validation, pipelines, leakage prevention, and typical tabular workflows at the moment those skills become useful.

## Completion Rule

Finishing an external course or reading assignment is not mastery. Students advance through evidence: task recognition, explanation, independent reconstruction, controlled implementation, error analysis, and reproducible execution.
""",
)

write(
    ROOT / "README.md",
    """# NOAI / IOAI Preparation Curriculum

A mastery-focused curriculum for secondary-school students preparing for NOAI China and later IOAI-style open-ended artificial-intelligence tasks.

## Canonical Learning Path

```text
CS50P Python
→ NumPy, Pandas, and visualisation
→ 北京市十一学校《中学机器学习十五讲》 on Bohrium
→ AI history and critical reading through
   Melanie Mitchell, Artificial Intelligence: A Guide for Thinking Humans
→ Andrew Ng Machine Learning Specialization
   + StatQuest
   + 3Blue1Brown
   + embedded Kaggle practice
   + model-recognition drills
   + typical model tasks
→ Andrew Ng Deep Learning Specialization
   + PyTorch
   + image, text, audio, and multimodal tasks
→ model comparison
→ EDA and data quality
→ feature engineering
→ model evaluation and error analysis
→ tuning
→ model ensembling
→ full competition simulation
```

## Curriculum Layers

| Layer | Count | Purpose |
|---|---:|---|
| Canonical scheduled pathway | 78 sessions | actual recommended learning order |
| Mainline lesson bank | 155 lessons | deeper practice, remediation, alternatives, and domain extension |
| Bohrium resource bank | 16 lessons | resource-hub missions and the fourteen-session Chinese foundation sequence |
| Total public lesson/resource files | 171 | selectable material, not a requirement to schedule everything |

## Start Here

- [Students](STUDENT_START_HERE.md)
- [Teachers](TEACHER_START_HERE.md)
- [Class Missions canonical pathway](02_Class_Missions/README.md)
- [Detailed 78-session sequence](00_Course_Overview/Detailed_Lesson_Sequence.md)
- [Course map](00_Course_Overview/Course_Map.md)
- [Pacing guide](00_Course_Overview/Pacing_Guide.md)

## Evidence Standard

Watching a video, finishing a chapter, or running supplied code is not mastery. Students must recognise, explain, reconstruct, debug, apply, analyse errors, and produce reproducible evidence.

## Licensing

Educational materials are copyright © 2026 Wang Morgan. All Rights Reserved. Source-code examples are licensed under the MIT License. See [LICENSE.md](LICENSE.md).
""",
)

write(
    ROOT / "TEACHER_START_HERE.md",
    """# Teacher Start Here

## Canonical Route

Teach the numbered folders in `02_Class_Missions/` in order. The full pathway contains 78 sessions.

1. Orientation and evidence — Sessions 1–2
2. CS50P Python — Sessions 3–12
3. NumPy, Pandas, and visualisation — Sessions 13–18
4. Bohrium ML foundations — Sessions 19–32
5. AI History and Thinking Humans — Sessions 33–40
6. Andrew Ng ML model labs — Sessions 41–58
7. Andrew Ng DL and PyTorch — Sessions 59–70
8. Model comparison, EDA, and evaluation — Sessions 71–74
9. Tuning, ensembling, and competition — Sessions 75–78

## Phase 04 Preparation

Students need legal access to Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans*. Assign the stated reading before class. Do not spend the full lesson silently reading and then remove the learning cycle. Each seminar checks retrieval, argument structure, evidence quality, claim boundaries, and independent reconstruction.

## External Resource Roles

- CS50P is the Python spine.
- Bohrium provides the pre-Andrew Chinese machine-learning concept sequence.
- Melanie Mitchell provides AI history, conceptual boundaries, and claim-audit practice.
- Andrew Ng Machine Learning is the classical-model spine.
- Kaggle Learn is embedded practical rehearsal inside the model labs.
- StatQuest and 3Blue1Brown are selected just-in-time explanations.
- Andrew Ng Deep Learning and PyTorch are paired concept and implementation spines.

## Before Each Cohort

Verify external-course access, the exact student runtime, current competition rules, private assessment security, and representative lesson timing. Automated checks establish repository consistency, not complete classroom readiness.
""",
)

write(
    ROOT / "STUDENT_START_HERE.md",
    """# Student Start Here

You will follow one learning path rather than opening every file in the repository.

```text
CS50P Python
→ NumPy / Pandas / visualisation
→ Bohrium ML foundations
→ AI history and critical reading
→ Andrew Ng ML + embedded Kaggle practice + model tasks
→ Andrew Ng DL + PyTorch
→ comparison, EDA, evaluation, tuning, and competition
```

## Reading Evidence

For Sessions 33–40, read the assigned part of Melanie Mitchell’s *Artificial Intelligence: A Guide for Thinking Humans* before class. Bring:

- one central claim;
- one supporting case;
- one unresolved question;
- one AI claim that should be tested rather than accepted immediately.

A chapter summary is not enough. You must separate the author’s argument, the evidence, and your own judgement.

## Mastery Rule

Watching, reading, or running code is not the finish line. You must explain the idea, reconstruct it independently, apply it to a new case, analyse errors, and submit evidence.
""",
)

# Shift later phase labels and embed Kaggle in Andrew ML.
replace(
    MISSIONS / "05_Andrew_Ng_ML_Model_Labs/README.md",
    [
        ("**Scheduled sessions:** 38–55", "**Scheduled sessions:** 41–58"),
        ("Sessions 38–55", "Sessions 41–58"),
    ],
)
andrew_readme = MISSIONS / "05_Andrew_Ng_ML_Model_Labs/README.md"
text = andrew_readme.read_text(encoding="utf-8")
if "## Embedded Kaggle Practice" not in text:
    text += """

## Embedded Kaggle Practice

Kaggle Learn is used inside the model labs rather than as a separate phase. Selected exercises provide short practical rehearsals of Pandas, train/validation splits, decision-tree baselines, missing-value handling, categorical encoding, pipelines, cross-validation, and leakage prevention. Every Kaggle activity must serve the model currently being learned and produce baseline, validation, and error-analysis evidence.

See [Kaggle Learn Refresh Map](../../05_Resources/Kaggle_Learn_Refresh_Map.md).
"""
    andrew_readme.write_text(text, encoding="utf-8")

for path, pairs in [
    (MISSIONS / "06_Andrew_Ng_DL_PyTorch/README.md", [("56–67", "59–70"), ("Sessions 56–67", "Sessions 59–70")]),
    (MISSIONS / "07_Model_Comparison_EDA_Evaluation/README.md", [("68–71", "71–74"), ("Sessions 68–71", "Sessions 71–74")]),
    (MISSIONS / "08_Tuning_Ensembling_Competition/README.md", [("72–75", "75–78"), ("Sessions 72–75", "Sessions 75–78")]),
]:
    replace(path, pairs)

# Update overview and operational documents without disturbing the lesson bank.
targets = [
    ROOT / "00_Course_Overview/README.md",
    ROOT / "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md",
    ROOT / "10_Ready_to_Teach_Pack/README.md",
    ROOT / "10_Ready_to_Teach_Pack/Curriculum_Readiness_Audit.md",
    ROOT / "MANIFEST.md",
    ROOT / "09_Teacher_Planning/README.md",
]
common = [
    ("75-session", "78-session"),
    ("75 sessions", "78 sessions"),
    ("Sessions 33–37", "Sessions 33–40"),
    ("Sessions 38–55", "Sessions 41–58"),
    ("Sessions 56–67", "Sessions 59–70"),
    ("Sessions 68–71", "Sessions 71–74"),
    ("Sessions 72–75", "Sessions 75–78"),
    ("33–37", "33–40"),
    ("38–55", "41–58"),
    ("56–67", "59–70"),
    ("68–71", "71–74"),
    ("72–75", "75–78"),
    ("Kaggle ML refresh", "AI History and Thinking Humans"),
    ("Kaggle machine-learning workflow refresh", "AI history and critical-reading sequence"),
    ("selected Kaggle Learn workflow refresh", "eight-session AI history and critical-reading sequence"),
]
for target in targets:
    replace(target, common)

# Make resource-role language explicit where the old standalone Kaggle phase appeared.
for target in [ROOT / "00_Course_Overview/Cohort_Pathways_and_Required_Optional_Map.md", ROOT / "10_Ready_to_Teach_Pack/README.md"]:
    if target.exists():
        text = target.read_text(encoding="utf-8")
        text = text.replace("| Kaggle Learn | required short workflow refresh |", "| Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* | required eight-session AI history and claim-audit sequence |\n| Kaggle Learn | selected embedded practice within Andrew Ng ML model labs |")
        target.write_text(text, encoding="utf-8")

# Update the structural validator to require the new phase and 78-session markers.
validator = ROOT / "scripts/validate_curriculum_structure.py"
text = validator.read_text(encoding="utf-8")
old_required = '    "02_Class_Missions/04_Kaggle_ML_Refresh/README.md",'
new_required = '\n'.join([
    '    "02_Class_Missions/04_AI_History_and_Thinking_Humans/README.md",',
    *[f'    "02_Class_Missions/04_AI_History_and_Thinking_Humans/{item["file"]}",' for item in LESSONS],
])
text = text.replace(old_required, new_required)
text = text.replace('(\"75 sessions\", \"155 lessons\", \"Competition sprint\")', '(\"78 sessions\", \"155 lessons\", \"Competition sprint\")')
text = text.replace('(\"75 sessions\", \"155 lessons\", \"70-Minute Bohrium Exception\")', '(\"78 sessions\", \"155 lessons\", \"70-Minute Bohrium Exception\")')
text = text.replace('(\"75 scheduled sessions\", \"Phase 8 — Tuning, Ensembling, and Competition\")', '(\"78 scheduled sessions\", \"Phase 8 — Tuning, Ensembling, and Competition\")')
text = text.replace('(\"Phase\", \"72–75\", \"155 mainline lesson files\", \"16 Bohrium resource lessons\")', '(\"Phase\", \"75–78\", \"155 mainline lesson files\", \"16 Bohrium resource lessons\")')
text = text.replace('(\"CS50P\", \"Bohrium\", \"Andrew Ng Machine Learning\", \"Andrew Ng Deep Learning\", \"Model Comparison\")', '(\"CS50P\", \"Bohrium\", \"AI History\", \"Andrew Ng Machine Learning\", \"Andrew Ng Deep Learning\", \"Model Comparison\")')
validator.write_text(text, encoding="utf-8")

# Keep the Kaggle resource map, but clarify its new embedded role.
kaggle_map = ROOT / "05_Resources/Kaggle_Learn_Refresh_Map.md"
if kaggle_map.exists():
    text = kaggle_map.read_text(encoding="utf-8")
    text = text.replace("# Kaggle Learn Refresh Map", "# Kaggle Learn Embedded Practice Map")
    if "not a separate scheduled phase" not in text:
        text = text.replace("\n", "\n\nKaggle Learn is not a separate scheduled phase. The selected material is embedded in Andrew Ng Machine Learning model labs when students need workflow rehearsal.\n", 1)
    kaggle_map.write_text(text, encoding="utf-8")

print("AI History phase created; pathway updated to 78 sessions.")
