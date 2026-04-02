---
slug: strategic-dynamics-derivation
type: derivation
status: conditional
depends:
  - strategy-persistence-schema
  - edge-update-via-gain
  - sector-condition-derivation
  - and-or-scope
stage: draft
---

# Derivation: Sector Condition Verification for Strategic Dynamics

Complete verification that specific strategy update dynamics satisfy the sector condition from #sector-condition-derivation, backing the schema proposed in #strategy-persistence-schema. Four cases are treated: a single-edge strategy, a two-edge AND-chain with observable intermediate, the same chain with unobservable intermediate, and a two-arm OR-node under exploratory action selection.

## Motivation

#strategy-persistence-schema proposes that the sector-condition mathematics (Props A.1, A.1S, A.2 in #sector-condition-derivation) extends from epistemic to strategic mismatch. The schema identifies three structural conditions (SA1, SA2', SA3) and conjectures the persistence form $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$. This appendix instantiates the schema for concrete Beta-Bernoulli edge dynamics, verifying the conditions case by case. Each proposition establishes the sector parameter $\alpha_\Sigma$ for a specific DAG topology; the persistence condition then follows by direct substitution into Proposition A.1 of #sector-condition-derivation.


## Common Setup

Throughout, edge credences follow Beta-Bernoulli dynamics: edge $k$ has true success probability $\theta_k \in (0,1)$, agent belief $p_k \sim \text{Beta}(\alpha_k, \beta_k)$ with point estimate $\hat p_k = \alpha_k / n_k$ where $n_k = \alpha_k + \beta_k$, and conjugate update on observing $y_k \in \{0,1\}$:

*[Definition (Beta-Bernoulli edge dynamics)]*

$$\Delta \hat p_k = \frac{y_k - \hat p_k}{n_k + 1}, \qquad \eta_k = \frac{1}{n_k + 1}$$

The single-step update matches the gain-based form from #edge-update-via-gain with $\eta_{\text{edge}} = 1/(n_k + 1)$.

