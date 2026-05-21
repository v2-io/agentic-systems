# Integration Plan: Retroactive Meta-Segments-Before-Instances Sweep

*Plan author: Claude Opus 4.7 (1M context), 2026-05-21.
Mandate: apply Joseph's 2026-05-21 narrative-ordering discipline
retroactively to AAT's existing meta-segments, which currently sit in
appendix-style positions in `01-aat-core/OUTLINE.md` "out of an
overabundance of caution." Re-position and re-author each so the meta-
segment narratively *precedes* its first instance reference, reading as
a pedagogical exposition of methodology and merits.*

> Companion to `implementation-impossibility-meta-segment-plan.md`. The
> latter lands a *new* meta-segment correctly placed; this plan brings
> the *existing* meta-segments into line with the same discipline. The
> two are independent — this sweep does not depend on the
> implementation-impossibility landing — but landing the new meta-
> segment first provides a positive precedent for the authoring posture
> this sweep applies. Suggested sequencing: implementation-impossibility
> first, then this sweep.

---

## 0. The principle (recap)

Joseph 2026-05-21:

> "Auditors have surfaced the desire (and I concur) to have the meta
> segments well-established as a pattern immediately before the first
> instance — even if the pattern and methodology was discovered via
> convergence after several of the instances — narrative-wise,
> especially when they are at this level of maturity and usefulness,
> they should come before the segments that use them, (that also means
> not as an appendix, which we've unwisely done before out of an
> overabundance of caution in the past); they should be very well
> written expositions on the methodology and merits — almost
> pedagogical but authentic and respectfully peer voiced and with the
> same epistemic humility we try to apply everywhere."

The principle has two distinct components:

1. **Repositioning** — each meta-segment moves in the OUTLINE to a
   position before its first instance reference. Not as an appendix.
