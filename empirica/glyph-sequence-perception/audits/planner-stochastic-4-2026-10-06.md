# Audit: planner stochastic-4 and the givens it rests on

*2026-10-06, about 18:50–19:40. Claude Opus 5.5, de novo: I had not worked on this study before. Written for the coordinating session and Joseph, before the loop is restarted on stochastic-4. I read the earlier planner audits only after my own pass, for their format.*

*What I read whole.* `METHODOLOGY.md`, `CATALOG.md`, the seal, the code diffs of `3399671d` and `bd724444`, `priority/plan.py`, `catalog/given_walk.py`, `catalog/givens.py`, `report/given.py`, and the R part of `catalog/build.py`. Of the generated files (`givens.json`, `CATALOG-GIVEN.md`, `CATALOG-VIEW.md`), I read headers and summary tables only.

*What I ran.* All from my scratchpad, writing nothing in the study:

- **Dry plans.** The planner in-process: stochastic-4 as committed, and stochastic-3 (`3399671d^`, with only its path line patched), on the same answers (318,806 records, read at about 18:55) and the same seeds, for three dummy round ids `zaudit1`–`zaudit3`.
- **Classifier probes.** `given_walk.classify` / `classify_cached` on hand-picked runs, pairs and sets.
- **Catalog queries.** Build `b20261006_183825`, model `catalog-v5-build5`.
- **R recomputed.** With the build's own functions, splitting the shuffled controls by whether the run they control walks a given.

*The seal.* I read no `choose` or `names` answers. The R recomputation went through `build.load()`, which drops sealed answers. Everything else I computed reads continue, pick and cohere answers only.

*Files.* I changed no tracked file but this one. Before I set `PYTHONDONTWRITEBYTECODE`, my first runs may have written `.pyc` files into the study's gitignored `__pycache__` directories. They hold the same bytes any run of the same Python writes.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

**Stochastic-4 is safe to run.**

- I found no validity, seal, determinism or sizing defect. Rounds come out the same size as under stochastic-3, within one question.
- It turns probing away from given walks. Questions whose glyphs walk a given fell from 12.3–13.4% of non-control questions under stochastic-3 to 0.9–1.5%, across three dry rounds [measured].

**What it calls "given" isn't quite what Joseph described, and the factor leaks.**

- **Wider than the definition (G1).** The classifier counts as given:
  - runs of one value or letter in several dresses;
  - walks that change dress partway.

  Joseph's definition excludes both, and `CATALOG-GIVEN.md` itself says a dress run "has a given set but not a given order". They are 20–30% of what stochastic-4 turns away. They include Joseph's own `①` / `⑴` / `❶` / `🯱` question.
- **The factor follows the question's glyphs, not the sequence the question serves (G2).** Skip tests, stride pairs and stride reflections of given sequences keep full weight. Skip tests on given sequences actually rose. Measured by the sequence served, questions about given sequences fell to about a third, not a tenth.
- **Classifier false negatives (G3, G4).** Some given sets escape, among them `{x, y, z}`. So do some given alphabets: the start of the Russian alphabet `абвгде`, and the start of the Arabic one `ابتث`.

**Before the restart:**

- I'd want one ruling, G1 (Joseph's).
- I'd land G2 and G3 with it; both are small code changes.
- G4–G8 can follow.

**If you restart as is, nothing breaks.** For some rounds:

- dress questions would be under-asked;
- skip tests on alphabets would be over-asked.

The shift in control rates (G5) starts whenever the planner turns away from given walks, so the catalog needs that note either way.

## G1. Dress runs, and walks that change dress, are counted as given

**The definition.** Joseph's definition, as quoted in `givens.py` and on `CATALOG-GIVEN.md`: *"contiguous, have a known canonical lexical ordering, known total order, same stylistic class ... implies a 'ready to use' sequence by design"*.

**The `dress` kind fails every clause.** A dress run such as `1 ¹ ① 𝟏` is:

- not contiguous;
- in no known order among its dresses;
- not one stylistic class, by construction.

`CATALOG-GIVEN.md`'s own decisions say so: *"A dress run has a given set but not a given order."* The planner still multiplies it by `GIVEN_RELEVANCE`, pairs included (`1 ①`, `a 𝐚`) [checked].

