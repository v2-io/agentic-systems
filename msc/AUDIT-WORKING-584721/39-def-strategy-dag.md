# Reflection 39 — def-strategy-dag (Section II row 14)

Substantial segment with the Correlation Hierarchy. Walking the prompts.

## §4.2 dependency check

`depends: [scope-and-or, post-causal-structure, def-pearl-causal-hierarchy, form-objective-functional, def-strategy-dimension]`. All upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "Correlation Hierarchy (L0/L1/L1'/L2), causal-efficacy-credence framing." ✓ exactly. Plus much more: the "Why a DAG" preamble (CMC-derived sufficiency direction, necessity open); the strategy-layer exactness contract; rootedness and source constraints; Regime A/B/C identification; leaf base credence; well-formedness constraint; strict-vs-soft-prerequisite distinction with the factor-above-correlation principle; L1' mixture form with Cramér-Rao-refutation under unobservable C; edge-credence dual coordinates (probability-space vs log-odds, Fisher-equivalent). **Substantially richer than predicted.**

**2. Cross-segment consistency.** Extensive cross-refs all internally consistent. The Correlation Hierarchy with the L1'-under-observable-C-only refutation is the recently-added (per CLAUDE-2.md) Cramér-Rao-floor identification analysis. Connects to disc-identifiability-floor's Instance 2. The edge-credence dual-coordinates subsection is the recently-added (2026-04-23) log-odds-as-natural-parameter content from deriv-edge-update-natural-parameter. Recent additions propagate cleanly.

**3. Math verification (at discretion — exercising it on the example).** The strict-prerequisite OR-alternatives example: $\theta_C = 0.8$, $\theta_{1|C} = 0.9$, $\theta_{2|C} = 0.7$, $\theta_{i|\neg C} = 0$.

Marginals: $\theta_1 = \theta_C \theta_{1|C} = 0.72$, $\theta_2 = \theta_C \theta_{2|C} = 0.56$.

L0 estimate: $1 - (1-0.72)(1-0.56) = 1 - 0.28 \times 0.44 = 1 - 0.1232 = 0.8768$. ✓ matches segment's "0.877."

Actual: $P(A_1 \cup A_2) = P(\cdot|C)P(C) + P(\cdot|\neg C)P(\neg C)$. Given C: $1 - (1-0.9)(1-0.7) = 0.97$. Given $\neg C$ with strict prereq: $0$. Actual: $0.8 \times 0.97 + 0.2 \times 0 = 0.776$. ✓ matches segment.

L0 overestimate: $0.877 - 0.776 = 0.101$. The bias has magnitude $\rho = \text{Cov}(A_1, A_2) > 0$ from shared C. Confirms the framework's claim about OR-node optimism. ✓

Math is correct.

**4. What direction next?** Row 15 = `def-satisfaction-gap`. The diagnostic-core segment. Then def-control-regret.

**5. What errors should I now watch for?**
- Future segments treating L0 as if always correct.
- Use of "AND/OR propagation" without specifying Correlation-Hierarchy level.
- Soft facilitators treated as strict prerequisites (different L1 vs L1' construction).
- L1' results applied without C-observability verification.
- "Naive L1" (common cause as parent of OR-siblings without restructuring) — same overestimate as L0.

**6. Predictions for next segments.** Row 15 = `def-satisfaction-gap`. Likely depends [def-value-object, form-objective-functional]. Definition of $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$.

**7. What would I change?** The "Why a DAG" preamble's distinction between *sufficiency* (derived from CMC) and *necessity* (open stronger result) is appropriately scoped. The strict-vs-soft-prerequisite distinction with the explicit "naive L1 fails" example is concrete and pedagogically useful.

The dual-coordinates (probability-space vs log-odds) subsection is good — names the operational distinction (AND/OR propagation in probability space; gradient updates in log-odds; Fisher-equivalent for moment-parameter results).

**8. What am I now curious about?**

(a) **The naive-L1-fails framing.** "Common cause as parent of both alternatives, alternatives remain OR-siblings" gives the *same* overestimate as L0. The correct construction is $G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}} = \text{OR}(A_1, A_2)$. **Factor above the correlation, not in parallel with it.** This is a real engineering insight that practitioners would otherwise miss.

