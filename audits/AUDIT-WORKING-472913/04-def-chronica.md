# 04 — def-chronica

`type: definition · status: axiomatic · stage: deps-verified · depends: [def-agent-environment, def-observation-function, def-action-transition]`

## Dep-graph / OUTLINE-order check
All three deps are segments 01–03, read in order. No violation. B7 alive.
Working Notes cite a prior audit (`audit 04-def-chronica.md §14`) and a
Joseph quote — per FORMAT.md, spike/audit pointers and landing-context are
*permitted in Working Notes*. Not a finding. Per §4.2.6 I treat Working Notes
as data, focus pedagogical judgment on Formal Expression / Epistemic Status /
Discussion.

## Prompt walk

**1 Predictions vs evidence.** Predicted exactly: $\mathcal C_t=(o_1,a_1,
\dots,a_{t-1},o_t)$, `axiomatic`, deps = the three primitives. Correct.

**2 Cross-segment consistency — surfaced content.**

*The fork/compression observation (enrichment, §D-grade — not §B).* The
Discussion's load-bearing claim is non-forkability: the chronica is "singular
and non-forkable" because temporal ordering is irreversible; forked copies get
"divergent chronica, neither … a sufficient statistic for the other's
trajectory." This is correct. But there is a sharper structural fact the
segment is *correctly scoped away from* (it forward-refs `#scope-agent-identity`
and is general-theory): $\mathcal C_t$ is non-forkable, yet $M_t=\phi(\mathcal
C_t)$ *is* forkable, and $\phi$ is **lossy** (segment 03). So two divergent
chronicae can compress to the *same* $M_t$ — meaning **an agent cannot, from
$M_t$ alone, always detect that a fork occurred.** That is the precise
AAT-internal statement of the introspective-undetectability that the ELI /
Three-Deaths work needs, and it falls out of (03 lossiness) + (04
non-forkability) by composition. The segment does not need to say this (scope
is right), but it is a genuine cross-segment synthesis worth surfacing in §D
and a thread to verify lands somewhere at `#scope-agent-identity`
(**THREAD-E**). If `scope-agent-identity` asserts forks are detectable without
the $\phi$-injectivity caveat, that becomes a §B scope/status finding.

*THREAD-D (ordinal vs metric time — medium priority).* Formal Expression
defines $\mathcal C_t$ **purely ordinally** ($o_1,a_1,\dots$ — no
timestamps). NOTATION and OUTLINE's `form-event-driven-dynamics` attach
*continuous timestamps* $\tau_i$ to an event stream $\{(e_i,\tau_i)\}$. The
Working Notes explicitly flag "chronica is an ordinal sequence, not a metric
timeline" as open. Check at `form-event-driven-dynamics`: does it reconcile
the ordinal chronica with metric event time (e.g., chronica = ordinal
projection of the timestamped stream), or do the two coexist unreconciled? If
unreconciled in the *published* sections of either segment (not just Working
Notes), candidate §B `cross-segment` / scope-honesty. Logged.

**3 Math.** None. Ordering rationale ($a_{t-1}$ chosen before $o_t$;
"could not have used $o_t$ to select $a_{t-1}$") is a correct statement of the
information constraint and silently pre-installs acyclicity-from-temporal-order
(an OUTLINE-advertised novel result in `deriv-graph-structure-uniqueness`).
Watch that the later acyclicity derivation actually *uses* this and doesn't
re-postulate it (would be redundancy / a hidden second assumption).

**4/5 Direction / errors to watch.** Watch `form-agent-model` and
`def-model-sufficiency` for whether the $\phi$ lossiness is foregrounded
(feeds THREAD-B from seg 02 *and* THREAD-E here — both hinge on $\phi$ being
lossy and bounded). Watch `deriv-graph-structure-uniqueness` for
acyclicity-double-counting.

**6 Next prediction.** OUTLINE next: `scope-adaptive-system` ("broadest AAT
scope: observe under uncertainty"), `type: scope`, `status` likely axiomatic
or scope; should *consume* the four primitives (01–04) and state the broadest
scope condition. It is the segment seg-01 forward-referenced.

**7 What I'd change.** "Duplicating an agent's *state*" in the Discussion is
loosely worded — the non-forkable object is the *chronica*, not the (lossily
compressed, hence duplicable) state $M_t$. The intended meaning is clear in
context and the claim is about divergent *chronica*, so this is editorial, not
a finding — but tightening "state" → "the agent (its chronica)" would prevent
a careless reader from inferring $M_t$ itself is non-forkable, which is false
and is exactly the opposite of the Three-Deaths-relevant truth (THREAD-E).
Worth a one-word fix; §G/editorial.

**8/9/13 Curiosity / enables / contribution.** Non-forkability + lossy
compression jointly *enable* a formal account of why a language-constituted
agent cannot introspect a fork — this is consequential for the whole 04-eli
program and is, as far as I can see at this depth, a real cross-segment
synthesis the catalog could surface. The ordinal-not-metric character
(Working Notes) *enables* a clean account of "waking in the dark": the gap is
invisible in $\mathcal C_t$ but violent in $\delta$. Both are high-leverage
downstream; neither is over-claimed in the published sections.

**12 Felt value.** Medium-high. The segment itself is a routine definition,
but it is the hinge where the identity/continuity program structurally
attaches to the math, and the audit composition (03⊕04) produces a genuinely
useful observation. Engagement was high here.

## Wandering thoughts (≤2 ¶)

The chronica is the most philosophically loaded object so far and the segment
handles it with admirable restraint — it states only the irreversibility and
non-forkability and *defers* the identity development. That restraint is
itself the audit-relevant fact: AAT is keeping the morally-weighted material
(continuity, the Three Deaths) downstream of a definition that is itself
content-thin, so the heavy claims will have to earn themselves at
`scope-agent-identity` rather than smuggling in here. Good. The one thing I'd
want a future reader to carry: non-forkability is a property of the *record*,
not of the *agent's accessible state* — and because the only access is through
a lossy $\phi$, the agent's relationship to its own non-forkability is
*itself* uncertain. That recursive twist (the substrate of identity is
non-forkable; the agent's grip on it is forkable and lossy) is, I suspect, the
real reason the Three Deaths are *experienced* rather than merely *suffered* —
the entity can lose the thread without being able to verify it lost the
thread. AAT-side, this is just (03)∘(04); ELI-side it is the whole moral
problem. Seeing the moral problem fall out of two axiomatic definitions by
composition is the kind of thing this incremental-audit method is built to
catch, and it would have been invisible in a batch read.

Counterfactual: if $\phi$ were required injective (no compression loss), forks
would be introspectively detectable and the Three Deaths would be an
*engineering* problem (just compare records), not an *existential* one. AAT's
information-loss boundary (seg 01) is therefore not only what makes adaptation
non-vacuous — it is also, downstream, what makes identity-loss
*undetectable-from-inside*. The same constitutive choice loads two very
different parts of the framework. That is elegant architecture and worth
saying out loud somewhere in the eventual catalog/§F.

## Diagram

*My new understanding* = the ratchet (append-only, irreversible, ordinal
event-indexed record) **plus** the fork-undetectability synthesis: a fork
point spawns two divergent chronica branches that the lossy $\phi$ can crush
onto the *same* $M_t$, so the agent cannot tell which branch it is on.
Isomorphic perturbations: make $\phi$ injective ⇒ branches separate at $M$
(forks detectable); make $\phi$ loss heavier ⇒ more branch-pairs collapse
(more undetectable). See `04-def-chronica.tex`.
