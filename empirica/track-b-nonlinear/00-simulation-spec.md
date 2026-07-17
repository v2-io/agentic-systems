# Simulation Specification: Nonlinear Mismatch Dynamics in TFT

**Status**: Specification for implementation. Targets TF-11 Open Question #1 and the
robustness of Corollary 11.2 (squared tempo advantage).

**Goal**: Determine how far TFT's quantitative predictions depend on the linear
mismatch ODE, and whether the qualitative results (persistence threshold, tempo
advantage) survive realistic nonlinearities.

---

## Background and Motivation

TFT's mismatch dynamics equation (TF-11) is:

    d||delta||/dt = -T * ||delta|| + rho(t)

This is explicitly labeled a *hypothesis* -- a first-order linear approximation. It
yields two key quantitative results:

1. **Steady-state mismatch**: ||delta||_ss = rho / T
2. **Squared tempo advantage** (Corollary 11.2): ||delta_B||_ss / ||delta_A||_ss = (gamma_A / gamma_B) * (T_A / T_B)^2

Both depend on linearity. Appendix A proves that *qualitative* results (persistence
threshold exists, tempo advantage exists, bounded mismatch under sector condition)
hold without linearity. The question is: how do the *quantitative* results change
under plausible nonlinearities?

### What would constitute a surprising result

- **Confirming**: Nonlinear steady-state mismatch deviates from rho/T by a
  multiplicative constant but preserves the scaling structure. The squared exponent
  in adversarial dynamics drops slightly (e.g., to 1.7-1.9) but remains superlinear.
  This would mean TFT's linear results are good approximations and the theory's
  quantitative claims need only minor caveats.

- **Surprising (positive)**: The squared relationship holds even under strong
  nonlinearities. This would suggest the result is more robust than the derivation
  implies -- perhaps there is a deeper reason for the exponent being 2.

- **Surprising (negative)**: Under saturating correction, the adversarial exponent
  drops to 1 or below (merely linear or sublinear advantage). This would mean TFT's
  most striking quantitative result is a linear artifact, and the adversarial
  dynamics section of TF-11 needs significant revision.

- **Surprising (structural)**: Nonlinear dynamics produce qualitatively new phenomena
  not present in the linear model -- bistability, limit cycles, chaotic mismatch
  oscillations, or sharp phase transitions. This would indicate TFT's current
  framework is missing important dynamical features.

---

## Simulation 1: Nonlinear Mismatch Dynamics (Single Agent)

### Purpose

Test how the steady-state mismatch, convergence rate, persistence threshold, and
mismatch distribution depend on the form of the correction function g(delta).

### Environment Model

A scalar environment state x_t following a discretized random walk:

    x_{t+1} = x_t + w_t

where w_t ~ N(0, q^2) is i.i.d. Gaussian noise with variance q^2. The parameter q
controls the environment change rate rho: since rho is the expected magnitude of
environmental change per unit time, we have rho = q (more precisely, rho = q *
sqrt(2/pi) for the expected absolute value, but the proportionality is what matters;
we can calibrate empirically).

### Agent Model

The agent maintains a scalar estimate x_hat_t and updates it each timestep:

    delta_t = x_t - x_hat_t            (mismatch: reality minus estimate)
    x_hat_{t+1} = x_hat_t + eta * g(delta_t)    (correction step)

where:
- eta is the update gain (related to T via T = nu * eta, and with nu = 1
  event/timestep, we have T = eta)
- g(.) is the correction function (the nonlinearity under investigation)

The mismatch evolves as:

    delta_{t+1} = x_{t+1} - x_hat_{t+1}
               = (x_t + w_t) - (x_hat_t + eta * g(delta_t))
               = delta_t - eta * g(delta_t) + w_t

In the continuous limit (small eta, many steps), the expected dynamics are:

    d||delta||/dt approx -eta * g'(0) * ||delta|| + rho

which matches TF-11's ODE when g is linear (g'(0) = 1, so T = eta).

### Correction Functions

