# Cluster Reference: Scope Honesty via No-Gos (Tiered Approximation)

**Overview:** Embeds external mathematical impossibility theorems (no-gos) into the agent's architecture as internal regime-switching boundaries, creating explicit, bounded approximation tiers.

---

## Canonical Source Segments

### Source: `disc-approximation-tiering.md`

```yaml
---
slug: disc-approximation-tiering
type: discussion
status: robust-qualitative
depends:
  - def-strategy-dag
  - def-value-object
  - form-composition-closure
stage: draft
---
```


# Discussion: Approximation Tiering

AAT uses a recurring meta-pattern for handling intractability: when a problem admits no tractable exact treatment in general, introduce a tiered hierarchy of approximations with proved monotonicity between tiers and a diagnostic for ascending when needed. Three such hierarchies exist in the theory — the Correlation Hierarchy (L0/L1/L2) in #def-strategy-dag, the Convention Hierarchy (C1/C2/C3) in #def-value-object, and the Tier 1/2/3 contraction taxonomy in #form-composition-closure. This segment articulates the pattern explicitly, identifies what makes a successful approximation tiering, and notes where other scattered simplifications might fit the same shape.

## Formal Expression

*[Discussion (approximation-tiering)]*

A successful approximation tiering has four components:

**(AT1) A parameter indexing tractability.** Some quantity (correlation modeling depth; continuation-policy fidelity; operator regularity) that admits a natural ordering from least to most demanding computation.

**(AT2) Monotonicity.** A proved ordering of the results produced at each level — each higher tier dominates the lower in the direction of interest (calibration accuracy, diagnostic force, guarantee strength).

**(AT3) Graceful degradation.** Lower tiers produce usable (not vacuous) results, with the specific form of the degradation characterized. An agent stuck at the lowest tier knows what it is missing, not just that it is incomplete.

**(AT4) Ascension diagnostic.** A signal the agent can detect at a lower tier that indicates escalation to a higher tier is warranted. Without this, the tiering is descriptive but not operational.

### The three AAT tierings

