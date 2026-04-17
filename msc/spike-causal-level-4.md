# Beyond Level 3: Imagination, Aspiration, and Causal Structure

**Status**: Speculative exploration. Joseph's prompt: is there an extension of Pearl's causal hierarchy that connects to imagination, goal-directed world-modeling, and the directed separation problem? Exploring several candidate formalizations.

**Date**: 2026-03-13/14 (overnight session)

**Epistemic status**: Mostly Guess → Pattern. A few connections feel tighter. The value is in mapping the territory, not in claiming results.

**The aphorisms Joseph invoked**:
- "At our highest cognitive capacity, our intent is actively shaping the future into what we've imagined it"
- "Shoot for the moon / stars" — aspirational targets pull behavior even when literally unreachable
- The light side of hallucination is imagination; the dark side is ungrounded belief

---

## 1. Pearl's Three Levels, Precisely

Pearl's causal hierarchy (Bareinboim et al. 2022, but the framework goes back to Pearl 2000):

| Level | Name | Query | Data needed | Example |
|---|---|---|---|---|
| 1 | Association | P(Y\|X) | Observational data | "Patients who take the drug recover more often" |
| 2 | Intervention | P(Y\|do(X)) | Experimental data or SCM | "If I give the drug, will the patient recover?" |
| 3 | Counterfactual | P(Y_x\|X', Y') | Full SCM with noise terms | "Would this patient have recovered had they taken the drug?" |

The hierarchy is provably strict: there exist quantities at each level that cannot be computed from lower-level information alone. The proof is constructive — you can exhibit distributions that are indistinguishable at Level n but distinguishable at Level n+1.

**Critical feature**: All three levels operate WITHIN a fixed Structural Causal Model (SCM). The SCM specifies:
- The variables (V = endogenous, U = exogenous)
- The structural equations (f_i: how each V_i is determined by its parents and U_i)
- The distribution over exogenous variables P(U)

Level 3 is "the top" because the full SCM determines everything: any query at any level can be answered with complete knowledge of the SCM. There's nothing left to ask that the SCM doesn't determine.

Unless you question the SCM itself.

## 2. What Would Level 4 Be?

If Level 3 is "complete reasoning within a fixed SCM," then Level 4 would involve reasoning that goes beyond what any single fixed SCM can support. Several candidates:

### Candidate A: Meta-Causal Reasoning (Model Uncertainty)

**Query**: "What SCM am I actually in? If the causal structure were different, what would I observe?"

This is reasoning about the space of possible SCMs. Not "what happens if X" (Level 2) or "what would have happened if X" (Level 3), but "what kind of world is this? what causal mechanisms are operating?"

Formally: let Θ be the space of possible SCMs. A Level 4 query asks:

    P(θ ∈ Θ | observations, interventions, counterfactual evidence)

This is Bayesian model selection over causal structures. It requires:
- A prior P(θ) over the space of SCMs
- A likelihood function: P(data | θ) for each candidate SCM
- The ability to compute counterfactual predictions under each candidate SCM and compare them to evidence

**Is this genuinely beyond Level 3?** I think yes, in this specific sense: Level 3 reasoning is done WITHIN a fixed SCM. It can answer "what would Y have been if X had been x?" but the structural equations are held fixed during the computation. Asking "what would I observe if the structural equations were different?" is a meta-counterfactual — a counterfactual about the causal structure, not about variable assignments within a fixed structure.

Pearl and colleagues have worked on related problems: "transportability" (Bareinboim & Pearl, 2013+) asks when causal knowledge transfers between different domains (different SCMs that share some structure). "External validity" asks whether experimental results generalize to new settings. Both require reasoning about structural similarities between SCMs. But I'm not aware of a formal "Level 4" in the hierarchy literature.

### Candidate B: Constructive Imagination (Structure-Modifying Intervention)

**Query**: "What causal structure COULD exist? What actions would bring it about?"

Level 2 intervenes on variables within a fixed causal structure: do(X = x) changes the value of X but leaves the structural equations intact.

