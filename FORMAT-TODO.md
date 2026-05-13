# FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes

*Active plan for the conventions-and-infrastructure layer that sits on top of the four-volume markdown-first build pipeline. Parent navigator: PRACTICA. The foundation (volume split, native kaobook hierarchy, markdown-first pipeline, persisted .aux per volume) landed end-of-day 2026-05-12 — see [CHANGELOG](CHANGELOG.md) entry "Monograph build pipeline: from zero to four-volume kaobook output." This file was refocused 2026-05-13 around the next-cycle cross-cutting work: bibliography + citation system, cross-reference / footnote / sidenote / margin-note conventions, and the imported-vs-AAD-native structural distinction.*

## Status

The four-volume build is functional and shipping. All four volumes (`aad`, `tst`, `loga`, `eli`) build cleanly via `bin/build-monograph --all`; markdown-first pipeline produces both `mono/<slug>-v<sem>.pdf` and `mono/<slug>-v<sem>.md` as parallel canonical artifacts; persisted `<component>/<slug>.aux` files are committed for cross-volume xr-refs.

The active work below decomposes into three workstreams:

- **Workstream A — Citation system.** Bibliography database, `bin/refs` machinery, `\cite{key}` source form, citation-status field for blind-review handling, anonymization scanner. ASF currently has no structured bibliography — segments carry full author-year-title prose with no `\cite{}` machinery — so this is the largest single workstream.
- **Workstream B — Cross-references, footnotes, sidenotes, margin-notes.** Obsidian `[[#^anchor]]` form, equation-anchor labels, footnote conventions (zero usage anywhere currently), sidenote (numbered Tufte-style) and margin-note (un-numbered) disciplines, `xr-hyper` for cross-volume refs.
- **Workstream C — Discipline + structural distinctions.** AAD-specific vs imported (Pearl, etc.) cue, Discussion-segment schema split, auto-cross-ref formula sweep in appendices, FORMAT.md doc sweep, chapter introduction across remaining Parts, FORMAT-compliance linter sweep.

Several architectural decisions are awaiting resolution; those are listed before the workstreams so the answers can flow into the right items as they land.

---

## Foundational facts (settled; reference for future work)

These were decided over the 2026-05-11 / 12 conversation and landed in the build pipeline. Re-decision is not on the table; the items below build on them.

### The hierarchy

| Level | Kaobook env | What it is | Examples |
|---|---|---|---|
| **Volume** (= Book) | `\documentclass{kaobook}` | One of the four theories, shipped as its own PDF | AAD, TST, LogA, ELI |
| **Part** | `\part` | A scope-boundary within a Volume; 1–5 per volume | "Adaptive Systems Under Uncertainty"; "Appendices: Details" |
| **Chapter** | `\chapter` | A grouping of segments within a Part; ~15 segments each (range ~5–25) | "Foundations"; "Mismatch & Gain"; "Persistence & Structural Adaptation" |
| **Section** (= Segment) | `\section` | A numbered claim unit; the 19 FORMAT types | Definition, Result, Derivation, Hypothesis, … |
| **Subsection** (= Field) | `\subsection` | A structural section *inside* a Segment | Formal Expression, Epistemic Status, Discussion, Findings, Working Notes |
| **Subsubsection** | `\subsubsection` | A named area *inside* a Subsection | "Search Log" inside Findings, "Linear case" inside Formal Expression |

Atoms (equations, tables, figures, named formulas) sit *within* Subsections and are numbered by kaobook's native counters.

**Appendices:** each appendix segment renders directly as a `\chapter` under an `\appendix\part{...}` group. There is no intermediate Chapter level inside Appendices — an appendix segment IS a chapter-level entity. Multiple `## *Appendices* <name>` groups per volume allowed (AAD has two: "Details" and "Operational Domains").

### The numbering scheme

Kaobook native, no custom counters:

- **Part:** Roman (I–N) per volume, kaobook default.
- **Chapter:** arabic, reset per Part.
- **Section** (= Segment): arabic, reset per Chapter; cross-ref display via cleveref → `Section 1.2.3` or just `1.2.3` depending on context.
- **Subsection / Subsubsection:** native, generally not cross-referenced.
- **Atoms:** equation/table/figure counters; reset per Section so atom IDs stay stable under segment-internal reordering.
- **Named-atom evergreen cross-refs:** `*[Type (name, from ...)]*` → `\label{atom:<name>}` so `#<name>` resolves directly, independent of positional numbering. *Author-side parsing in place; LaTeX-side `\label{atom:...}` emission queued — see Workstream B item 7.*

