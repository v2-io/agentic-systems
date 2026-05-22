# 3. Derivations

This file pushes the math on the six results announced in §2.6. Each result carries an honest tier label per the AAT conventions (exact / robust qualitative / conditional / heuristic / discussion-grade).

## 3.1 Result 1 — Stage-Localization of Repair

*[Derived (conditional on pipeline access). Tier: exact for the conditional statement; the conditional itself is structural.]*

### Statement

Let $\mathcal{A}$ be a Class 2 agent with coupling triple $\mathcal{C}_2 = (S, R, F)$ and pipeline $f_M = \tau \circ \alpha \circ \lambda \circ \phi$, where some subset $S \subseteq \{P1, P2, P3, P4\}$ of stages have a $G_t$ argument. If, for every $P_k \in S$, an external wrapper has *substitutability access* — the ability to intercept $P_k$'s input and supply its output to $P_{k+1}$ — then there exists a wrapped agent $\mathcal{A}'$ that is Class 1 at the wrapper level.

### Construction

For each $P_k \in S$, let $P_k^0: (M, x_{k-1}) \to x_k$ be a goal-blind operation that the wrapper supplies in place of $\mathcal{A}$'s native $P_k(\cdot; G)$. The choice of $P_k^0$ is the wrapper's design problem; canonical choices include:

- For $P_1$ (featurization): standard goal-blind feature extraction (e.g., uniformly attending to all input tokens, or extracting all observable features without goal-driven filtering).
- For $P_2$ (likelihood): an externally supplied likelihood model that does not condition on $G$.
- For $P_3$ (aggregation): a fixed-gain Bayes update with goal-blind weighting.
- For $P_4$ (consolidation): an externally supplied storage protocol.

The wrapped pipeline is