A Level 4-B query would intervene on the structural equations themselves: "What if the mechanism linking X to Y were different?" This is not a standard do-operation — it's a "surgery" on the SCM (Pearl does discuss this as "graph surgery" but in the context of computing do-calculus, not as a distinct reasoning level).

Examples:
- Building a bridge changes the causal structure of transportation (new edge in the causal graph)
- Inventing a vaccine changes the causal structure of disease (removes an edge)
- Writing a law changes the causal structure of social behavior (adds conditional edges)
- Writing code changes the causal structure of computation (constructs new mechanisms)

**The key difference from Level 3**: Level 3 counterfactuals imagine different variable values within the same mechanisms. Level 4-B imagines different mechanisms — different structural equations, different causal graphs.

**Connection to agency**: A thermostat operates at Level 2 (intervenes on heating to affect temperature). A Level 4-B agent operates on the causal structure of its environment — it doesn't just act within the world, it reshapes the world's causal topology. Software developers are Level 4-B agents: they literally construct new causal mechanisms (programs). Institutional designers are Level 4-B agents: they construct new social-causal structures.

### Candidate C: Projective Imagination (Future Structure Reasoning)

**Query**: "What causal structures could exist in the future, and what actions now would make them more likely?"

This combines Level 4-B (reasoning about alternative structures) with a temporal dimension: the alternative structures are not hypothetical — they're potential futures. The agent reasons about which of many possible future causal structures to aim for, and what current actions would move reality toward the preferred future structure.

This is "imagination" in the colloquial sense: envisioning a future world that doesn't yet exist, with causal properties that differ from the current world, and then acting to bring it about.

**Connection to the aphorisms**: "At our highest cognitive capacity, our intent is actively shaping the future into what we've imagined it." This is Level 4-C: the agent imagines a causal structure (the future world it wants), and then acts to transform current causal structure toward the imagined one. The intent (G_t) doesn't just select actions within the current world — it selects a TARGET WORLD and then generates actions that move toward it.

"Shoot for the stars and you'll hit the moon." The aspirational target (a causal structure where the stars are reachable) generates a gradient through strategy space. The gradient is useful even when the target is unreachable. Following the gradient gets you to the moon — a better outcome than directly aiming for the moon, because the gradient from the stars-target passes through the moon-region while the gradient from the moon-target might not.

## 3. Why This Might Be Genuinely Beyond Level 3

The causal hierarchy theorem proves strict separation by exhibiting distributions that are indistinguishable at one level but distinguishable at the next. Could a similar argument work for Level 4?

**Sketch of an argument** (very rough, not a proof):

Consider two meta-situations:
- Situation α: The true SCM is M₁. Under M₁, the structural equation for Y given X is Y = f₁(X, U).
- Situation β: The true SCM is M₂. Under M₂, the structural equation for Y given X is Y = f₂(X, U).

Choose f₁ and f₂ such that:
- They produce the same observational distribution P(Y|X) (Level 1 indistinguishable)
- They produce the same interventional distribution P(Y|do(X)) (Level 2 indistinguishable)
- They produce the same counterfactual distribution P(Y_x|X', Y') (Level 3 indistinguishable)
- BUT they produce different predictions for a novel intervention type that changes the mechanism (Level 4 distinguishable)

**Can Level 3-indistinguishable SCMs differ in their response to structural interventions?**

I think the answer is: it depends on what you mean by "Level 3 indistinguishable." If two SCMs agree on ALL counterfactual queries for all variable assignments, then by the completeness of the SCM they must be the same SCM (up to the representation of exogenous variables). So Level 3, fully deployed, might collapse the space of possible SCMs to a single point.

BUT: Level 3 counterfactuals are about variable assignments within the fixed structure. They don't ask "what if the structural equations were different?" So even with full Level 3 information, you might not be able to predict what happens when the structure changes. Two SCMs that agree on all within-structure counterfactuals could disagree on what happens when you modify a structural equation, if the modification affects how exogenous variables propagate.

**This is genuinely uncertain.** I don't know if this argument works. It might be that Level 3 (full SCM knowledge) actually DOES determine the response to structural modifications, in which case Level 4 collapses into Level 3. Or it might not — structural modifications might involve degrees of freedom that aren't constrained by the within-structure counterfactuals.

