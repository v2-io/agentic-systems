---
slug: directed-separation-under-composition
type: hypothesis
status: discussion-grade
depends:
  - directed-separation
  - multi-agent-scope
  - composition-closure
---

# Hypothesis: Directed Separation Under Composition

When individual agents satisfy directed separation ( #directed-separation), does the composite macro-agent also satisfy it? The answer depends on whether the composite's internal information routing — which observations reach which sub-agents — is itself goal-dependent. Two cases arise, corresponding to the first two classes in #directed-separation's architectural classification.

## Formal Expression

*[Hypothesis (directed-separation-under-composition, extending directed-separation to composites)]*

Consider $N$ agents $A_1, \ldots, A_N$, each satisfying directed separation individually: $M_{i,\tau^+} = f_M^{(i)}(M_{i,\tau^-}, e_{i,\tau})$ with no $G_t^{(i)}$ argument.

**The question.** Directed separation is about **processing**, not **selection** ( #directed-separation, scope condition). A single agent's goals affect which events it seeks (through $\pi$), but $f_M$ processes whatever event arrives without reference to $G_t$. At the composite level, the analogous question is: does the composite's internal information routing — which observations are distributed to which sub-agents — depend on the composite's goals $G_t^c$?

Note: the fact that sub-agents' goal-driven *actions* shape the environment, which other sub-agents then *observe*, is not a violation of directed separation. This is exactly the mechanism directed separation explicitly allows at the single-agent level: goals influence events through action, but processing of realized events is goal-blind. Agent $B$ observing environmental changes caused by $A$'s goal-driven behavior is $B$ processing a realized event — goal-blindly. The observations carry information about $A$'s goals, but that is a property of the event's content, not a failure of goal-blind processing.

### Case 1: Goal-blind routing

*[Hypothesis (Case 1)]*

If information routing between agents follows a fixed structure — org chart, communication protocol, defined interfaces — that does not depend on $G_t^c$, then:

- Each sub-agent processes observations goal-blindly (individual directed separation)
- The routing is goal-blind (by construction)
- Therefore $f_M^c$ is $G_t^c$-independent

Directed separation **survives** at the composite level. Examples: military command structures with doctrinal communication protocols, software teams with defined code-review processes, multi-agent AI systems with protocol-specified message passing.

### Case 2: Goal-dependent routing

*[Hypothesis (Case 2)]*

If the composite's communication structure depends on $G_t^c$ — different intelligence products shared depending on the mission, different information escalated depending on the objective — then the composite's effective observation function has a goal argument:

$$o_c = h^c(\Omega, a_{\text{micro}}, G_t^c, \xi)$$

Even if each sub-agent's $f_M^{(i)}$ processes $o_i$ goal-blindly, the **set of observations reaching each sub-agent** depends on $G_t^c$ through the routing function. Directed separation **fails** at the composite level. The composite is analogous to a Class 2 (merged) architecture: goal content shapes the information pathway, not through individual interpretation but through collective routing.

## Epistemic Status

*Discussion-grade.* Max attainable: conditional (when the supporting machinery is in place).

**Foundation caveats.** This segment's claims are limited by two pieces of under-specified machinery:

1. The concept of **"goal-dependent routing"** is used informally. What constitutes the composite's information routing function, and what it means formally for routing to "depend on $G_t^c$," requires a definition — specifying routing as a function from micro-observations and composite state to per-agent observations, with an explicit independence condition. Without this, the Case 1/2 distinction is intuitively clear but formally imprecise.

2. The **admissible coarse-graining** $\Lambda$ from #composition-closure has admissibility constraints ($\mathcal P_{\text{adm}}$, $\mathcal M_{\text{adm}}$) that are acknowledged as placeholders. Whether directed separation should be among the properties that $\mathcal M_{\text{adm}}$ requires is an open question that this segment's answer could inform — but until those constraints exist, claims about $A_c$ and $f_M^c$ are about a not-yet-fully-defined object.

The architectural classification (Class 1/2/3) that this segment extends is now part of #directed-separation's Formal Expression with a formal operationalization ($\kappa_{\text{processing}}$ as conditional mutual information). That foundation is robust qualitative.

The logic of each case is sound *given* a precise definition of routing. Case 1: goal-blind routing + goal-blind processing = goal-blind composite. Case 2: goal-dependent routing means the composite's observation function depends on $G_t^c$, regardless of individual processing. Both follow from directed separation's definition. The gap is in the formalization of "routing," not in the logic.

The claim that the architectural classification lifts to composition is **structurally motivated** by #composition-consistency (the theory must give consistent answers at every level of description). But this is an argument from theoretical coherence, not a derivation.

## Discussion

**What this is and what it isn't.** This segment provides a two-case taxonomy for directed separation under composition. It is NOT a derivation from first principles (the routing concept is too informal for that). It IS a useful classification that identifies which composites fall within Section III's scope (Case 1) and which require a coupled formulation (Case 2).

**Most composites of interest are Case 1.** Fixed communication structures are the norm in designed multi-agent systems: military doctrine specifies information flow regardless of the current mission; software development processes define code review, CI, and deployment pipelines independent of the feature being built; multi-agent AI protocols specify message formats and channels. Goal-dependent routing (Case 2) is rarer: crisis management (where communication structure changes with threat type), ad hoc teams assembled for specific objectives, and attention-based multi-agent architectures where query routing depends on the shared goal.

**Connection to logogenic agents.** LLM-based agents are individually Class 2 (goal-conditioned attention). Whether composites of LLM agents are Case 1 or Case 2 depends on whether the inter-agent communication protocol is fixed or goal-dependent. A multi-agent LLM system with fixed API contracts between agents is Case 1 at the composite level even though each agent is individually Class 2. The internal architecture of each agent and the composition architecture are separate questions.

**Adversarial implications.** Goal-dependent routing (Case 2) makes the composite's objective partially observable through its communication patterns. An adversary who can observe which information is being routed where can infer the composite's current goal. This creates a meta-strategic incentive for fixed routing: it preserves not just epistemic hygiene but operational security.

## Working Notes

- **Goal-information leakage is a separate phenomenon.** In any composite, sub-agents' goal-driven actions shape the environment, so observations carry statistical information about goals. This is real and may matter for adversarial dynamics, trust calibration, and OPSEC — but it is NOT a directed-separation issue. It's the normal action-environment coupling that directed separation explicitly allows. If this phenomenon deserves formalization (and it may — the mutual information $I(o_c; G_t^c \mid \Omega_t)$ is well-defined and operationally relevant), it should be its own segment about goal-information leakage, not a case within directed-separation analysis. An earlier draft of this segment conflated the two; this was caught by external review.
- **Formalizing routing.** The critical missing piece. A formal definition might specify: $R_t : \mathcal O_{\text{micro}} \to \prod_i \mathcal O_i$ as a routing function that distributes micro-observations to individual agents. The independence condition for Case 1: $R_t \perp G_t^c \mid \mathcal O_{\text{micro}}$. For Case 2: $R_t$ depends on $G_t^c$. This definition would need to handle both explicit communication (directed messages) and implicit communication (shared environment observations that are differentially accessible).
- **Partial goal-dependence.** Real composites may have mostly-fixed routing with occasional goal-dependent exceptions (a military unit that follows doctrinal comms but occasionally switches to crisis-specific channels). The error from treating such composites as Case 1 depends on the frequency and magnitude of the goal-dependent exceptions. A formal treatment would need to quantify this, possibly through a "routing independence fraction."
- **Testable prediction.** Organizations that restructure communication channels based on the current strategic objective should exhibit lower prediction accuracy at the organizational level (the shared model becomes goal-contaminated through routing, not just through environmental coupling). Compare prediction accuracy before and after mission-dependent communication restructuring.
