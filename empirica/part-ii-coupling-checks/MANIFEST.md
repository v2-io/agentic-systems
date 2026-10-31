# MANIFEST — part-ii-coupling-checks

*KR C.2 / C.1 / B.1 (`msc/inside-out-2026-10/INTENT.md`). Exact enumerations and small simulations that Part II's identification, goal-dependence and distortion segments lean on. Registered 2026-10-30 at the Part II round-2 integration; the scripts entered from the two 2026-10-30 spikes (`spikes/spike-loop-identification-decision-state-2026-10-30/`, `spikes/spike-allocation-vs-distortion-coupling-2026-10-30/sims/`) and their checks, which remain there as reasoning trail.*

**Vivarium-rerun status: not-applicable** for the exact enumerations (they are finite computations over a stated joint law, reproducible by hand); **planned** for the three simulations (route-3 confounding of the $M_t$-stratum), which are the kind of thing an authored world can rerun with ground truth.

**Publication disposition:** reproducibility supplement for the Part II identification and coupling results.

## What each piece computes, and who leans on it

Every claim below is *[Exact]* unless marked *simulation*; "exact" here means a finite enumeration over a stated joint law, with fractions where the script uses them.

| Piece | What it computes | Tier | Consuming segments |
|---|---|---|---|
| `check-part-ii-check-1-kappa0-action-collider.py` | A fair persistent world bit, a fair exogenous goal, $a_0 = G$ w.p. $0.9$, event $(a_0, o_1)$ with $o_1 = W \oplus a_0$, goal-blind update $M_1 = o_1$: $I(G; M_1 \mid e_1) = 0$ with $H(G \mid e_1) = 0.469$ bits, and the $M_1$-stratum confounded ($0.82$ vs $0.50$) while the $X_1$-stratum is not | exact | `#def-value-object` (premise 1, Record 1), `#der-directed-separation` (Record 3) |
| `check-part-ii-check-1-nogo-scope.py` | All 16 deterministic one-step environments $g(\theta, a)$: with a private coin stored in $X_1$, 16 on-policy-law classes and every untaken effect identified; with the policy deterministic in the chronica, 4 classes and untaken effects not identified | exact | `#der-loop-interventional-access` (the no-go and its complement) |
| `check-feedback-1-lemma1b-pstream.py` | Two-step enumeration: retaining past actions does not restore ignorability under a shared coin source; retaining the coins does | exact | `#der-loop-interventional-access` (coin-retention clause) |
| `check-feedback-1-kappa-collider.py` | The collider at $M_t$ at $\kappa_{\text{processing}} \gt 0$ | exact | `#def-value-object` (premise 1) |
| `check-part-ii-check-1-right-rung-rh-not-in-pi.py` | A prefix-closed two-member class with (SO) holding whose stitched replanner is not a member: $A_O^{\text{RH}} = 15 \gt A_O^{\text{B}} = 6$ | exact | `#def-value-object`, `#deriv-convention-monotonicity` (the (M) hypothesis) |
| `check-part-ii-check-1-onpolicy-test-detects.py` | The edge-credence learner at $\varepsilon = 0$ with deterministic tie-breaks: inside one $M_t$-stratum, $\mathbb E[o \mid X_t, a = 1]$ ranges $0.19$–$0.81$ over cells with $n \gt 200$; the on-policy sufficiency test fails, so it refutes rather than passes for free | simulation (200 000 episodes, seed 7) | `#def-value-object`, `#der-loop-interventional-access`, `#def-model-sufficiency` (the one-sided test) |
| `sim-strategy-counts-confound.py` | Route 3 of the $M_t$-form: a directed-separated agent whose Beta counts track a hidden regime; $M_t$-stratified on-policy exceeds interventional by $+0.09$ to $+0.11$ at $\varepsilon \in \{0.2, 0.05, 0\}$, $X_t$-stratified gap $\lt 0.001$ | simulation (40 000 episodes, seed 1) | `#def-value-object` (route 3, "roughly a tenth") |
| `check-feedback-1-singular-trajectory.py` | The same on one long trajectory with a switching regime: gap $+0.21$, $+0.20$, $+0.09$ at hazards $0.0005$, $0.005$, $0.05$; binned-$G$ gap $\lt 0.003$ | simulation (2 000 000 steps, seed 1) | `#def-value-object` (route 3, "two-tenths") |
| `check-feedback-1-eps0-identified-vs-truth.py` | At $\varepsilon = 0$, the identified untaken-action effect at a coarsening against the hidden-$\theta$ truth: max error $0.034$ over 41 cells | simulation (seed 7) | `#der-loop-interventional-access` (identification at a coarsening) |
| `distortion-check.py` | The C3 spike's N1–N12: the log-ratio-range identity and bounds, $\kappa$ as recoverability (N2, N9), allocation at $\kappa = 1$ with reliability $0$ (N8), the goal-informative principal (N7α/β), ignorable vs content-dependent dropping (N5), the misspecified tilt (N4), the 5a tie (N6, N10) | exact | `#der-directed-separation`, `#scope-observation-ambiguity-modulation`, `#der-orient-cascade` |
| `distortion-check-1.py` | K1–K8 and K2b: the Bennett bound on the tilt (tight on 20 000 instances; the four segment values); per-goal miscalibration of a goal-blind filter when the goal is evidence ($0.1927$; $0.1855$ with the action pinned); the encode-then-ignore report with reliability $0$ and the recalibration identity ($0.3301 \to 0.2881$); the retired numerator's zero under the pin; $\theta \leq \sqrt{\mathrm{KL}}$ on 20 000 pairs; the 5a cost qualifier; the operating-law $0/0$ for an injective policy and the probe-law $\kappa = 1$ | exact | `#der-directed-separation` ((NWI), clause 3, the norm, the probe law), `#scope-observation-ambiguity-modulation` (Bennett, the no-go on an ambiguity factor), `#deriv-observation-ambiguity-bias-bound` (the global constant), `#der-orient-cascade` (5a) |

Consumers cite this entry as `empirica:part-ii-coupling-checks`. The bodies state each instance self-contained; the scripts are how to reproduce them, not what the claims rest on.

## Provenance

The scripts were written by the C2 and C3 spikers (2026-10-30), their de-novo verifiers, the round-1 integrator and the round-1 independent checkers (`reviews/part-ii-check-1*.md`); the round-2 integrator re-ran every one from this directory (RUNS.md) and re-derived by hand the recalibration identity, the goal-informativeness identity and the global Fisher–Rao constant that `distortion-check-1.py` checks numerically.
