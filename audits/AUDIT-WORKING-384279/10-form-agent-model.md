# 10 — form-agent-model

*Type: formulation. Status: robust-qualitative. Stage: deps-verified. Depends: [def-agent-environment, def-observation-function, def-chronica].*

## Predictions vs evidence
Predicted: $M_t = \phi(\mathcal{C}_t)$ with completeness commitment. Found: exactly that, with $\mathcal{M}$ as model space and $\phi: \mathcal{C}^\ast \to \mathcal{M}$ as the compression map.

## Cross-segment consistency
Forward-refs `#def-model-sufficiency`, `#form-information-bottleneck`, `#def-mismatch-signal`, `#emp-update-gain`, `#def-agent-spectrum`. All consistent with the OUTLINE forward direction.

## Math verification
- $M_t = \phi(\mathcal{C}_t)$. ✓
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ — uses Kleene-star to denote "set of all finite chronicae of any length." Not explicitly in NOTATION.md but standard. Minor note.

## Prose-coherence
Heavy preamble↔Discussion duplication. Lines 14-18 (preamble) and lines 37-43 (Discussion) carry largely the same content:
- preamble: "many-to-one compression... agent-agnostic about realization (Kalman filter / RL / developer / LLM)... completeness assumption..."
- Discussion: same three points re-stated.

This is the strongest example of preamble-Discussion duplication in segments 1-10. Not a finding by itself (FORMAT.md cadence permits this), but observable.

## Watch list
- Honest *robust-qualitative* status label — the formulation is "robust" (any agent that conditions actions on retained info can be described this way) but the *specific* commitment to a complete compressed $M_t$ is a modeling choice. Label matches content. ✓
- "Degenerate cases" (line 43) flag PID controllers as too impoverished. The framework will need to reconcile PID with Section I's adaptive machinery elsewhere — PIDs are common control elements but Section I's claims rest on $M_t$ being rich enough for prolepsis.

## Next-segment predictions
`#form-information-bottleneck`. Will introduce Tishby's IB framework as the optimal compression criterion. Status likely robust-qualitative. Will probably formalize $\min I(M_t; \mathcal{C}_t) - \beta I(M_t; \Omega_{t+1})$ or similar.

## What I'd change
Reduce preamble-Discussion duplication. Either preamble carries the prose narrative and Discussion is bullets-only, or Discussion is the prose narrative and preamble is one-paragraph orientation. Not finding-worthy.

## Wandering thoughts

**On the agent-realization-agnostic framing.** "$M_t$ is the epistemic substate" with no commitment to representational form is the right move for a framework that wants to span Kalman filters through LLMs. The cost is that all the realization-specific machinery (Bayes' rule for Kalman, transformer attention for LLMs) lives at the realization level rather than at the framework level. The benefit is that framework-level claims (persistence, gain, tempo) apply across realizations.

**On the PID-as-blind-seeker observation.** A PID controller's $M_t$ is "the error signal and its history (integral, derivative)" — meaning $\phi$ projects $\mathcal{C}_t$ down to a 3-dimensional state. That's a *very* aggressive compression. The framework will claim Section I results apply to PIDs (control-theory is in scope) but here it's flagged as "too impoverished to support the adaptive dynamics of Section I." That's a tension: either PIDs are in scope (per cross-domain table in README-auditor) or they're outside (per this segment's degenerate-case label). The resolution probably lives in `def-model-sufficiency` — PIDs satisfy adaptive-scope but their model class fitness is low, so Section I applies in the *degraded-rate* sense rather than the full-power sense. Worth watching.