(b) **L1' identifiability obstruction under unobservable C.** Cramér-Rao floor on per-conditional decomposition: per-trial Fisher matrix is rank 1 rather than rank $2K+1$, so no unbiased online estimator on the joint conditional vector admits sector parameter $\alpha > 0$. This is a sharp no-go: the agent must either augment C-observability (preferred), use L2 explicit conditioning, or fall back to L0-on-marginals.

(c) **The detectability claim.** "An agent at L0 can detect causal insufficiency from its own data: persistent overestimation of plan success after edge credences have converged." Localization via pairwise covariance among sibling edges. Operationally significant — gives the agent a self-diagnostic protocol.

(d) **The four-decision-tree** for handling each common cause: L1 strict / L1' soft observable / L2 soft unobservable / fallback to L0-on-marginals. This is a clean operational framework that ML literature mostly lacks.

**9. What new knowledge enabled.** Strategy DAG with derived structure (CMC). Correlation Hierarchy four-level. Strict-vs-soft-prerequisite. L1' mixture form. Cramér-Rao-anchored refutation. Edge-credence dual coordinates. Naive-L1-fails caveat. Causal-insufficiency self-detection protocol.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** Section E (calibration): the Correlation Hierarchy with explicit observability check is one of the framework's strongest scope-honesty moves. Section D candidate already covered: this is the canonical instance of the "identifiability-floor" pattern at the strategy layer.

**12. How valuable does this segment *feel* to me?**

**High value, top-decile.** The Correlation Hierarchy with strict-vs-soft-prerequisite distinction and observability check is one of the framework's clearest scope-honesty moves. The L0 → L1 → L1' → L2 hierarchy with explicit identifiability analysis at each level is structurally sharp.

The factor-above-correlation principle (with the naive-L1-fails counterexample) is operationally important — the kind of insight that turns "use L1 augmentation" from doctrine into actionable engineering guidance.

The Cramér-Rao-anchored refutation under unobservable C is sharp — most ML literature handwaves about latent variables; AAD says "here's exactly when you can model them and when you can't."

Magnitude: top-decile. Type: substantial structural definition with extensive scope-honesty machinery. Engagement: strong; the example-math check confirmed the framework's specific numerical claims; the four-decision-tree is operationally satisfying.

**13. What does the framework now potentially contribute to the field?**

- **Plan-DAG designers:** four-level correlation hierarchy with explicit construction principles. The factor-above-correlation principle is concrete engineering guidance.
- **Causal-inference researchers:** strict-vs-soft-prerequisite distinction with Cramér-Rao-anchored refutation under unobservable common cause. ML literature treats these uniformly; AAD partitions explicitly.
- **AI alignment researchers:** formal handle on "the agent's causal model has unmodeled common causes." The dominant case in real-world AI deployment is L0 with hidden correlations.
- **Practitioners:** four-decision-tree for handling each common cause. L1 strict / L1' soft observable / L2 soft unobservable / L0-on-marginals fallback.
- **RL theorists:** the persistent-overestimation-as-detection signal connects causal-sufficiency violations to detectable agent behavior.
- **Edge-credence parameterization unification:** probability-space and log-odds dual coordinates with Fisher-equivalence for moment-parameter results.

**Most distinctive contribution:** explicit observability-check at L1' with Cramér-Rao-anchored refutation under unobservable common cause. This converts "can the agent model latent variables?" from a vague modeling-discretion question into a formal identifiability question with a sharp answer.

## Status-label / discipline

`status: conditional` — appropriate (conditional on causal sufficiency for L0; on observability for L1'; etc.). Tier-stratification within: DAG structure derived; AND/OR parameterization formulation choice; L0 results exact under causal sufficiency; L1' results conditional on observability; L1' under unobservable C structurally refuted.

`stage: draft`.

## Cadence check

Holding. Next: row 15 = `def-satisfaction-gap`.
