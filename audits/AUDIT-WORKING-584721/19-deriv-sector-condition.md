# Reflection 19 — deriv-sector-condition (Appendix A; first cited from row 22)

The load-bearing Lyapunov machinery for Section I's persistence claims. Reading in-context per the §4.2 appendix exception.

## §4.2 dependency check

`depends: [def-adaptive-tempo, def-mismatch-signal]`. Both upstream in OUTLINE walk. **No backward-dep finding.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** I predicted: "Lyapunov derivations for Model D and Model S, Prop A.1, Prop A.1S, Prop A.2, and the fluid-limit bridge." Verification: ✓ on Props A.1, A.1S, A.2. ✗ on the fluid-limit bridge — that's deferred to deriv-discrete-sector-condition.

**Surprise:** The segment's content is much richer than "three Lyapunov proofs." It carries:

- The sub-scope α/β partition with explicit operator-family classification (Rockafellar 1970 / Bauschke-Combettes 2017 monotone-operator lineage). The proximal / cocoercive / firmly-nonexpansive identifications are concrete and useful.
- Region-aware Prop A.1S via stopping-time localization at $\tau_R$ (Khasminskii 2012 ch. 5) — recently-added piece per CLAUDE-2.md, lands cleanly here.
- Structural Lipschitz-floor scope-exit for rule-based/discontinuous correction functions, with explicit hybrid-dissipative framework reference (van der Schaft-Schumacher 2000) — recently-added per CLAUDE-2.md (2026-04-24 Tier 1).
- "Matched vs forced" distinction for the Lyapunov quadratic coordinate (matched to the candidate, not Cauchy-FE-forced) — connects to disc-additive-coordinate-forcing.
- Derivation-audit table per FORMAT.md O-BP14 convention.

**2. Cross-segment consistency.** Cross-references all clean. The recently-added structural moves (PI / monotone-operator lineage / stopping-time localization / structural Lipschitz-floor) all propagate here as expected per CLAUDE-2.md priming.

**3. Math verification (at discretion — exercising it because this is the load-bearing proof).**

Prop A.1 (Model D, deterministic):
- $\dot V = \delta^T(-F + w) = -\delta^T F + \delta^T w$
- A2': $\delta^T F \geq \alpha\|\delta\|^2$ ⇒ $-\delta^T F \leq -\alpha\|\delta\|^2$
- Cauchy-Schwarz: $\delta^T w \leq \|\delta\|\|w\| \leq \rho\|\delta\|$
- So $\dot V \leq -\alpha\|\delta\|^2 + \rho\|\delta\| = -\|\delta\|(\alpha\|\delta\| - \rho)$
- $\dot V < 0$ iff $\|\delta\| > \rho/\alpha$, giving $R^* = \rho/\alpha$. ✓
- Boundary-inward at $\|\delta\| = R$: $\dot V|_{R} = -R(\alpha R - \rho) < 0$ when $\alpha R > \rho$. ✓ Positive invariance of $\mathcal B_R$.

Prop A.1S (Model S, stochastic):
- $dV = \delta^T(-F)dt + \delta^T \sigma_w dW + \frac{1}{2}\sigma_w^2 n\, dt$ via Itô.
  - Itô correction: for $V = \frac{1}{2}\|\delta\|^2$, $\nabla^2 V = I$, $\text{tr}(\sigma_w^2 I \cdot I) = n\sigma_w^2$, halved gives $\frac{n\sigma_w^2}{2}$. ✓
- Expectation: $d\mathbb E[V]/dt \leq -2\alpha \mathbb E[V] + \frac{n}{2}\sigma_w^2$ via A2': $\delta^T F \geq 2\alpha V$. ✓
- Solving the linear ODE: $\mathbb E[V(t)] \leq V(0)e^{-2\alpha t} + \frac{n\sigma_w^2}{4\alpha}(1 - e^{-2\alpha t})$. ✓
- Steady-state: $\mathbb E[V]_{ss} = \frac{n\sigma_w^2}{4\alpha}$ ⇒ $\mathbb E[\|\delta\|^2]_{ss} = \frac{n\sigma_w^2}{2\alpha}$ ⇒ RMS $= \sigma_w\sqrt{n/(2\alpha)}$. ✓
- Stopping-time localization: $\tau_R = \inf\{t : \|\delta\| > R\}$. On $[0, t \wedge \tau_R]$, A2' applies; the Itô integral is a martingale by optional stopping; the stopped Grönwall bound holds. Non-exit probability $\leq n\sigma_w^2/(2\alpha R^2)$ by Markov on the steady-state second moment. ✓

Prop A.2 (adaptive reserve): $R^*_{\text{after}} = (\rho + \Delta\rho)/\alpha$. Persistence preserved iff $(\rho + \Delta\rho)/\alpha < R$, i.e., $\Delta\rho < \alpha R - \rho = \Delta\rho^*$. ✓

