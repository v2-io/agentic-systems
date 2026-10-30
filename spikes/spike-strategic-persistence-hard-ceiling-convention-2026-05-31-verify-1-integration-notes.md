# Integration notes: verify-1 (strategic-persistence hard ceiling) landed in canon

**Date:** 2026-10-30  
**Role:** integrator (KR2.3, KR3.3a of `msc/inside-out-2026-10/INTENT.md`). Not the spiker and not the verifier.  
**Work order:** `spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md` §7, read whole.

## What landed where

- **Deleted:** `01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md`. Option (b) of verify-1 §7. The slug and title stated the false claim, and the true cap has a different subject and different dependencies, so it gets its own slug.
- **`#deriv-edge-credence-dynamics` Prop B.1F (new).** Verify-1 §2–§4: gain $1/n_t$ (post-update count), deterministic count dynamics, stationary gain exactly $1-\lambda$, the EWMA identity at $n_0 = n_{\text{eff}}$, the all-time trajectory guarantee for $n_0 \le n_{\text{eff}}$, and reachable region $\rho_\Sigma \lt R_\Sigma$ as the universal admissible-corrector floor. The corrected result went here rather than into the schema because the schema already cites B.1–B.6 for its derivations (math-lives-in-segments). Prop B.4's (SA3) is replaced by the exact two-sided interval (F73), which also appears in the summary bullet and the derived-vs-chosen table. The Epistemic Status "time-varying $\alpha$" paragraph now carries the true form.
- **`#deriv-evidence-allocation-ceiling` (new, `status: exact`, `stage: draft`).** Verify-1 §5.1 plus the §6 convention, named.
- **`#schema-strategy-persistence`.** Every carrier of $(1-\lambda)/(2-\lambda)$ and of the ceiling is replaced: intro paragraphs, §Forgetting as Prerequisite, Epistemic Status, instance 4, Discussion §6, Findings Brief/Impact/Novelty, and three Working-Notes/gold lines. The D.3 history line is deleted from WN; the history now lives in CHANGELOG. The F72 off-ramp flag became a regression guard, and the §5.2 noise analysis is parked as a WN forward pointer. The Model-S line gains one sentence on gain-modulated noise.
- **`#disc-constructive-impossibility-posture`.** Instance E is now the evidence-allocation ceiling, at 12 edit sites: depends, the three-moves list, table row E, the scope paragraph, instance statuses, the spine paragraph, the Brief, the Novelty claim, Related Work, the Search Log, and the WN.
- **OUTLINE** (prose at line 333 in two places, row replaced, B.1F noted on the edge-credence row), **TODO** (item removed), **spikes/INDEX** (05-31 section rewritten; 05-20 strengthening row records outcome B superseded), **05-31 spike** (Status line: superseded, kept in place), **CHANGELOG** (Landed bullet under today's Refuted bullet).

## Who checked what

- **§2–§4 (corrected C.1, trajectory guarantee).** Verifier derived and measured them. The coordinator measured the gain independently (six decimals at four $\lambda$ values). I re-derived the three-line algebra and the induction.
- **§5.1 (allocation cap).** Verifier's route: per-step expected correction $\pi_i g_i\,\delta$ with deterministic $g_i \le 1$, then DA.1. I re-derived it by a different route, the age route now written as Prop EA.1. For estimators that are convex combinations of observed outcomes with outcome-independent weights, under fixed allocation $\mathbb{E}[\hat p \mid O] - \theta_t$ is minus a weighted average of $\theta_t - \theta_s$ over observed $s$, which is at least $\rho_\Sigma \times$ (age of the youngest observation) under constant drift. Its expectation tends to $\rho_\Sigma/\pi$. This covers history-dependent random gains (Beta counts off their stationary point, per-time-step discounting), which the deterministic-gain route does not. The routes agree where both apply.
- **Simulation (mine).** Because $\hat p$ is linear in the outcomes with weights fixed by the observation history, replacing $y$ by $\theta$ yields $\mathbb{E}[\hat p \mid O]$ exactly. Averaging over the allocation randomness then gives the mean lag without Bernoulli noise. Effective per-step rate $= \rho/\lvert\text{lag}\rvert$, with $\rho = 10^{-3}$, $2\times 10^5$ paths, last 100 of 400 steps:

| $\pi$ | $\lambda$ | per-observation | $\pi(1-\lambda)$ | per-time-step | verify-1 §6 approx |
|---|---|---|---|---|---|
| 1.0 | 0.5 | 0.5000 | 0.5000 | 0.5000 | 0.5000 |
| 0.5 | 0.0 | 0.4999 | 0.5000 | undefined (count is 0 between pulls) | 0.5000 |
| 0.5 | 0.5 | 0.2499 | 0.2500 | 0.3788 | 0.3333 |
| 0.5 | 0.9 | 0.0500 | 0.0500 | 0.0971 | 0.0909 |
| 0.3 | 0.5 | 0.1500 | 0.1500 | 0.2660 | 0.2308 |
| 0.3 | 0.9 | 0.0300 | 0.0300 | 0.0929 | 0.0811 |

Per-time-step at $\lambda = 0.01$: $0.4986$ ($\pi = 0.5$), $0.2996$ ($\pi = 0.3$), so the supremum $\pi$ is approached as $\lambda \to 0^{+}$ under both conventions. My first attempt used raw Bernoulli outcomes, and with $\rho = 2\times 10^{-4}$ the noise swamped the lag, giving wrong-signed values at $\lambda = 0$. The $y \to \theta$ substitution is what made the check decisive.

- **§5.2 (noise).** I checked the linear-recursion algebra by direct simulation of $\xi' = (1-g)\xi + g\varepsilon - \rho$ with $v = 1/4$: $0.013558$ vs formula $0.013558$ ($g = 0.1$), $0.083339$ vs $0.083349$ ($g = 0.5$), $0.004083$ vs $0.004085$ ($g = 0.03$). The small-gain optimum and the $0.77\,R^3/v$ constant also match numerical minimization. Not landed in the body. As a model of the edge estimator it treats $v$ as constant and lets drift run unbounded; verify-1's own run on the real estimator was about 7% off for those reasons. It is parked in the schema's Working Notes at `conditional` at most.
- **§6 (discount convention).** Landed as a named convention in the allocation segment. Only the derived facts are stated: per-observation is exactly $\pi(1-\lambda)$, per-step is at most $\pi$, both approach $\pi$ as $\lambda \to 0^{+}$, and per-step needs $\lambda \gt 0$ for $\pi \lt 1$. The §6 per-step formula is not landed: it is 10–15% low at the points above.

So no new claim lands at full tier on the verifier's word alone. Every landed claim was re-derived by a second agent or checked by a second agent's measurement.

## Where the work order was wrong or incomplete

- **§7 undercounts carriers.** The posture segment names the old instance at 12 sites, not 3. OUTLINE line 333 also carries a direct "Proposition C.2 … half the strategic design space" sentence besides the "half of which" phrase. The F73 lower-bound-only form $\varepsilon \gt \rho_\Sigma(n_{\max}+1)/R_\Sigma$ sits in `#deriv-edge-credence-dynamics` at three places (SA3 statement, structural-results bullet, derived-vs-chosen table) as well as the schema.
- **§6's per-step approximation** is low by 10–15% at the tested points, and the per-step convention is undefined at $\lambda = 0$ for $\pi \lt 1$.
- **§5.1's derivation** assumes a deterministic per-observation gain. That holds for per-observation discounting at the stationary count but not off it, and not for per-time-step discounting. The claim survives (the age route covers those cases), but its stated derivation does not reach that far.
- §2–§4 and the verdict hold. I found nothing that changes them.

## The grep the verifier asked for

The pattern "substitute a stationary count into a gain indexed by the pre-update count" appears in `#deriv-update-detection-latency` (Epistemic Status line 88 and the corollary). It replaces $n_{\min}$ by $n_{\text{eff}}$ inside $(n_{\min}+1)$, but the stated cap $\Omega(1/((1-\lambda)\varepsilon))$ is the correct order, since the true per-observation gain is $1/n_{\text{eff}} = 1-\lambda$. Harmless at $\Omega$-level; left unchanged. `#der-mood-timescale`'s $J(\lambda)$ is the standard EWMA error variance (re-derived), not this pattern. `form-consolidation-dynamics`, `deriv-l1-update-bias`, `impl-strategy-dynamics`, `result-sector-persistence-template` and `impl-scaffolded-logogenic` already carry $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$, with no slow-forgetting qualifiers.

## Not changed, deliberately

- `ref/prior-art-analysis/cluster_references/failure_diagnosis_and_persistence.md` is a generated concatenation of segments for the 2026-05-21 prior-art analysis (per its `00-impact-meta-summary.md`). It carries the old schema text verbatim. It is a dated snapshot, not canon; regenerating it is a prior-art-pipeline decision.
- `msc/verify-sector-condition-cluster-2026-05-20.md`, `audits/**`, `spikes/.integrated/spike-schema-strategy-persistence-strengthening-2026-05-20.md`: history layer. The supersession is recorded in `spikes/INDEX.md` and CHANGELOG.
- **File routing.** Per `doc/sop/spikes.sop.md`, the 05-31 spike (refuted, never in canon) belongs in `.archived/`, and verify-1 plus these notes, now landed, in `.integrated/`. Both paths are cited from `msc/inside-out-2026-10/` (HANDOFF and the scout maps), so the move is left to the coordinator.
- **NeurIPS Paper 2** (outside this repo): `~/src/neurips/02-unified-convergence-rl/adjudicated/residue.md` §4's "convention decision owed (SEG vs ALT1)" is moot. The paper's $1-\lambda$ is correct and its Key Lemma 2 $\approx$ can become $=$ (Prop B.1F). Flagged to the coordinator, not edited.

## Open, for whoever comes next

- Extend Prop EA.1 beyond averaging estimators (drift extrapolation) and to state-dependent allocation (UCB/Thompson), plausibly as a minimax over bounded drift sequences.
- Land §5.2 once a model of the edge estimator's noise is settled: bounded drift, state-dependent $v$. The candidate home is the schema's Discussion.
- A closed form for the per-time-step discount convention's effective rate.
