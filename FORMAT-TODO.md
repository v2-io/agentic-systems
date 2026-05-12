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

**Appendices** are an exception to the Part→Chapter→Section nesting: each appendix segment renders directly as a `\chapter` under an `\appendix\part{...}` group. There is no intermediate Chapter level inside Appendices — an appendix segment *is* a chapter-level entity, independent. Multiple `## *Appendices* <name>` groups per volume are allowed (AAD has two: "Details" and "Operational Domains").

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

## Per-Volume Metadata: `mono-meta.yaml`

Each volume directory (`0N-*/`) carries a `mono-meta.yaml` declaring its display title, short tag, cover image, outline entrypoint, and version. The build script reads it to drive volume-specific behavior; defaults kick in for any missing keys.

**Schema** (loose; extend as needs surface):

```yaml
title:       "AAD: Adaptation and Actuation Dynamics"   # full display title
short_title: AAD                                        # running heads, refs, filenames
slug:        aad                                        # bin/build-monograph + output-version id
major:       0
minor:       1
patch:       0
outline:     OUTLINE.md                                 # entrypoint, relative to dir
cover_svg:   AAD-cover.svg                              # full-page cover image
```

Version components are explicit (`major` / `minor` / `patch` as separate keys, not a single `version: 0.1.0` string) so `bin/output-version` can read/write them cleanly. The canonical version lives here; no separate `VERSION` file.

---

## Volume Frontmatter Sequence

Every Volume's frontmatter renders in this fixed order:

1. **Cover** — from the volume's `cover_svg` (declared in `mono-meta.yaml`); rendered via `rsvg-convert` to a single-page PDF and `\includepdf`-ed as the first page. Volumes without a configured cover skip this step.
2. **Title page + Copyright** (combined on one page) — full title, author(s), license declaration (CC BY-SA — All Rights Reserved unless reassigned), citation block (canonical citation form for sibling-volume cross-references), and build-info stamp (`\buildsemver` / `\buildsha` / `\builddate` injected by the build script via `build-info.tex`).
3. **Table of Contents** — kaobook `\tableofcontents`, depth TBD (probably through Section so segments appear by name). Suppressible via `--no-toc` flag or `toc: false` in `mono-meta.yaml`.

Backmatter (bibliography, index, colophon) and the Title-page typographic design are deferred to a later session (see Phase 6).

---

## Build-Info Stamp

The build script emits `build-info.tex` into the staging directory on every build, defining:

- `\buildsemver` — semver from the volume's VERSION file
- `\buildsha` — current git short-sha, with `-dirty` suffix when the working tree has uncommitted changes
- `\builddate` — ISO date (YYYY-MM-DD)

The preamble inputs this file early so the title page / colophon can render the build provenance. Filename of the PDF carries semver only — `<short-title>-v<semver>.pdf`. Each build overwrites the same file; the previous build is snapshotted as `.prior.pdf` before being overwritten.

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

- **`bin/output-version <volume-id> bump <patch|minor|major>`** utility — increments the version (resetting lesser components to zero) by editing the volume's `mono-meta.yaml` directly. `<volume-id>` is the `01`/`02`/`03`/`04` prefix or the slug `aad`/`tst`/`loga`/`eli`.
- Version lives in each component's `mono-meta.yaml` (`major` / `minor` / `patch` keys). No separate `VERSION` file.
- **Build stem**: `<short-title-lower>-v<major>.<minor>.<patch>.pdf` (e.g., `aad-v0.1.0.pdf`) in `mono/`. Filename = the released version.
- **Git short-SHA shown in volume frontmatter** (and PDF metadata), not the filename. Frontmatter reads e.g. "Build: v0.1.0 · `758cd89` · 2026-05-12" so the build is traceable without polluting the filename.
- For incremental builds during development (no version bump), the stem stays as the last released version; the frontmatter SHA distinguishes which build the reader is looking at. Workspace-dirty marker (`758cd89-dirty`) when the working tree has uncommitted changes.

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

