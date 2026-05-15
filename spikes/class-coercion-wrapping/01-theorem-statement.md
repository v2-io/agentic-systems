# Sub-Spike A: Class-Coercion Theorem — Statement and Proof Attempt

**Status**: derivation in progress. Conditions stated; (A1)–(A4) verification works modulo specific wrapper-design constraints; directed-separation theorem is the load-bearing structural claim.
**Date**: 2026-05-09
**Depends on**: `00-brief.md`, `#form-composition-closure` (admissibility (A1)–(A4)), `#der-directed-separation`, `#hyp-directed-separation-under-composition`, `#def-agent-environment`, `#result-sector-persistence-template`, `#deriv-sector-condition`.

---

## 1. The setup, formally

Let $A$ be a primitive component, treated as a black-box function with input/output spaces $(\mathcal{I}_A, \mathcal{O}_A)$. The wrapper does not see $A$'s internal state — it only issues queries (inputs) and consumes responses (outputs). $\mathcal{Q}_A \subseteq \mathcal{I}_A$ is the set of admissible queries.

### 1.1 Wrapper state

The **wrapper** $W$ has state $X_W = (M_W, G_W) \in \mathcal{X}_M \times \mathcal{X}_G$ where $\mathcal{X}_G = \mathcal{X}_O \times \mathcal{X}_\Sigma$ per `#def-strategy-dimension`. The wrapper interacts with an environment via observations $o_W \in \mathcal{O}_W$ and actions $a_W \in \mathcal{A}_W$.

### 1.2 Wrapper update maps (type signatures)

The wrapper's update at macro-step $m$ takes the form

$$X_{W, m+1} = (\, M_{W, m+1},\ G_{W, m+1}\, )$$

with components defined as follows.

**Belief-side query selector** $q_M$:
$$q_M : \mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A$$

The wrapper chooses what to ask the component based on its current belief and the current observation. **No $G_W$ argument** — this is the structural commitment.

**Strategy-side query selector** $q_G$:
$$q_G : \mathcal{X}_M \times \mathcal{X}_G \to \mathcal{Q}_A$$

For strategy updates, queries may depend on $G_W$ (this is allowed by (A1)).

**Belief-update map** $f_M$:
$$f_M : \mathcal{X}_M \times \mathcal{O}_W \times \mathcal{Q}_A \times \mathcal{O}_A \to \mathcal{X}_M$$

Updates $M_W$ given the previous belief, the observation, the query made, and the component's response. **No $G_W$ argument.**

**Strategy-update map** $f_G$:
$$f_G : \mathcal{X}_G \times \mathcal{X}_M \times \mathcal{Q}_A \times \mathcal{O}_A \to \mathcal{X}_G$$

Updates $G_W$ given the previous strategy/objective, the current belief, the goal-conditioned query, and its response. May depend on $G_W$.

**External policy** $\pi_W$:
$$\pi_W : \mathcal{X}_W \to \mathcal{A}_W$$

Selects the wrapper's external action.

The full update step:

1. Construct goal-blind query $q_M(M_{W,m}, o_{W,m+1})$.
2. Get response $A(q_M)$.
3. Update $M_{W, m+1} = f_M(M_{W,m}, o_{W,m+1}, q_M, A(q_M))$.
4. Construct goal-conditioned query $q_G(M_{W,m+1}, G_{W,m})$.
5. Get response $A(q_G)$.
6. Update $G_{W, m+1} = f_G(G_{W,m}, M_{W,m+1}, q_G, A(q_G))$.
7. Select external action $a_{W, m+1} = \pi_W(X_{W, m+1})$.

The wrapper is a *temporally extended* macro-step: each macro-step makes at least two component calls (more in richer wrapper designs). This is where the tempo cost enters (sub-spike E).

### 1.3 Comparison with `#form-composition-closure` setup

