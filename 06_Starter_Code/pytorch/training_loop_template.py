import torch


def train_one_epoch(model, loader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0.0
    for features, labels in loader:
        # TODO: move tensors, zero gradients, forward pass,
        # calculate loss, backpropagate, update parameters.
        raise NotImplementedError
    return total_loss / max(len(loader), 1)
