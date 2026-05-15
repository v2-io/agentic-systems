# 04 — Spine-segment authoring brief: all the pieces, assembled

**Purpose.** Joseph confirmed the full-spine move (2026-05-14). This file is the assembly brief: it points at every piece the spine segment `#disc-stability-certificate` draws on, states what the segment must and must not claim, fixes a rational-but-provisional OUTLINE position, and lays out the propagation plan to the other areas (which lands *in the segment's Working Notes*, per Joseph's instruction). Author the segment from this file + the pieces it points at; do not re-derive — the mathematics is done in `01–`/`02–`/`03–`/`99–`.

## The pieces (everything the spine rests on)

**From this spike directory:**
- `00-brief.md` — the question sharpened; the three attack lines; the leg ledger.
- `01-L1-stability-certificate.md` — **the anchor.** Prop L1-lin: one-point operator-sector in *some* inner product ⟺ linearized equilibrium exponentially stable (Hurwitz), by the standard Lyapunov theorem. Exact, proved. The R0/R1/R2 certificate-strength ladder (one-point / incremental / Čencov-forced). The Lyapunov-non-symmetric counterexample showing the object is the *certificate*, not a potential.
- `02-L3-floor-is-the-boundary.md` — M1 = cone boundary; the four M1 instances verified as certificate-rank-collapse; **Sylvester's law of inertia is the named irreducibility mechanism for the rank-collapse subclass.**
- `03-L4-projection-and-the-broken-triad.md` — composition = certificate's projection-defect (Schur survives, dynamic guarantee doesn't, ε* = memory-commutator norm); **the integrability triad is FALSE** — three irreducibly distinct obstructions (Helmholtz / Sylvester / Mori–Zwanzig), each invariant under the others' freedoms.
- `99-verdict.md` — completion-state 2 (succeed-at-claim, strong) + sharp plural no-go; the honest open edges.

**Already landed (do not re-land; cross-reference):**
- `#disc-identifiability-floor` — now carries the **Sylvester-recognition Finding** ("The Rank-Collapse Floor's Irreducibility Is Sylvester's Law of Inertia") + the Discussion paragraph naming the mechanism + a Working Note pointing here. Commit `d46671e`. The spine cross-references this; it does not restate it.

**Predecessor + adjacent (provenance, not restated in segment voice):**
- `spikes/.integrated/spike-operator-sector-unification.md` — the C1 predecessor; "2-instance-plus-1-consequence"; the prior co-owner "DO NOT elevate unless O-BP10 surfaces at segment level" gate (now *met* by L1).
- `spikes/spike-jacobian-b1-strengthening.md` §6/§7 — the (SOC) curvature-metric axiom; the verdict that the metric is *forced* only via Čencov (statistical scope), *matched* elsewhere — this is the spine's **M3-facet** content.
- `spikes/.integrated/spike-mori-zwanzig-composition.md` — the zero-lag kernel bound closes, the trajectory bound doesn't — the spine's **composition-facet** content.

**The segments the spine organizes (facets — cross-ref, canonical-home stays with them):**
- `#disc-identifiability-floor` (M1) — the **boundary** facet (certificate rank-collapse; Sylvester).
- `#disc-separability-pattern` (M2) — the **scope-of-existence** facet (where the certificate exists).
- `#disc-additive-coordinate-forcing` (M3) — the **forced-identity** facet (which certificate; Čencov forces it uniquely in statistical scope).
- `#result-sector-persistence-template` / `#result-contraction-template` — the **interior** facet (operator-sector = certificate ≻ 0; the Lyapunov machinery).
- `#form-composition-closure` — the **projection-defect** facet (ε* = memory-commutator; Liberzon = no common certificate).
- O-BP10 (PROPOSALS Bundle 1; naming-cycle "contraction-over-drift principle") — the slogan the spine grounds at segment level (L1 is the surfacing).

## What the segment must claim (and must not)

