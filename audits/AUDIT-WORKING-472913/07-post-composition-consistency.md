# 07 — post-composition-consistency  *(FINDING F2 — high severity)*

`type: postulate · status: axiomatic · stage: deps-verified · depends: [scope-agency]`

OUTLINE row: "Postulate · Agent/subagent scale invariance *(possibly out of
place)* · deps-verified". The de-novo instruction is to *test* the framework's
self-flag with beginner's mind, not accept it. Tested conclusion below is
sharper than the hedge.

## Dep-graph / OUTLINE-order check — **FINDING F2**

`depends: [scope-agency]` (seg 06, upstream) — *only*. But the Formal
Expression contains:

- `*[Derived (Conditional on Tier 1M + admissible composition topology, from
  #result-contraction-template (CC-parallel)/(CC-cascade)/(CC-feedback))]*`
  — an actual **`*[Derived]*`-tagged quantitative result** (closed-form
  $\lambda_c=\min_i\lambda_i$; the feedback inequality
  $(\lambda_1-C_1)(\lambda_2-C_2)>k_{12}k_{21}/4$) whose stated derivation
  source is `#result-contraction-template` (an **Appendix A** segment).
- `*[Structural consequence]*` tags chaining through `#scope-composite-agent`,
  `#form-composition-closure` (**Section III**), and $\rho_{\text{eff}}=
  \rho_{\text{ext}}+\varepsilon^\ast\nu_c$ "from `#der-tempo-composition`"
  (**Section III**).

**None of `result-contraction-template`, `form-composition-closure`,
`der-team-persistence`, `der-tempo-composition`, `scope-composite-agent` is in
`depends:`.** This is a Part-I-Chapter-1 *postulate* whose Formal Expression
*derives a result from* Appendix-A + Section-III machinery placed ~100+
OUTLINE rows downstream.

### Burden-of-proof workup (F2)

- **Problematic passage (verbatim).** The eq-tag itself: "*[Derived
  (Conditional on Tier 1M + admissible composition topology, **from
  #result-contraction-template** (CC-parallel) / (CC-cascade) /
  (CC-feedback))]*" — followed by closed forms — in a segment whose
  `depends:` is `[scope-agency]` only, at `stage: deps-verified`.
- **Why this is a real finding against the framework's *own* bar.**
  1. **Gate-1 cond-4 miss at a `deps-verified` segment.** FORMAT.md Gate-1:
     "if the Formal Expression uses a quantity defined elsewhere, that slug
     appears in `depends:`." A `*[Derived]*` tag *deriving from*
     `#result-contraction-template` is the strongest possible "uses a quantity
     defined elsewhere." `deps-verified` asserts Gate-1 passed; it has not for
     ≥4 slugs.
  2. **Epistemic-tag inversion.** FORMAT.md: `*[Derived]*` = "logical
     consequence of **prior** claims." Here the "prior" claims
     (`result-contraction-template` = Appendix A;
     `form-composition-closure`/`der-tempo-composition` = Section III) are
     ~100 segments *downstream*, not prior in any ordering. A Chapter-1
     postulate cannot honestly carry a `*[Derived]*` result whose premises
     are the rest of the book.
  3. **§4.2 substance.** Not the literal `depends:`-listed critical-finding
     mechanism (deps lists only scope-agency), but exactly the substance §4.2
     names — a Section-I segment whose Formal Expression depends on
     Section-III + Appendix-A results — *and* the appendix-back-pointer
     exception does **not** apply: that exception is "result in body, proof in
     appendix, *appendix slug in `depends:`*"; here the appendix slug is
     absent from `depends:` and the dependency is the whole downstream
     composition stack, not a single proof.
