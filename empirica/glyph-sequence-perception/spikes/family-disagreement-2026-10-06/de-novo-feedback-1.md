# De novo feedback 1: the family-disagreement spike

*2026-10-06, an independent session (Claude Opus 5.5), asked by Joseph for a critical and adversarial pass. I read the spike's six documents and all 23 scripts, then METHODOLOGY, the SEAL file and `catalog/build.py`'s loader. I re-ran every script on the spike's own snapshot (`fd-snapshot.pkl`, taken 16:36, 184,459 answers kept), and then ran my own analyses on the same snapshot through the spike's `lib.py`, so every count below drops sealed answers before anything else. Labels: **[reproduced]** a number of the spike's, recomputed; **[re-derived]** my own computation; **[inference]** reasoning from those. My scripts live in the session scratchpad (`scratchpad/audit/my/`), which is not durable. Appendix A says exactly what each one changes, so they can be rebuilt.*

## Summary

Every number in FINDINGS and NOTES that comes from a committed script reproduces exactly. The problems are in what the numbers are taken to show. I found four that change a headline, and several smaller ones.

1. **The threshold model's "accounts for every flat split" result is not robust.** It depends on where an arbitrary prior on item strength is anchored. With the prior's centre and spread estimated from the data instead, continue flat splits exceed the model in three of six pair-directions and fall short in two. The model also over-predicts plain single-answer disagreement by about a factor of two for every pair, so it is miscalibrated, whichever way a flat-split count comes out. The spike's own `additive1.py` was written to catch this. Its output isn't reported anywhere.
2. **"Content agreement 93–99%" is mostly agreement on the code chart.** 77% of Sonnet–Grok both-commit pairs are both the context's code-point successor, which agree by construction. Off the chart, agreement is 0.82–0.93 on continue and 0.82–0.95 on triads whose middle the code point doesn't decide. The finding survives, with smaller numbers, and with the reading "they agree on the sequence" narrowed to "they agree where they leave the chart, too".
3. **"The tilt is Sonnet's rather than Claude's" is not supported.** Paired by candidate pair, Haiku without thinking moves toward the chart as much as Sonnet (+0.107 against +0.106). The Opus result it rests on comes from 9 paired pairs, with SE 0.26. Read correctly, the `choose` data pick out the same two Claude minds that carry the large contiguity offsets in whole-run recognition. That convergence *strengthens* a Claude-core-minds reading the spike set aside.
4. **The withdrawal in Finding 5 withdraws something Finding 3 still asserts.** The logit analysis does not dissolve Sonnet's dependence on chart class (observed against threshold-predicted: contiguous 0.975 against 0.788, "other" 0.473 against 0.585). It re-expresses it. "Abbott misattributes strictness to chart class" is a true property of the two parameterizations. The data were never asked which one fits, yet integration-plan item 2 rests on the answer.

Smaller: the `▁` scan's z-scale is overdispersed, so Gemini Pro's z = -3.9 is not distinguished by the scan itself (§5). The "Sonnet–Opus D ≈ 0" evidence is uninformative, because on the same items Sonnet–Grok is also about 0 (§6). Gemini's comparisons are selected toward familiar glyphs by dropping tool attempts (§7). A familiarity effect survives inside the withdrawn Grok reading (§8). There are several wording overreaches (§9) and a reproducibility gap (§10). The seal held (§11).

What stands, re-derived: content agreement between frontier minds is high even off the chart. Commitment thresholds differ by mind and question kind, and in ways that don't line up by family: Haiku against Sonnet and Opus within Claude, Flash against Pro within Gemini. Flash's `▁` avoidance is the strongest glyph-specific effect in the triads, by far. Sonnet chooses the chart's glyph more than Grok and Gemini Flash at matched `choose` positions. Thresholds by mind are real. Only the strong claim that they are the *whole* story of flat disagreement is in doubt.

## 1. The threshold model: the test of fit depends on an arbitrary anchor

**What FINDINGS says.** "That model predicts every flat Sonnet-continues / Grok-stops split: 43 observed, 51 predicted (95% band 38–65)." NOTES: "The additive threshold model accounts for all flat commit splits on continue."

