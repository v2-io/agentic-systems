---
slug: disc-structural-imagination
type: discussion
status: discussion-grade
depends:
  - def-pearl-causal-hierarchy
  - der-directed-separation
  - result-structural-adaptation-necessity
stage: draft
---

# Discussion: Structural Imagination — Model-Modifying Reasoning and the Scope Boundary of Directed Separation

Pearl's three levels all reason *within* a fixed structural causal model; a class of reasoning AAT's agents demonstrably perform — imagining alternative causal structures, planning actions that *change* the environment's mechanisms, and evaluating aspirational targets — operates *on the space of models* instead. This segment names that task class, states why it is computationally (not hierarchy-theoretically) distinct from Level 3, locates the scope boundary of directed separation exactly at its edge — goal-blind processing is correct for within-model evidence, and goal-*directed* exploration is correct (not a failure) for model-space reasoning — and proposes the tagged-workspace structure $X_t = (M_t, G_t, W_t)$ under which the two modes coexist without contamination. Hallucination is then diagnosed as a *level-confusion* failure: an explored model promoted to $M_t$ without grounding — a mechanism complementary to the quantitative goal-coupling displacement bound of #deriv-observation-ambiguity-bias-bound.

## Formal Expression

*[Formulation (structure-modifying action; sketch)]*

Pearl's SCM machinery already represents mechanism replacement (\citep[§7.2.4]{pearl-2009-causality} "local surgeries"): for $M = \langle U, V, F \rangle$, define $M[f_X := g]$ by replacing one structural equation, with $do(X = x)$ the constant-function special case. An action $a$ is **structure-modifying** with respect to the environment's causal model $M$ when the post-action environment is described by $M' = \sigma(M, a) \neq M$ — the structural equations themselves have changed (a bridge built, a law enacted, a program written), as opposed to standard actions, which set variable values within fixed mechanisms. The corresponding planning query optimizes over model space:

$$a^\ast = \arg\max_a \; \mathbb{E}_{M_{t+1} \sim P(\cdot \mid a, M_t)}\bigl[J(M_{t+1})\bigr],$$

a task with no Level-1–3 analog: the search space is a mechanism space, not a value space, and evaluation marginalizes over the models an action could produce.

*[Discussion — computational, not hierarchy-theoretic, distinctness]*

