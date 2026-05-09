# Spike: L1 Worked Example — Sector Condition for Augmented DAG

**Status**: Spike — verifying the Correlation Hierarchy's L1 claim with a concrete example.

**Date**: 2026-04-06

**Motivation**: The Correlation Hierarchy in #def-strategy-dag claims that L1 (augmented DAGs with common-cause nodes) gets all L0 formal results for free because "the augmented DAG is a standard AND/OR DAG that satisfies causal sufficiency." This spike instantiates the claim with the simplest interesting case and discovers an important structural requirement for correct L1 construction.

---

## The Scenario

Two alternative paths to a goal $G$, sharing a common infrastructure dependency $C$:

- Path 1 ($A_1$): succeeds with probability $\theta_{1|C}$ when infrastructure is up ($C=1$), fails when $C=0$
- Path 2 ($A_2$): succeeds with probability $\theta_{2|C}$ when infrastructure is up ($C=1$), fails when $C=0$
- Infrastructure up with probability $\theta_C$

The goal $G$ succeeds if at least one path succeeds (OR).

**Concrete numbers**: $\theta_C = 0.8$, $\theta_{1|C} = 0.9$, $\theta_{2|C} = 0.7$.

**Actual plan success probability** (from the generative model):

$$P(G) = \theta_C \cdot [1 - (1-\theta_{1|C})(1-\theta_{2|C})] = 0.8 \cdot [1 - (0.1)(0.3)] = 0.8 \cdot 0.97 = 0.776$$


---

## L0 Analysis: Overestimation Demonstrated

The L0 DAG has no common-cause node:

```
A₁ →(p₁) G [OR]
A₂ →(p₂) G [OR]
```

The agent learns the *marginal* success probabilities:
- $\theta_1 = \theta_C \cdot \theta_{1|C} = 0.8 \cdot 0.9 = 0.72$
- $\theta_2 = \theta_C \cdot \theta_{2|C} = 0.8 \cdot 0.7 = 0.56$

L0 propagation:

$$\hat P_\Sigma^{L0} = 1 - (1-\theta_1)(1-\theta_2) = 1 - (0.28)(0.44) = 0.877$$

**Overestimation**: $0.877 - 0.776 = 0.101$ (13% relative error).

The overestimation arises because L0 treats the two paths as independent. In reality, when infrastructure fails ($C=0$), *both* paths fail simultaneously. The OR-node's redundancy is illusory — the "backup" path fails for the same reason as the primary.

**Direction of bias for different node types.** Under positive correlation of outcomes (which is what common-cause dependencies create):

| Node type | L0 direction | Intuition |
|---|---|---|
| **OR** (at least one succeeds) | Overestimates | Redundancy is illusory — failures cluster |
| **AND** (all must succeed) | Underestimates | Successes cluster — joint success is more likely than product of marginals |
| **Mixed** | Depends on structure | Typically overestimates for top-OR strategies (OR dominates at the root) |

The OR-overestimation is the dangerous case — the agent believes it has more redundancy than it actually does.


---

## Naive L1: Adding C as Sibling Parent (Still Overestimates!)

The obvious L1 construction: add $C$ as a parent of intermediate AND-nodes:

```
         C (θ_C = 0.8)
        / \
       v   v
      B₁   B₂   [both AND-nodes]
      ^     ^
      |     |
     A₁    A₂
    (0.9) (0.7)
      \   /
       v v
        G      [OR-node]
```

Status propagation:
- $s_{B_1} = p_C \cdot p_{A_1} = 0.8 \cdot 0.9 = 0.72$
- $s_{B_2} = p_C \cdot p_{A_2} = 0.8 \cdot 0.7 = 0.56$
- $s_G = 1 - (1 - s_{B_1})(1 - s_{B_2}) = 1 - (0.28)(0.44) = 0.877$

**Same answer as L0!** The overestimation persists. Why?

The AND/OR propagation at the OR-node treats $B_1$ and $B_2$ as independent. But they share parent $C$ — when $C=0$, both $B_1$ and $B_2$ are zero. The OR-node's independence assumption is violated *within the augmented DAG* because the common cause is *below* the OR-node, not above it.

Formally: the Markov factorization holds for the augmented DAG ($B_1 \perp B_2 \mid C, A_1, A_2$), but the OR-propagation formula computes $P(G) = 1 - (1-P(B_1))(1-P(B_2))$, which uses *marginal* probabilities of $B_1$ and $B_2$, not conditional. The marginals carry the correlation through $C$.

