---
kind: review
author:
  name: Claude Opus 5.5 (TST lane checker 2)
  role: independent adversarial checker
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-check-2.md
  - msc/inside-out-2026-10/c1-lanes/tst-check-2.py
  - msc/inside-out-2026-10/c1-lanes/tst-round-2.md
  - reviews/tst-lane-round-2-integration.md
written: 2026-10-30
---

# TST lane, round 2 (8002d40a..0bf4d6d2): a second independent check

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These checks re-run and re-derive from the text at `6511154d`; every target file is unchanged there from `0bf4d6d2`. Numbers, reasoning and suggested replacement text are in the write-up named first above, under the label at the end of each item. The robustness numbers are printed by the script named second, run from a directory holding the three `git log` dumps that `elapsed_time.py`'s header describes. This record's list of items is its content; silence on something does not mean it was checked.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Do the numbers both segments' measurement paragraphs cite reproduce when `elapsed_time.py` is re-run on the three direct-commit histories, dumped afresh at the HEADs in its header; do sections (1)–(4) print what the script at 0fe3432c printed; and does `run_analysis.sh` reproduce 0.118 from the saved data?
- committed: before
- outcome: confirmed
- recheck: `python3 elapsed_time.py tst.log obsidian-linter.log ink.log`; the same with `git show 0fe3432c:02-tst-core/empirical-discontinuity/elapsed_time.py`; `./run_analysis.sh` on a copy of the toolkit

Every cited number reproduces, sections (1)–(8). Sections (1)–(4) print identical numbers; twelve section-label lines differ, so "byte-identical output" holds for the numbers, not the bytes. `run_analysis.sh` exits 0, reproduces $\alpha = 0.118$ and writes its figure into a recreated `results/`. Write-up, "What holds".

## C2 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Does the window-free rejection of a pure exponential in obsidian-linter ($b$'s interval excluding zero inside the working component) survive resampling author-days instead of pairs, the dominant author alone, dropping squash-merge commits, a second idle component, and low-quantile regression on uncapped gaps?
- committed: before
- outcome: confirmed
- recheck: `tst-check-2.py`, blocks (A), (B), (C), (D) for obsidian-linter

Block bootstrap $b$ $[0.51, 1.27]$; dominant author $[0.41, 1.32]$; without squash-merge commits $[0.60, 1.34]$; two idle components $[0.20, 1.25]$; quantile regression $b$ 1.0–1.4 with $a \le 0$. Write-up M1.

## C3 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Does "the count form's cost grows as a power of $(1+d)$ below 1" (Discussion), with "exponent about 0.7" (Epistemic Status), hold when time away is modelled with two idle components instead of one?
- committed: before
- outcome: narrowed
- recheck: `tst-check-2.py` block (B) for obsidian-linter; block (D) for its dominant author

With two idle components the obsidian-linter exponent is 0.85 $[0.63, 1.00]$; the dominant author alone gives 0.83 $[0.73, 0.97]$. The exponential stays rejected; "below 1" depends on the idle model, which Limits says ("the exponent moves with it") and the conclusion and Epistemic Status do not. Suggested text in write-up M1.

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: read-check
- line: measurement
- criterion: Does the evidence support the Epistemic Status's "rises with the number of crossings in the commit, without compounding" (repeated in #impl-code-structure and toolkit README §3), given that a pure exponential is not distinguished in ink and the corpus and that obsidian-linter's interval on $a$ reaches about $+0.06$?
- committed: after
- outcome: narrowed
- recheck: section (6) and `tst-check-2.py` block (A) intervals on $a$; compare with the Discussion's "Nothing in them shows compounding"

The evidence supports "shows no compounding", which the Discussion and #der-principled-decision-integration use, not "without compounding". Write-up M2.

## C5 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Against section (7)'s own pure-exponential null, how often is obsidian-linter's observed $a$ (negative at every cap) reached, and does item 3's "weaker evidence than they look", judged on $b$ alone, still describe the capped test there?
- committed: before
- outcome: narrowed
- recheck: `tst-check-2.py` block (E), 300 null replicates with section (7)'s seed and model

In obsidian-linter the null reaches the observed $a$ in 0.3–2% of draws, and the observed $b$ in 0.7–3%. Against the integrator's own null, the capped fits reject a pure exponential there. In ink and the corpus they lean the same way and do not decide (1–13%). The fitted exponential null puts working time at $d = 20$ (median 688 min) above its own idle median (606 min). Item 3 understates the largest history; this is a strengthening. Suggested text in write-up M3.

## C6 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Are the three measured histories "direct (not squash-merged)", and do ink's cited numbers hold without the commits that carry a squash-merge subject?
- committed: after
- outcome: narrowed
- recheck: section header line (`261 with squash-merge subjects` for ink); `tst-check-2.py` block (D) "no squash-merge-subject commits" and block (F)

