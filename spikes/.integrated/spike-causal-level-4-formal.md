# Toward a Formal Level 4: Two Sketch Approaches

**Status**: Formal exploration. Attempting to extend Pearl's causal hierarchy using his own machinery. Two approaches attempted. Honest about where each succeeds and fails.

**Date**: 2026-03-14 (overnight session, late)

**Prerequisites**: Pearl (2009) Chapter 1 (SCM definitions), Chapter 7 (counterfactual semantics, Theorem 7.1.7), Section 7.2.4 (mechanisms and surgeries).

---

## Background: What Level 3 Gives You

An SCM is M = ⟨U, V, F⟩ where:
- U = exogenous (background) variables
- V = endogenous variables
- F = {f_i} structural equations: v_i = f_i(pa_i, u_i)

Pearl's three levels, stated precisely:

**Level 1** — P(Y | X): Computable from the joint distribution P(v) alone. No causal model needed.

**Level 2** — P(Y | do(X = x)): Requires the causal graph G(M) at minimum. Computable from the "truncated factorization" (delete f_X, set X = x, propagate). The do-operator replaces a mechanism with a constant.

**Level 3** — P(Y_x = y | X = x', Y = y'): Requires the full SCM ⟨M, P(u)⟩. Evaluated via Theorem 7.1.7's three steps:
1. *Abduction*: Update P(u) to P(u | evidence)
2. *Action*: Form submodel M_x (replace f_X with X = x)
3. *Prediction*: Compute P(Y) in ⟨M_x, P(u | evidence)⟩

The hierarchy is strict: Bareinboim et al. (2022) prove there exist distributions at each level that cannot be computed from lower-level information.

**Key observation**: All three levels operate on a FIXED SCM M. The structural equations {f_i} are invariant. Level 2 replaces one equation with a constant (intervention). Level 3 reasons about alternative variable values under the same mechanisms. But neither Level 2 nor Level 3 asks: "what if a mechanism were different?"

## The Gap: Mechanism Change

Pearl discusses in §7.2.4 that actions are "local surgeries" — modifications to specific mechanisms. The standard do-operator is the simplest surgery: replace f_X with a constant. But Pearl also notes that "every causal model advertises not one but rather a host of submodels, each created by violating some laws."

The SCM framework CAN represent mechanism changes. Given M with equations F = {f_1, ..., f_n}, define:

    M[f_i := g] = ⟨U, V, F'⟩ where F' = {f_1, ..., f_{i-1}, g, f_{i+1}, ..., f_n}

This is well-defined. You can evaluate any query in M[f_i := g] using the same machinery. Pearl's do(X = x) is the special case where g is the constant function g(·) = x.

**But**: Pearl's calculus (do-calculus, identification rules, d-separation) is developed for the constant-surgery case. There is no "mechanism-calculus" analogous to do-calculus for arbitrary mechanism changes. And more importantly: there is no systematic treatment of REASONING ABOUT THE SPACE OF POSSIBLE MECHANISM CHANGES.

This is the gap where Level 4 might live.

## Approach 1: The Structural Intervention Operator

### Definition (Structural Intervention)

Given SCM M = ⟨U, V, F⟩, define the **structural do-operator**:

    do_s(f_X := g)

This replaces the structural equation for X from f_X(pa_X, u_X) to g(pa_X, u_X), leaving all other equations and the distribution P(U) unchanged.

The standard do-operator is a special case: do(X = x) = do_s(f_X := λ(·).x).

### Structural Counterfactual

By analogy with the standard counterfactual Y_x (the value of Y in submodel M_x), define:

    Y_{f_X := g}(u) = Y evaluated in M[f_X := g] at background U = u

This is "what would Y be if the mechanism producing X had been g instead of f_X?"

The three-step evaluation (Theorem 7.1.7) extends naturally:
1. *Abduction*: Update P(u | evidence) using the ORIGINAL model M
2. *Structural Action*: Form M[f_X := g]
3. *Prediction*: Compute P(Y) in ⟨M[f_X := g], P(u | evidence)⟩

### What's New Here?

The standard counterfactual Y_x asks: "what if X had been x (same mechanism, different input)?"

The structural counterfactual Y_{f_X := g} asks: "what if the mechanism producing X had been different (different mechanism, same background)?"

These are distinct questions. Consider a simple example:

