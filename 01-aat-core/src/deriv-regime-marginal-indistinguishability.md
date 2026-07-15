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

The relationship to `#disc-identifiability-floor` Instance 3 is supporting-derivation — Instance 3 carries the no-go statement, the escape menu, and the strengthened consequence; this segment carries the explicit construction backing the broadened no-go.

## Formal Expression

### Setup

Consider $N = 2$ scalar sub-agents indexed $i \in \{1, 2\}$, each with state $q_i \in \mathbb{R}$, base correction rate $\alpha \gt 0$, observation noise $w_i \sim \mathcal{N}(0, \sigma^2)$, base disturbance bound $\rho$, tempo $\mathcal{T}$. The composite state is $X^c = (q_1, q_2) \in \mathbb{R}^2$. An external observer $B$ accesses *only* per-sub-agent marginal data: for each $i$, the marginal stationary distribution $\mu_\infty^{(i)}$, the local mismatch process, and the per-sub-agent update rule $f_M^{(i)}$ as a structural object (white-box on each sub-agent, observed in isolation). The observer does *not* see: the composite-level coupling topology (sign + structure of cross-agent influence), the joint trajectory $\{X_t^c\}$ (only the projection onto per-sub-agent marginals), the game-structure object $\{O^{(j)}\}_{j \neq i}$ from sub-agent $i$'s frame, or composite-level convergence-rate-class diagnostics.

The inferential question: from per-sub-agent marginal data alone, can $B$ identify the composite's dynamic regime $\mathcal{R}(X^c) \in \{\text{R0}, \text{R1}, \text{R2}\}$ per `#disc-dynamic-regime-axis` §B?

### Witness 1: R0 vs R1 indistinguishability

*[Derived (cross-regime-witness, from Cournot equilibrium structure + shared-target marginal-matching)]*

**Composite A — R0 shared-objective contraction.** Sub-agent objective $O_A^{(i)} = -\tfrac{1}{2}(q_1 + q_2 - T)^2$ for shared target $T$. Per-agent gradient-flow best-response:

$$\dot q_i \;=\; -\alpha\,(q_i + q_j - T) + w_i.$$

The composite is R0 per `#disc-dynamic-regime-axis` §B.0: unique attracting fixed point at $(T/2, T/2)$, joint Lyapunov $V = \tfrac{1}{2}\lVert q - (T/2, T/2) \rVert^2$, exponential convergence at rate $\alpha$. The stationary marginal distribution of each sub-agent's state, computed from the linearized Ornstein-Uhlenbeck dynamics, is

$$\mu_{\infty, A}^{(i)} \;=\; \mathcal{N}\!\left(\,T/2,\; \sigma^2/(2\alpha)\,\right).$$

**Composite B — R1 strategic potential-game equilibrium (Cournot).** Sub-agent objective $O_B^{(i)} = q_i\,(a_0 - b(q_1 + q_2) - c)$ — quadratic-profit Cournot in canonical form. The game is a potential game (Monderer-Shapley 1996) with potential $\Phi_B$ satisfying $\partial \Phi_B / \partial q_i = \partial O_B^{(i)} / \partial q_i$ for each $i$. The unique Nash equilibrium $q_{B, \text{Nash}}^\ast$ is locally attracting under gradient flow, with local-curvature parameter $\lambda_{\min}(\nabla^2 \Phi_B(q_{B, \text{Nash}}^\ast))$ controlling the rate. Linearizing the best-response gradient flow around the Nash and adding the same observation noise, the stationary marginal distribution of each sub-agent's state is

$$\mu_{\infty, B}^{(i)} \;=\; \mathcal{N}\!\left(\,q_{B, \text{Nash}}^\ast,\; \sigma^2 / (2 \lambda_{\min}(\nabla^2 \Phi_B))\,\right).$$

**Parameter-matching.** Two free parameters on each side: $(T, \alpha)$ for Composite A, $(a_0, b, c)$ for Composite B (with $\alpha$ implicit in the gradient-flow rate). Two matching conditions:

