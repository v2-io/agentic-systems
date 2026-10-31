# Variant E split by noise placement (2026-10-30)

Consumer: `#deriv-observation-noise-placement`. Script: `variant_e_noise_placement.py` in this directory, run as `python3 -I variant_e_noise_placement.py` (seed 42).

**What Variant E actually varied.** `run_variant_e_adversarial` in `variant_ef_extensions.py` says the attacker's tempo advantage comes "via higher event rate nu_A (not higher gain)". The loop does something else: each step it takes one noisy observation per agent and corrects by `T_A_eff * obs_A`, with `T_A_eff = r * eta`. That is tempo raised by gain on a fixed channel, so the attacker's injected noise grows as the square of its gain. The same noise scale `sigma_obs` sits on both channels. The "optimal" column uses the gain computed for the defender's scale, multiplied by `r` for the attacker, so it is not each agent's own optimum.

## 1. Closed form reproduces the recorded table

Each agent's discrete stationary variance is $(\rho^2 + \alpha^2 s^2)/(\alpha(2-\alpha))$, with $\rho_A = q + \gamma\alpha_B$, $\rho_B = q + \gamma\alpha_A$; the exponent is the OLS log-log slope of $\sqrt{V_B/V_A}$ over the twelve tempo ratios.

| $s$ | recorded fixed | closed form | recorded Variant-E gain | closed form |
|:---:|:---:|:---:|:---:|:---:|
| 0.0 | 1.037 | 1.036 | 1.037 | 1.036 |
| 0.1 | 1.002 | 1.002 | 0.971 | 0.970 |
| 0.2 | 0.918 | 0.917 | 0.938 | 0.936 |
| 0.5 | 0.595 | 0.593 | 0.629 | 0.626 |
| 1.0 | 0.181 | 0.181 | 0.395 | 0.394 |

Closed form split by channel (fixed gain): defender-only noise gives slopes 1.04, 1.03, 1.02, 0.96, 0.82 and a ratio at $r = 4$ that rises from 4.59 to 4.94; attacker-only noise gives 1.04, 1.01, 0.93, 0.67, 0.40 and a ratio at $r = 4$ that falls to 1.11. The defender's RMS error at $r = 4$ rises from 0.574 to 0.618 under defender-only noise at $s = 1$.

## 2. Simulation, channels separated

The Variant-E fixed-gain loop, unchanged except for separate noise scales on the two channels; 150 trials, 15,000 steps, burn-in 4,000.

| noise on | slope | ratio $r = 0.5$ | $r = 1$ | $r = 4$ |
|:---|:---:|:---:|:---:|:---:|
| neither | 1.04 | 0.54 | 1.00 | 4.58 |
| both 1.0 | 0.18 | 0.80 | 1.00 | 1.20 |
| defender only 1.0 | 0.82 | 0.89 | 1.41 | 4.93 |
| attacker only 1.0 | 0.40 | 0.48 | 0.71 | 1.11 |
| both 0.5 | 0.59 | 0.63 | 1.00 | 2.09 |
| defender only 0.5 | 0.96 | 0.64 | 1.12 | 4.67 |
| attacker only 0.5 | 0.68 | 0.52 | 0.89 | 2.05 |

## 3. Event-rate tempo (closed form, not simulated)

The attacker takes $r$ sub-updates per step at per-event gain $\eta = 0.1$, each on a fresh observation: $V_A = \rho_A^2/(1-c^2) + \eta s^2/(2-\eta)$ with $c = (1-\eta)^r$. Slopes for $s = 0, 0.1, 0.2, 0.5, 1.0$: both channels noisy 0.95, 0.94, 0.91, 0.76, 0.50; attacker only 0.95, 0.94, 0.92, 0.84, 0.71. The gating is weaker than under gain-raised tempo; the no-noise slope is 0.95 rather than 1.04 because the per-step contraction $1-(1-\eta)^r$ is below $r\eta$.

Environment: Python 3.11.14, numpy 2.4.1, scipy 1.17.1 (2026-10-30).
