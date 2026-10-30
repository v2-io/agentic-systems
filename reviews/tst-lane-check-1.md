---
kind: review
author:
  name: Claude Opus 5.5 (TST lane checker 1)
  role: independent adversarial checker
sources:
  - msc/inside-out-2026-10/c1-lanes/tst-check.md
  - msc/inside-out-2026-10/c1-lanes/tst.md
written: 2026-10-30
---

# TST lane (df5a7c3b..bd889c03): an independent check

KRs **C.1** and **H.2** (`msc/inside-out-2026-10/INTENT.md`). These checks re-run and re-derive from the text at `f21dca70`; every file checked is byte-identical to `bd889c03`. Evidence, numbers and replacement text for each item are in the write-up named first above, under the label given at the end of each item. What I did not read is listed there. This record's list of items is its content; silence on an unread file means nothing.

## C1 (check)
- target: segment:hyp-exponential-cognitive-load
- at: f21dca70
- act: run
- line: measurement
- criterion: Does the Working Note's regression guard hold: does a time estimated from files and lines return $\alpha \approx 0.12$ against $d$ even with no per-file term, and does the saved estimate equal $10 + 5n + 0.15L$?
- committed: after
- outcome: confirmed
- recheck: `python3 reproduce_estimate_fit.py data/commits.json` in `02-tst-core/empirical-discontinuity/`

Max deviation $9\times10^{-13}$; $\operatorname{corr}(d,n) = 0.998$; V0 0.118 ($R^2$ 0.524, $N$ 205), V2 0.121, V3 0.073 with exponential $R^2$ below linear; fix rates 6.8% vs 11.4%. Write-up "What holds".

## C2 (check)
- target: segment:hyp-exponential-cognitive-load
- at: f21dca70
- act: run
- line: measurement
- criterion: Does every number in the Discussion's git-history measurement reproduce from `elapsed_time.py` on the six histories at the HEADs its header names?
- committed: after
- outcome: confirmed
- recheck: dump each history with the header's `git log` command, run `python3 elapsed_time.py <logs>`; separately fit $\log T$ on $\log(1+d)$ alone and $\log T$ on $d$ by OLS

All script-printed numbers match. "$\beta$ 0.4–0.7" (pure power slope, 0.39–0.69) and the "0.13" end of the forced-exponential range (log-OLS rate, 0.086–0.133) are correct but not printed by the script, so its recheck does not reproduce them.

