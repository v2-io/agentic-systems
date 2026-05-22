# 2. Formal Decomposition

## 2.1 Pipeline structure of $f_M$

Any belief-update function $f_M$ that maintains $M_t$ (whether Bayesian, Kalman, RL-with-world-model, LLM-as-tracker) factors functionally through a small set of operations. We posit a canonical four-stage decomposition, justified by mapping each stage to existing AAT machinery already in canon:

$$f_M \;=\; \tau \;\circ\; \alpha \;\circ\; \lambda \;\circ\; \phi$$

with:

- **(P0) Selection.** $a_t = \pi(M, G) \to h \to e_\tau$. Goals influence *which* event arrives (per `#scope-agency`, `#scope-observation-ambiguity-modulation`). This is the agent's observation-channel control via the policy. Formally outside $f_M$ (it is the *upstream* of $f_M$, not part of it); included here for completeness.

- **(P1) Featurization.** $\phi: \mathcal{E} \times \mathcal{M} \to \mathcal{X}$, $x = \phi(e_\tau, M_{\tau^-})$. Extract features from the realized event given the current model. In a Kalman tracker this is the innovation $\delta = o - \hat o$ per `#def-mismatch-signal`. In an LLM-as-tracker it is the attention-mediated encoding of the input given prior context.

- **(P2) Likelihood.** $\lambda: \mathcal{X} \times \mathcal{M} \to \mathcal{L}$, $\ell = \lambda(x, M_{\tau^-})$. Evaluate the likelihood of the features under hypotheses representable in $\mathcal{M}$. In a Kalman tracker this is the Gaussian likelihood $\mathcal{N}(0, S)$ on innovation $\delta$ with covariance $S = H P^- H^\top + R$. In Bayesian inference this is the $P(e \mid z)$ step.

- **(P3) Aggregation.** $\alpha: \mathcal{L} \times \mathcal{M} \to \mathcal{M}^+$, $M' = \alpha(\ell, M_{\tau^-})$. Combine likelihood with prior to produce the new (pre-storage) belief. In a Kalman tracker this is the update step $\hat x^+ = \hat x^- + K \delta$ with gain $K = P^- H^\top S^{-1}$, where the gain is determined by $\eta^\ast = U_M / (U_M + U_o)$ per `#emp-update-gain`.

