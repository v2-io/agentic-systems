---
slug: detail-operationalization
type: detail
status: conditional
depends:
  - def-mismatch-signal
  - emp-update-gain
  - def-adaptive-tempo
  - result-sector-condition-stability
  - result-persistence-condition
  - der-deliberation-cost
  - result-structural-adaptation-necessity
  - hyp-communication-gain
  - der-team-persistence
stage: draft
---

# Detail: Operationalization — Estimation Procedures

Estimation recipes for core AAT quantities, bridging the measurement gap between formal objects and practical deployment.

The segment is **domain-honest** about which quantities are easily measured and which are operationally challenging: model uncertainty admits predictive-posterior / ensemble-spread / Bayesian-NN estimators; observation uncertainty admits channel calibration or residual variance; the innovation is directly measurable from prediction-versus-observation residuals, but the estimation error that the persistence results contain is not (their mean squares differ by the channel-noise floor, so the error's mean square is estimable by subtraction, not read off); tempo from event rate times effective gain; the sector parameter via either the gain-sector bridge (where applicable — Bayesian on exponential families; gradient on strongly convex) or empirical correction-rate-vs-mismatch regression; disturbance parameters split per Model D ($\hat\rho_{\det}$) versus Model S ($\hat\sigma_w$) with sequential dependence on $\hat{\mathcal{T}}$; critical-mismatch tolerance is a *domain parameter* not an estimated quantity (it encodes "how wrong can the model be before actions become harmful or ineffective?"). Model-class fitness is named as particularly challenging — not directly computable, requiring search across the model class; the observable signature is persistent mismatch despite adequate learning. Satisfaction gap and control regret require evaluating attainability, generally intractable in exact form. AAT's commitment is that the abstract machinery is operationalizable with stated quality trade-offs at each estimation step, not analytical idealization with no path to practice.

## Measurement Targets

| Quantity | Role in AAT | Typical unit | Minimum data needed |
|----------|-------------|--------------|---------------------|
| $U_M$ | Model uncertainty ( #emp-update-gain) | domain-specific variance/entropy | Predictive posterior or ensemble spread |
| $U_o$ | Observation uncertainty ( #emp-update-gain) | sensor variance/noise scale | Channel calibration or residual variance |
| $\rho_{\det}(t)$ | Total disturbance-rate bound on the estimation error, Model D ( #hyp-mismatch-dynamics) | surprise per time | The environmental rate $\rho_{\text{env}}$, the channel-noise bound $\bar\nu$ and the gain; see "What the residual-based recipes estimate" below |
| $\sigma_w$ | Total disturbance intensity on the estimation error, Model S ( #hyp-mismatch-dynamics) | surprise per $\sqrt{\text{time}}$ | The environmental and channel intensities $\sigma_{\text{env}}$, $\sigma_\nu$ and the gain; see below |
| $\rho_{\text{delib}}$ | Local mismatch drift during pauses ( #der-deliberation-cost) | surprise per time | Deliberation windows with no corrective action |
| $\alpha$ | Lower correction efficiency bound ( #result-sector-condition-stability) | inverse time | Vector mismatch trajectories + correction term |
| $R$ | Radius where local sector condition holds ( #result-sector-condition-stability) | surprise magnitude | Same as $\alpha$, plus breakdown detection |
| $\Vert\delta_{\text{critical}}\Vert$ | Functional adequacy threshold ( #result-persistence-condition) | surprise magnitude | Task-level performance curve vs mismatch |

## Estimator Cookbook

### Estimating $U_M$ and $U_o$

Use the most native uncertainty representation available in the domain:

| Domain | $U_M$ estimator | $U_o$ estimator |
| ------ | --------------- | --------------- |
| Kalman / linear Gaussian | Prior predictive variance $P_{t \vert t-1}$ | Measurement-noise variance $R_t$ (known or EM-estimated) |
| Conjugate Bayes | Posterior variance / inverse effective sample size | Likelihood variance (or precision inverse) |
| RL with ensembles | Across-head predictive variance $\operatorname{Var}_i[Q_i(s,a)]$ | TD-target noise variance over replay batches |
| Neural net regression | Ensemble or Laplace posterior variance | Aleatoric head output $\sigma^2(x)$ |
| PID / classical control | State-estimation covariance from observer | Sensor noise from calibration + residual PSD |

For the scalar gain heuristic ( #emp-update-gain), normalize to common units and compute:

*[Operational Definition]*

$$\hat{\eta}^*_t = \frac{\hat{U}_{M,t}}{\hat{U}_{M,t} + \hat{U}_{o,t}}$$

### Estimating Disturbance Parameters ($\rho_{\det}$, $\sigma_w$, $\rho_{\text{delib}}$)

The disturbance model split (Model D vs. Model S; see #hyp-mismatch-dynamics, #result-sector-condition-stability) requires different estimation procedures depending on the disturbance character.

**What the residual-based recipes estimate.** The persistence results' $\rho$ and $\sigma_w$ are the *total* disturbance on the estimation error $\bar\delta$ of #def-mismatch-signal: environmental change plus the channel noise the correction feeds back ( #deriv-sector-condition, Setup). The agent does not observe $\bar\delta$; it observes the innovation $\bar\delta + \nu$. The recipes below take $s_t$ from prediction-versus-observation residuals, which is the innovation, and read $\hat\rho_{\det}$, $\hat\sigma_w$ and $\hat\rho_{\text{delib}}$ off its increments. They therefore estimate properties of the innovation sequence, not the disturbance on the estimation error. For a well-tuned linear filter the innovation sequence is white, with no correction dynamics to subtract, so the "expected correction" removed in the Model S formula is not present in the data. The recipes estimate $\rho$ and $\sigma_w$ as defined only when the channel is noiseless ($\nu = 0$, innovation equal to estimation error). The same holds for the $\alpha$ and $R$ recipes below, which also read the state off $\delta_t$. Two relations hold in general and give a sound route for linear correction. In mean square the innovation exceeds the estimation error by exactly the channel-noise floor, term (iii) of #result-mismatch-decomposition, so $\mathbb E\lVert\bar\delta\rVert^2$ is estimable by subtracting a calibrated channel variance from the innovation's. And the total disturbance is computed from its primitives rather than estimated directly: $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ under Model S and $\rho = \rho_{\text{env}} + \alpha\bar\nu$ under Model D, with the channel terms from calibration and the environmental terms identified from the observation stream. Estimators for those environmental terms, for nonlinear correction, and for $\alpha$ and $R$ from innovation data are not yet written. Until they are, the formulas below are stated for the noiseless-channel case.

**Identifying the disturbance model.** The choice between Model D and Model S is domain-dependent:
- **Model D** (bounded deterministic, GA-2): appropriate when the environment changes persistently and directionally. Estimate $\rho_{\det}$ from worst-case bounds on mismatch injection rate. Examples: adversary who maneuvers systematically, API that drifts, climate that shifts.
- **Model S** (stochastic zero-mean, GA-2S): appropriate when the environment fluctuates unpredictably around a stable mean. Estimate $\sigma_w$ from its environmental and channel parts (above). Examples: market noise, sensor noise, random perturbations.
- **Mixed environments** use both: estimate $\rho_{\det}$ from the persistent component (trend) and $\sigma_w$ from the residual variance after detrending. The adversarial exponent interpolates smoothly between $b = 2$ (pure drift) and $b = 3/2$ (pure noise); see #result-adversarial-exponent-regimes.

For a noiseless channel, where the residual is the estimation error, let $s_t = \lVert\delta_t\rVert$ in surprise units (e.g., negative log-likelihood residual scale).

**Model D: Global mismatch injection rate ($\hat{\rho}_{\det}$):**

*[Operational Definition]*

$$\hat{\rho}_{\det}(t) = \left[\frac{s_{t+\Delta t} - s_t}{\Delta t} + \hat{\mathcal{T}}_t \, s_t\right]_+$$

where $[x]_+ = \max(x, 0)$ and $\hat{\mathcal{T}}$ evaluated at time $t$ is estimated adaptive tempo. Take the supremum (or a high quantile) over the estimation window.

**Model S: Noise scale ($\hat{\sigma}_w$):**

*[Operational Definition]*

$$\hat{\sigma}_w^2 = \text{Var}\left[\frac{s_{t+\Delta t} - (1 - \hat{\eta}^\ast)s_t}{\sqrt{\Delta t}}\right]$$

i.e., the variance of the mismatch innovations (residuals after subtracting the expected correction). For AR(1) processes, this is the innovation variance $\hat{\rho}^2$ directly.

**Note on estimation sequencing.** Both estimators require $\hat{\mathcal{T}}_t$ (or $\hat{\eta}^\ast$), estimated from $\hat{\nu}$ and $\hat{\eta}^\ast$. Estimate the gain and event rate first (from the agent's internal statistics and observation timing), then use these to extract the disturbance parameters from the mismatch trajectory. This sequential structure avoids circularity but introduces sensitivity: errors in $\hat{\mathcal{T}}$ propagate into $\hat\rho_{\det}$ and $\hat\sigma_w$.

**Local pause-window drift for #der-deliberation-cost ($\hat{\rho}_{\text{delib}}$):**

*[Operational Definition]*

$$\hat{\rho}_{\text{delib}} = \operatorname*{median}_{w \in \mathcal{W}_{\text{pause}}} \frac{s_{w,\text{end}} - s_{w,\text{start}}}{\Delta\tau_w}$$

using windows where corrective action is suspended or effectively delayed.

### Estimating $\alpha$ (sector lower bound)

#deriv-sector-condition uses $\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2$ for $\Vert\delta\Vert \leq R$. Operationally:

1. Estimate $\dot{\delta}_t$ (finite differences or filtered derivative).
2. Compute $\widehat F_t = -\dot{\delta}_t + w_t$ where disturbance proxy $w_t$ is estimated from exogenous perturbation channels or residual balancing.
3. Form ratios $r_t = (\delta_t^T \widehat F_t) / \Vert\delta_t\Vert^2$ on bins of $\Vert\delta_t\Vert$.
4. Set conservative lower bound $\hat{\alpha}$ as a low quantile (e.g., 10th percentile) of $r_t$ in the valid region.

### Estimating $R$ (valid-region radius)

Estimate $R$ as the largest radius for which sector inequality violations remain below tolerance:

*[Operational Criterion]*

$$\hat{R} = \sup \left\{ r \gt 0 : \Pr\left(\delta^T \widehat{F} \lt \hat{\alpha}\Vert\delta\Vert^2 \,\middle\vert\, \Vert\delta\Vert \le r\right) \le \epsilon \right\}$$

with a chosen violation tolerance $\epsilon$ (e.g., 5%).

### Estimating $\Vert\delta_{\text{critical}}\Vert$

Define a mission-level performance metric $J$ (reward rate, tracking error, service SLA, etc.). Set the critical mismatch threshold where performance crosses a minimum acceptable level $J_{\min}$:

*[Operational Definition]*

$$\Vert\hat{\delta}_{\text{critical}}\Vert = \inf \left\{ d : \mathbb{E}[J \mid \Vert\delta\Vert = d] \lt J_{\min} \right\}$$

This anchors #result-persistence-condition to real task outcomes.

## Recommended Estimation Sequence

1. Fix mismatch representation $\delta$ in one consistent unit system (prefer surprise-scale).
2. Estimate $U_o$ from channel physics/calibration; estimate $U_M$ from model uncertainty.
3. Validate gain behavior against #emp-update-gain ($\hat{\eta}^\ast$ trend checks).
4. Estimate $\rho_{\text{delib}}$ from pause windows ( #der-deliberation-cost) and $\rho(t)$ from full traces.
5. Estimate $\alpha$ and $R$ from local correction dynamics ( #deriv-sector-condition).
6. Estimate $\Vert\delta_{\text{critical}}\Vert$ from task-performance degradation.
7. Compute derived diagnostics:

   - Tempo margin (Model D): $\hat{\mathcal{T}} - \hat\rho_{\det}/\lVert\hat\delta_{\text{critical}}\rVert$
   - Tempo margin (Model S): $\hat{\mathcal{T}} - n\hat\sigma_w^2/(2\lVert\hat\delta_{\text{critical}}\rVert^2)$
   - Reserve: $\widehat{\Delta \rho^\ast} = \hat\alpha\hat R - \hat\rho_{\det}$
   - Deliberation feasibility: $\Delta\eta^\ast(\Delta\tau)\Vert\delta_{\text{post}}\Vert - \hat\rho_{\text{delib}}\Delta\tau$

## Decision-Theoretic Procedures

### Estimating $\lambda$ (Exploration Price)

The exploration weight $\lambda(M_t)$ in the unified policy objective ( #disc-ciy-unified-objective) prices information in value-equivalent terms:

| Context | $\lambda$ estimator | Source |
|---------|--------------------|--------|
| Finite bandits | Gittins index from dynamic programming | Exact (Gittins 1979) |
| Linear-Gaussian | Probing cost in quadratic objective | Exact (dual control) |
| Discrete MDP | $(\text{VoI})^2 / \text{info gain}$ | Information-directed sampling (Russo & Van Roy) |
| General | $\hat{\lambda} = c \cdot \hat U_M / \hat U_o$ | Heuristic: scale CIY weight by relative uncertainty |

For the heuristic: when $U_M \gg U_o$ (highly uncertain model), exploration is cheap relative to exploitation risk, so $\lambda$ should be large. When $U_M \ll U_o$ (confident model, noisy observations), exploitation dominates. The constant $c$ is domain-specific.

### Deliberation Stopping Policy

From #der-deliberation-cost, deliberation of duration $\Delta\tau$ is warranted when $\Delta\eta^\ast(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau$. Operationally:

1. Estimate $\rho_{\text{delib}}$ from prior pause windows.
2. Before each deliberation episode, estimate $\Vert\delta_{\text{post}}\Vert$ as current mismatch + $\rho_{\text{delib}} \cdot \Delta\tau_{\text{planned}}$.
3. Estimate $\Delta\eta^\ast(\Delta\tau)$ from the diminishing-returns profile of past deliberation episodes.
4. Stop deliberating when the marginal improvement rate $\partial \Delta\eta^\ast / \partial \Delta\tau$ drops below $\rho_{\text{delib}} / \Vert\delta_{\text{post}}\Vert$.

### Structural-Switch Trigger

From #result-structural-adaptation-necessity, structural adaptation is indicated when parametric convergence leaves a mismatch floor. Operationally:

1. Estimate the current mismatch floor $\Vert\delta\Vert_{\text{floor}}$ from converged residual statistics.
2. Estimate post-switch expected mismatch as $\Vert\delta\Vert_{\text{new}} \approx \rho / \alpha'$ where $\alpha'$ is the sector bound under the candidate new model class.
3. Estimate transition cost $C_{\text{switch}}$: knowledge loss, retraining time ($\Delta\tau_{\text{switch}}$), and accumulated mismatch during transition ($\rho \cdot \Delta\tau_{\text{switch}}$).
4. Switch when: $(\Vert\delta\Vert_{\text{floor}} - \Vert\delta\Vert_{\text{new}}) \cdot T_{\text{horizon}} \gt C_{\text{switch}}$.

In a team or an ensemble, read a mismatch floor as structural only after the cheaper multi-agent remedies have been tried and the residual pattern has survived them: recalibrating trust in sources, routing queries away from failing members, improving channels. Residuals correlated across members point to a limitation they share; residuals confined to some members point to those members ( #der-team-persistence).

## Multi-Agent Quantities

Agent $i$ tracks, for each source $j$, the inputs to the communication gain of #hyp-communication-gain and the team quantities of #der-team-persistence:

| Quantity | Role in AAT | Estimator |
|----------|-------------|-----------|
| $U_{o,ji}$ | Channel noise in the communication gain | Message latency and the variance the channel adds to $j$'s report, from channel calibration |
| $U_{\text{src},j} + U_{\text{align},ji}$ | Source-quality and teleological-unity uncertainty | Variance of $j$'s past reports against later ground truth, minus $\hat U_{o,ji}$, floored at zero; for probabilistic reports, a running Brier or log-loss score |
| $V_{\text{disagree}}$ | Disagreement energy | Members' predictions on a common set of queries |
| $\Delta\mathcal T_i^{\text{cost}}(j)$ | Coordination cost | $i$'s direct-adaptation tempo with and without the channel to $j$ |

Residuals alone do not separate $U_{\text{src}}$ from $U_{\text{align}}$: miscalibration and strategic distortion can leave the same residual variance. Separating them needs evidence about the direction of $j$'s errors relative to $j$'s own interests. Where that is unavailable, the sum is what enters the gain.

Two procedures follow from the same segments. An update that would be costly if wrong, from a source whose reliability is low or poorly known, waits for agreement from other sources: the risk-asymmetric trust of #hyp-communication-gain applied as a quorum. Agreement counts only between sources that do not share an upstream source; otherwise the quorum counts one source several times ( #deriv-tempo-additivity). And query actions are logged apart from actions on the world, since their information yield and cost differ ( #def-causal-information-yield).

## Estimator Uncertainty Guidance

**$\hat{\eta}^\ast$ (gain estimate).** Approximate variance via the delta method:

$$\text{Var}(\hat{\eta}^*) \approx \hat{\eta}^{*2}(1-\hat{\eta}^*)^2 \left[\frac{\text{Var}(\hat{U}_M)}{\hat{U}_M^2} + \frac{\text{Var}(\hat{U}_o)}{\hat{U}_o^2}\right]$$

Near 0 or 1, stable (dominated by one source). Near 0.5, most volatile.

**$\hat{\rho}$ (mismatch injection rate).** Finite-difference estimation amplifies noise. Recommend smoothing before differencing. Minimum ~20 observations for stable trend; ~50 for reliable variance. The $[\cdot]_+$ clipping introduces positive bias at small $\rho$.

**$\hat{\alpha}$ (sector lower bound).** The 10th-percentile approach gives approximately 90% confidence under stationarity. Report quantile level, bin count, and bin width.

**$\hat{R}$ (sector-condition radius).** A sharp drop-off in sector-condition satisfaction is a strong signal; gradual decay suggests the sector condition may not hold cleanly.

**Nonstationarity caveat.** All estimators assume approximate stationarity over the estimation window. When environment regime changes are suspected ( #result-structural-adaptation-necessity), re-estimate from post-change data only.

## Epistemic Status

This is a *procedures document* — estimation recipes, not theoretical claims. Each estimator inherits the epistemic status of the quantity it targets: the gain estimator's validity depends on #emp-update-gain's structural claim; the sector-bound estimator's validity depends on #result-sector-condition-stability's assumptions. The estimation procedures themselves are *conditional* on these theoretical foundations and on the stationarity and data-sufficiency assumptions noted above.

## Working Notes

- End-to-end worked examples instantiating the full chain are in #example-kalman (exact) and #example-bandit (approximate).
- The $\hat{\rho}$ estimator's dependence on $\hat{\mathcal{T}}$ creates a sequential estimation chain. Errors compound. An alternative approach: estimate $\rho$ directly from exogenous environmental change measurements when available, bypassing the mismatch trajectory entirely.
- The structural-switch trigger's $T_{\text{horizon}}$ (expected time the new model class will remain adequate) is itself uncertain and difficult to estimate. In practice, this is where the agent's $M_t$ does the real work — predicting environmental stability.
