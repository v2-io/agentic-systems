---
slug: identifiability-floor
type: discussion
status: robust-qualitative
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

**No-go.** For any L1 world $\mathcal{W}_{L1}$ with latent common cause $C$, there exists an L0 world $\mathcal{W}_{L0}^\ast$ with edge probabilities matched to the on-policy regime conditionals such that the on-policy observation distribution is *identical*: $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$. The L0/L1 distinction is a Level 2 question (it concerns $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$); on-policy data is Level 1; the CHT forbids distinguishing them.

**Boundary characterization.** Five routes (cf. #causal-insufficiency-detection):
- (a) ε-exploration violates pure on-policy execution → partial detection at scale $O(\varepsilon)$.
- (b) Joint sibling observability under exploration violates short-circuit censoring → strong detection via the pairwise covariance test under #loop-interventional-access.
- (c) Intermediate-state observability at finer grain → very strong detection where available.
- (d) Structural priors positing common causes → prior-quality-dependent.
- (e) Direct intervention on the candidate latent → strongest where available.

**Strengthened consequence.** The covariance test under joint observability (route (b)) becomes the unique broadly-available detection mechanism. This sharpens #loop-interventional-access from "useful machinery" to "structurally required to escape the no-go." The orient cascade's step 4c (causal-sufficiency check) is no longer "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures.

### Instance 2 — L1' Mixture Identifiability from Single-Channel Observations ( #strategic-dynamics-derivation Prop B.7)

**Setting.** Identify the mixture parameters $(\theta_C, p_{j\mid C}, p_{j\mid \neg C})$ of a soft-facilitator L1' DAG using single-channel observations $y_j$ of one child at a time, with $C$ unobservable.

**External theorem.** The Cramér-Rao bound: the variance of any unbiased estimator is at least the inverse of the Fisher information matrix; if the Fisher matrix is rank-deficient, the bound is infinite in the null directions and no unbiased estimator achieves finite variance there.

**No-go.** Computing the Fisher information of the mixture model $\mu_j = \theta_C \theta_{j\mid C} + (1-\theta_C)\theta_{j\mid \neg C}$ at truth, the matrix admits the rank-1 factorization $\mathcal{F} = uu^T/(\mu_j(1-\mu_j))$ with $u = (\Delta_j, \theta_C, 1-\theta_C)$ and $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ the separability gap. The two-dimensional null space corresponds to perturbations along the indeterminacy manifold $\{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1-\hat\theta_C) \hat p_{\mid \neg C} = \mu_j\}$ — directions unobservable from a single binary signal. The smallest eigenvalue of the soft-EM update Jacobian is therefore zero; no SA1-preserving update on the joint conditional vector admits a sector parameter $\alpha \gt 0$.

