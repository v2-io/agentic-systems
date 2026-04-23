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

**Parameterization note.** Propositions B.1–B.7 below are stated in the *moment-parameter* (probability-space) coordinate $\hat p_k \in [0, 1]$, consistent with the Beta-Bernoulli conjugate presentation. The log-odds coordinate $\lambda_k = \log(\hat p_k / (1 - \hat p_k)) \in \mathbb{R}$ is the unique additive-evidence presentation forced by the evidential-additivity axiom ( #edge-update-natural-parameter); the sector-parameter content of each proposition is Fisher-equivalent in either coordinate, so the derivations are retained in moment-parameter form for algebraic tightness ($\eta_k = 1/(n_k + 1)$ is exact in probability space). The log-odds coordinate becomes load-bearing in #credit-assignment-boundary for the continuous-gradient signal function, where the probability-space presentation would exhibit a mechanical domain break.

Strategic mismatch per edge is $\delta_k = \hat p_k - \theta_k$. The sector-condition framework ( #sector-condition-derivation) requires: (SA1) $F(\mathbf{0}) = \mathbf{0}$, (SA2') $\boldsymbol{\delta}^T \mathbf{F}(\boldsymbol{\delta}) \geq \alpha_\Sigma \lVert\boldsymbol{\delta}\rVert^2$ within a region $\mathcal B_R$.

### Regime-adjustment convention

The propositions below state sector parameters $\alpha_\Sigma$ for the **canonical Regime-A case**, in which every edge's evidence is fully interventional and attributable (identifiability coefficient $\iota_{ij} = 1$ per #edge-update-causal-validity). For edges with $\iota_{ij} \lt 1$ (Regime B or C), each sector parameter carries an implicit $\iota_{ij}$ factor:

$$\alpha_\Sigma^{\text{eff}} = \iota_{ij} \cdot \alpha_\Sigma^{\text{stated}}$$

This commutes through every diagonal sector product in Props B.1–B.4 and B.6 because each edge's contribution to $\boldsymbol\delta_\Sigma^T \mathbf{F}$ is scaled by $\iota_{ij}$ independently: Regime-C edges ($\iota \approx 0$) contribute essentially nothing to the weakest-link minimum, and Regime-A edges ($\iota \approx 1$) recover the stated formulas exactly. The persistence condition $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ becomes $\iota_{ij} \cdot \alpha_\Sigma^{\text{stated}} \gt \rho_{\Sigma,ij}/R_{\Sigma,ij}$ per edge. The propositions below state everything in Regime-A form for clarity; the $\iota$-adjustment is uniform across cases and does not alter the structural results (evidence starvation, exploration gating, three-way gating) — only their quantitative thresholds per edge.

For Prop B.3 (unobservable intermediate), the regime adjustment does not change the A1 violation result: the bias is structural to the marginal Bayesian update, not to the identifiability quality. The plan-level fallback still recovers the sector condition with an $\iota$-adjusted $\alpha_{\Sigma,\text{plan}}$ governed by the aggregate's identifiability.


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


## Proposition B.6: Mixed AND/OR with Common-Cause Node (L1 Augmented DAG)

**Setup.** Goal $G$ reachable via two alternative actions $A_1, A_2$ (an OR-node), but both actions require a shared condition $C$ (a common-cause node). The L1 DAG factors the common cause above the OR-structure: $G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}} = \text{OR}(A_1, A_2)$. Three leaves: condition $C$ with true probability $\theta_C$, actions $A_1, A_2$ with true conditional probabilities $\theta_{1\mid C}, \theta_{2\mid C}$. Agent selects $\varepsilon$-greedy among $A_1, A_2$ (only testable when $C = 1$). Mismatch vector: $\boldsymbol\delta_\Sigma = (\delta_C, \delta_{A_1}, \delta_{A_2})^T$.

Plan confidence: $\hat P_\Sigma = \hat p_C \cdot [1 - (1 - \hat p_{A_1})(1 - \hat p_{A_2})]$. Reference value: $\Phi = \theta_C \cdot [1 - (1 - \theta_{1\mid C})(1 - \theta_{2\mid C})]$. At truth, $\hat P_\Sigma = \Phi =$ actual plan success probability (L1 is unbiased).

**Statement.** Under Beta-Bernoulli updating with observable condition $C$ and $\varepsilon$-greedy path selection, the expected correction function satisfies the sector condition globally with:

*[Derived (Conditional on Beta-Bernoulli model, L1 augmented DAG, observable common cause $C$, $\varepsilon$-greedy action selection)]*

$$\alpha_\Sigma = \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C(1-\varepsilon)}{n_{A_1}+1},\; \frac{\theta_C \varepsilon}{n_{A_2}+1}\right)$$

where $A_1$ is the greedy choice.

**Proof.**

Edge $C$ (condition leaf, observed every trial):

$$\mathbb{E}[\Delta \hat p_C] = \frac{\theta_C - \hat p_C}{n_C + 1} = -\frac{\delta_C}{n_C+1}$$

Edge $A_1$ (action leaf, tested when $C = 1$ and path 1 selected — probability $\theta_C(1-\varepsilon)$):

$$\mathbb{E}[\Delta \hat p_{A_1}] = -\frac{\theta_C(1-\varepsilon)\,\delta_{A_1}}{n_{A_1}+1}$$

Edge $A_2$ (action leaf, tested when $C = 1$ and path 2 selected — probability $\theta_C \varepsilon$):

$$\mathbb{E}[\Delta \hat p_{A_2}] = -\frac{\theta_C \varepsilon\,\delta_{A_2}}{n_{A_2}+1}$$

The expected correction function is diagonal:

$$\mathbf{F}(\boldsymbol\delta_\Sigma) = \begin{pmatrix} \delta_C/(n_C+1) \\ \theta_C(1-\varepsilon)\,\delta_{A_1}/(n_{A_1}+1) \\ \theta_C \varepsilon\,\delta_{A_2}/(n_{A_2}+1) \end{pmatrix}$$

**Verification of (SA1).** $\mathbf{F}(\mathbf{0}) = \mathbf{0}$. ✓

**Sector product:**

$$\boldsymbol\delta_\Sigma^T \mathbf{F} = \frac{\delta_C^2}{n_C+1} + \frac{\theta_C(1-\varepsilon)\,\delta_{A_1}^2}{n_{A_1}+1} + \frac{\theta_C\varepsilon\,\delta_{A_2}^2}{n_{A_2}+1} \;\geq\; \alpha_\Sigma \lVert\boldsymbol\delta_\Sigma\rVert^2 \quad\square$$

**Three-way gating.** This is the first mixed AND/OR case. The sector parameter $\alpha_\Sigma$ is determined by three independent gating mechanisms:
1. **Condition testing** ($1/(n_C+1)$): the common cause is the easiest component to calibrate — tested every trial, same as B.1.
2. **Evidence starvation** ($\theta_C$ factor on action terms): both action edges are gated by the condition probability, same mechanism as B.2.
3. **Exploration gating** ($(1-\varepsilon)$ and $\varepsilon$ factors): the two OR-alternatives compete for test opportunities, same mechanism as B.4.

The bottleneck is typically the explore action behind the condition: $\theta_C \varepsilon / (n_{A_2}+1)$.

