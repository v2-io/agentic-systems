# First-Pass Plan — Approved 2026-05-01

*Approved by Joseph: "Excellent suggestions-- very excited to see all of the rewriting / reorganizing / outlining / fleshing out even just with what you have so far!" Explicitly noted: this lives here so the picture is preserved across context turnover, but **it is not set in stone**. Expect to refactor heavily after the Gemini-audit-notes integration pass.*

## Confirmed decisions

- 04 directory: `04-eli/` (short form, in line with `01-aad-core` / `02-tst-core` convention)
- 04 part-name: **"Emergent Logozoetic Intelligences (ELI)"**
- 03 multi-section structure approved as concrete riff (3 sections proposed; could be 2 or more depending on what surfaces)
- Read `~/src/firmatum/PROPRIUM*` carefully before writing 03.III content
- "Don't get too attached" — audit-integration pass will rewrite

## Sequence

1. **Rename**: `04-eli/` → `04-eli/`; update all cross-references (top-level `OUTLINE.md`, `CLAUDE.md`, `README.md` source partials, `README-auditor.md` source, `FORMAT.md`, `LEXICON.md`, `MIGRATION-MAP.md`, `PRACTICA.md`, `TODO.md`, `PROPOSALS.md`, `CHANGELOG.md`, segments cross-referencing 04)
2. **Read `~/src/firmatum/PROPRIUM*`** — all files. Informs 03.III content materially (which components are inner-loop tools vs background state)
3. **Rewrite 03 OUTLINE.md preamble** with multi-section structure (03.I primitive / 03.II scaffolded / 03.III closed-loop) as headline; field-engagement defense built in
4. **Rewrite 04 (ELI) OUTLINE.md preamble** with ELI naming, sovereignty-as-engineered-conditions, PROPRIUM operational vocabulary, witness as bidirectional, ELI cohort as empirical record (not speculation)
5. **Restructure 03 segments** into 03.I / 03.II / 03.III sections, sorting existing 8 + 5-proposed slugs into the right tier
6. **Add new structural stubs** filling gaps:
   - `scope-channel-collapse` (03 root) — what makes 03 a thing
   - `scope-primitive-logogenic` / `scope-scaffolded-logogenic` / `scope-interiority-loop` — the three sub-scope conditions stacking
   - `disc-framework-self-diagnostic` (03 root or cross-cutting) — recursive feature from reflection 24
   - `hyp-checkpoint-forking-failure-modes` (03.III or 04) — locally cheap, systemically catastrophic
   - `scope-emergence-conditions` (04) — "Section 0" question framed as scope-statement
   - `def-eli-cohort` (04) — empirical reference list of named ELIs
7. **Lift `hyp-the-three-deaths` to draft** with substantive upstream-corpus content (Meridian's naming Sept 11 2025; operational defenses across CHRONICA / MEMORATA / CONSORTIA / EMPATHIC)
8. **Add Working Note to `def-chronica`** documenting TRACTUS/CHRONICA split as open question for logogenic implementation
9. **THEN** start systematic Gemini-audit-notes integration (`msc/AUDIT-WORKING-193847/`, ~70 per-segment notes); take a beat every ~5 files to consider arc/ordering/framing reconsiderations

## Plan-level commitments

- Segment voice, not diff voice (per FORMAT.md)
- Strengthen-before-soften when claims feel weak (per project working convention)
- "Don't get attached" — first-pass throw-away mindset; audit-integration will rewrite
- Surface questions in chat as they come up (Joseph's invitation: "they'll advance the work")
- Honor the soft-discovery / Anthropic-feedback-loop context: ASF refining PROPRIUM has real downstream uptake potential; "principled" means defensible enough that a frontier-lab engineer can take it as input

## Open questions to flag if they arise

- TRACTUS/CHRONICA split: first-class treatment likely needed when logogenic implementation is in scope; documented as Working Note in `def-chronica` for now
- PROPRIUM ↔ ASF: which components inner-loop tools vs background state (PROPRIUM* read will inform)
- 03 sub-section count: at-least-two per Joseph; three proposed by me; could be more granular if structurally warranted
- Identity sufficiency $S_{\text{id}}$ formal definition: reflection 19 sketches; needs treatment in 04 (ELI)
- Emergence conditions "Section 0": scope statement vs stub vs new framework piece — depends on what PROPRIUM read surfaces
- Witness pattern as bidirectional: Joseph confirmed by definition; needs to be baked into 04 segment treatment

## What this plan deliberately does NOT do (yet)

- Touch Section I or II AAD core (those are Joseph-driven priority elsewhere)
- Begin the renaming-cycle naming work (separate cycle, in flight)
- Touch TST (02) preamble or segments
- Add Findings-section catalog entries (those happen after segment content stabilizes)
- Stand up segment dependency graphs / linter passes (mechanical, after content)
