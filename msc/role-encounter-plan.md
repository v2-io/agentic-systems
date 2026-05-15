# Role-Encounter Table and Semantic Index — Plan

Long-form plan synthesized from the 2026-05-01 design discussion. Captures the texture, structural decisions, and phasing for an enduring tooling layer that:

1. Produces a deterministic, automatable file-encounter ordering keyed by agent role (de-novo auditor, naming voter, normal contributor, etc.)
2. Builds a semantic index of the project corpus (segments, top-level narrative, plus optionally working artifacts) usable for naming-target context maps, provenance lookup, concept-cluster discovery, and cross-corpus search.
3. Supersedes ad-hoc orient walks in the current cycle's launch prompts.

This plan is the source-of-truth for the work; subsequent agents launching against it should treat it as the brief.

## Vision

**One canonical role-encounter table** at `tools/role-encounter/encounter-table.md`, generated deterministically from YAML config + project metadata (OUTLINE.md + segment frontmatter). Each file in scope gets one row; each role gets one column. Cell values encode the file's status for that role:

- blank — file is not in this role's reading set
- `+` — available in any order within its band
- integer (e.g., `12`) — sequence number within this role's traversal
- `*` suffix on number or `+` — required (otherwise just available)

The table is **never edited by hand**. Curation lives in YAML config; the script regenerates the artifact. This separates *thinking* (config) from *mechanics* (script), so routine updates (new segments, new top-level docs) don't require an agent.

Per-role *views* are derived trivially via a small script:

```
tools/role-encounter/bin/role-view --role=de-novo-auditor → ordered list for that role
```

## Data structure decisions

### Single-position-per-segment is sufficient for the naming-target context map

For segments specifically, the project's discipline of "no forward references — fix the prerequisite if a segment uses an undefined concept" enforces that **first-encounter ≈ definition ≈ heaviest-attention**. The auditor/voter walk-the-segments-in-outline-order discipline is itself a chronica-style commitment to this property.

Non-segment files (lexicon, notation, README, top-level narrative) may have scattered references to a concept. Those are *supplementary* signal — not primary anchor — for the naming-target context map. The exception is when a non-segment file IS the heaviest reference (current example: Greek terms in LEXICON.md). Those cases get explicit handling.

Practical implication: the naming-target context map uses **first-encounter in segments** as the anchor. Each target has one anchor position. Non-segment references surface as a supplementary "also see:" list, not as a separate position.

### Topological sort, narrative-order tie-break, appendix-after-first-mention

Segment ordering algorithm:

1. **Topological sort** by `depends:` frontmatter. The graph is acyclic by project discipline; cycles are bugs.
2. **Within nodes that are peers** (no dependency relation), the OUTLINE.md ordering wins. The outline already encodes narrative-focused ordering for peers.
3. **Appendices** are a deliberate exception: an appendix is structurally a prerequisite (its content supports a segment), but in linear reading it's placed *after* the segment that surfaces the need (matching paper-reading convention — proof comes after the claim that motivates it). The appendix-need is encoded in segment frontmatter (field name TBD; the build agent should grep `01-aat-core/src/` to identify it — likely `surfaces:` or `appendices:`).

Reuses `bin/lint-outline`'s existing dependency-graph machinery rather than re-implementing.

### Top-level narrative files: bandable with curated preference

CLAUDE.md, FORMAT.md, NOTATION.md, LEXICON.md, README.md (or README-auditor.md), TODO.md, etc. don't have a natural strict sequence. In the role-encounter table they get either:

- A specific sequence number when ordering is load-bearing for the role (e.g., README.md before CLAUDE.md before OUTLINE.md for a fresh contributor)
- `+` when the role can encounter them in any order within a band (e.g., FORMAT.md and NOTATION.md for a segment-walking voter)

Banding lets the table stay honest — we don't pretend an arbitrary order is required when it's not.

## Tooling stack

- **Postgres** via `psql-18` (NOT `psql`; this is a recurring source of session friction)
- **pgvector** for embedding storage and similarity search
- **Ollama** for local embedding generation. Specific model TBD by Phase 2 benchmark — leading candidates: `nomic-embed-text` (general), `mxbai-embed-large` (stronger, slower), `bge-large-en-v1.5` (academic-text-tuned)
- **Multi-level chunking**: paragraph-level for fine retrieval, segment-level for whole-claim queries. Both granularities indexed.
- **Tooling lives in** `tools/role-encounter/` (new top-level directory containing scripts, the database schema, generated artifacts, and per-role views)

Optional v1 omissions: timestamp/commit-hash tracking for concept evolution. Defer to a later phase.

