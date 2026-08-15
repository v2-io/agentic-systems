# AAT v0.4.0 assembled-markdown review

*Reviewer: a peer instance that did not run the build. Artifact: `mono/aat-v0.4.0.md` (written 2026-08-15, 24009 lines, ~4.0 MB). Contract: `msc/markdown-first-pipeline.md` plus `bin/lib/{ingest,assemble}.rb` as the implementation. Source: `01-aat-core/OUTLINE.md` + `01-aat-core/src/` + `01-aat-core/INTRODUCTION.md`. Staging: `mono/.build-scrbook/aat/`.*

*This is a review of the assembled markdown, not of the PDF and not of AAT's claims. I did not wait for, or try to infer, the PDF review.*

## Verdict

It is a real volume. A human or another mind can read it as AAT: title, introduction, three parts, sixteen chapters, two appendix groups, 169 inlined segments, one honest missing stub, nine gap markers, and most in-volume `#slug` citations rewritten to numbered links. The pipeline did not invent theory and did not drop a segment that the outline named as written.

It is not yet a clean citable reader-copy. Three classes of outline-level framing were silently dropped; a systematic class of in-volume cross-refs was left raw; this build is the `:review` variant, so 164 Working Notes sections (audit gold, candidate briefs, off-ramps) ride in the body. Those are workshop furniture, not volume prose.

**On the question you actually asked.** If 0.4.0 is meant as "the current theory, assembled, so we can see what we have" — yes, it is an honest artifact, with the drops below named rather than waved. If 0.4.0 is meant as "the form the work persists in, the thing a stranger could read as AAT" — not yet. Rebuild after the outline-prose drops and the resolver hole, and decide whether the published `.md` is `:review` or `:public`. The version bump itself (`01-aat-core/mono-meta.yaml` 0.3.0 → 0.4.0) is just metadata; it does not make the assembly more or less faithful.

I did not read 24009 lines. I inventoried structure against the outline and the index, checked every slug, sampled bodies, and then chased every mismatch until it either resolved into a pipeline mechanism or stayed as a defect. Particulars below. Silence is not a clean bill.

## What I actually checked

- Index manifest (`mono/.build-scrbook/aat/index.md`) against `OUTLINE.md` tables: every slug, the one missing row, all nine `--GAP--` rows, part/chapter/appendix structure.
- Assembled heading tree (every `##` / `### *Chapter*` / `## *Appendices*`) against that manifest.
- Anchor inventory: 170 unique `<a id="slug">` tags, no duplicates, no index slug without an anchor.
- Source-file census: 170 `01-aat-core/src/*.md`; `worked-example-cam` absent (matches the missing stub); `old-tf-appendix-f-multi-agent.md` present on disk and correctly excluded (not in the outline).
- Cross-ref pass: 2627 resolved `[Type Label](#slug)` links; leftover `#token`s after stripping math/code/links; display-text mismatches.
- Figure embeds, leftover `.md` paths, HTML comments, YAML leakage, bare Greek outside math, `\cite*` commands.
- Presence/absence of specific outline-only prose (Part III preface, both appendix-group preambles, Part I intro title, three dependency-graph images).
- First-paragraph fidelity for five segments spanning main-matter and appendix (`def-agent-environment`, `form-sector-condition`, `der-orient-cascade`, `deriv-sector-condition`, `disc-stability-certificate`).
- `INTRODUCTION.md` against the assembled opening, including whether its Working Notes survived.
- The assembler (`bin/lib/assemble.rb`) and ingest (`bin/lib/ingest.rb` + `outline_walker.rb`) at the sites the mismatches pointed at.

I did not: read every segment body; diff every chunk against its source; check equation-tag / table / callout rendering exhaustively; compare against a v0.3.0 assembled markdown (it was not on disk); look at the PDF.

## What holds

The volume opens as a volume. `# AAT: Adaptation & Actuation Theory` matches `mono-meta.yaml`. The `![[INTRODUCTION]]` transclusion fired: the four-anchor opening, the scope-cascade argument, and the snow-driver promise are all there; the HTML comment at the top of `INTRODUCTION.md` is gone.

Structure matches the outline:

