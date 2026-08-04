# Student Runtime Qualification Record

**Status: NOT QUALIFIED until this record is completed for a named cohort, exact commit, and exact student environment.**

GitHub Actions proves that maintained repository assets run on its declared runner. It does not prove that a student device, Bohrium workspace, school network, regional package mirror, account permission, or competition runtime works. Do not copy CI results into the cohort fields without performing the named tests.

## Environment Identity

| Field | Record |
|---|---|
| Curriculum commit | REQUIRED |
| Cohort | REQUIRED |
| Verification date | REQUIRED |
| Platform | local / Bohrium / JupyterHub / Colab / other |
| Operating system | REQUIRED |
| Python version | REQUIRED |
| CPU | REQUIRED |
| RAM | REQUIRED |
| GPU and driver | n/a or exact record |
| Storage available | REQUIRED |
| Internet restrictions | REQUIRED |
| Package-install permission | REQUIRED |
| Tested by | REQUIRED |
| Reviewed by | REQUIRED |

## Dependency Qualification

| Component | Required version/range | Installed version | Clean install succeeds | Import succeeds | Representative task passes | Notes |
|---|---|---|---|---|---|---|
| Python | | | | | | |
| Jupyter / kernel | | | | | | |
| NumPy | | | | | | |
| Pandas | | | | | | |
| Matplotlib | | | | | | |
| scikit-learn | | | | | | |
| PyTorch | | | | | | |
| torchvision | | | | | | |
| Optuna | | | | | | |
| project-specific packages | | | | | | |

## Representative Execution Tests

- [ ] setup instructions work from a clean student account;
- [ ] CSV/data path handling works on the target operating system;
- [ ] one NumPy/Pandas notebook executes from a fresh kernel;
- [ ] one scikit-learn pipeline trains, validates, serialises, and reloads;
- [ ] one PyTorch training loop completes on the target hardware;
- [ ] CPU fallback works when GPU is unavailable;
- [ ] one authorised data-download or offline-data procedure works;
- [ ] one submission file is generated and validated;
- [ ] Chinese and English file paths do not break execution;
- [ ] memory and runtime remain within practical classroom limits;
- [ ] networking-disabled execution works when the competition requires it;
- [ ] organiser-provided local model/assets can be loaded exactly as documented.

## Performance Record

| Task | Dataset size | Hardware | Runtime | Peak memory | Pass/fail | Classroom implication |
|---|---:|---|---:|---:|---|---|
| data audit | | | | | | |
| classical baseline | | | | | | |
| PyTorch training loop | | | | | | |
| competition submission generation | | | | | | |

## Known Limitations and Workarounds

Record blocked packages, long downloads, unavailable GPU features, regional access issues, storage limits, required pre-caching, file-path restrictions, account quotas, and the exact tested workaround.

## Qualification Decision

- [ ] **Qualified** for the named cohort, commit, platform, hardware, and network.
- [ ] **Conditionally qualified** with documented and tested workarounds.
- [ ] **Not qualified**; blocking issues remain.

Decision rationale:

Reviewer signature/date:

A new qualification record is required after material changes to Python, dependencies, notebooks, hardware, hosted runtime, account permissions, network policy, local assets, or competition constraints.
