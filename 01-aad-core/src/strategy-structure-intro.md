---
slug: strategy-structure-intro
type: discussion
status: discussion-grade
depends:
  - def-strategy-dimension
  - norm-explicit-strategy-condition
  - der-causal-hierarchy-requirement
stage: draft
---

# Chapter Introduction: Strategy Structure and the Diagnostic Split

We commit to a formal representation for strategy — a probabilistic causal DAG with AND/OR semantics and single-parameter edges — and develop the headline diagnostic that lives on top of it: the satisfaction gap and control regret as orthogonal signals that distinguish "the goal is hard" from "the strategy is weak."

## Formal Expression

*[Discussion]*

This segment is a chapter-introduction bridge. It carries no formal claim of its own; the chapter's substantive content lives in the five segments below: #der-chain-confidence-decay (the log-additive identity), #scope-and-or (the conjunctive/disjunctive scope restriction), #def-strategy-dag (the formal DAG with Correlation Hierarchy), and the satisfaction-gap / control-regret diagnostic split ( #def-satisfaction-gap, #def-control-regret).

## Epistemic Status

*Discussion-grade.* Framing for what follows, not a derivation.

## Discussion

Chapter 2 answered the prerequisite questions for planning. Level 2 causal access is required for $Q_O$ evaluation ( #der-causal-hierarchy-requirement); the feedback loop provides it ( #der-loop-interventional-access); CIY estimability partitions domains into three admissibility regimes ( #scope-ciy-observational-proxy); the joint exploit/explore policy objective is structured by $\lambda(M_t)$ ( #disc-ciy-unified-objective); and the explicit-strategy condition ( #norm-explicit-strategy-condition) decides when explicit $\Sigma_t$ is worth maintaining at all. Those preliminaries say *whether* to plan and *what data substrate* planning operates on. They do not say what a plan *is*, formally. Chapter 3 commits.

**The formal commitment, and what is and isn't derived in it.** $\Sigma_t$ is a probabilistic causal DAG with AND/OR combination semantics and single-parameter edges ( #def-strategy-dag, #scope-and-or). Three things in this commitment are *derived* rather than chosen: acyclicity follows from temporal ordering ( #post-causal-structure) — strategy nodes are propositions about future events, events have positions in time, no cycles. The Markov factorization follows from the Causal Markov Condition theorem under causal sufficiency ( #deriv-graph-structure-uniqueness) — postulates P1, P2, P4 plus causal sufficiency imply DAG-with-Markov-property as a sufficient representation. What *is* a formulation choice, within the strongly motivated graphical structure, is the AND/OR parameterization — single-parameter edges and node-level conjunction/disjunction labels rather than full conditional probability tables. The choice is parsimony-motivated and converged across three independent formalism attempts; alternative parameterizations (Noisy-OR, weighted combination) are rejected for documented reasons in #scope-and-or. The strategy DAG is thus a *theorem-backed graphical structure with a chosen parameterization within it*, not a wholly chosen representation.

**Causal insufficiency is handled explicitly.** The dominant real-world case — strategies whose nodes share latent common causes that aren't represented in the graph — would silently corrupt the AND/OR propagation if treated as an exception. The Correlation Hierarchy named in #def-strategy-dag handles it as part of the formalism: L0 (independence, the tractable baseline), L1 (augmented DAG with strict-prerequisite common causes factored above the correlation they create), L1' (mixture form for soft facilitators with observable common cause), L2 (full joint, exponential and impractical). The hierarchy is what makes #def-strategy-dag honest about its scope. The downstream identifiability-floor result ( #der-causal-insufficiency-detection) shows that *purely on-policy* detection of L0-insufficiency is impossible — the unique broadly-available escape is joint sibling observability under exploration, which is one of Section II's load-bearing applications of #der-loop-interventional-access.

**Why two diagnostic quantities, not one.** The chapter's headline contribution is the *orthogonal split* between two gaps: the satisfaction gap $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ ( #def-satisfaction-gap), and control regret $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ ( #def-control-regret). An earlier single-$\delta_{\text{objective}}$ framing conflated two distinct diagnostic situations — "the goal is too hard given the current model and policy class" and "the strategy is too weak relative to what's available in the policy class" — into one signal. The two cases warrant *different* corrective actions: revise $O_t$ vs. revise $\Sigma_t$. The split is what makes the 2×2 diagnostic table operate, and that table is the structural basis for the orient cascade in #der-orient-cascade. The inferential force of each diagnostic scales with the continuation convention from #def-value-object (C1 one-step / C2 receding-horizon / C3 Bellman): under C1 the "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means *locally stuck*; under C3 it means *globally infeasible*. The diagnostic *form* is convention-independent; the *force* is convention-dependent.

**Chain confidence decay is foundational, not incidental.** The chapter opens with #der-chain-confidence-decay, the chain rule of probability lifted into log-confidence: $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$. The identity is elementary, but it does load-bearing work three layers deep. It anchors the additive-coordinate-forcing meta-pattern at the chain layer ( #disc-additive-coordinate-forcing) — the three other primary instances (reverse-KL at the divergence layer, log-odds at the update layer, Fisher metric at the metric layer) each cite this chain-layer identity as the analog motivating their additivity axiom. It grounds the structural pressure toward shallow strategies (deep chains have geometrically decaying confidence). And it composes with the per-edge update-rate decay from #deriv-edge-credence-dynamics to produce the triple depth penalty (confidence decay + evidence starvation + cognitive cost) developed in #form-strategy-complexity-cost. Its placement at the *head* of the chapter is deliberate — the chapter's other results inherit its additivity structure, and several Section II–wide results depend on it.

**The flow of the chapter.** Chain-rule identity ( #der-chain-confidence-decay) → AND/OR scope restriction ( #scope-and-or) → formal DAG with Correlation Hierarchy ( #def-strategy-dag) → the orthogonal diagnostic split ( #def-satisfaction-gap, #def-control-regret). By chapter end the reader has the formal strategy representation, the honest treatment of causal insufficiency, and the diagnostic signals that distinguish goal-revision triggers from strategy-revision triggers. Chapter 4 develops the per-edge dynamics that make individual strategy components update over time; Chapter 5 synthesizes the diagnostic into the orient cascade.

## Working Notes

- This is a chapter-introduction Discussion segment; it bridges Chapter 2's planning-decision arc to Chapter 3's formal strategy structure and diagnostic split. The Formal Expression is intentionally empty.
- The framing "Chapter 2 says whether to plan; Chapter 3 says what a plan IS" is the conceptual core. The decision to plan precedes the formal definition of what a plan is — this is the sharpest joint in Part II per the OUTLINE walkthrough.
- The "what is and isn't derived in the formal commitment" framing is meant to address what could otherwise read as overclaim. Joseph's stated discipline on this layer is to be explicit about which moves are theorem-backed and which are formulation choices, and the strategy-DAG segment is one of the places where the distinction matters most: acyclicity and Markov are theorem-backed, AND/OR is a chosen parameterization.
- The "two diagnostic quantities, not one" framing surfaces the orthogonality argument that makes Section II's headline contribution legible. The reader should leave Chapter 3 understanding *why* the split is structural rather than arbitrary — and why the 2×2 table that operates on it requires the split rather than being expressible in a single scalar.
- The chain-confidence-decay paragraph is doing pedagogical work that might otherwise be lost: the identity looks elementary and could read as a throwaway opener. Naming the three downstream layers it anchors prevents the reader from undervaluing it.