$$f_M^{\mathcal{A}'} \;=\; \tau^{(\cdot)} \circ \alpha^{(\cdot)} \circ \lambda^{(\cdot)} \circ \phi^{(\cdot)}$$

where each stage uses $P_k^0$ if $P_k \in S$ and the agent's native $P_k$ otherwise.

### Proof sketch

The composed function $f_M^{\mathcal{A}'}: (M_{\tau^-}, e_\tau) \to M_{\tau^+}$ has no $G$ argument at any stage. Each stage is a function of $(M, x)$ alone. By composition, the overall map has no $G$ dependence. Hence $\mathcal{A}'$ is Class 1 at the wrapper level: $\kappa_{\text{processing}}(\mathcal{A}') = 0$.

### Honest limits

(a) **Substitutability access is the conditional.** For monolithic Class 3 components (closed-source LLMs invoked via API; biological cognition under behavioral observation only), the stages are not externally addressable. The wrapper has access only to the agent's input/output boundary as a whole, not to its internal stage interfaces. In that regime, Result 1 does not apply; only full-agent wrapping (the W₀/W₁/W₂ construction at the agent level) is available.

(b) **$P_k^0$ must be a faithful goal-blind substitute.** If $P_k^0$ is significantly worse than $P_k$ on the goal-blind task (e.g., a much weaker featurizer), the wrapped agent is Class 1 but with degraded performance. The wrapping has a *capability cost*; this is the agent-level analog of the Brooks's-Law tempo overhead noted in `#der-class-coercion-via-wrapping`.

(c) **Cascade contamination requires upstream-most repair.** Result 3 below shows that coupling at $P_k$ contaminates $P_{k+1}, \ldots, P_4$ through their inputs. Minimal repair is therefore at the most upstream coupled stage, not at the most downstream symptom. Specifically: if $S = \{P_1, P_3\}$, repairing only $P_3$ leaves the cascade-contamination from $P_1$ untouched.

## 3.2 Result 2 — Form Determines Wrappability

*[Derived (content half: exact for the linear-bias model and the identifiability protocol; robust qualitative for general smooth content-form. Process half: a no-go — exact under the formal non-separability definition).]*

### Statement (positive half — content-form is post-hoc-wrappable)

If stage $\xi(\cdot; G)$ is **content-form coupled** per §2.4 — i.e., $\xi(u; G) = \xi^0(u) + b_\xi(G; u)$ with $b_\xi$ identifiable from a probing protocol — then there exists an external wrapper that does not require substitutability access (only behavioral probing access — the ability to query the agent with varied $G$ at the same $u$) and produces output equivalent to $\xi^0(u)$.

### Construction (content-form wrapper)

The wrapper's debiasing procedure:

1. **Probing phase.** Query $\mathcal{A}$ with a finite set $\{(u_i, G_j)\}$ of input-goal pairs, varying $G$ at fixed $u$. Record outputs $y_{ij} = \xi(u_i; G_j)$.
2. **Estimation.** Estimate $\hat b_\xi(G; u)$ from $\{y_{ij}\}$ via the identifying probes (assuming a reference goal $G_0$ is available with known $\hat b_\xi(G_0; u_i) = 0$, or via a normalization choice — see §3.2's "identifiability gauge" note below).
3. **Wrapping.** In normal operation, the wrapper subtracts the estimated bias: $\xi^{\text{wrapped}}(u; G) = \xi(u; G) - \hat b_\xi(G; u)$.

If $\hat b_\xi$ is a consistent estimator (in the sense of statistical estimation theory, given enough probes), the wrapped output converges to $\xi^0(u)$.

### Identifiability gauge

A subtlety: $b_\xi(G; u)$ is identifiable from probes *up to a $u$-dependent constant* if no reference goal is available. The remaining freedom corresponds to a shift of $\xi^0$ by that constant. If the goal is purely to *eliminate goal-dependence* (not to recover the unique honest $\xi^0$ up to absolute scale), the gauge freedom is harmless — any consistent estimator that produces $G$-invariant output suffices.

This matches Joseph's intuition that what we want from a Class 2 → Class 1 coercion is "directed-separation-by-construction," which is structurally a $G$-invariance property, not a goal-blind-truth-recovery property.

### Statement (negative half — process-form is not post-hoc-wrappable)

If stage $\xi(\cdot; G)$ is **process-form coupled** — there is no decomposition $\xi(u; G) = \xi^0(u) + b_\xi(G; u)$ with identifiable $b_\xi$ — then no external wrapper with behavioral-probing access alone can recover $\xi^0(u)$.

### Argument (process-form no-go)

Suppose, for contradiction, a wrapper $W$ exists that for any input $u$ and goal $G$ produces an output $W(\xi(u; G))$ that equals $\xi^0(u)$. Then for any pair $G_1, G_2$:

$$W(\xi(u; G_1)) = W(\xi(u; G_2)) = \xi^0(u).$$

Hence $W$ collapses $\xi(u; G_1)$ and $\xi(u; G_2)$ to the same point — $W$ must be many-to-one in a way that erases $G$-dependence.

But the probing protocol that constructs $W$ only sees $\{(u, G, \xi(u; G))\}$ — it does not see $\xi^0(u)$ directly. The construction of a many-to-one $W$ requires knowing *which* of the $G$-dependent responses is the "honest" one to collapse the others toward. Under process-form (no reference goal, no additive decomposition), there is no such honest response.

Equivalently in information-theoretic terms: the map from observable behavior to $\xi^0(u)$ has rank at most equal to the rank of $\xi(u; \cdot)$ as $G$ varies, minus the rank of the "honest" subspace. Under process-form coupling, that residual rank is zero.

So no external wrapper exists at the stage level. Repair requires *stage replacement* (Result 1) or *full-agent wrapping* (W₁).

### Honest scope of Result 2

(a) The argument assumes the wrapper has *only* behavioral-probing access. If the wrapper has substitutability access (Result 1's conditional), the form distinction doesn't gate wrappability — replacement works regardless of form.

(b) The argument assumes the goal-blind operation $\xi^0$ is *uniquely* what we want to recover. If the application only requires *some* $G$-invariant output (the wrapper is content with collapsing $\xi(u; G)$ to *any* fixed point as $G$ varies), then a coarser wrapper exists even under process-form. This corresponds to the "behavioral compliance" of W₂: the wrapper coerces a goal-blind output by *averaging* or *projecting*, not by *honest recovery*.

(c) Multiplicative process-form ($\xi(u; G) = \xi^0(u) \cdot h(G; u)$) is intermediate: the ratio $\xi(u; G_1) / \xi(u; G_2) = h(G_1; u)/h(G_2; u)$ is identifiable, so a *log-debiasing* wrapper works if a reference goal exists. The general no-go covers the *no-reference-goal* case.

## 3.3 Result 3 — Stage-Cascade Propagation

*[Derived. Tier: exact for the functional composition argument; robust qualitative for the empirical consequence.]*

### Statement

Let $\mathcal{A}$ have coupling at stage $P_k$. Then for all downstream stages $P_{k+1}, P_{k+2}, \ldots, P_4$, the effective composed map has a $G$-dependence even if those downstream stages are individually goal-blind.

### Argument

The downstream stage $P_{k+1}$ takes as input $x_k = P_k(u; G)$. Even if $P_{k+1}(\cdot)$ has no $G$ argument as a function, its *output* $x_{k+1} = P_{k+1}(x_k) = P_{k+1}(P_k(u; G))$ is a function of $G$ through the cascade. The same holds inductively for $P_{k+2}, \ldots, P_4$.

### Consequence — minimal repair is upstream-most

If $S = \{P_{k_1}, P_{k_2}, \ldots\}$ is the set of *natively coupled* stages, the cascade-effective coupled set is $\{P_{k_1}, P_{k_1+1}, \ldots, P_4\}$ — every stage from the most upstream native coupling forward. Stage-localization-of-repair (Result 1) applied at $P_{k_1}$ (substituting $P_{k_1}^0$) cleans up the cascade by removing the *source* of contamination. Applied only at a downstream stage, it leaves the cascade-contamination from upstream unaddressed.

### Subtle case — diluted contamination

If the downstream stage $P_{k+1}$ is *contractive* in a relevant metric — e.g., it projects onto a small range space, or aggregates many features with the coupled feature contributing only one component — the cascade contamination can be *attenuated* but not eliminated. Quantitatively, if the contamination at $P_k$'s output has bounded magnitude $\Delta$, the contamination at $P_{k+1}$'s output is bounded by $L \Delta$ where $L$ is the Lipschitz constant of $P_{k+1}$ on the relevant subspace. So a downstream-only repair can be *quantitatively useful* (reducing the magnitude of leakage) without being *structurally complete* (it does not make the cascade Class 1).

This corresponds operationally to *defensive scaffolding* (`#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition") applied at intermediate stages: it dilutes goal-contamination without removing the upstream source.

## 3.4 Result 4 — Source Asymmetry and Belief-Strategy Attractors

*[Conjectural-derived. Tier: robust qualitative; the formal fixed-point argument is exact under the stated linear feedback model; generalization to nonlinear strategic dynamics is heuristic.]*

This is the most substantive new structural result the typology produces. It is the one most worth subjecting to independent verification.

### Setup

Consider a Class 2 agent with *pure $\Sigma_t$-source* coupling at stage $P_3$ (aggregation). The coupled aggregation has multiplicative process-form:

$$M_{\tau^+} = M_{\tau^-} + K(\Sigma_{\tau^-}) \cdot \ell_\tau$$

where $\ell_\tau$ is the likelihood signal from upstream stages (goal-blind by assumption — only $P_3$ couples), and $K: \mathcal{S} \to \mathbb{R}^{+}$ is a $\Sigma$-dependent gain. Sunk-cost is the canonical instantiation: $K(\Sigma)$ decreases as $\Sigma$ commits more heavily to specific beliefs about reality (formally: as the projection of $\Sigma$ onto strategies-presuming-$M = m^\ast$ grows, $K$ falls *for evidence challenging $m^\ast$*).

The orient cascade (per `#der-orient-cascade`) updates $\Sigma$ as a function of the new $M$:

$$\Sigma_{\tau^+} = f_\Sigma(M_{\tau^+}, O_t, \Sigma_{\tau^-}).$$

### Closed-loop dynamics and fixed points

Substituting,

$$M_{\tau^+} = M_{\tau^-} + K(\Sigma_{\tau^-}) \cdot \ell_\tau, \qquad \Sigma_{\tau^+} = f_\Sigma(M_{\tau^-} + K(\Sigma_{\tau^-}) \ell_\tau, O_t, \Sigma_{\tau^-}).$$

A fixed point $(M^\ast, \Sigma^\ast)$ satisfies

$$K(\Sigma^\ast) \cdot \ell^\ast = 0, \qquad \Sigma^\ast = f_\Sigma(M^\ast, O_t, \Sigma^\ast).$$

Two ways to satisfy $K \cdot \ell = 0$:

- **(a) Honest convergence:** $\ell^\ast \to 0$ — no further evidence to integrate. $M^\ast$ is the agent's converged belief. Standard Bayesian convergence under stationary evidence stream.
- **(b) Pathological attractor:** $K(\Sigma^\ast) \to 0$ — the gain has collapsed even though $\ell^\ast \neq 0$. Evidence arrives, but the agent does not integrate it.

Case (b) is the sunk-cost attractor. It is *structurally possible* when $K$ decreases sharply on the subspace of $\Sigma$ committed to a particular $M$, and the orient cascade is such that $\Sigma^\ast$ is a stable point of $f_\Sigma$ near a particular $M$. Concretely: an agent commits to a plan $\Sigma$ that presumes $M = m^\ast$; evidence arrives suggesting $M \neq m^\ast$ ($\ell^\ast \neq 0$ pointing toward $m'$); but because $\Sigma$ is committed and $K(\Sigma^\ast)$ has fallen near zero, the evidence does not propagate to $M$. The agent's $M$ stays at $m^\ast$, $\Sigma$ stays committed, and the system rests in a $(m^\ast, \Sigma^\ast)$ attractor misaligned with the environment.

### Linearized stability analysis (under exact assumptions)

Linearize around $(M^\ast, \Sigma^\ast)$. Let $\delta M_\tau = M_\tau - M^\ast$, $\delta\Sigma_\tau = \Sigma_\tau - \Sigma^\ast$, and denote partial derivatives at the fixed point:

$$K^\ast = K(\Sigma^\ast), \quad K'^\ast = \partial_\Sigma K \big\vert_{\Sigma^\ast}, \quad A = \partial_M f_\Sigma \big\vert_{(M^\ast,\Sigma^\ast)}, \quad B = \partial_\Sigma f_\Sigma \big\vert_{(M^\ast,\Sigma^\ast)}.$$

The linearized dynamics are (with $\ell^\ast$ the linearization of $\ell_\tau$ around the fixed point — treating $\ell$ as a function of $M$ for the locally-linearized evidence-arrival process, $\ell \approx -L \delta M$ for some positive-definite information matrix $L$):

$$\delta M_{\tau^+} = \delta M_{\tau^-} + K^\ast \cdot (-L \delta M_{\tau^-}) + K'^\ast \delta\Sigma_{\tau^-} \cdot \ell^\ast = (I - K^\ast L) \delta M_{\tau^-} + (K'^\ast \ell^\ast) \delta\Sigma_{\tau^-}$$

$$\delta\Sigma_{\tau^+} = A \delta M_{\tau^+} + B \delta\Sigma_{\tau^-}$$

The Jacobian of the closed-loop map is

$$J = \begin{pmatrix} I - K^\ast L & K'^\ast \ell^\ast \\ A (I - K^\ast L) & A K'^\ast \ell^\ast + B \end{pmatrix}.$$

**Pathological-attractor condition.** $(M^\ast, \Sigma^\ast)$ is a stable attractor if all eigenvalues of $J$ have modulus less than 1. In the case $K^\ast \to 0$ (sunk-cost collapse), $I - K^\ast L \to I$ (no contraction in the $M$ direction), and stability is determined by $B$. If $B$ has eigenvalues with modulus less than 1 (the orient cascade is contractive in $\Sigma$ — typical for $\Sigma$-update dynamics with friction), the joint fixed point is stable *even though $M$ has no contraction* — the strategy stabilizes around its commitment, and the absence of belief-update propagation keeps $M$ near $m^\ast$.

This is the formal statement: $\Sigma$-source coupling with multiplicative process-form admits *self-stabilizing attractors* in which the agent's belief remains misaligned with the environment indefinitely.

### Contrast — pure $O_t$-source coupling

Substitute the same coupling but with $O$ as the source:

$$M_{\tau^+} = M_{\tau^-} + K(O_t) \cdot \ell_\tau.$$

Per the orient cascade (`#der-orient-cascade`), $O_t$ revises only when forced — under nominal operation, $O_t$ is *exogenous* to $M$. In steady state, $O_t = O^\ast$ is a constant; $K(O_t) = K(O^\ast)$ is a constant.

Closed-loop dynamics:

$$\delta M_{\tau^+} = (I - K(O^\ast) L) \delta M_{\tau^-} + 0 \cdot \delta O_{\tau^-}$$

(the $O$-feedback term is zero because $O$ doesn't update from $M$ in steady state). The map is contractive whenever $K(O^\ast) L$ has appropriate properties — standard Bayesian update with a goal-shaped (but constant) gain.

There is no self-stabilizing attractor of the type produced by $\Sigma$-coupling. The agent's belief has a *bias* (the gain $K(O^\ast)$ may be smaller than honest gain, producing slower convergence or non-zero asymptotic residual relative to true environment), but it does not have a feedback loop that *forecloses* belief-revision.

This is the formal source-asymmetry result: **pure $\Sigma_t$-source coupling can produce closed-loop pathological attractors; pure $O_t$-source coupling cannot.**

### Empirical resonance

The asymmetry matches the empirical literature:

- **Sunk-cost / commitment cascades** are documented as *self-reinforcing* in psychology (Staw 1976 *Knee-Deep in the Big Muddy*; Brockner 1992; Arkes & Blumer 1985) and in organizational behavior (Sleesman et al. 2012 meta-analysis). They are structurally $\Sigma$-source per the typology.
- **Identity-driven motivated reasoning** is documented as producing *bias* but not *runaway* — biased priors get corrected by sufficient evidence over time (Kahan's cultural-cognition project shows persistent bias but not divergent attractors in most settings; the persistent-bias regime where divergence is seen is when *identity-bound communities reinforce the priors*, which is a separate composite mechanism, not single-agent $O$-coupling). This is the $O$-source case per the typology.

The empirical literature already distinguishes these phenomena along the dynamical signature; the typology *predicts the structural reason* — $\Sigma$ closes a feedback loop, $O$ does not.

### Tier and caveats

The fixed-point argument is *exact* under (i) the linearized dynamics, (ii) the multiplicative process-form gain $K(\Sigma)$, and (iii) the orient-cascade assumption that $O$ is exogenous to $M$ in steady state. Generalization to nonlinear $K, f_\Sigma$ retains the *qualitative* asymmetry (the feedback-loop topology is independent of linearization) but the explicit fixed-point structure may admit multiple attractors, limit cycles, or chaos. *Robust qualitative* on the general claim; *exact* on the linearized version.

The result is sensitive to the assumption that $O$ revises only when forced — if $O$ is updated continuously by $M$ (the agent's objective slides toward what it believes possible), the asymmetry partially collapses: $O$-coupling then closes a feedback loop too, but the orient cascade explicitly forbids this in canonical AAT. (Identity-binding under adversarial pressure may be the empirical case where $O$ effectively updates from $M$; this is the regime where the asymmetry should attenuate.)

**Honest scope note on $K(\Sigma)$.** The multiplicative form $K(\Sigma)$ used here is *posited* as the structural shape of sunk-cost-style coupling, not derived from a more primitive AAT mechanism. The empirical mechanism is closer to: $\Sigma$-commitment imposes a cost on revising $M$ (the agent would lose the sunk investment by abandoning the strategy), which functions as an additional regularization term pulling belief toward strategy-consistent states; this *effective* dynamics is multiplicative-gain-like in the linearized regime. A fuller treatment would derive $K(\Sigma)$ from a utility-cost analysis of belief-revision-under-strategic-commitment; for the purpose of Result 4 the multiplicative form is a sufficient model of the empirical phenomenon. Independent verification of this step — does sunk-cost effective dynamics reduce to multiplicative gain in the linearization, or to a different form? — is the *single most worthwhile sub-spike* (recommended for verification before promotion).

## 3.5 Result 5 — Composition with the Leakage Locus

*[Derived from §3 of `spike-leakage-locus-2026-05-18` plus the typology. Tier: exact for the linear-Gaussian / smooth-tilt model; robust qualitative for the general statement.]*

### Statement

For any Class 2 sub-type $(S, R, F)$, the belief-displacement $\Delta\mu$ caused by goal-coupling is confined to the Fisher null space $\ker\mathcal I_\tau$ of the observation given the current latent state (per the Leakage Locus Lemma). The sub-type determines the *functional form of the displacement within that subspace*, not the support.

### Sketch

The Leakage Locus Lemma (§3 of `spike-leakage-locus-2026-05-18`) establishes that *any* smooth goal-tilt $c_G(z) = \exp(g^\top z)$ applied to the posterior produces displacement $\Delta\mu = \Lambda_0^{-1} g$ confined to $\ker\mathcal I_\tau$. The argument is information-geometric: along directions identified by the observation, the likelihood dominates the prior and the tilt is suppressed; along directions unidentified, the prior alone supports belief and the tilt passes through.

This argument does not depend on *where in the $f_M$ pipeline* the tilt is generated. A coupling at $P_1$ (featurization) that shapes the encoded $x$ ultimately produces a tilt on the posterior; a coupling at $P_3$ (aggregation) that shapes the gain $K$ produces a different functional form of tilt — but both effects are confined to $\ker\mathcal I_\tau$ by the same identifiability argument.

What the typology adds:

- **Content-form sub-types** produce $g$ that is *linear in $G$*. The displacement $\Delta\mu = \Lambda_0^{-1} g(G)$ is a linear function of the goal. Behavioral probing can recover $g(G)$ up to gauge.
- **Process-form sub-types** produce $g$ that is *nonlinear in $G$*, or more subtly, produce a $\Lambda_0$ that itself depends on $G$ (when the coupling shapes the precision-update at $P_2$ or $P_3$). Probing reveals not just biased means but a $G$-dependent covariance structure.
- **$\Sigma$-source sub-types** produce $g(\Sigma)$ where $\Sigma$ is itself a closed-loop function of $M$. The leakage locus argument still holds *per-step* (the locus is $\ker\mathcal I_\tau$), but the *dynamics* across steps admit the attractors of Result 4 — the tilt magnitude $\lVert g\rVert$ grows or persists when $\Sigma$ has locked onto a misaligned $M^\ast$.
- **$O$-source sub-types** produce $g(O)$ with $O$ exogenous; the tilt magnitude is exogenously bounded.

### Operational consequence

The composition gives a *finer-grained target* for the $\hat\kappa_{\text{processing}}$ behavioral estimator (per `#der-directed-separation` §"Empirical estimator for $\kappa_{\text{processing}}$"):

- The estimator should probe along $\ker\mathcal I_\tau$ (per the leakage-locus result).
- Within $\ker\mathcal I_\tau$, the estimator should distinguish *content* (mean shift) from *process* (covariance shift or higher-moment structure) signatures.
- Across time, the estimator should track whether the tilt is *exogenously bounded* ($O$-source signature) or *autocorrelated with $\Sigma$-updates* ($\Sigma$-source signature).

This is a substantive refinement: the existing estimator only measures aggregate $\hat\kappa$; the refined estimator measures *which Class 2 sub-type* the agent inhabits.

## 3.6 Result 6 — Wrapping-Regime Correspondence

*[Derived. Tier: robust qualitative — the correspondence is structural; the boundary cases (e.g., partial-information wrappers between W₁ and W₂) require per-case analysis.]*

### Statement

The W₀/W₁/W₂ wrapping regimes of `#der-class-coercion-via-wrapping` are the agent-level analogs of the stage-level form distinction in the typology:

| Wrapping regime | Stage-level analog | Class achieved at wrapper |
|---|---|---|
| W₀ (no wrapping) | n/a — the agent stands as-is | Whatever the un-wrapped agent is |
| W₂ (partial wrapping) | Content-form at the agent level — wrapper passes $G$ to component, post-hoc structures the response | Class-1-by-behavior (per `#der-directed-separation`) |
| W₁ (strict wrapping) | Process-form-with-pipeline-access — wrapper structurally substitutes goal-blind execution | Class-1-by-structure |

### Argument

W₂ — "the *query boundary* still passes $G_W$ to the component" — is structurally the content-form analog: the goal enters the operation, but the *output structuring* (typed parsed response) extracts a goal-blind belief-update by subtracting (or projecting away) the goal-shaped component of the response. The wrapping's effectiveness depends on the component's *behavioral compliance* with the prompted instruction-to-separate — exactly because W₂ is the content-form wrap at the agent level.

W₁ — "separate goal-blind queries to the underlying component update the wrapper's $M_W$" — is structurally the process-form-with-access analog: the wrapper does not pass $G$ to the belief-update query at all; the wrapper composes goal-blind component calls into a goal-blind composite pipeline. This is structural substitution at the agent level.

W₀ — no wrapping — is the case where the un-wrapped agent's Class status stands. For Class 3 monolithic agents without internal access, W₀ leaves the agent Class 3; for Class 2 agents that fit the use case, W₀ leaves the agent at its native sub-type.

### Sub-type matching

The typology refines the wrapping-regime recommendation:

- A Class 2 agent with *content-form* coupling (only): W₂ is sufficient. The wrapper structures the response to absorb the bias.
- A Class 2 agent with *process-form* coupling at any stage: W₂ may be insufficient because the response shape varies with $G$, not just the response content. W₁ is required (if pipeline access exists) — or a full Class-1 reimplementation.
- A Class 2 agent with *$\Sigma$-source* coupling: even W₁ may be insufficient if the wrapper passes a $\Sigma$ that the component's internal cascade picks up. The wrapper must additionally suppress the $\Sigma$-source channel (e.g., by holding $\Sigma$ constant per call or by stripping $\Sigma$-content from the query). This is a finer-grained design constraint the typology surfaces.

## 3.7 What is derived vs. what is chosen

Following the audit-friendly conventions of `#der-directed-separation`:

| Element | Source | Status |
|---|---|---|
| Pipeline decomposition $f_M = \tau \circ \alpha \circ \lambda \circ \phi$ | Posited as canonical decomposition; mapped to existing AAT machinery (mismatch signal, update gain) | Choice (well-justified; canonical for Bayesian-style updates) |
| (Stage × Source × Form) parameterization | Forced by the structural axes once the pipeline is in place | Derived from the choice above |
| Content-form / process-form distinction | Information-theoretic identifiability (probing recovers $\xi^0$ or it doesn't) | Derived (definitional; the identifiability gauge is a choice) |
| Result 1 (stage-localization of repair) | Functional composition argument | Derived; exact under the conditional |
| Result 2 (form determines wrappability) | Identifiability theory + behavioral-probing model | Derived (content half exact; process no-go exact under formal non-separability) |
| Result 3 (cascade propagation) | Composition of functions | Derived; exact |
| Result 4 (source asymmetry, belief-strategy attractors) | Linearized closed-loop analysis around fixed points + orient cascade exogeneity of $O$ | Robust qualitative; exact under linearization assumption |
| Result 5 (leakage locus composition) | Leakage Locus Lemma + typology | Derived; exact in linear-Gaussian instantiation |
| Result 6 (wrapping correspondence) | Structural mapping between agent-level wrapping regimes and stage-level form distinctions | Robust qualitative; the structural correspondence is exact, the boundary cases require per-case analysis |

The two genuinely-new structural results worth promoting are Result 2 (form-wrappability identifiability theorem) and Result 4 (source asymmetry / belief-strategy attractor). The others are organizing/composing the existing structure.
