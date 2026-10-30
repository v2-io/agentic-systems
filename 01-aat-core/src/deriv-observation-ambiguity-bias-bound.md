---
slug: deriv-observation-ambiguity-bias-bound
type: derivation
status: conditional
depends:
  - scope-agent-identity
  - disc-additive-coordinate-forcing
  - der-directed-separation
  - form-information-bottleneck
  - disc-compression-operations
stage: draft
---

# Derivation: Goal-Dependence Displacement Bound — the Constant $C$

How far a goal-coupled update's belief can depend on the goal — the displacement of the goal-conditional post-update law from the goal-marginal one — is bounded by the goal information the update transfers into the belief, $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$, which by the definition of $\kappa_{\text{processing}}$ ( #der-directed-separation) equals $\kappa_{\text{processing}} \cdot H(G \mid e_\tau, M_{\tau^-})$. This appendix derives the constant under two named sub-scopes, records a no-go showing that the constant cannot be universal without the (PI) parameterization-invariance axiom of #scope-agent-identity, and documents two failed derivation routes so future agents do not repeat them. Two things it does not bound, said at the top because the segment once claimed one of them: it does not bound the belief's *distortion* — its departure from the calibrated belief given the agent's information, which is the quantity #der-directed-separation's norm is about and #scope-observation-ambiguity-modulation treats — since calibrated allocation also makes the belief depend on the goal and shows up in this bound at full strength; and it says nothing about observation ambiguity, since the information term is the goal's recoverability from the belief, which saturates for any noiseless coupling however small.

## Formal Expression

### §1 — Setup and the audit before deriving

Let $M_{\tau^-} \in \mathcal{M}$ be the pre-update epistemic substate, $e_\tau$ the event triggering the update (the external event including the realized action, #der-directed-separation Scope Condition), $G$ the goal substate, and $\Omega_\tau$ the latent world-state the event is evidence about. The update produces a post-update state $M_{\tau^+}$ whose law may depend, possibly stochastically, on the goal. The **goal-conditional post-update law** is $P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G}$; the **goal-marginal post-update law** $P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}$, the average over the operating distribution of goals, is the baseline against which goal-dependence is measured. At the causally-disciplined baseline ($\kappa_{\text{processing}} = 0$ — Class 1 by construction or an idealized Class 2 in effect, equally) the two laws coincide for every goal and the displacement below is zero.

$$\lVert \Delta M_{\text{bias}}(G) \rVert \;:=\; d_{\mathcal{M}}\!\big(P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G},\; P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}\big),$$

a random variable in $G$. The name *bias* is inherited and is used here only for this displacement: it is the belief's dependence on the goal, not its departure from the truth.

**Type audit.** For a bound "$\lVert \Delta M_{\text{bias}} \rVert \leq C \cdot \sqrt{I}$" to be well-typed:

1. **Metric on laws over $\mathcal{M}$.** Two candidates are used, each within its own track: *(Track 1)* the Wasserstein distance $W_2$ between the two post-update laws as probability measures on $\mathcal{M}$, with a ground metric on $\mathcal{M}$; *(Track 2)* the Fisher–Rao spherical-arc distance $d_{FR}$ between the two laws as points on the unit $L^2$-sphere of $\sqrt{p}$, available on the statistical-manifold sub-case (H1). **Under the (PI) parameterization-invariance axiom of #scope-agent-identity** (fourth primary instance of #disc-additive-coordinate-forcing), Euclidean-on-parameters is a coordinate artifact and Fisher–Rao is the canonical invariant choice (Čencov 1982 uniqueness).
2. **Information coordinate.** $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ is in nats. Converting information to a distance between laws is what the Pinsker / Otto–Villani / Fisher–Rao machinery does.
3. **What $\kappa$ contributes.** Nothing beyond the information term: $\kappa_{\text{processing}} = I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}) / H(G \mid e_\tau, M_{\tau^-})$ by definition, so $I = \kappa \cdot H(G \mid e_\tau, M_{\tau^-})$ identically. The factor $\kappa$ enters the bound by that identity and not as a separate hypothesis.

### §2 — Track 1: Transport-inequality derivation under a log-Sobolev inequality

*[Derived (w2-transport-track, conditional on H2)]*

