# 02 — def-action-transition

`type: definition · status: axiomatic · stage: deps-verified · depends: [def-agent-environment]`

## Dep-graph / OUTLINE-order check
`def-agent-environment` is segment 01, already read in OUTLINE order. No
violation. B7 alive.

## Prompt walk

**1 Predictions vs evidence.** Predicted (in 01's reflection) this would
formalize $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a_t)$, axiomatic, depending on
01. All three correct.

**2 Cross-segment consistency — the live thread (high priority).** This
segment *directly addresses* the circularity worry I flagged on segment 01,
and in doing so sharpens it into a concrete, falsifiable cross-segment check:

> "Markov-of-$M_t$ is forced by *defining $M_t$ as complete*; Markov-of-$\Omega$
> is forced by *defining $\Omega$ as the sufficient state*. … Both are
> modeling commitments about the *breadth* of the named object, not
> structural assumptions about underlying world dynamics."

So by *this segment's own characterization*, the agent-side Markov move
(`#deriv-recursive-update` Constraint C3) is a **modeling commitment**, not a
derived necessity. That is consistent with my initial prediction that at least
one of the recursive-update "three constraints" is closer to a formulation
choice than a forced constraint. **Check to run at `der-recursive-update` /
`deriv-recursive-update`:** is C3 presented there as *derived/forced* or as a
*definitional completeness commitment*? If the derivation segment frames C3 as
forced while this definition segment frames the parallel move as a modeling
commitment, that is a cross-segment status tension (candidate §B,
`scope/status mismatch` flavor). Logged in running watch-list as **THREAD-A**.

**The disanalogy the segment does *not* draw (candidate finding — defer
judgment).** The segment asserts the $\Omega$-side and $M_t$-side moves are
"independent" and parallel ("both … about the breadth of the named object").
But there is an asymmetry it glosses: $\Omega$ is "the totality of state
external to the agent" with *no finiteness assumption* (segment 01), so
Markovianization-by-augmentation of $\Omega$ is genuinely without-loss — you
can always enlarge an unbounded object. $M_t$, by contrast, is a *compressed*
representation $\phi(\mathcal C_t)$ (per NOTATION / OUTLINE `form-agent-model`)
and is *bounded* precisely because segment 01's information-loss boundary is
constitutive. Markov-by-completeness for a *bounded* object is **not** free —
augmenting to recover sufficiency can hit the capacity wall. So the two
commitments are parallel in *form* but asymmetric in *cost*: $\Omega$-side is
WLOG; $M_t$-side has teeth. Calling them "independent … modeling commitments"
flattens that. **THREAD-B** — defer until `form-agent-model`,
`def-model-sufficiency`, `def-model-class-fitness`, `der-recursive-update`,
`deriv-recursive-update` are read; one of those may handle boundedness
explicitly and dissolve this. If none does, this is a real scope-honesty
finding: the agent-side Markov move inherits a boundedness caveat the segment
presents as cost-free.

**3 Math.** $\Omega_{t+1}\sim T(\cdot\mid\Omega_t,a_t)$; deterministic =
point-mass special case — correct. Nothing to compute.

**4/5 Direction / errors to watch.** Watch every later use of "Markov" or
"sufficient state" or "complete history" for whether the boundedness teeth
(THREAD-B) are acknowledged. Watch `der-recursive-update` for THREAD-A.

**6 Next-segment prediction.** OUTLINE next: `def-observation-function`
("lossy, noisy observations"), formalizing $o_t=h(\Omega_t,a_{t-1},
\varepsilon_t)$, axiomatic, `depends:` including `def-agent-environment`
(and plausibly `def-action-transition` for the $a_{t-1}$ argument).

**7 What I'd change.** Add one clause to the dual-Markov paragraph
acknowledging the bounded-vs-unbounded asymmetry, or explicitly forward-ref
where the agent-side boundedness cost is discharged. As written it slightly
over-claims symmetry. (Editorial-to-substantive depending on THREAD-B
resolution.)

**8/9/13 Curiosity / enables / contribution.** The state-augmentation
WLOG argument for $\Omega$ is standard control theory; its honest
characterization as a *commitment about breadth* (not an empirical claim) is
the AAT-discipline value-add. What it *enables*: it lets every downstream
result quantify over $T$ without a "assuming Markov dynamics" caveat — same
propagation-freedom dividend as segment 01's constitutive loss move.

**12 Felt value.** Moderate — higher than a bare definition because the
dual-Markov paragraph is doing real epistemic work and (usefully for the
audit) exposes a seam.

## Wandering thoughts (≤2 ¶)

The pair (01, 02) shows AAT's founding rhetorical strategy clearly: convert
every potential empirical objection into a *definitional scope decision* and
say so out loud. "Environments aren't really Markov" → "Ω is *defined* as the
sufficient state." "Agents don't have perfect access" → "loss is
constitutive." This is disciplined and honest, and it buys propagation-freedom.
But it has a characteristic failure mode the auditor should track: when you
discharge an objection by *definition*, the cost doesn't vanish — it
*relocates* to wherever the defined object meets a constraint. For Ω the cost
relocates nowhere (Ω is unbounded). For M_t it relocates to the model-capacity
machinery (R, model-class fitness, sufficiency). The segment's claim that the
two moves are "independent" is true as stated but invites the reader to also
infer "and equally cost-free," which is false. The most valuable audit
contributions in a framework this disciplined will often be exactly here: not
"the framework made an assumption it hid," but "the framework discharged a
cost by definition and the relocated cost is under-tracked at the new site."

Counterfactual worth holding: if AAT had *not* made Ω-Markov a definitional
commitment, it would need a global "assuming Markov environment" caveat — and
then the bounded-M_t asymmetry would be *visible* because both sides would
carry caveats and the reader would compare them. By making both moves
definitional, the framework gains cleanliness but loses the natural place
where the asymmetry would have announced itself. That is a real and subtle
architectural tradeoff; whether it's net-good depends entirely on whether
`def-model-sufficiency` / `form-agent-model` re-surface the M_t-side cost
loudly enough. That is now one of the things I am most curious to reach.

## Diagram

Represents *my new understanding*, which is the closed loop **plus** the
spotted bounded/unbounded asymmetry in the dual-Markov move. Left: the
fundamental loop $\Omega\xrightarrow{h}o\to\text{agent}\xrightarrow{a}\Omega$
with the two opacity lenses ($h$ unknown, $T$ unknown). Right: the asymmetry
inset — $\Omega$ as an arbitrarily-extensible box (augment freely, WLOG) vs
$M_t$ as a fixed-capacity box (augmentation hits the wall). See
`02-def-action-transition.tex`.
