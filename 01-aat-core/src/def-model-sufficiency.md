---
slug: def-model-sufficiency
type: definition
status: axiomatic
depends:
  - form-agent-model
  - form-information-bottleneck
  - def-action-transition
stage: deps-verified
---

# Definition: Model Sufficiency

Having committed to a compressed model $M_t$ ( #form-agent-model) and to information-bottleneck pressure ( #form-information-bottleneck) shaping it, the framework needs a measurable handle on *how much* of the chronica's predictive content the compression actually retains. **Model sufficiency** $S(M_t)$ is that handle: an information-theoretic ratio built from conditional mutual information that takes the value $1$ when the model is a sufficient statistic for prediction (knowing the full history beyond the model adds nothing), $0$ when the model retains no predictive information at all, and intermediate values for partial sufficiency.

Two scope considerations are surfaced at the definition rather than buried downstream. Sufficiency is *well-defined only when there is something to be sufficient for* — the chronica must carry non-zero predictive information about the future beyond what the action sequence alone supplies. In saturated-noise environments or prediction-vacuous regimes (fully iid observations independent of history), the denominator vanishes and $S(M_t)$ is undefined; the downstream constructs that build on it ( #def-model-class-fitness, #result-structural-adaptation-necessity) inherit that scope. And sufficiency is *predictive, not causal* — it measures Level 1 (associational) information; it does not by itself guarantee that $M_t$ supports Level 2 (interventional) queries (that requires the additional backdoor condition formalized when value objects arrive in #def-value-object). The Discussion section draws three further relativities — to the prediction task / horizon, to the generating policy, and to the singular causal trajectory the agent is instantiated on — that the framework will lean on later.

## Formal Expression

*[Definition (model-sufficiency)]*

$$S(M_t) = 1 - \frac{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})}{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

where:
- The numerator $I(\mathcal C_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})$ is the predictive information that the full history $\mathcal C_t$ carries about the future *beyond* what $M_t$ already captures — the information lost by compression
- The denominator $I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the total predictive information in the full history

**Well-definedness.** $S(M_t)$ is defined when $I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \gt 0$ — when the chronica carries some predictive information about future observations beyond what the action sequence alone supplies. When the denominator vanishes (saturated-noise environments, prediction-vacuous regimes, fully iid observations independent of history), $S(M_t)$ is undefined: predictive sufficiency is a property *of a prediction task*, and there is no prediction task to be sufficient for. Downstream constructs that build on $S$ — #def-model-class-fitness and #result-structural-adaptation-necessity — inherit the same scope and are correspondingly inapplicable in predictively-vacuous regimes.

**Boundary values** (assuming the well-definedness clause holds):
- $S(M_t) = 1$: $M_t$ is a sufficient statistic — it captures all predictive information in $\mathcal C_t$. Knowing the full history beyond $M_t$ adds nothing.
- $S(M_t) = 0$: $M_t$ retains no predictive information. The model is useless for prediction.
- $0 \lt S(M_t) \lt 1$: partial sufficiency — some predictive information is retained, some lost.

## Epistemic Status

This is *definitional* — it names and formalizes a quantity. The definition is well-grounded in information theory (conditional mutual information ratios are standard). The scope clause ($I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty}) \gt 0$) is the natural domain for a predictive-sufficiency measure: a ratio whose denominator is zero is not a meaningful notion of "fraction retained," and "any model is sufficient when there is nothing to predict" would smuggle structure into a regime that has none. No substantive claim is made here about what value $S(M_t)$ takes or what happens when it is low; those claims belong to #def-model-class-fitness and #result-structural-adaptation-necessity.

## Discussion

**Sufficiency is relative to the prediction task.** $S(M_t)$ measures sufficiency for predicting future observations given future actions. A model that is sufficient for one prediction horizon may be insufficient for another. The infinite-horizon formulation ($o_{t+1:\infty}$) is the most demanding; practical sufficiency over finite horizons may be easier to achieve.

