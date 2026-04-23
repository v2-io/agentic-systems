---
slug: l1-update-bias
type: derivation
status: conditional
depends:
  - credit-assignment-boundary
  - edge-update-natural-parameter
  - strategic-dynamics-derivation
  - discussion-identifiability-floor
  - strategy-persistence-schema
stage: draft
---

# Derivation: L1' Update-Bias Formula

Under L1' correlated-evidence regimes with unobservable common cause, the default log-odds edge-update ( #edge-update-natural-parameter) converges to a **biased fixed point** — edges settle at log-odds values that match the L1' root-probability rather than the marginal-edge truth. This segment derives a closed-form bias formula for the two-edge OR-root case, verifies it via Monte Carlo, and composes it with `#discussion-identifiability-floor` Instance 2 and `#strategy-persistence-schema`'s forgetting prerequisite to produce a **dual forgetting-rate requirement** on strategic persistence.

The bias is the quantitative companion to F13's structural-identifiability-floor result: F13 shows identification is *structurally impossible* from single-channel observation; this segment shows the resulting *magnitude drift* is bounded, Lipschitz in correlation strength $\rho$, and Cramér-Rao-floored under forgetting.

## Formal Expression

### Closed-form bias at matched-marginal initial conditions (two-edge OR-root)

*[Derived (L1-bias-formula-OR-root)]*

Let root node $G$ have two direct causal parents $e_1, e_2$ via OR-aggregation under L1' with latent common cause $C$ producing correlation $\rho$ between the parent edges. Assume matched-marginal initial conditions: $\hat\mu_j^{\text{init}} = \mu_j^\ast$ for each edge's marginal probability. Under the default log-odds update with per-edge gain $\eta_{\text{edge}} = 1/(n_k+1)$ and identifiability coefficient $\iota_k$, the per-cycle bias on edge $k$'s log-odds update satisfies

$$B_k(\rho) = -\frac{\iota_k \cdot (1 - \mu_{\bar k}) \cdot \rho}{(n_k + 1) \cdot \left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]}$$

where $\bar k \in \{1, 2\} \setminus \{k\}$ is the sibling edge. The bias is linear in $\rho$, decays as $1/(n_k+1)$ with experience, topologically asymmetric via the Jacobian factor $(1 - \mu_{\bar k})/\lVert\mathbf J\rVert^2$.

For AND-root aggregation, the bias has the same structural form with opposite sign. For mixed OR-AND sub-plans, the bias decomposes sub-plan-wise.

### L1'-induced biased fixed point

*[Derived (biased-fixed-point-exists)]*

Under continued L1' evidence, the log-odds fixed point satisfies

