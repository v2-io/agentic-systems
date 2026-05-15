---
slug: internal-external-decomposition
type: derivation
status: robust-qualitative
depends:
  - result-persistence-condition
  - hyp-mismatch-dynamics
  - def-adaptive-tempo
  - scope-edge-update-causal-validity
stage: draft
---

# Derivation: Internal-External Decomposition of Agent Viability

The persistence condition ($\alpha R \gt \rho$) provides a binary survival threshold. However, diagnosing *why* an agent persists requires decomposing its margin of survival (viability) into internal agent capacity versus external environmental affordance.

## Log-Viability

We define log-viability $\mathcal{V}$ as the margin by which the agent's steady-state mismatch $R^\ast$ stays below the critical task boundary $\lVert\delta_{\text{critical}}\rVert$:

$$\mathcal{V} = \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

Persistence holds exactly when $\mathcal{V} \gt 0$. Because $R^\ast = \rho / \alpha$ (under linear Model D), we can additively decompose viability:

$$\mathcal{V} = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$$

## The Full Decomposition ($\mathcal{V}_E + \mathcal{V}_I$)

By expanding $\alpha$ (tempo $\times$ gain $\times$ fidelity), $\rho$ (volatility $\times$ policy benignity $\times$ model expressiveness), and $\nu$ (cap vs chosen usage), we split the margin into two additive components:

$\mathcal{V} = \mathcal{V}_E + \mathcal{V}_I$

### Environmental Affordance ($\mathcal{V}_E$)
Properties purely dictated by the environment:
$$ \mathcal{V}_E = \log \lVert\delta_{\text{critical}}^{\text{domain}}\rVert - \log \rho_{\text{external}} + \log \nu_{\text{external-cap}} $$

### Internal-Operational Health ($\mathcal{V}_I$)
Properties controlled by the agent's architecture, policy, and goals:
$$ \mathcal{V}_I = \log h(O_t) - \log f(\mathcal{M}) - \log g(\pi) + \log \frac{\nu_{\text{chosen}}}{\nu_{\text{external-cap}}} + \log \eta^\ast + \log c_{\min} $$

## Confounding and Identifiability

In a feedback system, high internal capacity often creates high environmental affordance (e.g., a good team refactors the codebase, lowering future $U_o$ and $\rho_{\text{external}}$). Separating these terms using purely observational data is formally impossible (identifiability floor). Separating them requires Level 2 interventional data: rotating agents across different environments (Regime A) to isolate $\Delta\mathcal{V}_E$ from $\Delta\mathcal{V}_I$.