---
slug: deriv-observation-noise-placement
type: derivation
status: conditional
depends:
  - deriv-sector-condition
  - result-adversarial-tempo-advantage
  - der-adversarial-destabilization
  - emp-update-gain
  - result-persistence-condition
stage: draft
---

# Derivation: Observation Noise in an Adversarial Pair — Whom It Hurts Depends on Whose Channel It Is On

In a two-agent adversarial pair, observation noise does not gate the faster agent's advantage in general. What it does depends on whose channel carries it. Noise on the defender's own channel raises the defender's error at every gain and every tempo ratio, and it lowers the largest attacker tempo the defender can survive at any gain. It flattens the log-log slope of the mismatch ratio only because it adds to the defender's error a term the attacker does not drive. Noise on the attacker's channel is what reduces the attacker's advantage, measured as the ratio. When the attacker's tempo comes from gain on that channel, its own error has a minimum at its Kalman gain, and past the point where its injected noise exceeds the coupling, its advantage grows only as the square root of its tempo while its own error grows; when the tempo comes from event rate at a fixed per-event gain, the same loss of dominance arrives later and the exponent falls to one. The ratio is not the defender's error, which attacker-channel noise leaves unchanged at a fixed attacker gain. What protects the defender's own persistence is the attacker's: an attacker that must stay in its own region on a fixed channel cannot run its gain past a cap that falls with the square of its channel noise, and with the defender's own survivable bound this gives a condition under which the defender survives every attacker that survives. Noise added to the shared environment compresses the ratio but raises the slower agent's error by more than the faster agent's. The closed form reproduces the Variant-E simulation table, and splitting that simulation by channel shows that its exponent collapse came from the attacker's channel.

## Formal Expression

*[Definition (Setup)]* Two agents $i \in \{A, B\}$, $A$ the attacker and $B$ the defender, each a linear corrector at gain $\alpha_i$ on a fixed observation channel with noise intensity $\sigma_{\nu,i}$ per coordinate, so that $\mathcal T_i = \alpha_i$ in the convention of #result-adversarial-tempo-advantage. Each agent's environmental diffusion carries the other's coupling (Coupling Model S, #der-adversarial-destabilization):

$$\sigma_{\text{env},B} = \sigma_{\text{base}} + \gamma_A \alpha_A, \qquad \sigma_{\text{env},A} = \sigma_{\text{base}} + \gamma_B \alpha_B .$$

By the Setup of #deriv-sector-condition (Model S with channel noise, linear correction), each agent's steady-state mean-square estimation error is

$$V_i := \mathbb E\lVert\delta_i\rVert^2_{ss} = \frac{n\,(\sigma_{\text{env},i}^2 + \alpha_i^2\sigma_{\nu,i}^2)}{2\alpha_i},$$

minimized over the gain at the Kalman–Bucy gain $K_i = \sigma_{\text{env},i}/\sigma_{\nu,i}$, where $V_i = n\,\sigma_{\text{env},i}\,\sigma_{\nu,i}$. Tempos are exogenous, as in #result-adversarial-tempo-advantage. The mismatch ratio is $\sqrt{V_B/V_A}$ and the exponent $b$ is its slope against $\alpha_A/\alpha_B$ on log-log axes.

### P1. Noise on the defender's channel

*[Derived (defender-channel noise)]*

(a) *At fixed gains.* $\partial V_B/\partial\sigma_{\nu,B} = n\,\alpha_B\,\sigma_{\nu,B} \gt 0$ for every $\alpha_B \gt 0$, and $V_A$ does not depend on $\sigma_{\nu,B}$. So raising $\sigma_{\nu,B}$ raises the defender's error and the mismatch ratio at every tempo ratio. The attacker's effect on the defender's mean-square error per unit of tempo, $\partial V_B/\partial\alpha_A = n\,\gamma_A\,\sigma_{\text{env},B}/\alpha_B$, does not depend on $\sigma_{\nu,B}$ at all. What falls is the slope $b$, because $V_B$ gains the term $n\alpha_B\sigma_{\nu,B}^2/2$, which does not grow with $\alpha_A$; the ratio's level rises while its slope falls. A lower exponent here is not a smaller advantage.

(b) *At the defender's best gain.* The defender's Kalman gain $K_B = \sigma_{\text{env},B}/\sigma_{\nu,B}$ falls as $1/\sigma_{\nu,B}$, and its error there, $n\,\sigma_{\text{env},B}\,\sigma_{\nu,B}$, rises in proportion to $\sigma_{\nu,B}$. Re-tuning gives the defender its best attainable error on that channel, and that best error is increasing in $\sigma_{\nu,B}$ because the error at every gain is; re-tuning also costs tempo: since the defender's tempo is its gain, its coupled pressure on the attacker, $\gamma_B K_B$, falls, which lowers $V_A$. Along the re-tuned path the ratio $V_B/V_A$ therefore rises in $\sigma_{\nu,B}$ from both sides.

