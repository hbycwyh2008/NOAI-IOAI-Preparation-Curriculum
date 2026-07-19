# Phase 4 — Round 1 Paper-Test Training

Sessions 35–38. This phase converts knowledge into reliable paper-test performance.

---

## Session 35 — Multiple-Choice Reasoning and Distractor Analysis

**Duration:** 90 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–10 | 10-item closed-note diagnostic |
| 10–20 | Mark confidence before answers are discussed |
| 20–35 | Teacher models stem parsing and option elimination |
| 35–50 | Pair analysis of six distractors |
| 50–70 | Timed 15-item mixed set |
| 70–82 | Error taxonomy and correction |
| 82–90 | Exit set and submission |

### Strategy taught

1. Identify the tested concept before reading options.
2. Mark absolute terms such as *always*, *never*, and *only*.
3. Calculate independently when possible before selecting.
4. Eliminate options using definitions, preconditions, dimensions, and counterexamples.
5. Record confidence; high-confidence errors reveal dangerous misconceptions.

### Practice set

1. Which split is used primarily for final unbiased estimation? A training B validation C test D bootstrap training.
2. Which metric is most directly harmed by false negatives? A recall B precision C specificity D MSE.
3. Binary search requires: A unique values B sorted values C numeric values D a list shorter than 100.
4. A single-layer perceptron cannot represent: A AND B OR C NAND D XOR.
5. Increasing a classification threshold usually: A raises recall B lowers false negatives C lowers predicted positives D changes training labels.
6. Which operation should occur before `optimizer.step()`? A `loss.backward()` B `model.eval()` C save test labels D fit scaler on all data.
7. A model has train accuracy .99 and validation accuracy .62. Most likely: A underfitting B overfitting C perfect calibration D data normalization success.
8. Which is an unsupervised task? A price prediction B species classification C customer clustering D reward maximisation.
9. Standardisation should be fitted on: A all rows B training data C test data D validation+test.
10. Random forests primarily combine: A sequential residual models B bootstrap trees with feature randomness C one linear and one logistic model D nearest neighbours.

Students must state why every rejected option is wrong for at least five items.

### Independent task

Write four new multiple-choice questions: one Python trace, one metric calculation, one neural-network concept, and one ethics scenario. Include plausible distractor rationales in the private submission to the teacher.

---

## Session 36 — Python and Scikit-Learn Code Tracing

**Duration:** 90 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–8 | Two cold traces |
| 8–20 | Trace-table method |
| 20–35 | Python collection and function traces |
| 35–50 | Sklearn workflow code completion |
| 50–68 | Timed mixed code set |
| 68–80 | Run only after paper predictions |
| 80–90 | Corrections and exit ticket |

### Trace method

For each line record: line number, changed variable, new value/type/shape, output, and possible exception. For ML code also record fit data, transform data, prediction data, and metric inputs.

### Worksheet

1. Trace:
   ```python
   values = [2, 5, 2, 8]
   counts = {}
   for x in values:
       counts[x] = counts.get(x, 0) + 1
   print(counts[2], len(counts))
   ```
2. Trace list slicing and mutation:
   ```python
   a = [1,2,3,4]
   b = a[1:3]
   b[0] = 9
   print(a, b)
   ```
3. Find the indentation error that makes a loop return too early.
4. Complete:
   ```python
   X_train, X_val, y_train, y_val = ______(X, y, test_size=.2, random_state=42, stratify=y)
   model = LogisticRegression(max_iter=1000)
   model.______(X_train, y_train)
   pred = model.______(X_val)
   score = f1_score(______, ______)
   ```
5. Identify leakage:
   ```python
   scaler = StandardScaler().fit(X)
   X_train, X_val = train_test_split(scaler.transform(X), ...)
   ```
6. Predict the shape after `X.reshape(100, -1)` when `X` has 600 elements.
7. Explain why calling `fit_transform` on validation data is wrong.
8. Complete a `Pipeline` containing scaler and logistic regression.

### Independent task

Complete a 20-line sklearn baseline with six blanks and three planted workflow mistakes. Submit the corrected code plus a line-by-line explanation.

---

## Session 37 — Short Answers and Paper Calculations

**Duration:** 90 minutes

### Answer structure

Use **definition → mechanism/evidence → consequence → scenario-specific conclusion**. One accurate paragraph is stronger than a long list of disconnected terms.

### Calculation drill

1. From TP=24, TN=60, FP=15, FN=6, calculate accuracy, precision, recall, specificity, and F1.
2. Calculate MSE for targets `[2,4,9]` and predictions `[3,5,6]`.
3. Standardise 75 when mean=60 and SD=5.
4. Calculate Euclidean distance between `(2,-1)` and `(5,3)`.
5. Calculate output size for input 28, kernel 5, padding 2, stride 1.
6. Count parameters in `Linear(20,8)` and `Linear(8,3)`.
7. Apply one gradient update for parameter 2.0, gradient -0.6, learning rate .1.

### Short-answer prompts

1. Explain why accuracy can be misleading in rare-disease screening.
2. Distinguish overfitting from underfitting and give one evidence-based remedy for each.
3. Explain how a random forest differs from gradient boosting.
4. Explain backpropagation without saying only “it updates weights.”
5. Describe two sources of algorithmic bias and one mitigation for each.
6. Explain why test data must not be used for threshold selection.
7. Compare ReLU and Softmax by role and location in a network.

