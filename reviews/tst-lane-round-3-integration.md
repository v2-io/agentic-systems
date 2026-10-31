---
kind: review
author:
  name: Claude Opus 5.5 (TST lane round-3 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-round-3.md
  - msc/inside-out-2026-10/c1-lanes/tst-check-2.md
  - reviews/tst-lane-check-2.md
written: 2026-10-30
---

# TST lane, round 3: the integrator's re-runs and re-derivations

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These are the checks I re-ran or re-derived while integrating `reviews/tst-lane-check-2.md`, read against the text landed in `0bc90f7d`. They are the integrator's own; an independent verifier comes after. The account, with the reasoning and every place I departed from the check, is the first source above. The three direct-commit histories were dumped at the HEADs in `elapsed_time.py`'s header with the command there, and the three squash-merged ones likewise. Items C3 and C4 used scratch probes not kept in the repository; the account gives what they did, so they can be rebuilt.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Does every number in the Discussion's measurement paragraph and in the Epistemic Status come out of `elapsed_time.py` at 0bc90f7d, run on the three direct-commit histories with squash-merge pairs left out and author-day resampling?
- committed: before
- outcome: confirmed
- recheck: `python3 02-tst-core/empirical-discontinuity/elapsed_time.py tst.log obsidian-linter.log ink.log` (about 70 s)

Pairs 1,183 (obsidian-linter) and 358 (ink) at $d \le 25$, 277 (corpus); top-email shares 0.71 and 0.80; corpus 12 author-days. Spearman 0.39–0.45 and 0.15–0.18; partial 0.17–0.37 and 0.06–0.09. obsidian-linter medians 6.1, 12.1, 16.3, 33.6, 27.9 (last [15.9, 49.6]); ink 6.1, 7.1, 13.0, 11.8, 6.7. Nested $b = 1.013$ $[0.611, 1.334]$, $a = -0.078$ $[-0.178, +0.056]$; exponents 0.72 $[0.56, 0.88]$, 0.30 $[-0.04, 0.76]$, 0.50 $[0.17, 0.84]$; log-likelihood gaps 8.4, 0.8, 1.6. Capped $b$ 0.38–1.04. Forced rates 0.024–0.165 and 0.068–0.298. A 24-hour cap drops 0.13 at $d = 0$ and 0.27–0.35 at $d \ge 11$ in obsidian-linter.

## C2 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Do ink's and obsidian-linter's window-free results depend on which squash-merge rule is used (drop pairs with a squash commit at either end, only pairs ending in one, or remove those commits before pairing), or on counting ink's 70 locally committed "(#N)" commits as squash merges?
- committed: after
- outcome: confirmed
- recheck: refit section (6) under each rule; split ink's "(#N)" commits by committer (`git log --format='%ae|%ce|…'`; 191 committed through the web interface, 70 locally)

ink exponent 0.29, 0.30, 0.26 under the three rules, 0.30 with only the web-committed 191 treated as squash; obsidian-linter 0.72–0.73. All 261 of ink's "(#N)" commits have author date equal to commit date; the locally committed ones also carry pull-request titles. No conclusion depends on the rule.

## C3 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Is the one-idle mixture's fit the maximum of its likelihood, from 30 random starts per form, in each history?
- committed: after
- outcome: confirmed
- recheck: refit `mixture_em`'s model from 30 random starts (beta offset, idle mean, scales and shares drawn at random), compare log-likelihoods with the toolkit's fit

obsidian-linter and the corpus: the toolkit's fit is the best optimum found for every form. ink: a fit with slightly higher likelihood exists for each form ($-912.2$ against $-913.6$ for the nested form) in which the "idle" component has a median of 7 minutes, so labels have swapped and the component carrying $d$ is the long one. The toolkit's fit is the one whose idle component lies above its working component, which is the reading the method needs; either way ink does not distinguish the forms, which is what canon says.

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: With time away modelled by two idle components, what is obsidian-linter's power exponent at the likelihood's best optimum, and is the single-start figure the check cited (0.85 $[0.63, 1.00]$) that optimum?
- committed: after
- outcome: confirmed
- recheck: section (6) last line (best of 30 starts, bootstrap warm-started from it); and 30 random starts of the same model on the unfiltered pairs

Filtered: 0.86 $[0.69, 1.05]$, power ahead of exponential by 4.3 at the best optima; 3 distinct optima for the power form. A single start on the filtered pairs gave 0.74 with the exponential ahead by 1.8, a worse local optimum. Unfiltered: the best power optimum is 0.847, so the check's 0.85 was at it; its nested fit ($b = 0.988$, log-likelihood $-2934.9$) was not ($-2930.9$, $b = 0.749$). In ink the best optimum is a working spike of s.d. 0.17 beside an 8-minute idle component; in the corpus an idle component with a median of 141,060 minutes. Canon cites the variant for obsidian-linter only.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Against section (7)'s pure-exponential null, with squash-merge pairs left out and 1,000 replicates, how often are the observed $a$ and $b$ reached in each history, and does item 3's "lean against a pure exponential in every history and reject it in none" describe that?
- committed: before
- outcome: confirmed
- recheck: section (7)

$P(\text{null } b \geq \text{observed})$: obsidian-linter 0.039–0.095, ink 0.021–0.046, corpus 0.015–0.057. $P(\text{null } a \leq \text{observed})$: 0.013–0.079, 0.020–0.070, 0.041–0.089. The check's obsidian-linter figures (0.3–2% on $a$) were on pairs including squash merges with 300 replicates; dropping 81 pairs moved the fitted exponential (rate 0.243 to 0.261 on the log scale, idle median 606 to 509 minutes) and with it the null.

## C6 (check)
- target: segment:emp-changeset-size-principle
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Do the measurement paragraph's slopes and its overhead comparison come out of sections (4), (5) and (8) with squash-merge pairs left out?
- committed: before
- outcome: confirmed
- recheck: sections (5) and (8)

Capped lines slopes 0.11–0.50 (ink falls from 0.24 at a week to 0.11 uncapped); working-component 0.20 $[0.05, 0.49]$, 0.38 $[0.29, 0.67]$, 0.17 $[-0.02, 0.36]$; files 0.68 $[0.29, 1.50]$, 0.90 $[0.69, 1.27]$, 0.39 $[0.05, 0.75]$. obsidian-linter: 13.2 times the lines (24 against 318), 2.53 times the working time with the 0–10 bin subtracted. ink: 8.4 minutes in the 201–1000 bin (22 pairs) against 10.9 in the 11–50 bin, so the ratio is not defined.

## C7 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 0bc90f7d
- act: run
- line: measurement
- criterion: Run with `--keep-squash`, do gemini-cli and codex give Spearman $\rho \approx 0.1$ under caps of 60–240 minutes, as the Discussion's last sentence on squash-merged histories says?
- committed: before
- outcome: confirmed
- recheck: `python3 elapsed_time.py --keep-squash gemini-cli.log codex.log anthropic-sdk-python.log`, section (1)

gemini-cli 0.08–0.12, codex 0.07–0.10; anthropic-sdk-python $N$ = 34–44.

## C8 (check)
- target: segment:hyp-communication-gain
- at: 0bc90f7d
- act: rederive
- line: derivation
- criterion: In the scalar Gaussian location model with independent errors, does applying the terms one at a time, each with the gain at the then-current $U_{M_i}$ and $U_{M_i}$ updated after it, reproduce the joint posterior; does the joint update give term $k$ the gain $U^+_{M_i}/V_k$; and do separately computed gains summed against one prior overcount?
- committed: before
- outcome: confirmed
- recheck: joint posterior mean $m^+ = U^+(m/U_M + \sum_k o_k/V_k) = m + \sum_k (U^+/V_k)(o_k - m)$; single term $U^+/V = U_M/(U_M+V)$; numerically, 5 random draws of $U_M$, four $V_k$ and observations, sequential against joint mean and variance

Sequential and joint agree to $10^{-12}$ in every draw. With $U_M = V_1 = V_2 = 1$ the separate gains are $\tfrac12$ each, summing to 1; the joint gains are $\tfrac13$ each.

## C9 (check)
- target: segment:der-change-expectation-baseline
- at: 0bc90f7d
- act: rederive
- line: derivation
- criterion: Given $Q(t) \sim c/t$, does $Q(t_0+u)/Q(t_0) \to t_0/(t_0+u)$ with median remaining life $\sim t_0$; does a hazard prior with $0 \lt f(0) \lt \infty$ give $S(t) \sim f(0)/t$; and does Jeffreys' prior conditioned on survival alone fail to normalize, while with $p(t_0 \mid T) = 1/T$ it gives $t_0/T^2$?
- committed: before
- outcome: confirmed
- recheck: ratio of the asymptotic forms; Watson's lemma with $a = 1$ (as checked in `reviews/tst-old-files-h2-integration.md` C3 for general $a$); $\int_{t_0}^\infty T^{-1}dT = \infty$; $\int_{t_0}^\infty T^{-2}dT = 1/t_0$

Under time-first sampling (observation time uniform over a window $\Delta$), the probability of finding the system alive at age in $[t_0, t_0 + dt_0]$ is $dt_0/\Delta$ for every $T \geq t_0$: the likelihood is flat in $T$, and the posterior is the prior on $(t_0, \infty)$ renormalized.

## C10 (check)
- target: segment:der-change-expectation-baseline
- at: 0bc90f7d
- act: read-check
- line: correspondence
- criterion: Does Caves (2000, arXiv:astro-ph/0001414) say what the Lineage paragraph attributes to it, and to Buch and Gott: the Bayesian form with Jeffreys' prior and the uniform-age likelihood put forward by Buch, endorsed by Gott; the uniform-age likelihood presupposing that the phenomenon is in progress; the posterior given present age being the prior conditioned on survival; Gott's rule then needing a prior density $1/T^2$?
- committed: after
- outcome: confirmed
- recheck: the arXiv PDF, text extracted: pages 3–4 ("Gott has endorsed [3, 4] a Bayesian analysis suggested by Buch [5]"), Eqs. (7), (12), (13), (19), (30) and $w_g(T) = 1/T^2$; references [3] Gott, Nature 368, 108 (1994) and [5] Buch, Nature 368, 107–108 (1994)

I read Caves only. The citations of Buch and of Gott's 1994 reply are as Caves gives them; I did not read either.

## C11 (check)
- target: segment:hyp-communication-gain
- read: segment:hyp-communication-gain, segment:der-adversarial-destabilization, segment:der-deliberation-cost, segment:hyp-auftragstaktik-principle
- at: 0bc90f7d
- act: read-check
- line: correspondence
- criterion: Do the three Appendix F parts the second check found without a fate (section F.4 hierarchical "Information asymmetry"; F.5 "Decision-Theoretic Integration" items 2 and 3 with "What TFT contributes to game theory"; F.6 $A_{ji}$) now each have one?
- committed: after
- outcome: confirmed
- recheck: Appendix F (`~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md`) lines 193, 212–225, 235 against the four segments read and `questions/when-a-team-must-change-model-class-together-wha.md`

F.4 information asymmetry: landed in #hyp-communication-gain's Discussion, the upward half as stated and the downward half assigned to $U_{\text{src},j}$, not $U_{\text{align},ji}$ (reason in the account). F.5 item 2: landed there as a reply's wait counted as deliberation cost. F.5 item 3: a vsect question, since its home is Part I. "What TFT contributes": carried by #der-adversarial-destabilization (tempo as the attacker's lever, the reserve as what it exhausts, mismatch as what it raises) and #hyp-communication-gain's Working Note on the trust meta-game. F.6 $A_{ji}$: replaced in round 2 by #detail-operationalization's statement that residuals cannot separate $U_{\text{src}}$ from $U_{\text{align}}$.
