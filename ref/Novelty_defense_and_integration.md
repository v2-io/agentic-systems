# Novelty defense and integration

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Novelty defense and integration report](#novelty-defense-and-integration-report)
- [Executive summary](#executive-summary)
- [Pillar 1](#pillar-1)
  - [Causal insufficiency and forced exploration](#causal-insufficiency-and-forced-exploration)
  - [Closest papers](#closest-papers)
  - [Defense strategy](#defense-strategy)
- [Pillar 2](#pillar-2)
  - [Composition closure defect and Bridge Lemma](#composition-closure-defect-and-bridge-lemma)
  - [Closest papers](#closest-papers-1)
  - [Defense strategy](#defense-strategy-1)
- [Pillar 3](#pillar-3)
  - [Logogenic bias bound for LLMs](#logogenic-bias-bound-for-llms)
  - [Closest papers](#closest-papers-2)
  - [Defense strategy](#defense-strategy-2)
- [Pillar 4](#pillar-4)
  - [TST in agentic environments](#tst-in-agentic-environments)
  - [Closest papers](#closest-papers-3)
  - [Defense strategy](#defense-strategy-3)
- [Cross-cutting integration](#cross-cutting-integration)
- [Recommended claim language](#recommended-claim-language)
- [Bottom line](#bottom-line)
- [References](#references)

## Novelty defense and integration report

The two searches converge on a clear picture. The strongest prior art around unified agency sits in active inference, control as inference, information-theoretic bounded rationality, causal decision making under hidden confounding, and abstraction for partially observed or decentralized control \[Fri12c, Kap09, Ort12c, Fri15, Bar15, Zha16, Lee18b, Lee20, Sub20, Nay12\]. The direct novelty pressure on ASF does not come from broad systems theory papers alone. It comes from a handful of narrower literatures that already formalize parts of the same terrain. At the same time, the search did not uncover close matches for an ambiguity-bounded architectural bias law for LLM agents, nor for a rigorous transfer of these agentic formalisms into developer-agent software economics.

The right posture is therefore selective rather than maximalist. Several ASF claims should be positioned as sharpened syntheses over strong precursor mathematics. Others appear genuinely new, at least within the current evidence base. The main caution is pillar 4, where the current searches are materially thinner than the other three.

## Executive summary

| Pillar | Verdict | Main prior-art locus | Confidence |
|:---|:---|:---|:---|
| Causal insufficiency and forced exploration | Conceptual Precursor | Causal bandits and causal MDPs under hidden confounding \[Bar15, Zha16, For17, Lee18b, Lee20\] | High |
| Composition closure defect and Bridge Lemma | Conceptual Precursor | Approximate information states, state abstraction, decentralized control \[Sub20, Abe16, Tay08, Nay12, Con20\] | High |
| Logogenic bias bound for LLMs | Wholly Novel | Empirical ambiguity and action-belief gap work, with only loose bounded-rationality analogies \[Wan24b, Yan24d, Tan25, Pal25, Liu24, Gen15\] | Medium |
| TST in agentic environments | Wholly Novel | Developer-agent papers are systems and benchmark papers, not formal economic theory \[Yan24b, Pan24, Vij25, Xia25b, Gol25\] | Low |

## Pillar 1

### Causal insufficiency and forced exploration

The closest mathematical neighbors are not active inference papers. They are the causal bandit and causal MDP papers around hidden confounding and intervention design \[Bar15, Zha16, For17, Lee18b, Lee20\]. These works already establish the key premise that observational and interventional data are not interchangeable when latent common causes are present. They also show that naive strategies can be provably suboptimal even with many interventions.

What they do not appear to do, on current evidence, is state the ASF claim in the same form. The current literature justifies intervention by regret, identifiability, and policy optimality under confounding. It does not cleanly derive a no-go statement that perfect on-policy execution cannot reveal latent L1 strategy flaws and therefore forces deliberately redundant inefficiency.

| Item | What prior art already has | What still appears distinct in ASF |
|:---|:---|:---|
| Observational versus experimental mismatch | Hidden confounders make passive and active data non-equivalent \[Bar15, Zha16\] | The mismatch is framed as a no-go constraint on self-diagnosis under policy-perfect execution |
| Need for intervention | Low-regret learning can require both observational and interventional quantities \[Bar15, For17\] | Intervention is cast as structurally necessary for discovering latent strategic common causes |
| Exploration design | Not all interventions are useful. Some are redundant or dominated \[Lee18b, Lee20\] | The claim is about forced inefficient exploration, not just smarter intervention selection |
| Relation to causal hierarchy | The literature is explicitly causal and identifiability-aware \[Bar15, Lee18b, Lee20\] | The search did not surface a paper tying this to a general theorem about agentic self-correction under Pearl-style observational equivalence |

### Closest papers

\[Bar15\] is the most direct precursor. It shows that with unobserved confounders, a rational bandit agent cannot rely on experimental quantities alone and may need both observational and experimental information to achieve low regret. That is very close to the ASF intuition that efficient execution does not reveal enough structure.

\[Zha16\] ports the same issue into MDPs. Standard algorithms become suboptimal when unobserved confounders break the equivalence between passive observation and active intervention. This sharpens the claim from one-shot action choice to sequential control.

\[For17\] goes further by arguing that naive randomization can itself be suboptimal under hidden confounding, and that counterfactual fusion is needed. This is important because it narrows the gap between generic exploration and structure-aware experimentation.

\[Lee18b\] and \[Lee20\] are especially important for defense positioning. They prove that intervening on everything, or observing everything, can be provably wasteful or even harmful. This means the closest antecedent is not a generic exploration paper but a literature on minimal qualified interventions and non-redundant mixed policies.

\[Fri15\], by contrast, is a weaker threat to this pillar. It derives exploration from epistemic value inside expected free energy, not from causal unidentifiability. The uncertainty it reduces is uncertainty under the generative model, not Pearl-style observational equivalence under hidden common causes.

### Defense strategy

- Claim novelty at the level of **why exploration is required**, not merely that exploration has epistemic value.
- Cite the causal bandit and causal MDP line early as the nearest formal neighborhood \[Bar15, Zha16, For17, Lee18b, Lee20\].
- Concede that prior work already shows intervention can be necessary under hidden confounding.
- Then state the ASF increment narrowly: it recasts that need as a no-go theorem for self-diagnosis under policy-perfect execution, tied to latent strategic correlation structure rather than only regret minimization.
- Avoid language suggesting ASF discovered that causal intervention matters in agents. The safer claim is that ASF gives a stronger agent-theoretic interpretation and a new placement of inefficiency inside persistence and adaptation.

## Pillar 2

### Composition closure defect and Bridge Lemma

The strongest contrast here is not really ASF versus active inference as a whole. It is ASF versus two different literatures that solve different pieces of the problem.

One piece is the Markov blanket literature, which offers a statistical and thermodynamic account of system boundaries and nested agency \[Par19, Kir18\]. The other piece is the abstraction and decentralized control literature, which offers actual value-loss or optimality-loss bounds under coarse-graining and compressed information \[Sub20, Abe16, Tay08, Nay12, Con20\].

This split matters. The search did not uncover a Markov blanket paper that proves the kind of control-theoretic Bridge Lemma described in ASF. The blanket papers support nested agency conceptually and statistically, but not with explicit predictive-loss bounds for coarse-graining. The closest mathematical cousins to the Bridge Lemma live elsewhere.

| Literature | What it contributes | What it does not yet match |
|:---|:---|:---|
| Markov blankets and active inference \[Par19, Kir18\] | Internal and external separation, nested blanketed systems, variational bounds on surprise | No explicit coarse-graining error bound, no coordination-overhead theorem, no strong monotonicity condition |
| Approximate information states \[Sub20\] | Conditions for compressed histories to preserve control with explicit loss bounds | Not framed as composite agency or organizational closure |
| State abstraction and homomorphism bounds \[Abe16, Tay08\] | Near-optimality guarantees under aggregation | Single-agent MDP framing, not boundary formation of composite agents |
| Decentralized control and common information \[Nay12\] | Exact structural reduction of multi-controller systems to a coordinator POMDP | No explicit predictive-loss bound from composition, no closure-defect metric |
| Influence-based abstraction \[Con20\] | Direct bounds from predictive compression error to value loss in multi-agent settings | Still not the same as a strong-monotonicity criterion for macro-agent legitimacy |

### Closest papers

\[Par19\] is the key Markov blanket paper for comparison. It gives a formal partition between internal and external states and a variational bound on surprise. It also allows recursive nesting. But its compositional move is statistical and thermodynamic. It does not provide a control-theoretic bound on the error of treating a collection as one agent.

\[Kir18\] makes the same point in more explicitly hierarchical terms. It argues that systems can be nested blankets of blankets, and that autonomy depends on temporal depth. Yet the paper itself remains conceptual at the crucial compositional step. It invokes synergetic ordering and self-organization, not a theorem bounding predictive loss of coarse-graining.

\[Sub20\] is the strongest direct formal neighbor to a Bridge Lemma. It proves that if a compressed history state approximately preserves reward prediction and recursive self-prediction, then the resulting control policy has bounded loss. This is a real bridge from predictive compression error to control error.

\[Con20\] is also highly relevant. It gives explicit bounds on value loss from approximate influence representations in multi-agent systems. That is closer to coordination-overhead mathematics than the blanket papers are.

\[Nay12\] offers an exact structural reduction for decentralized control through common information and coordinator prescriptions. It does not prove a lossy composition theorem, but it shows the right formal space where such a theorem would live.

### Defense strategy

- Separate the literature review into **statistical boundaries** and **bounded-loss composition** instead of letting Markov blankets stand in for all prior art.
- Position \[Par19\] and \[Kir18\] as conceptual precursors on nested agency and system boundary, not as direct anticipation of the Bridge Lemma.
- Position \[Sub20\], \[Con20\], \[Abe16\], and \[Tay08\] as the closest mathematical neighbors because they actually prove approximation-loss results.
- Claim novelty narrowly at the missing junction: ASF appears to supply a criterion for when composition is legitimate as an agent boundary claim, not just when state compression preserves value.
- If strong monotonicity is central, foreground that no retrieved paper appears to make this condition the hinge between stable coexistence and valid macro-agent coarse-graining.

## Pillar 3

### Logogenic bias bound for LLMs

This pillar is where the literature thins out sharply. The search found many empirical demonstrations that tool-using or agentic LLMs behave badly under ambiguity, incomplete instructions, or action-belief mismatch \[Wan24b, Yan24d, Tan25, Pal25, Liu24, Vij25\]. It also found bounded-rationality work that can be read as a distant conceptual precursor for architectural tradeoffs, abstraction, and utility-shaped information processing \[Ort12c, Gen15\]. What it did not find is a formal architectural classification that looks like ASF class structure, nor a theorem that epistemic bias is bounded by environmental ambiguity.

| Item | What prior art already has | What still appears distinct in ASF |
|:---|:---|:---|
| Ambiguity hurts tool use | LLM agents fail under missing information and underspecified tasks \[Wan24b, Yan24d, Vij25\] | A formal bias law tied to ambiguity magnitude |
| Action-belief gap | Agents fail to act on known risk or stated confidence \[Tan25, Pal25\] | A mechanistic theorem from coupled belief-goal generation |
| Information-processing constraints | Bounded-rationality and hierarchical decision work links utility and compression \[Ort12c, Gen15\] | No equivalent classification of LLM agent architectures by bias coupling |
| Calibration fixes | Probe or verifier methods can reduce failures \[Liu24, Tan25\] | No derived upper bound of the form claimed by ASF |

### Closest papers

\[Wan24b\] is important because it explicitly links hallucinated missing arguments to the next-token prediction objective. That is conceptually close to the claim that one forward pass entangles truth-seeking and action selection. But it is an empirical prompt-and-benchmark paper, not a formal bias theorem.

\[Yan24d\] and \[Vij25\] show that models often fail to recognize incomplete conditions or underspecification and improve when forced to verify or ask clarifying questions. These are strong behavioral precursors for an ambiguity-sensitive bias claim.

\[Tan25\] and \[Pal25\] reveal a clean action-belief gap. Agents can know a risk or state a confidence and still act against that knowledge. These are very useful support papers for the general phenomenon, but they do not explain it through a coupled belief-goal architecture with a formal bound.

\[Ort12c\] and \[Gen15\] provide the best conceptual bridge from formal decision theory. They show how information-processing constraints shape choices, abstractions, and hierarchical organization. Still, they do not classify LLM architectures or derive semantic ambiguity bounds.

### Defense strategy

- State this claim as a **new formal law over a phenomenon already observed empirically**.
- Use the LLM-agent papers to establish that ambiguity sensitivity, hallucinated completion, and action-belief gaps are real and recurrent \[Wan24b, Yan24d, Tan25, Pal25, Liu24, Vij25\].
- Then state that the missing piece in prior art is a structural theorem linking those failures to a coupled belief-goal architecture and bounding their magnitude by environmental ambiguity.
- Avoid claiming ASF discovered LLM hallucination, motivated reasoning, or underspecification failure. The safer claim is that ASF supplies the first unifying formal account found in the current search.
- Keep this verdict provisional. A follow-on search focused only on formal ambiguity and epistemic bias in sequential agents could still surface closer math.

## Pillar 4

### TST in agentic environments

The current evidence base is weakest here. The developer-agent literature retrieved by the second search is real and growing, but it is mostly about interfaces, training environments, reinforcement learning pipelines, ambiguity benchmarks, and empirical failure analysis \[Yan24b, Pan24, Vij25, Xia25b, Gol25, Uga26\]. None of the papers surfaced by the searches instantiate free-energy, bounded-rationality, POMDP-control, or Pearl-style intervention theory to prove software engineering economics, code comprehension dominance, or technical debt as observability infrastructure.

This does not prove no such work exists. It only means the two searches did not find a close formal match.

| Subclaim | Evidence from current searches | Current verdict |
|:---|:---|:---|
| Developer agents operate in interactive, partially observed environments | Strong empirical support \[Yan24b, Pan24, Gol25\] | Prior art exists |
| Ambiguity and underspecification are central in coding tasks | Strong empirical support \[Vij25, Yan24b\] | Prior art exists |
| Tooling and interface shape observability and performance | Strong empirical support \[Yan24b, Xia25b\] | Prior art exists |
| Testing functions as a formal intervention operator in a causal sense | No close formal match surfaced | Provisionally novel |
| Code comprehension time dominates by a Lindy-like argument | No close formal match surfaced | Provisionally novel |
| Technical debt and architecture map into observation noise or update gain for developer agents | No close formal match surfaced | Provisionally novel |

### Closest papers

\[Yan24b\] shows that agent-computer interface design strongly shapes developer-agent performance. This is the closest current evidence to an observability story, but it remains design and ablation work rather than formal theory.

\[Pan24\] turns software repositories and tests into a training environment with verifiers. It is highly relevant as infrastructure, but the paper does not theorize testing as intervention or codebases as partially observed dynamical systems.

\[Vij25\] shows that underspecification in software tasks creates large performance losses that interaction can partly recover. This supports the importance of ambiguity in developer-agent settings.

\[Xia25b\] is useful as a cautionary baseline paper. Simpler non-agentic pipelines can outperform richer agent scaffolds. For TST this suggests that any theory of developer agents must explain when extra agentic machinery pays for itself.

### Defense strategy

- Mark the TST section as **provisional and undercovered** rather than fully closed.
- Claim novelty only for the formal transfer, not for the observation that coding agents benefit from feedback, tests, and better interfaces.
- Use the developer-agent papers as domain evidence that the environment has the right structure for TST style analysis.
- State plainly that the current searches did not uncover a prior paper formalizing software engineering economics with these agentic-control tools.
- Recommend a dedicated follow-on search on software repository cognition, technical debt as observability, and tests as interventions before making a maximal novelty claim.

## Cross-cutting integration

A useful way to frame ASF against the literature is to say that prior work has already formalized several **pieces** of the agentic cycle, but usually in different languages and with different target objects.

| ASF concern | Main prior-art language | Best use in ASF positioning |
|:---|:---|:---|
| Perception and control as one loop | Active inference and control as inference \[Fri12c, Kap09, Fri15\] | Adopt as unifying backdrop, not as novelty claim |
| Resource-bounded policy formation | Bounded rationality and information costs \[Ort12c, Gen15\] | Adopt as principled math for abstraction and computational tradeoffs |
| Causal insufficiency and experimentation | Causal bandits, causal MDPs, intervention design \[Bar15, Zha16, Lee18b, Lee20\] | Main novelty-threat locus for exploration claims |
| Composite agency and coordination | Approximate information states, abstractions, decentralized control \[Sub20, Nay12, Con20, Abe16\] | Main novelty-threat locus for composition claims |
| Ambiguity and misaligned action in LLM agents | Empirical agent benchmarking \[Wan24b, Tan25, Pal25, Vij25\] | Evidence of phenomenon, not yet close formal anticipation |
| Developer-agent environments | SWE agents and verifiers \[Yan24b, Pan24, Gol25\] | Domain evidence for TST style transfer, not yet matching theory |

## Recommended claim language

The literature supports a disciplined split between adoption, differentiation, and novelty.

- **Adopted mathematics**
  - perception and control as inference \[Fri12c, Kap09\]
  - information-processing costs and abstraction \[Ort12c, Gen15\]
  - bounded-loss compression and decentralized coordination \[Sub20, Nay12, Con20, Abe16\]
- **Differentiated but not wholly new terrain**
  - causal exploration under hidden confounding \[Bar15, Zha16, Lee18b, Lee20\]
  - nested agency and boundary talk in Markov blanket traditions \[Par19, Kir18\]
- **Most defensible novelty claims on current evidence**
  - a no-go framing that ties latent causal insufficiency to forced inefficiency in agentic self-correction
  - a composition criterion that joins agent boundary claims to bounded predictive-control loss, especially if strong monotonicity is essential
  - an ambiguity-bounded architectural bias law for LLM style agents
  - a formal transfer of agentic-control mathematics into developer-agent software economics, though this remains least secure due to search coverage

## Bottom line

The prior art is strongest where ASF touches causal exploration, inference-based control, bounded rationality, and coarse-grained control abstractions \[Bar15, Zha16, Fri12c, Kap09, Ort12c, Sub20, Con20\]. Those are the places where claims should be narrowed and carefully differentiated. The prior art is much weaker on an explicit LLM architectural bias law and on formal developer-agent software economics \[Wan24b, Tan25, Pal25, Yan24b, Pan24, Vij25\]. If the literature review states those asymmetries clearly, ASF can be presented not as mathematics from nowhere, but as a framework that unifies known mathematics, sharpens several open seams between literatures, and appears to add genuinely new theory in a few targeted places.

---

## References

\[Fri12c\] K. J. Friston, S. Samothrakis, and P. Montague, “Active inference and agency: optimal control without cost functions,” *Biological Cybernetics*, vol. 106, pp. 523–541, Oct. 2012, doi: [10.1007/s00422-012-0512-8](https://doi.org/10.1007/s00422-012-0512-8).

\[Kap09\] H. Kappen, V. Gómez, and M. Opper, “Optimal control as a graphical model inference problem,” *Machine Learning*, vol. 87, pp. 159–182, Jan. 2009, doi: [10.1007/s10994-012-5278-7](https://doi.org/10.1007/s10994-012-5278-7).

\[Ort12c\] P. A. Ortega and D. A. Braun, “Thermodynamics as a theory of decision-making with information-processing costs,” Apr. 29, 2012. doi: [10.1098/rspa.2012.0683](https://doi.org/10.1098/rspa.2012.0683).

\[Fri15\] K. J. Friston, F. Rigoli, D. Ognibene, C. Mathys, T. H. B. FitzGerald, and G. Pezzulo, “Active inference and epistemic value,” *Cognitive Neuroscience*, vol. 6, pp. 187–214, Feb. 2015, doi: [10.1080/17588928.2015.1020053](https://doi.org/10.1080/17588928.2015.1020053).

\[Bar15\] E. Bareinboim, A. Forney, and J. Pearl, “Bandits with Unobserved Confounders: A Causal Approach,” *Neural Information Processing Systems*, pp. 1342–1350, Dec. 2015.

\[Zha16\] J. Zhang and E. Bareinboim, “Markov Decision Processes with Unobserved Confounders : A Causal Approach,” 2016.

\[Lee18b\] S. Lee and E. Bareinboim, “Structural Causal Bandits: Where to Intervene?” *Neural Information Processing Systems*, pp. 2573–2583, Dec. 2018.

\[Lee20\] S. Lee and E. Bareinboim, “Characterizing Optimal Mixed Policies: Where to Intervene and What to Observe,” *Neural Information Processing Systems*, vol. 33, 2020.

\[Sub20\] J. Subramanian, A. Sinha, R. Seraj, and A. Mahajan, “Approximate information state for approximate planning and reinforcement learning in partially observed systems,” *ArXiv*, vol. abs/2010.08843, Oct. 2020.

\[Nay12\] A. Nayyar, A. Mahajan, and D. Teneketzis, “Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach,” *IEEE Transactions on Automatic Control*, vol. 58, pp. 1644–1658, Sep. 2012, doi: [10.1109/TAC.2013.2239000](https://doi.org/10.1109/TAC.2013.2239000).

\[For17\] A. Forney, J. Pearl, and E. Bareinboim, “Counterfactual Data-Fusion for Online Reinforcement Learners,” *International Conference on Machine Learning*, pp. 1156–1164, Jul. 2017.

\[Abe16\] D. Abel, D. E. Hershkowitz, and M. Littman, “Near Optimal Behavior via Approximate State Abstraction,” *International Conference on Machine Learning*, pp. 2915–2923, Jun. 2016.

\[Tay08\] J. Taylor, D. Precup, and P. Panangaden, “Bounding Performance Loss in Approximate MDP Homomorphisms,” *Neural Information Processing Systems*, pp. 1649–1656, Dec. 2008.

\[Con20\] E. Congeduti, A. Mey, and F. Oliehoek, “Loss Bounds for Approximate Influence-Based Abstraction,” *ArXiv*, vol. abs/2011.01788, Nov. 2020, doi: [10.5555/3463952.3464001](https://doi.org/10.5555/3463952.3464001).

\[Wan24b\] W. Wang *et al.*, “Learning to Ask: When LLM Agents Meet Unclear Instruction,” *Conference on Empirical Methods in Natural Language Processing*, pp. 21773–21784, Aug. 2024, doi: [10.18653/v1/2025.emnlp-main.1104](https://doi.org/10.18653/v1/2025.emnlp-main.1104).

\[Yan24d\] <span class="nocase">S.-Y. Yang, chaeHun. Park, T. Kim, and J. Choo</span>, “Can Tool-augmented Large Language Models be Aware of Incomplete Conditions?” *ArXiv*, vol. abs/2406.12307, Jun. 2024, doi: [10.48550/arXiv.2406.12307](https://doi.org/10.48550/arXiv.2406.12307).

\[Tan25\] Y. Tang, T. Li, E. Li, C. J. Maddison, H. Dong, and Y. Ruan, “LM Agents May Fail to Act on Their Own Risk Knowledge,” *ArXiv*, vol. abs/2508.13465, Aug. 2025, doi: [10.48550/arXiv.2508.13465](https://doi.org/10.48550/arXiv.2508.13465).

\[Pal25\] A. Pal, T. Kitanovski, A. Liang, A. Potti, and M. Goldblum, “Knowing What You Know Is Not Enough: Large Language Model Confidences Don’t Align With Their Actions,” Nov. 17, 2025.

\[Liu24\] H. Liu, Z.-Y. Dou, Y. Wang, N. Peng, and Y. Yue, “Uncertainty Calibration for Tool-Using Language Agents,” *Conference on Empirical Methods in Natural Language Processing*, pp. 16781–16805, 2024, doi: [10.18653/v1/2024.findings-emnlp.978](https://doi.org/10.18653/v1/2024.findings-emnlp.978).

\[Gen15\] T. Genewein, F. Leibfried, J. Grau-Moya, and D. A. Braun, “Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle,” *Frontiers Robotics AI*, vol. 2, p. 27, Nov. 2015, doi: [10.3389/frobt.2015.00027](https://doi.org/10.3389/frobt.2015.00027).

\[Yan24b\] J. Yang *et al.*, “SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering,” *ArXiv*, vol. abs/2405.15793, May 2024, doi: [10.48550/arXiv.2405.15793](https://doi.org/10.48550/arXiv.2405.15793).

\[Pan24\] J. Pan *et al.*, “Training Software Engineering Agents and Verifiers with SWE-Gym,” *ArXiv*, vol. abs/2412.21139, Dec. 2024, doi: [10.48550/arXiv.2412.21139](https://doi.org/10.48550/arXiv.2412.21139).

\[Vij25\] S. Vijayvargiya, X. Zhou, A. Yerukola, M. Sap, and G. Neubig, “Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering,” Feb. 18, 2025.

\[Xia25b\] C. Xia, Y. Deng, S. Dunn, and L. Zhang, “Demystifying LLM-Based Software Engineering Agents,” *Proceedings of the ACM on Software Engineering*, vol. 2, pp. 801–824, Jun. 2025, doi: [10.1145/3715754](https://doi.org/10.1145/3715754).

\[Gol25\] A. Golubev *et al.*, “Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning,” *ArXiv*, vol. abs/2508.03501, Aug. 2025, doi: [10.48550/arXiv.2508.03501](https://doi.org/10.48550/arXiv.2508.03501).

\[Par19\] T. Parr, L. D. Costa, and K. J. Friston, “Markov blankets, information geometry and stochastic thermodynamics,” *Philosophical transactions. Series A, Mathematical, physical, and engineering sciences*, vol. 378, Dec. 2019, doi: [10.1098/rsta.2019.0159](https://doi.org/10.1098/rsta.2019.0159).

\[Kir18\] M. D. Kirchhoff, T. Parr, E. Palacios, K. J. Friston, and J. Kiverstein, “The Markov blankets of life: autonomy, active inference and the free energy principle,” *Journal of the Royal Society Interface*, vol. 15, Jan. 2018, doi: [10.1098/rsif.2017.0792](https://doi.org/10.1098/rsif.2017.0792).

\[Uga26\] S. Ugare and S. Chandra, “Agentic Code Reasoning,” Mar. 2026.
