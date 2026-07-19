# Phase 6A — PyTorch and Computer Vision

Sessions 45–50. Standard duration: 90 minutes unless stated otherwise.

---

## Session 45 — Tensors, Devices, Shapes, and GPU Movement

### Resource segment

PyTorch Learn the Basics: **Tensors** and **Quickstart** sections on tensor creation, attributes, indexing, operations, and device movement.

### Essential teaching content

- A tensor has shape, dtype, device, and values.
- Batch-first image convention is normally `N × C × H × W`.
- Tensor operations require compatible shape, dtype, and device.
- `.to(device)` returns a tensor on the requested device; model and input must share a device.
- Converting tensors that require gradients directly to NumPy is unsafe; detach and move to CPU first.

### Entry check

1. State the difference between shape and dtype.
2. What does the first dimension usually mean in a training batch?
3. Why does a CUDA model fail on CPU input?

### Worksheet

1. State shape, dtype, and device for three supplied tensors.
2. Predict the output shape of `(32,10) @ (10,4)`.
3. Reshape 3,072 values into one RGB 32×32 image.
4. Explain `view`, `reshape`, `unsqueeze`, and `squeeze` in one sentence each.
5. Diagnose a mismatch between `float32` features and integer labels.
6. Write safe device-selection code using `torch.cuda.is_available()`.
7. Explain why `tensor.detach().cpu().numpy()` is used for analysis.
8. Identify whether broadcasting is valid for `(16,3,32,32)` plus `(1,3,1,1)`.

### Guided practice

Students predict every tensor shape in a mini image batch workflow before execution: create, permute, normalise, flatten, matrix multiply, and move to device.

### Independent task

Write a `describe_tensor` utility that reports shape, dtype, device, min/max, finite-value status, and gradient requirement. Test on CPU and, when available, GPU.

### Exit ticket

Cold diagnosis of one device mismatch and one incorrect reshape.

---

## Session 46 — Dataset, DataLoader, nn.Module, and Autograd

### Resource segment

PyTorch Learn the Basics: **Datasets & DataLoaders**, **Build the Neural Network**, and **Automatic Differentiation**.

### Essential teaching content

- `Dataset` defines length and item retrieval; `DataLoader` handles batching, shuffling, and parallel loading.
- `nn.Module` registers trainable layers and parameters.
- `forward` defines computation; call the module rather than calling `forward` directly.
- Autograd records operations on tensors requiring gradients.
- Gradients accumulate by default and must be cleared for standard mini-batch training.

### Worksheet

1. Explain the contract of `__len__` and `__getitem__`.
2. State why training data is often shuffled but validation data is not.
3. Predict the batch shapes for 64 grayscale 28×28 images and class labels.
4. Count parameters in a two-layer `nn.Module`.
5. Explain why layers assigned as module attributes are registered.
6. What happens if `optimizer.zero_grad()` is omitted?
7. Distinguish `requires_grad`, `.grad`, and `torch.no_grad()`.
8. Complete a custom dataset that returns `(features, label)`.

### Guided practice

Build a small tabular dataset class, loader, and MLP. Pause after each object and inspect one batch, parameter names, and output shape.

### Independent task

Rebuild the dataset/loader/model from an empty file. Add assertions for batch dimensions, label dtype, output class count, and finite values.

### Exit ticket

Explain the complete path from one dataset row to one model output.

---

## Session 47 — Training, Validation, Checkpoints, and Mixed Precision

### Resource segment

PyTorch Learn the Basics: **Optimizing Model Parameters** and **Save & Load the Model**; PyTorch AMP examples.

### Essential teaching content

Training loop order:

1. `model.train()`;
2. move batch to device;
3. clear gradients;
4. forward pass;
5. loss calculation;
6. backward pass;
7. optimizer step;
8. accumulate detached statistics.

Validation uses `model.eval()` and `torch.no_grad()`. Save the best validation checkpoint, not merely the final epoch. Automatic mixed precision can reduce memory/time on supported GPUs but requires correct scaler/autocast use.

### Worksheet

1. Put eight training operations in order.
2. Explain why validation must not call `backward()`.
3. Why can dropout produce different results in train and eval modes?
4. Complete a best-checkpoint condition.
5. State what belongs in a checkpoint for resuming training.
6. Explain epoch loss weighting when final batch size differs.
7. Identify two signs of exploding gradients or unstable training.
8. Explain one benefit and one risk of mixed precision.

### Guided practice

Complete a partially written train/validate loop, then deliberately introduce three errors: missing eval mode, failure to clear gradients, and saving the last rather than best model.

### Independent task

