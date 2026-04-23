---
spike: jacobian-b1-strengthening
date: 2026-04-23
status: exploratory
trigger: `msc/spike-contraction-metric-generalization.md` §8.2 item 1 and §9 question 1 flagged the central open left behind by the contraction-metric spike: the metric-α₂ promotions (info-metric Kalman, Fisher-metric exp-family, Hessian-metric strongly-convex, Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID-bounded-plant) land as `derived conditional on theorem-import from Lohmiller-Slotine 1998 / Slotine 2003` rather than `derived AAD-internally`. Attempt the improbable: lift (CT2) to an AAD-internally-forced condition via a Jacobian-level strengthening B1* of `#gain-sector-bridge`'s directional fidelity axiom.
posture: Strengthen-first. Attempt composition-consistency forcing (Angle 1) and bridge-lemma equivalence (Angle 2) before retreating. Ruthlessly apply `#additive-coordinate-forcing`'s 1-anchor-2-theorem motivation discipline — an axiom that "feels natural" is not the same as an axiom motivated by an existing AAD commitment.
relates_to:
  - gain-sector-bridge
  - sector-condition-derivation
  - sector-persistence-template
  - composition-closure
  - composition-consistency
  - additive-coordinate-forcing
  - discussion-separability-pattern
  - critical-mass-composition
  - msc/spike-contraction-metric-generalization.md
  - msc/spike-bridge-lemma-contraction.md
  - msc/spike-a2-prime-strengthening.md
---

# Spike: Can B1 Be Strengthened to a Jacobian-Level Condition B1*?

## Problem statement

`#gain-sector-bridge` carries the directional fidelity axiom (B1):

$$\delta^T H\, g(\delta) \geq c\, \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R. \tag{B1}$$

This is an *integral / inner-product-at-a-point* condition: B1 fixes one scalar inequality per state $\delta$. Together with the gain-based update form, B1 derives A2' (the Euclidean sector condition) via the identity $F = \eta^\ast H g$. The gain-sector bridge is AAD-internally derived within sub-scope $\alpha$ (Bayesian / exp-family / strongly-convex-gradient / L2-regularized / linear-PD), with B1 traced to Bayes-risk minimization or gradient-of-convex-loss structure.

`msc/spike-contraction-metric-generalization.md` promoted the template to `#contraction-template` (R1 landing) with the differential-contraction precondition

$$-\dot M - M\frac{\partial F}{\partial \xi} - \Big(\frac{\partial F}{\partial \xi}\Big)^T M \preceq -2\lambda M \tag{CT2}$$

and showed — in §1.2 — that **(CT2) with $M = I$ is strictly stronger than (T2)**; it is equivalent to `#composition-closure`'s DA2'-inc, the *incremental* sector bound (strong monotonicity of $F$ across the whole state space). The metric-α₂ promotions (matrix Kalman in information metric, exp-family in Fisher metric, Hessian-metric strongly-convex, Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID-bounded-plant, basin-chart non-convex-within-basin) land there via direct appeal to Lohmiller-Slotine 1998 / Slotine 2003 *as external theorems* — not via AAD-internal derivation.

The question this spike attacks:

> **Can AAD's B1 be strengthened to a Jacobian-level B1\*** such that (CT2) *and* its metric-α₂ consequences become AAD-internally derived rather than theorem-imported, with B1\*'s motivation matching the discipline that `#additive-coordinate-forcing`'s 1-anchor-plus-2-theorem characterization sets for the divergence and update layers?

The acid test — following the spike instructions and `#additive-coordinate-forcing`'s discipline — is the *AAD-internal motivation of the strengthened axiom*, not its mathematical validity. An axiom that "feels natural" is not the same as an axiom motivated by an existing AAD commitment (the way the chain layer motivates the divergence and update axioms).

The honest outcomes admissible to this spike:

- **(L1) Lift.** Some AAD-internal axiom forces B1\*, which is equivalent to (CT2) under $M = I$ and the natural metric-α₂ metrics. Metric-α₂ promotes to AAD-internally derived.
- **(L2) Mixed lift.** Some pieces of the strengthening are AAD-internal (e.g., the integration-at-zero identity, the composite-level Jacobian-condition under composition-consistency) while others require imported axioms (e.g., the Euclidean-to-metric coordinate choice). Metric-α₂ lands as partially AAD-internal, partially theorem-imported, with honest labeling.
- **(L3) No lift.** All candidate axioms require imports beyond AAD's existing commitments. Metric-α₂ stays at theorem-import with honest labeling; the negative result records the scope limit.

---

## §1. Precise statement of the target condition

### 1.1 Pointwise B1 and its bridge to A2'

`#gain-sector-bridge`'s B1 and the induced A2':

$$\text{(B1)} \quad \delta^T H\, g(\delta) \geq c\, \lVert\delta\rVert^2 \quad \text{on } \mathcal{B}_R$$

$$\text{(A2' Euclidean)} \quad \delta^T F(\delta) \geq \alpha \lVert\delta\rVert^2 \quad \text{on } \mathcal{B}_R, \qquad F = \eta^\ast H g, \qquad \alpha = \eta^\ast c.$$

This is a **zero-anchored pointwise** condition: it pairs each $\delta$ with $F(\delta)$ against $\delta$ itself. Geometrically, $F(\delta)$ lies in a cone around $\delta$ of apex cosine bounded below by $\alpha / (\lVert F\rVert/\lVert\delta\rVert)$.

### 1.2 The target: B1\* as a Jacobian-level condition

The target strengthening, in coordinate-free form:

$$\text{(B1*-Euclidean)} \quad \Big(\frac{\partial F}{\partial \delta}(\delta)\Big)_{\text{sym}} \succeq c_J\, I \quad \forall\, \delta \in \mathcal{B}_R, \tag{B1*-E}$$

i.e., the symmetric part of the Jacobian of $F$ at *every* state $\delta$ is uniformly positive-definite. Equivalently — the standard lemma relating monotonicity to symmetric-Jacobian (Rockafellar & Wets 1998 *Variational Analysis* Cor 12.4; Nesterov 2004 §2.1.3) — for $C^1$ $F$:

$$\text{(B1*-incremental)} \quad (\delta - \delta')^T (F(\delta) - F(\delta')) \geq c_J\, \lVert\delta - \delta'\rVert^2 \quad \forall\, \delta, \delta' \in \mathcal{B}_R. \tag{B1*-inc}$$

This is strong monotonicity of $F$ on $\mathcal{B}_R$. It is `#composition-closure`'s DA2'-inc, stated now at the single-agent level rather than at the composite level. For $C^1$ $F$, (B1\*-E) ⇔ (B1\*-inc).

In metric form:

$$\text{(B1*-metric)} \quad -M\frac{\partial F}{\partial \delta} - \Big(\frac{\partial F}{\partial \delta}\Big)^T M \preceq -2\lambda M. \tag{B1*-M}$$

This is exactly (CT2) for the time-invariant case. So **(B1\*-metric) ≡ (CT2)** when $M$ is time-invariant, and the question "can B1 be strengthened to imply (CT2)" is the same as "can B1 be strengthened to B1\*, with a metric choice."

### 1.3 Euclidean reduction check (Angle 6)

*[Derived]* B1\*-inc implies B1 via setting $\delta' = 0$ and using (A1) $F(0) = 0$:

$$(\delta - 0)^T (F(\delta) - F(0)) \geq c_J \lVert\delta - 0\rVert^2 \;\Longrightarrow\; \delta^T F(\delta) \geq c_J \lVert\delta\rVert^2,$$

which is A2' Euclidean with $\alpha \geq c_J$. This is the "integration-at-zero" reduction. So B1\* genuinely extends B1: any system satisfying B1\* satisfies B1 (with possibly stronger constant). This passes the "is this a strengthening, not a change" check of the spike instructions.

The converse — B1 ⇒ B1\* — fails generically: oscillatory globally-inward corrections satisfy B1 pointwise but fail B1\* (`msc/spike-bridge-lemma-contraction.md` §4.1 exhibits a counterexample). The gap between B1 and B1\* is non-empty; it is precisely the gap between pointwise and incremental.

### 1.4 What B1\* buys if we can motivate it AAD-internally

If B1\* is AAD-internally forced under a single-agent axiom, then:

1. `#gain-sector-bridge` upgrades from "B1 (pointwise) → A2' (Euclidean sector)" to "B1\* (incremental) → (CT2) (Jacobian contraction) → A2' (sector) as corollary."
2. `#composition-closure`'s DA2'-inc becomes the single-agent B1\* applied at the composite level, rather than a separately-posited condition for Tier 1 — the tier structure collapses to metric-α₁ (Euclidean B1\*) / metric-α₂ (non-Euclidean B1\*-M) / metric-β (B1\* fails).
3. `#contraction-template`'s metric-α₂ landings lift from "derived via Slotine theorem-import" to "derived AAD-internally under B1\*-M with metric choice."
4. `#critical-mass-composition`'s (CM2-M) generalization becomes AAD-internally derived rather than Slotine-imported.

This is a substantial architectural move. The question is whether the AAD-internal motivation clears the bar set by `#additive-coordinate-forcing`.

---

## §2. Angle 1: Composition-consistency forcing

**Claim under test.** `#composition-consistency` requires AAD's machinery to apply at every level; `#composition-closure`'s bridge lemma at the composite level already requires the Jacobian-level condition (DA2'-inc / (CT2) with $M = I$); therefore composition-consistency forces B1\* at the single-agent level as an AAD-internal commitment.

### 2.1 What composition-consistency actually says

`#composition-consistency` (Section I postulate): AAD's predictions at different levels of description must be compatible. `#composition-closure` operationalizes this as: bounded closure defect $\varepsilon^\ast$ under admissible coarse-graining, with composite machinery that *has the same shape* as single-agent machinery (A1–A4 admissibility).

The bridge-lemma content of `#composition-closure` §"Bridge lemma":

> The template's precondition (T2) is the one-point sector bound. For the trajectory-error instantiation, the bound propagation requires a **strictly stronger** condition: the macro-update map $f_c(\cdot, o)$ must be contracting in its state argument (**incremental sector bound**, DA2'-inc — strong monotonicity of $F_c$), not merely one-point sector-bounded at each state.

This is the composite-level DA2'-inc requirement. Three tiers result (Tier 1: DA2'-inc globally derivable; Tier 2: locally; Tier 3: per-domain).

