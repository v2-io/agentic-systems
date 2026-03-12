# Appendix B: Operationalization — Estimation Procedures

**Epistemic status**: This appendix is a procedures document. It specifies estimation recipes for core TFT quantities. End-to-end worked examples that instantiate the full chain are provided in [Appendix C](Appendix-C-Kalman-Example.md) (Kalman, exact) and [Appendix D](Appendix-D-RL-Example.md) (RL, approximate).

## Purpose

This appendix addresses the measurement gap between TFT's formal objects and practical deployment: how to estimate $U_M$, $U_o$, $\rho$, $\alpha$, $R$, and $\|\delta_{\text{critical}}\|$ from data.

## B.1 Measurement Targets

| Quantity | Role in TFT | Typical unit | Minimum data needed |
|----------|-------------|--------------|---------------------|
| $U_M$ | Model uncertainty (TF-06) | domain-specific variance/entropy | Predictive posterior or ensemble spread |
| $U_o$ | Observation uncertainty (TF-04/TF-06) | sensor variance/noise scale | Channel calibration or residual variance |
| $\rho(t)$ | Mismatch injection rate (TF-11) | surprise per time | Time-series of mismatch magnitudes |
| $\rho_{\text{delib}}$ | Local mismatch drift during pauses (TF-09) | surprise per time | Deliberation windows with no corrective action |
| $\alpha$ | Lower correction efficiency bound (App. A) | inverse time | Vector mismatch trajectories + correction term |
| $R$ | Radius where local sector condition holds (App. A) | surprise magnitude | Same as $\alpha$, plus breakdown detection |
| $\|\delta_{\text{critical}}\|$ | Functional adequacy threshold (TF-11) | surprise magnitude | Task-level performance curve vs mismatch |

## B.2 Estimator Cookbook

### B.2.1 Estimating $U_M$ and $U_o$

Use the most native uncertainty representation available in the domain:

| Domain                   | $U_M$ estimator                                                  | $U_o$ estimator                                          |
| ------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------- |
| Kalman / linear Gaussian | Prior predictive variance $P_{t \vert t-1}$                      | Measurement-noise variance $R_t$ (known or EM-estimated) |
| Conjugate Bayes          | Posterior variance / inverse effective sample size               | Likelihood variance (or precision inverse)               |
| RL with ensembles        | Across-head predictive variance $\operatorname{Var}_i[Q_i(s,a)]$ | TD-target noise variance over replay batches             |
| Neural net regression    | Ensemble or Laplace posterior variance                           | Aleatoric head output $\sigma^2(x)$                      |
| PID / classical control  | State-estimation covariance from observer                        | Sensor noise from calibration + residual PSD             |

For TFT's scalar gain heuristic (TF-06), normalize to common units and compute:

*[Operational Definition]*
$$\hat{\eta}^*_t = \frac{\hat{U}_{M,t}}{\hat{U}_{M,t} + \hat{U}_{o,t}}$$

### B.2.2 Estimating $\rho(t)$ and $\rho_{\text{delib}}$

Let $s_t = \|\delta_t\|$ in surprise units (e.g., negative log-likelihood residual scale).

Global mismatch injection rate:

*[Operational Definition]*
$$\hat{\rho}(t) = \left[\frac{s_{t+\Delta t} - s_t}{\Delta t} + \hat{\mathcal{T}}_t \, s_t\right]_+$$

where $[x]_+ = \max(x, 0)$ and $\hat{\mathcal{T}}_t$ is estimated adaptive tempo.