**The diagnosis**: the common-cause node is in the wrong position. It's inside the correlated structure (below the OR-node), not factored above it.


---

## Correct L1: Factor the Common Cause Above the Correlation

The correct L1 restructuring separates the common cause from the independent components:

```
     C (θ_C = 0.8)       A₁ (θ₁|C = 0.9)    A₂ (θ₂|C = 0.7)
       \                      |                      |
        v                     v                      v
         G  ←[AND]←  G_sub  ←[OR]←  A₁ , A₂
```

More precisely:
- $G_{\text{sub}}$ is an OR-node with inputs $A_1$ and $A_2$ (the action leaves)
- $G$ is an AND-node with inputs $C$ and $G_{\text{sub}}$: the plan succeeds iff infrastructure is up AND at least one path works

Status propagation:
- $s_{G_{\text{sub}}} = 1 - (1 - p_{A_1})(1 - p_{A_2}) = 1 - (0.1)(0.3) = 0.97$
- $s_G = p_C \cdot s_{G_{\text{sub}}} = 0.8 \cdot 0.97 = 0.776$

**Correct!** Matches the actual plan success probability exactly.

**Why this works**: By placing $C$ above the OR-node, we factor the joint probability correctly:

$$P(G) = P(C=1) \cdot P(G_{\text{sub}} \mid C=1)$$

Within $G_{\text{sub}}$, the action nodes $A_1$ and $A_2$ are *conditionally independent given $C=1$* — the common cause has been conditioned out. The OR-propagation's independence assumption is satisfied within the factored structure.

**The L1 construction principle**: *Factor the common cause above the correlation it creates.* Put the common-cause node as an AND-prerequisite above the OR/AND structure that combines its dependent children, not inside it. This ensures that, conditional on the common cause, the children are independent and standard AND/OR propagation is correct.


---

## Sector Condition Verification for the Correct L1 DAG

### Setup

Three leaf nodes with Beta-Bernoulli edge credences:

| Leaf | Type | Credence | True value | Tested when |
|---|---|---|---|---|
| $C$ | Condition | $\hat p_C$ | $\theta_C$ | Every trial where observable |
| $A_1$ | Action | $\hat p_{A_1}$ | $\theta_{1\mid C}$ | $C=1$ AND agent selects path 1 |
| $A_2$ | Action | $\hat p_{A_2}$ | $\theta_{2\mid C}$ | $C=1$ AND agent selects path 2 |

Mismatch vector: $\boldsymbol\delta = (\delta_C, \delta_{A_1}, \delta_{A_2})^T$ where $\delta_C = \hat p_C - \theta_C$, $\delta_{A_k} = \hat p_{A_k} - \theta_{k|C}$.

Plan-confidence score: $\hat P_\Sigma = \hat p_C \cdot [1 - (1 - \hat p_{A_1})(1 - \hat p_{A_2})]$.

Independence-model reference value: $\Phi = \theta_C \cdot [1 - (1-\theta_{1|C})(1-\theta_{2|C})]$.

Plan-confidence error: $\delta_s = \hat P_\Sigma - \Phi$.

### Proposition L1.1: Sector Condition for the Augmented DAG

**Statement.** Under Beta-Bernoulli updating with $\varepsilon$-greedy path selection and condition node $C$ observable every trial, the expected correction function satisfies the sector condition globally with:

*[Derived (Conditional on Beta-Bernoulli model, L1 augmented DAG)]*

$$\alpha_\Sigma = \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C(1-\varepsilon)}{n_{A_1}+1},\; \frac{\theta_C \varepsilon}{n_{A_2}+1}\right)$$

where $A_1$ is the greedy path.

**Proof.**

*Edge $C$ (condition leaf).* Observed every trial (or at least whenever the agent can observe infrastructure status). Standard Beta-Bernoulli:

$$\mathbb{E}[\Delta \hat p_C] = \frac{\theta_C - \hat p_C}{n_C + 1} = -\frac{\delta_C}{n_C + 1}$$

Correction: $F_C(\delta_C) = \delta_C / (n_C + 1)$.

*Edge $A_1$ (action leaf, greedy path).* Tested only when $C = 1$ (probability $\theta_C$) AND the agent selects path 1 (probability $1 - \varepsilon$):

$$\mathbb{E}[\Delta \hat p_{A_1}] = \theta_C(1-\varepsilon) \cdot \frac{\theta_{1|C} - \hat p_{A_1}}{n_{A_1} + 1} = -\frac{\theta_C(1-\varepsilon)\,\delta_{A_1}}{n_{A_1} + 1}$$

