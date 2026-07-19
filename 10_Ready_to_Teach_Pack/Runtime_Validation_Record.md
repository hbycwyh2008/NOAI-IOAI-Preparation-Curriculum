# Runtime Validation Record

**Validation date:** 2026-07-19  
**Curriculum commit tested:** `b56dc2d22b4fe240d06d055917d4465594d8e016`  
**Method:** each starter notebook was executed from a fresh Jupyter kernel with cells run in order; assertions were enabled and manual notebook state was not reused.

## Environment

- Python: `3.13.5`
- Platform: `Linux x86_64`
- NumPy: `2.3.5`
- Pandas: `2.2.3`
- Matplotlib: `3.10.8`
- scikit-learn: `1.8.0`
- PyTorch: `2.10.0+cpu`
- torchvision: `0.25.0+cpu`
- torchaudio: `2.10.0+cpu`
- OpenCV: `4.13.0`
- librosa: `0.11.0`
- nbformat: `5.10.4`
- nbclient: `0.10.4`

## Notebook results

| ID | Notebook | Result |
|---|---|---|
| N01 | `python_trace_and_debug.ipynb` | PASS |
| N02 | `statistics_and_metrics.ipynb` | PASS |
| N03 | `linear_logistic_models.ipynb` | PASS |
| N04 | `trees_and_ensembles.ipynb` | PASS |
| N05 | `numpy_pandas_audit.ipynb` | PASS |
| N06 | `sklearn_mixed_pipeline.ipynb` | PASS |
| N07 | `pytorch_mlp.ipynb` | PASS |
| N08 | `opencv_structural_baseline.ipynb` | PASS |
| N09 | `cnn_transfer_learning.ipynb` | PASS after reducing the CPU workload and removing an unnecessary torchvision architecture construction |
| N10 | `text_baseline_and_lstm.ipynb` | PASS after setting one PyTorch thread and using a compact instructional dataset |
| N11 | `audio_mel_classifier.ipynb` | PASS |
| N12 | `local_llm_multimodal.ipynb` | PASS without local model assets; the asset-manifest and structured-output smoke tests passed |

## Acceptance result

All twelve notebook implementations execute without a network download and are suitable for CPU-based instructional smoke testing. The supplied GitHub Actions workflow regenerates and re-executes the notebooks in a clean runner.

## Remaining environment-specific verification

This record does not claim that a particular Bohrium classroom image has been tested. Before the cohort begins, run the same workflow in the exact student image and record:

- Python and package versions;
- GPU model, memory, and driver when used;
- available storage and runtime limits;
- locally cached Qwen/pretrained assets and hashes;
- organiser restrictions on packages, internet, APIs, and models.
