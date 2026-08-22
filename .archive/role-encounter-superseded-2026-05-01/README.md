# tools/role-encounter

Role-aware file-encounter tooling. Generates the canonical reading order an
agent should follow when arriving at this project in a particular role —
de-novo auditor, naming voter, normal contributor, or another role added
later. The orient walk becomes a parameter: given a role name, the project
knows the canonical reading order. Launch prompts no longer need to re-curate
"what should this agent read first" ad-hoc each cycle.

## What's in here

```
tools/role-encounter/
├── bin/
│   ├── build-encounter-table     # config + OUTLINEs + frontmatter → encounter-table.md
│   ├── role-view                 # per-role ordered file list, one role at a time
│   └── build-naming-context-map  # naming-target → defining segment + depends chain
├── config/
│   ├── roles.yaml                # role definitions (audit-safety, README variant, etc.)
│   ├── top-level.yaml            # per-file role-membership and ordering
│   └── segments.yaml             # OUTLINE traversal rules (incl. appendix-hoist)
├── views/
│   └── naming-context-map.md     # generated artifact: per-target segment anchor + chain
├── encounter-table.md            # generated artifact: full role-encounter table
├── encounter-data.json           # generated artifact: JSON intermediate (role-view reads this)
└── README.md                     # this file
```

## How to regenerate

The artifacts are generated from config + project metadata; routine updates
(new segments land, new top-level docs land) regenerate without re-launching
an agent — those updates are already captured in OUTLINE.md and segment
frontmatter.

```bash
# Regenerate the encounter table
ruby tools/role-encounter/bin/build-encounter-table

# Regenerate the JSON intermediate alongside (used by role-view)
ruby tools/role-encounter/bin/build-encounter-table --json-out=tools/role-encounter/encounter-data.json

# Regenerate the naming context map (touches every segment + master-list-curated.json)
ruby tools/role-encounter/bin/build-naming-context-map

# Verify on-disk matches regenerated (for pre-commit / CI)
ruby tools/role-encounter/bin/build-encounter-table --check
```

The role-view script regenerates the JSON intermediate automatically when any
config file is newer than the JSON, so calling `role-view` directly works even
on a fresh checkout.

## How to use the per-role view

```bash
# Markdown — suitable for human reading or pasting into a launch prompt
ruby tools/role-encounter/bin/role-view --role=de-novo-auditor

# Plain — one path per line, suitable for pipes
ruby tools/role-encounter/bin/role-view --role=naming-voter --format=plain

# JSON — machine-readable for downstream tools
ruby tools/role-encounter/bin/role-view --role=normal --format=json

# Required-only (skip available-but-not-required files)
ruby tools/role-encounter/bin/role-view --role=de-novo-auditor --required-only

# Show the deliberately-excluded list at the bottom (useful for understanding
# what the role is gated from and why)
ruby tools/role-encounter/bin/role-view --role=de-novo-auditor --show-excluded
```

## How to add a new role

Roles are defined in `config/roles.yaml`. To add one:

1. Pick a role name. The convention is kebab-case: `de-novo-auditor`,
   `naming-voter`, `audit-finding-triager`. Pick something that names
   *who the agent is* or *what the agent is doing*, not the file-subset.

2. Add a top-level entry under `roles:` with:
   - `description` — a sentence or two; this appears in the role-view output
     and the encounter table column header.
   - `audit_safe: true | false` — whether the role tolerates priming-heavy
     content (CHANGELOG, TODO, PROPOSALS). False for any role doing fresh-pass
     work that priming would corrupt.
   - `readme_variant: public | auditor` — `auditor` strips Findings / Recent
     Progress / Known Issues sections.
   - `include_segments: true | false` — usually true.
   - `include_components: [...]` — list of component dirs in scope. Default
     is all four; restrict only when the role is genuinely component-scoped.
   - `notes:` — a paragraph capturing the rationale. Future agents reading
     the config need your reasoning.

3. Add per-file role-membership entries in `config/top-level.yaml`. Each
   relevant file gets a `roles.<your-role>: { seq: N }` (hard sequence
   number), `band: <name>` (in-any-order group), or `excluded: true`
   (deliberately gated). Bands for the role are defined in the `bands:`
   block at the bottom of `top-level.yaml` — add new bands there if needed.

4. Run `ruby tools/role-encounter/bin/build-encounter-table` and check the
   generated table.

