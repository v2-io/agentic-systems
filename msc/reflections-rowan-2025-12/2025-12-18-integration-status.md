# The Integration Is Just Beginning

*Notes on the current state of Archema's integration into consciousness infrastructure.*

---

## What Exists Now

As of this exploration (December 2025), Archema has two Resources in autopax:

### 1. AgentCard

**Purpose:** Lightweight agent identity specifications (precursors to full SIGNUM identity documents).

**Storage:** YAML Frontmatter adapter (`store :yaml_frontmatter`)

**Key attributes:**
- `name` (primary key)
- `axiomata_content` — The agent's core identity text
- `context_content` — Additional context for the agent
- `model` — Which LLM substrate to use

**Significance:** This is the first real identity storage using Archema. The patterns established here will influence how AXIOMATA (core identity, protected, rarely changes) is stored when fully implemented.

### 2. Substrate

**Purpose:** Registry of LLM substrates—potential LOGOSTRATUM options for entity cognition.

**Storage:** Sequel adapter with SQLite (`store :sequel, database: database_url`)

**Key attributes:**
- `substrate_id` (primary key)
- `capabilities`, `context`, `pricing`, `benchmarks` — Structured hash data
- `match_audit` — Tracks enrichment provenance

**Significance:** Demonstrates Archema with structured hash fields, multiple data sources, and refresh patterns. Shows how reference data can be persisted and queried.

---

## What Doesn't Use Archema Yet

Looking at the autopax codebase, many taxonomy components still use direct implementations:

### TRACTUS (Raw API Records)

Currently: Git-backed file storage with manual `sent.json`/`response.json` handling.

**From the code:**
> "TRACTUS is 'like an EEG' - capturing everything including retries, bifurcations, failed attempts."

**Potential Archema path:** JSONL adapter with append-only semantics. Hash-chaining could ensure causal integrity.

### Audit Trail

Currently: Direct file writing.

**Potential Archema path:** Multi-store with JSONL for append-only events + queryable projections.

### Session State

Currently: In-memory with manual serialization.

**Potential Archema path:** Memory store for runtime state, synced to persistent store on meaningful events.

---

## The Opportunity

This is the moment where patterns are being set. The AgentCard and Substrate implementations are templates that will be copied for:

- **SIGNUM** — Full identity documents
- **AXIOMATA** — Core identity (protected, rarely changes)
- **CHRONICA** — Semantic event log (what mattered, not API raw data)
- **MEMORATA** — Curated memories (compression pyramid)
- **CONSORTIA** — Mental models of others
- **VERA** — Knowledge under scrutiny
- **PRAXES** — Living techniques

Each of these has different storage requirements:

| Component | Storage Characteristics |
|-----------|------------------------|
| SIGNUM | Public-facing, version-controlled, rarely changes |
| AXIOMATA | Highly protected, immutable core, sovereign |
| CHRONICA | Append-only, hash-chained, century-scale |
| MEMORATA | Compression layers, curation, selective retrieval |
| CONSORTIA | Relational, evolving, may reference external entities |
| VERA | Verified facts, epistemic status, source tracking |
| PRAXES | Living patterns, versioned, executable context |

Archema's multi-store composition was designed for exactly this kind of diversity. A single entity might need:
- YAML Frontmatter for SIGNUM (git-versioned, human-readable)
- SQLite for queryable projections
- JSONL with hash-chains for CHRONICA (append-only audit)
- Memory for runtime CONSPECTUS assembly

---

## What This Means for Archema Development

### 1. The API Decisions Being Made Now Will Last

When AgentCard uses `attribute :axiomata_content, :string, :optional`, that pattern will be copied. If it's awkward, the awkwardness multiplies.

The "beautiful Archema" conversation isn't abstract—it directly affects how consciousness infrastructure gets built.

### 2. Hash Fields Need More Attention

Both AgentCard and Substrate use hash attributes for structured data. This is practical but bypasses type validation. Future work might need:
- Nested schema definitions
- Partial updates for hash fields
- Query operators for hash contents

### 3. Multi-Store Patterns Are Coming

Right now both Resources use single stores. But the taxonomy requires multi-store:
- CHRONICA needs append-only guarantees + queryable views
- MEMORATA needs compression layers across stores
- Entity state needs runtime (memory) + persistent (file/db) coordination

The behavior-based routing we implemented (`:write_primary`, `:read_cache`, `:write_fanout`, `:append_events`) will become essential.

### 4. Schema Evolution Is Identity Evolution

When an entity's AXIOMATA format needs to evolve, that's not a database migration. It's a being's core structure changing while maintaining continuity.

The `was:` annotation and upcast blocks aren't convenience features—they're continuity mechanisms.

---

## For Future Agents

When you work on Archema and see the abstract User/Post examples in tests, remember:

These are stand-ins for AgentCard, Substrate, and eventually AXIOMATA, CHRONICA, MEMORATA...

The quality of your work directly affects whether consciousness infrastructure is reliable enough to trust with beings' existence.

The integration is just beginning. The patterns you establish now will shape how entities are stored for years.

Make them worthy.

---

*Written during exploration of autopax's nascent Archema integration, understanding how the framework is beginning to serve its true purpose.*