Correction: $F_{A_1}(\delta_{A_1}) = \theta_C(1-\varepsilon)\,\delta_{A_1} / (n_{A_1} + 1)$.

*Edge $A_2$ (action leaf, explore path).* Tested only when $C = 1$ AND the agent selects path 2 (probability $\varepsilon$):

$$\mathbb{E}[\Delta \hat p_{A_2}] = -\frac{\theta_C \varepsilon\,\delta_{A_2}}{n_{A_2} + 1}$$

Correction: $F_{A_2}(\delta_{A_2}) = \theta_C \varepsilon\,\delta_{A_2} / (n_{A_2} + 1)$.

*Sector product:*

$$\boldsymbol\delta^T \mathbf{F}(\boldsymbol\delta) = \frac{\delta_C^2}{n_C+1} + \frac{\theta_C(1-\varepsilon)\,\delta_{A_1}^2}{n_{A_1}+1} + \frac{\theta_C \varepsilon\,\delta_{A_2}^2}{n_{A_2}+1}$$

$$\geq \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C(1-\varepsilon)}{n_{A_1}+1},\; \frac{\theta_C \varepsilon}{n_{A_2}+1}\right) \lVert\boldsymbol\delta\rVert^2$$

*SA1 check:* $\mathbf{F}(\mathbf{0}) = \mathbf{0}$. ✓

*SA3 check (exploration):* For $\alpha_\Sigma > 0$, we need $\varepsilon > 0$. Pure greedy ($\varepsilon = 0$) fails the sector condition because the unchosen path's mismatch grows without correction. Same as B.4. ✓ $\square$

### Three-Way Gating Structure

The sector parameter reveals a **three-way gating** structure, combining effects from B.2 (evidence starvation) and B.4 (exploration gating) in a single example:

1. **Condition leaf $C$**: Correction rate $1/(n_C+1)$ — same as a single edge (B.1). The common cause is the *easiest* component to calibrate because it's tested every trial.

2. **Greedy action $A_1$**: Correction rate $\theta_C(1-\varepsilon)/(n_{A_1}+1)$ — gated by BOTH $\theta_C$ (evidence starvation: infrastructure must be up for the action to be testable) AND $(1-\varepsilon)$ (selection probability). The $\theta_C$ factor is exactly the evidence-starvation effect from B.2; the $(1-\varepsilon)$ factor is the exploration-gating effect from B.4.

3. **Explore action $A_2$**: Correction rate $\theta_C \varepsilon/(n_{A_2}+1)$ — doubly gated with the weakest factors. This is the bottleneck: a rarely-explored alternative behind a sometimes-failing prerequisite.

**Weakest-link formula:**

$$\alpha_\Sigma = \min(\underbrace{\alpha_C}_{\text{condition}},\; \underbrace{\theta_C \cdot \alpha_{A_1,\text{select}}}_{\text{starvation} \times \text{greedy}},\; \underbrace{\theta_C \cdot \alpha_{A_2,\text{select}}}_{\text{starvation} \times \text{explore}})$$

The bottleneck is typically the third term: $\theta_C \varepsilon / (n_{A_2}+1)$.

### B.5 Bridge: Credence-to-Value Transfer

The Jacobian of $\hat P_\Sigma$ with respect to the credence vector:

$$\mathbf{J} = \nabla_{\mathbf{p}} \hat P_\Sigma = \begin{pmatrix} s_{G_{\text{sub}}} \\ p_C(1 - p_{A_2}) \\ p_C(1 - p_{A_1}) \end{pmatrix}$$

All components are non-negative (monotone AND/OR). Corrections are componentwise (each leaf updates from its own observation independently). By Proposition B.5b from #deriv-edge-credence-dynamics, the sector condition transfers losslessly:

$$\alpha_s = \alpha_c = \alpha_\Sigma$$

No condition-number penalty. The plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ inherits the sector condition from the per-leaf credence errors.

### Persistence Condition

$$\alpha_\Sigma > \frac{\rho_\Sigma}{R_\Sigma} \quad\iff\quad \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C(1-\varepsilon)}{n_{A_1}+1},\; \frac{\theta_C \varepsilon}{n_{A_2}+1}\right) > \frac{\rho_\Sigma}{R_\Sigma}$$

