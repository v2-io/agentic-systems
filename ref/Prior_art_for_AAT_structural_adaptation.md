# Prior art for AAT structural adaptation

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which, when parametric tuning fails and fitness drops, an agent is forced into structural adaptation by changing its representational architecture or model class rather than only adjusting parameters. The framework assumes systems that cannot fully represent the environment within their initial fixed parameter space. Prioritize formal mathematical predecessors, but also include weaker epistemic or conceptual treatments when they clearly articulate closely related claims. Relevant domains include continual learning, meta-learning, computational neuroscience, non-stationary reinforcement learning, adaptive control, singular perturbation and hierarchical control, and related interdisciplinary lineages. Relevant matches include: formal triggers, impossibility results, necessity claims, or closely related constructive formalisms for when an online agent must alter representational structure rather than continue parametric adaptation; applications of singular perturbation theory or other rigorous timescale-separation mathematics to learning, cognition, or agent adaptation, especially where fast cognitive or policy processes are treated as reaching a quasi-steady state before slower structural processes act; work on offline consolidation, replay, or related mechanisms that transfer information from episodic to semantic states using the Information Bottleneck, rate-distortion theory, or mathematically close equivalents based on constrained memory-prediction or compression tradeoffs; and mathematical analyses of the stability-plasticity dilemma that yield specific feasibility regions, forgetting rates, or bounds governing adaptation. Count both papers that integrate several parts of this picture and papers that establish one pillar cleanly within a different lineage. Exclude purely offline neural architecture search by human engineers, and exclude simple experience replay work that merely resamples data without a compression, transfer, or bottleneck objective. Restrict the search to academic papers only.

*Found 115 papers · May 20, 2026 · Estimated coverage of relevant papers: 70%*

## Summary of Results

The strongest precedent is a patchwork of formal pillars rather than a single unified framework: fixed-size continual learners face impossibility or linear-memory barriers \[1\], \[2\], bounded-resource online model selection requires preserving raw episodes to support later model-class changes \[3\], \[4\], and older partially observed/control lineages explicitly grow or switch representations when the current state is inadequate \[5\], \[6\], \[7\].

#### Formal necessity for leaving a fixed parameterization

- Nonlinear feature learning in continual learning admits no algorithm that simultaneously adapts and avoids forgetting in general \[1\].
- Any continual learner needs memory growing at least linearly with the number of tasks; efficient performance may require improper learning \[2\].
- Misspecified bandit/RL models show analogous failure: fixed linear classes can force linear regret or hard lower bounds unless the agent detects misspecification or falls back to a different class \[8\], \[9\], \[10\].

#### Constructive structural adaptation lineages

- Hidden-state RL already used explicit state splitting when utility prediction fails, growing internal state only when distinctions become useful \[5\], \[6\].
- Computational mechanics and PSRs formalize minimal predictive state/model classes and show when richer predictive structure is required beyond fixed Markov/POMDP parameterizations \[11\], \[12\], \[13\], \[14\].

#### Timescales, consolidation, and compression

- Singular-perturbation and two-timescale stochastic approximation provide the rigorous fast/slow template in which fast policy/value variables equilibrate before slower representation variables move \[15\], \[16\], \[17\], \[18\], \[19\].
- The replay/consolidation pillar is strongest in normative memory work: information bottleneck and semantic compression \[20\], \[21\], \[22\], plus episodic memory as the buffer that preserves evidence needed for later structural revision \[3\].

