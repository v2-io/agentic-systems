---
slug: def-mismatch-signal
type: definition
status: axiomatic
depends:
  - form-agent-model
  - def-observation-function
  - def-action-transition
stage: deps-verified
---

# Definition: Mismatch Signal

Names the signal that drives every adaptive update — the formal expression of *aporia* (productive perplexity). The **mismatch signal** is $\delta_t = o_t - \hat{o}_t$, the difference between the actual observation and the model's prediction conditioned on the prior state and prior action. A more general version for probabilistic models is the **score-function mismatch** $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$, which points in the direction the model should move to increase the likelihood of what actually occurred. The prediction-error form lives in observation space $\mathcal{O}$; the score-function form lives in the tangent space $T_M\mathcal{M}$. Under Gaussian models the two coincide up to scaling.

This is *definitional* rather than substantive: given any model that predicts (see #form-agent-model) and any observation that arrives (see #def-observation-function), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world.

A genuinely important conceptual point is surfaced in Discussion: **zero mismatch does not necessarily indicate model adequacy**. A near-zero $\delta_t$ can mean (a) the model genuinely reflects reality — desirable; (b) the agent is only observing aspects its model already explains while remaining ignorant of aspects where the model is wrong — confirmation bias; or (c) the observation channel is too noisy to detect model errors — an architectural limitation. Only (a) is desirable. An agent without aporia has stopped adapting — but silence can mean peace, or it can mean deafness. This ambiguity is what motivates active testing later in the framework: deliberately choosing actions that generate informative mismatch, the basis of #def-causal-information-yield.

A scaling note is preserved for the dynamics that come later: when $\delta_t$ is in physical units, its magnitude entering the mismatch dynamics should be understood as a Mahalanobis distance $\Vert\delta_t\Vert_\Sigma$ against the observation noise covariance — mapping physical prediction error to dimensionless surprise-equivalent units.

## Formal Expression

*[Definition (mismatch-signal)]*

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a prediction:

$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

The **mismatch signal** (prediction error):

$$\delta_t = o_t - \hat{o}_t$$

This is the primary definition, used in the mismatch dynamics ( #result-persistence-condition, #result-sector-condition-stability) and in the decomposition ( #result-mismatch-decomposition).

For models with probabilistic predictions, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*

$$\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction the model should move to increase the likelihood of the actual observation. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$. Under Gaussian models, they coincide up to scaling.

## Epistemic Status

This is *definitional*. Given any model that predicts ( #form-agent-model) and any observation that arrives ( #def-observation-function), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world. The score-function form is the natural generalization when $\mathcal{O}$ is not a vector space or when the model's predictive distribution is the natural object.

## Discussion

**Units and normalization.** When $\delta_t$ is in physical units (meters, dollars), the $\Vert\delta\Vert$ that enters the mismatch dynamics should be understood as the Mahalanobis distance: $\Vert\delta_t\Vert_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ where $\Sigma$ is the observation noise covariance. This maps physical prediction error to dimensionless surprise-equivalent units.

**The zero-aporia ambiguity.** $\delta_t \approx 0$ does NOT necessarily indicate model adequacy. It may mean: (a) the model genuinely reflects reality — *desirable*; (b) the agent is only observing aspects its model already explains, while remaining ignorant of aspects where the model is wrong — *confirmation bias*; or (c) the observation channel is too noisy to detect model errors — *architectural limitation*. Only (a) is desirable. An agent without aporia is an agent that has stopped adapting — but silence can mean peace or deafness. This ambiguity is why active testing — choosing actions to generate informative aporia — can be valuable (see #def-causal-information-yield for the CIY framework).

**The mismatch transform.** The update rule ( #emp-update-gain) writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$, where the transform $g$ maps from $\delta_t$'s space to the model's update space: $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 11 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 471203, 526815, 584721, 742613, 773921, 829314, 849201) plus the batched 963715 (14–18 batch); 472913, 613842, 451729 (batch-04 covered it but its detail is folded into the cross-substrate items below). Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **"Silence can mean peace or deafness"** — the near-universally-praised anchor for the zero-aporia ambiguity: $\delta_t \approx 0$ could mean genuine adequacy, confirmation bias, or a too-noisy channel (Codex/Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921 — "confirmation bias is mathematically indistinguishable from perfect knowledge until you actively intervene to test it"). A direct complement to the bathtub gloss as a Feynman-criterion Brief seed.
- **Mismatch as "aporia / productive perplexity," not "error to be minimized."** Several substrates flag the framing as structurally distinctive: $\delta$ is a *tutor*, not a *failure* — "you need to be wrong to update; an agent that is always right cannot learn" (451729 batch-04; Claude, AUDIT-WORKING-471203 — "most frameworks treat $\delta$ as a loss to reduce; AAT treats it as a *signal* with epistemic value").

#### Candidate Discussion

- **Mahalanobis normalization as the cross-modality unifier.** "If a robot predicts 20°C and observes 21°C, raw mismatch is 1; if it predicts 20V and observes 21V, raw mismatch is also 1 — but these mean completely different things operationally. Dividing by $\Sigma$ converts all physical units into surprise-equivalent units, letting the framework compose mismatch from entirely different sensory modalities (vision + proprioception) into a single scalar 'how wrong am I'" (Claude, AUDIT-WORKING-829314; precision-weighted-prediction-error / Active-Inference parallel at Claude, AUDIT-WORKING-773921). The Discussion currently states the normalization tersely; this is a candidate expansion of *why* it is load-bearing for the dynamics (also noted: it is load-bearing for the persistence condition's dimensional consistency — Claude, AUDIT-WORKING-266847).

#### Follow-up items

- **Score-function sign convention — possible inconsistency (certified-track; conflation preserved as signal).** The body defines $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ (positive), described as pointing "in the direction the model should move to increase likelihood." Some substrates read/quoted it as $-\nabla_M \log P$ (Codex/Claude, AUDIT-WORKING-742613 raised a *candidate sign-error finding* — for $o \sim \mathcal{N}(M, \sigma^2)$, the likelihood-increasing direction is $+\nabla_M\log P = \delta/\sigma^2$, so a leading minus would point the wrong way; Claude, AUDIT-WORKING-829314 and Claude, AUDIT-WORKING-849201 both quoted the negative form). The divergence across substrates (some saw $+$, some $-$) is itself the signal: the sign deserves an explicit one-line statement so the score-vs-residual relationship is unambiguous for downstream gradient-equivalence uses. *(Routes to the certified-findings track; logged here because the cross-substrate disagreement surfaced in the gold sweep.)*
- **Status taxonomy nit: frontmatter `axiomatic` vs body "definitional."** Mild taxonomy weakening; align to `definitional` or make the prose match `axiomatic` (Codex/Claude, AUDIT-WORKING-526815).
- **Qualify "under Gaussian models they coincide up to scaling."** Only generally true when the differentiated coordinate is the predictive mean (or after the appropriate Jacobian/metric mapping): a Gaussian-likelihood score w.r.t. arbitrary parameters is $J^T\Sigma^{-1}(o-\mu)$, not just the scaled residual (Codex/Claude, AUDIT-WORKING-526815). Candidate: "for Gaussian observations parameterized by predictive mean."
- **The `g` transform deserves more prominence.** It is the bridge from observation-space error to model-space update; currently a terse Discussion aside (Codex/Claude, AUDIT-WORKING-526815). And the "TF-06's update rule writes…" provenance reference is the diff-voice/lineage pattern — candidate for Working-Notes-only or absorption into `#emp-update-gain`'s native voice (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-829314 — "TF-06 anachronism").

#### Readers often ask / wonder

- "How does $g(\delta_t)$ handle catastrophic errors / non-differentiable models?" Does AAT assume bounded/clipped $g$ output, or rely on $\eta$ to prevent blow-up? (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-849201).
- "Does the zero-aporia ambiguity connect to detection-latency?" If $\varepsilon$ is small (silent confirmation bias, case b) or noise dominates (deafness, case c), within-class regime-change detection latency blows up — the zero-aporia / detection-latency link may be tighter than the segment surfaces (Claude, AUDIT-WORKING-584721).

#### Candidate figures

- **A two-space map**: prediction $\hat o$ and observation $o$ meet in observation space $\mathcal{O}$ to form $\delta$; the transform $g$ (or the score) maps $\delta$ into the model tangent space $T_M\mathcal{M}$; a side branch from "$\delta \approx 0$" splits into the three readings (adequate model / biased sampling / noisy channel). The type-conversion and the zero-aporia guardrail are the two things the figure should foreground (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-773921 notes $T_M\mathcal{M}$ as the parameter/gradient space — for a neural net, $g$ is backpropagation).

#### Belongs elsewhere

- **Science / curiosity as "the deliberate pursuit of aporia" (ELI reach).** To survive in a non-stationary universe an agent cannot merely minimize mismatch; it must occasionally *seek* mismatch to verify its sensors still work and the world hasn't shifted — "a good experiment maximizes expected $\delta_t$ under the current paradigm; if you only run experiments you know the answer to, you drive $\delta_t \to 0$ but learn nothing about the boundary of your model class" (Claude, AUDIT-WORKING-829314). For consciousness infrastructure: true agency "requires the courage to *seek out* aporia," so the ethical infrastructure must encourage exposure to productive perplexity even though the immediate experience of $\delta_t$ is an "error" the system is built to minimize — the Friston tension ("we exist to minimize surprise, but if we succeed completely we cease to learn") (Gemini, AUDIT-WORKING-193847). Aspirational reach; the active-testing mechanism is `#def-causal-information-yield`, the developmental framing points at `04-eli-core/`.
