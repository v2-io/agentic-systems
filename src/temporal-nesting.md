---
slug: temporal-nesting
type: derived
status: robust-qualitative
depends:
  - adaptive-tempo
  - structural-adaptation-necessity
---

# Derived: Temporal Nesting

An agent's adaptive processes stratify naturally by timescale, with each level operating on the quasi-steady-state output of the level below. Faster processes must approximately converge before slower ones act on their output.

## Formal Expression

*[Derived (temporal-nesting)]*

$$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$$

for each adjacent pair of adaptive timescales. If a slower process acts before the faster process beneath it has converged, the system oscillates — the slower process adjusts based on transient behavior rather than settled dynamics.

| Timescale | Process | What changes |
|-----------|---------|-------------|
| Fastest | Reactive response | Action given current model |
| Fast | Parametric update | Model parameters within $\mathcal{M}$ |
| Slow | Structural adaptation | Model class $\mathcal{M}$ |
| Slowest | Architectural change | The agent's fundamental structure |

This table is illustrative — real systems may have additional intermediate levels. The number of distinguishable timescales is not fixed; what matters is the structural relationship between adjacent levels.

## Epistemic Status

*Robust qualitative* — this is standard singular perturbation reasoning (Tikhonov's theorem). The convergence constraint follows from the structure of multi-timescale updating. The specific timescale ratios needed for adequate separation are domain-dependent and not derived within ACT.

## Discussion

**Domain instantiations of temporal nesting:**

- **PID control**: D-term (fastest, high-frequency response) → P-term (current error) → I-term (slowest, accumulated bias)
- **RL**: Action selection → value function update → policy improvement → architecture change
- **Biology**: Reflexes (ms) → perceptual learning (minutes) → skill acquisition (months) → developmental change (years) → evolutionary adaptation (generations)
- **Organizations**: Operational decisions (hours) → tactical adjustments (weeks) → strategic revision (quarters) → restructuring (years)
- **Boyd**: Tactical OODA (seconds–minutes) → operational (hours–days) → strategic (weeks–months) → grand strategic (years)

**Structural adaptation as slow-timescale dynamics.** The conservatism toward structural change ( #structural-adaptation-necessity) is a derived consequence of temporal nesting: structural adaptation operates at a much slower timescale than parametric, so the mismatch cost of the "pause" ($\rho \cdot \Delta\tau$) is enormous. The agent rationally resists until the parametric mismatch floor exceeds this cost. See also #deliberation-cost for the formal tradeoff.

**Violation symptoms.** When nesting is violated (a slower process acts before the faster one converges): oscillation, instability, degraded performance. In organizations: micromanagement (strategic decisions at operational tempo). In RL: policy updates before value function converges (policy oscillation). In biology: premature developmental transitions.

**Multi-timescale stability (sketch).** Singular perturbation theory gives the composite stability result: if each level is stable given the levels above it (each level has a stable attractor for fixed slower-level parameters), and the timescale separation is sufficient, the composite $N$-level system is stable. Making this rigorous for ACT requires specifying dynamics at deeper adaptive levels — an open problem. See #multi-timescale-stability for the framework.

**(Descended from TF-11.)**
