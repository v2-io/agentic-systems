# 29 — result-persistence-condition

*Type: result. Status: exact. Stage: claims-verified. Depends: [def-adaptive-tempo, def-mismatch-signal, result-sector-condition-stability, result-sector-persistence-template].*

## Predictions vs evidence
Predicted: $\alpha > \rho/R$ as headline form. Found: that, plus a **two-condition decomposition** (structural persistence + task adequacy) that I had not anticipated — and that is *the* substantive contribution of this segment.

## **Two-condition decomposition (methodologically important)**
- **Structural persistence:** $\alpha > \rho/R$ (Model D) or $\alpha > n\sigma_w^2/(2R^2)$ (Model S). The machinery's *capacity* to contain mismatch within the model class. Lyapunov-derived.
- **Task adequacy:** $R^* < \|\delta_{\text{critical}}\|$ where $\|\delta_{\text{critical}}\|$ is a domain-specific tolerance. The steady-state mismatch is small enough for the agent's actions to remain useful.

The two are *independent* — an agent can be structurally persistent but task-inadequate. Remedies differ: task inadequacy can be fixed by increasing tempo / reducing disturbance / relaxing tolerance; structural failure requires changing the correction architecture (`#result-structural-adaptation-necessity`). **This is one of the framework's quietly important conceptual moves.**

## Math verification
- Linear operational form: $\mathcal{T} > \rho/\|\delta_{\text{critical}}\|$ (Model D) — exact under $\alpha = \mathcal{T}$, $R = \infty$. ✓
- Linear Model S: $\mathcal{T} > n\sigma_w^2/(2\|\delta_{\text{critical}}\|^2)$. ✓
- Per-dimension: $\mathcal{T}_k > \rho_k/\delta_{\text{critical},k}$ — Lyapunov per dimension. ✓
- All math consistent with `#result-sector-condition-stability`'s derivations (verified there).

## Findings block (line 127+) — strong
The Brief field is genuinely good respectful-pedagogy prose:
> "An adaptive system persists when its correction speed beats the rate at which its world is changing, relative to how forgiving the world is. Below this threshold the system doesn't merely degrade — it loses bounded behavior, the way a balance held just barely beneath a tipping point is qualitatively different from one well above it."

Feynman-criterion target met. Worth noting as an exemplar in §E.

Novelty Claim posture: **synthesis** — Lyapunov machinery is standard; synthesis-with-two-condition-decomposition is the AAT-internal contribution. Aligns with `feedback_math_novelty_recognition.md` discipline. Related Work cites Khalil 2002, Khasminskii 2012, Lyapunov 1892, Rockafellar-Wets 1998, Wiener 1948, Ashby 1956, Conant-Ashby 1970 — proper prior-art attribution.

## Prose-coherence — strong
- "Persistence has a *price*, not just a threshold" (line 115) — connects to `#deriv-persistence-cost`'s information-rate bound. Two-tier framing: threshold + cost.
- Matrix-Loewner reference (line 111) — flags that per-coordinate is unsafe under cross-dimensional correction, matrix-Loewner is canonical.

## Cross-segment consistency
Anchors to `#result-sector-condition-stability`, `#result-sector-persistence-template`, `#deriv-sector-condition`, `#deriv-persistence-cost`, `#result-structural-adaptation-necessity`, `#result-adversarial-tempo-advantage`, `#der-gain-sector-bridge`, `#result-per-dimension-persistence`, `#deriv-matrix-persistence-condition`. Forward-refs to TST `#der-code-quality-as-observation-infrastructure` flagged as cross-component + structurally-motivated-but-not-yet-formally-derived.

## Watch list
- The two-condition decomposition (structural + task-adequacy) is one of the strongest pieces of the framework's contribution. Note positively in §E.
- The Brief field as Feynman-criterion exemplar.

## Next-segment predictions
`#result-structural-adaptation-necessity`. Will state when parametric updates fail and structural change is needed. Status likely `exact`.

## Brief wandering
The two-condition decomposition prevents a category of error in domain transfer — claiming "the team is structurally fine, just needs to work faster" when the actual issue is the domain's tolerance has tightened. The framework's care here compounds: it teaches readers to think about adaptive systems in two-dimensional terms (machinery + domain) rather than collapsing them into a single "is it working?" question.