**Note on estimation sequencing.** This estimator requires $\hat{\mathcal{T}}_t$, which is itself estimated from $\hat{\nu}$ and $\hat{\eta}^*$ (steps 2-3 in the recommended sequence, B.3). The estimation is therefore *sequential*, not simultaneous: estimate the gain and event rate first (from the agent's internal statistics and observation timing), then use these to extract $\rho$ from the mismatch trajectory. The gain and event rate are typically estimable independently of $\rho$ (they depend on the agent's own uncertainty and event timing, not on the environment's rate of change). This sequential structure avoids circularity but introduces sensitivity: errors in $\hat{\mathcal{T}}$ propagate linearly into $\hat{\rho}$.

Local pause-window drift for TF-09:

*[Operational Definition]*
$$\hat{\rho}_{\text{delib}} = \operatorname*{median}_{w \in \mathcal{W}_{\text{pause}}} \frac{s_{w,\text{end}} - s_{w,\text{start}}}{\Delta\tau_w}$$

using windows where corrective action is suspended or effectively delayed.

### B.2.3 Estimating $\alpha$ (sector lower bound)

Appendix A uses:

*[Assumption A2']*
$$\delta^T F(\mathcal{T}, \delta) \ge \alpha \|\delta\|^2 \quad \text{for } \|\delta\| \le R$$

Operationally:

1. Estimate $\dot{\delta}_t$ (finite differences or filtered derivative).
2. Compute $\widehat{F}_t = -\dot{\delta}_t + w_t$ where disturbance proxy $w_t$ is estimated from exogenous perturbation channels or residual balancing.
3. Form ratios $r_t = (\delta_t^T \widehat{F}_t) / \|\delta_t\|^2$ on bins of $\|\delta_t\|$.
4. Set conservative lower bound $\hat{\alpha}$ as a low quantile (for example 10th percentile) of $r_t$ in the valid region.

### B.2.4 Estimating $R$ (valid-region radius)

Estimate $R$ as the largest radius for which sector inequality violations remain below tolerance:

*[Operational Criterion]*
$$\hat{R} = \sup \left\{ r > 0 : \Pr\left(\delta^T \widehat{F} < \hat{\alpha}\|\delta\|^2 \,\middle|\, \|\delta\| \le r\right) \le \epsilon \right\}$$

with a chosen violation tolerance $\epsilon$ (for example 5%).

### B.2.5 Estimating $\|\delta_{\text{critical}}\|$

Define a mission-level performance metric $J$ (reward rate, tracking error, service SLA, etc.).
Set the critical mismatch threshold where performance crosses a minimum acceptable level $J_{\min}$:

*[Operational Definition]*
$$\|\hat{\delta}_{\text{critical}}\| = \inf \left\{ d : \mathbb{E}[J \mid \|\delta\| = d] < J_{\min} \right\}$$

This anchors TF-11's normalized persistence condition to real task outcomes.

## B.3 Recommended Estimation Sequence

1. Fix mismatch representation $\delta$ in one consistent unit system (prefer surprise-scale).
2. Estimate $U_o$ from channel physics/calibration; estimate $U_M$ from model uncertainty.
3. Validate gain behavior against TF-06 ($\hat{\eta}^*$ trend checks).
4. Estimate $\rho_{\text{delib}}$ from pause windows (TF-09) and $\rho(t)$ from full traces (TF-11).
5. Estimate $\alpha$ and $R$ from local correction dynamics (Appendix A).
6. Estimate $\|\delta_{\text{critical}}\|$ from task-performance degradation.
7. Compute derived diagnostics: tempo margin $\hat{\mathcal{T}} - \hat{\rho}/\|\hat{\delta}_{\text{critical}}\|$, reserve $\widehat{\Delta \rho^*} = \hat{\alpha}\hat{R} - \hat{\rho}$, and deliberation feasibility $\Delta\eta^*(\Delta\tau)\|\delta_{\text{post}}\| - \hat{\rho}_{\text{delib}}\Delta\tau$.

## B.4 Minimal Reproducibility Checklist

End-to-end worked examples demonstrating the full TFT chain are provided in [Appendix C](Appendix-C-Kalman-Example.md) (Kalman/linear-Gaussian domain, exact mapping) and [Appendix D](Appendix-D-RL-Example.md) (nonstationary bandit/RL domain, approximate mapping).

For any domain report claiming TFT validation, include:

1. Mismatch definition and units.
2. Estimation method for $U_M$, $U_o$, and uncertainty calibration diagnostics.
3. Estimation method for $\rho_{\text{delib}}$ and $\rho(t)$ with window definitions.
4. Sector-bound estimation method ($\alpha$, $R$) and violation tolerance $\epsilon$.
5. Task-level definition of $\|\delta_{\text{critical}}\|$.
6. At least one ablation where $\eta$ is intentionally miscalibrated to test TF-06 predictions.
7. At least one induced-shock test to evaluate reserve prediction $\Delta\rho^*$.

## B.5 Estimator Uncertainty and Sample-Size Guidance

The estimators in B.2 are point recipes. This section provides guidance on their reliability.

**$\hat{\eta}^*$ (gain estimate).** Inherits uncertainty from $\hat{U}_M$ and $\hat{U}_o$. The ratio $U_M/(U_M + U_o)$ is most sensitive when $U_M \approx U_o$ (both contribute equally). Approximate variance via the delta method:

*[Operational Guidance]*
$$\text{Var}(\hat{\eta}^*) \approx \hat{\eta}^{*2}(1-\hat{\eta}^*)^2 \left[\frac{\text{Var}(\hat{U}_M)}{\hat{U}_M^2} + \frac{\text{Var}(\hat{U}_o)}{\hat{U}_o^2}\right]$$

When $\hat{\eta}^*$ is near 0 or 1, the estimate is stable (dominated by one uncertainty source). Near 0.5, both sources matter and the estimate is most volatile.

**$\hat{\rho}$ (mismatch injection rate).** Finite-difference estimation amplifies noise. Recommend smoothing the mismatch time series (exponential moving average or local regression) before differencing. Minimum sample guidance: ~20 mismatch observations for a stable trend estimate; ~50 for reliable variance characterization. The $[\cdot]_+$ clipping in the estimator removes negative estimates but introduces positive bias at small $\rho$; report the pre-clipped distribution if possible.

**$\hat{\alpha}$ (sector lower bound).** The conservative lower-quantile approach (B.2.3) inherently accounts for estimation noise. The 10th-percentile choice gives approximately 90% confidence that the true $\alpha$ exceeds the estimate, under stationarity. Precision scales as $\sim 1/\sqrt{N}$ where $N$ is the number of bins. Report the quantile level, bin count, and bin width alongside $\hat{\alpha}$.

**$\hat{R}$ (sector-condition radius).** The violation-tolerance criterion (B.2.4) is inherently conservative. Report the tolerance $\epsilon$, the sample size per bin, and the number of bins with violations. A sharp drop-off in sector-condition satisfaction at some radius is a strong signal; a gradual decay is less informative and suggests the sector condition may not hold cleanly.

**General nonstationarity caveat.** All estimators assume approximate stationarity over the estimation window. If the environment is changing during estimation, the estimates characterize the *average* dynamics over that window, not instantaneous values. Use sliding windows matched to the expected stationarity timescale. When environment regime changes are suspected (TF-10), re-estimate from post-change data only.

## B.6 Decision-Theoretic Procedures

The estimators above support three operational decision procedures.

### B.6.1 Estimating $\lambda$ (Exploration Price)

The exploration weight $\lambda(M_t)$ in TF-08's unified policy objective prices information in value-equivalent terms. In domains with sufficient structure, $\lambda$ is derivable:

| Context | $\lambda$ estimator | Source |
|---------|--------------------|--------|
| Finite bandits | Gittins index from dynamic programming | Exact (Gittins 1979) |
| Linear-Gaussian | Probing cost in quadratic objective | Exact (dual control) |
| Discrete MDP | $(\text{VoI})^2 / \text{info gain}$ | Information-directed sampling (Russo & Van Roy) |
| General | $\hat{\lambda} = c \cdot \hat{U}_M / \hat{U}_o$ | Heuristic: scale CIY weight by relative uncertainty |

For the heuristic: when $U_M \gg U_o$ (highly uncertain model), exploration is cheap relative to exploitation risk, so $\lambda$ should be large. When $U_M \ll U_o$ (confident model, noisy observations), exploitation dominates. The constant $c$ is domain-specific and should be calibrated by held-out performance.

### B.6.2 Deliberation Stopping Policy

From Proposition 9.1 (TF-09), deliberation of duration $\Delta\tau$ is warranted when $\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| > \rho_{\text{delib}} \cdot \Delta\tau$. Operationally:

1. Estimate $\rho_{\text{delib}}$ from prior pause windows (B.2.2).
2. Before each deliberation episode, estimate $\|\delta_{\text{post}}\|$ as current mismatch + $\rho_{\text{delib}} \cdot \Delta\tau_{\text{planned}}$.
3. Estimate $\Delta\eta^*(\Delta\tau)$ from the diminishing-returns profile of past deliberation episodes (or from the marginal improvement of the first few candidate actions evaluated).
4. Stop deliberating when the marginal improvement rate $\partial \Delta\eta^* / \partial \Delta\tau$ drops below $\rho_{\text{delib}} / \|\delta_{\text{post}}\|$ (the first-order optimality condition from TF-09).

### B.6.3 Structural-Switch Trigger

From Proposition 10.1 (TF-10), structural adaptation is indicated when parametric convergence leaves a mismatch floor. Operationally, the switching decision balances expected mismatch reduction against transition cost:

1. Estimate the current mismatch floor $\|\delta\|_{\text{floor}}$ from the converged residual statistics.
2. Estimate the post-switch expected mismatch as $\|\delta\|_{\text{new}} \approx \rho / \alpha'$ where $\alpha'$ is the sector bound under the candidate new model class (may need pilot estimation).
3. Estimate transition cost $C_{\text{switch}}$: knowledge loss (parameters that don't transfer), retraining time ($\Delta\tau_{\text{switch}}$), and accumulated mismatch during transition ($\rho \cdot \Delta\tau_{\text{switch}}$).
4. Switch when: $(\|\delta\|_{\text{floor}} - \|\delta\|_{\text{new}}) \cdot T_{\text{horizon}} > C_{\text{switch}}$, where $T_{\text{horizon}}$ is the expected time the new model class will remain adequate.
