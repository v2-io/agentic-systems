# RG-0c: (O, Σ) Recursion Check Against Formal Definitions

**Status**: derived — verdict V2/V3 boundary, leaning V3 with a constructive V2-rescue path documented.
**Date**: 2026-05-09
**Brief**: `00-brief.md` §5 RG-0c.
**Depends on**: `01-aat-core/src/def-strategy-dag.md`, `01-aat-core/src/def-strategy-dimension.md`, `01-aat-core/src/form-objective-functional.md`, `01-aat-core/src/def-value-object.md`, `01-aat-core/src/def-satisfaction-gap.md`, `01-aat-core/src/form-complete-agent-state.md`, `01-aat-core/src/form-structural-change-as-parametric-limit.md`, `01-aat-core/src/example-strategy.md`, `02-prior-art-rg-ib-fep.md`.

---

## 0. The question, sharpened

The naive "fractal of agents" reading: an internal Σ-node represents "achieve condition $C_v$"; achieving $C_v$ is itself an objective; the sub-DAG below that node is a strategy for that sub-objective; so $(O, \Sigma)$ at depth 0 decomposes into $\{(O'_i, \Sigma'_i)\}$ at depth 1, and so on to action leaves.

To support a *formal* recursion claim — and a non-trivial AAT-distinctive one beyond FEP-RG (which already has form-preservation under coarse-graining; see `02-prior-art-rg-ib-fep.md` §2) — three things must hold simultaneously, against AAT's actual definitions:

- (R1) **The objective at the sub-level must satisfy the formal type of an objective.** Concretely: it must be (or induce) a value functional $V_{O'}: \text{trajectories} \to \mathbb{R}$ with a satisfaction threshold $V_{O'}^{\min}$ — `#form-objective-functional`'s definition.
- (R2) **The strategy at the sub-level must satisfy the formal type of a strategy.** Concretely: it must be a DAG with leaves either action propositions or condition propositions, AND/OR combination, terminal satisfaction conditions referencing $V_{O'}$, well-formedness in the sense of `#def-strategy-dag`.
- (R3) **The split survives.** $V_{O'}$ (evaluation) and the sub-DAG (guidance) must be *type-distinct objects*, not the same object playing two roles. AAT's definitional split between $O_t$ (evaluation) and $\Sigma_t$ (guidance) is what would be AAT-distinctive over FEP-RG, where free energy plays both roles. If at the sub-level the two collapse to one, the split does not survive recursion and AAT's contribution reduces to FEP-RG-style scale-free structure.

I read the segments and worked the question per (R1)–(R3) below, then reached a verdict.

---

## 1. Q1–Q4: What the segments actually define

### 1.1 What `#def-strategy-dag` says about internal nodes

The segment defines $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ with:

> "**Source constraint.** Leaf nodes are propositions about action success ('action $a$ succeeds at $\tau_v$') or observable conditions ('condition $C_v$ holds at $\tau_v$'). Both are propositional — the distinction is whether the proposition is within the agent's causal control (action) or not (condition)."

— so leaves are *propositions about events*, with associated temporal positions $\tau_v$.

For internal (non-leaf, non-root) nodes the segment is silent on the propositional content; the formal weight on internal nodes lives entirely in $\gamma_t \in \{\text{AND}, \text{OR}\}$ and the propagated status $s_v$. The forward pass formula

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR}\end{cases}$$

does not assign internal $v$ any object beyond a number $s_v \in [0, 1]$.

The closest the segment comes to attaching content to internal nodes is the **terminal satisfaction conditions** clause, which it scopes carefully:

> "**Terminal satisfaction conditions.** The root terminal $v_\text{root}$ and any intermediate nodes near the top of the DAG carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective. These conditions operationalize $O_t$ within $\Sigma_t$ — they are the agent's theory of what it means to satisfy the objective. **$O_t$ itself lives outside $\Sigma_t$** ( #def-strategy-dimension); **the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires.**"

(Emphasis mine.) This is the load-bearing sentence for the recursion question. The segment declares two things explicitly: (a) terminal conditions are predicates on trajectories — they have the right *kind* to be evaluated by something objective-like; (b) they are *internal encodings* of the parent $O_t$, not standalone objectives.

The well-formedness clause reinforces (b):

> "**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions yields a trajectory that satisfies the objective:
> $$\Pr\!\left(O_t \text{ satisfied by } \tau \;\middle\vert\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$
> where '$O_t$ satisfied' means $V_{O_t}(\tau)$ exceeds the objective's own satisfaction criterion (formalized as $V_{O_t}^{\min}$ in #def-satisfaction-gap)."

The terminal conditions are well-formed *by reference to $O_t$*, not by being objectives themselves. The $V_{O_t}^{\min}$ that licenses the satisfaction threshold lives on $O_t$, not on the terminal predicates.

### 1.2 What `#def-strategy-dimension` says about the split

The split is declared definitional, not approximate:

> "The split is **definitional** — it reflects a structural difference in the information, not a dynamic or timescale claim. $O_t$ and $\Sigma_t$ are different *kinds* of state answering different questions: ... $O_t$: **evaluation** ... $\Sigma_t$: **guidance**."

And the table reinforces the asymmetry: $O_t$ has type $V_{O_t}: \text{trajectories} \to \mathbb{R}$; $\Sigma_t$ has type "structured representation."

Crucially:

> "The decomposition resolves a type error. Earlier formulations used $\delta_{\text{goal}} = G_t - M_t$ as a goal mismatch signal. When $\Sigma_t$ is a DAG, this is a type error — you cannot subtract a graph from a state vector."

AAT treats $V_{O_t}$ and a DAG-shaped $\Sigma_t$ as *different types*. Conflating them is explicitly a "type error" the segment was written to fix. This is significant — it means any recursion proposal that re-conflates them at the sub-level is reintroducing the type error AAT's definitional split was constructed to remove.

### 1.3 What `#form-objective-functional` requires

For $X$ to formally count as an objective in AAT:

> "The **objective** $O_t$ induces a **value functional**: $V_{O_t}: \text{trajectories} \to \mathbb{R}$. $V_{O_t}(\tau)$ is a scalar measure of how well trajectory $\tau$ satisfies the objective. **This is the sole interface between $O_t$ and the rest of the theory** — the type-stable evaluation surface."

Plus:

> "**Satisfaction threshold.** Many objectives carry a natural threshold $V_{O_t}^{\min}$ — the minimum trajectory value the agent treats as acceptable. ... $V_{O_t}^{\min}$ is a parameter of the objective, not a theory output — it encodes 'what counts as success' in domain terms."

So a candidate $O'$ at depth 1 needs: (i) a domain-given functional on trajectories; (ii) optionally a threshold; (iii) the scalar-comparability commitment from the Epistemic Status (revealed-preference, scalarization, timescale-separated tradeoff resolution).

### 1.4 What "an objective" formally is in AAT

There is no separate `def-objective-functional.md` segment. `#form-objective-functional` is the canonical definition; `#def-strategy-dimension` declares the role; `#def-value-object` and `#def-satisfaction-gap` extend the diagnostic machinery (horizon-conditioned $V_O$, attainability $A_O$, satisfaction gap $\delta_\text{sat}$). All of this hangs on the same evaluation-functional surface.

---

## 2. Q5: Does an internal node's satisfaction condition formally qualify as $O'$?

This is the binding question. The naive reading says: "achieve $C_v$" is an objective; the sub-DAG below is a strategy for it; the recursion goes through.

The segments answer this directly, and the answer is **no — not without modification**. Three reasons.

### 2.1 The segment names the negative explicitly

`#def-strategy-dag`'s terminal-conditions paragraph:

> "$O_t$ itself lives outside $\Sigma_t$ ( #def-strategy-dimension); the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires."

This sentence is a deliberate non-identification. Terminal conditions are *encodings*, not the encoded thing. They are predicates that happen to be evaluable on trajectories, but they are not themselves objectives — they're the agent's theory of what would satisfy $O_t$. The segment's author specifically separates the two.

### 2.2 The type does not match `#form-objective-functional`

The leaf base credence formula says:

$$p_v(M_t) = \begin{cases} \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t) & v \text{ is action} \\ \Pr(C_v(\tau_v) \mid M_t) & v \text{ is condition}\end{cases}$$

These are *probabilities of propositions*, not *trajectory functionals*. The natural object an internal node carries — its satisfaction condition $C_v$ — is a Boolean predicate $C_v: \text{trajectories} \to \{0, 1\}$. To force it into the objective-functional shape we'd need:

$$V_{C_v}(\tau) = \mathbb{1}[C_v(\tau)], \qquad V_{C_v}^{\min} = 1$$

This is mechanically possible — an indicator-functional fits the Section II of `#form-objective-functional`'s table ("Target region $R$: $\mathbb{1}[s_T \in R]$, 'reach safe state'"). So *as a functional*, the indicator is a legitimate $V_{O'}$. But:

- The Epistemic Status of `#form-objective-functional` makes the real-valued codomain "load-bearing" precisely because it enables comparability and gradient-style diagnostics ($\delta_\text{sat}$ as a continuous magnitude, $\delta_\text{regret}$ as a continuous magnitude, the convention hierarchy, etc.). An indicator-valued $V_{O'}$ makes the diagnostic table degenerate to set-theoretic membership tests, which the segment explicitly notes is the *fallback* form for genuinely Pareto / non-scalar objectives, not the canonical form.
- The well-formedness clause is *unidirectional*: it asks whether achieving the terminal predicate guarantees $V_{O_t}(\tau) \geq V_{O_t}^{\min}$ (with high probability under $M_t$). It does not say the terminal predicate is *itself* an objective with its own $V^{\min}$. The whole purpose of the well-formedness check is to verify that the terminal predicate operationalizes $O_t$ — i.e., that the predicate is a (possibly imperfect) *encoding* of what $O_t$ requires, *not a substitute objective with independent existence*.

So: indicator-functionals fit the type, but the segment's framing puts them in the "substitute / encoding" role, not the "objective" role.

### 2.3 The leaf base credence is a probability, not an attainability

Even if we granted that internal nodes carry sub-objectives via indicator-functionals, the recursive AAT agent at depth 1 would need an attainability assessment $A_{O'}$ in the sense of `#def-satisfaction-gap`:

$$A_{O'}(M_t; \Pi, N_h) = \sup_{\pi \in \Pi} V_{O'}(M_t, \pi; N_h)$$

But the AAT strategy-DAG machinery propagates $s_v$ — a probability that $C_v$ will hold *under the current strategy* — not $A_{O'}$ — the supremum over a policy class. These are different quantities. The plan-confidence score $\hat P_\Sigma = s_{v_\text{root}}$ corresponds to $V_O(M_t, \pi_\text{current}; N_h)$ (the value of the current policy), not to $A_O$. The segment makes this distinction explicit:

> "$\hat P_\Sigma$ is explicitly distinct from $A_O$ ( #def-satisfaction-gap), which optimizes over the entire policy class, and from $V_O(\pi_\text{current})$ ( #def-value-object), which evaluates the current policy. $\hat P_\Sigma$ is cheap to compute ($O(\lvert V\rvert + \lvert E\rvert)$ forward pass) and updates in real time as $M_t$ changes through leaf credences."

(In fact $s_v$ for the AND/OR propagation tracks the agent's belief about the current plan's success on the encoded predicate. The supremum-over-Π that AAT reserves for "attainability" is computed *outside* the DAG and feeds into $\delta_\text{sat}$, not into $s_v$.)

This means: even if we identified $C_v$ with a sub-objective $O'$, the strategy DAG does not natively produce $A_{O'}$ for that sub-objective. The full diagnostic apparatus (orient cascade, satisfaction gap, control regret, 2×2 cell map) does not naturally instantiate at the sub-node level — it instantiates only at the agent level, where attainability is computed against the actual policy class $\Pi$.

### 2.4 The status field of `#def-strategy-dag` is not "recursive AAT"

The frontmatter:

```
status: conditional
depends:
  - scope-and-or
  - post-causal-structure
  - def-pearl-causal-hierarchy
  - form-objective-functional
  - def-strategy-dimension
```

The dependency on `form-objective-functional` is unidirectional — DAG terminal-conditions reference the objective functional. The reverse (sub-DAGs forming nested AAT instances with their own objective functionals) is not declared anywhere.

### 2.5 Verdict for Q5

**Internal nodes do not formally carry sub-objectives in the `#form-objective-functional` sense.** What they carry are *predicates* — Boolean satisfaction conditions whose role in the formalism is to *encode* $O_t$, not to be objectives in their own right. The segments name this distinction explicitly ("operationalize," "internal encoding," "lives outside $\Sigma_t$").

This forecloses (R1) for the load-bearing recursion: the sub-objective $O'$ is not a first-class citizen of AAT's type system. It is at best an indicator-functional, at worst a Boolean predicate, and in either case the well-formedness clause of `#def-strategy-dag` treats it as derived-from-$O_t$, not as a peer to $O_t$.

---

## 3. Q6: If sub-nodes carried genuine sub-objectives, what would the recursion look like?

This section is the V2-rescue attempt. Per project working norms, before settling on V3 I need to actually attempt a strengthening — what *would* it take to make the recursion formal? And does that attempt change anything else in the framework? The strengthening discipline here matters, because if a small natural extension makes the recursion go through and is consistent with the rest of the theory, V3 is the wrong call.

### 3.1 The proposed extension

To make every internal Σ-node carry a genuine sub-AAT instance, we'd need to lift each internal $v$ to a tuple $(O'_v, \Sigma'_v, M'_v)$ where:

- $O'_v$: a sub-objective with $V_{O'_v}: \text{trajectories} \to \mathbb{R}$ and $V_{O'_v}^{\min}$. The natural construction is:
  - For condition leaves: $V_{O'_v}(\tau) = \mathbb{1}[C_v(\tau_v)]$, $V_{O'_v}^{\min} = 1$.
  - For action leaves: similar, indicator on action-success.
  - For internal AND/OR nodes: $V_{O'_v}(\tau) = \mathbb{1}[\text{predicate at } v \text{ holds, given AND/OR aggregation of children's predicates}]$.
