# Sketch: Strategy Dynamics Gaps (Section II)

**Status**: Working sketch for the four --GAP-- entries in Section II of `01-aad-core/OUTLINE.md`. These gaps concern how $\Sigma_t$ evolves over time — the dynamics that parallel Section I's treatment of $M_t$ dynamics but with important structural differences.

**Date**: 2026-04-01

**The four gaps, in dependency order:**
1. When observational edge updates yield valid causal semantics
2. Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)
3. Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy)
4. Three-way exploit/explore/deliberate allocation with $\Sigma_t$

Gap 1 is foundational — the others depend on edge updates working. Gaps 2 and 3 are parallel (cost and speed of strategy revision). Gap 4 integrates everything into the action-selection framework.

---

## Gap 1: When Observational Edge Updates Yield Valid Causal Semantics

### The tension

Strategy edges carry causal semantics: $p_{ij} = \text{Cr}(j \text{ advances} \mid do(i), M_t)$ — an interventional quantity (#def-strategy-dag). But the update mechanism (#hyp-edge-update-via-gain) uses observational data: "I completed step $i$, then observed whether $j$ advanced." The question: when does this observational evidence validly update an interventional credence?

### Why this isn't as bad as it sounds

The feedback loop provides Level 2 causal access *by construction* (#der-loop-interventional-access). When the agent executes step $i$, it is *intervening* — it is performing $do(i)$, not merely observing $i$. So the observation "I did $i$, then $j$ happened" is quasi-interventional data, not pure observational data.

The agent's own actions are genuine interventions in Pearl's sense: they break the causal arrows into the action node (the agent chose the action based on its strategy, not because the environment forced it). This is exactly the distinction between $P(j \mid i)$ (observational) and $P(j \mid do(i))$ (interventional).

### When it works

*[Hypothesis — conditions for valid observational-to-causal edge updates]*

Edge updates from observational data yield valid causal credence updates when all of the following hold:

**(C1) The agent intervened on the parent node.** The agent actively executed step $i$ (rather than passively observing $i$ succeed through other causes). This is satisfied whenever the agent follows its own strategy — the very act of executing the plan generates interventional data about the plan's edges.

**(C2) The outcome is attributable.** The agent can distinguish "did $j$ advance because of my $do(i)$, or for other reasons?" This is the credit-assignment problem identified in #def-strategic-calibration. It is trivially satisfied for single-parent nodes (only one possible cause) and for well-isolated interventions (the agent controls for confounders by not doing other things simultaneously). It is violated when multiple edges converge on a single node and fire concurrently.

**(C3) No unmeasured confounding between the execution decision and the outcome measurement.** If the agent chose to execute $i$ precisely because conditions were favorable for $j$ succeeding (self-selection), the observed success rate $P(j \mid \text{did } i)$ overestimates $P(j \mid do(i))$. This is a standard selection-bias concern. It is mitigated when the agent varies its execution conditions (different contexts, different orderings) rather than always executing under favorable conditions.

### The three regimes

These conditions map directly onto the CIY admissibility regimes (#def-causal-information-yield):

| Regime | C1 | C2 | C3 | Causal validity |
|--------|----|----|----|----|
| **A: Intervention-rich** (software, lab science) | Agent controls execution | Good isolation (run one test at a time) | Agent varies conditions (different inputs, configs) | **Strong.** Observational updates approximate interventional. |
| **B: Partial intervention** (organizations, complex projects) | Agent executes but with coordination constraints | Multiple concurrent actions blur attribution | Self-selection likely (execute when conditions favor success) | **Moderate.** Updates are biased toward optimism; discount factor needed. |
| **C: Observation-only** (passive monitoring, adversarial info) | Agent did not intervene | Attribution impossible | Confounding dominant | **Weak.** Edge credences reflect association, not causation. Agent should flag these edges as observationally-grounded, not interventionally-grounded. |

### The discount factor

For Regime B, a practical correction: the agent should discount the update gain for edges where attribution is uncertain. A natural form:

$$\eta_{\text{edge}}^{\text{adjusted}} = \eta_{\text{edge}} \cdot \iota_{ij}$$

where $\iota_{ij} \in [0, 1]$ is an **identifiability coefficient** — the agent's confidence that the observed outcome is attributable to edge $(i, j)$ specifically. When $\iota_{ij} = 1$ (clean attribution), the full gain applies. When $\iota_{ij} = 0$ (no attribution possible), the edge is effectively unobservable — converging with the #der-observability-dominance result.

This unifies two sources of "frozen edges": low observability of the *outcome* ($\sigma_v \approx 0$, the node's success is hard to measure) and low identifiability of the *cause* ($\iota_{ij} \approx 0$, the outcome can't be attributed to this edge). Both drive $\eta_{\text{edge}} \to 0$.

### What this means for the theory

The gap resolves as a **scope condition with graduated validity**, not a binary pass/fail. Strategy edge updates are:
- Causally valid under conditions C1-C3 (Regime A agents, intervention-rich domains)
- Biased but useful under C1 alone (Regime B agents, with identifiability discount)
- Causally uninformative without C1 (Regime C, passive observation)

The working notes in #hyp-edge-update-via-gain already flag the signal function as the critical missing piece. This sketch proposes that the identifiability coefficient $\iota_{ij}$ is a key component of that signal function.

### Epistemic status

The three-regime classification: **robust qualitative** — it follows from standard causal inference (intervention vs observation, confounding, attribution). The identifiability coefficient $\iota_{ij}$: **hypothesis** — the idea is sound but the specific functional form is unspecified. The claim that the feedback loop provides Level 2 access for strategy edges (not just $M_t$ updates): **derived** from #der-loop-interventional-access, but this extension hasn't been verified independently.

### Open questions

1. Does the interaction between $M_t$ updates and edge updates (flagged in #hyp-edge-update-via-gain's working notes) create a statistical dependency that biases edge credences? The orient cascade processes $M_t$ first, then edges — but both use the same observation.
2. Can the identifiability coefficient be estimated online, or must it be set a priori? In software (run isolated tests), $\iota$ is nearly 1 by construction. In organizations, estimating $\iota$ may require explicit causal modeling of the multi-agent environment.
3. Time-varying edge reliability: the Beta-Bernoulli model assumes i.i.d. outcomes, but real edges drift. A forgetting mechanism (exponential discounting of old observations, as noted in #hyp-edge-update-via-gain's working notes) would connect edge updates to the mismatch dynamics framework.

---

## Gap 2: Complexity Cost of Maintaining $\Sigma_t$ (IB/MDL for DAGs)

### The parallel with $M_t$

For $M_t$, the information bottleneck (#form-information-bottleneck) formalizes the compression-prediction tradeoff:

$$\phi^* = \arg\min_\phi [I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; o_{t+1:\infty} \mid a_{t:\infty})]$$

Retain enough history to predict, but no more. The trade-off parameter $\beta$ depends on volatility $\rho$ — in fast-changing environments, aggressive compression is optimal because old data decays in relevance.

The strategy $\Sigma_t$ faces an analogous tradeoff, but the terms are different.

### The strategy complexity tradeoff

*[Hypothesis — IB analog for strategy]*

$$\Sigma_t^* = \arg\min_{\Sigma} \left[C_{\text{rep}}(\Sigma) - \beta_\Sigma \cdot \Delta V(\Sigma, M_t)\right]$$

where:
- $C_{\text{rep}}(\Sigma)$: representational cost of maintaining $\Sigma$. This is the cognitive load — the agent's capacity consumed by holding the strategy. For an LLM agent, this is context window space. For a human, working memory. For an organization, coordination structure.
- $\Delta V(\Sigma, M_t)$: the value improvement from having $\Sigma$ versus pure exploration — essentially the right side minus the left side of the explicit-strategy-condition inequality ($C_{\text{explore}} + C_{\text{repair}} - C_{\text{plan}}$).
- $\beta_\Sigma$: the strategy-complexity trade-off parameter.

### What $C_{\text{rep}}$ depends on

The representational cost of a strategy DAG scales with:

1. **Graph size**: $|V| + |E|$ — more nodes and edges consume more capacity.
2. **Monitoring burden**: Each edge with $\iota_{ij} > 0$ requires the agent to track outcomes and compute updates. More monitorable edges = more ongoing cognitive cost.
3. **Maintenance frequency**: From #form-structural-change-as-parametric-limit, the six operations (reweight, reclassify, prune, graft, revise terminals, full restructure) each have costs. A strategy in a volatile domain requires more frequent maintenance.

The first-order approximation: $C_{\text{rep}} \propto |V| + |E|$ plus a maintenance term proportional to the number of active (non-frozen) edges times the environment's strategic volatility $\rho_\Sigma$.

### The volatility dependence

The $\beta_\Sigma$ parameter mirrors the $\beta$ in the $M_t$ IB objective:

- **High strategic volatility** ($\rho_\Sigma$ large — requirements change often, adversary acts frequently, the causal landscape shifts): favor simple strategies. Complex strategies can't be maintained; they become incoherent faster than they can be revised. This is the "move fast and break things" regime.
- **Low strategic volatility** ($\rho_\Sigma$ small — stable requirements, predictable environment): favor rich strategies. The investment in detailed planning pays off because the plan stays valid.

This provides the principled answer to "how detailed should my plan be?" that #norm-explicit-strategy-condition's working notes identify: **maintain a strategy just complex enough that $C_{\text{rep}}$ stays below the value improvement $\Delta V$, given the environment's strategic volatility.**

### Connection to pruning thresholds

From #form-structural-change-as-parametric-limit: when should the agent prune (remove an edge with very low credence)? The IB framework gives the answer: prune when the edge's marginal contribution to $\Delta V$ falls below its marginal representational cost. For agents with hard capacity constraints (LLM context windows), this becomes: prune the lowest-value edges until $\Sigma_t$ fits within capacity.

### MDL alternative framing

Minimum Description Length (MDL) offers a complementary view: the optimal strategy is the one with the shortest description that still captures the relevant causal structure. Under MDL:

$$\Sigma_t^* = \arg\min_\Sigma [\text{desc}(\Sigma) + \text{desc}(\text{data} \mid \Sigma)]$$

where desc(Σ) is the encoding cost of the DAG structure and parameters, and desc(data | Σ) is the encoding cost of observed outcomes given the strategy's predictions. This naturally penalizes overfitting (a complex strategy that doesn't actually predict better than a simple one wastes description bits on structure).

The MDL framing may be more natural than IB for strategy because strategies are discrete structures (graphs), not continuous distributions. The "description length" of a DAG has well-studied forms in the graphical model literature.

### Epistemic status

The IB/MDL analog: **hypothesis**. The structural parallel with $M_t$ compression is genuine — both face a complexity-value tradeoff — but the specific formulation is not derived. The claim that $\beta_\Sigma$ depends on strategic volatility: **robust qualitative** — this follows from the same logic as the $M_t$ case.

### Open questions

1. What is the correct measure of representational cost for a DAG? Node count? Edge count? Description length? Something derived from the agent's specific representational substrate?
2. Is the strategy IB separable from the $M_t$ IB, or must they be jointly optimized? (The agent has a total capacity budget split between model and strategy.)
3. For LLM agents with finite context windows, is there an explicit capacity constraint $|V| + |E| \leq K_{\text{context}}$ that makes the optimization a constrained problem? If so, the Lagrange multiplier on the capacity constraint is the "shadow price of strategy complexity."

---

## Gap 3: Rate of Useful $\Sigma_t$ Revision (Adaptive Tempo for Strategy)

### The M_t analog

Adaptive tempo for $M_t$: $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$ — the product of observation frequency and update quality across channels.

The strategic analog:

*[Hypothesis — strategic tempo]*

$$\mathcal{T}_\Sigma = \sum_k \nu_\Sigma^{(k)} \cdot \eta_\Sigma^{(k)*}$$

where:
- $k$ indexes *strategy-relevant observation channels* — observations that yield evidence about edge validity
- $\nu_\Sigma^{(k)}$ is the rate at which edge-relevant evidence arrives on channel $k$
- $\eta_\Sigma^{(k)*} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}} / \iota)$: the identifiability-adjusted edge gain from Gap 1

### Why $\mathcal{T}_\Sigma \leq \mathcal{T}$

Strategic tempo is **gated by epistemic tempo**, by the orient cascade's ordering:

1. $M_t$ must update before edge credences can be meaningfully revised (the orient cascade processes $M_t$ first).
2. Edge observations are a *subset* of all observations — not every observation is relevant to strategy edges. Many observations only inform $M_t$.
3. Edge updates require attribution (Gap 1's identifiability), which further filters the useful observation rate.

Therefore $\nu_\Sigma \leq \nu$ and $\eta_\Sigma^* \leq \eta^*$ in general, so $\mathcal{T}_\Sigma \leq \mathcal{T}$.

This is a derivable inequality, not an assumption. The orient cascade forces it.

### Timescale decomposition

From #form-structural-change-as-parametric-limit, strategy operations have a natural timescale ordering:

| Operation | Characteristic rate | What limits it |
|-----------|-------------------|----------------|
| Edge reweighting | $\nu_{\text{reweight}}$ (fast) | Observation rate for edge-relevant outcomes |
| $\gamma$ reclassification | $\nu_{\text{reclass}}$ (slow) | Needs strong structural evidence |
| Pruning/grafting | $\nu_{\text{prune/graft}}$ (slower) | Needs sustained negative/positive evidence or creative hypothesis |
| Terminal revision | $\nu_{\text{terminal}}$ (rare) | Requires persistent $\delta_{\text{sat}} > 0$ |
| Full restructure | $\nu_{\text{restructure}}$ (rarest) | Catastrophic failure only |

The overall strategic tempo is dominated by the fastest operation (reweighting), but the *health* of the strategy depends on the slower operations happening at appropriate rates. An agent that reweights quickly but never prunes accumulates dead branches (representational waste → Gap 2's complexity cost).

### Strategic tempo and the persistence schema

#schema-strategy-persistence proposes: $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$ for strategy persistence. The strategic correction rate $\alpha_\Sigma$ is essentially the strategic tempo — the rate at which the agent corrects strategic mismatch.

This gives a precise meaning to the claim: **strategy persists when strategic tempo exceeds the ratio of strategic disturbance to strategic reserve.**

The strategic disturbance $\rho_\Sigma$ has qualitatively different sources from epistemic disturbance $\rho$:
- Requirement changes (what the agent needs to achieve changes)
- Environmental causal shifts (the causal relationships the strategy depends on change)
- Adversary actions (an opponent disrupts the agent's plan)
- Information decay (edge credences become stale as conditions drift)

The strategic reserve $R_\Sigma$ is how much strategic mismatch the agent can tolerate before its actions become counterproductive. A simple strategy (few edges, robust to errors) has large $R_\Sigma$. A complex brittle strategy has small $R_\Sigma$.

### The combined picture: Gap 2 + Gap 3

Gaps 2 and 3 together describe the strategy's sustainability:
- Gap 2 (complexity cost) determines the *capacity budget* for strategy
- Gap 3 (strategic tempo) determines the *maintenance rate*
- Together: the agent should maintain a strategy whose complexity consumes no more capacity than the tempo can maintain

If $C_{\text{rep}}(\Sigma_t) \cdot \rho_\Sigma / \mathcal{T}_\Sigma > K_{\text{capacity}}$: the strategy is too complex for the agent's maintenance bandwidth. Simplify (prune), or accept drift and eventual strategic failure.

### Epistemic status

Strategic tempo as gated by epistemic tempo: **derived** from the orient cascade. The specific functional form $\mathcal{T}_\Sigma = \sum \nu_\Sigma \cdot \eta_\Sigma^*$: **hypothesis** — structurally motivated by the M_t parallel, not independently derived. The timescale decomposition: **robust qualitative** — consistent with observations across domains.

### Open questions

1. Can strategic tempo be measured empirically? In software: count how often the agent revises its plan and whether revisions improve outcomes. In organizations: track strategy-review meeting frequency and the resulting plan-confidence changes.
2. The $\mathcal{T}_\Sigma \leq \mathcal{T}$ inequality: is it tight? Can strategic tempo approach epistemic tempo, or is there a structural gap? The gap should be proportional to the fraction of observations that are edge-relevant (small for most agents — most observations inform $M_t$ but not specific edges).
3. How does $\mathcal{T}_\Sigma$ decompose across the timescale hierarchy? Is the "fast" reweighting tempo sufficient, or do the slower structural operations create bottlenecks?

---

## Gap 4: Three-Way Exploit/Explore/Deliberate Allocation with $\Sigma_t$

### From two-way to three-way

Section I's unified policy objective (#def-causal-information-yield) balances two modes:

$$\pi^* = \arg\max_a [\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}(a; M_t)]$$

For actuated agents with explicit $\Sigma_t$, the allocation becomes three-way:

1. **Exploit**: Act to pursue $O_t$ via $\Sigma_t$. Execute the next step in the plan. This is the value-maximizing mode — do what the strategy says.
2. **Explore**: Act to improve $M_t$. Seek observations that reduce model uncertainty. This is the CIY-maximizing mode — learn about the world.
3. **Deliberate**: Pause external action to revise $\Sigma_t$. Run internal simulation, evaluate alternatives, prune/graft. This is the strategy-improvement mode — think about the plan.

### Why deliberation is a distinct mode

Deliberation is NOT the same as exploration:
- Exploration generates external observations (the agent acts in the environment and observes consequences).
- Deliberation generates internal evaluations (the agent simulates consequences using $M_t$ without external action).

And deliberation is NOT a zero-action:
- During deliberation, the environment continues to evolve. The agent pays the deliberation cost (#der-deliberation-cost): $\rho_{\text{delib}} \cdot \Delta\tau$.
- The agent also stops receiving external observations (unless passive channels are still active), so $M_t$ may degrade through drift.

### The three-way objective

*[Hypothesis — extended unified policy objective]*

At each decision point, the agent allocates its next time interval to one of three modes:

$$\text{mode}^* = \arg\max_{\text{mode} \in \{E, X, D\}} \left[\text{value}_{\text{mode}} - \text{cost}_{\text{mode}}\right]$$

where:

| Mode | Value term | Cost term |
|------|-----------|-----------|
| **Exploit (E)** | $\mathbb{E}[\text{value}(a_\Sigma)]$ — expected value from executing next plan step | Opportunity cost of not exploring or deliberating |
| **Explore (X)** | $\lambda \cdot \text{CIY}(a_X)$ — information value of exploratory action | Direct cost of action + foregone exploitation value |
| **Deliberate (D)** | $\mu \cdot \Delta\eta^*_\Sigma(\Delta\tau)$ — improvement in strategy quality from deliberation | $\rho_{\text{delib}} \cdot \Delta\tau$ — mismatch accumulated during pause |

Two new quantities appear:
- $\mu(M_t, \Sigma_t)$: the value-of-strategy-improvement weight. Analogous to $\lambda(M_t)$ for exploration. Large when $\delta_{\text{strategic}}$ is high (strategy is miscalibrated) or when $\delta_{\text{regret}}$ is high (current policy is suboptimal).
- $\Delta\eta^*_\Sigma(\Delta\tau)$: the improvement in strategy quality from $\Delta\tau$ units of deliberation. Diminishing returns by the same argument as in #der-deliberation-cost.

### When each mode dominates

The three-way allocation reduces to known cases at the boundaries:

**Exploit dominates when:**
- $\delta_{\text{epistemic}}$ is low (good model — exploration unnecessary)
- $\delta_{\text{strategic}}$ is low (good strategy — deliberation unnecessary)
- $\rho_{\text{delib}}$ is high (fast-changing environment — can't afford to stop acting)
- The current plan step has high expected value

This is the "fluent execution" regime — the agent knows what's happening and has a good plan. Just do it.

**Explore dominates when:**
- $\delta_{\text{epistemic}}$ is high (poor model — uncertainty is the bottleneck)
- $\lambda(M_t) \cdot \text{CIY}$ exceeds both exploitation value and deliberation value
- The agent is in a novel environment where $M_t$ is severely inadequate

This is the "orientation" regime — the agent doesn't know enough to plan or act effectively. Learn first.

**Deliberate dominates when:**
- $\delta_{\text{strategic}}$ is high but $\delta_{\text{epistemic}}$ is low (good model, bad plan)
- $\delta_{\text{regret}}$ is high (knows what to achieve but current strategy is suboptimal)
- $\rho_{\text{delib}}$ is low (stable environment — can afford to think)
- The next plan step has low expected value or high risk

This is the "strategic pause" regime — the agent understands the situation but needs a better approach. Think before acting.

### The cascade ordering constrains the allocation

The orient cascade (#der-orient-cascade) implies: **you cannot deliberate productively before you have an adequate $M_t$.**

This creates a natural sequencing:
1. If $\delta_{\text{epistemic}}$ is high: explore first (or exploit-with-exploration), regardless of strategic mismatch.
2. If $\delta_{\text{epistemic}}$ is low but $\delta_{\text{strategic}}$ is high: deliberate.
3. If both are low: exploit.

The agent should NOT deliberate when its model is poor — it will be revising its strategy based on incorrect beliefs. This is the formal basis for the common observation that "thinking harder with bad data makes things worse."

### Connection to existing segments

- #der-deliberation-cost provides the exploit-vs-deliberate tradeoff (the bilateral case).
- #def-causal-information-yield provides the exploit-vs-explore tradeoff (the bilateral case).
- The three-way allocation is the *joint* optimization. It reduces to each bilateral case when the third mode's value is zero.
- #norm-explicit-strategy-condition provides the meta-question: "is having $\Sigma_t$ at all worth the cost?" This is answered before the three-way allocation applies — if the answer is "no," the agent operates in the two-way explore/exploit regime from Section I.

### Epistemic status

The three-way decomposition: **robust qualitative** — the three modes are functionally distinct and the examples of when each dominates are clear across domains. The specific optimization framework: **hypothesis** — the mode-selection objective is structural, but $\mu(M_t, \Sigma_t)$ is unspecified, and the joint optimization has not been derived from first principles. The claim that the orient cascade constrains the allocation (explore before deliberate): **derived** — this follows from the information dependency in the cascade.

### Open questions

1. Is the allocation discrete (choose one mode per time step) or continuous (allocate a fraction of capacity to each)? For human agents, there's some evidence for time-sharing. For LLM agents, the context window forces serial processing — you're either reading code (explore), generating code (exploit), or reasoning about approach (deliberate).
2. The interaction between exploration and deliberation: can internal simulation generate CIY? #der-deliberation-cost's open question 3 asks this directly. If deliberation can surface model inconsistencies (internal mismatch), it functions as a hybrid explore/deliberate mode.
3. In adversarial settings, the opponent benefits from the agent's deliberation pause ($\rho_{\text{delib}}$ includes adversarial disturbance). Does this create a game-theoretic interaction where each agent tries to force the other into deliberation at inopportune times?
4. How does the allocation change over the course of a task? Natural trajectory: high explore initially (build $M_t$) → high deliberate (form $\Sigma_t$) → high exploit (execute) → periodic explore/deliberate as mismatch accumulates. This matches the software development pattern: read code → plan approach → implement → debug/revise.

---

## Cross-Gap Dependencies

```
Gap 1 (edge update validity)
  └─ Gap 2 (complexity cost) — uses identifiability-adjusted gain η_Σ*
  └─ Gap 3 (strategic tempo) — uses ι_ij to define ν_Σ and η_Σ*
       └─ Gap 4 (three-way allocation) — uses T_Σ to determine deliberation value
            └─ Gap 2 (complexity cost) — the capacity budget constrains what T_Σ can maintain
```

Gap 1 is the foundation. Gaps 2 and 3 are parallel but both feed into Gap 4. Gap 4 completes the picture by integrating strategy dynamics into the action-selection framework.

## What Would Promotion to src/ Look Like?

Each gap could become one or two segments:

| Gap | Candidate slug(s) | Type | Depends on |
|-----|-------------------|------|------------|
| 1 | `edge-update-causal-validity` | Scope + Hypothesis | edge-update-via-gain, causal-information-yield, loop-interventional-access |
| 2 | `strategy-complexity-cost` | Hypothesis | information-bottleneck, explicit-strategy-condition, structural-change-as-parametric-limit |
| 3 | `strategic-tempo` | Definition + Hypothesis | adaptive-tempo, orient-cascade, edge-update-via-gain |
| 4 | `exploit-explore-deliberate` | Hypothesis | causal-information-yield, deliberation-cost, strategic-tempo |

All would enter at `draft` status with honest epistemic labels. Gap 1 is closest to promotable (the three-regime classification rests on established causal inference). Gap 4 is furthest (the three-way optimization is structural but the formal details are sparse).