**The same kind takes in diacritic forms.** Any letters that some language's collation treats as forms of one letter count as a dress run. Examples [measured]:

- `óôõ` (Portuguese, base reading);
- `ÙÚÛÜ` (Welsh);
- `èéêë` (Ligurian).

These are Latin-1 walks in the order of the code chart.

**The walk kinds ignore dress.** `window`, `rotated`, `stride` and `reflection` don't check it [checked]. All of these are given:

- `1𝟐3𝟒𝟓`;
- `κλμνξο𝞹`;
- `⒃⒘⒙⒚⒛`;
- `𝟧𝟨𝟩𝟪𝟫𝟬𝟭`. This one walks the code chart across two Mathematical digit styles and wraps 9 → 0 where the style changes, so it is classified "rotated".

**How the minds treat them** [measured, catalog build 5]. 407 of the 1,431 given-walk records mix dresses, 120 of them `dress` runs. Recognised among those asked whole:

| kind | dresses | recognised / asked whole |
|---|---|---|
| window | one | 325 / 347 (94%) |
| window | mixed | 11 / 19 |
| dress | (any) | 14 / 37 (38%) |
| dress-window | mixed | 7 / 12 |
| stride | one | 55 / 67 |
| rotated | one | 24 / 31 |

Single-dress walks behave like known orders. That is the premise of the factor: little information is left in them. Dress runs don't behave that way.

**In the plans** [measured]. Under stochastic-3, dress and mixed-dress questions were 26 of 88, 19 of 67 and 16 of 79 given-walk questions in the three dry rounds (20–30%). Stochastic-4 cuts them to 0–5.

- One of the things turned away is Joseph's own question about dress order: `data/seeds/digit-dresses.jsonl`, *"Joseph's `①` vs `⑴` vs `❶` vs `🯱` question"*.
- The same rule takes 40 recognised mixed-dress runs off `CATALOG-VIEW.md` and puts them on `CATALOG-GIVEN.md`.

**What I'd suggest**, unless Joseph rules otherwise:

- Apply the factor, and the view's exclusion, only to single-dress walks: `window`, `rotated`, `stride` and `reflection` with one dress.
- Keep the catalog's given relation as it is. It already records the dresses, so readers can choose.

## G2. The factor follows the question's glyphs, so given sequences leak

`given_factor` classifies what the question shows: the context, context plus candidate, or the set. Questions that serve a given sequence escape it in three ways [checked; counts measured over the three dry rounds]:

- **Skip tests.** `𝜄 𝜃 → 𝜁?` skips a position, so it isn't a walk and keeps full weight.
  - Within a given sequence's claim, skip tests are now the only full-weight units. They lift the claim's mean weight and come first in its weighted order.
  - Skip tests on given sequences rose from 3, 3, 3 per round under stochastic-3 to 5, 7, 4 under stochastic-4.
- **Two-glyph contexts of stride walks.** By design, a pair counts only as a window, rotation or dress step. So these keep full weight:
  - k\* contexts such as `⑱⑮` (from `③⑥⑨⑫…`);
  - ends such as `፯፱`, `ⅨⅪ` and `㊿㊽`.
- **Reflections of strides.** `➓➑➏➍➏` and `𝋱𝋯𝋭𝋯` keep full weight, because the reflection kind needs steps of ±1.

G3 and G4 add false negatives on top of these.

**Net effect.** Questions whose source names a given sequence went from 50, 28, 35 per round to 12, 14, 12, about a third. My count by the same glyph test the factor applies reproduces the commit's figure (12.3–13.4% to 0.9–1.5% against its 12.1% to 2.0%). I take the commit to have counted that way too. A count made with the factor's own test can't see these leaks.

**What I'd suggest** [reasoned]:

- Where a unit serves a sequence (its claim is that sequence), take the factor from the sequence, `classify(seq, 3)`.
- Where it doesn't (explore, off-sequence items, sets, pick branches), take it from the glyphs, as now.

That also changes one thing in the other direction. The k\* and inside contexts of a *non-given* sequence that happen to be given windows would return to full weight: `8 9` inside `0123456789🔟`, for example. I think that is right, because they serve a claim that isn't given. It is a choice, though, and should be named as one.