Each function g: R -> R maps mismatch to correction signal. All satisfy g(0) = 0
and g'(0) = 1 (so that near zero mismatch, all functions behave linearly -- the
Taylor-approximation regime where TFT's linear ODE is valid).

**1. Linear (baseline)**

    g(delta) = delta

TFT's current assumption. The correction is proportional to mismatch at all scales.
Expected steady-state: ||delta||_ss = rho / T = q / eta.

**2. Saturating**

    g(delta) = delta / (1 + |delta| / R)

where R > 0 is the saturation radius. For |delta| << R, this is approximately delta
(linear regime). For |delta| >> R, this approaches R * sign(delta) -- the correction
is bounded regardless of how large the mismatch grows.

Physical motivation: The agent's update mechanism has finite capacity. A Kalman filter
with a fixed gain cannot make arbitrarily large corrections. A developer can only
process so much new information per session. A control system has actuator limits.

Expected behavior: Higher steady-state mismatch than linear prediction, because
correction is weaker at large delta. The persistence threshold is *harder* to satisfy
(the agent fails at a lower rho than the linear theory predicts). Specifically, the
effective T decreases as mismatch grows, so the agent needs more raw adaptive capacity
to maintain the same steady-state performance.

The steady-state condition delta = eta * g(delta) + w in expectation gives:
    E[|delta|] = q / (eta * effective_slope)
where effective_slope < 1 when |delta| is significant relative to R.

**3. Threshold (dead zone)**

    g(delta) = delta * 1[|delta| > epsilon]

where epsilon > 0 is the detection threshold. Mismatches smaller than epsilon go
entirely uncorrected.

Physical motivation: Agents with finite resolution ignore small discrepancies.
Developers don't fix trivial naming inconsistencies. PID controllers have dead bands.
Organisms don't respond to stimuli below detection threshold.

Expected behavior: Mismatch drifts freely within the dead zone, creating a minimum
steady-state mismatch of approximately epsilon (even when rho is small). The mismatch
distribution has a characteristic shape: concentrated near epsilon with a tail toward
larger values. The persistence threshold is unchanged for large rho (the dead zone
is irrelevant when mismatch is large) but creates an irreducible floor at small rho.

**4. Sigmoid (smooth saturation)**

    g(delta) = R * tanh(delta / R)

where R > 0 is the saturation scale. This combines the saturation of function 2 with
smoothness everywhere. For |delta| << R, tanh(delta/R) approx delta/R, so
g(delta) approx delta (linear). For |delta| >> R, g(delta) approx R * sign(delta)
(saturated).

Physical motivation: Many biological and neural response functions are sigmoidal.
This is the most "generic" smooth nonlinearity.

Expected behavior: Qualitatively similar to the saturating function, but smoother
transitions. The steady-state mismatch should be between the linear and saturating
predictions.

**5. Structural breakdown**

    g(delta) = delta * 1[|delta| < R_max]

where R_max > 0 is the model-class capacity. When mismatch exceeds R_max, the
correction function drops to zero -- the agent's model is so wrong that its update
mechanism cannot function (the model class is inadequate for the current state of
reality).

Physical motivation: This is TF-10's structural adaptation regime. A Kalman filter
linearized around the wrong operating point produces garbage updates. An organism
with the wrong behavioral repertoire cannot adapt parametrically. A developer
working from a fundamentally wrong architectural understanding makes changes that
don't help.

Expected behavior: A sharp phase transition. For rho < T * R_max (approximately),
the agent maintains bounded mismatch in the linear regime. For rho > T * R_max, the
agent occasionally gets pushed past R_max, correction shuts down, mismatch grows
further (positive feedback), and the agent diverges. This should manifest as a
bimodal mismatch distribution near the critical rho: sometimes the agent stays bounded,
sometimes it escapes. Above the critical rho, divergence is certain.

This directly validates Appendix A's Proposition A.1: the persistence condition
alpha > rho/R corresponds here to eta > q/R_max, or equivalently T > rho/R_max.

### Parameter Space

The simulations sweep over the following parameters:

