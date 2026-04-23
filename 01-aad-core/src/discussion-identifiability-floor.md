---
slug: discussion-identifiability-floor
type: discussion
status: discussion-grade
depends:
  - causal-insufficiency-detection
  - strategic-dynamics-derivation
  - causal-hierarchy-requirement
  - loop-interventional-access
stage: draft
---

# Discussion: The Identifiability Floor — A Class of Structural No-Go Results

AAD has derived a class of structural impossibility results — *floors below which* identification or detection is impossible from limited information. Each floor arises by applying an external information-theoretic theorem (the Pearl/Bareinboim causal hierarchy; the Cramér-Rao bound on Fisher information) to a specific AAD setting. The floors are negative results in form but positive in consequence: they precisely characterize what additional structure (loop-interventional access, multi-channel observability, observable latents) is required to escape the floor, and thereby strengthen the load-bearing role of the AAD machinery that supplies it.

This segment names the meta-pattern, collects the current instances, and identifies adjacent floors that are open research directions.

## The Pattern

Each instance of the identifiability floor has the form:

1. **Setting.** An AAD inferential task — detect a structural property, identify a parameter, distinguish two model classes — under a specific information regime (purely observational data, single observation channel, observation of marginals only, etc.).
2. **External theorem.** An information-theoretic limit independent of AAD: the causal hierarchy theorem (Bareinboim, Correa, Ibeling & Icard 2022) for distinguishing observational and interventional content; the Cramér-Rao bound for unbiased estimation under finite Fisher information.
3. **No-go.** The external theorem is invoked to prove that the inferential task is impossible under the regime: no statistic, no Bayesian comparison, no online estimator can succeed using only the available information.
4. **Boundary characterization.** The conditions under which the floor's regime fails — i.e., the agent has *more* information than the regime allows — admit (partial) identification. Each boundary route maps onto specific AAD machinery already required by the theory.
5. **Strengthened consequence.** The floor strengthens the load-bearing role of whichever AAD machinery is the unique broadly-available violation of the regime. Often this elevates a piece of machinery from "useful" to "structurally required by the theory."

The pattern is *not* a negative posture. AAD does not say "many things are impossible." It says: "here is precisely what cannot be inferred from limited data; here is exactly which additional capability is required to recover identification; the AAD machinery that supplies that capability is therefore load-bearing in the strongest possible sense — without it, the no-go forbids the inference entirely."

## Current Instances

### Instance 1 — On-Policy L0 Insufficiency Detection ( #causal-insufficiency-detection)

**Setting.** Detect whether an L0 strategy DAG is causally insufficient (a latent common cause is acting on multiple sibling action propositions) using only the agent's on-policy observation history under sequential short-circuit AND/OR execution.

**External theorem.** Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem: there exist SCMs that agree on Level 1 (associational) data but disagree on Level 2 (interventional) questions. Therefore Level 2 distinctions are not in general identifiable from Level 1 data.

**No-go.** For any L1 world $\mathcal W_{L1}$ with latent common cause $C$, there exists an L0 world $\mathcal W_{L0}^\ast$ with edge probabilities matched to the on-policy regime conditionals such that the on-policy observation distribution is *identical*: $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$. The L0/L1 distinction is a Level 2 question (it concerns $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$); on-policy data is Level 1; the CHT forbids distinguishing them.

