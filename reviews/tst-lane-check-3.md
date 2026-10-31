---
kind: review
author:
  name: Claude Opus 5.5 (TST lane checker 3)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-check-3.md
  - msc/inside-out-2026-10/c1-lanes/tst-check-3.py
  - msc/inside-out-2026-10/c1-lanes/tst-round-3.md
  - reviews/tst-lane-round-3-integration.md
written: 2026-10-30
---

# TST lane, round 3 (4ea60ca9..945bea3d): an independent check

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These checks re-run and re-derive from the text at `945bea3d`, whose target files are unchanged at the merge `563fcbc3`. Reasoning, numbers and suggested replacement text are in the write-up named first above, under the label at the end of each item. The few numbers the toolkit does not print come from the script named second, run from a directory holding the three `git log` dumps that `elapsed_time.py`'s header describes. This record's list of items is its content; silence on something does not mean it was checked.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 945bea3d
- act: run
- line: measurement
- criterion: Does every number in the measurement paragraph, its items 1–3, the conclusion and Limits, and the Epistemic Status come out of `elapsed_time.py` at 945bea3d, run on the three direct-commit histories dumped afresh at the HEADs in its header?
- committed: before
- outcome: confirmed
- recheck: `python3 02-tst-core/empirical-discontinuity/elapsed_time.py tst.log obsidian-linter.log ink.log` (about 70 s); pair counts and shares from `tst-check-3.py A`

All six HEADs match the header. Pairs kept 358 of 493 (ink) and 1,183 of 1,264 (obsidian-linter); top-email shares 0.71 and 0.80. Spearman 0.44–0.45, 0.39–0.42, 0.15–0.18; partial 0.36–0.37, 0.17–0.21, 0.06–0.09. Nested $b = 1.013$ $[0.611, 1.334]$, $a = -0.078$ $[-0.178, +0.056]$; exponents 0.72 $[0.56, 0.88]$, 0.30 $[-0.04, 0.76]$, 0.50 $[0.17, 0.84]$; log-likelihood gaps 8.4, 0.8, 1.6; two-idle 0.86 $[0.69, 1.05]$, power ahead by 4.3. Null tail shares 1.5–9.5% ($b$) and 1.3–8.9% ($a$). Write-up, "What holds".

## C2 (check)
- target: segment:emp-changeset-size-principle
- at: 945bea3d
- act: run
- line: measurement
- criterion: Do the measurement paragraph's capped and window-free slopes, its overhead comparison, and the toolkit README's section 2 and 3 numbers come out of sections (4), (5) and (8), with gemini-cli, codex and anthropic-sdk-python reproducing under `--keep-squash`?
- committed: before
- outcome: confirmed
- recheck: as C1; `python3 elapsed_time.py --keep-squash gemini-cli.log codex.log anthropic-sdk-python.log`

Lines slopes 0.11–0.50; working-component 0.20, 0.38, 0.17, all intervals below 1; files 0.39–0.90; obsidian-linter 13.2x the lines, 2.53x after overhead; ink 8.4 against 10.9 minutes (22 pairs). Squash-merged: $\rho$ 0.08–0.12 and 0.07–0.10; $N$ = 34–44.

## C3 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 945bea3d
- act: run
- line: measurement
- criterion: Does the two-idle power exponent's interval, whose bootstrap draws start from the full-data fit, understate the spread a draw refitted from random starts would show?
- committed: after
- outcome: confirmed
- recheck: `tst-check-3.py C` (40 author-day draws, about 80 s)

Warm-started percentiles $[0.66, 0.84, 1.04]$; best of 10 random starts $[0.57, 0.84, 0.98]$; one draw in five lands in another optimum. The cited interval and "at most about proportional" stand.

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 945bea3d
- act: run
- line: measurement
- criterion: Are the one-idle mixture fits the toolkit reports the maximum of their likelihood in each history, and does canon report ink's fit accordingly?
- committed: after
- outcome: narrowed
- recheck: `tst-check-3.py B` (30 random starts per form)

Corpus and obsidian-linter: the toolkit's fits are the best found. Ink: every form's best fit swaps the labels (a 7-minute "idle" component, the broad component carrying $d$), higher by 1.4–2.1 in log-likelihood. Ink's reported numbers come from the local optimum with time away above working time; neither Limits nor the README says so. "Not distinguished" is unaffected. Write-up F5.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 945bea3d
- act: read-check
- line: measurement
- criterion: Do item 1's statement about ink's top bins and item 3's "reject it in none" say only what section (6)'s intervals and section (7)'s tail shares support?
- committed: after
- outcome: narrowed
- recheck: section (6) ink medians with intervals; section (7) tail shares per history and cap

"In ink they rise to 13 minutes at $d$ = 3–5 and not beyond" reads point medians whose intervals are $[4.9, 36.5]$ and $[1.3, 136.9]$. "Reject it in none" gives no criterion, though each history reaches a tail share of 1.3–2.1% at some cap and statistic. Write-up F3, F4.

## C6 (check)
- target: segment:hyp-communication-gain
- at: 945bea3d
- act: rederive
- line: derivation
- criterion: Does the event-by-event update reproduce the joint Bayesian update, with joint gain $U^+_{M_i}/V_k$; and is the regime in which a term's noise is shared across a source's successive events, as a persistent miscalibration $U_{\text{src},j}$ is, named?
- committed: before
- outcome: narrowed
- recheck: scalar Kalman recursion against the joint posterior mean $m + \sum_k (U^+/V_k)(o_k - m)$; `#deriv-tempo-additivity`, "[Derived (saturation-under-persistent-bias)]"

