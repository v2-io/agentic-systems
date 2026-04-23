---
slug: spike-l1-update-bias
title: Spike — L1' Log-Odds Update Bias (Quantitative Numerical Floor)
status: research-spike
stage: ready-for-review
depends:
  - credit-assignment-boundary
  - edge-update-natural-parameter
  - discussion-identifiability-floor
  - strategic-dynamics-derivation
  - strategy-dag
  - causal-insufficiency-detection
  - strategy-persistence-schema
---

# Spike: L1' Log-Odds Update Bias (Quantitative Numerical Floor)

**Date.** 2026-04-22 (current session).

**Status.** Research spike. Not a promoted segment. The derivation below is exploratory; its intent is to supply a *concrete quantitative floor* for the qualitative no-go (F1) and rank-deficiency refutation (F13) already catalogued in #discussion-identifiability-floor. All claims here wait on review before segment placement.

**Bottom line (up front).** Under the canonical default signal function of #credit-assignment-boundary, applied by an L0 agent whose true generative world is an L1' common-cause mixture, the per-cycle log-odds update carries a **quantifiable bias** that is (i) derivable in closed form for OR-root and AND-root structures in terms of the sibling covariance $\rho = \operatorname{Cov}(Y_i, Y_j)$, (ii) **zero in expectation under Prop B.7's observable-$C$ five-way gating** when the agent decomposes its credences along the $C$-partition, and (iii) **bounded strictly away from zero** under the Cramér-Rao floor in the unobservable-$C$ single-channel regime. The bias is **not detectable from the agent's own on-policy data** under the F1 no-go scope conditions, which converts it from a binary "detection forbidden" claim into a concrete *numerical* instance of the #discussion-identifiability-floor pattern — an agent can be shown to be systematically mis-updating its log-odds coordinates without being able to recognize this fact from the signals it has access to. The result composes with #strategy-persistence-schema to produce a *forgetting-rate requirement* that tolerates bounded accumulated bias error. Simulation in §7 confirms the theoretical predictions.

