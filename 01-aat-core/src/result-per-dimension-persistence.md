---
slug: result-per-dimension-persistence
type: result
status: conditional
depends:
  - result-persistence-condition
  - def-adaptive-tempo
  - deriv-sector-condition
stage: draft
---

# Result: Per-Dimension Persistence

The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension, with the form depending on whether the disturbance is deterministic (Model D) or stochastic (Model S).

## Formal Expression

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance:

### Model D: Deterministic Per-Dimension Threshold

Under bounded disturbance $\lvert w_k(t)\rvert \leq \rho_k$ (GA-2, per dimension), the per-dimension steady-state mismatch is:

$$\lvert\delta_k\rvert_{ss} = \frac{\rho_k}{\alpha_k}$$

**Persistence requires** $\alpha_k \gt \rho_k / R_k$ **for each dimension**, or in linear operational form:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

This is the deterministic worst-case bound — exact under bounded disturbance by the same Lyapunov argument as Prop A.1, applied per dimension.

### Model S: Stochastic Per-Dimension Steady State

Under stochastic disturbance $w_{k,t} \sim N(0, \rho_k^2)$ (GA-2S, per dimension), the discrete AR(1) process $\delta_{k,t+1} = (1 - \eta_k)\delta_{k,t} + w_{k,t}$ has stationary distribution:

$$\delta_k \sim N\!\left(0,\; \frac{\rho_k^2}{2\eta_k - \eta_k^2}\right)$$

The stationary distribution supplies three task-adequacy criteria, each with its own threshold. The choice of criterion is an engineering decision; the three are related by exact constants for Gaussian $\delta_k$.

**(a) RMS bound** (mean-square, matches the scalar form in #result-persistence-condition):

$$\sqrt{E[\delta_k^2]} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}}$$

Requiring $\sqrt{E[\delta_k^2]} \lt \delta_{\text{critical},k}$ and using the small-$\eta_k$ approximation $2\eta_k - \eta_k^2 \approx 2\eta_k$:

$$\boxed{\;\eta_k \gt \frac{\rho_k^2}{2\,\delta_{\text{critical},k}^2}\;} \quad \text{(RMS criterion)}$$

This is the scalar Model S threshold in #result-persistence-condition ($\alpha \gt n\sigma_w^2/(2R^2)$) applied per dimension.

**(b) MAE bound** (mean absolute error; bounds the expected deviation rather than its square):

$$E\!\left[\lvert\delta_k\rvert\right] = \sqrt{E[\delta_k^2]} \cdot \sqrt{\frac{2}{\pi}} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

Requiring $E\!\left[\lvert\delta_k\rvert\right] \lt \delta_{\text{critical},k}$:

$$\eta_k \gt \frac{\rho_k^2}{\pi\,\delta_{\text{critical},k}^2} \quad \text{(MAE criterion)}$$

MAE is smaller than RMS by the factor $\sqrt{2/\pi} \approx 0.798$, so the MAE threshold is $2/\pi \approx 0.637$ times the RMS threshold. The criteria differ by a constant but bound different quantities; applying the same numerical $\delta_{\text{critical},k}$ under both does not mean the same thing.

**(c) Probability bound** (tail-risk criterion, for applications where occasional excursions matter):

$$P\!\left(\lvert\delta_k\rvert \gt \delta_{\text{critical},k}\right) \lt \epsilon \;\Longleftrightarrow\; \eta_k \gt \frac{\rho_k^2 \cdot z_{1-\epsilon/2}^2}{2\,\delta_{\text{critical},k}^2}$$

where $z_{1-\epsilon/2}$ is the two-sided Gaussian quantile. The probability bound at $\epsilon = 0.05$ (two-sided $z \approx 1.96$) is about $1.96^2 \approx 3.84$ times the RMS threshold — stricter because it bounds tail excursions rather than typical magnitudes.

**Recommended primary form.** The RMS criterion (a) is the canonical form for Model S persistence, matching the scalar treatment in #result-persistence-condition and the Lyapunov-based derivation in #deriv-sector-condition (Prop A.1S). The MAE and probability-bound variants are provided for applications where those are the natural task-adequacy measures. All three thresholds are quadratic in $\rho_k/\delta_{\text{critical},k}$ (not linear as in Model D), reflecting the $1/\sqrt{\alpha}$ scaling of the Model S stationary variance.

### Common Structure

The aggregate $L_2$ mismatch $\lVert\delta\rVert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio (Model S) or $\rho_k / \alpha_k$ ratio (Model D). The qualitative conclusion — the weak dimension is the bottleneck — holds for both models.

## Epistemic Status

*Exact conditional on disturbance model.* Both per-dimension forms are now derived from their respective disturbance models:

1. **Model D threshold** ($\mathcal T_k \gt \rho_k/\delta_{\text{critical},k}$) follows from Prop A.1 applied per dimension — the same Lyapunov argument with bounded disturbance, restricted to each coordinate. This is exact under GA-2 + GA-3.

2. **Model S steady state** follows from the AR(1) stationary distribution under Gaussian disturbance (GA-2S): $\delta_k \sim N(0, \rho_k^2/(2\eta_k - \eta_k^2))$. The RMS, MAE, and probability-bound thresholds are all exact under this distribution, differing by the constants $1$, $\sqrt{2/\pi}$, and $z_{1-\epsilon/2}$ respectively. The RMS form $\eta_k \gt \rho_k^2/(2\delta_{\text{critical},k}^2)$ matches the scalar Model S treatment in #result-persistence-condition applied per dimension. The 4-significant-figure simulation match validates Model S, not Model D.

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

**Implications for the persistence condition.** Like the scalar result, per-dimension persistence addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery on each dimension can outpace that dimension's disturbance rate. An agent can be structurally persistent on every dimension while still being operationally fragile on one (near its per-dimension $R_k$ boundary). The scalar persistence condition ( #result-persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition has two forms: Model D ($\mathcal T_k \gt \rho_k/\delta_{\text{critical},k}$, exact under bounded disturbance) and Model S ($\eta_k \gt \rho_k^2/(\pi \cdot \delta_{\text{critical},k}^2)$, exact under Gaussian disturbance). Both predict per-dimension failure correctly; the choice depends on the disturbance character in the domain.

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

## Findings

### The Weakest-Link Dimensional Persistence Law

**Brief:** When mismatch is multi-dimensional, persistence is governed by the worst-served dimension, not by aggregate or average performance. The scalar persistence condition (`#result-persistence-condition`) overestimates adaptive capacity whenever per-dimension correction gains differ from per-dimension disturbance rates. The correct condition is *per-dimension*: $\alpha_k \gt \rho_k/R_k$ under bounded disturbance (Model D, linear in $\rho_k$), or $\eta_k \gt \rho_k^2/(2\,\delta_{\text{critical},k}^2)$ under Gaussian disturbance (Model S, quadratic in $\rho_k$). The aggregate $L^2$ mismatch is dominated by the dimension with the largest $\rho_k/\eta_k$ ratio. A simulated 3D system shows the scalar form overestimating adaptive capacity by 72% with a single dimension accounting for 84% of the $L^2$ mismatch; equalizing the gain budget across dimensions (isotropic allocation) reduces aggregate mismatch by 13% by raising the bottleneck dimension's gain.

**Impact:** Establishes that survival in any multi-attribute environment is a *min* operation, not a sum or average — a structural critique of scalar capability metrics in adversarial and high-stakes settings. Adversarial implication is sharp: an opponent who identifies the target's weak dimension can concentrate disturbance there, amplifying the mismatch ratio asymmetrically while the aggregate may still appear acceptable. Per-dimension monitoring is therefore not optimization polish but a structural requirement for any agent operating under directed pressure. Carries through composition: a team of specialists each handling one dimension well composes better than a team of generalists mediocre at everything — provided the dimension assignment matches the actual disturbance structure. Calibrates how much the scalar form misleads (Model D linear, Model S quadratic in $\rho_k$), so the cost of conflating the two is itself quantified rather than asserted.