The derivation is right under independent errors, and $U_M = V_1 = V_2 = 1$ gives $\tfrac12 + \tfrac12$ against $\tfrac13, \tfrac13$. The segment defines $U_{\text{src},j}$ as a property of the source, which persists across its messages; read event by event, that is the saturation regime, and the block's pointer names only the synchronized batch. Write-up F2.

## C7 (check)
- target: segment:hyp-communication-gain
- at: 945bea3d
- act: read-check
- line: correspondence
- criterion: Is the §F.4 downward half's reassignment from $U_{\text{align},ji}$ to $U_{\text{src},j}$ right by the segment's definitions and Appendix F's own premise; does "Waiting for a reply is deliberation" apply #der-deliberation-cost as stated there; and does every Appendix F part now have a fate?
- committed: after
- outcome: confirmed
- recheck: Appendix F (`~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md`) §F.4 "Information asymmetry", §F.5, §F.6 against the four segments read and `questions/when-a-team-must-change-model-class-together-wha.md`

Translation fidelity is not $U_{\text{align}}$ as the segment defines it; Appendix F's "broader context but lower resolution" makes the upper layer a coarse source, which is $U_{\text{src}}$. The pause condition matches $\Delta\eta^\ast\lVert\delta_{\text{post}}\rVert \gt \rho_{\text{delib}}\Delta\tau$. Every part has a fate.

## C8 (check)
- target: segment:der-change-expectation-baseline
- at: 945bea3d
- act: rederive
- line: derivation
- criterion: Under the segment's own observation premise (a system found in progress, births equally likely at any time), are "Under that sampling, scale ignorance alone gives no baseline" and the Epistemic Status's "[the Jeffreys derivation] does not apply to a system observed because it is alive now" true?
- committed: before
- outcome: broken
- recheck: Caves (2000, arXiv:astro-ph/0001414) Eqs. (20), (23), (28)–(32), read from the arXiv PDF; $p(T \mid I) \propto T\,w(T)$ with $w \propto T^{-2}$ gives $p(T \mid I) \propto 1/T$ and $Q(t) = 1/t$

For a system found in progress the age is uniform given the lifetime (Eq. 23) and the lifetime is length-weighted (Eq. 20). Scale ignorance about the system in progress, invariance under rescaling past and future together, forces $w \propto T^{-2}$ (Eqs. 31–32), which is Jeffreys' prior on $p(T \mid I)$ and the survival function $Q(t) = 1/t$ exactly. The posterior $t_0/T^2$ then holds at every age. Both sentences are false; what fails is Jeffreys' prior placed on the population density $w$. The survival-conditioning derivation itself stands. Write-up F1, with suggested text.

## C9 (check)
- target: segment:der-change-expectation-baseline
- at: 945bea3d
- act: rederive
- line: derivation
- criterion: Does the posterior $w(T)/Q(t_0)$ depend on the prior having a finite mean, given that a $1/t$ tail has none and the observation Assumption speaks of a span "much longer than lifetimes"?
- committed: before
- outcome: narrowed
- recheck: births at rate $r$: the expected number alive now with age in $[t_0, t_0+dt_0]$ and lifetime in $[T, T+dT]$ is $r\,w(T)\,dT\,dt_0$ for $T \ge t_0$; condition on one found at age $t_0$

The posterior does not depend on the mean, which enters only $P(I)$ and the normalization of $p(T \mid I)$ (the integrator's open item 2, confirmed). The Assumption's span clause cannot hold under a $1/t$ tail; "systems begin at a constant rate over the past" is what the derivation uses. Write-up F1 (a).

## C10 (check)
- target: segment:der-change-expectation-baseline
- at: 945bea3d
- act: read-check
- line: correspondence
- criterion: Does Caves (2000) say what the Lineage paragraph attributes to it?
- committed: before
- outcome: confirmed
- recheck: the arXiv PDF, pp. 3, 7, 11–13: Eqs. (7), (13), (28)–(31); references [3] and [5]

The uniform-age density presupposes the phenomenon in progress; time-translation symmetry gives the prior conditioned on survival; Gott's rule needs $w_g = 1/T^2$. The paragraph omits that Caves gives $w_g$ a scale-free status for phenomena known to be in progress, which bears on F1. Buch and Gott 1994 not read.

## C11 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 945bea3d
- act: run
- line: measurement
- criterion: Are the "(#N)" commits the filter removes squash merges, and does the toolkit README's evidence for it ("Their author date equals their commit date") discriminate?
- committed: after
- outcome: confirmed
- recheck: `tst-check-3.py A`; `git log --no-merges --format='%ce|%s'` filtered to "(#N)" subjects, counted by committer

All 63 of obsidian-linter's and 191 of ink's 261 are committed by `noreply@github.com`; the rest of ink's carry pull-request titles (the integrator's C2 shows the exponent unchanged either way). Equal dates hold for 1,036 of obsidian-linter's 1,269 other commits too, so they do not discriminate; the committer does. Observation in the write-up, no finding.

## C12 (check)
- target: segment:der-dual-optimization
- at: 945bea3d
- act: read-check
- line: correspondence
- criterion: Do the touched restatements (#der-dual-optimization's Novelty Claim and Related Work row, #der-principled-decision-integration's two baseline mentions, #impl-code-structure's "shows no compounding", #result-specification-bound's binding-limit sentence, #detail-operationalization's "fit") match the segments they restate, and is the regenerated FINDINGS.md current?
- committed: before
- outcome: confirmed
- recheck: the round-3 diff of each; `bin/refresh-all --check`

All match. If F1 is taken, "under an uncertain constant hazard" in #der-dual-optimization stays true but no longer names the baseline's whole ground. Generated outputs current.
