---
kind: review
author:
  name: f72-integrator
  role: integrator
sources:
  - spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1-integration-notes.md
written: 2026-10-30
transcribed-by: Claude Fable 5.1 (vsect builder), from the source named above, read whole
---

# F72 landing: what the integrator re-derived or measured before it landed

The integrator's own record is the source file above; this review carries its checks in the typed form `vsect take` reads. The integrator was neither the spiker nor the verifier, and its model is not named in its file, so the author is recorded by role. The simulation script is not in the repository; its parameters are.

## C1 (check)
- target: segment:deriv-evidence-allocation-ceiling
- act: rederive
- line: derivation
- criterion: Prop EA.1 (allocation lag): under fixed allocation with observation probability $\pi_i$ and Model D drift $\rho_\Sigma$, does every estimator in class $\mathcal C$ (convex combinations of observed outcomes with history-fixed weights) have mean mismatch at least $\rho_\Sigma \times$ (age of the youngest observation), with expectation tending to $\rho_\Sigma/\pi_i$?
- committed: before
- outcome: confirmed
- recheck: integration notes §Who checked what, §5.1; re-derive by the age route (mismatch is minus a weighted average of $\theta_t - \theta_s$ over observed $s$) and compare with the verifier's deterministic-gain route

Re-derived by a route different from the verifier's. The verifier's route (per-step expected correction $\pi_i g_i\,\delta$ with $g_i \le 1$, then DA.1) assumes a deterministic per-observation gain, which holds for per-observation discounting at the stationary count but not off it, nor for per-time-step discounting. The age route covers those cases. The routes agree where both apply.

## C2 (check)
- target: segment:deriv-evidence-allocation-ceiling
- act: run
- line: simulation
- criterion: Does the measured effective per-step correction rate equal $\pi(1-\lambda)$ per observation and approach $\pi$ as $\lambda \to 0^{+}$ under both discount conventions?
- committed: before
- outcome: confirmed
- recheck: exact mean-lag simulation with $y \to \theta$ substitution, $\rho = 10^{-3}$, $2 \times 10^{5}$ paths, last 100 of 400 steps, $\pi \in \{1, 0.5, 0.3\}$, $\lambda \in \{0, 0.5, 0.9, 0.01\}$; the table is in the integration notes

Because $\hat p$ is linear in the outcomes with weights fixed by the observation history, replacing $y$ by $\theta$ yields $\mathbb{E}[\hat p \mid O]$ exactly; averaging over the allocation randomness gives the mean lag without Bernoulli noise. Per-observation rates matched $\pi(1-\lambda)$ to four decimals at every tested point. A first attempt with raw Bernoulli outcomes at $\rho = 2 \times 10^{-4}$ was swamped by noise and gave wrong-signed values at $\lambda = 0$; the substitution made the check decisive. The verifier's §6 per-step approximation was found 10–15% low at the tested points and was not landed.

## C3 (check)
- target: segment:deriv-edge-credence-dynamics
- act: rederive
- line: derivation
- criterion: Prop B.1F: gain $1/n_t$ with $n_t$ the post-update count, deterministic count dynamics $n_t = \lambda^t n_0 + (1-\lambda^t)/(1-\lambda)$, stationary gain exactly $1-\lambda$, the EWMA identity at $n_0 = n_{\text{eff}}$, and the all-time trajectory guarantee for $n_0 \le n_{\text{eff}}$
- committed: before
- outcome: confirmed
- recheck: verify-1 §2–§4; three lines of algebra for the gain and an induction for the trajectory guarantee

Re-derived the three-line algebra and the induction. The coordinator separately measured the gain to six decimals at four $\lambda$ values.

## C4 (check)
- target: segment:schema-strategy-persistence
- act: read-check
- line: derivation
- criterion: After the landing, does every carrier of $(1-\lambda)/(2-\lambda)$ and of the half-plane ceiling in the schema state the exact form $1-\lambda$ and no ceiling?
- committed: after
- outcome: confirmed
- recheck: grep the schema for `2-\lambda` and for `R_\Sigma/2`

Replaced at: intro paragraphs, §Forgetting as Prerequisite, Epistemic Status, instance 4, Discussion §6, Findings Brief/Impact/Novelty, and three Working-Notes lines. The verifier's work order undercounted carriers in the posture segment (12 sites, not 3) and missed the F73 lower-bound-only form at three places in `#deriv-edge-credence-dynamics`; all were replaced.