**Boundary characterization.** Three repair routes:
- (i) Augment $C$-observability — instrument secondary signals identifying $C$ per trial. Recovers Prop B.7 globally with the five-way-gating $\alpha_{L1'}$.
- (ii) Joint multi-child observation — when $K \geq 2$ children share $C$ with linearly independent conditional profiles AND are observed jointly under the same $C$-realization, the joint Fisher matrix can reach rank $2K+1$. Strong structural requirement (not satisfied by typical sequential strategy execution).
- (iii) Plan-level fallback — track the marginal $\hat\mu_j$ scalar (which is identifiable; recovers B.1's $\alpha = 1/(n_\mu+1)$) at the cost of losing the per-conditional decomposition, equivalent to L0-on-marginals.

**Strengthened consequence.** *Observability-as-information-augmentation* becomes load-bearing: when the agent can treat $C$ as an observable feature of the environment (e.g., a regime indicator the environment broadcasts — common in software/operational settings: build state, deployment regime, user tier), the problem transforms from refuted to globally derived. This elevates the engineering choice "instrument the latent" from a convenience to a theoretical prerequisite for L1' identifiability.

**Tier.** *Exact* (Cramér-Rao bound is exact for unbiased online estimators).

## Adjacent Floors (Open Research Directions)

### Causal-IB Extension for Interventional Relevance Variables

The standard Information Bottleneck ( #information-bottleneck) and the four AAD compression operations ( #compression-operations) work with associational relevance variables — $Y$ in a joint distribution with $X$ and $T$. Strategy edges in the regime-indexed interpretation ( #edge-update-causal-validity) want *interventional* relevance for Regime A: "what edge $(i, j)$ predicts under $do(i)$, not under observation of $i$." Standard IB cannot supply this; a causal-IB variant (Wieczorek & Roth 2017 and follow-ups) is the natural framework. The expected floor: under purely associational data, the interventional relevance content is bounded; the gap is recoverable via $do$-data from the loop. Open: formalize the gap as an identifiability floor parallel to Instances 1 and 2.

### Misspecification-Cost Quantification

Structural adaptation ( #structural-adaptation-necessity) names *when* to switch model classes. It does not quantify the *continuous degradation* from a mildly misspecified model under a finite information budget. Adjacent to #observation-ambiguity-modulation's $\kappa \cdot \mathcal A$ bound but not covered by it. The expected floor: under fixed information budget, the degradation rate from misspecification is bounded below by an information-theoretic quantity (likely related to the KL gap between true and assumed model classes). Open.

### Tier-Switching Policy Cost

Approximation tiering ( #approximation-tiering) enumerates AAD's tiered approximations (L0/L1/L1'/L2 in correlation, C1/C2/C3 in convention, Tier 1/2/3 in contraction). The cost of switching tiers — when should the agent move from L0 to L1, or from C1 to C2 — is itself a deliberation-cost problem. Under finite computation budget, the optimal switching policy faces an identifiability floor on its own switching diagnostics. Open.

## Why This Pattern Matters

**Strengthens the case for AAD's foundational machinery.** Each floor identifies a piece of AAD machinery as load-bearing in the strongest possible sense — without it, the corresponding inferential task is *impossible*, not merely *harder*. The loop's interventional access is not just useful; it is the unique broadly-available violation of the on-policy detection no-go. Observability of latents is not just convenient; it is the unique route from refuted-by-Cramér-Rao to globally-derived for L1' transfer.

**Maps the limits of AAD's machinery.** The floors precisely characterize what AAD cannot do without additional capability. This is honest scope-marking — at each floor, the theory states "here is what is impossible; here is what you need to escape the impossibility; here is what AAD supplies (or doesn't supply, as the case may be)."

**Provides a unifying framework for future no-go results.** Adjacent floors (causal-IB extension, misspecification cost, tier-switching cost) are open research directions that would extend the pattern. Each, if formalized, would have the same shape: setting → external theorem → no-go → boundary characterization → strengthened machinery.

**Connects AAD to information-theoretic foundations.** The external theorems (Pearl/Bareinboim hierarchy; Cramér-Rao bound; rate-distortion / IB) are the mature literature AAD inherits. Each instance positions AAD as a domain-specific application of an established theorem — not a re-derivation, but a consequential application that shapes downstream segment structure.

## Epistemic Status

*Robust qualitative.* The meta-pattern itself is a *discussion-grade* observation: two derived instances exist (Instance 1 at *exact* for shallow cases / *robust qualitative* for general; Instance 2 at *exact*); each is a legitimate no-go via external theorem. Whether the pattern is a *generative principle* — whether future AAD work will systematically encounter and derive more instances — is a *hypothesis* that the adjacent open floors test.

The strongest epistemic claim this segment makes is the meta-observation that AAD's machinery (loop-interventional access, observability-as-augmentation) acquires sharper load-bearing roles when read through the floors that motivate them. This is *robust qualitative*: the claim is structurally clear once the instances are stated, but is not itself a theorem.

Max attainable: *robust qualitative* for the meta-pattern (it is a presentational organizing principle, not a derivation). The individual instances retain their own epistemic status (Instance 1: *exact* / *robust qualitative*; Instance 2: *exact*).

## Discussion

**The pattern is asymmetric.** Each floor forbids inference *from* limited data; it does not forbid inference *with* the augmenting capability. The asymmetry is the source of the pattern's positive content — it tells the reader exactly what to instrument, observe, or intervene upon to escape the floor.

**The pattern composes with AAD's scope honesty.** Directed separation ( #directed-separation) classifies architectures by where Section II's exact results apply (Class 1 modular; Class 2 fully merged needs coupled formulation). The identifiability floors are a different kind of scope claim: they specify what the theory's machinery *cannot do* under specific information regimes, with explicit characterization of the regime escapes. Together, the architectural classification and the identifiability floors mark AAD's scope at two levels — what kinds of agents the theory applies to, and what those agents can and cannot infer from given data.

**The pattern is conservative in style.** Each floor invokes a published external theorem (Bareinboim et al. 2022; standard Cramér-Rao bound) rather than deriving a new impossibility result. AAD's contribution is the *application* — recognizing the AAD setting falls within the theorem's scope, characterizing the boundary conditions, and identifying which AAD machinery is the unique broadly-available escape. This style aligns with the broader posture of AAD as an integrating framework that connects established results across control theory, causal inference, and information theory under a common formalism.

## Working Notes

- **Naming convention.** "Identifiability floor" frames the pattern positively: the floor is what the agent cannot go below given limited information, but the boundary characterization tells the agent exactly how to climb above it. An alternative name "no-go theorems" would emphasize the negative form. Recommend retaining "floor" — it captures the asymmetry.

- **Instance 3 as a candidate.** The "L1 augmentation when the augmentation graph is itself causally insufficient" question (recurse the no-go: detect when the L1 augmentation is itself missing common causes) is a candidate Instance 3. Likely reduces to Instance 1 applied at the L1 level — the agent at L1 faces the same on-policy detection no-go for L1 → L2 escalation. Worth formalizing if a third instance emerges that does *not* reduce to the existing two.

- **Is the floor pattern unique to causal/identifiability questions?** The two current instances are both about distinguishing two parameter regimes from data. The pattern may also apply to other impossibility-style results in AAD: the inevitability of structural-adaptation thresholds ( #structural-adaptation-necessity), the cost of representing high-correlation regimes (L2 exponential blowup), the bandwidth limits in shared intent ( #shared-intent). Whether to absorb those into "identifiability floor" or treat them as a separate "structural-cost" pattern is open.

- **Cross-segment integrations.** The meta-pattern surfaces in (at least): #causal-insufficiency-detection (Instance 1); #strategic-dynamics-derivation Prop B.7 (Instance 2); #loop-interventional-access (load-bearing for Instance 1 escape); #strategy-dag (the L0/L1/L1'/L2 hierarchy is the regime ladder Instance 2 lives on). Each of these segments cross-references this one for the unifying frame.
