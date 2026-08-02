# Typical Task Map

| Model/family | Typical task | Required comparison |
|---|---|---|
| Linear regression | house price, sales, temperature, or demand prediction | mean baseline |
| Logistic regression | spam, churn, pass/fail, or risk classification | majority/probability baseline |
| K-nearest neighbours | small-scale classification or similarity lookup | logistic regression |
| Decision tree | interpretable tabular classification | shallow tree versus unrestricted tree |
| Random forest | nonlinear tabular prediction | single tree |
| Boosting | strong structured-data benchmark | random forest or linear model |
| Support vector machine | medium-sized high-dimensional classification | logistic regression |
| K-means | customer or item grouping without labels | random grouping and cluster interpretation |
| PCA | visualisation or compression of high-dimensional data | original features and explained variance |
| Anomaly detection | equipment, transaction, or sensor anomalies | simple threshold rule |
| Recommender system | movie, product, or content recommendation | popularity baseline |
| Neural network | nonlinear classification | strong classical baseline |

Every task produces a model card: suitable data, strengths, limitations, preprocessing needs, common failure modes, runtime, and evidence.
