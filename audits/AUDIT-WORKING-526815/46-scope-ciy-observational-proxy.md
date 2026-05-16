# 46 - scope-ciy-observational-proxy

Source: `01-aat-core/src/scope-ciy-observational-proxy.md`

## First-pass understanding

This segment defines an auxiliary observational CIY proxy as a difference of conditional mutual informations and explicitly warns that it is sign-indefinite. The canonical CIY remains the interventional, non-negative quantity; the proxy is diagnostic only and should not be placed directly into a policy objective. If canonical CIY is unavailable and no safe surrogate exists, the CIY term should be dropped rather than optimized through the proxy.

The regime classification is the practical center: Regime A supports direct interventional estimation, Regime B requires causal assumptions, and Regime C is passive/adversarial where CIY should not be used as a normal exploration term. This is the right kind of scope discipline, but the boundary between A and B depends on assignment/identification conditions, not merely on whether actions vary.

## Diagram attempt

I drew canonical CIY and proxy CIY as separate quantities rather than a single quantity with noise. Then I placed the three regimes under them: Regime A can estimate canonical CIY if action assignment is randomized or ignorable; Regime B can use assumptions/adjustment; Regime C should avoid CIY-policy optimization. This captures the segment's main safety lesson.

## Findings and watches

- Candidate finding: the proxy is described as observational, but its formula conditions on `Omega_t`. If `Omega_t` is the true environment state, the proxy is not generally computable from ordinary observations; if `Omega_t` is an estimated state, the formula should say so and inherit model-error caveats. If `Omega_t` is post-action state, conditioning on it may also block or distort the causal effect being diagnosed.
- Candidate finding: Regime A conflates action variation with randomized or identifiable intervention. "The agent varies its actions" is not enough for clean interventional estimates when action choice is policy-driven by state/history that also affects outcomes. Regime A needs randomization, known action mechanism plus adjustment, or sequential ignorability/positivity conditions.
- Watch: the segment says the proxy is not an approximation of canonical CIY, but the opening says CIY can be approximated from observational data. The final wording should consistently call it a separate diagnostic proxy that correlates under favorable conditions.
- Watch: large proxy magnitude can reflect confounding or conditioning artifacts, not just causal information carried by the action. The text mostly acknowledges this, but the diagnostic interpretation should remain cautious.

## Local verdict

The safety posture is good: do not optimize a sign-indefinite proxy. The technical pressure is on observability of `Omega_t` and on tightening Regime A so that "intervention-rich" means identifiable, not merely action-varying.
