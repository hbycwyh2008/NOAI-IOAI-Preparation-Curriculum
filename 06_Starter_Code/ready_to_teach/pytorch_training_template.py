"""Device-safe PyTorch train/validation/checkpoint scaffold.

Students supply a model, DataLoaders, loss, and optimizer. The functions include
shape/value checks and weighted loss aggregation but no task-specific solution.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import torch
from torch import nn
from torch.utils.data import DataLoader


def select_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def _check_batch(features: torch.Tensor, labels: torch.Tensor) -> None:
    if features.shape[0] != labels.shape[0]:
        raise ValueError("Feature and label batch sizes differ.")
    if not torch.isfinite(features).all():
        raise ValueError("Features contain NaN or infinity.")


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> dict[str, float]:
    model.train()
    total_loss = 0.0
    total_correct = 0
    total_examples = 0

    for features, labels in loader:
        _check_batch(features, labels)
        features = features.to(device)
        labels = labels.to(device)

        optimizer.zero_grad(set_to_none=True)
        logits = model(features)
        if logits.shape[0] != labels.shape[0]:
            raise ValueError("Model output batch size differs from labels.")
        loss = loss_fn(logits, labels)
        if not torch.isfinite(loss):
            raise FloatingPointError("Training loss is NaN or infinity.")
        loss.backward()
        optimizer.step()

        batch_size = labels.shape[0]
        total_loss += float(loss.detach()) * batch_size
        total_correct += int((logits.argmax(dim=1) == labels).sum().item())
        total_examples += batch_size

    if total_examples == 0:
        raise ValueError("Training loader is empty.")
    return {
        "loss": total_loss / total_examples,
        "accuracy": total_correct / total_examples,
    }


@torch.no_grad()
def validate(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    device: torch.device,
) -> dict[str, float]:
    model.eval()
    total_loss = 0.0
    total_correct = 0
    total_examples = 0

    for features, labels in loader:
        _check_batch(features, labels)
        features = features.to(device)
        labels = labels.to(device)
        logits = model(features)
        loss = loss_fn(logits, labels)

        batch_size = labels.shape[0]
        total_loss += float(loss) * batch_size
        total_correct += int((logits.argmax(dim=1) == labels).sum().item())
        total_examples += batch_size

    if total_examples == 0:
        raise ValueError("Validation loader is empty.")
    return {
        "loss": total_loss / total_examples,
        "accuracy": total_correct / total_examples,
    }


def fit(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    epochs: int,
    checkpoint_path: Path,
    device: torch.device | None = None,
) -> list[dict[str, Any]]:
    if epochs <= 0:
        raise ValueError("epochs must be positive.")
    device = device or select_device()
    model.to(device)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)

    history: list[dict[str, Any]] = []
    best_val_loss = float("inf")

    for epoch in range(1, epochs + 1):
        train_metrics = train_one_epoch(model, train_loader, loss_fn, optimizer, device)
        val_metrics = validate(model, val_loader, loss_fn, device)
        row = {"epoch": epoch, "train": train_metrics, "validation": val_metrics}
        history.append(row)
        print(row)

        if val_metrics["loss"] < best_val_loss:
            best_val_loss = val_metrics["loss"]
            torch.save(
                {
                    "epoch": epoch,
                    "model_state": model.state_dict(),
                    "optimizer_state": optimizer.state_dict(),
                    "validation": val_metrics,
                },
                checkpoint_path,
            )

    return history


def load_best(model: nn.Module, checkpoint_path: Path, device: torch.device | None = None) -> dict[str, Any]:
    device = device or select_device()
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(checkpoint["model_state"])
    model.to(device)
    model.eval()
    return checkpoint