**Boundary characterization.** Five routes (cf. #causal-insufficiency-detection):
- (a) $\varepsilon$-exploration violates pure on-policy execution → partial detection at scale $O(\varepsilon)$.
- (b) Joint sibling observability under exploration violates short-circuit censoring → strong detection via the pairwise covariance test under #loop-interventional-access.
- (c) Intermediate-state observability at finer grain → very strong detection where available.
- (d) Structural priors positing common causes → prior-quality-dependent.
- (e) Direct intervention on the candidate latent → strongest where available.

**Strengthened consequence.** The covariance test under joint observability (route (b)) becomes the unique broadly-available detection mechanism. This sharpens #loop-interventional-access from "useful machinery" to "structurally required to escape the no-go." The orient cascade's step 4c (causal-sufficiency check) is no longer "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures.

### Instance 2 — L1' Mixture Identifiability from Single-Channel Observations ( #strategic-dynamics-derivation Prop B.7)

**Setting.** Identify the mixture parameters $(\theta_C, p_{j\mid C}, p_{j\mid \neg C})$ of a soft-facilitator L1' DAG using single-channel observations $y_j$ of one child at a time, with $C$ unobservable.

**External theorem.** The Cramér-Rao bound (Cramér 1946, *Mathematical Methods of Statistics*, Princeton University Press): the variance of any unbiased estimator is at least the inverse of the Fisher information matrix; if the Fisher matrix is rank-deficient, the bound is infinite in the null directions and no unbiased estimator achieves finite variance there.

**No-go.** Computing the Fisher information of the mixture model $\mu_j = \theta_C \theta_{j\mid C} + (1-\theta_C)\theta_{j\mid \neg C}$ at truth, the matrix admits the rank-1 factorization $\mathcal{F} = uu^T/(\mu_j(1-\mu_j))$ with $u = (\Delta_j, \theta_C, 1-\theta_C)$ and $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ the separability gap. The two-dimensional null space corresponds to perturbations along the indeterminacy manifold $\{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1-\hat\theta_C) \hat p_{\mid \neg C} = \mu_j\}$ — directions unobservable from a single binary signal. The smallest eigenvalue of the soft-EM update Jacobian is therefore zero; no SA1-preserving update on the joint conditional vector admits a sector parameter $\alpha \gt 0$.

