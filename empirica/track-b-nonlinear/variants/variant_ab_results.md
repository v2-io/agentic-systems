# Variant A/B Results: Drift Disturbance Models

## The core question

TF-11 Corollary 11.2 predicts the squared tempo advantage: mismatch ratio scales as (T_A/T_B)^2 under adversarial coupling. The original sim2 found exponent ~1.05 for linear correction. Does the squared advantage appear when the disturbance model matches TF-11's deterministic rho?

## Answer: YES -- the squared advantage is real, and the original sim2's low exponent was an artifact of the coupling mechanism

The original sim2 coupled agents through **noise variance** (rho enters as the std dev of zero-mean Gaussian noise). TF-11's ODE uses rho as a **deterministic drift rate**. These are fundamentally different stochastic models with different scaling behavior. When the coupling mechanism matches the ODE (deterministic drift), the squared exponent emerges cleanly.

## Variant A Results: Deterministic Drift

### Single-agent steady state

With deterministic drift x_{t+1} = x_t + rho and correction xhat_{t+1} = xhat_t + eta * g(delta_t):

| Correction   | Steady-state |delta| | Ratio to rho/eta | Notes |
|-------------|:---------------------:|:----------------:|:------|
| Linear      | 0.5000                | 1.0000           | Exact match to ODE prediction |
| Saturating  | 1.0000                | 2.0000           | Higher: correction saturates at R |
| Threshold   | 0.5000                | 1.0000           | Same as linear (SS above epsilon) |
| Sigmoid     | 0.5493                | 1.0986           | Slightly higher (tanh saturation) |
| Breakdown   | 0.5000                | 1.0000           | Same as linear (SS below R_max) |

The linear steady-state prediction delta_ss = rho/eta is exactly confirmed. This validates that the deterministic drift model IS the correct discrete-time analog of TF-11's ODE.

### Adversarial exponent (standard parameters)

With T_B = 0.1, gamma = 0.5, rho_base = 0.01:

| Correction   | Exponent b | 95% CI              | Notes |
|-------------|:----------:|:-------------------:|:------|
| Linear      | 1.877      | [1.863, 1.890]      | Close to 2.0, depressed by non-negligible rho_base |
| Threshold   | 1.877      | [1.863, 1.890]      | Identical to linear (SS in linear regime of all corrections) |
| Saturating  | 6.854      | [6.434, 7.274]      | **DIVERGENCE ARTIFACT** (see below) |
| Sigmoid     | 6.653      | [5.974, 7.332]      | **DIVERGENCE ARTIFACT** (see below) |
| Breakdown   | 3.763      | [2.601, 4.925]      | **DIVERGENCE ARTIFACT** (see below) |

**Critical finding**: For linear and threshold corrections, the exponent is 1.877 -- very close to 2.0 and far above the original sim2's 1.05. The remaining gap from 2.0 is explained by the non-negligible rho_base (= 0.01, which is 20% of the coupling term gamma*T_B = 0.05).

