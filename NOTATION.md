---
slug: notation
type: reference
---

# AAD Notation and Conventions

All symbols used in Adaptation and Actuation Dynamics, serving as a single authoritative reference. When a symbol appears in any AAD document, its meaning is as defined here unless explicitly noted otherwise.

Notation conventions are adopted from TFT (`_obs/old-tf-00-notation-conventions.md`) with extensions for AAD's purposeful-agent machinery.


## The Adaptive Cycle

One complete traversal of the agent-environment feedback loop — the unit of adaptive work. The five phases are named from Greek philosophical vocabulary; see [`LEXICON.md`](LEXICON.md) for the full prose discussion (why these terms, what they mean beyond the formalism, and what the cycle is *not*).

| Phase | Greek | Formalism |
|-------|-------|-----------|
| **Prolepsis** (πρόληψις) | Anticipation | $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | $o_t$ arrives |
| **Aporia** (ἀπορία) | Perplexity | $\delta_t = o_t - \hat o_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning-toward | $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | $a_t = \pi(M_t)$ |

The cycle is: Prolepsis → Aisthesis → Aporia → Epistrophe → Praxis → (Prolepsis).


## Primitives ( #agent-environment, #observation-function, #action-transition)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\Omega$ | State space | Environment state (unobservable totality) |
| $\Omega_t$ | State | Environment state at time $t$ |
| $\mathcal{O}$ | Set | Observation space |
| $\mathcal{A}$ | Set | Action space |
| $o_t$ | $\in \mathcal{O}$ | Observation at time $t$ |
| $a_t$ | $\in \mathcal{A}$ | Action at time $t$ |
| $h$ | Function | Observation function: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ |
| $T$ | Distribution | Transition: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ |
| $\varepsilon_t$ | Random variable | Observation noise |
| $H(\cdot)$ | Functional | Shannon entropy |
| $I(\cdot; \cdot)$ | Functional | Mutual information |


