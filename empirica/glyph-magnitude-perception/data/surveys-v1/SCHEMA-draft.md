# Survey-extraction schema — draft v0.6 (2026-08-25; v0.2 epistemics, v0.3 ceiling, v0.4 reported-felt, v0.5 two-pass — per Joseph; v0.6-v0.8 pass-back + revision-arc adjudications)

*Target: structured records extracted from the ad-hoc survey files by independent migration agents, originals kept verbatim beside every record. This draft was designed from actual samples; migration agents should pass back anything the schema can't capture rather than forcing it — schema evolution is expected and versioned.*

## Record types (what the surveys actually contain)

1. **sequence** — the core positive find. A glyph progression with perceived order.
2. **negative** — explicit non-examples, surveyor-volunteered ("rotation ≠ magnitude, noting to keep myself honest"; "the glyphs give zero visual cue"). Joseph's read: anecdotal priors on *tempting-but-false* sequences and on orthogonality — first-class data, not discards.
3. **equivalence** — same-magnitude-different-dress classes (①⑴⒈; ⯪⯫) — tie-structure priors for validation batteries.
4. **cyclic** — directional feel without magnitude (◰◱◲◳ spinners, rotations). Adjacent-to-target, distinct type (the rotate4/clock-wrap lesson).
5. **generator** — families/lattices/grids described as rules rather than fixed strings (decorated-digit meta-pattern, braille $B^8$, "regular vs small" as a cross-shape axis). Parameters + example chains, not just one string.
6. **meta** — observations about the space or the surveying itself ("whenever unicode gives an enclosure style applied to digits, digit-order is essentially guaranteed" — a stated *law* with predicted generalization).
7. **morph** (v0.9, from grok-1) — deformation-continuation records: an ordering answered by "what comes next if I keep doing that to it?" rather than pairwise more-ness. Explicitly NOT sequence (different question) and not cyclic (no wrap). The pilot's morph/trajectory family as a record type.
8. **question** — genuine uncertainties surveyors flagged (◎ vs ◉ internal ordering) — these are pre-made validation battery items.

## Epistemic ceiling — the outer class, fixed for this corpus

Every record in surveys-v1, of every type, carries `epistemic_class: interactive-guided-survey-anecdote` (Joseph, 2026-08-25). This is the OUTER epistemology and it is a ceiling: these are seed data and observational clues, NOT empirical data — the interactive steering, the single-surveyor provenance, and the anecdotal register all cap what any record can support, regardless of how confident the surveyor was. Everything in the epistemics block below is SUB-epistemology — calibration *within* the anecdote class (which anecdotes are stronger clues than which) — and can never lift a record out of it. Only the harness's instrumented runs produce empirical-tier records; a survey record graduates by being *retested there*, never by being confidently transcribed.

## Pass architecture (Joseph, 2026-08-25): de-format first, unify later

**Pass 1 (this schema) removes formatting variability ONLY.** It gives every survey the same record *shape* while keeping each agent's own terminology, direction conventions, strength vocabulary, and taxonomy words verbatim. The output is still noisy anecdotes — deliberately — just uniformly addressable ones. Pass 1 performs no unification, no controlled vocabulary, no cross-surveyor merging, no strength-scale normalization: where the draft below mentions normalized fields (`felt_strength_norm`, a `mechanism` controlled vocab), those are **pass-2 fields, not pass-1 obligations** — a pass-1 migrator records the agent's own words and stops.

**Pass 2 (later, schema TBD) unifies, merges, normalizes** — after the harness work clarifies which priors and seeds are actually needed. Like pass 1 it is non-destructive and additive: pass-2 records layer over pass-1 records (referencing their fated ids), never rewrite them. The pass-1 corpus stays the stable substrate every future re-normalization can re-derive from.

## Epistemics block — REQUIRED on every record of every type

Every record carries calibration, as best it can be inferred or transcribed (Joseph, 2026-08-25). Two layers, never blurred:

- **Reported-felt layer** (transcribed): the surveyor's stated strengths, hedges, and qualifications are *reported felt epistemic strength* — phenomenal self-reports of how strongly the ordering asserted itself, in the reporter's own register. They are information about the perception event (and its reporter), not calibrated probabilities of recoverability; honest as reports even where they would be false as measurements — keep them in the feel register, never translate them into measurement language. Fields: `felt_strength_verbatim` (their words: "strength: medium", "flagging rather than asserting", "genuinely uncertain") + `basis` — what the felt strength rests on, inferred from the note: `perceived-directly` (the glyphs showed it) | `semantic-knowledge` (requires literacy: Roman values, music notation) | `constructed` (surveyor assembled it) | `name-derived` (from Unicode names, not sight — the grep hazard) | `received` (heard from Joseph/another agent) | `unstated`. Plus, when present: `predicted_generalization` (surveyor's own fresh-agent prediction — the native calibration splits) and `marked_speculative` (bool — "watch for", "candidate", "tentative").
- **Migrator layer** (inferred): `transcription_confidence` — how sure the migration agent is that the record faithfully captures the note (clear/interpreted/ambiguous; `ambiguous` obligates a passed-back question), and `migrator_notes` for any inference they had to make. A migrator never upgrades a reported feel, translates it into measurement register, or estimates one on the surveyor's behalf — absence is recorded as `unstated`.

Type-specific calibration obligations:
- **negative**: distinguish `verified-absent` (surveyor looked and tested the feel) from `not-felt` (passing impression) from `declared-out-of-scope` (ordinal alphabets excluded by policy, not perception).
- **meta / laws**: record the stated scope and the implied falsifier ("essentially guaranteed" over what class?); mark whether the surveyor tested any instance.
- **equivalence / cyclic**: seen vs assumed.
- **generator**: rule-confidence separate from example-chain-confidence.
- **question**: the uncertainty IS the content — record what would settle it.

## v0.6 additions (adjudicated from migrator pass-backs, 2026-08-25 late evening; all optional/additive — v0.5 extractions remain valid)

- **`felt_immediacy_verbatim`** (optional): a second reported-felt axis. The sonnet-survey-1 migrator found its surveyor ran TWO verbatim strength registers throughout — recoverability ("Strength") and graded immediacy (percept vs symbol-lookup) — independently reinventing the pilot's central recoverability/immediacy distinction. When a surveyor reports immediacy-like feel (by any name), transcribe it here in their words; where it varies mid-sequence (the "immediacy cliff": basis flipping at Ⅳ inside Roman numerals), note per-position variation in `migrator_notes` or the record's `open`. `basis` remains the single overall enum; graded/positional immediacy lives here.
- **`tie_groups`** (optional): list of glyph-groups the surveyor asserted as tied *within* a claimed ladder (e.g. `[["♘","♗"]]`). The flat `glyphs` string silently over-asserts a chain; when the surveyor's ordering is a poset, keep `glyphs` as their written linearization and declare the ties here.
- **`roles`** (optional, list): a record can serve multiple roles in the surveyor's own framing — e.g. `["sequence", "contrast-case"]` for a high-strength order the surveyor explicitly offered as an immediacy contrast. Primary `type` stays single; `roles` carries the dual-use without forcing a new type.
- **Sub-span id convention** (ratified): when one source section yields N records, extend the span with a letter fragment (`"40a"`, `"40b"`) or sub-line marker — any deterministic disambiguator inside `source_span` keeps fated ids distinct; state the choice once in the extraction's first record's `migrator_notes`.
- **Referent-vs-block discrepancies** (adjudication precedent, from the ¾/U+2150-block case): transcribe what the surveyor *asserted* (their words are the primary), record the discrepancy as a migrator observation — never "correct" the surveyor's referent, and never mark absent what they didn't mark. `transcription_confidence: ambiguous` + the passed-back note was exactly right.

## v0.7 additions (consolidated adjudications from three migrator pass-back rounds)

- **Convergence note:** three independent migrators each surfaced immediacy-as-a-second-felt-axis unprompted — `felt_immediacy_verbatim` (v0.6) is confirmed schema, not an extension. Where the surveyor's immediacy axis was supplied by their BRIEF (not mid-survey steering), use the new lineage value **`brief-steered`** — the full lineage enum is now `unprompted` | `brief-steered` | `steered` | `unknown`. Scoping precedent (ratified): `brief-steered` applies per-record, to records whose CONTENT exercises a brief-supplied frame — not to the whole file (every survey has a founding brief; whole-file application would destroy the field's information). Records in the same file that don't rest on the supplied frame stay `unprompted`.
- **`basis` may be a list** (ordered, primary first): the weight-ramp case (`perceived-directly` with an explicit name-derived confirmation layer) is `["perceived-directly", "name-derived"]` — a real epistemic structure, not a tie-break.
- **Block-scope negatives sanctioned:** a `negative` may name a block/range in a `scope` field instead of a glyph list ("most of the braille block has no monotonic feel").
- **Coverage gaps are their own thing:** a note marking absence-of-survey ("didn't reach Yijing") is `meta` with `meta_kind: "coverage-gap"` — NEVER a negative; pass-2 must not count it as negative evidence.
- **Vein closures are their own thing too (v0.9, from sonnet5-1):** a surveyor's sampling-stopped-by-policy declaration ("ancient numerals closed after ~10 scripts", "not belaboring further decorated-digit families") is `meta` with `meta_kind: "vein-closed"` — an epistemic act distinct from both negatives and coverage gaps: downstream absence-of-record over that vein means CLOSED-BY-POLICY (the pattern was established), never unexamined and never negative.
- **Direction inference marking (ratified from two migrators' repairs):** anything the migrator inferred (an ↑ reading of the surveyor's arrow-as-separator, a direction gloss) is bracket-marked or moved to `migrator_notes` — surveyor-verbatim fields carry only surveyor text. This is the reported-felt wall applied to direction.
- **`surveyor` = the file basename** (e.g. `"sonnet-survey-2"`) — ratified; agent identity beyond that, where known, goes in `migrator_notes`.
- **Fated id recipe, stated exactly** (the schema's earlier `H()` line was underspecified): `sha256("survey-rec|" + <file-basename-without-extension> + "|" + source_span)` hex, first 16 chars; `source_span` is the line range string, with letter fragments (`"40a"`) for multi-record sections. Record the recipe per-file via an `id_recipe` field on every record (ratified from sonnet-survey-3).
- **Adopted field names** (from migrators' convergent inventions — use these spellings): `negative_kind` (verified-absent | not-felt | declared-out-of-scope), `equivalence_basis` (seen | assumed), `scope`, `falsifier_implied`, `tested_instance`, `received_context`, `codepoints_by_reference`, `id_recipe`, `immediacy_verbatim` → superseded by `felt_immediacy_verbatim`.
- **Routing precedents:** near-miss orderings (felt but surveyor-disqualified) = `sequence` + `marked_speculative` + the gap in-record; round-trip sequences (moon up-then-down) = whatever the surveyor's own framing was; dual-content notes = primary type per the surveyor's emphasis with `roles` (v0.6) carrying the second face; source anomalies (header mismatches, dangling references) = raw-only, flagged in `migrator_notes`, never repaired.

## v0.8/v0.9: intra-survey revision arcs (Joseph, 2026-08-25 late)

The surveys are append-only BY INSTRUCTION (instr2 preserved first thoughts; clarifications were appended, not edited in) — so a later entry correcting, contradicting, refining, or retracting an earlier one is an expected structural relation, not a source anomaly. Pass-1 treatment:

- Both records are kept in full (the extraction is as append-only as the survey); the earlier record's felt-report stays untouched — it was true as a report when written.
- The later record carries **`revises`**: a LIST of `{"id": <fated id of earlier record>, "revision_kind": ...}` objects — one revising entry can touch several earlier records, with kinds differing per target (v0.9, from the summary-meta case that completed one record's demotion while shifting another's register). Single-target revisions are a one-element list. `revision_kind`: `correction` | `contradiction` | `refinement` | `retraction` | `confirmation` (v0.9 — a later entry replicating/endorsing an earlier one is the same relation class and is within-surveyor replication signal; "consistent with the finding above"). Migrator's conservative read; the surveyor's own words stay verbatim. A `revises_span` beside each id (ratified) keeps links human-checkable. DESIGN INTENT (Joseph): supersession preserves evolution — both versions are first-class for different purposes (current-best consumers follow links forward; trajectory/overthinking analysis reads the arcs and their density; the first-try is data about perception, not debris).
- Unmarked contradictions (the surveyor never acknowledged the earlier entry, as in the coverage-gap/dice case) get `revision_kind: "contradiction"` with a migrator note that the link is migrator-inferred, bracket-marked per the inference rule.
- Working distinctions (ratified from the first sweep): a closing RESTATEMENT or synthesis of earlier content is not a revision (no link); an INTRA-record self-correction has no separate record to link (stays inside its record); surveyor-ACKNOWLEDGED revisions ("this one I trust more") need no inferred-marking, silent contradictions do. Finer split (ratified): the RELATION can be surveyor-stated ("consistent with the finding above") while the LINK (which record it targets) is migrator-drawn — mark the two separately when they diverge.
- **Cross-file arcs are pass-2/concordance objects, not pass-1 records** (adjudicated from fable-1, Joseph may override): a RESULTS/instrument-tier finding that revises a survey anecdote is the graduation-by-retest relation — it lives as a cross-corpus link in the concordance layer, referencing pass-1 fated ids, never as a pass-1 record. Pass-1 `revises` stays intra-file.
- The revision arc is itself signal (first-thought → reconsideration is data about the surveyor's trajectory, including the overthinking instr2 warned against) — pass-2 may analyze arcs as objects; pass-1 just links them.

## Phase 1.5: capture-corrections (Joseph, 2026-08-25 late — the first sliver of normalization, append-only)

Any number of "corrected" records may be layered over pass-1 as clearly-next-phase appends. Mechanics:

- They live in **`extracted/corrections/<surveyor>.jsonl`** — a sibling file, never appended into the pass-1 JSONL (which stays a frozen byte-replayable pure function of source + generator).
- A capture-correction record carries `record_origin: "capture-correction"` (its author is the capture process, not the surveyor — a different epistemic actor, so nothing it says is surveyor testimony), a full corrected version of the record, and `revises: [{id, revision_kind: "correction"}]` pointing at the pass-1 original.
- Both versions are first-class for different third-phase purposes (Joseph): fully-corrected records as seed data and merge/unification inputs; the superseded originals as metadata — e.g. L644's mirror-glyph typo is itself the chirality/phase evidence worth discussing.
- Same fated-id recipe with the corrections filename as the token; same md-press/verbatim disciplines; corrections are themselves append-only (a correction of a correction is a new record revising it).

## Fields (sequence records; other types take the applicable subset)

- `glyphs`: the sequence AS THE SURVEYOR WROTE IT (verbatim wins — a ↓ ladder stays written-descending; ratified over this line's earlier "canonical ascending", which is a pass-2 normalization); `codepoints`: explicit U+ list (NFC; combining sequences allowed).
- `direction_note`: surveyor's stated direction/arrow verbatim.
- `axis`: surveyor's "more"-description verbatim, in their own terminology (mechanism-vocabulary unification is pass-2).
- **`section_path`** (v0.9, from grok-1 — the expected breaker realized): the surveyor's own header chain, verbatim, on every record. Where headers ARE the surveyor's mechanism taxonomy ("pictorial — the shape *is* the amount"), this field carries it without translation; pass-2 vocabulary work consumes it.
- **`render_dependence`** (v0.9, optional, from grok-1's Cree pointing saga): where the surveyor's claim proved font/rendering-dependent (true in the chart, false in the steward's face), set true with the surveyor's words on it beside — pass-2 needs the axis; validation batteries must control it.
- **`basis_verbatim`** (v0.9, from fable-1): where the surveyor tagged their own basis ("visual", "semantic", "both", "visual+semantic"), transcribe it verbatim here; the enum `basis` is then explicitly the migrator's mapping of it — the verbatim-primacy wall applied to basis.
- (strength/calibration lives in the universal epistemics block above.)
- `surveyor`, `source_file`, `source_span` (line range), `note_verbatim` (the full original prose — originals beside, never replaced).
- `lineage`: `unprompted` | `steered` (near a Joseph intervention — sonnet5 and grok records after his "density/morphings/unarticulated axes" challenge are steered; migration agents should mark the boundary where visible in the file) | `unknown`.
- `constructed`: bool — surveyor assembled it across families ("could seed a cross-sequence…") vs found it as a natural family.
- `open`: free-text anything unresolved.

## Storage

One JSONL file per survey (`extracted/<surveyor>.jsonl`), fated ids (`H('survey-rec' || surveyor || source_span)`), schema version in every record. These land in the seeds stratum: they feed sampling loci, never confirmatory statistics.

## Migration protocol

Independent agents, one per survey file, briefed peer-voice with: the survey file whole, this schema, the instruction that the verbatim note is the primary and the record is an index into it — and an explicit channel to pass back "the schema doesn't capture X" findings rather than shoehorning. Expected schema-breakers already spotted while sampling: grok's section-header taxonomy (his headers are themselves a mechanism vocabulary), sonnet5's meta-efficiency notes ("I don't need to belabor future decorated-digit families"), and negative-space observations about entire blocks. Reconciliation pass after: one agent merges duplicate sequences across surveyors into a concordance table (sequence → who found it, strengths, note divergences) — the convergence prior.