Strategic mismatch per edge is $\delta_k = \hat p_k - \theta_k$. The sector-condition framework ( #sector-condition-derivation) requires: (SA1) $F(\mathbf{0}) = \mathbf{0}$, (SA2') $\boldsymbol{\delta}^T \mathbf{F}(\boldsymbol{\delta}) \geq \alpha_\Sigma \lVert\boldsymbol{\delta}\rVert^2$ within a region $\mathcal B_R$.


## Proposition B.1: Single Edge ($A \to G$)

**Setup.** One action $A$, one goal $G$, one edge with credence $\hat p$ and true probability $\theta$. Mismatch: $\delta_\Sigma = \hat p - \theta$ (scalar).

**Statement.** Under Beta-Bernoulli updating, the expected correction function satisfies the sector condition globally (all $\lvert\delta_\Sigma\rvert \leq 1$) with:

*[Derived (Conditional on Beta-Bernoulli model)]*

$$\alpha_\Sigma = \frac{1}{n+1}$$

The bound is tight.

**Proof.**

The expected correction. Since $y \sim \text{Bernoulli}(\theta)$:

*[Derived (Proof Step)]*

$$\mathbb{E}[\Delta \hat p] = \frac{\theta - \hat p}{n+1} = -\frac{\delta_\Sigma}{n+1}$$

Identifying $F_\Sigma(\delta_\Sigma) = -\mathbb{E}[\Delta\delta_\Sigma] = \delta_\Sigma/(n+1)$:

*[Derived (Proof Step)]*

$$\delta_\Sigma \cdot F_\Sigma(\delta_\Sigma) = \frac{\delta_\Sigma^2}{n+1} = \frac{1}{n+1}\lVert\delta_\Sigma\rVert^2$$

So $\alpha_\Sigma = 1/(n+1)$. The correction is exactly linear, so the sector bound is tight (not merely a lower bound).

**Verification of (SA1).** At $\delta_\Sigma = 0$: $F_\Sigma(0) = 0$. Satisfied.

**Stochastic ultimate bound.** Decomposing $\delta_{\Sigma,t+1} = \delta_\Sigma \cdot n/(n+1) + (y - \theta)/(n+1)$ and computing $\mathbb{E}[\delta_{\Sigma,t+1}^2]$:

*[Derived (stochastic ultimate bound, single edge)]*

$$\mathbb{E}[\delta_{\Sigma,t+1}^2] = \delta_\Sigma^2 \cdot \frac{n^2}{(n+1)^2} + \frac{\theta(1-\theta)}{(n+1)^2}$$

The expected Lyapunov derivative $\mathbb{E}[\Delta V] \lt 0$ whenever:

$$\lvert\delta_\Sigma\rvert \gt \sqrt{\frac{\theta(1-\theta)}{2n+1}}$$

The stochastic noise floor decreases as $O(1/\sqrt{n})$ --- the standard Bayesian posterior concentration rate. $\square$


## Proposition B.2: Two-Edge AND-Chain, Observable Intermediate ($A \to B \to G$, $B$ observed)

**Setup.** Action $A$ leads to intermediate $B$, then to goal $G$. Both $y_B$ and $y_G$ are observed. Edge credences $\hat p_1, \hat p_2$ with true probabilities $\theta_1, \theta_2$. Plan confidence: $\hat P_\Sigma = \hat p_1 \hat p_2$ (AND propagation from #and-or-scope). Mismatch vector: $\boldsymbol{\delta}_\Sigma = (\delta_1, \delta_2)^T$.

The generative model:

$$y_B \sim \text{Bernoulli}(\theta_1), \qquad y_G \mid y_B = 1 \sim \text{Bernoulli}(\theta_2), \qquad y_G \mid y_B = 0 = 0$$

**Statement.** Under Beta-Bernoulli updating with observable intermediate, the expected correction function is diagonal and satisfies the sector condition globally with:

*[Derived (Conditional on Beta-Bernoulli model, observable intermediate)]*

$$\alpha_\Sigma = \min\!\left(\frac{1}{n_1+1},\; \frac{\theta_1}{n_2+1}\right)$$

**Proof.**

Edge 1 is tested every trial: $\Delta \hat p_1 = (y_B - \hat p_1)/(n_1+1)$, giving $\mathbb{E}[\Delta \hat p_1] = -\delta_1/(n_1+1)$.

Edge 2 is tested only when $y_B = 1$ (probability $\theta_1$). When $y_B = 0$, edge 2 receives no information:

*[Derived (Proof Step)]*

$$\mathbb{E}[\Delta \hat p_2] = \theta_1 \cdot \frac{\theta_2 - \hat p_2}{n_2+1} + (1 - \theta_1) \cdot 0 = -\frac{\theta_1 \delta_2}{n_2+1}$$

The expected correction function is diagonal:

$$\mathbf{F}(\boldsymbol{\delta}_\Sigma) = \begin{pmatrix} \delta_1/(n_1+1) \\ \theta_1 \delta_2/(n_2+1) \end{pmatrix}$$

**Verification of (SA1).** At $\boldsymbol{\delta}_\Sigma = \mathbf{0}$: $\mathbf{F}(\mathbf{0}) = \mathbf{0}$. Satisfied.

The sector product:

*[Derived (Proof Step)]*

$$\boldsymbol{\delta}_\Sigma^T \mathbf{F}(\boldsymbol{\delta}_\Sigma) = \frac{\delta_1^2}{n_1+1} + \frac{\theta_1 \delta_2^2}{n_2+1} \geq \min\!\left(\frac{1}{n_1+1}, \frac{\theta_1}{n_2+1}\right)(\delta_1^2 + \delta_2^2)$$

The minimum is achieved by whichever edge has the lower effective correction rate. $\square$

**The evidence-starvation effect.** Edge 2's effective correction rate $\theta_1/(n_2+1)$ is attenuated by the upstream success probability $\theta_1$. When $\theta_1$ is small, edge 2 is starved of evidence --- it is tested rarely, learns slowly, and becomes the weakest link. This gives a precise mechanism for #chain-confidence-decay: downstream edges in AND-chains are harder to calibrate, with correction rate proportional to the product of all upstream success probabilities.

**Generalization to depth $d$.** For a chain of depth $d$ with all intermediates observable, edge $k$'s effective correction rate is $\alpha_k = \prod_{j=1}^{k-1}\theta_j / (n_k + 1)$, giving:

*[Derived (depth-$d$ chain sector parameter)]*

$$\alpha_\Sigma = \min_{k=1}^{d}\; \frac{\prod_{j=1}^{k-1}\theta_j}{n_k+1}$$


## Proposition B.3: Two-Edge AND-Chain, Unobservable Intermediate ($A \to B \to G$, $B$ not observed)

**Setup.** Same DAG as Proposition B.2, but only $y_G \in \{0,1\}$ is observed. The agent cannot distinguish "$A \to B$ failed" from "$B \to G$ failed" when $y_G = 0$.

**Statement.** (a) The per-edge sector condition fails: the marginal Bayesian update violates (SA1) with systematic bias $O(1/n)$. (b) Plan-level tracking (treating $\hat\Phi = \hat p_1 \hat p_2$ as a single Beta over the composite probability $\Phi = \theta_1\theta_2$) recovers the sector condition with:

*[Derived (Conditional on Beta-Bernoulli model, unobservable intermediate)]*

$$\alpha_{\Sigma,\text{plan}} = \frac{1}{n_\Phi + 1}$$

**Proof of (a): Per-edge (SA1) violation.**

The joint posterior after success ($y_G = 1$) factors cleanly: $\alpha_k \to \alpha_k + 1$ for both edges. The joint posterior after failure ($y_G = 0$) includes the factor $(1 - \theta_1\theta_2)$, which does not decompose into separate functions of $\theta_1$ and $\theta_2$. Failure introduces posterior correlation.

The exact marginal Bayesian update for edge 1 on failure is:

*[Derived (Proof Step)]*

$$\Delta \hat p_1^{(\text{fail})} = -\frac{\hat p_1 \, q_1}{n_1 + 1}$$

where $q_1 = (1 - \hat p_1)/(1 - \hat p_1 \hat p_2)$ is the posterior probability that edge 1 caused the failure (the proportional-blame weight). The expected update, combining success (probability $\theta_1\theta_2$) and failure (probability $1 - \theta_1\theta_2$):

*[Derived (Proof Step)]*

$$\mathbb{E}[\Delta \hat p_1] = \theta_1\theta_2 \cdot \frac{1 - \hat p_1}{n_1+1} - (1-\theta_1\theta_2)\cdot\frac{\hat p_1\,q_1}{n_1+1}$$

Evaluating at truth ($\hat p_k = \theta_k$):

*[Derived (SA1 violation magnitude)]*

$$\mathbb{E}[\Delta \hat p_1]\big\rvert_{\hat p = \theta} = -\frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1+1} \neq 0$$

The bias is negative (pushes credence below truth), of magnitude $O(1/n)$, and arises because success always increments $\alpha_1$ by a full unit while failure increments $\beta_1$ by the fractional weight $q_1 \lt 1$. The success case over-credits edge 1 because the agent cannot separate edge 1's contribution from edge 2's. By symmetry, $\hat p_2$ is also biased downward. $\square$

**Proof of (b): Plan-level recovery.**

If the agent tracks $\hat\Phi$ directly as a Beta posterior over $\Phi = \theta_1\theta_2$ using $y_G \sim \text{Bernoulli}(\Phi)$, the setup reduces to a single-edge problem (Proposition B.1) with mismatch $\delta_\Phi = \hat\Phi - \Phi$ and sector parameter $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$. All single-edge results apply. $\square$

**Tradeoff.** Per-edge tracking provides diagnostic resolution (which edge is failing?) but yields biased, non-sector-conforming updates when the intermediate is unobservable. Plan-level tracking sacrifices diagnostic resolution but provides clean sector-condition satisfaction. This is a concrete instance of #observability-dominance: unobservable nodes freeze per-edge learning, making the aggregate the correct unit of analysis.

**Non-identifiability.** From $y_G$ observations alone, only $\Phi = \theta_1\theta_2$ is identifiable. The per-edge decomposition $(\theta_1, \theta_2)$ is underdetermined --- any pair with the same product produces identical observations. Per-edge identification requires per-edge observability (or structural constraints that break the symmetry).


## Proposition B.4: Two-Arm OR-Node ($A_1, A_2 \to G$, $\varepsilon$-greedy)

**Setup.** Goal $G$ reachable via two alternative actions $A_1, A_2$ (an OR-node from #and-or-scope). True probabilities $\theta_1, \theta_2$. Agent selects one action per trial: with probability $1 - \varepsilon$ the greedy choice (higher $\hat p_k$), with probability $\varepsilon$ the other. Mismatch vector: $\boldsymbol{\delta}_\Sigma = (\delta_1, \delta_2)^T$.

**Statement.** (a) Under a greedy policy ($\varepsilon = 0$), the sector condition fails for the full mismatch vector. (b) Under $\varepsilon$-greedy action selection with $\varepsilon \gt 0$, the sector condition is satisfied with:

*[Derived (Conditional on Beta-Bernoulli model, $\varepsilon$-greedy OR-node)]*

$$\alpha_\Sigma = \min\!\left(\frac{1-\varepsilon}{n_1+1},\; \frac{\varepsilon}{n_2+1}\right)$$

where arm 1 is the greedy choice.

**Proof of (a): Greedy failure.**

Under greedy selection, only the chosen arm updates. Assuming $\hat p_1 \gt \hat p_2$ (arm 1 is greedy):

$$\mathbf{F}(\boldsymbol{\delta}_\Sigma) = \begin{pmatrix}\delta_1/(n_1+1) \\ 0\end{pmatrix}$$

The sector product $\boldsymbol{\delta}_\Sigma^T \mathbf{F} = \delta_1^2/(n_1+1)$. For the sector condition to hold, we need $\delta_1^2/(n_1+1) \geq \alpha_\Sigma(\delta_1^2 + \delta_2^2)$. Setting $\delta_1 = 0$: the LHS is zero but $\alpha_\Sigma \delta_2^2 \gt 0$ for $\delta_2 \neq 0$. No $\alpha_\Sigma \gt 0$ works. $\square$

**Proof of (b): $\varepsilon$-greedy recovery.**

The expected correction (arm 1 greedy):

*[Derived (Proof Step)]*

$$\mathbb{E}[\mathbf{F}(\boldsymbol{\delta}_\Sigma)] = \begin{pmatrix}(1-\varepsilon)\,\delta_1/(n_1+1) \\ \varepsilon\,\delta_2/(n_2+1)\end{pmatrix}$$

The sector product:

*[Derived (Proof Step)]*

$$\boldsymbol{\delta}_\Sigma^T \mathbf{F} = \frac{(1-\varepsilon)\,\delta_1^2}{n_1+1} + \frac{\varepsilon\,\delta_2^2}{n_2+1} \geq \min\!\left(\frac{1-\varepsilon}{n_1+1},\;\frac{\varepsilon}{n_2+1}\right)\!(\delta_1^2 + \delta_2^2)$$

**Verification of (SA1).** At $\boldsymbol{\delta}_\Sigma = \mathbf{0}$: $\mathbf{F}(\mathbf{0}) = \mathbf{0}$. Satisfied. $\square$

**Optimal exploration rate.** Maximizing $\alpha_\Sigma$ over $\varepsilon$ by equalizing the two terms:

*[Derived (optimal exploration rate)]*

$$\varepsilon^\ast = \frac{n_1+1}{n_1+n_2+2}, \qquad \alpha_\Sigma^\ast = \frac{1}{n_1+n_2+2}$$

For equal experience ($n_1 = n_2$): $\varepsilon^\ast = 1/2$ (equal allocation). For unequal experience, $\varepsilon^\ast$ allocates more trials to the arm with higher $n$ (lower gain) to equalize correction rates.

**The $k$-arm generalization.** For $k$ OR-alternatives with $\varepsilon$-uniform exploration (probability $\varepsilon/(k-1)$ per non-greedy arm):

*[Derived ($k$-arm OR-node sector parameter)]*

$$\alpha_\Sigma = \min\!\left(\frac{1-\varepsilon}{n_{\text{greedy}}+1},\;\min_{j \neq \text{greedy}}\frac{\varepsilon/(k-1)}{n_j+1}\right)$$

With optimal equal-rate exploration and equal experience: $\alpha_\Sigma = 1/(k(n+1))$. The sector parameter scales as $1/k$ --- each additional alternative dilutes correction capacity.

**Condition (SA3).** For the sector condition to be satisfiable at all, the exploration rate must satisfy:

*[Derived (minimum exploration rate for persistence)]*

$$\varepsilon \gt \frac{\rho_\Sigma(n_{\max}+1)}{R_\Sigma}$$

A purely greedy agent ($\varepsilon = 0$) violates the sector condition because the unchosen alternative's mismatch grows without correction. This is the structural justification for (SA3) in #strategy-persistence-schema: OR-nodes require deliberate exploration to maintain strategic persistence.


## Persistence Conditions

Substituting each proposition's $\alpha_\Sigma$ into the persistence threshold $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$ from Proposition A.1 of #sector-condition-derivation:

**Single edge (B.1):**

*[Derived (single-edge persistence threshold)]*

$$\frac{1}{n+1} \gt \frac{\rho_\Sigma}{R_\Sigma} \quad\iff\quad n \lt \frac{R_\Sigma}{\rho_\Sigma} - 1$$

The critical experience level $n^\ast = R_\Sigma/\rho_\Sigma - 1$ is the point at which gain collapse occurs: the posterior has concentrated so much that the agent can no longer track environmental drift.

**Two-edge observable (B.2):**

*[Derived (two-edge persistence threshold, observable)]*

$$\min\!\left(\frac{1}{n_1+1},\;\frac{\theta_1}{n_2+1}\right) \gt \frac{\rho_\Sigma}{R_\Sigma}$$

This decomposes into two independent conditions: $n_1 \lt R_\Sigma/\rho_\Sigma - 1$ and $n_2 \lt \theta_1 R_\Sigma/\rho_\Sigma - 1$. The downstream edge has a stricter bound, tightened by $\theta_1$. Gain collapse hits downstream edges first.

**Two-edge unobservable (B.3):**

$$\frac{1}{n_\Phi+1} \gt \frac{\rho_\Sigma}{R_\Sigma} \quad\iff\quad n_\Phi \lt \frac{R_\Sigma}{\rho_\Sigma} - 1$$

Same form as single-edge, applied to the plan-level aggregate.

**Two-arm OR, $\varepsilon$-greedy (B.4):**

*[Derived (OR-node persistence threshold)]*

$$\min\!\left(\frac{1-\varepsilon}{n_1+1},\;\frac{\varepsilon}{n_2+1}\right) \gt \frac{\rho_\Sigma}{R_\Sigma}$$

With optimal exploration and equal experience ($n_1 = n_2 = n$):

$$n \lt \frac{R_\Sigma}{2\rho_\Sigma} - 1$$

The critical experience is halved relative to the single-edge case. Each additional OR-alternative further reduces the critical level by $1/k$.


## Summary of Results

| Case | Topology | $\alpha_\Sigma$ | SA1 | SA3 | Weakest link |
|------|----------|-----------------|-----|-----|-------------|
| **B.1** Single edge | $A \to G$ | $1/(n+1)$ | Yes | N/A | --- |
| **B.2** Two-edge, $B$ observable | $A \to B \to G$ (AND) | $\min(1/(n_1\!+\!1),\;\theta_1/(n_2\!+\!1))$ | Yes | N/A | Depth-gated (evidence starvation) |
| **B.3** Two-edge, $B$ unobservable | $A \to B \to G$ (AND) | $1/(n_\Phi\!+\!1)$ (plan-level) | Per-edge: No ($O(1/n)$ bias); Plan: Yes | N/A | Credit-assignment collapse |
| **B.4** Two-arm OR, $\varepsilon$-greedy | $A_1, A_2 \to G$ (OR) | $\min((1\!-\!\varepsilon)/(n_1\!+\!1),\;\varepsilon/(n_2\!+\!1))$ | Yes | Required | Exploration-gated |
| **B.5a** Credence→value (linear) | Any | $\alpha_s = \alpha_c$ (Jacobian cancels) | — | — | None (exact transfer) |
| **B.5b** Credence→value (nonlinear) | Any | $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$ | — | — | DAG sensitivity anisotropy |

**Structural results across cases:**

- **Gain as sector parameter.** In every case, $\alpha_\Sigma$ is determined by the edge update gain $\eta_k = 1/(n_k+1)$, modulated by observability ($\theta_1$ attenuation in B.2), credit-assignment (plan-level collapse in B.3), or action-selection policy ($\varepsilon$ in B.4). The structural parallel between epistemic and strategic persistence is not an analogy --- it is a mathematical identity at the sector-framework level.
- **Evidence starvation (AND-chains).** Downstream edges in AND-chains have correction rates attenuated by the product of upstream success probabilities. Depth increases fragility: $\alpha_\Sigma$ decays exponentially with chain depth.
- **Exploration gating (OR-nodes).** Unchosen OR-alternatives receive zero correction. The sector condition requires deliberate exploration (SA3) at a rate exceeding $\rho_\Sigma(n_{\max}+1)/R_\Sigma$. Pure greedy policies fail.
- **Gain-collapse threshold.** In all cases, increasing experience eventually violates persistence when the environment drifts. The critical experience level $n^\ast$ is inversely proportional to the drift rate $\rho_\Sigma$.


## Proposition B.5: Bridge from Credence Error to Value Residuals

The propositions above verify the sector condition for the credence-error mismatch state $\boldsymbol\delta_c = (\hat p_k - \theta_k)$. But #strategy-persistence-schema identifies $\delta_{\text{strategic}}$ (from #strategic-calibration) — the aggregated value-increment residuals — as the operational diagnostic. This proposition connects the two.

### Setup

The plan value $\hat P_\Sigma = P_\Sigma(\mathbf{p})$ is a function of the edge credence vector $\mathbf{p} = (p_1, \ldots, p_m)$. The true plan value is $\Phi = P_\Sigma(\boldsymbol\theta)$. Define:

- **Credence-error mismatch:** $\boldsymbol\delta_c = \mathbf{p} - \boldsymbol\theta \in \mathbb{R}^m$
- **Value-residual mismatch:** $\delta_s = \hat P_\Sigma - \Phi = P_\Sigma(\mathbf{p}) - P_\Sigma(\boldsymbol\theta)$

The Jacobian of plan value with respect to credences is $\mathbf{J} = \nabla_{\mathbf{p}} P_\Sigma \in \mathbb{R}^m$. By first-order Taylor expansion:

$$\delta_s \approx \mathbf{J}^T \boldsymbol\delta_c$$

For the vector-valued case (multiple diagnostic targets), $\boldsymbol\delta_s = \mathbf{J} \boldsymbol\delta_c$ where $\mathbf{J}$ is an appropriate Jacobian matrix. We treat the scalar case first, then generalize.

### B.5a: Linear Correction (Beta-Bernoulli)

*[Derived (value-residual sector condition, linear case)]*

When the correction in credence space is linear — $\mathbf{F}_c(\boldsymbol\delta_c) = \boldsymbol\eta \odot \boldsymbol\delta_c$ where $\eta_k = 1/(n_k+1)$ and $\odot$ is elementwise product — the expected correction in value space is:

$$F_s(\delta_s) = \mathbf{J}^T (\boldsymbol\eta \odot \boldsymbol\delta_c) = \mathbf{J}^T (\boldsymbol\eta \odot \mathbf{J}^{-T} \delta_s)$$

But we don't need this inverse. Consider the sector ratio directly. Since $\delta_s = \mathbf{J}^T \boldsymbol\delta_c$ and $F_s = \mathbf{J}^T \mathbf{F}_c$:

$$\delta_s \cdot F_s = (\mathbf{J}^T \boldsymbol\delta_c)^T (\mathbf{J}^T \mathbf{F}_c) = \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \mathbf{F}_c$$

For the linear case $\mathbf{F}_c = \eta_{\min} \boldsymbol\delta_c$ (using the worst-case uniform gain for the bound):

$$\delta_s \cdot F_s = \eta_{\min} \cdot \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \boldsymbol\delta_c = \eta_{\min} \cdot \lVert\mathbf{J}^T \boldsymbol\delta_c\rVert^2 = \eta_{\min} \cdot \delta_s^2$$

Therefore:

$$\frac{\delta_s \cdot F_s}{\delta_s^2} = \eta_{\min}$$

**The Jacobian cancels.** The sector parameter in value-residual space equals the sector parameter in credence space, regardless of DAG structure:

$$\alpha_s = \alpha_c = \eta_{\min} = \min_k \frac{1}{n_k + 1}$$

This holds because $\mathbf{J}\mathbf{J}^T$ appears in both numerator and denominator of the sector ratio, and the linear correction commutes with the Jacobian mapping.

**Interpretation.** The Jacobian $\mathbf{J}$ determines *which* credence errors matter most for plan value (high-sensitivity edges contribute more to value residuals). But it does not change the *rate* at which those errors are corrected, because the correction is proportional to the error regardless of the error's plan-value impact.

### B.5b: Nonlinear Correction

*[Derived (Conditional on Jacobian regularity)]*

When the correction is nonlinear — $\mathbf{F}_c(\boldsymbol\delta_c)$ not proportional to $\boldsymbol\delta_c$ — the Jacobian no longer cancels. The sector condition transfers with a condition-number penalty.

**The general bound.** The credence-space sector condition gives $\boldsymbol\delta_c^T \mathbf{F}_c \geq \alpha_c \lVert\boldsymbol\delta_c\rVert^2$. We need $\delta_s \cdot F_s \geq \alpha_s \cdot \delta_s^2$.

Using $\delta_s = \mathbf{J}^T \boldsymbol\delta_c$ and $F_s = \mathbf{J}^T \mathbf{F}_c$:

$$\delta_s \cdot F_s = \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \mathbf{F}_c$$

and $\delta_s^2 = \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \boldsymbol\delta_c$.

Let $\mathbf{A} = \mathbf{J}\mathbf{J}^T$ (positive semidefinite, positive definite when $\mathbf{J}$ has full rank). In the $\mathbf{A}$-weighted inner product:

$$\frac{\delta_s \cdot F_s}{\delta_s^2} = \frac{\langle \boldsymbol\delta_c, \mathbf{F}_c \rangle_A}{\langle \boldsymbol\delta_c, \boldsymbol\delta_c \rangle_A}$$

This is the Rayleigh quotient of $\mathbf{F}_c$ with respect to $\boldsymbol\delta_c$ in the $\mathbf{A}$-weighted norm. The Euclidean sector condition gives $\langle \boldsymbol\delta_c, \mathbf{F}_c \rangle_I \geq \alpha_c \lVert\boldsymbol\delta_c\rVert_I^2$. To transfer to the $\mathbf{A}$-weighted inner product:

$$\langle \boldsymbol\delta_c, \mathbf{F}_c \rangle_A = \boldsymbol\delta_c^T \mathbf{A} \mathbf{F}_c$$

By Cauchy-Schwarz in the $\mathbf{A}$-norm and using the Euclidean sector condition:

$$\alpha_s \geq \alpha_c \cdot \frac{\sigma_{\min}(\mathbf{A})}{\sigma_{\max}(\mathbf{A})} = \alpha_c \cdot \frac{\sigma_{\min}(\mathbf{J})^2}{\sigma_{\max}(\mathbf{J})^2} = \frac{\alpha_c}{\kappa(\mathbf{J})^2}$$

where $\kappa(\mathbf{J}) = \sigma_{\max}(\mathbf{J})/\sigma_{\min}(\mathbf{J})$ is the condition number of the Jacobian.

**Interpretation.** The condition number $\kappa(\mathbf{J})$ measures how *anisotropic* the DAG's value sensitivity is across edges. When all edges contribute roughly equally to plan value ($\kappa \approx 1$), the transfer is near-lossless. When one edge dominates ($\kappa \gg 1$), the transfer loses a factor of $\kappa^2$ — the agent corrects the high-sensitivity edge efficiently but the low-sensitivity edge's correction doesn't register in value space.

**When $\kappa(\mathbf{J})$ is large.** For deep AND-chains, the root-to-leaf Jacobian entries span a large range (leaves deep in the chain have attenuated sensitivity). For wide OR-nodes with one dominant arm, the non-dominant arms have low sensitivity. In both cases, $\kappa(\mathbf{J})$ grows with structural complexity.

**When $\kappa(\mathbf{J})$ is small.** For shallow DAGs with comparable edge sensitivities (balanced AND/OR trees), $\kappa \approx 1$ and the nonlinear penalty is negligible.

### B.5c: Implications

Three regimes for the credence-to-value bridge:

| Correction type | DAG structure | Transfer | $\alpha_s$ |
|---|---|---|---|
| Linear (Beta-Bernoulli) | Any | Exact (Jacobian cancels) | $\alpha_c$ |
| Nonlinear | Well-conditioned ($\kappa \approx 1$) | Near-lossless | $\approx \alpha_c$ |
| Nonlinear | Ill-conditioned ($\kappa \gg 1$) | Lossy | $\alpha_c / \kappa^2$ |

**The linear case closes the gap completely.** For Beta-Bernoulli edge updates (Props B.1-B.4), the operational diagnostic $\delta_{\text{strategic}}$ inherits the sector condition from credence error with no penalty. The derivation appendix validates the operational mismatch, not merely a surrogate.

**The nonlinear case identifies a new fragility.** Deep or unbalanced DAGs have high $\kappa(\mathbf{J})$, making the value-residual sector condition harder to satisfy even when per-edge credence correction is adequate. This is a *structural* fragility: the DAG's value sensitivity anisotropy degrades the persistence guarantee. It provides a new formal argument for the structural pressure toward shallow, balanced strategies identified qualitatively in #chain-confidence-decay.

**Connection to credit assignment.** The Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$ is computable from the DAG's status propagation formulas — it does not require solving the credit-assignment problem. The credit-assignment problem is about *decomposing observed value changes into per-edge contributions* (needed for the update rule). The Jacobian bridge is about *transferring a per-edge sector condition to the value-residual space* (needed for the persistence guarantee). These are different problems: the bridge works even when credit assignment is unsolved, because it only requires the sensitivity structure, not the causal attribution.


## Epistemic Status

*Conditional on the Beta-Bernoulli model.* Propositions B.1, B.2, and B.4 are *derived*: the sector-condition verification is exact algebra under the stated generative model. The persistence conditions follow by direct application of Proposition A.1 ( #sector-condition-derivation), which is independently established. Proposition B.3(a) (the SA1 violation) is also derived; B.3(b) reduces to B.1 by construction. Proposition B.5a (the credence-to-value bridge for linear correction) is *exact* — the Jacobian cancellation is algebraic, independent of DAG structure. Proposition B.5b (the nonlinear transfer) is *conditional on Jacobian regularity* — the condition-number bound requires $\sigma_{\min}(\mathbf{J}) \gt 0$, which holds for non-degenerate DAGs.

All results use the *expected-value* sector condition. A full stochastic treatment (Foster-Lyapunov or supermartingale convergence) would give probability bounds rather than expected-value bounds. The expected-value analysis gives the correct asymptotic behavior (posterior concentration at $O(1/\sqrt{n})$) but does not prove almost-sure convergence. For the stationary Beta-Bernoulli case, almost-sure convergence is guaranteed by the standard Bayesian consistency theorem independently of this derivation.

The time-varying $\alpha_\Sigma$ issue remains: since $n_k$ increases with each observation, $\alpha_\Sigma$ decreases over time. The sector-condition framework assumes constant $\alpha$. The results here give an *instantaneous* persistence check at the current experience level, not a trajectory guarantee. Experience discounting (exponential forgetting with factor $\lambda$) stabilizes $\alpha_\Sigma$ at approximately $1 - \lambda$, yielding the persistence requirement $\lambda \lt 1 - \rho_\Sigma/R_\Sigma$.

**What remains open:**

1. *General DAG topology.* Only linear AND-chains and isolated OR-nodes are verified. Mixed AND/OR DAGs may exhibit interaction effects between evidence starvation and exploration gating.
2. *Continuous outcomes.* The Beta-Bernoulli model gives conjugate, closed-form updates. Non-conjugate cases (continuous signals, partial observability) require approximate inference, and the sector condition must be verified for the approximation.
3. *Modified sector condition for biased correction.* The $O(1/n)$ bias in the unobservable case (B.3a) could be accommodated by a sector-condition variant tolerating asymptotically vanishing bias, potentially recovering per-edge results.
4. *Correlated edges.* All cases assume independent edges. Shared infrastructure or common-mode failures would introduce additional coupling.
5. *Adaptive exploration.* Proposition B.4 uses fixed $\varepsilon$. Adaptive strategies (UCB, Thompson sampling) allocate exploration based on current uncertainty and should yield tighter sector bounds.


## Discussion

**The sector parameter is the edge update gain.** Across all four cases, $\alpha_\Sigma$ is a function of $\eta_k = 1/(n_k+1)$ --- the same quantity that governs epistemic persistence ( #adaptive-tempo, #update-gain). Strategic persistence and epistemic persistence are governed by the same mathematical machinery, not merely structurally parallel. This validates the schema proposed in #strategy-persistence-schema at the level of concrete dynamics.

**AND vs. OR: structural vs. behavioral fragility.** The evidence-starvation effect (B.2) is structural --- it depends on the DAG topology and upstream reliability, not on the agent's policy. The exploration-gating effect (B.4) is behavioral --- it depends on the action-selection policy. AND-node persistence is improved by increasing upstream reliability (making early steps more likely to succeed). OR-node persistence is improved by increasing exploration (testing alternatives more frequently). The distinction maps to the familiar depth-vs-breadth tradeoff in planning.

**Gain collapse as the dominant failure mode.** In every drifting-environment case, the persistence threshold takes the form $n \lt c/\rho_\Sigma$ for some constant $c$. Accumulated experience suppresses the update gain, eventually making the agent unable to track environmental change. This gives the gain-collapse phenomenon ( #update-gain) a precise quantitative threshold for each topology.