### 2.2 Does composite DA2'-inc inherit from agent-level B1?

Consider a parallel composite: $F_c(\xi_1, \xi_2) = (F_1(\xi_1), F_2(\xi_2))$ with block-diagonal structure. The composite Jacobian is $\mathrm{blockdiag}(\partial F_1/\partial \xi_1, \partial F_2/\partial \xi_2)$. If each agent has B1 pointwise (not B1\*), the composite Jacobian's symmetric part can fail to be positive-definite at any specific state even though the pointwise sector condition holds for each sub-agent. *Specifically:* if agent 1 has $F_1(\xi_1) = R_\theta \xi_1$ for a rotation-scaling matrix with small positive-definite component, the one-point $\xi_1^T F_1(\xi_1) \geq c \lVert\xi_1\rVert^2$ can hold while $(\partial F_1/\partial \xi_1)_\text{sym}$ has negative eigenvalues in off-diagonal directions.

*[Derived]* Therefore: **agent-level B1 alone does not imply composite-level DA2'-inc.** `#composition-closure`'s Tier 1 conditions (Bayesian / exp-family / strongly-convex-gradient / linear-PD) all happen to give agent-level *Jacobian-level* monotonicity — they satisfy agent-level B1\*, not just B1. The Tier structure is in fact a structure on which agents satisfy B1\* vs merely B1.

### 2.3 The forcing chain under composition-consistency

*[Formulation (composition-consistency-force)]* Suppose we commit to: **composition-consistency requires that composite-level (A4), as needed for the bridge lemma, be inheritable from agent-level machinery without adding per-composite axioms.** Call this the *heredity commitment*: composite admissibility should be derivable from sub-agent properties plus topology, not from a separate composite posit.

Under heredity, the composite-level DA2'-inc must come from agent-level properties. As §2.2 shows, agent-level B1 is insufficient; agent-level B1\* is sufficient (via parallel composition: block-diagonal Jacobian inherits symmetric-part PD).

*[Derived (conditional on heredity commitment)]* Agent-level B1\* is **necessary** for composition-consistency under heredity, in the following precise sense: there exist admissible single-agent classes (satisfying B1 but not B1\*) whose parallel composite fails DA2'-inc, breaking the bridge lemma without any further AAD-axiom violation. The only way to re-establish composite DA2'-inc is to posit it separately at the composite (violating heredity) or to upgrade agent-level B1 to B1\*.

### 2.4 Is heredity an AAD-internal commitment?

This is the decisive question. `#composition-consistency` states that AAD's machinery should "apply at every level" and be "scale-invariant." `#composition-closure` concedes Tier 1/2/3 — a classification that already tolerates per-composite verification at Tiers 2/3. The honest statement: **heredity is a stronger form of composition-consistency than AAD currently commits to.**

Specifically:

- `#composition-closure`'s Tier 1 is the regime where agent-level properties *happen to* give composite-level contraction. The bridge lemma is derived there via the *coincidence* that Tier 1 agents have agent-level Jacobian monotonicity.
- `#composition-closure`'s Tier 2/3 already concedes that composite-level contraction may require local verification or per-domain argument — i.e., *non*-heredity.
- `#composition-consistency` as a postulate does not commit to heredity; it commits to level-compatibility as the existence of well-defined projections satisfying (A1)–(A4), (P1)–(P3).

So heredity is an *upgrade* to composition-consistency, not an *implication* of it. Adopting heredity-as-axiom would promote Tier 1 to "the scope where heredity is clean" and push Tiers 2/3 outside AAD's formal scope rather than inside it as qualified cases.

### 2.5 Verdict on Angle 1

*[Derived (conditional on heredity commitment), tier: robust qualitative, confidence: high]*

**Angle 1 force-result:** B1\* at the agent level is *equivalent*, under a heredity commitment, to composition-consistency applied at the bridge-lemma level. Stated as a conditional:

> IF `#composition-consistency` is strengthened to the heredity form (composite admissibility derived from agent-level properties without per-composite axioms),
> THEN agent-level B1\* is AAD-internally forced, via the argument that agent-level B1 is insufficient for composite-level DA2'-inc under parallel composition (§2.2).

The conditional is airtight. The open question is whether AAD is willing to adopt heredity as an axiomatic strengthening of composition-consistency.

**Matches the 1-anchor-2-theorem discipline?** The `#additive-coordinate-forcing` pattern has a specific discipline: the axiom is AAD-internally motivated when it is the "divergence-level analog" or "update-level analog" of a chain-level identity. Heredity plays a different structural role: it is a scope-strengthening of an existing postulate, not a decomposition-level analog. The AAD-internal motivation for heredity is "the theory should compose cleanly without per-composite axioms," which is a natural extension of composition-consistency but not in the Cauchy-FE family. **Heredity is AAD-internal, but not via the additive-coordinate-forcing route — it belongs to a different structural family (compositional-closure motivated).**

**Honest landing for Angle 1.** Heredity is a *legitimate* AAD-internal commitment candidate, motivated by the observation that Tier 2/3 in `#composition-closure` are honest scope retreats and heredity-as-axiom would convert them into out-of-scope regimes. Adopting heredity would promote B1\* to AAD-internally-forced. Not adopting it leaves B1\* as theorem-imported from Lohmiller-Slotine. The choice is a load-bearing architectural decision, not a purely mathematical question.

**Composition-consistency path is the most ambitious route identified in this spike, and it works under an explicit commitment.** The spike's instruction to "attempt the improbable first" is vindicated — Angle 1 has a non-trivial positive answer under a clearly-named strengthening.

---

## §3. Angle 2: Bridge-lemma-demand equivalence

**Claim under test.** `#composition-closure`'s DA2'-inc may already be *equivalent* to (CT2) with $M = I$. If yes, AAD has been carrying the Jacobian-level condition at the composite level all along — the strengthening only makes it explicit at the agent level, and B1\* is a natural single-agent predecessor of DA2'-inc.