- $\Sigma'_v$: the sub-DAG rooted at $v$, restricted to descendants of $v$. This is itself a DAG with the right structural form (acyclic, rooted at $v$, leaves are action/condition propositions).
- $M'_v$: the agent's beliefs about $\tau_{[v]}$ — the trajectory restricted to the temporal window in which $v$'s descendants live. Under directed separation, $M'_v$ is the same $M_t$ marginalized to the relevant variables — no goal-conditioned bias, so $M'_v$ has the same independence properties as $M_t$.

Under this lift, $G'_v = (O'_v, \Sigma'_v)$ is structurally the same kind of object as $G_t = (O_t, \Sigma_t)$. The agent state at depth 1 is $X'_v = (M'_v, G'_v)$, satisfying `#form-complete-agent-state`'s shape.

### 3.2 What the extension buys you

If the lift is taken seriously:

- **(R1) is satisfied** — sub-objectives are functionals (indicators). Coarsened, but legitimate.
- **(R2) is satisfied** — sub-strategies are DAGs with the right shape, produced by restriction.
- **(R3) — the split — survives**. $V_{O'_v}$ (evaluation: did $C_v$ hold?) is type-distinct from $\Sigma'_v$ (guidance: how did the sub-DAG produce $C_v$?). The sub-level still has objective and strategy as distinct objects.

The recursion bottoms out at action leaves, where the strategy is empty (no further sub-DAG) and the objective is the indicator on action success — which is a degenerate but legitimate AAT instance with $\Sigma' = \emptyset$ (Section I as a special case, per `#form-complete-agent-state`).

### 3.3 What the extension costs

Six things break or need adjustment.

**(C1) The diagnostic scaling collapses.** AAT's diagnostic apparatus — $A_O$, $\delta_\text{sat}$, $\delta_\text{regret}$, the 2×2 cell, the convention hierarchy — is built on $V_O$ being a *real-valued continuous functional*. With $V_{O'_v}$ an indicator, $A_{O'_v} \in \{0, 1\}$ and $\delta_\text{sat}$ becomes Boolean (`#form-objective-functional` Epistemic Status: "the diagnostic results ... degrade from quantitative scalar magnitudes to qualitative set-theoretic tests"). The orient cascade's 2×2 cell becomes a Boolean diagnosis at every internal node. This is not a fatal cost — Boolean diagnostics are still informative — but it means the *quantitative* diagnostic content lives only at the agent root. Internal sub-AAT instances inherit only the structural skeleton, not the quantitative diagnostics.

**(C2) The attainability mismatch is real.** As §2.3 noted, $s_v$ from the strategy DAG is the value-of-current-policy, not the supremum-over-policy-class. To produce $A_{O'_v}$ you'd need to optimize the sub-DAG over its own policy class — but the sub-DAG's "policy class" is just the leaf-action propositions, and re-optimizing means changing the leaf credences, which means changing $M_t$, not the strategy. The supremum collapses to the current $s_v$, and $A_{O'_v} = s_v$. This is consistent with `#example-strategy`'s observation that for greedy policies $V_O = \hat\theta_{k^\ast}$, but it means the "attainability" at internal nodes is just the propagated probability — a *much weaker* quantity than $A_O$ at the agent root.

**(C3) The temporal-nesting motivation pulls toward a different recursion.** The brief's RG framing wants the recursion to interact with timescale separation — the level-$n$ sub-AAT instance should run at a slower tempo than the level-($n+1$) sub-instance. That's the "depth as temporal nesting" connection from `#der-temporal-nesting`. But the strategy-DAG depth recursion goes the other way: deeper nodes are evidence-starved (their effective rate is $\nu_k^\text{eff} = \nu_\text{base} \prod_{j<k} \theta_j$ — the deeper the slower in *update rate*, but only because of the upstream gating, not because of any temporal-scale separation in the sub-objective itself). The sub-AAT interpretation does not naturally connect to temporal nesting; the brief's "depth as temporal nesting" connection is a different thread (closer to the level-$n$ adaptive-cycle structure of `#der-temporal-nesting`'s 5-level table) and conflating the two would be a category error.

**(C4) The "fractal of agents" reading risks reintroducing the type error.** `#def-strategy-dimension` flags conflating $O$ and $\Sigma$ as a type error AAT was constructed to fix. The proposed extension preserves the split *at each level* but at the cost of treating every internal node as a mini-agent — which makes "the strategy" a DAG of mini-agents, blurring the line between $G_t$-as-state and $G_t$-as-collection-of-sub-states. If the segment voice is "$G_t$ is a structured object of type $(O_t, \Sigma_t)$," the recursion implicitly says "$\Sigma_t$ is a DAG-of-$(O',\Sigma')$-tuples." The latter is still well-typed but it's a much heavier ontological commitment than the current "$\Sigma_t$ is a DAG of nodes with credences."

