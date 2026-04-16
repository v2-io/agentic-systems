---
slug: per-dimension-persistence
type: result
status: conditional
depends:
  - persistence-condition
  - adaptive-tempo
  - sector-condition-derivation
stage: draft
---

# Result: Per-Dimension Persistence

The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension, with the form depending on whether the disturbance is deterministic (Model D) or stochastic (Model S).

## Formal Expression

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance:

### Model D: Deterministic Per-Dimension Threshold

Under bounded disturbance $|w_k(t)| \leq \rho_k$ (GA-2, per dimension), the per-dimension steady-state mismatch is:

$$|\delta_k|_{ss} = \frac{\rho_k}{\alpha_k}$$

**Persistence requires** $\alpha_k > \rho_k / R_k$ **for each dimension**, or in linear operational form:

$$\mathcal{T}_k > \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

This is the deterministic worst-case bound — exact under bounded disturbance by the same Lyapunov argument as Prop A.1, applied per dimension.

### Model S: Stochastic Per-Dimension Steady State

Under stochastic disturbance $w_{k,t} \sim N(0, \rho_k^2)$ (GA-2S, per dimension), the discrete AR(1) process $\delta_{k,t+1} = (1 - \eta_k)\delta_{k,t} + w_{k,t}$ has stationary distribution $\delta_k \sim N(0, \rho_k^2/(2\eta_k - \eta_k^2))$, giving:

$$E[|\delta_k|] = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

which for small $\eta_k$ approximates:

$$E[|\delta_k|] \approx \frac{\rho_k}{\sqrt{2\eta_k}} \cdot \sqrt{\frac{2}{\pi}}$$

**Persistence requires** (from $E[|\delta_k|] < \delta_{\text{critical},k}$, small-$\eta_k$ approximation):

$$\eta_k > \frac{\rho_k^2}{\pi \cdot \delta_{\text{critical},k}^2}$$

Or as a probability bound ($P(|\delta_k| > \delta_{\text{critical},k}) < \epsilon$, using the Gaussian tail):

$$\eta_k > \frac{\rho_k^2 \cdot z_{1-\epsilon}^2}{2 \cdot \delta_{\text{critical},k}^2}$$

where $z_{1-\epsilon}$ is the Gaussian quantile. Note: the stochastic threshold is quadratic in $\rho_k/\delta_{\text{critical},k}$ (not linear as in Model D), reflecting the $1/\sqrt{\alpha}$ scaling.

### Common Structure

The aggregate $L_2$ mismatch $\lVert\delta\rVert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio (Model S) or $\rho_k / \alpha_k$ ratio (Model D). The qualitative conclusion — the weak dimension is the bottleneck — holds for both models.

## Epistemic Status

*Exact conditional on disturbance model.* Both per-dimension forms are now derived from their respective disturbance models:

1. **Model D threshold** ($\mathcal{T}_k > \rho_k/\delta_{\text{critical},k}$) follows from Prop A.1 applied per dimension — the same Lyapunov argument with bounded disturbance, restricted to each coordinate. This is exact under GA-2 + GA-3.

2. **Model S steady state** ($E[|\delta_k|] = \rho_k/\sqrt{2\eta_k - \eta_k^2} \cdot \sqrt{2/\pi}$) follows from the AR(1) stationary distribution under Gaussian disturbance (GA-2S). The stochastic persistence threshold ($\eta_k > \rho_k^2/(\pi \cdot \delta_{\text{critical},k}^2)$) is derived from this formula. The 4-significant-figure simulation match validates Model S, not Model D.

The previously noted "regime mixing" is resolved: the two threshold forms belong to different disturbance models. The Model D threshold is linear in $\rho_k$; the Model S threshold is quadratic. The 72% scalar overestimate and weak-dimension bottleneck are structural properties that hold under both models.

## Discussion

**Scalar tempo overestimates.** In a 3D system with gains $\eta = (0.15, 0.03, 0.03)$ and disturbances $\rho = (0.20, 0.20, 0.02)$:

| Dimension | $\eta_k$ | $\rho_k$ | $\rho_k / \eta_k$ | $E[\Vert\delta_k\Vert]$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 (well-tracked) | 0.15 | 0.20 | 1.33 | 0.303 |
| 2 (weak) | 0.03 | 0.20 | 6.67 | 0.656 |
| 3 (unimportant) | 0.03 | 0.02 | 0.67 | 0.066 |

Scalar prediction: $\rho / \mathcal{T} = 0.284 / 0.21 = 1.35$. Actual $\Vert\delta\Vert_{L_2} = 0.785$. Overestimate: 72%. Dimension 2 alone accounts for 84% of the $L_2$ mismatch.

**Isotropic allocation dominates.** Equalizing the same total gain budget ($\eta = 0.07$ per dimension) reduces $\Vert\delta\Vert_{L_2}$ from 0.785 to 0.685 — a 13% improvement — because it reduces the bottleneck effect on the weak dimension.

**Adversarial exploitation.** An adversary who identifies the target's weak dimension can concentrate disturbance there. Targeted attack (80% on the weak dimension) amplifies the mismatch ratio by 17% (from 2.70 to 3.15). The real danger is structural: if the weak dimension's mismatch exceeds its critical threshold ($R_{\text{max}}$), correction fails on that dimension while the aggregate $\Vert\delta\Vert_{L_2}$ may still look manageable. Per-dimension monitoring is essential.

**Implications for the persistence condition.** Like the scalar result, per-dimension persistence addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery on each dimension can outpace that dimension's disturbance rate. An agent can be structurally persistent on every dimension while still being operationally fragile on one (near its per-dimension $R_k$ boundary). The scalar persistence condition ( #persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition has two forms: Model D ($\mathcal{T}_k > \rho_k/\delta_{\text{critical},k}$, exact under bounded disturbance) and Model S ($\eta_k > \rho_k^2/(\pi \cdot \delta_{\text{critical},k}^2)$, exact under Gaussian disturbance). Both predict per-dimension failure correctly; the choice depends on the disturbance character in the domain.

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

## Working Notes
- The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question — it likely does qualitatively (the weakest dimension still dominates) but the quantitative overestimate may shrink.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) would replace the scalar $\mathcal{T}$ with a diagonal matrix $\mathcal{T} = \text{diag}(\mathcal T_1, \ldots, \mathcal T_d)$. The persistence condition becomes $\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$ for each $k$. This is mentioned in #adaptive-tempo's Discussion but not yet formalized.
- Simulation code: `../../msc/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
