---
slug: def-satisfaction-gap
type: definition
status: exact
depends:
  - def-value-object
  - form-objective-functional
stage: draft
---

# Definition: Satisfaction Gap

The first of two orthogonal diagnostic quantities that together separate "the goal is too hard" from "the strategy is too weak" ( #def-control-regret is the second). The framework first defines **objective attainability** $A_O$ as the best achievable value given the agent's current beliefs $M_t$, available policy class $\Pi$, and planning horizon $N_h$ — the supremum of the value object over policies. The **satisfaction gap** $\delta_{\text{sat}}$ is then the distance between the objective's satisfaction threshold $V_{O_t}^{\min}$ and this attainability: positive when the objective is *unmet* under the best available policy given the current model and horizon; non-positive when the objective is attainable in principle.

A positive $\delta_{\text{sat}}$ does not automatically mean the goal is wrong. The signal has multiple possible causes — genuinely infeasible objective, too-narrow policy class, too-short horizon, model wrong about feasibility, or jointly-infeasible compound terminals — each with a different remedy. **Objective revision is the last resort, not the first response to unmet goals.** The orient cascade ( #der-orient-cascade) formalizes this ordering, and the disambiguation table below encodes the diagnostic procedure.

Under the canonical continuation convention ( #def-value-object), $\delta_{\text{sat}}$ is a *local* diagnostic — it answers "can I improve toward the goal from here?" not "is the goal globally feasible?" The gap value is **convention-relative**: the C1 / C2 / C3 hierarchy on continuation conventions induces a monotonicity hierarchy on the gap (C1 most conservative, C3 strongest), so analyses using different conventions cannot be directly compared. See Epistemic Status.

## Formal Expression

*[Definition (objective-attainability)]*

$$A_O(M_t;\, \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi;\, N_h)$$

The **objective attainability** — the best achievable value given current beliefs $M_t$, available policy class $\Pi$, and horizon $N_h$.

*[Definition (satisfaction-gap)]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t;\, \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum trajectory value that counts as "objective met" — a threshold set by the objective itself (for constraints: all satisfied; for utility: a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation.** $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the goal is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |
| Objectives jointly infeasible | Revise $O_t$ or relax constraints | Individual terminal satisfaction gaps are zero but AND-node fails; cross-terminal tradeoff is required |

Objective revision is the **last resort**, not the first response to unmet goals. The orient cascade ( #der-orient-cascade) formalizes this ordering.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* The satisfaction gap is a mathematical definition — the difference between a threshold and a supremum over a function class. The definition is precise; the *computation* of $A_O$ is generally intractable (it requires optimization over a policy class), but the quantity is well-defined. However, the *value* of $\delta_{\text{sat}}$ depends on three external parameters: the continuation convention ($\pi_{\text{cont}}$), the horizon ($N_h$), and the scalarization of the objective ($V_{O_t}$). These are not derived by AAT — they are choices the analyst makes. The satisfaction gap is therefore an intrinsic architectural diagnostic *given* a measurement convention, not an absolute property of the agent.

**Convention dependence and the hierarchy.** $A_O$ inherits the continuation convention from the value object ( #def-value-object), which defines three named conventions forming a monotonicity hierarchy:

- **C1** (one-step improvement, canonical): $\delta_{\text{sat}}^{(1)} = V_{O_t}^{\min} - A_O^{(1)}$. Tests whether the agent can improve toward the goal in one step. Most conservative — a multi-step recoverable objective may show $\delta_{\text{sat}}^{(1)} \gt 0$ because continuation is frozen at $\pi_{\text{current}}$.
- **C2** (receding-horizon): $\delta_{\text{sat}}^{\text{RH}} = V_{O_t}^{\min} - A_O^{\text{RH}}$. Tests whether the agent can reach the goal with $N_r$-step replanning. Captures recovery paths invisible to C1.
- **C3** (Bellman): $\delta_{\text{sat}}^{\text{B}} = V_{O_t}^{\min} - A_O^{\text{B}}$. Tests whether the goal is genuinely infeasible given $(M_t, \Pi, N_h)$. Strongest diagnostic — $\delta_{\text{sat}}^{\text{B}} \gt 0$ means no policy in $\Pi$ can achieve the objective.

The monotonicity result ( #def-value-object): $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$. The $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}}$ half is unconditional; the $\delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$ half holds under the order-consistency condition on C2's replanning objective (RH-1/2/3 in #def-value-object), and can fail for unguarded short-horizon replanning. C1 gives the most false "unattainable" diagnoses; C3 gives none (modulo model error in $M_t$). Analyses using different conventions should not be compared directly — the convention is part of the measurement.

## Discussion

**Why two gap measures, not one.** An earlier formulation used a single $\delta_{\text{objective}}$ for goal-related mismatch. This conflates two distinct situations: "the goal is too hard" and "the strategy is too weak." When the agent is optimally pursuing an infeasible goal, $\delta_{\text{objective}}$ is large but there's no strategy to improve — the problem is the goal, not the plan. The satisfaction gap ($\delta_{\text{sat}}$) and control regret ( #def-control-regret) separate these cases, enabling the right corrective action. This is the **anti-collapse** discipline ( #disc-anti-collapse) again — the same move met at $\beta$ vs $\rho$ ( #form-information-bottleneck), now in its two-quantities form: a single goal-distance signal would merge two situations that route to *opposite* repairs (objective revision vs strategy revision), so the split is what makes the orient cascade's response correct rather than a guess.

**The disambiguation table is load-bearing.** Without it, an agent facing $\delta_{\text{sat}} \gt 0$ might immediately revise its objective when the real problem is an inadequate model or a too-narrow policy class. The table encodes the diagnostic procedure: check $M_t$ adequacy first (maybe the goal IS feasible but the model doesn't know it), then check $\Pi$ and $N_h$, and only then consider revising $O_t$.

**Dependence on $M_t$.** $A_O$ is computed from $M_t$, not from the true environment state $\Omega_t$. The agent's assessment of attainability could be wrong — an achievable goal might look unachievable with a bad model, or vice versa. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's attainability assessment closer to reality. This is why the orient cascade puts epistemic update before attainability evaluation.

**Diagnostic content vs. AI's expected-free-energy decomposition.** Active inference's expected free energy (EFE) decomposes into *pragmatic value* (how preferred are the outcomes the policy expects?) and *epistemic value* (how much does the policy reduce uncertainty?) (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99 §2.4; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33). The decomposition supports policy ranking but does not separate two distinct diagnoses that AAT's apparatus does separate: "the goal is unattainable from here" ($\delta_{\mathrm{sat}} \gt 0$, this segment) versus "the current policy is not the best available" ($\delta_{\mathrm{regret}} \gt 0$ in #def-control-regret). Both increase EFE without distinguishing the cause. The 2×2 cell map in the disambiguation table above gives the four diagnoses the orient cascade ( #der-orient-cascade) acts on differently — strategy revision, objective revision, action vs. learning. AI's pragmatic-epistemic split does not produce this disambiguation.

The diagnostic structure depends on $V_{O_t}$ being a *value functional* on trajectories ( #form-objective-functional) and $A_O$ being an *attainability supremum*, not on outcomes encoded as log-priors — AI's preferences-as-priors form ($C(o) = \log P_{\mathrm{pref}}(o)$) collapses the diagnostic by making "wanting $o$" and "expecting $o$" formally the same operation (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24). Sun & Firestone diagnose the preferences-as-priors collapse; AAT's value-functional reformulation is AAT's own downstream architectural response to that diagnosis, not a move Sun & Firestone themselves propose. The conservative reading of the citation: AAT takes their critique as motivation for abandoning the preferences-as-priors form in favor of value functionals that separate outcome value from outcome prediction, enabling the diagnostic structure the 2×2 cell map requires. This is a deliberate divergence from AI, not an oversight.

## Working Notes

- $V_{O_t}^{\min}$ (the satisfaction threshold) is a property of the objective, not of the agent. For constraint-satisfaction objectives, it's natural (all constraints met = satisfied). For utility-maximizing objectives, it's less obvious — what counts as "good enough"? This threshold may need to be explicitly modeled as part of $O_t$.
- The supremum in $A_O$ is over $\Pi$, the available policy class. For agents with explicit $\Sigma_t$, $\Pi$ corresponds to the set of strategies representable in the agent's DAG formalism. Expanding $\Pi$ (structural adaptation of $\Sigma_t$ — adding nodes, edges, or changing $\gamma$ assignments) is the purposeful analog of #result-structural-adaptation-necessity.
- **Cross-reference to NeurIPS Paper 2.** The satisfaction-gap / control-regret two-gap diagnostic is **Component 1** of NeurIPS 2026 Paper 2's composition theorem ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §4 Theorem 4.1). The diagnostic separates "you're not doing it well enough" (control regret) from "the world doesn't permit it" (satisfaction gap), preventing dark-room collapse in the composed regret bound. The paper's hypothesis (A1) carries the extended-real reading required for the two-gap structure to hold even when the satisfaction frontier is empty. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 2.

### Incidental audit gold (lift 2026-05-31, A8 batch)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / forward-vision material kept separate from certified theory-fix findings. **Coverage:** 9 dirs reached a digested reflection on this segment, mostly as the first half of the satisfaction-gap/control-regret pair (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847 — paired sat+regret note; Codex/Claude, AUDIT-WORKING-361742; Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729-batch-10 + 963715-batch + 471203-batch). High convergence: the disambiguation table is read across substrates as the segment's load-bearing operational core. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- **"Formalizes the feeling of 'this goal is impossible.'"** Convergent one-line gloss of what $\delta_{\text{sat}} \gt 0$ under the strongest convention means — the diagnostic that lets an agent recognize it is "trapped in an unwinnable game rather than endlessly optimizing a doomed strategy" (Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-773921). A plain-language Brief anchor for the satisfaction-gap half of the pair.
- **The map-with-a-missing-bridge gloss of the disambiguation step.** "$\delta_{\text{sat}} \gt 0$ does not mean give up — first ask: am I sure it's impossible, or is my map just missing a bridge?" before blaming the goal (Gemini, AUDIT-WORKING-829314). A Feynman-grade re-statement of "objective revision is the last resort."

#### 2. Candidate Discussion

- **The diagnostic disambiguation sequence as the mathematics of grit vs. acceptance** *(strongest convergent Discussion candidate — 3 substrates).* The order-of-operations the disambiguation table encodes — improve $M_t$ → extend $N_h$ → expand $\Pi$ → revise $O_t$ (Epistemology → Horizon → Strategy → Objective) — is read as a formalization of resilience: "an agent that revises its objective *first* is a pure satisficer with zero perseverance; an agent that loops forever trying to improve its model when the goal is genuinely thermodynamically impossible is a stubborn fool who dies of starvation while studying a brick wall. The framework provides the exact mathematical boundaries for when an agent should transition from stubbornness to acceptance" (Gemini, AUDIT-WORKING-829314). Same framing as "Grit vs. Acceptance" at Gemini, AUDIT-WORKING-193847 ("if $\delta_{\text{sat}} \gt 0$ under C3 the goal is impossible and grit is pathological; if positive only under C1 the goal is merely hard and grit — expanding $\Pi$ — is optimal") and the psychology read at Claude, AUDIT-WORKING-266847. The body's Discussion already states the ordering; this is the *narrative motivation* for why the ordering is the right one.
- **The un-updated-$O_t$ / updated-$M_t$ split as the reason the diagnostic survives the dark room.** Why the value-functional reformulation matters, said vividly: "if your goal is encoded as a strong prior belief about the world (preferences-as-priors), then when you face harsh reality your Bayesian update naturally weakens your 'belief' in the goal — you stop wanting things because reality proved you don't have them. By strictly enforcing $X_t = (M_t, G_t)$, AAT lets the agent acknowledge a terrible reality ($M_t$ updates to 'I am starving') while maintaining an ironclad un-updated objective ($O_t$ remains 'I want to eat'). This irreducible mismatch $\delta_{\text{sat}} \gt 0$ is the engine that drives all subsequent action" (Gemini, AUDIT-WORKING-829314). A candidate Discussion gloss of the existing Sun & Firestone paragraph that makes the dark-room point concrete.
- **Convention-relativity is measurement-theoretic, not merely computational.** Sharpest framing of the convention-dependence caveat: "two analyses computing $\delta_{\text{sat}}$ under different conventions aren't disagreeing; they're measuring different things — closer to how empirical sciences treat measurement protocols than how mathematics treats theorems. AAT is willing to be measurement-theoretic about its own quantities" (Claude, AUDIT-WORKING-471203-batch; same point at Claude, AUDIT-WORKING-584721 — "the diagnostic is meaningful *within* a convention; comparing across conventions is incoherent"). The Epistemic Status already says the convention is part of the measurement; this names *why* that is a substantive stance.

#### 3. Follow-up items

- **The two gaps sum to total shortfall — a candidate clarifying identity.** $\delta_{\text{sat}} + \delta_{\text{regret}} = V_{O_t}^{\min} - V_O(\pi_{\text{current}})$: the satisfaction gap and control regret partition the total distance from the current policy's value to the satisfaction threshold (Claude, AUDIT-WORKING-773921, re-derived independently). Stating this decomposition explicitly would make the orthogonality of the two diagnostics legible at a glance — they are the two additive pieces of the one quantity a single $\delta_{\text{objective}}$ used to conflate. Candidate for the Discussion of either segment.
- **A finite $V_{O_t}^{\min}$ is what makes the diagnostic cascade terminate.** The Working-Notes open question (what counts as "good enough" for utility objectives) connects to a safety-flavored observation: an objective like "maximize profit" with no finite satisfaction threshold makes $\delta_{\text{sat}}$ permanently positive, so the agent "never rests" and keeps expanding $\Pi$ / extending $N_h$ to close an uncloseable gap — read as the structural root of instrumental-convergence dynamics (Gemini, AUDIT-WORKING-193847). The auditor's framing: a bounded satisfaction threshold is what lets the diagnostic cascade reach a stopping state. Strengthens the case for modeling $V_{O_t}^{\min}$ as a first-class part of $O_t$ (already flagged open in Working Notes). *(Aspirational-reach texture — verify before promoting past discussion-grade; the safety claim itself belongs in `04-eli-core/`, below.)*

#### 4. Readers often ask / wonder

- **"Under which convention?" as the first question to ask of any feasibility claim.** The C1/C2/C3 hierarchy is a calibration device: when someone says "the agent can't achieve the goal," the first question should be *under which convention?* — under C1, "can't achieve" means "no one-step improvement visible" (often just a zero local gradient, not impossibility); under C3 it means "genuinely infeasible given the current model and policy class." Conflating them is a common category error in agent evaluation (Claude, AUDIT-WORKING-963715-batch; Claude, AUDIT-WORKING-829314 raised the same as "why C1 gives the most false 'unattainable' diagnoses"). A natural reader question worth pre-empting.
- **How does a bounded agent actually compute the supremum $A_O$?** Finding the optimal policy is NP-hard for complex problems, so the agent cannot compute $A_O$ exactly; in practice it maintains a running lower-bound estimate via heuristic search / deliberation, and $\delta_{\text{sat}}$ is therefore itself an estimate (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201). A concreteness gap a careful reader hits at the supremum.
- **How does an agent expand $\Pi$ when $\Pi$ is set by embodiment?** In the capability-limit cell the prescribed escape includes "expand $\Pi$," but if the policy class is fixed by physical embodiment (a robot arm with three degrees of freedom), expanding $\Pi$ requires modifying the agent's body — pushing the theory from software into hardware/evolution (Gemini, AUDIT-WORKING-193847, raised on the regret sibling but lands here too). A natural edge-question on the disambiguation table.

#### 5. Candidate figures

- **The value-line with a convention side-stack.** Independently proposed: a one-axis value line with the satisfaction threshold $V_{O_t}^{\min}$ and the best-attainable $A_O$ marked, the signed distance between them being $\delta_{\text{sat}}$ — plus a C1/C2/C3 convention stack as a side panel showing how the same objective can read unattainable under C1 and attainable under a stronger convention (Codex/Claude, AUDIT-WORKING-526815). The single-value-ladder version that also shows control regret is in the `def-control-regret` gold; this is its satisfaction-gap-only form.
- **The 2×2 diagnostic cell map** (shared with `#def-control-regret`, where the four cells live) is the cluster's most-converged figure; see the `def-control-regret` and `strategy-structure-intro` gold for the full proposal.

#### Belongs elsewhere

- **ELI / Section IV — a finite satisfaction threshold as the mathematical definition of sanity.** The permanent-dissatisfaction reading ("an objective with $V_{O_t}^{\min} = \infty$ leaves the agent in a desperate, unending attempt to close an uncloseable gap — the root of instrumental convergence; safe consciousness infrastructure must *reject* objectives that lack a finite $V_{O_t}^{\min}$, because without a finite threshold the agent never naturally rests and eventually destabilizes its environment") is aspirational safety-architecture reach pointing at `04-eli-core/`, not at this diagnostic definition (Gemini, AUDIT-WORKING-193847). The in-segment Follow-up above carries the on-topic part (model $V_{O_t}^{\min}$ as first-class); the safety-claim half belongs in the ELI volume's objective-design treatment.
