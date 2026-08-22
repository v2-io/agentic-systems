# TF-07: Action Selection (Derived)

Action selection — *praxis* in the adaptive loop's vocabulary (TF-00) — is a **function of the model**, not a separate process. The model's role is not merely to represent the environment but to generate actions, either implicitly or through deliberate computation.

**Epistemic status**: The core claim (action is a function of the model) is *derived* from TF-03. The implicit/explicit distinction and action fluency are *discussion* — conceptual properties that follow qualitatively from the formalism but are not formally derived here.

## Action as Model Function

*[Derived]*
$$a_t = \pi(M_t) \quad \text{(deterministic)}$$ *[Derived]*
$$a_t \sim \pi(\cdot \mid M_t) \quad \text{(stochastic)}$$

where $\pi$ is the agent's **policy** — the mapping from model state to action. We use $\pi_M$ when emphasizing that the policy is derived from (or embedded in) the model.

This is not a definition imposed on the system but a consequence of TF-03: the model $M_t$ is the agent's compressed history, and the action is a function of what the agent "knows" — i.e., of $M_t$. Any deterministic or stochastic dependence of action on history *through* the model is captured by $\pi(M_t)$.

## Implicit vs. Explicit Action Selection

A critical distinction emerges from the agent's **action fluency** — the degree to which effective action flows from the model without deliberative computation:

**Implicit (model-embedded):** When the model has internalized effective action-selection for the current situation — when $\pi(M_t)$ can be evaluated cheaply — action flows directly from the model state without deliberate computation. This is:

- Boyd's **implicit guidance and control** (the Orient→Act link, bypassing Decide)
- A trained RL policy in exploitation mode
- A well-tuned PID controller
- Expert intuition (Kahneman's System 1)
- A martial artist's trained reflexes
- An organism's instinctive responses
- An organization's established standard procedures

**Explicit (deliberative):** When the model's action-selection mapping is not internalized for the current situation — because the situation is novel, the action space is large, or the stakes demand verification — the agent engages in **internal simulation**, using the model to predict outcomes of candidate actions before selecting one. This is:

- Boyd's explicit **Decide** step
- Monte Carlo Tree Search / planning in RL
- Model Predictive Control's online optimization
- Human deliberate reasoning (Kahneman's System 2)
- An organization's strategic planning process

Deliberation requires *at minimum* **Level 2 epistemic access** (TF-02) — mental intervention. The agent uses its model to simulate: "what will I observe if I $do(a)$?" across candidate actions, then selects the best. This forward-looking comparison of hypothetical interventions is iterated interventional reasoning: the agent runs the model's causal structure forward under multiple candidate actions and compares the predicted consequences. When the agent additionally reasons retrospectively — "given that I did $a$ and observed $o$, what *would* have happened had I done $a'$ instead?" — it engages Pearl's **Level 3** (counterfactual) access, which is the basis for regret computation, hindsight analysis, and learning from single observations.

In practice, deliberation often involves both levels: comparing candidate actions (Level 2) and evaluating past choices to refine the comparison (Level 3). The computational cost of this simulation — and the mismatch it accumulates during execution (TF-09) — is what distinguishes deliberation from implicit action. When the model has internalized the mapping from situation to action (high action fluency), the interventional comparison has been "pre-computed" through prior experience; when it has not, the agent must perform the comparison explicitly, paying the temporal cost.

### Formal Characterization of Action Fluency

Action fluency can be characterized via the deliberation gain (TF-09): an agent has **high fluency** for a situation when additional deliberation yields negligible improvement — formally, when $\Delta\eta^\ast(\Delta\tau) \approx 0$ for all $\Delta\tau \gt 0$. Conversely, **low fluency** means deliberation significantly improves action quality, indicating that the policy $\pi(M_t)$ has not yet internalized an effective response.

This gives an operational characterization: fluency is the degree to which the agent's immediate (zero-deliberation) action approaches the quality achievable with unbounded deliberation. When fluency is high, the gap between implicit and explicit action vanishes; when low, deliberation is essential.

### Action Fluency vs. Model Sufficiency

Action fluency is distinct from model sufficiency $S(M_t)$ (TF-10). An agent can have high model sufficiency but low action fluency — a chess engine with a perfect model of the rules still requires expensive search to select good moves, because the action space is combinatorially large. Conversely, an agent can have moderate sufficiency but high fluency in a narrow domain — a reflex that responds effectively to the specific situations it evolved for, without representing the environment's full causal structure.

What reflexes, muscle memory, instincts, intuition, trained expertise, and System 1 cognition share is not merely "a cached policy" but that the *action-generating capacity itself* has been absorbed into the model's structure: the model doesn't just *predict* well, it *acts* well, cheaply. The mechanisms by which this absorption occurs vary enormously — evolution (instincts), repetitive training (muscle memory), pattern exposure (intuition), deliberate practice (expertise) — but the result is the same: the computational cost of evaluating $\pi(M_t)$ is low relative to the agent's action timescale.

### The Temporal Advantage of Implicit Action

When two action-selection modes produce equivalent expected outcomes, the faster mode is strictly preferable. This is an instance of the temporal optimality principle (cf. TST T-01: *"For any set of implementations achieving identical outcomes across all non-temporal dimensions, the one requiring least time is optimal"*). Within TFT, TF-09 derives this precisely: deliberation of duration $\Delta\tau$ accumulates mismatch cost $\rho \cdot \Delta\tau$, so any deliberation that does not improve action quality is net-harmful.

This creates a **structural pressure toward implicit action**: agents under selective pressure (biological evolution, market competition, adversarial conflict, training optimization) will tend to internalize frequently-needed action-selection patterns, converting explicit deliberation into implicit fluency. The pressure is stronger when:

- **$\rho$ is high** (fast-changing environments penalize deliberation, per TF-09)
- **The action pattern recurs frequently** (amortizing the cost of internalization)
- **$\mathcal{T}$ is at the persistence threshold** (no slack for deliberation overhead)

However, this is a *tendency under selection pressure*, not an inevitability. Deliberation remains essential — and may even be the primary mode — when:

- **The situation is genuinely novel** (no internalized pattern applies)
- **The action space is large relative to model capacity** (chess, strategic planning)
- **The stakes are asymmetric** (cost of error vastly exceeds cost of delay)
- **$\rho$ is low** (stable environment allows deliberation without mismatch accumulation)

Whether "Decide" is a separate component of the loop therefore depends on context. In high-tempo domains with recurrent patterns, deliberation tends to shrink as the model absorbs effective action patterns. In domains with vast action spaces or rare high-stakes decisions, deliberation may remain a permanent and central feature of the loop.

For the broader exploration-exploitation framework and how actions generate information, see TF-08.

## Domain Instantiations

| Domain | Implicit action | Explicit deliberation |
|--------|----------------|----------------------|
| Kalman + LQR | LQR control law from $\hat x_t$ | — (separation principle) |
| RL | Greedy policy $\arg\max Q(s,a)$ | MCTS, planning, rollouts |
| PID | $u = K_p e + K_i \int e + K_d \dot{e}$ | — (no deliberation) |
| Boyd's OODA | IG&C (Orient→Act) | Explicit Decide step |
| Organism | Reflexes, habits | Deliberate planning |
| Organization | Standard procedures | Strategic planning |
| Science | Apply known theory | Model-based prediction |
| Immune | Innate response | — (no deliberation) |
