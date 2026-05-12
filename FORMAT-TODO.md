# FORMAT-TODO.md — Hierarchy, Naming, Numbering, and Compliance Sweep

*Live plan for the cross-cutting cleanup decided 2026-05-11 over the monograph-build conversation. PRACTICA.md is the parent navigator; this file owns the detail.*

The work spans the build pipeline (renderer, counter resets, cross-ref rendering), the project documentation (FORMAT.md, CLAUDE.md, OUTLINE.md), the source corpus (segment files, cross-ref hygiene, FORMAT compliance), and a final pass to bring the corpus into compliance with the decided convention. The order of operations matters: numbering/vocabulary lands first; source-side cleanup follows.

---

## The Decided Hierarchy

A ubiquitous shared vocabulary across source, tooling, and prose. Each level has exactly one canonical name.

| Level | Name | What it is | Examples |
|---|---|---|---|
| 1 | **Book** | the whole monograph | "the ASF book" |
| 2 | **Part** | one of the four theories | AAD, TST, LogA, ELI |
| 3 | **Chapter** | a scope-boundary within a Part | "Adaptive Systems Under Uncertainty"; "Common Roots"; each appendix-group is a Chapter |
| 4 | **Segment** | a numbered claim unit | Definition, Result, Derivation, Hypothesis, Scope, … (any of the 19 FORMAT types) |
| 5 | **Subclaim** | rare named sub-item *inside* a Segment | Corollary, "Linear case", "Scalar specialization" |
| 6 | **Field** | a structural section *inside* a Segment | Formal Expression, Epistemic Status, Discussion, Findings, Working Notes |
| 7 | **Atom** | a numbered named thing *inside* a Field | equation, table, figure, named-formula |

**Two name shifts from prior usage:**

- **"Section" → "Chapter"**: "Section" was overloaded with LaTeX's `\section` (the level below `\chapter`), and the build emits these as `\chapter`. Calling them Chapters everywhere removes the collision and matches what they typographically are.
- **"Subsection" / "Subsubsection" → "Field" / "Subclaim"**: the things inside a Segment aren't really sections — they're either fixed-name structural *Fields* (Formal Expression, etc.) or named *Subclaims* (Corollary, named cases). Two different concepts that were conflated.

---

## The Numbering Scheme

- **Parts** — Roman (I–IV), kaobook default. Visible on Part-page dividers and running headers. *Not* part of segment cross-ref display.
- **Chapters** — arabic, **reset per Part**. AAD has Chapters 1–5 (3 substantive sections + 2 appendix-groups); TST has Chapter 1; LogA has Chapters 1–5; ELI has Chapters 1–5. Cross-ref display: `Chapter II.2` (Part Roman + Chapter arabic).
- **Segments** — arabic, **reset per Chapter**. Cross-ref display: `Definition II.2.4` (Part.Chapter.Segment). The Part prefix matters because segments are referenced across Parts.
- **Subclaims** — arabic, **reset per Segment**. Cross-ref display: `Corollary II.2.4(c)` or similar. Rare in practice.
- **Fields** — *unnumbered*. Fixed names by FORMAT discipline; a number adds nothing.
- **Atoms** (equations, tables, figures) — separate counters per atom-type, **reset per Segment** (not per Chapter). Display: `(II.2.4-1)`, `Table II.2.4-1`. The per-segment reset is deliberate: atoms are always tied to a Segment (there are no chapter-level atoms in source), so resetting per-segment keeps atom IDs stable as segment ordering changes within a chapter.

### Named-formula atoms

Most equations in the corpus already carry a **name** inside their epistemic-label tag:

```
*[Derived (structural-persistence, from sector-persistence-template)]*

$$\alpha > \rho/R$$
```

The `structural-persistence` token is a de-facto stable name for the equation that follows. It is the *intrinsic* identity of the formula — meaningful, author-chosen, and (unlike a positional number) preserved across reordering. The build should extract that name and emit `\label{atom:structural-persistence}` on the equation, so a source-side cross-ref like `#structural-persistence` resolves directly to it.

This generalizes to all atom types where the author has supplied a name in the tag:
- `*[Definition (name, ...)]*` → label on the following definitional equation
- `*[Derived (name, from ...)]*` → label on the derived equation
- `*[Hypothesis (name)]*` → label on the hypothesis equation
- etc.

Named-formula labels then become the **primary, evergreen** cross-ref target for equations. Positional `\label{eq:<slug>-<n>}` labels stay as a fallback for unnamed equations but should be considered a degraded surface that source-side cleanup gradually replaces.

---

## Cross-reference evergreen-ness

The unifying principle behind the numbering and labeling scheme:

> **Cross-references target intrinsic identity, not positional accident.**

A segment's slug, a named atom's name, a subclaim's name — these are stable across reordering, renaming-resistant, and meaningful. A positional counter (segment 17 of chapter II, equation 3 of segment 17) is not — it shifts when content moves.

