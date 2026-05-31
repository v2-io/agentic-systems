# 19 — result-mismatch-decomposition

*Type: result. Status: exact. Stage: claims-verified. First named result of the volume. Depends: [def-mismatch-signal, def-observation-function, def-action-transition, form-agent-model, scope-adaptive-system].*

## Predictions vs evidence
Predicted: bias-variance-style decomposition into reducible + irreducible. Found: exactly that — model error + observation noise.

## **Math verification (first substantive derivation)**

Claim:
$$\mathbb{E}[\|\delta_t\|^2] = \mathbb{E}[\|\hat o_t - \bar o_t\|^2] + \mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]$$

**Derivation verified directly:**
Let $\delta_t = o_t - \hat o_t = (o_t - \bar o_t) + (\bar o_t - \hat o_t)$ where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$.

Then $\|\delta_t\|^2$ expands to model-error squared + noise squared + 2×cross-term.

Cross-term: $2(o_t - \bar o_t)^T(\bar o_t - \hat o_t)$. Conditioning on $(\Omega_t, a_{t-1}, \mathcal{C}_{t-1})$:
- $\bar o_t$ is fixed (deterministic in $\Omega_t, a_{t-1}$)
- $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ is fixed (deterministic in $\mathcal{C}_{t-1}, a_{t-1}$ since $M_{t-1} = \phi(\mathcal{C}_{t-1})$)
- $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}, \mathcal{C}_{t-1}] = \mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ — first equality by GA-1 (fresh noise), second by definition of $\bar o_t$
- Therefore cross-term has conditional mean zero → tower property gives $\mathbb{E}[\text{cross-term}] = 0$. ✓

Then $\mathbb{E}[\|o_t - \bar o_t\|^2] = \mathbb{E}[\mathbb{E}[\|o_t - \bar o_t\|^2 \mid \Omega_t, a_{t-1}]] = \mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]$ — by definition of conditional variance about the conditional mean. ✓

**The decomposition is exact under GA-1.** No errors found.

## Prose-coherence
- Preamble (lines 14-20) and Discussion (lines 45-49) have substantial overlap (structural-persistence, model-sufficiency-alignment, reducible/irreducible framing). Within cadence.
- The "alignment assumption" caveat (line 47) is methodologically honest — $S(M_t) < 1$ doesn't automatically imply positive model error in the conditional mean; the connection requires that the lost information affects the one-step mean specifically.

## Watch list
- The fresh-noise assumption GA-1 is invoked as the assumption that makes the cross-term vanish. GA-1 is in NOTATION.md's global assumptions table — coherent.
- The proof step "Condition on $(\Omega_t, a_{t-1}, \mathcal{C}_{t-1})$" is correctly applied (line 36).

## Cross-segment consistency
First result anchoring the noise-floor / model-error split that downstream segments (#emp-update-gain, #def-model-sufficiency, #result-persistence-condition) will lift.

## Next-segment predictions
`#emp-update-gain`. Will introduce $\eta^\ast = U_M/(U_M + U_o)$ — the optimal update gain. Type `empirical` per OUTLINE. Will be the canonical Bayesian-update form, possibly with derivation in appendix.

## What I'd change
Reduce preamble-Discussion duplication (pattern continues across multiple segments). The structural-persistence point is made three times across this segment (preamble line 18-19, Formal Expression line 28's "$> 0$", Discussion line 49). Not a finding.

## Brief wandering
**The mismatch decomposition is exactly what the framework needs to ground the rest of Section I.** Without this, talking about "agents should drive $\delta_t$ to zero" would be confused (the floor exists). With this, the agent's job is clearly framed as "minimize the reducible part while accepting the irreducible." This is the foundation for everything in Ch.3 and Ch.4. Strong.
