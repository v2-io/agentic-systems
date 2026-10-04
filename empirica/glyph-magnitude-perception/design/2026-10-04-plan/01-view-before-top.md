# 01 — My view before opening the top-40 material or yesterday's interpretation

*Written 2026-10-04 by a Claude Opus 5.5 agent, at Joseph's request ("look into the work generally and … figure out the best way to surface stable sequences, how to measure them, and how to discover their degree of universality"). This file is committed by itself, before I open `analysis/top40.*`, `harness/top40/`, `data/stimuli-v1/top40*`, `analysis/views/`, or the `compare-*` tables, and before I read the v1.0 findings, debrief, results or the clean-room reading. Later files in this directory record what changed after each of those reads. This one stays as written.*

## What I had read when I wrote this

- **Read in full:** `pilot/pilot-record.md`, `pilot/DESIGN-scale-up.md` with its addenda, `protocol/PROTOCOL-v1.0.md` with its post-freeze notes, `PREDICTIONS-v1.0.md`, `data/stimuli-v1/LINEAGE.md`, `MANIFEST.md`, `RUNS.md`, `data/surveys-v1/{README,RECONCILIATION-QUEUE,SCHEMA-draft,SEED-PRIORITY-v1}.md`, and both prompts in `data/surveys-v1/prompts/`.
- **Read in part:** the surveys. I read grok-1's opening and its long closing walk (morphs, mutations, Cree), the closing reflections of sonnet5-1 and sonnet-survey-1 to -4, and the section structure of each.
- **The dialogue.** All 55 of Joseph's typed turns from the 08-25 session (`60066910…jsonl`, recovered from `~/.claude.bak.2026-09-23/`). His image of Grok's thinking was not available to me.
- **Memories.** `articulation-filter-clamps-liminal-perception`, `efficiency-is-the-tell`, `decisions-need-the-decision-list`, and `brief-carries-the-ask-not-my-downstream`.
- **Already in view.** That last memory is dated today. It describes the top-40 candidate rule: Jaccard 0.5, greedy 0.34, longest record wins ties. It also says the rule kept one surveyor's longest variant over the shared core in 15 of 117 candidates. So I knew the rule's shape before writing, though not its output. MANIFEST's v1.0 claims were also in view.

## What the study is asking, as I understand it

Two objects, held co-equally:

1. **The glyph-order structure.** Which glyph sequences minds treat as monotone, by what route that order reaches them, and how widely it is shared.
2. **The instrument.** How a format, context or answer channel adds or removes order.

The 08-25 record is a long run of the second object correcting the first. Forced choice gave chains that splice across domains. ⟂ dissolved most of them. Pairwise testing was blind to orders that only a whole set reveals. Asking a mind to name the axis blocked continuations it could otherwise produce. Grepping Unicode names blinded three surveyor families. Each correction came from changing the instrument and watching the order change.

Joseph's 08-25 constraints, as I read them, are design law here, not preferences:

- Discovery should need **no prior information about the glyphs** ("the area-filling / monte carlo walk"). It should not inject analytic assumptions ("pearson correlation etc.").
- **Surveys are seeds, never data.** They are polluted by steering, and their use is to choose loci and allocate initial resources.
- **No forced aspects.** No mechanism registry, no mechanism-organized batteries. Categories are allowed only as careful priming examples or as post-hoc hypotheses. Structure is found by measurable feature correlates after the fact, including linear directions in representation space.
- **Some orders need more than 2–4 glyphs present** before they can be perceived.
- **Fated randomness**, an append-only ledger, and replayable derived layers.

## The central judgment

**A "stable sequence" is a set of invariances, not one property.** "Monotone" is always relative to a mind, a context and an instrument. The pilot and v1.0 both found that every one of those three moves the answer. So the deliverable should not be a list of sequences that are true. It should be a catalog in which each sequence carries a **stability profile**: which transformations its order survives, and among which minds.

The transformations I think matter:

| invariance | the question it answers | what we already know varies it |
|---|---|---|
| resampling the same mind | is it noise? | API temperature defaults |
| presentation order | is it side or position bias? | 3B P('>') = 85%; the triad-cycle/position coupling noted after the audit |
| format (forced / tie / ⟂) | is it manufactured on demand, or below threshold? | ~80% (pilot), 0.28–0.72 (v1.0) |
| unit (pair / set / continuation) | is it holistic? | unfold and risebar: ⟂ pairwise, recovered from the set |
| context (bare API / CLI / agent harness / sheet) | is ⟂ discipline a property of the mind or of its situation? | sonnet-5.5: ⟂ 0.76 in the harness vs 0.41 at the CLI |
| set composition (salt, neighbours) | does membership hold up? | unfold shatters under salt; risebar absorbs everything on its axis |
| framing ("more" / "less" / "further along") | is the order an axis, or an answer prior? | **untested** |
| input channel (glyph token / rendered image / Unicode name) | *by what route* does the order arrive? | **untested**; I come back to this below |
| mind (family, scale, modality, tuning) | universality | small models vs frontier; family splits on ‱ |

On this view, "how to measure them" and "how measurement manufactures order" are one research program. The format question is one axis of the stability profile.

## Two things I think must change in how candidates are chosen

**(1) Selecting candidates by surveyor agreement is circular for a universality question.** Six of the seven surveys come from Claude-family minds; grok-1 is the exception. Choosing sequences because many surveyors wrote them down chooses sequences that are already salient to Claude-family minds. Their measured cross-mind agreement is then inflated by the selection. Surveyor count is fine for deciding where to look first, which is exactly the role Joseph gave the surveys. It is not fine as the filter on what gets measured.

