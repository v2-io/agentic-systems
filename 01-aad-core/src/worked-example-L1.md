---
slug: worked-example-L1
type: worked-example
status: conditional
depends:
  - strategy-dag
  - strategic-dynamics-derivation
  - graph-structure-uniqueness
stage: draft
---

# Worked Example: L1 Augmented DAG with Common-Cause Node

A concrete instantiation of the Correlation Hierarchy ( #strategy-dag) and Proposition B.6 ( #strategic-dynamics-derivation). Two OR-alternatives sharing an infrastructure dependency are modeled at L0 (independence) and L1 (augmented DAG), with the sector condition verified for L1.

## Setup

Two alternative paths to a goal $G$, sharing a common infrastructure dependency $C$:

- Infrastructure up with probability $\theta_C = 0.8$
- Path 1 succeeds with probability $\theta_{1|C} = 0.9$ when infrastructure is up, fails when down
- Path 2 succeeds with probability $\theta_{2|C} = 0.7$ when infrastructure is up, fails when down
- Goal succeeds if at least one path succeeds (OR)

**Actual plan success probability** (from the generative model):

$$P(G) = \theta_C \cdot [1 - (1-\theta_{1|C})(1-\theta_{2|C})] = 0.8 \cdot 0.97 = 0.776$$


## L0 Analysis: The Independence Model

The L0 DAG has two leaf nodes with marginal success probabilities:

$$\theta_1 = \theta_C \cdot \theta_{1|C} = 0.72, \qquad \theta_2 = \theta_C \cdot \theta_{2|C} = 0.56$$

OR-propagation:

$$\hat P_\Sigma^{L0} = 1 - (1-\theta_1)(1-\theta_2) = 1 - (0.28)(0.44) = 0.877$$

**Overestimation**: $0.877 - 0.776 = 0.101$ (13% relative error).

The overestimation equals $\text{Cov}(X_1, X_2)$ — the covariance induced by the shared infrastructure. The OR-node's redundancy is illusory: both paths fail together when infrastructure fails, so the "backup" provides less protection than the independence model predicts. This is the $-\rho$ bias from the Correlation Hierarchy's direction-of-bias formula.


## Naive L1: Why Adding a Node Is Not Sufficient

The obvious L1 construction adds $C$ as a parent of both paths:

- $B_1 = \text{AND}(C, A_1)$, $B_2 = \text{AND}(C, A_2)$
- $G = \text{OR}(B_1, B_2)$

Status propagation: $s_{B_1} = 0.8 \cdot 0.9 = 0.72$, $s_{B_2} = 0.8 \cdot 0.7 = 0.56$, $s_G = 1 - (0.28)(0.44) = 0.877$.

**Same answer as L0.** The OR-propagation treats $B_1$ and $B_2$ as marginally independent, but they are correlated through their shared parent $C$. Adding the common-cause node does not fix the overestimation because the node is *inside* the correlated structure (below the OR-node), not factored above it.


## Correct L1: Factor the Common Cause Above the Correlation

The correct L1 restructuring places $C$ as an AND-prerequisite *above* the OR-structure:

- $G_{\text{sub}} = \text{OR}(A_1, A_2)$ — the sub-plan assuming infrastructure holds
- $G = \text{AND}(C, G_{\text{sub}})$ — infrastructure must hold AND sub-plan must work

Status propagation:

$$s_{G_{\text{sub}}} = 1 - (1-\theta_{1|C})(1-\theta_{2|C}) = 1 - (0.1)(0.3) = 0.97$$

$$s_G = \theta_C \cdot s_{G_{\text{sub}}} = 0.8 \cdot 0.97 = 0.776$$

**Correct.** Matches the actual plan success probability exactly.

**Why this works**: $C$ is above the OR-node, so its value is factored out before the OR-propagation occurs. Conditional on $C=1$, the two paths $A_1$ and $A_2$ are genuinely independent (their exogenous noise terms are independent — the common cause has been conditioned away). The OR-propagation's independence assumption holds within $G_{\text{sub}}$ because the correlation source is above, not among the siblings.

**The L1 construction principle**: *factor the common cause above the correlation it creates.* When a common cause correlates siblings under an OR-node, restructure so the common cause gates the entire OR-structure via an AND-relationship. This ensures conditional independence of the OR-children and makes standard propagation correct.


## Sector Condition Verification (Proposition B.6)

Three leaf nodes with Beta-Bernoulli dynamics and $\varepsilon$-greedy path selection:

| Leaf | True value | Tested when | Expected correction |
|---|---|---|---|
| $C$ (condition) | $\theta_C = 0.8$ | Every trial | $-\delta_C/(n_C+1)$ |
| $A_1$ (greedy) | $\theta_{1\mid C} = 0.9$ | $C=1$ AND path 1 selected | $-\theta_C(1-\varepsilon)\,\delta_{A_1}/(n_{A_1}+1)$ |
| $A_2$ (explore) | $\theta_{2\mid C} = 0.7$ | $C=1$ AND path 2 selected | $-\theta_C\varepsilon\,\delta_{A_2}/(n_{A_2}+1)$ |

The sector parameter (full proof in Prop B.6 of #strategic-dynamics-derivation):

$$\alpha_\Sigma = \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C(1-\varepsilon)}{n_{A_1}+1},\; \frac{\theta_C \varepsilon}{n_{A_2}+1}\right)$$