**Must** (each is verified in the spike; cite, don't re-derive):
- The certificate object: the equilibrium positive-definite form certifying self-correction (converse-Lyapunov metric; = Fisher / `(P⁻)⁻¹` / loss-Hessian / plant-Lyapunov-metric per sub-case).
- L1-lin equivalence as the anchor (exact; Lyapunov theorem). O-BP10 is an equivalence, not analogy.
- The four-facet correspondence: interior (operator-sector) / scope (M2) / forced-identity (M3) / boundary (M1) / projection-defect (composition).
- The three irreducibility theorems are **distinct** (Helmholtz / Sylvester / Mori–Zwanzig); the plurality is the load-bearing content — it is *why* AAD has multiple meta-patterns and not one.
- The R0/R1/R2 rung ladder, stated honestly.

**Must not** (the discipline that keeps it honest):
- Must not claim the four meta-patterns *reduce* to one theorem (the triad is false). One *object*, distinct *failure modes*.
- Must not over-state scope: L1 is linearized/local (the level AAD's persistence results already operate at — state this, don't paper it). "All of AAD's cross-section is this cone" is robust-qualitative synthesis; the per-facet identifications are exact/cited.
- Segment voice, not diff voice (FORMAT.md): no "the spike," no "2026-05-14," no "predecessor" in Formal/Status/Discussion. Spike provenance and propagation plan live **only** in Working Notes.
- Must not restate M1/M2/M3 content — cross-reference; canonical home stays with each (the cross-reference-vs-canonical-home discipline `#impl-composition-machinery` already models).

## Rational-but-provisional OUTLINE position

`## *Appendices* Details`, **immediately before `#disc-identifiability-floor`** (currently OUTLINE.md line 381). Rationale: the spine is the object the three M-meta-segments are facets of, so it reads first among them; placing it as the lead of the four-row meta-segment cluster (spine → M1 → M2 → M3) is the natural order. **Provisional** because: (a) the four meta-segments may eventually warrant their own chapter rather than living in Appendix-A Details; (b) if the OUTLINE preamble (line 17, currently "Three meta-segments form AAD's cross-sectional structure…") is reframed to lead with the spine, the cluster may move to a more prominent position. Both are propagation steps (Working Notes), not this-pass actions.

## Propagation plan (lands in the segment's Working Notes; summarized here)

Ordered by commitment, lowest first; the keystone (preamble reframe) is flagged for Joseph, not auto-executed:

1. **`#disc-identifiability-floor` ← spine cross-ref (low; partly done).** The Sylvester Finding + Working Note already point here (d46671e). Add one cross-reference line in its Discussion's "complementarity" paragraph naming the spine as the object whose boundary it is. Cross-ref only; canonical home stays M1.
2. **`#disc-separability-pattern` ← spine cross-ref (low).** It already cross-refs M1 ("positive-half complement"); add the parallel line: it is the *scope-of-existence* facet of the certificate (where the certificate ≻ 0). Cross-ref only.
3. **`#disc-additive-coordinate-forcing` ← spine cross-ref (low).** Its "(PI)/Čencov forces Fisher" content *is* the spine's forced-identity facet; add a cross-reference framing it as such. Cross-ref only; the Čencov machinery's canonical home stays M3.
4. **`#result-sector-persistence-template` / `#result-contraction-template` ← interior-facet Discussion line (low-medium).** One Discussion sentence: the template's contraction condition is the certificate-interior; cross-ref the spine for the cone-geometry reading. No formal change.
5. **`#form-composition-closure` ← projection-defect Discussion line (low-medium).** It already carries the Mori–Zwanzig Working Note; add a Discussion line framing ε* as the certificate's projection-defect and Liberzon as "no common certificate," cross-ref the spine.
6. **O-BP10 segment-surfacing (the keystone; Joseph's call).** L1 is the surfacing — but whether O-BP10 becomes its own named segment / slogan-segment, or is absorbed as the spine's headline, is a framing decision. Recommend: the spine *is* O-BP10's segment-level home (the slogan is the spine's one-sentence summary, the equivalence is L1). The PROPOSALS Bundle-1 O-BP10 entry then points here. Flag for Joseph; do not auto-rewrite Bundle 1.
7. **OUTLINE preamble reframe (highest commitment; Joseph's call).** Line 17 currently: "Three meta-segments form AAD's cross-sectional structure: #disc-separability-pattern … #disc-identifiability-floor … #disc-additive-coordinate-forcing …". The spine would make this "One object — the stability certificate — with the three meta-segments as its facets." This is the auditor-visible framing change and the biggest framework-voice commitment. **Propose the exact replacement text in Working Notes; do not execute in the segment-landing pass.** Joseph confirms the preamble reframe separately, having seen the segment land first.

Steps 1–5 are cross-reference-only and safe to land alongside the segment in a follow pass. Steps 6–7 are framework-voice keystones gated on Joseph. The segment stands on its own without 6–7; it just isn't yet *surfaced* as the spine in the auditor-facing preamble until 7.
