*KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and KR H.2 ("every `old-*` file has a fate"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." — Joseph, 2026-10-30.*

# TST lane, round 4 (merge `a1fa9024`, lane `bbd5f3c9..b87f6680`): an independent check

Written by the fourth TST checker (Claude Opus 5.5) for the lead and for whoever integrates next. The typed record is `reviews/tst-lane-check-4.md`, where F1, F2 and F3 are the findings opened by checks C2, C6 and C4, F4's second half is C9's, and F4, F5, F7 and F8 are typed findings; the numbers the toolkit does not print come from `tst-check-4.py` beside this file. The lane's target files are identical at the landing `0201c156`, the merge and HEAD `e9578b96`. I read the round-4 account and the integrator's record first, then re-derived and re-ran from the segment texts, the toolkit, the repositories and Caves's paper. This report's content is its list of findings and checks; where it is silent, nothing was checked.

**Verdict.** What round 4 set out to fix is fixed, and the check-3 findings it answers (C4, C5, C6, C8, C9) are answered. The scale-ignorance derivation, its "whose lifetime" subsection, the Caves correspondence, the source-bias saturation, the toolkit's new lines and the README's squash-merge evidence all hold. Five things are not right yet. The most consequential is F1: the restructure dropped the observation premise that the hazard-mixture route needs, and under the main derivation's own likelihood that route gives about $0.41\,t_0$, not $t_0$. F2 is the next: section (7)'s new test is decided by Monte Carlo noise at 1,000 replicates, and at 10,000 it rejects a pure exponential in obsidian-linter.

## Findings

### F1. The hazard-mixture route gives the baseline only when survival is the whole observation (`#der-change-expectation-baseline`, and `#impl-foundations-features`)

Round 3's text conditioned the hazard mixture on survival because its observation premise said so. Round 4 replaced that premise with the uniform-age likelihood $p(t_0 \mid T) = 1/T$, said it holds under per-system sampling and under a constant birth rate alike, and left the hazard subsection conditioning on $T \gt t_0$ with no premise of its own. The two observations give different answers for the same prior $f$ on the hazard.

Take $f(k) \sim c\,k^{a-1}$ near zero, so $w(T) = \int f(k)\,k\,e^{-kT}dk \sim c\,\Gamma(a+1)\,T^{-(a+1)}$.

- Survival alone (item 1's constant birth rate with hazards varying across systems as $f$; or one system seen at a time unrelated to its start): the posterior is $w(T)/Q(t_0)$, the tail $(t_0/(t_0+u))^{a}$, the median $(2^{1/a}-1)\,t_0$. This is what the subsection states.
- The uniform-age likelihood applied to $f$ (per-system sampling, which the main derivation names as one of its two cases): the posterior is $\propto w(T)/T \sim T^{-(a+2)}$, the tail $(t_0/(t_0+u))^{a+1}$, the median $(2^{1/(a+1)}-1)\,t_0$. For a prior finite at zero hazard ($a = 1$) that is $(\sqrt2 - 1)\,t_0 \approx 0.41\,t_0$.

`tst-check-4.py hazard` simulates both with $f(k) = e^{-k}$: survival-only gives median remaining life $/(1+t_0)$ of 0.95–1.03, uniform-age gives 0.40–0.42, at $t_0$ = 10, 30, 100. (A third case, every system sharing one unknown $k$ and one alive system met at random among the alive, gives 0.41 too; whether meeting a system is itself evidence of how many are alive decides that case, and I would leave it out of canon.)

So the summary's "and at large age from an unknown constant termination hazard whose prior density at zero hazard is finite and positive", the subsection's untagged derivation, and the Epistemic Status's "a proper prior with the same tail" are each true only for a hazard prior about systems in general, observed through survival. That is the same distinction the "whose lifetime" subsection draws for Jeffreys' prior, and it applies here too. `#impl-foundations-features` (":42") repeats the claim as a robustness argument ("It is also robust. The same baseline follows ... from any unknown constant termination hazard ...") and inherits the gap; the record types that as F7 on that segment.

There is a stronger statement available, and it unifies the segment's two routes. Under the uniform-age likelihood the baseline needs $a \to 0$, $f \propto 1/k$: Jeffreys' prior on the hazard, which gives $w(T) = \int e^{-kT}dk = 1/T$, Jeffreys' prior on the lifetime, and so the scale-ignorance derivation itself. Under survival alone it needs $a = 1$, whose $w \sim f(0)/T^2$ is the $w \propto T^{-2}$ of item 2 made proper near zero. Being found in progress raises the tail exponent by one. Suggested text, appended to the hazard subsection's first paragraph after the median formula:

> This prior describes systems in general, $w$, and the conditioning on $T \gt t_0$ is item 1's: survival is the whole observation, as it is for systems met because they are alive while their hazards vary as $f$, or for one system seen at a time unrelated to its start. Under the uniform-age likelihood of the main derivation, the same $f$ gives $P(T \gt t_0 + u \mid t_0) \to (t_0/(t_0+u))^{a+1}$ and a median remaining life $(2^{1/(a+1)} - 1)\,t_0$, about $0.41\,t_0$ when $a = 1$. The baseline then needs $a \to 0$: $f \propto 1/k$ is Jeffreys' prior on the hazard, which gives $w \propto 1/T$ and the scale-ignorance derivation again. Whose lifetime the prior is about sets the multiplier here as it does for Jeffreys' prior.

And in the summary, "and at large age from an unknown constant termination hazard whose prior density at zero hazard is finite and positive, when that prior describes systems in general and the system is met because it is alive". The Epistemic Status's sentence wants the same clause. One more precision there: such a $w$ is proper, but for $a = 1$ its mean lifetime is infinite, so $T\,w(T)$, the lifetime of a system in progress, is not normalizable. The hazard mixture makes the prior proper near zero; it does not remove the impropriety at large $T$ from the in-progress reading.

### F2. Section (7)'s smallest-tail-share test needs more replicates, and with them obsidian-linter's capped fits reject (`#hyp-exponential-cognitive-load` item 3, the README, `elapsed_time.py`)

The statistic is right: a single-step min-$p$ over the eight readings, calibrated by the same replicates, is the standard way to account for their correlation. Pooling the observed history among the replicates (the exchangeable form) moves each value by at most 0.004. The resolution is the problem. At 1,000 replicates the observed smallest share is 13–20 replicate counts, and the shipped value is noisier than the binomial error the text cites. Re-run with more replicates (`tst-check-4.py minp REPS SEED`, whose null is the toolkit's loop; seed 12 at 1,000 reproduces the shipped line, and at 5,000 extends the shipped draws):

| history | shipped, 1,000 | 5,000 (seed 12) | 10,000 (seed 99) | 10,000 (seed 7) |
|---|---|---|---|---|
| corpus | 0.047 | 0.067 | 0.065 | 0.065 |
| obsidian-linter | 0.058 | 0.041 | 0.035 | 0.035 |
| ink | 0.062 | 0.060 | 0.062 | 0.061 |

The Monte Carlo standard error at 0.05 is 0.0022 at 10,000 replicates. Obsidian-linter's value moved from 0.058 to 0.035, about three times the "0.007" the text gives as the simulation's error. That figure is the binomial error of a share against a fixed threshold; here the threshold, the observed smallest share, is itself estimated from the same 1,000 replicates. Over twenty other seeds at 1,000 replicates (`tst-check-4.py minp 1000 1000,1001,...,1019`) the shipped statistic has a standard deviation of about 0.011 in each history, and ranges 0.019–0.061 (obsidian-linter, median 0.032), 0.048–0.084 (corpus, median 0.070) and 0.044–0.081 (ink, median 0.056). The shipped seed drew obsidian-linter's from the top of its range and the corpus's from the bottom.

So "All three sit at the edge of a 5% test, within the simulation's error of it" and "alone, settle it in none" are not what the data say. In obsidian-linter, the history whose window-free test already rejects a pure exponential, the capped fits alone reject it too, at about 3.5%; in the corpus and ink they do not (6.5% and 6.1%). Ink's null is also built from the one-idle fit that Limits now calls a chosen local optimum, so ink's number inherits that. Suggested replacement for item 3's last three sentences:

> They do so in 6.5% of 10,000 replicates for the corpus, 3.5% for obsidian-linter and 6.1% for ink. In obsidian-linter, then, the capped fits alone reject a pure exponential at the 5% level, narrowly; in the corpus and ink they lean against it without settling it.

These figures are from seeds 99 and 7; the toolkit's seed 12 at 10,000 will differ in the third decimal, and the text should quote what the toolkit prints.

And in `elapsed_time.py`, `windowed_null`'s `reps` at 10,000 (about five minutes for the three histories on this machine), with the README's two numbers updated to match. "The capped fits lean against a pure exponential in every history" stays true.

### F3. The persistent-bias sentence omits persistent misalignment from its floor, and the Epistemic Status still calls miscalibration unstructured (`#hyp-communication-gain`)

The saturation is right (my re-derivation agrees with the integrator's C3 and with `#deriv-tempo-additivity`'s "[Derived (saturation-under-persistent-bias)]"). Two sentences around it are not yet consistent with it.

- The new text says "so is a systematic misalignment", then gives the floor as precision $1/U_{\text{src},j}$. If misalignment persists across $j$'s messages too, the shared error has variance $U_{\text{src},j}$ plus the persistent part of $U_{\text{align},ji}$, and the floor is the reciprocal of that sum. Suggested: "what they tell $i$ about the quantity saturates at the precision of the source's persistent error: $1/U_{\text{src},j}$ when miscalibration is the only persistent part, less when misalignment persists too."
- The Epistemic Status keeps "This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured." The Formal Expression now says the opposite about $U_{\text{src},j}$ across a source's messages. Suggested: "This is appropriate for $U_{o,ji}$ (channel noise), and for $U_{\text{src},j}$ (miscalibration) within one message; across a source's messages its miscalibration is persistent, which the Formal Expression treats."

### F4. The baseline's premise is stronger than "absent specific information", and `#der-change-investment` does not inherit it (the integrator's question 1)

Round 4's Epistemic Status scopes the derivation correctly: no time scale known for the lifetime of the system in front of you, judged case by case. The opening sentence still says "Absent specific information about a software system's future", which is weaker. Caves (2000, p. 13) makes the difference concrete for exactly this class: the survival of a human institution, he writes, "is influenced by the 30-year time scale of a generation or by a typical human lifetime", and he counts the institutions among Gott's examples as phenomena with "readily identifiable time scales". Generic knowledge about software (platform and dependency lifetimes, team turnover) can be a time scale without being specific information about this system. Suggested opening: "When no time scale is known for a software system's lifetime, the uninformed median baseline ...". Whether software generally meets that premise is the empirical question `item:tst-cheap-falsifiers-and-measurement-design` (a) already owns.

Downstream, `#der-change-investment`'s Epistemic Status (":29") says it "inherits the assumptions of #der-change-expectation-baseline (median prediction ... and uniform feature rate)". Round 4 made the scale-free premise the baseline's governing assumption, and it is not in that list. Suggested: "(no evident time scale for the system's lifetime, median prediction ... and uniform feature rate)". In the record this is C9's finding, on that segment. The baseline's own Discussion item "We're sunsetting next quarter → $\hat n_{\text{future}} \to 0$" reads as an update to the baseline while the Epistemic Status says an announced end means the baseline does not apply; both are true, and a cold reader may need "(the uninformed baseline does not apply; the information replaces it)".

### F5. Ink's numbers in item 2 come from the chosen local optimum without saying so there (the integrator's question 3; `#hyp-exponential-cognitive-load`)

Item 2 gives ink's exponent 0.30 $[-0.04, 0.76]$ and log-likelihood gap 0.8; Limits, two paragraphs on, says those come from the fit with time away above working time, which is 1.4–2.1 below the best. "Not distinguished" holds at both optima: the label-swapped best fits differ by 0.7 between power and exponential (section (6), last line). The specific numbers do not. I would keep ink in the sentence and qualify the numbers inline: "Their working-time exponents are 0.30 $[-0.04, 0.76]$ (ink, from the fit with time away above working time; see Limits) and 0.50 ...".

### Smaller points (F8 in the record, except the last)

- "Both $\pi \propto 1/T$ and $w \propto T^{-2}$ are improper near zero": $\pi \propto 1/T$ is improper at both ends.
- The Lineage says Caves "read that prior as the density over all phenomena". He also says, in so many words, that $w_g$ "is different from the Jeffreys prior that Gott identifies with his predictions, the reason being that Gott uses the flawed Bayesian analysis", and that the Jeffreys prior "corresponds to invariance ... under rescaling of $t_p$ or $t_f$, but not both". The segment's reading (Jeffreys' prior on the in-progress lifetime $p(T \mid I)$ is $w_g$) is mathematically right and is marked as the segment's; a clause saying that Caves himself draws the contrast with Jeffreys' prior on $w$ would stop a reader from attributing the reading to him.
- `#impl-developer-agent` (":23") spells it "Jeffrey's-prior-derivation".

## What holds

- **The scale-ignorance derivation** (C1). $\pi(T) \propto 1/T$ times $1/T$ normalizes to $t_0/T^2$ on $[t_0, \infty)$; the survival is $t_0/(t_0+u)$, the median $t_0$, at every age. Item 1: with births at rate $r$ the count alive is $r\,w(T)\,dT\,dt_0$, so the posterior given age is $w(T)/Q(t_0)$ whatever the mean. Item 2 follows from the same count, not from item 1: integrating over age gives $T\,w(T)$ and uniform age given $T$; Jeffreys' prior on that forces $w \propto T^{-2}$, $Q = 1/t$. The rescaling form checks: $p(\alpha t_p, \alpha t_f)\,\alpha^2 = p(t_p, t_f)$ with $p \propto w(t_p + t_f)$ gives $w(\alpha T) = w(T)/\alpha^2$. Jeffreys' prior on $w$ conditioned on survival leaves $1/T$ on $(t_0, \infty)$, not normalizable. The main derivation's "holds whether ... drawn from among all systems ... or met because it is alive now" is right for the likelihood; the prior it is placed on differs between the two (the drawn system's $w$, or the in-progress $T\,w(T)$), which the next subsection explains.
- **Caves** (C3), read in the arXiv text pp. 12–13: Eqs. (30)–(32), "$w_g(T)$ has a scale-free status similar to that found by Jaynes for the Jeffreys prior", "$w(\alpha T) = w(T)/\alpha^2$", "Whether the scale-free prior information is appropriate must be judged case by case; it is not a universal rule." The segment's citations of Eqs. 31–32 and of the case-by-case caveat are faithful.
- **Source-bias saturation** (C4): with $o_n = \theta + s + e_n$ the sample mean is sufficient, with variance $U_s + U_e/n$ about $\theta$; the posterior variance tends to $(1/U_0 + 1/U_s)^{-1}$, and an update charging $U_s + U_e$ afresh tends to zero. Agrees with the integrator's numbers.
- **The toolkit** (C5): the three dumps at the header's HEADs; the merged script's output differs from the round-3 script's only by the two new lines per history (`diff`), and those give 0.047, 0.058, 0.062 and the label-swapped ink fits (best $-912.9$, $-912.2$, $-912.2$ against reported $-915.0$, $-914.2$, $-913.6$), as item 3, Limits and the README cite. Item 1's new reading of ink's top bins (5–37 and 1–137 minutes) matches section (6)'s intervals.
- **The README's squash-merge evidence** (C7): all 63 of obsidian-linter's "(#N)" commits and 191 of ink's 261 have committer `noreply@github.com`; equal author and commit dates hold for 1,036 of obsidian-linter's 1,269 other commits and 354 of ink's 403.
- **Restatements and generated output** (C8): `#der-dual-optimization`'s Novelty Claim and Related Work row match the baseline (subject to F1's qualifier, which "Bayesian survival analysis under ... an uncertain constant hazard" already carries in the word "survival"); `bin/extract-findings` run in a worktree at `a1fa9024` reproduces `FINDINGS.md` and the summary partial byte for byte. `md-press` reports nothing to change in the touched segments and the two lane files.

