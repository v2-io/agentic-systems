# Reflection 47 — disc-credit-assignment-boundary (Section II row 22)

Substantial segment with the default signal function and OKR connection.

## §4.2 dependency check

`depends: [def-strategy-dag, hyp-edge-update-via-gain, deriv-edge-update-natural-parameter, def-strategic-calibration, der-observability-dominance, der-gain-sector-bridge, deriv-strategic-dynamics]`. All upstream except deriv-edge-update-natural-parameter and deriv-strategic-dynamics (Appendix A, appendix-back-pointers per §4.2 exception). Both are candidate in-context reads — deferring to next batch since this segment is comprehensible without them. **No backward-dep critical finding.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "tractable/intractable boundary; design requirement framing." ✓ exactly. Plus much more: default signal function in log-odds with regime modulation; three-axis decomposition (outcome / attribution / regime); four-level credit-assignment-quality hierarchy; **substantial OKR/AAD connection mapping organizational management to formal AAD quantities.** The OKR mapping was unexpected and is one of the framework's clearest domain instantiations.

**2. Cross-segment consistency.** Extensive cross-refs internal. The log-odds presentation closes the mechanical break per Finding 2 / spike-gbp1-logit-scoping (Working Notes citation). Props B.1-B.7 remain in moment-parameter form via Fisher-equivalence — sector content parameterization-agnostic.

**3. Math verification (at discretion).** Default log-odds signal function $\lambda_k^{\text{new}} = \lambda_k + \eta_{\text{edge}} \cdot \iota_k \cdot J_k(y_G - \hat P_\Sigma)/\|J\|^2$ with sigmoid projection. The "log-odds eliminates mechanical break" claim is structural — domain is $\mathbb R$, additive updates can't exit; sigmoid projection guarantees $p \in (0,1)$ by construction. ✓

**4. What direction next?** Row 23 = `form-structural-change-as-parametric-limit`. Probably about pruning/grafting.

**5. What errors should I now watch for?**
- Future segments using probability-space updates without acknowledging the mechanical break (resolved in log-odds).
- Confusion between L0 directional-fidelity-on-average (works) and per-edge attribution (contaminated by correlated failures).
- Treating "credit assignment is solved" claims without specifying which level (0/1/2/3) of the hierarchy.

**6. Predictions for next segments.** Row 23 = `form-structural-change-as-parametric-limit`. status:draft per OUTLINE. Probably treats DAG-structural change (adding/removing nodes/edges) as continuous limit of parametric change.

**7. What would I change?** The OKR connection in Discussion is operationally striking. Could be elevated as a substantive piece of the framework's domain-instantiation contribution. The four-level quality hierarchy is clean.

**8. What am I now curious about?**

(a) **The four-level credit-assignment-quality hierarchy.** Persistence requires only Level 0; adaptive behavior requires Level 1; typical applications use Level 2; Level 3 is \#P-hard. Operationally clean tiering with explicit cost-benefit. Most ML literature implicitly demands Level 3 (or a heuristic for it); AAD says Level 1 is sufficient for the formal guarantees.

(b) **The OKR/AAD mapping.** Vanity metrics → high $\sigma_v$, low $p_{ij}$; too many KRs → $\alpha_\Sigma \propto 1/k$; lagging indicators → $\nu_{\text{obs}} \ll \rho$; Goodhart → $V_{O_t}(\tau) < V_{O_t}^{\min}$ despite terminals achieved. Each OKR failure mode maps to a specific formal quantity. This is a striking domain instantiation — the same formal machinery that predicts strategic persistence also predicts OKR success/failure.

(c) **The "observability is the lever, not algorithm design" framing.** The theory's structural insight: credit assignment is primarily an *observability design problem*, not an *algorithm design problem*. Invest in observable intermediates rather than smarter attribution algorithms. This is a structurally different recommendation than what most AI / planning literature gives.

(d) **AAD as REINFORCE-with-causal-weighting.** "Jacobian is score function, $(y_G - \hat P_\Sigma)$ is advantage, $\iota_k$ is causal-validity discount." Operationally connects to RL theory while distinguishing AAD's contribution.

**9. What new knowledge enabled.** Default log-odds signal function with regime modulation. Three-axis signal decomposition. Four-level credit-assignment-quality hierarchy. Directional-fidelity as minimal requirement (persistence robust to approximation). OKR/AAD operational mapping. Observability-as-lever design recommendation.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** **Section D candidate (strong):** the OKR/AAD operational mapping. This is one of the framework's most striking domain instantiations — multiple distinct failure modes mapped to specific formal quantities. Worth highlighting in the report's contribution-to-the-field section.

**12. How valuable does this segment *feel* to me?**

**High value, top-decile.** The OKR connection is one of the clearest operational instantiations I've encountered. Multiple OKR failure modes with formal quantity mappings makes the framework's organizational-management payoff specific, not generic. The four-level credit-assignment-quality hierarchy is clean tiering. The log-odds presentation closes the mechanical break by construction.

The "observability is the lever" reframing is structurally different from typical algorithm-focused approaches.

Magnitude: top-decile. Type: discussion-grade with substantial operational + structural content. Engagement: strong; the OKR mapping was unexpected and operationally satisfying. The four-level hierarchy is the kind of clean tiering I keep wanting to see in ML literature.

**13. What does the framework now potentially contribute to the field?**

- **Plan-DAG designers:** default credit-assignment scheme (gradient log-odds with regime modulation) + four-level quality hierarchy + directional-fidelity-as-minimal-requirement guidance.
- **Organizational researchers / management consultants:** OKR/AAD mapping with concrete failure-mode predictions tied to formal quantities. Vanity metrics, too-many-KRs, lagging indicators, Goodhart — all formal. A theory of why OKRs fail when they fail.
- **RL theorists:** AAD as REINFORCE-with-causal-identification-weighting. Bridges sequential decision theory and causal inference.
- **Practitioners:** "observability is the lever" — design for observable intermediates rather than smarter attribution algorithms. Operationally different from typical advice.
- **AI alignment researchers:** persistence-vs-attribution decoupling. Persistence is robust to approximate credit assignment; the formal guarantees don't require solving attribution.
- **Decision-theory researchers working on credit assignment:** \#P-hardness reduction (Shapley → AND/OR DAG) plus information-theoretic underdetermination plus posterior-correlation barrier. Three-pronged characterization of the difficulty.

**Most distinctive contribution:** the **OKR/AAD operational mapping**. Most theoretical frameworks don't reach into management practice this directly. AAD predicts specific OKR failure modes from the *same* formal machinery that handles plan-DAG persistence. This is a domain-bridging move that few frameworks attempt and even fewer execute cleanly.

The **observability-as-lever framing** is also distinctive: most ML literature on credit assignment focuses on algorithm sophistication; AAD's framework points at design-for-observability as the operationally more important lever.

## Status-label / discipline

`status: discussion-grade`. Mixed: default signal function is formulation; boundary characterization discussion-grade; design requirement derived from bridge theorem; intractability barriers sketch-grade. Tier-stratification within is honest.

`stage: draft`.

## Cadence check

Holding. Next: row 23 = `form-structural-change-as-parametric-limit`.
