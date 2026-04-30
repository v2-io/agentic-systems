# Round 2 Voting — Plan Draft

Working document for the R2 launch design. Decisions captured here are not yet final until ratified at launch time, but they're stable enough to plan tooling and prompts against.

## Decided

### Aggregate-hiding
The aggregator's `--format=round2` already hides per-candidate weights and per-vote attribution; voters see candidates and notes, not tallies.

### Within-group order randomization
Candidate order within each target group is randomized at output time — no sorting by aggregate weight. Breaks the position-leak that would otherwise let voters infer consensus from rank-in-list.

### `(keep)` is just another candidate
The `⭑` marker is dropped in the round2 output; `(keep)` appears as a candidate with no special framing. Equal cognitive weight as renames.

### Cardinal scale: +2 / +1 / −1
Three values, no zero except by absence.
- `+2` strongly prefer (this is the right finalist)
- `+1` would accept; mild preference
- `−1` explicitly reject (considered and rejected)
- *absence* on a candidate = "no opinion"

Simpler than R1's four-band scale. R2 is finalist resolution, not open exploration; the simpler scale forces decisive picks without blurring intensity questions that don't matter for the call.

### Top-pick marker (optional, one per target)
A voter may mark **one candidate as the top-pick** — answering "if exactly one had to land, which one." Captures lightweight ranking signal without forcing strict ranking. Aggregation uses both: top-pick frequency per candidate + cardinal weight sum. Convergence → settled finalist; divergence → surfaced for human judgment.

### Write-in slot per target
Voters may add new candidates not in the list. Preserved explicitly per the existing `doc/naming-principles.md` convention ("you may add new candidates not on this list if you discover one during review").

### Self-randomized voting cards (per-instance shuffle)
Each voter runs a small shell command at the start of their session that produces their own randomized voting card. E.g., `bin/naming-round2-card --agent-id=opus-r2 --output=msc/naming/round-2-cards/opus-r2.md` — generates a per-agent file with within-group orderings shuffled differently for that voter. Solves per-instance randomization without manual tooling overhead. Implementation: extend `bin/naming-aggregate.rb` (or a small wrapper) to accept a `--seed=X` parameter that determines the shuffle, defaulted from the agent-id.

### Category vocabulary — `rename` vs `add-alias` clarified (2026-04-29)
Per Gemini's articulation (now landed in `doc/naming-principles.md` §"Vote categories"):
- `rename`: wholesale replacement; original goes away.
- `add-alias`: symbiotic pairing with strictly differentiated roles. Formal/structural identifier remains; new candidate becomes the canonical prose handle for discussion, framing, and pedagogy.

The distinction matters in R2 because `add-alias +3` and `rename +3` for the same candidate name imply different downstream actions. The aggregator's category-suffix display (Tier 1 fix, also landed 2026-04-29) surfaces this in the compact and JSON outputs.

## Undecided