**Novelty Claim:** *Claim differentiation* on per-dimension Lyapunov stability. The per-coordinate Lyapunov argument is standard (control theory routinely does diagonal stability analysis); weakest-link arguments appear throughout reliability theory; multi-attribute critiques of scalar evaluation are familiar in decision theory. The AAT-distinctive contributions are (i) the explicit Model D / Model S decomposition with the corresponding linear vs quadratic threshold scaling in $\rho_k$, (ii) the quantitative overestimate calibration (~72% in a simulated 3D system) showing the scalar form is not just incomplete but materially misleading, and (iii) the connection to adversarial *concentration* — an opponent's optimal targeting strategy is to maximize $\rho_k$ at the weakest $\eta_k$, not to spread effort uniformly.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| Per-coordinate Lyapunov stability and ultimate boundedness | Khalil 2002 *Nonlinear Systems* (3rd ed.), Prentice Hall, chapters 4 and 9 (published 2002, found pre-2026) | *formal antecedent* — supplies the per-coordinate Lyapunov machinery; the per-dimension result is its application to AAT's correction structure under both bounded and Gaussian disturbance |
| AR(1) stationary distribution under Gaussian forcing (Ornstein-Uhlenbeck stationary) | Uhlenbeck & Ornstein 1930 *Physical Review* 36:823; Karatzas & Shreve 1991 *Brownian Motion and Stochastic Calculus* (published 1930/1991, found pre-2026) | *formal antecedent* — supplies the AR(1) stationary form used in the Model S threshold derivation |
| Weakest-link reliability / serial-system reliability | Gnedenko, Belyayev & Solovyev 1969 *Mathematical Methods of Reliability Theory*; Barlow & Proschan 1975 *Statistical Theory of Reliability* (published 1969/1975, found pre-2026) | *conceptual precursor* — the min-operation intuition for serially-dependent failures; AAT instantiates this for adaptive correction rather than for component failure |
| Multi-attribute decision theory and aggregate-vs-attribute critique | Keeney & Raiffa 1976 *Decisions with Multiple Objectives*, Wiley (published 1976, found pre-2026) | *conceptual precursor* — recognizes that aggregate scoring obscures per-attribute deficits; AAT supplies the dynamics-side analog with explicit failure thresholds |
| Adversarial robustness and per-feature attack budgets | Szegedy et al. 2014 *Intriguing Properties of Neural Networks*, ICLR; Madry et al. 2018 *Towards Deep Learning Models Resistant to Adversarial Attacks*, ICLR (published 2014/2018, found pre-2026) | *adjacent* — adversarial-ML literature on per-feature perturbation budgets; AAT's concentration analysis ($\rho_k$ at weakest $\eta_k$) gives an adaptive-system framing of the same vulnerability |
| Critique of scalar AI capability metrics | Various AI safety / evaluation literature (Hendrycks et al. 2021 benchmarks; capability evaluation methodology) (published 2021–, found 2026) | *adjacent* — the AAT result supplies a dynamics-grounded structural argument for why aggregate capability scores under-predict adversarial failure |

**Search Log:**
- 2026-04 (*intuition-only* on the integrated Model D / Model S framing): per-coordinate Lyapunov stability is standard control theory; weakest-link reliability and multi-attribute critiques of aggregate scoring are well-precedented in their own literatures. The AAT-distinctive contributions are (i) the side-by-side Model D / Model S threshold scaling difference (linear vs quadratic in $\rho_k$), (ii) the calibrated simulation overestimate as quantitative evidence the scalar form is misleading rather than merely incomplete, and (iii) the adversarial-concentration framing connecting weakest-dimension targeting to the per-dimension threshold. Targeted future search candidates: robustness in adversarial ML (per-feature adversarial attack literature, Goodfellow-Madry line); capability-evaluation methodology in AI safety (the critique-of-scalar-metrics framing has natural relevance there); portfolio-theory analogs of weakest-dimension exposure (Markowitz tradition with downside-risk concentration); reliability-theory weakest-link dynamics with stochastic forcing.
- 2025 (*targeted*): Khalil 2002 confirmed as formal antecedent for per-coordinate Lyapunov machinery; the segment cites it inline.

## Working Notes
- The diagonal-correction assumption: closed. The matrix-Loewner persistence condition `#deriv-matrix-persistence-condition` lifts the per-coordinate form to general (not-necessarily-diagonal, not-necessarily-axis-aligned-with-$D_\delta$) matrix tempo $\mathcal{T}$. Cross-dimensional correction produces off-diagonal entries in $\mathcal{T}$; under those off-diagonals, per-coordinate is *unsafe* — there exist regimes where per-coordinate declares persistence on a system whose stationary mismatch will exceed task-adequacy along the diagonal direction (the §4 counterexample of `#deriv-matrix-persistence-condition` is the constructive demonstration: $\mathcal{T} = \begin{pmatrix}1 & -0.9 \\ -0.9 & 1\end{pmatrix}$, $\Sigma_w = I$, $\delta_{\text{critical}} = (1.7, 1.7)$ — per-coordinate says PASS, matrix-Loewner correctly says FAIL with the bad direction $(1, 1)/\sqrt{2}$). The matrix-Loewner form is the canonical anisotropic persistence condition; per-coordinate is its diagonal-$\mathcal{T}$-axis-aligned-$D_\delta$ special case, sharp where the coordinate basis happens to be the correction-machinery's eigenbasis and unsafe outside it. The weak-direction bottleneck argument of this segment generalizes from "the weak coordinate dimension" to "the weak eigendirection of $\Sigma_\infty$ relative to $D_\delta$" in the matrix form.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) is now in `#def-adaptive-tempo`'s Tensor extension sub-block: $\mathcal{T} = \sum_k \nu^{(k)} \cdot K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ the matrix gain operator derived in `#deriv-fisher-local-update-gain`. The per-dimension persistence condition $\mathcal T_k > \rho_k / \delta_{\text{critical},k}$ is the diagonal projection of the tensor form along each natural-gradient direction; the matrix gain $K^{(k)}$ is the per-coordinate primitive this result invokes. Open: tightening this result's Formal Expression to invoke the tensor form directly rather than per-coordinate scalars would make the connection structural rather than discursive.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
