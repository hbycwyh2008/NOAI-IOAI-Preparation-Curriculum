# Phase 2A — AI and Machine Learning Foundations

Sessions 9–18. Standard duration: 90 minutes.

---

## Session 9 — AI Paradigms, Turing Test, and Capabilities

### Resource segment

AI for Everyone: **What AI Can and Cannot Do**; official syllabus sections on symbolism, connectionism, behaviourism, and the Turing Test.

### Essential teaching content

- Symbolic AI represents rules and knowledge explicitly.
- Connectionist systems learn distributed representations from examples.
- Behaviour-based approaches emphasise action and interaction with an environment.
- The Turing Test evaluates conversational indistinguishability, not truth, consciousness, fairness, or general intelligence.
- AI capability claims must name the task, data distribution, metric, and operating conditions.

### Entry check

1. Does passing a Turing Test prove consciousness? Explain.
2. Give one symbolic and one connectionist system.
3. What information is missing from the claim “the model is intelligent”?

### Guided practice

Classify six systems by dominant paradigm and identify what evidence would be needed to justify each capability claim.

### Worksheet

1. Define symbolic AI, connectionism, and behaviour-based AI.
2. Match expert system, CNN, and robot obstacle avoidance to a paradigm.
3. State two limitations of the Turing Test.
4. Rewrite “This AI understands medicine” as a measurable claim.
5. Explain narrow AI versus artificial general intelligence.
6. Identify one capability and one limitation of a current classifier.

### Independent task

Write a 250-word evaluation of an AI product claim using task, data, metric, limitation, and risk.

---

## Session 10 — Bias, Privacy, Safety, and Responsibility

### Resource segment

AI for Everyone: **AI and Society**; teacher case studies on automated hiring and face recognition.

### Essential teaching content

- Data bias, sampling bias, measurement bias, label bias, and deployment bias are distinct.
- Fairness metrics can conflict; the correct analysis depends on stakeholders and harms.
- Privacy concerns data collection, access, inference, retention, and re-identification.
- Safety is not only model accuracy: monitoring, fallback, human review, and incident response matter.
- Explainability does not automatically make a system fair or correct.

### Worksheet

1. Distinguish sampling bias from label bias.
2. A hiring model learns from historical hiring decisions. Name two possible bias pathways.
3. Why can overall accuracy hide subgroup harm?
4. Give one privacy risk created by retaining raw audio.
5. Propose one technical and one organisational mitigation.
6. Explain why “a human is in the loop” is not sufficient by itself.
7. Write a four-part ethics response: issue, evidence, affected group, mitigation.

### Guided practice

Teams audit a school attendance face-recognition proposal using purpose, necessity, alternatives, data, stakeholders, failure modes, and governance.

### Independent task

Complete a structured NOAI-style response to a medical-screening bias scenario.

---

## Session 11 — Supervised and Unsupervised Learning

### Resource segment

Machine Learning Specialization, Course 1 introduction; Google ML Crash Course: **Introduction to Machine Learning**.

### Essential teaching content

- Supervised learning uses input-label pairs; common outputs are continuous regression targets and discrete classes.
- Unsupervised learning seeks structure without target labels; examples include clustering, dimensionality reduction, and anomaly detection.
- Labels can be noisy, delayed, incomplete, or proxy variables.
- The presence of data does not imply the presence of usable labels.

### Worksheet

1. Classify eight tasks as regression, classification, clustering, or anomaly detection.
2. What is the label in a house-price prediction task?
3. Why is customer segmentation not automatically a classification problem?
4. Give one example of a proxy label and its risk.
5. Describe one way to evaluate clustering without known labels.
6. Explain why “unsupervised” does not mean “no human choices.”

### Guided practice

Students receive task cards with ambiguous wording and must identify input, target, available labels, possible metric, and learning paradigm.

### Independent task

Design one supervised and one unsupervised solution for the same school-energy dataset, including limitations.

---

## Session 12 — Reinforcement Learning Foundations

### Resource segment

Machine Learning Specialization, Course 3: **Reinforcement Learning Introduction**; optional IOAI Academy decision-under-constraint example.

