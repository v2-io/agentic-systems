# 08 — post-causal-structure  *(FINDING F3 — terminology collision; + sharpens F2/F1)*

`type: postulate · status: axiomatic · stage: deps-verified · depends: [def-agent-environment, def-chronica]`

## Dep-graph / OUTLINE-order check
Deps = 01, 04 (upstream). Forward `#`-refs to `#def-pearl-causal-hierarchy`,
`#def-mismatch-signal`, `#def-causal-information-yield`, `#scope-agency`,
`#scope-adaptive-system` are **Discussion-section only**, not in a Formal
Expression / `*[Derived]*` tag — FORMAT.md explicitly permits forward
`#`-refs in any section. **Not an F1/F2-type finding.** B7 alive.

## F2 / F1 cross-calibration (important — strengthens both prior findings)

Prediction (seg-07): test whether F2's forward-`*[Derived]*` accretion is a
*class* or *isolated*. **Result: `post-causal-structure` is the clean
contrast case.** It is a Chapter-1 postulate with *perfect* dependency &
epistemic hygiene: `axiomatic`, no `*[Derived]*` tag, consequences *previewed*
via legitimate Discussion `#`-refs, Epistemic Status explicitly disclaims
derivation ("AAT does not derive it … simply noted as a precondition"). So
**F2 is an outlier defect, not the framework's house style** — the theory
*can* and usually *does* write Chapter-1 postulates correctly. This
*strengthens* F2 (it deviates from a demonstrated in-corpus standard) and is a
strong **§E positive-calibration** datum.

It also **self-calibrates F1**: here Pearl is forward-referenced in
*Discussion* (legitimate, not flagged); in `scope-agency` (F1) `do(·)` was
used in the *Formal Expression* (flagged). I am correctly scoping F1 to
load-bearing Formal-Expression use, not over-flagging every Pearl
forward-ref. Good discipline check on myself (§3.3 charitable-vs-rigorous
applied to my own findings).

## FINDING F3 — "nominal" denotes opposite scope-membership across segs 06↔08

Reading `scope-agency` (seg 06) two segments ago left "**nominal** = no
interventional contrast = *excluded* from agency, adaptive-only" in my model.
Hitting this segment's coupling spectrum directly collides with it.

