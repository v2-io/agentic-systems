    # Spike: Information Bottleneck Unification — Scoping and Sketch

**Status**: Scoping spike. No segments modified. This document surveys whether the four currently-separate compression framings in AAD reduce to instances of a single Information Bottleneck (IB) problem, parameterized by different relevance variables. The purpose is to decide whether the integration is worth executing — not to execute it.

**Date**: 2026-04-21

**Depends on**: `#form-information-bottleneck`, `#form-strategy-complexity-cost`, `#def-shared-intent`, `#form-composition-closure` (admissibility conditions P1-P3), `#result-unity-closure-mapping`, `spikes/spike-unity-closure-mapping.md` §6, `audits/opus-audit-2026-04-21.md` "Bigger-picture synthesis §4", `TODO-04-21.md` Session D.

**Deliverable**: decision input for whether to invest 3-5 sessions rewriting the four segments above as instances of a master IB schema.

---

## 1. The Unification Conjecture, Stated Formally

### 1.1 The master schema

*[Conjecture (IB-master)]*

Every compression operation in AAD is an instance of the same information-theoretic optimization, differing only in (a) the information source $X$, (b) the compressed representation $T$ that the operation produces, (c) the relevance variable $Y$ the compression is *for*, and (d) the scalar trade-off $\beta \gt 0$ between compression aggressiveness and relevance preservation. The master objective:

$$T^\ast = \arg\min_{T \mid X} \;\bigl[\, I(X; T) \;-\; \beta \cdot I(T; Y) \,\bigr]$$

with the Markov chain $Y - X - T$ (i.e., $T$ is a function of $X$ alone; $Y$ interacts with $T$ only through $X$). Four instances of this schema are candidate AAD operations: model compression ($M_t$), strategy compression ($\Sigma_t$), shared-intent compression ($G_t^{\text{shared}}$), and composition projection ($\Lambda$).

### 1.2 What the conjecture actually claims, at three strengths

The claim "these are all IB instances" is ambiguous. The scoping value of distinguishing strengths:

**(U-strong) Formal reduction.** The four compression operations are *the same optimization problem* with different $(X, T, Y, \beta)$ bindings. A single derivation, carried out once for the master schema, specializes to each instance by substitution. *[Hypothesis]*

**(U-medium) Shared pattern.** The four operations share the same *shape* — same objective structure, same variational calculus, same rate-distortion interpretation — but differ in substantive ways (e.g., what the "source" is, whether the compression is deterministic or stochastic, which constraints are active) that prevent a single derivation from covering all four. *[Discussion]*

**(U-weak) Useful analogy.** The four operations can be *written in IB form* as a presentational device — a unifying vocabulary — but the analytic work for each remains domain-specific. *[Discussion]*

Honest default: (U-medium) is almost certainly true (the IB shape is already visible in all four segments); (U-strong) requires specific conditions for each instance; (U-weak) is trivially true and not worth a session. The execution decision depends on whether (U-strong) is achievable for enough of the instances that the unification is load-bearing rather than cosmetic.

### 1.3 What (U-strong) would require

For each instance, the substitution $(X, T, Y, \beta) \mapsto$ (instance-specific objects) must be well-typed, and the minimizer of the master objective must coincide with the minimizer currently attributed to the instance. If the instance-specific optimization has additional constraints not present in the master schema — e.g., regularity, discreteness, causal structure — those must be either (a) derivable from the IB form with the stated $(X, T, Y, \beta)$, or (b) explicitly parked as *supplementary* conditions separate from the IB core. (P2) Lipschitz continuity in `#form-composition-closure` is a known example of (b) — it is a regularity condition that the IB objective does not impose and must remain separate.

---

## 2. The Four Candidate Instances Mapped to $(X, T, Y, \beta)$

Each instance is stated in the form in which it currently appears in the segments, and the candidate IB binding is given.

### 2.1 Model compression ($M_t$) — the canonical case

Current form (from `#form-information-bottleneck`):

$$\phi^\ast = \arg\min_\phi \bigl[\, I(M_t;\; \mathcal C_t) \;-\; \beta \cdot I(M_t;\; o_{t+1:\infty} \mid a_{t:\infty}) \,\bigr]$$

**Candidate binding.**

| Schema | Instance |
|---|---|
| $X$ | $\mathcal C_t$ (chronica — interaction history) |
| $T$ | $M_t$ (compressed model state) |
| $Y$ | $o_{t+1:\infty} \mid a_{t:\infty}$ (future observations conditional on future actions — the prediction target, policy-conditioned per `#form-information-bottleneck` Discussion) |
| $\beta$ | $\beta(\rho, \pi)$ — volatility- and policy-dependent trade-off |

*[Fit]* Clean. The instance matches the master schema verbatim. The conditional mutual information $I(T; Y \mid a_{t:\infty})$ instead of $I(T; Y)$ is a mild schema extension that the IB literature admits (conditional IB, Chechik et al. 2005).

**Tension.** None at the formulation level. The "source" $\mathcal C_t$ grows without bound as $t \to \infty$; the IB frontier for such a non-stationary source is time-varying, but this is already acknowledged in `#form-information-bottleneck` (and handled in practice by forgetting).

### 2.2 Strategy compression ($\Sigma_t$)

