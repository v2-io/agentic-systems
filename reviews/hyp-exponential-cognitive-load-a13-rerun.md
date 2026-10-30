---
kind: review
author:
  name: Claude Opus 5.5 (TST lane integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/owner-review/integrator-items.md
  - msc/inside-out-2026-10/c1-lanes/tst.md
written: 2026-10-30
---

# `#hyp-exponential-cognitive-load`: the $\alpha \approx 0.118$ fit re-run, and the count form measured on real time

KR C.1 (integrator item A13). The integrator re-ran the owner review's circularity check before editing, then attempted the strengthen-first path (a non-circular measurement) and landed what it found in `fc204813`. The scripts are in `02-tst-core/empirical-discontinuity/`; the account is the second source above. An independent verifier comes after.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: a1c82543
- act: run
- line: measurement
- criterion: Does the Discussion's "first-pass git-history measurement" ($\alpha \approx 0.118$ at $d \le 25$, read as heuristic corroboration of the exponential form) measure time at all, or only the time estimator?
- committed: before
- outcome: broken
- recheck: `python3 reproduce_estimate_fit.py data/commits.json` in `02-tst-core/empirical-discontinuity/`; compare V0 (the saved estimate) with V2 (a formula with no per-file term)

The saved `commit_time_estimate` equals $10 + 5n + 0.15L$ to $10^{-12}$ minutes, and $\operatorname{corr}(d, n) = 0.998$. V0 reproduces $\alpha = 0.118$, $R^2 = 0.524$. V2 ($10 + 0.15L$) gives $\alpha = 0.121$, and V3 ($10 + 5n$, exactly linear) still gives $\alpha = 0.073$ while fitting worse than a line. The fit measures how lines changed grow with files changed in that repository; it cannot bear on the form.

## C2 (check)
- target: segment:hyp-exponential-cognitive-load
- at: fc204813
- act: run
- line: measurement
- criterion: Do the Discussion's three elapsed-time findings (positive association surviving a lines covariate; exponential coefficient $a$ zero or negative with power coefficient $b$ positive in $\log T = c + a\,d + b\log(1+d)$; power exponent 0.4–0.7 and 24-hour medians that flatten in the multi-author histories) reproduce from the histories named in `elapsed_time.py`'s header?
- committed: after
- outcome: confirmed
- recheck: dump each history with the `git log` command in `elapsed_time.py`'s header at the HEAD it names, then `python3 elapsed_time.py <logs>`; bootstrap seed 0, 2000 draws

Run by the integrator who wrote the paragraph, so this confirms reproduction, not independent judgment. The numbers in the paragraph were transcribed from the run's output; the interval for $b$ in ink reaches zero at the 60- and 240-minute caps, and the paragraph says so.

## C3 (check)
- target: segment:obs-software-epistemic-properties
- at: fc204813
- act: read-check
- line: derivation
- criterion: After the landing, does any live segment, OUTLINE or toolkit document still cite $\alpha \approx 0.118$ or the estimated-time fit as evidence for the exponential form?
- committed: after
- outcome: confirmed
- recheck: `grep -rn "0\.118\|FINDINGS.md\|METHODOLOGY.md" 01-aat-core 02-tst-core 03-llm-core 04-eli-core --include=*.md`, excluding `old-*` files

The remaining hits are in the toolkit README's §1, which states the number in order to show what it measures, and in `old-*` imports, whose fate is item H.2.
