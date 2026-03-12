---
slug: edge-update-via-gain
type: hypothesis
status: discussion-grade
depends:
  - strategy-dag
  - update-gain
  - mismatch-signal
---

# Hypothesis: Edge Update via Gain

The uncertainty-ratio gain principle ( #update-gain) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise. This gives a principled, conservative update rule that avoids overreacting to single observations.

## Formal Expression

*[Hypothesis (edge-update-via-gain)]*

Edge credences update via:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot \left(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\right)$$

where:
- $\text{signal}(o_t, i, j) \in [0, 1]$: evidential content of observation $o_t$ about the causal link $i \to j$
- $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$: update gain

with:
- $U_{\text{edge}}$: uncertainty about this specific causal link. If $p_{ij} \sim \text{Beta}(\alpha_{ij}, \beta_{ij})$: $U_{\text{edge}} = \text{Var}[\text{Beta}] = \alpha\beta / ((\alpha + \beta)^2(\alpha + \beta + 1))$
- $U_{\text{obs}}$: observation noise on the channel confirming this link. $U_{\text{obs}} \propto 1/\sigma_j$ (inverse of observability of node $j$)

**Beta-Bernoulli equivalence.** For binary observations (success/failure of step $j$):
- Observe success: $\alpha_{ij} \to \alpha_{ij} + 1$
- Observe failure: $\beta_{ij} \to \beta_{ij} + 1$
- Point estimate: $p_{ij} = \alpha / (\alpha + \beta)$

This is the standard Bayesian update for a Bernoulli process — the gain principle reduces to conjugate updating in the binary case.

## Epistemic Status

*Hypothesis.* The extension of the gain principle from $M_t$ to $\Sigma_t$ edges is structurally motivated: the same uncertainty-ratio logic applies wherever an agent updates a belief in response to noisy evidence. But the extension has not been validated independently. Specific open questions:

- **The signal function** $\text{signal}(o_t, i, j)$ is not specified. How does an observation about node $j$ translate into evidence about edge $i \to j$ specifically? In the binary case (step succeeded or failed) it's clear. In continuous domains, extracting per-edge evidence from aggregate observations is a proper inference problem — potentially requiring the agent to solve an attribution problem (which edge caused the observed outcome?).
- **Identifiability**: when multiple edges contribute to an observation, attributing evidence to specific edges requires causal identification assumptions. In intervention-rich domains (software: run a specific test), this is tractable. In confounded domains (organizational: multiple initiatives contributed to the quarterly results), it's genuinely hard.
- **Interaction with $M_t$ updates**: edge updates use observations that have already been used for $M_t$ updates (the orient cascade processes $M_t$ first). Whether this creates statistical dependencies that bias the edge update is not analyzed.

## Discussion

**Connection to #observability-dominance.** When $\sigma_j \approx 0$: $U_{\text{obs}} \to \infty$, $\eta_{\text{edge}} \to 0$. The edge is frozen at its prior. Unobservable links cannot be updated — this is the mechanism that makes unobservable paths epistemically dead.

**Connection to #strategic-calibration.** The edge update rule is the correction function that the strategic calibration residual calls for: persistently positive $r_{ij}$ (predicted value increment exceeds observed) should reduce $p_{ij}$; persistently negative $r_{ij}$ should increase it. The gain principle provides the update magnitude — how much to adjust given the evidence strength.

**Conservative by design.** The uncertainty ratio ensures the agent doesn't overreact to single observations: a well-established edge ($\alpha + \beta$ large, $U_{\text{edge}}$ small) requires strong evidence to revise; a newly hypothesized edge ($\alpha + \beta$ small, $U_{\text{edge}}$ large) is easily moved by evidence. This mirrors the epistemic gain's behavior for $M_t$ — the agent trusts accumulated experience over individual observations.

## Working Notes

- The signal function is the critical missing piece. For each edge, the agent needs to evaluate: "given what I just observed, how much evidence does this provide about the causal link $i \to j$?" Designing this for binary outcomes is straightforward; for continuous outcomes with multiple contributing edges, it requires causal attribution. This may be where the edge-identifiability conditions (WORKBENCH open question) become concrete.
- The Beta-Bernoulli model assumes edge outcomes are i.i.d. Bernoulli draws. This is adequate for many settings but misses: (a) time-varying edge reliability ($p_{ij}$ drifting), (b) context-dependent reliability ($p_{ij}$ varies with environmental conditions), (c) correlated edge outcomes. Extending to time-varying priors (discounting old evidence) would connect to the mismatch dynamics framework.
