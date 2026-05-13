# Spike: Scalar Objective Scope Analysis

**Status**: Conceptual analysis spike. Not for promotion to `src/` — informing a scope decision for #form-objective-functional and downstream segments.

**Date**: 2026-04-01

**Motivation**: AAD's #form-objective-functional defines $V_{O_t}: \text{trajectories} \to \mathbb{R}$, requiring a total ordering on trajectory outcomes. The codex review flagged this as making the diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) less universal than they appear for organizations, safety-constrained AI, and agents with true Pareto structure. The Working Notes in #form-objective-functional suggest modeling compound objectives as terminal AND-nodes in $\Sigma_t$ with simple scalar $O_t$. This spike tests that workaround and analyzes the alternatives.

---

## 1. Where the Scalar Restriction is Load-Bearing

The real-valued codomain of $V_{O_t}$ enters AAD in five places. Not all of them require total ordering with equal force.

### 1.1 Genuinely requires total ordering

**Satisfaction gap.** $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$ requires comparing a threshold to a supremum. The supremum itself requires a total ordering on $\mathbb{R}$ — $\sup$ is not defined over a partially ordered set in general (it exists iff every bounded subset has a least upper bound, which a Pareto order on $\mathbb{R}^k$ does not guarantee for arbitrary subsets). Without total ordering, $A_O$ is not well-defined as a single number.

**Control regret.** $\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h) \geq 0$ requires subtracting two scalar values. The non-negativity guarantee ($\geq 0$) depends on the supremum property. Under a partial order, the current policy might be Pareto-incomparable with the "best" — there is no single $A_O$ to regret against.

**Policy selection.** $\pi^\ast = \arg\max_a Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ requires $\arg\max$, which requires a total ordering on the range of $Q_O$. Without it, the agent cannot select a single action — it gets a Pareto frontier of actions.

### 1.2 Does NOT require total ordering

**Orient cascade ordering.** The cascade's information-dependency argument ("you cannot evaluate strategy quality with a broken reality model") references *which quantities appear in which formulas*, not the scalar nature of those quantities. Steps 1-5 would hold identically if $V_{O_t}$ were vector-valued — the logical dependencies are structural, not numerical. The cascade ordering is scalar-independent.

**Strategy DAG structure.** The DAG itself — nodes, edges, causal credences $p_{ij}$, AND/OR combination — is defined over propositions and probabilities, not over objective values. Edge credences are scalar probabilities regardless of objective dimensionality. The DAG structure is scalar-independent.

**Directed separation.** The claim that $f_M$ has no $G_t$ argument is architectural — it says which variables enter which update functions. Replacing scalar $V_{O_t}$ with vector $V_{O_t}$ changes nothing about which functions reference which state components.

**$G_t = (O_t, \Sigma_t)$ decomposition.** The definitional split ("evaluation vs. guidance") is type-theoretic, not value-theoretic. A vector-valued evaluation criterion is still an evaluation criterion.

### 1.3 Summary

The scalar restriction is load-bearing for the **diagnostic system** ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $\delta_{\text{strategic}}$, policy selection) and non-load-bearing for the **structural theory** (cascade ordering, DAG formalism, directed separation, $G_t$ decomposition). The structural results — which constitute the majority of Section II — survive a vector extension without modification.

---

## 2. Testing the AND-Node Workaround

The Working Notes in #form-objective-functional suggest: model compound objectives as terminal AND-nodes in $\Sigma_t$, keeping $O_t$ always simple (one scalar evaluation per terminal). Let us work through a concrete case.

### 2.1 Setup: Safety + Utility Agent

An autonomous vehicle must simultaneously:
- **Safety**: probability of collision below threshold $p_c < 10^{-6}$ per trip
- **Utility**: minimize trip duration $T$

These are incommensurable: no amount of time savings compensates for a collision. The agent cannot express a single $V_{O_t}(\tau) = w_1 \cdot \text{safety}(\tau) + w_2 \cdot \text{speed}(\tau)$ without the weights implying a collision-time tradeoff rate, which is precisely what incommensurability denies.

### 2.2 AND-Node Encoding

The strategy DAG has a root AND-node with two children:

```
         [GOAL: Complete Trip] (AND)
            /              \
  [Safety Met]           [Fast Arrival]
  p_collision < 10^-6    T < T_target
       |                     |
    ... safety              ... efficiency
    subtree                 subtree
```

Each child terminal has its own scalar satisfaction criterion:
- Safety terminal: $V_{\text{safe}}(\tau) = -\log(p_{\text{collision}}(\tau))$, with $V_{\text{safe}}^{\min} = -\log(10^{-6}) = 6\log(10)$
- Speed terminal: $V_{\text{speed}}(\tau) = -T(\tau)$, with $V_{\text{speed}}^{\min} = -T_{\text{target}}$

The root AND-node propagates: $s_{\text{root}} = s_{\text{safe}} \cdot s_{\text{speed}}$ (with edge credences). The $V_{O_t}$ for the whole agent is... what?

### 2.3 Where the Workaround Works

**Satisfaction gap decomposes.** With two terminals, we get two satisfaction gaps:
$$\delta_{\text{sat}}^{\text{safe}} = V_{\text{safe}}^{\min} - A_{\text{safe}}(M_t; \Pi, N_h)$$
$$\delta_{\text{sat}}^{\text{speed}} = V_{\text{speed}}^{\min} - A_{\text{speed}}(M_t; \Pi, N_h)$$

The AND semantics say: the compound objective is met iff BOTH gaps are $\leq 0$. This is clear and actionable. The disambiguation table applies per-terminal: if $\delta_{\text{sat}}^{\text{safe}} > 0$, investigate the safety subtree; if $\delta_{\text{sat}}^{\text{speed}} > 0$, investigate the speed subtree.

**Control regret partially decomposes.** Within each subtree, $\delta_{\text{regret}}$ makes sense: "am I pursuing safety as well as I could?" and "am I pursuing speed as well as I could?" are independently meaningful questions with scalar answers.

**The cascade still orders.** Each terminal's cascade follows the same information-dependency logic: epistemic update first, then per-terminal attainability, then per-terminal regret, then (last resort) per-terminal objective revision.

### 2.4 Where the Workaround Breaks

**Cross-terminal tradeoffs are invisible.** The critical question for the AV agent is: "I can shave 30 seconds off the trip by taking a route with collision probability $3 \times 10^{-6}$ instead of $8 \times 10^{-7}$ — should I?" Both terminals are affected by the same action choice. The AND-node structure says "both must be satisfied" but gives no guidance on how to navigate the tradeoff *within the feasible region* where both constraints could potentially be met by different policies.

More precisely: $A_{\text{safe}}$ and $A_{\text{speed}}$ are each computed by $\sup_{\pi \in \Pi}$ of their respective value functionals, but the supremizing policies are generally different. The policy that maximizes safety is not the policy that maximizes speed. The AND-node encodes the constraint "both must pass," but the agent needs to *choose a single policy* that satisfies both — and the AND-node machinery provides no selection principle for doing so.

**The root $V_{O_t}$ is ill-defined.** For the diagnostics to work at the root level (not just per-terminal), we need a single $V_{O_t}(\tau) \in \mathbb{R}$ for the whole trajectory. The AND-node can produce a plan-confidence score $\hat{P}_\Sigma = s_{\text{root}}$, but this is a probability-flavored heuristic, not a value functional. There is no principled way to combine $V_{\text{safe}}(\tau)$ and $V_{\text{speed}}(\tau)$ into a single scalar without introducing the very commensurability that the agent lacks.

**Objective revision is non-trivial.** If $\delta_{\text{sat}}^{\text{safe}} > 0$ persists, the cascade says "revise $O_t$." But revising *which* terminal? And what does "relaxing the safety constraint because no feasible policy can achieve it" mean for system design? The AND-node structure pushes this to a per-terminal decision, which is correct, but the theory says nothing about *which terminal to relax when both cannot be jointly satisfied* — a question that only arises with compound objectives.

### 2.5 Verdict on the AND-Node Workaround

The AND-node encoding is **adequate for constraint satisfaction**: "are all requirements met?" decomposes cleanly. It is **inadequate for multi-objective optimization**: "which feasible policy is best?" requires comparing policies that trade off across objectives, which requires either:
- a scalarization (which imposes commensurability), or
- a Pareto-dominance criterion (which may not select a unique policy), or
- a lexicographic priority (which imposes a fixed ordering).