Rebuild a complete loop from memory, restart the runtime, reload the best checkpoint, and reproduce the validation metric within a stated tolerance.

### Exit ticket

The teacher points to any line in the loop; the student explains its state-changing effect.

---

## Session 48 — OpenCV Preprocessing and Traditional Vision Baselines

### Resource segment

OpenCV University free-course modules: image reading, colour spaces, thresholding, filtering, edges, morphology, contours, and Hough transforms.

### Essential teaching content

- Images may load as BGR rather than RGB.
- Resize, crop, colour conversion, normalisation, and interpolation choices affect information.
- Thresholding and morphology can solve structured tasks without deep learning.
- Edges, contours, connected components, and Hough lines exploit geometric structure.
- A traditional baseline is valuable when data are small, labels weak, or task rules are visible.

### Worksheet

1. Explain BGR versus RGB and one symptom of confusion.
2. Choose nearest, bilinear, or area-style interpolation for three resizing situations.
3. Distinguish erosion, dilation, opening, and closing.
4. Explain global versus adaptive thresholding.
5. Select contours, connected components, or Hough lines for three tasks.
6. State what information a grayscale conversion may discard.
7. Design a pipeline for counting dark circular objects on a light background.
8. Identify three parameters that must be validated rather than guessed.

### Guided practice

Students build a classical pipeline on synthetic grid images: grayscale → threshold → morphology → connected components → count/measure. They record the effect of one parameter at a time.

### Independent task

Solve a second image task using only OpenCV/NumPy. Submit intermediate images and an explanation of why each transformation is necessary.

### Exit ticket

Given a failed segmentation image, propose the next diagnostic—not merely another random parameter.

---

## Session 49 — CNN Baseline, Augmentation, and Transfer Learning

### Resource segment

PyTorch transfer-learning tutorial; torchvision transforms and model documentation.

### Essential teaching content

- Establish a small CNN baseline before transfer learning.
- Augmentation must preserve labels and approximate plausible variation.
- Training transforms may be random; validation transforms must be deterministic.
- Transfer learning can freeze a pretrained backbone or fine-tune selected/all layers.
- Image normalisation must match pretrained-model expectations.
- Class balance, duplicate images, and entity leakage can invalidate validation.

### Worksheet

1. Classify six transforms as safe, risky, or label-destroying for a stated task.
2. Explain why random augmentation is not used for validation.
3. Compare feature extraction with full fine-tuning.
4. State how the final classification layer changes for a new class count.
5. Explain why pretrained normalisation matters.
6. Identify leakage when multiple crops from the same original image cross splits.
7. Design a fair baseline-versus-transfer experiment.
8. List five image error-analysis slices.

### Guided practice

Train a tiny CNN for a short fixed budget, then replace it with a pretrained model under the same split and metric. Compare errors, not just scores.

### Independent task

Fine-tune a pretrained classifier and produce: augmentation policy, frozen/unfrozen parameter count, learning curves, confusion matrix, and 12 annotated errors.

### Exit ticket

Defend one augmentation and reject one harmful augmentation for the current dataset.

---

## Session 50 — Detection, Segmentation, and Error Analysis

### Resource segment

PyTorch object-detection finetuning tutorial; introductory segmentation material from PyTorch/torchvision documentation.

### Essential teaching content

- Classification predicts an image-level label.
- Detection predicts classes and bounding boxes.
- Semantic segmentation predicts a class per pixel; instance segmentation separates objects.
- Intersection over Union measures overlap.
- Detection evaluation must handle localisation, class, confidence, and duplicate detections.
- Annotation quality often limits performance.

### Worksheet

1. Match five tasks to classification, detection, semantic segmentation, or instance segmentation.
2. Calculate IoU for two simple axis-aligned boxes using supplied coordinates.
3. Explain confidence threshold and non-maximum suppression.
4. Distinguish a classification error from a localisation error.
5. Why can resizing distort bounding boxes if annotations are not transformed identically?
6. List four annotation-quality problems.
7. Design an error taxonomy for missed, duplicate, misclassified, and poorly localised objects.
8. State when a classical connected-component method may outperform a detector.

### Guided practice

Students inspect 20 predictions and assign each to an error category. They calculate IoU for five examples and propose one targeted intervention per dominant error.

### Independent task

Complete either a lightweight detection/segmentation tutorial or a classical structural alternative. Submit a reproducible evaluation notebook and a limitation statement.

### Phase 6A exit gate

From a fresh runtime, students must inspect tensor/device state, build Dataset/DataLoader/model objects, train and reload a checkpoint, complete one classical vision baseline, fine-tune one image classifier, and perform structured visual error analysis.