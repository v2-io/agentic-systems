---
slug: persistence-cost
schema_version: 1
term: persistence cost
name: Persistence Cost
notation: "$\\dot R_{\\min}$"
brief: The minimum Shannon information rate an agent must acquire from observations to hold its estimation error at a given level — the sequential rate-distortion function, met exactly by the Kalman–Bucy filter.
layer: prose-symbol
status: canon
tags: [core_quantities, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/deriv-persistence-cost.md
first_asf_mention: 01-aat-core/src/deriv-persistence-cost.md
see_also: [adaptive-reserve, adaptive-tempo, structural-persistence, adaptive-system]
aliases: []
do_not_confuse: []
---

Under Model S with an $n$-dimensional Ornstein–Uhlenbeck signal, any causal estimator holding the per-component mean-square estimation error at $D$ must take in information at sustained rate (the sequential rate-distortion function):

$$\dot R \;\geq\; n\left(\frac{\sigma_w^2}{2D} - \lambda_s\right) \text{ nats per unit time}$$

The Kalman–Bucy filter meets this with equality, at rate $n\alpha/2$ where $\alpha$ is its correction gain (Duncan 1970; Mitter & Newton 2005). The bound is **filter-agnostic** — it constrains every causal estimator holding that error.

A first-class persistence diagnostic follows: for the Kalman-optimal agent the observation channel must have Shannon capacity $C_{\text{channel}} \geq \mathcal{T}/2$ nats/time per dimension. This **channel-capacity floor** is a persistence prerequisite the correction-rate inequality ($\alpha \gt \rho/R$) does not name. It is most binding where observation bandwidth is scarce: biological neurons, bandwidth-constrained distributed systems, and context-window-limited LLMs.

The result has a thermodynamic reading (Still et al. 2012): each nat of information about the signal costs at least $k_BT$ of dissipation, so the Kalman-optimal agent persisting at correction rate $\alpha$ in $n$ dimensions dissipates at least $\tfrac12 n\alpha\, k_BT$ per unit time.

Derived in [`#deriv-persistence-cost`](../../01-aat-core/src/deriv-persistence-cost.md).