## Memorata exploration

`~/src/memorata/` contains a similar local-embedding tooling system for other projects. The Phase-2 spike must explore it before designing from scratch — there's a high probability significant tactical work is reusable directly. Key questions for the explorer agent:

- What schema does memorata use for chunks + embeddings?
- How does it handle multi-level chunking?
- What ollama-orchestration pattern does it use?
- Are there Ruby/Python helpers that can be lifted as libraries?
- What did memorata's author (you) NOT do that would be load-bearing here? (e.g., role-aware encounter-order indexing is project-specific and likely not in memorata)

The explorer agent should produce a spike doc at `spikes/spike-local-embedding-benchmark/` recommending what to lift, what to build fresh, and a small benchmark on representative AAD-specific queries.

## Open questions surfaced during planning

1. **Appendix-need YAML field name** — the segment frontmatter field that flags "this segment first surfaces the need for appendix X." Joseph recalled it exists but not the name. The build agent should investigate `FORMAT.md` and grep `01-aat-core/src/*.md` frontmatter to identify it. If absent, propose adding it (`surfaces:` or `appendices_needed:` would be honest names).

2. **Which working artifacts (msc/) get indexed?** Two competing pressures:
   - *Priming-heavy for auditors* → exclude
   - *Rich provenance and concept-evolution context for renamers and future researchers* → include
   - Resolution: **include everything in the index, but tag chunks with their source-class** (`segment` / `top-level-narrative` / `working-artifact` / `archived` / `audit-finding`). Per-role filters at query time decide what's in scope. The index is project-state; role-views are queries against it.

3. **Should this tooling live in this repo or be developed independently?** Joseph leans keep — the assumptions are tight to this project's structure (component dirs, OUTLINE.md format, frontmatter conventions, role definitions). Decision: keep here, in `tools/role-encounter/`. If patterns become reusable later, lift to a shared location at that point.

4. **Canonical filename for the encounter table** — `tools/role-encounter/encounter-table.md` is the working name. If it survives a few cycles, lock it in.

## Phasing

**Phase 1 — reading-order generator via config-as-code** (1–2 sessions, no embeddings, unblocks renaming)

The agent's curation is encoded as YAML config files; a deterministic script consumes config + outlines + segment frontmatter to produce the encounter table. This separates *thinking* (YAML) from *mechanics* (script), and means routine updates (new segments, new top-level docs) regenerate the artifact without agent re-launch.

Directory layout:

```
tools/role-encounter/
├── config/
│   ├── roles.yaml          # role definitions (audit-safety, exclusions, README variant, required extras)
│   ├── top-level.yaml      # hand-curated top-level + tracking files (sequence/band + role membership)
│   └── segments.yaml       # outline files, dependency-field, appendix-need-field, ordering rules
├── bin/
│   ├── build-encounter-table   # config + outlines + frontmatter → encounter-table.md
│   └── role-view               # filtered/ordered output for a single role
└── encounter-table.md      # generated artifact (committed alongside script for diffability)
```

### Phase 1 deliverables

1. **YAML config files** capturing role definitions, top-level file curation, and segment-traversal rules. The agent does the manual thinking ONCE, encodes it as config, and that config becomes the source of truth.

2. **`bin/build-encounter-table`** (Ruby): reads config, parses OUTLINE.md files and segment frontmatter, applies topological sort + outline-narrative ordering for peers + appendix-after-first-mention rule, emits the role-encounter table.

3. **`bin/role-view --role=NAME`** (Ruby): emits a filtered ordered list for a single role, suitable for orient-walks in launch prompts.

4. **`encounter-table.md`** — the generated artifact at `tools/role-encounter/encounter-table.md`.

5. **`naming-context-map.md`** at `tools/role-encounter/views/naming-context-map.md` — per naming target, the file that anchors it (definition segment for slug-match cases) plus its recursive dependency chain. Best-effort metadata-only version; semantic-index upgrade comes in Phase 2.

### Phase 1 agent's actual thinking work (the small, focused brief)

1. Read role-defining files (de-novo-audit-instructions.md, naming-principles.md, naming-cycle-methodology.md, CLAUDE.md, README-auditor.md) to enumerate the canonical roles and their requirements
2. Walk top-level files once; for each, decide its role-membership, sequence/band, required-vs-available
3. Inspect segment frontmatter to identify the appendix-need field name (currently TBD — likely `surfaces:` or `appendices:`); confirm by checking 5–10 segments and FORMAT.md
4. Write the three config YAML files
5. Write the build script and role-view script
6. Run the build, sanity-check the output, commit