## Paper Catalog (115 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2016 | 1.0 | Episodic memory as a prerequisite for online updates of model structure ([link](https://www.semanticscholar.org/paper/b0c205c6655e8ab97bbc4ba0dc55ac40218ba830)) | D. G. Nagy and G. Orbán | Cognitive Science |
| 2 | 2022 | 3.4 | Continual learning: a feature extraction formalization, an efficient algorithm, and fundamental obstructions ([link](https://doi.org/10.48550/arXiv.2203.14383)) | Binghui Peng and Andrej Risteski | ArXiv |
| 3 |  |  | Continual learning: a feature extraction formalization, an efﬁcient algorithm, and barriers ([link](https://www.semanticscholar.org/paper/961aa0a0cd41b92aeaf82006d91b18bc1ae84114)) | Binghui Peng and Andrej Risteski |  |
| 4 | 2022 | 6.4 | Memory Bounds for Continual Learning ([link](https://doi.org/10.1109/FOCS54457.2022.00056)) | Xi Chen, Christos Papadimitriou, and Binghui Peng | 2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS) |
| 5 | 1999 | 19 | Computational Mechanics: Pattern and Prediction, Structure and Simplicity ([link](https://doi.org/10.1023/A:1010388907793)) | C. Shalizi and J. Crutchfield | Journal of Statistical Physics |
| 6 | 2004 | 9.1 | Blind Construction of Optimal Nonlinear Recursive Predictors for Discrete Sequences ([link](https://www.semanticscholar.org/paper/da820634f29f02e10c117fa84857753ded8f0204)) | C. Shalizi and Kristina Lisa Shalizi | Conference on Uncertainty in Artificial Intelligence |
| 7 | 1983 | 44 | A UNIVERSAL PRIOR FOR INTEGERS AND ESTIMATION BY MINIMUM DESCRIPTION LENGTH ([link](https://doi.org/10.1214/AOS/1176346150)) | J. Rissanen | Annals of Statistics |
| 8 | 1984 | 25 | Universal coding, information, prediction, and estimation ([link](https://doi.org/10.1109/TIT.1984.1056936)) | J. Rissanen | IEEE Trans. Inf. Theory |
| 9 | 2016 | 25 | Computational principles of synaptic memory consolidation ([link](https://doi.org/10.1038/nn.4401)) | M. Benna and Stefano Fusi | Nature Neuroscience |
| 10 | 1989 | 50 | Stochastic Complexity in Statistical Inquiry ([link](https://doi.org/10.1142/0822)) | J. Rissanen | World Scientific Series in Computer Science |
| 11 | 2005 | 27 | Cascade models of synaptically stored memories. ([link](https://doi.org/10.1016/J.NEURON.2005.02.001)) | Stefano Fusi, P. Drew, and L. Abbott | Neuron |
| 12 | 1995 | 33 | The context-tree weighting method: basic properties ([link](https://doi.org/10.1109/18.382012)) | F. Willems, Y. Shtarkov, and T. Tjalkens | IEEE Trans. Inf. Theory |
| 13 | 1997 | 16 | Stochastic approximation with two time scales ([link](https://doi.org/10.1016/S0167-6911(97%2990015-3)) | V. Borkar | Systems & Control Letters |
| 14 | 2007 | 12 | Limits on the memory storage capacity of bounded synapses ([link](https://doi.org/10.1038/nn1859)) | Stefano Fusi and L. Abbott | Nature Neuroscience |
| 15 | 2000 | 17 | The O.D.E. Method for Convergence of Stochastic Approximation and Reinforcement Learning ([link](https://doi.org/10.1137/S0363012997331639)) | V. Borkar and Sean P. Meyn | SIAM J. Control. Optim. |
| 16 | 2020 | 5.0 | Optimal forgetting: Semantic compression of episodic memories ([link](https://doi.org/10.1371/journal.pcbi.1008367)) | D. G. Nagy, B. Török, and G. Orbán | PLoS Computational Biology |
| 17 | 1986 | 66 | Singular perturbation methods in control : analysis and design ([link](https://doi.org/10.1137/1.9781611971118)) | P. Kokotovic, H. Khalil, and J. O’Reilly |  |
| 18 | 2000 | 165 | The information bottleneck method ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c)) | Naftali Tishby, Fernando C Pereira, and W. Bialek | ArXiv |
| 19 | 1993 | 6.6 | Overcoming Incomplete Perception with Utile Distinction Memory ([link](https://doi.org/10.1016/b978-1-55860-307-3.50031-9)) | A. McCallum | International Conference on Machine Learning |
| 20 | 2021 | 20 | Adapting to Misspecification in Contextual Bandits ([link](https://www.semanticscholar.org/paper/0979cb2939a71873542a4a7f34990bfbd1071f9c)) | Dylan J. Foster, C. Gentile, M. Mohri, and Julian Zimmert | ArXiv |
| 21 | 2013 | 5.8 | Efficient Partitioning of Memory Systems and Its Importance for Memory Consolidation ([link](https://doi.org/10.1371/journal.pcbi.1003146)) | Alex Roxin and Stefano Fusi | PLoS Computational Biology |
| 22 | 2017 | 8.0 | Misspecified Linear Bandits ([link](https://doi.org/10.1609/aaai.v31i1.11052)) | Avishek Ghosh, Sayak Ray Chowdhury, and Aditya Gopalan | ArXiv |
| 23 | 2019 | 13 | Finite-Time Performance Bounds and Adaptive Learning Rate Selection for Two Time-Scale Reinforcement Learning ([link](https://www.semanticscholar.org/paper/8cba38e7e2a4b6400c0dbb7a0c2c98918e354d57)) | Harsh Gupta, R. Srikant, and Lei Ying | ArXiv |
| 24 | 2007 | 46 | The Minimum Description Length Principle (Adaptive Computation and Machine Learning) ([link](https://doi.org/10.7551/mitpress/4643.001.0001)) | P. Grünwald |  |
| 25 | 1997 | 47 | Adaptive control using multiple models ([link](https://doi.org/10.1109/9.554398)) | K. Narendra and Jeyendran Balakrishnan | IEEE Trans. Autom. Control. |
| 26 | 2020 | 3.5 | Hebbian plasticity in parallel synaptic pathways: A circuit mechanism for systems memory consolidation ([link](https://doi.org/10.1371/journal.pcbi.1009681)) | M. Remme et al. | PLoS Computational Biology |
| 27 | 1992 | 0.7 | First Results with Utile Distinction Memory for Reinforcement Learning ([link](https://www.semanticscholar.org/paper/67eb2366790a9d5efb66001833f6bea8141b3472)) | R. A. McCallum |  |
| 28 | 2001 | 24 | Predictive Representations of State ([link](https://www.semanticscholar.org/paper/4a7de0669fd835b2efcab97c7d3dc28ea7a1e6a3)) | M. Littman, R. Sutton, and Satinder Singh | Neural Information Processing Systems |
| 29 | 2020 | 11 | Nonlinear Two-Time-Scale Stochastic Approximation: Convergence and Finite-Time Performance ([link](https://doi.org/10.1109/TAC.2022.3210147)) | Thinh T. Doan | IEEE Transactions on Automatic Control |
| 30 | 2021 | 17 | Organizing memories for generalization in complementary learning systems ([link](https://doi.org/10.1038/s41593-023-01382-9)) | Weinan Sun, Madhu S. Advani, N. Spruston, Andrew M. Saxe, and James E. Fitzgerald | Nature Neuroscience |
| 31 | 2018 | 0.9 | Semantic compression of episodic memories ([link](https://doi.org/10.32470/ccn.2018.1050-0)) | D. G. Nagy, B. Török, and G. Orbán | arXiv: Neurons and Cognition |
| 32 | 2014 | 8.0 | Statistical Computations Underlying the Dynamics of Memory Updating ([link](https://doi.org/10.1371/journal.pcbi.1003939)) | S. Gershman, Angela Radulescu, K. Norman, and Y. Niv | PLoS Computational Biology |
| 33 | 2019 | 28 | Learning with Good Feature Representations in Bandits and in RL with a Generative Model ([link](https://www.semanticscholar.org/paper/57e72da5765157f72e216054f64280dbf3f8d865)) | Tor Lattimore and Csaba Szepesvari | International Conference on Machine Learning |
| 34 | 2004 | 14 | Predictive State Representations: A New Theory for Modeling Dynamical Systems ([link](https://www.semanticscholar.org/paper/532c61a2af5cde64628d0cdd2ba0823800118d0f)) | Satinder Singh, Michael R. James, and Matthew R. Rudary | Conference on Uncertainty in Artificial Intelligence |
| 35 | 2009 | 5.2 | Past-future information bottleneck in dynamical systems. ([link](https://doi.org/10.1103/PHYSREVE.79.041925)) | F. Creutzig, A. Globerson, and Naftali Tishby | Physical review. E, Statistical, nonlinear, and soft matter physics |
| 36 | 2020 | 10 | Regret Bound Balancing and Elimination for Model Selection in Bandits and RL ([link](https://www.semanticscholar.org/paper/560f6277f345d6a3aa0004b1bb2b8e7e8fe985df)) | Aldo Pacchiano, Christoph Dann, C. Gentile, and P. Bartlett | ArXiv |
| 37 | 2017 |  | Episodic memory for continual model learning ([link](https://www.semanticscholar.org/paper/68d538f7cbb7f1b3f0158c4b53bbb9c919359de6)) | D. G. Nagy and G. Orbán | ArXiv |
| 38 | 2013 | 4.7 | A memory frontier for complex synapses ([link](https://www.semanticscholar.org/paper/75c7ec96aaa5d271d541466e5d5a7807e815b488)) | Subhaneil Lahiri and S. Ganguli | Neural Information Processing Systems |
| 39 | 2017 | 0.4 | Dynamic-Depth Context Tree Weighting ([link](https://www.semanticscholar.org/paper/8ba7fa658f1fe795a5c1a5ee1f2de36a61658be5)) | J. Messias and Shimon Whiteson | Neural Information Processing Systems |
| 40 | 2017 |  | Utile Context Tree Weighting ([link](https://www.semanticscholar.org/paper/7ec7c868d98101b304756b86d914684ebd93bb07)) | J. Messias and Shimon Whiteson | Neural Information Processing Systems |
| 41 | 2021 | 1.3 | Multi Timescale Stochastic Approximation: Stability and Convergence ([link](https://www.semanticscholar.org/paper/589bfa87d5e5cb1d6a3d7fad4faa2bbb20140212)) | Rohan Deb, Swetha Ganesh, and S. Bhatnagar |  |
| 42 | 1989 | 134 | Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem ([link](https://doi.org/10.1016/S0079-7421(08%2960536-8)) | M. McCloskey and N. J. Cohen | Psychology of Learning and Motivation |
| 43 | 2020 | 7.1 | Online Model Selection for Reinforcement Learning with Function Approximation ([link](https://www.semanticscholar.org/paper/cb40cc80be6db8da552c1ecfc3ad2edbd2c2f0e7)) | Jonathan Lee, Aldo Pacchiano, Vidya Muthukumar, Weihao Kong, and E. Brunskill | International Conference on Artificial Intelligence and Statistics |
| 44 | 2015 | 1.6 | Computational principles of biological memory ([link](https://www.semanticscholar.org/paper/2e9902cbdb8317365655beeafae25d4ae2f69372)) | M. Benna and Stefano Fusi | arXiv: Neurons and Cognition |
| 45 | 2007 | 46 | Bayesian Online Changepoint Detection ([link](https://www.semanticscholar.org/paper/9cacd41e4fbe518436877a6f1b24982099216e46)) | Ryan P. Adams and D. MacKay | arXiv: Machine Learning |
| 46 | 2011 | 3.5 | Context Tree Switching ([link](https://doi.org/10.1109/DCC.2012.39)) | J. Veness, K. S. Ng, Marcus Hutter, and Michael Bowling | 2012 Data Compression Conference |
| 47 | 2017 | 7.8 | Parameter-Free Online Learning via Model Selection ([link](https://www.semanticscholar.org/paper/1340d0789112200d22fbbbfdd030e9cf71c67ebe)) | Dylan J. Foster, Satyen Kale, M. Mohri, and Karthik Sridharan | Neural Information Processing Systems |
| 48 | 2007 | 0.6 | Optimal Causal Inference ([link](https://www.semanticscholar.org/paper/0c8c8cd4275c7f3505ba0250d7f1be54842d9440)) | Susanne Still, J. Crutchfield, and C. J. Ellison | ArXiv |
| 49 | 2013 | 3.6 | Synaptic Scaling Enables Dynamically Distinct Short- and Long-Term Memory Formation ([link](https://doi.org/10.1186/1471-2202-14-S1-P415)) | Christian Tetzlaff, Christoph Kolodziejski, M. Timme, M. Tsodyks, and F. Wörgötter | PLoS Computational Biology |
| 50 | 2004 | 7.8 | Off-line replay maintains declarative memories in a model of hippocampal-neocortical interactions ([link](https://doi.org/10.1038/nn1202)) | S. Káli and P. Dayan | Nature Neuroscience |
| 51 | 2007 | 14 | Hippocampal Contributions to Control: The Third Way ([link](https://www.semanticscholar.org/paper/c8e337a12df57783edb75eace2b8d67270a6823c)) | M. Lengyel and P. Dayan | Neural Information Processing Systems |
| 52 | 2001 | 17 | Online Model Selection Based on the Variational Bayes ([link](https://doi.org/10.1162/089976601750265045)) | Masa-aki Sato | Neural Computation |
| 53 | 2014 | 3.8 | Skip Context Tree Switching ([link](https://www.semanticscholar.org/paper/f6ca9c148417d4167ba8b72f185a35649dc4b446)) | Marc G. Bellemare, J. Veness, and Erik Talvitie | International Conference on Machine Learning |
| 54 | 2024 | 0.4 | A Lyapunov theory demonstrating a fundamental limit on the speed of systems consolidation ([link](https://doi.org/10.48550/arXiv.2402.01605)) | Alireza Alemi, Emre R. F. Aksay, and Mark S. Goldman | ArXiv |
| 55 | 2025 |  | Lyapunov theory demonstrating a fundamental limit on the speed of systems consolidation ([link](https://doi.org/10.1103/physrevresearch.7.023174)) | Alireza Alemi, Emre R. F. Aksay, and Mark S. Goldman | Physical review research |
| 56 | 2023 | 13 | The Ideal Continual Learner: An Agent That Never Forgets ([link](https://doi.org/10.48550/arXiv.2305.00316)) | Liangzu Peng, Paris V. Giampouras, and René Vidal | International Conference on Machine Learning |
| 57 | 2010 | 5.1 | Bayesian Nonparametric Methods for Learning Markov Switching Processes ([link](https://doi.org/10.1109/MSP.2010.937999)) | E. Fox, Erik B. Sudderth, Michael I. Jordan, and A. Willsky | IEEE Signal Processing Magazine |
| 58 | 1993 | 0.2 | Learning with Incomplete Selective Perception ([link](https://www.semanticscholar.org/paper/c54a1a81a37a4946039befc57c2fee74d378cf35)) | A. McCallum |  |
| 59 | 2018 | 1.0 | Best of many worlds: Robust model selection for online supervised learning ([link](https://www.semanticscholar.org/paper/e9d7c208497c34bda1fea5f2a131a1ee41bc575d)) | Vidya Muthukumar, Mitas Ray, Anant Sahai, and P. Bartlett | ArXiv |
| 60 | 2014 | 5.1 | Information Bottleneck Approach to Predictive Inference ([link](https://doi.org/10.3390/e16020968)) | Susanne Still | Entropy |
| 61 | 2000 | 1.4 | Information Bottlenecks, Causal States, and Statistical Relevance Bases: How to Represent Relevant Information in memoryless transduction ([link](https://doi.org/10.1142/S0219525902000481)) | C. Shalizi and J. Crutchfield | Adv. Complex Syst. |
| 62 | 2019 | 7.0 | Two-Timescale Networks for Nonlinear Value Function Approximation ([link](https://doi.org/10.7939/R3-DX5R-7020)) | Wesley Chung, Somjit Nath, A. Joseph, and Martha White | International Conference on Learning Representations |
| 63 | 2020 | 20 | Approximate information state for approximate planning and reinforcement learning in partially observed systems ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980)) | Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan | ArXiv |
| 64 | 2013 | 3.4 | Efficient learning and planning with compressed predictive states ([link](https://doi.org/10.5555/2627435.2750354)) | William L. Hamilton, M. M. Fard, and Joelle Pineau | J. Mach. Learn. Res. |
| 65 | 2010 | 1.9 | Bayesian variable order Markov models ([link](https://www.semanticscholar.org/paper/ab50e1fa0f249c1c758729573d36a508dae9cb1d)) | Christos Dimitrakakis | International Conference on Artificial Intelligence and Statistics |
| 66 | 1999 | 5.7 | Universal linear prediction by model order weighting ([link](https://doi.org/10.1109/78.790651)) | A. Singer and M. Feder | IEEE Trans. Signal Process. |
| 67 | 1996 | 3.0 | Hidden state and reinforcement learning with instance-based state identification ([link](https://doi.org/10.1109/3477.499796)) | A. McCallum | IEEE transactions on systems, man, and cybernetics. Part B, Cybernetics : a publication of the IEEE Systems, Man, and Cybernetics Society |
| 68 | 2018 | 12 | Continual Reinforcement Learning with Complex Synapses ([link](https://www.semanticscholar.org/paper/4b0e8a4df3605d5e22c9eacc3cb360ff08eb8c4e)) | Christos Kaplanis, M. Shanahan, and C. Clopath | International Conference on Machine Learning |
| 69 | 2021 | 1.9 | Optimal Model Selection in Contextual Bandits with Many Classes via Offline Oracles ([link](https://www.semanticscholar.org/paper/f40369ffd66b7476a7b630bd310be35069158a2d)) | Sanath Kumar Krishnamurthy and S. Athey | ArXiv |
| 70 | 2023 | 1.0 | Does Sparsity Help in Learning Misspecified Linear Bandits? ([link](https://doi.org/10.48550/arXiv.2303.16998)) | Jialin Dong and Lin F. Yang | International Conference on Machine Learning |
| 71 | 1989 | 26 | Inferring statistical complexity. ([link](https://doi.org/10.1103/PHYSREVLETT.63.105)) | J. Crutchfield and K. Young | Physical review letters |
| 72 | 1998 | 3.1 | A Decision-Theoretic Extension of Stochastic Complexity and Its Applications to Learning ([link](https://doi.org/10.1109/18.681319)) | K. Yamanishi | IEEE Trans. Inf. Theory |
| 73 | 2003 | 0.7 | Adaptive control using multiple models, switching and tuning ([link](https://doi.org/10.1002/acs.740)) | K. Narendra, Osvaldo Driollet, M. Feiler, and Koshy George | International Journal of Adaptive Control and Signal Processing |
| 74 | 2010 | 0.6 | Following the Flattened Leader ([link](https://www.semanticscholar.org/paper/acec7cd7cfd22b71efa974ab49e04cb547fece83)) | W. Kotłowski, P. Grünwald, and S. D. Rooij | Annual Conference Computational Learning Theory |
| 75 | 2018 | 5.5 | Spatio-temporal Bayesian On-line Changepoint Detection with Model Selection ([link](https://www.semanticscholar.org/paper/e6d2588d205ab64b4db7b1d5f2b01d9862a4a243)) | Jeremias Knoblauch and T. Damoulas | International Conference on Machine Learning |
| 76 | 1997 |  | On-Line Maximum Likelihood Prediction with Respect to General Loss Functions ([link](https://doi.org/10.1006/jcss.1997.1503)) | K. Yamanishi | J. Comput. Syst. Sci. |
| 77 | 2024 | 3.7 | LoRanPAC: Low-rank Random Features and Pre-trained Models for Bridging Theory and Practice in Continual Learning ([link](https://www.semanticscholar.org/paper/f344ff3e1ccbbf16b31cb688d26831034decd8d1)) | Liangzu Peng, Juan Elenter, Joshua Agterberg, Alejandro Ribeiro, and René Vidal | International Conference on Learning Representations |
| 78 | 2021 | 1.0 | Towards Costless Model Selection in Contextual Bandits: A Bias-Variance Perspective ([link](https://www.semanticscholar.org/paper/bc9914583a69474df771dafab0d4144d1d517a40)) | Sanath Kumar Krishnamurthy, Adrienne M. Propp, and Susan Athey | International Conference on Artificial Intelligence and Statistics |
| 79 | 2021 | 5.2 | Adapting to misspecification in contextual bandits with offline regression oracles ([link](https://www.semanticscholar.org/paper/6c4f209e2a378d3bc0b33bdb81906a6e6725e2f8)) | Sanath Kumar Krishnamurthy, Vitor Hadad, and S. Athey | ArXiv |
| 80 | 2021 | 1.5 | Improved Algorithms for Misspecified Linear Markov Decision Processes ([link](https://www.semanticscholar.org/paper/1ff7d5cbad5d320c8d4da773095d4bb22d423565)) | Daniel Vial, Advait Parulekar, S. Shakkottai, and R. Srikant | ArXiv |
| 81 | 2020 | 5.7 | Detecting and Adapting to Irregular Distribution Shifts in Bayesian Online Learning ([link](https://www.semanticscholar.org/paper/4b891bc552f51b9396511202d9d6f6c697382126)) | Aodong Li, Alex Boyd, Padhraic Smyth, and S. Mandt | Neural Information Processing Systems |
| 82 | 2006 | 5.0 | A Non-Parametric Bayesian Method for Inferring Hidden Causes ([link](https://www.semanticscholar.org/paper/77d1549b43efe3a89f0c072135924553f37118a5)) | F. Wood, T. Griffiths, and Zoubin Ghahramani | ArXiv |
| 83 | 2023 | 30 | A generative model of memory construction and consolidation ([link](https://doi.org/10.1038/s41562-023-01799-z)) | Eleanor Spens and N. Burgess | Nature Human Behaviour |
| 84 | 2007 |  | Switching between Predictors with an Application in Density Estimation ([link](https://www.semanticscholar.org/paper/fee6e8b6bfd008202590ce83c26cd89ae10967fe)) | Van Erven, D. Rooij, and P. Grünwald |  |
| 85 | 2008 | 0.7 | Approximate predictive state representations ([link](https://doi.org/10.65109/wtqk6477)) | Britton Wolfe, Michael R. James, and Satinder Singh | Adaptive Agents and Multi-Agent Systems |
| 86 | 2015 | 2.6 | Spectral Learning of Predictive State Representations with Insufficient Statistics ([link](https://doi.org/10.1609/aaai.v29i1.9635)) | Alex Kulesza, Nan Jiang, and Satinder Singh | AAAI Conference on Artificial Intelligence |
| 87 | 2000 | 8.4 | Predictability, Complexity, and Learning ([link](https://doi.org/10.1162/089976601753195969)) | W. Bialek, I. Nemenman, and Naftali Tishby | Neural Computation |
| 88 | 2004 | 0.7 | Reductions of Hidden Information Sources ([link](https://doi.org/10.1007/s10955-005-6797-4)) | N. Ay and J. Crutchfield | Journal of Statistical Physics |
| 89 | 2004 | 0.3 | When do differences matter? On-line feature extraction through cognitive economy ([link](https://doi.org/10.1016/j.cogsys.2004.06.005)) | D. Finton | ArXiv |
| 90 | 2026 |  | A Thermodynamic Theory of Learning Part II: Critical Period Closure and Continual Learning Failure ([link](https://doi.org/10.48550/arXiv.2602.07950)) | Daisuke Okanohara | ArXiv |
| 91 | 2024 | 6.5 | Order parameters and phase transitions of continual learning in deep neural networks ([link](https://doi.org/10.1073/pnas.2501899123)) | Haozhe Shan, Qianyi Li, and H. Sompolinsky | Proceedings of the National Academy of Sciences of the United States of America |
| 92 | 2025 |  | On the Theory of Continual Learning with Gradient Descent for Neural Networks ([link](https://doi.org/10.48550/arXiv.2510.05573)) | Hossein Taheri, A. Ghosh, and Arya Mazumdar | ArXiv |
| 93 | 2025 |  | Two-factor synaptic consolidation reconciles robustness with pruning and homeostatic scaling ([link](https://doi.org/10.1073/pnas.2422602122)) | Georgios Iatropoulos, W. Gerstner, and Johanni Brea | Proceedings of the National Academy of Sciences of the United States of America |
| 94 | 2006 | 0.1 | The Momentum Problem in MDL and Bayesian Prediction ([link](https://www.semanticscholar.org/paper/5c817187ca78dc3171853b6fe4ddd0d2999aaca8)) | T. Erven |  |
| 95 | 2023 | 4.8 | Kalman Filter for Online Classification of Non-Stationary Data ([link](https://doi.org/10.48550/arXiv.2306.08448)) | Michalis K. Titsias et al. | ArXiv |
| 96 | 2007 | 1.7 | Dynamic Model Selection With its Applications to Novelty Detection ([link](https://doi.org/10.1109/TIT.2007.896890)) | K. Yamanishi and Y. Maruyama | IEEE Transactions on Information Theory |
| 97 | 2021 |  | Efﬁcient Streaming Inference for Inﬁnite Latent Feature Models ([link](https://www.semanticscholar.org/paper/8feb1c850b773d06d7231136f3af4d9b9b50975e)) |  |  |
| 98 | 2022 |  | Constructing Memory: Consolidation as Teacher-Student Training of a Generative Model ([link](https://www.semanticscholar.org/paper/6ab939fac97b770f045ea17bce0a3697fcb003ea)) | Eleanor Spens and Neil Burgess |  |
| 99 | 2016 | 2.3 | Memory Transformation Enhances Reinforcement Learning in Dynamic Environments ([link](https://doi.org/10.1523/JNEUROSCI.0763-16.2016)) | Adam Santoro, P. Frankland, and B. Richards | The Journal of Neuroscience |
| 100 | 2018 | 25 | Unsupervised Predictive Memory in a Goal-Directed Agent ([link](https://www.semanticscholar.org/paper/c6a5e6a594adcfb8b1a9bb67975ebc439ceab4a9)) | Greg Wayne et al. | ArXiv |
| 101 | 2002 | 9.1 | Model Growth ([link](https://www.semanticscholar.org/paper/eb1da3a0e70ecad7fca3f64265a7a7434cf8849f)) | J. V. Maanen and Marcus Hutter |  |
| 102 | 2016 | 3.5 | Predictive Rate-Distortion for Infinite-Order Markov Processes ([link](https://doi.org/10.1007/s10955-016-1520-1)) | Sarah E. Marzen and J. Crutchfield | Journal of Statistical Physics |
| 103 | 2014 | 0.9 | Circumventing the Curse of Dimensionality in Prediction: Causal Rate-Distortion for Infinite-Order Markov Processes ([link](https://www.semanticscholar.org/paper/5308a461868cde8b8d175eee0de4eea699028d14)) | Sarah E. Marzen and J. Crutchfield | ArXiv |
| 104 | 2006 |  | Simultaneous Learning of Action and Space Hierarchies in Reinforcement Learning ([link](https://www.semanticscholar.org/paper/12e6d20386166840176d3c5a29b902d351452882)) | Mehran Asadi and A. Agah | International Conference on Artificial Intelligence |
| 105 | 2025 |  | On Understanding of the Dynamics of Model Capacity in Continual Learning ([link](https://doi.org/10.48550/arXiv.2508.08052)) | Supriyo Chakraborty and Krishnan Raghavan | ArXiv |
| 106 | 2023 | 1.9 | On the Interplay Between Misspecification and Sub-optimality Gap in Linear Contextual Bandits ([link](https://doi.org/10.48550/arXiv.2303.09390)) | Weitong Zhang, Jiafan He, Zhiyuan Fan, and Quanquan Gu | ArXiv |
| 107 | 2019 | 12 | Continuous Meta-Learning without Tasks ([link](https://www.semanticscholar.org/paper/48e8fa777c89132b82902ffaa2f2c889c494a9a8)) | James Harrison, Apoorva Sharma, Chelsea Finn, and M. Pavone | ArXiv |
| 108 | 2012 | 0.1 | Transfer Learning as Representation Selection ([link](https://www.semanticscholar.org/paper/c73852c058ad25d022b396ed92deb7b58e81f8b6)) | Trung Nguyen-Thanh, T. Silander, and T. Leong |  |
| 109 | 2013 | 1.6 | Regret Minimization for Branching Experts ([link](https://www.semanticscholar.org/paper/a50fccee10dc45a560c05241f14af52c1499aae4)) | Eyal Gofer, Nicolò Cesa-Bianchi, Claudio Gentile, and Yishay Mansour | Annual Conference Computational Learning Theory |
| 110 | 1999 | 2.0 | Predictive Information ([link](https://www.semanticscholar.org/paper/3068a485e76bc6e7d274aa8e7b68ccb979a39a3d)) | W. Bialek and Naftali Tishby |  |
| 111 | 2016 | 0.7 | Dynamic Choice of State Abstraction in Q-Learning ([link](https://doi.org/10.3233/978-1-61499-672-9-46)) | M. Tamassia, Fabio Zambetta, W. Raffe, F. Mueller, and Xiaodong Li | European Conference on Artificial Intelligence |
| 112 | 2019 | 44 | Continual Unsupervised Representation Learning ([link](https://www.semanticscholar.org/paper/5faaa08809c85c7affea0ad49f60528445df5bd5)) | Dushyant Rao et al. | Neural Information Processing Systems |
| 113 | 2012 | 9.3 | Change-Point Detection for High-Dimensional Time Series With Missing Data ([link](https://doi.org/10.1109/JSTSP.2012.2234082)) | Yao Xie, Jiaji Huang, and R. Willett | IEEE Journal of Selected Topics in Signal Processing |
| 114 | 2010 | 0.2 | Multimodeling Control via System Balancing ([link](https://doi.org/10.1155/2010/841830)) | N. Kovačević and D. Škatarić | Mathematical Problems in Engineering |
| 115 | 2002 | 0.1 | Nonlinear robust disturbance rejection ([link](https://doi.org/10.25911/5D514D62F355D)) | B. Harbin |  |

### Paper Details

1\. · 100% match · 2016 · 1.0 cit/yr\
**Episodic memory as a prerequisite for online updates of model structure** ([link](https://www.semanticscholar.org/paper/b0c205c6655e8ab97bbc4ba0dc55ac40218ba830))\
D. G. Nagy and G. Orbán\
*Cognitive Science* · 10 citations

> Human learning in complex environments critically depends on the ability to perform model selection, that is to assess competing hypotheses about the structure of the environment. Importantly, information is accumulated continuously, which necessitates an online process for model selection. While model selection in human learning has been explored extensively, it is unclear how memory systems support learning in an online setting. We formulate a semantic learner and demonstrate that online learning on open model spaces results in a delicate choice between either tracking a possibly infinite number of competing models or retaining experiences in an intact form. Since none of these choices is feasible for a bounded-resource memory system, we propose an episodic learner that retains an optimised subset of experiences in addition to semantic memory. On a simple model system we demonstrate that this normative theory of episodic memory can effectively circumvent the challenge of online model selection.

------------------------------------------------------------------------

2\. · 100% match · 2022 · 3.4 cit/yr\
**Continual learning: a feature extraction formalization, an efficient algorithm, and fundamental obstructions** ([link](https://doi.org/10.48550/arXiv.2203.14383))\
Binghui Peng and Andrej Risteski\
*ArXiv* · Mar 27, 2022 · 14 citations

> Continual learning is an emerging paradigm in machine learning, wherein a model is exposed in an online fashion to data from multiple different distributions (i.e. environments), and is expected to adapt to the distribution change. Precisely, the goal is to perform well in the new environment, while simultaneously retaining the performance on the previous environments (i.e. avoid”catastrophic forgetting”) – without increasing the size of the model. While this setup has enjoyed a lot of attention in the applied community, there hasn’t be theoretical work that even formalizes the desired guarantees. In this paper, we propose a framework for continual learning through the framework of feature extraction – namely, one in which features, as well as a classifier, are being trained with each environment. When the features are linear, we design an efficient gradient-based algorithm $`\mathsf{DPGD}`$, that is guaranteed to perform well on the current environment, as well as avoid catastrophic forgetting. In the general case, when the features are non-linear, we show such an algorithm cannot exist, whether efficient or not.

------------------------------------------------------------------------

3\. · 100% match\
**Continual learning: a feature extraction formalization, an efﬁcient algorithm, and barriers** ([link](https://www.semanticscholar.org/paper/961aa0a0cd41b92aeaf82006d91b18bc1ae84114))\
Binghui Peng and Andrej Risteski\
0 citations

> Continual learning is an emerging paradigm in machine learning, wherein a model is exposed in an online fashion to data from multiple different distributions (i.e. environments), and is expected to adapt to the distribution change. Precisely, the goal is to perform well in the new environment, while simultaneously retaining the performance on the previous environments (i.e. avoid “catastrophic forgetting”). While this setup has enjoyed a lot of attention in the applied community, there hasn’t be theoretical work that even formalizes the desired guarantees. In this paper, we propose a framework for continual learning through the framework of feature extraction—namely, one in which features, as well as a classiﬁer, are being trained with each environment. When the features are linear, we design an efﬁcient gradient-based algorithm DPGrad , that is guaranteed to perform well on the current environment, as well as avoid catastrophic forgetting. In the general case, when the features are non-linear, we show such an algorithm cannot exist, whether efﬁcient or not.

------------------------------------------------------------------------

4\. · 100% match · 2022 · 6.4 cit/yr\
**Memory Bounds for Continual Learning** ([link](https://doi.org/10.1109/FOCS54457.2022.00056))\
Xi Chen, Christos Papadimitriou, and Binghui Peng\
*2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS)* · Apr 22, 2022 · 26 citations

> Continual learning, or lifelong learning, is a formidable current challenge to machine learning. It requires the learner to solve a sequence of k different learning tasks, one after the other, while retaining its aptitude for earlier tasks; the continual learner should scale better than the obvious solution of developing and maintaining a separate learner for each of the k tasks. We embark on a complexity-theoretic study of continual learning in the PAC framework. We make novel uses of communication complexity to establish that any continual learner, even an improper one, needs memory that grows linearly with k, strongly suggesting that the problem is intractable. When logarithmically many passes over the learning tasks are allowed, we provide an algorithm based on multiplicative weights update whose memory requirement scales well; we also establish that improper learning is necessary for such performance. We conjecture that these results may lead to new promising approaches to continual learning.

------------------------------------------------------------------------

5\. · 100% match · 1999 · 19 cit/yr\
**Computational Mechanics: Pattern and Prediction, Structure and Simplicity** ([link](https://doi.org/10.1023/A:1010388907793))\
C. Shalizi and J. Crutchfield\
*Journal of Statistical Physics* · Jul 1, 1999 · 523 citations

> Computational mechanics, an approach to structural complexity, defines a process’s causal states and gives a procedure for finding them. We show that the causal-state representation—an ∈-machine—is the minimal one consistent with accurate prediction. We establish several results on ∈-machine optimality and uniqueness and on how ∈-machines compare to alternative representations. Further results relate measures of randomness and structural complexity obtained from ∈-machines to those from ergodic and information theories.

------------------------------------------------------------------------

6\. · 100% match · 2004 · 9.1 cit/yr\
**Blind Construction of Optimal Nonlinear Recursive Predictors for Discrete Sequences** ([link](https://www.semanticscholar.org/paper/da820634f29f02e10c117fa84857753ded8f0204))\
C. Shalizi and Kristina Lisa Shalizi\
*Conference on Uncertainty in Artificial Intelligence* · Jun 6, 2004 · 199 citations

> We present a new method for nonlinear prediction of discrete random sequences under minimal structural assumptions. We give a mathematical construction for optimal predictors of such processes, in the form of hidden Markov models. We then describe an algorithm, CSSR (Causal-State Splitting Reconstruction), which approximates the ideal predictor from data. We discuss the reliability of CSSR, its data requirements, and its performance in simulations. Finally, we compare our approach to existing methods using variable-length Markov models and cross-validated hidden Markov models, and show theoretically and experimentally that our method delivers results superior to the former and at least comparable to the latter.

------------------------------------------------------------------------

7\. · 100% match · 1983 · 44 cit/yr\
**A UNIVERSAL PRIOR FOR INTEGERS AND ESTIMATION BY MINIMUM DESCRIPTION LENGTH** ([link](https://doi.org/10.1214/AOS/1176346150))\
J. Rissanen\
*Annals of Statistics* · Jun 1, 1983 · 1911 citations

> of the number of bits required to write down the observed data, has been reformulated to extend the classical maximum likelihood principle. The principle permits estimation of the number of the parameters in statistical models in addition to their values and even of the way the parameters appear in the models; i.e., of the model structures. The principle rests on a new way to interpret and construct a universal prior distribution for the integers, which makes sense even when the parameter is an individual object. Truncated realvalued parameters are converted to integers by dividing them by their precision, and their prior is determined from the universal prior for the integers by optimizing the precision. 1. Introduction. In this paper we study estimation based upon the principle of minimizing the total number of binary digits required to rewrite the observed data, when each observation is given with some precision. Instead of attempting at an absolutely shortest description, which would be futile, we look for the optimum relative to a class of parametrically given distributions. This Minimum Description Length (MDL) principle, which we introduced in a less comprehensive form in \[25\], turns out to degenerate to the more familiar Maximum Likelihood (ML) principle in case the number of parameters in the models is fixed, so that the description length of the parameters themselves can be ignored. In another extreme case, where the parameters determine the data, it similarly degenerates to Jaynes’s principle of maximum entropy, \[14\]. But the main power of the new criterion is that it permits estimates of the entire model, its parameters, their number, and even the way the parameters appear in the model; i.e., the model structure. Hence, there will be no need to supplement the estimated parameters with a separate hypothesis test to decide whether a model is adequately parameterized or, perhaps, over parameterized.

------------------------------------------------------------------------

8\. · 100% match · 1984 · 25 cit/yr\
**Universal coding, information, prediction, and estimation** ([link](https://doi.org/10.1109/TIT.1984.1056936))\
J. Rissanen\
*IEEE Trans. Inf. Theory* · Jul 1, 1984 · 1029 citations

> A connection between universal codes and the problems of prediction and statistical estimation is established. A known lower bound for the mean length of universal codes is sharpened and generalized, and optimum universal codes constructed. The bound is defined to give the information in strings relative to the considered class of processes. The earlier derived minimum description length criterion for estimation of parameters, including their number, is given a fundamental information, theoretic justification by showing that its estimators achieve the information in the strings. It is also shown that one cannot do prediction in Gaussian autoregressive moving average (ARMA) processes below a bound, which is determined by the information in the data.

------------------------------------------------------------------------

9\. · 100% match · 2016 · 25 cit/yr\
**Computational principles of synaptic memory consolidation** ([link](https://doi.org/10.1038/nn.4401))\
M. Benna and Stefano Fusi\
*Nature Neuroscience* · Oct 3, 2016 · 236 citations

------------------------------------------------------------------------

10\. · 100% match · 1989 · 50 cit/yr\
**Stochastic Complexity in Statistical Inquiry** ([link](https://doi.org/10.1142/0822))\
J. Rissanen\
*World Scientific Series in Computer Science* · Nov 1, 1989 · 1827 citations

------------------------------------------------------------------------

11\. · 100% match · 2005 · 27 cit/yr\
**Cascade models of synaptically stored memories.** ([link](https://doi.org/10.1016/J.NEURON.2005.02.001))\
Stefano Fusi, P. Drew, and L. Abbott\
*Neuron* · Feb 17, 2005 · 577 citations

------------------------------------------------------------------------

12\. · 100% match · 1995 · 33 cit/yr\
**The context-tree weighting method: basic properties** ([link](https://doi.org/10.1109/18.382012))\
F. Willems, Y. Shtarkov, and T. Tjalkens\
*IEEE Trans. Inf. Theory* · May 1, 1995 · 1014 citations

> Describes a sequential universal data compression procedure for binary tree sources that performs the “double mixture.” Using a context tree, this method weights in an efficient recursive way the coding distributions corresponding to all bounded memory tree sources, and achieves a desirable coding distribution for tree sources with an unknown model and unknown parameters. Computational and storage complexity of the proposed procedure are both linear in the source sequence length. The authors derive a natural upper bound on the cumulative redundancy of the method for individual sequences. The three terms in this bound can be identified as coding, parameter, and model redundancy, The bound holds for all source sequence lengths, not only for asymptotically large lengths. The analysis that leads to this bound is based on standard techniques and turns out to be extremely simple. The upper bound on the redundancy shows that the proposed context-tree weighting procedure is optimal in the sense that it achieves the Rissanen (1984) lower bound. \>

------------------------------------------------------------------------

13\. · 100% match · 1997 · 16 cit/yr\
**Stochastic approximation with two time scales** ([link](https://doi.org/10.1016/S0167-6911(97%2990015-3))\
V. Borkar\
*Systems & Control Letters* · Feb 10, 1997 · 482 citations

------------------------------------------------------------------------

14\. · 100% match · 2007 · 12 cit/yr\
**Limits on the memory storage capacity of bounded synapses** ([link](https://doi.org/10.1038/nn1859))\
Stefano Fusi and L. Abbott\
*Nature Neuroscience* · Mar 11, 2007 · 222 citations

------------------------------------------------------------------------

15\. · 100% match · 2000 · 17 cit/yr\
**The O.D.E. Method for Convergence of Stochastic Approximation and Reinforcement Learning** ([link](https://doi.org/10.1137/S0363012997331639))\
V. Borkar and Sean P. Meyn\
*SIAM J. Control. Optim.* · 446 citations

> It is shown here that stability of the stochastic approximation algorithm is implied by the asymptotic stability of the origin for an associated ODE. This in turn implies convergence of the algorithm. Several specific classes of algorithms are considered as applications. It is found that the results provide (i) a simpler derivation of known results for reinforcement learning algorithms; (ii) a proof for the first time that a class of asynchronous stochastic approximation algorithms are convergent without using any a priori assumption of stability; (iii) a proof for the first time that asynchronous adaptive critic and Q-learning algorithms are convergent for the average cost optimal control problem.

------------------------------------------------------------------------

16\. · 100% match · 2020 · 5.0 cit/yr\
**Optimal forgetting: Semantic compression of episodic memories** ([link](https://doi.org/10.1371/journal.pcbi.1008367))\
D. G. Nagy, B. Török, and G. Orbán\
*PLoS Computational Biology* · May 8, 2020 · 30 citations

> It has extensively been documented that human memory exhibits a wide range of systematic distortions, which have been associated with resource constraints. Resource constraints on memory can be formalised in the normative framework of lossy compression, however traditional lossy compression algorithms result in qualitatively different distortions to those found in experiments with humans. We argue that the form of distortions is characteristic of relying on a generative model adapted to the environment for compression. We show that this semantic compression framework can provide a unifying explanation of a wide variety of memory phenomena. We harness recent advances in learning deep generative models, that yield powerful tools to approximate generative models of complex data. We use three datasets, chess games, natural text, and hand-drawn sketches, to demonstrate the effects of semantic compression on memory performance. Our model accounts for memory distortions related to domain expertise, gist-based distortions, contextual effects, and delayed recall. Author summary Human memory performs surprisingly poorly in many everyday tasks, which have been richly documented in laboratory experiments. While constraints on memory resources necessarily imply a loss of information, it is possible to do well or badly in relation to available memory resources. In this paper we recruit information theory, which establishes how to optimally lose information based on prior and complete knowledge of environmental statistics. For this, we address two challenges. 1, The environmental statistics is not known for the brain, rather these have to be learned over time from limited observations. 2, Information theory does not specify how different distortions of original experiences should be penalised. In this paper we tackle these challenges by assuming that a latent variable generative model of the environment is maintained in semantic memory. We show that compression of experiences through a generative model gives rise to systematic distortions that qualitatively correspond to a diverse range of observations in the experimental literature.

------------------------------------------------------------------------

17\. · 100% match · 1986 · 66 cit/yr\
**Singular perturbation methods in control : analysis and design** ([link](https://doi.org/10.1137/1.9781611971118))\
P. Kokotovic, H. Khalil, and J. O’Reilly\
2659 citations

> From the Publisher: Singular perturbations and time-scale techniques were introduced to control engineering in the late 1960s and have since become common tools for the modeling, analysis, and design of control systems. In this SIAM Classics edition of the 1986 book, the original text is reprinted in its entirety (along with a new preface), providing once again the theoretical foundation for representative control applications. This book continues to be essential in many ways. It lays down the foundation of singular perturbation theory for linear and nonlinear systems, it presents the methodology in a pedagogical way that is not available anywhere else, and it illustrates the theory with many solved examples, including various physical examples and applications. So while new developments may go beyond the topics covered in this book, they are still based on the methodology described here, which continues to be their common starting point. Audience Control engineers and graduate students who seek an introduction to singular perturbation methods in control will find this text useful. The book also provides research workers with sketches of problems in the areas of robust, adaptive, stochastic, and nonlinear control. No previous knowledge of singular perturbation techniques is assumed. About the Authors Petar Kokotovic is Director of the Center for Control Engineering and Computation at the University of California, Santa Barbara. Hassan K. Khalil is Professor of Electrical and Computer Engineering at Michigan State University. John O’Reilly is Professor of Electronics and Electrical Engineering at the University of Glasgow, Scotland.

------------------------------------------------------------------------

18\. · 100% match · 2000 · 165 cit/yr\
**The information bottleneck method** ([link](https://www.semanticscholar.org/paper/4ef483f819e11873822416042a4b6dc4652e010c))\
Naftali Tishby, Fernando C Pereira, and W. Bialek\
*ArXiv* · Apr 24, 2000 · 4311 citations

> We define the relevant information in a signal $`x\in X`$ as being the information that this signal provides about another signal $`y\in \Y`$. Examples include the information that face images provide about the names of the people portrayed, or the information that speech sounds provide about the words spoken. Understanding the signal $`x`$ requires more than just predicting $`y`$, it also requires specifying which features of $`\X`$ play a role in the prediction. We formalize this problem as that of finding a short code for $`\X`$ that preserves the maximum information about $`\Y`$. That is, we squeeze the information that $`\X`$ provides about $`\Y`$ through a \`bottleneck’ formed by a limited set of codewords $`\tX`$. This constrained optimization problem can be seen as a generalization of rate distortion theory in which the distortion measure $`d(x,\x)`$ emerges from the joint statistics of $`\X`$ and $`\Y`$. This approach yields an exact set of self consistent equations for the coding rules $`X \to \tX`$ and $`\tX \to \Y`$. Solutions to these equations can be found by a convergent re-estimation method that generalizes the Blahut-Arimoto algorithm. Our variational principle provides a surprisingly rich framework for discussing a variety of problems in signal processing and learning, as will be described in detail elsewhere.

------------------------------------------------------------------------

19\. · 100% match · 1993 · 6.6 cit/yr\
**Overcoming Incomplete Perception with Utile Distinction Memory** ([link](https://doi.org/10.1016/b978-1-55860-307-3.50031-9))\
A. McCallum\
*International Conference on Machine Learning* · Jun 27, 1993 · 216 citations

------------------------------------------------------------------------

20\. · 100% match · 2021 · 20 cit/yr\
**Adapting to Misspecification in Contextual Bandits** ([link](https://www.semanticscholar.org/paper/0979cb2939a71873542a4a7f34990bfbd1071f9c))\
Dylan J. Foster, C. Gentile, M. Mohri, and Julian Zimmert\
*ArXiv* · Jul 12, 2021 · 99 citations

> A major research direction in contextual bandits is to develop algorithms that are computationally efficient, yet support flexible, general-purpose function approximation. Algorithms based on modeling rewards have shown strong empirical performance, but typically require a well-specified model, and can fail when this assumption does not hold. Can we design algorithms that are efficient and flexible, yet degrade gracefully in the face of model misspecification? We introduce a new family of oracle-efficient algorithms for $`\varepsilon`$-misspecified contextual bandits that adapt to unknown model misspecification – both for finite and infinite action settings. Given access to an online oracle for square loss regression, our algorithm attains optimal regret and – in particular – optimal dependence on the misspecification level, with no prior knowledge. Specializing to linear contextual bandits with infinite actions in $`d`$ dimensions, we obtain the first algorithm that achieves the optimal $`O(d\sqrt{T} + \varepsilon\sqrt{d}T)`$ regret bound for unknown misspecification level $`\varepsilon`$. On a conceptual level, our results are enabled by a new optimization-based perspective on the regression oracle reduction framework of Foster and Rakhlin, which we anticipate will find broader use.

------------------------------------------------------------------------

21\. · 100% match · 2013 · 5.8 cit/yr\
**Efficient Partitioning of Memory Systems and Its Importance for Memory Consolidation** ([link](https://doi.org/10.1371/journal.pcbi.1003146))\
Alex Roxin and Stefano Fusi\
*PLoS Computational Biology* · Jul 1, 2013 · 75 citations

> Long-term memories are likely stored in the synaptic weights of neuronal networks in the brain. The storage capacity of such networks depends on the degree of plasticity of their synapses. Highly plastic synapses allow for strong memories, but these are quickly overwritten. On the other hand, less labile synapses result in long-lasting but weak memories. Here we show that the trade-off between memory strength and memory lifetime can be overcome by partitioning the memory system into multiple regions characterized by different levels of synaptic plasticity and transferring memory information from the more to less plastic region. The improvement in memory lifetime is proportional to the number of memory regions, and the initial memory strength can be orders of magnitude larger than in a non-partitioned memory system. This model provides a fundamental computational reason for memory consolidation processes at the systems level.

------------------------------------------------------------------------

22\. · 100% match · 2017 · 8.0 cit/yr\
**Misspecified Linear Bandits** ([link](https://doi.org/10.1609/aaai.v31i1.11052))\
Avishek Ghosh, Sayak Ray Chowdhury, and Aditya Gopalan\
*ArXiv* · Feb 12, 2017 · 74 citations

> We consider the problem of online learning in misspecified linear stochastic multi-armed bandit problems. Regret guarantees for state-of-the-art linear bandit algorithms such as Optimism in the Face of Uncertainty Linear bandit (OFUL) hold under the assumption that the arms expected rewards are perfectly linear in their features. It is, however, of interest to investigate the impact of potential misspecification in linear bandit models, where the expected rewards are perturbed away from the linear subspace determined by the arms features. Although OFUL has recently been shown to be robust to relatively small deviations from linearity, we show that any linear bandit algorithm that enjoys optimal regret performance in the perfectly linear setting (e.g., OFUL) must suffer linear regret under a sparse additive perturbation of the linear model. In an attempt to overcome this negative result,we define a natural class of bandit models characterized by a non-sparse deviation from linearity. We argue that the OFUL algorithm can fail to achieve sublinear regret even under models that have non-sparse deviation. We finally develop a novel bandit algorithm, comprising a hypothesis test for linearity followed by a decision to use either the OFUL or Upper Confidence Bound (UCB) algorithm. For perfectly linear bandit models, the algorithm provably exhibits OFULs favorable regret performance, while for misspecified models satisfying the non-sparse deviation property, the algorithm avoids the linear regret phenomenon and falls back on UCBs sublinear regret scaling. Numerical experiments on synthetic data, and on recommendation data from the public Yahoo! Learning toRank Challenge dataset, empirically support our findings.

------------------------------------------------------------------------

23\. · 100% match · 2019 · 13 cit/yr\
**Finite-Time Performance Bounds and Adaptive Learning Rate Selection for Two Time-Scale Reinforcement Learning** ([link](https://www.semanticscholar.org/paper/8cba38e7e2a4b6400c0dbb7a0c2c98918e354d57))\
Harsh Gupta, R. Srikant, and Lei Ying\
*ArXiv* · Jul 14, 2019 · 91 citations

> We study two time-scale linear stochastic approximation algorithms, which can be used to model well-known reinforcement learning algorithms such as GTD, GTD2, and TDC. We present finite-time performance bounds for the case where the learning rate is fixed. The key idea in obtaining these bounds is to use a Lyapunov function motivated by singular perturbation theory for linear differential equations. We use the bound to design an adaptive learning rate scheme which significantly improves the convergence rate over the known optimal polynomial decay rule in our experiments, and can be used to potentially improve the performance of any other schedule where the learning rate is changed at pre-determined time instants.

------------------------------------------------------------------------

24\. · 100% match · 2007 · 46 cit/yr\
**The Minimum Description Length Principle (Adaptive Computation and Machine Learning)** ([link](https://doi.org/10.7551/mitpress/4643.001.0001))\
P. Grünwald\
Mar 23, 2007 · 886 citations

> The minimum description length (MDL) principle is a powerful method of inductive inference, the basis of statistical modeling, pattern recognition, and machine learning. It holds that the best explanation, given a limited set of observed data, is the one that permits the greatest compression of the data. MDL methods are particularly well-suited for dealing with model selection, prediction, and estimation problems in situations where the models under consideration can be arbitrarily complex, and overfitting the data is a serious concern. This extensive, step-by-step introduction to the MDL Principle provides a comprehensive reference (with an emphasis on conceptual issues) that is accessible to graduate students and researchers in statistics, pattern classification, machine learning, and data mining, to philosophers interested in the foundations of statistics, and to researchers in other applied sciences that involve model selection, including biology, econometrics, and experimental psychology. Part I provides a basic introduction to MDL and an overview of the concepts in statistics and information theory needed to understand MDL. Part II treats universal coding, the information-theoretic notion on which MDL is built, and part III gives a formal treatment of MDL theory as a theory of inductive inference based on universal coding. Part IV provides a comprehensive overview of the statistical theory of exponential families with an emphasis on their information-theoretic properties. The text includes a number of summaries, paragraphs offering the reader a “fast track” through the material, and boxes highlighting the most important concepts.

------------------------------------------------------------------------

25\. · 100% match · 1997 · 47 cit/yr\
**Adaptive control using multiple models** ([link](https://doi.org/10.1109/9.554398))\
K. Narendra and Jeyendran Balakrishnan\
*IEEE Trans. Autom. Control.* · Feb 1, 1997 · 1387 citations

> Intelligent control may be viewed as the ability of a controller to operate in multiple environments by recognizing which environment is currently in existence and servicing it appropriately. An important prerequisite for an intelligent controller is the ability to adapt rapidly to any unknown but constant operating environment. This paper presents a general methodology for such adaptive control using multiple models, switching, and tuning. The approach was first introduced by Narendra et al. (1992) for improving the transient response of adaptive systems in a stable fashion. This paper proposes different switching and tuning schemes for adaptive control which combine fixed and adaptive models in novel ways. The principal mathematical results are the proofs of stability when these different schemes are used in the context of model reference control of an unknown linear time-invariant system. A variety of simulation results are presented to demonstrate the efficacy of the proposed methods.

------------------------------------------------------------------------

26\. · 100% match · 2020 · 3.5 cit/yr\
**Hebbian plasticity in parallel synaptic pathways: A circuit mechanism for systems memory consolidation** ([link](https://doi.org/10.1371/journal.pcbi.1009681))\
M. Remme et al.\
*PLoS Computational Biology* · Dec 4, 2020 · 19 citations

> Systems memory consolidation involves the transfer of memories across brain regions and the transformation of memory content. For example, declarative memories that transiently depend on the hippocampal formation are transformed into long-term memory traces in neocortical networks, and procedural memories are transformed within cortico-striatal networks. These consolidation processes are thought to rely on replay and repetition of recently acquired memories, but the cellular and network mechanisms that mediate the changes of memories are poorly understood. Here, we suggest that systems memory consolidation could arise from Hebbian plasticity in networks with parallel synaptic pathways — two ubiquitous features of neural circuits in the brain. We explore this hypothesis in the context of hippocampus-dependent memories. Using computational models and mathematical analyses, we illustrate how memories are transferred across circuits and discuss why their representations could change. The analyses suggest that Hebbian plasticity mediates consolidation by transferring a linear approximation of a previously acquired memory into a parallel pathway. Our modelling results are further in quantitative agreement with lesion studies in rodents. Moreover, a hierarchical iteration of the mechanism yields power-law forgetting — as observed in psychophysical studies in humans. The predicted circuit mechanism thus bridges spatial scales from single cells to cortical areas and time scales from milliseconds to years. Author summary After new memories are acquired, they can be transferred over time into other brain areas — a process called systems memory consolidation. For example, new declarative memories, which refer to the conscious memory of facts and events, depend on the hippocampus. Older declarative memories, however, also rely on neocortical networks. The cellular mechanisms underlying such a transfer are poorly understood. In this work, we show that a simple and in the brain ubiquitous connectivity pattern, combined with a standard learning rule, leads to gradual memory transfer. We illustrate our proposed mechanism in numerical simulations and mathematical analyses. At the neurophysiological level, our theory explains experimental findings on memory storage in the hippocampal formation when specific pathways between neural populations are disrupted. At the psychophysical level, we can account for the power-law forgetting curves typically found in humans. A consequence of the proposed model is that consolidated memories can yield faster responses because they are stored in increasingly shorter synaptic pathways between sensory and motor areas. By giving a mechanistic explanation of the consolidation process, we contribute to the understanding of the transfer of memories and the reorganization of memories over time.

------------------------------------------------------------------------

27\. · 100% match · 1992 · 0.7 cit/yr\
**First Results with Utile Distinction Memory for Reinforcement Learning** ([link](https://www.semanticscholar.org/paper/67eb2366790a9d5efb66001833f6bea8141b3472))\
R. A. McCallum\
Dec 1, 1992 · 22 citations

> This report presents a method by which a reinforcement learning agent can solve the incomplete perception problem using memory. The agent uses a Hidden Markov Model (HMM) to represent its internal state space and creates memory capacity by splitting states of the HMM. The key idea is a test to determine when and how a state should be split: the agent only splits a state when the split will help the agent predict utility. Thus the agent can build an internal state space proportionate to the task at hand, not as large as would be required to represent all of its perceivable world. I call the technique UDM, for Utile Distinction Memory.

------------------------------------------------------------------------

28\. · 100% match · 2001 · 24 cit/yr\
**Predictive Representations of State** ([link](https://www.semanticscholar.org/paper/4a7de0669fd835b2efcab97c7d3dc28ea7a1e6a3))\
M. Littman, R. Sutton, and Satinder Singh\
*Neural Information Processing Systems* · Jan 3, 2001 · 600 citations

> We show that states of a dynamical system can be usefully represented by multi-step, action-conditional predictions of future observations. State representations that are grounded in data in this way may be easier to learn, generalize better, and be less dependent on accurate prior models than, for example, POMDP state representations. Building on prior work by Jaeger and by Rivest and Schapire, in this paper we compare and contrast a linear specialization of the predictive approach with the state representations used in POMDPs and in k-order Markov models. Ours is the first specific formulation of the predictive idea that includes both stochasticity and actions (controls). We show that any system has a linear predictive state representation with number of predictions no greater than the number of states in its minimal POMDP model.

------------------------------------------------------------------------

29\. · 100% match · 2020 · 11 cit/yr\
**Nonlinear Two-Time-Scale Stochastic Approximation: Convergence and Finite-Time Performance** ([link](https://doi.org/10.1109/TAC.2022.3210147))\
Thinh T. Doan\
*IEEE Transactions on Automatic Control* · Nov 3, 2020 · 60 citations

> Two-time-scale stochastic approximation, a generalized version of the popular stochastic approximation, has found broad applications in many areas including stochastic control, optimization, and machine learning. Despite its popularity, theoretical guarantees of this method, especially its finite-time performance, are mostly achieved for the linear case while the results for the nonlinear counterpart are very sparse. Motivated by the classic control theory for singularly perturbed systems, we study in this article the asymptotic convergence and finite-time analysis of the nonlinear two-time-scale stochastic approximation. Under some fairly standard assumptions, we provide a formula that explicitly characterizes the rate of convergence of the main iterates to the desired solutions. In particular, we show that the mean square error generated by the method convergences to zero at a rate \<inline-formula\>\<tex-math notation=“LaTeX”\>$`{\mathcal O}(1/k^{2/3})`$\</tex-math\>\</inline-formula\>, where \<inline-formula\>\<tex-math notation=“LaTeX”\>$`k`$\</tex-math\>\</inline-formula\> is the number of iterations. The key idea in our analysis is to properly choose the two step sizes to characterize the coupling between the fast and slow time-scale iterates.

------------------------------------------------------------------------

30\. · 100% match · 2021 · 17 cit/yr\
**Organizing memories for generalization in complementary learning systems** ([link](https://doi.org/10.1038/s41593-023-01382-9))\
Weinan Sun, Madhu S. Advani, N. Spruston, Andrew M. Saxe, and James E. Fitzgerald\
*Nature Neuroscience* · Oct 15, 2021 · 78 citations

> Memorization and generalization are complementary cognitive processes that jointly promote adaptive behavior. For example, animals should memorize safe routes to specific water sources and generalize from these memories to discover environmental features that predict new ones. These functions depend on systems consolidation mechanisms that construct neocortical memory traces from hippocampal precursors, but why systems consolidation only applies to a subset of hippocampal memories is unclear. Here we introduce a new neural network formalization of systems consolidation that reveals an overlooked tension—unregulated neocortical memory transfer can cause overfitting and harm generalization in an unpredictable world. We resolve this tension by postulating that memories only consolidate when it aids generalization. This framework accounts for partial hippocampal–cortical memory transfer and provides a normative principle for reconceptualizing numerous observations in the field. Generalization-optimized systems consolidation thus provides new insight into how adaptive behavior benefits from complementary learning systems specialized for memorization and generalization. The authors derive a neural network theory of systems consolidation to assess why some memories consolidate more than others. They propose that brains regulate consolidation to optimize generalization, so only predictable memory components consolidate.

------------------------------------------------------------------------

31\. · 100% match · 2018 · 0.9 cit/yr\
**Semantic compression of episodic memories** ([link](https://doi.org/10.32470/ccn.2018.1050-0))\
D. G. Nagy, B. Török, and G. Orbán\
*arXiv: Neurons and Cognition* · Jun 20, 2018 · 7 citations

> Storing knowledge of an agent’s environment in the form of a probabilistic generative model has been established as a crucial ingredient in a multitude of cognitive tasks. Perception has been formalised as probabilistic inference over the state of latent variables, whereas in decision making the model of the environment is used to predict likely consequences of actions. Such generative models have earlier been proposed to underlie semantic memory but it remained unclear if this model also underlies the efficient storage of experiences in episodic memory. We formalise the compression of episodes in the normative framework of information theory and argue that semantic memory provides the distortion function for compression of experiences. Recent advances and insights from machine learning allow us to approximate semantic compression in naturalistic domains and contrast the resulting deviations in compressed episodes with memory errors observed in the experimental literature on human memory.

------------------------------------------------------------------------

32\. · 100% match · 2014 · 8.0 cit/yr\
**Statistical Computations Underlying the Dynamics of Memory Updating** ([link](https://doi.org/10.1371/journal.pcbi.1003939))\
S. Gershman, Angela Radulescu, K. Norman, and Y. Niv\
*PLoS Computational Biology* · Nov 1, 2014 · 92 citations

> Psychophysical and neurophysiological studies have suggested that memory is not simply a carbon copy of our experience: Memories are modified or new memories are formed depending on the dynamic structure of our experience, and specifically, on how gradually or abruptly the world changes. We present a statistical theory of memory formation in a dynamic environment, based on a nonparametric generalization of the switching Kalman filter. We show that this theory can qualitatively account for several psychophysical and neural phenomena, and present results of a new visual memory experiment aimed at testing the theory directly. Our experimental findings suggest that humans can use temporal discontinuities in the structure of the environment to determine when to form new memory traces. The statistical perspective we offer provides a coherent account of the conditions under which new experience is integrated into an old memory versus forming a new memory, and shows that memory formation depends on inferences about the underlying structure of our experience.

------------------------------------------------------------------------

33\. · 100% match · 2019 · 28 cit/yr\
**Learning with Good Feature Representations in Bandits and in RL with a Generative Model** ([link](https://www.semanticscholar.org/paper/57e72da5765157f72e216054f64280dbf3f8d865))\
Tor Lattimore and Csaba Szepesvari\
*International Conference on Machine Learning* · Nov 18, 2019 · 182 citations

> The construction by Du et al. (2019) implies that even if a learner is given linear features in $`\mathbb R^d`$ that approximate the rewards in a bandit with a uniform error of $`\epsilon`$, then searching for an action that is optimal up to $`O(\epsilon)`$ requires examining essentially all actions. We use the Kiefer-Wolfowitz theorem to prove a positive result that by checking only a few actions, a learner can always find an action that is suboptimal with an error of at most $`O(\epsilon \sqrt{d})`$. Thus, features are useful when the approximation error is small relative to the dimensionality of the features. The idea is applied to stochastic bandits and reinforcement learning with a generative model where the learner has access to $`d`$-dimensional linear features that approximate the action-value functions for all policies to an accuracy of $`\epsilon`$. For linear bandits, we prove a bound on the regret of order $`\sqrt{dn \log(k)} + \epsilon n \sqrt{d} \log(n)`$ with $`k`$ the number of actions and $`n`$ the horizon. For RL we show that approximate policy iteration can learn a policy that is optimal up to an additive error of order $`\epsilon \sqrt{d}/(1 - \gamma)^2`$ and using $`d/(\epsilon^2(1 - \gamma)^4)`$ samples from a generative model. These bounds are independent of the finer details of the features. We also investigate how the structure of the feature set impacts the tradeoff between sample complexity and estimation error.

------------------------------------------------------------------------

34\. · 100% match · 2004 · 14 cit/yr\
**Predictive State Representations: A New Theory for Modeling Dynamical Systems** ([link](https://www.semanticscholar.org/paper/532c61a2af5cde64628d0cdd2ba0823800118d0f))\
Satinder Singh, Michael R. James, and Matthew R. Rudary\
*Conference on Uncertainty in Artificial Intelligence* · Jul 7, 2004 · 298 citations

> Modeling dynamical systems, both for control purposes and to make predictions about their behavior, is ubiquitous in science and engineering. Predictive state representations (PSRs) are a recently introduced class of models for discrete-time dynamical systems. The key idea behind PSRs and the closely related OOMs (Jaeger’s observable operator models) is to represent the state of the system as a set of predictions of observable outcomes of experiments one can do in the system. This makes PSRs rather different from history-based models such as nth-order Markov models and hidden-state-based models such as HMMs and POMDPs. We introduce an interesting construct, the system-dynamics matrix, and show how PSRs can be derived simply from it. We also use this construct to show formally that PSRs are more general than both nth-order Markov models and HMMs/POMDPs. Finally, we discuss the main difference between PSRs and OOMs and conclude with directions for future work.

------------------------------------------------------------------------

35\. · 100% match · 2009 · 5.2 cit/yr\
**Past-future information bottleneck in dynamical systems.** ([link](https://doi.org/10.1103/PHYSREVE.79.041925))\
F. Creutzig, A. Globerson, and Naftali Tishby\
*Physical review. E, Statistical, nonlinear, and soft matter physics* · Apr 27, 2009 · 88 citations

> Biological systems need to process information in real time and must trade off accuracy of presentation and coding costs. Here we operationalize this trade-off and develop an information-theoretic framework that selectively extracts information of the input past that is predictive about the output future, obtaining a generalized eigenvalue problem. Thereby, we unravel the input history in terms of structural phase transitions corresponding to additional dimensions of a state space. We elucidate the relation to canonical correlation analysis and give a numerical example. Altogether, this work relates information-theoretic optimization to the joint problem of system identification and model reduction.

------------------------------------------------------------------------

36\. · 100% match · 2020 · 10 cit/yr\
**Regret Bound Balancing and Elimination for Model Selection in Bandits and RL** ([link](https://www.semanticscholar.org/paper/560f6277f345d6a3aa0004b1bb2b8e7e8fe985df))\
Aldo Pacchiano, Christoph Dann, C. Gentile, and P. Bartlett\
*ArXiv* · Dec 24, 2020 · 55 citations

> We propose a simple model selection approach for algorithms in stochastic bandit and reinforcement learning problems. As opposed to prior work that (implicitly) assumes knowledge of the optimal regret, we only require that each base algorithm comes with a candidate regret bound that may or may not hold during all rounds. In each round, our approach plays a base algorithm to keep the candidate regret bounds of all remaining base algorithms balanced, and eliminates algorithms that violate their candidate bound. We prove that the total regret of this approach is bounded by the best valid candidate regret bound times a multiplicative factor. This factor is reasonably small in several applications, including linear bandits and MDPs with nested function classes, linear bandits with unknown misspecification, and LinUCB applied to linear bandits with different confidence parameters. We further show that, under a suitable gap-assumption, this factor only scales with the number of base algorithms and not their complexity when the number of rounds is large enough. Finally, unlike recent efforts in model selection for linear stochastic bandits, our approach is versatile enough to also cover cases where the context information is generated by an adversarial environment, rather than a stochastic one.

------------------------------------------------------------------------

37\. · 100% match · 2017\
**Episodic memory for continual model learning** ([link](https://www.semanticscholar.org/paper/68d538f7cbb7f1b3f0158c4b53bbb9c919359de6))\
D. G. Nagy and G. Orbán\
*ArXiv* · Dec 4, 2017 · 0 citations

> Both the human brain and artificial learning agents operating in real-world or comparably complex environments are faced with the challenge of online model selection. In principle this challenge can be overcome: hierarchical Bayesian inference provides a principled method for model selection and it converges on the same posterior for both off-line (i.e. batch) and online learning. However, maintaining a parameter posterior for each model in parallel has in general an even higher memory cost than storing the entire data set and is consequently clearly unfeasible. Alternatively, maintaining only a limited set of models in memory could limit memory requirements. However, sufficient statistics for one model will usually be insufficient for fitting a different kind of model, meaning that the agent loses information with each model change. We propose that episodic memory can circumvent the challenge of limited memory-capacity online model selection by retaining a selected subset of data points. We design a method to compute the quantities necessary for model selection even when the data is discarded and only statistics of one (or few) learnt models are available. We demonstrate on a simple model that a limited-sized episodic memory buffer, when the content is optimised to retain data with statistics not matching the current representation, can resolve the fundamental challenge of online model selection.

------------------------------------------------------------------------

38\. · 100% match · 2013 · 4.7 cit/yr\
**A memory frontier for complex synapses** ([link](https://www.semanticscholar.org/paper/75c7ec96aaa5d271d541466e5d5a7807e815b488))\
Subhaneil Lahiri and S. Ganguli\
*Neural Information Processing Systems* · Dec 5, 2013 · 58 citations

> An incredible gulf separates theoretical models of synapses, often described solely by a single scalar value denoting the size of a postsynaptic potential, from the immense complexity of molecular signaling pathways underlying real synapses. To understand the functional contribution of such molecular complexity to learning and memory, it is essential to expand our theoretical conception of a synapse from a single scalar to an entire dynamical system with many internal molecular functional states. Moreover, theoretical considerations alone demand such an expansion; network models with scalar synapses assuming finite numbers of distinguishable synaptic strengths have strikingly limited memory capacity. This raises the fundamental question, how does synaptic complexity give rise to memory? To address this, we develop new mathematical theorems elucidating the relationship between the structural organization and memory properties of complex synapses that are themselves molecular networks. Moreover, in proving such theorems, we uncover a framework, based on first passage time theory, to impose an order on the internal states of complex synaptic models, thereby simplifying the relationship between synaptic structure and function.

------------------------------------------------------------------------

39\. · 100% match · 2017 · 0.4 cit/yr\
**Dynamic-Depth Context Tree Weighting** ([link](https://www.semanticscholar.org/paper/8ba7fa658f1fe795a5c1a5ee1f2de36a61658be5))\
J. Messias and Shimon Whiteson\
*Neural Information Processing Systems* · 4 citations

> Reinforcement learning (RL) in partially observable settings is challenging because the agent’s observations are not Markov. Recently proposed methods can learn variable-order Markov models of the underlying process but have steep memory requirements and are sensitive to aliasing between observation histories due to sensor noise. This paper proposes dynamic-depth context tree weighting (D2-CTW), a model-learning method that addresses these limitations. D2-CTW dynamically expands a suffix tree while ensuring that the size of the model, but not its depth, remains bounded. We show that D2-CTW approximately matches the performance of state-of-the-art alternatives at stochastic time-series prediction while using at least an order of magnitude less memory. We also apply D2-CTW to model-based RL, showing that, on tasks that require memory of past observations, D2-CTW can learn without prior knowledge of a good state representation, or even the length of history upon which such a representation should depend.

------------------------------------------------------------------------

40\. · 100% match · 2017\
**Utile Context Tree Weighting** ([link](https://www.semanticscholar.org/paper/7ec7c868d98101b304756b86d914684ebd93bb07))\
J. Messias and Shimon Whiteson\
*Neural Information Processing Systems* · 0 citations

> Reinforcement learning (RL) in partially observable settings is challenging because the agent’s immediate observations are not Markov. Recently proposed methods can learn variable-order Markov models of the underlying process but have steep memory requirements and are sensitive to aliasing between observation histories due to sensor noise. This paper proposes utile context tree weighting (UCTW), a model-learning method that addresses these limitations. UCTW dynamically expands a suffix tree while ensuring that the total size of the model, but not its depth, remains bounded. We show that UCTW approximately matches the performance of state-of-the-art alternatives at stochastic time-series prediction while using at least an order of magnitude less memory. We also apply UCTW to model-based RL, showing that, on tasks that require memory of past observations, UCTW can learn without prior knowledge of a good state representation, or even the length of history upon which such a representation should depend.

------------------------------------------------------------------------

41\. · 100% match · 2021 · 1.3 cit/yr\
**Multi Timescale Stochastic Approximation: Stability and Convergence** ([link](https://www.semanticscholar.org/paper/589bfa87d5e5cb1d6a3d7fad4faa2bbb20140212))\
Rohan Deb, Swetha Ganesh, and S. Bhatnagar\
Dec 7, 2021 · 6 citations

> This paper presents the first sufficient conditions that guarantee the stability and almost sure convergence of multi-timescale stochastic approximation (SA) iterates. It extends the existing results on one-timescale and two-timescale SA iterates to general $`N`$-timescale stochastic recursions, for any $`N \geq 1`$, using the ordinary differential equation (ODE) method. As an application, we study SA algorithms augmented with heavy-ball momentum in the context of Gradient Temporal Difference (GTD) learning. The added momentum introduces an auxiliary state evolving on an intermediate timescale, yielding a three-timescale recursion. We show that with appropriate momentum parameters, the scheme fits within our framework and converges almost surely to the same fixed point as baseline GTD. The stability and convergence of all iterates including the momentum state follow from our main results without ad hoc bounds. We then study off-policy actor-critic algorithms with a baseline learner, actor, and critic updated on separate timescales. In contrast to prior work, we eliminate projection steps from the actor update and instead use our framework to guarantee stability and almost sure convergence of all components. Finally, we extend the analysis to constrained policy optimization in the average reward setting, where the actor, critic, and dual variables evolve on three distinct timescales, and we verify that the resulting dynamics satisfy the conditions of our general theorem. These examples show how diverse reinforcement learning algorithms covering momentum acceleration, off-policy learning, and primal-dual methods-fit naturally into the proposed multi-timescale framework.

------------------------------------------------------------------------

42\. · 100% match · 1989 · 134 cit/yr\
**Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem** ([link](https://doi.org/10.1016/S0079-7421(08%2960536-8))\
M. McCloskey and N. J. Cohen\
*Psychology of Learning and Motivation* · 5006 citations

------------------------------------------------------------------------

43\. · 100% match · 2020 · 7.1 cit/yr\
**Online Model Selection for Reinforcement Learning with Function Approximation** ([link](https://www.semanticscholar.org/paper/cb40cc80be6db8da552c1ecfc3ad2edbd2c2f0e7))\
Jonathan Lee, Aldo Pacchiano, Vidya Muthukumar, Weihao Kong, and E. Brunskill\
*International Conference on Artificial Intelligence and Statistics* · Nov 19, 2020 · 39 citations

> Deep reinforcement learning has achieved impressive successes yet often requires a very large amount of interaction data. This result is perhaps unsurprising, as using complicated function approximation often requires more data to fit, and early theoretical results on linear Markov decision processes provide regret bounds that scale with the dimension of the linear approximation. Ideally, we would like to automatically identify the minimal dimension of the approximation that is sufficient to encode an optimal policy. Towards this end, we consider the problem of model selection in RL with function approximation, given a set of candidate RL algorithms with known regret guarantees. The learner’s goal is to adapt to the complexity of the optimal algorithm without knowing it \textit{a priori}. We present a meta-algorithm that successively rejects increasingly complex models using a simple statistical test. Given at least one candidate that satisfies realizability, we prove the meta-algorithm adapts to the optimal complexity with $`\tilde{O}(L^{5/6} T^{2/3})`$ regret compared to the optimal candidate’s $`\tilde{O}(\sqrt T)`$ regret, where $`T`$ is the number of episodes and $`L`$ is the number of algorithms. The dimension and horizon dependencies remain optimal with respect to the best candidate, and our meta-algorithmic approach is flexible to incorporate multiple candidate algorithms and models. Finally, we show that the meta-algorithm automatically admits significantly improved instance-dependent regret bounds that depend on the gaps between the maximal values attainable by the candidates.

------------------------------------------------------------------------

44\. · 100% match · 2015 · 1.6 cit/yr\
**Computational principles of biological memory** ([link](https://www.semanticscholar.org/paper/2e9902cbdb8317365655beeafae25d4ae2f69372))\
M. Benna and Stefano Fusi\
*arXiv: Neurons and Cognition* · Jul 27, 2015 · 17 citations

> Memories are stored, retained, and recollected through complex, coupled processes operating on multiple timescales. To understand the computational principles behind these intricate networks of interactions we construct a broad class of synaptic models that efficiently harnesses biological complexity to preserve numerous memories. The memory capacity scales almost linearly with the number of synapses, which is a substantial improvement over the square root scaling of previous models. This was achieved by combining multiple dynamical processes that initially store memories in fast variables and then progressively transfer them to slower variables. Importantly, the interactions between fast and slow variables are bidirectional. The proposed models are robust to parameter perturbations and can explain several properties of biological memory, including delayed expression of synaptic modifications, metaplasticity, and spacing effects.

------------------------------------------------------------------------

45\. · 100% match · 2007 · 46 cit/yr\
**Bayesian Online Changepoint Detection** ([link](https://www.semanticscholar.org/paper/9cacd41e4fbe518436877a6f1b24982099216e46))\
Ryan P. Adams and D. MacKay\
*arXiv: Machine Learning* · Oct 19, 2007 · 859 citations

> Changepoints are abrupt variations in the generative parameters of a data sequence. Online detection of changepoints is useful in modelling and prediction of time series in application areas such as finance, biometrics, and robotics. While frequentist methods have yielded online filtering and prediction techniques, most Bayesian papers have focused on the retrospective segmentation problem. Here we examine the case where the model parameters before and after the changepoint are independent and we derive an online algorithm for exact inference of the most recent changepoint. We compute the probability distribution of the length of the current \`\`run,’’ or time since the last changepoint, using a simple message-passing algorithm. Our implementation is highly modular so that the algorithm may be applied to a variety of types of data. We illustrate this modularity by demonstrating the algorithm on three different real-world data sets.

------------------------------------------------------------------------

46\. · 100% match · 2011 · 3.5 cit/yr\
**Context Tree Switching** ([link](https://doi.org/10.1109/DCC.2012.39))\
J. Veness, K. S. Ng, Marcus Hutter, and Michael Bowling\
*2012 Data Compression Conference* · Nov 14, 2011 · 51 citations

> This paper describes the Context Tree Switching technique, a modification of Context Tree Weighting for the prediction of binary, stationary, n-Markov sources. By modifying Context Tree Weighting’s recursive weighting scheme, it is possible to mix over a strictly larger class of models without increasing the asymptotic time or space complexity of the original algorithm. We prove that this generalization preserves the desirable theoretical properties of Context Tree Weighting on stationary n-Markov sources, and show empirically that this new technique leads to consistent improvements over Context Tree Weighting as measured on the Calgary Corpus.

------------------------------------------------------------------------

47\. · 100% match · 2017 · 7.8 cit/yr\
**Parameter-Free Online Learning via Model Selection** ([link](https://www.semanticscholar.org/paper/1340d0789112200d22fbbbfdd030e9cf71c67ebe))\
Dylan J. Foster, Satyen Kale, M. Mohri, and Karthik Sridharan\
*Neural Information Processing Systems* · Dec 30, 2017 · 65 citations

> We introduce an efficient algorithmic framework for model selection in online learning, also known as parameter-free online learning. Departing from previous work, which has focused on highly structured function classes such as nested balls in Hilbert space, we propose a generic meta-algorithm framework that achieves online model selection oracle inequalities under minimal structural assumptions. We give the first computationally efficient parameter-free algorithms that work in arbitrary Banach spaces under mild smoothness assumptions; previous results applied only to Hilbert spaces. We further derive new oracle inequalities for matrix classes, non-nested convex sets, and $`\mathbb{R}^{d}`$ with generic regularizers. Finally, we generalize these results by providing oracle inequalities for arbitrary non-linear classes in the online supervised learning model. These results are all derived through a unified meta-algorithm scheme using a novel “multi-scale” algorithm for prediction with expert advice based on random playout, which may be of independent interest.

------------------------------------------------------------------------

48\. · 100% match · 2007 · 0.6 cit/yr\
**Optimal Causal Inference** ([link](https://www.semanticscholar.org/paper/0c8c8cd4275c7f3505ba0250d7f1be54842d9440))\
Susanne Still, J. Crutchfield, and C. J. Ellison\
*ArXiv* · Aug 11, 2007 · 11 citations

> We consider an information-theoretic objective function for statistical modeling of time series that embodies a parametrized trade-off between the predictive power of a model and the model’s complexity. We study two distinct cases of optimal causal inference, which we call optimal causal filtering (OCF) and optimal causal estimation (OCE). OCF corresponds to the ideal case of having infinite data. We show that OCF leads to the exact causal architecture of a stochastic process, in the limit in which the trade-off parameter tends to zero, thereby emphasizing prediction. Specifically, the filtering method reconstructs exactly the hidden, causal states. More generally, we establish that the method leads to a graded model-complexity hierarchy of approximations to the causal architecture. We show for nonideal cases with finite data (OCE) that the correct number of states can be found by adjusting for statistical fluctuations in probability estimates.

------------------------------------------------------------------------

49\. · 100% match · 2013 · 3.6 cit/yr\
**Synaptic Scaling Enables Dynamically Distinct Short- and Long-Term Memory Formation** ([link](https://doi.org/10.1186/1471-2202-14-S1-P415))\
Christian Tetzlaff, Christoph Kolodziejski, M. Timme, M. Tsodyks, and F. Wörgötter\
*PLoS Computational Biology* · Jul 1, 2013 · 47 citations

> Memory storage in the brain relies on mechanisms acting on time scales from minutes, for long-term synaptic potentiation, to days, for memory consolidation. During such processes, neural circuits distinguish synapses relevant for forming a long-term storage, which are consolidated, from synapses of short-term storage, which fade. How time scale integration and synaptic differentiation is simultaneously achieved remains unclear. Here we show that synaptic scaling – a slow process usually associated with the maintenance of activity homeostasis – combined with synaptic plasticity may simultaneously achieve both, thereby providing a natural separation of short- from long-term storage. The interaction between plasticity and scaling provides also an explanation for an established paradox where memory consolidation critically depends on the exact order of learning and recall. These results indicate that scaling may be fundamental for stabilizing memories, providing a dynamic link between early and late memory formation processes.

------------------------------------------------------------------------

50\. · 100% match · 2004 · 7.8 cit/yr\
**Off-line replay maintains declarative memories in a model of hippocampal-neocortical interactions** ([link](https://doi.org/10.1038/nn1202))\
S. Káli and P. Dayan\
*Nature Neuroscience* · Feb 22, 2004 · 173 citations

*Showing top 50 of 115 papers. Full details available via CSV or BibTeX export.*
