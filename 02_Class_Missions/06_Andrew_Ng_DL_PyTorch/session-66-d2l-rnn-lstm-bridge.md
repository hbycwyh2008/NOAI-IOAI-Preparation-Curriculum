# Session 66 — D2L RNN, BPTT, and LSTM Bridge

**Placement:** embedded inside Session 66; this packet does not add another scheduled session.  
**Role:** connect recurrent equations, sequence shapes, and LSTM gates to a small PyTorch sequence model.

## Assigned D2L Sections

- [8.4 Recurrent Neural Networks](https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn.html)
- [8.6 Concise RNN Implementation](https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn-concise.html)
- [8.7 Backpropagation Through Time](https://zh.d2l.ai/chapter_recurrent-neural-networks/bptt.html)
- [9.2 Long Short-Term Memory](https://zh.d2l.ai/chapter_recurrent-modern/lstm.html)

Use the PyTorch tab. From-scratch equations are required for tracing; the final implementation may use `nn.RNN` or `nn.LSTM`.

## Required Mastery

Students must be able to:

1. explain how a hidden state carries information across time steps;
2. distinguish sequence length, batch size, input width, hidden width, layer count, and direction count;
3. trace one recurrent update by hand;
4. explain why repeated multiplication can contribute to vanishing or exploding gradients;
5. state the roles of the LSTM input, forget, and output gates and the cell state;
6. match the model output used for sequence classification to the task;
7. recognise padding, masking, and future-information leakage risks.

## Embedded Lesson Flow

| Block | Required action |
|---|---|
| Pre-class | Read D2L 8.4 and 9.2; create a symbol and shape glossary. |
| Entry Check | Label sequence, batch, feature, hidden, and output axes in three tensor layouts. |
| Core Pattern | Calculate one RNN hidden-state update and trace the recurrence across three steps. |
| Guided Practice | Run a small `nn.RNN` or `nn.LSTM`, inspect output and hidden-state shapes, and map them back to the equations. |
| Independent Rebuild | Build a sequence classifier and repair one axis, hidden-state, or padding error. |

## Shape Ledger

Record the selected PyTorch layout explicitly:

```text
input: batch × sequence × features
recurrent output: batch × sequence × hidden
final hidden: layers × batch × hidden
classifier output: batch × classes
```

Adjust the ledger when using bidirectionality, multiple layers, or `batch_first=False`.

## Independent Task

1. construct or load a small labelled sequence dataset;
2. define a simple non-recurrent baseline;
3. implement an RNN or LSTM classifier;
4. state every tensor shape before execution;
5. compare the recurrent model with the simple baseline under the same split and metric;
6. introduce and repair one sequence-axis or hidden-state error;
7. explain when an RNN/LSTM is unnecessary or inferior to a simpler model.

## Required Evidence

- one hand recurrent-state calculation;
- sequence-shape ledger;
- LSTM gate explanation;
- simple-baseline versus recurrent-model comparison;
- repaired tensor-layout or hidden-state failure;
- note on vanishing/exploding gradients and one practical remedy;
- leakage or masking check appropriate to the task.

## Gate

The student passes only when the implementation matches the predicted tensor shapes and the student can explain both the value and the limitation of recurrence for the chosen task.