The conventions:
- **Always** cross-ref by `#slug-name` (segments) or `#atom-name` (named atoms) when a stable name is available
- **Never** rely on a rendered number ("see Definition II.2.4") for the cross-ref itself — the rendered number is *display only*, derived at render time, not part of the source-of-truth reference
- **Fall back** to positional atom labels (`#<segment-slug>-eq-1`) only for unnamed atoms, and treat that as a smell to be cleaned up

The renderer's job is to make `#<name>` resolve to the right rendered number at compile time. The author's job is to give every reference target a name worth referencing by.

---

## Implementation plan, in order

The phases are sequenced so each one assumes the previous has landed.

### Phase 1a — Build feature: Table of Contents

Adding a ToC is the obvious immediate next build-feature after planning. Independent of the numbering/vocabulary work below, so worth landing first as a quick win.

- [ ] Add a ToC to the build, placed in the front-matter (after the title page, before Chapter 1)
- [ ] Use kaobook's `\tableofcontents` machinery — already present, just not invoked
- [ ] Add a flag / signal to disable: either a build-script `--no-toc` option, or a special signal in the master `OUTLINE.md` (e.g., a frontmatter key) that the builder reads
- [ ] Confirm that Part / Chapter entries render with their numbering; Segment entries appear at the Chapter level (or one deeper) — depending on `secnumdepth` choice

### Phase 1 — Pipeline (build/renderer)

**Counters and cross-ref formats:**
- [ ] Reset the kaobook `chapter` counter at each `\part`, so Chapter numbers run 1…N within each Part rather than continuing across all Parts.
- [ ] Change `\thesegment` from `\Roman{chapter}.\arabic{segment}` to display the full Part-prefixed form (`\Roman{part}.\arabic{chapter}.\arabic{segment}` or equivalent). Cross-refs then read `Definition I.2.4`.
- [ ] Add a per-segment `atom` counter (or per-atom-type counters). Reset on each segment open.
- [ ] Switch equation and table counters to atom-style: reset per segment, display as `<seg>-<n>` suffix (e.g., `(I.2.4-1)`).
- [ ] Update `\crefformat{segment}` (and equation/table) to use the new format. Verify `#1` (stored label value) is used, not `\thesegment` at cref-time — already fixed for segments; double-check for equation/table.
- [ ] Renderer state: track current Part, Chapter, Segment for any places where these need to be available at LaTeX-emit time.

**Source-side title handling:**
- [ ] In the outline-walker, when emitting `\chapter{...}`, strip leading manual numbering from the title string (`I. Adaptive Systems...` → `Adaptive Systems...`, `§03.I — Primitive...` → `Primitive Logogenic Agents`, `§04.1 — Identity` → `Identity`). The kaobook chapter counter provides the number; the title is just the name.

**Atom-type guards:**
- [ ] Confirm `\refstepcounter{atom-counter}` happens once per atom emission, with `\label{eq:<slug>-<n>}` / `\label{tbl:<slug>-<n>}` immediately after.

**Named-formula labels (the evergreen path):**
- [ ] Parser: extract the *name* token from `*[Type (name, from ...)]*` eq-tags. First parenthesized token before any comma is the name.
- [ ] Renderer: when emitting a display equation that has a pending eq-tag with a name, emit `\label{atom:<name>}` *in addition to* the positional `\label{eq:<slug>-<n>}`. The named label is the primary cross-ref target; the positional one is a fallback.
- [ ] Cross-ref resolution: `#<name>` in source resolves to `\cref{atom:<name>}` if such a label exists; else falls through to the existing `\cref{seg:<name>}` segment lookup.
- [ ] Apply the same pattern to named definitions, named hypotheses, etc. — any atom that carries a name in its tag.

### Phase 2 — Documentation

- [ ] Update `FORMAT.md` to use the new vocabulary throughout (Section → Chapter; subsections → Fields and Subclaims). Update the segment-cadence diagram. Update the numbering examples (`Definition I.3` → `Definition I.2.4` in the canonical example).
- [ ] Update `CLAUDE.md`'s vocabulary references where it references the hierarchy.
- [ ] This file (`FORMAT-TODO.md`) becomes the active checklist; once Phase 2 lands, the *decisions* migrate into FORMAT.md and this file shifts to tracking remaining sweep work.

### Phase 3 — OUTLINE files

