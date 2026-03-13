---
slug: team-persistence
type: derived
status: conditional
depends:
  - persistence-condition
  - sector-condition-stability
  - communication-gain
  - adaptive-tempo
---

# Derived: Team Persistence

Teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo while reducing effective disturbance.

## Formal Expression

### Distributed Tempo

*[Definition (distributed-tempo)]*

Agent $i$'s effective tempo includes contributions from both direct observation and communication from allies:

$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{direct observation tempo}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communication tempo}}$$

where $\nu_{ji}^{\text{comm}}$ is the rate of communication events from agent $j$ to agent $i$, and $\eta_{ji}^\ast$ is the communication gain ( #communication-gain). Faster team adaptation comes not only from faster individual sensing but from faster, more reliable knowledge transfer.

### Cooperative-Adversarial Disturbance Decomposition

*[Formulation (disturbance-decomposition)]*

The disturbance rate experienced by agent $i$ decomposes into environment, adversarial, and cooperative components:

$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j \to i}^{\text{adv}} \, \mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \, \mathcal{T}_j$$

where $\mathcal A_i$ is the set of agents adversarially coupled to $i$, $\mathcal C_i$ is the set cooperatively coupled, and the $\gamma$ coefficients capture coupling effectiveness (as in #adversarial-destabilization).

**The cooperative term is negative.** Allies reduce agent $i$'s effective disturbance by sharing information that preemptively corrects mismatch — each cooperative communication event that arrives before the corresponding environment disturbance would have been observed effectively cancels a unit of disturbance. This is the structural pattern consistent with why teams can persist in environments where individuals cannot: cooperative communication tempo offsets environment disturbance that would exceed any single agent's capacity.

**Effective disturbance rate.** The decomposition can yield $\rho_i \lt 0$ when cooperative coupling dominates both environment disturbance and adversarial coupling. The sector-condition analysis ( #sector-condition-stability) assumes non-negative disturbance (GA-2). Define:

*[Definition (effective-disturbance)]*

$$\rho_i^{\text{eff}} = \max(\rho_i, \, 0)$$

When $\rho_i^{\text{eff}} = 0$, the agent's cooperative network fully absorbs all disturbance — the persistence condition is trivially satisfied and mismatch decays to zero. This is an idealized limit; in practice, $\rho_i^{\text{eff}} \gt 0$ because cooperative coupling is imperfect and environment disturbance is never fully preempted. All downstream uses of $\rho_i$ in the persistence and reserve conditions should be read as $\rho_i^{\text{eff}}$.

### Team Persistence Condition

*[Derived (team-persistence, from sector-condition-stability, persistence-condition)]*

Applying the sector-condition framework ( #sector-condition-stability) with $\rho_i^{\text{eff}}$, agent $i$ persists iff:

$$\frac{\rho_i^{\text{eff}}}{\alpha_i} \lt R_i$$

Substituting the decomposition (the $\max(\cdot, 0)$ in $\rho_i^{\text{eff}}$ is omitted to expose the three levers; the condition is trivially satisfied when the numerator is non-positive):

$$\frac{\rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\alpha_i} \lt R_i$$

This reveals three distinct levers for team persistence:

1. **Increase $\alpha_i$** (individual correction efficiency) — better models, better gain calibration
2. **Increase cooperative tempo** ($\gamma^{\text{coop}} \mathcal T_j$) — more reliable allies, faster communication channels
3. **Reduce adversarial coupling** ($\gamma^{\text{adv}} \mathcal T_j$) — better deception detection, reduced exposure to adversarial actions

### Coordination Overhead Threshold

*[Discussion — Coordination Threshold]*

Communication channels have costs: time to compose and parse messages, bandwidth limitations, synchronization requirements. These costs reduce the agent's effective tempo by diverting capacity from direct adaptation. Let $\Delta \mathcal T_i^{\text{cost}}(j)$ represent the tempo-equivalent coordination cost of maintaining the channel with $j$ — the reduction in $i$'s direct observation tempo caused by the overhead, in units of $[t^{-1}]$.

The net benefit of adding agent $j$ to $i$'s communication network is positive only when:

$$\nu_{ji}^{\text{comm}} \, \eta_{ji}^* \gt \Delta \mathcal{T}_i^{\text{cost}}(j)$$

Both sides have units $[t^{-1}]$: the LHS is communication tempo gained, the RHS is direct-adaptation tempo lost to coordination overhead. This implies a natural team-size limit: adding members increases communication tempo with diminishing returns (as $U_{\text{src}}$ and $U_o$ accumulate across diverse sources) while coordination costs grow, potentially superlinearly. The optimal team size occurs where the marginal communication tempo equals the marginal coordination cost.

## Epistemic Status

Conditional on the communication-gain hypothesis ( #communication-gain). The distributed tempo definition is a *formulation* — a representational choice extending #adaptive-tempo to the multi-agent case. The disturbance decomposition is a *formulation* — the additive structure and the sign convention are modeling choices, not derivations. The persistence condition is *derived* from the sector-condition framework ( #sector-condition-stability) given the decomposition: the derivation is exact under the same assumptions (GA-2, GA-3 applied to $\rho_i^{\text{eff}}$). The coordination overhead threshold is *discussion-grade* — qualitatively clear but the claim about diminishing returns and superlinear costs is asserted, not derived.

Max attainable: *robust-qualitative* for the persistence condition (it inherits the sector-condition's robustness but the decomposition is a modeling choice). The coordination threshold could reach *conditional* with a concrete cost model.

## Discussion

**Compositional analog of #persistence-condition.** The single-agent persistence condition says an agent persists when $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$. This segment extends that condition to agents embedded in a cooperative-adversarial network. The formal structure is identical — the sector-condition machinery applies unchanged — but the *inputs* ($\mathcal T_i$ and $\rho_i$) now include inter-agent terms. This is consistent with #composition-consistency: the same dynamical laws apply at every level of description; what changes between levels is which channels contribute to tempo and which sources contribute to disturbance.

**Why teams can persist where individuals cannot.** The cooperative term $\sum_j \gamma_{j \to i}^{\text{coop}} \mathcal T_j$ is subtracted from the disturbance rate. An individual agent facing $\rho_{i,\text{env}} \gt \alpha_i R_i$ fails the persistence condition. Adding cooperative allies with sufficient communication tempo can reduce $\rho_i^{\text{eff}}$ below the persistence threshold without any change to the individual's own capabilities. The mechanism is information-theoretic: allies provide observations the agent could not make on its own timescale.

**Timescale separation and #composition-consistency.** The distributed tempo definition presumes that communication events and direct observation events are comparable — they enter additively into $\mathcal T_i$. This requires that the communication timescale is not so slow relative to the environment dynamics that communicated information is stale on arrival. When communication latency approaches $1/\rho_{i,\text{env}}$, the effective $\eta_{ji}^\ast$ degrades (the observation uncertainty $U_{o,ji}$ increases with staleness), naturally suppressing the communication tempo contribution.

**Complement to #adversarial-destabilization.** That segment characterizes when an adversary can push an agent past its stability boundary. This segment characterizes the cooperative counterpart: when allies can pull an agent back from instability. The $\gamma$ coefficients have the same structure — coupling effectiveness — but opposite sign in the disturbance decomposition.

## Working Notes

- The topology-dependent analysis (F.4 in the source material — peer networks, ensemble architectures, hierarchical structures) and game-theoretic integration (F.5) are related but separate concerns, not covered here. They may warrant their own segments.
- The coordination cost model $\Delta \mathcal T_i^{\text{cost}}(j)$ needs further specification to be useful. In software systems, coordination cost is empirically measurable (meeting time, code review latency, merge conflict rates). In military contexts, it maps to C2 overhead. The question is whether there is a useful *general* cost model or whether it is always domain-specific.
- The disturbance decomposition treats cooperative and adversarial coupling as additive and independent. In practice, the same agent $j$ might be cooperatively coupled on some dimensions and adversarially coupled on others (e.g., a competitor who shares some information). The per-dimension persistence condition ( #persistence-condition's per-dimension extension) may be relevant here.

*(Descended from TFT Appendix F, Section F.3.)*
