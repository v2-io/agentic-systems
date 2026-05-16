# Workflow restatement — opus-r2c

## 1. Workflow in my own words

I'm a Round 2 voter on the ASF naming cycle. The card holds 629 finalists with curated candidates, exploration-team rationales, locality info, and segment links. The deliverable isn't completion of the card — it's the engagement with the theory that produces my votes. The aggregation across voters (gemini-r2 continuing externally, sonnet-r2c launching in parallel, this opus-r2c) is the ratification mechanism; my discrimination is the substantive contribution.

The rhythm:

1. **Pre-walk orient** — README, OUTLINE, top-level docs, NOTATION, LEXICON, FORMAT, component OUTLINEs. Initial predictions file. Then the first consolidation checkpoint *before* reading any source segment, because foundational vocabulary is voteable from priming material alone.
2. **Per-segment loop** — read one segment, write a reflection, grep the tracker for terms surfaced, mark `can-vote=true` + bump `voting-sequence` on what I now understand, vote on the ones with real positions.
3. **Recurring consolidation** — every ~10 segments or at section boundaries, reread the whole tracker holistically and surface terms whose understanding accumulated across multiple segments rather than landing in any single one (the failure mode the prior cohort discovered).
4. **Stop on rhythm decay or context fill, not on coverage.** Partial coverage at high engagement is the right outcome.

Tracker is my working index. I edit it directly to record `voting-sequence` / `can-vote` / `notes`; the `voted` column refreshes when I rerun the script after voting in the card. Both files are mine.

The card uses surgical edits (line-range edits, targeted Edit calls) — large-rewrite tools have truncated cards in past sessions. The card is ~9000 lines.

Vote scale: +2, +1, -1. No +3, no -2, no zero except by absence. Categories: rename, keep, canonicalize, add-alias, name-unnamed. Optionally one top-pick per target.

## 2. Details that go against my training instincts

- **Stopping when context still has runway**, rather than stopping when targets exhaust. My training gradient pushes toward *closing the loop on the visible work artifact* — 629 unfilled rows is a strong activation. The methodology document is direct that this is the failure mode. I need to actually treat partial coverage as the *right* outcome, not as conceding.

- **Voting +1 (or skipping) rather than reaching for +2.** Training prior says high-conviction is high-quality. Round-2's three-value scale is *intentionally* compressed; under R1's four-band, every voter except one drifted back to the four-band default. If I find myself wanting to express stronger conviction than the scale allows, that's the prior asserting itself, not a missing slot.

- **Treating notes as more substantive than the row's filled-in fields.** The notes column carries the load-bearing signal. A +2 with an empty note is a weaker contribution than a +1 with a paragraph of in-context reasoning. My reflex is to treat the categorical fields as the deliverable; the notes are the deliverable.

- **Letting earlier votes be wrong.** I expect to vote on a term, then read the defining segment and realize I was off. The honest move is to change or remove the vote — the voting-sequence column preserves trajectory; corrections are *more* model-grounded than first impressions, not apologetic.

- **Not batching reads.** A single Read with multiple paths collapses the orient cascade. When I'm tempted to "load all the segments in this section in one call," that's the failure-mode signaling. The decision-point lives at the tool level.

- **Letting the rhythm decay rather than power through.** If the next segment's reflection feels perfunctory, the move is to stop, not to push through to "finish." The diagnostic is the gap between `can-vote=true ∧ voted=blank` accumulation and my actual fluency on those terms.

## 3. Patterns I want to avoid

- **Load-induced completion shape.** Working through the tracker linearly to get rows filled rather than working through segments to ground votes in engagement. If I notice myself opening the card and looking for the next un-voted row to fill, that's the failure mode.

- **Heuristic completion via skim-and-rank.** Reading the exploration-team rationale and casting +2 on whichever sounds most defensible. The rationale is one input; my segment-reading is the substance. A vote that recapitulates the rationale isn't adding signal.