- [ ] Master `OUTLINE.md`: confirm Part structure (already clean).
- [ ] `01-aad-core/OUTLINE.md`: strip `I. / II. / III.` prefixes from H2 chapter titles. Keep the "Appendices: Details" and "Appendices: Operational Domains" names as-is (they become numbered Chapters automatically).
- [ ] `02-tst-core/OUTLINE.md`: already trimmed (Prior Work cut). Verify the single chapter renders correctly.
- [ ] `03-logogenic-agents/OUTLINE.md`: strip `§03.I —` / `§03.II —` / `§03.III —` prefixes. Keep "Common Roots" name as-is.
- [ ] `04-eli/OUTLINE.md`: strip `§04.1 —` / `§04.2 —` / `§04.3 —` / `§04.4 —` prefixes. Keep "Common Roots" name as-is.
- [ ] Section letter codes in tables (`| S |` / `| I |` / `| E1 |` / `| L1 |` etc.): decide whether to normalize. *Optional* — they're authoring shorthand; the renderer doesn't consume them. Defer unless they become a stumbling block during the source-side sweep.

### Phase 4 — Source segments: cross-ref hygiene

- [ ] **Class A** broken refs (`#slug-name` where the slug doesn't match any segment file): per ref, decide whether the slug needs to be fixed (typo / stale rename) or the target is genuinely missing (and the ref should be replaced with a TODO marker or a prose description). Class A is mechanical and can be largely automated against the slug list.
- [ ] **Class B** inline pseudo-refs (`Prop A.1`, `Constraint C3`, `Step 4` in derivations): these are author-typed prose, not first-class labels. Decide per-segment whether to (a) promote to first-class Subclaims with proper labels, (b) leave as prose and accept that they're not clickable, or (c) introduce a structured Subclaim convention only where the reference target sits in a different segment.
- [ ] Verify `\cref` round-trip: for each rendered `\cref`, confirm the click navigates to the segment whose number it displays. (The crefformat fix landed; this is a sweep to confirm.)
- [ ] **Named-atom cross-ref audit**: for each `*[Type (name, ...)]*` tag in source, confirm the name is unique within its segment (or globally if cross-segment named refs exist) and that `#name` correctly resolves to the labeled atom.

### Phase 5 — Source segments: FORMAT compliance

The linter (`bin/lint-md`) catalogued 200+ FORMAT violations across the corpus. Most are GFM/Obsidian-rendering hygiene that the LaTeX renderer's shims absorb, but the source should still come into compliance for round-trip fidelity.

Linter findings (totals at time of writing):
- 203 `\text` outside `$` delimiters
- 142 hard-wraps (auto-fixable)
- 72 bare `|` in math (use `\vert` / `\lvert`/`\rvert`)
- 55 raw `>` in math (use `\gt`)
- 50 raw `<` in math (use `\lt`)
- 49+34 `$$` display-math blank-line issues
- 41 emphasis-vulnerable underscores (auto-fixable)
- 16 bare `*` in inline math (use `\ast`)
- 11 `\|` in math (use `\Vert`)

Plan:
- [ ] Run `bin/lint-md --fix` for the auto-fixable categories (hard-wraps, emphasis-underscores, etc.).
- [ ] Manual sweep for the math-compatibility categories (`|`/`\|`/`<`/`>`/`*` in math). Most are mechanical; delegating to a sub-agent is appropriate.
- [ ] Address `\text` outside `$` — these are usually math commands that escaped their delimiters; per-instance review.

### Phase 6 — Optional polish

- [ ] Section letter codes in tables — normalize if Phase 3 didn't already do it.
- [ ] Slug rename audit — separate concern from numbering; lives under the broader naming-cycle work, not here.
- [ ] Subclaim structural convention — if Phase 4 surfaces a strong case for first-class Subclaim labels (e.g., for AAD's Appendix derivations like "Prop A.1", "Prop DA.2"), spec out the convention and apply.

---

## Sequencing notes

- **Phase 1 lands before any source-side sweep.** Cross-ref cleanup against the wrong numbering scheme is wasted work.
- **Phase 3 (strip manual chapter numbering) lands with or just after Phase 1.** The two are coupled — if we strip without Phase 1's counter changes, the rendered output loses numbers entirely; if we add the counter without stripping, we get doubled "I. I. Adaptive Systems..." in rendering.
- **Phases 4 and 5 can be delegated to a sub-agent** once Phase 1–3 are stable. The agent's brief should be: "verify and normalize per FORMAT.md; report broken refs that need human judgment."
- **Phase 6 is optional**, after Phases 1–5 have settled the corpus.

---

## What this plan does NOT change

- Slug names themselves (the canonical segment IDs) — that's the naming-cycle work, tracked elsewhere
- The substance of segment content
- The segment promotion stages (FORMAT.md §Promotion Workflow)
- The four-Part top-level structure (AAD / TST / LogA / ELI) — Joseph's hierarchy decision
- Existing cross-ref slug syntax (`#slug-name`) — the surface convention stays; only the rendering and counter behavior changes

---

## Status

Created 2026-05-11. Currently Phase 0 — plan written. Phase 1a (ToC) lands as the immediate quick win; Phase 1 (numbering/renderer) is the substantive work that gates everything downstream.