**Cross-reference evergreen-ness principle:** cross-refs always target intrinsic identity (slug for segments, name for atoms), never positional numbers. The renderer produces the rendered number at compile time; the source never hardcodes one.

### Per-volume metadata: `mono-meta.yaml`

```yaml
title:       "AAD: Adaptation and Actuation Dynamics"
short_title: AAD
slug:        aad
major:       0
minor:       1
patch:       0
outline:     OUTLINE.md
cover_svg:   AAD-cover.svg
toc:         true
```

Version components are explicit (`major` / `minor` / `patch` as separate keys, not a single `version: 0.1.0` string) so `bin/output-version` can read/write them cleanly. Each Volume has its own semver, independent of siblings — AAD can be v1.0 (stable, citable) while LogA is at v0.3 (still evolving). The canonical version lives here; no separate `VERSION` file.

### Volume frontmatter sequence

Every Volume's frontmatter renders in this fixed order:

1. **Cover** — from `cover_svg`; rendered via `rsvg-convert` to a single-page PDF and `\includepdf`-ed as the first page. Volumes without a configured cover skip this step.
2. **Title page + Copyright** (combined on one page) — full title, author(s), license declaration, citation block (canonical citation form for sibling-volume cross-references), and build-info stamp.
3. **Table of Contents** — kaobook `\tableofcontents`, `secnumdepth = 3`, `tocdepth = 3`. Suppressible via `--no-toc` flag or `toc: false` in `mono-meta.yaml`.

Backmatter (bibliography, index, colophon) and proper title-page typographic design are deferred (see *Deferred* below).

### Build-info stamp

`build-info.tex` is emitted on every build, defining:

- `\buildsemver` — semver from `mono-meta.yaml`
- `\buildsha` — current git short-sha, with `-dirty` suffix when working tree has uncommitted changes
- `\builddate` — ISO date (YYYY-MM-DD)
- `\volumetitle` / `\volumeshorttitle` / `\volumeslug` / `\volumecoverpath` / `\ifvolumetoc`

Filename of the PDF carries semver only — `<slug>-v<semver>.pdf`. SHA + date appear in volume frontmatter.

### Vocabulary worth holding

- **Volume** = the published artifact (one PDF). **Book** = the conceptual unit. Interchangeable in casual prose; "Volume" preferred when emphasizing the publication.
- **Narrow-area** = anywhere the Tufte-style wide right margin is in play (body column + free margin column to the right). **Wide-area** = anywhere the text spans the full segment band (Discussion / Findings sections via the `segmentwidesection` wrapper). Tables, working-notes boxes, and segment-header rules all interact with this distinction.

### What the foundation does NOT change

- Slug names (canonical segment IDs)
- The substance of segment content
- Segment promotion stages (FORMAT.md §Promotion Workflow)
- The four-Volume top-level structure
- The `#slug-name` cross-ref surface convention (only what it resolves to changed)
- The kaobook visual register (tints, status badges, eq-tag marginnotes, Working Notes panels, Tufte tables, italic teal, mono olive, navy refs)

---

## Open architectural questions (awaiting decision)

Resolutions feed into the workstream items below. Listed in the order they unblock the most work.

1. **Where does the bib database live?**
   - Path A: `~/src/agentic-systems/refs/` (ASF-owned)
   - Path B: `~/src/refs/` (shared parent, both projects read; single source of truth)
   - Path C: ASF references `~/src/neurips/refs/` directly (couples ASF to NeurIPS)

   Trade-offs: Path A is simplest to start; Path B is the single-source-of-truth ideal; Path C couples ASF to NeurIPS. Lean B; A is the safe fallback.

   **Unblocks:** Workstream A items A1–A5.

