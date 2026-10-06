# De novo audit: the catalog design, version 3 (CATALOG.md; METHODOLOGY §2a concern 6)

*2026-10-06, Claude Opus 5.5, a session that wrote none of the three versions and neither earlier audit. Written for the session that wrote the design and for Joseph, before anything is built. I changed no file but this one and touched no running process. My contact with Postgres was `psql-18 --version` (18.6), and with the processes `pgrep` and `ps`, to see when the loop last started.*

## How I worked, and what this rests on

I read `CATALOG.md` and `METHODOLOGY.md` whole, then `HANDOFF.md`, the two spike findings CATALOG cites (`spikes/reasoned-pass-2026-10-06/FINDINGS.md`, `spikes/whys-basis-2026-10-06/FINDINGS.md`), `../data/seeds/` and `data/unicode/README.md`. I read code where a claim needed it: `port/port_seeds.py`, the `choose` parts of `probe/probe.py`, `priority/plan.py` and `tree/tree.py`, and the adapters in `core/judges.py`. For numbers I read `data/answers/*.jsonl` (259,901 records, rounds through c093, at about 19:15 UTC), `../data/growth/`, `../data/standings/r012.md` and `data/rounds/c094/` in place, read-only, with throwaway scripts in my scratchpad. I fitted no model.

I drafted my own findings before reading the two earlier audits, then used the v2 audit to check §14 (*Version 2's findings*, below).

Labels: **[measured]** counted from the data files; **[checked]** read in code or docs; **[reasoned]** follows from the design as written, not run.

## Summary

Version 3 fixes most of what the v2 audit found, and the reframing that carries it is right. A tier is now defined by *what recognition survives*, not by how much a mind deliberated, and the "chart-congruent, undiscriminated" state is named honestly. One latent-strength model replaces three. A behavioural discriminator (`choose`) exists in code, separate from any stated reason. Most of the design's numbers reproduce (*What I verified*, below).

The open problems now sit almost entirely in **§6c, the step from instruments to tiers**. That step is the design's purpose (§2: Joseph's ranking), and as written it doesn't yet do what §2 says:

1. **The assignment rules contradict the tier definitions and each other** (C1). Rule 2 labels any run without an asked D position "chart-congruent", which would put 1,185 non-monotone runs, half of all runs asked whole, in a tier defined as "the chart and the look agree everywhere". Rule 4 defines "rational" by deliberation, which §2, §7 and METHODOLOGY all rule out. Rules 1 and 3 can both fire, with no precedence. Nothing says how per-position tiers become a run's tier.
2. **D separates the chart from an alternative, not the chart from the look** (C2). At the canary's first D position, the chart's `▉` is itself a felt continuation, the start of the horizontal ladder, and first-impression minds recognise it. At the second, `▀` may be reached by name arithmetic (FIVE EIGHTHS, then HALF), which Joseph ranks with code-point arithmetic. The instruments address the code point; none addresses the name.
3. **Lookalike substitution has no control and little coverage where it's needed** (C3). Recognition is near ceiling, so surviving one substituted glyph says little without a non-lookalike substitution beside it. Among the canary's 15 glyphs, only `█` and `▔` have confusables at all.
4. **The tier order ranks a state of knowledge among properties** (C4). 781 of the 2,430 runs asked whole are contiguous in code points, so they have no interior D position, ever. They stay "undiscriminated", ranked below "rational", including `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`.
5. **Discriminating evidence already in the data goes unused** (C5). In 229 triples, minds agree on a middle that isn't the code-point median. For the canary, `▀ 🮃 🮅` drew `▀` in 10 of its 11 middles, while the first look's picks went 8 to 2 for the chart.
6. **Tests 3 and 4 accept or reject the catalog on how minds perceive** (C6). If minds prefer `▉`, a correct catalog fails test 3. The freeze also has a practical timing problem: the canary's D questions will be asked from round c095 onward, well before a model can be frozen.

The model (C8), the inputs (C9) and the objects (C10) need smaller work, several of them unspecified choices that §13's freeze will force anyway.

---

## C1. The tier rules against the tier definitions

