# Verdict: status ledger, value-direction, gated landings

**Spike.** `spikes/fight/` — Φ(fight) adversarial-embodied prompt vs AAT's deferred coupled-adversarial machinery.
**Status.** Exploratory; **not promoted**; no segment edited. All candidate landings author-gated. Documented dead-end recorded (guardrail).

## 1. The honest one-paragraph result

Φ(fight) has no research output to mine (verified: empty GitHub/HuggingFace, a USD 15K *proposal* to build a benchmark that does not exist, withheld-under-review claims). Used strictly as an ideation prompt per Joseph's instruction, the adversarial-multi-agent-embodied problem-class did two useful things against AAT's *own* machinery. (1) It refuted a plausible-looking guess — environment-mediated adversarial coupling is **not** a new directed-separation locus; it is the selection-not-processing case `#der-directed-separation` already scopes — and in doing so pointed precisely at the closed-loop / joint-best-response adversarial extension AAT defers in three named places, and a hypothesis that was then **spiked to resolution** (`03`): the energy budget converts `#der-adversarial-destabilization`'s discussion-grade Effects-Spiral corollary to **conditional-derived** — but *not* by formalizing its unspecified $\gamma_A(\lVert\delta_B\rVert)$ leg; by making that leg **unnecessary**. A hard-budget target self-depletes to certain finite-time destabilization against even a constant-effectiveness adversary, via the **decaying-$\alpha$ instantiation of `#result-sector-persistence-template`** (existing exact machinery, the `#schema-strategy-persistence` slot), conditional on two introduced resource axioms AAT does not currently carry, and explicitly *orthogonal to* (not a resolution of) the deferred joint-Jacobian problem. (2) It came back with a verified, strengthened floor-theoretic statement: for trained self-play policies the behavioral leakage estimator's counterfactual-goal precondition fails, so by the identifiability floor's Sylvester irreducibility the contamination subspace is escapable only by a rank-augmenting *mechanistic* channel, never by better behavioral metrics — which both explains Φ's method choice and makes the leakage-locus spike's Open-Q3 empirically posable. **Value-direction throughout is reversed: AAT is the lens; Φ is, at most, a future measurement substrate. Connection 2's foundation is itself an unlanded 2026-05-18 spike.**

## 2. Status ledger

| Item | Tier | Disposition |
|---|---|---|
| C1 guess: adversarial environment-mediation is a new coupling locus | **refuted** | documented dead-end (guardrail §4); do not re-attempt |
| C1: Φ regime = AAT's deferred closed-loop / joint-best-response adversarial extension | **verified mapping** | context for `#der-adversarial-destabilization` / `#deriv-strategic-composition`; not landed |
| C1: energy-bounded Effects-Spiral = decaying-$\alpha$ template instantiation (the *reduction*) | **exact-flavored, conditional on resource axioms** (`03` §5) | LANDED → `#der-resource-bounded-destabilization` + `#form-resource-budget` (exploratory branch) |
| C1: self-depletion → certain finite-time destabilization vs constant-$\gamma_A$; segment's open leg made *unnecessary* | **conditional-derived** (`03` §4) | strengthen-before-soften succeeded, narrower+sharper than the guess |
| C1: energy bound is orthogonal to (does not resolve) the deferred joint-Jacobian problem | **verified relationship** | guardrail — do not read it as cracking the symmetric equilibrium problem |
| C1: (A-cost),(A-gate) resource axioms | **introduced, not derived** | AAT has no resource structure (`#def-strategy-dimension` open) |
| C2 naïve "behavioral is blind" | **rejected** | superseded by §2 precise statement |
| C2 leakage confined to $\ker\mathcal I_\tau$, covariance-invisible | **exact/robust-qual — inherited, pre-landing** | belongs to `spike-leakage-locus-2026-05-18.md`; not re-derived here |
| C2: $\hat\kappa$ counterfactual precondition fails for self-play policies → mechanistic = the floor's rank-augmenting channel | **verified bridge** | context for the leakage spike's Open-Q3/Q4; not a standalone landing |
| C2: Φ-Arena could test exploit-circuit null-space concentration / M4-middle routing | **hypothesis (falsifiable, untested)** | no substrate exists; recorded as a posable prediction |

## 3. Candidate landings (author-gated — listed, not executed, not folded silently)

1. **Resource-structure extension — LANDED 2026-05-19 as an exploratory off-spine branch** (Joseph elected to open the axis). Two segments: `#form-resource-budget` (`type: formulation, status: conditional` — minimal $(\mathcal B_t, c, \psi)$ structure with posits (A-cost)/(A-gate), addressing `#def-strategy-dimension`'s open resource gap) and `#der-resource-bounded-destabilization` (`type: derived, status: conditional` — `03` §4 self-depletion result + §5 tiers, the decaying-$\alpha$ slot of `#result-sector-persistence-template`, structural parallel to `#schema-strategy-persistence`). Registered in `01-aat-core/OUTLINE.md` Appendix A (Stage `exploratory`); NOTATION.md updated; no spine segment depends on either. Strengthen-before-soften succeeded (discussion-grade → conditional-derived via a reduction to existing exact machinery, *not* by formalizing the unspecified term — by removing the need for it). Open follow-ons (regenerative regime; closed-form $\tau$) in the `der-` segment's Working Notes. CHANGELOG 2026-05-19.
2. **One-line guardrail in `#der-directed-separation` Working Notes** — only if Joseph judges the "environment-mediated coupling is a new locus" misconception likely to recur across agents; otherwise the §4 dead-end below suffices.
3. **C2 contributes context, not a landing** — it is downstream of `spike-leakage-locus-2026-05-18.md` resolving its own Open-Q3 (M4-middle / strategic-self-coupling reconciliation) and Open-Q4 (new floor instance vs re-description). The contribution is that both are empirically posable on an adversarial-embodied substrate; that is input to those author-decisions, not a resolution.

## 4. Documented dead-end (guardrail for future agents)

"Adversarial environment-mediation (an opponent best-responding to the target's strategy through the shared environment) is a *new* directed-separation coupling locus / a way an internally-Class-1 agent's directed separation fails." **Refuted.** `#der-directed-separation`'s Scope Condition makes directed separation about the *processing* of the realized event, not its *selection*; an adversary warping the event distribution is the selection channel, already in scope. The live question is not a new locus but the *closed-loop treatment of the (correctly exogenous-looking) disturbance* — i.e. the joint-best-response / Effects-Spiral extension AAT already defers. Do not re-derive the refutation; build on §2 of `01`.

## 5. Relationship to existing open items (so this does not duplicate them)

- `#der-adversarial-destabilization`: Effects-Spiral $\gamma_A(\lVert\delta_B\rVert)$ unformalized; joint-best-response deferred to `#deriv-strategic-composition`. — *C1 §3 proposes the missing coupling variable for the scoped energy-bounded case; it does not claim the general result.*
- `#disc-adversarial-coupling-pressure` Working Notes: κ-arms-race repeated game "would land as an appendix segment if pursued." — *C1 §2 notes Φ's matchup design is its empirical realization; no new game-theory derived here.*
- `spike-leakage-locus-2026-05-18.md` §9 Open-Q3, Open-Q4. — *C2 §3 shows both are empirically posable on an adversarial-embodied substrate; the spike's author-decisions are untouched.*

Nothing here is promoted. The two threads are reasoning trails; the only forward-going asset is candidate landing #1 (the energy-bound Effects-Spiral strengthening), explicitly Joseph-gated.