2. **How to mark imported-vs-AAD-native content?**
   - Option α: `origin: imported|aad-native|recapitulation` frontmatter field + visual cue at render-time
   - Option β: Distinct segment type `recapitulation` (orthogonal to `definition` / etc.)
   - Option γ: Convention-only in Epistemic Status framing, no machinery

   Most use cases are imports-within-otherwise-AAD-segments (one segment isn't purely imported), which leans α.

   **Unblocks:** Workstream C item C12.

3. **Sidenote source-side convention.**
   - Pandoc inline-footnote: `^[content here]` (cleanest; defines content at call site)
   - Mark + definition-elsewhere: `^[1]` ... separate definition
   - Magic-comment: `<!-- sidenote: content -->`

   Lean toward pandoc inline-footnote for source-locality.

   **Unblocks:** Workstream B item B9.

4. **Cross-volume xr-refs fallback form.**
   When sibling `.aux` is missing or version-mismatched, render as:
   - "see Wecker (2026), AAD §1.2.3" (bibliography-form)
   - `[AAD #def-foo]` (placeholder, marked for human review)
   - Soft cross-reference like the in-review handling in Workstream A

   Each volume's canonical citation form needs declaring (in `mono-meta.yaml`) for whichever form is chosen.

   **Unblocks:** Workstream B item B11.

5. **Migration sweep scope.**
   ~200+ prose citations exist in ASF segments. Options:
   - Full sweep (one Joseph-author session per ambiguous-key resolution; many sessions)
   - Incremental (convert as segments are touched for other reasons; drift risk)
   - Hybrid (full sweep on high-traffic segments, incremental on the rest)

   Lean hybrid.

   **Unblocks:** Workstream A item A3 phasing.

---

## Workstream A — Citation system

Goal: ASF parity with the NeurIPS workspace's citation discipline (`~/src/neurips/refs/entries/*.yml` + `bin/refs` + `\cite{key}` source form), extended with a citation-status field for the blind-review case.

- [ ] **A1. Establish the bib database location.** Pending open question 1. Seed from the NeurIPS database + the prose citations currently in ASF segments. YAML schema: bibkey, full citation, DOI, publication date, found date (when ASF first cited), verification date (when last checked against primary source), local PDF path (if any), citation-status (`pre-publication` / `in-review` / `preprint` / `published` / `withdrawn`), citation-domain (AAD / TST / LOGA / ELI / cross).
- [ ] **A2. Stand up `bin/refs` for ASF.** Port from NeurIPS (`add` / `verify` / `lint` / `search`); extend with the citation-status field for in-review handling. Conditional rendering: when the citing volume is itself anonymized, in-review citations render as soft "Wecker, in preparation" or local-source pointer; otherwise full citation. Same machinery covers the future case where ASF papers themselves go to blind-review venues.
- [ ] **A3. Run `bin/migrate-cites` across ASF segments.** ~200+ prose citations. Phasing per open question 5. Each ambiguous match (`[Hintikka 1991]` → multiple bib entries) flags for Joseph-author resolution.
- [ ] **A4. Wire biblatex / natbib into `mono/kaobook/main.tex`.** The `% kaobiblio loaded once we wire biblatex (task 7)` comment at `mono/common/main.tex:31` is the marker. Match NeurIPS's bracketed-superscript natbib config (`super,sort&compress`) for source-form `\cite{key}` / `\citet{key}` / `\citep{key}` rendering with postnotes. Bibliography position in volume frontmatter / backmatter to be decided alongside backmatter design (deferred).
- [ ] **A5. Anonymization scanner (`refs/deny-list.yml`).** Port from NeurIPS. Relevant for the future when ASF papers themselves go to blind-review venues; also prevents accidental ASF self-citation in NeurIPS submissions.

---

## Workstream B — Cross-refs, footnotes, sidenotes, margin-notes

Goal: Adopt NeurIPS's cross-reference / footnote conventions for ASF, then extend with sidenote + general-purpose margin-note disciplines beyond the equation-tag-only current state. Wire `xr-hyper` for cross-volume references.

- [ ] **B6. Add Obsidian `[[#^anchor]]` cross-ref form.** In addition to bare `#slug`. Cleveref typed-noun rendering ("Theorem 1.1", "Section 2"). `^eq-name` for equations routes to `\eqref{}` for parenthesized numbers. Coexists with `#slug` (which stays as the segment-level cross-ref); `[[#^anchor]]` extends the system to atom-level refs.
- [ ] **B7. Land `\label{atom:<name>}` emission.** Phase 1c-tail completion from the prior plan. The author-side parsing of `*[Type (name, from ...)]*` is in place; the LaTeX-side `\label` emission isn't. Once landed, named-atom evergreen cross-refs work end-to-end and unblock C15 (auto-cross-ref formula sweep).
- [ ] **B8. Specify footnote convention in FORMAT.md.** Both `[^anchor]` markdown form and `\footnote{...}` raw-TeX form per NeurIPS AUTHORING.md §2.4. Currently zero footnote usage anywhere in ASF segments — convention establishment is the work.
- [ ] **B9. Sidenote convention (Tufte-style numbered margin note).** Pending open question 3. Source-side convention TBD; renders to `\sidenote{...}` LaTeX macro using kaobook's machinery. Distinct from the un-numbered margin-note (B10): a sidenote carries a number that ties to its in-line callout, a margin-note just appears in the margin.
- [ ] **B10. Generalize `\marginnote{...}` discipline.** Currently used only for equation-tag emission via `\eqtag{...}`. Extend to author-driven margin annotation with a source-side convention (TBD). The un-numbered "just there in the margin" form Joseph distinguished from sidenotes.
- [ ] **B11. Wire `xr-hyper` into preamble.** Phase 1d. The `.aux` files are persisted (`01-aad-core/aad.aux` etc.); `xr-hyper` reads sibling-volume `.aux` for cross-volume label resolution. Fallback form pending open question 4. `.aux` staleness detection: warn or error when a sibling `.aux` was written against a different sibling-volume semver than the one being referenced.

---

## Workstream C — Discipline + structural distinctions

Goal: The conventions that distinguish *what* segments are doing (AAD-internal vs imported, claim vs discussion, in-flight vs settled) from how they render. Plus the documentation + sweep work that catches up the corpus to the new conventions.

- [ ] **C12. AAD-specific vs imported distinction.** Pending open question 2. Lightweight visual or structural cue at frontmatter / segment-type / Epistemic-Status level. Especially for segments like `def-pearl-causal-hierarchy` where the content is explicitly external (Pearl 2009; Bareinboim et al. 2022). The Pearl-hierarchy Part I → Part II move (TODO line 362) is one specific instance; this item generalizes it.
- [ ] **C13. Citation-status field on `refs/entries/`.** (`pre-publication` / `in-review` / `preprint` / `published` / `withdrawn`). Build conditionally renders soft cross-references for `in-review` status when the citing volume is itself under blind review; otherwise renders full citation. Subsumes part of A2 — the field is declared in A1, the conditional-rendering machinery lands here.
- [ ] **C14. Discussion-segment schema split in FORMAT.md.** Already flagged. Claim-segment schema (Formal Expression / Epistemic Status / Discussion / Findings required) vs discussion-segment schema (body-only, subheads optional). The Discussion-as-chapter-intro renderer mode (commit `8da83cd`) suppresses subheads at render-time; the source still has them. FORMAT.md should split the schema so authors don't have to fake it.
- [ ] **C15. Auto-cross-ref formula sweep in appendices.** Phase 4 of the prior plan. Many manual "Prop A.1" / "(7) above" / "Step 4" / "as shown in (12)" references still exist in appendix segments. Once B7 lands (named-atom labels), this sweep replaces manual cross-refs with `[[#^name]]` form and the renderer produces the rendered number.
- [ ] **C16. FORMAT.md doc sweep.** Vocabulary alignment with the conventions landed in foundation work + added through workstreams A/B/C. The narrow-area / wide-area vocabulary, the chunk format, the markdown-first pipeline, the new citation conventions, the cross-reference convention extensions — all need representation in FORMAT.md so de-novo audits and future-agent onboarding hit the right discipline. Pairs naturally with C14 (both touch FORMAT.md). CLAUDE.md gets the parallel sweep.
- [ ] **C17. Chapter introduction across Parts II/III/IV (AAD + other components).** AAD Part I is fully chapterized; AAD Parts II/III/IV use the walker's implicit-Chapter default. Same convention for the rest of AAD and for TST / LogA / ELI's outlines. Joseph chooses chapter groupings (with build-side help on dependency-cluster analysis if useful). For Parts with only one Chapter, the source can use a placeholder H3 ("Chapter 1: All segments") until proper grouping is decided.
- [ ] **C18. FORMAT-compliance linter sweep.** Phase 5 of the prior plan. `bin/lint-md --fix` for auto-fixable categories (hard-wraps, emphasis-underscores, `_` in `\text{}`); manual / agent-driven sweep for the rest (math compatibility issues — `|` / `\|` / `<` / `>` / `*` in math; `\text` outside `$`; etc.). ~200+ findings across the corpus.

---

## Deferred / outside-scope

Items previously tracked but not blocking the three workstreams. Lifted out so the active layout reads cleanly.

- **Backmatter design** — bibliography rendering layout, index, colophon. Surfaces during Workstream A landing (the bibliography position in the ToC + page-break treatment); design discussion deferred to a later session.
- **Title-page typographic design** — current minimum (title + author + build-info stamp); proper layout for license block, citation form, etc. deferred.
- **Per-volume preface** — short reader-orienting text at the start of each Volume (between ToC and Part I); tone is conversational, framework-positioning.
- **Companion PDFs** — specialized cuts (selected chapters, theme-based) for particular audiences.
- **Smart rebuild (per-volume hash cache)** — Phase 1e from the prior plan. The index.md frontmatter records source hashes for every chunk, but ingest still re-emits all chunks on every build. Architecture in place; implementation pass pending. Lower priority than A/B/C since the build is already fast enough.
- **`\includeonly` chapter-incremental builds** — only if per-volume builds become uncomfortably slow.
- **Section letter codes normalization in OUTLINE tables** — optional tidying.
- **Slug rename audit** — separate concern, naming-cycle work; lives at PRACTICA §"Names & Lexicon" and `msc/naming/`.
- **Cover artwork for TST / LogA / ELI** — AAD's cover lives at `01-aad-core/AAD-cover.svg`; siblings need authoring.
- **Dependency-graph SVG → PDF pipeline for image rendering** — separate piece similar to cover artwork; `rsvg-convert` invocation.
- **Table-rendering polish** — narrow-direction adaptation, snap-to-content-width epsilon, source-side math reflow for inherently-wider-than-page equations. In-source TODOs at `bin/lib/segment_renderer.rb` `convert_table` block. The current rendering handles the common cases; these are residual edge-case improvements.
- **Tighter typography candidates** — status badges / stage glyphs on appendix-chapter headings (currently a small indicator strip below the chapter glyph); `\l@appendixchapter` style for tighter ToC entries; etc. Cosmetic.
- **In-source TODOs in `bin/lib/`** — `AsfLatex` / `AsfVolumeLatex` inheritance vs mixin design; chunk-format contract expressed in two places (extract to `Mono::ChunkFormat`); `**Status**: missing` conflating epistemic-status with existence-status. Pick up when those modules need touching for other reasons.

---

## Files worth knowing about (current layout)

- `bin/build-monograph` — three-stage pipeline orchestrator
- `bin/output-version <slug> show|bump <patch|minor|major>` — per-volume semver utility (operates on `mono-meta.yaml`)
- `bin/lint-md` — markdown-convention linter (~880 lines; math-compat, voice, formatting)
- `bin/lint-outline` — outline + segment dependency linter (~640 lines; deps, cross-refs, orphans)
- `mono/kaobook/main.tex` — LaTeX entrypoint template (single `\input{body}` since Stage 3 emits the whole pipeline result into `body.tex`)
- `mono/kaobook/preamble/*.tex` — preamble fragments (`setup`, `environments`, `status-badges`, `eq-tags`)
- `bin/lib/outline_walker.rb` — role-prefix-aware OUTLINE parser; HTML-comment stripping at file-read
- `bin/lib/ingest.rb` — Stage 1; chunk + index emission with hash recording
- `bin/lib/assemble.rb` — Stage 2; chunk stitching with cross-ref resolution
- `bin/lib/typeset.rb` — Stage 3; `Kramdown::Converter::AsfVolumeLatex`
- `bin/lib/segment_renderer.rb` — `Kramdown::Converter::AsfLatex` (base class)
- `<component>/mono-meta.yaml` — per-volume metadata (title, slug, version, cover, toc)
- `<component>/<slug>.aux` — persisted `.aux` for cross-volume xr-refs (committed)
- `mono/.build/<slug>/{index.md, chunks/*.md}` — Stage 1 output (gitignored)
- `mono/<slug>-v<sem>.{pdf,md}` — released artifacts
- `msc/markdown-first-pipeline.md` — design doc; load-bearing reference for the chunk-format contract

NeurIPS workspace cross-references (the conventions Workstream A and parts of B port from):

- `~/src/neurips/AUTHORING.md` — the per-paper-agent rules; covers citations / cross-refs / footnotes / theorem callouts / anonymization in detail
- `~/src/neurips/refs/entries/*.yml` — canonical bib database (hundreds of entries)
- `~/src/neurips/refs/deny-list.yml` — anonymization vocabulary
- `~/src/neurips/bin/refs` — bib management CLI
- `~/src/neurips/bin/migrate-cites` — `[Author Year]` → `\cite{key}` sweeper
- `~/src/neurips/common/neurips_2026.sty` — sty file (canonical; do not modify)

---

*Created 2026-05-11 (v1: single-monograph plan); rewritten 2026-05-12 (v2: four-volume plan); foundation work landed end-of-day 2026-05-12; this file refocused 2026-05-13 around the cross-cutting conventions (citations / cross-refs / footnotes / sidenotes / margin-notes / discipline). Foundation history is captured in [CHANGELOG](CHANGELOG.md) entry "Monograph build pipeline: from zero to four-volume kaobook output" (2026-05-11 / 2026-05-12).*