This is deliberately **not** claimed as a "Level 4" of the causal hierarchy. Given full SCM knowledge, structural counterfactuals $Y_{f_X := g}$ are computable within Level 3, and no strictness witness (Level-3-indistinguishable but structurally-distinguishable pair) has been exhibited — the originating spike's supporting claim that agreement on all standard counterfactuals forces identical structural equations is plausible but was never derived, and nothing here leans on it. What is defensible and is claimed: the task class is *computationally and cognitively* distinct (mechanism-space search, no analog of the do-calculus for identification, inseparability of model identification from inference when actions modify the model), and it is precisely the reasoning mode AAT's structural-adaptation machinery ( #result-structural-adaptation-necessity, #def-model-class-fitness) presupposes an agent can perform.

*[Hypothesis (tagged workspace)]*

The complete agent state extends to $X_t = (M_t, G_t, W_t)$, where $W_t$ is the **imagination workspace**: the set of currently-explored alternative models (candidate structures, aspirational futures, hypothetical mechanism changes), explicitly tagged as ungrounded. Directed separation ( #der-directed-separation) holds for $M_t$ by definition of what $M_t$ is — evidence-processing remains goal-blind — and *correctly fails* for $W_t$: which alternative structures to explore is inherently goal-directed, and that coupling is the productive core of planning, construction, and aspiration rather than a leak to be bounded. Falsification handle: an architecture that maintains the tag (grounded vs explored) should show the bias-bound pathologies of goal coupling only in its $W_t$-to-$M_t$ promotion step, not in its $M_t$ updates.

*[Hypothesis (aspiration; formal statement at #def-satisfaction-gap)]*

Maintaining an infeasible aspirational objective can dominate feasible targets by the feasible objective's own measure — see the aspiration hypothesis landed in #def-satisfaction-gap's Discussion, which modifies the reading of "objective revision is the last resort."

## Epistemic Status

*Discussion-grade throughout; nothing here is derived.* The structure-modifying action formulation is a sketch on Pearl's own machinery (imported: Pearl 2009 §7.2.4; hierarchy strictness Bareinboim et al. 2022 — both already recapitulated in #def-pearl-causal-hierarchy); the planning query is a formulation; the $W_t$ workspace and the level-confusion diagnosis of hallucination are hypotheses with a stated falsification handle; the "no Level 4 in the strict sense" posture is a deliberate scope refusal, not modesty — the strictness question is open and recorded as such. The typing of what $\sigma(M, a)$ acts on interacts directly with the epistemic-target-ontology decision (PROPOSALS SP-30: $S_t = (\Omega_t, \theta)$ gives law-content its own slot, and a structure-modifying action is then an action on world-side $\theta$) — the vocabulary here is stated in current canon terms and should be re-typed when SP-30 is decided. Adjacent external literature (causal abstraction: Beckers & Halpern; Rubenstein et al.; transportability: Bareinboim & Pearl) is flagged for a relata pass before this segment advances past `draft`.

## Discussion

**Where directed separation's scope boundary actually sits.** #der-directed-separation already distinguishes goal-directed event *selection* (legitimate) from goal-blind event *processing* (the invariant). This segment adds a third distinction on the *content* axis: processing that updates the grounded model $M_t$ (goal-blind, Levels 1–3) versus reasoning that explores ungrounded alternatives $W_t$ (goal-directed, structure-modifying). The κ problem for merged architectures then reframes: the issue is not the amount of goal-coupling but **cross-contamination between two modes that individually have correct, opposite coupling disciplines** — an LLM's context window holds grounded belief and explored hypothesis in the same representation with no tag, so Level-4-appropriate coupling bleeds into Level-1–3 processing. Keeping the modes distinct is a design problem, not a parameter-tuning problem.

**Hallucination as level confusion — complementary to the bias bound.** Canon's quantitative hallucination treatment ( #deriv-observation-ambiguity-bias-bound and its NeurIPS Paper 3 sharpening) bounds the displacement of $M_t$ updates under goal coupling — a *drift* mechanism. The level-confusion diagnosis names a different failure: a $W_t$ element (imagined structure, hypothetical world) promoted to $M_t$ status without grounding — a *mis-typing* mechanism. The two are complementary: drift corrupts the grounded model gradually through coupled processing; promotion corrupts it discretely through a missing tag. The light side of the same machinery is imagination — the tag maintained, exploration goal-directed, promotion gated on evidence.

**Relation to structural adaptation.** #result-structural-adaptation-necessity establishes when parametric updates within the current model class must give way to structural change, treating the event discretely. Structural imagination is the *capability* that responding to that event presupposes: generating and evaluating candidate structures is model-space reasoning. A continuous structural-adequacy mismatch ($\delta_{\text{structural}}$, sitting between epistemic update and feasibility evaluation in the orient cascade) was sketched in the originating spike and is deliberately *not* landed here — it needs its own derivation of measurability before it earns a mismatch-family slot.

## Working Notes

- **Provenance.** Landed 2026-07-16 from `spikes/.integrated/spike-causal-level-4.md` + `spike-causal-level-4-formal.md` (2026-03-13/14, Joseph's aphorism-prompted overnight cluster) via the bulk-64 verification queue. The spikes' Approach-1 structural-counterfactual claim (Level-3 agreement forces equation identity) remains underived — do not cite it as established; the strictness question (is there a real Level 4?) remains open.
- **SP-30 interaction (re-type on decision).** If $S_t = (\Omega_t, \theta)$ is adopted, restate: a structure-modifying action is an intervention on world-side $\theta$; $W_t$ explores candidate $\theta$-content; the grounded/explored distinction becomes a typing on the agent's $\theta$-beliefs. If state-only $\Omega$ is kept, the current phrasing stands.
- **Relata pass owed** before promotion: Beckers & Halpern (causal abstraction), Rubenstein et al., Bareinboim & Pearl transportability, and the mental-simulation/prospection literature the spike gestured at — none load-bearing for the discussion-grade claims, all needed for honest Related-Work grounding.
- **$\delta_{\text{structural}}$** (fifth mismatch type) deliberately withheld — see Discussion; a future spike would need to derive what makes structural inadequacy *measurable* as a continuous signal before the cascade gains a slot.
