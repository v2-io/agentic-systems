# Prior art for AAT failure diagnosis and persistence

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which agents diagnose failure by orthogonally separating a satisfaction gap from control regret: whether a goal is achievable at all versus whether the current strategy is suboptimal. The framework further claims that this separation forces a strict internal update order—update model, then check satisfaction, then check regret, then revise strategy, then revise goal. Search broadly but math-first, with conceptual or cognitive-architectural antecedents as secondary support, across both older and newer literature and across decision theory, non-stationary reinforcement learning, active inference, cognitive architectures, and adjacent formal lineages. The environment is non-stationary and goals may become physically unachievable. For the satisfaction side, cast a wide net around unattainability, infeasibility, dead ends, viability failure, misspecification, or related formal treatments, while prioritizing papers that distinguish these from policy regret or strategy error. Also find prior art for the claim that exploration in a drifting world can be driven by survival or persistence requirements rather than only epistemic uncertainty, including derivations where maintaining viability, bounded tracking, or persistence sector conditions requires refreshing observations. In addition, find prior art for the claim that tracking a non-stationary environment formally requires bounded memory or exponential forgetting, and that without forgetting confidence calcifies and tracking fails. Count exact matches and strong mathematical analogues, but prioritize the best antecedents for each pillar separately, with extra weight on papers that partially or fully unify multiple pillars. Exclude standard stationary UCB or epsilon-greedy exploration motivated only by regret minimization, regret bounds that assume the goal is always achievable, and general OODA-loop papers that do not mathematically force the cascade order. Restrict the search to academic literature only.

*Found 88 papers · May 21, 2026 · Estimated coverage of relevant papers: 65%*

## Summary of Results

Failure diagnosis is most strongly anticipated in three separate mathematical lineages: viability/reachability theory treats goal unattainability as a state-space property \[1\], \[2\], dead-end and infeasible-goal MDPs separate success probability from conditional execution cost \[3\], \[4\], \[5\], \[6\], \[7\], \[8\], and non-stationary estimation/control shows that model update must precede any performance judgment because tracking itself requires forgetting or bounded memory \[9\], \[10\], \[11\], \[12\], \[13\].

#### Best antecedents for the AAT split

- **Satisfaction gap as unachievability/viability failure:** viability kernels formalize whether any control can keep the system inside constraints or reach acceptable sets \[1\], \[2\], \[14\], \[15\].
- **Control regret as strategy suboptimality conditional on achievability:** dead-end SSP extensions explicitly optimize in lexicographic order—first maximize reachability/survival probability, then minimize expected cost among successful policies \[4\], \[5\], \[6\], \[8\]. This is the closest mathematical analogue to separating satisfaction from regret.

#### Update-order antecedents

- A near-cascade is implicit across formalisms: **update model** with recency weighting \[10\], \[11\], \[13\], \[16\]; **check viability/reachability** \[1\], \[3\]; **optimize policy within the viable set** \[4\], \[5\]. No single paper in the set proves the full AAT order including an explicit final “revise goal” step.

#### Persistence-driven exploration and forgetting

- Exploration need not be purely epistemic: adaptive/dual control uses probing to maintain regulation or stabilizability \[17\], \[18\], \[19\], \[20\]; homeostatic RL and active inference tie sampling to survival or preferred-state maintenance \[21\], \[22\], \[23\].
- Tracking in drifting worlds repeatedly reduces to finite memory or exponential forgetting; without it, estimators become non-adaptive or depend on the entire past \[9\], \[11\], \[12\], \[13\].

