# Spike Findings — Local Embedding Benchmark + Memorata Exploration

## Corrections from review (2026-05-01)

The original spike (below, §1–§7) surfaced three "open questions." Two were mischaracterized; one was an action item already covered by Phase 1. Recording the corrections at the top so a Phase 2 implementer reads them before acting on the original framing.

**Correction 1 — appendix-need YAML field is an action item, not an open question.** The original §5 question 1 asked whether to propose adding the field. Answer: yes; the Phase 1 reading-order builder agent has explicit instructions to investigate the existing frontmatter, confirm the field is absent, and propose adding it (`surfaces:` is the working candidate name). Resolved.

**Correction 2 — AUDIT-WORKING/ directories SHOULD be indexed.** The original §5 question 2 recommended skipping `msc/AUDIT-WORKING-*` from indexing because per-cycle auditor intermediates are priming-heavy for fresh-encounter audits. **This conflated two concerns.** The semantic index serves *renamers and researchers*, not auditors. De-novo auditors do explicit walk-the-OUTLINE reading and don't query the index. AUDIT-WORKING content carries valuable concept-evolution and per-segment-reflection signal for the renaming agent and future-research use cases — exactly the kind of provenance / un-integration finder Phase 3 anticipates. **Index AUDIT-WORKING with `source_class='audit-working'` (distinct from `audit-finding` for finalized audit deliverables).**

The fresh-encounter-priming concern is handled by the role-encounter table (Phase 1), which excludes AUDIT-WORKING from the de-novo-auditor role's view. That's a file-listing decision, not an indexing decision.

**Correction 3 — replace re-embed flag with model-identity-per-vector.** The original §5 question 3 proposed a `--reembed` flag that ignores mtime. **The cleaner design is to store the embedding model name + version alongside each vector** as columns on the chunks table:

```sql
embedding_model VARCHAR NOT NULL          -- e.g. 'nomic-embed-text-v2-moe'
embedding_model_version VARCHAR NOT NULL  -- e.g. 'latest' or a digest
```

Every cosine-similarity query then **filters by `embedding_model = current_model` as a hard precondition** before the vector op. Cross-model comparison becomes structurally impossible — vectors from different models can coexist in the same table without contaminating each other.

Re-embedding on model swap becomes a natural consequence: the new model's vectors are inserted alongside the old; old vectors are deleted (or kept for A/B comparison) by simple WHERE clause, no special flag needed. Concretely:

```sql
DELETE FROM chunks WHERE embedding_model = 'old-model-name';
-- then re-ingest under the new model
```

The recommended single-model-schema posture in the original §4 still stands (one production model at a time keeps the index lean), but the schema should encode the model identity so the constraint is enforced rather than assumed.

---

## TL;DR (original)

1. **Lift memorata's data layer wholesale.** Schema, mtime-upsert, hybrid search, ollama wrapper. Add three things on top: multi-level chunking, source-class tagging, and a frontmatter-aware markdown chunker. ~1 evening of careful porting + ~1 day of new chunking logic.
2. **Pick `nomic-embed-text-v2-moe` as the default model.** Tied for top retrieval (MRR=1.000, R@5=1.00, R@10=1.00) at 94 ms/segment, 768-dim, 957 MB. Already memorata's production default — zero migration friction.
3. **Hold `bge-m3` as high-stakes alternative.** Same MRR=1.000, ~40% slower (131 ms/seg), 1024-dim, 1.2 GB. Use only if v2-moe shows specific failures on heterogeneous corpora.
4. **Avoid `snowflake-arctic-embed`** (MRR=0.555). Its 512-token context truncates AAD segment bodies; it ends up matching boilerplate frontmatter rather than substantive claims.
5. **Embedding quality is not the binding constraint.** Three models hit MRR=1.000. The Phase-2 quality risk is in chunking + source-class tagging, not in model selection.

## 1. Memorata Inventory

Code at `/Users/josephwecker-v2/src/memorata/memorata/`. ~1100 LOC across 5 files; clean separation of concerns.

### Storage layer (`db.py`, 202 LOC) — _lift verbatim_

