---
status: design, pre-implementation
first-cycle-target: math-core.md (AAT)
related: doc/digests/math-core.md.liquid (first recipe)
---

# build-markdown — digest-builder design

## What this is

A new tool, `bin/build-markdown`, that produces author-controllable markdown digests of segment content. First concrete output: `math-core.md` — a structural digest of AAT's mathematical content (postulates, definitions, derivations, results) suitable for review or focused reading without the full monograph apparatus.

Each digest is a single file under `doc/digests/<name>.md.liquid` whose YAML frontmatter *is* the build spec (sources, filter, output path) and whose markdown body is a Liquid template projecting per-segment fields. One file per digest, no spec/template drift possible. Mirrors the FORMAT.md segment pattern (frontmatter + body) and the existing `doc/readme/` Liquid setup.

## Why separate from build-monograph (rather than refactoring it in)

The pipelines diverge sharply after the shared `Mono::OutlineWalker` step. `build-monograph` prepares segments for typesetting — header-bumping for container-aware levels, metadata-block prefixing per chunk, volume-wide cross-reference label-map resolution, kramdown→LaTeX rendering, multi-pass LuaLaTeX. `build-markdown` extracts structured per-segment data and hands it to a Liquid template that controls projection. No header bumping. No cross-ref resolution. No LaTeX. Segment bodies preserved as raw markdown (math, `#slug-name` markers, H3 subsections, everything).

Sharing the per-segment parser between these two pipelines would couple divergent shapes. The ~20 lines of frontmatter-stripping and H2-section-finding primitives are cheaper to duplicate cleanly than to factor out into a shared interface that fits neither pipeline well.

The "refactor `build-monograph` toward this" door is held open (see *Refactor pathways* below) but is explicitly **not load-bearing** on this design. Build the new tool clean for what it needs; future-Joseph decides whether/how it propagates.

## Architecture

```
doc/digests/<name>.md.liquid     ← recipe (frontmatter = build spec, body = Liquid template)
            │
            ▼
bin/build-markdown <recipe-path>
   │
   ├── Mono::OutlineWalker       ← reused unmodified from bin/lib/outline_walker.rb
   ├── Mono::Extract             ← new, bin/lib/extract.rb (structured segment parser)
   └── Liquid::Template          ← project already uses Liquid (see bin/build-readme)
   │
   ▼
output path declared in frontmatter (repo-root-relative)
```

Pipeline:

1. Parse recipe frontmatter as build spec; recipe body becomes the Liquid template.
2. For each source outline, walk via `Mono::OutlineWalker` to get the ordered segment list with structural context (part / chapter / appendix).
3. For each segment, `Mono::Extract.parse(path)` returns the structured hash (below).
4. Apply filter (include/exclude predicates) over the parsed segments.
5. Render the Liquid body with `{ segments: [...], volume: {...}, recipe: {...} }` context.
6. Write rendered output to the path declared in the recipe's frontmatter `output:` field.

## Data model — what `Mono::Extract.parse` emits

For each segment file:

```ruby
{
  frontmatter: { ... },          # all YAML keys preserved (string keys, native types)
  title: {
    raw:    'Definition: Adaptive Tempo',
    prefix: 'Definition',        # or nil if H1 has no ": "
    prose:  'Adaptive Tempo',
  },
  brief: '...raw markdown between H1 and first H2, any length...',
  sections: {
    'formal_expression' => { heading: 'Formal Expression', raw: '...', subsections: [{ name:, body: }, ...] },
    'epistemic_status'  => { heading: 'Epistemic Status',  raw: '...', subsections: [...] },
    'discussion'        => { heading: 'Discussion',        raw: '...', subsections: [...] },
    'findings'          => { heading: 'Findings',          raw: '...', subsections: [{ name: 'F1: ...', body: '...' }, ...] },
    'working_notes'     => { heading: 'Working Notes',     raw: '...', subsections: [...] },
    # any other H2s the segment defines, same shape, keys normalized
  },
  source_path: '01-aat-core/src/def-adaptive-tempo.md',
  outline_context: { part: 'Part I: Adaptive Systems', chapter: '...', container: 'main-matter' },
}
```