This setup is a *special case* of the composition-closure setup with $N = 1$ "sub-agent" (the component $A$) and $K_c \geq 2$ component calls per macro-step. The wrapper is a coarse-graining of $A$ with $\Lambda$ being implicit (no explicit projection — the wrapper *constructs* $X_W$ rather than projecting from $A$'s internal state). The closure-defect $\varepsilon^*$ exists but has different semantics (sub-spike D — "coercion" rather than "fidelity").

## 2. Conditions for the theorem

**(C1) Goal-blind admissibility.** The query set $\mathcal{Q}_A$ contains queries whose specification can be constructed from $(M_W, o_W)$ alone. Formally:

$$\exists\, q_M : \mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A \quad \text{such that the response $A(q_M)$ provides information sufficient for some non-trivial belief-update.}$$

Failure mode: components whose query interface intrinsically requires goal-conditioning (e.g., a goal-conditioned policy network whose only operation is $\pi(s, g)$). Sub-spike B characterizes these.

**(C2) Stationary component conditional.** $A$'s output distribution conditional on input is fixed during the wrapper's operation:

$$P(A(\cdot) \mid q) \text{ does not depend on prior queries or on side information beyond $q$ itself.}$$

In particular: $A$ does not adapt online during deployment; pretraining is fixed. (Most deployed LLMs satisfy this; learning-during-deployment systems do not, and are scope-out for the basic theorem.)

**(C3) No implicit goal-inference.** $A$'s response to a goal-blind query $q_M$ does not depend on $G_W$ via inference from query patterns. Formally:

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M) \quad \forall\, q_M, G_W$$

This is the strong leakage-absence condition. Sub-spike C characterizes the residual when this fails.

(C3) is the most fragile condition for real components. For LLMs with pretraining-induced goal-correlations, (C3) holds *exactly* only for queries whose content is statistically independent of $G_W$ in the pretraining distribution. For most queries the wrapper would actually issue (whose content reflects $G_W$-correlated observations the wrapper has chosen to attend to via $\pi_W$), (C3) holds only approximately.

## 3. Theorem statements

**Theorem 1 (Class-Coercion via Wrapping, Exact Form).**

Let $A$ be a component satisfying (C1), (C2), (C3). Let $W$ be a wrapper over $A$ with type-signature-respecting update maps as in §1.2. Then:

(T1.1) The wrapper satisfies (A1) of `#form-composition-closure` by construction.

(T1.2) Under additional wrapper-design constraints D-A2, D-A3, D-A4 (stated below), the wrapper satisfies (A2), (A3), (A4) of `#form-composition-closure`.

(T1.3) Directed separation holds at the wrapper level *exactly*:

$$P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1},\ G_{W,m}) = P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1})$$

(T1.4) Therefore $W$ is a Class-1 architecture in the sense of `#der-directed-separation`.

**Theorem 2 (Class-Coercion via Wrapping, Approximate Form).**

If (C3) is replaced by a leakage bound

$$D_\text{KL}\big(P(A(q_M) \mid q_M, G_W)\, \big\Vert\, P(A(q_M) \mid q_M)\big) \le \kappa \quad \forall\, q_M, G_W$$

then directed separation holds at the wrapper level approximately:

$$D_\text{KL}\big(P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})\big) \le \kappa$$

The wrapper is *almost-Class-1* with leakage rate bounded by $\kappa$. The KL-divergence form is one choice; other divergences yield analogous bounds (sub-spike C).

## 4. Proof of Theorem 1

The argument has four parts: verifying each of (A1), (A2), (A3), (A4), and then the directed-separation claim (T1.3).

### 4.1 (A1) — AAD agent structure

By construction. The wrapper state is $X_W = (M_W, G_W)$, the update is recursive (each step takes $X_{W,m}$, $o_W$, and produces $X_{W,m+1}$), and the macro-policy is state-dependent ($\pi_W : \mathcal{X}_W \to \mathcal{A}_W$). All components of (A1) are present.

The (A1) decomposition holds because we *built it in*. The work was done in §1.1's choice of state space.

✓ (A1) by construction.

### 4.2 (A2) — Macro-mismatch is well-defined

