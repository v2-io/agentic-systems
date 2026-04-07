---
slug: directed-separation
type: derived
status: conditional
depends:
  - complete-agent-state
  - recursive-update
  - scope-condition
stage: deps-verified
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

### Architectural classification

*[Scope Condition (directed-separation-architecture)]*

Whether directed separation holds is determined by the agent's **processing topology** — specifically, whether $G_t$ is causally upstream of $f_M$ in the agent's internal processing graph. This is a structural property of the architecture, not a tunable parameter.

| Class | Topology | Directed separation | Examples |
|-------|----------|----|----|
| **1. Modular** | Separate estimator and planner, connected through state-estimate interface | Holds by construction — estimator has no causal path from $G_t$ | Kalman filter + LQR; modular RL with separate world model; military intelligence separated from operations |
| **2. Fully merged** | Single mechanism handles both epistemic and strategic processing | Fails by construction — $G_t$ is causally upstream of every computation | Transformer LLM (attention processes goals and observations together); potentially human cognition (motivated reasoning) |
| **3. Partially modular** | Some shared infrastructure, some separate pathways | Holds for modular stages, fails for merged stages | Biological cortex (shared sensory areas, separate prefrontal); hybrid AI with separate preprocessing |

**Operationalization.** The degree of coupling in partially modular architectures (Class 3) can be quantified as:

*[Definition (processing-coupling)]*

$$\kappa_{\text{processing}} = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-})}{H(G_t \mid e_\tau,\, M_{\tau^-})}$$

where $I(\cdot;\cdot\mid\cdot)$ is conditional mutual information and $H(\cdot\mid\cdot)$ is conditional entropy. The conditioning on $M_{\tau^-}$ is essential: without it, prior correlation between goals and model state (which exists even in modular agents) inflates the measure. The quantity captures *extra* goal information entering the epistemic update beyond what was already in the prior model — information that flows through shared causal paths in the processing infrastructure (paths that bypass the event $e_\tau$).

- $\kappa_{\text{processing}} = 0$: Class 1 (modular). No information about $G_t$ reaches $M_{\tau^+}$ except through $e_\tau$.
- $\kappa_{\text{processing}} \approx 1$: Class 2 (fully merged). Nearly all goal information is available to the epistemic update.
- $0 \lt \kappa_{\text{processing}} \lt 1$: Class 3 (partially modular). The value depends on the architecture's interface design.

**Distribution dependence.** $\kappa_{\text{processing}}$ is a distribution-dependent measure: it quantifies how much goal-information actually flows through the shared pathways under a given distribution of tasks, goals, and events. It does not directly measure whether pathways *exist* — that is the architectural classification (Class 1/2/3), which is structural and distribution-independent. A Class 1 agent has $\kappa = 0$ under ALL distributions (no pathway exists). A Class 2 agent has high $\kappa$ under most distributions (pathways exist and are used). A Class 3 agent's $\kappa$ varies with the task distribution — the same hybrid architecture may exhibit low coupling on familiar tasks (where the modular stages handle most processing) and high coupling on novel tasks (where goal-conditioned downstream reasoning dominates). The classification is the primary tool; the operationalization is a diagnostic for Class 3 agents where the degree of coupling is architecturally ambiguous.

**Why the classification is not a smooth parameter.** The architectural boundary between "has a separable perception module" and "processes everything through goal-conditioned attention" is discrete. Within the modular class, $\kappa \approx 0$ regardless of task. Within the fully merged class, $\kappa$ is high regardless of prompt design. Only in the partially modular class is $\kappa$ genuinely variable and worth parameterizing. This replaces the earlier $\kappa$-as-scalar framing (see `msc/spike-kappa-topology-insight.md`) which treated coupling as a smoothly tunable quantity.

**Implications for theory scope:**
- **Class 1**: Section II's results apply exactly. The sequential orient cascade is the correct analysis.
- **Class 2**: Requires coupled formulation from the start — $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition. This is the scope of `03-logogenic-agents/`.
- **Class 3**: The sequential cascade is an approximation. Approximation quality depends on $\kappa_{\text{processing}}$ and requires per-architecture error analysis.

## Epistemic Status

*Conditional* on the scope condition above. The conditional claim (IF epistemic update is goal-blind, THEN the separation holds) is exact. Whether a particular agent satisfies the condition is determined by its processing architecture (Class 1/2/3).

The architectural classification: **robust qualitative**. The three classes are structurally distinct (modular vs merged vs partial), well-motivated by examples across domains, and supported by a formal operationalization ($\kappa_{\text{processing}}$). The classification replaces the earlier $\kappa$-as-scalar framing, which is documented in `msc/spike-kappa-topology-insight.md`. The operationalization of $\kappa_{\text{processing}}$ as conditional mutual information is well-defined but typically not computable in closed form for real architectures — it serves as a conceptual anchor rather than a practical measurement tool.

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
- **Engineering design for Class 2 agents.** An LLM is internally fully merged, but the *agent system* (LLM + tools + memory + monitoring) can be designed with modular topology: separate observation processing from goal-directed reasoning, pass compressed state estimates between modules, add an external monitor that observes the $(S, A, S')$ stream independently of the LLM's attention. This creates partially-separated structure at the system level even though the component-level $\kappa$ is high. Hafez et al. (2026) provide a concrete instantiation of this pattern: the **Information Digital Twin (IDT)**, which monitors bi-predictability $P$ and entropy change $\Delta H$ from the $(S, A, S')$ stream as a modular sidecar, independent of the agent's internal processing. The IDT detects perturbations at 89% accuracy versus 44% for reward-based monitoring — empirical evidence that monitoring the information structure of the loop (Level 2 data, #loop-interventional-access) outperforms monitoring outcomes alone. For `03-logogenic-agents/`, the IDT pattern validates that modular monitoring of internally-merged agents is both feasible and effective.
- **Implication for logogenic agents**: rather than trying to extend the separated analysis to coupled agents, `03-logogenic-agents/` should start from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and show which Section II results survive as approximate or limiting cases.