**What the design says.** §2 defines four tiers by what recognition survives. §6c turns instruments into tiers with four numbered rules. §7: deliberation is "never the definition of a tier". §9: each record carries "Tier (§6c) with the instruments that assigned it".

**What follows** [reasoned, with counts measured].

- **Rule 2 mislabels runs the chart never explained.** "A run with no discriminator position and no substitution yet is chart-congruent, undiscriminated." §2 defines that tier as "the chart and the look agree everywhere". Until D is asked, rule 2 puts every run there, including runs whose steps aren't chart steps at all. Of the 2,430 distinct runs asked whole, 1,185 are not monotone in code points, and 1,179 of those have an interior position where the run's next glyph isn't the chart neighbour [measured]. That is what the chart class already says, with no question asked. Rule 2 should read "has no position where chart and run differ" (a fact from the glyphs), not "has no D answer yet" (a state of the asking), and the two need separate names (C4).
- **Rule 4 brings deliberation back as a definition.** "A run recognised with deliberation, not chart-reached, and not discriminated is rational." That contradicts §2's opening sentence, §7, and METHODOLOGY §2a concern 6 ("Never by how much a mind deliberated"). It is also empty or overlapping: a run that is "not discriminated" already falls under rule 2. In practice it would move Grok's recognitions, since Grok always thinks, into "rational" wherever rule 2 didn't take them first. The v2 audit's A3 is still open here.
- **"Rational" has no instrument.** §2's tier 2 is "interpretable with thought, and not reached by chart arithmetic". Nothing in §6c measures "interpretable with thought". The candidates in the design are the reasoned pass's non-chart continuations (`P R T V X Z → B D F …`), part B and a reasoned "none", which §5 and §6a send "at the rational tier". Those attach a tier to a kind of evidence, while §2 attaches tiers to recognitions. One way to make the tier real: rational is recognition at first impression of a run *proposed* only by deliberation (reasoned or generator minds) and not chart-reached. That is a provenance-of-candidate fact the catalog can read from tags.
- **Rules 1 and 3 can both fire, with no precedence.** A link can be chart-reached by `sonnet55r` (rule 3: chart-borne) and still win its D position (rule 1: intuitive). The reasoned-pass FINDINGS settles it one way: a chart-reached link that first-impression minds recognise "has to be checked at a discriminator position … before it counts as intuitive". So D decides, and the marker sets the question. METHODOLOGY §4 says the same of a candidate "recognised when shown, though not produced unprompted". The rules should say that, or that the marker wins, and why.
- **Per position or per run.** Rules 1 and 3 assign a tier "where its recognition holds" and "at those points". §9 gives a record one tier. The canary would be undiscriminated over `▁ … █`, tested at `█ → 🮆`, undiscriminated over `🮆 🮅 🮄`, tested at `🮄 → ▀`, and trivially chart-discordant at `▀ → 🮃` (the chart neighbour of `▀` going down is `╿`). Weakest position, strongest, a profile: each gives a different answer to Joseph's question, and the choice needs to be stated before the freeze.
- **Unassigned continuations at an end are a fact about generation past the run.** Rule 3 makes a run "chart-borne at those points", but no glyph of the run sits at an unassigned continuation. The marker says minds extend this run by arithmetic. It doesn't say the run's own recognition rests on the chart. It fits better as a fact on the record (§9 already lists it) than as a tier rule.

## C2. What a discriminator position discriminates

**What the design says.** §6c, D: at a context, a forced choice between "the chart's next glyph and an alternative"; preferring the run's own glyph means "the look (or meaning) wins over the chart" (§6a).

**What the data show at the canary's two positions** [measured].

