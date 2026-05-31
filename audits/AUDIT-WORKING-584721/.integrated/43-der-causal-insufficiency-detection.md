# Reflection 43 — der-causal-insufficiency-detection (Section II row 18)

The F1 no-go strengthening segment per CLAUDE-2.md / MEMORY priming. Substantial.

## §4.2 dependency check

`depends: [result-structural-adaptation-necessity, def-strategy-dag, der-loop-interventional-access, der-causal-hierarchy-requirement, def-pearl-causal-hierarchy, def-causal-information-yield]`. All upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "F1 no-go theorem under CHT, covariance test as unique broadly-available violation." ✓ exactly. Plus much more: explicit $\mathcal W_{L0}^*$ construction for shallow strict-prerequisite case; (S1)–(S5) scope conditions; five-route boundary characterization (a-ε-exploration, b-joint-observability-canonical, c-intermediate-observability, d-structural-priors, e-direct-intervention-on-latent); "diagnostic CIY" extending explore-exploit-deliberate to four-axis; explicit subsumption of aggregate-residual as degenerate special case. **Substantially richer than predicted.**

**2. Cross-segment consistency.** Cross-refs all internally consistent. The "no-go strengthens cascade's load-bearing" framing for orient-cascade step 4c is structurally sharp. The connection to disc-identifiability-floor (Instance 1) is explicit and matches CLAUDE-2.md's meta-pattern characterization. The #der-loop-interventional-access load-bearing role: "without it, the no-go forbids detection entirely; with it, route (b) is operational."

**3. Math verification (at discretion — exercising it on the construction).**

For 2-sibling OR with strict-prerequisite latent C:
- Marginal $\theta_1^* = \theta_C \theta_{1|C}$ ✓ (probability of $A_1$ success unconditionally).
- For $\theta_2^*$: this is $P(A_2 \text{ succeeds} | A_1 \text{ failed})$ under sequential-short-circuit. By Bayes:
  $P(A_2 \text{ succeeds} | A_1 \text{ failed}) = P(A_2 \text{ succeeds}, A_1 \text{ failed}) / P(A_1 \text{ failed})$
  $= [\theta_C \cdot (1 - \theta_{1|C}) \cdot \theta_{2|C} + (1 - \theta_C) \cdot 0] / [1 - \theta_C \theta_{1|C}]$
  (assuming strict prereq: $\theta_{2|\neg C} = 0$)
  $= \theta_C(1 - \theta_{1|C})\theta_{2|C} / (1 - \theta_C \theta_{1|C})$ ✓ matches the segment's formula.

The construction is correct. The CHT (Bareinboim 2022 Theorem 1) does the load-bearing work for the no-go.

**4. What direction next?** Row 19 = `der-observability-dominance`. Per OUTLINE, status:draft. Unobservable strategy edges freezing.

