*KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and KR H.2 ("every `old-*` file has a fate"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane: an independent check of what landed, ran and was deleted

Written by an independent checker (Claude Opus 5.5) for the lead coordinator and for the integrator who lands the corrections. The typed record is `reviews/tst-lane-check-1.md`; this file carries the evidence, the numbers and the replacement text. The lane's commits on main are `df5a7c3b` through `bd889c03`. Every file checked is byte-identical between `bd889c03` and `f21dca70`, so the record's checks read `f21dca70`. The lane's account and review records cite worktree hashes; on main, `fc204813` is `df5a7c3b`, `60162347` is `c374794a`, `2d204811` is `8d3c0026` and `de218fb0` is `055f2803`.

What I read and ran: both new scripts, re-run against all six histories at the HEADs the script names; every touched live segment's diff, and the full text of `#hyp-exponential-cognitive-load`, `#scope-continuous-operation`, `#der-team-persistence` and the relevant parts of `#hyp-communication-gain`; Appendix F in full; the originals of T-02, T-06, T-12, T-13, both Lindy files, FP-001 and FP-005 of the v0.1 principles, the reformulated sketch (S-08, S-09, S-14, Parts V and the open questions) and the simulation proposals (Sims 1, 5, 6 and the priority list). I word-diffed all five via-tft files and Appendix F against their external originals. I did not read the other old files whole. In particular I did not check the 2025 syntheses, the 960-analysis synthesis, `general-discussion`, `ai-specification-limit`, `causal-extensions` or `mapping` against their carriers beyond the word-diff. Treat this list of findings as the content; absence of a finding on an unread file means nothing.

## What holds

- **The circularity finding.** `reproduce_estimate_fit.py data/commits.json` gives $\max\lvert\text{saved} - (10 + 5n + 0.15L)\rvert = 9\times10^{-13}$, $\operatorname{corr}(d, n) = 0.998$, V0 $\alpha = 0.118$ ($R^2 = 0.524$, $N = 205$), V2 $0.121$, V3 $0.073$ (exponential $R^2$ 0.842 below linear 0.877), and the fix-message rates 6.8% ($d \gt 10$, $n = 44$) against 11.4%. The dataset's commits exist in `~/src/_core/tst`. The 0.118 never measured time.
- **Every number transcribed from `elapsed_time.py`.** Spearman, partials, nested-form coefficients and intervals, the binned medians, and the changeset-size slopes and medians all reproduce at seed 0. The two numbers that do not come from the script are "$\beta$ between 0.4 and 0.7" and the upper end "0.13" of the forced-exponential range. They are, respectively, the slope of $\log T$ on $\log(1+d)$ alone (0.39–0.69 across histories and caps) and the log-OLS exponential rate (0.086–0.133). Both are correct but not reproducible from the shipped script.
- **The hazard-mixture derivation** in `#der-change-expectation-baseline`. Watson's lemma, the limit $(2^{1/a}-1)t_0$, and the exact $b/(b+t)$ for the exponential prior all re-derive. An independent quadrature reproduces the six-prior table to three decimals at every age. The Ord attribution is honest. Ord (arXiv:2308.09045, pp. 6–7) derives only the uniform-prior case and remarks that a density reaching zero at $k = 0$ "in some cases" does not matter; the $a$-dependence is not in Ord. It is a standard Abelian result for Laplace transforms, which "stated here" does not overclaim.
- **The Appendix F falsifiers** are faithful to §F.7 #1–#3 in content. The disagreement diagnostic is faithful to §F.4.
- **"Formatting differences only."** The word-diffs of the five via-tft files against `v2-io/tst` and of Appendix F against `temporal-feedback` show only Unicode becoming LaTeX ($\Omega$, $U_o$, $\eta^\ast$).
- **The A13 carrier sweep.** No live segment cites 0.118 or the estimated-time fit as evidence. `bin/lint-outline` and `md-press -q` are clean on every touched file.
- **T-06 → `#der-change-investment`.** I spot-read for coverage: the near-zero-cost insight, optionality, aggregation across scopes and the compounding bifurcation are carried. **T-12 → reading locality**: carried, with familiarity and documentation. **FP-001's probabilistic form**: faithful.

## Broken

### B1. `#result-specification-bound`: the new paragraph states a floor the equation does not have

The landed text reads: "Rearranged, time cannot fall below $(\text{LOC}/C)^{3/4}$ however much effort is added." From $\text{LOC} = C E^{1/3} t^{4/3}$, $t = (\text{LOC}/C)^{3/4} E^{-1/4}$, which goes to zero as $E \to \infty$. The quantity $(\text{LOC}/C)^{3/4}$ is the time at $E = 1$, not a limit. The error is T-02's own ("Even with infinite effort ($E \to \infty$), time cannot go below…"). The integrator's C1 corrected the attribution and then imported the algebra, as "the floor $(\text{LOC}/C)^{3/4}$ is his". The Hypothesis sentence that follows reads that nonexistent floor as the specification bound.

Wikipedia's Putnam-model page states the software equation and that effort falls as time is extended. It gives no minimum time from the equation. My understanding is that Putnam obtains a minimum development time from a separate limit on staffing build-up. I have not verified that against the 1978 text, so the replacement below hedges it.

*Replacement for the paragraph's middle sentences:* "Solved for time, $t = (\text{LOC}/C)^{3/4} E^{-1/4}$: at fixed size and technology constant, time falls only as the fourth root of effort, so quartering the schedule costs $4^4 = 256$ times the effort. The equation alone sets no floor; a minimum development time in Putnam's framework needs a further constraint on how fast staff can be added. *[Hypothesis.]* Reading the effort-independent factor $(\text{LOC}/C)^{3/4}$ as the specification bound seen through a power law, $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$, is a conjecture of this theory, not Putnam's finding…" The rest of the paragraph can stay. The integrator should decide whether the conjecture survives the loss of a floor. It now has to say why the effort-insensitive factor, rather than a minimum, is what specification bounds. One candidate is the diminishing return: under $E^{-1/4}$, specification becomes the binding cost long before effort runs out.

### B2. `#hyp-exponential-cognitive-load`: "medians over gaps up to 24 hours, which the cap cannot distort"

The script drops gaps over the window rather than censoring them, so the medians are of a truncated sample. The share dropped also rises with $d$. Over 24 hours it is 0.15, 0.23, 0.24, 0.27, 0.26 and 0.35 in obsidian-linter for $d$ = 0, 1–2, 3–5, 6–10, 11–25 and 26–60, and 0.32 to 0.45 in ink. Counting the dropped gaps as censored gives obsidian-linter medians of 12, 54, 77, 160, 260 and 303 minutes; ink's are non-monotone (27, 101, 132, 59, 528, 647). Under either treatment, the "flatten" (71 then 70 minutes) belongs to the window. `elapsed_time.py`'s docstring says the same thing ("which a session cap cannot distort while under half of a bin is censored"). That holds for censoring, not for what the code does. The account repeats it ("Censoring checked").

Neither truncation nor censoring isolates working time: uncapped gaps include days away. A form-neutral alternative is to fit, per $d$ bin, a two-component Gaussian mixture on uncapped $\log T$. The work component has a per-bin mean and shared spread; the idle component has a shared mean and spread. Medians of the work component, with 100-draw bootstrap intervals:

| history | $d=0$ | 1–2 | 3–5 | 6–10 | 11–25 | idle median |
|---|---|---|---|---|---|---|
| obsidian-linter | 6.2 [5.0, 7.6] | 11.9 [8.6, 17.1] | 16.0 [13.4, 19.7] | 33.1 [24.3, 45.9] | 29.7 [0.8, 65.2] | 1585 min |
| ink | 5.4 [4.2, 7.1] | 8.3 [3.4, 22.3] | 15.0 [9.5, 26.9] | 15.0 [8.2, 27.5] | 15.5 [5.8, 38.6] | 10328 min |
| TST corpus | 3.1 [2.5, 3.8] | 5.4 [3.9, 8.0] | 5.6 [4.7, 7.1] | 8.5 [5.6, 13.0] | 16.4 [8.5, 26.9] | 95 min |

These rise and then flatten in the two multi-author histories without any window, which supports the segment's qualitative reading by a valid route. In the corpus they keep rising: from $d = 3$–5 to 11–25 the work median triples over about 14 crossings. That is a per-crossing rate near 0.08 and does not discriminate the forms. The mixture is a modelling choice, so it is heuristic tier like the rest.

*Replacement for the medians sentence of finding 3:* "Gap medians do not settle the form: any window that drops long gaps drops more of them at high $d$ (24 hours drops 15% at $d = 0$ and 26–35% at $d \ge 11$ in obsidian-linter). Separating a working component from idle time with a two-component mixture on uncapped gaps gives working-time medians that rise and then flatten in both multi-author histories (obsidian-linter 6.2, 11.9, 16.0, 33 and 30 minutes for $d$ = 0, 1–2, 3–5, 6–10 and 11–25; ink 5.4, 8.3, 15, 15 and 15.5). In the single-author corpus they keep rising (3.1 to 16.4), and over that range the corpus cannot separate the forms." The script needs the mixture added (Appendix below) so the recheck reproduces.

## Narrowed

### N1. The form test is scoped to the caps chosen

I swept the cap, with 1000-draw bootstraps, at $d \le 25$. The script's bootstrap uses 2000 draws, so the intervals at caps 60 and 480 differ in the third decimal from the account's.

| history | cap | $a$ [95%] | $b$ [95%] | power slope [95%] | lines slope, all $d$ |
|---|---|---|---|---|---|
| corpus | 60 | +0.028 [−0.016, +0.068] | +0.376 [+0.144, +0.629] | 0.51 | 0.14 |
| corpus | 1440 | +0.042 [−0.017, +0.104] | +0.392 [+0.067, +0.726] | 0.60 | 0.18 |
| corpus | none | **+0.078 [+0.001, +0.153]** | +0.293 [−0.049, +0.667] | 0.68 [0.50, 0.89] | 0.26 |
| obsidian-linter | 60 | −0.063 [−0.128, +0.007] | +0.721 | 0.48 | 0.24 |
| obsidian-linter | 1440 | −0.063 [−0.140, +0.007] | +1.006 [+0.708, +1.332] | 0.75 | 0.41 |
| obsidian-linter | none | −0.082 [−0.164, −0.003] | +1.190 | **0.85 [0.68, 1.01]** | 0.48 |
| ink | 480 | −0.026 [−0.150, +0.070] | +0.549 | 0.44 | 0.29 |
| ink | none | +0.050 [−0.141, +0.210] | +0.182 [−0.592, +1.044] | 0.39 | 0.24 |

I also simulated a true pure exponential through the same truncation. I drew $d$ from obsidian-linter's empirical distribution, used log-noise s.d. 2.0 (the empirical residual), $T_0$ of 8.5 or 20 minutes, and 200 replicates of 4000. At $\alpha = 0.118$, dropping gaps above the cap gives a fitted $a$ of 0.036–0.045 at a 60-minute cap and 0.064–0.079 at 480 minutes (true $0.112$), with $b$ only 0.04–0.06. At $\alpha = 0.2$, $b$ stays at or below 0.14.

What follows:

- The segment's "contains zero or lies below it everywhere" and "three findings hold in all three, at every cap and with lines changed as a covariate" are true only for caps of 60–480 minutes. In ink, $b$'s interval reaches zero at every cap once lines is a covariate. In the corpus, with no cap, the exponential coefficient is positive with an interval excluding zero.
- Truncation attenuates $a$ by 30–70%, so the capped intervals on $a$ do not bound the true exponential rate. In the corpus, the 60-minute upper bound of 0.068 is compatible with a true rate above 0.1.
- What survives every cap, and what truncation cannot manufacture, is the size of $b$ (0.38–1.2, against at most 0.14 from a truncated pure exponential) and obsidian-linter's negative $a$. So "a pure exponential in the count does not describe these data" stands, and that sentence is the one to keep. "Sublinear" does not stand unqualified: obsidian-linter's power slope rises to 0.85 [0.68, 1.01] without a cap, and $b$ reaches 1.0–1.2.
- The changeset-size slope on lines stays far below 1 at every cap (0.14–0.48), so `#emp-changeset-size-principle`'s conclusion is robust. It also rises with the cap, which is worth one clause there.

*Replacement for finding 2 and the first sentence of finding 3:* "2. A pure exponential in the count does not describe these data. In $\log T = c + a\,d + b\log(1+d)$ the exponential form predicts $a \gt 0$ with $b \approx 0$. Instead $b$ is 0.38–1.2 at every cap tried (60 minutes to none), larger than truncating a pure exponential can produce (at most about 0.14 in simulation at these caps). The coefficient $a$ is negative in obsidian-linter at every cap. Within caps of 60–480 minutes, its interval contains zero or lies below it in all three histories. Dropping long gaps attenuates a fitted $a$ by 30–70% in simulation, though, and in the single-author corpus without a cap $a = +0.078$ [+0.001, +0.153]. A smaller exponential component alongside the power term is not excluded there. 3. Read as a power law, $T \propto (1+d)^{\beta}$ with $\beta$ 0.4–0.7 within session caps, rising to 0.85 [0.68, 1.01] in obsidian-linter without one: sublinear, or at most about proportional." The Epistemic Status sentence "roughly as $(1+d)^{0.4}$ to $(1+d)^{0.7}$, and an exponential term in $d$ is indistinguishable from zero or negative once a power term is allowed" needs the same scoping. The same goes for the restatements in `#impl-code-structure`, `#der-principled-decision-integration` ("sublinearly in counted crossings"), `02-tst-core/OUTLINE.md` and the toolkit README §2.

### N2. `#der-change-expectation-baseline`: the summary paraphrase is broader than the theorem

The body's condition is exact: $a = 1$, i.e. $0 \lt f(0) \lt \infty$. The opening paragraph and the closing sentence of the new subsection paraphrase it as "any unknown constant termination hazard whose prior neither rules out arbitrarily low hazards nor gives them infinite weight". A Gamma($a = 2$) prior rules out no low hazard and gives none infinite weight, yet the integrator's own table shows its multiplier is $\sqrt2 - 1 = 0.414$. *Replacement in both places:* "…whose prior density at zero hazard is finite and positive". `#impl-foundations-features` already says this. Separately, "a weaker ignorance assumption than Jeffreys'" is better put as "a different, more checkable" one. A prior over the hazard and a scale-invariant prior over the lifetime are not ordered by strength.

### N3. `#scope-continuous-operation`: the availability formulation's conditions

The algebra is right: $\text{MTTR} = c/\mathcal T_{\text{ops}}$, $A = \mathcal T_{\text{ops}}/(\mathcal T_{\text{ops}} + c\lambda_f)$, and the target inequality. Three conditions are used but not named.

- Recovery is pure decay, with no background drift. Under `#hyp-mismatch-dynamics` with $\rho \gt 0$, mismatch decays toward $\rho/\mathcal T$, not zero. Recovery takes $\ln\big((\delta_0 - \rho/\mathcal T)/(\delta_{\text{ok}} - \rho/\mathcal T)\big)/\mathcal T$ and needs $\delta_{\text{ok}} \gt \rho/\mathcal T$.
- Incidents do not overlap: the clock for the next incident runs only during uptime. That is the alternating-renewal form $\text{MTTF}/(\text{MTTF}+\text{MTTR})$; "Poisson" alone allows arrivals during repair.
- $c = \mathbb E[\ln^{+}(\delta_0/\delta_{\text{ok}})]$, since incidents smaller than the tolerance cost nothing.

"Availability depends on the same ratio of correction tempo to disturbance rate as the persistence condition" is loose. With impulses of size $\delta_0$ at rate $\lambda_f$, the persistence ratio is linear in incident size ($\rho \approx \lambda_f\mathbb E[\delta_0]$) where availability is logarithmic. *Suggested:* "…depends on the ratio of correction tempo to incident rate, as the persistence condition does, though incident size enters logarithmically here and linearly there".

### N4. `#der-team-persistence`: the new falsifier

- "Steady-state mismatch does not fall by that amount": "that amount" is $\gamma^{\text{coop}}_{j\to i}\mathcal T_j$, a disturbance rate. The predicted change in the steady-state bound is $\gamma^{\text{coop}}_{j\to i}\mathcal T_j/\alpha_i$, and under the sector framework that is a bound, not a point prediction.
- More substantively, the segment's own "Separation from communication tempo" paragraph insists that an ally acts through communication or through action and that counting both double-counts. Yet the falsifier's test, "adding a reliable ally", adds both channels unless communication is held fixed. As written, a team that improves through communication alone would pass.

*Suggested:* "…in a controlled setting where the ally acts in the shared environment but sends $i$ nothing (communication tempo held fixed), with $\gamma^{\text{coop}}$ and $\mathcal T_j$ measured, the decomposition is refuted if $i$'s ultimate mismatch exceeds $(\rho_{i,\text{env}} - \gamma^{\text{coop}}_{j\to i}\mathcal T_j)/\alpha_i$ by more than measurement error."

The Working Note "The topology-dependent analysis (F.4 in the source material …) … not covered here" now points at a deleted file. It also undersells the segment, which now carries the peer-network diagnostic.

### N5. `#hyp-communication-gain`: $w_{ji}$ is undefined

The falsifier compares the gain with "any fixed trust weight $w_{ji}$". That symbol was defined in Appendix F §F.1's coupled update, $M_i^+ = M_i^- + \eta\,g(\delta) + \sum_j w_{ji}\eta_{ji}h_{ji}(M_j, M_i)$. The update was not carried and is defined nowhere in live canon. `#der-team-persistence`'s $V_{\text{disagree}}$ uses $w_{ij}$ the same way. Either carry the coupled update, or say "a fixed weight on $j$'s signal in place of $\eta_{ji}^\ast$". The content of falsifiers (i) and (ii) is faithful to §F.7.

## Fates that do not hold

### H1. Appendix F content not carried and now absent from the repository

The account says the ensemble and operational rules "are close enough to detail-operationalization that they were not landed". `#detail-operationalization` has no source-reliability content: no per-source calibration, no Brier or log-loss scoring, no quorum, no aggregator. Gone with the file:

- §F.1, the coupled update rule (the definition of $w_{ji}$, N5).
- §F.4, the ensemble topology:
  - aggregators weight experts by calibration, not confidence;
  - queries go to the most uncertain expert (CIY at the aggregation level);
  - the structural-adaptation trigger: if all experts fail alike (correlated residuals), expand the model class; if only some fail, re-route.
- §F.6, the practical control rules:
  - quorum before high-stakes updates from low-reliability sources;
  - auto-adjusting $w_{ji}$ from verified accuracy;
  - logging query actions separately from world actions;
  - the ordering of trust recalibration, routing and channel upgrade before structural adaptation.
- §F.8, the open questions on emergence and on consensus convergence for structured models.

The hierarchical topology (micromanagement as command-induced oscillation) is carried by `#der-temporal-nesting` and `#hyp-auftragstaktik-principle`. The original survives at `~/src/_ref/temporal-feedback/Appendix-F-Multi-Agent.md` and in git, so nothing is lost permanently. But H.2's "fate" for these parts is "dropped" while the account records "carried", and `#der-team-persistence`'s Working Note still points readers to the deleted file for them. The ensemble structural-adaptation trigger and the quorum rule look like Part III or `#detail-operationalization` content at discussion grade.

### H2. The via-tft provenance names the wrong repository

Three repointed Source lines (`#der-code-quality-as-observation-infrastructure`, `#hyp-causal-discovery-from-git`, `#scope-developer-agent`) cite "TST-via-TFT `via-tft/…` in the `temporal-software-theory` repository". The account says the same for all originals. The via-tft files are in `v2-io/tst`: commit `13b1024`, 2 commits, cloned locally as `~/src/_ref/temporal-software-theory`. `v2-io/temporal-software-theory` (`~/src/_core/tst`, 316 commits) has no `via-tft/` and shares no history with it; `git ls-remote` confirms they are distinct repositories. The local directory name is what misleads. *Replacement:* "…`via-tft/mapping.md` in the `v2-io/tst` repository…". The account's other location claims also need correcting, though they are not in canon: the Lindy original is `vault/04-workspace/1-inbox/lindy-mathematical-foundations.md`, and the 2025 syntheses are under `archive/` and `planning/`, not `vault/02-theory/`.

### H3. Simulations 3–6 "registered as questions"

Three questions were opened, for Sims 3, 4 and 6. Sim 5, multi-agent codebase evolution, has no question. It tests the very cooperative-persistence claim N4 concerns, plus the team-size breakeven of the coordination threshold. Either a question or a line in `#der-team-persistence`'s Working Notes would give it a fate.

## Hygiene

- **`at:` revisions off main.** Both lane review records bind checks to worktree commits that no branch contains. `git branch --contains` for each is empty; only the reflog holds them. vsect resolves the versions today, because the segment texts are identical to main's and the versions are content hashes. But the account's recheck commands (`git show de218fb0^:…`, `git show 2d204811^:…`) and the records' `at:` lines will stop resolving when the reflog expires. Main equivalents are at the top of this file.
- **`CURRENT-VOL1.md`** (built 13:33, before the lane) still carries the replaced "not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`)" sentence. It is a generated snapshot, for the next rebuild, not a hand edit.
- **All of the lane's own checks have now lapsed.** `vsect check --strict` lists A13 C2/C3 and H.2 C3–C6 as stale, mostly through upstream changes from other lanes (`#scope-adaptive-system`, `#def-agent-environment`, `#scope-agency`). Nothing the lane checked currently "holds" in vsect, so the confirmations above are the live evidence. A13 C3 and H.2 C6 are grep checks bound to `#obs-software-epistemic-properties`'s whole `depends:` chain. They would benefit from `- read:` declarations, which vsect now supports.
- **`run_analysis.sh`** mines `--repo ..`, which is ASF's `02-tst-core/`, not `~/src/_core/tst`. It writes over `data/commits.json` before step 3 reproduces the fit. Run as shipped, it will not reproduce 0.118. Point it at the corpus or have it write to a separate directory.

## Appendix: the scripts behind B2 and N1

Run from any directory with `elapsed_time.py`'s directory on `sys.path`. The logs are made with the `git log` command in its header.

```python
# censored vs truncated medians (B2)
d, g, _ = E.gaps(cs, 1e18, 10**9)
for lo, hi in [(0,0),(1,2),(3,5),(6,10),(11,25),(26,60)]:
    x = g[(d>=lo)&(d<=hi)]
    print(np.mean(x>1440), np.median(x[x<=1440]), np.median(np.where(x<=1440, x, np.inf)))

# work/idle mixture on uncapped log gaps (B2): per-bin work mean, shared work sd, shared idle mean/sd, per-bin weight
def em(y, b, K, iters=500):
    mu_w = np.array([np.median(y[b==k]) - 1 for k in range(K)]); s_w = 1.0
    mu_i, s_i = np.percentile(y, 85), 1.0; pi = np.full(K, 0.7)
    for _ in range(iters):
        pw = pi[b]*norm.pdf(y, mu_w[b], s_w); pid = (1-pi[b])*norm.pdf(y, mu_i, s_i); r = pw/(pw+pid)
        for k in range(K):
            m = b==k; mu_w[k] = np.sum(r[m]*y[m])/np.sum(r[m]); pi[k] = r[m].mean()
        s_w = np.sqrt(np.sum(r*(y-mu_w[b])**2)/r.sum())
        mu_i = np.sum((1-r)*y)/np.sum(1-r); s_i = np.sqrt(np.sum((1-r)*(y-mu_i)**2)/np.sum(1-r))
    return mu_w, s_w, mu_i, s_i, pi   # bins (0,0),(1,2),(3,5),(6,10),(11,25) on gaps(cs, 1e18, 25); 100 bootstrap refits, seed 0

# truncation simulation (N1): true pure exponential through a cap, nested fit
d = rng.choice(d_emp, 4000); T = T0*(1+alpha)**d*np.exp(rng.normal(0, 1.99, 4000)); m = T <= cap
coef = lstsq(column_stack([ones, d[m], log1p(d[m])]), log(T[m]))   # 200 replicates, seed 1
```