2. **Re-authoring** — the body of each meta-segment, where it currently
   reads as a synthesis-after-convergence style ("AAT has accumulated
   four results that share a pattern; here it is"), becomes a
   methodology-leading pedagogical exposition ("here is the pattern,
   why it matters, and what discipline governs it; here are its
   instances"). The substantive content (derivations, findings, cross-
   references) is preserved; the *narrative posture* changes.

The two components are coupled: a meta-segment placed before its
instances *should* read as forward-establishing (methodology-leading),
not as backward-synthesizing (convergence-recording). Repositioning
without re-authoring would leave the body voice mismatched with the new
location.

---

## 1. Priority targets

### 1.a Joseph 2026-05-21 named-priority

- **`01-aat-core/src/disc-identifiability-floor.md`** — the agent-side
  constructive-impossibility meta-pattern. Currently catalogs four
  instances + the Sylvester-mechanism recognition + the boundary-face
  positioning in the stability-certificate spine. Voice is
  synthesis-after-convergence (the §"Findings" Brief literally opens
  "Across four independently-derived results, AAT has converged on a
  recurring shape …" — convergence-led, not methodology-led).

- **`01-aat-core/src/disc-constructive-impossibility-posture.md`** —
  the cross-instance *style recognition* atop the boundary facet.
  Currently catalogs five cleanly-fitting instances. Even more
  convergence-led by its nature (it is *literally* a style-recognition
  pattern).

These two are first in line. They are also the most heavily-referenced
meta-segments in the framework — re-ordering them well is the largest
yield per move.

### 1.b Additional candidates (executor evaluates against OUTLINE)

The executor verifies current OUTLINE positions and confirms which need
moving. Likely candidates from a substantive-reading of the segments
(not OUTLINE-verified here):

- **`01-aat-core/src/disc-stability-certificate.md`** — the *spine*
  unifying the three facets (boundary / scope / forced-identity).
  Should *definitively* precede its facet meta-segments in the
  OUTLINE. The spine should come first; the facets follow. If it
  currently sits after the facets, that is the most important
  repositioning in the sweep.

- **`01-aat-core/src/disc-additive-coordinate-forcing.md`** — the
  forced-identity facet; covers four layer instances (chain /
  divergence / update / metric). Should precede its instance segments.

- **`01-aat-core/src/disc-separability-pattern.md`** — the scope facet;
  covers seven ladders' separable-core / structured-repair / general-
  open instances. Should precede the ladder segments.

- **`01-aat-core/src/disc-compression-operations.md`** — covers the
  four compression operations (model / strategy / shared-intent /
  composition projection). Should precede the operation segments.

- **`01-aat-core/src/disc-modularity-state-dynamics.md`** — *if* and
  when it lands (per PRACTICA's "Modularity-as-contested-property
  cycle"; currently scoped in `msc/modularity-cycle-plan-2026-05-09.md`
  but not yet landed). The forward-references to it from existing
  segments (per CLAUDE.md Key Architectural Decisions §7) already
  anticipate this discipline.

The executor *audits the current OUTLINE positions* before deciding
which to include in this sweep. Some may already be correctly placed.

---

## 2. Per-segment work (two-part)

### 2.a Repositioning (OUTLINE move)

For each priority meta-segment:
1. **Identify the segment's first instance reference** in the OUTLINE
   (the earliest segment that depends on it or cites it as a
   methodology source).
2. **Move the meta-segment to a position immediately preceding** that
   first instance reference. Not as an appendix.
3. **Verify dependencies via `bin/lint-outline`** — the meta-segment's
   `depends:` list and downstream `depends-on-this` set should remain
   consistent.

Suggested OUTLINE-organizational placement (executor evaluates against
the actual section structure of `01-aat-core/OUTLINE.md`): in a
"Meta-architecture" or "Methodology" section, *before* the substantive
theorem chapters that apply the methodology. If no such section exists,
the meta-segments are placed at the end of the chapter that introduces
their first instance (still narratively before; just chapter-end of
the introducing chapter rather than chapter-start of the using
chapter).

### 2.b Narrative re-authoring (segment body)

For each priority meta-segment, the body is re-authored to lead with
methodology, not synthesis. Concrete moves:

1. **Re-open the segment with the methodology.** Currently many meta-
   segments open with "AAT has accumulated N results that share a
   shape; this segment names the shape." The forward-leading version
   opens with the pattern itself — "Here is the constructive-impossibility
   five-step shape AAT applies repeatedly; here is why this discipline
   matters; here are its instances."
2. **Place the instances *after* the methodology**, not as a list-of-
   already-derived-results that the methodology emerges from. Instances
   demonstrate the pattern; they don't justify it.
3. **Keep the discovery-via-convergence narrative** — but move it to
   the §"Discussion" or §"Working Notes" rather than the lead. The
   honest history (the pattern was recognized after several instances
   had accumulated) is preserved; it just doesn't sit in the
   pedagogical-leading position.
4. **Strengthen the §"Findings" Brief** to follow the Feynman criterion
   — the Brief should be re-derivable from an everyday analog by a
   thoughtful non-specialist, *without* requiring the reader to have
   seen the instances first. Currently several Briefs assume instance-
   knowledge.
5. **Tone discipline.** Pedagogical but authentic; peer voice with the
   relevant adjacent literature; same epistemic humility AAT applies
   elsewhere (honest tier-marking on the meta-pattern's own status —
   typically `discussion-grade` at the meta-pattern level with
   instances carrying higher tiers; this stays).
6. **Preserve all substantive content.** No claims removed, no
   derivations changed, no findings dropped. The re-authoring is a
   *re-presentation* of what's already there.

### 2.c What does NOT change

- The meta-segment's substantive claims, derivations, and findings.
- The cross-references inbound from its instance segments (those still
  cite the meta-segment as their meta-pattern home).
- The tier classifications (the meta-pattern stays `discussion-grade`
  or whatever it currently is; the instances retain their per-instance
  tiers).
- The relationships to other meta-segments (sister-pattern / facet /
  posture cross-references).

---

## 3. Per-segment recommendations (executor verifies + refines)

### 3.a `disc-identifiability-floor`

- **Current opening (substantive recap):** "AAT has derived a class of
  structural impossibility results — *floors below which* identification
  or detection is impossible from limited information. Each floor
  arises by applying an external information-theoretic theorem … The
  floors are negative results in form but positive in consequence."
- **Forward-leading rewrite (suggested shape):** Lead with the five-step
  shape as the pedagogical entry point — "AAT recurrently applies a
  constructive-impossibility methodology with the following structure:
  (1) name an inferential task under a specific information regime …"
  Then explain *why* this discipline matters (the structural reason
  to use impossibility constructively rather than as inquiry-stoppers).
  *Then* introduce the four instances as demonstrations of the pattern.
- **Note:** The post-Object-B-landing version of this segment (per the
  identifiability-floor integration plan) is the right base to re-author
  from. This sweep should sequence *after* that integration lands.

### 3.b `disc-constructive-impossibility-posture`

- **Current voice:** explicitly catalog-style — recognizes a *style*
  across multiple instances, by its nature retrospective.
- **Forward-leading rewrite challenge:** this segment is by design
  cross-instance and discipline-recognition. The forward-leading move
  here is to lead with *what the posture is* (the methodological
  stance: treating impossibility results as recurring scope-honesty
  apparatus rather than inquiry-stoppers) *before* showing the five
  instances that exhibit it. The "this is recognition-tier, post-hoc"
  framing stays, but moves to Epistemic Status / Working Notes.
- **Tier:** stays `discussion-grade` (recognition, not theorem-
  derivation). The honesty about tier is itself a feature of the
  authoring posture.

### 3.c `disc-stability-certificate`

- **This is the spine.** Executor should verify its current OUTLINE
  position; if it currently sits *after* its three facets, repositioning
  is high-value. The spine unifies; the facets specialize. Reading
  order: spine → facets → instances of each facet.
- **Re-authoring:** if the spine currently leads with "AAT has converged
  on a single stability-certificate object with three facets," the
  forward-leading version opens with the certificate itself (what it
  is, why it matters, what the three-facet structure does for the
  framework's coherence), then introduces the facets.

### 3.d `disc-additive-coordinate-forcing`

- The four layer instances (chain / divergence / update / metric) are
  load-bearing. Forward-leading rewrite leads with the *underlying
  Legendre-Fenchel geometric object* and the *coordinate-forcing
  methodology* (an AAT-internal axiom + a uniqueness theorem ⟹ a
  forced coordinate), then introduces the four layers as
  demonstrations.
- The honest "this convergence across four independently-motivated
  axioms is itself the meta-pattern's substance" framing stays — moved
  to the §"Discussion" / §"Working Notes" rather than the lead.

### 3.e `disc-separability-pattern`

- Seven ladders are a lot to lead with directly. The forward-leading
  approach: introduce the *positive-scope methodology* (separable-core /
  structured-repair / general-open as a three-tier-per-ladder shape)
  with one example ladder demonstrating it concretely, *then* enumerate
  the seven ladders. Pedagogical scaffolding — give the reader one
  instance to anchor the pattern before showing the seven-fold
  application.

### 3.f `disc-compression-operations`

- The four compression operations (model / strategy / shared-intent /
  composition projection). Forward-leading approach: lead with the
  *shared IB shape* (the master IB objective + the U-medium honest scope
  caveat) and explain *why* the shared shape matters as an organizing
  principle, *then* introduce the four operations as instances.

### 3.g `disc-modularity-state-dynamics` (forward-looking)

- *Not yet landed.* When it lands (per PRACTICA's modularity cycle),
  it should land *correctly placed* from the start — narratively before
  its first instance, methodology-led. The existing forward-references
  from segments that mention M4 (per CLAUDE.md §Key Architectural
  Decisions §7) anticipate this discipline.

---

## 4. Order of operations

1. **Pre-flight.** Confirm the implementation-impossibility plan has
   landed (or is on the path to landing). That plan's new meta-segment
   serves as the positive precedent for correctly-placed authoring.
2. **OUTLINE audit.** Executor reads `01-aat-core/OUTLINE.md` in full
   and identifies the current position of each priority meta-segment +
   its first instance reference. This produces the actual repositioning
   target list.
3. **Per-segment workflow** (can be done sequentially or in parallel;
   each is largely independent):
   a. Reposition in OUTLINE.
   b. Re-author body for forward-leading methodology.
   c. Lint clean (`bin/lint-md` + `bin/lint-outline`).
   d. Verify cross-references inbound from instance segments still
      resolve correctly.
4. **Cross-reference sweep.** After all repositionings:
   `grep -rn "see #disc-\|cf. #disc-\|per #disc-"` to confirm inbound
   cross-references still point correctly (they should, but verify).
5. **CHANGELOG entry** — one consolidated entry for the sweep, or
   per-segment entries if the sweep is staged over multiple cycles.
6. **Commit** as a coherent commit per meta-segment (or a single sweep
   commit if all are done in one cycle).

---

## 5. CHANGELOG.md entry (draft)

```
## 2026-MM-DD — Meta-Segments-Before-Instances Narrative Sweep

The existing meta-segments — `#disc-identifiability-floor`,
`#disc-constructive-impossibility-posture`,
`#disc-stability-certificate`, `#disc-additive-coordinate-forcing`,
`#disc-separability-pattern`, `#disc-compression-operations` — were
repositioned in `01-aat-core/OUTLINE.md` and re-authored to lead with
methodology rather than synthesis-after-convergence, per Joseph's
2026-05-21 narrative-ordering discipline ("meta segments should come
before the segments they cover; not as appendices; very well written
expositions on methodology and merits — almost pedagogical but
authentic and respectfully peer voiced and with the same epistemic
humility we try to apply everywhere"). Each meta-segment now sits in
the OUTLINE narratively *before* its first instance reference, reads
as a forward-leading exposition (methodology → why it matters → instances
demonstrating the pattern), and preserves the discovery-via-convergence
history in §Discussion / §Working Notes rather than the pedagogical lead.

No substantive claims, derivations, or findings changed. Tier
classifications and cross-references preserved. The newly-landed
`#disc-implementation-impossibility` from the prior cycle served as
the positive precedent for the authoring posture this sweep applies
retroactively.

`#disc-modularity-state-dynamics`, when it lands per PRACTICA's
modularity cycle, will be placed correctly from the start.
```

The executor refines to the actual landing date and to the actual list
of segments that were in scope (some may already be correctly placed
and not need this sweep — the OUTLINE audit in §4 step 2 determines
the actual scope).

---

## 6. Verification — done when?

- Each priority meta-segment in §1 sits in `01-aat-core/OUTLINE.md`
  narratively before its first instance reference.
- Each priority meta-segment's body reads as forward-leading
  methodology — substantively unchanged but re-presented.
- `bin/lint-md` + `bin/lint-outline` clean.
- Cross-references inbound from instance segments still resolve.
- `bin/extract-findings` rolls up cleanly.
- CHANGELOG entry landed.

---

## 7. Honest scope

This is a *re-presentation* pass, not new content. The existing meta-
segments' substantive content stays. What changes:

- **OUTLINE position** (narrative ordering).
- **Body voice** (methodology-leading vs synthesis-after-convergence).
- **Findings Brief framing** (re-derivable from analog without instance-
  knowledge).

What does *not* change:

- Substantive claims, derivations, findings.
- Tier classifications.
- Cross-references inbound from instance segments.
- Relationships to other meta-segments.

The sweep is bounded by these constraints. If during the re-authoring
the executor surfaces a *substantive* issue (a derivation that needs
sharpening, a finding that needs revising), that is *out of scope* for
this sweep — surface it as a separate spike or TODO item, not a
within-sweep fix. The discipline of this sweep is purely re-
presentational.

---

*End of plan. The principle is Joseph's named discipline; the
substantive content is unchanged; what shifts is the framework's
narrative posture toward its own methodology. Authoring posture:
pedagogical but authentic; peer voice; same epistemic humility AAT
applies elsewhere. The implementation-impossibility landing serves as
the positive precedent; this sweep brings the existing meta-segments
into the same convention.*
