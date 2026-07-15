---
slug: continuous-operation
schema_version: 1
term: continuous operation
name: Continuous Operation
notation:
brief: The TST scope extension that folds failure-and-recovery cost into the temporal-optimality objective — effective time includes implementation time plus the expected cost of operational failures.
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 02-tst-core/src/scope-continuous-operation.md
first_asf_mention: 02-tst-core/src/scope-continuous-operation.md
see_also: [temporal-optimality, developer-agent, atomic-changeset]
aliases: []
do_not_confuse: []
---

For systems where $P(\text{perturbation}) \gt 0$ and required availability exceeds a threshold,
temporal optimization must account for operational cost:

$$T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$$

Under [temporal optimality](temporal-optimality.md), the objective is to minimize
$T_{\text{effective}}$, not just $T_{\text{implementation}}$. The **infinite-time observation**
makes this concrete: a non-operational system has effectively infinite implementation time for any feature from the user's perspective, so minimizing recovery time is not separate from minimizing development time — it is part of the same optimization.

This explains why fault-tolerance patterns (supervision trees, circuit breakers, bulkheads,
health checks) are time-optimal under the right conditions: when recovery time $T_{\text{recovery}}$
is much smaller than the defensive programming overhead $T_{\text{defensive}}$, accepting and quickly recovering from failures beats building deeply defensive systems. In AAT terms: system perturbations are environmental disturbances ($\rho$) in the operational domain; a team that cannot recover faster than failures accumulate is in the unmaintainability regime.

Scope defined in [`#scope-continuous-operation`](../../02-tst-core/src/scope-continuous-operation.md).
