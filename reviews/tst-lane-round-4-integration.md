---
kind: review
author:
  name: Claude Opus 5.5 (TST lane round-4 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-round-4.md
  - msc/inside-out-2026-10/c1-lanes/tst-check-3.md
  - reviews/tst-lane-check-3.md
written: 2026-10-30
---

# TST lane, round 4: the integrator's re-runs and re-derivations

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These are the checks I re-ran or re-derived while integrating `reviews/tst-lane-check-3.md`, read against the text at `0201c156`, which is the round-4 commit rebased onto main at `eba69748`; no target file differs between that rebase base and the base the check read. They are the integrator's own; an independent verifier comes after. The account is the first source above. The histories are the same dumps as round 3, at the HEADs in `elapsed_time.py`'s header. C1 and C3 used a scratch simulation, described in each item so it can be rebuilt.

## C1 (check)
- target: segment:der-change-expectation-baseline
- at: 0201c156
- act: rederive
- line: derivation
- criterion: With Jeffreys' prior $\pi(T) \propto 1/T$ on the lifetime of the system in progress and $p(t_0 \mid T) = 1/T$ for $t_0 \le T$, is the posterior $t_0/T^2$ at every age with median remaining life $t_0$; under a constant birth rate, is a system found in progress distributed as $T\,w(T)$ with uniform age, its posterior given age $w(T)/Q(t_0)$ whatever the mean lifetime, and does Jeffreys on it force $w \propto T^{-2}$ with $Q(t) = 1/t$; and does Jeffreys placed on $w$ fail to normalize after conditioning on survival?
- committed: before
- outcome: confirmed
- recheck: $\int_{t_0}^\infty T^{-2}dT = 1/t_0$; expected count alive with age in $dt_0$ and lifetime in $dT$ is $r\,w(T)\,dT\,dt_0$ for $T \ge t_0$; $T \cdot T^{-2} = 1/T$; $\int_{t_0}^\infty T^{-1}dT = \infty$. Simulation: $10^7$ systems, lifetimes from $w \propto T^{-2}$ on $[1, 10^3]$, births uniform over the last $10^3$, observed at the end; among those alive with age within 5% of $t_0$

69,213 alive. Median remaining life over age: 0.937, 1.009, 1.034 at $t_0$ = 3, 10, 30 (about 1,000 systems each), against 0.994, 0.980, 0.942 exact for the truncated $w$. The share of alive systems in six equal bins of $\log T$ over $[2, 500]$ is 0.165–0.168, flat, so $p(T \mid I) \propto 1/T$.

## C2 (check)
- target: segment:der-change-expectation-baseline
- at: 0201c156
- act: read-check
- line: correspondence
- criterion: Does Caves (2000) say that invariance of $p(t_p, t_f \mid I)$ under rescaling past and future together forces $w \propto T^{-2}$, that $w_g$ has for a phenomenon in progress the scale-free status Jeffreys' prior has before observation, and that whether scale-free prior information is appropriate must be judged case by case?
- committed: before
- outcome: confirmed
- recheck: arXiv:astro-ph/0001414, text extracted from the PDF, pp. 12–13, Eqs. (31)–(32) and the paragraph after them

"$w_g(T)$ has a scale-free status similar to that found by Jaynes for the Jeffreys prior"; "$w(\alpha T) = w(T)/\alpha^2$, which implies that the prior density has the form (31)"; "Whether the scale-free prior information is appropriate must be judged case by case; it is not a universal rule." The naming of $p(T \mid I) \propto 1/T$ as Jeffreys' prior on the system in progress is the checker's and this segment's, not Caves's; the segment's Lineage says so.

## C3 (check)
- target: segment:hyp-communication-gain
- at: 0201c156
- act: rederive
- line: derivation
- criterion: With messages $o_n = \theta + s + e_n$ from one source, $s \sim N(0, U_s)$ shared and $e_n \sim N(0, U_e)$ fresh, prior $\theta \sim N(0, U_0)$, does the posterior variance of $\theta$ saturate at $(1/U_0 + 1/U_s)^{-1}$, while an update charging $U_s + U_e$ afresh to each message drives it to zero?
- committed: before
- outcome: confirmed
- recheck: the sample mean is sufficient, with variance $U_s + U_e/n$ about $\theta$; $U_0 = 1$, $U_s = 0.25$, $U_e = 0.5$, $n$ = 1, 10, 100, 10,000

Exact: 0.4286, 0.2308, 0.2032, 0.2000 against the floor 0.2000. Fresh-noise update: 0.4286, 0.0698, 0.0074, 0.000075. The saturation is #deriv-tempo-additivity's persistent-bias theorem at one source.

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0201c156
- act: run
- line: measurement
- criterion: Does `elapsed_time.py` at 0201c156 print every line the round-3 script printed, unchanged, plus the two new lines, and do the new lines give the numbers Item 3 and Limits cite?
- committed: before
- outcome: confirmed
- recheck: `python3 elapsed_time.py tst.log obsidian-linter.log ink.log`; `diff` against the round-3 output with the two new lines removed (no difference)

Section (7), smallest of eight tail shares and the null's match: corpus 0.015 and 0.047, obsidian-linter 0.013 and 0.058, ink 0.020 and 0.062. Section (6), best of 30 random starts: obsidian-linter and the corpus equal the reported fits for all three forms; ink's best exceed the reported by 2.1 (exponential), 2.0 (power), 1.4 (nested), each with a 7-minute "idle" component and labels swapped. Monte Carlo error of a 0.05 share at 1,000 replicates is $\sqrt{0.05 \cdot 0.95/1000} = 0.007$.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0201c156
- act: read-check
- line: measurement
- criterion: Does item 1 read ink's two top bins by their intervals (11.8 $[4.9, 36.5]$ and 6.7 $[1.3, 136.9]$), not their point medians, here and in the README?
- committed: before
- outcome: confirmed
- recheck: section (6) medians line for ink; item 1 and README §2's first bullet
