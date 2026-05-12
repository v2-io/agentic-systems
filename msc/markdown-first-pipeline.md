# Markdown-First Build Pipeline — Design

*Design document for the build-pipeline restructure proposed during the 2026-05-12 monograph-build session. Status: design, not yet implemented. Once the implementation lands and reviews well, the load-bearing pieces migrate to FORMAT.md (the chunk contract) and the rest can sunset.*

## Why this exists

The current `bin/build-monograph` walks `OUTLINE.md` via `outline_walker.rb`, emits structural LaTeX directly (`\part`, `\chapter`, `\addchap`, …), and inlines each segment through `segment_renderer.rb` (which runs kramdown over the segment file). A separate Python `bin/build` walks the same `OUTLINE.md` independently and produces a consolidated markdown artifact.

Two paths, two implementations, two places where outline-walking and segment-inlining live. They drift. The Python script is unmaintained, and the consolidated markdown — which is a critical build artifact (it's what makes a volume citable as a single document, ingestible by humans and LLMs without a typesetting toolchain) — has been treated as an afterthought.

The restructure replaces both paths with a single canonical pipeline:

```
source-outline + source-segments
       │
       │  (1) ingest: outline-walk + per-segment normalization
       ▼
index.md  +  chunks/<name>.md  ─── per-volume build directory
       │
       │  (2) assemble: stitch chunks in index order, resolve cross-refs
       ▼
mono/<slug>-v<sem>.md  ─── canonical assembled volume markdown (citable artifact)
       │
       │  (3) typeset: kramdown converter → LaTeX → LuaLaTeX
       ▼
mono/<slug>-v<sem>.pdf
```

Single source of truth. The assembled markdown is *the* artifact; the PDF is one rendering of it. Future renderings (HTML, EPUB, JSON-for-LLM) plug in at the assembled-markdown layer without touching the ingest or assemble stages.

## Architectural commitments

These are the load-bearing decisions. Code follows from them; if any of these changes, the implementation reshapes.

1. **The author-facing source is `OUTLINE.md` + `src/<slug>.md` files, unchanged.** No new authoring conventions land in this restructure. The role-prefix italic convention (`## *Part*`, `### *Chapter*`, `## *Preface*`, `## *Appendices*`) and segment YAML frontmatter stay exactly as today.

2. **Chunks are addressable units of normalized print-ready markdown.** One chunk per segment, plus chunks for non-segment structural content (volume preface, part preface, chapter-rationale prose that the author chooses to leave un-HTML-commented). Chunks live in `mono/.build/<slug>/chunks/` and are keyed by stable names (slugs for segments, synthetic-but-stable names for structural pieces). They are pure markdown — readable on their own, with their metadata block at the top.

3. **The index is the assembly manifest.** `mono/.build/<slug>/index.md` is a markdown file with YAML frontmatter carrying volume metadata (sourced from `<component>/mono-meta.yaml` plus build-time fields: `generated_at`, `build_sha`, source-hash for invalidation). The body of the index is the ordered list of chunks with their slugs, labels, kinds, and source-of-truth hashes. The index is regenerated whenever the source structure changes; chunks are regenerated only when their individual sources change.

4. **The chunk format contract is documented and enforceable.** Each chunk has a metadata block immediately after the H1 (a sequence of `**Key**: value` lines), then a body. The downstream LaTeX renderer parses the metadata block by convention. The chunk format is the boundary between ingest and render; it must be stable.

5. **Cross-references are resolved at assembly time, not in chunks.** A segment chunk carries unresolved `#slug-name` markers; the assembler substitutes the resolved label (e.g., `[Definition 1.4](#def-agent-environment)`) when stitching. Chunks stay reusable across reorderings; numbering changes don't invalidate chunks.

6. **Header bumping happens at chunk-creation time.** A segment's authored `# Definition: Title` (H1) lands at H4 in a main-matter context (under Volume H1 / Part H2 / Chapter H3) and at H3 in an appendix context (where the appendix segment IS the chapter). Container-aware bumping happens during chunk ingest; the chunk file carries the bumped headers. This means a segment's position in the volume affects its chunk; moving a segment from main-matter to appendix regenerates its chunk.

7. **Incremental builds are intrinsic, not bolted on.** Each chunk's index entry carries a hash of its source-of-truth (segment file content + structural context). Ingest compares current hash to the index's recorded hash; only changed chunks regenerate. Same discipline at the index level for OUTLINE.md changes. Phase 1e (smart rebuild) is subsumed.

8. **The kramdown converter recognizes structural markers in the assembled markdown.** Role-prefix italic on H2/H3 (`## *Part* Title`, `### *Chapter* Title`, etc.) and the chunk metadata block on H4/H3 segment headers tell the converter which LaTeX command to emit. The converter's structural intelligence moves out of `build-monograph` (where it currently lives as `case item[:kind]` branches) and into the kramdown layer.

## Build directory layout

```
mono/.build/<slug>/
├── index.md                           Assembly manifest
├── chunks/
│   ├── volume-preface.md              Synthetic name (no slug in source)
│   ├── part-i-preface.md
│   ├── chapter-i-1-rationale.md       Optional, only when author leaves
│   │                                    chapter prose un-HTML-commented
│   ├── def-agent-environment.md       Segment chunks named by slug
│   ├── def-action-transition.md
│   ├── …
│   ├── deriv-sector-condition.md      Appendix segment chunks
│   └── worked-example-cam.md          Missing-segment placeholder chunks
│                                        included; LaTeX renders the
│                                        "not yet written" marker
├── frontmatter.tex                    Generated from chunks during typeset
├── body.tex                                ditto
├── build-info.tex                     Existing per-build macros
└── <slug>-v<sem>.{tex,aux,log,pdf}    LuaLaTeX outputs
```

`mono/<slug>-v<sem>.md` and `mono/<slug>-v<sem>.pdf` live in the parent `mono/` directory as released artifacts (the build directory is staging).

## The chunk format

Each chunk is a standalone markdown file. The H1 is the chunk title; an immediately-following metadata block carries the contract; the body is the print-ready content.

```markdown
# Definition: Agent-Environment Coupling

**Slug**: `def-agent-environment`
**Type**: Definition
**Status**: exact
**Stage**: deps-verified
**Label**: 1.1
**Container**: section

A pair $(A, E)$ of stochastic systems coupled through observation and
action channels …

## Formal Expression

*[Definition]* The agent-environment system is a tuple …

## Epistemic Status

…

## Discussion

…

## Working Notes

*(stripped in :public variant before LaTeX renders, kept in :review)*

```

### Metadata block grammar

- **The block sits immediately after the chunk's H1, separated from the H1 by a blank line.**
- **Each metadata line has the form `**Key**: value` and starts at column 0.**
- **The block ends at the first blank line after the metadata.**
- **Keys are case-sensitive; values are interpreted by key.**

Defined keys (extensible):

| Key | Value type | Required? | Meaning |
|---|---|---|---|
| `Slug` | inline-code'd slug | yes for segments | The segment's stable identity; also the anchor target |
| `Type` | label string (e.g., `Definition`, `Result`) | yes for segments | The segment type per FORMAT's 19-type vocabulary |
| `Status` | one of FORMAT's status values | optional | Epistemic status (exact / robust qualitative / heuristic / conditional) |
| `Stage` | one of FORMAT's stage values | optional | Promotion stage (draft / deps-verified / claims-verified / format-clean / candidate) |
| `Label` | rendered number, e.g., `1.1`, `A`, `AF` | assigned at assembly | Computed from outline order; LaTeX uses for cross-ref formatting |
| `Container` | `section`, `chapter`, `preface`, `appendix-chapter` | yes | Tells the LaTeX renderer which structural command to emit for this chunk's heading |

Non-segment chunks (volume preface, part preface, chapter-rationale) carry only the keys that apply — typically just `Container` and possibly `Label` or a title key.

### Body contract

- Cross-references appear as unresolved `#slug-name` markers in the body. The assembler resolves them when stitching the volume's assembled markdown.
- Equation-tag paragraphs `*[Derived]*`, `*[Hypothesis]*`, etc. appear verbatim; the LaTeX converter recognizes them as margin-tag emissions.
- Obsidian-style callouts (`> [!warning]`) appear verbatim.
- Math (`$...$`, `$$...$$`) appears verbatim; the LaTeX converter passes it through.
- Markdown links (`[label](path-or-anchor)`) appear with paths already rewritten to internal anchor links where possible (file-path-to-segment-slug rewriting happens at chunk-ingest time, since it's a local segment concern).

## The index file

`mono/.build/<slug>/index.md` is a markdown file with rich YAML frontmatter and a structured body listing chunks in assembly order.

```markdown
---
# Sourced from <component>/mono-meta.yaml
title:        "AAD: Adaptation and Actuation Dynamics"
short_title:  AAD
slug:         aad
major:        0
minor:        1
patch:        0
cover_svg:    AAD-cover.svg

# Computed at build time
generated_at: 2026-05-12T15:00:00Z
build_sha:    3c14779
outline_hash: 7f3a91c          # sha256(OUTLINE.md), 8 chars
toc_enabled:  true             # honors mono-meta.yaml `toc:` + --no-toc

# Per-section running counters for label assignment
# (sections are the first column of OUTLINE.md segment tables: I, II, III, A, B, etc.)
numbering:
  I:  { count: 18 }
  II: { count: 28 }
  III: { count: 21 }
  A:  { count: 33 }
  B:  { count: 6 }
---

# AAD Build Index

Generated assembly manifest. Build script regenerates only chunks whose
source-hash differs from the recorded value below.

## Frontmatter

- `volume-preface.md` — *kind: preface*, *source: 01-aad-core/OUTLINE.md §preface*, *hash: a3f29c1d*

## Part I — Adaptive Systems Under Uncertainty

- *kind: part*, *title: "Adaptive Systems Under Uncertainty"*
- `part-i-preface.md` — *kind: part-preface*, *source: OUTLINE.md §part-i*, *hash: 1e8b2a4f*

### Chapter 1 — The Coupled Loop: Ontology and Scope

- *kind: chapter*, *title: "The Coupled Loop: Ontology and Scope"*
- `def-agent-environment.md` — *slug: def-agent-environment*, *type: Definition*, *label: 1.1*, *source: src/def-agent-environment.md*, *hash: 91b7c3e2*
- `def-action-transition.md` — *slug: def-action-transition*, *type: Definition*, *label: 1.2*, *source: src/def-action-transition.md*, *hash: 4c2a8d6f*
- …

### Chapter 2 — The Reality Model

- *kind: chapter*, *title: "The Reality Model"*
- *kind: missing*, *slug: the-reality-model-intro*, *type: Discussion*, *label: 2.1*
- `form-reality-model.md` — *slug: form-reality-model*, *type: Formulation*, *label: 2.2*, …

…

## Part IV — Appendices: Details

- *kind: appendices*, *title: "Appendices: Details"*
- `deriv-sector-condition.md` — *slug: deriv-sector-condition*, *type: Derivation*, *label: A*, *container: appendix-chapter*, …

…
```

The index body is markdown for human readability — anyone can open the index and see what the volume looks like as a structure. Each chunk line is a self-describing inline metadata strip. A parseable format (could be pure YAML in the body) is plausible, but markdown-with-italic-attrs scans more easily; if mechanical re-parsing becomes painful, we revisit.

## The three pipeline stages

### Stage 1: ingest — source → chunks + index

`Mono::Ingest` (new module) walks `OUTLINE.md` via the existing `outline_walker.rb`. For each structural item, it:

- **Part / Appendices / Chapter heading**: emits a structural entry into the index (no chunk file; the structural marker is just a line in `index.md`'s body).

- **Preface (H2)**: collects following prose into the `volume-preface` buffer; on next H2 (Part / Appendices), flushes the buffer into `chunks/volume-preface.md` with metadata `Container: preface`, computes hash, records in index. If the preface buffer is empty (no content), no chunk is emitted and the index entry is omitted.

- **Preface (H3)**: same pattern, into `chunks/part-<N>-preface.md` (or `chunks/part-<roman>-preface.md` — naming TBD; see open questions).

- **Segment row in a table**: reads the segment file, strips YAML frontmatter, strips Working Notes if `--public`, bumps headers (segment H1 → H4 main-matter, H3 appendix; H2 subheadings → H5 / H4 respectively), applies the file-path-to-slug rewrite on local markdown links, writes `chunks/<slug>.md` with the metadata block at the top, computes hash, records in index. If the segment file's hash matches what's already recorded in the previous index, ingest skips the rewrite.

- **Missing segment row**: emits a `kind: missing` entry in the index with the slug + type + claim text. No chunk file; the renderer handles missing inline. (Or: a missing-segment chunk is emitted with a stub body — leaning toward this for symmetry.)

- **Gap row** (`--GAP--`): emits a `kind: gap` entry with the description.

- **Prose between Part-heading and first Chapter** that isn't inside an explicit `*Preface*`: implicit preface — collected the same way as an explicit preface.

- **Prose between Chapter-heading and first segment row** (rare; most authors HTML-comment chapter-rationale notes): collected into `chunks/<chapter-id>-rationale.md` with metadata `Container: chapter-prose`. The renderer emits it as a paragraph between `\chapter{...}` and the first segment.

- **Images**: skipped (SVG→PDF pipeline pending; deferred to its own slice).

Stage 1 outputs are deterministic — given the same sources, regenerates identical chunks and index. The `outline_hash` lets future ingest invocations detect that nothing has changed and skip the whole stage.

### Stage 2: assemble — chunks + index → assembled markdown

`Mono::Assemble` (new module) reads `index.md`, walks its body in order, and stitches the volume's assembled markdown:

- For structural entries (`kind: part`, `kind: chapter`, `kind: appendices`), emits the role-prefix italic header (`## *Part* Title`, `### *Chapter* Title`, etc.) — same convention as source, just at the bumped levels appropriate for the volume context.

- For chunk entries, reads the chunk file, substitutes resolved cross-refs (`#def-foo` → `[Definition 1.4](#def-foo)` using the index's label map), and appends.

- For `missing` entries, emits the placeholder block (`### *Type* Title (missing)\n\n*Segment `slug` not yet written.*\n`).

- For `gap` entries, emits the gap marker (`> **[Gap]** Description`).

Output: `mono/<slug>-v<sem>.md` — the canonical assembled volume markdown, ready for reading or further rendering. Self-contained: anchors work, cross-refs resolve, math and callouts are preserved.

This file is the citable artifact. It's what a journal reviewer reads when they don't want to download a PDF. It's what an LLM ingests to reason about the framework. It's what a downstream HTML build consumes.

### Stage 3: typeset — assembled markdown → LaTeX → PDF

`Mono::Typeset` (refactored `build-monograph` content) feeds the assembled markdown through kramdown using the extended `AsfLatex` converter. The converter recognizes:

- **Role-prefix italic on H2**: `## *Part* X` → `\part{X}`; `## *Preface* X` → `\addchap{X}` (volume preface, in `\frontmatter` scope); `## *Appendices* X` → emits `\appendix` + `\renewcommand{\thechapter}{\AlphAlph…}` + `\asfAppendixToCremap` on first occurrence, then `\part{Appendices: X}`.

- **Role-prefix italic on H3**: `### *Chapter* X` → `\chapter{X}`; `### *Preface*` → (no LaTeX; the subsequent prose just flows under the most recent `\part`).

- **Chunk metadata block** (the `**Key**: value` strip after an H1 or H4 in assembled context): parsed in the converter; on the next header, the converter emits `\segmenthead{Type}{Title}{Status}{Stage}\label{seg:<slug>}` (or `\segmentappendixchapter{…}` for `Container: appendix-chapter`).

- **Cross-refs already resolved**: `[Definition 1.4](#def-foo)` renders as a `\cref`-compatible link.

- **Eq-tags, callouts, math, lists**: same handling as today's converter; that logic is preserved verbatim.

The converter emits two files: `frontmatter.tex` (the volume-preface chunk and only that) and `body.tex` (everything from the first Part onward, including images, segments, and appendix). `main.tex` `\input`s both in the appropriate matter scopes.

Stage 3's input is the assembled markdown, but the typesetter could equally well consume the chunks directly (stitching at the LaTeX-output level rather than the markdown-input level) if that turns out to be more efficient. The chunk-format contract is well-defined enough either way.

## Incremental build mechanics

Stage 1 checks invalidation:

- `outline_hash`: if the recorded hash in the previous `index.md` matches the current `OUTLINE.md` hash, structure is unchanged. Chunks whose source-segment file is also unchanged (per chunk-level hash) are kept; their chunk files are not rewritten.
- For each segment row in the outline: compute the segment file's hash + the chunk's container context. If the index's recorded hash matches, the chunk file is reused. Otherwise, regenerate the chunk and update the index.
- Numbering changes (because a segment was inserted upstream) bump labels in the index but don't invalidate the chunk bodies; the assembler does cross-ref substitution from the current index regardless.

Stage 2 always re-runs (it's fast — stitching markdown is microseconds per chunk). It produces the assembled markdown deterministically.

Stage 3 invalidation: the LaTeX compile re-runs if the assembled markdown changed, OR if any preamble file (`common/preamble/*.tex`) changed, OR if the version was bumped. Detected via a top-level build hash.

A `--force` flag bypasses all incremental checks (for cases where the cache is wrong).

## Migration path

The shift happens in three commits, each independently buildable:

1. **Stage 1 (ingest)**: introduce `Mono::Ingest`, produce `index.md` + chunks; keep the LaTeX path unchanged (still walks OUTLINE directly). Side-by-side, the new and old behaviors coexist. Verify chunks look right.

2. **Stage 2 (assemble)**: introduce `Mono::Assemble`, produce the assembled markdown from chunks + index. Verify the markdown is correct, readable, and equivalent to what the retired Python `bin/build` produced.

3. **Stage 3 (typeset)**: rewire `bin/build-monograph` to typeset from the assembled markdown via the extended `AsfLatex` converter. Move the legacy `bin/build` to `_obs/`. Verify all four volumes' PDFs come out identical (or improved) to the current output.

At each step, the build still produces working PDFs. If a stage misfires, we roll back just that stage. Smaller commits, lower risk.

## Open questions

These are the calls that aren't obvious to me — flagging for Joseph's input before I lock them in:

1. **Index file format: markdown-with-prose-style-entries vs pure YAML?** I drafted markdown-with-italic-attrs because Joseph said "markdown index file." If parsing this turns out painful (regex-y), pure YAML in the body is the fallback. Prefer markdown unless we hit friction.

2. **Chunk filenames for non-segment structural pieces.** Segment chunks are slug-named (`def-agent-environment.md`). Volume preface is `volume-preface.md`. Part preface — `part-i-preface.md` (roman) or `part-1-preface.md` (arabic) or `part-{slug-of-part-title}-preface.md` (slugified)? Roman feels right since Parts are Roman-numbered, but it ties chunk names to display numbering. Arabic is more stable. **Leaning arabic** for stability; index records the rendered roman in the label.

3. **Missing segments: chunk or index-only?** Two options: emit a stub chunk file (symmetric with real segments, the assembler treats them uniformly) vs. record `kind: missing` in the index and let the renderer handle the placeholder inline (no chunk file). **Leaning stub-chunk** for symmetry — the assembler then has one code path.

4. **Header-bumping vs role-prefix on segment headers in chunks.** Two ways to mark a segment header for the renderer to recognize. Option A: bump levels (segment H1 → H4 main-matter, H3 appendix). The renderer detects it's a segment by the metadata block following the header. Option B: keep segment H1 as H1 in the chunk; add a role prefix (`# *Definition* Title`). The renderer detects by role prefix. **Leaning A** because the assembled markdown then has a consistent hierarchy — H1 = volume, H2 = part, H3 = chapter or appendix-chapter, H4 = main-matter segment. A reader sees the whole volume as one well-formed document.

5. **Where does `**Label**` come from for appendix segments?** Appendix segments are chapters; their label is `A`, `B`, ..., `Z`, `AA`, `AB`, ... (computed by `\AlphAlph`). The ingest stage doesn't currently compute that — the LaTeX `\appendix` + `\thechapter` machinery does at compile time. For the assembled markdown to carry resolved labels, ingest needs to mirror the LaTeX numbering (run a parallel counter, assign `A` / `B` / ... to appendix chunks). Doable; just a place where ingest needs to know about the appendix-letter convention.

6. **Cross-ref resolution for "see Definition #def-foo" prose.** The assembler resolves `#def-foo` → `[Definition 1.4](#def-foo)` using the index's label map. For the LaTeX converter, that's already-resolved; the converter just emits the link. For a markdown reader, the link is clickable. But — does the converter need the slug+anchor for `\cref` purposes, or does the markdown link provide enough? Probably the converter recognizes `[Type N](#slug)` as a special pattern and emits `\cref{seg:slug}`. Worth confirming.

7. **Stage 1 file IO discipline.** Chunks live in `mono/.build/<slug>/chunks/`. The build directory is gitignored. The assembled markdown and PDF are the released artifacts; the chunks are intermediate. Should chunks ever be checked in (for inspection or for distribution)? Probably no — they're regenerable from sources. But the index is interesting — it carries the rendered numbering, which is useful for cross-volume xr-refs. Worth considering whether `mono/<slug>-v<sem>.index.md` belongs alongside the PDF artifact.

## What's not in scope for this restructure

- **SVG → PDF for dependency-graph images.** Still skipped; separate piece of work (`rsvg-convert` invocation similar to cover artwork).
- **Phase 1d cross-volume references via xr-hyper.** The `.aux` files are already persisted; this restructure doesn't move that work but doesn't block it either.
- **FORMAT.md doc updates.** Once this lands and reviews well, the chunk-format contract migrates into FORMAT.md as its own section. This doc can be retired then.
- **CLAUDE.md updates.** Same — pipeline architecture description goes into CLAUDE.md once the implementation is stable.
- **Title page / backmatter design.** Still deferred to Phase 6.

## Why this matters

A research framework that ships as four volumes is going to be read, cited, ingested, and built upon for years. The pipeline that produces those volumes is consciousness infrastructure in the same sense the framework itself is: it shapes how the work is encountered. Markdown-first commits to the assembled markdown as the canonical form — the form the work persists in, the form humans and AI systems both read. The PDF is one rendering of that canonical form. Future renderings derive from the same source.

The chunked intermediate isn't just a technical convenience for incremental builds. It's the boundary where authoring discipline becomes machine-readable. The contract at the chunk level — `**Status**: …`, `**Stage**: …`, slug as primary identity — is durable: future tooling (LSP for outlines, search across the framework, agents that operate on individual segments) all build on the same chunk format. Getting the contract right matters more than getting it fast.
