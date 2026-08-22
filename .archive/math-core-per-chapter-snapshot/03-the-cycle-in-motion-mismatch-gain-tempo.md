# The Cycle in Motion: Mismatch, Gain, & Tempo


## Formulation: Event-Driven Dynamics

- **Slug**: `form-event-driven-dynamics`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: deps-verified
- **Depends**: `post-causal-structure`, `def-observation-function`, `def-action-transition`, `form-agent-model`

The coupling between agent and environment occurs through discrete events — observations arriving and actions completing — at potentially variable and heterogeneous rates. Discrete-time notation is the special case of uniform-interval events on a single channel.

*[Formulation (event-driven-dynamics)]*

**Event** ($e$): An atomic unit of agent-environment interaction, typed as:
- **Observation event**: $e = (\text{obs}, k, o^{(k)})$ — a datum arriving on observation channel $k$
- **Action completion**: $e = (\text{act}, j, r^{(j)})$ — the result of action $j$ completing

**Event stream** ($\mathcal{E}$): The temporally ordered sequence of all events:

$$\mathcal{E} = \{(e_1, \tau_1), (e_2, \tau_2), \ldots\} \quad \text{where } \tau_1 \leq \tau_2 \leq \cdots$$

**Channel rate** ($\nu^{(k)}$): The characteristic event rate of channel $k$, which may vary over time.

**Event information content**: The mutual information between the event and the environment state, conditioned on the current model:

*[Definition (event-information-content)]*