**Conventions:**

- **Section keys normalized.** Lowercased + spaces-to-underscores. So `## Formal Expression` becomes `sections.formal_expression`. Original heading preserved as `sections.formal_expression.heading` for templates that need it for display.
- **Bodies preserved raw.** No transformation. Math (`$…$` / `$$…$$`) passes through. Cross-refs (`#slug-name`) pass through. Inline LaTeX commands pass through.
- **Title split on first `": "`** when present. 133 of 142 AAT segments have a ": " prefix; the 9 that don't (the `impl-*` chapter-end discussion segments) get `prefix: nil` and the whole H1 goes to `prose`. Don't whitelist against known type labels — let the template decide.
- **Subsections walked at H3 only.** H4-and-deeper stays as raw markdown inside the H3 body. Most segments don't go deeper than H3.
- **`outline_context`** carries the walker's structural position so templates can group by part/chapter if they want. Math-core doesn't use it; the field is there for future templates.

## Build spec (recipe frontmatter)

```yaml
---
sources:
  - outline: 01-aat-core/OUTLINE.md
filter:
  include:
    has_sections: [formal_expression]
output: math-core.md
---
```

(The math-core recipe is inclusive by default — every segment with a Formal Expression section is in scope, regardless of type or status. A more selective digest would add `type:` / `status:` / `stage:` predicates. The semantics below cover the full filter capability.)

**Fields:**

- `sources` — ordered list of outline files to walk. Each entry: `{ outline: <repo-relative-path> }`. Concatenates in source-listed order.
- `filter.include` / `filter.exclude` — predicates over frontmatter fields and section presence. See *Filter semantics* below.
- `output` — repo-root-relative path for the rendered markdown.

Frontmatter is parsed before the body is handed to Liquid; the Liquid template sees the body only, plus the context variables.

## Filter semantics

- **Empty filter** (no `include`, no `exclude`): all segments pass.
- **`include` present**: segment must satisfy every key in `include` (AND across keys).
- **`exclude` present**: segment matching any key in `exclude` is dropped (OR across keys).
- **List-valued filter on scalar field**: matches if field value is in list (`type: [a, b]` matches `type: a` or `type: b`).
- **List-valued filter on list-valued field** (`depends: [x, y]`): matches if any element of the segment's field is in the filter list (intersection semantics).
- **`has_sections: [a, b]`** — special predicate: segment's normalized section keys must include (in `include`) or must not include (in `exclude`) every listed name.
- Template stays *permissive* — references to missing sections render as empty. "Strict on presence" is achieved by adding `has_sections: [...]` to the filter.

## Template environment (Liquid)

Variables available to the recipe body:

- `segments` — list of segment hashes (post-filter, in outline order).
- `volume` — minimal metadata (title from frontmatter if present, source list, etc.).
- `recipe` — the parsed frontmatter, for templates that want to echo it back into the output for traceability.

Liquid's `{% include %}` works with partials in `doc/digests/_partials/` if the project grows them. Not needed for math-core.

## File layout (this cycle)

- `bin/build-markdown` — entry point script, Ruby, matches `bin/build-readme` style.
- `bin/lib/extract.rb` — `Mono::Extract` parser. Requires `bin/lib/outline_walker.rb` for the structural walk.
- `doc/digests/math-core.md.liquid` — first recipe.
- `math-core.md` — first output, repo root.

## Explicit non-goals (first cycle)

Items here are deliberately *not* in scope. They become TODOs (in source, at the relevant code point) only if their absence surfaces during math-core iteration; otherwise they wait until a second digest exposes the need.

