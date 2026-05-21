# Prior art for AAT causal plan graphs

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which agent plans or strategies are modeled as causal DAGs with probabilistic AND/OR structure, where edges carry single-parameter credences for step success rather than full conditional probability tables. The core claim is that an active agent’s ordinary action-perception loop intrinsically generates interventional evidence in the Pearl Level-2 sense because taking an action breaks natural causal symmetry on the realized trajectory. The search should find antecedents for this claim as old as the literature allows, including papers that formally treat agent actions as interventions, manipulations, experiments, or information-gathering acts even if they do not explicitly phrase the point as a singular-trajectory Pearl `do()` claim. Relevant domains include causal reinforcement learning, causal decision theory, dual control and active experimentation, automated planning, decision theory, reliability engineering, operations research, and older cybernetic or control lineages when they are mathematically or conceptually close. Also find prior art for the claims that deep hierarchical strategies suffer a compounded depth cost or fragility penalty, including probabilistic decay across sequential conjunctive structure, delayed credit or evidence starvation in deeper plans, and maintenance cost for sustaining deeper strategy graphs; and that when sibling actions share a latent common cause, agents must augment the plan graph using a correlation hierarchy or related dependence structure to avoid failure under causal insufficiency. Count both exact mechanism matches and broader conceptual overlaps. Reliability lineages should count even when not framed as agent theory, including mathematically relevant work on probabilistic fault or success structures, common-cause failure, and related AND/OR dependency models. Exclude patents and other non-academic sources; exclude standard Bayesian networks that require full CPTs instead of single-parameter step credences; exclude standard MDP value iteration or deep RL planning that does not explicitly construct causal DAGs of the strategy; and exclude papers that merely invoke Pearl’s hierarchy without applying it to an agent’s internal plan validation. Prioritize the best antecedents for each pillar separately, then any papers that partially unify multiple pillars.

*Found 110 papers · May 21, 2026 · Estimated coverage of relevant papers: 62%*

## Summary of Results

The strongest prior art is split rather than monolithic: agent-generated action as intervention is explicit in Pearl’s action calculus \[1\], \[2\], \[3\] and in adaptive-control formulations that treat an agent’s own past actions in an I/O stream as causal interventions rather than observations \[4\], \[5\], while probabilistic AND/OR plan structure with compact stepwise success/failure parameters appears most clearly in planning and reliability lineages \[6\], \[7\], \[8\], \[9\], \[10\], \[11\].

#### Interventional agency and sequential plans

- **Actions vs. observations:** causal conditioning `do(.)` \[1\], local surgery \[2\], and sequential plan evaluation under hidden variables \[3\].
- **Decision-theoretic counterparts:** causal influence diagrams and decisions as causes \[12\], \[13\], \[14\], \[15\].
- **Active control as experiment:** dual control and probing actions as information-gathering control \[16\], \[17\], \[18\], \[19\].
- **Agent-internal treatment of self-actions:** Bayesian control rule papers are the cleanest direct antecedent for “my own actions are interventions” in ordinary interaction \[4\], \[5\].

#### AND/OR strategy graphs, depth cost, and dependence

- **Compact probabilistic conjunctive/disjunctive structure:** AND/OR search and plan evaluation with per-step uncertainty \[6\], \[7\], \[11\].
- **Depth fragility:** success decays across sequential conjunctive structure; errors/penalties accumulate with deeper AND branches \[7\], \[11\], with close mathematical analogues in phased-mission and dynamic fault analysis \[20\], \[21\].
- **Latent shared causes:** common-cause and dependent-failure modeling is the main antecedent for augmenting naive AND/OR graphs with correlation hierarchy or dependency structure \[22\], \[23\], \[24\], \[25\], \[26\], \[27\], \[28\].