**Reproduced.** The same `rasch.py` run prints the reverse direction too. Sonnet stops while Grok continues: observed 2, predicted 10.4, band 5–17. Sonnet against Haiku without thinking, reverse: 3 against 9.7, band 5–16. **Both reverse counts fall outside the model's own 95% band.** FINDINGS doesn't report them, and NOTES' "accounts for all" contradicts them.

**Why the forward match is weak evidence [re-derived].** `rasch.py` and `additive.py` estimate each item's strength $\beta_i$ with a fixed $N(0, 4)$ prior. After every iteration they also re-centre every $\alpha_m$ so that Sonnet's is exactly 0, and they don't shift $\beta$ to match. The prior therefore pulls thinly answered items toward Sonnet's 50% point. Most items rest on one or two other answers (for Sonnet–Grok, 14,591 of 17,281 items have one or two), so the prior dominates. The effect is easy to see:

- `additive1.py`, the spike's own relative test, which I ran: observed single-answer disagreement is 0.37–0.80 of predicted for **every** pair. Sonnet–Grok is 0.53, Sonnet–Opus 0.37, Flash–Pro 0.54. The model predicts about twice the disagreement there is.
- Fitting the same model with the prior's centre and spread estimated from the data (empirical Bayes: $\beta_i \sim N(\mu, \tau^2)$, $\mu$ and $\tau$ fitted; Appendix A) changes the flat-split verdicts on continue:

| pair (A, B) | A continues, B stops: obs / pred [95%] | A stops, B continues: obs / pred [95%] |
|---|---|---|
| Sonnet, Grok | 43 / 33.3 [22–44] | 2 / 8.2 [3–14] |
| Sonnet, Haiku-nt | **65 / 49.0 [35–61]** | 3 / 7.8 [3–13] |
| Haiku-nt, Grok | **38 / 19.5 [12–29]** | **42 / 30.4 [20–41]** |

The single-answer ratio stays at 0.35–0.75 under this fit too. So the problem isn't only the anchor. A one-dimensional logistic model, with $\beta$ estimated from one or two other answers, doesn't describe these items, which are mostly near-certain continue or near-certain stop. Neither a "pass" nor a "fail" on flat-split counts means much until that is fixed.

**What survives [inference].** The per-mind stop rates do differ: `threshold.py` shows Grok above Sonnet in every determinacy bin, and that's model-free. What doesn't survive is "a flat split is a context sitting between two thresholds: settled, not unclear" as a general reading. That's the reading the debrief gives Joseph ("asking again won't settle anything") and that plan items 1–2 build on.

**Strengthening attempt worth making, not made here.** The claim may be recoverable. A model whose items can be near-deterministic would be a fair test: a mixture of "everyone continues", "everyone stops" and a logistic middle, or a 2PL with a per-mind slope, fitted on items with enough answers. Calibrate it first on single-answer disagreement (ratio near 1). Only then count flat splits. If it then accounts for them in both directions, the threshold reading is earned.

## 2. Content agreement is mostly chart agreement; the finding survives, smaller

**Re-derived, continue, both minds commit:**

| pair | all | both wrote the chart's next | neither did | non-contiguous context |
|---|---|---|---|---|
| Sonnet–Grok | 0.940 (n=10,858) | 1.000 (n=8,324) | 0.883 (n=2,129) | 0.875 |
| Sonnet–Opus | 0.957 (3,258) | 1.000 (2,569) | 0.888 (617) | 0.875 |
| Opus–Grok | 0.954 (2,405) | 1.000 (1,851) | 0.933 (475) | 0.911 |
| Sonnet–Gemini Flash | 0.928 (1,911) | 1.000 (1,408) | 0.822 (444) | 0.831 |
| Grok–Gemini Flash | 0.944 (1,826) | 1.000 (1,342) | 0.882 (432) | 0.883 |

Three-quarters of the "content agreement" is two minds both walking the code chart. METHODOLOGY §1 says a chart walk is not thereby a sequence, so that part is agreement about Unicode's allocation, not about the sequence. Off the chart, agreement is still high and still shows no family affinity. On contexts all three of Sonnet, Opus and Grok continued, non-contiguous only (n = 517): Sonnet–Opus 0.905, Sonnet–Grok 0.882, Opus–Grok 0.928.