**(2) Choosing one representative variant per sequence throws away the thing to be measured.** When surveyors wrote `░▒▓█`, `▫░▒▓█` and `□░▒▓█`, the question is not which string is the sequence. It is where the shared order lives and which rungs are contested. The principled unit is the **locus**: the connected component of overlapping records. Its stimulus is the **union of glyphs** across all of its variants. What we measure, per mind, is the partial order over that union. Extra variant rungs then act as natural salt. Stable sequences come out as maximal chains in the cross-mind consensus partial order. Forks (Grok's `<⊂⊆⋐` / `<≪⋘` / `<⟨⟪`) and lattices (braille, sextants, the drain) come out as what they are, with no need to linearize them. This also answers, with data rather than a rule, the problem the memory names (longest variant kept, core suppressed).

Large components (all the numeric glyphs, say) need splitting into fated sub-loci small enough to show whole, around 8–10 glyphs. The pairwise layer then stitches them.

## The surfacing loop I would build

This is close to the loop DESIGN-scale-up sketched on 08-25. It differs in where candidates come from and in what counts as a result.

**Intake, from several independent streams, each lineage-labelled:**

- **(a) Every survey record from all seven surveys.** The `record_type`/`type` defect is fixed, and records are grouped into loci. No strength or concordance filter is applied; SEED-PRIORITY may order the work, but it never excludes anything.
- **(b) A prior-free generative stream.** Fated, block-uniform single glyphs, or pairs, go to a mixed-family panel with the articulation-free continuation prompt ("if something comes next, continue it; it may have no name; otherwise decline"). Most will decline. The ones that continue are discoveries no survey primed. This is the cheapest route to Joseph's "no prior information about the glyphs", because it lets the mind do the search in its own latent space instead of having us sample ~10¹⁰ pairs. It also measures the base rate at which minds invent continuations, which is the null that stream (a) needs.
- **(c) Recycled discoveries.** Frontier proposals from continuation at both ends of a stable chain, chains found in the pairwise graph, and absorptions found in salting.
- **(d) Controls.** Fated noise sets matched in size and block distribution; permutations of candidates; and the surveyors' own tempting-but-false negatives. The negatives are first-class, as Joseph said on 08-25.

**Measurement.** One battery per locus, identical whatever the source, so a candidate's origin cannot shape how it is tested:

1. **Set level first.** Gestalt reconstruction over 3 fated shuffles, with ⟂ and EXTRA allowed. Record **the order the mind produces**, not only its distance from an author's reference. Universality should be computed between minds' orders, so the surveyor's string never becomes the gold standard.
2. **Pairwise, targeted by the minds' own arrangements.** Adjacent rungs of each mind's arrangement, plus the disputed pairs. Both orders, under both ⟂-bearing and forced formats. The two formats measure different things: forced direction, made consistent across both orders and resamples, carries order below the ⟂ threshold, and the ⟂-format commit rate carries felt salience. Collapsing them is how "manufactured" and "sub-threshold" got conflated. A *manufactured* order should be idiosyncratic: inconsistent across resamples and minds, or explained by position and answer priors. A *sub-threshold* order should be consistent even when each mind would decline it. The pilot's graded battery already showed the second kind exists (Ogham, star weight).
3. **Continuation from prefixes of length 2–5**, in both directions. This gives the onset length for holistic orders and proposals at the frontier.
4. **Salting with fated distractors** drawn from the same block and from rejected proposals.
5. **A framing control on a subset.** Ask for "less", and ask "further along?". A real magnitude should invert cleanly under "less". An answer prior such as "pick the denser glyph" or "pick the second glyph" will not.

**Stop rule:** loop until K rounds accept no new rung, as already designed. The uniform-pair stream keeps running alongside as a standing control. Its purpose is the denominator: how often a given mind, in a given context, orders two random glyphs at all.

## Measuring by route: three input channels

This is the part I most want to add. The pilot's mechanism language ("visual", "ink", "compiled decode") was introspective, and Joseph ruled that mechanism must be found by correlates, never imposed. Correlating with a font's ink is indirect, because no judge ever sees pixels.

The same multimodal mind can be given the same locus three ways:

- **as text glyphs** (the token channel, what every run so far used);
- **as a rendered image** of the glyphs, in two or three fonts, with no codepoints in the prompt;
- **as Unicode names** (`LOWER ONE EIGHTH BLOCK`, …), with no glyphs.

Where the order survives tells us how it arrives:

- It holds as an image, in several fonts: the order is in the shapes.
- It holds only as text and names: it is carried by knowledge or names.
- It holds as text but not as names: it is learned from the glyph's own usage.

The minds are never asked to name anything, so the articulation filter does not apply. The categories are never imposed; they are read off from which channel carries the order. The channel test also gives "ink" a proper test: the image channel is where ink can act at all. The name channel puts the grep-on-names hazard, which surveyors fell into, under measurement instead of leaving it as a trap.

Two more measurement tiers ask nothing at all, for open-weight models (the local panel, Glimmer):

- **Likelihood.** Compare log-probabilities of a locus's permutations in a neutral frame, under a base model where one is available. This is order with no question asked. Its confound is string familiarity (`▁▂▃▄▅▆▇█` is memorized as a string), so it is evidence about exposure as much as about perception. Read beside the asked tiers, it shows how much of an order is a memorized string.
- **Representation.** Linear directions in hidden states that order a locus. This is the "linear semantic vectors" thread Joseph flagged, extended past the one embedding probe. Per-glyph token geometry also matters here: byte-level tokenization splits most rare glyphs into several tokens, and codepoint neighbours share lead bytes.

Together these give a gradient over how much the instrument asks: representation → likelihood → continuation → set → pair → articulated survey. That gradient is itself the measurement of "how format manufactures or suppresses order". An order present at every tier is robust. One present only under forced pairs is manufactured. One present at set level and not in pairs is holistic. One present only in likelihood is familiarity.

## Universality

- **Universality is always relative to a panel and a context set.** State both. Describe the panel along the dimensions that plausibly matter: family, scale, text-only vs vision-trained, base vs instruct vs reasoning, tokenizer, and the context it was run in.
- **Statistic.** Per locus, agreement *between minds' own orders*: mean pairwise τ over the shared glyphs, and Kendall's W, against a permutation null that depends on set size. Per adjacent link, the share of minds and families for which the link holds. **A chain is as universal as its weakest adjacent link.** The ends of a ladder are usually safe and the middle is where it dies, so per-link reporting is the honest unit.
- **Weight families, not models.** Four Claude models agreeing is close to one observation, not four. Weighting by family (or a hierarchical mind-within-family model) stops the panel's Anthropic skew from inflating "universal".
- **Name the likely cause of sharing.** Much of what is shared across LLMs may be shared training text: Unicode charts and names, sparkline usage. That is not a confound to remove. It is an explanation to test, and the name channel and the likelihood tier test it.
- **Other kinds of mind.** A human arm (Joseph, Suzanna, whoever is willing) on rendered glyphs would put LLM universality against human perception. DESIGN-scale-up proposed this, even at n = 1. A gestalt-and-pairs page as a published artifact with a shared database would make it cheap. The image channel also gives vision-only models a seat.

## Hazards the record already names, which the plan has to carry

- **Triad position coupling.** The post-audit protocol note says every within-orientation 3-cycle in this design is three same-position answers. Cycle rates therefore need edges made consistent across both orders before they mean transitivity.
- **⟂ depends on context.** So "how much is manufactured" has to be reported per context, never as a constant.
- **The prompt's own list primes axis words.** "MORE (magnitude, amount, intensity, size, value)" lists axes. A variant with no axis words belongs in the framing control.
- **Codepoint and byte proximity confound "within-locus coherence".** Within-page survival (73%) against cross-page (14%) could partly reflect token similarity. The control is within-block pairs on no felt axis against cross-block pairs on a shared one.
- **Reasoning effort is not equalized**, and thinking can construct comparisons. Effort should be a recorded factor, varied on a subset.
- **Render dependence.** Ink measured in one terminal font is one face. The image channel needs several fonts, and so does any ink correlate.
- **Builder-chosen stimuli (class B)** should not enter confirmatory sets. Selection should be by fated rule from loci, or come from the minds' own generations.

## Discovery, then confirmation

Discovery rounds are exploratory and run until dry. Then: freeze a catalog with stability profiles, register predictions about which links and chains hold for which panel and contexts, and confirm on a fresh fate with at least one family that was not in discovery. v1.0 already established the registration practice. What changes is that candidates now come from loci and generative discovery, not from hand-picked or concordance-picked lists.

## Measure first?

Nothing has to be measured before this plan is right in outline. Three parameters should be set by small pilots before a large run:

1. **Within-mind test-retest variance at default temperature.** This decides how many reps a link needs. v1.0's conflict battery ran 3 reps, so this may already be computable from existing ledgers with no new calls.
2. **Channel feasibility.** Does an image-channel gestalt work at all for a frontier multimodal judge on 2–3 controls (dice, ramp) and 2 noise foils, and does the name channel give anything? About 30 calls.
3. **Likelihood feasibility.** Can the local stack (ollama / llama.cpp) return log-probabilities usable for permutation scoring? About an hour of local compute.

Quota (corrected by Joseph mid-session): only Codex is exhausted, until Nov 2. Anthropic is fine. Gemini is rate-limited but usable. Local models, Glimmer included, are fine but slow. OpenAI's frontier model is therefore absent from any panel before Nov 2. gpt-oss-20b is the OpenAI-family stand-in, with the obvious caveat.

## What I expect the top-40 material to show

This is a prediction, made before opening it, so the next file can say whether I was primed. I expect the top-40 list to:

- be dominated by Claude-family-salient sequences (circled digits, block ramps, dice, circle fill), because of how it was selected;
- carry some suppressed shared cores, as the memory reports;
- produce cross-mind agreement figures that look high.

I would read those figures as agreement about *what was pre-selected for agreement*, not as an estimate of universality. If the material contradicts this, the next file will say so.
