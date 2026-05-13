# Spike: Sector Condition for Two-Edge Strategic Dynamics (A→B→G)

**Status**: Spike (investigatory). Extends `spike-single-edge-strategic-dynamics.md` to the minimal multi-edge case.

**Date**: 2026-04-01

**Objective**: Determine whether the sector condition extends from a single strategy edge to a two-edge chain A→B→G. The key new phenomena are: vector mismatch (two edges = two-dimensional mismatch), credit assignment (attributing outcomes to specific edges), and the observable vs. unobservable intermediate node distinction.

**Depends on**: #def-strategy-dag, #def-strategic-calibration, #der-chain-confidence-decay, #scope-and-or, #deriv-sector-condition, #der-observability-dominance, #hyp-edge-update-via-gain, `spike-single-edge-strategic-dynamics.md`

---

## 1. Setup

Consider a two-step strategy: action $A$ leads to intermediate state $B$, which leads to goal $G$. The strategy DAG is $A \to B \to G$ with two edges.

- **Node B is AND**: both edges must succeed for $G$ to be achieved. (This is the chain semantics from #scope-and-or — a linear chain is the degenerate AND case where each node has exactly one parent.)
- **Edge credences**: $p_1 = p_{AB}$ (agent's belief that executing $A$ successfully advances $B$), $p_2 = p_{BG}$ (agent's belief that achieving $B$ advances $G$).
- **True probabilities**: $\theta_1 = \theta_{AB}$, $\theta_2 = \theta_{BG}$, both in $(0, 1)$.
- **Plan confidence**: $\hat{P}_\Sigma = p_1 \cdot p_2$ (AND-node propagation from #def-strategy-dag).
- **True success probability**: $\theta_\Sigma = \theta_1 \cdot \theta_2$ (assuming edge independence).

The agent executes $A$, potentially observes the status of $B$, and observes whether $G$ is achieved.

*[Definition (two-edge setup)]*

### 1.1 Mismatch State

The mismatch is now a vector:

$$\boldsymbol{\delta}_\Sigma = \begin{pmatrix} \delta_1 \\ \delta_2 \end{pmatrix} = \begin{pmatrix} p_1 - \theta_1 \\ p_2 - \theta_2 \end{pmatrix} \in \mathbb{R}^2$$

The sector condition requires:

$$\boldsymbol{\delta}_\Sigma^T \mathbf{F}(\boldsymbol{\delta}_\Sigma) \geq \alpha_\Sigma \|\boldsymbol{\delta}_\Sigma\|^2$$

where $\mathbf{F}: \mathbb{R}^2 \to \mathbb{R}^2$ is the expected correction function and $\|\boldsymbol{\delta}_\Sigma\|^2 = \delta_1^2 + \delta_2^2$.

### 1.2 Observation Model

The agent has access to two potential observation channels:

1. **$G$-observation**: always available. The agent observes $y_G \in \{0, 1\}$ — whether the goal was achieved.
2. **$B$-observation**: available only when $B$ is observable. The agent observes $y_B \in \{0, 1\}$ — whether the intermediate state was reached.

The generative model:

$$y_B \sim \text{Bernoulli}(\theta_1)$$

$$y_G \mid y_B \sim \begin{cases} \text{Bernoulli}(\theta_2) & \text{if } y_B = 1 \\ 0 & \text{if } y_B = 0 \end{cases}$$

So $y_G = y_B \cdot z$ where $z \sim \text{Bernoulli}(\theta_2)$ independent of $y_B$. The joint distribution:

| $y_B$ | $y_G$ | Probability |
|-------|-------|-------------|
| 0 | 0 | $1 - \theta_1$ |
| 1 | 0 | $\theta_1(1 - \theta_2)$ |
| 1 | 1 | $\theta_1 \theta_2$ |

Note: $y_B = 0, y_G = 1$ has probability zero (cannot reach $G$ without $B$ — the AND-chain constraint).

---

## 2. Case 1: Observable Intermediate (B is Observable)

When $B$ is observable, the agent observes both $y_B$ and $y_G$ on each trial. This cleanly separates the two edges.

### 2.1 Independent Updates

**Edge 1 update** ($A \to B$): The agent observes $y_B$ directly. This is a Bernoulli observation of edge 1's success, exactly as in the single-edge spike. With Beta posterior $\text{Beta}(\alpha_1, \beta_1)$ and total pseudo-count $n_1 = \alpha_1 + \beta_1$:

$$\Delta p_1 = \frac{y_B - p_1}{n_1 + 1}$$

**Edge 2 update** ($B \to G$): The agent observes $y_G$ conditional on $y_B$. When $y_B = 1$ (intermediate achieved), the agent observes whether $G$ followed — a direct Bernoulli test of edge 2. When $y_B = 0$ ($B$ not reached), the agent gets no information about edge 2 (the edge was never "activated"). With Beta posterior $\text{Beta}(\alpha_2, \beta_2)$ and total pseudo-count $n_2 = \alpha_2 + \beta_2$:

$$\Delta p_2 = \begin{cases} \frac{y_G - p_2}{n_2 + 1} & \text{if } y_B = 1 \\ 0 & \text{if } y_B = 0 \end{cases}$$

*[Derived (observable-intermediate updates)]*

**Critical observation.** Edge 2 updates only when edge 1 succeeds. The effective observation rate for edge 2 is $\theta_1$ (the true success rate of edge 1). When $\theta_1$ is small, edge 2 rarely gets tested, and its pseudo-count $n_2$ grows slowly. This is the chain's credit-assignment advantage: clean attribution, but at the cost of slower learning for downstream edges.

### 2.2 Expected Correction Function

The expected correction for each edge:

**Edge 1** (updates every trial):

$$\mathbb{E}[\Delta p_1] = \frac{\theta_1 - p_1}{n_1 + 1} = -\frac{\delta_1}{n_1 + 1}$$

So $F_1(\delta_1) = \delta_1 / (n_1 + 1)$.

**Edge 2** (updates only when $y_B = 1$):

$$\mathbb{E}[\Delta p_2] = \theta_1 \cdot \frac{\theta_2 - p_2}{n_2 + 1} + (1 - \theta_1) \cdot 0 = -\frac{\theta_1 \cdot \delta_2}{n_2 + 1}$$

So $F_2(\delta_2) = \theta_1 \cdot \delta_2 / (n_2 + 1)$.

*[Derived (expected correction, observable intermediate)]*

**The correction function is diagonal:**

$$\mathbf{F}(\boldsymbol{\delta}_\Sigma) = \begin{pmatrix} \delta_1 / (n_1 + 1) \\ \theta_1 \cdot \delta_2 / (n_2 + 1) \end{pmatrix}$$

### 2.3 Sector Condition Verification

*[Derived (sector condition, observable intermediate)]*

$$\boldsymbol{\delta}_\Sigma^T \mathbf{F}(\boldsymbol{\delta}_\Sigma) = \frac{\delta_1^2}{n_1 + 1} + \frac{\theta_1 \cdot \delta_2^2}{n_2 + 1}$$

We need this to be $\geq \alpha_\Sigma (\delta_1^2 + \delta_2^2)$ for some $\alpha_\Sigma > 0$. This holds with:

$$\alpha_\Sigma = \min\left(\frac{1}{n_1 + 1},\; \frac{\theta_1}{n_2 + 1}\right)$$

**The sector condition is satisfied.** The sector parameter is the minimum of the two per-edge effective correction rates.

### 2.4 The Weakest-Link Structure

The two per-edge correction rates are:

- Edge 1: $\alpha_1 = 1/(n_1 + 1)$ — same as the single-edge case.
- Edge 2: $\alpha_2 = \theta_1 / (n_2 + 1)$ — attenuated by $\theta_1$.

The overall $\alpha_\Sigma = \min(\alpha_1, \alpha_2)$ is a **weakest-link** result: the system's correction rate is limited by the slowest-correcting edge.

**The $\theta_1$ attenuation is the key new phenomenon.** Edge 2's effective correction rate is reduced by a factor of $\theta_1$ compared to its stand-alone rate. This is because edge 2 only gets tested when edge 1 succeeds (with probability $\theta_1$). If $\theta_1$ is small (first step rarely succeeds), edge 2 learns very slowly — it is effectively starved of evidence.

This gives a precise mechanism for the chain-confidence-decay observation (#der-chain-confidence-decay): longer chains are not just less confident, they are harder to calibrate. Each edge downstream of an unreliable upstream edge receives observations at a reduced rate, proportional to the product of all upstream success probabilities.

### 2.5 Generalization to Depth-$d$ Chains

For a chain of depth $d$ with observable intermediates, the same argument applies inductively. Edge $k$ (from node $k-1$ to node $k$) gets tested only when all upstream edges succeed. The effective correction rate for edge $k$:

$$\alpha_k = \frac{\prod_{j=1}^{k-1} \theta_j}{n_k + 1}$$

The overall sector parameter:

$$\alpha_\Sigma = \min_{k=1}^{d} \alpha_k = \min_{k=1}^{d} \frac{\prod_{j=1}^{k-1} \theta_j}{n_k + 1}$$

*[Derived (depth-$d$ chain sector parameter, observable intermediates)]*

The deepest edge is typically the bottleneck (smallest numerator), confirming the qualitative prediction of #der-chain-confidence-decay and #der-observability-dominance: deep chains are fragile because downstream edges cannot be calibrated efficiently.

### 2.6 Persistence Condition (Observable Intermediate)

Applying the persistence condition from #deriv-sector-condition:

$$\alpha_\Sigma > \frac{\rho_\Sigma}{R_\Sigma}$$

$$\min\left(\frac{1}{n_1 + 1},\; \frac{\theta_1}{n_2 + 1}\right) > \frac{\rho_\Sigma}{R_\Sigma}$$

*[Derived (two-edge persistence condition, observable intermediate)]*

This decomposes into two independent conditions (both must hold):

1. $n_1 < R_\Sigma / \rho_\Sigma - 1$ (same as single-edge)
2. $n_2 < \theta_1 \cdot R_\Sigma / \rho_\Sigma - 1$ (tighter by factor $\theta_1$)

**The downstream edge has a stricter persistence bound.** For the same drift rate $\rho_\Sigma$ and reserve $R_\Sigma$, edge 2 hits its persistence limit earlier (at lower $n_2$) because its effective gain is attenuated. If $\theta_1 = 0.5$, edge 2's critical experience level is halved relative to a stand-alone edge.

**Gain collapse hits downstream edges first.** This is a prediction about multi-step strategies: in drifting environments, the later steps of a sequential plan become uncalibratable before the earlier steps do. The agent should either shorten its plan (reduce depth) or increase observability of intermediates (faster testing of downstream edges via exploration).

---

## 3. Case 2: Unobservable Intermediate (B is Not Observable)

When $B$ is not observable, the agent observes only $y_G \in \{0, 1\}$ — the final outcome. It cannot distinguish between "A→B failed" and "B→G failed" when $y_G = 0$.

This is the credit-assignment problem in its purest form.

### 3.1 The Observation

The agent sees:

$$y_G \sim \text{Bernoulli}(\theta_1 \theta_2)$$

A single binary observation about the product $\theta_1 \theta_2$. There are three possible underlying causes of failure ($y_G = 0$):

1. Edge 1 failed ($y_B = 0$): probability $1 - \theta_1$
2. Edge 2 failed ($y_B = 1, y_G = 0$): probability $\theta_1(1 - \theta_2)$
3. Both failed: subsumed by case 1 (if $B$ is not reached, edge 2 is never tested)

### 3.2 Bayesian Update (Joint Posterior)

The correct Bayesian approach: maintain a joint posterior $\pi(\theta_1, \theta_2 \mid \text{data})$ and update it on each observation of $y_G$.

**Prior.** Assume independent Beta priors: $\theta_1 \sim \text{Beta}(\alpha_1, \beta_1)$, $\theta_2 \sim \text{Beta}(\alpha_2, \beta_2)$. The prior is $\pi(\theta_1, \theta_2) = \text{Beta}(\theta_1; \alpha_1, \beta_1) \cdot \text{Beta}(\theta_2; \alpha_2, \beta_2)$.

**Likelihood.** $P(y_G = 1 \mid \theta_1, \theta_2) = \theta_1 \theta_2$, $P(y_G = 0 \mid \theta_1, \theta_2) = 1 - \theta_1 \theta_2$.

**Posterior after observing $y_G = 1$:**

$$\pi(\theta_1, \theta_2 \mid y_G = 1) \propto \theta_1 \theta_2 \cdot \pi(\theta_1, \theta_2) \propto \theta_1^{\alpha_1} \theta_2^{\alpha_2} (1-\theta_1)^{\beta_1 - 1} (1-\theta_2)^{\beta_2 - 1}$$

This factors as $\text{Beta}(\theta_1; \alpha_1 + 1, \beta_1) \cdot \text{Beta}(\theta_2; \alpha_2 + 1, \beta_2)$. That is: success credits both edges equally, incrementing both $\alpha$ counts by 1. The posterior remains a product of independent Betas.

*[Derived (posterior after success, unobservable intermediate)]*

**Posterior after observing $y_G = 0$:**

$$\pi(\theta_1, \theta_2 \mid y_G = 0) \propto (1 - \theta_1 \theta_2) \cdot \pi(\theta_1, \theta_2)$$

The factor $(1 - \theta_1 \theta_2)$ does NOT factor into a function of $\theta_1$ alone times a function of $\theta_2$ alone. The posterior is **no longer a product of independent Betas.** Failure introduces correlation between the edge beliefs.

*[Derived (posterior after failure, unobservable intermediate)]*

**This is the fundamental asymmetry.** Success decomposes cleanly (both edges contributed, both get credit). Failure does not decompose (which edge failed?) and introduces posterior correlation.

### 3.3 The Non-Conjugacy Problem

After a single failure, the joint posterior is:

$$\pi(\theta_1, \theta_2 \mid y_G = 0) \propto (1 - \theta_1\theta_2) \cdot \theta_1^{\alpha_1 - 1}(1-\theta_1)^{\beta_1 - 1} \cdot \theta_2^{\alpha_2 - 1}(1-\theta_2)^{\beta_2 - 1}$$

This is not a standard distribution. After multiple failures, each introduces another $(1 - \theta_1\theta_2)$ factor, creating a polynomial mixture that grows in complexity. **The exact Bayesian posterior is intractable** for repeated updating — it is not in any standard conjugate family.

In practice, the agent must approximate. The natural approximation strategies:

1. **Moment matching**: project the true posterior back onto independent Betas after each update (expectation propagation / assumed density filtering)
2. **Marginal updating**: update each edge's marginal posterior independently, ignoring the correlation
3. **Proportional credit**: attribute failure proportionally to the agent's current beliefs about which edge is likely responsible

We analyze each approximation and its sector-condition implications.

### 3.4 Approximation 1: Marginal Bayesian Update

Compute the marginal expected update for each edge's point estimate.

**Point estimates.** The agent's point estimates are $p_1 = \alpha_1/n_1$ and $p_2 = \alpha_2/n_2$ (with $n_k = \alpha_k + \beta_k$).

**Expected update for $p_1$.** We need $\mathbb{E}[p_1^{\text{new}} - p_1]$.

On success ($y_G = 1$, probability $\theta_1 \theta_2$): from §3.2, both $\alpha$ counts increment. So $p_1^{\text{new}} = (\alpha_1 + 1)/(n_1 + 1)$, giving:

$$\Delta p_1^{(\text{success})} = \frac{\alpha_1 + 1}{n_1 + 1} - \frac{\alpha_1}{n_1} = \frac{1 - p_1}{n_1 + 1}$$

On failure ($y_G = 0$, probability $1 - \theta_1\theta_2$): the exact Bayesian update is intractable. Consider the **proportional-blame** approximation: the agent asks "given failure, what's the probability each edge was responsible?" and updates accordingly.

**Probability that edge 1 caused the failure** (given $y_G = 0$, using the agent's beliefs):

$$q_1 = P(y_B = 0 \mid y_G = 0) = \frac{P(y_G = 0 \mid y_B = 0) P(y_B = 0)}{P(y_G = 0)} = \frac{(1 - p_1)}{1 - p_1 p_2}$$

**Probability that edge 2 caused the failure** (given $y_G = 0$, $y_B = 1$):

$$q_2 = P(y_B = 1, z = 0 \mid y_G = 0) = \frac{p_1(1 - p_2)}{1 - p_1 p_2}$$

Note: $q_1 + q_2 = 1$ (exhaustive partition of failure causes under the AND-chain model).

Under proportional blame, the agent updates edge $k$'s $\beta$ count by $q_k$ (fractional count):

$$\alpha_1 \to \alpha_1, \quad \beta_1 \to \beta_1 + q_1 \quad \text{(failure attributed to edge 1 with weight } q_1\text{)}$$

$$\alpha_2 \to \alpha_2, \quad \beta_2 \to \beta_2 + q_2 \quad \text{(failure attributed to edge 2 with weight } q_2\text{)}$$

*[Formulation (proportional-blame update, unobservable intermediate)]*

This gives:

$$\Delta p_1^{(\text{failure})} = \frac{\alpha_1}{n_1 + q_1} - \frac{\alpha_1}{n_1} = -\frac{\alpha_1 q_1}{n_1(n_1 + q_1)} \approx -\frac{p_1 q_1}{n_1 + 1}$$

(using $q_1 \leq 1$ and $n_1 + q_1 \approx n_1 + 1$ for the approximation, which is tight for $n_1 \gg 1$).

Similarly:

$$\Delta p_2^{(\text{failure})} \approx -\frac{p_2 q_2}{n_2 + 1}$$

### 3.5 Expected Correction (Proportional-Blame Approximation)

*[Derived (expected correction, unobservable intermediate, proportional-blame)]*

Combining success and failure cases:

$$\mathbb{E}[\Delta p_1] = \theta_1 \theta_2 \cdot \frac{1 - p_1}{n_1 + 1} + (1 - \theta_1 \theta_2) \cdot \left(-\frac{p_1 q_1}{n_1 + 1}\right)$$

$$= \frac{1}{n_1 + 1}\left[\theta_1\theta_2(1 - p_1) - (1 - \theta_1\theta_2) p_1 q_1\right]$$

Now substitute $q_1 = (1 - p_1)/(1 - p_1 p_2)$:

$$= \frac{1}{n_1 + 1}\left[\theta_1\theta_2(1 - p_1) - (1 - \theta_1\theta_2) \cdot \frac{p_1(1 - p_1)}{1 - p_1 p_2}\right]$$

$$= \frac{1 - p_1}{n_1 + 1}\left[\theta_1\theta_2 - \frac{(1 - \theta_1\theta_2) p_1}{1 - p_1 p_2}\right]$$

This is messy. Let us evaluate the expression directly by writing $\Phi = \theta_1 \theta_2$ (true joint success) and $\hat{\Phi} = p_1 p_2$ (estimated joint success):

$$\mathbb{E}[\Delta p_1] = \frac{1}{n_1 + 1}\left[\Phi(1 - p_1) - (1 - \Phi) \cdot \frac{p_1(1 - p_1)}{1 - \hat{\Phi}}\right]$$

$$= \frac{1 - p_1}{n_1 + 1}\left[\Phi - \frac{(1 - \Phi) p_1}{1 - \hat{\Phi}}\right]$$

$$= \frac{1 - p_1}{n_1 + 1} \cdot \frac{\Phi(1 - \hat{\Phi}) - (1 - \Phi)p_1}{1 - \hat{\Phi}}$$

The numerator simplifies:

$$\Phi(1 - \hat{\Phi}) - (1 - \Phi)p_1 = \Phi - \Phi\hat{\Phi} - p_1 + \Phi p_1 = \Phi(1 + p_1 - \hat{\Phi}) - p_1$$

$$= \theta_1\theta_2(1 + p_1 - p_1 p_2) - p_1$$

This does not simplify to a clean function of $\delta_1 = p_1 - \theta_1$ alone. The correction for edge 1 depends on both edges' credences and both true values. **The correction function is coupled — each edge's expected correction depends on the other edge's state.**

### 3.6 Checking Alignment at Truth

At truth ($p_1 = \theta_1$, $p_2 = \theta_2$, so $\hat{\Phi} = \Phi$):

$$\mathbb{E}[\Delta p_1]\big|_{p=\theta} = \frac{1 - \theta_1}{n_1 + 1}\cdot \frac{\Phi(1 - \Phi) - (1 - \Phi)\theta_1}{1 - \Phi}$$

$$= \frac{1 - \theta_1}{n_1 + 1}\cdot \frac{(1 - \Phi)(\Phi - \theta_1)}{1 - \Phi} = \frac{1 - \theta_1}{n_1 + 1}\cdot (\Phi - \theta_1)$$

Wait — at truth, $\Phi = \theta_1 \theta_2$, so $\Phi - \theta_1 = \theta_1(\theta_2 - 1)$:

$$= \frac{1 - \theta_1}{n_1 + 1} \cdot \theta_1(\theta_2 - 1) = -\frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1 + 1}$$

**This is NOT zero.** At truth ($\delta_1 = \delta_2 = 0$), the expected correction for edge 1 is negative (pushing $p_1$ downward). This violates (A1): $F(\boldsymbol{0}) \neq \boldsymbol{0}$.

*[Derived (A1 violation under proportional blame)]*

**This is a serious problem.** The proportional-blame approximation introduces systematic bias. Even when the agent's beliefs are perfectly calibrated, the update rule pushes credences away from truth. The bias arises because the blame-assignment uses the agent's current beliefs ($p_1, p_2$) as point estimates for the true probabilities, but the nonlinear coupling through $(1 - p_1 p_2)$ creates a Jensen's-inequality-type bias.

**Diagnosis.** The issue is that on failure, the proportional blame $q_1 = (1-p_1)/(1-p_1 p_2)$ uses the agent's point estimates. At truth, with $p_k = \theta_k$, the blame attributions are correct *on average*. But the success case increments $\alpha_1$ by exactly 1, while the failure case increments $\beta_1$ by the fractional weight $q_1 < 1$. The total expected pseudo-count increment per trial is $\theta_1\theta_2 \cdot 1 + (1-\theta_1\theta_2) \cdot q_1$, and the expected $\alpha$ increment is $\theta_1\theta_2 \cdot 1$. At truth, the ratio $\alpha / (\alpha + \beta)$ should remain at $\theta_1$, but the fractional blame assignment distorts this.

Let me recompute more carefully. After one trial starting from truth ($p_1 = \theta_1$):

- On success (prob $\theta_1\theta_2$): $\alpha_1 \to \alpha_1 + 1$. New $p_1 = (\alpha_1 + 1)/(n_1 + 1) = (\theta_1 n_1 + 1)/(n_1 + 1)$.
  - Change: $\Delta p_1 = (1 - \theta_1)/(n_1 + 1)$.
- On failure (prob $1 - \theta_1\theta_2$): $\beta_1 \to \beta_1 + q_1$. New $p_1 = \alpha_1/(n_1 + q_1)$.
  - At truth: $q_1 = (1 - \theta_1)/(1 - \theta_1\theta_2)$.
  - Change: $\Delta p_1 = \theta_1 n_1/(n_1 + q_1) - \theta_1 = -\theta_1 q_1/(n_1 + q_1) \approx -\theta_1 q_1 / n_1$ for large $n_1$.

Expected change:

$$\mathbb{E}[\Delta p_1] \approx \theta_1\theta_2 \cdot \frac{1 - \theta_1}{n_1 + 1} - (1 - \theta_1\theta_2) \cdot \frac{\theta_1 q_1}{n_1}$$

$$= \theta_1\theta_2 \cdot \frac{1-\theta_1}{n_1} - (1-\theta_1\theta_2) \cdot \frac{\theta_1(1-\theta_1)}{n_1(1-\theta_1\theta_2)}$$

$$= \frac{\theta_1(1-\theta_1)}{n_1}\left[\theta_2 - 1\right] = -\frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1}$$

This confirms the bias: **at truth, the proportional-blame update systematically pushes $p_1$ downward** at rate $\theta_1(1-\theta_1)(1-\theta_2)/n_1$. By symmetry, $p_2$ is also pushed downward. The agent becomes systematically pessimistic about both edges.

**The bias is $O(1/n)$ — it vanishes as the agent accumulates experience.** But it is not zero, and it violates the fundamental requirement (A1) of the sector-condition framework.

### 3.7 Exact Marginal Bayesian Update

The proportional-blame approximation is biased. What about the exact marginal Bayesian update?

The exact posterior marginal for $\theta_1$ after observing $y_G$ is:

$$\pi(\theta_1 \mid y_G) = \int_0^1 \pi(\theta_1, \theta_2 \mid y_G) \, d\theta_2$$

**After success ($y_G = 1$):**

$$\pi(\theta_1 \mid y_G = 1) \propto \theta_1^{\alpha_1}(1-\theta_1)^{\beta_1 - 1} \int_0^1 \theta_2^{\alpha_2}(1-\theta_2)^{\beta_2-1} d\theta_2$$

The integral is $B(\alpha_2+1, \beta_2)/B(\alpha_2, \beta_2) = \alpha_2/(\alpha_2+\beta_2)$. It's a constant with respect to $\theta_1$, so:

$$\pi(\theta_1 \mid y_G = 1) = \text{Beta}(\theta_1; \alpha_1 + 1, \beta_1)$$

The marginal update for $\theta_1$ on success is exactly: $\alpha_1 \to \alpha_1 + 1$. Same as the proportional-blame case.

**After failure ($y_G = 0$):**

$$\pi(\theta_1 \mid y_G = 0) \propto (1 - \theta_1\theta_2) \cdot \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1} \cdot \theta_2^{\alpha_2-1}(1-\theta_2)^{\beta_2-1}$$

Integrating out $\theta_2$:

$$\pi(\theta_1 \mid y_G = 0) \propto \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1} \int_0^1 (1-\theta_1\theta_2) \theta_2^{\alpha_2-1}(1-\theta_2)^{\beta_2-1} d\theta_2$$