**5. What errors should I now watch for?**
- Future segments treating residual-based diagnostics as primary detectors (it's confirmatory, scales as O(ε)).
- Treating "L0 vs L1" as Level 1 distinguishable.
- Failing the precondition checks (joint observability, credence stabilization, stationarity) and still claiming detection.
- Conflating short-circuit-as-efficiency with diagnostic-blindness — they trade off.

**6. Predictions for next segments.** Row 19 = `der-observability-dominance`. Probably depends on emp-update-gain, def-strategy-dag. The "unobservable edges freeze" claim per OUTLINE.

**7. What would I change?** The five-route boundary characterization is excellent — explicitly maps each scope-condition violation to AAD machinery with detection strength. The "diagnostic CIY" framing extends exploration-exploitation-deliberation to a *four-axis* (adding "diagnose"). This is a richer framework than the three-way disc-exploit-explore-deliberate that CLAUDE-2.md priming flagged.

The "no-go is asymmetric" Working Note (forbids structural detection on-policy; allows parametric learning on-policy) is an important distinction worth surfacing more prominently.

**8. What am I now curious about?**

(a) **Four-axis explore-exploit-deliberate-diagnose.** The fourth "diagnose" axis is added here. disc-exploit-explore-deliberate (forward) was the three-way framing per CLAUDE-2.md. So "diagnose" is the recently-added (this segment's contribution) fourth axis. Whether it propagates into disc-exploit-explore-deliberate or stays here as an extension is worth tracking.

(b) **The no-go's asymmetry.** "On-policy parameter learning is fine; on-policy structural detection is forbidden." This means an L0 agent can converge to perfect L0 conditionals on-policy and *still* be in an L1 world without ever knowing. The structural-vs-parametric split is sharper than I'd appreciated — connects to result-structural-adaptation-necessity at a deeper level.

(c) **The censoring-as-structural-source observation.** "Sequential short-circuit evaluation is what makes on-policy data Level 1 only — it censors the joint outcomes that would constitute Level 2 evidence." This is an elegant structural framing: efficiency-driven short-circuit *forces* the no-go. SA3 ε-exploration is the compromise — pay efficiency cost for diagnostic capability.

(d) **Domain instantiations.** Software deployment / military / investment / organizational examples are concrete and operationally useful. Each names where joint-observability-route is/isn't available.

**9. What new knowledge enabled.** F1 no-go theorem (CHT-anchored). Five-route boundary characterization with AAD-machinery mapping. Covariance test as unique broadly-available detector. Aggregate-residual subsumed as degenerate special case (with O(ε) off-policy scaling). Diagnostic-CIY as four-axis extension. Censoring as structural source of the no-go. No-go asymmetry (parametric OK / structural requires extras).

**10. Should the audit process change?** Continuing.

**11. Outline updates.** Section E (calibration): this is one of the framework's strongest segments — F1 strengthening converts soft observation ("residual collapses") into sharp no-go theorem with explicit construction and five-route escape. Confirms the CLAUDE-2.md framing of "F1 strengthening = strengthen-first repair posture executed." Section D candidate confirmed: this is Instance 1 of the identifiability-floor meta-pattern.

**12. How valuable does this segment *feel* to me?**

**High value, top-decile.** This is one of the framework's strongest pieces. The F1 strengthening converts what was originally a soft observation ("the residual mechanism doesn't work on-policy") into a sharp no-go theorem with explicit observationally-equivalent-world construction. The covariance test is then the unique broadly-available escape, making `#der-loop-interventional-access` structurally load-bearing in both Section I single-agent and Section III composition contexts.

The five-route boundary characterization is operationally useful — practitioners can match their detection capability against the route map. The "diagnostic CIY" four-axis extension (adding "diagnose" to explore-exploit-deliberate) is a substantive framework extension. The censoring-as-structural-source observation is elegant.

Magnitude: top-decile. Type: identifiability-floor instance with explicit theorem-and-escape structure. Engagement: strong; the construction math worked out cleanly; the four-axis extension surprised me.

**13. What does the framework now potentially contribute to the field?**

- **Causal-inference researchers:** concrete identifiability problem with explicit construction of observationally-equivalent worlds. Bareinboim CHT applied to plan-DAG inference.
- **ML practitioners building plan-DAG systems:** sharp warning that residual-based diagnostics for L0 insufficiency don't work on-policy; covariance tests under exploration are the unique broadly-available alternative.
- **AI alignment researchers:** formal handle on "the agent's plan model has hidden correlations." Detection requires loop-interventional-access machinery; without it, structurally impossible.
- **AI-system designers:** five concrete routes to detection with operational tradeoffs (efficiency vs diagnostic capability). Provides a decision-tree for detection-capability investment.
- **Practitioners:** four-axis exploration framework (explore / exploit / deliberate / diagnose) extending the standard explore-exploit tradeoff. The "diagnose" axis is for testing structural assumptions, distinct from testing edge values.
- **Decision theorists working on structural-vs-parametric distinctions:** the no-go's asymmetry (parametric on-policy OK, structural on-policy impossible) sharpens the divide.

**Most distinctive contribution:** explicit identifiability theorem with five-route boundary characterization, plus "diagnostic CIY" as a fourth axis on the explore-exploit-deliberate framework. The framework is operationally clearer than typical ML literature on detection of latent confounders.

## Status-label / discipline

`status: conditional` — appropriate (conditional on (S1)-(S5) scope conditions). Tier-stratification within: no-go exact for shallow, robust-qualitative for general; boundary characterization robust-qualitative; primary detection mechanism robust-qualitative; aggregate residual exact (on-policy collapse) + heuristic (off-policy scaling); detection-to-construction discussion-grade.

`stage: draft` despite depth — recent F1 strengthening per CLAUDE-2.md (2026-04-22), Gate 1/2 may not have re-run.

## Cadence check

Holding. Next: row 19 = `der-observability-dominance`.