**Model**: Y = f_X(X) + U_Y where f_X is a known function and X is observed.

- Standard counterfactual: "What would Y be if X had been 3?" → Y_{X=3} = f_X(3) + U_Y
- Structural counterfactual: "What would Y be if f_X had been g instead?" → Y_{f_X := g} = g(X) + U_Y

The standard counterfactual changes the input to the mechanism. The structural counterfactual changes the mechanism itself.

### Is This Genuinely Beyond Level 3?

**Honest assessment**: In principle, no. If you know the full SCM ⟨M, P(u)⟩, you can compute Y_{f_X := g}(u) for any u by simply plugging in. The structural counterfactual is *computable* from Level 3 information.

**But computability ≠ representability in the hierarchy**. The hierarchy distinguishes levels by what DISTRIBUTIONS can be recovered from what information. The question is: can you construct two scenarios that are Level 3-indistinguishable (same counterfactual distributions for all variable-value counterfactuals) but distinguishable via structural counterfactuals?

**Claim**: No, you cannot. If two SCMs agree on all standard counterfactuals Y_x(u) for all variables X, Y, settings x, and background values u, then their structural equations must be identical (the counterfactuals uniquely determine the equations). Therefore, they would also agree on structural counterfactuals.

**Conclusion**: The structural intervention operator is a useful EXTENSION of the do-calculus but does NOT define a new level in the strict hierarchy sense. It's a richer class of queries within Level 3.

### But the Practical Distinction Remains

Even though structural counterfactuals don't create a new hierarchy level in the mathematical sense, they are COMPUTATIONALLY and COGNITIVELY distinct:

1. Standard counterfactuals require knowing the mechanism f_X. Structural counterfactuals require knowing the SPACE of possible mechanisms and being able to evaluate the model under each alternative.

2. Standard interventions (do(X = x)) have a clean calculus (do-calculus, identification rules). Structural interventions (do_s(f_X := g)) do not yet have an analogous calculus for identification from data.

3. The PLANNING problem is qualitatively different: "what value should I set X to?" (Level 2 planning) vs. "what mechanism should I install for X?" (structural planning). The latter requires optimization over a function space, not a value space.

## Approach 2: The Model Uncertainty Layer

### The Setup

Instead of extending the do-operator, consider reasoning over a SPACE of SCMs.

Let Θ = {M_θ : θ ∈ Θ} be a parameterized family of SCMs sharing the same variable set V but with different structural equations F_θ = {f_{i,θ}}.

An agent has:
- A prior P(θ) over models
- Evidence e from observations and interventions
- The task of making decisions that depend on which model is correct

### Level 4 Queries

**Model Selection Query**: P(θ | e) — which model am I in?

This is Bayesian model selection. It requires:
- Computing the likelihood P(e | θ) for each candidate model
- Updating the prior: P(θ | e) ∝ P(e | θ) P(θ)

**Structural Prediction Query**: P(Y | do(X = x), e) when the model is uncertain:

    P(Y | do(X = x), e) = Σ_θ P(Y | do(X = x), θ) P(θ | e)

This marginalizes over model uncertainty. Level 2 gives P(Y | do(X = x)) within a fixed model. Level 4 gives P(Y | do(X = x)) across model uncertainty.

**Design Query**: "What mechanism g should I install for X to maximize E[Y]?"

    g* = argmax_g Σ_θ E[Y | do_s(f_X := g), θ] P(θ | e)

This optimizes over mechanism choices while accounting for model uncertainty. There is no Level 1-3 analog of this query because Levels 1-3 don't consider mechanism choice.

### Is THIS Genuinely Beyond Level 3?

**A stronger case than Approach 1.** Here's why:

Level 3 operates within a single SCM. The agent knows M and reasons about counterfactuals within it. But the MODEL SELECTION query — "which M am I in?" — is a question ABOUT models, not WITHIN a model.

Pearl explicitly separates causal DISCOVERY (Chapter 2 — learning the model) from causal INFERENCE (Chapters 3-10 — reasoning within the model). Causal discovery uses different algorithms (constraint-based, score-based) operating on different information (conditional independence patterns in data). It's not part of the Level 1-3 hierarchy — it's a prerequisite.

**Level 4 might be: the unification of causal discovery and causal inference under a single reasoning framework.** Specifically: reasoning that must SIMULTANEOUSLY identify the model (which mechanisms are operative?) and make decisions within it (what interventions to perform?), in a setting where actions can change which model applies.

