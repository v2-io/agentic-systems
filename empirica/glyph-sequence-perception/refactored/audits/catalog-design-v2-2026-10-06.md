# De novo audit: the catalog design, version 2 (CATALOG.md; METHODOLOGY §2a concern 6)

*2026-10-06, Claude Opus 5.5, a session that wrote neither version of the design nor the first audit. Written for the session that wrote it and for Joseph, before anything is built. I changed no file but this one, and I touched no running process. My only contact with Postgres was `psql-18 --version` (18.6).*

## How I worked, and what this rests on

I read `CATALOG.md` and `METHODOLOGY.md` whole, then `HANDOFF.md` and the top of `PROGRESS.md`. Where a claim needed checking against code, I read parts of `probe/probe.py`, `priority/plan.py`, `tree/tree.py`, `report/best.py` and `run.py`, plus the thinking spike's `report.md`, `../data/seeds/` and `../data/growth/`. For numbers I read `data/answers/*.jsonl` in place, read-only, at about 18:40 UTC (rounds through c092, 257,017 records), using throwaway scripts in my scratchpad. Most counts are therefore slightly larger than the design's through-c090 figures.

I read the version-1 audit (`catalog-design-2026-10-06.md`) only after my own findings were drafted, so that it wouldn't steer my reading. I then used it to check §13's claims about which findings were addressed (*Version 1's findings*, below).

Labels: **[measured]** means counted from the answer files; **[checked]** means read in code or docs; **[reasoned]** means it follows from the design as written and I haven't run it. I fitted no model.

Partway through, the coordinator asked about a proposed refinement to the seed rater. I answered by message; the substance is in *The seed refinement* below, so that Joseph has it too.

## Summary

Version 2 is a large improvement on what the first audit describes. It has separate contrasts per part, raters as minds in conditions, strength and certainty side by side, untested shown as a state, an explicit dependence table and real acceptance tests. Those are the right commitments, and most of them should survive the build.

The remaining problems concentrate on one point: the design's central purpose, which is to rank intuitive recognition above chart-borne recognition (§2). As written it can't do that. The instruments meant to separate the two either don't exist for the runs where the question arises, or measure something else:

1. **R-chart has no control for monotone runs** (A1). Its control is the same glyphs in code-point order, which for a monotone run is the run itself. About half of what is asked whole is monotone, including every chart walk and the first canary, `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`. So acceptance test 4 can't be run, and "chart-borne" can't be assigned where it matters most.
2. **R-shuffle ranks chart walks first, by construction** (A2). Contiguous code-point runs are called coherent 97% of the time by Claude and 96% by Grok; non-monotone runs 59% and 75%. No choice of false-positive rate changes that order. The design's main defence, R-chart, is missing exactly there (A1).
3. **"Intuitive" defined by deliberation condition is, on cohere, Claude** (A3). Grok always thinks, and Gemini has no cohere answers. Sonnet's and Opus's zero-thinking sheets are chosen by the models themselves, not assigned. The study's own spike found that thinking doesn't change chart-following.
4. **The strength and certainty quantities have no single generative model behind them** (A4). Dawid–Skene's binary latent class can't represent graded strength. The strength formula (Abbott) is defined only for yes/no parts, and the family weighting is a second weighting laid over a likelihood.
5. **Kneser–Ney branch shares contradict §7** (A5). Interpolation is backoff. This came in through the first audit's own recommendation.

The other findings concern definitions, inputs and tests (A6–A11), with strengthening routes where I found them. Several instruments that would close A1 are cheap, and some already half-exist in the data.

---

## A1. R-chart is undefined for monotone runs, and test 4 can't be run

**What the design says.** §6b: R-chart is evidence from "cohere and order questions on runs whose visible order and code-point order disagree", against "the same glyphs in code-point order". "Chart-borne recognition is a run whose R-chart part is near zero while R-shuffle is high." §12 test 4: chart walks (`🨀 🨁 🨂 …`, the `Ý Þ ß à` crossing) "must score lower on R-chart than the felt runs of test 3".

**What follows** [checked, reasoned].

- `▁ ▂ ▃ ▄ ▅ ▆ ▇ █` is U+2581–U+2588, monotone, and so are `🨀 🨁 🨂` and `Ý Þ ß à`. For all of them, visible order equals code-point order, so R-chart has no control and no value. Test 4 compares two quantities that don't exist. The second canary, `█ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔`, is non-monotone (U+2588, U+1FB86 … U+2580 … U+2594), so it does get an R-chart part.
- "Near zero" and "absent" will be conflated unless the design separates them. Either every monotone run reads as chart-borne, or none does, depending on how a missing value is handled.
- How common this is [measured]. Of Claude's cohere answers on real (non-control) runs, 1,651 are on runs whose code points are contiguous, 941 on monotone non-contiguous runs and 2,400 on non-monotone runs. So 52% of whole-run evidence sits where R-chart can't exist. Of the 639 forward survey seeds, 313 are contiguous and 146 monotone: 72%.
- Where R-chart does exist, it is often close to a second shuffle [measured]. For non-monotone runs asked whole, the code-point-sorted arrangement of the same glyphs is itself contiguous in 662 of 3,293 answers (20%). In 1,772 (54%) the glyphs span more than 64 code points, so "code-point order" is a jump across blocks that no one would read as a chart walk. A low "yes" on that control says the sorted order is incoherent, not that the chart can't explain the run.

**Why it matters.** Joseph's distinction (§2) is about runs where chart and perception could both explain recognition, and the monotone runs are the main such class. His words are "monotonic perceptual sequences that were also monotonic in chart order", which he finds "fine", against intuitive sequences that are "(much) better". The design measures the chart/perception contrast only where the two already disagree, which is the easier half.

**What could make the claim true (strengthening first).** Each of these is a probing addition (§11) or a read of data that already exists:

- **Discriminator positions.** At a monotone run's ends, and inside it wherever the chart has a neighbour that isn't in the run, chart-next and perceptual-next differ. After `▇` the chart gives `▉` (U+2589, left seven-eighths); the felt run gives `█`. After `█` the chart gives `▉` again, and the felt cycle gives `🮆`. An inhibit or two-alternative question at those positions, perceptual candidate against chart-next intruder, measures chart-following run by run. This is the narrower tag the embedding spike's verifier proposed (HANDOFF), and §11's canary note (after `🮄`, `🮃` ×8 against `▀` ×2) is one instance. The triad era shows the stakes: its grown row for the ramp is `_ ‗ ▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ █ 🮆 🮅 🮄 ▀ 🮃 🮂 🮀` [measured, `../data/growth/r006.json` onward], with the chart intruder `▉` inside it.
- **Lookalike substitution.** Replace one glyph of a monotone run with a near-identical glyph from another block, so the code-point order breaks and the look doesn't. If recognition survives, the chart wasn't needed. The block elements have lookalikes among the legacy-computing symbols, so the canary can be tested this way.
- **The unassigned-code-point marker at the run's ends.** METHODOLOGY §4 already treats continuations into unassigned code points as "a clean marker of code-point arithmetic". Counted per run at its open ends, it is evidence that this run is extended by arithmetic.
- **A class-level control for monotone runs.** Chart windows (tags `control: chart`) are code-point order alone. Claude calls them coherent 0.84, Grok 0.82 [measured]. A monotone run's whole-run yes rate against that class rate is a weak but real R-chart for the monotone case. Weak, because both sit near ceiling.
- **A fourth label.** Where chart and perception coincide everywhere and no discriminator exists, the honest state is *chart-congruent, undiscriminated*, not chart-borne and not intuitive. The ranking in §2 needs a place for it.

If the first two exist before the build, test 4 can be restated against them and becomes the discriminating test it was meant to be.

## A2. R-shuffle ranks chart walks first, by construction

**What the data show** [measured, cohere, yes share of yes/no/can't-tell answers, rounds c001–c092].

| family | real: contiguous | real: monotone | real: non-monotone | shuffles of contiguous | of monotone | of non-monotone |
|---|---|---|---|---|---|---|
| Claude | 0.973 (1,651) | 0.787 (941) | 0.587 (2,400) | 0.127 (1,630) | 0.195 (915) | 0.281 (2,304) |
| Grok | 0.964 (633) | 0.881 (394) | 0.745 (893) | 0.339 (632) | 0.375 (381) | 0.481 (837) |

Abbott strength, $(p - c)/(1 - c)$, with each class's own shuffle rate as $c$: Claude 0.97 / 0.74 / 0.43, Grok 0.95 / 0.81 / 0.51. With Claude's pooled shuffle rate (0.213): 0.97 / 0.73 / 0.48.

**Why it matters.**

- R-shuffle asks whether this order is recognised beyond a scrambled order of the same glyphs. Code-point order is a strongly recognised order, so chart walks lead on R-shuffle whatever the false-positive rate. This isn't a calibration bug, and better rates won't remove it: stratifying by class lowers non-monotone strength slightly. It is what R-shuffle measures.
- §6b builds the intuitive tier from R-shuffle, L-near and G, "together with R-chart wherever its control exists". G inherits the same lean: 92% of the 5,201 continuations that reach the 24-glyph cap are ±1 code-point walks [measured]. With R-chart absent on monotone runs (A1), the top of the intuitive tier will be chart walks. That is the "very obvious answer" Joseph says he isn't excited to rediscover.
- The false-positive rate still depends on the class of run (about 2.2 times from contiguous to non-monotone for Claude), so the rater model should carry it. A single per-rater rate per part, which is how §6c reads, misstates certainty for every run outside the mix it was estimated on.

**What could make it true.** Keep R-shuffle as what it is: evidence that an order is felt beyond its scramble. Rank the intuitive tier on parts that can tell perception from the chart (A1's instruments) wherever chart and perception coincide, and say in §6b that R-shuffle alone can't distinguish them.

## A3. "Intuitive" as a deliberation condition is, on cohere, one family and partly self-selected

**What the design says.** §6b: intuitive recognition is evidence "from raters in conditions without deliberation"; rational is "the same parts from deliberating raters (thinking on, reasoned)". §6c: "A rater is a mind in a condition: thinking budget, effort, prompt variant, protocol era."

**What the data show** [measured, thinking tokens per answer, real answers, c-rounds].

| kind | mind | answers | share with 0 thinking tokens | median |
|---|---|---|---|---|
| cohere | haiku45nt | 4,601 | 1.00 | 0 |
| cohere | sonnet55 | 4,601 | 0.92 | 0 |
| cohere | opus55 | 957 | 0.90 | 0 |
| cohere | haiku45 | 930 | 0.00 | 1,222 |
| cohere | grok46 | 4,264 | 0.00 | 338 |
| continue | gemini38flash | 4,145 | 0.89 | 0 |

Gemini has no cohere answers and 4 inhibit answers.

**Why it matters.**

- **No-deliberation cohere evidence is all Claude.** Grok always thinks, so all of its evidence lands in the rational tier. The intuitive tier on R-shuffle is therefore Claude's judgement. §2 says the rater model exists so that "volume from one family and fluency with the chart can't stand in for perception", and here the tier definition does that on its own.
- **Measured thinking isn't an assigned condition.** Sonnet thinks adaptively (HANDOFF: "about one sheet in five with zero" on continue; 92% zero on cohere), so whether a Sonnet answer had thinking depends on the sheet. Treating it as a rater condition puts an outcome of the item on the rater side. Only `haiku45nt` (budget 0) and `haiku45` (31000) are assigned conditions. Of the Claude minds, `haiku45nt` discriminates least on shuffles (0.34 yes against Sonnet's 0.11).
- **The condition doesn't track what Joseph cares about.** In the thinking spike, Haiku's first glyph was the last context glyph ±1 code point 0.96 of the time with thinking on and 0.94 with it off. For Sonnet the budget lever made no difference (`spikes/thinking-felt-2026-10-05/report.md`, METHODOLOGY §4: thinking "did not make Haiku more chart-bound"). `haiku45nt` calls chart windows coherent at 0.84, the same as Sonnet [measured]. Joseph's criterion is that a sequence "doesn't need internal arithmetic or thinking about the glyph's name and codepoint". That is about what the recognition rests on, not whether tokens were spent. A thinking-off rater can still follow the chart, and a thinking rater can reason about shapes.
- **The condition is nested in family.** Grok has no off condition and Gemini has no cohere data, so a hierarchical model can't separate "condition" from "family" on cohere. "Whether a condition matters … is read off the fit" (§6c) holds only within Claude.

**What could make it true.**

- Define the intuitive and chart-borne tiers by what recognition survives: discriminator positions, lookalike substitution and the unassigned marker (A1). Keep deliberation as a measured covariate whose effect is reported, the answer to METHODOLOGY §4's question, rather than the definition of a tier.
- If deliberation stays an axis, use assigned conditions only. Make it identifiable across families: Gemini Flash on cohere and inhibit (HANDOFF lists letting its drain take new kinds first as "offered and not decided"), and §4a's low-effort contrast.
- §2's sentence that Claude's minds "most readily read glyphs as chart positions" should carry its evidence, which is mixed. On the unassigned-code-point marker (METHODOLOGY §4), the Gemini minds (15–21 per 1,000) exceed Sonnet (9), Grok (8) and Opus (0), and only thinking-on Haiku (35) is higher. The table in A2 supports it in one respect: Claude's recognition gap between contiguous and non-monotone runs is 0.39, Grok's 0.22. Claude is the most voluminous family; whether it is the most chart-reading one is not settled. On cohere, the Claude–Grok difference is also a difference of deliberation.

## A4. One generative model for strength and certainty

**What the design says.** §6a: strength is Abbott's $(p - c)/(1 - c)$ per rater, combined over raters, with an interval. Certainty is "a weight of evidence in decibans, itemised by answer". §6c: rates are fitted by three-category Dawid–Skene with EM. Families are pooled hierarchically, and "each family's pooled contribution enters once, weighted by its own measured discrimination".

**The tension** [reasoned].

- Dawid–Skene has a binary latent class per item (true or false) with one true-positive rate per rater. Under it, every true item has the same expected yes rate for a given rater, so "a run at 60% and a run at 95%" (§6a) differ only by noise. Graded strength, the quantity §6a puts first, has no place in that model. Test 8 will find the item-level spread as overdispersion. That spread is the signal.
- Abbott's formula is defined for yes/no parts. G is a likelihood ratio, O is an ordering model (Mallows dispersion or Plackett–Luce worths), and Seed is a reliability. For those three, §6a's "strength" is undefined.
- Per-answer decibans add up exactly only against a point alternative (a stated strength under $H$). With fitted rates, each answer's contribution also depends on the whole fit. That's acceptable if stated. The stated alternative is the substance of "certainty".
- The family weighting sits on top of a likelihood. In a likelihood model, evidence adds by answer, and volume counts. "Enters once, weighted by discrimination" is a different combination rule: a weighted mean of family estimates. Both are defensible, but they can't both be the rule. On cohere, discrimination-weighting means Claude: Sonnet's shuffle rate is 0.11, Grok's 0.41. A2's table suggests that shuffle discrimination partly is chart-reading: Claude rejects shuffles of contiguous runs far more often than shuffles of non-monotone ones.

**What could make it true.** One latent-strength model can deliver both quantities. A candidate: for rater $r$ and item $i$, $P(\text{yes}) = c_r + (1 - c_r)\,s_r\,\theta_i$, with $\theta_i \in [0, 1]$ the item's strength, $c_r$ its false-positive rate (from that part's controls, by chart class per A2), and $s_r$ its sensitivity (a logistic item-response form works too). Strength is the posterior of $\theta_i$. Certainty is the weight of evidence for $\theta_i \gt 0$ against $\theta_i = 0$, itemised as each answer's log-likelihood ratio at a stated alternative. Hierarchical priors on $c_r$ and $s_r$ give the family pooling. The family combination rule is then one stated choice, either the likelihood's own or a weighted mean of family $\theta$s, with its reason. For G, O and Seed, the design should say what plays the role of $\theta$.

One reassurance [reasoned]: the planner chooses what to ask from earlier answers, and those answers are all in the data. So for a full-likelihood fit the selection is ignorable (missing at random). The danger is in summaries over selected subsets, which is A6.

## A5. Kneser–Ney branch shares contradict §7

§6d: branch shares "come from interpolated Kneser–Ney". §7: "No prior, backoff or neighbouring evidence fills them in", and evidence only at a suffix is "reported as such, never substituted". Interpolated Kneser–Ney gives every context a share for continuations named only at its suffixes, plus discounted mass for unseen ones. That is backoff. It also counts answers pooled across raters, which §6c exists to prevent.

This entered through the first audit's F3, which recommended Kneser–Ney for a descriptive generation part without reconciling it with its own F5 ("untested is a state").

**What might hold.** A record's branch shares can be the raw per-context shares with their intervals, per rater and family, which the design already keeps "beside them". If a smoothed view helps priority, it can be a labelled reader view that never enters a record's part.

## A6. G's likelihood is calibrated on selected links, and the caveat was dropped

§6d bases G's weight on "the median share of first continuations naming such a link is 0.5, and 14% are never named". The first audit attached a caveat: "many of those inhibit questions were asked *because* shown answers ended there". Version 2 drops it, and the caveat goes to the heart of the matter [measured, inhibit by `source.why`]:

| why the inhibit was asked | answers |
|---|---|
| `recognize-written` (written past a shown end) | 3,374 |
| near / far controls | 2,154 / 1,962 |
| `falsify-skip` | 1,706 |
| `recognize` | 912 |

The largest class of recognised links was asked because first-impression generation at that shown context had stopped. Calibrating "how often recognised links are named" on them builds "not named" into the recognised distribution by selection, which makes G's "not named" look uninformative. The rejected distribution is mostly skip tests, links two steps on, which are almost never named first by construction. So the likelihood ratio for "named" is inflated too.

**What might hold.** Calibrate on links whose inhibit question was chosen independently of their generation. A tagged random sample of recognition targets would do, as would the tendril branches. Alternatively, carry the reason for asking as a covariate. That requires putting it in `tags`, since the catalog doesn't read `source` (A8).

## A7. Runs, links and "own context" under the 8-glyph context cap

**Facts** [checked, measured]. Continue and inhibit contexts are asserted to be 2–8 glyphs (`probe.py` lines 141 and 147; plan.py line 91 gives `(2, 8)` for every kind except cohere, order and pick). Every shown continue or inhibit context in the data is 2–8 glyphs long. The tree trims written contexts to "its last ≤ 8 glyphs" (`tree.py` line 13). Written continuations are cut at 24 (`MAX_CONTINUE`), and 5,201 of them stop there exactly.

**Consequences.**

- In a run of more than 9 glyphs, no link after the ninth can have shown evidence at its full prefix. Under §7's three states, every such link is permanently "evidence only at a suffix" or written-only. That is a fixed feature of the probe, not a gap a question can fill.
- §4's enumeration rule ("every maximal run of links that each carry evidence of their own") reads two ways. If "own context" means the full prefix, maximal runs from shown evidence stop near 9 glyphs, and longer ones come almost only from single written answers, mostly chart walks (A2). If it means any context ending at the link, maximal paths through a branching graph grow combinatorially, and the "linear in the candidates" claim fails. The design should say which it means.
- A continuation that reaches the 24-glyph cap is censored, not ended. Nothing in §6d or §7 says so, and an "end" read from it would be false.

**What could make it true.** METHODOLOGY §3 already has the bridge the catalog needs. A link holds at a long context when it is stable: minds agree at its $k^\ast$, and the prediction stays put when the context is lengthened backward. Suffix evidence then stands for the longer context because lengthening was tested and nothing flipped, not because a prior fills it in. Four states would say this: evidence at its own context; at a suffix, with lengthening tested and no flip (up to the 8-glyph cap, stated as a cap); at a suffix, untested for flips; none. The enumeration rule can then use the first two. Whether 8 is right (it reads like the pick cap §1 calls a loss) is a probing question. Whatever the answer, the catalog should state the cap, because it sets the reach of every long run's link evidence.

## A8. Inputs: what §5 and §6b leave unassigned or change silently

- **Reasoned answers become evidence.** §5 makes `sonnet55r` evidence "as distinct rater conditions" (the rational tier). METHODOLOGY §4 says its answers "are kept apart from the tree's evidence (`Tree.reasoned`) and never confirm a link". That is a change of policy, the same kind as the first audit's F9, and it should be named as one for Joseph.
- **`next` and `between` have no part.** §5 lists both as evidence. In §6b's table, G takes "continue (shown), picks", and nothing takes the triad era's `next` (6,248 records with up to 3 ranked proposals) or `between` (1,370 two-sided fills). `next` presumably belongs to G, with rank handled. `between` is its own kind of claim and needs a part or a stated exclusion.
- **`limit` isn't an outcome** [checked, measured]. A usage-limit call is recorded as `call-failed` with reason "limit" (`probe.py` line 443, `run.py` line 203). No record has outcome `limit`. Excluding it is still correct, but the §5 row describes something the data don't contain.
- **Joseph's and the dropspot seeds aren't answer records** [measured]. `data/answers/seeds.jsonl` holds the survey minds only (fable-1, sonnet5-1, grok-1, sonnet-survey-1/2/4, sonnet-3). `../data/seeds/joseph-block-fill-cycle.jsonl` and the other dropspot files reach the planner, not the answers. "Joseph when he proposes a run" (§6c) has no input until those seeds are ported as tagged votes.
- **Seed votes are clustered.** One survey sequence becomes many records: every prefix, in both directions (the dice seed `⚀ … ⚅` alone gives 10). §6f clusters written answers by answer but not seed votes by seed.
- **Seed raters and family pooling.** The seed records carry `family: claude` or `grok`. Pooled toward family, a surveyor would borrow rates from the first-impression judges, and the reverse. That should be ruled out.
- **Controls without `source`.** Skip tests are identified only by `source.why`, and shuffles are paired with their originals only by `source.of`. Both can be derived structurally: a skip is the candidate two steps on in the record's own run, and a shuffle has its original's glyph set. The design should say so, because the obvious implementation reads `source`. One wrinkle: reordered candidates (shuffles a mind called coherent, 1,207 answers) share their original's glyph set, so pairing by glyph set is many-to-many. `tags.control` keeps control answers out of the candidate's evidence, as METHODOLOGY §4a requires.
- **The skip control isn't a clean negative.** "Yes" to the glyph two steps on is sometimes right: `▁ ▃ ▅ ▇` is a sequence too. L-skip's false-positive rate is therefore an upper bound, and it is high for exactly the families that see coarser sequences.

## A9. Cycle and branch records

- **Neither has defined parts.** §8 says every record carries parts with strength and certainty. For a cycle, it isn't stated which answers count (manifestations? cohere on a period?) or what the control is. For a branch, it isn't stated what is measured. The METHODOLOGY branch is a context with differing continuations, so its natural part is the branch shares at the divergence context.
- **Branch relations are pairwise.** "A pair of records sharing a terminal sub-run" with no minimum length relates every pair of records that share one end glyph. That count is quadratic in records. A minimum shared length, or the METHODOLOGY definition (shared context, then the separating continuation), keeps it bounded.
- **Manifestation is bounded by the caps** [reasoned]. A mind manifests a cycle of period $P$ by writing the rest of the period and then all of it again from a shown context shorter than $P$, so it writes $2P - \text{shown}$ glyphs. With shown at most 8 and written at most 24, $P \le 16$, and the 15-glyph block-fill cycle needs a shown context of at least 6. Test 3's "the full cycle once its answers are in" depends on the planner asking it from long enough contexts. "Runs are not bounded" (§4) should say that manifestable cycles are.

## A10. The acceptance tests

- **Test 3 can pass for the wrong reason.** Contiguous runs sit at a 0.97 yes rate (A2), so `▁ … █` will be in the upper quarter of its length band along with the chart walks. Test 4 was meant to tell them apart, and it can't be run (A1).
- **Canary provenance.** The top-down canary `█ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔` is the independent session's completion of Joseph's `▁▂▃▄▅▆▇█🮆🮅🮄...` ("Completed by the independent session … not typed by Joseph", `../data/seeds/joseph-block-fill-cycle.jsonl`). A fable-1 survey seed corroborates it (`🮂 🮃 ▀ 🮄 🮅 🮆 █`), and the triad era's grown row differs (it has `▉`, and ends at `🮀` or `🮁`, not `▔`). Test 3 should say this.
- **Tuning risk.** The design has many free choices: strata, pooling, the combination rule, discounts, thresholds. Tests that name the expected winners invite choosing among them until the canaries pass. Freezing the model choices before the canaries are computed, and recording that order, would keep tests 3 and 4 honest.
- **Test 2 is close to a split-half check of a binomial rate.** It confirms that each control class is homogeneous, not that the rates transfer to candidates. Leaving out a whole control class (fit without chart windows, predict their yes rate from the model's covariates) tests transfer.
- **Test 5 can't fail.** §4 makes every candidate input a record, so "all 4,905 rows are records" holds by construction. The informative version asks what fraction have any whole-run evidence, and what their parts say.
- Tests 6–9 look right to me as stated.

## A11. Smaller points

- **Priority targets what moves.** §9 asks where a record's intuitive parts are "most likely to move". The design acknowledges that certainty then grows with asking (§6a). Strength intervals are also mildly biased under outcome-dependent sampling. That's minor beside A1–A4, but worth one line in §9.
- **The manifest should include candidate inputs.** These are `../data/growth/` and `../data/seeds/`, which HANDOFF schedules to move to `.archive/triad-era/`. Hashes of the files won't care where they live, but the build's paths will.
- **Where computation lives.** §10 keeps "the JSONL-over-Python path" as reference "until the database reproduces it record for record". If EM, the ordering model and Kneser–Ney run in Python and Postgres stores and serves the results, there is one implementation, and the parity test is a load check. If any of them is meant to run in SQL, the design should say which, because two implementations of an EM fit are expensive to keep in agreement.

---

## The seed refinement (the coordinator's question, answered during the audit)

The proposal says recognition is easier than generation. So a reasoned seed predicts recognition with less effort, which would offset §6c's discount, bounded by the faculty: chart-generated seeds predict only chart-verified recognition. The offset would be measured as no-deliberation raters' recognition of seed runs beyond shuffles.

- **The principle is sound, and the boundary is right.** Joseph's tendril design assumes the same asymmetry ("most of them are easier to recognize than to generate"). Cheaper isn't the same as non-deliberative, though: checking a chart walk is a cheap chart operation. The boundary is best stated as a property of the run and of the verifying mind, since how a survey seed was generated isn't observed. And the argument isn't specific to seeds: it applies equally to `sonnet55r` and the picks, so it belongs as one measured fact about generators.
- **The boundary can't operate on most seeds yet.** 72% of seed runs are monotone, where R-chart doesn't exist (A1).
- **The proposed measurement rewards chart-generated seeds.** Recognition beyond shuffles is highest for contiguous runs (A2). Seed-sourced runs score 0.84 (Claude, no deliberation) and 0.94 (Grok), against 0.99 and 0.97 for walk-sourced runs [measured].
- **It isn't identifiable yet.** No-deliberation cohere raters are all Claude, and 426 of 639 seeds came from Claude surveyors. The measurement would mostly be Claude recognising Claude's generations (A3).
- **Double counting.** A seed's weight estimated from how its runs fare on cohere, then added back as evidence for those runs, counts the same answers twice. The weight is honestly a prior for seed runs not yet asked whole, and should fall away once a run has its own evidence.

A sharper wording I offered: *a generator's weight on the intuitive parts is measured, per chart-congruence class, as the rate at which raters of a family other than the generator's, in an assigned no-deliberation condition, recognise its runs beyond the class-matched control; it applies only to runs without whole-run evidence of their own; until a non-Claude no-deliberation rater answers cohere, it is unidentified for Claude-generated seeds, and stated as such.*

## METHODOLOGY §2a, concern 6

- **"Each with a posterior score and its weight of evidence, itemised by channel, family and answer"** is version 1's wording. It contradicts the entry's own "Two quantities" bullet and CATALOG §6a. It would read better as "strength and certainty per part, itemised by answer and rater".
- **"232 of the triad era's 300 top rows appeared nowhere"** says neither which ranking defines the 300 nor where the count can be reproduced. The first audit couldn't reproduce it either. A pointer would let the next reader check it.
- **"One standard for evidence"** (Jeffreys per family, the equal-weight family mean, 0.5 and 90%) will be superseded by the catalog's model for every reader once it is built. Concern 6 should say so, or the two standards will coexist with no rule for which wins. BEST already departs from it (precision-weighted, Abbott-corrected; HANDOFF).

## Version 1's findings, against §13

I checked these after drafting the above.

| finding | in version 2 | what remains |
|---|---|---|
| F1, contrast class | separate parts with their own controls | R-chart missing for monotone runs (A1); false-positive rates by chart class (A2) |
| F2, raters | minds in conditions, three categories, residuals listed | conditions partly self-selected and nested in family (A3) |
| F3, generation | measured one-way likelihood; continue null listed | Kneser–Ney against §7 (A5); the selection caveat dropped (A6) |
| F4, triads | an ordering model, no adjacency prior | resolved as far as I can see; O's strength still undefined (A4) |
| F5, run layer | an enumeration rule, containment, untested as a state | "own context" ambiguous under the 8-glyph cap (A7) |
| F6, two quantities | side by side | no single model delivers both (A4) |
| F7, dependence | the §6f table | seed votes not clustered (A8) |
| F8, inputs | §5 | `next`/`between` unassigned, reasoned answers made evidence, `limit` not an outcome (A8) |
| F9, seeds | restored as a rater | see the seed section |
| F10, cycles | METHODOLOGY's definition | no parts; bounded by the caps (A9) |
| F11, tests | rewritten | test 4 can't be run, test 3 passes at ceiling (A10). Test 4 came from F11's own suggestion, which assumed the R-chart control would cover chart walks |
| F12, references | fixed | — |

## Adjacent findings

- **Order questions are asked in the new protocol** [measured]: 1,134 real `order` answers with era `ctx`. METHODOLOGY §5 ("Order answers are not asked in the new protocol yet"), §4a's "Already designed but never run" list, and HANDOFF ("Next to build") still say they aren't.
- **`tree.triad_chains` is defined and called nowhere** [checked: `grep -r triad_chains --include=*.py`]. It was added in commit `75e5694c` with a default `cap=24`. If it is meant as a candidate generator for the catalog, the cap is a cut of the kind §1 warns about.
- **The 8-glyph context cap** (`probe.py` lines 141 and 147, `plan.py` line 91) isn't marked "chosen without evidence", unlike `MAX_RUN` and `MAX_ORDER` beside it.
- **The `../data/seeds/README.md` rule is now out of date.** It says a seed's "written order is never evidence … never enters a statistic". Joseph's later direction (seeds as tagged votes) supersedes it.
- **Gemini is still absent from every new kind of question**, which caps everything above at two families. Of the open decisions in HANDOFF, this is the one that most limits the catalog: A3, and the seed weight.

## What I didn't do

I didn't fit any model, so every claim about how a fitted model would behave is [reasoned]. I didn't verify §1's history bullets or the 232/300 figure. I read the code only where a finding needed it. In A1 and A2, "monotone" and "contiguous" mean strictly monotone in code points and steps of exactly ±1. A run that is contiguous except for one skip counts as monotone, so the contiguous figures are a lower bound on how much of the evidence is near-chart. The A2 figures are pooled over minds within each family; the per-mind rates (A3) vary inside Claude. Treat this report's finding list, not its silence, as its content: I may have missed things in §6e's ordering model and §10's build mechanics, which I read less closely than §4–§7.

## On the brief

The bare brief worked for me. Saying that nothing was built kept me from looking for an implementation, and the one boundary was clear. The coordinator's mid-audit question about seeds was useful rather than disruptive, because it landed after the data that bear on it had already been computed.