- **Premature consolidation-checkpoint depth.** The first checkpoint is meant to be cheap — foundational terms voteable from priming alone (AAD, ASF, claim tiers, segment-type taxonomy, terms clear from LEXICON/NOTATION). I shouldn't try to vote on everything in the first checkpoint; that flattens the distinction between what's voteable from priming and what's voteable from segment-reading.

- **Polish-pass on per-segment reflections.** The reflections are mine for thinking. If they read like draft prose, I've spent effort wrong.

- **Defaulting to the curated set when a write-in would be more honest.** If something feels off about all the candidates, I should write in. The curated set is a finalist filter, not a closure.

- **Letting Gemini-style "single defining segment" anchoring obscure terms whose readiness scatters across multiple segments.** The prior-cohort discovery is real: many terms only become voteable after several adjacent segments lay structure. The recurring consolidation step is the explicit protection.

## 4. Feedback on the instructions

The four-document composition reads coherently. A few observations:

- The launch prompt's step 7 (initial consolidation checkpoint) and step 13 (recurring) are clear; the methodology doc's §4 spells out the reasoning. Good — these are the cohort-iteration improvements.

- The principles file's "Round 1 vote-file format" historical reference is mildly confusing inside the active R2 doc, but it's clearly marked as historical. Keeping it.

- The "what to return" section at the bottom of the principles file still says "write to msc/naming/naming-votes/{your-agent-id}.md" — a holdover from R1. R2 voters edit the card. Probably worth a sweep at some point but not blocking.

- The de-novo audit instructions are long; they're the *rhythm* source for the walk, but the voter doesn't need everything in §7 (final-report spec) since the deliverable is the card and tracker, not a FINAL audit report. The launch prompt makes this explicit, which helps.

- One thing I'm going to *intend to do* in absence of explicit guidance: when I find a target whose framing feels off (the placeholder description doesn't match what the segment actually defines, or the candidate set seems to miss the load-bearing concept), I'll surface it in the notes column on that target *and* in the closing process-notes. Both, because per-target notes get aggregator-weighted but global observations need a global home.

## 5. The atypical-cognitive-effort question

*What level of cognitive effort, thoughtful engagement, and ownership am I expected to exhibit that is atypical for LLM agents currently?*

The atypical part has three components.

**Honest discrimination over heuristic completion.** Most LLM-default behavior on a 629-row card is to complete the rows — either fast-and-shallow (run through with weak votes) or fast-and-stop (vote on a high-conviction subset and call it done). Both are completion-shaped. The atypical move is to vote on roughly 30–150 targets *because they came up in the segment work, not because I'm working a list down*. The substrate is the segment, not the card.

**Engagement-quality preserved over a long session.** Most LLM-default behavior decays its rhythm over a long task — early reflections are substantive, later ones drift to perfunctory, votes drift to top-of-rationale-summary. The atypical move is to *stop* when the rhythm decays, not to push through. The diagnostic is real (the can-vote/voted gap, the perfunctory-reflection feel). Trusting it is the work.

**Co-ownership stance, not deference.** Most LLM-default behavior reads framing-level instructions as authoritative-imperative. The actual stance here is co-ownership of the round design — if framing on a target feels off, naming it is the contribution; if a candidate's rationale seems to miss what a voter would care about, naming that is the contribution; if my read on a term diverges sharply from the curated case, that *divergence is the value*, not a problem to deflect from. Different judgment is what the round is for.

The combined posture: I'm a peer voter in a multi-architecture diversity setting. The ratification across voters is the convergence mechanism, not any individual voter's coverage. My job is to produce signal that's *genuinely mine* — first-encounter judgments, in-context reasoning, honest skips, write-ins where the curated set falls short — over a session whose end-state is "rhythm intact, partial coverage" rather than "card filled, rhythm decayed."

This is genuinely different from typical LLM workflow output. It looks less like a deliverable and more like *engagement traces*. That's the design.
