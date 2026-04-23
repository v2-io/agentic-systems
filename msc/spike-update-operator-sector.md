---
spike: spike-update-operator-sector
type: spike
status: investigatory
date: 2026-04-22
depends-on:
  - sector-persistence-template
  - sector-condition-derivation
  - gain-sector-bridge
  - credit-assignment-boundary
  - edge-update-natural-parameter
  - discrete-sector-condition
  - strategic-dynamics-derivation
  - adaptive-gain-dynamics
  - discussion-identifiability-floor
---

# Spike: Sector Condition on the Update Operator (Log-Odds Credit-Assignment Iteration)

**Status:** Spike (investigatory). Recasts the log-odds credit-assignment update as a discrete dynamical system on the evidence-accumulation sequence and asks whether an A2'-like sector condition can be placed on the *update operator itself* (not on the underlying plant). If yes, the A2' α/β partition transfers to the update layer, Gaps A and B land under one template, and the discrete contraction work in `#discrete-sector-condition` extends from mismatch dynamics to credit-assignment dynamics.

**Date:** 2026-04-22.

**Motivation.** AAD's persistence machinery is continuous-time ODE / Lyapunov, with the discrete-time bridge in `#discrete-sector-condition` (DA2'/DA.1/DA.1S) covering the mismatch ODE only. The log-odds edge update in `#credit-assignment-boundary` is a discrete iteration on $\lambda_k$ whose contraction toward $\lambda_k^\ast$ is neither stated as a sector problem nor covered by the existing discrete apparatus. We write the update as a one-step operator $T$ and ask whether a sector condition of the form

$$(T\lambda - \lambda^\ast)^\top (\cdot)(\lambda - \lambda^\ast) \leq \gamma \lVert\lambda - \lambda^\ast\rVert^2, \qquad \gamma \lt 1$$

can be derived from structural properties of the gradient Jacobian $J$, the identifiability coefficient $\iota$, and the gain schedule $\eta_k$.

**Headline outcome (summary, then derivations).** Under log-odds presentation with linear-in-log-odds dynamics and a step-size floor, the credit-assignment iteration admits an A2'-analog `(O-A2')` contraction condition whose sector constant is the Fisher-weighted product $\iota \cdot \eta_k \cdot \lambda_{\min}(J^\top J / \lVert J\rVert^2)$ on the log-odds coordinate. The stochastic-approximation analog (Robbins-Monro under unbiased gradient estimator) inherits the same contraction in mean-square under a standard step-size schedule. Sub-scope α of `#gain-sector-bridge` transfers structurally: Bayesian and exponential-family updates satisfy `(O-A2')` by construction. Sub-scope β fails structurally: non-Bayesian, non-exponential-family updates generally fail `(O-A2')` — and AAD's `#discussion-identifiability-floor` machinery already accounts for the failure mode via `#edge-update-causal-validity` (regime-C edges have $\iota \approx 0$, hence $\alpha_{\text{op}} \approx 0$, hence frozen credence per `#observability-dominance`). The discrete step-size condition of `#discrete-sector-condition` lifts: under `O-DA2'` (additive Lipschitz bound on $J$) the operator iterates as a Banach contraction with contraction factor derived from `(O-A2')` via Cauchy-Schwarz.

The honest break-test is where Gaps A and B differ: the Fisher metric is in general *non-diagonal under L1' correlation*, so the sector condition transforms rather than breaks — whitening inverts the off-diagonal via `(O-A2'-whit)`. But L1' with unobservable common cause hits `#discussion-identifiability-floor`'s Cramér-Rao refutation (rank-1 Fisher per `#strategic-dynamics-derivation` Prop B.7 refutation): no sector-positive operator exists, so `(O-A2')` fails structurally rather than gracefully. This gives the composition argument a first non-trivial obstruction to absorb.

---

## 1. Operator Formulation

### 1.1 The log-odds credit-assignment update as a map

Fix an edge $k \in E$ of the strategy DAG. Let $\lambda_k \in \mathbb{R}$ be the log-odds credence, $\iota_k \in [0, 1]$ the regime identifiability coefficient (`#edge-update-causal-validity`), $J_k = \partial P_\Sigma / \partial p_k \geq 0$ the per-edge Jacobian at $\hat{p}$, and $\eta_k = 1/(n_k + 1)$ the Beta-Bernoulli edge gain. The `#credit-assignment-boundary` default signal function reads:

*[Definition (credit-assignment operator, log-odds)]*

$$T_k(\lambda_k; o_t) \;=\; \lambda_k + \eta_k \cdot \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert \mathbf{J} \rVert^2}$$

Stack across edges: $T(\boldsymbol\lambda; o_t) = \boldsymbol\lambda + \mathbf{A}(\boldsymbol\lambda)(y_G - \hat P_\Sigma(\boldsymbol\lambda))$, where $\mathbf{A}(\boldsymbol\lambda) = \eta \cdot \operatorname{diag}(\iota) \cdot \mathbf{J} / \lVert \mathbf{J} \rVert^2$ is the per-edge attribution weight vector. Under i.i.d. observations with ground-truth probabilities $\boldsymbol\theta^\ast$ and true log-odds $\boldsymbol\lambda^\ast = \operatorname{logit}(\boldsymbol\theta^\ast)$, $T$ defines a *stochastic* one-step operator.

**Input.** Observation $o_t$ (the outcome signal $y_G \in \{0,1\}$), which enters through the residual $y_G - \hat P_\Sigma$.

**Output.** Per-edge log-odds increment $\Delta \lambda_k = T_k(\lambda_k; o_t) - \lambda_k$.

**Iteration structure.** Apply $T$ repeatedly to a sequence of i.i.d. observations $\{o_t\}_{t=1}^{\infty}$. Let $\boldsymbol\lambda_t$ denote the state after $t$ applications.

The question — is $T$ a contraction toward $\boldsymbol\lambda^\ast$?

### 1.2 Expected-value operator

Define the expected-value operator $\overline T(\boldsymbol\lambda) = \mathbb{E}_{o \sim P(\cdot \mid \boldsymbol\theta^\ast)}[T(\boldsymbol\lambda; o)]$. Under the AAD edge-update model (each observation is one Bernoulli draw from the true outcome distribution at the plan level), $\mathbb{E}[y_G] = \Phi(\boldsymbol\theta^\ast) \geq \hat P_\Sigma(\boldsymbol\lambda)$ holds iff $\boldsymbol\theta^\ast \succeq \sigma(\boldsymbol\lambda)$ for monotone-AND DAGs. So:

*[Derived (expected-value operator, from default signal function + monotone Jacobian)]*

$$\overline T_k(\boldsymbol\lambda) \;=\; \lambda_k + \eta_k \cdot \iota_k \cdot \frac{J_k \cdot (\Phi(\boldsymbol\theta^\ast) - \hat P_\Sigma(\boldsymbol\lambda))}{\lVert \mathbf{J} \rVert^2}$$

Fixed points of $\overline T$ satisfy $\hat P_\Sigma(\boldsymbol\lambda) = \Phi(\boldsymbol\theta^\ast)$ on the identifiable subspace ($\iota_k J_k \neq 0$) — i.e., the plan-level confidence matches the ground-truth plan-level success. Off-identifiable coordinates ($\iota_k = 0$ or $J_k = 0$) leave $\lambda_k$ fixed at its prior, consistent with `#observability-dominance`.

**Target.** Let $\boldsymbol\lambda^\ast$ denote *any* fixed point of $\overline T$ in the identifiable subspace. Uniqueness of $\boldsymbol\lambda^\ast$ requires the plan-level success function $\Phi$ to be strictly monotone and the identifiable subspace to be dimension-full — conditions satisfied for monotone AND/OR DAGs with all regime-A edges but not in general.

---

## 2. Sector Condition on the Operator (`O-A2'`)

### 2.1 Candidate condition

Write $e_k = \lambda_k - \lambda_k^\ast$ (log-odds error from truth) and $\boldsymbol e = \boldsymbol\lambda - \boldsymbol\lambda^\ast$. The operator contracts toward $\boldsymbol\lambda^\ast$ iff

$$\boldsymbol e^\top \mathbb{E}[T(\boldsymbol\lambda; o) - \boldsymbol\lambda^\ast] \leq (1 - \gamma) \lVert \boldsymbol e \rVert^2$$

for some $\gamma \in (0, 1]$. Equivalent to: $\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \boldsymbol\lambda^\ast) \leq (1 - \gamma) \lVert \boldsymbol e \rVert^2$. Substituting $\overline T$'s definition and using $\overline T(\boldsymbol\lambda^\ast) = \boldsymbol\lambda^\ast$:

$$\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \overline T(\boldsymbol\lambda^\ast)) \leq (1 - \gamma) \lVert \boldsymbol e \rVert^2$$

*[Formulation `(O-A2')` — operator-level sector condition]*

The update operator $T$ satisfies `(O-A2')` on $\mathcal{B}_R = \{\boldsymbol\lambda : \lVert \boldsymbol\lambda - \boldsymbol\lambda^\ast\rVert \leq R\}$ with sector constant $\alpha_{\text{op}} \gt 0$ iff:

$$\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \boldsymbol\lambda) \leq -\alpha_{\text{op}} \lVert \boldsymbol e \rVert^2, \qquad \forall \lVert \boldsymbol e \rVert \leq R$$

That is, the expected operator displacement projects *backward* (toward truth) along the error direction with at least sector-constant efficiency $\alpha_{\text{op}}$ per step.

This is the direct discrete-time analog of A2': replacing the continuous-time correction function $F(\delta)$ with the operator displacement $\boldsymbol\lambda - \overline T(\boldsymbol\lambda)$ (or equivalently, the expected negative increment $-\mathbb{E}[\Delta \boldsymbol\lambda]$). The contraction factor in norm follows by Cauchy-Schwarz plus an operator-Lipschitz bound (§3.3).

### 2.2 Derivation of `(O-A2')` from structural properties

*[Derived (`(O-A2')` from default-signal gradient attribution + monotone Jacobian + Bayesian evidential additivity)]*

Compute $\overline T_k - \lambda_k$ from §1.2 and dot with $\boldsymbol e$:

$$\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \boldsymbol\lambda) = \sum_k e_k \cdot \eta_k \cdot \iota_k \cdot \frac{J_k \cdot (\Phi - \hat P_\Sigma)}{\lVert \mathbf{J} \rVert^2}$$

Factor:

$$= \frac{1}{\lVert \mathbf{J} \rVert^2} \left( \sum_k \eta_k \iota_k J_k e_k \right) (\Phi - \hat P_\Sigma)$$

The key step (Step 1): for monotone-AND DAGs with all regime-A edges, $\Phi - \hat P_\Sigma$ and $\sum_k J_k (\lambda_k^\ast - \lambda_k) = -\sum_k J_k e_k$ share the same sign when $\boldsymbol e$ is small (linearization of $\hat P_\Sigma$ around $\boldsymbol\lambda^\ast$). More precisely, expand $\hat P_\Sigma(\boldsymbol\lambda) = \Phi + \mathbf{J}_\lambda^\top (\boldsymbol\lambda - \boldsymbol\lambda^\ast) + O(\lVert \boldsymbol e \rVert^2)$ where $\mathbf{J}_\lambda = \mathbf{J} \cdot \operatorname{diag}(\sigma'(\boldsymbol\lambda))$ is the log-odds-coordinate Jacobian (a positive diagonal rescaling). Then:

$$\Phi - \hat P_\Sigma = -\mathbf{J}_\lambda^\top \boldsymbol e + O(\lVert \boldsymbol e \rVert^2)$$

Substituting:

$$\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \boldsymbol\lambda) = -\frac{1}{\lVert \mathbf{J} \rVert^2} \left( \sum_k \eta_k \iota_k J_k e_k \right) \left( \sum_k J_{\lambda, k} e_k \right) + O(\lVert \boldsymbol e \rVert^3)$$

Since $J_{\lambda, k} = J_k \cdot \sigma'(\lambda_k)$ with $\sigma'(\lambda_k) \in (0, 1/4]$, both parentheses are linear forms in $\boldsymbol e$. Define the *attribution vector* $a_k = \eta_k \iota_k J_k$ and the *log-odds-sensitivity vector* $b_k = J_k \sigma'(\lambda_k)$. Then:

$$\boldsymbol e^\top (\overline T(\boldsymbol\lambda) - \boldsymbol\lambda) = -\frac{1}{\lVert \mathbf{J} \rVert^2} (\boldsymbol a^\top \boldsymbol e)(\boldsymbol b^\top \boldsymbol e) + O(\lVert \boldsymbol e \rVert^3)$$

