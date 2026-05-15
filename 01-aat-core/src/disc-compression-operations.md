---
slug: disc-compression-operations
type: discussion
status: robust-qualitative
depends:
  - form-information-bottleneck
  - form-strategy-complexity-cost
  - def-shared-intent
  - form-composition-closure
  - def-chronica
stage: draft
---

# Discussion: Compression Operations in AAD

AAD contains four compression operations — the epistemic model $M_t$, the strategy DAG $\Sigma_t$, shared intent $G_t^{\text{shared}}$, and the composition projection $\Lambda$ — each formulated in its own segment with its own objective. Three of the four are written in Information Bottleneck (IB) form already; the fourth is stated as an IB constraint. This segment makes the shared shape explicit, promotes one underspecified source (the ontologically ambiguous "true causal structure" for $\Sigma_t$) to a cleaner formulation parallel to $M_t$, and establishes that composition admissibility (P1) is the Lagrangian-dual of a standard IB objective. It does *not* claim the four operations reduce to a single optimization problem — cross-instance theorems do not follow from the shared shape alone, and several conditions (Lipschitz regularity (P2), dimensional reduction (P3) in the Gaussian case, interventional relevance for Level-2 edges) remain outside the IB frame.

## Formal Expression

### The shared IB shape

*[Discussion (ib-shape)]*

Every compression operation in AAD has an objective or constraint of the form:

$$T^\ast = \arg\min_{T \mid X}\; \bigl[\, I(X; T) \;-\; \beta \cdot I(T; Y) \,\bigr]$$

with the Markov chain $Y - X - T$. The four AAD instances specialize this with different bindings:

| Instance | $X$ (source) | $T$ (compressed) | $Y$ (relevance variable) | $\beta$ (trade-off) |
|---|---|---|---|---|
| Model compression ( #form-information-bottleneck) | $\mathcal C_t$ | $M_t$ | $o_{t+1:\infty} \mid a_{t:\infty}$ | $\beta(\rho, \pi)$ — volatility and policy |
| Strategy compression ( #form-strategy-complexity-cost) | $\mathcal C_t$ | $\Sigma_t$ | $\pi^\ast \mid M_t$ | $\beta_\Sigma$ — cognitive cost per decision-bit |
| Shared intent ( #def-shared-intent) | $G_t^{\text{full}} = (O_t, \Sigma_t)$ | $G_t^{\text{shared}}$ | $a_t^{\text{coordinated}}$ | bandwidth per coordination-bit |
| Composition projection ( #form-composition-closure P1) | $X_{\text{micro},t}$ | $\Lambda_x(X_{\text{micro},t})$ | $o_{\text{micro},t+1} \mid a_{\text{micro},t}$ | $\beta(\epsilon_I)$ — rate-distortion Lagrange multiplier |

What the four instances share: *shape* (the objective structure), *variational calculus* (minimization over stochastic compressors), and *rate-distortion interpretation* (each trade-off parameter indexes a point on the frontier). What they do not share: source type (history vs. structured state), relevance-variable availability (observed vs. latent), computability (Gaussian closed forms vs. variational approximation), or a single joint optimization across the four. The level of unification is *medium*: shared shape and vocabulary, not a shared master problem.

### Strategy compression: source reformulation

*[Formulation (strategy-compression-source)]*

The current statement in #form-strategy-complexity-cost has the $\Sigma_t$ IB objective as:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t}\; \bigl[\, \operatorname{DL}(\Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

Two issues with this as currently written:

1. **The compression cost is description length, not mutual information.** DL and $I(X; T)$ are related through coding-theoretic equivalences but coincide only under specific coding schemes. Using DL in the complexity term blocks the identification of this objective as an IB instance directly.
2. **The "source" is not an AAD object.** To fit the IB shape, the objective implicitly treats $\Sigma_t$ as a compression of "the true causal structure." That structure is not part of AAD's ontology — the agent never has access to it; it is only ever implicit.

**Reformulation.** Treat $\Sigma_t$ as a compression of $\mathcal C_t$ (the interaction history — the agent's only evidence) *for decision-relevance*, parallel to $M_t$ which is a compression of $\mathcal C_t$ *for prediction-relevance*:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t}\; \bigl[\, I(\mathcal C_t; \Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

Under this reformulation:

- The source $\mathcal C_t$ is a well-defined AAD object, shared with the $M_t$ instance.
- The two instances differ cleanly in relevance variable: $M_t$ is compressed for prediction ($Y = o_{t+1:\infty} \mid a$); $\Sigma_t$ is compressed for guidance ($Y = \pi^\ast \mid M_t$). Prediction is about *what will happen*; guidance is about *what to do*. Both are computed from the same history, with different targets.
- The information cost $I(\mathcal C_t; \Sigma_t)$ replaces $\operatorname{DL}(\Sigma_t)$ as the theory-level compression term. The DL formulation remains useful as an *operational* cost measure for specific DAG encodings; it is not the theoretical quantity the IB objective minimizes.

**Relationship between the two cost measures.** Under MDL with a specific encoding scheme for DAGs (the one in #form-strategy-complexity-cost), $\operatorname{DL}(\Sigma_t)$ is an upper bound on $I(\mathcal C_t; \Sigma_t)$ for DAGs produced by the given encoder — coding cost dominates distinguishability cost. In practice, DL is computable and $I$ is not, so the operational minimization uses DL as a proxy; the theoretical minimization uses $I$. The IB objective above is the theoretical statement; the DL-based minimization in #form-strategy-complexity-cost remains the practical one.

**Variational form.** The Shannon mutual information $I(\Sigma_t; \pi^\ast \mid M_t)$ in the relevance term collapses to zero when $\pi^\ast$ is deterministic-from-$M_t$. The variational form (cf. #form-strategy-complexity-cost) replaces the relevance term with the KL-divergence $D_{\mathrm{KL}}(\pi^\ast(\cdot \mid M_t) \,\Vert\, Q_{\Sigma_t}(\pi \mid M_t))$ — note the $\pi^\ast$-first direction, which is *forced* by a regret-bound derivation (full derivation and admissible-divergence family analysis in #deriv-strategy-cost-regret-bound). Under bounded value range and deterministic $\pi^\ast$, Pinsker's inequality gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast\Vert Q_{\Sigma_t})}$ where $R$ is the strategy-induced regret against $\pi^\ast$; the opposite KL direction is vacuous ($+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass). The $\pi^\ast$-first KL is well-defined and graded under deterministic $\pi^\ast$. Under the variational reading, the AAD $\Sigma_t$ is a tractable approximation of the policy-relevant posterior, and the KL term measures approximation quality — aligning the strategy compression with the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020). The direction alignment is convergent: both AAD's regret-bound and active inference's variational-free-energy derivations pick $\pi^\ast$-first KL (reverse-KL in the variational-inference vocabulary), with AAD's additional interpretation being an upper-regret-bound rather than free-energy-gradient. The shared-IB-shape framing of the four AAD compression operations is the rate-distortion specialization of this variational picture; AAD's commitment is to the rate-distortion form (which gives the (P1) Lagrangian-dual derivation and the four-instance unification at U-medium), not to the full variational free-energy interpretation.

### Composition admissibility (P1) as IB Lagrangian-dual

*[Derived (p1-ib-dual, from composition-closure + rate-distortion duality)]*

#form-composition-closure condition (P1) is currently stated as a lower-bound constraint:

$$I\bigl(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\bigr) \;\geq\; (1 - \epsilon_I) \cdot I\bigl(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\bigr)$$

This is the *constraint form* of an IB problem. In Lagrangian form:

$$\Lambda^\ast \;\in\; \arg\min_{\Lambda \in \mathcal P}\; \bigl[\, I(X_{\text{micro}}; \Lambda_x(X_{\text{micro}})) \;-\; \beta(\epsilon_I) \cdot I(\Lambda_x(X_{\text{micro}});\, Y_{\text{rel}}) \,\bigr]$$

where $Y_{\text{rel}} = (o_{\text{micro},t+1} \mid a_{\text{micro},t})$ and $\beta(\epsilon_I)$ is the Lagrange multiplier corresponding to the relevance-preservation tolerance $\epsilon_I$. The correspondence $\epsilon_I \leftrightarrow \beta$ is the standard rate-distortion duality: smaller $\epsilon_I$ (more relevance preserved) corresponds to larger $\beta$ (less aggressive compression).

Consequence: admissible projections are those that sit *on or above* the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$. The information-theoretic content of (P1) is exactly "project onto the IB frontier with a tolerance $\epsilon_I$." This formalizes the connection previously logged in #form-composition-closure's Working Notes and in #result-unity-closure-mapping's §Connection to the Information Bottleneck.

**What this resolves.** The #form-composition-closure Working Note "Open: Information Bottleneck unification" is now resolved for (P1): it is the Lagrangian-dual of the IB constraint at $\beta(\epsilon_I)$. The corresponding Working Note in #result-unity-closure-mapping §6 moves from conjecture to derived result. Nothing else about (P1) changes — the condition continues to define admissible projections; only its information-theoretic reading is now explicit.

### What stays separate from the IB frame

Three admissibility and structural conditions do *not* reduce to IB:

- **(P2) Lipschitz continuity.** Not an IB constraint. The bridge lemma in #form-composition-closure requires (P2) for analytic reasons (propagating bounded closure defect into bounded trajectory error); IB does not impose any continuity condition on compressors. (P2) remains a separate admissibility condition.
- **(P3) Dimensional reduction.** In the Gaussian-IB case relevant to composition, the IB-optimal $T$ at any finite $\beta$ typically uses full support of $\mathbb R^{\dim X}$; the categorical dimensionality reduction $\dim \mathcal X_c \lt \dim \mathcal X_{\text{micro}}$ is a *harder* condition than any rate constraint. (P3) remains separate. (In discrete cases it may be rate-implied, but the composition instance is Gaussian.)
- **Interventional relevance (Level 2).** The relevance variable in all four instances is associational ($Y$ in a joint distribution with $X$ and $T$). Strategy edges in the regime-indexed interpretation ( #scope-edge-update-causal-validity) want interventional relevance for Regime A: "what edge $(i, j)$ predicts *under $do(i)$*." This is a strictly stronger requirement than IB provides. Adapting IB to interventional relevance (causal IB, Wieczorek & Roth 2017 and follow-ups) is an extension direction, not a specialization of the master IB.

The honest slogan is therefore "the (P1)-analog in each compression operation is IB; regularity, dimensionality, and interventional relevance are separate conditions that compose with it."

## Epistemic Status

*Robust-qualitative.* The claim that the four compression operations share IB shape is *discussion-grade* — it is a presentational observation supported by examining each segment's formulation and noting structural alignment. The $\Sigma_t$ source reformulation is a *formulation choice* replacing one underspecified source with a cleaner one; no derivation is needed because the new formulation and the old are not the same claim. The (P1) as Lagrangian-dual of IB is *derived* — rate-distortion duality is standard (see §I.12–13 of Cover & Thomas) and the constraint-form ↔ Lagrangian-form equivalence is mechanical.

Max attainable: *robust-qualitative* for the shared-shape claim; *derived conditional on rate-distortion duality* for (P1) as IB Lagrangian-dual; *formulation* for the $\Sigma_t$ source reformulation. The strongest version of the unification claim — "U-strong," that the four operations are the same optimization problem with different bindings — is *not* established and is unlikely to be, for reasons in the Discussion.

This segment does not promote any of the four instance segments. Each remains the primary site for its own instance. What this segment adds is the shared-shape framing, the $\Sigma_t$ source fix, and the (P1) derivation.

## Discussion

**Why not go further.** Two distinct claims could be made: (a) U-strong — the four operations are the *same* optimization problem with different bindings, so a single derivation specializes to each instance; (b) U-medium — the four share *shape*, vocabulary, and variational structure but differ in substantive ways (source type, relevance-variable availability, computability) that prevent a single derivation from covering all four. U-strong requires cross-instance theorems, results of the form "because these are all IB, property X holds across all four." No such theorems are identified. The shared IB shape is legibility-enhancing but does not produce deductions for free. This segment therefore states U-medium (shared shape) honestly rather than overclaiming U-strong.

**Honest credit to the hierarchical-generative-model lineage.** AAD's four compression operations are a structurally narrower family than the operations a hierarchical generative model in the predictive-coding lineage (Friston 2008, "Hierarchical models in the brain," *PLoS Comp. Biol.* 4; Friston 2010, "The free-energy principle: a unified brain theory?" *Nat. Rev. Neurosci.* 11; Clark 2013, "Whatever next?", *Behav. Brain Sci.* 36; Hohwy 2013, *The Predictive Mind*, OUP) could express. A hierarchical generative model layers compressions of compressions, with each layer producing a representation tuned to the next layer's prediction target — and the AAD compressions ($M_t$ for prediction, $\Sigma_t$ for guidance, shared intent for coordination, $\Lambda$ for level-bridging) are all expressible within that frame as specific layer-bindings. What AAD adds is structural: (a) the *relevance variables* $Y$ are made first-class with explicit per-instance bindings (see the table in §"The shared IB shape"); (b) the (P1)–(P3) admissibility conditions for composition give a measurable closure-defect bound that hierarchical-generative-model layering does not natively produce ( #form-composition-closure); (c) regime-indexed edges ( #scope-edge-update-causal-validity) introduce Pearl-Level-2 relevance for Regime A, which standard hierarchical generative models do not address. The shared family is real; AAD's additions are also real. The honest framing is "AAD's compressions are a structured subset of the hierarchical-generative-model family with additional structure load-bearing for AAD's specific results."

**Why this is not the "biggest available unification."** It is better described as the *most legible* unification. The pattern is already half-named at each instance site (three of four segments already write their objectives in IB form); the segment-level contribution is sharpening the naming and fixing one formulation issue ($\Sigma_t$ source), not discovering a new structural result. The biggest leverage concision move in the theory — the sector-Lyapunov template in #result-sector-persistence-template — is substantively different: it removes repeated content and absorbs proofs that previously appeared in multiple segments. This segment adds legibility without removing much.

**What each $\beta$ means.** The four trade-off parameters are not unified in value, only in role:

- $\beta(\rho, \pi)$ for $M_t$ depends on environmental volatility and policy; fast-changing environments or high-value policies both warrant higher $\beta$.
- $\beta_\Sigma$ for $\Sigma_t$ is the cognitive cost per decision-relevant bit retained; bounded-context agents (LLMs with finite windows) have low $\beta_\Sigma$.
- The bandwidth $\beta$ for shared intent is the communication-capacity-per-coordination-bit; low-bandwidth teams have low $\beta$.
- The $\beta(\epsilon_I)$ for (P1) is the rate-distortion Lagrange multiplier at tolerance $\epsilon_I$.

These are four calibration problems, not one. A theory of *resource allocation across the four compression operations* — where a single cognitive budget is split across modeling, strategy, communication, and composition — is not currently in AAD, and the unification does not produce it. If such a theory is ever needed, it would tie the four $\beta$s together through an outer optimization; the spike flags this as an open direction.

**Relationship to #def-unity-dimensions and #result-unity-closure-mapping.** The unity dimensions parametrize rate-distortion curves for closure defects ( #result-unity-closure-mapping). Under the present segment's framing, unity dimensions are *curve parameters for the $\Lambda$ instance of the IB schema*. This tightens the existing #result-unity-closure-mapping Discussion, which already presented the rate-distortion reading as the correct interpretation; it is now stated uniformly across the four compression operations.

**Relationship to #deriv-graph-structure-uniqueness.** The DAG-uniqueness result derives the *shape* of $\Sigma_t$ from operational postulates ( #deriv-graph-structure-uniqueness, Cox-analog). The present segment characterizes the *compression level* of $\Sigma_t$. These operate at different levels: uniqueness supplies the representational type (the compressed $T$ is a DAG), IB supplies the rate-distortion trade-off within that type (how richly the DAG is populated). The two arguments are independent and compatible — IB-compressed $\Sigma_t$ is a DAG-with-fewer-nodes, not a non-DAG.

**Position relative to the additive-coordinate-forcing pattern.** The IB Lagrangian's $I(X;T) - \beta \cdot I(T;Y)$ is an additive decomposition on a log-scale coordinate (mutual information is logarithmic by construction) — the same shape that #disc-additive-coordinate-forcing catalogs at the chain / divergence / update layers. The IB case is classified as an *adjacent family member* rather than a fourth primary instance because #form-information-bottleneck adopts the Lagrangian form from Tishby, Pereira & Bialek 1999 as an applied external theorem rather than re-deriving it under an AAD-internally-motivated additivity axiom. The Shore-Johnson 1980 system-independence axioms that axiomatize IB's additivity are cited in #deriv-strategy-cost-regret-bound §6.1; if a future framing pass promotes Shore-Johnson to an explicit AAD axiom, IB would move from adjacent member to fourth primary instance.

## Working Notes

- **The $\Sigma_t$ source reformulation changes the theoretical quantity without changing the operational computation.** #form-strategy-complexity-cost's DL-based minimization remains the practical procedure; what changes is the theoretical claim about what that procedure approximates. Depending on promotion-workflow preferences, the reformulation may warrant a small note in #form-strategy-complexity-cost referencing this segment.
- **(P1) as IB Lagrangian-dual does not close #form-composition-closure's other Working Notes.** Computability of (P1) for nonlinear/non-Gaussian systems, choice of $\epsilon_I$, and $N$-agent scaling remain open. The unification resolves the *framing* question but not the *computation* questions.
- **Synthesis segment vs. full unification.** This segment is a targeted synthesis: it fixes the $\Sigma_t$ source, derives (P1) as IB Lagrangian-dual, and tables the four instances. It does *not* rewrite the four instance segments as specializations of a master schema. If future work reveals that the four instance segments are pulling in inconsistent directions (e.g., if the $\Sigma_t$ reformulation creates friction with the DL-based minimization in #form-strategy-complexity-cost), that is the signal to escalate to a full rewrite in which the instance segments become thin specializations. Short of that signal, this targeted synthesis is the stopping point.
- **The Gaussian IB frontier derivation is deferred.** Completing the derivation that the means-sum projection attains the Gaussian IB frontier in the symmetric two-Kalman case would promote #result-unity-closure-mapping's rate-distortion claim from discussion-grade to derived. The obstruction is mechanical (specializing Chechik, Globerson, Tishby & Weiss 2005, "Information Bottleneck for Gaussian Variables," *J. Machine Learning Research* 6:165–188, Theorem 3.1 to the symmetric-gain setup) rather than structural — feasible as a follow-up derivation, not required for this segment.