**Named sub-scope.** **(H2) Log-Sobolev inequality on the goal-marginal post-update law.** $P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}$, as a measure on $\mathcal{M}$ with the chosen ground metric, satisfies a log-Sobolev inequality with constant $\rho_{\text{LSI}} \gt 0$. Sufficient: strong log-concavity with constant $K$ (Bakry–Émery 1985), giving $\rho_{\text{LSI}} \geq K$; for a Gaussian law on a Euclidean chart, $\rho_{\text{LSI}} = 1 / \sigma^2$.

**Step 1 — KL from mutual information.** By the chain rule of relative entropy (Cover & Thomas 2006 Theorem 2.5.3), on the post-update law:

$$\mathbb{E}_G\big[\mathrm{KL}\big(P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G} \,\Vert\, P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}\big)\big] \;=\; I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}).$$

*Exact identity.* (NeurIPS 2026 Paper 3's Lemma 5.1 is this step.)

**Step 2 — Otto–Villani under LSI.** From (H2) and Otto & Villani 2000 *J. Funct. Anal.* 173(2):361–400 Theorem 1, for the reference measure $\mu = P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}$ and any $\nu \ll \mu$, $W_2^2(\nu, \mu) \leq (2 / \rho_{\text{LSI}})\, \mathrm{KL}(\nu \Vert \mu)$. Taking $\nu$ the goal-conditional law, averaging over $G$ and substituting Step 1:

**Result (Track 1).** *[Derived, conditional on (H2)]*

$$\boxed{\;\mathbb{E}_G\big[W_2^2\big(P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G},\, P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}\big)\big] \;\leq\; \frac{2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot H(G \mid e_\tau, M_{\tau^-})\;}$$

The constant is $C_{W_2}^2 = 2 / \rho_{\text{LSI}}$: the concentration of the goal-marginal post-update law is what converts transferred information into displacement, and nothing else does. No pushforward step from world-state to belief appears, because both laws compared are laws of the belief itself; the Lipschitz-posterior hypothesis a previous version of this derivation carried is not needed and is not stated.

### §3 — Track 2: Fisher–Rao derivation under (PI) + Čencov in the small-information regime

*[Derived (fisher-rao-track, conditional on H1 + H4)]*

**Named sub-scope.**

- **(H1) Statistical-manifold sub-case.** The two post-update laws have densities with respect to a common reference on $\mathcal{M}$, so that they are points of the unit $L^2$-sphere of $\sqrt{p}$ and the Fisher–Rao spherical-arc distance $d_{FR}$ between them is defined. Under the (PI) axiom, Čencov's uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS 1982; Ay, Jost, Lê & Schwachhöfer 2017 *Information Geometry*, Theorem 5.1) forces the Fisher metric as the canonical Riemannian metric up to global scale.
- **(H4) Small-information regime.** $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}) \ll 1$ nat, so the second-order expansion of KL at coincident laws is sharp.

**Step 1 — KL-to-Fisher-squared-distance identity.** For nearby densities $p, q$, $\mathrm{KL}(p \Vert q) = \tfrac{1}{2} d_{FR}^2(p, q) + O(d_{FR}^3)$ (Cover & Thomas 2006 §12.5; Amari & Nagaoka 2000 §3.7 Theorem 3.1).

**Step 2 — Compose with Step 1 of §2.** Under (H4), $d_{FR}^2 \leq 2\, \mathrm{KL}\,(1 + o(1))$ for each goal; averaging over $G$ and substituting the chain-rule identity, $\mathbb{E}_G[d_{FR}^2] \leq 2\, I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})\,(1 + o(1))$; Jensen gives the first-moment form.

**Result (Track 2).** *[Derived, conditional on (H1)+(H4)]*

$$\boxed{\;\mathbb{E}_G\, d_{FR}\big(P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}, G},\, P_{M_{\tau^+} \mid e_\tau, M_{\tau^-}}\big) \;\leq\; \sqrt{2} \cdot \sqrt{\kappa_{\text{processing}} \cdot H(G \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))\;}$$

The constant $C_{FR} = \sqrt{2}$ (nats) is universal and dimension-free; the price is the small-information regime.