- [ ] **Restructure mono/ as output-only.** mono/ holds PDFs, markdowns (when emission lands), `.build/` staging, README, .gitignore. Move build infrastructure (`main.tex`, `preamble/`, `lib/`, `vendor/`) into a new `common/` directory.
- [ ] **CLI shape**: `bin/build-monograph aad` (or `01`, `tst`, `02`, etc.) builds one volume; `bin/build-monograph --all` builds all four in dep order. Bare invocation defaults to `--all`. No `--volume` flag — the positional arg is the volume id.
- [ ] **Per-volume PDF output** at `mono/<short-title>-v<major>.<minor>.<patch>.pdf`.
- [ ] Each Volume's build reads its `<component>/OUTLINE.md` as entrypoint and its `<component>/mono-meta.yaml` for version + cover + title.
- [ ] **Per-volume `.aux` retention**: on successful build, copy the volume's `.aux` out of `.build/` into the volume's component dir (e.g., `01-aad-core/aad.aux`); sibling builds read these for Phase 1d xr-refs.
- [ ] Version + frontmatter wiring: `bin/output-version` reads/writes `mono-meta.yaml`; the build-info stamp continues using `\buildsemver` (constructed from `major.minor.patch`) / `\buildsha` / `\builddate`.

### Phase 1c — Native LaTeX Hierarchy (Renderer)

- [ ] Map outline H2 → `\part`, H3 → `\chapter`, segment → `\section`
- [ ] Drop the custom `\segment` counter and `\thesegment` overrides
- [ ] Migrate per-segment-type rendering (tints, status badges, stage glyphs, header strip) onto a `\segheading` macro that wraps `\section` with the styling
- [ ] Update cleveref formats to use native section counters (`Section 1.2.3` etc.)
- [ ] Atoms (equation/table/figure) — reset per Section, named-atom labels via `*[Type (name, ...)]*` extraction

### Phase 1d — Cross-Volume References + Persisted `.aux`

- [ ] `xr-hyper` integration in each Volume's preamble, configured to read sibling Volumes' `.aux` files
- [ ] **`.aux` files persisted and version-controlled** — each successful Volume build copies its `.aux` (and any auxiliary metadata cleveref needs) out of `.build/` into the volume directory (e.g., `01-aad-core/aad.aux`) and that artifact is committed. Sibling builds read these committed `.aux` files for cross-volume label resolution.
- [ ] Cross-volume ref fallback: when sibling `.aux` not present (or version-mismatched), render as bibliography citation pointing to the sibling volume's canonical citation form
- [ ] Each Volume publishes a standard bibliography entry for itself (declared in `mono-meta.yaml` or a sibling `cite-self.bib`) so sibling-volume citations consume it
- [ ] `.aux` staleness detection: warn or error when a sibling `.aux` was written against a different sibling-volume semver than the one being referenced

### Phase 1e — Smart Rebuild

Per-volume hash cache so a Volume rebuilds only when its inputs actually changed. Triggers:

- Source files inside the Volume's component dir (`<component>/src/**`, `<component>/OUTLINE.md`, `<component>/mono-meta.yaml`)
- Shared build infrastructure (`mono/preamble/**`, `mono/lib/**`, `bin/build-monograph`, `bin/output-version`)
- Bibliography database (when it lands in Phase 6)
- Sibling Volumes' persisted `.aux` files (xr cross-refs may change)
- VERSION file change (always rebuilds, regardless of source-hash)
- `--force` flag (manual override)

Implementation:

