# Spike: Sector Condition Verification for Single-Edge Strategic Dynamics

**Status**: Spike (investigatory). Attempts to instantiate the strategy-persistence-schema (#schema-strategy-persistence) for the simplest possible case.

**Date**: 2026-04-01

**Objective**: Verify whether the Beta-Bernoulli edge-credence update satisfies the sector condition from #deriv-sector-condition, thereby closing the gap between the proposed schema and a genuine result for the one-edge case.

**Depends on**: #schema-strategy-persistence, #hyp-edge-update-via-gain, #deriv-sector-condition, #result-sector-condition-stability, #result-persistence-condition, #emp-update-gain

---

## 1. Setup

Consider the simplest possible purposeful agent: one action $A$, one goal $G$, one strategy edge $A \to G$ with credence $p \in [0, 1]$.

- **True success probability**: $\theta \in (0, 1)$. Executing action $A$ yields success (reaching $G$) with probability $\theta$ and failure with probability $1 - \theta$.
- **Agent's belief**: The agent maintains a Beta posterior $p \sim \text{Beta}(\alpha_c, \beta_c)$ over the edge's reliability, with point estimate $\hat{p} = \alpha_c / (\alpha_c + \beta_c)$. (We use $\alpha_c, \beta_c$ for the Beta pseudo-counts to avoid collision with the sector-condition parameter $\alpha$.)
- **Update rule**: On observing outcome $y \in \{0, 1\}$ (failure/success), the agent performs the standard conjugate update:
  - Success ($y = 1$): $\alpha_c \to \alpha_c + 1$
  - Failure ($y = 0$): $\beta_c \to \beta_c + 1$

Let $n = \alpha_c + \beta_c$ be the total pseudo-count (a measure of experience). The point estimate after update is:

$$\hat{p}_{\text{new}} = \frac{\alpha_c + y}{n + 1}$$

*[Definition (single-edge setup)]*

---

## 2. Mapping to AAD Quantities

The sector-condition framework (#deriv-sector-condition) requires:

1. A **mismatch state** $\delta$
2. A **correction function** $F$ such that $\delta^T F \geq \alpha \|\delta\|^2$
3. A **bounded disturbance** $\|w(t)\| \leq \rho$

We now identify each quantity for the single-edge case.

### 2.1 Strategic Mismatch

*[Formulation (strategic-mismatch, single-edge case)]*

$$\delta_\Sigma = \hat{p} - \theta$$

The strategic mismatch is the difference between the agent's credence in the edge and the true success probability. This is a scalar, so $\|\delta_\Sigma\| = |\hat{p} - \theta|$.

**Why this, not $|p - \theta|$ for some distributional $p$?** The agent acts on its point estimate $\hat{p}$. The full posterior $\text{Beta}(\alpha_c, \beta_c)$ captures uncertainty *about* $\theta$, but the mismatch that matters for strategic persistence is between the *operative belief* (the credence driving decisions) and the *truth*. The point estimate is the operative belief for a risk-neutral agent.

**Zero mismatch at truth**: When $\hat{p} = \theta$, $\delta_\Sigma = 0$. This satisfies the structural requirement (SA1) — no correction occurs when the edge credence is perfectly calibrated (the expected update is zero; see §3).

### 2.2 Correction Function

The Beta-Bernoulli update changes the point estimate by:

$$\Delta \hat{p} = \hat{p}_{\text{new}} - \hat{p} = \frac{\alpha_c + y}{n + 1} - \frac{\alpha_c}{n} = \frac{n(\alpha_c + y) - \alpha_c(n + 1)}{n(n+1)} = \frac{ny - \alpha_c}{n(n+1)} = \frac{y - \hat{p}}{n + 1}$$

So the single-step update is:

*[Derived (single-step update)]*

$$\Delta \hat{p} = \frac{1}{n+1}(y - \hat{p})$$

This matches the gain-based form from #hyp-edge-update-via-gain:

$$\hat{p}_{\text{new}} = \hat{p} + \eta_{\text{edge}} \cdot (\text{signal} - \hat{p})$$

with $\eta_{\text{edge}} = 1/(n+1)$ and $\text{signal} = y$.

**Expected correction.** The outcome $y$ is Bernoulli with parameter $\theta$, so:

*[Derived (expected correction)]*

$$\mathbb{E}[\Delta \hat{p} \mid \theta, \hat{p}] = \frac{1}{n+1}(\theta - \hat{p}) = -\frac{1}{n+1}\delta_\Sigma$$

The expected update always points toward the truth: positive when $\hat{p} < \theta$, negative when $\hat{p} > \theta$, zero when $\hat{p} = \theta$.

**Identifying $F$.** The mismatch dynamics in AAD are $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$. In the discrete single-edge case, with one observation per time step and no disturbance (stationary $\theta$):

$$\mathbb{E}[\delta_{\Sigma,t+1} - \delta_{\Sigma,t}] = \mathbb{E}[\Delta \hat{p}] = -\frac{1}{n+1}\delta_\Sigma$$

So the correction function (in expected value) is:

*[Formulation (correction function, single-edge)]*

$$F_\Sigma(\delta_\Sigma) = \frac{1}{n+1}\delta_\Sigma = \eta_{\text{edge}} \cdot \delta_\Sigma$$

This is linear in $\delta_\Sigma$ with slope $\eta_{\text{edge}} = 1/(n+1)$.

### 2.3 Strategic Disturbance

If $\theta$ is stationary, there is no disturbance: $w(t) = 0$. The mismatch shrinks toward zero (posterior concentration).

*[Formulation (strategic disturbance, single-edge)]*

If $\theta$ drifts — the true edge reliability changes over time at rate $|\dot{\theta}| \leq \rho_\Sigma$ — then each time step introduces new mismatch of magnitude up to $\rho_\Sigma$. The mismatch dynamics become:

$$\mathbb{E}[\delta_{\Sigma,t+1}] = \delta_{\Sigma,t} - \frac{1}{n+1}\delta_{\Sigma,t} + w_t = \left(1 - \frac{1}{n+1}\right)\delta_{\Sigma,t} + w_t$$

where $|w_t| \leq \rho_\Sigma$.

**Sources of strategic disturbance in the single-edge case:**
- The environment changes such that $A$'s success probability shifts (e.g., a tool degrades, a market condition changes, an adversary adapts)
- The goal $G$ redefines what counts as "success" (objective revision — but this is outside the single-edge model)

### 2.4 Update Gain

*[Derived (edge update gain)]*

$$\eta_{\text{edge}} = \frac{1}{n + 1} = \frac{1}{\alpha_c + \beta_c + 1}$$

This is a decreasing function of experience. A fresh agent ($n$ small) has high gain; an experienced agent ($n$ large) has low gain. This is the Beta-Bernoulli special case of the uncertainty-ratio principle (#emp-update-gain): $\eta^* = U_M / (U_M + U_o)$, where:

- $U_M = \text{Var}[\text{Beta}(\alpha_c, \beta_c)] = \alpha_c \beta_c / (n^2(n+1))$
- $U_o$ is the observation noise (for Bernoulli outcomes, the inherent variance $\theta(1-\theta)$)

In the Bernoulli case, the exact Bayesian posterior update gives $\eta_{\text{edge}} = 1/(n+1)$ regardless of $U_o$ — the conjugacy absorbs observation noise automatically. The gain decreases purely as a function of accumulated evidence.

---

## 3. Sector Condition Verification

**This is the key mathematical step.** We need to verify (SA2') from #deriv-sector-condition:

$$\delta_\Sigma \cdot F_\Sigma(\delta_\Sigma) \geq \alpha_\Sigma \cdot \delta_\Sigma^2 \quad \text{for } |\delta_\Sigma| \leq R_\Sigma$$

(In one dimension, $\delta^T F = \delta \cdot F$ since both are scalars.)

### 3.1 Expected Sector Condition

*[Derived (expected sector condition, single-edge)]*

Substituting $F_\Sigma(\delta_\Sigma) = \eta_{\text{edge}} \cdot \delta_\Sigma$:

$$\delta_\Sigma \cdot F_\Sigma(\delta_\Sigma) = \delta_\Sigma \cdot \eta_{\text{edge}} \cdot \delta_\Sigma = \eta_{\text{edge}} \cdot \delta_\Sigma^2$$

Therefore:

$$\eta_{\text{edge}} \cdot \delta_\Sigma^2 \geq \alpha_\Sigma \cdot \delta_\Sigma^2$$

This holds for all $\delta_\Sigma$ when:

$$\alpha_\Sigma \leq \eta_{\text{edge}} = \frac{1}{n+1}$$

**The sector condition is satisfied in expectation, with $\alpha_\Sigma = \eta_{\text{edge}} = 1/(n+1)$.** In fact, the expected correction is *exactly* linear ($F_\Sigma = \eta_{\text{edge}} \cdot \delta_\Sigma$), so the sector bound is tight — $\alpha_\Sigma$ equals the slope exactly, not merely a lower bound.

**The sector condition holds globally** (for all $\delta_\Sigma \in [-1, 1]$, not just within some local ball $\mathcal{B}_R$), because the linearity of the expected correction holds for all $\hat{p}, \theta \in [0, 1]$. There is no saturation, no breakdown, no threshold — the Beta-Bernoulli update is a well-behaved linear correction in expectation.

### 3.2 Stochastic Complication

The above analysis uses the *expected* correction. But the actual single-step correction is stochastic:

$$\Delta \hat{p} = \frac{y - \hat{p}}{n + 1}, \quad y \sim \text{Bernoulli}(\theta)$$

The actual $\delta_\Sigma \cdot \Delta\hat{p}$ on a single step can be negative (the update moves *away* from truth). Specifically:

- If $\hat{p} < \theta$ (agent underestimates), a failure ($y = 0$) pushes $\hat{p}$ further down: $\Delta\hat{p} = -\hat{p}/(n+1) < 0$, increasing $|\delta_\Sigma|$.
- If $\hat{p} > \theta$ (agent overestimates), a success ($y = 1$) pushes $\hat{p}$ further up: $\Delta\hat{p} = (1-\hat{p})/(n+1) > 0$, increasing $|\delta_\Sigma|$.

The probability of a "wrong-direction" step when $\hat{p} < \theta$ is $P(y = 0) = 1 - \theta$. For $\hat{p} > \theta$, it is $P(y = 1) = \theta$.

**However, the expected product is still positive:**

*[Derived (expected sector product)]*

$$\mathbb{E}[\delta_\Sigma \cdot \Delta\hat{p}] = \delta_\Sigma \cdot \mathbb{E}[\Delta\hat{p}] = \delta_\Sigma \cdot \frac{-\delta_\Sigma}{n+1} = -\frac{\delta_\Sigma^2}{n+1}$$

Wait — the sign convention needs care. We have $\delta_\Sigma = \hat{p} - \theta$, and $\Delta\hat{p} = (y - \hat{p})/(n+1)$. The *correction* in the sector framework is $F_\Sigma = -\mathbb{E}[\Delta\delta_\Sigma]$. Since $\Delta\delta_\Sigma = \Delta\hat{p}$ (because $\theta$ is fixed on a single step), and $\mathbb{E}[\Delta\hat{p}] = (\theta - \hat{p})/(n+1) = -\delta_\Sigma/(n+1)$:

$$F_\Sigma = -\mathbb{E}[\Delta\delta_\Sigma] = \frac{\delta_\Sigma}{n+1}$$

So $\delta_\Sigma \cdot F_\Sigma = \delta_\Sigma^2/(n+1) > 0$ for $\delta_\Sigma \neq 0$. The sector condition holds in expectation.

**The stochastic reality.** For a proper stochastic Lyapunov treatment, we would need the *expected* Lyapunov derivative:

$$\mathbb{E}[\Delta V \mid \delta_\Sigma] = \mathbb{E}\left[\frac{1}{2}\delta_{\Sigma,t+1}^2 - \frac{1}{2}\delta_{\Sigma,t}^2\right]$$

Let us compute this directly.

*[Derived (expected Lyapunov change)]*

$$\delta_{\Sigma,t+1} = \hat{p}_{\text{new}} - \theta = \hat{p} + \frac{y - \hat{p}}{n+1} - \theta = \delta_\Sigma \cdot \frac{n}{n+1} + \frac{y - \theta}{n+1}$$

Therefore:

$$\delta_{\Sigma,t+1}^2 = \delta_\Sigma^2 \cdot \frac{n^2}{(n+1)^2} + 2\delta_\Sigma \cdot \frac{n}{(n+1)^2}(y - \theta) + \frac{(y - \theta)^2}{(n+1)^2}$$

Taking expectations ($\mathbb{E}[y - \theta] = 0$, $\mathbb{E}[(y-\theta)^2] = \theta(1-\theta)$):

$$\mathbb{E}[\delta_{\Sigma,t+1}^2] = \delta_\Sigma^2 \cdot \frac{n^2}{(n+1)^2} + \frac{\theta(1-\theta)}{(n+1)^2}$$

So:

$$\mathbb{E}[\Delta V] = \frac{1}{2}\mathbb{E}[\delta_{\Sigma,t+1}^2] - \frac{1}{2}\delta_\Sigma^2 = \frac{1}{2}\left[\delta_\Sigma^2\left(\frac{n^2}{(n+1)^2} - 1\right) + \frac{\theta(1-\theta)}{(n+1)^2}\right]$$

$$= \frac{1}{2}\left[-\delta_\Sigma^2 \cdot \frac{2n + 1}{(n+1)^2} + \frac{\theta(1-\theta)}{(n+1)^2}\right]$$

$$= \frac{1}{2(n+1)^2}\left[-(2n+1)\delta_\Sigma^2 + \theta(1-\theta)\right]$$

**For the Lyapunov function to decrease in expectation**, we need:

$$\mathbb{E}[\Delta V] < 0 \iff (2n+1)\delta_\Sigma^2 > \theta(1-\theta)$$

$$\iff |\delta_\Sigma| > \sqrt{\frac{\theta(1-\theta)}{2n+1}}$$

*[Derived (stochastic ultimate bound, single-edge)]*

This gives the **stochastic ultimate bound**:

$$|\delta_\Sigma|^* = \sqrt{\frac{\theta(1-\theta)}{2n+1}}$$

When mismatch exceeds this threshold, the expected Lyapunov derivative is negative — mismatch decreases in expectation. When mismatch is below this threshold, the Bernoulli observation noise can dominate the correction, and mismatch may fluctuate.

**Interpretation.** The stochastic ultimate bound $|\delta_\Sigma|^*$ decreases as $1/\sqrt{n}$ — the standard Bayesian posterior concentration rate. For a stationary $\theta$, the mismatch converges to zero in probability. This is just the Bayesian consistency result (for Beta-Bernoulli, the posterior concentrates on the true $\theta$) expressed in the Lyapunov language.

### 3.3 Reconciling with the Sector Framework

The sector condition holds in the deterministic-equivalent sense: the expected correction satisfies $\alpha_\Sigma = 1/(n+1)$. The stochastic residual introduces an effective noise floor at $|\delta_\Sigma|^* = \sqrt{\theta(1-\theta)/(2n+1)}$.

To map this cleanly to the AAD framework, we decompose:

*[Formulation (stochastic sector decomposition)]*

$$\Delta\delta_\Sigma = \underbrace{-\frac{\delta_\Sigma}{n+1}}_{\text{correction } (-F_\Sigma)} + \underbrace{\frac{y - \theta}{n+1}}_{\text{observation noise}}$$

The observation noise term $\epsilon = (y - \theta)/(n+1)$ has zero mean and variance $\theta(1-\theta)/(n+1)^2$. It plays the role of the disturbance $w(t)$ in the sector framework, but it is *internal* noise (arising from the binary nature of the observation), not *external* disturbance (from $\theta$ changing).

**Effective disturbance from observation noise:**

$$\rho_{\text{obs}} = \sqrt{\mathbb{E}[\epsilon^2]} = \frac{\sqrt{\theta(1-\theta)}}{n+1}$$

This is the RMS magnitude of the per-step noise injection. It decreases as $1/(n+1)$ — the observation noise becomes less damaging as the agent accumulates experience, because the gain $\eta_{\text{edge}} = 1/(n+1)$ shrinks the impact of each observation.

---

## 4. Persistence Condition for the Single Edge

We can now write the persistence condition for the single-edge strategy, combining the sector parameter with both sources of disturbance.

### 4.1 Stationary Environment ($\theta$ fixed)

With no environmental drift, the only "disturbance" is observation noise. From the stochastic analysis (§3.2), the mismatch fluctuates around zero with scale $|\delta_\Sigma|^* = \sqrt{\theta(1-\theta)/(2n+1)}$. There is no persistence threshold to satisfy — the agent always converges. This is the Bayesian consistency result: with sufficient data, the posterior concentrates on truth.

**There is no strategic persistence problem in a stationary single-edge environment.** The agent's belief converges to reality regardless of initial conditions.

### 4.2 Drifting Environment ($\theta$ changes)

Now suppose $\theta$ changes over time at rate $|\dot{\theta}| \leq \rho_\Sigma$. Each time step introduces up to $\rho_\Sigma$ of new mismatch in addition to the correction and observation noise:

$$\Delta\delta_\Sigma = -\frac{\delta_\Sigma}{n+1} + \frac{y - \theta}{n+1} + w_t, \qquad |w_t| \leq \rho_\Sigma$$

The expected Lyapunov derivative with disturbance (using the deterministic bound, following #deriv-sector-condition):

$$\mathbb{E}[\Delta V] \leq -\frac{\delta_\Sigma^2}{n+1} + |\delta_\Sigma| \cdot \rho_\Sigma + \frac{\theta(1-\theta)}{2(n+1)^2}$$

(The first term is from the correction; the second is the disturbance coupling; the third is the observation-noise contribution computed in §3.2, absorbed into a constant floor.)

For the dominant-balance persistence condition, we focus on the deterministic sector framework (disturbance vs. correction), treating observation noise as a secondary effect that inflates the ultimate bound:

*[Derived (single-edge persistence condition)]*

$$\alpha_\Sigma > \frac{\rho_\Sigma}{R_\Sigma}$$

where:
- $\alpha_\Sigma = \frac{1}{n+1}$ (sector parameter = edge update gain)
- $\rho_\Sigma$ is the drift rate of $\theta$
- $R_\Sigma$ is the maximum tolerable credence error (the agent's "strategic reserve" — how wrong the edge credence can be before decisions degrade catastrophically)

**Persistence threshold:**

*[Derived (single-edge persistence threshold)]*

$$\frac{1}{n+1} > \frac{\rho_\Sigma}{R_\Sigma} \quad \iff \quad n < \frac{R_\Sigma}{\rho_\Sigma} - 1$$

**The ultimately bounded mismatch** (when the condition is satisfied):

$$|\delta_\Sigma|_{ss} = \frac{\rho_\Sigma}{\alpha_\Sigma} = \rho_\Sigma \cdot (n+1)$$

(Plus the observation-noise floor $\sqrt{\theta(1-\theta)/(2n+1)}$, which is typically subdominant when $\rho_\Sigma$ is non-negligible.)

### 4.3 Interpretation

The persistence condition $n < R_\Sigma / \rho_\Sigma - 1$ has a striking and important interpretation:

**An experienced agent is MORE vulnerable to strategic drift than a novice.**

As the agent accumulates experience ($n$ grows), its update gain $\eta_{\text{edge}} = 1/(n+1)$ decreases. This is ordinarily a virtue (stability, resistance to noise). But in a drifting environment, it becomes a liability: the agent cannot update fast enough to track the changing truth.

Specifically:
- **Novice agent** ($n$ small): high gain, tracks drift easily, but noisy estimates
- **Experienced agent** ($n$ large): low gain, stable estimates, but sluggish to track drift
- **Critical transition**: when $n$ exceeds $R_\Sigma / \rho_\Sigma - 1$, the agent's credence error exceeds the tolerable bound

**This is the gain-collapse phenomenon** identified in #emp-update-gain, now given precise quantitative form for the single-edge case. The gain decreases as $1/(n+1)$; the disturbance $\rho_\Sigma$ is constant; eventually the gain falls below the threshold.

### 4.4 Connection to Adaptive Reserve

*[Derived (single-edge adaptive reserve)]*

$$\Delta\rho_\Sigma^* = \alpha_\Sigma \cdot R_\Sigma - \rho_\Sigma = \frac{R_\Sigma}{n+1} - \rho_\Sigma$$

The adaptive reserve *decreases with experience* — the agent becomes more fragile to drift as it becomes more confident. When $\Delta\rho_\Sigma^* = 0$:

$$n^* = \frac{R_\Sigma}{\rho_\Sigma} - 1$$

This is the **critical experience level** — the pseudo-count at which the agent's posterior concentration exactly matches its need to track environmental drift. Beyond $n^*$, the agent cannot absorb any additional disturbance.

---

## 5. The Forgetting Fix: Experience Discounting

The persistence failure at large $n$ has a well-known remedy: **discount old evidence.** If the agent maintains an effective window of the most recent $n_{\text{eff}}$ observations (via exponential forgetting, sliding window, or equivalent), then the gain stabilizes at $\eta_{\text{edge}} \approx 1/(n_{\text{eff}} + 1)$ rather than declining to zero.

*[Discussion (experience discounting)]*

**Exponential forgetting.** Replace the Beta update with a discounted version: at each step, shrink the pseudo-counts by a factor $\lambda \in (0, 1)$:

$$\alpha_c \to \lambda \alpha_c + y, \quad \beta_c \to \lambda \beta_c + (1 - y)$$

The effective pseudo-count stabilizes at $n_{\text{eff}} \approx 1/(1 - \lambda)$, giving a steady-state gain of:

$$\eta_{\text{eff}} \approx \frac{1 - \lambda}{1} = 1 - \lambda$$

The persistence condition becomes:

$$(1 - \lambda) > \frac{\rho_\Sigma}{R_\Sigma} \quad \iff \quad \lambda < 1 - \frac{\rho_\Sigma}{R_\Sigma}$$

**Interpretation.** The forgetting rate $(1 - \lambda)$ must exceed the disturbance-to-reserve ratio. More forgetting means faster tracking but noisier estimates; less forgetting means stable estimates but slower tracking. The optimal $\lambda$ balances these — this is the bias-variance tradeoff for a non-stationary single-edge strategy.

**Connection to AAD.** This is the strategic analog of the gain-reset mechanism described in #emp-update-gain: "An agent whose gain does NOT reset after structural change will continue trusting a stale model." In the single-edge case, continuous discounting replaces discrete reset, but the principle is the same — the agent must maintain sufficient update capacity to track a changing environment.

---

## 6. Summary of Results

| Quantity | AAD (epistemic, general) | Single-edge strategic analog |
|----------|-------------------------|------------------------------|
| Mismatch $\delta$ | $M_t$ predictions $-$ reality | $\hat{p} - \theta$ (credence $-$ truth) |
| Correction $F$ | Sector-bounded, general | $\eta_{\text{edge}} \cdot \delta_\Sigma$ (linear, exact) |
| Sector parameter $\alpha$ | Worst-case correction efficiency | $1/(n+1)$ (update gain) |
| Disturbance $\rho$ | Environment change rate | $\theta$ drift rate |
| Reserve $R$ | Model class capacity | Max tolerable credence error |
| Persistence | $\alpha > \rho/R$ | $1/(n+1) > \rho_\Sigma / R_\Sigma$ |
| Ultimate bound $R^*$ | $\rho/\alpha$ | $\rho_\Sigma \cdot (n+1)$ |
| Adaptive reserve $\Delta\rho^*$ | $\alpha R - \rho$ | $R_\Sigma/(n+1) - \rho_\Sigma$ |

*[Derived (sector condition verification — single-edge Beta-Bernoulli)]*

**The sector condition is satisfied.** For the expected Beta-Bernoulli correction function, $F_\Sigma(\delta_\Sigma) = \delta_\Sigma/(n+1)$, the sector condition holds globally (all $|\delta_\Sigma| \leq 1$) with $\alpha_\Sigma = 1/(n+1)$. The bound is tight — the correction is exactly linear, so $\alpha_\Sigma$ equals the correction slope.

**The persistence condition has the same form as the epistemic case** ($\alpha > \rho/R$), instantiated with strategic quantities. The strategy-persistence-schema's proposed form is confirmed for this case.

---

## 7. What This Does and Doesn't Establish

### What it establishes

1. **The sector condition is satisfiable for strategic dynamics.** The Beta-Bernoulli correction function satisfies (SA2') globally, not just locally. This is the simplest possible case, but it closes the gap between "proposed schema" and "verified for at least one instance."

2. **The persistence condition has the right form.** $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$ matches #result-persistence-condition exactly, with $\alpha_\Sigma = \eta_{\text{edge}}$. The structural parallel between epistemic and strategic persistence is not an analogy — it is a mathematical identity at the level of the sector framework.

3. **Gain collapse is the dominant failure mode.** For drifting environments, the decreasing gain $1/(n+1)$ eventually violates persistence. This gives the gain-collapse phenomenon (#emp-update-gain) a precise threshold: $n^* = R_\Sigma/\rho_\Sigma - 1$.

4. **Experience discounting resolves the failure mode.** Exponential forgetting stabilizes the gain at $1-\lambda$, with a clean persistence condition on $\lambda$.

### What it doesn't establish

1. **Multi-edge extension.** A real strategy has many edges, with correlated updates and coupled mismatch dynamics. The single-edge case has no interaction effects, no credit-assignment problem, no DAG structure. The sector condition for the multi-edge case requires vector analysis (mismatch $\delta_\Sigma \in \mathbb{R}^m$ for $m$ edges), and the correction function may not be separable across edges.

2. **Non-Bernoulli outcomes.** Continuous-valued outcomes, multi-valued signals, and partial observability all complicate the correction function. The Beta-Bernoulli case is the cleanest possible — conjugacy gives exact closed-form updates. For non-conjugate cases, the correction function is approximate (variational, particle filter, etc.), and verifying the sector condition requires additional assumptions.

3. **The stochastic Lyapunov treatment is incomplete.** The expected-value analysis suffices for the sector-condition check (which is about the correction function's structural properties), but a full stochastic persistence result would require martingale-based stability theory (supermartingale convergence, Foster-Lyapunov criteria). The expected Lyapunov analysis gives the right bound ($|\delta_\Sigma|^* \sim 1/\sqrt{n}$) but does not prove almost-sure convergence — though this is guaranteed by the Bayesian consistency theorem for the stationary case.

4. **Time-varying $n$.** In the standard Beta model, $n$ increases with each observation, so $\alpha_\Sigma$ is not constant — it decreases over time. The sector-condition framework assumes constant $\alpha$. We treated $\alpha_\Sigma = 1/(n+1)$ at the current experience level, which gives an instantaneous persistence check but not a trajectory guarantee. For the discounted model ($n_{\text{eff}}$ stabilized), the constant-$\alpha$ assumption is approximately satisfied.

5. **Connection to $\delta_{\text{strategic}}$ from #def-strategic-calibration.** The calibration residual is defined in terms of value increments ($\Delta V_O$), not raw credence errors. The mismatch $\hat{p} - \theta$ used here is a special case where value is proportional to edge reliability. For complex strategies, the mapping from credence errors to value-increment residuals involves the DAG structure and the value function's sensitivity to each edge — a potentially nonlinear transformation.

6. **The $R_\Sigma$ parameter.** "Maximum tolerable credence error" is defined here by fiat. A proper derivation would connect it to the agent's decision problem: how wrong can $\hat{p}$ be before the agent makes a suboptimal decision? For a single action $A$ with an alternative idle action, this becomes: at what credence error does the agent switch from "do $A$" to "don't do $A$" (or vice versa) when it shouldn't? This depends on the costs and payoffs, not just the edge credence — a richer model than the pure dynamics treated here.

---

## 8. Path to Promotion

To promote the strategy-persistence-schema from "proposed schema" to a segment at "draft" or higher status, the following steps are needed:

1. **Formalize the single-edge result.** This spike verifies the sector condition in the expected-value sense. A clean write-up as a segment (e.g., `single-edge-strategic-persistence.md`) would present the result with proper epistemic tags:
   - The expected sector condition: *Derived (Conditional on Beta-Bernoulli model)*
   - The persistence threshold: *Derived (Conditional on Beta-Bernoulli model + bounded drift)*
   - The gain-collapse threshold: *Derived*
   - The discounting fix: *Discussion*

2. **Address the time-varying $\alpha_\Sigma$ issue.** The sector parameter $\alpha_\Sigma = 1/(n+1)$ decreases with experience. Either: (a) re-derive the sector-condition results for time-varying $\alpha$ (standard in adaptive control — the key is that $\alpha(t)$ must be bounded below by a positive value, which fails for the undiscounted Beta), or (b) restrict to the discounted case where $\alpha_\Sigma$ stabilizes.

3. **Extend to two edges.** The minimal multi-edge case: one intermediate node $B$ between $A$ and $G$, with edges $A \to B$ and $B \to G$. This introduces edge correlation (observing $G$ success is evidence about both edges), the credit-assignment problem, and the DAG structure. If the sector condition holds for this case with appropriate vector analysis, it strongly motivates the general multi-edge result.

4. **Connect $\delta_\Sigma$ to $\delta_{\text{strategic}}$.** Show that the calibration residual from #def-strategic-calibration reduces to $|\hat{p} - \theta|$ in the single-edge case, establishing the formal bridge between the concrete mismatch used here and the general strategic mismatch defined in the theory.

5. **Stochastic Lyapunov formalization.** Replace the expected-value sector condition with a proper stochastic Lyapunov argument (supermartingale or Foster-Lyapunov). This would give almost-sure or in-probability bounds rather than expected-value bounds, and would properly account for the observation-noise contribution to steady-state mismatch.

---

## 9. Broader Significance

This spike confirms that the strategy-persistence-schema is not vacuous — the sector condition *can* be satisfied by concrete strategic update dynamics. The Beta-Bernoulli case is the simplest possible, but it establishes the structural feasibility.

The deeper insight is quantitative: **the sector parameter for strategic dynamics is the edge update gain**, $\alpha_\Sigma = \eta_{\text{edge}}$. This directly connects strategic persistence to the gain dynamics analyzed throughout Section I. In the epistemic case, the gain determines how quickly the model corrects toward reality. In the strategic case, the same gain determines how quickly edge credences correct toward truth. The unification is not merely structural (same form of persistence condition) but parametric (same quantity plays the same role).

The gain-collapse result — that experienced agents become vulnerable to drift precisely because their confidence suppresses updating — is both intuitive and quantitatively sharp. It provides a formal basis for the organizational wisdom that successful institutions can become brittle: their accumulated experience (large $n$) produces excellent performance in stable environments but catastrophic failure when conditions change.

The forgetting fix is the standard resolution, but seeing it emerge from the persistence condition as a *requirement* (rather than a heuristic) is new: the forgetting rate must satisfy $(1-\lambda) > \rho_\Sigma / R_\Sigma$, or persistence fails. This transforms "organizations should stay adaptive" from a platitude into a quantitative constraint.
