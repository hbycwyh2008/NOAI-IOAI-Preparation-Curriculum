# Phase 6B — NLP, Audio, LLMs, and Multimodality

Sessions 51–57. Standard duration: 90 minutes.

---

## Session 51 — Tokenisation, Vocabulary, Padding, and Embeddings

### Resource segment

Hugging Face LLM Course: **Transformer models**, **Using tokenizers**, and **Handling multiple sequences**; teacher comparison with word-level tokenisation.

### Essential teaching content

- Tokenisation converts text into model-readable IDs; tokens are not necessarily words.
- A vocabulary maps token strings to integer IDs.
- Unknown-token handling differs between fixed word vocabularies and subword tokenizers.
- Batches require padding and attention masks; truncation can remove task-critical information.
- Embeddings map discrete IDs to learned dense vectors.
- Padding IDs must not be interpreted as ordinary content.

### Entry check

1. Why can one English word become multiple tokens?
2. What is the difference between token ID and embedding vector?
3. Why is an attention mask needed?

### Worksheet

1. Build a word-level vocabulary for four short sentences with `<PAD>` and `<UNK>`.
2. Convert one sentence to IDs.
3. Pad three sequences to a common length and write the attention masks.
4. State the batch shape when batch size is 8, sequence length 40, embedding dimension 64.
5. Explain one risk of truncating from the right.
6. Compare word, character, and subword tokenisation.
7. Identify data leakage in fitting a vocabulary using labels or test-only text statistics.
8. Explain why pretrained tokenizer and model must match.

### Guided practice

Students implement a small tokenizer/vocabulary/padding pipeline, then compare it with a pretrained subword tokenizer on names, numbers, punctuation, and unknown words.

### Independent task

Create a reusable batch-collation function returning padded IDs, lengths/attention masks, and labels. Test empty, long, and unknown-token cases.

### Exit ticket

Trace one sentence from raw text to model-ready batch tensors.

---

## Session 52 — RNN and LSTM Sequence Modelling

### Resource segment

Deep Learning Specialization sequence-model introduction; PyTorch sequence-model examples for RNN/LSTM inputs and hidden states.

### Essential teaching content

- An RNN updates a hidden state sequentially, sharing parameters across time.
- Vanilla RNNs struggle with long-range dependencies because gradients can vanish/explode.
- LSTM gates control what is written, retained, and exposed through cell/hidden states.
- Input/output shape depends on `batch_first`, layers, directions, and hidden size.
- Final-state classification is not always ideal; pooling or attention can use all time steps.

### Worksheet

1. Label input, hidden state, recurrent transition, and output in an unrolled RNN.
2. State the output shape for batch-first input `(32,50,64)` into an LSTM with hidden size 128.
3. State hidden/cell shapes for two layers, one direction.
4. Explain vanishing gradients without using only the phrase “the model forgets.”
5. Give the roles of input, forget, and output gates.
6. Explain why sequence lengths and padding matter.
7. Compare final hidden state, mean pooling, and max pooling for classification.
8. Identify one task where order matters and one bag-of-words baseline may suffice.

### Guided practice

Build a small embedding–LSTM–classifier model. Students maintain a shape ledger and inspect hidden states for batches with different padded lengths.

### Independent task

Compare a simple bag-of-words/logistic baseline with an LSTM using the same split and metric. Explain whether sequence modelling added value.

### Exit ticket

Explain the data flow through embedding, LSTM, pooled representation, and classifier.

---

## Session 53 — Hugging Face Text Classification and Fine-Tuning

### Resource segment

Hugging Face LLM Course: **Fine-tuning a model with the Trainer API or a full training loop**, focusing on sequence classification.

### Essential teaching content

- Match task, tokenizer, model checkpoint, label mapping, and number of labels.
- Tokenize batched text with truncation and dynamic padding where appropriate.
- Fine-tuning updates pretrained parameters for the task; feature extraction freezes them.
- Metrics must be calculated from logits and labels correctly.
- Shortcuts such as source names, templated text, or duplicated passages can create leakage.

### Worksheet

1. List the minimum fields required for a text-classification dataset.
2. Explain `AutoTokenizer` and `AutoModelForSequenceClassification`.
3. Convert logits to predicted classes.
4. State why label-to-ID and ID-to-label mappings should be saved.
5. Compare static maximum-length padding with dynamic padding.
6. Identify leakage through duplicate articles across train/validation.
7. Design an error slice by length, class, negation, or rare tokens.
8. Explain why a pretrained model may underperform a simple baseline on tiny/noisy data.

### Guided practice

Fine-tune a compact checkpoint for a short budget, then compare against TF-IDF + logistic regression. Record runtime, macro F1, class recall, and five disagreements.

### Independent task

Rebuild the inference pipeline from saved checkpoint/tokenizer. It must accept a list of texts and return labels, probabilities, and truncation warnings.

### Exit ticket

Explain one example where the transformer and baseline disagree and which evidence is needed to judge it.

---

## Session 54 — Waveforms, Sample Rates, Spectrograms, and Mel Features

### Resource segment

Hugging Face Audio Course: **Introduction to audio data**, **Preprocessing audio datasets**, and spectrogram/Mel-feature sections.

### Essential teaching content

- A waveform is amplitude over sampled time.
- Sample rate determines samples per second and limits representable frequency.
- Resampling must be consistent across train, validation, and inference.
- STFT produces time–frequency representations; window/hop length trade temporal and frequency resolution.
- Mel scaling approximates human pitch resolution; log-Mel features compress dynamic range.
- Duration, silence, clipping, channel count, and recording source can become shortcuts.

### Worksheet