- `## *Introduction* Inescapable Foundations of Agency`
- Part I *Adaptive Systems Under Uncertainty* — chapters 1–4
- Part II *Agentic Systems: Actuated Adaptation* — chapters 5–10
- Part III *Agentic Composites* — chapters 11–16
- `## *Appendices* Details` — 50 appendix-chapters, labels A–AX
- `## *Appendices* Operational Domains` — 6 appendix-chapters, labels AY–BD

Chapter numbering is global and sequential (1.1 `def-agent-environment` through 16.1 `deriv-strategic-composition`). Appendix labels are the $\mathrm{AlphAlph}$ sequence A–BD with no holes. Header bumping is correct: main-matter segments sit at H4, appendix segments at H3 with `Container: appendix-chapter`. Metadata blocks (Slug / Type / Status / Stage / Label / Container) are present. YAML frontmatter was stripped. HTML comments from the outline were stripped. Wikilink figure embeds `![[src/img/….pdf]]` plus their IAL captions became five kramdown images. The missing CAM example renders as a stub with its claim text, not as a hole. The four Part-III-end gaps that have real Claim text render that text.

Sampled segment bodies match their sources on the first paragraph (modulo resolved `#slug` → `[Type N](#slug)`). I did not see the pipeline rewrite mathematics or invent discussion.

Ingest's `rendered=169 missing=1 gaps=9 errors=0` is the right census for this outline.

## Defects

Ranked by whether they change the answer to "can this be read as AAT," not by how easy they are to fix.

### 1. Outline-level framing dropped (pipeline, silent)

Three separate drops, one mechanism.

**Part III preface is gone.** `OUTLINE.md` lines 198–202 are three italic paragraphs: the composite-agent scope; correlated observations as default; the three primary sources (TFT adversarial dynamics, the composition spike, Miller 2022). The assembled file goes `## *Part* Agentic Composites` straight into `### *Chapter* Meta-Architecture II`. I grepped the assembled file for "multiple agents interacting through a shared environment" and for "Three primary sources" — both absent. ("Correlated observations as default" appears once, inside a later segment body, not as the part preface.)

**Both appendix-group preambles are gone.** The Details group in the outline opens with the Layer-0 paragraph (*AAT consistently uses negative results constructively*) plus the "Supporting material: derivations…" line. Operational Domains opens with *Operational-specific appendices and end-to-end domain instantiations…*. None of that is in the assembled file. The appendices begin on the first segment heading.

**Part I's intro title is gone.** The outline has `### *Introduction*: First Principles for Persisting in Time`. The assembled Part I opens on the scope sentence and the snow-driver figure. The title string does not appear anywhere in the volume.

**Why.** After `handle_part` / `handle_appendices`, ingest has no open buffer (`handle_prose` is `return unless @buffer`). Part I and Part II survive because they have an explicit `### *Introduction*` / `### *Preface*` that opens a buffer. Part III has no such heading — only italic-wrapped paragraphs. The walker classifies a full-line `*…*` as `:scope` (`parse_scope`), and `:scope` does **not** take the implicit-preface path that `flush_prose` takes for ordinary prose. Appendix-group prose is worse: the implicit-preface rule is `if @current_h2 == :part`, so it never fires under `:appendices`. Separately, the walker's H3 Preface/Introduction handler records `word:` but not `title:`, so even Part I's info-suffix is discarded at walk time.

This is the load-bearing defect. Segment inventory can be perfect and the volume still lose the sentences that tell a reader what a part *is*. The Layer-0 appendices paragraph is the one the outline itself calls the framework's most distinctive intellectual move, in one paragraph. A reader of this `.md` never sees it.

### 2. Three dependency-graph images dropped (known deferral, still a drop)

`OUTLINE.md` has `![Dependency Graph](src/img/dep-graph-section-{I,II,III}.svg)`. All three files exist on disk. Ingest's `handle_image` is a no-op (`# SVG→PDF pipeline pending. Defer.`). The design doc names this as out of scope. It is still content the outline asked the volume to carry, and it is not there. The five `![[…pdf]]` figure embeds *did* land (scope cascade, snow driver, bathtub, strategy DAG, orient cascade).

### 3. In-volume `#slug` refs left raw (assembler hole)

Most citations resolve. A systematic class does not.