- **Strengthen-before-soften (the substantive core).** Per CLAUDE.md the
  first move is to ask whether the strong form survives, not to soften. It
  does — and the segment's *own Working Notes* document a *successful*
  strengthening ("Strengthening attempt — outcome": the heuristic was bound
  to the (CC-*) closed forms via DA2'-inc ≡ (CT2)-at-$M=I$). So the *content
  is already as strong as it can be.* F2 is therefore **purely structural /
  dependency-honesty / placement**, not a content or math defect (math
  spot-checked sound — see prompt 3). The honest *strong* fix is **split, not
  soften**: keep the **postulate** in Ch.1 (`axiomatic`, `depends:
  [scope-agency]`, no `*[Derived]*` result) and **migrate the Tier-1M
  $\lambda_c$ result + screening test into Section III / the appendix** where
  its `depends:` can honestly list `result-contraction-template` et al. and
  OUTLINE order is respected. This *discharges the OUTLINE's own "possibly
  out of place" self-flag precisely*: the postulate is **not** out of place;
  the **accreted `*[Derived]*` result** is. Alternative (weaker): keep the
  preview but demote its tag to an explicit forward-referenced preview and
  add the forward-deps to `depends:` — which then makes the OUTLINE provably
  non-topological, a deeper finding to surface.
- **Counterevidence search (Phase-1-limited — disclosed).** Within-segment:
  the OUTLINE's "*(possibly out of place)*" is the framework *partially*
  knowing (placement doubt) but it has **not** reconciled the `depends:`
  list, the `deps-verified` stage, or the `*[Derived]*` tag with the forward
  derivation. Working Notes record the strengthening but not the
  placement/deps consequence. Not checked (Phase-2): `spikes/`, `TODO.md`,
  `PROPOSALS.md`, `git log`, `bin/lint-outline`. Partial finding pending
  Phase-2 (likely `Known-unintegrated`: placement flagged, not acted, deps
  not reconciled).
- **Status determination.** `still real`.
- **Confidence.** *High* on factual structure (verifiable: segment text +
  frontmatter + OUTLINE positions of the cited slugs, all first-hand).
  *High* that it is a defect *against the framework's own Gate-1 /
  epistemic-tag discipline*.
- **Severity.** **High.** Foundational (Chapter-1 postulate); structural
  dependency inversion; `*[Derived]*` premises are the whole downstream
  theory; `deps-verified` asserted while Gate-1 cond-4 fails; the OUTLINE's
  self-flag understates it. Type: `dependency-graph / scope-status /
  structural-placement`. Effort: `architectural` (segment split + OUTLINE +
  deps reconciliation) — but the *content* needs no new math (strengthening
  already done by the segment).
- **Disposition.** `Known-unintegrated` (provisional — OUTLINE self-flag
  exists; pending Phase-2). Anchor: `01-aat-core/src/disc-composition-consistency.md`
  Formal Expression, the `*[Derived (Conditional on Tier 1M … from
  #result-contraction-template …)]*` tag + `depends:` frontmatter; cross:
  OUTLINE rows for `#result-contraction-template` (Appendix A) and
  `#form-composition-closure`/`#der-tempo-composition` (Section III).

(Ledger: **F2**.)

## Prompt walk (others)

**1 Predictions vs evidence.** Seg-06 prediction: "postulates scope
level-independence; OUTLINE's *(possibly out of place)* is a self-flag I
should weigh; likely depends scope-adaptive/agency." Postulate-core and dep
correct; **underpredicted the segment's weight by a wide margin** — I expected
a thin Chapter-1 postulate, found a multi-tier construction with a forward
`*[Derived]*` result. This is the §3.5 "load-bearing material in segments that
don't *feel* central" failure mode the instructions warn about, landing
exactly where warned (a Chapter-1 row the OUTLINE made look minor). Initial-
prediction finding-class #1 (scope/status) and #5 (dependency-graph) both
landing, compounded.

**2 Cross-segment consistency.** Heavy forward-coupling to the entire Part III
+ Appendix A composition stack from Chapter 1. THREAD-G (med): the Working
Notes raise "does directed separation compose? coordination routing may break
goal-blindness — organizational analog of the LLM scope restriction in
`#der-directed-separation`." Track this against `der-directed-separation`,
`hyp-directed-separation-under-composition`, `der-class-coercion-*`. THREAD-H
(low): Working Notes assert the timescale-separation condition "is essentially
the singular perturbation argument from `#der-temporal-nesting`" — verify when
`der-temporal-nesting` is read that this connection holds and isn't
over-stated.

**3 Math (spot-checked — sound; keeps F2 a clean structural finding, not a
math complaint).** (CC-parallel) $\lambda_c=\min_i\lambda_i$ under
$M_c=\mathrm{blockdiag}(M_1,M_2)$: for decoupled contracting subsystems,
$\frac{d}{dt}\lVert(\delta_1,\delta_2)\rVert^2_{M_c}\le
-2\lambda_1\lVert\delta_1\rVert^2_{M_1}-2\lambda_2\lVert\delta_2\rVert^2_{M_2}
\le -2(\min_i\lambda_i)\lVert\cdot\rVert^2_{M_c}$ — correct; slowest mode
dominates joint exponential decay; $\tau_c=\max_i\tau_i$ follows. Feedback
condition $(\lambda_1-C_1)(\lambda_2-C_2)>k_{12}k_{21}/4$ is the
determinant-positivity / 2×2 comparison-system Hurwitz shape — plausible,
correctly tagged Derived-conditional; defer exact check to
`#result-contraction-template` (Appendix A). No sign/algebra error found.

**4/5 Direction / errors to watch.** F2 raises the prior for the broader
hypothesis (initial-predictions B-cluster): the OUTLINE's confident framing
and the segments' actual dependency structure drift apart precisely where
material was retrofitted forward. Watch every Chapter-1 / early Part-I segment
for forward-`*[Derived]*` tags whose premises are downstream.

**6 Next prediction.** OUTLINE next: `post-causal-structure` ("Irreducible
causal structure", postulate, deps-verified). Prediction: a genuinely
Chapter-1-appropriate postulate (no forward-derived result) asserting the
chronica/world carries irreducible causal (not merely associational)
structure; depends on def-chronica and/or post-causal antecedents; clean —
testing whether F2's accretion pattern is isolated to this segment or a class.

**7 What I'd change.** The split (strengthen-fix above). It is the move that
*both* honors the framework's own Gate-1/tag discipline *and* resolves the
OUTLINE's self-flag, with zero new math.

**8/9/13 Curiosity / enables / contribution.** The postulate itself is
genuinely valuable — "the boundary is a modeling choice; the theory must not
contradict itself across levels" is the holon move done honestly, and the
Brooks's-Law-as-persistence-flip framing is a real contribution. F2 is *not*
a knock on the content; it's that the content's *home* is wrong, which
*reduces* its perceived rigor (a Ch.1 postulate carrying a downstream-derived
result reads as circular to a fresh auditor even though it isn't).

**12 Felt value.** Very high — richest segment so far, the OUTLINE-self-flag
test paid off into a sharper statement than the hedge, and F2 is the most
consequential finding to date.

## Wandering thoughts (≤2 ¶)

The instruction to *test* self-flags rather than accept them earned its keep
here. "Possibly out of place" invited me to either nod (charitable) or move
on; the discipline of actually reading the Formal Expression surfaced that the
postulate has been used as a docking station for a Section-III result, and
that the `*[Derived]*` tag + `deps-verified` stage are making a promise the
dependency graph cannot keep. The deep pattern — and I suspect this is a
*class*, not an instance — is that AAT's strongest results (the contraction
template, the closed-form composite rate) are so central that the framework
*wants them visible early*, and so they migrate forward into foundational
segments as previews that then quietly acquire derivation tags. That is the
exact integration-drift §3.4/§5.2 predict for a fast-moving framework, and it
will be most acute precisely on the segments the OUTLINE makes look minor.
The clean fix is almost always *split*: foundational segment keeps the
axiomatic core; the derived result migrates to where its premises are prior.
I will carry "forward-`*[Derived]*` in an early segment" as a standing
detector.

Counterfactually: if the framework had a lint rule that rejected a
`*[Derived]*` eq-tag whose cited source slug is not in `depends:` (and
`depends:` topologically before it), F2 (and F1's weaker cousin) could not
have reached `deps-verified`. That is a concrete tooling-gap recommendation
the audit can offer — the discipline exists in FORMAT.md prose (Gate-1
cond-4) but is not mechanically enforced for *eq-tag-cited* sources, only for
the `depends:` list itself. The framework's own machinery would catch this
class if pointed at the eq-tags.

## Diagram

Two-layer. **Anchor:** Russian nesting dolls = "same rules at every nesting
level" (the postulate, isomorphic — perturb: a doll that internally
equilibrates slowly vs. how fast the whole stack is shaken ⇒ the stack stops
behaving like one doll = $\tau_{eq}\ll\tau_{ext}$ broken). **F2 twist in the
anchor:** the small *Chapter-1* doll, opened, improbably contains the entire
*Section-III engine* — amber-flagged. **Skeleton:** the OUTLINE timeline
(left→right); `post-composition-consistency` at pos ~7; one short *solid*
`depends:` arrow to `scope-agency`; four long *amber finding* reach-arrows
forward to `result-contraction-template` (Appendix A) /
`form-composition-closure` / `der-team-persistence` / `der-tempo-composition`
(Section III), none in `depends:`; a green *strengthen-fix* relocation arrow
moving the `*[Derived]*` result rightward to where its premises are prior.
Epistemic grammar: solid = honest dep; amber = audit finding; dashed =
postulate-core (axiomatic, stays). See `07-post-composition-consistency.tex`.