- **Mean-matching:** $T_A / 2 = q_{B, \text{Nash}}^\ast$. Choose $T_A = 2\, q_{B, \text{Nash}}^\ast$.
- **Variance-matching:** $\sigma^2 / (2\alpha) = \sigma^2 / (2\,\lambda_{\min}(\nabla^2 \Phi_B))$. Choose $b$ in Composite B such that $\lambda_{\min}(\nabla^2 \Phi_B) = \alpha$.

Under both conditions: $\mu_{\infty, A}^{(i)} = \mu_{\infty, B}^{(i)} = \mathcal{N}(q^\ast, \sigma^2/(2\alpha))$ for both $i$, where $q^\ast = T_A/2 = q_{B, \text{Nash}}^\ast$. The marginal *transient* second moments also match under the matched local-curvature condition — both are exponentially-converging Ornstein-Uhlenbeck-type processes per sub-agent in the linearization.

**The R0/R1 witness.** Composite A satisfies $\mathcal{R}(\Sigma_A) = \text{R0}$ (unique global attractor + global Lyapunov); Composite B satisfies $\mathcal{R}(\Sigma_B) = \text{R1}$ (unique-Nash equilibrium with local Lyapunov-on-deviation, but Nash structure rather than shared-target structure). The marginal-data observer sees identical $\mu^{(i)}$ in both; cannot distinguish $\mathcal{R} = \text{R0}$ from $\mathcal{R} = \text{R1}$. ∎

### Witness 2: R0 vs R2 indistinguishability

*[Derived (cross-regime-witness, from matching-pennies aggregation + shared-target marginal-matching)]*

**Composite C — R2 cyclic-distributional regime (matching-pennies under continuous-action smoothing).** Take the $2 \times 2$ matching-pennies payoff structure, smoothed to continuous actions via softmax-style best-response with temperature parameter $\tau$. The composite has no pure-strategy Nash; the mixed-Nash is at $(1/2, 1/2)$; under no-regret dynamics (Hart-Mas-Colell 2000) the empirical joint distribution converges to the CCE set at rate $O(1/\sqrt T)$. The per-sub-agent marginal stationary distribution under this regime is a continuous distribution with mean $1/2$ and bounded variance determined by $\tau$ and the noise level $\sigma^2$.

