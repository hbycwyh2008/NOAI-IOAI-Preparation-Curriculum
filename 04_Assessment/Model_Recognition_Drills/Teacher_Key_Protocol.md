# Model Recognition Teacher Key Protocol

The public repository contains scenarios, response fields, scoring dimensions, and mastery rules. It must not contain a complete answer key or calibrated accepted-answer bank.

## Private Key Contents

For each scenario, the private teacher record should contain:

- primary and acceptable alternative task formulations;
- required output and label-availability reasoning;
- acceptable baselines;
- suitable metrics and error-cost explanations;
- acceptable model families with assumptions;
- required validation/group/time split;
- common leakage and shift risks;
- common wrong answers and diagnostic follow-up questions;
- scoring examples at 0, 1, and full credit for ambiguous fields.

## Feedback Rule

Do not reply only with the final model name. Use this order:

1. ask the student to restate the required output;
2. ask whether labels exist during training;
3. ask what one row/sample represents;
4. ask for the simplest valid baseline;
5. ask what error the metric should value;
6. only then compare model families.

## Security Rule

- Store detailed solutions in a private teacher repository or access-controlled system.
- Do not commit answer keys, hidden labels, private tests, scoring scripts, or calibration examples to public Git history.
- Rotate or modify scenarios used in formal scored assessments.
- Treat public scenarios as practice; formal mastery confirmation includes a fresh secured set.

## Mastery Decision

Mark mastery only after five consecutive independently completed daily sets at or above 90%, followed by one fresh secured mixed set. A student who memorises public scenarios but cannot explain output, labels, baseline, metric, validation, and limitations has not met the standard.