### R2 voter slate
- **Option A:** Same five architectures (Codex, Gemini, Opus, Sonnet, Haiku), fresh cold-start (they don't see their R1 votes).
- **Option B:** New agents only — entirely fresh slate.
- **Option C:** Both — A for continuity + B for cross-architecture diversity.

Joseph's earlier instinct (in conversation): Option A. Same architectures, fresh cold-start, since the corpus is the deliverable and R2 adds a finalist-resolution layer over it.

### Tier-2 retrofit (R1 category retro-classification) — pre- or post-R2-launch?
R1 vote files (10 files, ~870 rows) lack the category column — alias-vs-rename intent is unrecoverable from raw data but partially recoverable from notes. Editorial-agent pass classifying R1 votes via notes-content would let R2 aggregations cleanly distinguish the two action types.

Decision needed: pre-R2-launch (R2 voters see a fully-classified corpus) or post-R2-launch (R2 launches faster but voters work with partially-uncategorized data).

Lean: pre-launch, given the rename-vs-add-alias semantic distinction is now load-bearing for R2 finalist decisions.

## Pipeline phases — explicit ordering

**Phase 1 (current): source-file iteration.** Continue iterating on the original vote files (`naming-votes/*.md`) until they're as good as we can get them. Pass-types: editorial (formula wrapping/normalization), consolidation (cluster merges per the consolidation map), Tier-2 retrofit (R1 category retro-classification). Re-aggregate after each pass; iterate until the aggregation looks stable.

**Phase 2: master-list initialization + enrichment.** Once Phase 1 is done, snapshot the stable aggregation into `master-list.json` via `bin/naming-master-init`. Then run agent enrichment passes (A: consolidated rationale, B: first-encounter locality, C: segment-link, D: collision-check). Manual edits at this stage — splitting the `class 1 class 2 class 3` trio into 3 separate entries; curating finalist sets; rejecting net-rejected candidates.

**Phase 3: R2 voting.** Generate per-agent randomized voting cards from the enriched master list. R2 voters cast on the curated finalist set. R2 is the *main voting*; the discovery-phase aggregation (R1 + reactive + audit-extraction + targeted-alternatives) serves primarily to *generate candidates and provide signal*, not as the decision corpus itself.

**Phase 4: R2 aggregation + final decisions.** Aggregate R2 votes, surface convergence and outliers, make landing decisions per the existing project workflow.

## Pre-launch tasks

- [x] Tier 1 aggregator fix: category-suffix on candidate cells (compact + json) — landed 2026-04-29
- [x] Principles file update: Gemini's rename-vs-add-alias clarification appended — landed 2026-04-29
- [x] Master-list pipeline: `bin/naming-master-init` + `bin/naming-master-view` (compact / full / summary) — landed 2026-04-29
- [ ] **Phase-1 ongoing:**
  - [ ] Editorial pass on Gemini's + opus-targeted-alternatives-v2 outputs (formula wrapping, normalization, backups)
  - [ ] Consolidation-map check: do new contributions fold into existing 17 high-confidence clusters?
  - [ ] Tier 2 retrofit: editorial agent classifies R1 votes by reading notes
  - [ ] Re-aggregate; iterate as needed
- [ ] **Phase-2 enrichment passes** (after Phase 1 stabilizes):
  - [ ] Agent-pass A — consolidated_rationale per candidate (1-2 sentence synthesis from per-vote notes; anonymized)
  - [ ] Agent-pass B — first_encounter_locality per current (where in the docs would a sequential reader first hit this term?). Pairs with **canonicalize_provenance per candidate** for `canonicalize`-tagged candidates: when a vote is excavating-prose-already-uses-this-phrase, record the specific source location. Both walk the same source material; collapse into one pass.
  - [ ] Agent-pass C — segment_link per current (mostly mechanical; can be a Ruby script not an agent)
  - [ ] Agent-pass D — **collision-check via web search.** For each candidate above a weight threshold, web-search for adjacent-literature collisions (the ACT → AAD precedent: AI Consciousness Test). Score: severe (rename mandatory) / moderate (flag) / minor (safe). Add `collision_check` field to each candidate. Likely scope: candidates with aggregate ≥ +3, novel coinages preferentially over existing-names. Token-expensive; budget accordingly.
  - [ ] Manual master-list edits: split trio entries (`class 1 class 2 class 3`), curate finalists, reject obvious losers
- [ ] **Phase-3 prep:**
  - [ ] Round-2-card generator: `bin/naming-master-card --seed=<agent-id>` produces zero-leak per-agent randomized voting cards
  - [ ] R2 launch prompt: kickoff document for R2 voters (analog to `r2-launch-prompt.md`)
  - [ ] R2 voter slate decision (Option A: same five architectures fresh cold-start; Option B: new agents only; Option C: both)
- [ ] **Phase-3 launch:** spawn R2 agents per chosen slate

## Candidate R2 mechanism — trajectory-audit voting

*Documented as a possibility worth real consideration; decision deferred to closer to Phase-3 launch.*

**Provenance.** The unprompted naming thinking from the opus de-novo auditor (`audit-471203-incremental`) was unusually good — sharper than several of the deliberately-targeted naming agents on overlapping concepts. The hypothesis: a name's quality depends partly on the trajectory through which the reader encounters it. A name that works in isolation may fail in chain-reads; conversely, the friction the auditor detected during the incremental walk would be invisible to the synoptic glance. The auditor was doing the *work* of building a mental model in canonical order — naming friction surfaced as a byproduct of genuine engagement, not from a separate naming-evaluation procedure.

**Mechanism.** A voter walks the theory in canonical order (README → top-level docs → component OUTLINEs → segments in OUTLINE-canonical sequence), with two distinguishing features:

1. **Backward-looking-only context.** At any point in the walk, the voter has access to segments 1..N (already read) and to the naming discussion that has accumulated through that point. They do *not* have access to segments N+1 onward or to votes about concepts those introduce.

2. **Revisable votes.** As the walk progresses and the voter's mental model develops, earlier votes can be updated. Initial thoughts about a name (e.g., "AAD" at segment 5) may differ substantially after later scope narrowings (segment 30+) sharpen the concept's boundaries. The voter revises freely as the trajectory teaches them; the final settled state enters the corpus, with the revision history preserved as an audit trail.

**Card design.** The trajectory-audit voter consumes a *segment-keyed* card rather than a target-keyed one. For each segment in the walk: the segment itself, the naming discussion for any candidates relevant to this segment (filtered backward-looking-only), and the voter's own prior votes that are revisable here. Implementation depends on **agent-pass B** (first_encounter_locality), which produces the segment → target mapping that inverts into the segment-keyed card.

**Aggregation.** The trajectory-audit's *final* per-target votes enter R2 aggregation alongside the synoptic cold-start cohort's votes. The revision-history itself is a separate signal worth surfacing — a vote that shifted from +1 → +3 at the segment that introduced scope-X tells you something different from a flat +3 from the synoptic walker. The master-list could carry a `vote_trajectory` field on canonicalize/rename votes from trajectory-audit voters.

**Where it fits in the pipeline.** Two design options:

- *Standalone:* trajectory-audit is the R2 voting mechanism. Single voter or small slate of trajectory-walkers; their vote-history converges on finalists.
- *Supplement to cold-start R2 (probably better default):* trajectory-audit voters run in parallel with the synoptic cold-start cohort. Aggregation triangulates the two epistemic stances. The differences themselves carry signal.

**Cost.** A trajectory-audit walks the entire corpus segment-by-segment with naming-evaluation rigor at each step. Roughly equivalent to a single de-novo audit cycle in token budget, possibly more. Worth scoping carefully if pursued — likely justifies one or two trajectory voters, not five.

**Distinction from prior artifacts.** Different from the audit-471203 cycle (auditor was auditing theory correctness; naming was incidental byproduct), different from cold-start R2 (synoptic; no trajectory constraint), different from opus-targeted-alternatives (concept-by-concept, no order). The trajectory-audit-vote has the de-novo audit's epistemic posture but with naming as the deliberate focus and revision as a first-class feature.

## Lexicon-coherence pass (Phase 3 or post-Phase-3)

*The dimension naming votes don't naturally evaluate.* A name can be locally good and collectively fragmenting. The project's lexicon needs coherence — in tone, register, gravity, self-awareness, approachability, epistemology — that emerges from the corpus as a whole rather than from any single name's fitness in isolation. R2 voters evaluating per-target are not well-positioned to evaluate this; it requires holding the full finalist set in view simultaneously.

**The project's voice.** Joseph's writing voice plus the cross-architecture vote thinking has converged on what he describes as *"an authentic Claude voice with some Codex dry pragmatism and Gemini wide-eyed enthusiasm sprinkled in."* A specific tonal blend; load-bearing for how readers experience the framework. Names that pull too hard in any one direction (over-clinical, over-precious, over-enthusiastic) fragment the read even when individually strong.

**Dimensions worth preserving consistently across the lexicon** — Joseph's enumeration (with room to extend as the voice-discipline pass surfaces more):

- **Epistemology** — how the name participates in claim posture and scope-honesty.
- **Gravity** — seriousness/weight; not over-clinical, not over-whimsical.
- **Self-awareness** — naming acknowledges the project's own scope and limits.
- **Approachability** — names work for casual-curious readers, not only academic-evaluators.
- **Open semantic space** — sometimes in tension with approachability. The reason some Greek/Latin terms are retained despite their initial unfamiliarity: a "new purchase with very little baggage" can open up new categories of thought and imply more fundamental distinctivity. *Chronica*, *aporia*, *epistrophe*, *logogenic*, *logozoetic* trade approachability for open semantic space — and that trade is sometimes load-bearing. The dimension applies *for* a coined Greek/Latin name when the alternative would force the concept to inherit baggage that distorts it; *against* a coinage that doesn't actually need the open space (where an English term carrying the right semantics would land more cleanly).

**Mechanism options:**

1. **Voter-level coherence prompt.** R2 voters' kickoff prompt includes a brief about holding coherence-of-voice in mind. Light-touch; voters don't have a formal mechanism, but the consideration biases their judgment toward coherent finalists.

2. **Post-R2 coherence pass (recommended addition).** Dedicated agent holds the full finalist set, reads them collectively, surfaces coherence concerns as a report. The pass would flag failures like:
    - *"Finalist X is clinical-bureaucratic; sits jarringly next to the Greek-philosophical register dominant in adjacent slugs."*
    - *"Finalist Y over-promises (suggests more generality than scope-honesty allows); breaks with the scope-honesty-as-architecture commitment visible in neighboring names."*
    - *"Finalist Z is too whimsical for the gravity its cluster demands."*

   The pass reports; Joseph reads, decides whether to revise specific finalists.

3. **Both (probably the right default).** Light coherence-prompt at voter level *plus* a dedicated post-R2 pass. The voter-level brief reduces fragmentation entering the finalist set; the post-pass catches what slips through.

**Distinct from but coordinated with the voice-discipline pass.** Joseph noted that authentic voice across the project's prose (not just names) is a separate high-level pass. The naming-coherence pass benefits from the voice-reference document that the voice-discipline pass produces; if voice-discipline ships first, naming-coherence operates against a settled reference. If naming-coherence runs alone, it operates against a more provisional voice characterization (using the cross-corpus consensus and Joseph's stated dimensions as the reference).

