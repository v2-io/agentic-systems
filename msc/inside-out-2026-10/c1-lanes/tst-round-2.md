*KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and KR H.2 ("every `old-*` file has a fate"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane, round 2: what the check changed, and what a verifier should look at

Written by the round-2 integrator (Claude Opus 5.5) for the independent verifier who comes next and for the lead. Input: the checker's write-up `c1-lanes/tst-check.md` and record `reviews/tst-lane-check-1.md`. The landing is commit 2cd1ad0c; my re-runs and re-derivations are typed in `reviews/tst-lane-round-2-integration.md` (C1–C14), taken into vsect. Everything the checker proposed was treated as an input to re-run or re-derive. Most of it held. The two places it did not are the most important part of this account.

## Where the check's proposals did not hold

**N1's replacement text.** It says "$b$ is 0.38–1.2 at every cap tried (60 minutes to none)". The checker's own table shows ink uncapped $b = 0.182$ and the corpus uncapped $b = 0.293$; my sweep agrees. Its argument that $b$ is "larger than truncating a pure exponential can produce (at most about 0.14)" rests on a simulation with one log-normal component (s.d. 2.0). Real gaps are a mixture of working time and time away, and the idle component matters. I fitted each history's mixture with a *pure exponential* working component, simulated it on the history's own $d$ values, applied the same caps, and refitted the nested OLS (`elapsed_time.py` section 7). The null gives $a$ near zero and $b$ up to about 1. In obsidian-linter the null's $a$ median is +0.005 to +0.018 while the true working rate is 0.243, and the null's $b$ reaches [0.44, 1.02] at 24 hours. The observed $b$ is reached in 0.7–6% of null draws. So the capped form test, the lane's main evidence, discriminates only weakly, and the segment now says that.

**B2's "flatten".** The checker's mixture medians reproduce exactly, but its replacement sentence says the medians "rise and then flatten in both multi-author histories". In obsidian-linter the 11–25 bin's interval is about 14–60 minutes, which does not distinguish flattening from a continued rise. The segment says the top bin is too uncertain.

## What replaced the windowed form test (strengthen-first)

The checker's per-bin mixture separates working time from time away but only yields medians. Putting the nested form $c + a\,d + b\log(1+d)$ inside the working component's mean gives a form test with no window at all (section 6). Result:

- **obsidian-linter** (1,264 pairs): $b = 0.98$ [0.51, 1.33], $a = -0.07$ [−0.17, +0.07]. The pure exponential is rejected. Working-time power exponent 0.72 [0.56, 0.87].
- **ink and the corpus:** not distinguished. Exponent 0.50 in both, $b$'s interval reaches zero, and the likelihood gap is 1.6.

The obsidian-linter likelihood gap (9.8) is not robust under bootstrap (95% [−3.3, 32.7]), so the segment rests the rejection on the nested coefficients. With a second idle component, the obsidian-linter exponent becomes 0.85 and the gap 4.1. This came from a scratch script and is not cited as a number; it is why the segment says "the exponent moves with it".

Net change in canon: "three findings hold in all three, at every cap" and "sublinear, $\beta$ 0.4–0.7" become a per-history statement. The pure exponential is rejected where the data discriminate and undistinguished elsewhere, and nothing shows compounding. The changeset-size conclusion survives window-free: the slope on lines is 0.20, 0.38 and 0.31, every interval below 1. Its overhead argument is recomputed from working-time medians (2.8× and 1.6× for about 13× the lines).

`elapsed_time.py` sections (5)–(8) print every number canon cites. Sections (1)–(4) are byte-identical in output to the script at 0fe3432c. The docstring's false censoring sentence is gone. README §2–3 is rewritten. `run_analysis.sh` no longer mines over `data/commits.json`. That file is a 229-commit snapshot that today's corpus cannot regenerate, so mining goes to `rerun/`; the script reproduces 0.118 from the saved data and recreates `results/`, which `analyze_outliers.py` writes its figure into and which the first lane had deleted.

## B1: Putnam

I read Putnam's own 1978 workshop paper ("Example of an early sizing, cost and schedule estimate…", NASA GSFC Third Summer Software Engineering Workshop, NTRS 19820068869; text extracted from the NTRS PDF). His minimum time comes from the difficulty-gradient constraint $K = \lvert\nabla D\rvert t_d^3$, which gives $t_{\min} = (\text{LOC}/(C\lvert\nabla D\rvert^{1/3}))^{3/7}$. His example re-derives: 1.81 years, 35.4 MY of development effort. (The commit body of 2cd1ad0c says 35.6, from rounding $t$ to 1.81 before cubing; 35.4 is right.) The $(\text{time}_{\text{specify}})^{3/4}$ conjecture had nothing under it and is deleted. In its place:

- *Derived, conditional on a sufficient transmission time that effort does not shorten:* any law of Putnam's form must fail beyond $E = (\text{LOC}/C)^3\tau^{-4}$.
- *Hypothesis:* observed compression limits are partly this bound. Its prediction is that at equal size, technology constant and staffing gradient, more distinguishing information or a slower channel lengthens the minimum schedule.

I did not read the 1978 IEEE TSE paper the segment cites for the equation.

## Found while integrating, not in the check

`#der-change-expectation-baseline`'s Jeffreys derivation read "After observing survival to age $t_0$ … $\pi(T \mid T \gt t_0) = t_0/T^2$". Conditioning the improper $1/T$ prior on survival alone does not normalize. The $t_0/T^2$ posterior is Gott's, and needs the Copernican likelihood $p(t_0 \mid T) = 1/T$. The likelihood is now named, and the hazard-mixture paragraph notes that its route needs survival alone. This also bears on N2's wording: the two routes rest on different assumptions, neither weaker.

## Appendix F (H1, N4, N5) and Sim 5 (H3): fates

| Part | Fate |
|---|---|
| §F.1 coupled update | Landed: `#hyp-communication-gain` Formulation. $w_{ji}$ and $\eta_{ji}$ enter only as a product, so a separate trust weight cannot be identified; fixed trust is a constant $\eta_{ji}$, and falsifier (i) now says so. |
| §F.4 peer network | Carried (disagreement diagnostic, `#der-team-persistence`); $w_{ij}$ now defined there. |
| §F.4 ensemble | Landed: `#der-team-persistence` Discussion (correlated residuals = shared limitation → model class; weight by calibration = $U_{\text{src}}$). |
| §F.4 "query the most uncertain expert" | Set aside. As written it sends queries to the least-informed expert; whether that maximizes information yield depends on whose uncertainty the query resolves, which the source does not say. |
| §F.4 hierarchical | Carried: `#der-temporal-nesting`, `#hyp-auftragstaktik-principle` (verified). |
| §F.2 $U_{\text{align}}^{\text{eff}} = U_{\text{align}}^{\text{Bayes}}/Q_p$ | Set aside. One arbitrary form of the conservative-quantile idea that `#hyp-communication-gain` carries; calibrating $p$ is asked below. |
| §F.6 per-source quantities | Landed: `#detail-operationalization` "Multi-Agent Quantities". Residual estimator floored at zero; residuals cannot separate $U_{\text{src}}$ from $U_{\text{align}}$, said there. |
| §F.6 quorum, logging, remedies-before-structure | Landed: same segment. The quorum is tied to the common-source regime, and the remedy ordering sits under its Structural-Switch Trigger. |
| §F.5 game theory; §F.8 Q3 | vsect question `in-aat-s-terms-tempo-reserve-mismatch-communicat`. |
| §F.8 Q1, Q2, Q5 | vsect question `under-what-conditions-does-the-multi-agent-updat`. |
| §F.8 Q4 (a), (b) | vsect question `how-should-the-null-distribution-p-0-of-hyp-comm`; (c) is carried by `#deriv-tempo-additivity`. |
| Sim 5 | vsect question `in-a-simulated-codebase-worked-by-several-agents`, which asks that action and communication be varied separately (N4's point). |

N4's falsifier is now a bound, with every channel from $j$ to $i$ held fixed. That includes $i$ observing $j$'s actions, which the landed §F.1 text counts as communication; the checker's suggested "sends $i$ nothing" would not have excluded it. The original §F.7 #2 itself said "adding cooperative communication channels", which conflates the two terms the live segment separates.

## Other items

- N3 re-derived, including the $\rho \gt 0$ repair time; the "same ratio" sentence is replaced by the linear-versus-logarithmic comparison.
- H2: `git remote` confirms via-tft is in `v2-io/tst`; three Source lines repointed. The first lane's account (`tst.md`) also names wrong locations for the Lindy original and the 2025 syntheses (checker H2). That file is another lane's account, so I leave it; the correct locations are in the checker's H2.
- `at:` revisions off main: the eight lane review items that cite worktree hashes are annotated (`vsect annotate`) with their main equivalents.
- The lane's open question `does-per-commit-cost-grow-with-the-dependency-st` said the count cost "grows sublinearly"; it now says "shows no compounding".
- `vsect revise` classified seven records as redefined. Among them is `#def-causal-information-yield`: the first lane edited it (055f2803) and never took the edit in. `#result-mismatch-decomposition` also has an untaken edit, from a Part I lane; I left it to that lane.
- Not done: `CURRENT-VOL1.md` still carries the old CIY sentence (checker F3). It is a generated snapshot, and rebuilding it in a parallel worktree would conflict with every other lane's merge, so it belongs to whoever rebuilds after merging.
- The line of `#scope-evolving-software` reserved for the Part I integrator is untouched.

## Open findings this landing answers, for the verifier to close

vsect lets only someone other than the reviser mark a finding answered (`vsect findings --answered <item> --by-revision 2cd1ad0c --why …`). These are the ones 2cd1ad0c is meant to answer:

- `review:tst-lane-check-1#C3/finding` (B2), `#C4/finding` (N1), `#C7/finding` (N2), `#C8/finding` (B1), `#C9/finding` (N3), `#C10/finding` (N5), `#C11/finding` (N4), `#C13/finding` (H2), `#F1` (H1), `#F2` (H3).
- From the first lane: `review:tst-old-files-h2-integration#C2/finding` (the CIY sentence), answered by 055f2803 and confirmed by the checker's C12.
- `#F3` (`CURRENT-VOL1.md`) stays open until a rebuild.

My checks read 2cd1ad0c. The commit after this account's first version changed three segments:

- `#emp-changeset-size-principle`: "rising as the cap is raised" was false for ink, which falls to 0.24 uncapped. Narrowed, classified redefined.
- `#der-change-expectation-baseline`: Epistemic Status names the Copernican premise; "Jeffrey's" becomes "Jeffreys'". Classified reworded.
- `#hyp-communication-gain`: Epistemic Status names the Formulation. Classified reworded.

So C4, C8, C9 and C12 of my record rest on text that has since changed, and `vsect confirm` on those three records is a second mind's to make.

## What I would check, if I were the verifier

1. **The mixture.** Is a two-component log-normal on $\log T$, with the working share free per bin, a fair separation of working time from time away? Is the window-free form test sound, and does the obsidian-linter rejection survive a model you would choose instead?
2. **The null in section 7.** Is a pure exponential plus the fitted idle component the right null for the capped test?
3. **The new derived claim** in `#result-specification-bound`, and whether its condition (transmission time not shortened by effort) is stated where a reader will see it.
4. **The Copernican correction** in `#der-change-expectation-baseline`, against Gott 1993.
5. **Appendix F** against the fates table, especially the two set-asides.