**Scaling difference between tracks.** Track 1 bounds $W_2^2$ linearly in $I$; Track 2 bounds $d_{FR}^2$ linearly in $I$, equivalently $d_{FR} \propto \sqrt{I}$. They are bounds in different metrics under different hypotheses, tight in different regimes (Track 1 where the LSI constant is the binding fact, Track 2 where the small-$I$ expansion is sharp).

**What the information term does and does not do.** Because $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ measures the goal's *recoverability* from the belief, a noiseless update whose belief is an injective function of a discrete goal transfers all of $H(G \mid e_\tau, M_{\tau^-})$ — $\kappa_{\text{processing}} = 1$ — however small the displacement is (the C3 spike's Proposition 3.3; `spikes/spike-allocation-vs-distortion-coupling-2026-10-30/sims/check.py`, N2). The bound is then $C \sqrt{H(G \mid e_\tau, M_{\tau^-})}$, true and loose: it is a ceiling on displacement set by how much goal information is there to transfer, and a tight description of displacement only when the update is noisy relative to the goal-shift. It says nothing about how far the belief sits from the *calibrated* belief given the agent's information: calibrated allocation makes the belief depend on the goal and is bounded here at the same rate as distortion ( #scope-observation-ambiguity-modulation for the quantity that separates them).

### §4 — No-go: no universal $C$ under a Euclidean-parameter norm

*[Proved (no-universal-C-euclidean, counterexample-grade)]*

**Claim.** No universal constant $C$ — independent of $\mathcal{M}$'s geometry, parameterization and coupled-update structure — exists such that $\lVert \Delta M_{\text{bias}} \rVert_{\text{Euclidean}} \leq C \sqrt{I}$ under the Euclidean norm on an arbitrary parameter chart.

**Counterexample.** Let $\mathcal{M} = \{N(0, \sigma^2) : \sigma \gt 0\}$ parameterized by $\sigma$, with the two post-update laws two nearby points of it. The Fisher information in $\sigma$ is $\mathbf{I}(\sigma) = 2 / \sigma^2$, so the Fisher–Rao line element is $ds^2 = 2\, d\sigma^2 / \sigma^2$ and a Fisher–Rao displacement $d_{FR}$ corresponds to a Euclidean-$\sigma$ displacement $\Delta\sigma \approx \sigma\, d_{FR} / \sqrt{2}$. For fixed $I = 1$ nat, Track 2 bounds $d_{FR} \leq \sqrt{2}$, and $\Delta\sigma \approx \sigma$ grows without bound as $\sigma \to \infty$. No universal $C$ in Euclidean-parameter norm exists; equivalently, any chart rescaling $\phi \mapsto a\phi$ scales chart-Euclidean distances by $a$ while leaving KL, mutual information and $d_{FR}$ invariant.

**Implication.** The no-go strengthens the (PI) commitment rather than weakening the bound: **under (PI), Fisher–Rao is the canonical metric and $C = \sqrt{2}$ is universal; without (PI), $C$ does not exist as a universal constant.** The (PI) axiom is *load-bearing* for this derivation.

**Position relative to #disc-identifiability-floor.** The no-go has the shape of a floor-pattern no-go (external obstruction: Euclidean-parameter norms carry unbounded Fisher condition numbers; escape: (PI) + Fisher–Rao) but does not meet the five-element test for a floor instance: a *single* escape, and a strengthened consequence that re-uses existing (PI)+Čencov machinery rather than elevating new machinery. It is a downstream theorem of the (PI) commitment, recorded here as the reason (PI) is load-bearing, not as a floor instance (the distinction is drawn in #disc-additive-coordinate-forcing §"Downstream consequences of the (PI) commitment").

### §5 — Failed derivation routes (honest record)

Two routes were attempted and fail structurally; recorded so they are not re-attempted without new evidence.

**(F1) Cramér–Rao inversion — wrong direction.** Treat $G$ as a parameter estimated from the belief and invert the Cramér–Rao lower bound $\mathrm{Var}(\hat G) \geq \mathbf{I}_G^{-1}$ into an upper bound on displacement. Cramér–Rao bounds estimator error *below*; inverting it needs a fixed-estimator-class assumption unavailable for a Class 3 (Coupled) update. The transport route of §2 is the correct machinery.

