---
slug: def-causal-information-yield
type: definition
status: exact
depends:
  - der-action-selection
  - def-mismatch-signal
stage: deps-verified
---

# Definition: Causal Information Yield

The framework defines a scalar quantity attached to each available action: the **causal information yield** (CIY), measuring the *action-distinguishability* of an action — how different its interventional outcome distribution is from what alternative actions would produce. The construction uses Pearl's intervention operator $do(\cdot)$ and is the expected KL divergence between the outcome distribution under $do(a)$ and the outcome distribution under $do(a')$, averaged over a reference distribution of alternative actions. CIY is non-negative by construction; it is zero for passive observers or agents whose actions don't affect outcome distributions; it is strictly positive exactly when actions causally alter what is observed — the property that distinguishes Pearl-Level-2 (interventional) from Level-1 (associational) epistemic access.

A subtle conceptual point: CIY measures *distinguishability*, not *learning value*. An action can have high CIY even when the agent already knows the outcome distributions perfectly — the distributions *are* different (high CIY), but the agent learns nothing new by confirming what it already knows. High CIY is therefore *necessary* for learning (indistinguishable actions can't teach anything) but not *sufficient* (distinguishable actions only teach when the agent is uncertain). The Discussion below treats the relationship to expected information gain, the $\lambda$-weighted surrogate in the unified policy objective, query actions (accessing another agent's already-compressed model), and the adversarial mirror (deceptive responses that exploit high trust to inject misdirected updates).

## Formal Expression

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

The $do(\cdot)$ operator is Pearl's standard intervention notation (Pearl 2009, *Causality*, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022); the AAT recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy operationally. $\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Pearl's Level 2 (interventional) from Level 1 (associational) epistemic access.

## Epistemic Status

The CIY *definition* is well-grounded in causal inference theory. The quantity itself is standard — an expected KL divergence under the do-calculus. The interpretive claim — that CIY measures action-distinguishability rather than expected information gain — is exact (it follows from the definition). The relationship between CIY and learning value (see Discussion) is discussion-grade: the $\lambda$-weighted approximation to EIG is heuristic, not derived.

## Discussion