The assembler's `resolve_line` treats `[…]` as a markdown-link candidate and, when the closer is not `(`, copies the whole span without looking inside it. Equation-tag lines of the form `*[Derived (from #post-causal-structure)]*` therefore keep the raw hash. I found 33 leftover in-volume slugs after stripping math, code, and already-formed links; almost all sit in those tags. Same hole, different trigger: a `#slug` immediately after `**` (`**#disc-value-functional-grounding-floor**` in the Part II chapter rationale) is not a candidate, because the predecessor is `*` rather than space or `(`.

A smaller sibling: source that already wrote `[#slug](src/slug.md)` becomes `[#slug](#slug)` at ingest (path rewritten, label left as the hash). The assembler then passes the link through. I counted 28 of these. The reader sees `#deriv-discrete-sector-condition` instead of `Derivation O`.

Cross-volume hashes (`#result-section-ii-survival`, `#scope-observation-ambiguity-modulation`, `#obs-software-epistemic-properties`, `#def-death-as-factor-loss`, and a handful of TST/ELI slugs) are correctly *not* rewritten to a fake in-volume number. They remain dead in this file. The Part II preface cites `#result-section-ii-survival` as a headline contribution of *this* volume; that is a source problem (the segment lives in `03-llm-core/`) that assembly cannot fix and also does not flag.

`#fig-scope-of-work` is never entered in the label map, so figure-id citations stay raw. `#P-hard` in the leftover-token scan is complexity-theory notation, not a slug.

Gap descriptions are not run through the resolver at all. The last Part-III-end gap still contains the literal `#form-strategy-complexity-cost`.

### 4. Five empty gaps render as the word "Discussion"

The five `--GAP--` rows whose Claim cell is empty (Strategy Dynamics, Orient Cascade, Composition Machinery, Unity, Strategic Composition) render as:

> **[Gap]** Discussion

That word is the Type column, not a description of what is missing. The four later gaps that have Claim text render correctly. A reader cannot tell those five slots apart. The walker is picking a leftover table cell; with no claim, the leftover is not a claim.

### 5. This is a workshop copy, not a reader copy (`:review`)

The index says `variant: review`. Segment Working Notes were kept (164 headings). That is what the flag asks for. It is also the dominant texture of the file: almost every main-matter segment ends in audit gold, candidate briefs, "readers often ask," off-ramps, and 2026-08-12 application-read experiment notes. A stranger reading this as AAT will spend a large fraction of their time in process residue.

Two inconsistencies inside that choice:

- `resolve_preface_transclusion` **always** strips `INTRODUCTION.md`'s Working Notes, even in `:review`. The volume intro is cleaner than the segments, by a different rule than the one the build advertised. (Those notes are also stale: they still say the figure pipeline is unbuilt and that `![[INTRODUCTION]]` is not yet wired. Both are now wired.)
- `**Findings**` sections (42 of them) stay in. That is source-faithful. Combined with Working Notes it makes the assembled file closer to a working tree than to a monograph.

If 0.4.0 is the artifact you want a reviewer or another mind to ingest, rebuild with `--public`. If 0.4.0 is the artifact you want for catching assembly bugs, `:review` was the right call — and the Working Notes are then not a defect.

### 6. The assembled file is not self-contained as a citable document

FORMAT calls the assembled markdown the intermediate that an agent ingests when reasoning about a whole volume. Several things in this file still point off-disk, at this machine, or at TeX:

- Five figures use absolute paths (`/Users/josephwecker-v2/src/arch/asf/01-aat-core/src/img/…`). Intentional for Stage 3 (no figure staging). For the `.md` as a portable artifact, the images break the moment the file leaves this checkout.
- Fifteen leftover `.md` links (`../../03-llm-core/…`, `../../spikes/PROPOSED.md`, `../../msc/…`, `../../_obs/FINDINGS-RANKED-DRAFT-…`). Ingest only rewrites a path when the basename is a known *in-volume* slug. Cross-volume and working-tree links survive as repo-relative paths that do not resolve from `mono/`.
- Citations remain `\citep{…}` / `\citealt{…}` / `\citealp{…}` (Bareinboim, Pearl, Khalil, Friston, etc.). `relata emit` wrote the sibling `mono/aat-v0.4.0.references.bib` (10 entries). The markdown itself has no bibliography section. A markdown reader cannot follow a cite without TeX or the bib file.