**(F2) Rate-distortion inversion — wrong problem structure.** Apply the rate-distortion inequality for a Gaussian source and invert to bound displacement by "bits in." Rate-distortion describes the minimum rate to represent a source within distortion $D$; it does not describe the maximum displacement induced by injecting side-information into an update. Transport inequalities are the correct machinery.

The shared pattern: **source-coding lower bounds (Cramér–Rao, rate-distortion) cannot be inverted into upper bounds on side-information-induced displacement**; upper bounds need transport inequalities (Pinsker, Otto–Villani, Bakry–Émery) or the Fisher–Rao expansion.

### §6 — Two-goal Gaussian example, exact to first order

*[Illustrative, exact under stated assumptions]*

Let the goal be $G \in \{-, +\}$ uniform and the goal-conditional post-update laws be $N(\pm\beta, \sigma^2)$ on a one-dimensional chart of $\mathcal{M}$; the goal-marginal law is the symmetric mixture. The transferred information is $I(G; M_{\tau^+} \mid e, M^-) = \mathrm{JSD}(N(\beta, \sigma^2), N(-\beta, \sigma^2))$, and for $\beta \ll \sigma$, $\mathrm{JSD} \approx \tfrac{1}{4}\, \mathrm{KL}(N(\beta) \Vert N(-\beta)) = \tfrac{1}{4} \cdot \tfrac{2\beta^2}{\sigma^2} = \tfrac{\beta^2}{2\sigma^2}$; $H(G) = \log 2$, so $\kappa_{\text{processing}} \approx \beta^2 / (2 \sigma^2 \log 2)$. Track 2 then bounds $\mathbb{E}\, d_{FR} \leq \sqrt{2 I} = \beta / \sigma$. The actual Fisher–Rao distance from either conditional law to the mixture is, to first order, half the location-family distance between the two conditionals, $\tfrac{1}{2} \cdot 2\beta / \sigma = \beta / \sigma$: the bound is tight at first order, which is the sharpness the symmetric two-point witness is for. In the same example the mixture is close to $N(0, \sigma^2 + \beta^2)$ and satisfies LSI with $\rho_{\text{LSI}} \approx 1 / \sigma^2$ in the chart metric, so Track 1 gives $\mathbb{E}\, W_2^2 \leq 2 \sigma^2 \cdot \beta^2 / (2 \sigma^2) = \beta^2$, against the actual $W_2^2 = \beta^2$ between $N(\pm\beta, \sigma^2)$ and $N(0, \sigma^2)$: also tight. (The transferred-information identity $I = \mathrm{JSD}$ for a uniform binary goal is Paper 3's Corollary 4.4; the example here is checkable by hand.)

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Chain-rule identity $\mathbb{E}_G[\mathrm{KL}(P_{M^+ \mid G} \Vert P_{M^+})] = I(G; M^+ \mid \cdot)$ | Cover & Thomas 2006 Theorem 2.5.3 | Exact |
| $I(G; M^+ \mid e, M^-) = \kappa_{\text{processing}} \cdot H(G \mid e, M^-)$ | Definition of $\kappa_{\text{processing}}$ ( #der-directed-separation) | Exact (identity) |
| Pinsker's inequality | Standard (Csiszár–Körner) | Exact |
| Otto–Villani $W_2^2 \leq (2 / \rho_{\text{LSI}}) \mathrm{KL}$ under LSI | Otto & Villani 2000 Theorem 1; Bakry–Émery 1985 | Exact |
| KL-to-Fisher expansion $\mathrm{KL} = \tfrac{1}{2} d_{FR}^2 + O(d_{FR}^3)$ | Cover & Thomas 2006 §12.5; Amari & Nagaoka 2000 §3.7 Theorem 3.1 | Exact (standard information geometry) |
| **Track 1 bound** $\mathbb{E}[W_2^2] \leq (2 / \rho_{\text{LSI}}) \kappa H(G \mid e, M^-)$ | §2 | **Derived (conditional on H2)** |
| **Track 2 bound** $\mathbb{E}\, d_{FR} \leq \sqrt{2} \sqrt{\kappa H(G \mid e, M^-)}\,(1 + o(1))$ | §3 | **Derived (conditional on H1 + H4)** |
| $C_{FR} = \sqrt{2}$ universal and dimension-free | §3 | Exact under (H1)+(H4) |
| No universal $C$ in Euclidean-parameter norm | §4 counterexample | Proved (counterexample-grade) |
| (F1), (F2) fail | §5 | Recorded failures |
| Two-goal Gaussian example, tight to first order | §6 | Exact under its assumptions |
| The bound does not bound distortion from the calibrated belief, and saturates for noiseless couplings | §3, last paragraph; C3 spike Proposition 3.3 | Exact |

The hypotheses (LSI on the goal-marginal post-update law; the statistical-manifold sub-case; small information; (PI)) are standard regularity or AAT-internal axioms already adopted. The no-go §4 justifies (PI) as load-bearing. The failed attempts §5 record structural reasons two alternatives cannot work.

## Epistemic Status

*Conditional — exact under (H2) (Track 1) or (H1)+(H4) (Track 2).* Both tracks are derived theorems under named hypotheses, and both bound the same object: the displacement of the goal-conditional post-update law from the goal-marginal one, in transferred goal information $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}) = \kappa_{\text{processing}} \cdot H(G \mid e_\tau, M_{\tau^-})$. Track 1 is linear in the information with constant $2 / \rho_{\text{LSI}}$; Track 2 is $\sqrt{I}$ with the universal $\sqrt{2}$, in the small-information regime. The no-go §4 is *proved* by the heteroscedastic-normal counterexample. The failed attempts §5 are *recorded* at structural-reason level.

