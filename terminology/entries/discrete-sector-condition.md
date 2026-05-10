---
slug: discrete-sector-condition
schema_version: 1
term: discrete sector condition
name: Discrete Sector Condition
notation: "DA2'"
brief: The discrete-time analog of the sector condition — adds a Lipschitz magnitude bound (DA2'b) to the directional fidelity lower bound (DA2'a), closing the fluid-limit gap between event-driven and continuous-time Lyapunov results.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aad-core/src/deriv-discrete-sector-condition.md
first_asf_mention: 01-aad-core/src/deriv-discrete-sector-condition.md
see_also: [sector-condition, adaptive-system, event-driven-dynamics, adaptive-reserve]
aliases: ["DA2'"]
do_not_confuse: [sector-condition]
---

The continuous-time sector condition (A2') requires only a one-sided inner-product bound
$\delta^T F \geq \alpha\|\delta\|^2$ because $\dot V$ depends only on $\delta^T F$. Discretization
introduces a quadratic term $(\eta^\ast)^2 \|F_d\|^2$ in the per-step recurrence, requiring an
additional **Lipschitz magnitude bound**:

- **(DA2'a) Lower sector bound**: $\delta^T F_d(\delta) \geq c_{\min}\|\delta\|^2$ (directional fidelity, identical to continuous A2')
- **(DA2'b) Lipschitz bound**: $\|F_d(\delta)\| \leq c_{\max}\|\delta\|$ (bounded correction magnitude)

The combined constraint $c_{\max} < 2/\eta^\ast$ is the **no-overshoot condition**. Under DA2',
per-step Lyapunov decay gives contraction factor $\lambda_{\text{eff}}^2 = 1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2$.

Three propositions follow directly: **DA.1** (bounded mismatch, deterministic: $R^\ast_D = \rho_\text{step}/(1-\lambda_\text{eff})$), **DA.2** (discrete adaptive reserve), and **DA.1S** (mean-square bounded mismatch, stochastic). In the fluid limit (high event rate, fixed $\mathcal{T} = \nu\eta^\ast$), all three recover the continuous results exactly for Model D; the Model S gap is $O(c_{\max}^2/(c_{\min}^2\nu))$ — small when well-conditioned.

**Significance**: closes the fluid-limit gap (GA-5) between event-driven dynamics and continuous-time Lyapunov analysis. The discrete and continuous frameworks now form a complete, bridged pair.

Derived in [`#deriv-discrete-sector-condition`](../../01-aad-core/src/deriv-discrete-sector-condition.md).