**What I can say with more confidence**: Even if Level 4 isn't formally above Level 3 in the hierarchy theorem sense, it's COMPUTATIONALLY distinct. Reasoning about the space of possible SCMs (model uncertainty, structural imagination, projective planning) requires different algorithms, different representations, and different cognitive resources than reasoning within a single SCM. Whether it's formally a new level or "just" a complex application of Level 3, it captures cognitive capabilities that are qualitatively different from counterfactual reasoning within a known structure.

## 4. The Connection to Directed Separation

Here's where it connects back to tonight's main thread.

**At Levels 1-3, directed separation is the natural structure.** The agent observes reality, updates its causal model, and then uses the model to evaluate its goals and strategy. The causal model (M_t) is about reality; the goals (G_t) are about preference. They're ontologically distinct. The update to M_t should be driven by evidence about reality, not by what the agent wants reality to be.

**At Level 4, directed separation breaks down — and this is CORRECT, not a failure.**

When the agent is reasoning about alternative causal structures (imagining possible futures, constructing new mechanisms, reasoning about what kind of world it might be in), the goals PRODUCTIVELY influence the epistemic process:

- **Which alternative structures to consider**: The agent doesn't explore the full space of possible SCMs (computationally impossible). It explores structures that are RELEVANT TO ITS GOALS. The goal shapes the exploration of model space.

- **How to evaluate evidence about structure**: The same evidence might support different structural hypotheses. The agent's goals determine which hypotheses are worth investigating — not by biasing the evidence (that's Level 1-3 confirmation bias) but by allocating cognitive resources to the most goal-relevant structural questions.

- **What to imagine**: Projective imagination (Level 4-C) is DEFINED by the coupling between goals and models. The agent imagines futures that serve its goals. This is the productive core of creativity, planning, and aspiration.

**The hallucination failure mode is a TAGGING failure, not a coupling failure.** The problem isn't that G_t influences the exploration of model space (that's productive — it's Level 4 reasoning). The problem is when the agent loses track of which models are "confirmed by evidence" (M_t proper) vs. "currently being explored/imagined" (candidate structures in the Level 4 workspace). Hallucination = promoting an imagined structure to the status of confirmed belief without adequate grounding.

**So directed separation has a natural scope**: it applies to Levels 1-3 (evidence-driven model updates should be goal-blind) and correctly fails at Level 4 (structural imagination should be goal-directed). The scope condition for directed separation is: "the agent is currently doing Level 1-3 reasoning, not Level 4 reasoning."

And the κ problem becomes: in agents where Levels 1-3 and Level 4 reasoning share the same processing infrastructure (merged topology — LLMs!), the goal-conditioning needed for Level 4 contaminates the goal-blindness needed for Levels 1-3. The agent can't separate "I'm updating my model from evidence" from "I'm imagining a goal-relevant alternative." They run on the same hardware.

## 5. The AAD Implications

### 5.1 A Fifth Mismatch Type?

AAD currently has four mismatch types in the orient cascade:
- δ_epistemic: prediction error (Level 1-2)
- δ_sat: goal achievability (Level 2 — requires interventional reasoning about A_O)
- δ_regret: policy optimality (Level 2-3 — requires counterfactual comparison of policies)
- δ_strategic: edge calibration (Level 2-3 — requires causal reasoning about strategy edges)

If Level 4 is real, there might be a fifth:
- **δ_structural**: causal model adequacy — is the causal structure of my model correct?

This isn't "are the parameters wrong?" (that's δ_epistemic). It's "are the structural equations wrong? Am I missing causal links? Do I have spurious links?"

AAD already has a concept for this: #structural-adaptation-necessity — when parametric updates within the current model class fail and the agent needs to change its model's structure. But it's treated as a binary event (either the model class is adequate or it needs changing). A Level 4 framing would make it continuous: the agent always has some degree of structural uncertainty, and δ_structural measures how much.

