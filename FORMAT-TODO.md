# FORMAT-TODO.md — Volume Split, Hierarchy, Numbering, and Compliance Sweep

*Live plan for the cross-cutting cleanup decided over the monograph-build conversation 2026-05-11 / 2026-05-12. PRACTICA.md is the parent navigator; this file owns the detail. Supersedes the single-monograph plan from 2026-05-11 (preserved in git history at `5460fa9`).*

The framework ships as **four independent volumes**, one PDF per Part of the prior structure (AAD / TST / LogA / ELI). The earlier "everything in one ~600pp PDF" approach hit predictable limits — too big to digest, too unstable to cite when later volumes are still evolving, too slow to build during iteration. Volumes solve all four problems and let us drop back onto **kaobook's native hierarchy** instead of fighting it with custom counter machinery.

---

## The Decided Hierarchy

A ubiquitous shared vocabulary across source, tooling, and prose. Native LaTeX / kaobook semantics throughout.

| Level | Kaobook env | What it is | Examples |
|---|---|---|---|
| **Volume** (= Book) | `\documentclass{kaobook}` | One of the four theories, shipped as its own PDF | AAD, TST, LogA, ELI |
| **Part** | `\part` | A scope-boundary within a Volume; 1–5 per volume | "Adaptive Systems Under Uncertainty"; "Appendices: Details" |
| **Chapter** | `\chapter` | A grouping of segments within a Part; ~15 segments each (range ~5–25) | "Foundations"; "Mismatch & Gain"; "Persistence & Structural Adaptation" |
| **Section** (= Segment) | `\section` | A numbered claim unit; the 19 FORMAT types | Definition, Result, Derivation, Hypothesis, … |
| **Subsection** (= Field) | `\subsection` | A structural section *inside* a Segment | Formal Expression, Epistemic Status, Discussion, Findings, Working Notes |
| **Subsubsection** | `\subsubsection` | A named area *inside* a Subsection | "Search Log" inside Findings, "Linear case" inside Formal Expression |

**Atoms** (equations, tables, figures, named formulas) sit *within* Subsections and are numbered by kaobook's native counters.

**Vocabulary discipline:**
- "Volume" is the published artifact (one PDF). "Book" is the conceptual unit. They are interchangeable in casual prose; "Volume" is preferred when emphasizing the publication.
- The four-Volume structure means each Volume's *Part* level is what we previously called a "Section" of the monograph.
- The new **Chapter** level fills the grouping gap between Part and Segment — readers got from "scope boundary" to "Definition I.1" with no organizing intermediate.

---

## The Numbering Scheme

Kaobook native, no custom counters:

- **Part**: Roman (I–N) per volume, kaobook default
- **Chapter**: arabic, reset per Part (Part I → Chapters 1, 2, 3; Part II → Chapters 1, 2; etc.)
- **Section** (= Segment): arabic, reset per Chapter; cross-ref display via cleveref → `Section 1.2.3` or just `1.2.3` depending on context
- **Subsection / Subsubsection**: native, generally not cross-referenced
- **Atoms**: equation/table/figure counters; **reset per Section** so atom IDs stay stable under segment-internal reordering. Display: `(1.2.3.1)` or just `(1.2.3-1)` — TBD during implementation

**Named-atom evergreen cross-refs**: the name token from `*[Type (name, from ...)]*` eq-tags is the atom's intrinsic identity. The renderer extracts that name and emits `\label{atom:<name>}` on the equation so `#<name>` resolves directly, independent of positional numbering. Same convention applies to named definitions, derived items, etc.

**Cross-reference evergreen-ness principle**: cross-refs always target intrinsic identity (slug for segments, name for atoms), never positional numbers. The renderer produces the rendered number at compile time; the source never hardcodes one.

---

## Cross-Volume References

Volumes are standalone PDFs but routinely reference each other. Two-tier strategy:

1. **Primary (when all volumes are built together)**: `xr-hyper` package reads sibling volumes' `.aux` files and produces clickable cross-PDF links with proper section numbers. `.aux` files are version-controlled so they're available to any volume's build.
2. **Fallback (when sibling `.aux` files aren't present)**: cross-volume refs render as a bibliography-style citation pointing to the sibling volume by its DOI / citation key — e.g., "see Wecker (2026), §1.2.3" — so a reader with only one volume in hand gets a usable reference. Each volume publishes a standard bibliography entry for itself, citable by sibling volumes.

The build script handles the discovery: if a sibling `.aux` exists, use xr-hyper; otherwise fall through to the bibliography form.

**Bibliography, other frontmatter, other backmatter**: full design deferred to a later discussion. Captured here as a TODO so it doesn't get lost.

---

## Versioning Per Volume

Each Volume has its own semantic version, independent of the others. AAD can be v1.0 (stable, citable) while LogA is at v0.3 (still evolving).

- **`bin/output-version <volume-id> bump <patch|minor|major>`** utility — increments the version, resetting lesser components to zero. `<volume-id>` is the `01`/`02`/`03`/`04` prefix (or the slug `aad`/`tst`/`loga`/`eli` — TBD during implementation).
- VERSION files live in each component directory (`01-aad-core/VERSION` etc.).
- **Build stem**: `<volume-id>-v<semver>.pdf` (e.g., `aad-v0.1.0.pdf`) — *no `+<sha>` suffix in filename.* Filename = the released version.
- **Git short-SHA shown in volume frontmatter** (and PDF metadata), not the filename. Frontmatter reads e.g. "Build: v0.1.0 · `758cd89` · 2026-05-12" so the build is traceable without polluting the filename.
- For incremental builds during development (no version bump), the stem stays as the last released version; the frontmatter SHA distinguishes which build the reader is looking at. If we need a workspace-dirty marker for development builds, frontmatter can show `758cd89-dirty` or similar.

---

## Smart Rebuilds

A Volume rebuilds only when something it depends on changed. Sources of change:

- **Source files** of the Volume's component dir (`<component>/src/*.md`, `<component>/OUTLINE.md`)
- **Shared build infrastructure** (`mono/preamble/`, `mono/lib/`, `bin/build-monograph`) — these affect every Volume
- **Bibliography database** (when it lands)
- **Sibling volumes' `.aux` files** (for xr cross-references)
- **Explicit version bump** via `bin/output-version`
- **`--force` flag** for cases where the cache is wrong or the user wants to be sure (especially after preamble/script edits — even though those should trigger by themselves via shared-infrastructure detection)

Implementation candidates:
- **`latexmk`**: detects file changes and reruns lualatex/biber as needed. Standard, robust.
- **Per-volume hash cache**: build script computes a content hash over the volume's inputs (source files + shared infra + biblio); skips rebuild if hash unchanged. Simpler than latexmk for our needs.
- **`\includeonly` / kaobook subfiles**: for chapter-level incremental compile *within* a volume. Useful during heavy editing of one chapter. Possibly overkill for now; revisit if per-volume builds get slow.

Probably start with the per-volume hash cache (simpler, fits our build script), and add latexmk-style or `\includeonly` later if needed.

---

## Implementation Plan, by Phase

Phases assume each predecessor has landed. Phase 1a (ToC) is independent and can land first.

### Phase 1a — Per-Volume Table of Contents

- [ ] Each Volume's build emits a ToC in front-matter
- [ ] Native kaobook `\tableofcontents`
- [ ] Decide `secnumdepth` (probably 3 — through Section/Segment, not deeper)
- [ ] `--no-toc` flag and/or `toc: false` signal in OUTLINE.md frontmatter to suppress

### Phase 1b — Volume Split (Build Pipeline)

- [ ] Build script accepts `--volume <id>` to build one volume; `--all` to build the four
- [ ] Each Volume's build reads its `<component>/OUTLINE.md` as entrypoint
- [ ] Output: `<vol>-v<semver>.pdf` in repo root or per-component dir
- [ ] Per-volume `VERSION` files; per-volume `.aux` retention
- [ ] `bin/output-version <vol> bump <level>` utility

### Phase 1c — Native LaTeX Hierarchy (Renderer)

- [ ] Map outline H2 → `\part`, H3 → `\chapter`, segment → `\section`
- [ ] Drop the custom `\segment` counter and `\thesegment` overrides
- [ ] Migrate per-segment-type rendering (tints, status badges, stage glyphs, header strip) onto a `\segheading` macro that wraps `\section` with the styling
- [ ] Update cleveref formats to use native section counters (`Section 1.2.3` etc.)
- [ ] Atoms (equation/table/figure) — reset per Section, named-atom labels via `*[Type (name, ...)]*` extraction

### Phase 1d — Cross-Volume References

- [ ] `xr-hyper` integration in each Volume's preamble, configured to read sibling Volumes' `.aux` files
- [ ] `.aux` files persisted and version-controlled (`<component>/<vol>.aux`)
- [ ] Cross-volume ref fallback: when sibling `.aux` not present, render as bibliography citation
- [ ] Each Volume publishes a standard bibliography entry for itself (for sibling-volume citations to consume)

### Phase 1e — Smart Rebuild

- [ ] Per-volume input hash cache (source files + shared infra + biblio + sibling-aux digests)
- [ ] Skip lualatex run when hash unchanged
- [ ] `--force` flag bypasses the cache
- [ ] Version-bump always triggers rebuild

### Phase 2 — Documentation

- [ ] Update `FORMAT.md` with new vocabulary (Volume / Part / Chapter / Section / Subsection / Subsubsection) and the named-atom evergreen cross-ref convention
- [ ] Update `CLAUDE.md` references to the hierarchy
- [ ] Decision-record: this file is the live record until docs catch up

### Phase 3 — OUTLINEs (Source-side Structural Work)

- [ ] In each component `OUTLINE.md`, introduce H3 chapter headings between Part-level H2s and segment tables. Joseph chooses the chapter groupings (with build-side help on dependency-cluster analysis if useful)
- [ ] For Parts with only one Chapter, the source can use a placeholder H3 ("Chapter 1: All segments") until proper grouping is decided
- [ ] Strip manual numbering from Part and Chapter titles (LaTeX numbers them now)
- [ ] Decide whether table section-codes (`| S |` / `| I |` / `| E1 |` / `| L1 |`) get normalized — optional, defer if not blocking

### Phase 4 — Source segments: cross-ref hygiene

- [ ] **Class A** broken slug refs: validate every `#slug-name`, fix typos / stale renames, mark genuinely missing targets
- [ ] **Class B** inline pseudo-refs (`Prop A.1`, `Step 4`): decide promote-to-named-atom vs. leave-as-prose per case
- [ ] **Named-atom cross-ref audit**: confirm names from `*[Type (name, ...)]*` tags are unique within their segment / volume scope; verify `#name` resolves to the right atom
- [ ] **Cross-volume cross-ref audit**: identify refs that target a sibling Volume; verify they resolve via xr-hyper

### Phase 5 — Source segments: FORMAT compliance (linter)

- [ ] `bin/lint-md --fix` for auto-fixable categories (hard-wraps, emphasis-underscores)
- [ ] Manual / agent-driven sweep for math compatibility (`|`/`\|`/`<`/`>`/`*` in math)
- [ ] `\text` outside `$` per-instance review
- [ ] Other linter findings (~200+ total)

### Phase 6 — Deferred / Optional

- [ ] **Bibliography, frontmatter, backmatter** design — full discussion deferred to a later session
- [ ] **Per-volume preamble / preface** — short reader-orienting text at the start of each Volume; tone is conversational, framework-positioning
- [ ] **Companion PDFs** — specialized cuts (selected chapters, theme-based) for particular audiences; future work
- [ ] **`\includeonly` chapter-incremental builds** — only if per-volume builds become uncomfortably slow
- [ ] **Section letter codes** normalization in OUTLINE tables
- [ ] **Slug rename audit** — separate concern, naming-cycle work

---

## Sequencing notes

- **Phase 1a (ToC)** is independent and lands first as a quick win.
- **Phase 1b (volume split) and 1c (native hierarchy) land together** — they're tightly coupled; splitting volumes without dropping the custom counter machinery is more work than doing both at once.
- **Phase 1d (xr cross-refs) follows 1b** — once volumes exist, cross-volume refs become a thing.
- **Phase 1e (smart rebuild)** can land anytime after 1b/1c — it's an optimization, not a correctness fix.
- **Phase 2 (docs)** can run in parallel with Phase 3 once Phase 1 lands.
- **Phase 3 (chapter introduction)** can run in parallel for each component; Joseph drives one component while a sub-agent could draft the strawman for others.
- **Phases 4 and 5 (cross-ref + FORMAT cleanup)** delegate cleanly to an agent once Phase 3 stabilizes the source structure.

---

## What this plan does NOT change

- Slug names themselves (canonical segment IDs)
- The substance of segment content
- The segment promotion stages (FORMAT.md §Promotion Workflow)
- The four-Volume top-level structure (decided)
- Existing cross-ref slug syntax (`#slug-name`) — the surface convention stays; only what it resolves to changes
- The kaobook visual register already built (tints, status badges, eq-tag marginnotes, Working Notes panels, Tufte tables, italic teal, mono olive, navy refs) — 100% portable to the new structure

---

## Status

Created 2026-05-11 (v1: single-monograph plan); rewritten 2026-05-12 (v2: four-volume plan). Currently Phase 0 — plan written. Phase 1a (ToC) is the immediate quick win. Phase 1b/1c (volume split + native hierarchy) is the substantive work that lets everything downstream land.
