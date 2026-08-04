# Level 3 — Competition and Multimodal Scenarios

For every scenario, include the validation design, leakage risk, runtime constraint, and submission-output check in addition to the standard answer format.

### Day 25 — Multimodal truth check
Each sample contains an image, a caption, and a binary label indicating whether the caption accurately describes the image. The competition supplies train labels and requires a probability for each test sample. Compare text-only, image-only, and fusion baselines.

### Day 26 — Audio event classification
Audio clips are labelled with one of eight environmental sound classes. Several clips come from the same original recording device and location. The evaluation set contains new locations.

### Day 27 — Scientific parameter estimation
A simulation generates curves from three hidden continuous physical parameters. Training samples include the curve and the three parameter values. Predict all three parameters for each test curve.

### Day 28 — Document question answering
Each sample contains a document image and a question. The required output is a short text answer. Training data contains accepted answers, but exact string matching may penalise equivalent wording.

### Day 29 — Image retrieval
The test system gives one query image and a gallery of candidate images. The output is an ordered list of gallery IDs, and visually related items should appear near the top.

### Day 30 — Segmentation with limited labels
A small set of satellite images has pixel-level flood masks; a much larger set is unlabelled. The submission requires one binary mask per test image.

### Day 31 — Tabular competition shift
The train set contains labelled transactions from January through September; the test set contains October and November. Customer IDs repeat over time, and several aggregate features can accidentally include future information.

### Day 32 — Language generation scoring
Given a structured record, the system must produce a concise natural-language explanation. Evaluation combines schema compliance, factual consistency, and a semantic similarity score. Hallucinated facts are heavily penalised.

### Day 33 — Local-model constraint
A task allows only organiser-provided local model files and forbids internet access. The model must classify text into five classes under a strict memory and runtime budget. State the simplest offline baseline before proposing use of the supplied model.

### Day 34 — Continuation task
An at-home round supplied a baseline, training data, and a validation protocol. Contest 1 adds new constraints and asks for a controlled improvement. Explain what must remain fixed for a fair comparison and what evidence is required before changing the model family.

### Day 35 — Novel task under time pressure
Contest 2 presents an unfamiliar dataset with hidden test labels and a four-hour limit. You have 30 minutes to produce the first valid submission. Define the sequence from task contract to baseline, validation, output validation, and first diagnostic.

### Day 36 — Ensemble decision
Three models have similar overall scores but make different errors across sources and classes. You have out-of-fold predictions and a fixed validation design. Decide what evidence is needed before averaging, weighting, or stacking, and identify leakage risks.
