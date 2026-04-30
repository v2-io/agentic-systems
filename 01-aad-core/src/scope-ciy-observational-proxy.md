---
slug: scope-ciy-observational-proxy
type: scope
status: conditional
depends:
  - def-causal-information-yield
  - der-loop-interventional-access
stage: draft
---

# Scope: CIY Observational Proxy

When and how causal information yield can be approximated from observational data rather than interventional experiments.

## Formal Expression

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is **sign-indefinite in general** and requires causal assumptions for interpretation. The canonical CIY (interventional, #def-causal-information-yield) is the primary quantity; the proxy is auxiliary.

**Safety conditions for proxy use.** The proxy form should NOT be used in policy optimization (e.g., as the CIY term in a policy objective) because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction. The proxy is suitable only for diagnostic purposes: detecting whether an action carried causal information (large proxy magnitude) vs. none (proxy near zero). For decision-making, use the canonical CIY (non-negative by construction) or a known-safe surrogate (ensemble disagreement, UCB bonuses). If the canonical CIY is intractable and no safe surrogate is available, the CIY term should be dropped from the policy objective entirely, defaulting to pure exploitation.

### Admissibility regimes

*[Scope Condition (ciy-admissibility)]*

Three regimes determine when CIY can be estimated and how strong the causal identification is:

**Regime A — Randomized interventions.** The agent varies its actions across episodes (RL agents exploring, scientists experimenting, organisms probing). CIY is directly estimable from the agent's execution data and non-negative by construction. This is the standard case for active agents within the adaptive loop ( #der-loop-interventional-access). Action variation provides the identification needed for clean interventional estimates.

**Regime B — Observational with causal assumptions.** The agent cannot freely vary actions (constrained by coordination, policy, or resource limits). CIY estimation requires additional structure: a known causal DAG, instrumental variables, or functional form assumptions. Results inherit whatever causal assumptions are made. The interventional interpretation of CIY is weaker — it holds under the assumed causal structure but not model-free.

**Regime C — Adversarial or passive observation.** The agent either did not intervene (passive monitoring) or the observation channel includes responses from potentially adversarial sources. In the passive case, CIY is zero by definition (no intervention, no interventional information). In the adversarial case, CIY from the query action itself remains non-negative, but the *content* of the response may be designed to increase model-reality mismatch. The adversary operates through the disturbance term $\rho$, not through the information measure.

The regime is a property of the **domain and the agent's action space**, not a parameter the agent chooses. Software development is typically Regime A (the agent runs tests, deploys to staging, observes results — high action variation). Organizational strategy is typically Regime B (multiple initiatives run concurrently, attribution requires assumptions). Intelligence analysis is typically Regime C (the analyst observes but does not intervene).

## Epistemic Status

Conditional on the causal assumptions within each regime. The proxy definition is standard information theory; the admissibility classification is a scope decision, not a derived result. The safety conditions for proxy use are normative — they follow from the sign-indefiniteness of the proxy, not from AAD-specific machinery.

Max attainable: conditional. The regime boundaries are domain properties that cannot be derived within the theory.

## Discussion

**Relationship to the canonical CIY.** The proxy is not an approximation of the canonical CIY — it is a different quantity that happens to correlate with CIY under favorable conditions (Regime A). The canonical CIY ( #def-causal-information-yield) is defined interventionally and is non-negative by construction. The proxy uses observational mutual information and can be negative. They agree when the agent's action variation satisfies the conditions for causal identification; they diverge otherwise.

**Regime as a domain property.** The admissibility regime is not something the agent selects — it is determined by the domain's action space and observation structure. An agent that cannot vary its actions is in Regime B or C regardless of its internal architecture. This has implications for which domains CIY-based exploration is applicable to: Regime A domains get the full benefit; Regime B domains get weaker guarantees; Regime C domains should use alternative exploration strategies entirely.