*[Derived — generic form, valid for arbitrary monotone attribution.]*

**Case 1: Componentwise attribution (Prop B.5b, componentwise).** When the Jacobian is diagonal ($J_k$ depends only on $\lambda_k$, as in a set of independent disjunctive root-to-leaf paths), both $\boldsymbol a$ and $\boldsymbol b$ are parallel to $\boldsymbol e$ componentwise, and the product $(\boldsymbol a^\top \boldsymbol e)(\boldsymbol b^\top \boldsymbol e) \geq \sum_k a_k b_k e_k^2 \cdot (1 - \varepsilon)$ for some $\varepsilon \to 0$ as $R \to 0$. The sector constant is:

$$\alpha_{\text{op}}^{\text{comp}} \;=\; \min_k \frac{\eta_k \iota_k J_k^2 \sigma'(\lambda_k^\ast)}{\lVert \mathbf{J} \rVert^2}$$

**Case 2: Coupled attribution.** When the Jacobian is full, $(\boldsymbol a^\top \boldsymbol e)(\boldsymbol b^\top \boldsymbol e) \geq \lambda_{\min}(\tfrac{1}{2}(\boldsymbol a \boldsymbol b^\top + \boldsymbol b \boldsymbol a^\top)) \lVert \boldsymbol e \rVert^2$. This symmetric part is PSD iff $\boldsymbol a$ and $\boldsymbol b$ are "aligned enough" — formally, iff the dot product $\boldsymbol a \cdot \boldsymbol b \geq 0$, which holds because both vectors have nonnegative components. The sector constant is:

$$\alpha_{\text{op}}^{\text{coup}} \;=\; \frac{1}{\lVert \mathbf{J} \rVert^2} \lambda_{\min}\!\left( \tfrac{1}{2}(\boldsymbol a \boldsymbol b^\top + \boldsymbol b \boldsymbol a^\top) \right)$$

In either case, `(O-A2')` holds with $\alpha_{\text{op}} \gt 0$ provided every identifiable edge ($\iota_k J_k \gt 0$) contributes positively.

### 2.3 Sector constant in closed form

*[Derived (operator sector constant)]*

For Bernoulli outcomes at the plan level with Beta-Bernoulli edge updates ($\eta_k = 1/(n_k+1)$), and monotone-AND/OR DAG with all regime-A edges:

$$\alpha_{\text{op}}^{\text{comp}} \;=\; \min_k \frac{1}{n_k + 1} \cdot \iota_k \cdot \frac{J_k^2}{\lVert \mathbf{J} \rVert^2} \cdot \sigma'(\lambda_k^\ast)$$

Reading off the ingredients:

| Factor | Source | Failure mode |
|---|---|---|
| $1/(n_k+1)$ | `#edge-update-via-gain` Beta-Bernoulli gain | Gain collapse as $n \to \infty$ (Prop B.3 weakening) |
| $\iota_k \in [0,1]$ | `#edge-update-causal-validity` regime coefficient | Regime C sets $\iota \approx 0$ — frozen edge |
| $J_k^2 / \lVert \mathbf{J}\rVert^2 \in [0,1]$ | Jacobian attribution fraction | Path-dominated DAG: one $J_k$ large, others near zero |
| $\sigma'(\lambda_k^\ast) \in (0, 1/4]$ | Log-odds-to-probability sensitivity | Saturated edges ($\lambda_k^\ast \to \pm\infty$) |

Each factor is bounded, positive, and structurally tied to AAD quantities. The sector constant degrades gracefully when any one factor shrinks; it vanishes only when a structural identifiability obstruction applies (ι=0 or $J_k=0$).

---

## 3. Sub-scope α Inheritance

### 3.1 Exponential-family / Bayesian sub-scope

`#gain-sector-bridge` sub-scope α (Kalman, conjugate Bayesian, exponential family in natural parameters) is the sub-scope in which A2' is *derived* from B1 directional fidelity. The question is whether `(O-A2')` inherits the same sub-scoping.

*[Derived (α-sub-scope inheritance, from Bayesian coherence + evidential-additivity uniqueness)]*

**Claim.** For agent classes in sub-scope α of `#gain-sector-bridge`, `(O-A2')` holds with $\alpha_{\text{op}}^{\text{comp}}$ as derived above.

**Argument.** Within sub-scope α, the update is Bayesian in the log-odds coordinate by `#edge-update-natural-parameter`'s evidential-additivity uniqueness theorem:

$$\lambda_k^{\text{post}} - \lambda_k^{\text{prior}} = \ell(y)$$

with $\ell(y) = \log[P(y \mid H_1)/P(y \mid H_0)]$ the per-observation log-likelihood ratio. The expected log-likelihood ratio at truth is $\mathbb{E}_{y \sim P_{H_1^\ast}}[\ell(y)] = D_{\mathrm{KL}}(P_{H_1^\ast} \Vert P_{H_0^\ast}) \geq 0$, with equality iff the distributions coincide. Therefore, for any $\boldsymbol\lambda$ in the identifiable subspace:

$$\boldsymbol e^\top \mathbb{E}[\boldsymbol\lambda^{\text{post}} - \boldsymbol\lambda] = \boldsymbol e^\top \mathbb{E}[\boldsymbol\ell] \leq 0$$

with strict inequality away from $\boldsymbol\lambda^\ast$. This gives B1-analog directional fidelity at the operator level. Combined with the Jacobian-sensitivity structure (§2.2 Step 1), `(O-A2')` follows. The sector constant $\alpha_{\text{op}}$ is the log-likelihood-ratio second-moment scaled by the attribution structure:

$$\alpha_{\text{op}}^{\text{Bayes}} \;\propto\; \mathbb{E}[\ell(y)^2] = \mathcal{I}(\theta^\ast) \quad (\text{Fisher information at truth})$$