$$= \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1}\left[1 - \theta_1 \cdot \frac{\alpha_2}{\alpha_2+\beta_2}\right]$$

$$= \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1}(1 - \theta_1 \bar{p}_2)$$

where $\bar{p}_2 = \alpha_2/n_2$ is the prior mean for edge 2.

This is NOT a Beta distribution — the factor $(1 - \theta_1 \bar{p}_2)$ is an extra polynomial in $\theta_1$. The marginal posterior for $\theta_1$ has the form:

$$\pi(\theta_1 \mid y_G = 0) \propto \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1} - \bar{p}_2 \cdot \theta_1^{\alpha_1}(1-\theta_1)^{\beta_1-1}$$

This is a mixture of two Beta kernels: $\text{Beta}(\alpha_1, \beta_1)$ and $\text{Beta}(\alpha_1+1, \beta_1)$.

*[Derived (marginal posterior after failure)]*

$$\pi(\theta_1 \mid y_G = 0) = (1 - w) \cdot \text{Beta}(\alpha_1, \beta_1) + w \cdot \text{Beta}(\alpha_1 + 1, \beta_1)$$

Wait — that's not right either. Let me be more careful. We have:

$$\pi(\theta_1 \mid y_G = 0) \propto \theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1}(1 - \bar{p}_2 \theta_1)$$

