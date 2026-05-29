# 23 — hyp-mismatch-dynamics

*Type: hypothesis. Status: heuristic. Stage: deps-verified. Depends: [def-adaptive-tempo, def-mismatch-signal, deriv-sector-condition].*

## Predictions vs evidence
Predicted: linear ODE preview + steady-state form $\rho/\mathcal{T}$. Found: both Model D and Model S steady states + transient solution + adversarial-coupling scaling exponents.

## **Math verification (substantive)**
- ODE $d\|\delta\|/dt = -\mathcal{T}\|\delta\| + \rho(t)$. ✓
- Model D steady state: setting $\dot{\|\delta\|} = 0$: $\|\delta\|_{ss} = \rho/\mathcal{T}$. ✓ (Direct algebra.)
- Transient: $\|\delta(t)\| = \|\delta_0\| e^{-\mathcal{T}t} + (\rho/\mathcal{T})(1 - e^{-\mathcal{T}t})$. ✓ (Standard 1st-order linear ODE solution via integrating factor.)
- Model S steady state: O-U process $d\delta = -\mathcal{T}\delta\,dt + \sigma_w dW_t$ has stationary variance $\sigma_w^2/(2\mathcal{T})$, so RMS = $\sigma_w/\sqrt{2\mathcal{T}}$. ✓ ($n$-D isotropic: $\sigma_w\sqrt{n/(2\mathcal{T})}$. ✓)
- Adversarial scaling: $1/\mathcal{T}$ scaling under Model D → squared advantage $(\mathcal{T}_A/\mathcal{T}_B)^2$; $1/\sqrt{\mathcal{T}}$ scaling under Model S → 3/2-power advantage. Consistent dimensional reasoning. (To verify formally at `#result-adversarial-tempo-advantage`.)

## Prose-coherence
- The Model D vs Model S distinction is methodologically important and is consistently flagged across the segment.
- "Heuristic" status is honest — the linear ODE is explicitly a first-order approximation; the nonlinear sector-condition framework handles the general case.
- Bridging assumption from discrete to continuous (line 56) named with explicit error bound $O(\eta^* c_{\max}/\nu^{1/2})$.

## Cross-segment consistency
Forward-refs `#result-sector-condition-stability`, `#result-persistence-condition`, `#deriv-discrete-sector-condition`, `#deriv-sector-condition`, `#form-event-driven-dynamics`, `#result-structural-adaptation-necessity`, `#result-adversarial-tempo-advantage`. Dense and coherent.

## Watch list
- Model S has the noise variance written sometimes as $\sigma_w^2$ (line 38 SDE), sometimes implicitly as $\sigma_w$ (line 42 RMS). The convention is $\sigma_w$ = standard deviation, $\sigma_w^2$ = variance. Consistent here.

## Next-segment predictions
End of Ch.3 — next is the chapter intro for Ch.4 (`#persistence-and-limits-intro`). Then derivations of deliberation cost, sector condition, persistence condition, etc. Will get into the math-correctness heavy work I've been previewing.

## Brief wandering
The Model-D/Model-S distinction is one of the framework's quietly important moves. Most adaptive-control literature works in Model-D (deterministic bounded disturbance); most stochastic-control works in Model-S (Brownian noise). AAT handles both and surfaces the $1/\mathcal{T}$ vs $1/\sqrt{\mathcal{T}}$ scaling distinction — which is the kind of qualitative-difference that downstream adversarial-coupling results lift into the $(\mathcal{T}_A/\mathcal{T}_B)^2$ vs $(\mathcal{T}_A/\mathcal{T}_B)^{3/2}$ characterization. Strong.