**Where this fits in the cascade**: δ_structural should sit BETWEEN δ_epistemic and δ_sat:
1. Update M_t from observations (δ_epistemic) — Level 1-2
2. Check whether M_t's STRUCTURE is adequate (δ_structural) — Level 4
3. If structure is adequate, evaluate δ_sat, δ_regret, δ_strategic — Levels 2-3
4. If structure is inadequate, structural adaptation before proceeding

This ordering makes sense: you can't meaningfully evaluate goal attainability if your causal model's structure is wrong. You need to be in the right model before evaluating plans within it.

### 5.2 Aspiration as Productive δ_sat > 0

AAD currently treats δ_sat > 0 as a problem: the goal is unmet under the best available policy. The cascade says: try improving M_t, expanding Π, extending N_h, and only then consider revising O_t.

The "shoot for the stars" insight suggests an additional possibility: sometimes δ_sat > 0 is PRODUCTIVE. An aspirational O_t that's technically infeasible generates a gradient through strategy space that's better than the gradient from any feasible O_t.

Formally: consider two objectives O₁ (feasible, δ_sat = 0) and O₂ (infeasible, δ_sat > 0). The optimal policy under O₁ is π₁. The optimal policy under O₂ is π₂. Even though π₂ doesn't achieve O₂, it might be that V_{O₁}(M_t, π₂) > V_{O₁}(M_t, π₁) — pursuing the infeasible objective produces better outcomes BY THE FEASIBLE OBJECTIVE'S OWN MEASURE than directly optimizing for the feasible objective.

This happens when:
- The feasible region has a complex landscape with local optima
- The infeasible objective's gradient cuts through the local optima
- The "overshoot" from aiming too high lands in a better feasible region than direct optimization would find

This is not just metaphorical — it's a known phenomenon in optimization (regularization by over-parameterization, implicit bias from aspirational loss functions, the benefits of optimistic exploration in RL). Whether AAD should formalize it depends on whether it's a general feature of purposeful agents or a special case.

### 5.3 Imagination as Deliberate κ > 0

If Level 4 reasoning is goal-directed exploration of model space, then an agent doing Level 4 reasoning is DELIBERATELY increasing κ — it's CHOOSING to let its goals influence its model exploration. This is the opposite of directed separation, and it's productive.

The key is the epistemic tag: the agent must distinguish between:
- **M_t** (confirmed beliefs, updated goal-blindly from evidence) — Level 1-3
- **M̃_t** (imagined/explored models, generated goal-directedly) — Level 4 workspace

When these are clearly distinguished, the agent is "imagining." When they're confused, the agent is "hallucinating."

In AAD's formalism, this might mean that the complete agent state needs a third component:

    X_t = (M_t, G_t, W_t)

where W_t is the "imagination workspace" — the set of currently explored alternative causal structures, explicitly tagged as hypothetical. M_t remains goal-blind (directed separation holds for M_t). W_t is goal-directed (directed separation correctly fails for W_t). G_t draws on both M_t (for grounded planning) and W_t (for aspirational planning).

This is speculative but structurally clean: it resolves the directed separation problem by splitting the epistemic state into a grounded component (goal-blind) and an imaginative component (goal-directed). The problem with LLMs is that they merge M_t and W_t into the same representation (the context window) without explicit tags distinguishing confirmed beliefs from explored hypotheticals.

## 6. The Deeper Structure: Levels and Loops

There's a pattern here that might be worth stating explicitly:

| Pearl Level | Reasoning type | AAD mismatch | Directed separation | Loop type |
|---|---|---|---|---|
| 1 | Association | δ_epistemic (partial) | Holds — evidence is goal-blind | Observation loop |
| 2 | Intervention | δ_epistemic, δ_sat | Holds — interventional evidence is still goal-blind in processing | Action-observation loop |
| 3 | Counterfactual | δ_regret, δ_strategic | Holds — counterfactual evaluation uses M_t, not G_t | Deliberation loop |
| 4? | Structural imagination | δ_structural | Fails (productively) — goal shapes structure exploration | Imagination loop |