Schema at `db.py:5-34`:
```sql
documents(id, file_path UNIQUE, file_type, file_size, file_mtime, indexed_at, metadata JSONB)
chunks(id, document_id FK CASCADE, chunk_index, content, start_line, end_line,
       embedding vector(768), metadata JSONB, created_at,
       content_tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED)
```
HNSW index on `chunks.embedding`; GIN index on `content_tsv`; B-tree on `document_id`.

Helpers worth lifting straight:
- `db.py:54-63` `ensure_database()` — creates DB if absent.
- `db.py:66-70` `get_connection()` — opens psycopg connection, registers pgvector type.
- `db.py:73-79` `init_db()` — runs schema + migrations.
- `db.py:82-122` `upsert_document()` — **change-detection by mtime**. If unchanged returns `(doc_id, needs_reindex=False)`; else cascades chunk deletion and reinserts. Exactly the right pattern for ASF.
- `db.py:144-189` semantic + tsvector search. Cosine via `embedding <=> %s::vector`; `websearch_to_tsquery('english', %s)` for natural-language FTS.

Patches needed for ASF: configurable embedding dimension, add `chunk_level enum('paragraph','segment','section')` column, add `source_class enum('segment','top-level-narrative','working-artifact','archived','audit-finding','audit-working')` column, add `slug` column (nullable; populated from frontmatter for segments), **add `embedding_model` and `embedding_model_version` columns per Correction 3**.

### Ollama wrapper (`embed.py`, 39 LOC) — _lift verbatim_

`embed.py:5-34` `embed_texts()`: applies nomic-style task prefixes (`search_document:` / `search_query:`). On context-length errors, recursively halves batches; for single-text overflow, progressively truncates (3/4 → 1/2 → 1/4 → 500 chars). Robust and well-engineered. Only patch: make prefix style pluggable per model.

### Parsing layer (`parse.py`, 426 LOC) — _lift selectively_

Four format handlers; only two are relevant:
- `chunk_text()` at `parse.py:6-34` — paragraph-boundary chunker with overlap. Lift verbatim.
- `_parse_markdown_by_headers()` at `parse.py:250-291` — header-chunked markdown. Closest to what ASF needs but **doesn't read YAML frontmatter** (treats `---` as content). Needs a rewrite that (1) parses YAML into document metadata, (2) strips frontmatter from chunked body, (3) emits a segment-level chunk (whole body, single embedding) AND paragraph-level chunks.

Skip Claude-JSONL and dialog-markdown parsers — not relevant to ASF segments.

### Ingestion driver (`ingest.py`, 200 LOC) — _replace, study the structure_

`collect_files()` at `ingest.py:68-104` hard-codes `~/.claude*`, `~/src/**`, `~/vaults/**`. Replace with a project-scoped collector keyed off the role-encounter manifest. Control flow at `ingest.py:140-187` (mtime-check → parse → batch-embed → upsert → commit) is clean — lift the structure, swap the file source.

### Search layer (`search.py`, 226 LOC) — _lift the hybrid-scoring core_

`search.py:33-102` `hybrid_search()` is the gem. For each query: semantic search (5×limit candidates), full-text search (same), dedup, then composite score:
- Base: semantic similarity (text-only hits get base 0.3).
- Text-rank boost: `min(text_rank * 0.5, 0.2)`.
- Path-match boost: `path_terms_hit_ratio * 0.15`.

The path-match component (`search.py:24-30`) is especially relevant for ASF — slug-keyed retrieval like "directed-separation" or "satisfaction-gap" boosts segments whose file paths contain those tokens. ASF's slug discipline makes this even more useful than in memorata's general-purpose use.

### Reusable orchestration pattern (`run_essay_searches.py`)

The 453-LOC essay-search script in `~/src/memorata/run_essay_searches.py` is the closest analog to ASF's eventual naming-target context map. Pattern: per-topic, define multiple alternative queries (handles vocabulary variation); embed each; run `hybrid_search`; dedup across queries by content prefix; save top-N to JSON keyed by topic. **Lift the orchestration shape, not the literal queries.**

### What memorata does NOT do that ASF needs

