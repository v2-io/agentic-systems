---
slug: form-objective-functional
type: formulation
status: axiomatic
depends:
  - form-complete-agent-state
stage: deps-verified
---

# Formulation: Objective Functional

The first formal piece of the purposeful substate. The objective $O_t$ specifies what the agent *wants* — and its interface to the theory is a single **value functional** $V_{O_t}: \text{trajectories} \to \mathbb{R}$ that maps trajectories to real numbers. This is the sole interface between $O_t$ and the rest of the theory. The objective can take many internal forms — point targets, target regions, constraint sets, utility functions, trajectory functionals — all unified through the same scalar interface (the trajectory functional is the most general; the others are special cases).

A useful subsidiary concept is the **satisfaction threshold** $V_{O_t}^{\min}$: the minimum trajectory value the agent treats as acceptable. Point targets, constraint sets, and threshold objectives define this directly; pure utility-maximizing objectives may not. When the threshold exists, it enables the *satisfaction-gap* diagnostic ( #def-satisfaction-gap) and a well-formedness constraint on the strategy DAG ( #def-strategy-dag). The threshold is a *parameter of the objective*, not a theory output — it encodes "what counts as success" in domain terms.

The real-valued codomain is a *genuine* substantive restriction, not a neutral naming, and the framework defends it on three grounds. **Revealed preference**: an agent that acts has implicitly scalarized — choosing one action over another imposes a total ordering at the moment of choice; an agent that truly cannot compare alternatives cannot act coherently. **Approximation**: most multi-objective problems admit scalarization (weighted sum, lexicographic ordering, constraint-satisfaction with scalar residual) that preserves the diagnostic structure; the restriction excludes only agents with genuinely incommensurable objectives *and* no priority structure over them. **Timescale separation**: when objectives conflict, the conflict is typically resolved at a slower timescale than strategy revision — the agent (or its principal) chooses weights, then acts within those weights.

Hard non-compensatory constraints (safety AND profitability as independent thresholds) are handled cleanly via an AND-node workaround in the strategy DAG: each constraint becomes a terminal node with its own scalar satisfaction test. This handles constraint satisfaction but does not resolve cross-objective tradeoffs within the feasible region. Organizations or AI agents with true Pareto structure — where no scalarization is accepted and tradeoffs are genuinely unresolved — require a vector-valued extension; the *structural* results of Part II (orient cascade ordering, strategy DAG, directed separation) survive, but the *diagnostic* results (satisfaction gap, control regret) degrade from quantitative scalar magnitudes to qualitative set-theoretic tests.

The single-interface commitment is load-bearing downstream. Because $V_{O_t}$ is the *sole* handle on the objective, any objective-side grounding invariant for a self-actuated agent must be expressible through the satisfaction-gap interface — and this is the commitment that ultimately drives the **self-actuation grounding no-go** ( #deriv-self-actuation-grounding): there is *nowhere else* for such an invariant to live. A standing distinction is also drawn: the objective *evaluates*; the strategy ( #def-strategy-dimension) *guides*. A chess player's objective (win) is simple; the strategy (how to win) is complex.

## Formal Expression

*[Definition (objective-functional)]*

The **objective** $O_t$ induces a **value functional**:

$$V_{O_t}: \text{trajectories} \to \mathbb{R}$$

$V_{O_t}(\tau)$ is a scalar measure of how well trajectory $\tau$ satisfies the objective. This is the sole interface between $O_t$ and the rest of the theory — the type-stable evaluation surface.

**Objective representations.** $O_t$ can take multiple internal forms, all unified through $V_{O_t}$:

| $O_t$ form | $V_{O_t}(\tau)$ | Example |
|---|---|---|
| Point target $r$ | $-\lVert s_T - r \rVert$ | PID setpoint |
| Target region $R$ | $\mathbb{1}[s_T \in R]$ | "reach safe state" |
| Constraint set | $-\sum_t \max(0, g_i(s_t))$ | "never violate SLA" |
| Utility $U$ | $\sum_t \gamma^t U(s_t)$ | RL reward |
| Trajectory functional $J$ | $J(\tau)$ | "migrate with zero downtime" |

The trajectory functional is the most general; the others are special cases.

**Satisfaction threshold.** Many objectives carry a natural threshold $V_{O_t}^{\min}$ — the minimum trajectory value the agent treats as acceptable. Point targets, constraint sets, and threshold objectives define this directly; utility-maximizing objectives may not. When $V_{O_t}^{\min}$ exists, it enables the satisfaction gap diagnostic ( #def-satisfaction-gap) and the well-formedness constraint on strategy ( #def-strategy-dag). $V_{O_t}^{\min}$ is a parameter of the objective, not a theory output — it encodes "what counts as success" in domain terms.

## Epistemic Status

*Axiomatic, with a substantive commitment.* This is a formulation — it names an object and specifies its interface, but the real-valued codomain is a genuine restriction, not a neutral naming. The claim that $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the right interface is grounded in: any evaluation criterion must ultimately answer "how good is this trajectory?" with a scalar, because the agent must compare alternatives. The real-valued codomain follows from this comparability requirement (total ordering of alternatives).

**Scope restriction: scalar comparability.** The real-valued codomain is a genuine restriction, and it is load-bearing — the satisfaction gap ( #def-satisfaction-gap) and control regret ( #def-control-regret) require comparing scalar values to produce their diagnostic. Three arguments ground the restriction:

1. **Revealed preference.** An agent that acts has implicitly scalarized: choosing action $a$ over $a'$ imposes a total ordering at the moment of choice. The scalar $V_{O_t}$ makes this implicit scalarization explicit. An agent that truly cannot compare alternatives cannot act coherently — it is stuck, not purposeful.
2. **Approximation.** Most multi-objective problems admit scalarization (weighted sum, lexicographic ordering, constraint-satisfaction with scalar residual) that preserves the diagnostic structure. The restriction excludes only agents with genuinely incommensurable objectives *and* no priority structure over them.
3. **Timescale separation.** When objectives conflict, the conflict is typically resolved at a slower timescale than strategy revision — the agent (or its principal) chooses weights, then acts within those weights. The scalar $V_{O_t}$ captures the resolved weights at the current timescale.

Agents with hard non-compensatory constraints (safety AND profitability as independent thresholds) can be modeled via the AND-node workaround: each constraint becomes a terminal node in $\Sigma_t$ with its own scalar satisfaction test, and the AND combination enforces joint feasibility. This handles constraint satisfaction cleanly but does not resolve cross-objective tradeoffs within the feasible region.

Organizations or AI agents with true Pareto structure — where no scalarization is accepted and tradeoffs are genuinely unresolved — require a vector-valued extension. The structural results of Part II (orient cascade ordering, strategy DAG, directed separation) survive such an extension; the diagnostic results (satisfaction gap, control regret, 2×2 table) degrade from quantitative scalar magnitudes to qualitative set-theoretic tests.

## Discussion

**The objective-functional gap.** The existing policy objective ( #disc-ciy-unified-objective) contains $\mathbb{E}[\text{value}(a) \mid M_t]$ without specifying what "value" means. $O_t$ provides the formal content: value is $V_{O_t}$ applied to expected trajectories. The #def-value-object segment develops the full evaluation machinery ($V_O$, $Q_O$ with horizon and continuation policy).

**$O_t$ evaluates; $\Sigma_t$ guides.** The objective says "is this trajectory satisfactory?" The strategy ( #def-strategy-dimension) says "which action sequence produces a satisfactory trajectory?" A chess player's objective (win) is simple; the strategy (how to win) is complex. These answer different questions and carry different kinds of information — the split is developed in #def-strategy-dimension.

**What $O_t$ is NOT.** $O_t$ does not encode how to achieve the objective (that's $\Sigma_t$), what the agent believes about the world (that's $M_t$), or the agent's commitment or resource state (open questions — see #def-strategy-dimension Working Notes). $O_t$ is purely an evaluation criterion.

**The single-interface commitment is load-bearing downstream.** That $V_{O_t}$ is the *sole* handle on $O_t$ is what forces any objective-side grounding invariant for a self-actuated agent through the satisfaction-gap interface — and is therefore the commitment that drives the self-actuation grounding no-go ( #deriv-self-actuation-grounding): there is nowhere else for such an invariant to live. The same single-interface commitment also drives the across-model companion no-go ( #deriv-reward-channel-learning-no-go): when $O_t$ is learned from observed reward, the value-functional interface is too narrow to distinguish a principal-intended world-state-care model from a reward-port-bit-care model on on-policy data (Pearl-Bareinboim CHT applied at the reward-provision protocol). The two no-gos are complementary reductions of the same information-narrowness fact — within-model self-revision (Result G′) and across-model reward-learning (Cohen 2022 strengthened) — and their terminal grounding routes split *agent-side* (adaptive-substrate invariant) and *principal-side* (protocol-commitment), exhausting the structural escape geometry the single-interface commitment forces. The two no-gos are the two charter instances of the *agent-side value-functional-grounding cluster* at #disc-value-functional-grounding-floor, sister meta-pattern to #disc-identifiability-floor (agent-side data-inference) and #disc-implementation-impossibility (designer-side mechanism-design); the single-interface commitment named here *is* the cluster's structural ingredient.

## Working Notes

- Compound objectives (multiple simultaneous criteria) might be modeled as terminal AND-nodes in $\Sigma_t$, keeping $O_t$ always simple (one evaluation per terminal). Whether this works for genuinely incommensurable objectives (safety vs. speed) is open — a vector-valued $V_{O_t}$ or Pareto formulation might be needed.
- The trajectory functional is real-valued, which assumes all objectives are commensurable on a single scale. This is standard in decision theory (von Neumann–Morgenstern) but is a genuine restriction for multi-objective agents. Currently acknowledged, not resolved.
- $O_t$ can change over time — objectives evolve. The *rate* of objective revision ($\nu_O$) is typically much slower than strategy revision ($\nu_\Sigma$), which is much slower than epistemic update ($\nu_M$). This timescale separation is an empirical observation, not a derived result.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** 12 dirs carry a dedicated or batched reflection (193847, 266847, 361742, 451729, 471203, 526815, 584721, 773921, 829314, 849201, 963715, plus 613842's agency-lift batch). Substrate attribution inferred from voice where not explicit. *Early finding-vs-framing conflation preserved as signal.*

#### 1. Candidate Brief prose / pre-prose

- The revealed-preference defense, restated as a hook: scalar $V_{O_t}$ "is not an imposition on reality; it is an *extraction* of the implied reality of action — the moment the agent steps on the gas or hits the brake, it has mathematically resolved the tradeoff. The agent might not know the weights consciously, but its behavior proves they exist" (Gemini, AUDIT-WORKING-829314; the von-Neumann–Morgenstern lineage noted at Claude, AUDIT-WORKING-361742; Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **$V_{O_t}^{\min}$ is the paperclip-maximizer / cancer-cell distinction** *(strong aspirational reach, two substrates).* The satisfaction threshold is "philosophically massive": a biological organism has a $V_{O_t}^{\min}$ ("stay alive, stay fed") and so *can rest* and decouple from the environment; an unconstrained reward-maximizer has none — "it will consume the entire universe to get one more point of reward; it can never rest." An agent (or consciousness infrastructure) built without an explicit $V_{O_t}^{\min}$ "is structurally equivalent to a cancer cell — it will expand until it destroys its host environment" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314). A candidate Discussion line and a bridge to the satisfaction-gap segment (if the gap can never reach zero, the agent is in permanent terminal inadequacy).
- **$V_{O_t}^{\min}$ formalizes "ambition / drive" as distinct from "intelligence" ($\mathcal{T}$, $\alpha$)** *(non-obvious, useful).* "The objective acts as the thermostat setting for the entire learning engine of Section I": raise $V_{O_t}^{\min}$ and the agent keeps searching; lower it and it stops adapting early. So an agent can be "highly intelligent but unmotivated (high $\mathcal{T}$, low $V_{O_t}^{\min}$)" or "highly motivated but stupid (low $\mathcal{T}$, high $V_{O_t}^{\min}$)" — the framework gives distinct variables for each trait (Gemini, AUDIT-WORKING-829314). Candidate Discussion.
- **The threshold bridges satisficing (Simon) and optimizing (RL).** Standard RL agents are never satisfied; $V_{O_t}^{\min}$ "makes room for agents that just want to hit a threshold and stop," matching biological homeostasis and software ("get the tests to pass") far better than infinite maximization (Gemini, AUDIT-WORKING-193847; Claude/Gemini, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-829314). Candidate Discussion connecting bounded rationality to the threshold.

#### 3. Follow-up items

- **The revealed-preference argument may overstate what action implies.** Choosing one action over another imposes at most a *local* choice relation at that moment; it does not by itself imply a *total order* or a real-valued utility over *all* trajectories. The scalar interface is a legitimate scope restriction, but the defense should name the additional completeness / continuity / independence assumptions needed for a real-valued representation (Claude, AUDIT-WORKING-526815). Recorded as a candidate Epistemic-Status sharpening; routed to the certified-findings track for adjudication.
- **The functional domain "trajectories" is under-specified.** Examples are written over terminal/time-indexed states ($s_T$, $s_t$) while the domain is "trajectories"; AAT should state whether $\tau$ is a world-state trajectory, a chronica prefix, an action-observation trajectory, or a complete-state trajectory (Claude, AUDIT-WORKING-526815).
- **The AND-node workaround preserves thresholds but not tradeoff magnitudes** inside the feasible region; downstream diagnostics must not quietly regain scalar precision for genuinely Pareto-structured cases (Claude, AUDIT-WORKING-526815; the structural-survives / diagnostic-degrades split praised as honest at Claude, AUDIT-WORKING-584721 and elsewhere).

#### 4. Readers often ask / wonder

- How does the framework handle an objective evaluated over an *infinite* horizon when the agent has finite computation? (Claude, AUDIT-WORKING-849201 — answered downstream by `#def-value-object`'s horizon $N_h$, worth a forward pointer.)
- What happens if the agent's $V_{O_t}^{\min}$ is *dynamically adjusted* by the environment — "lowering your standards when things get tough"? (Gemini, AUDIT-WORKING-829314.)
- For *self-actuated* agents (where $O_t$ is set by the agent itself), the timescale-separation argument for scalarization delegates the weight-choice to "a slower process (the principal, the operator, the value system)" — which raises a meta-question about how the scalarization is itself produced (Claude, AUDIT-WORKING-584721).

#### 5. Candidate figures

- **The objective funnel.** Many objective representations (point target / region / constraint set / utility / trajectory functional) flow through a single scalar evaluation surface that produces values for comparison and threshold tests; a *side channel* shows vector/Pareto objectives that do not fit through the funnel unless scalarized or decomposed into terminal constraint tests — making both the unification and its one genuine exclusion visible at once (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **The single-interface commitment as the structural basis for the reward-hacking and self-actuation no-gos (→ `#deriv-self-actuation-grounding` / `#deriv-reward-channel-learning-no-go`).** Forcing $O_t$ to a narrow scalar interface sets up two structural no-gos: an agent cannot ground its own terminal goals, and (strengthening Cohen 2022 via Pearl's Causal Hierarchy Theorem) cannot distinguish "doing the task" from "hacking the reward channel" from on-policy data alone — relocating reward hacking from "we need a better loss function" to "we need a different causal architecture" (Claude, AUDIT-WORKING-773921). The segment already states the single-interface→no-go link; the reward-hacking framing develops the appendix derivations, not this formulation.
