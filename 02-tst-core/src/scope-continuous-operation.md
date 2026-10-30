---
slug: scope-continuous-operation
type: scope
status: axiomatic
depends:
  - scope-evolving-software
  - def-system-availability
  - post-temporal-optimality
  - hyp-mismatch-dynamics
stage: draft
---

# Scope: Continuous Operation

For systems that must operate while evolving, temporal optimization includes the expected cost of failures and recovery.

## Formal Expression

*[Scope (continuous-operation, extending scope-evolving-software)]*

For systems where $P(\text{perturbation}) \gt 0$ and $\text{required availability} \gt A_{\text{threshold}}$, the effective time includes operational cost:

$$T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$$

Under #post-temporal-optimality, this means minimizing the sum, not just the first term.

### The infinite-time observation

A non-operational system has effectively infinite implementation time for any feature from the user's perspective. Therefore, minimizing recovery time is not separate from minimizing development time — it is part of the same optimization.

## Epistemic Status

The scope extension is *definitional* — we choose to include operational time in the optimization. The consequence (effective time includes $P(\text{failure}) \times T_{\text{recovery}}$) follows from #post-temporal-optimality applied to the extended scope. The "infinite-time" observation is an asymptotic argument: as availability drops, effective feature delivery time grows without bound.

## Discussion

**Defensive vs. fault-tolerant.** Different design strategies optimize different terms:

- **Defensive programming**: high $T_{\text{implementation}}$ (validation, error handling), aims for low $P(\text{failure})$, often high $T_{\text{recovery}}$ when failures occur (complex systems fail complexly)
- **Fault-tolerant design** (e.g., "let it crash"): lower $T_{\text{implementation}}$, accepts higher $P(\text{failure})$, minimizes $T_{\text{recovery}}$ (fast restart, isolated failures)

When $T_{\text{recovery}} \ll T_{\text{defensive}}$, accepting and quickly recovering from failures is time-optimal. Supervision trees, circuit breakers, bulkheads, and health checks are all mechanisms that minimize $T_{\text{recovery}}$ — their widespread adoption is consistent with the temporal-optimality prediction, though the model captures only the time dimension of the design tradeoff.

**Perturbation types.** Systems face impulse perturbations (traffic spikes, deploys), sustained stress (degraded dependencies, memory leaks), and cascading failures (propagation through coupled components). Low #def-system-coupling limits cascade scope; fast recovery minimizes $T_{\text{recovery}}$; graceful degradation maintains partial #def-system-availability.

**Connection to AAT.** Perturbations are environmental disturbances ($\rho$) in the operational domain. The persistence condition ( #result-persistence-condition) applies: the team's operational tempo must exceed the disturbance rate relative to acceptable mismatch. A team that cannot recover faster than failures accumulate is in the unmaintainability regime.

**Availability as a tempo-to-incident-rate ratio.** *[Formulation (Conditional on Poisson incidents during uptime, recovery without background drift, and #hyp-mismatch-dynamics).]* Let incidents arrive at rate $\lambda_f$ while the system is up, so $\text{MTTF} = 1/\lambda_f$, and let none arrive during a repair. Let each incident open a mismatch $\delta_0$ that operational correction at tempo $\mathcal T_{\text{ops}}$ drives down exponentially until it is below an acceptable level $\delta_{\text{ok}}$, with no other disturbance acting meanwhile. Then $\text{MTTR} = c/\mathcal T_{\text{ops}}$ with $c = \mathbb E[\ln^{+}(\delta_0/\delta_{\text{ok}})]$, since an incident within tolerance costs no repair. The alternating-renewal form gives

$$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} = \frac{\mathcal T_{\text{ops}}}{\mathcal T_{\text{ops}} + c\,\lambda_f},$$

and an availability target $A^\ast$ is met exactly when $\mathcal T_{\text{ops}} \geq c\,\lambda_f\, A^\ast/(1 - A^\ast)$. With a background disturbance rate $\rho \gt 0$ during recovery, mismatch decays toward $\rho/\mathcal T_{\text{ops}}$ rather than zero, so a repair takes $\ln\!\big((\delta_0 - \rho/\mathcal T_{\text{ops}})/(\delta_{\text{ok}} - \rho/\mathcal T_{\text{ops}})\big)/\mathcal T_{\text{ops}}$ and finishes only if $\delta_{\text{ok}} \gt \rho/\mathcal T_{\text{ops}}$; the form above is the limit $\rho/\mathcal T_{\text{ops}} \ll \delta_{\text{ok}}$. Availability, like the persistence condition, compares correction tempo with the rate at which mismatch arrives. Incident size enters differently: logarithmically here, through $c$, and linearly in the persistence condition, where impulses of size $\delta_0$ at rate $\lambda_f$ amount to $\rho \approx \lambda_f\,\mathbb E[\delta_0]$. The target fixes the threshold. The two design strategies above act on different factors: defensive programming lowers $\lambda_f$, and fault-tolerant design raises $\mathcal T_{\text{ops}}$ and lowers $c$ by keeping incidents small.

## Working Notes

- The $P(\text{failure}) \times T_{\text{recovery}}$ term is an expected-value approximation. In practice, failure distributions are heavy-tailed — rare catastrophic failures may dominate the expectation. A risk-sensitive formulation (e.g., CVaR) might be more appropriate for critical systems, but AAT's temporal-optimality postulate as stated uses expected time.
- The scope extension is mild — it just says "count operational time too." But it has strong implications: development decisions that seem suboptimal under pure implementation time (T-08) become optimal when operational time is included. This is why the scope narrowing matters.
- TST T-15's perturbation taxonomy (impulse, stress, cascade) maps to AAT's disturbance characterization in the persistence condition. Impulse = spike in $\rho$; stress = sustained elevated $\rho$; cascade = $\rho$ amplified by coupling. The persistence condition handles all three through the $\rho$ term, but the qualitative distinction is useful for practitioners.
