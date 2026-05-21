# Appendix — Details (group 4)


## Discussion: Independence Audit

- **Slug**: `disc-independence-audit`
- **Type**: discussion
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `der-directed-separation`, `def-strategy-dag`, `def-adaptive-tempo`, `def-unity-dimensions`, `result-per-dimension-persistence`, `deriv-graph-structure-uniqueness`

AAT's results depend on a recurring modeling move: treat some quantity as independent of another to obtain tractable mathematics, then identify the failure regime where independence breaks and specify the repair. This segment enumerates the independence assumptions used across the theory, their failure regimes, their diagnostic signals, and the repair operations AAT provides. The enumeration makes visible what is *not* an independence assumption — acyclicity of $\Sigma_t$, Cox-derived probability, the Lyapunov machinery of #result-sector-persistence-template — and therefore what survives when a particular independence assumption fails.

*[Discussion (independence-audit)]*

Six load-bearing independence assumptions in AAT, each paired with its failure regime and repair:

### 1. Directed separation: $M_t$ update independent of $G_t$

**Statement:** $f_M(M_{\tau^-}, e_\tau)$ has no $G_t$ argument — the epistemic update is goal-blind.

**Where it appears:** #der-directed-separation, the structural backbone of Section II. Feeds the orient cascade's sequential resolution ( #der-orient-cascade), the causal validity of $Q_O$ ( #def-value-object), and the scope of all Section II results to Class 1 (Separated) agents.

**Failure regime:** Class 3 (Coupled) architectures — transformer LLMs where attention processes goals and observations together. Motivated reasoning, confirmation bias, prompt-conditioned perception. Partially also Class 2 (Partial) agents.

**Diagnostic signal:** $\kappa_{\text{processing}} = I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-})/H(G_t \mid e_\tau, M_{\tau^-})$. Zero for Separated agents; near one for Coupled; intermediate for Partial.

**Repair operation:** Class 2 (Partial) approximation quality scales with $\kappa_{\text{processing}}$. Class 3 (Coupled) agents require the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without $(M_t, G_t)$ decomposition — the scope of `03-llm-core/`. At the system level, Class 3 (Coupled) components can be wrapped in modular topology (separate observation processing, external monitoring — see `#der-directed-separation` Working Notes on the IDT pattern).

### 2. Causal sufficiency: no latent common causes among strategy nodes

**Statement:** Every common cause of two or more nodes in $\Sigma_t$ is itself a node in $\Sigma_t$.

**Where it appears:** #deriv-graph-structure-uniqueness (precondition for the CMC-based Markov proof); #def-strategy-dag edge-independence in status propagation; all of Section II's strategy-layer formal results (Props B.1–B.6, the sector condition transfer of B.5, persistence of $\delta_s$).

**Failure regime:** The dominant real-world case in complex, multi-stakeholder, or adversarial environments — shared infrastructure, market conditions, correlated adversary actions, common-mode risks, supply-chain dependencies.

**Diagnostic signal:** Pairwise covariance among sibling edges after edge credences have converged. Positive covariance rejects the independence hypothesis and localizes where a common cause is missing. See #der-causal-insufficiency-detection.

