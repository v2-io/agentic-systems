---
slug: per-dimension-persistence
type: theorem
status: exact
depends:
  - persistence-condition
  - adaptive-tempo
---

# Per-Dimension Persistence

The scalar persistence condition $\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$ overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension: $\mathcal{T}_k > \rho_k / \|\delta_{\text{critical},k}\|$ for each dimension $k$ with significant disturbance.

## Formal Expression

*[Theorem (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance $\rho_k$:

The per-dimension steady-state mismatch (AR(1) process) is:

$$E[\|\delta_k\|] = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

which for small $\eta_k$ approximates:

$$E[\|\delta_k\|] \approx \frac{\rho_k}{\sqrt{2\eta_k}} \cdot \sqrt{\frac{2}{\pi}}$$

**Persistence requires** $\eta_k > \rho_k / \|\delta_{\text{critical},k}\|$ **for each dimension independently.**

The aggregate $L_2$ mismatch $\|\delta\| = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio.

## Epistemic Status

*Exact.* The per-dimension steady state is derived from the AR(1) stationary distribution and matches simulation to 4 significant figures. The scalar tempo overestimates by 72% in a 3-dimensional test case with 5:1 gain variation. This is a mathematical result, not an approximation — the per-dimension AR(1) processes are independent under diagonal correction, so the per-dimension theory is simply the 1D result applied per dimension.

## Discussion

**Scalar tempo overestimates.** In a 3D system with gains $\eta = (0.15, 0.03, 0.03)$ and disturbances $\rho = (0.20, 0.20, 0.02)$:

| Dimension | $\eta_k$ | $\rho_k$ | $\rho_k / \eta_k$ | $E[\|\delta_k\|]$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 (well-tracked) | 0.15 | 0.20 | 1.33 | 0.303 |
| 2 (weak) | 0.03 | 0.20 | 6.67 | 0.656 |
| 3 (unimportant) | 0.03 | 0.02 | 0.67 | 0.066 |

Scalar prediction: $\rho / \mathcal{T} = 0.284 / 0.21 = 1.35$. Actual $\|\delta\|_{L_2} = 0.785$. Overestimate: 72%. Dimension 2 alone accounts for 84% of the $L_2$ mismatch.

**Isotropic allocation dominates.** Equalizing the same total gain budget ($\eta = 0.07$ per dimension) reduces $\|\delta\|_{L_2}$ from 0.785 to 0.685 — a 13% improvement — because it reduces the bottleneck effect on the weak dimension.

**Adversarial exploitation.** An adversary who identifies the target's weak dimension can concentrate disturbance there. Targeted attack (80% on the weak dimension) amplifies the mismatch ratio by 17% (from 2.70 to 3.15). The real danger is structural: if the weak dimension's mismatch exceeds its critical threshold ($R_{\text{max}}$), correction fails on that dimension while the aggregate $\|\delta\|_{L_2}$ may still look manageable. Per-dimension monitoring is essential.

**Implications for the persistence condition.** The scalar persistence condition ( #persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition $\mathcal{T}_k > \rho_k / \|\delta_{\text{critical},k}\|$ is both necessary and sufficient (under diagonal correction).

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

## Working Notes
- The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question — it likely does qualitatively (the weakest dimension still dominates) but the quantitative overestimate may shrink.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) would replace the scalar $\mathcal{T}$ with a diagonal matrix $\mathcal{T} = \text{diag}(\mathcal{T}_1, \ldots, \mathcal{T}_d)$. The persistence condition becomes $\mathcal{T}_k > \rho_k / \delta_{\text{critical},k}$ for each $k$. This is mentioned in #adaptive-tempo's Discussion but not yet formalized.
- Simulation code: `scratch/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