What the bound is a bound on is part of its epistemic status. It bounds *goal-dependence* of the belief. It does not bound *distortion* — the belief's departure from the calibrated belief given the agent's information — and it cannot be read as the $\varepsilon(\kappa)$ bound for the degradation norm of #der-directed-separation in the sense of "how far off the truth a $\kappa \gt 0$ agent's belief is": calibrated allocation produces goal-dependence at full strength with no distortion, and a noiseless injective coupling of any magnitude sits at $\kappa = 1$. What the bound does deliver for the degradation norm is the controlled continuity of the *belief's goal-dependence* off $\kappa = 0$, which is what a downstream functional of $M_t$ — the value object's $Q_O$, say ( #def-value-object) — inherits as goal-dependence through its argument.

A previous version of this derivation bounded the same displacement by $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$, the goal's evidential value about the world, through a chain rule on the *world-state* conditional laws, a Lipschitz pushforward from world-state to belief, and a factor $\kappa$ introduced by assertion. The chain rule on the world-state laws relates the *true* conditional laws, which for a distorting agent under goal-independence do not depend on the goal while the agent's belief does, so the inequality was about a different object than the one it was applied to; and the information term is identically zero in the regime where goal-dependence is a defect ( #scope-observation-ambiguity-modulation, Epistemic Status). The present form is Paper 3's: the chain rule is on the post-update law, which *is* the agent's belief, and every step then relates the quantities it names.

Max attainable: *exact* for the composition of the textbook inequalities and for the no-go; *conditional* overall. Open: the large-information regime for Track 2 (compact-manifold assumption or staged composition), and whether a bound on *distortion* indexed by any processor property exists — the C3 spike shows it cannot be indexed by $\kappa$, and #scope-observation-ambiguity-modulation's fixed-gain hypothesis is the candidate carrier.

## Honest failure modes

The appendix does **not** cover:

1. **Non-statistical-manifold sub-cases of $\mathcal{M}$.** Mixed continuous/discrete components, graphical-model structure, non-parametric models without a common reference measure: (H1) weakens and Čencov's uniqueness does not straightforwardly apply. Track 1 may still apply under a ground metric on $\mathcal{M}$ for which (H2) holds.
2. **Unbounded KL / structural-failure limit.** If some goal-conditional post-update law has support disjoint from the goal-marginal law's, the KL and hence $I$ diverge and the bound is vacuous — a structural failure of the coupled update, not of the bound.
3. **Heavy-tailed goal-marginal post-update laws.** LSI fails for heavy-tailed measures; Track 1 degrades to Pinsker's total-variation form, the $O(\sqrt{\varepsilon})$ baseline without the LSI tightening.
4. **Large-information regime.** Track 2's $\sqrt{I}$ scaling uses the second-order expansion; a global Fisher–Rao statement needs a compact-manifold assumption or staged application (Paper 3 states a global $C = 2$ on the spherical arc by a chord–arc argument; unread here and not adopted).
5. **Distortion.** The quantity the degradation norm is about is not bounded here at all (Epistemic Status).

## Discussion

**Position in the #disc-additive-coordinate-forcing meta-pattern.** Track 2's $C_{FR} = \sqrt{2}$ is a downstream theorem of the fourth primary instance (Čencov invariance at the metric layer, under (PI)): once (PI) forces Fisher–Rao as the canonical metric, the KL-to-Fisher identity supplies the universal constant in the small-information regime, and the no-go §4 shows the commitment is load-bearing rather than convenient.

**Connection to #deriv-variational-sector-condition.** Both use Pinsker's inequality as a first step in propagating a KL bound and then diverge: this segment's cascade is KL-to-distance-between-laws machinery; `#deriv-variational-sector-condition`'s is KL-to-scalar-constant machinery. Adjacent family members, not candidates for a shared template.

**What this bound gives the degradation norm, stated carefully.** The scoping rule of #der-directed-separation asks that a result stated at $\kappa_{\text{processing}} = 0$ carry, where it can be shown, how it degrades off the zero. This appendix gives one such degradation, for one kind of consequence: any downstream functional of the belief inherits the belief's goal-dependence, and that goal-dependence is bounded by $C \sqrt{\kappa\, H(G \mid e_\tau, M_{\tau^-})}$ — continuous in $\kappa$ and zero at zero. The value object's $Q_O$ ( #def-value-object) is the first realized client: at $\kappa \gt 0$ its value depends on the goal through $M_t$, and this bound says by at most how much. It is not a bound on how far $Q_O$ is from the value a calibrated belief would give, and #def-value-object does not read it as one.

**Connection to logogenic agents.** This appendix's bounds are the quantitative apparatus behind #result-section-ii-survival's Class 3 (Coupled) scope-survival analysis, for the goal-dependence of the diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) read off a goal-coupled belief: the Lipschitz composition there bounds how much a diagnostic varies with the goal, not how far it is from the diagnostic a calibrated belief would give. #scope-observation-ambiguity-modulation carries the distortion side.