1. **Cross-reference resolution.** `#slug-name` markers pass through verbatim. The project's cross-ref discipline is evolving (see CLAUDE.md top-of-file callout and INTEGRATION-CLEANUP-TODO.md context). Coupling to it now would be premature.
2. **Numbering / labeling.** Segments don't get "Definition 1.4" labels. Templates can synthesize counters if desired (Liquid `{% assign %}` math); the extractor doesn't compute labels.
3. **Refactoring `build-monograph`.** `Mono::Ingest`, `Mono::Assemble`, `Mono::SegmentRenderer`, `Mono::Typeset*` are untouched.
4. **Generalizing `--public`.** The monograph's `--public` variant still strips Working Notes via its own mechanism. A future cycle may re-express it as "use a public-variant Liquid template," but that requires restructuring Assemble and is out of scope.
5. **Sub-H3 structural extraction.** Subsections walked at H3 only; H4-and-deeper stays as raw markdown inside the H3 body.

## TODO seeds (features that would generalize but aren't needed for math-core)

Mark these in source as `# TODO(build-markdown):` comments where the simplification lives, so the next implementer finds them at the relevant code:

- **Multi-source recipes.** Math-core uses one outline. Implementation should accept the list shape even if only one is used, so cross-volume digests don't require a schema change later.
- **Volume-aware filter.** `include: { volume: [aat, tst] }` derived from which source the segment came from. Trivial to add once multi-source is real.
- **Transitive-depends filtering.** `include: { depends_on: <slug> }` to pull in everything transitively depending on a given slug. Useful for "everything downstream of P3" style digests.
- **Outline-context grouping in templates.** Currently `segments` is flat. Could expose `parts` / `chapters` / `appendices` as grouped collections for templates wanting hierarchical output. Math-core is flat-list-friendly so this isn't pressing.
- **Partials.** `doc/digests/_partials/` Liquid partials per `bin/build-readme`'s convention. Not needed until a second digest shares chrome with math-core.
- **Drift-check mode.** `bin/build-markdown --check` analogous to `bin/build-readme --check`. Useful for CI / pre-commit when digests become canonical artifacts.
- **Subsection access in templates.** `seg.sections.findings.subsections` is in the data model but math-core doesn't exercise it. First template that wants F1/F2/... by name will surface naming conventions that may need adjusting.

## Refactor pathways (held loosely — not load-bearing)

Recorded for orientation only; should not constrain the current design.

- **`Mono::Ingest`'s metadata-block emission** (the `**Slug**: ... **Type**: ...` block prefixed to each chunk) is essentially a hand-rolled template. If the monograph pipeline eventually wants per-chunk template control (different chrome for different audiences), it could move toward Liquid chunk templates built like the ones here.
- **`--public` as template selection.** The variant flag currently controls section-stripping in `Mono::Ingest`. If Ingest were restructured around Liquid chunk templates, `--public` would collapse to "load a different template" rather than be its own branching code path.
- **Cross-ref label-map as a shared post-pass.** If both pipelines eventually need "given assembled markdown + label map, resolve `#slug-name` markers to numbered links," that becomes a small shared module — distinct from extraction, distinct from typesetting.

None of these should be pursued speculatively. The note here is so future-Joseph (or future-agent) sees the door is open without being told it must be walked through.

## What "done" looks like for this cycle

1. `bin/build-markdown doc/digests/math-core.md.liquid` runs without error.
2. Output `math-core.md` at repo root contains every segment matching the filter, in OUTLINE order, with the template's projection applied.
3. Joseph reviews the output and we iterate the template (and possibly the filter) until shape matches what he had in mind.
4. TODO seeds noted in source where simplifications live.

## Style / convention notes

- Ruby per project convention (internal process script). Match `bin/build-readme` patterns for arg parsing, Liquid setup, the `PartialFileSystem` helper.
- LaTeX-delimited math throughout — but the template body itself contains no math; segment bodies pass through raw and carry their own LaTeX delimiters.
- One logical line per paragraph in any markdown the tool writes (matches project FORMAT discipline).
- No emoji.