Rewrite $1 - \bar{p}_2\theta_1 = (1 - \bar{p}_2) + \bar{p}_2(1-\theta_1)$:

$$\propto (1-\bar{p}_2)\,\theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1-1} + \bar{p}_2\,\theta_1^{\alpha_1-1}(1-\theta_1)^{\beta_1}$$

This is a mixture of $\text{Beta}(\alpha_1, \beta_1)$ and $\text{Beta}(\alpha_1, \beta_1+1)$, with unnormalized weights $(1-\bar{p}_2) B(\alpha_1, \beta_1)$ and $\bar{p}_2 B(\alpha_1, \beta_1+1)$.

The normalized mixture weight for the $\text{Beta}(\alpha_1, \beta_1+1)$ component is:

$$w = \frac{\bar{p}_2 \cdot B(\alpha_1, \beta_1+1)}{(1-\bar{p}_2) \cdot B(\alpha_1, \beta_1) + \bar{p}_2 \cdot B(\alpha_1, \beta_1+1)}$$

Using $B(\alpha_1, \beta_1+1) = B(\alpha_1, \beta_1) \cdot \beta_1/(\alpha_1+\beta_1) = B(\alpha_1, \beta_1) \cdot \beta_1/n_1$:

$$w = \frac{\bar{p}_2 \cdot \beta_1/n_1}{(1-\bar{p}_2) + \bar{p}_2 \cdot \beta_1/n_1} = \frac{\bar{p}_2 \beta_1}{\bar{p}_2 \beta_1 + (1-\bar{p}_2)n_1}$$

