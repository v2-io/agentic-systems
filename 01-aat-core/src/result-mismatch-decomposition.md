---
slug: result-mismatch-decomposition
type: result
status: exact
depends:
  - def-mismatch-signal
  - def-observation-function
  - def-action-transition
  - form-agent-model
  - scope-adaptive-system
stage: claims-verified
---

# Result: Mismatch Decomposition

The first named *result* of the volume. The expected squared mismatch $\mathbb{E}[\Vert\delta_t\Vert^2]$ decomposes cleanly into three additive parts: an **estimation term** (the gap between the model's predictive mean $\hat o_t$ and the Bayes predictor $\hat o_t^{\mathrm B} = \mathbb{E}[o_t \mid \mathcal C_{t-1}, a_{t-1}]$ — the best any chronica-measurable model could do), a **state-uncertainty floor** (the variance the true conditional mean $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ retains given the interaction history — untouchable by better modeling, movable only by *acting* to make the history more informative), and a **channel-noise term** (the conditional variance of the observation channel itself, given environment state and action). The result is a Pythagorean refinement of the bias-variance decomposition applied to the prediction problem; all cross-terms vanish — one pair under the fresh-noise global assumption GA-1 (observation noise conditionally independent of the past chronica given current environment state and action), the standard assumption in state-space models, and the third because the Bayes predictor is by construction the conditional mean given the history. The model can improve the first term; acting can shrink the second; the third is a property of the channel.

The conceptual stakes of this seemingly mechanical decomposition are large. The result establishes that prediction error is *structurally persistent* in any realistic adaptive regime — there are floors below which mismatch cannot be driven by any amount of better modeling. The channel floor is set by the observation sensor itself. The state-uncertainty floor is set by how much of the environment's state the interaction history pins down: it binds *every* chronica-measurable predictor — including the Bayes-optimal one — whenever residual state uncertainty moves the one-step conditional mean. Deterministic, noiseless, perfectly-specified systems are limiting edge cases, not the typical adaptive regime. The total expected squared mismatch is therefore strictly positive whenever any of the three terms is — and in typical settings all three are.

The decomposition has direct operational consequences picked up downstream. An agent that tries to eliminate *all* mismatch — including the two floors — will overfit, adjusting its model to explain noise and degrading future predictions. The update-gain construct #emp-update-gain implicitly separates signal from noise by weighting observations in proportion to their informativeness, but the floor facts are what make the gain question meaningful at all. The decomposition also clarifies the relationship to #def-model-sufficiency: when $S(M_t) \lt 1$, the model has lost predictive information relative to the full history; under an alignment assumption (the lost information affects the one-step conditional mean) this implies a positive estimation term in the decomposition.

## Formal Expression

*[Derived (result-mismatch-decomposition)]*

For any agent-environment pair within AAT's scope ( #scope-adaptive-system), with $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ the true conditional mean and $\hat o_t^{\mathrm B} = \mathbb{E}[o_t \mid \mathcal C_{t-1}, a_{t-1}]$ the Bayes predictor (the best predictive mean any chronica-measurable model can produce):

$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \hat o_t^{\mathrm B}\Vert^2]}_{\text{(i) estimation error (reducible by modeling)}} + \underbrace{\mathbb{E}[\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})]}_{\text{(ii) state-uncertainty floor (movable only by acting)}} + \underbrace{\mathbb{E}[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{(iii) channel noise (irreducible)}} \gt 0$$

with positivity whenever any term is positive. Grouping (i)+(ii) recovers the coarser bias-variance form $\mathbb{E}[\Vert\hat o_t - \bar o_t\Vert^2] + \mathbb{E}[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]$; the refinement shows that the grouped "model error" is bounded below by the state-uncertainty floor — no chronica-measurable model reduces it to zero.

### Derivation

1. By #scope-adaptive-system, $H(\Omega_t \mid \mathcal C_t) \gt 0$ — residual state uncertainty persists; since $\mathcal C_{t-1}$ is coarser than $\mathcal C_t$, the uncertainty available at prediction time is at least as large. This is what makes term (ii) generically positive (step 4).
2. By #form-agent-model, the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$; $M_{t-1}$ is built from the chronica, so $\hat o_t$ is one of the chronica-measurable predictors over which $\hat o_t^{\mathrm B}$ is optimal. By the tower property and GA-1, $\hat o_t^{\mathrm B} = \mathbb{E}[\bar o_t \mid \mathcal C_{t-1}, a_{t-1}]$.
3. Write $\delta_t = (o_t - \bar o_t) + (\bar o_t - \hat o_t^{\mathrm B}) + (\hat o_t^{\mathrm B} - \hat o_t)$ and expand. All three cross-terms vanish by orthogonality (uncorrelated — not independence). The two involving the noise difference: condition on $(\Omega_t, a_{t-1}, \mathcal C_{t-1})$; the other two differences are then fixed, and $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}, \mathcal C_{t-1}] = \mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$ and the fresh-noise assumption GA-1 ($\varepsilon_t$ conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$). The remaining cross-term: condition on $(\mathcal C_{t-1}, a_{t-1})$; the third difference is fixed, and $\mathbb{E}[\bar o_t - \hat o_t^{\mathrm B} \mid \mathcal C_{t-1}, a_{t-1}] = 0$ by step 2.
4. Term (iii) is positive when observation noise is non-degenerate. Term (ii) is positive exactly when residual state uncertainty *moves the one-step conditional mean* — step 1's $H(\Omega_t \mid \mathcal C_t) \gt 0$ is necessary for this but not sufficient (uncertainty confined to mean-irrelevant state coordinates, or to higher moments only, leaves the floor at zero); this is the same alignment qualifier used for the sufficiency connection in the Discussion. Term (i) is positive when the model's predictive mean differs from the Bayes predictor. Any one suffices.