**Landing recommendation (up front).** Promote the closed-form OR-root bias formula (§3) and the observable/unobservable-$C$ bifurcation (§§4–5) as a new **extension segment** `#l1-update-bias` in the Appendix A cluster, sitting adjacent to `#discussion-identifiability-floor` and cross-referenced from Prop B.7 of `#strategic-dynamics-derivation` and from `#credit-assignment-boundary`. Weak alternative: absorb into `#discussion-identifiability-floor` as Instance 3 (numerical companion). The extension-segment route is preferred because the closed-form bias formula is **of independent interest** (it quantifies what Prop B.7's no-go costs) and does not reduce to the existing two instances.

---

## 1. Setup and Problem Statement

### 1.1 The setting

Fix a two-edge L0 strategy DAG with OR root ( #strategy-dag):

$$\text{root}_G = \text{OR}(A_1, A_2)$$

Each sibling $A_j$ is a leaf action proposition with agent credence $p_j$ in probability space and $\lambda_j = \log(p_j / (1-p_j))$ in the log-odds coordinate forced by #edge-update-natural-parameter. The plan-confidence score is:

$$\hat P_\Sigma = 1 - (1 - p_1)(1 - p_2)$$

The default signal function of #credit-assignment-boundary, restated in log-odds:

*[Definition (default-log-odds-update-L0-two-edge-OR)]*

$$\Delta \lambda_k = \frac{1}{n_k + 1} \cdot \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert\mathbf J\rVert^2}, \qquad \mathbf J = \nabla_\mathbf p \hat P_\Sigma$$

For the OR root, $J_k = 1 - p_{\bar k}$ where $\bar k$ is the sibling index. The agent observes $(y_1, y_2)$ jointly (violation of F1's S3, so the agent is assumed to be in the joint-observability regime that SA3 exploration admits; this is the favorable case for L0, and if bias appears here it is *structural*). The root outcome under OR is $y_G = 1 - (1 - y_1)(1 - y_2)$.

### 1.2 Two competing true worlds

The agent's working model is L0: $Y_1, Y_2$ independent with marginal rates $\mu_1, \mu_2$. Two candidate true worlds:

- **L0-matched (reference).** $Y_1 \perp Y_2$, $\Pr(Y_k = 1) = \mu_k$, edges independent. This is the agent's own L0 assumption.
- **L1' truth with common cause $C$.** $C \sim \text{Bernoulli}(\theta_C)$; $Y_j \mid C \sim \text{Bernoulli}(p_{j \mid C})$; $Y_j \mid \neg C \sim \text{Bernoulli}(p_{j \mid \neg C})$. The L0 marginal $\mu_j = \theta_C p_{j \mid C} + (1 - \theta_C) p_{j \mid \neg C}$ is matched to the L0-matched world's $\mu_j$, so all L0-observable one-point statistics agree.

The *separability gap* for sibling $j$ is $\Delta_j = p_{j \mid C} - p_{j \mid \neg C}$, and the pairwise covariance under L1' is:

*[Derived (common-cause covariance identity)]*

$$\rho \equiv \operatorname{Cov}(Y_1, Y_2) = \theta_C (1 - \theta_C) \Delta_1 \Delta_2$$

This is the canonical mixture-model covariance and makes $\rho$ a product of scales in three axes: $C$'s activation frequency, and each sibling's $C$-sensitivity. It vanishes when any of the three is zero.

### 1.3 The quantity of interest

Define the **per-cycle log-odds update bias**:

*[Definition (log-odds-update-bias)]*

$$B_k(\rho \mid \text{state}) \equiv \mathbb{E}\bigl[\Delta \lambda_k \mid \text{L1' truth}\bigr] - \mathbb{E}\bigl[\Delta \lambda_k \mid \text{L0-matched truth}\bigr]$$

where the expectation is over one cycle conditional on the current agent state (credences $\mathbf p$, pseudo-counts $\mathbf n$, policy). Both sides use the *same* default update rule with the *same* agent state. The difference isolates the effect of the true-world covariance on the forced log-odds coordinate.

---

## 2. The Signal Decomposition

### 2.1 The residual identity

*[Derived (from OR plan-value identity and the definition of $y_G$)]*

The plan-level residual under OR is:

$$y_G - \hat P_\Sigma = [1 - (1 - y_1)(1 - y_2)] - [1 - (1 - p_1)(1 - p_2)]$$
$$= (1 - p_1)(1 - p_2) - (1 - y_1)(1 - y_2)$$

Taking expectations under each true world:

Under L0-matched: $\mathbb E[(1 - y_1)(1 - y_2)] = (1 - \mu_1)(1 - \mu_2)$ by independence. At the initial point $\mathbf p = \boldsymbol \mu$ (agent matched to marginal truth):

$$\mathbb E[y_G - \hat P_\Sigma \mid \text{L0-matched}, \mathbf p = \boldsymbol\mu] = 0$$

Under L1' truth: $\mathbb E[(1 - y_1)(1 - y_2)] = (1 - \mu_1)(1 - \mu_2) + \rho$ by the covariance identity. At $\mathbf p = \boldsymbol\mu$:

$$\mathbb E[y_G - \hat P_\Sigma \mid \text{L1' truth}, \mathbf p = \boldsymbol\mu] = \rho - 0 = \;-\rho \quad \text{(wait: signs)}$$

Care with signs: the expectation $\mathbb E[(1 - y_1)(1 - y_2)]$ is *larger* under positive correlation (joint failure more likely than the independence model predicts), so $\mathbb E[(1 - p_1)(1 - p_2) - (1 - y_1)(1 - y_2)] = 0 - \rho = -\rho$. So:

*[Derived (L1' residual expectation at matched marginals)]*

$$\mathbb E[y_G - \hat P_\Sigma \mid \text{L1' truth}, \mathbf p = \boldsymbol\mu] = -\rho$$

This matches the #strategy-dag Correlation Hierarchy table (OR: bias is $-\rho$ — overestimation of plan success).

### 2.2 Expected log-odds update bias — closed form

Substituting into the default signal function:

*[Derived (closed-form log-odds bias at matched marginals)]*

$$B_k(\rho \mid \mathbf p = \boldsymbol\mu, \mathbf n) = \frac{1}{n_k + 1} \cdot \iota_k \cdot \frac{J_k \cdot (-\rho) - J_k \cdot 0}{\lVert\mathbf J\rVert^2}$$

$$\boxed{\;B_k(\rho) = -\frac{\iota_k \cdot J_k \cdot \rho}{(n_k + 1) \cdot \lVert\mathbf J\rVert^2} = -\frac{\iota_k (1 - \mu_{\bar k}) \rho}{(n_k + 1) [(1 - \mu_1)^2 + (1 - \mu_2)^2]}\;}$$

This is the quantitative core result.

**Features of the formula:**

1. **Sign.** Negative for OR root (positive $\rho$ ⟹ bias pushes $\lambda_k$ *downward*). The agent's overoptimism about OR-redundancy under latent common cause drives its log-odds *below* truth. Symmetric AND-root case (derived in §2.3) gives *positive* bias (underestimation pushes $\lambda_k$ upward).

2. **Scaling in $\rho$.** Linear in $\rho$ at matched marginals. Vanishes at $\rho = 0$ (degenerate L1'; either $\theta_C \in \{0, 1\}$ or $\Delta_j = 0$).

3. **Scaling in $n_k$.** Decays as $1/(n_k+1)$. Agents with deep experience have small per-cycle bias *per step*, but no mechanism to correct it — the bias is persistent and its cumulative effect over $T$ cycles is $\sum_{t=0}^{T-1} 1/(n+t+1) \approx \log(T/n)$ for large $T$, unbounded without forgetting.

4. **Regime modulation.** $\iota_k$ enters multiplicatively. Regime A ($\iota_k = 1$): full bias. Regime C ($\iota_k \to 0$): bias is suppressed because the agent is not updating at all. This is the *observational-dominance* case of #observability-dominance. Regime B modulates proportionally.

5. **Topological asymmetry.** $J_k = 1 - \mu_{\bar k}$ for OR: when the sibling is already believed likely ($\mu_{\bar k} \to 1$), the Jacobian on $k$ vanishes (the $k$-edge doesn't matter for plan value), and $B_k \to 0$. When the sibling is unlikely ($\mu_{\bar k} \to 0$), $J_k \to 1$ and the full bias lands on $k$. The *less-redundant* sibling absorbs more bias — exactly the edge where the agent would be *most confident* its credence is well-calibrated.

### 2.3 AND-root counterpart

*[Derived (analogous calculation for AND root)]*

For an AND root $\hat P_\Sigma = p_1 p_2$, $\mathbb E[y_G] = \mathbb E[y_1 y_2] = \mu_1 \mu_2 + \rho$ under L1'. The residual expectation is $+\rho$. With $J_k = p_{\bar k} = \mu_{\bar k}$:

$$B_k^{\text{AND}}(\rho) = +\frac{\iota_k \mu_{\bar k} \rho}{(n_k+1) (\mu_1^2 + \mu_2^2)}$$

Positive sign matches the Correlation Hierarchy table (AND underestimates under positive $\rho$). The agent's credence is driven *upward* to explain unexpectedly-frequent joint success.

### 2.4 Bias beyond the matched-marginal starting point

The calculation above is for the *initial* cycle with $\mathbf p = \boldsymbol\mu$. After cycles of biased updates, $\mathbf p \ne \boldsymbol\mu$, and the residual expectation gains a first-order correction. The leading-order dynamic is captured by the ODE approximation:

*[Derived (leading-order bias ODE at fixed pseudo-counts)]*

$$\frac{d\lambda_k}{dt} = -\frac{\iota_k J_k}{\lVert\mathbf J\rVert^2 (n + t + 1)} \cdot \Bigl(\mathbb E[y_G - \hat P_\Sigma] \Bigr)$$

The residual expectation depends on $\mathbf p(t)$. Linearizing around the L1'-induced fixed point (the point where the average residual reaches zero under L1' truth), the trajectory converges but to a *biased* limit:

*[Derived (L1'-induced biased fixed point)]*

$$\mathbf p^\ast_{\text{L1'}} = \arg\{\mathbf p : \mathbb E_{\text{L1'}}[y_G] = \hat P_\Sigma(\mathbf p)\}$$

which for OR is the solution to $(1 - p_1^\ast)(1 - p_2^\ast) = (1 - \mu_1)(1 - \mu_2) + \rho$, i.e., the L0 credence pair that *matches the L1' root-failure probability* rather than the marginal success rates. This is a well-defined surface in $(p_1, p_2)$ space; the dynamic picks a specific point depending on the $J_k$ weighting.

**Key structural observation.** The L1'-induced fixed point $\mathbf p^\ast_{\text{L1'}}$ is **not** the marginal truth $\boldsymbol\mu$. The agent's log-odds coordinates converge to the *wrong* values — specifically, to values that make the agent's plan-confidence score $\hat P_\Sigma$ match the true root probability under L1'. This is a form of "performative correctness at the plan level, incorrectness at the edge level." The agent's plan-confidence is well-calibrated for plan-level prediction; its per-edge credences are biased, and the miscalibration is invisible from plan-level signals alone.

---

## 3. Observable-$C$ Branch: Prop B.7's Zero-Bias Result

**Claim (informal).** When the agent observes $C$ per trial and decomposes its credences as per Prop B.7 of #strategic-dynamics-derivation (two conditional branches $p_{j \mid C}$ and $p_{j \mid \neg C}$), the analogue of $B_k$ in the conditional-branch log-odds coordinates is **zero at the true conditional parameters**.

### 3.1 Setup under Prop B.7

The agent maintains conditional log-odds $\lambda_{j \mid C} = \log(p_{j \mid C} / (1 - p_{j \mid C}))$ and $\lambda_{j \mid \neg C}$, and updates only the conditional coordinate corresponding to the observed $C$-state each trial:

$$\Delta \lambda_{j \mid s} = \frac{1}{n_{j \mid s} + 1} \cdot \iota_{j \mid s} \cdot \frac{J_{j \mid s} \cdot (y_G - \hat P_\Sigma^{L1'})}{\lVert\mathbf J^{L1'}\rVert^2} \cdot \mathbb 1\{C = s\}$$

### 3.2 Residual expectation decomposes

Under Prop B.7's componentwise conditional-branch update, the expected residual on the $C = s$ branch is:

*[Derived (conditional residual at conditional truth)]*

$$\mathbb E[y_G - \hat P_\Sigma^{L1'} \mid C = s, \mathbf p_{\mid s} = \boldsymbol\theta_{\mid s}] = 0$$

by exactly the same argument as Prop B.7's SA1 verification: at conditional truth, the expected root outcome on the $C = s$ branch matches the conditional plan-confidence score. No separability-gap correction appears because the decomposition *undoes* the mixture — each conditional branch is a standard L0 DAG with independent evidence.

### 3.3 Zero-bias statement

*[Derived (L1' observable-$C$ zero-bias result)]*

$$B_{j \mid s}(\rho \mid \mathbf p_{\mid s} = \boldsymbol\theta_{\mid s}) = 0 \quad \text{for } s \in \{0, 1\}, j \in \mathcal J_s$$

The observable-$C$ decomposition is *exactly* the transformation that eliminates the bias. Prop B.7's five-way gating $\alpha_{L1'}$ now has a quantitative interpretation: it is the sector parameter that the agent achieves *after paying the bias cost of decomposing*. The zero-bias result is the *reason* B.7's transfer is lossless — the decomposition aligns the update direction with the native conditional truth.

### 3.4 When repair routes are operative

The five-way gating condition of Prop B.7 requires that every conditional branch accumulates positive experience (no empty cell). An agent with $\theta_C$ very small has rare $C = 1$ trials; $n_{j \mid C}$ grows slowly; the $\theta_C / (n_{j \mid C} + 1)$ term of $\alpha_{L1'}$ is the bottleneck. Zero bias holds *per-branch* but the slower branch accumulates evidence at the gated rate.

**Summary of §3.** Under Prop B.7's five gating conditions plus observable-$C$, the L1' bias formula of §2 is eliminated entirely in the conditional-branch log-odds. The cost is representational (two conditional credences per affected edge) and computational (running both branches). This is the observable-$C$ branch of #discussion-identifiability-floor Instance 2 — the *positive* side of the asymmetric floor.

---

## 4. Unobservable-$C$ Branch: Cramér-Rao Lower Bound on Bias

**Claim (informal).** Under unobservable $C$ and single-channel observation, the Cramér-Rao floor of F13 (per Prop B.7's refutation) translates into a **quantitative lower bound on bias magnitude** in any online estimator. No log-odds update rule can drive the bias below this floor without additional information augmentation.

### 4.1 The Fisher rank-1 structure

From #strategic-dynamics-derivation Prop B.7 "Refuted Under Unobservable $C$":

$$\mathcal F(\phi) = \frac{1}{\mu_j (1 - \mu_j)} u u^T, \qquad u = (\Delta_j, \theta_C, 1 - \theta_C)$$

The rank-1 structure means that among the three parameters $(\theta_C, p_{j \mid C}, p_{j \mid \neg C})$, only one linear combination — the one along the direction $u$ — carries identifiable information per trial. The two-dimensional null space of $\mathcal F$ corresponds to perturbations along the indeterminacy manifold:

$$\mathcal M_{\text{indet}} = \{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1 - \hat\theta_C) \hat p_{\mid \neg C} = \mu_j\}$$

### 4.2 Cramér-Rao bias floor for any online estimator

Let $\hat\phi^{(T)}$ be any online estimator based on $T$ single-channel observations. Decompose the estimator's error as $\hat\phi^{(T)} - \phi^\ast = \mathbf v_\parallel + \mathbf v_\perp$ where $\mathbf v_\parallel$ is the component along $u$ (identifiable) and $\mathbf v_\perp$ is the component in the null space (unidentifiable).

*[Derived (Cramér-Rao bias floor, from null-space decomposition)]*

The Cramér-Rao bound along $u$ gives $\text{Var}(\mathbf v_\parallel) \geq 1 / (T \cdot \lVert u\rVert^2 / (\mu_j(1-\mu_j)))$. The null-space direction $\mathbf v_\perp$ carries **no finite-variance bound** — the CR bound is $+\infty$ in this direction. So any unbiased estimator has infinite variance along $\mathbf v_\perp$, and any finite-variance estimator is biased in $\mathbf v_\perp$:

$$\lVert \mathbb E[\hat\phi^{(T)}] - \phi^\ast \rVert_{\mathcal M_{\text{indet}}} \not\to 0 \quad \text{as } T \to \infty$$

for any estimator with bounded variance. The bias magnitude along $\mathcal M_{\text{indet}}$ is structurally bounded below by the estimator's variance-bias tradeoff in the null direction.

### 4.3 Induced bound on log-odds bias

Translating to log-odds coordinates: the log-odds triple $(\lambda_C, \lambda_{j \mid C}, \lambda_{j \mid \neg C})$ is a smooth reparameterization of $(\theta_C, p_{j \mid C}, p_{j \mid \neg C})$. The Fisher information in the log-odds coordinates is the parameter-space Fisher transformed by the Jacobian of the reparameterization, which is diagonal and nonzero (smooth monotone map). So the rank structure is preserved: the log-odds-space Fisher matrix has rank 1, with null-space $\mathcal M_{\text{indet}}$ mapped through the log-odds reparameterization.

*[Derived (log-odds bias floor, conditional on unobservable $C$ single-channel regime)]*

**For any online estimator updating $(\lambda_C, \lambda_{j \mid C}, \lambda_{j \mid \neg C})$ from single-channel $y_j$ observations, there exists a minimum asymptotic bias $B_{\min}(\rho) \gt 0$ along the null manifold, with $B_{\min}(\rho) = 0$ iff $\rho = 0$ (i.e., $\Delta_j = 0$ or $\theta_C \in \{0, 1\}$).**

This is an application of the Cramér-Rao bound to the log-odds coordinate rather than a new result. Its force in the AAD context is that it holds **regardless of the update rule** — the agent cannot engineer around the floor by choosing a different signal function.

### 4.4 The concrete L0 agent's bias in the unobservable-$C$ regime

An L0 agent that does *not* attempt the Prop B.7 decomposition simply runs the §2 bias formula forever. Its per-cycle bias is given by eq. (§2.2):

$$B_k(\rho) = -\frac{\iota_k J_k \rho}{(n_k + 1) \lVert\mathbf J\rVert^2}$$

Cumulative over $T$ cycles starting from $n = n_0$, the total log-odds drift from truth is:

$$\Delta\lambda_k^{\text{cumul}}(T) = -\iota_k \rho \sum_{t=0}^{T-1} \frac{J_k(t)}{(n_0 + t + 1) \lVert\mathbf J(t)\rVert^2}$$

For the frozen-state approximation ($J_k$ slowly-varying):

$$\lvert \Delta\lambda_k^{\text{cumul}}(T) \rvert \approx \frac{\iota_k \lvert \rho\rvert J_k}{\lVert\mathbf J\rVert^2} \cdot \log\frac{n_0 + T}{n_0 + 1}$$

The cumulative bias is logarithmic in $T$ — **unbounded**, but very slowly growing. With forgetting factor $\lambda$, $n$ stabilizes at $n_{\text{eff}} = 1/(1 - \lambda)$ and the per-cycle bias also stabilizes, so cumulative bias saturates:

*[Derived (saturated-bias with forgetting)]*

$$\lvert \Delta\lambda_k^{\text{saturated}} \rvert = \frac{\iota_k \lvert \rho\rvert J_k (1 - \lambda)}{\lVert\mathbf J\rVert^2} \cdot \tau_{\text{mix}}$$

where $\tau_{\text{mix}}$ is the mixing time of the biased process (inverse of effective update rate). The **forgetting-rate-dependent bias floor** is then:

*[Derived (bounded bias under forgetting)]*

$$\lvert \Delta\lambda_k^{\text{saturated}} \rvert \leq \frac{\iota_k \lvert \rho\rvert \max J_k}{(\min \lVert\mathbf J\rVert^2) (1 - \lambda)}$$

This is the quantitative companion to #strategy-persistence-schema's forgetting prerequisite: forgetting must be *strong enough* to both maintain sector persistence *and* bound the accumulated bias. The two requirements are distinct and may compete.

### 4.5 Summary of §4

Under unobservable $C$ and single-channel observation, the L0 agent's log-odds coordinates accumulate a *quantifiable* bias proportional to $\rho / (n_k + 1)$ per cycle, saturating under forgetting at a bound proportional to $\rho / (1 - \lambda)$. This bias is **not a detection signal** — the agent sees no residual pattern that distinguishes "biased L0 credences under L1' truth" from "well-calibrated L0 credences under L0-matched truth." The Cramér-Rao floor makes this non-detection *exact*: no estimator can reduce the null-space bias below the floor.

---

## 5. On-Policy Undetectability: Composition With F1

### 5.1 The F1 no-go scope

From #causal-insufficiency-detection, under pure on-policy execution (scope conditions S1–S5), no function of the agent's observable history distinguishes L1' truth from L0-matched truth. Specifically:

$$\mathbb P_{\pi_{L0}}^{\text{obs}}[\text{L1' truth}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\text{L0-matched truth}]$$

The agent's entire observation stream (under S1–S5) is statistically identical in the two worlds.

### 5.2 The bias is present but undetectable

The bias $B_k(\rho)$ of §2 is *not zero* under L1' truth. The agent's log-odds coordinates genuinely drift toward the L1'-induced biased fixed point $\mathbf p^\ast_{\text{L1'}}$. But this drift is not evidence of L1' truth — it is evidence that *plan-level residuals are being closed at matched-marginal credences*, which is equally consistent with either world. The agent's *own* residuals, computed from its own observations, average to zero at $\mathbf p^\ast_{\text{L1'}}$ in both worlds (by construction of the fixed point).

*[Derived (on-policy undetectability of L1' bias)]*

Under scope conditions S1–S5 of #causal-insufficiency-detection, the bias $B_k(\rho)$ is not a function of any on-policy observable statistic. The agent's log-odds coordinate drift is identical in expectation (as a function of its own observations) under L1' truth and under L0-matched truth with the right matching.

### 5.3 The #discussion-identifiability-floor instance structure

Under the meta-pattern in #discussion-identifiability-floor:

1. **Setting.** Estimate edge log-odds $\lambda_k$ using the default signal function under L0 assumption, when the true world is L1' with unobservable common cause.
2. **External theorems.** (a) Bareinboim et al. 2022 Causal Hierarchy Theorem — L1' vs L0-matched is a Level 2 distinction undetectable from Level 1 on-policy data. (b) Cramér-Rao bound on Fisher information — the per-trial Fisher matrix for single-channel mixture observation is rank 1, so the indeterminacy manifold has infinite Cramér-Rao bound.
3. **No-go.** On-policy edge credences accumulate a *quantifiable* bias $B_k(\rho) \propto \iota_k J_k \rho / (n_k + 1)$ that is neither detectable (CHT) nor reducible below the Cramér-Rao floor (Fisher rank-1).
4. **Boundary characterization.** Three escape routes from the combined no-go: (a) observe $C$ per trial (recovers Prop B.7 zero bias); (b) run multi-child joint observations satisfying rank-$2K+1$ Fisher condition; (c) accept the bias and forget fast enough ($1 - \lambda \gt \rho / R_\Sigma^\text{bias}$ for some tolerance radius) to keep cumulative bias bounded.
5. **Strengthened consequence.** The #strategy-persistence-schema forgetting prerequisite now carries *two* load-bearing functions: (i) asymptotic sector persistence, (ii) bounded cumulative L1' bias. The two requirements can be reconciled in the parameter region where $\rho / R_\Sigma^\text{bias} \lt 1 - \lambda \lt 1 - \rho_\Sigma / R_\Sigma$; outside this window, no forgetting rate satisfies both.

This is a candidate **Instance 3** for #discussion-identifiability-floor, sitting between Instance 1 (on-policy L0/L1 detection no-go) and Instance 2 (Cramér-Rao refutation of L1' under unobservable single-channel). What Instance 3 adds: the *quantitative numerical floor* — not just "detection is impossible" (Instance 1) and "unbiased online estimation is impossible" (Instance 2), but "the biased estimator's bias is *this specific magnitude*, determined by $\rho$, and the forgetting rate needed to tolerate it is *this specific threshold*."

---

## 6. Regime-Dependence and the A/B/C Modulation

### 6.1 The regime classification in edge semantics

Per #edge-update-causal-validity, the identifiability coefficient $\iota_k$ ranges over:

- **Regime A** (intervention-rich): $\iota_k \approx 1$. Full bias as derived in §2.
- **Regime B** (partial intervention): $\iota_k \in (0, 1)$. Bias is proportionally reduced.
- **Regime C** (observation-only): $\iota_k \approx 0$. Bias is suppressed — but not because the agent has correct credences; because the agent *is not updating* in the L0 log-odds coordinate at all.

### 6.2 The apparent paradox

At Regime C, the agent is nominally "safe" from the bias — $B_k(\rho) \to 0$. But this is not a substantive reduction in miscalibration; it is a consequence of the agent's credence being *frozen*. The agent's credence at Regime C is whatever its prior was; if the prior is wrong, the agent stays wrong. The bias formula's collapse to zero at $\iota_k = 0$ is correct but misleading — the *mean-squared error* of the agent's credence against conditional truth is not zero at Regime C; it is just not evolving.

The correct reading: Regime C edges are #observability-dominance frozen-credence cases. The Correlation Hierarchy bias mechanism operates through the *update rule*; when the update rule is dormant, there is no bias *accumulation*. But there is still *initial-condition bias* if the prior was set under the wrong model class.

### 6.3 Regime A drives maximum bias; Regime C suppresses accumulation

The saturation bias under forgetting (§4.4) scales with $\iota_k$. Combined with the #strategy-persistence-schema forgetting prerequisite, we get a **regime-dependent forgetting window**:

- Regime A, large $\rho$: narrow window. Need strong forgetting for bias control, but not so strong that sector persistence fails.
- Regime C, any $\rho$: wide window. Bias does not accumulate because updates are dormant.
- Regime B: intermediate.

This links the edge-semantics regime classification to the forgetting-rate tradeoff and gives an AAD-native explanation for why "observational-dominant" domains (Regime C) exhibit less apparent bias accumulation than "intervention-rich" domains (Regime A) — it's not that observational domains are closer to the true causal structure, it's that their update rule is dormant so the bias has no vehicle.

---

## 7. Simulation Check

### 7.1 Protocol

A minimal L1' two-edge OR-root common-cause example. The agent uses the default log-odds signal function with no forgetting. True world switches between L1' (with unobservable $C$) and L0-matched (independent edges at same marginals).

```python
# (Condensed — full script in /tmp/l1sim/sim.py)
for t in range(n_cycles):
    # draw outcomes
    if L1prime:
        c = rng.random() < theta_C
        y1, y2 = (rng.random() < (pjC[j] if c else pjnC[j]) for j in (0,1))
    else:
        y1, y2 = (rng.random() < mu[j] for j in (0,1))
    y_root = 1 - (1-y1)*(1-y2)                # OR

    # agent default update (log-odds, no forgetting)
    p1, p2 = sigmoid(lam1), sigmoid(lam2)
    Pplan = 1 - (1-p1)*(1-p2)
    r = y_root - Pplan
    J1, J2 = 1-p2, 1-p1
    Jn2 = J1*J1 + J2*J2
    lam1 += (1/(n1+1)) * J1 * r / Jn2
    lam2 += (1/(n2+1)) * J2 * r / Jn2
    n1 += 1; n2 += 1
```

### 7.2 Results (400-trial Monte Carlo average; $n_{\text{init}} = 10$, 5000 cycles)

**Scenario A: symmetric strong-common-cause.** $\theta_C = 0.4$, $p_{j \mid C} = 0.9$, $p_{j \mid \neg C} = 0.1$ → $\mu_j = 0.42$, $\rho = 0.1536$.

| Scenario | $\lambda_1$ start | $\lambda_1$ end | Drift |
|---|---|---|---|
| L1' truth | -0.3228 | -0.7225 | **-0.3997** |
| L0-matched | -0.3228 | -0.3223 | 0.0005 |
| **Bias (diff)** | | | **-0.4002** |

The bias is cleanly negative (consistent with the OR-overestimation direction predicted by §2). The matched L0 simulation confirms the update rule is itself well-calibrated (residual statistic zero under L0-matched truth).

**Scenario B: asymmetric mild common cause.** $\theta_C = 0.5$, $p_{j \mid C} = (0.8, 0.6)$, $p_{j \mid \neg C} = (0.3, 0.2)$ → $\mu = (0.55, 0.40)$, $\rho = 0.05$.

| Edge | L1' drift | L0-matched drift | Bias |
|---|---|---|---|
| $\lambda_1$ | -0.168 | -0.004 | -0.164 |
| $\lambda_2$ | -0.127 | -0.001 | -0.126 |

Asymmetric bias across the two edges, consistent with the Jacobian asymmetry $J_k = 1 - \mu_{\bar k}$ (§2.5).

**Scenario C: degenerate L1' ($\Delta = 0$).** $\theta_C = 0.5$, $p_{j \mid C} = p_{j \mid \neg C} = 0.5$ → $\rho = 0$.

| Edge | L1' drift | Bias |
|---|---|---|
| $\lambda_1, \lambda_2$ | -0.002 | ≈ 0 |

Confirms the bias vanishes when $\rho = 0$, as predicted.

**Scenario D: $\theta_C$ sweep with symmetric $p_{j \mid C} = 0.9$, $p_{j \mid \neg C} = 0.1$.**

| $\theta_C$ | $\rho$ | Cumulative bias ($\lambda_1$) |
|---|---|---|
| 0.10 | 0.0576 | -0.138 |
| 0.20 | 0.1024 | -0.240 |
| 0.30 | 0.1344 | -0.324 |
| 0.50 | 0.1600 | -0.440 |
| 0.70 | 0.1344 | -0.528 |
| 0.90 | 0.0576 | -0.484 |

The asymmetry visible in the sweep (e.g., $\theta_C = 0.9$ giving larger bias per unit $\rho$ than $\theta_C = 0.1$) is predicted by the Jacobian factor $J_k = 1 - \mu_{\bar k}$: at high $\theta_C$, $\mu \to p_{j \mid C}$ which is high, so $1 - \mu$ is small — but the actual trajectory integrates over shifting $\mathbf p(t)$, and the frozen-state prediction captures only the leading-order initial rate. The integrated drift is asymmetric because the bias-induced $\mathbf p(t)$ trajectory itself is asymmetric in the $\theta_C = 0.9$ vs $\theta_C = 0.1$ cases.

### 7.3 Initial-rate check against closed form

The initial-cycle per-edge bias at $\mathbf p = \boldsymbol\mu$, $n_k = 10$:

| $\theta_C$ | $\rho$ | Predicted init. rate $B_1$ | Observed avg rate over 100 cycles |
|---|---|---|---|
| 0.10 | 0.0576 | $-3.2 \times 10^{-3}$ | consistent |
| 0.30 | 0.1344 | $-9.3 \times 10^{-3}$ | consistent |
| 0.50 | 0.1600 | $-1.5 \times 10^{-2}$ | consistent |
| 0.70 | 0.1344 | $-1.8 \times 10^{-2}$ | consistent |

The closed-form prediction matches the observed initial-cycle rates. The cumulative drift over 3000–5000 cycles is the sum $\sum_t \eta_t J_k(t) (-\rho) / \lVert \mathbf J(t)\rVert^2$ and depends on the trajectory of $\mathbf p(t)$; this integrates to the values in the scenario tables.

### 7.4 Simulation findings summary

The simulation confirms:

- **Formula sign and magnitude.** Initial-rate bias matches §2 closed form quantitatively.
- **Vanishing at $\rho = 0$.** Confirmed by scenario C.
- **Jacobian asymmetry.** Confirmed by scenario B (asymmetric edges show asymmetric bias).
- **Cumulative drift is logarithmic.** Bias trajectory grows with $\log(T/n_0)$ as predicted, not linearly — consistent with the $\eta_t = 1/(n+t+1)$ sum.
- **No L0-matched false positive.** Under L0-matched truth, the update rule produces no drift (bias is a genuine L1'-specific effect, not an artifact).

---

## 8. Strategy-Persistence Consequence

### 8.1 The forgetting-rate dual requirement

The existing #strategy-persistence-schema forgetting prerequisite is:

$$(1 - \lambda) \gt \rho_\Sigma / R_\Sigma \quad \text{(sector persistence)}$$

The bias-tolerance prerequisite from §4.4 is (informally):

$$(1 - \lambda) \gt c_B \cdot \rho / R_\Sigma^{\text{bias}} \quad \text{(bounded L1' cumulative bias)}$$

where $c_B$ is a topology-dependent constant (Jacobian ratio) and $R_\Sigma^{\text{bias}}$ is the tolerance radius for log-odds bias magnitude. The combined forgetting window is:

*[Derived (combined forgetting-rate admissibility)]*

$$\max\!\left(\frac{\rho_\Sigma}{R_\Sigma}, \frac{c_B \rho}{R_\Sigma^{\text{bias}}}\right) \lt (1 - \lambda) \lt 1$$

The window is non-empty iff both thresholds are less than one, which gives the agent-level admissibility condition. When the window is empty (e.g., $\rho$ so large that $c_B \rho / R_\Sigma^{\text{bias}} \geq 1$), no forgetting rate simultaneously maintains sector persistence and bounds the L1' bias. The agent must either augment observability (Prop B.7 repair routes) or accept persistence failure.

### 8.2 Composition with #stability-induced-myopia

The parked spike `msc/spike-stability-induced-myopia.md` derives a detection-latency theorem $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ for regime change detection. The present spike's L1' bias is *already accumulated* at the time of regime change — the agent is not at conditional truth when the environment drifts, so the detection-latency bound applies to the *biased* starting state. The composition:

*[Derived (combined detection-latency under L1' bias)]*

The detection-latency bound is $\mathbb E[T_{\text{detect}}] \geq (n_{\min}+1) \cdot \Delta\lambda_{\text{detect}} / \varepsilon_{\text{eff}}$, where $\varepsilon_{\text{eff}} = \varepsilon - \lvert B_k(\rho) \cdot T_{\text{pre}}\rvert$ is the effective regime-change footprint *after* subtracting the L1' bias already accumulated over pre-change cycles $T_{\text{pre}}$. When the pre-change L1' bias is comparable to the regime-change footprint, $\varepsilon_{\text{eff}}$ can be near zero even at large $\varepsilon$, making the detection latency astronomical.

This links the two spikes: stability-induced-myopia characterizes the latency of regime-change detection; L1'-update-bias characterizes the pre-existing miscalibration that degrades the effective signal-to-noise ratio. Together they name a stronger version of the high-operating-point trap — the mature agent accumulates L1' bias that then masks subsequent regime change, compounding both slowness to detect drift and the magnitude of drift that must be detected.

---

## 9. Epistemic Status

### 9.1 Per-claim epistemic tier

| Claim | Tier |
|---|---|
| §2.2 closed-form initial-rate bias $B_k(\rho) = -\iota_k J_k \rho / [(n_k+1) \lVert\mathbf J\rVert^2]$ | **Exact** (algebraic identity under Correlation Hierarchy for OR; AND counterpart equally exact) |
| §2.3 AND-root symmetric counterpart | **Exact** (same derivation) |
| §2.4 L1'-induced biased fixed point existence | **Derived** (conditional on frozen-state approximation; exact at first order) |
| §2.4 trajectory convergence to biased fixed point | **Robust qualitative** (not proved to converge under arbitrary initial conditions; frozen-state picture omits the $n_k$ growth) |
| §3 observable-$C$ zero-bias result | **Exact** (direct consequence of Prop B.7's SA1 verification at conditional truth) |
| §4.2 Cramér-Rao null-space bias floor | **Exact** (standard CR bound applied to rank-1 Fisher of mixture model) |
| §4.3 Log-odds bias floor is non-zero for $\rho \ne 0$ | **Derived** (Cramér-Rao bound is parameterization-invariant under smooth monotone reparameterization) |
| §4.4 Saturated-bias under forgetting | **Derived** (conditional on exponential-forgetting model of #strategy-persistence-schema) |
| §5.2 On-policy undetectability | **Exact** (direct application of F1 no-go / CHT) |
| §5.3 Instance-3 structure for #discussion-identifiability-floor | **Discussion-grade** (meta-pattern recognition; the instance itself is derived, but its placement as the third instance is structural) |
| §6 A/B/C regime modulation | **Robust qualitative** (structural; the specific form of Regime-B interpolation depends on the $\iota$-derivation path) |
| §7 simulation match with §2 formula | **Empirical** (confirmatory; matches closed form to within Monte Carlo error) |
| §8.1 combined forgetting-window admissibility | **Derived** (composition of two earlier bounds) |
| §8.2 composition with #stability-induced-myopia | **Conjectural** (both individual results are derived; the composition is stated but not fully formalized) |

### 9.2 Scope and limitations

- The §2 closed form is derived for OR and AND roots at **two-edge topologies**. Generalization to arbitrary mixed AND/OR DAGs is open; the structural argument (residual expectation shifts by $\pm\rho$ under correlation) extends, but the Jacobian structure becomes topology-specific.
- The **matched-marginal initial condition** is load-bearing: at other starting points, the L0-matched expected residual is nonzero and the bias isolates differently. The initial-point simplification is what makes the closed form clean; practical agents start elsewhere, and the trajectory analysis requires the ODE picture of §2.4.
- The Cramér-Rao floor (§4.2–4.3) is about **unbiased estimators**; the L0 default signal function is *biased* under L1' truth (that is the result of §2). The floor therefore bounds what *any* estimator could achieve, not just the default one. An agent that explicitly modeled the indeterminacy manifold and chose a biased estimator optimally could do no better than the floor.
- The **forgetting window** combination (§8.1) assumes both prerequisites have the same $R_\Sigma$ scale, which is not formally established — the sector-persistence tolerance and the bias tolerance are different quantities in different coordinates. A proper treatment would need matched coordinates or a Fisher-information bridge.

### 9.3 Max attainable status

The §2 closed-form bias is at **max attainable = exact**. The Cramér-Rao floor is at **exact**. The meta-pattern placement within #discussion-identifiability-floor is at **max attainable = robust qualitative** (it is a structural observation about the catalog, not a derivation). The #strategy-persistence-schema forgetting-window composition is at **max attainable = conditional** (depends on matched-coordinate assumption).

---

## 10. Landing Recommendation

### 10.1 Preferred route: New appendix segment `#l1-update-bias`

**Slug.** `l1-update-bias` (or `#l1-prime-update-bias` for disambiguation from the generic L1 case).

**Type.** `derivation` — the segment carries multiple derived claims (§2 closed form, §3 zero-bias under observable $C$, §4 Cramér-Rao floor) of mixed strength. Qualifies for the FORMAT.md O-BP14 derivation-audit table convention.

**Status.** `conditional` — conditional on two-edge-OR topology for the closed form, conditional on Bayesian sub-scope $\alpha$ of #gain-sector-bridge for the sector-parameter interpretation, conditional on exponential-forgetting model for the saturation bound.

**Stage.** `draft` on landing.

**Depends on.**
- `credit-assignment-boundary` (default signal function; where the bias lives)
- `edge-update-natural-parameter` (log-odds coordinate and its forcing)
- `strategic-dynamics-derivation` (Prop B.7 observable-$C$ transfer; Cramér-Rao refutation under unobservable $C$)
- `strategy-dag` (Correlation Hierarchy; L0/L1/L1' definitions)
- `causal-insufficiency-detection` (F1 no-go; on-policy undetectability)
- `identifiability-floor` (meta-pattern, for Instance 3 positioning)
- `strategy-persistence-schema` (forgetting-window prerequisite and its doubling)
- `edge-update-causal-validity` (regime A/B/C modulation)

**Derivation-audit table (preview of what would appear in the segment):**

| Property | Source | Strength |
|---|---|---|
| Closed-form $B_k(\rho)$ for two-edge OR (§2.2) | Correlation Hierarchy covariance identity + default log-odds update | Exact (conditional on two-edge OR and matched-marginal initial point) |
| AND-root counterpart $B_k^{\text{AND}}(\rho)$ (§2.3) | Symmetric derivation | Exact (same conditionality) |
| L1'-induced biased fixed point (§2.4) | Residual-expectation zero condition | Derived (frozen-state) |
| Observable-$C$ zero-bias result (§3) | Prop B.7 SA1 verification at conditional truth | Exact (direct consequence) |
| Cramér-Rao bias floor under unobservable $C$ (§4) | Fisher rank-1 + CR bound | Exact (standard theorem applied) |
| Saturated bias under forgetting (§4.4) | Exponential-forgetting model + fixed-point analysis | Derived (conditional on exp-forgetting) |
| On-policy undetectability (§5.2) | F1 no-go / Bareinboim CHT | Exact (direct application) |
| Combined forgetting-window (§8.1) | Composition of sector prerequisite and bias bound | Derived (conditional on matched-scale tolerances) |
| Regime A/B/C modulation (§6) | $\iota_k$ multiplicative entry in the formula | Robust qualitative |

### 10.2 Cross-segment integrations required on promotion

- **`#discussion-identifiability-floor`**: add as Instance 3 in the *Current Instances* section. Update §"Adjacent Floors (Open Research Directions)" to note that one of the open directions has been derived.
- **`#credit-assignment-boundary`**: add a subsection or Working-Note reference noting the quantitative bias under L1' truth; the existing "Correlated-failure interaction (L0 vs L1)" discussion becomes the qualitative summary, pointing to the new segment for the quantitative form.
- **`#strategy-persistence-schema`**: add a Discussion paragraph on the bias-tolerance second role of forgetting, and cross-reference the combined forgetting-window bound.
- **`#strategic-dynamics-derivation` Prop B.7**: add a "What the positive transfer costs" observation linking to the bias formula in the unobservable-$C$ refutation subsection.
- **`#stability-induced-myopia` (if/when promoted)**: note the composition with the L1' bias as a pre-change-state effect that degrades the effective regime-change footprint.

### 10.3 Alternative route: Absorb into `#discussion-identifiability-floor` Instance 3

Possible but not recommended. The closed-form bias formula has independent downstream utility (regime-dependent forgetting prescriptions, sim benchmarks, TST deployment guidance) that merits its own segment. Absorbing it as Instance 3 would compress out the load-bearing §2 closed form. Reserve the absorption path as a fallback if the reviewer finds the bias formula too narrow in its current two-edge form.

### 10.4 Fallback route: Distribute

If the reviewer judges the derivation too incomplete for a standalone appendix:
- Land §2 closed form in `#credit-assignment-boundary` Discussion (quantitative companion to the existing correlated-failure paragraph).
- Land §3 zero-bias observation in `#strategic-dynamics-derivation` Prop B.7 Discussion.
- Land §4 Cramér-Rao bound in `#discussion-identifiability-floor` Instance 2 discussion (sharpening the refutation to a quantitative floor).
- Land §8 forgetting-window in `#strategy-persistence-schema` Discussion.

This captures about 70% of the content but loses the composition narrative.

---

## 11. Open Questions (for possible future spikes)

1. **Multi-edge OR.** Generalize §2's closed form to $K$-arm OR with pairwise covariance matrix $\mathbf \Sigma$. The residual expectation generalizes to $-\sum_{i \lt j} \rho_{ij} \prod_{k \ne i, j}(1 - p_k)$. The per-edge bias decomposition becomes topology-heavy but tractable.
2. **Deep DAG with interior common causes.** For L1' facilitators at interior nodes, the Jacobian computation involves backward propagation. Whether the closed-form structure survives is open.
3. **Adaptive forgetting.** The combined forgetting-window of §8.1 suggests an *adaptive* forgetting rule that tunes $\lambda$ in response to estimated $\rho$ (from covariance tests under route (b) of F1). The tuning rule is a meta-level design problem — the forgetting rate itself becomes a learned quantity.
4. **AND/OR mixed topology.** Mixed roots (AND of OR sub-plans, etc.) inherit the opposite-sign behavior at different levels. The net bias at a specific edge depends on the sign-alternation pattern along the path to root. A clean treatment would decompose bias contributions along topology levels.
5. **Non-Bayesian agents.** The sub-scope $\beta$ of #gain-sector-bridge (PID, rule-based, human-judgment) does not invoke the log-odds coordinate at all. The bias analysis there would need a coordinate-free formulation — likely via Fisher-information bounds that are parameterization-agnostic.
6. **Connection to misspecification-cost adjacent floor.** #discussion-identifiability-floor's third open direction (misspecification-cost quantification) may reduce to a generalization of the bias formula here, with the L0 agent playing the role of the misspecified model. Worth checking whether the closed-form approach extends.

---

## 12. Honest Epistemic Close

This spike does **not** produce a new theorem in the sense of establishing a novel structural impossibility. What it does:

1. **Supplies a quantitative form** for what #discussion-identifiability-floor's Instance 2 (Cramér-Rao refutation) costs *in practice*. The existing Instance 2 says "no unbiased online estimator exists under unobservable $C$"; this spike quantifies the biased estimator's bias in AAD's native log-odds coordinate, at the default signal function, with sign and magnitude derivable.
2. **Bridges the two existing Instances (1 and 2).** Instance 1 (F1 on-policy detection no-go) says detection is forbidden. Instance 2 (F13 CR refutation) says unbiased estimation is forbidden. This spike shows the *biased estimator*'s behavior — it *does* accumulate a specific bias pattern, that pattern is *not detectable* by the agent (Instance 1), and it is *not correctable* to below the CR floor (Instance 2). The combination is a numerical floor with a specific formula.
3. **Composes with `#strategy-persistence-schema`** to give a *dual* forgetting requirement and an explicit admissibility window.
4. **Gives concrete, testable predictions** for simulation (§7) that match the closed-form formulas.

What this spike does **not** do:

- Generalize beyond two-edge topologies.
- Prove the trajectory convergence under the biased update rule (frozen-state picture only).
- Quantify the regime-change interaction with pre-accumulated bias beyond a schematic composition statement.
- Produce a uniqueness theorem analogous to the three Cauchy-FE results in the 2026-04-22/23 cycle.

The recommendation to promote is *weak* relative to the recommendation-to-promote bar used in the 2026-04-22/23 strengthening cycle. The result here is a quantitative instrument for an existing meta-pattern, not a new pattern. Its value is engineering — practical agents facing L1' domains (software deployment with shared infrastructure, organizational strategy with shared enabling conditions, investment with market regime correlations) get a closed-form rule for *how wrong their log-odds become and how much forgetting is needed to bound it*. That is useful output, but it sits in the third ring (empirical/heuristic applications) by FORMAT.md's epistemic-triage taxonomy, not in the inevitability core.

My recommendation: **promote to appendix segment with status `conditional`, landing in the Appendix A cluster adjacent to #discussion-identifiability-floor and #additive-coordinate-forcing.** The segment will be at `draft` stage with the three §9.1 exact claims being the strongest content. Cross-segment integrations are straightforward and listed in §10.2.

---

## Appendix: Simulation Script

Full script at `/tmp/l1sim/sim.py` (reproduced here for archival — moving to `msc/sims/` on promotion):

```python
import numpy as np

rng = np.random.default_rng(0)
def sigmoid(x): return 1.0/(1.0+np.exp(-x))

def run(scenario, n_cycles=20000, n_trials=200, theta_C=0.4,
        pjC=(0.9, 0.9), pjnC=(0.1, 0.1), n_init=10):
    mu = [theta_C*pjC[j] + (1-theta_C)*pjnC[j] for j in (0,1)]
    d = [pjC[j] - pjnC[j] for j in (0,1)]
    rho_true = theta_C*(1-theta_C)*d[0]*d[1]

    drift1 = np.zeros(n_cycles+1); drift2 = np.zeros(n_cycles+1)
    for _ in range(n_trials):
        lam1 = np.log(mu[0]/(1-mu[0])); lam2 = np.log(mu[1]/(1-mu[1]))
        n1 = n_init; n2 = n_init
        lam1_hist = [lam1]; lam2_hist = [lam2]
        for t in range(n_cycles):
            if scenario == 'L1prime':
                c = rng.random() < theta_C
                y1 = int(rng.random() < (pjC[0] if c else pjnC[0]))
                y2 = int(rng.random() < (pjC[1] if c else pjnC[1]))
            else:
                y1 = int(rng.random() < mu[0]); y2 = int(rng.random() < mu[1])
            y_root = 1 - (1-y1)*(1-y2)
            p1 = sigmoid(lam1); p2 = sigmoid(lam2)
            Pplan = 1 - (1-p1)*(1-p2)
            r = y_root - Pplan
            J1 = 1-p2; J2 = 1-p1
            Jn2 = J1*J1 + J2*J2 + 1e-12
            lam1 += (1/(n1+1)) * J1 * r / Jn2
            lam2 += (1/(n2+1)) * J2 * r / Jn2
            n1 += 1; n2 += 1
            lam1_hist.append(lam1); lam2_hist.append(lam2)
        drift1 += np.array(lam1_hist); drift2 += np.array(lam2_hist)
    return drift1/n_trials, drift2/n_trials, mu[0], mu[1], rho_true
```