**(C5) The diagnostic scaling cost compounds with the ontological cost.** Each internal node now hosts an attainability check, a satisfaction-gap test, a control-regret evaluation. The agent's working memory (already a constraint per `#def-strategy-dimension` working notes — "maintaining a 500-node DAG is qualitatively different from maintaining a 12-node one") now hosts $|V|$ sub-AAT instances rather than $|V|$ nodes. For finite-context agents (LLMs), this is a major increase in cognitive cost.

**(C6) Equivalence with HTN / options / approximate-MDP-homomorphism.** This is the load-bearing prior-art question (Q9). Hierarchical Task Networks (HTN; Erol-Hendler-Nau 1994; Nau et al. 2003 SHOP2), Sutton-Precup-Singh's Options framework (1999), and Dietterich's MAXQ value-function decomposition (2000) all decompose goals into sub-goals with sub-policies, with the sub-goals carrying termination predicates and the sub-policies being executed until the predicate holds. The MDP-homomorphism literature (Ravindran-Barto 2004, Abel et al. 2020 — already cited in `02-prior-art-rg-ib-fep.md` §4) gives error bounds for approximate sub-task aggregation. **Under the proposed extension, AAT's recursion is a more typed version of the options/MAXQ idea: each sub-option's termination predicate is the indicator-functional $V_{O'_v}$; the sub-DAG is a sub-policy; the agent executes the sub-strategy until the sub-objective is achieved.** The "more typed" part — explicit AND/OR aggregation, single-parameter edges, the Correlation Hierarchy, the L0/L1/L1' apparatus — is real AAT content that the options literature doesn't have. But the recursion *itself* is the standard hierarchical-decomposition move.

The honest scope statement: under the proposed extension, the recursion is *a typed version of options/HTN/MAXQ-style hierarchical decomposition*, with AAT's specific contributions being:
- Single-parameter edges with credence + identifiability decomposition.
- AND/OR combination semantics.
- The Correlation Hierarchy (L0/L1/L1') that handles correlated sub-task failures via an explicit common-cause factoring.
- The well-formedness clause linking sub-objective predicates to the parent objective via $V_{O_t}^{\min}$.

This is integration content, not invention content. Per the project's prior-art-integration discipline (CLAUDE.md "AAT's contribution is integration, not invention"), this is acceptable framing — but it must be framed as integration, with the options / HTN / MAXQ work cited as the antecedents.

### 3.4 The strengthening verdict

The strengthening attempt produces a formal recursion that is consistent with the existing definitions, *under the price of indicator-functional sub-objectives and the explicit acknowledgment that the recursion is a typed version of options/HTN/MAXQ*. (R1)–(R3) are satisfiable.

But the cost analysis shows two things:
- The recursion *as a load-bearing AAT-novel claim* does not survive (C6): it's a typed version of standard hierarchical decomposition, with AAT's contribution being the typing rather than the recursion itself.
- The recursion *as a structural connection* between strategy-DAG depth and form-preservation under coarse-graining is consistent with the framework but does not naturally connect to temporal-nesting (C3), so it does not provide the "single operation viewed from different axes" elegance the brief was reaching for.

This puts the question on the V2/V3 boundary. The recursion can be made formal under modification — but the modification reveals it as integration rather than invention, *and* the temporal-nesting elegance the brief wanted does not transfer through this extension. Both readings are honest.

---

## 4. Q7: What would have to change in the formal definitions

The minimal modifications to `#def-strategy-dag` and friends to make the recursion formal:

1. **`#def-strategy-dag` Formal Expression.** Add a paragraph after "Terminal satisfaction conditions" stating that *every* internal node carries a satisfaction predicate $C_v: \text{trajectories} \to \{0, 1\}$ (not just terminals), and that the well-formedness clause extends recursively:

   $$\Pr(C_{v} \text{ satisfied} \mid \text{children's predicates achieved per } \gamma_v, M_t) \geq 1 - \epsilon$$

2. **`#def-strategy-dimension` Formal Expression.** Add a recursion clause: "If $\Sigma_t$ is a DAG, each internal node $v$ induces a sub-instance $G'_v = (O'_v, \Sigma'_v)$ where $V_{O'_v}(\tau) = \mathbb{1}[C_v(\tau)]$ and $\Sigma'_v$ is the sub-DAG rooted at $v$. The full purposeful state is recursive: $G_t = (O_t, \Sigma_t)$ where $\Sigma_t$ is a DAG of $(O', \Sigma')$ instances bottoming out at action leaves."

3. **`#form-objective-functional` Discussion.** Note the indicator-valued degenerate case as a first-class instance, with the diagnostic scaling collapse acknowledged.

4. **`#def-satisfaction-gap` and `#def-value-object`.** Note that at internal sub-AAT instances, attainability $A_{O'_v}$ collapses to the propagated $s_v$ under the natural restriction (the sub-DAG cannot re-optimize over a policy class that the parent DAG is already optimizing).

5. **A new segment** would be needed to differentiate from options / HTN / MAXQ — something like `#disc-strategy-recursion-vs-htn` documenting the integration: which contributions are AAT-distinctive (typing, AND/OR, Correlation Hierarchy, well-formedness referencing $V_{O_t}^{\min}$) and which are inherited (the recursion structure itself).

These are real changes — they touch four segments and require a new one — but they are *internally consistent* with the existing theory. The framework would not break under them. The question is whether the resulting recursion is load-bearing enough to justify the surface area.

---

## 5. Q8: Differentiation from FEP-RG

`02-prior-art-rg-ib-fep.md` §2 establishes that Friston 2019 (*J. Theor. Biol.*) and Friston et al. 2025 (*Frontiers in Network Physiology*) cover the form-preservation reading of "active-inference under coarse-graining" and explicitly state functional-form invariance as the renormalization criterion. In FEP, free energy plays both objective and strategy roles: the same scalar quantity is minimized by perception (interpreting current observations) and by action (selecting next action). There is no $O$/$\Sigma$ split; expected free energy at the policy level is the only object.

If AAT's recursion is to be AAT-distinctive over FEP-RG, the $O$/$\Sigma$ split must survive recursion. Under the §3 extension, it does — at every depth, $V_{O'_v}$ (indicator on $C_v$) is type-distinct from $\Sigma'_v$ (the sub-DAG). Even when $V_{O'_v}$ degenerates to an indicator, it is *not* the same object as $\Sigma'_v$.

But this differentiation is structurally weaker than the brief's first-cut hoped. Three observations:

- **The split survives, but it survives in a degenerate form.** The sub-objectives are indicators, not real-valued functionals. The full diagnostic apparatus (continuous $\delta_\text{sat}$, continuous $\delta_\text{regret}$, the 2×2 magnitudes) does not instantiate at the sub-level; it lives only at the agent root. So while AAT's split is formally maintained at every level, its *operational content* (the diagnostic scaling) lives only at the top.
- **FEP-RG already has an analog of the split, just in a different form.** Friston 2025 RGM separates predictive posteriors over states from predictive posteriors over paths ("a clear homology with the segregation of processing in the visual cortical hierarchy" — `02-prior-art-rg-ib-fep.md` §2). This is not the same split as $O$/$\Sigma$ (the FEP version is states-vs-paths, AAT's is evaluation-vs-guidance), but the existence of a structural split that preserves under their RG already partially preempts AAT's "the split survives recursion" claim. AAT's distinctiveness is now narrowed to "the *evaluation/guidance* split survives" rather than "*some* split survives."
- **The differentiation has to live at the top-level diagnostics, not at the recursion.** What's actually AAT-distinctive is the agent-level apparatus: the convention hierarchy (C1/C2/C3), the 2×2 cell map, the orient cascade's information-dependency ordering, the Correlation Hierarchy. These are not features of the recursion; they are features of the agent. The recursion provides the *substrate* the agent's apparatus operates on, but the recursion itself adds little beyond what FEP-RG already covers.

Net: under the §3 extension, the split survives recursion in a degenerate form, but this is a thinner contribution than the brief implied. The AAT-distinctive content is at the top-level diagnostics, not at the recursion structure.

---

## 6. Q9: Distinction from HTN / Options / MAXQ — honest scope

Sub-section 3.3(C6) identified the prior art:

- **HTN planning** (Erol-Hendler-Nau 1994; Nau et al. 2003 SHOP2). Tasks decompose into methods; methods decompose recursively until primitive actions. Each task has preconditions and effects (its own success criterion, like $V_{O'}^{\min} = 1$). This is the closest classical-AI analog of the proposed §3 extension.
- **Options framework** (Sutton-Precup-Singh 1999, *Artificial Intelligence* 112). An option is a tuple $(I, \pi, \beta)$: initiation set, policy, termination condition. Termination conditions are predicates $\beta: S \to [0,1]$ — exactly the sub-$V_{O'}$ shape. Options can be hierarchical (options-over-options).
- **MAXQ value decomposition** (Dietterich 2000, *JAIR* 13). Value function decomposes recursively along a task hierarchy. Each task has its own pseudo-reward and termination predicate. This is the direct analog of recursive $V_O$.
- **MDP-homomorphism error bounds** (Ravindran-Barto 2004; Taylor-Precup-Panangaden 2008; Abel et al. 2020). Approximate aggregation of sub-MDPs with predictive-loss bounds — the bridge-lemma neighborhood (already cited in `02-prior-art-rg-ib-fep.md` §5).

Under the §3 extension, AAT's recursion is structurally a typed version of options / MAXQ (and a probabilistic version of HTN). The decomposition structure — sub-objective + sub-policy + termination predicate, recursing to primitive actions — is the same.

What's AAT-distinctive:
- **AND/OR combination semantics** as the explicit aggregation rule. Options/MAXQ use generic value composition (typically sum or max). AND/OR is more expressive for representing prerequisite-vs-alternative structure.
- **Single-parameter edges with explicit causal credence and identifiability decomposition** (`#def-strategy-dag`'s $p_{ij}$ + identifiability coefficient $\iota_{ij}$). Options/MAXQ do not maintain explicit causal credences with identification regimes attached.
- **The Correlation Hierarchy (L0/L1/L1')** that handles correlated sub-task failures via explicit common-cause factoring. This is a contribution none of HTN/options/MAXQ has — they treat sub-task outcomes as independent or do not pose the question.
- **Well-formedness referencing the parent $V_{O_t}^{\min}$.** Options' termination predicates are domain-specified; AAT's well-formedness clause requires explicit verification that the predicate operationalizes the parent objective.

What's not AAT-distinctive:
- The recursion structure itself.
- The use of termination predicates.
- The bottoming-out at primitive actions.

Honest scope statement: **the recursion, taken on its own, is essentially the same move as options / MAXQ. AAT's contribution is the typing of the move (AND/OR, single-parameter credences, identifiability, Correlation Hierarchy, well-formedness)**. This is integration content, not invention content.

If RG-2 proceeds, it should be presented as: "AAT's strategy-DAG recursion instantiates the standard hierarchical-decomposition framework of options / MAXQ, with type-level contributions (AND/OR aggregation, causal credence + identifiability, correlation handling) that the standard frameworks do not provide. The recursion itself is not novel; the typing of the recursion is."

This is the correct framing per `CLAUDE.md`'s Prior-art integration discipline. Whether it's load-bearing enough to justify a new segment depends on whether the agent-level apparatus actually exploits the recursion.

---

## 7. Verdict

I considered V1, V2, and V3 against the analysis above.

**V1 (recursion is formally legitimate and distinct from prior art) — rejected.** Two reasons. First, the segments as written do not licence the recursion: `#def-strategy-dag` explicitly says "$O_t$ itself lives outside $\Sigma_t$" and "the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires" — internal nodes are encodings, not standalone objectives, and `#def-strategy-dimension` flags conflating them as a type error AAT was constructed to fix. Second, even with the §3 extension that makes the recursion formal, the structure is not distinct from options / MAXQ — those frameworks already do hierarchical task decomposition with termination predicates. AAT's distinctive content lives in the typing (AND/OR, single-parameter credences, Correlation Hierarchy), not in the recursion.

**V3 (recursion is informal / metaphorical) — close but not quite.** The recursion can be made formal under the §3 extension, with indicator-functional sub-objectives. The framework would not break. So calling it "informal / metaphorical" is too strong — the recursion is *constructible* as formal AAT content; it just isn't load-bearing in the way the brief's first-cut framing wanted.

**V2 (recursion is formally legitimate but mostly equivalent to standard hierarchical planning) — adopted.**

The verdict is V2 with a narrow scope: the strategy-DAG recursion *can* be made formal via the §3 extension and is then a typed version of the options / MAXQ hierarchical-decomposition framework, with AAT-distinctive contributions in the typing rather than the recursion itself. **It is not, on this analysis, a load-bearing AAT-novel claim.** The split survives recursion (differentiating from FEP-RG where free energy plays both roles), but in a degenerate indicator-functional form whose operational content lives at the agent root, not at the sub-level.

### 7.1 Operational implications for RG-2

Three options for what to do with RG-2:

(a) **Drop RG-2 as a load-bearing claim.** Document the analysis here, note that the recursion is a typed instance of options/MAXQ, and let RG-2 sit as an honest structural observation rather than a load-bearing AAT-distinctive piece. This is consistent with V2: the framing is real but the contribution is integration, not invention.

(b) **Promote RG-2 as an integration-content segment.** Write a new `#disc-strategy-recursion-vs-htn` segment in the AAT-prior-art-integration mode: cite Erol-Hendler-Nau 1994, Sutton-Precup-Singh 1999, Dietterich 2000, Ravindran-Barto 2004, Abel et al. 2020 generously; note AAT's typing contributions; do not claim recursion novelty. This is consistent with `CLAUDE.md`'s prior-art-integration discipline.

(c) **Defer RG-2 entirely and keep the focus on (i) the bridge-lemma flow-distance synthesis and (ii) the directed-separation-as-order-parameter contribution from `02-prior-art-rg-ib-fep.md` §8.** These two are the actually-AAT-distinctive contributions in the RG framing. The (O, Σ) recursion is the weakest of the three remaining novelty candidates after this analysis.

My recommendation: **(c) for the immediate verdict; (b) as the eventual landing if the recursion adds operational content elsewhere in the framework**. If the strategy-DAG recursion never ends up doing load-bearing work in subsequent results — if the diagnostics live only at the agent root and the recursion is used only for narrative compactness — there is no need to formalize it. If a downstream result genuinely uses the recursion (e.g., a result that decomposes the persistence condition along DAG depth, or a result connecting evidence-starvation rates to nested-tempo separation), then (b) is the right move and the integration content gets written.

### 7.2 Honest limits

Three things this analysis did *not* establish, that future work might revisit:

- **Whether a non-degenerate $V_{O'_v}$ is constructible.** I assumed the natural construction is indicator-valued. Alternative constructions — e.g., $V_{O'_v}(\tau) = \Pr(C_v \text{ holds} \mid \tau)$, a soft-predicate value — might restore some diagnostic content at the sub-level. This is worth a focused look if RG-2 is revisited.
- **Whether the recursion has empirical traction in software / organizational domains.** TST's hierarchical task decomposition (Section IV / `02-tst-core/`) is intuitively close to this recursion. If TST's empirical work surfaces a domain where recursive sub-AAT instances *do* make load-bearing predictions that flat AAT does not, the analysis here would need to be revisited.
- **Whether RGM-style scale-free-by-construction is a better match for AAT's aspirations than recursive AAT.** Friston et al. 2025's approach builds scale-invariance into the model's parametric structure (Dirichlet hyperparameters at each scale, blocking transformations). AAT might be better off adopting this construction directly — citing FEP-RG generously — rather than trying to make recursive AAT distinctive.

---

## 8. Final verdict

**V2.** Recursion is formally legitimate (under the §3 minimal modifications) but mostly equivalent to standard hierarchical-planning frameworks (HTN, Options, MAXQ, MDP-homomorphism). AAT-distinctive content within the recursion is narrow — the typing contributions (AND/OR aggregation, single-parameter credences with identifiability, Correlation Hierarchy, well-formedness referencing $V_{O_t}^{\min}$) — and lives in the type system rather than the recursion structure. The split between $O$ and $\Sigma$ does survive recursion (differentiating from FEP-RG), but in a degenerate indicator-functional form whose operational content lives only at the agent root.

**Recommended action for RG-2**: defer. The (O, Σ) recursion is the weakest of the three remaining AAT-novelty candidates surveyed in `02-prior-art-rg-ib-fep.md` §8, and pushing it as load-bearing would force AAT into a competition with options/MAXQ on terrain where the pre-existing literature has the structural priority. The other two candidates — (i) bridge-lemma as flow-distance, (ii) directed-separation as order parameter — are stronger and should carry the RG framing's load-bearing weight.

If `99-verdict.md` decides to proceed with the RG framing on the strength of (i) and (ii), this file argues that (O, Σ) recursion should *not* be promoted as a third pillar. It can be mentioned honestly as a structural observation that follows from existing definitions under the §3 extension and is consistent with the standard hierarchical-planning literature, but it should not be advertised as AAT-distinctive content.

---

## File index

- This file: `03-rg-0c-strategy-recursion.md`
- Brief: `00-brief.md`
- Load-bearing math: `01-rg-0a-two-kalman-Kc-extension.md`
- Iterated coarse-graining: `01b-rg-0a-iterated-coarse-graining.md`
- Prior art: `02-prior-art-rg-ib-fep.md`
- Synthesis (final): `99-verdict.md`

## Source segments cited verbatim

- `01-aat-core/src/def-strategy-dag.md` (Source constraint, Terminal satisfaction conditions, Well-formedness, Strategy self-assessment, Working Notes)
- `01-aat-core/src/def-strategy-dimension.md` (Formal Expression, "the decomposition resolves a type error")
- `01-aat-core/src/form-objective-functional.md` (Definition of $V_{O_t}$, Satisfaction threshold, Epistemic Status — scope restriction)
- `01-aat-core/src/def-value-object.md` (Convention Hierarchy, Monotonicity)
- `01-aat-core/src/def-satisfaction-gap.md` (Definition of $A_O$, Convention dependence)
- `01-aat-core/src/form-complete-agent-state.md` (Formal Expression, Discussion — backward compatibility)
- `01-aat-core/src/form-structural-change-as-parametric-limit.md` (Formal Expression — six operations)
- `01-aat-core/src/example-strategy.md` (Section II Chain Instantiation — AND/OR DAG, plan confidence calculation)

## Prior-art neighbors (to cite if RG-2 is promoted)

- Erol, Hendler, Nau 1994 — UMCP HTN planning
- Nau, Au, Ilghami, et al. 2003 — SHOP2 HTN
- Sutton, Precup, Singh 1999 — Options framework, *Artificial Intelligence* 112
- Dietterich 2000 — MAXQ value decomposition, *JAIR* 13
- Ravindran, Barto 2004 — Algebraic approach to abstraction in RL
- Abel, Arumugam, Asadi, et al. 2020 — Value-preserving state-action abstractions
- Friston 2019 — Markov blankets and hierarchical self-organisation, *J. Theor. Biol.* (form-preservation)
- Friston et al. 2025 — From pixels to planning, *Frontiers in Network Physiology* (RGM)
