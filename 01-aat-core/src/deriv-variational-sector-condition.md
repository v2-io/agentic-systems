---
slug: deriv-variational-sector-condition
type: derivation
status: conditional
depends:
  - deriv-sector-condition
  - result-sector-persistence-template
  - der-gain-sector-bridge
  - form-strategy-complexity-cost
  - disc-compression-operations
stage: draft
---

# Derivation: Variational Approximate-A2' ($\varepsilon$-Fidelity)

Variational / approximate-posterior agents (VI, amortized VI, active-inference-style variational free energy) currently sit in A2' sub-scope $\beta$ per `#form-sector-condition`: their correction functions target the *best-in-class* variational posterior $q^\ast$ rather than the true posterior $p$, and the approximation gap can rotate the correction direction enough to break B1 directional fidelity ( #der-gain-sector-bridge). Under a KL bound $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$ on the variational approximation, directional fidelity recovers in a quantifiable form: **$\varepsilon$-fidelity B1**, with sector-constant degradation scaling as $O(\sqrt\varepsilon)$ (Pinsker-tight). The sector-persistence template applies under a Regime-A / Regime-B decomposition — clean sector bound on an annulus away from the projection-error floor, approximation-dominated on a ball of radius $\delta_0 = O(\sqrt\varepsilon)$ around the target. This promotes controlled-KL VI from sub-scope $\beta$ to a new intermediate tier $\alpha'$ within the A2' partition (cf. the $\alpha$ / $\alpha_1$ / $\alpha_2$ / $\beta$ refinements from `#deriv-adaptive-gain-dynamics` and `#deriv-fisher-whitened-update-rule`).