Since $\beta_1/n_1 = 1 - p_1$:

$$w = \frac{\bar{p}_2(1-p_1)}{\bar{p}_2(1-p_1) + (1-\bar{p}_2)} = \frac{p_2(1-p_1)}{1 - p_1 p_2}$$

(using $\bar{p}_2 = p_2$ as the agent's current point estimate).

**This is exactly $q_2$ from §3.4** — the probability that edge 2 caused the failure, given the agent's beliefs. So the exact marginal posterior is:

*[Derived (exact marginal posterior structure)]*

$$\pi(\theta_1 \mid y_G = 0) = (1 - q_2)\,\text{Beta}(\alpha_1, \beta_1) + q_2\,\text{Beta}(\alpha_1, \beta_1+1)$$

$$= q_1\,\text{Beta}(\alpha_1, \beta_1) + q_2\,\text{Beta}(\alpha_1, \beta_1+1)$$

**Interpretation.** With probability $q_1 = (1-p_1)/(1-p_1 p_2)$ (blame on edge 1), the edge-1 belief absorbs the failure ($\beta_1$ increments). With probability $q_2 = p_1(1-p_2)/(1-p_1 p_2)$ (blame on edge 2), the edge-1 belief is unchanged. The exact marginal posterior IS the proportional-blame update, but expressed as a mixture rather than a fractional count.

The **marginal mean** of this mixture:

$$\mathbb{E}[\theta_1 \mid y_G = 0] = q_1 \cdot \frac{\alpha_1}{n_1+1} + q_2 \cdot \frac{\alpha_1}{n_1} = \alpha_1 \left(\frac{q_1}{n_1+1} + \frac{q_2}{n_1}\right)$$

$$= \alpha_1 \cdot \frac{q_1 n_1 + q_2(n_1+1)}{n_1(n_1+1)} = \alpha_1 \cdot \frac{n_1 + q_2}{n_1(n_1+1)} = p_1 \cdot \frac{n_1 + q_2}{n_1+1}$$

So:

$$\Delta p_1^{(\text{failure, exact})} = p_1 \cdot \frac{n_1 + q_2}{n_1+1} - p_1 = p_1 \cdot \frac{q_2 - 1}{n_1+1} = -\frac{p_1 q_1}{n_1+1}$$

This is the same formula as the proportional-blame approximation in §3.4 (without the large-$n$ approximation error). So **the proportional-blame fractional-count update is exactly the marginal Bayesian point-estimate update** for the mean of the exact posterior.

### 3.8 Revisiting A1: Does the Exact Marginal Satisfy Zero-Correction-at-Truth?

With the exact formula $\Delta p_1^{(\text{failure})} = -p_1 q_1/(n_1+1)$, the expected update is:

$$\mathbb{E}[\Delta p_1] = \theta_1\theta_2 \cdot \frac{1 - p_1}{n_1+1} + (1 - \theta_1\theta_2) \cdot \left(-\frac{p_1 q_1}{n_1+1}\right)$$

At truth ($p_k = \theta_k$, so $q_1 = (1-\theta_1)/(1-\theta_1\theta_2)$):

$$\mathbb{E}[\Delta p_1]\big|_{\text{truth}} = \frac{1}{n_1+1}\left[\theta_1\theta_2(1-\theta_1) - (1-\theta_1\theta_2) \cdot \frac{\theta_1(1-\theta_1)}{1-\theta_1\theta_2}\right]$$

$$= \frac{\theta_1(1-\theta_1)}{n_1+1}\left[\theta_2 - 1\right] = -\frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1+1}$$

