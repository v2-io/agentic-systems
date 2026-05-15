---
slug: result-unity-closure-mapping
type: result
status: conditional
depends:
  - def-unity-dimensions
  - form-composition-closure
  - form-information-bottleneck
stage: draft
---

# Result: Unity-to-Closure Rate-Distortion Mapping

Unity dimensions parametrize rate-distortion curves for closure-defect components, not point-valued predictors. The achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in both the relevant content unity $U_d$ and the structural unity $U_f$ (update-rule homogeneity), with higher unity along either axis lowering achievable defect at a given compression. Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly. The two-axis structure (content $\times$ structure) is forced by the heterogeneous-Kalman case below and is reflected definitionally in #def-unity-dimensions.

## Formal Expression

### Rate-distortion framing (general)

*[Formulation (unity-rate-distortion)]*

Fix a composite agent satisfying the admissibility conditions (A1)-(A4) in #form-composition-closure. For each content unity dimension $U_d$ (with $d \in \{M, \Sigma, \text{obs}\}$, and $U_O$ contributing jointly with $U_\Sigma$ — see below) and the structural unity $U_f$ (update-rule homogeneity, defined in #def-unity-dimensions), the achievable component closure defect under a projection whose corresponding macro-dimension is $k_d$ satisfies:

$$\varepsilon_d^{\min}(k_d) = f_d\big(k_d;\; U_d,\; U_f\big)$$

where $f_d$ is monotone decreasing in both unity arguments, monotone increasing in aggressiveness of compression (smaller $k_d$). The mapping from unity to closure-defect *magnitude* is via the shape of this rate-distortion surface; unity does not directly predict closure-defect value. In the linear-Gaussian Kalman case the structural argument reduces to $1 - U_f \propto \lvert\Delta K\rvert / K_{\max}$ on the gain mismatch.

### Linear-Gaussian closed forms (two-agent scalar case)

*[Derived (obs-closure-linear-Gaussian, from unity-dimensions, composition-closure)]*

For two agents with scalar observations correlated at $\rho_{o,\text{eff}}$ (combining $\rho_{\text{env}}$ and $\rho_{\text{obs}}$), under 1D principal-component projection of observations, the minimum achievable observation closure defect is:

$$\varepsilon_o^2(k_o=1) = \sigma_o^2 \cdot \frac{1 - \rho_{o,\text{eff}}}{2} \;\propto\; 1 - U_{\text{obs}}$$

Higher perceptual unity → observations are more redundant → 1D summary suffices → $\varepsilon_o$ small. Exact in the linear-Gaussian scalar case.

*[Derived (action-closure-independent-policies, from unity-dimensions, composition-closure)]*

For two agents with scalar quadratic objectives, independent LQR policies ($\rho_\Sigma = 0$), scalar targets $r_1, r_2$ with correlation $\rho_O$, under 1D state projection, the minimum achievable action closure defect is:

$$\varepsilon_a^2 \propto \kappa^2 \cdot (1 - \rho_O) \;\propto\; \kappa^2 \cdot (1 - U_O)$$

where $\kappa$ is the scalar LQR gain. Adding policy coordination ($\rho_\Sigma \gt 0$) further reduces $\varepsilon_a$ through a multiplicative factor. The joint $(U_O, U_\Sigma)$ dependence takes the form:

$$\varepsilon_a^2 \propto (1 - U_O) \cdot f_1(U_\Sigma) + g(U_\Sigma)$$

with $f_1$ decreasing in $U_\Sigma$ and $g$ capturing residual strategic-misalignment error even when targets coincide.

### State closure in linear-Gaussian

*[Derived (state-closure-linear-Gaussian-trivial, from composition-closure)]*

For linear-Gaussian micro-dynamics with consistent linear projections $\Lambda_x$ and $\Lambda_o$ (the macro observation projection is the same linear combination as the macro state projection), the state closure defect vanishes:

$$\varepsilon_x = 0$$

regardless of $U_M$ or compression dimension. Linear projections of linear dynamics are exact *when the range of $\Lambda_x$ is invariant under the micro-dynamics matrix*. $\varepsilon_x$ becomes non-trivial when:

- the projection's range is non-invariant under the dynamics matrix — even with linear dynamics, consistent projections, and homogeneous updates, cross-coordinate coupling or anisotropic noise scales that mix macro-subspace components with their orthogonal complement give $\varepsilon_x \gt 0$ (the Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ in #form-composition-closure is the general expression of this obstruction),
- the projection is inconsistent (macro state and macro observation projections disagree),
- the micro-dynamics are nonlinear, or
- sub-agent update rules are heterogeneous (see Two-axis structure below).

### Two-axis structure (update heterogeneity)

*[Derived (two-axis-structure, from composition-closure, linear-Gaussian case)]*

In the non-degenerate linear-Gaussian case with heterogeneous sub-agent update rules — e.g., two Kalman filters with different gains $K_1^\ast \neq K_2^\ast$ tracking correlated processes, projected to the 1D sum $\hat\omega_+ = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$ — the state closure defect has the closed form:

$$\varepsilon_x^2 = (\Delta K/2)^2 \big[S_- - C_{+-}^2 / S_+\big]$$

where $\Delta K = K_1^\ast - K_2^\ast$, $S_\pm$ are the innovation variances in the $\pm$ directions, and $C_{+-}$ is their cross-covariance.

This exhibits two independent drivers of $\varepsilon_x$, one along each unity axis of #def-unity-dimensions:

1. **Content unity** ($U_M$, via process correlation $\rho$): higher correlation → lower $\varepsilon_x$.
2. **Structural unity** ($U_f$, via gain mismatch $\Delta K$): when $\Delta K = 0$ (i.e., $U_f = 1$), $\varepsilon_x = 0$ at every $\rho$; when $\Delta K \neq 0$, $\varepsilon_x \gt 0$ even at perfect content correlation.

The four content unities measure shared information (goals, policies, observations, model state); $U_f$ measures whether sub-agents implement the same correction rule. The two axes contribute to the closure-defect rate-distortion surface independently — content unity controls compressibility of what the agents agree on; structural unity controls whether projection induces memory by mixing the discarded subspace into the retained one.

## Epistemic Status

*Conditional.* Max attainable: *exact* (linear-Gaussian scalar cases) to *robust qualitative* (general).

- The observation and action closed forms are *exact* in the linear-Gaussian scalar case with stated projection choices.
- The state closure form $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ is *exact* in the two-Kalman heterogeneous case.
- The rate-distortion framing (unity as compressibility parameter rather than direct predictor) is *robust qualitative* — it survives beyond linear-Gaussian, but concrete rate-distortion curves require case-by-case derivation.
- The joint $(U_O, U_\Sigma) \to \varepsilon_a$ formula is a *sketch* — the leading structure is derived; the precise forms of $f_1$ and $g$ are mechanical extensions not fully computed here.

Ceiling-limiting factors: non-Gaussian cases require information-theoretic bounds (Gaussian IB is fully tractable; general IB is not), and the structural-unity axis $U_f$ has a worked closed form only in the linear-Gaussian Kalman gain-mismatch case — a general theory of $f_M$ structural variation across arbitrary update operators is open.

## Discussion

**Why a one-axis reading fails.** A "high $U_M$ predicts low $\varepsilon_x$" reading is wrong in the two-Kalman case with the standard means-only projection: $\varepsilon_x \equiv 0$ for every correlation value, irrespective of $U_M$. The closure-defect surface depends on the projection choice, on the content-unity axis, and on the structural-unity axis $U_f$ — high content unity with mismatched update rules still produces $\varepsilon_x \gt 0$, while low content unity under a non-compressing projection still produces $\varepsilon_x = 0$. The rate-distortion framing is what makes the multi-parameter dependence explicit.

