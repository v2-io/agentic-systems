---
slug: deriv-regime-marginal-indistinguishability
type: derivation
status: conditional
depends:
  - deriv-strategic-composition
  - deriv-critical-mass-composition
  - disc-identifiability-floor
  - result-sector-persistence-template
  - disc-dynamic-regime-axis
stage: draft
---

# Derivation: Regime-Marginal Indistinguishability — Cross-Regime Witness for `#disc-identifiability-floor` Instance 3 (Broadened Scope)

This segment supplies the parameter-by-parameter witness construction for `#disc-identifiability-floor` Instance 3's broadened-scope claim (2026-05-21): from sub-agent marginal data alone, the coupling-topology bit distinguishing among R0 / R1 / R2 dynamic regimes (per `#disc-dynamic-regime-axis`) is unidentifiable. The witnesses are exact for symmetric-matched-Tier-1-scalar sub-agents under standard coupling models (Model D for disturbance; the same models `#deriv-critical-mass-composition` uses, where the Instance-3 coupling-sign-bit witness is established). The mechanism is rank-collapse / Sylvester-at-one-remove on the marginal-Fisher operator for the topology coordinate, parallel to the Instance-3 coupling-sign-bit mechanism but acting on a higher-dimensional topology coordinate.

The segment exists because the witness math has to live in canon per the math-lives-in-segments discipline; the spike that derived it (`spikes/spike-identifiability-floor-instance-6-2026-05-21.md`) records the reasoning trail but cannot carry the formal derivation as canon-grade content. The relationship to `#disc-identifiability-floor` Instance 3 is supporting-derivation — Instance 3 carries the no-go statement, the escape menu, and the strengthened consequence; this segment carries the explicit construction backing the broadened no-go.

## Formal Expression

### Setup

Consider $N = 2$ scalar sub-agents indexed $i \in \{1, 2\}$, each with state $q_i \in \mathbb R$, base correction rate $\alpha \gt 0$, observation noise $w_i \sim \mathcal N(0, \sigma^2)$, base disturbance bound $\rho$, tempo $\mathcal T$. The composite state is $X^c = (q_1, q_2) \in \mathbb R^2$. An external observer $B$ accesses *only* per-sub-agent marginal data: for each $i$, the marginal stationary distribution $\mu_\infty^{(i)}$, the local mismatch process, and the per-sub-agent update rule $f_M^{(i)}$ as a structural object (white-box on each sub-agent, observed in isolation). The observer does *not* see: the composite-level coupling topology (sign + structure of cross-agent influence), the joint trajectory $\{X_t^c\}$ (only the projection onto per-sub-agent marginals), the game-structure object $\{O^{(j)}\}_{j \neq i}$ from sub-agent $i$'s frame, or composite-level convergence-rate-class diagnostics.

The inferential question: from per-sub-agent marginal data alone, can $B$ identify the composite's dynamic regime $\mathcal R(X^c) \in \{\text{R0}, \text{R1}, \text{R2}\}$ per `#disc-dynamic-regime-axis` §B?

### Witness 1: R0 vs R1 indistinguishability

*[Derived (cross-regime-witness, from Cournot equilibrium structure + shared-target marginal-matching)]*

**Composite A — R0 shared-objective contraction.** Sub-agent objective $O_A^{(i)} = -\tfrac{1}{2}(q_1 + q_2 - T)^2$ for shared target $T$. Per-agent gradient-flow best-response:

$$\dot q_i \;=\; -\alpha\,(q_i + q_j - T) + w_i.$$

The composite is R0 per `#disc-dynamic-regime-axis` §B.0: unique attracting fixed point at $(T/2, T/2)$, joint Lyapunov $V = \tfrac{1}{2}\lVert q - (T/2, T/2) \rVert^2$, exponential convergence at rate $\alpha$. The stationary marginal distribution of each sub-agent's state, computed from the linearized Ornstein-Uhlenbeck dynamics, is

$$\mu_{\infty, A}^{(i)} \;=\; \mathcal N\!\left(\,T/2,\; \sigma^2/(2\alpha)\,\right).$$

**Composite B — R1 strategic potential-game equilibrium (Cournot).** Sub-agent objective $O_B^{(i)} = q_i\,(a_0 - b(q_1 + q_2) - c)$ — quadratic-profit Cournot in canonical form. The game is a potential game (Monderer-Shapley 1996) with potential $\Phi_B$ satisfying $\partial \Phi_B / \partial q_i = \partial O_B^{(i)} / \partial q_i$ for each $i$. The unique Nash equilibrium $q_{B, \text{Nash}}^\ast$ is locally attracting under gradient flow, with local-curvature parameter $\lambda_{\min}(\nabla^2 \Phi_B(q_{B, \text{Nash}}^\ast))$ controlling the rate. Linearizing the best-response gradient flow around the Nash and adding the same observation noise, the stationary marginal distribution of each sub-agent's state is