Required: a well-defined prediction $\hat o_{W,m+1}(M_W, a_{W,m})$ such that $\delta_{W,m+1} = o_{W,m+1} - \hat o_{W,m+1}$ is meaningful.

The wrapper must include a prediction map $\hat o_W : \mathcal{X}_M \times \mathcal{A}_W \to \mathcal{O}_W$. This is **wrapper-design constraint D-A2**: the wrapper must commit to a prediction interface against which observations can be compared.

For most belief-state representations, this is straightforward. If $M_W$ stores predicted distributions over future observations (Bayesian posterior, exponential-family parameters), $\hat o_W$ is the maximum a posteriori or expectation under the posterior. If $M_W$ is a learned representation (e.g., a vector embedding produced by $A$), the wrapper must commit to a decoder $\hat o_W$ — possibly using $A$ itself in a different mode.

✓ (A2) holds under D-A2 (commit to a prediction map). The constraint is operational, not theoretically deep.

### 4.3 (A3) — Macro-tempo is well-defined

Required: well-defined update rate $\nu_W$ and optimal gain $\eta_W^*$ for the wrapper's observation channels.

The wrapper updates once per macro-step. If macro-steps occur at rate $\nu_W$ in real time, then $\nu_W$ is well-defined. The gain $\eta_W^*$ depends on the structure of $f_M$ — for a Bayesian belief-update, $\eta_W^*$ is the standard Kalman-like gain (per `#emp-update-gain` and `#example-kalman`).

For non-Kalman $f_M$ (e.g., gradient descent on a loss derived from $A$'s response), the gain is the gradient step size or its stochastic-approximation analog.

This is **wrapper-design constraint D-A3**: $f_M$ must support a gain interpretation — typically true when $f_M$ is from the Tier-1 class (Bayesian on exponential families, gradient on strongly convex losses, linear-PD).

✓ (A3) holds under D-A3 (Tier-1 belief-update map).

### 4.4 (A4) — Sector-bounded macro-correction

Required: the macro-correction function $F_W(\mathcal{T}_W, \delta_W) = $ change-in-$M_W$-from-mismatch-$\delta_W$ satisfies the sector condition

$$\delta_W^T F_W(\mathcal{T}_W, \delta_W) \geq \alpha_W \|\delta_W\|^2 \quad \text{for } \|\delta_W\| \leq R_W$$

with $\alpha_W > 0$ and $R_W > 0$.

This is **wrapper-design constraint D-A4**: $f_M$ must satisfy the sector condition with positive correction rate. Per `#deriv-sector-condition` Prop A.1, this is automatic for Bayesian updates on exponential families; per `#der-gain-sector-bridge`, it follows for linear corrections with positive-definite gain. For more exotic $f_M$ (e.g., non-monotonic correction, gradient descent on non-convex losses), (A4) may hold only locally or fail altogether — Tier-2 / Tier-3 in the bridge-lemma classification of `#form-composition-closure`.

✓ (A4) holds under D-A4 (Tier-1 belief-update map). For Tier-2/3 the wrapper inherits the corresponding tier-restricted persistence guarantee; the bridge lemma's sector condition becomes local rather than global.

### 4.5 The directed-separation claim (T1.3)

This is the load-bearing structural step. Goal: show that under (C1)–(C3), $M_{W,m+1}$ is conditionally independent of $G_{W,m}$ given $(M_{W,m}, o_{W,m+1})$.

**Step 1: identify all paths from $G_W$ to $M_{W,m+1}$.**

The wrapper's update chain for $M_W$ is:

$$M_{W,m+1} = f_M\big(\, M_{W,m},\ o_{W,m+1},\ q_M(M_{W,m}, o_{W,m+1}),\ A\big(q_M(M_{W,m}, o_{W,m+1})\big)\, \big)$$

For $G_W$ to influence $M_{W,m+1}$, it must enter through one of the four arguments of $f_M$:

(P-1) $M_{W,m}$ — already conditioned on.
(P-2) $o_{W,m+1}$ — already conditioned on.
(P-3) $q_M(M_{W,m}, o_{W,m+1})$ — by type signature, $q_M$ does not take $G_W$. ✗ closed.
(P-4) $A(q_M)$ — the component's response to a goal-blind query.

Paths P-1 and P-2 are conditioned on. Path P-3 is closed by the type signature of $q_M$ (this is the structural commitment of the wrapper).

**Step 2: P-4 is the only open path. Close it under (C3).**

Path P-4 is open if and only if $A(q_M)$ depends on $G_W$ given $q_M$. By (C3):

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$$

This means $A(q_M) \perp G_W \mid q_M$. Since $q_M$ is determined by $(M_{W,m}, o_{W,m+1})$, and the entire pipeline conditions on these, the dependence of $M_{W,m+1}$ on $G_W$ vanishes.

Formally: by the chain rule,

$$P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})$$

