---
slug: hyp-directed-separation-under-composition
type: hypothesis
status: conditional
depends:
  - der-directed-separation
  - scope-multi-agent
  - form-composition-closure
stage: draft
---

# Hypothesis: Directed Separation Under Composition

The question whether the composite-level directed-separation condition holds: if every sub-agent satisfies #der-directed-separation individually, does the composite macro-agent also satisfy it? The answer is *conditional on the composite's routing structure* ( #scope-multi-agent).

The framework draws a careful distinction first. Sub-agents' goal-driven actions shape the environment, which other sub-agents observe. This is **not** a violation of directed separation — it is the same mechanism the single-agent result explicitly allows: goals influence *events* through action, but processing of realized events is goal-blind. Agent $B$ observing environmental changes caused by Agent $A$'s goal-driven behavior is $B$ processing a realized event goal-blindly. The observations carry information about $A$'s goals, but that is a property of the event's content, not a failure of goal-blind processing. Similarly, individual messages reflecting individual goals is action through policy, not a routing-structure dependence on the composite's goals.

The substantive question is whether the **routing structure** depends on the composite's goal. Two cases. **Case 1 — goal-blind routing**: when neither communication topology nor protocol depends on the composite's goals (military command structures with doctrinal communication protocols; software teams with defined code-review processes; multi-agent AI systems with protocol-specified message passing), directed separation *survives* at the composite level. **Case 2 — goal-dependent routing**: when the topology changes based on objective (different reporting chains activated depending on mission) or the protocol changes (different intelligence products shared depending on objective), the composite's effective observation function acquires a goal argument. Even if each sub-agent processes its observations goal-blindly, *the set of observations reaching each sub-agent depends on the composite's goal through the routing function*. Directed separation *fails* at the composite level.

This refinement establishes that **composite-level class membership depends on routing structure, not just sub-agent class**. A composite of Class-1-(Separated) sub-agents with goal-blind routing remains Class 1 at the composite level. A composite of Class-1-(Separated) sub-agents with goal-*dependent* routing becomes effectively Class 3 (Coupled) at the composite level — and the coupled-formulation machinery applies at the macro level even though every sub-agent individually satisfies directed separation. The architectural classification is therefore *not preserved under composition with goal-dependent routing*. For the special case of a single-component composite (wrapper-around-component), #der-class-coercion-via-wrapping promotes the equivalent result from hypothesis to derived; the general $N$-agent case treated here remains a hypothesis.

## Formal Expression

*[Hypothesis (directed-separation-under-composition, extending directed-separation to composites)]*

Consider $N$ agents $A_1, \ldots, A_N$, each satisfying directed separation individually: $M_{i,\tau^+} = f_M^{(i)}(M_{i,\tau^-}, e_{i,\tau})$ with no $G_t^{(i)}$ argument.