## Epistemic Status

*Exact* under the fresh-noise assumption (observation noise $\varepsilon_t$ conditionally independent of history given current state and action). This is the standard assumption in state-space models — noise is a property of the observation channel at the moment of observation. The decomposition is a mathematical identity: a Pythagorean refinement of the bias-variance decomposition, with two orthogonality arguments in place of one. The positivity of $\mathbb{E}[\Vert\delta_t\Vert^2]$ follows from any of the three conditions; all typically hold simultaneously. The positivity of term (ii) specifically carries the alignment qualifier stated in the derivation — residual state uncertainty must move the one-step conditional mean.

## Discussion

**Three floors, two kinds of "irreducible."** The estimation term is reducible by better modeling. The state-uncertainty floor is *irreducible by modeling* — it binds the Bayes-optimal predictor itself — but *movable by acting*: more informative action and observation choices shrink $\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})$, which is precisely the door through which active sensing and causal information yield ( #def-causal-information-yield) enter the mismatch budget. The channel floor is irreducible outright — a property of the sensor, movable only by changing the instrument. The framework's calibration anchor exhibits the middle floor exactly: in #example-kalman, the steady-state *optimal* filter — well-specified by construction — has innovation variance $H P^- H^\top + R \gt R$; the excess $H P^- H^\top$ is the state-uncertainty floor, present at the in-class optimum.

**Reducible vs. irreducible (overfitting).** An agent that tries to eliminate *all* mismatch — including the two floors — will overfit: adjusting its model to explain noise, degrading future predictions. The update gain ( #emp-update-gain) implicitly separates signal from noise by weighting observations in proportion to their informativeness.

**Connection to model sufficiency.** When $S(M_t) \lt 1$ ( #def-model-sufficiency), the model has lost predictive information relative to the full history. Under an alignment assumption (the lost information affects the one-step conditional mean), this implies positive estimation error (term i). Without that alignment assumption, insufficiency still implies positive regret under proper scoring rules but not necessarily positive one-step mean error.

**Mismatch is structurally persistent.** In realistic AAT regimes, mismatch signals persist — they can be reduced but not eliminated when observation noise is non-degenerate. Deterministic, noiseless, perfectly specified systems are limiting edge cases, not the typical adaptive regime.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 7 of the 14 contributing audit dirs reached a digested reflection on this segment (384279, 471203, 526815, 584721, 742613, 773921, 849201) plus the batched 963715 (14–18 batch) and 451729 (batch-04); 193847, 266847, 361742, 472913, 613842, 829314 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **"Things you can learn vs things you just have to tolerate."** The plain-language split that makes the decomposition land: it "takes the abstract concept of aporia and splits it into model error you *can* reduce and irreducible channel noise you can't" (Claude, AUDIT-WORKING-773921). Strong Brief seed.
- **Chasing zero mismatch in a noisy world is overfitting — *apophenia*.** "Driving mismatch to zero in a noisy environment constitutes overfitting, mapping perfectly to apophenia (finding patterns in noise) in human psychology" (Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-471203 — "the model can chase its own predictions to perfect fit on observation noise, which is *worse* than partial fit on the true signal"). A vivid hook the segment's "overfit" Discussion sentence could adopt.

#### Candidate Discussion

- **The agent-vs-modeler perspective gap (a structural identifiability point).** The decomposition is observable to the *modeler* but not to the *agent*: the agent sees only $\delta_t$, not its split into model-error vs channel-noise. So the agent cannot directly answer "is my mismatch from a bad model or a noisy channel?" — the same kind of structural (not statistical) identifiability obstacle as the zero-aporia ambiguity, unresolvable without additional assumptions or active intervention (CIY-style). A candidate Discussion paragraph naming why active testing (Level 2 access) is the agent's only route to estimating the split (Claude, AUDIT-WORKING-584721).
- **GA-1 (fresh noise) is the load-bearing assumption — name its failure mode.** The cross-term vanishes only because $\varepsilon_t$ is conditionally independent of history given current state/action. Under *temporally correlated* noise (a sensor that drifts over hours rather than emitting independent white noise per reading), the cross-term does not vanish and the agent will overfit to the noise with standard gain updates (Claude, AUDIT-WORKING-849201). Candidate: surface the correlated-noise failure mode explicitly so downstream uses of the decomposition inherit the GA-1 caveat.

#### Follow-up items

- **"This is orthogonality (uncorrelated), not independence."** A small piece of mathematical precision worth keeping visible — the cross-term vanishing needs only zero *conditional mean*, not full independence (Claude, AUDIT-WORKING-471203). Already in the body; flagged as worth preserving as a Brief-able precision.
- **GA-1 / `def-action-transition` declared-dependency hygiene.** GA-1 is invoked but is a global assumption (not a segment), and the Formal Expression uses $a_{t-1}$ while `def-action-transition` is not in `depends:` — both noted as deps-discipline items folded into the root-cause F-A series (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721). Certified-track; surfaced here only because it recurred.

#### Readers often ask / wonder

- "Why does $S(M_t) \lt 1$ not *automatically* imply positive squared-mismatch?" Because if the lost predictive information pertained only to the *variance* (not the *mean*) of the observation, $\Vert\delta_t\Vert^2$ wouldn't increase even though the model is objectively worse — squared mismatch is "blind" to certain information loss. This is exactly what the segment's alignment assumption names, and it may be the deeper motivation for the score-function mismatch $\tilde\delta$ which cares about the whole distribution (Claude, AUDIT-WORKING-773921). A reader reaching the alignment caveat will want this worked out.

#### Candidate figures

- **A Pythagorean / vector-decomposition diagram** (not a pipeline): prediction $\hat o$ and true conditional mean $\bar o$ form the reducible leg; $\bar o$ to observation $o$ forms the irreducible-noise leg; their expected cross-term is zero under GA-1 (orthogonality marker). The visual should make "chasing leg two" (fitting the noise) look like the wrong move (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- The "noise floor on persistence" reach — an ultimate-bound idea $R^\ast \gtrsim \sqrt{\mathbb{E}[\mathrm{Var}(o \mid \Omega, a)]}/\alpha$ separating the agent's controllable share from the irreducible — pertains to the persistence-condition segments, not here; noted as a downstream use of the decomposition (Claude, AUDIT-WORKING-584721).
