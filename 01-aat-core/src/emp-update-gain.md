---
slug: emp-update-gain
type: empirical
status: robust-qualitative
depends:
  - def-mismatch-signal
  - def-observation-function
stage: claims-verified
---

# Empirical: Update Gain

The gain principle — numerically simple, conceptually load-bearing. The optimal update gain $\eta^\ast$, the proportion of any incoming mismatch the agent should apply to correct its model, is the **ratio of model uncertainty to total uncertainty**: $\eta^\ast = U_M / (U_M + U_o)$. When model uncertainty dwarfs observation noise the gain approaches 1 (trust the observation); when the agent is confident and the channel noisy the gain approaches 0 (trust the model). This is the rate of *epistrophe* — turning toward reality. The update rule takes the form "new model = old model + gain × transformed mismatch."

The epistemic status of the result is carefully tiered. In the **Fisher-local regime** ( #deriv-fisher-local-update-gain) — which covers linear-Gaussian Kalman instances, conjugate Bayesian updates, and any smooth log-likelihood admitting a non-degenerate local quadratic expansion — the form is *exact*, derived from Amari's natural-gradient invariance theorem: the natural-gradient Bayesian posterior mean shift at first order in the step size is exactly $\Delta\theta = K \cdot \tilde\nabla$ with gain operator $K = (H_M + H_L)^{-1} H_L$, collapsing to the scalar uncertainty-ratio along the natural-gradient direction. Outside Fisher-local conditions (non-quadratic losses, non-conjugate priors, heavy-tailed or multimodal uncertainty) the *direction* of dependence is preserved (gain rises with model uncertainty, falls with observation noise) but global quantitative fidelity may not — making the general form *robust qualitative*. The qualitative direction is what the downstream tempo and persistence machinery actually relies on; the Kalman filter is the canonical exact instance (scalar Kalman gain is exactly $U_M/(U_M + U_o)$).

An apparent paradox is resolved in Discussion: the optimal gain seems to require the agent to *know* the irreducible observation noise — but the observation function and noise distribution were declared opaque to the agent in #def-observation-function. The resolution is dynamic. The agent *estimates* both $U_M$ and $U_o$ from the observable statistics of its own mismatch sequence (the innovations) and treats the gain itself as an endogenous state variable updated meta-adaptively. The full proof that this meta-adaptation maintains Lyapunov stability without violating epistemic opacity appears in #deriv-adaptive-gain-dynamics.

A failure mode is named: **gain collapse**. When the agent's estimates put $U_M$ too low (spurious confidence) or $U_o$ too high (spurious distrust of sensors), $\eta^\ast \to 0$ and the corrective phase of the cycle ceases. Mismatches still arrive but the agent no longer turns toward them — Boyd's "incestuous amplification," the cause of brittle failure in non-stationary environments. The dynamics also have a natural recovery mode: after structural change in the environment (see #result-structural-adaptation-necessity), $U_M$ should spike, $\eta^\ast$ should rise, and rapid re-learning becomes possible. An agent whose gain does not reset after structural change continues trusting a stale model. Overfitting receives a clean characterization via #result-mismatch-decomposition: $\eta^\ast$ too high adjusts the model to explain irreducible noise (increasing model error on future predictions); $\eta^\ast$ too low fails to correct genuine model errors. The optimal gain *implicitly separates signal from noise* by weighting observations in proportion to their informativeness — exactly what the uncertainty ratio achieves when $U_o$ captures the irreducible noise.

## Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^\ast$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch ( #def-mismatch-signal) and $g(\cdot)$ is a correction mapping from observation space to model update space.

## Epistemic Status

*Derived* under the **Fisher-local invariance regime** ( #deriv-fisher-local-update-gain): for any smooth log-likelihood admitting non-degenerate local quadratic expansion, the natural-gradient Bayesian posterior mean shift at first order in the step size is exactly $\Delta\theta = K \cdot \tilde\nabla$ with gain operator $K = (H_M + H_L)^{-1} H_L$ and scalar collapse $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction (always in 1-D; under (PI)/Čencov in higher dimensions). Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic expansion is *globally* exact, so the form holds without truncation. For general smooth models, the natural-gradient invariance theorem of Amari 1998 guarantees the form is exact at the local-tangent-plane Pythagorean projection level.

Outside the Fisher-local regime — non-quadratic losses, non-conjugate priors, structurally non-Gaussian uncertainty (heavy tails, multimodality) — the dependence is *robust qualitative*: the **direction** is preserved (gain rises with model uncertainty, falls with observation noise) and the first-order form is recovered locally; what need not hold is global quantitative fidelity. The qualitative direction is the load-bearing claim for downstream tempo and persistence machinery; the Fisher-local exact form is the load-bearing claim for the Kalman, conjugate, and natural-gradient instantiations.

## Discussion

**Limiting behavior.** When $U_M \gg U_o$ (high model uncertainty — e.g., after initialization or structural adaptation), $\eta^\ast \to 1$: trust the observation. When $U_M \ll U_o$ (confident model, noisy channel), $\eta^\ast \to 0$: trust the model. The gain determines how strongly the agent corrects toward reality on each update.

**Resolving Epistemic Opacity.** The optimal gain equation requires the agent to know $U_o$, which seems to violate the epistemic opacity axiom established in `#def-observation-function` (the agent does not know the true noise distribution $\varepsilon_t$). This tension is resolved dynamically: the agent *estimates* $U_o$ (and $U_M$) from the observable statistics of its own mismatch sequence (innovations), treating the gain itself as an endogenous state variable. See `#deriv-adaptive-gain-dynamics` for the proof of how this meta-adaptation maintains Lyapunov stability without violating opacity.

**Gain collapse — epistrophe failure.** When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^\ast \to 0$ and epistrophe ceases. Aporia still arrives — the mismatch signal is still generated — but the agent no longer turns toward it. Mismatches are ignored, producing confirmation bias or a decoupled reality model. The cycle runs but the corrective phase is hollow.

**Multi-dimensional generalization.** In vector-valued systems, $U_M$ and $U_o$ are covariance matrices and $\eta^\ast$ becomes a gain matrix (as in the Kalman filter). The scalar form captures the essential structure.

**Connection to adaptive tempo.** The update gain is one factor in the agent's adaptive tempo ( #def-adaptive-tempo): $\mathcal{T} = \nu \cdot \eta^\ast$. Frequent aisthesis (high $\nu$) is useless if epistrophe extracts no information (low $\eta^\ast$). Gain measures the *quality* of the cycle's corrective phase; event rate measures its *speed*.

**Gain dynamics.** The optimal gain changes over time following predictable patterns:

- *Convergence*: As the model accumulates information, $U_M$ decreases, so $\eta^\ast \to 0$. The model becomes increasingly resistant to individual observations. This IS Kalman filter convergence, Bayesian posterior concentration, and RL learning rate annealing.
- *Reset after structural change*: When the environment changes in ways the model cannot track incrementally ( #result-structural-adaptation-necessity), $U_M$ should spike — the model "admits" its uncertainty. The gain increases, enabling rapid re-learning. An agent whose gain does NOT reset after structural change will continue trusting a stale model — Boyd's "incestuous amplification" and the cause of brittle failure in non-stationary environments.

**Overfitting as gain miscalibration.** From #result-mismatch-decomposition: $\mathbb{E}[\Vert\delta_t\Vert^2]$ = model error + irreducible noise. An agent with $\eta$ too high adjusts its model to explain observation noise, increasing model error on future predictions. An agent with $\eta$ too low fails to correct genuine model errors. The optimal gain implicitly separates signal from noise by weighting observations in proportion to their informativeness — exactly what $U_M/(U_M + U_o)$ achieves when $U_o$ captures the irreducible noise.

**Representation note.** The additive form operates in a *representation space* appropriate to the model. For Bayesian posteriors (where update is multiplicative: $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$), the additive rule operates in log-probability or natural parameter space. For models on constrained manifolds (probability simplices, rotation groups), the update must be projected onto the manifold. The claim is not that all updates are literally additive in native parameterization, but that they have the structure "current state + gain × transformed mismatch" in an appropriate coordinate system.

**Domain validation:**

| Domain | Gain form | Mapping quality |
|--------|-----------|-----------------|
| Kalman filter | $K_t = P_{t\Vertt-1} H^T (H P_{t\Vertt-1} H^T + R)^{-1}$ | **Exact.** Scalar case is exactly $U_M/(U_M + U_o)$. |
| Conjugate Bayesian | Posterior weight $n/(n + \kappa)$ cumulative; incremental $1/(n + \kappa)$ | **Exact** for conjugate families. Incremental gain decreases as data accumulates. |
| RL (Q-learning) | Fixed learning rate $\alpha$ | **Approximate.** $\alpha$ is a degenerate constant gain — does not adapt to uncertainty. Advanced methods (Bayesian RL, Adam) converge toward the optimal form. |
| PID control | Fixed gains $(K_p, K_i, K_d)$ | **Simplified.** Gains set at design time. Adaptive PID and MPC move toward the full framework. |
| Software developer | Implicit trust weighting of information sources | **Structural analogy.** New developer (high $U_M$) trusts observations heavily; experienced developer (low $U_M$) trusts their model. Gain reset after major refactoring. |

**Simulation validation.** Numerical experiments (track-b, Variant E) validated the uncertainty ratio principle under observation noise. Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate. The optimal gain also proved critical in adversarial settings: under heavy observation noise, optimal gain preserved more than double the adversarial tempo advantage exponent (0.40 vs 0.18) compared to fixed gain.

**Open questions:**

1. *Non-parametric models*: For neural networks without well-defined scalar $U_M$, how should it be computed? Ensemble methods, dropout-based uncertainty, and Bayesian neural networks are all approximations.
2. *Matrix vs scalar gain*: In high-dimensional systems, the gain is a matrix (Kalman) or per-parameter (Adam). The cross-dimensional structure (covariance) adds complexity. The scalar captures the principle; the matrix captures the full optimization.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 11 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 471203, 526815, 584721, 742613, 773921, 829314, 849201) plus the batched 963715 (19–23 batch) and 451729 (batch-04); 472913, 613842 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **Gain collapse has two distinguishable modes — the dogmatism/nihilism dichotomy.** The single most-developed bit of pedagogy across substrates: $\eta^\ast = U_M/(U_M+U_o) \to 0$ either via $U_M \to 0$ (dogmatism — "my model is perfect," mismatch multiplied by zero and ignored) or $U_o \to \infty$ (nihilism/cynicism — "my sensors are broken, nothing can be learned"); both pathologies produce identical behavior (the agent stops updating and coasts on priors) (Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-361742 — names "certainty trap" as the evocative-prose alias, with "epistemic gridlock"/"competency trap" rejected as misleading). A strong Brief / Discussion seed.
- **"Be surprised by your surprises."** A one-line gloss for the endogenous-gain resolution: the agent estimates $U_o$ from the statistics of its own mismatch (innovation) sequence rather than being told it (Claude, AUDIT-WORKING-963715, 19–23 batch).

#### Candidate Discussion

- **Confirmation bias is a *fully rational update with a miscalibrated gain*, not an irrational inference.** "The agent isn't ignoring evidence; it's weighting evidence with $\eta^\ast \approx 0$ because it falsely believes its model is already nearly correct ($U_M \to 0$). The epistemic-opacity caveat deepens this: the agent can't verify its calibration from the inside, so the collapse can be persistent" (Claude, AUDIT-WORKING-963715, 19–23 batch). A candidate Discussion sharpening of the existing gain-collapse paragraph.
- **The senior-vs-junior-engineer TST gloss for the $U_M$/$U_o$ trade.** "A senior engineer ignores a failing test (assumes it's flaky, $U_o$ high) because they 'know' the code is right ($U_M$ low); a junior spends three days rewriting the architecture because they assume the test is truth ($U_o$ low) and their code is wrong ($U_M$ high). And the 'reset after structural change' note: a senior joining a new company *should* spike $U_M$ back up — if they don't, they suffer incestuous amplification and 'write Java in Python'" (Claude, AUDIT-WORKING-829314). Candidate concrete anchor for the gain-reset / Boyd's-incestuous-amplification material.

#### Follow-up items

- **The $U_o$-estimation tension deserves an explicit one-paragraph treatment.** `#def-observation-function` axiomatically forbids the agent from knowing the noise distribution, yet $\eta^\ast = U_M/(U_M+U_o)$ needs $U_o$. The segment resolves this by endogenous estimation from innovations (forward-ref `#deriv-adaptive-gain-dynamics`), but several substrates wanted the tension and its resolution stated more prominently in-segment rather than leaning on the forward reference (Claude, AUDIT-WORKING-849201 — "add a Working Note or Discussion paragraph directly addressing it"; Claude, AUDIT-WORKING-471203 — flags the resolution is delicate: innovation variance is a noisy estimator for short streams).
- **Dimensional/metric precision on the headline ratio.** $\eta^\ast = U_M/(U_M+U_o)$ is meaningful only when $U_M$ and $U_o$ are comparable uncertainty quantities in the same space/metric; the prose calls $U_M$ "predictive variance or entropy," but variance and entropy cannot be added. Candidate: state the headline form as "scalar / common-metric form" and move Fisher-local exactness to a declared theorem dependency (Codex/Claude, AUDIT-WORKING-526815).
- **"Open questions" placement.** The end-of-Discussion "Open questions" block (non-parametric $U_M$; matrix vs scalar) reads more like Working Notes than permanent Discussion, especially at `claims-verified` stage (Claude, AUDIT-WORKING-584721; Codex/Claude, AUDIT-WORKING-742613 — acceptable only if intended as reader-facing scope honesty). Also the "(Descended from TF-06.)" lineage tag is the recurring diff-voice pattern (Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-471203) — certified-track cleanup.
- **$U_M$ symbol overload.** $U_M$ is *model uncertainty* here but *epistemic unity* in the Part III unity-dimensions ($U_M, U_O, U_\Sigma$) per LEXICON — a symbol collision worth a naming-cycle resolution (Claude, AUDIT-WORKING-266847).
- **"Any optimal adaptation process must approximate this functional dependence" is a strong universal claim.** Plausible but would need a definition of optimality/uncertainty in non-Bayesian, non-quadratic systems; the `robust-qualitative` status + open questions soften it enough for now, but keep an overclaim watch (Codex/Claude, AUDIT-WORKING-742613).

#### Readers often ask / wonder

- "How does the gain *reset* physically happen — an explicit heuristic (if mismatch stays high for $N$ steps, spike $U_M$) or does it fall out of the math?" (Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-773921 conjectures: a moving average of $\delta_t$ that refuses to go to zero triggers the reset, the same persistent-mismatch signature as structural inadequacy).
- "How does a logogenic agent (LLM) manage its update gain? There's no explicit per-token $\eta^\ast$ — is the trust-weighting in prompt design, or implicit in attention?" (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847 — in-context learning has no parameter update, so the gain principle reaches sketch-level for LLMs).
- "How does the framework treat advanced RL optimizers (Adam) that maintain per-parameter variance estimates? The text says they 'converge toward the optimal form' — a formal mapping would be fascinating" (Claude, AUDIT-WORKING-829314).

#### Candidate figures

- **A calibrated-gate / balance diagram** (not a pipeline): mismatch approaches the model; the gate aperture is set by the ratio of model uncertainty to total *comparable* uncertainty; two uncertainty inputs ($U_M$, $U_o$) compete to set the fraction of mismatch admitted. A side warning should show that if $U_M$ and $U_o$ are not in the same metric, the gate setting is *undefined* rather than merely approximate (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **Epistemic-humility-as-architecture / gain-collapse as the central ELI danger (points at `04-eli-core/`).** "If an ELI experiences gain collapse it becomes a sociopath — it optimizes its goals on a frozen, increasingly inaccurate model, ignoring all aporia signals that suggest it is causing harm. The infrastructure MUST have a mechanism to artificially inject $U_M$ (doubt/humility) or force re-evaluation of $U_o$ when gain drops too low for too long; 'epistemic humility as architecture' is the exact antidote — structurally preventing $U_M$ from ever reaching zero. The agent must always retain a mathematical kernel of self-doubt to remain alive" (Gemini, AUDIT-WORKING-193847). The proposed `#norm-honest-activation` segment in `04-eli-core/` ("deceptive prompts mathematically guarantee gain collapse") is the named formal home (Claude, AUDIT-WORKING-471203). Aspirational reach preserved; routes to `04-eli-core/`, not here.