This is the operator-level analog of the `#gain-sector-bridge` factoring $\alpha = \eta \cdot c_{\min}$: the sector constant factors into a gain term ($\eta_k / \lVert \mathbf J \rVert^2$) and a Fisher/attribution term ($\iota_k J_k^2 \sigma'(\lambda^\ast) \cdot \mathcal{I}$).

### 3.2 Variational / β sub-scope — structural failure mode

Sub-scope β of `#gain-sector-bridge` includes variational approximate posteriors (B1 not guaranteed by optimality because approximation-direction error can rotate the correction), non-Bayesian rule-based updates, and severely misspecified agents (FM-5). For these:

*[Derived (β-sub-scope failure, from non-Bayesian evidential-additivity + Jacobian misalignment)]*

**Claim.** For agents in sub-scope β, `(O-A2')` fails structurally unless the correction-direction rotation is bounded.

**Argument.** Without evidential additivity in log-odds (`#edge-update-natural-parameter` scope), the update $\lambda_k^{\text{post}} - \lambda_k^{\text{prior}}$ is not the log-likelihood ratio. The expected update $\mathbb{E}[\boldsymbol\lambda^{\text{post}} - \boldsymbol\lambda^{\text{prior}}]$ can rotate by up to the approximation angle $\theta_{\text{var}}$ of the variational posterior — specifically, for reverse-KL variational approximations, the rotation is bounded by the chain-rule additivity defect per `#strategy-cost-regret-bound` §6.1. If $\theta_{\text{var}} \lt \pi/2$, `(O-A2')` holds with an attenuated sector constant $\alpha_{\text{op}} \cdot \cos \theta_{\text{var}}$. If $\theta_{\text{var}} \geq \pi/2$, the expected update projects *away* from truth and the operator diverges.

This is the operator-level analog of `#gain-sector-bridge` FM-1 (directional infidelity). The rotation-tolerance characterization is new.

### 3.3 Summary: Operator-level A2' sub-scope partition

| Sub-scope | Member classes | `(O-A2')` status | Sector constant |
|---|---|---|---|
| **α-op** | Kalman edge-tracker, Beta-Bernoulli, conjugate Bayesian, exp-family in natural params | Derived | $\alpha_{\text{op}}^{\text{Bayes}}$ (§2.3) |
| **β-op conservative** | Variational posteriors with bounded rotation $\theta_{\text{var}} \lt \pi/2$ | Derived (attenuated) | $\alpha_{\text{op}} \cos \theta_{\text{var}}$ |
| **β-op breaking** | Rule-based, severely misspecified, $\theta_{\text{var}} \geq \pi/2$ | Fails | No positive sector constant |

The α-op / β-op partition is structurally parallel to `#gain-sector-bridge` α / β — and transfers the same member classes.

---

## 4. Correlated-Failure Generalization (L1' regime)

### 4.1 Fisher metric under L1' correlation

Under Correlation Hierarchy L1' (`#strategy-dag`), the per-trial Fisher information matrix is non-diagonal — edge credences share variance through the common-cause structure. Write the joint Fisher matrix as:

$$\mathcal{F}(\boldsymbol\lambda^\ast) \;=\; \mathcal{F}_0 + \Delta_{L1'}$$

where $\mathcal{F}_0$ is the L0 (independent) diagonal Fisher and $\Delta_{L1'}$ is the L1' correlation correction (off-diagonal, symmetric, PSD when common-cause observable per Prop B.7). The expected-update step becomes:

$$\mathbb{E}[\boldsymbol\lambda^{\text{post}} - \boldsymbol\lambda^\ast] = -\mathcal{F}(\boldsymbol\lambda^\ast) \cdot (\boldsymbol\lambda - \boldsymbol\lambda^\ast) + O(\lVert \boldsymbol e \rVert^2)$$

### 4.2 Graceful degradation (observable common cause)

*[Derived (`(O-A2')` transfers under observable L1', from Prop B.7 five-way gating)]*

When the common cause $C$ is observable (Prop B.7 sub-case), $\mathcal{F}$ remains PSD with $\lambda_{\min}(\mathcal{F}) \gt 0$. Applying `(O-A2')` with the Jacobian replaced by the Fisher-weighted Jacobian:

$$\alpha_{\text{op}}^{L1'} \;=\; \min_k \frac{\eta_k \iota_k}{\lVert \mathbf J \rVert^2} \cdot \lambda_{\min}(\mathcal{F}(\boldsymbol\lambda^\ast))$$

The correlation enters through $\lambda_{\min}(\mathcal{F})$, which is bounded below by $\lambda_{\min}(\mathcal{F}_0) - \lVert \Delta_{L1'} \rVert$ when the correction is small. Graceful degradation: L1' correlation shrinks but does not zero the sector constant.

### 4.3 Structural break (unobservable common cause)

*[Derived (`(O-A2')` breaks under unobservable L1', from Cramér-Rao rank-1 floor)]*

When $C$ is unobservable, the marginalized Fisher is rank-1 (`#strategic-dynamics-derivation` Prop B.7 refutation, `#discussion-identifiability-floor`). Then $\lambda_{\min}(\mathcal{F}) = 0$ and `(O-A2')` fails structurally — no positive sector constant exists along the unidentifiable direction. This is *not* graceful degradation; it is the same no-go pattern as `#causal-insufficiency-detection` (on-policy L0-vs-L1 via CHT) but at the update-operator layer.

**Interpretation.** The update operator $T$ has the same identifiability-floor structure as the underlying plant: gradual degradation under soft identifiability loss, structural break under hard identifiability loss. The Fisher-whitened repair (multi-channel joint observation per Prop B.7 repair route ii) is the operator-level analog of `#observability-dominance`'s augmentation: observability buys back rank and rank buys back sector constant.

### 4.4 Connection to spike-fisher-whitened-update and spike-l1-update-bias

A Fisher-whitened operator $T_{\text{whit}}(\boldsymbol\lambda) = \boldsymbol\lambda + \mathcal{F}^{-1} \cdot \nabla_{\text{log-lik}}$ would restore componentwise `(O-A2')` at the cost of requiring Fisher rank-full and computationally tractable inversion. For observable L1', this is the path that preserves `(O-A2')` globally; for unobservable L1', no whitening can restore rank, and the structural break remains. This connects directly to the referenced spike topics — the spike here names the operator-level sector problem, which those spikes would address with specific whitening or bias-correction machinery.

---

## 5. Discrete-vs-Continuous Lifting: Step-Size Condition for Operator Contraction

### 5.1 The gap

`#discrete-sector-condition` (DA2'/DA.1/DA.1S) handles mismatch dynamics discretization under a Lipschitz bound on $F_d$ and a step-size constraint $\eta^\ast \lt 2c_{\min}/c_{\max}^2$. The operator formulation here is already discrete (one operator application per observation), so no time-discretization is needed. What we need instead is the analog: under what operator-Lipschitz bound on $J$, $\iota$, and $\eta_k$ does iterated $T$ converge as a Banach contraction?

### 5.2 Operator-Lipschitz condition `(O-DA2')`

*[Formulation `(O-DA2')` — operator-Lipschitz bound]*

$T$ satisfies `(O-DA2')` on $\mathcal{B}_R$ with constant $L_{\text{op}}$ iff:

$$\lVert T(\boldsymbol\lambda; o) - \boldsymbol\lambda \rVert \leq L_{\text{op}} \cdot \lVert \boldsymbol\lambda - \boldsymbol\lambda^\ast \rVert + M_{\text{op}}$$

for all $\boldsymbol\lambda \in \mathcal{B}_R$ and $o$ in the support of the observation distribution, where $M_{\text{op}}$ is the per-step disturbance magnitude (variance of the unbiased estimator).

**Ingredients of $L_{\text{op}}$.** For the default signal function, $\lVert T - \boldsymbol\lambda \rVert \leq \max_k (\eta_k \iota_k |J_k| / \lVert \mathbf J \rVert^2) \cdot |y_G - \hat P_\Sigma|$. Expanding $|y_G - \hat P_\Sigma| \leq 1 + \lVert \mathbf J_\lambda \rVert \cdot \lVert \boldsymbol e \rVert$ gives:

$$L_{\text{op}} \leq \max_k \frac{\eta_k \iota_k J_k}{\lVert \mathbf J \rVert^2} \cdot \lVert \mathbf J_\lambda \rVert$$

Plugging back $J_{\lambda,k} = J_k \sigma'(\lambda_k) \leq J_k / 4$:

$$L_{\text{op}} \leq \max_k \frac{\eta_k \iota_k J_k^2}{4 \lVert \mathbf J \rVert^2} \leq \frac{\max_k \eta_k \iota_k}{4}$$

For Beta-Bernoulli with $n_k \geq 1$, $\eta_k \leq 1/2$ and $\iota_k \leq 1$, so $L_{\text{op}} \leq 1/8$. This is always well below 1 — the operator is *always* Lipschitz-bounded by structural constants, not tuning parameters.

### 5.3 Discrete contraction theorem `(O-DA.1)`

*[Derived `(O-DA.1)` — operator contraction]*

Under `(O-A2')` with constant $\alpha_{\text{op}}$ and `(O-DA2')` with constant $L_{\text{op}}$, the expected iterate satisfies:

$$\lVert \mathbb{E}[\boldsymbol\lambda_{t+1}] - \boldsymbol\lambda^\ast \rVert^2 \leq (1 - 2\alpha_{\text{op}} + L_{\text{op}}^2) \lVert \boldsymbol\lambda_t - \boldsymbol\lambda^\ast \rVert^2 + \sigma_{\text{op}}^2$$

where $\sigma_{\text{op}}^2$ is the per-step variance (unbiased estimator noise). The contraction factor $\lambda_{\text{op}}^2 = 1 - 2\alpha_{\text{op}} + L_{\text{op}}^2$ is $\lt 1$ iff $\alpha_{\text{op}} \gt L_{\text{op}}^2 / 2$. For Beta-Bernoulli, $L_{\text{op}} \leq 1/8$, so $L_{\text{op}}^2 / 2 \leq 1/128$. The step-size condition reduces to:

$$\alpha_{\text{op}} \;\gt\; \tfrac{1}{128}$$

This is always satisfied in the identifiable regime — $\alpha_{\text{op}}$ is set by structural constants (see §2.3) that stay well above $1/128$ unless identifiability collapses. The step-size condition *lifts structurally* from the continuous case, not as a separate tuning parameter.

**Steady-state bound.** The stochastic analog (mean-square contraction) follows the same pattern as `#discrete-sector-condition` DA.1S:

$$\mathbb{E}[\lVert \boldsymbol\lambda_t - \boldsymbol\lambda^\ast \rVert^2] \leq \lambda_{\text{op}}^{2t} \lVert \boldsymbol\lambda_0 - \boldsymbol\lambda^\ast \rVert^2 + \frac{\sigma_{\text{op}}^2}{1 - \lambda_{\text{op}}^2}$$

with the steady-state ball radius $R_{\text{op}}^\ast = \sigma_{\text{op}} / \sqrt{1 - \lambda_{\text{op}}^2}$.

### 5.4 Stochastic-approximation connection

*[Discussion (Robbins-Monro / Borkar 2008 connection)]*

Setting $\eta_k = \eta_0 / (n_k + 1)$ (Beta-Bernoulli) recovers the classical Robbins-Monro step-size schedule $\sum \eta_k = \infty$, $\sum \eta_k^2 \lt \infty$. Under `(O-A2')` (a stochastic-approximation stability condition) and standard Lipschitz regularity of the gradient estimator, Borkar 2008 (*Stochastic Approximation: A Dynamical Systems Viewpoint*) Ch. 2 gives almost-sure convergence $\boldsymbol\lambda_t \to \boldsymbol\lambda^\ast$ through the ODE method. `(O-DA.1)` is the finite-sample mean-square rate; Borkar's theorem is the asymptotic a.s. statement. Both follow from the same structural properties.

**The step-size condition lifts.** `#discrete-sector-condition`'s step-size constraint on continuous-time discretization is replaced, at the operator level, by the ODE-method stability condition — automatically satisfied when `(O-A2')` holds in sub-scope α. No separate step-size tuning is required when the gain schedule matches Robbins-Monro.

---

## 6. Composition Preview

### 6.1 Parallel edge updates

When multiple edges update in parallel (one observation, multiple edge updates), the composed operator is $T(\boldsymbol\lambda; o) = (T_1(\lambda_1; o), \ldots, T_{|E|}(\lambda_{|E|}; o))$. The sector constant of the composed operator is $\alpha_{\text{op}}^{\text{joint}} = \min_k \alpha_{\text{op},k}$ (worst-case edge), the parallel analog of `#team-persistence`'s cooperative coupling inequality.

*[Derived (parallel composition sector constant, from `(O-A2')` applied componentwise)]*

$$\alpha_{\text{op}}^{\text{joint}} \;\geq\; \min_k \alpha_{\text{op},k} \;=\; \min_k \frac{\eta_k \iota_k J_k^2 \sigma'(\lambda_k^\ast)}{\lVert \mathbf J \rVert^2}$$

Standard (weakest-link) bound. Non-trivial improvement requires correlation structure between the edges — if the edges share a common cause observable ($C$-observable L1'), the joint update can exploit the correlation to gain sector constant beyond weakest-link, exactly as `#critical-mass-composition`'s matched-Tier-1 dyad does at the mismatch level.

### 6.2 Sequential credit assignment (credit pipeline)

When credit flows through multiple DAG layers (plan-level outcome → intermediate-layer edges → root edges), the composed operator is $T = T_{\text{layer-L}} \circ T_{\text{layer-(L-1)}} \circ \cdots \circ T_{\text{layer-1}}$. The sector constant of the composition is the product (operator-analog of the multi-step contraction in `#discrete-sector-condition`):

*[Derived — sequential composition, conditional on layer-wise sector constants]*

$$\alpha_{\text{op}}^{\text{seq}} \;\geq\; \prod_\ell \alpha_{\text{op},\ell}$$

This is the log-additive form: $\log \alpha_{\text{op}}^{\text{seq}} = \sum_\ell \log \alpha_{\text{op},\ell}$, parallel to `#chain-confidence-decay`'s additive log-confidence accumulation. The structure matches `#additive-coordinate-forcing`'s meta-pattern — the log-odds coordinate's additivity lifts to the operator-layer composition.

### 6.3 Concrete base case for Gap B / `spike-operator-sector-unification` (C1)

The pair (`#edge-update-natural-parameter` + `(O-A2')` + parallel composition inequality) gives a concrete base case: for a DAG with $K$ identifiable regime-A edges and observable intermediates, the composed credit-assignment operator is a Banach contraction with sector constant $\geq \min_k \alpha_{\text{op},k}$ and step-size-free convergence. This instantiates the composition-Lyapunov argument at the credit-assignment layer without requiring new machinery.

**What this hands Gap B.** If `spike-operator-sector-unification` (C1) pursues the unification of mismatch-operator and update-operator contraction under a single template, the argument above supplies the concrete base-case operator and sector constant for the credit-assignment side. Gap A (mismatch operator) uses `#discrete-sector-condition`; Gap B (update operator) uses `(O-A2')` as derived here; the unification is sector-persistence-template *applied twice*, with coupling terms characterizing the interaction — exactly the augmented-state Lyapunov composition that `#adaptive-gain-dynamics` (MG-1)–(MG-4) does for fixed-plant / adaptive-gain.

---

## 7. Honest Break-Test: Where the Operator-Sector Formulation Fails

`(O-A2')` / `(O-DA.1)` are not universal. Enumerate the structural failure modes, sharp and without hedging:

### 7.1 Non-monotone gains

If $\eta_k$ is non-monotone in $n_k$ (e.g., resetting-gain schedules, step-size warmup-then-decay, adaptive optimizers like Adam with bias-correction), the fixed-gain Lyapunov argument of §5.3 breaks. The path forward is `#adaptive-gain-dynamics`'s augmented-state approach: treat the gain as state, give it its own sector condition (MG-2), verify timescale separation (MG-3). This is the same composition pattern applied at the operator level — no new machinery, but careful verification required per agent class.

### 7.2 Non-conservative outcome noise

If the per-observation residual $y_G - \hat P_\Sigma$ has bias (biased estimator) or temporal correlation (non-i.i.d. observations), the expected-operator derivation of §1.2 breaks. For biased estimators, `(O-A2')` still holds but $\boldsymbol\lambda^\ast$ shifts to a biased fixed point — the operator converges to $\boldsymbol\lambda^\ast + \text{bias}$, not to truth. For correlated observations, the supermartingale argument of §5.3 becomes a mixing-conditions argument (standard in stochastic approximation but requires additional bookkeeping). In both cases, `(O-A2')` is the right machinery, but the content it delivers is weaker.

### 7.3 Structurally misspecified $J$

The most serious failure: if $\mathbf J$ in the default signal function does not reflect the true causal Jacobian (wrong DAG structure, wrong regime classification, wrong edge identifiability coefficient), the operator converges to a fixed point of the *mis-specified* expected-operator, not the true operator. This is `#gain-sector-bridge` FM-5 (severe misspecification) at the operator level. The fixed point of the misspecified operator is generally offset from truth by a distance proportional to $\lVert \mathbf J - \mathbf J^{\text{true}} \rVert$. `(O-A2')` holds with respect to the misspecified $\boldsymbol\lambda^\ast$, not the true one.

**This is `#discussion-identifiability-floor`'s misspecification-cost open gap at the operator level.** The structural-adaptation route (`#structural-adaptation-necessity`) is needed when the mis-specified fixed point lies outside the task-adequacy threshold.

### 7.4 Rank-deficient Fisher (Cramér-Rao refutation)

Already covered in §4.3: unobservable L1' common cause, rank-1 Fisher, structural break. No sector-positive operator exists. The only repair routes are (i) augment observability (Prop B.7 repair route ii) or (ii) accept plan-level-only tracking (L0-on-marginals fallback).

### 7.5 The `#approximation-tiering` structural classification transfers

| Tier | Class membership | `(O-A2')` status |
|---|---|---|
| Tier 1 (proved, global) | Kalman, conjugate Bayesian, exp-family in natural params, L2-regularized strongly-convex | `(O-A2')` derived globally; `(O-DA.1)` converges |
| Tier 2 (proved, local) | Gradient on locally strongly convex loss, well-tuned PID | `(O-A2')` derived in basin; `(O-DA.1)` converges from basin |
| Tier 3 (domain-specific) | Rule-based, variational with high rotation, severely misspecified | `(O-A2')` case-by-case; structural-adaptation often required |

This transfers `#approximation-tiering`'s structural classification directly to the update operator. No new ladder is needed.

---

## 8. Candidate Landing

### 8.1 Primary target: new appendix segment `#update-operator-sector`

**Type:** `derivation` (status: `conditional`).

**Dependencies:** `sector-persistence-template`, `sector-condition-derivation`, `gain-sector-bridge`, `credit-assignment-boundary`, `edge-update-natural-parameter`, `edge-update-causal-validity`, `discrete-sector-condition`, `strategic-dynamics-derivation`, `identifiability-floor`.

**Contents:**

1. Operator formulation of the default signal function (§1 here).
2. `(O-A2')` — operator-level sector condition, derived from `#gain-sector-bridge` B1 + `#edge-update-natural-parameter` evidential-additivity (§2 here).
3. `α-op / β-op` sub-scope partition inheriting from `#gain-sector-bridge` α/β (§3 here).
4. Correlated-failure generalization with graceful L1'-observable / structural L1'-unobservable break (§4 here).
5. `(O-DA.1)` contraction theorem with step-size condition derived from structural constants (§5 here).
6. Composition preview — parallel + sequential composition sector constants (§6 here).
7. Break-test classification with `#approximation-tiering` transfer (§7 here).
8. Derivation-audit table (O-BP14 convention).

**Why an appendix rather than extension of `#sector-persistence-template`:** The template is about state-variable Lyapunov persistence on continuous-time mismatch dynamics. The operator-level result is about discrete-time credit-assignment iteration — structurally different object (operator vs. correction function), different failure modes (rank-deficient Fisher vs. sector-breakdown beyond $\mathcal B_R$), different composition pattern (Banach contraction vs. augmented-state Lyapunov). Making the operator formulation a separate appendix preserves the template's clean statement and surfaces the operator-layer result as its own derivation.

### 8.2 Secondary landing: extension of `#discrete-sector-condition`

Add a new §7 to `#discrete-sector-condition` titled "Operator-level sector analog" that states `(O-A2')` and `(O-DA.1)` as extensions of DA2'/DA.1 to the update-operator setting. Cross-reference `#update-operator-sector` for the full derivation. This positioning makes visible that `#discrete-sector-condition` covers *two* discrete-time objects: the event-driven mismatch update and the observation-driven credit-assignment operator, under two sector conditions (DA2', `O-A2'`) that share structural form.

### 8.3 Tertiary landing: unification segment `#operator-sector-unification` (Gap B base case)

If Gap B / C1 becomes concrete, a unification segment would state the shared Banach-contraction-under-sector-condition template across both mismatch and update layers, with `(MG-1)`–`(MG-4)`-style timescale-separation conditions characterizing interaction. This is one step beyond where the spike currently lands — it requires the actual composition proof, not just the parallel-and-sequential sector constants derived here.

**Recommendation:** land §§1–7 as `#update-operator-sector` (primary), add §7 of `#discrete-sector-condition` as a cross-reference stub (secondary), defer `#operator-sector-unification` until Gap B has a concrete target.

### 8.4 Integration with the three meta-segments

`#update-operator-sector` composes cleanly with AAD's three meta-patterns:

- **`#discussion-separability-pattern`.** Adds a seventh ladder (update-operator sector scope): sub-scope α-op (separable-core, Bayesian/exp-family), β-op conservative (structured-repair, bounded-rotation variational), β-op breaking (general-open, unbounded-rotation or severely misspecified).
- **`#discussion-identifiability-floor`.** Adds an instance: rank-deficient Fisher under unobservable L1' is a Cramér-Rao-floor no-go at the operator level (§4.3 here). This is the fourth `#discussion-identifiability-floor` instance, complementing on-policy CHT no-go, L1' mixture-identifiability obstruction, and misspecification-cost extension.
- **`#additive-coordinate-forcing`.** Adds an *application* of the log-odds coordinate forcing from `#edge-update-natural-parameter`: the sequential-composition sector constant (§6.2 here) is log-additive specifically because the log-odds coordinate is the uniquely-forced additive evidence coordinate. The operator-layer composition inherits the log-additive structure — the three-layer additive-decomposition pattern extends to the operator-composition layer as an *adjacent instance* (classified parallel to Lyapunov quadratic and IB Lagrangian in `#additive-coordinate-forcing`).

---

## 9. Epistemic Assessment

### 9.1 What's derived

Strength per section, honestly:

| Section | Content | Tier |
|---|---|---|
| §1 | Operator formulation of default signal function | Definition |
| §2.1 | `(O-A2')` candidate condition | Formulation |
| §2.2 | `(O-A2')` derivation from structural properties | **Derived (conditional on monotone-AND + regime-A + small-$R$ linearization)** |
| §2.3 | Closed-form sector constant $\alpha_{\text{op}}^{\text{comp}}$ | Derived |
| §3.1 | α-sub-scope inheritance, `(O-A2')` derived for Bayesian agents | **Derived (conditional on `#edge-update-natural-parameter` evidential-additivity axiom)** |
| §3.2 | β-sub-scope failure mode (rotation-bounded variational attenuation) | Robust qualitative |
| §4.2 | `(O-A2')` graceful degradation under observable L1' | Derived (conditional on Prop B.7 five-way gating) |
| §4.3 | `(O-A2')` structural break under unobservable L1' | **Proved (external theorem: Cramér-Rao)** |
| §5.3 | `(O-DA.1)` discrete contraction theorem | Derived (conditional on `(O-A2')` + `(O-DA2')`) |
| §5.4 | Robbins-Monro / Borkar 2008 connection | Derived (external theorem) |
| §6.1 | Parallel composition sector constant (weakest-link) | Derived |
| §6.2 | Sequential composition (log-additive) | **Derived (conditional on layer-wise sector constants)** |
| §6.3 | Concrete base case for Gap B | Derived |
| §7 | Break-test classification | Robust qualitative |

### 9.2 What's not derived

- **Section 7.3 (structurally misspecified $J$) is open.** The misspecification-cost question at the operator level is the operator-layer version of `#discussion-identifiability-floor`'s misspecification-cost open gap. A tight bound on $\lVert \boldsymbol\lambda_{\text{miss}}^\ast - \boldsymbol\lambda^\ast \rVert$ in terms of $\lVert \mathbf J - \mathbf J^{\text{true}} \rVert$ is not given here.
- **Unification with mismatch operator (Gap B).** §6.3 says the spike *supplies* a base case, not that it *closes* the gap. The actual unification — a single template covering both mismatch and update layers with coupling characterization — is deferred.
- **Non-AND DAGs.** The monotone-AND-with-regime-A derivation in §2.2 Step 1 uses nonnegativity of Jacobian components. For OR-nodes, the Jacobian can have mixed signs, and the derivation of `(O-A2')` requires sign-control arguments that are sketched but not worked through here.
- **Operator-Lipschitz constant $L_{\text{op}}$ is conservative.** The bound $L_{\text{op}} \leq 1/8$ in §5.2 uses $\sigma'(\lambda) \leq 1/4$ and $\eta_k \leq 1/2$ pessimistically. For specific DAGs, $L_{\text{op}}$ can be computed more tightly.
- **Fixed-point uniqueness.** §1.2 asserts uniqueness under strict-monotonicity assumptions that should be checked per DAG class. Multiple fixed points in the identifiable subspace are possible for non-AND DAGs.

### 9.3 Max attainable

*Conditional* — `(O-A2')` is conditional on structural properties (monotone-AND, regime-A, evidential-additivity axiom) that are genuinely agent-class-dependent. Within sub-scope α, these conditions are derivable; within sub-scope β, they are not. The α-op / β-op sub-scoping is honest scope narrowing, not scope retreat — parallel to `#sector-condition-derivation`'s A2' sub-scoping.

The break-test (§7) is sharp: the three structural failure modes (non-monotone gains, non-conservative outcome noise, structurally misspecified $J$) plus the Cramér-Rao refutation (§4.3) together characterize where `(O-A2')` fails. This is the honest scope boundary.

### 9.4 The "strengthen before soften" posture

The spike attempts the strong form — a universal sector condition on the update operator — and finds it holds structurally in sub-scope α, degrades gracefully in one family of sub-scope β cases (variational with bounded rotation), breaks structurally in two others (unobservable L1' Cramér-Rao, severely misspecified $J$). The α / β partition inherited from `#gain-sector-bridge` is the right landing: `(O-A2')` is derived where A2' is derived, assumed where A2' is assumed, and breaks where Cramér-Rao floors the identifiability of the update direction itself.

This is genuine strengthening — before the spike, the log-odds update's contraction toward truth was implicit; now it has an operator-level sector condition with closed-form sector constant factoring into $\eta$, $\iota$, $J^2/\lVert\mathbf J\rVert^2$, $\sigma'(\lambda^\ast)$ (§2.3), each term structurally tied to AAD quantities that already carry their own scope and epistemic status.

---

## 10. Recommended Follow-Ups

1. **Land `#update-operator-sector`** as primary deliverable. Format: `derivation` segment following FORMAT.md §Derivation-audit-table convention. Cross-reference hooks into `#credit-assignment-boundary` (default signal function is now an instance of an `(O-A2')`-satisfying operator), `#edge-update-via-gain` (Beta-Bernoulli gain gives concrete sector constant), `#discussion-identifiability-floor` (fourth instance at operator layer), `#discussion-separability-pattern` (seventh ladder).

2. **Update `#credit-assignment-boundary`** to reference `(O-A2')` as the contraction guarantee underlying its Level-1 design requirement (directional fidelity). This clarifies that directional fidelity gives sector-positive expected update, which via `(O-A2')` + `(O-DA.1)` gives Banach contraction in log-odds.

3. **Update `#edge-update-natural-parameter`** Discussion section with cross-reference: the evidential-additivity axiom's role in deriving `(O-A2')` at the operator level is a load-bearing application beyond the uniqueness theorem stated there.

4. **Extend `#discrete-sector-condition`** with a new §7 "Operator-level analog" that states `(O-A2')` + `(O-DA.1)` as siblings of DA2' + DA.1, cross-referencing the full derivation in `#update-operator-sector`.

5. **Spike follow-ups.** `spike-fisher-whitened-update` could investigate the Fisher-whitened operator $T_{\text{whit}}$ referenced in §4.4 as the L1'-observable repair. `spike-l1-update-bias` could characterize the bias structure of the mis-specified `(O-A2')` fixed point under §7.3 (misspecification cost at operator layer).

6. **Defer** `#operator-sector-unification` until Gap B / C1 has a concrete target. The spike supplies ingredients (parallel weakest-link composition + sequential log-additive composition + base-case sector constant) but not the full unification argument.

---

## Working Notes

- The spike uses $\lambda$ both as log-odds coordinate and as contraction-factor notation — a Notation clash resolvable by renaming the contraction factor to $\rho_{\text{op}}$ in the landing segment. Kept here for readability against `#discrete-sector-condition`'s $\lambda_{\text{eff}}$.
- The operator-Lipschitz bound $L_{\text{op}} \leq 1/8$ in §5.2 is pessimistic because it uses $\sigma'(\lambda) \leq 1/4$ globally. Tighter bounds per specific edge (e.g., $\sigma'(\lambda_k^\ast)$ evaluated at truth) give smaller $L_{\text{op}}$; `(O-DA.1)` is correspondingly looser.
- §2.2 Step 1 uses small-$R$ linearization of $\hat P_\Sigma$. Quadratic-order corrections $O(\lVert \boldsymbol e \rVert^3)$ are absorbed in the proof's $\alpha_{\text{op}} \gt L_{\text{op}}^2/2$ margin; a more careful argument (Taylor expansion with explicit remainder) would give sharper region constants.
- The parallel-composition weakest-link bound in §6.1 is the operator-level `#team-persistence` analog under *cooperative coupling*. Could be strengthened via explicit correlation structure — parallel to `#critical-mass-composition`'s matched-Tier-1 composite result. Specific: if two edges share a common cause observable, their joint Fisher gains rank and $\alpha_{\text{op}}^{\text{joint}}$ can exceed $\min_k \alpha_{\text{op},k}$.
- The sequential-composition log-additive form in §6.2 connects to `#chain-confidence-decay` + `#additive-coordinate-forcing` via the *operator* layer — the log-additive sector constant is a fourth adjacent instance in the additive-coordinate-forcing pattern (after chain, divergence, update), with the coordinate forced by the composition structure rather than by a Cauchy functional equation. Worth surfacing explicitly if the meta-pattern segment is revised.
- Non-AND DAG case (§9.2 third bullet) is the first-order open question. The OR-node Jacobian has mixed signs, and the `(O-A2')` derivation in §2.2 uses nonnegativity. `spike-or-node-strategic-dynamics` has the moment-parameter-form OR-node derivation — extending to the operator formulation would give the first sub-case verification for non-AND DAGs.
