# 02 — What changed after reading the v1.0 record (still before the top-40 material)

*Written after `01-view-before-top.md` was committed (d09b2fdf). Read since then:*

- *the clean-room reading in full (`analysis/independent-reading-2026-10-03/`: README, PROVENANCE, CLEANROOM-README, LETTER, 01–04, and `verification/VERIFICATION.md`);*
- *three of its tables (`conflict-items.tsv`, `manufactured-edges.txt`, `p13.txt`);*
- *the builder's `analysis/2026-10-03-v1.0-findings.md`;*
- *`debrief.md`.*

*Still unopened: everything on the top* list, and `analysis/v1.0-results.md`, which contains the top-40 tables.*

## How much weight I give yesterday's record

- **The numbers: full weight.** Two independent loaders reproduced them: the clean-room analyst's and its adversarial verifier's.
- **The clean-room reading's interpretation: high weight.** Its author never saw the primed analysis, and its verifier corrected it where it overreached.
- **The builder's interpretation: less, by layer.**
  - On the core claims it agrees with the clean room, after its two audits.
  - Where it is primed, the priming sits in what was *selected*, not in how it was *scored*: the SIGNA probe, the class-B conflict and holistic items, the top-40 candidate rule.
  - Its MANIFEST wording still carries one framing the data now contradict. "Offering ⟂ removes … directed edges" reads as removing noise, but what ⟂ removes is a shared ordering (below).
- **Where this leaves the MANIFEST.** The claims list should eventually be restated against the clean-room reading. That is Joseph's to decide, and I have not touched MANIFEST.

## What moved in my plan

### 1. My criterion for "manufactured" was right. The pilot's reading of its 80% was not.

In stage 1 I argued that forced direction and ⟂-commit measure different things. I said a manufactured order would be idiosyncratic and a sub-threshold order would be consistent.

The clean room measured exactly this. When one frontier judge drops an edge under ⟂ that it committed under forced choice, judges from *other model families* pick the same forced winner 83% of the time (chance 50%; surviving edges 96–97%). This holds at 0.82 even with every numeric glyph removed.

So the edges ⟂ removes are a weaker ordering *shared across families*. They are not noise. What the instruments cannot tell apart is whether that ordering is faintly felt or built on demand by a heuristic all the families share.

That gives the plan a sharper target: separate "felt but sub-threshold" from "shared heuristic". The next item is how.

### 2. The null I proposed was too weak. There is a generic order on arbitrary glyph sets.

- **The evidence.** On fated random noise sets, frontier judges produced an order 36% of the time, and *different families often produced the same order*. Every frontier answer to noise-3 starts with `˛`.
- **Why that breaks my null.** A permutation null for gestalt τ treats any agreement above chance as structure. Some of it is a generic order every mind applies to any glyph set.
- **The baseline the plan now needs.** For each mind, a **generic glyph scalar**: one latent "more-ness" score per glyph, fitted from forced-choice answers on uniform-random pairs, made consistent across both orders. If such a scalar fits well, it *is* the shared heuristic from item 1, and its cross-family agreement is a finding in its own right. It probably connects to the qwen3-embedding "more" direction.
- **What a candidate sequence is then scored on.** Its agreement *beyond what the generic scalar predicts*, against the empirical distribution of agreement on matched noise sets. That excess is where specific axes live. Roman numerals (value against ink) and `☷ > ⚌` (line count against ink) show such axes exist. "Is there an order?" becomes "is there an order the generic scalar doesn't explain?"
- **Whether a single scalar exists at all is itself a test.** The pilot's forced-choice walks looked globally non-transitive. Once slot effects are removed, order-stable triads show zero cycles at every tier (below). That leaves room for an approximately scalar generic order, and it is cheap to measure from uniform-pair data.

### 3. The triad unit as built cannot measure transitivity

In a cyclic orientation set (AB, BC, CA), a 3-cycle is the same event as one screen slot winning all three times. The pilot's "37% cycles at 3B" goes with a 76% first-slot preference.

- **What survives the fix.** Restricted to edges consistent across both orders, there are **zero cycles at every tier** where any can be measured.
- **What the plan should do.** Score transitivity on order-stable edges only. Treat "capability buys transitivity" as unsupported. What capability visibly buys is order-stability and use of ⟂.

### 4. One presentation per order is too few

The conflict battery is the only v1.0 instrument with repeats: 2 orders × 3 reps. My count from the clean room's per-item table shows how often a frontier judge gave the *same* answer on all six presentations of an item:

| judge | items, of 38 |
|---|---|
| opus55 | 32 |
| grok46 | 28 |
| sonnet55 | 27 |
| gemini38flash | 26 |
| sonnet55, sheet | 24 |
| sonnet5 | 18 |
| haiku45 | 17 |
| gemini31pro | 17 |

These items are hard by design, so the counts overstate noise on easy ladders. On contested links, though, one presentation per order cannot tell a flip caused by sampling from a tie resolved by slot.

