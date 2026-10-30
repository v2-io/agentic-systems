---
kr: C.2
item: C3 (allocation vs distortion coupling)
written: 2026-10-30
head: 620ac98c
---

# Adversarial instances — one deliberately out-of-family case per universally quantified claim

*Companion to `01-derivation.md`. The drill: for every "for all" landed there, construct an instance outside the motivating family and see whether the claim survives, scopes, or breaks. All numbers are exact enumeration from `sims/check.py` (`sims/check-output.txt`), nats.*

## Proposition A (allocation preserves calibration) — motivating family: a goal-indexed deterministic coarsening with a selection-aware Bayes update

**Out-of-family 1: the drop rule peeks at content (N5).** World $\Omega \in \{0, 1\}$ with $P(\Omega = 1) = 0.6$; two binary features with accuracies $0.9$ and $0.7$. Rule: always encode $x_1$; encode $x_2$ only when $x_2 = 1$ (confirming), else drop. This is "only allocation" in form. A naive update that treats a dropped $x_2$ as never observed has reliability $0.0148$; the same rule with the pattern modeled (the drop reveals $x_2 = 0$) has reliability $0$. **Scopes the claim:** calibration survives iff the mechanism is ignorable or modeled (Proposition A′). The explorer's "selection-aware" was a name for this condition, not the condition.

**Out-of-family 2: the drop rule depends only on retained content (N5, third row).** Encode $x_2$ iff $x_1 = 1$, naive update: reliability $0$, resolution $0.3677$ (between the $x_1$-only and full-information values). **Survives:** a content-dependent rule whose inputs the updater also sees is ignorable; the claim does not require the mechanism to be content-blind.

**Out-of-family 3: goal-dependent randomization in the encoder.** A stochastic encoder whose randomization is independent of $\Omega$ is a garbling of the information; the Bayes posterior given the garbled output is still a conditional expectation (Lemma 2.2). **Survives** without computation; noted because "deterministic coarsening" was the flagship.

**Out-of-family 16: the agent does not know what it encoded (Dorst 2023's two-world example; N13).** Equiprobable worlds $b, g$; the update becomes certain of $g$ at $g$ and stays at $0.5$ at $b$ because the agent cannot tell $b$ from "unresolved." No goal anywhere. Brier: prior $0.25$, updated $0.125 = 0.25 - 0.25 + 0.125$ — resolution $0.25$, **reliability $0.125$**, Reflection fails ($\mathbb E[\text{updated } P(g)] = 0.75 \ne 0.5$), yet the update is strictly better than not updating; the recalibrated forecast ($0$ at $b$) would score $0$ but the agent cannot issue it. **Scopes Prop A a third time:** "allocation preserves calibration" also needs the agent to know what it encoded (access / No Ambiguity). Without it, calibration failure is not evidence of goal-driven distortion, and goal-driven allocation that produces goal-dependent ambiguity (Dorst's cognitive search) does cost reliability. The invariant that survives is Value.

## Proposition B (distortion strictly costs under every strictly proper rule) — motivating family: a well-specified Bayesian with a goal-tilt

**Out-of-family 4: misspecified prior (N4).** True $P(\Omega = 1) = 0.8$, agent prior $0.3$, one feature with accuracy $0.6$, exponential tilt toward $\Omega = 1$ with gain $\lambda$. Objective expected log score: $1.0015$ at $\lambda = 0$, $0.6318$ at $\lambda = 1$, $0.4927$ at $\lambda = 2.5$, minimum near $\lambda \approx 2.23$; subjective (agent-model) score minimized at $\lambda = 0$. **Scopes the claim:** strictly worse under the agent's own model always; under the world's law only when well-specified. "Accuracy about the world, for every goal" is false as a universal; the honest norm is about the reliability term under the stated law.

**Out-of-family 5: a non-motivated distortion (N11).** Round the full-information posterior to the nearest $0.25$ (clipped to $[0.05, 0.95]$): reliability $0.0088 \gt 0$. **Survives, and sharpens:** the claim is not about goals at all; any departure from conditional-expectation form costs, and coarsening the *belief* is not coarsening the *information* (the latter is allocation and costs only resolution).

**Out-of-family 6: a goal under which the tilt happens to vanish.** If $u_G$ is constant on $\mathrm{supp}\,\pi$ the tilted belief equals $\pi$ (N1, last check) and the expected score is unchanged. **Scopes "for every goal":** for every goal under which the update actually departs from the conditional.

## Theorem 3.1 / Proposition 3.2 ($\kappa$ cannot separate) — motivating family: two goals, two features

**Out-of-family 7: allocation at maximal $\kappa$ (N8, N3).** The allocation agent of (N3) reports different beliefs under the two goals on every one of the four feature patterns, so $I(G; M^+ \mid e, M^-) = H(G) = \log 2$ and $\kappa_{\text{processing}} = 1$ throughout, with reliability $0$ under both goals and resolutions $0.3552$ / $0.0791$. **Survives in the strong form:** not only can $\kappa$ not separate the kinds, a perfectly calibrated agent sits at the maximum of canon's scale.

## Proposition 3.3 ($\kappa$ does not measure magnitude) — motivating family: deterministic injective coupling

**Out-of-family 8: noisy update (N9).** Reported log-odds $\pm\lambda$ plus Gaussian noise $s$. Mutual information depends on $\lambda / s$ only: $\kappa = 0.062$ at $(0.3, 1)$, $0.486$ at $(1, 1)$, $1.000$ at $(1, 0.1)$ and at $(10^{-3}, 10^{-4})$. **Scopes the claim:** $\kappa$ is the detectability of the goal against the update's own noise; it saturates for any noiseless coupling and otherwise measures signal-to-noise, not displacement. The deterministic case was the limit, not the exception.

