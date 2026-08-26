# Scale-up design — complete walk, recycling loop, paper-grade verification

*Drafted 2026-08-25 from the pilot session (see sequences.md for the full experimental arc). Status: proposal for Joseph; nothing here is built yet except where noted.*

## What is debugged (survived a measured challenge)

- Triad unit: 3 pairs × both orders, reverse cycles split across two independent judges (cycle rate 1–2% at Sonnet = local transitivity; the split defeats coherence-construction).
- Response set: glyph-echo + graded `by` (somewhat/much/vastly) + ≈ (equal-on-axis) + ⟂ (no ordering). ⟂ measured as removing ~80% manufactured edges. Distance antisymmetry 100% within judge, 96% within-1 across judges.
- Both-orders presentation (kills side bias; 3B P('>')=85% pathology caught).
- Gestalt reconstruction with noise foils (36/36 honest ⟂ on foils) — the only instrument that sees holistic sequences.
- Motion-continuation without articulation (unlocks confounded axes; ~4-glyph onset).
- Salted membership validation (blind lookalike distractors; boundary = axis ∧ family).
- Stateless ollama replication (per-call independence; strictest protocol instantiation).

## Must fix before any big run

1. Stimulus/response collision: ban ≈, ⟂, and answer vocabulary from stimulus pools.
2. Echo-parse loss (14% at 3B): add index labels (A/B) as answer fallback alongside echo.
3. Salt insertion: seeded-random positions, not deterministic interleave.
4. Option-list permutation per ITEM (currently per judge).
5. Pin + record model versions; hash prompts; record temperature/seed per call.
6. THE LEDGER (biggest gap): single SQLite store; every judgment a row with full provenance (stimulus, order, prompt-hash, instrument+protocol version, model, seed, ts, raw response, parsed). All analyses become recomputable views.

## The loop (recycling architecture)

walk (triads, mixture sampling, standing long-tail quota that never closes) → poset store (cross-consistent edges; ⟂ boundaries; tie clusters) → continuation agents propose rungs at the poset frontier (motion-framing for braids) → salting validates proposed rungs (membership; catches false precision on continuous axes)  
  → accepted rungs re-enter the walk pool  
  → poset emits candidate sequences → gestalt reconstruction validates at set level → holistic candidates route to length-graded continuation (onset curves) instead of pairs → generator lattices ($B^4$ quadrants, $B^6$ sextants/hexagrams, $B^8$ braille, product grids like star weight×points) tracked as objects, chains sampled from them Cross-substrate panel: every frozen hypothesis replicated on 3B + 70B + Sonnet minimum. Stop rule: loop-until-dry on the poset frontier (K rounds with no accepted new rungs), not fixed-N.

## Paper-grade verification: pilot → prereg → confirm

- Everything to date = pilot. Freeze protocol v1.0 from it.
- Write predictions file BEFORE the confirmation run (registered predictions; the pilot already contains several that failed honestly — keep that practice and cite it).
- Power from pilot variance: ~30–40 triads per per-sequence claim; family claims pool.
- Confirmation run: fresh judges, fresh RNG seeds, held-out glyph pools; pilot data never enters confirmatory statistics.
- Analysis plan fixed in advance: hierarchical partial-order / Bradley-Terry inference, cycle rate as transitivity statistic, Wilson + bootstrap CIs, multiple-comparison control at the claim level.
- Negative results are first-class: pairwise-blindness to holistic sequences, the ⟂ demand-characteristics measurement (80% manufactured edges), the axis-naming filter, morph-family failure, risebar false precision.
- Candidate paper spine: (1) protocol as reusable instrument for perceptual-order discovery in LLMs; (2) taxonomy: factorizable / holistic / authored / generator- lattice, each with an empirical signature; (3) substrate-invariance of axes vs capability-dependence of discipline; (4) immediacy as conflict arbiter (5 converging operationalizations); (5) demand characteristics measured and corrected.
- Optional strengthener: a human-judge arm (even n=1 Joseph, prereg'd) for the cross-mind claims.

## Pilot artifacts (this directory)

sequences.md (full experimental record, append-only) · probe*.py (ollama protocol) · triads.py / discover*.py / analyze.py / summarize.py (analysis) · walk*/battery*/ conflict/morph/gestalt/extend/continue/salt task+key JSONs · results*.jsonl · workflow scripts under the session workflows dir (rerunnable via scriptPath).

## Addenda from design review with Joseph (2026-08-25 evening)

- **Fated randomness (vivarium convention), mandatory:** all stochastic behavior derives its seed as a deterministic hash of the root object being processed — `seed = H(protocol_version || purpose_tag || canonical(root_object))`. Purpose tags give domain separation (side-order vs option-permutation vs salt-position for the same object must not correlate); protocol version inside the hash makes re-fating an explicit versioned act. Canonicalize before hashing (sorted keys, NFC, codepoint-explicit glyph serialization). Sampler draws are fated too: `H(ver || 'sample' || pool_digest || stratum || index)` — uniform in distribution, bit-reproducible in fact. Consequences: no seed bookkeeping, parallel-safe, partial runs merge on resume, stimulus→prompt hashes stable for caching.
- **Stimulus lineage field** on every event (survey-seed / frontier-proposal / uniform-tail): pollution is fine if labeled; confirmatory statistics condition on strata that never touched seeds; uniform tail is the standing uncontaminated control.
- **Surveys are seeds, not data** (Joseph): steering polluted them while sharpening the question — their role is loci/centers-of-gravity for initial resource allocation.
- **Lens-generation arm in the loop:** perceive (diffuse, polluted, generative) → validate (frozen instruments) → re-walk (new lens reopens old panes). Lenses are versioned first-class objects; pane verdicts are lens-relative; the loop has epochs, one per lens generation — a new lens legitimately re-wets a dry frontier (in the protocol text, so it isn't goalpost-moving).
- Language: Python, stdlib+sqlite3 (pending check against any estate script-language convention). Raw truth = append-only JSONL per run + manifest; parse versioned and re-runnable over verbatim raw responses; SQLite strictly a rebuildable index; strata seeds/ runs/ derived/ frozen/.

- **Lens-registry proposal WITHDRAWN (Joseph, 2026-08-25 — supersedes the lens-generation-arm framing above where they conflict):** no mechanism registry, no mechanism-organized batteries; sampling is structure-blind and graph-driven. Categories only as careful imagination-priming examples in generative briefs and as post-hoc hypothetical analysis labels. The empirical-feature-correlate program (ink mass, embeddings, name tokens vs discovered families; linear-readability of sequence membership in embedding space) replaces it as the defensible structure-finding instrument.
- **Index engine: Postgres 18, not SQLite (Joseph, 2026-08-25):** the derived, rebuildable index over the append-only JSONL truth is Postgres on this machine's existing 18 install (CLI is `psql-18` — the versioned binary; bare `psql` is a known friction source) with pgvector, so record store and embedding vectors share one queryable home. First harness milestone: extracted/*.jsonl + schema -> ingest -> explore; concordance and further commissioning gate on that exploration.
