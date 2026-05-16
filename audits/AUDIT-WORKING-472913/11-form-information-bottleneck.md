# 11 — form-information-bottleneck  *(no finding; multiple strong §E exemplars; Phase-3 hypothesis survives a real test)*

`type: formulation · status: exact · stage: draft · depends: [form-agent-model, def-action-transition]`

## Dep-graph / DETECTOR / OUTLINE-order
Deps = 10, 02 (upstream). `def-chronica` is transitive via `form-agent-model`
— direct deps are exactly what the Formal Expression uses (the
$a_{t:\infty}$-conditioning ⇒ `def-action-transition` is a *genuine* dep, not
"mentioned"). One `*[Formulation (IB-objective)]*` tag, no `*[Derived]*` —
DETECTOR clean. B7 alive (11/11).

## Status/type tension — tested, NOT a finding (strong §E)

I predicted a possible `status`-label mismatch (`status: exact` on a
`type: formulation` segment). Tested: the Epistemic Status paragraph
*explicitly resolves it* and does so exactly per FORMAT.md's Gate-2
type-vs-status decomposition: `type: formulation` because *choosing IB* (over
MDL / Bayesian-sufficiency) is a representational choice; `status: exact`
because *given that choice* the IB optimum's form is an exact consequence of
the imported Tishby–Pereira–Bialek 1999 theorem under the explicit binding
$X=\mathcal C_t$, $T=M_t$, $Y=o_{t+1:\infty}\mid a_{t:\infty}$, Markov chain
$Y\!-\!X\!-\!T$ by construction. The "Max attainable" note ("exact for the
IB-as-applied-theorem core; robust-qualitative for $\beta(\rho,\pi)$") applies
FORMAT.md's max-attainable discipline precisely. This is one of the most
careful Epistemic Status paragraphs in the walk so far — **§E exemplar**, and
a direct counter-instance to F2's tag-inversion: the framework *can* pair
type/status with full rigor; F1/F2 are lapses, not the mode.

## Gate-2-probes-Discussion: the β-vs-ρ claim — actively verified (not nodded)

Per CLAUDE.md Gate-2 discipline + my Phase-3 commitment to seek a *content*
defect, I did not charitably nod the segment's most substantive Discussion
claim — the "double-counting error" paragraph. **Verification:** IB optimum
$\phi^\ast=\arg\min_\phi[I(M_t;\mathcal C_t)-\beta\,I(M_t;o_{t+1:\infty}\mid
a_{t:\infty})]$ is determined by the joint $p(\mathcal C_t,Y)$. Higher
volatility $\rho$ ⇒ faster decorrelation ⇒ $I(\mathcal C_t^{\text{old}};
o_{t+1:\infty})$ intrinsically lower ⇒ the IB-optimal $\phi^\ast$ retains less
of the old tail *at fixed $\beta$*, because there is less predictive content
to retain. So volatility enters **through the joint distribution / the IB
curve**, not through $\beta$; "the agent must lower $\beta$ in volatile
environments" double-counts $\rho$ (once via $p$, once via $\beta$). The
claim **holds** — it follows from the IB objective's structure, it is not
post-hoc plausibility. It is correctly tiered (direction robust-qualitative;
$\beta$ = internal-memory-cost the substantive reinterpretation). This is the
*good* Gate-2 case (claim that ADDS something that follows from the
formalism), the inverse of CLAUDE.md's "deliberation as computation"
anti-example. A genuinely sharp insight; **§E**, even Finding-grade as a
*strength* (it forecloses a common modeling error).

**Phase-3 hypothesis status:** I tried to break "all findings are
unnamed-relocations, never wrong content" by hard-checking this segment's one
non-trivial derivable claim. It was *correct*. Hypothesis survives a genuine
disconfirmation attempt (logged — the attempt matters as much as the
outcome).

## §E: anti-F2 relocation-naming + prior-art discipline

- **Explicit relocation-target naming (anti-F2):** "the cross-instance
  unification claim itself remains *robust-qualitative*, which is a property
  of `#disc-compression-operations`, *not of this segment*." The segment
  *disclaims downstream segments' epistemic burdens by name* — the exact
  opposite of F2 (which absorbed a downstream derived result). This is the
  framework doing relocation-naming *perfectly*, which sharpens the Phase-3
  spine: the defect class is *unnamed* relocation; here naming is exemplary.
- **Prior-art integration (CLAUDE.md discipline):** IB adopted directly, full
  citation, "*not* a novel formulation," original name kept; the
  IB-vs-IT-MDP-lineage and variational-free-energy positioning live *in
  Discussion* (where CLAUDE.md says integration belongs, not a separate
  comparison doc); explicit non-over-adoption ("borrows the form without
  committing to AI's preferences-as-priors stance"). Textbook-correct.

## THREAD-B reinforcement
"when a model is 'good enough' … formalized in `#def-model-sufficiency`" —
`def-model-sufficiency` named *again* as the adequacy home (3rd consistent
naming: seg-09 preview, seg-10 forward, seg-11 here). THREAD-B's resolution
path is robust; near-certain dissolution pending the def-model-sufficiency
delivery check (seg ~12).

## Prompt walk (others, brief)

**1 Predictions.** Type ✓; status mis-predicted (guessed robust-qual; actual
`exact`, and the actual is *more precise and correct* — third consecutive
under-credit of the framework's status precision; prior firmly updated:
**default-expect AAT to choose the more rigorous honest label**, stop
predicting the softer one).
**6 Next prediction.** OUTLINE next: `#def-model-sufficiency` (`type:
definition`, OUTLINE stage `deps-verified`). Predict: defines $S(M_t)\in[0,1]$
= fraction of $\mathcal C_t$'s predictive info retained; deps form-agent-model
(+ form-information-bottleneck). **THREAD-B decisive test:** does it quantify
the *bounded-adequacy* residual (deliver the thrice-forwarded "enough?"
question)? Predict yes (the relocation-naming has been too consistent to
fail) ⇒ THREAD-B → §B.1 rescinded.
**7 What I'd change.** Nothing. Another F2 yardstick.
**12 Felt value.** High — no finding, but the richest §E segment yet and the
first place I *actively tried and failed to break* the Phase-3 spine, which
is worth more to the audit's integrity than a marginal finding.

## Wandering thoughts (≤2 ¶)

The audit is developing a clean bimodal texture: the *derivation/postulate
hinge* segments (06 scope-agency, 07 post-composition) carry the
unnamed-relocation defects; the *formulation/bridge* segments (09, 10, 11)
are not just clean but *exemplary* — they name relocation targets, tier their
claims, and disclaim downstream burdens with a precision that is genuinely
impressive. This bimodality is itself the most important Phase-3 observation
so far: it is not that AAT's integration discipline is uniformly slipping
(the integration-debt hypothesis in its crude form), it is that the
discipline is *excellent in the framing/formulation layer and lapses
specifically where a foundational segment got retrofitted with downstream
load* (F2) or borrowed downstream vocabulary into a Formal Expression (F1).
The sharpened spine: **the defects cluster at points of forward-pressure on
load-bearing early segments** — exactly where the framework's strongest
results "want" to be visible early. That is a more precise, more useful, and
more *charitable-yet-rigorous* diagnosis than "integration slipped," and it
points at a concrete structural remedy (the split discipline + the TG1 lint).
I'm now fairly confident this is the §F headline; still seeking the
disconfirming *content* defect, and noting honestly that 11 segments in I
have not found one — every finding is structural/relocational, every
content/math claim I've hard-checked has held.

The β-vs-ρ double-counting point deserves a sentence of its own
appreciation, setting aside audit-voice: it is the kind of result that is
*obvious once seen and easy to get wrong unseen*, which is exactly the
novelty signature I flagged in 00-initial-predictions §5 for the
satisfaction-gap split. A modeller who "lowers β because the world is
volatile" is making a real, common, plausible-sounding error, and the segment
kills it in three sentences by pointing at where ρ actually enters the
objective. If the rest of the framework has more of these, the "integration
not invention" framing undersells it — there is genuine *clarifying* novelty
in saying precisely which knob a cause turns. Logged as a Phase-3 / §F
positive (the framework's distinctive value may be *disambiguation of which
parameter responds to which cause*, a recurring move I should now watch for
as a named pattern, not just instance-by-instance).

## Diagram

Two-layer vertical. **Anchor:** a *travel journal* of finite size. Stable
trip ⇒ old entries still predict tomorrow ⇒ keep many. Chaotic trip ⇒
yesterday barely predicts tomorrow ⇒ *the world itself* makes old pages
worthless, so the optimal journal shortens **automatically**. Bag-size /
writing-time = $\beta$ = an *internal* budget, **not** "how chaotic the trip
is." Double-counting = shrinking the journal *because* the trip is chaotic
when chaos already made old pages worthless (cutting twice). Perturb: crank
chaos ⇒ old-page predictive value drops natively (curve shifts) at fixed bag;
shrink the bag only if the bag actually shrank. **Skeleton:** the IB
rate–distortion curve with **two independent levers** — $\rho$ shifts the
*curve* (via the joint $p(\mathcal C_t,Y)$), $\beta$ slides the *operating
point* (internal cost). The "tempting error" (move both for one cause) drawn
as an amber path that is **struck through** (refuted, theory's-voice
correction — like seg-06's cut, but here the X marks the *error the segment
kills*, not an audit finding). Solid = `exact` IB core; dashed =
robust-qualitative $\beta(\rho,\pi)$ direction. See
`11-form-information-bottleneck.tex`.