### Independent task

Write responses under a strict limit of 80 Chinese characters or 45 English words each, then revise for missing mechanism or scenario link.

---

## Session 38 — Full Timed Round 1 Mock and Correction Cycle

**Duration:** 150 minutes

### Timeline

| Time | Activity |
|---|---|
| 0–5 | Rules, materials, and answer-sheet check |
| 5–105 | Closed-note 100-point mock |
| 105–115 | Self-check using a fixed checklist; no answer key |
| 115–130 | Confidence coding and error classification |
| 130–145 | Teacher-led correction of highest-value gaps |
| 145–150 | Individual priority commitment |

# Round 1 Mock A — 100 Points

## Section A — Multiple Choice, 20 × 2 = 40 points

1. The correct operator for equality comparison in Python is: A `=` B `==` C `:=` D `!=`.
2. `range(1,8,3)` produces: A 1,4,7 B 1,3,5,7 C 1,4,8 D 0,3,6.
3. Binary search on an unsorted array is: A always correct B valid only for integers C not guaranteed correct D slower but correct.
4. The task “predict tomorrow's temperature” is usually: A clustering B regression C classification D reinforcement learning.
5. A false negative in disease screening means: A healthy predicted sick B sick predicted healthy C sick predicted sick D healthy predicted healthy.
6. Precision equals: A TP/(TP+FN) B TN/(TN+FP) C TP/(TP+FP) D (TP+TN)/all.
7. A model with poor training and validation performance is most consistent with: A underfitting B leakage C perfect generalisation D calibration.
8. Which should be fitted on training data only? A target labels B StandardScaler C test metric formula D class names.
9. L2 regularisation mainly penalises: A missing values B large squared weights C false positives D small datasets.
10. A pure decision-tree node has Gini impurity: A 0 B .5 C 1 D undefined.
11. Random forests differ from a single tree by using: A only deeper trees B bootstrap samples and feature randomness C no labels D gradient descent.
12. Boosting typically builds learners: A independently in parallel B sequentially C without errors D only on test data.
13. The output of ReLU for -3 is: A -3 B 0 C 3 D .047.
14. A stack of linear layers without nonlinear activations is equivalent to: A a decision tree B one linear transformation C a random forest D k-means.
15. For PyTorch `CrossEntropyLoss`, the model should usually output: A rounded classes B logits C one-hot strings D confusion matrices.
16. Applying Softmax before `CrossEntropyLoss` is usually: A required B redundant/incorrect C a data split D augmentation.
17. In a CNN, padding can: A create labels B preserve spatial size C remove all channels D calculate F1.
18. An AUC of .5 suggests: A perfect ranking B random ranking C zero false positives D perfect calibration.
19. The Turing Test directly establishes: A consciousness B fairness C conversational indistinguishability under the test D causal reasoning.
20. Historical hiring data may reproduce: A only random noise B historical discrimination C guaranteed fairness D test-set independence.

## Section B — Python and Code Completion, 20 points

### B1 — Trace, 8 points

```python
values = [3, 1, 3, 2]
result = []
for i, x in enumerate(values):
    if x not in result and i % 2 == 0:
        result.append(x)
print(result)
```

1. Fill a trace table for each iteration. (6)
2. State the printed output. (2)

### B2 — Complete the ML workflow, 12 points

```python
from sklearn.model_selection import __________
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

X_train, X_val, y_train, y_val = __________(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ('scale', __________()),
    ('model', LogisticRegression(max_iter=1000))
])
model.__________(X_train, y_train)
pred = model.__________(X_val)
print(f1_score(__________, __________))
```

Award points for all seven blanks plus a three-sentence explanation of why the pipeline prevents one form of leakage.

## Section C — Calculations, 20 points

1. TP=30, TN=50, FP=10, FN=10. Calculate accuracy, precision, recall, specificity, and F1. (10)
2. A 32×32 image passes through convolution kernel 3, padding 1, stride 2. Calculate spatial output. Then apply 2×2 pooling stride 2. (4)
3. A network contains `Linear(12,5)` and `Linear(5,2)`. Count trainable parameters. (3)
4. Parameter `w=1.5`, gradient `0.8`, learning rate `.05`. Calculate new `w`. (3)

## Section D — Short Answer, 20 points

Answer each in 60–90 words or equivalent concise Chinese.

1. Explain data leakage and give one preprocessing example. (5)
2. Compare bagging and boosting. (5)
3. Explain backpropagation through the chain rule. (5)
4. Analyse one bias risk in an automated school-admission model and propose a mitigation. (5)

## Required correction record

For every lost point, classify the cause:

- K: knowledge gap;
- C: calculation error;
- R: reading/stem error;
- P: Python trace error;
- W: workflow/leakage error;
- T: time-management error;
- E: explanation incomplete.

The student rewrites every incorrect response and schedules one targeted repair task.

### Phase exit gate

- At least 80/100 on two non-identical mocks;
- no unresolved high-confidence misconception;
- all calculation formulas reproduced from memory;
- code-completion accuracy at least 85%;
- final ten minutes reserved for checking.