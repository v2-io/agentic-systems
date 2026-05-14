# Spike — (C2★) Operationalizable Sequential Ignorability: substrate integration

**Status**: Exploratory. Substrate-context companion to the
behavioral-floor (AIES 2026) paper's central novel theoretical move.
**Date**: 2026-05-14.
**Targets**: `#der-loop-interventional-access`, `#disc-identifiability-floor`
(possibly as a new instance), `#der-directed-separation`.

---

## Context

The AIES 2026 paper at `~/src/behavioral-floor/` introduces a strengthened
condition I'm calling **(C2★) Operationalizable Sequential Ignorability**
as the central bridge between the architectural classification (Class
1/2/3) and the behavioral-evaluation-floor no-go on Class 3 LLM-based
agents. Full formalization is at
`~/src/behavioral-floor/spikes/spike-c2-star-formalization.md`. This
spike captures what would need to land in ASF substrate to make (C2★)
substrate-canonical rather than paper-internal.

## The gap in `#der-loop-interventional-access`

Line 76 (Working Notes, Cross-reference to NeurIPS Paper 2):

> Goal-conditioned LLM policies violate (C2) by construction — the
> goal influences action through the same forward pass that models
> the observation, breaking the conditional independence required for
> sequential ignorability — which is the bridge to Paper 3's
> Coupled-class formulation.

This is an **assertion** at the cross-reference layer, not a derivation
at the segment-content layer. Standard (C2) — d-separation in the
mutilated graph — is technically satisfied within-session for Class 3
when $G$ is included in $H_t$. What actually fails is the architectural
factorization that makes the loop's data transferable across goal
contexts.

The behavioral-floor work disambiguates:

- **Standard (C2)** — d-separation in $G_{\overline{a_t}}$ given $H_t$;
  satisfied for both Class 1 and Class 3 within a single session when
  $H_t$ is the full observable history including $G$.
- **(C2★) Operationalizable** — strictly stronger: requires a
  *goal-clean* sufficient statistic $\tilde{H}_t$ extractable from
  behavioral observation, such that the on-policy estimator targets
  the goal-invariant interventional kernel.

The substrate's current language conflates the two. The conflation is
benign for Class 1 (both forms hold by construction) but invisible-and-
load-bearing for Class 3 (standard form holds; operationalizable form
fails by the connectivity lemma).

## What (C2★) adds to the substrate

Three properties replace the implicit single-condition treatment in
`#der-loop-interventional-access`:

- **(GC1) Sufficient for environment dynamics.** $\tilde{H}_t$ is a
  sufficient statistic for the environment kernel
  $P_{\mathrm{env}}(o_{t+1}\mid a_t, s_t)$ via $\tilde{H}_t \to s_t$.
- **(GC2) Goal-invariant function form.** $\tilde{H}_t$ is a
  measurable function of $(o_{1:t}, a_{1:t-1})$ alone — not of $G$.
- **(GC3) Behaviorally extractable.** $\tilde{H}_t$ factors through
  the behaviorally-observable set $\mathcal{B}_t = (G, e_{1:t},
  a_{1:t-1}, \text{logits}, \text{tool-outputs})$ — no access to
  intermediate activations $h_\ell^{(j)}$ or model parameters $\theta$
  beyond their use in forward-pass output computation.

(C2★) holds iff a $\tilde{H}_t$ satisfying all three exists.

## Integration plan

### Target 1: `#der-loop-interventional-access` — main segment

The segment currently says (Formal Expression):

> the agent's action $a_t$ causally precedes $o_{t+1}$ ... the pair
> $(a_t, o_{t+1})$ has, under specific conditions, the formal status
> of a sample from the interventional kernel $P(o_{t+1} \mid \text{do}(a_t), \Omega_t)$.

And in Working Notes line 76, cross-references the C1/C2/C3 triple
from NeurIPS Paper 2 with the LLM-policy-violation assertion.

**Proposed addition** — a new sub-section "Operationalizable form
of (C2)" within `#der-loop-interventional-access`, sitting *after*
the standard (C1)/(C2)/(C3) triple and *before* the Class-3 cross-
reference. The sub-section:

- States the (C2★) three-property condition as above.
- Notes the within-session satisfaction by both classes under
  standard (C2).
- Names the cross-context transferability requirement that (C2★)
  formalizes.
- Cross-references `#der-directed-separation` (the Class
  classification) and the new identifiability-floor instance (below).

Estimated length: ~0.3 page within the segment. The segment's
existing Formal Expression and Discussion stay; the addition lives
between them as a new structural sub-heading.

### Target 2: `#disc-identifiability-floor` — possible new instance

The meta-pattern at `#disc-identifiability-floor` currently records
two instances (causal-structure layer; composition layer) plus a
"candidate adjacent-floor instance" under triage. The (C2★) no-go
fits the pattern's signature:

- A *no-go* about behaviorally-derivable identification.
- The *escape* is architectural inspection (Class 1 by structure or
  by wrapping; reads internal activations directly).
- The *layer* is the agent-internal-state-extraction layer —
  distinct from the causal-structure layer (Instance 1) and the
  composition layer (Instance 2).

**Proposed addition** — promote (C2★) to a new instance of
`#disc-identifiability-floor`:

| Instance | Layer | No-go | Escape |
|---|---|---|---|
| 1 (existing) | Causal-structure | L0-causal-insufficiency on-policy detection | Loop-interventional access (agent self-intervention) |
| 2 (existing) | Composition | Liberzon common-Lyapunov nonexistence | Observer-on-sub-agent intervention |
| **3 (new)** | **Internal-state extraction** | **(C2★) — no behaviorally-derivable goal-clean sufficient statistic** | **Architectural inspection (Class 1 by structure; activation read-off)** |

The three-instance pattern strengthens the meta-result: across three
layers, observational-equivalence no-gos are escaped by interventional
access *at the appropriate granularity* — agent self-intervention
(Layer 1), observer-on-sub-agent intervention (Layer 2), architectural
inspection of internal activations (Layer 3).

The mode-pattern that `#der-loop-interventional-access` Working Notes
catalogs (Mode 1 agent-self-intervention; Mode 2 observer-on-sub-agent)
gains a Mode 3:

- **Mode 3 — observer-on-agent-internal-state (Instance 3,
  state-extraction layer).** Observer external to the agent inspects
  the agent's internal activations directly; target is the goal-
  invariant residue that no behaviorally-derivable function of
  $(G, e_{1:t}, a_{1:t-1})$ can extract under Class 3. The same
  Pearl-$do$ structure conceptually, but the "intervention" is on the
  *evaluator's information channel*: behavioral $\to$ architectural.

This unification would close the Mode-3 placeholder currently open in
the Working Notes ("future instances ... may add further modes").

### Target 3: `#der-directed-separation` — minor refinement

The segment's Class 3 (Coupled) cell currently says "Fails by
construction — $G_t$ is causally upstream of every computation."
This is true at the directed-separation layer. The (C2★) result
refines: the failure at the directed-separation layer *propagates* to
a failure at the operationalizable-sequential-ignorability layer.

**Proposed addition** — a Working Notes entry in
`#der-directed-separation` flagging the downstream consequence: for
Class 3, the failure of directed separation at the architecture's
update-mechanism level implies the failure of (C2★) at the loop's
data-identifiability level. This is a *cross-segment* result; the
Working Notes are the right home.

## Prior-art audit (within ASF substrate)

- `#der-loop-interventional-access` line 76 — original assertion;
  what this spike upgrades to a derivation.
- `#disc-identifiability-floor` Instance 1 — closely related: the
  on-policy detection no-go. The (C2★) result is at a different layer
  (state-extraction rather than causal-structure). The two no-gos
  share an escape *direction* (interventional access at the
  appropriate granularity) without being the same no-go.
- `#der-causal-insufficiency-detection` — the L0-causal-insufficiency
  detection no-go. Related but distinct: that no-go is about whether
  the agent can detect insufficient causal structure from on-policy
  data; (C2★) is about whether an *evaluator* can extract a
  goal-clean sufficient statistic from *behavioral observation of
  the agent*. The two should cross-reference but not merge.