$$\mu_{\infty, B}^{(i)} \;=\; \mathcal N\!\left(\,q_{B, \text{Nash}}^\ast,\; \sigma^2 / (2 \lambda_{\min}(\nabla^2 \Phi_B))\,\right).$$

**Parameter-matching.** Two free parameters on each side: $(T, \alpha)$ for Composite A, $(a_0, b, c)$ for Composite B (with $\alpha$ implicit in the gradient-flow rate). Two matching conditions:

- **Mean-matching:** $T_A / 2 = q_{B, \text{Nash}}^\ast$. Choose $T_A = 2\, q_{B, \text{Nash}}^\ast$.
- **Variance-matching:** $\sigma^2 / (2\alpha) = \sigma^2 / (2\,\lambda_{\min}(\nabla^2 \Phi_B))$. Choose $b$ in Composite B such that $\lambda_{\min}(\nabla^2 \Phi_B) = \alpha$.

Under both conditions: $\mu_{\infty, A}^{(i)} = \mu_{\infty, B}^{(i)} = \mathcal N(q^\ast, \sigma^2/(2\alpha))$ for both $i$, where $q^\ast = T_A/2 = q_{B, \text{Nash}}^\ast$. The marginal *transient* second moments also match under the matched local-curvature condition — both are exponentially-converging Ornstein-Uhlenbeck-type processes per sub-agent in the linearization.

**The R0/R1 witness.** Composite A satisfies $\mathcal R(\Sigma_A) = \text{R0}$ (unique global attractor + global Lyapunov); Composite B satisfies $\mathcal R(\Sigma_B) = \text{R1}$ (unique-Nash equilibrium with local Lyapunov-on-deviation, but Nash structure rather than shared-target structure). The marginal-data observer sees identical $\mu^{(i)}$ in both; cannot distinguish $\mathcal R = \text{R0}$ from $\mathcal R = \text{R1}$. ∎

### Witness 2: R0 vs R2 indistinguishability

*[Derived (cross-regime-witness, from matching-pennies aggregation + shared-target marginal-matching)]*

**Composite C — R2 cyclic-distributional regime (matching-pennies under continuous-action smoothing).** Take the $2 \times 2$ matching-pennies payoff structure, smoothed to continuous actions via softmax-style best-response with temperature parameter $\tau$. The composite has no pure-strategy Nash; the mixed-Nash is at $(1/2, 1/2)$; under no-regret dynamics (Hart-Mas-Colell 2000) the empirical joint distribution converges to the CCE set at rate $O(1/\sqrt T)$. The per-sub-agent marginal stationary distribution under this regime is a continuous distribution with mean $1/2$ and bounded variance determined by $\tau$ and the noise level $\sigma^2$.

**Parameter-matching to Composite A.** Choose Composite A's parameters $(T_A, \alpha_A)$ to align with Composite C's per-sub-agent marginal mean ($T_A / 2 = 1/2 \Rightarrow T_A = 1$) and variance (choose $\alpha_A$ such that $\sigma^2 / (2 \alpha_A)$ equals Composite C's marginal variance — solvable for appropriate $\tau$).

**The R0/R2 witness.** Composite A is R0 (state-variable macro-state, joint Lyapunov). Composite C is R2 (distributional macro-state, no joint Lyapunov on $\mathcal X^c$; CCE convergence only). The marginal-data observer sees identical $\mu^{(i)}$ in both; cannot distinguish $\mathcal R = \text{R0}$ from $\mathcal R = \text{R2}$. This sharpening is qualitatively cleaner than the R0/R1 witness because the *joint* dynamic regimes differ qualitatively — convergent vs cyclic-in-joint-distribution — while the per-sub-agent marginals can be made stationary in both cases by appropriate observation-aggregation: cyclic in the *joint* distribution projects to *stationary* in the marginal distribution when the cycle is over the joint coordinate that the marginal averages out. ∎

### Mechanism (Sylvester at one remove, same as Instances 1 / 2 / 4)

*[Discussion]*

The composite-level topology coordinate — the bit $(\sigma, p)$ distinguishing R0 / R1 / R2, where $\sigma$ is the coupling-sign-bit (cooperative vs adversarial) and $p$ is the potential-existence bit (potential/monotone game-structure vs none) — enters the per-sub-agent marginal observation law $p(q_i \mid \theta_{\text{topology}})$ only through the *fixed-point* and *local-curvature* parameters that the witness constructions above match across composites. Computing the Fisher information of the marginal observation law with respect to $\theta_{\text{topology}}$ yields a rank-deficient matrix: the topology coordinate has a null direction along the manifold

$$\Big\{\theta : (\text{mean}, \text{variance})(\theta) = (q^\ast, \sigma^2/(2\alpha))\Big\}.$$

By Sylvester's law of inertia (`#disc-identifiability-floor` Sylvester-recognition Finding), no reparameterization of the marginal-observation coordinate system removes this null direction — the irreducibility is invariant under the observer's representational freedom. The escape requires *rank-augmentation*: observation of a coordinate the marginal projection has annihilated. This is exactly the same mechanism as `#disc-identifiability-floor` Instances 1, 2, and 4; the present derivation occupies the *same* rank-collapse subclass as Instance 3's original coupling-sign-bit derivation, with the rank-collapse occurring on a topology coordinate of higher dimension than Instance 3's single sign-bit.

The mechanism's *one-remove* status (per `#disc-identifiability-floor` Instance 4's Mechanism discussion) is preserved: the *generating* action producing the indistinguishable pair is the swap between cooperative-shared-objective coupling and strategic-potential-game coupling (a structural game-theoretic operation), not metric congruence; but the *escape-side* irreducibility under the observer's representational freedom is identical to Instance 2's Fisher-null-on-a-fiber. The architecture of the proof is parallel to Instance 4's, applied to a different topology coordinate.