## G3. Sets are ordered by the wrong index

**The cause.** `classify_cached(..., as_set=True)` sorts letters by their minimum index over *every* given that holds them, not by their index in one given. So any letter whose position differs between alphabets can sort out of order [measured].

- **Not given, though they are:** `{x, y, z}`, `{t, u, v}`, `{X, Y, Z}` and `{f, g, h}` (Quechua lists `h` second); `{ъ, ы, ь}`; Fraktur sets J–Q; Arabic `عظغ`.
- **Given, correctly:** `αβγ`, `абв`, `rst`.

**In the plans.** Under stochastic-4, 4, 5 and 3 of about 50 triad, order and names questions a round were given sets that escaped the factor.

**The fix.** For each given that holds every glyph, sort by the index in that given and classify; accept the first match.

## G4. "Most widely used alphabet" counts locale IDs

**The cause.** The classifier takes only the alphabet with the most entries in `languages`. Those entries are CLDR locale IDs, so a language listed with and without its script counts twice [checked].

- **Cyrillic.** The top alphabet holding `а`–`е` is Serbian/Bosnian (`bs_Cyrl`, `sr`, `sr_Cyrl`: 3), ahead of Russian (`ce`, `ru`: 2).
- **Arabic.** The top alphabet is Sindhi (`sd`, `sd_Arab`).

**The result** [measured]:

- `абвгде`, `клмн` and `ابتث`, the opening of the hijāʾī order, are not given.
- `абвгдеёжз` is given, because `ё` rules Serbian out.

**Impact on the catalog today.** 8 records (3 of them recognised). Small, but systematic. The same rule is why diacritic runs (G1) land on Welsh, Ligurian and Portuguese.

**A latent case: Hangul.** CLDR's Korean exemplars are its 11,172 syllables, which collate in code-point order.

- So the chart walk `가각갂갃` is a given window.
- `가나다라` and the jamo are not; `CATALOG-GIVEN.md` notes the jamo.
- No catalog record walks Hangul yet.

**What I'd suggest.** Collapse locale IDs to languages, and accept a walk over any alphabet of a stated set rather than the single top one. Or keep the top-alphabet rule and record the alternatives on the record.

## G5. Control rates differ by given-ness, and stochastic-4 shifts the mix

R's false-positive rate $c_r$ is pooled per (rater, set class). Shuffles of given walks are rejected far more readily than shuffles of other runs in the same class [measured; yes rate to the shuffled control, contiguous sets]:

| rater | pooled | given walks | not given |
|---|---|---|---|
| grok46 | 0.364 (1,581) | 0.204 (388) | 0.417 (1,193) |
| haiku45nt | 0.274 (1,429) | 0.143 (349) | 0.316 (1,080) |
| gemini38flash | 0.150 (234) | 0.000 (77) | 0.223 (157) |
| sonnet55 | 0.045 (1,429) | 0.014 (349) | 0.056 (1,080) |

On "other" sets the gap is smaller: Grok 0.322 against 0.466, Sonnet 0.141 against 0.132.

**Decisions today: little change.** I recomputed R with controls split by given-ness. Of about 3,700 runs asked whole, 6 non-given runs fall out of recognition and 15 given runs come in. Strengths move more than decisions.

**What changes at the restart** [reasoned]:

- From the restart round, few new controls are shuffles of given walks.
- So the pooled contiguous-class $c_r$ drifts toward the non-given rate: Grok from 0.364 toward 0.417.
- CATALOG §14's test 2 (control rates held out by round) would see that drift. It comes from the planner, not from the model.

**What I'd suggest.**

- Stratify $c_r$ by the given relation; build 5 already carries it.
- At least, record the restart round in the catalog's history as a planner boundary.

## G6. Lookalike loses its known-answer cases

**The numbers** [measured]. Given walks were 271 of the lookalike stream's 809 candidates, 35% of its weight before the factor and 5% after.

**Why it matters** [reasoned]. An alphabet with one letter swapped for a confusable from another block is the case where we know the answer: recognition rests on identity. That makes it the instrument's natural check, as the name-only validation sets are for the names question. Those sets were exempted on exactly that ground.

