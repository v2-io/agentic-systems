# Sub-Spike B: Component Admissibility

**Status**: derivation. Three-class partition; characterization of failure modes for Class C; quality-vs-separation tradeoff inside Class B.
**Date**: 2026-05-09
**Depends on**: `01-theorem-statement.md` (especially condition C1).

---

## 1. The condition restated

**(C1) Goal-blind admissibility.** The query set $\mathcal{Q}_A$ contains queries whose specification can be constructed from $(M_W, o_W)$ alone — i.e., there exists a query selector $q_M : \mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A$ such that $A(q_M)$ provides a non-trivial belief-update.

The "non-trivial" qualifier matters: every component admits the trivial goal-blind query "do nothing / null query," but the response is uninformative. The condition is interesting only when goal-blind queries yield information sufficient for $f_M$ to make non-trivial updates.

This sub-spike partitions components by admissibility class.

## 2. The three-class partition

### 2.1 Class A — goal-blind by design

Components whose interface is *already* goal-blind: queries take observation-grounded inputs and return facts/predictions/embeddings that the wrapper can use. The wrapper construction in this case is straightforward — the component is already Class 1 by itself; wrapping adds the explicit $G_W$ scaffold but doesn't require any structural separation work.

Examples:

- **POMDP belief-state filters.** $f_M$ is a Bayesian update on the observation; no goal input. These are Class-1 by design.
- **World models / generative models of the environment.** Take observation, return next-state prediction. Goal-blind by interface (the model doesn't know about goals). E.g., a learned dynamics model in MBRL.
- **Sensory pipelines.** Image classifiers, OCR, speech-to-text. Take input, return labels/text. No goal role.
- **Memory retrieval systems.** Vector DB queries, semantic search. The query content may correlate with goals, but the retrieval mechanism itself doesn't take a goal input.
- **Domain-specific oracles.** Calculators, theorem provers, databases. Goal-blind by design.

For Class-A components, (C1) is trivially satisfied. (C3) is also trivially satisfied — the component doesn't have access to $G_W$ in any form. The wrapping construction works exactly, and the wrapping move is mostly *organizational* (giving the system explicit $G_W$ structure and an Interpres loop).

This is also why directed-separation is "easy" for purely-perceptual systems: the perception components are Class-A, and the goal-conditioning happens only at the action-selection layer.

### 2.2 Class B — admit a goal-blind query mode

Components that *can* be queried goal-conditionally (and typically are, in practice) but also support goal-blind queries. This is the interesting wrapping case — a single component plays two roles: goal-blind for $M_W$ updates, goal-conditioned for $G_W$ updates.

Examples:

- **Large language models.** Can be prompted with "summarize this observation" (goal-blind) or "given goal $G$, plan next action" (goal-conditioned). Both modes are accessible from the same model. Wrapping splits the usage into two channels.
- **Hybrid RL agents with separable value/policy components.** The value function $V(s)$ or $Q(s, \cdot)$ may be queryable as a goal-blind state-evaluator, while the policy $\pi(s, g)$ is goal-conditioned.
- **Modular cognitive systems.** Anything where one black-box module supports multiple query types — e.g., a reasoner that answers both "what's true?" (epistemic) and "what should I do given goal X?" (instrumental).
- **Multi-modal models (vision-language, etc.).** Often admit both perception-only queries (caption an image) and goal-conditioned queries (describe what's relevant for goal X).

For Class-B components, (C1) holds *operationally* — the wrapper has to *choose* to use the goal-blind mode, and the choice is up to the wrapper's design. (C3) is the question of whether the goal-blind query *actually delivers* a goal-blind response. Typically not exactly, due to pretraining-induced correlations (sub-spike C).

The wrapping construction is *substantive* for Class B — it's the design move that takes a multi-mode component and uses it in a structurally separated way.

### 2.3 Class C — fundamentally goal-conditioned

Components whose *only* operating mode requires goal-conditioning. The wrapper cannot construct a goal-blind query because the component's interface intrinsically demands a goal as input.

Examples:

- **Pure end-to-end goal-conditioned policy networks.** $\pi : \mathcal{S} \times \mathcal{G} \to \mathcal{A}$ where the goal $g$ is a required input and the network has no separable belief or value channel. Running with a "null goal" is undefined behavior.
- **Reward-model-conditioned generators.** Models trained to produce outputs scored under a reward model that takes a goal/preference as input.
- **Closed-loop systems with internal goal-state inseparable from world-model.** E.g., an agent whose internal representation tangles "where I am" and "where I want to be" in a single vector with no projection to a goal-blind subspace.

For Class-C components, (C1) fails. The wrapping construction does not apply directly. The component can still be used inside a larger system, but the system cannot be Class-1 at the wrapper level via this construction — the goal-information leakage is at the input level, not the response level.

**Honest scope: Class-C components are scope-out for the basic theorem.** Sub-spike H (Parts III/IV connection) may identify whether any partial result is available — e.g., approximate Class-1 status with leakage rate equal to the component's goal-conditioning sensitivity — but the basic theorem of `01-theorem-statement.md` does not address Class-C.

### 2.4 Quasi-classes and edge cases

- **Class A* (Class-A with goal-conditioned auxiliary).** A nominally goal-blind component (e.g., world model) that has been *fine-tuned* on goal-correlated data and now exhibits goal-bias in its outputs. Operationally Class-B with strong leakage rather than Class-A.
- **Class B* (Class-B with effective Class-C use).** A multi-mode component that the wrapper *could* use in goal-blind mode, but in practice uses goal-conditionally (because the goal-conditioned mode is more accurate). The construction is then *design-foregone* rather than infeasible.
- **Class B with degraded goal-blind mode.** A component whose goal-blind queries are technically supported but produce much worse outputs than goal-conditioned queries. The wrapper pays a cost in $f_M$ quality. This connects to the quality-vs-separation tradeoff in §3.

## 3. The quality-vs-separation tradeoff (within Class B)

For a Class-B component, the wrapper has a design choice: how aggressively to restrict $q_M$ to goal-blind content, vs. how much to allow context that might inform the response (and risk leakage).

### 3.1 The extremes

**Maximally goal-blind.** $q_M$ contains *only* the current observation, with no context, no history, no metadata. The component answers a narrow question. Goal-blind by construction (no goal-correlated content in the query). But the response may be information-poor — the component can't use context to disambiguate or focus.

**Maximally informed.** $q_M$ contains the full observation history, all retrievable memories, and contextual cues. The component answers a richer question. The response is information-rich. But the context content correlates with goals (the wrapper has been selectively retrieving goal-relevant content), so the goal-blind query is goal-blind only nominally.

### 3.2 The tradeoff

There's no clean optimum. Wrapper design choices that maximize $f_M$ information often increase leakage; choices that minimize leakage often produce information-poor $f_M$. This is a real engineering tradeoff in practice.

Sub-spike C will quantify the leakage side. The information-side quality is harder to characterize abstractly — it depends on the task and the component's response distribution conditioned on richer vs. sparser queries.

A useful framing: leakage rate $\kappa$ from sub-spike C scales with the mutual information between the query content and $G_W$. The wrapper minimizes this by reducing query content. But that also reduces the information $A(q_M)$ provides about the world, hurting $f_M$.

A clean result we'd want here (probably in sub-spike C): $\kappa \le I(q_M ; G_W)$ — the leakage is upper-bounded by the mutual information between the query selection and the goal. This connects to the wrapper's policy-of-attention: how much does $q_M$ depend on $G_W$ implicitly through the wrapper's state?

Wait — the wrapper's $q_M$ has type $\mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A$, *no $G_W$ argument*. So $q_M$ doesn't depend on $G_W$ structurally. But $M_W$ may depend on $G_W$ historically — past states of the wrapper accumulated belief in goal-relevant ways because past observation-selection was via $\pi_W$ which is goal-conditioned.

So the path is: $G_W$ → past $\pi_W$ choices → past observations → $M_W$ → $q_M$ → component query content → leakage. This is a *historical* leakage path, not a current-step leakage path. The directed-separation theorem of §1.2 is about current-step independence, conditioning on $M_W$. Historical correlation between $M_W$ and $G_W$ is allowed by the theorem.

But: in Theorem 2 (approximate form), the leakage bound $\kappa$ applies to the conditional $P(A(q_M) | q_M, G_W)$. Historical correlations matter only insofar as $A$ infers $G_W$ *from $q_M$ itself*. If $q_M$ contains content that statistically correlates with $G_W$ in $A$'s pretraining distribution, $A$ may infer $G_W$ probabilistically from $q_M$ even though $q_M$ doesn't structurally encode $G_W$.

So the fundamental leakage mechanism is: query content carries goal-information in pretraining-distribution-induced correlation. This is the (C3) failure mode and is the center of sub-spike C.

## 4. PROPRIUM and Parts III/IV — class assignment

LLMs sit in Class B. They support both modes (goal-blind summarization/extraction, goal-conditioned planning/generation), and the wrapping construction extracts goal-blind information for $M_W$ via prompting choices.

The leakage rate $\kappa$ for LLMs is:
- Plausibly small for queries on observation-grounded content unrelated to goal-content (e.g., "summarize the OCR'd text").
- Plausibly large for queries on observation-grounded content that's heavily goal-correlated (e.g., "what facts are relevant?" — this query *is* goal-conditioned by inference).

PROPRIUM's nine-component architecture (per memory) includes structural separation between components that handle world-state and components that handle goal-state. This is consistent with using the underlying LLM as a Class-B component with deliberate goal-blind / goal-conditioned mode separation.

Sub-spike H will work this out concretely once sub-spike F (empirical instances) characterizes PROPRIUM in detail.

## 5. Failure modes for Class C and what (if anything) can be salvaged

Class-C components fail (C1). The wrapping construction's structural separation breaks at the input layer.

What partial results might be available?

**Salvage attempt 1: null-goal queries.** If the component admits a "null goal" or "no preference" input that produces a goal-neutral response, this could serve as a goal-blind query. But this requires the null-goal mode to be well-defined and to produce information-bearing responses. Many goal-conditioned components don't have this — running them with a null goal produces nonsense or refusal.

**Salvage attempt 2: goal-uniform averaging.** Run the component with a representative sample of goals and average the responses. The averaged response is goal-blind in expectation but loses information specific to any one goal. This is operationally expensive ($K$ queries per macro-step instead of one).

**Salvage attempt 3: goal-blind extraction via auxiliary head.** Train or distill a separate goal-blind component (e.g., "predict the next observation regardless of goal") that lives alongside the goal-conditioned one. This converts Class C into Class A* by adding capability — a different construction, not pure wrapping.

**Salvage attempt 4: accept Class-3 status and use AAD's existing scope-restricted machinery.** If wrapping doesn't work, the system remains Class-3, and AAD's results apply only with the corresponding scope restrictions. This is what CLAUDE.md's existing "Class 2 exit" framing acknowledges.

For Class-C, the honest answer is: the basic theorem doesn't apply, and salvage attempts cost something (information loss, computation, additional training). Whether any salvage is worthwhile depends on the application.

## 6. Verdict and connections

**(C1) characterization**: Class-A components satisfy (C1) trivially. Class-B components satisfy (C1) operationally — the wrapper's design must include a goal-blind query mode. Class-C components fail (C1) and are scope-out for the basic theorem.

**The wrapping move is non-trivial only for Class B.** Class A is already Class-1; Class C cannot be wrapped without modification. Most practical interest is in Class B — LLMs, hybrid RL agents, multi-modal models. The PROPRIUM / Parts-III/IV instance is Class B.

**Quality-vs-separation tradeoff**: Within Class B, the wrapper trades $f_M$ information against leakage rate $\kappa$. This is a real engineering tradeoff and will be quantified in sub-spike C.

**Connections to existing AAD**:
- Strengthens the architecture-class taxonomy in `#der-directed-separation` by introducing the *operational* Class-B distinction (admits goal-blind mode but isn't natively goal-blind).
- Connects to `#hyp-directed-separation-under-composition` — the hypothesis is restricted to admissible components; Class-C components remain genuinely scope-out.

## 7. Honest limits

What this sub-spike does:
- Partitions components by admissibility.
- Characterizes Class B as the substantive wrapping case.
- Identifies the quality-vs-separation tradeoff inside Class B.
- Notes salvage attempts for Class C and their costs.

What this sub-spike does *not* do:
- Provide a precise quantitative criterion for "non-trivial belief-update" — the qualifier in (C1). I've used it informally; making it precise would require defining a minimum-information-gain threshold per macro-step.
- Address the case of *time-varying* admissibility — components that are Class B in some operating regimes and effectively Class C in others (e.g., LLMs that resist goal-blind use under adversarial prompting).
- Verify class-membership for any specific real component empirically. Sub-spike F's instance survey will help here.

The (C1) characterization is honest at the structural level. The quantitative leakage characterization for Class B is in sub-spike C; the empirical verification for specific systems is in sub-spike F.

---

## File index

- This file: `02-admissibility.md`
- Brief: `00-brief.md`
- Theorem statement (depended on): `01-theorem-statement.md`
- Leakage (next): `03-leakage.md`