- **`▁ … █ → 🮆` against `▉`.** `▉` is LEFT SEVEN EIGHTHS BLOCK, the first step of `█ ▉ ▊ ▋ ▌ ▍ ▎ ▏`, a classic perceptual ladder. The triad era ranked that ladder 58th of its top 300 rows (rank 0.95) [measured, `../data/standings/r012.md`]. First-impression minds recognise `▉` after the ramp: asked "does `▉` come directly after?", `haiku45nt` and `sonnet55` said yes at `▆ ▇ █` (c007), and `haiku45`, `haiku45nt` and `sonnet55` at `▃ ▄ ▅ ▆ ▇ █` (c022); Grok said no both times. The forced picks at `▁ ▂ ▃ ▄ ▅ ▆ ▇ █` (c022) were `▉` ×4 (`grok46g`), `▀` ×5 (`haiku45g`) and `▁` ×5 (`sonnet55g`, wrapping round as a cycle). No mind picked `🮆`. So a preference for `▉` here would be a branch preference between two felt continuations, not evidence that the chart carried the judgement.
- **`🮄 → ▀` against `🮃`.** Here the chart's candidate is a one-step skip (UPPER THREE EIGHTHS after UPPER FIVE EIGHTHS), so D is cleaner. But `▀` is UPPER HALF BLOCK. A mind can get from FIVE EIGHTHS to HALF by arithmetic on names as easily as by the look. Joseph's criterion, quoted in §2, excludes both: *"doesn't need internal arithmetic or thinking about the glyph's name and codepoint"*. The whys spike already has a NAME category (817 of Claude's picks cite it).

**Why it matters** [reasoned]. Unicode allocates lookalike families contiguously, so the chart's neighbour is often a perceptual relative. In step-two runs (`▁ ▃ ▅ ▇`), D's chart candidate is the skipped glyph `▄`, also a felt continuation. A D outcome for the chart then puts a run in "chart-borne" when it is really a branch point. And a D outcome against the chart can put a name-borne run in "intuitive".

**What could make it true.**

- **Qualify each D position by the chart candidate's own standing.** If the chart's glyph is itself recognised at that context (L beyond its control, or picked), the position measures a branch preference. Record it as one, and don't let it assign a tier. The catalog already holds that evidence.
- **A name class beside the chart class.** Unicode names are data the catalog already loads (the manifest has the Unicode version). For each D position, ask whether a name pattern (fraction words, ordinals, ONE … NINE, LEFT/RIGHT/UPPER/LOWER) predicts the run's glyph. Where it does, the position is *name-congruent* and can't establish "intuitive" on its own. This gives Joseph's "name" exclusion an instrument, as the chart class does for code points.
- **A control for D** in METHODOLOGY §4a's sense ("decoy against decoy"): the same pair shown after a context that favours neither, which measures each candidate's standalone pull.

## C3. Lookalike substitution

**What the design says.** §6c: replace one glyph of a monotone run with "a near-identical glyph from another block", taken from Unicode's confusables data. "If recognition survives, the chart wasn't needed."

**Facts** [measured, `data/unicode/confusables-16.0.0.txt`].

- **The canary has almost no coverage.** Of its 15 glyphs, only two have confusables: `█` (`■ ∎`, a black square and an end-of-proof mark, neither of them full height) and `▔` (`‾ ¯ ﹉ …`). `▁ … ▇`, `🮆 🮅 🮄`, `▀`, `🮃` and `🮂` have none. The positions where the canary leaves the chart can't be substituted.
- **The session knows the style limit, but the design doesn't say it yet.** `data/unicode/README.md` (committed two minutes after v3) says confusables "preserve identity, not style", so for styled letters a substitution tests identity rather than look. And its first measurement: 454 of 1,203 monotone runs have a substitutable interior glyph.

**The missing control** [reasoned, from measured rates]. Claude says yes to contiguous runs 0.97 of the time and Grok 0.96. A run with one glyph swapped out is still mostly in order. Without a contrast, "recognition survives the substitution" will mostly mean "R is near ceiling". The design's own principle ("each kind of contrast is its own part") asks for a matched *non-lookalike* substitution at the same position, a glyph from another block of the same broad kind. The instrument's signal is the difference between the two.

## C4. A state of knowledge in a ranking of properties

**What the design says.** §2 ranks tier 1 above 2 above 3 above 4, and calls tier 3 "an honest state, not a verdict". §3: "choosing a ranking key is the read-off's job".

**Facts** [measured]. Of the 2,430 runs asked whole, 781 (32%) are contiguous in code points. Those include `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`, the circled numerals, the dice faces and the moon phases. A contiguous run has no interior position where chart and run differ, so D can never discriminate inside it, and lookalike coverage is thin (C3). Those runs stay in tier 3 for good.

**Why it matters** [reasoned].

- Joseph's quote ranks intuitive sequences above chart-monotone ones he finds "fine". It doesn't rank *undecided* below *rational*. A reader that ranks by tier will put the bottom-up ramp, which is perceptually about as plain as a sequence gets, below a worked-out rational run. That's a judgement nobody has made.
- Tiers are discrete, assigned by rules with implicit cut-offs ("prefer its own glyphs" at what certainty?). The rest of the design, and Joseph's standing preference for soft weights over cuts, keeps quantities continuous and side by side.

**A shape that might hold.** The record could store two things. One is **chart independence**: D, substitution and the triad evidence of C5, each with strength and certainty, and each marked chart-congruent or name-congruent per C2. The other is **discrimination status**: whether any position can discriminate, and which have been asked. Tiers then become a labelled view a reader computes, with §2's ordering as the default view, which is what §3 already says about ranking keys.

## C5. Discriminating evidence already in the data

§6c draws D from `choose` alone, and §6d uses triads and order lines only as order evidence. But a triad whose answered middle isn't the code-point median is a behavioural discriminator, and the ported triad era is the largest body of answers the study has.

**Facts** [measured, triad answers with a middle, both eras]:

- 12,888 middles. In 2,290 (17.8%), the middle given isn't the code-point median of the three. By family: Claude 0.18, Gemini 0.19, Grok 0.16.
- Of the 1,717 triples with at least 3 middles, 229 have a modal middle, given by at least 75% of their answers, that isn't the code-point median.
- **The canary.** For `▀ 🮃 🮅`, the code-point median is `🮃` and the median by height is `▀`. Middles: Gemini `▀` 3 of 3, Grok `▀` 3 of 3, Claude `▀` 4 of 5 (plus 3 "none"). For `▀ █ 🮅`, the code-point median is `█` and the median by height is `🮅`. Middles: `🮅` in 6 of 7. The triad era's grown rows place `▀` between `🮄` and `🮃` from r004 on (`█ 🮆 🮅 🮄 ▀ 🮃 🮂 🮁`).

**Why it matters.** It goes against the "first look" quoted in test 3, which was 8 picks to 2 for `🮃`. More generally, O already carries chart contrast for every triple and line where code-point order and the asked order differ. Folding that into §6c gives the chart-independence part thousands of answers before `choose` has any. C2's caveats apply equally: the middle `▀` may be name-borne.

## C6. The acceptance tests

- **Tests 3 and 4 are claims about minds, not about the catalog** [reasoned]. Test 3 passes if minds prefer `🮆` over `▉` and `▀` over `🮃`. If they don't, a catalog that reports exactly what they answered "fails", and the freeze then leaves no honest move: change the model and break the freeze, or keep it and ship a failed test. The same holds for test 4. `🨀 🨁 🨂` is contiguous, so it has no interior D position, and the honest assignment may well be "undiscriminated", not "chart-borne". As acceptance tests, these would read better procedurally: *the catalog's assignment at these positions follows from the listed answers by the frozen rules, and a hand audit agrees.* Whether the canary is intuitive is then a finding the catalog reports.
- **The freeze and the clock** [measured, checked]. `choose` was committed at 13:00, and its planner puts Joseph's seeds first. Round c094 was planned at 13:03 by the loop's old code (it holds no `choose` questions) and resumed after the 13:05 restart. So c095 is the first round to ask D, and the canary's positions lead it. Their answers will likely be in the ledgers within the hour, long before a model can be frozen. No read-off shows `choose` today (`best.py` and `run.py` don't read it), so the freeze is workable if it is defined as *before anyone queries the canary's D answers*. It would be worth recording that, and the commit at which the model is frozen, explicitly.
- **Test 2's held-out class is a different population.** Chart windows are random contiguous runs (`🥩 🥨 🥧 🥦` is one), while the real contiguous runs were generated. Predicting the windows' yes rate from a model fitted without them tests population transfer as much as rate transfer. A miss would be ambiguous.
- **Test 9** needs "little" stated, and should expect movement where the planner just asked, because asking is outcome-dependent.