**A question for Joseph.** Should lookalike on given walks be exempt from the factor, or keep a share?

## G7. What the turn costs in discovery: little on continue, more on picks

**Continue at given contexts** [measured]. Of the answers naming a glyph not already shown, 1,183 leave the given and 17,686 stay on it (6%). The ones that leave are mostly code-chart neighbours: `⓮⓭⓬⓫ → ❿`, `óôõ → ö`.

**Picks at given contexts** [measured]. 339 answers leave and 489 stay. Some that leave are just the kind this study looks for: `ⅢⅡⅠ0 → −`, `½⅝¾⅞ → 1`.

**Recognised runs that grow out of a given** [measured]. 186 of the 1,617 recognised non-given runs extend a given walk at one end: `0123456789🔟`, `၉၈၇၆၅၄၃၂၁၀−`, `0⅛¼⅜½⅝¾⅞1`. Their end contexts aren't given walks, so they keep full weight.

**The generator** [reasoned]. Branches off givens start in the generator; Joseph's tendril example begins at `abc`. Under stochastic-4, new given roots are picked at 0.1. Branches already grown are unaffected.

## G8. Smaller things

- **Provenance.**
  - `plan.json` records `GIVEN_RELEVANCE`, but not the hash of `givens.json` or of `given_walk.py`, though both now move the plan.
  - The catalog manifest hashes `givens.json`, but its code hashes leave out `given_walk.py` (as they already left out `links.py` and `order.py`).
  - `givens.json` can be regenerated only under the ICU venv (ICU 78.3, whose Unicode 17 data is filtered to 16).
- **Edges of the pair rule** [measured].
  - The first and last positions of any given form a "rotated" step: `a z`, `0 9`, `Α Ω`.
  - Neighbours in a sparse value line form a window: `½ ⅗`, `⅓ ⅜`, `Ⅻ Ⅼ`.

  These are rare in plans.
- **Value lines across dresses** [measured]. A mixed-dress run is given only when one dress holds every value. So `1𝟐3𝟒𝟓` is given and `0⅛¼⅜½⅝¾⅞1` isn't. The Roman symbol order `ⅠⅤⅩⅬⅭⅮⅯ` isn't given. Consistent with the code, perhaps not with the intent.
- **The governing documents.**
  - METHODOLOGY §5 still says stochastic-3 plans from c106, and it describes relevance without the given factor.
  - CATALOG §11 (the view's rule, which the freeze fixes) doesn't say that the view leaves given walks out.
  - §13's freeze list doesn't name `givens.json` or `given_walk.py`, though the view now depends on them.
  - CATALOG's header still says builds 0–3.
- **CATALOG-GIVEN's "Walks not recognised (yet)."** 980 records. At 0.1, most will stay there for a long time.
- **`classify_cached` has no size bound** in the long-lived loop. Negligible.
- **`run.py plan RID` writes `data/rounds/RID/`.** A dry run writes nothing only when `plan()` is called in-process.

## Checked and found sound

- **The seal** [checked]. The factor reads glyphs only. The canary isn't a given: neither the run nor any of its pairs. `blind()` is unchanged.
- **Sizes** [measured]. Question counts per dry round are the same under both planners: 890/890, 701/700, 794/795.
- **Determinism** [checked]. The classifier's ties are broken by given id. Explore's extra draw is fated.
- **Controls and validation sets** [checked]. Controls are untouched. The name-only validation sets are exempt through their `from` prefix.
- **Explore** [measured]. The rejection keeps the stream's size. Given pairs fell from 9 to 1 of 128.
- **Runtime** [measured]. The first plan takes about 20 s longer while the cache warms. After that, both planners take about 40 s.

## What I didn't do

- I didn't implement or test the per-claim factor (G2) or the set fix (G3).
- I probed `givens.json` (913 givens) rather than auditing it whole.
- I didn't check `CATALOG-VIEW.md` beyond its counts.
- I didn't look in `spikes/`.

## On the brief

The brief was clear, and its facts were the ones I couldn't have found myself: the seal, the loop holding stochastic-3, the venv for `givens.py`. One thing would have saved a step: "a dummy round id writes nothing" holds for `plan()` called in-process, not for `run.py plan`.
