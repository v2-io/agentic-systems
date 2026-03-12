---
slug: continuous-operation
type: scope
status: axiomatic
depends:
  - software-scope
  - system-availability
  - temporal-optimality
---

# Scope: Continuous Operation

For systems that must operate while evolving, temporal optimization includes the expected cost of failures and recovery.

## Formal Expression

*[Scope (continuous-operation, extending software-scope)]*

For systems where $P(\text{perturbation}) \gt 0$ and $\text{required availability} \gt A_{\text{threshold}}$, the effective time includes operational cost:

$$T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$$

Under #temporal-optimality, this means minimizing the sum, not just the first term.

### The infinite-time observation

A non-operational system has effectively infinite implementation time for any feature from the user's perspective. Therefore, minimizing recovery time is not separate from minimizing development time — it is part of the same optimization.

## Epistemic Status

The scope extension is *definitional* — we choose to include operational time in the optimization. The consequence (effective time includes $P(\text{failure}) \times T_{\text{recovery}}$) follows from #temporal-optimality applied to the extended scope. The "infinite-time" observation is an asymptotic argument: as availability drops, effective feature delivery time grows without bound.

## Discussion

**Defensive vs. fault-tolerant.** Different design strategies optimize different terms:

- **Defensive programming**: high $T_{\text{implementation}}$ (validation, error handling), aims for low $P(\text{failure})$, often high $T_{\text{recovery}}$ when failures occur (complex systems fail complexly)
- **Fault-tolerant design** (e.g., "let it crash"): lower $T_{\text{implementation}}$, accepts higher $P(\text{failure})$, minimizes $T_{\text{recovery}}$ (fast restart, isolated failures)

When $T_{\text{recovery}} \ll T_{\text{defensive}}$, accepting and quickly recovering from failures is time-optimal. Supervision trees, circuit breakers, bulkheads, and health checks are all mechanisms that minimize $T_{\text{recovery}}$ — their widespread adoption is consistent with the temporal-optimality prediction, though the model captures only the time dimension of the design tradeoff.

**Perturbation types.** Systems face impulse perturbations (traffic spikes, deploys), sustained stress (degraded dependencies, memory leaks), and cascading failures (propagation through coupled components). Low #system-coupling limits cascade scope; fast recovery minimizes $T_{\text{recovery}}$; graceful degradation maintains partial #system-availability.

**Connection to ACT.** Perturbations are environmental disturbances ($\rho$) in the operational domain. The persistence condition ( #persistence-condition) applies: the team's operational tempo must exceed the disturbance rate relative to acceptable mismatch. A team that cannot recover faster than failures accumulate is in the unmaintainability regime.

## Working Notes

- The $P(\text{failure}) \times T_{\text{recovery}}$ term is an expected-value approximation. In practice, failure distributions are heavy-tailed — rare catastrophic failures may dominate the expectation. A risk-sensitive formulation (e.g., CVaR) might be more appropriate for critical systems, but ACT's temporal-optimality postulate as stated uses expected time.
- The scope extension is mild — it just says "count operational time too." But it has strong implications: development decisions that seem suboptimal under pure implementation time (T-08) become optimal when operational time is included. This is why the scope narrowing matters.
- TST T-12's perturbation taxonomy (impulse, stress, cascade) maps to ACT's disturbance characterization in the persistence condition. Impulse = spike in $\rho$; stress = sustained elevated $\rho$; cascade = $\rho$ amplified by coupling. The persistence condition handles all three through the $\rho$ term, but the qualitative distinction is useful for practitioners.

*(Descended from TST T-12, D-08.)*
