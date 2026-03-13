---
slug: communication-gain
type: hypothesis
status: discussion-grade
depends:
  - update-gain
  - multi-agent-scope
---

# Hypothesis: Communication Gain

When an agent incorporates information from another agent (rather than from direct observation), the optimal update gain extends the uncertainty ratio with additional terms for source quality and alignment uncertainty.

## Formal Expression

*[Hypothesis (communication-gain)]*

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as #update-gain)
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence
- $U_{\text{align},ji}$: **alignment uncertainty** — $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives

When all additional terms are zero (perfect channel, calibrated and aligned source): $\eta_{ji}^\ast \to 1$ (full trust). When any term is large: $\eta_{ji}^\ast \to 0$ (ignore the signal).

**Connection to single-agent case.** When $j$ is the environment (direct observation): $U_{\text{src}} = U_{\text{align}} = 0$, recovering #update-gain's standard form $\eta^\ast = U_M / (U_M + U_o)$.

## Epistemic Status

*Hypothesis.* The additive denominator treats all uncertainty sources as independent, zero-mean noise — a structural heuristic, not a strict variance derivation. This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured. For $U_{\text{align},ji}$ (deception), additivity is conservative: it correctly drives $\eta_{ji}^\ast$ toward zero when alignment uncertainty is high, but misses the adversary's *actual* strategy — presenting as trustworthy to exploit high $\eta_{ji}^\ast$. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics.

All four uncertainty terms must be expressed in a **common predictive-dispersion scale** before summation — the same units as $U_{M_i}$ (variance of the predictive distribution over the observed quantity). When hard to estimate directly, a conservative approximation: set $U_{\text{src}} + U_{\text{align}}$ to the empirical variance of $j$'s past prediction residuals as observed by $i$, minus the known channel noise $U_{o,ji}$.

## Discussion

**The denominator terms have different natures.** $U_{o,ji}$ is a property of the *channel* — improvable by infrastructure. $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its model, or estimable by $i$ through calibration tracking. $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable.

**Trust calibration as a meta-model.** Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a **trust meta-model** — a model of models. This meta-model is itself subject to ACT's full apparatus: it has mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single disagreements), and can be structurally inadequate ( #structural-adaptation-necessity — the agent's trust model class may not capture the actual reliability structure of its sources).

**Risk-asymmetric trust.** The Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent (HILP — high impact, low probability) can cause catastrophic model corruption ( #adversarial-destabilization, effects spiral). Mild miscalibration toward a reliable source (LIHP) causes small ongoing inefficiency. For high-stakes interactions, use a conservative quantile of the trust posterior rather than the mean — require more evidence before granting high trust.

**Trust transitivity.** When agent $i$ has no direct experience with agent $k$, but trusted intermediary $j$ provides an assessment, the transitive trust question arises. A Bayesian mixture model discounts the recommendation by the intermediary's own reliability:

$$P_i(\theta_k \mid s_j) \propto \left[r_{ji} \cdot P(s_j \mid \theta_k) + (1 - r_{ji}) \cdot P_0(s_j)\right] \cdot P_i(\theta_k)$$

where $r_{ji}$ is $i$'s reliability estimate of $j$ and $\theta_k$ is $k$'s true alignment. When $r_{ji} \to 0$, the posterior collapses to the prior (no update); when $r_{ji} \to 1$, the full informative likelihood applies. This model gives a principled three-phase trust formation: prior → transitive update → direct experience (which eventually swamps the prior).

## Working Notes

- The communication gain enters the distributed tempo: $\mathcal{T}_i = \sum_k \nu_i^{(k)} \eta_i^{(k)\ast} + \sum_{j} \nu_{ji}^{\text{comm}} \eta_{ji}^\ast$. This is the formal basis for #team-persistence — teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo.
- Coordination overhead limits team size: adding members increases communication tempo with diminishing returns while coordination costs grow. The optimal team size occurs where marginal communication tempo equals marginal coordination cost. This connects to organizational theory (span of control, communication overhead).
- The adversary's strategy (making $U_{\text{align}}$ *appear* low) creates a meta-game on trust estimation. This is where game theory enters — the trust calibration itself is strategic. ACT provides the state variables (mismatch, gain, tempo, reserve); game theory provides the equilibrium analysis.
- Open: when multiple intermediaries provide corroborating recommendations about $k$, correlation matters. If all got their information from the same source, corroboration is illusory.
- Consider eventually **splitting $U_{\text{src},j}$ from $U_{\text{align},ji}$** into separate treatment tracks, not just separate denominator terms. Source calibration uncertainty is an *estimation* problem (estimable, improvable, converges with data). Alignment uncertainty is a *strategic* problem (the adversary optimizes *over* the defender's trust policy, not independently of it). The additive heuristic correctly drives $\eta_{ji}^\ast$ toward zero in both cases, but a richer model would separate the estimation problem (how good is this source?) from the trust-policy problem (how much should I trust, given that the source knows my trust policy?). The latter requires game-theoretic treatment — ACT provides the state variables; the equilibrium analysis is external.

*(Descended from TFT Appendix F, Section F.2.)*