## C7. The first look and the provenance in test 3

- **"A single answer per mind" isn't what the data hold** [measured]. The 8 to 2 are ten forced picks in c087 from two generator minds, both Claude: `haiku45g` `🮃` ×5, and `sonnet55g` `🮃` ×3 and `▀` ×2. They are picks (generation, at medium effort, prompted to be creative), not D.
- **The provenance cites only the seed that agrees.** Test 3 gives fable-1's survey seed `🮂 🮃 ▀ 🮄 🮅 🮆 █` as corroboration. The other two survey seeds through these glyphs follow the chart and omit `▀`: sonnet5-1 `🮂 🮃 🮄 🮅 🮆`, grok-1 `🮃 🮄 🮆` [measured, `../data/seeds.jsonl`]. They are also evidence (seed votes, §7). Recording all three, together with C5's triads and C2's picks at `█`, gives Joseph the honest prior picture before D answers arrive.

## C8. The model

**(a) Strength's scale isn't identified** [reasoned]. In $P(\text{yes}_{ri}) = c_r + (1 - c_r)\, s_r\, \theta_i$, only the product $s_r \theta_i$ is determined by the data. Any $k \gt 1$ gives the same likelihood with $s_r k$ and $\theta_i / k$, wherever the bounds allow. So the posterior of $\theta_i$, which §7 calls strength, gets its scale from the priors on $s_r$. Two ways out: anchor $\theta$ by convention (for example $\max_i \theta_i = 1$, or $\theta = 1$ for a stated reference class), or report the identified quantity, the expected excess yes rate $\bar s\, \theta_i$. This matters doubly for the family rule. Each family's $\theta_i$ is "estimated within the family", so families' $\theta$s sit on scales their own priors set, and a weighted mean of them mixes scales.