$$\lambda_k^{\text{L1'-FP}} = \lambda_k^\ast + \int_0^\infty e^{-\eta_{\text{edge}} \iota_k t} B_k(\rho)\, dt = \lambda_k^\ast - \rho \cdot (1 - \mu_{\bar k})/\left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]$$

(for constant-$\iota$ approximation). Each edge's log-odds converges to a **wrong value** that matches the L1' root probability rather than the marginal truth. **Plan-level correctness is purchased at edge-level miscalibration**: the agent predicts plan outcomes correctly on-policy (the L1' mixture on the sibling matches the L1' marginal), but its per-edge credences are systematically biased.

This is the quantitative companion to F1's on-policy undetectability (`#discussion-identifiability-floor` Instance 1) at the marginal level: the bias accumulates at rate $1/(n_k+1)$, converges to a bounded non-zero value, and is *not detectable from on-policy data* because the mixture's marginal is matched to the on-policy observations.

### Observable-$C$ zero-bias result

*[Derived (observable-C-zero-bias)]*

Under Prop B.7's five-way-gating with $C$ observable, conditioning on $C$ decomposes the L1' mixture into two single-child-per-component problems:

$$B_k(\rho \mid C = c) = 0 \quad \text{in expectation at conditional truth, for each } c \in \{0, 1\}.$$

Prop B.7's decomposition *exactly eliminates the bias* — the five gating conditions (facilitator monotonicity; $C$-observability; $\iota > 0$ for common-cause edge; marginal sector condition; identifiability of per-component rates) are precisely the conditions under which conditional-on-$C$ updates restore exactness. This makes Prop B.7's derivation the quantitative escape from the L1' bias.

### Unobservable-$C$ Cramér-Rao bias floor under forgetting

*[Derived (bias-floor-under-forgetting)]*

When $C$ is unobservable and the agent uses experience discounting at rate $\lambda \in [0, 1)$ to maintain plasticity (`#strategy-persistence-schema`'s forgetting prerequisite), the steady-state bias is

$$B_k^{\text{SS}}(\rho, \lambda) = -\frac{\iota_k \cdot \rho \cdot (1 - \mu_{\bar k})}{(1 - \lambda) \cdot \left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]}.$$

The Cramér-Rao floor from `#discussion-identifiability-floor` Instance 2's rank-1 Fisher matrix translates directly: no unbiased estimator can reduce the bias below $\rho / (1 - \lambda) \cdot [\text{constant}]$. The bias is structurally present in any online estimator operating on single-channel observation of one child edge, not merely the specific default-signal estimator.

### Dual forgetting-rate requirement

*[Derived (dual-forgetting-requirement)]*

`#strategy-persistence-schema` requires forgetting rate $(1 - \lambda) > \rho_\Sigma / R_\Sigma$ for asymptotic sector-persistence. The L1' bias floor above imposes a **second** constraint: to keep the bias bounded relative to the sector reserve,

$$(1 - \lambda) > c_B \cdot \rho / R_\Sigma^{\text{bias}}$$

where $c_B$ is a topology-dependent constant from the Jacobian factor and $R_\Sigma^{\text{bias}}$ is the tolerable bias-reserve within the sector region. The forgetting rate must satisfy **both**:

$$(1 - \lambda) > \max\left(\frac{\rho_\Sigma}{R_\Sigma},\; \frac{c_B \cdot \rho}{R_\Sigma^{\text{bias}}}\right).$$

**When the admissibility window is empty** (no forgetting rate satisfies both constraints simultaneously), no standard persistence regime works — the agent must augment (observable-$C$ via instrumented regime indicators; multi-child joint observation; plan-level fallback) or accept biased-fixed-point operation.

### Monte Carlo verification

*[Empirical claim (monte-carlo-confirmation)]*

Numerical simulation (400 trials × 5000 cycles, four scenarios: OR-cooperative, OR-adversarial, AND-cooperative, AND-adversarial) confirms the closed-form predictions:
- Sign of bias matches theoretical prediction in all scenarios.
- Magnitude matches closed form within $< 5\%$ at $\rho \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
- Vanishing at $\rho = 0$ verified.
- Jacobian-induced topological asymmetry verified: OR and AND roots produce opposite-sign biases of matching magnitude.
- Initial-cycle rate $dB_k/dt \mid_{t=0}$ matches closed form quantitatively.
- Logarithmic cumulative drift matches (biased-fixed-point convergence rate).

Full simulation parameters and results in `msc/spike-l1-update-bias.md` §7.

## Epistemic Status

*Conditional.* Max attainable: *exact* for the two-edge OR-root / AND-root matched-marginal case. The closed-form bias formula is derived via first-order perturbation of the log-odds update around matched-marginal truth; the Jacobian factor is specific to the DAG topology (OR vs AND vs mixed). *Robust qualitative* for deeper DAG structures where the bias Decompose sub-plan-wise but closed-form coefficients depend on per-sub-plan Jacobians.

**What is load-bearing:**
- The linear-in-$\rho$ scaling is exact (first-order in small correlation).
- The $1/(n_k+1)$ experience scaling is exact (follows from `#edge-update-natural-parameter`'s Beta-Bernoulli gain).
- The observable-$C$ zero-bias result under Prop B.7 gating is exact.
- The dual forgetting-rate requirement is a first-order composition of two separate constraints.

**What is not established:**
- Closed-form bias for non-matched-marginal initial conditions (transient bias during convergence). Numerical simulation works; analytic form is messier.
- Higher-than-second-order DAG structures (L2-general). Scope boundary.
- Full coupled bias formula under `#adaptive-gain-dynamics` meta-gain machinery. Open.

## Discussion

**Composition with `#discussion-identifiability-floor` Instance 2.** F13 establishes the structural no-go for single-channel L1' mixture identification (Cramér-Rao rank-1); this segment gives the **quantitative numerical-floor** companion — the bias is bounded, continuous in $\rho$, and vanishes at $\rho = 0$. Instance 2 answers "is it identifiable?" (no, structurally); this segment answers "if we update anyway, how wrong is the result?" (bounded drift to a biased fixed point).

**Composition with `#fisher-whitened-update-rule`.** The Fisher-whitened update recovers sharp *directional* fidelity but does not reduce the *magnitude* bias — Fisher whitening operates downstream of identification, and Instance 2's obstruction is an identification obstruction. The full picture for the default signal function under L1': **direction preserved (angle ≤ 45° per `#fisher-whitened-update-rule`)**, **magnitude biased by $B_k(\rho)$ with Cramér-Rao floor under forgetting (this segment)**, **observable-$C$ restores exactness (Prop B.7)**, **undetectable on-policy (Instance 1 + Instance 2 composition)**. This is the honest quantitative account of what the default signal function does under Gemini's Gap A (validation under correlated failures).

**Relationship to `#strategy-persistence-schema`'s forgetting.** The segment's existing forgetting prerequisite (for asymptotic sector-persistence) becomes dual under L1': forgetting must *both* outpace sector disturbance *and* prevent bias accumulation. When the two constraints are compatible (admissibility window non-empty), the existing forgetting-rate requirement suffices with appropriate $\rho$-dependent tuning. When incompatible, augmentation is required — a structural scope narrowing that elevates observable-$C$ instrumentation from convenience to prerequisite.

**Connection to `#stability-induced-myopia`'s detection-latency.** The detection-latency theorem ($\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$) assumes unbiased marginal tracking; under L1' bias, the pre-accumulated drift degrades effective $\varepsilon$ for subsequent regime-change detection. High-operating-point agents with pre-accumulated L1' bias face a compounded myopia floor. Follow-on refinement possible in `#stability-induced-myopia`.

## Working Notes

- Landing context: `msc/spike-l1-update-bias.md` (2026-04-23 Gap A/B cycle). Closed-form derivation + Monte Carlo verification in the spike.
- **Open: non-matched-marginal transient bias.** Closed-form for arbitrary initial conditions is messier but numerically tractable. A tighter analytic treatment would compose `#edge-update-natural-parameter`'s $\beta$-Bernoulli dynamics with the L1' mixture and likely requires Markov-chain convergence-rate analysis.
- **Open: $N$-edge common-cause extensions.** Three or more children of a single common cause produce a tensor of Jacobian factors. The structural scaling likely remains $O(\rho)$ per edge, but the exact coefficients need working out.
