# Level 2 — Mixed and Ambiguous Scenarios

These scenarios contain distracting keywords or validation traps. Define the required output precisely before naming the task.

### Day 13 — House type or price
A housing table can support two products: predicting the sale price and predicting whether a property is detached, semi-detached, or apartment. The product manager has not chosen which output is required. State what must be clarified and classify both possible tasks.

### Day 14 — Fraud across customers
Transactions are labelled fraudulent or legitimate. The same customer may have many transactions, and the model will be deployed on entirely new customers. Explain the task and the validation split that matches deployment.

### Day 15 — Hospital readmission time
For discharged patients, the exact number of days until readmission is known when readmission occurs; many patients are not readmitted during the observation window. The hospital wants a risk estimate over time, not merely a yes/no label.

### Day 16 — Search ranking
For each search query, past results have relevance grades from 0 to 4. The system must order candidate documents for a new query. A highly relevant document placed first matters more than one placed tenth.

### Day 17 — Defect image localisation
Training images include pixel masks showing the exact defective region. The system must output a mask, not only state whether a defect exists.

### Day 18 — Rare species
Camera-trap images have species labels, but 90% belong to one common species. The conservation team cares about detecting rare species and will review only high-confidence alerts.

### Day 19 — Time-dependent demand
Daily demand is available for 300 stores. Promotions and weather are known in advance. The model will forecast the next 14 days for the same stores. Randomly shuffling all rows creates unrealistic information leakage.

### Day 20 — Student misconception
Each written answer may contain several misconception types at once. Teachers have annotated zero, one, or multiple misconception tags per answer.

### Day 21 — New-product recommendation
Users have interaction histories, but newly launched products have no interactions. Product text, category, and price are available. The system must rank products for each user and handle cold-start items.

### Day 22 — Duplicate patients
A medical image dataset contains several scans from each patient. Labels are attached to scans, but evaluation should estimate performance on unseen patients. Identify the task and the grouping requirement.

### Day 23 — Quality score bands
A factory records a continuous quality score from 0 to 100, but operators currently report low, medium, or high by applying fixed thresholds. Decide whether the model should predict the score or the band, and explain the consequence of each choice.

### Day 24 — Topic discovery versus tagging
A news archive has no topic labels, and editors first want to discover recurring themes. Later, after reviewing the themes, they may label articles for automatic tagging. Classify the two stages separately.