**Connection to the Information Bottleneck ( #form-information-bottleneck).** The rate-distortion shape is not coincidental. Projection admissibility condition (P1) in #form-composition-closure is the Lagrangian-dual of the IB constraint: the projection sits on or above the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$ for the relevance variable "next observation given action" ( #disc-compression-operations supplies the derivation). Unity dimensions — measured as mutual-information-like quantities between sub-agent state components — parametrize the frontier's shape. The four AAD compression operations ($M_t$, $\Sigma_t$, shared intent, $\Lambda$) share IB shape but are not shown to reduce to a single master problem (U-medium, per #disc-compression-operations); cross-instance theorems do not follow from shared shape alone. (P2) Lipschitz continuity is not naturally IB and remains a separate admissibility condition; (P3) dimensional reduction remains separate in the Gaussian case. The Gaussian-IB closed form applies to linear-Gaussian composition setups; beyond them, the IB frontier is definitional but requires variational or numerical approximation.

**Two-axis structure.** The unity profile in #def-unity-dimensions decomposes into a content axis (four dimensions: $U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$) measuring shared information, and a structural axis ($U_f$) measuring shared correction rules. In purposeful-agent settings ($G_t$ present), $U_\Sigma$ already absorbs structural variation in the policy half of the cycle — agents with different action laws have different effective policies — but the model-update half remains uncovered without $U_f$. In pure Section I composition (passive estimators, no $G_t$), $U_f$ is the only handle on structural homogeneity, and the heterogeneous-Kalman case in this segment is the canonical instance where it bites.

**Interpretation of "low closure defect."** Unity controls the rate-distortion curve; low closure defect is achievable with aggressive compression when unity is high. But closure defect alone does not measure composite *optimality* (see #form-composition-closure §5.1): two independent Kalman filters can have $\varepsilon^\ast = 0$ (perfectly representable) while failing to exploit cross-correlations (suboptimal relative to a joint filter). The rate-distortion mapping is about representability, not optimality.

## Working Notes

- **Extension to nonlinear cases.** The framing is linear-Gaussian because that's where rate-distortion has closed forms. Extension to nonlinear micro-dynamics would likely show $\varepsilon_x \gt 0$ even with consistent projections (the identity-propagation argument in Formal Expression relies on linearity). Worth a follow-up spike.
- **Structural-unity formalization.** A quantitative measure $U_f$ across arbitrary $f_M$ functions (beyond the linear-Gaussian gain-mismatch closed form) is open. Candidates for the underlying operator distance: operator-norm distance in function space, Fisher-information-weighted distance, or IB-style comparison. See #def-unity-dimensions Working Notes.
- **Joint $(U_O, U_\Sigma)$ derivation.** The exact $f_1$ and $g$ functional forms require a full joint-LQR vs independent-LQR comparison. Mechanical but deferred.
- **$U_O$ → sector-constant pathway (partial via #deriv-critical-mass-composition).** The LQR-compatibility sketch $\gamma(U_O) = -\gamma_{\max}U_O$ in #deriv-critical-mass-composition §5.2 (flagged discussion-grade) is a structural complement to this segment's rate-distortion framing: it channels $U_O$ into the composite sector-constant $\kappa_c$ through the signed coupling $\gamma$ rather than through the closure defect $\varepsilon$. Upgrading (UO-mult) from discussion-grade to derived requires the action-space inner-product analysis natural to this segment: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. Natural extension to the linear-Gaussian closed-form section above.
- **Mori-Zwanzig cross-check.** Under a stationary-measure setting, the Koopman-operator formulation of the projection-induced dynamics identifies the non-degenerate Kalman case as exercising the zero-lag memory kernel $K_0$ non-trivially, with $\lVert K_0 \rVert$ scaling with $\lvert\Delta K\rvert$. This is consistent with the two-axis finding here — a Mori-Zwanzig lower bound on $\varepsilon^\ast$ via the zero-lag kernel and the rate-distortion bound via IB should coincide at the same linear-algebraic quantity (the $L^2$ residual of projecting off an eigenspace of the micro-propagator). Formal equivalence not yet established. The MZ connection is developed further in #form-composition-closure Epistemic Status.
- **Relationship to #scope-composite-agent.** This segment describes quality *conditional* on composition existing — i.e., on #scope-composite-agent being satisfied via at least one of its three disjunctive routes (shared objective, hierarchical derivation, mutual benefit), *not* via a scalar $U_O$ threshold. The rate-distortion curves parametrize quality given scope-satisfaction; they do not address whether a composite exists at all. For multi-agent systems where no scope route applies, closure-defect quality talk is a category error — there is no composite whose closure defect to measure.
