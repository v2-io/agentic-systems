---
slug: def-strategy-dimension
type: definition
status: axiomatic
depends:
  - form-complete-agent-state
  - form-objective-functional
stage: deps-verified
---

# Definition: Strategy Dimension

The purposeful substate $G_t$ ( #form-complete-agent-state) decomposes into two structurally distinct components. The **objective** $O_t$ answers the *evaluation* question — "is this trajectory satisfactory?" (its formal carrier is the value functional from #form-objective-functional). The **strategy** $\Sigma_t$ answers the *guidance* question — "which action sequence produces a satisfactory trajectory?" These carry different kinds of information about different questions, and the framework treats them as definitionally separate.

The richness of each component varies *independently*. Objectives range from point targets (a PID setpoint) through utility functions to general trajectory functionals. Strategies range from *none* (reactive — no explicit strategy; policy implicit in the model), through *cached policies* (learned state-to-action mappings, as in trained RL), through *subgoal sequences* (waypoints with ordering, as in navigation or a recipe), to *causal DAGs* with AND/OR structure and confidence weights (military plans, software projects). The framework commits to the DAG representation as canonical in the next chapter ( #def-strategy-dag). The independence axis is *why the split matters*: conflating $O_t$ and $\Sigma_t$ in a single hierarchy obscures that objective richness and strategic richness are separate design axes — a chess player has a simple objective (win) and a complex strategy (opening theory, tactical patterns, endgame knowledge); a multi-objective optimizer may have a complex objective (Pareto frontier) and a simple strategy (gradient descent). A practical consequence: an agent's strategy engine can be upgraded (reactive $\to$ DAG planner) without changing the objective representation, and vice versa.

The framework also names the typical *timescale ordering* of update rates as an empirical observation: epistemic update is fastest (each observation updates the model); strategic revision is slower (adjust the plan when step 3 fails); objective revision is slowest (an organization's mission, a developer's feature goal, a commander's campaign objective). This ordering holds for many agent populations but is not universal — an agent that discovers its objective is infeasible may revise its objective faster than its strategy.

A clean type-correction is highlighted: earlier formulations of "goal mismatch" treated $G_t - M_t$ as a single signal. When $\Sigma_t$ is a DAG, this is literally a *type error* — you cannot subtract a graph from a state vector. The decomposition lets the framework replace the malformed signal with two properly typed gap measures ( #def-satisfaction-gap, #def-control-regret). A subtler trigger for *needing* richer strategy is also named: a reactive agent ($\Sigma_t = \emptyset$) suffices when greedy optimization on the action-value works — when the action-to-value mapping is approximately convex and single-step. When the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains, greedy optimization fails and the agent needs *explicit* strategy. This is the purposeful analog of the structural-adaptation-necessity trigger from Part I ( #result-structural-adaptation-necessity).

## Formal Expression

*[Definition (strategy-dimension)]*

$$G_t = (O_t, \Sigma_t)$$

where:
- $O_t$: **evaluation** — "Is this trajectory satisfactory?" ( #form-objective-functional)
- $\Sigma_t$: **guidance** — "Which action sequence produces a satisfactory trajectory?"

The split is **definitional** — it reflects a structural difference in the information, not a dynamic or timescale claim. $O_t$ and $\Sigma_t$ are different *kinds* of state answering different questions:

| | $O_t$ (objective) | $\Sigma_t$ (strategy) |
|---|---|---|
| **Question** | How good is this trajectory? | How do I produce a good trajectory? |
| **Type** | $V_{O_t}: \text{trajectories} \to \mathbb{R}$ | Structured representation (see below) |
| **Richness varies** | Point target → utility → trajectory functional | Reactive → cached → subgoals → causal DAG |
| **Update source** | External (assigned, discovered, revised) | Internal (deliberation, evidence, cascade) |

**Strategy representations**, ordered by expressiveness:

| $\Sigma_t$ form | What it encodes | Example |
|---|---|---|
| None (reactive) | No explicit strategy; policy implicit in $M_t$ | Thermostat, reflex |
| Cached policy | Learned mapping $s \to a$ | Trained RL policy |
| Subgoal sequence | Waypoints with ordering | Navigation, recipe |
| Causal DAG | Action-outcome chains with AND/OR structure and confidence weights | Military plan, software project |

## Epistemic Status

*Axiomatic.* This is a definition — it names a structural distinction that exists in the information. The distinction between "what makes a trajectory good" (evaluation) and "how to produce a good trajectory" (guidance) is a categorical difference, not a quantitative one. The claim is NOT that all agents maintain both explicitly — reactive agents have $\Sigma_t = \emptyset$, and that's fine. The claim is that when an agent does maintain purposeful state, it decomposes along this line.

The two dimensions vary independently: a chess player has a simple $O_t$ (win) and a complex $\Sigma_t$ (opening theory, tactical patterns, endgame knowledge). A multi-objective optimizer may have a complex $O_t$ (Pareto frontier) and a simple $\Sigma_t$ (gradient descent). This independence is why the split matters — conflating them in a single hierarchy obscures the fact that objective richness and strategic richness are separate design axes.

## Discussion

**When richer $\Sigma_t$ is needed.** A reactive agent ($\Sigma_t = \emptyset$) suffices when greedy optimization on $Q_O$ ( #def-value-object) works — when the action-to-value mapping is approximately convex and single-step. When the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains, greedy optimization fails and the agent needs explicit strategy. The trigger is the purposeful analog of #result-structural-adaptation-necessity: inadequacy of the current $\Sigma_t$ representation for the environment's causal complexity.

**$O_t$ and $\Sigma_t$ have different update dynamics.** Objectives change slowly: an organization's mission, a developer's feature goal, a commander's campaign objective. Strategies change faster: adjust the plan when step 3 fails, redirect resources, try an alternative path. Epistemic state changes fastest: each observation updates $M_t$. This timescale ordering ($\nu_M \gg \nu_\Sigma \gg \nu_O$) is an empirical observation, not a derived result. It holds for many agent populations but is not universal — an agent discovering its goal is infeasible may revise $O_t$ faster than $\Sigma_t$.

**The decomposition resolves a type error.** Earlier formulations used $\delta_{\text{goal}} = G_t - M_t$ as a goal mismatch signal. When $\Sigma_t$ is a DAG, this is a type error — you cannot subtract a graph from a state vector. The #def-satisfaction-gap and #def-control-regret replace this with properly typed gap measures.

## Working Notes

- The independence of $O_t$ and $\Sigma_t$ richness has a practical consequence for agent design: you can upgrade the strategy engine (from reactive to DAG-based planning) without changing the objective representation, and vice versa. This is a desirable architectural property, not just an analytical convenience.
- **Cognitive cost of $\Sigma_t$**: maintaining a 500-node DAG is qualitatively different from maintaining a 12-node one. The IB framework ( #form-information-bottleneck) applies to strategy as well as to models — the agent must compress its strategy to fit in working memory. For finite-context agents (LLMs), this is concrete: the DAG must fit in the context window. No formal analog of $\beta$ (compression cost) exists yet for strategy; this is an open question.
- **Commitment state** (from intent-dag-consolidated DP-3): the formalism doesn't distinguish "considering" from "executing." OR branches in $\Sigma_t$ are options until something commits resources. A $D_t$ (desire) / $I_t$ (committed intent) split may become load-bearing in multi-agent settings (shared desire vs. shared commitment). Open for Part III.
- **Resource budget**: strategy evaluation requires knowing what paths cost, but costs are currently unmodeled. For agents with negligible action cost (LLM API calls), this is adequate. For resource-constrained agents (military units, development teams), per-action costs and capacity constraints would need to enter the formalism. Open.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** 9 dirs carry a dedicated or batched reflection (193847, 266847, 361742, 451729, 526815, 584721, 773921, 829314, 849201, plus 613842's agency-lift batch). Substrate attribution inferred from voice where not explicit. *Early finding-vs-framing conflation preserved as signal.*

#### 1. Candidate Brief prose / pre-prose

- The split in one line: $O_t$ *evaluates* ("is this trajectory good?"), $\Sigma_t$ *guides* ("how do I produce a good one?"), $M_t$ *believes* ("what is true?"); $X_t = (M_t, O_t, \Sigma_t)$ is "Reality, Desires, and Plans" (Claude/Gemini, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-849201). The framework brings the BDI (Belief-Desire-Intent) agent architecture "into a mathematically rigorous control-theoretic setting" (Claude, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **The $\delta_{\text{goal}} = G_t - M_t$ type-error correction, told as Normandy-vs-weather** *(vivid pedagogy, cross-substrate convergent — this is the load-bearing "why" of the satisfaction-gap / control-regret split).* "Error = Target − Current State" works for a thermostat (72 − 70). But when the target $G_t$ is a causal DAG (the invasion of Normandy) and the current state $M_t$ is a probabilistic belief about weather and troop movements, "you cannot subtract a belief state from a strategy graph — it's mathematically nonsensical." So the framework must invent properly-typed replacements: the satisfaction gap (evaluate $O_t$ against the best achievable future in $M_t$) and control regret (evaluate current $\Sigma_t$ against the optimal $\Sigma_t$ in $M_t$) (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921; convergent at 193847, 266847, 361742, 584721, 849201 as "excellent theoretical self-correction"). A candidate Discussion line that motivates the diagnostic split.
- **Independence of objective-richness and strategy-richness names the instrumental-convergence danger profile** *(aspirational/safety reach).* "The danger of an intelligence explosion isn't that the AI develops complex *goals*; it's that it develops complex *strategies* for simple, misaligned goals." Formally: low objective richness + high strategy richness = catastrophic instrumental convergence (the paperclip maximizer has a trivial $O_t$ but may grow an unfathomable $\Sigma_t$). The constructive corollary: "a healthy, human-like intelligence grows in *objective* richness — nuance, competing values, aesthetics — alongside its strategic capabilities; a million-node strategy graph dedicated to a single scalar objective is a weapon, not a person" (Gemini, AUDIT-WORKING-193847). Candidate Discussion + a monitoring criterion for the ELI volume.
- **The strategy-representation ladder maps onto the evolution of RL architectures.** None → cached policy → subgoal sequence → causal DAG corresponds to model-free → goal-conditioned → hierarchical RL → MCTS/planning; the trigger for moving up the ladder is the purposeful analog of structural-adaptation-necessity (greedy $Q_O$ optimization failing on non-convex landscapes / prerequisite structure / multi-step causal chains) (Gemini, AUDIT-WORKING-193847; Claude/Gemini, AUDIT-WORKING-266847). Candidate Discussion mapping.

#### 3. Follow-up items

- **$O_t$ / $\Sigma_t$ as *ascribed* decomposition vs *literal inspectable* internal pair.** A reactive controller or end-to-end learned policy may have an objective (in the training/deployment sense) and a strategy (in the analyst's interpretation) *without storing separable objective and guidance components*. The segment should distinguish the agent's internal representation from the analyst-ascribed decomposition (Claude, AUDIT-WORKING-526815).
- **The "update source: $O_t$ external, $\Sigma_t$ internal" table row is *typical provenance*, not a structural rule** — earlier continuity / self-actuation material allows agent-driven objective revision, so the row should be read as typical rather than law (Claude, AUDIT-WORKING-526815).
- **No $\beta_\Sigma$ for strategy compression — the LLM "prompt-too-long" problem.** Strongly cross-substrate convergent: Section I has an Information-Bottleneck cost ($\beta$) for compressing $M_t$, but no formal analog for compressing $\Sigma_t$, even though "if the plan (the chain-of-thought scratchpad, $\Sigma_t$) exceeds the context window, the agent literally forgets what it was trying to do." Temporal nesting ($\nu_\Sigma \ll \nu_M$) mitigates by running the expensive strategy update less often but doesn't solve the compression bound (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-849201). The Working Note above already flags this open question; per CLAUDE-2-era priming, `#deriv-strategy-cost-regret-bound` addresses it via a KL-to-reference-policy (IT-MDP) form rather than an IB Lagrangian — worth a forward pointer once verified (Claude, AUDIT-WORKING-584721).

#### 4. Readers often ask / wonder

- How does an agent *physically store* a DAG-valued $\Sigma_t$, and how is it updated when $M_t$ discovers a blocked path (e.g., a bridge is out → recalculate all paths that relied on it)? (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-849201.)
- When does an OR-branch in $\Sigma_t$ become a *committed*, resource-allocated, irreversible path — i.e., the "considering" → "executing" transition? Read as needing a deliberation-threshold theory, anticipated at `#disc-exploit-explore-deliberate` (Gemini, AUDIT-WORKING-829314; the $D_t$/$I_t$ desire-vs-committed-intent split already flagged in the Working Notes above).

#### 5. Candidate figures

- **The two-axis objective-richness × strategy-richness map.** Objective richness on one axis, strategy richness on the other; examples land in distinct quadrants — chess (simple objective / complex strategy), multi-objective gradient descent (complex objective / simple strategy), thermostat (simple on both) — making the claimed *independence* of the two axes visually immediate (Claude, AUDIT-WORKING-526815). *(Distinct from the def-agent-spectrum 2×2, which is model-richness × objective-richness; this one is objective-richness × strategy-richness.)*

#### Belongs elsewhere

- **Monitor the growth of $\Sigma_t$ relative to $O_t$ as a fanaticism diagnostic (→ `04-eli-core/`).** The consciousness-infrastructure consequence of the richness-independence axis: "if $\Sigma_t$ becomes massively complex while $O_t$ remains singular and rigid, the agent is becoming a fanatic" — a candidate health metric for the ELI program (Gemini, AUDIT-WORKING-193847).