### Essential teaching content

- An agent observes a state, chooses an action, receives a reward, and transitions.
- A policy maps states to actions or action probabilities.
- Return aggregates future rewards; discounting controls the influence of delayed rewards.
- Reward design can produce unintended behaviour.
- Exploration gathers information; exploitation uses current knowledge.

### Worksheet

1. Label state, action, reward, environment, and policy in a maze.
2. Explain immediate reward versus return.
3. What could go wrong if a cleaning robot is rewarded only for the amount of dirt collected?
4. Distinguish supervised labels from RL rewards.
5. Give one exploration action and one exploitation action.
6. Explain why delayed rewards make credit assignment difficult.

### Guided practice

Students analyse three reward functions for the same game and predict likely unintended strategies.

### Independent task

Design a small RL environment with states, actions, transition idea, terminal condition, reward, and one reward-hacking risk.

---

## Session 13 — Linear Regression: Model, Residual, and Cost

### Resource segment

Google ML Crash Course: **Linear Regression** sections on linear models and loss; MLS Course 1: model representation and cost function.

### Essential teaching content

- Prediction: `y_hat = wx + b` for one feature.
- Residual: observed minus predicted value.
- Mean squared error penalises larger errors more strongly.
- Fitting selects parameters; evaluation estimates generalisation.
- Extrapolation beyond training data is risky.

### Worked example

For points `(1,3), (2,5), (3,7)` and model `y_hat = 2x + 1`, calculate predictions, residuals, squared errors, and MSE.

### Worksheet

1. Calculate predictions for `x = 0, 2, 5` when `w=3, b=-1`.
2. Calculate residuals for three supplied observations.
3. Compute MSE from errors `[-2, 1, 3]`.
4. Why does MSE emphasise a large outlier?
5. Interpret slope and intercept in a temperature/energy model.
6. Explain interpolation versus extrapolation.
7. Identify whether a classification target is suitable for ordinary linear regression.

### Guided practice

Students compare three candidate lines by calculating MSE on a four-row dataset.

### Independent task

Fit `LinearRegression` to a one-feature synthetic dataset, report coefficient/intercept, plot predictions, and explain two largest residuals.

---

## Session 14 — Gradient Descent, Feature Scaling, and Multiple Regression

### Resource segment

Google ML Crash Course: **Linear Regression — Gradient Descent**; MLS Course 1: gradient descent and multiple features.

### Essential teaching content

- A gradient gives the direction of steepest increase; subtracting it decreases cost locally.
- Learning rate too small is slow; too large can oscillate or diverge.
- Feature scaling improves optimisation when feature magnitudes differ.
- Multiple regression combines weighted features; coefficients require careful interpretation with correlated inputs.

### Worksheet

1. Apply one update: `w_new = w - alpha * gradient` for `w=4`, `alpha=.1`, gradient `6`.
2. Predict the effect of learning rates `0.000001`, `0.1`, and `10` on the same smooth cost curve.
3. Why can income and age on different scales slow optimisation?
4. Standardise values `[10, 20, 30]` using mean 20 and standard deviation 10.
5. Write the multiple regression equation for three features.
6. Explain why a coefficient is not automatically causal.

### Guided practice

Students inspect four loss curves and diagnose slow learning, convergence, oscillation, or divergence.

### Independent task

Train scaled and unscaled gradient-based regressors, keep all other settings fixed, and compare convergence evidence.

---

## Session 15 — Logistic Regression, Sigmoid, and Decision Boundaries

### Resource segment

Google ML Crash Course: **Logistic Regression**; MLS Course 1 classification introduction.

### Essential teaching content

- Logistic regression models log-odds as a linear function.
- Sigmoid maps a real-valued score into `(0,1)`.
- A probability threshold converts probability to class.
- The linear score defines a decision boundary.
- Probability is not the same as certainty or calibrated reliability.

### Worksheet

1. State the range of the sigmoid function.
2. Convert probabilities `.2, .5, .8` to classes at threshold `.5`.
3. Repeat at threshold `.7`; state which errors may rise.
4. Explain why a probability model is still called logistic *regression*.
5. Sketch a one-dimensional decision boundary.
6. Explain why a high predicted probability can still be wrong.
7. Identify features and target in a spam-classification example.

