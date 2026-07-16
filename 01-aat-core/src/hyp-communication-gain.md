---
slug: hyp-communication-gain
type: hypothesis
status: discussion-grade
depends:
  - emp-update-gain
  - scope-multi-agent
stage: draft
---

# Hypothesis: Communication Gain

The extension of the uncertainty-ratio gain principle (`#emp-update-gain`) to *inter-agent* communication channels. When an agent incorporates information from *another agent* (rather than from direct observation), the optimal update gain extends with additional terms in the denominator: **communication channel noise** (latency, ambiguity, compression loss, bandwidth limits), **source quality uncertainty** (the receiver's uncertainty about the sender's model calibration and domain competence), and **teleological-unity uncertainty** (the receiver's uncertainty about whether the sender's communications serve the receiver's interests or the sender's potentially conflicting objectives). When all additional terms are zero (perfect channel, calibrated and aligned source) the gain heads to 1 (full trust); when any term is large the gain heads to 0 (ignore the signal). When the "sender" is the environment (direct observation), the source-quality and alignment terms vanish and the standard single-agent gain formula is recovered.

The three additional denominator terms have *different natures*. Channel noise is a property of the *channel* — improvable by infrastructure. Source quality is a property of the *source* — improvable by the sender improving its model, or estimable by the receiver through calibration tracking. Alignment uncertainty is a property of the *relationship* — the game-theoretic variable. The three are independent levers; the framework's prescription is to track them separately.

The receiver's estimates of source quality and alignment constitute a **trust meta-model** — a model of models. This meta-model is itself subject to AAT's full apparatus: it has its own mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single disagreements), and can be structurally inadequate (the agent's trust model class may not capture the actual reliability structure of its sources, per `#result-structural-adaptation-necessity`). The framework also names **risk-asymmetric trust**: the Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent in a high-stakes interaction can cause catastrophic model corruption (the adversarial-destabilization effects spiral, `#der-adversarial-destabilization`); mild miscalibration toward a reliable source causes only small ongoing inefficiency. For high-stakes interactions, the framework prescribes using a *conservative quantile* of the trust posterior rather than the mean. **Trust transitivity** is handled via a Bayesian mixture: when no direct experience exists with a candidate source but a trusted intermediary provides an assessment, the recommendation is discounted by the intermediary's own reliability — giving a principled three-phase trust formation (prior → transitive update → direct experience, which eventually swamps the prior).

The framework is explicit about a limitation: the additive denominator treats all uncertainty sources as independent zero-mean noise — appropriate for channel noise and source miscalibration, but *misses the adversary's actual strategy* of presenting as trustworthy to exploit high gain. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics. The status is honestly *hypothesis-discussion-grade* — the additive heuristic correctly drives the gain toward zero when alignment uncertainty is high, but a full treatment of the adversarial case requires game-theoretic equilibrium analysis external to AAT (AAT provides the state variables; the equilibrium analysis is external).

## Formal Expression

*[Hypothesis (communication-gain)]*

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as #emp-update-gain)
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence
- $U_{\text{align},ji}$: **teleological-unity uncertainty** — $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives

When all additional terms are zero (perfect channel, calibrated and aligned source): $\eta_{ji}^\ast \to 1$ (full trust). When any term is large: $\eta_{ji}^\ast \to 0$ (ignore the signal).

**Connection to single-agent case.** When $j$ is the environment (direct observation): $U_{\text{src}} = U_{\text{align}} = 0$, recovering #emp-update-gain's standard form $\eta^\ast = U_M / (U_M + U_o)$.

## Epistemic Status

*Hypothesis.* The additive denominator treats all uncertainty sources as independent, zero-mean noise — a structural heuristic, not a strict variance derivation. This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured. For $U_{\text{align},ji}$ (deception), additivity is conservative: it correctly drives $\eta_{ji}^\ast$ toward zero when teleological-unity uncertainty is high, but misses the adversary's *actual* strategy — presenting as trustworthy to exploit high $\eta_{ji}^\ast$. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics.

All four uncertainty terms must be expressed in a **common predictive-dispersion scale** before summation — the same units as $U_{M_i}$ (variance of the predictive distribution over the observed quantity). When hard to estimate directly, a conservative approximation: set $U_{\text{src}} + U_{\text{align}}$ to the empirical variance of $j$'s past prediction residuals as observed by $i$, minus the known channel noise $U_{o,ji}$.

## Discussion

**The denominator terms have different natures.** $U_{o,ji}$ is a property of the *channel* — improvable by infrastructure. $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its model, or estimable by $i$ through calibration tracking. $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable.

**Trust calibration as a meta-model.** Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a **trust meta-model** — a model of models. This meta-model is itself subject to AAT's full apparatus: it has mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single disagreements), and can be structurally inadequate ( #result-structural-adaptation-necessity — the agent's trust model class may not capture the actual reliability structure of its sources).

