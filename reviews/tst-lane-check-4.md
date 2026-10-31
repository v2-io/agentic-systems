---
kind: review
author:
  name: Claude Opus 5.5 (TST lane checker 4)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-check-4.md
  - msc/inside-out-2026-10/c1-lanes/tst-check-4.py
  - msc/inside-out-2026-10/c1-lanes/tst-round-4.md
  - reviews/tst-lane-round-4-integration.md
written: 2026-10-31T04:05:00Z
---

# TST lane, round 4 (merge a1fa9024): an independent check

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These checks re-derive and re-run from the text at `a1fa9024`; every target file is identical at the landing `0201c156` and at HEAD `e9578b96`. Reasoning, numbers and suggested replacement text are in the write-up named first above. Numbers the toolkit does not print come from the script named second, run from a directory holding the three `git log` dumps that `elapsed_time.py`'s header describes, at the HEADs it names. This record's list of items is its content; silence on something does not mean it was checked.

## C1 (check)
- target: segment:der-change-expectation-baseline
- at: a1fa9024
- act: rederive
- line: derivation
- criterion: Does Jeffreys' prior on the lifetime of the system in progress with the uniform-age likelihood give $t_0/T^2$ and median remaining life $t_0$ at every age; under a constant birth rate, does item 1's $w(T)/Q(t_0)$ hold whatever the mean, does item 2 (in-progress lifetime $\propto T\,w(T)$, uniform age, Jeffreys on it forces $w \propto T^{-2}$, $Q = 1/t$) follow, does the rescaling form give the same $w$, and does Jeffreys on $w$ fail to normalize after survival?
- committed: before
- outcome: confirmed
- recheck: by hand; count alive $r\,w(T)\,dT\,dt_0$ for $T \ge t_0$; $p(\alpha t_p, \alpha t_f)\alpha^2 = p(t_p, t_f)$ with $p \propto w(t_p + t_f)$ gives $w(\alpha T) = w(T)/\alpha^2$

All hold. Item 2 follows from the birth-rate count directly, item 1 then giving the same posterior. The main derivation's likelihood holds under both samplings; the prior it is placed on is the drawn system's $w$ under one and $T\,w(T)$ under the other, which the "whose lifetime" subsection explains. Write-up, "What holds".

## C2 (check)
- target: segment:der-change-expectation-baseline
- at: a1fa9024
- act: rederive
- line: derivation
- criterion: Does the hazard-mixture route give median remaining life $\sim t_0$ (for a prior finite and positive at zero hazard) under the segment's stated observation, the uniform-age likelihood that the main derivation says holds under per-system sampling and a constant birth rate alike?
- committed: before
- outcome: narrowed
- recheck: by hand: with $f \sim c\,k^{a-1}$, $w \sim c\,\Gamma(a+1)T^{-(a+1)}$; survival-only posterior $w/Q(t_0)$, tail exponent $a$; uniform-age posterior $\propto w(T)/T$, tail exponent $a+1$; $f \propto 1/k$ gives $w = 1/T$. Simulation `tst-check-4.py hazard`, $f(k) = e^{-k}$

Survival-only: median remaining life over $1 + t_0$ of 0.95–1.03 at $t_0$ = 10, 30, 100 (one system at an unrelated time; hazards varying across systems met alive). Uniform-age (per-system sampling): 0.40–0.42, against $\sqrt2 - 1 = 0.414$. The route holds only for a prior on systems in general observed through survival, a premise round 4 removed from the text. This check's finding is the write-up's F1.

## C3 (check)
- target: segment:der-change-expectation-baseline
- at: a1fa9024
- act: read-check
- line: correspondence
- criterion: Do the segment's Formal Expression, Epistemic Status and Lineage say only what Caves (2000) says about $w_g$, its scale-free status for a phenomenon in progress (Eqs. 31–32), and case-by-case appropriateness?
- committed: before
- outcome: confirmed
- recheck: arXiv:astro-ph/0001414, text extracted from the PDF, pp. 12–13, Eqs. (30)–(32) and the two paragraphs after; p. 13 on human institutions

Faithful. Caves also contrasts $w_g$ with Jeffreys' prior explicitly and calls Gott's analysis flawed; the segment marks its own reading as its own, and a clause naming Caves's contrast would help (write-up, smaller points; F8).

## C4 (check)
- target: segment:hyp-communication-gain
- at: a1fa9024
- act: rederive
- line: derivation
- criterion: With $o_n = \theta + s + e_n$, $s$ shared and $e_n$ fresh, does the posterior variance of $\theta$ saturate at $(1/U_0 + 1/U_s)^{-1}$ while a fresh-noise update tends to zero; and are the sentences around the new paragraph consistent with it?
- committed: before
- outcome: narrowed
- recheck: sample mean sufficient with variance $U_s + U_e/n$; `#deriv-tempo-additivity` "[Derived (saturation-under-persistent-bias)]"

The saturation holds. The floor omits persistent misalignment, which the same paragraph says persists, and the Epistemic Status still calls $U_{\text{src},j}$ unstructured. This check's finding is the write-up's F3.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: a1fa9024
- act: run
- line: measurement
- criterion: Does `elapsed_time.py` at a1fa9024 print every line the round-3 script printed, unchanged, plus the two new lines per history, and do those give the numbers item 1, item 3, Limits and the README cite?
- committed: before
- outcome: confirmed
- recheck: dumps made afresh at the header's HEADs (all three match); both scripts run; `diff` of outputs

