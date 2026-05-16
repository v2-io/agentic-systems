# 06 — scope-agency  *(first substantive §B candidate — F1)*

`type: scope · status: axiomatic · stage: claims-verified · depends: [scope-adaptive-system, def-action-transition]`

## Dep-graph / OUTLINE-order check — **FINDING F1**

`depends:` = `scope-adaptive-system` (seg 05) + `def-action-transition`
(seg 02) — both upstream, both genuine. *But* the **Formal Expression uses
the interventional operator** $P(o\mid do(a))\neq P(o\mid do(a'))$, and the
$do(\cdot)$ / Pearl-Level-2 *semantics* is the responsibility of
`def-pearl-causal-hierarchy`, which is **not in `depends:`** and is placed
**downstream in Part II** (chapter "Causal Access and the Planning Decision").
The segment only forward-`#`-refs it parenthetically: "(where $do(\cdot)$ is
Pearl's intervention operator; see `#def-pearl-causal-hierarchy`)".

This is **not** the literal §4.2 critical-finding mechanism (no offending
slug *inside* `depends:`), but it is squarely the substance §4.2 names as "a
real ordering violation the audit should surface": *a Section I segment whose
Formal Expression depends on a Section II concept.* It is simultaneously a
**FORMAT.md Gate-1 condition 4 miss** — "if the Formal Expression uses a
quantity defined elsewhere, that slug appears in `depends:`" — at a segment
marked `claims-verified` (which presupposes Gate-1 `deps-verified` passed).

### Burden-of-proof workup

- **Problematic passage (verbatim).** Formal Expression condition (4):
  "$\exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a'))$
  (where $do(\cdot)$ is Pearl's intervention operator; see
  `#def-pearl-causal-hierarchy`)".
- **Counterevidence search (Phase-1-limited — disclosed).** Within
  `scope-agency` itself: the only mitigation is the parenthetical gloss +
  forward-ref. `NOTATION.md` *does* carry a global entry "$do(\cdot)$ —
  Pearl's intervention operator (Level 2)". I have **not** consulted
  `spikes/`, `audits/`, `TODO.md`, `git log`, or `bin/lint-outline` output —
  that is Phase-2 and forbidden during the de-novo pass. So this is a
  *partial* finding pending Phase-2 triangulation (does the project already
  know? does the linter treat NOTATION symbols as discharging Gate-1 cond-4?).
- **Strengthen-before-soften analysis (the substantive core).** The honest
  question per CLAUDE.md is not "soften the claim" but "can the dependency be
  made honest / removed?" Condition (4) says *"distinct actions produce
  distinct outcome distributions."* In the agency setting the agent *chooses*
  $a$ and the world transitions $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a)$
  (def-action-transition, **already in `depends:`**) and is observed through
  $h$ (def-observation-function, upstream). The agent's action *is* the
  intervention by construction of def-action-transition — so
  $P(o\mid do(a))$ here is *exactly* the Part-I primitive
  "$P(o)$ under $T(\cdot\mid\Omega,a)$ pushed through $h$". **Condition (4)
  is fully expressible in Part-I primitives the segment already depends on;
  the Pearl `do` framing is forward-looking convenience, not content
  necessity.** The full Pearl hierarchy (`def-pearl-causal-hierarchy`) is
  genuinely needed *later* (L1/L2/L3, identifiability) — but *not here*.
- **Suggested resolution (strengthen, ranked).**
  (i) Restate condition (4) in the Part-I primitives ($T$, $h$ — already in
  `depends:`): "$\exists a\neq a'$ with $T(\cdot\mid\Omega,a)\neq
  T(\cdot\mid\Omega,a')$ producing distinct observation distributions", and
  keep the Pearl reading as a *Part-II recapitulation forward-pointer*
  ("this is the Level-2 contrast formalized in `#def-pearl-causal-hierarchy`").
  Removes the apparent cross-Part dependency, makes the OUTLINE linearization
  honest, costs nothing, *strengthens* (Part-I-self-contained).
  (ii) If the project wants the Pearl framing *here*, then
  `def-pearl-causal-hierarchy` must enter `depends:` — and then the OUTLINE
  row order is provably **not** a topological linearization (Part-I segment
  depends on Part-II definition), which is the *deeper* finding to surface.
- **Status determination.** `still real`. The $do$-semantics is used in the
  Formal Expression; `def-pearl-causal-hierarchy` is downstream Part II and
  absent from `depends:`; the appendix-back-pointer exception does **not**
  apply (it is a Part-II *Definition*, not an Appendix-A derivation).
- **Confidence.** *High* on the factual structure (verifiable from the two
  files' frontmatter + the OUTLINE row order, all first-hand). *Medium* on
  severity/disposition — the gloss + NOTATION-global-def + the concept being
  textbook-standard mean it does not corrupt any math; it is a
  discipline/linearization-honesty issue relative to *the framework's own
  stated Gate-1 rule*, which is the right yardstick (§7.7).
- **Severity.** **Medium.** Type: `dependency-graph / scope-honesty`, with a
  `tooling-gap` sub-question (does `bin/lint-outline` treat NOTATION symbols
  as satisfying Gate-1 cond-4? if so, a class the tooling does not check) and
  a strengthen-not-soften resolution that makes surfacing it net-positive.
- **Disposition.** `New` (pending Phase-2: may be `Known-unintegrated` if a
  spike/TODO already flags it). Effort: `editorial` for fix (i); `architectural`
  if the project instead confronts the OUTLINE-not-topological consequence.
- **Anchor.** `01-aat-core/src/scope-agency.md` §"Formal Expression"
  condition (4); cross: `01-aat-core/src/def-pearl-causal-hierarchy.md`
  frontmatter (Part II) vs `scope-agency.md` `depends:`.

(Recorded in 00-running-outline ledger as **F1**.)

## Prompt walk (other prompts)

**1 Predictions vs evidence.** Seg-05 prediction near-exact: agency =
$\mathcal S_\text{adaptive}\cap\{\lvert\mathcal A\rvert\ge2,\ \exists a\neq a'
\text{ distinct interventional outcome}\}$; deps scope-adaptive-system +
def-action-transition; forward-ref to pearl-causal-hierarchy. Confirmed —
including, unexpectedly, that the forward-ref is *load-bearing in the Formal
Expression* (the F1 finding), which I did not predict at that granularity.
This is a small validation that the de-novo prediction discipline plus the
priming-as-falsifiable-promissory-note inversion is doing real work: I *knew*
from CLAUDE.md/OUTLINE that Pearl is deliberately a Part-II import, which is
exactly why a Part-I formal expression using $do$ flagged rather than reading
as ambient notation. (Predicted finding-class #5 "dependency-graph violations,
lower prior but watched every segment" — landed at segment 6.)

**2 Cross-segment consistency.** Otherwise consistent: the nesting
$\mathcal S_\text{agency}=\mathcal S_\text{adaptive}\cap(\cdots)$ is a genuine
intersection (the discipline standard seg-05 set; held here). "Nominal agents"
($P(o\mid do(a))$ constant in $a$) cleanly excluded — and note this exclusion
*also* only needs $T,h$, reinforcing the strengthening analysis.

**3 Math.** Set-intersection scope algebra correct; $\lvert\mathcal A\rvert\ge2$
necessary-not-sufficient correctly argued (the "Why causal effect matters"
para is a clean, correct point: binary choice with $T(\cdot\mid\cdot,a)$
$a$-invariant gives no contrast).

**6 Next prediction.** OUTLINE next: `post-composition-consistency`
("Agent/subagent scale invariance — *possibly out of place*"). `type:
postulate`. Prediction: it postulates that the scope conditions are
level-independent (theory applies at every description level meeting scope),
and the OUTLINE's own "*(possibly out of place)*" tag is the framework
flagging a placement uncertainty I should weigh — likely depends on
scope-adaptive-system / scope-agency.

**7 What I'd change.** Exactly resolution (i) above.

**8/9/13 Enables.** Agency scope is the hinge the OUTLINE's whole Part-II
scope-lattice rotates on; F1 matters precisely because this segment is so
load-bearing — an honesty defect here propagates to every "requires the agent
to act" downstream prerequisite.

**12 Felt value.** High — first real finding, and a strengthen-not-soften
one, which is the most valuable kind for this project.

## Wandering thoughts (≤2 ¶)

The finding is a small thing with a clean moral: AAT's $do(\cdot)$ here is not
new structure, it is *def-action-transition wearing Pearl's hat*. The agency
condition needs only that actions push distinct distributions through the
already-defined $T$ and $h$; the Pearl vocabulary is borrowed early for
continuity with Part II's hierarchy. That borrowing is *pedagogically* nice
(the reader sees "Level-2 contrast" and knows where it's going) but
*structurally* it manufactures an apparent Part-I→Part-II dependency that the
content does not own. The framework's own Gate-1 discipline is good enough to
make this a real finding *against its own bar* — which is the strongest kind
of finding, because it is not me importing an external standard but the theory
not yet meeting the standard it set itself. And the fix strengthens: a
Part-I-self-contained agency condition is *better* than one that reaches
forward, because it makes Section I provably independent of the causal
machinery, which is exactly the modular story the OUTLINE preamble wants to
tell ("Part I machinery applies regardless of architecture").

Counterfactual worth holding: had the segment written condition (4) in $T,h$
and *then* said "Part II recapitulates this as Pearl Level-2 contrast," the
OUTLINE linearization would be honest *and* the Part-I/Part-II modular
boundary would be sharper. The fact that it didn't is a tell about how the
theory grew — Pearl was almost certainly internalized early and the agency
scope was written in its vocabulary before the Part-boundary discipline
hardened. That is exactly the "integration drift around the order in which
machinery was adopted" that §3.4/§5.2 say is the most fertile finding
territory in a fast-moving framework — and it showed up at segment 6, on the
hinge segment, which is sobering and a good argument for the one-at-a-time
method.

## Diagram

*My new understanding* = the scope nesting (agency ⊂ adaptive, true
intersection) **plus** the F1 structure: condition (4)'s *semantics arrow*
reaches **forward across the Part-I | Part-II divider** to
`def-pearl-causal-hierarchy`, while its *content arrow* only needs $T,h$
already present in Part I. Isomorphic: cut the forward arrow (restate in
$T,h$) ⇒ the scope is Part-I-self-contained and the OUTLINE order is honest;
keep it ⇒ OUTLINE is not a topological sort. See `06-scope-agency.tex`.