(c) *Survivable attacker tempo.* By #deriv-sector-condition (exit exponent capped at the Kalman gain), the mean-square persistence condition is satisfiable at some gain iff $R_B^2 \gt n\,\sigma_{\text{env},B}\,\sigma_{\nu,B}$. With the coupling this reads

$$\gamma_A\,\mathcal T_A \;\lt\; \frac{R_B^2}{n\,\sigma_{\nu,B}} - \sigma_{\text{base}},$$

so the largest attacker tempo the defender can withstand at any gain falls as $\sigma_{\nu,B}$ rises, as $R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$ (when the Kalman gain is admissible; a cap on the gain only lowers this bound further). At a fixed gain the threshold of #der-adversarial-destabilization becomes $\gamma_A\mathcal T_A \lt \sqrt{2\alpha_B R_B^2/n - \alpha_B^2\sigma_{\nu,B}^2} - \sigma_{\text{base}}$, which also falls strictly in $\sigma_{\nu,B}$.

*Model D.* With channel noise bounded by $\bar\nu_B$, the defender's bound is $\rho_{\text{env},B}/\alpha_B + \bar\nu_B$ ( #deriv-sector-condition Setup): defender-channel noise raises it by the same amount at every gain, leaves the attacker's contribution $\gamma_A\mathcal T_A/\alpha_B$ unchanged, and so again raises the ratio while flattening its slope. The Kalman-gain forms in (b) and (c) are Model S results and are not carried over to Model D.

### P2. Noise on the attacker's channel

*[Derived (attacker-channel noise)]*

(a) $\partial V_A/\partial\sigma_{\nu,A} = n\,\alpha_A\,\sigma_{\nu,A} \gt 0$ and $V_B$ does not depend on $\sigma_{\nu,A}$ at a fixed attacker gain, so the ratio falls at every tempo ratio. The defender's own error is not lowered by this; it falls only if the attacker responds by lowering its gain, since $\sigma_{\text{env},B} = \sigma_{\text{base}} + \gamma_A\alpha_A$.

(b) *Tempo raised by gain on the attacker's channel.* $V_A(\alpha_A)$ is smallest at $K_A = \sigma_{\text{env},A}/\sigma_{\nu,A}$ and grows past it. Once $\alpha_A\sigma_{\nu,A} \gg \sigma_{\text{env},A}$ (with $\sigma_{\text{env},A} \approx \gamma_B\alpha_B$, a tempo ratio $\alpha_A/\alpha_B \gg \gamma_B/\sigma_{\nu,A}$, the scope bound of #result-adversarial-tempo-advantage), $V_A \approx n\alpha_A\sigma_{\nu,A}^2/2$. With the defender coupling-dominant ($\gamma_A\alpha_A \gg \sigma_{\text{base}}$ and $\gamma_A\alpha_A \gg \alpha_B\sigma_{\nu,B}$), $V_B \approx n\gamma_A^2\alpha_A^2/(2\alpha_B)$, and

$$\frac{V_B}{V_A} \;\approx\; \frac{\gamma_A^2\,\alpha_A^2/\alpha_B}{\alpha_A\,\sigma_{\nu,A}^2} = \frac{\gamma_A^2}{\sigma_{\nu,A}^2}\,\frac{\alpha_A}{\alpha_B}, \qquad \sqrt{\frac{V_B}{V_A}} \;\approx\; \frac{\gamma_A}{\sigma_{\nu,A}}\left(\frac{\alpha_A}{\alpha_B}\right)^{1/2}:$$

the exponent falls from $3/2$ to $1/2$. The advantage keeps growing, at the slower rate, while the attacker's own error grows linearly in its gain and its expected stay in its region shortens ( #deriv-sector-condition, exit exponent capped at the Kalman gain).