**B.5b applies.** The Jacobian $\mathbf{J} = (s_{G_{\text{sub}}},\; \hat p_C(1 - \hat p_{A_2}),\; \hat p_C(1 - \hat p_{A_1}))^T$ is non-negative (monotone AND/OR). Corrections are componentwise (each leaf updates independently). Therefore $\alpha_s = \alpha_c = \alpha_\Sigma$ — the plan-confidence error inherits the sector condition with no penalty.

**Optimal exploration.** Equalizing the action terms: $\varepsilon^\ast = (n_{A_1}+1)/(n_{A_1}+n_{A_2}+2)$, giving $\alpha_\Sigma^\ast = \min(1/(n_C+1),\;\theta_C/(n_{A_1}+n_{A_2}+2))$.

**L0 comparison.** An L0 model of the same scenario (no $C$ node, marginal probabilities $\theta_k = \theta_C \cdot \theta_{k\mid C}$) has $\alpha_\Sigma^{L0} = \min((1-\varepsilon)/(n_1+1),\;\varepsilon/(n_2+1))$ and reference value $\Phi^{L0} = 1 - (1-\theta_1)(1-\theta_2)$. The L0 sector parameter is *higher* (no $\theta_C$ attenuation) but $\Phi^{L0}$ systematically overestimates actual plan success. L1 persistence is harder (lower $\alpha_\Sigma$) but calibration is honest ($\Phi^{L1}$ matches reality). The tradeoff: L0 is easier to maintain but calibrates to a biased target; L1 is harder to maintain but calibrates to truth.

**The L1 construction principle.** The common-cause node $C$ must be factored *above* the OR-structure whose children it correlates. A naive construction (adding $C$ as a parent of both $A_1$ and $A_2$ while keeping them as OR-siblings) does not fix the overestimation because the OR-propagation formula treats siblings as marginally independent. Correct L1 construction makes $C$ an AND-prerequisite above the OR-structure, so the OR-children are conditionally independent given $C$. Full worked example with quantitative L0/L1 comparison: #worked-example-L1.


## Summary of Results

| Case | Topology | $\alpha_\Sigma$ | SA1 | SA3 | Weakest link |
|------|----------|-----------------|-----|-----|-------------|
| **B.1** Single edge | $A \to G$ | $1/(n+1)$ | Yes | N/A | --- |
| **B.2** Two-edge, $B$ observable | $A \to B \to G$ (AND) | $\min(1/(n_1\!+\!1),\;\theta_1/(n_2\!+\!1))$ | Yes | N/A | Depth-gated (evidence starvation) |
| **B.3** Two-edge, $B$ unobservable | $A \to B \to G$ (AND) | $1/(n_\Phi\!+\!1)$ (plan-level) | Per-edge: No ($O(1/n)$ bias); Plan: Yes | N/A | Credit-assignment collapse |
| **B.4** Two-arm OR, $\varepsilon$-greedy | $A_1, A_2 \to G$ (OR) | $\min((1\!-\!\varepsilon)/(n_1\!+\!1),\;\varepsilon/(n_2\!+\!1))$ | Yes | Required | Exploration-gated |
| **B.5a** Credence→value (linear) | Any | $\alpha_s = \alpha_c$ (Jacobian cancels) | — | — | None (exact transfer) |
| **B.5b** Credence→value (nonlinear, componentwise) | Any | $\alpha_s = \alpha_c$ ($J_k \geq 0$ preserves bound) | — | — | None (exact transfer) |
| **B.5b** Credence→value (coupled) | Any | $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$ | — | — | Inter-edge coupling |
| **B.6** L1 augmented, mixed AND/OR | $G = \text{AND}(C, \text{OR}(A_1, A_2))$ | $\min(1/(n_C\!+\!1),\;\theta_C(1\!-\!\varepsilon)/(n_{A_1}\!+\!1),\;\theta_C\varepsilon/(n_{A_2}\!+\!1))$ | Yes | Required | Three-way gating |
| **B.7** L1' mixture form, observable $C$ | $\hat P_\Sigma^{L1'} = \hat\theta_C P_\Sigma(\hat{\mathbf p}_{\mid C}) + (1\!-\!\hat\theta_C) P_\Sigma(\hat{\mathbf p}_{\mid \neg C})$ | $\min(1/(n_C\!+\!1),\;\min_j \theta_C\pi_{j\mid C}/(n_{j\mid C}\!+\!1),\;\min_j (1\!-\!\theta_C)\pi_{j\mid \neg C}/(n_{j\mid \neg C}\!+\!1))$ | Yes | Required *and* facilitator monotonicity | Five-way gating; **refuted under unobservable $C$** (Cramér-Rao floor) |

**Structural results across cases:**

