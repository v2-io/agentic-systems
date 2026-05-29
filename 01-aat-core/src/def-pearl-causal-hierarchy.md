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

This segment recapitulates Pearl's three-level hierarchy of causal reasoning (Pearl 2009, *Causality*, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022) as the vocabulary AAT will deploy throughout the rest of Part II and beyond. The framework is explicit that this is *imported* machinery, not an AAT contribution.

**Level 1 — Associational.** "What will I observe next, given what I've observed before?" Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #form-agent-model), including purely passive observers. Temporal ordering ( #post-causal-structure) constrains which associations are meaningful — later observations can depend on earlier ones, not vice versa.

**Level 2 — Interventional.** "What will I observe if I *do* this?" The $do(\cdot)$ operator marks the crucial distinction from Level 1: this is not "what observation tends to follow this action in the historical record" but "what will happen *because* I take this action now." Three conditions must hold: the agent's action temporally precedes the observation; the agent chose the action (it was not determined by the same causes that determine the observation); the environment's response carries information about the causal relationship. Level 2 is why the feedback loop is more powerful than passive observation: by acting and then observing consequences, the agent obtains information about *mechanisms*, not merely correlations. The binary action requirement of #scope-agency ensures at least Level 2 access is structurally available.

**Level 3 — Counterfactual.** "Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?" This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. The most demanding epistemic level; the basis for regret computation, strategic simulation, and learning from single observations.

The *strict-non-collapse theorem* (Bareinboim et al. 2022, Theorem 1) is load-bearing for the rest of Part II: Level-2 quantities cannot in general be computed from Level-1 data alone; Level-3 quantities cannot be computed from Level-2 alone. This is what forces Ch.2's central question: agents that need to *learn* their action consequences during operation require *Level-2 access*, which Level-1 data cannot supply ( #der-causal-hierarchy-requirement). AAT's *distinctive contribution* is not the hierarchy itself but its grounding in agent dynamics — the loop-as-Level-2-engine result ( #der-loop-interventional-access), the regime-indexed identification-strength framing, and the application throughout Part II's strategy-revision machinery.

A clarification is offered: the three levels describe epistemic access *the causal structure makes available* — not what any particular agent *uses*. A Kalman filter plus LQR has Level-2 access structurally present (its innovation signal is conditioned on prior action) but the separation principle guarantees estimation quality is invariant to control policy — so the system does not *exploit* the interventional structure. A PID controller has no deliberative capacity at all and operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

A domain note worth flagging: **software development is a uniquely rich domain for the hierarchy**. For code-internal counterfactuals with deterministic outcomes — "what would the test suite report under implementation X instead of Y, environment fixed?" — `git checkout` plus re-implementation plus test execution is *literal Level-3 realization with ground-truth verification*, not a proxy. The conditions are precise: deterministic outcome, cost-commensurate replay, content-addressed immutable history ( #obs-software-epistemic-properties). For counterfactuals crossing the agent-environment boundary, it is a strong executable proxy but not literal Level 3. This scoped Level-3 access is what makes software AAT's privileged calibration laboratory for causal reasoning.

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

AAT's *distinctive contribution* is not the hierarchy itself but its grounding: the loop-as-Level-2-engine result ( #der-loop-interventional-access), the regime-indexed identification-strength framing ( #scope-edge-update-causal-validity), and the application throughout Part II's strategy-revision machinery. The recapitulation here is in service of those moves, not a primary AAT result.

## Discussion

**Availability vs. exploitation.** The three levels describe epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within AAT's scope operate primarily at Level 1. A Kalman filter coupled with an LQR controller has Level 2 access structurally present (its innovation signal is conditioned on prior action), but the separation principle guarantees estimation quality is invariant to control policy — the system does not *exploit* the interventional structure. Only dual control (choosing actions partly for their informational value) exercises Level 2 access in this domain. Similarly, a PID controller has no deliberative capacity — it operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

**Forward-looking deliberation exercises Level 2, shading into Level 3.** Comparing candidate actions before choosing — "what will happen if I do X vs Y?" — primarily exercises Level 2 (iterated mental intervention). When the agent evaluates past choices to refine the comparison ("given what happened when I tried X last time, what would Y have produced?"), it exercises Level 3.

**The causal hierarchy theorem.** Bareinboim et al. (2022) prove that the three levels form a strict hierarchy: Level 2 knowledge cannot in general be computed from Level 1 data alone, and Level 3 cannot be computed from Level 2 alone. This is load-bearing for AAT's Part II: evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query, so agents that need to *learn* action consequences during operation require causal structure beyond predictive models ( #der-causal-hierarchy-requirement).

**Software as a uniquely rich domain for this hierarchy.** In most domains, Level 3 counterfactuals require model-based simulation with uncertain fidelity. Software development is the privileged exception *for a specific class*: for code-internal counterfactuals with deterministic outcomes — "what would the test suite report under implementation X instead of Y, environment fixed?" — `git checkout` plus re-implementation plus test execution is literal Level 3 realization with ground-truth verification, not a proxy. For counterfactuals crossing the agent–environment boundary (what feature sequence the team would have shipped, how the market would have responded) it is a strong executable proxy, not literal Level 3. The precise conditions — the ($\alpha$) deterministic-outcome / ($\beta$) cost-commensurate-replay / ($\gamma$) content-addressed-immutable conjunction, and why the resulting uniqueness is configurational rather than necessary (with named falsifiers) — are established in #obs-software-epistemic-properties (P2; `02-tst-core/`). This scoped Level-3 access is what makes software AAT's privileged calibration laboratory for causal reasoning.

**Domain instantiations of the three levels:**

| Domain | Level 1 (Association) | Level 2 (Intervention) | Level 3 (Counterfactual) |
|--------|----------------------|----------------------|------------------------|
| Kalman filter | Prediction from state estimate | Innovation conditioned on action | Not typically exercised |
| RL agent | Value function prediction | Action → reward observation | Regret computation |
| Scientific method | Correlational observation | Experimental intervention | "What if we had used control X?" |
| Military (Boyd) | Pattern recognition | Probe/feint → observe response | "What if we had attacked from the flank?" |
| Software developer | "I think this function does X" | Run test → observe result | `git checkout` + alt. impl. — literal for code-internal deterministic counterfactuals; proxy across the agent–environment boundary ( #obs-software-epistemic-properties) |
| Immune system | Antigen pattern matching | Antibody → pathogen response | Not exercised (no counterfactual reasoning) |

## Working Notes

- This segment is positioned in Part II Ch.2 ("Causal Access and the Planning Decision") as of the 2026-05-12 relocation. It previously lived in Part I Ch.1 alongside AAT's own ontological commitments, which mis-framed it as foundational AAT machinery rather than as an imported framework recapitulated for AAT's purposes. The relocation places it at the head of the chapter that deploys it operationally.
- Part I segments that previously depended on this segment in their `depends:` frontmatter (`def-causal-information-yield`) now reference Pearl 2009 / Bareinboim 2022 via external citation with a forward pointer to this recapitulation. TST segments do the same. The relocation thus introduces no dangling dependencies; what changes is the rhetorical posture (imported framework, lightly cited where mentioned, recapitulated where deployed) and the OUTLINE position (Part II Ch.2 rather than Part I Ch.1).