| Hierarchy | Parameter | Monotonicity | Lowest tier | Highest tier | Ascension diagnostic |
|---|---|---|---|---|---|
| **Correlation** ( #def-strategy-dag) | Modeling depth of inter-edge dependence | L0 is conservative; L1 is unbiased on augmented graph; L2 is the full joint | L0 (independence model, $O(\lvert V\rvert + \lvert E\rvert)$ propagation) | L2 (full joint, $O(2^m)$ in general) | Sibling-edge covariance after credence convergence ( #der-causal-insufficiency-detection) |
| **Convention** ( #def-value-object) | Continuation-policy fidelity | $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ (proved monotonicity) | C1 (one-step improvement) | C3 (Bellman optimal) | Persistent $\delta_{\text{sat}} \gt 0$ under C1 that C2 replanning may resolve |
| **Contraction** ( #form-composition-closure) | Operator regularity for bridge lemma | Tier 1 $\supset$ Tier 2 $\supset$ Tier 3 in terms of proved contraction strength | Tier 3 (domain-specific verification required) | Tier 1 (contraction proved for full class) | Structural test: is the correction strongly monotone, locally convex, or neither? |

Each row satisfies (AT1)–(AT4) fully — these are mature tierings in the theory. Each tiering is independently motivated by a different source of intractability, and each has its own ascension mechanism. Their structural similarity is not designed-in; it is the consequence of facing three separate intractable problems with the same modeling strategy.

### Candidate future tierings

Several other scattered simplifications in the theory have the right shape to become tierings but are not currently organized that way:

- **Scalar vs. per-dimension tempo** (around #def-adaptive-tempo, #result-per-dimension-persistence). Tier 0 (scalar isotropic), Tier 1 (per-dimension), Tier 2 (full tensor with off-diagonal coupling). Monotonicity: scalar overestimates margin, per-dimension is exact for diagonal-gain systems, full tensor handles off-diagonal gain coupling. Ascension diagnostic: gain variance across dimensions.
- **AND/OR parameterization** ( #scope-and-or). Tier 0 (AND/OR, $O(k)$ parameters per node), Tier 1 (weighted/threshold, $O(k)$ additional parameters), Tier 2 (full CPT, $O(2^k)$ parameters). Monotonicity: expressiveness. Ascension diagnostic: systematic miscalibration at AND/OR nodes that survives L1 augmentation.
- **Identifiability regimes** ( #scope-edge-update-causal-validity). Regime A/B/C is already a tiering of causal identification quality, with $\iota_{ij}$ as the indexing parameter. Monotonicity: interventional $\succeq$ partial $\succeq$ observational. Ascension diagnostic: available intervention opportunities in the domain.

Promoting these to named tierings with explicit (AT1)–(AT4) structure would make AAT's scope parameterization more uniform. This is not pursued here — it is noted as a direction for editorial consolidation.

## Epistemic Status

*Robust-qualitative.* Max attainable: *robust-qualitative*. The meta-pattern is an editorial observation: three existing hierarchies in the theory share the same four-component structure, and the shared structure is worth naming because it makes the theory's scope-parameterization move visible rather than implicit. The pattern itself is not a theorem — there is no result that says "every intractable AAT problem admits a (AT1)–(AT4) tiering." The candidate future tierings are conjectures about where the pattern could be extended; each would require its own monotonicity proof and ascension diagnostic.

The three existing tierings are individually grounded: the L0→L1 monotonicity holds under the CMC theorem and augmentation construction; the C1→C2→C3 monotonicity is proved in #def-value-object; the Tier 1/2/3 taxonomy is grounded in operator theory (strong monotonicity, local convexity, arbitrary).

## Discussion

**Why this matters.** AAT's results are often presented as "exact under assumption X." A reader can misread this as "the theory works when X holds and breaks otherwise." The tiering pattern reveals a different structure: when X fails, a named lower tier takes over with a characterized weaker result, and the theory provides a diagnostic for when to escalate to reinstating X by structural repair. This is graceful degradation — a property that a theory wanting to apply across a range of agents and domains needs, and that AAT achieves in three places independently.

Reading AAT through the tiering lens: the theory's "exact" core is what it guarantees at the highest tier of each hierarchy. Its "conditional" periphery is where specific tiers are in force. The claim is not that agents should always operate at the highest tier — that would often be intractable — but that the theory tells the agent which tier it is in and how to get to a higher one when the binding constraint changes.

**Connection to #disc-independence-audit.** The two meta-segments are complementary. #disc-independence-audit enumerates the independence assumptions whose failure drops a result from exact to conditional. This segment enumerates the tierings that provide the structured *recovery* from those drops. Together they characterize AAT's scope parameterization: the independence audit says where the boundaries are; the tiering pattern says how to navigate within them.

**What a full tiering promotion would look like.** If the scattered simplifications listed above were promoted to named tierings, the theory's scope-parameterization would be dramatically more uniform: every conditional result would come with its own tiering and ascension diagnostic. This is aspirational. The three existing tierings took substantial segment-work to formalize (a full Appendix derivation for the CMC, a monotonicity proof for the convention hierarchy, a spike for the incremental sector bound). Extending the pattern to five or six hierarchies would be correspondingly substantial.

**The pattern is not unique to AAT.** Approximation tiering is a common move in applied mathematics — numerical methods (low-order vs. high-order integrators with error bounds), information theory (typical vs. exact coding with rate-distortion monotonicity), statistical inference (maximum-likelihood vs. Bayesian vs. nonparametric). AAT's contribution is not the tiering pattern itself but its deployment across the specific intractable problems that adaptive-agent theory faces.

## Working Notes

- **Formal characterization of the tiering pattern.** Is there a mathematical structure that unifies approximation tiering across domains? Candidates: lattices of model classes ordered by inclusion, rate-distortion curves with explicit corners, hierarchies of Galerkin approximations. None of these is an exact match; the AAT tierings are closer to "ordered families of sufficient conditions" than to any standard mathematical hierarchy. Worth investigating whether a cleaner abstract pattern exists.
- **Interaction between tierings.** An agent operating at L1 correlation, C2 convention, and Tier 2 contraction is in a specific combined regime. The cross-hierarchy interactions are not worked out — is there cross-hierarchy monotonicity? (E.g., does L1 change anything about the convention hierarchy's guarantees?) Each tiering is independently-grounded but the joint structure is not yet mapped.
- **Diagnostic costs.** Each ascension diagnostic has a cost: detecting sibling covariance requires observing convergence; detecting C1-inadequacy requires comparing replanning values; detecting Tier 1 violations requires verifying strong monotonicity. A unified treatment of "when is the diagnostic itself worth running?" would connect this segment to #der-deliberation-cost and the allocation analysis in #disc-exploit-explore-deliberate.


---

### Source: `disc-identifiability-floor.md`

```yaml
---
slug: disc-identifiability-floor
type: discussion
status: discussion-grade
depends:
  - der-causal-insufficiency-detection
  - deriv-edge-credence-dynamics
  - der-causal-hierarchy-requirement
  - der-loop-interventional-access
stage: draft
---
```


# Discussion: The Identifiability Floor — A Class of Structural No-Go Results

AAT has derived a class of structural impossibility results — *floors below which* identification or detection is impossible from limited information. Each floor arises by applying an external information-theoretic theorem (the Pearl/Bareinboim causal hierarchy; the Cramér-Rao bound on Fisher information) to a specific AAT setting. The floors are negative results in form but positive in consequence: they precisely characterize what additional structure (loop-interventional access, multi-channel observability, observable latents) is required to escape the floor, and thereby strengthen the load-bearing role of the AAT machinery that supplies it.

This segment names the meta-pattern, collects the current instances, and identifies adjacent floors that are open research directions.

## The Pattern

Each instance of the identifiability floor has the form:

1. **Setting.** An AAT inferential task — detect a structural property, identify a parameter, distinguish two model classes — under a specific information regime (purely observational data, single observation channel, observation of marginals only, etc.).
2. **External theorem.** An information-theoretic limit independent of AAT: the causal hierarchy theorem (Bareinboim, Correa, Ibeling & Icard 2022) for distinguishing observational and interventional content; the Cramér-Rao bound for unbiased estimation under finite Fisher information.
3. **No-go.** The external theorem is invoked to prove that the inferential task is impossible under the regime: no statistic, no Bayesian comparison, no online estimator can succeed using only the available information.
4. **Boundary characterization.** The conditions under which the floor's regime fails — i.e., the agent has *more* information than the regime allows — admit (partial) identification. Each boundary route maps onto specific AAT machinery already required by the theory.
5. **Strengthened consequence.** The floor strengthens the load-bearing role of whichever AAT machinery is the unique broadly-available violation of the regime. Often this elevates a piece of machinery from "useful" to "structurally required by the theory."

The pattern is *not* a negative posture. AAT does not say "many things are impossible." It says: "here is precisely what cannot be inferred from limited data; here is exactly which additional capability is required to recover identification; the AAT machinery that supplies that capability is therefore load-bearing in the strongest possible sense — without it, the no-go forbids the inference entirely."

## Current Instances

### Instance 1 — On-Policy L0 Insufficiency Detection ( #der-causal-insufficiency-detection)

**Setting.** Detect whether an L0 strategy DAG is causally insufficient (a latent common cause is acting on multiple sibling action propositions) using only the agent's on-policy observation history under sequential short-circuit AND/OR execution.

**External theorem.** Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem: there exist SCMs that agree on Level 1 (associational) data but disagree on Level 2 (interventional) questions. Therefore Level 2 distinctions are not in general identifiable from Level 1 data.

**No-go.** For any L1 world $\mathcal W_{L1}$ with latent common cause $C$, there exists an L0 world $\mathcal W_{L0}^\ast$ with edge probabilities matched to the on-policy regime conditionals such that the on-policy observation distribution is *identical*: $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$. The L0/L1 distinction is a Level 2 question (it concerns $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$); on-policy data is Level 1; the CHT forbids distinguishing them.

**Boundary characterization.** Five routes (cf. #der-causal-insufficiency-detection):
- (a) $\varepsilon$-exploration violates pure on-policy execution → partial detection at scale $O(\varepsilon)$.
- (b) Joint sibling observability under exploration violates short-circuit censoring → strong detection via the pairwise covariance test under #der-loop-interventional-access.
- (c) Intermediate-state observability at finer grain → very strong detection where available.
- (d) Structural priors positing common causes → prior-quality-dependent.
- (e) Direct intervention on the candidate latent → strongest where available.

**Strengthened consequence.** The covariance test under joint observability (route (b)) becomes the unique broadly-available detection mechanism. This sharpens #der-loop-interventional-access from "useful machinery" to "structurally required to escape the no-go." The orient cascade's step 4c (causal-sufficiency check) is no longer "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures.

### Instance 2 — L1' Mixture Identifiability from Single-Channel Observations ( #deriv-edge-credence-dynamics Prop B.7)

**Setting.** Identify the mixture parameters $(\theta_C, p_{j\mid C}, p_{j\mid \neg C})$ of a soft-facilitator L1' DAG using single-channel observations $y_j$ of one child at a time, with $C$ unobservable.

**External theorem.** The Cramér-Rao bound (Cramér 1946, *Mathematical Methods of Statistics*, Princeton University Press): the variance of any unbiased estimator is at least the inverse of the Fisher information matrix; if the Fisher matrix is rank-deficient, the bound is infinite in the null directions and no unbiased estimator achieves finite variance there.

**No-go.** Computing the Fisher information of the mixture model $\mu_j = \theta_C \theta_{j\mid C} + (1-\theta_C)\theta_{j\mid \neg C}$ at truth, the matrix admits the rank-1 factorization $\mathcal{F} = uu^T/(\mu_j(1-\mu_j))$ with $u = (\Delta_j, \theta_C, 1-\theta_C)$ and $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ the separability gap. The two-dimensional null space corresponds to perturbations along the indeterminacy manifold $\{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1-\hat\theta_C) \hat p_{\mid \neg C} = \mu_j\}$ — directions unobservable from a single binary signal. The smallest eigenvalue of the soft-EM update Jacobian is therefore zero; no SA1-preserving update on the joint conditional vector admits a sector parameter $\alpha \gt 0$.

**Boundary characterization.** Three repair routes:
- (i) Augment $C$-observability — instrument secondary signals identifying $C$ per trial. Recovers Prop B.7 globally with the five-way-gating $\alpha_{L1'}$.
- (ii) Joint multi-child observation — when $K \geq 2$ children share $C$ with linearly independent conditional profiles AND are observed jointly under the same $C$-realization, the joint Fisher matrix can reach rank $2K+1$. Strong structural requirement (not satisfied by typical sequential strategy execution).
- (iii) Plan-level fallback — track the marginal $\hat\mu_j$ scalar (which is identifiable; recovers B.1's $\alpha = 1/(n_\mu+1)$) at the cost of losing the per-conditional decomposition, equivalent to L0-on-marginals.

**Strengthened consequence.** *Observability-as-information-augmentation* becomes load-bearing: when the agent can treat $C$ as an observable feature of the environment (e.g., a regime indicator the environment broadcasts — common in software/operational settings: build state, deployment regime, user tier), the problem transforms from refuted to globally derived. This elevates the engineering choice "instrument the latent" from a convenience to a theoretical prerequisite for L1' identifiability.

**Tier.** *Exact* (Cramér-Rao bound is exact for unbiased online estimators).

### Instance 3 — Composite Contraction Certification from Component Data ( #deriv-critical-mass-composition, #result-contraction-template)

**Setting.** Certify $\kappa_c \gt 0$ (composite contracting in a combined metric) for $N$ sub-agents each verified at its own level (individual sector conditions with parameters $(\alpha_i, R_i)$, individual Tier 1 classifications per `spikes/spike-bridge-lemma-contraction.md`, individual modularity per `#der-directed-separation`), using only component-level data: per-sub-agent trajectories, mismatch observations, update rules — no observation of the coupling topology (sign pattern of cross-agent influence), no common contraction metric chosen across sub-agents, no passivity certificate on the coupling channels, no shared Lyapunov function.

**External theorem.** Common-Lyapunov nonexistence for switched linear systems — Liberzon 2003, *Switching in Systems and Control*, Theorem 2.1; explicit $2 \times 2$ counterexample in Dayawansa & Martin 1999, "A converse Lyapunov theorem for a class of dynamical systems which undergo switching," *IEEE Trans. Automat. Control* 44:751; systematic review in Shorten, Wirth, Mason, Wulff & King 2007, "Stability criteria for switched and hybrid systems," *SIAM Review* 49:545. Complementary anchor: small-gain contrapositive — Jiang, Teel & Praly 1994, "Small-gain theorem for ISS systems and applications," *Math. Control Signals Syst.* 7:95; if interconnection gain is unbounded or not observable from component data, no composite-ISS certificate from that data. The Liberzon/Shorten common-Lyapunov result is the sharper anchor for AAT's setting.

**No-go.** There exist pairs of coupled systems $(\Sigma_1, \Sigma_2)$ and $(\Sigma_1, \Sigma_2')$ with **identical marginal component-level observation distributions** but opposite composite-contraction signs ($\kappa_c \gt 0$ in the cooperative regime per `#deriv-critical-mass-composition` (CM2) with $\gamma \lt 0$; $\kappa_c \lt 0$ in the adversarial regime per `#der-adversarial-destabilization` with $\gamma \gt 0$ past the destabilization threshold). Concretely, take two symmetric-matched-Tier-1 scalar agents with coupling term $\gamma\mathcal T \cdot \text{sign}(\delta_{\bar i})$. Each sub-agent in isolation sees $\dot\delta_i = -\alpha\delta_i + w_i^{\text{total}}$ with total disturbance bound $\rho + \lvert\gamma\rvert\mathcal T$ — consistent with both $\gamma = +\gamma_0$ (adversarial) and $\gamma = -\gamma_0$ (cooperative) since the cross-term is absorbed into bounded-disturbance regardless of sign. Only observation of the *joint* dynamics (or structural knowledge of the coupling sign) distinguishes them. **The single bit of coupling-sign distinguishing cooperative from adversarial regimes is unidentifiable from component marginals, and that bit is exactly what flips composite persistence.**

**Boundary characterization.** Four structural escapes:

- (a) **Observable coupling topology** via composite-extended `#der-loop-interventional-access` — interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response, which is a $do(\cdot)$-data distinction between the two coupled constructions.
- (b) **Matched Tier at the composite level** — shared architecture (matched Tier 1, same norm/metric) admits a joint quadratic Lyapunov $V = \sum V_i$, yielding `#deriv-critical-mass-composition`'s (CM2) closed form. Under `#result-contraction-template`'s topology-indexed closure results, this extends to heterogeneous composites via (CM2-M) for matched contraction-metric structure across agents.
- (c) **Passivity / storage-function certificate** on the coupling channel (Willems 1972 *Arch. Ration. Mech. Anal.* 45:321). Adjacent machinery not currently in an AAT segment.
- (d) **Common contraction metric** (Lohmiller & Slotine 1998). Operationalized in `#result-contraction-template`: composite metric $M_c$ constructed compositionally from sub-agent metrics per topology (parallel / cascade / negative-feedback), with rate $\lambda_c$ from Slotine 2003.

**Strengthened consequence.** The no-go elevates three pieces of AAT machinery from "useful" to "structurally required":

1. `#deriv-critical-mass-composition` moves from "closed-form result in a special case" to **the unique broadly-available composition-contraction certificate under the matched-Tier structural escape (b)**; without (CM2) or its contraction-metric generalization (CM2-M) in `#result-contraction-template`, the weakest-link bound (WL) in `#form-composition-closure` cannot see coupling sign and so cannot distinguish the two coupled constructions.
2. **Composite-extended `#der-loop-interventional-access`** becomes the unique coupling-sign identifier under heterogeneous Tier structures — the composite-layer analog of the single-agent interventional-access-escape for Instance 1.
3. `#scope-composite-agent` acquires **load-bearing enabling status**: scope-satisfaction (one of C-i, C-ii, C-iii) is what positions the composite within a regime where one of (a)–(d) can operate. Without scope-satisfaction, the composite might not be a composite, and the escapes have no coherent target.

**Tier.** *Exact* for the symmetric-matched-Tier-1-scalar construction exhibited above. *Robust qualitative* for general heterogeneous composites, inheriting the common-Lyapunov-nonexistence structure from Liberzon / Shorten / Dayawansa-Martin without a closed-form AAT-level counterexample.

### Instance 4 — Universal Information-to-Distance Constant under Non-(PI) Norms ( #deriv-observation-ambiguity-bias-bound )

> [!warning]
> **KNOWN-DEFECTIVE — TODO: FIXME. Do not rely on this as a floor instance; it contradicts its own cited source and this segment's own floor test.** The cited source `#deriv-observation-ambiguity-bias-bound` states *in canon* that this no-go "does not match the five-element test for a floor instance … a *single* escape … the honest position: this no-go is a **downstream theorem of the (PI) commitment, not a new floor instance**." The "Boundary characterization" below is indeed a *single* escape, which fails this segment's own ≥2-distinct-escapes criterion; and the Sylvester-mechanism Discussion taxonomizes only three floors (rank-collapse {I1, I2} + composition I3), silently omitting this one, while the Findings Brief still counts "four." An independent recheck (`spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`) finds this ordinal conflated two objects: *this* one (a category error — a downstream (PI) theorem, **not** a floor) and a genuine floor at the architecturally-distinct / behaviorally-identical layer (the same object as the rho Regime-C confound and CL-2's reserved refinement). Resolving the slot — relabeling this entry and installing the genuine floor — is a Joseph-reserved disposition, gated on an independent-verify of the recheck's Object-B construction; deliberately **not** done here.

**Setting.** Derive a universal constant $C$ that bounds the parameter-space displacement $\lVert \Delta M_{\text{bias}} \rVert$ caused by observation ambiguity, scaling predictably with the mutual information $I(G; \Omega \mid e, M)$.

**External theorem.** The Cramér-Rao lower bound, or equivalent metric equivalences linking Kullback-Leibler divergence to local distance metrics.

**No-go.** Without a canonical metric on the model space $\mathcal{M}$, no universal information-to-distance constant exists. If the parameter space uses an arbitrary Euclidean norm, the relationship between KL divergence (an information-theoretic quantity) and parameter displacement is unbounded and coordinate-dependent. An explicit counterexample exists in heteroscedastic-normal families (see `#deriv-observation-ambiguity-bias-bound`, Attempt E) where $C$ can be made arbitrarily large by reparameterization.

**Boundary characterization.** The unique escape is to adopt the Parameterization Invariance (PI) axiom. Under (PI), Čencov's theorem forces the geometry to be the Fisher-Rao metric. In this canonical geometry, the relationship between mutual information and parameter displacement is universally bounded (e.g., $C_{FR} = \sqrt{2}$ in the small-information regime).

**Strengthened consequence.** This elevates the (PI) axiom from a "nice-to-have" geometric property to a **load-bearing requirement** for the Class 3 (Coupled) bias bound in `#result-section-ii-survival` and `#scope-observation-ambiguity-modulation`. Without (PI), the bias bound is merely an order-of-magnitude heuristic; with (PI), it is a rigorous theorem.

**Tier.** *Exact (counter-example-grade).* The non-existence of a universal $C$ in arbitrary Euclidean norms is proven by explicit construction.

## Adjacent Floors (Open Research Directions)

### Causal-IB Extension for Interventional Relevance Variables

The standard Information Bottleneck ( #form-information-bottleneck) and the four AAT compression operations ( #disc-compression-operations) work with associational relevance variables — $Y$ in a joint distribution with $X$ and $T$. Strategy edges in the regime-indexed interpretation ( #scope-edge-update-causal-validity) want *interventional* relevance for Regime A: "what edge $(i, j)$ predicts under $do(i)$, not under observation of $i$." Standard IB cannot supply this; a causal-IB variant (Wieczorek & Roth 2017 and follow-ups) is the natural framework. The expected floor: under purely associational data, the interventional relevance content is bounded; the gap is recoverable via $do$-data from the loop. Open: formalize the gap as an identifiability floor parallel to Instances 1 and 2.

### Misspecification-Cost Quantification

Structural adaptation ( #result-structural-adaptation-necessity) names *when* to switch model classes. It does not quantify the *continuous degradation* from a mildly misspecified model under a finite information budget. Adjacent to #scope-observation-ambiguity-modulation's $\kappa \cdot \mathcal A$ bound but not covered by it. The expected floor: under fixed information budget, the degradation rate from misspecification is bounded below by an information-theoretic quantity (likely related to the KL gap between true and assumed model classes). Open.

### Tier-Switching Policy Cost

Approximation tiering ( #disc-approximation-tiering) enumerates AAT's tiered approximations (L0/L1/L1'/L2 in correlation, C1/C2/C3 in convention, Tier 1/2/3 in contraction). The cost of switching tiers — when should the agent move from L0 to L1, or from C1 to C2 — is itself a deliberation-cost problem. Under finite computation budget, the optimal switching policy faces an identifiability floor on its own switching diagnostics. Open.

### Mechanism-Design Impossibility (candidate 4th instance from #deriv-strategic-composition)

Under the mechanism-design framing of strategic composition ( #deriv-strategic-composition §Discussion), an outside designer may be able to shape sub-agents' objectives $\{O_t^{(i)}\}$ so that the induced strategic equilibrium coincides with a desired joint state. Impossibility results from social-choice theory — **Gibbard-Satterthwaite** 1973-75 (no dominant-strategy non-dictatorial Pareto-efficient voting mechanism for ≥3 alternatives); **Myerson-Satterthwaite** 1983 (no efficient, individually-rational, incentive-compatible bilateral-trade mechanism without subsidies); **Arrow** 1951 (no social welfare function satisfying unrestricted-domain + Pareto-efficient + IIA + non-dictatorial simultaneously) — establish that certain mechanism-design goals are **structurally unachievable** under stated constraints. This matches the meta-pattern shape: setting (composite-design task under specific-constraint regime) → external theorem (social-choice impossibility) → no-go → boundary characterization (relaxation of constraints: Bayes-Nash in place of dominant-strategy; randomized allocations; subsidy injection; strategy-space restriction) → strengthened consequence (the AAT machinery of `#deriv-strategic-composition`'s sub-scope $\alpha'$ potential-game conditions becomes a load-bearing target for mechanism design). Candidate fourth instance; would require a dedicated formalization of the AAT-machinery escape route specifically rather than the general social-choice escape. Open.

## Why This Pattern Matters

**Strengthens the case for AAT's foundational machinery.** Each floor identifies a piece of AAT machinery as load-bearing in the strongest possible sense — without it, the corresponding inferential task is *impossible*, not merely *harder*. The loop's interventional access is not just useful; it is the unique broadly-available violation of the on-policy detection no-go. Observability of latents is not just convenient; it is the unique route from refuted-by-Cramér-Rao to globally-derived for L1' transfer.

**Maps the limits of AAT's machinery.** The floors precisely characterize what AAT cannot do without additional capability. This is honest scope-marking — at each floor, the theory states "here is what is impossible; here is what you need to escape the impossibility; here is what AAT supplies (or doesn't supply, as the case may be)."

**Provides a unifying framework for future no-go results.** Adjacent floors (causal-IB extension, misspecification cost, tier-switching cost) are open research directions that would extend the pattern. Each, if formalized, would have the same shape: setting → external theorem → no-go → boundary characterization → strengthened machinery.

**Connects AAT to information-theoretic foundations.** The external theorems (Pearl/Bareinboim hierarchy; Cramér-Rao bound; rate-distortion / IB) are the mature literature AAT inherits. Each instance positions AAT as a domain-specific application of an established theorem — not a re-derivation, but a consequential application that shapes downstream segment structure.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. The segment is a presentational organizing principle — it names a shared shape across separately-derived results, not a theorem in its own right. What is derivative here is the recognition that two independent AAT findings share the pattern (setting → external theorem → no-go → boundary characterization → strengthened consequence); the pattern itself is not derived and has no identification claim of its own.

*Individual instances retain their own, higher, epistemic status.* Instance 1 (on-policy L0 insufficiency detection, via the Causal Hierarchy Theorem) is *exact* for shallow strict-prerequisite cases and *robust qualitative* for general DAG topology, derived in #der-causal-insufficiency-detection. Instance 2 (L1' under unobservable common cause, via the Cramér-Rao bound on Fisher information) is *exact* under the Fisher rank-1 calculation in #deriv-edge-credence-dynamics Prop B.7 refutation. Readers citing this segment for a specific no-go should cite the instance's own derivation, not the meta-pattern.

The segment makes one additional claim: that AAT's machinery (loop-interventional access, observability-as-information-augmentation) acquires sharper load-bearing roles when read through the floors that motivate them. This is a *discussion-grade* observation about the theory's architecture — it is visible once the instances are assembled, but is not itself a theorem.

*Whether the pattern is a generative principle* — whether future AAT work will systematically encounter and derive more instances — is a *hypothesis* that the adjacent open floors test.

Max attainable: *discussion-grade* for the meta-pattern (it is a presentational organizing principle, not a derivation). The individual instances retain their own epistemic status as derived above.

## Discussion

**The pattern is asymmetric.** Each floor forbids inference *from* limited data; it does not forbid inference *with* the augmenting capability. The asymmetry is the source of the pattern's positive content — it tells the reader exactly what to instrument, observe, or intervene upon to escape the floor.

**The asymmetry has a named mechanism for the rank-collapse instances: Sylvester's law of inertia.** For the instances whose floor is a rank-deficiency of an information operator — Instance 2 (Fisher rank-1 under an unobservable common cause) cleanly, and Instance 1 (the causal-parameter block carries no score under a purely observational regime) structurally — the reason no change of coordinates escapes the floor is one theorem. The agent's only representational freedom is the choice of coordinate / metric, and every such change acts on the information operator by *congruence* ($\mathcal G \mapsto S^\top \mathcal G S$ for invertible $S$ — the standard Fisher-information reparameterization law). Sylvester's law of inertia states that congruence preserves inertia: the number of zero eigenvalues is invariant under every invertible reparameterization. So a rank-deficient information operator is rank-deficient in *every* coordinate; the floor is the boundary of the positive-definite cone, and the entire reparameterization freedom is a congruence orbit that cannot cross that boundary. This is why the only escape is *rank-augmentation* — adding a genuinely new score component (interventional data via the loop, a side channel, a witness), which is not a coordinate change — and never reweighting. The per-instance "no reparameterization removes the degeneracy" computations (the Fisher rank-1 calculation in #deriv-edge-credence-dynamics Prop B.7; the on-policy no-detection argument in #der-causal-insufficiency-detection) are special cases of this single law. **The mechanism is specific to the rank-collapse subclass, not to all floors.** Instance 3 (composite contraction certification) is a *different* obstruction: composition is a non-invertible projection, not a congruence, so its no-go is a Schur-complement / memory-kernel statement (the certificate's metric survives projection but its dynamic guarantee does not), not an inertia statement. That the floors do not share one mechanism — Sylvester for rank-collapse, a projection/closure obstruction for composition — is itself load-bearing: it is why the floor pattern is a presentational family rather than a single theorem.

**The pattern composes with AAT's scope honesty.** Directed separation ( #der-directed-separation) classifies architectures by where Section II's exact results apply (Class 1 Separated; Class 3 Coupled needs coupled formulation). The identifiability floors are a different kind of scope claim: they specify what the theory's machinery *cannot do* under specific information regimes, with explicit characterization of the regime escapes. Together, the architectural classification and the identifiability floors mark AAT's scope at two levels — what kinds of agents the theory applies to, and what those agents can and cannot infer from given data.

**Complementarity with the separability pattern ( #disc-separability-pattern).** This segment names the *negative half* of AAT's scope; the companion meta-segment #disc-separability-pattern names the *positive half* — separable-core / structured-repair / general-open across six ladders (correlation, convention, architecture, contraction, identification, scope). Each identifiability-floor instance here has a positive counterpart there: Instance 1's on-policy detection no-go matches the observable-sibling-covariance structured-repair in the correlation ladder; Instance 2's unobservable-$C$ L1' refutation matches the observable-$C$ / facilitator-monotonicity structured-repair in the same ladder. The two halves together characterize AAT's scope at both extremes — what succeeds and under what machinery, and what structurally cannot succeed without specific information augmentation.

**This segment is the *boundary facet* of the stability certificate ( #disc-stability-certificate).** The rank-collapse floors are the certificate dropping rank — the boundary of the positive-definite cone whose interior is operator-sector — with the Sylvester-law irreducibility (above) the statement that the framework's representational freedom is a congruence orbit that cannot cross that boundary. Read through the spine, this segment answers "where does the agent's measuring-stick go flat, and why does no re-graduation un-flatten it"; #disc-separability-pattern answers "where does a stick exist at all" (scope-of-existence facet) and #disc-additive-coordinate-forcing "which stick is forced" (forced-identity facet).

**The pattern is conservative in style.** Each floor invokes a published external theorem (Bareinboim et al. 2022; standard Cramér-Rao bound) rather than deriving a new impossibility result. AAT's contribution is the *application* — recognizing the AAT setting falls within the theorem's scope, characterizing the boundary conditions, and identifying which AAT machinery is the unique broadly-available escape. This style aligns with the broader posture of AAT as an integrating framework that connects established results across control theory, causal inference, and information theory under a common formalism.

## Findings

### The Identifiability Floor as Cross-Cutting Meta-Pattern

**Brief:** Across four independently-derived results (the fourth — Instance 4 — is contested and KNOWN-DEFECTIVE; see its note above; the count is unreconciled pending its Joseph-reserved resolution), AAT has converged on a recurring shape: an inferential task (detecting a structural property, identifying a parameter, distinguishing two model classes) is shown structurally impossible under a specific information regime, by importing an external information-theoretic theorem (Pearl/Bareinboim's causal hierarchy, the Cramér-Rao bound, Liberzon's common-Lyapunov-nonexistence, Čencov's invariance theorem); the conditions under which the regime fails are characterized as boundary routes, each of which maps onto specific AAT machinery the theory already requires; and the floor strengthens the load-bearing role of that machinery by elevating it from "useful" to "the unique broadly-available escape." The pattern is a presentational organizing principle, not a theorem of its own — but the recognition that four distinct AAT results share this shape is itself an architectural finding worth surfacing externally, because it tells the reader where to look for AAT's distinctive scope-honesty moves and which adjacent floors are open research.

**Impact:** Surfaces a unifying frame for results that would otherwise read as disparate impossibility theorems. Each instance gains interpretive context (it is one of an emerging class) and the meta-segment provides a consistent template for evaluating candidate future floors (causal-IB extension, misspecification cost, tier-switching cost, mechanism-design impossibility). The pattern's positive content — that each floor names exactly which AAT machinery the theory requires to escape it — converts a sequence of negative results into a structural argument for the load-bearing status of the loop's interventional access (Instances 1 and 3, two semantically distinct deployment modes), of observability-as-information-augmentation (Instance 2), and of the (PI) parameterization-invariance axiom (Instance 4). The complementary `#disc-separability-pattern` carries the positive half (separable-core / structured-repair / general-open across seven ladders); together the two meta-segments mark AAT's scope honestly at both extremes.

**Novelty Claim:** *Claim recognition* of structural pattern across four AAT results that import external information-theoretic theorems to derive impossibility statements with mapped boundary-route escapes; the meta-pattern is an organizing principle rather than a theorem, and the per-instance prior-art positioning lives in the instance segments (`#der-causal-insufficiency-detection`, `#deriv-edge-credence-dynamics`, `#deriv-critical-mass-composition` / `#result-contraction-template`, `#deriv-observation-ambiguity-bias-bound`).

**Related Work:**

The four instances import distinct external theorems; per-instance prior-art landscapes live in the instance segments. The meta-pattern itself has no direct anticipation in the AAT-adjacent literature surveyed; the closest cousins are scope-honesty moves in formal-method literatures (Liberzon's switched-systems analysis, which itself instances the pattern; Cramér-Rao tradition in identifiability theory) and the broader posture of conservative-form causal inference (Pearl 2009, *Causality*; Bareinboim et al. 2022). What the meta-pattern adds is the cross-instance observation: AAT repeatedly recognizes that its own setting falls within a published external impossibility theorem, characterizes the boundary-route escape via existing AAT machinery, and uses the floor to elevate that machinery to load-bearing status.

| Pattern element | Where the move is established in the prior literature | Relationship / Positioning |
|---|---|---|
| Importing CHT to derive on-policy detection no-go (Instance 1) | Bareinboim, Correa, Ibeling & Icard 2022 (published 2022, found 2025) | *formal antecedent* — see `#der-causal-insufficiency-detection` Findings for the full Pillar-1 prior-art table; the meta-pattern subsumes this instance |
| Importing Cramér-Rao to derive mixture-identifiability no-go (Instance 2) | Cramér 1946, *Mathematical Methods of Statistics* (published 1946, found 2025-04) | *formal antecedent* — Fisher rank-deficiency forces the floor; see `#deriv-edge-credence-dynamics` Prop B.7 for the explicit calculation |
| Importing common-Lyapunov-nonexistence to derive composite-contraction no-go (Instance 3) | Liberzon 2003, *Switching in Systems and Control* §2.1; Dayawansa & Martin 1999 *IEEE TAC* 44:751; Shorten et al. 2007 *SIAM Review* 49:545 (found 2025-04) | *formal antecedent* — the symmetric-matched-Tier-1-scalar counterexample uses the standard switched-systems machinery; see `#deriv-critical-mass-composition` and `#result-contraction-template` for the AAT-internal closures |
| Importing (PI)/Čencov to derive universal-constant no-go (Instance 4) | Čencov 1982, *Statistical Decision Rules and Optimal Inference* (published 1982, found 2024); explicit heteroscedastic-normal counterexample derived AAT-internally | *formal antecedent for (PI) escape, AAT-internal for the no-go construction* — see `#deriv-observation-ambiguity-bias-bound` Attempt E |
| Cross-instance pattern recognition | No direct anticipation surfaced at search depth | *claim novelty* under cursory search — the meta-pattern as an articulated framework has not been found in the surveyed literatures; the constituent moves (scope-honesty, importing external no-go theorems, boundary characterization) are individually well-precedented but their cross-instance unification within an integrated agent-theoretic framework is a presentational contribution rather than a borrowed schema |

**Search Log:**

- 2026-04 (*nominally comprehensive at the per-instance level*, via `ref/Novelty_defense_and_integration.md` Pillar 1): The Undermind defense covered Instance 1's prior-art landscape (causal bandits / causal MDPs under hidden confounding); the meta-pattern itself was not the search target. Instances 2–4 inherit per-instance comprehensiveness from their constituent segments rather than from a cross-instance search.
- 2026-04 (*intuition-only* on the meta-pattern as an articulated framework): The cross-instance recognition that four AAT results share the *setting → external theorem → no-go → boundary characterization → strengthened-consequence* shape has not been searched for as a unified concept. Targeted future search candidates: scope-honesty traditions in formal verification (refinement-mapping work; Lamport's TLA; Abadi-Lamport refinement); identifiability-theory meta-frameworks; the broader "no-go theorems" literature in physics and economics. Expected outcome: the constituent moves are well-precedented; the unified framework as applied to an integrated agent theory may be novel under cursory search but is unlikely to be novel under comprehensive search of methodological-essay literature.

### The Rank-Collapse Floor's Irreducibility Is Sylvester's Law of Inertia

**Brief:** Picture the agent trying to pin down a parameter as localizing a point in a landscape whose curvature is the information it has. A "floor" is a *flat direction* in that landscape — a direction the data cannot resolve (rank-deficient Fisher information). The agent's only freedom is to re-draw its map: choose different coordinates, a different metric. Sylvester's law of inertia says that re-drawing the map with any invertible change of coordinates can bend, rotate, and rescale the contours but can never change *how many genuinely flat directions* exist at a point — a flat valley stays flat in every coordinate system. So when the information operator is rank-deficient, no choice of representation recovers the lost direction; the only thing that ever helps is *taking a new measurement* — adding genuinely new information (an intervention, a side channel, a witness), which is not a re-drawing of the map. A thoughtful non-specialist can re-derive the qualitative claim from the analog alone: you cannot survey your way out of a blind spot by changing the units on the ruler; you have to look from a new vantage point. This is the exact mechanism behind every rank-collapse identifiability floor, and it explains in one sentence why those floors are escapable only by capability, never by cleverness of representation.

**Impact:** Converts a sequence of per-instance "we checked, no reparameterization removes the degeneracy" computations (Fisher rank-1 in #deriv-edge-credence-dynamics Prop B.7; on-policy no-detection in #der-causal-insufficiency-detection) into one named classical theorem (Sylvester 1852), sharpening the meta-pattern's load-bearing claim. It converts the prior honest-but-soft positioning "the identifiability floor is *orthogonal* to the contraction/operator-sector machinery" into the sharp geometric statement: operator-sector is the *interior* of the positive-definite (information / stability-certificate) cone; the rank-collapse floor is its *boundary*; and the boundary is invariant under the agent's entire representational freedom because that freedom is exactly the congruence orbit Sylvester's law fixes. The escape routes named per instance (loop-interventional access; observability of latents) are unified as *rank-augmentation* of the information operator — the unique category of move that is not a congruence. The result also bounds its own scope honestly: it is the mechanism for the rank-collapse subclass only. Instance 3 (composite contraction certification) has a structurally different obstruction — composition is a non-invertible projection, so its no-go is a Schur-complement / memory-kernel statement, not an inertia statement. That the floors are *plural in mechanism* (Sylvester for rank-collapse; a projection-closure obstruction for composition) is itself the reason the floor pattern is a presentational family and not a single theorem — this Finding makes that plurality precise rather than leaving it as "they are different concerns."

**Novelty Claim:** *Claim recognition* that the irreducibility of AAT's rank-collapse identifiability floors is a single named classical theorem — Sylvester's law of inertia applied to the Fisher-information reparameterization law — rather than a coincidence of per-instance computations; and *claim differentiation* that this mechanism is specific to the rank-collapse subclass and provably distinct from the composition floor's projection-closure obstruction. Sylvester's law itself is classical (1852); the contribution is the recognition that AAT's representational freedom is exactly its congruence orbit, which makes the floor's irreducibility a corollary rather than a checked property.

**Related Work:**
- Sylvester, J. J. (1852), "A demonstration of the theorem that every homogeneous quadratic polynomial is reducible by real orthogonal substitutions to the form of a sum of positive and negative squares," *Phil. Mag.* 4(23):138–142 (found 2026-05-14) — *formal antecedent* — the inertia-invariance theorem; applied here to the Fisher-information congruence.
- Horn, R. A., & Johnson, C. R. (2013), *Matrix Analysis* (2nd ed.), Thm 4.5.8 (found 2026-05-14) — *formal antecedent* — standard modern statement of the law of inertia used in the argument.
- Lehmann, E. L., & Casella, G. (1998), *Theory of Point Estimation* (2nd ed.), §2.5 (found 2026-05-14) — *formal antecedent* — the Fisher-information reparameterization law $\mathcal G_\varphi = S^\top \mathcal G_\theta S$ that makes every coordinate change a congruence.
- Per-instance external theorems (Bareinboim et al. 2022; Cramér 1946) — *adjacent* — established in the instance segments' own Findings; this Finding adds the cross-instance mechanism, not the per-instance prior art.

**Search Log:**
- 2026-05-14 (*targeted*): The recognition arose in the operator-family-unification spike from the certificate-cone framing. Sylvester's law and the Fisher reparameterization law are textbook; the search target was whether the *recognition* "AAT's identifiability-floor irreducibility = Sylvester's law via the Fisher congruence" appears as an articulated statement in the identifiability-theory or causal-inference methodological literature. Not found at this depth; the constituent facts are universally known but the cross-instance unification as the named irreducibility mechanism for an integrated agent theory's floor pattern appears to be a fresh presentational recognition. Expected to remain *recognition*-tier under deeper search (the pieces are classical; the assembly is the contribution).

## Working Notes

- **Sylvester-recognition provenance.** The rank-collapse-floor-as-Sylvester finding and the certificate-cone framing it sits in were worked out in the 2026-05-14 operator-family-unification cycle; see CHANGELOG 2026-05-14. The broader spine question (reorganizing M1/M2/M3 as facets of one certificate-cone object) is *resolved* — landed as #disc-stability-certificate + #result-certificate-existence, with this segment as the boundary facet (see the Discussion cross-ref above). Originating spike is absorbed archaeology, not a live reference.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Naming convention.** "Identifiability floor" frames the pattern positively: the floor is what the agent cannot go below given limited information, but the boundary characterization tells the agent exactly how to climb above it. An alternative name "no-go theorems" would emphasize the negative form. Recommend retaining "floor" — it captures the asymmetry.

- **Instance 3 as a candidate.** The "L1 augmentation when the augmentation graph is itself causally insufficient" question (recurse the no-go: detect when the L1 augmentation is itself missing common causes) is a candidate Instance 3. Likely reduces to Instance 1 applied at the L1 level — the agent at L1 faces the same on-policy detection no-go for L1 → L2 escalation. Worth formalizing if a third instance emerges that does *not* reduce to the existing two.

- **Is the floor pattern unique to causal/identifiability questions?** The two current instances are both about distinguishing two parameter regimes from data. The pattern may also apply to other impossibility-style results in AAT: the inevitability of structural-adaptation thresholds ( #result-structural-adaptation-necessity), the cost of representing high-correlation regimes (L2 exponential blowup), the bandwidth limits in shared intent ( #def-shared-intent). Whether to absorb those into "identifiability floor" or treat them as a separate "structural-cost" pattern is open.

- **Cross-segment integrations.** The meta-pattern surfaces in (at least): #der-causal-insufficiency-detection (Instance 1); #deriv-edge-credence-dynamics Prop B.7 (Instance 2); #der-loop-interventional-access (load-bearing for Instance 1 escape); #def-strategy-dag (the L0/L1/L1'/L2 hierarchy is the regime ladder Instance 2 lives on). Each of these segments cross-references this one for the unifying frame.


---

### Source: `disc-separability-pattern.md`

```yaml
---
slug: disc-separability-pattern
type: discussion
status: discussion-grade
depends:
  - def-strategy-dag
  - def-value-object
  - der-directed-separation
  - form-composition-closure
  - scope-edge-update-causal-validity
  - def-agent-spectrum
  - disc-approximation-tiering
  - disc-identifiability-floor
stage: draft
---
```


# Discussion: The Separability Pattern — Separable Core, Structured Repair, General Open

AAT consistently runs a three-part epistemic posture across state spaces that admit no tractable exact treatment in general: name the **separable core** where identification is clean, name the **structured repair** that recovers identification under explicitly-added machinery, and name the **general open** case where the problem is either intractable or structurally unidentifiable. Six ladders in the current theory share this shape. This segment names the pattern as an organizing principle, catalogs the instances, and makes the complementarity with `#disc-identifiability-floor` (which names the *negative half* of AAT's scope) explicit.

## The pattern

Each instance of the separability pattern has the form:

1. **Separable core.** A sub-class of problem in which identification is tractable by construction — the quantity of interest has a clean estimator that requires only assumptions the agent can verify or control. "Separability" here is broader than statistical independence: it names the regime in which the quantity decomposes along a structural axis (independence, additive decomposition, directed separation, strong contraction, clean intervention, etc.) without interaction terms requiring additional machinery.

2. **Structured repair.** A sub-class where the separability assumption fails but a *specific, named, bounded-cost* additional mechanism recovers identification. The repair is structured: it identifies the failure mode, adds a specific compensating construction, and typically carries a characterized loss in tightness or generality. Repairs are not "apply heuristics"; they are "augment with observability of $C$ and accept $O(1)$ per-node parameter cost," "run receding-horizon replanning at cost $\mathrm{DL}(\Sigma_t)$," or similar.

3. **General open.** The fully-general case where no tractable repair is known. This is where `#disc-identifiability-floor` instances live — structural no-go results that characterize *why* the general case remains open. Naming this boundary positively (as a known frontier) rather than negatively (as a failure) is part of AAT's load-bearing scope honesty.

## Current instances — six ladders

| Ladder | Separable core | Structured repair | General open |
|---|---|---|---|
| **Correlation** ( #def-strategy-dag) | **L0** — independence model, $O(\lvert V\rvert + \lvert E\rvert)$ propagation | **L1** — strict-prerequisite augmentation with explicit common-cause node; **L1'** — soft-facilitator mixture with five-way gating under observable $C$ + facilitator monotonicity ( #deriv-edge-credence-dynamics Prop B.7) | **L2** — full joint; **L1' unobservable-$C$** single-channel is *refuted* by Cramér-Rao floor ( #disc-identifiability-floor Instance 2) |
| **Convention** ( #def-value-object) | **C1** — one-step improvement | **C2** — receding-horizon replanning | **C3** — Bellman optimal; intractable for large state spaces |
| **Architecture** ( #der-directed-separation) | **Class 1 (Separated)** — directed separation holds by construction | **Class 2 (Partial)** — directed separation holds for identified submodules | **Class 3 (Coupled)** — directed separation fails by construction; logogenic territory; coupled formulation required |
| **Contraction** ( #form-composition-closure) | **Tier 1** — strong monotonicity; bridge lemma applies with proved $\varepsilon^\ast$ | **Tier 2** — local convexity; bridge applies within a specified basin | **Tier 3** — neither; domain-specific verification required per instance |
| **Identification regime** ( #scope-edge-update-causal-validity) | **Regime A** — interventional ($\iota_{ij} = 1$); action is a literal $do(\cdot)$ | **Regime B** — partial intervention ($0 \lt \iota_{ij} \lt 1$); confounder adjustment, side-channel observation | **Regime C** — observational ($\iota_{ij} \approx 0$); identification depends on external assumptions (e.g., unconfoundedness) |
| **Scope hierarchy** ( #def-agent-spectrum) | **Adaptive** — basic feedback loop; #scope-adaptive-system satisfied | **Agency** — goal-bearing with $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect; adds $O_t$ and $\Sigma_t$ machinery (Section II); #scope-agency satisfied | **Composite** — multi-agent / team / logogenic; Section III gaps listed at the OUTLINE level (latent structural diversity, endogenous coupling, composition transition dynamics, agent opacity) |
| **A2'-scope** ( #result-contraction-template) | **metric-$\alpha_1$** — Euclidean metric, AAT-internally derived via DA2'-inc ≡ (CT2) at $M = I$ (scalar Kalman, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) | **metric-$\alpha_2$** — non-Euclidean metric under explicit conditions; includes five cases (information-metric Kalman, Fisher-metric exp-family, Hessian-metric ill-conditioned, Lyapunov-metric linear-Hurwitz-non-symmetric, Lyapunov-metric PID-bounded-plant). Two of five (Fisher cases) AAT-internally forced under (PI)/Čencov per `#disc-additive-coordinate-forcing`; remaining three theorem-imported from Lohmiller-Slotine 1998 | **metric-$\beta$** — contraction-metric formulation fails (variational-to-projected-target; rule-based / non-smooth; severely misspecified; per-step SGD / human judgment) |

*GUC Architecture-row key: Class 1 = Separated (was Modular); Class 2 = Partial (was Class 3 Partially modular); Class 3 = Coupled (was Class 2 Fully merged). See `#der-directed-separation`.*

Each row independently satisfies the three-part shape. The shared shape is not designed-in: it arises because AAT faces seven distinct sources of intractability and applies the same posture (name the clean case, name the repair, name what remains open) to each.

## Complementarity with the identifiability floor

The **separability pattern** names the *positive half* of AAT's scope: for each ladder, what succeeds under what conditions. Each separable-core entry is a positive identification claim; each structured-repair entry is a positive identification claim *conditional on* an explicitly-named added mechanism.

This segment is the *scope-of-existence facet* of the stability certificate ( #disc-stability-certificate): a separable-core entry is a region where a certificate exists cleanly, a structured-repair entry is a region where one exists under explicitly-added machinery, and a general-open entry is where no certificate is available without further information. Read through the spine, this segment answers "where does the agent's measuring-stick exist at all"; #disc-identifiability-floor answers "where does it go flat" (boundary facet) and #disc-additive-coordinate-forcing "which stick is forced" (forced-identity facet).

The `#disc-identifiability-floor` names the *negative half*: structural no-go results (impossibility under limited information) that characterize why specific general-open cases remain open. Two floors are currently derived:

- **Instance 1** (on-policy L0-insufficiency detection via Causal Hierarchy Theorem) — forbids L0/L1 distinction from purely on-policy data. The positive counterpart: the **separable core under observable sibling covariance** is the unique broadly-available violation of the no-go's scope, naming what the agent *can* observe to escape the floor.
- **Instance 2** (L1' unobservable-$C$ single-channel via Cramér-Rao) — forbids mixture-parameter identification when $C$ is unobservable. The positive counterpart: the **structured repair under observable $C$** (Prop B.7 with facilitator monotonicity) is the identification-succeeds-under-augmentation claim matching the no-go's "unless $C$ is observable or multi-child observation is available" scope exit.

Together, the two meta-segments mark AAT's scope at two epistemic layers:

- **Separability pattern** — "here is what succeeds, with clean conditions and explicit repairs."
- **Identifiability floor** — "here is what structurally cannot succeed without specific information augmentation."

Neither alone gives the full picture. A theory stating only the positive half looks unbounded in its claims; a theory stating only the negative half looks conservative in a way that hides its achievements. Together they give scope honesty at both extremes.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. The segment is a presentational organizing principle. It names a shared shape that AAT already runs across multiple ladders; the pattern itself is not derived and has no theorem of its own. The individual ladder entries retain their own epistemic status — Correlation hierarchy results are at the tier specified in #def-strategy-dag and #deriv-edge-credence-dynamics; Convention hierarchy monotonicity is at the tier specified in #def-value-object; Contraction tier taxonomy is at the tier specified in #form-composition-closure; etc.

Max attainable: *discussion-grade* for the meta-pattern (it is an organizing principle, not a derivation). Individual instances are at their own tiers as above. The six-ladder enumeration could become *robust-qualitative* if a uniqueness argument were derived showing that separable-core / structured-repair / general-open is the unique viable posture across scope-parameterized hierarchies under AAT's scope-honesty architectural principle — but this is not currently in hand, nor clearly attainable.

## Discussion

**The pattern is load-bearing for how AAT presents its results.** A common failure mode of applied theories is the binary "exact under assumption X, breaks otherwise" presentation. The separability pattern refuses this presentation across six instances: where X fails, a named lower tier takes over with a characterized weaker result, and the theory provides a diagnostic for when to escalate (per #disc-approximation-tiering's AT4 component). Readers who learn the pattern once can navigate any instance; this is what makes AAT tractable as an integrating framework rather than a pile of instantiations.

**Relationship to #disc-approximation-tiering.** This segment is complementary to #disc-approximation-tiering, not redundant with it. #disc-approximation-tiering names the *structural template* (AT1 parameter indexing tractability; AT2 proved monotonicity between tiers; AT3 graceful degradation; AT4 ascension diagnostic) — the how-it-works of each tiering. This segment names the *epistemic posture* (separable core, structured repair, general open) — the what-each-tier-commits-to. Both are needed: #disc-approximation-tiering explains what makes a successful tiering; this segment explains the shape of the commitment each tier makes about identification.

**Relationship to #disc-independence-audit.** #disc-independence-audit catalogs the *independence assumptions* whose failure degrades results; this segment catalogs the *ladders of recovery*. Together with #disc-approximation-tiering they form a three-part characterization of AAT's scope:

- **#disc-independence-audit** — where the boundaries are (which assumptions, what breaks if they fail).
- **#disc-approximation-tiering** — how to navigate within the boundaries (parameterized hierarchy + monotonicity + ascension).
- **#disc-separability-pattern** (this) — what each tier positively commits to (separable core / structured repair / general open).

**The pattern is distinctive to AAT's integration-over-invention character.** Approximation tiering with a separability posture is a common move in applied mathematics — it appears in numerical methods (exact vs. high-order vs. low-order with error bounds), in statistical inference (parametric separable-core / semiparametric repair / nonparametric open), in causal identification (Pearl's three-layer hierarchy is itself an instance). AAT's contribution is not the pattern but its deployment across the six specific intractable problems adaptive-agent theory faces, each with its own positive-half identification claims and negative-half floor instances.

**The A2' sub-scope partition is a proper three-part ladder via #result-contraction-template.** The A2' partition carries three tiers: sub-scope $\alpha$ (A2' derived under `#der-gain-sector-bridge` directional fidelity) as the separable core; sub-scope metric-$\alpha_2$ (non-Euclidean metric under explicit conditions — five cases, with two Fisher-metric cases AAT-internally forced under the (PI)/Čencov fourth primary instance of `#disc-additive-coordinate-forcing`) as the structured-repair middle tier; sub-scope $\beta$ (A2' assumed) as the general-open tier. A2'-scope therefore qualifies as the seventh ladder of this meta-pattern, as enumerated in the table above. The structured-repair middle tier closes what would otherwise be a binary $\alpha$/$\beta$ partition lacking a derivable middle ground.

**The software calibration-lab framing ( #obs-software-epistemic-properties) is a specific instance.** C-BP3's calibration-lab reframing (commit `d0373fc`) partitions operational domains into "separable core" (software, where identification conditions P1–P6 are cleanly satisfied) and "structured-repair / general open" (other domains, which inherit under explicitly-named transfer assumptions). This is a domain-axis instance of the same pattern — software is the domain-axis separable core; the transfer-assumption table is the domain-axis structured-repair specification.

## Working Notes

- **Standalone-paper candidacy.** This meta-pattern is a candidate for standalone publication per the *B-N-Sep* portfolio entry. The strategic plan (paper structure, prior-art landscape, cite-and-extend anchors, venue analysis, effort estimate) lives at [`msc/separability-standalone-paper-proposal.md`](../../msc/separability-standalone-paper-proposal.md), which subsumes the equivalent section in `~/src/ops/papers/03-asf-tier2-and-cross-segment.md`. **Verified novel** by independent prior-art search: Undermind 31-paper full-text sweep (2026-05-04) returned no exact named cross-domain meta-pattern; closest neighbors are Hintikka 1991 (general theory of identifiability), Pearl/Shpitser ID lineage (most-developed within-domain instance), Bareinboim 2022 (cross-hierarchy meta-discussion at N=2-3 hierarchies), Basse-Bojinov 2020 (modern formal abstraction across fields), Maclaren-Nicholson 2019 (ill-posed inverse problems as cross-field dual structure). Full report at [`ref/separability-ladder-prior-art-report.md`](../../ref/separability-ladder-prior-art-report.md).

- **Citations to land on promotion to draft / when paper drafting begins:**
   - **Hintikka, J. (1991).** *"Towards a General Theory of Identifiability."* In *Definitions and Definability: Philosophical Perspectives*, J. H. Fetzer et al. (eds.), Kluwer Academic. DOI: 10.1007/978-94-011-3346-3_7. Locally at [`ref/towards-a-general-theory-of-identifiability.pdf`](../../ref/towards-a-general-theory-of-identifiability.pdf). **Strongest older abstract anchor**: tripartite *definable / identifiable / non-identifiable* trichotomy. Hintikka §1: "P is identifiable on the basis of T[P]" when "the interpretation of P is not determined on the basis of the theory alone, but is determined by the theory together with a number of auxiliary empirical results." The pattern's middle rung in Hintikka's vocabulary; ASF's structured repair generalizes "auxiliary empirical results" to "named bounded-cost structural augmentation" (a real but small extension).
   - **Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022).** *"On Pearl's Hierarchy and the Foundations of Causal Inference."* In *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books. DOI: 10.1145/3501714.3501743. Treats Pearl's hierarchy as a logical and epistemic hierarchy and compares it to formal-language and complexity hierarchies — closest existing cross-hierarchy meta-discussion at N=2-3, but stops short of the cross-domain meta-pattern this segment names.
   - **Robins, J., Richardson, T. & Shpitser, I. (2020).** *"An Interventionist Approach to Mediation Analysis."* In *Probabilistic and Causal Inference*, ACM Books. DOI: 10.1145/3501714.3501754. Cleanest in-domain cite-and-extend anchor: clean separable case + structured-repair via expanded-graph decomposition + recanting-witness no-go.
   - **Shpitser, I. & Pearl, J. (2006, 2008).** *"Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models"* (AAAI); *"Complete Identification Methods for the Causal Hierarchy"* (JMLR 9). Foundational ID completeness papers — the cleanest verified no-go-plus-recovery pairing; the ID algorithm IS this template within causal inference.
   - **Bareinboim, E. & Pearl, J. (2012, 2014); Lee, S., Correa, J. D. & Bareinboim, E. (2019).** Surrogate experiments (z-identifiability), transportability with limited experiments, general identifiability with arbitrary surrogates. Each is a structured-repair instance with a named bounded augmentation. Several locally at `ref/`.
   - **Basse, G. W. & Bojinov, I. (2020).** *"A general theory of identification."* Closest modern formal abstraction across fields (identifiable / partially-identified / strongly-non-identifiable regimes); lacks the bounded-cost-repair operator as middle rung.
   - **Maclaren, O. J. & Nicholson, R. (2019).** *"What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems."* arXiv 1904.02826. Best dual-structure cross-field neighbor (causal identification ↔ ill-posed inverse problems); centers on stability/regularization rather than structured-repair.
   - **Restricted-intervention lineage:** Robins 1986 (treatment-regime semantics; locally at `ref/`); Richardson 2013 SWIGs; Dawid 2000 ("causal inference without counterfactuals"; locally at `ref/`); Dawid 2020 (decision-theoretic foundations); Richardson-Robins 2023 (SWIG/decision-theoretic bridge). Patches the missing-prior-art lineage for restricted/regime-defined intervention semantics.
   - **Neighboring recurrence inside causal identification:** Robins-Richardson 2010 (alternative graphical models, expanded graphs); Stensrud et al. 2019 (separable effects in competing events); Díaz 2022 (non-agency interventions); Shpitser-Tchetgen 2014 (intervention hierarchy unification). Pattern recurs in mediation, competing-events, edge-intervention settings within wider causal-identification literature.
   - **Adjacent abstractions that stop short:** Iwasaki-Simon 1994 (causality and model abstraction; near-decomposability); Hoover 2012 (causal structure and hierarchies of models; well-made-toaster vs repairman cases). Strong philosophy-and-Simon-line parallels; not a formal tractability/identifiability ladder. Downey-Fellows 1995/1999 (parameterized complexity, FPT/W[1]/paraNP-hard) and Simpson 1999 (reverse mathematics) for hierarchy-of-strength formalisms; verified weak connection to applied-identifiability ladders.

- **Pending family rename and rung-rename decision.** The family name is queued for rename: `discussion-separability-pattern` → `discussion-separability-ladder`, on Round-1 consensus rationale that "ladder" is more evocative for the three-rung shape than "pattern" (which is generic). See [`msc/naming/naming-rename-plan.md`](../../msc/naming/naming-rename-plan.md) §"Deferred to refined Round 1 / Round 2". The **three rung-names** (currently *separable core* / *structured repair* / *general open*) are also under consideration for refinement; Hintikka 1991's *definable / identifiable / non-identifiable* trichotomy is a strong candidate for an aligned echo (modulo a small extension on the middle rung from "auxiliary empirical results" to "named bounded-cost structural augmentation"). Decision deferred (2026-05-04). The standalone-paper proposal (above) is ready to draft against either the status-quo names or any of the alternates — the rename can land separately with no impact on paper-drafting tractability.

- **Cross-ladder monotonicity.** The six ladders interact — an agent operating at L0 correlation + C2 convention + Class 1 architecture + Tier 1 contraction + Regime A identification + Agency scope is in a specific combined regime. Does cross-ladder monotonicity hold in any direction? E.g., does moving from L0 to L1 change anything about the Convention hierarchy's guarantees, or do the ladders factor independently? `#disc-approximation-tiering`'s Working Notes flag this as an open question; the separability pattern's complementarity with the identifiability floor adds a further axis (which combinations are known-unidentifiable per #disc-identifiability-floor).

- **Extension candidates beyond the six.** Three candidate future ladders noted in #disc-approximation-tiering — scalar-vs-per-dimension tempo, AND/OR parameterization, A/B/C identification (now promoted here) — fit the separability-pattern shape. Promoting them to named ladders with explicit separable-core / structured-repair / general-open entries would extend the pattern to 8–9 ladders. Each promotion requires its own per-instance work.

- **Necessity argument for the pattern itself.** Is there a scope-honesty theorem of the form "any theory that claims exactness under Class-1-style assumptions *and* claims coverage beyond those assumptions must exhibit the separability pattern (or an equivalent three-part decomposition) to avoid latent overclaim"? If so, AAT's deployment of the pattern six times would be a *derived* structural necessity rather than a stylistic consistency. Speculative; not pursued.

- **Does C-BP2 belong in AAT core or in the wider framework narrative?** The segment currently lives in `01-aat-core/` because its instances are AAT segments. If TST adopts the same pattern across its own ladders (e.g., software-calibration-lab as a domain-axis ladder), the segment may want to move up to the root framework level. Deferred; the current placement is defensible while TST adoption is partial.

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Architecture row updated: Class 1 | Class 2 | Class 3 now reads left-to-right monotonically (cleanest → middle → worst), matching the six other AAT ladders. GUC key added below the row. Removed at `candidate` stage per FORMAT.md Gate 4.


---