## Epistemic Status

*Conditional* on the standard coupling models (Model D for disturbance; the same models `#deriv-critical-mass-composition` uses for Instance 3's original coupling-sign-bit construction). The two witness constructions are at parameter-by-parameter explicit level for the symmetric-matched-Tier-1-scalar case (R0 vs R1 with $T_A = 2 q_{B, \text{Nash}}^\ast$ and $\lambda_{\min}(\nabla^2 \Phi_B) = \alpha$ as the matching conditions; R0 vs R2 with mean-matching and variance-matching against the matching-pennies-with-continuous-smoothing marginal).

Max attainable: *exact* in the symmetric-matched-Tier-1-scalar sub-scope, anchored by the explicit parameter matching above; *robust qualitative* in the general heterogeneous case, inheriting the Liberzon 2003 / Dayawansa-Martin 1999 / Shorten et al. 2007 common-Lyapunov-nonexistence structure that `#disc-identifiability-floor` Instance 3 (Boundary Characterization) already invokes. The tier statement is the same one Instance 3 carries; the broader topology coordinate does not change the tier.

## Discussion

### Why this is a supporting derivation rather than a sixth identifiability-floor instance

The witness constructions in §"Witness 1" and §"Witness 2" *do* derive a cross-regime no-go from per-sub-agent marginal data, but the integrity test on M1 (the five-element test sharpened by `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §2 and applied in `spikes/spike-identifiability-floor-instance-6-2026-05-21.md` §4) finds three of four distinctness criteria failing against the existing Instance 3:

- Same external theorem (Liberzon 2003 / Dayawansa-Martin 1999 / Shorten et al. 2007 — the same anchor Instance 3 invokes; no new external theorem required).
- Same mechanism family (rank-collapse / Sylvester-at-one-remove on the marginal-Fisher operator).
- Four of five escapes inherit verbatim from Instance 3 (a, b, c, d unchanged; only (e) is new).
- Two of three strengthened consequences inherit-with-broadening from Instance 3; only the `#deriv-strategic-composition` sub-scope $\alpha'/\beta'$ elevation is genuinely new.

Per the strengthen-first landing posture (`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md` and its landing-half `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`), this segment lands the *math* in canon (math-lives-in-segments discipline) while the *Instance 3 broadening* in `#disc-identifiability-floor` lands the *no-go statement, escape menu, and strengthened consequence* (integration-is-replacement at the meta-segment scope level). The candidate "Instance 6" framing is deleted; the broadening of Instance 3 carries the strengthened content; this segment carries the explicit witness backing.

The split — math segment plus meta-segment broadening rather than a new instance — preserves M1's instance-count integrity (the instances are *plural in mechanism*, not just plural in surface no-go) while ensuring the derived content lands in canon at full visibility.

### Relationship to `#disc-dynamic-regime-axis`

This segment's witnesses are what concretely back `#disc-dynamic-regime-axis`'s §H "Identifiability floor for regime" — the regime-axis meta-segment names the negative-half complementarity in the abstract; this segment supplies the constructive witness showing the no-go is real and parameter-explicit. The relationship is parallel to how `#disc-identifiability-floor` Instance 3's coupling-sign-bit witness in `#deriv-critical-mass-composition` (asymmetric-limit treatment) backs the meta-segment-level no-go statement.

When the dynamic-regime axis advances to meta-segment status (per `spikes/strategic-composition-class-3-attempt-2026-05-21/07-SOLIDIFIED-PLAN.md` Phase 6), this segment is the canonical backing for the regime-axis floor; the complementarity structure (`#disc-separability-pattern` ↔ `#disc-identifiability-floor` parallel for the regime axis) is then:

- *Positive half:* `#disc-dynamic-regime-axis` four-tier ladder (R0 / R1 / R2 / R3 with their respective Lyapunov machinery).
- *Negative half:* `#disc-identifiability-floor` Instance 3 (broadened) — backed by this segment's witnesses.

The double-duty Instance 3 serves both `#disc-separability-pattern` Contraction ladder *and* `#disc-dynamic-regime-axis` four-tier ladder; this segment's witnesses extend that double-duty to the regime-axis level explicitly.

### Open extensions

- **Composite-of-composites case.** The witness constructions handle finite-$N$ matched-symmetric-Tier-1 sub-agents. The composite-of-composites question (regime-identification of meta-composites from sub-composite marginal data) plausibly inherits the Liberzon machinery one level up but is not derived here.
- **Finite-sample refinements.** The §"Witness 1" / §"Witness 2" constructions are exact-population statements (stationary distributions identical). The finite-sample minimax error of regime classification under observation budget $T$ is the Fano-style refinement that the 2026-05-20 spike correctly identified as the *adjacent* tool. Should be derivable from `#der-agent-opacity` $H_b$ machinery applied at the composite layer; not done here.
- **Mean-field R3 lift.** The §"Witness 1" / §"Witness 2" constructions handle R0 / R1 / R2 finite-$N$. The R3 mean-field tier (per `#disc-dynamic-regime-axis` §B.3) has its own identifiability question — from finite-$N$ marginal data, can the limit MFG regime be identified? Plausibly governed by the Lasry-Lions-monotonicity-vs-not bit (the MFG-analog of the potential-existence bit handled here). Tied to the R3 lift in `#deriv-strategic-composition` Working Notes mean-field extension.

## Findings

### Cross-Regime Marginal Indistinguishability (Witness Backing for Broadened Instance 3)

**Brief:** When you watch only one player at a time in a multi-agent system, you cannot tell what game they are playing — and "what game they are playing" determines whether the system as a whole will settle to a target, settle to a strategic equilibrium, or cycle in distribution forever. Two concrete worked constructions show this: two firms in Cournot competition that produce identical per-firm production-quantity distributions to a rowing team optimizing for a shared target (different game, same marginal); two players in matching pennies whose mixed strategy produces identical per-player action distributions to the same rowing team (different *kind* of equilibrium, same marginal). The mechanism is the same as for the simpler coupling-sign-bit case: the topology bit lives in a direction the marginal projection annihilates, and Sylvester's law of inertia says you cannot recover an annihilated direction by changing the units on the ruler — only by looking from a new vantage point (intervening on the topology, or observing the joint trajectory's convergence-rate class).

**Impact:** Backs `#disc-identifiability-floor` Instance 3's 2026-05-21 broadening from coupling-sign-bit to coupling-topology-bit with explicit parameter-by-parameter witness constructions. Preserves the math-lives-in-segments discipline (the derivation lives in canon, not only in the spike). Provides the canonical worked instantiation for the broadened no-go, parallel to how `#deriv-critical-mass-composition`'s asymmetric-limit treatment carries Instance 3's original coupling-sign-bit witness. Operationalizes the "regime is unidentifiable from per-sub-agent marginals" claim that the dynamic-regime axis meta-segment (`#disc-dynamic-regime-axis`) references as the negative-half of its complementarity structure.

**Novelty Claim:** *Claim integration* — the witness constructions extend Instance 3's coupling-sign-bit construction to broader topology coordinates (R0 vs R1; R0 vs R2) using the same Liberzon 2003 / Dayawansa-Martin 1999 / Shorten et al. 2007 anchor and the same Sylvester-at-one-remove mechanism. The Cournot construction (Composite B in §"Witness 1") is standard Monderer-Shapley 1996 potential-game-as-Cournot; the matching-pennies construction (Composite C in §"Witness 2") is standard rock-paper-scissors-style cyclic-game smoothing. The contribution is the parameter-matching against R0 shared-target dynamics that produces marginal-indistinguishability across regimes — and the mechanism reduction to Instance 3's rank-collapse-on-topology-coordinate framework.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Common-Lyapunov nonexistence for switched systems | Liberzon 2003 *Switching in Systems and Control* §2.1; Dayawansa-Martin 1999 *IEEE TAC* 44:751; Shorten et al. 2007 *SIAM Review* 49:545 | *formal antecedent* — same anchor `#disc-identifiability-floor` Instance 3 invokes; this segment extends the application from coupling-sign-bit to coupling-topology-bit |
| Cournot duopoly as potential game | Cournot 1838 *Recherches*; Monderer-Shapley 1996 *Games and Economic Behavior* 14:124 §3 | *formal antecedent* — standard potential-game instantiation used as Composite B in Witness 1 |
| Matching pennies / cyclic-game smoothing | Standard textbook (Fudenberg-Tirole 1991 *Game Theory* §1; Hart-Mas-Colell 2000 *Econometrica* 68:1127) | *formal antecedent* — standard cyclic-game template used as Composite C in Witness 2 |
| Sylvester's law of inertia as escape-irreducibility | Sylvester 1852 *Phil. Mag.* 4(23):138; cf. `#disc-identifiability-floor` Sylvester-recognition Finding | *formal antecedent* — same congruence-invariance machinery the rank-collapse subclass relies on |

**Search Log:**

- 2026-05-21 (*targeted*, BG2 derivation spike at `spikes/spike-identifiability-floor-instance-6-2026-05-21.md`): Re-read `#disc-identifiability-floor` (full segment), Instance 3 in detail, the 2026-05-20 spike's M1 five-element-test discipline, `#disc-stability-certificate` mechanism taxonomy, `#deriv-critical-mass-composition` for Instance-3 escape-(b) operationalization. All citations in this segment's §"Witness 1" / §"Witness 2" (Liberzon 2003, Dayawansa-Martin 1999, Shorten et al. 2007, Monderer-Shapley 1996, Hart-Mas-Colell 2000) are inherited from existing AAT machinery's citation set; no new external citations are introduced. The witness construction is a parameter-matched application of standard game-theoretic templates against the R0 shared-objective dynamics — the constructions are not novel in themselves; the contribution is the cross-regime marginal-indistinguishability *recognition* and the mechanism-reduction to Instance 3's rank-collapse framework.

## Working Notes

- **Provenance.** Derivation worked in `spikes/spike-identifiability-floor-instance-6-2026-05-21.md` §3.3. The spike's §4 M1 distinctness check identified three of four tests failing against Instance 3, landing the recommendation as "broaden Instance 3 + new appendix segment" rather than "new Instance 6." This segment is the new appendix segment per that landing.
- **Cross-regime witness sub-cases.** Witness 1 (R0 vs R1) is the load-bearing cross-regime construction. Witness 2 (R0 vs R2) is qualitatively cleaner (the joint regime differs more dramatically) but operationally similar. A fourth witness (R1 vs R2 — Cournot equilibrium with parameter-matched marginals to matching-pennies cyclic dynamics) is plausible but not derived here; per the strengthen-first second-pass, the R0 vs R1 and R0 vs R2 witnesses are sufficient to establish the broadened no-go scope.
- **Connection to escape (e).** The convergence-rate-class escape (per `#disc-identifiability-floor` Instance 3 escape (e), added 2026-05-21) distinguishes Witness 2's R0-vs-R2 case passively: Composite A converges exponentially, Composite C converges polynomially. Escape (e) does *not* distinguish Witness 1's R0-vs-R1 case (both converge exponentially at the matched local rate $\alpha$); the R0-vs-R1 distinction requires one of escapes (a)-(d) per the Instance-3 Boundary Characterization.
- **Composite-of-composites lift.** Per `#disc-dynamic-regime-axis` §I (Q3), the regime axis under nested composition is open. A natural extension of this segment's witnesses to composite-of-composites would test whether marginal-indistinguishability at the sub-composite layer propagates to the meta-composite regime question. Follow-on spike candidate if the composition-of-regimes question becomes load-bearing for `04-eli-core/` population work.
- **Fano-style finite-sample refinement.** The §"Witness 1" / §"Witness 2" constructions are exact-population statements. A finite-sample bound on regime-classification minimax error at observation budget $T$ would be the natural quantitative companion — per the 2026-05-20 spike's Fano-anchor-as-finite-sample-refinement distinction. Plausibly derivable from `#der-agent-opacity` $H_b$ machinery applied at the composite layer; not in scope here.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. This segment uses regime-axis vocabulary (R0/R1/R2) rather than GUC-class vocabulary; no GUC-class references inside. Removed at `candidate` stage per FORMAT.md Gate 4.