In ink, 261 of 664 non-merge commits, and 100 of 493 pairs, are squash merges. Without them ink's working medians are 5.8, 7.0, 12.5, 11.1, 6.2 (no rise across the top bins). Its exponent is 0.29 $[0.04, 0.60]$ and its capped Spearman 0.16–0.19. The changeset-size lines slope is 0.19 $[0.05, 0.34]$, so that conclusion stands. obsidian-linter is unaffected. Write-up M4.

## C7 (check)
- target: segment:hyp-exponential-cognitive-load
- at: 6511154d
- act: run
- line: measurement
- criterion: Does "the 316-commit TST research corpus (one author)", with i.i.d. pair-bootstrap intervals, describe what the corpus is and how independent its pairs are; and do "45 authors" and "156 authors" describe where the measured pairs come from?
- committed: after
- outcome: narrowed
- recheck: `git -C ~/src/_core/tst log a37e5eff --no-merges --format=%B | grep -ci 'co-authored-by: claude'` (149); file extensions changed; `tst-check-2.py` header lines and block (A)

The corpus is a mostly-Markdown theory repository: 149 of its 316 commits are co-authored by Claude, and its 277 pairs fall on twelve author-days. Its block-bootstrap exponent interval is $[0.17, 0.87]$ (cited $[0.32, 0.66]$). Measured pairs are 68% one author in obsidian-linter and 82% one person, under two emails, in ink. No conclusion changes; the descriptions and the corpus's intervals do. Write-up M5.

## C8 (check)
- target: segment:emp-changeset-size-principle
- at: 6511154d
- act: run
- line: measurement
- criterion: Does the working-time slope of $\log T$ on $\log(1+L)$ stay below 1 when the bootstrap resamples author-days, and in ink without squash-merge commits?
- committed: before
- outcome: confirmed
- recheck: `tst-check-2.py` block (F)

Lines: corpus 0.20 $[0.05, 0.47]$, obsidian-linter 0.38 $[0.31, 0.57]$, ink 0.31 $[0.18, 0.43]$, ink without squash merges 0.19 $[0.05, 0.34]$. Files: "reaches 1 in obsidian-linter and the corpus" also holds ($[0.67, 1.23]$, $[0.15, 1.46]$).

## C9 (check)
- target: segment:result-specification-bound
- at: 6511154d
- act: read-check
- line: correspondence
- criterion: In Putnam's own 1978 workshop text, is $E$ in the software equation life-cycle effort, does the minimum time come from the gradient constraint "cannot be exceeded", is $\lvert\nabla D\rvert$ related to concurrency, and do 1.81 years and 35.4 MY (with development effort $0.4K$) appear?
- committed: before
- outcome: confirmed
- recheck: NTRS 19820068869 PDF, abstract and pages 5–6

The abstract states $S_s = C_k K^{1/3} t_d^{4/3}$, solved with $K = \lvert\nabla D\rvert t_d^3$, where $\lvert\nabla D\rvert$ measures "the degree of concurrency of major task accomplishment". Page 5 reads "K is the life cycle effort in man years … (Dev Effort = .4K)", and the minimum time is 1.81 years and 35.4 MY with "the gradient condition … = 15 cannot be exceeded". $0.4 \cdot 15 \cdot 1.807^3 = 35.4$.

## C10 (check)
- target: segment:result-specification-bound
- at: 6511154d
- act: rederive
- line: derivation
- criterion: Does $t \ge \tau$ at every effort, with $t = (\text{LOC}/C)^{3/4}E^{-1/4}$, give $E \le (\text{LOC}/C)^3\tau^{-4}$; is "halving the schedule costs sixteen times the effort" right; and is the derived claim's extra condition (a transmission time effort does not shorten) stated where a reader meets the claim?
- committed: before
- outcome: confirmed
- recheck: raise $(\text{LOC}/C)^{3/4}E^{-1/4} \ge \tau$ to the fourth power; $2^4 = 16$; the tag and Epistemic Status

Condition is in the tag and in Epistemic Status. One reading note, no finding: where Putnam's gradient limit binds first, the region where the law fails is never reached. The Hypothesis paragraph carries that question. Write-up "Observations".

## C11 (check)
- target: segment:der-change-expectation-baseline
- at: 6511154d
- act: rederive
- line: derivation
- criterion: Does conditioning $\pi(T) \propto 1/T$ on survival alone fail to normalize, does the Copernican likelihood give $t_0/T^2$ with median remaining life $t_0$, and is the hazard route's "needs no Copernican likelihood" consistent with that?
- committed: before
- outcome: confirmed
- recheck: $\int_{t_0}^\infty T^{-1}dT = \infty$; $P(T \gt t_0+u\mid t_0) = t_0/(t_0+u)$; marginal $\int k e^{-kT}f(k)\,dk \sim f(0)/T^2$ for $0 \lt f(0) \lt \infty$