The workaround is useful and should be documented. It covers a common and important case (multiple must-satisfy constraints). But it does not eliminate the need for the scalar restriction — it relocates the restriction from $O_t$ to the per-terminal level, where it is less problematic because each terminal evaluates a single dimension.

---

## 3. The Vector Extension

Suppose we lift the restriction: $V_{O_t}: \text{trajectories} \to \mathbb{R}^k$ for $k$ objective dimensions. What happens?

### 3.1 Satisfaction Gap

**Component-wise definition is straightforward:**
$$\delta_{\text{sat}}^{(i)} = V_{O_t}^{\min,(i)} - A_O^{(i)}(M_t; \Pi, N_h)$$

where $A_O^{(i)} = \sup_{\pi \in \Pi} V_O^{(i)}(M_t, \pi; N_h)$ — the best achievable value on dimension $i$.

**But each $A_O^{(i)}$ is achieved by a different policy.** The per-component attainabilities are individually achievable but not jointly achievable in general. Define the **joint attainability set**:
$$\mathcal{A}_O(M_t; \Pi, N_h) = \{(V_O^{(1)}(M_t, \pi; N_h), \ldots, V_O^{(k)}(M_t, \pi; N_h)) : \pi \in \Pi\}$$

The satisfaction question becomes: does the attainability set intersect the target region $\{v \in \mathbb{R}^k : v^{(i)} \geq V_{O_t}^{\min,(i)} \; \forall i\}$? This is well-defined and computable in principle. But it replaces a scalar comparison ($\delta_{\text{sat}} \leq 0$?) with a set-intersection test ($\mathcal{A}_O \cap \text{target} \neq \emptyset$?).

**The single-number diagnostic is lost.** The original $\delta_{\text{sat}}$ gives a magnitude (how far from feasible) and a sign (feasible or not). The vector version gives a yes/no (does the intersection exist) but no natural single number for "how far." One could define $\delta_{\text{sat}}^{\text{vec}} = \min_{\pi \in \Pi} \max_i \delta_{\text{sat}}^{(i)}(\pi)$ (minimax gap), but this introduces an implicit priority structure (worst-case dimension dominates).

**Disambiguation partially survives.** The table in #def-satisfaction-gap (goal infeasible / policy class too narrow / horizon too short / model wrong) applies per-dimension. But a new row is needed: "objectives jointly infeasible" — individually achievable but not simultaneously. This is a genuinely new failure mode that the scalar formulation cannot represent.

### 3.2 Control Regret

**Pareto dominance replaces scalar comparison.** $\pi'$ dominates $\pi$ iff $V_O^{(i)}(M_t, \pi'; N_h) \geq V_O^{(i)}(M_t, \pi; N_h)$ for all $i$, with strict inequality for at least one. Define:

$$\text{Pareto-dominated}(\pi) = \exists \pi' \in \Pi : \pi' \succ_{\text{Pareto}} \pi$$

The agent has "regret" iff its current policy is Pareto-dominated — there exists an alternative that is better on at least one dimension without being worse on any. This is well-defined but:

- It does not give a scalar $\delta_{\text{regret}}$ — only a binary (dominated or not).
- A dominated policy could be far from the frontier or close to it; the binary does not measure the distance.
- The Pareto frontier itself may contain many policies, with no principled selection among them without additional structure (preferences, constraints, social choice rules).

**The 2x2 diagnostic degrades.** The original diagnostic power of the two-gap system comes from four distinct cells ($\delta_{\text{sat}} \leq/> 0 \times \delta_{\text{regret}} \approx/\gg 0$) prescribing different corrective actions. Under Pareto, we get:

| | Target region reachable | Target region unreachable |
|---|---|---|
| Not Pareto-dominated | Success | Capability limit |
| Pareto-dominated | Strategy problem | Both |

This looks similar but is coarser: "Pareto-dominated" tells you improvement exists but not how much or in which direction. "Target region unreachable" tells you feasibility fails but not which dimension is the bottleneck. The diagnostic specificity that makes the scalar version actionable (large $\delta_{\text{regret}}$ means "big strategy improvement available") is lost.

### 3.3 Orient Cascade

**The ordering survives intact.** The cascade's five steps are driven by information dependency, not by scalar arithmetic:

1. Update $M_t$ — prerequisite for everything (unchanged)
2. Evaluate attainability — requires updated $M_t$ (unchanged; the set-intersection test replaces the scalar comparison, but the dependency is the same)
3. Evaluate regret — requires attainability assessment (unchanged; Pareto dominance replaces scalar subtraction)
4. Evaluate strategic calibration — requires adequate $M_t$ and evidence of suboptimal execution (unchanged)
5. Revise $O_t$ if needed — last resort (unchanged)

The ordering is purely structural. It does not reference the dimensionality of $V_{O_t}$ anywhere. This confirms the finding from Section 1.2: the cascade ordering is scalar-independent.

### 3.4 Summary of the Vector Extension

The structural theory (cascade, DAG, separation, decomposition) is dimension-agnostic. The diagnostic system ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, the 2x2 table) degrades from quantitative scalar measures to qualitative set-theoretic tests. The degradation is real: the scalar diagnostics are more actionable. The question is whether this degradation reflects a genuine theoretical insight or a convenience of the formalism.

---

## 4. Does the Scalar Restriction Reveal Something Real?

### 4.1 The Coherent-Agency Argument

There is a substantive argument that effective agency requires commensurability, not just that the formalism requires it:

**To act, you must choose.** At each timestep, the agent selects one action from its action space. If two actions have incomparable outcomes (one is better on safety, the other on speed, and neither dominates), the agent must still pick one. The act of choosing *implicitly* imposes a total ordering on the relevant alternatives — the agent's behavior reveals a preference, even if the agent cannot articulate one.

This is the revealed-preference argument from decision theory (Samuelson, 1938). Under mild consistency axioms (transitivity, independence), revealed preferences admit a utility representation — a scalar $V_{O_t}$. The scalar restriction is not an arbitrary convenience; it follows from the logical structure of sequential decision-making under consistency.

**The counter-argument.** Organizations and multi-stakeholder systems routinely act without resolved preferences. A committee decision may cycle (A beats B beats C beats A). An AI system with multiple reward signals may exhibit intransitive behavior. These are real agents that violate the consistency axioms. The revealed-preference argument proves that *consistent* agents have scalar objectives, not that *all* agents do.

### 4.2 The Approximation Argument

Any Pareto-optimal policy corresponds to *some* scalarization — a weighted sum $\sum_i w_i V_O^{(i)}$ for some weights $w_i \geq 0$. This is the supporting-hyperplane theorem for convex sets. So the scalar formulation can represent any Pareto-optimal outcome, just not all at once:

- The scalar formalism with fixed weights represents one point on the Pareto frontier.
- Varying the weights traces the frontier (for convex feasible sets).
- The formalism misses only the *meta-question* of which weights to use.

This means the scalar restriction is less severe than it appears: AAD with scalar $V_{O_t}$ can analyze any single Pareto-optimal policy. What it cannot do is analyze the *set* of Pareto-optimal policies simultaneously, or reason about the tradeoff structure itself.

### 4.3 The Timescale Argument

There is a natural timescale separation that makes the scalar restriction less restrictive in practice:

- **Within an action cycle**: the agent must choose one action. At this timescale, it operates as if it has a scalar objective (revealed by its choice).
- **Across action cycles**: the effective weights may shift. A safety-critical situation raises safety's weight; an efficiency deadline raises speed's weight.
- **At the objective-revision timescale**: the agent or its principal may explicitly revise the scalarization weights.

AAD already has this timescale structure ($\nu_M \gg \nu_\Sigma \gg \nu_O$). The scalar $V_{O_t}$ can be understood as the *current* scalarization, which changes at the $\nu_O$ timescale. This is not a cheat — it is the claim that at any given moment, the agent's behavior reveals a scalar ordering, even if that ordering changes over time.

### 4.4 Verdict

The scalar restriction reflects a genuine insight about action-level agency: choosing an action forces a total ordering on the relevant alternatives at the moment of choice. This is substantive, not just convenient. But it is a restriction to *coherent individual agents* — organizations, committees, and multi-principal systems may genuinely lack the coherence that makes a scalar objective well-defined.

