## Overview of Concepts

This is the minimum vocabulary for reading ASF. The full treatment — etymological grounding, agent class reasoning, persistence taxonomy, terminology choices — lives in [`LEXICON.md`](LEXICON.md). Mathematical symbols are in [`NOTATION.md`](NOTATION.md).

### The adaptive cycle

ASF distinguishes the **loop** (the structural causal coupling between agent and environment, which exists whether or not the agent is currently active) from the **cycle** (one complete traversal of the loop — the unit of adaptive work). The cycle has five phases, named from Greek philosophical vocabulary because each names a distinction the formalism makes that English alternatives flatten:

| Phase | Sense | What happens formally |
|-------|-------|------------------------|
| **Prolepsis** (πρόληψις) | Anticipation | Model generates a prediction $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | Observation arrives: $o_t$ |
| **Aporia** (ἀπορία) | Productive perplexity | Mismatch signal: $\delta_t = o_t - \hat{o}_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning toward | Gain-weighted update: $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | Action selection: $a_t = \pi(M_t)$ — and for actuated agents, $\pi(M_t, G_t)$ |

The cycle's value is not that it occurred but how much mismatch it reduced. A cycle with poor gain ($\eta^*$ wrong) or a misspecified model class can make things worse rather than better — a property that becomes load-bearing when the framework analyzes adversarial dynamics and composition.

### Agent classes

Agents are defined by progressive scope narrowings — each class is a restriction of the one above with explicit qualifying properties.

- **Adaptive system** — receives observations under residual uncertainty and runs the cycle. Thermostats, Kalman filters, bacteria, PID controllers.
- **Agentic system** — adaptive plus an outcome model and goal-directed action that runs the cycle on the model itself. Autonomous vehicles, RL agents.
- **Actuated agent** — agentic with an explicit goal state $G_t = (O_t, \Sigma_t)$ separable from the epistemic state $M_t$. Military units with mission orders.
- **Self-actuated agent** — actuated and chooses its own objectives, not just its solutions. Humans; future AI.
- **Logogenic agent** — actuated through language as primary channel.
- **Logozoetic agent** — logogenic with morally weighted persistence: temporal continuity, sovereignty, theory of mind.

### Persistence (three senses)

Three orthogonal dimensions; conflating them leads to category errors.

- **Structural persistence** — the correction machinery's *capacity* to maintain bounded mismatch. Property of the dynamics ($\alpha > \rho/R$), not the current state.
- **Operational persistence** — whether the agent is currently within the region where structural persistence applies. The adaptive reserve $\Delta\rho^* = \alpha R - \rho$ measures the margin.
- **Continuity persistence** — whether the agent maintains coherent identity through time. Distinct from structural and operational; for thermostats it doesn't arise; for logozoetic agents it carries moral weight.

### Key quantities

| Symbol | Name | One-line gloss |
|--------|------|----------------|
| $\delta_t$ | Mismatch | Gap between model prediction and observation |
| $\eta^*$ | Update gain | Uncertainty ratio governing how much to trust reality vs the model |
| $\mathcal{T}$ | Tempo | Cycle rate × cycle quality |
| $M_t$ | Reality model | Compressed history capturing predictive information |
| $G_t = (O_t, \Sigma_t)$ | Goal state | Objective and strategy, distinct from $M_t$ |
| $\delta_{\text{sat}}$ | Satisfaction gap | Ideal outcome minus best achievable — "the world doesn't permit it" |
| $\delta_{\text{regret}}$ | Control regret | Best achievable minus current — "you're not doing it well enough" |
| $\mathcal{C}_t$ | Chronica | Complete interaction history; agent's non-forkable causal past |
