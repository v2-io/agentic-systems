---
slug: der-architecture-noidentifiability
type: derived
status: conditional
depends:
  - def-mismatch-signal
  - result-mismatch-decomposition
  - deriv-sector-condition
  - scope-agent-identity
  - der-loop-interventional-access
  - der-agent-opacity
  - disc-identifiability-floor
  - deriv-edge-credence-dynamics
stage: draft
---

# Derived: Architecture No-Identifiability from On-Policy Summary Data

The framework's identifiability-floor at the *agent-internal architecture* layer. Two AAT agents whose linearized closed-loop residual dynamics are minimal state-space realizations related by an invertible similarity transformation produce *identical* on-policy summary statistics: identical innovation spectrum, identical sector-condition summary $(\alpha, R)$, identical similarity-invariant deviation summaries — and therefore identical observation law under on-policy, in-regime, summary-only access. An observer with that access cannot distinguish the two agents, even though they implement the correction in structurally distinct internal coordinates. The architectural degree of freedom AAT cares about — `#der-agent-opacity`'s "which internal mechanism" — lives entirely in the $GL(n)$ similarity fiber and is annihilated by the on-policy observation map.

The no-go is *exact* in the linear-Gaussian / Kalman sub-scope, anchored by Kalman 1963 and Ho-Kalman 1966 canonical-form non-uniqueness; *robust-qualitative* in the general sub-scope via the Causal Hierarchy Theorem applied at the agent-as-SCM layer (Bareinboim, Correa, Ibeling & Icard 2022). The mechanism is **not** Sylvester's law of inertia inherited for free — the *generating* group action that produces the indistinguishable pair is state-space similarity $T(\cdot)T^{-1}$, not the metric congruence $S^\top(\cdot)S$ that Sylvester governs. It *reduces*, however, to the same shape as the Instance-2 rank-collapse floor ( #deriv-edge-credence-dynamics Prop B.7): the on-policy Fisher information of the realization manifold is identically zero along the similarity-fiber tangent distribution, so the observed-Fisher is rank-deficient on a structurally-forced indeterminacy manifold — Instance-2's mechanism with the manifold being a Lie-group fiber rather than a single indeterminacy submanifold. Escape-irreducibility under the agent's *metric/coordinate* freedom (distinct from the similarity freedom that *generates* the pair) is then Sylvester at one remove, identically to Instance 2.