**Parameter-matching to Composite A.** Choose Composite A's parameters $(T_A, \alpha_A)$ to align with Composite C's per-sub-agent marginal mean ($T_A / 2 = 1/2 \Rightarrow T_A = 1$) and variance (choose $\alpha_A$ such that $\sigma^2 / (2 \alpha_A)$ equals Composite C's marginal variance — solvable for appropriate $\tau$).

**The R0/R2 witness.** Composite A is R0 (state-variable macro-state, joint Lyapunov). Composite C is R2 (distributional macro-state, no joint Lyapunov on $\mathcal{X}^c$; CCE convergence only). The marginal-data observer sees identical $\mu^{(i)}$ in both; cannot distinguish $\mathcal{R} = \text{R0}$ from $\mathcal{R} = \text{R2}$. This sharpening is qualitatively cleaner than the R0/R1 witness because the *joint* dynamic regimes differ qualitatively — convergent vs cyclic-in-joint-distribution — while the per-sub-agent marginals can be made stationary in both cases by appropriate observation-aggregation: cyclic in the *joint* distribution projects to *stationary* in the marginal distribution when the cycle is over the joint coordinate that the marginal averages out. ∎

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

The witness constructions in §"Witness 1" and §"Witness 2" *do* derive a cross-regime no-go from per-sub-agent marginal data, but the integrity test on M1 (the five-element distinctness test) finds three of four distinctness criteria failing against the existing Instance 3:

- Same external theorem (Liberzon 2003 / Dayawansa-Martin 1999 / Shorten et al. 2007 — the same anchor Instance 3 invokes; no new external theorem required).
- Same mechanism family (rank-collapse / Sylvester-at-one-remove on the marginal-Fisher operator).
- Four of five escapes inherit verbatim from Instance 3 (a, b, c, d unchanged; only (e) is new).
- Two of three strengthened consequences inherit-with-broadening from Instance 3; only the `#deriv-strategic-composition` sub-scope $\alpha'/\beta'$ elevation is genuinely new.

Per the strengthen-first landing posture (`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md` and its landing-half `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`), this segment lands the *math* in canon (math-lives-in-segments discipline) while the *Instance 3 broadening* in `#disc-identifiability-floor` lands the *no-go statement, escape menu, and strengthened consequence* (integration-is-replacement at the meta-segment scope level). The candidate "Instance 6" framing is deleted; the broadening of Instance 3 carries the strengthened content; this segment carries the explicit witness backing.

The split — math segment plus meta-segment broadening rather than a new instance — preserves M1's instance-count integrity (the instances are *plural in mechanism*, not just plural in surface no-go) while ensuring the derived content lands in canon at full visibility.

### Relationship to `#disc-dynamic-regime-axis`

This segment's witnesses are what concretely back `#disc-dynamic-regime-axis`'s §H "Identifiability floor for regime" — the regime-axis meta-segment names the negative-half complementarity in the abstract; this segment supplies the constructive witness showing the no-go is real and parameter-explicit. The relationship is parallel to how `#disc-identifiability-floor` Instance 3's coupling-sign-bit witness in `#deriv-critical-mass-composition` (asymmetric-limit treatment) backs the meta-segment-level no-go statement.

When the dynamic-regime axis advances to meta-segment status, this segment is the canonical backing for the regime-axis floor; the complementarity structure (`#disc-separability-pattern` ↔ `#disc-identifiability-floor` parallel for the regime axis) is then:

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
| Multivariate Markov chains with prescribed component behavior but different joint dependence | Bielecki-Jakubowski-Niewkeglowski 2011, *Intricacies of dependence between components of multivariate Markov chains: weak Markov consistency and weak Markov copulae* (DOI 10.1214/EJP.V18-2238)[^bg2-2026-05-21] | *closest structural analogue* — same-marginals-different-coupling-law construction at the multivariate Markov-chain level; the hidden distinction is filtration-level dependence rather than potential-vs-cyclic game structure, but the formal move (matched per-component behavior, distinct joint law) is the same shape as Witness 1 / Witness 2 at the game-topology level |
| Marginal-non-determining ergodic measures (stochastic-process side) | Courbage-Hamdan 2001, *A family of stationary processes with infinite memory having the same p-marginals* (DOI 10.4064/CM90-2-2)[^bg2-2026-05-21]; Courbage-Hamdan 1998, *An ergodic Markov chain is not determined by its two-dimensional marginal laws* (DOI 10.1016/S0167-7152(97)00096-5)[^bg2-2026-05-21]; Hamdan 2000, *Markov Chains with Positive Transitions Are Not Determined by Any p-Marginals* (DOI 10.1007/S006050070034 — journal-name unverified at landing time)[^bg2-2026-05-21]; Hamdan 2002, *An ergodic Markov chain is not determined by any p-marginals* (DOI 10.1016/S0019-3577(02)80028-3)[^bg2-2026-05-21] | *adjacent literature* — strong precedent for "finite-order marginals do not determine the generating law" at the stochastic-process level. Different object (Markov chains, not coupled best-response dynamics) but identical formal shape (matched marginals, distinct joint law) |
| Network-reconstruction limits from temporal data | Angulo-Moreno-Barabási-Liu 2015, *Fundamental limitations of network reconstruction* (arXiv:1508.03559)[^bg2-2026-05-21] | *adjacent literature* — graph topology is generically as hard to recover as the full interaction matrix without persistent excitation; underdetermines coupling from per-node observation. Closest network-level impossibility neighbor on the topology-from-component-data axis. Different setting (general dynamical, not strategic), but the underdetermination-from-reduced-observation pattern is shared |
| Delay-reconstruction recovers only transitive closure | Cummins-Gedeon-Spendlove 2015, *On the Efficacy of State Space Reconstruction Methods in Determining Causality* (SIAM J. Appl. Dyn. Syst. 14:335)[^bg2-2026-05-21] | *adjacent literature* — componentwise trajectory data recovers at most the transitive closure of the interaction graph, not direct edges or feedback orientation. Explicit negative result on what trajectory data cannot tell an observer; not a game-structure witness but operationally similar shape |
| Game-side observational equivalence (quantal-response rationalization; consistent-game-set characterization) | Haile-Hortaçsu-Kosenok 2008, *On the Empirical Content of Quantal Response Equilibrium* (DOI 10.1257/AER.98.1.180)[^bg2-2026-05-21] (any interior action distribution rationalizable as QRE); Ziani-Chandrasekaran-Ligett 2016, *Efficiently Characterizing Games Consistent with Perturbed Equilibrium Observations* (DOI 10.7907/Z91Z42CF)[^bg2-2026-05-21] (characterizing the whole consistent set of games rather than point-identifying) | *adjacent literature* — stronger observational-equivalence statements on the game side than mere nonidentification, but at the equilibrium-rationalization layer rather than the per-component-marginal-trajectory layer this segment treats. Game-topology distinction (potential vs non-potential; cooperative vs cyclic) not the target of these results |
| Information-structure observational compatibility | Penalva-Ryall 2003, *Causal assessment in finite extensive-form games*[^bg2-2026-05-21]; Penalva-Zuasti-Fabra-Ryall 2004, *Empirical Implications of Information Structure in Finite-Length Extensive-Form Games*[^bg2-2026-05-21]; Lehrer-Rosenberg-Shmaya 2006, *Signaling and mediation in Bayesian games*[^bg2-2026-05-21] | *adjacent literature* — different information structures observationally compatible with respect to outcome / equilibrium distributions; another form of hidden structure surviving unchanged at the observable level. Different concern (information structure, signaling, mediation) but same shape (hidden distinction not visible at observable layer) |

**Novelty assessment.** The cross-topology game witness with hidden distinction in potential-vs-non-potential or cooperative-vs-cyclic structure under matched per-component marginals appears uncodified relative to the prior-art search[^bg2-2026-05-21]; Witness 1 (R0-vs-R1 Cournot under matched marginal mean and variance) and Witness 2 (R0-vs-R2 matching-pennies under aggregation) are the specific instantiations the verdict identifies as uncodified. The closest structural analogues are Bielecki et al. 2011 (multivariate Markov-chain same-marginals-different-coupling) and the Courbage-Hamdan / Hamdan sequence (marginal-non-determining stochastic processes) — both at the stochastic-process layer rather than the game-topology layer. AAT's contribution: the *naming claim* on the game-topology-bit witness as the cross-regime indistinguishability instantiation of the established marginal-non-determining shape.

**Search Log:**

- 2026-05-21 (*targeted*): The core citations in §"Witness 1" / §"Witness 2" (Liberzon 2003, Dayawansa-Martin 1999, Shorten et al. 2007, Monderer-Shapley 1996, Hart-Mas-Colell 2000) are inherited from existing AAT machinery's citation set; the witness construction is a parameter-matched application of standard game-theoretic templates against R0 shared-objective dynamics — the constructions are not novel in themselves, and the contribution is the cross-regime marginal-indistinguishability *recognition* and the mechanism-reduction to Instance 3's rank-collapse framework.
- 2026-05-21 (*targeted second-pass*): A second-pass comprehensive-search pass searched specifically for prior art on (Q1) broader-topology-bit unidentifiability beyond the coupling-sign-bit witness, and (Q2) convergence-rate-class as a passive regime classifier. Verdict on both: *no exact hit found in this set*. The Related Work table above incorporates the verdict's strongest neighbors at adjacent layers; see footnote `[^bg2-2026-05-21]` for the verification-deferral notice on every neighbor citation introduced from this pass.

## Working Notes

- **Provenance.** Derivation worked in `spikes/.integrated/spike-identifiability-floor-instance-6-2026-05-21.md` §3.3. The spike's §4 M1 distinctness check identified three of four tests failing against Instance 3, landing the recommendation as "broaden Instance 3 + new appendix segment" rather than "new Instance 6." This segment is the new appendix segment per that landing.
- **Cross-regime witness sub-cases.** Witness 1 (R0 vs R1) is the load-bearing cross-regime construction. Witness 2 (R0 vs R2) is qualitatively cleaner (the joint regime differs more dramatically) but operationally similar. A fourth witness (R1 vs R2 — Cournot equilibrium with parameter-matched marginals to matching-pennies cyclic dynamics) is plausible but not derived here; per the strengthen-first second-pass, the R0 vs R1 and R0 vs R2 witnesses are sufficient to establish the broadened no-go scope.
- **Connection to escape (e).** The convergence-rate-class escape (per `#disc-identifiability-floor` Instance 3 escape (e), added 2026-05-21) distinguishes Witness 2's R0-vs-R2 case passively: Composite A converges exponentially, Composite C converges polynomially. Escape (e) does *not* distinguish Witness 1's R0-vs-R1 case (both converge exponentially at the matched local rate $\alpha$); the R0-vs-R1 distinction requires one of escapes (a)-(d) per the Instance-3 Boundary Characterization.
- **Composite-of-composites lift.** Per `#disc-dynamic-regime-axis` §I (Q3), the regime axis under nested composition is open. A natural extension of this segment's witnesses to composite-of-composites would test whether marginal-indistinguishability at the sub-composite layer propagates to the meta-composite regime question. Follow-on spike candidate if the composition-of-regimes question becomes load-bearing for `04-eli-core/` population work.
- **Fano-style finite-sample refinement.** The §"Witness 1" / §"Witness 2" constructions are exact-population statements. A finite-sample bound on regime-classification minimax error at observation budget $T$ would be the natural quantitative companion — per the 2026-05-20 spike's Fano-anchor-as-finite-sample-refinement distinction. Plausibly derivable from `#der-agent-opacity` $H_b$ machinery applied at the composite layer; not in scope here.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. This segment uses regime-axis vocabulary (R0/R1/R2) rather than GUC-class vocabulary; no GUC-class references inside. Removed at `candidate` stage per FORMAT.md Gate 4.

- **Primary-source verification spike queued (2026-05-21).** All BG2-introduced citations in this segment's Related Work table (marked with footnote `[^bg2-2026-05-21]`) need primary-source verification before any further reliance. The characterizations attributed to those papers are currently synthesized from `ref/Unidentifiability_and_rate_class_prior_art.md`, not from direct reading of the sources. Verification targets in approximate load-bearing order for this segment: (i) Bielecki-Jakubowski-Niewkeglowski 2011 — *closest structural analogue* (multivariate-Markov-chain same-marginals-different-coupling); load-bearing for the segment's positioning of the Witness math; (ii) Courbage-Hamdan 2001 + Courbage-Hamdan 1998 + Hamdan 2000 + Hamdan 2002 sequence — strongest direct-precedent for "finite-order marginals do not determine the generating law"; the Hamdan 2000 journal name was not specified in the Undermind report and should be resolved at verification (the DOI prefix would identify it, but the executor will not infer from DOI structure without confirming the actual paper); (iii) Angulo et al. 2015, Cummins et al. 2015 — network-reconstruction limits; (iv) Haile et al. 2008, Ziani et al. 2016 — game-side observational equivalence; (v) Penalva et al. 2003/2004, Lehrer et al. 2006 — information-structure observational compatibility. Spike to be scheduled per Joseph's go.

[^bg2-2026-05-21]: The paper and the characterization of its claims are inherited from a second-pass Undermind synthesis (search conducted 2026-05-21); the primary source has *not* been verified at landing time. A primary-source verification spike is queued — see Working Notes above.
