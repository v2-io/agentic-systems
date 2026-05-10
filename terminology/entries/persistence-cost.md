---
slug: persistence-cost
schema_version: 1
term: persistence cost
name: Persistence Cost
notation: "$\\dot{R}_{\\min}$"
brief: The minimum Shannon information rate an agent must acquire from observations to maintain bounded mismatch — a Landauer-analog lower bound derived from the rate-distortion theorem.
layer: prose-symbol
status: canon
tags: [core_quantities, structural_concepts]
source_type: asf
primary_source: 01-aad-core/src/deriv-persistence-cost.md
first_asf_mention: 01-aad-core/src/deriv-persistence-cost.md
see_also: [adaptive-reserve, tempo, structural-persistence, adaptive-system]
aliases: []
do_not_confuse: []
---

Under Model S (stochastic disturbance) with $n$-dimensional Ornstein-Uhlenbeck signal, any
adaptive process achieving the tight sector-persistence ultimate bound must acquire information
from observations at sustained rate:

$$\dot R_{\min} = \frac{n\alpha}{2} \text{ nats per unit time}$$

where $\alpha$ is the sector constant. The Kalman-Bucy filter achieves this bound exactly
(Mitter-Newton 2005). The bound is **filter-agnostic** — it constrains any implementation via
Shannon's rate-distortion theorem, regardless of the correction function's specific form.

A first-class persistence diagnostic follows: the observation channel must have Shannon capacity
$C_{\text{channel}} \geq \mathcal{T}/2$ nats/time per dimension. This **channel-capacity floor**
is the persistence prerequisite the current tempo framework ($\alpha > \rho/R$) does not name.
It is most binding where observation bandwidth is non-abundant: biological neurons, bandwidth-
constrained distributed systems, and context-window-limited LLMs.

The result has a thermodynamic reading (Still et al. 2012): each nat of information about the
signal costs at least $k_BT$ of dissipation, so persistence at sector constant $\alpha$ in $n$
dimensions costs at least $n\alpha k_BT/(2\ln 2)$ of thermodynamic dissipation per unit time.

Derived in [`#deriv-persistence-cost`](../../01-aad-core/src/deriv-persistence-cost.md).
