---
slug: unity-closure-mapping
type: result
status: conditional
depends:
  - definition-unity-dimensions
  - composition-closure
  - information-bottleneck
stage: draft
---

# Result: Unity-to-Closure Rate-Distortion Mapping

Unity dimensions parametrize rate-distortion curves for closure-defect components, not point-valued predictors. For each unity $U_d$, the achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in $U_d$ (higher unity → lower achievable defect at a given compression). Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly. Update-rule heterogeneity across sub-agents is an independent axis, not captured by the unity dimensions as defined in #definition-unity-dimensions.

## Formal Expression

### Rate-distortion framing (general)

*[Formulation (unity-rate-distortion)]*

Fix a composite agent satisfying the admissibility conditions (A1)-(A4) in #composition-closure. For each unity dimension $U_d$ (with $d \in \{M, \Sigma, \text{obs}\}$, and $U_O$ contributing jointly with $U_\Sigma$ — see below), the achievable component closure defect under a projection whose corresponding macro-dimension is $k_d$ satisfies:

$$\varepsilon_d^{\min}(k_d) = f_d\big(k_d;\; U_d,\; \Delta f\big)$$

where $f_d$ is monotone decreasing in $U_d$, monotone increasing in aggressiveness of compression (smaller $k_d$), and depends on the update-rule heterogeneity $\Delta f$ across sub-agents. The mapping from unity to closure-defect *magnitude* is via the shape of this rate-distortion curve; unity does not directly predict closure-defect value.

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

regardless of $U_M$ or compression dimension. Linear projections of linear dynamics are exact. $\varepsilon_x$ becomes non-trivial only when:

- the projection is inconsistent (macro state and macro observation projections disagree),
- the micro-dynamics are nonlinear, or
- sub-agent update rules are heterogeneous (see Two-axis structure below).

### Two-axis structure (update heterogeneity)

*[Derived (two-axis-structure, from composition-closure, linear-Gaussian case)]*

In the non-degenerate linear-Gaussian case with heterogeneous sub-agent update rules — e.g., two Kalman filters with different gains $K_1^\ast \neq K_2^\ast$ tracking correlated processes, projected to the 1D sum $\hat\omega_+ = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$ — the state closure defect has the closed form:

$$\varepsilon_x^2 = (\Delta K/2)^2 \big[S_- - C_{+-}^2 / S_+\big]$$

where $\Delta K = K_1^\ast - K_2^\ast$, $S_\pm$ are the innovation variances in the $\pm$ directions, and $C_{+-}$ is their cross-covariance.

This reveals two independent drivers of $\varepsilon_x$:

1. **Sub-agent unity** ($U_M$, via process correlation $\rho$): higher correlation → lower $\varepsilon_x$.
2. **Update heterogeneity** ($\Delta K$): different Kalman gains produce $\varepsilon_x \gt 0$ regardless of correlation. When $\Delta K = 0$, $\varepsilon_x = 0$ at every $\rho$; when $\Delta K \neq 0$, $\varepsilon_x \gt 0$ even at perfect correlation.

Update heterogeneity is not captured by any of the four unity dimensions as defined in #definition-unity-dimensions. The four unities measure shared *content* (information, goals, policies, observations); $\Delta K$ measures differential *structure* (whether agents implement the same correction rule). This is an independent dimension of the closure-defect rate-distortion surface.

## Epistemic Status

*Conditional.* Max attainable: *exact* (linear-Gaussian scalar cases) to *robust qualitative* (general).

- The observation and action closed forms are *exact* in the linear-Gaussian scalar case with stated projection choices.
- The state closure form $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ is *exact* in the two-Kalman heterogeneous case.
- The rate-distortion framing (unity as compressibility parameter rather than direct predictor) is *robust qualitative* — it survives beyond linear-Gaussian, but concrete rate-distortion curves require case-by-case derivation.
- The joint $(U_O, U_\Sigma) \to \varepsilon_a$ formula is a *sketch* — the leading structure is derived; the precise forms of $f_1$ and $g$ are mechanical extensions not fully computed here.

Ceiling-limiting factors: non-Gaussian cases require information-theoretic bounds (Gaussian IB is fully tractable; general IB is not) and the update-heterogeneity axis is framework-specific — a general theory of $f_M$ structural variation is open.

## Discussion

**Why the naive reading fails.** A literal reading of #definition-unity-dimensions' Discussion — "high $U_M$ predicts low $\varepsilon_x$" etc. — is wrong in the two-Kalman case with the standard means-only projection: $\varepsilon_x \equiv 0$ for every correlation value. The Discussion in #definition-unity-dimensions did not specify the projection, leaving the claim ambiguous. Making the rate-distortion structure explicit resolves the ambiguity: for a fixed projection, closure defect is a *function of multiple parameters*, and unity controls one axis (compressibility) among several.

