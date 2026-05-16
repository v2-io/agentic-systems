# 05 — scope-adaptive-system

`type: scope · status: axiomatic · stage: claims-verified · depends: [def-agent-environment, def-observation-function, def-chronica]`

## Dep-graph / OUTLINE-order check
Deps = 01, 03, 04 (all upstream). **Deliberately omits `def-action-transition`
(02)** — and that omission is *correct*, not a Gate-1 miss: adaptive scope is
the pre-action scope (explicitly includes "passive Bayesian learners," "Kalman
filter estimating a passive signal"); the Formal Expression uses only
$\mathcal O$, $\mathcal C_t$, $\Omega_t$, $H$ — no $T$/$a_t$. Precise
dependency hygiene = positive §E datum. OUTLINE stage `claims-verified` matches
frontmatter `stage:` — stage-consistency check passes. B7 alive.

## Prompt walk

**1 Predictions vs evidence.** Predicted it consumes the primitives and states
the broadest scope condition; that it is the segment seg-01 forward-referenced.
Both correct. Did not predict the *precise* operationalization
$H(\Omega_t\mid\mathcal C_t)>0$ — see prompt 2.

**2 Cross-segment consistency — a *sharpening*, audited as sound.** Seg-01
made information loss constitutive *at the observation map* ($h$ many-to-one).
This segment operationalizes it *at the history level*: $H(\Omega_t\mid
\mathcal C_t)>0$. These are not the same condition — a per-step-lossy $h$ can
still, accumulated over a static environment, drive $H(\Omega_t\mid\mathcal
C_t)\to 0$ (collectively-injective-over-time). The segment uses the
*history-level* condition, which is the correct operational one (it is exactly
what makes the *dynamics* non-vacuous). So this is a genuine
sharpen-not-restate: seg-01's constitutive intuition is here promoted to the
operationally right predicate, and the exclusions ($H=0$ closed-form;
$\mathcal O=\emptyset$ pure computation) match seg-01's "perfect access ⟹
vacuous" exactly. Consistency holds and the framework *strengthened* its own
boundary in the right direction. Positive §E.

*THREAD-F (low).* The set $\mathcal S_\text{adaptive}=\{(\text{Agent},\Omega):
\mathcal O\neq\emptyset,\,H(\Omega_t\mid\mathcal C_t)>0\}$ has **no temporal
quantifier** on $H(\Omega_t\mid\mathcal C_t)>0$ (∀t? ∃t? eventually? running?).
An agent that fully learns a static world has $H\to0$ and would exit scope
mid-life. Probably immaterial — the persistence results carry GA-2 disturbance
$\rho>0$ which keeps $H>0$ as a running condition — but check whether any
later result needs $H>0$ *uniformly in $t$* while only this set-predicate is
cited as its scope warrant. If so, scope-honesty gap. Logged.

*Minor seam (note, not finding).* `def-chronica` wrote $\mathcal
C_t=(o_1,a_1,\dots)$ with actions interleaved; adaptive scope admits
action-free passive systems conditioning on $\mathcal C_t$. The clean reading:
$\mathcal C_t$ is the interaction *record*; for a passive observer the action
entries are vacuous and $\mathcal C_t$ degenerates to the $o$-subsequence.
Consistent; the primitive-layer notation just leads with the agent case. Not
§B; ≤§G editorial if anything.

**3 Math.** Entropy-conditioning $H(\Omega_t\mid\mathcal C_t)>0$ is the right
formal object; $H=0$ ⟺ $\Omega_t$ a.s. determined by $\mathcal C_t$ — correct.
Nothing numerical to compute.

**4/5 Direction / errors to watch.** This installs the *scope-region* mental
model the OUTLINE's Part II "scope lattice" will lean on. Watch that Part II's
nested scopes (agency ⊂ adaptive; learning-agent; Class-1) are stated as
*genuine intersections* (as here: agency = adaptive ∩ Pearl-L2-contrast), not
as relabelings. The discipline shown here is the standard to hold them to.

**6 Next prediction.** OUTLINE next: `scope-agency` — "narrows to action with
Pearl-level-2 contrast." `type: scope`, depends on `scope-adaptive-system`
(+ `def-action-transition`, finally, since action enters here) and likely
`def-pearl-causal-hierarchy` *forward*-ref. Prediction: agency =
$\mathcal S_\text{adaptive}\cap\{$≥binary choice, ≥1 action with distinct
interventional outcome distribution$\}$.

**7 What I'd change.** Add the temporal quantifier to the $H>0$ condition (or
a clause "as a running condition; see GA-2") to close THREAD-F preemptively.
Cheap, prevents a downstream scope-honesty seam.