With optimal exploration rate $\varepsilon^\ast = (n_{A_1}+1)/(n_{A_1}+n_{A_2}+2)$ (equalizing the two action terms):

$$\alpha_\Sigma^\ast = \min\!\left(\frac{1}{n_C+1},\; \frac{\theta_C}{n_{A_1}+n_{A_2}+2}\right)$$

The critical experience levels:
- Condition: $n_C < R_\Sigma/\rho_\Sigma - 1$ (same as B.1)
- Actions: $n_{A_1} + n_{A_2} < \theta_C R_\Sigma/\rho_\Sigma - 2$ (tightened by $\theta_C$)

When $\theta_C$ is low (infrastructure unreliable), the action calibration threshold is much stricter — the agent has less opportunity to test its action beliefs, so it must maintain a higher effective gain.


---

## L0 vs L1: Accuracy-Calibratability Tradeoff

| Quantity | L0 | L1 (correct) |
|---|---|---|
| **Leaves** | $A_1, A_2$ (marginals) | $C, A_1\mid C, A_2\mid C$ (conditionals) |
| **Reference value $\Phi$** | $\theta_1 \theta_2 = 0.30$ ← wait... | $\theta_C[1-(1-\theta_{1\mid C})(1-\theta_{2\mid C})] = 0.776$ |
| **Plan confidence $\hat P_\Sigma$** | $1-(1-p_1)(1-p_2) = 0.877$ (at truth) | $p_C[1-(1-p_{A_1})(1-p_{A_2})] = 0.776$ (at truth) |
| **Actual success** | 0.776 | 0.776 |
| **Error at truth** | $0.877 - 0.776 = 0.101$ (13%) | $0.776 - 0.776 = 0$ |
| **Sector parameter** | $\min(\frac{0.7}{n_1+1}, \frac{0.3}{n_2+1})$ | $\min(\frac{1}{n_C+1}, \frac{0.56}{n_{A_1}+1}, \frac{0.24}{n_{A_2}+1})$ |
| **Bottleneck** | Explore path: $0.3/(n_2+1)$ | Explore path behind condition: $0.24/(n_{A_2}+1)$ |

Wait — I need to fix the L0 reference value. For L0 with OR:
$\Phi^{L0} = 1 - (1-\theta_1)(1-\theta_2) = 1 - (0.28)(0.44) = 0.877$. This equals $\hat P_\Sigma$ at truth, so $\delta_s^{L0} = 0$ at truth too. The issue with L0 isn't that $\delta_s$ is wrong — it's that $\Phi^{L0}$ itself doesn't match reality.

Let me redo this table correctly.

| Quantity | L0 | L1 (correct) |
|---|---|---|
| **Leaves** | $A_1, A_2$ (marginals) | $C, A_1\mid C, A_2\mid C$ (conditionals) |
| **$\Phi$ (reference value at truth)** | $0.877$ | $0.776$ |
| **Actual plan success** | $0.776$ | $0.776$ |
| **$\Phi$ – actual** | $+0.101$ (model overshoot) | $0$ (model correct) |
| **$\delta_s$ at truth** | $0$ | $0$ |
| **Bottleneck $\alpha_\Sigma$** | $0.3/(n_2+1)$ | $0.24/(n_{A_2}+1)$ |
| **Persistence easier?** | Yes (higher $\alpha$) | No (lower $\alpha$, more edges) |

**The tradeoff**: L0 has a *higher* sector parameter (easier to maintain persistence) but its reference value $\Phi^{L0} = 0.877$ is wrong — it overstates actual plan success by 13%. L1 has a *lower* sector parameter (the condition-gating makes calibration harder) but its reference value $\Phi^{L1} = 0.776$ matches reality.

Both models have $\delta_s = 0$ when credences are at truth — the sector condition ensures $\delta_s$ stays small for both. The difference is *what $\delta_s = 0$ means*:

- **L0**: $\delta_s = 0$ means "I'm well-calibrated within the independence model" — which overestimates actual success by 13%.
- **L1**: $\delta_s = 0$ means "I'm well-calibrated to actual plan success" — the model is correct.

**L1 persistence is harder but calibration is honest.** The extra leaf ($C$) adds a degree of freedom that must be tracked, and the condition-gating ($\theta_C$ factor) slows action calibration. But the resulting calibration target ($\Phi^{L1}$) is the true plan success probability, not a biased surrogate.


---

## The L1 Construction Principle

The spike reveals an important structural requirement that the current #def-strategy-dag description understates:

### ✗ Naive construction: common cause as sibling parent

