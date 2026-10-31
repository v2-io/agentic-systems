---
slug: obs-gated-tempo-advantage
type: observation
status: empirical
depends:
  - der-adversarial-destabilization
  - emp-update-gain
  - def-adaptive-tempo
  - deriv-observation-noise-placement
stage: draft
---

# Observation: Gated Tempo Advantage

Observation noise on both agents' channels *gates* the adversarial tempo advantage from the prior result, and the gating comes from the faster agent's own channel. In the simulation recorded here (Variant E) each agent corrects on one noisy observation per step, and the attacker's tempo is raised by raising its gain, so the attacker feeds back channel noise in proportion to the square of its gain. At observation noise comparable to or larger than process noise, the steady-state mismatch-ratio exponent drops sharply: at fixed gain the agents lose nearly all of the superlinear scaling, and at the two highest noise levels lowering both agents' base gain toward the noise level keeps more of it than the fixed gain does. The closed form for this model reproduces the table, and the same loop re-run with noise on one channel at a time places the effect: noise on the attacker's channel produces most of the collapse, while noise on the defender's channel alone raises the mismatch ratio at every tempo ratio even as it flattens the slope ( #deriv-observation-noise-placement).

The gain principle ( #emp-update-gain) bears on both halves. The attacker's advantage is bounded by its own channel: past its Kalman gain, raising its gain injects more noise than it removes lag, and past the tempo ratio where that noise outgrows the coupling its advantage grows only as the square root of its tempo. *Gated* names that regime structure: the superlinear scaling of `#result-adversarial-tempo-advantage` holds while each agent's error is set by the coupling, and an agent whose error is set instead by its own injected noise has stepped out of it. Noise on the defender's own channel is not a defense. At fixed gain it does lower the exponent without changing tempo or gain, but only because it adds to the defender's error a term the attacker does not drive; the defender's error and the mismatch ratio rise at every tempo ratio. Re-tuning to the noise, as the gain principle says it should, does not undo this: the defender's best attainable error rises in proportion to its channel noise, its gain and tempo fall, and the attacker tempo it can survive at any gain falls as that noise rises ( #deriv-observation-noise-placement, P1).

## Formal Expression

*[Observation (obs-gated-tempo-advantage, from track-b Variant E)]*

In a two-agent adversarial system with observation noise $\sigma_{\text{obs}}$ added to each agent's mismatch signal, one noisy observation per step, and the attacker's tempo raised by gain ($\mathcal T_A = r\,\eta$, $\mathcal T_B = \eta$):

| $\sigma_{\text{obs}}$ | Exponent (fixed $\eta$) | Exponent (optimal $\eta^\ast$) |
|:---:|:---:|:---:|
| 0.00 | 1.04 | 1.04 |
| 0.10 | 1.00 | 0.97 |
| 0.20 | 0.92 | 0.94 |
| 0.50 | 0.60 | 0.63 |
| 1.00 | 0.18 | 0.40 |

At $\sigma_{\text{obs}} = 1.0$ (10x the agents' process noise at equal tempo), the fixed-gain adversarial exponent drops from $\sim 1.0$ to $\sim 0.2$. The right-hand column uses the gain the simulation computed for the defender's noise level, $\eta^\ast$, with the attacker at $r\,\eta^\ast$; it is not each agent's own optimum. Lowering both agents' base gain this way restores the exponent to $\sim 0.4$, because the attacker's injected noise falls with its gain.

**The mechanism.** Each correction feeds a share of the channel noise back into the estimation error, in proportion to the square of the gain ( #deriv-sector-condition, Setup). An attacker whose tempo comes from a larger gain on the same noisy observation therefore injects noise that grows faster than its correction removes lag, and past its Kalman gain its own error rises with its tempo. Split by channel, noise on the attacker's side alone gives exponent 0.40 at $\sigma_{\text{obs}} = 1.0$; noise on the defender's side alone gives 0.82 while raising the mismatch ratio at every tempo ratio ( #deriv-observation-noise-placement, Variant-E check).

## Epistemic Status

*Empirical*, as a simulation record; its numbers are now derived. The closed form of #deriv-observation-noise-placement (the discrete stationary variance of each noisy linear corrector, with the coupling of #der-adversarial-destabilization) reproduces both columns of the table to within $0.003$, so the table is a property of the model and not only of the runs. The single-agent half was already derived: for linear correction at rate $\alpha$ the steady-state estimation error is $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, smallest at the Kalman gain, because each correction injects a share of the channel noise ( #deriv-sector-condition Setup; #result-persistence-condition "Two levers"). What stays specific to this record is the parameter choice: gain-raised attacker tempo, equal noise on both channels, and a base-to-coupling ratio of about one, so the noise-free exponent is $\sim 1.04$ rather than a coupling-dominant value.

## Discussion

**Observation quality gates the faster agent's advantage.** Boyd insisted that the quality of Orient (observation processing) matters more than raw OODA speed. The model gives one mechanism for this: an agent that raises its tempo by correcting harder on the same noisy observations feeds its own channel noise back into its estimate, so its advantage over a slower agent is bounded by the quality of its own channel. Raising tempo by observing more often is a different lever, since independent observations average their noise; the simulation recorded here did not test it, and the closed form for it shows weaker gating ( #deriv-observation-noise-placement, P2(c)). The model captures one mechanism (noisy correction steps), not the full richness of Orient processing.

**The optimal gain helps most in the moderate-noise regime.** At $\sigma_{\text{obs}} = 0.05$ (observation noise half of process noise), the optimal gain cuts steady-state mismatch by 52% compared to fixed gain. At very high noise, the improvement is less dramatic in absolute terms but more important relatively (0.40 vs. 0.18 exponent).

**Practical implication.** An agent facing an adversary with superior tempo should invest in degrading the adversary's observation quality rather than trying to match its speed, and should protect its own: noise on its own channel lowers the attacker tempo it can survive. Conversely, an agent with superior tempo should protect its observation channels; its tempo advantage is only as good as the observation quality that supports it.

**Connection to code quality.** In the software domain ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`), code quality IS observation infrastructure. A well-structured codebase provides low-noise observations (clear tests, readable code, explicit interfaces). A poorly structured codebase adds observation noise to every development cycle, degrading the developer's effective tempo regardless of how fast they work.

**Recipient-side reading.** In the vocabulary of #der-interaction-channel-classification, high $U_{o,B}$ raises the observability floor (boundary (I-c)), so more of $A$'s events land in Regime III (ambient noise) instead of producing usable updates. Regime-III events still enter $\sigma_{w,B}^2$ and drain $B$'s reserve, and the Model-S persistence condition is a bound on that same $\sigma_w$, so moving events from Regime II to Regime III does not shelter $B$; it changes which repair applies, not whether $B$ is hurt.

## Working Notes
- The finding that fixed $\eta = 0.1$ is "remarkably robust" to observation noise (42% degradation at $\sigma_{\text{obs}} = 10 \times q_{\text{env}}$) suggests that conservative gains are a reasonable default for environments with unknown noise levels. The cost of being slightly below optimal is much less than the cost of being above optimal (overcorrection amplifies noise).
- The interaction between observation noise and adversarial exponent regime (drift vs. stochastic) has not been tested. The Variant E results use stochastic coupling only. Whether observation noise degrades the deterministic-drift exponent ($b = 2$) by the same proportion is an open question.
- Simulation code: `../../empirica/track-b-nonlinear/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.

### Incidental audit gold (gold-lift sweep, A15, 2026-05-31)

Cross-audit "wandering thoughts" / §14 ideation, deduplicated and lightly attributed. *Orthogonal* pedagogical / framing / forward-vision material staged for an eventual separate promotion pass. **Coverage:** two dirs reached a digested reflection on this segment (193847 Gemini, 829314 Gemini); the careful Claude auditor (451729) covered it inside the §III batch-15 reflection but with no segment-specific gold beyond the exponent material lifted to its sibling. Finding-vs-framing conflation preserved (the slug appears as `obs-gates-advantage` in some dirs — matched by content).

#### 1. Candidate Brief prose / pre-prose

- The Boyd connection stated as the segment's spine: **"observation quality gates tempo advantage"** — you cannot compute your way out of a fog machine; optimal Bayesian updating *cannot* rescue a tempo advantage if the sensors are bad (Gemini, 193847; Gemini, 829314). Strong Brief anchor.
- The software corollary as a memorable plain-language claim: **"you cannot out-hire a bad codebase."** Hiring a 10x developer whose raw rate $\nu$ is ten times anyone's still collapses to ~1x if the spaghetti codebase makes every observation $o_{t+1}$ noisy — the high $U_o$ forces the optimal gain $\eta^\ast$ down and the effective tempo $\mathcal{T}$ with it; the only fix is to invest in observability (tests, telemetry, refactor), not to type faster (Gemini, 829314). The collapse to ~1x is exact only for noise shared across readings (a misleading name misleads every reading); with independent noise, ten times the event rate buys about three times the tempo ( #def-adaptive-tempo, §Observation noise gating).

#### 2. Candidate Discussion

- **Hyper-reactivity is self-destabilizing** — the noisy-speedometer car: checking a noisy sensor 1000×/s and adjusting the gas 1000×/s amplifies sensor noise into physical, destructive oscillation; the high-frequency control loop turns observation noise into self-generated disturbance $\rho$. A vivid Discussion frame (Gemini, 193847), true in the linear model when the faster loop corrects harder on each reading, which is gain raised on a fixed channel; more independent readings with proportionally smaller corrections lower the error instead ( #def-adaptive-tempo, §Observation noise gating).
- **Conservative gain as a defensive default.** The Working-Notes finding that fixed $\eta=0.1$ is "remarkably robust" to $10\times$ noise (only 42% degradation) reads as: simple sluggish conservative processes often out-survive hyper-optimized high-gain systems in volatile environments — "is stubbornness mathematically optimal when you don't know your opponent's $U_o$?" Worth a Discussion sentence beyond the current single WN bullet (Gemini, 193847; Gemini 829314 converges).

#### 4. Readers often ask / wonder

- **Does the $b=2$ (deterministic-drift) exponent degrade under observation noise by the same proportion as the $b\approx 1.5$ stochastic one?** Variant E tested stochastic coupling only — an honest open question readers will hit (Gemini, 193847; already a WN bullet, surfaced again as a reader-want).

#### Belongs elsewhere

- **Forward-vision (ELI architecture, `04-eli-core/` / `03-llm-core/`).** "If a future AI's internal inference loop runs faster than its ability to get clean signals from reality, it will hallucinate and over-correct on the noise in its own processing — it will literally shake itself apart. The infrastructure must implement a *low-pass filter* on the agent's actions: when observation noise $U_o$ crosses a threshold, physically throttle the agent's action rate $\nu$. An agent must not be allowed to act faster than it can cleanly observe." A derived-feeling safety-architecture principle pointing at runtime governance, not this segment (Gemini, 193847).
- **TST (`02-tst-core/`).** "Code quality IS observation infrastructure" — clean code is not aesthetics but a literal reduction in $U_o$ that protects developer tempo from degrading into noise — was repeatedly named the most practical takeaway in the framework; the segment already cross-references `#der-code-quality-as-observation-infrastructure`, and the gold here is the *strength of the pull* to make this a headline TST instantiation (Gemini, 829314; Gemini 193847). The adversarial dual: "an agent facing a faster adversary should invest in degrading the adversary's observation quality (FUD, obfuscate own metrics / raise own $H_b$, decoy products) rather than matching speed" — already in the segment's Practical-implication paragraph; auditors flag it as a high-resonance point worth foregrounding.