$$= \int P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, q_M, A(q_M)) \cdot P(A(q_M) \mid q_M, G_{W,m}) \cdot \mathbb{1}[q_M = q_M(M_{W,m}, o_{W,m+1})]\, dA\, dq_M$$

Under (C3), the second factor reduces to $P(A(q_M) \mid q_M)$, which is independent of $G_{W,m}$. The integrand no longer depends on $G_{W,m}$, so the integral equals $P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})$.

**Step 3: This is conditional independence.**

We have shown:

$$P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m}) = P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})$$

which is exactly directed separation at the wrapper level. ∎

### 4.6 What this proves vs. what's wrapper-design constraint

The theorem-content is:

- (T1.1) (A1) by construction. **Theorem.** Free given the type signatures of §1.2.
- (T1.3) Directed separation at wrapper level under (C1)–(C3). **Theorem.** This is the load-bearing structural result.
- (T1.4) Class-1 status follows from (T1.3) plus `#der-directed-separation`'s definition of the classes. **Theorem.**

The wrapper-design constraints are:

- D-A2: commit to a prediction map. Required for (A2). Operational; not theoretically deep.
- D-A3: $f_M$ supports a gain interpretation. Required for (A3). Holds for Tier-1 belief-update maps.
- D-A4: $f_M$ satisfies the sector condition. Required for (A4). Holds for Tier-1 belief-update maps; tiered downward for Tier-2/3.

The constraints D-A2/D-A3/D-A4 are familiar from `#form-composition-closure` and `#deriv-sector-condition`. They are inherited from those segments and not re-derived here. The wrapper-design choices about *how* to build $f_M$ (Bayesian on what state space? gradient on what loss? linear with what gain?) are not part of the theorem — they are application-level choices.

The theorem says: **given any wrapper that satisfies the type signatures of §1.2 and chooses $f_M$ from the Tier-1 class (or from a Tier-2/3 class with tier-restricted scope), and given any component satisfying (C1)–(C3), the wrapper is Class-1 by construction at the wrapper level.**

## 5. Proof of Theorem 2 (approximate form)

**Step 1: bound the leakage at the component level.**

By assumption, $D_\text{KL}(P(A(q_M) \mid q_M, G_W)\, \|\, P(A(q_M) \mid q_M)) \le \kappa$.

**Step 2: propagate to the wrapper-level update.**

The wrapper-level update $M_{W,m+1}$ is a deterministic function of $(M_W, o_W, q_M, A(q_M))$. The KL-divergence between $P(M_{W,m+1} \mid \ldots, G_W)$ and $P(M_{W,m+1} \mid \ldots)$ is bounded above by the KL-divergence between $P(A(q_M) \mid q_M, G_W)$ and $P(A(q_M) \mid q_M)$ — the data-processing inequality.

Specifically, since the wrapper-level update factors as

$$M_{W,m+1} = f_M(\ldots, A(q_M))$$

and the only $G_W$-dependent input is $A(q_M)$, the data-processing inequality gives:

$$D_\text{KL}\big(P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})\big) \le \kappa$$

