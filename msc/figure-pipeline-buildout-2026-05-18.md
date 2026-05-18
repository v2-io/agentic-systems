# Figure pipeline build-out — working memo (2026-05-18)

**Status: in progress (autonomous; Joseph AFK).** Working substrate, not a
deliverable. Future-me / Joseph reviewable.

## Mandate

Joseph: teach `bin/build-monograph` to render figure embeds. AFK, granted
autonomy to be "thoughtful and holistic and wise", and to pull in other
diagrams from `src/img/`, `spikes/visual/`, `audits/AUDIT-*` as warranted.

### Locked decisions (Joseph, 2026-05-18, via AskUserQuestion)

1. **TikZ resolution.** On a figure embed pointing at `X.pdf`, if `X.tex`
   exists, `\includestandalone{X}` it natively into the monograph run
   (vector; via the `standalone` package), **not** a separate compile.
   Fall back to `\includegraphics{X.pdf}` (then `.svg` via rsvg-convert,
   mirroring `stage_cover_pdf`) when no `.tex` / standalone fails.
2. **Numbering/captions/crossrefs.** Decide + build now (not deferred).

### My scoping judgment (conservative where editorial)

- The **mechanism** (resolver + standalone include + caption/label/number
  + crossref, both render targets) is the firm deliverable.
- Figures must be **first-class atoms in the existing `#slug` cross-ref
  system**, not a parallel one (project anti-pattern test:
  parallels-infrastructure ⇒ framing wrong; cross-ref machinery already
  exists in `assemble.rb` / `segment_renderer.rb`).
- **Editorial insertion is conservative.** Auto-wire a found figure into
  monograph prose only with clear textual warrant (e.g. the intro's
  explicit "the reader should expect to meet [a figure]" hook that
  `scope-of-work` filled). Everything else: catalogued with a judged
  recommendation for Joseph, **not** silently spliced into published
  prose. Placing a figure in the monograph is an editorial act; absent
  warrant it waits for his eye.

## Plan / checklist

- [ ] Baseline: build AAT scrbook (+ kaobook) green BEFORE changes.
- [ ] Study: cross-ref system, atom/figure numbering model, preface-chunk
      render path, both typeset targets, `standalone` availability.
- [ ] Design the markdown figure convention (caption + `#fig-` label,
      integrated with existing crossref + atom numbering).
- [ ] Implement: resolver (ingest/assemble) + segment_renderer emission +
      `\usepackage{standalone}` in both preambles + both typeset targets.
- [ ] Verify: scope-of-work renders in the built PDF; a `#fig-…` crossref
      resolves; both targets build; pre-existing content unchanged.
- [ ] Survey src/img/ + spikes/visual/ + audits/AUDIT-* ; judged catalog.
- [ ] Wire only textually-warranted figures; catalogue the rest here.
- [ ] Commit in disciplined, explicit-pathspec, logically-separate steps.

## Decision log

- **Scope:** scrbook only (Joseph 2026-05-18). Implement in the shared
  `segment_renderer`/`ingest` (kaobook inherits free) but only verify
  scrbook; do not break kaobook, do not polish it.
- **Baseline:** `bin/build-monograph aad` → exit 0 BEFORE changes;
  artifact `mono/aat-v0.2.0s.pdf`. Reference point for "didn't regress".
- **Figures = the table atom, generalized.** `convert_table` is the
  model: `\captionof{<float>}{cap}\label{<ns>:slug}` in-flow (NOT a
  floating env — matches "figure sits where the prose puts it"),
  `\needspace` orphan guard. Figures mirror it: `\captionof{figure}` +
  `\label{fig:<slug>}`, centered include, in-flow.
- **Cross-ref integration (not parallel).** `#slug` already → 
  `\cref{seg:slug}` in `segment_renderer.process_prose`; a slug whose
  name starts `fig-` instead → `\cref{fig:slug}`. Purely lexical, no
  registry; consistent with the project's role-prefix slug discipline
  (`def-`, `disc-`, … → `fig-`). `postprocess_latex` only rewrites
  `\cref{seg:…}` to `\externalref`, so `fig:` refs pass clean.
