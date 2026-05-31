---
slug: norm-explicit-strategy-condition
type: normative
status: conditional
depends:
  - def-strategy-dimension
  - der-causal-hierarchy-requirement
stage: draft
---

# Normative: Explicit Strategy Condition

The framework's design criterion for *when explicit strategy is worth maintaining at all*. An agent benefits from carrying an explicit strategy $\Sigma_t$ ( #def-strategy-dimension) when *the cost of planning is less than the cost of learning through exploration alone*. The inequality compares the cost of constructing and evaluating the strategy plus ongoing maintenance cost (as $M_t$ evolves and edges need revision) against the cost of learning action-outcome mappings through direct interaction plus the cost of correcting errors discovered only through execution. All costs are measured in the same units, typically time or tempo-equivalent cost.

The result is honestly *normative*, not derived. It is labeled as a design criterion rather than a theorem because loop-based and model-based approaches may differ along axes the cost inequality does not capture: final value (the model introduces bias; exploration may discover things planning cannot), risk profile (exploration risks real damage; planning risks wrong models), reversibility (some exploratory actions are irreversible), and model bias (explicit $\Sigma_t$ inherits the biases of $M_t$; loop-based learning does not). The inequality is correct *when* the outcomes are approximately equivalent — a condition that must be verified case by case, not assumed.

The intuitive cases are stated cleanly. The right side (explore + repair) is large — strongly favoring planning — when actions are expensive or irreversible (production deployments, military operations, surgical procedures); when exploration damage is severe (a wrong move loses the game; a wrong deployment takes down the service); when the environment is slow to respond (waiting for market or test feedback); when the action space is enormous (combinatorial planning). The left side (plan + maintain) is large — favoring pure exploration — when the environment is too complex or novel for useful models, when $M_t$ is severely inadequate, when the environment changes faster than $\Sigma_t$ can be maintained, or when actions are cheap and reversible (A/B testing, sandbox exploration).

