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
- ⬜ **Markdown-first restructure (priority)** — the pipeline should pass through a consolidated per-volume markdown intermediate. Today the walker emits structural events that `build-monograph` translates directly into LaTeX, and the consolidated markdown is produced by a separate (now-retired) Python `bin/build` script. Both paths duplicate the OUTLINE-walk / segment-inlining logic, and the markdown artifact (a critical build-pipeline deliverable, called out as such by Joseph) has been treated as an afterthought. The right architecture is single-source: walker emits consolidated markdown; kramdown (`AsfLatex` converter, extended) processes the same markdown to emit LaTeX; the `.md` artifact is a natural byproduct of one pass. Concretely: (a) new `common/lib/markdown_emitter.rb` walks OUTLINE.md and inlines segments (frontmatter, working-notes stripping, header-bumping, anchor insertion, cross-ref rewriting with per-section academic numbering); (b) `Kramdown::Converter::AsfLatex` extended to recognize the role-prefix italic convention on H2/H3 headers and an analogous segment-opener marker on inlined segment headings, emitting `\part` / `\chapter` / `\addchap` / `\segmenthead` / `\segmentappendixchapter` accordingly; (c) `bin/build-monograph` rewired to emit-then-process; (d) legacy `bin/build` moved to `_obs/`.
- ⬜ Phase 1d — xr-hyper cross-volume refs, sibling-volume citations
- ⬜ Phase 1e — smart-rebuild hash cache
- ⬜ Phase 2 — FORMAT.md / CLAUDE.md doc sweep (vocabulary alignment)
- ⬜ Phase 3 — chapter introduction across Parts II/III/IV of AAD + other components
- ⬜ Phase 4 — cross-ref hygiene sweep
- ⬜ Phase 5 — FORMAT-compliance linter sweep
- ⬜ Phase 6 — table dynamic-shrinking, backmatter design, title-page typography, per-volume preface

**Tighter typography candidates surfaced during the 1c/1a cycle:**
- Status badges + stage glyphs on appendix-chapter headings are emitted by `\segmentappendixchapter` but currently render in a plain indicator strip below kaobook's chapter glyph — could be promoted into the chapter heading itself once a tighter visual register is decided.
- Appendix-chapter ToC entries now use the `\chapter[short]{rich}` two-arg form so the ToC stays compact (clean title only, no italic type prefix). If further compression is wanted, the next step is a custom `\l@appendixchapter` style.

## Handoff Notes (for the next session)

**Where to pick up:** the four-volume build is working. `bin/build-monograph aad` (or `01`/`tst`/`02`/etc.) builds one volume; `bin/build-monograph --all` builds all four. Outputs land in `mono/<slug>-v<M>.<m>.<p>.pdf` with persisted `.aux` in each `<component>/<slug>.aux`.

**Suggested next phases in order:**

1. **Phase 1a — Per-volume ToC.** Quick win; just adds `\tableofcontents` in `common/main.tex` after frontmatter. Decide depth (probably 3 — through Section). Adds a `toc: false` opt-out signal to `mono-meta.yaml`.
2. **Phase 1d — xr-hyper cross-volume refs.** The `.aux` files are now persisted per volume; wire `xr-hyper` in `common/preamble/` so each volume's preamble registers its three siblings. Fallback citation form when sibling `.aux` is stale or missing.
3. **Phase 1e — Smart rebuild.** Per-volume input-hash cache so `bin/build-monograph aad` skips when nothing AAD-relevant changed. Implementation candidate: hash over `<component>/src/**` + `<component>/OUTLINE.md` + `<component>/mono-meta.yaml` + `common/**` + sibling-`.aux` digests, cached at `mono/.build/<slug>/.input-hash`.
4. **Phase 3 — Chapter introduction in OUTLINEs.** Parts II/III/IV of AAD already chapterized in source by Joseph (or in progress); same convention for TST / LogA / ELI components. The walker's implicit-Chapter default handles unchapterized parts gracefully meanwhile.

**Known unfinished business:**

- Title page is minimal — needs proper layout per the frontmatter sequence spec (Cover → Title+Copyright → ToC). The macros `\volumetitle` / `\buildsha` etc. are available; just no layout uses them yet.
- Cover artwork for TST / LogA / ELI not authored.
- Old AAD-specific tints in segment headers are mapped per-type and working; if FORMAT.md changes the 19-type list, the tint mapping (`common/preamble/environments.tex` `\setheadertint`) needs to stay in sync.
- Table dynamic-shrinking: tables that overflow currently stay overflowing rather than auto-shrinking. Captured as a deferred Phase 6 item.

**Files to know about:**

- `common/main.tex` — LaTeX entrypoint template (per-volume)
- `common/preamble/*.tex` — preamble fragments (setup / environments / status-badges / eq-tags)
- `common/lib/segment_renderer.rb` — kramdown subclass for segment markdown → LaTeX
- `common/lib/outline_walker.rb` — role-prefix-aware OUTLINE parser
- `bin/build-monograph` — main build script
- `bin/output-version` — per-volume semver utility (operates on `mono-meta.yaml`)
- `FORMAT-TODO.md` — this file; the live plan
- `<component>/mono-meta.yaml` — per-volume metadata (title, slug, version, cover)
- `<component>/<slug>.aux` — persisted aux for Phase 1d xr-refs (committed)

## Status

Created 2026-05-11 (v1: single-monograph plan); rewritten 2026-05-12 (v2: four-volume plan); progress-snapshot added 2026-05-12 mid-cycle. Phase 1c landed; Phase 1b (volume split) is the immediate next substantive step.