## Temporal Structure ( #causal-structure, #chronica)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\mathcal C_t$ | Sequence | Interaction history (*chronica*): $(o_1, a_1, \ldots, a_{t-1}, o_t)$ |
| $do(\cdot)$ | Operator | Pearl's intervention operator (Level 2) |
| $\text{CIY}(a)$ | Scalar $\geq 0$ | Causal information yield of action $a$ ( #causal-information-yield) |


## The Model ( #agent-model, #information-bottleneck)

| Symbol | Type | Meaning |
|--------|------|---------|
| $M_t$ | $\in \mathcal{M}$ | Model state (epistemic substate) at time $t$ |
| $\mathcal{M}$ | Set | Model space (the class of representable models) |
| $\phi$ | Function | Compression: $M_t = \phi(\mathcal C_t)$ |
| $f$ | Function | Recursive update: $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ |
| $S(M_t)$ | $\in [0, 1]$ | Model sufficiency ( #model-sufficiency) |
| $\mathcal{F}(\mathcal{M})$ | $\in [0, 1]$ | Model class fitness ( #model-class-fitness) |
| $\beta$ | Scalar $\gt 0$ | Information bottleneck trade-off parameter |


## Event-Driven Dynamics ( #event-driven-dynamics)

| Symbol | Type | Meaning |
|--------|------|---------|
| $e$ | Event | An atomic observation or action-completion event |
| $\tau$ | $\in \mathbb R_{\geq 0}$ | Continuous timestamp of an event |
| $\mathcal{E}$ | Sequence | Event stream: $\{(e_i, \tau_i)\}$ |
| $\nu^{(k)}$ | Rate (Hz) | Event rate on channel $k$ |
| $M_{\tau^-}$, $M_{\tau^+}$ | $\in \mathcal{M}$ | Model state just before / after event at $\tau$ |
| $\mathcal{I}(e_\tau)$ | Scalar $\geq 0$ | Event information content: $I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$ |
| $U_o^{(k)}$ | Scalar $\gt 0$ | Observation uncertainty on channel $k$ |


## Mismatch Signal ( #mismatch-signal)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\hat o_t$ | $\in \mathcal{O}$ | Predicted observation: $\mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| $\delta_t$ | $\in \mathcal{O}$ | Mismatch signal (prediction error): $o_t - \hat o_t$ |
| $\tilde{\delta}_t$ | $\in T_M\mathcal{M}$ | Score-function mismatch: $-\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ |


## Update Gain ( #update-gain)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\eta$ | Scalar, vector, or matrix | Update gain (general) |
| $\eta^\ast$ | Same | Optimal update gain |
| $\eta^{(k)\ast}$ | Same | Optimal gain on channel $k$ |
| $U_M$ | Scalar $\gt 0$ | Model uncertainty: $\text{Var}_{M_{t-1}}[\hat o_t \mid a_{t-1}]$ |
| $U_o$ | Scalar $\gt 0$ | Observation uncertainty: $\text{Var}[\varepsilon_t]$ |
| $g$ | Function | Mismatch transform: maps mismatch to update direction |


## Action Selection ( #action-selection)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\pi$ | Function or distribution | Policy: $a_t = \pi(M_t)$ or $a_t \sim \pi(\cdot \mid M_t)$ |
| $\lambda(M_t)$ | Scalar $\geq 0$ | Exploration-exploitation balance weight ( #causal-information-yield) |


## Adaptive Tempo and Dynamics ( #adaptive-tempo, #mismatch-dynamics)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\mathcal{T}$ | Rate ($t^{-1}$) | Adaptive tempo (epistemic): $\sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ |
| $\mathcal{T}_\Sigma$ | Rate ($t^{-1}$) | Strategic tempo: $\sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij}$ ( #strategic-tempo) |
| $\rho(t)$ | Rate (surprise/time) | Environment change rate (mismatch injection rate) |
| $\rho_\Sigma$ | Rate | Strategic disturbance rate (rate of causal-link invalidation) |
| $\lVert\delta\rVert_{ss}$ | Scalar $\geq 0$ | Steady-state mismatch: $\rho / \mathcal{T}$ (linear approximation) |


## Lyapunov / Sector-Condition Analysis ( #sector-condition-stability)

| Symbol | Type | Meaning |
|--------|------|---------|
| $F(\mathcal{T}, \delta)$ | Function | Correction function (general nonlinear) |
| $w(t)$ | Vector | Disturbance (new mismatch), $\lVert w(t)\rVert \leq \rho$ |
| $\alpha$ | Scalar $\gt 0$ | Lower sector bound of correction function |
| $R$ | Scalar $\gt 0$ | Radius of sector-condition region (model class capacity) |
| $R^\ast$ | Scalar $\gt 0$ | Ultimately bounded mismatch radius: $\rho/\alpha$ |
| $\Delta\rho^\ast$ | Scalar $\geq 0$ | Adaptive reserve: $\alpha R - \rho$ |
| $\gamma_A$ | Scalar $\gt 0$ | Coupling effectiveness of $A$'s actions on $B$'s disturbance |
| $V(\delta)$ | Scalar $\geq 0$ | Lyapunov function: $\frac{1}{2}\lVert\delta\rVert^2$ |


## Deliberation ( #deliberation-cost)

| Symbol | Type | Meaning |
|--------|------|---------|
| $\Delta\tau$ | Duration $\geq 0$ | Deliberation duration |
| $\Delta\eta^\ast(\Delta\tau)$ | Scalar $\geq 0$ | Gain improvement from deliberation |
| $\rho_{\text{delib}}$ | Rate | Local mismatch drift rate during deliberation pauses |


## Purposeful Agent State (Section II)

| Symbol | Type | Meaning |
|--------|------|---------|
| $X_t$ | State | Complete agent state: $(M_t, G_t)$ |
| $G_t$ | State | Purposeful substate: $(O_t, \Sigma_t)$ |
| $O_t$ | Objective | What the agent wants — induces value functional $V_{O_t}$ |
| $\Sigma_t$ | Strategy | How the agent plans to get it — a probabilistic causal DAG |
| $V_O(M_t, \pi; N_h)$ | Scalar | Value object: horizon- and policy-conditioned |
| $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ | Scalar | Action-value object |
| $\delta_{\text{sat}}$ | Scalar | Satisfaction gap: $V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$ |
| $\delta_{\text{regret}}$ | Scalar $\geq 0$ | Control regret: $A_O - V_O(\pi_{\text{current}})$ |
| $\delta_{\text{strategic}}$ | Scalar $\geq 0$ | Strategic calibration: edge residual aggregate |
| $p_{ij}$ | $\in [0, 1]$ | Edge confidence weight in strategy DAG |
| $\gamma(v)$ | $\in \{\text{AND}, \text{OR}\}$ | Node combination rule in strategy DAG |


## Multi-Agent (Section III)

| Symbol | Type | Meaning |
|--------|------|---------|
| $U_M$ | Scalar $\in [-1, 1]$ | Epistemic unity (shared model) |
| $U_O$ | Scalar $\in [-1, 1]$ | Teleological unity (shared objective) |
| $U_\Sigma$ | Scalar $\in [-1, 1]$ | Strategic unity (coordinated action) |
| $\eta_{ji}^\ast$ | Scalar | Communication gain: $U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$ |
| $C_{\text{coord}}$ | Rate ($t^{-1}$) | Coordination overhead (tempo-equivalent) |


## Conventions

**Subscript $t$**: Discrete time index or macroscopic continuous time. Context disambiguates: $M_t = f(M_{t-1}, o_t, a_{t-1})$ is discrete; $d\lVert\delta\rVert/dt$ is continuous.

**Subscript $\tau$**: Continuous timestamp of an individual event. Used in the event-driven formulation for microscopic update dynamics.

**Superscript $(k)$**: Channel index. Distinguishes observation or action channels with distinct rates and noise.

**Calligraphic letters** ($\mathcal{M}$, $\mathcal{O}$, $\mathcal{A}$, $\mathcal{E}$, $\mathcal{C}$, $\mathcal{T}$, $\mathcal{I}$): Sets, spaces, or aggregate quantities. $\mathcal{C}$ for chronica (not $\mathcal{H}$, to avoid collision with entropy). Exceptions: $\mathcal{T}$ is a scalar rate (calligraphic distinguishes from temperature); $\mathcal{I}(e_\tau)$ is a scalar (distinguishes from mutual information $I$).

**$\lVert\cdot\rVert$**: Norm (Euclidean or information-theoretic). Used for mismatch magnitude.

**$\lvert\cdot\rvert$**: Cardinality of a set (e.g., $\lvert\mathcal{A}\rvert$). Not for mismatch — use $\lVert\cdot\rVert$.

**Scalar reduction of gain and tempo.** When $\eta^\ast$ appears as scalar in mismatch dynamics, it represents the effective correction fraction along the current mismatch direction: $\eta^\ast_{\text{eff}} = \delta^T K \delta / \lVert\delta\rVert^2$. Scalar tempo $\mathcal{T} = \nu \cdot \eta^\ast_{\text{eff}}$ is the correction rate along this direction. The sector condition parameter $\alpha$ corresponds to the worst-case scalar projection. The full anisotropic treatment requires a tempo tensor; the scalar reduction is valid when correction dynamics are approximately isotropic.


## Units

The theory uses natural (dimensionless information-theoretic) units where possible:

| Quantity | Units | Notes |
|----------|-------|-------|
| $\eta^\ast$ | Dimensionless $\in [0, 1]$ | Ratio |
| $\nu^{(k)}$ | Events per unit time (Hz) | |
| $\mathcal{T}$ | Inverse time ($t^{-1}$) | Effective correction rate |
| $\rho$ | Surprise $\cdot t^{-1}$ | Mismatch injection rate |
| $S(M_t)$ | Dimensionless $\in [0, 1]$ | Ratio |

**Dimensional analysis of the mismatch ODE.** In $d\lVert\delta\rVert/dt = -\mathcal{T}\lVert\delta\rVert + \rho$: LHS has units [surprise $\cdot t^{-1}$]; $\mathcal{T}\lVert\delta\rVert$ has $[t^{-1}] \cdot [\text{surprise}]$; $\rho$ has [surprise $\cdot t^{-1}$]. All consistent. Note $\mathcal{T}$ and $\rho$ have different units — the persistence condition $\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ is dimensionally consistent. The shorthand "$\mathcal{T} \gt \rho$" is valid only when $\lVert\delta_{\text{critical}}\rVert$ is normalized to 1.


## Global Assumptions

Load-bearing assumptions that appear locally but are referenced by multiple results:

| ID | Assumption | Used by |
|----|-----------|---------|
| GA-1 | **Fresh noise.** $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. | #mismatch-decomposition |
| GA-2 | **Bounded disturbance (Model D).** $\lVert w(t)\rVert \leq \rho$ for finite $\rho$. Deterministic worst-case bound; no distributional assumption. | #sector-condition-stability, #persistence-condition |
| GA-2S | **Stochastic disturbance (Model S).** $w(t)$ is zero-mean with $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$. Alternative to GA-2 for environments with noise rather than drift. | #sector-condition-stability (Prop A.1S), #persistence-condition, #adversarial-exponent-regimes |
| GA-3 | **Sector condition (continuous).** $\delta^T F(\mathcal{T}, \delta) \geq \alpha\lVert\delta\rVert^2$ for $\lVert\delta\rVert \leq R$. Derived from the gain principle when the update rule has directional fidelity (B1); for gradient-based agents, equivalent to local strong convexity of the loss. Remains an independent assumption for non-gradient agents. The discrete-time analog (DA2') adds a Lipschitz upper bound $\lVert F_d(\delta)\rVert \leq c_{\max}\lVert\delta\rVert$ — strictly stronger than an inner-product upper bound, required because the discrete contraction involves $\lVert F_d\rVert^2$. See #gain-sector-bridge, #discrete-sector-condition. | #sector-condition-stability, #discrete-sector-condition |
| GA-4 | **Local deliberation drift.** Mismatch accumulates at rate $\rho_{\text{delib}}$ during inaction. | #deliberation-cost |
| GA-5 | **Fluid limit.** Event rate high relative to dynamics timescale ($\eta^\ast \ll 1$). | #mismatch-dynamics |