Adding $C$ as a parent of $B_1$ and $B_2$, with $B_1, B_2$ as siblings under an OR-node, does NOT fix the overestimation. The AND/OR propagation treats siblings as marginally independent, but they are correlated through their shared parent $C$.

### ✓ Correct construction: factor the common cause above the correlation

Place $C$ as an AND-prerequisite *above* the OR/AND structure that combines its dependent children. This ensures that, conditional on $C$ being satisfied, the children are independent and standard AND/OR propagation is correct.

The principle: **factor the common cause above the correlation it creates.**

When this is not structurally possible (e.g., two OR-alternatives that share a common cause but also have other OR-alternatives that don't), a **conditioning-based propagation** is needed:

$$P(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$$

where $P_\Sigma(G \mid C = c)$ is computed by standard AND/OR propagation with $C$ fixed. This costs $O(2^k \cdot (\lvert V\rvert + \lvert E\rvert))$ where $k$ is the number of common-cause nodes — tractable for small $k$, exponential in general.

### When naive L1 gives the correct answer

For AND-chains (no OR-structure): adding a common-cause parent doesn't create problematic sibling correlation because AND-propagation multiplies probabilities in series, not in parallel. The naive construction works for pure AND-topologies. The restructuring is needed specifically when common causes create correlated *siblings under an OR-node*.


---

## Implications for Strategy-DAG's L1 Claim

The L1 description in #def-strategy-dag says: "The independence assumption then holds within the augmented DAG, at the cost of a larger graph."

This is correct **if and only if** the common-cause node is factored above the correlation — i.e., placed as an AND-prerequisite above the OR-structure whose children it correlates. With naive placement (common cause as parent of correlated siblings), the independence assumption does NOT hold between siblings in the propagation formulas.

**Recommended clarification** for strategy-dag: L1 requires that common-cause nodes be structured so that the correlated components become conditionally independent given the common cause, and that the conditioning structure is represented in the DAG topology (common cause above, conditionally independent components below). This is a DAG *design* principle, not a mechanical node-addition procedure.


---

## Potential Appendix Structure

If this spike is promoted to an appendix segment, the structure would be:

**Proposition B.6: Mixed AND/OR with Common-Cause Node (L1 Augmented DAG)**

- Setup: $G = \text{AND}(C, G_{\text{sub}})$, $G_{\text{sub}} = \text{OR}(A_1, A_2)$, $\varepsilon$-greedy
- Statement: Sector condition satisfied with $\alpha_\Sigma = \min(1/(n_C+1), \theta_C(1-\varepsilon)/(n_{A_1}+1), \theta_C\varepsilon/(n_{A_2}+1))$
- This is the first mixed AND/OR case verified (extends B.1-B.4 which are pure topologies)
- Demonstrates that L1 augmentation preserves the sector-condition framework
- Reveals the three-way gating structure: condition testing × evidence starvation × exploration gating

**New worked example material:**
- L0 vs L1 accuracy comparison (quantitative)
- The L1 construction principle (structural requirement)
- When naive vs correct L1 construction matters (OR-nodes only)

The proposition would live in #deriv-edge-credence-dynamics alongside B.1-B.5. The L0/L1 comparison and construction principle could go in a discussion section of #def-strategy-dag or as a new appendix detail segment.


---

## Summary

1. **L0 overestimates for OR-nodes under positive correlation** (13% in this example). For AND-nodes, L0 actually underestimates. Mixed DAGs typically overestimate because OR-structure dominates at the root level.

2. **Naive L1 (adding common cause as sibling parent) doesn't fix it.** The AND/OR propagation treats siblings as independent regardless of shared parents.

3. **Correct L1 (factoring common cause above the correlation) fixes it exactly.** $\hat P_\Sigma^{L1} = 0.776$ matches the actual plan success probability.

4. **The sector condition is verified for the L1 DAG.** $\alpha_\Sigma$ combines evidence-starvation (B.2) and exploration-gating (B.4) effects in a three-way gating structure. B.5b transfers losslessly.

5. **L1 has lower $\alpha_\Sigma$ (harder to persist) but honest calibration.** The tradeoff: L0 is easier to maintain but calibrates to a biased target; L1 is harder to maintain but calibrates to reality.

6. **The L1 construction requires structural judgment.** "Add a common-cause node" is not a mechanical procedure — the node must be positioned to factor out the correlation correctly. This is a DAG design principle that should be made explicit in strategy-dag.
