# Session 60 — PyTorch Forward Pass: `nn.Module`, Logits, and Shape Debugging

**Duration:** 75 minutes  
**Prerequisite:** Session 47 conceptual forward propagation and Session 59 tensor/device work

## Required Mastery

Students must be able to:

1. implement a small network as an `nn.Module`;
2. explain what belongs in `__init__` and what belongs in `forward`;
3. track batch, feature, hidden, and output shapes through every layer;
4. distinguish logits, probabilities, predictions, targets, and loss;
5. match the final layer and loss function to regression, binary classification, or multiclass classification;
6. recognise when a softmax or sigmoid should not be inserted before a logits-based loss;
7. diagnose a matrix-shape, dtype, or device mismatch from an error message;
8. verify the forward pass with a small batch before training.

## Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–8 | **Skill Warm-Up** | Predict shapes for a batch passing through two `nn.Linear` layers. |
| 8–15 | **Talk Robin 1** | Explain the difference between conceptual layer equations and a PyTorch `forward` method. |
| 15–22 | **Entry Check** | Match task type, output shape, and loss function. |
| 22–35 | **Core Pattern** | Trace batch → module → logits → loss-ready output. |
| 35–53 | **Guided Practice** | Repair a model with an incorrect input width, activation placement, and target dtype. |
| 53–67 | **Independent Rebuild** | Implement and test a fresh `nn.Module` from a shape specification. |
| 67–75 | **Talk Robin 2 + Evidence** | Explain the forward trace and one repaired failure. |

## Core Pattern

```text
input batch
→ shape assertion
→ linear transformation
→ activation
→ hidden representation
→ output layer
→ logits or regression output
→ loss function
```

## Guided Practice

Students annotate and repair:

```python
class Classifier(torch.nn.Module):
    def __init__(self, n_features: int, n_classes: int) -> None:
        super().__init__()
        self.hidden = torch.nn.Linear(n_features, 16)
        self.output = torch.nn.Linear(16, n_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.hidden(x))
        return self.output(x)
```

The class must state the expected shape and dtype before and after each operation and explain why the returned tensor is logits.

## Independent Rebuild

Create a module from a supplied task card. Include:

- constructor parameters;
- shape comments;
- a deterministic synthetic batch;
- assertions for output shape and finite values;
- the matching loss function;
- one intentionally introduced failure and its diagnosis;
- CPU-safe execution evidence.

## Evidence

Submit the shape ledger, tested module, output/loss interpretation, repaired error record, and one explanation of why a correct forward pass is necessary but not sufficient for a correct training system.

## Gate

The module must run on a fresh process, produce the required output shape, use a compatible loss, and be explained without relying on trial-and-error execution.