| Parameter | Symbol | Default | Sweep Range | Role |
|-----------|--------|---------|-------------|------|
| Update gain | eta | 0.1 | [0.01, 0.5] | Controls T (= eta with nu=1) |
| Env noise std | q | 0.1 | [0.01, 1.0] | Controls rho |
| Saturation radius | R | 1.0 | [0.1, 10.0] | Scale of nonlinearity |
| Dead zone threshold | epsilon | 0.1 | [0.01, 1.0] | Detection threshold |
| Breakdown radius | R_max | 2.0 | [0.5, 10.0] | Model class capacity |
| Number of timesteps | num_steps | 10000 | -- | Simulation length |
| Number of trials | num_trials | 200 | -- | Monte Carlo replicates |
| Burn-in period | burn_in | 2000 | -- | Steps to discard for steady-state |
| Random seed | seed | 42 | -- | Reproducibility |

The key independent variable is the ratio rho/T = q/eta. The linear theory predicts
||delta||_ss = rho/T = q/eta regardless of the absolute values.

### Measurements and Outputs

**M1. Steady-state mismatch vs rho/T**

For each correction function and each (q, eta) pair:
- Run num_trials independent simulations of num_steps each
- Discard the first burn_in steps
- Compute mean |delta| over the remaining steps for each trial
- Report the median and [10th, 90th] percentile across trials

Plot: ||delta||_ss (y-axis) vs q/eta (x-axis) for all five correction functions on
the same axes. Overlay the linear prediction ||delta||_ss = q/eta as a reference line.
Use log-log axes to reveal power-law structure.

**M2. Convergence rate from initial conditions**

For each correction function:
- Start with delta_0 = 5.0 (well above expected steady state)
- Set q = 0.1, eta = 0.1 (so rho/T = 1.0)
- Track mean |delta_t| across trials as a function of t
- Fit an exponential decay to the initial transient: |delta_t| ~ A * exp(-lambda * t)
  + ||delta||_ss

Plot: |delta_t| vs t for all correction functions. The linear case should show
lambda = eta = T. Saturating/sigmoid cases should show slower convergence when
starting from large mismatch.

**M3. Persistence threshold**

For each correction function:
- Fix eta = 0.1
- Sweep q from 0.01 to 2.0 (so rho/T from 0.1 to 20)
- For each q, determine whether the agent "persists" (|delta_t| remains bounded)
  or "diverges" (|delta_t| grows without bound or exceeds 100 * R_max)
- For the structural breakdown case, measure the fraction of trials that diverge
  at each q

Plot: Fraction of persistent trials vs q/eta. The linear case should show 100%
persistence at all finite q/eta (since the linear ODE always has a bounded steady
state). The structural breakdown case should show a sharp drop at q/eta approx R_max.
The saturating case should show a gradual increase in mean mismatch (always bounded
but growing nonlinearly with q/eta).

**M4. Mismatch distribution**

For each correction function at q/eta = 1.0:
- Collect the distribution of |delta_t| across all (post-burn-in) timesteps and
  all trials

Plot: Histogram / KDE of |delta| for each correction function. The linear case
should be approximately half-normal (the stationary law for |x| where x is
Ornstein-Uhlenbeck; NOT exponential as previously stated). The threshold case should show a concentration near epsilon. The
structural breakdown case should show bimodality near the critical rho.

**M5. Phase portraits**

For each correction function:
- Plot the deterministic flow: d(delta)/dt = -eta * g(delta) as a function of delta
  (this is the correction component only, without noise)
- Overlay the noise magnitude q to show where stochastic effects dominate
- For the structural breakdown case, show the basin of attraction boundary

Plot: d(delta)/dt vs delta for each correction function, with horizontal lines at
+/- q showing the noise scale.

### Output Format

All numerical results are saved as:
- NPZ file: `sim1_results.npz` containing arrays for each measurement
- CSV files: `sim1_steadystate.csv`, `sim1_convergence.csv` for tabular data
- Figures: `sim1_fig1_steadystate.png`, `sim1_fig2_convergence.png`, etc.

---

## Simulation 2: Adversarial Coupling (Two Agents)

### Purpose

Test whether the squared tempo advantage (Corollary 11.2) holds beyond the linear
regime.