**(b) The family weights favour the family that cites the chart more** [measured]. Discrimination on R as yes(real) − yes(shuffle), by chart class:

| family | contiguous | monotone | other |
|---|---|---|---|
| Claude | 0.85 | 0.59 | 0.31 |
| Grok | 0.62 | 0.50 | 0.26 |

Weighting by measured discrimination gives Claude the most weight where runs walk the chart, which is exactly where its whys cite the chart twice as often as Grok's (0.38 against 0.18). The v2 audit's A4 flagged this ("shuffle discrimination partly is chart-reading"), and v3 adopts the rule without discussing it. If discrimination is the weight, the place to measure it is where the chart can't help: the "other" class, or D.

**(c) Which control sets $c$, and therefore certainty** [measured]. Certainty is itemised as each answer's log-likelihood ratio, and a "yes" is worth up to $\log(1/c_r)$, which grows fast as $c_r$ gets small. L names two controls, with different rates: near decoys draw yes 0.03 (Claude) and 0.01 (Grok); skip tests draw 0.11 and 0.02. The reasoned-pass FINDINGS adds a third reference: chart-neighbour candidates draw 0.84. So one "yes" to a link can be worth up to about 3.5 nats against near decoys, but only about 2.2 against Claude's skip tests. Which one the model uses decides L's certainty. Reporting certainty per control would keep that visible.

**(d) The certainty's alternative is chosen from the same data.** "$\theta_i$ at its posterior mean" makes the ratio a likelihood-ratio statistic rather than a weight of evidence at a stated alternative. Since the model is frozen first anyway, a fixed alternative (or a Bayes factor with the stated prior on $\theta$) is equally cheap and means what it says.

**(e) D doesn't fit $\theta \in [0, 1]$.** D must be able to show a preference *for* the chart (rules 1 and 3), so it needs a signed scale around 0.5. "Combined as in §7" needs saying for that scale, including what "discrimination" means for D's family weights.

**(f) Choices still open that the freeze will force.** Mallows or Plackett–Luce for O, and a reversal-invariant form of it, since triads are unoriented. How "can't tell" enters the binary model. G's mapping to a probability. The rule from part-level strengths to a tier, or to C4's view. Whether sheet position is a covariate: §3 promises probing "sheet position" findings, and §7 doesn't model it.

## C9. Inputs