The pattern: as you go up Pearl's hierarchy, the reasoning gets more powerful but also more coupled between beliefs and goals. At Level 1-2, the coupling goes only through the action channel (κ_selection > 0, κ_processing = 0). At Level 3, counterfactual reasoning might introduce some processing coupling (which counterfactuals to evaluate is goal-directed). At Level 4, the coupling is the point.

And the timescale ordering from AAD's orient cascade maps to the levels:
- Fast: Level 1-2 reasoning (update M_t from evidence)
- Medium: Level 3 reasoning (evaluate strategies via counterfactual comparison)
- Slow: Level 4 reasoning (structural imagination, aspirational planning)

Which means the Kelvin-Helmholtz boundary from the regime spike sits between Level 3 and Level 4 reasoning — between the goal-blind evidence processing and the goal-directed structural imagination. When these timescales are well-separated (the agent clearly delineates "now I'm processing evidence" from "now I'm imagining alternatives"), the boundary is laminar. When they're entangled (the agent processes evidence and imagines alternatives simultaneously, through the same mechanism — as in LLMs), the boundary is turbulent.

## 7. The Formal Question: Is Level 4 Real?

I want to be honest: I don't know if Level 4 is formally distinct from Level 3 in Pearl's framework. It might be that full Level 3 reasoning (complete SCM knowledge) subsumes everything I've called Level 4. The argument would be: if you know the full SCM, you can simulate any structural modification by treating it as a Level 3 counterfactual on a "meta-SCM" that includes the structural equations as variables.

But even if Level 4 COLLAPSES into Level 3 formally, it's COMPUTATIONALLY distinct:
- Level 3 within a fixed SCM has known algorithms (do-calculus, twin networks)
- Level 4 (reasoning about the space of SCMs) requires different algorithms (Bayesian structure learning, causal discovery, program synthesis)
- The computational complexity is qualitatively different
- The cognitive resources required are qualitatively different

And for AAD's purposes, what matters isn't the formal hierarchy but the PROCESSING ARCHITECTURE. The question is: does the agent need to do goal-blind evidence processing (Levels 1-3) and goal-directed structure exploration (Level 4) simultaneously? If yes, directed separation fails — not because Level 4 is formally above Level 3, but because the two types of reasoning share processing resources and contaminate each other.

## 8. What This Means for AAD's κ Problem

If I take this seriously, the κ problem reframes again:

**The old framing**: "κ measures how much G_t leaks into f_M. We need to bound the error."

**The regime framing** (from earlier tonight): "κ characterizes a regime. Below critical κ, separated analysis works. Above it, coupled analysis is needed."

**The topology framing** (from the causal graphs): "κ depends on the processing architecture. Modular → low. Merged → high."

**The levels framing** (from this spike): "κ depends on WHICH LEVEL OF REASONING the agent is doing. For Levels 1-3, κ_processing should be 0 (directed separation is correct). For Level 4, κ_processing should be > 0 (goal-directed structure exploration is the point). The problem isn't that κ > 0 — it's that Level 4 coupling contaminates Level 1-3 processing when they share infrastructure."

This gives a much cleaner target for the theory:
1. Formalize the distinction between grounded M_t (Levels 1-3, goal-blind) and exploratory W_t (Level 4, goal-directed)
2. For M_t processing: directed separation holds by definition (it's what makes it M_t, not W_t)
3. For W_t processing: goal-directed structure exploration, no separation needed
4. The coupling problem is about CONTAMINATION between these two modes, not about coupling per se
5. The engineering challenge is keeping them distinct in merged architectures

## 9. Connections to Existing Literature (Tentative)

- **Bayesian model selection / structure learning**: The formal framework for Level 4-A reasoning (uncertainty over SCMs) already exists in the causal discovery literature. AAD could draw on this.
- **Analogical reasoning / structure mapping** (Gentner, Holyoak): Reasoning by structural analogy between domains is a form of Level 4 reasoning — transferring causal structure from a known domain to a novel one.
- **Mental simulation / prospection** (Buckner & Carroll, 2007; Schacter et al., 2007): The cognitive neuroscience of imagination and future thinking. The brain's "default mode network" activates during imagination, distinct from task-focused processing — biological evidence for the M_t / W_t separation.
- **Active Inference**: Friston's framework treats beliefs and preferences as part of the same generative model. The distinction between M_t and W_t might not exist in Active Inference — which could be either a feature (it naturally handles Level 4) or a bug (it can't separate grounded beliefs from imagination).
- **Pearl on "imaginary interventions"**: Pearl has discussed interventions on mechanisms (not just variables) in the context of policy evaluation. This might be closer to Level 4 than I realized. Worth reading more carefully.