## C3 (check)
- target: segment:hyp-exponential-cognitive-load
- at: f21dca70
- act: run
- line: measurement
- criterion: Are the "medians over gaps up to 24 hours" immune to the window, as the Discussion states ("which the cap cannot distort"), so that their flattening in the multi-author histories is a property of the data?
- committed: after
- outcome: broken
- recheck: per $d$ bin on uncapped gaps, the share above 1440 minutes, and the median with those gaps dropped vs counted as censored (code in the write-up's appendix)

The script drops gaps above the window, and the dropped share rises with $d$ (obsidian-linter 0.15 at $d=0$ to 0.26–0.35 at $d \ge 11$; ink 0.32–0.45). Censored medians: 12, 54, 77, 160, 260, 303 minutes. The flattening is the window's. A work/idle mixture on uncapped gaps restores a valid version of the reading for the multi-author histories (6.2, 11.9, 16.0, 33, 30 minutes) but not for the corpus. Replacement sentence in write-up B2.

## C4 (check)
- target: segment:hyp-exponential-cognitive-load
- at: f21dca70
- act: run
- line: measurement
- criterion: Do findings 2 and 3 ("$a$'s interval contains zero or lies below it everywhere"; "hold in all three, at every cap and with lines changed as a covariate"; "$\beta$ between 0.4 and 0.7, so sublinear") hold beyond the 60–480-minute caps chosen, and can dropping long gaps produce them from a true exponential?
- committed: after
- outcome: narrowed
- recheck: nested fit at caps 60, 480, 1440, 10080 and none; simulate a pure exponential with obsidian-linter's $d$ distribution and log-noise s.d. 2.0 through each cap

Uncapped, the corpus gives $a = +0.078$ [+0.001, +0.153]. Obsidian-linter's power slope reaches 0.85 [0.68, 1.01] and $b$ 1.0–1.2. In ink, with lines as a covariate, $b$'s interval reaches zero at every cap. Truncation attenuates a true $a$ by 30–60% but yields $b \le 0.14$. What survives every cap: $b$ far above what truncation makes, and obsidian-linter's negative $a$. "A pure exponential does not describe these data" stands; "sublinear" and "indistinguishable from zero" need scoping. Replacement text in write-up N1, which also lists the four restatements to align.

## C5 (check)
- target: segment:emp-changeset-size-principle
- at: f21dca70
- act: run
- line: measurement
- criterion: Does the log-log slope of elapsed time on lines changed stay below 1 when the window changes, as the paragraph's conclusion (proportionality cannot hold for implementation and comprehension together) needs?
- committed: after
- outcome: confirmed
- recheck: slope of $\log T$ on $\log(1+L)$ over all $d$ at caps 60, 480, 1440, 10080 and none, three direct-commit histories

0.14–0.26 (corpus), 0.24–0.48 (obsidian-linter), 0.22–0.40 (ink): far below 1 at every window, rising with the window. The transcribed numbers at 24 hours reproduce.

## C6 (check)
- target: segment:der-change-expectation-baseline
- at: f21dca70
- act: rederive
- line: derivation
- criterion: Do the hazard-mixture results re-derive (Watson's lemma tail $c\Gamma(a)t^{-a}$, median remaining $(2^{1/a}-1)t_0$, exact $t_0 + b$ for the exponential prior), and does an independent quadrature reproduce the six-prior table?
- committed: after
- outcome: confirmed
- recheck: substitute $u = kt$; quadrature of $S(t)$ and root-find the conditional median at ages $10$ to $10^4$

Every entry matches to three decimals. The Ord attribution is accurate: Ord derives the uniform case only.

## C7 (check)
- target: segment:der-change-expectation-baseline
- at: f21dca70
- act: read-check
- line: derivation
- criterion: Does the summary paraphrase ("any unknown constant termination hazard whose prior neither rules out arbitrarily low hazards nor gives them infinite weight") state the same condition as the derivation ($0 \lt f(0) \lt \infty$)?
- committed: after
- outcome: narrowed
- recheck: the Gamma $a = 2$ row of the segment's own table

A Gamma($a=2$) prior satisfies the paraphrase and gives multiplier $\sqrt2 - 1$. Replace with "whose prior density at zero hazard is finite and positive", in the opening paragraph and the subsection's last paragraph. Write-up N2.

## C8 (check)
- target: segment:result-specification-bound
- at: f21dca70
- act: rederive
- line: derivation
- criterion: Does $\text{LOC} = C E^{1/3} t^{4/3}$ imply that "time cannot fall below $(\text{LOC}/C)^{3/4}$ however much effort is added"?
- committed: after
- outcome: broken
- recheck: solve for $t$

$t = (\text{LOC}/C)^{3/4}E^{-1/4} \to 0$ as $E \to \infty$; the equation sets no floor. The error is T-02's, carried into the replacement, and the Hypothesis sentence reads the nonexistent floor as the specification bound. Replacement in write-up B1.

## C9 (check)
- target: segment:scope-continuous-operation
- at: f21dca70
- act: rederive
- line: derivation
- criterion: Does $A = \mathcal T_{\text{ops}}/(\mathcal T_{\text{ops}} + c\lambda_f)$ follow from the stated conditions (Poisson incidents, #hyp-mismatch-dynamics), and is availability governed by "the same ratio" as the persistence condition?
- committed: after
- outcome: narrowed
- recheck: #hyp-mismatch-dynamics transient solution with $\rho \gt 0$; alternating-renewal availability

The algebra holds, given three unnamed conditions: no background drift during recovery ($\delta_{\text{ok}} \gg \rho/\mathcal T$); incidents not arriving during repair; $c$ taken over $\ln^{+}$. Incident size enters logarithmically here and linearly in the persistence ratio, so "the same ratio" overstates. Write-up N3.

## C10 (check)
- target: segment:hyp-communication-gain
- at: f21dca70
- act: read-check
- line: correspondence
- criterion: Are the two new falsifiers faithful to Appendix F §F.7 #1 and #3, and stated in the segment's own notation?
- committed: after
- outcome: narrowed
- recheck: `~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md` §F.7 (or git `055f2803^`); grep live canon for a definition of $w_{ji}$

Content is faithful. $w_{ji}$ is Appendix F §F.1's, and is defined nowhere in live canon. Write-up N5.

## C11 (check)
- target: segment:der-team-persistence
- at: f21dca70
- act: read-check
- line: discussion
- criterion: Is the cooperative-decomposition falsifier faithful to §F.7 #2 and a sharp test of this segment's decomposition, and is the disagreement diagnostic faithful to §F.4?
- committed: after
- outcome: narrowed
- recheck: the segment's "Separation from communication tempo" paragraph and team persistence condition; Appendix F §F.4, §F.7

The diagnostic is faithful. The falsifier compares a mismatch change with a disturbance rate ("by that amount" should be $\gamma\mathcal T_j/\alpha_i$, and is a bound). It also does not hold communication fixed, which the segment's own separation paragraph requires. The Working Note still cites "F.4 in the source material", a deleted file. Write-up N4.

## C12 (check)
- target: segment:def-causal-information-yield
- at: f21dca70
- act: read-check
- line: discussion
- criterion: Do #der-team-persistence and #hyp-communication-gain carry what the replacement sentence says they carry (distributed tempo and team persistence; the trust meta-model and the boundary with game theory)?
- committed: after
- outcome: confirmed
- recheck: read both segments' Formal Expression and Discussion

## C13 (check)
- target: segment:scope-developer-agent
- at: f21dca70
- act: read-check
- line: correspondence
- criterion: Does the repointed Source line ("TST-via-TFT `via-tft/mapping.md` in the `temporal-software-theory` repository") resolve to the original? The same line was repointed in #der-code-quality-as-observation-infrastructure and #hyp-causal-discovery-from-git.
- committed: after
- outcome: broken
- recheck: `git -C ~/src/_core/tst ls-tree -r HEAD --name-only | grep via-tft` (none); `git -C ~/src/_ref/temporal-software-theory remote -v` (`v2-io/tst`); `git ls-remote` both

via-tft lives in `v2-io/tst` (commit `13b1024`), a separate repository from `v2-io/temporal-software-theory`, with no shared history. The word-diff confirms that content differs from the deleted copies only in formatting. Replace "the `temporal-software-theory` repository" with "the `v2-io/tst` repository" in all three segments. Write-up H2.

## F1 (finding)
- target: segment:der-team-persistence

The Appendix F deletion dropped content the account records as carried ("close enough to detail-operationalization"). #detail-operationalization has no source-reliability content. Gone:
- §F.1, the coupled update rule (where $w_{ji}$ is defined);
- §F.4, the ensemble topology, including its structural-adaptation trigger (all experts failing alike → expand the model class; some failing → re-route);
- §F.6, the practical control rules (quorum for high-stakes low-reliability updates, per-source calibration, separate logs for query and world actions, the ordering before structural adaptation);
- §F.8, the open questions on emergence and on consensus convergence.

This segment's Working Note still sends readers to the deleted file for F.4. The original survives in `~/src/_ref/temporal-feedback/` and git. Each part needs a fate: landed at honest tier, or set aside with a reason. Write-up H1.

## F2 (finding)
- target: segment:der-team-persistence

The account says simulation proposals 3–6 were registered as questions; three questions were opened, for Sims 3, 4 and 6. Sim 5 (multi-agent codebase evolution) tests this segment's cooperative-persistence claim and the coordination threshold's team-size breakeven, and has no fate. Write-up H3.

## F3 (finding)
- target: segment:def-causal-information-yield

`CURRENT-VOL1.md` (built before the lane) still carries this segment's replaced sentence, including its pointer to the deleted `src/old-tf-appendix-f-multi-agent.md`. It is a generated snapshot; the next `bin/build-monograph … --emit-current 01` clears it.