## The integrator's three questions

1. Item 2 follows from the birth-rate count directly, and item 1's posterior then gives the same $t_0/T^2$; yes. The case-by-case caveat is the right scope, but it is stated only in the Epistemic Status, and the opening sentence and `#der-change-investment` still carry the weaker premise (F4).
2. The min-$p$ is the right statistic. Each replicate's tail shares are computed against a set that includes itself but not the observed history, which makes the shipped value slightly anti-conservative, by at most 0.004 here; pooling the observed history among the replicates removes it. The number of replicates is what decides the reading (F2).
3. Ink should stay in "not distinguished", which holds at both optima; its two numbers want an inline qualifier (F5).

## Check 3's findings

Answered by the round-4 revisions and recorded as answered in `vsect`: `review:tst-lane-check-3#C4/finding` (ink's local optimum, in Limits, the README and section (6)), `#C5/finding` (item 1 reads the intervals; item 3 now names a criterion, whose resolution F2 takes up), `#C6/finding` (the persistent-source regime is named; F3 is about two sentences beside it), `#C8/finding` and `#C9/finding` (the scale-ignorance restructure and the constant birth rate).

Of check 3's own checks, which lapsed when round 4 changed the texts they read: C3 (the two-idle interval) and C7 (Appendix F's fates) I confirmed with `vsect confirm --judgment for-checks`, since round 4's diff does not touch what they checked. C1, C10, C11 and C12 I re-took at the current versions instead (my C5, C3, C7, C8), because the text they read changed in the passages they checked. C2 lapsed through upstream segments outside this lane and is not mine to judge. The older lapsed checks from rounds 1–3 I left for their lanes. Minutes after they were taken, my C1 and C3 already show as lapsed upstream, through another lane's revisions of `#def-observation-function` and `#scope-adaptive-system`, on which the baseline rests through `depends:`; that is the ledger working, not a defect in this check.

The record's `written:` time was typed rather than read from the clock; the take event's `at:` (03:27:29Z) is the true time, and the event is annotated to say so.

## H.2

Nothing in `a1fa9024` creates, moves or gives a fate to an `old-*` file. This round serves H.2 only in that it is the lane that `old-tst-*` fates opened.

## On the process

The account's list of what a verifier might look at was useful as context and did not steer: F1 is in none of its three questions, and it came from reading the restructured segment as a cold reader would, asking what each subsection's conditioning assumes. One thing I would do differently in the toolkit generally: a Monte Carlo p-value that is reported beside a threshold wants its replicate count set by the distance to that threshold, not fixed in advance.

I am staying on the line.