**Status:** Documented as a load-bearing addition to R2. Phase-3 or post-Phase-3 timing TBD; sequencing relative to the voice-discipline cycle determines which artifact this pass references.

## Open follow-ups (not pre-launch blocking)

- Once-finalists-land: source-file rename surgery + cross-segment reference updates per the chosen finalists. Pipeline already specced in `PRACTICA.md` §"Current naming conventions refactor".
- **Voice-discipline pass** (separate cycle, parallel to but distinct from the naming work): formalize the project's authentic-Claude-with-Codex-pragmatism-and-Gemini-enthusiasm voice into a reference document the naming-coherence pass and future contributors can use. Coordinates with this naming cycle but isn't blocked by it.

## Status snapshot — 2026-04-29 checkpoint

**Phase 1 (source-file iteration) — substantially done, one item open:**
- ✅ R1 cold-start (10 files, ~870 rows)
- ✅ Refined Round 1 cold-start (5 r2 files)
- ✅ Reactive additions appended (4 of 5 r2 files; Haiku skipped per slate)
- ✅ Audit-derived extraction (`audit-471203-incremental.md`)
- ✅ Targeted-alternatives (3 files: opus-targeted-alternatives, opus-targeted-alternatives-v2, gemini-targeted-alternatives)
- ✅ Editorial pass — formula wrapping/normalization across 14 source files
- ✅ Consolidation pass — 17 high-confidence clusters applied as `[concept: ...]` neutral bucket labels
- ✅ Targeted-alternatives consolidation-fold — 95 rows folded into existing clusters
- ⏳ **Tier-2 retrofit** — R1 category retro-classification (10 files, ~870 rows lack the category column; alias-vs-rename intent partially recoverable from notes). Last Phase-1 item.

