# TF-03: The Model (Formulation)

Any persisting agent maintains a **model** — a compressed representation of its interaction history that supports prediction and action selection.

## Definitions

**Interaction History** ($\mathcal C_t$, *chronica*): The complete, singular causal record of the agent's observations and actions:

*[Definition]*
$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

This is the agent's *only* raw material. Everything the agent "knows" must be constructed from this.

**Model** ($M_t$): A compression of the interaction history:

*[Definition]*
$$M_t = \phi(\mathcal{C}_t)$$

where $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps histories to elements of a **model space** $\mathcal{M}$.

**Model Space** ($\mathcal{M}$): The set of representable models. This is a structural choice that constrains what the agent can represent:

| Model Space $\mathcal{M}$ | Instance |
|----------------------------|----------|
| $\mathbb{R}^n \times \mathbb{S}^n_{++}$ (vector + covariance) | Kalman filter |
| $\Delta(\Theta)$ (distributions over parameters) | Bayesian agent |
| $\{Q: \mathcal{S} \times \mathcal{A} \to \mathbb{R}\}$ (value functions) | RL agent |
| Neural network weight space | Deep learning agent |
| $\mathbb{R}^3$ (error, integral, derivative) | PID controller |
| (Procedures, beliefs, culture) | Organization |
| Antibody repertoire + memory cells | Immune system |

## The Recursive Update

The model updates recursively as a consequence of the causal structure (TF-02):

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

The arrow of time, partial observability, and state completeness jointly determine this as the unique causal-respecting update form. See TF-02 for the derivation and TF-04 for the multi-channel event framework. The function $f$ is the **update function** — the mechanism by which new information is incorporated into the model. Its properties are the subject of TF-05 and TF-06.

## Model Quality as Compression Efficiency

The model faces a fundamental trade-off formalized by the **information bottleneck**[^tishby2000]:

*[Formulation (IB-objective)]*
$$\phi^* = \arg\min_{\phi} \left[ I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

- $I(M_t; \mathcal C_t)$ measures **compression cost** — how much of the history the model retains
- $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ measures **predictive power** — how much the model can predict
- $\beta$ controls the trade-off: higher $\beta$ favors prediction; lower favors compression

Varying $\beta$ traces a Pareto frontier of optimal models. This IS the rate-distortion curve for the agent's epistemic problem.

A PID controller's model ($\mathbb{R}^3$) is an aggressively compressed point on this curve — it retains almost nothing of the history but preserves enough for effective control of simple dynamics. A Bayesian posterior retains much more. Neither is universally superior; the optimal point depends on $\mathcal{M}$, the environment's complexity, and the agent's computational constraints.

**Connection to environmental volatility.** The optimal $\beta$ is not static — it depends on the environment's rate of change $\rho$ (TF-11). In highly volatile environments (high $\rho$), the predictive value of historical detail decays rapidly: detailed memories of past dynamics become stale as the environment shifts. The optimal $\beta$ is therefore *lower* — the agent should compress aggressively, retaining only the most robust predictive structure, because (a) historical detail has diminishing predictive shelf-life, and (b) complex models with many parameters have lower effective $\eta^\ast$ per parameter (TF-06), reducing adaptive tempo $\mathcal{T}$. In stable environments (low $\rho$), $\beta$ can be higher: the agent has the luxury of retaining dense historical specificities for nuanced, high-fidelity predictions. This connects TF-03's representation choice to TF-11's persistence condition: an agent that retains too much history in a volatile environment pays twice — once in computational cost, and once in reduced $\mathcal{T}$ that may fall below the persistence threshold.

## Model Adequacy

A model is **adequate** to the degree that it is a sufficient statistic[^fisher1922] for the history with respect to future prediction. The formal measure of adequacy — **model sufficiency** $S(M_t)$ — and the related concept of **model class fitness** $\mathcal{F}(\mathcal{M})$ are introduced in TF-10, where they become load-bearing for the structural adaptation necessity result (Proposition 10.1).

The key intuition: when the model captures everything predictively relevant in the history, knowing the full history $\mathcal C_t$ in addition to $M_t$ provides no further predictive power. Perfect sufficiency ($S = 1$) is an ideal. Real models are approximately sufficient, and the degree of approximation determines both the quality of the recursive update and the agent's susceptibility to structural inadequacy.

## Why This Is a Formulation

This document is labeled "Formulation" rather than "Axiom" because it makes a specific modeling choice: we analyze adaptive systems as maintaining compressed predictive representations. This is a representational definition, not a psychological or metaphysical claim — "model" includes any internal state that induces non-random action-history dependence, from a thermostat's bimetallic strip to a Bayesian posterior.

The framing is deliberately broad. An agent whose actions are non-random with respect to outcomes is, by definition, using some function of its history — i.e., a model, however implicit. This makes the formulation nearly tautological within the theory's scope, which is by design: TFT does not claim that all systems "have models" in any deep sense, but rather that analyzing them as maintaining compressed representations is productive when the formal apparatus (sufficiency, information bottleneck, model class fitness) can be meaningfully applied.

The model may be explicit (a Kalman state vector, a Bayesian posterior) or implicit (a subsumption architecture's wiring, a PID controller's three-number state, an organization's culture). The formulation claims only that it *exists*, not that it takes any particular form. The theory's content comes not from this existence claim but from the specific mathematical framework applied to it.

---

[^fisher1922]: Fisher, R. A. (1922). "On the mathematical foundations of theoretical statistics." *Phil. Trans. Royal Society A*, 222, 309–368.
[^tishby2000]: Tishby, N., Pereira, F. C., & Bialek, W. (2000). "The information bottleneck method." *arXiv:physics/0004057*.
