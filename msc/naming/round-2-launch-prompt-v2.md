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

## Your first action — workflow restatement

After you've created your audit working directory and finished reading the four documents above, but *before* you begin the walk itself, write a workflow restatement at `msc/AUDIT-WORKING-<your-id>/00-workflow-restatement.md`. Section 3 of the methodology document specifies what it covers — including a self-articulated answer to *"What level of cognitive effort, thoughtful engagement, and ownership are you expected to exhibit that is atypical for LLM agents currently?"* This file is the gate between reading and working; voters who skip it or approach it as a checkbox reliably hit the failure modes the methodology warns about.

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

## Your expected course

As per all of the instructions above, your expected course will be:

### Pre-walk (one-time setup)

- [ ] **1. Read the four instruction documents** in the order given in "Reading order before you start" above: [`doc/naming-principles.md`](../../doc/naming-principles.md) → [`doc/naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) → [`doc/de-novo-audit-instructions.md`](../../doc/de-novo-audit-instructions.md) → this launch prompt.
- [ ] **2. Create your audit working directory** at `msc/AUDIT-WORKING-NNNNNN/` (six random digits of your choice; pick anything, just avoid existing-directory collisions). Per [`doc/de-novo-audit-instructions.md`](../../doc/de-novo-audit-instructions.md) §"Before you begin: create your audit-working directory."
- [ ] **3. Write your workflow restatement** at `00-workflow-restatement.md` in your working directory, covering the five components specified in [`doc/naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) §3 — including a self-articulated answer to *"What level of cognitive effort, thoughtful engagement, and ownership are you expected to exhibit that is atypical for LLM agents currently?"* This is the gate between reading and working.
- [ ] **4. Orient to the project at the README level.** Unlike a full auditor (who reads [`README-auditor.md`](../../README-auditor.md) to avoid priming on findings / recent progress / known issues), you may read [`README.md`](../../README.md) directly — the priming content is useful to voters because the round's substance *is* the project's actual concepts. The auditor variant remains an option if you prefer the leaner orientation.
- [ ] **5. Orient to the rest of the top-level files and OUTLINEs as appropriate.** [`CLAUDE.md`](../../CLAUDE.md), [`OUTLINE.md`](../../OUTLINE.md), [`PRACTICA.md`](../../PRACTICA.md), [`NOTATION.md`](../../NOTATION.md), [`LEXICON.md`](../../LEXICON.md), [`FORMAT.md`](../../FORMAT.md), and the per-component outlines ([`01-aad-core/OUTLINE.md`](../../01-aad-core/OUTLINE.md), [`02-tst-core/OUTLINE.md`](../../02-tst-core/OUTLINE.md), [`03-logogenic-agents/OUTLINE.md`](../../03-logogenic-agents/OUTLINE.md), [`04-logozoetic-agents/OUTLINE.md`](../../04-logozoetic-agents/OUTLINE.md)). Sample what helps; don't try to read everything.
- [ ] **6. Write your initial predictions** at `00-initial-predictions.md` in your working directory, per [`doc/de-novo-audit-instructions.md`](../../doc/de-novo-audit-instructions.md) §4.1. Concrete enough to be falsifiable.
- [ ] **7. Run your first consolidation checkpoint** *before* reading any source segment. After the orientation reads in steps 4-5 you'll already understand some terms well enough to vote on them — framework-name acronyms (`AAD`, `ASF`), foundational vocabulary, claim-tier and segment-type taxonomy, terms whose definitions are clear from `LEXICON.md` and `NOTATION.md` alone. Read the entire tracker holistically (it's small — about 50KB), identify these, bump `voting-sequence` + mark `can-vote=true` for each, and cast votes immediately (if you have a real position) or leave the can-vote/voted gap and come back later. Per [`doc/naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) §4 ("Periodic consolidation checkpoints"). This is the cheapest checkpoint with the highest yield-per-effort and surfaces foundational targets that the per-segment grep-loop in step 10 below will structurally miss.

### The walk (per-segment loop)

- [ ] **8. Read *only* the very next single segment** (in OUTLINE order, modulo the appendix-back-pointer exception in `de-novo-audit-instructions.md` §4.2). One at a time, not batched. The "wanting to batch" pull is the failure mode the rhythm exists against.
- [ ] **9. Write your between-segment reflection** as a numbered file in your working directory (e.g., `12-deriv-discrete-sector-condition.md` for the 12th segment you've read), per [`doc/de-novo-audit-instructions.md`](../../doc/de-novo-audit-instructions.md) §4.4. The 14 reflection prompts there are guides; substance over completion.
- [ ] **10. Scan your tracker for terms surfaced in the segment** — `grep` for the actual term or concept (using spaces, the way they appear in the tracker's third content column) in `msc/naming/round-2-trackers/{your-agent-id}-tracker.md` is usually enough. Targets where this segment is the term's defining home are the highest-leverage votes; targets where the segment merely mentions a term in passing are weaker — wait for the defining segment.
- [ ] **11. For each surfaced target you have a real position on:** mark the next `voting-sequence` integer and `can-vote=true` in your tracker, jump into your card by row number, and cast the vote with substantive in-context reasoning in the notes column. Use surgical file edits (targeted replace, line-range edits) not bash/cat-style rewrites — the card is large and large rewrites have truncated cards in past sessions.
- [ ] **12. Resync the tracker periodically** by running `ruby bin/naming-master-tracker --card=msc/naming/round-2-cards/{your-agent-id}.md` — this refreshes the `voted` column from card state while preserving your voting-sequence / can-vote / notes edits.
- [ ] **13. After every ~10 segments or at natural part/section boundaries: run a recurring consolidation checkpoint.** Same shape as step 7 — read the tracker holistically, identify items now voteable that the per-segment grep had missed, and earlier votes where new understanding may want revisiting (raise/lower weight, change category, or remove). Mark `can-vote` + bump `voting-sequence` for new ones; cast immediately or defer per the rhythm. Per [`doc/naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) §4. The 2026-04-30 cohort discovered (across two voters who returned to consolidate post-walk) that this captures dozens of foundational targets the per-segment loop structurally misses — running checkpoints *during* the walk rather than only at the end keeps the in-flight `can-vote`/`voted` gap from accumulating into a backlog.
- [ ] **Loop back to step 8** until context fills or rhythm decays. Partial coverage with high engagement is the right outcome; full coverage at decayed engagement is the failure mode to avoid.

### When you stop

- [ ] **14. Write your closing observations** in your card's "Cold-start observations" / "Process notes" section at the bottom — anything cycle-level worth surfacing for the round design (per [`doc/naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) §6). Targets where the framing felt off, terms whose defining segment didn't match the card's framing, gaps in the candidate set, observations about the rhythm itself — all in scope.

**You are not writing a final audit report.** The de-novo audit instructions describe one (`§7`); voters in this round borrow the audit *rhythm* but the deliverable is your card and tracker, not an `audits/audit-NNNNNN-FINAL-*.md` document. Your engagement and your votes are the contribution.
