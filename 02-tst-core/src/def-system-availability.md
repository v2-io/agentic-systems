---
slug: def-system-availability
type: definition
status: axiomatic
depends:
  - scope-software
---

# Definition: System Availability

The fraction of time a system serves its users successfully.

## Formal Expression

*[Definition (system-availability)]*

$$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$$

where MTTF = Mean Time To Failure, MTTR = Mean Time To Recovery.

## Epistemic Status

Definitional. This is the standard reliability engineering definition. AAD does not add to or modify it; it is imported as a prerequisite for #scope-continuous-operation, which extends the temporal optimization framework to account for operational failures.

## Discussion

Availability connects to AAD through #scope-continuous-operation: a non-operational system has effectively infinite implementation time for any feature. From the user's perspective, downtime is lost time. The temporal optimality postulate therefore applies to operational time as well as development time.