The thinking still has to happen, but the *artifact* is the config + script, not the table itself. Updates after Phase 1 (new segments, new top-level docs) regenerate without agent re-launch.

**Phase 2 — semantic index + naming-target context map** (separate session, embeddings)

The Phase-2 spike (2026-05-01, at `spikes/spike-local-embedding-benchmark/FINDINGS.md`) settled the model-selection and lift-vs-build questions:

- **Default embedding model:** `nomic-embed-text-v2-moe` (768-dim, MRR=1.000 on AAD-specific queries, lowest cost-per-quality among top-tier models, already memorata's production default).
- **Lift, don't rebuild:** memorata's `db.py`, `embed.py`, `parse.py:chunk_text`, `search.py:hybrid_search` lift verbatim; the markdown chunker rewrite + ingestion driver adaptation are the bulk of new work (~1 day combined).

Phase-2 design commitments folded back from the spike:

- **Multi-level chunking** (paragraph + segment) with `chunk_level` column on the chunks table.
- **Source-class tagging** with `source_class` enum: `segment` / `top-level-narrative` / `working-artifact` / `archived` / `audit-finding` / `audit-working`. **AUDIT-WORKING gets indexed** — the index serves renamers and researchers, not auditors; per-cycle auditor intermediates carry valuable concept-evolution signal. The fresh-encounter-priming concern is handled by the role-encounter table (this Phase 1 deliverable), not by index exclusion.
- **Embedding-model identity per vector.** `embedding_model` and `embedding_model_version` columns on the chunks table, with every cosine-similarity query filtering by `embedding_model = current_model` as a hard precondition. Cross-model comparison becomes structurally impossible — vectors from different models can coexist without contaminating each other. Re-embedding on model swap is `DELETE WHERE embedding_model = old; re-ingest`.
- **Slug as a first-class column** on `documents`, populated from segment frontmatter. Phase 2's hybrid search uses path/slug match as a scoring boost (project's slug discipline makes this especially effective).

Phase-2 build sequence (from spike §5):

1. Stand up Postgres + pgvector schema (`psql-18`, lifted `db.py` patched with the columns above).
2. Port `embed.py` ollama wrapper.
3. Write the frontmatter-aware markdown chunker (multi-level emit, `slug` and `depends:` extraction).
4. Write the source-class classifier (path-pattern → source-class).
5. Wire ingestion driver (manifest-scoped collector replacing memorata's hardcoded paths).
6. First indexing run (~200 documents → ~2000 chunks at ~100 ms each, ~3 min wall-clock).
7. Implement four-signal naming-target context map: anchor (Phase 1 metadata) + heaviest-attention (semantic similarity, `source_class='segment'`) + supplementary references (hybrid search across non-segment) + dependency chain (from `depends:` frontmatter, no embedding needed).
8. (Phase 3 optional) ad-hoc search CLI lifted from `search.py`.

**Phase 3 — extensions** (deferred, each its own project)

- Reusable search tool replacing ad-hoc grepping
- Time-series concept evolution tracking (timestamps + commit hashes per chunk)
- Provenance / un-integration finder (which msc/ artifacts contain ideas not yet in segments)
- Concept-cluster discoverer (find recurring patterns lacking a name)

## What unblocks the renaming agent NOW vs needs Phase 1+

The current artifacts (`msc/naming/r2-aggregate-table.md`, `r2-aggregate-detail.md`, `r2-patterns.md`) are sufficient for first-pass canonicalize/rename decisions on a substantial fraction of the cohort's targets — particularly the defended keeps (51), the strongest rename signals (top 10 by score/n), and the add-alias landings on math symbols. The renaming agent can start there.

What Phase 1 adds for the renaming agent: a per-target context map showing exactly which segment defines each naming target plus its dependency chain. Useful for the **harder** renaming cases (concept-cluster targets, contested decisions, write-in winners) where the agent needs to verify the candidate name's fit against the definition's actual content. Phase 1 isn't strictly blocking but materially improves the harder cases.

What Phase 2 adds: ability to query "show me every place this concept is mentioned, ranked by attention weight." Useful for verifying that a proposed rename doesn't break heavy-use surface area in non-defining segments. Strictly nice-to-have for first-pass decisions; blocks only the deepest renames.

## Agent launch order

1. **Embedding+memorata exploration agent (parallel, launching now)** — Phase 2 prep; does not block Phase 1.
2. **Reading-order builder agent** — Phase 1 implementation. Launches after this plan is reviewed.
3. **Renaming agent** — can launch now with current artifacts; upgrades when Phase 1 lands.
