# IB unification novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [IB unification novelty memo](#ib-unification-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The memo must not overclaim novelty for IB itself](#the-memo-must-not-overclaim-novelty-for-ib-itself)
    - [The shared-shape claim must stay separate from theorem transfer](#the-shared-shape-claim-must-stay-separate-from-theorem-transfer)
    - [The strategy layer has to be more than ordinary policy compression](#the-strategy-layer-has-to-be-more-than-ordinary-policy-compression)
    - [The communication layer needs to be specifically about shared intent](#the-communication-layer-needs-to-be-specifically-about-shared-intent)
    - [The composition layer must not become a relabeling of state-space compression](#the-composition-layer-must-not-become-a-relabeling-of-state-space-compression)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [References](#references)

# IB unification novelty memo

## Overall judgment

The literature already contains strong ancestry for each local piece of AAT’s information bottleneck story. Canonical IB gives the basic compression relevance objective \[Tis00, Har07\]. Predictive-state and causal-state work applies that logic to past-future compression in dynamical systems \[Sti07d, Cre09\]. Bounded-rational and hierarchical decision papers extend the same style of objective across internal processing nodes \[Ort12c, Gen15, Pen17\], and \[Tis11\] pushes this further by explicitly treating decisions and actions under one information-theoretic framework that links rate-distortion style tradeoffs to Bellman-style control. Sequential control and minimum-information control recast perception-action and control under sequential rate-distortion or directed-information constraints \[Tan14, Tan15b, Fox16c, Fox16\]. Multi-layer IB shows that several bottlenecks can be chained in one formal communication architecture, even with different relevance targets at different layers \[Yan17b\]. State-space compression gives a close ancestor for macro projection under prediction and computation tradeoffs \[Wol14\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-02, AAT-chapter-08, AAT-chapter-11, and AAT-chapter-12:

- one agency framework in which four different compression operations are read as instances of the same IB or rate-distortion shape
- an explicit distinction between the canonical IB form and the control sibling form, while still treating both as descendants of the same Shannon lineage
- a strategy-layer claim centered on chronica to guidance compression rather than only policy regularization or controller channel limits
- a scope-honest rule that shared compression shape does not license automatic theorem transfer across layers

That package still looks promising. The weak claim is crowded. The strong claim still looks open.

## Claim under review

The project is not merely saying that information bottleneck ideas are useful in several places.

The stronger claim is that four internal AAT maps share one compression logic:

- chronica to predictive model for belief-state construction
- chronica to strategy representation for guidance
- full purposeful state to shared-intent message for coordination
- micro-state to macro-state for composition projection

The project also makes a second claim that matters just as much: the shared shape is architectural, not theorem-automatic. The same Lagrangian form recurs because bounded cognition repeatedly asks what to retain and what to discard relative to a relevance variable, but each layer still needs its own extra proofs once one leaves the pure IB frame.

Read that way, AAT is making a stronger claim than “many things look like IB.” It is proposing a single bounded-cognition spine running through prediction, guidance, communication, and composition, while refusing to overclaim that one layer’s theorems automatically migrate to the others.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Canonical compression relevance objective | \[Tis00\], \[Har07\] | Strong | Low novelty by itself |
| Past to future predictive-state compression | \[Sti07d\], \[Cre09\] | Strong | Low novelty by itself |
| Multi-node bounded-rational architectures under one information objective | \[Gen15\], \[Pen17\], \[Ort12c\], \[Tis11\] | Strong | Moderate novelty only in broader packaging |
| Control as sequential rate-distortion or minimum-information optimization | \[Tan14\], \[Tan15b\], \[Fox16c\], \[Fox16\] | Strong | Low novelty by itself |
| Layered propagation of bottlenecked representations with different relevance targets | \[Yan17b\] | Partial to strong | Moderate novelty only if AAT goes beyond one communication stack |
| Macro projection as predictive compression of dynamical systems | \[Wol14\] | Partial | Moderate novelty |
| One framework unifying prediction, guidance, communication, and composition | distributed ancestry only | Weak | High potential novelty |
| Shared shape with explicit non-transfer of layer-specific theorems | hinted in several papers, especially \[Gen15\], but not stated as a framework rule | Partial | High potential novelty |

## What the prior art already establishes

\[Tis00\] is the canonical anchor. It formalizes the single-bottleneck objective

``` math
I(\tilde X; X) - \beta I(\tilde X; Y)
```

for one source, one compressed representation, and one relevance variable. That is the cleanest ancestor for AAT’s general thought that bounded representation is compression relative to task-relevant structure. \[Har07\] strengthens the same lineage by clarifying the relevance-defined distortion view. But this line is still one bottleneck at a time, not a full cross-interface architecture.

\[Sti07d\] and \[Cre09\] are the clearest ancestors for the model layer. They compress history while preserving predictive information about the future, making past to future compression the natural template for belief-state construction. \[Cre09\] is especially useful because it explicitly formulates a past-future information bottleneck objective and ties the resulting information curve to model reduction and system identification. This is very close to AAT’s chronica to model move. Their significance here is not only formal resemblance. They show that predictive-state construction is already understood as an IB or rate-distortion problem, which sharply lowers the novelty available for AAT’s model layer in isolation.

\[Gen15\] is probably the strongest single nearby paper for the broader package. It gives a unified bounded-rational objective over several internal interfaces and explicitly treats abstraction and hierarchy as consequences of limited information-processing capacity. It covers one-step decisions, serial hierarchies, and parallel hierarchies inside one optimization principle. \[Pen17\] extends the same style to a serial perception-action channel. \[Tis11\] strengthens this ancestry from another angle by explicitly unifying decisions and actions under an information-theoretic control language, presenting a free-energy style tradeoff between value-to-go and information-to-go and linking Bellman recursion to Blahut-Arimoto style optimization. This is real prior art for the idea that more than one internal map can sit under one information-theoretic objective.

The control line gives a second strong ancestry cluster. \[Tan15b\] minimizes directed information subject to LQG performance and explicitly joins a sensor-side compression principle to the controller side. \[Fox16c\] states the control problem directly as a sequential rate-distortion problem where observation to action mutual information is the scarce resource. \[Tan14\] provides the immediate sequential rate-distortion backbone. These papers are highly relevant because they support AAT’s claim that not every layer needs the canonical “compress X while preserving Y” form. Some layers naturally take the sibling form where the relevance object is control quality or target policy rather than an explicit external variable.

\[Yan17b\] is important because it is the closest literal multi-layer IB result in the set. It studies a layered encoding chain where each layer has its own relevance target and derives a joint rate-relevance region. That is a real precedent for saying that several bottlenecks can be studied together. But the setup remains one communication architecture fed by one source. It is not yet the AAT move of treating prediction, guidance, coordination, and composition as different agency interfaces.

\[Wol14\] is the best macro-projection ancestor. State-space compression treats macrostate construction as predictive compression under computation cost, which is very close in spirit to AAT’s composition projection story. The paper is not about agency composition in AAT’s sense, but it does show that micro to macro projection already has a serious information-theoretic compression lineage.

Taken together, the prior art already establishes five things clearly:

- IB is the canonical local form for compression with a relevance variable \[Tis00\]
- predictive state construction can be cast in exactly that form \[Sti07d, Cre09\]
- multiple internal nodes, including decision and action stages, can sit under one information-limited architecture \[Gen15, Pen17, Tis11\]
- control and action channels naturally induce a sequential rate-distortion sibling rather than a literal canonical IB copy \[Tan15b, Fox16c\]
- macro projection can also be treated as predictive compression \[Wol14\]

What the literature does not seem to already provide is the exact AAT bundle that says these four operations belong to one agency-level family while still requiring separate theorem work above the shared shape.

## Where AAT seems genuinely new

AAT looks strongest where it turns a family resemblance into an architectural doctrine.

First, I do not see a paper in the project that unifies all four AAT operations in one formal agency frame. The closest papers each stop earlier. \[Gen15\] and \[Tis11\] unify substantial bounded-rational internal structure, but not composition projection and not shared-intent communication in AAT’s sense. \[Yan17b\] unifies multiple bottlenecks in one layered network, but not heterogeneous agency interfaces. \[Wol14\] gives macro compression, but not as one member of a four-part family tied to prediction, guidance, and coordination. The package still looks open.

Second, AAT’s distinction between canonical IB and control-sibling forms is better than it may first sound. The literature already contains both kinds of objective. What is rarer is saying clearly that they are siblings rather than identical twins. \[Tis00\] is about relevance to an explicit variable. \[Tan15b\] and \[Fox16c\] are about preserving control performance under information limits. AAT’s likely good move is to unify them at the Shannon rate-distortion level without pretending the local mathematics is interchangeable.

Third, the strategy layer may be the most distinctive piece. There is substantial literature on bounded control, bounded planning, and information-regularized policies \[Gen15, Tan15b, Fox16c\], but AAT’s strategy object is more structured than a bare action distribution. It is a compressed guidance object, often DAG-like, maintained under cognitive and revision costs. That is not absent from all prior work, but it is less directly occupied than the model layer or the control layer.

Fourth, the project’s scope-honest non-transfer claim looks like a real contribution. \[Gen15\] is especially helpful here because it gives a unified principle but is explicit that convergence and convexity guarantees do not automatically carry over from the one-step case to the serial and parallel cases. AAT seems ready to elevate that from a local caveat into a framework rule: same compression shape, different proof obligations. That is a useful and not yet standard way to organize a broad theory.

Fifth, the composition side could matter more than it first appears. \[Wol14\] already gives a strong compression framing for macro descriptions of dynamical systems, but AAT wants that move inside an agency architecture where macro projection is one sibling of belief compression, strategy compression, and communication compression. That family-level positioning still looks uncommon.

## Stress tests that matter most

### The memo must not overclaim novelty for IB itself

The field already knows that compression with relevance is a natural principle for many problems \[Tis00, Gen15, Tan15b\]. The novelty cannot be “AAT discovered that many things look like information bottlenecks.”

### The shared-shape claim must stay separate from theorem transfer

This is the main pressure point. AAT is strongest if it keeps saying that a common Shannon or IB shape does not make all layers mathematically interchangeable. \[Gen15\] is a useful precedent here because the unified principle does not erase layer-specific analysis.

### The strategy layer has to be more than ordinary policy compression

If the guidance layer collapses to “control with an information penalty,” the memo becomes much weaker. The strongest version is that AAT compresses chronica into a reusable strategic object with its own maintenance and revision structure, not just into a stochastic action rule.

### The communication layer needs to be specifically about shared intent

There is already multi-layer IB and distributed information processing \[Gen15, Yan17b\]. AAT only gets a sharper claim if its communication layer really compresses purposeful state for coordination rather than just passing generic latent features down a stack.

### The composition layer must not become a relabeling of state-space compression

\[Wol14\] is strong enough that loose rhetoric would be punished here. AAT needs to show why its micro to macro projection belongs inside an agency framework, not merely in generic dynamical-systems model reduction.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| AI theory | It would give one bounded-cognition language for prediction, planning, coordination, and composition | \[Gen15\], \[Tis00\] |
| Control and decision theory | It would connect canonical IB and sequential rate-distortion as sibling layers inside one architecture | \[Tan15b\], \[Fox16c\] |
| Multi-agent coordination | It would treat shared-intent communication as one principled compression problem rather than an ad hoc messaging design choice | \[Yan17b\], \[Pen17\] |
| Macro-agency and abstraction | It would place macro projection inside the same family as other internal bottlenecks | \[Wol14\], \[Sti07d\] |

The largest direct effect would likely be internal to AAT itself. This memo offers one of the cleanest ways to make the whole framework look like one theory rather than a series of local constructions.

The second major effect would be on bounded-rationality research. Much of that literature is already close to a common language, but it is still split across prediction, control, communication, and abstraction communities. A successful AAT paper could give a cleaner map of what is genuinely the same across those areas and what is only analogous.

The third effect would be on multi-agent and systems work. If shared intent and composition projection really belong on the same compression spine as model and strategy formation, then communication design and macro-abstraction stop looking like add-ons and start looking like core agency operations.

## Bottom line

The weak version of this memo is not novel. The field already knows that IB and rate-distortion ideas recur in prediction, bounded decision-making, control, layered information processing, and macro compression \[Tis00, Sti07d, Gen15, Tan15b, Yan17b, Wol14\].

The strong version does look novel. AAT’s best claim is not that several operations can each be written in an IB-like way, but the stronger architectural thesis that four distinct agency interfaces are instances of one bounded-cognition compression family, with canonical IB and control-sibling forms treated as related descendants of the same rate-distortion spine, and with theorem transfer kept explicitly layer-local.

The cleanest sharpened read is:

- local ancestry is strong at every layer
- package-level unification still looks open
- the scope-honest non-transfer rule is part of the novelty, not a retreat from it

A strong one-line framing is this:

AAT’s novelty is not the observation that many agentic subproblems admit information-theoretic compression, but the stronger claim that prediction, guidance, coordination, and composition are four agency interfaces on one rate-distortion spine, even though each layer keeps its own theorem burden.

## Potential field impact if the claim holds

The impact ceiling is moderate to high. This is not likely to land as a single killer theorem. It is more likely to matter by giving several neighboring fields a better common map.

At the modest end, the paper would still be valuable as a synthesis. It would connect information bottleneck theory, predictive-state compression, bounded rationality, minimum-information control, multi-layer IB, and macro compression without pretending those areas are identical.

At the stronger end, it could become a useful organizing framework for bounded cognition in AI. Instead of treating belief compression, planning compression, communication compression, and abstraction as separate tricks, the paper would suggest a common design question: what information should be retained at this interface, relative to this relevance notion, under this budget.

The biggest direct effect would likely be on the reception of the whole AAT project. This memo could make several chapters read as parts of one architecture rather than as adjacent ideas.

A practical impact ranking would be:

- moderate impact if the paper is received as a disciplined synthesis of several information-theoretic lineages
- high impact if the four-operation package is seen as a genuinely useful architecture-level unification
- very high impact if later work starts treating shared intent and composition projection as standard members of the same bounded-cognition family as belief and strategy compression

## Venue strategy

### Best-fit venues by framing

If the paper is framed as a broad AI-theory contribution about bounded cognition across several agent interfaces, [Artificial Intelligence](https://www.sciencedirect.com/journal/artificial-intelligence) is the best fit. Its scope explicitly includes broad advances across AI, including reasoning under uncertainty, multi-agent systems, planning, and new ways of looking at AI problems.

If the paper is framed more as a theoretical learning-and-decision framework with information-theoretic machinery, [Transactions on Machine Learning Research](https://www.jmlr.org/tmlr/editorial-policies.html) is plausible. TMLR explicitly welcomes theoretical studies and new analytical frameworks that advance understanding of learning in intelligent systems.

If the paper is framed as a general architecture claim about agency and intelligence, [AGI Conference](https://agi-conference.org/call-for-papers) is also a natural venue. Its scope is broad and architecture-friendly, though the audience is narrower and more theory-facing than AIJ’s.

### Recommended path

The cleanest publication strategy is:

1.  Write the full framework-facing version for Artificial Intelligence.
2.  Keep a tighter theory-facing version in reserve for TMLR if the strongest contribution becomes the analytical unification rather than the broad agency architecture.
3.  Use AGI if the goal is to seed the vocabulary and architecture claim quickly with a more theory-native audience.

### Practical ranking for this project

My venue ranking for this exact memo is:

- Artificial Intelligence
- Transactions on Machine Learning Research
- AGI Conference

The fork is simple:

- if the main claim is “this unifies several agency interfaces inside one AI theory,” favor Artificial Intelligence
- if the main claim is “this is a new analytical framework for bounded learning and decision interfaces,” consider TMLR
- if the main claim is “this is a general architecture thesis for agency,” AGI is a strong community fit

---

## References

\[Tis00\] N. Tishby, F. C. Pereira, and W. Bialek, “The information bottleneck method,” *ArXiv*, vol. physics/0004057, Apr. 2000.

\[Har07\] P. Harremoës and N. Tishby, “The Information Bottleneck Revisited or How to Choose a Good Distortion Measure,” *2007 IEEE International Symposium on Information Theory*, pp. 566–570, Jun. 2007, doi: [10.1109/ISIT.2007.4557285](https://doi.org/10.1109/ISIT.2007.4557285).

\[Sti07d\] S. Still, J. Crutchfield, and C. J. Ellison, “Optimal causal inference: estimating stored information and approximating causal architecture.” *Chaos*, vol. 20 3, pp. 037111, Aug. 2007, doi: [10.1063/1.3489885](https://doi.org/10.1063/1.3489885).

\[Cre09\] F. Creutzig, A. Globerson, and N. Tishby, “Past-future information bottleneck in dynamical systems.” *Physical review. E, Statistical, nonlinear, and soft matter physics*, vol. 79 4 Pt 1, pp. 041925, Apr. 2009, doi: [10.1103/PHYSREVE.79.041925](https://doi.org/10.1103/PHYSREVE.79.041925).

\[Ort12c\] P. A. Ortega and D. A. Braun, “Thermodynamics as a theory of decision-making with information-processing costs,” Apr. 29, 2012. doi: [10.1098/rspa.2012.0683](https://doi.org/10.1098/rspa.2012.0683).

\[Gen15\] T. Genewein, F. Leibfried, J. Grau-Moya, and D. A. Braun, “Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle,” *Frontiers Robotics AI*, vol. 2, p. 27, Nov. 2015, doi: [10.3389/frobt.2015.00027](https://doi.org/10.3389/frobt.2015.00027).

\[Pen17\] Z. Peng, T. Genewein, F. Leibfried, and D. A. Braun, “An information-theoretic on-line update principle for perception-action coupling,” *2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, pp. 789–796, Sep. 2017, doi: [10.1109/IROS.2017.8202240](https://doi.org/10.1109/IROS.2017.8202240).

\[Tis11\] N. Tishby and D. Polani, “Information Theory of Decisions and Actions,” 2011. doi: [10.1007/978-1-4419-1452-1_19](https://doi.org/10.1007/978-1-4419-1452-1_19).

\[Tan14\] T. Tanaka, K.-K. K. Kim, P. Parrilo, and S. Mitter, “Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs,” *IEEE Transactions on Automatic Control*, vol. 62, pp. 1896–1910, Nov. 2014, doi: [10.1109/TAC.2016.2601148](https://doi.org/10.1109/TAC.2016.2601148).

\[Tan15b\] T. Tanaka, P. M. Esfahani, and S. Mitter, “LQG Control With Minimum Directed Information: Semidefinite Programming Approach,” *IEEE Transactions on Automatic Control*, vol. 63, pp. 37–52, Oct. 2015, doi: [10.1109/TAC.2017.2709618](https://doi.org/10.1109/TAC.2017.2709618).

\[Fox16c\] R. Fox and N. Tishby, “Minimum-information LQG control part I: Memoryless controllers,” *2016 IEEE 55th Conference on Decision and Control (CDC)*, pp. 5610–5616, Jun. 2016, doi: [10.1109/CDC.2016.7799131](https://doi.org/10.1109/CDC.2016.7799131).

\[Fox16\] R. Fox and N. Tishby, “Minimum-information LQG control Part II: Retentive controllers,” *2016 IEEE 55th Conference on Decision and Control (CDC)*, pp. 5603–5609, Jun. 2016, doi: [10.1109/CDC.2016.7799130](https://doi.org/10.1109/CDC.2016.7799130).

\[Yan17b\] Q. Yang, P. Piantanida, and D. Gündüz, “The multi-layer information bottleneck problem,” *2017 IEEE Information Theory Workshop (ITW)*, pp. 404–408, Nov. 2017, doi: [10.1109/ITW.2017.8278006](https://doi.org/10.1109/ITW.2017.8278006).

\[Wol14\] D. Wolpert, J. A. Grochow, E. Libby, and S. Dedeo, “Optimal high-level descriptions of dynamical systems,” Sep. 25, 2014.