### The Separability Argument

Levels 1-3 are separable from model identification: you first identify the model (Level 0?), then reason within it (Levels 1-3).

Level 4 is NOT separable when the agent's actions can change the model. If my actions can change the causal structure of the environment (build a bridge → new causal pathways; write a law → new causal constraints; develop a technology → new mechanisms), then:

1. My current model M_t describes the current causal structure
2. My action a_t changes the structure: the post-action environment is described by M_{t+1} ≠ M_t
3. To evaluate action a_t, I need to predict M_{t+1}(a_t) — what structure will result from my action
4. This requires reasoning about the SPACE of possible models, not just about variables within the current model

This is a genuinely new computational task that Level 3 doesn't address: **planning over model space, where actions modify the model itself.**

### Formal Definition (Sketch)

**Definition (Model-Modifying Action)**

An action a is *model-modifying* with respect to SCM M if the post-action environment is described by M' = σ(M, a) where σ is a model transition function and M' ≠ M (the structural equations have changed).

Standard actions: do(X = x) keeps M fixed (modifies variable values, not structure).
Model-modifying actions: σ(M, a) produces a new M' with different {f_i}.

**Definition (Level 4 Planning Query)**

Given current model M_t, model transition function σ, prior P(M_{t+1} | a, M_t), and objective functional J:

    a* = argmax_a E_{M_{t+1} ~ P(·|a,M_t)} [J(M_{t+1})]

This optimizes over actions that change the model, not just variable values within the model.

**Why this requires new machinery**: Level 2 planning optimizes over do(X = x) within a fixed model. Level 4 planning optimizes over model-modifying actions. The search space is qualitatively different (function spaces vs. value spaces), and the evaluation requires marginalizing over possible resulting models.

## Connection to the Directed Separation Problem

### Where Each Level Lives in AAD

| Pearl Level | AAD reasoning | Directed separation | Example |
|---|---|---|---|
| 1 (Association) | P(Y\|X) — correlational model update | Holds trivially | Kalman filter observation |
| 2 (Intervention) | P(Y\|do(X)) — action-value estimation, Q_O | Holds — evidence processing is goal-blind | Evaluating action consequences |
| 3 (Counterfactual) | P(Y_x\|x',y') — regret, strategy calibration | Holds — counterfactual evaluation uses M_t | "Would this strategy have worked?" |
| 4 (Structural) | P(M_{t+1}\|a, M_t) — model-modifying planning | **Fails productively** — goals guide model exploration | "What causal structure should I create?" |

### The Directed Separation Connection

At Levels 1-3, the epistemic update f_M processes observations within a fixed causal model. Goals (G_t) don't need to influence this processing because the model M_t is about reality as it is — the structural equations describe the current world.

At Level 4, the agent reasons about ALTERNATIVE causal structures. Which alternatives to consider is inherently goal-directed — you explore models that are relevant to your objectives. This is productive coupling between G_t and the model exploration process.

**The key reframing**: Directed separation applies to reasoning WITHIN a fixed model (Levels 1-3). It correctly fails for reasoning ABOUT models (Level 4). The problem with merged architectures (LLMs) is that both types of reasoning share the same processing infrastructure, so the goal-directed model exploration (Level 4, productive coupling) contaminates the goal-blind evidence processing (Levels 1-3, needs separation).

### Hallucination as Level Confusion

A hallucination is the agent confusing Level 4 output (an explored/imagined model) with Level 1-3 output (a confirmed belief about reality). The explored model gets promoted to M_t without adequate grounding.

In the SCM framework: the agent considers M' = σ(M_t, hypothetical_action) — "what if the world worked this way?" — and then treats M' as if it were M_t. The model-modifying action was hypothetical (it was imagined, not performed), but the resulting model is treated as if it describes reality.

The fix: maintain a clear distinction between:
- M_t: the current best model of reality (updated via Levels 1-3, goal-blind)
- W_t: the set of explored/imagined alternative models (generated via Level 4, goal-directed)
- The epistemic tags that distinguish them

### "Shoot for the Stars" as Level 4 Planning

The aspiration insight formalized:

Let M_t be the current model (reality as it is). Let M* be an aspirational model (reality as we want it to be). M* may be infeasible — there may be no sequence of actions that transforms M_t into M*.