(c) *Tempo raised by event rate.* Let the attacker observe at event rate $\nu_A$ with per-event noise variance $s_A^2$ and correct with per-event gain $h_A$, so $\alpha_A = \nu_A h_A$ and its channel intensity is $\sigma_{\nu,A}^2 = s_A^2/\nu_A$ ( #result-persistence-condition, the event-rate lever). The injected term is $\alpha_A^2\sigma_{\nu,A}^2 = \alpha_A h_A s_A^2$, linear in tempo, and

$$V_A = \frac{n\,\sigma_{\text{env},A}^2}{2\alpha_A} + \frac{n\,h_A s_A^2}{2}.$$

At a fixed per-event gain the attacker's error falls toward the floor $n h_A s_A^2/2$, which does not move with its tempo. Its coupling dominance ($\sigma_{\text{env},A}^2 \gg \alpha_A h_A s_A^2$) still fails, at $\alpha_A \sim \sigma_{\text{env},A}^2/(h_A s_A^2)$ rather than at the gain-raised point; past it, with the defender coupling-dominant, $\sqrt{V_B/V_A} \approx \gamma_A\alpha_A/(s_A\sqrt{h_A\alpha_B})$, and the exponent falls from $3/2$ to $1$. An attacker keeps its coupling dominance as its tempo grows only if its per-event gain falls at least as fast as its tempo grows, that is, if its event rate grows at least as the square of its tempo. In the discrete form of the Variant-E script the floor is $h\,s^2/(2-h)$ per coordinate, and the slopes the script prints for this case over $r \in [0.5, 4]$ are local slopes, not this asymptote. This case is closed form only; it has not been simulated.

### P3. Noise added to the shared environment

*[Derived (shared base noise)]*

Without channel noise, $\sqrt{V_i} = \sigma_{\text{env},i}\sqrt{n/(2\alpha_i)}$, so $\partial\sqrt{V_B}/\partial\sigma_{\text{base}} = \sqrt{n/(2\alpha_B)} \gt \sqrt{n/(2\alpha_A)} = \partial\sqrt{V_A}/\partial\sigma_{\text{base}}$ whenever $\alpha_A \gt \alpha_B$. Raising $\sigma_{\text{base}}$ moves the ratio toward $(\alpha_A/\alpha_B)^{1/2}$, the non-coupling-dominant limit of #result-adversarial-tempo-advantage (Regime 3), while the slower agent's error rises by more than the faster agent's, and its destabilization threshold $(R_B\sqrt{2\alpha_B/n} - \sigma_{\text{base}})/\gamma_A$ ( #der-adversarial-destabilization) falls. Under Model D the same holds with $\rho_{\text{base}}/\alpha_i$ in place of $\sigma_{\text{base}}\sqrt{n/(2\alpha_i)}$.

### P4. An attacker that must persist is capped by its own channel

*[Derived (attacker persistence cap)]*

By the Model S window of #result-persistence-condition (gain-injected channel noise), the attacker persists in mean square at gain $\alpha_A$ only if $n(\sigma_{\text{env},A}^2 + \alpha_A^2\sigma_{\nu,A}^2) \lt 2\alpha_A R_A^2$, that is, for $\alpha_A$ between the roots of this quadratic, the larger of which is

$$\alpha_+ = \frac{R_A^2 + \sqrt{R_A^4 - n^2\sigma_{\text{env},A}^2\sigma_{\nu,A}^2}}{n\,\sigma_{\nu,A}^2} \;\leq\; \frac{2R_A^2}{n\,\sigma_{\nu,A}^2},$$

whatever $\sigma_{\text{env},A}$ is. A persisting attacker therefore exerts coupled pressure $\gamma_A\alpha_A \lt 2\gamma_A R_A^2/(n\sigma_{\nu,A}^2)$ on the defender. With P1(c), the defender can persist at some gain against every attacker that itself persists if

$$\frac{2\gamma_A R_A^2}{n\,\sigma_{\nu,A}^2} \;\leq\; \frac{R_B^2}{n\,\sigma_{\nu,B}} - \sigma_{\text{base}} .$$

The left side falls as $1/\sigma_{\nu,A}^2$ and the right side rises as $\sigma_{\nu,B}$ falls, so degrading the attacker's channel and protecting one's own both widen the condition. Unlike P2(a), this is a statement about the defender's own persistence, not about the ratio. It binds an attacker that must stay in its own region and observes through a fixed channel. An attacker that is willing to leave its region is not capped. An attacker that raises its event rate lowers its channel intensity as $\sigma_{\nu,A}^2 = s_A^2/\nu_A$ and raises its cap in proportion to $\nu_A$.

### Check against the Variant-E simulation

*[Derived (reproduction), with simulation]*

Variant E ( `empirica:track-b-nonlinear`, `variant_ef_extensions.py`) is the discrete form of this Setup: $\delta_{t+1} = (1-\alpha)\delta_t - \alpha\varepsilon_t + w_t$ with stationary variance $(\rho^2 + \alpha^2 s^2)/(\alpha(2-\alpha))$, $q = 0.05$, $\gamma = 0.5$, $\alpha_B = 0.1$, $\alpha_A = r\alpha_B$ (capped at $0.9$) for twelve tempo ratios $r$ from $0.5$ to $4$, one noisy observation per step, and the same noise scale $s$ on both channels. The attacker's tempo is therefore raised by gain on a fixed channel. The closed form gives the recorded exponents to within $0.003$:

| $s$ | recorded, fixed gain | closed form | recorded, Variant-E gain | closed form |
|:---:|:---:|:---:|:---:|:---:|
| 0.0 | 1.037 | 1.036 | 1.037 | 1.036 |
| 0.1 | 1.002 | 1.002 | 0.971 | 0.970 |
| 0.2 | 0.918 | 0.917 | 0.938 | 0.936 |
| 0.5 | 0.595 | 0.593 | 0.629 | 0.626 |
| 1.0 | 0.181 | 0.181 | 0.395 | 0.394 |

Re-running the same loop with the noise on one channel at a time (seed 42, 150 trials, 15,000 steps, burn-in 4,000), at fixed gain:

| noise on | exponent | ratio at $r = 0.5$ | at $r = 1$ | at $r = 4$ |
|:---|:---:|:---:|:---:|:---:|
| neither | 1.04 | 0.54 | 1.00 | 4.58 |
| both, $s = 1$ | 0.18 | 0.80 | 1.00 | 1.20 |
| defender only, $s = 1$ | 0.82 | 0.89 | 1.41 | 4.93 |
| attacker only, $s = 1$ | 0.40 | 0.48 | 0.71 | 1.11 |
| both, $s = 0.5$ | 0.59 | 0.63 | 1.00 | 2.09 |
| defender only, $s = 0.5$ | 0.96 | 0.64 | 1.12 | 4.67 |
| attacker only, $s = 0.5$ | 0.68 | 0.52 | 0.89 | 2.05 |

Defender-only noise raises the ratio at every tempo ratio (P1a) while lowering the slope. Attacker-only noise produces most of the two-sided collapse (P2). The recipe is `empirica/track-b-nonlinear/variants/variant_e_noise_placement.py`, run as `python3 -I variant_e_noise_placement.py` from that directory; it prints the closed-form table, the split re-run, and the event-rate closed form of P2(c), and its output is recorded in `variant_e_noise_placement_results.md` beside it.

## Epistemic Status

*Conditional*, and exact under its stated model: linear correction on a fixed channel, white channel noise, Coupling Model S (or D where stated), and exogenous tempos. P1–P4 are algebra on the steady state of #deriv-sector-condition and the coupling model of #der-adversarial-destabilization; P1(c) uses that segment's satisfiability condition at the Kalman gain, and P4 the Model S window of #result-persistence-condition. P4's cap was also checked on random parameter draws (the integrator's 20,000 and the independent checker's, none violating it). The exponents in P2(b) and P2(c) are asymptotic slopes; between regimes the slope is a local one. The reproduction of the Variant-E table checks that the simulation is this model; the split re-run is a simulation of the theory's own equations, not an instantiation. What remains open is the fully coupled case in which each agent's tempo responds to the other's error, and nonlinear correction, where #result-adversarial-exponent-regimes finds thresholds rather than exponents.

## Claim Record

### Noise on the defender's own channel raises the defender's error and the mismatch ratio, and lowers the attacker tempo it can survive

**Register:** formal — P1, a theorem about the two-agent linear model.

**Population:** pairs of linear correctors on fixed white-noise channels under Coupling Model S with exogenous tempos (P1a–c); P1a's direction also under Model D with bounded channel noise.

**True of:** the Variant-E pair, by the closed form and by the split re-run (defender-only noise at $s = 1$: ratio at $r = 4$ rises from 4.58 to 4.93 while the slope falls from 1.04 to 0.82); internal consistency, not instantiation.

**False of:** an attack carried on the defender's observation channel itself (misinformation, #der-interaction-channel-classification Regime I with adversarial content), where the channel's true reliability is lower than the defender assumes; there the gain principle ( #emp-update-gain) says to lower the gain to that reliability, which is calibration, not added noise, and is outside this Setup.

**Falsifier:** a linear-corrector pair in this Setup in which raising $\sigma_{\nu,B}$ lowers $V_B$ or the ratio at some tempo ratio; P1a's derivative rules it out.

**Instantiated:** no.

### Noise on the attacker's channel reduces the attacker's advantage, and under gain-raised tempo cuts the exponent to one half

**Register:** formal — P2.

**Population:** as above; P2(b) for attacker tempo raised by gain on its channel, past the tempo ratio $\gamma_B/\sigma_{\nu,A}$.

**True of:** the Variant-E pair (attacker-only noise at $s = 1$: slope 0.40, ratio at $r = 4$ falls to 1.11); internal consistency, not instantiation.

**False of:** an attacker whose tempo comes from event rate at a fixed per-event gain, whose noise floor does not grow with tempo (P2c); its exponent falls to one, not one half. An attacker whose event rate grows at least as the square of its tempo keeps the coupling dominant and the exponent at $3/2$.

**Falsifier:** a pair in this Setup where the ratio slope stays at $3/2$ past $\alpha_A/\alpha_B \gg \gamma_B/\sigma_{\nu,A}$ under gain-raised tempo.

**Instantiated:** no.

### A defender facing a faster attacker should degrade the attacker's observation and protect its own, not add noise to its own channel or to the shared environment

**Register:** normative — a design recommendation for the defender's own persistence, drawn from P1(c) and P4.

**Population:** defenders whose interaction with a faster attacker is described by the Setup, facing an attacker that must persist in its own region on a fixed channel (P4); the link from a defender's opacity to the attacker's channel noise ( #der-agent-opacity) is qualitative.

**True of:** the Setup, by P1(c) and P4: raising $\sigma_{\nu,A}$ or lowering $\sigma_{\nu,B}$ widens the condition under which the defender survives every persisting attacker, and raising $\sigma_{\nu,B}$ narrows it; internal consistency, no comparison on a real agent.

**False of:** an attacker willing to leave its own region (no P4 cap), against which attacker-channel noise lowers only the ratio and not the defender's error; an attacker that raises its event rate, whose cap grows with it; and contests scored by the mismatch ratio's slope, where defender-channel noise would look like a gain.

**Falsifier:** a comparison on real adversarial agents in which raising the defender's own observation noise improves its persistence or its error against a faster attacker.

**Instantiated:** no.

## Discussion

**Slope is not level.** The exponent $b$ is a slope on log-log axes. A term in the defender's error that the attacker does not drive (its own injected channel noise, or a large shared base disturbance) flattens that slope by raising the floor the attacker's contribution sits on. A flatter slope can come with a higher ratio at every tempo ratio, as in P1a. Reading a lower $b$ as a weaker attacker is the error this segment exists to block.

**Where the two-sided result came from.** The Variant-E table records both channels noisy at once and reads as "observation noise gates the tempo advantage." Split by channel, almost all of the collapse belongs to the attacker's channel (P2), because the simulation raised the attacker's tempo by gain on one noisy observation per step, so the attacker injected noise in proportion to the square of its gain. That is the regime where its own injected noise outgrows the coupling, the scope bound #result-adversarial-tempo-advantage names. Boyd's emphasis on Orient quality survives in this form: the faster agent's advantage is only as good as its own observation channel.

**The defender's levers.** P1–P4 give the defender three levers, and they point different ways. Its own channel's quality is its survival margin: by P1(c) the survivable attacker tempo is $R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$, falling as $\sigma_{\nu,B}$ rises. The attacker's channel is where noise helps the defender, but not through the attacker's error, which does not enter the defender's: at a fixed attacker gain the defender's error is unchanged (P2a). It helps through the attacker's own persistence, which caps a persisting attacker's gain as $1/\sigma_{\nu,A}^2$ (P4), and, for an attacker tuned to its own Kalman gain $K_A = \sigma_{\text{env},A}/\sigma_{\nu,A}$, through that gain falling as $\sigma_{\nu,A}$ rises. The shared environment narrows the ratio but costs the slower agent more than the faster one. The cost of each lever is in the defender's own error and persistence margin, which the exponent alone does not show.

## Working Notes

- The fully coupled version, where each agent's gain is a best response to the other's, is the natural next derivation; its home is #deriv-strategic-composition. The attacker's objective decides it. Damage alone gives it no reason to lower its gain, since $V_B$ grows without bound in $\alpha_A$. The ratio $V_B/V_A$ has no finite global maximizer (it grows as $\alpha_A$ once noise sets the attacker's error), though under weak coupling it can have a local maximum near the attacker's Kalman gain (independent check 1, F3). A Kalman-tuned attacker lowers its gain as its channel noise rises; for every other attacker, persistence is what P4 caps. An objective that trades damage against the attacker's own error is the open case.
- P2(c) is closed form only. A simulation with $r$ genuine sub-updates per step would test it.
