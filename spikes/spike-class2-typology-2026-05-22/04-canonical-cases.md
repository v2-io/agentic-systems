# 4. Canonical Cases — Placement in the Typology

The typology's load-bearing-ness depends on whether it carves familiar phenomena distinctly. This file places known coupling phenomena into the (stage × source × form) parameterization and checks: (i) do they get distinct cells? (ii) are the cells empirically distinguishable? (iii) does each implied repair regime make sense?

## 4.1 The placement table

| Phenomenon | Stage(s) | Source | Form | Repair regime (per Results 1–6) |
|---|---|---|---|---|
| Goal-directed attention | (P0) Selection only | $O$ or $\Sigma$ | — | None needed — formally allowed (`#der-directed-separation` scope condition) |
| Confirmation bias (classical) | P2 (likelihood) | $M$-self (prior amplification) | Process (multiplicative) | $M$-self not in $\{O, \Sigma\}$ source space — special case, see §4.3 below |
| Motivated reasoning (identity-driven) | P1 (featurization) + P2 (likelihood) | $O$ | Content for moderate; Process for strong-identity-binding | W₂ for moderate; W₁ + identity-suppression for strong |
| Sunk-cost commitment | P3 (aggregation) | $\Sigma$ | Process (multiplicative — $K(\Sigma)$ gain modulation) | W₁ with $\Sigma$-channel suppression; admits belief-strategy attractors (Result 4) |
| Identity-protective consolidation | P4 (consolidation) | $O$ | Process (compositional — different storage decisions) | W₁ + storage-protocol externalization |
| Frame coupling | P1 (featurization) | $O$ + $\Sigma$ | Process (compositional — different feature schema) | W₁ + featurization-protocol externalization; multi-frame composition |
| Wishful thinking (general) | P3 (aggregation) | $O$ | Content for mild; Process for strong | W₂ for mild; W₁ for strong |
| Goal-shaped affect / urgency | (P0) bypasses cascade | n/a (not stage-coupling proper) | n/a | External pacing scaffolding (`#disc-adversarial-coupling-pressure` affect mechanism) |
| Attention-mediated LLM coupling | P1 (featurization) — universal across stages in monolithic case | $O$ + $\Sigma$ (prompt-mixed) | Process (compositional — attention re-weights all features) | Full Class-3 — requires W₁ wrapping construction; no stage repair available without internal access |

The table partitions the phenomena into operationally meaningful cells. Several observations follow.

## 4.2 The typology distinguishes phenomena the scalar collapses

A scalar $\kappa_{\text{processing}}$ would lump all of moderate motivated reasoning, sunk cost, and wishful thinking together as "Class 2 with $\kappa$ around 0.3" (illustrative). The typology distinguishes them:

- Moderate motivated reasoning sits at P1+P2 / $O$ / content — wrappable by W₂ at the response-structuring layer.
- Sunk cost sits at P3 / $\Sigma$ / process — wrappable by W₁ with $\Sigma$-suppression, and additionally diagnostic for belief-strategy attractors.
- Wishful thinking (P3 / $O$ / content) is wrappable by W₂ but does not produce attractors.

These have *different repair recommendations* — recommendations the scalar cannot generate.

## 4.3 The $M_t^{\text{prior}}$ self-coupling case — confirmation bias proper

Classical confirmation bias is the phenomenon "prior belief shapes how new evidence is processed." Formally:

$$P(z \mid e) \propto P(e \mid z) \cdot P(z)$$

is *standard* Bayesian update; prior shapes posterior trivially. The pathological case is when $P(e \mid z)$ — the likelihood — depends on the prior $P(z)$ in a way that *amplifies* the prior. E.g., when the agent's interpretation of $e$ is itself biased by what the agent already believes, beyond what Bayesian conditioning allows.

This is structurally $M_t^{\text{prior}} \to f_M$ rather than $G_t \to f_M$. Per the typology's source space $R \subseteq \{O, \Sigma\}$, it is *not* a sub-type of Class 2 in the parameterization above. It is a separate failure mode.

Is it Class 2 at all? Per `#der-directed-separation`'s formal condition, $f_M(M_{\tau^-}, e_\tau)$ has $M_{\tau^-}$ as an argument; the conditional-independence statement is $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$. So $M_{\tau^-}$-dependence is *allowed* in Class 1. Classical confirmation bias's $M$-self-amplification is therefore *not* a violation of directed separation — it is within Class 1 and is a *quality-of-update* concern rather than a goal-coupling concern.