- [ ] Per-volume input-set definition — what files contribute to the hash
- [ ] Hash computation + cache (`mono/.build/<volume>/.input-hash`)
- [ ] Skip-when-unchanged path in the build script
- [ ] `--force` flag plumbed through
- [ ] Version-bump triggers unconditional rebuild
- [ ] `bin/build-monograph --all` builds dirty volumes in dependency order (so a downstream volume rebuild can see the upstream volume's freshly-written `.aux`)

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

- [ ] **Table dynamic-shrinking heuristic** — most tables don't shrink to fit content even when they could; auto-detect overflow and scale (via `\resizebox` or stepping `\footnotesize → \scriptsize` for very wide tables). Goal: more tables fit on one page without per-table source intervention.
- [ ] **Backmatter design** — bibliography, index, colophon; full layout and content discussion deferred to a later session
- [ ] **Title-page typographic design** — current implementation is the minimum (title + author + build-info); proper typography for license block, citation form, etc. deferred
- [ ] **Per-volume preface** — short reader-orienting text at the start of each Volume (between ToC and Part I); tone is conversational, framework-positioning
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

## Progress Snapshot (2026-05-12, end-of-day)

**Landed (committed):**
- ✅ Phase 1a (per-volume ToC) — `\tableofcontents` emitted in `\frontmatter` scope from `common/main.tex`; `secnumdepth = 3` (parts/chapters/sections all numbered); `tocdepth = 3`; opt-out via `mono-meta.yaml` `toc: false` and CLI `--no-toc`; build-info macro `\ifvolumetoc` gates the emission
- ✅ Phase 1b (volume split) — `bin/build-monograph <volume>` and `--all`; each volume builds to `mono/<slug>-v<M>.<m>.<p>.pdf`; per-volume `.aux` persisted to `<component>/<slug>.aux` for Phase 1d
- ✅ Phase 1c (native kaobook hierarchy) — `outline_walker.rb` parses role-prefix convention; build pipeline emits `\part` / `\chapter` / `\section` natively. Section-level segments drive off kaobook's native `section` counter (custom `\segment` counter retired); appendix segments render as `\chapter` via `\segmentappendixchapter` so an appendix segment *is* its chapter (the FORMAT-TODO design). `\appendix` resets the chapter counter and our `\thechapter` override uses `\AlphAlph` so appendix chapters are A, B, …, Z, AA, AB, … with overflow protection. Cleveref formats overridden for both `section` and `chapter` counters so `\cref{seg:foo}` renders as a bare number (matching the existing prose convention "see Definition #def-foo" → "see Definition 1.4" or "see Derivation A").
- ✅ Directory restructure: `mono/` is output-only; `common/` holds main.tex / preamble / lib / vendor / kaobook
- ✅ `mono-meta.yaml` schema landed (`title` / `short_title` / `slug` / `major`/`minor`/`patch` / `outline` / `cover_svg` / `toc`)
- ✅ `bin/output-version <slug> show|bump <patch|minor|major>` operates on `mono-meta.yaml` directly
- ✅ Cover-page rendering (rsvg-convert) — AAD cover working; other volumes need covers authored. Cover-page emission lifted out of `body.tex` into `main.tex` frontmatter via the `\volumecoverpath` build-info macro, so the frontmatter sequence is cover → ToC → mainmatter.
- ✅ Build-info stamp (`\buildsemver` / `\buildsha` / `\builddate` / `\volumetitle` / `\volumeshorttitle` / `\volumeslug` / `\volumecoverpath` / `\ifvolumetoc`); dirty-tree detection
- ✅ All-arabic numbering register — chapters and chapter-prefixed equation/table/section references render as arabic (`3.5`, `Table 3.1`, `Definition 3.4`). Parts retain Roman (kaobook default, standard convention).

**Mid-flight:**
- 🚧 AAD's `OUTLINE.md` reorganized into the role-prefix convention with chapters; Parts II/III/IV awaiting source-side reorganization (current implicit-Chapter default lets them build)
- 🚧 Cover artwork: AAD done; TST / LogA / ELI pending
- 🚧 Build-info macros declared but the title page that consumes them is minimal — proper title-page+copyright layout pending (Phase 6)

**Not yet started:**
- ✅ **Markdown-first restructure (landed across Stages 1–3)** — design at [`msc/markdown-first-pipeline.md`](msc/markdown-first-pipeline.md). The pipeline runs as a chunked intermediate flow: `source-outline + source-segments → index + chunks → assembled markdown → LaTeX → PDF`. The duplication between the (retired Python) `bin/build` and the Ruby `build-monograph` walks is gone; the assembled markdown is the canonical citable artifact and the PDF is one rendering of it.
  - ✅ **Stage 1 (ingest)** — `common/lib/ingest.rb` walks `OUTLINE.md` and produces `mono/.build/<slug>/{index.md, chunks/*.md}`. Each chunk is print-ready markdown with the documented metadata-block contract. Per-section academic numbering native; appendix chapter letters via `\AlphAlph`. Source hashes recorded for incremental-rebuild support (not yet implemented; the per-chunk hashing is in place for the next pass).
  - ✅ **Stage 2 (assemble)** — `common/lib/assemble.rb` stitches index + chunks into the canonical per-volume markdown at `mono/<slug>-v<sem>.md`. Cross-refs resolved to `[Type N.M](#slug)` anchor links. The Python `bin/build` legacy moved to `_obs/bin-build-superseded-2026-05-12.py`.
  - ✅ **Stage 3 (typeset)** — `common/lib/typeset.rb` converts assembled markdown to LaTeX via `Kramdown::Converter::AsfVolumeLatex`. Role-prefix italic on H2/H3 maps to `\addchap` / `\part` / `\chapter` / appendix-with-`\AlphAlph`; segment headers with metadata block become `\segmenthead` / `\segmentappendixchapter`. Segment-internal subhead transitions (epigraph open/close, wide-section for Discussion/Findings, workingnotes wrapper) use level-aware wrapper closing so nested H6 subheads inside Working Notes don't prematurely close the wrapper. `\mainmatter` boundary emitted exactly once on the first `*Part*` / `*Appendices*` crossing. Resolved cross-refs `[Type N.M](#slug)` route through `\cref{seg:slug}` for bare-number rendering. HTML anchors suppressed. `main.tex` simplified to `\input{body}` (typeset output handles frontmatter / mainmatter scope transitions internally).
  - Verified end-to-end across all four volumes: AAD 489p (vs prior 489p), TST 56p (vs 55p), LogA 61p (vs 61p), ELI 53p (vs 54p). The ±1-page deltas are layout-level (slight spacing differences around section transitions); no fatal LaTeX errors; wrapper begin/end pairs all balance.

**Distinct from the broader doc/schema work:**

- ⬜ **Distinct schema for Discussion-type segments (FORMAT.md update)** — claims and discussions need a structural distinction in FORMAT.md. Claim segments carry Formal Expression / Epistemic Status / Discussion / Findings subheads because those are the load-bearing parts of an epistemic-architecture claim. Discussion segments — chapter intros, scope meta-discussion, meta-segments like the M-series — don't need Formal Expression or Epistemic Status sections; they're not propositions defending themselves, they're orientation prose. The current schema asks them to fake those subheads with placeholder content. FORMAT.md should split: claim schema (current) vs discussion schema (just body, with the subheads optional rather than required). Joseph 2026-05-12.
- ⬜ **Incremental rebuild (per-chunk hash cache)** — the index.md frontmatter records source hashes for every chunk, but ingest still re-emits all chunks on every build. The next pass should: (a) read the prior index.md if present, (b) for each segment-chunk entry, compare current source-file hash to recorded hash, (c) skip regeneration when unchanged. Same discipline at the outline level for the index itself. Stage 1 of the pipeline already supports this architecturally — it's an implementation pass, not a redesign.
- ⬜ Phase 1d — xr-hyper cross-volume refs, sibling-volume citations
- ⬜ Phase 2 — FORMAT.md / CLAUDE.md doc sweep (vocabulary alignment with the role-prefix / native-hierarchy / chunk-format conventions)
- ⬜ Phase 3 — chapter introduction across Parts II/III/IV of AAD + other components
- ⬜ Phase 4 — cross-ref hygiene sweep
- ⬜ Phase 5 — FORMAT-compliance linter sweep
- ⬜ Phase 6 — backmatter design, title-page typography, per-volume preface, dependency-graph SVG → PDF pipeline for image rendering

**Table rendering deferred items** (logged in source-level TODOs at `common/lib/segment_renderer.rb` `convert_table`):
- Narrow-direction adaptation: a wide-area table whose content would fit body width could be narrowed to match the surrounding prose column (Table 7.2 example, rare enough to defer).
- Snap-to-content-width: when a column's normalized weight is just slightly under one of the actual cell widths (within an epsilon), snap up to that cell width to avoid wrapping by just a few characters.
- Source-side math reflow: a handful of display equations (e.g., the 254.9pt one at AAD line 7506) are inherently wider than the page and don't break naturally. Author-side line-break decisions needed — `\\` or `aligned` blocks in the source.

**Tighter typography candidates:**
- Status badges + stage glyphs on appendix-chapter headings render as a small indicator strip below kaobook's chapter glyph — could be promoted into the chapter heading itself once a tighter visual register is decided.
- Appendix-chapter ToC entries use the `\chapter[short]{rich}` two-arg form so the ToC stays compact. If further compression is wanted, a custom `\l@appendixchapter` style is the next step.
- Cover artwork for TST / LogA / ELI not yet authored (AAD's cover lives at `01-aad-core/AAD-cover.svg`).
- Title page is minimal — proper layout per the frontmatter sequence spec (Cover → Title + Copyright → ToC) is Phase 6.

---

## Handoff Notes (current as of end of 2026-05-12)

**State of the build:** all four volumes build cleanly via `bin/build-monograph --all`. The markdown-first pipeline is the sole source path; each volume produces both `mono/<slug>-v<sem>.pdf` and `mono/<slug>-v<sem>.md` as canonical artifacts. The PDF compiles and matches the assembled markdown structure.

**Vocabulary worth holding (Joseph 2026-05-12):** "narrow-area" = anywhere the Tufte-style wide right margin is in play (body column + free margin column to the right). "Wide-area" = anywhere the text already spans the full segment band (Discussion / Findings sections via the `segmentwidesection` wrapper; the segmentrulewidth = textwidth + sep + marginparwidth). Tables, working-notes boxes, and segment-header rules all interact with this distinction; keep the vocabulary when reasoning about width-related rendering choices.

**Pipeline shape:**

```
source-outline + source-segments
  │
  │ Stage 1 (Mono::Ingest)
  ▼
mono/.build/<slug>/{index.md, chunks/*.md}
  │
  │ Stage 2 (Mono::Assemble)
  ▼
mono/<slug>-v<sem>.md   ← canonical citable artifact
  │
  │ Stage 3 (Mono::Typeset → AsfVolumeLatex)
  ▼
body.tex → LuaLaTeX → mono/<slug>-v<sem>.pdf
```

The design doc at [`msc/markdown-first-pipeline.md`](msc/markdown-first-pipeline.md) covers the chunk-format contract, the index-file format, and the architectural commitments.

**Suggested next moves in order of impact:**

1. **Phase 2 doc sweep.** FORMAT.md and CLAUDE.md still reference the pre-restructure structure in places. Update vocabulary: Volume / Part / Chapter / Section (= Segment); the chunk format; the markdown-first pipeline; the narrow-area / wide-area distinction. Most useful for de-novo audits and future-agent onboarding.
2. **Discussion-segment schema split** in FORMAT.md (logged above). Pairs naturally with Phase 2 since both touch FORMAT.md.
3. **Phase 1d xr-hyper cross-volume refs.** The `.aux` files are persisted per volume; the cross-volume refs from segments to sibling-volume slugs would resolve cleanly with `xr-hyper` wired into the preamble.
4. **Phase 1e incremental rebuild.** Per-chunk hashes are already in the index; ingest just needs to read the prior index and skip regeneration when source-hash matches.
5. **Phase 3 chapter introduction across Parts II/III/IV.** AAD Part I is fully chapterized; same convention for the rest of AAD and the other components. The walker's implicit-Chapter default handles unchapterized parts gracefully meanwhile.

**Files worth knowing about (current layout):**

- `bin/build-monograph` — three-stage pipeline orchestrator
- `bin/output-version <slug> show|bump <patch|minor|major>` — per-volume semver utility (operates on `mono-meta.yaml`)
- `common/main.tex` — LaTeX entrypoint template (single `\input{body}` since Stage 3 emits the whole pipeline-result into body.tex)
- `common/preamble/*.tex` — preamble fragments (`setup`, `environments`, `status-badges`, `eq-tags`)
- `common/lib/outline_walker.rb` — role-prefix-aware OUTLINE parser; HTML-comment stripping at file-read
- `common/lib/ingest.rb` — Stage 1; chunk and index emission with hash recording
- `common/lib/assemble.rb` — Stage 2; chunk stitching with cross-ref resolution
- `common/lib/typeset.rb` — Stage 3; `Kramdown::Converter::AsfVolumeLatex`
- `common/lib/segment_renderer.rb` — `Kramdown::Converter::AsfLatex` (base class with shared converter logic; AsfVolumeLatex inherits)
- `<component>/mono-meta.yaml` — per-volume metadata (title, slug, version, cover, toc)
- `<component>/<slug>.aux` — persisted aux for Phase 1d xr-refs (committed)
- `mono/.build/<slug>/{index.md, chunks/*.md}` — Stage 1 output (gitignored)
- `msc/markdown-first-pipeline.md` — design doc; load-bearing reference for the chunked-intermediate architecture

**In-source TODOs to know about** (for the next agent who touches table rendering):

- `common/lib/segment_renderer.rb`:
  - `convert_table` block: narrow-direction adaptation + snap-to-content-width epsilon (logged TODOs in the file)
  - Math source-length over-estimation: `cell_visual_length` does a reasonable job stripping LaTeX commands, but the heuristic could be refined further with sublinear (sqrt) weighting on the column-share computation if math/prose imbalance returns
- `common/lib/ingest.rb`:
  - Incremental rebuild via per-chunk hash comparison (architecture in place, implementation pending)
  - Math-pipe substitution timing (chunks carry `\vert`/`\Vert` instead of `|`; revisit if downstream non-LaTeX renderers want raw pipes)
- `common/lib/typeset.rb`:
  - AsfVolumeLatex / AsfLatex inheritance coupling — a `KramdownHelpers` mixin would be a flatter design
  - Chunk-format contract expressed in two places (emission in ingest.rb, parsing in typeset.rb's `preprocess_metadata_blocks`); extract to `Mono::ChunkFormat` when changes become coupled
- `common/lib/assemble.rb`:
  - `**Status**: missing` conflates epistemic-status with existence-status; split when a second existence-state appears

## Status

Created 2026-05-11 (v1: single-monograph plan); rewritten 2026-05-12 (v2: four-volume plan); markdown-first restructure landed end-of-day 2026-05-12 (Stages 1+2+3 across commits `be33269`, `62b2e1e`, `610b549`, `c448a00`, `e84cd80`); table-rendering cycles completed 2026-05-12 (commits `ba74d61`, `9208651`, `9159969`, `ebaf24d`); Discussion-as-chapter-intro feature landed `8da83cd`. The four-volume build is functional, the markdown-first pipeline is the sole source path, and all tables render cleanly per Joseph's review.