**Three-way gating.** This is the first verified mixed AND/OR topology, combining:

1. **Condition testing** — $C$ is tested every trial, same rate as a single edge (B.1)
2. **Evidence starvation** — action edges are gated by $\theta_C$ (tested only when $C=1$), same mechanism as B.2
3. **Exploration gating** — OR-alternatives compete for test opportunities ($\varepsilon$ vs $1-\varepsilon$), same mechanism as B.4

The B.5b bridge applies (non-negative Jacobian, componentwise corrections): $\alpha_s = \alpha_\Sigma$ with no penalty.


## L0 vs L1 Comparison

| Quantity | L0 | L1 (correct) |
|---|---|---|
| **Leaf edges** | 2 ($A_1, A_2$ at marginals) | 3 ($C, A_1\mid C, A_2\mid C$) |
| **$\Phi$ at truth** | $0.877$ (biased) | $0.776$ (correct) |
| **$\Phi$ – actual success** | $+0.101$ (overestimates) | $0$ (unbiased) |
| **Bottleneck $\alpha_\Sigma$ (at $\varepsilon = 0.3$)** | $0.3/(n_2+1)$ | $0.24/(n_{A_2}+1)$ |
| **Persistence threshold** | Lower (easier) | Higher (harder) |

**The tradeoff**: L0 has a higher sector parameter (easier to maintain persistence) but its reference value $\Phi^{L0}$ is systematically wrong — it overestimates actual success by the covariance $\rho$. L1 has a lower sector parameter (the $\theta_C$ attenuation makes action calibration harder) but its reference value $\Phi^{L1}$ is correct.

Both models have $\delta_s = 0$ when credences are at truth. The difference is what $\delta_s = 0$ *means*:

- **L0**: well-calibrated within the independence model — which overstates plan success by $\rho$
- **L1**: well-calibrated to actual plan success

**L1 persistence is harder but calibration is honest.** The extra leaf ($C$) adds a degree of freedom, and the condition-gating slows action calibration. But the resulting target ($\Phi^{L1}$) is the true plan success probability, not a biased surrogate.


## When Correct L1 Construction Is Not Possible

The factoring-above principle works when the common cause cleanly gates all correlated children through a single AND-relationship. When this is not structurally possible — for example, when some OR-alternatives share a common cause and others do not — a **conditioning-based propagation** is needed:

$$P(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$$

where $P_\Sigma(G \mid C = c)$ is computed by standard AND/OR propagation with $C$ fixed. Cost: $O(2^k \cdot (\lvert V\rvert + \lvert E\rvert))$ where $k$ is the number of common-cause nodes. Tractable for small $k$; exponential in general.

For strategies with many correlated common causes, this approaches L2 complexity, and the agent faces a practical choice: model the most important common causes at L1 (accepting residual L0 bias from unmodeled causes) or invest in richer propagation algorithms.


## Detecting Latent Common Causes

The detection of causal insufficiency and interventional localization of latent common causes is treated as a standalone result in #causal-insufficiency-detection. The key connection to this worked example: the L0 residual $\Phi^{L0} - \bar{y}_G$ converges to $+\rho$ (our example: $0.877 - 0.776 = 0.101$), providing a precise, quantitative detection signal. The agent does not need to know the common cause exists *a priori* — it discovers the need for L1 from persistent structured residuals after convergence.


## Epistemic Status

*Conditional on Beta-Bernoulli model.* The L0 overestimation, L1 correction, and sector condition verification are exact algebra. The direction-of-bias formula ($\pm\rho$) is exact for two binary siblings; for deeper DAGs with multiple common causes, the bias involves higher-order covariance terms. The L1 construction principle (factor common cause above the correlation) is general for single common causes gating OR-siblings; the conditioning-based extension for more complex topologies is standard (variable elimination in Bayesian networks).
