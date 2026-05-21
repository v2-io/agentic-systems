# Credit assignment boundary novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Credit assignment boundary novelty memo](#credit-assignment-boundary-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The three barriers must stay genuinely distinct](#the-three-barriers-must-stay-genuinely-distinct)
    - [The persistence claim needs to stay at the right level](#the-persistence-claim-needs-to-stay-at-the-right-level)
    - [The decomposability analogy must not be overstated](#the-decomposability-analogy-must-not-be-overstated)
    - [The OKR move must be stated as observability engineering, not management rhetoric](#the-okr-move-must-be-stated-as-observability-engineering-not-management-rhetoric)
    - [The correlation barrier should not overclaim impossibility](#the-correlation-barrier-should-not-overclaim-impossibility)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [References](#references)

# Credit assignment boundary novelty memo

## Overall judgment

The literature already contains strong ancestry for most of the negative side of AAT’s claim. Exact causal responsibility and blame are computationally hard in general structural models \[Eit01, Ale14, Cho03\]. Shapley-style compositional attribution is tractable only on special deterministic and decomposable structures, and becomes hard again when those properties fail \[Are20, Kar23i\]. Hidden-variable causal inference shows that many fine-grained causal queries are not point-identifiable from observables alone, leaving only bounds or partial identification \[Bal94, Shp06b, Shp08\]. Bayesian-network sensitivity work shows that useful plan-level query guarantees can transfer from parameter perturbations without solving exact local attribution \[Cha01c, Cha04\]. Diagnosability and sensor-placement work then gives a strong formal lineage for the idea that observability can be designed into a system rather than merely suffered as a limitation \[Tra01, Yas08\]. Economics and contract theory add a parallel observability lineage: better signals improve implementability and attribution quality \[Hol79, Hol91\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-08:

- a three-barrier boundary for strategy-DAG credit assignment combining computational hardness, information-theoretic underdetermination, and posterior-correlation loss
- a sharp claim that exact edge-level attribution is not required for persistence-style plan guarantees
- a default design requirement of directional fidelity rather than exact unbiased attribution
- a translation of observability design into organizational terms, where OKR-like intermediate nodes function as tractability-enabling instrumentation

That package looks strong. The pieces are not new. The boundary synthesis still may be.

## Claim under review

The project is not merely saying that credit assignment is hard.

The stronger claim is that edge-level credit assignment in a strategy DAG has a principled boundary with three distinct failure modes:

- exact attribution is computationally intractable in general compositional graphs
- when intermediate nodes are hidden, some attribution directions are not identifiable from the available data at all
- even when approximate inference is possible, any factorized edgewise posterior throws away correlation structure created by multi-parent nodes

AAT then adds a second, more original-looking claim: exact attribution is not actually required for the main persistence result. What matters is that the update signal has directional fidelity, so that plan-level error remains controlled even if local blame is approximate. On top of that, the framework treats observability as a design variable. Insert the right intermediate observables and a formerly intractable or underdetermined attribution problem can become componentwise and manageable.

Read that way, AAT is making a stronger claim than “credit assignment is difficult in DAGs.” It is proposing a full boundary theory plus a design doctrine for how to live on the tractable side of that boundary.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Exact causal or compositional attribution is hard in general | \[Eit01\], \[Ale14\], \[Cho03\], \[Val79\], \[Pro83\] | Strong | Low novelty by itself |
| Tractable islands exist on decomposable structures | \[Eit02b\], \[Are20\], \[Kar23i\] | Strong | Low novelty by itself |
| Hidden intermediates create non-identifiability or only bounds | \[Bal94\], \[Shp06b\], \[Shp08\], \[Pea95b\] | Strong | Low novelty by itself |
| Correlation structure defeats naive factorized edgewise attribution | \[Zha94\], \[Ric12b\], \[Shp14b\] | Partial to strong | Moderate novelty in this exact packaging |
| Plan-level guarantees can transfer without exact local attribution | \[Cha01c\], \[Cha04\], \[Mac19\] | Partial | Moderate to high novelty |
| Observability can be designed to improve isolability or implementation quality | \[Yas08\], \[Tra01\], \[Hol79\], \[Hol91\] | Strong | Moderate novelty only in AAT packaging |
| OKRs as observability-by-design for deep strategy graphs | distributed ancestry only | Weak | High potential novelty |
| One unified three-barrier boundary for strategy-DAG credit assignment | no direct single precursor found | Weak | Highest novelty candidate |

## What the prior art already establishes

The computational-hardness lineage is strong. \[Cho03\] and \[Ale14\] show that exact causal responsibility and blame in structural models are expensive to compute, even before moving to rich edgewise plan attributions. These papers are not about AAT strategy DAGs specifically, but they are close in spirit because they formalize contribution assignment inside causal structures rather than in simple independent models. Their message is already close to AAT’s first barrier: exact local causal credit is not cheap in general.

The Boolean-circuit and Shapley line sharpens the tractability side. \[Are20\] is especially useful because it proves a clean boundary: attribution is polynomial on deterministic and decomposable circuits, and becomes hard when either structural property is removed. \[Kar23i\] reinforces the same lesson by tying Shapley computation to model counting. This gives AAT a strong formal ancestor for saying that decomposability is not cosmetic. It is what separates tractable from intractable compositional attribution.

The information barrier is also well supported. \[Bal94\] is a particularly good ancestor because it states the key point in nearly the right language: when only observables are available and hidden mechanisms remain latent, some counterfactual probabilities can only be bounded rather than identified exactly. \[Pea95b\], \[Shp06b\], and \[Shp08\] extend the same general lesson for sequential plans and hidden-variable causal queries. This is strong prior art for AAT’s second barrier. When the middle of the plan is invisible, there may simply not be enough information in the data to recover exact edge-level credit.

The sensitivity and estimability line helps on the positive side. \[Cha04\] shows that one can map local parameter changes to global query changes and reason about the disturbance of the overall distribution even when attribution is distributed across multiple parameters. \[Mac19\] is useful because it warns that identifiability alone is not enough if the inverse problem is unstable. Together they support the AAT idea that plan-level guarantees can be posed at a higher level than exact per-edge blame. The nearest existing ancestry is not a theorem about strategy-DAG persistence, but it does support the shape of the argument.

The observability-by-design side has two very good lineages. \[Yas08\] is the most direct formal match. It shows that sensor placement changes detectability, discriminability, and diagnosability by changing which internal failures can be isolated. That is almost exactly the right ancestor for AAT’s thought that inserting intermediate observable nodes changes the tractability class of credit assignment. \[Hol79\] gives the economics version of the same idea: better signals improve contracts precisely when they add information about action beyond what is already present in the terminal payoff. That is not about DAG diagnosis, but it is a rigorous ancestor for the broader doctrine that attribution quality depends on the observables one chooses to generate.

Taken together, the prior art already establishes five strong points:

- exact local causal attribution is hard in rich causal structures \[Cho03, Ale14\]
- decomposable structure can create tractable islands \[Are20, Kar23i\]
- hidden intermediates can turn exact attribution into a bounds problem \[Bal94, Shp08\]
- global query behavior can still be analyzed through transfer and sensitivity machinery \[Cha04, Mac19\]
- instrumentation and observability design can change what failures are isolable \[Yas08, Hol79\]

What the literature does not seem to already provide is the exact AAT package that combines those into one credit-assignment boundary for strategy DAGs and then says the right design requirement is directional fidelity plus observability engineering.

## Where AAT seems genuinely new

AAT looks strongest where it fuses the three barriers into one theorem-shaped boundary.

First, I do not see a single prior paper in the project that says all three of the following together about one strategy representation: exact attribution is hard, some directions are unidentifiable, and any factorized approximation discards essential correlation structure. Those ideas all exist separately. The unification still looks open.

Second, the persistence claim may be the most important novelty center. The existing literatures mostly ask how to compute attribution, when attribution is impossible, or when attribution becomes tractable. AAT adds a different question: how much attribution quality is actually needed for the system-level guarantee we care about. The answer it seems to give is much weaker and therefore more useful: not exact blame, just directional fidelity. That is a very good kind of novelty if it survives scrutiny.

Third, the OKR or observability-by-design framing looks better than it first sounds. \[Yas08\] and \[Hol79\] already show that measurement design changes diagnosis and implementation quality. But AAT’s move is more concrete for organizational or agentic systems: add intermediate nodes that are observable and strategically meaningful, and a deep opaque plan graph becomes a shallower diagnosable structure. I do not see that exact translation already stated in the retrieved literature.

Fourth, AAT’s use of strategy DAGs as the native object helps. The causality and Shapley papers are mostly about generic structural models, Boolean circuits, or contribution scores. The AAT claim is narrower and more architectural: plans are causal objects with edges, observability patterns, and revision dynamics. That narrower target could make the synthesis feel more load-bearing rather than merely analogical.

Fifth, the memo is strongest when it is modest about exact attribution and ambitious about boundary conditions. If framed as “we solved credit assignment,” it will look overclaimed. If framed as “we characterize where exact edge-level credit is impossible or unnecessary, and what structure rescues useful diagnosis,” it becomes much more defensible.

## Stress tests that matter most

### The three barriers must stay genuinely distinct

If the memo slides into one generic “credit assignment is hard” story, it loses most of its force. The computational barrier, the identifiability barrier, and the correlation barrier do different work and should remain separate.

### The persistence claim needs to stay at the right level

This is the technical hinge. AAT should not imply that exact edge-level diagnostics are available without exact attribution. The cleaner claim is narrower: plan-confidence or plan-level stability can still be controlled without solving full local blame.

### The decomposability analogy must not be overstated

\[Are20\] is strong support, but it is about SHAP on deterministic and decomposable Boolean circuits. That is ancestry, not identity. The memo should use it as a structural analogue, not pretend it is already an AAT strategy-DAG theorem.

### The OKR move must be stated as observability engineering, not management rhetoric

This part is promising only if it stays formal. The closest ancestors are sensor placement and informativeness, not popular business language.

### The correlation barrier should not overclaim impossibility

The safest claim is not that factorized posteriors are useless. It is that they are approximate by construction because multi-parent structures induce dependencies they cannot represent.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Planning and agent architecture | It would give a clean boundary for when plan diagnosis can be exact, approximate, or only bounded | \[Cho03\], \[Bal94\], \[Are20\] |
| RL and decision systems | It would shift focus from exact temporal blame to the weaker update quality actually needed for stable revision | \[Cha04\], \[Mac19\] |
| Organization and management design | It would formalize why intermediate key results and instrumentation improve diagnosability | \[Hol79\], \[Yas08\] |
| AI safety and oversight | It would clarify when a system can explain failures componentwise versus only at aggregate level | \[Shp08\], \[Bal94\] |

The biggest direct effect would likely be on how AAT talks about revision and diagnosis. This memo gives the framework a principled answer to a classic objection: if real plans are deep and partially hidden, why think edge-level revision is meaningful at all.

The second major effect would be on systems design. The observability-by-design part gives a constructive answer: do not merely hope for attribution after the fact, build the plan so that informative intermediate observables exist.

The third effect would be on evaluation culture. AAT suggests that exact attribution is often the wrong gold standard. In many cases the right question is whether the update signal is good enough to keep plan-level error bounded and to localize failures at the granularity the system can actually observe.

## Bottom line

The weak version of this memo is not novel. The field already knows that exact causal attribution can be computationally hard, that hidden variables can destroy identifiability, that decomposable structures create tractable islands, and that observability design changes diagnosability \[Cho03, Bal94, Are20, Yas08, Hol79\].

The strong version does look novel. AAT’s best claim is not that credit assignment is difficult, but the stronger architectural thesis that strategy-DAG revision sits behind a three-barrier boundary: exact local blame may be computationally intractable, informationally underdetermined, and correlation-losing even before approximation enters, yet persistence-level guarantees can survive on the weaker requirement of directional fidelity, and observability can be engineered to move the system back toward tractability.

The cleanest sharpened read is:

- each negative barrier has strong prior art
- observability engineering also has strong prior art
- the unified boundary plus directional-fidelity escape still looks open

A strong one-line framing is this:

AAT’s novelty is not the observation that credit assignment is hard, but the stronger claim that strategy-DAG credit assignment has three distinct failure boundaries, while the guarantees that matter most require only directionally faithful updates and the right observability design.

## Potential field impact if the claim holds

The impact ceiling is high because this memo sits close to several live bottlenecks at once.

At the modest end, the paper would still be valuable as a synthesis. It would connect causal responsibility, Shapley tractability, hidden-variable identifiability, sensitivity analysis, and diagnosability engineering under one shared question.

At the stronger end, it could improve how people build agentic systems and organizations. Instead of demanding impossible exact blame in opaque plans, it would encourage a more realistic design discipline: identify the granularity at which attribution is possible, and instrument the system so that critical intermediate failures become observable.

The biggest direct effect would likely be on planning and oversight. The memo offers a principled reason why some systems can only support aggregate or bounded diagnosis, and why others can support sharper local diagnosis because they were built with the right internal observables.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis of causality, attribution, and diagnosability literatures
- high impact if the three-barrier boundary is seen as a useful general framework for plan revision
- very high impact if the observability-by-design doctrine becomes standard language for agent and organization design

## Venue strategy

### Best-fit venues by framing

If the paper is framed around causal attribution, identifiability, and uncertainty under hidden structure, [UAI 2026](https://www.auai.org/uai2026/call_for_papers) is the cleanest specialist venue. UAI describes itself as a premier conference on learning and reasoning in the presence of uncertainty, which fits the core boundary claim well.

If the paper is framed more as a broad AI-theory contribution about planning, diagnosis, and agent design, [Artificial Intelligence](https://www.sciencedirect.com/journal/artificial-intelligence) is probably the best long-form home. Its scope explicitly includes broad advances in AI, including planning and action, reasoning under uncertainty, and multi-agent systems.

If the paper is framed as a new analytical framework for learning and revision in intelligent systems, [Transactions on Machine Learning Research](https://www.jmlr.org/tmlr/editorial-policies.html) is also plausible. TMLR explicitly welcomes theoretical studies and new analytical frameworks about the design and behavior of learning in intelligent systems.

### Recommended path

The cleanest publication strategy is:

1.  Write the full theory version for Artificial Intelligence.
2.  If the causal and uncertainty boundary becomes the sharpest core, prepare a tighter conference version for UAI.
3.  If the strongest pitch becomes learning-theoretic revision under imperfect attribution, consider TMLR.

### Practical ranking for this project

My venue ranking for this exact memo is:

- Artificial Intelligence
- UAI
- Transactions on Machine Learning Research

The fork is simple:

- if the main claim is “this is a broad theory of attribution boundaries in agent planning,” favor Artificial Intelligence
- if the main claim is “this is a causality and identifiability boundary result,” favor UAI
- if the main claim is “this is a new analytical framework for stable learning under imperfect credit assignment,” consider TMLR

## Submission snapshot

This venue advice is time-sensitive. The venue positioning above is a snapshot as of May 21, 2026.

---

## References

\[Eit01\] T. Eiter and T. Lukasiewicz, “Complexity results for structure-based causality,” *Artif. Intell.*, vol. 142, pp. 53–89, Aug. 2001, doi: [10.1016/S0004-3702(02)00271-0](https://doi.org/10.1016/S0004-3702(02)00271-0).

\[Ale14\] G. Aleksandrowicz, H. Chockler, J. Y. Halpern, and A. Ivrii, “The Computational Complexity of Structure-Based Causality,” *ArXiv*, vol. abs/1412.3076, Jun. 2014, doi: [10.1613/jair.5229](https://doi.org/10.1613/jair.5229).

\[Cho03\] H. Chockler and J. Y. Halpern, “Responsibility and blame: a structural-model approach,” *ArXiv*, vol. cs.AI/0312038, Aug. 2003, doi: [10.1613/JAIR.1391](https://doi.org/10.1613/JAIR.1391).

\[Are20\] M. Arenas, P. Barceló, L. Bertossi, and M. Monet, “The Tractability of SHAP-Score-Based Explanations for Classification over Deterministic and Decomposable Boolean Circuits,” *AAAI Conference on Artificial Intelligence*, pp. 6670–6678, Dec. 2020, doi: [10.1609/aaai.v35i8.16825](https://doi.org/10.1609/aaai.v35i8.16825).

\[Kar23i\] A. Kara, D. Olteanu, and D. Suciu, “From Shapley Value to Model Counting and Back,” *Proceedings of the ACM on Management of Data*, vol. 2, pp. 1–23, Jun. 2023, doi: [10.1145/3651142](https://doi.org/10.1145/3651142).

\[Bal94\] A. Balke and J. Pearl, “Counterfactual Probabilities: Computational Methods, Bounds and Applications,” *Conference on Uncertainty in Artificial Intelligence*, pp. 46–54, Jul. 1994, doi: [10.1016/B978-1-55860-332-5.50011-0](https://doi.org/10.1016/B978-1-55860-332-5.50011-0).

\[Shp06b\] I. Shpitser and J. Pearl, “Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models,” *AAAI Conference on Artificial Intelligence*, pp. 1219–1226, Jul. 2006.

\[Shp08\] I. Shpitser and J. Pearl, “Complete Identification Methods for the Causal Hierarchy,” *J. Mach. Learn. Res.*, vol. 9, pp. 1941–1979, Jun. 2008, doi: [10.5555/1390681.1442797](https://doi.org/10.5555/1390681.1442797).

\[Cha01c\] H. Chan and A. Darwiche, “When do Numbers Really Matter?” *ArXiv*, vol. abs/1408.1692, Aug. 2001, doi: [10.1613/jair.967](https://doi.org/10.1613/jair.967).

\[Cha04\] H. Chan and A. Darwiche, “Sensitivity Analysis in Bayesian Networks: From Single to Multiple Parameters,” *Conference on Uncertainty in Artificial Intelligence*, pp. 67–75, Jul. 2004.

\[Tra01\] L. Travé-Massuyès, T. Escobet, and R. Milne, “Model-based Diagnosability and Sensor Placement Application to a Frame 6 Gas Turbine Subsystem,” *International Joint Conference on Artificial Intelligence*, pp. 551–556, Aug. 2001.

\[Yas08\] A. A. Yassine, S. Ploix, and J. Flaus, “A Method for Sensor Placement Taking into Account Diagnosability Criteria,” *International Journal of Applied Mathematics and Computer Sciences*, vol. 18, pp. 497–512, Dec. 2008, doi: [10.2478/v10006-008-0044-5](https://doi.org/10.2478/v10006-008-0044-5).

\[Hol79\] B. R. Holmstrom, “Moral Hazard and Observability,” 1979. doi: [10.2307/3003320](https://doi.org/10.2307/3003320).

\[Hol91\] B. R. Holmstrom and P. R. Milgrom, “Multitask Principal–Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design,” 1991. doi: [10.1093/JLEO/7.SPECIAL_ISSUE.24](https://doi.org/10.1093/JLEO/7.SPECIAL_ISSUE.24).

\[Val79\] L. Valiant, “The Complexity of Enumeration and Reliability Problems,” *SIAM J. Comput.*, vol. 8, pp. 410–421, Aug. 1979, doi: [10.1137/0208032](https://doi.org/10.1137/0208032).

\[Pro83\] J. Provan and M. Ball, “The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected,” *SIAM J. Comput.*, vol. 12, pp. 777–788, Nov. 1983, doi: [10.1137/0212053](https://doi.org/10.1137/0212053).

\[Eit02b\] T. Eiter and T. Lukasiewicz, “Causes and explanations in the structural-model approach: Tractable cases,” *Artificial Intelligence*, pp. 146–153, Aug. 2002, doi: [10.1016/j.artint.2005.12.003](https://doi.org/10.1016/j.artint.2005.12.003).

\[Pea95b\] J. Pearl and J. Robins, “Probabilistic evaluation of sequential plans from causal models with hidden variables,” *Conference on Uncertainty in Artificial Intelligence*, pp. 444–453, Aug. 1995.

\[Zha94\] N. Zhang and D. Poole, “Intercausal Independence and Heterogeneous Factorization,” *ArXiv*, vol. abs/1302.6855, Jul. 1994, doi: [10.1016/B978-1-55860-332-5.50082-1](https://doi.org/10.1016/B978-1-55860-332-5.50082-1).

\[Ric12b\] T. Richardson, J. Robins, and I. Shpitser, “Nested Markov Properties for Acyclic Directed Mixed Graphs,” *Conference on Uncertainty in Artificial Intelligence*, p. 13, Aug. 2012, doi: [10.1214/22-AOS2253](https://doi.org/10.1214/22-AOS2253).

\[Shp14b\] I. Shpitser, R. Evans, T. Richardson, and J. Robins, “INTRODUCTION TO NESTED MARKOV MODELS,” 2014. doi: [10.2333/BHMK.41.3](https://doi.org/10.2333/BHMK.41.3).

\[Mac19\] O. J. Maclaren and R. Nicholson, “What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems,” *ArXiv*, vol. abs/1904.02826, Apr. 2019.