But the GRADIENT from M_t toward M* — the sequence of model-modifying actions that move the causal structure of reality toward M* — passes through intermediate models that ARE achievable and that may be BETTER than what you'd achieve by planning within M_t alone.

    path(M_t → M*) passes through M_moon
    direct_plan(M_t → M_moon) may be suboptimal
    gradient(M_t → M*) restricted to feasible models may reach M_moon from a better direction

This is the formal content of "shoot for the stars, land on the moon": the aspirational model M* generates a better trajectory through model space than any directly-feasible target model.

## How Strong Is This?

### What I think works (Hypothesis level):

1. **The model-modifying action definition** is clean and fills a real gap. Pearl's do-operator doesn't handle actions that change the structural equations themselves.

2. **The inseparability argument** is the strongest formal claim: when actions can modify models, you cannot separate model identification from inference. This IS a genuinely new computational task.

3. **The directed separation connection** is structurally sound: Level 4 reasoning productively couples goals and model exploration, and the problem with merged architectures is cross-contamination between Level 4 (needs coupling) and Levels 1-3 (need separation).

### What I'm unsure about (Guess → Pattern level):

1. **Whether this constitutes a "Level 4" in the strict hierarchy sense.** Bareinboim et al.'s strictness proof works by exhibiting distributions indistinguishable at one level but distinguishable at the next. I haven't exhibited such a pair for Level 3 vs. Level 4. The reason: with full SCM knowledge, Level 3 determines the model uniquely, so there's nothing to distinguish. The Level 4 distinction might be COMPUTATIONAL (requiring different algorithms) rather than INFORMATIONAL (requiring different data).

2. **Whether Pearl would agree this is beyond his framework.** He discusses mechanism changes, model modification, and "local surgeries." He might argue this is already within the SCM framework — just an application of counterfactual reasoning to the choice of mechanisms. The distinction might be one of emphasis and scope, not fundamental.

3. **Whether the model-modifying action concept is well-defined enough.** What determines σ(M, a)? If the agent knows how its actions change the causal structure, that knowledge is itself a higher-level causal model. There might be an infinite regress.

### What's genuinely unknown:

1. Whether a clean strictness result is possible (Level 3-indistinguishable but Level 4-distinguishable scenarios).
2. Whether the "design query" (optimize over mechanism space) has tractable algorithms or is inherently harder than standard causal inference.
3. Whether the model transition function σ can be formalized without circularity.
4. How any of this relates to the active literature on causal abstraction (Beckers & Halpern, Rubenstein et al.) which deals with relationships between models at different levels of description.

---

## Summary

**Two approaches to Level 4:**

| | Approach 1: Structural Intervention | Approach 2: Model Uncertainty Layer |
|---|---|---|
| Core idea | Extend do-operator to mechanism changes | Reason over space of SCMs |
| Formally new? | No — computable within Level 3 given full SCM | Probably yes — inseparability of discovery and inference when actions modify models |
| Practically distinct? | Yes — different computational problem | Yes — qualitatively different planning task |
| Connection to directed separation | Indirect | Direct — Level 4 is where coupling becomes productive |
| Connection to "imagination" | Structural counterfactuals as imagining alternative mechanisms | Model exploration as imagination |
| Strength of argument | Clean formalism, weak novelty claim | Stronger novelty claim, needs formal tightening |

**Recommendation for AAD**: Don't claim "we've extended Pearl's hierarchy." Do claim: "AAD identifies a class of reasoning tasks — model-modifying planning under model uncertainty — that goes beyond standard Level 1-3 causal inference. This class corresponds to the 'imagination' or 'structural exploration' mode that productively couples goals and model dynamics, and whose contamination of Level 1-3 evidence processing is the root cause of the directed separation problem in merged architectures."

This is honest: it identifies a genuinely new computational/cognitive task, connects it to the directed separation problem, and doesn't overclaim hierarchy-theoretic novelty that hasn't been proved.

---

*This is the most technically demanding spike of the night. Approach 2 (model uncertainty with model-modifying actions) is the stronger contribution. The inseparability argument — that model identification and inference can't be separated when actions modify models — is the tightest formal claim. Whether this is "Level 4" in the strict sense is less important than the practical truth: planning that changes causal structure requires different reasoning than planning within a fixed structure, and this distinction maps exactly onto the directed separation boundary.*