∎

The wrapper is *almost-Class-1* — directed separation holds with KL-divergence bound $\kappa$. This is the analog of "approximate Class 1" in the existing classification, with an explicit bound.

## 6. Connections to existing AAD machinery

### 6.1 Strengthening of `#hyp-directed-separation-under-composition`

The hypothesis is currently stated as: when does directed separation hold under composition? The theorem provides a *constructive* answer for the special case where the composition is wrapper-around-component: directed separation holds *whenever the wrapper's type signatures are respected and (C1)–(C3) hold*.

This promotes the hypothesis to a derived result for the wrapper-around-component case. It does not address general $N$-agent composition where each sub-agent might be Class-3.

### 6.2 Inheritance of persistence template

Under D-A4, the wrapper inherits `#result-sector-persistence-template` at the wrapper level: persistence holds when $\alpha_W R_W > \rho_W$ where $\rho_W$ is the wrapper-level effective disturbance.

The wrapper-level disturbance has two contributions:
- External environmental disturbance $\rho_\text{ext}$ acting through $o_W$.
- Internal disturbance from the wrapping construction itself — the variance of $A(q_M)$ around its expected value, which the wrapper cannot control.

The total effective disturbance is $\rho_W = \rho_\text{ext} + \rho_\text{int}$, where $\rho_\text{int}$ is bounded by the variance of $A$'s responses to goal-blind queries. The persistence condition $\alpha_W R_W > \rho_\text{ext} + \rho_\text{int}$ thus has an explicit dependence on the component's noise structure.

This connects the wrapping construction directly to the existing template machinery without requiring new Lyapunov work.

### 6.3 Tempo-cost as Brooks's-Law form

The wrapper makes $K \ge 2$ component calls per macro-step. By `#der-tempo-composition`, the wrapper-level tempo is bounded by

$$\mathcal{T}_W \le \mathcal{T}_A^{\text{nominal}} - C_\text{coord}^\text{wrap}$$

where $C_\text{coord}^\text{wrap}$ is the coordination overhead specific to the wrapping construction. Sub-spike E quantifies this.

### 6.4 Form-preservation framing

The form-preservation framing from `spikes/temporal-nesting-rg/99-verdict.md` reads (A1)–(A4) as form-preservation conditions: macro must itself be AAD. The class-coercion theorem says this form-preservation can be *constructed* even when the underlying component fails directed separation. In form-preservation language: the AAD form is preserved at the wrapper level, even when the underlying $A$ does not satisfy form-preservation on its own.

## 7. Honest scope statement

What the theorem does:
- Provides a *constructive* route to Class-1 status given an admissible component and a Tier-1-class belief-update map.
- Inherits AAD's existing persistence and tempo machinery at the wrapper level.
- Identifies precisely which conditions are theorem content vs. wrapper-design constraint.

What the theorem does *not* do:
- Prove that any specific real LLM satisfies (C3). The exact form is a structural ideal; real components leak. Theorem 2 (approximate form) is the realistic version, with the leakage bound $\kappa$ to be characterized empirically (sub-spike C and G).
- Prove the wrapper-design constraints (D-A2, D-A3, D-A4) hold automatically. They must be honored when the wrapper is built. The theorem says "if you build the wrapper correctly, the framework applies."
- Address components that fail (C1) — i.e., components whose query interface intrinsically requires goal-conditioning. These are scope-out for the basic theorem; sub-spike B characterizes them and asks whether any partial result is available.
- Resolve the question of whether the wrapping construction is the "same" agent as the underlying component "in some meaningful sense." It produces a *different* agent — specifically, a Class-1 agent built around the component as oracle. The relationship is that of the wrapper to the wrapped, not identity.

## 8. What changes in AAD if this lands

The theorem promotes `#hyp-directed-separation-under-composition` from hypothesis to derived (in the wrapper-around-component special case). It also resolves the "Class 2 exit" framing in CLAUDE.md ("Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation") into a "constructive route through" — the LLMs are scope-in *for the wrapper construction*, not scope-out.

