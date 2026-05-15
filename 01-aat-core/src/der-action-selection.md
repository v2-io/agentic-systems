---
slug: der-action-selection
type: derived
status: exact
depends:
  - form-agent-model
  - der-recursive-update
stage: deps-verified
---

# Derived: Action Selection

Praxis (informed action) is a function of the model. The model's role is not merely to represent the environment but to generate actions — either implicitly (from internalized patterns) or through explicit deliberation. The degree to which effective praxis flows from the model without deliberative computation is *action fluency*.

## Formal Expression

*[Derived (action-selection, from agent-model completeness)]*

Action is a function of the agent's complete internal state. Under Section I scope ( #scope-adaptive-system) — where $M_t$ is the entire internal state — this gives:

$$a_t = \pi(M_t) \quad \text{(deterministic)}$$

$$a_t \sim \pi(\cdot \mid M_t) \quad \text{(stochastic)}$$

where $\pi$ is the agent's **policy** — the mapping from internal state to action.

This is not imposed on the system but follows from #form-agent-model: $M_t$ is defined as the agent's compressed, complete internal record, and action depends on what the agent retains — i.e., on $M_t$. Any deterministic or stochastic dependence of action on history *through* the model is captured by $\pi(M_t)$.

**Section II lift.** When the internal state lifts to $X_t = (M_t, G_t)$ for purposeful agents ( #form-complete-agent-state), the same structural argument gives $a_t = \pi(M_t, G_t)$ — action conditions on the complete internal state, which now includes the purposeful substate. The policy form here is the Section I instantiation $G_t = \emptyset$; the actuated-agent form is recovered by the same completeness argument applied to $X_t$.

## Epistemic Status

*Exact* within Section I scope. The derivation follows from #form-agent-model's completeness commitment: if $M_t$ is the agent's complete internal state (by definition), then action — which depends on internal state — is a function of $M_t$. The Section II generalization $a_t = \pi(M_t, G_t)$ is exact within Section II scope by the same argument applied to the lifted state $X_t$ ( #form-complete-agent-state); see #def-model-sufficiency for the form already in use downstream. The implicit/explicit distinction and action fluency concept are *discussion-grade* — qualitative properties that follow from the formalism but are not formally derived as propositions.

## Discussion

**Implicit vs. explicit action selection.** A critical distinction emerges from the agent's *action fluency* — the degree to which effective action flows from the model without deliberative computation:

**Implicit (model-embedded):** When $\pi(M_t)$ can be evaluated cheaply — the model has internalized effective action-selection for the current situation. This is Boyd's implicit guidance and control (Orient→Act, bypassing Decide), a trained RL policy in exploitation mode, a well-tuned PID controller, expert intuition (System 1), a martial artist's trained reflexes, an organization's standard operating procedures.

**Explicit (deliberative):** When the situation is novel, the action space is large, or the stakes demand verification — the agent engages in internal simulation, using the model to predict outcomes of candidate actions before selecting. This is Boyd's explicit Decide step, MCTS/planning in RL, Model Predictive Control, human deliberate reasoning (System 2), organizational strategic planning. Deliberation requires at minimum Level 2 epistemic access ( #def-pearl-causal-hierarchy) — the agent uses its model to simulate "what will I observe if I $do(a)$?" across candidates.

**Formal characterization of action fluency.** An agent has *high fluency* for a situation when additional deliberation yields negligible improvement — formally, when $\Delta\eta^\ast(\Delta\tau) \approx 0$ for all $\Delta\tau \gt 0$ (see #der-deliberation-cost). Conversely, *low fluency* means deliberation significantly improves action quality. Fluency is the degree to which the agent's immediate (zero-deliberation) action approaches the quality achievable with unbounded deliberation.

**Action fluency is distinct from model sufficiency.** An agent can have high $S(M_t)$ ( #def-model-sufficiency) but low fluency — a chess engine with a perfect model of the rules still requires expensive search. Conversely, an agent can have moderate sufficiency but high fluency in a narrow domain — a reflex that responds effectively to specific situations it evolved for. What reflexes, muscle memory, intuition, and expertise share is that the *action-generating capacity itself* has been absorbed into the model's structure: the model doesn't just predict well, it *acts* well, cheaply.

**Structural pressure toward implicit action.** When two action-selection modes produce equivalent expected outcomes, the faster mode is preferable (the persistence condition penalizes slower tempo — and in TST, the temporal optimality postulate makes this normative). This creates a pressure: agents under selective pressure (evolution, competition, training) tend to internalize frequently-needed action patterns, converting explicit deliberation into implicit fluency. The pressure is stronger when $\rho$ is high (fast-changing environments penalize deliberation — see #der-deliberation-cost), the pattern recurs frequently, or $\mathcal{T}$ is near the persistence threshold ( #result-persistence-condition) with no slack for deliberation overhead.

However, deliberation remains essential when the situation is genuinely novel, the action space is large relative to model capacity (chess, strategic planning), the stakes are asymmetric (cost of error vastly exceeds cost of delay), or $\rho$ is low (stable environment allows deliberation without mismatch accumulation).

**Connection to Section II.** For actuated agents ( #def-agent-spectrum), the lifted form $\pi(M_t, G_t)$ above unpacks: action conditions on the purposeful substate $G_t = (O_t, \Sigma_t)$ as well as on $M_t$, coupling all substates through action ( #der-directed-separation). The action-deliberation-exploration tradeoff (Section II gap) extends the implicit/explicit distinction to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$).

**Domain instantiations:**

| Domain | Implicit action | Explicit deliberation |
|--------|----------------|----------------------|
| Kalman + LQR | LQR control law from $\hat{x}_t$ | — (separation principle) |
| RL | Greedy policy $\arg\max Q(s,a)$ | MCTS, planning, rollouts |
| PID | $u = K_p e + K_i \int e + K_d \dot{e}$ | — (no deliberation) |
| Boyd's OODA | IG&C (Orient→Act) | Explicit Decide step |
| Organism | Reflexes, habits | Deliberate planning |
| Organization | Standard procedures | Strategic planning |
| Software developer | Known patterns, familiar code | Reading docs, analyzing alternatives |
