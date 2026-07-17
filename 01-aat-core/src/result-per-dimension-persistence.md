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

The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions. *The weak dimension is the bottleneck*: it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension, derived from the same Lyapunov argument applied dimension-by-dimension. Under Model D (bounded deterministic disturbance) persistence requires $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ for each dimension $k$; under Model S (Gaussian stochastic disturbance) the per-dimension AR(1) stationary distribution supplies three task-adequacy criteria (RMS / MAE / probability bound) related by exact constants. The exact thresholds differ by model and criterion, but the structural form — *weak dimension limits aggregate persistence* — is robust across all variants.

The result is *load-bearing for adversarial dynamics*. An attacker who identifies the target's weak dimension can concentrate disturbance there: the same total disturbance budget concentrated on the weak axis amplifies the mismatch ratio asymmetrically while aggregate metrics still look acceptable, and structural failure follows when that one dimension exceeds its $\delta_{\text{critical},k}$ threshold even with healthy aggregate $\lVert\delta\rVert_{L_2}$. Per-dimension monitoring is therefore not optimization polish but a structural requirement for any agent operating under directed pressure. The full adversarial-targeting machinery (the 16-cell emitter-recipient composition in `#der-agent-opacity` with closed-form arg-max) operates on this per-dimension structure, exploiting the asymmetry the scalar persistence condition hides. The matrix-Loewner persistence formulation `#deriv-matrix-persistence-condition` is the strictly sharper canonical form under cross-dimensional correction (off-diagonal $\mathcal{T}$, eigenbasis misalignment with coordinates); the per-dimension form here is the diagonal-$\mathcal{T}$ + axis-aligned-$D_\delta$ special case, sharp inside that regime and unsafe outside it.

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

1. **Model D threshold** ($\mathcal{T}_k \gt \rho_k/\delta_{\text{critical},k}$) follows from Prop A.1 applied per dimension — the same Lyapunov argument with bounded disturbance, restricted to each coordinate. This is exact under GA-2 + GA-3.

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

**Implications for the persistence condition.** Like the scalar result, per-dimension persistence addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery on each dimension can outpace that dimension's disturbance rate. An agent can be structurally persistent on every dimension while still being operationally fragile on one (near its per-dimension $R_k$ boundary). The scalar persistence condition ( #result-persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition has two forms: Model D ($\mathcal{T}_k \gt \rho_k/\delta_{\text{critical},k}$, exact under bounded disturbance) and Model S ($\eta_k \gt \rho_k^2/(\pi \cdot \delta_{\text{critical},k}^2)$, exact under Gaussian disturbance). Both predict per-dimension failure correctly; the choice depends on the disturbance character in the domain.

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
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) is now in `#def-adaptive-tempo`'s Tensor extension sub-block: $\mathcal{T} = \sum_k \nu^{(k)} \cdot K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ the matrix gain operator derived in `#deriv-fisher-local-update-gain`. The per-dimension persistence condition $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ is the diagonal projection of the tensor form along each natural-gradient direction; the matrix gain $K^{(k)}$ is the per-coordinate primitive this result invokes. Open: tightening this result's Formal Expression to invoke the tensor form directly rather than per-coordinate scalars would make the connection structural rather than discursive.
- Simulation code: `../../empirica/track-b-nonlinear/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.

### Incidental audit gold (gold-lift sweep, A15, 2026-05-31)

Cross-audit "wandering thoughts" / §14 ideation, deduplicated and lightly attributed. *Orthogonal* pedagogical / framing / forward-vision material staged for an eventual separate promotion pass. **Coverage:** four dirs reached a digested reflection (193847 Gemini, 829314 Gemini, 849201 Gemini, 451729 Claude batched §III batch-15). Rated very-high felt value across substrates ("destroys the illusion of the average agent"). Finding-vs-framing conflation preserved.

#### 1. Candidate Brief prose / pre-prose

- The headline as a one-liner readers keep reaching for: **"survival is a `min()`, not an `average()`."** An agent scoring 99/100 on 99 tasks and 0 on "don't delete the production database" looks ~98% capable on a scalar metric, but persistence is determined entirely by that 0 — and an adversary attacks the 0, not the 99 (Gemini, 829314). Strong Brief / Discussion anchor; tighter than the current "weak dimension is the bottleneck."
- **"You cannot prove an AI is safe *on average* if safety is a multi-dimensional requirement"** — the same point in the safety-evaluation register (Gemini, 849201; Claude, 451729).

#### 2. Candidate Discussion

- **The quadratic-noise asymmetry, dramatized.** Model S threshold is quadratic in $\rho_k$ ($\eta_k \gt \rho_k^2/2\delta_{\text{critical},k}^2$) while Model D is linear: double the environmental noise and you need *four times* the gain, not twice. Because $\eta_k$ is bounded ($0\lt\eta_k\lt 1$ in standard discrete updating) and by hardware, a quadratic requirement hits the ceiling fast — "a noisy environment doesn't linearly degrade persistence, it mathematically crushes the *possibility* of persistence far faster than a systematically drifting one does" (Gemini, 829314). A candidate Discussion paragraph making the linear-vs-quadratic split *consequential*, not just stated.
- **Scalar AI capability metrics, dynamics-grounded critique.** This result supplies a Lyapunov-grounded argument for why AI-safety evaluation must be per-dimension / worst-case, not aggregate: aggregate scores systematically over-predict adaptive capacity (the calibrated 72% overestimate is the quantitative evidence), and the adversarial-ML literature's per-feature attack budgets (Szegedy, Madry et al.) are the empirical rediscovery of the same phenomenon — AAT gives the formal grounding for *why* per-dimension is necessary, not merely useful (Claude, 451729; the segment's Findings already cite adjacency, this is the sharpened Discussion framing). The "red-teaming works because the adversary needs only the one dimension with the largest $\rho_k/\eta_k$, not global superiority" gloss is the operational complement (Gemini, 193847).
- **Isotropic allocation as a normative design principle.** "Spreading tempo evenly reduces the bottleneck penalty / isotropic allocation dominates" — flagged as practically useful and worth surfacing as an explicit design corollary rather than leaving implicit (Gemini, 849201).

#### 3. Follow-up items

- **Cross-dimensional / coupled-correction regime.** Off-diagonal correction (fixing one dimension improves/degrades another — the definition of transfer learning / structural generalizability) breaks the diagonal-$\eta$ assumption and needs full-covariance analysis. *Status: largely closed* — `#deriv-matrix-persistence-condition` lifts the per-coordinate form to matrix tempo (see the WN bullet above); the open empirical question auditors raise is whether a *highly coupled* model (large off-diagonals) survives *better* than an independent one in this framework (Gemini, 849201; Gemini 193847; Claude 451729 implicit).