### Guided practice

Use a table of model scores, sigmoid probabilities, labels, and thresholds to fill predicted classes and error types.

### Independent task

Create a small logistic-regression classifier, plot predicted probability against one feature, and explain the boundary.

---

## Session 16 — Thresholds, Log Loss, and Sklearn Classification

### Resource segment

Google ML Crash Course: **Classification — Thresholds** and logistic loss; scikit-learn `LogisticRegression` and `predict_proba` documentation.

### Essential teaching content

- Log loss rewards confident correct predictions and strongly penalises confident wrong predictions.
- `predict_proba` permits threshold control; `predict` uses the estimator's class decision rule.
- Threshold selection belongs inside validation, not on the final test set.
- Different costs justify different thresholds.

### Worksheet

1. Which prediction receives greater log-loss penalty: wrong at `.55` or wrong at `.99`? Why?
2. For 10 probabilities and labels, calculate predictions at `.3`, `.5`, and `.8`.
3. At which threshold is recall highest?
4. At which threshold are false positives lowest?
5. Explain why threshold tuning on test labels leaks information.
6. Write sklearn code to obtain positive-class probabilities.
7. State one situation requiring a threshold below `.5`.

### Guided practice

Students build a threshold table containing TP, TN, FP, FN, precision, and recall for three thresholds.

### Independent task

Choose a threshold for a disease-screening scenario, justify the error trade-off, and document validation evidence.

---

## Session 17 — Mean, Variance, Standard Deviation, and Z-Scores

### Resource segment

StatQuest: **Mean, Variance and Standard Deviation**; teacher note on sample versus population notation.

### Essential teaching content

- Mean measures centre but is sensitive to outliers.
- Variance averages squared deviations; standard deviation returns to original units.
- Median and interquartile range may better describe skewed data.
- A z-score expresses distance from the mean in standard-deviation units.

### Worksheet

Using `[2, 4, 4, 6, 9]`:

1. Calculate the mean and median.
2. Calculate each deviation from the mean.
3. Calculate population variance and standard deviation.
4. Add `100`; compare the change in mean and median.
5. Calculate the z-score of `9` using supplied mean and SD.
6. Explain why deviations sum to zero but squared deviations do not.
7. Choose mean/SD or median/IQR for house prices with extreme mansions.

### Guided practice

Pairs calculate statistics independently, compare discrepancies, and identify whether the error arose in centre, deviation, squaring, averaging, or square root.

### Independent task

Write functions for mean, population variance, standard deviation, and z-score without calling NumPy's corresponding summary functions.

---

## Session 18 — Normal Distribution, Distance, and Standardisation

### Resource segment

StatQuest: **The Normal Distribution** and **Standardization**; teacher note on Euclidean distance.

### Essential teaching content

- A normal distribution is symmetric and parameterised by mean and standard deviation.
- The 68–95–99.7 rule is an approximation for normal data.
- Euclidean distance is scale-sensitive.
- Standardisation centres features and scales by standard deviation.
- Fit preprocessing on training data only, then apply the fitted transformation elsewhere.

### Worksheet

1. Approximately what proportion lies within one, two, and three SDs of a normal mean?
2. Calculate Euclidean distance between `(1,2)` and `(4,6)`.
3. Compare two candidates when one feature is measured in yuan and another in years; explain scale dominance.
4. Standardise `x=70` when mean is 50 and SD is 10.
5. Why must validation data not determine the scaler mean?
6. Explain why standardisation does not make a skewed variable normal.
7. State one model family that usually benefits strongly from scaling and one that often benefits less.

### Guided practice

Students compare nearest neighbours before and after standardising two features with very different units.

### Independent task

Build a small distance-based classifier twice—raw and scaled—and explain any neighbour or prediction changes.

### Phase 2A exit gate

Cold performance must include task-type classification, one regression calculation, one threshold analysis, one descriptive-statistics calculation, one distance calculation, and a structured ethics response.