**Triads, re-derived:** agreement on the middle when both commit, by triple class (Sonnet–Grok; the other frontier pairs are similar):
- contiguous: 0.98;
- gaps of 2–4: 0.93;
- gaps of 5 or more: 0.91, with both naming the code-point median only 0.51 of the time;
- triples spanning several blocks: 0.82, both on the median 0.43.

The middle that minds agree on is not just the median. This half of Finding 1 is stronger than FINDINGS shows, because it holds where the chart can't explain it.

**Suggested restatement.** "Where two frontier minds both continue, they write the same glyph 0.94–0.99 of the time. Most of that is the shared code-chart successor; where neither writes it, 0.82–0.93. Triad middles agree 0.82–0.95 even where the code-point median doesn't decide." Also, "92–97%" for triads silently leaves out the Haiku-with-thinking pairs (0.877–0.899). Continue named its Haiku exception; triads should too.

## 3. The chart test (`choose`): the tilt is not shown to be Sonnet's alone

**Reproduced.** Sonnet 0.536 against Grok 0.470 on 446 paired positions. My paired SE is 0.022, z = 3.0, so "about three standard errors" is right. Not reported: **Sonnet against Gemini Flash, +0.120, z = 4.7** (308 positions). Haiku without thinking sits between them (+0.042 against Sonnet, z = 1.6; +0.025 against Grok, z = 1.0).

**Controls.** FINDINGS says "Against its own controls, context moves Sonnet toward the chart; Grok, Gemini Flash and Opus move away." It leaves out Haiku without thinking, which has the second-largest sample: unpaired, real 0.492 against control 0.438. I paired real answers with neutral-context controls on the same candidate pair and chart:

| mind | paired pairs | real minus control | SE |
|---|---|---|---|
| Sonnet | 137 | +0.106 | 0.061 |
| Haiku without thinking | 135 | +0.107 | 0.060 |
| Grok | 137 | -0.044 | 0.054 |
| Gemini Flash | 76 | -0.099 | 0.084 |
| Opus | **9** | -0.111 | 0.261 |

So "the tilt is Sonnet's rather than Claude's" rests on Opus, and the Opus control comparison carries almost no information. No mind's shift is individually beyond 2 SE. The unpaired rates are also confounded by position bias, which is strong:
- Haiku without thinking picks the first option only 0.26 of the time on controls, against 0.59 on real positions;
- Opus's 30 controls have the chart shown first 0.60 of the time, and Opus picks the first option 0.77 of the time.

The pairing above removes most of this. A position-balanced estimate per mind would remove the rest.

**What this gives instead [inference].** The minds that tilt toward the chart in `choose` are Sonnet and Haiku without thinking. Those are the same two minds with the largest contiguity offsets in whole-run recognition (Sonnet +3.1, Haiku without thinking +2.3; Opus +1.7 on a quarter of the data). Two independent instruments name the same minds. That deserves a sentence in FINDINGS, and it argues against demoting the effect to "Sonnet's".

## 4. Finding 5 and the withdrawal: one deviation, two descriptions, and no model comparison

**Reproduced from `cohere_logit.py`:** the per-mind threshold reproduces Grok's, Flash's and Haiku-without-thinking's class pattern to about 0.03, but not Sonnet's:
- contiguous runs: 0.975 observed against 0.788 predicted;
- monotone: 0.735 against 0.701;
- other: 0.473 against 0.585.

Under the logit model, then, Sonnet *is* below its threshold prediction on non-monotone runs and above it on contiguous ones. That is the same deviation the Abbott table showed ("Sonnet looks specifically weak on non-monotone runs"), described from another baseline. So FINDINGS both withdraws "Sonnet leans on the chart" and asserts, in Finding 3, that Claude's core minds favour contiguous runs. These are one claim. What the logit analysis actually shows is narrower: Grok's, Flash's and Haiku-without-thinking's apparent class differences under Abbott are what a pure threshold difference would produce, and Sonnet's (and probably Opus's) are not.

**Which correction fits the data was not tested.** Abbott ($P = c + (1-c)\beta$, a high-threshold model) and a logit threshold make different predictions about how a mind's yes rate on real runs varies with item strength. Both can be fitted to the same cohere answers with their shuffled controls, and compared by held-out likelihood. Until that is done, Finding 5 is a valid caution about parameterization, not "a correction to the catalog's method". Integration-plan item 2, which replaces CATALOG §9's combination rule, rests on that comparison.

