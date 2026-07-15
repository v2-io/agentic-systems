---
slug: strategy-persistence
schema_version: 1
term: strategy persistence
name: Strategy Persistence
notation:
brief: The strategic-layer instantiation of sector persistence — $\Sigma_t$ persists iff the strategic correction rate exceeds disturbance-to-reserve ratio, with forgetting as a structural prerequisite (not a tunable heuristic).
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/schema-strategy-persistence.md
first_asf_mention: 01-aat-core/src/schema-strategy-persistence.md
see_also: [strategy-dag, strategic-tempo, structural-persistence, adaptive-reserve, sector-condition]
aliases: []
do_not_confuse: [structural-persistence, operational-persistence]
---

The sector-persistence template applied to $\Sigma_t$: strategy persists iff

$$\alpha_\Sigma \gt \frac{\rho_\Sigma}{R_\Sigma}$$

where $\alpha_\Sigma$ is the strategic correction rate, $\rho_\Sigma$ is the rate at which the environment invalidates causal links, and $R_\Sigma$ is the strategic reserve.

**The critical difference from epistemic persistence**: For Beta-Bernoulli edge updates, the sector parameter $\alpha_\Sigma = 1/(n+1)$ decays monotonically with accumulated experience $n$.
Without a forgetting mechanism, $\alpha_\Sigma \to 0$ and every agent eventually violates the threshold. Exponential forgetting with discount factor $\lambda$ stabilizes the effective sample size at $1/(1-\lambda)$, giving steady-state $\alpha_\Sigma^{ss} \approx 1-\lambda$. The
**forgetting prerequisite**:

$$(1-\lambda) \gt \frac{\rho_\Sigma}{R_\Sigma}$$

is a **structural prerequisite of the trajectory guarantee**, not a tunable heuristic. An agent without forgetting has no long-run strategic persistence regardless of initial calibration. The forgetting rate $(1-\lambda)$ plays the role of adaptive tempo in the strategic analog of the persistence condition: faster forgetting means faster tracking but noisier estimates.

Organizational calcification, RL value-function staleness, scientific-paradigm lock-in, and the loss-of-edge phenomenon in incumbent firms all instantiate the same dynamic.

Proposed schema in [`#schema-strategy-persistence`](../../01-aat-core/src/schema-strategy-persistence.md).
