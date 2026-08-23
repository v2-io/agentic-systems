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

An agent with a goal needs more than a model of reality. It needs a theory of how its own actions produce progress toward the goal — which steps depend on which, which alternatives are available, where the uncertainty lives. Chapter 3 makes that theory formal.

Chapter 2 answered the prerequisite questions: planning requires Level-2 causal access ( #der-causal-hierarchy-requirement); the feedback loop supplies it ( #der-loop-interventional-access); explicit strategy is worth maintaining when the cost-benefit favors it ( #norm-explicit-strategy-condition). None of that tells us what a strategy *is*, formally. Chapter 3 commits.

The commitment is more constrained than it might look. We don't choose acyclicity — it falls out of temporal ordering. Strategy nodes are propositions about time-indexed future events (a retried step is a new node at a later time), events have positions in time, and time has a direction, so the graph cannot have cycles. We don't choose the Markov property either — given causal sufficiency, the Causal Markov Condition theorem (Spirtes–Glymour–Scheines, Pearl) forces the factorization. What we *do* choose, inside the strongly motivated graphical structure, is the parameterization: single-parameter edges with AND/OR combination semantics at nodes, rather than full conditional probability tables. The choice is parsimony-motivated — each edge carries one number rather than a $2^k$ table at a node with $k$ parents — and it converged across three independent attempts to formalize the same content. Alternative parameterizations (Noisy-OR everywhere, weighted combinations) are rejected for documented reasons; see #scope-and-or.

The wrinkle the formalism handles explicitly is causal insufficiency. Most strategy graphs in the wild have nodes that share latent common causes — shared infrastructure, common-mode risks, correlated adversary actions — that the agent has not represented as nodes. Naive AND/OR propagation on such graphs produces systematically biased plan-success estimates: it overestimates redundancy on OR-structures (the parallel paths share their failure modes) and underestimates joint reliability on AND-structures (the prerequisites also share their successes). The Correlation Hierarchy (L0 / L1 / L1' / L2, in #def-strategy-dag) handles this as part of the formalism rather than as an exception. There is a sobering downstream result: under purely on-policy execution, an agent at L0 *cannot detect* its own causal insufficiency from its own data — the worlds with and without a latent common cause are observationally indistinguishable from on-policy traces alone (the no-go in #der-causal-insufficiency-detection). The unique broadly-available escape is joint sibling observability under exploration — "broadly available" in the defined sense of #der-causal-insufficiency-detection: the one of its five escape routes that uses only machinery the theory already requires. This is one of Part II's load-bearing applications of #der-loop-interventional-access.

The chapter's headline result is the diagnostic split. When an agent is not achieving its goal, the framework asks two distinct questions, not one. The satisfaction gap

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$$

is positive when the best policy in the agent's current class cannot reach the satisfaction threshold given the agent's current model. Control regret

$$\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$$

is positive when the agent is leaving value on the table — its current policy is worse than the best available. Together they produce a 2×2 cell map: goal attainable + policy good is success; goal attainable + policy poor means revise the strategy; goal unattainable + policy poor means revise the strategy first and then re-check; goal unattainable + policy good is the *capability limit* — the agent is doing the best it can but the goal is out of reach. Each cell prescribes a different corrective action, and getting the prescription right requires the orthogonal split. An earlier framing that lumped everything into a single goal-distance signal could not distinguish "the goal is too hard" from "the strategy is too weak" — and the two have different remedies. The split is what makes the orient cascade (Chapter 5) actionable.

A detail worth surfacing up front. The chapter opens with #der-chain-confidence-decay — the chain rule of probability lifted to log-space:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lt i})$$

The identity is elementary; the consequence is not. Deep strategies are exponentially fragile in their depth — confidence in a 10-step plan is the product of 10 conditional probabilities, and each one is less than 1. This grounds the structural pressure toward shallow, parallelizable strategies. The same log-additive structure also anchors three other uniqueness theorems downstream in AAT (reverse-KL at the divergence layer, log-odds at the update layer, Fisher metric at the metric layer) — see #disc-additive-coordinate-forcing for the catalog. The identity at the head of this chapter does load-bearing work three layers deep.

The flow of the chapter: chain-rule identity ( #der-chain-confidence-decay) → AND/OR scope restriction ( #scope-and-or) → formal DAG with Correlation Hierarchy ( #def-strategy-dag) → orthogonal diagnostic split ( #def-satisfaction-gap, #def-control-regret). The chapter leaves us with a formal strategy representation, an honest treatment of causal insufficiency, and the diagnostic signals that tell whether the problem is the goal, the strategy, the model, or some combination.

![[src/img/strategy-dag-example.pdf]]
{#fig-strategy-dag-example caption="A worked strategy DAG. Leaf base credences and single-parameter edge credences propagate through AND/OR combination to a strategy-plan-confidence score at the root. The numerics are shown so the propagation can be checked by hand; the single-parameter edge is the chosen parameterization (noisy-OR and weighted variants were rejected)."}

## Working Notes

- This is a chapter-introduction segment; it bridges Chapter 2's planning-decision arc to Chapter 3's formal strategy structure and diagnostic split. It carries no formal claim of its own.
- The framing "Chapter 2 says whether to plan; Chapter 3 says what a plan IS" is the conceptual core. The decision to plan precedes the formal definition of what a plan is — this is the sharpest joint in Part II per the OUTLINE walkthrough.
- The "what is and isn't derived in the formal commitment" framing addresses what could otherwise read as overclaim. Acyclicity and Markov are theorem-backed; AND/OR is a chosen parameterization. Surfacing the distinction is important because the strategy-DAG segment is one of the places where the *derived vs. chosen* distinction matters most.
- The "two diagnostic quantities, not one" framing surfaces the orthogonality argument that makes Part II's headline contribution legible. Earlier single-signal framings could not distinguish the two situations and therefore could not prescribe different remedies.
- The chain-confidence-decay paragraph names what the identity unlocks downstream. The identity itself looks elementary; the three load-bearing layers it anchors are not.

### Incidental audit gold (lift 2026-05-31, A8 batch)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / forward-vision material kept separate from certified theory-fix findings. **Coverage:** this chapter-intro reached a digested reflection in 2 dirs (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-526815); the broader strategy-structure cluster was walked by ~7 substrates whose per-segment notes landed on the content segments rather than the intro.

#### 1. Candidate Brief prose / pre-prose

- The chapter's own one-line self-description converged independently as the standout framing: *"goal too hard" vs "strategy too weak" require different remedies* — the diagnostic split is the point of the whole chapter (Claude, AUDIT-WORKING-526815). A Brief-grade compression of what the intro already develops at length.

#### 2. Candidate figures

- **The 2×2 diagnostic-split diagram as the chapter's anchor figure.** Independently flagged as "the clearest diagram" for the whole chapter intro: one axis satisfaction gap, the other control regret, the four cells prescribing continue / revise-strategy / revise-strategy-then-recheck / capability-limit. The rationale: it "directly captures why the two-signal formulation is better than a single goal-distance signal" (Claude, AUDIT-WORKING-526815). Note the existing `#fig-strategy-dag-example` is the DAG-propagation figure; this proposed 2×2 is a *second*, complementary chapter figure. (Multiple substrates independently reached for this same 2×2 across the cluster — see the `def-satisfaction-gap` / `def-control-regret` gold.)

#### 3. Follow-up items

- **Chapter-intro navigation hazard.** One auditor mis-entered the chapter by opening `strategy-structure-intro.md` as if it were the *Part II* intro (its filename reads like a part entry point), reading it before its upstream dependencies and self-flagging a topological-order violation. Suggested mitigations: chapter-number filename prefixes, or an explicit `part-intro.md` per Part so an `ls` does not present a chapter-intro as a part entry point (Claude, AUDIT-WORKING-773921). A naming/navigation signal, not a theory issue — routes to the naming/FORMAT workflow, not this segment's body.

#### Off-ramp (NOT gold — flagged for the certified track)

- **Intro-level acyclicity wording may under-state the time-unrolling condition.** The intro says acyclicity "falls out of temporal ordering"; an auditor noted this is exact only for time-indexed event *tokens* (or once retry-loops / maintenance-cycles / feedback-plans are explicitly unrolled in time), not for reusable event *types* with repeated subgoals — and suggested the intro state the time-unrolled / event-token condition the way `#def-strategy-dag` does (Claude, AUDIT-WORKING-526815). The same auditor noted on re-reading `#def-strategy-dag` that the full segment *does* state the condition properly (retry loops as distinct time-indexed nodes), so the gap, if any, is intro-summary wording only — a small framing-precision item, recorded for the lead to judge whether it rises to a finding.
