# Prior art for AAT agency theory

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT). The core claim is that an agent’s internal model of reality is a many-to-one compression of a strictly irreversible, non-forkable sequence of events (“chronica”). Under strict partial observability, where the agent never accesses true environment states, and under computational constraints that prevent storing full history, state updates must be recursive (Markovian). The framework further claims that the optimal compression of this history is characterized by the Information Bottleneck principle: maximizing predictive information about future observations while minimizing retained historical data. Prioritize broad conceptual predecessors and mathematical formalisms across theoretical computer science, control theory, reinforcement learning theory, and active inference, from early cybernetics through modern work. Relevant matches include formalisms that treat agent history as a singular discrete event sequence; proofs or derivations that recursive or Markovian updates are structurally forced by causality or computational limits in adaptive systems; formal applications of Information Bottleneck to predictive state representations, internal agent models, or memory in POMDPs; and conceptual predecessors that recognize model-class fitness or quantify how much predictive information a representational class retains. Exclude work centered on general RL memory buffers such as standard experience replay without information-theoretic compression limits, and standard POMDP literature that uses belief states without framing them as an optimal rate-distortion or Information Bottleneck compression of history. Known anchors include Tishby’s Information Bottleneck, Predictive State Representations, and Active Inference / the Free Energy Principle.

*Found 89 papers · May 20, 2026 · Estimated coverage of relevant papers: 96%*

## Summary of Results

The clearest prior-art chain is that prediction from a single irreversible observation history is formalized as minimal causal-state compression in computational mechanics \[1\], \[2\], recast for controlled partially observed systems as predictive state representations built entirely from observable action–observation histories \[3\], \[4\], and then optimized under explicit memory–prediction tradeoffs by the Information Bottleneck and predictive rate–distortion programs \[5\], \[6\], \[7\], \[8\].

#### Structural precedents

- Classical stochastic control already frames the agent’s effective state as a **function of history** that must support recursive updating under partial observation \[9\], \[10\].
- Modern information-state theory makes this explicit: a valid information state is precisely a history compression that is both sufficient for prediction/reward and recursively updateable, with approximate versions yielding approximate dynamic programs \[11\], \[12\].
- PSRs sharpen the same idea without latent environment-state access: state is a vector of predictions about future tests, derived from action–observation history rather than hidden-state posteriors \[3\], \[4\].

#### Information-theoretic compression line

- IB gives the canonical objective: minimize retained information about history while preserving information relevant to prediction \[5\].
- Predictive IB and optimal causal inference apply this directly to past→future compression, recovering graded approximations to causal architecture and, in the limit, exact causal states \[6\], \[7\], \[13\], \[14\].
- Predictive information quantifies how much of the past matters for the future and links retained predictive information to model-class complexity \[15\], \[16\].

#### Adjacent agency formalisms

- Active inference/free-energy work supplies a parallel variational treatment of internal generative models under partial observability, with explicit links to IB and bounded-rational control \[17\], \[18\], \[19\].