**Connection to the Information Bottleneck ( #information-bottleneck).** The rate-distortion shape is not coincidental. Projection admissibility condition (P1) in #composition-closure is the Lagrangian-dual of the IB constraint: the projection sits on or above the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$ for the relevance variable "next observation given action" ( #compression-operations supplies the derivation). Unity dimensions — measured as mutual-information-like quantities between sub-agent state components — parametrize the frontier's shape. The four AAD compression operations ($M_t$, $\Sigma_t$, shared intent, $\Lambda$) share IB shape but are not shown to reduce to a single master problem (U-medium, per #compression-operations); cross-instance theorems do not follow from shared shape alone. (P2) Lipschitz continuity is not naturally IB and remains a separate admissibility condition; (P3) dimensional reduction remains separate in the Gaussian case. The Gaussian-IB closed form applies to linear-Gaussian composition setups; beyond them, the IB frontier is definitional but requires variational or numerical approximation.

**Two-axis structure and the unity-dimensions gap.** The update-heterogeneity finding exposes a real gap in #definition-unity-dimensions: the four dimensions capture content-sharing but not structural homogeneity of update rules. In purposeful-agent settings ($G_t$ present), $U_\Sigma$ partially absorbs this — agents with different Kalman-like updates have different effective policies, so strategic unity captures some of the effect. In pure Section I composition (passive estimators, no $G_t$), the framework has no way to capture update heterogeneity. Three resolution options are logged in #definition-unity-dimensions' Working Notes; the honest minimal framing is to accept the two-axis structure.

**Interpretation of "low closure defect."** Unity controls the rate-distortion curve; low closure defect is achievable with aggressive compression when unity is high. But closure defect alone does not measure composite *optimality* (see #composition-closure §5.1): two independent Kalman filters can have $\varepsilon^\ast = 0$ (perfectly representable) while failing to exploit cross-correlations (suboptimal relative to a joint filter). The rate-distortion mapping is about representability, not optimality.

## Working Notes

- **Extension to nonlinear cases.** The framing is linear-Gaussian because that's where rate-distortion has closed forms. Extension to nonlinear micro-dynamics would likely show $\varepsilon_x \gt 0$ even with consistent projections (the identity-propagation argument in Formal Expression relies on linearity). Worth a follow-up spike.
- **Update-heterogeneity formalization.** A quantitative measure of $\Delta f$ across arbitrary $f_M$ functions (not just scalar gains) is open. Candidates: operator-norm distance in function space, Fisher-information-weighted distance, or IB-style comparison.
- **Joint $(U_O, U_\Sigma)$ derivation.** The exact $f_1$ and $g$ functional forms require a full joint-LQR vs independent-LQR comparison. Mechanical but deferred.
- **$U_O$ → sector-constant pathway (partial via #critical-mass-composition).** The LQR-compatibility sketch $\gamma(U_O) = -\gamma_{\max}U_O$ in #critical-mass-composition §5.2 (flagged discussion-grade) is a structural complement to this segment's rate-distortion framing: it channels $U_O$ into the composite sector-constant $\kappa_c$ through the signed coupling $\gamma$ rather than through the closure defect $\varepsilon$. Upgrading (UO-mult) from discussion-grade to derived requires the action-space inner-product analysis natural to this segment: define the environment's action-coupling operator, show that LQR-linear policies produce cross-actions with inner product proportional to target correlation, and pin $\gamma_{\max}$ in terms of the quadratic objective's Hessian and the environment's coupling gain. Natural extension to the linear-Gaussian closed-form section above.
- **Mori-Zwanzig cross-check.** Under a stationary-measure setting, the Koopman-operator formulation of the projection-induced dynamics identifies the non-degenerate Kalman case as exercising the zero-lag memory kernel $K_0$ non-trivially, with $\lVert K_0 \rVert$ scaling with $\lvert\Delta K\rvert$. This is consistent with the two-axis finding here — a Mori-Zwanzig lower bound on $\varepsilon^\ast$ via the zero-lag kernel and the rate-distortion bound via IB should coincide at the same linear-algebraic quantity (the $L^2$ residual of projecting off an eigenspace of the micro-propagator). Formal equivalence not yet established. The MZ connection is developed further in #composition-closure Epistemic Status.
- **Relationship to #scope-composite-agent.** This segment describes quality *conditional* on composition existing — i.e., on #scope-composite-agent being satisfied via at least one of its three disjunctive routes (shared objective, hierarchical derivation, mutual benefit), *not* via a scalar $U_O$ threshold. The rate-distortion curves parametrize quality given scope-satisfaction; they do not address whether a composite exists at all. For multi-agent systems where no scope route applies, closure-defect quality talk is a category error — there is no composite whose closure defect to measure.
