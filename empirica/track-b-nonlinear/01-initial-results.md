# Track B Nonlinear Simulations: Initial Results

## What ran

Both simulations completed successfully with no errors (only a benign matplotlib
warning about the non-interactive Agg backend).

- **sim1_nonlinear_mismatch.py** -- Single-agent mismatch dynamics under 5
  correction functions (linear, saturating, threshold/dead-zone, sigmoid,
  structural breakdown). 200 Monte Carlo trials, 10k steps each. All 5 metrics
  (M1--M5) completed.

- **sim2_adversarial_coupling.py** -- Two adversarially coupled agents, testing
  whether the squared tempo advantage (Corollary 11.2) survives nonlinearity.
  200 trials, 20k steps. All 6 metrics (M1--M6) completed.

## Key numerical findings

### Sim 1: Single-agent steady-state mismatch at rho/T = 1.0

| Correction     | Median |delta| | [P10, P90]           |
|----------------|:------:|:----------------------:|
| Linear         | 0.1823 | [0.1773, 0.1880]      |
| Saturating     | 0.2122 | [0.2045, 0.2220]      |
| Threshold      | 0.1850 | [0.1800, 0.1907]      |
| Sigmoid        | 0.1860 | [0.1807, 0.1925]      |
| Breakdown      | 0.1823 | [0.1773, 0.1880]      |

The continuous-ODE prediction (rho/T = 1.0) overestimates the simulated
discrete-time steady state (~0.18) by roughly 5x. The exact discrete-time AR(1)
formula matches well. Saturating correction shows the largest uplift in
steady-state mismatch (~16% above linear), as expected from bounded correction
force.

### Sim 2: Does the squared tempo advantage survive nonlinearity?

**No. The squared exponent does NOT survive.** This is the headline finding.

Corollary 11.2 predicts exponent b = 2.0. Measured exponents:

| Correction     | Exponent b | 95% CI           | Interpretation      |
|----------------|:----------:|:----------------:|:--------------------|
| Linear         | 1.053      | [1.027, 1.079]   | Weakly superlinear  |
| Saturating     | 1.252      | [1.213, 1.292]   | Weakly superlinear  |
| Threshold      | 1.012      | [0.988, 1.037]   | Essentially linear  |
| Sigmoid        | 1.133      | [1.095, 1.170]   | Weakly superlinear  |
| Breakdown      | 1.241      | [1.046, 1.437]   | Weakly superlinear  |

Even the **linear** correction function gives b ~ 1.05, not 2.0. All five
correction types cluster between 1.0 and 1.3 -- far below the predicted squared
advantage.

### R-sweep (saturating correction): exponent vs saturation radius

As R increases (nonlinearity weakens), the exponent rises but converges toward
~1.06, not 2.0:

- R = 0.32: b = 1.555 (strongest nonlinearity tested)
- R = 1.0:  b = 1.234
- R = 31.6: b = 1.059 (nearly linear regime)

The exponent does NOT converge to 2.0 even at R = 31.62, which is essentially
the linear limit for the parameter ranges tested. This suggests the discrepancy
is not a nonlinearity artifact -- the coupling model itself (noise-variance
coupling at these parameter values) does not produce the squared law in the
discrete-time simulation.

## Figures produced

### Sim 1 (5 figures + 1 NPZ)
- `sim1_fig1_steadystate.png` -- Steady-state |delta| vs rho/T (log-log), all 5 corrections
- `sim1_fig2_convergence.png` -- Convergence from delta_0=5.0
- `sim1_fig3_persistence.png` -- Persistence fraction vs rho/T
- `sim1_fig4_distribution.png` -- Mismatch histograms at steady state (5 panels)
- `sim1_fig5_phaseportrait.png` -- Deterministic correction flow phase portrait
- `sim1_results.npz` -- All numerical data

### Sim 2 (6 figures + 1 NPZ)
- `sim2_fig1_ratio_vs_tempo.png` -- Mismatch ratio vs tempo ratio (the key plot)
- `sim2_fig2_exponents.png` -- Bar chart of effective exponents
- `sim2_fig3_gamma_asymmetry.png` -- Effect of gamma asymmetry
- `sim2_fig4_collapse.png` -- Catastrophic collapse fractions
- `sim2_fig5_phaseportrait.png` -- Phase portrait of coupled breakdown dynamics
- `sim2_fig6_exponent_vs_R.png` -- Exponent vs saturation radius R
- `sim2_results.npz` -- All numerical data

## Surprises and anomalies

1. **The biggest surprise: even linear correction gives exponent ~1.05, not 2.0.**
   The squared law from Corollary 11.2 is a continuous-time, coupling-dominant
   approximation. At these parameter values (T_B = 0.1, q_base = 0.05,
   gamma = 0.5), the base noise q_base is not negligible compared to the
   adversarial coupling term gamma*T, so the coupling-dominant regime is not
   fully reached. Additionally, the discrete-time AR(1) dynamics differ from the
   continuous ODE. The exact discrete-time linear prediction (dotted line in
   sim2_fig1) tracks the linear simulation closely, confirming the simulation is
   correct -- the issue is that the continuous-ODE squared law doesn't apply at
   these parameters.

2. **Saturating and sigmoid corrections actually show *higher* exponents than
   linear** (1.25 and 1.13 vs 1.05). This is counterintuitive -- nonlinearity
   appears to slightly amplify the tempo advantage rather than suppress it. This
   may be because saturation limits the correction of the faster agent less (its
   mismatch stays small, in the linear regime of the saturation curve), while the
   slower agent's larger mismatch gets clipped by saturation.

3. **Threshold (dead-zone) correction has the lowest exponent** (~1.01), nearly
   pure linear. The dead zone hurts the slow agent (large mismatches still get
   full correction) and the fast agent equally (small mismatches fall in the dead
   zone), roughly canceling out.

4. **No catastrophic collapse observed** at the tested parameter range for
   linear, saturating, sigmoid, or threshold corrections. Only the structural
   breakdown correction shows collapse at high tempo ratios, as expected from
   Proposition A.3. The predicted collapse threshold ratio is ~0.7, and collapse
   onset is visible in the sim2_fig4 plot.

5. **The R-sweep is the most diagnostic result.** Even at R = 31.62 (effectively
   linear), the exponent is only 1.059. To recover the theoretical exponent of
   2.0, one would likely need to either (a) decrease q_base to make the coupling
   truly dominant, or (b) decrease eta (T) to approach the continuous-time limit,
   or (c) both. This points to a regime-validity question for Corollary 11.2.
