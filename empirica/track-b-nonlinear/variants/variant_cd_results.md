# Variants C & D Results: Regime Testing for the Squared Tempo Advantage

## Executive Summary

The squared tempo advantage (exponent b = 2.0, Corollary 11.2) **does not emerge in any parameter regime** for the stochastic simulation. The maximum achievable exponent for the discrete stochastic (AR(1)) model is **b = 1.5**, not 2.0. This is not a discretization artifact that vanishes as eta approaches 0 -- it is a fundamental difference between the deterministic ODE and the stochastic process.

The continuous-ODE prediction (which *does* reach b = 2.0 in the coupling-dominant limit) is the wrong reference model for stochastic dynamics with zero-mean noise. The root cause is identified analytically below.

## What Was Tested

- **Variant C**: Swept eta (= T_B) from 0.1 down to 0.001, measuring the effective exponent. Tests whether the continuous-time ODE limit recovers the squared law.
- **Variant D**: Swept q_base from 0.1 down to 0.0001 at eta = 0.01, measuring the effective exponent. Tests whether the coupling-dominant regime recovers the squared law.
- **Deep regime**: Both eta = 0.001 AND q_base = 0.001 simultaneously.
- **2D analytical sweep**: Computed the exact discrete and continuous predictions across a grid of (eta, q_base) to map the full exponent landscape.

All tests used the **linear** correction function only, isolating the regime effect from nonlinearity.

## Key Numerical Results

### Variant C: Exponent vs eta

| eta    | Simulation | Discrete AR(1) | Continuous ODE |
|--------|:----------:|:--------------:|:--------------:|
| 0.1000 |     1.052  |        1.053   |        1.605   |
| 0.0500 |     0.918  |        0.921   |        1.446   |
| 0.0200 |     0.744  |        0.744   |        1.254   |
| 0.0100 |     0.645  |        0.645   |        1.149   |
| 0.0050 |     0.584  |        0.580   |        1.082   |
| 0.0020 |     0.533  |        0.534   |        1.035   |
| 0.0010 |     0.506  |        0.517   |        1.018   |

**Surprise**: As eta decreases, the exponent **drops toward 0.5**, not rises toward 2.0. The simulation matches the discrete AR(1) prediction exactly. The continuous ODE prediction drops toward 1.0 (it would reach 2.0 only in the coupling-dominant limit, which is not met at q_base = 0.05).

### Variant D: Exponent vs q_base

| q_base  | gamma*T/q | Simulation | Discrete AR(1) | Continuous ODE |
|---------|:---------:|:----------:|:--------------:|:--------------:|
| 0.1000  |     0.05  |     0.573  |        0.577   |        1.082   |
| 0.0500  |     0.10  |     0.640  |        0.645   |        1.149   |
| 0.0200  |     0.25  |     0.786  |        0.791   |        1.296   |
| 0.0100  |     0.50  |     0.936  |        0.941   |        1.446   |
| 0.0050  |     1.00  |     1.096  |        1.101   |        1.605   |
| 0.0020  |     2.50  |     1.275  |        1.280   |        1.784   |
| 0.0010  |     5.00  |     1.367  |        1.372   |        1.876   |
| 0.0001  |    50.00  |     1.476  |        1.481   |        1.986   |

**This is the key result.** As q_base approaches 0 (coupling dominance increases):

- The **continuous ODE exponent approaches 2.0** (reaching 1.986 at q_base = 0.0001). This confirms Corollary 11.2 is correct *for the ODE model*.
- The **discrete AR(1) exponent approaches 1.5** (reaching 1.481 at q_base = 0.0001). This is the stochastic model's asymptote.
- The **simulation matches the discrete AR(1)** prediction precisely, confirming the code is correct.

### 2D Analytical Sweep

- Discrete AR(1) exponent range: [0.502, 1.483] -- never exceeds 1.5
- Continuous ODE exponent range: [1.003, 2.000] -- reaches 2.0

## Root Cause Analysis

The discrepancy is **not** a discretization artifact, a finite-time effect, or a statistical noise issue. It is a fundamental difference between deterministic and stochastic steady states.

### The deterministic ODE model

The mismatch ODE d|delta|/dt = -T * |delta| + rho has steady state:

    |delta|_ss = rho / T

This scales as 1/T. The mismatch ratio becomes:

    ||delta_B|| / ||delta_A|| = (rho_B / T_B) / (rho_A / T_A)
                              = (rho_B / rho_A) * (T_A / T_B)