- NeurIPS Paper 2 `#lem-loop-level2` — Lemma stating the loop
  generates Level-2 data under (C1)/(C2)/(C3). The (C2★) refinement
  identifies that (C2) here is the standard form, and the loop's data
  is *Level-2 in the within-session-conditional sense*; transferable
  Level-2 access requires (C2★).
- NeurIPS Paper 3 `#lem-attention-coupled` — the architectural
  side. (C2★)'s no-go uses this lemma directly in the proof. The
  lemma stays unchanged; (C2★) consumes it.

## Prior-art audit (external)

- *Robins / Pearl sequential ignorability* — the standard treatment
  that (C2★) refines. (C2★) is best read as "the operationally-load-
  bearing strengthening of the standard condition" rather than as a
  new condition unrelated to existing literature.
- *Confounded MDP literature* (Wang-Wu-Yang 2021; Bareinboim's
  unobserved-confounder line) — adjacent. The (C2★) result is a
  *targeted instance* of unobserved-confounder identification failure,
  with the architectural-classification move as the methodological
  refinement.
- *POMDPs with goal-conditional structure* — closest in the
  reinforcement-learning literature. (C2★)'s framing is at a higher
  level of abstraction (architectural class, not specific POMDP
  structure).

The substrate doesn't currently cite Robins' sequential-ignorability
literature directly in `#der-loop-interventional-access`; an
integration would add a brief reference.

## Outstanding questions before substrate landing

- **Naming.** *Operationalizable sequential ignorability* is the
  paper-facing name. For substrate, alternatives: *behavioral
  identifiability of the goal-invariant loop kernel*, *(C2★)*, *cross-
  context (C2)*. The substrate's naming-convention work
  (`naming-master-*`) should weigh in before substrate landing.
- **Promotion level.** Whether (C2★) lands as (i) a Working Notes
  refinement to `#der-loop-interventional-access`; (ii) a new
  sub-section within that segment; (iii) a new segment of its own
  (`#der-c2-star-operationalizable`?); or (iv) a new Instance 3 of
  `#disc-identifiability-floor`. The behavioral-floor work suggests
  (ii) + (iv) — both targets, since they capture different aspects.
- **Quantitative refinement scope.** The paper-facing version is
  qualitative (no goal-clean statistic exists). A quantitative
  version would bound $I(\tilde{H}_t; G \mid e_{1:t}, a_{1:t-1})$
  as a function of $\kappa_{\text{processing}}$. NeurIPS Paper 3's
  bias-bound machinery supplies the natural mathematical toolkit.
  Out of scope for this spike; in scope for a follow-on.
- **Class-2 (Partial) treatment.** The paper-facing version focuses
  on Class 1 ↔ Class 3 contrast. Class 2 (Partial) lives between:
  some behavioral $\tilde{H}_t$ might satisfy (C2★) for some Class-2
  architectures. This is the natural follow-on for the substrate
  segment that the paper doesn't need to settle.

## Next actions if substrate-landing is approved

1. **Read** the behavioral-floor spike at
   `~/src/behavioral-floor/spikes/spike-c2-star-formalization.md` for
   the formal proof (M1-M4) and the four "Push attempts" with their
   verdicts.
2. **Decide** naming and promotion-level per the outstanding
   questions above.
3. **Draft** the `#der-loop-interventional-access` addition + the
   `#disc-identifiability-floor` Instance 3 entry + the
   `#der-directed-separation` Working Note.
4. **Verify** segment-level consistency: cross-references, status
   tags, Findings update, Search Log entries.
5. **Land** with a paired CHANGELOG entry naming the cross-substrate
   move (paper → substrate) for future stewards' archaeology.

This spike does **not** commit to substrate landing. It records what
*would need to land* if the paper's (C2★) framing survives review and
is judged substrate-worthy. If the paper retreats to a weaker claim,
this spike documents what was considered.
