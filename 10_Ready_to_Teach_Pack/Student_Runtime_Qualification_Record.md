# Student Runtime Qualification Record

Complete this record for the exact environment used by a named cohort. GitHub Actions success does not replace student-device validation.

## Environment Identity

| Field | Record |
|---|---|
| Curriculum commit | |
| Cohort | |
| Verification date | |
| Platform | local / Bohrium / JupyterHub / Colab / other |
| Operating system | |
| Python version | |
| CPU | |
| RAM | |
| GPU and driver | |
| Storage available | |
| Internet restrictions | |
| Package-install permission | |
| Tested by | |
| Reviewed by | |

## Dependency Qualification

| Component | Required version or range | Installed version | Install succeeds from clean environment | Import succeeds | Representative task passes | Notes |
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
- [ ] one data download or offline-data procedure works;
- [ ] one submission file is generated and validated;
- [ ] Chinese and English file paths do not break execution;
- [ ] memory and runtime remain within practical classroom limits.

## Performance Record

| Task | Dataset size | Hardware | Runtime | Peak memory | Pass/fail | Classroom implication |
|---|---:|---|---:|---:|---|---|
| data audit | | | | | | |
| classical baseline | | | | | | |
| PyTorch training loop | | | | | | |
| competition submission generation | | | | | | |

## Known Limitations and Workarounds

Record blocked packages, long downloads, unavailable GPU features, regional access issues, storage limits, or required pre-caching.

## Qualification Decision

- [ ] **Qualified** for the named cohort and commit.
- [ ] **Conditionally qualified** with documented workarounds.
- [ ] **Not qualified**; blocking issues remain.

A new qualification record is required after material changes to Python, dependencies, hardware, hosted runtime, or competition constraints.