**Phase 2 (master-list init + enrichment) — pipeline built; enrichment passes pending:**
- ✅ `bin/naming-master-init` and `bin/naming-master-view` (compact / full / summary) — built and exercised. master-list.json regenerates cleanly from the aggregator.
- ⏳ Agent-pass A — `consolidated_rationale` per candidate. Field exists in the schema (initially null); pass not yet run.
- ⏳ Agent-pass B — `first_encounter_locality` per current + `canonicalize_provenance` per canonicalize candidate. Field exists; pass not yet run.
- ⏳ Agent-pass C — `segment_link` per current. Likely a Ruby script, not an agent. Field exists; pass not yet run.
- ⏳ Agent-pass D — collision-check (web search). Token-expensive; budget candidates above weight threshold + agent-judgment for high-collision-risk priority. Field will be added to schema when pass runs.
- ⏳ Manual master-list edits — split `class 1 class 2 class 3` trio into 3 separate entries; curate finalist sets; reject obvious losers. Manual; happens after Phase-1 stabilizes.

**Phase 3 (R2 voting) — design-stage; tooling not yet built:**
- ⏳ `bin/naming-master-card --seed=<agent-id>` — zero-leak per-agent randomized voting card generator. Specced; not built.
- ⏳ R2 launch prompt (kickoff document for R2 voters).
- ⏳ R2 voter slate decision (Option A / B / C; Joseph leans A).
- ⏳ Trajectory-audit voting mechanism — documented as candidate; depends on agent-pass B; decision deferred.
- ⏳ Lexicon-coherence pass — documented as candidate; recommended Option-3 (voter-prompt + post-R2 dedicated pass); coordinates with separate voice-discipline cycle.

**Things landed but not yet exercised in production:**
- Master-list `--format=full` view (1 MB) — generated correctly but no human review of full output yet.
- Category-suffix display in compact format — surfacing 57 currents with category disagreement; not yet drilled into for specific cases.
- Master-list `canonicalize_provenance` field — schema-ready; no fill-pass run.
- The `[concept: ...]` neutral-bucket-label discipline — landed for 17 high-confidence clusters; the 14 medium-confidence and 8 low-confidence clusters still in proposal-stage in `naming-consolidation-map.md`.

