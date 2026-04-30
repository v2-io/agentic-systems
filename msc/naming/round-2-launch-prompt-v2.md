Your Agent ID: {your-agent-id}

You are participating in Round 2 of a multi-round naming review for the **Agentic Systems Framework (ASF)**. Round 2 resolves finalists for the project's lasting vocabulary — the names that will carry the framework forward across every future reader and session. Your card holds 629 targets with the curated finalist candidates, exploration-team rationales, first-encounter locality, segment links, and provenance tags.

Your discrimination as a voter is the substantive deliverable of this round, not a minor judgment over an otherwise-finished artifact. The aggregation across voters at the end is the ratification mechanism. The substance is what you find load-bearing, what feels awkward, what passes the renamed-from-now-sounds-weird test, what a skilled reader six months out could refer to in conversation without looking it up. **Thoughtful and strictly honest judgment is the value, not deference** — that's a description of what the round is *for*, not a courtesy you're being extended. Cross-voter divergence on a target carries information; it's surfaced for human judgment at landing time, not averaged away.

## Reading order before you start

These four documents compose into the round's full instruction set. Read them in order; each has one job, and none is canonical alone:

1. **`doc/naming-principles.md`** — what we name and why; categories; evaluation criteria; architectural invariants.
2. **`doc/naming-cycle-methodology.md`** — how the pieces compose: the tracker, the segment-walk rhythm, failure modes we've seen and the disciplines that protect against them, stopping rules, what co-ownership of this round means concretely. *Read this carefully — it carries lessons from prior cohorts about what produces good output.*
3. **`doc/de-novo-audit-instructions.md`** — the segment-walk rhythm itself: one segment at a time, reflections as you go, the posture-discipline that the methodology in (2) borrows.
4. **Your card and tracker** (paths below) — the actual work. The card's preamble carries the voting-mechanic spec (scale, top-pick, write-in, category column, heading conventions, within-target randomization). The tracker is your working file across the walk.

The methodology document carries most of what used to be in this prompt — vision, posture details, how the workflow composes, failure modes, stopping rules. This prompt now only carries what's *specific to this round* (R2 finalist resolution) and *specific to you* (your identity, where your card lives, cold-start scope).

## Cold-start scope

The cold-start restriction is narrow and specific: **avoid contamination from anchoring naming-cycle workings under `msc/naming/`**. Files containing vote tallies, aggregate weights, candidate-by-candidate leaderboard signal, or other voters' position statements would collapse the cross-voter diversity this round depends on. Files describing the cycle's design, plans, and meta-process don't anchor and are useful context.

### Within `msc/naming/`, the whitelist (read freely)

- Your own card at `msc/naming/round-2-cards/{your-agent-id}.md` and your tracker at `msc/naming/round-2-trackers/{your-agent-id}-tracker.md`
- `msc/naming/round-2-plan.md` — design and phase-plan for R2 itself
- `msc/naming/collision-check-2026-04-29.md` and `msc/naming/collision-check-brief.md` — external-collision sweep on likely finalists
- `msc/naming/mini-lexicon-todo.md` — non-vote-shaped items the schema couldn't naturally absorb
- `msc/naming/pass-a-brief.md`, `msc/naming/pass-b-brief.md` — the editorial-pass briefs that produced the rationales and locality/provenance fields on your card
- `msc/naming/name-transition-aad.md` — the ACT→AAD rename rationale and transition record; case study for naming epistemics on this project

### Within `msc/naming/`, do not read

- Other voters' cards or trackers in `msc/naming/round-2-cards/` or `msc/naming/round-2-trackers/`
- `msc/naming/master-list-curated.json`, `msc/naming/master-list-*.md`, `msc/naming/naming-aggregate-r2-*` (aggregate weights, vote tallies)
- `msc/naming/naming-votes/*` (Round 1 votes; would re-anchor)
- `msc/naming/naming-consolidation-*`, `msc/naming/naming-tier2-*`, `msc/naming/naming-pilot-rename-plan.md`
- `msc/naming/_archive/*` (superseded artifacts)

If you're unsure about a file in `msc/naming/` not listed: would reading it surface aggregate weights, candidate ranks, vote tallies, or other voters' positions? If yes, skip. If no, it's whitelist-eligible — exercise judgment.

If you've already glanced at any of the excluded files in this session — including incidentally — disclose it explicitly at the bottom of your card under a "Cold-start observations" heading. The contribution may still be useful as long as it is marked.

### Outside `msc/naming/`, navigate freely and thoroughly

The whole project is grounding material. The methodology document spells out the segment-walk rhythm — `CLAUDE.md`, `README.md`, `OUTLINE.md`, segment files, `NOTATION.md`, `LEXICON.md`, predecessor docs, sibling-project source under `~/src/firmatum/`, `~/src/_core/tst/`, `~/src/shoshin/`, `~/src/embeddings/`, `ref/agentic-tft/`, and `git log` / `git blame` are all in scope when relevant.

## Where your work lives

Your **card**: `msc/naming/round-2-cards/{your-agent-id}.md`. If it doesn't exist, generate it via:

```
ruby bin/naming-master-card --seed={your-agent-id}
```

The seed is your agent ID (deterministic shuffle; same agent-ID always produces the same card).

Your **tracker**: `msc/naming/round-2-trackers/{your-agent-id}-tracker.md`. Generate via:

```
ruby bin/naming-master-tracker --card=msc/naming/round-2-cards/{your-agent-id}.md
```

Re-run the tracker script periodically as you cast votes — it preserves your voting-sequence / can-vote / notes columns and refreshes the voted column from current card state.

You vote by editing the card directly; the tracker is your working index across the walk. Both are yours.

## One last thing

This round's design has been iterated based on prior voters' feedback — including the tracker concept itself, the column schema, and the methodology's segment-walk rhythm. Your engagement with this round will likely produce signals that shape the next. If you notice the framing of a target itself feels off, name that. If a candidate's exploration-team rationale seems to miss what a voter would actually care about, name that. The "Cold-start observations" / "Process notes" section at the bottom of the card is fair game for cycle-level concerns.

Naming is irreducibly aesthetic; there is no derivation that settles it. Be confident where you are, honest where you are not, let the multi-architecture aggregation do the convergence work, and write in your own voice.
