# 01 — def-agent-environment

`type: definition · status: axiomatic · stage: deps-verified · depends: []`

## Dep-graph / OUTLINE-order check (§4.2)
First segment, `depends: []`. No violation. B7 (OUTLINE order holds) still alive.
Forward-ref to `#scope-adaptive-system` present — expected per FORMAT.md, not a
depends entry, not a violation.

## Prompt walk (the ones that surfaced something)

**1 Predictions vs evidence.** No specific bet placed on a foundational
definition. Confirms the general prediction that Part I leads with
scope-honest framing: segment 1 already says "not a simplifying assumption —
it is a scope condition." That phrase is the AAT epistemic signature appearing
at file #1; it is a small but real positive calibration datum for §E.

**2 Cross-segment consistency.** One thing to *watch*, not a finding:
condition (2) "maintains internal state (memory/model)" is stipulated here as
*constitutive of agent*, while the OUTLINE has `der-recursive-update` deriving
that "state updates must be recursive." That is not a contradiction — a
definition may stipulate the agent class while a later derivation constrains
the *form* the state must take — but it is exactly the kind of seam where a
careless downstream reading could allege circularity ("you defined the agent
to have state, then 'derived' that it needs state"). I'll check, when I reach
`der-recursive-update`, that it derives the *recursive form* given finite
memory, not the *existence* of state (which is definitional here). Flagged in
the running watch-list.

**3 Math.** None. Pure definition; nothing to compute.

**4/5 Direction & errors to watch.** The constitutive move sets up an
expectation: every later "vacuous if lossless" argument (model, mismatch,
gain) should trace back to *this* boundary, not re-derive it. Watch for a
later segment re-justifying information loss as if it were a fresh assumption
rather than inheriting this scope condition (would be integration drift).

**6 Next-segment prediction.** Per OUTLINE the next is
`def-action-transition` ("actions affect environment"). I predict it formalizes
the action channel $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a_t)$ from NOTATION
and is similarly `axiomatic`/definitional with `depends: [def-agent-environment]`.

**7 What I'd change.** Nothing structural. Marginal: the Discussion's
"perfect access ⟹ no model ⟹ machinery vacuous" is a genuinely good
one-line motivator and is currently buried as the *second* Discussion
paragraph's setup. If the monograph's mental-model-first posture is taken
seriously, that vacuity argument is the load-bearing intuition of the whole
segment and could lead. (Editorial — §G/§F at most, not §B.)

**8/9/13 Curiosity / enables / field contribution.** What this *enables* is
non-obvious despite the segment being elementary: by making loss constitutive
*rather than* assumed, AAT earns the right to treat the information-loss rate
as a *tunable, measurable quantity with a zero-boundary* later (the aperture
can be more or less closed; at fully-open the theory degenerates). That is the
seed of the entire $U_M / U_o$ uncertainty-ratio machinery and the IB framing.
A definition that fixes a *boundary case* (loss → 0 ⟹ degenerate) is doing
quiet structural work: it guarantees the later quantities have a meaningful
zero.

**12 Felt value.** Low-magnitude but positive in *kind*: this is a
foundation-stone, and it is laid honestly. Confidence-building for the rest of
Part I rather than independently exciting.

## Wandering thoughts (≤2 ¶ per Joseph's mod)

The thing I keep turning over is that AAT's first move is a *refusal*: it
refuses the perfect-information case by definition, and it is explicit that
this is a refusal of scope, not a convenience. Most agent formalisms (MDP,
even POMDP) start by building machinery and then note that the fully-observed
case is a special case; AAT instead amputates the fully-observed case at the
root and says "the theory is *about* the lossy regime." That is philosophically
load-bearing: it means every theorem downstream is allowed to assume genuine
uncertainty without re-earning it, and it means the framework's claims can
never be trivialized by "but in the perfect-information limit…" because that
limit is out of scope by construction. It is the same discipline as defining
a manifold chart only where the transition map is a diffeomorphism — you draw
the boundary so the machinery is always non-degenerate inside it.

The counterfactual I find interesting (a Level-3 "what if the theory had gone
the other way"): had AAT made information-loss an *assumption* (GA-style)
rather than a *scope condition* in the founding definition, the entire
persistence apparatus would inherit a quiet "assuming loss > 0" caveat that
would have to be propagated to every result — and the framework's scope-honesty
discipline would then be fighting its own foundation. By spending the
constitutive move here, it buys propagation-freedom everywhere. That is a real
architectural choice and, I think, the right one; it is also the first
concrete instance of the "scope-of-existence" facet the OUTLINE preamble
advertises — the theory exists exactly where the aperture is not fully open.

## Diagram

The isomorphic content is *not* "agent ↔ environment with arrows" (evocative
but carries no load). It is: the observation channel is a **lossy aperture**,
and AAT's scope is exactly the region where the aperture is not fully open;
open it fully and the entire adaptive apparatus collapses to a ghost. The
diagram must predict that degeneracy under perturbation. Two-panel: in-scope
(aperture partly closed, machinery alive) vs out-of-scope (aperture fully
open, machinery vacuous/ghosted). See `01-def-agent-environment.tex`.