The result has a striking operational consequence: **mean-field VI is structurally sub-optimal as an adaptive system by a factor $\sqrt{1-r^2}$ in the sector constant, regardless of compute or training data**, because the mean-field family does not match the Fisher metric. **Natural-gradient VI recovers the full sector parameter** (Khan-Lin 2017 conjugate-computation equivalence places it in full sub-scope $\alpha$ rather than $\alpha'$) because the natural-gradient direction matches the Fisher metric — no degradation. Where persistence-optimality matters, the variational-family choice is not interchangeable; the long-running Bayesian-deep-learning practical preference for natural-gradient over mean-field has a principled persistence-theoretic reading inside AAT.

## Formal Expression

### $\varepsilon$-fidelity B1

*[Derived (eps-fidelity-B1, from Pinsker + Cauchy-Schwarz)]*

Let the true posterior be $p(z \mid x)$ and the variational approximation $q_\phi(z \mid x)$ with $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$. Under standard Lipschitz assumptions on the observation model and nested-support on the variational family, the total-variation distance bounds as $\lVert q_\phi - p\rVert_{TV} \leq \sqrt{\varepsilon/2}$ (Pinsker's inequality). Propagating this bound through the correction function via Cauchy-Schwarz:

$$(K\hat P - P^\ast)^T (\hat P - P^\ast) \geq (c_{\min} - C_H \sqrt{2\varepsilon}/\lVert\delta\rVert) \cdot \lVert\delta\rVert^2$$

where $C_H$ is a constant depending on the observation-model Lipschitz constant. The effective sector constant

$$c_\varepsilon(\lVert\delta\rVert) = c_{\min} - C_H\sqrt{2\varepsilon}/\lVert\delta\rVert$$

is state-dependent: large-mismatch regions see near-full sector constant; near-target regions see degraded sector constant due to approximation error dominating.

### Regime-A / Regime-B decomposition

*[Formulation (regime-decomposition-variational)]*

Define $\delta_0 = 2 C_H \sqrt{2\varepsilon}/c_{\min}$ (the approximation-dominated radius around target). Then:

- **Regime A — clean sector bound** ($\lVert\delta\rVert \gt 2\delta_0$). On the annulus $\mathcal B_R \setminus \mathcal B_{2\delta_0}$, $c_\varepsilon \geq c_{\min}/2$: sector condition holds with constant $c_{\min}/2$. The template's ultimate bound $\rho_\xi / (c_{\min}/2)$ applies.
- **Regime B — approximation-dominated floor** ($\lVert\delta\rVert \leq 2\delta_0$). Near target, $c_\varepsilon$ can be arbitrarily small; the correction may not contract. The ultimate bound gains an additive $O(\sqrt\varepsilon)$ term: $R^\ast_\varepsilon = \rho_\xi/(c_{\min}/2) + \delta_0 = \rho_\xi/(c_{\min}/2) + O(\sqrt\varepsilon)$.

Sector-persistence template instantiates with:
- State variable $\xi = \hat P - P^\ast$ (variational mismatch to target posterior).
- Effective ultimate bound $R^\ast_\varepsilon$ on Euclidean norm.
- Persistence requires $R^\ast_\varepsilon \lt R$, i.e., $\rho_\xi/(c_{\min}/2) + O(\sqrt\varepsilon) \lt R$.

Khasminskii stopping-time localization (same technique as `#deriv-sector-condition` Prop A.1S and the A2' strengthening spike) applies to the annulus Regime A; Regime B is handled by accepting $\delta_0$ as a projection-error floor.

### Per-case verdicts

*[Derived (per-variational-case)]*

The $\alpha'$-membership depends on the specific variational scheme:

**Natural-gradient VI with exponential-family $q_\phi$.** Khan & Lin 2017 (*Conjugate-computation variational inference*) showed natural-gradient VI is equivalent to closed-form conjugate-Bayesian updates for exponential-family variational distributions. This recovers *full* sub-scope $\alpha$ membership (not merely $\alpha'$), with A2' derived rather than $\varepsilon$-degraded, by converting the variational update into a Bayesian update in a reparameterized family. The $\varepsilon = 0$ limit is exact.

**Mean-field VI.** When the true posterior is approximately factorized ($p(z) \approx \prod_i p_i(z_i)$), mean-field VI achieves small $\varepsilon$ and is the workhorse $\alpha'$ case. Ultimate bound degrades by additive $O(\sqrt\varepsilon)$; sector persistence holds.

**Amortized VI (VAE-style).** Amortization adds a second approximation error (the variational network's function-class limit). KL bounds compose *additively*: $\delta_0$ grows as $\sqrt{\varepsilon_{\text{family}} + \varepsilon_{\text{amort}} + \varepsilon_{\text{generalization}}}$. Under controlled-$\varepsilon$ amortized VI, $\alpha'$ membership holds with a larger floor.

**Diffusion-posterior / energy-based with uncontrolled MCMC.** No controlled $\varepsilon$ bound; $\varepsilon$ grows with mixing time. Stays firmly in sub-scope $\beta$.

**Active inference (variational free energy).** Conditional $\alpha'$ under exponential-family $q$ + natural-gradient; $\varepsilon$-degraded $\alpha'$ otherwise. This does **not** force V-strong G-BP2 (presentation of AAT as control-theoretic specialization of active inference) — V-medium (KL-divergence-based cognitive cost) remains the appropriate scope commitment; the comparison trail is in the spike-routing cycle (CHANGELOG 2026-05-17).

### Sub-scope $\alpha'$ in the A2' partition

*[Derived (sub-scope-alpha-prime-partition)]*

The A2' sub-scope partition is structured as:

- **Sub-scope $\alpha$** (derived under B1 directional fidelity; `#der-gain-sector-bridge`): Kalman, conjugate Bayesian, exponential-family natural parameters, strongly-convex gradient, L2-regularized, linear-PD-symmetric.
- **Sub-scope $\alpha_1$/$\alpha_2$** (`#result-contraction-template`): metric-formulation generalization of $\alpha$.
- **Sub-scope $\alpha_3$** (`#deriv-fisher-whitened-update-rule`): correlated evidence + Fisher-whitened under (PI)/Čencov.
- **Sub-scope $\alpha'$** (this segment): controlled-KL VI under Pinsker's inequality with $O(\sqrt\varepsilon)$ sector-constant degradation + Regime-A/B decomposition.
- **Sub-scope $\beta$**: uncontrolled-$\varepsilon$ agents; non-smooth rule-based; severely misspecified; per-step SGD; human judgment.

This gives the full current picture: $\{\alpha, \alpha_1, \alpha_2, \alpha_3, \alpha', \beta\}$.

## Epistemic Status

*Conditional.* Max attainable: *exact* for the Pinsker-bound derivation (standard inequality). The $O(\sqrt\varepsilon)$ rate is tight in general — improving to $O(\varepsilon)$ requires stronger inequalities (log-Sobolev, Talagrand T2) holding for the specific variational family and target; not chased in this segment but is a potential refinement for concentration-preserving families.

**Load-bearing:**
- Pinsker + Cauchy-Schwarz gives the $O(\sqrt\varepsilon)$ rate rigorously.
- Regime-A annulus sector bound with $c_{\min}/2$ is derived (straightforward bookkeeping on the state-dependent $c_\varepsilon$).
- Natural-gradient VI promotion to full $\alpha$ is standard (Khan & Lin 2017).
- Mean-field VI as workhorse $\alpha'$ is standard variational analysis.

**Not established:**
- $O(\varepsilon)$ rate (would require stronger inequalities).
- Quantitative $\varepsilon$ bounds for specific variational families in practice (amortization gaps are typically not estimable tightly).
- $\alpha'$ membership under mode-missing VI (multimodal posteriors where $q$ concentrates on a subset of modes). These may require separate analysis.

## Honest Failure Modes

*[Scope honesty — variational-alpha-prime-limits]*

- **Uncontrolled-$\varepsilon$ agents**: diffusion posteriors with finite MCMC; VAEs trained without KL control; any VI without a bounded-$\varepsilon$ certificate. Stays in $\beta$.
- **Mode-missing on strongly multimodal posteriors**: $q$ misses modes; $\varepsilon$ is irreducible regardless of optimization. $\alpha'$ fails structurally.
- **Non-Lipschitz observation models**: the $C_H$ constant diverges; the Pinsker propagation bound doesn't hold. $\alpha'$ fails.
- **Support mismatch**: $q$'s support is not a subset of $p$'s support (or vice versa); KL is $+\infty$. $\alpha'$ fails.
- **Non-exponential-family + non-amortized + uncontrolled + multimodal**: the worst case, strictly $\beta$.

## Discussion

**Relationship to `#form-strategy-complexity-cost`.** The G-BP2 V-medium variational form landed in `#form-strategy-complexity-cost` uses KL divergence in the cognitive-cost term. This segment provides the complementary story on the persistence side: KL-bounded VI has $\varepsilon$-fidelity B1 and $\alpha'$ sector condition. The two together characterize the cognitive/persistence tradeoff for variational agents: $\varepsilon$ controls both the cognitive cost (how far from the target) and the persistence degradation (how much sector-constant penalty). Large $\varepsilon$ means cheap-but-persistently-weak; small $\varepsilon$ means expensive-but-persistently-sharp.

**Relationship to `#disc-compression-operations`.** Variational compression is the first of the four AAT compression operations; its $\alpha'$ sector structure gives a concrete persistence guarantee for variational representation of $M_t$. The other three operations (strategy $\Sigma_t$, shared-intent, coarse-graining $\Lambda$) may admit similar $\varepsilon$-fidelity analyses where a KL-bound on the compression is available.

**Meta-pattern positioning.**
- *`#disc-separability-pattern`*: $\alpha'$ sits on the structured-repair tier of the A2'-scope ladder (7th ladder from `#result-contraction-template`), alongside metric-$\alpha_2$ and $\alpha_3$. Each represents "sector condition recovered under explicit additional structure."
- *`#disc-additive-coordinate-forcing`*: variational persistence sits *outside* this meta-pattern — no logarithmic coordinate is forced; Pinsker is a bound, not a Cauchy-FE argument. $\alpha'$ is an adjacent family member (shape: controlled-approximation-with-quantified-degradation), not a primary instance.

## Working Notes

- Landing context: `spikes/spike-variational-a2prime.md` (2026-04-23 Gap A/B cycle).
- **Open: $O(\varepsilon)$ rate via Talagrand T2.** For concentration-preserving variational families with log-Sobolev or T2-Talagrand inequalities, the Pinsker bound can be sharpened to $O(\varepsilon)$ directly (without square-root). Not chased here; would extend $\alpha'$ to a tighter sub-tier for specific family classes.
- **Amortization gap bounds.** Generalization-gap analysis for VAEs (Rainforth et al. 2018; Nowozin 2018) gives function-class error bounds; composing with variational-family error gives the full $\delta_0$ in amortized VI. Follow-up work.
- **Connection to natural-gradient VI.** Khan & Lin 2017's conjugate-computation framing makes natural-gradient VI full sub-scope $\alpha$ (not just $\alpha'$). The $\alpha'$ tier is for *non-natural-gradient* VI under KL control.
