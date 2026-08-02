# Session 35 — How Machines Recognise Images

**Class duration:** 70 minutes  
**Required reading before class:** Chapters 4–5  
**Essential question:** Is image classification a form of seeing, understanding, or sophisticated pattern matching?

## Required Mastery

Students must be able to:

1. Formalise image classification: pixels as input `X`, class labels as `y`, and class scores or probabilities as output.
2. Distinguish training, validation, and test data.
3. Explain the intuition of local receptive fields, learned filters, feature hierarchies, and convolution.
4. Explain why convolutional structure is useful for images.
5. Describe the role of large labelled datasets and shared benchmarks such as ImageNet.
6. Distinguish object classification, detection, scene description, contextual reasoning, and causal understanding.
7. Explain why high benchmark accuracy supports only a bounded claim under a particular data and evaluation protocol.
8. Recognise that label categories and dataset construction involve human decisions.
9. Identify what additional evidence would be needed before claiming that a model understands a scene.

## Misconceptions to Reject

- Recognising the label **cat** proves that a model understands what a cat is.
- High test accuracy guarantees performance on every real-world image.
- A benchmark label is a complete and objective description of the image.
- A CNN necessarily organises visual concepts in the same way a person does.

## Core Pattern

```text
pixels
→ local learned features
→ feature hierarchy
→ class scores
→ predicted label
```

## 70-Minute Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–7 | **Skill Warm-Up** | Identify `X`, `y`, prediction, and metric in three image tasks. |
| 7–14 | **Talk Robin 1** | Compare one visual success from the reading with one limitation. |
| 14–20 | **Entry Check** | Explain the different purposes of training, validation, and test data. |
| 20–32 | **Core Pattern** | Reconstruct the path from pixels to a class prediction. |
| 32–48 | **Guided Practice** | Compare cat–dog classification, danger detection in a photograph, and explaining why people in a scene are running. |
| 48–62 | **Independent Rebuild** | Construct a capability ladder from pixel processing to classification, detection, scene description, contextual reasoning, and causal understanding. Add one test and one limitation for each level. |
| 62–70 | **Talk Robin 2 + Evidence** | Explain which steps are demonstrated by a classifier and which remain untested. |

## Exit Evidence

Identify `X`, `y`, prediction, and metric in an image-classification task, then explain why correct recognition is not full scene understanding.

## Gate

The student must distinguish the task the model actually performs from the broader human capability suggested by ordinary words such as **see** or **understand**.