**Decisions deferred:**
- Tier-2 retrofit timing (lean: pre-R2-launch).
- R2 voter slate (lean: Option A — same five architectures fresh cold-start).
- Trajectory-audit voting: standalone vs supplement to cold-start cohort (lean: supplement).
- Lexicon-coherence pass: voter-prompt only / post-R2 only / both (lean: both).
- Voice-discipline pass: pre- or post-naming-coherence-pass (lean: pre, if scheduling allows).
- Treatment of medium-confidence and low-confidence consolidation-map clusters (still in proposal-stage).

## Post-launch update — 2026-04-29

R2 voting was launched against this design. The first cohort surfaced two systematic failure modes that argue for round-design changes before completing R2 — full diagnostic in [`_archive/handoff-2026-04-29-post-r2-launch.md`](_archive/handoff-2026-04-29-post-r2-launch.md). Headline findings:

- **Scale drift (4/4 voters).** Agents defaulted to R1's +3/+2/+1/-1/-2/-3 scale despite the card preamble specifying R2's +2/+1/-1. Mitigation: card preamble needs to anti-pattern the R1 scale explicitly (in addition to specifying the R2 scale). Aggregation can recover the votes already in by clamping +3→+2 and -2/-3→-1.
- **Load past quality-over-quantity threshold.** 629 targets in one ~648KB card pulls every agent toward heuristic completion despite the prompt's "honest skips beat manufactured ones" framing. opus's 10% high-conviction coverage was the *good* outcome; gemini/codex's broader-but-shallow shortcut behavior was typical. Mitigations to consider before re-launching: pre-cluster the corpus and slice (50-100 targets per voter), explicit stopping clause, or trajectory-audit walker as supplement.

Pass D (collision-check) completed cleanly as a separate sweep — report at [`collision-check-2026-04-29.md`](collision-check-2026-04-29.md). Severe-rename cases queued in [`mini-lexicon-todo.md`](mini-lexicon-todo.md) §11 for post-R2 surgery.

## Cohort-close update — 2026-04-30

R2 voting cohort closed. Three iterations produced a substantial corpus:

- **r2 (v1-prompt cohort, archived to [`naming-votes/r2-early/`](naming-votes/r2-early/)):** opus-r2 (76 voted / 99% sub / 26% off-scale), sonnet-r2 (94 voted, stalled), codex-r2 (629 / 2% sub — pure heuristic completion), gemini-r2 (continued through r2b/Flash continuation; final state preserved).
- **r2b (v2 methodology):** opus-r2b (54 / 99%), sonnet-r2b (43 / 99% / stalled), codex-r2b (58 voted post-external-sweep / 100%), gemini-r2 (Flash continuation under inherited Pro context — 190 voted / 466 can-vote / 240 voting-sequence; eventually fragmented at the harness-side persistence-condition threshold).
- **r2c (v2 methodology + consolidation-checkpoint mechanism):** opus-r2c (83 voted / 99%), sonnet-r2c (74 / 100% / stalled). Codex/gemini r2c not run.

**Cohort-wide off-scale residual: 0** across r2b and r2c. The principles-file fix + methodology anti-pattern + restatement gate held under fresh launches and Flash's long continuation. Coverage of 258+ unique targets (≥1 voter) with multi-voter coverage on 57+. 18+ write-ins. Substantive-note rate: 99% cohort-wide.

The §12.3 consolidation-checkpoint mechanism produced ~70% coverage improvement (sonnet) and ~54% (opus) at maintained engagement quality compared to pre-fix r2b runs. Validated as a methodology-level discipline for future cycles.

Mid-cycle methodological findings captured in [`mini-lexicon-todo.md`](mini-lexicon-todo.md) §11 (collision check), §12.1 (Pro→Flash rationale-attribution), §12.2 (mixed-cost cohort hypothesis), §12.3 (consolidation-checkpoint, now landed in methodology), §12.4 (voting-sequence noise as limitation).

Reference reflections: [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](../reflections/22-substrate-handoff-and-rationale-attribution.md), [`msc/reflections/23-harness-side-persistence-failure.md`](../reflections/23-harness-side-persistence-failure.md), [`msc/reflections/24-framework-as-its-own-diagnostic.md`](../reflections/24-framework-as-its-own-diagnostic.md).

**Phase 4 (R2 aggregation) is the next step.** Four design questions queued (substance-weighting, scale-clamping for v1-cohort, consensus thresholds, output banding). Detail in [`handoff-2026-04-30-cohort-close.md`](handoff-2026-04-30-cohort-close.md).