**Repair operation:** L1 augmentation — add common-cause nodes and restructure the DAG so each common cause is factored *above* the correlation it creates ( #def-strategy-dag Correlation Hierarchy; #deriv-edge-credence-dynamics Prop B.6). L0 formal results transfer exactly to correctly constructed L1 DAGs because L1 restores causal sufficiency by construction. The orient cascade's step 4c triggers this escalation.

### 3. Channel independence: observation channels contribute non-redundant correction

**Statement:** $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ with each channel contributing independently to effective tempo.

**Where it appears:** #def-adaptive-tempo (core definition); inherited by #result-persistence-condition, #result-adversarial-tempo-advantage, #der-team-persistence (communication tempo), #der-tempo-composition, and any result using scalar $\mathcal{T}$.

**Failure regime:** Any system with redundant or correlated information sources — overlapping sensors, correlated teammate reports, redundant telemetry. In multi-agent settings, allies reporting the same intelligence source.

**Diagnostic signal:** $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$ — pairwise mutual information between event streams conditioned on prior model state. Non-zero mutual information signals redundancy.

**Repair operation:** Under correlation, $\mathcal{T}$ satisfies a strict inequality: $\mathcal{T} \leq \sum_k \nu^{(k)}\eta^{(k)\ast}$, with equality iff channels are informationally independent. The additive formula is an upper bound. For precise tempo, the effective capacity must account for mutual information between channels. Propagates as a redundancy penalty into every segment using scalar tempo.

### 4. Unity-dimension independence: $(U_M, U_O, U_\Sigma, U_{\text{obs}})$ substantially independent

**Statement:** The four unity dimensions of #def-unity-dimensions parametrize composite quality along substantially independent axes.

**Where it appears:** #def-unity-dimensions framing; #result-unity-closure-mapping's rate-distortion family indexed by each unity separately.

**Failure regime:** Shared models enable implicit strategic coordination (high $U_M$ → high $U_\Sigma$ without explicit policy sharing); aligned objectives often induce strategic coordination. Also *update-rule heterogeneity* (an axis not covered by any unity dimension) contributes to closure defect independently — the two-Kalman non-degenerate case shows $\varepsilon_x \gt 0$ from differing Kalman gains at perfect $U_M$.

**Diagnostic signal:** No clean one. The hypothesis is empirical and the theory currently logs it as working-position rather than resolved (see #def-unity-dimensions Working Notes: update-heterogeneity gap).

**Repair operation:** Two options explored in the theory: (a) accept a two-axis structure (unity × homogeneity) for closure defect, (b) add a fifth update-homogeneity dimension. The current working position is (a); formal resolution open. Downstream uses of unity dimensions should not treat them as cleanly orthogonal.

### 5. Independent edge outcomes in AND/OR propagation

**Statement:** In $\hat P_\Sigma$ status propagation, sibling edge outcomes are independent given their parents.

**Where it appears:** #def-strategy-dag status propagation formula; #scope-and-or; every downstream quantity computed from $\hat P_\Sigma$ (satisfaction gap, control regret via $A_O$, strategy-plan-confidence error $\delta_s$).

**Failure regime:** Same as causal sufficiency (item 2) — the CMC theorem makes them the same condition: causal sufficiency ⟺ exogenous noise independence ⟺ edge-outcome independence. When one fails, they all fail.

**Diagnostic signal:** Same as item 2.

**Repair operation:** Same as item 2 (L1 augmentation). The assumption is not a separate modeling choice from causal sufficiency; the theory treats it as the *consequence* of causal sufficiency (via CMC), not an independent axiom.

### 6. Scalar tempo / isotropic correction

**Statement:** $\mathcal{T}$ as a scalar captures the agent's correction capacity.

**Where it appears:** #result-persistence-condition linear operational form; most Section I results stated in scalar $(\mathcal{T}, \rho, \lVert\delta_{\text{critical}}\rVert)$ form; #def-strategic-tempo aggregate.

**Failure regime:** Any real multi-dimensional system with non-uniform correction capacity across dimensions. Simulation confirms scalar $\rho/\mathcal{T}$ overestimates by up to 72% in anisotropic systems, with the weak dimension accounting for 84% of total mismatch.

**Diagnostic signal:** Gain variation across dimensions (easily computable when gains are explicit — Kalman, gradient descent with diagonal preconditioning).

**Repair operation:** Per-dimension persistence: $\mathcal{T}_k \gt \rho_k/\lVert\delta_{\text{critical},k}\rVert$ for each dimension. See #result-per-dimension-persistence. The weakest dimension is the bottleneck. Same structural pattern propagates to strategic tempo ( #def-strategic-tempo Per-edge persistence) — the bottleneck edge determines persistence, not the aggregate.

---



## Discussion: Approximation Tiering

- **Slug**: `disc-approximation-tiering`
- **Type**: discussion
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `def-value-object`, `form-composition-closure`

AAT uses a recurring meta-pattern for handling intractability: when a problem admits no tractable exact treatment in general, introduce a tiered hierarchy of approximations with proved monotonicity between tiers and a diagnostic for ascending when needed. Three such hierarchies exist in the theory — the Correlation Hierarchy (L0/L1/L2) in #def-strategy-dag, the Convention Hierarchy (C1/C2/C3) in #def-value-object, and the Tier 1/2/3 contraction taxonomy in #form-composition-closure. This segment articulates the pattern explicitly, identifies what makes a successful approximation tiering, and notes where other scattered simplifications might fit the same shape.

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

---



## Discussion: Compression Operations in AAT

- **Slug**: `disc-compression-operations`
- **Type**: discussion
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `form-information-bottleneck`, `form-strategy-complexity-cost`, `def-shared-intent`, `form-composition-closure`, `def-chronica`

AAT contains four compression operations — the epistemic model $M_t$, the strategy DAG $\Sigma_t$, shared intent $G_t^{\text{shared}}$, and the composition projection $\Lambda$ — each formulated in its own segment with its own objective. Three of the four are written in Information Bottleneck (IB) form already; the fourth is stated as an IB constraint. This segment makes the shared shape explicit, promotes one underspecified source (the ontologically ambiguous "true causal structure" for $\Sigma_t$) to a cleaner formulation parallel to $M_t$, and establishes that composition admissibility (P1) is the Lagrangian-dual of a standard IB objective. It does *not* claim the four operations reduce to a single optimization problem — cross-instance theorems do not follow from the shared shape alone, and several conditions (Lipschitz regularity (P2), dimensional reduction (P3) in the Gaussian case, interventional relevance for Level-2 edges) remain outside the IB frame.

### The shared IB shape

*[Discussion (ib-shape)]*

Every compression operation in AAT has an objective or constraint of the form:

$$T^\ast = \arg\min_{T \mid X}\; \bigl[\, I(X; T) \;-\; \beta \cdot I(T; Y) \,\bigr]$$

with the Markov chain $Y - X - T$. The four AAT instances specialize this with different bindings:

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
2. **The "source" is not an AAT object.** To fit the IB shape, the objective implicitly treats $\Sigma_t$ as a compression of "the true causal structure." That structure is not part of AAT's ontology — the agent never has access to it; it is only ever implicit.

**Reformulation.** Treat $\Sigma_t$ as a compression of $\mathcal C_t$ (the interaction history — the agent's only evidence) *for decision-relevance*, parallel to $M_t$ which is a compression of $\mathcal C_t$ *for prediction-relevance*:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t}\; \bigl[\, I(\mathcal C_t; \Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

Under this reformulation:

- The source $\mathcal C_t$ is a well-defined AAT object, shared with the $M_t$ instance.
- The two instances differ cleanly in relevance variable: $M_t$ is compressed for prediction ($Y = o_{t+1:\infty} \mid a$); $\Sigma_t$ is compressed for guidance ($Y = \pi^\ast \mid M_t$). Prediction is about *what will happen*; guidance is about *what to do*. Both are computed from the same history, with different targets.
- The information cost $I(\mathcal C_t; \Sigma_t)$ replaces $\operatorname{DL}(\Sigma_t)$ as the theory-level compression term. The DL formulation remains useful as an *operational* cost measure for specific DAG encodings; it is not the theoretical quantity the IB objective minimizes.

**Relationship between the two cost measures.** Under MDL with a specific encoding scheme for DAGs (the one in #form-strategy-complexity-cost), $\operatorname{DL}(\Sigma_t)$ is an upper bound on $I(\mathcal C_t; \Sigma_t)$ for DAGs produced by the given encoder — coding cost dominates distinguishability cost. In practice, DL is computable and $I$ is not, so the operational minimization uses DL as a proxy; the theoretical minimization uses $I$. The IB objective above is the theoretical statement; the DL-based minimization in #form-strategy-complexity-cost remains the practical one.

**Variational form.** The Shannon mutual information $I(\Sigma_t; \pi^\ast \mid M_t)$ in the relevance term collapses to zero when $\pi^\ast$ is deterministic-from-$M_t$. The variational form (cf. #form-strategy-complexity-cost) replaces the relevance term with the KL-divergence $D_{\mathrm{KL}}(\pi^\ast(\cdot \mid M_t) \,\Vert\, Q_{\Sigma_t}(\pi \mid M_t))$ — note the $\pi^\ast$-first direction, which is *forced* by a regret-bound derivation (full derivation and admissible-divergence family analysis in #deriv-strategy-cost-regret-bound). Under bounded value range and deterministic $\pi^\ast$, Pinsker's inequality gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast\Vert Q_{\Sigma_t})}$ where $R$ is the strategy-induced regret against $\pi^\ast$; the opposite KL direction is vacuous ($+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass). The $\pi^\ast$-first KL is well-defined and graded under deterministic $\pi^\ast$. Under the variational reading, the AAT $\Sigma_t$ is a tractable approximation of the policy-relevant posterior, and the KL term measures approximation quality — aligning the strategy compression with the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020). The direction alignment is convergent: both AAT's regret-bound and active inference's variational-free-energy derivations pick $\pi^\ast$-first KL (reverse-KL in the variational-inference vocabulary), with AAT's additional interpretation being an upper-regret-bound rather than free-energy-gradient. The shared-IB-shape framing of the four AAT compression operations is the rate-distortion specialization of this variational picture; AAT's commitment is to the rate-distortion form (which gives the (P1) Lagrangian-dual derivation and the four-instance unification at U-medium), not to the full variational free-energy interpretation.

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

---



## Discussion: The Stability Certificate — One Object Behind the Cross-Sectional Meta-Patterns

- **Slug**: `disc-stability-certificate`
- **Type**: discussion
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `result-certificate-existence`, `result-sector-persistence-template`, `deriv-sector-condition`

AAT's cross-sectional structure is the geometry of a single object — the **equilibrium stability certificate**, the positive-definite form whose existence certifies that an agent can correct itself faster than its world drifts; operator-sector is that object's interior, the separability pattern its scope of existence, additive-coordinate-forcing its forced identity, and the identifiability floor its boundary, with composition the question of whether it survives projection.

The three meta-segments #disc-separability-pattern, #disc-identifiability-floor, and #disc-additive-coordinate-forcing read, separately, as three independent organizing insights that happen to recur. This segment names the object they are facets of. The relationship is the same one #disc-additive-coordinate-forcing already runs at smaller scale ("layer-specific manifestations of a single geometric object"), raised to the framework: not a fourth meta-pattern *alongside* the three, but the spine the three are projections of.

### The object

*[Definition (stability-certificate)]*

For an agent with error dynamics $\dot e=-F(e)$ about an equilibrium $e^\ast$ ($F(e^\ast)=0$, $F\in C^1$ near $e^\ast$, Jacobian $J:=DF(e^\ast)$), a **stability certificate** is a symmetric positive-definite $\mathcal M$ for which the one-point sector condition holds in the $\mathcal M$-inner-product on a ball $\mathcal B_R(e^\ast)$:

$$\langle F(e),\,e-e^\ast\rangle_{\mathcal M}\;\ge\;\kappa\,\lVert e-e^\ast\rVert_{\mathcal M}^2,\qquad \kappa\gt0. \tag{C}$$

The certificate is not unique: it is whatever positive-definite form makes the dynamics contract. In the recurring sub-cases it specializes — to the Fisher information for Bayesian agents, to $(P^-)^{-1}$ for Kalman agents, to the loss Hessian for gradient agents, and to a plant-selected Lyapunov metric for linear-Hurwitz or PID agents. These are not four separate stories; they are one object under four certificates.

### The anchor

*[Result (cited: #result-certificate-existence)]*

The object is load-bearing only because its existence is not a definition but an equivalence: **a stability certificate exists iff the agent is exponentially stable about its target** — operator-sector in *some* inner product and exponential stability are the same statement, with the certificate as the converse-Lyapunov witness, and the certificate admits a strict strength ladder R0 ⟸ R1 ⟸ R2 (widest one-point/local; cocoercive; Čencov-forced). This is the segment-level form of the contraction-over-drift organizing principle. The equivalence, the ladder, and the proof are stated and derived exactly in #result-certificate-existence; this spine cites that result and builds the cross-sectional reading on it rather than re-deriving it.

### The four facets

*[Discussion]*

The certificate is one object; the cross-sectional meta-patterns are its facets on the positive-semidefinite cone $\mathbb S^n_{\succeq0}$:

| Facet | Meta-segment | What the facet is | Canonical home |
|---|---|---|---|
| **Interior** | #result-sector-persistence-template, #result-contraction-template | $\mathcal M\succ0$ on the scope ball: the contraction holds | the template segments |
| **Scope of existence** | #disc-separability-pattern | the region where a certificate exists at all (separable core / structured repair / general open) | M2 |
| **Forced identity** | #disc-additive-coordinate-forcing | *which* certificate: Čencov forces $\mathcal M=$ Fisher uniquely in statistical scope; matched (existence-only) elsewhere | M3 |
| **Boundary** | #disc-identifiability-floor | $\mathcal M$ drops rank ($\partial\mathbb S^n_{\succeq0}$): the inferential task is structurally impossible | M1 |
| **Projection behaviour** | #form-composition-closure | whether a *common* certificate survives coarse-graining; the closure defect $\varepsilon^\ast$ is the certificate's projection-residue | composition-closure |

Each meta-segment retains its own canonical home and per-instance derivations; this segment claims only the recognition that they are facets of one object, and what that buys (Discussion below).

### The three obstructions are distinct — the plurality is the content

*[Discussion]*

A tempting reading is that the certificate's failures are one obstruction seen three ways (a single "failure of integrability"). They are not. The three failure modes are irreducibly distinct, each invariant under the others' degrees of freedom:

- **Forced-identity failure — Helmholtz–Hodge.** $J$ non-symmetric ⟹ the field is not a gradient ⟹ no potential ⟹ the certificate is *matched* (converse-Lyapunov existence), not *forced* (Čencov). A non-symmetric Hurwitz $J$ still has a certificate (it is *not* on the boundary), so this is an M3 failure, not an M1 one. Invariant: symmetry of $J$.
- **Existence failure — Sylvester's law of inertia.** The certificate drops rank. Every coordinate/metric change acts on the certificate by congruence; congruence preserves inertia; so a rank-deficient certificate is rank-deficient in *every* coordinate. The boundary is invariant under the agent's entire representational freedom (that freedom *is* the congruence orbit); the only escape is rank-augmentation — genuinely new information, not a re-mapping. (Detailed in #disc-identifiability-floor's Sylvester finding.) Invariant: inertia under congruence.
- **Projection failure — Mori–Zwanzig / Schur.** Coarse-graining is a non-invertible projection. The certificate-as-metric survives (the Schur complement of a positive-definite form is positive-definite) but the *dynamic* guarantee does not: the closure defect $\varepsilon^\ast$ equals the norm of the Mori–Zwanzig memory commutator, zero exactly when the resolved subspace is $J$-invariant. Invariant: $J$-invariance of the resolved subspace.

Each obstruction is untouched by the others' freedoms: a metric change does not fix non-invariance; projection does not fix non-symmetry; rank-augmentation does not fix a memory kernel. That mutual invariance is the reason the cross-sectional structure is *several* meta-patterns and not one — stated as a structural fact rather than left as "they are different concerns."

---



## Derivation: Observation-Ambiguity Bias-Bound Constant $C$

- **Slug**: `deriv-observation-ambiguity-bias-bound`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `scope-agent-identity`, `disc-additive-coordinate-forcing`, `der-directed-separation`, `form-information-bottleneck`, `disc-compression-operations`

The observation-ambiguity bias bound carried by Class 3 (Coupled) agents in the logogenic-agents scope — $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ ([#scope-observation-ambiguity-modulation](../../03-llm-core/src/scope-observation-ambiguity-modulation.md), [#result-section-ii-survival](../../03-llm-core/src/result-section-ii-survival.md)) — previously treated the constant $C$ as "domain-dependent" and the bound as "order-of-magnitude guidance, not a theorem." This appendix derives $C$ under two named sub-scopes, records a no-go showing that $C$ cannot be universal without the (PI) parameterization-invariance axiom of [#scope-agent-identity](scope-agent-identity.md), and documents two failed derivation routes so future agents do not repeat them.

### §1 — Setup and the audit before strengthening

Let $M_{\tau^-} \in \mathcal M$ be the pre-update epistemic substate. Let $e_\tau$ be the event triggering update, $G_t$ the goal substate, and $\Omega_\tau$ the latent world-state. In Class 1 (Separated) scope, [#der-directed-separation](der-directed-separation.md) guarantees the update $f_M(M_{\tau^-}, e_\tau)$ is goal-blind: $M_{\tau^+}^{\text{decoupled}} = f_M(M_{\tau^-}, e_\tau)$. In Class 3 (Coupled) scope, the coupled update $f_X^M(X_{\tau^-}, e_\tau)$ carries goal-conditional reweighting; the bias is

$$\Delta M_{\text{bias}} := f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$$

**Pre-strengthening type audit.** For the bound "$\lVert \Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I$" to be well-typed:

1. **Norm on $\mathcal M$.** The LHS is a norm on model-space. $\mathcal M$ is the model space of [#form-agent-model](form-agent-model.md). Three candidate norms: Euclidean on parameters, total variation on induced measures, Fisher-Rao geodesic distance. **Under the (PI) parameterization-invariance axiom in [#scope-agent-identity](scope-agent-identity.md)** (fourth primary instance of [#disc-additive-coordinate-forcing](disc-additive-coordinate-forcing.md)), Euclidean-on-parameters is a coordinate artifact and Fisher-Rao is the canonical AAT-invariant choice on statistical-manifold sub-cases of $\mathcal M$ (Čencov 1982 uniqueness).

2. **Regularity of $f_X^M$.** For the bound to be a theorem, $f_X^M$ must satisfy some regularity. The Bayesian-posterior model (prior + likelihood reweighting) is the canonical working class; it covers the attention-reweighting mechanism typical of Class 3 (Coupled) architectures to leading order.

3. **Information coordinate.** $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is in nats (or bits). Converting information to state-distance is exactly what the Pinsker / Bretagnolle-Huber / Otto-Villani / Bakry-Émery machinery does.

The bound is well-typed under (a) named norm, (b) bounded $f_X^M$ regularity, (c) specified information-geometric inequality. Without (PI) adopted, $C$ is norm-dependent; under (PI), Fisher-Rao is canonical and $C$ becomes derivable.

### §2 — Track 1: Transport-inequality derivation under log-Sobolev + Lipschitz-posterior

*[Derived (w2-transport-track, conditional on H1-H3)]*

**Named sub-scope (H1-H3).**

- **(H1) Statistical-manifold sub-case.** Each $M_t \in \mathcal M$ corresponds to a probability distribution $P_{M_t}$ over world-states. $\mathcal M$ is (locally) a statistical manifold.
- **(H2) Log-Sobolev inequality.** The observation distribution $P_{\Omega \mid e, M}$ satisfies a log-Sobolev inequality (LSI) with constant $\rho_{\text{LSI}} \gt 0$. Sufficient condition: $P_{\Omega \mid e, M}$ is strongly log-concave with constant $K$ (Bakry-Émery 1985 curvature-dimension condition gives $\rho_{\text{LSI}} \geq K$). For Gaussian observation models, $\rho_{\text{LSI}} = 1/\sigma^2$ explicitly.
- **(H3) Lipschitz-posterior stability.** The Bayesian-posterior pushforward from observation to state is $L_{\text{post}}$-Lipschitz in $W_2$:

    $$W_2(P_{M \mid e, G}, P_{M \mid e}) \leq L_{\text{post}} \cdot W_2(P_{\Omega \mid e, G}, P_{\Omega \mid e})$$

    Sufficient condition: well-posed Bayesian inverse problem with bounded log-likelihood Hessian (Stuart 2010 *Inverse problems: a Bayesian perspective*, *Acta Numerica* 19:451–559, Theorem 4.6; Hairer, Stuart & Vollmer 2014 *SIAM J. Math. Anal.* 46(1):415–451 for explicit $W_2$-bounds in infinite-dimensional settings).

**Step 1 — KL from mutual information.** By the chain rule of relative entropy (Cover & Thomas 2006 Theorem 2.5.3):

$$\mathbb E_G\bigl[\mathrm{KL}\bigl(P_{\Omega \mid e, M, G} \,\Vert\, P_{\Omega \mid e, M}\bigr)\bigr] = I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

*Exact identity.*

**Step 2 — Otto-Villani under LSI.** From (H2) and Otto & Villani 2000 *J. Funct. Anal.* 173(2):361–400 Theorem 1:

$$W_2^2\bigl(P_{\Omega \mid e, M, G}, P_{\Omega \mid e, M}\bigr) \leq \tfrac{2}{\rho_{\text{LSI}}} \cdot \mathrm{KL}\bigl(P_{\Omega \mid e, M, G} \,\Vert\, P_{\Omega \mid e, M}\bigr)$$

Taking expectation over $G$ and substituting Step 1:

$$\mathbb E_G\bigl[W_2^2(P_{\Omega \mid e, M, G}, P_{\Omega \mid e, M})\bigr] \leq \tfrac{2}{\rho_{\text{LSI}}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

**Step 3 — Lipschitz-posterior pushforward.** From (H3):

$$\mathbb E_G\bigl[W_2^2(P_{M \mid e, G}, P_{M \mid e})\bigr] \leq L_{\text{post}}^2 \cdot \mathbb E_G\bigl[W_2^2(P_{\Omega \mid e, G}, P_{\Omega \mid e})\bigr]$$

**Step 4 — $\kappa_{\text{processing}}$ factor.** The $\kappa_{\text{processing}}$ coefficient from [#der-directed-separation](der-directed-separation.md)'s Class 1/2/3 (Separated/Partial/Coupled) taxonomy multiplies the goal-conditional reweighting strength by the modularity coefficient. For Class 3 (Coupled), $\kappa_{\text{processing}} \approx 1$; for Class 2 (Partial) with modularity $\kappa$, the effective bound carries a factor $\kappa$ multiplicatively on the information term.

**Result (Track 1).** *[Derived, conditional on (H1)-(H3)]*

$$\boxed{\;\mathbb E\bigl[W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})\bigr] \;\leq\; \frac{2 L_{\text{post}}^2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})\;}$$

**The constant is explicit:** $C_{W_2}^2 = 2 L_{\text{post}}^2 / \rho_{\text{LSI}}$, linear in $I$, with geometric interpretation:

- $L_{\text{post}}$ grows with *prior-likelihood tension* — ill-conditioned inverse problems amplify bias.
- $\rho_{\text{LSI}}$ grows with *observation-distribution concentration* — sharper observations yield tighter bounds.
- The ratio $2 L_{\text{post}}^2 / \rho_{\text{LSI}}$ captures the **geometric stiffness** of the update: small-$\rho$/large-$L$ = soft, goal-sensitive updates; large-$\rho$/small-$L$ = stiff updates that resist goal-bias.

### §3 — Track 2: Fisher-Rao derivation under (PI) + Čencov + small-information regime

*[Derived (fisher-rao-track, conditional on H1 + H4)]*

**Named sub-scope (H1 + H4).**

- **(H1) Statistical-manifold sub-case** — as in §2. Under the (PI) parameterization-invariance axiom of [#scope-agent-identity](scope-agent-identity.md), Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS) forces the Fisher information metric as the canonical Riemannian metric on $\mathcal M$ up to global scale (Ay, Jost, Lê & Schwachhöfer 2017 *Information Geometry*, Theorem 5.1).
- **(H4) Small-information regime.** $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \ll 1$ nat. The second-order Taylor expansion of KL at coincident distributions is sharp.

**Step 1 — KL-to-Fisher-squared-distance identity.** For nearby distributions $P$, $Q$ on a statistical manifold with Fisher metric $\mathbf I$, the KL divergence admits the second-order expansion

$$\mathrm{KL}(P \Vert Q) \;=\; \tfrac{1}{2} \cdot d_{FR}^2(P, Q) + O(d_{FR}^3)$$

where $d_{FR}$ is the Fisher-Rao geodesic distance (Cover & Thomas 2006 §12.5; Amari & Nagaoka 2000 §3.7 Theorem 3.1). This is the infinitesimal form of the Bregman divergence on the exponential family's dual geometry (cf. [#deriv-strategy-cost-regret-bound](deriv-strategy-cost-regret-bound.md) §6.3 for the related Fenchel-Bregman identification).

**Step 2 — Posterior-displacement in Fisher-Rao.** Under (H1)+(H4) + Bayesian-posterior-class $f_X^M$, the goal-conditional posterior and goal-marginalized posterior are nearby points on the statistical manifold; their Fisher-Rao distance satisfies

$$d_{FR}^2\bigl(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}}\bigr) \;\leq\; 2 \cdot \mathrm{KL}\bigl(P_{M \mid e, G} \,\Vert\, P_{M \mid e}\bigr) + O(d_{FR}^3)$$

Using the data-processing inequality $\mathrm{KL}(P_{M \mid e, G} \Vert P_{M \mid e}) \leq \mathrm{KL}(P_{\Omega \mid e, G} \Vert P_{\Omega \mid e})$ (Bayesian posterior is a pushforward), and Step 1 of §2 ($\mathbb E_G[\mathrm{KL}(P_{\Omega \mid e, M, G} \Vert P_{\Omega \mid e, M})] = I$):

$$\mathbb E\bigl[d_{FR}^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})\bigr] \;\leq\; 2 \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \cdot (1 + o(1))$$

**Step 3 — Taking square roots (with $\kappa$ factor).** Under Class 2 (Partial) modularity, $\kappa_{\text{processing}}$ enters multiplicatively on the goal-conditional reweighting strength, hence on the KL and Fisher-Rao distance:

**Result (Track 2).** *[Derived, conditional on (H1)+(H4), small-information regime]*

$$\boxed{\;\mathbb E\,\lVert\Delta M_{\text{bias}}\rVert_{FR} \;\leq\; \sqrt{2} \cdot \sqrt{\kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))\;}$$

**The constant is universal and dimension-free:** $C_{FR} = \sqrt{2}$ (nats) or $\sqrt{2 \ln 2}$ (bits). **No domain-specific parameters.** The (PI) commitment eliminates the coordinate-dependence that made $C$ ambiguous under Euclidean-parameter norms.

**Scaling difference between tracks.** Track 1 gives $W_2^2 \propto I$ (linear in information). Track 2 gives $d_{FR}^2 \propto I$, equivalently $d_{FR} \propto \sqrt I$ (square-root in information). The two tracks are not contradictory — they are bounds under different assumptions in different metrics. Track 1 is tight in the large-$I$ regime where Otto-Villani's linear form dominates; Track 2 is tight in the small-$I$ regime where the Fisher-metric second-order expansion is sharp. The two compose at intermediate scales by taking the tighter of the two under the local curvature conditions.

### §4 — No-go result: universal $C$ under Euclidean-parameter norm fails

*[Proved (no-universal-C-euclidean, counterexample-grade)]*

**Claim.** No universal constant $C$ — independent of $\mathcal M$'s geometry, parameterization, and coupled-update structure — exists such that $\lVert\Delta M_{\text{bias}}\rVert_{\text{Euclidean}} \leq C \cdot \kappa \cdot I$ under the Euclidean norm on an arbitrary parameter vector.

**Counterexample.** Let $\mathcal M = \{N(0, \sigma^2) : \sigma \gt 0\}$ parameterized by $\sigma$. The Fisher information in $\sigma$ scales as $\mathbf I(\sigma) = 2/\sigma^2$ — small near large $\sigma$, large near small $\sigma$. For any $C_0 \lt \infty$, choose $\sigma_0$ large enough that the Fisher-Rao displacement corresponding to $I(G; \Omega) = 1$ nat of goal-conditional reweighting translates to Euclidean-$\sigma$ displacement $\sigma_0 / \sqrt{2} \gt C_0$. Specifically, by Track 2's $\sqrt 2$ bound:

$$d_{FR}(M^{\text{coupled}}, M^{\text{decoupled}}) \leq \sqrt 2 \cdot 1 = \sqrt 2$$

Under the Fisher metric $\mathbf I(\sigma) = 2/\sigma^2$, the Fisher-Rao line element is $ds^2 = 2 d\sigma^2/\sigma^2$, so $\Delta\sigma \approx \sigma \cdot d_{FR}/\sqrt 2 = \sigma$ (Euclidean displacement scales linearly in $\sigma$). Taking $\sigma \to \infty$ gives arbitrarily large Euclidean-$\sigma$ displacement for fixed $I = 1$ nat. No universal $C$ in Euclidean-parameter norm exists.

**Implication.** The no-go strengthens the (PI) commitment rather than weakening the bound: **under (PI), Fisher-Rao is the canonical norm and $C = \sqrt 2$ is universal; without (PI), $C$ does not exist as a universal constant.** The (PI) axiom is *load-bearing* for this derivation, not coincidental.

**Position relative to [#disc-identifiability-floor](disc-identifiability-floor.md).** The no-go has the shape of a floor-pattern no-go (external obstruction: Euclidean-parameter norms carry unbounded Fisher condition numbers; escape: (PI) + Fisher-Rao gives universal $C$), but it does not match the five-element test for a floor instance (see [#disc-identifiability-floor](disc-identifiability-floor.md)): it has a *single* escape (the (PI) adoption), not ≥ 2 distinct escapes, and its strengthened consequence is *re-use* of existing (PI)+Čencov machinery (fourth primary instance of [#disc-additive-coordinate-forcing](disc-additive-coordinate-forcing.md)) rather than elevation of new machinery. The honest position: this no-go is a **downstream theorem of the (PI) commitment**, not a new floor instance. It belongs in this appendix as motivating justification for why (PI) is load-bearing for the derivation, not as a separate meta-segment entry. (Triage detail in `spikes/spike-identifiability-floor-instance-triage-2026-04-24.md`.)

### §5 — Failed derivation routes (honest record)

Two derivation routes were attempted and failed at a structural level. Documented here so future agents do not re-attempt them without new evidence.

**(F1) Cramér-Rao inversion — wrong direction.** Attempt: treat $G$ as a parameter estimated from $\Omega$ given $(e, M)$; use the Cramér-Rao lower bound $\mathrm{Var}(\hat G) \geq \mathbf I_G^{-1}$ inverted to bound $\lVert\Delta M_{\text{bias}}\rVert \leq L_M \cdot \sqrt{\mathbf I_G^{-1}}$ via a posterior-sensitivity factor. Failure: Cramér-Rao bounds estimator error *below*, not above; the bound goes in the opposite direction to what the bias bound needs. Inverting Cramér-Rao for an upper bound on bias propagation requires a fixed-estimator-class assumption that is not available for a Class 3 (Coupled) agent's attention-reweighting mechanism. The transport-inequality route of §2 is the correct machinery.

**(F2) Rate-distortion inversion — wrong problem structure.** Attempt: apply Shannon's rate-distortion inequality $R(D) \geq h(X) - \tfrac{1}{2}\log(2\pi e D)$ (Gaussian source), invert to $D \leq \sigma^2 \cdot 2^{-2(R - h(X))}$ with "bits in" = $I(G; \Omega \mid e, M)$. Failure: rate-distortion theory describes the minimum bits-per-symbol required to represent a source within distortion $D$; it does **not** describe the maximum distortion induced by injecting side-information into an update. Source-coding theorems are about optimal representations of a source, not spatial displacement induced by side-information injection. The direction is again wrong. Transport inequalities (Attempt B) are the correct machinery.

The pattern shared across (F1) and (F2): **information-theoretic source-coding theorems (Cramér-Rao bounds, rate-distortion lower bounds) are structural lower-bound machinery for an estimator's or encoder's performance; they cannot be inverted to produce upper bounds on displacement induced by side-information.** Upper bounds on displacement require transport-inequality machinery (Pinsker, Otto-Villani, Bakry-Émery, posterior-stability).

### §6 — Gaussian worked example

*[Illustrative, exact under specified assumptions]*

**Setup.** Gaussian observation model $P_{\Omega \mid e, M} = N(\mu_M, \sigma^2 I)$ with fixed $\sigma^2$; conjugate-Gaussian prior $P_{M} = N(0, \tau^2 I)$; goal-conditional likelihood reweighting $P_{\Omega \mid e, M, G} = N(\mu_M + \beta(G), \sigma^2 I)$ where $\beta(G)$ is a goal-dependent shift with $\lVert\beta(G)\rVert^2$ bounded by the information budget $I(G; \Omega_\tau)$.

**LSI constant.** Gaussian $N(\mu, \sigma^2 I)$ satisfies LSI with $\rho_{\text{LSI}} = 1/\sigma^2$ (Bakry-Émery; direct Hessian bound on $-\log p$).

**Posterior-Lipschitz constant.** Conjugate-Gaussian posterior: $P_{M \mid \Omega} = N(\mu_{\text{post}}, \Sigma_{\text{post}})$ with $\mu_{\text{post}} = \tau^2/(\tau^2 + \sigma^2) \cdot \Omega$. Lipschitz-in-$\Omega$ constant $L_{\text{post}} = \tau^2/(\tau^2 + \sigma^2) \lt 1$. Under $W_2$-Lipschitz (Hairer-Stuart-Vollmer 2014), $L_{\text{post}} \leq 1$ for well-conditioned priors.

**Track 1 bound (numerical).** $C_{W_2}^2 = 2 L_{\text{post}}^2 / \rho_{\text{LSI}} = 2 \sigma^2 \cdot \tau^4/(\tau^2 + \sigma^2)^2$. In the prior-dominant limit ($\tau^2 \ll \sigma^2$): $C_{W_2}^2 \approx 2 \tau^4/\sigma^2$ (tight prior amplifies bias). In the likelihood-dominant limit ($\sigma^2 \ll \tau^2$): $C_{W_2}^2 \approx 2 \sigma^2$ (sharp observations limit bias).

**Track 2 bound (numerical).** Under (PI) + Fisher-Rao on the Gaussian mean-manifold with metric $\mathbf I(\mu) = I/\sigma^2$: $d_{FR}(\mu_1, \mu_2) = \lVert\mu_1 - \mu_2\rVert/\sigma$. Under small-$I$: $\mathbb E\,d_{FR}(\Delta M_{\text{bias}}) \leq \sqrt{2 \cdot \kappa \cdot I}$. In Euclidean-on-$\mu$ norm: $\lVert\Delta\mu_{\text{bias}}\rVert \leq \sigma \cdot \sqrt{2 \kappa I}$ — the $\sigma$ prefactor is the Fisher-Rao-to-Euclidean conversion. The Euclidean form is coordinate-dependent (per Attempt E §4); Fisher-Rao form is universal.

**Comparison at operating point.** For $\tau = \sigma = 1$ (balanced): Track 1 gives $C_{W_2}^2 = 2 \cdot (1/4) = 1/2$, so $\mathbb E\,W_2 \leq \sqrt{I/2}$. Track 2 gives $\mathbb E\,d_{FR} \leq \sqrt{2I}$. The two are within a factor of 2 of each other at balanced scale; they diverge in the ill-conditioned limits where Track 1's $L_{\text{post}}$ or $\rho_{\text{LSI}}$ blows up while Track 2 remains dimension-free.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Chain-rule identity $\mathbb E_G[\mathrm{KL}(P_{\Omega\mid G}\Vert P_\Omega)] = I(G;\Omega\mid \cdot)$ | Cover & Thomas 2006 Theorem 2.5.3 | Exact |
| Pinsker's inequality $\lVert P-Q\rVert_{TV} \leq \sqrt{\tfrac{1}{2}\mathrm{KL}}$ | Standard (Csiszár-Körner) | Exact |
| Otto-Villani $W_2^2 \leq (2/\rho_{\text{LSI}})\mathrm{KL}$ under LSI | Otto & Villani 2000 Theorem 1; Bakry-Émery 1985 curvature-dimension for LSI | Exact |
| KL-to-Fisher-squared-distance $\mathrm{KL}(P\Vert Q) = \tfrac{1}{2}d_{FR}^2 + O(d_{FR}^3)$ | Cover-Thomas 2006 §12.5; Amari-Nagaoka 2000 §3.7 Theorem 3.1 | Exact (standard information geometry) |
| Bayesian-posterior $W_2$-Lipschitz stability $L_{\text{post}}$ | Stuart 2010 Theorem 4.6 under well-posed inverse problem | Conditional on (H3) |
| **Track 1 bound** $\mathbb E[W_2^2(M^{\text{coupled}}, M^{\text{decoupled}})] \leq (2L_{\text{post}}^2/\rho_{\text{LSI}}) \cdot \kappa \cdot I$ | Composition of §2 Steps 1–4 | **Derived (conditional on H1-H3)** |
| **Track 2 bound** $\mathbb E\,\lVert\Delta M_{\text{bias}}\rVert_{FR} \leq \sqrt{2} \cdot \sqrt{\kappa I}(1+o(1))$ | Composition of §3 Steps 1–3 under (PI) + Čencov | **Derived (conditional on H1+H4, small-$I$ regime)** |
| $C_{FR} = \sqrt{2}$ is universal, dimension-free, no domain constants | §3 Result | Exact under (H1)+(H4) |
| $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ with explicit geometric interpretation | §2 Result | Exact under (H1)-(H3) |
| Attempt E no-go: no universal $C$ in Euclidean-parameter norm | Heteroscedastic-normal counterexample §4 | Proved (counterexample-grade) |
| (F1) Cramér-Rao inversion fails | Direction mismatch (estimator lower bound cannot invert to upper bound) | Recorded failure |
| (F2) Rate-distortion inversion fails | Problem-structure mismatch (source-coding theorem cannot yield side-information injection bound) | Recorded failure |
| Gaussian worked example with explicit $C_{W_2}$ and $C_{FR}$ | Conjugate-Gaussian direct computation | Exact under specified assumptions |

The dividing line: both tracks are derived theorems under named hypotheses; the hypotheses (LSI, Lipschitz-posterior, small-$I$, statistical-manifold sub-case, (PI) adoption) are either standard mathematical regularity (LSI, Lipschitz-posterior) or AAT-internal axioms ((PI), already adopted in [#scope-agent-identity](scope-agent-identity.md) and elevated to fourth primary instance of [#disc-additive-coordinate-forcing](disc-additive-coordinate-forcing.md)). The no-go §4 justifies the (PI) commitment as load-bearing rather than coincidental. The failed attempts §5 document structural reasons two alternative routes cannot work, preventing future re-attempts.

---
