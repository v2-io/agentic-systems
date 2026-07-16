# Layer 3 mechanism counterfactual separation

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Determine whether any scholarly work—published papers, preprints, theses, workshop papers, technical lecture notes, or well-circulated technical blog posts—already states or implies a query-level separation between Pearl’s Layer 3 counterfactual content and latent-anchored mechanism counterfactuals. The target result is the existence of finite recursive SCMs M_A and M_B that agree on the entire joint potential-outcome process, including nested and cross-world counterfactuals (M_A ≡*3 M_B), but assign different probabilities to a query involving replacement of one structural equation by an arbitrary function of its parents and the shared exogenous variables. The minimal motivating witness uses Y = X ⊕ U_Y versus Y = X ⊕ U_Y ⊕ 1, with replacement g(x,u_Y)=u_Y and query P(Y*{f_Y:=g}=Y\_{x=0}). Search for results stated in different vocabularies, including counterfactual indistinguishability, response-function or principal-stratification representations, latent reparameterization or coordinate dependence, and identifiability under mechanism or model changes. Rank first any work with an explicit separation theorem or counterexample, and also any adjacent result that logically implies such a separation even if it does not use this terminology. For each candidate, determine whether it genuinely provides disagreement on a query, rather than merely showing that structural functions are underdetermined or discussing mechanism change without a distinguishability result. A second, equivalent form of the target should be searched for independently: any result comparing an SCM against its own exogenous relabeling (a measure-automorphism image of the exogenous space), where Layer-3 equivalence holds automatically by construction, yet a mechanism replacement written as a fixed function table over the latent coordinates yields queries on which the model and its relabeled image disagree — we have derived that this disagreement is generic (it occurs for every SCM admitting a nontrivial exogenous automorphism on which some mechanism depends), so prior art may exist as a genericity or invariance-failure statement rather than as a two-model counterexample. Audit adjacent literatures for results that may imply or delimit the separation: soft, imperfect, parametric, shift-scale, stochastic, edge, mechanism, policy, and conditional-plan interventions; sigma-calculus; causal abstraction and exact transformations; structural-equation and interventionist causal logics; quantification over functions or interventions; and proposals for higher causal-hierarchy levels. Pay particular attention to whether the replacement is anchored to latent variables or instead uniformly specified in potential-outcome coordinates, since uniform PO-specifications are expected to be Layer-3-reducible while latent-anchored replacements may depend on the coordinatization of the exogenous space. Also look for treatments of Pearl’s interventions-as-variables construction or model enlargement that could be mistaken for an informational collapse, and assess whether the enlargement is itself determined by Layer-3 content. The final search assessment should separate exact prior art, logically implicating prior art, boundary/supporting results, and clean misses, while flagging venue and publication status. A paper should be promoted to the first-rank novelty set whenever its theorem or identifiability construction entails the same distinguishability claim, even if its framing is causal abstraction, soft-intervention identifiability, or causal logic rather than Pearl’s hierarchy.

*Found 9 papers · July 16, 2026 · Estimated coverage of relevant papers: 100%*

## Summary of Results

No retrieved work states the target separation: two finite recursive SCMs with identical full joint potential-outcome (Layer-3) process but different probabilities for a replacement intervention whose function is fixed over latent coordinates. The closest conceptual antecedents make the latent-coordinate issue visible, but do not supply the required distinguishability theorem or the XOR-style witness.

#### Nearest results

- Exogenous isomorphism is explicitly proposed as a criterion tied to complete Layer-3 identifiability in \[1\]. This is the most directly relevant vocabulary, yet the available description gives sufficient conditions for identifying models up to exogenous isomorphism—not a proof that a fixed latent-anchored replacement distinguishes isomorphic/relabelled models.
- Exogenous reparameterizations are formalized and said to preserve SCM causal semantics in \[2\]. This strongly supports the constructional premise that latent representations can be changed without altering ordinary causal/counterfactual semantics; it is not, from the retrieved record, a result about mechanism-replacement queries failing that invariance.
- Canonical/counterfactual representations separate a counterfactual random-process choice from interventional constraints \[3\], providing a useful response-function/PO coordinate perspective, but no mechanism-change separation is reported.

#### Boundary results and clean misses

- Standard Layer-3 work concerns cross-world counterfactuals under ordinary interventions \[7\] or logical languages for such queries \[5\], not substitution of an equation by a latent-indexed function table.
- PO–SCM comparison and abstraction results \[6, 8, 9\] clarify representability and framework mismatch, but do not establish disagreement on a shared replacement query.

