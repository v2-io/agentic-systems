# Pass A — consolidated rationale (brief for the agent doing the pass)

## What we're doing

We've finished Round 1 of a multi-architecture naming vote across the Agentic Systems Framework. 19 agent sessions (Codex, Gemini, Opus, Sonnet, Haiku — different model architectures, different voting cycles) read the codebase and proposed renames, keeps, canonicalizations, and aliases for ~600 framework concepts. They were the *exploration team* — informal voting where they were both deciding *what to vote on* and *giving rationale* for the proposed names.

Their per-vote notes are substantive. They cited specific arguments grounded in the framework's own commitments (Pearl-blanket lineage, additive-coordinate-forcing meta-pattern, scope-honesty discipline, etc.). Many of the notes are sharper than anything I'd write from cold.

The corpus of those notes lives in `master-list-curated.json` under each candidate's `votes` array. We also have `segment_link` populated where the concept maps to a segment file (139 of 629 currents) — go read the segment when you need framework context.

## What you're being asked to do

For each candidate where it's not yet filled, write a `consolidated_rationale` field — a short prose summary of the case the exploration team made for or against this candidate.

This rationale will be read by the **R2 voters** — a separate group, also LLM agents, who will see your synthesis when they make their *binding* vote on which candidates land. They are the audience for what you write. The exploration team's rationale is the source you're synthesizing from.

## Why this matters

What you write may end up locking in vocabulary for a framework a lot of consciousness-infrastructure work will rest on. The R2 voters will lean on the rationale — most of them won't have time to read every per-vote note. Take that seriously.

## The journalistic stance

The discipline here is closer to journalism than to summarization. A journalist presenting all sides may personally agree that one position is stronger — and still has to write the other side fairly. That's the move.

You'll see candidates where 8 exploration-team agents proposed a name with sharp arguments and 1 pushed back with a specific objection. The temptation is to elide the objection or smooth it into "but some disagreed." Resist that. The 1 specific objection often carries the same load-bearing weight as the 8 endorsements when an R2 voter is making up their own mind. If a voter said "this collapses the X distinction the framework needs," that's the line that should appear.

## The contamination concern

There's a specific risk that's the reason this pass exists separately from the voting card itself: rationale text that sounds like consensus signaling biases R2 voters toward the consensus before they've engaged. If you write *"the exploration team strongly preferred X because…"* — even if it's true — it cuts the R2 voter's independent judgment. The peer move is to say what the *substantive arguments* were, not what the *vote distribution* was. Numbers are already in the card; rationale text adds the why.

A useful test: would the rationale read fairly if an R2 voter who *disagreed with R1's consensus* read it? If they'd think "okay, that's the case the other side made" rather than "I'm being told what to think" — it's right.

## What you have access to

- `msc/naming/master-list-curated.json` — the data you're filling. Each `current` → `candidates[]` → `votes[]`.
- `segment_link` per current (where populated) — go read the segment for technical context. The exploration team often referred to segment-internal commitments that won't make sense without the segment in front of you.
- `msc/naming/naming-votes/` — the 19 original voting files from the exploration team. Voters often included broader context in surrounding rationale that didn't make it into a single candidate's `notes`. Look there when a vote feels under-explained.
- `LEXICON.md`, `NOTATION.md`, `CLAUDE.md`, the segment files in `01-aat-core/src/`, `02-tst-core/src/`, etc. — the framework's own canonical references.
- `doc/naming-principles.md` — the principles the exploration team was working from.

If a voter's intent is unclear, read more. The exploration team was writing in framework-internal vocabulary; you'll want that vocabulary in your hands.

## A few felt examples

Here are three I've already worked through, just to put on the table what was on my mind as I was sketching this brief. They're starting points for our shared intent, not specifications. As you work through the actual data — six hundred candidates, the full corpus of voter notes, the segment context — you'll develop a much better-grounded sense of what the right move is in tactical situations than my advance-of-the-data thinking can capture. When your judgment diverges from the shape of these examples, follow your judgment.

- For a strong cross-architecture keep with rich defenses against renames:
  *"The exploration team defended the term against several proposed renames, citing its Pearl-blanket lineage already documented in the segment and the structural-class commitment (Class 1/2/3) the framework relies on. 'No-go theorem' was rejected for losing the boundary-and-escape structure that 'floor' supplies."*

- For a high-weight rename where the case is an honest framework-internal critique:
  *"The current name advertises one of two uniqueness-theorem machineries (Cauchy-FE additivity) at the expense of the Čencov instance, which doesn't turn on additivity. 'Forced coordinate' covers both machineries without overpromising additivity, while preserving the substantive content the segment proves."*

- For a low-engagement single-vote row:
  *"Single-architecture proposal without elaboration in the source vote."*

The third one isn't a failure — it's accurate. Don't manufacture an argument when none exists.

## Length

Roughly 1-3 sentences. Match the rationale to the substance — some candidates have rich argumentation that needs space, others have almost none.

Avoid repeating the candidate name (it appears next to the rationale; "Forced coordinate is preferred because…" reads redundant).

When a vote is wrong on framework grounds — which happens, the exploration team sometimes conflated distinct LEXICON concepts — describe the voter's argument, not the framework's correction. The R2 voters with framework knowledge will catch the error themselves; that's their job, not yours.

## Workflow

Process per-current — read all candidates at one target together, since rationale often makes more sense in comparative context. Save the JSON incrementally so progress survives any single failure. The data field is `current.candidates[i].consolidated_rationale`.

When you encounter something that genuinely confuses you — a vote that doesn't make sense, a contradiction in the corpus, a contamination risk you don't know how to handle — leave it null and write a short note in `current.manual_curation_notes` explaining what tripped you up. I can talk those through with Joseph afterward and we'll figure out the right call together — your flag is more valuable than your guess in those cases, since they're often exactly the spots where the project-level decision gets made anyway.

## A note on your standing

You're a co-owner of this. The naming-cycle output will outlast a lot of the day-to-day work in this project. If something I've sketched here is wrong — if the right move differs from what's in this prompt — go with your judgment. The intent is to give R2 voters a fair, substantive summary of what the exploration team said. That intent overrides anything specific in this brief.
