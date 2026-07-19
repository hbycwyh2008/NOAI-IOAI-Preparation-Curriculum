# Hidden Mock Generation and Sealing Protocol

Hidden labels, target-generation code, reference predictions, and scoring secrets must never be committed to the public curriculum repository.

## Separation model

- **Student repository:** task statement, visible train labels, test inputs, sample submission, baseline scaffold, public validator.
- **Private teacher package:** generation seed, target formula, hidden labels, reference scores, scoring script, hidden tests, release log.

## Generate immediately before use

For each scored mock:

1. choose a new high-entropy seed;
2. generate train/test inputs and hidden labels in the private teacher environment;
3. export only permitted student files;
4. run the reference baseline and scoring script;
5. validate row count, ID uniqueness/order, column names, dtypes, ranges, and finite values;
6. compute SHA-256 hashes for every distributed and hidden file;
7. archive the seed and hashes in the private release record;
8. distribute student files through a channel that does not expose the private package.

## Release record template

```text
Mock name:
Curriculum commit:
Teacher-key version:
Generated UTC time:
Generator version/hash:
Secret seed location:
Student package hashes:
Hidden-label hash:
Scoring-script hash:
Reference baseline score:
Validator result:
Distributed by:
```

## Required checks

- train and test IDs do not overlap unless the task explicitly requires repeated entities;
- hidden labels are absent from filenames, metadata, notebook outputs, and Git history;
- the public validator checks schema only and cannot reconstruct labels;
- the scoring script uses the official metric and tested edge-case policy;
- source/group leakage is tested;
- a constant and simple baseline produce plausible scores;
- the hidden set contains difficult and distribution-shift slices;
- the final student package can be opened without access to the private directory.

## After the mock

- preserve submissions and score records privately;
- publish only the intended solution discussion and de-identified aggregate analysis;
- rotate the seed and regenerate before reusing a task as a scored assessment;
- never reuse the same hidden test for practice and formal scoring.