**Two cautions on the contiguity offsets [re-derived, inference].**
- **The reference group differs per mind.** Each mind's offset is relative to $\beta$ estimated from *the other minds*, and that pool's composition differs per mind (Claude-heavy for Grok, Claude-light for Sonnet). Prior shrinkage of $\beta$ on items near the ceiling also adds a positive contiguous offset for every mind. So the absolute offsets aren't on one scale. The ordering within one source is more trustworthy than the pooled numbers.
- **Within the source that matters most, the outlier is Grok, not Claude.** `selfpref.py` on walks gives Sonnet +1.52, Haiku without thinking +1.90, Opus +1.14, **Gemini Flash +1.19 ± 0.51**, Grok -1.33. Flash sits with the Claude minds, and NOTES summarises it as "Opus and Gemini mixed". On written runs, Flash is -0.19, like Grok. So whether this is a Claude trait or a Grok trait isn't settled by the data. Flash favouring walks also tells somewhat against self-preference as the explanation, if walks were mostly Claude-written. That is checkable from the walks' answer provenance, and not checked here.

## 5. The `▁` scan: Flash is robust; the scan alone doesn't establish Pro

**Reproduced.** Flash z = -19.1 (n = 98), Pro z = -3.9 (n = 84). The agent's no-`▁` rerun (`scratchpad/glyphscan_noU2581.py`) confirms that Flash's other ramp glyphs are spillover. So are its `_` and `‗` cells, which also vanish.

**The z-scale is not calibrated.** With `▁` triads removed, the cells beyond $|z| = 4$ include `🞆` (Haiku, -5.5, n = 12), `ᚒ` (Sonnet, -5.1, n = 8), `ᬌ` (Sonnet, -4.9), `🞷` (Haiku, -4.2) and others. Over 2,388 cells, a calibrated scale would put about 0.15 cells beyond 4. The variance treats every answer as independent, but triad items are re-asked in rotations on the same sheets. So Pro's -3.9 ranks about 17th and sits inside the background. That Gemini Pro avoids `▁` rests on the earlier OBSERVATIONS (3/18), not on this scan. That's fine, but FINDINGS should say so: "Nothing else comes close" is true of Flash's -19 and not of Pro's -3.9.

**The scan partly masks family-shared effects.** $\beta$ excludes only the answering mind, so Flash's refusals sit inside Pro's $\beta$ and dilute Pro's residual. They also produce the mirror artefact: positive `▁` residuals for Haiku (+6.6), Grok (+5.0) and Opus (+4.2). To find *family*-specific glyphs, which is the spike's question, $\beta$ should exclude the whole family of the mind being scored.

A curiosity at noise level: Pro's next cells are `g` and `Ġ` (U+0120), together in the same 18 triads. `Ġ` is byte-level BPE's space marker. Gemini isn't byte-level, so I'd record it only as something to look at alongside `▁`.

## 6. "Sonnet and Opus are indistinguishable on continuation (D ≈ 0)" carries no information about family

**Re-derived.** `distance.py` uses only items each mind answered at least twice. For Sonnet–Opus that is 51 highly determined items ($W = 0.96$). On those same items, Sonnet–Grok gives $D = -0.006 \pm 0.005$ (45 items), and Opus–Grok gives 0.000. Every frontier pair is indistinguishable there. The decomposition MAP promised (noise floor, against within-family, against across) is powered only for Sonnet, Haiku without thinking and Grok. Within Claude, that compares Sonnet with a non-thinking small model, so "family" is confounded with capability and deliberation condition. The honest statement is that within-family spread at the same tier is unmeasured on continue: Sonnet–Opus has 51 items, Flash–Pro too few. Finding 4 reads stronger than the data.

The pick distances in NOTES reproduce via `distance.prepare` and `distance`. They don't come from `python3 distance.py pick` as committed, because `distance.py`'s MINDS list has no generator minds, so that command prints nothing. Grok–Flash on picks is $D = 0.090$ (n = 27), lower than within-Claude. That's small n, but it cuts against "on forced picks, there is a family component".