## Paper Catalog (89 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2000 | 165 | The information bottleneck method ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c)) | Naftali Tishby, Fernando C Pereira, and W. Bialek | ArXiv |
| 2 | 1999 | 19 | Computational Mechanics: Pattern and Prediction, Structure and Simplicity ([link](https://doi.org/10.1023/A:1010388907793)) | C. Shalizi and J. Crutchfield | Journal of Statistical Physics |
| 3 | 2009 | 5.2 | Past-future information bottleneck in dynamical systems. ([link](https://doi.org/10.1103/PHYSREVE.79.041925)) | F. Creutzig, A. Globerson, and Naftali Tishby | Physical review. E, Statistical, nonlinear, and soft matter physics |
| 4 | 2014 | 0.9 | Circumventing the Curse of Dimensionality in Prediction: Causal Rate-Distortion for Infinite-Order Markov Processes ([link](https://www.semanticscholar.org/paper/5308a461868cde8b8d175eee0de4eea699028d14)) | Sarah E. Marzen and J. Crutchfield | ArXiv |
| 5 | 2016 | 3.5 | Predictive Rate-Distortion for Infinite-Order Markov Processes ([link](https://doi.org/10.1007/s10955-016-1520-1)) | Sarah E. Marzen and J. Crutchfield | Journal of Statistical Physics |
| 6 | 2000 | 1.4 | Information Bottlenecks, Causal States, and Statistical Relevance Bases: How to Represent Relevant Information in memoryless transduction ([link](https://doi.org/10.1142/S0219525902000481)) | C. Shalizi and J. Crutchfield | Adv. Complex Syst. |
| 7 | 2014 | 5.1 | Information Bottleneck Approach to Predictive Inference ([link](https://doi.org/10.3390/e16020968)) | Susanne Still | Entropy |
| 8 | 2000 | 8.4 | Predictability, Complexity, and Learning ([link](https://doi.org/10.1162/089976601753195969)) | W. Bialek, I. Nemenman, and Naftali Tishby | Neural Computation |
| 9 | 2001 | 24 | Predictive Representations of State ([link](https://www.semanticscholar.org/paper/4a7de0669fd835b2efcab97c7d3dc28ea7a1e6a3)) | M. Littman, R. Sutton, and Satinder Singh | Neural Information Processing Systems |
| 10 | 2004 | 14 | Predictive State Representations: A New Theory for Modeling Dynamical Systems ([link](https://www.semanticscholar.org/paper/532c61a2af5cde64628d0cdd2ba0823800118d0f)) | Satinder Singh, Michael R. James, and Matthew R. Rudary | Conference on Uncertainty in Artificial Intelligence |
| 11 | 2020 | 20 | Approximate information state for approximate planning and reinforcement learning in partially observed systems ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980)) | Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan | ArXiv |
| 12 | 2012 | 21 | A Free Energy Principle for Biological Systems. ([link](https://doi.org/10.3390/E14112100)) | Karl J. Friston | Entropy |
| 13 | 2012 | 16 | Active inference and agency: optimal control without cost functions ([link](https://doi.org/10.1007/s00422-012-0512-8)) | Karl J. Friston, Spyridon Samothrakis, and P. Montague | Biological Cybernetics |
| 14 | 2010 | 45 | Action and behavior: a free-energy formulation ([link](https://doi.org/10.1007/s00422-010-0364-z)) | Karl J. Friston, J. Daunizeau, J. Kilner, and S. Kiebel | Biological Cybernetics |
| 15 | 2018 | 29 | Generalised free energy and active inference ([link](https://doi.org/10.1007/s00422-019-00805-w)) | Thomas Parr and Karl J. Friston | Biological Cybernetics |
| 16 | 2011 | 20 | Information Theory of Decisions and Actions ([link](https://doi.org/10.1007/978-1-4419-1452-1_19)) | Naftali Tishby and D. Polani |  |
| 17 | 2007 | 4.5 | Information-theoretic approach to interactive learning ([link](https://doi.org/10.1209/0295-5075/85/28005)) | Susanne Still | EPL (Europhysics Letters) |
| 18 | 2007 | 0.6 | Optimal Causal Inference ([link](https://www.semanticscholar.org/paper/0c8c8cd4275c7f3505ba0250d7f1be54842d9440)) | Susanne Still, J. Crutchfield, and C. J. Ellison | ArXiv |
| 19 | 2012 | 18 | The thermodynamics of prediction ([link](https://doi.org/10.1103/PhysRevLett.109.120604)) | Susanne Still, David A. Sivak, A. Bell, and G. Crooks | Physical review letters |
| 20 | 1989 | 26 | Inferring statistical complexity. ([link](https://doi.org/10.1103/PHYSREVLETT.63.105)) | J. Crutchfield and K. Young | Physical review letters |
| 21 | 1965 | 15 | Optimal control of Markov processes with incomplete state information ([link](https://doi.org/10.1016/0022-247X(65%2990154-X)) | K. Åström | Journal of Mathematical Analysis and Applications |
| 22 | 1965 | 3.3 | Sufficient statistics in the optimum control of stochastic systems ([link](https://doi.org/10.1016/0022-247X(65%2990027-2)) | C. Striebel | Journal of Mathematical Analysis and Applications |
| 23 | 2013 | 3.4 | Efficient learning and planning with compressed predictive states ([link](https://doi.org/10.5555/2627435.2750354)) | William L. Hamilton, M. M. Fard, and Joelle Pineau | J. Mach. Learn. Res. |
| 24 | 2010 | 3.1 | Predictive State Temporal Difference Learning ([link](https://www.semanticscholar.org/paper/c3e84987d911a2f3a02cd32f30507ca7169f1b0c)) | Byron Boots and Geoffrey J. Gordon | Neural Information Processing Systems |
| 25 | 2015 | 5.5 | Information-Theoretic Bounded Rationality ([link](https://www.semanticscholar.org/paper/a5a6611134e82077184a2d3b7a336c75402cdaaf)) | Pedro A. Ortega, Daniel A. Braun, Justin Dyer, Kee-Eung Kim, and Naftali Tishby | ArXiv |
| 26 | 2008 | 7.2 | A Minimum Relative Entropy Principle for Learning and Acting ([link](https://doi.org/10.1613/JAIR.3062)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 27 | 2017 | 3.3 | A Unified Bellman Equation for Causal Information and Value in Markov Decision Processes ([link](https://www.semanticscholar.org/paper/f5f235579f02d9fad0d18cd19795de7e45c2f8eb)) | Stas Tiomkin and Naftali Tishby | ArXiv |
| 28 | 1999 | 2.0 | Predictive Information ([link](https://www.semanticscholar.org/paper/3068a485e76bc6e7d274aa8e7b68ccb979a39a3d)) | W. Bialek and Naftali Tishby |  |
| 29 | 2019 | 5.4 | Approximate information state for partially observed systems ([link](https://doi.org/10.1109/CDC40024.2019.9029898)) | Jayakumar Subramanian and Aditya Mahajan | 2019 IEEE 58th Conference on Decision and Control (CDC) |
| 30 | 2020 | 8.6 | Near Optimality of Finite Memory Feedback Policies in Partially Observed Markov Decision Processes ([link](https://www.semanticscholar.org/paper/337566d4f14e00e32cfba465ae6a50a1e07404ca)) | A. D. Kara and S. Yüksel | J. Mach. Learn. Res. |
| 31 | 2002 | 1.8 | Pattern Discovery in Time Series, Part I: Theory, Algorithm, Analysis, and Convergence ([link](https://www.semanticscholar.org/paper/d3345b5eae4c0060505af5421edace8d99405244)) | C. Shalizi, Kristina Lisa Shalizi, and James P. Crutchfleld |  |
| 32 | 2001 | 11 | Causal architecture, complexity and self-organization in time series and cellular automata ([link](https://www.semanticscholar.org/paper/1530382baf56cd93d0fe69318efdfe060b4b7179)) | C. Shalizi and M. Olsson |  |
| 33 | 2009 | 6.9 | Prediction, Retrodiction, and the Amount of Information Stored in the Present ([link](https://doi.org/10.1007/s10955-009-9808-z)) | C. J. Ellison, J. Mahoney, and J. Crutchfield | Journal of Statistical Physics |
| 34 | 2009 | 7.5 | Time’s barbed arrow: irreversibility, crypticity, and stored information. ([link](https://doi.org/10.1103/PhysRevLett.103.094101)) | J. Crutchfield, C. J. Ellison, and J. Mahoney | Physical review letters |
| 35 | 2004 | 0.7 | Reductions of Hidden Information Sources ([link](https://doi.org/10.1007/s10955-005-6797-4)) | N. Ay and J. Crutchfield | Journal of Statistical Physics |
| 36 | 2014 | 5.2 | Computational Mechanics of Input–Output Processes: Structured Transformations and the ϵ\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt}  ([link](https://doi.org/10.1007/s10955-015-1327-5)) | Nix Barnett and J. Crutchfield | Journal of Statistical Physics |
| 37 | 2012 | 21 | Thermodynamics as a theory of decision-making with information-processing costs ([link](https://doi.org/10.1098/rspa.2012.0683)) | Pedro A. Ortega and Daniel A. Braun | Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences |
| 38 | 2015 | 12 | Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle ([link](https://doi.org/10.3389/frobt.2015.00027)) | Tim Genewein, Felix Leibfried, Jordi Grau-Moya, and Daniel A. Braun | Frontiers Robotics AI |
| 39 | 2020 | 40 | Active inference on discrete state-spaces: A synthesis ([link](https://doi.org/10.1016/j.jmp.2020.102447)) | Lancelot Da Costa et al. | Journal of Mathematical Psychology |
| 40 | 2013 | 26 | The anatomy of choice: active inference and agency ([link](https://doi.org/10.3389/fnhum.2013.00598)) | Karl J. Friston et al. | Frontiers in Human Neuroscience |
| 41 | 2025 |  | Decision, Inference, and Information: Formal Equivalences Under Active Inference ([link](https://doi.org/10.3390/e28010001)) | Patrick Sweeney, Jaime Ruiz-Serra, and Michael S. Harré | Entropy |
| 42 | 2008 | 0.7 | Approximate predictive state representations ([link](https://doi.org/10.65109/wtqk6477)) | Britton Wolfe, Michael R. James, and Satinder Singh | Adaptive Agents and Multi-Agent Systems |
| 43 | 2009 | 16 | Closing the learning-planning loop with predictive state representations ([link](https://doi.org/10.1177/0278364911404092)) | Byron Boots, S. Siddiqi, and Geoffrey J. Gordon | The International Journal of Robotics Research |
| 44 | 2009 |  | Optimally Predictive Causal Inference ([link](https://www.semanticscholar.org/paper/f1d54e3e5bc4330d6c8a52b3d261eef31781dfde)) | Susanne Still |  |
| 45 | 2017 | 4.5 | Thermodynamic Cost and Benefit of Memory. ([link](https://doi.org/10.1103/PhysRevLett.124.050601)) | Susanne Still | Physical review letters |
| 46 | 2012 | 16 | An information-theoretic approach to curiosity-driven reinforcement learning ([link](https://doi.org/10.1007/s12064-011-0142-z)) | Susanne Still and Doina Precup | Theory in Biosciences |
| 47 | 2014 | 3.3 | Informational and Causal Architecture of Discrete-Time Renewal Processes ([link](https://doi.org/10.3390/e17074891)) | Sarah E. Marzen and J. Crutchfield | Entropy |
| 48 | 2016 | 3.2 | Informational and Causal Architecture of Continuous-time Renewal Processes ([link](https://doi.org/10.1007/s10955-017-1793-z)) | Sarah E. Marzen and J. Crutchfield | Journal of Statistical Physics |
| 49 | 2017 | 3.0 | Structure and Randomness of Continuous-Time, Discrete-Event Processes ([link](https://doi.org/10.1007/s10955-017-1859-y)) | Sarah E. Marzen and J. Crutchfield | Journal of Statistical Physics |
| 50 | 2019 | 9.4 | State Abstraction as Compression in Apprenticeship Learning ([link](https://doi.org/10.1609/AAAI.V33I01.33013134)) | David Abel et al. | AAAI Conference on Artificial Intelligence |
| 51 | 2021 | 5.4 | Deciding What to Learn: A Rate-Distortion Approach ([link](https://www.semanticscholar.org/paper/59e1f4e89f1a0fde5ecc9edee63a03159089c372)) | Dilip Arumugam and Benjamin Van Roy | International Conference on Machine Learning |
| 52 | 2022 | 2.0 | On Rate-Distortion Theory in Capacity-Limited Cognition & Reinforcement Learning ([link](https://doi.org/10.48550/arXiv.2210.16877)) | Dilip Arumugam, Mark K. Ho, Noah D. Goodman, and Benjamin Van Roy | ArXiv |
| 53 | 2022 | 0.3 | Between Rate-Distortion Theory & Value Equivalence in Model-Based Reinforcement Learning ([link](https://doi.org/10.48550/arXiv.2206.02025)) | Dilip Arumugam and Benjamin Van Roy | ArXiv |
| 54 | 2022 | 5.1 | Deciding What to Model: Value-Equivalent Sampling for Reinforcement Learning ([link](https://doi.org/10.48550/arXiv.2206.02072)) | Dilip Arumugam and Benjamin Van Roy | ArXiv |
| 55 | 2016 | 1.8 | Minimum-information LQG control part I: Memoryless controllers ([link](https://doi.org/10.1109/CDC.2016.7799131)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 56 | 2016 | 1.3 | Minimum-information LQG control Part II: Retentive controllers ([link](https://doi.org/10.1109/CDC.2016.7799130)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 57 | 2015 | 11 | LQG Control With Minimum Directed Information: Semidefinite Programming Approach ([link](https://doi.org/10.1109/TAC.2017.2709618)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | IEEE Transactions on Automatic Control |
| 58 | 2015 | 1.1 | LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | ArXiv |
| 59 | 2017 | 1.7 | Transfer-Entropy-Regularized Markov Decision Processes ([link](https://doi.org/10.1109/TAC.2021.3069347)) | Takashi Tanaka, H. Sandberg, and M. Skoglund | IEEE Transactions on Automatic Control |
| 60 | 2001 | 8.3 | Information-theoretic approach to the study of control systems ([link](https://doi.org/10.1016/j.physa.2003.09.007)) | H. Touchette and S. Lloyd | Physica A-statistical Mechanics and Its Applications |
| 61 | 1990 | 21 | CAUSALITY, FEEDBACK AND DIRECTED INFORMATION ([link](https://www.semanticscholar.org/paper/557668619327081a6b77aa5b181fa84722a875a4)) | J. Massey |  |
| 62 | 1998 | 13 | Directed information for channels with feedback ([link](https://doi.org/10.3929/ETHZ-A-001988524)) | G. Kramer |  |
| 63 | 2006 | 14 | The Capacity of Channels With Feedback ([link](https://doi.org/10.1109/TIT.2008.2008147)) | S. Tatikonda and S. Mitter | IEEE Transactions on Information Theory |
| 64 | 2009 |  | 6WRFKDVWLF&RQWURORYHU)LQLWH&DSDFLW&KDQQHOV ([link](https://www.semanticscholar.org/paper/46ac552a420e2b304b159b5982717fed8b1a6f32)) | C. Charalambous, C. Kourtellaris, and Photios A. Stavrou |  |
| 65 | 2011 | 1.0 | Information-Theoretic Viewpoints on Optimal Causal Coding-Decoding Problems ([link](https://www.semanticscholar.org/paper/5ce6a2a8e2bd47e3a1665bf2ddac06e441facd25)) | Siva K. Gorantla and T. Coleman | ArXiv |
| 66 | 2018 | 1.7 | Task-Driven Estimation and Control via Information Bottlenecks ([link](https://doi.org/10.1109/ICRA.2019.8794213)) | Vincent Pacelli and Anirudha Majumdar | 2019 International Conference on Robotics and Automation (ICRA) |
| 67 | 2019 | 1.7 | Estimating Predictive Rate–Distortion Curves via Neural Variational Inference ([link](https://doi.org/10.3390/e21070640)) | Michael Hahn and Richard Futrell | Entropy |
| 68 | 2020 | 3.0 | Optimal prediction with resource constraints using the information bottleneck ([link](https://doi.org/10.1101/2020.04.29.069179)) | V. Sachdeva, T. Mora, A. Walczak, and S. Palmer | PLoS Computational Biology |
| 69 | 2014 | 1.9 | Optimal high-level descriptions of dynamical systems ([link](https://www.semanticscholar.org/paper/ba13d49c5b1c2a274b585094ea89c9a4e74ba5cb)) | D. Wolpert, Joshua A. Grochow, E. Libby, and S. Dedeo | arXiv: Information Theory |
| 70 | 2006 |  | Information Theoretic Approaches for Predictive Models : Results and Analysis ([link](https://www.semanticscholar.org/paper/bf26c1807af780d66b0a18931d6e0378f33a5155)) | Monica Dinculescu and Doina Precup |  |
| 71 | 2007 | 1.1 | Policy-Gradients for PSRs and POMDPs ([link](https://www.semanticscholar.org/paper/d365b66fe8afc73e93efd25912564c00aef7b9a2)) | Douglas Aberdeen, O. Buffet, and Owen Thomas | International Conference on Artificial Intelligence and Statistics |
| 72 | 2008 | 2.6 | On Near Optimality of the Set of Finite-State Controllers for Average Cost POMDP ([link](https://doi.org/10.1287/moor.1070.0279)) | Huizhen Yu and D. Bertsekas | Math. Oper. Res. |
| 73 | 2022 |  | Near Optimality of Finite Memory Policies for POMPDs with Continuous Spaces ([link](https://doi.org/10.1109/CDC51059.2022.9993165)) | A. D. Kara, Erhan Bayraktar, and S. Yüksel | 2022 IEEE 61st Conference on Decision and Control (CDC) |
| 74 | 2023 | 2.7 | Another Look at Partially Observed Optimal Stochastic Control: Existence, Ergodicity, and Approximations Without Belief-Reduction ([link](https://doi.org/10.1007/s00245-024-10211-9)) | S. Yüksel | Applied Mathematics & Optimization |
| 75 | 2024 | 6.7 | Agent-state based policies in POMDPs: Beyond belief-state MDPs ([link](https://doi.org/10.1109/CDC56724.2024.10886046)) | Amit Sinha and Aditya Mahajan | 2024 IEEE 63rd Conference on Decision and Control (CDC) |
| 76 | 2024 | 6.5 | Active Inference as a Model of Agency ([link](https://doi.org/10.48550/arXiv.2401.12917)) | Lancelot Da Costa, Samuel Tenka, Dominic Zhao, and Noor Sajid | ArXiv |
| 77 | 2012 | 0.9 | Free Energy and the Generalized Optimality Equations for Sequential Decision Making ([link](https://www.semanticscholar.org/paper/8141b978fa4600f4e4dd0f2d7a363da48f62dd08)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 78 | 2012 | 0.2 | Adaptive Coding of Actions and Observations ([link](https://www.semanticscholar.org/paper/70a76ed83473afa7f8a491dceb05ca2209234a31)) | Pedro A. Ortega and Daniel A. Braun | Neural Information Processing Systems |
| 79 | 2003 | 1.8 | On competitive prediction and its relation to rate-distortion theory ([link](https://doi.org/10.1109/TIT.2003.820014)) | T. Weissman and N. Merhav | IEEE Trans. Inf. Theory |
| 80 | 1975 | 1.2 | Process definitions of distortion-rate functions and source coding theorems ([link](https://doi.org/10.1109/TIT.1975.1055440)) | R. Gray, D. Neuhoff, and J. Omura | IEEE Trans. Inf. Theory |
| 81 | 2012 | 0.1 | Causal Rate Distortion Function on Abstract Alphabets: Optimal Reconstruction and Properties ([link](https://www.semanticscholar.org/paper/e9f76edcca3ab5028938e90f96ad9002adbe4545)) | Photios A. Stavrou, C. Charalambous, and C. Kourtellaris | ArXiv |
| 82 | 2011 | 0.1 | Causal Rate Distortion Function on Abstract Alphabets and Optimal Reconstruction Kernel ([link](https://www.semanticscholar.org/paper/a6394b7105208888955fed22ca86133e520737be)) | C. Charalambous, Photios A. Stavrou, and C. Kourtellaris | ArXiv |
| 83 | 2006 |  | On Causal Coding of Markovian Sources with General Alphabets ([link](https://www.semanticscholar.org/paper/15b863c0c1a2120b0c332afa33011f5807e368e1)) | Manchester Grand Hyatt Hotel |  |
| 84 | 2008 | 10 | Predictive information and explorative behavior of autonomous robots ([link](https://doi.org/10.1140/EPJB/E2008-00175-0)) | N. Ay et al. | The European Physical Journal B |
| 85 | 2010 | 46 | Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy ([link](https://doi.org/10.1184/R1/6720692.V1)) | Brian D. Ziebart |  |
| 86 | 2024 | 1.5 | Resource-rational reinforcement learning and sensorimotor causal states, and resource-rational maximiners ([link](https://doi.org/10.1098/rsfs.2024.0062)) | Sarah Marzen | Interface Focus |
| 87 | 2022 | 9.1 | Guaranteed Discovery of Control-Endogenous Latent States with Multi-Step Inverse Models ([link](https://www.semanticscholar.org/paper/df2499f13dd98d4ce7a46888834084798c9930e4)) | Alex Lamb et al. | Trans. Mach. Learn. Res. |
| 88 | 2014 |  | Compressed Predictive State Representation: An Efficient Moment-Method for Sequence Prediction and Sequential Decision-Making ([link](https://www.semanticscholar.org/paper/ddadadef3eb26a19a8ba18f89a0084bbb40048f5)) | William L. Hamilton |  |
| 89 | 2022 | 12 | PAC Reinforcement Learning for Predictive State Representations ([link](https://doi.org/10.48550/arXiv.2207.05738)) | Wenhao Zhan, Masatoshi Uehara, Wen Sun, and Jason D. Lee | ArXiv |

### Paper Details

1\. · 100% match · 2000 · 165 cit/yr\
**The information bottleneck method** ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c))\
Naftali Tishby, Fernando C Pereira, and W. Bialek\
*ArXiv* · Apr 24, 2000 · 4311 citations

> We define the relevant information in a signal $`x\in X`$ as being the information that this signal provides about another signal $`y\in \Y`$. Examples include the information that face images provide about the names of the people portrayed, or the information that speech sounds provide about the words spoken. Understanding the signal $`x`$ requires more than just predicting $`y`$, it also requires specifying which features of $`\X`$ play a role in the prediction. We formalize this problem as that of finding a short code for $`\X`$ that preserves the maximum information about $`\Y`$. That is, we squeeze the information that $`\X`$ provides about $`\Y`$ through a \`bottleneck’ formed by a limited set of codewords $`\tX`$. This constrained optimization problem can be seen as a generalization of rate distortion theory in which the distortion measure $`d(x,\x)`$ emerges from the joint statistics of $`\X`$ and $`\Y`$. This approach yields an exact set of self consistent equations for the coding rules $`X \to \tX`$ and $`\tX \to \Y`$. Solutions to these equations can be found by a convergent re-estimation method that generalizes the Blahut-Arimoto algorithm. Our variational principle provides a surprisingly rich framework for discussing a variety of problems in signal processing and learning, as will be described in detail elsewhere.

------------------------------------------------------------------------

2\. · 100% match · 1999 · 19 cit/yr\
**Computational Mechanics: Pattern and Prediction, Structure and Simplicity** ([link](https://doi.org/10.1023/A:1010388907793))\
C. Shalizi and J. Crutchfield\
*Journal of Statistical Physics* · Jul 1, 1999 · 523 citations

> Computational mechanics, an approach to structural complexity, defines a process’s causal states and gives a procedure for finding them. We show that the causal-state representation—an ∈-machine—is the minimal one consistent with accurate prediction. We establish several results on ∈-machine optimality and uniqueness and on how ∈-machines compare to alternative representations. Further results relate measures of randomness and structural complexity obtained from ∈-machines to those from ergodic and information theories.

------------------------------------------------------------------------

3\. · 100% match · 2009 · 5.2 cit/yr\
**Past-future information bottleneck in dynamical systems.** ([link](https://doi.org/10.1103/PHYSREVE.79.041925))\
F. Creutzig, A. Globerson, and Naftali Tishby\
*Physical review. E, Statistical, nonlinear, and soft matter physics* · Apr 27, 2009 · 88 citations

> Biological systems need to process information in real time and must trade off accuracy of presentation and coding costs. Here we operationalize this trade-off and develop an information-theoretic framework that selectively extracts information of the input past that is predictive about the output future, obtaining a generalized eigenvalue problem. Thereby, we unravel the input history in terms of structural phase transitions corresponding to additional dimensions of a state space. We elucidate the relation to canonical correlation analysis and give a numerical example. Altogether, this work relates information-theoretic optimization to the joint problem of system identification and model reduction.

------------------------------------------------------------------------

4\. · 100% match · 2014 · 0.9 cit/yr\
**Circumventing the Curse of Dimensionality in Prediction: Causal Rate-Distortion for Infinite-Order Markov Processes** ([link](https://www.semanticscholar.org/paper/5308a461868cde8b8d175eee0de4eea699028d14))\
Sarah E. Marzen and J. Crutchfield\
*ArXiv* · Dec 8, 2014 · 10 citations

> Author(s): Marzen, Sarah; Crutchfield, James P \| Abstract: Predictive rate-distortion analysis suffers from the curse of dimensionality: clustering arbitrarily long pasts to retain information about arbitrarily long futures requires resources that typically grow exponentially with length. The challenge is compounded for infinite-order Markov processes, since conditioning on finite sequences cannot capture all of their past dependencies. Spectral arguments show that algorithms which cluster finite-length sequences fail dramatically when the underlying process has long-range temporal correlations and can fail even for processes generated by finite-memory hidden Markov models. We circumvent the curse of dimensionality in rate-distortion analysis of infinite-order processes by casting predictive rate-distortion objective functions in terms of the forward- and reverse-time causal states of computational mechanics. Examples demonstrate that the resulting causal rate-distortion theory substantially improves current predictive rate-distortion analyses.

------------------------------------------------------------------------

5\. · 100% match · 2016 · 3.5 cit/yr\
**Predictive Rate-Distortion for Infinite-Order Markov Processes** ([link](https://doi.org/10.1007/s10955-016-1520-1))\
Sarah E. Marzen and J. Crutchfield\
*Journal of Statistical Physics* · May 3, 2016 · 35 citations

------------------------------------------------------------------------

6\. · 100% match · 2000 · 1.4 cit/yr\
**Information Bottlenecks, Causal States, and Statistical Relevance Bases: How to Represent Relevant Information in memoryless transduction** ([link](https://doi.org/10.1142/S0219525902000481))\
C. Shalizi and J. Crutchfield\
*Adv. Complex Syst.* · Jun 16, 2000 · 36 citations

> Discovering relevant, but possibly hidden, variables is a key step in constructing useful and predictive theories about the natural world. This brief note explains the connections between three approaches to this problem: the recently introduced information-bottleneck method, the computational mechanics approach to inferring optimal models, and Salmon’s statistical relevance basis.

------------------------------------------------------------------------

7\. · 100% match · 2014 · 5.1 cit/yr\
**Information Bottleneck Approach to Predictive Inference** ([link](https://doi.org/10.3390/e16020968))\
Susanne Still\
*Entropy* · Feb 17, 2014 · 62 citations

> This paper synthesizes a recent line of work on automated predictive model making inspired by Rate-Distortion theory, in particular by the Information Bottleneck method. Predictive inference is interpreted as a strategy for efficient communication. The relationship to thermodynamic efficiency is discussed. The overall aim of this paper is to explain how this information theoretic approach provides an intuitive, overarching framework for predictive inference.

------------------------------------------------------------------------

8\. · 100% match · 2000 · 8.4 cit/yr\
**Predictability, Complexity, and Learning** ([link](https://doi.org/10.1162/089976601753195969))\
W. Bialek, I. Nemenman, and Naftali Tishby\
*Neural Computation* · Jul 19, 2000 · 216 citations

> We define predictive information Ipred(T) as the mutual information between the past and the future of a time series. Three qualitatively different behaviors are found in the limit of large observation times T: Ipred(T) can remain finite, grow logarithmically, or grow as a fractional power law. If the time series allows us to learn a model with a finite number of parameters, then Ipred(T) grows logarithmically with a coefficient that counts the dimensionality of the model space. In contrast, power-law growth is associated, for example, with the learning of infinite parameter (or non-parametric) models such as continuous functions with smoothness constraints. There are connections between the predictive information and measures of complexity that have been defined both in learning theory and the analysis of physical systems through statistical mechanics and dynamical systems theory. Furthermore, in the same way that entropy provides the unique measure of available information consistent with some simple and plausible conditions, we argue that the divergent part of Ipred(T) provides the unique measure for the complexity of dynamics underlying a time series. Finally, we discuss how these ideas may be useful in problems in physics, statistics, and biology.

------------------------------------------------------------------------

9\. · 100% match · 2001 · 24 cit/yr\
**Predictive Representations of State** ([link](https://www.semanticscholar.org/paper/4a7de0669fd835b2efcab97c7d3dc28ea7a1e6a3))\
M. Littman, R. Sutton, and Satinder Singh\
*Neural Information Processing Systems* · Jan 3, 2001 · 600 citations

> We show that states of a dynamical system can be usefully represented by multi-step, action-conditional predictions of future observations. State representations that are grounded in data in this way may be easier to learn, generalize better, and be less dependent on accurate prior models than, for example, POMDP state representations. Building on prior work by Jaeger and by Rivest and Schapire, in this paper we compare and contrast a linear specialization of the predictive approach with the state representations used in POMDPs and in k-order Markov models. Ours is the first specific formulation of the predictive idea that includes both stochasticity and actions (controls). We show that any system has a linear predictive state representation with number of predictions no greater than the number of states in its minimal POMDP model.

------------------------------------------------------------------------

10\. · 100% match · 2004 · 14 cit/yr\
**Predictive State Representations: A New Theory for Modeling Dynamical Systems** ([link](https://www.semanticscholar.org/paper/532c61a2af5cde64628d0cdd2ba0823800118d0f))\
Satinder Singh, Michael R. James, and Matthew R. Rudary\
*Conference on Uncertainty in Artificial Intelligence* · Jul 7, 2004 · 298 citations

> Modeling dynamical systems, both for control purposes and to make predictions about their behavior, is ubiquitous in science and engineering. Predictive state representations (PSRs) are a recently introduced class of models for discrete-time dynamical systems. The key idea behind PSRs and the closely related OOMs (Jaeger’s observable operator models) is to represent the state of the system as a set of predictions of observable outcomes of experiments one can do in the system. This makes PSRs rather different from history-based models such as nth-order Markov models and hidden-state-based models such as HMMs and POMDPs. We introduce an interesting construct, the system-dynamics matrix, and show how PSRs can be derived simply from it. We also use this construct to show formally that PSRs are more general than both nth-order Markov models and HMMs/POMDPs. Finally, we discuss the main difference between PSRs and OOMs and conclude with directions for future work.

------------------------------------------------------------------------

11\. · 100% match · 2020 · 20 cit/yr\
**Approximate information state for approximate planning and reinforcement learning in partially observed systems** ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980))\
Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan\
*ArXiv* · Oct 17, 2020 · 112 citations

> We propose a theoretical framework for approximate planning and learning in partially observed systems. Our framework is based on the fundamental notion of information state. We provide two equivalent definitions of information state—i) a function of history which is sufficient to compute the expected reward and predict its next value; ii) equivalently, a function of the history which can be recursively updated and is sufficient to compute the expected reward and predict the next observation. An information state always leads to a dynamic programming decomposition. Our key result is to show that if a function of the history (called approximate information state (AIS)) approximately satisfies the properties of the information state, then there is a corresponding approximate dynamic program. We show that the policy computed using this is approximately optimal with bounded loss of optimality. We show that several approximations in state, observation and action spaces in literature can be viewed as instances of AIS. In some of these cases, we obtain tighter bounds. A salient feature of AIS is that it can be learnt from data. We present AIS based multi-time scale policy gradient algorithms. and detailed numerical experiments with low, moderate and high dimensional environments.

------------------------------------------------------------------------

12\. · 100% match · 2012 · 21 cit/yr\
**A Free Energy Principle for Biological Systems.** ([link](https://doi.org/10.3390/E14112100))\
Karl J. Friston\
*Entropy* · Oct 31, 2012 · 285 citations

> This paper describes a free energy principle that tries to explain the ability of biological systems to resist a natural tendency to disorder. It appeals to circular causality of the sort found in synergetic formulations of self-organization (e.g., the slaving principle) and models of coupled dynamical systems, using nonlinear Fokker Planck equations. Here, circular causality is induced by separating the states of a random dynamical system into external and internal states, where external states are subject to random fluctuations and internal states are not. This reduces the problem to finding some (deterministic) dynamics of the internal states that ensure the system visits a limited number of external states; in other words, the measure of its (random) attracting set, or the Shannon entropy of the external states is small. We motivate a solution using a principle of least action based on variational free energy (from statistical physics) and establish the conditions under which it is formally equivalent to the information bottleneck method. This approach has proved useful in understanding the functional architecture of the brain. The generality of variational free energy minimisation and corresponding information theoretic formulations may speak to interesting applications beyond the neurosciences; e.g., in molecular or evolutionary biology.

------------------------------------------------------------------------

13\. · 100% match · 2012 · 16 cit/yr\
**Active inference and agency: optimal control without cost functions** ([link](https://doi.org/10.1007/s00422-012-0512-8))\
Karl J. Friston, Spyridon Samothrakis, and P. Montague\
*Biological Cybernetics* · Oct 1, 2012 · 223 citations

> This paper describes a variational free-energy formulation of (partially observable) Markov decision problems in decision making under uncertainty. We show that optimal control can be cast as active inference. In active inference, both action and posterior beliefs about hidden states minimise a free energy bound on the negative log-likelihood of observed states, under a generative model. In this setting, reward or cost functions are absorbed into prior beliefs about state transitions and terminal states. Effectively, this converts optimal control into a pure inference problem, enabling the application of standard Bayesian filtering techniques. We then consider optimal trajectories that rest on posterior beliefs about hidden states in the future. Crucially, this entails modelling control as a hidden state that endows the generative model with a representation of agency. This leads to a distinction between models with and without inference on hidden control states; namely, agency-free and agency-based models, respectively.

------------------------------------------------------------------------

14\. · 100% match · 2010 · 45 cit/yr\
**Action and behavior: a free-energy formulation** ([link](https://doi.org/10.1007/s00422-010-0364-z))\
Karl J. Friston, J. Daunizeau, J. Kilner, and S. Kiebel\
*Biological Cybernetics* · Mar 1, 2010 · 734 citations

> We have previously tried to explain perceptual inference and learning under a free-energy principle that pursues Helmholtz’s agenda to understand the brain in terms of energy minimization. It is fairly easy to show that making inferences about the causes of sensory data can be cast as the minimization of a free-energy bound on the likelihood of sensory inputs, given an internal model of how they were caused. In this article, we consider what would happen if the data themselves were sampled to minimize this bound. It transpires that the ensuing active sampling or inference is mandated by ergodic arguments based on the very existence of adaptive agents. Furthermore, it accounts for many aspects of motor behavior; from retinal stabilization to goal-seeking. In particular, it suggests that motor control can be understood as fulfilling prior expectations about proprioceptive sensations. This formulation can explain why adaptive behavior emerges in biological agents and suggests a simple alternative to optimal control theory. We illustrate these points using simulations of oculomotor control and then apply to same principles to cued and goal-directed movements. In short, the free-energy formulation may provide an alternative perspective on the motor control that places it in an intimate relationship with perception.

------------------------------------------------------------------------

15\. · 100% match · 2018 · 29 cit/yr\
**Generalised free energy and active inference** ([link](https://doi.org/10.1007/s00422-019-00805-w))\
Thomas Parr and Karl J. Friston\
*Biological Cybernetics* · Apr 23, 2018 · 235 citations

> Active inference is an approach to understanding behaviour that rests upon the idea that the brain uses an internal generative model to predict incoming sensory data. The fit between this model and data may be improved in two ways. The brain could optimise probabilistic beliefs about the variables in the generative model (i.e. perceptual inference). Alternatively, by acting on the world, it could change the sensory data, such that they are more consistent with the model. This implies a common objective function (variational free energy) for action and perception that scores the fit between an internal model and the world. We compare two free energy functionals for active inference in the framework of Markov decision processes. One of these is a functional of beliefs (i.e. probability distributions) about states and policies, but a function of observations, while the second is a functional of beliefs about all three. In the former (expected free energy), prior beliefs about outcomes are not part of the generative model (because they are absorbed into the prior over policies). Conversely, in the second (generalised free energy), priors over outcomes become an explicit component of the generative model. When using the free energy function, which is blind to future observations, we equip the generative model with a prior over policies that ensure preferred (i.e. priors over) outcomes are realised. In other words, if we expect to encounter a particular kind of outcome, this lends plausibility to those policies for which this outcome is a consequence. In addition, this formulation ensures that selected policies minimise uncertainty about future outcomes by minimising the free energy expected in the future. When using the free energy functional—that effectively treats future observations as hidden states—we show that policies are inferred or selected that realise prior preferences by minimising the free energy of future expectations. Interestingly, the form of posterior beliefs about policies (and associated belief updating) turns out to be identical under both formulations, but the quantities used to compute them are not.

------------------------------------------------------------------------

16\. · 100% match · 2011 · 20 cit/yr\
**Information Theory of Decisions and Actions** ([link](https://doi.org/10.1007/978-1-4419-1452-1_19))\
Naftali Tishby and D. Polani\
314 citations

------------------------------------------------------------------------

17\. · 100% match · 2007 · 4.5 cit/yr\
**Information-theoretic approach to interactive learning** ([link](https://doi.org/10.1209/0295-5075/85/28005))\
Susanne Still\
*EPL (Europhysics Letters)* · Sep 12, 2007 · 84 citations

> The principles of statistical mechanics and information theory play an important role in learning and have inspired both theory and the design of numerous machine learning algorithms. The new aspect in this paper is a focus on integrating feedback from the learner. A quantitative approach to interactive learning and adaptive behavior is proposed, integrating model- and decision-making into one theoretical framework. This paper follows simple principles by requiring that the observer’s world model and action policy should result in maximal predictive power at minimal complexity. Classes of optimal action policies and of optimal models are derived from an objective function that reflects this trade-off between prediction and complexity. The resulting optimal models then summarize, at different levels of abstraction, the process’s causal organization in the presence of the learner’s actions. A fundamental consequence of the proposed principle is that the learner’s optimal action policies balance exploration and control as an emerging property. Interestingly, the explorative component is present in the absence of policy randomness, i.e. in the optimal deterministic behavior. This is a direct result of requiring maximal predictive power in the presence of feedback.

------------------------------------------------------------------------

18\. · 100% match · 2007 · 0.6 cit/yr\
**Optimal Causal Inference** ([link](https://www.semanticscholar.org/paper/0c8c8cd4275c7f3505ba0250d7f1be54842d9440))\
Susanne Still, J. Crutchfield, and C. J. Ellison\
*ArXiv* · Aug 11, 2007 · 11 citations

> We consider an information-theoretic objective function for statistical modeling of time series that embodies a parametrized trade-off between the predictive power of a model and the model’s complexity. We study two distinct cases of optimal causal inference, which we call optimal causal filtering (OCF) and optimal causal estimation (OCE). OCF corresponds to the ideal case of having infinite data. We show that OCF leads to the exact causal architecture of a stochastic process, in the limit in which the trade-off parameter tends to zero, thereby emphasizing prediction. Specifically, the filtering method reconstructs exactly the hidden, causal states. More generally, we establish that the method leads to a graded model-complexity hierarchy of approximations to the causal architecture. We show for nonideal cases with finite data (OCE) that the correct number of states can be found by adjusting for statistical fluctuations in probability estimates.

------------------------------------------------------------------------

19\. · 100% match · 2012 · 18 cit/yr\
**The thermodynamics of prediction** ([link](https://doi.org/10.1103/PhysRevLett.109.120604))\
Susanne Still, David A. Sivak, A. Bell, and G. Crooks\
*Physical review letters* · Mar 15, 2012 · 250 citations

> A system responding to a stochastic driving signal can be interpreted as computing, by means of its dynamics, an implicit model of the environmental variables. The system’s state retains information about past environmental fluctuations, and a fraction of this information is predictive of future ones. The remaining nonpredictive information reflects model complexity that does not improve predictive power, and thus represents the ineffectiveness of the model. We expose the fundamental equivalence between this model inefficiency and thermodynamic inefficiency, measured by dissipation. Our results hold arbitrarily far from thermodynamic equilibrium and are applicable to a wide range of systems, including biomolecular machines. They highlight a profound connection between the effective use of information and efficient thermodynamic operation: any system constructed to keep memory about its environment and to operate with maximal energetic efficiency has to be predictive.

------------------------------------------------------------------------

20\. · 100% match · 1989 · 26 cit/yr\
**Inferring statistical complexity.** ([link](https://doi.org/10.1103/PHYSREVLETT.63.105))\
J. Crutchfield and K. Young\
*Physical review letters* · Jul 10, 1989 · 973 citations

> Statistical mechanics is used to describe the observed information processing complexity of nonlinear dynamical systems. We introduce a measure of complexity distinct from and dual to the information theoretic entropies and dimensions. A technique is presented that directly reconstructs minimal equations of motion from the recursive structure of measurement sequences. Application to the period-doubling cascade demonstrates a form of superuniversality that refers only to the entropy and complexity of a data stream.

------------------------------------------------------------------------

21\. · 100% match · 1965 · 15 cit/yr\
**Optimal control of Markov processes with incomplete state information** ([link](https://doi.org/10.1016/0022-247X(65%2990154-X))\
K. Åström\
*Journal of Mathematical Analysis and Applications* · Feb 1, 1965 · 930 citations

------------------------------------------------------------------------

22\. · 100% match · 1965 · 3.3 cit/yr\
**Sufficient statistics in the optimum control of stochastic systems** ([link](https://doi.org/10.1016/0022-247X(65%2990027-2))\
C. Striebel\
*Journal of Mathematical Analysis and Applications* · Dec 1, 1965 · 200 citations

------------------------------------------------------------------------

23\. · 100% match · 2013 · 3.4 cit/yr\
**Efficient learning and planning with compressed predictive states** ([link](https://doi.org/10.5555/2627435.2750354))\
William L. Hamilton, M. M. Fard, and Joelle Pineau\
*J. Mach. Learn. Res.* · Dec 1, 2013 · 43 citations

> Predictive state representations (PSRs) offer an expressive framework for modelling partially observable systems. By compactly representing systems as functions of observable quantities, the PSR learning approach avoids using local-minima prone expectation-maximization and instead employs a globally optimal moment-based algorithm. Moreover, since PSRs do not require a predetermined latent state structure as an input, they offer an attractive framework for model-based reinforcement learning when agents must plan without a priori access to a system model. Unfortunately, the expressiveness of PSRs comes with significant computational cost, and this cost is a major factor inhibiting the use of PSRs in applications. In order to alleviate this shortcoming, we introduce the notion of compressed PSRs (CPSRs). The CPSR learning approach combines recent advancements in dimensionality reduction, incremental matrix decomposition, and compressed sensing. We show how this approach provides a principled avenue for learning accurate approximations of PSRs, drastically reducing the computational costs associated with learning while also providing effective regularization. Going further, we propose a planning framework which exploits these learned models. And we show that this approach facilitates model-learning and planning in large complex partially observable domains, a task that is infeasible without the principled use of compression.

------------------------------------------------------------------------

24\. · 100% match · 2010 · 3.1 cit/yr\
**Predictive State Temporal Difference Learning** ([link](https://www.semanticscholar.org/paper/c3e84987d911a2f3a02cd32f30507ca7169f1b0c))\
Byron Boots and Geoffrey J. Gordon\
*Neural Information Processing Systems* · Oct 29, 2010 · 49 citations

> We propose a new approach to value function approximation which combines linear temporal difference reinforcement learning with subspace identification. In practical applications, reinforcement learning (RL) is complicated by the fact that state is either high-dimensional or partially observable. Therefore, RL methods are designed to work with features of state rather than state itself, and the success or failure of learning is often determined by the suitability of the selected features. By comparison, subspace identification (SSID) methods are designed to select a feature set which preserves as much information as possible about state. In this paper we connect the two approaches, looking at the problem of reinforcement learning with a large set of features, each of which may only be marginally useful for value function approximation. We introduce a new algorithm for this situation, called Predictive State Temporal Difference (PSTD) learning. As in SSID for predictive state representations, PSTD finds a linear compression operator that projects a large set of features down to a small set that preserves the maximum amount of predictive information. As in RL, PSTD then uses a Bellman recursion to estimate a value function. We discuss the connection between PSTD and prior approaches in RL and SSID. We prove that PSTD is statistically consistent, perform several experiments that illustrate its properties, and demonstrate its potential on a difficult optimal stopping problem.

------------------------------------------------------------------------

25\. · 100% match · 2015 · 5.5 cit/yr\
**Information-Theoretic Bounded Rationality** ([link](https://www.semanticscholar.org/paper/a5a6611134e82077184a2d3b7a336c75402cdaaf))\
Pedro A. Ortega, Daniel A. Braun, Justin Dyer, Kee-Eung Kim, and Naftali Tishby\
*ArXiv* · Dec 21, 2015 · 57 citations

> Bounded rationality, that is, decision-making and planning under resource limitations, is widely regarded as an important open problem in artificial intelligence, reinforcement learning, computational neuroscience and economics. This paper offers a consolidated presentation of a theory of bounded rationality based on information-theoretic ideas. We provide a conceptual justification for using the free energy functional as the objective function for characterizing bounded-rational decisions. This functional possesses three crucial properties: it controls the size of the solution space; it has Monte Carlo planners that are exact, yet bypass the need for exhaustive search; and it captures model uncertainty arising from lack of evidence or from interacting with other agents having unknown intentions. We discuss the single-step decision-making case, and show how to extend it to sequential decisions using equivalence transformations. This extension yields a very general class of decision problems that encompass classical decision rules (e.g. EXPECTIMAX and MINIMAX) as limit cases, as well as trust- and risk-sensitive planning.

------------------------------------------------------------------------

26\. · 100% match · 2008 · 7.2 cit/yr\
**A Minimum Relative Entropy Principle for Learning and Acting** ([link](https://doi.org/10.1613/JAIR.3062))\
Pedro A. Ortega and Daniel A. Braun\
*ArXiv* · Oct 20, 2008 · 126 citations

> This paper proposes a method to construct an adaptive agent that is universal with respect to a given class of experts, where each expert is designed specifically for a particular environment. This adaptive control problem is formalized as the problem of minimizing the relative entropy of the adaptive agent from the expert that is most suitable for the unknown environment. If the agent is a passive observer, then the optimal solution is the well-known Bayesian predictor. However, if the agent is active, then its past actions need to be treated as causal interventions on the I/O stream rather than normal probability conditions. Here it is shown that the solution to this new variational problem is given by a stochastic controller called the Bayesian control rule, which implements adaptive behavior as a mixture of experts. Furthermore, it is shown that under mild assumptions, the Bayesian control rule converges to the control law of the most suitable expert.

------------------------------------------------------------------------

27\. · 100% match · 2017 · 3.3 cit/yr\
**A Unified Bellman Equation for Causal Information and Value in Markov Decision Processes** ([link](https://www.semanticscholar.org/paper/f5f235579f02d9fad0d18cd19795de7e45c2f8eb))\
Stas Tiomkin and Naftali Tishby\
*ArXiv* · Mar 5, 2017 · 30 citations

> The interaction between an artificial agent and its environment is bi-directional. The agent extracts relevant information from the environment, and affects the environment by its actions in return to accumulate high expected reward. Standard reinforcement learning (RL) deals with the expected reward maximization. However, there are always information-theoretic limitations that restrict the expected reward, which are not properly considered by the standard RL. In this work we consider RL objectives with information-theoretic limitations. For the first time we derive a Bellman-type recursive equa- tion for the causal information between the environment and the agent, which is combined plausibly with the Bellman recursion for the value function. The unified equitation serves to explore the typical behavior of artificial agents in an infinite time horizon.

------------------------------------------------------------------------

28\. · 100% match · 1999 · 2.0 cit/yr\
**Predictive Information** ([link](https://www.semanticscholar.org/paper/3068a485e76bc6e7d274aa8e7b68ccb979a39a3d))\
W. Bialek and Naftali Tishby\
Feb 25, 1999 · 54 citations

> Observations on the past provide some hints about what will happen in the future, and this can be quantified using information theory. The \`\`predictive information’’ defined in this way has connections to measures of complexity that have been proposed both in the study of dynamical systems and in mathematical statistics. In particular, the predictive information diverges when the observed data stream allows us to learn an increasingly precise model for the dynamics that generate the data, and the structure of this divergence measures the complexity of the model. We argue that divergent contributions to the predictive information provide the only measure of complexity or richness that is consistent with certain plausible requirements.

------------------------------------------------------------------------

29\. · 98% match · 2019 · 5.4 cit/yr\
**Approximate information state for partially observed systems** ([link](https://doi.org/10.1109/CDC40024.2019.9029898))\
Jayakumar Subramanian and Aditya Mahajan\
*2019 IEEE 58th Conference on Decision and Control (CDC)* · Dec 1, 2019 · 35 citations

> The standard approach for modeling partially observed systems is to model them as partially observable Markov decision processes (POMDPs) and obtain a dynamic program in terms of a belief state. The belief state formulation works well for planning but is not ideal for online reinforcement learning because the belief state depends on the model and, as such, is not observable when the model is unknown.In this paper, we present an alternative notion of an information state for obtaining a dynamic program in partially observed models. In particular, an information state is a sufficient statistic for the current reward which evolves in a controlled Markov manner. We show that such an information state leads to a dynamic programming decomposition. Then we present a notion of an approximate information state and present an approximate dynamic program based on the approximate information state. Approximate information state is defined in terms of properties that can be estimated using sampled trajectories. Therefore, they provide a constructive method for reinforcement learning in partially observed systems. We present one such construction and show that it performs better than the state of the art for three benchmark models.

------------------------------------------------------------------------

30\. · 94% match · 2020 · 8.6 cit/yr\
**Near Optimality of Finite Memory Feedback Policies in Partially Observed Markov Decision Processes** ([link](https://www.semanticscholar.org/paper/337566d4f14e00e32cfba465ae6a50a1e07404ca))\
A. D. Kara and S. Yüksel\
*J. Mach. Learn. Res.* · Oct 15, 2020 · 48 citations

> In the theory of Partially Observed Markov Decision Processes (POMDPs), existence of optimal policies have in general been established via converting the original partially observed stochastic control problem to a fully observed one on the belief space, leading to a belief-MDP. However, computing an optimal policy for this fully observed model, and so for the original POMDP, using classical dynamic or linear programming methods is challenging even if the original system has finite state and action spaces, since the state space of the fully observed belief-MDP model is always uncountable. Furthermore, there exist very few rigorous approximation results, as regularity conditions needed often require a tedious study involving the spaces of probability measures leading to properties such as Feller continuity. In this paper, we rigorously establish near optimality of finite window control policies in POMDPs under mild non-linear filter stability conditions and the assumption that the measurement and action sets are finite (and the state space is real vector valued). We also establish a rate of convergence result which relates the finite window memory size and the approximation error bound, where the rate of convergence is exponential under explicit and testable geometric filter stability conditions. While there exist many experimental results and few rigorous asymptotic convergence results, an explicit rate of convergence result is new in the literature, to our knowledge.

------------------------------------------------------------------------

31\. · 92% match · 2002 · 1.8 cit/yr\
**Pattern Discovery in Time Series, Part I: Theory, Algorithm, Analysis, and Convergence** ([link](https://www.semanticscholar.org/paper/d3345b5eae4c0060505af5421edace8d99405244))\
C. Shalizi, Kristina Lisa Shalizi, and James P. Crutchfleld\
Oct 29, 2002 · 43 citations

> We present a new algorithm for discovering patterns in time series and other sequential data. We exhibit a reliable procedure for building the minimal set of hidden, Markovian states that is statistically capable of producing the behavior exhibited in the data \| the underlying process’s causal states. Unlike conventional methods for fltting hidden Markov models (HMMs) to data, our algorithm makes no assumptions about the process’s causal architecture (the number of hidden states and their transition structure), but rather infers it from the data. It starts with assumptions of minimal structure and introduces complexity only when the data demand it. Moreover, the causal states it infers have important predictive optimality properties that conventional HMM states lack. Here, in Part I, we introduce the algorithm, review the theory behind it, prove its asymptotic reliability, and use large deviation theory to estimate its rate of convergence. In the sequel, Part II, we outline the algorithm’s implementation, illustrate its ability to discover even \di‐cult” patterns, and compare it to various alternative schemes.

------------------------------------------------------------------------

32\. · 89% match · 2001 · 11 cit/yr\
**Causal architecture, complexity and self-organization in time series and cellular automata** ([link](https://www.semanticscholar.org/paper/1530382baf56cd93d0fe69318efdfe060b4b7179))\
C. Shalizi and M. Olsson\
267 citations

> All self-respecting nonlinear scientists know self-organization when they see it: except when we disagree. For this reason, if no other, it is important to put some mathematical spine into our floppy intuitive notion of self-organization. Only a few measures of self-organization have been proposed; none can be adopted in good intellectual conscience. To find a decent formalization of self-organization, we need to pin down what we mean by organization. The best answer is that the organization of a process is its causal architecture—its internal, possibly hidden, causal states and their interconnections. Computational mechanics is a method for inferring causal architecture—represented by a mathematical object called the e-machine—from observed behavior. The e-machine captures all patterns in the process which have any predictive power, so computational mechanics is also a method for pattern discovery. In this work, I develop computational mechanics for four increasingly sophisticated types of process—memoryless transducers, time series, transducers with memory, and cellular automata. In each case I prove the optimality and uniqueness of the e-machine’s representation of the causal architecture, and give reliable algorithms for pattern discovery. The e-machine is the organization of the process, or at least of the part of it which is relevant to our measurements. It leads to a natural measure of the statistical complexity of processes, namely the amount of information needed to specify the state of the E-machine. Self-organization is a self-generated increase in statistical complexity. This fulfills various hunches which have been advanced in the literature, seems to accord with people’s intuitions, and is both mathematically precise and operational.

------------------------------------------------------------------------

33\. · 87% match · 2009 · 6.9 cit/yr\
**Prediction, Retrodiction, and the Amount of Information Stored in the Present** ([link](https://doi.org/10.1007/s10955-009-9808-z))\
C. J. Ellison, J. Mahoney, and J. Crutchfield\
*Journal of Statistical Physics* · May 22, 2009 · 117 citations

> We introduce an ambidextrous view of stochastic dynamical systems, comparing their forward-time and reverse-time representations and then integrating them into a single time-symmetric representation. The perspective is useful theoretically, computationally, and conceptually. Mathematically, we prove that the excess entropy—a familiar measure of organization in complex systems—is the mutual information not only between the past and future, but also between the predictive and retrodictive causal states. Practically, we exploit the connection between prediction and retrodiction to directly calculate the excess entropy. Conceptually, these lead one to discover new system measures for stochastic dynamical systems: crypticity (information accessibility) and causal irreversibility. Ultimately, we introduce a time-symmetric representation that unifies all of these quantities, compressing the two directional representations into one. The resulting compression offers a new conception of the amount of information stored in the present.

------------------------------------------------------------------------

34\. · 85% match · 2009 · 7.5 cit/yr\
**Time’s barbed arrow: irreversibility, crypticity, and stored information.** ([link](https://doi.org/10.1103/PhysRevLett.103.094101))\
J. Crutchfield, C. J. Ellison, and J. Mahoney\
*Physical review letters* · Feb 7, 2009 · 129 citations

> We show why the amount of information communicated between the past and future-the excess entropy-is not in general the amount of information stored in the present-the statistical complexity. This is a puzzle, and a long-standing one, since the former describes observed behavior, while optimal prediction requires the latter. We present a closed-form expression for the excess entropy in terms of optimal causal predictors and retrodictors-both machines of computational mechanics. This leads us to two new system invariants: causal irreversibility-the asymmetry between the causal representations-and crypticity-the degree to which a process hides its state information.

------------------------------------------------------------------------

35\. · 83% match · 2004 · 0.7 cit/yr\
**Reductions of Hidden Information Sources** ([link](https://doi.org/10.1007/s10955-005-6797-4))\
N. Ay and J. Crutchfield\
*Journal of Statistical Physics* · May 21, 2004 · 15 citations

> In all but special circumstances, measurements of time-dependent processes reflect internal structures and correlations only indirectly. Building predictive models of such hidden information sources requires discovering, in some way, the internal states and mechanisms. Unfortunately, there are often many possible models that are observationally equivalent. Here we show that the situation is not as arbitrary as one would think. We show that generators of hidden stochastic processes can be reduced to a minimal form and compare this reduced representation to that provided by computational mechanics – the ε-machine. On the way to developing deeper, measure-theoretic foundations for the latter, we introduce a new two-step reduction process. The first step (internal-event reduction) produces the smallest observationally equivalent σ-algebra and the second (internal-state reduction) removes σ-algebra components that are redundant for optimal prediction. For several classes of stochastic dynamical systems these reductions produce representations that are equivalent to ε-machines.

------------------------------------------------------------------------

36\. · 81% match · 2014 · 5.2 cit/yr\
\*\*Computational Mechanics of Input–Output Processes: Structured Transformations and the ϵ\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \*\* ([link](https://doi.org/10.1007/s10955-015-1327-5))\
Nix Barnett and J. Crutchfield\
*Journal of Statistical Physics* · Dec 8, 2014 · 59 citations

> Computational mechanics quantifies structure in a stochastic process via its causal states, leading to the process’s minimal, optimal predictor—the ϵ-machine\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}
> ``` math
> \epsilon {\text {-}}\mathrm{machine}
> ```
> \end{document}. We extend computational mechanics to communication channels coupling two processes, obtaining an analogous optimal model—the ϵ-transducer\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}
> ``` math
> \epsilon {\text {-}}\mathrm{transducer}
> ```
> \end{document}—of the stochastic mapping between them. Here, we lay the foundation of a structural analysis of communication channels, treating joint processes and processes with input. The result is a principled structural analysis of mechanisms that support information flow between processes. It is the first in a series on the structural information theory of memoryful channels, channel composition, and allied conditional information measures.

------------------------------------------------------------------------

37\. · 78% match · 2012 · 21 cit/yr\
**Thermodynamics as a theory of decision-making with information-processing costs** ([link](https://doi.org/10.1098/rspa.2012.0683))\
Pedro A. Ortega and Daniel A. Braun\
*Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences* · Apr 29, 2012 · 301 citations

> Perfectly rational decision-makers maximize expected utility, but crucially ignore the resource costs incurred when determining optimal actions. Here, we propose a thermodynamically inspired formalization of bounded rational decision-making where information processing is modelled as state changes in thermodynamic systems that can be quantified by differences in free energy. By optimizing a free energy, bounded rational decision-makers trade off expected utility gains and information-processing costs measured by the relative entropy. As a result, the bounded rational decision-making problem can be rephrased in terms of well-known variational principles from statistical physics. In the limit when computational costs are ignored, the maximum expected utility principle is recovered. We discuss links to existing decision-making frameworks and applications to human decision-making experiments that are at odds with expected utility theory. Since most of the mathematical machinery can be borrowed from statistical physics, the main contribution is to re-interpret the formalism of thermodynamic free-energy differences in terms of bounded rational decision-making and to discuss its relationship to human decision-making experiments.

------------------------------------------------------------------------

38\. · 76% match · 2015 · 12 cit/yr\
**Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle** ([link](https://doi.org/10.3389/frobt.2015.00027))\
Tim Genewein, Felix Leibfried, Jordi Grau-Moya, and Daniel A. Braun\
*Frontiers Robotics AI* · Nov 1, 2015 · 125 citations

> Abstraction and hierarchical information-processing are hallmarks of human and animal intelligence underlying the unrivaled flexibility of behavior in biological systems. Achieving such a flexibility in artificial systems is challenging, even with more and more computational power. Here we investigate the hypothesis that abstraction and hierarchical information-processing might in fact be the consequence of limitations in information-processing power. In particular, we study an information-theoretic framework of bounded rational decision-making that trades off utility maximization against information-processing costs. We apply the basic principle of this framework to perception-action systems with multiple information-processing nodes and derive bounded optimal solutions. We show how the formation of abstractions and decision-making hierarchies depends on information-processing costs. We illustrate the theoretical ideas with example simulations and conclude by formalizing a mathematically unifying optimization principle that could potentially be extended to more complex systems.

------------------------------------------------------------------------

39\. · 74% match · 2020 · 40 cit/yr\
**Active inference on discrete state-spaces: A synthesis** ([link](https://doi.org/10.1016/j.jmp.2020.102447))\
Lancelot Da Costa et al.\
*Journal of Mathematical Psychology* · Jan 20, 2020 · 255 citations

> Active inference is a normative principle underwriting perception, action, planning, decision-making and learning in biological or artificial agents. From its inception, its associated process theory has grown to incorporate complex generative models, enabling simulation of a wide range of complex behaviours. Due to successive developments in active inference, it is often difficult to see how its underlying principle relates to process theories and practical implementation. In this paper, we try to bridge this gap by providing a complete mathematical synthesis of active inference on discrete state-space models. This technical summary provides an overview of the theory, derives neuronal dynamics from first principles and relates this dynamics to biological processes. Furthermore, this paper provides a fundamental building block needed to understand active inference for mixed generative models; allowing continuous sensations to inform discrete representations. This paper may be used as follows: to guide research towards outstanding challenges, a practical guide on how to implement active inference to simulate experimental behaviour, or a pointer towards various in-silico neurophysiological responses that may be used to make empirical predictions.

------------------------------------------------------------------------

40\. · 72% match · 2013 · 26 cit/yr\
**The anatomy of choice: active inference and agency** ([link](https://doi.org/10.3389/fnhum.2013.00598))\
Karl J. Friston et al.\
*Frontiers in Human Neuroscience* · Sep 25, 2013 · 329 citations

> This paper considers agency in the setting of embodied or active inference. In brief, we associate a sense of agency with prior beliefs about action and ask what sorts of beliefs underlie optimal behavior. In particular, we consider prior beliefs that action minimizes the Kullback–Leibler (KL) divergence between desired states and attainable states in the future. This allows one to formulate bounded rationality as approximate Bayesian inference that optimizes a free energy bound on model evidence. We show that constructs like expected utility, exploration bonuses, softmax choice rules and optimism bias emerge as natural consequences of this formulation. Previous accounts of active inference have focused on predictive coding and Bayesian filtering schemes for minimizing free energy. Here, we consider variational Bayes as an alternative scheme that provides formal constraints on the computational anatomy of inference and action—constraints that are remarkably consistent with neuroanatomy. Furthermore, this scheme contextualizes optimal decision theory and economic (utilitarian) formulations as pure inference problems. For example, expected utility theory emerges as a special case of free energy minimization, where the sensitivity or inverse temperature (of softmax functions and quantal response equilibria) has a unique and Bayes-optimal solution—that minimizes free energy. This sensitivity corresponds to the precision of beliefs about behavior, such that attainable goals are afforded a higher precision or confidence. In turn, this means that optimal behavior entails a representation of confidence about outcomes that are under an agent’s control.

------------------------------------------------------------------------

41\. · 70% match · 2025\
**Decision, Inference, and Information: Formal Equivalences Under Active Inference** ([link](https://doi.org/10.3390/e28010001))\
Patrick Sweeney, Jaime Ruiz-Serra, and Michael S. Harré\
*Entropy* · Dec 19, 2025 · 0 citations

> A central challenge in artificial intelligence and cognitive science is identifying a unifying principle that governs inference, learning, and action. Active inference proposes such a principle: the minimization of variational free energy. Advocates of active inference argue that the framework subsumes classical models of optimal behavior—including Bayesian decision theory, resource rationality, optimal control, and reinforcement learning—while also instantiating information-theoretic principles such as rate-distortion theory and maximum entropy. However, the literature outlining these conceptual links remains fragmented, limiting integration across fields. This review develops these connections systematically. We show how these major frameworks admit formal correspondences with expected free energy minimization when expressed in variational form, exposing a shared optimization principle that underlies theories of optimal decision-making and information processing. This synthesis is intended both to orient researchers from other fields who are new to active inference and to clarify foundational assumptions for those already working within the framework.

------------------------------------------------------------------------

42\. · 68% match · 2008 · 0.7 cit/yr\
**Approximate predictive state representations** ([link](https://doi.org/10.65109/wtqk6477))\
Britton Wolfe, Michael R. James, and Satinder Singh\
*Adaptive Agents and Multi-Agent Systems* · May 12, 2008 · 13 citations

> Predictive state representations (PSRs) are models that represent the state of a dynamical system as a set of predictions about future events. The existing work with PSRs focuses on trying to learn exact models, an approach that cannot scale to complex dynamical systems. In contrast, our work takes the first steps in developing a theory of approximate PSRs. We examine the consequences of using an approximate predictive state representation, bounding the error of the approximate state under certain conditions. We also introduce factored PSRs, a class of PSRs with a particular approximate state representation. We show that the class of factored PSRs allow one to tune the degree of approximation by trading off accuracy for compactness. We demonstrate this trade-off empirically on some example systems, using factored PSRs that were learned from data.

------------------------------------------------------------------------

43\. · 66% match · 2009 · 16 cit/yr\
**Closing the learning-planning loop with predictive state representations** ([link](https://doi.org/10.1177/0278364911404092))\
Byron Boots, S. Siddiqi, and Geoffrey J. Gordon\
*The International Journal of Robotics Research* · Dec 11, 2009 · 270 citations

> A central problem in artificial intelligence is to choose actions to maximize reward in a partially observable, uncertain environment. To do so, we must learn an accurate environment model, and then plan to maximize reward. Unfortunately, learning algorithms often recover a model that is too inaccurate to support planning or too large and complex for planning to succeed; or they require excessive prior domain knowledge or fail to provide guarantees such as statistical consistency. To address this gap, we propose a novel algorithm which provably learns a compact, accurate model directly from sequences of action-observation pairs. We then evaluate the learner by closing the loop from observations to actions. In more detail, we present a spectral algorithm for learning a predictive state representation (PSR), and evaluate it in a simulated, vision-based mobile robot planning task, showing that the learned PSR captures the essential features of the environment and enables successful and efficient planning. Our algorithm has several benefits which have not appeared together in any previous PSR learner: it is computationally efficient and statistically consistent; it handles high-dimensional observations and long time horizons; and, our close-the-loop experiments provide an end-to-end practical test.

------------------------------------------------------------------------

44\. · 64% match · 2009\
**Optimally Predictive Causal Inference** ([link](https://www.semanticscholar.org/paper/f1d54e3e5bc4330d6c8a52b3d261eef31781dfde))\
Susanne Still\
0 citations

> Natural systems compute intrinsically and produce information. The organization of a stochastic dynamical system is reflected in the time series of observations made of the system and can be quantified by the excess entropy or predictive information—the mutual information between past and future. This information can be used to build models of varying complexity that capture the causal structure of the underlying system. Here we study two distinct cases of causal inference, which we call optimal causal filtering and optimal causal estimation. Optimal causal filtering corresponds to the ideal case in which infinite data are available. We show that, in the limit in which a model complexity constraint is relaxed, the filtering method finds the causal architecture of a stochastic dynamical system, known as the causal state partition. In that limit, it reconstructs exactly the system’s hidden, causal states. More generally, it finds a graded model-complexity hierarchy of approximations to the causal architecture. For nonideal cases with finite data, we show how the correct number of underlying causal states can be found by optimal causal estimation. A previously derived model complexity control term allows us to correct for the effect of statistical fluctuations in probability estimates and thereby avoid over-fitting.

------------------------------------------------------------------------

45\. · 62% match · 2017 · 4.5 cit/yr\
**Thermodynamic Cost and Benefit of Memory.** ([link](https://doi.org/10.1103/PhysRevLett.124.050601))\
Susanne Still\
*Physical review letters* · Apr 29, 2017 · 41 citations

> This Letter exposes a tight connection between the thermodynamic efficiency of information processing and predictive inference. A generalized lower bound on dissipation is derived for partially observable information engines which are allowed to use temperature differences. It is shown that the retention of irrelevant information limits efficiency. A data representation method is derived from optimizing a fundamental physical limit to information processing: minimizing the lower bound on dissipation leads to a compression method that maximally retains relevant, predictive, information. In that sense, predictive inference emerges as the strategy that least precludes energy efficiency.

------------------------------------------------------------------------

46\. · 60% match · 2012 · 16 cit/yr\
**An information-theoretic approach to curiosity-driven reinforcement learning** ([link](https://doi.org/10.1007/s12064-011-0142-z))\
Susanne Still and Doina Precup\
*Theory in Biosciences* · Jul 12, 2012 · 219 citations

------------------------------------------------------------------------

47\. · 58% match · 2014 · 3.3 cit/yr\
**Informational and Causal Architecture of Discrete-Time Renewal Processes** ([link](https://doi.org/10.3390/e17074891))\
Sarah E. Marzen and J. Crutchfield\
*Entropy* · Aug 28, 2014 · 39 citations

> Renewal processes are broadly used to model stochastic behavior consisting of isolated events separated by periods of quiescence, whose durations are specified by a given probability law. Here, we identify the minimal sufficient statistic for their prediction (the set of causal states), calculate the historical memory capacity required to store those states (statistical complexity), delineate what information is predictable (excess entropy), and decompose the entropy of a single measurement into that shared with the past, future, or both. The causal state equivalence relation defines a new subclass of renewal processes with a finite number of causal states despite having an unbounded interevent count distribution. We use these formulae to analyze the output of the parametrized Simple Nonunifilar Source, generated by a simple two-state hidden Markov model, but with an infinite-state epsilon-machine presentation. All in all, the results lay the groundwork for analyzing processes with infinite statistical complexity and infinite excess entropy.

------------------------------------------------------------------------

48\. · 56% match · 2016 · 3.2 cit/yr\
**Informational and Causal Architecture of Continuous-time Renewal Processes** ([link](https://doi.org/10.1007/s10955-017-1793-z))\
Sarah E. Marzen and J. Crutchfield\
*Journal of Statistical Physics* · Nov 3, 2016 · 31 citations

> We introduce the minimal maximally predictive models (ϵ-machines\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}
> ``` math
> \epsilon \text{-machines }
> ```
> \end{document}) of processes generated by certain hidden semi-Markov models. Their causal states are either discrete, mixed, or continuous random variables and causal-state transitions are described by partial differential equations. As an application, we present a complete analysis of the ϵ-machines\documentclass\[12pt\]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}
> ``` math
> \epsilon \text{-machines }
> ```
> \end{document} of continuous-time renewal processes. This leads to closed-form expressions for their entropy rate, statistical complexity, excess entropy, and differential information anatomy rates.

------------------------------------------------------------------------

49\. · 54% match · 2017 · 3.0 cit/yr\
**Structure and Randomness of Continuous-Time, Discrete-Event Processes** ([link](https://doi.org/10.1007/s10955-017-1859-y))\
Sarah E. Marzen and J. Crutchfield\
*Journal of Statistical Physics* · Apr 16, 2017 · 27 citations

> Loosely speaking, the Shannon entropy rate is used to gauge a stochastic process’ intrinsic randomness; the statistical complexity gives the cost of predicting the process. We calculate, for the first time, the entropy rate and statistical complexity of stochastic processes generated by finite unifilar hidden semi-Markov models—memoryful, state-dependent versions of renewal processes. Calculating these quantities requires introducing novel mathematical objects (
> ``` math
> \epsilon 
> ```
> ϵ-machines of hidden semi-Markov processes) and new information-theoretic methods to stochastic processes.

------------------------------------------------------------------------

50\. · 52% match · 2019 · 9.4 cit/yr\
**State Abstraction as Compression in Apprenticeship Learning** ([link](https://doi.org/10.1609/AAAI.V33I01.33013134))\
David Abel et al.\
*AAAI Conference on Artificial Intelligence* · Jul 17, 2019 · 64 citations

> State abstraction can give rise to models of environments that are both compressed and useful, thereby enabling efficient sequential decision making. In this work, we offer the first formalism and analysis of the trade-off between compression and performance made in the context of state abstraction for Apprenticeship Learning. We build on Rate-Distortion theory, the classic Blahut-Arimoto algorithm, and the Information Bottleneck method to develop an algorithm for computing state abstractions that approximate the optimal tradeoff between compression and performance. We illustrate the power of this algorithmic structure to offer insights into effective abstraction, compression, and reinforcement learning through a mixture of analysis, visuals, and experimentation.

*Showing top 50 of 89 papers. Full details available via CSV or BibTeX export.*
