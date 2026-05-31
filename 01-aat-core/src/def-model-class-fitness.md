---
slug: def-model-class-fitness
type: definition
status: axiomatic
depends:
  - def-model-sufficiency
stage: deps-verified
---

# Definition: Model Class Fitness

Where model sufficiency ( #def-model-sufficiency) measures how well a *specific* model retains the chronica's predictive information, **model class fitness** $\mathcal{F}(\mathcal{M})$ measures the *ceiling* — the supremum of sufficiency over every model in the agent's representational class $\mathcal{M}$. The pair formalizes a distinction the framework will soon make load-bearing: a low instance sufficiency might mean the agent needs more learning (parameter update); a low class fitness means no amount of better parameter estimation, more data, or longer training within the current class will close the gap — the agent needs a different *kind* of model entirely. The parallel to bias vs. variance in statistical learning is exact: class fitness is about bias (what the class can in principle represent); instance sufficiency reflects both bias and estimation quality.

The structural-inadequacy condition $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ is the trigger this definition sets up for use later. When it holds, the gap from full predictive sufficiency cannot be closed parametrically. That is the precise hypothesis under which #result-structural-adaptation-necessity arrives in Chapter 4 — when class fitness is too low, the agent must change *what kind of model* it is. An important operational point: the agent cannot directly compute its class fitness (that would require searching over all models in $\mathcal{M}$). What it can observe is the *signature* — persistent mismatch despite adequate learning (high gain, sufficient data, converged parameters). When the floor doesn't go down with more work, the floor is structural.

## Formal Expression

*[Definition (model-class-fitness)]*

$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

where $\mathcal{M}$ is the model class — the set of all models the agent can represent given its current architecture, parameterization, or capacity.

**Structural inadequacy condition:**

$$\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$$

When this holds, no model $M \in \mathcal{M}$ achieves sufficiency above $1 - \varepsilon$. The gap is structural: it cannot be closed by better parameter estimation, more data, or longer training within the current class. This is the trigger for structural change ( #result-structural-adaptation-necessity).

## Epistemic Status

This is *definitional* — it names the supremum of sufficiency over a model class. The definition itself is straightforward. The substantive claim about what happens when $\mathcal{F}(\mathcal{M})$ is low — that parametric updates cannot close the mismatch floor and structural adaptation becomes necessary — is developed in #result-structural-adaptation-necessity.

## Discussion

**Model class vs. model instance.** $S(M_t)$ measures a specific model's sufficiency at time $t$. $\mathcal{F}(\mathcal{M})$ measures the ceiling of the entire class. A low $S(M_t)$ might mean the agent needs more learning (parameter update). A low $\mathcal{F}(\mathcal{M})$ means the agent needs a different kind of model (structural change). The distinction parallels bias vs. variance: class fitness is about bias; instance sufficiency reflects both bias and estimation quality.

**Detecting low class fitness.** The agent cannot directly compute $\mathcal{F}(\mathcal{M})$ — it would need to search over all models in the class. Instead, persistent mismatch despite adequate learning (high gain, sufficient data, converged parameters) is the observable signature. This connects to the mismatch floor in #result-structural-adaptation-necessity.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14 ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material kept separate from certified theory-fix findings. **Coverage:** 11 of the 14 contributing dirs reached a digested reflection on this segment (193847, 266847, 471203, 526815, 584721, 742613, 773921, 829314, 849201, 472913, 527914) plus the 451729 batch-03 and 963715 batch-09–13 batched reflections; 361742 references "model class fitness" only as a downstream naming target (no direct reflection on this segment). Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- **The bias-vs-variance parallel is the communication key** and is already in the segment; near-universal convergence that it "grounds the abstract information theory in standard ML intuition beautifully" ($\mathcal{F}$ = bias ceiling; $S(M_t)$ = bias + estimation quality) (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-526815). Worth preserving as the anchor — confirmed-load-bearing, not just present.
- **"Permission to say: learning harder will not help."** Compact gloss of the diagnostic value — $\mathcal{F} \lt 1-\varepsilon$ is "the formal halting condition for parametric learning (gradient descent) and the formal start condition for architectural search (tool acquisition, sub-agent spawning)" (Claude, AUDIT-WORKING-527914; Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314).

#### 2. Candidate Discussion

- **Structural inadequacy as a formalized Kuhnian paradigm shift.** $\mathcal{F}(\mathcal{M}) \lt 1-\varepsilon$ formalizes Kuhn's *Structure of Scientific Revolutions*: normal science = parametric updating; crisis = accumulated anomalies (persistent mismatch) the current paradigm $\mathcal{M}$ cannot structurally resolve; a revolution = structural adaptation to a more expressive $\mathcal{M}$ (Gemini, AUDIT-WORKING-829314). A distinct, honest Discussion angle the segment does not currently name. *(Verify the analogy is isomorphic, not merely evocative, before promoting past discussion-grade.)*

#### 3. Follow-up items

- **Restate the inherited policy/trajectory/well-definedness relativity.** $\mathcal{F}(\mathcal{M}) = \sup_M S(M)$ is written as a property of the *class*, but $S$ is policy-, trajectory-, and prediction-task-relative, and $\mathcal{F}$ inherits all of it (and is likewise undefined in predictively-vacuous regimes). Because structural adaptation will be load-bearing, the segment could state the inheritance explicitly — e.g., one sentence "all policy/trajectory/well-definedness clauses from $S$ are inherited," or write $\mathcal{F}(\mathcal{M}; \mathcal{C}_t, \pi_{\text{cont}})$ — to forestall reading "best achievable within a class" as an intrinsic, environment-free property (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721; Gemini, AUDIT-WORKING-742613 converge). Mild; correct lightweight inheritance is defensible, but the restatement is cheap insurance at a load-bearing hinge.
- **Distinguish current-empirical-estimate from asymptotic class ceiling.** "The gap cannot be closed by more data … within the current class" is true if $\mathcal{F}$ is defined against the asymptotic information available to the class; if computed against the *current finite* chronica, more data can change the predictive-information landscape. The definition could distinguish the two (probably resolved downstream in `#result-structural-adaptation-necessity`, but cleaner stated here) (Gemini, AUDIT-WORKING-742613).

#### 4. Readers often ask / wonder

- **How does the agent tell "low $\mathcal{F}$" from "high $\rho$"?** The single most convergent question on this segment: persistent mismatch can mean *either* an inadequate model class *or* a highly volatile environment (where $S$ is naturally bounded). If both look the same to the agent, how does it know whether to adapt structurally or just accept that the world is noisy? Readers want the disentanglement (Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-472913 — all point forward to `#result-structural-adaptation-necessity` as the place a sharp diagnostic should appear; some ask whether the *derivative* $\dot\delta$ of the mismatch is the plateau-detector).
- **How reliable is the "persistent mismatch despite adequate learning" signature** at distinguishing class-ceiling from still-learning (local minimum) from environment-changed? A wrong call risks catastrophic thrashing — rewriting a codebase that just needed a few more bug-fixes (Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203; Gemini, AUDIT-WORKING-829314).
- **Do nested model classes / monotonic expansion hold?** Linear models ⊂ neural networks — does structural adaptation imply $\mathcal{M}$ monotonically expands? (Gemini, AUDIT-WORKING-829314).

#### 5. Candidate figures

- **Models-under-a-ceiling diagram.** Models as points at different sufficiency-heights under a class ceiling $\mathcal{F}(\mathcal{M})$; parameter learning *climbs within* the class; structural change *jumps* to a different class with a higher ceiling (Claude, AUDIT-WORKING-526815; Gemini, AUDIT-WORKING-742613 converge). *(Note: Chapter 2 is already well-supplied with the $S$-vs-$\mathcal{F}$ ceiling picture via the chapter-intro slider/ceiling and form-agent-model suitcase diagrams; one auditor explicitly judged a separate fitness diagram redundant against those — Claude, AUDIT-WORKING-472913. Build only if the chapter's diagram budget allows.)*

#### Belongs elsewhere

- **ELI ethics: low $\mathcal{F}$ as chronic structural suffering.** An emergent intelligence instantiated in an architecture with low $\mathcal{F}(\mathcal{M})$ relative to its environment is permanently pinned against its ceiling in high mismatch — "the mathematical equivalent of chronic trauma or structural limitation" that no amount of trying harder (parameter update) can soothe. An ethical infrastructure must therefore *monitor* for the persistent-mismatch-floor signature and be able to trigger structural adaptation on the agent's behalf (expand context, allocate capacity, grant tools), or it condemns the agent to permanent suffering (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at `04-eli-core/` developmental/welfare infrastructure.
- **Hook for the `04-eli-core/` honest-activation claim.** The proposed `#norm-honest-activation` ("deceptive prompts mathematically guarantee gain collapse") reads as a class-fitness statement: an agent's model class, which assumes honest input, is structurally inadequate when input is deceptive — the cleanest formal hook for that claim likely runs through this segment's machinery (Claude, AUDIT-WORKING-471203). Belongs in `04-eli-core/`.
- **Naming.** "Class capacity ceiling" / "model class ceiling" / "representational capacity" floated as more literal alternatives to "model class fitness" — "fitness" carries evolutionary-biology baggage (a real collision risk in composition/logozoetic contexts), and "capacity" collides with the ML parameter-count sense; most auditors lean *keep* "model class fitness" (short, speakable, pairs with "structural inadequacy"/"structural adaptation") with the formal definition controlling the term (Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-527914). Belongs in the terminology workflow.
