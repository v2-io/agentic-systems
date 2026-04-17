# Spike: Projection Admissibility ($\mathcal P_{\text{adm}}$)

**Status**: Exploratory derivation
**Date**: 2026-04-01
**Motivation**: The composition-closure criterion defines $\varepsilon^\ast$ as an infimum over admissible projections ($\mathcal P_{\text{adm}}$) and admissible macro-dynamics ($\mathcal M_{\text{adm}}$). The macro-dynamics admissibility is specified (A1-A4 in #composition-closure). The projection admissibility is NOT specified. This means $\varepsilon^\ast$ is currently an infimum over an undefined set, and all quantitative composition results concern an undefined object.

This spike proposes a concrete specification for $\mathcal P_{\text{adm}}$, instantiates it for the simplest nontrivial case (two Kalman filters), specifies the load-bearing norm choices, and assesses whether projection admissibility can be derived from (A1)-(A4) or is genuinely independent.

**Depends on**: #composition-closure, #multi-agent-scope, #sector-condition-derivation, `msc/spike-composition-bridge-2agent.md`, `msc/working-composition-admissibility.md`

---

## 1. The Problem

The closure defect is:

$$\varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert$$

$\mathcal M_{\text{adm}}$ is the class of macro-dynamics satisfying (A1)-(A4): AAD agent structure, well-defined mismatch, well-defined tempo, bounded macro-correction (sector condition). This prevents the infimum from being trivially zero.

$\mathcal P_{\text{adm}}$ is the class of admissible projections $\Lambda = (\Lambda_x, \Lambda_o, \Lambda_a, \Lambda_\Omega)$. Without constraints:
- If $\mathcal P_{\text{adm}}$ is too broad, the infimum can be driven to zero by degenerate projections (e.g., $\Lambda_x = \text{const}$, which maps every micro-state to the same macro-state -- trivially zero $\varepsilon_x$ but useless).
- If $\mathcal P_{\text{adm}}$ is too narrow, interesting composites are excluded.

The question: what makes a projection admissible?

### 1.1 What a projection must do

$\Lambda$ maps the micro-system to a macro-system. A useful projection must:

1. **Preserve enough predictive structure** that the macro-state is informative about macro-observations and macro-actions (otherwise the macro-agent is blind or impotent).
2. **Be regular enough** that bounded micro-errors don't explode into unbounded macro-errors (otherwise the bridge lemma fails).
3. **Actually reduce dimensionality** (otherwise the "macro-agent" is just the full micro-system relabeled, which is trivially admissible but not a genuine abstraction).

These correspond to three candidate constraints: information preservation, Lipschitz regularity, and dimensionality reduction.

---

## 2. Two Candidate Approaches

### 2.1 Approach I: Information-Preservation Admissibility

The projection must retain sufficient predictive mutual information. The macro-state must be able to predict macro-observations at least as well as the micro-state predicts micro-observations, up to a controlled loss.

*[Formulation (information-preservation-admissibility)]*

A projection $\Lambda$ is information-admissible at level $\epsilon_I$ if:

$$I\big(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\big) \geq (1 - \epsilon_I) \cdot I\big(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\big)$$

The left side is the predictive mutual information the macro-state has about next macro-observations, conditioned on the macro-action. The right side is the same quantity at the micro level. The ratio $(1 - \epsilon_I)$ controls how much predictive power may be sacrificed by projection.

**Interpretation.** This is the information bottleneck (IB) applied to the projection. The IB framework (Tishby et al. 1999) characterizes optimal compressions that preserve relevance while discarding irrelevant detail. Here, "relevance" is predictive -- the macro-state must predict the macro-observation stream.

**Strengths:**
- Principled: directly controls the predictive capability of the macro-agent.
- Domain-agnostic: mutual information is well-defined for any probability space.
- Connected to existing AAD machinery: the information bottleneck framework (#information-bottleneck) already formalizes model compression; this extends it to the projection.
- The parameter $\epsilon_I$ is interpretable: the fraction of predictive information lost to projection.

**Weaknesses:**
- Requires knowing the joint distribution $P(X_{\text{micro},t}, o_{\text{micro},t+1}, a_{\text{micro},t})$ -- hard or impossible to compute in general.
- Does not guarantee AAD structure at the macro level. A neural network encoder could satisfy this condition without producing a decomposed $(M_c, G_c)$ state. (But this is handled by $\mathcal M_{\text{adm}}$, which constrains the macro-dynamics to be AAD-shaped.)
- Does not guarantee regularity (Lipschitz continuity) of the projection.

### 2.2 Approach II: Lipschitz Admissibility

The projection must be Lipschitz continuous, bounding how much micro-errors are amplified by the projection.

*[Formulation (lipschitz-admissibility)]*

A projection $\Lambda$ is Lipschitz-admissible at level $L$ if:

$$\lVert \Lambda_x(X) - \Lambda_x(X') \rVert_{\mathcal X_c} \leq L \cdot \lVert X - X' \rVert_{\mathcal X_{\text{micro}}} \quad \forall\, X, X' \in \mathcal X_{\text{micro}}$$

and analogously for $\Lambda_o$, $\Lambda_a$, $\Lambda_\Omega$, each with its own Lipschitz constant $L_o$, $L_a$, $L_\Omega$.

**Interpretation.** Nearby micro-states map to nearby macro-states. The bridge lemma in #composition-closure already implicitly assumes this -- the Lipschitz constant determines how projection amplifies the trajectory error.

**Strengths:**
- The bridge lemma requires it (or something equivalent). Without Lipschitz regularity, bounded closure defect does NOT imply bounded trajectory error -- small micro-perturbations can cause large macro-jumps through discontinuous projection.
- Computationally tractable: Lipschitz constants can be verified for specific projection operators (linear projections, weighted averages, SVD truncation).
- The constant $L$ has a direct role in the trajectory error bound: the bridge lemma gives $\lVert e_t \rVert \leq L \cdot \varepsilon^\ast / \alpha_c$ when the projection is $L$-Lipschitz.

**Weaknesses:**
- Does not guarantee the projection retains useful information. A constant map $\Lambda_x(X) = c$ is 0-Lipschitz but useless.
- Lipschitz continuity is a regularity condition, not a content condition. It prevents pathological projections but doesn't ensure good ones.

### 2.3 Assessment: Which is primary?

Neither alone is sufficient. Together they are complementary:

| Property | Information-preservation | Lipschitz |
|----------|------------------------|-----------|
| Prevents trivial/degenerate projections | Yes ($\Lambda = \text{const}$ has zero mutual information) | No ($\Lambda = \text{const}$ is Lipschitz) |
| Prevents pathological amplification | No | Yes |
| Required by bridge lemma | No (but implied by tractability) | Yes (directly) |
| Computationally tractable | Hard (general case) | Easier (specific cases) |
| Domain-agnostic | Yes | Yes |

**Recommendation.** Define $\mathcal P_{\text{adm}}$ as the intersection: projections that are both information-preserving and Lipschitz-continuous. The information condition prevents degenerate projections; the Lipschitz condition prevents pathological projections. The formal definition:

*[Definition (projection-admissibility)]*

$$\mathcal P_{\text{adm}}(\epsilon_I, L) = \left\{ \Lambda : \begin{array}{l} \text{(P1) Information preservation at level } \epsilon_I \\ \text{(P2) Lipschitz continuity at level } L \\ \text{(P3) Dimensionality reduction: } \dim(\mathcal X_c) \lt \dim(\mathcal X_{\text{micro}}) \end{array} \right\}$$

where:

**(P1) Information preservation.** The predictive mutual information condition from Approach I:

$$I\big(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\big) \geq (1 - \epsilon_I) \cdot I\big(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\big)$$

**(P2) Lipschitz continuity.** Each component of $\Lambda$ is Lipschitz:

$$\lVert \Lambda_x(X) - \Lambda_x(X') \rVert \leq L \cdot \lVert X - X' \rVert \quad \forall\, X, X'$$

(and analogously for $\Lambda_o, \Lambda_a, \Lambda_\Omega$, each with its own constant).

**(P3) Dimensionality reduction.** The macro-state space has strictly lower dimension than the micro-state space. This prevents the trivial "keep everything" projection, which has $\varepsilon^\ast = 0$ but is not a genuine abstraction. Without this, the infimum is always zero (achieved by the identity projection).

### 2.4 The $\epsilon_I$ and $L$ parameters

The admissible class is parameterized by $(\epsilon_I, L)$. These are part of the problem specification, not derived quantities:

- $\epsilon_I$ controls the quality-of-abstraction floor: how much predictive power the projection is allowed to sacrifice. Setting $\epsilon_I = 0$ requires lossless prediction (very restrictive); $\epsilon_I = 0.5$ allows discarding half the predictive information (very permissive).
- $L$ controls the regularity floor: how much amplification the projection is allowed. Setting $L = 1$ means the projection is non-expansive; $L \gt 1$ allows amplification.

The closure defect $\varepsilon^\ast$ depends on $(\epsilon_I, L)$: larger $\epsilon_I$ and $L$ enlarge $\mathcal P_{\text{adm}}$, potentially lowering $\varepsilon^\ast$ (more projections to search over). But the trajectory error bound $\varepsilon^\ast L / \alpha_c$ may increase because $L$ amplifies.

The natural choice for many applications: $L = 1$ (non-expansive projection, no amplification of micro-errors) and $\epsilon_I$ chosen to be the minimum information loss compatible with genuine dimensionality reduction.

---

## 3. Instantiation: Two Kalman Filters Tracking Correlated Processes

### 3.1 Setup

Two agents, each a Kalman filter, tracking correlated scalar processes.

**Environment.** Two correlated random walks:

$$\begin{pmatrix} \omega_{1,t+1} \\ \omega_{2,t+1} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \omega_{1,t} \\ \omega_{2,t} \end{pmatrix} + \begin{pmatrix} w_{1,t} \\ w_{2,t} \end{pmatrix}$$

where the process noise has covariance:

$$Q = \begin{pmatrix} q_1 & q_{12} \\ q_{12} & q_2 \end{pmatrix}, \quad q_{12} = \rho_{\text{corr}} \sqrt{q_1 q_2}$$

Here $\rho_{\text{corr}} \in [-1, 1]$ is the correlation between the two processes.

**Agent 1** observes $\omega_{1,t}$ with noise variance $r_1$:

$$o_{1,t} = \omega_{1,t} + v_{1,t}, \quad v_{1,t} \sim N(0, r_1)$$

**Agent 2** observes $\omega_{2,t}$ with noise variance $r_2$:

$$o_{2,t} = \omega_{2,t} + v_{2,t}, \quad v_{2,t} \sim N(0, r_2)$$

Each agent runs an independent Kalman filter (no communication). Agent $i$'s state is its posterior: $M_{i,t} = (\hat\omega_{i,t}, P_{i,t})$ where $\hat\omega_{i,t}$ is the state estimate and $P_{i,t}$ is the error variance.

### 3.2 The micro-system

The micro-state is the pair of Kalman filter states:

$$X_{\text{micro},t} = \big((\hat\omega_{1,t}, P_{1,t}),\; (\hat\omega_{2,t}, P_{2,t})\big)$$

Micro-state dimension: 4 (two means, two variances).

Each filter converges to steady-state variance $P_i^\ast$ (the positive root of the discrete algebraic Riccati equation):

$$P_i^\ast = \frac{-r_i + \sqrt{r_i^2 + 4 q_i r_i}}{2}$$

The steady-state Kalman gain is:

$$K_i^\ast = \frac{P_i^\ast}{P_i^\ast + r_i} = \frac{P_i^\ast + q_i - P_i^\ast}{P_i^\ast + r_i} = \frac{q_i}{P_i^\ast + r_i}$$

Wait -- let me be more careful. For the scalar random walk with observation model above, the Kalman filter prediction step gives $P_{i,t\mid t-1} = P_{i,t-1} + q_i$ and the update step gives $P_{i,t} = (1 - K_{i,t}) P_{i,t\mid t-1}$ with $K_{i,t} = P_{i,t\mid t-1} / (P_{i,t\mid t-1} + r_i)$. At steady state:

$$P_i^\ast + q_i = P_{i,\text{pred}}^\ast, \quad K_i^\ast = \frac{P_{i,\text{pred}}^\ast}{P_{i,\text{pred}}^\ast + r_i}, \quad P_i^\ast = (1 - K_i^\ast) P_{i,\text{pred}}^\ast$$

Substituting: $P_i^\ast = P_{i,\text{pred}}^\ast \cdot r_i / (P_{i,\text{pred}}^\ast + r_i)$, and $P_{i,\text{pred}}^\ast = P_i^\ast + q_i$. So:

$$P_i^\ast = \frac{(P_i^\ast + q_i) r_i}{P_i^\ast + q_i + r_i}$$

This gives the Riccati equation: $P_i^{\ast 2} + P_i^\ast q_i + P_i^\ast r_i = P_i^\ast r_i + q_i r_i$, simplifying to $P_i^{\ast 2} + q_i P_i^\ast - q_i r_i = 0$, with positive root:

$$P_i^\ast = \frac{-q_i + \sqrt{q_i^2 + 4 q_i r_i}}{2}$$

And steady-state gain:

$$K_i^\ast = \frac{P_i^\ast + q_i}{P_i^\ast + q_i + r_i}$$

The AAD parameters for each filter:
- Event rate: $\nu_i = 1$ (one observation per time step).
- Optimal gain: $\eta_i^\ast = K_i^\ast$.
- Adaptive tempo: $\mathcal T_i = \nu_i \cdot \eta_i^\ast = K_i^\ast$.
- The "mismatch" is the innovation: $\delta_{i,t} = o_{i,t} - \hat\omega_{i,t\mid t-1}$, with variance $P_{i,\text{pred}}^\ast + r_i$.
- The "correction function" is the Kalman update: $F_i(\delta_i) = K_i^\ast \delta_i$ (linear, so the sector condition holds with $\alpha_i = K_i^\ast$, $R_i = \infty$ for the linear Gaussian case).

### 3.3 The natural projection

The natural macro-state for two agents tracking correlated processes is the best linear unbiased estimate of $\omega_c = (\omega_1, \omega_2)$ given the two individual estimates. Since each agent tracks one component, the natural projection candidates are:

**Projection A (concatenation / identity):** $\Lambda_x^{(A)} = \text{id}$: keep both estimates. Macro-state $= (\hat\omega_1, P_1, \hat\omega_2, P_2)$. Dimension 4 = micro dimension. Violates (P3). $\varepsilon^\ast = 0$ trivially. Not a genuine abstraction.

**Projection B (averaged scalar):** $\Lambda_x^{(B)}(X_{\text{micro}}) = \frac{1}{2}(\hat\omega_1 + \hat\omega_2)$. Macro-state dimension: 1. Genuine dimensionality reduction. But this is only meaningful if $\omega_1$ and $\omega_2$ are estimates of a common quantity, which they aren't (they track different processes). This projection is natural only when $\rho_{\text{corr}} = 1$ (perfectly correlated processes, meaning $\omega_1 = \omega_2 + \text{const}$).

**Projection C (optimal 2D estimator):** The "macro-agent" is the optimal joint estimator -- the full 2D Kalman filter that exploits cross-correlations. This uses macro-state $(\hat\omega_c, P_c)$ where $\hat\omega_c \in \mathbb R^2$ and $P_c \in \mathbb R^{2 \times 2}$. Macro-state dimension: $2 + 3 = 5$ (2 means, 3 unique covariance entries). This is LARGER than the micro-state (dimension 4), which seems paradoxical but reflects the fact that the joint estimator tracks cross-correlations that the independent filters ignore. Violates (P3) by increasing dimension.

**Projection D (means only):** $\Lambda_x^{(D)}(X_{\text{micro}}) = (\hat\omega_1, \hat\omega_2)$. Macro-state dimension: 2 (vs. micro-state dimension 4). Genuine reduction -- discards the covariance information $(P_1, P_2)$. The macro-agent knows the point estimates but not the uncertainty.

This is the interesting case for this spike: it discards real structure (uncertainty estimates) and we can compute the resulting closure defect exactly.

### 3.4 Working Projection D: means only

**Macro-state:** $X_c = (\hat\omega_1, \hat\omega_2)$, dimension 2.

**Projected micro-dynamics:** at each step, the Kalman filter update for agent $i$ is:

$$\hat\omega_{i,t} = \hat\omega_{i,t\mid t-1} + K_{i,t}(o_{i,t} - \hat\omega_{i,t\mid t-1}) = (1 - K_{i,t})\hat\omega_{i,t\mid t-1} + K_{i,t} o_{i,t}$$

with $\hat\omega_{i,t\mid t-1} = \hat\omega_{i,t-1}$ (random walk, so the prediction is just the previous estimate).

At steady state ($K_{i,t} = K_i^\ast$), the micro-dynamics for the mean are:

$$\hat\omega_{i,t} = (1 - K_i^\ast)\hat\omega_{i,t-1} + K_i^\ast o_{i,t}$$

Applying $\Lambda_x^{(D)}$ to the micro-state just reads off the means. The "projected micro-dynamics" are:

$$\Lambda_x^{(D)}(f_{\text{micro}}(X_{\text{micro},t}, o_t)) = \big((1 - K_1^\ast)\hat\omega_{1,t} + K_1^\ast o_{1,t+1},\; (1 - K_2^\ast)\hat\omega_{2,t} + K_2^\ast o_{2,t+1}\big)$$

**Macro-dynamics candidate:** the macro-agent updates the means using some gain $K_c$:

$$f_c(X_{c,t}, o_{c,t+1}) = \big((1 - K_{c,1})\hat\omega_{1,t} + K_{c,1} o_{1,t+1},\; (1 - K_{c,2})\hat\omega_{2,t} + K_{c,2} o_{2,t+1}\big)$$

**Closure defect for the state update:**

$$\varepsilon_x = \mathbb E\left[\frac{1}{2}\sum_{i=1}^2 \lvert(K_i^\ast - K_{c,i})(o_{i,t+1} - \hat\omega_{i,t})\rvert^2\right]^{1/2}$$

Wait -- I should be more careful with the norm. For a 2D macro-state, using the Euclidean norm:

$$\varepsilon_x^2 = \mathbb E\left[\sum_{i=1}^2 (K_i^\ast - K_{c,i})^2 (o_{i,t+1} - \hat\omega_{i,t})^2\right]$$

The innovation $o_{i,t+1} - \hat\omega_{i,t}$ has variance $P_i^\ast + q_i + r_i = P_{i,\text{pred}}^\ast + r_i$ (prediction error variance). So:

$$\varepsilon_x^2 = \sum_{i=1}^2 (K_i^\ast - K_{c,i})^2 (P_{i,\text{pred}}^\ast + r_i)$$

This is minimized when $K_{c,i} = K_i^\ast$ -- the macro-agent uses the same gains as the individual filters. In that case, $\varepsilon_x = 0$.

**Key observation.** For Projection D (means only), the optimal macro-dynamics exactly reproduce the micro-dynamics of the means, because the Kalman gain at steady state is a constant that doesn't depend on $P_{i,t}$ (it's converged to $K_i^\ast$). The covariance state $(P_1, P_2)$ has decoupled from the mean state $(\hat\omega_1, \hat\omega_2)$ at steady state.

**Result: $\varepsilon^\ast = 0$ for Projection D at steady state.** The discarded information (covariance) is irrelevant to the macro-dynamics of interest (mean updates). This is the information bottleneck in action: $P_i$ is "irrelevant" to predicting $\hat\omega_{i,t+1}$ given $\hat\omega_{i,t}$ and $o_{i,t+1}$, because $K_i^\ast$ is a constant.

**But this is too clean.** It depends on steady-state convergence. During transient ($P_{i,t}$ still evolving), $K_{i,t}$ depends on $P_{i,t}$, so discarding covariance creates a genuine closure defect. The transient closure defect measures how quickly the system converges to the regime where the projection is lossless.

### 3.5 The non-trivial case: correlated processes, joint estimation

The two-Kalman case becomes non-trivial when we ask: what does the *composite* know that the *individuals* don't?

Agent 1 tracks $\omega_1$ using $o_1$. Agent 2 tracks $\omega_2$ using $o_2$. When $\rho_{\text{corr}} \neq 0$, information about $\omega_2$ leaks through $o_1$ (because the process noises are correlated). Neither agent exploits this cross-information -- they run independent filters.

The **optimal joint estimator** (a single 2D Kalman filter on the full system) would use the observation model:

$$\begin{pmatrix} o_1 \\ o_2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} \omega_1 \\ \omega_2 \end{pmatrix} + \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$$

with process noise covariance $Q$ (correlated) and observation noise covariance $R = \text{diag}(r_1, r_2)$ (independent). The joint filter's steady-state covariance $P_c^\ast$ solves the 2D Riccati equation and satisfies $P_c^\ast \preceq \text{diag}(P_1^\ast, P_2^\ast)$ whenever $\rho_{\text{corr}} \neq 0$ -- the joint filter is strictly better because it exploits cross-correlations.

**The closure defect of the independent-filter composite.** The projection question becomes: how well can a macro-dynamics that processes $(o_1, o_2)$ jointly approximate the optimal joint estimator, when the micro-system consists of two independent filters?

Projection: $\Lambda_x(\hat\omega_1, P_1, \hat\omega_2, P_2) = (\hat\omega_1, \hat\omega_2)$ (keep means, discard individual covariances).

The optimal macro-dynamics for these two means would be the joint Kalman filter gains $K_c = (P_c^\ast + Q)(P_c^\ast + Q + R)^{-1}$ (2x2 matrix). But the micro-system uses $K_{\text{micro}} = \text{diag}(K_1^\ast, K_2^\ast)$.

The closure defect per step is:

$$\varepsilon_x = \mathbb E\left[\lVert (K_c - K_{\text{micro}})\delta_t \rVert^2\right]^{1/2}$$

where $\delta_t = (o_{1,t} - \hat\omega_{1,t}, o_{2,t} - \hat\omega_{2,t})$.

For the optimally chosen macro-dynamics (using $K_c$), the defect comes from the DIFFERENCE between what the micro-system does (independent gains) and what the optimal macro-system would do (joint gains). The off-diagonal entries of $K_c$ are the cross-gains -- the extent to which $o_1$ should update $\hat\omega_2$ and vice versa. The micro-system has zero cross-gains.

**Exact result.** Let $K_c = K_{\text{micro}} + \Delta K$ where $\Delta K$ captures the cross-gains. Then:

$$\varepsilon_x^2 = \text{tr}\big(\Delta K \cdot \text{Cov}[\delta_t] \cdot \Delta K^T\big) = \text{tr}\big(\Delta K (P_{\text{pred}}^\ast + R) \Delta K^T\big)$$

where $P_{\text{pred}}^\ast = \text{diag}(P_{1,\text{pred}}^\ast, P_{2,\text{pred}}^\ast)$ is the joint prediction covariance of the *independent* filters.

When $\rho_{\text{corr}} = 0$: $\Delta K = 0$, so $\varepsilon_x = 0$. Independent processes, independent filters -- no information to exploit across agents.

When $\rho_{\text{corr}} \neq 0$: $\Delta K \neq 0$, and $\varepsilon_x \propto \lvert\rho_{\text{corr}}\rvert$. The closure defect measures the cross-information that independent filters fail to exploit.

**This is the closure defect as missed opportunity.** The micro-system (two independent filters) fails to use cross-correlations. The optimal macro-system would use them. The gap $\varepsilon_x$ quantifies the cost of independence -- a sensible and interpretable result.

### 3.6 Admissibility verification for the two-Kalman case

**(P1) Information preservation.** The predictive mutual information of the projected state $(\hat\omega_1, \hat\omega_2)$ about next observations $(o_1, o_2)$ given current actions (none in this passive case):

$$I((\hat\omega_1, \hat\omega_2); (o_{1,t+1}, o_{2,t+1})) = I(\hat\omega_1; o_{1,t+1}) + I(\hat\omega_2; o_{2,t+1}) + \text{cross terms}$$

At steady state, $I(\hat\omega_i; o_{i,t+1})$ depends on the SNR $P_i^\ast / r_i$. The cross terms arise from the correlation between $\omega_1$ and $\omega_2$. The full micro-state $((\hat\omega_1, P_1), (\hat\omega_2, P_2))$ has the same predictive information as $(\hat\omega_1, \hat\omega_2)$ at steady state (because $P_i$ is constant and thus adds no information). So $(1 - \epsilon_I) = 1$ -- no information loss at steady state. (P1) is satisfied trivially.

**(P2) Lipschitz continuity.** $\Lambda_x^{(D)}$ is a linear projection (extract the mean components). Lipschitz constant $L = 1$ (it's a coordinate projection, hence non-expansive in the Euclidean norm).

**(P3) Dimensionality reduction.** $\dim(\mathcal X_c) = 2 \lt 4 = \dim(\mathcal X_{\text{micro}})$. Satisfied.

All three conditions are satisfied. The two-Kalman case is cleanly admissible under the proposed $\mathcal P_{\text{adm}}$.

---

## 4. Norm Specification for the Two-Kalman Case

The composition-closure Working Notes flag that norm choices are load-bearing but unspecified. Here we specify norms for the two-Kalman instantiation.

### 4.1 State norm: prediction-error covariance norm

The natural norm on the macro-state space measures the quality of the macro-estimate. For Kalman-filter-type agents, the natural metric is the prediction-error covariance.

*[Definition (Kalman state norm)]*

$$\lVert X_c - X_c' \rVert_{\mathcal X}^2 = (\hat\omega_c - \hat\omega_c')^T (P_{\text{pred}}^\ast)^{-1} (\hat\omega_c - \hat\omega_c')$$

This is the Mahalanobis distance weighted by the inverse prediction-error covariance. It normalizes each component by its expected variability -- differences in well-estimated components (small $P$) are more significant than differences in poorly-estimated components (large $P$).

**Why this norm.** In the Euclidean norm, a 1-unit difference in a well-estimated component counts the same as a 1-unit difference in a poorly-estimated one. The Mahalanobis norm says: what matters is how many "standard deviations" apart the estimates are, measured in the natural units of the estimation problem. This is the norm the Kalman filter itself implicitly uses -- the Kalman gain minimizes the trace of the error covariance, which is the expected squared Mahalanobis distance from truth.

### 4.2 Observation norm: innovation covariance norm

The natural norm on the observation space is the innovation-weighted norm:

$$\lVert o - o' \rVert_{\mathcal O}^2 = (o - o')^T S^{-1} (o - o')$$

where $S = P_{\text{pred}}^\ast + R$ is the innovation covariance of the optimal estimator.

### 4.3 Combination norm on $(\varepsilon_x, \varepsilon_a, \varepsilon_o)$

Since these are two passive estimators (no actions), $\varepsilon_a = 0$. The closure defect reduces to:

$$\varepsilon^\ast = \sqrt{\varepsilon_x^2 + \varepsilon_o^2}$$

with the state and observation norms specified above. In the active case (agents with actions), the combination norm should weight the three components by their relative importance to the macro-agent's persistence. A natural weighting:

$$\varepsilon^\ast = \sqrt{w_x \varepsilon_x^2 + w_a \varepsilon_a^2 + w_o \varepsilon_o^2}$$

where $w_x, w_a, w_o \gt 0$ sum to 1. For the Kalman case, $w_x = w_o = 1/2$.

### 4.4 The closure defect in these norms

Using the Mahalanobis state norm, the closure defect from $\S$3.5 becomes:

$$\varepsilon_x^2 = \text{tr}\big(\Delta K \cdot S \cdot \Delta K^T \cdot (P_{\text{pred}}^\ast)^{-1}\big)$$

This has a clean interpretation: it's the ratio of "missed cross-correction" to "expected estimation uncertainty." When the cross-gains $\Delta K$ are small relative to the estimation uncertainty, the closure defect is small -- the independent filters are nearly as good as the joint filter.

### 4.5 Norm specification for the general case

The two-Kalman case suggests a pattern for general norm specification:

1. **State norm**: weight by the inverse of the expected state uncertainty. Components that the agent estimates well should be weighted more heavily (differences there are more significant). Formally: if the macro-state has a natural covariance structure $\Sigma_X$, use $\lVert \cdot \rVert = \lVert \cdot \rVert_{\Sigma_X^{-1}}$.

2. **Observation norm**: weight by the inverse of the observation noise covariance. High-SNR observations should count more than noisy ones.

3. **Action norm**: weight by the sensitivity of the environment transition to the action. Actions that have large effects should be weighted more heavily.

For domains without a natural covariance structure (e.g., discrete state spaces, non-Gaussian models), the Euclidean norm is the default, with the caveat that it weights all components equally and may not reflect the agent's actual sensitivities.

---

## 5. Can $\mathcal P_{\text{adm}}$ Be Derived from (A1)-(A4)?

This is the key structural question: are the projection admissibility constraints (P1)-(P3) independent of the macro-dynamics admissibility constraints (A1)-(A4), or does requiring the macro-dynamics to be AAD-shaped already constrain which projections are admissible?

### 5.1 (A1)-(A4) partially constrain the projection

**(A1) implies partial P1.** If the macro-dynamics must decompose as $X_c = (M_c, G_c)$ with recursive update, then $\Lambda_x$ must map micro-states to a space that supports this decomposition. This rules out projections that destroy the epistemic/purposeful distinction -- for example, projecting all of $X_{\text{micro}}$ onto a single scalar. But it doesn't specify how much predictive information must be retained within the $(M_c, G_c)$ structure.

**(A2) implies information relevance.** If the macro-mismatch $\delta_c = o_c - \hat o_c(M_c, a_c)$ must be well-defined, then $\Lambda_o$ must produce observations from which predictions can be compared. This means $\Lambda_o$ must preserve enough observation structure for predictions to be meaningful. A projection that maps all observations to a constant violates (A2) -- the mismatch would be identically zero, which is vacuous, not informative.

**(A4) implies regularity.** The sector condition requires $\delta_c^T F_c(\mathcal T_c, \delta_c) \geq \alpha_c \lVert\delta_c\rVert^2$. If $\Lambda_x$ is wildly discontinuous, the macro-dynamics $f_c$ inherits that discontinuity through the closure equation, making the sector condition impossible to satisfy. In practice, (A4) imposes an implicit Lipschitz constraint on the projection -- not directly, but through the requirement that the macro-correction function be well-behaved.

### 5.2 What (A1)-(A4) do NOT constrain

**(A1)-(A4) do not specify information preservation level.** The macro-agent could have a very coarse model (low predictive information) or a very fine model (high predictive information), as long as the sector condition is satisfied. A macro-agent with a crude model can still have a positive $\alpha_c$ (it corrects its crude predictions reliably); the mismatch is just larger.

**(A1)-(A4) do not specify dimensionality.** The macro-state could be nearly as large as the micro-state (fine-grained abstraction) or much smaller (coarse abstraction), as long as (A1)-(A4) are satisfied.

**(A1)-(A4) do not prevent degenerate projections -- entirely.** Consider a projection that maps all micro-states to a single fixed point $X_c^0$. The macro-dynamics trivially satisfies (A1) (with degenerate $(M_c, G_c)$). But (A2) fails: the mismatch is either undefined or identically zero. So (A2) rules out the most degenerate case. But it doesn't rule out projections that retain some structure while discarding most predictive information.

### 5.3 Assessment

**(A1)-(A4) partially constrain $\Lambda$ but do not fully determine $\mathcal P_{\text{adm}}$.** The macro-dynamics admissibility imposes implicit structural and regularity requirements on the projection, but these are necessary conditions, not a complete specification.

The key gap: **(A1)-(A4) do not specify how much predictive information the projection must retain.** They specify that the macro-dynamics must work (positive correction, bounded mismatch), but a macro-agent with a very coarse projection can still "work" in the formal sense while being a poor representation of the micro-system. The information-preservation condition (P1) fills this gap by requiring the macro-state to retain a controlled fraction of the predictive structure.

**Conclusion.** $\mathcal P_{\text{adm}}$ is genuinely independent of $\mathcal M_{\text{adm}}$. The macro-dynamics admissibility constrains what the macro-dynamics look like (structural, stability); the projection admissibility constrains what the projection looks like (information, regularity). Both are needed for $\varepsilon^\ast$ to be well-defined over a non-trivial, non-degenerate class.

However, the two classes interact: a good projection makes it easier to find macro-dynamics satisfying (A1)-(A4) with large $\alpha_c$, and strict macro-dynamics constraints (high $\alpha_c$) implicitly require projections with good regularity. The optimization over the product $\mathcal P_{\text{adm}} \times \mathcal M_{\text{adm}}$ is a joint optimization, not two independent ones.

---

## 6. What Remains Open

### 6.1 Computing (P1) in practice

The information-preservation condition requires computing conditional mutual information over the joint distribution of micro-states, observations, and actions. For linear-Gaussian systems (like the Kalman case), this is tractable -- mutual information has closed-form expressions in terms of covariance matrices. For general nonlinear, non-Gaussian systems, it requires either:
- Monte Carlo estimation from simulated trajectories (feasible but expensive)
- Variational bounds (tractable but approximate)
- Domain-specific structure that simplifies the computation

The practical computability of (P1) for real multi-agent systems is an open empirical question.

### 6.2 The right value of $\epsilon_I$

The information-preservation threshold $\epsilon_I$ is a free parameter. Too small ($\epsilon_I \to 0$): only near-lossless projections are admissible, making $\varepsilon^\ast$ large (few projections to search over). Too large ($\epsilon_I \to 1$): degenerate projections are admissible, making $\varepsilon^\ast$ meaningless. What is the "right" $\epsilon_I$?

A natural choice: $\epsilon_I$ should be comparable to the fractional information loss from adding one additional agent to the composite. If adding agent $N+1$ loses $\epsilon_I$ of predictive information through increased coordination demands, the projection can afford to lose $\epsilon_I$ as well. This ties $\epsilon_I$ to the team size and coupling structure, but formalizing this relationship is open.

### 6.3 Extension to non-Gaussian, nonlinear systems

The two-Kalman instantiation benefits enormously from linearity and Gaussianity:
- Mutual information has closed forms.
- Kalman gains are computable.
- Steady-state convergence is guaranteed.
- The projection is a linear map with Lipschitz constant 1.

In nonlinear systems:
- Mutual information requires approximation.
- Gains are state-dependent (no steady-state gain in general).
- Convergence is not guaranteed.
- Nonlinear projections may have state-dependent Lipschitz constants.

The Lipschitz condition (P2) generalizes cleanly: any smooth projection between finite-dimensional manifolds is locally Lipschitz. The information condition (P1) generalizes in principle (mutual information is always well-defined) but becomes computationally intractable.

For particle filters, ensemble Kalman filters, and other nonlinear estimators, the natural projection is empirical: project the particle cloud or ensemble, and measure information preservation empirically. Whether this can be formalized as an admissibility condition (rather than checked post hoc) is open.

### 6.4 Scaling with $N$ agents

For $N$ agents, the micro-state dimension scales as $O(N \cdot d)$ where $d$ is the per-agent state dimension. The projection must reduce this to $O(d_c)$ where $d_c \ll N \cdot d$.

The information-preservation condition becomes harder to satisfy as $N$ grows: more agents means more micro-information, and retaining $(1 - \epsilon_I)$ of it requires a higher-dimensional macro-state. At some $N$, no projection satisfying (P1) and (P3) simultaneously may exist -- the macro-state must be nearly as large as the micro-state to retain enough predictive information.

This is the formal analog of the claim that very large teams cannot be treated as single agents. The theory should predict this: for sufficiently large $N$ with sufficient inter-agent coupling, $\varepsilon^\ast$ exceeds $\varepsilon_{\max}$, and the composite is no longer a valid macro-agent.

Whether $\varepsilon^\ast$ scales polynomially or exponentially with $N$ depends on the coupling structure. For tree-structured coupling (hierarchical organizations), dimensional reduction may be efficient. For fully-connected coupling, it may not. Characterizing this scaling is a major open question.

### 6.5 Relationship to Mori-Zwanzig formalism

The Mori-Zwanzig (MZ) projection operator formalism (Mori 1965, Zwanzig 1973) is the standard framework for coarse-graining dynamical systems in statistical mechanics. MZ decomposes the dynamics into a "relevant" part (projected, Markovian) and a "memory" part (the integral of past correlations between projected and discarded variables).

The closure defect $\varepsilon^\ast$ is related to the MZ memory kernel: when the memory kernel is small (fast decay of correlations between projected and discarded variables), the closure defect is small. When the memory kernel is large (slow decay, long-range correlations), the macro-description requires memory corrections -- the "Markovian macro-dynamics" assumed by (A1) fail.

A rigorous connection between $\varepsilon^\ast$ and the MZ memory kernel would anchor AAD's composition framework in established dynamical-systems theory. The form should be: $\varepsilon^\ast \geq \text{(something involving the norm of the memory kernel)}$, providing a lower bound on the closure defect in terms of the non-Markovian character of the projected dynamics. This connection is plausible but unworked.

### 6.6 Projection admissibility for strategy DAGs

The projection $\Lambda_x$ maps micro-states (including individual strategy DAGs $\Sigma_i$) to a macro-state (including a possible macro-strategy $\Sigma_c$). How should individual strategies compose under projection?

Options:
- **Union of DAGs**: $\Sigma_c$ is the union of all individual DAGs, with inter-agent edges added. Dimension increases with $N$ -- violates (P3).
- **Abstracted DAG**: $\Sigma_c$ has coarser nodes (each macro-node corresponds to a cluster of micro-nodes from different agents). This is genuine projection but requires a principled clustering method.
- **No macro-strategy**: $G_c = O_c$ (shared objective only), with no explicit $\Sigma_c$. The macro-agent has a goal but no articulated plan. This is the simplest (and most honest for loosely coupled teams) but excludes strategy-dependent results at the macro level.

How to project strategies is deeply domain-specific and is not resolved by (P1)-(P3). The information-preservation condition provides a functional test (does the projected strategy retain predictive information about macro-actions?), but the specific projection mechanism remains open.

---

## 7. Summary and Recommendations

### What this spike establishes:

1. **$\mathcal P_{\text{adm}}$ is specified as three conditions**: (P1) information preservation, (P2) Lipschitz continuity, (P3) dimensionality reduction. No single condition suffices alone; together they prevent degenerate projections (P1), pathological projections (P2), and trivial projections (P3).

2. **The two-Kalman case is fully worked**: natural projection (means only, Projection D), exact closure defect (zero at steady state for independent processes, proportional to $\lvert\rho_{\text{corr}}\rvert$ for correlated processes), admissibility verified (all three conditions satisfied with $L = 1$, $\epsilon_I = 0$).

3. **Norm choices are specified**: Mahalanobis (inverse-covariance-weighted) norms for states and observations, with the prediction-error covariance as the natural weighting matrix. The combination norm on $(\varepsilon_x, \varepsilon_a, \varepsilon_o)$ is Euclidean with optional domain-specific weights.

4. **$\mathcal P_{\text{adm}}$ is genuinely independent of $\mathcal M_{\text{adm}}$**: (A1)-(A4) partially constrain the projection (ruling out the most degenerate cases) but do not fully determine it. The information-preservation condition is the key independent contribution.

5. **The closure defect as missed opportunity**: in the Kalman case, $\varepsilon^\ast$ measures the cross-information that independent agents fail to exploit. This is a more interpretable meaning than "approximation error" -- it's the cost of independence.

### What remains:

- Computing (P1) for nonlinear/non-Gaussian systems (tractability open).
- The right choice of $\epsilon_I$ (likely domain-dependent; no universal recommendation).
- Scaling of $\varepsilon^\ast$ with $N$ (depends on coupling structure; tree vs. fully connected).
- Connection to Mori-Zwanzig formalism (plausible but unworked).
- Strategy DAG projection (deeply domain-specific; not resolved by the general framework).

### Recommendations for promotion:

- **(P1)-(P3) are ready for inclusion in #composition-closure.** They can be added as a new subsection "Admissibility constraints on projections" parallel to the existing "Admissibility constraints on macro-dynamics." The $(\epsilon_I, L)$ parameters should be presented as problem specification, not derived quantities.
- **The two-Kalman case is ready for a worked-example segment** (a new `worked-kalman-composition` slug). It instantiates the full composition-closure framework with exact results and interpretable quantities.
- **The norm specification is ready for inclusion in #composition-closure's Working Notes** as a concrete recommendation, not a requirement. The Mahalanobis norm is natural for estimation-type agents; other domains need their own norms.
- **The A1-A4 vs. P1-P3 independence result should be stated** in the Epistemic Status of #composition-closure, clarifying that projection admissibility is a separate formulation choice.