The restriction is therefore **correctly scoped** for AAD's core target (individual agents or tightly coordinated teams with unified command), and **honestly acknowledged** as a limitation for the composition setting (Section III) where multiple agents with different objectives must coordinate.

---

## 5. Recommendation

### What AAD Should Do

**Keep the scalar restriction for the core theory (Sections I-II).** The restriction is load-bearing for the diagnostic system and reflects a genuine insight about coherent agency. Removing it would sacrifice the quantitative diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$ as magnitudes) for a more general but less actionable formulation.

**Strengthen the scope note in #form-objective-functional.** The current note is honest but could be sharper. Add:
- The revealed-preference argument (why the restriction is substantive, not just convenient).
- The approximation argument (any Pareto-optimal policy has a scalar representation; the restriction excludes the meta-question of weight selection, not the individual policies).
- The timescale argument ($V_{O_t}$ is the *current* scalarization, which may change at $\nu_O$ timescale).

**Document the AND-node workaround explicitly.** Promote the Working Notes suggestion to a brief discussion in #form-objective-functional or #def-strategy-dag:
- AND-node encoding handles constraint satisfaction cleanly (all must pass).
- Per-terminal satisfaction gaps decompose naturally.
- The workaround is adequate for "multiple must-satisfy criteria" and inadequate for "multi-objective optimization within the feasible region."
- Cross-terminal tradeoff navigation requires either scalarization or external priority structure.

**Note the vector extension as future work, not current scope.** The vector extension is well-defined but sacrifices diagnostic power for generality. It belongs in Section III (composition) or in a future multi-objective extension, not in the core theory. Specifically:
- The cascade ordering is dimension-agnostic and would survive the extension unchanged.
- The DAG structure is dimension-agnostic.
- The diagnostics would degrade from scalar magnitudes to set-theoretic tests.
- The 2x2 corrective table would lose quantitative specificity.

**Add one new entry to the disambiguation table in #def-satisfaction-gap.** The compound-objective case introduces a failure mode not currently listed: "objectives jointly infeasible — individually attainable but no single policy satisfies all simultaneously." This belongs in the table even under the scalar formalism, because the AND-node workaround makes it visible through per-terminal $\delta_{\text{sat}}$ values.

### What AAD Should NOT Do

**Do not attempt a Pareto extension in Sections I-II.** The structural theory does not need it (it is already dimension-agnostic). The diagnostic system would be weakened by it. The coherent-agency argument justifies the restriction for individual agents, which is AAD's scope.

**Do not treat the scalar restriction as a deficiency.** It is a scope decision, analogous to directed separation being an architectural classification rather than an approximation. Agents with genuinely incommensurable objectives are outside AAD's core scope, just as fully merged agents (where $M_t$ depends on $G_t$) are outside the directed-separation scope. Both are acknowledged, not apologized for.

**Do not conflate the AND-node workaround with the vector extension.** The AND-node workaround keeps $V_{O_t}$ scalar at each terminal and uses the DAG's combination structure to express compound requirements. The vector extension changes the type of $V_{O_t}$ itself. These are different approaches with different tradeoffs. The workaround is a technique within the current formalism; the extension would change the formalism.

---

## 6. Implications for Existing Segments

If the recommendations above are adopted, the changes to existing segments are minor:

| Segment | Change |
|---|---|
| #form-objective-functional | Strengthen Epistemic Status scope note with the three arguments (revealed-preference, approximation, timescale). Promote AND-node workaround from Working Notes to Discussion. |
| #def-satisfaction-gap | Add "jointly infeasible" row to disambiguation table. Note that compound objectives via AND-nodes produce per-terminal $\delta_{\text{sat}}$ values. |
| #def-control-regret | No change needed. The per-terminal version follows from the AND-node structure without modifying the definition. |
| #def-strategy-dag | Add a brief note that compound objectives appear as AND-nodes near the root, with per-terminal satisfaction criteria. Already implicit in the "rootedness" constraint. |
| #der-orient-cascade | No change needed. The cascade ordering is scalar-independent. |
| #def-strategy-dimension | No change needed. The $G_t = (O_t, \Sigma_t)$ split is type-theoretic. |
| #def-value-object | No change needed. The value object machinery works per-terminal. |

No new segments are needed. The existing structure accommodates the analysis through strengthened scope notes and one additional disambiguation row.