Thus the retrieved landscape supports a sharp novelty claim: Layer-3 equivalence is treated as preserving counterfactual content, while the invariance failure of latent-anchored mechanism replacement—and especially its generic exogenous-automorphism form—does not appear as an explicit prior result. \[1\] and \[2\] warrant closest-prior-art review; both are arXiv preprints, whereas \[7\] is JMLR and \[5\] AAAI.

## Paper Catalog (9 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2025 | 2.5 | Exogenous Isomorphism for Counterfactual Identifiability ([link](https://doi.org/10.48550/arXiv.2505.02212)) | Yikang Chen and Dehui Du | ArXiv |
| 2 | 2016 | 1.1 | Structural Causal Models: Cycles, Marginalizations, Exogenous Reparametrizations and Reductions ([link](https://www.semanticscholar.org/paper/810b28e22adb665a1ffaf53b0696d9a8487efbb5)) | S. Bongers, J. Peters, B. Schölkopf, and J. Mooij | ArXiv |
| 3 | 2025 | 1.0 | Canonical Representations of Markovian Structural Causal Models: A Framework for Counterfactual Reasoning ([link](https://doi.org/10.48550/arXiv.2507.16370)) | Lucas de Lara | ArXiv |
| 4 | 2019 | 0.3 | Causal models on probability spaces ([link](https://www.semanticscholar.org/paper/dfe8e04fa594c9e2aeaecdc4ab92e8f6b207d186)) | Irineo Cabreros and John D. Storey | arXiv: Statistics Theory |
| 5 | 2020 | 5.7 | Probabilistic Reasoning across the Causal Hierarchy ([link](https://doi.org/10.1609/AAAI.V34I06.6577)) | D. Ibeling and Thomas F. Icard | AAAI Conference on Artificial Intelligence |
| 6 | 2023 | 7.8 | Comparing Causal Frameworks: Potential Outcomes, Structural Models, Graphs, and Abstractions ([link](https://doi.org/10.48550/arXiv.2306.14351)) | D. Ibeling and Thomas F. Icard | ArXiv |
| 7 | 2008 | 16 | Complete Identification Methods for the Causal Hierarchy ([link](https://doi.org/10.5555/1390681.1442797)) | I. Shpitser and J. Pearl | J. Mach. Learn. Res. |
| 8 | 2023 | 0.4 | A clarification on the links between potential outcomes and do-interventions ([link](https://doi.org/10.1515/jci-2024-0033)) | Lucas De Lara | Journal of Causal Inference |
| 9 | 2015 | 1.1 | A Distinction between Causal Effects in Structural and Rubin Causal Models ([link](https://doi.org/10.2139/SSRN.2587076)) | Dionissi Aliprantis |  |

### Paper Details

1\. · 100% match · 2025 · 2.5 cit/yr\
**Exogenous Isomorphism for Counterfactual Identifiability** ([link](https://doi.org/10.48550/arXiv.2505.02212))\
Yikang Chen and Dehui Du\
*ArXiv* · May 4, 2025 · 3 citations

> This paper investigates $`\sim_{\mathcal{L}_3}`$-identifiability, a form of complete counterfactual identifiability within the Pearl Causal Hierarchy (PCH) framework, ensuring that all Structural Causal Models (SCMs) satisfying the given assumptions provide consistent answers to all causal questions. To simplify this problem, we introduce exogenous isomorphism and propose $`\sim_{\mathrm{EI}}`$-identifiability, reflecting the strength of model identifiability required for $`\sim_{\mathcal{L}_3}`$-identifiability. We explore sufficient assumptions for achieving $`\sim_{\mathrm{EI}}`$-identifiability in two special classes of SCMs: Bijective SCMs (BSCMs), based on counterfactual transport, and Triangular Monotonic SCMs (TM-SCMs), which extend $`\sim_{\mathcal{L}_2}`$-identifiability. Our results unify and generalize existing theories, providing theoretical guarantees for practical applications. Finally, we leverage neural TM-SCMs to address the consistency problem in counterfactual reasoning, with experiments validating both the effectiveness of our method and the correctness of the theory.

------------------------------------------------------------------------

2\. · 100% match · 2016 · 1.1 cit/yr\
**Structural Causal Models: Cycles, Marginalizations, Exogenous Reparametrizations and Reductions** ([link](https://www.semanticscholar.org/paper/810b28e22adb665a1ffaf53b0696d9a8487efbb5))\
S. Bongers, J. Peters, B. Schölkopf, and J. Mooij\
*ArXiv* · Nov 18, 2016 · 11 citations

> Structural causal models (SCMs), also known as non-parametric structural equation models (NP-SEMs), are widely used for causal modeling purposes. In this paper, we give a rigorous treatment of structural causal models, dealing with measure-theoretic complications that arise in the presence of cyclic relations. The central question studied in this paper is: given a (possibly cyclic) SCM defined on a large system (consisting of observable endogenous and latent exogenous variables), can we “project it down” to an SCM that describes a subsystem (consisting of a subset of the observed endogenous variables and possibly different latent exogenous variables) in order to obtain a more parsimonious but equivalent representation of the subsystem? We define a marginalization operation that effectively removes a subset of the endogenous variables from the model, and a class of mappings, exogenous reparameterizations, that can be used to reduce the space of exogenous variables. We show that both operations preserve the causal semantics of the model and that under mild conditions they can lead to a significant reduction of the model complexity, at least in terms of the number of variables in the model. We argue that for the task of estimating an SCM from data, the existence of “smooth” reductions would be desirable. We provide several conditions under which the existence of such reductions can be shown, but also provide a counterexample that shows that such reductions do not exist in general. The latter result implies that existing approaches to estimate linear or Markovian SCMs from data cannot be extended to general SCMs.

------------------------------------------------------------------------

3\. · 92% match · 2025 · 1.0 cit/yr\
**Canonical Representations of Markovian Structural Causal Models: A Framework for Counterfactual Reasoning** ([link](https://doi.org/10.48550/arXiv.2507.16370))\
Lucas de Lara\
*ArXiv* · Jul 22, 2025 · 1 citations

> Counterfactual reasoning aims at answering contrary-to-fact questions like \`\`Would have Alice recovered had she taken aspirin?’’and corresponds to the most fine-grained layer of causation. Critically, while many counterfactual statements cannot be falsified-even by randomized experiments-they underpin fundamental concepts like individual-wise fairness. Therefore, providing models to formalize and implement counterfactual beliefs remains a fundamental scientific problem. In the Markovian setting of Pearl’s causal framework, we propose an alternative approach to structural causal models to represent counterfactuals compatible with a given causal graphical model. More precisely, we introduce counterfactual models, also called canonical representations of structural causal models. They enable analysts to choose a counterfactual assumption via random-process probability distributions with preassigned marginals and characterize the counterfactual equivalence class of structural causal models. Using these representations, we present a normalization procedure to disentangle the (arbitrary and unfalsifiable) counterfactual choice from the (typically testable) interventional constraints. In contrast to structural causal models, this allows to implement many counterfactual assumptions while preserving interventional knowledge, and does not require any estimation step at the individual-counterfactual layer: only to make a choice. Finally, we illustrate the specific role of counterfactuals in causality and the benefits of our approach on theoretical and numerical examples.

------------------------------------------------------------------------

4\. · 61% match · 2019 · 0.3 cit/yr\
**Causal models on probability spaces** ([link](https://www.semanticscholar.org/paper/dfe8e04fa594c9e2aeaecdc4ab92e8f6b207d186))\
Irineo Cabreros and John D. Storey\
*arXiv: Statistics Theory* · Jul 2, 2019 · 2 citations

> We describe the interface between measure theoretic probability and causal inference by constructing causal models on probability spaces within the potential outcomes framework. We find that measure theory provides a precise and instructive language for causality and that consideration of the probability spaces underlying causal models offers clarity into central concepts of causal inference. By closely studying simple, instructive examples, we demonstrate insights into causal effects, causal interactions, matching procedures, and randomization. Additionally, we introduce a simple technique for visualizing causal models on probability spaces that is useful both for generating examples and developing causal intuition. Finally, we provide an axiomatic framework for causality and make initial steps towards a formal theory of general causal models.

------------------------------------------------------------------------

5\. · 55% match · 2020 · 5.7 cit/yr\
**Probabilistic Reasoning across the Causal Hierarchy** ([link](https://doi.org/10.1609/AAAI.V34I06.6577))\
D. Ibeling and Thomas F. Icard\
*AAAI Conference on Artificial Intelligence* · Jan 9, 2020 · 37 citations

> We propose a formalization of the three-tier causal hierarchy of association, intervention, and counterfactuals as a series of probabilistic logical languages. Our languages are of strictly increasing expressivity, the first capable of expressing quantitative probabilistic reasoning—including conditional independence and Bayesian inference—the second encoding do-calculus reasoning for causal effects, and the third capturing a fully expressive do-calculus for arbitrary counterfactual queries. We give a corresponding series of finitary axiomatizations complete over both structural causal models and probabilistic programs, and show that satisfiability and validity for each language are decidable in polynomial space.

------------------------------------------------------------------------

6\. · 46% match · 2023 · 7.8 cit/yr\
**Comparing Causal Frameworks: Potential Outcomes, Structural Models, Graphs, and Abstractions** ([link](https://doi.org/10.48550/arXiv.2306.14351))\
D. Ibeling and Thomas F. Icard\
*ArXiv* · Jun 25, 2023 · 24 citations

> The aim of this paper is to make clear and precise the relationship between the Rubin causal model (RCM) and structural causal model (SCM) frameworks for causal inference. Adopting a neutral logical perspective, and drawing on previous work, we show what is required for an RCM to be representable by an SCM. A key result then shows that every RCM – including those that violate algebraic principles implied by the SCM framework – emerges as an abstraction of some representable RCM. Finally, we illustrate the power of this ameliorative perspective by pinpointing an important role for SCM principles in classic applications of RCMs; conversely, we offer a characterization of the algebraic constraints implied by a graph, helping to substantiate further comparisons between the two frameworks.

------------------------------------------------------------------------

7\. · 39% match · 2008 · 16 cit/yr\
**Complete Identification Methods for the Causal Hierarchy** ([link](https://doi.org/10.5555/1390681.1442797))\
I. Shpitser and J. Pearl\
*J. Mach. Learn. Res.* · Jun 1, 2008 · 283 citations

> We consider a hierarchy of queries about causal relationships in graphical models, where each level in the hierarchy requires more detailed information than the one below. The hierarchy consists of three levels: associative relationships, derived from a joint distribution over the observable variables; cause-effect relationships, derived from distributions resulting from external interventions; and counterfactuals, derived from distributions that span multiple “parallel worlds” and resulting from simultaneous, possibly conflicting observations and interventions. We completely characterize cases where a given causal query can be computed from information lower in the hierarchy, and provide algorithms that accomplish this computation. Specifically, we show when effects of interventions can be computed from observational studies, and when probabilities of counterfactuals can be computed from experimental studies. We also provide a graphical characterization of those queries which cannot be computed (by any method) from queries at a lower layer of the hierarchy.

------------------------------------------------------------------------

8\. · 34% match · 2023 · 0.4 cit/yr\
**A clarification on the links between potential outcomes and do-interventions** ([link](https://doi.org/10.1515/jci-2024-0033))\
Lucas De Lara\
*Journal of Causal Inference* · Sep 12, 2023 · 1 citations

> Abstract Most of the scientific literature on causal modeling considers the structural framework of Pearl and the potential-outcome framework of Rubin to be formally equivalent and therefore interchangeably uses do-interventions and the potential-outcome framework to define counterfactual outcomes. In this article, we agnostically superimpose a structural causal model and a Rubin causal model compatible with the same observations to specify the mathematical conditions under which counterfactual outcomes obtained via do-interventions and potential outcomes need to, do not need to, can, or cannot be equal (almost surely or in law). Our comparison builds upon the fact that such causal models do not have to produce the same counterfactual outcomes and highlights real-world problems where they generally cannot correspond under classical causal-inference assumptions. Then, we examine common claims and practices from the causality literature in the light of this comparison. In doing so, we aim at clarifying the links between the two causal frameworks and the interpretation of their respective counterfactuals.

------------------------------------------------------------------------

9\. · 22% match · 2015 · 1.1 cit/yr\
**A Distinction between Causal Effects in Structural and Rubin Causal Models** ([link](https://doi.org/10.2139/SSRN.2587076))\
Dionissi Aliprantis\
Mar 27, 2015 · 12 citations

> Structural Causal Models define causal effects in terms of a single Data Generating Process (DGP), and the Rubin Causal Model defines causal effects in terms of a model that can represent counterfactuals from many DGPs. Under these different definitions, notationally similar causal effects make distinct claims about the results of interventions to the system under investigation: Structural equations imply conditional independencies in the data that potential outcomes do not. One implication is that the DAG of a Rubin Causal Model is different from the DAG of a Structural Causal Model. Another is that Pearl’s do-calculus does not apply to potential outcomes and the Rubin Causal Model.