**The question.** Directed separation is about **processing**, not **selection** ( #der-directed-separation, scope condition). A single agent's goals affect which events it seeks (through $\pi$), but $f_M$ processes whatever event arrives without reference to $G_t$. At the composite level, the analogous question is: does the composite's routing structure $R_t$ ( #scope-multi-agent) depend on the composite's goals $G_t^c$?

Note: sub-agents' goal-driven actions shape the environment, which other sub-agents observe. This is NOT a violation of directed separation — it is the same mechanism directed separation explicitly allows at the single-agent level: goals influence events through action, but processing of realized events is goal-blind. Agent $B$ observing environmental changes caused by $A$'s goal-driven behavior is $B$ processing a realized event goal-blindly. The observations carry information about $A$'s goals, but that is a property of the event's content, not a failure of goal-blind processing. Similarly, individual messages reflecting individual agents' goals is action through policy, not a routing-structure dependence on $G_t^c$.

### Case 1: Goal-blind routing

*[Hypothesis (Case 1)]*

If the routing structure satisfies $R_t \perp G_t^c$ ( #scope-multi-agent, goal-blind routing) — neither the communication topology $\mathcal{N}_t$ nor the protocol $c_t^{(j \to i)}$ depends on the composite's goals — then:

- Each sub-agent processes observations goal-blindly (individual directed separation)
- The routing is goal-blind (by construction)
- Therefore $f_M^c$ is $G_t^c$-independent

Directed separation **survives** at the composite level. Examples: military command structures with doctrinal communication protocols, software teams with defined code-review processes, multi-agent AI systems with protocol-specified message passing.

### Case 2: Goal-dependent routing

*[Hypothesis (Case 2)]*

If $R_t$ depends on $G_t^c$ — either the topology $\mathcal{N}_t$ changes (different reporting chains activated depending on the mission) or the protocol $c_t^{(j \to i)}$ changes (different intelligence products shared depending on the objective) — then the composite's effective observation function has a goal argument:

$$o_c = h^c(\Omega, a_{\text{micro}}, G_t^c, \xi)$$

Even if each sub-agent's $f_M^{(i)}$ processes $o_i$ goal-blindly, the **set of observations reaching each sub-agent** depends on $G_t^c$ through the routing function. Directed separation **fails** at the composite level. The composite is analogous to a Class 3 (Coupled) architecture: goal content shapes the information pathway, not through individual interpretation but through collective routing.

## Epistemic Status

*Conditional* on the routing structure of the composite. Max attainable: conditional (the two cases are genuine architectural alternatives). Previously discussion-grade; upgraded after routing formalization in #scope-multi-agent and architectural classification promotion in #der-directed-separation (2026-04-01).

**Foundation status.**

1. The **architectural classification** (Class 1/2/3) is in #der-directed-separation's Formal Expression with formal operationalization ($\kappa_{\text{processing}}$). Status: robust qualitative.
2. The **routing structure** $R_t$ is defined in #scope-multi-agent with a formal goal-independence condition ($R_t \perp G_t^c$). The definition decomposes into topology independence and protocol independence. Whether this captures all relevant ways that composite information flow can depend on goals is an open question.
3. The **admissible coarse-graining** $\Lambda$ from #form-composition-closure now has specified admissibility constraints: (A1)-(A4) for macro-dynamics and (P1)-(P3) for projections. The remaining gaps are validation (exercising the machinery on a purposeful multi-agent example) and computability (P1 requires conditional mutual information, tractable only for linear-Gaussian), not missing definitions.

The logic of each case is sound given the routing definition. Case 1: goal-blind routing + goal-blind processing = goal-blind composite. Case 2: goal-dependent routing means the composite's observation function depends on $G_t^c$, regardless of individual processing. Both follow from directed separation's scope condition.

The claim that the architectural classification lifts to composition is **structurally motivated** by #disc-composition-consistency (the theory must give consistent answers at every level of description). This is an argument from theoretical coherence, not a derivation.

## Discussion

**What this is and what it isn't.** This segment provides a two-case taxonomy for directed separation under composition. It is not yet a derivation — the remaining caveat (admissibility placeholders) prevents that. It IS a useful classification that identifies which composites fall within Part III's scope (Case 1) and which require a coupled formulation (Case 2).

**Constructive special case: wrapper-around-component.** For the special case of a single-component composite — one underlying primitive component embedded inside an external scaffold — the question of when directed separation holds is *derived* by `#der-class-coercion-via-wrapping`. Under explicit conditions on the component (admissibility of goal-blind queries, stationary conditional, no implicit goal-inference) and on the wrapper's update maps (type signatures that exclude $G_W$ from the belief-update path), directed separation holds at the wrapper level by structural commitment. The construction promotes the wrapper-around-component case from hypothesis to derived; the general $N$-agent composition case (Case 1 vs. Case 2 above) remains a hypothesis pending further work.

**Most composites of interest are Case 1.** Fixed communication structures are the norm in designed multi-agent systems: military doctrine specifies information flow regardless of the current mission; software development processes define code review, CI, and deployment pipelines independent of the feature being built; multi-agent AI protocols specify message formats and channels. Goal-dependent routing (Case 2) is rarer: crisis management (where communication structure changes with threat type), ad hoc teams assembled for specific objectives, and attention-based multi-agent architectures where query routing depends on the shared goal.

**Connection to logogenic agents.** LLM-based agents are individually Class 3 (Coupled; goal-conditioned attention). Whether composites of LLM agents are Case 1 or Case 2 depends on whether the inter-agent communication protocol is fixed or goal-dependent. A multi-agent LLM system with fixed API contracts between agents is Case 1 at the composite level even though each agent is individually Class 3 (Coupled). The internal architecture of each agent and the composition architecture are separate questions.

**Adversarial implications.** Goal-dependent routing (Case 2) makes the composite's objective partially observable through its communication patterns. An adversary who can observe which information is being routed where can infer the composite's current goal. This creates a meta-strategic incentive for fixed routing: it preserves not just epistemic hygiene but operational security.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Goal-information leakage is a separate phenomenon.** In any composite, sub-agents' goal-driven actions shape the environment, so observations carry statistical information about goals. This is real and may matter for adversarial dynamics, trust calibration, and OPSEC — but it is NOT a directed-separation issue. It's the normal action-environment coupling that directed separation explicitly allows. If this phenomenon deserves formalization (and it may — the mutual information $I(o_c; G_t^c \mid \Omega_t)$ is well-defined and operationally relevant), it should be its own segment about goal-information leakage, not a case within directed-separation analysis. An earlier draft of this segment conflated the two; this was caught by external review.
- **Partial goal-dependence.** Real composites may have mostly-fixed routing with occasional goal-dependent exceptions (a military unit that follows doctrinal comms but occasionally switches to crisis-specific channels). The error from treating such composites as Case 1 depends on the frequency and magnitude of the goal-dependent exceptions. A formal treatment would need to quantify this, possibly through a "routing independence fraction."
- **Testable prediction.** Organizations that restructure communication channels based on the current strategic objective should exhibit lower prediction accuracy at the organizational level (the shared model becomes goal-contaminated through routing, not just through environmental coupling). Compare prediction accuracy before and after mission-dependent communication restructuring.

- **Composite-class-inheritance table (canonical home: `#der-directed-separation`; added 2026-05-21 per Phase 5 cross-segment ripple).** This hypothesis segment's Case 1 / Case 2 dichotomy was the original framing for composite-level class lift. The 2026-05-21 strategic-composition cycle (`spikes/strategic-composition-class-3-attempt-2026-05-21/`) extended the analysis along a third axis (substrate sharing with $G^c$-allocation, per `01-STRENGTHEN-ATTEMPTS.md` §5 (R4)) and produced the *axis-decomposed composite-class-inheritance table* now living in `#der-directed-separation` §"Composite-level class inheritance." That table is the consolidated home for the sub-agent-class × routing × substrate → composite-class lookup; this segment's Case 1 / Case 2 dichotomy remains the underlying hypothesis (still hypothesis-grade — the $N$-agent general case is not derived; the wrapper-around-component special case is derived in `#der-class-coercion-via-wrapping`). The dynamic-regime axis (`#disc-dynamic-regime-axis`) — goal alignment vs strategic interaction — is *independent* of the routing-structure axis this segment treats, and a clean separation: alignment work moves composites along the regime axis; routing-structure work moves them along the architectural-class axis.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings (handled elsewhere — the F122–F126 cluster, esp. the Case-1-needs-goal-blind-projection-too point, is routed to the findings track; see report flags). **Coverage:** two dirs reached a digested reflection (526815, 849201). Lower note-count, but high felt-value on the OPSEC and LLM-composite-inversion observations. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The Case 1 / Case 2 line stated plainly as an infrastructure test: a composite stays Class 1 (Separated) when "the infrastructure doesn't change based on the goal" ($R_t \perp G_t^c$) and each sub-agent's $f_M$ is goal-blind; it slides to Class 2 when "the infrastructure shifts based on the goal (e.g., activating crisis channels), [so] the composite's observation function becomes goal-dependent" (Claude, AUDIT-WORKING-849201). A compact Brief gloss of the dichotomy.

#### 2. Candidate Discussion

- **Goal-dependent routing is an OPSEC vulnerability — derived from the structure.** The standout insight: when routing depends on the composite goal, "adversaries can infer the goal just by watching the routing topology" — so Case-2 routing is not only an epistemic-hygiene failure but a security leak, "a brilliant practical insight derived directly from the theoretical structure" (Claude, AUDIT-WORKING-849201). A candidate Discussion addition turning the routing distinction into an operational consequence (and it resonates with the consciousness-infrastructure goal-blind-routing imperative lifted into #scope-multi-agent).
- **The LLM-composite inversion.** "While individual LLMs are Class 2/3, a multi-LLM system with fixed API contracts might be Case 1 at the macro level" — a "fascinating inversion of expectations" where composition *recovers* separation that the components individually lack (Claude, AUDIT-WORKING-849201). The segment treats this; the framing is a candidate reader-orienting Discussion line. *(Correctness caveat flagged in the report: F124 notes this belongs under the wrapper-derived special case #der-class-coercion-via-wrapping, since the general Case-1 setup assumes each sub-agent is individually separated — keep the tier/scope honest if promoted.)*

#### 3. Follow-up items

- **Case 1 needs goal-blind *projection*, not just goal-blind sub-agents + routing.** A real structural sharpening (routed as a finding, noted here for completeness): the Case-1 conclusion also requires the macro projection / coarse-graining and macro-update interface to be goal-blind — a goal-conditioned $\Lambda$, aggregation window, or macro-observation definition can reintroduce coupling even when sub-agent processing and routing are clean. The proposed sharper theorem shape: "goal-blind sub-agent processing, goal-blind routing, *and* goal-blind projection/update together preserve composite-level directed separation" (Codex/Claude, AUDIT-WORKING-526815, F122). This is a strengthen-the-hypothesis candidate, not framing gold — see report off-ramp flag.

#### 4. Readers often ask / wonder

- **"Isn't a sub-agent inferring another's goal from its actions already a separation failure?"** No — and the segment's existing "goal-information leakage" Working Note resolves exactly this trap: inferring goals from observed actions is normal, valid Bayesian inference (the action-environment coupling directed separation explicitly allows), distinct from a *structural* flaw in the processing pipeline. A fresh reader independently flagged this distinction as "resolving a major conceptual trap" (Claude, AUDIT-WORKING-849201). Strong signal the distinction is a natural reader stumble worth keeping prominent.

#### Belongs elsewhere

- *(No distinct belongs-elsewhere gold beyond the cross-links already noted — the OPSEC and goal-blind-routing-imperative material co-locates naturally with #scope-multi-agent and the consciousness-infrastructure reach lifted there.)*