- **Joseph's seed is already an answer record** [measured, checked]. `port/port_seeds.py` (commit `6a60b7b6`, two minutes after v3) ports his `joseph-2026-10-06-0` as 18 votes, family `human`, mind `joseph`, both directions. The session's completion `-2` is rightly left as a candidate. §5 ("not yet answer records … a prerequisite") and §12 ("to build") are stale.
- **Which dropspot seeds become votes?** §5 and §12 say "Joseph's and the dropspot seeds". `port_seeds.py` ports Joseph's own sequences only, and says why: the other dropspot entries are "questions to ask, not anyone's perception". The code's rule seems the sounder one. A constructed lattice (`digit-dresses`) is nobody's generation. Whichever it is, the design and the code should agree.
- **Pick nulls aren't mentioned** [measured]. 1,863 answered picks are at random contexts (`tags.null`, `source.why` `pick-null`). §5 and §6a send "picks" to G as link evidence. Nulls should be G's null, never link evidence, and §12's "continue null to build" should note that the pick null exists already.
- **The `muse` family** (glimmer, 257 triad-era triad answers) has no stated treatment, while HANDOFF says glimmer is off the roster.
- **`limit` isn't in the data** [measured]. The 107,972 failed calls carry reason `is_error` (107,667), `timeout`, and so on. None carries `limit`, because the fix came after the void rounds. Excluding them is still right. §5's row describes reasons the records don't have.
- **The reason for asking, in tags, needs METHODOLOGY's consent.** §6e moves "why asked" into `tags` so G can condition on it. METHODOLOGY §2a concern 2 says the tree "knows nothing about why a question was asked … so where a question came from can never become evidence". Conditioning on the design variable is the standard correction for selection, and it isn't evidence. But relabelling the field doesn't change what the catalog knows, and the rule it bends is Joseph's. One sentence in each document would settle it: the reason for asking may enter as a selection covariate, never as evidence.
- **A skip test is a relation, not an answer.** "Inhibit whose candidate is the glyph two steps on in the record's own run": an inhibit record has a context and a candidate, and "two steps on" holds only relative to a run. The same answer is a skip test for `… a b c` and link evidence for `… a c`. That is fine, and arguably right, but it makes L's control rate depend on which runs the catalog has. The design should say so, and say whether one answer may be control and evidence at once.

## C10. Objects

- **"Shown contexts run 2–8 glyphs" isn't true of picks** [measured]. 611 answered picks have contexts of 9–24 glyphs (since the cap fix in §1). They are G evidence at long contexts, outside §8's four states ("up to the 8-glyph cap"). A fifth state, or a sentence on how pick links beyond 8 are held, would close it.
- **"Evidence" has no threshold, and the threshold is a cut** [measured, approximate]. §4's runs and branches need links that "have evidence". Of 16,452 shown contexts with a first continuation (continue and the triad era's `next`), 2,034 have two or more distinct continuations if one answer counts as evidence, and about 95 if two answers each are required. That choice changes the record set by an order of magnitude, and §4 calls the rule "not a cut on score". The threshold should be named as a parameter chosen without evidence, as the study does elsewhere. Also, "keeps the count linear in the candidates" isn't what the rule bounds: maximal runs come from the tree, not the candidates.
- **The branch relation sentence** ("two runs are related as branches when one of them passes through it") reads as if one run suffices. METHODOLOGY §3's version is "both pass through the branch context and continue differently".
- **The 24-glyph cap anchors as well as censors** [measured]. 5,290 continue answers stop at exactly 24 glyphs, against 248 at 23. The censoring rule in §5 is right. The spike also says "up to 24" in the prompt draws walks to the cap, which is a probing finding (concern 1) to pass on.
- **The canary is a cycle in §1 and a run in §13.** Its seed note says "read as a cycle, it returns to empty". How a cycle record and the run records along its period relate (containment? one canonical record?) isn't stated.

## Smaller points

- **Manifest.** Add the Python, numpy and scipy versions (EM results can depend on them), and the confusables and Blocks files, which their README already hashes.
- **METHODOLOGY §2a concern 6 says "The engine. Postgres 18."** CATALOG §11 puts computation in Python, with Postgres storing and serving. "Store" would match.
- **BEST.md's header says "Seed votes are never evidence."** That's legitimate for a read-off with its own criteria, but once the catalog supersedes it (concern 6), the two will say opposite things about seeds. It's worth noting where readers will see both.