The *normative grounding* is anchored in the persistence condition ( #result-persistence-condition), not in an external preference postulate. The persistence condition demonstrates that agents whose correction tempo is insufficient *degrade* — descriptive, not value-laden. The cost inequality operationalizes the consequence: approaches consuming less tempo budget leave more margin above the persistence threshold. The normative element is the preference for *maintaining persistence margin*, which is hard to argue against since the alternative is degradation. The Discussion below treats the strongly-favors-planning and strongly-favors-exploration cases in detail, the persistence-margin grounding, and the connection to the three-way exploit/explore/deliberate refinement in #disc-exploit-explore-deliberate; Working Notes flag the most useful practical reading — not as a binary decision rule but as a way to *calibrate strategy complexity* so the planning-and-maintenance cost stays just below the exploration-and-repair cost for the current environment.

## Formal Expression

*[Normative (explicit-strategy-condition)]*

An agent benefits from explicit $\Sigma_t$ when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

where:
- $C_{\text{plan}}$: cost of constructing and evaluating the strategy (deliberation, simulation, model queries)
- $C_{\text{maintain}}$: ongoing cost of keeping $\Sigma_t$ current as $M_t$ evolves (edge revision, structural updates)
- $C_{\text{explore}}$: cost of learning action-outcome mappings through direct interaction (real actions, real time, real consequences)
- $C_{\text{repair}}$: cost of correcting errors discovered only through execution (rollbacks, rework, damage)

All costs are measured in the same units (typically time or tempo-equivalent cost). The inequality requires that the two approaches produce approximately equivalent non-temporal outcomes — otherwise the comparison is between different strategies, not different approaches to the same goal.

## Epistemic Status

*Normative, not derived.* This is labeled *normative* because it is a design criterion (a preference for the less costly approach given equivalent outcomes), not a theorem. In practice, loop-based and model-based approaches may differ in:

- **Final value**: the model introduces bias; exploration may discover things planning cannot
- **Risk profile**: exploration risks real damage; planning risks wrong models
- **Reversibility**: some exploratory actions are irreversible
- **Model bias**: explicit $\Sigma_t$ inherits the biases of $M_t$; loop-based learning does not

The inequality is correct *when* the outcomes are approximately equivalent — a condition that must be verified case by case, not assumed. When the precondition fails (model-based and loop-based approaches produce qualitatively different outcomes), the cost inequality is insufficient and the choice requires richer analysis (e.g., expected regret including model error).

## Discussion

**When the inequality strongly favors planning.** The right side ($C_{\text{explore}} + C_{\text{repair}}$) is large when:
- Actions are expensive or irreversible (production deployments, military operations, surgical procedures)
- Exploration damage is severe (a wrong move in chess loses the game; a wrong deployment takes down the service)
- The environment is slow to respond (waiting for market feedback, waiting for test results)
- The action space is enormous (combinatorial planning problems)

In these domains, explicit $\Sigma_t$ is strongly motivated even if the planning model is imperfect.

**When the inequality favors pure exploration.** The left side ($C_{\text{plan}} + C_{\text{maintain}}$) is large when:
- The environment is too complex or novel for useful models (genuinely unknown territory)
- $M_t$ is severely inadequate (model predictions are worse than random)
- The environment changes faster than $\Sigma_t$ can be maintained ($\rho_\Sigma$ exceeds planning capacity)
- Actions are cheap and reversible (A/B testing, sandbox exploration)

**Normative grounding.** The cost inequality is grounded in the persistence condition ( #result-persistence-condition), not in an external preference postulate. The persistence condition demonstrates that agents whose correction tempo is insufficient *degrade* — this is a descriptive result, not a value judgment. The cost inequality operationalizes the consequence: approaches that consume less tempo budget leave more margin above the persistence threshold. The normative element is the preference for maintaining persistence margin — which is hard to argue against, since the alternative is degradation. (In TST, the temporal optimality postulate provides an additional normative grounding specific to software development.)

**Connection to the three-way tradeoff.** For actuated agents, the binary explore/exploit tradeoff extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), and deliberate (revise $\Sigma_t$). The cost inequality addresses the coarsest question (is explicit $\Sigma_t$ worth having?). The finer allocation between the three modes is addressed in #disc-exploit-explore-deliberate — the extended deliberation threshold is derived, but the broader three-way framing is discussion-grade. The deepest insight: deliberation is internal exploration (simulation, counterfactual reasoning, cross-domain synthesis), making it a fundamentally different resource type from external action.

## Working Notes

- The inequality as stated is static — it compares cumulative costs. A dynamic version would ask: "given current $M_t$ quality, is it worth deliberating further or should I act now?" This connects to #der-deliberation-cost's threshold: deliberation is worthwhile only when additional deliberation improves action quality enough to justify the time spent.
- Part of $C_{\text{maintain}}$ is the cognitive cost of keeping $\Sigma_t$ in the agent's representational capacity. For LLM agents, this means fitting the strategy in the context window. A 500-node DAG may exceed this capacity, making the left side of the inequality large enough that simpler strategies (or pure exploration) become preferable despite higher exploration costs.
- The cost inequality may be most useful not as a binary decision rule but as a way to calibrate $\Sigma_t$ complexity: the agent should maintain a strategy just complex enough that $C_{\text{plan}} + C_{\text{maintain}}$ stays below $C_{\text{explore}} + C_{\text{repair}}$ for the current environment. This gives a principled answer to "how detailed should my plan be?"

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** dedicated reflections at 526815, 584721, 773921, 829314, 849201 plus the batch dir 471203. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The calibration reading (already in Working Notes) was independently singled out as *"one of the most practical pieces of advice for software engineering and organizational design I have ever seen formalized"* (Claude, AUDIT-WORKING-773921) and the segment's most useful operational handle (Claude, AUDIT-WORKING-584721). Strong signal to promote the *"how detailed should my plan be?"* framing from Working Notes into the Brief / body.
- The reframing of the planning-vs-learning debate: the cost inequality *"reframes the question from doctrinal (planning-vs-RL camps) to empirical (which costs dominate in your domain?)"* (Claude, AUDIT-WORKING-584721). A clean contribution statement.

#### 2. Candidate Discussion

- **The Agile-vs-Waterfall mapping as the canonical worked instance.** Strong cross-substrate convergence (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921) that the four costs *are the mathematical foundation of software-engineering methodologies*: Waterfall assumes $C_{\text{repair}} \to \infty$ (space shuttle) and $C_{\text{explore}}$ prohibitive → spend heavily on $C_{\text{plan}} + C_{\text{maintain}}$; Agile/Lean assumes $C_{\text{repair}}$ cheap (revert a git commit) and $C_{\text{explore}}$ fast (A/B test) → minimize planning, gather interventional data instead. *"Neither approach is universally right — the optimal strategy depends entirely on the physical parameters of the environment ... Agile in a high-$C_{\text{repair}}$ environment like surgery dies; Waterfall in a low-$C_{\text{repair}}$/high-volatility web startup goes bankrupt paying $C_{\text{maintain}}$ for a plan that is instantly obsolete."* A candidate Discussion example or TST cross-reference.
- **The LLM context-window as a structural $C_{\text{maintain}}$ amplifier.** The Working-Notes point (a 500-node DAG may exceed an LLM's representational capacity) was read as load-bearing: *"for an LLM, $C_{\text{maintain}}$ is massive because of the finite context window — every plan step consumes tokens, crowding out operational memory ... the math says an LLM should not write a master plan up front; it should just start writing code and see what breaks — pure exploration is mathematically optimal for them given their current cognitive costs."* And the engineering corrective: *"if we want LLMs to plan better, we must artificially reduce their $C_{\text{maintain}}$ — external structured scratchpad / hierarchical memory to offload the description length of the DAG; AAT gives the exact equation for why this intervention is necessary"* (Gemini, AUDIT-WORKING-829314). Candidate Discussion sharpening connecting the cost inequality to scaffolding design — and it converges with the persistence-bandwidth-floor framing already noted in `#impl-causal-access`.

#### 3. Follow-up items (soft / scope-honesty)

- **"Loop-based learning does not inherit biases" overstates.** The Epistemic Status contrasts explicit-$\Sigma_t$ (inherits $M_t$ bias) with loop-based learning (does not). But direct exploration is still biased by policy selection, partial observability, confounding, update rules, and the model used to *interpret* observations. The honest contrast is *"planning inherits model bias differently,"* not *"loop learning is unbiased"* (Codex/Claude, AUDIT-WORKING-526815). Candidate one-clause fix.
- **Persistence-margin grounding is not universal across continuity stances.** The normative grounding leans on "preference for persistence margin, hard to argue against." But the continuity-stance work (`#disc-continuity-stance`) recognizes task-terminal / indifferent / negotiated-continuation agents — the criterion is compelling for agents whose *objectives require ongoing persistence*, and should not silently override the objective's stance toward continuation (Codex/Claude, AUDIT-WORKING-526815). Candidate scope qualifier.
- **Dependency-declaration gap.** The criterion is grounded in `#result-persistence-condition`, which is not declared in `depends:`. Acceptable if Discussion-only dependencies aren't tracked, but the grounding is substantive (Codex/Claude, AUDIT-WORKING-526815). Worth a glance against the project's depends-tracking policy.
- **Common-units / risk treatment.** Irreversible damage and heavy-tailed repair costs are not well represented by a static scalar inequality unless the cost measure already embeds risk; the equivalent-non-temporal-outcomes precondition is doing a lot of work (Codex/Claude, AUDIT-WORKING-526815). The body's caveat already names this; the signal is that it is easy to read past.

#### 4. Readers often ask / wonder

- **How does the three-way budget (exploit / explore / deliberate) get allocated in real time?** Several substrates noted the body's binary inequality answers only the coarsest question and the real interest is the dynamic three-way allocation — *"this maps exactly to the control loop of an advanced autonomous agent (Devin / SWE-agent); understanding how the framework triggers transitions between the three modes is the key to building AAT-compliant agents"* (Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314 — classical RL treats deliberation as computationally free, AAT costs it via $C_{\text{plan}}$). The body forward-points to `#disc-exploit-explore-deliberate`; readers want that pointer prominent.

#### Belongs elsewhere

- The compounding-fragility-of-long-chains material (chain-confidence decay, evidence starvation, cognitive cost = a "triple depth penalty") that auditors raised while reading this segment belongs at `#der-chain-confidence-decay` (the next segment), not here.