- **Markdown convention** (mirrors tables' `{caption=…}` IAL): the
  Obsidian embed, optionally followed by a Kramdown IAL line:
  `![[<path>]]` then `{#<fig-slug> caption="<text>"}`. Renders in
  Obsidian as the image (IAL shows as small text, as table IALs do).
  Bare `![[path]]` (no IAL) = centered, numbered, uncaptioned,
  unlabeled (graceful, like an empty-caption table).
- **TikZ-first include (Joseph's call).** Resolver, given `<path>`:
  if a sibling `<base>.tex` exists → `\includestandalone{<absbase>}`
  (vector, native; host gets `\usepackage{standalone}`); elif `.pdf`
  → `\includegraphics`; elif `.svg` → rsvg-convert→pdf then
  `\includegraphics`; else LOUD visible placeholder + warn (never
  silent), mirroring the cover's loud-failure discipline.
- **Path strategy:** resolve the embed's relative src against the
  component dir (`Pathname(@spec[:outline]).dirname`, as
  `resolve_preface_transclusion` already does) to an ABSOLUTE path at
  ingest time, baked into the normalized Kramdown image. body.tex is
  a regenerated gitignored stage artifact, so absolute paths are fine
  and avoid all stage-copy plumbing (cover needs staging only because
  it's referenced from committed main.tex via build-info; figures live
  in regenerated body.tex).
- **Resolver placement:** `ingest.rb`, applied to the preface body
  (needed now) AND segment bodies (general; no-op without embeds), so
  a figure can appear anywhere, not just the intro.

## ⚠ Critical finding — `\includestandalone` is structurally incompatible

Joseph's AskUserQuestion choice was "`\input` the standalone `.tex`
directly" (`\includestandalone`). Empirically, that choice is **not
viable here**, for a structural (not tweakable) reason — flagged for
his review; I deviated, with rationale, rather than ship a regression:

- First green-looking build silently **collapsed 637 pages → 8**.
  Exit 0, no LaTeX "error" — LaTeX *cleanly* ended the document early
  at the figure. The assembled markdown was full (2.2 MB), so it was
  a typeset-stage truncation.
- LaTeX log: `(\end occurred when \if on line 39 was incomplete)` —
  line 39 = the `\includestandalone`. Isolated harness (`/tmp/sotest`)
  confirmed: **every** `\includestandalone` variant fatally errors
  `! Undefined control sequence \scopeclass` at the figure's first
  body line; `\includegraphics` of the compiled PDF works (clean,
  no leak).
- Root cause: `\includestandalone` does **not** execute the subfile's
  *preamble* — exactly where the refactor's `\scopeclass`/`\rail`
  engine lives — and it needs subfiles known at *main-preamble* time
  to hoist their preambles, whereas this pipeline discovers figures
  mid-body. Structural mismatch, not a setup bug. (Note: the refactor
  that made the figure a clean tool is *also* what makes it
  incompatible with naive `\includestandalone` — engine-in-preamble.)

**Resolution (honors the intent, not the literal mechanism):** the
resolver compiles the `.tex` to PDF with `lualatex` when the `.tex`
is newer than (or the) `.pdf` — so the **`.tex` stays source of
truth, output is vector, regenerated from source** (everything
Joseph wanted from "pull in the tikz"), via the robust
`\includegraphics` path. The committed `.pdf` is the cache/artifact
and fallback. Per strengthen-before-soften: this is the stronger
path to the goal, not a softening to "just use the committed pdf".
Host preamble: only `graphicx` needed now (the standalone/tikz/libs
block I added for the broken approach is removed — less monograph
preamble surface).

## Final status (verified)

- **Works, no regression.** `bin/build-monograph aat` → exit 0, **649
  pages** (orig ≈637; +≈12 = the figure + intro embed now rendering &
  reflow — an addition, not a loss; 1604 deep-content keyword hits
  confirm body intact). The catastrophic 637→8 collapse was caught
  (page-count check) and fixed.
- **Figure renders** in the Introduction (vector, recompiled from
  `scope-of-work.tex`), sized to the text block, in-flow where the
  prose promises it.
- **Numbered + cross-reffable.** `.aux`:
  `\newlabel{fig:fig-scope-of-work}{{1}…figure.0.1}` and a `@cref`
  entry `[figure][1]` — it **is Figure 1**; `#fig-scope-of-work`
  anywhere → `\cref{fig:fig-scope-of-work}` → "Figure 1". Flat
  volume-wide numbering decision is in effect and front-matter-safe.
- **Caption renders "Figure ." (bare, no inline number) — and that
  is consistent with the project's existing behaviour: every TABLE in
  the monograph renders "Table ." the same way.** The number is
  delivered at `\cref` sites by the project's deliberate cross-ref
  convention (setup.tex: "the type word kept in the markdown link
  text … LaTeX renders the number alone"), not inside the caption.
  So this is house style, NOT a defect introduced here. Whether the
  project wants caption-embedded numbers ("Figure 1: …" / "Table
  3.2: …") is a **pre-existing, monograph-wide caption-format
  question that equally affects tables** — explicitly out of scope
  for this figure work; flagged for Joseph, not unilaterally changed.
- **No tracked-file mutation by builds** (`.mono.pdf` gitignored;
  committed `scope-of-work.pdf` untouched). Build stays idempotent
  and multi-agent-safe.

## Findings / surveyed-figure catalogue

**Survey scope decision (wise/conservative).** The mechanism is the
firm deliverable; it is now *general* (any `.tex`/`.svg`/`.pdf`/`.png`
embed in any segment or preface works). Editorial *placement* of
figures into monograph prose is a separate act needing textual warrant
and ideally Joseph's eye — done conservatively: **only scope-of-work
wired** (it had explicit prose warrant: the intro literally promised
"a figure the reader should expect to meet early"). Everything else is
catalogued with a recommendation, NOT spliced in — placing figures
into the voiced monograph unilaterally while Joseph is AFK and another
agent is active in the tree is not wise.

### `01-aat-core/src/img/` — the legitimate monograph figure pool

The mechanism handles all of these as-is (no further pipeline work):

- **TikZ `.tex` (source-of-truth; recompiled on change):**
  `scope-of-work` ✅ wired (intro). `orient-cascade`,
  `driver-snow-foundation`, `sector-cone`, `strategy-dag-example`,
  `bathtub-scaffold` — all monograph-grade, each with an obvious
  conceptual home by slug (orient-cascade → the orient-cascade
  derivation; sector-cone → sector-condition stability;
  driver-snow-foundation → the recurring driver/snowstorm worked
  anchor named in the Introduction; strategy-dag-example → strategy
  DAG; bathtub-scaffold → the persistence "bathtub" Feynman gloss the
  project explicitly canonizes). **Recommend** Joseph (or a warranted
  follow-up) embed each at its segment via the now-trivial convention:
  `![[src/img/<name>.pdf]]` + `{#fig-<name> caption="…"}`.
- **`.svg`-only (no `.tex`):** adaptive-cycle, agent-environment,
  agent-spectrum, chain-confidence-decay, complete-agent-state,
  dep-graph-{full,section-I,II,III}, gain-sector-bridge,
  mismatch-decomposition, persistence-condition, recursive-update,
  satisfaction-gap-control-regret, sector-condition-stability,
  temporal-nesting. The resolver renders these via cached
  `rsvg-convert`→pdf. Several (agent-spectrum, persistence-condition,
  mismatch-decomposition, satisfaction-gap-control-regret) are strong
  candidates; the `dep-graph-*` are dependency graphs — likely
  apparatus, not monograph body. Same recommendation: warranted
  embed, not auto-splice.

### `spikes/visual/` — NOT monograph material

`catalog-ideation.md`, `diagram-catalog-ideation.md`, `car-as-agent.md`,
`epistemic-labeling-schema.md`, `attempts/`, `surveys/` — these are
diagram *ideation / working notes*, not finished figures. Correctly
excluded from the monograph.

### `audits/AUDIT-*/` — GATED, untouched

`AUDIT-WORKING-*` per-segment `.png/.pdf/.tex` are auditors' working
renders. CLAUDE.md / audits/README.md impose a **standing
non-optional gate**: no processing/mining/cleanup of `AUDIT-WORKING-*`
without consulting Joseph. I did not read, mine, or pull any of them —
only listed top-level names to confirm they are out of scope. They
stay untouched.

### Net recommendation

Ship the mechanism + scope-of-work. The other `src/img` figures are a
fast follow-up *with Joseph's editorial eye* (which figure lands in
which segment is a voice/placement call), now that embedding is one
two-line convention and the build renders it correctly.

## Scattering wired (2026-05-18, Joseph-sanctioned autonomous)

Joseph asked for "a scattering of figures to compare and contrast" —
one or more per chapter, verified not-stale, driver-snow-foundation
into the Part-1 preface specifically. Source = `01-aat-core/src/img/`
only. **Deliberately did NOT touch `audits/AUDIT-*`** (standing
consult-Joseph gate; he was asleep, could not decide-with-me) nor
`spikes/visual/` (ideation, not figures). Each figure was
**verified against current canon before wiring** (the load-bearing
part — a theory-contradicting figure is worse than none):

| Figure | Home | Staleness verification |
|---|---|---|
| `scope-of-work` | Volume Introduction | (earlier) |
| `driver-snow-foundation` | **Part I Introduction** (OUTLINE.md inline part-preface — Joseph's named want) | v2 2026-05-15 Joseph-revised; uses current AAT notation (δ, ρ, 𝒯, R, α, `#scope-adaptive-system`); **persistence-fail `ρ>αR` matches canon exactly** (`der-team-persistence.md`). Cruft fixed: dangling `#der-delib` → live `#der-deliberation-cost`. |
| `bathtub-scaffold` | `persistence-and-limits-intro.md` (Part I) | Matches the canonical Alan-Walton bathtub gloss (water=mismatch, inflow=drift, drain=correction, rim=capacity); companion slugs `#result-persistence-condition`/`#disc-stability-certificate` live; compiles via the .tex→.mono.pdf path. |
| `strategy-dag-example` | `strategy-structure-intro.md` (Part II) | Single-parameter AND/OR edge credences — matches the canonical model; noisy-OR / WEIGHTED (rejected variants) absent. `#def-strategy-dag` live. |
| `orient-cascade` | `impl-orient-cascade.md` (Part II) | Five-step cascade + 2×2 diagnostic matches `#der-orient-cascade` (live; its derivation prose in the same chapter describes exactly this ordering). |

`sector-cone` (and the `.svg` set) left **catalogued, not wired** —
five is a good scattering for design intuition; over-splicing the
monograph unilaterally is not wise. They are one two-line embed away
whenever Joseph wants them.

Editorial placement: all into discussion-grade chapter-intro / impl
segments or prefaces (low-risk boundaries), self-captioned, plain-prose
captions, no insertion into dense derivations, no voice-contract prose
altered.

**Scattering build verified:** `bin/build-monograph aat` exit 0,
**651 pp** (≈637 baseline + 14 = the 5 figures + reflow — an
addition, not the 8-pp collapse class), all 5 `\includegraphics`
from freshly-recompiled `.mono.pdf` + all 5 `\label{fig:…}` present,
no LaTeX trouble, committed `src/img/*.pdf` unmutated. driver-snow
visually confirmed rendering correctly in the Part I Introduction
(schematic + translation table + the cruft-fixed
`#der-deliberation-cost` cell + `ρ>αR`).

**Honest caption note (corrected a misread):** the caption renders
"Figure : <text>" — *bare, no inline number* — which is **exactly
how every TABLE in the monograph already renders ("Table .")**. The
number is delivered at `\cref` sites (`.aux`:
`\newlabel{fig:…}{{1}…}` etc., one per figure). So numbering +
cross-ref WORK; the in-caption number is suppressed by the project's
pre-existing caption convention that affects tables identically. I
briefly misread a low-res render as "Figure 2:"; raw `pdftotext`
("Figure :") is authoritative and is reported here. Whether captions
should carry inline "Figure N:/Table N:" is a **monograph-wide
caption-format decision for Joseph** (it would change tables too) —
explicitly NOT made unilaterally.
