# Round 1 Mock B — 100 Points

**Duration:** 120 minutes  
**Conditions:** closed note; calculator only when explicitly permitted by the teacher; no AI tools.  
**Suggested time:** Section A 30 min, B 25 min, C 30 min, D 25 min, review 10 min.

Do not write explanations beside multiple-choice items unless asked. Mark confidence H/M/L for each answer after completing the paper.

---

## Section A — Multiple Choice, 20 × 2 = 40 points

1. What is printed?
   ```python
   x = [1, 2, 3]
   y = x
   y.append(4)
   print(len(x))
   ```
   A 3  B 4  C error  D 1

2. Which data structure best represents a mapping from class name to count?  
   A tuple  B dictionary  C string  D float

3. The output of `list(range(5, 0, -2))` is:  
   A `[5,3,1]`  B `[5,4,3,2,1]`  C `[5,3]`  D `[0,2,4]`

4. Which is a valid reason to use grouped cross-validation?  
   A every feature is numerical  B rows from one person must not cross splits  C the model is linear  D the test set is large

5. In binary classification, specificity equals:  
   A TP/(TP+FN)  B TN/(TN+FP)  C TP/(TP+FP)  D FP/(FP+TN)

6. Lowering the classification threshold usually:  
   A decreases predicted positives  B increases recall  C guarantees higher F1  D changes model weights

7. Which statement about ROC AUC is most accurate?  
   A it is accuracy at threshold .5  B it measures ranking across thresholds  C it guarantees calibrated probabilities  D it is only for regression

8. Fitting a scaler before cross-validation can cause:  
   A underflow  B data leakage  C class creation  D image augmentation

9. A model has training loss high and validation loss high. The strongest initial diagnosis is:  
   A likely underfitting  B certain leakage  C perfect fit  D threshold too low

10. L1 regularisation is especially associated with:  
    A encouraging sparse weights  B making every weight equal  C increasing image size  D creating labels

11. A tree split is useful when it:  
    A increases weighted impurity  B reduces weighted impurity  C removes the target  D uses only ID columns

12. In bagging, component models are commonly trained:  
    A on bootstrap samples  B only on false negatives  C without replacement on test data  D sequentially on residuals

13. Gradient boosting regression conceptually fits each new learner to:  
    A class names  B remaining errors/residuals  C random labels  D validation predictions only

14. What is the ReLU output for `z=2.7`?  
    A 0  B -2.7  C 2.7  D .5

15. Which tensor shape is conventional for a batch of 16 RGB 64×64 images in PyTorch?  
    A `(64,64,3,16)`  B `(16,3,64,64)`  C `(16,64,64)`  D `(3,16,64,64)`

16. `optimizer.zero_grad()` is normally used because:  
    A gradients accumulate by default  B labels are strings  C Softmax needs clearing  D validation changes weights

17. During validation, the correct pair is usually:  
    A `model.train()` and `backward()`  B `model.eval()` and `torch.no_grad()`  C `model.eval()` and optimizer step  D dropout and augmentation only

18. A tokenizer attention mask primarily distinguishes:  
    A train and test labels  B content tokens and padding  C images and audio  D correct and incorrect predictions

19. In audio, 48,000 samples at 16 kHz represent:  
    A 0.33 s  B 3 s  C 16 s  D 48 s

20. A model trained on historical decisions may reproduce unfairness because:  
    A labels can encode past discrimination  B neural networks cannot use numbers  C validation removes all bias  D privacy guarantees fairness

---

## Section B — Python and ML Code, 20 points

### B1 — Trace and Explain, 8 points

```python
def transform(values):
    output = []
    for i, value in enumerate(values):
        if value % 2 == 0:
            output.append(value // 2)
        elif i > 1:
            output.append(value + i)
    return output

items = [6, 5, 3, 8]
answer = transform(items)
print(answer[-1], len(answer))
```

1. Complete a trace table showing `i`, `value`, condition outcome, and `output` after each iteration. (5)
2. State the value of `answer`. (1)
3. State the printed output. (1)
4. Give one input of length 2 that makes the returned list empty. (1)

### B2 — Repair a Leakage-Safe Pipeline, 12 points

The following code contains missing imports/blanks and two conceptual errors.

```python
import pandas as pd
from sklearn.model_selection import __________
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import __________

X = data.drop(columns=['target'])
y = data['target']

numeric = ['age', 'hours']
categorical = ['device', 'course']

preprocess = ColumnTransformer([
    ('num', Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale', __________())
    ]), numeric),
    ('cat', Pipeline([
        ('impute', SimpleImputer(strategy='most_frequent')),
        ('encode', OneHotEncoder(handle_unknown=__________))
    ]), categorical)
])

X_train, X_val, y_train, y_val = __________(
    X, y, test_size=.25, random_state=7, stratify=y
)

X_train = preprocess.fit_transform(X_train)
X_val = preprocess.fit_transform(X_val)  # conceptual error 1

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_train)            # conceptual error 2
print(f1_score(y_val, pred))
```

1. Fill the five blanks. (5)
2. Correct conceptual error 1. (2)
3. Correct conceptual error 2. (2)
4. Rewrite the workflow as one sklearn `Pipeline`. (3)

---

## Section C — Calculations, 20 points

1. A classifier produces TP=18, TN=72, FP=8, FN=12. Calculate:  
   a. accuracy; b. precision; c. recall; d. specificity; e. F1. Show formulas. (10)

2. Targets are `[4, 7, 9, 10]`; predictions are `[5, 5, 10, 8]`. Calculate MSE and RMSE. (4)

3. A 64×64 image passes through `Conv2d` with kernel 5, padding 2, stride 2, then max pooling with kernel 2 and stride 2. Calculate both spatial output sizes. (3)

4. Count all trainable parameters in:  
   `Linear(30,12)` followed by `Linear(12,4)`. Include biases. (2)

5. Apply one gradient descent update: parameter `-0.4`, gradient `1.6`, learning rate `0.025`. (1)

---

## Section D — Structured Short Answers, 20 points

Answer each in no more than 90 English words or an equivalent concise Chinese response. Each answer must contain definition/claim, mechanism/evidence, and scenario-specific implication.

1. **Validation design:** Explain why a random row split can be invalid for a speech dataset containing multiple clips per speaker. Give a better strategy. (5)

2. **Neural networks:** Explain why nonlinear activation functions are necessary in a multilayer network. (5)

3. **Model comparison:** A random forest scores macro F1 .82 ± .01 in five folds; a boosting model scores .84 ± .08 and requires ten times the runtime. Recommend a model for a time-limited contest and justify the decision. (5)

4. **Responsible AI:** A school deploys an automated risk score to decide which students receive counselling. Identify one bias or harm pathway and propose both a technical and an organisational mitigation. (5)

---

## Final Review Checklist

Before submitting:

- [ ] every question has an answer;
- [ ] positive class is consistent in metric calculations;
- [ ] every denominator is checked;
- [ ] tensor/conv shapes use the correct formula;
- [ ] code predictions are written before mental execution changes them;
- [ ] short answers include a mechanism, not definitions alone;
- [ ] confidence H/M/L is marked for all items.

## Post-Mock Error Codes

Use: `K` knowledge, `C` calculation, `R` reading, `P` Python trace, `W` workflow/leakage, `S` shape, `E` explanation, `T` time. The correction submission must include the correct reasoning and one prevention strategy for every lost point.