- **`scope-agency` (06), verbatim:** "**Nominal agents**
  ($P(o\mid do(a))=P(o\mid do(a'))$ for all $a,a'$): Have choices that make
  no difference. … Same as passive observers for AAT's purposes: adaptive
  only." → *"nominal" ⇒ outside agency.*
- **`post-causal-structure` (08), verbatim:** "**Nominal coupling**
  ($a_t$ negligibly affects $\Omega_{t+1}$, but the agent's *choice of what
  to observe* produces distinguishable observation distributions): …still
  within scope — the agent's query actions generate weak but nonzero
  interventional contrasts. The theory applies." → *"nominal" ⇒ inside
  agency.*
- This segment's **"Zero coupling"** row ("…AND observation distributions are
  action-independent … **Outside the agency scope**") is the category that
  *actually equals* `scope-agency`'s "nominal agents."

So: same word "**nominal**" labels **opposite scope-membership** in two
adjacent foundational scope segments — and the collision sits *exactly on the
agency/adaptive boundary*, the hinge the OUTLINE scope-lattice and F1 both
show is load-bearing for all of Part II. Plus a **within-segment**
inconsistency: this segment's bullet calls the intermediate category
"**Nominal coupling**" but its own later prose calls the same thing
"**query-only coupling**" ("…through weak coupling … to *query-only coupling*
(choosing which question to ask)").

- **Status determination.** `still real` — survives current src text in both
  segments; not a Working-Notes-only caveat.
- **Strengthen-before-soften.** Neither claim is wrong about its spectrum
  point; do not soften either. The fix is purely terminological and the
  better term is *already in this segment's own prose*: rename the bullet
  "Nominal coupling" → "**query-only coupling**" (self-consistent), and either
  keep "Zero coupling" or align `scope-agency`'s "nominal agents" →
  "zero-coupling agents." Resolution is in-text; zero new content.
- **Counterevidence search (Phase-1-limited).** Both segment texts read
  first-hand; collision explicit & verbatim. Not checked: LEXICON entry for a
  canonical "nominal" definition (LEXICON read at orientation had no "nominal"
  agent-class term — so no canonical anchor exists, which makes drift more
  likely, not less), `spikes/`, `git log` (Phase-2).
- **Confidence.** *High* (verbatim cross-quote, first-hand).
- **Severity.** **Medium-Low.** No math wrong; but "nominal" is a
  scope-boundary term at the most load-bearing boundary, and a downstream
  segment or fresh reader citing "nominal scope" could mis-scope. Type:
  `cross-segment-contradiction / doc-rot (terminology)`. Disposition: `New`
  (terminology drift; no LEXICON anchor). Effort: `editorial` (rename in 1–2
  segments; consider a LEXICON entry to prevent recurrence — a `tooling/
  vocabulary-gap` sub-note).
- **Anchor.** `01-aat-core/src/scope-agency.md` §Discussion "Nominal agents";
  `01-aat-core/src/post-causal-structure.md` §Discussion "Nominal coupling" /
  "Zero coupling" / "query-only coupling".

(Ledger: **F3**.)

## Prompt walk (others)

**1 Predictions vs evidence.** Predicted "clean Ch.1 postulate, no
forward-derived result" — exactly right; the *purpose* of the prediction
(class vs isolated test for F2) paid off decisively.

**2 Cross-segment.** F3 above. Also: "causal structure independent of
coupling strength" is consistent with seg-01/05/06 (loss constitutive; scope
geometry) and refines the coupling spectrum cleanly *modulo* the F3 label.
THREAD-F revisit: "Zero coupling … within adaptive scope if they observe
under residual uncertainty" — still set-membership phrasing, no temporal
quantifier; THREAD-F neither resolved nor contradicted here. Logged as
"still open, consistent."

**3 Math.** None (postulate). The $T(\Omega_{t+1}\mid\Omega_t,a_t)=
T(\Omega_{t+1}\mid\Omega_t)\ \forall a_t$ zero-coupling characterization is
correct and is the precise negation of `scope-agency` cond (4) — internal
consistency on the *concept* (only the *label* drifts).

**6 Next prediction.** OUTLINE next: chapter "The Reality Model" intro
(`the-reality-model-intro`, `type: discussion`, `stage: draft`). Prediction:
a chapter-bridge discussion segment (Ch.1 ontology/scope → the compressed
representation $M_t$), "static-but-already-enough-to-fail" framing per the
OUTLINE row; likely thin `depends:`; watch whether a chapter-intro discussion
segment smuggles a forward-`*[Derived]*` (DETECTOR) — predict it does not
(intros are framing, not derivation).

**7 What I'd change.** F3 rename (in-text resolution). Nothing else; this
segment is otherwise a model of how a Ch.1 postulate should read — it is the
yardstick F2 should be held to.

**9/13 Enables.** "Causality = temporal precedence, prior to and weaker than
statistical causality" cleanly *enables* the later Pearl-hierarchy import to
be framed as a *strengthening* of an already-postulated primitive, not a
fresh assumption — same propagation-freedom dividend pattern as segs 01/02/05.
The CIY pointer (action-contingent obs carry Level-2 info; action-independent
carry only Level-1) is the seed of the whole exploration/causal-yield line.

**12 Felt value.** High — not for the postulate (clean, expected) but for
what the cross-read produced: F3, and the F2/F1 calibration that makes the
prior findings sharper and my own discipline checkable.

## Wandering thoughts (≤2 ¶)

The most useful thing this segment did was *not* its own content but its role
as a control. Having a clean Chapter-1 postulate immediately after the
F2 segment is the experimental contrast that converts F2 from "maybe this is
just how AAT writes postulates" into "the framework has a demonstrated
standard and this one segment fell off it." That is only available because
the walk is one-at-a-time and ordered: the control arrived right after the
case. A batch reader holding both at once would likely have averaged them
("postulates here are a bit forward-leaning") and lost the sharpness. The
incremental method is, so far, paying its rent specifically in *calibration* —
not just finding issues but locating the in-corpus standard each issue should
be judged against.

F3 is small but it is the canonical shape of the most common predicted
finding-class (terminology drift at a load-bearing boundary, no LEXICON
anchor). What makes it worth recording rather than waving away: "nominal" is
not decorative prose — it is a *scope predicate* sitting on the exact
agency/adaptive seam that F1 showed the entire Part-II applicability story
rotates on. A theory whose central discipline is scope-honesty cannot afford
its scope vocabulary to denote opposite memberships two segments apart. The
reassuring part is that the repair is already latent in the text ("query-only
coupling"), which is the same signature as F2's repair being latent in its own
Working Notes: AAT keeps *almost* catching these itself. That pattern —
self-repair material present but unintegrated — is, I suspect, going to be the
dominant texture of this audit's findings, and it argues for "integration
debt" over "theory gap" as the framework's actual health diagnosis. Early to
say; logging the hypothesis.

## Diagram

Two-layer, vertical. **Anchor:** an arrow-of-time domino row — A can cause B
only if A precedes B; you can topple forward ($a_{t-1}\to o_t$) but cannot
make a later domino tip an earlier one (can't use $o_t$ to choose $a_{t-1}$);
perturb by reversing the arrow ⇒ the loop collapses (isomorphic to "temporal
ordering is constitutive"). Coupling strength = how hard the push:
strong/weak/query-only/zero as push-strength gradient. **Skeleton:** the
coupling spectrum axis (strong→weak→query-only→zero) with the agency|adaptive
scope boundary marked, and **F3** flagged in amber — the word "nominal"
pinned to *two different points with opposite scope-membership* across
segs 06↔08 — with the teal strengthen-fix ("query-only", already in-text).
See `08-post-causal-structure.tex`.