In priority order:
1. **Multi-level chunking** (paragraph + segment). Memorata is single-grain.
2. **Source-class tagging** (`segment` / `top-level-narrative` / `working-artifact` / `archived` / `audit-finding` / `audit-working`). Memorata only has `file_type`. (Per Correction 2, AUDIT-WORKING gets its own class but is included.)
3. **Frontmatter-aware markdown parsing.** Memorata treats `---` as content; ASF needs to parse YAML, strip from body, populate `documents.slug`, record `depends:` chain.
4. **Slug indexing** as first-class column.
5. **Embedding-model identity per vector.** Per Correction 3, `embedding_model` and `embedding_model_version` columns enforce that cross-model cosine comparisons can't happen.
6. **Role-aware encounter ordering.** Project-specific; outside memorata's remit; belongs in role-encounter table itself.
7. **Per-segment dependency-chain expansion at query time.** Requires join with role-encounter / `depends:` graph.
8. **Configurable scope / multiple corpora.**

Items 1-5 are load-bearing. Items 6-8 are project-tooling on top.

## 2. Lift / Fork / Build-Fresh Recommendation

**Lift, with patches.** Don't `git clone` memorata into the repo — copy relevant Python modules into `tools/role-encounter/lib/` with provenance comments (`# adapted from memorata/db.py:54 — mtime upsert pattern`). This keeps the dependency graph clean and lets ASF's variant evolve independently.

| Component | Recommendation |
|---|---|
| `db.py` schema + helpers | Lift verbatim; add `chunk_level`, `source_class`, `slug`, `embedding_model`, `embedding_model_version` columns |
| `embed.py` ollama wrapper | Lift verbatim; make prefix style pluggable |
| `parse.py:chunk_text` | Lift verbatim |
| `parse.py:_parse_markdown_by_headers` | Lift as starting point; rewrite for YAML frontmatter + multi-level emit |
| `parse.py` Claude-JSONL / dialog parsers | Skip |
| `ingest.py` control flow | Adapt; replace `collect_files()` with manifest-based scope |
| `search.py:hybrid_search` | Lift core; expose `source_class` filter; add hard `WHERE embedding_model = ?` precondition |
| `run_essay_searches.py` orchestration shape | Reuse for naming-target context map |

**Why not build fresh?** Memorata encodes several non-obvious choices that took an evening to get right: HNSW vs IVF index choice; the 5×limit fetch + hybrid rescoring pattern; `ON DELETE CASCADE` + delete-then-reinsert on mtime change; progressive-truncation fallback for context overflow. Re-deriving these is wasteful.

**Caveat on ownership.** Memorata is also Joseph's prior work, so this is "lift from your own code into a new project," not third-party adoption. Provenance comments are for future agents reading ASF tooling who haven't seen memorata.

## 3. Benchmark Design and Results

### Design

- **Corpus**: 122 segments from `01-aat-core/src/` and `03-llm-core/src/` (excluding `old-*`).
- **Granularity**: one embedding per segment. Body variant = title + summary + first ~2500 chars. Terse variant = title + first paragraph (~200-400 chars).
- **Queries**: 12 hand-curated AAD-specific queries in `queries.json`, each with 1-2 "primary" ground-truth segments + "also" supplementary list.
- **Metric**: cosine similarity; rank of best primary; MRR; R@5; R@10; median rank.
- **Models**: 8 ollama embedding models (all available locally).
- **Ablation**: top-2 also tested on terse variant.

