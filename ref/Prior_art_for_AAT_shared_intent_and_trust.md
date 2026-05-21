# Prior art for AAT shared intent and trust

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which optimal communication between cooperative agents (“Shared Intent”) is the Information Bottleneck compression of the sender’s purposeful state. Under bandwidth constraints, the framework claims there is a mathematically optimal communication hierarchy (“Auftragstaktik” / Mission Command) in which sharing objectives is superior to coordinating strategies, which is in turn superior to synchronizing models. The search should prioritize formal proofs, mathematical derivations, and closely equivalent formalisms across multi-agent reinforcement learning, rate-distortion and information theory, team decision and control theory, mechanism design, and organizational economics. Relevant matches include formal results showing that under communication constraints it is better to transmit goals, intentions, sufficient statistics, compressed purposeful state, or other higher-level task information rather than full plans, policies, or models; applications of Information Bottleneck, rate-distortion, or related communication-theoretic objectives to what agents should communicate in decentralized or cooperative systems; and partial unifications that connect bandwidth-constrained communication with hierarchical command, delegation, or mission-style coordination. Exclude papers where agents simply broadcast full state without compression or bandwidth limits. Also find prior art for the claim that when agents update based on communication, the update gain should be discounted separately by channel noise, source competence (epistemic uncertainty), and source alignment (teleological uncertainty), and that misplaced trust can trigger a catastrophic “effects spiral,” so trust must be evaluated asymmetrically using a conservative posterior quantile or closely related downside-risk criterion rather than expected value alone. Search broadly but math-first across Bayesian trust models, decentralized systems, mechanism design, signaling, principal-agent theory, robust control, risk-sensitive decision-making, and safe multi-agent learning, including older non-MARL lineages when the mathematics is closer than the framing. Relevant matches include formal models that explicitly separate competence from intent, honesty, benevolence, alignment, or related teleological variables instead of bundling them into a single reliability score; trust or belief-update rules that discount communication by both epistemic and teleological uncertainty; and risk-sensitive, CVaR, quantile, or other asymmetric trust-evaluation methods motivated by catastrophic downside in decentralized or high-stakes systems. Give extra weight to papers that partially unify the communication-hierarchy and trust-discounting pillars in a single posture, but also capture the strongest antecedents to each pillar separately. Restrict the search to academic papers only; exclude patents and non-academic sources, and exclude simple reputation systems that collapse competence and intent into one generic score.

*Found 90 papers · May 21, 2026 · Estimated coverage of relevant papers: 91%*

## Summary of Results

Scientific precedence exists, but in two largely separate lineages: information-constrained control/team theory formalizes optimal communication as task-relevant compression or sufficient information \[1\], \[2\], \[3\], \[4\], \[5\], \[6\], while trust theory separately formalizes source evaluation by competence/intent decompositions and conservative downside-sensitive uptake \[7\], \[8\], \[9\], \[10\].

#### Shared intent under bandwidth

- IB and sequential rate-distortion supply the core mathematical template: compress state/history to preserve only task-relevant information, with control performance traded against mutual or directed information \[1\], \[2\], \[3\], \[11\], \[12\], \[13\].
- Decentralized team results identify common/sufficient information states, showing large parts of private history can be ignored or compressed without loss of optimality \[5\], \[6\], \[14\], \[15\], \[16\].
- Modern MARL papers instantiate this as low-entropy, intention- or task-oriented communication \[17\], \[18\], \[19\], \[20\], but the strongest proofs are mostly in control and team theory rather than MARL.
- Organizational economics supplies the closest hierarchy/delegation antecedents: authority and delegation economize on communication under complexity and misalignment \[21\], \[22\], \[23\], \[24\], \[25\]. Direct proofs of the exact ordering “objectives \> strategies \> models” were not explicit in this set.

#### Trust as epistemic and teleological discounting

- Several formal trust models explicitly separate competence/knowledge from helpfulness, integrity, sincerity, or alignment \[7\], \[8\], \[9\], \[26\], \[27\].
- Robust uptake of advice is handled with asymmetric downside criteria—CVaR, worst-case distrust, or conservative persuasion—rather than expectation alone \[10\], \[28\], \[29\]; strategic adviser competence and agenda interact in repeated settings \[30\].
- A single formalism unifying compressed mission-style communication with competence/alignment-discounted trust did not appear in the retrieved papers.