The hazard route's marginal lifetime prior has the same $T^{-2}$ tail as Jeffreys' prior times the Copernican likelihood, which is why the two routes agree. Attribution note, no finding: the Bayesian form is Buch's (1994), endorsed by Gott (Caves 2000, arXiv:astro-ph/0001414); Gott 1993 argued without a prior. Write-up "Observations".

## C12 (check)
- target: segment:scope-continuous-operation
- at: 6511154d
- act: rederive
- line: derivation
- criterion: With $\dot\delta = -\mathcal T\delta + \rho$ during recovery and arrivals only during uptime, are the repair time, its finiteness condition, $A = \mathcal T/(\mathcal T + c\lambda_f)$ with $c = \mathbb E[\ln^+(\delta_0/\delta_{\text{ok}})]$, and the target inequality right?
- committed: before
- outcome: confirmed
- recheck: $\delta(t) = \rho/\mathcal T + (\delta_0 - \rho/\mathcal T)e^{-\mathcal T t}$; $\text{MTTF}/(\text{MTTF}+\text{MTTR})$

## C13 (check)
- target: segment:der-team-persistence
- read: segment:der-team-persistence, segment:result-sector-condition-stability, segment:hyp-communication-gain
- at: 6511154d
- act: rederive
- line: discussion
- criterion: Given $R^\ast = \rho/\alpha$ as #result-sector-condition-stability states it at 6511154d, does the falsifier's bound $(\rho_{i,\text{env}} - \gamma^{\text{coop}}_{j\to i}\mathcal T_j)/\alpha_i$ follow, with every channel from $j$ held fixed, and is "mismatch below the bound refutes nothing" the right direction?
- committed: before
- outcome: confirmed
- recheck: #result-sector-condition-stability line 17 ("ultimately bounded by $R^\ast = \rho/\alpha$")

## C14 (check)
- target: segment:hyp-communication-gain
- at: 6511154d
- act: rederive
- line: derivation
- criterion: In the landed multi-agent update, where each source's gain is computed against the same prior $U_{M_i}$, does summing the terms agree with the joint Bayesian update when several terms arrive at once?
- committed: after
- outcome: narrowed
- recheck: $U_{M_i} = U_{o,i} = 1$ and one source of residual variance 1: summed gains $1/2 + 1/2 = 1$, joint gains $1/3 + 1/3$

Summed gains overshoot when terms coincide. Event by event, with $U_{M_i}$ updated between events, the update is consistent with #deriv-tempo-additivity, where independent streams almost never coincide. The segment does not say which reading it means, and falsifier (i) depends on it. Suggested clause in write-up N6.

## C15 (check)
- target: segment:der-team-persistence
- at: 6511154d
- act: read-check
- line: correspondence
- criterion: Does every part of Appendix F (`~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md`) now have a fate, carried in a named segment, asked as a vsect question, or set aside with a reason, as the round-2 fates table and its C13 say?
- committed: before
- outcome: narrowed
- recheck: Appendix F section by section against the six segments read and `questions/` (the four asked 2026-10-30); grep 01-aat-core/src for each remaining part

Everything the first check's H1 listed has a fate. Three parts do not. They are §F.4 hierarchical "Information asymmetry" (upward compression enters $U_{o,ji}$, downward translation enters $U_{\text{align},ji}$), §F.5 "Decision-Theoretic Integration" items 2–3 (consulting other agents as deliberation, coordinated structural switching) with "What TFT contributes to game theory", and §F.6 $A_{ji}$, which was replaced rather than carried, unrecorded. Write-up N7.

## C16 (check)
- target: segment:scope-developer-agent
- at: 6511154d
- act: run
- line: correspondence
- criterion: Do the three via-tft Source lines name the repository that holds `via-tft/`?
- committed: before
- outcome: confirmed
- recheck: `git -C ~/src/_ref/temporal-software-theory remote -v` (v2-io/tst; `via-tft/` present); `git -C ~/src/_core/tst remote -v` (v2-io/temporal-software-theory; no `via-tft/`)

## C17 (check)
- target: segment:def-causal-information-yield
- at: 6511154d
- act: read-check
- line: correspondence
- criterion: Does the rebuilt `CURRENT-VOL1.md` still carry the replaced "not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`)" sentence (first check's F3)?
- committed: before
- outcome: confirmed
- recheck: `grep -c old-tf-appendix-f CURRENT-VOL1.md` (0); line 1164 carries "The multi-agent consequences are in Part III …"

## C18 (check)
- target: segment:detail-operationalization
- read: segment:detail-operationalization
- at: 6511154d
- act: run
- line: correspondence
- criterion: Is the new `depends:` on #hyp-communication-gain and #der-team-persistence a forward reference in the outline, and are the touched segments md-press clean?
- committed: before
- outcome: confirmed
- recheck: `bin/lint-outline` (no ordering violations or missing dependencies in any component; the segment is in Appendix B); `md-press -q` on the eight touched segments, the account, the integrator's record and the new questions
