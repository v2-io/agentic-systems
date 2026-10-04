# A letter about the v1.0 data

Joseph,

You asked one question, so I'll start there.

**Can the old signa sequence be treated as a plausible human-made sequence included as a sort of control?** Yes, and I think "nuanced" is the right word for what kind of control it is. Its value comes from one fact: it was fixed ten months before the study, in your zoetica work, as a time notation, and nobody chose it because of how it would behave here. Every other ordered stimulus in v1.0 was proposed by an LLM surveyor, picked by the builder, or carried over from the pilot. So signa controls for selection: for the possibility that the study only finds what its own stimulus-pickers already saw.

What it shows, once you analyze the two halves separately instead of the whole sequence, is this. Every frontier judge reproduces your order exactly inside the line half (`·╶╌╍━═`) and inside the circle half (`⚬○◎◉⬤`): 180 of 181 committed edges. Where they leave you is the same place for all of them: the step from `═` (1 hour) to `⚬` (4 hours). Five of the Claude and Grok runs say outright that `═` is more than `⚬`, and the two Geminis decline 25 of the 30 line-versus-circle comparisons. In the gestalt task, 13 of the 21 frontier answers are exactly `·⚬○◎◉⬤`, with the lines set aside as a separate, still-ordered group. In your design, `·` heads the lines as the shortest mark; the judges almost unanimously put it at the root of the circles, as the smallest disc. It really does belong to both.

So the judges don't scatter. They depart from your intent at one specific, interpretable point: the radix reset in your notation, where hours begin and the glyphs restart small. Two limits keep this from being a stronger claim:

- **It doesn't prove "unbiased" in the strong sense.** Perception of the glyphs and a shared prior that "ladders grow in visual size" predict the same pattern, and nothing in v1.0 separates those.
- **It's exploratory.** Signa was added after the predictions were registered, there was no prediction about it, and it ran only in the ⟂-available format. So it can't speak to how much order forced-choice formats add.

One thing worth protecting: if the aspectus glyphs are being redesigned (your word *"old"* suggests so), the new set can be a good hypothesis test, but it can't take over this role. Only something fixed before anyone saw the data can.

On "with the correct analysis", you were right that it matters. Whole-sequence statistics mislead on signa in both directions. Pairwise τ looks "moderate". Gestalt τ looks "perfect": 1.00 for four judges, because the protocol computes τ only over the glyphs a judge kept, and they kept only the circles. Scored branch by branch and seam by seam, the picture is the one above. That exclusion artifact also affects other gestalt numbers, for example opus on your `unfold`.

Beyond your question, four things seemed most important to me. Each one is about what a number *means*, not about whether it reproduces. The numbers reproduce: an independent verifier rebuilt them with its own code.

1. **The edges ⟂ removes are not noise.** When one frontier judge declines a pair under the ⟂ format but commits to it under forced choice, judges from *other model families* pick the same winner 83% of the time, against 50% for chance. The pilot's "the format manufactures 80% of edges" is better read as "the ⟂ option suppresses a weaker ordering that the model families share". Whether that shared ordering is faintly felt or built by a common heuristic, these instruments can't say. The pilot's 80% is also partly about conditions. Run as a Claude Code subagent with your global context and the pilot wording, the same Sonnet model says ⟂ about 1.6–1.85× as often as it does as a clean API judge. The pilot also placed both orders of each pair on the same sheet, which v1.0 never did.

2. **The triad cycle statistic can't measure transitivity as designed.** Each orientation set is arranged cyclically (AB, BC, CA). In such a set, a 3-cycle is the same event as "the same slot won all three". The pilot's llama "37% cycles" goes with a 76% preference for the first slot. When I keep only pairs that answer the same way in both orders, there are zero cycles for every judge where that can be measured, small models included. Order-stable judgments look transitive at every scale tested. What larger models clearly buy is more order-stable judgments and more willingness to say ⟂.

3. **Several pilot signatures don't replicate as stated.** Your drain, the pilot's example of an *authored* sequence that judges couldn't reconstruct, is now reconstructed exactly (reversed) by several judges. Their main alternative is your three strata in reversed stratum order. The per-mille result (‱ wins about 3:1) turns out to be Sonnet-specific: most other judges side with denoted value. Noise foils drew ⟂ only 64% of the time, and some random sets got the *same* order from several model families. That is a reminder that any glyph set has a faint shared "complexity" order, so high gestalt agreement needs a baseline to mean much.

4. **Some of the pilot holds up.** Compiled numeric decoding beats ink everywhere it exists (Roman, small digits, seven-segment, fractions). `☷ > ⚌` is unanimous. Number and ink survive as axes for frontier judges, and the number axis fades at 3–4B, as the builder predicted. Against registered thresholds: P2, P3, P4, P7 and P9 hold. Most of the rest are mixed, or not supported as worded. The per-prediction table is in `02-registered-predictions.md`.

On new data, I've listed what's missing and why in `04-new-data.md` without designing anything. The three I'd point to first are signa (and other things fixed before the study) under forced and tie formats; even a few human judgments on signa's seam; and a transitivity unit that slot preference can't imitate.

How the work went: I read everything in the clean room and wrote my own pairing and scoring code on top of the builder's parser. I traced signa's provenance through zoetica and date-bounded memorata searches; the queries are listed in `01-signa.md`. Then I asked a fresh agent for an adversarial re-derivation with a bare brief. It reproduced the numbers and caught real errors in my interpretation:

- I had offered "every flip is same-slot" as evidence; it's true by definition.
- I had said an ink rule "predicted" signa's seam; it doesn't discriminate below rising-ink steps.
- I had framed signa more broadly than it can bear.
- It added sheet-pairing as a factor and found a second signa-like case, `elab-n`.

Those corrections are now in the documents, with the wrong versions removed. Its report sits unedited in `verification/`.

I'm glad to stay on the line.