Only the two new lines differ. Smallest share 0.015, 0.013, 0.020; null matches 0.047, 0.058, 0.062. Ink's best of 30 starts $-912.9$, $-912.2$, $-912.2$ against reported $-915.0$, $-914.2$, $-913.6$, labels swapped; corpus and obsidian-linter equal reported. Ink's top-bin intervals $[4.9, 36.5]$, $[1.3, 136.9]$.

## C6 (check)
- target: segment:hyp-exponential-cognitive-load
- at: a1fa9024
- act: run
- line: measurement
- criterion: Does item 3's reading ("All three sit at the edge of a 5% test, within the simulation's error of it"; "alone, settle it in none") hold when section (7)'s statistic is computed with enough replicates that Monte Carlo error is small beside the distance to 5%?
- committed: before
- outcome: narrowed
- recheck: `tst-check-4.py minp` at 10,000 replicates (seeds 99 and 7) and 5,000 (seed 12, extending the shipped draws); twenty seeds at 1,000; pooled (exchangeable) form beside the shipped one

At 10,000: corpus 0.065, obsidian-linter 0.035, ink 0.061–0.062 (s.e. 0.0022); pooled differs by under 0.001. At 1,000 the shipped statistic's s.d. across seeds is about 0.011, not the cited 0.007. Obsidian-linter's capped fits alone reject a pure exponential at 5%; the corpus's and ink's do not. This check's finding is the write-up's F2.

## C7 (check)
- target: segment:hyp-exponential-cognitive-load
- at: a1fa9024
- act: run
- line: measurement
- criterion: Are all 63 of obsidian-linter's and 191 of ink's "(#N)" commits committed by the web interface's merge, and do equal author and commit dates fail to discriminate, as the README now says?
- committed: before
- outcome: confirmed
- recheck: `git log --no-merges --format='%ce|%s'` and `'%at %ct|%s'` in both repositories at the header's HEADs

63 of 63 and 191 of 261 by `noreply@github.com` (ink's others: 51 and 19 by two maintainers). Equal dates in 1,036 of 1,269 and 354 of 403 non-"(#N)" commits.

## C8 (check)
- target: segment:der-dual-optimization
- at: a1fa9024
- act: read-check
- line: correspondence
- criterion: Do the Novelty Claim and Related Work row match the restructured baseline, and is the regenerated `FINDINGS.md` current?
- committed: before
- outcome: confirmed
- recheck: the round-4 diff; `bin/extract-findings` in a worktree at a1fa9024, no diff in `FINDINGS.md` or `doc/readme/src/_findings-summary.md`

Both match; "survival analysis under ... an uncertain constant hazard" already carries F1's premise in the word "survival".

## C9 (check)
- target: segment:der-change-investment
- at: a1fa9024
- act: read-check
- line: correspondence
- criterion: Does the Epistemic Status's list of assumptions inherited from #der-change-expectation-baseline include the premise round 4 made governing, no time scale known for the system's lifetime?
- committed: before
- outcome: narrowed
- recheck: `02-tst-core/src/der-change-investment.md` Epistemic Status, against the baseline's Epistemic Status at a1fa9024

The list names median prediction and uniform feature rate only. This check's finding is the second half of the write-up's F4.

## F4 (finding)
- target: segment:der-change-expectation-baseline
- at: a1fa9024

The opening sentence's premise, "Absent specific information about a software system's future", is weaker than the one the derivation needs and the Epistemic Status states, no time scale known for the system's lifetime; Caves (p. 13) names human institutions as phenomena with identifiable time scales. The Discussion's "sunsetting next quarter" item reads as an update to a baseline the Epistemic Status says does not apply there. Suggested text in the write-up, F4.

## F5 (finding)
- target: segment:hyp-exponential-cognitive-load
- at: a1fa9024

Item 2 gives ink's exponent 0.30 $[-0.04, 0.76]$ and log-likelihood gap 0.8 from the one-idle fit that Limits calls a chosen local optimum, without saying so where the numbers appear. "Not distinguished" holds at both optima; the numbers want an inline qualifier. Write-up F5.

## F7 (finding)
- target: segment:impl-foundations-features
- at: a1fa9024

The baseline paragraph's robustness claim, "The same baseline follows, at large age, from any unknown constant termination hazard whose prior density at zero hazard is finite and positive", inherits C2's finding (write-up F1): it holds for a prior on systems in general observed through survival, and not under the uniform-age likelihood. Write-up F1.

## F8 (finding)
- target: segment:der-change-expectation-baseline
- at: a1fa9024

Two small precisions. "Both $\pi \propto 1/T$ and $w \propto T^{-2}$ are improper near zero": $\pi$ is improper at both ends. The Lineage would be safer naming that Caves himself contrasts $w_g$ with Jeffreys' prior (his Jeffreys' prior being on $w$) and calls Gott's analysis flawed, so that the segment's reading is not attributed to him. Write-up, smaller points.