### Model

Two agents A and B, each tracking its own drifting scalar target:

    x_A_{t+1} = x_A_t + w_A_t
    x_B_{t+1} = x_B_t + w_B_t

where the noise variances encode the adversarial coupling:

    Var(w_B_t) = q_base^2 + (gamma_A * T_A)^2
    Var(w_A_t) = q_base^2 + (gamma_B * T_B)^2

Here gamma_A * T_A represents the disruption that A's adaptive tempo imposes on B's
environment, and vice versa. (Using variance rather than standard deviation for the
coupling follows from the independence of base noise and adversarial disruption;
alternatively, we can use additive standard deviations -- both are tested.)

**Coupling model justification**: In TF-11, the coupling is rho_B = rho_base +
gamma_A * T_A. Since rho corresponds to the noise standard deviation (expected
absolute change per step), the more direct implementation is:

    rho_B = q_base + gamma_A * T_A    (additive std coupling)

This is the primary coupling model. The variance-additive version is a secondary
check.

Each agent updates its estimate independently:

    delta_A_t = x_A_t - x_hat_A_t
    x_hat_A_{t+1} = x_hat_A_t + eta_A * g(delta_A_t)

    delta_B_t = x_B_t - x_hat_B_t
    x_hat_B_{t+1} = x_hat_B_t + eta_B * g(delta_B_t)

with T_A = eta_A, T_B = eta_B (since nu = 1 for both).

### Theoretical Prediction

Under linear correction (g = identity) and additive std coupling:

    rho_B = q_base + gamma_A * T_A
    rho_A = q_base + gamma_B * T_B

    ||delta_B||_ss = rho_B / T_B = (q_base + gamma_A * T_A) / T_B
    ||delta_A||_ss = rho_A / T_A = (q_base + gamma_B * T_B) / T_A

When adversarial coupling dominates (gamma * T >> q_base):

    ||delta_B||_ss / ||delta_A||_ss
        approx (gamma_A * T_A / T_B) / (gamma_B * T_B / T_A)
        = (gamma_A / gamma_B) * (T_A / T_B)^2

This is Corollary 11.2's squared tempo advantage.

### Parameter Space

| Parameter | Symbol | Default | Sweep Range | Role |
|-----------|--------|---------|-------------|------|
| Tempo A | T_A (= eta_A) | 0.1 | [0.05, 0.5] | A's adaptive tempo |
| Tempo B | T_B (= eta_B) | 0.1 | [0.05, 0.5] | B's adaptive tempo |
| T_A / T_B ratio | r | 1.0 | [0.5, 5.0] | Primary sweep variable |
| Coupling A | gamma_A | 0.5 | [0.1, 2.0] | A's disruption effectiveness |
| Coupling B | gamma_B | 0.5 | [0.1, 2.0] | B's disruption effectiveness |
| gamma_A / gamma_B ratio | -- | 1.0 | [0.5, 2.0] | Asymmetry parameter |
| Base noise | q_base | 0.05 | [0.01, 0.2] | Non-adversarial disturbance |
| Correction function | g | linear | all 5 | The nonlinearity |
| Nonlinearity parameters | R, eps, R_max | 1.0, 0.1, 2.0 | varied | As in Sim 1 |
| Timesteps | num_steps | 20000 | -- | Longer for coupled convergence |
| Trials | num_trials | 200 | -- | Monte Carlo replicates |
| Burn-in | burn_in | 5000 | -- | Longer burn-in for coupling |
| Random seed | seed | 42 | -- | Reproducibility |

The primary sweep is over T_A/T_B with T_B fixed. For each ratio, T_A = r * T_B.

### Measurements and Outputs

**M1. Mismatch ratio vs tempo ratio (the key plot)**

For each correction function:
- Fix T_B = 0.1, gamma_A = gamma_B = 0.5, q_base = 0.05
- Sweep T_A/T_B from 0.5 to 5.0 (about 20 points, log-spaced)
- For each ratio, run num_trials simulations, compute steady-state ||delta_B||/||delta_A||
- Plot on log-log axes: mismatch ratio (y) vs tempo ratio (x)
- Overlay the theoretical prediction: (gamma_A/gamma_B) * (T_A/T_B)^2