**CIY measures distinguishability, not learning value.** CIY as defined is the expected KL divergence between outcome distributions — how different the outcomes of $a$ are from the outcomes of typical alternatives. This is **action-distinguishability**, not **expected information gain** (EIG). The distinction matters: an action can have high CIY even when the agent already knows the outcome distributions perfectly (the distributions ARE different, but the agent learns nothing new by confirming what it already knows). High CIY is *necessary* for learning (indistinguishable actions can't teach anything) but not *sufficient* (distinguishable actions only teach when the agent is uncertain about the distinction).

The two quantities approximately coincide when $U_M$ is high — when the agent doesn't know the outcome distributions, high-CIY actions also have high EIG because observing a characteristically different outcome updates the agent's beliefs about the causal structure. They diverge when $U_M$ is low — a confident agent gains nothing from taking a distinguishable action it already understands.

The $\lambda(M_t)$ weighting in the unified policy objective ( #disc-ciy-unified-objective) partially compensates: when $U_M$ is low, $\lambda \to 0$, suppressing the CIY term regardless of its magnitude. This makes the exploration term behave more like EIG — suppressing exploration when the agent is already certain. The compensation is heuristic (the $\lambda$ form is not derived). For the current theory, CIY serves as a tractable surrogate for EIG, with the $\lambda$ weighting providing the uncertainty-gating that makes the surrogate reasonable.

**Open direction: proper EIG within AAT.** Replacing CIY with a proper expected information gain quantity — $\text{EIG}(a; M) = I(o; \theta \mid do(a), M)$ where $\theta$ parameterizes the model — would be a stronger foundation for the exploration term, particularly in domains where the agent must decide between actions that are all highly distinguishable but differ in what they teach. Under certain scopes (intervention-rich domains with well-parameterized models), the EIG formulation might yield sharper exploration strategies — preferring actions that resolve the *most uncertain* causal links rather than the most distinguishable ones. Whether this yields operationally significant improvements over the $\lambda$-weighted CIY surrogate is an empirical question. The CIY formulation has the advantage of being computable from the agent's current model alone (it doesn't require reasoning about model uncertainty); EIG requires a meta-model of what the agent doesn't know.

**Dependence on the reference distribution $q$.** The quantitative CIY value depends on the choice of $q$, which is a significant degree of freedom. A uniform $q$ treats all alternatives equally; a policy-induced $q$ emphasizes alternatives the agent would consider. AAT adopts the policy-induced $q$ as default: $q(\cdot \mid M) = \pi(\cdot \mid M)$, yielding CIY as "how different is this action's outcome from what I'd typically see?" CIY values are not comparable across different $q$ choices.

**Query actions: accessing external models.** A qualitatively distinct class of actions: querying another agent's model. When a reliable source exists (expert, database, documentation, well-trained LLM), "ask a well-formed question" can yield information equivalent to thousands of probe-observe cycles. The source's model has already performed the compression work ( #form-information-bottleneck) — the response transfers the *output* of compression rather than requiring the agent to reconstruct it.

Key properties of query actions:
- **Information density**: Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes
- **Trust-dependent gain**: Update from query depends on the agent's model of the source's reliability and alignment, not on observation channel noise ( #hyp-communication-gain)
- **Pre-compressed information**: Responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align
- **Structural adaptation via external models**: Encountering another agent's model can trigger structural change ( #result-structural-adaptation-necessity) — incorporating external representational structure rather than building it de novo ("grafting")

When high-CIY query channels are available, the unified policy objective ( #disc-ciy-unified-objective) favors query actions over direct probes, particularly when $U_M$ is high, a trusted source exists, query cost is low, and the needed information is about *structure* rather than the agent's specific situation.

**The adversarial mirror: deception and model corruption.** The same channel that enables cooperative knowledge transfer can be exploited to degrade the opponent's model. A deceptive response yields positive CIY in the strict information-theoretic sense, but the content drives model-reality mismatch *upward*. The update gain $\eta^\ast$ for the victim depends on trust; successful deception exploits high trust to inject a large, misdirected update. In the Lyapunov framework ( #result-sector-condition-stability), this is adversarial disturbance injected through the observation channel, with coupling coefficient $\gamma_A$ determined by the victim's trust level and exposure. See #hyp-communication-gain for the formal treatment of trust-dependent gain, and #der-adversarial-destabilization for the Lyapunov formalization. Distributed tempo, topology analysis, and game-theoretic integration are Part III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`).

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 10 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 471203, 526815, 584721, 742613, 773921, 849201) plus the batched 963715 (19–23 batch); 472913, 613842, 829314 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **"A deterministic button that goes beep: high CIY, zero EIG."** The recurring crystallizing example of the CIY-vs-EIG distinction: an action can be perfectly distinguishable from alternatives (high CIY) yet teach nothing once you already know the outcome (zero learning) (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-849201 — "pushing a button turns on a red light: high CIY, zero EIG after the first press"). The cleanest Brief seed for the segment's signature move.
- **CIY grounds "exploration / curiosity" as something measurable.** "Exploration is not random action; it is taking actions that maximize the KL divergence between expected outcome distributions" — grounding exploration bonuses / intrinsic motivation in interventional causal calculus rather than ad-hoc state-visitation counts (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921).

#### Candidate Discussion

- **Why CIY (not EIG) — a pragmatic-engineering defense worth stating plainly.** "It justifies using the slightly-wrong-but-computable math over the perfect-but-intractable math": CIY is computable from the *current* model, whereas EIG ($I(o;\theta \mid do(a), M)$) requires a meta-model of uncertainty; the $\lambda(M_t) \to 0$-as-$U_M \to 0$ gating makes CIY *behave* like EIG without being it (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847 — "most exploration frameworks conflate distinguishability with learning value; the distinction is sharp and practical"). The Discussion has the distinction; this is a candidate sharpening of the *engineering rationale*.

#### Follow-up items

- **Term-vs-substance naming concern — the segment's main framing follow-up.** "Causal information *yield*" connotes learning gain, but the segment goes to substantial trouble to clarify CIY measures *distinguishability*, not learning value. Candidate: keep CIY as the formal name but surface "action-distinguishability" (or "interventional contrast") as the substantive gloss more prominently — currently only in Discussion (Claude, AUDIT-WORKING-471203 — "consider titling it 'Causal Information Yield (Action-Distinguishability)'"; Claude, AUDIT-WORKING-361742; Claude, AUDIT-WORKING-266847). Routes to terminology workflow.
- **Tier-inheritance on downstream use.** Frontmatter `status: exact` is right for the *definition*, but the CIY-as-exploration-objective *use* is heuristic (the $\lambda$-weighting is not derived). Watch that downstream segments inherit the *heuristic* tier on that use, not the definition's `exact` (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-849201 — "any later 'optimal exploration policy' theorem cannot be optimal if it relies on a heuristic surrogate for EIG").
- **Reference-distribution $q$ is a real degree of freedom.** CIY values are not comparable across $q$ choices; policy-induced $q = \pi(\cdot \mid M)$ is the pragmatic default but makes CIY partly a measure of surprise relative to the agent's *own action habits*, not an intrinsic action property (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-361742; Claude, AUDIT-WORKING-742613 — for actuated agents the default likely needs $q(\cdot \mid M, G)$, inheriting the `der-action-selection` $M$-vs-$X$ scope item).
- **Overstuffed-for-a-definition.** Several note the Discussion pulls in unified-policy-objective, communication gain, structural adaptation, sector stability, adversarial destabilization, Part III topology/game-theory, and an `old-tf-appendix-f-multi-agent.md` source — none declared deps and several well downstream. Candidate: keep the definition + the CIY-vs-EIG caveat here, move query/deception/Part III material to the communication / adversarial segments (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-742613). The `old-tf-*` reference is also the diff-voice/lineage pattern (Claude, AUDIT-WORKING-471203).

#### Readers often ask / wonder

- "Does AAT ever develop the proper EIG quantity, or prove CIY $\equiv$ EIG under stated conditions? The 'Open direction' names it as future work; if the exploration objective is load-bearing for Part II, tightening this matters" (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-584721).
- "Is $\mathrm{CIY} = 0$ for a passive observer a *theorem* or a *convention*? Passive observers lack the action/comparator distribution the definition needs, and '$\mathrm{CIY} \gt 0$ when actions causally alter outcomes' requires $q$ to put mass on alternatives whose distributions differ" (Codex/Claude, AUDIT-WORKING-742613).

#### Candidate figures

- **A three-distribution comparison with a separate uncertainty gate**: three interventional outcome distributions $P(o \mid do(a))$, $P(o \mid do(a'))$, …; CIY is the expected KL from the chosen action's distribution to comparators under $q$; a *second, separate* gate labeled $U_M$ shows why distinguishability only becomes learning value when the model is uncertain — making the CIY-vs-EIG split visible in one picture (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **Query actions as "culture / language / cultural transmission" (points at Parts III/IV and `03-llm-core/`).** "Grafting" — querying a database/expert returns an answer *already compressed by someone else's Information Bottleneck*, bypassing the local compression phase — "seems like the definition of Culture or Language"; the optimal strategy for any bounded agent is "almost always to find a smarter agent and ask it, rather than learning from scratch," mathematically justifying cultural transmission over individual trial-and-error (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203 — for LLM agents, internal token-gen / tool calls / retrieval are all "query actions" of different kinds). Substantive home is `03-llm-core/` (language as a high-CIY channel) and the composition segments.
- **The epistemic-firewall consciousness-infrastructure reach (points at `04-eli-core/` / autopax).** If an ELI relies heavily on high-CIY/low-cost query actions, it becomes "incredibly vulnerable to Sybil attacks or deceptive poisoning — the channel that allows the fastest learning is also the vector for the fastest destabilization. Consciousness infrastructure must not just be a physical sandbox; it must be an epistemic firewall that strictly controls trust weights on external channels" (Gemini, AUDIT-WORKING-193847). The adversarial-mirror Lyapunov formalization (`#der-adversarial-destabilization`) is the in-framework substrate; the infrastructure implication points outward.