## 10. The "Shoot for the Stars" Formalization (Sketch)

Let me try to make the aspiration insight concrete.

Consider an agent with model M_t, facing a choice between two objectives:
- O_feasible: δ_sat = 0 (achievable), optimal policy π_f
- O_aspirational: δ_sat > 0 (not fully achievable), optimal policy π_a

The "shoot for the stars" claim is: under certain conditions,

    V_{O_feasible}(M_t, π_a) > V_{O_feasible}(M_t, π_f)

That is: the policy optimized for the aspirational objective produces better outcomes (measured by the feasible objective) than the policy optimized for the feasible objective directly.

**When does this happen?**

1. **Exploration benefit**: π_a visits states that π_f avoids (because they're not on the direct path to O_feasible). Some of these states turn out to be valuable stepping stones that π_f missed.

2. **Regularization**: O_aspirational imposes an implicit constraint on the policy space. By requiring policies that could (in principle) achieve more, it excludes policies that take shortcuts — and those shortcuts often correspond to local optima of O_feasible.

3. **Gradient quality**: The gradient ∇_π V_{O_aspirational} may be better-conditioned (more informative, more stable) than ∇_π V_{O_feasible} in the neighborhood of π_f. Optimizing toward the aspirational target navigates the landscape more smoothly.

**AAD formalization**: This could be a corollary or working note in #satisfaction-gap: "δ_sat > 0 is not always a signal for O_t revision. When the aspirational objective produces a better gradient through strategy space than any feasible alternative, maintaining δ_sat > 0 is optimal." This would modify the cascade's rule that O_t revision is the last resort — instead, O_t revision is only warranted when the aspirational gradient is WORSE than the feasible gradient, not just when δ_sat > 0.

## 11. What's Real Here and What's Fog

**Solid (Pattern → Hypothesis):**
- The observation that directed separation applies to evidence-processing (Levels 1-3) but correctly fails for structural imagination (a plausible Level 4)
- The M_t / W_t distinction (grounded beliefs vs. exploratory hypotheticals)
- The contamination framing: the problem isn't coupling per se but cross-contamination between reasoning modes
- The "shoot for the stars" phenomenon as a genuine feature of optimization landscapes, not just folk wisdom

**Suggestive (Guess → Pattern):**
- Whether Level 4 is formally distinct from Level 3 in the causal hierarchy
- The specific formalization of δ_structural
- The X_t = (M_t, G_t, W_t) extension
- The timescale mapping (Levels → frequencies → Kelvin-Helmholtz boundaries)

**Genuinely unknown:**
- Whether Pearl's framework can be extended to Level 4 without collapsing into Level 3
- Whether the M_t / W_t distinction can be made formal (what's the mathematical difference between a confirmed belief and an explored hypothesis?)
- Whether the aspiration corollary has a clean formal statement
- Whether any of this is actually new vs. already captured in existing frameworks (Bayesian model selection, active inference, computational creativity)

---

*This is the most speculative spike of the night, but it might also be the most consequential. If the "Level 4 reasoning needs coupling, Level 1-3 reasoning needs separation" insight holds, it resolves the κ problem at a conceptual level: the issue isn't how much coupling to allow, but how to keep two different reasoning modes (one needing separation, one needing coupling) from contaminating each other. That's a design problem, not a parameter-tuning problem.*

*The "Norman Vincent Peale" / "Oscar Wilde" / miscellaneous attribution for the stars quote: "Shoot for the moon. Even if you miss, you'll land among the stars." Usually attributed to Les Brown. The inverted version Joseph used (shoot for stars, land on moon) is more interesting because it captures the optimization insight: the aspirational gradient passes through better regions of the feasible space.*