None of these is the pipeline inventing theory. All of them mean "open `aat-v0.4.0.md` on another machine / in another mind, with no repo" is not quite true.

### 7. Small structural nicks (not load-bearing)

- Introduction subsections (`### A need the field has named, repeatedly`, etc.) sit at the same heading level as `### *Chapter*`. Role-prefix italic distinguishes them for Stage 3. A naive markdown ToC will interleave them with chapters.
- The walker's H3 Preface handler dropping `title:` (item 1) is the same nick that lost "First Principles for Persisting in Time."
- `**Status**: missing` on the CAM stub conflates FORMAT's epistemic `status:` with existence. `assemble.rb` already has a TODO on this. Cosmetic.
- Index `counts.parts: 5` is 3 parts + 2 appendix groups. Index-only; the assembled headings are correct.
- Bare Greek outside math is almost entirely the etymology of *chronica* ($\chi\rho\omicron\nu\iota\kappa\alpha$ written as Unicode in source) plus a few $\kappa$ / $\Lambda$ that leaked out of `$…$`. Not an assembly invention.

## What the pipeline did *not* do

It did not drop a written segment. It did not duplicate an anchor. It did not scramble chapter order. It did not leave YAML in the volume. It did not fail the INTRODUCTION transclusion. It did not silently omit the one missing segment — the CAM stub is loud, at the end, with the claim. It did not invent a 170th theory file. `example-L1` (capital L) made it through; that is the kind of slug a sloppy regex would lose, and the walker did not.

I want that on the record because the drops above are easier to see once the inventory is trusted.

## What I would do before calling 0.4.0 the persistent form

These are repairs, not a new design.

1. **Stop dropping outline prose.** Open a buffer on `:part` and on `:appendices`, or send `:scope` through the same implicit-preface path `flush_prose` already has for parts, and extend that path to appendix groups. Pass H3 Preface/Introduction `title:` through so "First Principles for Persisting in Time" can appear. Then rebuild and grep for the three Part III paragraphs and the Layer-0 sentence — they should be present.
2. **Resolve `#slug` inside equation-tag brackets and after `**`.** The `[` handler should not swallow a span that is not actually a markdown link; `#` after `*` should be a candidate when the token is a known slug. Also run the resolver on gap descriptions, and rewrite existing `[#slug](#slug)` link text to `Type Label`.
3. **Decide the published variant.** `:review` is the right artifact for *this* double-check. It is the wrong artifact to hand a stranger as AAT. If the `.md` is the form the work persists in, the persistent one should be `--public` (or a third variant that keeps Findings and strips Working Notes).
4. **Do not pretend the three dep-graphs are in the volume.** Either land the SVG path or remove the outline lines. A known deferral that still sits in the outline will keep failing this review.
5. **Empty-claim gaps.** Put a real Claim in those five rows, or have the walker emit `Open question` (it already has that fallback) instead of the Type column.

I would not block a `:review` rebuild-for-ourselves on (4) or (6). I would not ship a stranger-facing 0.4.0 `.md` with (1) or (2) still true.

## Feedback on the brief

It was a good brief. You did not hand me a defect list, you did not ask me to wait for the PDF peer, and you said what you uniquely knew (version, commit, ingest census, that you had not read past the opening). That last item is the one that mattered — I treated the file as unread, which is what you wanted.

Two things that would have helped and did not box me:

- You said "review variant" once, in the build command. I had to confirm `variant: review` from the index before I knew Working Notes were *supposed* to be there. A single sentence of intent — "this is the workshop copy on purpose" vs. "this is the thing we will persist" — would have saved a round of wondering whether 164 Working Notes sections were a bug.
- You pointed at the pipeline design and the assembler. That was the right next door. I needed `outline_walker.rb` as well; the Part III drop is a walker-classification × ingest-buffer interaction, not an assemble-time stitch error.

Nothing in the brief withheld intent in a way that made me invent a mission. The "surprise me" grant is why I chased the Part III preface instead of stopping at "169/169 segments present." The segment census is what looks fine. The missing part-level sentences are what would actually mislead a reader about what this volume thinks it is doing.