## Findings

### Universal Constant for the Goal-Dependence Displacement Bound under Parameterization-Invariance

**Brief:** When a goal-coupled agent (like an LLM) processes evidence, the belief it ends up with can depend on what it was trying to do, not only on what it saw. How much it can depend on the goal is bounded by how much information about the goal the update lets into the belief — a quantity that is, by definition, the agent's coupling $\kappa$ times how much there was to let in. This result computes the constant in that bound under two sets of conditions, and shows that one of them — committing to a particular geometry on the model space, the (PI) axiom — is necessary in a strong sense: without it no universal constant exists. What the bound does not do is say how far the belief is from the *truth*: an agent that merely attends to different things for different goals has goal-dependent beliefs that are all correct, and shows up here at full strength.

**Impact:** Supplies the explicit constant for the belief's goal-dependence off $\kappa_{\text{processing}} = 0$, which is what downstream functionals of the belief — the value object, the Part II diagnostics on a Class 3 substrate — inherit; keeps the no-go that makes (PI) load-bearing; and records two failed derivation routes. It no longer claims to bound bias relative to the goal-blind update, nor to refine a coarser bound through observation ambiguity: the previous version's information term measured the goal's evidential value about the world and vanished in the regime that mattered, and its $\kappa$ factor was asserted. The distortion question moves to #scope-observation-ambiguity-modulation, where it is carried by a model-free range bound and a fixed-gain hypothesis with a test.

