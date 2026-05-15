# terminology/ — naming source-of-truth

Multi-agent-safe terminology store for the Agentic Systems Framework. The CLI lives at `bin/term`. This directory holds the data: per-entry markdown-with-YAML-frontmatter files, append-only decision events.

## Layout

```
terminology/
├── README.md                            this file
├── entries/<slug>.md                    one file per term; filename is the canonical key
└── decisions/<slug>/                    append-only directory of decision events
    └── <ts>-<decider>-<action>.md
```

`LEXICON.md` (root) is **generated** from these entries by `bin/term render`. Do not hand-edit it; edit the relevant entry under `terminology/entries/<slug>.md` and re-run `bin/term render`. Same discipline as `bin/build-readme` regenerating `README.md` from `doc/readme/` partials.

## Why the structure looks like this

**Per-entry files, not one shared LEXICON.md.** Multiple agents add or refine terminology entries independently. With one shared markdown LEXICON.md, every concurrent edit is a potential merge conflict on the table-row level; the failure mode is silent (a malformed table row renders ambiguously). With per-entry files, two agents adding distinct terms touch distinct files — git resolves trivially. Two agents editing the *same* entry surfaces as a clean single-file conflict. The shared LEXICON.md is recovered as a *generated* artifact via `bin/term render`.

**Markdown body for the definition, not just frontmatter.** The previous LEXICON.md table-cell format flattened the *definition* into a one-line gloss. Many terms deserve a paragraph or two of prose with links to defining segments. The frontmatter carries structured metadata (notation, status, tags, source, cross-refs); the markdown body carries the prose definition. Frontmatter-mostly entries (Greek phases, simple symbols) are fine — short body or empty body.

**Append-only decision events, not mutable status fields.** Naming decisions ride downstream of cycle work — votes, audits, curation passes, individual judgment calls. We need to know *who* decided *what* (canonicalize, rename, add-alias, etc.) for *which slug*, *when*, and *why*. Mutable status fields lose that history (and lose it silently when overwritten). Append-only files preserve it. Filenames include a UTC timestamp + decider + action, so two agents recording decisions for the same entry never collide.

**Permissive extractor / strict linter.** `Entry.load` and `bin/term render` do NOT block on schema issues. They load and emit what's there, marking missing required fields as `(missing)`. `bin/term lint` is the place where schema issues, cross-ref issues, and content issues surface as actionable warnings. This separation lets render show the current state of the world even when entries are mid-edit; it lets lint be strict without blocking everyday workflows.

**YAML frontmatter, not a separate metadata file.** YAML is in the Ruby stdlib (no extra gems); markdown frontmatter is a familiar pattern; agents already read/write the format. The structure is shallow enough that whitespace fragility isn't a real concern.

## Design decisions: why per-entry markdown-YAML, not sqlite

The original sketch was sqlite. Re-examined 2026-05-08 and re-decided in favor of per-entry markdown-with-YAML-frontmatter, modeled on the `~/src/neurips/refs/` pattern that landed in May 2026 for citation-management. The summary of the trade study:

| Concern | sqlite | per-entry YAML+markdown (this design) |
|---|---|---|
| Crash-atomicity of single write | WAL (journal-replay) | `safe_write`: temp-file + fsync + `rename(2)` |
| Concurrent writes to distinct keys | serialized inside one DB connection | filesystem-disjoint; no contention |
| Concurrent writes to same key | last-writer-wins, contents irrecoverable from history | last-writer-wins at filesystem; previous content recoverable via `git log -p` of the entry file |
| Reviewability of audit trail | binary; reviewer needs `sqlite3` CLI to inspect | markdown frontmatter; `cat`, `git blame`, GitHub PR diffs all work |
| Build-pipeline interface | export step → `LEXICON.md` | render step → `LEXICON.md` (same artifact) |
| Backup / restore | one binary file (must be quiesced) | `git` already does this, per-entry granularity |
| Dependencies | `sqlite3` gem (native build) | stdlib only |
| Indices / query planning | built-in B-trees | linear scan over ~50–200 files (ms-scale; non-issue at this size) |
| Definition prose with rich formatting | text column (lossy for code blocks, links) | native markdown body — first-class |

