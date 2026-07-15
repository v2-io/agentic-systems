---
slug: variational-sector-condition
schema_version: 1
term: variational sector condition
name: Variational Sector Condition
notation:
brief: The $\varepsilon$-fidelity extension of the sector condition to variational/approximate-posterior agents — sector constant degrades by $O(\sqrt\varepsilon)$ under a KL bound on the approximation, promoting controlled-KL VI to sub-scope $\alpha'$.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/deriv-variational-sector-condition.md
first_asf_mention: 01-aat-core/src/deriv-variational-sector-condition.md
see_also: [sector-condition, adaptive-system, adaptive-gain-dynamics]
aliases: ["$\\varepsilon$-fidelity sector condition"]
do_not_confuse: [sector-condition]
---

Variational / approximate-posterior agents (VI, amortized VI, active-inference variational free energy) currently sit in A2' sub-scope $\beta$ because their correction functions target the *best-in-class* variational posterior $q^\ast$ rather than the true posterior $p$. The approximation gap can rotate the correction direction enough to break directional fidelity.

Under a KL bound $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$, directional fidelity recovers in a quantifiable form: the effective sector constant

$$c_\varepsilon(\lVert\delta\rVert) = c_{\min} - C_H\sqrt{2\varepsilon}/\lVert\delta\rVert$$

is state-dependent. A **Regime-A / Regime-B decomposition** results: on the annulus
$\lVert\delta\rVert \gt 2\delta_0$ (Regime A), the sector condition holds with constant
$c_{\min}/2$; near the target (Regime B, $\lVert\delta\rVert \leq 2\delta_0$), the ultimate bound acquires an additive $O(\sqrt\varepsilon)$ floor.

This promotes **controlled-KL VI** from sub-scope $\beta$ to a new intermediate tier $\alpha'$
in the A2' partition. Natural-gradient VI with exponential-family $q_\phi$ recovers full sub-scope $\alpha$ (exact, via Khan & Lin 2017). Uncontrolled-$\varepsilon$ agents
(diffusion posteriors, VAEs without KL control) remain in $\beta$.

The $\varepsilon$-$\alpha'$ tradeoff: large $\varepsilon$ means cheap-but-persistently-weak;
small $\varepsilon$ means expensive-but-persistently-sharp.

Derived in [`#deriv-variational-sector-condition`](../../01-aat-core/src/deriv-variational-sector-condition.md).
