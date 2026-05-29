# 17 — der-action-selection

*Type: derived. Status: exact. Stage: deps-verified. Depends: [form-agent-model, der-recursive-update].*

## Predictions vs evidence
Predicted: $a_t = \pi(M_t)$ derivation from completeness, second of "two derivations from completeness." Found: exactly that, plus substantial *action fluency* elaboration (implicit vs explicit action selection).

## Math verification
- $a_t = \pi(M_t)$ deterministic; $a_t \sim \pi(\cdot \mid M_t)$ stochastic. ✓
- Section II lift to $a_t = \pi(M_t, G_t)$ via $X_t = (M_t, G_t)$ completeness. ✓
- Action-fluency formal characterization: high fluency iff $\Delta\eta^*(\Delta\tau) \approx 0$. ✓ (To verify when I reach `#der-deliberation-cost`.)

## Prose-coherence
- Status `exact` in frontmatter matches body Epistemic Status "*Exact*" — **consistent tagging**, contrast with der-recursive-update where they diverged.
- Line 39 marks the implicit/explicit fluency content as "*discussion-grade* — qualitative properties that follow from the formalism but are not formally derived as propositions" — multi-tier honesty within an `exact`-status segment.
- Domain-instantiations table (Kalman+LQR / RL / PID / Boyd OODA / Organism / Organization / Software developer) is rich and pedagogically useful.

## Cross-segment consistency
Forward-refs `#der-deliberation-cost`, `#def-model-sufficiency`, `#result-persistence-condition`, `#def-pearl-causal-hierarchy`, `#def-agent-spectrum`, `#der-directed-separation`, `#form-complete-agent-state`. All coherent.

## Watch list
- The within-segment multi-tier tagging (exact-overall + discussion-grade-for-sub-claims) is a *positive* pattern. Worth highlighting as something the framework does well in §E.
- Cross-section pointer "Section I form is the special case $G_t = \emptyset$" (line 35) cleanly handles the future-section forward-ref.

## Next-segment predictions
`#def-mismatch-signal`. Will introduce $\delta_t = o_t - \hat o_t$ formally. Probably definition + axiomatic. NOTATION.md has $\delta_t \in \mathcal{O}$ and $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ as the score-function variant.

## What I'd change
Nothing structural — clean segment with good multi-tier honesty.

## Brief wandering
The implicit/explicit distinction (action fluency) is a meaningful pedagogical addition that's not strictly *part of the derivation* — but it's important for downstream connections (OODA loop, System 1/2, RL exploit/explore, etc.). The framework's choice to fold it into der-action-selection rather than break it into a separate segment seems right: the *concept* of action fluency is bound to action selection, and separating it would create a thin segment + dependency chain that doesn't add value.
