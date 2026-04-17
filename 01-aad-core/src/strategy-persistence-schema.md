---
slug: strategy-persistence-schema
type: proposed-schema
status: sketch
depends:
  - sector-condition-stability
  - strategic-calibration
  - strategy-dag
stage: draft
---

# Proposed-schema: Strategy Persistence Schema

The sector-condition mathematics ( #sector-condition-stability, #sector-condition-derivation) proves bounded mismatch for any system with: a mismatch state, a correction function satisfying sector bounds, and bounded disturbance. This mathematics is domain-agnostic — it doesn't care whether the mismatch is epistemic or strategic. If the strategic update dynamics can be shown to satisfy the same structural conditions, strategy persistence follows by the same result.

## Formal Expression

*[Proposed Schema (strategy-persistence-schema)]*

**If** strategic update dynamics satisfy:
- **(SA1)** Zero correction at zero strategic mismatch: when the mismatch state is zero, no revision occurs
- **(SA2')** Local sector condition on strategic correction: the correction function is appropriately bounded
- **(SA3)** Sufficient exploration (OR-nodes only): the action selection policy allocates correction capacity to all OR alternatives at a rate exceeding the strategic disturbance-to-reserve ratio
- Bounded strategic disturbance: the rate at which the environment invalidates causal links is bounded

**Then** $\Sigma_t$ persists iff:

$$\alpha_\Sigma \gt \frac{\rho_\Sigma}{R_\Sigma}$$

where $\alpha_\Sigma$ is the strategic correction rate, $\rho_\Sigma$ is the strategic disturbance rate, and $R_\Sigma$ is the strategic reserve (tolerance for strategic mismatch before performance degrades catastrophically).

**Which mismatch state?** The schema applies to any mismatch state for which conditions (SA1)-(SA3) can be verified. Two candidates exist:

- **Plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$: the scalar difference between the agent's plan-confidence score and the independence-model plan value at true edge parameters. This is the mismatch for which persistence IS proved (Props B.1-B.5 in #strategic-dynamics-derivation). It is computable from status propagation without credit assignment. **Scope:** $\delta_s$ operates at L0 of the Correlation Hierarchy ( #strategy-dag) — it tracks calibration within the independence model. For L1 (augmented DAG), the same persistence result applies to the augmented graph's $\hat P_\Sigma$. The gap between L0's $\Phi$ and actual plan success under correlated failure is a model-class limitation, not an estimation error.
- **Strategic-calibration residual** $\delta_{\text{strategic}}$: the per-edge value-increment residual aggregation defined in #strategic-calibration. This is the mismatch the orient cascade ( #orient-cascade) uses for edge-level revision. Persistence of $\delta_{\text{strategic}}$ remains **open** and requires the credit-assignment machinery in #credit-assignment-boundary.

The verified instances below all use per-edge credence error $\boldsymbol\delta_c = (\hat p_k - \theta_k)$ or the plan-level surrogate $\delta_s$. They do not verify the schema for $\delta_{\text{strategic}}$ directly.

## Epistemic Status

*Sketch, with verified instances.* This is a **result schema**, not a proven result in the general case. The mathematical template (sector conditions → bounded mismatch) is derived ( #sector-condition-derivation). What was missing was instantiation — showing that specific strategic update dynamics satisfy the template's preconditions. Four cases have now been verified (full derivations in #strategic-dynamics-derivation):

1. **Single edge, Beta-Bernoulli** ($A \to G$): Sector condition satisfied globally with $\alpha_\Sigma = 1/(n+1)$. The bound is tight (expected correction is exactly linear). (A1) satisfied. Persistence condition: $1/(n+1) > \rho_\Sigma / R_\Sigma$.

2. **Two-edge chain, observable intermediate** ($A \to B \to G$, $B$ observable): Sector condition satisfied globally with $\alpha_\Sigma = \min(1/(n_1+1), \theta_1/(n_2+1))$ — a weakest-link result. Correction function is diagonal (no cross-edge coupling). (A1) satisfied. The $\theta_1$ factor in edge 2's rate is the evidence-starvation effect.

3. **Two-edge chain, unobservable intermediate** ($A \to B \to G$, $B$ not observable): Per-edge sector condition **fails** — the marginal Bayesian update violates (A1) with bias $O(1/n)$. But plan-level tracking (treating $\hat{\Phi} = p_1 p_2$ as a single Beta) recovers the sector condition with $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$, at the cost of per-edge diagnostic resolution.

4. **Two-arm OR-node, $\varepsilon$-greedy** ($A_1, A_2 \to G$, $G$ is OR): Sector condition satisfied with $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ — an **exploration-gated** weakest-link, not depth-gated as in AND chains. (SA3) required: minimum exploration rate $\varepsilon > \rho_\Sigma(n_{\max}+1)/R_\Sigma$. Pure greedy ($\varepsilon = 0$) **fails** the sector condition. With optimal equal-rate allocation, $\alpha_\Sigma = 1/(n_1 + n_2 + 2)$ — the correction capacity is split across alternatives.

The schema is no longer purely hypothetical. The sector parameter for strategic dynamics is the edge update gain $\eta_{\text{edge}}$ — the same quantity that governs epistemic persistence. The structural parallel between epistemic and strategic persistence is not an analogy but a mathematical identity at the sector-framework level.

## Discussion

**What's needed to promote this from schema to result.**

1. **Strategic mismatch state**: partially resolved. Prop B.5 in #strategic-dynamics-derivation shows the sector condition transfers from per-edge credence error to **plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ — the scalar difference between the agent's plan-confidence score and the independence-model plan value at true edge parameters (note: $\Phi$ is NOT actual plan success probability under correlated failure — see #strategy-dag edge-independence caveat). For linear correction (Beta-Bernoulli), the transfer is exact ($\alpha_s = \alpha_c$); for nonlinear correction, $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$. **However**, $\delta_s$ is distinct from the **strategic-calibration residual** $\delta_{\text{strategic}}$ defined in #strategic-calibration, which is an $L^2$ aggregation of per-edge value-increment residuals requiring credit assignment to compute. Persistence of $\delta_s$ (plan-level tracking) is proved; persistence of $\delta_{\text{strategic}}$ (per-edge diagnostics) remains open and requires the credit-assignment machinery in #credit-assignment-boundary.

2. ~~**Strategic correction function**: needs to satisfy the sector condition.~~ **Resolved** for Beta-Bernoulli edges. Props B.1-B.4 in #strategic-dynamics-derivation verify the sector condition for four topologies (single edge, two-edge AND observable/unobservable, two-arm OR).

3. **Strategic disturbance**: The rate at which the environment invalidates causal links in $\Sigma_t$. **Still open** as a formalized quantity — currently a domain parameter ($\rho_\Sigma$), analogous to how $\rho$ for epistemic disturbance is a domain parameter in #persistence-condition.

4. ~~**Sector condition verification**: the critical mathematical step.~~ **Resolved** for four topologies. See #strategic-dynamics-derivation.

5. ~~**Credit assignment / signal function**: needed for edge updates.~~ **Characterized at the theory level.** #credit-assignment-boundary shows persistence does not require credit assignment (Prop B.5), establishes directional fidelity as the minimal requirement, and provides a gradient-based default signal function. The specific update algorithm is domain engineering, not theory — the same way the gain *estimator* is domain engineering while the gain *principle* ($\eta^\ast = U_M/(U_M + U_o)$) is theory. Caveat: the default gradient signal inherits $\hat P_\Sigma$'s overestimation bias under correlated failures ( #strategy-dag, #credit-assignment-boundary).

**The structural parallel is genuine.** This schema extends *structural persistence* (see Persistence in `LEXICON.md`) from the epistemic substate to the strategy substate — asking whether the strategy correction machinery can outpace the rate at which the environment invalidates the agent's causal theory. It inherits the same limitation: structural persistence of $\Sigma_t$ does not address operational persistence (how close $\lVert\delta_{\text{strategic}}\rVert$ is to $R_\Sigma$) or continuity persistence (whether the agent's strategic identity coheres through time). The persistence condition for $M_t$ ( #persistence-condition) says: adaptive tempo must exceed the ratio of disturbance to critical mismatch. If the same mathematics applies to $\Sigma_t$, then strategy persistence requires strategic tempo to exceed the ratio of strategic disturbance to critical strategic mismatch. The strategic analog of "the environment changes faster than the agent can learn" is "the world invalidates plans faster than the agent can revise them." Both lead to the same catastrophic outcome: the system cannot maintain bounded mismatch and begins to degrade.

**What this would buy the theory.** If promoted to a result, strategy persistence would:
- Provide a formal criterion for "when does a strategy remain viable?"
- Connect strategic failure modes to the same mathematical framework as epistemic failure modes
- Enable quantitative comparison: is the bottleneck epistemic persistence (model can't keep up with reality changes) or strategic persistence (plans can't keep up with requirement changes)?
- Ground the organizational intuition that plans need to be revised faster than the situation changes

## Working Notes

- **Done.** Five cases verified: single-edge AND, two-edge AND (observable and unobservable intermediate), two-arm OR ($\varepsilon$-greedy), and mixed AND/OR with common-cause node (L1 augmented DAG). Full derivations in #strategic-dynamics-derivation (Props B.1–B.6). Key findings: AND-node persistence is depth-gated (evidence starvation); OR-node persistence is exploration-gated (action selection policy); L1 augmented DAGs exhibit three-way gating (condition testing × starvation × exploration). All satisfy the schema's form ($\alpha_\Sigma > \rho_\Sigma/R_\Sigma$). B.6 is the first mixed AND/OR case and confirms L1 results transfer from L0 with correct construction. The next step is deeper mixed topologies and multiple common causes.
- **Strategic tempo now formalized.** #strategic-tempo defines $\mathcal{T}_\Sigma = \sum_{(i,j)} \nu_{ij} \cdot \eta_{\text{edge},ij}$ and verifies consistency with all four cases. The relationship to the schema's sector parameter: $\alpha_\Sigma \leq \mathcal{T}_\Sigma / |E|$ (persistence is bottleneck-limited, not throughput-limited). #strategy-complexity-cost provides the IB/MDL framework for strategy compression and derives max useful depth $d^\ast$.
- The strategic disturbance $\rho_\Sigma$ is qualitatively different from epistemic disturbance $\rho$. Epistemic disturbance is about the environment changing (physical state evolves). Strategic disturbance is about the agent's causal theory becoming invalid (the intervention-outcome mapping shifts). These can be correlated (a changing environment invalidates both model and strategy) but they're not the same quantity.
- The stochastic treatment (from track-b simulations) suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$ for the steady-state strategic mismatch. If this carries over from the epistemic domain, the persistence threshold is different in the stochastic case. Whether strategic disturbance is better modeled as deterministic or stochastic drift is domain-dependent.