**Risk-asymmetric trust.** The Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent (HILP — high impact, low probability) can cause catastrophic model corruption ( #der-adversarial-destabilization, effects spiral). Mild miscalibration toward a reliable source (LIHP) causes small ongoing inefficiency. For high-stakes interactions, use a conservative quantile of the trust posterior rather than the mean — require more evidence before granting high trust.

**Trust transitivity.** When agent $i$ has no direct experience with agent $k$, but trusted intermediary $j$ provides an assessment, the transitive trust question arises. A Bayesian mixture model discounts the recommendation by the intermediary's own reliability:

$$P_i(\theta_k \mid s_j) \propto \left[r_{ji} \cdot P(s_j \mid \theta_k) + (1 - r_{ji}) \cdot P_0(s_j)\right] \cdot P_i(\theta_k)$$

where $r_{ji}$ is $i$'s reliability estimate of $j$ and $\theta_k$ is $k$'s true alignment. When $r_{ji} \to 0$, the posterior collapses to the prior (no update); when $r_{ji} \to 1$, the full informative likelihood applies. This model gives a principled three-phase trust formation: prior → transitive update → direct experience (which eventually swamps the prior).

## Working Notes

- The communication gain enters the distributed tempo: $\mathcal{T}_i = \sum_k \nu_i^{(k)} \eta_i^{(k)\ast} + \sum_{j} \nu_{ji}^{\text{comm}} \eta_{ji}^\ast$. This is the formal basis for #der-team-persistence — teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo.
- Coordination overhead limits team size: adding members increases communication tempo with diminishing returns while coordination costs grow. The optimal team size occurs where marginal communication tempo equals marginal coordination cost. This connects to organizational theory (span of control, communication overhead).
- The adversary's strategy (making $U_{\text{align}}$ *appear* low) creates a meta-game on trust estimation. This is where game theory enters — the trust calibration itself is strategic. AAT provides the state variables (mismatch, gain, tempo, reserve); game theory provides the equilibrium analysis.
- Open, now partially derived: when multiple intermediaries provide corroborating recommendations about $k$, correlation matters. If all got their information from the same source, corroboration is illusory — this is the common-source regime of #deriv-tempo-additivity (2026-07-15): closed-form redundancy penalty, saturation at the shared source's bias floor, and the two-sided caveat that anti-correlated intermediary errors instead *triangulate* (super-additive). What remains open here is the trust-mixture-specific form.
- Consider eventually **splitting $U_{\text{src},j}$ from $U_{\text{align},ji}$** into separate treatment tracks, not just separate denominator terms. Source calibration uncertainty is an *estimation* problem (estimable, improvable, converges with data). Alignment uncertainty is a *strategic* problem (the adversary optimizes *over* the defender's trust policy, not independently of it). The additive heuristic correctly drives $\eta_{ji}^\ast$ toward zero in both cases, but a richer model would separate the estimation problem (how good is this source?) from the trust-policy problem (how much should I trust, given that the source knows my trust policy?). The latter requires game-theoretic treatment — AAT provides the state variables; the equilibrium analysis is external.

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings (the gain-denominator findings F167–F172 from AUDIT-WORKING-526815 are routed for adjudication — see the off-ramp note at the end). **Coverage:** two dirs carry a dedicated reflection (526815, 849201) plus a forward-looking note from the batched 471203. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The diagnostic payoff, plainly stated: the segment "formalizes trust as a computable scalar gain" and decomposes "why I shouldn't listen to you" into three causes — **Channel** (noise/latency), **Competence** (source calibration), and **Alignment** (whether the source serves your interests) — "incredibly useful for diagnostics" (Claude, AUDIT-WORKING-849201). Candidate Brief anchor: trust as a three-gate discount on the update gain.
- "The exact equation for how much an agent should change its mind when another agent tells it something" (Claude, AUDIT-WORKING-849201).

#### 2. Candidate Discussion

- **Estimation vs. strategy — the load-bearing asymmetry, stated for readers.** Source *competence* uncertainty is an estimation problem; source *alignment* uncertainty is a strategic, game-theoretic one — "an intelligent adversary does not generate random noise; they optimize to exploit your trust," so treating $U_{\text{align}}$ as a zero-mean Gaussian variance term is a *structural heuristic*, not a derived gain (Claude, AUDIT-WORKING-849201; Codex/Claude, AUDIT-WORKING-526815 — deception "changes the generation policy for the signal rather than merely widening an independent noise distribution"). The existing final Working Note already names this split; the auditor framing is candidate Discussion prose for *why* it matters.
- **The conservative-quantile patch as a rigorous fix, not a hack.** Using a conservative quantile of the trust posterior (rather than the mean) for high-stakes interactions is "a rigorous, decision-theoretic patch for this heuristic gap" — worth presenting as the principled response to the strategic-alignment problem rather than an ad-hoc safety margin (Claude, AUDIT-WORKING-849201).
- **Transitive trust as Bayesian mixture.** "Updating your trust in C based on a message from B, discounted by your trust in B" — flagged as "a beautiful application of Bayesian mixture modeling" and a candidate Discussion illustration of the trust-network structure (Claude, AUDIT-WORKING-849201).

#### 3. Follow-up items

- **Theory of mind / nested beliefs is missing from the communication vocabulary.** This segment and #def-shared-intent "handle inter-agent epistemic unity, but the recursive structure — 'I believe that you believe that I believe …' — is central to multi-agent reasoning (Aumann common knowledge, level-$k$ thinking) and isn't in the framework's vocabulary" (Claude, AUDIT-WORKING-471203, adversarial-creative-challenges "Missing 2"). The segment's own note that estimating $U_{\text{src}}$/$U_{\text{align}}$ requires a "meta-model (a model of another agent's model)" is the natural attachment point (Claude, AUDIT-WORKING-849201). Candidate scope-extension follow-up shared with #def-shared-intent.
- **Adversarial poisoning of the transitive-trust network (Sybil attacks).** How does the framework handle a Sybil attack on the transitive-trust mixture — many fake intermediaries corroborating a false claim about $k$? (Claude, AUDIT-WORKING-849201). The segment's existing correlation Working Note ("if all got their information from the same source, corroboration is illusory") is the seed; Sybil-resistance is the sharper open follow-up.

#### 4. Readers often ask / wonder

- Fresh readers converge on the question the segment is built to answer — "how much should I trust this message?" — and find the Channel/Competence/Alignment decomposition the satisfying response (Claude, AUDIT-WORKING-849201). A candidate readers-often-ask lead-in.

#### 5. Candidate figures

- **Three-gate message diagram.** A received message passing through three gates before reaching the receiver's update rule, with the strategic-alignment gate drawn as a *loop* (the sender optimizes the message against the receiver's trust rule) rather than as an independent noise gate like the channel and competence gates — visually separating the variance-like gates from the adversarial one (Codex/Claude, AUDIT-WORKING-526815).

#### Off-ramp (NOT gold — routed to certified-findings track)

- AUDIT-WORKING-526815 raised findings on this segment that are strengthen-first / scope-precision candidates, flagged here only so they are not lost: **F167** — the additive communication-gain denominator is only optimal under strong common-scale, independent, approximately zero-mean assumptions ($U_o$, $U_{\text{src}}$, $U_{\text{align}}$ need a precise map onto the same predictive-dispersion units before the ratio carries Bayesian-gain force); **F168** — treating teleological-unity uncertainty as additive variance under-models strategic deception (misalignment changes the message *policy* adversarially as a function of the receiver's trust rule); **F169** (soft) — estimating $U_{\text{src}} + U_{\text{align}}$ from residual variance minus channel noise is fragile (residuals conflate calibration, alignment, receiver model error, nonstationarity, common shocks; the subtraction can go negative without a floor); **F170** — the distributed-tempo note adds communication tempo contributions linearly, repeating the tempo-additivity concern (messages can be redundant/correlated/delayed/costly/strategically selected); **F171** (soft) — the transitive-trust mixture collapses to the prior only if $P_0(s_j)$ is explicitly uninformative about $\theta_k$ and normalized consistently, and the scalar reliability $r_{ji}$ hides domain/calibration/alignment dimensions; **F172** (watch) — risk-asymmetric trust should be tied to an explicit loss function/decision rule (a conservative posterior quantile is plausible for high-impact downside but is not implied by Bayesian reliability estimation alone). *These are formalization/scope tightenings, not no-gos; routed for adjudication on the strengthen-first track.*