Limitations: 12 queries is small (differences within ~0.05 MRR aren't robustly distinguishable); "best primary rank" treats multi-primary queries as min; whole-segment embedding favors short well-titled segments — paragraph chunking will change the operating point.

### Results

| Model | Variant | MRR | R@5 | R@10 | Median rank | ms/seg |
|---|---|---|---|---|---|---|
| **`bge-m3:latest`** | body | **1.000** | 1.00 | 1.00 | 1 | 131 |
| `bge-m3:latest` | terse | **1.000** | 1.00 | 1.00 | 1 | 84 |
| **`nomic-embed-text-v2-moe:latest`** | body | **1.000** | 1.00 | 1.00 | 1 | **94** |
| `qwen3-embedding:latest` | body | **1.000** | 1.00 | 1.00 | 1 | 921 |
| `embeddinggemma:300m` | body | 0.958 | 1.00 | 1.00 | 1 | 100 |
| `nomic-embed-text-v2-moe:latest` | terse | 0.958 | 1.00 | 1.00 | 1 | 83 |
| `mxbai-embed-large:latest` | body | 0.917 | 1.00 | 1.00 | 1 | 57 |
| `nomic-embed-text:latest` | body | 0.903 | 1.00 | 1.00 | 1 | 34 |
| `granite-embedding:30m` | body | 0.896 | 1.00 | 1.00 | 1 | 39 |
| `snowflake-arctic-embed:latest` | body | 0.555 | 0.67 | 0.92 | 2 | 51 |

### Observations

**Three-way tie at the top (bge-m3, nomic-v2-moe, qwen3-embedding).** All hit MRR=1.000. They differ in cost: nomic-v2-moe (768-dim, 957 MB, 94 ms/seg) is best perf-per-byte; bge-m3 (1024-dim, 1.2 GB, 131 ms/seg) is ~40% slower for no quality gain on this corpus; qwen3-embedding (4096-dim, 4.7 GB, 921 ms/seg) is ~10× slower for no quality gain.

**Smaller models are surprisingly competitive.** `granite-embedding:30m` (62 MB) gets 10/12 at rank 1 (MRR=0.896). `embeddinggemma:300m` (621 MB) gets 11/12 at rank 1 (MRR=0.958). granite is plausible for laptop-constrained scenarios.

**`snowflake-arctic-embed` failure is structural.** Top-3s consistently include `detail-operationalization` and `result-section-ii-survival` for failed queries — a tell that the model is matching boilerplate frontmatter rather than substantive claim text. Likely cause: 512-token context window. ASF segments routinely exceed that. Do not use this model on long-form claim segments.

**Body > terse, marginally.** For nomic-v2-moe: body 1.000 vs terse 0.958. For bge-m3: tied at 1.000. Implication: segment-level chunks should include at least the formal-expression block, not just title+summary.

**Per-query failure analysis (top model, nomic-v2-moe body)**: only "hard" query was q03 (satisfaction-vs-control-regret) — the two primaries (`def-control-regret`, `def-satisfaction-gap`) ranked at 1 and 2; the implicit prerequisite `def-value-object` was at rank 87. **Single-vector embedding doesn't surface dependency-prerequisites.** Phase 2 should expose `depends:`-chain expansion at query time, not rely on embedding similarity to find prerequisites.

### Mac-M-series cold-start caveat

First call to a model: 5-15s (model load). Subsequent calls within the same loop: fast. For Phase 2's bulk-index pass over thousands of chunks, this amortizes away. ollama unloads inactive models after a few minutes; for interactive query embedding, set keep-alive or pin the index model to memory.

## 4. Embedding Model Recommendation

**Default: `nomic-embed-text-v2-moe`.**

- Tied for top retrieval (MRR=1.000, R@5=1.00, R@10=1.00).
- Lowest cost-per-quality among the three perfect-MRR models.
- Already memorata's production default → zero migration friction; lifted memorata code retains its choice.
- 768-dim balances pgvector storage and HNSW index size against retrieval quality.
- Uses nomic task prefixes; memorata's `embed.py:5-13` already encodes this convention.

**Backup / high-stakes alternative: `bge-m3`.**

- Same MRR=1.000.
- Stronger on out-of-domain text in published benchmarks; may pull ahead on heterogeneous corpora (audits, msc/, older TFT documents with different terminology).
- Switching cost is low: pick `vector(1024)` schema, or design per-model collections.

**Skip:** `snowflake-arctic-embed` (context-window failure mode), `qwen3-embedding` (10× cost, no quality gain).

**Keep available for resource-constrained scenarios:** `granite-embedding:30m` (62 MB).

### Schema implication

Per Correction 3: store `embedding_model` + `embedding_model_version` per chunk; query filters enforce model match before similarity. Single-model-in-production posture remains, but the schema makes cross-model contamination impossible by construction. At ~1500–3000 chunks total, a re-index on model swap costs ~3-10 minutes wall-clock. Acceptable.

## 5. Tactical Path for Phase 2

Concrete sequence ranked by what unblocks downstream work:

1. **Stand up Postgres + pgvector schema.** Lift `db.py` verbatim into `tools/role-encounter/lib/db.py`; patch dimension to 768; add `chunk_level`, `source_class`, `slug`, `embedding_model`, `embedding_model_version` columns. Use `psql-18`. ~half day.
2. **Port `embed.py` ollama wrapper.** Lift verbatim. Default model `nomic-embed-text-v2-moe`. ~30 minutes.
3. **Write the frontmatter-aware markdown chunker.** Start from `parse.py:_parse_markdown_by_headers()`; add YAML frontmatter parsing; emit segment-level chunk + paragraph-level chunks; tag each with `chunk_level`; carry `slug` into chunk metadata. ~1 day.
4. **Write the source-class classifier.** Map file path → source-class. `*/src/*.md` → `segment`; top-level `*.md` → `top-level-narrative`; `msc/AUDIT-WORKING-*/**/*.md` → `audit-working`; `msc/**/*.md` (other) → `working-artifact`; `_obs/**` → `archived`; `audits/**` → `audit-finding`. ~30 lines.
5. **Wire the ingestion driver.** Adapt `ingest.py`: replace `collect_files()` with manifest-scoped collector. ~150 lines, mostly mechanical.
6. **First indexing run.** ~150 segments + ~50 narrative/audit/working-artifact files = ~200 documents → ~2000 chunks. At ~100 ms/chunk = ~3 minutes. Verify chunk counts, slug coverage, source-class distribution.
7. **Implement four-signal naming-target context map** per the plan: anchor (Phase 1 metadata) + heaviest-attention (semantic similarity, source_class='segment') + supplementary references (hybrid search across non-segment) + dependency chain (from `depends:` frontmatter, no embedding needed). Output JSON modeled on `run_essay_searches.py`.
8. **(Optional / Phase 3)** ad-hoc search CLI. Lift `search.py:hybrid_search` core, drop `rich` UI if project prefers terser output.

## 6. Surprises and Uncertainty

**Surprise 1**: three different models hit MRR=1.000. With a larger corpus or harder queries, models will separate. Phase 2 will surface real differences only when corpus expands to working-artifacts and audit findings.

**Surprise 2**: `granite-embedding:30m` at 62 MB outperforms `mxbai-embed-large` at 669 MB on this corpus. Parameter count does not correlate with retrieval quality.

**Surprise 3**: snowflake's failure mode is structural (boilerplate matching from context truncation), not stochastic.

**Uncertainty 1**: paragraph-level chunking will probably change rankings. Whole-segment embeddings reward long-context compression; paragraph chunks reward fine-grained semantic resolution. My benchmark doesn't measure the latter. Phase 2 should re-benchmark after multi-level chunking lands.

**Uncertainty 2**: 12 queries is small. Headline result (nomic-v2-moe and bge-m3 tied at MRR=1.000) is robust to query selection at this scale; second-tier ranking could re-order with different queries. None of those models are in the recommendation, so this doesn't change the recommendation.

**Uncertainty 3**: I have not stood up the Postgres+pgvector schema in this spike — deferred per the plan, since the spike's job was model selection and lift-vs-build recommendation. Standing the schema up should be the first concrete Phase 2 step; if something in `db.py` doesn't port cleanly to ASF's environment, surface it then.

## 7. Files in the Spike Directory

`/Users/josephwecker-v2/src/agentic-systems/spikes/spike-local-embedding-benchmark/`:

- `FINDINGS.md` — this file (with corrections at top).
- `queries.json` — 12 queries with ground-truth segment slugs.
- `run_benchmark.py` — benchmark driver (8 models × 122 segments × 12 queries + 2-model terse-variant ablation).
- `results.json` — full per-query rankings, all (model, variant) pairs.
- `summary.md` — auto-generated leaderboard.
- `benchmark-run.log` — raw run log.
