---
slug: per-dimension-persistence
type: result
status: empirical
depends:
  - persistence-condition
  - adaptive-tempo
---

# Result: Per-Dimension Persistence

The scalar persistence condition $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension: $\mathcal T_k \gt \rho_k / \Vert\delta_{\text{critical},k}\Vert$ for each dimension $k$ with significant disturbance.

## Formal Expression

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance $\rho_k$:

The per-dimension steady-state mismatch (AR(1) process) is:

$$E[\Vert\delta_k\Vert] = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

which for small $\eta_k$ approximates:

$$E[\Vert\delta_k\Vert] \approx \frac{\rho_k}{\sqrt{2\eta_k}} \cdot \sqrt{\frac{2}{\pi}}$$

**Persistence requires** $\eta_k \gt \rho_k / \Vert\delta_{\text{critical},k}\Vert$ **for each dimension independently.**

The aggregate $L_2$ mismatch $\Vert\delta\Vert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio.

## Epistemic Status

*Empirical.* The per-dimension steady-state formula is derived from the AR(1) stationary distribution (a stochastic-noise model) and matches simulation to 4 significant figures within that model. However, two issues prevent an `exact` status:

1. **Regime mixing.** The summary states the persistence threshold as $\mathcal T_k \gt \rho_k / \lVert\delta_{\text{critical},k}\rVert$ (a deterministic-drift condition using per-dimension tempo), but the formal expression derives steady-state mismatch from a stochastic AR(1) process using raw gain $\eta_k$, not tempo $\mathcal T_k = \nu_k \eta_k$. These are different models: the deterministic-drift threshold comes from the sector-condition framework ( #sector-condition-stability); the stochastic formula comes from AR(1) stationarity. The per-dimension threshold as stated does not follow from the AR(1) formula — it is the deterministic result applied per dimension, which is plausible but not derived from the stochastic model presented.

2. **Simulation evidence, not proof.** The 72% overestimate and 4-significant-figure match are simulation results within the AR(1) model class. They validate the stochastic formula but do not constitute a proof of the per-dimension persistence threshold. The threshold is better understood as an empirical finding supported by simulation and motivated by the deterministic analogy.

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

**Implications for the persistence condition.** Like the scalar result, per-dimension persistence addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery on each dimension can outpace that dimension's disturbance rate. An agent can be structurally persistent on every dimension while still being operationally fragile on one (near its per-dimension $R_k$ boundary). The scalar persistence condition ( #persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition $\mathcal T_k \gt \rho_k / \lVert\delta_{\text{critical},k}\rVert$ is the natural extension — simulation confirms it predicts per-dimension failure correctly, but its formal status is empirical (validated within the AR(1) model class, not derived from the sector-condition framework in the stochastic regime). See Epistemic Status above for the precise gap.

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

## Working Notes
- The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question — it likely does qualitatively (the weakest dimension still dominates) but the quantitative overestimate may shrink.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) would replace the scalar $\mathcal{T}$ with a diagonal matrix $\mathcal{T} = \text{diag}(\mathcal T_1, \ldots, \mathcal T_d)$. The persistence condition becomes $\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$ for each $k$. This is mentioned in #adaptive-tempo's Discussion but not yet formalized.
- Simulation code: `../../msc/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