## Paper Catalog (88 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 1991 | 46 | Viability theory ([link](https://doi.org/10.1007/978-0-8176-4910-4)) | J. Aubin |  |
| 2 | 2012 | 6.9 | A Theory of Goal-Oriented MDPs with Dead Ends ([link](https://www.semanticscholar.org/paper/7b879ee4a07228cdbbaa1c6e31ffa3693c857892)) | A. Kolobov, Mausam, and Daniel S. Weld | ArXiv |
| 3 | 2008 | 18 | On Upper-Confidence Bound Policies for Non-Stationary Bandit Problems ([link](https://www.semanticscholar.org/paper/6eb7f22b9329ff77d0bdb6d86f35a7b6e62be1e3)) | Aurélien Garivier and É. Moulines | arXiv: Statistics Theory |
| 4 | 2014 | 15 | Homeostatic reinforcement learning for integrating reward collection and physiological stability ([link](https://doi.org/10.7554/eLife.04811)) | Mehdi Keramati and B. Gutkin | eLife |
| 5 | 1993 | 2.9 | Performance analysis of the forgetting factor RLS algorithm ([link](https://doi.org/10.1002/ACS.4480070604)) | Lei Guo, L. Ljung, and P. Priouret | International Journal of Adaptive Control and Signal Processing |
| 6 | 2019 | 3.9 | Trading-Off Static and Dynamic Regret in Online Least-Squares and Beyond ([link](https://doi.org/10.1609/AAAI.V34I04.6149)) | Jianjun Yuan and Andrew G. Lamperski | ArXiv |
| 7 | 2019 | 18 | Weighted Linear Bandits for Non-Stationary Environments ([link](https://www.semanticscholar.org/paper/821cb38c5f408e681840b3237093ad0cd33b6aa7)) | Yoan Russac, Claire Vernade, and O. Cappé | Neural Information Processing Systems |
| 8 | 2010 | 4.2 | Stochastic viability and dynamic programming ([link](https://doi.org/10.1016/j.sysconle.2010.07.008)) | L. Doyen and M. Lara | Syst. Control. Lett. |
| 9 | 2012 | 4.4 | Stochastic Safest and Shortest Path Problems ([link](https://doi.org/10.1609/aaai.v26i1.8367)) | F. Teichteil-Königsbuch | Proceedings of the AAAI Conference on Artificial Intelligence |
| 10 | 1987 | 3.0 | Design of adaptive algorithms for the tracking of time‐varying systems ([link](https://doi.org/10.1002/ACS.4480010103)) | A. Benveniste | International Journal of Adaptive Control and Signal Processing |
| 11 | 1987 | 1.4 | Asymptotically efficient self-tuning regulators ([link](https://doi.org/10.1137/0325026)) | T. Lai and C. Z. Wei | Siam Journal on Control and Optimization |
| 12 | 2017 | 3.5 | Efficient solutions for Stochastic Shortest Path Problems with Dead Ends ([link](https://www.semanticscholar.org/paper/9d217059284f4efda99fdff13f5e405364242b9a)) | Felipe W. Trevizan, F. Teichteil-Königsbuch, and S. Thiébaux | Conference on Uncertainty in Artificial Intelligence |
| 13 | 2021 | 4.0 | Safe Value Functions ([link](https://doi.org/10.1109/TAC.2022.3200948)) | P. Massiani, Steve Heim, Friedrich Solowjow, and Sebastian Trimpe | IEEE Transactions on Automatic Control |
| 14 | 2024 | 7.6 | Online Linear Regression in Dynamic Environments via Discounting ([link](https://doi.org/10.48550/arXiv.2405.19175)) | A. Jacobsen and Ashok Cutkosky | International Conference on Machine Learning |
| 15 | 2020 | 0.5 | A randomized relaxation method to ensure feasibility in stochastic control of linear systems subject to state and input constraints ([link](https://doi.org/10.1016/j.automatica.2020.108854)) | Luca Deori, S. Garatti, and M. Prandini | Autom. |
| 16 | 2018 | 4.6 | On-Line Learning of Linear Dynamical Systems: Exponential Forgetting in Kalman Filters ([link](https://doi.org/10.1609/aaai.v33i01.33014098)) | Mark Kozdoba, Jakub Marecek, T. Tchrakian, and Shie Mannor | AAAI Conference on Artificial Intelligence |
| 17 | 1984 | 4.5 | Tracking of Slowly Varying Parameters by Directional Forgetting ([link](https://doi.org/10.1016/S1474-6670(17%2961051-6)) | R. Kulhavý and M. Kárný | IFAC Proceedings Volumes |
| 18 | 2019 | 7.6 | Probabilistic planning with formal performance guarantees for mobile service robots ([link](https://doi.org/10.1177/0278364919856695)) | Bruno Lacerda, Fatma Faruq, David Parker, and Nick Hawes | The International Journal of Robotics Research |
| 19 | 1987 | 9.1 | Persistent excitation in adaptive systems ([link](https://doi.org/10.1080/00207178708933715)) | K. Narendra and A. Annaswamy | International Journal of Control |
| 20 | 1993 | 5.2 | On a general concept of forgetting ([link](https://doi.org/10.1080/00207179308923034)) | R. Kulhavý and M. Zarrop | International Journal of Control |
| 21 | 2017 | 26 | Stochastic model predictive control with active uncertainty learning: A Survey on dual control ([link](https://doi.org/10.1016/j.arcontrol.2017.11.001)) | A. Mesbah | Annu. Rev. Control. |
| 22 | 2016 | 0.1 | Risk-Averse ω-regular Markov Decision Process Control ([link](https://www.semanticscholar.org/paper/83f40dc9d6c3196e5ff4f156820d4274d92ef815)) | Rüdiger Ehlers, Salar Moarref, and U. Topcu | ArXiv |
| 23 | 2020 | 8.8 | Optimal Probabilistic Motion Planning With Potential Infeasible LTL Constraints ([link](https://doi.org/10.1109/TAC.2021.3138704)) | Mingyu Cai, Shaoping Xiao, Zhijun Li, and Z. Kan | IEEE Transactions on Automatic Control |
| 24 | 1976 | 1.3 | Caution, Probing, and the Value of Information in the Control of Uncertain Systems ([link](https://www.semanticscholar.org/paper/239c259f0ffcc625c38c26daf37bd7f027c0998d)) | Y. Bar-Shalom and E. Tse |  |
| 25 | 1990 | 4.2 | Estimating time-varying parameters by the Kalman filter based algorithm: stability and convergence ([link](https://doi.org/10.1109/9.45169)) | Lei Guo | IEEE Transactions on Automatic Control |
| 26 | 2020 | 19 | Reinforcement Learning for Non-Stationary Markov Decision Processes: The Blessing of (More) Optimism ([link](https://www.semanticscholar.org/paper/5b3e68658c99ed9c461a909b16b862221946d6ad)) | Wang Chi Cheung, D. Simchi-Levi, and Ruihao Zhu | ArXiv |
| 27 | 2011 | 3.6 | A Reinforcement Learning Theory for Homeostatic Regulation ([link](https://www.semanticscholar.org/paper/ea210f761a19395d4b70f53dec2b6f446db22ebe)) | Mehdi Keramati and B. Gutkin | Neural Information Processing Systems |
| 28 | 2015 | 6.4 | This Time the Robot Settles for a Cost: A Quantitative Approach to Temporal Logic Planning with Partial Satisfaction ([link](https://doi.org/10.1609/aaai.v29i1.9670)) | Morteza Lahijanian, Shaull Almagor, Dror Fried, L. Kavraki, and Moshe Y. Vardi | AAAI Conference on Artificial Intelligence |
| 29 | 1991 | 1.1 | A result on the mean square error obtained using general tracking algorithms ([link](https://doi.org/10.1002/ACS.4480050402)) | L. Ljung and P. Priouret | International Journal of Adaptive Control and Signal Processing |
| 30 | 1985 | 7.5 | Restricted exponential forgetting in real-time identification ([link](https://doi.org/10.1016/0005-1098(87%2990054-9)) | R. Kulhavý | Autom. |
| 31 | 2000 | 6.0 | Survey of adaptive dual control methods ([link](https://doi.org/10.1049/IP-CTA:20000107)) | N. Filatov and H. Unbehauen |  |
| 32 | 2014 | 2.4 | On the minimal revision problem of specification automata ([link](https://doi.org/10.1177/0278364915587034)) | Kangjin Kim, Georgios Fainekos, and S. Sankaranarayanan | The International Journal of Robotics Research |
| 33 | 2015 | 53 | Active Inference, homeostatic regulation and adaptive behavioural control ([link](https://doi.org/10.1016/j.pneurobio.2015.09.001)) | G. Pezzulo, Francesco Rigoli, and Karl J. Friston | Progress in Neurobiology |
| 34 | 1972 | 2.3 | An actively adaptive control for linear systems with random parameters via the dual control approach ([link](https://doi.org/10.1109/CDC.1972.269088)) | E. Tse and Y. Bar-Shalom | IEEE Conference on Decision and Control |
| 35 | 1988 | 5.9 | Modified least squares algorithm incorporating exponential resetting and forgetting ([link](https://doi.org/10.1080/00207178808906026)) | M. Salgado, G. Goodwin, and R. Middleton | International Journal of Control |
| 36 | 2023 | 1.3 | Bi-Objective Lexicographic Optimization in Markov Decision Processes with Related Objectives ([link](https://doi.org/10.48550/arXiv.2305.09634)) | Damien Busatto-Gaston et al. | ArXiv |
| 37 | 2015 | 61 | Active inference and epistemic value ([link](https://doi.org/10.1080/17588928.2015.1020053)) | Karl J. Friston et al. | Cognitive Neuroscience |
| 38 | 2008 |  | Robust and stochastic viability ([link](https://doi.org/10.1007/978-3-540-79074-7_7)) | M. Lara and L. Doyen |  |
| 39 | 2013 | 1.2 | An MPC Approach to Dual Control ([link](https://doi.org/10.3182/20131218-3-IN-2045.00151)) | Tor Aksel N. Heirung, B. Ydstie, and B. Foss | IFAC Proceedings Volumes |
| 40 | 2016 | 0.8 | On Reward Function for Survival ([link](https://www.semanticscholar.org/paper/0466f1aaa36e2f174c0153475099a4f47ffa35cc)) | N. Yoshida | ArXiv |
| 41 | 2011 | 25 | Viability Theory: New Directions ([link](https://doi.org/10.1007/978-3-642-16684-6)) | J. Aubin, A. Bayen, and P. Saint-Pierre |  |
| 42 | 2012 | 16 | Active inference and agency: optimal control without cost functions ([link](https://doi.org/10.1007/s00422-012-0512-8)) | Karl J. Friston, Spyridon Samothrakis, and P. Montague | Biological Cybernetics |
| 43 | 2021 | 1.4 | Efficient Strategy Synthesis for MDPs With Resource Constraints ([link](https://doi.org/10.1109/TAC.2022.3209612)) | František Blahoudek, Petr Novotn’y, M. Ornik, Pranay Thangeda, and U. Topcu | IEEE Transactions on Automatic Control |
| 44 | 2019 | 0.6 | Viability of an open set for stochastic control systems ([link](https://doi.org/10.1016/J.SPA.2018.11.012)) | R. Buckdahn, Hélène Frankowska, and M. Quincampoix | Stochastic Processes and their Applications |
| 45 | 2013 | 38 | Non-Stationary Stochastic Optimization ([link](https://doi.org/10.1287/opre.2015.1408)) | Omar Besbes, Y. Gur, and A. Zeevi | Oper. Res. |
| 46 | 2018 | 21 | Learning to Optimize under Non-Stationarity ([link](https://doi.org/10.2139/SSRN.3261050)) | Wang Chi Cheung, D. Simchi-Levi, and Ruihao Zhu | ArXiv |
| 47 | 1981 | 1.7 | Deterministic convergence of a self-tuning regulator with variable forgetting factor ([link](https://doi.org/10.1049/IP-D:19810004)) | A. O. Cordero and D. Mayne |  |
| 48 | 1995 | 0.6 | A parallel adaptation algorithm for recursive-least-squares adaptive filters in nonstationary environments ([link](https://doi.org/10.1109/78.482100)) | S. D. Peters and A. Antoniou | IEEE Trans. Signal Process. |
| 49 | 1981 | 18 | Implementation of self-tuning regulators with variable forgetting factors ([link](https://doi.org/10.1016/0005-1098(81%2990070-4)) | T. Fortescue, L. Kershenbaum, and B. Ydstie | Autom. |
| 50 | 2019 | 0.6 | Active Roll-outs in MDP with Irreversible Dynamics ([link](https://www.semanticscholar.org/paper/89c3d2fdf5e3885f7d3bf1fbfb939dd4dffa45df)) | Odalric-Ambrym Maillard, Timothy A. Mann, R. Ortner, and Shie Mannor |  |
| 51 | 1992 | 3.6 | Recursive forgetting algorithms ([link](https://doi.org/10.1080/00207179208934228)) | J. Parkum, N. K. Poulsen, and J. Holst | International Journal of Control |
| 52 | 1984 | 4.2 | On the statistical efficiency of the LMS algorithm with nonstationary inputs ([link](https://doi.org/10.1109/TIT.1984.1056892)) | B. Widrow and E. Walach | IEEE Trans. Inf. Theory |
| 53 | 1994 | 1.0 | Exponentially weighted least squares identification of time-varying systems with white disturbances ([link](https://doi.org/10.1109/78.330351)) | M. Campi | IEEE Trans. Signal Process. |
| 54 | 2021 | 0.9 | Reinforcement learning with soft temporal logic constraints using limit-deterministic generalized Büchi automaton ([link](https://doi.org/10.1016/j.jai.2024.12.005)) | Mingyu Cai, Zhangli Zhou, Lin Li, Shaoping Xiao, and Z. Kan | Journal of Automation and Intelligence |
| 55 | 2021 | 1.9 | Continuous Homeostatic Reinforcement Learning for Self-Regulated Autonomous Agents ([link](https://www.semanticscholar.org/paper/9201986fdabbffa88f397c43134da8d707fb7c83)) | Hugo Laurençon, Charbel-Raphaël Ségerie, J. Lussange, and B. Gutkin | ArXiv |
| 56 | 2020 | 8.1 | Recursive Least Squares With Variable-Direction Forgetting: Compensating for the Loss of Persistency \[Lecture Notes\] ([link](https://doi.org/10.1109/MCS.2020.2990516)) | A. Goel, Adam L. Bruce, and D. Bernstein | IEEE Control Systems |
| 57 | 2001 | 4.0 | Viability kernels and capture basins of sets under differential inclusions ([link](https://doi.org/10.1109/CDC.2002.1185102)) | J. Aubin | Proceedings of the 41st IEEE Conference on Decision and Control, 2002. |
| 58 | 2019 | 3.2 | Randomized Exploration for Non-Stationary Stochastic Linear Bandits ([link](https://www.semanticscholar.org/paper/3f3cb7f9fb9fdda257b258564ece4e62e01b6f9e)) | Baekjin Kim and Ambuj Tewari | Conference on Uncertainty in Artificial Intelligence |
| 59 | 1989 | 0.8 | Nonasymptotic results for finite-memory WLS filters ([link](https://doi.org/10.1109/CDC.1989.70461)) | M. Niedźwiecki and L. Guo | Proceedings of the 28th IEEE Conference on Decision and Control, |
| 60 | 1995 | 2.5 | Exponential stability of general tracking algorithms ([link](https://doi.org/10.1109/9.402229)) | Lei Guo and L. Ljung | IEEE Trans. Autom. Control. |
| 61 | 2007 | 1.4 | A Dynamic Programming Approach to Viability Problems ([link](https://doi.org/10.1109/ADPRL.2007.368186)) | Pierre-Arnaud Coquelin, Sophie Martin, and R. Munos | 2007 IEEE International Symposium on Approximate Dynamic Programming and Reinforcement Learning |
| 62 | 2022 |  | Dynamic Regret Minimization for Control of Non-stationary Linear Dynamical Systems ([link](https://doi.org/10.1145/3489048.3522649)) | Yuwei Luo, Varun Gupta, and M. Kolar | Abstract Proceedings of the 2022 ACM SIGMETRICS/IFIP PERFORMANCE Joint International Conference on Measurement and Modeling of Computer Systems |
| 63 | 2018 |  | Occupation Measure Heuristics to Solve Stochastic Shortest Path with Dead Ends ([link](https://doi.org/10.1109/bracis.2018.00096)) | Milton Condori Fernández, Leliane Nunes de Barros, and Karina Valdivia Delgado | 2018 7th Brazilian Conference on Intelligent Systems (BRACIS) |
| 64 | 2019 | 1.0 | Model-invariant viability kernel approximation ([link](https://doi.org/10.1016/J.SYSCONLE.2019.03.010)) | Mahdi Yousefi, K. Heusden, Ian M. Mitchell, and G. Dumont | Syst. Control. Lett. |
| 65 | 1999 | 34 | Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback ([link](https://doi.org/10.1109/9.763226)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 66 | 2006 | 21 | The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link—Part I: Scalar Systems ([link](https://doi.org/10.1109/TIT.2006.878169)) | Anant Sahai and S. Mitter | IEEE Transactions on Information Theory |
| 67 | 2020 | 13 | Convergence and Consistency of Recursive Least Squares with Variable-Rate Forgetting ([link](https://doi.org/10.1016/j.automatica.2020.109052)) | Adam L. Bruce, A. Goel, and D. Bernstein | Autom. |
| 68 | 2023 | 9.3 | Generalized Forgetting Recursive Least Squares: Stability and Robustness Guarantees ([link](https://doi.org/10.1109/TAC.2024.3394351)) | Brian Lai and D. Bernstein | IEEE Transactions on Automatic Control |
| 69 | 2018 | 29 | Generalised free energy and active inference ([link](https://doi.org/10.1007/s00422-019-00805-w)) | Thomas Parr and Karl J. Friston | Biological Cybernetics |
| 70 | 2004 |  | Robust LRTDP: Reachability Analysis ([link](https://www.semanticscholar.org/paper/71acee4a9a0b891b8db2d52ff4f821bbf8fa2abe)) | O. Buffet |  |
| 71 | 2018 |  | Human-help in automated planning under uncertainty ([link](https://doi.org/10.11606/T.45.2019.TDE-19122018-211701)) | I. Franch |  |
| 72 | 2004 | 34 | Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates ([link](https://doi.org/10.1137/S0363012902402116)) | G. Nair and R. Evans | SIAM J. Control. Optim. |
| 73 | 2002 | 2.2 | Adaptive dual control ([link](https://www.semanticscholar.org/paper/9c1fe4c9791bab12e3a494664a71acd442c496af)) | B. Wittenmark |  |
| 74 | 2017 |  | Algorithms for persistent autonomy and surveillance ([link](https://www.semanticscholar.org/paper/5de00a96eef1b31cc2a0ee5e4cf4f2435a66f189)) | Cenk Baykal |  |
| 75 | 1991 | 18 | An Analysis of Stochastic Shortest Path Problems ([link](https://doi.org/10.1287/moor.16.3.580)) | D. Bertsekas and J. Tsitsiklis | Math. Oper. Res. |
| 76 | 2021 | 1.0 | On exploration requirements for learning safety constraints ([link](https://www.semanticscholar.org/paper/b4d39f7805fe30e03a35f7a77be8e762daa52723)) | P. Massiani, Steve Heim, and Sebastian Trimpe | ArXiv |
| 77 | 2020 | 3.9 | Recursive Least Squares with Variable-Direction Forgetting – Compensating for the loss of persistency ([link](https://www.semanticscholar.org/paper/772d524bc1403853a5bcbed1182e5327de80f555)) | A. Goel, Adam L. Bruce, and D. Bernstein | arXiv: Optimization and Control |
| 78 | 2018 | 1.8 | Interrupting behaviour: Minimizing decision costs via temporal commitment and low-level interrupts ([link](https://doi.org/10.1371/journal.pcbi.1005916)) | K. Lloyd and P. Dayan | PLoS Computational Biology |
| 79 | 2019 | 7.4 | No-Regret Exploration in Goal-Oriented Reinforcement Learning ([link](https://www.semanticscholar.org/paper/384ce8a6d36ef3102a71b8d32ebabafad26b7da7)) | Jean Tarbouriech, Evrard Garcelon, Michal Valko, Matteo Pirotta, and A. Lazaric | International Conference on Machine Learning |
| 80 | 2017 | 13 | Deep active inference ([link](https://doi.org/10.1007/s00422-018-0785-7)) | K. Ueltzhöffer | Biological Cybernetics |
| 81 | 2018 | 8.2 | Value of Information in Feedback Control: Quantification ([link](https://doi.org/10.1109/TAC.2021.3113472)) | T. Soleymani, J. Baras, and S. Hirche | IEEE Transactions on Automatic Control |
| 82 | 2022 | 1.4 | Opportunistic Qualitative Planning in Stochastic Systems with Preferences over Temporal Logic Objectives ([link](https://doi.org/10.48550/arXiv.2203.13803)) | A. Kulkarni and Jie Fu | ArXiv |
| 83 | 2021 | 0.6 | On Minimizing Total Discounted Cost in MDPs Subject to Reachability Constraints ([link](https://doi.org/10.1109/TAC.2024.3384834)) | Y. Savas, Christos K. Verginis, M. Hibbard, and U. Topcu | IEEE Transactions on Automatic Control |
| 84 | 2025 | 1.1 | Viability of Future Actions: Robust Safety in Reinforcement Learning via Entropy Regularization ([link](https://doi.org/10.1007/978-3-032-06106-5_8)) | P. Massiani, Alexander von Rohr, Lukas Haverbeck, and Sebastian Trimpe | ECML/PKDD |
| 85 | 1983 | 0.9 | The problem of forgetting old data in recursive estimation ([link](https://doi.org/10.1016/S1474-6670(17%2962386-3)) | T. Hägglund | IFAC Proceedings Volumes |
| 86 | 1989 |  | Non-Asymptotic Results for Finite-Memory WLS Filters TP11 - 3:45 ([link](https://www.semanticscholar.org/paper/f10e01e3934485686c33fd0c981dff81bde04b92)) | M. Niediwiecki and Lei Guo |  |
| 87 | 2013 | 0.1 | Performance of water extraction in an endangered aquifer when management is not all-powerful: a theoretical framework based on a viability theory ([link](https://doi.org/10.1061/9780784412947.051)) | C. Rougé and G. Deffuant |  |
| 88 | 2020 |  | Parameter-Free Learning for Evolving Markov Decision Processes: The Blessing of (More) Optimism. ([link](https://www.semanticscholar.org/paper/d6ec97dcb292ac86d13a136c57afa9b3121ba604)) | Wang Chi Cheung, D. Simchi-Levi, and Ruihao Zhu | arXiv: Learning |

### Paper Details

1\. · 100% match · 1991 · 46 cit/yr\
**Viability theory** ([link](https://doi.org/10.1007/978-0-8176-4910-4))\
J. Aubin\
1632 citations

------------------------------------------------------------------------

2\. · 100% match · 2012 · 6.9 cit/yr\
**A Theory of Goal-Oriented MDPs with Dead Ends** ([link](https://www.semanticscholar.org/paper/7b879ee4a07228cdbbaa1c6e31ffa3693c857892))\
A. Kolobov, Mausam, and Daniel S. Weld\
*ArXiv* · Aug 14, 2012 · 95 citations

> Stochastic Shortest Path (SSP) MDPs is a problem class widely studied in AI, especially in probabilistic planning. They describe a wide range of scenarios but make the restrictive assumption that the goal is reachable from any state, i.e., that dead-end states do not exist. Because of this, SSPs are unable to model various scenarios that may have catastrophic events (e.g., an airplane possibly crashing if it flies into a storm). Even though MDP algorithms have been used for solving problems with dead ends, a principled theory of SSP extensions that would allow dead ends, including theoretically sound algorithms for solving such MDPs, has been lacking. In this paper, we propose three new MDP classes that admit dead ends under increasingly weaker assumptions. We present Value Iteration-based as well as the more efficient heuristic search algorithms for optimally solving each class, and explore theoretical relationships between these classes. We also conduct a preliminary empirical study comparing the performance of our algorithms on different MDP classes, especially on scenarios with unavoidable dead ends.

------------------------------------------------------------------------

3\. · 100% match · 2008 · 18 cit/yr\
**On Upper-Confidence Bound Policies for Non-Stationary Bandit Problems** ([link](https://www.semanticscholar.org/paper/6eb7f22b9329ff77d0bdb6d86f35a7b6e62be1e3))\
Aurélien Garivier and É. Moulines\
*arXiv: Statistics Theory* · May 22, 2008 · 329 citations

> Multi-armed bandit problems are considered as a paradigm of the trade-off between exploring the environment to find profitable actions and exploiting what is already known. In the stationary case, the distributions of the rewards do not change in time, Upper-Confidence Bound (UCB) policies have been shown to be rate optimal. A challenging variant of the MABP is the non-stationary bandit problem where the gambler must decide which arm to play while facing the possibility of a changing environment. In this paper, we consider the situation where the distributions of rewards remain constant over epochs and change at unknown time instants. We analyze two algorithms: the discounted UCB and the sliding-window UCB. We establish for these two algorithms an upper-bound for the expected regret by upper-bounding the expectation of the number of times a suboptimal arm is played. For that purpose, we derive a Hoeffding type inequality for self normalized deviations with a random number of summands. We establish a lower-bound for the regret in presence of abrupt changes in the arms reward distributions. We show that the discounted UCB and the sliding-window UCB both match the lower-bound up to a logarithmic factor.

------------------------------------------------------------------------

4\. · 100% match · 2014 · 15 cit/yr\
**Homeostatic reinforcement learning for integrating reward collection and physiological stability** ([link](https://doi.org/10.7554/eLife.04811))\
Mehdi Keramati and B. Gutkin\
*eLife* · Dec 2, 2014 · 175 citations

> Efficient regulation of internal homeostasis and defending it against perturbations requires adaptive behavioral strategies. However, the computational principles mediating the interaction between homeostatic and associative learning processes remain undefined. Here we use a definition of primary rewards, as outcomes fulfilling physiological needs, to build a normative theory showing how learning motivated behaviors may be modulated by internal states. Within this framework, we mathematically prove that seeking rewards is equivalent to the fundamental objective of physiological stability, defining the notion of physiological rationality of behavior. We further suggest a formal basis for temporal discounting of rewards by showing that discounting motivates animals to follow the shortest path in the space of physiological variables toward the desired setpoint. We also explain how animals learn to act predictively to preclude prospective homeostatic challenges, and several other behavioral patterns. Finally, we suggest a computational role for interaction between hypothalamus and the brain reward system. DOI: http://dx.doi.org/10.7554/eLife.04811.001

------------------------------------------------------------------------

5\. · 100% match · 1993 · 2.9 cit/yr\
**Performance analysis of the forgetting factor RLS algorithm** ([link](https://doi.org/10.1002/ACS.4480070604))\
Lei Guo, L. Ljung, and P. Priouret\
*International Journal of Adaptive Control and Signal Processing* · Nov 1, 1993 · 93 citations

> An analysis is given of the performance of the standard forgetting factor recursive least squares (RLS) algorithm when used for tracking time-varying linear regression models. Three basic results are obtained: (1) the ‘P-matrix’ in the algorithm remains bounded if and only if the (time-varying) covariance matrix of the regressors is uniformly non-singular; (2) if so, the parameter tracking error covariance matrix is of the order O(μ + γ2/μ), where μ = 1 - λ, λ is the forgetting factor and γ is a quantity reflecting the speed of the parameter variations; (3) this covariance matrix can be arbitrarily well approximated (for small enough μ) by an expression that is easy to compute.

------------------------------------------------------------------------

6\. · 100% match · 2019 · 3.9 cit/yr\
**Trading-Off Static and Dynamic Regret in Online Least-Squares and Beyond** ([link](https://doi.org/10.1609/AAAI.V34I04.6149))\
Jianjun Yuan and Andrew G. Lamperski\
*ArXiv* · Sep 6, 2019 · 26 citations

> Recursive least-squares algorithms often use forgetting factors as a heuristic to adapt to non-stationary data streams. The first contribution of this paper rigorously characterizes the effect of forgetting factors for a class of online Newton algorithms. For exp-concave and strongly convex objectives, the algorithms achieve the dynamic regret of $`\max\{O(\log T),O(\sqrt{TV})\}`$, where $`V`$ is a bound on the path length of the comparison sequence. In particular, we show how classic recursive least-squares with a forgetting factor achieves this dynamic regret bound. By varying $`V`$, we obtain a trade-off between static and dynamic regret. In order to obtain more computationally efficient algorithms, our second contribution is a novel gradient descent step size rule for strongly convex functions. Our gradient descent rule recovers the order optimal dynamic regret bounds described above. For smooth problems, we can also obtain static regret of $`O(T^{1-\beta})`$ and dynamic regret of $`O(T^\beta V^*)`$, where $`\beta \in (0,1)`$ and $`V^*`$ is the path length of the sequence of minimizers. By varying $`\beta`$, we obtain a trade-off between static and dynamic regret.

------------------------------------------------------------------------

7\. · 100% match · 2019 · 18 cit/yr\
**Weighted Linear Bandits for Non-Stationary Environments** ([link](https://www.semanticscholar.org/paper/821cb38c5f408e681840b3237093ad0cd33b6aa7))\
Yoan Russac, Claire Vernade, and O. Cappé\
*Neural Information Processing Systems* · Sep 19, 2019 · 119 citations

> We consider a stochastic linear bandit model in which the available actions correspond to arbitrary context vectors whose associated rewards follow a non-stationary linear regression model. In this setting, the unknown regression parameter is allowed to vary in time. To address this problem, we propose D-LinUCB, a novel optimistic algorithm based on discounted linear regression, where exponential weights are used to smoothly forget the past. This involves studying the deviations of the sequential weighted least-squares estimator under generic assumptions. As a by-product, we obtain novel deviation results that can be used beyond non-stationary environments. We provide theoretical guarantees on the behavior of D-LinUCB in both slowly-varying and abruptly-changing environments. We obtain an upper bound on the dynamic regret that is of order d B_T<sup>{1/3}T</sup>{2/3}, where B_T is a measure of non-stationarity (d and T being, respectively, dimension and horizon). This rate is known to be optimal. We also illustrate the empirical performance of D-LinUCB and compare it with recently proposed alternatives in simulated environments.

------------------------------------------------------------------------

8\. · 100% match · 2010 · 4.2 cit/yr\
**Stochastic viability and dynamic programming** ([link](https://doi.org/10.1016/j.sysconle.2010.07.008))\
L. Doyen and M. Lara\
*Syst. Control. Lett.* · Feb 5, 2010 · 69 citations

> This paper deals with the stochastic control of nonlinear systems in the presence of state and control constraints, for uncertain discrete-time dynamics in finite dimensional spaces. In the deterministic case, the viability kernel is known to play a basic role for the analysis of such problems and the design of viable control feedbacks. In the present paper, we show how a stochastic viability kernel and viable feedbacks relying on probability (or chance) constraints can be defined and computed by a dynamic programming equation. An example illustrates most of the assertions.

------------------------------------------------------------------------

9\. · 100% match · 2012 · 4.4 cit/yr\
**Stochastic Safest and Shortest Path Problems** ([link](https://doi.org/10.1609/aaai.v26i1.8367))\
F. Teichteil-Königsbuch\
*Proceedings of the AAAI Conference on Artificial Intelligence* · Jul 22, 2012 · 61 citations

> Optimal solutions to Stochastic Shortest Path Problems (SSPs) usually require that there exists at least one policy that reaches the goal with probability 1 from the initial state. This condition is very strong and prevents from solving many interesting problems, for instance where all possible policies reach some dead-end states with a positive probability. We introduce a more general and richer dual optimization criterion, which minimizes the average (undiscounted) cost of only paths leading to the goal among all policies that maximize the probability to reach the goal. We present policy update equations in the form of dynamic programming for this new dual criterion, which are different from the standard Bellman equations, but produce the same solution if there exists one policy leading to the goal with probability 1 from the initial state. We demonstrate that our equations converge in infinite horizon without any condition on the structure of the problem or on its policies, which actually extends the class of SSPs that can be solved. We experimentally show that our dual criterion provides well-founded solutions to SSPs that can not be solved by the standard criterion, and that using a discount factor with the latter certainly provides solution policies but which are not optimal considering our well-founded criterion.

------------------------------------------------------------------------

10\. · 100% match · 1987 · 3.0 cit/yr\
**Design of adaptive algorithms for the tracking of time‐varying systems** ([link](https://doi.org/10.1002/ACS.4480010103))\
A. Benveniste\
*International Journal of Adaptive Control and Signal Processing* · Sep 1, 1987 · 115 citations

> Abstract The design of adaptive algorithms for the purpose of the tracking of slowly time varying systems is investigated . A criterion for measuring the tracking capability of an algorithm in this situation was introduced in an earlier work; the domain of vali dity of this criterion is shown to be much wider than expected before. On the other hand, multistep algorithms, introduced in the Soviet literature, are generalized and systematically studied; they are shown to provide significant improvements over the classical (one-step) methods for the purpose of tracking. Finally, a complete design me thodology for adaptive algorithms used on time varying systems is given.

------------------------------------------------------------------------

11\. · 100% match · 1987 · 1.4 cit/yr\
**Asymptotically efficient self-tuning regulators** ([link](https://doi.org/10.1137/0325026))\
T. Lai and C. Z. Wei\
*Siam Journal on Control and Optimization* · Mar 1, 1987 · 54 citations

> This paper studies the problem of adaptive regulation of linear systems with white-noise disturbances. The apparent dilemma between the control objective and the need of information for parameter estimation is resolved by occasional use of white-noise probing inputs and by a reparametrization of the model. Insights into the question concerning how often and when such probing inputs should be introduced are provided by the concept of “asymptotic efficiency,” which quantifies the asymptotically minimal cost due to parameter ignorance, or equivalently, due to the infeasibility of using the optimal regulator that assumes knowledge of the system parameters. Asymptotically efficient adaptive regulators are constructed by making use of certain basic properties of adaptive predictors involving recursive least squares for the reparametrized model.

------------------------------------------------------------------------

12\. · 100% match · 2017 · 3.5 cit/yr\
**Efficient solutions for Stochastic Shortest Path Problems with Dead Ends** ([link](https://www.semanticscholar.org/paper/9d217059284f4efda99fdff13f5e405364242b9a))\
Felipe W. Trevizan, F. Teichteil-Königsbuch, and S. Thiébaux\
*Conference on Uncertainty in Artificial Intelligence* · 33 citations

> Many planning problems require maximizing the probability of goal satisfaction as well as minimizing the expected cost to reach the goal. To model and solve such problems, there have been several attempts at extending Stochastic Shortest Path problems (SSPs) to deal with dead ends and optimize a dual optimization criterion. Unfortunately these extensions lack either theoretical robustness or practical efﬁciency. We study a new, perhaps more natural optimization criterion capturing these problems, the Min-Cost given Max-Prob (MCMP) criterion. This criterion leads to the minimum expected cost policy among those with maximum success probability, and accurately accounts for the cost and risk of reaching dead ends. Moreover, it lends itself to efﬁcient solution methods that build on recent heuristic search algorithms for the dual representation of stochastic shortest paths problems. Our experiments show up to one order of magnitude speed-up over the state of the art.

------------------------------------------------------------------------

13\. · 100% match · 2021 · 4.0 cit/yr\
**Safe Value Functions** ([link](https://doi.org/10.1109/TAC.2022.3200948))\
P. Massiani, Steve Heim, Friedrich Solowjow, and Sebastian Trimpe\
*IEEE Transactions on Automatic Control* · May 25, 2021 · 20 citations

> Safety constraints and optimality are important but sometimes conflicting criteria for controllers. Although these criteria are often solved separately with different tools to maintain formal guarantees, it is also common practice in reinforcement learning (RL) to simply modify reward functions by penalizing failures, with the penalty treated as a mere heuristic. We rigorously examine the relationship of both safety and optimality to penalties, and formalize sufficient conditions for safe value functions (SVFs): value functions that are both optimal for a given task, and enforce safety constraints. We reveal this structure by examining when rewards preserve viability under optimal control, and show that there always exists a finite penalty that induces an SVF. This penalty is not unique, but upper-unbounded: larger penalties do not harm optimality. Although it is often not possible to compute the minimum required penalty, we reveal clear structure of how the penalty, rewards, discount factor, and dynamics interact. This insight suggests practical, theory-guided heuristics to design reward functions for control problems where safety is important.

------------------------------------------------------------------------

14\. · 100% match · 2024 · 7.6 cit/yr\
**Online Linear Regression in Dynamic Environments via Discounting** ([link](https://doi.org/10.48550/arXiv.2405.19175))\
A. Jacobsen and Ashok Cutkosky\
*International Conference on Machine Learning* · May 29, 2024 · 15 citations

> We develop algorithms for online linear regression which achieve optimal static and dynamic regret guarantees \emph{even in the complete absence of prior knowledge}. We present a novel analysis showing that a discounted variant of the Vovk-Azoury-Warmuth forecaster achieves dynamic regret of the form $`R_{T}(\vec{u})\le O\left(d\log(T)\vee \sqrt{dP_{T}^{\gamma}(\vec{u})T}\right)`$, where $`P_{T}^{\gamma}(\vec{u})`$ is a measure of variability of the comparator sequence, and show that the discount factor achieving this result can be learned on-the-fly. We show that this result is optimal by providing a matching lower bound. We also extend our results to \emph{strongly-adaptive} guarantees which hold over every sub-interval $`[a,b]\subseteq[1,T]`$ simultaneously.

------------------------------------------------------------------------

15\. · 100% match · 2020 · 0.5 cit/yr\
**A randomized relaxation method to ensure feasibility in stochastic control of linear systems subject to state and input constraints** ([link](https://doi.org/10.1016/j.automatica.2020.108854))\
Luca Deori, S. Garatti, and M. Prandini\
*Autom.* · May 1, 2020 · 3 citations

> Abstract We consider a linear system affected by an additive stochastic disturbance and address the design of a finite horizon control policy that is optimal according to some cost criterion and accounts also for probabilistic constraints on both the input and state variables. The resulting policy can be implemented over a receding horizon according to the model predictive control strategy. Such a possibility, however, is hampered by the fact that a feasibility issue may arise when recomputing the policy. Infeasibility indeed can occur if the disturbance has unbounded support and the state is required to remain in a bounded set. In this paper, we propose a solution to this issue that is based on the introduction of a constraint relaxation that becomes effective only when the original problem turns out to be unfeasible. This is obtained via a cascade of two probabilistically-constrained optimization problems where, in the first one, performance is neglected and the policy is designed to fully recover feasibility or – if this is not possible – to determine the minimum level of relaxation which is needed to recover feasibility; in the second step, such a minimum relaxation level is imposed while optimally (re-)tuning the control policy parameters. Both problems are solved through a computationally tractable scenario-based scheme using a finite number of disturbance realizations and providing an approximate solution that satisfies with high confidence the original probabilistic constraints of the cascade.

------------------------------------------------------------------------

16\. · 100% match · 2018 · 4.6 cit/yr\
**On-Line Learning of Linear Dynamical Systems: Exponential Forgetting in Kalman Filters** ([link](https://doi.org/10.1609/aaai.v33i01.33014098))\
Mark Kozdoba, Jakub Marecek, T. Tchrakian, and Shie Mannor\
*AAAI Conference on Artificial Intelligence* · Sep 16, 2018 · 35 citations

> The Kalman filter is a key tool for time-series forecasting and analysis. We show that the dependence of a prediction of Kalman filter on the past is decaying exponentially, whenever the process noise is non-degenerate. Therefore, Kalman filter may be approximated by regression on a few recent observations. Surprisingly, we also show that having some process noise is essential for the exponential decay. With no process noise, it may happen that the forecast depends on all of the past uniformly, which makes forecasting more difficult.Based on this insight, we devise an on-line algorithm for improper learning of a linear dynamical system (LDS), which considers only a few most recent observations. We use our decay results to provide the first regret bounds w.r.t. to Kalman filters within learning an LDS. That is, we compare the results of our algorithm to the best, in hindsight, Kalman filter for a given signal. Also, the algorithm is practical: its per-update run-time is linear in the regression depth.

------------------------------------------------------------------------

17\. · 100% match · 1984 · 4.5 cit/yr\
**Tracking of Slowly Varying Parameters by Directional Forgetting** ([link](https://doi.org/10.1016/S1474-6670(17%2961051-6))\
R. Kulhavý and M. Kárný\
*IFAC Proceedings Volumes* · Jul 1, 1984 · 189 citations

------------------------------------------------------------------------

18\. · 100% match · 2019 · 7.6 cit/yr\
**Probabilistic planning with formal performance guarantees for mobile service robots** ([link](https://doi.org/10.1177/0278364919856695))\
Bruno Lacerda, Fatma Faruq, David Parker, and Nick Hawes\
*The International Journal of Robotics Research* · Jun 16, 2019 · 53 citations

> We present a framework for mobile service robot task planning and execution, based on the use of probabilistic verification techniques for the generation of optimal policies with attached formal performance guarantees. Our approach is based on a Markov decision process model of the robot in its environment, encompassing a topological map where nodes represent relevant locations in the environment, and a range of tasks that can be executed in different locations. The navigation in the topological map is modeled stochastically for a specific time of day. This is done by using spatio-temporal models that provide, for a given time of day, the probability of successfully navigating between two topological nodes, and the expected time to do so. We then present a methodology to generate cost optimal policies for tasks specified in co-safe linear temporal logic. Our key contribution is to address scenarios in which the task may not be achievable with probability one. We introduce a task progression function and present an approach to generate policies that are formally guaranteed to, in decreasing order of priority: maximize the probability of finishing the task; maximize progress towards completion, if this is not possible; and minimize the expected time or cost required. We illustrate and evaluate our approach with a scalability evaluation in a simulated scenario, and report on its implementation in a robot performing service tasks in an office environment for long periods of time.

------------------------------------------------------------------------

19\. · 100% match · 1987 · 9.1 cit/yr\
**Persistent excitation in adaptive systems** ([link](https://doi.org/10.1080/00207178708933715))\
K. Narendra and A. Annaswamy\
*International Journal of Control* · 358 citations

> The importance of the concept of persistent excitation (PE) in adaptive identification and control has been recognized for some time. Recently it has become evident that it also plays a central role in many questions related to the robustness of adaptive systems. There is every reason to believe that arguments involving this concept will continue to feature prominently in the analysis of most of the important problems of adaptive control. Hence there is a real need for a deeper understanding of the concept. The paper is written with three objectives. The first, which is tutorial in nature, is to provide a general framework for the discussion of persistent excitation and to collect results in the area, which are scattered throughout the adaptive literature. The second objective is to present some new results related to the uniform asymptotic stability (u.a.s.) and robustness of adaptive systems and the relation of PE to the stability properties of a class of non-linear systems. The final objective is to di…

------------------------------------------------------------------------

20\. · 98% match · 1993 · 5.2 cit/yr\
**On a general concept of forgetting** ([link](https://doi.org/10.1080/00207179308923034))\
R. Kulhavý and M. Zarrop\
*International Journal of Control* · Oct 1, 1993 · 169 citations

> Practice leads us to seek a simple method which would make parameter estimation (and subsequent control or signal processing) reliably adaptive. Unfortunately, in most applications we lack sufficient information to specify a complete model of parameter variations. In other words, the problem is ‘under-determined’ which prevents us from employing standard equations of probability calculus. In this paper we apply known principles of rational behaviour in such situations to propose a plausible and well justified solution. The result we get is close to classical exponential forgetting, but regularized by available prior information. We demonstrate the practical implications of this feature.

------------------------------------------------------------------------

21\. · 96% match · 2017 · 26 cit/yr\
**Stochastic model predictive control with active uncertainty learning: A Survey on dual control** ([link](https://doi.org/10.1016/j.arcontrol.2017.11.001))\
A. Mesbah\
*Annu. Rev. Control.* · Nov 20, 2017 · 217 citations

------------------------------------------------------------------------

22\. · 95% match · 2016 · 0.1 cit/yr\
**Risk-Averse ω-regular Markov Decision Process Control** ([link](https://www.semanticscholar.org/paper/83f40dc9d6c3196e5ff4f156820d4274d92ef815))\
Rüdiger Ehlers, Salar Moarref, and U. Topcu\
*ArXiv* · Mar 22, 2016 · 1 citations

> Many control problems in environments that can be modeled as Markov decision processes (MDPs) concern infinite-time horizon specifications. The classical aim in this context is to compute a control policy that maximizes the probability of satisfying the specification. In many scenarios, there is however a non-zero probability of failure in every step of the system’s execution. For infinite-time horizon specifications, this implies that the specification is violated with probability 1 in the long run no matter what policy is chosen, which prevents previous policy computation methods from being useful in these scenarios. In this paper, we introduce a new optimization criterion for MDP policies that captures the task of working towards the satisfaction of some infinite-time horizon $`\omega`$-regular specification. The new criterion is applicable to MDPs in which the violation of the specification cannot be avoided in the long run. We give an algorithm to compute policies that are optimal in this criterion and show that it captures the ideas of optimism and risk-averseness in MDP control: while the computed policies are optimistic in that a MDP run enters a failure state relatively late, they are risk-averse by always maximizing the probability to reach their respective next goal state. We give results on two robot control scenarios to validate the usability of risk-averse MDP policies.

------------------------------------------------------------------------

23\. · 95% match · 2020 · 8.8 cit/yr\
**Optimal Probabilistic Motion Planning With Potential Infeasible LTL Constraints** ([link](https://doi.org/10.1109/TAC.2021.3138704))\
Mingyu Cai, Shaoping Xiao, Zhijun Li, and Z. Kan\
*IEEE Transactions on Automatic Control* · Jul 28, 2020 · 51 citations

> This paper studies optimal motion planning subject to motion and environment uncertainties. By modeling the system as a probabilistic labeled Markov decision process (PL-MDP), the control objective is to synthesize a finite-memory policy, under which the agent satisfies complex high-level tasks expressed as linear temporal logic (LTL) with desired satisfaction probability. In particular, the cost optimization of the trajectory that satisfies infinite horizon tasks is considered, and the trade-off between reducing the expected mean cost and maximizing the probability of task satisfaction is analyzed. The LTL formulas are converted to limit-deterministic Büchi automata (LDBA) with a reachability acceptance condition and a compact graph structure. The novelty of this work lies in considering the cases where LTL specifications can be potentially infeasible and developing a relaxed product MDP between PL- MDP and LDBA. The relaxed product MDP allows the agent to revise its motion plan whenever the task is not fully feasible and quantify the revised plan’s violation measurement. A multi- objective optimization problem is then formulated to jointly consider the probability of task satisfaction, the violation with respect to original task constraints, and the implementation cost of the policy execution. The formulated problem can be solved via coupled linear programs. This work first bridges the gap between probabilistic planning revision of potential infeasible LTL specifications and optimal control synthesis of both plan prefix and plan suffix of the trajectory over the infinite horizons. Experimental results are provided to demonstrate the effectiveness of the proposed framework.

------------------------------------------------------------------------

24\. · 94% match · 1976 · 1.3 cit/yr\
**Caution, Probing, and the Value of Information in the Control of Uncertain Systems** ([link](https://www.semanticscholar.org/paper/239c259f0ffcc625c38c26daf37bd7f027c0998d))\
Y. Bar-Shalom and E. Tse\
Jul 1, 1976 · 67 citations

------------------------------------------------------------------------

25\. · 92% match · 1990 · 4.2 cit/yr\
**Estimating time-varying parameters by the Kalman filter based algorithm: stability and convergence** ([link](https://doi.org/10.1109/9.45169))\
Lei Guo\
*IEEE Transactions on Automatic Control* · Feb 1, 1990 · 154 citations

> Convergence and stability properties of the Kalman filter-based parameter estimator are established for linear stochastic time-varying regression models. The main features are: both the variances and sample path averages of the parameter tracking error are shown to be bounded; the regression vector includes both stochastic and deterministic signals, and no assumptions of stationarity or independence are requires; and the unknown parameters are only assumed to have bounded variations in an average sense. \>

------------------------------------------------------------------------

26\. · 90% match · 2020 · 19 cit/yr\
**Reinforcement Learning for Non-Stationary Markov Decision Processes: The Blessing of (More) Optimism** ([link](https://www.semanticscholar.org/paper/5b3e68658c99ed9c461a909b16b862221946d6ad))\
Wang Chi Cheung, D. Simchi-Levi, and Ruihao Zhu\
*ArXiv* · Jun 24, 2020 · 114 citations

> We consider un-discounted reinforcement learning (RL) in Markov decision processes (MDPs) under drifting non-stationarity, i.e., both the reward and state transition distributions are allowed to evolve over time, as long as their respective total variations, quantified by suitable metrics, do not exceed certain variation budgets. We first develop the Sliding Window Upper-Confidence bound for Reinforcement Learning with Confidence Widening (SWUCRL2-CW) algorithm, and establish its dynamic regret bound when the variation budgets are known. In addition, we propose the Bandit-over-Reinforcement Learning (BORL) algorithm to adaptively tune the SWUCRL2-CW algorithm to achieve the same dynamic regret bound, but in a parameter-free manner, i.e., without knowing the variation budgets. Notably, learning non-stationary MDPs via the conventional optimistic exploration technique presents a unique challenge absent in existing (non-stationary) bandit learning settings. We overcome the challenge by a novel confidence widening technique that incorporates additional optimism.

------------------------------------------------------------------------

27\. · 90% match · 2011 · 3.6 cit/yr\
**A Reinforcement Learning Theory for Homeostatic Regulation** ([link](https://www.semanticscholar.org/paper/ea210f761a19395d4b70f53dec2b6f446db22ebe))\
Mehdi Keramati and B. Gutkin\
*Neural Information Processing Systems* · Dec 12, 2011 · 52 citations

> Reinforcement learning models address animal’s behavioral adaptation to its changing “external” environment, and are based on the assumption that Pavlovian, habitual and goal-directed responses seek to maximize reward acquisition. Negative-feedback models of homeostatic regulation, on the other hand, are concerned with behavioral adaptation in response to the “internal” state of the animal, and assume that animals’ behavioral objective is to minimize deviations of some key physiological variables from their hypothetical setpoints. Building upon the drive-reduction theory of reward, we propose a new analytical framework that integrates learning and regulatory systems, such that the two seemingly unrelated objectives of reward maximization and physiological-stability prove to be identical. The proposed theory shows behavioral adaptation to both internal and external states in a disciplined way. We further show that the proposed framework allows for a unified explanation of some behavioral pattern like motivational sensitivity of different associative learning mechanism, anticipatory responses, interaction among competing motivational systems, and risk aversion.

------------------------------------------------------------------------

28\. · 90% match · 2015 · 6.4 cit/yr\
**This Time the Robot Settles for a Cost: A Quantitative Approach to Temporal Logic Planning with Partial Satisfaction** ([link](https://doi.org/10.1609/aaai.v29i1.9670))\
Morteza Lahijanian, Shaull Almagor, Dror Fried, L. Kavraki, and Moshe Y. Vardi\
*AAAI Conference on Artificial Intelligence* · Jan 25, 2015 · 72 citations

> The specification of complex motion goals through temporal logics is increasingly favored in robotics to narrow the gap between task and motion planning. A major limiting factor of such logics, however, is their Boolean satisfaction condition. To relax this limitation, we introduce a method for quantifying the satisfaction of co-safe linear temporal logic specifications, and propose a planner that uses this method to synthesize robot trajectories with the optimal satisfaction value. The method assigns costs to violations of specifications from user-defined proposition costs. These violation costs define a distance to satisfaction and can be computed algorithmically using a weighted automaton. The planner utilizes this automaton and an abstraction of the robotic system to construct a product graph that captures all possible robot trajectories and their distances to satisfaction. Then, a plan with the minimum distance to satisfaction is generated by employing this graph as the high-level planner in a synergistic planning framework. The efficacy of the method is illustrated on a robot with unsatisfiable specifications in an office environment.

------------------------------------------------------------------------

29\. · 88% match · 1991 · 1.1 cit/yr\
**A result on the mean square error obtained using general tracking algorithms** ([link](https://doi.org/10.1002/ACS.4480050402))\
L. Ljung and P. Priouret\
*International Journal of Adaptive Control and Signal Processing* · Jul 1, 1991 · 37 citations

> Tracking time-varying properties is of crucial importance in all adaptive algorithms. In this contribution we study a fairly general algorithm for tracking properties of model parameters that can be described in a linear regression form (including AR models and the like). An explicit expression for the mean square error between the estimated and the true (time-varying) parameter is established. For slow adaptation this expression can be arbitrarily well approximated by a much simpler expression. The treatment differs from other related studies using weak convergence theory, averaging, etc. in that the results are not asymptotic in nature and are applicable also to the transient phase as well as over unbounded time intervals.

------------------------------------------------------------------------

30\. · 87% match · 1985 · 7.5 cit/yr\
**Restricted exponential forgetting in real-time identification** ([link](https://doi.org/10.1016/0005-1098(87%2990054-9))\
R. Kulhavý\
*Autom.* · Jul 1, 1985 · 307 citations

------------------------------------------------------------------------

31\. · 86% match · 2000 · 6.0 cit/yr\
**Survey of adaptive dual control methods** ([link](https://doi.org/10.1049/IP-CTA:20000107))\
N. Filatov and H. Unbehauen\
158 citations

> A survey of adaptive dual control methods, elaborated from the early 1960s until the present, is given. The development of dual control methods is considered in chronological order, taking into account its close interconnection with general progress in adaptive control theory and applications. Detailed classifications of stochastic adaptive control methods and dual control methods are presented. The properties of a neutral control system and the nature of the dual effect in adaptive control systems are described. The historical stages of the development of the theory and applications of dual control are reviewed.

------------------------------------------------------------------------

32\. · 85% match · 2014 · 2.4 cit/yr\
**On the minimal revision problem of specification automata** ([link](https://doi.org/10.1177/0278364915587034))\
Kangjin Kim, Georgios Fainekos, and S. Sankaranarayanan\
*The International Journal of Robotics Research* · Apr 8, 2014 · 29 citations

> As robots are being integrated into our daily lives, it becomes necessary to provide guarantees on their safe and provably correct operation. Such guarantees can be provided using automata theoretic task and mission planning where the requirements are expressed as temporal logic specifications. However, in real-life scenarios, it is to be expected that not all user task requirements can be realized by the robot. In such cases, the robot must provide feedback to the user on why it cannot accomplish a given task. Moreover, the robot should indicate what tasks it can accomplish which are as “close” as possible to the initial user intent. This paper establishes that the latter problem, which is referred to as the minimal specification revision problem, is NP-complete. A heuristic algorithm is presented that can compute good approximations to the Minimal Revision Problem (MRP) in polynomial time. The experimental study of the algorithm demonstrates that in most problem instances the heuristic algorithm actually returns the optimal solution. Finally, some cases where the algorithm does not return the optimal solution are presented.

------------------------------------------------------------------------

33\. · 85% match · 2015 · 53 cit/yr\
**Active Inference, homeostatic regulation and adaptive behavioural control** ([link](https://doi.org/10.1016/j.pneurobio.2015.09.001))\
G. Pezzulo, Francesco Rigoli, and Karl J. Friston\
*Progress in Neurobiology* · Nov 1, 2015 · 556 citations

> Highlights • An Active Inference account of homeostatic regulation and behavioural control.• Pavlovian, habitual and goal-directed behaviours explained with one scheme.• A possible phylogenetic trajectory from simpler to hierarchical controllers.• Precision-dependent processes regulate habitual and goal-directed behaviour.

------------------------------------------------------------------------

34\. · 84% match · 1972 · 2.3 cit/yr\
**An actively adaptive control for linear systems with random parameters via the dual control approach** ([link](https://doi.org/10.1109/CDC.1972.269088))\
E. Tse and Y. Bar-Shalom\
*IEEE Conference on Decision and Control* · Dec 1, 1972 · 123 citations

> A new method is presented for controlling a discrete-time linear system with, possibly time-varying, random parameters in the presence of input and output noise. The cost is assumed to be quadratic in the state and control. Previous algorithms for the above problem when the system had both zeroes and poles unknown were of the open-loop feedback type, i.e., they did not take into account that future observations will be made. Therefore, even though these schemes were adaptive, their learning was “accidental”. In contrast to this, the new approach uses an expression of the optimal cost-to-go that exhibits the dual purpose of the control: learning and control. The effect of the present control on the future estimation (“learning”) appears explicitly in the cost used in the stochastic dynamic programming equation. The resulting sequence of controls, which is of the closed-loop type, is shown via simulations to appropriately divide its energy between the learning and the control purposes. Therefore, this control is called actively adaptive because it regulates the speed and amount of learning as required by the performance index. The simulations on a third order system with six unknown parameters also demonstrate the computational feasibility of the proposed algorithm.

------------------------------------------------------------------------

35\. · 82% match · 1988 · 5.9 cit/yr\
**Modified least squares algorithm incorporating exponential resetting and forgetting** ([link](https://doi.org/10.1080/00207178808906026))\
M. Salgado, G. Goodwin, and R. Middleton\
*International Journal of Control* · Feb 1, 1988 · 227 citations

> In this paper we present the general analysis of a class of least squares algorithms with emphasis on their dynamic performance particularly in the presence of poor excitation. The analysis is carried out in a deterministic framework and stresses geometrical interpretations. The core of this paper is the proposal and analysis of a new algorithm which incorporates exponential forgetting and resetting to an unprejudiced treatment of data when excitation is poor. The algorithm is particularly suitable for tracking time-varying parameters and is similar in computational complexity to the standard recursive least squares algorithm. The superior performance of the algorithm is verified via simulation studies.

------------------------------------------------------------------------

36\. · 82% match · 2023 · 1.3 cit/yr\
**Bi-Objective Lexicographic Optimization in Markov Decision Processes with Related Objectives** ([link](https://doi.org/10.48550/arXiv.2305.09634))\
Damien Busatto-Gaston et al.\
*ArXiv* · May 16, 2023 · 4 citations

> We consider lexicographic bi-objective problems on Markov Decision Processes (MDPs), where we optimize one objective while guaranteeing optimality of another. We propose a two-stage technique for solving such problems when the objectives are related (in a way that we formalize). We instantiate our technique for two natural pairs of objectives: minimizing the (conditional) expected number of steps to a target while guaranteeing the optimal probability of reaching it; and maximizing the (conditional) expected average reward while guaranteeing an optimal probability of staying safe (w.r.t. some safe set of states). For the first combination of objectives, which covers the classical frozen lake environment from reinforcement learning, we also report on experiments performed using a prototype implementation of our algorithm and compare it with what can be obtained from state-of-the-art probabilistic model checkers solving optimal reachability.

------------------------------------------------------------------------

37\. · 80% match · 2015 · 61 cit/yr\
**Active inference and epistemic value** ([link](https://doi.org/10.1080/17588928.2015.1020053))\
Karl J. Friston et al.\
*Cognitive Neuroscience* · Feb 17, 2015 · 682 citations

> We offer a formal treatment of choice behavior based on the premise that agents minimize the expected free energy of future outcomes. Crucially, the negative free energy or quality of a policy can be decomposed into extrinsic and epistemic (or intrinsic) value. Minimizing expected free energy is therefore equivalent to maximizing extrinsic value or expected utility (defined in terms of prior preferences or goals), while maximizing information gain or intrinsic value (or reducing uncertainty about the causes of valuable outcomes). The resulting scheme resolves the exploration-exploitation dilemma: Epistemic value is maximized until there is no further information gain, after which exploitation is assured through maximization of extrinsic value. This is formally consistent with the Infomax principle, generalizing formulations of active vision based upon salience (Bayesian surprise) and optimal decisions based on expected utility and risk-sensitive (Kullback-Leibler) control. Furthermore, as with previous active inference formulations of discrete (Markovian) problems, ad hoc softmax parameters become the expected (Bayes-optimal) precision of beliefs about, or confidence in, policies. This article focuses on the basic theory, illustrating the ideas with simulations. A key aspect of these simulations is the similarity between precision updates and dopaminergic discharges observed in conditioning paradigms.

------------------------------------------------------------------------

38\. · 80% match · 2008\
**Robust and stochastic viability** ([link](https://doi.org/10.1007/978-3-540-79074-7_7))\
M. Lara and L. Doyen\
0 citations

------------------------------------------------------------------------

39\. · 79% match · 2013 · 1.2 cit/yr\
**An MPC Approach to Dual Control** ([link](https://doi.org/10.3182/20131218-3-IN-2045.00151))\
Tor Aksel N. Heirung, B. Ydstie, and B. Foss\
*IFAC Proceedings Volumes* · Dec 1, 2013 · 15 citations

> Abstract We present a model predictive control (MPC) approach to solve the dual adaptive control problem. The cost function minimized by the controller rewards probing the system for information when the parameter estimates are poor. The control algorithm is designed to handle poorly identified models and excites the system so that information can be gathered to achieve the optimal trade-off between process control and identification. This excitation is achieved without requiring the input to be persistently exciting; rather, the probing objective is based on an exact formulation of the expected value of the output error at the first time stage. The resulting expression is also used for the second time stage; this ensures that a proper trade-off between excitation and output regulation is maintained. The algorithm can be viewed as the merging of adaptive control with MPC and its design can easily be implemented with modifications to an existing MPC. As an example we consider a first-order linear process system with two unknown parameters. Our proposed algorithm probes the system even when the output error is small and quickly gathers enough information to correctly identify the unknown plant parameters.

------------------------------------------------------------------------

40\. · 78% match · 2016 · 0.8 cit/yr\
**On Reward Function for Survival** ([link](https://www.semanticscholar.org/paper/0466f1aaa36e2f174c0153475099a4f47ffa35cc))\
N. Yoshida\
*ArXiv* · Jun 18, 2016 · 8 citations

> Obtaining a survival strategy (policy) is one of the fundamental problems of biological agents. In this paper, we generalize the formulation of previous research related to the survival of an agent and we formulate the survival problem as a maximization of the multi-step survival probability in future time steps. We introduce a method for converting the maximization of multi-step survival probability into a classical reinforcement learning problem. Using this conversion, the reward function (negative temporal cost function) is expressed as the log of the temporal survival probability. And we show that the objective function of the reinforcement learning in this sense is proportional to the variational lower bound of the original problem. Finally, We empirically demonstrate that the agent learns survival behavior by using the reward function introduced in this paper.

------------------------------------------------------------------------

41\. · 78% match · 2011 · 25 cit/yr\
**Viability Theory: New Directions** ([link](https://doi.org/10.1007/978-3-642-16684-6))\
J. Aubin, A. Bayen, and P. Saint-Pierre\
Jul 19, 2011 · 366 citations

------------------------------------------------------------------------

42\. · 75% match · 2012 · 16 cit/yr\
**Active inference and agency: optimal control without cost functions** ([link](https://doi.org/10.1007/s00422-012-0512-8))\
Karl J. Friston, Spyridon Samothrakis, and P. Montague\
*Biological Cybernetics* · Oct 1, 2012 · 223 citations

> This paper describes a variational free-energy formulation of (partially observable) Markov decision problems in decision making under uncertainty. We show that optimal control can be cast as active inference. In active inference, both action and posterior beliefs about hidden states minimise a free energy bound on the negative log-likelihood of observed states, under a generative model. In this setting, reward or cost functions are absorbed into prior beliefs about state transitions and terminal states. Effectively, this converts optimal control into a pure inference problem, enabling the application of standard Bayesian filtering techniques. We then consider optimal trajectories that rest on posterior beliefs about hidden states in the future. Crucially, this entails modelling control as a hidden state that endows the generative model with a representation of agency. This leads to a distinction between models with and without inference on hidden control states; namely, agency-free and agency-based models, respectively.

------------------------------------------------------------------------

43\. · 75% match · 2021 · 1.4 cit/yr\
**Efficient Strategy Synthesis for MDPs With Resource Constraints** ([link](https://doi.org/10.1109/TAC.2022.3209612))\
František Blahoudek, Petr Novotn’y, M. Ornik, Pranay Thangeda, and U. Topcu\
*IEEE Transactions on Automatic Control* · May 5, 2021 · 7 citations

> We consider qualitative strategy synthesis for the formalism called consumption Markov decision processes. This formalism can model the dynamics of an agent that operates under resource constraints in a stochastic environment. The presented algorithms work in time polynomial with respect to the representation of the model and they synthesize strategies ensuring that a given set of goal states will be reached (once or infinitely many times) with probability 1 without resource exhaustion. In particular, when the amount of resource becomes too low to safely continue in the mission, the strategy changes course of the agent toward one of a designated set of reload states where the agent replenishes the resource to full capacity; with a sufficient amount of resource, the agent attempts to fulfill the mission again. We also present two heuristics that attempt to reduce the expected time that the agent needs to fulfill the given mission, a parameter important in practical planning. The presented algorithms were implemented, and the numerical examples demonstrate the effectiveness (in terms of computation time) of the planning approach based on consumption Markov decision processes and the positive impact of the two heuristics on planning in a realistic example.

------------------------------------------------------------------------

44\. · 72% match · 2019 · 0.6 cit/yr\
**Viability of an open set for stochastic control systems** ([link](https://doi.org/10.1016/J.SPA.2018.11.012))\
R. Buckdahn, Hélène Frankowska, and M. Quincampoix\
*Stochastic Processes and their Applications* · Oct 1, 2019 · 4 citations

> Abstract The problem of compatibility of a stochastic control system and a set of constraints – the so called viability property – has been widely investigated during the last three decades. Given a stochastic control system, the question is to characterize sets A such that for any initial condition in A there exists a control ensuring that the associated stochastic process remains forever almost surely in A (this is called the viability property of A ). When A is closed and the dynamics is continuous, the viability property has been characterized in the literature through several equivalent geometric conditions involving A , the drift and the diffusion of the control system. In this article we give a necessary and sufficient condition involving the boundary of an open set A ensuring the viability property of A , whenever A has a C 2 , 1 boundary and the dynamics are Lipschitz. If moreover a classical convexity condition on the control dynamics holds true, we show that the viability of an open set A is equivalent to the viability of its closure. This last result is rather surprising, because several very elementary examples in the deterministic framework show that, in general, there is no such equivalence for a general open set A . We will also discuss examples illustrating that the above equivalence is wrong when either the boundary of A does not have enough regularity, or the dynamics are not Lipschitz continuous.

------------------------------------------------------------------------

45\. · 70% match · 2013 · 38 cit/yr\
**Non-Stationary Stochastic Optimization** ([link](https://doi.org/10.1287/opre.2015.1408))\
Omar Besbes, Y. Gur, and A. Zeevi\
*Oper. Res.* · Jul 20, 2013 · 491 citations

> We consider a non-stationary variant of a sequential stochastic optimization problem, in which the underlying cost functions may change along the horizon. We propose a measure, termed variation budget , that controls the extent of said change, and study how restrictions on this budget impact achievable performance. We identify sharp conditions under which it is possible to achieve long-run average optimality and more refined performance measures such as rate optimality that fully characterize the complexity of such problems. In doing so, we also establish a strong connection between two rather disparate strands of literature: (1) adversarial online convex optimization and (2) the more traditional stochastic approximation paradigm (couched in a non-stationary setting). This connection is the key to deriving well-performing policies in the latter, by leveraging structure of optimal policies in the former. Finally, tight bounds on the minimax regret allow us to quantify the “price of non-stationarity,” which mathematically captures the added complexity embedded in a temporally changing environment versus a stationary one.

------------------------------------------------------------------------

46\. · 70% match · 2018 · 21 cit/yr\
**Learning to Optimize under Non-Stationarity** ([link](https://doi.org/10.2139/SSRN.3261050))\
Wang Chi Cheung, D. Simchi-Levi, and Ruihao Zhu\
*ArXiv* · Oct 5, 2018 · 160 citations

> We introduce algorithms that achieve state-of-the-art \emph{dynamic regret} bounds for non-stationary linear stochastic bandit setting. It captures natural applications such as dynamic pricing and ads allocation in a changing environment. We show how the difficulty posed by the non-stationarity can be overcome by a novel marriage between stochastic and adversarial bandits learning algorithms. Defining $`d,B_T,`$ and $`T`$ as the problem dimension, the \emph{variation budget}, and the total time horizon, respectively, our main contributions are the tuned Sliding Window UCB (\texttt{SW-UCB}) algorithm with optimal $`\widetilde{O}(d^{2/3}(B_T+1)^{1/3}T^{2/3})`$ dynamic regret, and the tuning free bandit-over-bandit (\texttt{BOB}) framework built on top of the \texttt{SW-UCB} algorithm with best $`\widetilde{O}(d^{2/3}(B_T+1)^{1/4}T^{3/4})`$ dynamic regret.

------------------------------------------------------------------------

47\. · 68% match · 1981 · 1.7 cit/yr\
**Deterministic convergence of a self-tuning regulator with variable forgetting factor** ([link](https://doi.org/10.1049/IP-D:19810004))\
A. O. Cordero and D. Mayne\
77 citations

> The usual implementation of Astrom’s self-tuning regulator employs a forgetting factor whose value is a compromise to meet the conflicting demands of low steady-state variance and rapid response to process changes. To obtain better performance a new self-tunning regulator with a variable forgetting factor has recently been proposed. The paper establishes the deterministic convergence of a suitable modified varsion of this algorithm.

------------------------------------------------------------------------

48\. · 66% match · 1995 · 0.6 cit/yr\
**A parallel adaptation algorithm for recursive-least-squares adaptive filters in nonstationary environments** ([link](https://doi.org/10.1109/78.482100))\
S. D. Peters and A. Antoniou\
*IEEE Trans. Signal Process.* · Nov 1, 1995 · 18 citations

> An accurate new expression for the steady-state tracking performance of exponentially weighted recursive-least-squares (RLS) adaptive filters in a random walk scenario is derived. This relation is then used to provide a detailed comparison between RLS-performance and that of normalized least-mean-squares adaptive filters. Further, a variable-forgetting-factor algorithm referred to as the parallel adaptation algorithm that approximately achieves the theoretical minimum mean-squared-error performance in a random walk scenario is developed. Extensive simulation results are presented to support the present findings and demonstrate the improved performance of the proposed algorithm in a number of different applications.

------------------------------------------------------------------------

49\. · 65% match · 1981 · 18 cit/yr\
**Implementation of self-tuning regulators with variable forgetting factors** ([link](https://doi.org/10.1016/0005-1098(81%2990070-4))\
T. Fortescue, L. Kershenbaum, and B. Ydstie\
*Autom.* · 826 citations

------------------------------------------------------------------------

50\. · 62% match · 2019 · 0.6 cit/yr\
**Active Roll-outs in MDP with Irreversible Dynamics** ([link](https://www.semanticscholar.org/paper/89c3d2fdf5e3885f7d3bf1fbfb939dd4dffa45df))\
Odalric-Ambrym Maillard, Timothy A. Mann, R. Ortner, and Shie Mannor\
Jul 9, 2019 · 4 citations

> In Reinforcement Learning (RL), regret guarantees scaling with the square root of the time horizon have been shown to hold only for communicating Markov decision processes (MDPs) where any two states are connected. This essentially means that an algorithm can eventually recover from any mistake. However, real-world tasks usually include situations where taking a single “bad” action can permanently trap a learner in a suboptimal region of the state-space. Since it is provably impossible to achieve sub-linear regret in general multi-chain MDPs, we assume a weak mechanism that allows the learner to request additional information. Our main contribution is to address: (i) how much external information is needed, (ii) how and when to use it, and (iii) how much regret is incurred. We design an algorithm that minimizes requests for external information in the form of rollouts of a policy specified by the learner by actively requesting it only when needed. The algorithm provably achieves O(√ T) active regret after T steps in a large class of multi-chain MDPs, by only requesting O(log(T)) rollout transitions. The superiority of our algorithm to standard algorithms such as R-Max and UCRL is demonstrated in experiments on some illustrative grid-world examples. (a) (b) (c) Figure 1: Example of (a) a communicating MDP, (b) a unichain MDP with a single recurrent class, and (c) a multi-chain MDP with two recurrent classes. The circles represent states while the labeled edges represent transitions due to executing actions {a, b, c}.

*Showing top 50 of 88 papers. Full details available via CSV or BibTeX export.*