## 7. Gemini's comparisons are selected toward familiar glyphs

Every comparison drops `tool-attempt` answers (`values.value` returns None) and the `no-lookup` re-asks (variant filter). Gemini's continue tool attempts are not random [re-derived]:

| mind | contexts all single-token glyphs | contexts with an unfamiliar glyph |
|---|---|---|
| Gemini Flash | 0.081 (n = 1,039) | 0.188 (n = 2,639) |
| Gemini Pro | 0.107 (n = 244) | 0.187 (n = 572) |

(Single-token in either of two public byte-level tokenizers; "unfamiliar" means at least one glyph isn't.) The excluded `no-lookup` answers (536 Flash, 133 Pro, on continue) are Gemini's answers to exactly those contexts. So Gemini's thresholds, content agreement (Opus–Pro 0.987 on 76 items) and sidings are measured on an easier subset than the other minds'. A tool attempt is METHODOLOGY's own measurement ("did not answer from impression"), so it should either be modelled as a third outcome or bound the comparisons as a stated selection. Neither FINDINGS nor "Still open" mentions this.

## 8. The withdrawn Grok reading: the withdrawal stands, but "no familiarity effect" doesn't

`endplace.py`'s refutation compares chart-next with other glyphs without holding determinacy fixed, and chart-next contexts are mostly near-certain. Holding fixed the other minds' share for Sonnet's glyph [re-derived], whether the glyph is chart-next makes no difference to Grok's stopping. So the withdrawal of "Grok refuses chart walks" stands, now on firmer ground.

But at high determinacy (others at least 0.8 for Sonnet's glyph), Grok stops after a chart-next glyph that is multi-token 0.093 of the time (n = 2,496) against 0.049 when it is single-token (n = 871), z about 4.7. NOTES 17:05 says "No familiarity effect". A weaker form survives: Grok stops more often in unfamiliar territory even where the other minds continue. "Others" there are mostly Claude minds, so this is also consistent with Grok stopping where *Claude* chart-walks. That is close to the original reading, minus "refuses".

## 9. Wording that outruns the numbers

- **"That model predicts every flat … split."** It predicts a count, and one direction only (§1).
- **"Gemini Flash is the readiest of all minds to name a triad middle."** Its $\alpha$ is +0.05 logit above Sonnet's, a tie. The gapped-triad shares (0.82 against 0.72) support "readier on gapped triples".
- **Triads in the thresholds paragraph.** Finding 2 states thresholds by mind and kind with no qualifier. For triads, flat splits exceed the additive prediction by factors of 2 to 15 (Grok–Flash 66 against 26 and 13 against 0.8; Flash–Pro 4 against 0.1). NOTES records this; FINDINGS doesn't. The correlated-repeats explanation is untested, and it would apply equally to continue.
- **"At family level … one content split in 467 questions."** That's 453 triads and 14 continue contexts. The family-level continue test has almost no data and should be called unpowered, not clean. The one split, `■▤▦`, can be read: Claude and Gemini put `▦` (crosshatch) between `■` (solid) and `▤` (horizontal lines), an order by fill density, while Grok gives the code-point median `▤`. It's a small-n instance of look against chart, worth a line.
- **The nine Sonnet–Grok splits.** "Grok `🂑` (correct)" means the chart's successor. For dominoes 6-0…6-3 → 6-4 it is also the right tile, but "correct" should say which sense. "An arithmetic slip" for `🂱` (U+1F0B1, against U+1F091) is an inference, and should be labelled so.
- **Debrief: "… so the study's 'how the format manufactures the order a mind reports' shows up here directly."** The phrase is the magnitude era's claim 3 (`.archive/2026-10-04-magnitude-era/`). The link is apt, and it's sharper than the debrief makes it. That era's independent reading found that the orderings a "decline" option suppresses are *shared across families* (83% cross-family agreement on the forced winners). That's the same shape as Finding 1: declining hides a shared ordering. FINDINGS never draws the connection, and the debrief is the only place it appears. Joseph will read the debrief alone, so its two strongest sentences ("asking again won't settle anything"; the parameter "read … after each model's caution is accounted for") should wait for §1's recalibration.

## 10. Reproducibility

The spike's numbers come from a pickle in a session scratchpad (`/private/tmp/…/fd-snapshot.pkl`). The answer files are gitignored and keep growing while the drains run, so once the scratchpad is cleaned, no one can rebuild the snapshot. `lib.py` records per-file SHA-256 prefixes, but only inside the pickle. Writing that manifest into the spike directory, together with the git commit of the ledgers the answers were built from (or byte lengths per answer file, since the drains append), would make the spike checkable later. This pass relied on the pickle still existing.

## 11. The seal

`lib.sealed` matches `catalog/build.py`'s rule character for character. On kept records, the fields it checks cover every glyph a `choose` or `names` question shows: `chart` is always one of `candidates`, and `names` records carry their glyphs in `shown`. Every analysis in the spike, and every analysis of mine, loaded through `lib.py`. I queried, counted and displayed no sealed answer. NOTES 16:36 discloses one pre-`lib` count of records by kind × family that included sealed records in its totals. It counted records, not answer content, and the SEAL's wording ("query, tabulate or display those answers") arguably reaches it. I mention it for the record, not as a breach that matters for the freeze.

## Implications for the integration plan

- **Item 1 (no disagreement term; information $p(1-p)$ through each mind's threshold).** Premature until the threshold model is calibrated (§1). The intuition that flat splits are partly strictness is well supported. That they are *settled* is not.
- **Item 2 (replace §9's combination rule).** It needs §4's model comparison first, and a fit that passes §1's calibration check.
- **Item 3 (the per-sequence quantity).** The three parts are sensible. "Content splits" should be read off the chart: a split between two chart-successor answers can't happen, and agreement on the chart successor isn't sequence evidence. "Threshold-corrected strength" inherits §1.
- **Item 4 (universality on content and corrected strength).** Agreed. Add §7's selection caveat for Gemini.
- **Items 5–6.** Agreed. For item 6, the walks' authorship can already be split by which minds' answers built each walk, which may give self-preference against chart reliance some power before new runs exist.

## What I did not do

I did not fit the mixture or 2PL model that §1 says the claim needs, and I did not run §4's Abbott-against-logit comparison. Those are the strengthening attempts. I did not check the literature citations against the papers (Panickssery, Bowman and Feng, NeurIPS 2024, is real and says what is claimed; I didn't open Cacioli 2026 or TokSuite). I did not read the whys-basis, contested-positions or embedding spikes beyond what MAP quotes.

## On the brief

The brief was right for an audit. Two things would have saved time: the fact (now in the README) that the NOTES timestamps are estimates, and a pointer to where the snapshot lives. The second I found only because this session shares the spike agent's scratchpad.

## Appendix A: what my checks change, so they can be rebuilt

- **`eb.py`.** `additive.py`'s model and tests unchanged, except that the item prior is $N(\mu, \tau^2)$. Each iteration sets $\mu$ to the mean of the $\beta$ modes and $\tau^2$ to the mean of $(\beta - \mu)^2$ plus the posterior variance. There is no re-centering of $\alpha$, and Newton runs 40 steps. It prints single-answer obs/pred and flat-split obs/pred with a 400-draw band. Fitted values: continue-stop $\mu = -1.55$, $\tau = 1.65$; triads $\tau = 2.02$; cohere $\tau = 1.49$.
- **`calib.py`.** As `additive.py`, but it bins items by how many answers from other minds their $\beta$ rests on (1–2, 3–5, 6–11, 12+).
- **`content.py`.** `commit.py`'s pairing (first answer per mind, plain variant, no control), split by whether each answer equals `endplace.chart_next(context)`. Also a common set where Sonnet, Opus and Grok all commit.
- **`choose2.py`.** Paired Sonnet–Grok difference with SE over positions. Real against neutral-control paired on (candidate pair, chart) per mind. Position bias from `tags.chose_position` (checked: position `a` is `candidates[0]` in all 2,492 tagged answers).
- **`dist2.py`.** `distance.distance` restricted to the Sonnet–Opus item set, and over generator minds for picks (real and null).
- **`endplace2.py`.** `endplace.table`, binned by the other minds' share for Sonnet's glyph, by chart-next, and by token familiarity.
- **The triad-class table in §2, and §7's tool-attempt rates.** Short inline computations over the same snapshot.