**The bias is confirmed for the exact marginal update too.** This is NOT an approximation artifact. The marginal Bayesian update of the point estimate, using only $y_G$ observations, is biased at truth.

### 3.9 Understanding the Bias

**Why does the exact Bayesian update have a biased marginal mean?**

The answer is subtle. The exact *joint* posterior $\pi(\theta_1, \theta_2 \mid \text{data})$ is unbiased — its mean converges to $(\theta_1, \theta_2)$. But we are computing the point-estimate update using the *agent's current point estimates* $p_k$ to compute blame weights $q_k$. The blame weights should use the true values $\theta_k$, but the agent doesn't know them.

More precisely: the exact marginal posterior $\pi(\theta_1 \mid y_G = 0)$ computed in §3.7 uses the prior mean $\bar{p}_2 = p_2$ as a plug-in for $\theta_2$ when integrating out $\theta_2$. When $p_2 \neq \theta_2$, this introduces error in the marginal.

But we evaluated AT truth ($p_k = \theta_k$), and the bias persists. So the issue is deeper.

**The real explanation.** The expected marginal change in $p_1$ should be computed by integrating over the true generative process:

$$\mathbb{E}[\Delta p_1] = P(y_G = 1) \cdot \Delta p_1^{(\text{success})} + P(y_G = 0) \cdot \mathbb{E}[\Delta p_1^{(\text{failure})}]$$

The success update increments $\alpha_1$ by 1 — the full unit. The failure update increments $\beta_1$ by a fractional amount $q_1 < 1$. On average, the total $\alpha$ increment rate is $\theta_1\theta_2$ per trial, and the total $\beta$ increment rate is $(1 - \theta_1\theta_2) \cdot q_1$ per trial. At truth:

$$\text{rate ratio} = \frac{\theta_1\theta_2}{(1-\theta_1\theta_2) \cdot (1-\theta_1)/(1-\theta_1\theta_2)} = \frac{\theta_1\theta_2}{1-\theta_1}$$

For unbiased updating, this ratio should equal $\theta_1/(1-\theta_1)$ (to keep $\alpha/(\alpha+\beta)$ stable at $\theta_1$). But the actual ratio is $\theta_1\theta_2/(1-\theta_1) \neq \theta_1/(1-\theta_1)$ (unless $\theta_2 = 1$).

**The success case always fully credits edge 1 ($\alpha_1 \to \alpha_1 + 1$), but edge 1's actual contribution to success is only $\theta_1$-worth of the total probability $\theta_1\theta_2$.** Success is overcredited to edge 1 because the agent cannot distinguish "I succeeded because edge 1 was reliable" from "I succeeded because edge 2 was reliable."

And yet: the exact *joint* Bayesian posterior converges correctly by the standard consistency theorem. The problem is with the factored point-estimate representation, not with the full posterior. The joint posterior has correlations that encode the missing information; collapsing to marginal point estimates discards this.

*[Derived (marginal point-estimate bias, unobservable intermediate)]*

**Key result.** For a two-edge chain with unobservable intermediate, any update rule that:
1. Uses marginal point estimates (not the full joint posterior), and
2. Attributes success by incrementing both edges' $\alpha$ counts equally,

will have systematic downward bias on both $p_1$ and $p_2$ at truth. The bias magnitude is $O(1/n)$, so it vanishes as experience accumulates, but it violates (A1) at every finite $n$.

### 3.10 Sector Condition for the Unobservable Case

Given the (A1) violation, the standard sector-condition framework does not apply directly. However, we can modify the framework to accommodate the bias.

**Modified sector condition.** Define the *bias-corrected mismatch* $\tilde{\delta}_k = p_k - \theta_k + b_k$, where $b_k$ is the asymptotic bias (the value at which the expected update is zero). For edge 1:

Setting $\mathbb{E}[\Delta p_1] = 0$ in the general formula and solving for $p_1$: this requires solving a nonlinear equation involving both $p_1, p_2, \theta_1, \theta_2$. There is no clean closed form.

**Alternative: bound the bias and treat it as disturbance.**

At truth, the bias magnitude for edge 1 is:

$$|b_1| = \frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1+1}$$

This is $O(1/n)$ and bounded by $1/(4(n_1+1))$ (maximized at $\theta_1 = 1/2$, $\theta_2 = 0$). We can absorb this bias into the disturbance term:

$$\rho_{\text{eff}} = \rho_\Sigma + |b_1| + |b_2|$$

where $|b_k|$ are the bias magnitudes. This preserves the sector-condition structure at the cost of increasing the effective disturbance.

**But this is unsatisfying.** The bias depends on $n_k$ (it decreases with experience), so $\rho_{\text{eff}}$ is time-varying. And the bias-as-disturbance framing loses the structural insight about *why* the unobservable case is harder.

### 3.11 A Cleaner Approach: The Product-Space View

Instead of tracking mismatch per-edge, consider the **plan-level mismatch**:

$$\delta_\Phi = \hat{\Phi} - \Phi = p_1 p_2 - \theta_1\theta_2$$

This is a scalar, and the agent observes $y_G \sim \text{Bernoulli}(\Phi)$. The update for $\hat{\Phi}$ can be derived directly:

$$\hat{\Phi}_{\text{new}} = p_1^{\text{new}} \cdot p_2^{\text{new}}$$

In the **success case**: $p_1^{\text{new}} = (\alpha_1+1)/(n_1+1)$, $p_2^{\text{new}} = (\alpha_2+1)/(n_2+1)$. The product changes in a complex way.

In the **failure case**: the product update depends on the blame assignments.

This approach inherits the per-edge update's problems and adds the nonlinearity of the product. It does not simplify the analysis.

**An alternative plan-level approach.** If the agent maintains a *direct* Beta posterior on $\Phi = \theta_1\theta_2$ (treating the chain as a single edge with unknown probability $\Phi$), then the single-edge spike's results apply directly:

$$\alpha_{\Sigma,\text{plan}} = \frac{1}{n_\Phi + 1}$$

where $n_\Phi$ is the pseudo-count for the plan-level Beta. The sector condition holds with the same arguments as the single-edge case. But this sacrifices per-edge resolution — the agent cannot distinguish between "edge 1 is unreliable" and "edge 2 is unreliable." It can detect that the plan is failing, but cannot diagnose which step needs revision.

*[Discussion (plan-level vs. per-edge tracking)]*

**The tradeoff:**
- **Per-edge tracking** (two Betas): diagnostic resolution (can identify which edge is failing), but biased updates when the intermediate is unobservable and does not cleanly satisfy the sector condition.
- **Plan-level tracking** (one Beta): no diagnostic resolution, but unbiased updates and clean sector-condition satisfaction with $\alpha_\Sigma = 1/(n_\Phi+1)$.

