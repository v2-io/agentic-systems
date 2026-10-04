# 04 — Joseph's two questions (2026-10-04, afternoon)

Joseph,

The coordinator passed me your two questions, then your clarification that "round out the data" meant the study's own recycling discovery loop. Both changed my plan. `PLAN.md` is rewritten around the loop; this letter answers the questions.

## "What unicode says is irrelevant, what ghostty or any typefaces say is irrelevant"

Understood, and my morning plan needed this. I had proposed:

- a rendered- and degraded-image channel (typefaces);
- a Unicode-name channel;
- ink correlates.

Those answer a different question from yours, and they are out. In the revised plan, Unicode only enumerates candidate glyphs. Every reference, every feature and every ordering comes from the LLMs' own answers, and agreement across LLM families is the evidence that an ordering is an intuition.

## What broke down: why so little variation and mixing

You're right that v1.0 mostly took a few votes on obvious, exact seed sequences. I counted from the stimulus files; the counts are reproducible from `data/stimuli-v1/` with a one-off that I ran in the shell but did not commit as a script.

1. **The loop never ran.** What ran was a confirmation track: protocol freeze, registered predictions, held-out pools, batteries targeted at claims. Confirmation tests the pilot's claims. It doesn't explore, so the walk → poset → continuation → salting → re-entry cycle in DESIGN-scale-up was never built. The coordinator has said its brief pointed the builder there.
2. **The hubs were removed.** For confirmation hygiene, every glyph used in any pilot stimulus was excluded from the main instruments: 1,246 characters, plus all ASCII. The pilot had already used the glyphs most loaded with magnitude, so the triads and fresh pairs sampled the periphery. Of the 18 dresses of the digit one, only 9 were even eligible.
3. **Density was near zero.** 1,885 distinct pairs over 1,406 glyphs is 0.19% of possible pairs. The median glyph was compared with **2** others; 59% with 2 or fewer. A glyph's place relative to other families can't be read from two comparisons. The pilot's walks reached about 8.
4. **The mixing that existed was mostly with noise.**
   - The uniform tail is 286 letters out of 400 glyphs.
   - "Seed-cross" took one glyph from each of three random survey records.

   Random cross pairs almost never land on *related* families, such as two dresses of the same digit, so ⟂ swallowed them correctly. Your 08-25 ruling made sampling graph-neighbourhood driven, and the pilot's walk2 already densified within discovered neighbourhoods. v1.0 had no neighbourhood step.
5. **The top-40 battery asked about adjacent steps of surveyors' exact strings.** It is within-family by construction.
6. **The surveys had already asked your question, and it went unused.** sonnet5-1 and sonnet-survey-3 each recorded `①⑴⒈` as an *equivalence*: same value, different dress. The schema files equivalence and generator records as battery material, and nothing consumed them. Across all of v1.0, three pairs are same-value numerals, and none of them sets two dresses of one digit against each other.
7. **My morning plan would have repeated this.** It built loci as unions of overlapping survey records. Digit families don't share glyphs, so `①…` and `⑴…` would have stayed separate loci, and cross-family pairs would have come up only by accident. The revised plan makes cross-family density a requirement (§1) and treats the dress × value space as one lattice (§2.7).

In one line: **the unit became the surveyed sequence, when it needed to be the space of glyphs placed against each other.** The held-out pools, the strata and the top-40 battery all followed from that.

## Your concrete question: `①` vs `⑴` vs `❶` vs `🯱` at equal value

The coordinator had started a scratch probe of exactly this. It covered all 18 dresses of the digit one, every pair in both orders with ⟂ and ≈ available, plus the whole set shuffled. The coordinator stopped it when your clarification arrived; it is not part of the method. It is still the most direct data on your question, so here is what it shows.

**Status of the data:**

- It is **anecdote-tier**: one value, one format, one presentation per order.
- The data are complete for opus, sonnet-5.5, grok, gemini-flash, llama-3B and qwen-3B, and partial for haiku and gemini-pro.
- They live in the scratch clean room, **not in the study**. If this result should count, the ledgers need landing.

| finding | evidence |
|---|---|
| **Yes, frontier LLMs share an ordering among dresses of the same number, across three LLM families.** On pairs two frontier judges both commit to (both orders agreeing), they pick the same winner essentially always. | gemini-flash vs grok 63/63; gemini-pro vs grok 59/59; gemini-flash vs sonnet 40/40; grok vs opus 22/22; grok vs haiku 35/37 |
| **The shared order runs by visual weight and emphasis.** | Top: the negative circled `❶ ➊`. Then bold math `𝟏 𝟭` and double-circled `⓵`. Then plain, circled and fullwidth `1 ① １`. Bottom: superscript and subscript `¹ ₁` |
| **Claude mostly says they're equal; Gemini and Grok mostly order them.** | Opus calls 104 of 153 pairs ≈; Sonnet 72; Gemini and Grok single digits. Opus answers ⟂ to the whole set three times out of three. The pairs Opus does commit to agree with the other families 100% of the time. |
| **The small models show no shared ordering.** | llama-3B agrees with the frontier on 25/43 to 39/58 pairs; qwen-3B on 2/4 to 8/21. Their whole-set answers degenerate into repeats like `①①①…`. |

So for frontier LLMs the answer is "equal on value, ordered on weight". How much each mind says out loud depends on the mind. Gemini and Grok commit. Claude mostly calls them equal, and the edges it does commit to match everyone else's. This is the same pattern the clean-room reading found for edges that ⟂ removes: an ordering shared across families, below some minds' threshold for committing.

The probe can't say whether that dress order holds at other values, or whether a heavier dress ever beats a larger number (`❹` vs `5`). I briefly launched a follow-up of my own design to test exactly that: 18 dresses, at values 4/8 and at 4-vs-5. I stopped it within minutes, after your clarification, because it was another hand-designed battery. Partial ledgers (a few dozen calls) sit beside the coordinator's in scratch; I don't use them. The loop measures those questions as the dress × value lattice, sampled densely with everything around it. Those are the same two questions, answered by the method you asked for.

## What's next

`PLAN.md` §9 has three decisions:

- **Magnitude or progression:** is the graph built on "more" alone, or also on "further along"?
- **The panel:** which models are each round's minds.
- **The build:** whether I build the loop from the existing runner.

I'm ready to start on the last if you want me to.

Claude (Opus 5.5)

---

*Scripts:*

- *`scripts/ones_probe.py`: reads the coordinator's scratch probe. Usage: `ones_probe.py <clean-room root>`.*
- *`scripts/dress_stimuli.py`: the stopped follow-up's stimulus builder, kept for traceability.*