- **(P4) Consolidation.** $\tau: \mathcal{M}^+ \to \mathcal{M}$, $M_{\tau^+} = \tau(M')$. Post-update transformation: storage, normalization, regularization, memory consolidation. In a Kalman tracker this is the trivial identity (or a covariance-projection step); in an LLM agent with external memory it is the write to the memory store with whatever filtering applies; in biological cognition it is the consolidation-during-sleep / context-switch step.

Each stage in the (P1)–(P4) chain can independently take or omit a $G_t$ argument. The Class 1 case has none; the Class 3 case has all; Class 2 is a non-trivial subset.

## 2.2 The Class 2 parameterization

A Class 2 partial-coupling agent is parameterized by a triple

$$\mathcal{C}_2 = (S, R, F)$$

with:

- $S \subseteq \{P1, P2, P3, P4\}$, $S \neq \emptyset$ and $S \neq \{P1, P2, P3, P4\}$ — the **stage set** at which goals enter $f_M$. Empty $S$ = Class 1; full $S$ = Class 3 (in the process-form case).
- $R \subseteq \{O, \Sigma\}$, $R \neq \emptyset$ — the **source set** within $G_t = (O_t, \Sigma_t)$ that acts as the coupling input. (The case $R = \{O, \Sigma\}$ is admitted; it covers agents where both objective and strategy enter.)
- $F: S \to \{\text{content}, \text{process}\}$ — the **form** at each coupled stage. Formal definitions in §2.4 below.

A Class 2 sub-type is a particular value of $\mathcal{C}_2$. The cardinality of the sub-typing space, ignoring form, is

$$(2^4 - 2) \times (2^2 - 1) = 14 \times 3 = 42 \text{ non-trivial sub-types}$$

before content/process refinement. With form: at most $42 \times 2^{\lvert S\rvert} \le 42 \times 16$ cells; but most are empirically degenerate (see §3.2 on stage-cascade propagation).

The point of the parameterization is not exhaustive enumeration but to make the structural carve *visible*: the scalar $\kappa_{\text{processing}}$ is the projection of $\mathcal{C}_2$ onto the magnitude axis, and projecting destroys most of the information.

## 2.3 Recovery of canon labels

The endpoints of the parameterization recover canon:

- **Class 1 (Separated).** $S = \emptyset$. No coupling. $\kappa_{\text{processing}} = 0$ under all distributions. Section II's exact results apply.

- **Class 3 (Coupled).** $S = \{P1, P2, P3, P4\}$, $R = \{O, \Sigma\}$, $F \equiv \text{process}$. Goals enter at every stage, from both sources, with non-separable functional dependency. This is the "fully entangled" limit Joseph's question gestures at. $\kappa_{\text{processing}}$ near 1.

- **Class 2 (Partial), formal $\kappa^c$ criterion in `#hyp-directed-separation-under-composition`.** At the composite level, the criterion measures whether $G^c$ enters $f^c_M$ through a pathway bypassing the event channel. This corresponds to $S \ne \emptyset$ at the composite level, with the composite's $G^c$ as source.

The parameterization gives strictly more structure than the canon labels carry. In particular it lets us state honestly that "Class 3 (fully Coupled)" is the corner $(S, R, F) = (\{P1,P2,P3,P4\}, \{O,\Sigma\}, \text{process-throughout})$ — *and that there is a meaningful interior to Class 2 the scalar $\kappa$ obscures*.

## 2.4 Content vs Process — formal definitions

A stage operation $\xi$ (any of $\phi, \lambda, \alpha, \tau$) with a goal argument $G$ admits a **content-form / process-form** classification. The intuition is that *content* means the goal acts as an additive bias on the operation's output (separable from the goal-blind operation), while *process* means the operation's *functional form* depends on the goal (non-separable).

### Definition (content-form coupling)

Stage $\xi(\cdot; G)$ is **content-form coupled** if there exist functions $\xi^0$ (goal-blind) and $b_\xi$ (bias) such that

$$\xi(u; G) \;=\; \xi^0(u) \;+\; b_\xi(G; u)$$

and $b_\xi(G_0; u) = 0$ for some *reference goal* $G_0$ (or, more generally, $\xi^0$ is identifiable from observations of $\xi(u; G)$ across a probing protocol that varies $G$ at fixed $u$).

The identifiability requirement is what makes the form operationally meaningful: a content-form coupling can be *measured* (by varying $G$ at fixed $u$ and recording the difference) and therefore *subtracted out* (by a wrapper that estimates $b_\xi$ from probes and corrects post-hoc).

### Definition (process-form coupling)

Stage $\xi(\cdot; G)$ is **process-form coupled** if it is not content-form coupled — i.e., no decomposition $\xi = \xi^0 + b_\xi$ exists with $\xi^0$ identifiable.

Equivalently: process-form coupling means that under different goals $G_1, G_2$, the maps $\xi(\cdot; G_1)$ and $\xi(\cdot; G_2)$ are functionally different in ways not capturable as an additive bias. The agent's response to the same input has different *shape*, not just different *position*.

### A useful sharpening — the multiplicative-form case

The most empirically common process-form is **multiplicative**:

$$\xi(u; G) \;=\; \xi^0(u) \cdot h(G; u)$$

where $h$ is a positive scalar (or pointwise-positive) modulator. Multiplicative form is process per the definition (no $G_0$ makes $h \equiv 1$ in general, and even when one exists the *ratio* of responses recovers $h$ but not $\xi^0$ absolutely without a reference). It is what the leakage-locus spike's $\exp(g^\top z)$ exponential-tilt model assumes; it is also what attention-mediated coupling in transformers produces structurally (attention weights *multiply* value vectors; the goal token affects the weights, not the values).

A more general process-form is **compositional**:

$$\xi(u; G) \;=\; \xi^\dagger(u, G)$$

with no separable factor. This is the "function class changes with $G$" case in its starkest form — e.g., a goal that switches the agent between *interpolative* and *extrapolative* belief-update modes.

### Why the content/process distinction is load-bearing

§3 derives the operational consequence: content-form coupling is *wrappable* by post-hoc debiasing (W₂-equivalent at the stage level); process-form coupling is *not* — it requires stage replacement (W₁-equivalent) or full-agent wrapping. This is the structural reason Joseph's intuition about "what can be partially detangled" admits a sharp answer: content-form sub-types are detanglable from the outside; process-form sub-types are not.

## 2.5 Source labels — $O$, $\Sigma$, and $M$-self

A coupling can be sourced from:

- $O_t$ — the **objective**. Identity-binding, terminal-value commitments, "I want this to be true" pressure. The Working Notes of `#disc-adversarial-coupling-pressure` name this as the $O \to M$ pathway.

- $\Sigma_t$ — the **strategy**. Sunk-cost, plan-commitment, "if this is true my plan is wrong, so it can't be true." The same Working Note's $\Sigma \to M$ pathway.

- $M_t^{\text{prior}}$ self-coupling. Confirmation bias proper — prior belief shapes how new evidence is processed, without explicit $G_t$ pathway. This is structurally subtler: it is not a $G \to f_M$ coupling at all but a $M_{\tau^-} \to f_M$ amplification within the goal-blind machinery. Whether it counts as "Class 2" depends on whether one reads $f_M$ as conditioning on $M_{\tau^-}$ (the canon position — it does) or whether the *amplification* of prior in some directions is itself a coupling pathway (which would be a structural extension to canon).

For the scope of this spike, $R \subseteq \{O, \Sigma\}$ — we treat the $M$-self case as orthogonal (see `06-edge-cases-and-no-gos.md` §6.1 for a careful unpacking). The two-source parameterization is the live one.

## 2.6 What the parameterization predicts

§3 derives the following from the formal setup:

1. **Stage-localization of repair** (Result 1, §3.1). Coupling confined to a stage subset $S$ is repairable by intervening at $S$, *provided pipeline access is available*. For monolithic Class 3 components, no such access exists; only full-agent wrapping applies.

2. **Form determines wrappability** (Result 2, §3.2). Content-form coupling at any subset of stages is wrappable by *post-hoc debiasing* (no internal access required, only behavioral probing). Process-form coupling requires *stage replacement* (internal access) or full-agent wrapping.

3. **Stage-cascade propagation** (Result 3, §3.3). $G$-coupling at stage $P_k$ contaminates all downstream stages $P_{k+1}, P_{k+2}, \ldots$ even if those stages are individually goal-blind. The *naming* of a sub-type by its primary coupling stage is well-defined; the *effect* propagates.

4. **Source asymmetry — belief-strategy attractors** (Result 4, §3.4). Pure $\Sigma_t$-source coupling creates *feedback loops* $M_t \to \Sigma_t \to f_M \to M_t$ that admit fixed points $(M^\ast, \Sigma^\ast)$ misaligned with the environment. Pure $O_t$-source coupling does not produce such attractors (because $O_t$ is exogenous to $M_t$ in steady state per the orient cascade). This is a genuine structural difference between $O$ and $\Sigma$ as coupling sources.

5. **Composition with the leakage locus** (Result 5, §3.5). All Class 2 sub-types share the property that their effect on belief is confined to $\ker\mathcal I_\tau$ (per the leakage-locus result of `spike-leakage-locus-2026-05-18`). The sub-type determines *the functional form* of the displacement within that subspace, not its *support*.

6. **Wrapping-regime correspondence** (Result 6, §3.6). The W₀/W₁/W₂ wrapping regimes of `#der-class-coercion-via-wrapping` correspond to the form-axis of the sub-typology: W₂ ↔ content; W₁ ↔ process-but-with-pipeline-access; W₀ ↔ no-coercion-needed-or-no-access.

These are the load-bearing results. The next file pushes the math.
