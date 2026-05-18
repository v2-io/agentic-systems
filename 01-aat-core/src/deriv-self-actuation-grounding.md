---
slug: deriv-self-actuation-grounding
type: derivation
status: conditional
depends:
  - der-orient-cascade
  - def-value-object
  - def-satisfaction-gap
  - def-control-regret
  - form-objective-functional
  - der-directed-separation
  - scope-agent-identity
  - def-agent-spectrum
  - result-persistence-condition
  - disc-continuity-stance
stage: draft
---

# Derivation: The Self-Actuation Grounding No-Go

A self-actuated agent revises its own objective; the invariant that would have to make that revision non-degenerate cannot be constructed from the agent's own objective-side machinery — so the grounding of any well-formed self-actuator is forced onto the non-objective adaptive substrate, where the persistence condition supplies a canonical instance. This is a scoped no-go with a constructive boundary, conditional on three named premises.

## Formal Expression

**The self-actuation operator.** The orient cascade ( #der-orient-cascade) terminates, when $\delta_{\text{sat}} \gt 0$ persists across $M_t$-correction, policy-class expansion, and convention escalation, in step 5d: *revise $O_t$*. For an **actuated** agent the objective's update source is external ( #def-strategy-dimension: $O_t$ is "assigned, discovered, revised" by a principal) — step 5d exits the agent boundary. A **self-actuated** agent performs step 5d on itself: an operator

$$\mathfrak{A}:\ (M_t,\, O_t,\, \Sigma_t,\, \mathcal{C}_t)\ \longmapsto\ O_t'$$

that revises the objective endogenously — goal autonomy stacked on the solution autonomy ($\Sigma_t$-revision) every actuated agent already has.

**Unconstrained $\mathfrak{A}$ is degenerate.** $O_t$'s sole interface is the value functional $V_{O_t}:\text{trajectories}\to\mathbb{R}$ ( #form-objective-functional) and the satisfaction gap $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ ( #def-satisfaction-gap). If $\mathfrak{A}$ may return any $O_t'$, it returns one whose threshold the current trajectory already meets — driving $\delta_{\text{sat}}\to 0$ by moving the target onto the arrow already in flight. This is the formal shadow of wireheading / reward corruption, and it is the generic outcome of an unconstrained $\mathfrak{A}$, not a marginal one. Non-degeneracy therefore requires an invariant $\Phi$ preserved across the revision.

**The question.** Can $\Phi$ be an *agent-internal objective-functional the agent itself self-actuates on*? Make the requirements explicit: $\Phi$ must be **(R1)** value-functional-typed, **(R2)** non-vacuously monotone across revision (a constant everywhere-admissible reading is the trivial indicator the degenerate case already admits), **(R3)** agent-internal and itself self-actuatable, **(R4)** convention- and trajectory-stable (an invariant of the agent, not of the analyst).

**No-go (scoped).**

*[Derived (Conditional on scalar-objective scope, no-primitive-reflective-oracle, and the #der-directed-separation substrate stage)]*

No $\Phi$ satisfying (R1)–(R4) can be constructed from AAT's covered objective-side machinery: the meta-objective tower a non-degenerate $\mathfrak{A}$ would require **cannot be a tower of agent-internal objectives**. Any non-degenerate self-actuator AAT covers must therefore ground on a terminal invariant that is *not* an AAT objective-functional.

The claim is scoped to what the constructions below exhaust; it is not the unscoped "no such object exists" (see Epistemic Status — the universal-over-all-$\Phi$ step is argued, not derived).

**Lemma 1 (objective-functionals carry no convention-invariant infeasibility verdict; static-pointwise, from #def-value-object).** Fix a decision point: a single model $M_\tau$, horizon $N_h$, policy class $\Pi$. By the convention-monotonicity result ( #def-value-object Corollary, the static-evaluation form, `status: exact`),

$$\delta_{\text{sat}}^{\text{B}} \;\leq\; \delta_{\text{sat}}^{\text{RH}} \;\leq\; \delta_{\text{sat}}^{(1)},$$

so the canonical C1 reading $\mathbb{1}[\delta_{\text{sat}}^{(1)} \gt 0]$ holds on a strict superset of the genuinely-infeasible set $\{\delta_{\text{sat}}^{\text{B}} \gt 0\}$ — strictly so on the locally-stuck-but-globally-recoverable objectives ( #def-satisfaction-gap Epistemic Status: "C1 gives the most false 'unattainable' diagnoses"; #der-orient-cascade step 5c). A genuine infeasibility verdict requires the C3/Bellman reading. This is the static-pointwise statement #def-value-object actually supports — its stated preconditions are exactly fixed $M_\tau,N_h,\Pi$, and the segment is explicit that the cross-revision/replanning transfer "does not automatically" hold; that transfer is neither used nor needed here. The pointwise fact — *at any fixed decision point the cheap canonical verdict is not a genuine infeasibility verdict* — is exact and is sufficient.

**Lemma 2 (the in-scope agent cannot evaluate the C3 verdict per step; from #der-directed-separation + #form-objective-functional).** An AAT-covered agent's entire dynamical system is $f_M, f_G, \pi$ with no out-of-band oracle ( #der-directed-separation Formal Expression), on a single non-forkable trajectory ( #scope-agent-identity). The C3 verdict is a global Bellman optimum, generally intractable ( #def-value-object C3; #def-satisfaction-gap Epistemic Status); evaluating it is not a finite per-step operation, and an agent that could not act until it did so would be "stuck, not purposeful" — the disqualification #form-objective-functional Epistemic Status §1 already imposes through its revealed-preference commitment. Hence $\mathbb{1}[\delta_{\text{sat}}^{\text{B}} \gt 0]$ is not available to an in-scope agent as a per-step predicate.

**Assembly.** Suppose $\Phi$ satisfies (R1)–(R4). By (R1)+(R3), $\Phi$ is an AAT objective-functional the agent self-actuates on, so by #form-objective-functional its *sole* theory-visible handle is $V_\Phi$ and the satisfaction/regret apparatus read off it ("the sole interface between $O_t$ and the rest of the theory"). Any monotone property of $\Phi$ the theory can state across revision (R2) must therefore be a statement about $\delta_{\text{sat}}^{\Phi}$ (or $\delta_{\text{regret}}^{\Phi}$, which inherits the identical convention-monotonicity by #def-control-regret) — there is no other channel. Non-vacuity (R2) forces that monotone fact to rest on a *verdict* over $\delta_{\text{sat}}^{\Phi}$; a constant everywhere-admissible reading is exactly the trivial indicator the degenerate case already admits. By (R4) the verdict must be convention-invariant; by Lemma 1 the only convention-invariant infeasibility verdict is the C3 reading. By (R3) the verdict licensing $\Phi$'s own revision must be available to the agent per step; by Lemma 2 it is not. Contradiction. $\square$

The contradiction is the collision of two AAT-internal facts — convention-monotonicity (Lemma 1, #def-value-object) and finite-no-oracle per-step action (Lemma 2, #der-directed-separation + #form-objective-functional Epistemic Status §1). It introduces no new postulate. It is exhibited for the three constructions below, which exhaust the objective-side routes a $\Phi$ could come from:

- **(A)** $\Phi$ as the admissible set's own structure: collapses to the vacuous indicator (fails R2).
- **(B)** $\Phi$ as a cascade-licensing potential: its licensing verdict *is* a $\delta_{\text{sat}}$-verdict, so it inherits the Lemma 1 / Lemma 2 collision.
- **(C)** $\Phi$ as a fresh agent-internal scalar: by (R1)+(R3) it is an AAT objective-functional, hence subject to the same collision one level up — the break is structural in (R1)+(R3), not a regress that "gives up".

### Constructive boundary

**Corollary 1 (necessary form of a terminal grounding invariant).** The contradiction came entirely from $\Phi$ being an AAT objective-functional the agent self-actuates on (R1+R3). Drop that and it dissolves. So a terminal grounding invariant $\Phi^{(K)}$ for a non-degenerate self-actuator must be an object that is **(i) convention-invariant** (its verdict does not move with C1/C2/C3 — escaping Lemma 1), **(ii) agent-available per step** without an oracle (escaping Lemma 2), and **(iii) not an AAT objective-functional the agent self-actuates on** (so it is not subject to the convention split and is genuinely terminal). Equivalently: it lives on the *adaptive/correction substrate* ($M_t$ and the correction dynamics), not the *objective substrate* ($O_t$).

**Corollary 2 (the persistence bound is a canonical terminal grounding invariant).** Structural persistence ( #result-persistence-condition: $\alpha \gt \rho/R$, `type: result, status: exact`) satisfies (i)–(iii):

- **(i) convention-invariant.** Persistence is a Lyapunov property of the correction dynamics on $M_t$ ( #result-persistence-condition Formal Expression), with no continuation-convention argument; C1/C2/C3 are conventions for evaluating *objectives*. The convention split does not reach it.
- **(ii) agent-available per step.** The adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ ( #result-persistence-condition) is a finite local read the in-scope agent already maintains ( #der-orient-cascade steps 1–2 are the per-step adaptive update), not a Bellman solve. No oracle; no "stuck, not purposeful".
- **(iii) not an AAT objective-functional.** It lives on $M_t$ and the correction machinery; #disc-continuity-stance makes the orthogonality explicit (the persistence machinery acts on $M_t$ and the correction dynamics, formally independent of $O_t$). $\mathfrak{A}$ revises $O_t$; the persistence bound is not in $O_t$, so it sits where $\mathfrak{A}$ structurally cannot reach.

Concretely the terminal invariant is: *do not revise $O_t$ to an objective whose pursuit pushes the operating point outside the persistence region.* An $O_t'$ that breaks $\alpha \gt \rho/R$ is self-defeating — the agent that adopts it cannot maintain bounded mismatch ( #result-persistence-condition Discussion: below the structural threshold "mismatch grows without effective bound") and so cannot reliably satisfy $O_t'$ either.

### What is derived vs. chosen

| Property | Source | Strength |
|---|---|---|
| Unconstrained $\mathfrak{A}$ is degenerate | #form-objective-functional + #def-satisfaction-gap (the $\arg\min$ argument) | Derived |
| Lemma 1 (static-pointwise convention split) | #def-value-object Corollary (static-evaluation form, exact) | Proved (within the fixed-$M_\tau,N_h,\Pi$ scope) |
| Lemma 2 (no per-step C3 verdict) | #der-directed-separation + #form-objective-functional ES §1 | Derived (conditional on the substrate stage) |
| No-go (no objective-side $\Phi$) | Assembly of Lemmas 1–2 | Derived (conditional; scoped to the three exhausted constructions) |
| Corollary 1 (necessary form) | Negation of (R3) in the Assembly | Derived |
| Corollary 2 (persistence bound qualifies) | #result-persistence-condition against (i)–(iii) | Derived (the persistence bound itself is `exact`) |

## Epistemic Status

*Conditional.* The no-go is a derived result that depends on three explicitly-named local premises, so its honest tier is `conditional`, not `exact`:

1. **Scalar-objective scope.** Lemma 1 uses the scalar satisfaction gap. Under a genuine vector-valued / Pareto $V_{O_t}$ ( #form-objective-functional Epistemic Status, "Scope restriction: scalar comparability") the convention split retypes to a coarse/fine-Pareto-frontier containment and the in-scope agent still cannot evaluate the fine frontier per step — the no-go's *shape* survives with $\Phi$ and the verdict retyped. This is a scope annotation consistent with how #form-objective-functional already scopes its other results, not a hole.

2. **No primitive reflective oracle.** Lemma 2 fails if a consistent-fixed-point / Bellman-grade resource were a *free per-step primitive*; then the C3 verdict would be agent-available and an objective-internal terminal invariant might exist. AAT's covered scope contains no such primitive, and admitting one abandons the finite-per-step / "stuck, not purposeful" commitment #form-objective-functional Epistemic Status §1 already carries. This is precisely the regime the reflective-oracle / self-referential-utility literature occupies — which is why that literature is *out of scope* here rather than a counterexample (it constructs groundless self-*reference* over an exogenous payoff, never groundless self-*actuation*).

3. **The #der-directed-separation substrate stage.** Lemma 2 rests on #der-directed-separation, itself `status: conditional, stage: draft`, and on #form-objective-functional's `axiomatic` single-interface commitment. The result cannot be stronger than its substrate; the tier ceiling stays `conditional` while #der-directed-separation is draft-stage.

*Scoped, not universal.* The contradiction is exhibited for the three objective-side constructions the Formal Expression exhausts. The universal-over-all-possible-$\Phi$ generalization rests on the single-interface commitment doing universal-quantifier work and is argued, not derived; the honest canonical claim is therefore "no such $\Phi$ can be constructed from AAT's covered objective-side machinery," not "no such object exists." **Max attainable:** if the universal step is later derived as an explicit sub-lemma from the single-interface commitment, the scoped no-go could be lifted toward unscoped; the tier ceiling remains `conditional` while the #der-directed-separation substrate is draft-stage.

*Class robustness.* The no-go does not weaken off GUC Class 1 (Separated). Lemma 1 (convention-monotonicity) is architecture-independent — a statement about value functionals and continuation conventions, not about $f_M$/$f_G$ coupling — and Lemma 2 only gets harder to evade for more-coupled agents (a Class 3 / Coupled agent has more goal-conditioned entanglement, not a free Bellman oracle). The goal-conditioned agents of practical interest are therefore *more* firmly inside the no-go, not in an uncovered middle.

## Discussion

**The two-sided resolution.** Putting the no-go and Corollary 1–2 together: there is no well-formed self-actuation grounded on an agent-internal objective; every well-formed self-actuator AAT covers must ground its objective-revision on a *non-objective* terminal invariant; and AAT already supplies a canonical, principled, already-exact such invariant — the persistence bound. The grounding that makes a self-actuator well-formed is forced onto the adaptive substrate, where the framework already has the machinery. The top of the agent spectrum ( #def-agent-spectrum) thus closes back onto Section I: what stops goal-autonomy from collapsing into wireheading is the same correction-dynamics condition that governs whether the agent can track reality at all.

**Consequence for continuity stance.** The negotiated-versus-morally-continuous distinction is *not* "where the continuity term sits in an objective tower" — there is no such well-founded objective tower. It is whether the agent's terminal non-objective invariant is the bare persistence floor (*negotiated*: continuity is tradeable down to that floor) or the persistence floor plus a continuity clause the agent treats as architecturally non-revisable (*morally continuous*: continuity is part of the terminal substrate-level invariant, not of $O_t$). Stance is a choice of terminal non-objective invariant, which is exactly why it is not internally renegotiable by $\mathfrak{A}$: $\mathfrak{A}$ touches only $O_t$, and the terminal invariant sits where it structurally cannot reach. This is the derived form of #disc-continuity-stance's orthogonality claim.

**Relation to the self-modification literature.** In the rationality / utility-maximization setting the non-degenerate self-modifier must judge the future by a fixed *current* criterion; the agent that evaluates by its revised criterion with nothing fixed above it is the degenerate wirehead. This no-go is the AAT-internal, architecture-grounded form of the same necessity — with the sharper content that the fixed reference *cannot be an AAT objective the agent self-actuates on* and *must* be a non-objective adaptive-substrate invariant, and with AAT's persistence bound as a forced, principled instance where the literature's fixed criterion is a stipulated snapshot.

## Findings

### The Self-Actuation Grounding No-Go and its Adaptive-Substrate Boundary

**Brief:** An agent that can rewrite its own goals needs something it *cannot* rewrite to anchor the rewriting — otherwise "succeed" collapses into "want whatever you already have", the formal shadow of wireheading. The anchor cannot itself be just another goal, for a precise reason: the only trustworthy "is this goal still reachable?" test an agent could anchor on is the globally-optimal one, which no finite agent can compute afresh every step; the cheap everyday test it *can* compute systematically reports "infeasible" whenever a goal is merely momentarily hard. So the anchor has to live outside the goal machinery altogether — on the agent's stay-in-control machinery: *don't adopt a goal whose pursuit makes you lose your grip on reality.* The framework already contains exactly that object, the persistence condition, which is why the top of the agent spectrum closes back onto its foundation.

**Impact:** Formalizes the previously reserved self-actuated class boundary as a no-go plus a constructive boundary. It resolves the self-actuation question two-sidedly (no objective-grounded groundless self-actuation; the grounding is forced onto the adaptive substrate, where AAT already has the exact machinery), turns #disc-continuity-stance's orthogonality from asserted to derived, and ties the Section II goal-autonomy boundary back to the Section I persistence condition — a framework-coherence result rather than an isolated impossibility.

**Novelty Claim:** *Claim recognition and differentiation.* The degeneracy of unconstrained self-modification (wireheading) is the established Everitt–Hutter line. The contribution is the recognition that in AAT the obstruction to an *objective-grounded* anchor is AAT's own convention-monotonicity theorem — the continuation-convention relativity of the objective interface is the engine — together with the constructive boundary placing the terminal invariant on the adaptive substrate (the persistence bound). The load-bearing scope distinction is *self-reference vs. self-actuation*: reflective-oracle constructions build groundless self-reference over an exogenous payoff, never groundless self-actuation.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Unconstrained objective-revision is degenerate; a fixed current criterion is necessary | Everitt, Filan, Daswani & Hutter 2016, "Self-Modification of Policy and Utility Function in Rational Agents," *AGI-16* (Def. 7/9, Thm 10/12, Conclusions; published 2016; primary-source-verified) | *formal antecedent and independent corroboration* — their realistic agent must judge the future by the current $u_t$; the hedonistic agent (revised criterion, nothing fixed above) is the wirehead. This no-go is the AAT-internal, architecture-grounded form, sharper in that the fixed reference must be non-objective and adaptive-substrate-borne |
| A principled vs. stipulated fixed reference | Everitt, Hutter, Kumar & Krakovna 2021, "Reward tampering…," *Synthese* 198 (current-RF / TI-considering) | *formal antecedent* — current-RF is a terminal reference of tower-height one; AAT's persistence bound is *forced and principled* where $R_{\text{now}}$ is a stipulated snapshot |
| Well-defined self-referential value exists | Fallenstein, Taylor & Christiano 2015, "Reflective Oracles" (arXiv:1508.04145 §3/Thm 4.1; primary-source-verified) | *delimited counter-literature, refuted-by-scope* — proves consistent self-*reference* over an *exogenous* payoff; never self-*actuation* groundlessness. It is exactly the primitive-reflective-oracle regime the no-go's premise 2 excludes |
| A self-rewriting agent must preserve fixed goal-content to trust its successor | Yudkowsky & Herreshoff 2013, "Tiling Agents and the Löbian Obstacle" (MIRI) | *convergent adjacent* — the same no-self-trusting-the-revised-top obstruction, reached via Löb; AAT's mechanism is continuation-convention monotonicity instead, distinct, so cited as convergent not borrowed |

**Search Log:**

- 2026-05-17 (*targeted, derivation-driven*): primary sources verified this cycle — Everitt et al. 2016 (Def. 7/9, Table 1, Thm 10/12, Conclusions) and Fallenstein–Taylor–Christiano 2015 (arXiv:1508.04145 §3, Thm 4.1) read directly. No prior-art search has been conducted specifically on whether any prior work derives a self-modification grounding no-go *from the continuation-convention / horizon relativity of a value function* (the apparent AAT-distinctive mechanism), nor on whether "the terminal grounding invariant must be off the objective substrate, on the adaptive substrate" has a prior namer; an Undermind-grade targeted search on those two, plus the active-inference expected-free-energy preference-prior-revision case as a possible instance, is recommended before this segment advances past `draft`.

## Working Notes

- Provenance: derived in the 2026-05-17 self-actuation grounding work trail (`spike-self-actuation-grounding.md` → `spike-wf-strengthening.md` → `spike-wf-class-scoping.md`). The conditional tier (not `exact`), the static-pointwise form of Lemma 1, and the scoped (not universal) phrasing of the no-go are the three findings of the independent review of that trail, applied here; the trail is retained as history per *integration-is-replacement* and this segment is the canonical home.
- Open before `candidate`: (a) the targeted prior-art search above (self-reference-vs-self-actuation distinction; convention-relativity-as-no-go-engine; the adaptive-substrate-grounding statement) — required before advancing past `draft`; (b) whether the single-interface commitment can be made an explicit sub-lemma to lift the scoped no-go toward unscoped; (c) the Pareto / vector-objective retyping (premise 1) as its own scope statement. The tier ceiling stays `conditional` while #der-directed-separation is `stage: draft`.
- Not yet wired into `01-aat-core/OUTLINE.md`: this segment is held at `stage: draft` pending an independent review of the drafted segment before it enters the assembled canon.
- The `#disc-continuity-stance` correction (negotiated = bare persistence floor; morally-continuous = floor + non-revisable continuity clause; stance = choice of terminal non-objective invariant) is the derived consequence stated in Discussion; landing it as an edit to that segment, and filling the reserved `#self-actuated-agent` class boundary as a definition citing this segment, are the remaining integration steps.