## What I verified, and it holds

[measured unless noted] About 260,000 records, about 150,000 real (151,929 not failed); about 107,000 failed calls (107,972; 107,447 in c028–c079). Claude about two thirds of the answers (65%). `between` 1,370. 46 duplicated answer IDs, all triad era. 4,905 distinct grown rows over r004–r012. Coherence yes rates by family and chart class: Claude 0.97 / 0.79 / 0.59, Grok 0.96 / 0.88 / 0.74. Claude's shuffle rates 0.13 / 0.20 / 0.28. Chart windows 0.85 (Claude) and 0.82 (Grok). Whys citing the chart 0.38 against 0.18 (from the spike's REPORT). The fable-1 seed. The r012 standings: 300 rows, all rank ≥ 0.75; 245 of them are neither asked whole nor inside a run asked whole on today's data, consistent with the 232 that also excludes BEST candidates. Claude and Grok adapters save only thinking-token counts, agy saves the text [checked]. Postgres 18.6. `tool-attempt` is 721 today (673 in the design; the data move). The tendril branches' coverage by coherence is roughly flat in their pick share (0.16–0.23 across share bins), which supports §6e's use of them as an approximately unselected set.

## Version 2's findings, against §14

| finding | in version 3 | what remains |
|---|---|---|
| A1, monotone runs | D, substitution, markers, class control, the undiscriminated tier | C2 (what D separates), C3 (control, coverage), C4 (contiguous runs stuck) |
| A2, R ranks chart walks | stated in §6b, rates by class | resolved |
| A3, deliberation as tier | tiers by survival; deliberation a covariate | rule 4 brings it back (C1) |
| A4, one model | the latent-strength model | scale not identified; the discrimination weight, which A4 flagged as chart-reading, adopted without comment (C8) |
| A5, Kneser–Ney | removed | resolved |
| A6, G's selection | unselected sets; reason into tags | the METHODOLOGY rule it bends (C9); tendril coverage checked, flat |
| A7, the 8-glyph cap | four states, censoring | picks beyond 8; "evidence" threshold; "linear" claim (C10) |
| A8, inputs | as listed | `limit` still described as present; seeds now ported; dropspot scope; pick nulls, muse (C9) |
| A9, cycles and branches | parts stated | branch-relation sentence (C10) |
| A10, tests | canary via D, provenance, freeze, transfer, test 5 | tests 3–4 assert perception; freeze timing; selective provenance (C6, C7) |
| A11 | priority, manifest, computation | resolved |

## Adjacent

- **`is_steward` counts the session's completion as Joseph's** [checked, `priority/plan.py`]. It matches "joseph" anywhere in the author string, and the completion's author is "the independent session (Claude Opus 5.5), completing Joseph's …". So the planner serves the session's guess with Joseph's priority, including at D steps. This affects priority only, not evidence, but the retraction's intent was the opposite.
- **The canary's picks at `▁ … █` are themselves a finding worth showing Joseph.** The three generator minds took the three readings: Sonnet a cycle back to `▁`, Haiku the vertical `▀`, Grok the horizontal `▉`. None took his `🮆`.

## What I didn't do

I fitted no model, so C8 is reasoning. I didn't reproduce BEST's candidate set, so the 232 is checked only as consistent. The branch counts in C10 parse the triad era's `next` answers loosely and are approximate. I didn't read `report/best.py` or `tree/tree.py` beyond the parts named. The design's §10 and §11 build mechanics got less attention than §4–§8. Treat this report's finding list, not its silence, as its content.

## On the brief

The bare brief worked for me. "Nothing is built except what the document marks as built" sent me to check that one thing, which is how I found that c094 predates it, and that the freeze will meet the canary's D answers within the hour. One thing I'd have welcomed knowing up front: that the design's author was committing related changes (the seed port, the confusables data) while I read. I found them in `git log` and was glad to. If you have follow-up questions, I'm on the line.