**Math is sound throughout.** Standard Lyapunov / Itô-Lyapunov machinery applied correctly to the sector-condition setup. The stopping-time localization for region-awareness is the standard technique for handling local A2' in stochastic settings.

**4. What direction next?** Reading deriv-gain-sector next (cited from der-gain-sector-bridge). I expect Prop B.3 (gain-sector bridge under B1 directional fidelity) and Prop B.4 (gradient-sector equivalence via strong convexity).

**5. What errors should I now watch for?**
- Future segments using "sector condition" without specifying sub-scope α vs β.
- Future segments using "ultimate bound $R^* = \rho/\alpha$" without acknowledging the initial-condition requirement (trajectory must start in $\mathcal B_R$ for the result to apply).
- Misapplication of Prop A.1S without the region-awareness check ($R^*_S < R$).
- Conflation of "matched coordinate" (Lyapunov quadratic) with "forced coordinate" (Cauchy-FE-derived). The segment is explicit; downstream that conflates them = finding.
- Rule-based / discontinuous correction functions being treated as in-scope for contraction-based composition analysis. The structural Lipschitz-floor scope-exit is explicit; downstream violations = finding.

**6. Predictions for next segments.** Reading next: `deriv-gain-sector`. Likely Prop B.3 (gain-sector bridge), Prop B.4 (gradient-sector equivalence), counterexample FM-1 for B1 violation, simulation validation tables.

**7. What would I change?** The "operator-family classification" subsection is dense and load-bearing. It's appropriately placed (after the basic A2' grounding, before the proofs), but readers without monotone-operator theory background will struggle. Could benefit from a one-sentence "TL;DR" at the top: "the α/β partition can be restated as: α = operator families that are cocoercive in some natural inner product; β = those that aren't." Mild editorial; not a finding.

**8. What am I now curious about?**

(a) The "matched vs forced" distinction is a structural insight: AAD has *forced* coordinates at chain (log-additive identity), divergence (reverse-KL), update (log-odds), metric (Fisher) layers — all via Cauchy-FE-style or Čencov-style uniqueness theorems on AAD-internal axioms. The Lyapunov quadratic is *matched* (canonical-but-not-forced). This is honest scope-honesty about which coordinates are theoretically forced vs conventionally chosen. Would be cleaner to surface this distinction as a stand-alone observation in #disc-additive-coordinate-forcing rather than buried here. Possible Section D candidate.

(b) The structural Lipschitz-floor scope-exit composition with identifiability-floor: rule-based agents with regime-dependent thresholds suffer *both* non-contractibility AND non-identifiability when the regime is unobservable. This is a sharp combination — two different floor mechanisms compose multiplicatively. Could rule-based / threshold-triggered AI systems (e.g., heuristic-based agents, classical expert systems) be in this double-floor regime? Worth thinking about.

(c) Prop A.1S's region-awareness is "no longer deferred" per the segment — meaning earlier versions had it as an Epistemic-Status caveat. The framework strengthened the proposition statement to incorporate the region condition directly. This is the kind of cleanup the F-V findings batch would catch.

(d) The non-exit probability $\leq n\sigma_w^2/(2\alpha R^2)$ scales linearly in $\sigma_w^2$ and inversely in $\alpha R^2$. So agents with large $R$ (model-class-capacious) and high $\alpha$ (strong correction) have very low excursion probability. The "robust" vs "fragile" framing in Prop A.2 fits naturally: robust agents are also low-excursion.

**9. What new knowledge enabled.** Persistence machinery now derived (not assumed) under qualitative sector conditions. Adaptive reserve is computable from $(\alpha, R, \rho)$. Sub-scope α/β explicit and operator-family-grounded. Structural Lipschitz-floor scope-exit clear. Region-aware Prop A.1S available.

**10. Should the audit process change?** Math verification on this segment was high-value. The load-bearing proofs check out. Worth doing on every appendix-derivation segment given they're the framework's spine.

**11. Outline updates.** Section E (calibration) gets significant confirmation: the framework's central machinery is mathematically sound. The recently-added pieces (Khasminskii localization, monotone-operator lineage, structural-Lipschitz-floor) propagate cleanly. Section D candidate: "matched vs forced" coordinate distinction as a structural observation.

## Status-label / discipline

`status: exact` defended carefully — Props A.1, A.2 exact under stated assumptions; Prop A.1S exact in region-aware form; A2' tier-stratified by sub-scope (derived in α / assumed in β). Tier-stratification of "exact" within a single segment is honest. `stage: draft` interesting given depth — Gate 1/2 audits may not have re-run since recent additions.

## Cadence check

Next: `deriv-gain-sector` (cited from der-gain-sector-bridge).
