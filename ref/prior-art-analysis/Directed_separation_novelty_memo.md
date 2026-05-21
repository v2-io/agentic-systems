# Directed separation novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Directed separation novelty memo](#directed-separation-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The taxonomy must be more than relabeling](#the-taxonomy-must-be-more-than-relabeling)
    - [The wrapper move must beat the older hybrid-architecture literature](#the-wrapper-move-must-beat-the-older-hybrid-architecture-literature)
    - [The leakage bound must not collapse into a loose analogy](#the-leakage-bound-must-not-collapse-into-a-loose-analogy)
    - [The tempo cost must be principled, not anecdotal](#the-tempo-cost-must-be-principled-not-anecdotal)
    - [Scope honesty about coupled systems is part of the contribution](#scope-honesty-about-coupled-systems-is-part-of-the-contribution)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [References](#references)

# Directed separation novelty memo

## Overall judgment

The literature already supplies deep ancestry for the two ends of AAT’s contrast. Classical control and POMDP work give strong precedents for architectures in which estimation is sufficient and can be separated from control \[Won68, Wit71, Sma73\]. Active inference and related work give a clear non-modular contrast class in which action and inference are treated as one variational process rather than a belief-then-control pipeline \[Fri12, Bal18, Bal20\]. Hybrid robot and planner-wrapper architectures also show that external scaffolding around a nontrivial controller is an old idea \[Gat92, Sim94, Au04\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-05 and AAT-chapter-11:

- a unified three-class taxonomy of separated, partial, and coupled agents
- a directed-separation criterion stated at the level of causal processing topology rather than software modularity
- a wrapper construction that coerces a coupled component into wrapper-level Class-1 behavior
- an explicit leakage bound and tempo tax for that coercion

That package looks like the real novelty opportunity. If the wrapper theorem, leakage story, and tempo-cost story hold up, this memo lands well above a mere restatement of the separation principle.

## Claim under review

In the project files, directed separation is not just a modularity slogan.

AAT-chapter-05 treats directed separation as a structural asymmetry: epistemic update is goal-blind conditional on the realized event, purposeful update depends on the updated epistemic state, and action is the coupling point. The same chapter then classifies architectures into separated, partial, and coupled according to whether goals are causally upstream of epistemic processing.

AAT-chapter-11 pushes the claim further. It says that a coupled component can be wrapped so that the wrapper’s belief-side update is structurally goal-blind, either exactly or approximately. The exact form depends on the wrapper’s type signatures and a conditional-independence condition on the underlying component. The approximate form yields a KL-style leakage bound. The same chapter adds a cost story: wrapper-level coercion trades modularity for more calls, more coordination, and less realized tempo.

Read together, the claim is stronger than “some systems are modular and others are not.” It is an architectural theory of when epistemic and teleological processing are distinct, when they are entangled, and how far entangled substrates can be coerced back toward modularity.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Separation of estimation from control | \[Won68\], \[Wit71\], \[Sma73\] | Strong | Low novelty by itself |
| Explicit contrast between modular and entangled cognition | \[Fri12\], \[Bal18\], \[Bal20\], \[Bru21c\] | Moderate to strong | Moderate novelty mostly through synthesis |
| Architectural stacks separating planning, perception, and action | \[Geo98\], \[Gat92\], \[Sim94\] | Moderate | Low to moderate novelty by itself |
| Wrapping external sources or planners around a core system | \[Au04\], \[Gat92\], \[Sim94\] | Partial | Moderate novelty if AAT proves stronger guarantees |
| Formal leakage bound for wrapper-level goal contamination | weak nearby ancestry in information-theoretic control \[Tan15b\], \[Fox16c\] | Weak | High potential novelty |
| Explicit tempo or coordination tax for coercing modularity | qualitative ancestry in robotics and information-constrained control \[Au04\], \[Tan15b\], \[Fox16c\] | Partial | High potential novelty if stated as a theorem rather than an engineering slogan |

## What the prior art already establishes

\[Won68\], \[Wit71\], and \[Sma73\] give the strongest classical baseline. They show that, under the right assumptions, state estimation can be treated as sufficient for control and the controller can operate on the estimate as if it were the state. This is the deep ancestor of belief-first, act-second architectures. But these papers do not offer a broad architectural taxonomy across modern AI systems, and they do not discuss wrapper constructions around entangled substrates.

\[Geo98\] gives a clean AI-side baseline for separated purposeful agents. The BDI picture clearly distinguishes beliefs, desires, and intentions, and therefore belongs in the ancestry of AAT’s epistemic-versus-purposeful split. Still, BDI is not the same as AAT’s directed-separation criterion. It is a useful architectural predecessor, not a theorem about causal processing topology.

\[Fri12\] is the main entangled counterpoint. It explicitly absorbs reward or cost into prior beliefs and treats action and posterior beliefs as minimizing one free-energy functional. This is a real alternative to separation-style architectures, not just a different notation for the same thing. \[Bal18\] and \[Bal20\] are especially important because they make the comparison explicit: LQG-style modularity tracks the separation principle, while active inference drops that principle and entangles action with inference. Those papers provide the strongest prior-art bridge between classical control modularity and modern non-modular theories.

The hybrid-architecture and robot-control literature shows that scaffolding and layering are not new. \[Gat92\] integrates planning and reacting asynchronously in a heterogeneous real-time robot architecture. \[Sim94\] advocates structured control that layers reactive behaviors onto deliberative components while explicitly constraining interactions between planning, perception, and action. \[Au04\] goes even closer to the wrapper idea by putting wrappers around conventional planners so that some memory accesses are replaced by external queries, with query-management and backtracking analysis. These are genuine ancestors of the “wrap an inner system” move.

The information-constrained control literature gives the nearest formal ancestor of AAT’s cost story. \[Tan15b\] proves a three-stage architecture with a virtual sensor, Kalman filter, and certainty-equivalence controller under a directed-information objective. That paper is especially relevant because it explicitly combines separation with an information cost. \[Fox16c\] similarly studies the tradeoff between external control performance and internal information rate, including principled reduction of controller order. These are strong precedents for saying modular structure can have a price. But they do not prove AAT’s specific wrapper-level leakage or tempo claims.

\[Bru21c\] matters for the blanket discussion. It distinguishes Pearl-style blankets as epistemic conditional-independence tools from Friston-style blankets as a stronger metaphysical construct. That distinction supports AAT’s attempt to recast directed separation as a conservative conditional-independence claim rather than a sweeping ontology of agents. It does not, however, yield AAT’s architecture classification by itself.

## Where AAT seems genuinely new

AAT looks strongest where it fuses several lines that prior work leaves separate.

First, the project does not merely say that some architectures are modular and others are entangled. It proposes a three-way taxonomy: separated, partial, and coupled. That may sound simple, but it is a real refinement over the usual binary contrast. The partial class is important because many practical systems are not clean Kalman-filter stacks and not pure end-to-end entanglement either. They have mixed routing, shared infrastructure, and distribution-dependent leakage.

Second, AAT’s criterion is more structural than most of the comparison literature. The question is not whether the codebase is modular or whether the designer says there is a planner and a world model. The question is whether goals are causally upstream of epistemic processing. That is a sharper criterion than software modularity and closer to a real architectural invariant.

Third, the wrapper move appears materially stronger than the older hybrid-architecture literature. \[Gat92\], \[Sim94\], and \[Au04\] show layered control, planner wrappers, and external-query management. What they do not appear to show is that a wrapper can induce wrapper-level directed separation in a theorem-shaped way. AAT’s exact and approximate forms are the novelty center here. If the wrapper-level belief update is structurally goal-blind by type signature, and if remaining dependence is pushed into an explicit KL leakage term, that is significantly more formal than ordinary planner-wrapper engineering.

Fourth, AAT’s leakage story looks distinctive. The nearest ancestors are information-theoretic control papers that price communication or directed information \[Tan15b, Fox16c\]. But those papers do not derive a wrapper-level bound on contamination of epistemic updates by teleological state. If AAT really does that, it has a nontrivial new result rather than just a new metaphor.

Fifth, the class-1-by-structure versus class-1-by-behavior distinction looks genuinely useful and not already standard. It clarifies the difference between a wrapper that is structurally separated because of its query discipline and a wrapper that merely persuades a coupled model to behave as if separated. That distinction matters a great deal for modern LLM-agent stacks, and I do not see it already cleanly named in the project literature.

## Stress tests that matter most

### The taxonomy must be more than relabeling

AAT cannot claim major novelty for discovering that some systems are modular and others are not. The real test is whether the separated, partial, and coupled partition earns its keep analytically. If the partial class changes what can be proved, measured, or safely approximated, the taxonomy matters. If not, reviewers may read it as relabeling.

### The wrapper move must beat the older hybrid-architecture literature

This is the main pressure point. \[Gat92\], \[Sim94\], and \[Au04\] already show external structure layered around planning and action. AAT needs to show what is new: not merely wrapping, but wrapper-level conditional independence or an explicit leakage theorem. If that step is not sharp, the novelty drops.

### The leakage bound must not collapse into a loose analogy

The nearest comparison class for the leakage claim is not ordinary modular software design. It is information-theoretic control and communication-constrained control \[Tan15b, Fox16c\]. AAT needs to show that its leakage quantity is not just another name for limited bandwidth or information rate, but a specifically epistemic-versus-teleological contamination measure.

### The tempo cost must be principled, not anecdotal

The robotics and planning literature already knows that layered systems can be slower or more cumbersome \[Au04, Sim94\]. AAT’s contribution here would only be strong if the cost is tied to wrapper structure in a principled way, not merely asserted as “more modules means more latency.”

### Scope honesty about coupled systems is part of the contribution

One of the more attractive features of the project material is that it does not pretend Class 3 systems satisfy the exact results. It says the theory has a scope boundary and then offers a coercion route with imperfect guarantees. That honesty itself may be part of the contribution, especially against blanket or active-inference framings that often blur the line between epistemic formalism and architectural reality \[Bru21c\].

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| LLM-agent engineering | It would give a principled way to talk about when wrappers genuinely induce modularity versus merely imitate it | \[Gat92\], \[Sim94\], \[Au04\] |
| Control and cognitive architecture theory | It would unify separation-principle ancestry with modern entangled alternatives under one cleaner architectural picture | \[Won68\], \[Wit71\], \[Fri12\], \[Bal18\], \[Bal20\] |
| Safety of agent scaffolds | It would make goal leakage an analyzable property rather than a vague prompt-engineering worry | \[Tan15b\], \[Fox16c\] |
| Composition of agent systems | It would help explain when wrapped composites can be treated as belief-first agents and when they remain coupled underneath | \[Geo98\], \[Bru21c\] |

The largest immediate impact would likely be on LLM-agent engineering. A great deal of current practice tries to force planning, retrieval, tool use, critique, and execution into cleaner channels by prompt structure or scaffolding. AAT gives a way to ask whether that is merely behavioral compliance or a real wrapper-level architectural separation.

The second major impact would be on theory. Right now the separation-principle lineage, active-inference lineage, and practical wrapper literature often live in different conversations. AAT could connect them in one frame: separated architectures, coupled architectures, and coercion between them.

The third impact would be on safety and evaluation. If wrapper-level goal leakage can be bounded, then “how entangled is this agent scaffold?” becomes a technical question rather than only an intuition. That would be a meaningful advance for evaluating agentic systems that appear modular at the interface but are built on coupled substrates.

## Bottom line

The weak version of this memo is not novel. The field already knows that estimator-controller separation exists, that active inference offers a non-modular alternative, and that planners and reactive layers can be externally orchestrated \[Won68, Fri12, Gat92\].

The strong version does look novel. AAT’s most promising claim is not the existence of modularity, but the stronger architectural thesis that entangled systems can be coerced into wrapper-level modularity only imperfectly and at a quantifiable cost: goal leakage can be bounded rather than ignored, and the price of coercion is tempo.

A strong one-line framing is this:

AAT’s novelty is not the observation that some agents are modular and others are entangled, but the stronger claim that wrapper-level directed separation can be induced, diagnosed, and costed even when the underlying substrate is coupled.

## Potential field impact if the claim holds

The impact ceiling is high because the claim speaks directly to one of the field’s live confusions: whether current agent scaffolds are genuinely modular or only operationally staged.

At the modest end, the paper would still matter as a strong synthesis. It would connect the separation-principle lineage, active-inference non-modularity, hybrid robot architectures, and modern wrapper practice into one intelligible map. That alone would be useful because these literatures are rarely discussed together.

At the stronger end, the paper could change how people talk about agent architecture. Instead of asking only whether a system has a planner, memory, tool layer, or critic, it would ask whether goals are causally upstream of epistemic processing and whether the apparent modularity is structural or merely behavioral. That would be a more mature vocabulary for compound AI systems.

The biggest direct effect would likely be on LLM-agent engineering. Many current systems use retrieval, tools, verifier loops, planner-executor splits, and orchestration wrappers to force cleaner separation of concerns. AAT could give a principled language for when those scaffolds really induce wrapper-level separation, when they only simulate it, and what leakage and tempo cost come with the attempt.

The second major effect would be on evaluation and safety. If goal leakage can be bounded at the wrapper level, then entanglement is no longer only a qualitative worry. It becomes something that can in principle be measured, compared, and optimized against. That would be a meaningful step beyond current prompt-engineering heuristics.

The third major effect would be on theory. AAT could offer a shared frame in which classical separation, active-inference entanglement, and modern compound-AI wrappers are all special cases of one more general architectural question. That is the kind of unification that tends to travel well across subfields.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis of familiar ingredients
- high impact if the wrapper theorem and leakage story are seen as technically new and useful
- very high impact if the structural-versus-behavioral separation distinction becomes standard language for agentic systems

## Venue strategy

### Best-fit venues by framing

The right venue depends on whether the paper is presented as architectural theory, technical agent-systems work, or a learning-theoretic safety result.

If the paper is framed as a deep theorem about architecture and general intelligence, the AGI Conference is a strong fit. The AGI 2026 call explicitly welcomes work on AGI architectures, planning, reasoning, motivation, safety, and hybrid methods, including hybrid architectures for language grounding and perception. That makes AGI one of the cleanest conference homes in substance. The constraint is timing: the AGI 2026 deadline was extended to April 20, 2026, so that cycle is already closed. [AGI Conference CFP](https://agi-conference.org/call-for-papers)

If the paper is framed around current compound agent systems and wrappers, ACM CAIS is unusually well matched. CAIS presents itself as a venue for rigorous, reproducible research on compound AI architectures, optimization, evaluation, and deployment, including RAG, multi-agent, and tool-augmented designs. For the LLM-wrapper angle of the memo, CAIS may be the most natural conference audience. The current 2026 meeting is already imminent, but the venue itself is highly relevant for future cycles. [ACM CAIS home](https://www.caisconf.org/)

If the paper is framed as a mathematically sharp technical result on learning or intelligent systems, TMLR is attractive. TMLR emphasizes technical correctness over subjective significance and explicitly invites theoretical studies, new analytical frameworks, and work on the design and behavior of learning in intelligent systems. The main constraint is again scope: the paper has to read as machine learning research rather than mainly as cognitive architecture theory. [TMLR overview](https://www.jmlr.org/tmlr/) [TMLR editorial policies](https://www.jmlr.org/tmlr/editorial-policies.html)

If the paper is framed as a broad AI theory contribution rather than a narrow conference paper, Artificial Intelligence journal is likely the strongest single home. AIJ explicitly welcomes broad advances in AI, including automated reasoning, planning and action, multi-agent systems, and ethical AI. That breadth suits a paper whose real contribution is a new architectural lens rather than one isolated benchmark or application. [AIJ aims and scope](https://www.sciencedirect.com/journal/artificial-intelligence)

### Recommended path

The cleanest publication strategy is:

1.  Write the full theory version for Artificial Intelligence journal.
2.  If the current wrapper and scaffold angle is central, target a conference version for ACM CAIS or AGI in the next cycle.
3.  If fast technical feedback matters, prepare a more compressed learning-theoretic version for TMLR.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- ACM CAIS
- AGI Conference
- TMLR

The fork is simple:

- if the main claim is “this is a new architecture theory for agents,” favor Artificial Intelligence journal or AGI
- if the main claim is “this clarifies modern agent wrappers and scaffolds,” favor ACM CAIS
- if the main claim is “this is a technical theorem about intelligent learning systems,” favor TMLR

## Submission snapshot

This venue advice is time-sensitive. The conference dates, positioning, and deadlines above are a snapshot as of May 21, 2026.

---

## References

\[Won68\] W. Wonham, “On the Separation Theorem of Stochastic Control,” May 01, 1968. doi: [10.1137/0306023](https://doi.org/10.1137/0306023).

\[Wit71\] H. Witsenhausen, “Separation of estimation and control for discrete time systems,” Nov. 01, 1971. doi: [10.1109/PROC.1971.8488](https://doi.org/10.1109/PROC.1971.8488).

\[Sma73\] R. Smallwood and E. Sondik, “The Optimal Control of Partially Observable Markov Processes over a Finite Horizon,” *Oper. Res.*, vol. 21, pp. 1071–1088, Oct. 1973, doi: [10.1287/opre.21.5.1071](https://doi.org/10.1287/opre.21.5.1071).

\[Fri12\] K. J. Friston, S. Samothrakis, and P. Montague, “Active inference and agency: optimal control without cost functions,” *Biological Cybernetics*, vol. 106, pp. 523–541, Oct. 2012, doi: [10.1007/s00422-012-0512-8](https://doi.org/10.1007/s00422-012-0512-8).

\[Bal18\] M. Baltieri and C. Buckley, “The modularity of action and perception revisited using control theory and active inference,” *IEEE Symposium on Artificial Life*, pp. 121–128, Jun. 2018, doi: [10.1162/isal_a_00031](https://doi.org/10.1162/isal_a_00031).

\[Bal20\] M. Baltieri and C. Buckley, “On Kalman-Bucy filters, linear quadratic control and active inference,” May 13, 2020.

\[Gat92\] E. Gat, “Integrating Planning and Reacting in a Heterogeneous Asynchronous Architecture for Controlling Real-World Mobile Robots,” *AAAI Conference on Artificial Intelligence*, pp. 809–815, Jul. 1992.

\[Sim94\] R. Simmons, “Structured control for autonomous robots,” *IEEE Trans. Robotics Autom.*, vol. 10, pp. 34–43, Feb. 1994, doi: [10.1109/70.285583](https://doi.org/10.1109/70.285583).

\[Au04\] T. Au, D. S. Nau, and V. Subrahmanian, “Utilizing Volatile External Information During Planning,” *European Conference on Artificial Intelligence*, pp. 647–651, Aug. 2004.

\[Bru21c\] J. Bruineberg, K. Dołęga, J. E. Dewhurst, and M. Baltieri, “The Emperor’s New Markov Blankets,” *Behavioral and Brain Sciences*, vol. 45, Oct. 2021, doi: [10.1017/S0140525X21002351](https://doi.org/10.1017/S0140525X21002351).

\[Geo98\] M. Georgeff, B. Pell, M. Pollack, M. Tambe, and M. Wooldridge, “The Belief-Desire-Intention Model of Agency,” *ATAL*, pp. 1–10, Jul. 1998, doi: [10.1007/3-540-49057-4_1](https://doi.org/10.1007/3-540-49057-4_1).

\[Tan15b\] T. Tanaka, P. M. Esfahani, and S. Mitter, “LQG Control With Minimum Directed Information: Semidefinite Programming Approach,” *IEEE Transactions on Automatic Control*, vol. 63, pp. 37–52, Oct. 2015, doi: [10.1109/TAC.2017.2709618](https://doi.org/10.1109/TAC.2017.2709618).

\[Fox16c\] R. Fox and N. Tishby, “Minimum-information LQG control part I: Memoryless controllers,” *2016 IEEE 55th Conference on Decision and Control (CDC)*, pp. 5610–5616, Jun. 2016, doi: [10.1109/CDC.2016.7799131](https://doi.org/10.1109/CDC.2016.7799131).
