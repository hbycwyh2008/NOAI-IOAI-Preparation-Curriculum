# Andrew ML Mathematics Bridge Rubric

**Purpose:** assess whether a student can use the mathematics required to understand and implement Andrew Ng Machine Learning models.

**Maximum:** 32 points  
**Recommended gate:** 24/32, with no critical error in shape reasoning, loss interpretation, or gradient direction.

| Criterion | 4 — Secure | 3 — Mostly secure | 2 — Partial | 1 — Not yet secure |
|---|---|---|---|---|
| Task and notation | Correctly maps the real task to `X`, `y`, examples, features, parameters, predictions, loss, and metric | One minor notation or task-boundary error | Several objects are named but roles are confused | Cannot connect notation to the task |
| Shapes and vectorisation | Correctly states and checks shapes; explains rows, features, parameters, and vectorised prediction | Minor orientation or convention error | Can state some shapes but cannot diagnose incompatibility | Treats arrays as unstructured numbers |
| Equation meaning | Translates equations accurately into task language and explains every operation | Meaning is mostly correct but one operation is vague | Gives a procedural reading without task meaning | Recites symbols without interpretation |
| Hand prediction and loss | Correctly computes a prediction, residual, and loss and explains what the loss emphasises | Minor arithmetic error with correct method | Completes only part of the calculation or confuses error and loss | Cannot calculate or interpret the objective |
| Graph and function reasoning | Correctly interprets slope, intercept, curvature, sigmoid behaviour, and parameter effects | Mostly correct with one weak graph interpretation | Reads points but cannot predict parameter effects | Cannot use a graph to reason about the model |
| Derivative and gradient reasoning | Correctly explains slope sign, partial derivatives, gradient direction, learning rate, and one update | Correct update with incomplete explanation | Knows the rule but cannot justify direction or diagnose learning rate | Moves parameters in the wrong direction or treats gradient as the parameter |
| Probability, log loss, and metrics | Clearly distinguishes score, probability, threshold, class, loss, and evaluation metric; explains confident errors | One distinction remains weak | Several terms are used interchangeably | Confuses probability, prediction, loss, and metric |
| Code and model-behaviour connection | Translates equation to code and code to equation; predicts effects of scale or parameter changes and states limitations | Translation is correct but behaviour or limitations are incomplete | Runs code but explanation is shallow | Cannot connect mathematical objects to implementation |

## Critical Errors

A student does not pass the bridge while any of these remain:

- impossible or unexplained `X`, `y`, parameter, or prediction shapes;
- treating the evaluation metric as the quantity directly optimised without evidence;
- moving a parameter uphill while claiming to perform gradient descent;
- treating a raw score, probability, threshold, and class as the same object;
- claiming that a low training loss proves generalisation, understanding, or deployment safety.

## Required Evidence

Use the [Andrew ML Mathematics Bridge Evidence Template](../03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md) and collect:

- task and notation ledger;
- shape ledger;
- equation-to-words explanation;
- equation-to-code translation;
- hand prediction and loss calculation;
- graph or contour interpretation;
- one gradient-descent update;
- probability/loss/metric distinction;
- scale or distance analysis;
- misconception and repair record.

## Reassessment

Reassessment must use a new task or new numbers. Recopying the original worked example is not sufficient evidence of transfer.