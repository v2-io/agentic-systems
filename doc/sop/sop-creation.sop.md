# Creating and extending SOPs — the `doc/sop/` convention

> [!note]
> **Status:** authoritative (the convention itself; the home is young and still filling in).
> **Owns:** what an SOP is in this repo, how SOP files are named and how they branch, and how to create or extend one. The first SOP written — every other SOP inherits this convention.
> **See also:** [`../../msc/sop-consolidation-design-2026-06-01.md`](../../msc/sop-consolidation-design-2026-06-01.md) (the inventory + migration plan this home executes) · `CLAUDE.md` (the auto-loaded disposition + index layer this home is the on-demand complement to).

## What an SOP is here — and what is not

An **SOP** is a *procedure*: a repeatable how-to-do-a-thing with steps, an enum, or a decision tree — the audit walk, spike disposition, the naming cycle, segment-promotion mechanics, the build pipeline, multi-agent methods, commit hygiene. SOPs live here, in `doc/sop/`, stated once and authoritatively, read on demand.

What does **not** belong here is **disposition** — *how to BE*: the truth-honoring stance, the failure-mode body-signals (the *"therefore"* trigger; the urge to write *"this is not a weakening"*), peer-voice, strengthen-before-soften-as-reflex, the collaboration posture with Joseph. Disposition is texture, not checklist, and it has to be *present* at the load-bearing moment — so it stays in the auto-loaded layer (`CLAUDE.md` + the memory files), which a procedure file you must remember to open cannot do.

The cut is the test: **if it fires a reflex, it is disposition (auto-loaded); if you follow it step by step, it is procedure (an SOP).** Many disciplines have both halves — strengthen-before-soften is a *disposition* (the reflex that catches the easy soften) *and* the audit SOP encodes the *procedure* the reflex triggers. Put each half in its layer, and have one point at the other.

## The two-layer shape (defer-don't-fork)

`CLAUDE.md` (auto-loaded) carries the **index, the disposition, and the before-action triggers**; `doc/sop/` (on-demand) carries the **procedure**. A trigger is the seam: *"before softening an audit finding, see the audit sop."* This mirrors the proven global pattern — `~/.claude/CLAUDE.md` (index + disposition) ↔ `~/.claude/memory/` (detail) — scaled into the project.

The binding discipline is **defer-don't-fork**: each rule is stated *once*, in its home; everywhere else *references* it. When a rule moves into an SOP, the old site is **reduced to a pointer, not left as a softened duplicate** (integration-is-replacement, at the document level). A rule restated in two places drifts; a rule stated once and pointed at cannot.

## File and naming convention

The topic is the stable identity; `.sop` is its namespace marker; leaf-vs-branch is shown by file-vs-directory.

- **Leaf topic** → a single file: `doc/sop/<topic>.sop.md`.
- **Branching topic** → the `<topic>.sop.md` file becomes an *index*, and its pieces live in a sibling directory `doc/sop/<topic>.sop/<piece>.sop.md`. The index file and the directory coexist (one ends in `.md`, one does not — no filesystem collision). A piece may itself branch the same way (`<piece>.sop/<sub-piece>.sop.md`), so the tree grows organically only where a topic actually needs the room.
- **Resolution rule** — *"see the X sop"* means: open `doc/sop/X.sop.md` first; if it is an index, follow it into `doc/sop/X.sop/`.
- **Master index** → `doc/sop/sop.md` (planned, not yet built — deferred until we know whether it would be too redundant with `CLAUDE.md`'s index; see *Status of this home*).

Worked illustration: FORMAT will be interred here as `format.sop.md`. Because it is large (frontmatter, cadence, promotion gates, voice-and-provenance, working notes, equation tags, …), it will branch — `format.sop.md` becomes the index and the pieces land as `format.sop/formal-expression.sop.md`, `format.sop/promotion-gates.sop.md`, and so on.

## Creating or extending an SOP

1. **Confirm it is procedure, not disposition** (the reflex-vs-step test above). If it fires a reflex, it belongs in `CLAUDE.md` / memory, not here.
2. **Find or make the home.** One file per discipline-cluster. Start as a leaf `<topic>.sop.md`; branch to `<topic>.sop/` only when the single file genuinely strains. Do not pre-fragment — organic growth, not speculative directories.
3. **State it once.** Write the procedure in the SOP. If it currently lives elsewhere (CLAUDE.md, a memory, a working doc), **move it** and leave a one-line pointer behind. Verify against the primary source first — migration is replacement, and a half-moved rule is worse than an unmoved one.
4. **Header.** Open every SOP with the status callout: **Status** (authoritative / draft / planned-stub), **Owns** (the one-line scope — the rule that lives here and nowhere else), **See also** (adjacent homes + the disposition triggers that point in). This keeps the home greppable and makes single-sourcing auditable.
5. **Honest marking + freshness.** A planned-but-unwritten topic is a *stub* and says so (an empty authoritative-looking file is a landmine here). What is written stays true; pointers stay live. Freshness is binding; completeness is not — a half-filled home honest about its gaps beats a full one that lies about them.

## Status of this home (2026-06-01)

Young and filling in. The topic set is touched as stubs ahead of migration: `audit`, `spikes`, `naming`, `multi-agent` (new — currently sole-carried in project memory), `git-hygiene` (new — same), `build-pipeline`, `format` (will branch). The migration order, the manual-interment plan (the big audit manuals and FORMAT relocate here and branch), and the per-source map live in the design doc linked above. The master index (`sop.md`) and the question of how `doc/sop/` and `CLAUDE.md` divide the indexing role are deliberately deferred until the gathering-and-ordering is further along.

## Near-future work to mine

- **The global `~/.claude/CLAUDE.md` is overloaded too**, and carries a fair amount of ASF-specific material that wants mining into this project layer (or its own consolidation). Out of scope for the project-layer pass that opens this home — but flagged here so it is not lost. A global-layer pass is the natural successor, on its own seam.
- **Project memory is the immediate source.** The sole-carrier method / git-hygiene memories migrate into `multi-agent.sop.md` / `git-hygiene.sop.md`; the duplicates thin to pointers; `MEMORY.md` (currently over its load limit, so silently truncating) comes back under budget as that bulk drains. Do the index curation in the same batches as the extraction, not as a deferred pass.

## Provenance

First SOP in `doc/sop/`, written 2026-06-01 to seed the convention every other SOP inherits. Backed by the six-cluster inventory synthesized in [`../../msc/sop-consolidation-design-2026-06-01.md`](../../msc/sop-consolidation-design-2026-06-01.md).