Recommended segment-level landings (subject to sub-spike I prior-art results, which may shift the framing):

- **New segment** `01-aat-core/src/der-class-coercion-via-wrapping.md` (or `result-class-coercion-via-wrapping.md`) — statement, proof, conditions, costs.
- **Update** `#hyp-directed-separation-under-composition` to cite the constructive result.
- **Update** `#der-directed-separation` Discussion section to describe the wrapping route (and the cost of taking it).
- **Cross-component reference** in `03-logogenic-agents/` and `04-eli/` segments — PROPRIUM as canonical instance (sub-spike H).
- **Discussion-level integration** in `#der-tempo-composition` connecting the Brooks's-Law form to the wrapping construction.

## 9. Self-review

**Tier**: derived (theorem) under (C1)–(C3) + D-A2/3/4. The proof is honest at the level of conditional-independence reasoning + data-processing inequality; both are standard. No Lyapunov work was invented here — everything inherits from existing AAD machinery.

**Three lenses**:
- *Wisdom*: Does this solve the real problem? Yes — it gives a constructive route from Class-3 components to Class-1 systems, which is what Parts III/IV need. The conditions are precise enough to be checkable; the costs are tied to existing AAD machinery (Brooks's-Law, persistence template).
- *Strength*: Is the proof rigorous? Steps 1–3 of §4.5 are clean conditional-independence reasoning. The approximate version uses standard data-processing inequality. The wrapper-design constraints are flagged honestly. Edge cases — failure of (C1), failure of D-A4 — are identified, not glossed.
- *Beauty*: Is this pleasant to read? The type signatures of §1.2 carry the structural commitment cleanly. The proof in §4.5 is short and the structure (4 paths, 3 closed by structure, 1 closed by (C3)) is easy to grasp. The "what's theorem vs. what's design constraint" separation in §4.6 makes the load-bearing parts visible.

**What I'm uncertain about**:
- Whether (C3) is the right condition or whether something weaker would do. The KL-form may be replaceable by a different divergence that's easier to bound empirically (e.g., total variation, mutual information). Sub-spike C should test this.
- Whether the data-processing inequality bound in §5 is tight or loose. If the wrapper's $f_M$ is invertible, the bound is tight; for compressing $f_M$, the wrapper-level KL may be strictly less than $\kappa$. Worth a check.
- Whether the (C1) admissibility condition is the *right* characterization — sub-spike B will tell.

**What I would still want before promoting to a `01-aat-core/src/` segment**:
- Sub-spike B: admissibility characterization.
- Sub-spike C: leakage bound $\kappa$ characterized in usable terms.
- Sub-spike F + I: empirical instances + prior-art differentiation, to confirm the construction is well-positioned in the existing literature.
- Sub-spike H: connection to Parts III/IV — does PROPRIUM specifically constrain or strengthen what's been shown here?

The theorem itself is in good shape. The next-up dependencies are sub-spikes B and C (running on the Tier-1 belief-update class as default, with explicit leakage characterization).

---

## File index

- This file: `01-theorem-statement.md`
- Brief: `00-brief.md`
- Admissibility: `02-admissibility.md` (sub-spike B, pending — depends on this file)
- Leakage: `03-leakage.md` (sub-spike C, pending — depends on this file)
- Coercion-vs-fidelity ε*: `04-epsilon-semantics.md` (sub-spike D, pending)
- Tempo cost: `05-tempo-cost.md` (sub-spike E, pending)
- Empirical instances: `06-empirical-instances.md` (delegated)
- Quantitative bounds: `07-quantitative-bounds.md` (sub-spike G, pending — depends on §6.2 persistence-template inheritance and sub-spike E)
- Parts III/IV connection: `08-parts-3-4-connection.md` (sub-spike H, pending — depends on `06-empirical-instances.md`)
- Prior-art differentiation: `09-prior-art-differentiation.md` (delegated)
- Synthesis: `99-verdict.md` (final)