On log-log axes, the squared relationship appears as a line with slope 2. The actual
slope is the key measurement -- it tells us the *effective exponent* under each
nonlinearity.

**M2. Effective exponent estimation**

For each correction function:
- Fit log(mismatch_ratio) = a + b * log(T_A/T_B) via least squares
- Report b (the effective exponent) with confidence interval
- Under linear correction, b should be 2.0
- Under nonlinear correction, b < 2 is expected for saturating functions

Create a summary table:

| Correction Function | Effective Exponent b | 95% CI | Deviation from 2 |
|---------------------|---------------------|--------|-------------------|

**M3. Effect of gamma asymmetry**

For T_A/T_B = 2.0 (moderate tempo advantage):
- Sweep gamma_A/gamma_B from 0.5 to 2.0
- Measure how the mismatch ratio depends on coupling asymmetry
- Compare to the linear prediction: ratio should be proportional to gamma_A/gamma_B

**M4. Catastrophic collapse threshold (structural breakdown only)**

For the structural breakdown correction function:
- Fix T_B = 0.1, gamma_A = gamma_B = 0.5, R_max = 2.0
- Sweep T_A/T_B from 0.5 to 5.0
- For each ratio, measure the fraction of trials where B diverges (|delta_B| > 10 * R_max)
- Identify the critical T_A/T_B ratio where B transitions from stable to divergent

This tests Appendix A, Proposition A.3: Agent A destabilizes B when
gamma_A * T_A > Delta_rho_B* = alpha_B * R_B - rho_B_base. With alpha_B = T_B = 0.1,
R_B = R_max = 2.0, rho_B_base = q_base = 0.05, we get
Delta_rho_B* = 0.1 * 2.0 - 0.05 = 0.15. Destabilization requires
gamma_A * T_A > 0.15, i.e., T_A > 0.3, i.e., T_A/T_B > 3.0. The simulation should
show a sharp transition near this ratio.

**M5. Phase portrait of coupled system**

For the structural breakdown case at T_A/T_B = 3.0 (near the critical ratio):
- Plot representative trajectories in (|delta_A|, |delta_B|) space
- Show the basin of attraction boundary
- Illustrate the effects spiral (Corollary A.3.1) when B is pushed past R_max

**M6. Sensitivity to nonlinearity parameters**

For the saturating correction function:
- Fix T_A/T_B = 2.0, gamma_A = gamma_B = 0.5
- Sweep R (saturation radius) from 0.1 to 10.0
- Measure the effective exponent at each R
- The exponent should approach 1.5 as R -> infinity (stochastic coupling limit;
  2.0 only under deterministic drift — see variant C/D results) and decrease as
  R -> 0 (strongly saturating limit)

Plot: Effective exponent b vs R. This characterizes how "much" nonlinearity is needed
to break the squared relationship.

### Output Format

All numerical results are saved as:
- NPZ file: `sim2_results.npz` containing arrays for each measurement
- CSV files: `sim2_exponents.csv`, `sim2_collapse.csv` for tabular data
- Figures: `sim2_fig1_ratio_vs_tempo.png`, `sim2_fig2_exponents.png`, etc.

---

## Implementation Notes

### Discrete-Time Considerations

The theory is formulated in continuous time but the simulations are discrete. With
dt = 1 (one event per timestep) and eta playing the role of T (since nu = 1), the
discrete dynamics are:

    delta_{t+1} = delta_t - eta * g(delta_t) + w_t

This is an Euler discretization of:

    d(delta)/dt = -eta * g(delta) + w(t)