**Boundary characterization.** Three repair routes:
- (i) Augment $C$-observability — instrument secondary signals identifying $C$ per trial. Recovers Prop B.7 globally with the five-way-gating $\alpha_{L1'}$.
- (ii) Joint multi-child observation — when $K \geq 2$ children share $C$ with linearly independent conditional profiles AND are observed jointly under the same $C$-realization, the joint Fisher matrix can reach rank $2K+1$. Strong structural requirement (not satisfied by typical sequential strategy execution).
- (iii) Plan-level fallback — track the marginal $\hat\mu_j$ scalar (which is identifiable; recovers B.1's $\alpha = 1/(n_\mu+1)$) at the cost of losing the per-conditional decomposition, equivalent to L0-on-marginals.

**Strengthened consequence.** *Observability-as-information-augmentation* becomes load-bearing: when the agent can treat $C$ as an observable feature of the environment (e.g., a regime indicator the environment broadcasts — common in software/operational settings: build state, deployment regime, user tier), the problem transforms from refuted to globally derived. This elevates the engineering choice "instrument the latent" from a convenience to a theoretical prerequisite for L1' identifiability.

**Tier.** *Exact* (Cramér-Rao bound is exact for unbiased online estimators).

### Instance 3 — Composite Contraction Certification from Component Data ( #critical-mass-composition, #contraction-template)

**Setting.** Certify $\kappa_c > 0$ (composite contracting in a combined metric) for $N$ sub-agents each verified at its own level (individual sector conditions with parameters $(\alpha_i, R_i)$, individual Tier 1 classifications per `msc/spike-bridge-lemma-contraction.md`, individual modularity per `#directed-separation`), using only component-level data: per-sub-agent trajectories, mismatch observations, update rules — no observation of the coupling topology (sign pattern of cross-agent influence), no common contraction metric chosen across sub-agents, no passivity certificate on the coupling channels, no shared Lyapunov function.

**External theorem.** Common-Lyapunov nonexistence for switched linear systems — Liberzon 2003, *Switching in Systems and Control*, Theorem 2.1; explicit $2 \times 2$ counterexample in Dayawansa & Martin 1999, "A converse Lyapunov theorem for a class of dynamical systems which undergo switching," *IEEE Trans. Automat. Control* 44:751; systematic review in Shorten, Wirth, Mason, Wulff & King 2007, "Stability criteria for switched and hybrid systems," *SIAM Review* 49:545. Complementary anchor: small-gain contrapositive — Jiang, Teel & Praly 1994, "Small-gain theorem for ISS systems and applications," *Math. Control Signals Syst.* 7:95; if interconnection gain is unbounded or not observable from component data, no composite-ISS certificate from that data. The Liberzon/Shorten common-Lyapunov result is the sharper anchor for AAD's setting.

**No-go.** There exist pairs of coupled systems $(\Sigma_1, \Sigma_2)$ and $(\Sigma_1, \Sigma_2')$ with **identical marginal component-level observation distributions** but opposite composite-contraction signs ($\kappa_c > 0$ in the cooperative regime per `#critical-mass-composition` (CM2) with $\gamma < 0$; $\kappa_c < 0$ in the adversarial regime per `#adversarial-destabilization` with $\gamma > 0$ past the destabilization threshold). Concretely, take two symmetric-matched-Tier-1 scalar agents with coupling term $\gamma\mathcal T \cdot \text{sign}(\delta_{\bar i})$. Each sub-agent in isolation sees $\dot\delta_i = -\alpha\delta_i + w_i^{\text{total}}$ with total disturbance bound $\rho + |\gamma|\mathcal T$ — consistent with both $\gamma = +\gamma_0$ (adversarial) and $\gamma = -\gamma_0$ (cooperative) since the cross-term is absorbed into bounded-disturbance regardless of sign. Only observation of the *joint* dynamics (or structural knowledge of the coupling sign) distinguishes them. **The single bit of coupling-sign distinguishing cooperative from adversarial regimes is unidentifiable from component marginals, and that bit is exactly what flips composite persistence.**

**Boundary characterization.** Four structural escapes:

- (a) **Observable coupling topology** via composite-extended `#loop-interventional-access` — interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response, which is a $do(\cdot)$-data distinction between the two coupled constructions.
- (b) **Matched Tier at the composite level** — shared architecture (matched Tier 1, same norm/metric) admits a joint quadratic Lyapunov $V = \sum V_i$, yielding `#critical-mass-composition`'s (CM2) closed form. Under `#contraction-template`'s topology-indexed closure results, this extends to heterogeneous composites via (CM2-M) for matched contraction-metric structure across agents.
- (c) **Passivity / storage-function certificate** on the coupling channel (Willems 1972 *Arch. Ration. Mech. Anal.* 45:321). Adjacent machinery not currently in an AAD segment.
- (d) **Common contraction metric** (Lohmiller & Slotine 1998). Operationalized in `#contraction-template`: composite metric $M_c$ constructed compositionally from sub-agent metrics per topology (parallel / cascade / negative-feedback), with rate $\lambda_c$ from Slotine 2003.

**Strengthened consequence.** The no-go elevates three pieces of AAD machinery from "useful" to "structurally required":

1. `#critical-mass-composition` moves from "closed-form result in a special case" to **the unique broadly-available composition-contraction certificate under the matched-Tier structural escape (b)**; without (CM2) or its contraction-metric generalization (CM2-M) in `#contraction-template`, the weakest-link bound (WL) in `#composition-closure` cannot see coupling sign and so cannot distinguish the two coupled constructions.
2. **Composite-extended `#loop-interventional-access`** becomes the unique coupling-sign identifier under heterogeneous Tier structures — the composite-layer analog of the single-agent interventional-access-escape for Instance 1.
3. `#scope-composite-agent` acquires **load-bearing enabling status**: scope-satisfaction (one of C-i, C-ii, C-iii) is what positions the composite within a regime where one of (a)–(d) can operate. Without scope-satisfaction, the composite might not be a composite, and the escapes have no coherent target.

**Tier.** *Exact* for the symmetric-matched-Tier-1-scalar construction exhibited above. *Robust qualitative* for general heterogeneous composites, inheriting the common-Lyapunov-nonexistence structure from Liberzon / Shorten / Dayawansa-Martin without a closed-form AAD-level counterexample.

## Adjacent Floors (Open Research Directions)

### Causal-IB Extension for Interventional Relevance Variables

The standard Information Bottleneck ( #information-bottleneck) and the four AAD compression operations ( #compression-operations) work with associational relevance variables — $Y$ in a joint distribution with $X$ and $T$. Strategy edges in the regime-indexed interpretation ( #edge-update-causal-validity) want *interventional* relevance for Regime A: "what edge $(i, j)$ predicts under $do(i)$, not under observation of $i$." Standard IB cannot supply this; a causal-IB variant (Wieczorek & Roth 2017 and follow-ups) is the natural framework. The expected floor: under purely associational data, the interventional relevance content is bounded; the gap is recoverable via $do$-data from the loop. Open: formalize the gap as an identifiability floor parallel to Instances 1 and 2.

### Misspecification-Cost Quantification

Structural adaptation ( #structural-adaptation-necessity) names *when* to switch model classes. It does not quantify the *continuous degradation* from a mildly misspecified model under a finite information budget. Adjacent to #observation-ambiguity-modulation's $\kappa \cdot \mathcal A$ bound but not covered by it. The expected floor: under fixed information budget, the degradation rate from misspecification is bounded below by an information-theoretic quantity (likely related to the KL gap between true and assumed model classes). Open.

### Tier-Switching Policy Cost

Approximation tiering ( #approximation-tiering) enumerates AAD's tiered approximations (L0/L1/L1'/L2 in correlation, C1/C2/C3 in convention, Tier 1/2/3 in contraction). The cost of switching tiers — when should the agent move from L0 to L1, or from C1 to C2 — is itself a deliberation-cost problem. Under finite computation budget, the optimal switching policy faces an identifiability floor on its own switching diagnostics. Open.

### Mechanism-Design Impossibility (candidate 4th instance from #strategic-composition)

Under the mechanism-design framing of strategic composition ( #strategic-composition §Discussion), an outside designer may be able to shape sub-agents' objectives $\{O_t^{(i)}\}$ so that the induced strategic equilibrium coincides with a desired joint state. Impossibility results from social-choice theory — **Gibbard-Satterthwaite** 1973-75 (no dominant-strategy non-dictatorial Pareto-efficient voting mechanism for ≥3 alternatives); **Myerson-Satterthwaite** 1983 (no efficient, individually-rational, incentive-compatible bilateral-trade mechanism without subsidies); **Arrow** 1951 (no social welfare function satisfying unrestricted-domain + Pareto-efficient + IIA + non-dictatorial simultaneously) — establish that certain mechanism-design goals are **structurally unachievable** under stated constraints. This matches the meta-pattern shape: setting (composite-design task under specific-constraint regime) → external theorem (social-choice impossibility) → no-go → boundary characterization (relaxation of constraints: Bayes-Nash in place of dominant-strategy; randomized allocations; subsidy injection; strategy-space restriction) → strengthened consequence (the AAD machinery of `#strategic-composition`'s sub-scope α' potential-game conditions becomes a load-bearing target for mechanism design). Candidate fourth instance; would require a dedicated formalization of the AAD-machinery escape route specifically rather than the general social-choice escape. Open.

## Why This Pattern Matters

**Strengthens the case for AAD's foundational machinery.** Each floor identifies a piece of AAD machinery as load-bearing in the strongest possible sense — without it, the corresponding inferential task is *impossible*, not merely *harder*. The loop's interventional access is not just useful; it is the unique broadly-available violation of the on-policy detection no-go. Observability of latents is not just convenient; it is the unique route from refuted-by-Cramér-Rao to globally-derived for L1' transfer.

**Maps the limits of AAD's machinery.** The floors precisely characterize what AAD cannot do without additional capability. This is honest scope-marking — at each floor, the theory states "here is what is impossible; here is what you need to escape the impossibility; here is what AAD supplies (or doesn't supply, as the case may be)."

**Provides a unifying framework for future no-go results.** Adjacent floors (causal-IB extension, misspecification cost, tier-switching cost) are open research directions that would extend the pattern. Each, if formalized, would have the same shape: setting → external theorem → no-go → boundary characterization → strengthened machinery.

**Connects AAD to information-theoretic foundations.** The external theorems (Pearl/Bareinboim hierarchy; Cramér-Rao bound; rate-distortion / IB) are the mature literature AAD inherits. Each instance positions AAD as a domain-specific application of an established theorem — not a re-derivation, but a consequential application that shapes downstream segment structure.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. The segment is a presentational organizing principle — it names a shared shape across separately-derived results, not a theorem in its own right. What is derivative here is the recognition that two independent AAD findings share the pattern (setting → external theorem → no-go → boundary characterization → strengthened consequence); the pattern itself is not derived and has no identification claim of its own.

*Individual instances retain their own, higher, epistemic status.* Instance 1 (on-policy L0 insufficiency detection, via the Causal Hierarchy Theorem) is *exact* for shallow strict-prerequisite cases and *robust qualitative* for general DAG topology, derived in #causal-insufficiency-detection. Instance 2 (L1' under unobservable common cause, via the Cramér-Rao bound on Fisher information) is *exact* under the Fisher rank-1 calculation in #strategic-dynamics-derivation Prop B.7 refutation. Readers citing this segment for a specific no-go should cite the instance's own derivation, not the meta-pattern.

The segment makes one additional claim: that AAD's machinery (loop-interventional access, observability-as-information-augmentation) acquires sharper load-bearing roles when read through the floors that motivate them. This is a *discussion-grade* observation about the theory's architecture — it is visible once the instances are assembled, but is not itself a theorem.

*Whether the pattern is a generative principle* — whether future AAD work will systematically encounter and derive more instances — is a *hypothesis* that the adjacent open floors test.

Max attainable: *discussion-grade* for the meta-pattern (it is a presentational organizing principle, not a derivation). The individual instances retain their own epistemic status as derived above.

## Discussion

**The pattern is asymmetric.** Each floor forbids inference *from* limited data; it does not forbid inference *with* the augmenting capability. The asymmetry is the source of the pattern's positive content — it tells the reader exactly what to instrument, observe, or intervene upon to escape the floor.

**The pattern composes with AAD's scope honesty.** Directed separation ( #directed-separation) classifies architectures by where Section II's exact results apply (Class 1 modular; Class 2 fully merged needs coupled formulation). The identifiability floors are a different kind of scope claim: they specify what the theory's machinery *cannot do* under specific information regimes, with explicit characterization of the regime escapes. Together, the architectural classification and the identifiability floors mark AAD's scope at two levels — what kinds of agents the theory applies to, and what those agents can and cannot infer from given data.

**Complementarity with the separability pattern ( #discussion-separability-pattern).** This segment names the *negative half* of AAD's scope; the companion meta-segment #discussion-separability-pattern names the *positive half* — separable-core / structured-repair / general-open across six ladders (correlation, convention, architecture, contraction, identification, scope). Each identifiability-floor instance here has a positive counterpart there: Instance 1's on-policy detection no-go matches the observable-sibling-covariance structured-repair in the correlation ladder; Instance 2's unobservable-$C$ L1' refutation matches the observable-$C$ / facilitator-monotonicity structured-repair in the same ladder. The two halves together characterize AAD's scope at both extremes — what succeeds and under what machinery, and what structurally cannot succeed without specific information augmentation.

**The pattern is conservative in style.** Each floor invokes a published external theorem (Bareinboim et al. 2022; standard Cramér-Rao bound) rather than deriving a new impossibility result. AAD's contribution is the *application* — recognizing the AAD setting falls within the theorem's scope, characterizing the boundary conditions, and identifying which AAD machinery is the unique broadly-available escape. This style aligns with the broader posture of AAD as an integrating framework that connects established results across control theory, causal inference, and information theory under a common formalism.

## Working Notes

- **Naming convention.** "Identifiability floor" frames the pattern positively: the floor is what the agent cannot go below given limited information, but the boundary characterization tells the agent exactly how to climb above it. An alternative name "no-go theorems" would emphasize the negative form. Recommend retaining "floor" — it captures the asymmetry.

- **Instance 3 as a candidate.** The "L1 augmentation when the augmentation graph is itself causally insufficient" question (recurse the no-go: detect when the L1 augmentation is itself missing common causes) is a candidate Instance 3. Likely reduces to Instance 1 applied at the L1 level — the agent at L1 faces the same on-policy detection no-go for L1 → L2 escalation. Worth formalizing if a third instance emerges that does *not* reduce to the existing two.

- **Is the floor pattern unique to causal/identifiability questions?** The two current instances are both about distinguishing two parameter regimes from data. The pattern may also apply to other impossibility-style results in AAD: the inevitability of structural-adaptation thresholds ( #structural-adaptation-necessity), the cost of representing high-correlation regimes (L2 exponential blowup), the bandwidth limits in shared intent ( #shared-intent). Whether to absorb those into "identifiability floor" or treat them as a separate "structural-cost" pattern is open.

- **Cross-segment integrations.** The meta-pattern surfaces in (at least): #causal-insufficiency-detection (Instance 1); #strategic-dynamics-derivation Prop B.7 (Instance 2); #loop-interventional-access (load-bearing for Instance 1 escape); #strategy-dag (the L0/L1/L1'/L2 hierarchy is the regime ladder Instance 2 lives on). Each of these segments cross-references this one for the unifying frame.