Current form (from `#form-strategy-complexity-cost`):

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \bigl[\, \operatorname{DL}(\Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

**Candidate binding.**

| Schema | Instance |
|---|---|
| $X$ | The "true causal structure" the strategy DAG approximates — call this $\Sigma^\ast$ or the causal environment structure |
| $T$ | $\Sigma_t$ (the agent's maintained DAG) |
| $Y$ | $\pi^\ast$ (optimal policy), conditional on $M_t$ |
| $\beta$ | $\beta_\Sigma$ |

*[Fit]* **Partial.** Two issues.

**Issue A: compression cost is DL, not $I(X; T)$.** The current segment uses *description length* $\operatorname{DL}(\Sigma_t)$ in place of the mutual information $I(\Sigma^\ast; \Sigma_t)$. Under MDL, these are related (description length is a coding cost, mutual information is a distinguishability cost), but they coincide only for specific coding schemes. Making the master binding exact would require either (a) reformulating the complexity cost as $I(\Sigma^\ast; \Sigma_t)$, abandoning the concrete DAG-encoding interpretation, or (b) treating $\operatorname{DL}(\Sigma_t)$ as an operational proxy for $I(X; T)$ and accepting the mismatch.

**Issue B: the "source" is not obviously an object in AAD's ontology.** Unlike $\mathcal C_t$ (which is a well-defined history), "the true causal structure" is at best a latent variable the agent never observes. In the model-compression case, the source is the actual history; in the strategy case, the source is a target the agent is approximating without direct access. This breaks symmetry with the canonical IB setup where $X$ is observed and $T$ is a function of $X$.

**Weaker, cleaner binding.** If we treat the "source" as $\mathcal C_t$ (interaction history — the agent's only evidence) and the "relevance variable" as action-outcome joint $\pi^\ast \mid M_t$, the binding becomes:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \bigl[\, I(\mathcal C_t; \Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

This puts $\Sigma_t$ as a compression of $\mathcal C_t$ *for* decision-relevance, parallel to $M_t$ as a compression of $\mathcal C_t$ *for* prediction-relevance. The two instances then differ cleanly in relevance variable: prediction ($Y = o_{t+1:\infty} \mid a$) versus guidance ($Y = \pi^\ast \mid M_t$). This is a cleaner fit and probably the right reformulation if the unification proceeds. *[Hypothesis]*

### 2.3 Shared intent ($G_t^{\text{shared}}$)

Current form (from `#def-shared-intent`):

$$G_t^{\text{shared}} = \arg\min_{G_s} \bigl[\, I(G_t^{\text{full}}; G_s) \;-\; \beta \cdot I(G_s; a_t^{\text{coordinated}}) \,\bigr]$$

**Candidate binding.**

| Schema | Instance |
|---|---|
| $X$ | $G_t^{\text{full}} = (O_t, \Sigma_t)$ — sender's full purposeful state |
| $T$ | $G_t^{\text{shared}}$ — compressed signal transmitted to partners |
| $Y$ | $a_t^{\text{coordinated}}$ — jointly optimal action |
| $\beta$ | Bandwidth/relevance trade-off |

*[Fit]* **Direct and clean** — this instance is already written in IB form, cites Tishby, and identifies the relevance variable explicitly. It is the cleanest of the four.

**Tension.** The relevance variable $a_t^{\text{coordinated}}$ is not observed by the sender (computing it requires knowing partners' states); see `#def-shared-intent` Epistemic Status for the honest caveat. This is a practical issue for instantiation, not a schema-fit issue — the IB setup permits any $Y$ the compressor is trying to preserve, whether or not the compressor has direct access to $Y$. The Working Note about multi-dimensional relevance (coordination plus conflict resolution plus replanning) is a substantive extension but not a schema violation: IB with a vector-valued relevance variable is standard.

### 2.4 Composition projection admissibility (P1 in `#form-composition-closure`)

Current form (from `#form-composition-closure` (P1)):

$$I\bigl(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\bigr) \geq (1 - \epsilon_I) \cdot I\bigl(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\bigr)$$

This is a *constraint*, not an objective. To map it to the master schema, we reformulate (P1) as characterizing projections on the IB frontier for the relevance variable "next observation given action."

**Candidate binding.**

| Schema | Instance |
|---|---|
| $X$ | $X_{\text{micro},t}$ (full micro-state) |
| $T$ | $\Lambda_x(X_{\text{micro},t}) = X_{c,t}$ (macro-state) |
| $Y$ | $o_{\text{micro},t+1} \mid a_{\text{micro},t}$ (next observation given action) |
| $\beta$ | Implicit — set by the relevance-preservation tolerance $\epsilon_I$ |

*[Fit]* **Conjecturally clean, but reformulation non-trivial.** The existing (P1) is stated as a lower bound on retained mutual information: "the projection preserves at least $(1 - \epsilon_I)$ of the predictive information." Stated as IB, this becomes:

$$\Lambda^\ast \in \arg\min_{\Lambda \in \mathcal P} \; I\bigl(X_{\text{micro},t}; \Lambda_x(X_{\text{micro},t})\bigr) \quad \text{s.t.} \quad I\bigl(\Lambda_x(X_{\text{micro},t});\; Y_{\text{rel}}\bigr) \geq (1 - \epsilon_I)\, I(X_{\text{micro},t}; Y_{\text{rel}})$$

where $Y_{\text{rel}} = (o_{\text{micro},t+1} \mid a_{\text{micro},t})$. In Lagrangian form this is the master IB objective at a specific $\beta$ (the Lagrange multiplier of the constraint). So (P1) as stated admits exactly two equivalent forms: (a) constraint form ("retain $(1 - \epsilon_I)$"), (b) Lagrangian form ("optimize $I(X; T) - \beta \cdot I(T; Y_{\text{rel}})$ at $\beta = \beta(\epsilon_I)$"). The mapping $\epsilon_I \leftrightarrow \beta$ is the rate-distortion duality.

**Tensions.**

- **(P2) Lipschitz is not IB.** This is acknowledged in `spike-unity-closure-mapping.md` §6.4 and must remain separate. It is a regularity condition that IB does not impose.
- **(P3) Dimensionality reduction.** Two readings: (i) (P3) is an *independent* constraint on $\dim T$ that IB does not impose; (ii) (P3) is the *rate constraint* that is implicit in IB — fixing the compression rate $I(X; T)$ is approximately the same as fixing the dimensionality of $T$. See §4 for investigation.
- **The admissibility condition defines a *class* of projections, not a unique minimizer.** The IB master schema as written produces a unique minimizer (at fixed $\beta$); (P1) produces an inequality that any projection within the class must satisfy. Reconciliation: the IB-optimal projection at a given rate defines the *frontier*; (P1) admits projections *at or above* the frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$. So (P1) = "be on or above the IB frontier at a specified rate." This matches the `spike-unity-closure-mapping.md` §6.1 proposal.

### 2.5 Summary table

| Instance | $X$ | $T$ | $Y$ | $\beta$ | Fit |
|---|---|---|---|---|---|
| $M_t$ | $\mathcal C_t$ | $M_t$ | $o_{t+1:\infty} \mid a_{t:\infty}$ | $\beta(\rho, \pi)$ | Clean |
| $\Sigma_t$ (current) | "True causal structure" (hypothetical) | $\Sigma_t$ | $\pi^\ast \mid M_t$ | $\beta_\Sigma$ | DL-for-$I(X;T)$ mismatch; "source" ill-defined |
| $\Sigma_t$ (reformulated) | $\mathcal C_t$ | $\Sigma_t$ | $\pi^\ast \mid M_t$ | $\beta_\Sigma$ | Clean, parallels $M_t$ with different relevance variable |
| $G_t^{\text{shared}}$ | $G_t^{\text{full}}$ | $G_t^{\text{shared}}$ | $a_t^{\text{coordinated}}$ | bandwidth-driven | Direct |
| $\Lambda$ ((P1)) | $X_{\text{micro}}$ | $\Lambda_x(X_{\text{micro}})$ | $o_{\text{micro},t+1} \mid a_{\text{micro},t}$ | $\beta(\epsilon_I)$ via Lagrangian duality | Constraint-form; clean after reformulation |

---

## 3. What Follows if the Unification Holds

Concrete consequences. This section lists what would change, not what would be good in the abstract.

### 3.1 New segments (creation)

- **`#master-compression-principle`** (or rename `#form-information-bottleneck`): a single formulation segment stating the master IB objective, with explicit instance-binding template. This becomes the definitional home for the schema. Type: `formulation`. Depends on `#form-agent-model` and standard information theory.

### 3.2 Segments that simplify

- **`#form-information-bottleneck`**: becomes instance #1 (model compression). Current Discussion paragraphs about policy-relativity, volatility-dependence, and broader applicability can be consolidated — they become properties of the master schema that happen to specialize here.
- **`#form-strategy-complexity-cost`**: the IB-objective subsection becomes a pointer to the master schema with the $\Sigma_t$ binding. The DL formulation remains (as an operational cost measure), but the "analogy with `#form-information-bottleneck`" framing becomes "the $\Sigma_t$ instance of the master schema." The max-depth derivation ($d^\ast$) is independent of the unification; it stays as-is.
- **`#def-shared-intent`**: same treatment — the formulation is already in IB form; the Discussion becomes "this is the instance with relevance variable $a_t^{\text{coordinated}}$."
- **`#form-composition-closure`** (P1): explicitly presented as the IB constraint form, with cross-reference to the master schema. The Working Note "Open: Information Bottleneck unification" becomes resolved. The bridge lemma discussion is unaffected — it operates downstream of admissibility.

### 3.3 Scattered quantities that unify

- **Four separate $\beta$ parameters** (`#form-information-bottleneck`'s $\beta$, `#form-strategy-complexity-cost`'s $\beta_\Sigma$, `#def-shared-intent`'s $\beta$, `#form-composition-closure`'s implicit $\beta(\epsilon_I)$) become one schematic trade-off parameter whose *interpretation* is instance-specific (volatility, cognitive cost, bandwidth, rate constraint) but whose *role* is identical.
- **Four separate "relevance variables"** become explicit instance-level objects, promoting what is currently implicit to the level of formal specification. `#def-shared-intent` makes this explicit; the others do not.
- **Four separate rate-distortion curves** (implicit in each segment) become specializations of one curve-generating principle. `#result-unity-closure-mapping` already takes this view for (P1); it would extend naturally.

### 3.4 Currently-separate conditions that become instances

- The claim that "(P1) is structurally an IB relevance-preservation condition" (currently flagged in `#form-composition-closure` Working Notes and `spike-unity-closure-mapping.md` §6.1) becomes derivable.
- `#result-unity-closure-mapping`'s suggestion that unity dimensions parametrize rate-distortion curves becomes concrete: unity dimensions are *rate-distortion curve parameters* for the $\Lambda$ instance.
- `#def-model-sufficiency` $S(M_t)$ becomes a *diagnostic* on the $M_t$-instance IB frontier — how close the actual $M_t$ is to the frontier-optimal $T$ at a given rate.

### 3.5 What does NOT change

- The sector-condition machinery (`#result-persistence-condition`, `#schema-strategy-persistence`, etc.) is untouched. The unification is about compression, not dynamics.
- The strategy-DAG structure (AND/OR nodes, edge semantics, correlation hierarchy) is untouched.
- The directed-separation scope (modular/merged/partial) is untouched.
- The orient cascade structure is untouched.
- The bridge lemma contraction conditions (Tier 1/2/3) are untouched — they apply *after* admissibility.

The unification is strictly a reframing of the four compression segments and a sharpening of their downstream consequences. It does not touch the dynamical core of AAD.

### 3.6 Honest assessment of the "unification payoff"

The biggest concrete wins, ranked by how load-bearing they are:

1. **Relevance variable as first-class.** Currently implicit in three of four instances. Making it explicit forces clarity about *what each compression is for*, which is information-theoretic content the segments currently leave to interpretation. This is the strongest case for the unification: it converts implicit rhetoric into explicit structure.
2. **(P1) derived rather than asserted.** The rate-distortion reading promoted from Working Note to derived result. Moderate — the underlying observation is already there in spikes.
3. **Shared vocabulary and cross-references.** Future segments that need compression machinery ( `03-logogenic-agents/` and `02-tst-core/` both will) have one idiom to import rather than four. Moderate but compounding.
4. **Pedagogical concision.** Four segments teaching the same shape become one teaching the shape and three applying it. Minor but real.

Weak cases:

- Cross-instance *results* that only become available after unification are not obvious. There is no visible theorem of the form "because these are all IB, property X holds across instances." The master schema doesn't produce cross-instance deductions for free.
- The unification does not resolve any currently-open question in the theory. `#form-composition-closure`'s Working Notes about nonlinear (P1) computability, $\epsilon_I$ calibration, and $N$-agent scaling are not addressed by the IB reformulation.

---

## 4. What the Unification Does NOT Collapse

### 4.1 (P2) Lipschitz — confirmed separate

*[Established]*

The Lipschitz regularity condition is not an IB constraint. IB does not impose any continuity condition on the compressor — arbitrary stochastic maps with discontinuous realizations are IB-admissible as long as they preserve relevance. The bridge lemma in `#form-composition-closure` requires (P2) for an independent reason: to propagate bounded closure defect into bounded trajectory error (an analytic, not information-theoretic, requirement).

Under the unification, (P2) remains a separate admissibility condition. The segment's presentation becomes:

> Admissible projections are those that (a) sit on the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$ (= current (P1) restated as IB) and (b) are Lipschitz-continuous at constant $L$ (= current (P2)).

No loss of content; the IB/regularity separation is made explicit.

### 4.2 (P3) Dimensionality reduction — investigate

*[Open in scoping]*

Two possibilities:

**(P3-as-IB).** The IB objective at rate $I(X; T) \leq r$ implicitly constrains $\dim T$ via the channel capacity bound $I(X; T) \leq H(T) \leq \log \lvert T\rvert$ (discrete) or $\leq \frac{1}{2} \log \det (\operatorname{Cov}(T))$ up to constants (Gaussian). At sufficiently small rate, the IB-optimal $T$ is low-dimensional automatically. Under this reading, (P3) is not an independent condition — it is a *consequence* of the IB rate constraint when the rate is small enough. The natural reformulation: "(P3) is the IB rate constraint set small enough to force $\dim T \lt \dim X$."

**(P3-as-separate).** (P3) as stated is a strict inequality $\dim \mathcal X_c \lt \dim \mathcal X_{\text{micro}}$ — a categorical dimensional condition, not a soft rate condition. The IB-optimal $T$ at given $\beta$ might be *full-dimensional* over a support of size $\lt \dim X$, which would satisfy (P3) only in a measure-zero sense. In that case (P3) is genuinely separate and must be imposed independently.

**Which is right?** Neither is universal. For discrete $X$ and $T$, dimension is a cardinality, and (P3) is a soft rate constraint in disguise. For continuous (Gaussian) $X$ and $T$, dimension is support-geometry, and (P3) is a *harder* condition than any rate constraint — the IB frontier at any finite $\beta$ typically uses full support of $\mathbb R^{\dim X}$. Under the Gaussian IB in `spike-unity-closure-mapping.md`, the IB-optimal $T$ is a linear projection onto the top eigenvectors of a generalized eigenvalue problem; here $\dim T$ *is* a free parameter set by the truncation, not derived from $\beta$.

**Tentative conclusion.** In the Gaussian IB setup relevant to composition (P1), (P3) is a separate truncation-rank constraint, not a consequence of the IB optimization. Under the unification, (P3) remains separate, with the same status as (P2). This reduces the "unified IB" reading to "(P1) is IB with (P2), (P3) as side constraints" — still a clean story, but the claim "all admissibility conditions reduce to IB" is weaker than "only (P1) is the IB content; (P2) and (P3) are analytic/structural side conditions."

### 4.3 Other things that resist the unification

**Edge-level semantics in $\Sigma_t$.** The DAG's edge confidences $p_{ij}$, the AND/OR combination rules $\gamma(v)$, the correlation hierarchy (L0/L1/L2), and the regime indexing ($\iota_{ij}$) are structural properties of the strategy representation, not IB content. The IB objective says "find a compressed $\Sigma_t$ that retains decision-relevant information"; it does not say "the compressed $\Sigma_t$ is a DAG with single-parameter edges." The DAG-uniqueness result (`#deriv-graph-structure-uniqueness`) operates at a different level — it derives the *shape* of the representation, not its compression level. Under the unification, the DAG-uniqueness argument supplies the structural constraint that $\Sigma_t$ must be a DAG; the IB argument supplies the rate-distortion trade-off for how richly that DAG is populated.

**Recursion/temporal structure.** The update rule $M_t = f(M_{t-1}, o_t, a_{t-1})$ is a recursion; the IB objective is an optimization at a fixed $t$. The IB-optimal $\phi$ need not be recursively computable; finding recursive agents that approximate the IB frontier is a separate problem (the "variational IB" literature). Under the unification, the recursive structure of $M_t$ is orthogonal to the IB characterization of what $M_t$ ideally contains. Same point applies to $\Sigma_t$'s edge-update dynamics and the shared-intent update-and-transmission loop.

**Communication channel properties.** `#def-shared-intent` cleanly maps to IB in form but omits channel noise, delay, and misinterpretation (acknowledged in Epistemic Status). These are the communication-theoretic problems Shannon separated from source compression; the unification inherits this separation. The IB reformulation does not, by itself, give a theory of noisy inter-agent communication — it gives the source-compression half.

**Level 2 / intervention-relative relevance.** All four instances use mutual information (Level 1, associational). Strategy in particular wants interventional relevance — "what the edge $i \to j$ predicts *under $do(i)$*". IB's relevance variable $Y$ is observational. The regime-indexed interpretation of edge semantics (A/B/C) can be partially absorbed — A-regime edges have $Y = o \mid do(i)$, C-regime edges have $Y = o$ — but this is a per-edge story, not a single master-schema move. Under (U-strong) this is a real obstruction; under (U-medium) it is a known extension direction.

---

## 5. Linear-Gaussian Spike Work: (P1) and the Gaussian IB Frontier

### 5.1 Setup

From `spikes/spike-unity-closure-mapping.md` §2, the two-Kalman linear-Gaussian setup. Environment:
$$\omega_{t+1} = \omega_t + w_t, \quad w_t \sim \mathcal N(0, Q), \quad Q = q \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$$

Observations $o_{i,t} = \omega_{i,t} + v_{i,t}$, $v_{i,t} \sim \mathcal N(0, r)$, $v_1 \perp v_2$.

Steady-state Kalman filter per agent: $M_{i,t} = (\hat\omega_{i,t}, P^\ast)$, with identical $P^\ast$ and identical Kalman gain $K^\ast$ (homogeneous case, $\Delta K = 0$; the heterogeneous case is §10 of the unity-closure-mapping spike, which exhibits genuine $\varepsilon_x \gt 0$).

Micro-state: $X_{\text{micro}} = (\hat\omega_1, \hat\omega_2) \in \mathbb R^2$ at steady state (covariances are constants, discarded). Relevance target: $Y = (o_{1,t+1}, o_{2,t+1}) \mid (a_{1,t}, a_{2,t})$. For passive estimators with no control ($a_t \equiv 0$), $Y = o_{t+1} = \omega_{t+1} + v_{t+1}$.

### 5.2 The Gaussian IB frontier

The Gaussian IB (Chechik et al. 2005) for jointly Gaussian $(X, Y)$ with $T$ a linear Gaussian channel of $X$:

$$T^\ast_{\beta}(X) = A_\beta X + \xi, \quad \xi \sim \mathcal N(0, \Sigma_\xi)$$

with $A_\beta$ given by the generalized eigenvalue problem for $\Sigma_{Y \mid X}^{-1/2} \Sigma_{Y} \Sigma_{Y \mid X}^{-1/2}$, truncated to the eigenvectors whose eigenvalues exceed a threshold set by $\beta$. The IB frontier in the $(I(X; T), I(T; Y))$ plane is piecewise linear with breakpoints at the eigenvalues.

In the two-Kalman case:
- $\Sigma_X = \operatorname{Cov}(\hat\omega_1, \hat\omega_2)$ is a $2 \times 2$ matrix with off-diagonal $\rho_M \sigma_{\hat\omega}^2$ (where $\rho_M$ is the induced correlation of estimates, monotone in $\rho$ per the unity-closure-mapping spike §3.1).
- $\Sigma_{Y \mid X}$: conditional covariance of next observation given current estimate. For the random-walk-plus-white-noise observation model at steady state, $\Sigma_{Y \mid X} = Q + r I$ (the prediction-error covariance plus observation noise).
- $\Sigma_Y = \Sigma_X + \Sigma_{Y \mid X}$ at steady state (total observation covariance).

The Gaussian IB solution truncates to the eigenvectors of $\Sigma_{Y \mid X}^{-1} \Sigma_Y$ (or equivalently, the canonical-correlation basis between $X$ and $Y$). With $\Sigma_Y$ and $\Sigma_{Y \mid X}$ both diagonalizable in the $(+, -)$ basis of the estimate-space (because $Q$ is symmetric in $\rho$), the canonical directions are $u_+ = (1,1)/\sqrt 2$ and $u_- = (1,-1)/\sqrt 2$, with eigenvalues:

$$\lambda_+ = \frac{(1 + \rho_M) \sigma_{\hat\omega}^2 + q(1+\rho) + r}{q(1+\rho) + r}, \quad \lambda_- = \frac{(1 - \rho_M) \sigma_{\hat\omega}^2 + q(1-\rho) + r}{q(1-\rho) + r}$$

(Ordinary generalized eigenvalues of $\Sigma_Y \Sigma_{Y \mid X}^{-1}$ in the diagonal basis.)

### 5.3 IB-optimal projection at rate $\log(2)$ (1D truncation)

At $\beta$ large enough to retain only the top canonical direction, $T^\ast = u_+^T X = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$. This is *exactly* the means-sum projection used in `spike-unity-closure-mapping.md` §10 for the non-degenerate case — and it is the natural (P1)-admissible projection when the two estimates are positively correlated.

**IB-frontier value at 1D.** The retained relevance is:
$$I(T^\ast; Y) = \tfrac{1}{2} \log \lambda_+$$

while the full micro-relevance is:
$$I(X; Y) = \tfrac{1}{2} \log(\lambda_+ \lambda_-)$$

The fractional retained relevance is $\log \lambda_+ / \log(\lambda_+ \lambda_-)$, which → 1 as $\rho \to 1$ (canonical directions collapse, $\lambda_- \to 1$) and → $1/2$ as $\rho \to 0$ (symmetric contributions).

### 5.4 Comparing to (P1) as stated

(P1) requires $I(\Lambda_x(X); \Lambda_o(o_{t+1}) \mid \Lambda_a(a_t)) \geq (1 - \epsilon_I) \cdot I(X; o_{t+1} \mid a_t)$. With $\Lambda_x = \Lambda_o = u_+^T$ and $\Lambda_a$ trivial (no control), this becomes:

$$\tfrac{1}{2} \log \lambda_+ \geq (1 - \epsilon_I) \cdot \tfrac{1}{2} \log(\lambda_+ \lambda_-)$$

*[Conjecture (IB-P1-linear-Gaussian, unverified)]* The means-sum projection *attains the Gaussian IB frontier at rate $I(X; T) = \tfrac{1}{2} \log \lambda_+$* — i.e., no other 1D projection retains more $I(T; Y)$ at the same $I(X; T)$. This would establish that (P1) at the corresponding $\epsilon_I$ is *tight* for the means-sum projection in the linear-Gaussian symmetric case.

**What I can verify here.** The means-sum projection is the top canonical direction of $(X, Y)$, which is the generic form of the Gaussian IB solution at 1D. Under the symmetry of the two-Kalman setup (identical agents, symmetric $Q$), the canonical basis coincides with the principal-component basis of $\Sigma_X$ — so the means-sum is *both* the PCA-optimal 1D projection of $X$ *and* the CCA-optimal 1D projection of $X$ for predicting $Y$. These coincide because of the symmetry; in general they do not.

**What I cannot verify here.** Whether the means-sum projection attains the IB *frontier* — the exact trade-off curve — without writing out the full Gaussian IB Lagrangian. The Chechik et al. (2005) result gives the frontier as a function of eigenvalues and $\beta$; tracing the specific $\beta$ at which the 1D truncation becomes optimal requires one more page of algebra than I can fit in this spike.

**Honest obstruction.** To *prove* the conjecture I need to show: for all stochastic maps $T = f(X)$ with $I(X; T) = \tfrac{1}{2} \log \lambda_+$, $I(T; Y) \leq \tfrac{1}{2} \log \lambda_+$ with equality only for $T = u_+^T X$ (plus additive Gaussian noise of the appropriate variance). This follows from the Gaussian IB theorem (Chechik et al. 2005 Theorem 3.1) specialized to rank-1 $A_\beta$, but specializing the theorem to this problem requires writing out the appropriate $\beta$ and verifying the eigenvalue threshold is crossed exactly when the 1D truncation is selected. The scoping conclusion: the derivation is *mechanical-but-nontrivial* — 2-3 pages of Gaussian-IB algebra — and does not have closed-form obstructions. **Feasible in the integration session; not completed here.**

### 5.5 Heterogeneous-gain case (from §10 of unity-closure-mapping spike)

When $\Delta K \neq 0$, the means-sum projection produces $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2 / S_+]$. The IB reading: the means-sum is *no longer* the IB-optimal 1D projection, because the canonical basis for $Y = o_{t+1}$ relative to $X = \hat\omega$ is no longer the symmetric $(+, -)$ basis — the heterogeneous gains break the symmetry. The IB-optimal 1D projection in the heterogeneous case is a rotation of the means-sum; computing how much rotation is another mechanical derivation.

**Testable consequence.** The IB-optimal 1D projection should achieve *lower* $\varepsilon_x$ than the means-sum projection when $\Delta K \neq 0$. If the IB unification is right, the IB-optimal projection is the "correct" admissibility criterion, and the means-sum is admissible only when gains are symmetric. This is a falsifiable claim and worth checking numerically in the integration session.

### 5.6 Summary of the spike work

What was derived here:

- *[Derived (linear-Gaussian-symmetric)]* The means-sum projection is the PCA-optimal 1D projection of $X$ and the CCA-optimal 1D projection of $X$ for predicting $Y$ (they coincide under symmetric $Q$ and $\Delta K = 0$).
- *[Conjecture, spike-level]* The means-sum projection attains the Gaussian IB frontier at the corresponding rate. Proof requires specializing Chechik et al. 2005 Theorem 3.1; not done here.
- *[Identified]* In the heterogeneous case ($\Delta K \neq 0$), the means-sum is *not* IB-optimal; a rotation improves $\varepsilon_x$. This is a testable consequence of the unification and a candidate disconfirmation if it fails.

**Provisional confidence that (P1) attains the Gaussian IB frontier in linear-Gaussian:** moderate. The structural match is there; the symmetry argument supplies half of it; the remaining half is mechanical but not done.

---

## 6. Risks and Obstructions

### 6.1 Tractability

**Gaussian IB is tractable; general IB is not.** The Chechik et al. closed forms cover linear-Gaussian with jointly Gaussian $(X, Y)$; this covers the two-Kalman case and much of the composition-closure machinery when agents are Kalman-type. It does *not* cover:

- Discrete strategy DAGs (edges are Bernoulli, not Gaussian).
- Nonlinear agent updates (Bayesian filters beyond the Kalman class).
- Non-Gaussian relevance variables (next-action-given-state when actions are discrete).
- Multi-agent composition with heterogeneous agent types.

For these, the IB frontier exists as a definition but computing it requires variational approximation, sampling, or numerical optimization. The unification would *remain correct in principle* but *lose its closed-form advantage*. This is a sharp limit on how far the unification propagates quantitatively.

### 6.2 Relevance-variable underdetermination

**Which relevance variable?** Each instance names a candidate $Y$, but several could be defensible:

- $M_t$: $Y$ could be next observation ($o_{t+1}$), future trajectory ($o_{t+1:\infty}$), or future reward. Different choices yield different IB frontiers and different optimal $M_t$. `#form-information-bottleneck` selects $o_{t+1:\infty}$; this choice is not derived from first principles.
- $\Sigma_t$: $Y$ could be optimal policy ($\pi^\ast$), optimal action ($a^\ast_t$), or action-value ($Q(\cdot, \cdot)$). `#form-strategy-complexity-cost` selects $\pi^\ast$; this is a choice.
- Shared intent: $Y$ could be coordinated action, team value, or joint strategy. `#def-shared-intent` selects coordinated action.
- Composition (P1): $Y$ could be next observation, macro-trajectory, or macro-reward. `#form-composition-closure` (P1) selects next observation.

**The unification as currently stated commits the theory to these four specific relevance variables.** This is a substantive commitment — choosing a different $Y$ changes what "compression-optimal" means. The theory should either (a) defend each choice, or (b) allow the relevance variable to be a parameter of the compression operation. Currently the segments are silent on this. Under the unification, the silence becomes visible as an explicit choice — which is both a clarity gain and a commitment the theory takes on.

*[Concrete risk]* If a reviewer challenges the choice of $Y$ for any of the four instances, the unification propagates the challenge to all. Under four independent formulations, the choice of $Y$ is local to each segment and can be defended locally.

### 6.3 (P2) and (P3) remain separate

Confirmed in §4. The unification slogan "all compression is IB" overclaims; the honest slogan is "(P1)-analogs are IB; regularity and dimensionality are separate." If the segments promote the stronger slogan, they understate the role of Lipschitz and dimension conditions. This is not a deal-breaker but is a precise understatement risk.

### 6.4 Level 1 vs Level 2

IB's relevance variable is associational ($Y$ appears in a joint distribution with $X$ and $T$). Strategy edges in the regime-indexed interpretation (A/B/C) want interventional relevance for A-regime edges. This is a strictly stronger requirement than IB provides. Under the unification, A-regime edges would need an *interventional IB* variant (compression preserving $P(Y \mid do(T))$ rather than $P(Y \mid T)$). Such a variant is not standard in the literature and would be an extension, not a specialization.

If the integration session proceeds without resolving this, the unification would cover the Level-1 aspects of compression and leave the Level-2 aspects as separate machinery. This is acceptable but should be stated explicitly; the segments currently fudge the Level-1/Level-2 distinction in their compression discussions.

### 6.5 Proliferation of $\beta$ calibrations

**Each instance has its own $\beta$.** The master schema says "one objective shape"; it does not say "one $\beta$ value across instances." In practice, $\beta(\rho, \pi)$ for $M_t$, $\beta_\Sigma$ for $\Sigma_t$, bandwidth-$\beta$ for shared intent, and $\epsilon_I$-derived $\beta$ for (P1) are four different calibration problems. The unification gives a common *form* for the problem but does not unify the *parameters*.

This means the unification does not give cross-instance predictions of the form "if $\beta$ for $M_t$ is X, then $\beta_\Sigma$ for $\Sigma_t$ is Y." Those relationships, if they exist, come from the agent's overall resource-allocation problem (cognitive budget split across model, strategy, communication, and composition) — a problem the theory does not currently formulate. Under the unification, this becomes a visible gap; before unification, it is invisible because each $\beta$ lives in its own segment.

**Judgment call.** Making the gap visible is a gain or a loss depending on perspective. Joseph's "always strengthen before narrowing" principle favors making it visible — the theory either has a resource-allocation story or it does not; pretending otherwise is worse than admitting the gap.

### 6.6 Incremental benefit, not structural

Unlike the sector-Lyapunov template factoring (Session A.1), which *removes repeated content*, the IB unification *adds a master segment and cross-references four existing segments*. The net page count change is modest; the concision gain is mostly in avoiding re-explanation of the IB shape at each instance.

If the aim is concision, the Lyapunov-template factoring is higher-leverage. If the aim is integration (making an implicit pattern explicit), the IB unification is the right move. These are different targets.

---

## 7. Estimated Execution Effort

Effort in sessions (Joseph's unit of account; Session A.1 is one session, Session A.2 is 30 minutes, roughly).

**Scoping (this document).** 1 session. Done.

**Integration path A — minimal.**

1. **Session D.1 (1 session).** Rewrite `#form-information-bottleneck` as the master-compression formulation with explicit $(X, T, Y, \beta)$ schema. Add instance-binding table showing the four cases. Update `#notation.md` if needed for schema-level $X/T/Y$ variables.
2. **Session D.2 (0.5 session).** Update `#form-strategy-complexity-cost` and `#def-shared-intent` to reference the master schema, with explicit instance bindings. Walk back any duplication of IB formulation.
3. **Session D.3 (0.5 session).** Update `#form-composition-closure` (P1) to reference the master schema; promote `#form-composition-closure`'s "Open: Information Bottleneck unification" Working Note to a cross-reference in Discussion. Keep (P2), (P3) as separate admissibility conditions with explicit notes about why they are not IB.

Total minimal: **2 sessions after the scoping spike.**

**Integration path B — with linear-Gaussian verification.**

Path A plus:

4. **Session D.4 (1 session).** Complete the Gaussian IB derivation for the two-Kalman case (§5.4 conjecture). Verify the means-sum projection attains the frontier in the symmetric case; compute the IB-optimal projection in the heterogeneous case and compare $\varepsilon_x$ to the means-sum. Promote this to `#result-unity-closure-mapping` as a derived result (currently discussion-grade).
5. **Session D.5 (0.5 session).** Update `#result-unity-closure-mapping` to state (P1) as IB-frontier attainment (with explicit derivation), and walk back the "conjecture" language in Discussion.

Total minimal + verification: **3.5 sessions after scoping.**

**Integration path C — with extension work.**

Path B plus:

6. **Session D.6 (1-2 sessions).** Address the Level-1/Level-2 gap: specify which instances need interventional relevance and how the IB variant works there. This is research, not just integration — probably warrants its own spike before committing.
7. **Session D.7 (1 session).** Address the $\beta$-coordination question: does AAD want a resource-allocation layer that ties the four $\beta$'s together? If yes, scope that work. If no, document the deliberate separation.

Total with extensions: **5.5-6.5 sessions.**

**Recommendation for scoping decision.** Path A is load-bearing; Paths B and C are quality improvements. If the unification is to be executed at all, Path A + B (3.5 sessions) is the right target. Path C is optional and could be deferred.

---

## 8. Recommendation

**Conditional yes, with narrowing.** Path A + B (3.5 sessions) is worth executing, provided (a) the Gaussian IB derivation in §5.4 completes without surprises and (b) Joseph judges the "implicit becomes explicit" gain on relevance variables to be worth the cost of committing to specific $Y$ choices.

The basis for the recommendation:

**In favor.**

- The pattern is real. Three of the four instances already write their objectives in IB form; the fourth (`#form-composition-closure` (P1)) is in IB-constraint form. The cross-reference table in §2.5 does not require creative reinterpretation — it just names what is already there.
- The "relevance variable as first-class" move is the biggest substantive gain. It converts theory-level rhetoric ("compression preserves decision-relevant information") into formal content (specific $Y$, with specific $\beta$).
- The unification subsumes two currently-open Working Notes (`#form-composition-closure` IB unification note; `#result-unity-closure-mapping`'s IB connection paragraph). Those Notes currently block segment promotion; resolving them is a concrete workflow win.
- The sector-Lyapunov template factoring (Session A.1) is the highest-leverage concision move; IB unification is the highest-leverage *generalization* move. They are complementary, not competing.

**Against.**

- The unification is not a theorem engine. It does not deliver cross-instance results; it is a reframing that makes an implicit pattern explicit. The segments will not become dramatically shorter or proofier.
- (P2), (P3), and the Level-2 extension remain outside the IB frame. The "all compression is IB" slogan overclaims; the accurate slogan is weaker.
- The Gaussian IB closed form is local. Beyond linear-Gaussian, the unification loses computational bite, though it retains conceptual bite.
- **Alternative consideration.** The same clarity gain could be achieved more cheaply by a single `#disc-compression-operations` synthesis segment (like the proposed `#disc-independence-audit` and `#disc-approximation-tiering` in Session B) that lists the four instances with their $(X, T, Y, \beta)$ bindings as a cross-cutting reference, without rewriting the four instance segments. This would take 1 session instead of 3.5 and would deliver most of the clarity with less risk. Under this alternative, the four segments keep their current formulations; the new synthesis segment supplies the unifying view.

**Strongest version of the "against" case.** If the alternative synthesis segment achieves the clarity goal at 1/4 the cost, the full unification is a net loss. The full unification's marginal value over the synthesis segment is (a) the (P1) derivation (moderate — already most of the way there in `#result-unity-closure-mapping`) and (b) the explicit commitment to shared vocabulary for future segments (compounding but deferred).

**Final judgment.** Execute the *synthesis segment first* (1 session — roughly Session B.2/B.3 scale). Evaluate whether it resolves the clarity gap to Joseph's satisfaction. Proceed to the full Path A + B unification (2.5 additional sessions) only if the synthesis segment reveals that the four instance segments are individually pulling in inconsistent directions — which is what the full unification would correct. If the four instance segments are already pointing the same way with the synthesis segment as a pointer, the full unification is overbuilt.

**In one sentence.** The pattern is real, the unification is defensible, and the Gaussian IB spike is tractable — but the cheapest version of the gain is a single synthesis segment, not a four-segment rewrite, and the recommendation is to try the cheap version first.

---

## 9. Working Notes

- **Open: synthesis-segment-first vs full-unification.** The Path A + B plan above assumes Joseph wants the full unification. The §8 recommendation suggests trying the synthesis segment first. The final decision is Joseph's; the spike is neutral between paths.
- **Open: the $\beta$-coordination problem.** Section 6.5's "cognitive resource allocation across $M, \Sigma, \text{comm}, \Lambda$" is a real research question the unification surfaces. It is out of scope for the IB unification itself but may merit its own spike if the theory wants to address it.
- **Open: interventional IB for regime-A edges.** Section 6.4's Level-2 compression variant is a genuine research direction. There is a small literature on causal IB (Wieczorek-Roth 2017 and follow-ups); adapting it to AAD's regime-indexed edges is a separate spike.
- **Cross-check with `#deriv-graph-structure-uniqueness`.** The DAG-uniqueness argument derives the *shape* of $\Sigma_t$ from operational postulates. The IB unification supplies the *compression level* of $\Sigma_t$. These should be independent; if they interact (e.g., if IB compresses $\Sigma_t$ into a non-DAG), the unification has a structural conflict. Informal check: IB compressed $\Sigma_t$ retains the most decision-relevant *parts of the DAG* — it prunes nodes and edges, not the DAG structure — so the two arguments appear compatible. Worth verifying in the integration session.
- **The choice of relevance variable as a theory-level commitment.** This is the subtlest point of the spike. Currently each segment picks a $Y$ in isolation and the picks are defensible individually. Under unification, the four picks become a *system of commitments* the theory makes about what each compression operation is for. A reviewer could challenge any pick; under the unification, the challenge propagates. This is a feature of explicit commitment, not a bug, but it does mean the unification takes on visibility risk that the scattered formulations avoid.
- **What I did *not* investigate.** Whether the IB unification admits a "composite IB" where all four instances share a single joint objective (e.g., an agent's total cognitive cost across model, strategy, communication, and projection). This would be the strongest possible form of the unification — not just shared shape but shared optimization problem — and is implausibly strong. Not pursued. The synthesis-segment approach is the weaker but achievable target.
- **On the audit framing.** `audits/opus-audit-2026-04-21.md` "Bigger-picture synthesis §4" states that IB unification is "the biggest available unification in the theory." On closer examination it may be more accurate to say it is *the most legible* unification — the pattern is obviously there and a synthesis segment would capture it cleanly. The "biggest" claim suggests cross-instance results would follow; §3.6 and §6.6 argue they do not. This spike walks back the "biggest" framing to "most legible, worth capturing."
