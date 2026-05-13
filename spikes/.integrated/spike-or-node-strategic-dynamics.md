# Spike: Sector Condition for OR-Node Strategic Dynamics

**Status**: Spike (investigatory). Extends the AND-node results in `spike-single-edge-strategic-dynamics.md` and `spike-two-edge-strategic-dynamics.md` to OR-nodes.

**Date**: 2026-04-02

**Objective**: Determine whether the sector condition extends to OR-node strategy DAGs. The key new phenomenon: the agent must choose which alternative to test, so untested alternatives receive zero correction. Does the persistence schema survive?

**Depends on**: #def-strategy-dag, #scope-and-or, #deriv-sector-condition, #der-observability-dominance, #hyp-edge-update-via-gain, `spike-single-edge-strategic-dynamics.md`, `spike-two-edge-strategic-dynamics.md`

---

## 1. Setup

The simplest OR structure: goal $G$ reachable via two alternative actions.

- **Action $A_1$**: reaches $G$ with true probability $\theta_1 \in (0,1)$
- **Action $A_2$**: reaches $G$ with true probability $\theta_2 \in (0,1)$
- **$G$ is an OR-node**: $G$ is achieved if either path succeeds
- **Agent's beliefs**: Beta posteriors $p_k \sim \text{Beta}(\alpha_k, \beta_k)$ with point estimates $\hat{p}_k = \alpha_k / n_k$ where $n_k = \alpha_k + \beta_k$

