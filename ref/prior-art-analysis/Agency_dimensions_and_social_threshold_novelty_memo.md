# Agency dimensions and social threshold novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Agency dimensions and social threshold novelty memo](#agency-dimensions-and-social-threshold-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The two axes must stay genuinely independent](#the-two-axes-must-stay-genuinely-independent)
    - [The objective-richness axis must be concrete](#the-objective-richness-axis-must-be-concrete)
    - [The social threshold should stay minimal and structural](#the-social-threshold-should-stay-minimal-and-structural)
    - [Structural agency measures should remain distinct from the two-axis map](#structural-agency-measures-should-remain-distinct-from-the-two-axis-map)
    - [The migration story must not overclaim developmental theory](#the-migration-story-must-not-overclaim-developmental-theory)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [References](#references)

# Agency dimensions and social threshold novelty memo

## Overall judgment

This is one of the more genuinely open novelty zones in the project. The literature contains strong ancestry for each flank separately, but not for the full package. Model richness has solid prior art: predictive controllers, interactive-learning complexity results, and recent world-model theorems all support the claim that flexible goal-directed behavior requires internal predictive structure \[Sch91, Sti07b, Ric25, Vir25\]. Objective richness has partial ancestry in bounded-rationality, utility, and control formalisms, but it is much less often treated as an explicit continuous axis in its own right \[Gen15, Ort15, Ger14\]. The social-threshold side also has a good prior-art base: one-state machines are unconditional, while two-state machines are the minimal architecture for contingent reciprocity and forgiving social behavior \[Lin92b, Rom11, Zag13\]. Structural agency measures distinct from reward success also exist, especially in informational-closure, semantic-information, and bipredictability lineages \[Ber06, Ber08b, Kol18b, Alb21, Haf26, Haf26b\].

What does not appear to be already present in the project literature is the full AAT package:

- agency parameterized by two independent continuous axes, model richness and objective richness
- region-like migration across that space as learning or adaptation changes effective internal structure
- a clean social threshold claim that one-state systems are below the minimal architecture for genuine contingent sociality while two-state systems are the first nontrivial social regime
- a structural, scale-aware agency lens that can talk about architecture without collapsing into task performance

That package looks more novel than most of the remaining topics. It is not the easiest theorem memo, but it may be one of the strongest framework memos.

## Claim under review

The project is not merely saying that some agents have better models than others, or that social behavior needs memory.

The stronger claim is that agency varies along at least two largely independent dimensions:

- **model richness**: how much internal predictive structure the agent has about the world
- **objective richness**: how rich the agent’s purposive structure is, from absent or degenerate preference through simple setpoint to trajectory-level or structured objectives

The project then adds a second claim: these dimensions are continuous, not just category labels, and agents can move across the space as training, adaptation, or auto-tuning changes their effective structure.

Finally, the project adds a sharp threshold story for sociality. On this view, one-state machines are not merely weakly social. They are structurally below the threshold for contingent social behavior. Two-state machines are the minimal architecture that can support reciprocity, branch on partner behavior, and recover cooperation after noise.

Read that way, AAT is making a stronger claim than “agency comes in degrees.” It is proposing a coordinate system for kinds of agency plus a minimal-complexity threshold for social agency.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Model richness as a real structural dimension | \[Sch91\], \[Sti07b\], \[Ric25\], \[Vir25\] | Strong | Low novelty by itself |
| Objective richness as a separate graded dimension | \[Gen15\], \[Ort15\], \[Ger14\] and related utility formalisms | Partial | Moderate to high novelty |
| Joint continuous two-axis decomposition of agency | no close direct precursor found | Weak | Highest novelty candidate |
| Migration across regions as learning changes effective structure | partial ancestry only | Weak | High novelty |
| One-state machines are unconditional and below contingent sociality | \[Rub86\], \[Lin92b\], \[Zag13\], \[Vol02\] | Strong | Low novelty by itself |
| Two-state machines are minimal for contingent reciprocity or forgiving social behavior | \[Lin92b\], \[Rom11\], \[Zag13\] | Strong | Moderate novelty only in broader packaging |
| Structural agency measures distinct from task success | \[Alb21\], \[Kol18b\], \[Haf26\], \[Haf26b\] | Strong | Low novelty by itself |
| One framework connecting the two-axis map, social threshold, and structural agency metrics | no direct single precursor found | Weak | High novelty |

## What the prior art already establishes

The model-richness side is the strongest and cleanest. \[Ric25\] is especially important because it gives a formal theorem shape: sufficiently general multi-step goal-directed behavior forces an implicit world model. Earlier work already points in this direction through model-building control and predictive-state compression \[Sch91, Sti07b\], but \[Ric25\] makes the case much sharper. This means AAT should not claim novelty for saying that sophisticated flexible agency requires predictive internal structure.

The objective-richness side is much less developed as an explicit axis. There is plenty of literature where richer utility or preference structure matters, and bounded-rational architectures often trade off utility against informational cost \[Gen15, Ort15\]. But that is not the same as treating objective richness itself as a continuous coordinate of agency. This is one of the memo’s clearest possible novelty openings.

The structural-agency side has real prior art too. \[Kol18b\] defines semantic information in terms of what is causally necessary for self-maintenance, which is clearly architecture-level rather than reward-level. \[Alb21\] is especially useful because it explicitly separates task performance from internal structural and causal measures of autonomy. \[Haf26\] and \[Haf26b\] then go even further by proposing bipredictability as a task-independent interaction-quality measure and by sharply distinguishing agency from intelligence. These are strong ancestors for the claim that one can study agency structurally rather than only by reward or success metrics.

The social-threshold side is also well supported. The finite-automata literature has long treated strategy complexity as a structural variable \[Rub86, Abr86, Kal88\]. But the strongest threshold pattern is simpler than that whole literature: one-state automata can only implement unconditional behavior, while two-state automata are the first regime in which contingent reciprocity becomes possible. \[Zag13\] is especially vivid here, because the paper’s full strategy space makes the threshold visually obvious: ALLC and ALLD are the one-state cases, while forgiving and reciprocal strategies live in the two-state region. \[Lin92b\] and \[Rom11\] support the same general message.

The coevolution literature adds a systems-level version of the threshold story. \[Mil96b\] and \[Mil22c\] suggest that adding even minimal state complexity can unlock sharp transitions from asocial to social regimes. That is good ancestry for AAT’s social-threshold ambition, even if those papers do not state the threshold in exactly the same way.

Taken together, the prior art already establishes five things clearly:

- model richness is real and tightly connected to flexible agency \[Ric25\]
- structural measures of agency distinct from reward performance are possible \[Alb21, Kol18b, Haf26b\]
- finite-state complexity matters for social behavior \[Rub86, Kal88\]
- one-state machines are unconditional \[Zag13\]
- two-state machines are the first plausible regime for contingent reciprocity \[Lin92b, Zag13\]

What the literature does not seem to already provide is the exact AAT package that makes model richness and objective richness into one joint coordinate system and then anchors sociality at a minimal architectural threshold inside that map.

## Where AAT seems genuinely new

AAT looks strongest where it turns several nearby literatures into one taxonomy of agency.

First, I do not see a close prior paper in the project that parameterizes agency by two independent continuous axes of model richness and objective richness. The pieces exist separately, but the joint decomposition still looks open. This is the memo’s clearest novelty center.

Second, the objective-richness axis may be more important than the model-richness axis for novelty. The field already talks a lot about whether agents have models. It talks much less cleanly about how rich their purposive structure is in a way that can vary continuously and independently of model quality. If AAT can make that axis feel natural rather than arbitrary, it has a real contribution.

Third, the social-threshold claim is stronger than a generic “memory matters” line. The finite-state literature supports a threshold at two states for contingent sociality quite well. AAT’s opportunity is to absorb that into a larger theory of agency types. That makes the threshold feel like a theorem-shaped consequence of a coordinate system rather than a niche result from repeated games.

Fourth, the structural agency-measure line gives AAT a useful external hook. \[Alb21\], \[Kol18b\], and \[Haf26b\] all support the idea that architecture and coupling quality can be measured apart from reward. That does not by itself yield AAT’s two-axis map, but it makes the framework look less speculative when it claims that agency should be described structurally.

Fifth, AAT may be unusually strong if it can connect individual and social thresholds. The intriguing version is not just “two states are needed for reciprocity.” It is that the same coordinate system that classifies solitary agents also predicts when social agency first becomes possible.

## Stress tests that matter most

### The two axes must stay genuinely independent

This is the main pressure point. If objective richness just collapses into model richness or vice versa, the memo gets much weaker. The framework needs examples where one rises without the other.

### The objective-richness axis must be concrete

This is also where reviewers may push hardest. The axis needs to do analytical work, not just redescribe “having more complicated goals.”

### The social threshold should stay minimal and structural

The strongest claim is not “two states are enough for all sociality.” It is the narrower and cleaner claim that two states are the minimal architecture for contingent social behavior, while one-state systems are stuck with unconditional policies.

### Structural agency measures should remain distinct from the two-axis map

The memo is strongest if those measures are used as supporting ancestry, not as if they already instantiate AAT’s decomposition. \[Haf26b\], for example, offers a different two-axis split, but not AAT’s model-richness versus objective-richness split.

### The migration story must not overclaim developmental theory

The safe claim is that training and adaptation can move systems across regions of the map. The unsafe claim would be a universal developmental law without evidence.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| AI theory | It would give a coordinate system for talking about kinds and degrees of agency | \[Ric25\], \[Alb21\], \[Haf26b\] |
| Multi-agent theory | It would tie minimal sociality to architectural thresholds rather than just payoff equilibria | \[Rub86\], \[Lin92b\], \[Zag13\] |
| Comparative cognition and artificial life | It would offer a common language for simple, reactive, model-rich, and socially contingent agents | automata and autonomy lineages |
| Safety and evaluation | It would help distinguish structural agency from mere benchmark success | \[Kol18b\], \[Haf26\] |

The biggest direct effect would likely be conceptual but important. AAT would give people a better language for saying what kind of agent they are talking about, rather than treating all successful controllers as points on one vague intelligence scale.

The second major effect would be on social-agent analysis. The threshold story gives a clean explanation of why some systems can coordinate only blindly while others can reciprocate, forgive, or adapt to partner behavior.

The third effect would be on evaluation. If agency really has structural dimensions distinct from reward success, then many current benchmarks are measuring only a thin slice of what matters.

## Bottom line

The weak version of this memo is not novel. The field already knows that flexible agency requires predictive structure, that architecture-level agency measures can differ from reward success, and that one-state versus two-state automata mark a real boundary between unconditional and contingent strategies \[Ric25, Alb21, Kol18b, Zag13\].

The strong version does look novel. AAT’s best claim is not that agency has structure, but the stronger framework thesis that agency can be mapped in a two-dimensional space of model richness and objective richness, with genuine migration across that space as systems learn, and with social agency emerging only once minimal internal complexity crosses the contingent-behavior threshold.

The cleanest sharpened read is:

- the model-richness side has strong prior art
- the social-threshold side has strong prior art
- the structural-measure side has strong prior art
- the joint two-axis coordinate system still looks open

A strong one-line framing is this:

AAT’s novelty is not the observation that some agents have better models or more memory, but the stronger claim that agency occupies a structured space with independent model and objective axes, and that contingent sociality first appears only after a minimal internal-complexity threshold is crossed.

## Potential field impact if the claim holds

The impact ceiling is substantial because this memo could provide vocabulary the field currently lacks.

At the modest end, the paper would still matter as a synthesis. It would connect world-model necessity, autonomy measures, finite-automata social complexity, and architecture-level agency metrics under one shared question.

At the stronger end, it could become a useful classification language. People could talk more precisely about whether a system is model-poor but objective-rich, model-rich but objective-poor, pre-social, minimally social, or structurally social in a contingent sense.

The biggest direct effect would likely be on how broad AI theory papers frame agent comparisons. The memo offers a way to stop collapsing all agency talk into one scalar.

A practical impact ranking would be:

- moderate impact if the paper is received as a thoughtful synthesis and taxonomy
- high impact if the two-axis map is seen as a useful common language across AI and artificial life
- very high impact if the social-threshold story becomes standard shorthand for when real contingent sociality begins

## Venue strategy

### Best-fit venues by framing

If the paper is framed as a broad AI-theory contribution about kinds of agency and structural evaluation, [Artificial Intelligence](https://www.sciencedirect.com/journal/artificial-intelligence) is the strongest long-form home.

If the paper is framed as a general-agency or AGI-architecture contribution, [AGI Conference](https://agi-conference.org/call-for-papers) is a natural venue. Its scope is broad and especially friendly to foundational architecture questions.

If the paper is framed as a theoretical learning-and-intelligence framework with structural measures and formal axes, [Transactions on Machine Learning Research](https://www.jmlr.org/tmlr/editorial-policies.html) is plausible, though somewhat less natural than AIJ or AGI.

### Recommended path

The cleanest publication strategy is:

1.  Write the full framework version for Artificial Intelligence.
2.  If the goal is early conceptual uptake, prepare a theory-facing conference version for AGI.
3.  If the strongest contribution becomes the formal structural-measure side, consider TMLR.

### Practical ranking for this project

My venue ranking for this exact memo is:

- Artificial Intelligence
- AGI Conference
- Transactions on Machine Learning Research

The fork is simple:

- if the main claim is “this is a broad coordinate system for agency,” favor Artificial Intelligence
- if the main claim is “this is a foundational theory of general agency,” favor AGI
- if the main claim is “this is a formal framework for structural intelligence measures,” consider TMLR

## Submission snapshot

This venue advice is time-sensitive. The venue positioning above is a snapshot as of May 21, 2026.

---

## References

\[Sch91\] J. Schmidhuber, “A possibility for implementing curiosity and boredom in model-building neural controllers,” Feb. 14, 1991. doi: [10.7551/mitpress/3115.003.0030](https://doi.org/10.7551/mitpress/3115.003.0030).

\[Sti07b\] S. Still, “Information-theoretic approach to interactive learning,” Sep. 12, 2007. doi: [10.1209/0295-5075/85/28005](https://doi.org/10.1209/0295-5075/85/28005).

\[Ric25\] J. Richens, D. Abel, A. Bellot, and T. Everitt, “General agents contain world models,” Jun. 02, 2025.

\[Vir25\] N. Virgo, M. Biehl, M. Baltieri, and M. Capucci, “A ‘good regulator theorem’ for embodied agents,” *ArXiv*, vol. abs/2508.06326, Aug. 2025, doi: [10.48550/arXiv.2508.06326](https://doi.org/10.48550/arXiv.2508.06326).

\[Gen15\] T. Genewein, F. Leibfried, J. Grau-Moya, and D. A. Braun, “Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle,” *Frontiers Robotics AI*, vol. 2, p. 27, Nov. 2015, doi: [10.3389/frobt.2015.00027](https://doi.org/10.3389/frobt.2015.00027).

\[Ort15\] P. A. Ortega, D. A. Braun, J. Dyer, K.-E. Kim, and N. Tishby, “Information-Theoretic Bounded Rationality,” *ArXiv*, vol. abs/1512.06789, Dec. 2015.

\[Ger14\] S. Gerrit, “Informational Constraints and Organisation of Behaviour,” Jan. 24, 2014. doi: [10.18745/TH.15436](https://doi.org/10.18745/TH.15436).

\[Lin92b\] B. G. Linster, “Evolutionary Stability in the Infinitely Repeated Prisoners’ Dilemma Played by Two-State Moore Machines,” Apr. 01, 1992. doi: [10.2307/1060227](https://doi.org/10.2307/1060227).

\[Rom11\] J. Romero, “Finite Automata in Undiscounted Repeated Games with Private Monitoring,” Mar. 01, 2011.

\[Zag13\] B. M. Zagorsky, J. G. Reiter, K. Chatterjee, and M. Nowak, “Forgiver Triumphs in Alternating Prisoner’s Dilemma,” *PLoS ONE*, vol. 8, Aug. 2013, doi: [10.1371/journal.pone.0080814](https://doi.org/10.1371/journal.pone.0080814).

\[Ber06\] N. Bertschinger, E. Olbrich, N. Ay, and J. Jost, “Information and closure in systems theory,” 2006.

\[Ber08b\] N. Bertschinger, E. Olbrich, N. Ay, and J. Jost, “Autonomy: An information theoretic perspective,” *Bio Systems*, vol. 91 2, pp. 331–45, Feb. 2008, doi: [10.1016/j.biosystems.2007.05.018](https://doi.org/10.1016/j.biosystems.2007.05.018).

\[Kol18b\] A. Kolchinsky and D. Wolpert, “Semantic information, autonomous agency and non-equilibrium statistical physics,” *Interface Focus*, vol. 8, Jun. 2018, doi: [10.1098/rsfs.2018.0041](https://doi.org/10.1098/rsfs.2018.0041).

\[Alb21\] L. Albantakis, “Quantifying the Autonomy of Structurally Diverse Automata: A Comparison of Candidate Measures,” *Entropy*, vol. 23, Oct. 2021, doi: [10.3390/e23111415](https://doi.org/10.3390/e23111415).

\[Haf26\] W. Hafez, C. Reid, and A. Nazeri, “The Informational Cost of Agency: A Bounded Measure of Interaction Efficiency for Deployed Reinforcement Learning,” Mar. 01, 2026.

\[Haf26b\] W. Hafez, C. Wei, R. Felipe, A. Nazeri, and C. Reid, “A Mathematical Theory of Agency and Intelligence,” *ArXiv*, vol. abs/2602.22519, Feb. 2026, doi: [10.48550/arXiv.2602.22519](https://doi.org/10.48550/arXiv.2602.22519).

\[Rub86\] A. Rubinstein, “Finite automata play the repeated prisoner’s dilemma,” Jun. 01, 1986. doi: [10.1016/0022-0531(86)90021-9](https://doi.org/10.1016/0022-0531(86)90021-9).

\[Vol02\] O. Volij, “In Defense of DEFECT,” *Games Econ. Behav.*, vol. 39, pp. 309–321, May 2002, doi: [10.1006/game.2001.0893](https://doi.org/10.1006/game.2001.0893).

\[Abr86\] D. Abreu and A. Rubinstein, “The Structure of Nash Equilibrium in Repeated Games with Finite Automata (Now published in Econometrica, 56 (1988), pp.1259-1282.),” 1986. doi: [10.2307/1913097](https://doi.org/10.2307/1913097).

\[Kal88\] E. Kalai and W. Stanford, “Finite Rationality and Interpersonal Complexity in Repeated Games,” Mar. 01, 1988. doi: [10.2307/1911078](https://doi.org/10.2307/1911078).

\[Mil96b\] J. H. Miller, “The coevolution of automata in the repeated Prisoner’s Dilemma,” 1996. doi: [10.1016/0167-2681(95)00052-6](https://doi.org/10.1016/0167-2681(95)00052-6).

\[Mil22c\] J. H. Miller, “Ex Machina: Coevolving Machines and the Origins of the Social Universe,” Dec. 06, 2022. doi: [10.37911/9781947864429](https://doi.org/10.37911/9781947864429).