**8/9/13 Curiosity / enables / contribution.** What this *enables*: a clean
two-axis exclusion geometry ($\mathcal O$-axis and $H$-axis) that every later
scope narrowing can be drawn *inside*. The contribution is not the conditions
(standard partial-observability) but the *honest geometric framing*: AAT is
the theory of the open region, with both degenerate boundaries explicitly
named and excluded rather than absorbed as limits. That geometry is reusable
and is, I think, genuinely good pedagogy waiting to be drawn.

**12 Felt value.** Medium. Not surprising, but it is the segment where seg-01's
philosophy becomes an operational predicate, and it does so by *strengthening*,
which is the behavior CLAUDE.md's discipline most wants — worth a §E mention.

## Wandering thoughts (≤2 ¶)

The audit-relevant pattern across 01→05: AAT keeps *promoting constitutive
intuitions into operational predicates and tightening them as it goes*, rather
than asserting the strong form up front and caveating later. Seg-01: "loss is
constitutive" (philosophy). Seg-05: "$H(\Omega_t\mid\mathcal C_t)>0$"
(predicate), which is *strictly the right* condition and is a strengthening of
the per-map lossiness (it is the history-level statement that actually
controls non-vacuity of the dynamics). This is the inverse of the failure
mode CLAUDE.md warns about (assert strong, soften later); here the framework
asserts a philosophical commitment, then *cashes it as the precise
operational condition*. Five segments in, the foundation is behaving like a
disciplined theory, and the right thing for the audit to record is *where it
keeps doing this* (calibration §E) so the reader can weight the eventual §B
findings against a baseline of genuine discipline rather than against an
assumed-charitable one.

The only structural soft spot here is the missing temporal quantifier
(THREAD-F), and it is interesting precisely because it is the kind of thing
that *looks* like nothing and could be load-bearing: if a downstream
persistence or identifiability result quietly needs $H>0$ to hold *uniformly*
(not just initially), then this set-predicate is under-specified as a scope
warrant and the gap would be invisible at every individual segment while real
across them — the §3.4 within-vs-cross failure mode in miniature. I'll carry
it. Counterfactually, had the framework written $\inf_t H(\Omega_t\mid\mathcal
C_t)>0$ or tied it to $\rho>0$, the scope would self-evidently compose with
the persistence results; as written, the composition is *probably* fine but
*assumed* rather than *shown*.

## Diagram

*My new understanding* = the scope as a two-axis open region with both
degenerate boundaries explicitly excised, and agency as a true nested
sub-region. Idiom: region/Venn geometry (not a node graph). Axes: perceptual
channel ($\mathcal O=\emptyset$ wall) and residual uncertainty
($H(\Omega_t\mid\mathcal C_t)=0$ wall). $\mathcal S_\text{adaptive}$ = the open
interior; $\mathcal S_\text{agency}$ = adaptive ∩ Pearl-L2 contrast, a nested
disc. Isomorphic: push toward either wall ⇒ exit the region into the named
degenerate case (pure computation / closed-form). Establishes the
scope-onion vocabulary Part II reuses. See `05-scope-adaptive-system.tex`.
