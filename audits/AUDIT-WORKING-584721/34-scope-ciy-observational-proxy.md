# Reflection 34 — scope-ciy-observational-proxy (Section II row 9)

## §4.2 dependency check

`depends: [def-causal-information-yield, der-loop-interventional-access]`. Both upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "When CIY can be estimated from observational data; connects to identification-strength caveats." ✓ exactly. The Regime A/B/C classification matches what der-loop-interventional-access referenced.

**2. Cross-segment consistency.** Regime A/B/C consistent across segments. The "sign-indefinite proxy should NOT be used in policy optimization" warning is operationally crisp.

**3. Math verification (at discretion).** The proxy $I(o_t; a_{t-1}|M_{t-1}) - I(o_t; a_{t-1}|\Omega_t, M_{t-1})$ is sign-indefinite — first term is observational, second is conditional on true state. The difference can be positive or negative depending on confounding structure. Sign-indefiniteness is correctly flagged. ✓

**4. What direction next?** Row 10 = `disc-ciy-unified-objective`. The joint exploitation-exploration objective.

**5. What errors should I now watch for?**
- Future segments using the proxy form in policy optimization (segment is explicit this is unsafe).
- Confusion of CIY (canonical, non-negative) with CIY-proxy (sign-indefinite).
- Treating Regime as agent-selectable rather than domain-property.

**6. Predictions for next segments.** Row 10 = `disc-ciy-unified-objective`. Per OUTLINE, status:draft. Joint exploitation-exploration objective with $\lambda$-weighted CIY term.

**7. What would I change?** The "Safety conditions for proxy use" warning is appropriately strong — operational guidance that prevents misuse. Good.

**8. What am I now curious about?** The Regime A/B/C classification is the same identification-regime spectrum used in der-loop-interventional-access and (per OUTLINE) #scope-edge-update-causal-validity. It's a recurring framework worth tracking. Could be a meta-pattern: regime-indexed identification-strength as a structural framing across multiple segments.

**9. What new knowledge enabled.** CIY-proxy formal definition. Three-regime admissibility. Safety conditions for proxy use.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** No new findings.

**12. How valuable does this segment *feel* to me?**

Medium. Compact and operationally useful — the safety warning prevents a real misuse. Not foundational, but does its scope-narrowing job cleanly. The regime classification with domain examples (software = A, organizational = B, intelligence = C) is concretely useful.

Magnitude: middle of pack. Type: clean scope condition with safety guidance.

**13. What does the framework now potentially contribute?**

- **Researchers building exploration-bonus systems** get a precise warning: sign-indefinite proxies are unsafe for optimization.
- **Causal-inference researchers** get the regime-indexed framing for when observational proxy approximates interventional CIY.
- **Practitioners** get domain-classification examples (software A, organizational B, intelligence C) — useful for choosing exploration strategies.
- **AI safety researchers** get a clean operational rule: in Regime C (adversarial / passive), default to pure exploitation rather than attempting CIY-driven exploration with bad proxies.

Most distinctive: the sign-indefinite-proxy safety warning is operationally crisp. Most exploration literature handwaves about "approximate interventional information"; AAD names the failure mode explicitly.

## Status-label / discipline

`status: conditional` — appropriate; depends on regime-specific causal assumptions. `stage: draft`.

## Cadence check

Holding. Next: row 10 = `disc-ciy-unified-objective`.