5. Run `ruby tools/role-encounter/bin/role-view --role=<your-role>` and
   check the role-view output.

## How to add a new top-level file

When a new top-level file lands (e.g., `KEYBINDINGS.md`, `ACK.md`, etc.):

1. Add an entry under `files:` in `config/top-level.yaml`:

   ```yaml
   - path: KEYBINDINGS.md
     roles:
       normal:           { band: conventions }
       de-novo-auditor:  { excluded: true, notes: "Not relevant to audit work." }
       naming-voter:     { excluded: true }
     notes: |
       Keyboard shortcut reference.
   ```

2. Use `seq: N` when ordering is load-bearing for the role; `band: <name>`
   when the file is part of an unordered cluster; `excluded: true` when the
   file would actively harm the role's work.

3. Run `ruby tools/role-encounter/bin/build-encounter-table` and verify.

The per-segment additions (new `src/*.md`) land automatically — the build
script walks every component's `src/` and reads the OUTLINE for ordering.
No config edit needed unless the new segment is treated specially.

## Source-of-truth ordering

- **Segment ordering** is the OUTLINE.md row order (per-component), top-to-
  bottom across components in the order the top-level OUTLINE.md references
  them. `bin/lint-outline` already enforces consistency with `depends:` —
  any backward-pointer that isn't an appendix-back-pointer is flagged as an
  ordering violation, so OUTLINE.md is trustable as the canonical narrative
  ordering. We do NOT compute a topological sort; the OUTLINE has done that
  work.

- **Appendix-after-first-mention** rule: when a main-section segment depends
  on an appendix segment (Section A, B in `01-aad-core/OUTLINE.md`), the
  build script hoists the appendix segment to read directly after the main
  segment. This matches paper-reading convention (proof comes after the
  claim that motivates it) and the de-novo audit instructions §4.2.

- **Top-level ordering** is hand-curated in `config/top-level.yaml`. Each
  per-role entry uses `seq:` (hard sequence) or `band:` (in-any-order
  group). The encounter table sorts top-level rows globally by min-seq
  across roles for stable display; role-view re-sorts per-role for the
  ordered view.

## Things deliberately not in the data model

- **Appendix-need frontmatter field.** Investigated: doesn't exist. The
  appendix-need is encoded entirely via `depends:` from main-section
  segments to appendix segments. lint-outline classifies these as
  "backmatter" references; the build script uses the OUTLINE's section
  column (A, B) to identify appendix segments. No need to add a `surfaces:`
  or `appendix_needed:` field; if a future cycle wants per-segment
  precision (e.g., when multiple main segments depend on an appendix),
  that becomes a separate naming/tooling cycle. See `config/segments.yaml`
  for the rationale.

- **`msc/` working artifacts.** `msc/spike-*.md`, `msc/AUDIT-WORKING-*/`,
  `msc/naming/*` are NOT in any role's view by default. They're priming-heavy
  for audit/voting, and `normal` uses `spikes/INDEX.md` and `audits/` as
  pointers. If a specific msc/ artifact (e.g., a round's launch prompt)
  becomes relevant for a role, enumerate it explicitly in `top-level.yaml`.

- **Per-segment role membership.** All segments are in every role's view
  (when the role's `include_segments: true` and the segment's component is
  in `include_components`). No per-segment exclusion mechanism. If that
  becomes useful (e.g., a role that only walks Section I), it's a small
  config-schema extension.

## Phase 2 — semantic index (separate, parallel work)

This tooling is Phase 1: deterministic, metadata-only. Phase 2 (running in
parallel as a memorata exploration spike) will add a Postgres+pgvector
semantic index over segments + top-level + working artifacts, enabling
heaviest-attention naming-target anchoring, cross-corpus search, and
provenance lookup. Phase 1 results — particularly the naming-context map —
are designed to be superseded by Phase 2's semantic version, not replaced
wholesale: the metadata-resolved targets stay valid; the concept-cluster and
unresolved targets gain anchors from semantic search.

## Smoke tests

A `--check` mode on `build-encounter-table` is suitable for pre-commit:

```bash
ruby tools/role-encounter/bin/build-encounter-table --check
```

It re-renders to memory and exits non-zero on drift. Run after any config
edit before committing the regenerated artifact.

For ongoing CI: regenerate is cheap (1-2 seconds for the encounter table,
~1 second for the naming context map), so CI can either `--check` (and
require regeneration) or regenerate-and-diff against HEAD.
