# Model Comparison Matrix

| Family | Strong when | Main limitations | Scaling | Interpretability | Typical data size |
|---|---|---|---|---|---|
| Linear/logistic | approximately linear signal, sparse or high-dimensional features | misses complex interactions without feature work | usually helpful | high | small to large |
| K-nearest neighbours | local similarity is meaningful | slow inference, scale-sensitive, weak in high dimensions | required | medium | small |
| Decision tree | nonlinear rules and mixed tabular relationships | unstable and easy to overfit | usually unnecessary | high | small to medium |
| Random forest | robust nonlinear tabular baseline | larger, less transparent, weak extrapolation | unnecessary | medium | medium |
| Boosting | strong structured-data performance | tuning-sensitive and sequential | model-dependent | medium | medium to large |
| Support vector machine | medium-sized high-dimensional classification | scale-sensitive and expensive on large data | required | low to medium | small to medium |
| Neural network | large or unstructured data with complex signal | data/compute demand, instability, lower transparency | usually required | low | medium to very large |
| K-means | compact distance-based clusters | requires k and compatible geometry | required | medium | small to large |
| PCA | correlated high-dimensional numeric features | linear projection can reduce interpretability | required | medium | small to large |

Treat this as a starting hypothesis. Actual selection depends on validation evidence, constraints, and failure analysis.
