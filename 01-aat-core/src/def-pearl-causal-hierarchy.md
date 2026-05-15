---
slug: def-pearl-causal-hierarchy
type: definition
status: axiomatic
depends:
  - post-causal-structure
  - scope-agency
stage: deps-verified
---

# Definition: Pearl's Causal Hierarchy (Recapitulation)

AAT adopts Pearl's three-level hierarchy of causal reasoning — association, intervention, counterfactual — as the vocabulary for distinguishing kinds of epistemic access within the feedback loop. This segment recapitulates the hierarchy at the level of detail AAT's derivations deploy, with the canonical sources (Pearl 2009, *Causality*, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022, in *Probabilistic and Causal Inference: The Works of Judea Pearl*) carrying the underlying theory. The binary action requirement of #scope-agency ensures at least Level 2 access is structurally available; the chapter that follows is what deploys the hierarchy as operational machinery.

## Formal Expression

*[Definition (pearl-causal-hierarchy, recapitulating Pearl 2009 and Bareinboim et al. 2022)]*

**Level 1 — Associational**: $P(o_t \mid \mathcal{C}_{\lt t})$

*What will I observe next, given what I've observed before?*

Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #form-agent-model), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires: (1) the agent's action temporally precedes the observation ( #post-causal-structure), (2) the agent chose the action (it was not determined by the same causes that determine the observation), (3) the environment's response carries information about the causal relationship.

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t$ ( #def-mismatch-signal), conditioned on the agent's own action, is an *interventional* signal.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for regret computation, strategic simulation, and learning from single observations.

## Epistemic Status

*Recapitulation of an external result.* The three-level hierarchy and the strict-non-collapse theorem (Bareinboim, Correa, Ibeling & Icard 2022, Theorem 1: Level-2 quantities cannot in general be computed from Level-1 data alone; Level-3 quantities cannot in general be computed from Level-2 alone) are well-established results in causal-inference theory. They live within AAT's segment set because subsequent derivations deploy them as machinery: #der-causal-hierarchy-requirement applies the non-collapse theorem to the value-object's $do(\cdot)$ query and concludes that purposeful agents who must *learn* their action consequences need Level-2 access; #der-loop-interventional-access shows that the feedback loop is itself a Level-2 data engine; the no-go in #der-causal-insufficiency-detection, the strategy-DAG-as-causal-DAG framing in #def-strategy-dag, and the causal-information appendices ( #deriv-causal-ib-exploration, #deriv-causal-ib-lmi) all operate on the hierarchy. Where Part I segments and TST segments only need to *reference* the hierarchy (cite its existence and the do-operator notation) rather than deploy it, external citation to Pearl 2009 / Bareinboim et al. 2022 suffices; the AAT recapitulation here is what those external citations point to when the reader wants the in-framework vocabulary.

AAT's *distinctive contribution* is not the hierarchy itself but its grounding: the loop-as-Level-2-engine result ( #der-loop-interventional-access), the regime-indexed identification-strength framing ( #scope-edge-update-causal-validity), and the application throughout Section II's strategy-revision machinery. The recapitulation here is in service of those moves, not a primary AAT result.

## Discussion

**Availability vs. exploitation.** The three levels describe epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within AAT's scope operate primarily at Level 1. A Kalman filter coupled with an LQR controller has Level 2 access structurally present (its innovation signal is conditioned on prior action), but the separation principle guarantees estimation quality is invariant to control policy — the system does not *exploit* the interventional structure. Only dual control (choosing actions partly for their informational value) exercises Level 2 access in this domain. Similarly, a PID controller has no deliberative capacity — it operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

**Forward-looking deliberation exercises Level 2, shading into Level 3.** Comparing candidate actions before choosing — "what will happen if I do X vs Y?" — primarily exercises Level 2 (iterated mental intervention). When the agent evaluates past choices to refine the comparison ("given what happened when I tried X last time, what would Y have produced?"), it exercises Level 3.

**The causal hierarchy theorem.** Bareinboim et al. (2022) prove that the three levels form a strict hierarchy: Level 2 knowledge cannot in general be computed from Level 1 data alone, and Level 3 cannot be computed from Level 2 alone. This is load-bearing for AAT's Section II: evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query, so agents that need to *learn* action consequences during operation require causal structure beyond predictive models ( #der-causal-hierarchy-requirement).

**Software as a uniquely rich domain for this hierarchy.** In most domains, Level 3 counterfactuals require model-based simulation with uncertain fidelity. In software development, `git checkout` provides Level 3 access with ground-truth verification — the agent can literally execute the counterfactual. This is one of software's unique epistemic properties ( #obs-software-epistemic-properties — cross-component reference, see `02-tst-core/`) and makes it an ideal testbed for causal reasoning within AAT.

**Domain instantiations of the three levels:**

| Domain | Level 1 (Association) | Level 2 (Intervention) | Level 3 (Counterfactual) |
|--------|----------------------|----------------------|------------------------|
| Kalman filter | Prediction from state estimate | Innovation conditioned on action | Not typically exercised |
| RL agent | Value function prediction | Action → reward observation | Regret computation |
| Scientific method | Correlational observation | Experimental intervention | "What if we had used control X?" |
| Military (Boyd) | Pattern recognition | Probe/feint → observe response | "What if we had attacked from the flank?" |
| Software developer | "I think this function does X" | Run test → observe result | `git checkout` + alternative implementation |
| Immune system | Antigen pattern matching | Antibody → pathogen response | Not exercised (no counterfactual reasoning) |

## Working Notes

- This segment is positioned in Part II Ch.2 ("Causal Access and the Planning Decision") as of the 2026-05-12 relocation. It previously lived in Part I Ch.1 alongside AAT's own ontological commitments, which mis-framed it as foundational AAT machinery rather than as an imported framework recapitulated for AAT's purposes. The relocation places it at the head of the chapter that deploys it operationally.
- Part I segments that previously depended on this segment in their `depends:` frontmatter (`def-causal-information-yield`) now reference Pearl 2009 / Bareinboim 2022 via external citation with a forward pointer to this recapitulation. TST segments do the same. The relocation thus introduces no dangling dependencies; what changes is the rhetorical posture (imported framework, lightly cited where mentioned, recapitulated where deployed) and the OUTLINE position (Part II Ch.2 rather than Part I Ch.1).