Three structurally distinct escapes: (a) loop-interventional access ( #der-loop-interventional-access) perturbs along similarity-fiber directions that on-policy data never excites — the intervention generates Level-2 data, the no-go is Level-1-only; (b) higher-moment / out-of-regime observation distinguishes the pair in the nonlinear sub-scope (AAT's $\beta$) — *provably void* in the linear-Gaussian sub-scope, since a Gaussian innovation carries no information beyond second order; (c) architecture instrumentation (direct read of the update rule or internal state) breaks the black-box scope, structurally the same kind as Instance 2's "instrument the latent" escape. A fourth proposed escape — horizon extension under the same policy — collapses into (a): more samples of an annihilated observation law cannot escape the annihilation.

The strengthened consequence is that `#der-loop-interventional-access` acquires a *third semantically-distinct deployment mode* — at the agent-internal layer — alongside Instance 1's agent-self-intervention (breaking causal-sufficiency degeneracy) and Instance 3's observer-on-sub-agent intervention (breaking coupling-sign degeneracy). The shared content across the three modes is "Level-2 data breaks a Level-1 degeneracy"; the distinct content is *which* degeneracy.

## Formal Expression

### The Setting

*[Definition (architecture-noidentifiability-setting)]*

Two AAT agents $A$ and $A'$ are *architecturally distinct, behaviorally identical from on-policy summary data* in a regime $\Omega$ when:

- both operate on the same regime-restricted trajectory under their respective on-policy execution;
- both share the same sector-condition summary $(\alpha, R)$ in $\Omega$ ( #deriv-sector-condition), equivalently the same ultimate-deviation statistics on the similarity-invariant summaries of $\lVert\delta\rVert$ in that regime;
- the observer has *on-policy, in-regime, summary-only* access — no off-policy intervention, no out-of-regime samples, no white-box read of the update rule or internal state.

Per `#scope-agent-identity`, $A$ and $A'$ are agents on singular trajectories with action-marginal invariance under change of internal-coordinate parameterization. The question is whether the architectural content — the basis in which the correction is implemented, internal to the agent — can be recovered from the observer's accessible data.

### The No-Go Theorem (exact in the linear-Gaussian / Kalman sub-scope)

*[Derived (architecture-noidentifiability-Kalman, from Kalman-Ho canonical-form non-uniqueness applied to AAT-agent realizations), exact in the linear-Gaussian sub-scope]*

Let the linearized closed-loop residual dynamics of $A$ and $A'$ be minimal state-space realizations

$$d\delta_t = -F\,\delta_t\,dt + \sigma_w\,dW_t, \qquad d\delta'_t = -F'\,\delta'_t\,dt + \sigma'_w\,dW_t$$

with $F, F'$ Hurwitz (sector-condition-satisfying per `#deriv-sector-condition`) and the two realizations related by an invertible similarity $T \in GL(n)$:

$$F' = T\,F\,T^{-1}, \qquad \sigma'_w\,\sigma_w'^{\top} = T\,\sigma_w\,\sigma_w^{\top}\,T^{\top}.$$

**Claim.** The stationary innovation process — hence the $(\alpha, R)$-summary, the innovation spectrum, and every *similarity-invariant* summary of the on-policy observation law — is **identical** for $A$ and $A'$. No on-policy, in-regime, summary-restricted statistic distinguishes them.

**Derivation.** The innovation's stationary law is determined by the pair $(F, \sigma_w \sigma_w^\top)$ only through similarity-invariant quantities. Specifically:

- The eigenvalues of $F$ (the $\alpha$-spectrum entering the sector summary) are similarity-invariant.
- The stationary covariance $\Pi$ solves the Lyapunov equation

$$F\,\Pi + \Pi\,F^{\top} = \sigma_w\,\sigma_w^{\top}$$

(standard form for the OU drift $-F$ with $F$ Hurwitz, sign convention matching `#deriv-sector-condition`), and transforms under similarity as $\Pi' = T\,\Pi\,T^{\top}$.

- The observed quantities are the *innovation spectrum* $\det(i\omega I - F)$ and its similarity-invariant moments — for example, the *deviation magnitude under any similarity-invariant norm* (a norm derived from the dynamics, such as the $F$-induced metric, rather than a fixed external basis). Each is annihilated by the similarity action.

The architectural content — the basis $T$, that is, *which* internal coordinates implement the correction — lives entirely in the similarity orbit and is annihilated by the on-policy observation map. $\square$

**Scope of "identical."** The claim restricts to *similarity-invariant* summaries of the on-policy observation law. Fixed-external-basis quadratic forms in the raw residual are *not* in general similarity-invariant — for instance,

$$\mathbb{E}\,\lVert\delta\rVert^2 = \operatorname{tr}\Pi, \qquad \operatorname{tr}(T\,\Pi\,T^{\top}) \neq \operatorname{tr}\Pi \;\text{in general}$$

(equality only when $T$ is orthogonal). The on-policy observer who consumes $(\alpha, R)$ summaries and the innovation spectrum sees only similarity-invariant content; an observer with access to a fixed external basis can in principle break the orbit by observing the raw covariance, but that is a *different* observation regime than the on-policy summary access the no-go is stated under.

### The General Sub-Scope (robust qualitative)

*[Derived (architecture-noidentifiability-general, from causal hierarchy theorem applied at agent-as-SCM layer), robust qualitative]*

Outside the linear-Gaussian sub-scope, the no-go is robust-qualitative rather than exact. Model the agent as a structural causal model over its internal state space (per `#scope-agent-identity`'s token-level commitment to singular-trajectory agents). The Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem then applies at the agent-as-SCM layer: two SCMs over the agent's state space agreeing on Level-1 observation data — the on-policy summary distribution — cannot in general be distinguished on Level-2 questions about $do(\cdot)$ on the agent's internal coordinates.

The dual-anchor structure (sharp Kalman-Ho for the linear-Gaussian sub-scope; CHT-at-agent-as-SCM for the general case) is the same shape Instance 1 carries — explicit construction sharp / CHT general — and the tier separation is load-bearing: collapsing to "exact" overclaims; collapsing to "robust-qualitative" understates the sub-scope's sharpness.

### Mechanism: Instance-2 Fisher Null on a Lie-Group Fiber

*[Derived (mechanism-reduction-to-instance-2, from Fisher-information factorization through similarity-invariants)]*

The no-go's *generating* group action is state-space similarity $F \mapsto T\,F\,T^{-1}$ on the realization manifold. Sylvester's law of inertia ( #disc-identifiability-floor §Discussion) governs metric *congruence* $\mathcal{G} \mapsto S^\top \mathcal{G} S$, a different group action; the no-go therefore does **not** inherit Sylvester at the generating-action layer.

The reduction to Instance-2 mechanism proceeds via Fisher geometry. Parameterize the agent by

$$\theta = (\text{similarity-invariants}, \text{orbit-coordinates})$$

— formally, the realization manifold fibered over the transfer-function manifold by the $GL(n)$ similarity group. By the §"No-Go Theorem" derivation, the on-policy observation law depends on $\theta$ only through the similarity-invariant base. The Fisher information of the on-policy observation channel, as a quadratic form on the full realization manifold, is therefore *identically zero* on the entire tangent distribution of the similarity fiber. That is the Instance-2 structure (Fisher rank-deficiency along a structurally-forced indeterminacy manifold; #deriv-edge-credence-dynamics Prop B.7), with the manifold being a $GL(n)$ Lie-group fiber rather than the mixture-indeterminacy manifold of Instance 2.

The agent's *escape-irreducibility under its metric/coordinate freedom* is then Sylvester at one remove — identically to Instance 2. Once the rank-deficient observed-Fisher is recognized, no reparameterization of the observation model refills the rank-deficient direction; congruence preserves inertia.

The two group actions and their roles, made precise:

- The **similarity action** $T(\cdot)T^{-1}$ on the realization manifold *generates* the indistinguishable architectural pair $(A, A')$. This is what makes the floor a floor at all, and it is *not* Sylvester — it is the fiber of the realization-to-transfer-function bundle.
- The **congruence action** $S^\top(\cdot) S$ on the observed-Fisher governs the agent's potential escape by reparameterizing its observation model. This *is* Sylvester, and it forbids the escape, identically to Instance 2.

This no-go is therefore a member of the rank-collapse subclass of `#disc-identifiability-floor` ($\{$Instance 1, Instance 2, Instance 4$\}$ via Sylvester at one remove) rather than Instance 3's projection / Schur-complement obstruction. The additional structure beyond Instance 2 is that the rank-deficient direction is a Lie-group fiber.

### Boundary Characterization: Three Structurally Distinct Escapes

*[Derived (escape-routes, from no-go scope conditions)]*

The no-go's scope is (i) on-policy, (ii) in-regime, (iii) summary-only. Each scope-condition violation corresponds to an AAT capability that admits identification:

| Route | Scope violated | AAT capability | Detection strength |
|---|---|---|---|
| (a) Loop-interventional access | (i) on-policy | #der-loop-interventional-access — $do(\cdot)$ on the agent's input | Sharp in linear-Gaussian sub-scope; robust qualitative general |
| (b) Higher-moment / out-of-regime | (ii) in-regime + (iii) summary-only | Beyond sub-scope $\alpha$: higher-moment statistics of the innovation; out-of-regime sampling | Provably void in linear-Gaussian sub-scope; informative in nonlinear sub-scope $\beta$ |
| (c) Architecture instrumentation | (iii) summary-only (white-box) | Direct read of the update rule or internal state; same kind as Instance 2's "instrument the latent" | Strongest when available |

**Route (a) — loop-interventional access (sharp).** A $do(\cdot)$ intervention on the agent's input perturbs the system along *similarity-fiber directions that on-policy data never excites*. The interventional response (correction-function Jacobian probed off the on-policy manifold) is *not* similarity-invariant: $T F T^{-1}$ and $F$ respond differently to a probe in a fixed external basis. The intervention generates Level-2 data; the §"No-Go Theorem" derivation is a Level-1-only statement. Genuinely escapes the orbit degeneracy.

**Route (b) — higher-moment / out-of-regime (sub-scope-bounded).** In the nonlinear sub-scope $\beta$, two agents matched at $(\alpha, R)$ and second-order generally differ at moments of order $\geq 3$. In the linear-Gaussian sub-scope this route is *provably void*: a Gaussian innovation carries no information beyond second order, so higher-moment observation adds nothing — the similarity orbit remains invisible. The "escape exists here, provably not there" boundary is exactly the kind of sharp scope-statement that makes a floor instance informative.

**Route (c) — architecture instrumentation.** Direct read of the update rule or internal state breaks the black-box scope: the observer now has access to the basis $T$ itself, not just its annihilated projection onto the on-policy observation law. Structurally the same kind as Instance 2's escape (i) ("instrument the latent" — #deriv-edge-credence-dynamics Prop B.7); genuinely distinct from (a) and (b) in *what the observer must have* (white-box access versus interventional access versus moment-level access).

**Route (d), horizon extension under the same policy — does not escape.** Passive observation at longer horizons under the *same* on-policy execution generates more *samples* of the same observation law; the §"No-Go Theorem" derivation is a statement about the *law* (the architectural content is annihilated by the spectrum map), not about the sample size. Horizon extension that takes the agent *out of the current regime* is no longer the same policy in the same regime — that is a regime change, which is structurally an exogenous intervention-like event, collapsing into route (a)/(b). Route (d) is therefore either void (same regime) or a special case of (a)/(b); the count of structurally distinct escapes is **three**, not four.

### Why Fano Is the Finite-Sample Refinement, Not the Exact Anchor

*[Derived (fano-degeneracy-at-zero-information), exact]*

A Fano-style anchor (Fano 1961, *Transmission of Information*) gives a lower bound on prediction error probability *given* a bound on the channel mutual information $I(A; \text{obs})$ between the architectural variable and the observation. Under the similarity-orbit construction, the on-policy observation law is *identical* for $A$ and $A'$ — not merely close — so $I(A; \text{obs}) = 0$ exactly. Fano degenerates to the trivial bound "error probability $\geq$ prior," vacuous and strictly weaker than the *exact* Kalman-Ho indistinguishability statement.

Fano is therefore the right tool for the *approximate / finite-sample* version of the no-go — architectures that are close but not equal in innovation spectrum, $I \gt 0$ small — and the wrong tool for the *exact* population-level no-go. The exact anchor is Kalman-Ho; Fano is honest open follow-on work on the finite-sample refinement, distinct from the floor itself. (Cross-reference: `#der-agent-opacity` Working Notes record the parallel finding from the observer-side $H_b$ task.)

### Strengthened Consequence

*[Derived (third-mode-of-interventional-access)]*

The no-go elevates `#der-loop-interventional-access` to a load-bearing role at the *agent-internal* layer — the third semantically distinct deployment mode after:

1. **Mode 1: agent-self-intervention** — Instance 1's escape, breaking a *causal-sufficiency* degeneracy among the agent's action propositions ( #der-causal-insufficiency-detection).
2. **Mode 2: observer-on-sub-agent intervention** — Instance 3's escape, breaking a *coupling-sign* degeneracy across composite sub-agents ( #deriv-critical-mass-composition).
3. **Mode 3: observer-on-agent-input intervention** — this segment's escape, breaking a *similarity-orbit* degeneracy on the agent's internal architecture.

The three modes are *different group-theoretic objects*: each breaks a Level-1 degeneracy of a distinct kind, yet shares the load-bearing content "Level-2 data is the unique broadly-available violation of the Level-1 no-go." This converts the Instance-4 floor from "yet another no-go" into structural confirmation that `#der-loop-interventional-access` carries the same load-bearing role at *three* distinct AAT layers (action, composite, architecture), each escape preserving the framework's existing scope honesty rather than introducing new machinery.

### Tier

*Exact* in the linear-Gaussian / Kalman sub-scope ($\alpha_1$), anchored by Kalman-Ho canonical-form non-uniqueness. *Robust qualitative* in the general sub-scope, anchored by CHT-at-agent-as-SCM. **The exact / robust-qualitative tier boundary is load-bearing and must be carried consistently** — collapsing to flat "exact" overclaims the general case; collapsing to flat "robust qualitative" understates the sub-scope's sharpness. The mechanism reduction (§"Mechanism") is exact: the Fisher-null factorization through similarity-invariants follows in elementary steps from the §"No-Go Theorem" derivation.

The escape-count statement ("three structurally distinct escapes, with the proposed fourth collapsing into the first") is *exact* — the collapse of route (d) into (a) and the void of route (b) inside the linear-Gaussian sub-scope are both elementary consequences of the no-go statement itself. The escape-machinery mappings are *robust qualitative*, inheriting the tier of the cited segments ( #der-loop-interventional-access, #der-agent-opacity).

## Epistemic Status

*Conditional.* Max attainable: *exact* for the Kalman-Ho derivation in the linear-Gaussian sub-scope; *robust qualitative* for the general case via CHT-at-agent-as-SCM; *exact* for the mechanism reduction to Instance-2 Fisher-null on a Lie-group fiber; *exact* for the escape count (three, not four) and for the Fano-degeneracy-at-$I=0$ observation; *robust qualitative* for the escape-machinery mappings.

**Load-bearing:**
- The Kalman-Ho construction makes the architectural-identifiability no-go *exact in a precisely characterized sub-scope* — replacing the prior sketch-grade framing ( #der-agent-opacity Working Notes' candidate-status for a generic observer-side floor).
- The mechanism reduction to Instance-2 Fisher-null on a $GL(n)$ fiber places the no-go in the rank-collapse subclass $\{$Instance 1, Instance 2, Instance 4$\}$ via Sylvester at one remove, repairing `#disc-identifiability-floor`'s Sylvester-mechanism taxonomy to three rank-collapse members plus one projection/closure member ($\{$Instance 3$\}$).
- The three-mode classification of `#der-loop-interventional-access` (causal-sufficiency / coupling-sign / similarity-orbit) is a structural unification across three identifiability-floor instances.

**Not established:**
- The general (non-linear-Gaussian) sub-scope at *exact* tier. CHT-at-agent-as-SCM is robust-qualitative; an explicit construction-grade no-go in general sub-scope $\beta$ is honestly open.
- The finite-sample Fano refinement (architectures close-but-not-equal in innovation spectrum, $I(A;\text{obs}) \gt 0$ small). Open follow-on direction, distinct from the population-level no-go derived here.
- Sharp characterization of the boundary between similarity orbits and behavioral equivalence classes when the agent's nonlinear dynamics admit *partial* spectrum identifiability (the sub-scope-$\beta$ moment-cascade question).

## Honest Limits

- **Linearization scope.** The Kalman-Ho construction operates on the *linearized* closed-loop residual dynamics. Sector-condition-satisfying agents ( #deriv-sector-condition) admit such linearization in a basin around the singular trajectory; the no-go's exact tier inherits that scope. Outside the basin, the general-case CHT anchor applies but the construction is not closed-form.
- **Action-marginal invariance vs. internal-coordinate freedom.** Per `#scope-agent-identity`, the action space is coordinate-free and observed quantities are parameterization-invariant. The similarity orbit is a *different* invariance — internal to the realization manifold, distinct from action-marginal parameterization-invariance — and the no-go is about identifying the internal architecture, not about action-level identifiability.
- **Closed-loop residual dynamics, not open-loop plant.** The no-go is stated for the closed-loop $\delta$-dynamics ( #def-mismatch-signal) — what the on-policy observer actually sees. Open-loop plant identification from interventional experiments is route (a) and is *not* subject to this no-go.

## Discussion

**Position in the identifiability-floor pattern.** This no-go is the fourth instance of `#disc-identifiability-floor` and the third member of the rank-collapse subclass via Sylvester at one remove. The Sylvester-mechanism Discussion of the meta-segment ( #disc-identifiability-floor §Discussion) is repaired by this addition: the three-rank-collapse taxonomy is $\{$Instance 1, Instance 2, Instance 4$\}$ unified by congruence-preserves-inertia at the escape-irreducibility layer; Instance 3 stands alone as the projection/closure obstruction. The plurality-of-mechanism that makes the floor pattern a *family* rather than a single theorem is preserved (Sylvester for rank-collapse, Schur/projection for composition); the Sylvester-side is strengthened from two to three members.

**Why Instance-2's mechanism, not new.** The Fisher-null direction here is a $GL(n)$ Lie-group fiber rather than the single mixture-indeterminacy manifold of Instance 2, but the *kind* of obstruction is identical: a rank-deficient observed-Fisher along a structurally-forced indeterminacy manifold. Naming it a new mechanism would be inflation — the AAT-distinctive recognition is precisely that the architectural d.o.f. AAT cares about (`#der-agent-opacity`'s "which internal mechanism") is the similarity orbit and that the orbit is annihilated by the on-policy observation map; the obstruction theorem itself is the same shape as Instance 2. Naming it Sylvester-for-free would be the opposite inflation — similarity and congruence are different group actions. The honest position is "Instance-2 mechanism on a Lie-group fiber, Sylvester at one remove on the escape."

**Relationship to `#der-agent-opacity`'s observer-indexed $H_b$.** This segment's no-go is structurally distinct from a generic observer-prediction-of-action floor: the architectural d.o.f. is invisible *at the observation-law level* regardless of observer instrumentation, not because of a particular observer's filtration. An observer with arbitrarily fine $\mathcal{F}_B^t$ over the on-policy summary distribution still cannot escape the similarity orbit; the observer-indexing of $H_b$ is orthogonal. The natural relationship is at the meta-pattern level (both name floors in the family of `#disc-identifiability-floor`); the *quantities* are distinct ($H_b$ is observer-conditional action entropy; this segment's invariant is the similarity orbit).

**Conservative integration with the Sylvester recognition.** The 2026-05-14 Sylvester-recognition Finding in `#disc-identifiability-floor` taxonomized two rank-collapse floors (Instances 1, 2) and explicitly said *"the floors do not share one mechanism — Sylvester for rank-collapse, a projection/closure obstruction for composition."* This segment's addition does not contradict that recognition; it extends the rank-collapse subclass to three members and preserves the projection/closure distinction for Instance 3. The plurality-as-feature framing of the meta-segment's Discussion is intact.

**Multi-agent / Hafez bridge.** The architectural d.o.f. that this no-go identifies as un-recoverable from on-policy summary data is structurally adjacent to `#der-agent-opacity`'s $H_b$ in this sense: both quantities concern the *world's view of the agent's internal architecture* through information-theoretic limits. The Hafez et al. 2026 IDT pattern (Information Digital Twin, bi-predictability $P$) — operationally a low-$H_b$-preserving observation channel — is a structurally-instrumented escape, and its 89% perturbation-detection performance is consistent with this segment's route (c) "architecture instrumentation" classification.

## Findings

### Architecture No-Identifiability from On-Policy Summary Data — the Fourth Identifiability Floor

**Brief:** Imagine two agents that both keep a desk tidy by the same rules: same overall reaction speed, same tolerance for clutter, same long-run mess level. One agent reasons by tracking pile heights; the other tracks distances between piles. Watching them work — under their normal habits, summary statistics only — you literally *cannot tell which one is running*. The visible behavior is the same, the variability is the same, the rate of clean-up is the same, the cluttered ceiling is the same. Different inner mechanisms, identical outer signature. There are only three honest ways to tell the agents apart: poke one in a way it wouldn't normally do (intervention), look at fine-grained details its rules would not normally generate (out-of-regime / higher-moment observation), or open the hood and read the wiring (white-box access). And a fourth pretender — "just watch longer" — does *not* work, because watching longer accumulates more samples of the same signature, never the missing distinction. This is the floor: it is structurally impossible to recover the inner-mechanism information from the outer summary alone, and the only paths forward are exactly the three named escapes, each of them violating a clearly-stated scope condition.

**Impact:** Closes the long-contested fourth instance of `#disc-identifiability-floor` with a sharp, dual-anchored no-go (Kalman-Ho linear-Gaussian sub-scope, exact; CHT-at-agent-as-SCM general, robust qualitative). Extends the Sylvester-mechanism rank-collapse subclass to three members $\{$Instance 1, Instance 2, Instance 4$\}$ via the at-one-remove escape-irreducibility, while preserving the projection/closure distinctness of Instance 3 — the plurality-of-mechanism that makes the floor pattern a presentational family rather than a single theorem stays intact, sharpened. Elevates `#der-loop-interventional-access` to a third semantically-distinct deployment mode (agent-internal architecture, alongside agent-self-intervention and observer-on-sub-agent), unifying the strengthened-consequence content of three identifiability-floor instances under one piece of machinery. The result mathematically settles the Regime-C confound of the rho-decomposition ( #result-mismatch-decomposition + #internal-external-decomposition) as the same object projected onto the disturbance-statistic coordinate — one decision, not two.

**Novelty Claim:** *Claim derivation* of the architecture-noidentifiability floor with named scope (linear-Gaussian sub-scope, on-policy summary access) and named dual anchor (Kalman 1963 / Ho-Kalman 1966 / Anderson-Moore 1979 §10.4 for the sharp sub-scope; Bareinboim, Correa, Ibeling & Icard 2022 for the general case). The Kalman-Ho canonical-form non-uniqueness theorem is classical (1963/1966); the AAT-distinctive content is *recognizing* that the architectural degree of freedom the framework cares about — `#der-agent-opacity`'s "which internal mechanism" — *is* the similarity orbit, and that the orbit is annihilated by the on-policy observation map. *Claim differentiation* on mechanism: the obstruction is Instance-2's Fisher-null along a structurally-forced indeterminacy manifold (the manifold being a $GL(n)$ Lie-group fiber) rather than a new mechanism, with Sylvester preserving inertia on the escape side identically to Instance 2 — a *member* of the rank-collapse subclass, not a new mechanism family. *Claim recognition* that the previously-proposed Fano anchor degenerates at $I(A;\text{obs}) = 0$ (vacuous lower bound on prediction error under a zero-information channel), so Kalman-Ho is the exact-population anchor and Fano is the finite-sample refinement — a demonstrated no-go on the proposed Fano anchoring, not an assertion.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| State-space realization non-uniqueness up to similarity (the sharp sub-scope anchor) | Kalman, R. E. (1963), "Mathematical description of linear dynamical systems," *J. SIAM Control* 1(2):152–192; Ho, B. L. & Kalman, R. E. (1966), "Effective construction of linear state-variable models from input/output functions," *Regelungstechnik* 14:545–548; Anderson, B. D. O. & Moore, J. B. (1979), *Optimal Filtering*, Prentice-Hall, §10.4 — minimal realizations sharing an innovation spectrum form a similarity-equivalence class | *formal antecedent* — adopted with citation; AAT-distinctive recognition is that the architectural d.o.f. of `#der-agent-opacity` *is* the similarity orbit |
| Causal Hierarchy Theorem (the general-case anchor) | Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022), "On Pearl's Hierarchy and the Foundations of Causal Inference," in *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM | *formal antecedent* — applied at the agent-as-SCM layer; same anchor Instance 1 uses, here in the agent-internal-architecture setting |
| Fano's inequality (finite-sample refinement, not the exact anchor) | Fano, R. M. (1961), *Transmission of Information*, MIT Press; Cover, T. M. & Thomas, J. A. (2006), *Elements of Information Theory*, Wiley, §2.10 | *adjacent* — vacuous at $I = 0$ for the exact construction; the right tool for the finite-sample architectures-close-but-not-equal version of the no-go (honest open) |
| Sylvester's law of inertia (escape-irreducibility, at one remove) | Sylvester, J. J. (1852), *Phil. Mag.* 4(23):138–142; Horn, R. A. & Johnson, C. R. (2013), *Matrix Analysis* (2nd ed.), Thm 4.5.8 | *formal antecedent* — applied here to the *escape* side (congruence on the observed-Fisher), distinct from the generating action (similarity on the realization manifold). Sylvester forbids the escape by reparameterization identically to Instance 2 |
| Fisher-information reparameterization law | Lehmann, E. L. & Casella, G. (1998), *Theory of Point Estimation* (2nd ed.), §2.5 — $\mathcal G_\varphi = S^\top \mathcal G_\theta S$ as the standard congruence law | *formal antecedent* — the law that makes the escape-side reparameterization a congruence action |
| Hafez et al. 2026 / IDT bi-predictability | Hafez, A. M., Khan, F. M. & Iqbal, M. (2026), *A Mathematical Theory of Agency and Intelligence* — IDT pattern, bi-predictability $P$ | *adjacent* — IDT-as-architecture-instrumentation is route (c) of this segment's escape structure; the 89% IDT detection rate is consistent with white-box access escaping the orbit |

**Search Log:**
- 2026-05 (*targeted*): Kalman 1963 / Ho-Kalman 1966 / Anderson-Moore 1979 §10.4 verified as the canonical-form-non-uniqueness anchors; CHT-at-agent-as-SCM application of Bareinboim et al. 2022 verified consistent with Instance 1's general-sub-scope use. Fano 1961 ↔ Cover-Thomas §2.10 verified for the finite-sample refinement framing. Sylvester 1852 + Horn-Johnson Thm 4.5.8 + Lehmann-Casella §2.5 inherited from the 2026-05-14 Sylvester-recognition Finding in `#disc-identifiability-floor`.
- 2026-04 / 2026-05 (*intuition-only*) on whether the cross-instance recognition "the architectural d.o.f. AAT cares about *is* the similarity orbit, annihilated by the on-policy observation map" has been articulated in the system-identification or causal-inference literatures as the AAT-internal-agent-theory framing applied to multi-agent identifiability. The constituent pieces (Kalman-Ho canonical-form non-uniqueness; CHT-at-agent-as-SCM; Fisher rank-deficiency along Lie-group fibers) are textbook; the cross-instance unification as the fourth member of an integrated agent-theoretic floor pattern appears to be a presentational contribution under cursory search. Targeted future search candidates: system-identification literature on the agent-theoretic interpretation of canonical-form non-uniqueness; observability / identifiability literature for nonlinear agents; mechanism-grounded identifiability in multi-agent reinforcement learning.

## Working Notes

- **Provenance.** The architectural-noidentifiability floor was previously sketched in `spikes/.integrated/spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` §8 / §10.1 (candidate, Fano anchor proposed but uncompleted) and surfaced from the disturbance-statistic coordinate as the Regime-C confound of `spikes/.integrated/spike-rho-structure-recheck-2026-05-18.md` §3 (same object). The 2026-05-18 resolution spike `spikes/.integrated/spike-identifiability-floor-instance4-resolution-2026-05-18.md` re-derived the no-go independently and supplied the Kalman-Ho construction, the mechanism reduction to Instance-2-on-a-fiber, the escape audit, and the Fano-degenerates-at-$I=0$ no-go on the proposed Fano anchor; the math-gate trail at `spikes/.routing-trail/SPIKE-VERIFY-471802/` (confirmer ≠ author) cleared the substantive math conditional on three named repairs that are applied in this segment: (i) the "identical" claim restricted to similarity-invariant summaries (not raw moments); (ii) the Lyapunov-equation sign matching `#deriv-sector-condition`'s standard form ($F\Pi + \Pi F^\top = \sigma_w\sigma_w^\top$); (iii) the exact / robust-qualitative tier boundary carried consistently rather than collapsed to flat exact.

- **Finite-sample Fano refinement is honestly open.** The Fano-style bound on the *approximate* version (architectures close-but-not-equal in innovation spectrum, $I(A;\text{obs}) \gt 0$ small) is real research, distinct from the population-level Kalman-Ho no-go. Candidate spike for a future cycle; not blocked by anything here.

- **General non-Gaussian sub-scope at exact tier.** The CHT-at-agent-as-SCM general-case anchor is robust-qualitative. An explicit construction-grade no-go in the nonlinear sub-scope $\beta$ would upgrade the general case to exact-with-conditions; honestly open.

- **The mechanism reduction's relationship to operator-sector machinery.** The §"Mechanism" section's recognition that the Fisher-null here is a rank-deficiency on a $GL(n)$ Lie-group fiber places it in the stability-certificate spine's *boundary facet* ( #disc-stability-certificate, #disc-identifiability-floor) at the same level as Instance 2's mixture-indeterminacy manifold. Whether the Lie-group-fiber generalization of Instance 2's mechanism is worth its own meta-statement (a "Fisher-null-along-structurally-forced-manifold" sub-pattern of the rank-collapse subclass) is open architectural taxonomy.