**Exact discrete-time steady state.** For the linear case g(delta) = delta, the
discrete dynamics are an AR(1) process: delta_{t+1} = (1-eta)*delta_t + w_t. The
exact stationary standard deviation is q / sqrt(2*eta - eta^2), and the expected
absolute mismatch is E[|delta|] = q * sqrt(2/pi) / sqrt(2*eta - eta^2). This
differs from the continuous-ODE prediction rho/T = q/eta by a factor of
eta * sqrt(2/pi) / sqrt(2*eta - eta^2). For small eta (the regime where TF-11's
continuous approximation is valid), this factor approaches sqrt(1/pi) ~ 0.564, so
the continuous ODE overestimates E[|delta|] by about 77%. The simulations use the
exact discrete-time formula as the reference line for the linear case; the
continuous-ODE prediction is shown separately for comparison.

The key point: the **ratio** of mismatch between correction functions (or between
agents in Sim 2) is the quantity of interest, and these ratios are relatively
insensitive to the discrete-vs-continuous distinction. The squared tempo advantage
exponent in particular depends on the ratio structure, not the absolute values.

The discretization is valid when eta << 1 (small gain regime), which is the same
condition under which TF-11's continuous ODE is valid (see TF-11's bridging
assumption). For eta > 0.5, the discrete dynamics may exhibit oscillations not
present in the continuous ODE; this is noted but not a primary concern since the
theory is designed for the small-gain regime.

### Statistical Methodology

- All simulations use a fixed random seed for reproducibility
- Monte Carlo trials use independent random streams (seed + trial_index)
- Steady-state statistics are computed after discarding a burn-in period
- Confidence intervals are bootstrap percentile intervals (1000 bootstrap samples)
- The effective exponent in Sim 2 is estimated via weighted least squares on
  log-transformed data, with weights inversely proportional to the variance of
  each point's log-estimate

### Computational Considerations

Sim 1: 5 functions x ~20 parameter points x 200 trials x 10000 steps = ~2e8 scalar
operations. Trivially fast in vectorized NumPy (< 1 minute on a laptop).

Sim 2: 5 functions x ~20 ratio points x ~5 gamma points x 200 trials x 20000 steps
= ~2e9 scalar operations. Still fast in vectorized NumPy (< 10 minutes).

No GPU or parallelism needed. The simulations are embarrassingly parallel across
trials if speed becomes a concern.

### Plotting Standards

- All figures use matplotlib with a clean, publication-quality style
- Font size: 12pt for labels, 10pt for tick labels, 14pt for titles
- Colors: colorblind-safe palette (tab10 or similar)
- Log-log axes where power-law relationships are expected
- Error bands showing [10th, 90th] percentile (not just mean)
- Reference lines (theoretical predictions) shown as dashed black
- Each figure saved as PNG (300 dpi) and also displayed if running interactively
- Figure size: 8x6 inches for single panels, 12x8 for multi-panel

---

## Connections to Theory

### What each result means for TFT

| Simulation Result | If Confirming | If Surprising |
|-------------------|---------------|---------------|
| Steady-state scales as rho/T | Linear ODE is good approximation | Need nonlinear correction terms in TF-11 |
| Squared exponent holds | Corollary 11.2 is robust | Adversarial analysis needs revision |
| Sharp collapse at breakdown threshold | Prop A.3 validated quantitatively | Collapse is gradual (Lyapunov overly conservative) |
| Dead zone creates irreducible floor | Confirms threshold effect intuition | Dead zone doesn't matter (noise washes it out) |
| Mismatch distribution is non-trivial | Linear ODE oversimplifies | Or: distribution is simple (exponential) |

### Connections to Appendix A

- The persistence threshold (Prop A.1) is directly testable via Sim 1 M3
- The adaptive reserve (Prop A.2) is testable via Sim 2 M4 (collapse threshold)
- The adversarial destabilization (Prop A.3) is testable via Sim 2 M4 and M5
- The effects spiral (Cor A.3.1) should be visible in Sim 2 M5 phase portraits

### What to report

The key output for a theory paper is a compact summary:

1. A table of effective exponents (does the squared relationship hold?)
2. A figure showing mismatch ratio vs tempo ratio for each correction function
3. The persistence threshold for each correction function (how much harder is it
   under nonlinearity?)
4. Whether any qualitative phenomena (bistability, limit cycles, sharp collapse)
   emerge that the linear theory cannot predict

These results directly inform whether TF-11's quantitative claims need revision,
and if so, in which direction.