1. How many samples are in 2.5 seconds at 16 kHz?
2. What happens to duration if 32,000 samples are interpreted at 8 kHz rather than 16 kHz?
3. Explain time-domain waveform versus spectrogram.
4. Predict the effect of a larger hop length.
5. Why are Mel bins not equally spaced in Hertz?
6. List four audio audit checks.
7. Identify leakage if synthetic and real audio come from different file formats or sample rates.
8. Explain why padding long silence may mislead a classifier.

### Guided practice

Load clips, inspect waveform/duration/sample rate, resample, trim/pad deliberately, and plot linear and log-Mel spectrograms. Students connect every visual change to a parameter.

### Independent task

Write `audit_audio_folder` to report sample-rate distribution, duration quantiles, clipping rate, channel counts, and unreadable files.

### Exit ticket

Given a Mel spectrogram, identify axes and name one pattern that could be a recording artifact rather than class information.

---

## Session 55 — Audio Classification, ASR, and TTS Workflows

### Resource segment

Hugging Face Audio Course: **Audio classification**, **Automatic speech recognition**, and **Text-to-speech** overview modules.

### Essential teaching content

- Audio classification predicts clip/segment labels; ASR maps speech to text; TTS maps text to speech.
- Classification can use engineered Mel-image baselines or pretrained audio encoders.
- ASR evaluation commonly uses word/character error rates; label text normalisation affects scores.
- Speaker/source leakage is critical: split by speaker, recording, or source when needed.
- Synthetic-speech detection may accidentally learn codec, silence, language, or generator fingerprints.

### Worksheet

1. Match four tasks to classification, ASR, or TTS.
2. Why is a random clip-level split invalid when the same speaker appears in both sets?
3. Define false positive and false negative for synthetic-speech detection.
4. Explain one Mel-image CNN baseline.
5. What does word error rate compare conceptually?
6. Why must reference and predicted text be normalised consistently?
7. List five shortcut risks in real-versus-synthetic audio.
8. Design an error analysis by speaker, duration, language, noise, and confidence.

### Guided practice

Build a log-Mel classifier baseline and audit performance by source. Then run a pretrained ASR pipeline on a few clips and compare transcription errors.

### Independent task

Create an audio-classification report containing source-aware split, baseline, threshold, confusion matrix, duration/source slices, and 10 reviewed errors.

### Exit ticket

Explain why a high random-split score may collapse under a speaker-held-out split.

---

## Session 56 — LLM Tokens, Next-Token Prediction, Prompting, and APIs

### Resource segment

Hugging Face LLM Course: introductory transformer/causal-language-model sections; current official API documentation selected by the teacher.

### Essential teaching content

- A causal language model estimates the next-token distribution conditioned on prior tokens.
- Sampling settings such as temperature and top-p alter output diversity, not factuality guarantees.
- A prompt defines context, instructions, examples, and requested output schema.
- Reliable API use requires environment variables, error handling, retries, timeouts, logging, and output validation.
- LLM outputs are untrusted data; never execute generated code or accept claims without verification.
- Competition rules may restrict network/API access, model size, or provided checkpoints.

### Worksheet

1. Explain next-token prediction without saying “the model searches the internet.”
2. Distinguish context window, token, prompt, completion, and system instruction.
3. Predict the qualitative effect of low versus high temperature.
4. Rewrite a vague prompt as role/task/input/constraints/output-schema instructions.
5. Why should API keys use environment variables?
6. Design JSON-schema checks for a model returning class, confidence, and reason.
7. List four hallucination/robustness checks.
8. Explain prompt injection in a document-processing task.

### Guided practice

Students call an approved model or use a teacher-supplied offline response simulator. They require strict JSON, validate it, handle malformed output, and compare deterministic versus sampled settings.

### Independent task

Build an LLM-assisted classifier or extractor with input sanitisation, structured output validation, retry limit, logs, and a non-LLM fallback.

### Exit ticket

Name one thing a lower temperature can improve and one thing it cannot guarantee.

---

## Session 57 — Qwen Local Inference, Multimodality, and Responsible Offline Use

### Resource segment

Current official Qwen/Hugging Face model documentation chosen immediately before teaching; NOAI annual rules and FAQ; IOAI Academy multimodal and competition-strategy resources.

### Essential teaching content

- Local inference workflow: obtain an allowed checkpoint before the offline event, load tokenizer/processor/model, select device/dtype, control memory, run inference, validate outputs, and cache only permitted assets.
- Quantisation can reduce memory but may change compatibility or quality.
- Multimodal models combine modality-specific processing with a shared generation/reasoning interface.
- Image/audio inputs require exact processor conventions.
- Offline readiness means no hidden download, login, API, model-hub, or package dependency during competition.
- Always defer to the current annual NOAI/IOAI rules on models, internet, packages, and pretrained assets.

### Worksheet

1. List every asset that must exist locally before an offline run.
2. Explain tokenizer/processor/model compatibility.
3. Estimate model-weight memory at 16-bit and 8-bit for a teacher-supplied parameter count.
4. Explain one benefit and one cost of quantisation.
5. Design a preflight test proving inference works with network disabled.
6. Identify three multimodal prompt/data alignment failures.
7. Create an allowed-assets manifest containing filename, version, checksum, source, and licence.
8. Explain why “it worked yesterday from the model hub” is not competition readiness.

### Guided practice

Run an allowed small local text or vision-language checkpoint, disable network access, restart the runtime, and reproduce inference from local files. Measure startup time and peak memory.

### Independent task

Produce an offline deployment package with environment lock, local-model path configuration, deterministic smoke test, sample input/output, failure messages, and rule-compliance checklist.

### Phase 6B exit gate

Students must prepare text/audio data correctly, build one sequence model and one transformer/audio baseline, perform source-aware error analysis, create validated structured LLM output, and demonstrate offline local-model execution without network dependence.