## Paper Catalog (90 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2004 | 80 | Control under communication constraints ([link](https://doi.org/10.1109/TAC.2004.831187)) | S. Tatikonda and S. Mitter | IEEE Transactions on Automatic Control |
| 2 | 2012 | 22 | Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach ([link](https://doi.org/10.1109/TAC.2013.2239000)) | A. Nayyar, Aditya Mahajan, and D. Teneketzis | IEEE Transactions on Automatic Control |
| 3 | 2015 | 11 | LQG Control With Minimum Directed Information: Semidefinite Programming Approach ([link](https://doi.org/10.1109/TAC.2017.2709618)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | IEEE Transactions on Automatic Control |
| 4 | 2019 | 20 | Learning Efficient Multi-agent Communication: An Information Bottleneck Approach ([link](https://www.semanticscholar.org/paper/ac7fbe27a47236689bf2076e7ffc9561a06941e1)) | R. Wang et al. | International Conference on Machine Learning |
| 5 | 2016 | 1.8 | Minimum-information LQG control part I: Memoryless controllers ([link](https://doi.org/10.1109/CDC.2016.7799131)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 6 | 2021 | 22 | Communication in Multi-Agent Reinforcement Learning: Intention Sharing ([link](https://www.semanticscholar.org/paper/9ed9ff62749f450247d1f6be9d1c14142fa63f05)) | Woojun Kim, Jongeui Park, and Y. Sung | International Conference on Learning Representations |
| 7 | 2026 |  | Robust Trust ([link](https://www.semanticscholar.org/paper/8d3536ffc54dc01feeb4211ef93252e48f1e93a2)) | Piotr Dworczak and A. Smolin |  |
| 8 | 2016 | 1.3 | Minimum-information LQG control Part II: Retentive controllers ([link](https://doi.org/10.1109/CDC.2016.7799130)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 9 | 2022 | 3.6 | A Unified Approach to Dynamic Decision Problems With Asymmetric Information: Nonstrategic Agents ([link](https://doi.org/10.1109/TAC.2021.3060835)) | Hamidreza Tavafoghi, Ouyang Yi, and D. Teneketzis | IEEE Transactions on Automatic Control |
| 10 | 2012 | 9.4 | Epistemic trust: modeling children’s reasoning about others’ knowledge and intent. ([link](https://doi.org/10.1111/j.1467-7687.2012.01135.x)) | Patrick Shafto, Baxter S. Eaves, Danielle Navarro, and A. Perfors | Developmental science |
| 11 | 2004 | 20 | Stochastic linear control over a communication channel ([link](https://doi.org/10.1109/TAC.2004.834430)) | S. Tatikonda, Anant Sahai, and S. Mitter | IEEE Transactions on Automatic Control |
| 12 | 2020 | 1.0 | Task-Based Information Compression for Multi-Agent Communication Problems with Channel Rate Constraints ([link](https://www.semanticscholar.org/paper/0218f804322c63ada943788c95d38266ae0a9ca5)) | Arsham Mostaani, T. Vu, S. Chatzinotas, and B. Ottersten | ArXiv |
| 13 | 2023 | 2.1 | Minimizing Return Gaps with Discrete Communications in Decentralized POMDP ([link](https://doi.org/10.48550/arXiv.2308.03358)) | Jingdi Chen and Tian Lan | ArXiv |
| 14 | 2001 |  | Complexity and Coordination by Authority ∗ ([link](https://www.semanticscholar.org/paper/155c4af62e235caa0e48f6484b4250aab8676466)) | I. Segal |  |
| 15 | 2024 | 1.3 | Cooperation and Control in Delegation Games ([link](https://doi.org/10.24963/ijcai.2024/26)) | Oliver Sourbut, Lewis Hammond, and Harriet Wood | ArXiv |
| 16 | 2018 | 1.1 | A Sufficient Information Approach to Decentralized Decision Making ([link](https://doi.org/10.1109/CDC.2018.8619040)) | Hamidreza Tavafoghi, Ouyang Yi, and D. Teneketzis | 2018 IEEE Conference on Decision and Control (CDC) |
| 17 | 2024 | 2.4 | Optimal Communication and Control Strategies in a Cooperative Multiagent MDP Problem ([link](https://doi.org/10.1109/TAC.2024.3386454)) | Sagar Sudhakara, Dhruva Kartik, Rahul Jain, and A. Nayyar | IEEE Transactions on Automatic Control |
| 18 | 2002 | 43 | Authority and Communication in Organizations ([link](https://doi.org/10.1111/1467-937X.00227)) | Wouter Dessein | The Review of Economic Studies |
| 19 | 2012 | 0.1 | Trusting the Messenger and the Message ([link](https://www.semanticscholar.org/paper/fbf1e71500b290141b59d8141d26e05135698da2)) | S. Villata et al. |  |
| 20 | 2000 | 165 | The information bottleneck method ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c)) | Naftali Tishby, Fernando C Pereira, and W. Bialek | ArXiv |
| 21 | 2021 |  | CGIBNet: Bandwidth-constrained Communication with Graph Information Bottleneck in Multi-Agent Reinforcement Learning ([link](https://www.semanticscholar.org/paper/b8316bb525fd6aa9b03a03be6598936c603efb65)) | Qi Tian, Kun Kuang, Baoxiang Wang, Furui Liu, and Fei Wu |  |
| 22 | 2015 | 2.3 | Rationally Inattentive Control of Markov Processes ([link](https://doi.org/10.1137/15M1008476)) | Ehsan Shafieepoorfard, M. Raginsky, and Sean P. Meyn | ArXiv |
| 23 | 2009 | 2.3 | Learning to trust in the competence and commitment of agents ([link](https://doi.org/10.1007/s10458-008-9055-8)) | Michael J. Smith and Marie desJardins | Autonomous Agents and Multi-Agent Systems |
| 24 | 2020 | 1.5 | State Aggregation for Multiagent Communication over Rate-Limited Channels ([link](https://doi.org/10.1109/GLOBECOM42002.2020.9322138)) | Arsham Mostaani, T. Vu, S. Chatzinotas, and B. Ottersten | GLOBECOM 2020 - 2020 IEEE Global Communications Conference |
| 25 | 1993 | 23 | The organization of decentralized information processing ([link](https://doi.org/10.2307/2951495)) | R. Radner | Econometrica |
| 26 | 2021 | 3.5 | Common Information based Approximate State Representations in Multi-Agent Reinforcement Learning ([link](https://www.semanticscholar.org/paper/c51231fad16b994da85035088c43ac0860a4fa64)) | Hsu Kao and V. Subramanian | International Conference on Artificial Intelligence and Statistics |
| 27 | 2014 | 10 | Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs ([link](https://doi.org/10.1109/TAC.2016.2601148)) | Takashi Tanaka, Kwang-Ki K. Kim, P. Parrilo, and S. Mitter | IEEE Transactions on Automatic Control |
| 28 | 2023 | 10 | Robust Multi-Agent Communication With Graph Information Bottleneck Optimization ([link](https://doi.org/10.1109/TPAMI.2023.3337534)) | Shifei Ding et al. | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| 29 | 2021 | 1.0 | Optimal communication and control strategies in a multi-agent MDP problem ([link](https://www.semanticscholar.org/paper/27ee2d143f61cdde2be3622c7415b37e96f3643d)) | Sagar Sudhakara, Dhruva Kartik, Rahul Jain, and A. Nayyar | ArXiv |
| 30 | 2015 | 1.1 | LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | ArXiv |
| 31 | 2001 | 1.1 | Communication Complexity and Coordination by Authority ([link](https://www.semanticscholar.org/paper/6058a6ecc7dcc59546cf1c0c8bc4d741b8cc7c2d)) | I. Segal |  |
| 32 | 2018 | 1.2 | Systems of Bounded Rational Agents with Information-Theoretic Constraints ([link](https://doi.org/10.1162/neco_a_01153)) | Sebastian Gottwald and Daniel A. Braun | Neural Computation |
| 33 | 2015 | 35 | Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach ([link](https://www.semanticscholar.org/paper/f583f9e720c16f6bb50f9d624b61c3bc851be008)) | Yinlam Chow, Aviv Tamar, Shie Mannor, and M. Pavone | ArXiv |
| 34 | 2018 | 7.9 | Learning to Share and Hide Intentions using Information Regularization ([link](https://www.semanticscholar.org/paper/70f4a0478f2979005b3628491c8b95335834cb64)) | D. Strouse, Max Kleiman-Weiner, J. Tenenbaum, M. Botvinick, and D. Schwab | ArXiv |
| 35 | 2014 | 4.6 | A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level ([link](https://doi.org/10.1109/TAC.2015.2500658)) | Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina | IEEE Transactions on Automatic Control |
| 36 | 2017 | 1.7 | Transfer-Entropy-Regularized Markov Decision Processes ([link](https://doi.org/10.1109/TAC.2021.3069347)) | Takashi Tanaka, H. Sandberg, and M. Skoglund | IEEE Transactions on Automatic Control |
| 37 | 2007 | 14 | Formal Trust Model for Multiagent Systems ([link](https://www.semanticscholar.org/paper/f14430e29ad3ff0fe4fb5a1a9ab507d34986bfa8)) | Yonghong Wang and Munindar P. Singh | International Joint Conference on Artificial Intelligence |
| 38 | 2012 | 4.9 | Nonanticipative Rate Distortion Function and Relations to Filtering Theory ([link](https://doi.org/10.1109/TAC.2013.2293403)) | C. Charalambous, Photios A. Stavrou, and N. Ahmed | IEEE Transactions on Automatic Control |
| 39 | 2022 | 6.5 | Trading off Utility, Informativeness, and Complexity in Emergent Communication ([link](https://doi.org/10.52202/068431-1614)) | Mycal Tucker, R. Levy, J. Shah, and Noga Zaslavsky | Advances in Neural Information Processing Systems 35 |
| 40 | 2017 | 5.1 | Fully Decentralized Policies for Multi-Agent Systems: An Information Theoretic Approach ([link](https://www.semanticscholar.org/paper/e6be7302cc97fe951a24f0b3c3c54995a20c7b12)) | Roel Dobbe, David Fridovich-Keil, and C. Tomlin | ArXiv |
| 41 | 2005 | 0.1 | A Model for Competence and Integrity in Variable Payoff Games ([link](https://www.semanticscholar.org/paper/66ef4e234cc16a56a33fa532330aadab9db77bea)) | Michael J. Smith and Marie desJardins |  |
| 42 | 2007 | 102 | You have printed the following article : Formal and Real Authority in Organizations ([link](https://dash.harvard.edu/bitstream/1/4554125/1/Aghion_FormalRealA.pdf)) | P. Aghion and Jean Tirole |  |
| 43 | 2019 | 2.3 | Common Knowledge and Sequential Team Problems ([link](https://doi.org/10.1109/TAC.2019.2912536)) | A. Nayyar and D. Teneketzis | IEEE Transactions on Automatic Control |
| 44 | 2015 | 3.9 | SDP-based joint sensor and controller design for information-regularized optimal LQG control ([link](https://doi.org/10.1109/CDC.2015.7402920)) | Takashi Tanaka and H. Sandberg | 2015 54th IEEE Conference on Decision and Control (CDC) |
| 45 | 2004 | 34 | Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates ([link](https://doi.org/10.1137/S0363012902402116)) | G. Nair and R. Evans | SIAM J. Control. Optim. |
| 46 | 2006 | 21 | The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link—Part I: Scalar Systems ([link](https://doi.org/10.1109/TIT.2006.878169)) | Anant Sahai and S. Mitter | IEEE Transactions on Information Theory |
| 47 |  |  | Quantization and Coding for Decentralized LTI Systems 1 ([link](https://www.semanticscholar.org/paper/9318fb88b89140c16558b5457beed0e78fb8ee9f)) | S. Yüksel and T. Başar |  |
| 48 | 2024 | 1.6 | Bayesian Persuasion: From Persuasion toward Counter-Suasion ([link](https://doi.org/10.1109/ISIT57864.2024.10619410)) | Ananya Das, Aishwarya Soni, and Amitalok J. Budkuley | 2024 IEEE International Symposium on Information Theory (ISIT) |
| 49 | 1995 | 0.9 | Communication Requirements for Individual Agents in Networks and Hierarchies ([link](https://doi.org/10.1007/978-1-4615-2261-4_12)) | T. Marschak and S. Reichelstein |  |
| 50 | 2008 | 2.6 | Identifying tractable decentralized control problems on the basis of information structure ([link](https://doi.org/10.1109/ALLERTON.2008.4797732)) | Aditya Mahajan, A. Nayyar, and D. Teneketzis | 2008 46th Annual Allerton Conference on Communication, Control, and Computing |
| 51 | 2022 | 8.7 | Learning Task-Oriented Channel Allocation for Multi-Agent Communication ([link](https://doi.org/10.1109/TVT.2022.3195202)) | Guojun He, Shibo Cui, Yueyue Dai, and Tao Jiang | IEEE Transactions on Vehicular Technology |
| 52 | 2017 |  | A Framework for Rate Efficient Control of Distributed Discrete Systems ([link](https://www.semanticscholar.org/paper/ac0c7221348c102a7c0b1265e7caa240742054b6)) | J. Ren, S. Torabi, and J. Walsh | ArXiv |
| 53 | 2009 | 0.6 | Decentralized Computation and Communication in Stabilization of Distributed Control Systems ([link](https://www.semanticscholar.org/paper/9f36932bd180b4549e07dc822d1271eaa18104e6)) | S. Yüksel |  |
| 54 | 1993 | 1.3 | Toward a theory of honesty and trust among communicating autonomous agents ([link](https://doi.org/10.1007/BF01384248)) | P. Gmytrasiewicz and E. Durfee | Group Decision and Negotiation |
| 55 | 1998 | 1.7 | Network Mechanisms, Informational Efficiency, and Hierarchies ([link](https://doi.org/10.1006/JETH.1997.2375)) | T. Marschak and S. Reichelstein | Journal of Economic Theory |
| 56 | 2015 | 0.4 | An algorithmic approach to identify irrelevant information in sequential teams ([link](https://doi.org/10.1016/j.automatica.2015.08.002)) | Aditya Mahajan and S. Tatikonda | Autom. |
| 57 | 2014 | 0.8 | A theory of sufficient statistics for teams ([link](https://doi.org/10.1109/CDC.2014.7039791)) | Jeff Wu and S. Lall | 53rd IEEE Conference on Decision and Control |
| 58 | 2016 | 3.7 | Rate of prefix-free codes in LQG control systems ([link](https://doi.org/10.1109/ISIT.2016.7541729)) | Takashi Tanaka, K. Johansson, T. Oechtering, H. Sandberg, and M. Skoglund | 2016 IEEE International Symposium on Information Theory (ISIT) |
| 59 | 1999 | 6.1 | Real-Time Decentralized Information Processing as a Model of Organizations with Boundedly Rational Agents ([link](https://doi.org/10.1111/1467-937X.00101)) | T. Zandt | The Review of Economic Studies |
| 60 | 1994 | 26 | The firm as a communication network ([link](https://doi.org/10.2307/2118349)) | M. Dewatripont and P. Bolton | ULB Institutional Repository |
| 61 | 2019 | 0.6 | Too good to be truthful: Why competent advisers are fired ([link](https://doi.org/10.2139/SSRN.2759803)) | Christoph Schottmüller | J. Econ. Theory |
| 62 | 2021 | 0.2 | Multi-agent Communication with Graph Information Bottleneck under Limited Bandwidth ([link](https://www.semanticscholar.org/paper/de7e81b1c897c85e0bc88e6644ece43bcac06c4f)) | Qi Tian, Kun Kuang, Baoxiang Wang, Furui Liu, and Fei Wu | ArXiv |
| 63 | 2024 | 5.6 | Learning Efficient and Robust Multi-Agent Communication via Graph Information Bottleneck ([link](https://doi.org/10.1609/aaai.v38i16.29682)) | Shifei Ding, Wei Du, Ling Ding, Lili Guo, and Jian Zhang | AAAI Conference on Artificial Intelligence |
| 64 | 2022 | 0.5 | Intent-Grounded Compositional Communication through Mutual Information in Multi-Agent Teams ([link](https://www.semanticscholar.org/paper/b8089cce7ab740c03daff13af6f9c2d62b004df7)) | Seth Karten and K. Sycara |  |
| 65 | 2000 | 1.4 | Information Bottlenecks, Causal States, and Statistical Relevance Bases: How to Represent Relevant Information in memoryless transduction ([link](https://doi.org/10.1142/S0219525902000481)) | C. Shalizi and J. Crutchfield | Adv. Complex Syst. |
| 66 | 2014 | 0.3 | Sufficient statistics for multi-agent decision problems ([link](https://doi.org/10.1109/ALLERTON.2014.7028492)) | Jeffrey N. Wu and S. Lall | 2014 52nd Annual Allerton Conference on Communication, Control, and Computing (Allerton) |
| 67 | 2015 | 0.3 | Sufficient statistics for dynamic teams ([link](https://doi.org/10.1109/ACC.2015.7172194)) | Jeff Wu and S. Lall | 2015 American Control Conference (ACC) |
| 68 | 1998 | 2.7 | Control of LQG systems under communication constraints ([link](https://doi.org/10.1109/CDC.1998.760856)) | S. Tatikonda, A. Sahai, and S. Mitter | Proceedings of the 37th IEEE Conference on Decision and Control (Cat. No.98CH36171) |
| 69 | 1999 | 3.9 | Control of LQG systems under communication constraints ([link](https://doi.org/10.1109/ACC.1999.786578)) | S. Tatikonda, Anant Sahai, and S. Mitter | Proceedings of the 1999 American Control Conference (Cat. No. 99CH36251) |
| 70 | 1997 | 5.4 | LQG Control with Communication Constraints ([link](https://doi.org/10.1007/978-1-4615-6281-8_21)) | V. Borkar and S. Mitter |  |
| 71 | 1999 | 34 | Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback ([link](https://doi.org/10.1109/9.763226)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 72 | 2003 |  | Abstract communication for coordinated planning ([link](https://www.semanticscholar.org/paper/fd601ccbf5cf6e2037716ce9b9d350984a2094bd)) | B. Clement and E. Durfee |  |
| 73 | 2025 | 1.3 | Sequential Non-Bayesian Persuasion ([link](https://www.semanticscholar.org/paper/341a1f322f09fe90928da1e5bba044e313da8595)) | Yaron Azrieli and Rachana Das |  |
| 74 | 2010 | 5.6 | Combining statistics and arguments to compute trust ([link](https://doi.org/10.1145/1838206.1838236)) | P. Matt, Maxime Morge, and Francesca Toni | Adaptive Agents and Multi-Agent Systems |
| 75 | 2024 | 4.8 | Effective Multi-Agent Communication Under Limited Bandwidth ([link](https://doi.org/10.1109/TMC.2023.3339213)) | Lebin Yu et al. | IEEE Transactions on Mobile Computing |
| 76 | 2023 | 1.2 | On the Role of Emergent Communication for Social Learning in Multi-Agent Reinforcement Learning ([link](https://doi.org/10.48550/arXiv.2302.14276)) | Seth Karten, Siva Kailas, Huao Li, and K. Sycara | ArXiv |
| 77 | 2009 | 5.2 | Past-future information bottleneck in dynamical systems. ([link](https://doi.org/10.1103/PHYSREVE.79.041925)) | F. Creutzig, A. Globerson, and Naftali Tishby | Physical review. E, Statistical, nonlinear, and soft matter physics |
| 78 | 2016 | 0.2 | Approximate Sufficient Statistics for Team Decision Problems ([link](https://www.semanticscholar.org/paper/e7a9b3f09a038409b3d2ddbad567ba4661817921)) | A. Lemon and S. Lall | AAAI Spring Symposia |
| 79 | 2017 | 0.1 | Static teams with common information ([link](https://doi.org/10.1016/J.IFACOL.2017.08.1449)) | A. Mahajan and Mohammad Afshari | IFAC-PapersOnLine |
| 80 | 1982 | 0.1 | Sufficient statistics in team control problems with a common past ([link](https://doi.org/10.1109/CDC.1982.268424)) | G. Casalino, F. Davoli, R. Minciardi, and R. Zoppoli | 1982 21st IEEE Conference on Decision and Control |
| 81 | 1982 | 0.0 | Sufficient Statistics for Decentralized Estimation ([link](https://www.semanticscholar.org/paper/7e19933d0ace871b735aac534cd64c91cc7b3edf)) | R. Tenney and Decision Systems. |  |
| 82 | 2012 | 0.1 | Distributed estimation in multi-agent networks ([link](https://doi.org/10.1109/ISIT.2012.6284202)) | L. Sankar and H. Poor | 2012 IEEE International Symposium on Information Theory Proceedings |
| 83 | 2005 | 1.0 | Cooperation vs. hierarchy: an information-theoretic comparison ([link](https://doi.org/10.1109/ISIT.2005.1523366)) | L. Sankar, G. Kramer, and N. Mandayam | Proceedings. International Symposium on Information Theory, 2005. ISIT 2005. |
| 84 | 2023 | 0.6 | Low Entropy Communication in Multi-Agent Reinforcement Learning ([link](https://doi.org/10.1109/ICC45041.2023.10278640)) | Lebin Yu, Yunbo Qiu, Qiexiang Wang, Xudong Zhang, and Jian Wang | ICC 2023 - IEEE International Conference on Communications |
| 85 | 2024 | 1.3 | Reinforcement Learning over Noisy Channels: An Information Bottleneck Approach ([link](https://doi.org/10.1109/MILCOM61039.2024.10773737)) | Clement Kam, J. Macker, and Yin Sun | MILCOM 2024 - 2024 IEEE Military Communications Conference (MILCOM) |
| 86 | 2014 | 5.1 | Information Bottleneck Approach to Predictive Inference ([link](https://doi.org/10.3390/e16020968)) | Susanne Still | Entropy |
| 87 | 1999 | 1.7 | Information Aggregation and Communication in Organizations ([link](https://doi.org/10.1287/MNSC.45.5.659)) | P. Jehiel | Management Science |
| 88 | 1982 | 0.2 | Order transmission efficiency in large hierarchical organizations ([link](https://doi.org/10.1080/00207728208926367)) | B. Roehner | International Journal of Systems Science |
| 89 | 1994 | 56 | Formalising Trust as a Computational Concept ([link](https://www.semanticscholar.org/paper/8c584c4820e615aaf3c40a6737315c712ecd6927)) | S. Marsh |  |
| 90 | 1998 | 23 | Principles of trust for MAS: cognitive anatomy, social importance, and quantification ([link](https://doi.org/10.1109/ICMAS.1998.699034)) | C. Castelfranchi and R. Falcone | Proceedings International Conference on Multi Agent Systems (Cat. No.98EX160) |

### Paper Details

1\. · 100% match · 2004 · 80 cit/yr\
**Control under communication constraints** ([link](https://doi.org/10.1109/TAC.2004.831187))\
S. Tatikonda and S. Mitter\
*IEEE Transactions on Automatic Control* · Jul 12, 2004 · 1745 citations

------------------------------------------------------------------------

2\. · 100% match · 2012 · 22 cit/yr\
**Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach** ([link](https://doi.org/10.1109/TAC.2013.2239000))\
A. Nayyar, Aditya Mahajan, and D. Teneketzis\
*IEEE Transactions on Automatic Control* · Sep 7, 2012 · 305 citations

> A general model of decentralized stochastic control called partial history sharing information structure is presented. In this model, at each step the controllers share part of their observation and control history with each other. This general model subsumes several existing models of information sharing as special cases. Based on the information commonly known to all the controllers, the decentralized problem is reformulated as an equivalent centralized problem from the perspective of a coordinator. The coordinator knows the common information and selects prescriptions that map each controller’s local information to its control actions. The optimal control problem at the coordinator is shown to be a partially observable Markov decision process (POMDP) which is solved using techniques from Markov decision theory. This approach provides 1) structural results for optimal strategies and 2) a dynamic program for obtaining optimal strategies for all controllers in the original decentralized problem. Thus, this approach unifies the various ad-hoc approaches taken in the literature. In addition, the structural results on optimal control strategies obtained by the proposed approach cannot be obtained by the existing generic approach (the person-by-person approach) for obtaining structural results in decentralized problems; and the dynamic program obtained by the proposed approach is simpler than that obtained by the existing generic approach (the designer’s approach) for obtaining dynamic programs in decentralized problems.

------------------------------------------------------------------------

3\. · 100% match · 2015 · 11 cit/yr\
**LQG Control With Minimum Directed Information: Semidefinite Programming Approach** ([link](https://doi.org/10.1109/TAC.2017.2709618))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*IEEE Transactions on Automatic Control* · Oct 14, 2015 · 113 citations

> We consider a discrete-time linear–quadratic–Gaussian (LQG) control problem, in which Massey’s directed information from the observed output of the plant to the control input is minimized, while required control performance is attainable. This problem arises in several different contexts, including joint encoder and controller design for data-rate minimization in networked control systems. We show that the optimal control law is a linear–Gaussian randomized policy. We also identify the state-space realization of the optimal policy, which can be synthesized by an efficient algorithm based on semidefinite programming. Our structural result indicates that the filter–controller separation principle from the LQG control theory and the sensor–filter separation principle from the zero-delay rate-distortion theory for Gauss–Markov sources hold simultaneously in the considered problem. A connection to the data-rate theorem for mean-square stability by Nair and Evans is also established.

------------------------------------------------------------------------

4\. · 100% match · 2019 · 20 cit/yr\
**Learning Efficient Multi-agent Communication: An Information Bottleneck Approach** ([link](https://www.semanticscholar.org/paper/ac7fbe27a47236689bf2076e7ffc9561a06941e1))\
R. Wang et al.\
*International Conference on Machine Learning* · Nov 16, 2019 · 133 citations

> We consider the problem of the limited-bandwidth communication for multi-agent reinforcement learning, where agents cooperate with the assistance of a communication protocol and a scheduler. The protocol and scheduler jointly determine which agent is communicating what message and to whom. Under the limited bandwidth constraint, a communication protocol is required to generate informative messages. Meanwhile, an unnecessary communication connection should not be established because it occupies limited resources in vain. In this paper, we develop an Informative Multi-Agent Communication (IMAC) method to learn efficient communication protocols as well as scheduling. First, from the perspective of communication theory, we prove that the limited bandwidth constraint requires low-entropy messages throughout the transmission. Then inspired by the information bottleneck principle, we learn a valuable and compact communication protocol and a weight-based scheduler. To demonstrate the efficiency of our method, we conduct extensive experiments in various cooperative and competitive multi-agent tasks with different numbers of agents and different bandwidths. We show that IMAC converges faster and leads to efficient communication among agents under the limited bandwidth as compared to many baseline methods.

------------------------------------------------------------------------

5\. · 100% match · 2016 · 1.8 cit/yr\
**Minimum-information LQG control part I: Memoryless controllers** ([link](https://doi.org/10.1109/CDC.2016.7799131))\
Roy Fox and Naftali Tishby\
*2016 IEEE 55th Conference on Decision and Control (CDC)* · Jun 6, 2016 · 18 citations

> With the increased demand for power efficiency in feedback-control systems, communication is becoming a limiting factor, raising the need to trade off the external cost that they incur with the capacity of the controller’s communication channels. With a proper design of the channels, this translates into a sequential rate-distortion problem, where we minimize the rate of information required for the controller’s operation under a constraint on its external cost. Memoryless controllers are of particular interest both for the simplicity and frugality of their implementation and as a basis for studying more complex controllers. In this paper we present the optimality principle for memoryless linear controllers that utilize minimal information rates to achieve a guaranteed external-cost level. We also study the interesting and useful phenomenology of the optimal controller, such as the principled reduction of its order.

------------------------------------------------------------------------

6\. · 100% match · 2021 · 22 cit/yr\
**Communication in Multi-Agent Reinforcement Learning: Intention Sharing** ([link](https://www.semanticscholar.org/paper/9ed9ff62749f450247d1f6be9d1c14142fa63f05))\
Woojun Kim, Jongeui Park, and Y. Sung\
*International Conference on Learning Representations* · 116 citations

------------------------------------------------------------------------

7\. · 100% match · 2026\
**Robust Trust** ([link](https://www.semanticscholar.org/paper/8d3536ffc54dc01feeb4211ef93252e48f1e93a2))\
Piotr Dworczak and A. Smolin\
Feb 10, 2026 · 0 citations

> An agent chooses an action based on her private information and a recommendation from an informed but potentially misaligned adviser. With a known probability, the adviser truthfully reports his signal; with the remaining probability, he can send any message. We characterize optimal robust decision rules that maximize the agent’s worst-case expected payoff. Every optimal rule is equivalent to a trust-region policy in belief space: the adviser’s reported beliefs are taken at face value if they fall within the trust region but are otherwise clipped to the trust region’s boundary. We derive alignment thresholds above which advice is strictly valuable and fully characterize the solution in both binary-state and binary-action environments.

------------------------------------------------------------------------

8\. · 100% match · 2016 · 1.3 cit/yr\
**Minimum-information LQG control Part II: Retentive controllers** ([link](https://doi.org/10.1109/CDC.2016.7799130))\
Roy Fox and Naftali Tishby\
*2016 IEEE 55th Conference on Decision and Control (CDC)* · Jun 6, 2016 · 13 citations

> Retentive (memory-utilizing) sensing-acting agents may operate under limitations on the communication between their sensing, memory and acting components, requiring them to trade off the external cost that they incur with the capacity of their communication channels. In this paper we formulate this problem as a sequential rate-distortion problem of minimizing the rate of information required for the controller’s operation under a constraint on its external cost. We reduce this bounded retentive control problem to the memoryless one, studied in Part I of this work \[1\], by viewing the memory reader as one more sensor and the memory writer as one more actuator. We further investigate the structure of the resulting optimal solution and demonstrate its interesting phenomenology.

------------------------------------------------------------------------

9\. · 100% match · 2022 · 3.6 cit/yr\
**A Unified Approach to Dynamic Decision Problems With Asymmetric Information: Nonstrategic Agents** ([link](https://doi.org/10.1109/TAC.2021.3060835))\
Hamidreza Tavafoghi, Ouyang Yi, and D. Teneketzis\
*IEEE Transactions on Automatic Control* · Mar 1, 2022 · 15 citations

> We study a general class of dynamic multi- agent decision problems with asymmetric information and nonstrategic agents, which include dynamic teams as a special case. When agents are nonstrategic, an agent’s strategy is known to the other agents. Nevertheless, the agents’ strategy choices and beliefs are interdependent over times, a phenomenon known as signaling. We introduce the notion of sufficient information that effectively compresses the agents’ information in a mutually consistent manner. Based on the notion of sufficient information, we propose an information state for each agent that is sufficient for decision-making purposes. We present instances of dynamic multiagent decision problems where we can determine an information state with a time-invariant domain for each agent. Furthermore, we present a generalization of the policy-independence property of belief in partially observed Markov decision processes (POMDP) to dynamic multiagent decision problems. Within the context of dynamic teams with asymmetric information, the proposed set of information states leads to a sequential decomposition that decouples the interdependence between the agents’ strategies and beliefs over time and enables us to formulate a dynamic program to determine a globally optimal policy via backward induction.

------------------------------------------------------------------------

10\. · 100% match · 2012 · 9.4 cit/yr\
**Epistemic trust: modeling children’s reasoning about others’ knowledge and intent.** ([link](https://doi.org/10.1111/j.1467-7687.2012.01135.x))\
Patrick Shafto, Baxter S. Eaves, Danielle Navarro, and A. Perfors\
*Developmental science* · May 1, 2012 · 132 citations

> A core assumption of many theories of development is that children can learn indirectly from other people. However, indirect experience (or testimony) is not constrained to provide veridical information. As a result, if children are to capitalize on this source of knowledge, they must be able to infer who is trustworthy and who is not. How might a learner make such inferences while at the same time learning about the world? What biases, if any, might children bring to this problem? We address these questions with a computational model of epistemic trust in which learners reason about the helpfulness and knowledgeability of an informant. We show that the model captures the competencies shown by young children in four areas: (1) using informants’ accuracy to infer how much to trust them; (2) using informants’ recent accuracy to overcome effects of familiarity; (3) inferring trust based on consensus among informants; and (4) using information about mal-intent to decide not to trust. The model also explains developmental changes in performance between 3 and 4 years of age as a result of changing default assumptions about the helpfulness of other people.

------------------------------------------------------------------------

11\. · 100% match · 2004 · 20 cit/yr\
**Stochastic linear control over a communication channel** ([link](https://doi.org/10.1109/TAC.2004.834430))\
S. Tatikonda, Anant Sahai, and S. Mitter\
*IEEE Transactions on Automatic Control* · Sep 13, 2004 · 442 citations

------------------------------------------------------------------------

12\. · 100% match · 2020 · 1.0 cit/yr\
**Task-Based Information Compression for Multi-Agent Communication Problems with Channel Rate Constraints** ([link](https://www.semanticscholar.org/paper/0218f804322c63ada943788c95d38266ae0a9ca5))\
Arsham Mostaani, T. Vu, S. Chatzinotas, and B. Ottersten\
*ArXiv* · May 28, 2020 · 6 citations

> A collaborative task is assigned to a multiagent system (MAS) in which agents are allowed to communicate. The MAS runs over an underlying Markov decision process and its task is to maximize the averaged sum of discounted one-stage rewards. Although knowing the global state of the environment is necessary for the optimal action selection of the MAS, agents are limited to individual observations. The inter-agent communication can tackle the issue of local observability, however, the limited rate of the inter-agent communication prevents the agent from acquiring the precise global state information. To overcome this challenge, agents need to communicate their observations in a compact way such that the MAS compromises the minimum possible sum of rewards. We show that this problem is equivalent to a form of rate-distortion problem which we call the task-based information compression. We introduce two schemes for task-based information compression (i) Learning-based information compression (LBIC) which leverages reinforcement learning to compactly represent the observation space of the agents, and (ii) State aggregation for information compression (SAIC), for which a state aggregation algorithm is analytically designed. The SAIC is shown, conditionally, to be capable of achieving the optimal performance in terms of the attained sum of discounted rewards. The proposed algorithms are applied to a rendezvous problem and their performance is compared with two benchmarks; (i) conventional source coding algorithms and the (ii) centralized multiagent control using reinforcement learning. Numerical experiments confirm the superiority of the proposed algorithms.

------------------------------------------------------------------------

13\. · 100% match · 2023 · 2.1 cit/yr\
**Minimizing Return Gaps with Discrete Communications in Decentralized POMDP** ([link](https://doi.org/10.48550/arXiv.2308.03358))\
Jingdi Chen and Tian Lan\
*ArXiv* · 7 citations

> Communication is crucial for solving cooperative Multi-Agent Reinforcement Learning tasks in Partially-Observable Markov Decision Processes. Existing works often rely on black-box methods to encode local information/features into messages shared with other agents. However, such black-box approaches are unable to provide any quantitative guarantees on the expected return and often lead to the generation of continuous messages with high communication overhead and poor interpretability. In this paper, we establish an upper bound on the return gap between an ideal policy with full observability and an optimal partially-observable policy with discrete communication. This result enables us to recast multi-agent communication into a novel online clustering problem over the local observations at each agent, with messages as cluster labels and the upper bound on the return gap as clustering loss. By minimizing the upper bound, we propose a surprisingly simple design of message generation functions in multi-agent communication and integrate it with reinforcement learning using a Regularized Information Maximization loss function. Evaluations show that the proposed discrete communication significantly outperforms state-of-the-art multi-agent communication baselines and can achieve nearly-optimal returns with few-bit messages that are naturally interpretable.

------------------------------------------------------------------------

14\. · 100% match · 2001\
**Complexity and Coordination by Authority ∗** ([link](https://www.semanticscholar.org/paper/155c4af62e235caa0e48f6484b4250aab8676466))\
I. Segal\
0 citations

> We prove that the simplest communication allowing two players to coordinate on a course of action is authority (letting one player choose an action). We also consider the case where each player possesses valuable information about the benefits of a large number of actions. For this case, we identify conditions under which authority can only be asymptotically improved upon by protocols of exponential complexity in the number of actions (i.e. those describing an unbounded number of actions). ∗I am greatly indebted to Eric Maskin for his thorough reading of earlier versions of the paper and many valuable suggestions. I am grateful to Daron Acemoglu, Philippe Aghion, Susan Athey, Abhijit Banerjee, Alberto Bisin, Drew Fudenberg, Oliver Hart, Bengt Holmstrom, Eric Maskin, Thomas Marschak, Paul Milgrom, Antonio Rangel, Steve Tadelis, Jean Tirole, and participants of seminars at Berkeley, Harvard, and MIT for helpful comments and discussions, to Edouard Servan-Schreiber for valuable research assistance, and to Alfred P. Sloan foundation and UC Berkeley’s Committee on Research for financial support. “Fundamentally, communication is required to translate purpose into terms of the concrete action required to effect it what to do and when and where to do it \[…\] Under very simple and usually temporary conditions and with small numbers of persons the communication problem often appears simple, but under many conditions, even with small numbers, a special channel of communication is required. For if all talk at once there is confusion, and there is indecision particularly as to timing of actions. This creates the necessity for a leader.” Chester Barnard (1938)

------------------------------------------------------------------------

15\. · 100% match · 2024 · 1.3 cit/yr\
**Cooperation and Control in Delegation Games** ([link](https://doi.org/10.24963/ijcai.2024/26))\
Oliver Sourbut, Lewis Hammond, and Harriet Wood\
*ArXiv* · Feb 24, 2024 · 3 citations

> Many settings of interest involving humans and machines – from virtual personal assistants to autonomous vehicles – can naturally be modelled as principals (humans) delegating to agents (machines), which then interact with each other on their principals’ behalf. We refer to these multi-principal, multi-agent scenarios as delegation games. In such games, there are two important failure modes: problems of control (where an agent fails to act in line their principal’s preferences) and problems of cooperation (where the agents fail to work well together). In this paper we formalise and analyse these problems, further breaking them down into issues of alignment (do the players have similar preferences?) and capabilities (how competent are the players at satisfying those preferences?). We show – theoretically and empirically – how these measures determine the principals’ welfare, how they can be estimated using limited observations, and thus how they might be used to help us design more aligned and cooperative AI systems.

------------------------------------------------------------------------

16\. · 100% match · 2018 · 1.1 cit/yr\
**A Sufficient Information Approach to Decentralized Decision Making** ([link](https://doi.org/10.1109/CDC.2018.8619040))\
Hamidreza Tavafoghi, Ouyang Yi, and D. Teneketzis\
*2018 IEEE Conference on Decision and Control (CDC)* · Dec 1, 2018 · 8 citations

> We study a general class of decentralized dynamic decision-making problems with many agents, asymmetric information, and hidden actions. We propose the notion of sufficient information that provides a mutually consistent compression of the agents’ private and common information for decision-making purposes. We define a class of strategies, called sufficient information-based (SIB) strategies, that are based on the agents’ sufficient information. We show that restriction to SIB strategies is without loss of optimality in decentralized decision problems with non-strategic agents (i.e. teams). Accordingly, we provide a sequential decomposition of dynamic teams over time that specifies an algorithm for determining globally optimal strategies. For decentralized decision problems with strategic agents (i.e. games), we show that the class of SIB strategies is closed under the best response map. Consequently, we propose a notion of sufficient information-based equilibrium and provide a sequential decomposition of dynamic games over time that specifies an algorithm for determining Sufficient Information Based Perfect Bayesian Equilibria (SIB-PBE).

------------------------------------------------------------------------

17\. · 100% match · 2024 · 2.4 cit/yr\
**Optimal Communication and Control Strategies in a Cooperative Multiagent MDP Problem** ([link](https://doi.org/10.1109/TAC.2024.3386454))\
Sagar Sudhakara, Dhruva Kartik, Rahul Jain, and A. Nayyar\
*IEEE Transactions on Automatic Control* · Oct 1, 2024 · 4 citations

> The problem of controlling cooperative multiagent systems under different models of information sharing among agents has received significant attention in the recent literature. In this article, we consider a setup where rather than committing to a fixed and nonadaptive information sharing protocol (e.g., periodic sharing or no sharing, etc.), agents can dynamically decide at each time step whether to share information with each other and incur the resulting communication cost. This setup requires a joint design of agents’ communication and control strategies in order to optimize the tradeoff between communication costs and the control objective. We first show that agents can ignore a big part of their private information without compromising the system performance. We then provide a common-information-approach-based solution for the strategy optimization problem. This approach relies on constructing a fictitious partially observable markov decision process (POMDP) whose solution (obtained via a dynamic program) characterizes the optimal strategies for the agents. We extend our solution to incorporate time-varying packet-drop channels and constraints on when and how frequently agents can communicate.

------------------------------------------------------------------------

18\. · 100% match · 2002 · 43 cit/yr\
**Authority and Communication in Organizations** ([link](https://doi.org/10.1111/1467-937X.00227))\
Wouter Dessein\
*The Review of Economic Studies* · Oct 1, 2002 · 1019 citations

> This paper studies delegation as an alternative to communication. We show that a principal prefers to delegate control to a better informed agent rather than to communicate with this agent as long as the incentive conflict is not too large relative to the principal’s uncertainty about the environment. We further identify cases in which the principal optimally delegates control to an “intermediary”, and show that keeping a veto-right typically reduces the expected utility of the principal unless the incentive conflict is extreme. Copyright 2002, Wiley-Blackwell.

------------------------------------------------------------------------

19\. · 100% match · 2012 · 0.1 cit/yr\
**Trusting the Messenger and the Message** ([link](https://www.semanticscholar.org/paper/fbf1e71500b290141b59d8141d26e05135698da2))\
S. Villata et al.\
2 citations

> Information provided by a source should be assessed by an intelligent agent on the basis of several criteria: most notably, its content and the trust one has in its source. In turn, the observed quality of information should feed back on the assessment of its source, and such feedback should intelligently distribute among different features of the source—e.g., competence and sincerity. We propose a formal framework in which trust is not treated as a monolithic and static concept. We regard trust as a multi-dimensional concept relativized to the sincerity of the source and its competence with respect to specific domains: both these aspects influence the assessment of the information, and also determine a feedback on the trustworthiness degree of its source. We provide a framework to describe the combined effects of competence and sincerity on the perceived quality of information. We focus on the feedback dynamics from information quality to source evaluation, highlighting the role that uncertainty reduction, and social comparison play in determining the amount and the distribution of feedback. Category: I.2.11, Distributed Artificial Intelligence, Intelligent agents

------------------------------------------------------------------------

20\. · 100% match · 2000 · 165 cit/yr\
**The information bottleneck method** ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c))\
Naftali Tishby, Fernando C Pereira, and W. Bialek\
*ArXiv* · Apr 24, 2000 · 4311 citations

> We define the relevant information in a signal $`x\in X`$ as being the information that this signal provides about another signal $`y\in \Y`$. Examples include the information that face images provide about the names of the people portrayed, or the information that speech sounds provide about the words spoken. Understanding the signal $`x`$ requires more than just predicting $`y`$, it also requires specifying which features of $`\X`$ play a role in the prediction. We formalize this problem as that of finding a short code for $`\X`$ that preserves the maximum information about $`\Y`$. That is, we squeeze the information that $`\X`$ provides about $`\Y`$ through a \`bottleneck’ formed by a limited set of codewords $`\tX`$. This constrained optimization problem can be seen as a generalization of rate distortion theory in which the distortion measure $`d(x,\x)`$ emerges from the joint statistics of $`\X`$ and $`\Y`$. This approach yields an exact set of self consistent equations for the coding rules $`X \to \tX`$ and $`\tX \to \Y`$. Solutions to these equations can be found by a convergent re-estimation method that generalizes the Blahut-Arimoto algorithm. Our variational principle provides a surprisingly rich framework for discussing a variety of problems in signal processing and learning, as will be described in detail elsewhere.

------------------------------------------------------------------------

21\. · 100% match · 2021\
**CGIBNet: Bandwidth-constrained Communication with Graph Information Bottleneck in Multi-Agent Reinforcement Learning** ([link](https://www.semanticscholar.org/paper/b8316bb525fd6aa9b03a03be6598936c603efb65))\
Qi Tian, Kun Kuang, Baoxiang Wang, Furui Liu, and Fei Wu\
Dec 20, 2021 · 0 citations

> Communication is one of the core components for cooperative multi-agent reinforcement learning (MARL). The communication bandwidth, in many real applications, is always subject to certain constraints. To improve communication efficiency, in this article, we propose to simultaneously optimize whom to communicate with and what to communicate for each agent in MARL. By initiating the communication between agents with a directed complete graph, we propose a novel communication model, named Communicative Graph Information Bottleneck Network (CGIBNet), to simultaneously compress the graph structure and the node information with the graph information bottleneck principle. The graph structure compression is designed to cut the redundant edges for determining whom to communicate with. The node information compression aims to address the problem of what to communicate via learning compact node representations. Moreover, CGIBNet is the first universal module for bandwidth-constrained communication, which can be applied to various training frameworks (i.e., policy-based and value-based MARL frameworks) and communication modes (i.e., single-round and multi-round communication). Extensive experiments are conducted in Traffic Control and StarCraft II environments. The results indicate that our method can achieve better performance in bandwidth-constrained settings compared with state-of-the-art algorithms.

------------------------------------------------------------------------

22\. · 100% match · 2015 · 2.3 cit/yr\
**Rationally Inattentive Control of Markov Processes** ([link](https://doi.org/10.1137/15M1008476))\
Ehsan Shafieepoorfard, M. Raginsky, and Sean P. Meyn\
*ArXiv* · Feb 12, 2015 · 26 citations

> The article poses a general model for optimal control subject to information constraints, motivated in part by recent work of Sims and others on information-constrained decision-making by economic agents. In the average-cost optimal control framework, the general model introduced in this paper reduces to a variant of the linear-programming representation of the average-cost optimal control problem, subject to an additional mutual information constraint on the randomized stationary policy. The resulting optimization problem is convex and admits a decomposition based on the Bellman error, which is the object of study in approximate dynamic programming. The theory is illustrated through the example of information-constrained linear-quadratic-Gaussian (LQG) control problem. Some results on the infinite-horizon discounted-cost criterion are also presented.

------------------------------------------------------------------------

23\. · 100% match · 2009 · 2.3 cit/yr\
**Learning to trust in the competence and commitment of agents** ([link](https://doi.org/10.1007/s10458-008-9055-8))\
Michael J. Smith and Marie desJardins\
*Autonomous Agents and Multi-Agent Systems* · Feb 1, 2009 · 39 citations

------------------------------------------------------------------------

24\. · 100% match · 2020 · 1.5 cit/yr\
**State Aggregation for Multiagent Communication over Rate-Limited Channels** ([link](https://doi.org/10.1109/GLOBECOM42002.2020.9322138))\
Arsham Mostaani, T. Vu, S. Chatzinotas, and B. Ottersten\
*GLOBECOM 2020 - 2020 IEEE Global Communications Conference* · Dec 1, 2020 · 8 citations

> A collaborative task is assigned to a multiagent system (MAS) in which agents are allowed to communicate. The MAS runs over an underlying Markov decision process and its task is to maximize the averaged sum of discounted one-stage rewards. Although knowing the global state of the environment is necessary for the optimal action selection of the MAS, agents are limited to individual observations. The inter-agent communication can tackle the issue of local observability, however, the limited rate of the inter-agent communication prevents the agents from acquiring the precise global state information. To overcome this challenge, agents need to communicate their observations in a compact way such that the MAS compromises the minimum possible sum of rewards. We show that this problem is equivalent to a form of rate-distortion problem which we call the task-based information compression. State Aggregation for Information Compression (SAIC) is introduced here to perform the task-based information compression. The SAIC is shown, conditionally, to be capable of achieving the optimal performance in terms of the attained sum of discounted rewards. The proposed algorithm is applied to a rendezvous problem and its performance is compared with two benchmarks; (i) conventional source coding algorithms and the (ii) centralized multiagent control using reinforcement learning. Numerical experiments confirm the superiority and fast convergence of the proposed SAIC.

------------------------------------------------------------------------

25\. · 100% match · 1993 · 23 cit/yr\
**The organization of decentralized information processing** ([link](https://doi.org/10.2307/2951495))\
R. Radner\
*Econometrica* · Sep 1, 1993 · 765 citations

> In a decision-theoretic model of a firm, the author represents managers as information processors of limited capacity; efficiency is measured in terms of (1) the number of processors and (2) the delay between the receipt of information by the organization and the implementation of the decision. The author characterizes efficient networks for both one-shot and repeated regimes, as well as the corresponding ‘production function’ relating the number of items processed to the number of processors and the delay. He sketches some applications to common decision paradigms, and implications for decentralization and organizational returns to scale. Copyright 1993 by The Econometric Society.

------------------------------------------------------------------------

26\. · 100% match · 2021 · 3.5 cit/yr\
**Common Information based Approximate State Representations in Multi-Agent Reinforcement Learning** ([link](https://www.semanticscholar.org/paper/c51231fad16b994da85035088c43ac0860a4fa64))\
Hsu Kao and V. Subramanian\
*International Conference on Artificial Intelligence and Statistics* · Oct 25, 2021 · 16 citations

> Due to information asymmetry, finding optimal policies for Decentralized Partially Observable Markov Decision Processes (Dec-POMDPs) is hard with the complexity growing doubly exponentially in the horizon length. The challenge increases greatly in the multi-agent reinforcement learning (MARL) setting where the transition probabilities, observation kernel, and reward function are unknown. Here, we develop a general compression framework with approximate common and private state representations, based on which decentralized policies can be constructed. We derive the optimality gap of executing dynamic programming (DP) with the approximate states in terms of the approximation error parameters and the remaining time steps. When the compression is exact (no error), the resulting DP is equivalent to the one in existing work. Our general framework generalizes a number of methods proposed in the literature. The results shed light on designing practically useful deep-MARL network structures under the”centralized learning distributed execution”scheme.

------------------------------------------------------------------------

27\. · 100% match · 2014 · 10 cit/yr\
**Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs** ([link](https://doi.org/10.1109/TAC.2016.2601148))\
Takashi Tanaka, Kwang-Ki K. Kim, P. Parrilo, and S. Mitter\
*IEEE Transactions on Automatic Control* · Nov 27, 2014 · 120 citations

> Sequential rate-distortion (SRD) theory provides a framework for studying the fundamental trade-off between data-rate and data-quality in real-time communication systems. In this paper, we consider the SRD problem for multi-dimensional time-varying Gauss-Markov processes under mean-square distortion criteria. We first revisit the sensor-estimator separation principle, which asserts that considered SRD problem is equivalent to a joint sensor and estimator design problem in which data-rate of the sensor output is minimized while the estimator’s performance satisfies the distortion criteria. We then show that the optimal joint design can be performed by semidefinite programming. A semidefinite representation of the corresponding SRD function is obtained. Implications of the obtained result in the context of zero-delay source coding theory and applications to networked control theory are also discussed.

------------------------------------------------------------------------

28\. · 100% match · 2023 · 10 cit/yr\
**Robust Multi-Agent Communication With Graph Information Bottleneck Optimization** ([link](https://doi.org/10.1109/TPAMI.2023.3337534))\
Shifei Ding et al.\
*IEEE Transactions on Pattern Analysis and Machine Intelligence* · Nov 29, 2023 · 25 citations

> Recent research on multi-agent reinforcement learning (MARL) has shown that action coordination of multi-agents can be significantly enhanced by introducing communication learning mechanisms. Meanwhile, graph neural network (GNN) provides a promising paradigm for communication learning of MARL. Under this paradigm, agents and communication channels can be regarded as nodes and edges in the graph, and agents can aggregate information from neighboring agents through GNN. However, this GNN-based communication paradigm is susceptible to adversarial attacks and noise perturbations, and how to achieve robust communication learning under perturbations has been largely neglected. To this end, this paper explores this problem and introduces a robust communication learning mechanism with graph information bottleneck optimization, which can optimally realize the robustness and effectiveness of communication learning. We introduce two information-theoretic regularizers to learn the minimal sufficient message representation for multi-agent communication. The regularizers aim at maximizing the mutual information (MI) between the message representation and action selection while minimizing the MI between the agent feature and message representation. Besides, we present a MARL framework that can integrate the proposed communication mechanism with existing value decomposition methods. Experimental results demonstrate that the proposed method is more robust and efficient than state-of-the-art GNN-based MARL methods.

------------------------------------------------------------------------

29\. · 100% match · 2021 · 1.0 cit/yr\
**Optimal communication and control strategies in a multi-agent MDP problem** ([link](https://www.semanticscholar.org/paper/27ee2d143f61cdde2be3622c7415b37e96f3643d))\
Sagar Sudhakara, Dhruva Kartik, Rahul Jain, and A. Nayyar\
*ArXiv* · Apr 22, 2021 · 5 citations

> The problem of controlling multi-agent systems under different models of information sharing among agents has received significant attention in the recent literature. In this paper, we consider a setup where rather than committing to a fixed information sharing protocol (e.g. periodic sharing or no sharing etc), agents can dynamically decide at each time step whether to share information with each other and incur the resulting communication cost. This setup requires a joint design of agents’ communication and control strategies in order to optimize the trade-off between communication costs and control objective. We first show that agents can ignore a big part of their private information without compromising the system performance. We then provide a common information approach based solution for the strategy optimization problem. This approach relies on constructing a fictitious POMDP whose solution (obtained via a dynamic program) characterizes the optimal strategies for the agents. We also show that our solution can be easily modified to incorporate constraints on when and how frequently agents can communicate.

------------------------------------------------------------------------

30\. · 100% match · 2015 · 1.1 cit/yr\
**LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis** ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*ArXiv* · Oct 14, 2015 · 12 citations

> In the interest of evaluating an information-theoretic requirement for feedback control, this paper proposes a framework to synthesize a control policy that minimizes Massey’s directed information from the state sequence to the control sequence while attaining required Linear-Quadratic-Gaussian (LQG) control performance. Interpretation and significance of this framework is discussed in the context of networked control theory. As the main result, we show that an optimal control policy can be realized by an attractively simple three-stage decision architecture comprising (1) a linear sensor with additive Gaussian noise, (2) a Kalman filter, and (3) a certainty equivalence controller. This result suggests an integration of two separation principles previously known in the literature: the filter-controller separation principle in the LQG control theory, and the sensorfilter separation principle in zero-delay rate-distortion theory for Gauss-Markov sources. It is also shown that an optimal policy can be synthesized by semidefinite programming (SDP). Both time-varying finite-horizon problems and time-invariant infinitehorizon problems are considered. Our results can be viewed as a generalization of the data-rate theorem for mean-square stability by Nair & Evans, extended for a control performance analysis.

------------------------------------------------------------------------

31\. · 100% match · 2001 · 1.1 cit/yr\
**Communication Complexity and Coordination by Authority** ([link](https://www.semanticscholar.org/paper/6058a6ecc7dcc59546cf1c0c8bc4d741b8cc7c2d))\
I. Segal\
27 citations

> We prove that the simplest communication allowing two players to coordinate on a course of action is authority (letting one player choose an action). We also consider the case where each player possesses valuable information about the benefits of a large number of actions. For this case, we identify conditions under which authority can only be asymptotically improved upon by protocols of exponential complexity in the number of actions (i.e. those describing an unbounded number of actions).

------------------------------------------------------------------------

32\. · 100% match · 2018 · 1.2 cit/yr\
**Systems of Bounded Rational Agents with Information-Theoretic Constraints** ([link](https://doi.org/10.1162/neco_a_01153))\
Sebastian Gottwald and Daniel A. Braun\
*Neural Computation* · Sep 16, 2018 · 9 citations

> Specialization and hierarchical organization are important features of efficient collaboration in economical, artificial, and biological systems. Here, we investigate the hypothesis that both features can be explained by the fact that each entity of such a system is limited in a certain way. We propose an information-theoretic approach based on a free energy principle in order to computationally analyze systems of bounded rational agents that deal with such limitations optimally. We find that specialization allows a focus on fewer tasks, thus leading to a more efficient execution, but in turn, it requires coordination in hierarchical structures of specialized experts and coordinating units. Our results suggest that hierarchical architectures of specialized units at lower levels that are coordinated by units at higher levels are optimal, given that each unit’s information-processing capability is limited and conforms to constraints on complexity costs.

------------------------------------------------------------------------

33\. · 100% match · 2015 · 35 cit/yr\
**Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach** ([link](https://www.semanticscholar.org/paper/f583f9e720c16f6bb50f9d624b61c3bc851be008))\
Yinlam Chow, Aviv Tamar, Shie Mannor, and M. Pavone\
*ArXiv* · Jun 6, 2015 · 383 citations

> In this paper we address the problem of decision making within a Markov decision process (MDP) framework where risk and modeling errors are taken into account. Our approach is to minimize a risk-sensitive conditional-value-at-risk (CVaR) objective, as opposed to a standard risk-neutral expectation. We refer to such problem as CVaR MDP. Our first contribution is to show that a CVaR objective, besides capturing risk sensitivity, has an alternative interpretation as expected cost under worst-case modeling errors, for a given error budget. This result, which is of independent interest, motivates CVaR MDPs as a unifying framework for risk-sensitive and robust decision making. Our second contribution is to present an approximate value-iteration algorithm for CVaR MDPs and analyze its convergence rate. To our knowledge, this is the first solution algorithm for CVaR MDPs that enjoys error guarantees. Finally, we present results from numerical experiments that corroborate our theoretical findings and show the practicality of our approach.

------------------------------------------------------------------------

34\. · 100% match · 2018 · 7.9 cit/yr\
**Learning to Share and Hide Intentions using Information Regularization** ([link](https://www.semanticscholar.org/paper/70f4a0478f2979005b3628491c8b95335834cb64))\
D. Strouse, Max Kleiman-Weiner, J. Tenenbaum, M. Botvinick, and D. Schwab\
*ArXiv* · Aug 1, 2018 · 62 citations

> Learning to cooperate with friends and compete with foes is a key component of multi-agent reinforcement learning. Typically to do so, one requires access to either a model of or interaction with the other agent(s). Here we show how to learn effective strategies for cooperation and competition in an asymmetric information game with no such model or interaction. Our approach is to encourage an agent to reveal or hide their intentions using an information-theoretic regularizer. We consider both the mutual information between goal and action given state, as well as the mutual information between goal and state. We show how to stochastically optimize these regularizers in a way that is easy to integrate with policy gradient reinforcement learning. Finally, we demonstrate that cooperative (competitive) policies learned with our approach lead to more (less) reward for a second agent in two simple asymmetric information games.

------------------------------------------------------------------------

35\. · 100% match · 2014 · 4.6 cit/yr\
**A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level** ([link](https://doi.org/10.1109/TAC.2015.2500658))\
Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina\
*IEEE Transactions on Automatic Control* · Jul 1, 2014 · 55 citations

> This paper studies networked control systems closed over noiseless digital channels. We focus on noisy linear time-invariant (LTI) plants with stationary Gaussian disturbances, Gaussian initial state, scalar-valued control inputs and sensor outputs. For this set-up, we show that the absolute minimal directed information rate that allows one to achieve a prescribed level of performance (not necessarily stationary), over all combinations of encoder-controller-decoder, is achieved when the decoder output is jointly Gaussian with the other signals in the system. This directed information rate lower bounds the achievable operational data rates. When restricting our attention to encoder-controller-decoders which make the random processes in the loop (strongly) asymptotically wide-sense stationary, this bound can be expressed in terms of their asymptotic power spectral densities. Then we show that the directed information rate and stationary performance of any such scheme can be achieved when the concatenated encoder, channel, controller and decoder behave as an AWGN channel with LTI filters. We also present a simple coding scheme that allows one to achieve (operational) average data rates that are at most (approximately) 1.254 bits away from the derived lower bound, while satisfying the performance constraint. A numerical example is presented to illustrate our findings.

------------------------------------------------------------------------

36\. · 100% match · 2017 · 1.7 cit/yr\
**Transfer-Entropy-Regularized Markov Decision Processes** ([link](https://doi.org/10.1109/TAC.2021.3069347))\
Takashi Tanaka, H. Sandberg, and M. Skoglund\
*IEEE Transactions on Automatic Control* · Aug 30, 2017 · 15 citations

> We consider the framework of transfer-entropy-regularized Markov decision process (TERMDP) in which the weighted sum of the classical state-dependent cost and the transfer entropy from the state random process to the control input process is minimized. Although TERMDPs are generally formulated as nonconvex optimization problems, an analytical necessary optimality condition can be expressed as a finite set of nonlinear equations, based on which an iterative forward–backward computational procedure similar to the Arimoto–Blahut algorithm is developed. It is shown that every limit point of the sequence generated by the proposed algorithm is a stationary point of the TERMDP. Applications of TERMDPs are discussed in the context of networked control systems theory and nonequilibrium thermodynamics. The proposed algorithm is applied to an information-constrained maze navigation problem, whereby we study how the price of information qualitatively alters the optimal decision polices.

------------------------------------------------------------------------

37\. · 100% match · 2007 · 14 cit/yr\
**Formal Trust Model for Multiagent Systems** ([link](https://www.semanticscholar.org/paper/f14430e29ad3ff0fe4fb5a1a9ab507d34986bfa8))\
Yonghong Wang and Munindar P. Singh\
*International Joint Conference on Artificial Intelligence* · Jan 6, 2007 · 279 citations

> Trust should be substantially based on evidence. Further, a key challenge for multiagent systems is how to determine trust based on reports from multiple sources, who might themselves be trusted to varying degrees. Hence an ability to combine evidence-based trust reports in a manner that discounts for imperfect trust in the reporting agents is crucial for multiagent systems.
>
> This paper understands trust in terms of belief and certainty: A’s trust in B is reflected in the strength of A’s belief that B is trustworthy. This paper formulates certainty in terms of evidence based on a statistical measure defined over a probability distribution of the probability of positive outcomes. This novel definition supports important mathematical properties, including (1) certainty increases as conflict increases provided the amount of evidence is unchanged, and (2) certainty increases as the amount of evidence increases provided conflict is unchanged. Moreover, despite a more subtle definition than previous approaches, this paper (3) establishes a bijection between evidence and trust spaces, enabling robust combination of trust reports and (4) provides an efficient algorithm for computing this bijection.

------------------------------------------------------------------------

38\. · 100% match · 2012 · 4.9 cit/yr\
**Nonanticipative Rate Distortion Function and Relations to Filtering Theory** ([link](https://doi.org/10.1109/TAC.2013.2293403))\
C. Charalambous, Photios A. Stavrou, and N. Ahmed\
*IEEE Transactions on Automatic Control* · Oct 3, 2012 · 67 citations

> The relation between nonanticipative rate distortion function (RDF) and filtering theory is discussed on abstract spaces. The relation is established by imposing a realizability constraint on the reconstruction conditional distribution of the classical RDF. Existence of the extremum solution of the nonanticipative RDF is shown using weak \*-convergence on appropriate topology. The extremum reconstruction conditional distribution is derived in closed form, for the case of stationary processes. The realization of the reconstruction conditional distribution which achieves the infimum of the nonanticipative RDF is described. Finally, an example is presented to illustrate the concepts.

------------------------------------------------------------------------

39\. · 100% match · 2022 · 6.5 cit/yr\
**Trading off Utility, Informativeness, and Complexity in Emergent Communication** ([link](https://doi.org/10.52202/068431-1614))\
Mycal Tucker, R. Levy, J. Shah, and Noga Zaslavsky\
*Advances in Neural Information Processing Systems 35* · 28 citations

> Emergent communication (EC) research often focuses on optimizing task-speciﬁc utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Information Bottleneck (IB) tradeoff between the informativeness and complexity of the lexicon. Here, we integrate these two approaches by trading off utility, informativeness, and complexity in EC. To this end, we propose Vector-Quantized Variational Information Bottleneck (VQ-VIB), a method for training neural agents to encode inputs into discrete signals embedded in a continuous space. We evaluate our approach in multi-agent reinforcement learning settings and in color reference games and show that: (1) VQ-VIB agents can continuously adapt to changing communicative needs and, in the color domain, align with human languages; (2) the emergent VQ-VIB embedding spaces are semantically meaningful and perceptually grounded; and (3) encouraging informativeness leads to faster convergence rates and improved utility, both in VQ-VIB and in prior neural architectures for symbolic EC, with VQ-VIB achieving higher utility for any given complexity. This work offers a new framework for EC that is grounded in information-theoretic principles that are believed to characterize human language evolution and that may facilitate human-agent interaction.

------------------------------------------------------------------------

40\. · 100% match · 2017 · 5.1 cit/yr\
**Fully Decentralized Policies for Multi-Agent Systems: An Information Theoretic Approach** ([link](https://www.semanticscholar.org/paper/e6be7302cc97fe951a24f0b3c3c54995a20c7b12))\
Roel Dobbe, David Fridovich-Keil, and C. Tomlin\
*ArXiv* · Jul 20, 2017 · 45 citations

> Learning cooperative policies for multi-agent systems is often challenged by partial observability and a lack of coordination. In some settings, the structure of a problem allows a distributed solution with limited communication. Here, we consider a scenario where no communication is available, and instead we learn local policies for all agents that collectively mimic the solution to a centralized multi-agent static optimization problem. Our main contribution is an information theoretic framework based on rate distortion theory which facilitates analysis of how well the resulting fully decentralized policies are able to reconstruct the optimal solution. Moreover, this framework provides a natural extension that addresses which nodes an agent should communicate with to improve the performance of its individual policy.

------------------------------------------------------------------------

41\. · 100% match · 2005 · 0.1 cit/yr\
**A Model for Competence and Integrity in Variable Payoff Games** ([link](https://www.semanticscholar.org/paper/66ef4e234cc16a56a33fa532330aadab9db77bea))\
Michael J. Smith and Marie desJardins\
2 citations

> Agents often have to trust one another when engaging in joint actions. In many cases, no single design team has the authority to assure that agents cooperate. Trust is required when agents hold potentially different values or conflicting goals. This paper presents a framework and some initial experiments for decomposing agent reputation within a multi-agent society into two characteristics: competence and integrity. The framework models competence as the probability of successfully carrying out an intended action. Integrity is modeled as a rational commitment to maintaining a reputation, based on the agent’s assessment of the game’s discount rate. We show that a simple, one-level-deep recursive model—given accurate knowledge of self and the other agent’s competence and integrity (commitment to reputation)—outperforms titfor-tat and other standard strategies in evolutionary round-robin iterated prisoner’s dilemma tournaments. This indicates that the approach taken here warrants further investigation using more realistic and com-

------------------------------------------------------------------------

42\. · 100% match · 2007 · 102 cit/yr\
**You have printed the following article : Formal and Real Authority in Organizations** ([link](https://dash.harvard.edu/bitstream/1/4554125/1/Aghion_FormalRealA.pdf))\
P. Aghion and Jean Tirole\
1970 citations

> This paper develops a theory of the allocation of formal authority (the right to decide) and real authority (the effective control over decisions) within organizations, and it illustrates how a formally integrated structure can accommodate various degrees of “real” integration. Real authority is determined by the structure of information, which in turn depends on the allocation of formal authority. An increase in an agent’s real authority promotes initiative but results in a loss of control for the principal. After spelling out (some of) the main determinants of the delegation of formal authority within organizations, the paper examines a number of factors that increase the subordinates’ real authority in a formally integrated structure: overload, lenient rules, urgency of decision, reputation, performance measurement, and multiplicity of superiors. Finally, the amount of communication in an organization is shown to depend on the allocation of formal authority.

------------------------------------------------------------------------

43\. · 100% match · 2019 · 2.3 cit/yr\
**Common Knowledge and Sequential Team Problems** ([link](https://doi.org/10.1109/TAC.2019.2912536))\
A. Nayyar and D. Teneketzis\
*IEEE Transactions on Automatic Control* · Apr 22, 2019 · 16 citations

> We consider a general sequential team problem based on Witsenhausen’s intrinsic model. Our formulation encompasses all teams in which the uncontrolled inputs can be viewed as random variables on a finite probability space, the number of control inputs/decisions is finite and the decisions take values in finite spaces. We define the concept of common knowledge in such teams and use it to construct a sequential decomposition of the problem of optimizing the team strategy profile. If the information structure is classical, our common knowledge based decomposition is identical to classical dynamic program. If the information structure is such that the common knowledge is trivial, our decomposition is similar in spirit to Witsenhausen’s standard form based decomposition \<xref ref-type=“bibr” rid=“ref17”\>\[17\]\</xref\>. In this case, the sequential decomposition is essentially a sequential reformulation of the strategy optimization problem and appears to have limited value. For information structures with nontrivial common knowledge, our sequential decomposition differs from Witsenhausen’s standard form based decomposition because of its dependence on common knowledge. Our common knowledge based approach generalizes the common information based methods of \<xref ref-type=“bibr” rid=“ref12”\>\[12\]\</xref\>–\<xref ref-type=“bibr” rid=“ref13”/\>\<xref ref-type=“bibr” rid=“ref14”\>\[14\]\</xref\>.

------------------------------------------------------------------------

44\. · 100% match · 2015 · 3.9 cit/yr\
**SDP-based joint sensor and controller design for information-regularized optimal LQG control** ([link](https://doi.org/10.1109/CDC.2015.7402920))\
Takashi Tanaka and H. Sandberg\
*2015 54th IEEE Conference on Decision and Control (CDC)* · Mar 6, 2015 · 44 citations

> We consider a joint sensor and controller design problem for linear Gaussian stochastic systems in which a weighted sum of quadratic control cost and the amount of information acquired by the sensor is minimized. This problem formulation is motivated by situations where a control law must be designed in the presence of sensing, communication, and privacy constraints. We show that an optimal linear joint sensor-controller policy is comprised of a linear sensor, Kalman filter, and a certainty equivalence controller, and can be synthesized by a numerically efficient algorithm based on semidefinite programming (SDP).

------------------------------------------------------------------------

45\. · 100% match · 2004 · 34 cit/yr\
**Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates** ([link](https://doi.org/10.1137/S0363012902402116))\
G. Nair and R. Evans\
*SIAM J. Control. Optim.* · Feb 1, 2004 · 753 citations

> Feedback control with limited data rates is an emerging area which incorporates ideas from both control and information theory. A fundamental question it poses is how low the closed-loop data rate can be made before a given dynamical system is impossible to stabilize by any coding and control law. Analogously to source coding, this defines the smallest error-free data rate sufficient to achieve “reliable” control, and explicit expressions for it have been derived for linear time-invariant systems without disturbances. In this paper, the more general case of finite-dimensional linear systems with process and observation noise is considered, the object being mean square state stability. By inductive arguments employing the entropy power inequality of information theory, and a new quantizer error bound, an explicit expression for the infimum stabilizing data rate is derived, under very mild conditions on the initial state and noise probability distributions.

------------------------------------------------------------------------

46\. · 100% match · 2006 · 21 cit/yr\
**The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link—Part I: Scalar Systems** ([link](https://doi.org/10.1109/TIT.2006.878169))\
Anant Sahai and S. Mitter\
*IEEE Transactions on Information Theory* · Jan 4, 2006 · 432 citations

> In this paper, we review how Shannon’s classical notion of capacity is not enough to characterize a noisy communication channel if the channel is intended to be used as part of a feedback loop to stabilize an unstable scalar linear system. While classical capacity is not enough, another sense of capacity (parametrized by reliability) called “anytime capacity” is necessary for the stabilization of an unstable process. The required rate is given by the log of the unstable system gain and the required reliability comes from the sense of stability desired. A consequence of this necessity result is a sequential generalization of the Schalkwijk-Kailath scheme for communication over the additive white Gaussian noise (AWGN) channel with feedback. In cases of sufficiently rich information patterns between the encoder and decoder, adequate anytime capacity is also shown to be sufficient for there to exist a stabilizing controller. These sufficiency results are then generalized to cases with noisy observations, delayed control actions, and without any explicit feedback between the observer and the controller. Both necessary and sufficient conditions are extended to continuous time systems as well. We close with comments discussing a hierarchy of difficulty for communication problems and how these results establish where stabilization problems sit in that hierarchy

------------------------------------------------------------------------

47\. · 100% match\
**Quantization and Coding for Decentralized LTI Systems 1** ([link](https://www.semanticscholar.org/paper/9318fb88b89140c16558b5457beed0e78fb8ee9f))\
S. Yüksel and T. Başar\
0 citations

> We study the communication rate requirements for centralized and decentralized control schemes when the plant and the controller are connected via a noiseless bandlimited channel. We introduce recursive quantizers that achieve monotonic boundedness and exponential stability of the worst-case state estimation error with minimum rate. Rate requirements for centralized schemes are shown to be lower than those for decentralized schemes. A quantification of the information sharing between the controllers, such as full, instant, and one-step delayed information sharing, is shown to crucial for communication requirements and complexity. Slepian-Wolf coding argument is used to show that information sharing by the controllers, and not by the plants, is sufficient to achieve the lower bound on the rate, and schemes confirming this efficiency are constructed. It is also shown that delay in communication between the controllers leads to higher rate requirements between the controllers and the plants.

------------------------------------------------------------------------

48\. · 100% match · 2024 · 1.6 cit/yr\
**Bayesian Persuasion: From Persuasion toward Counter-Suasion** ([link](https://doi.org/10.1109/ISIT57864.2024.10619410))\
Ananya Das, Aishwarya Soni, and Amitalok J. Budkuley\
*2024 IEEE International Symposium on Information Theory (ISIT)* · Jul 7, 2024 · 3 citations

> We study the problem of Bayesian persuasion under receiver distrust. In the classical Bayesian persuasion problem introduced by Kamenica and Gentzkow \[AER, 2011\], there are two parties, a sender Alice and a receiver Bob, who engage in a one-way interaction from sender to receiver. The sender employs a signalling strategy so as to persuade or steer the receiver toward taking a certain action(s) with respect to a random state known only to her. Both parties are rational and seek to optimize their expected utilities; however, their utilities are intimately coupled as they are functions of the random state and the receiver’s action. In this work, we initiate a systematic study of Bayesian persuasion when the receiver is distrustful of the sender. Extending the result of Kamenica and Gentzkow \[AER, 2011\], we present a necessary and sufficient criterion for the existence of a signalling scheme for persuasion under distrust. Interestingly, our results unveil the existence of a regime under a so-called ‘super-distrustful’ receiver when a rational sender should seek to ‘counter-persuade’ or employ ‘counter-suasion’ to derive maximal benefit.

------------------------------------------------------------------------

49\. · 100% match · 1995 · 0.9 cit/yr\
**Communication Requirements for Individual Agents in Networks and Hierarchies** ([link](https://doi.org/10.1007/978-1-4615-2261-4_12))\
T. Marschak and S. Reichelstein\
29 citations

------------------------------------------------------------------------

50\. · 100% match · 2008 · 2.6 cit/yr\
**Identifying tractable decentralized control problems on the basis of information structure** ([link](https://doi.org/10.1109/ALLERTON.2008.4797732))\
Aditya Mahajan, A. Nayyar, and D. Teneketzis\
*2008 46th Annual Allerton Conference on Communication, Control, and Computing* · Sep 1, 2008 · 46 citations

> Sequential decomposition of two general models of decentralized systems with non-classical information structures is presented. In model A, all agents have two observations at each step: a common observation that all agents observe and a private observation of their own. The control actions of each agent is based on all past common observations, the current private observation and the contents of its memory. At each step, each agent also updates the contents of its memory. A cost function, which depends on the state of the plant and the control actions of all agents, is given. The objective is to choose control and memory update functions for all agents to either minimize a total expected cost over a finite horizon or to minimize a discounted cost over an infinite horizon. In model B, the agents do not have any common observation, the rest is same as in model A. The key idea of our solution methodology is the following. From the point of view of a fictitious agent that observes all common observations, the system can be viewed as a centralized system with partial observations. This allows us to identify information states and obtain a sequential decomposition. When the system variables take values in finite sets, the optimality equations of the sequential decomposition are similar to those of partially observable Markov decision processes (POMDP) with finite state and action spaces. For such systems, we can use algorithms for POMDPs to compute optimal designs for models A and B.

*Showing top 50 of 90 papers. Full details available via CSV or BibTeX export.*