## Paper Catalog (110 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2008 | 7.2 | A Minimum Relative Entropy Principle for Learning and Acting ([link](https://doi.org/10.1613/JAIR.3062)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 2 | 2009 | 1.4 | A Bayesian Rule for Adaptive Control based on Causal Interventions ([link](https://doi.org/10.2991/AGI.2010.39)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 3 | 1994 | 4.1 | A Probabilistic Calculus of Actions ([link](https://doi.org/10.1016/B978-1-55860-332-5.50062-6)) | J. Pearl | ArXiv |
| 4 | 1994 | 0.2 | From Imaging and Stochastic Control to a Calculus of Actions ([link](https://www.semanticscholar.org/paper/868abc852a46c8448c74c28da7781c5263a2da19)) | J. Pearl |  |
| 5 | 1995 | 6.8 | Probabilistic evaluation of sequential plans from causal models with hidden variables ([link](https://www.semanticscholar.org/paper/afff0ccdca925f0c48bb836c291c84d1ce14156f)) | J. Pearl and J. Robins | Conference on Uncertainty in Artificial Intelligence |
| 6 | 1995 | 0.2 | Action as a Local Surgery ([link](https://www.semanticscholar.org/paper/39eb2f1af69818dd9a21bc7316dedb5a2e63ed6e)) | J. Pearl |  |
| 7 | 2008 | 2.7 | Identifying Dynamic Sequential Plans ([link](https://www.semanticscholar.org/paper/f194a45fb846441d013a560970f79d96c0912851)) | Jin Tian | Conference on Uncertainty in Artificial Intelligence |
| 8 | 2021 |  | Execution Ordering in AND/OR Graphs with Failure Probabilities ([link](https://doi.org/10.1609/socs.v3i1.18246)) | Priyankar Ghosh, P. Chakrabarti, and P. Dasgupta | Symposium on Combinatorial Search |
| 9 | 1995 | 4.5 | Decision-Theoretic Foundations for Causal Reasoning ([link](https://doi.org/10.1613/JAIR.202)) | D. Heckerman and Ross D. Shachter | J. Artif. Intell. Res. |
| 10 | 2006 | 0.5 | Using Interaction to Compute Better Probability Estimates in Plan Graphs ([link](https://www.semanticscholar.org/paper/0a535bf2697982ff8a6febef7ecff8087a7ee7b6)) | D. Bryce and David E. Smith |  |
| 11 | 2010 | 7.1 | Identifying the consequences of dynamic treatment strategies: A decision-theoretic overview ([link](https://doi.org/10.1214/10-SS081)) | A. Dawid and V. Didelez | ArXiv |
| 12 | 2005 | 0.5 | RELIABILITY MODELING AND ANALYSIS OF COMPLEX HIERARCHICAL SYSTEMS ([link](https://doi.org/10.1142/S0218539305001963)) | L. Xing | International Journal of Reliability, Quality and Safety Engineering |
| 13 | 1994 | 1.4 | A Decision-based View of Causality ([link](https://doi.org/10.1016/B978-1-55860-332-5.50043-2)) | D. Heckerman and Ross D. Shachter | ArXiv |
| 14 | 1983 |  | Optimal searches from and ornodes ([link](https://www.semanticscholar.org/paper/24443bab1120fd3ab503d1375ef605f20b21f02f)) | J. Barnett | International Joint Conference on Artificial Intelligence |
| 15 | 2021 | 2.5 | Causal Markov Decision Processes: Learning Good Interventions Efficiently ([link](https://www.semanticscholar.org/paper/7990ed58591c23dbef01bc8010220d20c13156d2)) | Yangyi Lu, A. Meisami, and Ambuj Tewari | ArXiv |
| 16 | 1997 | 0.1 | Development and Evaluation of Strategic Plans ([link](https://www.semanticscholar.org/paper/0034a1e6711a52dca8743e6e47aeeae38ac984aa)) | T. Cazenave and Regis Moneret |  |
| 17 | 1981 |  | Effect of sympathetic failures on redundant system reliability ([link](https://www.semanticscholar.org/paper/7131745b5fbb0820f7f1326919976f56386a6dc9)) | I. Papazoglou and S. Mitra |  |
| 18 | 2002 | 12 | Influence Diagrams for Causal Modelling and Inference ([link](https://doi.org/10.1111/j.1751-5823.2002.tb00354.x)) | A. Dawid | International Statistical Review |
| 19 | 2002 | 1.5 | Treatment of general dependencies in system fault-tree and risk analysis ([link](https://doi.org/10.1109/TR.2002.801848)) | J. Vaurio | IEEE Trans. Reliab. |
| 20 | 2016 | 5.1 | Markov Decision Processes with Unobserved Confounders : A Causal Approach ([link](https://www.semanticscholar.org/paper/69c68d804e7c052665d5b4049c0d9c9d8baa11c0)) | Junzhe Zhang and E. Bareinboim |  |
| 21 | 2008 | 0.5 | Identifying Optimal Sequential Decisions ([link](https://www.semanticscholar.org/paper/c43385a150a13bb0d06787050e2b9c2173b617cb)) | P. Dawid and V. Didelez | Conference on Uncertainty in Artificial Intelligence |
| 22 | 1997 | 7.6 | A modular approach for analyzing static and dynamic fault trees ([link](https://doi.org/10.1109/RAMS.1997.571665)) | R. Gulati and J. Dugan | Annual Reliability and Maintainability Symposium |
| 23 | 1989 | 1.4 | A model for system reliability with common-cause failures ([link](https://doi.org/10.1109/24.46447)) | L. Page and J. Perry | IEEE Transactions on Reliability |
| 24 | 1994 | 2.2 | Action Networks: A Framework for Reasoning about Actions and Change under Uncertainty ([link](https://doi.org/10.1016/B978-1-55860-332-5.50023-7)) | Adnan Darwiche and M. Goldszmidt | Conference on Uncertainty in Artificial Intelligence |
| 25 | 2024 | 0.9 | Why Online Reinforcement Learning is Causal ([link](https://doi.org/10.48550/arXiv.2403.04221)) | Oliver Schulte and Pascal Poupart | ArXiv |
| 26 | 2009 | 2.2 | Incorporating Common-Cause Failures Into the Modular Hierarchical Systems Analysis ([link](https://doi.org/10.1109/TR.2008.2011855)) | L. Xing, A. Shrestha, L. Meshkat, and Wendai Wang | IEEE Transactions on Reliability |
| 27 | 1998 | 4.0 | An implicit method for incorporating common-cause failures in system analysis ([link](https://doi.org/10.1109/24.722285)) | J. Vaurio | IEEE Transactions on Reliability |
| 28 | 1994 | 8.6 | Counterfactual Probabilities: Computational Methods, Bounds and Applications ([link](https://doi.org/10.1016/B978-1-55860-332-5.50011-0)) | Alexander Balke and J. Pearl | Conference on Uncertainty in Artificial Intelligence |
| 29 | 1994 | 0.6 | Symbolic Causal Networks for Reasoning about Actions and Plans ([link](https://www.semanticscholar.org/paper/f3552ebb16a70b8f19ea332468115efa63bcc7c5)) | Adnan Darwiche and J. Pearl |  |
| 30 | 1989 |  | Dependent Failure Modelling by Fault Tree Technique ([link](https://doi.org/10.1007/978-94-017-0629-2_9)) | S. Contini |  |
| 31 | 1978 | 0.2 | Comparison of three methods for the quantitative analysis of common cause failures ([link](https://www.semanticscholar.org/paper/27f9b82b00388babf1d0bdd2aab7b3bb06332b94)) | K. N. Fleming and P. Raabe |  |
| 32 | 1994 | 8.5 | Probabilistic Planning with Information Gathering and Contingent Execution ([link](https://www.semanticscholar.org/paper/5205d4ab167f83c6f1098cc45e04249e8314db5d)) | Denise Draper, S. Hanks, and Daniel S. Weld | International Conference on Artificial Intelligence Planning Systems |
| 33 | 2025 |  | When Should Reinforcement Learning Use Causal Reasoning? ([link](https://www.semanticscholar.org/paper/1ea0a4c86eaf441a6aafe6b52213985cd06304d9)) | Oliver Schulte and Pascal Poupart | Trans. Mach. Learn. Res. |
| 34 | 2021 | 16 | Shaking the foundations: delusions in sequence models for interaction and control ([link](https://www.semanticscholar.org/paper/bc031724d5323b294e22a895977928b79fbe8a29)) | Pedro A. Ortega et al. | ArXiv |
| 35 | 1994 | 1.6 | A Probablistic Model of Action for Least-Commitment Planning with Information Gathering ([link](https://doi.org/10.1016/B978-1-55860-332-5.50028-6)) | Denise Draper, S. Hanks, and Daniel S. Weld | Conference on Uncertainty in Artificial Intelligence |
| 36 | 2016 | 6.1 | A general cause based methodology for analysis of common cause and dependent failures in system risk and reliability assessments ([link](https://doi.org/10.1016/j.ress.2015.06.007)) | A. O’Connor and A. Mosleh | Reliab. Eng. Syst. Saf. |
| 37 | 2007 | 2.4 | Reliability analysis of hierarchical computer-based systems subject to common-cause failures ([link](https://doi.org/10.1016/j.ress.2006.04.010)) | L. Xing, L. Meshkat, and S. Donohue | Reliab. Eng. Syst. Saf. |
| 38 | 2020 | 9.9 | Decision-theoretic foundations for statistical causality ([link](https://doi.org/10.1515/jci-2020-0008)) | P. Dawid | Journal of Causal Inference |
| 39 | 1994 | 4.0 | An Algorithm for Probabilistic Least-Commitment Planning ([link](https://www.semanticscholar.org/paper/3288fce6e3b69b2f03d323f7ac20acaece5a55ef)) | N. Kushmerick, S. Hanks, and Daniel S. Weld | AAAI Conference on Artificial Intelligence |
| 40 | 1993 | 3.8 | From Conditional Oughts to Qualitative Decision Theory ([link](https://doi.org/10.1016/B978-1-4832-1451-1.50006-8)) | J. Pearl | Conference on Uncertainty in Artificial Intelligence |
| 41 | 1976 | 2.1 | On the Quantitative Analysis of Priority-AND Failure Logic ([link](https://doi.org/10.1109/TR.1976.5220025)) | J. B. Fussell, E. F. Aber, and R. Rahl | IEEE Transactions on Reliability |
| 42 | 1994 | 4.6 | Conditioning and Intervening ([link](https://doi.org/10.1093/bjps/45.4.1001)) | Christopher Meek and C. Glymour | The British Journal for the Philosophy of Science |
| 43 | 2013 | 4.0 | Generalized Thompson sampling for sequential decision-making and causal inference ([link](https://doi.org/10.1186/2194-3206-2-2)) | Pedro A. Ortega and Daniel A. Braun | Complex Adaptive Systems Modeling |
| 44 | 2016 | 19 | Causal Bandits: Learning Good Interventions via Causal Inference ([link](https://www.semanticscholar.org/paper/4d9f776cb5bf419a8ff1c1a65e54141ddc976ec1)) | Finnian Lattimore, Tor Lattimore, and Mark D. Reid | Neural Information Processing Systems |
| 45 | 1995 | 14 | An Algorithm for Probabilistic Planning ([link](https://doi.org/10.1016/0004-3702(94%2900087-H)) | N. Kushmerick, S. Hanks, and Daniel S. Weld | Artif. Intell. |
| 46 | 2010 | 2.3 | Algebraic modelling of Dynamic Fault Trees, contribution to qualitative and quantitative analysis ([link](https://www.semanticscholar.org/paper/0ea912813d4c7f5840d40458d477268d44dd62d6)) | G. Merle |  |
| 47 | 1994 | 1.6 | Epsilon-Safe Planning ([link](https://doi.org/10.1016/B978-1-55860-332-5.50037-7)) | R. Goldman and M. Boddy | Conference on Uncertainty in Artificial Intelligence |
| 48 | 2020 | 5.8 | Characterizing Optimal Mixed Policies: Where to Intervene and What to Observe ([link](https://www.semanticscholar.org/paper/93ac56f4431cb7d0d3389887c56817dab246967d)) | Sanghack Lee and E. Bareinboim | Neural Information Processing Systems |
| 49 | 1996 | 0.9 | A Logic of Time, Chance, and Action for Representing Plans ([link](https://doi.org/10.1016/0004-3702(94%2900070-0)) | P. Haddawy | Artif. Intell. |
| 50 | 2006 | 0.3 | Using Correlation to Compute Better Probability Estimates in Plan Graphs ([link](https://www.semanticscholar.org/paper/d08bcdb673651830d662a6b75918cefb20ee9554)) | D. Bryce and David E. Smith |  |
| 51 | 2009 | 5.1 | Decision makers conceive of their choices as interventions. ([link](https://doi.org/10.1037/a0014585)) | Y. Hagmayer and S. Sloman | Journal of experimental psychology. General |
| 52 | 2024 | 7.7 | Fault Tree Analysis Including Component Dependencies ([link](https://doi.org/10.1109/TR.2023.3264943)) | S. Tolo and J. Andrews | IEEE Transactions on Reliability |
| 53 | 2006 | 0.1 | An Efficient Approach for the Reliability Analysis of Phased-Mission Systems with Dependent Failures ([link](https://doi.org/10.1115/1.802442.paper3)) | L. Xing, L. Meshkat, and S. Donahue |  |
| 54 | 2018 | 15 | Structural Causal Bandits: Where to Intervene? ([link](https://www.semanticscholar.org/paper/615b2c912cb6f17ab2f5b15a44b06d64147a5ed5)) | Sanghack Lee and E. Bareinboim | Neural Information Processing Systems |
| 55 | 2017 | 43 | An overview of fault tree analysis and its application in model based dependability analysis ([link](https://doi.org/10.1016/j.eswa.2017.01.058)) | Sohag Kabir | Expert Syst. Appl. |
| 56 | 2000 | 0.2 | Dependency modelling using fault-tree and cause-consequence analysis ([link](https://www.semanticscholar.org/paper/75760a38c2a4b06b58fa5d31ead3793872316006)) | L. M. Ridley |  |
| 57 | 2012 | 0.6 | Assessing dynamic treatment strategies ([link](https://doi.org/10.1002/9781119945710.CH8)) | C. Berzuini, A. Dawid, V. Didelez, P. Dawid, and L. Bernardinelli |  |
| 58 | 2002 | 3.1 | Dependability analysis of systems with on-demand and active failure modes, using dynamic fault trees ([link](https://doi.org/10.1109/TR.2002.1011531)) | L. Meshkat, J. Dugan, and J. Andrews | IEEE Trans. Reliab. |
| 59 | 2005 | 1.1 | Describing and Valuing Interventions That Observe or Control Decision Situations ([link](https://doi.org/10.1287/deca.1050.0045)) | D. Matheson and J. Matheson | Decis. Anal. |
| 60 | 2011 | 1.3 | A Unified Framework for Resource-Bounded Autonomous Agents Interacting with Unknown Environments ([link](https://doi.org/10.17863/CAM.14005)) | Pedro A. Ortega |  |
| 61 | 1972 | 2.3 | NEW METHODOLOGY FOR OBTAINING CUT SETS FOR FAULT TREES. ([link](https://www.semanticscholar.org/paper/7ed80b7c4667c80cad01d91e4e0fc96cbd3d4562)) | J. B. Fussell and W. Vesely | Transactions of the American Nuclear Society |
| 62 | 1987 | 37 | Fault Tree Handbook ([link](https://www.semanticscholar.org/paper/c0f501211a34b13356a0cd43f2ebd0050abd5e10)) | W. E. Vesely, F. Goldberg, N. Roberts, and D. Haasl |  |
| 63 | 2022 | 3.5 | Causal Discovery and Reinforcement Learning: A Synergistic Integration ([link](https://www.semanticscholar.org/paper/a45df3efbd472d4d43ddc4072c61f7f674981ac6)) | Arquímides Méndez-Molina, E. Morales, and L. Sucar | European Workshop on Probabilistic Graphical Models |
| 64 | 1977 | 3.3 | Reliability and Fault Tree Analysis ([link](https://doi.org/10.2307/1267714)) | R. Barlow, J. B. Fussell, and N. Singpurwalla | Technometrics |
| 65 | 2005 | 0.4 | Aspects of casual inference in a non-counterfactual framework. ([link](https://www.semanticscholar.org/paper/19ad06c43ffb0105811a86b9456b510324419d23)) | S. Geneletti |  |
| 66 | 1996 | 2.5 | Decision-Theoretic Troubleshooting: A Framework for Repair and Experiment ([link](https://doi.org/10.1007/978-1-4615-5089-1_15)) | J. Breese and D. Heckerman | ArXiv |
| 67 | 1994 | 6.3 | Probabilistic Evaluation of Counterfactual Queries ([link](https://doi.org/10.1145/3501714.3501733)) | Alexander Balke and J. Pearl | Probabilistic and Causal Inference |
| 68 | 1993 | 4.3 | Fault trees and Markov models for reliability analysis of fault-tolerant digital systems ([link](https://doi.org/10.1016/0951-8320(93%2990005-J)) | J. Dugan, S. Bavuso, and M. Boyd | Reliability Engineering & System Safety |
| 69 | 2020 |  | Towards intervention-centric causal reasoning in learning agents ([link](https://www.semanticscholar.org/paper/e450e2febab59255c6d39460429a674b291e6fae)) | B. Lansdell | ArXiv |
| 70 | 1982 | 1.5 | Causal Decision Theory ([link](https://doi.org/10.2307/2026547)) | B. Skyrms | The Journal of Philosophy |
| 71 | 2003 | 1.8 | An overview of the phase-modular fault tree approach to phased mission system analysis ([link](https://www.semanticscholar.org/paper/089479ccc615413a3da66a63ca875e1e1223982f)) | Leila Meshkat |  |
| 72 | 1996 | 2.5 | Causation, Action and Counterfactuals ([link](https://doi.org/10.1007/978-94-017-0487-8_18)) | J. Pearl | Theoretical Aspects of Rationality and Knowledge |
| 73 | 2025 | 1.7 | Modelling complexity in system safety: generalizing the D2T2 methodology ([link](https://doi.org/10.48550/arXiv.2510.17351)) | S. Tolo and J. Andrews | Reliab. Eng. Syst. Saf. |
| 74 | 2013 | 0.5 | Progressive heuristic search for probabilistic planning based on interaction estimates ([link](https://doi.org/10.1111/exsy.12037)) | Yolanda E-Martín, M. Rodríguez-Moreno, and David E. Smith | Expert Systems |
| 75 | 2019 |  | A Guiding Principle for Causal Decision Problems ([link](https://www.semanticscholar.org/paper/de69caf350e7a52882943d326c718910cf5d8247)) | Mauricio Gonzalez-Soto, L. Sucar, and Hugo Jair Escalante | ArXiv |
| 76 | 1984 | 6.2 | Causal Decision Theory ([link](https://doi.org/10.1086/psaprocbienmeetp.1984.2.192504)) | E. Eells | PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association |
| 77 | 1999 | 5.8 | Probabilistic Planning in the Graphplan Framework ([link](https://doi.org/10.1007/10720246_25)) | Avrim Blum and J. Langford | European Conference on Planning |
| 78 | 1975 | 0.4 | Computerized Fault Tree Analysis: TREEL and MICSUP. ([link](https://www.semanticscholar.org/paper/26dc0922ed8118378ba3eef33bc46320a3d80059)) | P. Pande, Mitchell Spector, and P. Chatterjee |  |
| 79 | 2024 |  | Characterising Interventions in Causal Games ([link](https://doi.org/10.48550/arXiv.2406.09318)) | Manuj Mishra, James Fox, and Michael Wooldridge | Conference on Uncertainty in Artificial Intelligence |
| 80 | 2004 |  | Causal identification in design networks ([link](https://www.semanticscholar.org/paper/dbf561769baf139f69157aa75a1f5c1855fda293)) | R. Monroy, G. Arroyo-Figueroa, L. Sucar, and H. Sossa |  |
| 81 | 2021 | 0.2 | Dependency-aware Fault Tree Analysis ([link](https://doi.org/10.1109/icsrs53853.2021.9660639)) | Alexander Prohaska | 2021 5th International Conference on System Reliability and Safety (ICSRS) |
| 82 | 2010 |  | A Minimum Relative Entropy Controller for Undiscounted Markov Decision Processes ([link](https://www.semanticscholar.org/paper/64d315f5055eaa6003be2f7ce15a49a1ebd24860)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 83 | 1993 | 6.6 | \[Bayesian Analysis in Expert Systems\]: Comment: Graphical Models, Causality and Intervention ([link](https://doi.org/10.1214/SS/1177010894)) | J. Pearl | Statistical Science |
| 84 | 1993 |  | CSM-184 - Planning and Execution using Partial Decision Trees ([link](https://www.semanticscholar.org/paper/35c6ca88165fc68e73f9705100b337a71046eec7)) | S. Steel and Lee Ho |  |
| 85 | 1977 | 0.1 | A modular approach to fault tree and reliability analysis ([link](https://www.semanticscholar.org/paper/086ac506b0311116302fedd7f4ed06298aee3e94)) | J. Olmos and Wolf Lothar | Transactions of the American Nuclear Society |
| 86 | 1988 |  | Decision, probability, and utility: Causal decision theory ([link](https://doi.org/10.1017/CBO9780511609220.023)) | David Lewis |  |
| 87 | 2006 | 2.4 | Concurrent Probabilistic Planning in the Graphplan Framework ([link](https://www.semanticscholar.org/paper/58d299cff784301523725f9887516ee0352bb7ab)) | Iain Little and S. Thiébaux | International Conference on Automated Planning and Scheduling |
| 88 | 2018 |  | Condition Fault Tree: An Extension of Traditional Fault Tree to Handle Uncertainty ([link](https://doi.org/10.1115/ICONE26-81243)) | Zhenxu Zhou and Qin Zhang | Volume 9: Student Paper Competition |
| 89 | 1995 | 0.3 | Exploiting System Hierarchy to Compute Repair Plans in Probabilistic Model-Based Diagnosis ([link](https://www.semanticscholar.org/paper/1edbdab64c7948fd016b28fb53aa65774ba70349)) | S. Srinivas and E. Horvitz | Conference on Uncertainty in Artificial Intelligence |
| 90 | 2005 | 0.5 | Causal Models of Decision Making: Choice as Intervention ([link](https://www.semanticscholar.org/paper/5eb41804b55ae77657654354016ac311c13d28b5)) | Y. Hagmayer and S. Sloman |  |
| 91 | 1997 |  | Handling Contingency Selection Using Goal Values ([link](https://www.semanticscholar.org/paper/f4340e4df0e9223eb710e9032fe7d31766ab074d)) | Nilufer Onder and M. Pollack |  |
| 92 | 2013 | 0.7 | A Formal Treatment of Sequential Ignorability ([link](https://doi.org/10.1007/s12561-014-9110-8)) | A. Dawid and Panayiota Constantinou | Statistics in Biosciences |
| 93 | 2010 | 2.6 | Observing and Intervening: Rational and Heuristic Models of Causal Decision Making ([link](https://doi.org/10.2174/1874350101003010119)) | Björn Meder, Tobias Gerstenberg, Y. Hagmayer, and Michael R. Waldmann | The Open Psychology Journal |
| 94 | 2010 | 0.1 | Convergence of Bayesian Control Rule ([link](https://www.semanticscholar.org/paper/a7f004a1ca2f9de8f2fe9c8adbef487ccf0b1415)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 95 | 1961 | 2.0 | DUAL CONTROL THEORY, IV ([link](https://www.semanticscholar.org/paper/bc1cf3fd03b7df35f7d31e228c99bdd557f91bc8)) | A. Feldbaum |  |
| 96 | 1994 | 0.0 | Robust Planning in Uncertain Environments ([link](https://doi.org/10.1016/B978-1-55860-332-5.50063-8)) | Stephen G. Pimentel and Lawrence M. Brem | Conference on Uncertainty in Artificial Intelligence |
| 97 | 1977 | 0.6 | FRANTIC II: a computer code for time dependent unavailability analysis ([link](https://www.semanticscholar.org/paper/6b5f8676c15b6c34c00dd6118fdb99f9c2d436ea)) | W. Vesely et al. |  |
| 98 | 1981 | 3.5 | Stochastic dynamic programming: Caution and probing ([link](https://doi.org/10.1109/TAC.1981.1102793)) | Y. Bar-Shalom | IEEE Transactions on Automatic Control |
| 99 | 1973 | 3.2 | Wide-sense adaptive dual control for nonlinear stochastic systems ([link](https://doi.org/10.1109/TAC.1973.1100238)) | E. Tse, Y. Bar-Shalom, and L. Meier | IEEE Transactions on Automatic Control |
| 100 | 1966 | 16 | Information Value Theory ([link](https://doi.org/10.1109/TSSC.1966.300074)) | R. Howard | IEEE Trans. Syst. Sci. Cybern. |
| 101 | 2017 | 3.3 | A Unified Bellman Equation for Causal Information and Value in Markov Decision Processes ([link](https://www.semanticscholar.org/paper/f5f235579f02d9fad0d18cd19795de7e45c2f8eb)) | Stas Tiomkin and Naftali Tishby | ArXiv |
| 102 | 2020 | 3.0 | Resolving Spurious Correlations in Causal Models of Environments via Interventions ([link](https://www.semanticscholar.org/paper/98b49ec25f7b8526d512efe7bb8a81ab8ef7be17)) | S. Volodin, Nevan Wichers, and J. Nixon | ArXiv |
| 103 | 2000 | 6.0 | Survey of adaptive dual control methods ([link](https://doi.org/10.1049/IP-CTA:20000107)) | N. Filatov and H. Unbehauen |  |
| 104 | 1974 | 7.7 | Dual effect, certainty equivalence, and separation in stochastic control ([link](https://doi.org/10.1109/TAC.1974.1100635)) | Y. Bar-Shalom and E. Tse | IEEE Transactions on Automatic Control |
| 105 | 2015 | 6.4 | Dual Control for Approximate Bayesian Reinforcement Learning ([link](https://www.semanticscholar.org/paper/d5c48f3c6b1147c411957a06538e12fced2d60d5)) | Edgar D. Klenske and Philipp Hennig | J. Mach. Learn. Res. |
| 106 | 1974 | 0.6 | Adaptive Dual Control Methods ([link](https://www.semanticscholar.org/paper/b754a3c671772c52b9ae512fa9c9ff14fa6a1bd4)) | E. Tse |  |
| 107 | 2002 | 2.2 | Adaptive dual control ([link](https://www.semanticscholar.org/paper/9c1fe4c9791bab12e3a494664a71acd442c496af)) | B. Wittenmark |  |
| 108 | 1982 | 0.2 | A dual approach to Bayesian inference and adaptive control ([link](https://doi.org/10.1007/BF00133976)) | L. Tesfatsion | Theory and Decision |
| 109 | 2015 | 61 | Active inference and epistemic value ([link](https://doi.org/10.1080/17588928.2015.1020053)) | Karl J. Friston et al. | Cognitive Neuroscience |
| 110 | 1986 | 21 | AND/OR graph representation of assembly plans ([link](https://doi.org/10.1109/70.54734)) | L. H. D. Mello and A. Sanderson | IEEE Trans. Robotics Autom. |

### Paper Details

1\. · 100% match · 2008 · 7.2 cit/yr\
**A Minimum Relative Entropy Principle for Learning and Acting** ([link](https://doi.org/10.1613/JAIR.3062))\
Pedro A. Ortega and Daniel A. Braun\
*ArXiv* · Oct 20, 2008 · 126 citations

> This paper proposes a method to construct an adaptive agent that is universal with respect to a given class of experts, where each expert is designed specifically for a particular environment. This adaptive control problem is formalized as the problem of minimizing the relative entropy of the adaptive agent from the expert that is most suitable for the unknown environment. If the agent is a passive observer, then the optimal solution is the well-known Bayesian predictor. However, if the agent is active, then its past actions need to be treated as causal interventions on the I/O stream rather than normal probability conditions. Here it is shown that the solution to this new variational problem is given by a stochastic controller called the Bayesian control rule, which implements adaptive behavior as a mixture of experts. Furthermore, it is shown that under mild assumptions, the Bayesian control rule converges to the control law of the most suitable expert.

------------------------------------------------------------------------

2\. · 100% match · 2009 · 1.4 cit/yr\
**A Bayesian Rule for Adaptive Control based on Causal Interventions** ([link](https://doi.org/10.2991/AGI.2010.39))\
Pedro A. Ortega and Daniel A. Braun\
*ArXiv* · Nov 26, 2009 · 23 citations

> Explaining adaptive behavior is a central problem in artificial intelligence research. Here we formalize adaptive agents as mixture distributions over sequences of inputs and outputs (I/O). Each distribution of the mixture constitutes a ‘possible world’, but the agent does not know which of the possible worlds it is actually facing. The problem is to adapt the I/O stream in a way that is compatible with the true world. A natural measure of adaptation can be obtained by the KullbackLeibler (KL) divergence between the I/O distribution of the true world and the I/O distribution expected by the agent that is uncertain about possible worlds. In the case of pure input streams, the Bayesian mixture provides a well-known solution for this problem. We show, however, that in the case of I/O streams this solution breaks down, because outputs are issued by the agent itself and require a different probabilistic syntax as provided by intervention calculus. Based on this calculus, we obtain a Bayesian control rule that allows modeling adaptive behavior with mixture distributions over I/O streams. This rule might allow for a novel approach to adaptive control based on a minimum KLprinciple.

------------------------------------------------------------------------

3\. · 100% match · 1994 · 4.1 cit/yr\
**A Probabilistic Calculus of Actions** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50062-6))\
J. Pearl\
*ArXiv* · Jul 29, 1994 · 130 citations

> We present a symbolic machinery that admits both probabilistic and causal information about a given domain and produces probabilistic statements about the effect of actions and the impact of observations. The calculus admits two types of conditioning operators: ordinary Bayes conditioning, P(y\|X = x), which represents the observation X = x, and causal conditioning, P(y\|do(X = x)), read the probability of Y = y conditioned on holding X constant (at x) by deliberate action. Given a mixture of such observational and causal sentences, together with the topology of the causal graph, the calculus derives new conditional probabilities of both types, thus enabling one to quantify the effects of actions (and policies) from partially specified knowledge bases, such as Bayesian networks in which some conditional probabilities may not be available.

------------------------------------------------------------------------

4\. · 100% match · 1994 · 0.2 cit/yr\
**From Imaging and Stochastic Control to a Calculus of Actions** ([link](https://www.semanticscholar.org/paper/868abc852a46c8448c74c28da7781c5263a2da19))\
J. Pearl\
7 citations

> This paper highlights relationships among stochastic control theory, Lewis’ notion of “imaging”, and the representation of actions in AI systems. We show that the language of causal graphs offers a practical solution to the frame problem and its two satellites: the ramification and concurrency problems. Finally, we present a symbolic machinery that admits both probabilistic and causal information and produces probabilistic statements about the effect of actions and the impact of observations.

------------------------------------------------------------------------

5\. · 100% match · 1995 · 6.8 cit/yr\
**Probabilistic evaluation of sequential plans from causal models with hidden variables** ([link](https://www.semanticscholar.org/paper/afff0ccdca925f0c48bb836c291c84d1ce14156f))\
J. Pearl and J. Robins\
*Conference on Uncertainty in Artificial Intelligence* · Aug 18, 1995 · 208 citations

> The paper concerns the probabilistic evaluation of plans in the presence of unmeasured variables, each plan consisting of several concurrent or sequential actions. We establish a graphical criterion for recognizing when the effects of a given plan can be predicted from passive observations on measured variables only. When the criterion is satisfied, a closed-form expression is provided for the probability that the plan will achieve a specified goal.

------------------------------------------------------------------------

6\. · 100% match · 1995 · 0.2 cit/yr\
**Action as a Local Surgery** ([link](https://www.semanticscholar.org/paper/39eb2f1af69818dd9a21bc7316dedb5a2e63ed6e))\
J. Pearl\
5 citations

> What gives us the audacity to expect that actions should have neat and compact representations? Why did the authors of STRIPS \[Fikes & Nilsson, 1971\] and BURIDAN \[Kushmerick et al., 1993\] believe they could get away with such short specification for actions? Whether we take the probabilistic paradigm that actions are transformations from probability distributions to probability distributions, or the deterministic paradigm that actions are transformations from states to states, such transformations could in principle be infinitely complex. Yet, in practice, people teach each other rather quickly what actions normally do to the world, people predict the consequences of any given action without much hustle, and AI researchers are writing languages for actions as if it is a God given truth that action representation should be compact, elegant and meaningful. Why? The paradigm I wish to explore in this paper is that these expectations are not only justified but, mainly, that once we understand the justification, we will be in better shape to craft effective representations for actions.

------------------------------------------------------------------------

7\. · 100% match · 2008 · 2.7 cit/yr\
**Identifying Dynamic Sequential Plans** ([link](https://www.semanticscholar.org/paper/f194a45fb846441d013a560970f79d96c0912851))\
Jin Tian\
*Conference on Uncertainty in Artificial Intelligence* · Jul 9, 2008 · 49 citations

> We address the problem of identifying dynamic sequential plans in the framework of causal Bayesian networks, and show that the problem is reduced to identifying causal effects, for which there are complete identification algorithms available in the literature.

------------------------------------------------------------------------

8\. · 100% match · 2021\
**Execution Ordering in AND/OR Graphs with Failure Probabilities** ([link](https://doi.org/10.1609/socs.v3i1.18246))\
Priyankar Ghosh, P. Chakrabarti, and P. Dasgupta\
*Symposium on Combinatorial Search* · Aug 20, 2021 · 0 citations

> In this paper we consider finding solutions for problems represented using AND/OR graphs, which contain tasks that can fail when executed. In our  setting each node represent an atomic task which is associated with a failure probability and a rollback penalty. This paper reports the following contributions - (a) an algorithm for finding the optimal ordering of the atomic tasks in a given solution graph which minimizes the expected penalty, (b) an algorithm for finding the optimal ordering in the presence of user defined ordering constraints, and (c) a counter example showing the lack of optimal substructure property for the problem of finding the solution graph having minimum expected penalty, and a pseudo-polynomial algorithm for finding the solution graph with minimum expected penalty.

------------------------------------------------------------------------

9\. · 100% match · 1995 · 4.5 cit/yr\
**Decision-Theoretic Foundations for Causal Reasoning** ([link](https://doi.org/10.1613/JAIR.202))\
D. Heckerman and Ross D. Shachter\
*J. Artif. Intell. Res.* · Jun 1, 1995 · 139 citations

> We present a definition of cause and effect in terms of decision-theoretic primitives and thereby provide a principled foundation for causal reasoning. Our definition departs from the traditional view of causation in that causal assertions may vary with the set of decisions available. We argue that this approach provides added clarity to the notion of cause. Also in this paper, we examine the encoding of causal relationships in directed acyclic graphs. We describe a special class of influence diagrams, those in canonical form, and show its relationship to Pearl’s representation of cause and effect. Finally, we show how canonical form facilitates counterfactual reasoning.

------------------------------------------------------------------------

10\. · 100% match · 2006 · 0.5 cit/yr\
**Using Interaction to Compute Better Probability Estimates in Plan Graphs** ([link](https://www.semanticscholar.org/paper/0a535bf2697982ff8a6febef7ecff8087a7ee7b6))\
D. Bryce and David E. Smith\
11 citations

> Plan graphs are commonly used in planning to help compute heuristic “distance” estimates between states and goals. A few authors have also attempted to use plan graphs in probabilistic planning to compute estimates of the probability that propositions can be achieved and actions can be performed. This is done by propagating probability information forward through the plan graph from the initial conditions through each possible action to the action effects, and hence to the propositions at the next layer of the plan graph. The problem with these calculations is that they make very strong independence assumptions in particular, they usually assume that the preconditions for each action are independent of each other. This can lead to gross overestimates in probability when the plans for those preconditions interfere with each other. It can also lead to gross underestimates of probability when there is synergy between the plans for two or more preconditions. In this paper we introduce a notion of the binary interaction between two propositions and actions within a plan graph, show how to propagate this information within a plan graph, and show how this improves probability estimates for planning. This notion of interaction can be thought of as a continuous generalization of the notion of mutual exclusion (mutex) often used in plan graphs. At one extreme (interaction = 0) two propositions or actions are completely mutex. With interaction= 1, two propositions or actions are independent, and with interaction\> 1, two propositions or actions are synergistic. Intermediate values can and do occur indicating different degrees to which propositions and action interfere or are synergistic. We compare this approach with another recent approach by Bryce that computes probability estimates using Monte Carlo simulation of possible worlds in plan graphs.

------------------------------------------------------------------------

11\. · 100% match · 2010 · 7.1 cit/yr\
**Identifying the consequences of dynamic treatment strategies: A decision-theoretic overview** ([link](https://doi.org/10.1214/10-SS081))\
A. Dawid and V. Didelez\
*ArXiv* · Oct 17, 2010 · 110 citations

> We consider the problem of learning about and comparing the consequences of dynamic treatment strategies on the basis of observational data. We formulate this within a probabilistic decision-theoretic framework. Our approach is compared with related work by Robins and others: in particular, we show how Robins’s ‘G-computation’ algorithm arises naturally from this decision-theoretic perspective. Careful attention is paid to the mathematical and substantive conditions required to justify the use of this formula. These conditions revolve around a property we term stability, which relates the probabilistic behaviours of observational and interventional regimes. We show how an assumption of ‘sequential randomization’ (or ‘no unmeasured confounders’), or an alternative assumption of ‘sequential irrelevance’, can be used to infer stability. Probabilistic influence diagrams are used to simplify manipulations, and their power and limitations are discussed. We compare our approach with alternative formulations based on causal DAGs or potential response models. We aim to show that formulating the problem of assessing dynamic treatment strategies as a problem of decision analysis brings clarity, simplicity and generality.

------------------------------------------------------------------------

12\. · 100% match · 2005 · 0.5 cit/yr\
**RELIABILITY MODELING AND ANALYSIS OF COMPLEX HIERARCHICAL SYSTEMS** ([link](https://doi.org/10.1142/S0218539305001963))\
L. Xing\
*International Journal of Reliability, Quality and Safety Engineering* · Dec 1, 2005 · 10 citations

> In this paper we consider the problem of reliability modeling and analysis of hierarchical computer-based systems (HS) with modular imperfect coverage (MIPC) and common-cause failures (CCF). The MIPC and CCF can cause vertical dependence that runs through different levels of the system as well as horizontal dependence that runs across components or modules on the same system level. The consideration of these dependencies poses unique challenges to existing HS reliability analysis methods. We propose an efficient decomposition and aggregation approach named EDA-HS to the reliability evaluation of complex hierarchical systems with both MIPC and CCF as one way to meet the above challenges in an efficient and elegant manner. Our approach is to decouple the effects of both MIPC and CCF from the combinatorics of the solution. The approach is represented in a dynamic fault tree by a proposed probabilistic functional dependency gate and a proposed CCF gate modeled after the existing FDEP gate. We present the basics and advantages of the EDA-HS approach by working through an analysis of an example HS subject to MIPC and CCF.

------------------------------------------------------------------------

13\. · 100% match · 1994 · 1.4 cit/yr\
**A Decision-based View of Causality** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50043-2))\
D. Heckerman and Ross D. Shachter\
*ArXiv* · Jul 29, 1994 · 45 citations

> Most traditional models of uncertainty have focused on the associational relationship among variables as captured by conditional dependence. In order to successfully manage intelligent systems for decision making, however, we must be able to predict the effects of actions. In this paper, we attempt to unite two branches of research that address such predictions: causal modeling and decision analysis. First, we provide a definition of causal dependence in decision-analytic terms, which we derive from consequences of causal dependence cited in the literature. Using this definition, we show how causal dependence can be represented within an influence diagram. In particular, we identify two inadequacies of an ordinary influence diagram as a representation for cause. We introduce a special class of influence diagrams, called causal influence diagrams, which corrects one of these problems, and identify situations where the other inadequacy can be eliminated. In addition, we describe the relationships between Howard Canonical Form and existing graphical representations of cause.

------------------------------------------------------------------------

14\. · 100% match · 1983\
**Optimal searches from and ornodes** ([link](https://www.semanticscholar.org/paper/24443bab1120fd3ab503d1375ef605f20b21f02f))\
J. Barnett\
*International Joint Conference on Artificial Intelligence* · Aug 8, 1983 · 0 citations

> The problem is to organize search from an AND node in a way that minimizes expected cost. The result is derived as a corollary to earlier work of Simon and Kadane. It is shown that, unless knowledge gained during the search changes the probability or cost estimates of remaining parts of the search, the original a priori strategy remains optimal. The effect of approximating the search statistics used to determine the optimal strategy is examined, and it is found that the impact on expected cost is linearly bounded by the quality of the approximation. Then the case of searching an infinite conjunct is considered. Finally, some related research topics are discussed.

------------------------------------------------------------------------

15\. · 100% match · 2021 · 2.5 cit/yr\
**Causal Markov Decision Processes: Learning Good Interventions Efficiently** ([link](https://www.semanticscholar.org/paper/7990ed58591c23dbef01bc8010220d20c13156d2))\
Yangyi Lu, A. Meisami, and Ambuj Tewari\
*ArXiv* · Feb 15, 2021 · 13 citations

> We introduce causal Markov Decision Processes (C-MDPs), a new formalism for sequential decision making which combines the standard MDP formulation with causal structures over state transition and reward functions. Many contemporary and emerging application areas such as digital healthcare and digital marketing can benefit from modeling with C-MDPs due to the causal mechanisms underlying the relationship between interventions and states/rewards. We propose the causal upper confidence bound value iteration (C-UCBVI) algorithm that exploits the causal structure in C-MDPs and improves the performance of standard reinforcement learning algorithms that do not take causal knowledge into account. We prove that C-UCBVI satisfies an Õ(HS √ ZT ) regret bound, where T is the the total time steps, H is the episodic horizon, and S is the cardinality of the state space. Notably, our regret bound does not scale with the size of actions/interventions (A), but only scales with a causal graph dependent quantity Z which can be exponentially smaller than A. By extending C-UCBVI to the factored MDP setting, we propose the causal factored UCBVI (CF-UCBVI) algorithm, which further reduces the regret exponentially in terms of S. Furthermore, we show that RL algorithms for linear MDP problems can also be incorporated in C-MDPs. We empirically show the benefit of our causal approaches in various settings to validate our algorithms and theoretical results.

------------------------------------------------------------------------

16\. · 100% match · 1997 · 0.1 cit/yr\
**Development and Evaluation of Strategic Plans** ([link](https://www.semanticscholar.org/paper/0034a1e6711a52dca8743e6e47aeeae38ac984aa))\
T. Cazenave and Regis Moneret\
Oct 1, 1997 · 2 citations

> At the strategic level, a Go program has to manage uncertainty because of the difficulty to correctly evaluate middle game positions (strength of groups, battles). It has to be cautious not to rely on too many uncertain assumptions, otherwise its opponent will find a weakness in the plan. When faced with multiple choices for achieving a given strategic goal, we provide a method for assessing the least hazardous plan (a plan is a subtree of goals that leads to the success of the root goal). We combine AND/OR tree search with probability estimations of success of the achievement of the goal. Intuitively, errors cumulate at AND nodes because different conditions have to be satisfied at the same time.

------------------------------------------------------------------------

17\. · 100% match · 1981\
**Effect of sympathetic failures on redundant system reliability** ([link](https://www.semanticscholar.org/paper/7131745b5fbb0820f7f1326919976f56386a6dc9))\
I. Papazoglou and S. Mitra\
0 citations

> Purpose of this paper is to analyze the effect on the reliability of redundant systems of a class of dependent failures due to causes internal to the system (sympathetic failures). A general Markovian model incorporating both common cause (externally generated) and sympathetic failures is developed. This model includes the ..beta..-factor and the Marshall-Olkin models as special cases. Three specialized versions of the general model are presented. It is shown that sympathetic failures can lower the reliability of a system beyond the limit set by common-cause failures.

------------------------------------------------------------------------

18\. · 100% match · 2002 · 12 cit/yr\
**Influence Diagrams for Causal Modelling and Inference** ([link](https://doi.org/10.1111/j.1751-5823.2002.tb00354.x))\
A. Dawid\
*International Statistical Review* · Aug 1, 2002 · 294 citations

------------------------------------------------------------------------

19\. · 100% match · 2002 · 1.5 cit/yr\
**Treatment of general dependencies in system fault-tree and risk analysis** ([link](https://doi.org/10.1109/TR.2002.801848))\
J. Vaurio\
*IEEE Trans. Reliab.* · Nov 7, 2002 · 35 citations

> Implicit and explicit methods are described for reliability and risk analysis of systems with dependent or correlated basic events. General rules are presented for modeling any group of n mutually s-dependent events with 2/sup n/-1 s-independent events. The probabilities of these virtual events are determined based on the joint probabilities of the original s-dependent events, typically known by s-correlation or conditional probabilities. The transformations preserve the values of all terms (e.g., minimal cut sets), independent of system success criteria. This facilitates general use of ordinary fault-tree computer codes that assume basic events to be s-independent. Explicit basic event probabilities are obtained for calculating the probability of failure on demand of standby safety systems when the s-dependency is caused by scheduling and synchronization of test episodes between n redundant components (1 /spl les/ n /spl les/ 4), and by statistical variation of failure rates. Interesting “negative probabilities” are encountered in this exercise, mainly due to negative s-correlation between the component unavailabilities with staggered testing. Results obtained for human-error events are useful when the conditional probability to repeat an error is larger than the probability of an error in a single isolated task. Explicit results are obtained for systems with time-related common-cause failures modeled by general multiple failure rates. The impacts of test intervals and test staggering are included. Staggered testing is optimal with an ETR (extra-testing rule), although ETR is not important for 1-out-of-n:G systems. An economic model provides insights into the impacts of various parameters: the optimal test interval increases with increasing redundancy and testing cost, and it decreases with increasing accident cost and initiating event rate. Staggered testing with ETR allows for the longest optimal test intervals. Rules are presented for changing s-dependency probabilities when some component is known to be failed. Current fault-tree quantification tools are not well geared to use the implicit method in spite of the fact that it would simplify the fault-tree construction, reduce the number of cut sets, and allow different types of dependencies or correlations in the analysis. A recommendation is to computerize the implicit method or include it as an option to current codes. It would need only a data table for joint probabilities and the ability to pick-up data from this table whenever two or more of the s-dependent events appear in a term (or a cut set).

------------------------------------------------------------------------

20\. · 100% match · 2016 · 5.1 cit/yr\
**Markov Decision Processes with Unobserved Confounders : A Causal Approach** ([link](https://www.semanticscholar.org/paper/69c68d804e7c052665d5b4049c0d9c9d8baa11c0))\
Junzhe Zhang and E. Bareinboim\
53 citations

> Markov decision processes (MDPs) constitute one of the most general frameworks for modeling decision-making under uncertainty, being used in multiple fields, including economics, medicine, and engineering. The goal of the agent in an MDP setting is to learn more about the environment so as to optimize a certain criterion. This task is pursued through the exploration of the environment by actively performing interventions (i.e., through the randomization of its actions), which contrasts with the agent passively observing the environment and not exerting any control over it (i.e., through random sampling). The existence of unobserved confounders, namely, unmeasured variables affecting both the action and the outcome or both the action and the state variables, implies that these two datacollection modes (passive and active) will in general not coincide. It is clear that by performing interventions, any potential inclination (intuition) of the agent will be ignored, which will imply a loss of information and failure to achieve an optimal behavior. In this paper, we formalize this observation and study its conceptual and algorithmic implications. We first demonstrate that standard algorithms may act sub-optimally when unobserved confounders are present. We then propose a systematic method to enhance these algorithms using causal inference theory and leveraging observational data. We formally and empirically show that this new approach produces superior results than current state-of-the-art MDP algorithms.

------------------------------------------------------------------------

21\. · 100% match · 2008 · 0.5 cit/yr\
**Identifying Optimal Sequential Decisions** ([link](https://www.semanticscholar.org/paper/c43385a150a13bb0d06787050e2b9c2173b617cb))\
P. Dawid and V. Didelez\
*Conference on Uncertainty in Artificial Intelligence* · Jul 9, 2008 · 9 citations

> We consider conditions that allow us to find an optimal strategy for sequential decisions from a given data situation. For the case where all interventions are unconditional (atomic), identifiability has been discussed by Pearl & Robins (1995). We argue here that an optimal strategy must be conditional, i.e. take the information available at each decision point into account. We show that the identification of an optimal sequential decision strategy is more restrictive, in the sense that conditional interventions might not always be identified when atomic interventions are. We further demonstrate that a simple graphical criterion for the identifiability of an optimal strategy can be given.

------------------------------------------------------------------------

22\. · 100% match · 1997 · 7.6 cit/yr\
**A modular approach for analyzing static and dynamic fault trees** ([link](https://doi.org/10.1109/RAMS.1997.571665))\
R. Gulati and J. Dugan\
*Annual Reliability and Maintainability Symposium* · Jan 13, 1997 · 224 citations

------------------------------------------------------------------------

23\. · 100% match · 1989 · 1.4 cit/yr\
**A model for system reliability with common-cause failures** ([link](https://doi.org/10.1109/24.46447))\
L. Page and J. Perry\
*IEEE Transactions on Reliability* · Oct 1, 1989 · 51 citations

> A model for the analysis of systems subject to common-cause failures is proposed. The system consists of a finite number of components that are subject to: (1) statistically independent failures, and (2) external failure causes (they need not be mutually statistically independent) for groups of components. Applications to fault-tree analysis and network reliability problems are discussed. \>

------------------------------------------------------------------------

24\. · 98% match · 1994 · 2.2 cit/yr\
**Action Networks: A Framework for Reasoning about Actions and Change under Uncertainty** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50023-7))\
Adnan Darwiche and M. Goldszmidt\
*Conference on Uncertainty in Artificial Intelligence* · Jul 29, 1994 · 71 citations

> This work proposes action networks as a semantically well founded framework for reasoning about actions and change under uncertainty. Action networks add two primitives to probabilistic causal networks: controllable variables and persistent variables. Controllable variables allow the representation of actions as directly setting the value of specific events in the domain, subject to preconditions. Persistent variables provide a canonical model of persistence according to which both the state of a variable and the causal mechanism dictating its value persist over time unless intervened upon by an action (or its consequences). Action networks also allow different methods for quantifying the uncertainty in causal relationships, which go beyond traditional probabilistic quantification. This paper describes both recent results and work in progress.

------------------------------------------------------------------------

25\. · 95% match · 2024 · 0.9 cit/yr\
**Why Online Reinforcement Learning is Causal** ([link](https://doi.org/10.48550/arXiv.2403.04221))\
Oliver Schulte and Pascal Poupart\
*ArXiv* · Mar 7, 2024 · 2 citations

> Reinforcement learning (RL) and causal modelling naturally complement each other. The goal of causal modelling is to predict the effects of interventions in an environment, while the goal of reinforcement learning is to select interventions that maximize the rewards the agent receives from the environment. Reinforcement learning includes the two most powerful sources of information for estimating causal relationships: temporal ordering and the ability to act on an environment. This paper examines which reinforcement learning settings we can expect to benefit from causal modelling, and how. In online learning, the agent has the ability to interact directly with their environment, and learn from exploring it. Our main argument is that in online learning, conditional probabilities are causal, and therefore offline RL is the setting where causal learning has the most potential to make a difference. Essentially, the reason is that when an agent learns from their {\em own} experience, there are no unobserved confounders that influence both the agent’s own exploratory actions and the rewards they receive. Our paper formalizes this argument. For offline RL, where an agent may and typically does learn from the experience of {\em others}, we describe previous and new methods for leveraging a causal model, including support for counterfactual queries.

------------------------------------------------------------------------

26\. · 95% match · 2009 · 2.2 cit/yr\
**Incorporating Common-Cause Failures Into the Modular Hierarchical Systems Analysis** ([link](https://doi.org/10.1109/TR.2008.2011855))\
L. Xing, A. Shrestha, L. Meshkat, and Wendai Wang\
*IEEE Transactions on Reliability* · Feb 10, 2009 · 38 citations

------------------------------------------------------------------------

27\. · 95% match · 1998 · 4.0 cit/yr\
**An implicit method for incorporating common-cause failures in system analysis** ([link](https://doi.org/10.1109/24.722285))\
J. Vaurio\
*IEEE Transactions on Reliability* · Jun 1, 1998 · 113 citations

> A general procedure incorporates common-cause (CC) failures into system analysis by an implicit method; i.e., after first solving the system probability equation without CC failures. Components of subsets are assumed to be equally vulnerable to CC of any particular multiplicity. The method allows for age-dependent hazard rates, repairable and nonrepairable components, systems with multiple CC groups, and systems where not all components are statistically-identical or subject to CC failures. Key equations are given both for reliability block-diagrams and fault-trees (success and failure models), considering the system reliability, availability and failure intensity functions. Initial failures and certain human errors are included, mainly for standby-system applications. The implicit method can dramatically simplify the Boolean manipulation and quantification of fault trees. Possible limitations and extensions are discussed.

------------------------------------------------------------------------

28\. · 94% match · 1994 · 8.6 cit/yr\
**Counterfactual Probabilities: Computational Methods, Bounds and Applications** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50011-0))\
Alexander Balke and J. Pearl\
*Conference on Uncertainty in Artificial Intelligence* · Jul 29, 1994 · 273 citations

> Evaluation of counterfactual queries (e.g., “If A were true, would C have been true?”) is important to fault diagnosis, planning, and determination of liability. In this paper we present methods for computing the probabilities of such queries using the formulation proposed in \[Balke and Pearl, 1994\], where the antecedent of the query is interpreted as an external action that forces the proposition A to be true. When a prior probability is available on the causal mechanisms governing the domain, counterfactual probabilities can be evaluated precisely. However, when causal knowledge is specified as conditional probabilities on the observables, only bounds can computed. This paper develops techniques for evaluating these bounds, and demonstrates their use in two applications: (1) the determination of treatment efficacy from studies in which subjects may choose their own treatment, and (2) the determination of liability in product-safety litigation.

------------------------------------------------------------------------

29\. · 92% match · 1994 · 0.6 cit/yr\
**Symbolic Causal Networks for Reasoning about Actions and Plans** ([link](https://www.semanticscholar.org/paper/f3552ebb16a70b8f19ea332468115efa63bcc7c5))\
Adnan Darwiche and J. Pearl\
20 citations

> We present an approach for reasoning about actions and plans when domain knowledge is represented by a symbolic causal network, which is a principled, logical representation of a domain that explicates its perceived causal structure. The proposed approach shows that causal structures can play a key role in logical reasoning about actions given their effective role in dealing with some of the problems associated with such reasoning, including the frame, ramification, and concurrency problems.

------------------------------------------------------------------------

30\. · 92% match · 1989\
**Dependent Failure Modelling by Fault Tree Technique** ([link](https://doi.org/10.1007/978-94-017-0629-2_9))\
S. Contini\
0 citations

------------------------------------------------------------------------

31\. · 91% match · 1978 · 0.2 cit/yr\
**Comparison of three methods for the quantitative analysis of common cause failures** ([link](https://www.semanticscholar.org/paper/27f9b82b00388babf1d0bdd2aab7b3bb06332b94))\
K. N. Fleming and P. Raabe\
May 1, 1978 · 12 citations

> A comparison is presented of three methods to predict the reliability characteristics of redundant systems subject to independent and common cause failures. Markov models are used to show that the ‘’beta factor’’ method, developed and used in the HTGR risk assessment study conducted at General Atomic, is theoretically consistent with alternative approaches that are based on the multivariate exponential distribution developed by Marshall and Olkin. Comparative assessments of simple redundant systems based on actual reliability data are used to investigate differences between the ‘’beta factor’’ method and the ‘’geometric mean’’ approach used in the Reactor Safety Study.

------------------------------------------------------------------------

32\. · 91% match · 1994 · 8.5 cit/yr\
**Probabilistic Planning with Information Gathering and Contingent Execution** ([link](https://www.semanticscholar.org/paper/5205d4ab167f83c6f1098cc45e04249e8314db5d))\
Denise Draper, S. Hanks, and Daniel S. Weld\
*International Conference on Artificial Intelligence Planning Systems* · Jun 13, 1994 · 271 citations

> Most AI representations and algorithms for plan generation have not included the concept of information-producing actions (also called diagnostics, or tests, in the decision making literature). We present a planning representation and algorithm that models information-producing actions and constructs plans that exploit the information produced by those actions. We extend the BURIDAN (Kushmerick et al. 1994) probabilistic planning algorithm, adapting the action representation to model the behavior of imperfect sensors, and combine it with a framework for contingent action that extends the CNLP algorithm (Peot and Smith 1992) for conditional execution. The result, C-BURIDAN, is an implemented planner that builds plans with probabilistic information-producing actions and contingent execution.

------------------------------------------------------------------------

33\. · 90% match · 2025\
**When Should Reinforcement Learning Use Causal Reasoning?** ([link](https://www.semanticscholar.org/paper/1ea0a4c86eaf441a6aafe6b52213985cd06304d9))\
Oliver Schulte and Pascal Poupart\
*Trans. Mach. Learn. Res.* · 0 citations

> Reinforcement learning (RL) and causal reasoning naturally complement each other. The goal of causal reasoning is to predict the effects of interventions in an environment, while the goal of reinforcement learning is to select interventions that maximize the rewards the agent receives from the environment. Reinforcement learning includes the two most powerful sources of information for estimating causal relationships: temporal ordering and the ability to act on an environment. This paper provides a theoretical study examining which reinforcement learning settings we can expect to benefit from causal reasoning, and how. According to our analysis, the key factor is whether the behavioral policy—which generates the data—can be executed by the learning agent , meaning that the observation signal available to the learning agent comprises all observations used by the behavioral policy. Common RL settings with behavioral policies that are executable by the learning agent include on-policy learning and online exploration, where the learning agent uses a behavioral policy to explore the environment. Common RL settings with behavioral policies that are not executable by the learning agent include offline learning with a partially observable state space and asymmetric imitation learning where the demonstrator has access to more observations than the imitator. Using the theory of causal graphs, we show formally that when the behavioral policy is executable by the learning agent, conditional probabilities are causal, and can therefore be used to estimate expected rewards as done in traditional RL. However, when the behavioral policy is not executable by the learning agent, conditional probabilities may be confounded and provide misleading estimates of expected rewards. For confounded settings, we describe previous and new methods for leveraging causal reasoning.

------------------------------------------------------------------------

34\. · 90% match · 2021 · 16 cit/yr\
**Shaking the foundations: delusions in sequence models for interaction and control** ([link](https://www.semanticscholar.org/paper/bc031724d5323b294e22a895977928b79fbe8a29))\
Pedro A. Ortega et al.\
*ArXiv* · Oct 20, 2021 · 72 citations

> The recent phenomenal success of language models has reinvigorated machine learning research, and large sequence models such as transformers are being applied to a variety of domains. One important problem class that has remained relatively elusive however is purposeful adaptive behavior. Currently there is a common perception that sequence models”lack the understanding of the cause and effect of their actions”leading them to draw incorrect inferences due to auto-suggestive delusions. In this report we explain where this mismatch originates, and show that it can be resolved by treating actions as causal interventions. Finally, we show that in supervised learning, one can teach a system to condition or intervene on data by training with factual and counterfactual error signals respectively.

------------------------------------------------------------------------

35\. · 90% match · 1994 · 1.6 cit/yr\
**A Probablistic Model of Action for Least-Commitment Planning with Information Gathering** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50028-6))\
Denise Draper, S. Hanks, and Daniel S. Weld\
*Conference on Uncertainty in Artificial Intelligence* · Jul 29, 1994 · 51 citations

> AI planning algorithms have addressed the problem of generating sequences of operators that achieve some input goal, usually assuming that the planning agent has perfect control over and information about the world. Relaxing these assumptions requires an extension to the action representation that allows reasoning both about the changes an action makes and the information it provides. This paper presents an action representation that extends the deterministic STRIPS model, allowing actions to have both causal and informational effects, both of which can be context dependent and noisy. We also demonstrate how a standard least-commitment planning algorithm can be extended to include informational actions and contingent execution.

------------------------------------------------------------------------

36\. · 90% match · 2016 · 6.1 cit/yr\
**A general cause based methodology for analysis of common cause and dependent failures in system risk and reliability assessments** ([link](https://doi.org/10.1016/j.ress.2015.06.007))\
A. O’Connor and A. Mosleh\
*Reliab. Eng. Syst. Saf.* · 63 citations

------------------------------------------------------------------------

37\. · 90% match · 2007 · 2.4 cit/yr\
**Reliability analysis of hierarchical computer-based systems subject to common-cause failures** ([link](https://doi.org/10.1016/j.ress.2006.04.010))\
L. Xing, L. Meshkat, and S. Donohue\
*Reliab. Eng. Syst. Saf.* · Mar 1, 2007 · 46 citations

------------------------------------------------------------------------

38\. · 89% match · 2020 · 9.9 cit/yr\
**Decision-theoretic foundations for statistical causality** ([link](https://doi.org/10.1515/jci-2020-0008))\
P. Dawid\
*Journal of Causal Inference* · Apr 26, 2020 · 60 citations

> Abstract We develop a mathematical and interpretative foundation for the enterprise of decision-theoretic (DT) statistical causality, which is a straightforward way of representing and addressing causal questions. DT reframes causal inference as “assisted decision-making” and aims to understand when, and how, I can make use of external data, typically observational, to help me solve a decision problem by taking advantage of assumed relationships between the data and my problem. The relationships embodied in any representation of a causal problem require deeper justification, which is necessarily context-dependent. Here we clarify the considerations needed to support applications of the DT methodology. Exchangeability considerations are used to structure the required relationships, and a distinction drawn between intention to treat and intervention to treat forms the basis for the enabling condition of “ignorability.” We also show how the DT perspective unifies and sheds light on other popular formalisations of statistical causality, including potential responses and directed acyclic graphs.

------------------------------------------------------------------------

39\. · 89% match · 1994 · 4.0 cit/yr\
**An Algorithm for Probabilistic Least-Commitment Planning** ([link](https://www.semanticscholar.org/paper/3288fce6e3b69b2f03d323f7ac20acaece5a55ef))\
N. Kushmerick, S. Hanks, and Daniel S. Weld\
*AAAI Conference on Artificial Intelligence* · Aug 1, 1994 · 128 citations

> We define the probabilistic planning problem in terms of a probability distribution over initial world states, a boolean combination of goal propositions, a probability threshold, and actions whose effects depend on the execution-time state of the world and on random chance. Adopting a probabilistic model complicates the definition of plan success: instead of demanding a plan that provably achieves the goal, we seek plans whose probability of success exceeds the threshold.
>
> This paper describes a probabilistic semantics for planning under uncertainty, and presents a fully implemented algorithm that generates plans that succeed with probability no less than a user-supplied probability threshold. The algorithm is sound (if it terminates then the generated plan is sufficiently likely to achieve the goal) and complete (the algorithm will generate a solution if one exists).

------------------------------------------------------------------------

40\. · 88% match · 1993 · 3.8 cit/yr\
**From Conditional Oughts to Qualitative Decision Theory** ([link](https://doi.org/10.1016/B978-1-4832-1451-1.50006-8))\
J. Pearl\
*Conference on Uncertainty in Artificial Intelligence* · Jul 9, 1993 · 125 citations

> The primary theme of this investigation is a decision theoretic account of conditional ought statements (e.g., “You ought to do A, if C”) that rectifies glaring deficiencies in classical deontic logic. The resulting account forms a sound basis for qualitative decision theory, thus providing a framework for qualitative planning under uncertainty. In particular, we show that adding causal relationships (in the form of a single graph) as part of an epistemic state is sufficient to facilitate the analysis of action sequences, their consequences their interaction with observations, their expected utilities and, hence, the synthesis of plans and strategies under uncertainty.

------------------------------------------------------------------------

41\. · 87% match · 1976 · 2.1 cit/yr\
**On the Quantitative Analysis of Priority-AND Failure Logic** ([link](https://doi.org/10.1109/TR.1976.5220025))\
J. B. Fussell, E. F. Aber, and R. Rahl\
*IEEE Transactions on Reliability* · Dec 1, 1976 · 103 citations

------------------------------------------------------------------------

42\. · 86% match · 1994 · 4.6 cit/yr\
**Conditioning and Intervening** ([link](https://doi.org/10.1093/bjps/45.4.1001))\
Christopher Meek and C. Glymour\
*The British Journal for the Philosophy of Science* · Dec 1, 1994 · 144 citations

> We consider the dispute between causal decision theorists and evidential decision theorists over Newcomb-like problems. We introduce a framework relating causation and directed graphs developed by Spirtes et al. (1993) and evaluate several arguments in this context. We argue that much of the debate between the two camps is misplaced; the disputes turn on the distinction between conditioning on an event E as against conditioning on an event I which is an action to bring about E. We give the essential machinery for calculating the effect of an intervention and consider recent work which extends the basic account given here to the case where causal Knowledge is incomplete.

------------------------------------------------------------------------

43\. · 85% match · 2013 · 4.0 cit/yr\
**Generalized Thompson sampling for sequential decision-making and causal inference** ([link](https://doi.org/10.1186/2194-3206-2-2))\
Pedro A. Ortega and Daniel A. Braun\
*Complex Adaptive Systems Modeling* · Mar 18, 2013 · 53 citations

> PurposeSampling an action according to the probability that the action is believed to be the optimal one is sometimes called Thompson sampling.MethodsAlthough mostly applied to bandit problems, Thompson sampling can also be used to solve sequential adaptive control problems, when the optimal policy is known for each possible environment. The predictive distribution over actions can then be constructed by a Bayesian superposition of the policies weighted by their posterior probability of being optimal.ResultsHere we discuss two important features of this approach. First, we show in how far such generalized Thompson sampling can be regarded as an optimal strategy under limited information processing capabilities that constrain the sampling complexity of the decision-making process. Second, we show how such Thompson sampling can be extended to solve causal inference problems when interacting with an environment in a sequential fashion.ConclusionIn summary, our results suggest that Thompson sampling might not merely be a useful heuristic, but a principled method to address problems of adaptive sequential decision-making and causal inference.

------------------------------------------------------------------------

44\. · 85% match · 2016 · 19 cit/yr\
**Causal Bandits: Learning Good Interventions via Causal Inference** ([link](https://www.semanticscholar.org/paper/4d9f776cb5bf419a8ff1c1a65e54141ddc976ec1))\
Finnian Lattimore, Tor Lattimore, and Mark D. Reid\
*Neural Information Processing Systems* · Jun 10, 2016 · 186 citations

> We study the problem of using causal models to improve the rate at which good interventions can be learned online in a stochastic environment. Our formalism combines multi-arm bandits and causal inference to model a novel type of bandit feedback that is not exploited by existing approaches. We propose a new algorithm that exploits the causal feedback and prove a bound on its simple regret that is strictly better (in all quantities) than algorithms that do not use the additional causal information.

------------------------------------------------------------------------

45\. · 85% match · 1995 · 14 cit/yr\
**An Algorithm for Probabilistic Planning** ([link](https://doi.org/10.1016/0004-3702(94%2900087-H))\
N. Kushmerick, S. Hanks, and Daniel S. Weld\
*Artif. Intell.* · Jul 1, 1995 · 433 citations

------------------------------------------------------------------------

46\. · 85% match · 2010 · 2.3 cit/yr\
**Algebraic modelling of Dynamic Fault Trees, contribution to qualitative and quantitative analysis** ([link](https://www.semanticscholar.org/paper/0ea912813d4c7f5840d40458d477268d44dd62d6))\
G. Merle\
Jul 7, 2010 · 36 citations

> In the context of the reliability of critical systems, we focus on Dynamic Fault Tree (DFT) analysis. Our contribution is the definition of an algebraic framework allowing to determine the structure function of DFTs and to extend the analytical methods commonly used to analyze Static Fault Trees to DFTs. First, we review the main approaches which allow to analyze DFTs, as well as their limits. Then, the algebraic framework allowing the modelling of DFTs is presented. This algebraic framework is based on a temporal model of events, and on the definition of three temporal operators allowing to model the sequences of appearance of events. These temporal operators allow to algebraically define the behaviour of dynamic gates, and hence the structure function of DFTs. A probabilistic model of these dynamic gates is given to determine the failure probability of the top event of DFTs from this structure function. Finally, we show how the structure function of DFTs can be simplified to a canonical form thanks to some theorems and to a minimal form thanks to the definition of a minimization criterion. Last, we show how DFTs can be analyzed analytically and directly from this minimal canonical form of the structure function. We illustrate this approach on two DFT examples from the literature.

------------------------------------------------------------------------

47\. · 84% match · 1994 · 1.6 cit/yr\
**Epsilon-Safe Planning** ([link](https://doi.org/10.1016/B978-1-55860-332-5.50037-7))\
R. Goldman and M. Boddy\
*Conference on Uncertainty in Artificial Intelligence* · Jul 29, 1994 · 51 citations

> We introduce an approach to high-level conditional planning we call e-safe planning. This probabilistic approach commits us to planning to meet some specified goal witch a probability of success of at least 1 - e for some user-supplied e. We describe several algorithms for e-safe planning based on conditional planners. The two conditional planners we discuss are Peot and Smith’s nonlinear conditional planner, CNLP, and our own linear conditional planner, PLINTH. We present a straightforward extension to conditional planners for which computing the necessary probabilities is simple, employing a commonly-made but perhaps overly-strong independence assumption. We also discuss a second approach to e-safe planning which relaxes this independence assumption, involving the incremental construction of a probability dependence model in conjunction with the construction of the plan graph.

------------------------------------------------------------------------

48\. · 84% match · 2020 · 5.8 cit/yr\
**Characterizing Optimal Mixed Policies: Where to Intervene and What to Observe** ([link](https://www.semanticscholar.org/paper/93ac56f4431cb7d0d3389887c56817dab246967d))\
Sanghack Lee and E. Bareinboim\
*Neural Information Processing Systems* · 37 citations

> Intelligent agents are continuously faced with the challenge of optimizing a policy based on what they can observe (see) and which actions they can take (do) in the environment where they are deployed. Most policy can be parametrized in terms of these two dimensions, i.e., as a function of what can be seen and done given a certain situation, which we call a mixed policy . In this paper, we investigate several properties of the class of mixed policies and provide an efﬁcient and effective characterization, including optimality and non-redundancy. Speciﬁcally, we introduce a graphical criterion to identify unnecessary contexts for a set of actions, leading to a natural characterization of non-redundancy of mixed policies. We then derive sufﬁcient conditions under which one strategy can dominate the other with respect to their maximum achievable expected rewards (optimality). This characterization leads to a fundamental understanding of the space of mixed policies and a possible reﬁnement of the agent’s strategy so that it converges to the optimum faster and more robustly. One surprising result of the causal characterization is that the agent following a more standard approach—intervening on all intervenable variables and observing all available contexts—may be hurting itself, and will never achieve an optimal performance.

------------------------------------------------------------------------

49\. · 83% match · 1996 · 0.9 cit/yr\
**A Logic of Time, Chance, and Action for Representing Plans** ([link](https://doi.org/10.1016/0004-3702(94%2900070-0))\
P. Haddawy\
*Artif. Intell.* · Feb 1, 1996 · 28 citations

> Abstract This paper integrates logical and probabilistic approaches to the representation of planning problems by developing a first-order logic of time, chance, and action. We start by making explicit and precise commonsense notions about time, chance, and action central to the planning problem. We then develop a logic, the semantics of which incorporates these intuitive properties. The logical language integrates both modal and probabilistic constructs and allows quantification over time points, probability values, and domain individuals. Probability is treated as a sentential operator in the language, so it can be arbitrarily nested and combined with other logical operators. The language can represent the chance that facts hold and events occur at various times. It can represent the chance that actions and other events affect the future. The model of action distinguishes between action feasibility, executability, and effects. We present a proof theory for the logic and show how the logic can be used to describe actions in such a way that the action descriptions can be composed to infer properties of plans via the proof theory.

------------------------------------------------------------------------

50\. · 83% match · 2006 · 0.3 cit/yr\
**Using Correlation to Compute Better Probability Estimates in Plan Graphs** ([link](https://www.semanticscholar.org/paper/d08bcdb673651830d662a6b75918cefb20ee9554))\
D. Bryce and David E. Smith\
6 citations

> Plan graphs are commonly used in planning to help compute heuristic “distance” estimates between states and goals. A few authors have also attempted to use plan graphs in probabilistic planning to compute estimates of the probability that propositions can be achieved and actions can be performed. This is done by propagating probability information forward through the plan graph from the initial conditions through each possible action to the action effects, and hence to the propositions at the next layer of the plan graph. The problem with these calculations is that they make very strong independence assumptions - in particular, they usually assume that the preconditions for each action are independent of each other. This can lead to gross overestimates in probability when the plans for those preconditions interfere with each other. It can also lead to gross underestimates of probability when there is synergy between the plans for two or more preconditions. In this paper we introduce a notion of the binary correlation between two propositions and actions within a plan graph, show how to propagate this information within a plan graph, and show how this improves probability estimates for planning. This notion of correlation can be thought of as a continuous generalization of the notion of mutual exclusion (mutex) often used in plan graphs. At one extreme (correlation=0) two propositions or actions are completely mutex. With correlation = 1, two propositions or actions are independent, and with correlation \> 1, two propositions or actions are synergistic. Intermediate values can and do occur indicating different degrees to which propositions and action interfere or are synergistic. We compare this approach with another recent approach by Bryce that computes probability estimates using Monte Carlo simulation of possible worlds in plan graphs.

*Showing top 50 of 110 papers. Full details available via CSV or BibTeX export.*