**Novelty Claim:** *Claim differentiation* on the composition of the post-update chain rule with Otto–Villani and with the Fisher–Rao expansion for the goal-coupled setting, plus *claim novelty* on the no-go counterexample showing that universal $C$ in Euclidean-parameter norms cannot exist; both are shared with NeurIPS 2026 Paper 3, which carries them at theorem grade. The upstream tracks compose textbook machinery (Cover–Thomas; Otto–Villani 2000; Amari–Nagaoka 2000); the contribution is the composition and the no-go.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| KL-to-$W_2$ transport under log-Sobolev | Otto & Villani 2000 *J. Funct. Anal.* 173:361–400; Bakry & Émery 1985 curvature-dimension condition | *formal antecedent* — adopted directly in Track 1 |
| Čencov uniqueness of the Fisher metric | Čencov 1982, *Statistical Decision Rules and Optimal Inference*; Ay, Jost, Lê & Schwachhöfer 2017 *Information Geometry* Theorem 5.1 | *formal antecedent* — adopted via (PI) in #scope-agent-identity; the no-go §4 is the AAT-internal demonstration that the adoption is load-bearing |
| KL-to-Fisher second-order expansion | Amari & Nagaoka 2000 §3.7 Theorem 3.1; Cover & Thomas 2006 §12.5 | *formal antecedent* — supplies Track 2's small-information sharpness |
| Information-processing-constraint bounds on decisions | Ortega & Braun 2012 *Proc. R. Soc. A*; Genewein et al. 2015 *Front. Robot. AI* 2:27 | *adjacent literature* — a different quantity (decision quality under information constraint) in shared vocabulary |
| Variational bounds on posterior beliefs in active inference | Friston et al. 2017, *Neural Computation* 29:1–49 | *adjacent literature* — overlapping transport machinery in a different framework; Track 1 does not need the variational-free-energy commitment |

**Search Log:**

- 2026-04 (*nominally comprehensive*): a Pillar-3 pass located bounded-rationality and information-cost literatures as the closest decision-theoretic precursors and no equivalent of the universal-$C$ derivation under (PI). The verdict attached to the product-form law downstream is retired with that law; this segment's narrower contribution (the constant and the no-go) keeps a Medium confidence with a follow-on targeted search recommended on posterior-displacement bounds for goal-coupled architectures.

## Working Notes

- **Regression guard.** Do not restore the information term $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$, the Lipschitz-posterior pushforward (H3), or a Step 4 that multiplies the information term by $\kappa_{\text{processing}}$: the term is $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$, the chain rule is on the post-update law, and $\kappa$ enters by its definition. Do not describe this bound as bounding bias relative to the goal-blind update or as the degradation norm's bound on tracking reality; it bounds goal-dependence.
- **$\rho_{\text{LSI}}$ for AAT-native cases.** The LSI constant of the goal-marginal post-update law is explicit for Gaussian laws on a Euclidean chart and otherwise not computed; exponential-family / conjugate-prior cases ( #der-gain-sector-bridge) are the natural next computations.
- **Large-information regime.** Track 2's $\sqrt{I}$ scaling is the small-$I$ expansion; the global statement needs a compact-manifold assumption or staged composition. Paper 3's global constant on the spherical arc is unread here.
- **Class 2 (Partial) bias-bound analog.** The bound is stated for all $\kappa \in [0, 1]$ through the identity $I = \kappa H$; whether a *tighter* bound exists for Class 2 architectures with a known per-stage decomposition ( #disc-partial-coupling-pathways) is open.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged / fully coupled, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Cross-reference to NeurIPS Paper 3.** NeurIPS 2026 Paper 3 ("How Much Can LLMs Hallucinate? An Upper Bound on Goal-Coupling Displacement", `~/src/neurips/03-llm-hallucinate-bound/`) carries the present form at theorem grade: the bias quantity relative to the goal-marginal post-update law (`03-setup.md` §"The bias quantity"); the chain rule on the post-update law (§5 Lemma 5.1); the umbrella theorem (§4 Theorem 4.1) with Track 1 under its (H2') and Track 2 giving $C = 2$ globally on the spherical arc and $\sqrt{2}$ locally under (R)+(K)+(H4'); the chart-rescaling no-go (§4 Theorem 4.2); Čencov uniqueness-and-sharpness (§4 Theorem 4.3); and the JSD estimator for a uniform binary goal (Corollary 4.4). Its *architectural corollary* factors transferred information through a ratio $\kappa := I(G; M_{\tau^+} \mid \cdot) / I(G; \Omega_\tau \mid \cdot)$ under a bounded-attenuation commitment; that denominator is the quantity retired from this segment, zero under goal-independence, so the corollary covers only agents whose goals are evidence about the world, and its Class 1 criterion ($G \perp M_{\tau^+} \mid \Omega_\tau, e_\tau, M_{\tau^-}$) excludes the goal-as-evidence Bayesian it is meant to include ( #scope-observation-ambiguity-modulation, Working Notes). Those are notes for the paper; canon does not use the corollary. In-review external draft, not canon.
