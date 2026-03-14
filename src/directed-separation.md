---
slug: directed-separation
type: derived
status: conditional
depends:
  - complete-agent-state
  - recursive-update
---

# Derived: Directed Separation

The epistemic update function $f_M$ is goal-blind: it processes incoming events without reference to the agent's objectives or strategy. The purposeful update $f_G$ depends on the updated epistemic state. Action couples all substates. This directed asymmetry — epistemic update is independent of purpose; purposeful update depends on epistemic state — is the structural backbone of the theory.

## Formal Expression

*[Derived (directed-separation, from complete-agent-state + scope condition)]*

**The update functions:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau) \qquad \text{(no } G_t \text{ argument)}$$

$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau) \qquad \text{(depends on updated } M_t \text{)}$$

**The policy:**

$$a_t = \pi(M_t, G_t) \qquad \text{(couples all substates)}$$

The three lines encode the full coupling structure:
- $f_M$ determines how the agent updates beliefs — independently of what it wants
- $f_G$ determines how the agent revises purpose — in light of what it now believes
- $\pi$ determines what the agent does — based on both what it knows and what it wants

*[Scope Condition (directed-separation-scope)]*

The claim "$f_M$ has no $G_t$ argument" requires that the epistemic update is **goal-blind conditional on the realized event**. This holds when:

1. The observation mechanism $h$ may be action-dependent ( #scope-condition allows this), but $f_M$ processes whatever event arrives without reference to why the agent sought that event
2. The agent does not use its goals to filter, weight, or interpret observations differently — no goal-dependent attention thresholds or confirmation bias baked into $f_M$

If the agent's goals influence the *observation mechanism* (goal-directed sensing, attention allocation, query selection), the **event that arrives** depends on $G_t$ through $\pi \to a_t \to e_\tau$. But $f_M$ still processes the event goal-blindly. The directed separation is about the **processing** of events, not the **selection** of events.

## Epistemic Status

*Conditional* on the scope condition above. The scope condition is genuine — many agents we care about violate it to some degree. The conditional claim (IF epistemic update is goal-blind, THEN the separation holds) is exact. Whether any particular agent satisfies the condition is an empirical question about its architecture.

## Discussion

**This is a genuine scope restriction, not a footnote.** An LLM agent's prompt includes the task objective, which shapes how it interprets code, documentation, and error messages. Its $f_M$ is goal-conditioned in practice: the agent reading code with the goal "fix the auth bug" processes the same code differently than one with "add logging." The epistemic update and purposeful evaluation are entangled in the attention mechanism.

**When the approximation is good:**
- Goal-conditioning affects *attention* (which events to seek) more than *interpretation* (how to process events that arrive)
- The agent has strong epistemic discipline (updates beliefs based on evidence quality, not goal alignment)
- The epistemic update is architecturally separated from goal evaluation (e.g., separate model-update and planning modules)

**When the approximation is poor:**
- The agent exhibits confirmation bias (interpreting ambiguous evidence in goal-consistent ways)
- Goal-conditioning is deeply embedded in the processing architecture (attention-based models where the query includes intent)
- The agent's observation channel is strategically controlled by an adversary who knows the agent's goals

**What directed separation buys the theory.** Section I's $M_t$-side quantities — $\delta$, $\eta^\ast$, $\mathcal{T}$, the persistence condition — remain well-defined on $M_t$ regardless of whether directed separation holds. What directed separation provides is the *clean factorized update*: $M_t$ updates independently, then $G_t$ updates in light of the new $M_t$, and the orient cascade resolves sequentially. Without directed separation, the $M_t$ dynamics depend on $G_t$, the update becomes a coupled system, and the sequential orient cascade becomes an approximation of a simultaneous fixed-point problem. The theory still applies — the quantities are well-defined — but the modular Section I → Section II lift becomes a coupled analysis.

**The deeper question.** Goal-conditioned epistemic dynamics — where $f_M$ depends on $G_t$ — is the formal territory of motivated reasoning, confirmation bias, and wishful thinking. A future extension would model these as departures from directed separation: coupling terms in $f_M$ that create richer (and more fragile) dynamics. The current theory treats this as out of scope, which is honest but leaves the most human-like and LLM-like agents as approximate fits.

## Working Notes

- The scope condition is more precisely a conditional independence: $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$. The epistemic update is independent of the purposeful state conditional on the prior epistemic state and the incoming event.
- Directed separation connects to the orient cascade ( #orient-cascade): the cascade's ordering ($M_t$ first, then $G_t$) is forced by the information dependency that directed separation establishes. If $f_M$ depended on $G_t$, the cascade ordering would become a simultaneous fixed-point problem, not a sequential resolution.
- **Architectural classification (from fresh-eyes assessment 2026-03-14).** Directed separation is a property of the agent's *processing architecture*, not a tunable parameter. Three architecture classes determine whether separation holds:
  1. **Modular architectures** (sensor arrays, separate estimation and planning modules, classical control): separation holds *by construction*. The estimator literally doesn't have access to the goal representation. This covers: Kalman filters, PID controllers, robotic sensor fusion, military command structures with separated intelligence and operations functions, software development teams where code review is separate from feature planning.
  2. **Fully merged architectures** (transformer attention where the prompt/goal shapes every computation): separation *fails by construction*. The processing architecture has no separable epistemic pathway — every computation is goal-conditioned through the attention mechanism. This covers: LLM agents, attention-based RL agents, potentially human cognition (where motivated reasoning is well-documented).
  3. **Partially modular architectures** (separate preprocessing with goal-conditioned downstream reasoning): separation holds for the modular stages and fails for the merged stages. The error introduced by assuming full separation depends on how much of the processing is modular vs. merged.

  This classification replaces the earlier κ-as-scalar framing (from the overnight spikes). The κ scalar implies a smooth interpolation between separated and coupled regimes, but the architectural boundary between "has a separable perception module" and "processes everything through goal-conditioned attention" is a discrete structural property, not a continuous parameter. For Class 1 agents, Section II's results apply exactly. For Class 2 agents, Section V needs a coupled formulation from the start. For Class 3, the error analysis depends on the specific architecture.
- **Implication for Section V scope**: rather than trying to extend the separated analysis to coupled agents (which requires κ and approximation error bounds), Section V should start from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and show which Section II results survive as approximate or limiting cases. This is more honest and avoids the false promise that a sufficiently clever approximation can rescue the clean factorization for architectures that structurally violate it.