$$\mathcal{I}(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much ($\mathcal{I} \gg 0$). This connects directly to the mismatch signal ( #def-mismatch-signal).

**Channel-specific observation uncertainty**:

*[Definition (channel-uncertainty)]*

$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

Different channels have different noise characteristics. A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. The update gain ( #emp-update-gain) should weight channels accordingly.

---



## Derived: Recursive Update

- **Slug**: `der-recursive-update`
- **Type**: derived
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `form-agent-model`, `form-event-driven-dynamics`, `deriv-recursive-update`

Agent state updates (epistrophe — the corrective turning toward reality) must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full interaction history. For finite agents this is computational necessity; for agents with unlimited computation it is the natural structure imposed by temporal ordering.

*[Derived (recursive-update, from temporal postulate and $M_t$ completeness)]*

**Event-driven update:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

where:
- $M_{\tau^-}$ is the model state immediately before event $e_\tau$
- $M_{\tau^+}$ is the model state immediately after
- $f_M$ is the update function — it takes the current model and the new event, not the full history $\mathcal C_t$

**Between-event evolution:**

$$\frac{dM}{d\tau} = g_M(M_\tau)$$

Between events, the model evolves autonomously — internal reorganization, prediction generation, decay of transient states. The between-event dynamics depend only on the current model state, not on external input (which, by definition, arrives only at events).

---



## Derived: Action Selection

- **Slug**: `der-action-selection`
- **Type**: derived
- **Status**: exact
- **Stage**: deps-verified
- **Depends**: `form-agent-model`, `der-recursive-update`

Praxis (informed action) is a function of the model. The model's role is not merely to represent the environment but to generate actions — either implicitly (from internalized patterns) or through explicit deliberation. The degree to which effective praxis flows from the model without deliberative computation is *action fluency*.

*[Derived (action-selection, from agent-model completeness)]*

Action is a function of the agent's complete internal state. Under Section I scope ( #scope-adaptive-system) — where $M_t$ is the entire internal state — this gives:

$$a_t = \pi(M_t) \quad \text{(deterministic)}$$

$$a_t \sim \pi(\cdot \mid M_t) \quad \text{(stochastic)}$$

where $\pi$ is the agent's **policy** — the mapping from internal state to action.

This is not imposed on the system but follows from #form-agent-model: $M_t$ is defined as the agent's compressed, complete internal record, and action depends on what the agent retains — i.e., on $M_t$. Any deterministic or stochastic dependence of action on history *through* the model is captured by $\pi(M_t)$.

**Section II lift.** When the internal state lifts to $X_t = (M_t, G_t)$ for purposeful agents ( #form-complete-agent-state), the same structural argument gives $a_t = \pi(M_t, G_t)$ — action conditions on the complete internal state, which now includes the purposeful substate. The policy form here is the Section I instantiation $G_t = \emptyset$; the actuated-agent form is recovered by the same completeness argument applied to $X_t$.

---



## Definition: Mismatch Signal

- **Slug**: `def-mismatch-signal`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `form-agent-model`, `def-observation-function`, `def-action-transition`

The discrepancy between the model's prediction and the actual observation — the formal expression of *aporia* (productive perplexity). This is the signal that drives all adaptation: the agent discovers that reality and model have diverged, and this discovery is generative.

*[Definition (mismatch-signal)]*

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a prediction:

$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

The **mismatch signal** (prediction error):

$$\delta_t = o_t - \hat{o}_t$$

This is the primary definition, used in the mismatch dynamics ( #result-persistence-condition, #result-sector-condition-stability) and in the decomposition ( #result-mismatch-decomposition).

For models with probabilistic predictions, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*

$$\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction the model should move to increase the likelihood of the actual observation. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$. Under Gaussian models, they coincide up to scaling.

---



## Result: Mismatch Decomposition

- **Slug**: `result-mismatch-decomposition`
- **Type**: result
- **Status**: exact
- **Stage**: claims-verified
- **Depends**: `def-mismatch-signal`, `def-observation-function`, `def-action-transition`, `form-agent-model`, `scope-adaptive-system`

Expected squared mismatch decomposes into reducible model error and irreducible observation noise. The model can improve the first term; the second is a property of the channel.

*[Derived (result-mismatch-decomposition)]*

For any agent-environment pair within AAT's scope ( #scope-adaptive-system), when observation noise is non-degenerate or the model's predictive mean is misspecified:

$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}} \gt 0$$

where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is the true conditional mean.

### Derivation

1. By #scope-adaptive-system, $H(\Omega_t \mid \mathcal C_t) \gt 0$ — residual uncertainty persists.
2. By #form-agent-model, the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$.
3. Decompose mismatch into model error and noise. The cross-term vanishes by the fresh-noise assumption (GA-1): $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. Condition on $(\Omega_t, a_{t-1}, \mathcal C_{t-1})$; then both $\bar o_t$ and $\hat o_t$ are fixed, and $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}, \mathcal C_{t-1}] = \mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$ and GA-1. The outer expectation gives zero. This is orthogonality (uncorrelated), not independence.
4. Term (ii) is positive when observation noise is non-degenerate. Term (i) is positive when the model's predictive mean differs from the true conditional mean. Either suffices.

---



## Empirical: Update Gain

- **Slug**: `emp-update-gain`
- **Type**: empirical
- **Status**: robust-qualitative
- **Stage**: claims-verified
- **Depends**: `def-mismatch-signal`, `def-observation-function`

The optimal weight an agent assigns to new observations when updating its model — the rate of *epistrophe* (turning toward reality). How much the agent should trust the incoming observation versus its own prior understanding.

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^\ast$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch ( #def-mismatch-signal) and $g(\cdot)$ is a correction mapping from observation space to model update space.

---



## Definition: Causal Information Yield

- **Slug**: `def-causal-information-yield`
- **Type**: definition
- **Status**: exact
- **Stage**: deps-verified
- **Depends**: `der-action-selection`, `def-mismatch-signal`

Actions don't merely select among outcomes — they produce characteristically different outcome distributions depending on the causal structure. Causal information yield (CIY) quantifies the **action-distinguishability** of an action: how different its outcome distribution is from what alternative actions would produce.

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

The $do(\cdot)$ operator is Pearl's standard intervention notation (Pearl 2009, *Causality*, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022); the AAT recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy operationally. $\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Pearl's Level 2 (interventional) from Level 1 (associational) epistemic access.

---



## Definition: Adaptive Tempo

- **Slug**: `def-adaptive-tempo`
- **Type**: definition
- **Status**: exact
- **Stage**: claims-verified
- **Depends**: `emp-update-gain`, `form-event-driven-dynamics`

The effective rate at which an agent acquires useful information from its environment — the product of observation frequency and update quality across all channels.

*[Definition (adaptive-tempo)]*

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where:
- $k$ indexes the agent's distinct observation channels
- $\nu^{(k)}$ is the event rate on channel $k$
- $\eta^{(k)\ast}$ is the optimal update gain on channel $k$ ( #emp-update-gain)

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^\ast$.

### Tensor extension under Fisher-local invariance regime

*[Definition (tensor-adaptive-tempo)]*

Under the Fisher-local invariance regime ( #deriv-fisher-local-update-gain), the optimal update gain on channel $k$ is matrix-valued: $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$, with $H_M = U_M^{-1}$ the prior precision and $H_L^{(k)} = (U_o^{(k)})^{-1}$ the channel-$k$ observed Fisher information. The tensor adaptive tempo is then

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot K^{(k)}$$

— matrix-valued, with per-direction rates given by the eigenvalues of $\sum_k \nu^{(k)} K^{(k)}$ in the appropriate basis. The scalar form $\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ is recovered in the **shared-eigenbasis collapse**: when all $H_M, \{H_L^{(k)}\}$ commute (always in 1-D; under (PI)/Čencov along the natural-gradient direction in higher dimensions), each $K^{(k)}$ acts as the eigenvalue $\eta^{(k)\ast} = U_M/(U_M + U_o^{(k)})$ on the shared natural-gradient direction and the matrix sum collapses to a scalar.

The matrix gain operator $K^{(k)}$ is the per-coordinate primitive: in anisotropic regimes where the prior and likelihoods do not share an eigenbasis (or where different channels pin down different directions), the tensor form preserves the per-direction information that the scalar form averages away.

---



## Hypothesis: Mismatch Dynamics

- **Slug**: `hyp-mismatch-dynamics`
- **Type**: hypothesis
- **Status**: heuristic
- **Stage**: deps-verified
- **Depends**: `def-adaptive-tempo`, `def-mismatch-signal`, `deriv-sector-condition`

The evolution of model-reality mismatch over time is governed by the balance between the agent's corrective capacity (tempo) and the rate of environmental change (disturbance). The linear ODE is a first-order approximation; the general nonlinear case is handled by the sector-condition framework ( #result-sector-condition-stability).

*[Hypothesis (mismatch-dynamics)]*

$$\frac{d\Vert\delta\Vert}{dt} = -\mathcal{T} \cdot \Vert\delta\Vert + \rho(t)$$

where:
- $\mathcal{T} \cdot \Vert\delta\Vert$ is the rate at which the agent corrects mismatch (proportional to both tempo and current mismatch)
- $\rho(t)$ is the **environment change rate** — the rate at which new mismatch is introduced by changes in $\Omega$

**Steady state, Model D (deterministic bounded disturbance, $\lVert w(t)\rVert \leq \rho$):**

Setting $d\lVert\delta\rVert/dt = 0$:

*[Derived (from linear hypothesis, deterministic)]*

$$\lVert\delta\rVert_{ss} = \frac{\rho}{\mathcal{T}}$$

Steady-state mismatch is the ratio of how fast the environment changes to how fast the agent adapts.

**Steady state, Model S (stochastic zero-mean disturbance, $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$):**

*[Derived (from Itô-Lyapunov analysis — see Prop A.1S in #deriv-sector-condition)]*

$$\lVert\delta\rVert_{\text{rms}} = \frac{\sigma_w}{\sqrt{2\mathcal{T}}}$$

(scalar case, $n = 1$; general: $\sigma_w\sqrt{n/(2\mathcal{T})}$). Steady-state mismatch scales as the square root of the disturbance-to-correction ratio, not the ratio itself. The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) means correction is less effective against noise than against drift.

**Transient solution (Model D):**

$$\lVert\delta(t)\rVert = \lVert\delta_0\rVert e^{-\mathcal{T} t} + \frac{\rho}{\mathcal{T}}(1 - e^{-\mathcal{T} t})$$

Mismatch decays exponentially from initial conditions toward the steady state.

---
