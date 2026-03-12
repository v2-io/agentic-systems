---
slug: operationalization
type: detail
status: conditional
depends:
  - mismatch-signal
  - update-gain
  - adaptive-tempo
  - sector-condition-stability
  - persistence-condition
  - deliberation-cost
  - structural-adaptation-necessity
---

# Detail: Operationalization — Estimation Procedures

Estimation recipes for core ACT quantities, bridging the measurement gap between formal objects and practical deployment.

## Measurement Targets

| Quantity | Role in ACT | Typical unit | Minimum data needed |
|----------|-------------|--------------|---------------------|
| $U_M$ | Model uncertainty ( #update-gain) | domain-specific variance/entropy | Predictive posterior or ensemble spread |
| $U_o$ | Observation uncertainty ( #update-gain) | sensor variance/noise scale | Channel calibration or residual variance |
| $\rho(t)$ | Mismatch injection rate ( #mismatch-dynamics) | surprise per time | Time-series of mismatch magnitudes |
| $\rho_{\text{delib}}$ | Local mismatch drift during pauses ( #deliberation-cost) | surprise per time | Deliberation windows with no corrective action |
| $\alpha$ | Lower correction efficiency bound ( #sector-condition-stability) | inverse time | Vector mismatch trajectories + correction term |
| $R$ | Radius where local sector condition holds ( #sector-condition-stability) | surprise magnitude | Same as $\alpha$, plus breakdown detection |
| $\|\delta_{\text{critical}}\|$ | Functional adequacy threshold ( #persistence-condition) | surprise magnitude | Task-level performance curve vs mismatch |

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

For the scalar gain heuristic ( #update-gain), normalize to common units and compute:

*[Operational Definition]*

$$\hat{\eta}^*_t = \frac{\hat{U}_{M,t}}{\hat{U}_{M,t} + \hat{U}_{o,t}}$$

### Estimating $\rho(t)$ and $\rho_{\text{delib}}$

Let $s_t = \|\delta_t\|$ in surprise units (e.g., negative log-likelihood residual scale).

Global mismatch injection rate:

*[Operational Definition]*

$$\hat{\rho}(t) = \left[\frac{s_{t+\Delta t} - s_t}{\Delta t} + \hat{\mathcal{T}}_t \, s_t\right]_+$$

where $[x]_+ = \max(x, 0)$ and $\hat{\mathcal{T}}_t$ is estimated adaptive tempo.

**Note on estimation sequencing.** This estimator requires $\hat{\mathcal{T}}_t$, estimated from $\hat{\nu}$ and $\hat{\eta}^*$. Estimate the gain and event rate first (from the agent's internal statistics and observation timing), then use these to extract $\rho$ from the mismatch trajectory. This sequential structure avoids circularity but introduces sensitivity: errors in $\hat{\mathcal{T}}$ propagate linearly into $\hat{\rho}$.

Local pause-window drift for #deliberation-cost:

*[Operational Definition]*

$$\hat{\rho}_{\text{delib}} = \operatorname*{median}_{w \in \mathcal{W}_{\text{pause}}} \frac{s_{w,\text{end}} - s_{w,\text{start}}}{\Delta\tau_w}$$

using windows where corrective action is suspended or effectively delayed.

### Estimating $\alpha$ (sector lower bound)

#sector-condition-derivation uses $\delta^T F(\mathcal{T}, \delta) \geq \alpha \|\delta\|^2$ for $\|\delta\| \leq R$. Operationally:

1. Estimate $\dot{\delta}_t$ (finite differences or filtered derivative).
2. Compute $\widehat{F}_t = -\dot{\delta}_t + w_t$ where disturbance proxy $w_t$ is estimated from exogenous perturbation channels or residual balancing.
3. Form ratios $r_t = (\delta_t^T \widehat{F}_t) / \|\delta_t\|^2$ on bins of $\|\delta_t\|$.
4. Set conservative lower bound $\hat{\alpha}$ as a low quantile (e.g., 10th percentile) of $r_t$ in the valid region.

### Estimating $R$ (valid-region radius)

Estimate $R$ as the largest radius for which sector inequality violations remain below tolerance:

*[Operational Criterion]*

$$\hat{R} = \sup \left\{ r > 0 : \Pr\left(\delta^T \widehat{F} < \hat{\alpha}\|\delta\|^2 \,\middle|\, \|\delta\| \le r\right) \le \epsilon \right\}$$

with a chosen violation tolerance $\epsilon$ (e.g., 5%).

### Estimating $\|\delta_{\text{critical}}\|$

Define a mission-level performance metric $J$ (reward rate, tracking error, service SLA, etc.). Set the critical mismatch threshold where performance crosses a minimum acceptable level $J_{\min}$:

*[Operational Definition]*

$$\|\hat{\delta}_{\text{critical}}\| = \inf \left\{ d : \mathbb{E}[J \mid \|\delta\| = d] < J_{\min} \right\}$$

This anchors #persistence-condition to real task outcomes.

## Recommended Estimation Sequence

1. Fix mismatch representation $\delta$ in one consistent unit system (prefer surprise-scale).
2. Estimate $U_o$ from channel physics/calibration; estimate $U_M$ from model uncertainty.
3. Validate gain behavior against #update-gain ($\hat{\eta}^*$ trend checks).
4. Estimate $\rho_{\text{delib}}$ from pause windows ( #deliberation-cost) and $\rho(t)$ from full traces.
5. Estimate $\alpha$ and $R$ from local correction dynamics ( #sector-condition-derivation).
6. Estimate $\|\delta_{\text{critical}}\|$ from task-performance degradation.
7. Compute derived diagnostics: tempo margin $\hat{\mathcal{T}} - \hat{\rho}/\|\hat{\delta}_{\text{critical}}\|$, reserve $\widehat{\Delta \rho^*} = \hat{\alpha}\hat{R} - \hat{\rho}$, and deliberation feasibility $\Delta\eta^*(\Delta\tau)\|\delta_{\text{post}}\| - \hat{\rho}_{\text{delib}}\Delta\tau$.

## Decision-Theoretic Procedures

### Estimating $\lambda$ (Exploration Price)

The exploration weight $\lambda(M_t)$ in #causal-information-yield's policy objective prices information in value-equivalent terms:

| Context | $\lambda$ estimator | Source |
|---------|--------------------|--------|
| Finite bandits | Gittins index from dynamic programming | Exact (Gittins 1979) |
| Linear-Gaussian | Probing cost in quadratic objective | Exact (dual control) |
| Discrete MDP | $(\text{VoI})^2 / \text{info gain}$ | Information-directed sampling (Russo & Van Roy) |
| General | $\hat{\lambda} = c \cdot \hat{U}_M / \hat{U}_o$ | Heuristic: scale CIY weight by relative uncertainty |

For the heuristic: when $U_M \gg U_o$ (highly uncertain model), exploration is cheap relative to exploitation risk, so $\lambda$ should be large. When $U_M \ll U_o$ (confident model, noisy observations), exploitation dominates. The constant $c$ is domain-specific.

### Deliberation Stopping Policy

From #deliberation-cost, deliberation of duration $\Delta\tau$ is warranted when $\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| > \rho_{\text{delib}} \cdot \Delta\tau$. Operationally:

1. Estimate $\rho_{\text{delib}}$ from prior pause windows.
2. Before each deliberation episode, estimate $\|\delta_{\text{post}}\|$ as current mismatch + $\rho_{\text{delib}} \cdot \Delta\tau_{\text{planned}}$.
3. Estimate $\Delta\eta^*(\Delta\tau)$ from the diminishing-returns profile of past deliberation episodes.
4. Stop deliberating when the marginal improvement rate $\partial \Delta\eta^* / \partial \Delta\tau$ drops below $\rho_{\text{delib}} / \|\delta_{\text{post}}\|$.

### Structural-Switch Trigger

From #structural-adaptation-necessity, structural adaptation is indicated when parametric convergence leaves a mismatch floor. Operationally:

1. Estimate the current mismatch floor $\|\delta\|_{\text{floor}}$ from converged residual statistics.
2. Estimate post-switch expected mismatch as $\|\delta\|_{\text{new}} \approx \rho / \alpha'$ where $\alpha'$ is the sector bound under the candidate new model class.
3. Estimate transition cost $C_{\text{switch}}$: knowledge loss, retraining time ($\Delta\tau_{\text{switch}}$), and accumulated mismatch during transition ($\rho \cdot \Delta\tau_{\text{switch}}$).
4. Switch when: $(\|\delta\|_{\text{floor}} - \|\delta\|_{\text{new}}) \cdot T_{\text{horizon}} > C_{\text{switch}}$.

## Estimator Uncertainty Guidance

**$\hat{\eta}^*$ (gain estimate).** Approximate variance via the delta method:

$$\text{Var}(\hat{\eta}^*) \approx \hat{\eta}^{*2}(1-\hat{\eta}^*)^2 \left[\frac{\text{Var}(\hat{U}_M)}{\hat{U}_M^2} + \frac{\text{Var}(\hat{U}_o)}{\hat{U}_o^2}\right]$$

Near 0 or 1, stable (dominated by one source). Near 0.5, most volatile.

**$\hat{\rho}$ (mismatch injection rate).** Finite-difference estimation amplifies noise. Recommend smoothing before differencing. Minimum ~20 observations for stable trend; ~50 for reliable variance. The $[\cdot]_+$ clipping introduces positive bias at small $\rho$.

**$\hat{\alpha}$ (sector lower bound).** The 10th-percentile approach gives approximately 90% confidence under stationarity. Report quantile level, bin count, and bin width.

**$\hat{R}$ (sector-condition radius).** A sharp drop-off in sector-condition satisfaction is a strong signal; gradual decay suggests the sector condition may not hold cleanly.

**Nonstationarity caveat.** All estimators assume approximate stationarity over the estimation window. When environment regime changes are suspected ( #structural-adaptation-necessity), re-estimate from post-change data only.

## Epistemic Status

This is a *procedures document* — estimation recipes, not theoretical claims. Each estimator inherits the epistemic status of the quantity it targets: the gain estimator's validity depends on #update-gain's structural claim; the sector-bound estimator's validity depends on #sector-condition-stability's assumptions. The estimation procedures themselves are *conditional* on these theoretical foundations and on the stationarity and data-sufficiency assumptions noted above.

## Working Notes

- End-to-end worked examples instantiating the full chain are in #worked-example-kalman (exact) and #worked-example-bandit (approximate).
- The $\hat{\rho}$ estimator's dependence on $\hat{\mathcal{T}}$ creates a sequential estimation chain. Errors compound. An alternative approach: estimate $\rho$ directly from exogenous environmental change measurements when available, bypassing the mismatch trajectory entirely.
- The structural-switch trigger's $T_{\text{horizon}}$ (expected time the new model class will remain adequate) is itself uncertain and difficult to estimate. In practice, this is where the agent's $M_t$ does the real work — predicting environmental stability.

*(Descended from TFT Appendix B: Operationalization.)*