This tradeoff is a concrete instance of the observability-dominance principle (#der-observability-dominance): when the intermediate is unobservable, the per-edge decomposition is epistemically dead for the purpose of clean updating. The agent's *effective* strategy is the plan-level aggregate, regardless of the nominal per-edge decomposition.

### 3.12 Structured Approximation: EM-Style Update

There is a principled middle ground between full Bayesian inference (intractable) and naive per-edge point estimates (biased). Consider an **expectation-maximization** style approach:

**E-step.** Given current beliefs $(p_1, p_2)$ and observation $y_G$, compute the posterior probability that $B$ was achieved:

$$P(y_B = 1 \mid y_G = 0, p_1, p_2) = \frac{p_1(1 - p_2)}{1 - p_1 p_2} = q_2$$

$$P(y_B = 1 \mid y_G = 1, p_1, p_2) = 1 \quad \text{(if $y_G = 1$, $B$ must have been reached)}$$

**M-step.** Use the imputed $y_B$ to update each edge independently:

- On success ($y_G = 1$): $y_B = 1$ (certain). Update edge 1 with $y_B = 1$, edge 2 with $y_G = 1$.
- On failure ($y_G = 0$): $y_B$ is uncertain. Update edge 1 with soft evidence $\hat{y}_B = q_2$ (probability $B$ was reached). Update edge 2 with soft evidence, but only conditional on $B$ having been reached.

This is exactly the proportional-blame update of §3.4. The EM-style framing makes explicit that the bias arises from using point estimates in the E-step — a known issue with online EM.

**The bias can be reduced by iterating the E-step** (using the updated $(p_1, p_2)$ to re-impute $y_B$, then re-updating). But this does not eliminate it for finite samples.

### 3.13 Summary: The Unobservable Case Is Genuinely Hard

*[Discussion (unobservable intermediate assessment)]*

**What we can establish:**

1. **Success updates are clean.** When $y_G = 1$, the marginal Bayesian update for each edge is exactly the standard Beta increment ($\alpha_k \to \alpha_k + 1$). The success case preserves independence.

2. **Failure updates introduce correlation.** When $y_G = 0$, the joint posterior is no longer a product of independent Betas. Any representation that maintains per-edge independence (factored point estimates) is an approximation.

3. **The proportional-blame update is the marginal Bayesian mean.** It is not a heuristic — it is the exact update for the marginal mean of the posterior. But it is biased as a point-estimate update rule because it discards the posterior correlation.

4. **The bias is $O(1/n)$.** It vanishes as the agent accumulates experience. Asymptotically, the marginal posteriors concentrate on the true values (by the Bayesian consistency theorem for identifiable models — and the model IS identifiable: $\theta_1\theta_2 = \Phi$ alone is not sufficient to identify $\theta_1, \theta_2$ individually, so identification requires that either the model has a proper joint prior or additional structure breaks the symmetry).

5. **(A1) is violated at every finite $n$.** The zero-correction-at-truth property fails, which means the standard sector condition cannot be applied directly.

**What we cannot cleanly establish:**

1. **A sector-condition bound for the per-edge unobservable case.** The coupling between edges, the (A1) violation, and the nonlinear blame-assignment mechanism prevent a clean $\alpha_\Sigma$ characterization.

2. **Whether the bias is harmful in practice.** The bias pushes both credences downward (toward pessimism). In an AND-chain, pessimistic credences lead to conservative behavior (lower plan confidence → more likely to switch strategies or seek alternatives). This might actually be adaptive — but it is not the unbiased convergence the sector framework requires.

3. **Identification.** With only $y_G$ observations, the agent observes $\Phi = \theta_1\theta_2$ but cannot identify $\theta_1$ and $\theta_2$ separately. The prior (specifically, the ratio $\alpha_1/n_1$ vs $\alpha_2/n_2$) determines how the observed $\Phi$ is decomposed. If the prior is wrong, the decomposition is wrong, and the marginal estimates need not converge to the true values — only the product $p_1 p_2$ converges to $\theta_1\theta_2$.

---

## 4. Identification and Observability

The unobservable-intermediate case reveals a deeper issue: **non-identifiability**.

### 4.1 The Identification Problem

From $y_G$ alone, the agent can learn $\Phi = \theta_1\theta_2$ (the plan success rate). But the decomposition into $(\theta_1, \theta_2)$ is underdetermined. Any pair $(\theta_1', \theta_2')$ with $\theta_1'\theta_2' = \Phi$ produces identical observations.

**With independent Beta priors**, the agent's decomposition is driven by the relative prior strengths. If $n_1 \gg n_2$ (much more prior experience about edge 1), then most of the uncertainty is attributed to edge 2. Conversely, if $n_1 \approx n_2$, the attribution is roughly symmetric. The point estimates converge to SOME pair $(\hat{\theta}_1, \hat{\theta}_2)$ with $\hat{\theta}_1 \hat{\theta}_2 = \Phi$, but not necessarily to the true $(\theta_1, \theta_2)$.

*[Derived (non-identifiability, unobservable intermediate)]*

**This is the formal content of #der-observability-dominance for this case.** The edges connected to the unobservable node $B$ are not individually identifiable from the terminal observation alone. They are "frozen" in a weaker sense than full freezing: their product converges, but their individual values may not.

### 4.2 When Identification Succeeds

The per-edge values ARE identifiable when:

1. **$B$ is sometimes observable.** Even occasional observations of $B$ break the symmetry. If the agent observes $y_B$ on a fraction $f$ of trials, the per-edge learning rate is at least $f \cdot \min(1/(n_1+1), \theta_1/(n_2+1))$ — the observable-case rate, attenuated by $f$.

2. **The agent has other strategies that test the same edges.** If edge $A \to B$ also appears in another strategy $A \to B \to G'$, the agent gets independent evidence about edge 1 from the other strategy's outcomes.

3. **The agent can experiment.** By deliberately testing whether $B$ is achievable (executing $A$ and checking $B$ directly, without needing $G$), the agent converts the unobservable case to the observable case for the cost of an exploratory action.

These are all instances of the general principle from #hyp-edge-update-via-gain: per-edge learning requires per-edge observability (or a proxy for it).

---

## 5. Sector Condition Summary

### 5.1 Observable Intermediate: Clean Result

*[Derived (two-edge sector condition, observable intermediate)]*

$$\alpha_\Sigma = \min\left(\frac{1}{n_1+1},\; \frac{\theta_1}{n_2+1}\right)$$

- The sector condition holds globally (all $\delta_k \in [-1, 1]$).
- The bound is tight for each edge independently (expected correction is linear in mismatch per-edge).
- The correction function is diagonal — no cross-edge coupling.
- (A1) is satisfied: at truth, expected correction is zero for each edge.
- The persistence condition is $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$, giving per-edge experience bounds.
- Downstream edges are attenuated by upstream success probability — the **evidence-starvation** effect.

### 5.2 Unobservable Intermediate: Partial Results

**What holds:**
- Plan-level sector condition: if the agent tracks $\hat{\Phi} = p_1 p_2$ as a single-edge Beta, $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$ and the single-edge results apply directly.
- The marginal posteriors' means converge to values consistent with the true $\Phi$ (product converges correctly even if factors do not).

**What fails:**
- Per-edge (A1): zero-correction-at-truth is violated with bias $O(1/n)$.
- Per-edge identification: $\theta_1, \theta_2$ are not individually identifiable from $y_G$ alone.
- Per-edge sector condition: not established. The coupled, biased correction function does not fit the standard framework.

**Assessment:** The unobservable case requires either (a) a modified sector-condition framework that accommodates asymptotically vanishing bias, or (b) acceptance that the plan-level aggregate is the correct unit of analysis for the sector condition. Option (b) is consistent with #der-observability-dominance — the theory already predicts that unobservable structure is epistemically dead for individual tracking.

### 5.3 Comparison Table

| Quantity | Observable Intermediate | Unobservable Intermediate |
|----------|------------------------|--------------------------|
| Mismatch dimension | 2 (per-edge) | 1 (plan-level) or 2 (biased) |
| Correction coupling | None (diagonal) | Coupled (blame assignment) |
| (A1) zero at truth | Yes | No (per-edge); Yes (plan-level) |
| Sector condition | Holds; $\alpha = \min(\alpha_1, \alpha_2)$ | Holds at plan level; open per-edge |
| Identification | Both edges identified | Only product identified |
| Diagnostic resolution | Full (which edge failed?) | None (plan failed) |
| Persistence condition | Per-edge bounds | Plan-level bound only |

---

## 6. Connection to Observability Dominance

The two-edge analysis provides a concrete mathematical mechanism for #der-observability-dominance:

**Observable B.** The agent has diagnostic resolution: it can identify which edge is miscalibrated and correct specifically. The sector condition holds per-edge, with the weakest link determining overall $\alpha_\Sigma$. The downstream evidence-starvation effect ($\alpha_2$ attenuated by $\theta_1$) is a quantitative prediction: downstream edges learn more slowly, proportional to upstream reliability.

**Unobservable B.** The agent loses diagnostic resolution. Per-edge credences are not individually identifiable. The marginal update is biased. The agent can track plan-level success, but cannot localize failure. This is exactly the prediction of #der-observability-dominance — unobservable nodes freeze per-edge learning — given precise mathematical form.

**The observability investment tradeoff.** Making $B$ observable costs something (instrumentation, monitoring, time spent checking). The benefit is: clean per-edge sector conditions instead of the degraded plan-level-only result. The value of this investment is:

$$\Delta\alpha = \min\left(\frac{1}{n_1+1}, \frac{\theta_1}{n_2+1}\right) - \frac{1}{n_\Phi+1}$$

When $n_1 \approx n_2 \approx n_\Phi/2$ (similar experience per edge vs. aggregate), this is positive whenever $\theta_1 > 1/2$ — i.e., whenever the first edge is more likely to succeed than fail. The diagnostic decomposition provides faster effective correction than the aggregate whenever the plan has a reasonable chance of partial success.

---

## 7. Implications for Strategy Architecture

### 7.1 Prefer Observable Intermediates

The mathematical analysis gives a sharp prescription: **design strategies with observable intermediate nodes.** This converts the intractable unobservable case to the clean observable case. The cost is instrumentation; the benefit is per-edge identification, unbiased updates, and a provable sector condition.

This is the strategic analog of the software engineering principle in #der-code-quality-as-observation-infrastructure (TST cross-reference): tests and monitoring make intermediate states observable, enabling per-component calibration rather than end-to-end-only assessment.

### 7.2 The Depth-Observability Tradeoff

For a depth-$d$ chain with all intermediates observable, $\alpha_\Sigma = \min_k \prod_{j<k}\theta_j / (n_k+1)$. This decays exponentially with depth (via the product of upstream $\theta_j$). Long chains are hard to calibrate even with full observability — deep edges are evidence-starved.

For a depth-$d$ chain with no intermediates observable, the plan-level $\alpha_\Sigma = 1/(n_\Phi+1)$ does not decay with depth — but diagnostic resolution is zero. The agent knows whether the plan works but not which step is failing.

**Optimal strategy architecture balances depth against observability.** Shallow plans with full observability are best for calibration. Deep plans are justified only when intermediate observability is maintained at each level — which has increasing cost as depth grows.

### 7.3 Evidence Starvation and Exploration

The downstream attenuation factor $\prod_{j<k}\theta_j$ creates a natural exploration incentive: if the agent wants to learn about deep edges, it must first make the upstream edges reliable (high $\theta_j$). This is the "skill hierarchy" structure — learn basic skills first, then build on them. The sector-condition analysis makes the quantitative tradeoff precise: each upstream edge's reliability determines how fast the downstream edges can be calibrated.

---

## 8. What This Does and Doesn't Establish

### What it establishes

1. **The sector condition extends to multi-edge chains with observable intermediates.** The sector parameter is $\alpha_\Sigma = \min_k \alpha_k$, a weakest-link result. Each edge's effective correction rate is its stand-alone rate attenuated by the product of upstream success probabilities (evidence-starvation effect). This is a clean, derived result.

2. **The unobservable intermediate case breaks per-edge (A1).** Observing only the terminal outcome introduces a systematic bias in marginal point-estimate updates. The bias is $O(1/n)$ (asymptotically vanishing) and pushes credences toward pessimism. This is an exact result about the marginal Bayesian update, not an approximation artifact.

3. **Plan-level tracking recovers the sector condition.** If the agent tracks aggregate plan success as a single Beta, the single-edge results apply directly. This sacrifices per-edge diagnostic resolution but provides a clean persistence guarantee.

4. **Per-edge identification requires per-edge observability.** From terminal observations alone, only the product $\theta_1\theta_2$ is identifiable. Individual edge parameters require individual edge observations (or structural constraints that break the symmetry). This is the formal content of #der-observability-dominance for the two-edge case.

5. **Observability investment has quantifiable value.** Making the intermediate observable increases $\alpha_\Sigma$ from the plan-level rate to the per-edge weakest-link rate. The improvement depends on $\theta_1$ and the relative experience levels.

### What it doesn't establish

1. **Sector condition for the per-edge unobservable case.** The bias and coupling prevent direct application of the sector framework. A modified framework (asymptotically vanishing bias, or coupled-correction sector conditions) might recover the result, but this is not attempted here.

2. **Extension to general DAGs (OR nodes, multi-parent nodes).** The analysis assumes a linear AND-chain. OR nodes, which provide alternative paths, introduce different coupling: success on one path provides no evidence about the other. The credit-assignment problem for OR-nodes is the complement of the AND-node problem: success must be attributed (which path worked?), while failure is clean (all paths failed). This is left for future work.

3. **Correlated edge failures.** The analysis assumes independent edges (conditional on the agent's beliefs). Correlated failures (shared infrastructure, common-mode risks) would further complicate the unobservable case.

4. **Optimal blame assignment under non-identifiability.** Is the proportional-blame (marginal Bayesian) update the *best* strategy for the agent, given non-identifiability? Or would a different decomposition (e.g., one that accounts for the asymptotic bias) converge faster? This is an open question in Bayesian experimental design.

5. **Time-varying $\alpha_\Sigma$.** As in the single-edge case, the sector parameter depends on $n_k$ (which increases with observations). The constant-$\alpha$ assumption in the sector framework is violated. The discounted (exponential forgetting) model would stabilize $\alpha_\Sigma$, but the interaction between discounting and credit assignment for the unobservable case is not analyzed.

---

## 9. Path Forward

1. **Promote the observable-intermediate result.** The two-edge sector condition with observable intermediate is clean enough for a draft segment (e.g., `multi-edge-sector-condition.md`). The weakest-link structure and evidence-starvation effect are genuine results.

2. **Formalize the observability-identification connection.** The non-identifiability result for the unobservable case should be connected to #der-observability-dominance as a concrete theorem: "per-edge identification requires per-edge observability."

3. **Investigate the $O(1/n)$ bias.** The systematic pessimism bias in the unobservable case is interesting. Does it help or hurt? A pessimistic agent in an AND-chain is more likely to seek alternatives or invest in observability — both adaptive responses. The bias might be a *feature*, not a bug, from an evolutionary perspective.

4. **Extend to OR-nodes.** The complementary credit-assignment problem (attributing success across OR-branches) should have a similar structure. If the AND-node result extends to OR-nodes, the general DAG case follows by composition.

5. **Modified sector condition for biased correction.** Develop a sector-condition variant that accommodates $F(\mathbf{0}) = b \neq \mathbf{0}$ with $|b| = O(1/n)$. This would allow the per-edge unobservable result to be stated as: "sector condition holds asymptotically, with a transient bias that contributes $O(1/n)$ effective disturbance."