### 3.1 Precise equivalence

*[Derived]* For $C^1$ $F$ on a convex domain $\mathcal{B}_R$:

(a) **DA2'-inc** ($\langle \delta - \delta', F(\delta) - F(\delta')\rangle \geq c\, \lVert\delta-\delta'\rVert^2$ for all pairs in $\mathcal{B}_R$)

is equivalent to

(b) **Jacobian-symmetric-part-PD** ($(\partial F/\partial \delta)_\text{sym} \succeq c\, I$ pointwise on $\mathcal{B}_R$)

which is equivalent to

(c) **(CT2) with $M = I$** and $\lambda = c$.

*Proof sketch.* (a)→(b): for $\delta' \to \delta$, divide by $\lVert\delta-\delta'\rVert^2$ and take limits; the quadratic form $v^T (\partial F/\partial\delta)_\text{sym} v \geq c \lVert v\rVert^2$ in every direction $v$. (b)→(a): integrate along the segment from $\delta'$ to $\delta$:

$$(F(\delta) - F(\delta'))^T(\delta - \delta') = \int_0^1 (\delta - \delta')^T \frac{\partial F}{\partial\delta}(\delta' + s(\delta-\delta'))(\delta - \delta')\, ds,$$

and the integrand is bounded below by $c \lVert\delta-\delta'\rVert^2$ by (b). (b)↔(c): direct algebraic identity, since (CT2) with $M = I$ and $\dot M = 0$ reads $-(\partial F/\partial \delta) - (\partial F/\partial \delta)^T \preceq -2\lambda I$, equivalent to symmetric part $\succeq \lambda I$. $\square$

*[Result (bridge-DA2-inc-ct2-equivalence), status: exact, tier: robust qualitative]*

**DA2'-inc ≡ (CT2) with $M = I$** for $C^1$ $F$ on convex domains. The equivalence is standard (Rockafellar-Wets 1998 *Variational Analysis* Cor 12.4; Nesterov 2004 §2.1.3) and carries through verbatim to AAD.

### 3.2 Structural consequence: AAD already carries the Jacobian-level condition

`#composition-closure`'s bridge lemma is derived under DA2'-inc for Tier 1 agents. By §3.1, this is the same as (CT2) with $M = I$ for those agents. **AAD has been using the Jacobian-level Euclidean contraction condition at the composite level under the name DA2'-inc, without recognizing it as a Jacobian condition.**

`msc/spike-bridge-lemma-contraction.md` §4.1 identifies the condition as "strong monotonicity of $F_d$" and notes the counterexample (oscillatory corrections that satisfy one-point but fail incremental). The equivalence §3.1 is implicit there but not named — the Lohmiller-Slotine connection was not made.

*[Derived]* The bridge-lemma-demand equivalence means: **AAD's composite-level (CT2)-with-$M=I$ is already AAD-internally committed.** It is the DA2'-inc that composition-closure requires for Tier 1. The question is whether the *agent-level* version — B1\* — is a natural predecessor.

### 3.3 Is agent-level B1\* a natural predecessor of composite-level DA2'-inc?

*[Derived]* Under heredity (Angle 1), yes: agent-level B1\* ⇒ composite-level DA2'-inc via parallel composition (block-diagonal Jacobian), cascade composition (block-lower-triangular Jacobian with symmetric-part bounds via Schur complement), and feedback composition (small-gain). This is the standard Slotine 2003 compositional calculus, now read as "agent-level Jacobian-PD inherits to composite-level Jacobian-PD under characterized topologies."

Without heredity, composite-level DA2'-inc is separately posited. Agent-level B1\* is then not required — AAD could commit to composite-level Jacobian conditions without agent-level ones. This is logically consistent but structurally awkward: the composite-level axiom would float unattached to agent-level machinery.

### 3.4 Verdict on Angle 2

*[Result (angle-2-equivalence-lift), status: exact (the equivalence), conditional (the agent-level promotion under heredity), tier: exact for equivalence, robust qualitative for promotion]*

**Angle 2 force-result:** `#composition-closure`'s DA2'-inc is *already* AAD-internally equivalent to (CT2) with $M = I$. The Jacobian-level condition is not a new import from Lohmiller-Slotine; it is the explicit form of what AAD was already positing at the composite level under a different name.

**Consequence:** The Lohmiller-Slotine theorem-import status of metric-α₁ cases (Euclidean metric, strongly-convex gradient, Kalman-in-Euclidean) **does not apply** — these are AAD-internal via the equivalence §3.1. The theorem-import status applies only to metric-α₂ cases (non-Euclidean metrics: Fisher, Hessian, information, Lyapunov). The spike's opening framing was overly pessimistic on this point.

**Matches the 1-anchor-2-theorem discipline?** Angle 2 establishes a *structural equivalence*, not a Cauchy-FE-forced coordinate. It belongs to the converse-Lyapunov-existence family, not the additive-coordinate-forcing family. `#additive-coordinate-forcing` explicitly classifies the Lyapunov case as an *adjacent family member*, not a primary instance — and the equivalence here is in the Lyapunov family. So Angle 2's lift is AAD-internal **but via the adjacent-family mechanism** (matched coordinate, not forced coordinate), not the primary-family mechanism.

**Honest landing for Angle 2.** The metric-α₁ landings (Euclidean cases) **lift to AAD-internally derived** via the equivalence §3.1 under the DA2'-inc / bridge-lemma framework already in `#composition-closure`. The metric-α₂ landings (non-Euclidean cases) remain theorem-imported at this level — Angle 2 does not force the metric choice, only the Jacobian-level structure at $M = I$.

This is a **genuine partial lift**: Euclidean-incremental metric-α₁ → AAD-internal; non-Euclidean metric-α₂ → theorem-imported (Angles 3, 5 revisit). This is the (L2) mixed-lift outcome anticipated in §1.

---

## §4. Angle 3: Parameterization-invariance axiom

**Claim under test.** Axiomatically require B1 to be parameterization-invariant. AAD-internal motivation: the theory should not depend on arbitrary choice of coordinates. If invariance forces the Fisher metric (Čencov 1982), then parameterization-invariant B1 reduces to (CT2) in the Fisher metric for statistical manifolds.

### 4.1 Čencov's theorem

Čencov 1982 (*Statistical Decision Rules and Optimal Inference*, AMS): on a statistical manifold (parameter space of a probabilistic family), the *unique* Riemannian metric invariant under sufficient statistic transformations (Markov morphisms) is the Fisher information metric, up to positive scalar. The theorem extends to finite-dimensional exponential families directly.

### 4.2 Invariance as an AAD-internal axiom?

Consider the candidate axiom:

*[Formulation (parameterization-invariance axiom)]* **(PI)** AAD's directional fidelity axiom should be invariant under the choice of coordinate chart on the state space: if $\delta \mapsto \phi(\delta)$ is a diffeomorphic reparameterization, B1 should hold for $F$ iff it holds for $\phi_\ast F$.

Under (PI), B1's coordinate form would need to transform covariantly — pushing the analysis to Riemannian (or Finsler) geometry. The Euclidean pointwise $\delta^T F(\delta) \geq c \lVert\delta\rVert^2$ is *not* reparameterization-invariant: under a linear reparameterization $\phi(\delta) = A\delta$, it becomes $(A\delta)^T (AF) \geq c \lVert A\delta\rVert^2$ which requires $A^T A$-weighted sector, not Euclidean. So (PI) immediately forces a non-Euclidean sector form.

For statistical-manifold agents (exp-family / conjugate Bayesian / Fisher-natural-gradient), (PI) + Čencov forces the Fisher metric. The sector condition becomes $\delta^T \mathbf{I}(\theta) F(\delta) \geq c \delta^T \mathbf{I}(\theta) \delta$, and B1\* in Fisher metric is (CT2) with $M = \mathbf{I}(\theta)$. This is `spike-contraction-metric-generalization.md` §2.2's Fisher-metric natural-gradient contraction, now derived under (PI) + Čencov.

### 4.3 Is (PI) AAD-internally motivated?

(PI) is structurally appealing: a theory of adaptive agents should not depend on how a particular agent's state is parameterized — different agents with different internal representations of the same underlying dynamics should satisfy (or fail) B1 uniformly. This sits as an extension of `#agent-identity`'s token-level commitment (agents are defined at the trajectory level, not the parameterization level).

However, (PI) has a critical scope limitation: **Čencov's uniqueness theorem requires the manifold to be a statistical manifold.** For non-statistical agents (PID on a physical plant, rule-based agents, human judgment, generic non-probabilistic dynamics), the Markov-morphism invariance group is not defined, and Čencov does not apply. (PI) then admits a family of invariant metrics (any Riemannian metric invariant under the *dynamics*-preserving transformations, which depend on the agent's specific structure), and the uniqueness collapses.

For the five metric-α₂ cases:

- **Fisher-metric exp-family**: (PI) + Čencov forces the Fisher metric uniquely. **Clean AAD-internal derivation under (PI).**
- **Information-metric matrix Kalman**: the information matrix $(P^-)^{-1}$ is the Fisher metric on the Gaussian posterior family. (PI) + Čencov applies. **Clean AAD-internal derivation under (PI).**
- **Hessian-metric strongly-convex**: the Hessian is a Riemannian metric on the parameter space induced by the loss, not by a statistical structure. (PI) alone does not force the Hessian over other loss-derived metrics; the optimization-theoretic motivation for the Hessian (natural gradient of $L$) is external. **(PI) does not lift.**
- **Lyapunov-metric linear-Hurwitz**: the Lyapunov metric solves a specific Lyapunov equation; it is selected by the *plant structure*, not by an invariance property. **(PI) does not lift.**
- **Lyapunov-metric PID-bounded-plant**: same structural issue. **(PI) does not lift.**

### 4.4 Verdict on Angle 3

*[Derived (conditional on PI adoption and statistical-manifold scope), tier: robust qualitative, confidence: high for Fisher cases, low for non-Fisher cases]*

**Angle 3 force-result:** (PI) is an AAD-internally motivated axiom candidate (it matches `#agent-identity`'s scope commitment that AAD is agent-trajectory-level, not parameterization-level). Under (PI), Čencov's theorem forces the Fisher metric uniquely **on statistical manifolds**. For the *statistical* metric-α₂ cases (Fisher-metric exp-family, information-metric matrix Kalman), (PI) + Čencov lifts the theorem-import to AAD-internal.

**Scope limit.** (PI) does *not* force the coordinate choice for non-statistical metric-α₂ cases (Hessian gradient, Lyapunov linear-Hurwitz, Lyapunov PID-bounded-plant). For these, the metric is selected by problem structure (Hessian of loss, solution of Lyapunov equation) rather than by an invariance group. **Two of five metric-α₂ cases lift under (PI); three stay theorem-imported.**

**Matches the 1-anchor-2-theorem discipline?** (PI) is closer to the Cauchy-FE pattern than Angle 2's equivalence — it invokes a uniqueness theorem (Čencov) on an AAD-internally-motivated axiom (reparameterization invariance). The structural analog is:

- *Chain layer*: chain rule (identity) + log coordinate forced.
- *Divergence layer*: chain-rule additivity axiom + reverse-KL coordinate forced (Hobson-Csiszár-Shore-Johnson).
- *Update layer*: evidential additivity axiom + log-odds coordinate forced (Aczél).
- *(PI) statistical layer*: reparameterization invariance axiom + Fisher metric forced (Čencov).

This is genuinely parallel! The Fisher metric on statistical manifolds is the uniqueness-theorem-forced coordinate under an AAD-internal axiom (reparameterization invariance / agent-trajectory-level invariance), with Čencov 1982 playing the role that Aczél 1966 and Hobson 1969 play for the divergence and update layers.

**This suggests (PI) could be a fourth primary instance of `#additive-coordinate-forcing`** — but via a *metric-uniqueness* theorem (Čencov) rather than a *functional-equation* uniqueness theorem (Cauchy). The existing pattern is Cauchy-FE on an additivity axiom → logarithmic coordinate forced. The (PI) pattern would be Čencov uniqueness on an invariance axiom → Fisher metric forced. These are both uniqueness-theorem-forced coordinates under AAD-internally-motivated axioms, but they are different structural families (Cauchy-FE vs Čencov-invariance). `#additive-coordinate-forcing` already flags this possibility in its Working Notes §Lyapunov-and-the-Fisher-information-extension as "a sub-question of the G-BP3 scoping spike."

**Honest landing for Angle 3.** (PI) is an AAD-internal axiom candidate, structurally parallel to the additive-coordinate-forcing motivational discipline (uniqueness theorem on an AAD-motivated axiom), but via Čencov's theorem rather than Cauchy-FE. It lifts **two of five** metric-α₂ cases (the statistical ones: Fisher exp-family, information-metric Kalman) to AAD-internal; it does **not** lift the three non-statistical metric-α₂ cases. This is a **structurally clean partial lift**.

---

## §5. Angle 4: Incremental-B1 axiom (the direct Jacobian-level strengthening)

**Claim under test.** Directly adopt B1\*-inc as an axiom, motivated as "directional fidelity should hold between nearby states, not just at a single state." AAD-internal motivation: robustness of the B1 property to small perturbations of the state.

### 5.1 The axiom

*[Formulation (incremental-B1 axiom)]* **(B1*)** For all $\delta, \delta' \in \mathcal{B}_R$:

$$(\delta - \delta')^T H (g(\delta) - g(\delta')) \geq c_J \lVert\delta - \delta'\rVert^2. \tag{B1*}$$

By §1.3 Euclidean reduction, (B1\*) ⇒ B1 (pointwise). (B1\*) is strong monotonicity of $Hg$ on $\mathcal{B}_R$, which gives strong monotonicity of $F = \eta^\ast H g$, which by §3.1 is equivalent to (CT2) with $M = I$.

### 5.2 AAD-internal motivation for (B1\*)

Three candidate motivations:

**(M1) Robustness to state perturbation.** B1 asserts directional fidelity *at a state*; (B1\*) asserts directional fidelity *between nearby states*. A natural interpretation: if the agent's update rule has B1 at $\delta$, and $\delta'$ is a small perturbation of $\delta$, the update rule should also have directional fidelity at $\delta'$ in a way that *varies smoothly* with state. (B1\*) is the infinitesimal form of this smoothness.

Is this AAD-internal? AAD commits to smooth update rules in sub-scope $\alpha$ (Bayesian / gradient / linear-PD are all smooth); rule-based and discontinuous systems are in $\beta$. So smoothness is already a sub-scope $\alpha$ commitment. (M1) is then a smoothness upgrade of B1: "within sub-scope $\alpha$, directional fidelity should be smooth," which formalized as Jacobian-level gives (B1\*).

However, "smooth" is weaker than "incremental-monotone." A smooth update rule can satisfy B1 without satisfying (B1\*) — the counterexample of rotating-inward corrections in `msc/spike-bridge-lemma-contraction.md` §4.1 is perfectly smooth but violates (B1\*). So smoothness alone does not force (B1\*); the move to (B1\*) requires something stronger than smoothness.

**(M2) Invariance under small state perturbations of the directional-fidelity property.** Stronger than (M1): not only should B1 hold smoothly across states, but the *infimum constant* $c$ in B1 should be bounded below by $c_J > 0$ uniformly — which is (B1\*). This is motivated as: "the sector-condition constant should be uniform over the admissible region, not state-specific." This is already part of `#gain-sector-bridge`'s definition: $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min} = \inf_{\lVert\delta\rVert \leq R} \delta^T Hg(\delta)/\lVert\delta\rVert^2$. So AAD already commits to a uniform lower bound on the pointwise sector ratio — but this is uniformity in the *magnitude*, not uniformity in the *directional monotonicity*.

**(M3) No spurious invariant cycles.** B1 allows oscillatory corrections that are globally inward-pointing but locally non-monotone (the `msc/spike-bridge-lemma-contraction.md` §4.1 counterexample). These correspond to trajectories with invariant cycles inside $\mathcal{B}_R$ that do not converge. (B1\*) rules them out. AAD's persistence results (Props A.1, A.1S, A.2) deliver ultimate boundedness $\lVert\delta\rVert \leq R^\ast$ but do *not* rule out invariant cycles within $\mathcal{B}_{R^\ast}$. The existing template is compatible with oscillatory equilibria. (B1\*) adds monotone convergence to a fixed point. AAD-internal motivation: "adaptation should converge monotonically in some metric, not oscillate indefinitely within the region."

Is (M3) AAD-internally motivated? `#mismatch-dynamics` carries the linear-ODE form $d\lVert\delta\rVert/dt = -\mathcal T\lVert\delta\rVert + \rho$ as "a first-order approximation" — the linear form is monotone convergence. `#sector-condition-derivation` weakens this to the sector condition, which admits non-monotone convergence within $\mathcal{B}_{R^\ast}$. The weakening is intentional — sector conditions accommodate richer nonlinear dynamics — so strengthening back to monotone convergence via (B1\*) is partially a retreat from what sector conditions are designed for.

However: AAD's persistence-cost results (`#persistence-cost`) and the `#critical-mass-composition` closed-form inequalities assume an ultimate-bound *fixed point*, not a non-trivial attractor. The analyses are cleaner under monotone convergence. So (M3) is AAD-internally motivated as "the ultimate bound should be approached monotonically, enabling the fixed-point analyses that downstream segments use."

### 5.3 Verdict on Angle 4

*[Derived (conditional on M1, M2, or M3 acceptance), tier: robust qualitative, confidence: medium]*

**Angle 4 force-result:** (B1\*) as an axiom has three candidate AAD-internal motivations: (M1) smoothness of B1, (M2) uniformity of sector constant, (M3) monotone convergence to fixed point.

Assessed against the 1-anchor-2-theorem discipline:

- (M1) is weaker than (B1\*) — smoothness does not force incremental monotonicity. **Fails.**
- (M2) is already in AAD (uniform $c_{\min}$), but it is uniformity of *magnitude*, not of *directional monotonicity between pairs*. **Partial** — requires an additional "uniform between pairs" upgrade.
- (M3) is AAD-adjacent (enables downstream fixed-point analyses) but sits in partial tension with sector-condition weakenings. **Partial** — defensible but not load-bearingly forced.

**Honest landing for Angle 4.** Direct adoption of (B1\*) as an axiom is AAD-compatible but not AAD-internally *forced* by existing commitments in the way the Cauchy-FE axioms are forced by the chain layer. (B1\*) is a **natural strengthening but not a forced one**. Under (M3), there is a legitimate AAD-internal motivation (monotone convergence to fixed point for downstream analysis), but this is more an *adoption* than a *forcing*.

**Matches the 1-anchor-2-theorem discipline?** (B1\*) on its own does not match the Cauchy-FE discipline because it is not a uniqueness-theorem-forced coordinate; it is a direct axiom strengthening. It matches at best the "adjacent family member" tier of `#additive-coordinate-forcing` (coordinate matched, not forced).

---

## §6. Angle 5: Second-order-curvature axiom

**Claim under test.** The natural metric is induced by the second-order curvature at the fixed point (Fisher for Bayesian, Hessian for gradient, $(P^-)^{-1}$ for Kalman). If the metric choice is AAD-forced by an axiom linking metric to curvature, then (CT2) with that metric becomes AAD-internal.

### 6.1 The axiom

*[Formulation (second-order-curvature axiom)]* **(SOC)** The AAD metric for the contraction condition should equal the second-order curvature of the objective function (log-likelihood, loss, or free energy) at the operating point of the agent, to within a positive scalar.

Specifically: for an agent minimizing a function $\Phi(\delta)$ with minimum at $\delta^\ast$, the AAD metric is $M(\delta) = \nabla^2 \Phi(\delta)$ on $\mathcal{B}_R$, subject to uniform PD.

### 6.2 AAD-internal motivation for (SOC)

The second-order curvature is the natural metric in three structural settings:

- **Bayesian / statistical**: $\Phi = -\log p$ (negative log-likelihood); $\nabla^2 \Phi$ at the posterior mode = Fisher information + prior curvature. This is the local Gaussian approximation, which is AAD-adjacent via `#update-gain`'s optimality characterization.
- **Gradient-on-loss**: $\Phi = L$ (loss); $\nabla^2 L$ is the Hessian. For strongly convex $L$, Hessian is uniformly PD and (SOC) gives the Hessian metric.
- **Kalman**: $\Phi = -\log p(\text{history} \mid \omega)$; $\nabla^2 \Phi$ on the posterior = $(P^-)^{-1}$ (inverse prior covariance + observation Fisher). This matches the information metric.

(SOC) is unifying across these three cases. For non-statistical / non-gradient agents (PID on a physical plant, rule-based), (SOC) is either undefined (no $\Phi$ function) or mis-specified (the "curvature" concept doesn't apply to rule-based dynamics).

### 6.3 Is (SOC) AAD-internal?

Three tests:

**(T-internal-1) Analog of chain-confidence-decay?** The `#additive-coordinate-forcing` motivational discipline requires an AAD-internal axiom that is an "analog of the chain layer." (SOC) is not an additivity axiom — it is a metric-specification axiom. It does not fit the Cauchy-FE discipline.

**(T-internal-2) Motivated by existing AAD commitments?** The existing commitments that (SOC) could be motivated by:

- `#update-gain`'s optimal-gain characterization in sub-scope $\alpha$ (Bayesian gain is posterior mean update weighted by posterior precision). Posterior precision = Fisher information + prior precision, which is the Hessian of the log-posterior. **Yes, (SOC) is motivated for Bayesian agents by `#update-gain`.**
- `#gain-sector-bridge`'s gradient-equivalence characterization (sector condition ↔ strong convexity). Strong convexity is Hessian $\succeq \mu I$; using Hessian as metric is the natural metric for strongly convex optimization. **Yes, (SOC) is motivated for gradient agents by `#gain-sector-bridge`.**
- For non-Bayesian, non-gradient agents (PID, rule-based): no commitment motivates (SOC). **Scope-limited.**

**(T-internal-3) Fits the 1-anchor-2-theorem structure?** The anchor role is played by... what? There is no mathematical identity at the metric level that (SOC) is an analog of. (SOC) is a postulate, not a uniqueness-theorem-forced coordinate.

### 6.4 Verdict on Angle 5

*[Derived (conditional on SOC adoption, scope-limited), tier: robust qualitative, confidence: medium]*

**Angle 5 force-result:** (SOC) is AAD-motivated for sub-scope $\alpha$ (Bayesian / gradient / Kalman) via connections to `#update-gain` and `#gain-sector-bridge`, but the motivation is *domain-specific* rather than uniform. (SOC) lifts the three metric-α₂ cases where the curvature interpretation is natural (Fisher for exp-family, Hessian for strongly-convex gradient, information for matrix Kalman) but does not lift Lyapunov-metric cases (linear-Hurwitz, PID-bounded-plant) because Lyapunov metrics are selected by plant dynamics, not by an objective-function curvature.

**Matches the 1-anchor-2-theorem discipline?** No. (SOC) is a direct metric-specification axiom, not a uniqueness-theorem-forced coordinate. It matches the "adjacent family member" tier only: coordinate chosen to match the problem structure, not forced by an AAD-internal functional-equation.

**Honest landing for Angle 5.** (SOC) is a legitimate axiom candidate, but its status is "domain-specific metric choice aligned with optimization-theoretic commitments" rather than "AAD-internally-forced coordinate." It does not clear the `#additive-coordinate-forcing` discipline. **Three of five metric-α₂ cases lift under (SOC) + domain recognition (statistical / strongly-convex-gradient / Kalman); two do not (Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID-bounded-plant).**

---

## §7. Angle 8: Structural comparison to the 1-anchor-2-theorem pattern

This angle is the acid test of all preceding angles: does *any* candidate B1\* axiom match the motivational discipline set by the Cauchy-FE theorems?

### 7.1 The discipline

`#additive-coordinate-forcing` states the discipline:

> The acid test is the axiom's AAD-internal motivation, not just its mathematical validity... Cauchy-FE uniqueness as a corollary of the axioms rather than an added derivation technique.

And:

> The Lyapunov case therefore belongs to a different structural family — the converse-Lyapunov existence family — not the Cauchy-FE additive-coordinate-forcing family.

The Lyapunov case, under `#additive-coordinate-forcing`, is an *adjacent family member*, not a primary instance. The reason: the quadratic coordinate is *matched* to the sector form, not *forced* by an AAD-internal axiom via a uniqueness theorem.

### 7.2 Structural comparison of the angles

| Angle | AAD-internal axiom | Uniqueness theorem | Coordinate forced? | Structural family |
|---|---|---|---|---|
| 1 (composition-consistency forcing) | Heredity commitment (strengthened #composition-consistency) | — (equivalence, not uniqueness) | (CT2) at $M=I$ via composition | Compositional-closure |
| 2 (bridge-lemma equivalence) | (Existing) DA2'-inc at composite | — (identity, not uniqueness) | (CT2) at $M=I$ via DA2'-inc equivalence | Converse-Lyapunov existence |
| 3 (parameterization invariance) | (PI) reparameterization invariance | Čencov 1982 | Fisher metric (statistical manifolds only) | **Uniqueness-theorem-forced under AAD axiom (statistical scope only)** |
| 4 (incremental-B1) | (M3) monotone convergence to fixed point | — (direct axiom, not uniqueness) | (CT2) at $M=I$ | Converse-Lyapunov existence |
| 5 (second-order curvature) | (SOC) metric-from-curvature | — (domain-specific matching) | Domain-specific (Fisher / Hessian / info) | Matched-coordinate adjacent |

**Only Angle 3 matches the 1-anchor-2-theorem discipline in the strict sense** — and only for *statistical-manifold agents*. It produces Fisher-metric contraction under (PI) + Čencov, structurally parallel to how the divergence and update layers produce their logarithmic coordinates under their axioms + Aczél / Hobson / Csiszár.

Angles 1, 2, 4, 5 establish AAD-internal-lift results of varying strength, but via different structural mechanisms (compositional-closure, converse-Lyapunov, direct axiom, matched coordinate) — not via the primary Cauchy-FE-like uniqueness-theorem-forced family.

### 7.3 What this means for the overall question

**The honest answer is (L2) — mixed lift with layered structure:**

- **Euclidean metric-α₁ (M = I)**: Lifts to AAD-internal via Angle 2 (DA2'-inc equivalence). AAD was already committed to the Jacobian-level condition at the composite level; stating it explicitly at the agent level is making implicit commitments explicit. **Clean lift, converse-Lyapunov-family mechanism.**

- **Statistical metric-α₂ (Fisher exp-family, information-metric Kalman)**: Lift to AAD-internal via Angle 3 (PI + Čencov). This is a uniqueness-theorem-forced coordinate structurally parallel to the Cauchy-FE family, with Čencov playing the uniqueness-theorem role. **Clean lift, uniqueness-theorem-forced family (new instance).**

- **Non-statistical metric-α₂ (Hessian strongly-convex, Lyapunov linear-Hurwitz, Lyapunov PID-bounded-plant)**: No clean AAD-internal lift. (PI) + Čencov does not apply. (SOC) is domain-specific motivation. Angle 4 direct axiom adoption is defensible under (M3) but not forced. **Remains theorem-imported with honest labeling.**

- **Composition-consistency under heredity**: A legitimate AAD-internal strengthening route for B1\* at the agent level. Whether AAD adopts heredity-as-axiom is an architectural decision rather than a mathematical necessity. **Conditional lift.**

---

## §8. Landing map — what this means for the metric spike's promotions

### 8.1 Updated derivation-status table for metric-α₂ cases

| metric-α₂ case | Pre-spike status | Post-spike status | AAD-internal mechanism |
|---|---|---|---|
| Scalar / matrix Kalman (information metric) | Theorem-import (Slotine) | **AAD-internally derived** | (PI) + Čencov → Fisher = information metric; Angle 3 |
| Exp-family Fisher-metric (natural-gradient) | Theorem-import (Slotine) | **AAD-internally derived** | (PI) + Čencov → Fisher metric; Angle 3 |
| Hessian-metric strongly-convex gradient | Theorem-import (Slotine) | **Theorem-import with honest labeling** | (SOC) is domain-specific, not forced |
| Lyapunov-metric linear-Hurwitz-non-symmetric | Theorem-import (Slotine) | **Theorem-import with honest labeling** | Metric from plant dynamics, not AAD-internal axiom |
| Lyapunov-metric PID-bounded-plant | Theorem-import (Slotine) | **Theorem-import with honest labeling** | Metric from plant dynamics, not AAD-internal axiom |
| Non-convex-within-basin (basin-chart) | Theorem-import (Slotine) | **Theorem-import with honest labeling** | Basin-specific metrics, no global AAD-internal axiom |

**Net partial lift:** two of six cases (Kalman and exp-family) promote to AAD-internal under (PI) + Čencov. Four cases stay theorem-imported (Hessian, two Lyapunov-metric cases, basin-chart) with honest labeling.

### 8.2 Updated derivation-status for Euclidean metric-α₁ cases

All Euclidean metric-α₁ cases (scalar Kalman, Euclidean strongly-convex gradient, L2-regularized, linear-PD-symmetric) **lift to AAD-internally derived** via Angle 2's DA2'-inc ≡ (CT2)-at-$M=I$ equivalence. This is a broader lift than expected from the pre-spike framing: AAD was already committed to the Jacobian-level condition at the composite level via `#composition-closure`'s DA2'-inc, and the equivalence §3.1 makes the commitment explicit at the agent level.

### 8.3 Mixed-lift summary

The honest landing is the **(L2) mixed-lift** outcome anticipated in §1:

| Layer | Mechanism | AAD-internal status |
|---|---|---|
| Pointwise B1 / A2' Euclidean | `#gain-sector-bridge` derivation under sub-scope $\alpha$ | AAD-internally derived (pre-existing) |
| Incremental B1\* / (CT2) at $M = I$ | DA2'-inc equivalence (Angle 2) | **AAD-internally derived (new — lifted by this spike)** |
| Fisher-metric / information-metric contraction | (PI) + Čencov uniqueness theorem (Angle 3) | **AAD-internally derived (new — conditional on PI adoption)** |
| Hessian / Lyapunov-metric contraction (three cases) | (SOC) domain-specific or Lyapunov-equation-from-plant | Theorem-imported from Lohmiller-Slotine with honest labeling |
| Composition under heredity | Heredity strengthening of `#composition-consistency` (Angle 1) | Conditional lift — load-bearing architectural decision |
| Adversarial dynamics, rule-based, severely-misspecified | Out of metric scope altogether | Remains β |

### 8.4 Candidate landing for the (B1\*) formulation at segment level

The spike instructions specified the goal: "if B1* is cleanly AAD-internally motivated and implies (CT2), the `#contraction-template` segment lands with metric-α₂ at status `derived` (AAD-internal) rather than `derived conditional on theorem-import`."

**Recommended landing:**

- **`#contraction-template`** (when created per R1 of `msc/spike-contraction-metric-generalization.md`): land metric-α₁ cases at `status: derived` (AAD-internal via DA2'-inc equivalence, Angle 2). Land statistical metric-α₂ cases (Fisher exp-family, information Kalman) at `status: derived, conditional on (PI)` (AAD-internal via Čencov, Angle 3). Land non-statistical metric-α₂ cases at `status: derived, conditional on theorem-import from Lohmiller-Slotine 1998` with explicit labeling.

- **`#gain-sector-bridge`**: optionally add an "Incremental form (B1\*)" paragraph in Formal Expression, stating (B1\*) as the Jacobian-level strengthening equivalent to agent-level DA2'-inc. Status: derived-under-sub-scope-α-heredity-commitment, or optional strengthening under (M3) monotone-convergence motivation. Do not make B1\* the default — pointwise B1 is load-bearing in several existing derivations and the strengthening introduces additional scope commitments (smoothness, monotone convergence).

- **`#additive-coordinate-forcing`**: consider adding Angle 3's (PI) + Čencov route as a fourth primary instance or a strong adjacent-family instance. The structural parallel with the divergence and update layers is genuine (uniqueness-theorem-forced coordinate under AAD-internal invariance axiom) but belongs to the Čencov-uniqueness family rather than the Cauchy-FE family. A framing note on the meta-segment would be appropriate: "The uniqueness-theorem-forced-coordinate pattern is broader than the Cauchy-FE family; it also includes Čencov-invariance on statistical manifolds."

- **`#composition-closure`**: optionally add a Discussion note that DA2'-inc is equivalent to (CT2) with $M = I$, reconciling AAD's nomenclature with the Lohmiller-Slotine vocabulary. This is structural transparency, not a content change.

---

## §9. Honest epistemic assessment

### 9.1 What this spike achieves

1. **Angle 1 — composition-consistency forcing under heredity (conditional positive).** Heredity is a legitimate AAD-internal axiom candidate that would force B1\* at the agent level. It is a strengthening of `#composition-consistency` and is an architectural decision rather than a mathematical necessity.

2. **Angle 2 — DA2'-inc ≡ (CT2) at $M = I$ (exact equivalence).** AAD already carries the Jacobian-level Euclidean-metric condition at the composite level via DA2'-inc. The equivalence is standard (Rockafellar-Wets, Nesterov) and transfers to AAD without modification. Agent-level B1\* is the natural predecessor at the agent level, with composition-hereditary transfer to the composite.

3. **Angle 3 — (PI) + Čencov for statistical-manifold cases (clean primary lift).** Parameterization-invariance as AAD-internal axiom, structurally parallel to `#additive-coordinate-forcing`'s discipline. Čencov's theorem forces the Fisher metric uniquely on statistical manifolds. Two of six metric-α₂ cases (Fisher exp-family, information-metric Kalman) lift to AAD-internally-derived via this route.

4. **Angle 4 — direct incremental-B1 axiom (partial).** Three motivation candidates (smoothness upgrade, uniform sector constant, monotone convergence). (M3) is the strongest and is AAD-adjacent but not AAD-forced. Matches "adjacent family member" tier, not primary.

5. **Angle 5 — second-order curvature (domain-specific).** (SOC) is AAD-motivated for Bayesian and gradient agents via connections to `#update-gain` and `#gain-sector-bridge`, but not for Lyapunov-metric cases. Matched-coordinate adjacent, not forced.

6. **Angle 8 — structural comparison.** The 1-anchor-2-theorem discipline is strict. Only Angle 3 matches the primary Cauchy-FE-like uniqueness-theorem-forced-coordinate family (via Čencov instead of Cauchy-FE). Angles 1 and 2 lift via the converse-Lyapunov / composition-closure family (adjacent). Angles 4 and 5 land at matched-coordinate adjacent.

### 9.2 What this spike does not achieve

1. **Does not force all metric-α₂ cases to AAD-internal.** Hessian-metric strongly-convex, Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID-bounded-plant, and basin-chart non-convex-within-basin remain theorem-imported. No AAD-internal axiom cleanly forces these metric choices.

2. **Does not provide a unified AAD-internal derivation of (CT2) across all sub-scope metric-α agents.** Different sub-cases lift via different mechanisms (Angle 2 for Euclidean, Angle 3 for statistical, theorem-import for the rest).

3. **Does not address sub-scope metric-β.** Rule-based, severely-misspecified, human-judgment, variational stay in β; the spike does not promote them.

4. **Does not resolve whether AAD should adopt heredity as axiom.** This is architectural — a load-bearing decision about the strength of composition-consistency.

### 9.3 Tiering and confidence

| Claim | Tier | Confidence |
|---|---|---|
| DA2'-inc ≡ (CT2)-at-$M=I$ for $C^1$ $F$ on convex domains (Angle 2) | Exact | High (standard Rockafellar-Wets) |
| Euclidean B1 reduces to pointwise from incremental via integration-at-zero | Exact | High |
| Agent-level B1 is insufficient for composite-level DA2'-inc under parallel composition (Angle 1, §2.2) | Derived | High |
| Heredity commitment would force agent-level B1\* (Angle 1) | Derived, conditional on heredity adoption | High for logical chain; heredity itself is axiomatic decision |
| (PI) + Čencov forces Fisher metric uniquely on statistical manifolds (Angle 3) | Derived | High (Čencov 1982 is standard) |
| (PI) does not force coordinate for non-statistical agents | Derived (scope limit) | High |
| (SOC) is domain-specific, not uniformly forcing | Derived (scope limit) | High |
| Angle 4's (B1\*) under motivations (M1)–(M3) matches only adjacent-family tier | Robust qualitative | Medium (depends on interpretation of discipline) |
| Only Angle 3 matches primary-instance Cauchy-FE-like discipline | Robust qualitative | High (structural reading of the discipline) |
| Mixed-lift outcome: Euclidean + statistical metric-α₂ lift; non-statistical metric-α₂ stays imported | Robust qualitative | High |

### 9.4 Overall verdict

**The answer to the spike's central question is (L2) mixed lift.** Partial AAD-internal derivation of (CT2) is achievable under explicit architectural commitments:

- **Euclidean (CT2) at $M = I$** lifts to AAD-internal via DA2'-inc equivalence (Angle 2). AAD was carrying this commitment implicitly at the composite level; making it explicit at the agent level is a structural transparency move.
- **Statistical metric-α₂** ((CT2) at $M = $ Fisher) lifts to AAD-internal via (PI) + Čencov (Angle 3). This is a clean uniqueness-theorem-forced-coordinate result structurally parallel to `#additive-coordinate-forcing`'s divergence and update layers — with Čencov 1982 playing the role that Aczél 1966 and Hobson 1969 play for those layers.
- **Non-statistical metric-α₂** (Hessian, Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID, basin-chart) stays theorem-imported. No AAD-internal axiom cleanly forces these metric choices; the metrics are selected by problem-specific structure (Hessian of a specific loss, Lyapunov equation for a specific plant, basin geometry of a specific $L$).
- **Composition-heredity** is a separate AAD-internal-commitment candidate that would force B1\* at the agent level. Its adoption is architectural, not mathematical.

**The 1-anchor-2-theorem discipline is clarified by this spike.** The discipline separates:

- **Primary instances** (Cauchy-FE-family or Čencov-invariance-family): uniqueness-theorem-forced coordinate under AAD-internally-motivated axiom. Candidates: the three existing Cauchy-FE layers (chain, divergence, update); the new Čencov-invariance layer (Angle 3, for statistical manifolds).
- **Adjacent family members** (converse-Lyapunov, matched-coordinate, composition-hereditary): coordinate implicit in the formulation, motivated by AAD but not forced by a uniqueness theorem. Candidates: `#sector-condition-derivation`'s quadratic Lyapunov; `#information-bottleneck`'s Lagrangian form; Angle 2's DA2'-inc equivalence at $M = I$; Angle 4's direct incremental-B1 axiom; Angle 5's second-order-curvature metric.

`#additive-coordinate-forcing` correctly names three of its existing instances as primary and two (Lyapunov, IB) as adjacent. This spike adds a candidate fourth primary instance (Angle 3, Čencov-invariance) with scope limited to statistical manifolds, and classifies Angles 1, 2, 4, 5 as adjacent-family.

**Strongest takeaway.** Angle 2 alone — the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence — is sufficient to lift the **Euclidean metric-α₁** cases to AAD-internally-derived without any architectural commitment beyond what `#composition-closure` already carries. This is a substantive but under-advertised lift: AAD's existing bridge-lemma requirement already commits to the Jacobian-level Euclidean contraction; the spike makes the commitment explicit.

**Strongest single candidate strengthening.** Angle 3's (PI) axiom is the only candidate that clears the 1-anchor-2-theorem discipline in the strict primary-instance sense. Its scope is limited to statistical manifolds, which is exactly where Čencov applies; non-statistical metric-α₂ cases stay theorem-imported. **If AAD is willing to commit to a "parameterization-invariance" axiom as an extension of its existing `#agent-identity` token-level commitment, two metric-α₂ cases (Fisher exp-family, information-metric Kalman) promote to AAD-internally-derived with a clean structural parallel to the Cauchy-FE theorems.**

**Strongest architectural-decision strengthening.** Angle 1's heredity commitment is the most ambitious candidate. Its adoption would force agent-level B1\* and lift Tier 1/2/3 composition-closure to a cleaner topology-indexed structure. Its non-adoption leaves `#composition-closure`'s tier structure as the honest scope statement. The trade-off: heredity is load-bearing for generalizing `#critical-mass-composition` (CM2) to (CM2-M) heterogeneous composites; without heredity, (CM2-M) remains theorem-imported from Slotine 2003 §IV.

---

## §10. Open questions after this spike

1. **Should AAD adopt parameterization-invariance (PI) as an axiom?** If yes, two metric-α₂ cases (Fisher exp-family, information-metric Kalman) lift to AAD-internally-derived as a fourth primary instance of `#additive-coordinate-forcing` (Čencov-invariance family). If no, these stay theorem-imported. This is a distinct axiomatic decision from the chain / divergence / update triple; its adoption would extend `#additive-coordinate-forcing`'s uniqueness-theorem-forced-coordinate mechanism from functional-equation (Cauchy-FE) to invariance-uniqueness (Čencov).

2. **Should AAD adopt heredity as a strengthening of `#composition-consistency`?** If yes, agent-level B1\* is AAD-internally forced, and `#composition-closure`'s Tier 1/2/3 collapses to a cleaner topology-indexed structure. If no, the current Tier structure remains as the honest scope statement. Trade-off: heredity is needed for (CM2-M) heterogeneous composites.

3. **Is there a unified AAD-internal axiom covering non-statistical metric-α₂ cases (Hessian, Lyapunov)?** The Hessian case is AAD-motivated via `#gain-sector-bridge`'s gradient-strong-convexity equivalence but not via an invariance axiom. The Lyapunov-metric cases are plant-specific (Hurwitz spectrum, PID nominal design), selected by problem structure rather than by an AAD-internal commitment. An AAD-internal axiom that unifies these cases is open.

4. **Is the Čencov-invariance family a fourth primary instance of `#additive-coordinate-forcing`?** The structural parallel in Angle 3 is clean on the uniqueness-theorem-forced-coordinate axis but differs from the existing three instances on the additivity-axiom axis (Čencov is about invariance, not additivity). Promoting Čencov-invariance to a primary instance would broaden the meta-pattern from "Cauchy-FE on additivity" to "uniqueness theorem on structural axiom" — a genuine generalization. Whether this broadening is justified is a meta-segment refinement question.

5. **Interaction with adaptive-metric algorithms.** `msc/spike-adaptive-gain-dynamics.md` (MG-4) coupling-boundedness discusses meta-gain sector conditions. An adaptive-metric analog (learning $M$ alongside $\xi$) has structural parallels. Whether (PI) survives when $M$ is itself adaptive is a subsequent question.

6. **Interaction with `#discussion-identifiability-floor`.** The metric formulation (whether AAD-internal or theorem-imported) is silent on identification. No axiom covered in this spike escapes the identifiability floor; the metric lift and the identifiability floor are orthogonal. A combined Jacobian-level B1\* + identifiability-floor analysis would characterize the joint scope where contraction + observability hold; this is a follow-up.

---

## §11. Recommended segment actions

Do not modify segments within this spike. The following are *recommendations* for future work:

### 11.1 Minimal (no new commitments)

- `#composition-closure`: add a Discussion note that DA2'-inc is equivalent to (CT2) with $M = I$ (Angle 2 §3.1), reconciling AAD's nomenclature with Lohmiller-Slotine vocabulary. Structural transparency, no content change.
- `#contraction-template` (when landed per R1 of contraction-metric spike): classify Euclidean metric-α₁ cases as AAD-internally derived via DA2'-inc equivalence (Angle 2). Classify non-statistical metric-α₂ cases explicitly as theorem-imported from Lohmiller-Slotine 1998 with honest labeling.

### 11.2 Moderate (adopt PI)

- Add a new formulation segment `#parameterization-invariance` (type: formulation / scope; status: formulation-choice). State (PI) as an invariance commitment motivated as an infinitesimal extension of `#agent-identity`'s token-level commitment. Cite Čencov 1982.
- `#additive-coordinate-forcing`: extend the three-instances table to four, adding the Čencov-invariance primary instance. Reframe the meta-pattern description from "Cauchy-FE on additivity axiom" to "uniqueness-theorem-forced coordinate under AAD-internally-motivated axiom" (generalization). Cross-classify the existing three as Cauchy-FE subfamily, new Čencov-invariance as distinct subfamily.
- `#gain-sector-bridge`: add an "Incremental / Jacobian-level form (B1\*)" subsection in Formal Expression, stating (B1\*) and citing the DA2'-inc equivalence. Status: derived in sub-scope metric-α₁ via Angle 2; derived in sub-scope metric-α₂ under (PI) + Čencov for statistical-manifold agents; theorem-imported for non-statistical metric-α₂.
- `#contraction-template`: lift statistical metric-α₂ cases to AAD-internally derived under (PI).

### 11.3 Strong (adopt heredity + PI)

- Strengthen `#composition-consistency` to the heredity form: composite admissibility derivable from sub-agent properties plus topology. Consequence: `#composition-closure`'s Tier 1/2/3 compresses to topology-indexed structure; Tier 2/3 become out-of-scope rather than qualified-in-scope.
- Agent-level B1\* becomes AAD-internally forced via Angle 1.
- `#critical-mass-composition` (CM2-M) promotes to AAD-internally-derived for heterogeneous composites (replacing the current matched-symmetric restriction).

The strong option is the most ambitious. It has the deepest architectural consequences and the highest return: a clean topology-indexed composition theory without per-Tier caveats. Its cost is committing to heredity, which narrows AAD's stated scope — Tier 2/3 agents in the current formulation become formally out-of-scope rather than qualified-in-scope.

A follow-up spike should assess whether heredity-as-axiom is compatible with AAD's `#discussion-separability-pattern` posture (heredity would promote the current A2' binary into a three-tier ladder as the seventh ladder in `#discussion-separability-pattern`).

---

## §12. References

**Variational analysis / strong monotonicity:**
- Rockafellar, R. T. & Wets, R. J.-B. (1998). *Variational Analysis*. Springer. Cor 12.4 (equivalence of strong monotonicity and Jacobian-symmetric-part-PD for $C^1$ maps).
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. §2.1.3 (strong convexity characterized by Jacobian-level and incremental conditions).

**Contraction analysis:**
- Lohmiller, W. & Slotine, J.-J. E. (1998). "On contraction analysis for non-linear systems." *Automatica* 34(6):683–696.
- Slotine, J.-J. E. (2003). "Modular stability tools for distributed computation and control." *Int. J. Adapt. Control Signal Process.* 17(6):397–416.

**Information geometry / Čencov:**
- Čencov (Chentsov), N. N. (1982). *Statistical Decision Rules and Optimal Inference*. Translations of Mathematical Monographs 53, AMS. [Uniqueness of Fisher metric under sufficient-statistic invariance.]
- Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS / Oxford University Press.

**AAD segments referenced:**
- `#gain-sector-bridge`, `#sector-condition-derivation`, `#sector-persistence-template`, `#composition-closure`, `#composition-consistency`, `#additive-coordinate-forcing`, `#discussion-separability-pattern`, `#critical-mass-composition`, `#agent-identity`.

**AAD spike trail:**
- `msc/spike-contraction-metric-generalization.md` (2026-04-22) — §8.2 item 1, §9 question 1: the Jacobian-level B1 open.
- `msc/spike-bridge-lemma-contraction.md` (2026-04-06) — DA2'-inc identification + Tier 1/2/3.
- `msc/spike-a2-prime-strengthening.md` — sub-scope α / β partition landing.

---

*(End of spike.)*