## Proposition 4.1 (calibration is boundary-invariant; selection/processing is not) — motivating family: an ignorable encoder

**Out-of-family 9: a non-ignorable encoder, redrawn.** Take Out-of-family 1's peeking rule and draw the $f_M$ boundary at the encoder's output, so the drop is "selection." Reliability is $0.0148$ under either drawing. **Survives in both directions:** the redrawing makes a benign agent look coupled (motivating case) and cannot make a distorting agent look clean (this case); the reliability term is the invariant either way.

## Theorem 6.1 (Jensen-gap identity; range bound) — motivating family: discrete $\Omega$, bounded tilt

**Out-of-family 10: Gaussian mean shift (N12).** $\pi = N(\mu, \sigma^2)$, reported belief $N(\mu + \beta, \sigma^2)$. This *is* an exponential tilt with $u = x$ and $\lambda = \beta / \sigma^2$; the Jensen gap is $\tfrac{1}{2}\lambda^2 \sigma^2 = \beta^2 / (2\sigma^2)$, which equals $\mathrm{KL}(N(\mu, \sigma^2) \Vert N(\mu + \beta, \sigma^2))$ exactly: $0.1250$, $0.0312$, $0.5000$ for $\sigma = 1, 2, 0.5$ at $\beta = 0.5$. The range bound is vacuous (unbounded support). **Scopes the bound, confirms the identity:** on unbounded support use the cumulant form, where the ambiguity factor is $\mathrm{Var}_\pi(u_G) = \sigma^2$ — which is exactly the dependence canon's own Gaussian worked example (`deriv-observation-ambiguity-bias-bound.md` §6) found numerically for its Track 2 form.

**Out-of-family 11: mass placed outside the support.** A reported belief that puts positive probability on a world-state with $\pi$-probability zero (an impossible state asserted) is not a multiplicative reweighting of $\pi$ ($r_G$ would have to be infinite there); $\mathrm{KL}(M^+_G \Vert \pi) = \infty$. **Outside the class, by design:** this is the structural-failure limit canon names ("unbounded KL," `deriv-observation-ambiguity-bias-bound.md` Honest failure modes 2), and it is the hallucination mechanism `#disc-structural-imagination` calls level confusion, not drift. The tilt law is a drift law.

**Out-of-family 12: tilt that varies only off-support (N1, last check).** $\pi = (0.5, 0.5, 0)$, $u = (1, 1, 50)$, $\lambda = 3$: displacement $0$. **Survives:** the "ambiguity" that matters is the spread of the goal-relevant functional *on the support of the calibrated posterior*, not its spread over the whole state space.

## Proposition 7.1 (5a starvation as VOI) — motivating family: pursue-only versus pursue-plus-abandon

**Out-of-family 13: abandon present but never optimal (N10).** Add the abandon action with payoff $0$: $\mathrm{VOI}(f_{\text{feas}}) = 0$ again. **Scopes (b):** presence of the revise option is not enough; it must be optimal under infeasibility and not under feasibility. An agent whose objective-revision option is valued at nothing allocates exactly like one that has no such option — the grounding-condition connection in §7 of the derivation is load-bearing, not decorative.

## §5.1 (the ambiguity factor is zero under (NWI)) — motivating family: a two-state world with an uninformative goal

**Out-of-family 14: the goal is informative (N7β).** Goals assigned by a principal who knows more: $P(\text{flaw} \mid e, G = \text{correct}) = 0.8$, $0.2$ under $G = \text{ship}$. $\mathcal A = 0.278$; the goal-using Bayesian moves $0.30$ in total variation from the goal-blind belief and scores $0.5004$ versus the goal-blind agent's $0.6931$. **Confirms the dichotomy from the other side:** when $\mathcal A \gt 0$, the "bias" the bound measures is the correct update on an informative goal, and the goal-blind agent is the one that is wrong.

**Out-of-family 15: (NWI) without the action in the conditioning set.** Binary $\Omega$, $a \in \{0, 1\}$ chosen by the goal, $e = \Omega \oplus a$. Then $G \perp \Omega$ marginally but $G$ and $\Omega$ are perfectly dependent given $e$, so $I(G; \Omega \mid e) = H(\Omega) \gt 0$ — not because the goal is evidence about the world but because conditioning on a collider without the realized action manufactures dependence. **Scopes §5.1:** the identically-zero claim needs the realized action in the conditioning set, which is what "conditional on the realized event" has to mean (derivation §1.1). A reader who omits $a$ will compute a positive $\mathcal A$ that is a selection artifact.

## Summary table

| Claim | Instances | Outcome |
|---|---|---|
| Prop A | 1, 2, 3, 16 | scoped to ignorability (A′) and to access (the agent knows what it encoded); survives otherwise |
| Prop B | 4, 5, 6 | scoped to subjective / well-specified; sharpened to non-goal distortions |
| Thm 3.1 / Prop 3.2 | 7 | survives, strong form |
| Prop 3.3 | 8 | scoped: detectability (SNR), saturating in the noiseless limit |
| Prop 4.1 | 9 | survives both directions |
| Thm 6.1 | 10, 11, 12 | identity survives on unbounded support (cumulant form); range bound scoped to bounded support; class boundary at out-of-support mass |
| Prop 7.1 | 13 | scoped: revise option must be optimal under infeasibility |
| §5.1 | 14, 15 | survives; needs realized action in the conditioning set |

No claim broke outright; five were scoped by their instance (Prop A twice — ignorability from my own instance, access from the literature scan's), and the scopes are now in the statements.
