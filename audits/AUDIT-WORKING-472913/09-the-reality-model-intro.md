# 09 — the-reality-model-intro  *(no finding; §E exemplar; THREAD-B advance)*

`type: discussion · status: discussion-grade · stage: draft · depends: [def-chronica, scope-adaptive-system, def-agent-environment]`

## Dep-graph / DETECTOR / OUTLINE-order
Deps = 04, 05, 01 (upstream). **DETECTOR clean:** no `## Formal Expression`,
no `*[Derived]*` tag; forward `#`-refs (`#form-agent-model`,
`#form-information-bottleneck`, `#def-model-sufficiency`,
`#def-model-class-fitness`) are *prose previews of the next four segments* —
the legitimate forward-reference pattern. B7 alive. Prediction (seg 08)
confirmed exactly: bridge/discussion, thin deps, no forward-`*[Derived]*`.

## §E positive exemplar (calibration — weigh against F2)

This segment is the **correct** way to forward-reference, and saying so
sharpens F2 further: "*The trigger lives in this chapter; the consequence
unfolds in Chapter 4*" — a preview *in prose*, explicitly deferred, no
derivation tag. It also does mental-model-first pedagogy (intuition before
formalism: "an agent navigating uncertainty cannot see the world directly")
and honest prior-art adoption ("Tishby's information bottleneck … we adopt
that framing directly" — integration-not-invention, no novelty overclaim).
Three CLAUDE.md disciplines (forward-ref hygiene, respectful pedagogy,
prior-art integration) all demonstrated correctly in one bridge segment. The
framework's *standard* is high; F1/F2/F3 are deviations from it, not its
nature — important for reader weighting given my heavy priming.

## THREAD-B advance (boundedness)

Seg-02 THREAD-B worried the bounded/compressed nature of $M_t$ (vs unbounded
$\Omega$) makes the agent-side Markov-by-completeness move *not* cost-free,
and asked whether `form-agent-model`/`def-model-sufficiency` re-surface that
cost. This intro **foregrounds the boundedness explicitly**: "Carrying that
history in raw form is infeasible … finite agents compress"; "anything not in
$M_t$ is lost to the agent, by construction." Partially reassuring — the cost
(loss by compression) is named at the chapter gate. The real THREAD-B test is
now sharply localized: does `#form-agent-model` (next) carry the *completeness
commitment's cost* (that the bounded $M_t$ cannot in general Markovianize an
arbitrary history without residual loss), and does `#def-model-sufficiency`
quantify exactly that residual? THREAD-B updated: "intro foregrounds
boundedness; cost-carry verification moves to seg 10–13."

## Prompt walk (light segment — proportionate)

**2 Cross-segment.** Consistent with 01 (loss constitutive), 04 (chronica as
sole raw material), 05 (scope). The "low class-fitness ⇒ change class not
parameters" seed is previewed honestly as a Ch.4 consequence — I'll hold it
to its derivation at `#result-structural-adaptation-necessity`
(`#def-model-class-fitness` is in the inevitability-core per FORMAT.md, so
the bar there is mathematical inevitability — flagged for that segment).
THREAD-D (ordinal vs metric chronica) not touched here; still open,
consistent.

**3 Math.** None (no formal claim — its Working Notes say so explicitly; the
`discussion-grade`/no-Formal-Expression status is honest).

**6 Next prediction.** OUTLINE next: `#form-agent-model` — `type:
formulation` (per FORMAT.md it is in the *canonical-formulations ring*, not
inevitability-core: "$M_t=\phi(\mathcal C_t)$ … most definitions" are
formulation choices). Predict: commits $M_t=\phi(\mathcal C_t)$ +
completeness assumption; `status` ~ axiomatic/formulation; deps =
def-chronica (+ maybe form-information-bottleneck forward). **Key THREAD-B
test:** does it state completeness as a *modeling commitment with a named
residual cost* (consistent with seg-02's `def-action-transition`
characterization of the parallel move) or as cost-free? That determines
whether THREAD-B becomes a finding or dissolves.

**7 What I'd change.** Nothing. This is a model bridge segment; if anything
it is the template the *other* chapter-intros (and F2's segment) should match.

**12 Felt value.** Moderate — low as standalone content (it asserts nothing),
high as *calibration*: it is the cleanest demonstration yet of the in-corpus
standard, and it tightens the THREAD-B test to two specific upcoming segments.

## Wandering thoughts (≤2 ¶)

The chapter-intro segments are turning out to be the audit's calibration
instruments more than its finding sources, and that is itself a finding about
*method*: in a framework with priming-heavy framing prose, the bridge
segments are where the framework states its *aspirations* (mental-model-first,
honest deferral, integration-not-invention), and the derivation/postulate
segments are where it either meets or misses them. Reading an intro right
before the segments it previews sets up a clean predictions-vs-evidence test
for the next four files at once — the intro *is* the framework handing me its
own falsifiable promissory note for the chapter, which is exactly the
inverted-priming stance from 00-initial-predictions §0, now operating at
chapter granularity rather than whole-framework granularity. I'll treat every
chapter-intro this way: not as audit-target but as the chapter's promissory
note to grade the chapter against.

The substantive thing I'm now most curious about is whether the
"low-ceiling ⇒ change class not parameters" seed is *genuinely* the trigger
for an inevitability-core result (structural-adaptation-necessity) or whether
the inevitability is softer than the intro's confident "central result"
framing. The intro is allowed to be confident (it's framing), but it has
written a promissory note ("the mismatch floor that parametric updates cannot
get below is set by this ceiling") that `#result-structural-adaptation-necessity`
and `#def-model-class-fitness` must actually pay in inevitability-grade math,
because FORMAT.md itself lists those in the inevitability core. That is the
sharpest chapter-level prediction I can make and I've logged it. If the
ceiling argument turns out to be robust-qualitative rather than exact, the
intro's "one of the framework's central results" is an overclaim — but I will
not pre-judge; the test is the derivation, two-to-four segments out.

## Diagram

Two-layer vertical. **Anchor:** image-compression — a scene compressed within
a *class* (limited palette): tuning the quality slider (parametric) improves
the instance but hits a ceiling $\mathcal F<1$ the class cannot exceed;
only switching representation class (truecolor) raises the ceiling.
Isomorphic: $S$ = fraction of scene surviving; $\mathcal F$ = best achievable
*in this class*; low $\mathcal F$ ⇒ change class not parameters (perturb:
lower the class ceiling ⇒ slider cannot reach $S{=}1$ ⇒ must switch — exactly
structural-adaptation-necessity). **Skeleton:** the pipeline
$\mathcal C_t \xrightarrow{\phi} M_t$, the $S$ gauge, the $\mathcal F$
ceiling, and a **dashed "previewed → derived in Ch.4" arrow** — drawn in the
*legitimate forward-ref grammar* and explicitly captioned "compare F2: this
is how a forward-reference should look (preview, not derive)." The diagram
doubles as an F2 calibration instrument. See `09-the-reality-model-intro.tex`.
