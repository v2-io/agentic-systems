# Spike: Finding 13 — Strengthening Attempt for Prop B.5b (L1' Sector Transfer)

**Status:** Spike — strengthening attempt (Move-1 through Move-8). Outcome: partial success. The full unconditioned version of Prop B.5b is *refuted at the linearization* by a rank-deficient Fisher matrix; a clean derived sub-case (B.5b-obs-C) is established with explicit $\alpha_{L1'}$ and global scope.

**Date:** 2026-04-22

**Source finding:** `msc/pending-findings-2026-04-22.md` Finding 13 (lines 457–482).

**Predecessor spike:** `msc/spike-finding-13-l1-default-narrowing.md` — softening repair to `#strategy-dag` headline. This spike attempts the harder structural move (derive the L1' transfer) before falling back to softening; the softening repair remains valid as a fallback for the non-derived sub-cases.

**Companion material:** `msc/spike-L1-worked-example.md`; `01-aad-core/src/worked-example-L1.md` (lines 120-136); `01-aad-core/src/strategy-dag.md` (Correlation Hierarchy); `01-aad-core/src/strategic-dynamics-derivation.md` (Props B.5, B.5b, B.6); `01-aad-core/src/strategy-persistence-schema.md`; `01-aad-core/src/edge-update-via-gain.md`; `01-aad-core/src/credit-assignment-boundary.md`.

---

## §1. Strengthening Attempt Log

The objective: derive Prop B.5b — the L1' analog of Prop B.6 — establishing that the sector condition transfers from per-conditional-edge credences to plan-confidence error for an L1' (mixture-form) DAG.

| Move | Description | Outcome |
|---|---|---|
| **M1** | Set up L1' update dynamics (responsibilities, soft Beta-Bernoulli on each conditional, $\hat\theta_C$ update) | ✓ Done. Two sub-cases identified: (A) $C$ observable per trial, (B) $C$ unobservable, joint update |
| **M2** | Define error variables $\xi = (\xi_C, \xi_{\vert C}, \xi_{\vert\neg C})$ and correction function $F(\xi)$ | ✓ Done. SA1 verified at truth for both sub-cases |
| **M3** | Linearize at equilibrium; compute Jacobian | ✓ Done. **For SUB-A**: Jacobian is diagonal with positive entries. **For SUB-B**: Jacobian equals the Fisher matrix scaled by $1/(n+1)$ — and the Fisher matrix is *rank 1* (not rank 3) — see §4.3 |
| **M4** | Verify or refute conjecture $\alpha_{L1'} \approx \alpha_{L0} \cdot \min(\theta_C, 1-\theta_C) \cdot s$ | ✗/✓ The conjecture is *qualitatively* correct (separability and branch-balance both gate the rate) but *quantitatively* the structure is branch-specific gating, not a uniform scaling. SUB-A gives the precise form: each conditional branch carries its own gating factor |
| **M5** | Extend to nonlinear (global) sector condition | ✓ For SUB-A: global by direct extension of B.6's argument (componentwise Beta-Bernoulli on each branch). ✗ For SUB-B: cannot extend a globally-zero linearization to a global guarantee |
| **M6** | State the full Prop B.5b | ✗ As stated for the *general* L1' case (no scope restriction): **fails**. Rank-1 Fisher means SA2' admits no $\alpha \gt 0$. ✓ As **B.5b-obs-C** (derived sub-case with $C$-observability): succeeds globally |
| **M7** | Sub-case fallbacks | ✓ Three sub-case results carved out: B.5b-obs-C (full derivation), B.5b-multi-channel (sketch with explicit identifiability requirement), B.5b-known-thetaC-soft-EM (still rank-deficient, requires multi-channel) |
| **M8** | Strengthened segment text | ✓ Drafted for `#strategy-dag` headline + Correlation Hierarchy table + new B.5b proposition for `#strategic-dynamics-derivation` |

**Net outcome.** A clean, fully-derived sub-case (B.5b-obs-C) with a precise five-way-gating $\alpha_{L1'}$ formula. The fully *general* L1' case is refuted, not merely unverified — there is a fundamental identifiability obstruction (Fisher rank deficiency from a single binary observation channel) that no additional clever update rule can overcome. The narrowing is therefore *principled*: L1' transfers cleanly when $C$ is observable; otherwise it requires either multi-channel structure (sketch) or an explicit information augmentation (interventional probing of $C$). This collapses Finding 13's narrowing from "L1' formal transfer is open" into "L1' formal transfer is established for the observable-$C$ sub-case (B.5b-obs-C); the joint-Bayesian sub-case is structurally obstructed by mixture identifiability and requires either $C$-observation or multi-child observability for repair."

---

## §2. Statements

### Prop B.5b-obs-C (Derived) — L1' Sector Transfer Under Observable Common Cause

> **Setup.** Mixture-form L1' DAG with binary common cause $C$ (true prior $\theta_C \in (0,1)$) gating a sub-plan with conditional structure $G_{\mid C}$ (under $C=1$) and $G_{\mid \neg C}$ (under $C=0$). Plan-confidence: $\hat P_\Sigma^{L1'} = \hat\theta_C \cdot P_\Sigma(G_{\mid C}) + (1-\hat\theta_C) \cdot P_\Sigma(G_{\mid \neg C})$. Per-conditional credences $\hat p_{j\mid C}, \hat p_{j\mid \neg C}$ for each affected child $j$. Agent observes $C$-state directly each trial (e.g., $C$ is a condition leaf in the L1 sense — an observable proposition). Edge dynamics: Beta-Bernoulli per conditional branch, with the agent updating only the active branch on each trial.
>
> **Statement.** Under Beta-Bernoulli updating with observable common cause and componentwise updates on each conditional branch, the expected correction function satisfies the sector condition globally (within the natural region $\lVert\xi\rVert \leq 1$ in joint credence space), with sector parameter
>
> $$\alpha_{L1'} = \min\!\left(\frac{1}{n_C + 1},\; \min_{j \in \mathcal{J}_C} \frac{\theta_C \cdot \pi_{j\mid C}}{n_{j\mid C} + 1},\; \min_{j \in \mathcal{J}_{\neg C}} \frac{(1-\theta_C) \cdot \pi_{j\mid \neg C}}{n_{j\mid \neg C} + 1}\right)$$
>
> where $\mathcal J_C$ ($\mathcal J_{\neg C}$) is the set of children tested under $C=1$ ($C=0$), $\pi_{j\mid C}$ is the action-selection probability for child $j$ conditional on $C=1$ (e.g., $1-\varepsilon$ for greedy, $\varepsilon$ for explore in an OR-node), and $n_{j\mid C}$ is the per-conditional edge experience.
>
> **Bridge.** Under *facilitator monotonicity* ($P_\Sigma(G_{\mid C}) \geq P_\Sigma(G_{\mid \neg C})$ — the defining property of a soft facilitator), the plan-value Jacobian $\mathbf{J} = \nabla_{\hat\phi} \hat P_\Sigma^{L1'}$ is non-negative. Then by Prop B.5b (componentwise nonlinear case), the sector condition transfers losslessly to plan-confidence error: $\alpha_s = \alpha_c = \alpha_{L1'}$.
>
> *[Derived (Conditional on Beta-Bernoulli model, observable common cause, facilitator monotonicity)]*
>
> **Region.** Global, with the same caveats as Props B.1, B.2, B.4, B.6: $\alpha_{L1'} = 1/(n+1)$-class parameters decay with experience, so trajectory persistence requires the experience-discounting prerequisite of `#strategy-persistence-schema`.

### Prop B.5b-multi-channel (Sketch) — L1' Under Multi-Child Observability

> **Setup.** L1' mixture form, $C$ unobservable, but $K \geq 2$ children share $C$ with linearly independent conditional-success profiles $(\theta_{j\mid C}, \theta_{j\mid \neg C})$. Joint observations $(y_1, \ldots, y_K)$ are generated per trial from the same $C$-realization.
>
> **Statement (sketch).** When the joint Fisher information across children has rank $2K+1$ (full rank in the $(\theta_C, \{p_{j\mid C}, p_{j\mid \neg C}\})$ parameter space), an SA1-preserving online EM update admits a sector parameter
>
> $$\alpha_{L1'}^{\text{multi}} \;\geq\; \frac{\sigma_{\min}(\mathcal{F})}{\max_k(n_k + 1)}$$
>
> where $\mathcal{F}$ is the per-trial joint Fisher matrix.
>
> **Open.** The full-rank condition requires both that the conditional profiles span the parameter space and that the agent observes children jointly (not in isolation across trials). For typical strategic DAGs where children are tested one at a time, this sub-case does not apply directly — see §4.3.

### Sub-case B.5b-known-thetaC-single-channel — REFUTED (Fisher rank deficient)

> Even with $\theta_C$ *known* and only one child $j$ being learned ($p_{j\mid C}, p_{j\mid \neg C}$), the Fisher information from $y_j$ alone is rank 1, not rank 2. Soft EM converges to *some* point on the indeterminacy manifold $\{(p, q) : \theta_C p + (1-\theta_C) q = \mu\}$, not to the truth. SA2' admits no $\alpha \gt 0$ for the joint $(p_{j\mid C}, p_{j\mid \neg C})$ vector.

### Full Prop B.5b (general L1') — REFUTED

> Without scope restriction (no $C$-observability, no multi-child structure, no side-information channel), L1' admits no sector parameter $\alpha \gt 0$ for the joint conditional-credence vector. **The mixture is unidentifiable from a single binary observation channel.** This is a Fisher-information lower bound, not a defect of the soft-EM update rule: any unbiased online estimator of the conditionals must respect the Cramér-Rao bound, and the Cramér-Rao bound is infinite in the unidentifiable directions.

---

## §3. Setup: L1' Update Dynamics (Move 1)

### 3.1 The Mixture Generative Model

Common cause $C \in \{0, 1\}$ with $P(C=1) = \theta_C$. Per child $j$ with parents that include $C$ as a soft facilitator, true success rates differ across $C$-states:

- $P(y_j = 1 \mid C = 1) = \theta_{j\mid C}$
- $P(y_j = 1 \mid C = 0) = \theta_{j\mid \neg C}$

with the soft-facilitator condition $\theta_{j\mid C} \gt \theta_{j\mid \neg C}$ and importantly $\theta_{j\mid \neg C} \gt 0$ (this is what distinguishes L1' from strict-prerequisite L1, where $\theta_{j\mid \neg C} = 0$).

Marginal: $P(y_j = 1) = \mu_j := \theta_C \theta_{j\mid C} + (1-\theta_C) \theta_{j\mid \neg C}$.

### 3.2 Agent Beliefs

Agent maintains:
- $\hat\theta_C \in [0, 1]$: credence on the common cause being active.
- $\hat p_{j\mid C}, \hat p_{j\mid \neg C} \in [0, 1]$: per-conditional success credences for each child $j$.

Joint plan-confidence:

$$\hat P_\Sigma^{L1'} = \hat\theta_C \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid C}) + (1 - \hat\theta_C) \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C})$$

where $P_\Sigma(\hat{\mathbf{p}}_{\mid s})$ is the standard L0 AND/OR propagation evaluated on the conditional credences for $C = s$.

Agent's marginal forecast: $\hat\mu_j = \hat\theta_C \hat p_{j\mid C} + (1-\hat\theta_C)\hat p_{j\mid \neg C}$.

### 3.3 Update Rules — Two Sub-Cases

**SUB-A ($C$ observable per trial).** The agent observes $(C_t, y_{j,t})$ per trial. Updates decouple:

- $\hat\theta_C$ updates on $C_t$:
$$\Delta \hat\theta_C = \frac{C_t - \hat\theta_C}{n_C + 1}$$
- If $C_t = 1$ and child $j$ tested: $\hat p_{j\mid C}$ updates Beta-Bernoulli on $y_{j,t}$:
$$\Delta \hat p_{j\mid C} = \frac{y_{j,t} - \hat p_{j\mid C}}{n_{j\mid C} + 1}$$
- If $C_t = 0$ and child $j$ tested: $\hat p_{j\mid \neg C}$ updates Beta-Bernoulli on $y_{j,t}$:
$$\Delta \hat p_{j\mid \neg C} = \frac{y_{j,t} - \hat p_{j\mid \neg C}}{n_{j\mid \neg C} + 1}$$

The two conditional branches are *non-interacting* in the update — exactly because $C$-observation lets the agent *route* each trial's evidence to the correct branch.

**SUB-B ($C$ unobservable).** Agent observes only $y_{j,t}$. The minimal SA1-preserving update is *online soft EM* with responsibility-weighted Beta-Bernoulli on each branch:

1. Compute responsibility (posterior on $C$ given $y_{j,t}$ under current beliefs):
$$\gamma_j(y_{j,t}; \hat\phi) = \frac{\hat\theta_C \cdot \hat p_{j\mid C}^{y_{j,t}}(1-\hat p_{j\mid C})^{1-y_{j,t}}}{\hat\theta_C \cdot \hat p_{j\mid C}^{y_{j,t}}(1-\hat p_{j\mid C})^{1-y_{j,t}} + (1-\hat\theta_C) \cdot \hat p_{j\mid \neg C}^{y_{j,t}}(1-\hat p_{j\mid \neg C})^{1-y_{j,t}}}$$

2. Soft Beta-Bernoulli on the active conditional, weighted by responsibility:
$$\Delta \hat p_{j\mid C} = \gamma_j \cdot \frac{y_{j,t} - \hat p_{j\mid C}}{n_{j\mid C} + 1}, \qquad \Delta \hat p_{j\mid \neg C} = (1-\gamma_j) \cdot \frac{y_{j,t} - \hat p_{j\mid \neg C}}{n_{j\mid \neg C} + 1}$$

3. Update $\hat\theta_C$ via the responsibility (a Robbins-Monro stochastic-approximation step toward the posterior marginal of $C$):
$$\Delta \hat\theta_C = \frac{\gamma_j - \hat\theta_C}{n_C + 1}$$

This is a standard online-EM update; see Cappé & Moulines (2009) for the canonical treatment of stochastic-approximation EM for latent-data models. The Robbins-Monro step on $\hat\theta_C$ averages responsibilities, which under correct identification converges to $\theta_C$.

### 3.4 Error Variables

Define $\xi = (\xi_C, \{\xi_{j\mid C}, \xi_{j\mid \neg C}\}_j)$ where $\xi_C := \theta_C - \hat\theta_C$, $\xi_{j\mid s} := \theta_{j\mid s} - \hat p_{j\mid s}$. The state vector lives in $[-1, 1]^{2K+1}$ for $K$ mixture-affected children.

The expected per-trial change defines the correction function $F(\xi) := -E[\Delta\xi]$ (negative because $\xi$ is the truth-minus-belief signed gap, while the update reduces $\hat\phi$'s deviation from $\theta$). The sector condition requires $\xi^T F(\xi) \geq \alpha \lVert\xi\rVert^2$ in some operating region $\lVert\xi\rVert \leq R$.

---

## §4. Linearization, Jacobian, Fisher Information (Moves 2-3)

### 4.1 SA1 Verification at Truth (Both Sub-Cases)

**SUB-A.** At $\hat\phi = \theta$ (truth), each branch's expected update is zero by standard Beta-Bernoulli analysis:
- $E[\Delta\hat\theta_C \mid \hat\theta_C = \theta_C] = (E[C] - \theta_C)/(n_C+1) = 0$.
- $E[\Delta\hat p_{j\mid C} \mid \hat p_{j\mid C} = \theta_{j\mid C}] = \theta_C \cdot (\theta_{j\mid C} - \theta_{j\mid C})/(n+1) = 0$ (where the $\theta_C$ factor arises from the test-rate conditional on $C=1$).
- $E[\Delta\hat p_{j\mid \neg C}] = 0$ by symmetric argument.

SA1 holds. ✓

**SUB-B.** At truth, by direct calculation:

$$E[\gamma_j(y_{j,t}; \theta)] = P(y=1) \cdot E[\gamma_j \mid y=1] + P(y=0) \cdot E[\gamma_j \mid y=0]$$
$$= \mu_j \cdot \frac{\theta_C \theta_{j\mid C}}{\mu_j} + \bar\mu_j \cdot \frac{\theta_C(1-\theta_{j\mid C})}{\bar\mu_j} = \theta_C \theta_{j\mid C} + \theta_C(1-\theta_{j\mid C}) = \theta_C$$

So $E[\Delta\hat\theta_C \mid \theta] = (\theta_C - \theta_C)/(n_C+1) = 0$. ✓

For $\hat p_{j\mid C}$ at truth:

$$E[\gamma_j (y_j - \theta_{j\mid C})] = E[\gamma_j y_j] - \theta_{j\mid C} E[\gamma_j]$$
$$= P(y=1) \cdot \frac{\theta_C \theta_{j\mid C}}{\mu_j} - \theta_{j\mid C} \cdot \theta_C = \theta_C \theta_{j\mid C} - \theta_C \theta_{j\mid C} = 0$$

So $E[\Delta \hat p_{j\mid C} \mid \theta] = 0$. ✓ Symmetric for $\hat p_{j\mid \neg C}$.

**SA1 holds for both sub-cases.** This was a non-obvious check for SUB-B; the responsibility-weighting structure preserves the at-truth zero precisely because the Bayes posterior on $C$, integrated under the true generative distribution, recovers the marginal $\theta_C$.

### 4.2 SUB-A: Diagonal Jacobian, Positive Entries

Linearize at truth. With $\xi_C = \theta_C - \hat\theta_C$ small:

$$E[\Delta\hat\theta_C \mid \xi] = \frac{\theta_C - \hat\theta_C}{n_C + 1} = \frac{\xi_C}{n_C+1}$$

So $-E[\Delta\xi_C] = -\xi_C/(n_C+1) \cdot (-1) = \xi_C/(n_C+1)$ (the $-1$ is because $\xi_C = \theta_C - \hat\theta_C$ moves opposite to $\hat\theta_C$). Then $F_C(\xi) = \xi_C/(n_C+1)$.

For $\hat p_{j\mid C}$, the test-rate on $C=1$ branch is $\theta_C \cdot \pi_{j\mid C}$ where $\pi_{j\mid C}$ is the action-selection probability for $j$ conditional on $C=1$:

$$E[\Delta\hat p_{j\mid C} \mid \xi] = \theta_C \pi_{j\mid C} \cdot \frac{\theta_{j\mid C} - \hat p_{j\mid C}}{n_{j\mid C}+1} = \frac{\theta_C \pi_{j\mid C} \cdot \xi_{j\mid C}}{n_{j\mid C}+1}$$

So $F_{j\mid C}(\xi) = \theta_C \pi_{j\mid C} \xi_{j\mid C} / (n_{j\mid C}+1)$. Symmetric for $\hat p_{j\mid \neg C}$ with factor $(1-\theta_C) \pi_{j\mid \neg C}$.

The Jacobian $\mathbf J_F = \partial F / \partial \xi$ at truth is **diagonal** with positive entries:

$$\mathbf{J}_F = \mathrm{diag}\!\left(\frac{1}{n_C+1},\; \left\{\frac{\theta_C \pi_{j\mid C}}{n_{j\mid C}+1}\right\}_{j \in \mathcal{J}_C},\; \left\{\frac{(1-\theta_C)\pi_{j\mid \neg C}}{n_{j\mid \neg C}+1}\right\}_{j \in \mathcal{J}_{\neg C}}\right)$$

Sector product near equilibrium:

$$\xi^T F(\xi) = \frac{\xi_C^2}{n_C+1} + \sum_{j \in \mathcal{J}_C} \frac{\theta_C \pi_{j\mid C} \xi_{j\mid C}^2}{n_{j\mid C}+1} + \sum_{j \in \mathcal{J}_{\neg C}} \frac{(1-\theta_C) \pi_{j\mid \neg C} \xi_{j\mid \neg C}^2}{n_{j\mid \neg C}+1}$$

$$\geq \alpha_{L1'} \cdot \lVert\xi\rVert^2$$

with $\alpha_{L1'}$ as stated in §2 (Prop B.5b-obs-C).

This is the **SUB-A linearization result.** It is also exact globally (§5) because the Beta-Bernoulli update is linear in $\xi$, not just at first order — same algebra as B.6.

### 4.3 SUB-B: Fisher-Information Analysis — The Rank-1 Obstruction

Consider one mixture-affected child, dropping the $j$ subscript. Parameters: $\phi = (\theta_C, p_{\mid C}, p_{\mid \neg C})$.

**Soft EM as Fisher scoring.** The expected soft-EM step at truth equals (up to the $1/(n+1)$ scaling) the natural-gradient ascent step on the expected log-likelihood — which is Fisher scoring (Cappé & Moulines 2009; cf. Sato 1999, "Online Model Selection Based on the Variational Bayes"). The Jacobian of $F$ at truth is therefore:

$$\mathbf{J}_F = \frac{\mathcal{F}(\theta)}{n+1}$$

where $\mathcal{F}(\theta)$ is the Fisher information matrix of the mixture model evaluated at truth. (A direct algebraic verification by perturbing the responsibility expressions in §3.3 around truth produces the same matrix — the identification is a fact about EM convergence, not an artifact of any particular derivation route.)

**Computing $\mathcal{F}$.** Score functions $s_k(y; \phi) = \partial_\phi \log P(y; \phi)$:

- $s_{\theta_C}(y=1) = \Delta/\mu$, $s_{\theta_C}(y=0) = -\Delta/\bar\mu$, where $\Delta := p_{\mid C} - p_{\mid \neg C}$ is the *separability gap*.
- $s_{p_{\mid C}}(y=1) = \theta_C/\mu$, $s_{p_{\mid C}}(y=0) = -\theta_C/\bar\mu$.
- $s_{p_{\mid \neg C}}(y=1) = (1-\theta_C)/\mu$, $s_{p_{\mid \neg C}}(y=0) = -(1-\theta_C)/\bar\mu$.

Fisher information $\mathcal F_{kl} = E[s_k s_l]$. Direct computation:

$$\mathcal{F} = \frac{1}{\mu \bar\mu} \begin{pmatrix} \Delta^2 & \Delta\theta_C & \Delta(1-\theta_C) \\ \Delta\theta_C & \theta_C^2 & \theta_C(1-\theta_C) \\ \Delta(1-\theta_C) & \theta_C(1-\theta_C) & (1-\theta_C)^2 \end{pmatrix}$$

**Rank-1 factorization.** Let $u := (\Delta, \theta_C, 1-\theta_C)^T$. Then $\mathcal{F} = u u^T / (\mu\bar\mu)$. So $\mathcal{F}$ has **rank 1** for any non-degenerate mixture (i.e., any $u \neq 0$). The non-zero eigenvalue is $\lVert u\rVert^2/(\mu\bar\mu) = (\Delta^2 + \theta_C^2 + (1-\theta_C)^2)/(\mu\bar\mu)$; the other two eigenvalues are zero.

**Consequence for SA2'.** The smallest eigenvalue of the Jacobian $\mathbf J_F = \mathcal{F}/(n+1)$ is zero, so

$$\inf_{\xi \neq 0} \frac{\xi^T F(\xi)}{\lVert\xi\rVert^2} = \frac{\lambda_{\min}(\mathcal{F})}{n+1} = 0.$$

**No $\alpha \gt 0$ admits the sector inequality for the joint conditional-credence vector under SUB-B with a single observation channel.** The two-dimensional null space of $\mathcal{F}$ corresponds to perturbations $\xi$ that move along the indeterminacy manifold $\{\hat\phi : \hat\theta_C \hat p_{\mid C} + (1-\hat\theta_C) \hat p_{\mid \neg C} = \mu\}$ — these directions are *unobservable* from a single-channel binary signal, and the Cramér-Rao bound is infinite there.

**This refutes the unconditioned Prop B.5b at the linearization level.** It also explains why Finding 13's narrowing was needed: L1' transfer is not merely "open" — it is *fundamentally obstructed* whenever $C$ is not observable and there is no multi-channel structure to break the identifiability degeneracy.

### 4.4 SUB-B Multi-Channel Case (Sketch)

For $K \geq 2$ children sharing $C$, with linearly independent conditional profiles and **joint per-trial observation** (i.e., the agent observes $(y_1, \ldots, y_K)$ from the *same* trial's $C$-realization), the joint Fisher matrix is:

$$\mathcal{F}_{\text{joint}} = E\!\left[\sum_k s^{(k)} (s^{(k)})^T\right]$$

(plus cross-terms because the $y_k$ share $C$). Each $s^{(k)}$ contributes a rank-1 piece in the $(\theta_C, p_{k\mid C}, p_{k\mid \neg C})$ subblock. The joint Fisher rank can in principle reach $2K + 1$ — but only when the joint observation is available, which is a strong structural requirement: the agent must run all $K$ children in parallel under the same $C$-realization.

**For typical strategic DAGs** where the agent attempts one child at a time across separate trials (with $C$ resampled or not directly observed), the joint observation is unavailable, and per-trial each $y_k$ contributes only its own rank-1 Fisher piece — degenerate again.

This sub-case is therefore *sketched, not derived*: it provides a clean identifiability sufficient condition (full joint Fisher rank) but its applicability to standard strategy DAGs is limited and the conditions under which agents can collect joint multi-child observations require further specification.

---

## §5. Conjecture Verification (Move 4)

The task spec proposed:
$$\alpha_{L1'} \approx \alpha_{L0} \cdot \min(\theta_C, 1-\theta_C) \cdot s$$
where $s$ is a separability factor.

**Verdict.** Qualitatively right, quantitatively wrong:

| Element | Conjecture | Actual (B.5b-obs-C) |
|---|---|---|
| Base rate | $\alpha_{L0} = 1/(n+1)$ | $1/(n_{j\mid s}+1)$ per conditional branch (separate counts) |
| Branch-balance factor | $\min(\theta_C, 1-\theta_C)$ uniform | Branch-specific: $\theta_C$ on $C=1$ branch, $(1-\theta_C)$ on $C=0$ branch — NOT uniformized to a min |
| Separability factor $s$ | Postulated | **Absent in SUB-A** — observability bypasses separability altogether. Re-emerges in SUB-B as the rank-1 Fisher direction ($\propto \Delta = p_{\mid C} - p_{\mid \neg C}$) |
| Other gating | (Not in conjecture) | Action-selection $\pi_{j\mid s}$ (carries through from B.4 / B.6) |

**Why the conjecture's $\min$ structure was wrong.** The conjecture imagined L1' as a single homogenized rate. In reality, L1' has *two parallel branches* with independent gating: the $C=1$ branch is gated by $\theta_C$, the $C=0$ branch by $(1-\theta_C)$. The bottleneck is the *worst* branch, not the *worst common factor*. So $\alpha_{L1'} = \min(\ldots, \theta_C \cdot \text{stuff}, (1-\theta_C) \cdot \text{stuff})$ rather than $\min(\theta_C, 1-\theta_C) \cdot \text{stuff}$.

**Why separability $s$ was absent in SUB-A.** When $C$ is observable, the agent never has to *infer* $C$-state from $y$. So the conditionals' separability is irrelevant to the update — each conditional branch is learned from its own dedicated subsample. Separability becomes binding only in SUB-B, where it appears as the magnitude of the Fisher null space (direction of unidentifiability).

**The corrected conjecture:**

$$\boxed{\alpha_{L1'}^{\text{obs-C}} = \min\!\left(\frac{1}{n_C+1},\; \min_j \frac{\theta_C \pi_{j\mid C}}{n_{j\mid C}+1},\; \min_j \frac{(1-\theta_C)\pi_{j\mid \neg C}}{n_{j\mid \neg C}+1}\right)}$$

This is a generalization of B.6's three-way gating (condition × evidence-starvation × exploration) to a *five-way gating* (condition × evidence-starvation × exploration on each of two conditional branches).

---

## §6. Global Sector Condition or Failure (Move 5)

### 6.1 SUB-A — Global

The SUB-A correction function is *exactly linear* in $\xi$ (the Beta-Bernoulli update with conditional test rates is linear, not merely first-order). The diagonal positive Jacobian computed in §4.2 is the exact $\mathbf J_F$ everywhere in $[-1, 1]^{2K+1}$. Therefore:

$$\xi^T F(\xi) = \xi^T \mathbf{J}_F \xi \geq \lambda_{\min}(\mathbf{J}_F) \lVert\xi\rVert^2 = \alpha_{L1'} \lVert\xi\rVert^2$$

holds **globally**, not just locally near truth. This matches the global scope of B.6 (the strict-prerequisite L1 case) — both rest on the same componentwise-linear Beta-Bernoulli structure, with L1' adding a parallel branch.

### 6.2 SUB-B — No Global Result Possible

Linearization gave $\lambda_{\min}(\mathbf J_F) = 0$. A correction function with a degenerate Jacobian at the equilibrium cannot satisfy $\xi^T F(\xi) \geq \alpha \lVert\xi\rVert^2$ for any $\alpha \gt 0$ in any neighborhood of the equilibrium (the inequality must hold pointwise; near $\xi = 0$ along the null direction of $\mathbf J_F$, both sides are quadratic in $\xi$ but the LHS is *higher*-order along the null while RHS is full quadratic). So no $\alpha_{L1'} \gt 0$ exists for SUB-B in the joint conditional vector.

**Possible weighted-norm Lyapunov.** One might try a weighted norm $V(\xi) = \tfrac{1}{2}\xi^T P \xi$ with $P$ chosen to align with the identifiable subspace. This works if we *project out* the null directions: $V_{\text{proj}}(\xi) := \tfrac{1}{2} \lVert \Pi_{\text{ident}} \xi\rVert^2$ where $\Pi_{\text{ident}}$ projects onto the rank-1 identifiable subspace. Then $V_{\text{proj}}$ tracks the marginal $\hat\mu_j$, which *is* identifiable and satisfies a B.1-style sector condition with $\alpha = 1/(n+1)$.

But this is essentially **plan-level tracking** (the L1' analog of B.3(b)): if you collapse the conditional decomposition and track only the marginal, you recover persistence — at the cost of losing the per-conditional diagnostics that L1' was constructed to preserve. This is a *known* fallback path; it does not strengthen L1' but rather demonstrates that the per-conditional decomposition under SUB-B carries no sector-condition guarantee beyond what L0 already provides.

### 6.3 SUB-B Multi-Channel — Conditional Global

When the joint Fisher matrix is full-rank (multi-child joint observation), the linearization Jacobian is positive-definite at truth with $\lambda_{\min} = \sigma_{\min}(\mathcal F_{\text{joint}})/\max_k(n_k+1)$. Local sector condition holds in a neighborhood; global extension would require uniform positivity of the Fisher matrix across the parameter region, which is not automatic for nonlinear models. This sub-case admits a *local* sector parameter; global verification is open.

---

## §7. Sub-Case Summary (Move 7)

| Sub-case | Identifiability | $\alpha_{L1'}$ | Region | Status |
|---|---|---|---|---|
| **B.5b-obs-C** ($C$ observable) | Yes (direct) | $\min\!\left(\frac{1}{n_C+1},\; \min_j \frac{\theta_C \pi_{j\mid C}}{n_{j\mid C}+1},\; \min_j \frac{(1-\theta_C)\pi_{j\mid \neg C}}{n_{j\mid \neg C}+1}\right)$ | Global | **Derived** |
| **B.5b-multi-channel** ($K \geq 2$ children, joint observation) | Yes (Fisher full-rank) | $\sigma_{\min}(\mathcal{F})/\max_k(n_k+1)$ | Local (truth neighborhood) | Sketch — applicability narrow |
| **B.5b-known-thetaC single channel** | No (Fisher rank 1) | — (no $\alpha \gt 0$ admissible) | — | **Refuted** |
| **B.5b general (single channel, joint Bayesian)** | No (Fisher rank 1) | — | — | **Refuted** (Cramér-Rao floor) |
| **B.5b plan-level fallback** ($V_{\text{proj}}$ on $\hat\mu$) | Yes (the marginal) | $1/(n_\mu+1)$ on plan-level scalar | Global | Equivalent to L0 on marginals — does *not* recover per-conditional diagnostics |

**The honest summary.** L1' admits a clean derived sector transfer **iff the common cause is directly observable** (B.5b-obs-C). When $C$ is unobservable and the agent has only single-channel observations, no SA1-preserving update can satisfy SA2' for the joint conditional vector — this is a Cramér-Rao bound, not a defect of any particular update rule. The multi-channel case is a partial repair requiring strong joint-observability assumptions; the plan-level fallback collapses L1' to L0-on-marginals.

**Action item from this:** the published `#worked-example-L1` already implicitly assumed observability of $C$ (it's described as a "condition leaf" — exactly the SUB-A regime). The L1 strict case (B.6) explicitly requires $C$ to be observable. **L1' for soft facilitators inherits the same observability requirement** — once recognized, B.6's three-way gating extends *naturally* to L1''s five-way gating, and the formal transfer goes through.

---

## §8. Strengthened Segment Text (Move 8)

### 8.1 Revised `#strategy-dag` Headline (Line 20)

**Current:**

> **Strategy-layer exactness contract.** All formal results in AAD's strategy layer ... are proved under **L0 (independence)** ... **L1 (augmented DAG with explicit common-cause nodes) is the practical default in complex domains** ... L0 formal results transfer exactly to correctly constructed L1 DAGs, because L1 restores causal sufficiency by construction.

**Proposed (replaces both the softening narrowing in `spike-finding-13-l1-default-narrowing.md` §2.1 and the original):**

> **Strategy-layer exactness contract.** All formal results in AAD's strategy layer — the sector condition transfer ( #strategic-dynamics-derivation, Prop B.5), the persistence schema ( #strategy-persistence-schema), the gradient-based credit assignment ( #credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L0 formal results transfer exactly to correctly constructed L1 DAGs (strict prerequisites, Prop B.6) and L1' DAGs (soft facilitators, Prop B.5b-obs-C) — provided the common cause is observable per trial.** When the common cause is unobservable, the per-conditional decomposition is *fundamentally* (not merely "openly") obstructed — the mixture parameters are non-identifiable from a single observation channel (Fisher rank deficiency, Prop B.5b refuted form), and the agent must either collect direct $C$-observations, run multi-child joint observations (Prop B.5b-multi-channel, sketch), or fall back to plan-level (L0-on-marginals) tracking. See the Correlation Hierarchy below.

### 8.2 New Prop B.5b for `#strategic-dynamics-derivation`

To be inserted after Prop B.5 (the credence-to-value bridge) or alongside Prop B.6 (the L1-strict case) in `#strategic-dynamics-derivation`. Full text (proof-ready):

---

#### Proposition B.5b: L1' Mixture-Form Sector Transfer (Observable Common Cause)

**Setup.** L1' (mixture-form) DAG with binary common cause $C$, true prior $\theta_C \in (0,1)$, gating a sub-plan with conditional structures $G_{\mid C}$ (when $C=1$) and $G_{\mid \neg C}$ (when $C=0$). Each affected child $j$ carries two conditional credences $\hat p_{j\mid C}$ and $\hat p_{j\mid \neg C}$. Plan confidence:

$$\hat P_\Sigma^{L1'} = \hat\theta_C \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid C}) + (1-\hat\theta_C) \cdot P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C})$$

The agent observes $C$-state directly each trial (i.e., $C$ is treated as an observable condition leaf, in parallel with B.6). Per trial, the agent (i) updates $\hat\theta_C$ from observed $C$ via Beta-Bernoulli; (ii) on $C=1$ trials, attempts a child $j$ via the active selection policy $\pi_{\mid C}$ and updates $\hat p_{j\mid C}$ from $y_j$; (iii) on $C=0$ trials, attempts a child $j$ via $\pi_{\mid \neg C}$ and updates $\hat p_{j\mid \neg C}$ from $y_j$.

**Statement.** Under Beta-Bernoulli updating with observable common cause, componentwise updates per conditional branch, and *facilitator monotonicity* ($P_\Sigma(G_{\mid C}) \geq P_\Sigma(G_{\mid \neg C})$), the expected correction function on the joint state $(\hat\theta_C, \{\hat p_{j\mid C}\}, \{\hat p_{j\mid \neg C}\})$ satisfies the sector condition globally with:

*[Derived (Conditional on Beta-Bernoulli model, observable common cause, facilitator monotonicity)]*

$$\alpha_{L1'} = \min\!\left(\frac{1}{n_C+1},\; \min_{j \in \mathcal{J}_C}\frac{\theta_C \pi_{j\mid C}}{n_{j\mid C}+1},\; \min_{j \in \mathcal{J}_{\neg C}}\frac{(1-\theta_C)\pi_{j\mid \neg C}}{n_{j\mid \neg C}+1}\right)$$

where $\mathcal J_s$ is the set of children tested on the $C=s$ branch and $\pi_{j\mid s}$ is the action-selection probability for child $j$ on that branch.

**Proof.**

*Edge $C$ (condition leaf, observable every trial).* Standard Beta-Bernoulli on direct $C$-observation:

$$\mathbb{E}[\Delta\hat\theta_C] = \frac{\theta_C - \hat\theta_C}{n_C+1} = -\frac{\xi_C}{n_C+1}$$

so $F_C(\xi) = \xi_C/(n_C+1)$.

*Edge $p_{j\mid C}$ (conditional credence, $C=1$ branch).* Tested when $C=1$ (probability $\theta_C$) and the agent's $C=1$-conditional policy selects $j$ (probability $\pi_{j\mid C}$):

$$\mathbb{E}[\Delta\hat p_{j\mid C}] = \theta_C \pi_{j\mid C} \cdot \frac{\theta_{j\mid C} - \hat p_{j\mid C}}{n_{j\mid C}+1} = -\frac{\theta_C \pi_{j\mid C} \xi_{j\mid C}}{n_{j\mid C}+1}$$

so $F_{j\mid C}(\xi) = \theta_C \pi_{j\mid C} \xi_{j\mid C}/(n_{j\mid C}+1)$.

*Edge $p_{j\mid \neg C}$ (conditional credence, $C=0$ branch).* Symmetric: tested with probability $(1-\theta_C)\pi_{j\mid \neg C}$:

$$F_{j\mid \neg C}(\xi) = \frac{(1-\theta_C)\pi_{j\mid \neg C} \xi_{j\mid \neg C}}{n_{j\mid \neg C}+1}$$

*Sector product.* The correction function is diagonal in $\xi$ with positive entries:

$$\xi^T F(\xi) = \frac{\xi_C^2}{n_C+1} + \sum_{j \in \mathcal{J}_C}\frac{\theta_C \pi_{j\mid C} \xi_{j\mid C}^2}{n_{j\mid C}+1} + \sum_{j \in \mathcal{J}_{\neg C}}\frac{(1-\theta_C)\pi_{j\mid \neg C} \xi_{j\mid \neg C}^2}{n_{j\mid \neg C}+1}$$

$$\geq \alpha_{L1'} \cdot \lVert\xi\rVert^2$$

with $\alpha_{L1'}$ as stated.

*SA1 check.* $F(0) = 0$ at truth ($\xi = 0$). ✓

*Globality.* The Beta-Bernoulli updates are linear in $\xi$ on $[-1, 1]^{2K+1}$, so the diagonal Jacobian computed at truth is the exact $\mathbf J_F$ throughout. The sector inequality holds globally with the same $\alpha_{L1'}$.

*B.5b bridge to plan value.* Jacobian of $\hat P_\Sigma^{L1'}$ with respect to the joint state:

$$\mathbf{J}_{P_\Sigma} = \begin{pmatrix} P_\Sigma(\hat{\mathbf{p}}_{\mid C}) - P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C}) \\ \hat\theta_C \cdot \nabla_{\hat{\mathbf{p}}_{\mid C}} P_\Sigma(\hat{\mathbf{p}}_{\mid C}) \\ (1-\hat\theta_C) \cdot \nabla_{\hat{\mathbf{p}}_{\mid \neg C}} P_\Sigma(\hat{\mathbf{p}}_{\mid \neg C}) \end{pmatrix}$$

By facilitator monotonicity, the first entry is $\geq 0$. The other entries are $\geq 0$ by AND/OR monotonicity on each conditional sub-DAG. So $\mathbf J_{P_\Sigma} \geq 0$ componentwise. By the componentwise nonlinear case of Prop B.5b, the sector condition transfers losslessly:

$$\alpha_s = \alpha_c = \alpha_{L1'} \qquad \square$$

**Five-way gating.** This generalizes B.6's three-way gating to five gating mechanisms, one per term in the $\min$:

1. **Condition testing** ($1/(n_C+1)$): the common cause is the easiest component to calibrate — directly observed every trial.
2. **Evidence starvation, $C=1$ branch** ($\theta_C$ factor): conditional edges on the $C=1$ branch are gated by the prior frequency of $C=1$.
3. **Exploration gating, $C=1$ branch** ($\pi_{j\mid C}$ factor): OR-alternatives within the $C=1$ branch compete for test opportunities.
4. **Evidence starvation, $C=0$ branch** ($1-\theta_C$ factor): conditional edges on the $C=0$ branch are gated by the prior frequency of $C=0$.
5. **Exploration gating, $C=0$ branch** ($\pi_{j\mid \neg C}$ factor): OR-alternatives within the $C=0$ branch.

The bottleneck is typically whichever of $\theta_C$ and $1-\theta_C$ is smaller (the rare branch sees fewer trials), modulated by exploration on that branch.

**Reduction to B.6 (strict prerequisite limit).** Setting $\theta_{j\mid \neg C} \to 0$ collapses the $\neg C$ branch (the agent learns the $\neg C$ conditionals are zero with no remaining variance). The per-edge state for the $\neg C$ branch drops out of the sector inequality, and the formula reduces to B.6's three-way gating with $\alpha_\Sigma = \min(1/(n_C+1), \theta_C(1-\varepsilon)/(n_{A_1}+1), \theta_C\varepsilon/(n_{A_2}+1))$. ✓

**Refuted under unobservable $C$.** When $C$ is not observable, the agent can only update the joint state via online soft EM on the marginal $y_j$. The Fisher information of the mixture model evaluated at truth is **rank 1** (not rank $2K+1$): $\mathcal{F} = u u^T / (\mu\bar\mu)$ with $u = (\Delta, \theta_C, 1-\theta_C)$ and $\Delta = p_{\mid C} - p_{\mid \neg C}$ the separability gap. The two-dimensional null space corresponds to indeterminacy directions in the conditional decomposition. By the Cramér-Rao bound, no SA1-preserving update on the joint conditional vector admits a sector parameter $\alpha \gt 0$. The agent must either:

(i) Augment $C$-observability (B.5b-obs-C above);
(ii) Run $K \geq 2$ children jointly under the same $C$-realization (B.5b-multi-channel sketch — sufficient when joint Fisher reaches rank $2K+1$);
(iii) Fall back to plan-level tracking on the marginal $\hat\mu_j$ (recovering B.1's $\alpha = 1/(n_\mu+1)$ but losing the per-conditional decomposition — equivalent to L0-on-marginals).

This refutation closes the "L1' formal transfer is open" item in `#strategic-dynamics-derivation` Epistemic Status: the *cleanly-derivable* sub-case is B.5b-obs-C; the *general* sub-case is fundamentally obstructed by mixture identifiability, not merely under-derived.

---

### 8.3 Updated Correlation Hierarchy Table for `#strategy-dag`

(Replaces the proposed table from `spike-finding-13-l1-default-narrowing.md` §2.3 — the L1' row gains a derived sector parameter and an explicit observability requirement.)

| Level | Model | When correct | $\hat P_\Sigma$ status | Sector transfer status | Computation |
|---|---|---|---|---|---|
| **L0: Independence** | AND/OR propagation as-is | Causally sufficient DAG (all common causes explicit) | Correct probability | Prop B.5 (linear), B.5b (componentwise nonlinear): $\alpha_s = \alpha_c$ | $O(\lvert V\rvert + \lvert E\rvert)$ |
| **L1: Augmented DAG (strict prerequisites)** | Strict-prerequisite common-cause nodes added explicitly; AND/OR propagation on augmented graph | Augmented DAG is causally sufficient *and* every modeled common cause has $\theta_{\text{child} \mid \neg C} \approx 0$ | Correct for augmented graph | Prop B.6: $\alpha_\Sigma = \min(1/(n_C+1), \theta_C\pi_j/(n_j+1))$ — three-way gating | $O(\lvert V'\rvert + \lvert E'\rvert)$, larger graph |
| **L1': Mixture form (soft facilitators)** | Conditional sub-DAGs weighted by common-cause state: $\hat P_\Sigma = \theta_C P_\Sigma(G\mid C) + (1-\theta_C) P_\Sigma(G\mid\neg C)$ | Soft-facilitator common causes ($\theta_{\text{child}\mid\neg C} \gt 0$) **with $C$ observable per trial** | Correct for the weighted combination | Prop B.5b-obs-C: $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$ — five-way gating. **Refuted when $C$ unobservable** (Fisher rank-1; falls back to plan-level tracking or multi-child joint observation) | $O(\lvert V'\rvert + \lvert E'\rvert)$ per common cause; doubles parametric footprint for affected edges |
| **L2: Full correlation** | Arbitrary joint failure distribution over edges | Always (but requires specifying the full joint) | Correct | Reduces to L0 on the augmented joint state | Exponential in general |

**Scope sub-bullet** (after the table):

> *[Discussion (regime classification)]* **Choosing among L1, L1', and L2 requires classifying each common cause and verifying observability.** $\theta_{\text{child}\mid\neg C} \approx 0$ → L1 (factor above the correlation, B.6). $\theta_{\text{child}\mid\neg C} \gt 0$ with **$C$ observable** → L1' (B.5b-obs-C). $\theta_{\text{child}\mid\neg C} \gt 0$ with $C$ unobservable → L1' is identifiability-obstructed; either augment $C$-observability (preferred), use L2 explicit conditioning, or fall back to L0-on-marginals (losing per-conditional diagnostics). Mixed-classification environments (some strict, some soft, varying observability) combine L1 and L1' on observable-$C$ branches and accept L0 bias elsewhere. Treating L1 as the universal default (regardless of strict vs soft classification or observability) systematically *understates* success on soft-facilitator branches.

### 8.4 Updates to Cross-Segments (Latent Items, Not Blocking)

The B.5b-obs-C result also enables tightening parentheticals in:

- `#strategy-persistence-schema` (line 66): the L1 inheritance now explicitly extends to L1'-obs-C with the same template.
- `#worked-example-L1` (lines 130-134): the "open" qualifier on L1' transfer should be replaced with "derived under observable $C$ via B.5b-obs-C; refuted under unobservable $C$."
- `#strategic-dynamics-derivation` (line 513): the "L1/L2 scope" item moves from "Partially resolved" to "Resolved (B.6 for L1-strict, B.5b-obs-C for L1'-observable; refuted under unobservable $C$ — augmentation required)."
- `#causal-insufficiency-detection` (Step 3a insertion): "Classify $C$ as strict or soft. If strict, factor above (→ L1, B.6). If soft and $C$ observable, build mixture form (→ L1', B.5b-obs-C). If soft and $C$ unobservable, augment observability or fall back to L0-on-marginals."
- `#independence-audit` (line 47): "L1 augmentation (strict prerequisites, observable $C$) or L1' mixture form (soft facilitators, observable $C$); when $C$ unobservable, augment or fall back."

These are not blocking; they queue for the next promotion of each segment.

---

## §9. Comparison to the Softening Repair

The softening repair (`spike-finding-13-l1-default-narrowing.md`) narrowed `#strategy-dag`'s headline to scope L0→L1 transfer to strict prerequisites and tagged L1' transfer as "open." The strengthening attempt produces a different and stronger outcome:

| Aspect | Softening repair | Strengthening attempt |
|---|---|---|
| **L1' transfer status** | "Open" | **Derived (B.5b-obs-C)** with explicit $\alpha_{L1'}$ formula, *iff* $C$ observable. **Refuted (Cramér-Rao floor)** when $C$ unobservable |
| **Headline scope** | L1 strict only; L1' "open"; L2 fallback | L1 strict (B.6) + L1' observable-$C$ (B.5b-obs-C); L1' unobservable-$C$ requires augmentation; L2 fallback for arbitrary joint |
| **Correlation Hierarchy table** | L1' as fourth row, sector status "open" | L1' as fourth row, sector status **Derived** with formula; observability requirement explicit |
| **What the reader learns** | "L1' is a valid regime but the formal machinery isn't there yet" | "L1' is a fully formal regime when $C$ is observable; the open question collapses into a *modeling decision* (do we observe $C$?), not a theoretical gap" |
| **Action items for downstream segments** | Five clarifying parentheticals at next promotion | Same five parentheticals, but each substantively *strengthens* (replaces "open" with "derived under $C$-observability")  |
| **Scope of `#strategy-persistence-schema`** | L1 inheritance only | L1 + L1'-obs-C inheritance; the experience-discounting prerequisite extends naturally |
| **L0 transfer status** | Unchanged (B.5/B.5b for L0) | Unchanged (B.5/B.5b for L0) |
| **L2 status** | Unchanged | Unchanged |
| **Risk of misuse** | A reader who takes "L1 by default" at face value still applies L1 incorrectly to soft facilitators | Same risk if reader doesn't notice the observability requirement; mitigated by explicit table column "Sector transfer status" |

**What the strengthening adds beyond the softening:**

1. **A real, derived sector parameter for L1'** — the five-way-gating formula $\alpha_{L1'}^{\text{obs-C}}$. This gives concrete persistence thresholds for soft-facilitator strategies.
2. **A principled refutation** of the unobservable-$C$ case — not "open," but **structurally obstructed by mixture identifiability.** This is information the softening did not have.
3. **A clear modeling decision tree** for practitioners: classify the common cause as strict/soft, then check $C$-observability, then choose L1 / L1'-obs-C / multi-child / L0-fallback.
4. **Reduced theoretical debt** — `#strategic-dynamics-derivation` Item 4 in the open list ("Correlated edges (L1/L2 scope) — Partially resolved") moves to fully resolved.

**What the strengthening does *not* change relative to softening:**

- The Correlation Hierarchy still reads with L0/L1/L1'/L2 as four rows.
- The headline contract still names strict-vs-soft classification.
- The `#worked-example-L1` segment text is largely unchanged (it already implicitly assumed observable $C$; the strengthening makes that explicit and confers full sector verification on L1').
- The misclassification failure mode is still named (treating soft as strict undervalues sub-plans).

**Recommendation.** Adopt the strengthening repair (this spike) in place of the softening repair. The softening text was *correct* but conservative — it tagged a derivable result as "open." The strengthening makes the soft-facilitator regime first-class while exposing a genuine theoretical fact (the unobservable-$C$ obstruction) that helps practitioners route their modeling decisions.

---

## §10. Open Questions for Joseph

1. **Observability classification.** B.5b-obs-C requires *direct* $C$-observation per trial. In TST domains (CI signals, infrastructure status, organizational state), $C$ is often inferred from secondary signals with some noise. Does the proposition extend to *partial* observability via the identifiability coefficient $\iota_C$ (cf. `#edge-update-causal-validity`)? My read: yes, with $\alpha_{L1'} \to \iota_C \cdot \alpha_{L1'}$ on the $C$-term and a corresponding tightening on the conditional terms (the soft-routing of evidence under partial $C$-observation interpolates between SUB-A and SUB-B). Worth a dedicated extension or a mention in B.5b's discussion?

2. **Multi-child observability requirement.** B.5b-multi-channel as sketched requires *joint* observation of $K \geq 2$ children under the *same* $C$-realization. This is a stronger structural requirement than typical strategy execution permits (the agent attempts one path at a time). Is there value in formalizing this sub-case despite its narrow applicability, or should we leave it as a sketch and emphasize the observable-$C$ path as the practical recommendation?

3. **Facilitator monotonicity scope.** B.5b-obs-C requires $P_\Sigma(G_{\mid C}) \geq P_\Sigma(G_{\mid \neg C})$ for the Jacobian transfer. This is the *defining property of a facilitator* (it helps), but for the rare case of an *anti-facilitator* (a condition that makes the sub-plan harder when present), the Jacobian sign on the $\hat\theta_C$ component flips. Should B.5b-obs-C state this explicitly as a scope condition, or treat anti-facilitators as a separate regime?

4. **Region of validity.** B.5b-obs-C's globality is on $[-1, 1]^{2K+1}$ — the full Beta-Bernoulli parameter region. The conjugate update is well-defined globally there. But the *facilitator monotonicity* condition $P_\Sigma(G_{\mid C}) \geq P_\Sigma(G_{\mid \neg C})$ is on the agent's *current beliefs*; if a perturbation pushes $\hat{\mathbf{p}}$ into a region where this flips, the Jacobian transfer (B.5b componentwise) loses the non-negativity. In practice this is unlikely (the agent's beliefs evolve smoothly under Beta-Bernoulli), but the global claim has a small caveat. Worth flagging?

5. **The plan-level fallback under SUB-B.** §6.2 noted that projecting onto the identifiable subspace recovers a B.1-style sector condition for $\hat\mu_j$ — but at this point you are tracking *only* the marginal, equivalent to L0. Should this be promoted to a named "L1'-fallback" sub-case in the Correlation Hierarchy, or is it sufficiently obvious from the table that "if you can't identify the conditionals, you're effectively at L0"?

6. **Naming.** "B.5b-obs-C" is a working label. Cleaner alternatives:
   - **B.7** (if it gets a new proposition slot in `#strategic-dynamics-derivation`, parallel to B.6 for L1-strict)
   - **B.6'** (emphasizing the parallel to B.6 with the soft-facilitator extension)
   - **B.5b-L1'** (emphasizing it's the L1' instantiation of B.5b's componentwise case)

   My recommendation: **B.7** — it deserves first-class status alongside B.6 because the five-way-gating structure is qualitatively new (extending three-way to five-way), not just a reapplication of B.5b's machinery. The B.5b segment in `#strategic-dynamics-derivation` already covers the L0/L1-componentwise transfer; B.7 would be the L1' extension. Confirm preference.

7. **Promotion to segment.** Should this spike's B.5b-obs-C result land in `#strategic-dynamics-derivation` (as Prop B.7 / B.5b-obs-C) and propagate to `#strategy-dag`'s Correlation Hierarchy table immediately, or queue behind other Phase-1 batch items? My read: this is a substantive strengthening (turns "open" into "derived" for the soft-facilitator regime, the *practically dominant* common-cause pattern), worth promoting in the same batch as the softening repair would have been.

8. **Refutation visibility.** The unobservable-$C$ case is now *refuted* (Cramér-Rao bound), not "open." Where should this be stated? Options:
   - In `#strategic-dynamics-derivation` Prop B.5b's Epistemic Status (alongside the derivation of B.5b-obs-C).
   - In `#strategy-dag`'s Correlation Hierarchy discussion as a named identifiability-obstruction caveat.
   - In `#worked-example-L1` §"When Correct L1 Construction Is Not Possible" as the "semantic failure mode under unobservable $C$."

   My read: all three, with cross-references. The refutation is structural enough to deserve named visibility — it's not a minor caveat but a fundamental scope statement on what L1' can and cannot deliver.

---

## §11. Effort and Confidence

**Effort delivered:** ~3 hours of focused derivation + writeup.

**Confidence:**
- **B.5b-obs-C derivation:** High. The algebra is direct extension of B.6's machinery to a parallel branch. SA1 verification at truth is explicit. Globality follows from the linear Beta-Bernoulli structure.
- **Refutation of unobservable-$C$ case:** High. The Fisher matrix factorization $\mathcal{F} = u u^T/(\mu\bar\mu)$ is direct algebra; the rank-1 structure is a reflection of the binary observation channel's intrinsic information capacity (one bit per trial). The Cramér-Rao bound is a textbook lower bound on any unbiased estimator's variance.
- **Multi-channel sketch:** Medium. The full-rank condition is correctly identified, but the practical applicability (joint multi-child observation under same $C$-realization) is restrictive and not fully worked through.
- **Facilitator monotonicity scope condition:** High. Direct from the Jacobian computation.

**Not in scope.**
- Continuous outcomes for the mixture (analogous to remaining open item #2 in `#strategic-dynamics-derivation`).
- Adaptive exploration policies for L1' (analogous to remaining open item #5).
- Formal connection to the `architectural-proposals-2026-04-22.md` G-BP1 (natural-parameter reparameterization) — natural-parameter form may simplify L1''s mixture analysis but is a separate move.
- Formal SOC/RG framing (architectural-proposals-2026-04-22 — separate move).

**Risk.** The B.5b-obs-C result rests on the assumption that the agent can route per-trial evidence to the correct conditional branch via $C$-observation. In practice, $C$-observation is *rarely* perfect — there is observation noise on $C$, partial observability, time-lag in $C$-detection, etc. The proposition as stated handles only the perfect-observability case; partial-observability extension via $\iota_C$ (Open Question 1) is a natural follow-on but unverified.

**Recommendation.** Adopt the strengthening repair as the next-promotion content for `#strategy-dag` and `#strategic-dynamics-derivation`, with the softening repair retired (its content is subsumed and extended). Open questions 1–8 collected as latent items for Joseph's review before the segment-edit pass.
