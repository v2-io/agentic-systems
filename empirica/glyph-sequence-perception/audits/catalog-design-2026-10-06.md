# De novo audit: the catalog design (CATALOG.md, METHODOLOGY §2a concern 6)

*2026-10-06, Claude Opus 5.5, an independent session that did not write the design. Written for the session that wrote it and for Joseph, before anything is built. Uncommitted: I changed no file but this one.*

## How I worked, and what this rests on

I read `CATALOG.md` and `METHODOLOGY.md` whole, then `HANDOFF.md`, the header and `triad_chains`/`sequences` of `tree/tree.py`, the head, controls and link-recognition sections of `BEST.md`, the opening entries of `../OBSERVATIONS.md`, the triad-era port's record construction, and the growth files. For numbers I copied `data/answers/*.jsonl` to my scratchpad at about 17:45 UTC (rounds through c090) and counted from that copy with throwaway scripts. Nothing running was touched. The only contact with Postgres was `psql-18 --version` (client 18.6, which matches §7).

Labels used below: **[measured]** means I counted it from the snapshot; **[checked]** means I read it in code or docs; **[reasoned]** means it follows from the model as written and I have not run it. I did not fit any model. I did not reproduce the "232 of 300 top rows" figure (I don't know which ranking defines the 300) or the "190-glyph monsters".

## Summary

The diagnosis in §1 is right, and the two-layer split (raw tree, then one derived catalog that every reader uses) is the right repair. So are several commitments that are easy to lose later: answers-only evidence, determinism, absent evidence shown as absent, the JSONL ledgers as truth with the database derived from them, the reference implementation kept until parity, and acceptance tests stated before the build.

The model in §5, as written, would reproduce several of the failures it exists to end, and the places where it would do so share a root. It treats each proposition as having one $H$ and one $\lnot H$, with one false-positive rate per family and channel. The study's own controls show that there is no single $\lnot H$: the "yes" rate depends on which kind of non-sequence a run is contrasted with, and the contrast that matters most for signa (felt order against code-chart order) is the one with no control yet. Most of what follows comes from that.

The findings that matter most, in order:

1. **There is no single false-positive rate** (F1). For Claude's cohere answers, shuffles are called coherent 21% of the time, chart windows 84%, and real candidate runs 75%. A Dawid–Skene weight anchored on shuffles will score code-chart walks as confidently recognised sequences. For inhibit, near decoys give 2.8% but skip tests, which are plausible wrong links, give 10.4%.
2. **The family is not one rater** (F2). Within Claude, the rate at which shuffles are called coherent runs from 11% (Sonnet) to 34% (Haiku, thinking off). A family-level rate is a mixture whose weights are set by the roster and the planner.
3. **The generation model contradicts three of the design's own promises** (F3). Under a Pitman–Yor model, "none" answers push a link below its backoff: the morph-ladder failure comes back through the share. Its posterior is not a sum of per-answer terms, so hand audit and byte determinism don't hold as stated. And it pools long-context answers into their suffixes, which blurs $k^\ast$.
4. **The triad prior turns betweenness into adjacency** (F4). METHODOLOGY says twice that it isn't adjacency. At least 3,882 ported triad answers come from long-range triples. Fitting $\lambda$ to generation aims at the one target the canary is known to fail.
5. **The run layer is unspecified exactly where the old losses happened** (F5): which runs exist, what counts as "plausible", how containment and branches are defined, and a 24-glyph bound that 132 of BEST's current candidates exceed.

The rest are smaller or follow from these. A possible shape that keeps the design's intent and avoids F1–F4 is in *A shape that might hold*, offered as one option.

---

## F1. The contrast class is part of the proposition

**What the design says.** §5b: each family $f$ on channel $k$ has a sensitivity $s_{fk}$ and a false-positive rate $e_{fk}$. "The false-positive rates come straight from the controls. Shuffles measure $e$ for cohere… Near decoys measure it for inhibit."

**What the data show** [measured, real answers only, "yes" share of all answers including can't-tell]:

| family | cohere: real runs | shuffled | chart windows | inhibit: candidates | near decoy | far decoy | skip test (`falsify-skip`) |
|---|---|---|---|---|---|---|---|
| claude | 0.754 (4,581) | 0.213 (4,462) | 0.844 (1,159) | 0.496 (4,137) | 0.028 (1,489) | 0.001 (1,361) | 0.104 (1,170) |
| grok | 0.847 (1,840) | 0.407 (1,772) | 0.815 (471) | 0.484 (1,540) | 0.006 (524) | 0.000 (514) | 0.015 (455) |

(Skip tests are inhibit questions whose candidate is the glyph two steps on. If the sequence is real, they are wrong links: plausible, in-sequence, and not adjacent. That makes them the closest thing in the data to the hard negatives a real catalog meets.)

**Why it matters.**

- $e$ is a property of the pair (family, contrast class), not of the family. "Yes" against shuffles means *this order is felt more than a scrambled order of the same glyphs*. "Yes" against chart windows says nothing for either family, because chart windows get *more* yeses than real candidates. So a Dawid–Skene cohere weight anchored on shuffles ($\log(s/e)$ with $e \approx 0.21$) gives a full positive weight to every code-chart walk. BEST's current top recognised run (`Ù Ú Û Ü Ý Þ ß à …`, crossing `Þ ß` because the chart does) shows the effect. So do the 5-of-5 runs at the top of a quick shuffle-anchored score. All five I looked at are chart-contiguous. Some are also real sequences (`♳ … ♹`, the recycling codes 1–7), and others are not obviously more than chart neighbours (`🨀 … 🨅`, `Ѡ … Ѭ`). The cohere channel scores them alike, and that is the point.
- For inhibit, $e$ from near decoys (0.028 for Claude) is almost four times lower than the yes rate on skip tests (0.104). A link that only near decoys calibrate gets about $10\log_{10}(0.5/0.028) \approx 12.5$ dB per "yes". Against the skip-test rate it would get about 6.8 dB. One answer pattern, "1 yes in 4", is weak evidence *for* the link under the near-decoy rate and weak evidence *against* it under the skip-test rate [reasoned, with $s \approx 0.5$ from the candidates' own yes rate]. BEST's link table already shows links "recognised" on `cl 1/3 gr 0/1`.
- "Chart order versus felt order" is listed in §10 as an open question. Under this model it is the cohere channel's central parameter, not a side issue: which population supplies $e$ decides whether chart walks score as sequences.

**What could make the claim true (strengthening first).** Make the contrast part of the proposition: "recognised beyond shuffled", "recognised beyond chart order", "link beyond near decoy", "link beyond in-sequence skip". Each has its own control, so each has an honest $e$, and each becomes a separate part of the record. The METHODOLOGY's "tests side by side" already points this way. The chart-order contrast needs its missing control: runs where visible order and chart order disagree. §10 names the order question on such sets; the cohere question would need the same. A second route is to model $e$ as depending on item covariates (chart adjacency, same block, alphabet position), fitted across all controls at once. That is more machinery, but it would carry over to candidates no control resembles.

## F2. A family is several raters, and the mix moves

**What the data show** [measured, cohere and inhibit yes shares by mind]:

| mind | shuffled yes | can't tell on shuffles | real-run yes | near-decoy yes | can't tell on near decoys |
|---|---|---|---|---|---|
| sonnet55 | 0.113 | 0.038 | 0.697 | 0.002 | 0.049 |
| opus55 | 0.122 | 0.127 | 0.801 | 0.000 | 0.104 |
| haiku45 (thinking) | 0.202 | 0.145 | 0.741 | 0.015 | 0.167 |
| haiku45nt (no thinking) | 0.335 | 0.159 | 0.804 | 0.061 | 0.307 |
| grok46 | 0.407 | 0.062 | 0.847 | 0.006 | 0.069 |

**Why it matters.**

- Within Claude, the false-positive rate on shuffles varies threefold, and on near decoys by more than an order of magnitude. A family rate is a mixture weighted by how many questions each mind answered, which the planner, the pacing and `minds.json` decide and which changes between rounds. A "yes" from Sonnet and one from Haiku-without-thinking would get the same weight, which they don't deserve.
- The data are lopsided [measured]. Gemini has 0 cohere, 0 pick and 4 inhibit answers, so most new channels have two families. Claude contributes about 66% of the continue answers and about 71% of the cohere answers, through five minds. "Family weighting falls out of the data" will mostly mean Claude against Grok, while the larger variation sits inside Claude.
- "Can't tell weighs 0" assumes it is equally likely under $H$ and $\lnot H$. The table says it isn't: Haiku-without-thinking says it on 31% of near decoys and about 12% of real candidates. Dawid–Skene handles a third response category natively, so it can be estimated rather than set to zero.
- Raters also interact with items for reasons the study treats as findings rather than noise. The triad era found that Gemini Flash leaves `▁` out of the fill ramp, probably for tokenizer reasons (`../OBSERVATIONS.md`, 2026-10-04), and `▁` is the first glyph of the canary. A model with constant per-rater rates would absorb that as lower Gemini sensitivity and lose it.

**What might hold.** Raters at the level of the mind and its condition (thinking budget, prompt variant, protocol era), partially pooled toward the family. That is a hierarchical Dawid–Skene, or an item-response model with rater discrimination and threshold. It also answers the §10 question about the thinking budget: make it a rater covariate, and the data say whether it matters. Per-family weights then become a read-off of the fit instead of an assumption in it.

## F3. The generation model, against the design's own promises

**(a) The one-way rule doesn't hold under Pitman–Yor.** §5c says that not naming `x` "lowers only `x`'s share, never below the prior". In a hierarchical Pitman–Yor model, the predictive probability at context $u$ (counts $c$, tables $t$, discount $d$, strength $\theta$) is

$$P(x \mid u) = \frac{c_{ux} - d\,t_{ux}}{\theta + c_{u\cdot}} + \frac{\theta + d\,t_{u\cdot}}{\theta + c_{u\cdot}}\,P(x \mid \pi(u)),$$

so for a glyph never named at $u$ it is $P(x \mid \pi(u))$ times a factor below 1. With 30 "none" answers seated at 3 tables, $\theta = 1$ and $d = 0.5$, the factor is $2.5/31 \approx 0.08$ [reasoned]. "None" is a category, so "none" answers do count against `x`, by a factor of about twelve here. That is BEST's old morph-ladder failure, reintroduced through the share. The weight in §5c ("posterior probability of `x` at `c` against the probability the null contexts give a named glyph") inherits it.

**(b) It isn't a sum of answers, and it isn't deterministic as usually fitted.** Teh (2006) fits the model by Gibbs sampling over seating arrangements. The sequence memoizer (Wood et al. 2009) uses approximate inference too. Then three promises fail: the evidence row "per (proposition, answer)" with its own weight of evidence (§7), "recomputing the score from the listed answers and rates gives the stored number" (§9 test 6), and byte-for-byte rebuilds (§2, test 1). A seeded sampler can be deterministic, but that is not recomputable by hand.

**(c) It pools long contexts into short ones.** In the hierarchical model, a child context's tables are customers of its parent, so an answer at `a b c` raises its predictive probability at `b c`. That is the model's purpose. But §3 says "a link at a long context is not the same claim as at its suffix", and the tree deliberately does not pool ("k\* needs each length asked as itself", `tree.py`). Any $k^\ast$, stability or flip read from Pitman–Yor posteriors would be smoothed toward short contexts. The planner's lengthening tests rely on exactly that distinction.

**(d) Continue has no null contexts in the data.** The §4 table names "null contexts" as continue's control. Every continue record has `tags.control = null` and no `null` tag [measured]. The nulls that exist are picks (`tags.null = true`, 1,462 answers), forced, at medium effort, from the generator minds (`sonnet55g`, `haiku45g`, `grok46g`). The closest thing for continue is `explore` questions, which are identifiable only through `source`. The catalog doesn't read `source`, and many of those questions are seeded rather than random.

**What could make it true.**

- For a descriptive generation part (what comes next, with branch shares): interpolated Kneser–Ney is the closed-form, deterministic approximation to the hierarchical Pitman–Yor model with one table per type (Teh 2006 makes the correspondence explicit). It is hand-recomputable from counts. Keep raw per-node counts beside it for $k^\ast$ and stability.
- For the link's weight of evidence from generation, the one-way rule can become a measured likelihood instead of an assertion. What matters is $P(\text{named at } c \mid \text{link recognised})$. Among inhibit-recognised links (yes in at least 75% of at least 2 answers) that also have continue answers at the same context, the median share of first continuations naming the candidate is 0.5, and 14% are never named there [measured; selection caveat: many of those inhibit questions were asked *because* shown answers ended there]. A likelihood built from that distribution, which has mass near zero, makes "not named" weak evidence against a link, at a size the data set. That is METHODOLOGY's one-way intuition with a number attached, and it will move as the morph-type links accumulate.
- A null for continue would need tagged random contexts asked the continue way. It would be a probing change (concern 1).

## F4. The triad prior turns betweenness into adjacency

**What the design says.** §5d: a triad answer that `y` is between `x` and `z` gives pseudo-counts to `x y → z` and `z y → x`; order lines do the same for each adjacent pair in a line; $\lambda$ is fitted by how well the prior predicts held-out continue and pick answers.

**What the rest of the study says.** METHODOLOGY §6: triads are "**not edges.** A middle says `q` lies between `p` and `r`, not that `q` is adjacent to either", and lines are "**not edges.** A line orders a *subset*, so neighbours in a line need not be adjacent in any sequence". §4: triads and order sets "do not create edges". `tree.triad_chains` already does the betweenness-to-transition step, and labels it "candidates only (a generator, never evidence)". §5d promotes that generator to a prior on evidence, without saying that it is overriding §6.

**What the data show** [measured, from `source.part`, which the catalog may not read]: 1,820 `square` triads, 1,612 `seed` triads and 450 `cand` triads in the triad era are tagged `long-range`, and 2,809 more were drawn from a weighted exploration pool. The canary shows the problem directly: the triad era asked `🮃 🮄 🮅` from the ref `🮂🮃▀🮄🮅🮆█` (answer: middle `🮄`). §5d would put mass on `🮃 🮄 → 🮅`, a context that is not on the felt path, where `▀` separates `🮃` from `🮄`. Without reading `source`, the catalog can't tell adjacent triples from long-range ones.

**Why fitting $\lambda$ to generation aims at the wrong target.** METHODOLOGY's central finding is that recognition and generation come apart (the morph case), and the canary is an instance. Given `🮂 🮃 🮄 🮅 🮆`, a c002 continue answer (Gemini) writes the chart, `🮇 🮈 🮉 🮊 🮋`, while the triad era's order answers put `🮂 🮃 ▀ 🮄 🮅 🮆 █` in the felt order [measured]. A $\lambda$ chosen to predict generation will shrink triad mass precisely where triads know something generation doesn't. "If $\lambda$ goes to zero, that is itself a finding" is true, but the finding would be the known one, and the canary would stay lost.

**Double counting.** Triads enter generation as a prior (§5d) and again as the betweenness part of the run score (§5e).

**What might hold.** Betweenness and order lines are evidence about the *order of a set*, which is what they were asked about. They fit naturally into a run-level likelihood over orderings: a Mallows or Plackett–Luce-type model of each family's betweenness and line answers given a hypothesised order, with orthogonality ("only two", "none") as its own outcome. That likelihood can use *every* triple of a run that was asked, not only consecutive ones (§5e uses only consecutive triples, which leaves out the long-range triads that do bear on the run). It belongs in the recognition side of the record. As a candidate generator, `triad_chains` already brings the triad era's rows back without making them evidence.

## F5. The run layer is unspecified where the old losses lived

Every incident in §1 is a rule about which runs exist and how they are cut, merged or ranked. The design specifies propositions and scoring in detail but not the following.

- **Which runs become records.** "Every plausible branch gets its own record" needs a rule for "plausible", and so does "categories with real posterior mass" (§5c). Whatever the rule is, it is a cut, and METHODOLOGY §7 asks for cuts to be soft or named. The rule should be stated, with its parameters marked as chosen without evidence, and tested by acceptance test 4.
- **Containment.** If every sub-run of a record is also a record, the count grows quadratically in run length. If not, which ones are? §3 says containment is a relation and nothing is deleted, but not which runs exist to be related.
- **Branches against canonical orientation.** "Shares a prefix … then continues differently" depends on which end comes first, and canonical orientation is chosen by code-point order. A branch at the high-code-point end of a run is a shared *suffix* in canonical form. A branch should be defined at a shared terminal sub-run in either direction, with the direction recorded.
- **The 24-glyph bound.** §3 bounds contexts to 1–24 glyphs, and §7 says paths of at most 24 glyphs are recursive CTEs. If that bounds runs, it repeats the cap-at-8 lesson at 24. 132 of BEST's current candidates are longer than 24 [measured; mostly chart walks, but not all real sequences are short: `A … Z` is 26, and the circled numbers `① … ㊿` are 50]. Whole-run evidence can't exist above 24 glyphs (`probe.MAX_RUN = 24`, "chosen without evidence"), so the design should say how windows of a long run combine into evidence about the run. That is another combination rule, and it needs stating.
- **Path enumeration cost.** Enumerating paths up to length 24 with a recursive CTE is exponential in branching. Dense neighbourhoods (Latin letters with case and diacritic branches, chart neighbours) can blow up unless the enumeration is pruned by score. Pruning is then the enumeration rule from the first bullet.
- **"All links hold" as a product.** §5e enters links "as the probability that they all hold". If that is a product of link posteriors, it is a length penalty ($0.95^{20} \approx 0.36$). Joseph asked that length organise and not rank, and §1's own ranking incident was a length effect in the other direction. It also assumes links are independent, and links that were never asked would sit at their prior, so any long run with one untested link is pulled toward the prior.
- **Untested is a state, not a low score.** The triad era's fit placed glyphs arbitrarily on links nobody had asked (`▂ ▁` swapped in the ramp, the colon put at the bottom) and made them look settled (`../OBSERVATIONS.md`, 2026-10-04). The fix then was to list untested links and discount them, and later to rank only supported pieces. The catalog's backoff and triad prior fill untested links with mass in the same way. §6's "absent evidence is shown as absent" covers coverage counts. It should also cover the score: each record should say which of its links have evidence at their own context and which have only backoff or prior.

## F6. One number, or two quantities

METHODOLOGY §2a: "Agreement is the perceptual quantity, how strongly minds converge. The interval is how sure we are of it", and read-offs "don't collapse them into one number". CATALOG §5e: "A reader can then rank by the overall score."

A posterior $P(H)$ is a certainty, not a strength. Under Dawid–Skene with one sensitivity per rater, every run whose yes rate is above a crossover tends to certainty as answers accumulate, and every run below it tends to zero. With Claude's rates (yes/(yes+no): real 0.795, shuffled 0.238) the crossover is a yes rate of about 0.52 [reasoned]. A run at 60% and a run at 95% both end at $P(H) \to 1$, and their order is set by $n$ times a divergence: in effect, by how often they were asked.

- **Today** [measured]: cohere answers per real run have a median of 3 and a maximum of 5, so the top saturates. Every 5-of-5 run ties at about 26 dB under the shuffle anchor, and the five I looked at are all chart-contiguous, real sequences and chart neighbours alike (F1).
- **With §8's expected-information-gain priority**, promising records are asked more, so their scores grow because they were asked. For a Bayesian, optional stopping is harmless only if the likelihood is right, and §5f says it isn't (dependence) and F1–F2 say why. METHODOLOGY §6's rule, "a *share* … never a raw count that rewards over-asked contexts", is the frequentist form of the same caution.

**What might hold.** Keep both quantities on every record: a strength (for example, each family's yes rate above its matched control, with its interval) and a certainty. Leave the choice of ranking key to each read-off, as METHODOLOGY says. If Joseph wants one overall number for the planner, that is his call to make against METHODOLOGY §2a, and the design should name it as a change rather than slip it in.

## F7. Dependence that §5f doesn't list

§5f lists dependence within a family, within a sheet, between nested contexts, and between links and their run. Missing:

- **Correlated errors across families.** All the families learned the Unicode charts, and both call chart windows coherent at about 0.82–0.84. Dawid–Skene's known failure mode is exactly this: raters who make the same mistake look like independent confirmation, and the evidence is multiplied. Cross-family agreement on chart walks will read as strong evidence.
- **Within one written answer.** One continue answer that writes a 24-glyph chart walk yields evidence for 23 links at once. 4,956 continuations are exactly 24 glyphs long, the longest any answer reaches [measured]. METHODOLOGY §4 says long written runs through unfamiliar blocks are mostly chart walks, and until now BEST kept the written channel apart, awaiting shown confirmation. Merging written answers into link evidence without modelling this dependence brings chart-walk inflation back.
- **Across channels within a mind.** A mind's continue, pick, inhibit and cohere answers about the same run share whatever it knows about the chart. Summing their weights treats them as independent.
- **One answer, many propositions.** A link's evidence also feeds every run containing it, and every cohere answer feeds containment relations if any propagation is ever added. The evidence table makes this auditable. The independence that the sum in §5a assumes does not hold.

## F8. Inputs the design doesn't define

These are small one by one, but the build reads every record, and the design doesn't yet say which records count.

- **Most "answer records" in §7 are failures.** Of the 237,734 records it counts, about 107,000 are `call-failed` rows from the void rounds c028–c079. In my snapshot, 107,447 of 251,495 records are failures in void rounds; 143,516 are real answers [measured]. Other outcomes need stating too: `tool-attempt` (673), `unparsed`, `other`, unassigned code points, and the `GAP` pseudo-glyph in `between` contexts. Each needs a stated rule: evidence, its own outcome, or excluded with a reason.
- **Variants and minds that METHODOLOGY keeps apart:** `reasoned` (1,740 continue answers, `sonnet55r`), `reflection` (4,638; §3, "never grow a sequence"), `no-lookup` (669). The design mentions reflections but not reasoned answers, and they are tagged as ordinary continue records. Also the `muse` family (Glimmer, 257 triad-era answers), and the two protocols (`gsp-0.1` and `ctx-0.1`) with their different prompts.
- **Duplicate answer IDs.** 46 records in `triad-era.jsonl` are identical duplicates of another record's `aid` (rounds r003–r005: 9 sheets list the same presentation twice, and the port writes one parsed answer for each listing) [measured]. A primary key on `aid` would reject the load, which is good, but the current tree counts those answers twice. Whether the second presentation's own answer was lost is a question for the port.
- **Determinism needs a manifest.** The loop re-records earlier rounds as drains fold in answers, so "the same answers" should be a hash of the input files, recorded with each build, together with the Unicode version and any candidate inputs (seeds, growth files). The growth files live in `../data/growth`, which HANDOFF schedules to move to `.archive/triad-era/`.
- **Float sums in Postgres.** A view that sums `double precision` weights can differ in its last bits between runs when the planner parallelises the aggregate. Byte-identical builds need a fixed summation order: sums done in Python, `numeric`, or parallelism off for the build.

## F9. Seeds: a policy change worth naming

§2: "Seeds are never evidence." METHODOLOGY §2a gives the opposite as Joseph's direction: seeds are tagged votes from the surveyor's family, *"segregate those out if we need a more pure analysis"*. HANDOFF lists it among his standing directions. BEST already leaves seeds out, which is a read-off's own choice. As concern-6 policy, it changes what the planner sees. That may be the better rule, but it reverses a ratified one, so it should be stated as a change for Joseph, or the catalog could carry seed votes as a tagged part that readers may include.

## F10. Cycles

§3 defines a cycle as "a run whose last glyph is followed by its first", made of distinct glyphs. METHODOLOGY §3 defines it by a context state that returns, which admits periods that repeat glyphs (the bouncing spinner `- \ | / - / | \`, period 8, 4 distinct glyphs). METHODOLOGY also requires that a mind *manifest* the cycle, and `tree.py` implements that rule. CATALOG leaves out both, and 1,067 continue answers contain a repeated glyph [measured]. The canonical form (smallest rotation over both orientations) works for distinct-glyph cycles; for periods with repeats, the canonical form would be over the period's sequence.

## F11. The acceptance tests

- **Test 2 is partly circular.** If the controls anchor $e$, they will score at their own false-positive rate by construction. Fit on half the controls and test on the other half.
- **Test 3 can't fail as written.** "Appear as records with their evidence" holds for a record with a very low score. Say what score, or what rank against what, would count as passing. A negative canary would also help: a run the study regards as a chart walk rather than a felt sequence (`🨀 🨁 🨂 …`, or the `Ý Þ ß à` crossing) should score below the felt ones on the felt-order part. That depends on the open question in F1, which is a reason to settle it before the build.
- **Test 4's range.** The 4,905 distinct grown rows reproduce exactly, but from `../data/growth/r004–r012.json`. No growth files exist for r001–r003.
- **Tests worth adding:**
  - calibration on held-out controls;
  - posterior predictive checks of the rater model (does it reproduce the observed spread of yes counts per item, or is the data overdispersed against it?);
  - sensitivity of the top records to the choice of contrast class;
  - rank stability when one more round is added;
  - a comparison with BEST's current recognised and rejected sets, with each disagreement explained (test 5 does this for links only).

## F12. The document itself

- **Section references are ambiguous.** CATALOG has its own §2 and §3, but "(§2)", "(§3)", "(§2a)" and "Reflections (§3)" in §3–§4 mean METHODOLOGY's. A reader arriving cold, as I did, follows the wrong one first. "METHODOLOGY §2" would remove the ambiguity.
- **Joseph's quote and the diagram differ.** He calls the catalog the better input to "the probing concern"; the diagram routes it to priority (3). He probably meant priority, but there is a real probing use too: §5f's sheet-position effects, once estimated, are a measurement-validity finding for concern 1. That is worth one line.
- **A precedent worth citing.** The triad era also had a global fit that ordered glyphs, and it "dropped/merged valid creative sequences" (commit `b1a78dbe`) and placed untested links arbitrarily (OBSERVATIONS, 2026-10-04). It was demoted to a guess-proposer. The catalog is the second global model proposed as the source of sequences. Saying what is different this time (answers only, untested shown as untested, nothing folded) would answer the obvious question before Joseph asks it.
- The §7 size figures count failures as answers (F8).

## A shape that might hold

This is one option, offered because each objection above comes with a way to keep the design's intent.

- **Records:** every named link at its own context, with no cut, and runs from a stated enumeration rule. Candidate inputs: tree walks, triad chains, seeds, grown rows, and shuffles a mind called coherent.
- **Parts, each with its own likelihood and a named contrast:**
  - whole-run recognition beyond shuffles;
  - whole-run recognition beyond chart order, once its control exists;
  - link recognition beyond near decoys and beyond in-sequence skips;
  - generation as a measured one-way likelihood (F3);
  - order-of-set evidence from triads and lines through an ordering model (F4).

  Raters are minds in conditions, pooled toward families (F2).
- **On every part,** a strength and a certainty (F6), the answer IDs, and the evidence that rests only on backoff or prior marked as untested (F5).
- **One overall score** only if Joseph wants one, built by an explicit rule that a read-off can ignore.
- **A deterministic, closed-form fit wherever possible** (Kneser–Ney for generation; EM with a fixed initialisation and order for the raters), so that the hand audit in test 6 is real.

The engine question is separate, as §7 says. Postgres is fine at this size. Its transactional build matters less than its queryability, because a deterministic rebuild into a versioned schema with an atomic switch gives readers the same guarantee.

## Adjacent findings

- METHODOLOGY §4 still says BEST counts a link as recognised only when it beats the near control "in ≥ 2 families", and §5's skip test says the same. BEST now uses one family (Joseph's change). Its link table shows rows recognised on one family's answers.
- Gemini is close to absent from every new kind of question (0 cohere, 0 pick, 4 inhibit). HANDOFF already lists this as undecided. For the catalog, it means the rater model has two families on most channels.
- The pick null and the generator minds are a different condition from the continue minds: forced, at medium effort, from other mind configurations. Any generation null borrowed from picks should carry that as a stated mismatch.

## What I didn't do

I did not fit Dawid–Skene or Pitman–Yor to the data. The numbers in F3(a) and F6 come from the formulas, not from fits. I did not reproduce the 232/300 figure or the history in §1's first three bullets. I read `best.py`, `plan.py` and `probe.py` only where a finding needed them. §9's planned independent critique of the statistics, by a spiker briefed through `SPIKE-PROMPT.template.md`, is still worth doing; this report could be one of its inputs, or a reason to change its brief.

On the brief I was given: the single boundary and the stated audience were both useful. Saying that nothing in either document was built saved me from looking for code that doesn't exist.