**Plan confidence** (OR propagation from #def-strategy-dag):

$$\hat{P}_\Sigma = 1 - (1 - p_1)(1 - p_2) = p_1 + p_2 - p_1 p_2$$

**True plan success probability**:

$$\Phi = 1 - (1 - \theta_1)(1 - \theta_2) = \theta_1 + \theta_2 - \theta_1 \theta_2$$

(assuming the agent can try both on a single trial — otherwise $\Phi = \max(\theta_1, \theta_2)$ and the plan confidence overstates by conflating "could work via either" with "will try both")

*[Definition (two-arm OR setup)]*

### 1.1 The Critical Structural Difference from AND

In an AND chain ($A \to B \to G$), executing $A$ tests edge 1 on every trial. Edge 2 gets tested only when edge 1 succeeds (the evidence-starvation effect), but it is at least probabilistically tested.

In an OR node, the agent **chooses** which action to try. On each trial:
- If $A_1$ is chosen: observe $y_1 \sim \text{Bernoulli}(\theta_1)$. Edge 1 updates. **Edge 2 receives no information.**
- If $A_2$ is chosen: observe $y_2 \sim \text{Bernoulli}(\theta_2)$. Edge 2 updates. **Edge 1 receives no information.**

The unchosen alternative's credence is frozen — this is #der-observability-dominance applied to OR alternatives. The evidence starvation is absolute (zero rate), not attenuated (rate $\times$ upstream success probability as in AND chains).

### 1.2 Mismatch State

$$\boldsymbol{\delta}_\Sigma = \begin{pmatrix} \delta_1 \\ \delta_2 \end{pmatrix} = \begin{pmatrix} p_1 - \theta_1 \\ p_2 - \theta_2 \end{pmatrix}$$

---

## 2. Correction Function Under Action Selection

On each trial, the agent selects one action according to a policy. The correction function depends on the selection policy.

### 2.1 Greedy Policy (Always Pick Highest Credence)

Suppose $p_1 > p_2$ (agent believes $A_1$ is better). The greedy policy always picks $A_1$. Then:

$$\mathbf{F}(\boldsymbol{\delta}_\Sigma) = \begin{pmatrix} \delta_1 / (n_1 + 1) \\ 0 \end{pmatrix}$$

The sector product:

$$\boldsymbol{\delta}_\Sigma^T \mathbf{F} = \frac{\delta_1^2}{n_1 + 1}$$

For the sector condition we need:

$$\frac{\delta_1^2}{n_1 + 1} \geq \alpha_\Sigma \cdot (\delta_1^2 + \delta_2^2)$$

**This fails when $\delta_2$ is large.** If $\delta_2^2 \gg \delta_1^2$, the LHS is small relative to $\|\boldsymbol{\delta}\|^2$, and no $\alpha_\Sigma > 0$ satisfies the condition uniformly.

**Result: The sector condition fails for the full 2D mismatch under a greedy policy.** The untested alternative contributes mismatch but no correction.

*[Derived (greedy sector failure)]*

### 2.2 ε-Greedy Policy (Explore with Probability ε)

Now suppose the agent explores: with probability $\varepsilon$ it tries the non-greedy arm, with probability $1 - \varepsilon$ it tries the greedy arm. Without loss of generality, assume $A_1$ is the greedy choice.

Expected correction:

$$\mathbb{E}[\mathbf{F}] = \begin{pmatrix} (1-\varepsilon) \cdot \delta_1 / (n_1 + 1) \\ \varepsilon \cdot \delta_2 / (n_2 + 1) \end{pmatrix}$$

Expected sector product:

$$\mathbb{E}[\boldsymbol{\delta}_\Sigma^T \mathbf{F}] = \frac{(1-\varepsilon)\,\delta_1^2}{n_1 + 1} + \frac{\varepsilon\,\delta_2^2}{n_2 + 1}$$

For the sector condition to hold:

$$\frac{(1-\varepsilon)\,\delta_1^2}{n_1 + 1} + \frac{\varepsilon\,\delta_2^2}{n_2 + 1} \geq \alpha_\Sigma \cdot (\delta_1^2 + \delta_2^2)$$

This must hold for all $(\delta_1, \delta_2)$. Setting $\delta_2 = 0$ gives $\alpha_\Sigma \leq (1-\varepsilon)/(n_1+1)$. Setting $\delta_1 = 0$ gives $\alpha_\Sigma \leq \varepsilon/(n_2+1)$. So:

*[Derived (OR-node sector parameter, ε-greedy)]*

$$\alpha_\Sigma = \min\!\left(\frac{1-\varepsilon}{n_1 + 1},\; \frac{\varepsilon}{n_2 + 1}\right)$$

**The sector parameter is the minimum of the greedy correction rate and the exploration correction rate.** The weakest link is the least-tested alternative.

### 2.3 Optimal Exploration Rate

Given equal experience ($n_1 = n_2 = n$), $\alpha_\Sigma$ is maximized when the two terms are equal:

$$(1-\varepsilon)/(n+1) = \varepsilon/(n+1)$$

$$\varepsilon^* = 1/2$$

Equal allocation! For equal experience, the optimal exploration rate is 50/50. This makes sense: with symmetric experience, both arms contribute equally to mismatch, so both need equal correction capacity.

For unequal experience ($n_1 \neq n_2$), balancing the two terms:

$$(1-\varepsilon)/(n_1+1) = \varepsilon/(n_2+1)$$

$$\varepsilon^* = \frac{n_1 + 1}{n_1 + n_2 + 2}$$

The optimal exploration rate allocates more trials to the arm with MORE experience (higher $n$, lower gain), because that arm's correction rate is already suppressed and needs more trials to compensate. This is counterintuitive at first — but the goal is not to learn faster about the less-tested arm, it is to *equalize the correction rates* across both arms for the sector condition.

With optimal allocation:

$$\alpha_\Sigma^* = \frac{1}{n_1 + n_2 + 2}$$

*[Derived (optimal α for equal-rate OR-node)]*

**Compare to the single-edge case:** The single-edge sector parameter is $1/(n+1)$. The OR-node with two arms and optimal exploration has $1/(n_1 + n_2 + 2)$. The correction capacity is split across the two arms — the total experience across both arms determines the sector parameter, not the experience on a single arm.

---

## 3. Persistence Condition for OR-Nodes

### 3.1 General Form

*[Derived (OR-node persistence condition)]*

$$\alpha_\Sigma > \frac{\rho_\Sigma}{R_\Sigma}$$

where $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$.

With optimal exploration and equal $n$:

$$\frac{1}{2n + 2} > \frac{\rho_\Sigma}{R_\Sigma} \quad \iff \quad n < \frac{R_\Sigma}{2\rho_\Sigma} - 1$$

**Compare to single-edge:** Single-edge persistence fails at $n^* = R_\Sigma/\rho_\Sigma - 1$. Two-arm OR-node persistence fails at $n^* = R_\Sigma/(2\rho_\Sigma) - 1$ — **half the critical experience level.** Each additional OR alternative dilutes the correction capacity.

### 3.2 The Minimum Exploration Rate

For the persistence condition to be satisfiable at all, both terms in $\alpha_\Sigma$ must exceed $\rho_\Sigma/R_\Sigma$. The binding constraint is the exploration term:

$$\frac{\varepsilon}{n_2 + 1} > \frac{\rho_\Sigma}{R_\Sigma}$$

$$\varepsilon > \frac{\rho_\Sigma (n_2 + 1)}{R_\Sigma}$$

*[Derived (minimum exploration rate for persistence)]*

**In a drifting environment, the agent MUST explore all OR alternatives at a rate proportional to the drift rate.** A purely greedy agent ($\varepsilon = 0$) cannot persist because the unchosen alternative's mismatch grows without correction until it dominates $\|\boldsymbol{\delta}_\Sigma\|$, violating the sector condition.

This is the OR-node analog of the AND-node evidence-starvation result: AND chains naturally provide attenuated testing of downstream edges; OR nodes provide ZERO testing of unchosen alternatives unless the agent deliberately explores.

### 3.3 The k-Arm Generalization

For $k$ OR alternatives with $\varepsilon$-uniform exploration (equal probability $\varepsilon/(k-1)$ for each non-greedy arm):

$$\alpha_\Sigma = \min\!\left(\frac{1 - \varepsilon}{n_{\text{greedy}} + 1},\; \min_{j \neq \text{greedy}} \frac{\varepsilon/(k-1)}{n_j + 1}\right)$$

With optimal equal-rate exploration and equal experience:

$$\alpha_\Sigma = \frac{1}{k(n+1)}$$

The sector parameter scales as $1/k$ — each additional alternative dilutes correction capacity further. The persistence condition becomes:

$$n < \frac{R_\Sigma}{k \rho_\Sigma} - 1$$

**OR nodes with many alternatives are hard to keep calibrated in drifting environments.** The correction capacity must be spread across all alternatives, and each additional alternative dilutes the effective correction rate.

---

## 4. Stationary Environment: A Different Story

### 4.1 Per-Edge Persistence is Unnecessary

In a stationary environment ($\theta_1, \theta_2$ fixed, $\rho_\Sigma = 0$), the persistence condition is trivially satisfied for any $\varepsilon > 0$. But even with $\varepsilon = 0$ (pure greedy), the agent may function well:

- If $\hat{p}_1 > \hat{p}_2$ and $\theta_1 > \theta_2$: the agent correctly identified the better arm and exploits it. Edge 2's credence is miscalibrated ($\delta_2 \neq 0$) but this doesn't affect performance.
- If $\hat{p}_1 > \hat{p}_2$ but $\theta_1 < \theta_2$: the agent made the wrong choice. But with any $\varepsilon > 0$ and stationary $\theta$, Bayesian consistency eventually corrects this.

**In the stationary case, plan-level persistence holds even when per-edge persistence fails.** The agent doesn't need to calibrate the unchosen arm — it needs to identify and exploit the best arm.

### 4.2 Connection to Satisfaction Gap / Control Regret

This is where the Section II diagnostics add value:

- **Satisfaction gap** $\delta_{\text{sat}}$: If $\max(\theta_1, \theta_2) < V_{O_t}^{\min}$, no amount of exploration helps — the world doesn't permit satisfactory performance. The agent should revise $O_t$, not explore more.
- **Control regret** $\delta_{\text{regret}}$: The gap between $\max(\theta_1, \theta_2)$ and current performance. A greedy agent that identified the best arm has $\delta_{\text{regret}} \approx 0$. An agent stuck on the wrong arm has $\delta_{\text{regret}} = \theta_{\text{best}} - \theta_{\text{chosen}}$.
- **Strategic calibration** $\delta_{\text{strategic}}$: The per-edge residuals. Even when control regret is zero (correct arm chosen), strategic calibration can be poor (unchosen arm's credence is wrong). This matters only if the environment might change (requiring re-evaluation of alternatives) or if the strategy is part of a larger composite.

The stationary OR-node reveals: **per-edge persistence is about calibration, not performance. Plan-level persistence is about performance.** These can diverge for OR-nodes in a way they cannot for AND-nodes (where every edge matters for the plan to succeed).

---

## 5. Comparison: AND vs. OR Sector Dynamics

| Property | AND chain ($A \to B \to G$) | OR node ($A_1, A_2 \to G$) |
|----------|---------------------------|----------------------------|
| Testing policy | Automatic: execute $A$, downstream edges tested if upstream succeeds | Agent-chosen: must select which alternative to test |
| Evidence starvation | Attenuated: rate $\times \prod_{j<k} \theta_j$ | Absolute: unchosen = zero rate |
| Sector parameter | $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ | $\min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ |
| Weakest link | Depth-gated (evidence starvation) | Exploration-gated (action selection) |
| Stationary persistence | Always (Bayesian consistency) | Per-edge: only with exploration. Plan-level: always (if correct arm found) |
| Drifting persistence | $n < R_\Sigma/\rho_\Sigma - 1$ (single edge) | $n < R_\Sigma/(k\rho_\Sigma) - 1$ (per arm, $k$ alternatives) |
| Failure mode | Downstream edges become stale (slow) | Unchosen alternatives become stale (total) |
| Remedy | Higher upstream reliability (increase $\theta_1$) | Minimum exploration rate (increase $\varepsilon$) |

*[Derived (AND vs OR comparison)]*

The fundamental difference: **AND-node persistence depends on the structure of the DAG (depth, upstream success rates). OR-node persistence depends on the agent's action selection policy (exploration rate).** AND-node issues are structural; OR-node issues are behavioral.

---

## 6. Plan-Level Sector Condition for OR-Nodes

Following the approach in the two-edge spike (Case 2 for unobservable intermediates): can we track the plan-level mismatch as a single scalar and get a cleaner sector condition?

### 6.1 Plan-Level Mismatch

$$\delta_{\text{plan}} = \hat{P}_\Sigma - \Phi = (p_1 + p_2 - p_1 p_2) - (\theta_1 + \theta_2 - \theta_1\theta_2)$$

Expanding:

$$\delta_{\text{plan}} = (1-\theta_2)\delta_1 + (1-\theta_1)\delta_2 - \delta_1\delta_2$$

For small per-edge mismatches, the linear approximation:

$$\delta_{\text{plan}} \approx (1-\theta_2)\delta_1 + (1-\theta_1)\delta_2$$

### 6.2 Plan-Level Correction

When $A_1$ is tried ($y_1$ observed):

$$\Delta P_\Sigma = (1-p_2)\Delta p_1 = \frac{(1-p_2)(y_1 - p_1)}{n_1+1}$$

Expected plan-level correction:

$$\mathbb{E}[\Delta\delta_{\text{plan}} \mid A_1 \text{ tried}] = \frac{-(1-p_2)\delta_1}{n_1+1}$$

Under $\varepsilon$-greedy (greedy on $A_1$):

$$\mathbb{E}[\Delta\delta_{\text{plan}}] = -\frac{(1-\varepsilon)(1-p_2)\delta_1}{n_1+1} - \frac{\varepsilon(1-p_1)\delta_2}{n_2+1}$$

### 6.3 The Sector Condition at Plan Level

For the sector product $\delta_{\text{plan}} \cdot F_{\text{plan}}$, where $F_{\text{plan}} = -\mathbb{E}[\Delta\delta_{\text{plan}}]$:

Using the linear approximation $\delta_{\text{plan}} \approx (1-\theta_2)\delta_1 + (1-\theta_1)\delta_2$ and $F_{\text{plan}} \approx (1-\varepsilon)(1-\theta_2)\delta_1/(n_1+1) + \varepsilon(1-\theta_1)\delta_2/(n_2+1)$:

$$\delta_{\text{plan}} \cdot F_{\text{plan}} = \left[(1-\theta_2)\delta_1 + (1-\theta_1)\delta_2\right] \cdot \left[\frac{(1-\varepsilon)(1-\theta_2)\delta_1}{n_1+1} + \frac{\varepsilon(1-\theta_1)\delta_2}{n_2+1}\right]$$

This expands to a quadratic form in $(\delta_1, \delta_2)$. The sector condition $\delta_{\text{plan}} \cdot F_{\text{plan}} \geq \alpha \cdot \delta_{\text{plan}}^2$ is equivalent to asking whether the quadratic form is bounded below by $\alpha$ times the squared linear form.

**This does not simplify to a clean scalar sector condition.** Unlike AND-node plan confidence ($P_\Sigma = p_1 p_2$, which is multiplicative and gives a Beta-like plan-level update), the OR formula ($P_\Sigma = p_1 + p_2 - p_1p_2$) is additive with a cross term, and the plan-level dynamics inherit the nonlinear coupling.

**Result: Plan-level tracking for OR-nodes does not yield a clean scalar sector condition.** The per-dimension approach (with exploration) is the natural framework.

*[Derived (plan-level does not simplify for OR)]*

---

## 7. Summary and Implications for the Persistence Schema

### What this spike establishes

1. **OR-nodes require deliberate exploration for per-edge persistence.** A greedy agent cannot satisfy the sector condition for the full mismatch vector because the unchosen alternative receives zero correction. This is a fundamental structural difference from AND-nodes.

2. **The sector condition holds with $\varepsilon$-greedy exploration.** The sector parameter is $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$, gated by the exploration rate rather than by depth as in AND chains.

3. **The minimum exploration rate is $\varepsilon > \rho_\Sigma(n_{\max}+1)/R_\Sigma$.** In drifting environments, the agent must allocate correction capacity to all alternatives proportional to the drift rate. Pure exploitation fails.

4. **The sector parameter scales as $1/k$ with $k$ alternatives.** More alternatives dilute the correction rate. The persistence condition becomes harder with wider OR-nodes. This creates structural pressure toward **pruning unpromising alternatives** — a principled basis for the common-sense observation that too many options paralyze decision-making.

5. **Per-edge persistence and plan-level persistence diverge for OR-nodes.** In stationary environments, an agent can have excellent plan-level performance (correct arm chosen, low control regret) while having poor strategic calibration (unchosen arms miscalibrated). This divergence does not occur for AND-nodes (where every edge matters for the plan).

6. **Plan-level sector analysis does not simplify for OR-nodes** the way it does for AND-nodes. The OR propagation formula's additive structure prevents clean scalar reduction.

### Implications for the strategy-persistence-schema

The schema's form ($\alpha_\Sigma > \rho_\Sigma/R_\Sigma$) is confirmed for OR-nodes, with the crucial caveat that **$\alpha_\Sigma$ depends on the action selection policy, not just the update dynamics.** This means the schema's conditions need an additional requirement:

- **(SA3) Sufficient exploration**: For OR-nodes, the action selection policy must allocate correction capacity to all alternatives at a rate exceeding $\rho_\Sigma/R_\Sigma$.

This is a new condition not present in the AND-node cases. It connects the strategy-persistence schema to the exploration-exploitation tradeoff (#disc-ciy-unified-objective) — exploration is not just about learning, it is about maintaining the sector condition for strategic persistence.

### Verified instances (updated)

| Case | Node type | Sector condition | $\alpha_\Sigma$ | Notes |
|------|-----------|-----------------|------------------|-------|
| 1. Single edge | — | Satisfied globally | $1/(n+1)$ | Tight bound (linear correction) |
| 2. Two-edge chain, $B$ observable | AND | Satisfied globally | $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ | Evidence starvation for edge 2 |
| 3. Two-edge chain, $B$ unobservable | AND | Per-edge fails; plan-level OK | $1/(n_\Phi+1)$ (plan) | Bias $O(1/n)$ per-edge |
| **4. Two-arm OR, $\varepsilon$-greedy** | **OR** | **Satisfied (with exploration)** | $\min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ | **Exploration-gated, not depth-gated** |

---

## 8. Open Questions

1. **Mixed AND/OR DAGs.** Real strategies combine AND and OR nodes. The sector parameter for a mixed DAG will involve both evidence-starvation (AND) and exploration-gating (OR) effects. Is the weakest-link principle sufficient, or do interactions between AND and OR nodes create new phenomena?

2. **Adaptive exploration.** The $\varepsilon$-greedy analysis uses a fixed exploration rate. Adaptive strategies (UCB, Thompson sampling, Bayesian optimization) allocate exploration based on current uncertainty. These should give tighter sector bounds — the agent explores where correction is most needed — but the analysis is more complex because the correction function depends on the mismatch state itself.

3. **OR-nodes with shared observations.** If trying $A_1$ gives partial information about $A_2$ (e.g., they share a common prerequisite), the absolute evidence starvation softens. This is analogous to correlated channels in the tempo redundancy analysis.

4. **Stochastic Lyapunov treatment.** As with the AND cases, a full stochastic treatment (Foster-Lyapunov or supermartingale) would give probability bounds rather than expected-value bounds.

5. **The pruning threshold.** If the sector parameter scales as $1/k$, there is a maximum number of alternatives the agent can maintain: $k_{\max} = R_\Sigma / (\rho_\Sigma(n+1))$. Beyond this, the agent should prune the least-promising alternatives to concentrate correction capacity. What determines which alternatives to prune?
