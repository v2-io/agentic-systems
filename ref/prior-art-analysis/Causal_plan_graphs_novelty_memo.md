# Causal plan graphs novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Causal plan graphs novelty memo](#causal-plan-graphs-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The action-intervention claim must not sound like rediscovering Pearl](#the-action-intervention-claim-must-not-sound-like-rediscovering-pearl)
    - [The compact-edge representation has to be defended as a deliberate abstraction](#the-compact-edge-representation-has-to-be-defended-as-a-deliberate-abstraction)
    - [The depth-cost story should stay bundled and concrete](#the-depth-cost-story-should-stay-bundled-and-concrete)
    - [The dependence escalation should be framed as structural necessity, not optional refinement](#the-dependence-escalation-should-be-framed-as-structural-necessity-not-optional-refinement)
    - [The sequential-plan literature should be used carefully](#the-sequential-plan-literature-should-be-used-carefully)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [References](#references)

# Causal plan graphs novelty memo

## Overall judgment

The literature already contains strong ancestry for several major pieces of AAT’s causal-plan-graph story. Pearl’s action calculus and sequential-plan work make the action versus observation distinction explicit and treat plans as intervention sequences rather than associative forecasts \[Pea94b, Pea95, Pea95b\]. Decision-theoretic causality and influence-diagram work gives a parallel foundation for representing actions as causal nodes in DAG-like planning models \[Hec94, Hec95, Daw02, Daw10\]. Adaptive-control work and the Bayesian control rule sharpen the agent-internal version of the same idea: an agent’s own past actions in an input-output stream must be treated as interventions, not as ordinary evidence \[Ort08, Ort09\]. AND/OR planning and reliability lineages then provide strong ancestry for compact stepwise success or failure structures with single-parameter local uncertainty \[Bar83, Caz97, Gho21b, Fus72, Ves87\]. Finally, common-cause and dependent-failure modeling gives strong prior art for augmenting naive independent graphs when sibling branches share latent dependencies \[Fle78, Pap81, Vau02, Xin05\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-08:

- one internal planning formalism where an agent’s strategy is a causal DAG with probabilistic AND/OR structure and single-parameter edge credences
- the explicit claim that ordinary acting already generates Pearl Level-2 style evidence on the realized trajectory
- a bundled depth-cost story combining probabilistic fragility, evidence starvation, and maintenance burden for deep strategies
- a correlation-hierarchy doctrine in which latent common causes force structural augmentation of the plan graph rather than merely local parameter retuning

That package still looks promising. The raw ingredients are not new. The exact internal-agent synthesis may be.

## Claim under review

The project is not merely saying that plans can be represented graphically or that actions have effects.

The stronger claim is that an agent’s strategy should be modeled as a causal DAG whose edges carry compact success credences, and that the agent’s own action-perception loop continuously produces interventional evidence about that graph. Under that view, strategy learning is not just forecasting outcomes from trajectories. It is updating a causal plan model from interventions the agent itself performs.

AAT then adds two further claims.

First, deep hierarchical plans pay a triple cost:

- success probability decays across conjunctive depth
- downstream edges receive less evidence because they are tested only when upstream steps succeed
- the graph becomes more expensive to maintain and revise as depth grows

Second, independent-edge plan graphs are only a first rung. When siblings share a latent common cause, the plan graph is causally insufficient and must be augmented with higher-order dependence structure rather than treated as a merely miscalibrated independent DAG.

Read that way, AAT is making a stronger claim than “causal planning is useful.” It is proposing an internal causal model of strategy with compact local credences, interventional learning by ordinary acting, and principled escalation from independence to dependence-aware graph structure.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Actions must be distinguished from observations | \[Pea94b\], \[Pea95\], \[Ort08\], \[Ort09\] | Strong | Low novelty by itself |
| Sequential plans evaluated as intervention sequences under hidden variables | \[Pea95b\], \[Tia08\], \[Daw10\] | Strong | Low novelty by itself |
| Decision nodes as causal nodes in DAG-like planning models | \[Hec95\], \[Daw02\] | Strong | Low novelty by itself |
| Compact AND/OR plan structure with local failure probabilities | \[Bar83\], \[Caz97\], \[Gho21b\] | Strong | Moderate novelty only in AAT packaging |
| Depth fragility or compounded penalty in deep conjunctive structures | \[Caz97\], \[Gho21b\], \[Mes03\], \[Xin06\] | Partial to strong | Moderate novelty in the full bundled depth story |
| Common-cause augmentation beyond naive independent branches | \[Pap81\], \[Pag89\], \[Vau02\], \[Xin05\], \[Xin09\] | Strong | Low novelty by itself |
| Ordinary acting as a standing source of interventional evidence for an internal plan graph | \[Ort08\], \[Ort09\] come closest | Partial | High potential novelty |
| One unified internal planning object combining intervention semantics, compact edge credences, depth penalties, and correlation hierarchy | no direct single precursor found | Weak | Highest novelty candidate |

## What the prior art already establishes

The action-intervention lineage is very strong. \[Pea94b\] and \[Pea95\] make the distinction between observation and deliberate action explicit through the do-operator and local surgery viewpoint. \[Pea95b\] then applies that logic directly to sequential plans with hidden variables, asking when the effect of a plan can be identified from observational data and when it cannot. This is powerful prior art for the basic AAT stance that plans should be evaluated causally rather than associationally.

\[Ort08\] and \[Ort09\] are especially important because they move the same distinction inside the agent. Their core claim is not merely that actions have causal effects in the world. It is that an adaptive agent’s own past actions in an input-output stream must be treated as interventions rather than ordinary evidence. That is probably the strongest existing ancestor for AAT’s claim that ordinary acting itself generates interventional evidence for internal learning.

\[Hec95\] gives a complementary decision-theoretic foundation. It represents decisions as special nodes in influence-diagram style structures and derives causal reasoning from decision-theoretic primitives. This is excellent ancestry for the idea that internal planning graphs should include explicit action nodes whose semantics differ from ordinary chance nodes.

The compact-graph side also has good ancestry. \[Bar83\], \[Caz97\], and \[Gho21b\] all treat AND/OR structures with local task-level success or failure information rather than huge full conditional tables. \[Gho21b\] is particularly useful because it studies expected penalty in AND/OR graphs with task failure probabilities and rollback costs, showing that execution ordering matters and that optimal substructure can fail in these probabilistic settings. That is not the same object as AAT’s strategy DAG, but it is strong structural prior art for compact local-credence planning with fragility costs.

The hidden-dependence lineage is mature in reliability and risk analysis. \[Pap81\], \[Vau02\], \[Xin05\], and related work show that naive independent fault or success structures fail when components share common causes or other dependencies. This is exactly the right ancestry for AAT’s move from a naive independent plan graph to a correlation hierarchy with explicit common-cause augmentation.

The dynamic-plan-identification line strengthens the plan-level causal story. \[Tia08\] shows that dynamic sequential-plan identification can be reduced to identification of causal effects in causal Bayesian networks. \[Daw10\] gives a decision-theoretic account of dynamic treatment strategies and the conditions under which observational data can support intervention evaluation. These papers support the general claim that plan evaluation belongs in intervention theory, not just in empirical forecasting.

Taken together, the prior art already establishes five strong points:

- action and observation require different probabilistic syntax \[Pea94b, Ort08\]
- sequential plans should be evaluated as intervention sequences \[Pea95b, Tia08\]
- decisions can be represented as causal nodes in DAG-like models \[Hec95\]
- compact AND/OR structures with local failure parameters are already natural planning objects \[Gho21b\]
- latent shared causes can force augmentation of naive independent graphs \[Vau02, Xin05\]

What the literature does not seem to already provide is the exact AAT package that binds those into one internal strategy object and then uses ordinary acting as the standing mechanism for causal plan revision.

## Where AAT seems genuinely new

AAT looks strongest where it turns scattered lineages into one internal-agent planning formalism.

First, I do not see a single paper in the project that unifies intervention semantics, compact AND/OR local credences, depth penalties, and latent-dependence escalation inside one native strategy representation. Each piece has ancestry. The exact combination still looks open.

Second, the “ordinary acting yields interventional evidence” claim may be the main novelty center. \[Ort08\] and \[Ort09\] come very close, but they are framed as adaptive control and mixture-of-experts rules rather than as an internal plan-DAG validation story. AAT’s move is to treat everyday execution of a plan as the default intervention mechanism for learning the plan graph. That is sharper and more architecturally specific.

Third, the compact edge-credence story helps. Much of the causal-planning literature assumes richer structural models, while much of the planning literature does not foreground intervention semantics. AAT’s use of single-parameter edge credences in a causal DAG may therefore hit a sweet spot: rich enough for causal revision, simple enough for practical strategy maintenance.

Fourth, the bundled depth-cost story is stronger than any one ingredient. The field already knows about success decay and execution-order penalties \[Gho21b\], and AAT itself supplies evidence-starvation and maintenance-cost machinery elsewhere in the chapter. The likely novelty is the three-part package: deep plans are not just less likely to work, they are harder to calibrate and more expensive to sustain.

Fifth, the correlation-hierarchy move is a good candidate for real novelty in packaging. Reliability engineering already knows that common causes break independent branch models. But AAT’s likely distinctive claim is that this is not a niche repair for fault trees. It is a general escalatory rule for internal planning models: when sibling outcomes covary beyond the independent graph, move to a richer causal plan representation.

## Stress tests that matter most

### The action-intervention claim must not sound like rediscovering Pearl

The novelty is not that actions differ from observations. That is already deeply established. The novelty has to be the internal-agent reading: routine acting supplies the intervention stream for plan revision.

### The compact-edge representation has to be defended as a deliberate abstraction

A lot of prior art uses richer causal models. AAT should not imply that single-parameter edge credences are universally sufficient. The better claim is that they are a disciplined first-order compression of a strategy graph.

### The depth-cost story should stay bundled and concrete

If the memo says only that deep plans are fragile, it becomes ordinary. The stronger version is that deep plans degrade along three distinct axes: success, learnability, and maintenance.

### The dependence escalation should be framed as structural necessity, not optional refinement

This is where the reliability lineage helps most. The point is not merely that richer models are nicer. It is that independent-edge models can become causally insufficient when common causes are present.

### The sequential-plan literature should be used carefully

\[Pea95b\] and \[Tia08\] support plan-level intervention evaluation strongly, but they are not already compact internal strategy-DAG papers in the AAT sense. They are ancestry, not identity.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Planning theory | It would give a compact causal internal model of strategy rather than a pure search or forecast object | \[Pea95b\], \[Gho21b\] |
| Adaptive agents | It would make ordinary execution itself the source of interventional plan learning | \[Ort08\], \[Ort09\] |
| Safety and diagnosis | It would clarify when plan failures reflect local miscalibration versus hidden common causes | \[Vau02\], \[Xin05\] |
| Organization and operations | It would support causal decomposition of multi-step plans with explicit escalation when branch dependencies appear | planning and reliability lineages |

The biggest direct effect would likely be on how AAT understands strategy. Plans would stop being merely symbolic action recipes or expected-outcome forecasts and become causal objects that are revised from intervention data generated by the agent itself.

The second major effect would be on diagnosis. The correlation-hierarchy move gives the framework a principled answer to a common failure mode: when repeated plan failures cluster across sibling branches, the right update may be to add hidden common-cause structure rather than to keep down-weighting individual edges.

The third effect would be on practical planning under bounded cognition. The compact-edge representation plus the triple depth penalty offers a disciplined reason to prefer shallower, more observable strategies when possible.

## Bottom line

The weak version of this memo is not novel. The field already knows that actions must be treated differently from observations, that sequential plans are intervention objects, that compact AND/OR graphs can carry local failure parameters, and that common causes break naive independent branch models \[Pea94b, Pea95b, Hec95, Gho21b, Vau02\].

The strong version does look novel. AAT’s best claim is not that causal planning exists, but the stronger architectural thesis that an agent’s strategy can be modeled as a compact causal DAG whose ordinary execution already supplies interventional evidence for revision, whose deep structure pays a bundled fragility and learnability cost, and whose independent-branch form must escalate to richer dependence structure when latent common causes appear.

The cleanest sharpened read is:

- intervention semantics has strong prior art
- compact graph structure has strong prior art
- dependence augmentation has strong prior art
- the exact internal-agent synthesis still looks open

A strong one-line framing is this:

AAT’s novelty is not the observation that plans have causes, but the stronger claim that strategy itself is a compact causal graph learned from the interventions of ordinary acting, with principled escalation from independent edges to dependence-aware structure when the graph becomes causally insufficient.

## Potential field impact if the claim holds

The impact ceiling is high because this memo sits at the junction of causal reasoning, planning, and adaptive control.

At the modest end, the paper would still be valuable as a synthesis. It would connect Pearl-style intervention semantics, decision-theoretic causal planning, Bayesian adaptive control, AND/OR graph fragility, and reliability-style dependence modeling under one shared strategy object.

At the stronger end, it could give people a more realistic planning language for agentic systems. Rather than treating plans as fixed trees or policies as opaque black boxes, the paper would treat strategy as a revisable causal structure whose edges are tested by acting and whose hidden dependencies have to be discovered when local calibration fails.

The biggest direct effect would likely be on adaptive planning systems. The memo suggests a disciplined workflow: start with a compact independent graph, learn from interventions generated by ordinary action, monitor depth and evidence starvation, and escalate to richer dependence structure only when the data forces it.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis of causal planning and reliability lineages
- high impact if the “ordinary acting as intervention stream” idea is seen as a useful internal-agent principle
- very high impact if the compact causal-strategy-graph view becomes standard language for agent planning and diagnosis

## Venue strategy

### Best-fit venues by framing

If the paper is framed around causal intervention semantics, sequential-plan identification, and hidden-variable conditions, [UAI 2026](https://www.auai.org/uai2026/call_for_papers) is the cleanest specialist venue.

If the paper is framed as a broad AI-theory contribution about strategy representation, planning, and adaptive causal diagnosis, [Artificial Intelligence](https://www.sciencedirect.com/journal/artificial-intelligence) is probably the best long-form home.

If the paper is framed as a learning-and-control framework for revisable strategy graphs under intervention data, [Transactions on Machine Learning Research](https://www.jmlr.org/tmlr/editorial-policies.html) is also plausible.

### Recommended path

The cleanest publication strategy is:

1.  Write the full theory version for Artificial Intelligence.
2.  If the causal-plan-identification core becomes the sharpest technical contribution, prepare a tighter conference version for UAI.
3.  If the strongest pitch becomes adaptive learning from intervention traces in agent systems, consider TMLR.

### Practical ranking for this project

My venue ranking for this exact memo is:

- Artificial Intelligence
- UAI
- Transactions on Machine Learning Research

The fork is simple:

- if the main claim is “this is a broad theory of causal strategy representation,” favor Artificial Intelligence
- if the main claim is “this is a plan-identification and intervention-semantics result,” favor UAI
- if the main claim is “this is a new framework for adaptive learning of strategy graphs,” consider TMLR

## Submission snapshot

This venue advice is time-sensitive. The venue positioning above is a snapshot as of May 21, 2026.

---

## References

\[Pea94b\] J. Pearl, “A Probabilistic Calculus of Actions,” *ArXiv*, vol. abs/1302.6835, Jul. 1994, doi: [10.1016/B978-1-55860-332-5.50062-6](https://doi.org/10.1016/B978-1-55860-332-5.50062-6).

\[Pea95\] J. Pearl, “Action as a Local Surgery,” 1995.

\[Pea95b\] J. Pearl and J. Robins, “Probabilistic evaluation of sequential plans from causal models with hidden variables,” *Conference on Uncertainty in Artificial Intelligence*, pp. 444–453, Aug. 1995.

\[Hec94\] D. Heckerman and R. D. Shachter, “A Decision-based View of Causality,” *ArXiv*, vol. abs/1302.6816, Jul. 1994, doi: [10.1016/B978-1-55860-332-5.50043-2](https://doi.org/10.1016/B978-1-55860-332-5.50043-2).

\[Hec95\] D. Heckerman and R. D. Shachter, “Decision-Theoretic Foundations for Causal Reasoning,” *J. Artif. Intell. Res.*, vol. 3, pp. 405–430, Jun. 1995, doi: [10.1613/JAIR.202](https://doi.org/10.1613/JAIR.202).

\[Daw02\] A. Dawid, “Influence Diagrams for Causal Modelling and Inference,” Aug. 01, 2002. doi: [10.1111/j.1751-5823.2002.tb00354.x](https://doi.org/10.1111/j.1751-5823.2002.tb00354.x).

\[Daw10\] A. Dawid and V. Didelez, “Identifying the consequences of dynamic treatment strategies: A decision-theoretic overview,” *ArXiv*, vol. abs/1010.3425, Oct. 2010, doi: [10.1214/10-SS081](https://doi.org/10.1214/10-SS081).

\[Ort08\] P. A. Ortega and D. A. Braun, “A Minimum Relative Entropy Principle for Learning and Acting,” *ArXiv*, vol. abs/0810.3605, Oct. 2008, doi: [10.1613/JAIR.3062](https://doi.org/10.1613/JAIR.3062).

\[Ort09\] P. A. Ortega and D. A. Braun, “A Bayesian Rule for Adaptive Control based on Causal Interventions,” *ArXiv*, vol. abs/0911.5104, Nov. 2009, doi: [10.2991/AGI.2010.39](https://doi.org/10.2991/AGI.2010.39).

\[Bar83\] J. Barnett, “Optimal searches from and ornodes,” Aug. 08, 1983.

\[Caz97\] T. Cazenave and R. Moneret, “Development and Evaluation of Strategic Plans,” Oct. 01, 1997.

\[Gho21b\] P. Ghosh, P. Chakrabarti, and P. Dasgupta, “Execution Ordering in AND/OR Graphs with Failure Probabilities,” *Symposium on Combinatorial Search*, pp. 41–48, Aug. 2021, doi: [10.1609/socs.v3i1.18246](https://doi.org/10.1609/socs.v3i1.18246).

\[Fus72\] J. B. Fussell and W. Vesely, “NEW METHODOLOGY FOR OBTAINING CUT SETS FOR FAULT TREES.” 1972.

\[Ves87\] W. E. Vesely, F. Goldberg, N. Roberts, and D. Haasl, “Fault Tree Handbook,” Dec. 1987.

\[Fle78\] K. N. Fleming and P. Raabe, “Comparison of three methods for the quantitative analysis of common cause failures,” May 01, 1978.

\[Pap81\] I. Papazoglou and S. Mitra, “Effect of sympathetic failures on redundant system reliability,” 1981.

\[Vau02\] J. Vaurio, “Treatment of general dependencies in system fault-tree and risk analysis,” *IEEE Trans. Reliab.*, vol. 51, pp. 278–287, Nov. 2002, doi: [10.1109/TR.2002.801848](https://doi.org/10.1109/TR.2002.801848).

\[Xin05\] L. Xing, “RELIABILITY MODELING AND ANALYSIS OF COMPLEX HIERARCHICAL SYSTEMS,” Dec. 01, 2005. doi: [10.1142/S0218539305001963](https://doi.org/10.1142/S0218539305001963).

\[Tia08\] J. Tian, “Identifying Dynamic Sequential Plans,” *Conference on Uncertainty in Artificial Intelligence*, pp. 554–561, Jul. 2008.

\[Mes03\] L. Meshkat, “An overview of the phase-modular fault tree approach to phased mission system analysis,” Jul. 2003.

\[Xin06\] L. Xing, L. Meshkat, and S. Donahue, “An Efficient Approach for the Reliability Analysis of Phased-Mission Systems with Dependent Failures,” May 01, 2006. doi: [10.1115/1.802442.paper3](https://doi.org/10.1115/1.802442.paper3).

\[Pag89\] L. Page and J. Perry, “A model for system reliability with common-cause failures,” Oct. 01, 1989. doi: [10.1109/24.46447](https://doi.org/10.1109/24.46447).

\[Xin09\] L. Xing, A. Shrestha, L. Meshkat, and W. Wang, “Incorporating Common-Cause Failures Into the Modular Hierarchical Systems Analysis,” *IEEE Transactions on Reliability*, vol. 58, pp. 10–19, Feb. 2009, doi: [10.1109/TR.2008.2011855](https://doi.org/10.1109/TR.2008.2011855).
