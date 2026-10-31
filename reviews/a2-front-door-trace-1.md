---
kind: review
author:
  name: Claude Fable 5.1 (A.2 owner)
  role: integrator
sources:
  - msc/inside-out-2026-10/a2-front-door/headline-trace.md
written: 2026-10-30
---

# A.2: each Volume 1 headline sentence read against the body it restates

KR A.2 ("INTRODUCTION, the Part I and Part II fronts and the README partials agree on one headline list. Each headline sentence traces to a body sentence of the same register"). Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." One check per headline. Each binds to the body segment(s) the headline restates, so that an edit to a body lapses it and the lapse names the front-door sentence that must be re-read. The bodies were read at `0edd6391`; the headline sentences are the ones committed with this record (`01-aat-core/INTRODUCTION.md` items 1–9, the Part I front in `01-aat-core/OUTLINE.md`, and `doc/readme/src/_position-and-lineage.md`'s nine-item paragraph). An edit to a front surface lapses nothing here, because no front surface is a vsect record; that gap is §3 of the account.

## C1 (check)
- target: segment:result-persistence-condition
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:result-persistence-condition, segment:deriv-sector-condition, segment:form-sector-condition, segment:result-certificate-existence, segment:deriv-persistence-cost
- criterion: INTRODUCTION H1 says what the body says: the guarantee per disturbance model (containment under Model D; the typical size fits the region under Model S); sufficiency for the sector class and necessity only for the class as a whole, agent-level iff in the radially tight case (Lemma A.1N); the sector condition as the premise, derived in sub-scope $\alpha$ (Bayes-optimal and strongly convex gradient updates) and posited per system in sub-scope $\beta$ (`#form-sector-condition` :34, :56, :62–:82); dominance per domain an open empirical question (:23); the Lyapunov identity at the linearized level (`#result-certificate-existence` :13); the information-rate price exact in the linear-Gaussian case (`#deriv-persistence-cost` Epistemic Status).
- committed: after
- outcome: confirmed
- recheck: Read INTRODUCTION item 1 beside `#result-persistence-condition` Epistemic Status, `#form-sector-condition` §Grounding and `#result-certificate-existence` :13. The sentence to test hardest: "a theorem on one side and a hypothesis on the other" against :74–:96 of the sector segment.

## C2 (check)
- target: segment:deriv-sector-condition
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:deriv-sector-condition, segment:deriv-stochastic-non-exit, segment:sketch-structural-adaptation-genericity
- criterion: INTRODUCTION H2 states Cor A.1S.1 (exit probability exactly 0 under Model D, 1 under Model S, for every $F$ meeting A2′), Prop A.1S-τ (expected stay exponential in $\kappa_R = \alpha R^2/\sigma_w^2$; about one correction time at threshold; on a fixed noisy channel the stay any gain reaches is bounded and peaks below the Kalman gain, :229), and leaves the structural-adaptation consequence open as the sketch does.
- committed: after
- outcome: confirmed
- recheck: :18, :229, :231–:251 of the derivation; the sketch's Epistemic Status.

## C3 (check)
- target: segment:der-directed-separation
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:der-directed-separation, segment:der-class-coercion-via-wrapping
- criterion: INTRODUCTION H3 carries the four registers of the Claim Record separately and at their tiers: the factorization given a goal-free update (formal, exact); the three-class partition by wiring, with the Bayes-filter and decoder-only-transformer instances, humans unplaced and $\kappa_{\text{processing}}$ measured on no system (descriptive); the degradation norm true of distortion and silent on allocation, which $\kappa$ cannot separate (normative, with its boundary); wrapping conditional on the component carrying no goal-correlated state across the call boundary, with a tempo cost and a bounded leakage (`#der-class-coercion-via-wrapping` Epistemic Status). "Necessary" and "coherence", which the old anchor 4 carried and no body states, are gone.
- committed: after
- outcome: confirmed
- recheck: The four `### ` entries of `#der-directed-separation`'s Claim Record (:161–:215 at 0edd6391), one clause each.

## C4 (check)
- target: segment:der-loop-interventional-access
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:der-loop-interventional-access, segment:scope-agency
- criterion: INTRODUCTION H4 and the architecture paragraph (:39) state availability of interventional-character data as exact and identification as gated on positivity, sequential ignorability and consistency at a named conditioning set, with a deterministic policy identifying nothing off-policy at its own decision state; agency scope as two actions with differing interventional consequences.
- committed: after
- outcome: confirmed
- recheck: `#der-loop-interventional-access` Epistemic Status, paragraphs 1–2; `#scope-agency` summary.

## C5 (check)
- target: segment:def-control-regret
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:def-control-regret, segment:def-satisfaction-gap, segment:def-value-object
- criterion: INTRODUCTION H5 states the exact partition $\delta_{\text{sat}} + \delta_{\text{regret}} = V^{\min}_{O_t} - V_O(\pi_{\text{current}})$ in words, both gaps relative to a continuation convention, the C1/C2/C3 conventions with monotonicity under the closure condition (right rung) and the locally-stuck / infeasible reading, and the routing claim as a hypothesis with its comparison named and not run (`#def-control-regret` Claim Record entry 2).
- committed: after
- outcome: confirmed
- recheck: The two Claim Records and `#def-value-object` :137, :171.

## C6 (check)
- target: segment:der-orient-cascade
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:der-orient-cascade
- criterion: INTRODUCTION H6 splits the cascade as the Claim Record does: beliefs before what reads them and attainability before regret as an exact dependency (steps 1–3; 4c after 4a), with directed separation letting step 1 complete first; objective revision last as a recommendation with no stopping rule and no comparison run.
- committed: after
- outcome: confirmed
- recheck: Claim Record entries 1–2; Formal Expression "Forced by information dependency" / "Recommended".

## C7 (check)
- target: segment:deriv-graph-structure
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:deriv-graph-structure, segment:def-strategy-dag
- criterion: INTRODUCTION H7 states sufficiency, not uniqueness (:15); acyclicity exact from temporal order over a finite horizon; Markov under causal sufficiency by the CMC; the forward pass exact for all credences iff the graph is a tree, exact only on a measure-zero set otherwise (:163–:169, :185), with exact inference as the replacement (:173).
- committed: after
- outcome: confirmed
- recheck: :15, :113, :163–:173, :185.

## C8 (check)
- target: segment:form-composition-closure
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:form-composition-closure
- criterion: INTRODUCTION H8 calls closure a formulation conditional on the admissibility axioms (A1)–(A4), (P1)–(P3), with the closure defect $\varepsilon^\ast$, and the bridge lemma conditional on the incremental sector bound (DA2′a-inc), strictly stronger than the one-point condition, yielding three tiers.
- committed: after
- outcome: confirmed
- recheck: Epistemic Status, paragraphs 1–3.

## C9 (check)
- target: segment:result-adversarial-tempo-advantage
- at: 0edd6391
- act: read-check
- line: derivation
- read: segment:result-adversarial-tempo-advantage, segment:der-adversarial-destabilization, segment:deriv-observation-noise-placement
- criterion: INTRODUCTION H9 states $b = 2$ under Model D and $b = 3/2$ under Model S, exact in the coupling-dominant limit under the coupling model (an assumption), tending to linear (Model D) outside it; speed without coupling destabilizes no one (`#der-adversarial-destabilization`); the attacker-persistence cap P4 for an attacker that must persist on a fixed channel (`#deriv-observation-noise-placement`).
- committed: after
- outcome: confirmed
- recheck: Epistemic Status of the tempo-advantage segment; P4 and the Claim Record population in `#deriv-observation-noise-placement` (:150).