- **Gain as sector parameter.** In every case, $\alpha_\Sigma$ is determined by the edge update gain $\eta_k = 1/(n_k+1)$, modulated by observability ($\theta_1$ attenuation in B.2), credit-assignment (plan-level collapse in B.3), action-selection policy ($\varepsilon$ in B.4), or a combination of these (B.6). The structural parallel between epistemic and strategic persistence is not an analogy --- it is a mathematical identity at the sector-framework level.
- **Evidence starvation (AND-chains).** Downstream edges in AND-chains have correction rates attenuated by the product of upstream success probabilities. Depth increases fragility: $\alpha_\Sigma$ decays exponentially with chain depth.
- **Exploration gating (OR-nodes).** Unchosen OR-alternatives receive zero correction. The sector condition requires deliberate exploration (SA3) at a rate exceeding $\rho_\Sigma(n_{\max}+1)/R_\Sigma$. Pure greedy policies fail.
- **Three-way gating (L1 augmented).** When a common cause gates OR-alternatives, calibration faces condition testing, evidence starvation, and exploration gating simultaneously (B.6). The bottleneck is the least-explored action behind the rarest condition.
- **Five-way gating (L1' mixture, observable $C$).** When the common cause is a *soft facilitator* ($\theta_{j\mid \neg C} \gt 0$) and is observable per trial, calibration faces five gating mechanisms simultaneously (B.7): condition testing, evidence starvation on each conditional branch ($C=1$ and $C=0$), and exploration gating on each branch. The bottleneck is whichever branch is rarer, modulated by exploration on that branch. **Identifiability obstruction under unobservable $C$:** without direct $C$-observation, the mixture parameters are non-identifiable from a single observation channel — the per-trial Fisher information matrix is rank 1 rather than rank $2K+1$, so by the Cramér-Rao bound (Cramér 1946, *Mathematical Methods of Statistics*, Princeton University Press) no unbiased online estimator on the joint conditional vector admits $\alpha \gt 0$. The agent must augment $C$-observability, run multi-child joint observations, or fall back to plan-level (L0-on-marginals) tracking.
- **Gain-collapse threshold.** In all cases, increasing experience eventually violates persistence when the environment drifts. The critical experience level $n^\ast$ is inversely proportional to the drift rate $\rho_\Sigma$.
- **L1 tradeoff.** L1 augmented DAGs have lower $\alpha_\Sigma$ (harder to persist) but honest calibration ($\Phi^{L1}$ matches reality). L0 is easier to maintain but calibrates to a biased target. The choice depends on whether accuracy or trackability is the binding constraint.


## Proposition B.7: L1' Mixture-Form Sector Transfer (Observable Common Cause)

Where Prop B.6 handles a strict-prerequisite common cause via an AND-prerequisite construction (L1), this proposition handles a *soft-facilitator* common cause via the mixture form L1' ( #strategy-dag, Correlation Hierarchy). It is the L1' analog of B.6, generalizing three-way gating to five-way gating across two parallel conditional branches.

### Setup

L1' (mixture-form) DAG with binary common cause $C$, true prior $\theta_C \in (0,1)$, gating a sub-plan with conditional structures $G_{\mid C}$ (when $C=1$) and $G_{\mid \neg C}$ (when $C=0$). Each affected child $j$ carries two conditional credences $\hat p_{j\mid C}$ and $\hat p_{j\mid \neg C}$. Plan confidence:

$$\hat P_\Sigma^{L1'} = \hat\theta_C \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid C}) + (1-\hat\theta_C) \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C})$$

The agent observes $C$-state directly each trial (i.e., $C$ is treated as an observable condition leaf, in parallel with B.6). Per trial, the agent (i) updates $\hat\theta_C$ from observed $C$ via Beta-Bernoulli; (ii) on $C=1$ trials, attempts a child $j$ via the active selection policy $\pi_{\mid C}$ and updates $\hat p_{j\mid C}$ from $y_j$; (iii) on $C=0$ trials, attempts a child $j$ via $\pi_{\mid \neg C}$ and updates $\hat p_{j\mid \neg C}$ from $y_j$.

Mismatch state: $\boldsymbol\xi = (\xi_C, \{\xi_{j\mid C}\}, \{\xi_{j\mid \neg C}\})$ with $\xi_C = \theta_C - \hat\theta_C$, $\xi_{j\mid s} = \theta_{j\mid s} - \hat p_{j\mid s}$.

### Statement

*[Derived (Conditional on Beta-Bernoulli model, observable common cause $C$, componentwise conditional-branch update, facilitator monotonicity)]*

Under Beta-Bernoulli updating with observable common cause, componentwise updates per conditional branch, and *facilitator monotonicity* ($P_\Sigma(G_{\mid C}) \geq P_\Sigma(G_{\mid \neg C})$), the expected correction function on the joint state satisfies the sector condition globally with:

$$\alpha_{L1'} = \min\!\left(\frac{1}{n_C+1},\; \min_{j \in \mathcal{J}_C}\frac{\theta_C \pi_{j\mid C}}{n_{j\mid C}+1},\; \min_{j \in \mathcal{J}_{\neg C}}\frac{(1-\theta_C)\pi_{j\mid \neg C}}{n_{j\mid \neg C}+1}\right)$$

where $\mathcal J_s$ is the set of children tested on the $C=s$ branch and $\pi_{j\mid s}$ is the action-selection probability for child $j$ on that branch.

### Proof

*Edge $C$ (condition leaf, observable every trial).* Standard Beta-Bernoulli on direct $C$-observation:

$$\mathbb{E}[\Delta\hat\theta_C] = \frac{\theta_C - \hat\theta_C}{n_C+1} = -\frac{\xi_C}{n_C+1}$$

so $F_C(\boldsymbol\xi) = \xi_C/(n_C+1)$.

*Edge $p_{j\mid C}$ (conditional credence, $C=1$ branch).* Tested when $C=1$ (probability $\theta_C$) and the agent's $C=1$-conditional policy selects $j$ (probability $\pi_{j\mid C}$):

$$\mathbb{E}[\Delta\hat p_{j\mid C}] = \theta_C \pi_{j\mid C} \cdot \frac{\theta_{j\mid C} - \hat p_{j\mid C}}{n_{j\mid C}+1} = -\frac{\theta_C \pi_{j\mid C} \xi_{j\mid C}}{n_{j\mid C}+1}$$

so $F_{j\mid C}(\boldsymbol\xi) = \theta_C \pi_{j\mid C} \xi_{j\mid C}/(n_{j\mid C}+1)$.

*Edge $p_{j\mid \neg C}$ (conditional credence, $C=0$ branch).* Symmetric: tested with probability $(1-\theta_C)\pi_{j\mid \neg C}$:

$$F_{j\mid \neg C}(\boldsymbol\xi) = \frac{(1-\theta_C)\pi_{j\mid \neg C} \xi_{j\mid \neg C}}{n_{j\mid \neg C}+1}$$

*Sector product.* The correction function is diagonal in $\boldsymbol\xi$ with positive entries:

$$\boldsymbol\xi^T \mathbf F(\boldsymbol\xi) = \frac{\xi_C^2}{n_C+1} + \sum_{j \in \mathcal{J}_C}\frac{\theta_C \pi_{j\mid C} \xi_{j\mid C}^2}{n_{j\mid C}+1} + \sum_{j \in \mathcal{J}_{\neg C}}\frac{(1-\theta_C)\pi_{j\mid \neg C} \xi_{j\mid \neg C}^2}{n_{j\mid \neg C}+1} \;\geq\; \alpha_{L1'} \cdot \lVert\boldsymbol\xi\rVert^2$$

with $\alpha_{L1'}$ as stated.

*SA1 check.* $\mathbf F(\mathbf 0) = \mathbf 0$ at truth ($\boldsymbol\xi = 0$). ✓

*Globality.* The Beta-Bernoulli updates are linear in $\boldsymbol\xi$ on $[-1, 1]^{2K+1}$, so the diagonal Jacobian computed at truth is the exact $\mathbf J_{\mathbf F}$ throughout. The sector inequality holds globally with the same $\alpha_{L1'}$.

*B.5b bridge to plan value.* Jacobian of $\hat P_\Sigma^{L1'}$ with respect to the joint state:

$$\mathbf{J}_{P_\Sigma} = \begin{pmatrix} P_\Sigma(\hat{\mathbf{p}}_{\mid C}) - P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C}) \\ \hat\theta_C \cdot \nabla_{\hat{\mathbf{p}}_{\mid C}} P_\Sigma(\hat{\mathbf{p}}_{\mid C}) \\ (1-\hat\theta_C) \cdot \nabla_{\hat{\mathbf{p}}_{\mid \neg C}} P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C}) \end{pmatrix}$$

By facilitator monotonicity, the first entry is $\geq 0$. The other entries are $\geq 0$ by AND/OR monotonicity on each conditional sub-DAG. So $\mathbf J_{P_\Sigma} \geq 0$ componentwise. By the componentwise nonlinear case of B.5b, the sector condition transfers losslessly: $\alpha_s = \alpha_c = \alpha_{L1'}$. $\square$

### Five-Way Gating

This generalizes B.6's three-way gating to five gating mechanisms, one per term in the $\min$:

1. **Condition testing** ($1/(n_C+1)$): the common cause is the easiest component to calibrate — directly observed every trial.
2. **Evidence starvation, $C=1$ branch** ($\theta_C$ factor): conditional edges on the $C=1$ branch are gated by the prior frequency of $C=1$.
3. **Exploration gating, $C=1$ branch** ($\pi_{j\mid C}$ factor): OR-alternatives within the $C=1$ branch compete for test opportunities.
4. **Evidence starvation, $C=0$ branch** ($1-\theta_C$ factor): conditional edges on the $C=0$ branch are gated by the prior frequency of $C=0$.
5. **Exploration gating, $C=0$ branch** ($\pi_{j\mid \neg C}$ factor): OR-alternatives within the $C=0$ branch.

The bottleneck is typically whichever of $\theta_C$ and $1-\theta_C$ is smaller (the rare branch sees fewer trials), modulated by exploration on that branch.

### Reduction to B.6 (Strict-Prerequisite Limit)

Setting $\theta_{j\mid \neg C} \to 0$ collapses the $\neg C$ branch (the agent learns the $\neg C$ conditionals are zero with no remaining variance). The per-edge state for the $\neg C$ branch drops out of the sector inequality, and the formula reduces to B.6's three-way gating with $\alpha_\Sigma = \min(1/(n_C+1), \theta_C(1-\varepsilon)/(n_{A_1}+1), \theta_C\varepsilon/(n_{A_2}+1))$. ✓

### Refuted Under Unobservable $C$ (Mixture Identifiability Obstruction)

*[Derived (cramer-rao-floor, from Fisher information of mixture model + Cramér-Rao bound)]*

When $C$ is not observable, the agent can only update the joint state via online soft EM on the marginal $y_j$. Computing the Fisher information of the mixture model $\mu_j = \theta_C \theta_{j\mid C} + (1-\theta_C)\theta_{j\mid \neg C}$ at truth, the score vector for parameters $\phi = (\theta_C, p_{j\mid C}, p_{j\mid \neg C})$ admits the rank-1 factorization:

$$\mathcal{F}(\phi) = \frac{1}{\mu_j(1-\mu_j)}\, u u^T, \qquad u = (\Delta_j,\; \theta_C,\; 1-\theta_C)$$

where $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ is the *separability gap*. The matrix is rank 1 for any non-degenerate mixture; the two-dimensional null space corresponds to perturbations along the indeterminacy manifold $\{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1-\hat\theta_C) \hat p_{\mid \neg C} = \mu_j\}$ — directions unobservable from a single binary signal.

Since the soft-EM step at truth equals (up to the $1/(n+1)$ scaling) the natural-gradient ascent on the expected log-likelihood, the Jacobian of the correction function equals $\mathcal F / (n+1)$, also rank 1. Therefore $\lambda_{\min}(\mathbf J_F) = 0$, and **no SA1-preserving update on the joint conditional vector admits a sector parameter $\alpha \gt 0$ under SUB-B.** This is a Cramér-Rao bound, not a defect of any particular update rule: any unbiased online estimator must respect the bound, which is infinite in the unidentifiable directions.

**Repair routes.** When $C$ is unobservable, the agent must:

(i) **Augment $C$-observability** (recover B.7 above) — instrument secondary signals that identify $C$ per trial, transforming the problem from refuted to globally derived.
(ii) **Run $K \geq 2$ children jointly under the same $C$-realization** — when the joint Fisher matrix reaches rank $2K+1$, the mixture is identifiable; local sector condition holds with $\alpha \geq \sigma_{\min}(\mathcal F_{\text{joint}})/\max_k(n_k+1)$. Strong structural requirement (joint observation typically unavailable in standard sequential strategy execution).
(iii) **Fall back to plan-level tracking on the marginal $\hat\mu_j$** — recovers B.1's $\alpha = 1/(n_\mu+1)$ on the scalar marginal but loses the per-conditional decomposition (equivalent to L0-on-marginals).

### Connection to the Identifiability-Floor Pattern

The B.7-vs-refuted-unobservable-$C$ structure is one of two no-go theorems in AAD's strategy layer. The other is the on-policy detection no-go in #causal-insufficiency-detection, which prohibits L0-vs-L1 distinction from purely on-policy data via the causal hierarchy theorem. Both are structural impossibility results derived from external information-theoretic theorems (Bareinboim et al. 2022 Causal Hierarchy Theorem; Cramér-Rao bound on the Fisher information). Both strengthen related machinery — the on-policy no-go strengthens #loop-interventional-access; the mixture no-go strengthens the case for *observability-as-information-augmentation*. See #discussion-identifiability-floor for the meta-pattern.


## Proposition B.5: Bridge from Credence Error to Value Residuals

The propositions above verify the sector condition for the credence-error mismatch state $\boldsymbol\delta_c = (\hat p_k - \theta_k)$. This proposition extends the result to **plan-confidence error** — the scalar difference between the agent's plan-confidence score and the independence-model plan value evaluated at true edge parameters. This is a natural plan-level mismatch that is distinct from (but related to) the per-edge value-increment residuals $\delta_{\text{strategic}}$ defined in #strategic-calibration.

**Relationship to $\delta_{\text{strategic}}$.** #strategic-calibration defines $\delta_{\text{strategic}}$ as an $L^2$ aggregation of per-edge value-increment residuals — a quantity that requires credit assignment to compute. Plan-confidence error $\delta_s$ defined here is a *different* quantity: it is the error in the DAG's aggregate self-assessment, computable from status propagation without credit assignment. The two are related (both measure strategy-reality mismatch) but not identical. This proposition shows the sector condition holds for plan-confidence error; extending it to $\delta_{\text{strategic}}$ directly would require the credit-assignment machinery discussed in #credit-assignment-boundary.

### Setup

The plan value $\hat P_\Sigma = P_\Sigma(\mathbf{p})$ is a function of the edge credence vector $\mathbf{p} = (p_1, \ldots, p_m)$. The **independence-model reference value** is $\Phi = P_\Sigma(\boldsymbol\theta)$ — the AND/OR propagation formula evaluated at the true edge parameters $\boldsymbol\theta$. Note: $\Phi$ is NOT the actual probability of plan success when edge outcomes are correlated ( #strategy-dag, edge-independence caveat). It is the best the independence model can do with perfect edge knowledge. Under correlated failure, the actual plan success probability may be lower than $\Phi$; the gap is a model-class limitation of the AND/OR DAG representation, not an estimation error. What $\delta_s$ tracks is calibration *within the independence model*, not calibration to reality. Define:

- **Credence-error mismatch:** $\boldsymbol\delta_c = \mathbf{p} - \boldsymbol\theta \in \mathbb{R}^m$
- **Plan-confidence error:** $\delta_s = \hat P_\Sigma - \Phi = P_\Sigma(\mathbf{p}) - P_\Sigma(\boldsymbol\theta)$ (scalar)

The gradient of plan value with respect to credences is $\mathbf{J} = \nabla_{\mathbf{p}} P_\Sigma \in \mathbb{R}^m$ (a vector, since $P_\Sigma$ is scalar). By first-order Taylor expansion:

$$\delta_s \approx \mathbf{J}^T \boldsymbol\delta_c$$

### B.5a: Linear Correction (Beta-Bernoulli)

*[Derived (value-residual sector condition, linear case)]*

When the correction in credence space is linear — $\mathbf F_c(\boldsymbol\delta_c) = \boldsymbol\eta \odot \boldsymbol\delta_c$ where $\eta_k = 1/(n_k+1)$ and $\odot$ is elementwise product — consider the sector ratio directly. Since $\delta_s = \mathbf{J}^T \boldsymbol\delta_c$ and $F_s = \mathbf{J}^T \mathbf F_c$:

$$\delta_s \cdot F_s = (\mathbf{J}^T \boldsymbol\delta_c)^T (\mathbf{J}^T \mathbf{F}_c) = \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \mathbf{F}_c$$

For the linear case $\mathbf F_c = \eta_{\min} \boldsymbol\delta_c$ (using the worst-case uniform gain for the bound):

$$\delta_s \cdot F_s = \eta_{\min} \cdot \boldsymbol\delta_c^T \mathbf{J} \mathbf{J}^T \boldsymbol\delta_c = \eta_{\min} \cdot \lVert\mathbf{J}^T \boldsymbol\delta_c\rVert^2 = \eta_{\min} \cdot \delta_s^2$$

Therefore:

$$\frac{\delta_s \cdot F_s}{\delta_s^2} = \eta_{\min}$$

**The Jacobian cancels.** The sector parameter in value-residual space equals the sector parameter in credence space, regardless of DAG structure:

$$\alpha_s = \alpha_c = \eta_{\min} = \min_k \frac{1}{n_k + 1}$$

This holds because $\mathbf{J}\mathbf{J}^T$ appears in both numerator and denominator of the sector ratio, and the linear correction commutes with the Jacobian mapping.

**Interpretation.** The Jacobian $\mathbf{J}$ determines *which* credence errors matter most for plan value (high-sensitivity edges contribute more to value residuals). But it does not change the *rate* at which those errors are corrected, because the correction is proportional to the error regardless of the error's plan-value impact.

### B.5b: Nonlinear Componentwise Correction

*[Derived (from per-component sector condition + Jacobian non-negativity)]*

When the correction is nonlinear but **componentwise** — each edge corrects independently, so $(\mathbf F_c)_k$ depends only on $(\boldsymbol\delta_c)_k$ — and the plan-value Jacobian is **non-negative** ($J_k \geq 0$ for all $k$), the transfer is lossless regardless of nonlinearity.

**The per-component sector condition** (from Props B.1-B.4): for each edge $k$,

$$(\boldsymbol\delta_c)_k \cdot (\mathbf{F}_c)_k \geq \alpha_c \cdot (\boldsymbol\delta_c)_k^2$$

which gives $(\mathbf F_c)_k / (\boldsymbol\delta_c)_k \geq \alpha_c$ (the correction-to-mismatch ratio exceeds $\alpha_c$ for each edge independently).

**Jacobian non-negativity** holds for all well-formed AND/OR DAGs: increasing any edge credence $p_k$ never decreases plan value $P_\Sigma$ (monotonicity of AND/OR propagation). Therefore $J_k = \partial P_\Sigma / \partial p_k \geq 0$ for all $k$.

**The transfer.** Since $J_k \geq 0$ preserves the inequality direction:

$$J_k \cdot (\mathbf{F}_c)_k \geq J_k \cdot \alpha_c \cdot (\boldsymbol\delta_c)_k \quad \text{for each } k$$

Summing:

$$\mathbf{J}^T \mathbf{F}_c = \sum_k J_k (\mathbf{F}_c)_k \geq \alpha_c \sum_k J_k (\boldsymbol\delta_c)_k = \alpha_c \cdot \mathbf{J}^T \boldsymbol\delta_c$$

Therefore $F_s \geq \alpha_c \cdot \delta_s$, giving:

$$\alpha_s = \alpha_c$$

**No condition-number penalty.** The Jacobian's anisotropy is irrelevant when the correction is componentwise and the Jacobian is non-negative. The non-negativity ensures that every edge's correction contributes in the right direction to the value correction, regardless of how unevenly the Jacobian weights different edges.

**When does componentwise correction hold?** For all cases in Props B.1, B.2, and B.4 — the standard Beta-Bernoulli update on each edge, including the stochastic (nonlinear) single-step realization. The correction IS nonlinear (the actual per-step update $(y - \hat p)/(n+1)$ is random, not proportional to $\delta_k$), but it is componentwise (each edge updates from its own observation independently).

**When does it fail?** When edge corrections are coupled — correcting one edge changes another's correction direction. This occurs for:
- **Unobservable intermediates (B.3) under marginal Bayesian updates:** The marginal Bayesian update couples edge posteriors. The correction for edge 2 depends on the joint posterior over both edges, not just on $(\boldsymbol\delta_c)_2$ alone. *And — critically — Prop B.3(a) showed that this scheme violates SA1 with $O(1/n)$ bias: there is no valid $\alpha_c$ for the marginal Bayesian update on coupled edges in the first place.* The per-edge bound must therefore be re-established before the Jacobian transfer can be applied.
- **Shared observations:** If testing one arm gives partial information about another (correlated arms), corrections couple across edges — with an SA1 status that depends on the specific attribution scheme used to project the shared observation onto per-edge updates.

*[Scope (coupled-case-applicability)]*

**The coupled-case Cauchy-Schwarz bound presupposes a valid $\alpha_c$.** For the bound $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$ to apply meaningfully, the per-edge sector condition must hold — i.e., the attribution scheme must satisfy SA1. Marginal Bayesian updates on coupled edges do *not* satisfy this precondition (Prop B.3(a)). The resolution is to replace marginal Bayesian with **gradient-based attribution** (Prop B.5d below), which recovers SA1 and yields a valid per-edge sector parameter that admits the Jacobian transfer with the $\kappa^2$ penalty.

**Per-edge vs. plan-level routes through coupling.** Prop B.3(b) already established an alternative route for the two-edge unobservable case: tracking at the plan level ($\hat\Phi = \hat p_1 \hat p_2$) with a single Beta posterior recovers SA1 directly, yielding $\alpha_\Sigma = 1/(n_\Phi + 1)$. The plan-level route works *without* needing the Jacobian bridge because it sidesteps per-edge attribution entirely. The gradient-based per-edge route works *through* the Jacobian bridge, preserving per-edge credences at the cost of the $\kappa^2$ penalty. Both routes give valid sector parameters; the choice depends on whether per-edge diagnostics or aggregate efficiency matters more.

**The refined picture: nonlinearity is not the problem; inter-edge coupling combined with the attribution scheme is.** A nonlinear but componentwise correction transfers losslessly through any non-negative Jacobian. A coupled correction under a scheme that preserves SA1 (gradient-based) incurs the condition-number penalty because the coupling can redirect correction away from the value-relevant direction. A coupled correction under a scheme that violates SA1 (marginal Bayesian) has no valid $\alpha_c$ to transfer at all and must be replaced before B.5 applies.

### Proposition B.5d: Gradient-Based Attribution Restores SA1 on Coupled Edges

**Setup.** Same two-edge AND topology as B.3: edges with true probabilities $\theta_1, \theta_2$, credences $\hat p_1, \hat p_2$, plan probability $\hat P_\Sigma = \hat p_1 \hat p_2$, observable plan outcome $y_G \in \{0, 1\}$ with $\mathbb E[y_G] = \Phi = \theta_1 \theta_2$. Intermediate is unobservable.

**Gradient-based per-edge update.** Distribute plan-level surprise proportionally to the Jacobian component:

*[Formulation (gradient-attribution)]*

$$\Delta \hat p_k \;=\; \frac{1}{n_k + 1} \cdot J_k \cdot (y_G - \hat P_\Sigma), \qquad J_k = \frac{\partial \hat P_\Sigma}{\partial \hat p_k}$$

For the two-edge AND case, $J_1 = \hat p_2$, $J_2 = \hat p_1$.

**Verification of SA1.** At truth ($\hat p_k = \theta_k$):

$$\mathbb E[\Delta \hat p_k]\big\rvert_{\hat{\mathbf p} = \boldsymbol\theta} \;=\; \frac{J_k}{n_k + 1} \cdot \mathbb E[y_G - \hat P_\Sigma]\big\rvert_{\hat{\mathbf p} = \boldsymbol\theta}$$

The bracket evaluates as: $\mathbb E[y_G] = \Phi$ by definition of $y_G$ as a Bernoulli outcome with mean $\Phi$; and $\hat P_\Sigma\big\rvert_{\hat{\mathbf p} = \boldsymbol\theta} = \theta_1 \theta_2 = \Phi$. Therefore $\mathbb E[y_G - \hat P_\Sigma]\big\rvert_{\hat{\mathbf p} = \boldsymbol\theta} = 0$, and:

$$\mathbb E[\Delta \hat p_k]\big\rvert_{\hat{\mathbf p} = \boldsymbol\theta} \;=\; 0 \quad \text{for all } k. \qquad \text{(SA1 satisfied)}$$

The contrast with marginal Bayesian is precise: the marginal scheme suffers from a $\Phi$-vs-$\theta_k$ mismatch (the update treats each edge's marginal likelihood rather than the joint), producing the $O(1/n)$ bias derived in Prop B.3(a). The gradient scheme distributes surprise via the Jacobian, which aligns the per-edge update direction with the plan-level gradient — and this gradient is zero at truth by construction.

**Sector parameter (SA2').** With the gradient-based scheme, the per-edge correction is:

$$F_k(\boldsymbol\delta) \;=\; \frac{J_k}{n_k + 1} \cdot (\Phi - \hat P_\Sigma) \;\approx\; \frac{J_k}{n_k + 1} \cdot \mathbf J^T \boldsymbol\delta$$

where the approximation uses the first-order expansion $\hat P_\Sigma - \Phi \approx \mathbf J^T \boldsymbol\delta$ valid near truth. The per-edge sector bound is:

$$\boldsymbol\delta^T \mathbf F(\boldsymbol\delta) \;\approx\; \sum_k \frac{J_k^2}{n_k + 1} \cdot (\mathbf J^T \boldsymbol\delta)^2 / \lVert\boldsymbol\delta\rVert \;\geq\; \frac{\sigma_{\min}(\mathbf J)^2}{\max_k(n_k + 1)} \lVert\boldsymbol\delta\rVert^2$$

giving:

$$\alpha_c^{\text{grad}} \;\geq\; \frac{\sigma_{\min}(\mathbf J)^2}{\max_k(n_k + 1)}$$

**Transfer through B.5c.** Applying the coupled-case Cauchy-Schwarz bound:

$$\alpha_s \;\geq\; \frac{\alpha_c^{\text{grad}}}{\kappa(\mathbf J)^2} \;=\; \frac{\sigma_{\min}(\mathbf J)^2 / \max_k(n_k+1)}{\sigma_{\max}(\mathbf J)^2 / \sigma_{\min}(\mathbf J)^2} \;=\; \frac{\sigma_{\min}(\mathbf J)^4}{\sigma_{\max}(\mathbf J)^2 \cdot \max_k(n_k+1)}$$

The $\sigma_{\min}(\mathbf J)^4 / \sigma_{\max}(\mathbf J)^2$ factor is the full cost of coupled per-edge attribution — a steep penalty compared to the componentwise case. The plan-level route (B.3(b)) avoids this penalty entirely by tracking $\Phi$ as a single quantity with $\alpha_\Sigma = 1/(n_\Phi + 1)$, at the cost of losing per-edge diagnostics.

**Why not proportional-blame or other schemes?** Proportional-blame distributes surprise proportionally to current credences: $\Delta \hat p_k \propto \hat p_k \cdot (y_G - \hat P_\Sigma) / \sum_j \hat p_j$. This violates SA1 because the proportionality factor $\hat p_k / \sum_j \hat p_j$ is not the gradient direction, so the distribution over edges does not align with the plan-level surprise's actual attribution. Only schemes whose per-edge update aligns with the Jacobian direction preserve SA1 for coupled edges; gradient-based is the canonical such scheme.

**Claim.** For coupled edges with unobservable intermediates, gradient-based attribution is the minimal scheme that (a) satisfies SA1, (b) yields a well-defined per-edge sector parameter, (c) admits the Cauchy-Schwarz Jacobian transfer, and (d) permits per-edge diagnostics. Its $\sigma_{\min}^4 / \sigma_{\max}^2$ scaling is inherent to the coupled case, not an artifact of the scheme. $\square$

### B.5c: Implications

Four regimes for the credence-to-value bridge, indexed by correction type and attribution scheme:

| Correction type | Edge coupling | Attribution | SA1 | Transfer | $\alpha_s$ |
|---|---|---|---|---|---|
| Linear | Any | — | Yes | Exact (Jacobian cancels) | $\alpha_c$ |
| Nonlinear, componentwise | Independent edges | Per-edge Bayesian | Yes | Exact ($J_k \geq 0$ preserves bound) | $\alpha_c$ |
| Nonlinear, coupled | Coupled edges | Gradient-based (Jacobian distribution) | Yes | $\kappa(\mathbf{J})^2$ penalty | $\alpha_c^{\text{grad}} / \kappa^2$ |
| Nonlinear, coupled | Coupled edges | Marginal Bayesian | **No** (O(1/n) bias) | — (Jacobian bridge does not apply) | plan-level alternative ( #strategy-dag) |

**Componentwise correction closes the gap for all verified cases.** Props B.1, B.2, and B.4 all use componentwise edge updates with non-negative Jacobian. The operational diagnostic $\delta_{\text{strategic}}$ inherits the sector condition from credence error with no penalty — even for the nonlinear (stochastic) single-step realization. The derivation validates the operational mismatch, not merely a surrogate.

**Inter-edge coupling — not nonlinearity — is the fragility.** The $\kappa^2$ penalty arises only when correcting one edge changes another's correction direction (B.3's unobservable case, correlated observations). Deep or unbalanced DAGs have high $\kappa(\mathbf{J})$ when corrections couple, but the coupling, not the depth or imbalance per se, is what degrades the persistence guarantee.

**Connection to credit assignment.** The Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$ is computable from the DAG's status propagation formulas — it does not require solving the credit-assignment problem. The credit-assignment problem is about *decomposing observed value changes into per-edge contributions* (needed for the update rule). The Jacobian bridge is about *transferring a per-edge sector condition to the value-residual space* (needed for the persistence guarantee). These are different problems: the bridge works even when credit assignment is unsolved, because it only requires the sensitivity structure, not the causal attribution.


## What Is Derived vs. What Is Chosen

The segment carries derivations at three distinct strengths: (i) exact sector-parameter algebra for concrete Beta-Bernoulli topologies (B.1, B.2, B.4, B.6, B.7 under observable $C$ + facilitator monotonicity), (ii) two structural refutations that are *themselves* derivations of impossibility (B.3(a) SA1 bias; B.7 Cramér-Rao floor under unobservable $C$), and (iii) formulation choices (Beta-Bernoulli dynamics, componentwise conditional-branch updates, the particular $\varepsilon$-greedy policy family). The dividing line runs between the Beta-Bernoulli *model* (chosen) and the sector-parameter *algebra conditional on that model* (proved). B.7's positive transfer requires two load-bearing conditions — observability of $C$ *and* facilitator monotonicity $P_\Sigma(G\mid C) \geq P_\Sigma(G\mid \neg C)$ — either of which failing disqualifies the transfer.

| Property | Source | Strength |
|---|---|---|
| Beta-Bernoulli edge dynamics ($\Delta\hat p_k = (y_k - \hat p_k)/(n_k+1)$) | Conjugate-prior model; matches #edge-update-via-gain | Formulation choice |
| Regime-A adjustment: $\alpha_\Sigma^{\text{eff}} = \iota_{ij} \cdot \alpha_\Sigma^{\text{stated}}$ | Diagonal commutation across Props B.1–B.4, B.6; #edge-update-causal-validity | Derived |
| **B.1** Single-edge sector parameter $\alpha_\Sigma = 1/(n+1)$ | Expected Beta-Bernoulli update + sector product algebra | Proved (tight, conditional on Beta-Bernoulli) |
| **B.1** Stochastic ultimate bound $\lvert\delta\rvert \gt \sqrt{\theta(1-\theta)/(2n+1)}$ | Second-moment recursion + expected-Lyapunov decrement | Derived |
| **B.2** Observable AND-chain sector parameter $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ | Diagonal correction function; sector product algebra | Proved (conditional on Beta-Bernoulli + observable intermediate) |
| **B.2** Depth-$d$ generalization $\alpha_\Sigma = \min_k \prod_{j \lt k}\theta_j/(n_k+1)$ | Iteration of B.2 pattern under observable intermediates | Derived |
| **B.3(a)** Per-edge SA1 violation under marginal Bayesian attribution ($O(1/n)$ bias) | Exact marginal update + evaluation at truth | Derived as refutation (no valid $\alpha_c$ exists) |
| **B.3(b)** Plan-level recovery $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi+1)$ | Reduction of aggregate $\hat\Phi$ tracking to B.1 | Derived (reduction) |
| **B.3** Non-identifiability of $(\theta_1,\theta_2)$ from $y_G$ alone | Product $\Phi = \theta_1\theta_2$ symmetry in observation channel | Proved |
| **B.4(a)** Pure-greedy OR ($\varepsilon=0$) violates sector condition | Counterexample at $\delta_1 = 0,\,\delta_2 \neq 0$ | Derived as refutation |
| **B.4(b)** $\varepsilon$-greedy sector parameter $\min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ | Policy-weighted correction; sector product algebra | Proved (conditional on Beta-Bernoulli + $\varepsilon$-greedy) |
| **B.4** Optimal exploration $\varepsilon^\ast = (n_1+1)/(n_1+n_2+2)$ | Term-equalization in $\min$ | Derived |
| **B.4** Minimum exploration rate (SA3 requirement) $\varepsilon \gt \rho_\Sigma(n_{\max}+1)/R_\Sigma$ | Substitution into persistence threshold $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ | Derived |
| **B.5a** Linear credence-to-value transfer $\alpha_s = \alpha_c$ (Jacobian cancels) | Algebraic cancellation of $\mathbf{J}\mathbf{J}^T$ | Proved (exact, DAG-structure independent) |
| **B.5b** Componentwise nonlinear transfer $\alpha_s = \alpha_c$ | Per-component sector bound + monotone AND/OR ($\mathbf{J}\geq 0$) | Proved (conditional on componentwise update + non-negative Jacobian) |
| **B.5b** Coupled-edge Cauchy-Schwarz bound $\alpha_s \geq \alpha_c/\kappa(\mathbf{J})^2$ | Cauchy-Schwarz on $\mathbf{J}^T\mathbf F_c$ and $\mathbf{J}^T\boldsymbol\delta_c$ | Derived (conditional on Jacobian regularity *and* an SA1-preserving attribution scheme) |
| **B.5c** Four-regime classification of credence-to-value transfer | Combination of linear/nonlinear × componentwise/coupled × attribution type | Derived |
| **B.5d** Gradient-based attribution restores SA1 on coupled edges | Jacobian-weighted surprise distribution; $\mathbb{E}[y_G - \hat P_\Sigma]\rvert_{\boldsymbol\theta} = 0$ | Derived |
| **B.5d** Sector parameter under gradient attribution $\alpha_c^{\text{grad}} \geq \sigma_{\min}(\mathbf{J})^2/\max_k(n_k+1)$ | First-order expansion near truth + singular-value analysis | Derived |
| **B.5d** Gradient-based as *minimal* SA1-preserving scheme for coupled edges | Argument excluding proportional-blame and other schemes | Derived qualitatively (not a uniqueness theorem) |
| **B.6** L1 augmented-DAG sector parameter (three-way gating: condition / starvation / exploration) | Diagonal correction function over $(\delta_C, \delta_{A_1}, \delta_{A_2})$; sector product | Proved (conditional on Beta-Bernoulli + observable $C$ + $\varepsilon$-greedy) |
| **B.6** L0-vs-L1 comparison: L1 is lower $\alpha_\Sigma$ but honestly calibrated | Direct $\Phi^{L0}$ vs $\Phi^{L1}$ computation at truth | Derived |
| **B.6** L1-construction principle (common cause factored *above* OR-structure) | Requirement for conditional independence of OR-siblings given $C$ | Derived |
| **B.7** L1' mixture-form sector parameter (five-way gating) | Diagonal correction function over $(\xi_C, \{\xi_{j\mid C}\}, \{\xi_{j\mid \neg C}\})$; sector product | Derived (conditional on Beta-Bernoulli + observable $C$ + componentwise conditional-branch update + *facilitator monotonicity* $P_\Sigma(G\mid C)\geq P_\Sigma(G\mid \neg C)$) |
| **B.7** Componentwise update per conditional branch | Matches Beta-Bernoulli on the branch actually executed each trial | Formulation choice |
| **B.7** Facilitator-monotonicity condition $P_\Sigma(G\mid C) \geq P_\Sigma(G\mid \neg C)$ | Required so the first Jacobian entry of $\hat P_\Sigma^{L1'}$ is non-negative, enabling the lossless B.5b transfer | Load-bearing scope condition |
| **B.7** Reduction to B.6 under strict-prerequisite limit ($\theta_{j\mid\neg C}\to 0$) | Collapse of $\neg C$-branch terms in the sector inequality | Verification (algebraic consistency) |
| **B.7** Refutation under unobservable $C$ (single-channel Fisher rank 1) | Cramér-Rao bound applied to rank-1 Fisher $\mathcal{F}(\phi) = uu^T/[\mu_j(1-\mu_j)]$ | Proved by external theorem (Cramér-Rao bound) — no unbiased online estimator admits $\alpha \gt 0$ |
| **B.7** Repair route (i): augment $C$-observability | Recovers the positive B.7 derivation | Formulation / scope choice (maps to #loop-interventional-access) |
| **B.7** Repair route (ii): $K\geq 2$ joint children under same $C$-realization | Fisher matrix rank reaches $2K+1$; local sector condition | Derived (sketch; applicability narrow) |
| **B.7** Repair route (iii): plan-level fallback on marginal $\hat\mu_j$ | Reduction to B.1 on scalar marginal | Derived (at cost of per-conditional decomposition) |
| Persistence thresholds (substitution of each $\alpha_\Sigma$ into $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$) | Proposition A.1 of #sector-condition-derivation | Derived (each) |
| Gain-collapse threshold $n^\ast \propto R_\Sigma/\rho_\Sigma$ common across cases | Direct inversion of persistence condition | Derived |
| Expected-value (rather than almost-sure) sector analysis | Pedagogical simplification; a.s. convergence via standard Bayesian consistency | Formulation choice (scope) |
| Constant-$\alpha$ assumption with experience-discounting ($\lambda$) stabilization | Instantaneous persistence check + forgetting-factor analysis | Derived (instantaneous only) |


## Epistemic Status

*Conditional on the Beta-Bernoulli model.* Propositions B.1, B.2, B.4, and B.6 are *derived*: the sector-condition verification is exact algebra under the stated generative model. The persistence conditions follow by direct application of Proposition A.1 ( #sector-condition-derivation), which is independently established. Proposition B.3(a) (the SA1 violation) is also derived; B.3(b) reduces to B.1 by construction. Proposition B.5a (the credence-to-value bridge for linear correction) is *exact* — the Jacobian cancellation is algebraic, independent of DAG structure. Proposition B.5b (the componentwise nonlinear transfer) is *exact under non-negative Jacobian* — algebraic, no condition-number penalty. The coupled-edge case of B.5b is *conditional on (i) Jacobian regularity* — the condition-number bound requires $\sigma_{\min}(\mathbf{J}) \gt 0$, which holds for non-degenerate DAGs — *and (ii) an SA1-preserving attribution scheme* (gradient-based, Prop B.5d); marginal Bayesian attribution on coupled edges does not admit the Cauchy-Schwarz bound because SA1 fails upstream. Proposition B.5d (gradient-based attribution) is *derived* — SA1 verification is algebraic and the sector-parameter bound follows from standard singular-value analysis of the Jacobian.

All results use the *expected-value* sector condition. A full stochastic treatment (Foster-Lyapunov or supermartingale convergence) would give probability bounds rather than expected-value bounds. The expected-value analysis gives the correct asymptotic behavior (posterior concentration at $O(1/\sqrt{n})$) but does not prove almost-sure convergence. For the stationary Beta-Bernoulli case, almost-sure convergence is guaranteed by the standard Bayesian consistency theorem independently of this derivation.

The time-varying $\alpha_\Sigma$ issue remains: since $n_k$ increases with each observation, $\alpha_\Sigma$ decreases over time. The sector-condition framework assumes constant $\alpha$. The results here give an *instantaneous* persistence check at the current experience level, not a trajectory guarantee. Experience discounting (exponential forgetting with factor $\lambda$) stabilizes $\alpha_\Sigma$ at approximately $1 - \lambda$, yielding the persistence requirement $\lambda \lt 1 - \rho_\Sigma/R_\Sigma$.

**What remains open:**

1. ~~*General DAG topology.*~~ **Partially resolved.** Proposition B.6 verifies the first mixed AND/OR case (L1 augmented DAG with common-cause node). The three-way gating structure (condition testing × evidence starvation × exploration gating) appears to be the general pattern. Remaining: arbitrary mixed AND/OR DAGs with multiple common causes and deeper nesting.
2. *Continuous outcomes.* The Beta-Bernoulli model gives conjugate, closed-form updates. Non-conjugate cases (continuous signals, partial observability) require approximate inference, and the sector condition must be verified for the approximation.
3. ~~*Modified sector condition for biased correction.*~~ **Resolved via Prop B.5d (gradient-based attribution).** The $O(1/n)$ bias in the unobservable case (B.3a) under marginal Bayesian updates is eliminated by switching to gradient-based attribution, which satisfies SA1 exactly at truth. Per-edge results are recovered under the gradient scheme at the $\sigma_{\min}^4 / \sigma_{\max}^2$ scaling. Alternative route (plan-level tracking, B.3(b)) remains available without the condition-number penalty.
4. ~~*Correlated edges (L1/L2 scope).*~~ **Resolved.** Proposition B.6 verifies the sector condition for L1 (strict-prerequisite augmented DAG); Proposition B.7 verifies it for L1' (soft-facilitator mixture form, observable common cause) with five-way gating. The unobservable-$C$ single-channel case is *refuted* by the Cramér-Rao floor (mixture identifiability obstruction; see B.7 §"Refuted Under Unobservable $C$") — not merely "open" but structurally impossible without additional information augmentation. Practical paths under unobservable $C$: augment $C$-observability, run multi-child joint observations (sketch only, narrow applicability), or fall back to plan-level tracking on the marginal. Strategies requiring full L2 conditioning over $k$ unobservable common causes still cost $O(2^k)$.
5. *Adaptive exploration.* Proposition B.4 uses fixed $\varepsilon$. Adaptive strategies (UCB, Thompson sampling) allocate exploration based on current uncertainty and should yield tighter sector bounds.


## Discussion

**The sector parameter is the edge update gain.** Across all four cases, $\alpha_\Sigma$ is a function of $\eta_k = 1/(n_k+1)$ --- the same quantity that governs epistemic persistence ( #adaptive-tempo, #update-gain). Strategic persistence and epistemic persistence are governed by the same mathematical machinery, not merely structurally parallel. This validates the schema proposed in #strategy-persistence-schema at the level of concrete dynamics.

**AND vs. OR: structural vs. behavioral fragility.** The evidence-starvation effect (B.2) is structural --- it depends on the DAG topology and upstream reliability, not on the agent's policy. The exploration-gating effect (B.4) is behavioral --- it depends on the action-selection policy. AND-node persistence is improved by increasing upstream reliability (making early steps more likely to succeed). OR-node persistence is improved by increasing exploration (testing alternatives more frequently). The distinction maps to the familiar depth-vs-breadth tradeoff in planning.

**Gain collapse as the dominant failure mode.** In every drifting-environment case, the persistence threshold takes the form $n \lt c/\rho_\Sigma$ for some constant $c$. Accumulated experience suppresses the update gain, eventually making the agent unable to track environmental change. This gives the gain-collapse phenomenon ( #update-gain) a precise quantitative threshold for each topology.

**The credence-to-value bridge decouples persistence from credit assignment.** Proposition B.5 shows that strategic persistence (in value-residual space) can be established from per-edge sector conditions (in credence space) without solving the credit-assignment problem. The bridge requires only the value-sensitivity Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$, which is computable from the DAG's status propagation formulas in $O(\lvert V\rvert + \lvert E\rvert)$ time. Credit assignment — attributing observed value changes to specific edges — is needed for the *update rule* (computing the signal function in #edge-update-via-gain), not for the *persistence guarantee*. This means the persistence analysis can proceed even while the update rule remains incompletely specified.

**Inter-edge coupling is the true fragility, not nonlinearity or DAG depth.** Proposition B.5b shows that nonlinear componentwise corrections transfer losslessly through any non-negative Jacobian — the $\kappa(\mathbf{J})^2$ penalty arises only when corrections are *coupled* across edges. This refines the earlier qualitative argument from #chain-confidence-decay: the structural pressure toward shallow, balanced strategies is not about depth per se but about the coupling that deep or complex structures tend to introduce. A deep AND-chain with fully observable intermediates (B.2) has componentwise corrections and transfers losslessly despite high depth. The same chain with unobservable intermediates (B.3) has coupled corrections and incurs the penalty. The distinction is observability-mediated coupling, not topological complexity.