#### 4. Readers often ask / wonder

- **"How does an adversary actually *aim* its disturbance at a specific dimension — does it require a Model of the target's Model (Level-3 theory of mind)?"** A natural reader question once weakest-dimension targeting is named; a sentence pointing at `#der-agent-opacity` / the 16-cell targeting machinery would preempt it (Gemini, 849201).

#### Belongs elsewhere

- **Forward-vision (ELI / "Society of Mind" architecture, `04-eli-core/`).** The dark side of comparative advantage: a specialist has high $\eta_k$ on one dimension and $\approx 0$ elsewhere, so it is entirely dependent on the *composite* to shield its weak dimensions — if internal routing $\mathcal{N}_t$ fails and the sub-agent is exposed to an out-of-specialty disturbance, it instantly shatters ($\rho_k\gg R_k$). Therefore robustness requires a **generalist floor**: every sub-agent must carry a minimum baseline $\eta$ across *all* vital dimensions even while specializing, or the composite cascades on routing failure — "you cannot build a resilient mind entirely out of idiot-savants." A derived-feeling architecture constraint pointing at logozoetic composite design, not this segment (Gemini, 193847).

#### Off-ramp (NOT gold) — routed for adjudication, not promotion

- **(193847 poke — genuine, load-bearing) — the "weakest link" claim presupposes a conjunctive ($L_\infty$) failure boundary.** "Weak dimension is the bottleneck" is rigorous only if survival requires $\lvert\delta_1\rvert\lt c_1$ *and* $\lvert\delta_2\rvert\lt c_2$ (a hypercube / $L_\infty$ boundary). If the objective functional $V_O$ is a smooth $L_2$ norm (total Euclidean distance from target), excelling on dimension 1 *can* compensate for dimension 2 within an $L_2$ budget — the segment computes $\lVert\delta\rVert_{L_2}=0.785$ and calls it an overestimate, but under an $L_2\lt 1.0$ boundary the agent *survived*. The segment conflates the *anisotropy of the error vector* with the *geometry of the failure condition*. Recommended discharge (a strengthening): state the failure-boundary-geometry assumption explicitly — for most complex biological/software systems survival is *conjunctive* across vital dimensions (working memory AND working actuators; excess memory doesn't fix broken actuators), so the boundary is a hypercube and the $L_\infty$ norm governs, which *makes the weakest-link claim rigorous* and cleanly justifies the "specialists compose better than generalists" close. This is a named-scope-condition strengthening, not a softening — flag for adjudication / a possible spike. (526815 did not reach this segment, so the deeply-mathematical track has no finding here; this $L_\infty$ poke is the strongest certified-track item and comes from the Gemini adversarial-audit pass.)