The plan should run ≥ 3 reps per order on every link it scores. That settles stage-1 pilot question 1 without new calls.

### 5. Score the mind's own arrangement, and report what it left out

- **The protocol's gestalt τ rewards exclusion.** It is computed over kept glyphs, so moving awkward glyphs to EXTRA raises it. Opus scores 1.00 on unfold by setting `-=` aside; haiku scores 1.00 on the drain by keeping only the trigrams.
- **Minds agree with each other against the author.** Signa's `═→⚬` seam and elab-n's `nɳɲŋ` (19 of 24 frontier answers) are both cases.

Both support stage 1's choice: universality computed *between minds' own arrangements*. The gestalt record per mind needs four parts: the produced order, the partition (what was kept and what went to EXTRA), coverage, and whether separate families were concatenated or split.

### 6. Context and sheet pairing are first-class factors

- **Context.** The same model's ⟂ use is 1.6–1.85× higher as a Claude Code subagent with Joseph's global context and the pilot wording than as a clean API judge.
- **Sheet pairing.** In the pilot, both orders of each pair sat on one sheet. That took mixed verdicts from about 14% to about 1%.

v1.0 could not separate harness, wording, global context, effort, sheet size and sheet pairing. They belong in a factorial on a fixed reference set, which is the "format" axis of the stability profile from stage 1, made concrete. The point it serves: a ⟂ rate is largely the judge's commit threshold *in a context*. Every claim using ⟂ has to name its context.

### 7. Missing answers are not random, so the answer channel matters most for small models

- **Glyph-specific losses.** haiku45 cannot echo `⬤` and emits neighbouring codepoints, so `⬤`'s rank drops for that judge.
- **Small models answer by slot.** Their data are dominated by slot preference: qwen2.5 answers "first, much" to 50 of 110 signa pairs. Their failure to show the number axis could be a channel failure as much as a perceptual one.

For local and open-weight models, the plan should read the **logits of both answer options in both orders**. Averaging over orders cancels slot bias analytically, and there is nothing to parse. Ollama 0.34.4 is the local runtime; that its API exposes token log-probabilities is my expectation, not something I verified. That makes the stage-1 "likelihood feasibility" pilot the gate on whether small models enter the universality panel as readings rather than as parse statistics.

### 8. A fifth intake stream: sequences fixed before the study, for a purpose

Signa's value as a control comes from one property: it was fixed outside the study, before it, for a function. That property is not rare. Sources include:

- the progress and sparkline glyph sets fixed in widely used software (tqdm-style bar fills, sparkline libraries, terminal meters);
- rating and severity scales in UI kits;
- the ladders Unicode itself declares in character names (the 1F78x size and weight grids);
- weather-icon progressions in forecast software.

These belong in intake beside the survey loci, labelled as their own class. They cannot fully answer "does the study only find what its own pickers saw?", but they can start to. The Unicode-name ladders double as name-channel material.

### 9. Frontier judges saturate on the survey seeds, so universality must be measured where it can fail

- **The seeds.** Frontier judges agree with surveyors' written orders on 0.90–1.00 of seed-local triads. The builder's top-40 summary says the frontier saturates and only the floor and small-model columns discriminate.
- **Two readings of that, which the selection argument from stage 1 predicts together.** The survey ladders really are easy for every frontier family; and Claude-surveyed seeds were checked mostly by minds that share their training climate.
- **Where universality can actually fail:** small models read through logits (item 7), the context factorial (item 6), the image and name channels (stage 1), non-Claude surveyors' records and generatively discovered candidates, and humans. Universality claims built on survey seeds and frontier judges alone will look stronger than they are.

## What stands from stage 1 unchanged

- loci as glyph-unions instead of chosen variants;
- the prior-free generative stream;
- the forced/⟂ separation, now with the cross-family test as its criterion;
- the three input channels;
- the tier gradient from representation to articulated survey;
- family-weighted universality and per-link, weakest-link chains;
- discovery, then registration, then confirmation.

The empirical reading above sharpens all of them and contradicts none.

## Still unmeasured, and how much it matters

1. **Does a per-mind generic glyph scalar exist, and does it agree across families?** This needs forced-choice answers on uniform-random pairs, both orders, per mind. The v1.0 format experiment's fresh-mixed stratum (80 pairs) may support a first look, though it is likely too sparse to fit a scalar. It matters a lot: it decides whether the baseline in item 2 is a scalar or something richer.
2. **Image-channel and name-channel feasibility.** Two small checks: does a multimodal frontier judge reconstruct dice, the ramp, and two noise foils from a rendered image, and does the name channel answer at all? The harness drives judges through CLIs with tools stripped, so an image input may need a direct API adapter.
3. **Logprob readout on the local stack** (item 7).

None of these has to come before the plan. Each one decides a design branch inside it.
