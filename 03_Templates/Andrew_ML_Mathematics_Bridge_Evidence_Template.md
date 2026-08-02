# Andrew ML Mathematics Bridge Evidence Template

**Student:**  
**Date:**  
**Session:**  
**Task or dataset:**

Use this record during the transition into Andrew Ng Machine Learning. Show mathematical meaning, not only final answers.

## 1. Task Formalisation

- Real task:
- Input `X`:
- Target/output `y`:
- One row represents:
- Features available at prediction time:
- Output type:
- Baseline:
- Evaluation metric:

## 2. Notation Ledger

| Symbol | Meaning in this task | Type | Allowed range or units |
|---|---|---|---|
| `m` | | | |
| `n` | | | |
| `X` | | | |
| `x^(i)` | | | |
| `y` | | | |
| `w` | | | |
| `b` | | | |
| `ŷ` | | | |
| `J` or loss | | | |

## 3. Shape Ledger

| Object | Expected shape | Why |
|---|---:|---|
| `X` | | |
| one example | | |
| `y` | | |
| `w` | | |
| predictions | | |

Potential shape error:

## 4. Equation to Words

Equation or model rule:

```text

```

In task language, this means:

Each operation does:

- multiplication:
- addition:
- averaging or summation:
- nonlinear transformation, if present:

## 5. Equation to Code

NumPy-style pseudocode or code:

```python

```

Which code object corresponds to each mathematical symbol?

## 6. Hand Prediction and Loss

Given values:

- input:
- parameters:
- target:

Prediction calculation:

Residual or error:

Loss calculation:

What does the loss emphasise?

## 7. Graph or Contour Reasoning

Sketch or attach the graph/contour.

- Horizontal axis:
- Vertical axis:
- Meaning of slope:
- Meaning of curvature or contour spacing:
- What happens when a named parameter increases?
- Which direction reduces the objective?

## 8. Gradient-Descent Reasoning

Supplied parameter:

Supplied gradient or derivative:

Learning rate:

One update:

```text
new parameter =
```

Explain the update direction in words:

What could happen if the learning rate is too small?

What could happen if it is too large?

## 9. Probability, Threshold, Loss, and Metric

- Raw score:
- Probability or transformed score:
- Threshold:
- Predicted class:
- Training loss:
- Evaluation metric:

Explain why these are not interchangeable:

## 10. Scale and Distance

Two points or examples:

Distance calculation:

Which feature dominates and why?

What changes after scaling?

Which models are especially sensitive to this?

## 11. Misconception and Repair

A mathematical idea I initially misunderstood:

Evidence that exposed the misunderstanding:

My corrected explanation:

## 12. Mathematics Gate Checklist

- [ ] I can identify scalar, vector, matrix, probability, parameter, prediction, loss, and metric.
- [ ] I can state the shapes of `X`, `y`, parameters, and predictions.
- [ ] I can translate an equation into task language.
- [ ] I can translate an equation into code or pseudocode.
- [ ] I can calculate a small prediction and loss by hand.
- [ ] I can use a graph to determine slope direction.
- [ ] I can explain one gradient-descent update.
- [ ] I can distinguish probability, threshold, predicted class, loss, and metric.
- [ ] I can explain why feature scale matters.
- [ ] I can state one limitation that the mathematics does not remove.

## Teacher Feedback

- Secure idea:
- Required repair:
- Reassessment evidence:
- Gate status: **Pass / Reteach / Reassess**