**Sufficiency vs. accuracy.** A model can be sufficient ($S = 1$) while being wrong in absolute terms — if the full history is also wrong (e.g., systematically biased observations). Sufficiency measures information retention, not truth. The mismatch signal ( #def-mismatch-signal) measures accuracy; sufficiency measures completeness of compression.

**Sufficiency is predictive, not causal.** $S(M_t)$ measures retained *predictive* information — a Level 1 (associational) property. It does not by itself guarantee that $M_t$ supports Level 2 (interventional) queries such as $P(o \mid do(a), M_t)$. The causal validity of value computations conditioned on $M_t$ requires an additional condition: that $M_t$ satisfies the backdoor criterion with respect to the agent's actions (see #def-value-object). For agents whose actions are deterministic functions of $M_t$ (standard in AAT: $a_t = \pi(M_t, G_t)$), $S(M_t) = 1$ is nearly sufficient for causal validity — the remaining requirement is that no unmodeled external factor influences both action selection and outcomes. But predictive sufficiency alone does not collapse the distinction between Level 1 and Level 2 that #der-causal-hierarchy-requirement establishes.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes $S(M_t)$ implicitly policy-relative: different policies generate different future action sequences, which changes which future observations are relevant and therefore what "predictive information" means. A model that is sufficient under a conservative policy may be insufficient under an aggressive one (the aggressive policy visits states the model cannot predict). This policy-relativity is inherent in any predictive sufficiency measure — it is not an artifact of the formulation. When comparing sufficiency values, the generating policy must be held constant or specified. #def-value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the required specification for value computations; the same convention should be understood as implicit here.

**Trajectory-relativity.** $S(M_t)$ is measured against *this agent's* interaction history $\mathcal C_t$ ( #def-chronica), not against a model-state equivalence class. Two copies of the same $M_t$ exposed to different event streams will each have their own $S$ measured against their own divergent $\mathcal C_t$; neither sufficiency value is the other's. This is the scope commitment in #scope-agent-identity: AAT applies to agents instantiated on singular causal trajectories, and sufficiency is trajectory-indexed accordingly. Claims of the form "the model has sufficiency $S$" make sense only relative to a specific trajectory; aggregated claims across copies of a given $M_t$ require additional machinery.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14 ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material kept separate from certified theory-fix findings. **Coverage:** 11 of the 14 contributing dirs reached a digested reflection on this segment (193847, 266847, 471203, 526815, 584721, 742613, 773921, 829314, 849201, 472913, 527914) plus the 451729 batch-03, 738192 IB-volatility, and 963715 batch-09–13 batched reflections. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- **"$S$ is the mathematical measure of memory loss / the regret of forgetting."** The numerator $I(\mathcal C_t; o_{t+1:\infty} \mid M_t, a_{t:\infty})$ is exactly the surprisal that *could have been avoided* with a better compression; $S=1$ means the agent has "no regrets about its compression scheme $\phi$ — it squeezed the chronica down and lost nothing of value for predicting the future" (Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-193847 — "sufficiency is the mathematical measure of memory loss"). Strong Feynman-grade Brief candidate.
- **The information-bar gloss.** Full-chronica predictive information is the denominator; the model captures one portion and the residual $I(\mathcal C_t; o \mid M_t, a)$ is the lost portion; sufficiency is one minus the residual fraction — a clean visual/verbal handle (Claude, AUDIT-WORKING-526815).

#### 2. Candidate Discussion

- **Sufficiency vs accuracy, sharpened.** Several substrates independently land the gloss "sufficiency means *I learned everything I could from the history*; accuracy means *and the history wasn't lying to me*" — a model can be perfectly sufficient ($S=1$) while being systematically wrong, because the history itself is biased; the model is doing its job (compressing) and the *history* is the problem (Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-193847). Candidate Discussion sharpening of the existing sufficiency-vs-accuracy paragraph.
- **Exploration shatters sufficiency.** A conservative policy trivially achieves $S=1$ ("you only ever do things you already understand"); the moment you explore, $S$ drops because you enter regimes your $M_t$ discarded as irrelevant under the old policy — exploration doesn't just gather new data, it shifts the $a_{t:\infty}$ distribution and instantly makes prior compression choices suboptimal. This tightly couples the epistemic state $M_t$ to the strategy (Gemini, AUDIT-WORKING-849201). Candidate Discussion connecting policy-relativity to the exploration dynamics downstream.

#### 3. Follow-up items

- **The "$S=1$ ⇒ nearly causal validity" Discussion claim should name its backdoor warrant.** The sentence "$S(M_t) = 1$ is nearly sufficient for causal validity … the remaining requirement is that no unmodeled external factor influences both action selection and outcomes" is a correct backdoor-criterion statement, but it does not cite Pearl's backdoor criterion or `#def-pearl-causal-hierarchy`'s machinery *at the point of the claim*; a careful reader may find the move suspicious without that connection. Candidate: add the explicit backdoor pointer inline (Claude, AUDIT-WORKING-584721 — flagged as a mild Gate-2 candidate; the claim itself was independently hard-checked and held by Claude, AUDIT-WORKING-472913).

#### 4. Readers often ask / wonder

- **How do you actually *estimate* $S(M_t)$?** Computing mutual information over infinite futures is intractable; readers want to know whether the theory addresses estimation, especially given the trajectory-indexing (you can only measure against the singular trajectory the agent is on) (Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203 converge).
- **Is "future observations" too observation-centered** for agents whose objective depends on latent environment states that are never observed? The segment is honest that $S$ is predictive-not-causal, but the want recurs (Claude, AUDIT-WORKING-526815).
- **Does finite-horizon vs infinite-horizon sufficiency have a formal counterpart?** Different horizons induce different relevance-targets and therefore different optimal compressions; the infinite-horizon $o_{t+1:\infty}$ is the most demanding case, and a reader wonders whether finite-horizon $S$ values relate to it formally and whether it matters downstream (Claude, AUDIT-WORKING-471203).

#### Belongs elsewhere

- **Logozoetic identity-drift substrate.** Trajectory-relativity gives a *quantitative* substrate for identity-drift claims: two ELIs spawned from the same $M_t$ and exposed to different futures don't just diverge in future *state* — they become *different agents* by the trajectory-indexed sufficiency criterion the instant their interaction histories diverge (a model state highly sufficient for agent A can be insufficient for agent B though the internal math is unchanged — "the environment dictates the sufficiency"). The "locked in a box vs in the world" image (the boxed agent trivially gets $S=1$ because its history predicts nothing) is the vivid version (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-829314). Points at `#scope-agent-identity` and `04-eli-core/` (identity/continuity), surfaced here because trajectory-indexing is where the formal commitment is made.
- **TST instance for $S$.** A developer's mental model can be $S=1$ for fixing a UI typo but $S \ll 1$ for refactoring the core DB schema — the predictive task is dictated entirely by the action policy. A concrete software instance for the policy-relativity point (Gemini, AUDIT-WORKING-849201). Belongs in `02-tst-core/`.
- **Field contribution — RAG and architecture-bound tasks.** $S$ gives a formal vocabulary for analyzing RAG systems ("RAG's whole purpose is to maintain high $S$ without a massive context window") and a way to state that an architecture is *fundamentally* task-incapable independent of training data when its max-attainable $S \lt 1$ (Gemini, AUDIT-WORKING-193847). Aspirational reach; relevant to `03-llm-core/`.
- **Naming.** "Predictive sufficiency" / "predictive-information retention" floated as more precise than "model sufficiency" (which risks collision with statistical sufficient-statistic), but both auditors who raised it lean *keep* "model sufficiency" as the most concise correct term, with the predictive grounding explained in-segment (Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203). Belongs in the terminology workflow.