In the coupling-dominant limit (rho_B/rho_A -> T_A/T_B):

    ratio -> (T_A/T_B)^2    [exponent 2]

### The stochastic AR(1) model

The discrete process delta_{t+1} = (1-T) * delta_t + w_t with w_t ~ N(0, rho^2) has stationary variance:

    Var[delta] = rho^2 / (1 - (1-T)^2) = rho^2 / (2T - T^2)

For small T: Var[delta] ~ rho^2 / (2T), so:

    E[|delta|] ~ rho / sqrt(T)     (not rho / T)

This scales as 1/sqrt(T), not 1/T. The mismatch ratio becomes:

    ||delta_B|| / ||delta_A|| = (rho_B / sqrt(T_B)) / (rho_A / sqrt(T_A))
                              = (rho_B / rho_A) * sqrt(T_A / T_B)

In the coupling-dominant limit:

    ratio -> (T_A/T_B) * sqrt(T_A/T_B) = (T_A/T_B)^{3/2}    [exponent 1.5]

### Why they differ

The ODE d|delta|/dt = -T*|delta| + rho describes the evolution of the *expected* mismatch magnitude when rho is a deterministic drift (or a constant positive disturbance rate). In this case, |delta| converges to a fixed point rho/T.

But in the stochastic model, the noise w_t is zero-mean Gaussian. The *expected* delta is zero (it fluctuates symmetrically around the target). What we measure is E[|delta|], which scales with the standard deviation of the stationary distribution, not with the mean. The variance of an AR(1) process scales as rho^2 / T (not rho^2 / T^2), giving the sqrt(T) dependence.

The ODE model conflates two different things:
1. **Bias under persistent drift**: if the environment drifts deterministically at rate rho, the steady-state tracking error is rho/T. This gives exponent 2.
2. **RMS fluctuation under stochastic noise**: if the environment fluctuates stochastically with noise scale rho, the steady-state RMS error is rho/sqrt(2T). This gives exponent 1.5.

These are fundamentally different physical situations. Corollary 11.2's squared law is correct for case (1) but not case (2).

### Crossover in the existing sims

In Variant C, as eta decreases with q_base fixed, the coupling term gamma*T shrinks relative to q_base, moving *away* from coupling dominance. This explains why the exponent drops toward 0.5 (the non-coupled limit where rho_A ~ rho_B ~ q_base and only the sqrt(T_A/T_B) factor remains).

In Variant D, decreasing q_base increases coupling dominance, and the exponent rises from ~0.5 toward the stochastic asymptote of 1.5.

At the original sim2 parameters (eta=0.1, q_base=0.05), the exponent is ~1.05, which happens to be in the crossover zone between these limits.

## Implications for TF-11

### What Corollary 11.2 gets right

- The *qualitative* prediction is correct: tempo advantage is superlinear (exponent > 1 in the coupling-dominant regime)
- The coupling-dominant condition (gamma*T >> q_base) is correctly identified as necessary
- Under deterministic persistent drift, the squared law (exponent 2) is exact

### What needs correction

- The squared law (exponent 2) applies to the **deterministic ODE** model, not to the **stochastic** model
- For zero-mean stochastic disturbances (the more common case), the asymptotic exponent is **1.5**, not 2.0
- The mismatch dynamics equation d|delta|/dt = -T*|delta| + rho is ambiguous about whether rho represents deterministic drift or stochastic noise scale -- these give different steady-state scaling

### Suggested caveat for TF-11

Corollary 11.2 should note that the squared exponent (b=2) holds when rho represents a *persistent directional disturbance rate* (deterministic drift). When environmental change is stochastic (zero-mean perturbations with scale rho), the mismatch ratio scales as (T_A/T_B)^{3/2} in the coupling-dominant regime. The general case interpolates between these depending on the drift-to-diffusion ratio of the disturbance.

## Figures

- `variant_c_exponent_vs_eta.png` -- Exponent vs eta (Variant C)
- `variant_d_exponent_vs_qbase.png` -- Exponent vs q_base (Variant D)
- `variant_cd_2d_heatmap.png` -- 2D heatmap of analytical exponents over (eta, q_base)
- `variant_cd_ratio_comparison.png` -- Mismatch ratio vs tempo ratio for three parameter sets
- `variant_cd_results.npz` -- All numerical data

## Code

`variant_cd_regimes.py` -- Self-contained script importing only g_linear from the parent sim1. Uses parameter dataclasses, analytical predictions alongside simulations, and matplotlib Agg backend.