**Divergence artifact for saturating/sigmoid/breakdown**: Under deterministic drift, when rho_B exceeds T_B * R (the saturating correction's maximum correction rate), the mismatch grows linearly without bound. This is physically correct -- it IS the persistence threshold failure from Proposition 11.1 -- but it makes the "exponent" measurement meaningless for those corrections at these parameters. At high tempo ratios, rho_B = rho_base + gamma*T_A grows while T_B*R stays fixed, so B diverges while A remains stable, producing artificially extreme "exponents".

### Coupling dominance sweep (the definitive test)

Sweeping rho_base from 0.316 (base-dominated) to 0.0001 (coupling-dominated), with linear correction:

| rho_base / (gamma * T_B) | Exponent |
|:-------------------------:|:--------:|
| 6.325                     | 1.213    |
| 2.000                     | 1.445    |
| 1.125                     | 1.579    |
| 0.632                     | 1.702    |
| 0.200                     | 1.877    |
| 0.063                     | 1.956    |
| 0.020                     | 1.986    |
| 0.002                     | 1.999    |

**As rho_base -> 0 (coupling-dominated regime), the exponent converges to 2.000.** This is the exact prediction of Corollary 11.2.

The exponent smoothly decreases as the base disturbance becomes more significant relative to the adversarial coupling, reaching ~1.2 when the base dominates by 6:1. This confirms the "coupling-dominant" qualifier in TF-11 is not a technicality -- it determines whether the squared law holds.

## Variant B Results: Drift-Noise Interpolation

### How does the exponent change as we interpolate between stochastic and deterministic coupling?

Parameterizing by f = mu/(mu+sigma), where mu is deterministic drift and sigma is noise std, with mu+sigma held constant. The adversarial coupling enters through mu (the deterministic component), not sigma (the stochastic component). Linear correction throughout.

| Drift fraction f | mu/sigma ratio | Exponent |
|:----------------:|:--------------:|:--------:|
| 0.00 (pure noise)| 0              | 2.000    |
| 0.10             | 0.11           | 1.933    |
| 0.30             | 0.43           | 1.828    |
| 0.50             | 1.00           | 1.747    |
| 0.70             | 2.33           | 1.682    |
| 0.90             | 9.00           | 1.629    |
| 1.00 (pure drift)| infinity       | 1.606    |

**Surprising finding**: the exponent is HIGHEST (= 2.0) at f = 0 (pure noise with coupling through drift) and DECREASES as the deterministic fraction increases.

**Why?** At f = 0 (pure noise, mu = 0, sigma > 0), the coupling acts only through the drift term mu_B = gamma * T_A. The noise sigma is the same for both agents (uncoupled). So the ratio of steady-state mismatches is determined entirely by the bias ratio: (mu_B/T_B) / (mu_A/T_A) = (gamma*T_A/T_B) / (gamma*T_B/T_A) = (T_A/T_B)^2. The noise adds symmetric fluctuations that cancel in the ratio.

At f = 1 (pure drift, sigma = 0), the disturbance is entirely deterministic. But now rho_base > 0 contributes a non-coupling-dependent term, which dilutes the squared scaling. The exponent of 1.606 reflects the ratio rho_base / (gamma*T) at these parameters.

**This confirms**: the squared advantage is a property of the **coupling-dominant** regime, not of deterministic vs stochastic disturbance per se.

### All correction functions at key drift fractions

| Correction   | f=0 (noise) | f=0.5 (balanced) | f=1 (drift) |
|-------------|:-----------:|:----------------:|:-----------:|
| Linear      | 2.000       | 1.747            | 1.606       |
| Threshold   | 1.986       | 1.747            | 1.606       |
| Saturating  | 6.417       | 7.259            | 7.119       |
| Sigmoid     | 5.936       | 7.567            | 7.938       |
| Breakdown   | 3.593       | 4.003            | 4.923       |

Again, saturating/sigmoid/breakdown show divergence artifacts (exponents > 3 are meaningless -- they reflect diverging B, not steady-state scaling). Linear and threshold give clean results consistent with the squared law in coupling-dominant regime.

## Why the original sim2 gave exponent ~1.05

The original sim2 implemented adversarial coupling as:
```
noise_B ~ N(0, rho_B^2)  where  rho_B = q_base + gamma_A * T_A
```

This puts ALL the coupling into the **noise standard deviation**. The steady state of the AR(1) process delta_{t+1} = (1 - T) * delta_t + N(0, sigma^2) is:

    E[|delta|] = sigma * sqrt(2/pi) / sqrt(2T - T^2)

The mismatch ratio with noise-variance coupling becomes:

    ratio = (sigma_B / sigma_A) * sqrt((2*T_A - T_A^2) / (2*T_B - T_B^2))

In the coupling-dominant limit (sigma ~ gamma*T):

    ratio ~ (T_A / T_B) * sqrt(T_A / T_B) = (T_A/T_B)^1.5

This gives a theoretical exponent of **1.5 in the coupling-dominant limit**, not 2.0. The measured 1.05 was even lower because q_base was not negligible.

**The fundamental issue**: mapping TF-11's rho (a deterministic rate) to a noise standard deviation changes the scaling exponent. The noise std maps to the *amplitude* of fluctuations, not the *bias* of the steady state. The squared law arises from the ratio of steady-state biases (rho/T), which only appears when coupling enters through a deterministic drift term.

## Theoretical implications

1. **Corollary 11.2 is correct** -- but only when the coupling mechanism matches the ODE's assumptions. The rho in TF-11 represents a deterministic rate of environmental change, and the squared advantage holds when this rate is dominated by the adversary's adaptive tempo.

2. **The original sim2 did not falsify TF-11**. It tested a different stochastic model (noise-variance coupling) that does not map cleanly to TF-11's deterministic-rate ODE. The result (exponent ~1.05) reflects the different scaling of noise-variance coupling, not a failure of the theory.

3. **For applications**: the squared advantage depends on the nature of the adversarial coupling. If the opponent's tempo increases the *systematic drift* of your environment (e.g., they move faster, changing the tactical situation at a steady rate), the squared law applies. If the opponent's tempo increases the *unpredictability/noise* of your environment (e.g., they act randomly and you observe noisy signals), the scaling is weaker (~1.5 in the limit, lower with base noise).

4. **Nonlinear correction creates persistence thresholds, not lower exponents**. For saturating/sigmoid corrections under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when rho exceeds the correction capacity. This is exactly TF-11 Proposition 11.1's persistence threshold, now observed directly.

5. **The coupling-dominance qualifier matters quantitatively**. At rho_base/(gamma*T) ~ 1, the exponent drops to ~1.6. The squared law requires the adversarial coupling to genuinely dominate the base disturbance rate.

## Figures produced

- `variant_a_single_agent.png` -- Single-agent convergence under deterministic drift (5 corrections)
- `variant_a_adversarial_ratio.png` -- Mismatch ratio vs tempo ratio (deterministic drift)
- `variant_a_adversarial_exponents.png` -- Exponent bar chart (deterministic drift)
- `variant_a_coupling_dominance.png` -- Exponent vs base-to-coupling ratio (the key plot)
- `variant_b_exponent_vs_drift_fraction.png` -- Exponent vs drift/noise fraction (interpolation)
- `variant_b_all_corrections.png` -- All corrections at key drift fractions