The decisive points: (i) the decision audit trail is the canonical record of how terminology became canonical, and a binary store would make it harder for reviewers to read; (ii) the data model is document-shaped, not relational (no joins, no foreign keys, no index-driven queries that aren't trivially fine at this size scanned linearly); (iii) per-entry `git diff` / `git blame` / GitHub PR review of terminology edits is genuinely load-bearing in the multi-agent workflow; (iv) the markdown body for prose definitions lifts terminology entries from one-line table cells to first-class explanatory artifacts.

## Atomicity contract (`safe_write`)

All entry writes, decision-event writes, and rendered LEXICON.md writes go through `safe_write` (defined in `bin/term`):

1. Write `content` to a sibling tempfile `<dest>.tmp.<pid>.<rand>` using `O_WRONLY | O_CREAT | O_EXCL`.
2. `fsync` the body to disk.
3. `File.rename(tmp, dest)` — POSIX `rename(2)` is atomic on the same filesystem (APFS, ext4, xfs all honor this).
4. On any error, the tmp is unlinked; the destination is untouched.

A reader concurrent with a writer always sees either the prior content or the new content — never a half-written file. A crash between fsync and rename leaves a `.tmp.<pid>.<rand>` artifact (harmless; never the destination); `bin/term validate` sweeps such artifacts older than 60s.

**Concurrent writes to the same slug are intentionally not serialized by a lock.** Last-writer-wins at the filesystem level. Real coordination happens through git: per-entry files mean conflicts are clean single-file merges, not corrupted shared stores.

## Schema — `terminology/entries/<slug>.md`

```markdown
---
slug: control-regret                      # MUST match filename basename
schema_version: 1
term: control regret                      # canonical lowercase prose form
name: Control Regret                      # display capitalization
notation: $\delta_{\text{regret}}$        # LaTeX form (drives NOTATION.md eventually)
brief: Best achievable minus current performance.
layer: prose-symbol                       # slug | prose-symbol | framing-vocabulary | public-api
status: canon                             # working | draft | canon | weak | deprecated | superseded
tags: [core_quantities, diagnostic]       # mixed semantic + flag tags; multi-section render
source_type: asf                          # asf | external | standard | mathematical | philosophical
primary_source: 01-aat-core/src/def-control-regret.md
first_asf_mention: 01-aat-core/src/def-control-regret.md
see_also: [satisfaction-gap]
aliases: []                               # acceptable variants (paired vocabulary, etc.)
do_not_confuse: []                        # external collisions to flag for readers
internal_note: null                       # agent-side metadata; never emitted to LEXICON.md
---

The gap between *best achievable* performance under current information and
*current* performance — "you're not doing it well enough." Pairs with
[satisfaction gap](satisfaction-gap.md) ($\delta_{\text{sat}}$, "the world doesn't
permit it") to form a 2×2 diagnostic: any failure-to-achieve decomposes into a
strategy/execution component (control regret) and a structural-impossibility
component (satisfaction gap). The split routes interventions — control regret
says *train harder / re-plan*; satisfaction gap says *change the goal or accept
the floor*.

Defined in [`#def-control-regret`](../../01-aat-core/src/def-control-regret.md).
```

**`brief:` is the one-line gloss** that appears in the rendered LEXICON.md table row. The markdown body is the longer definition — links, paragraphs, examples — that surfaces when a reader follows the entry's link from LEXICON.md.

**`notation:` field is reserved for the LaTeX form** that pairs with the term and will drive a future generated `NOTATION.md` (parallel to `bin/term render` for `LEXICON.md`).

**Field ordering on save is deterministic** (`Entry#frontmatter_yaml` orders fields canonically). This keeps git diffs clean across rewrites.

## Decision events — `terminology/decisions/<slug>/<ts>-<decider>-<action>.md`

Each naming decision is one file. Frontmatter + free-form note:

```markdown
---
slug: control-regret
action: canonicalize
decider: joseph
outcome: committed
timestamp: 20260508T143012Z
---

R2 cohort: 20 canonicalize votes / 6 architectures. No competing alts that
weren't pure formatting variants. Pair-binding with #def-satisfaction-gap is
load-bearing for the 2x2 diagnostic. Landed via batch C1 of TERMINOLOGY-TODO.
```

**Outcomes:** `committed` / `rejected` / `revised` / `superseded`. The latest event per action wins; older events stay as the audit trail (never delete).

**Actions** (defined in `bin/term`):

| Action | What it records |
|---|---|
| `canonicalize` | Existing name affirmed as canonical; no rename |
| `rename` | Name changed (old retired). Use `--from` / `--to` |
| `add-alias` | Parallel name added with role separation. Use `--form` |
| `add-cite` | First-encounter prior-art cite added (route-d adopted-standard cases) |
| `deprecate` | Name retired. Use `--replaced-by` if applicable |
| `supersede` | Name replaced by another entry. Use `--by-slug` for pointer |
| `update-gloss` | Definition refined; entry already exists |
| `nuance-flag` | Nuance noted on a canonicalize commitment. Use `--note` |

Action set is extensible — `bin/term decide` warns on unknown actions but does not block, so new event-type vocabulary can land before the CLI knows about it.

## Workflow

### Adding an entry

```bash
# Interactive scaffold (creates a stub at terminology/entries/<slug>.md)
bin/term add control-regret

# Or pipe full markdown on stdin
cat draft-entry.md | bin/term add control-regret
```

### Recording a decision

```bash
bin/term decide control-regret canonicalize --by joseph \
  --note "R2 cohort: 20 votes / 6 archs. Pair-binding with satisfaction-gap is load-bearing."

bin/term decide bias-bound rename --by joseph \
  --from bias-bound --to observation-ambiguity-bias-bound \
  --note "Citability fix per Criterion 9 route (a); names the phenomenon, drops Class-N reference."

bin/term decide multi-agent add-cite --by joseph \
  --note "Route (d) adopted-standard; first-encounter cite of Shoham & Leyton-Brown 2008 + Stone & Veloso 2000."
```

### Inspecting

```bash
bin/term show control-regret           # entry + decision history + segment cross-refs
bin/term list --tag core_quantities    # filter by tag, status, or layer
bin/term search "regret"               # fuzzy match by slug / term / name / brief
```

### Linting and validating

```bash
bin/term lint        # schema + cross-ref checks; exit 1 on any ERROR finding
bin/term validate    # round-trip load smoke-test; sweeps stale `.tmp.*` artifacts
```

`lint` surfaces three severities:
- `ERROR` — blocking (slug-mismatch, missing required fields like `term` / `brief`)
- `WARN` — surfaceable (missing optional fields, unknown status/layer values)
- `INFO` — informational (no segment references the slug — could mean term-only entry, not necessarily a problem)

The render step is **independent of lint** — `bin/term render` always emits LEXICON.md regardless of lint findings, marking missing fields as `(missing)`. This lets you see the current state of the world even when entries are mid-edit.

### Generating LEXICON.md

```bash
bin/term render                                  # writes terminology/_emitted/LEXICON.md (staging)
bin/term render --output LEXICON.md              # writes root LEXICON.md (refuses if hand-authored)
bin/term render --output LEXICON.md --force      # writes root LEXICON.md unconditionally
```

**Default destination is the staging path**, not the live root LEXICON.md. Until the existing hand-authored LEXICON entries have been migrated into `terminology/entries/`, rendering directly to the live LEXICON.md would replace real content with a partial generated view. Once migration is complete, change the default in `bin/term`'s `cmd_render` to `ROOT/'LEXICON.md'`.

**Clobber guard:** the renderer refuses to overwrite a destination file that does NOT carry the `Auto-generated` marker on its first ~5 lines, unless `--force` is passed. This catches accidental clobbers of hand-authored LEXICON.md or any other markdown file. Files that the renderer itself produced carry the marker and are overwritten freely.

Sections in LEXICON.md are thematic groupings driven by the `tags:` field on each entry. Display order for known tags (`cycle_phases`, `agent_classes`, `core_quantities`, etc.) is set in `Renderer::TAG_DISPLAY_ORDER`; unknown tags get appended alphabetically. Multi-tagged entries appear in each of their tag sections (intentional — let readers find a term via any of its semantic anchors).

Within each section, entries sort by `seq:` (ascending) first, then alphabetically by `term:` for entries without `seq:`. Use `seq:` on axis-keyed entries where taxonomy order matters — e.g., `seq: 1 / 2 / 3` for a three-value axis so entries render in logical rather than alphabetical order. Entries without `seq:` always sort alphabetically after any sequenced entries in the same section.

**Subgroups within a section** — add `subgroup: "Subgroup Name"` to entries that belong to a named sub-table within their tag section. Entries without `subgroup:` render first as a plain table (no sub-header); named subgroups follow as `### Subgroup Name` tables, ordered by the minimum `seq:` value of their entries (then alphabetically by subgroup name). Using a globally monotonic `seq:` space across the whole section drives both entry order within each subgroup and subgroup order naturally — e.g., seq 1–5 for the top-level entries, 10–14 for "Claim Postures", 20–25 for "Search Log Depth Tiers".

### Concurrency

Two agents can run any combination of `add` / `decide` / `render` / `lint` simultaneously without coordination as long as they don't both edit the *same* entry's markdown file. Decision events carry timestamps and never overwrite — concurrent decides serialize naturally on the filesystem.

## What is not (yet) here

- **Bootstrap importer from the existing LEXICON.md.** Decided 2026-05-08 to convert the existing handful of entries manually rather than build an importer; `bin/term import-from-markdown` was considered and skipped given the small population (small enough to hand-convert).
- **Per-entry `change_log:` field.** Decision events live separately in `terminology/decisions/`; this keeps entry frontmatter focused on current state and pushes history into the dedicated audit trail.
- **NOTATION.md emission.** Planned: a parallel `bin/term render --notation` (or separate verb) that emits NOTATION.md from entries with a `notation:` field. Same per-entry source, different generated view.
- **Auto-cross-ref between terms.** Currently `see_also:` is hand-maintained. A future pass might auto-detect cross-references from `do_not_confuse:` and bidirectional `see_also:` resolution.