However: when the prior $M_{\tau^-}$ has been historically shaped by $G$-coupled updates (i.e., the *trajectory* of prior $M$-states has been corrupted by goal-coupling), then the apparent "$M$-self-amplification" carries cumulative $G$-content. This is the **trajectory-coupling** case: each step's coupling is small, but the cumulative effect on $M_t^{\text{prior}}$ creates effective $G$-content in the prior that confirmation-bias-style processing then amplifies.

This is a real refinement, distinct from per-step Class 2 coupling. It deserves its own treatment, possibly as a separate sub-typology axis (the "temporal grain" axis mentioned in §1.5). For this spike, recorded as out-of-scope and flagged for follow-on.

## 4.4 The affect/urgency case — not stage-coupling

`#disc-adversarial-coupling-pressure` names "affect / urgency" as a mechanism that "bypasses deliberate $f_M$; the agent acts before $M_t$ updates resolve." This is *not* a $G \to f_M$ coupling — it is a *cascade-bypass* that prevents $f_M$ from running cleanly.

Per the typology, this sits outside the (S, R, F) parameterization. It is a separate operational regime: time-pressure-induced under-deliberation. Its repair is *not* wrapping — it is *external pacing* (forcing the orient cascade to run before action), which is the institutional-scaffolding side of `#disc-adversarial-coupling-pressure`.

Operational note: the affect/urgency case may *interact* with Class 2 sub-types — under time pressure, an agent with mild $O$-source content-coupling at P3 may exhibit much stronger effective coupling because the cascade-correction mechanism is not given time to run. This is an *interaction effect*, not a stage placement.

## 4.5 The frame-coupling case

"Frame coupling" — the categorical structure of $M_t$ being shaped by goals — is the strongest form of P1 (featurization) process-coupling. A goal "find the bug in this code" frames the input as a debugging task; the *features extracted* are bug-relevant features. A goal "review this code for style" frames the same input differently.

Within the typology: stage P1, source $O$ or $\Sigma$, form *compositional process*. The featurization map $\phi(\cdot; G)$ has functionally different outputs under different goals — not additively decomposable.

Repair: W₂ insufficient (the response structure differs across goals; there is no debiasing transformation). W₁ possible if the wrapper can call the featurization stage with a "neutral frame" goal, then re-process the output with goal-specific aggregation. This is the *multi-frame composition* pattern operational in some Class 2 systems (e.g., having the same model produce a debugger's-eye view AND a stylist's-eye view AND a security-auditor's-eye view, then composing).

Operationally: frame-coupling is *useful* (the agent attends to what matters), and its "repair" is not removal but *explicit multi-framing*. This is the case where the structural typology recommends *not* coercing to Class 1 but rather *managing* the frame-coupling intentionally.

## 4.6 Transformer-LLM attention as the "fully entangled" reference case

The canonical Class 3 case from `#der-directed-separation`: transformer LLMs.

Placement under the typology: the attention mechanism processes all input tokens (including the goal-bearing prompt tokens) jointly, producing token representations that are simultaneously goal-conditioned and observation-encoded. There is no functional separation between $\phi$ (featurization), $\lambda$ (likelihood), and $\alpha$ (aggregation) in the monolithic attention computation — they are fused into a single forward pass.

In the typology: $S = \{P1, P2, P3\}$ (perhaps not P4 — the storage step, in an LLM with external memory, may be separable), $R = \{O, \Sigma\}$ (the prompt mixes both), $F \equiv$ process (compositional — attention weights are nonlinear in goal-tokens).

This is structurally the cell *closest to* the fully-entangled corner $\{P1, P2, P3, P4\}, \{O, \Sigma\},$ process. P4 may or may not be coupled depending on the agent's memory architecture.

So Class 3 (monolithic LLM) is at the corner of the parameterization, *with the optional P4 cell depending on architecture*. This is internally consistent: the typology recovers canon at its endpoints.

## 4.7 What the placements check

(a) The cells the typology produces are distinguishable. The phenomena fall into separate cells; same-cell phenomena have similar dynamical signatures.

(b) Each cell's recommended repair regime is operationally sensible. Moderate motivated reasoning admits debiasing; strong sunk-cost requires structural intervention; frame coupling admits multi-framing not coercion.

(c) The boundary cases (M-self coupling; affect/urgency; frame coupling) are recognized as *outside* or *adjacent to* the core (S, R, F) parameterization, with honest scope statements.

(d) The Class 3 monolithic LLM case lands at the parameterization's structural corner.

The typology survives this check. Genuine sharpening points:

- The form (content vs process) distinction is the most operationally important — it determines wrappability.
- The source ($O$ vs $\Sigma$) distinction is the most dynamically important — it determines whether attractors are possible.
- The stage axis is the most architectural — it determines where repair must be applied.

These are three different operational outputs from the typology, each correlating with one of the three axes. That correlation is what makes the typology load-bearing rather than ornamental.
