# Prior art for AAT composite agency

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which a group of agents forms a valid composite or macro-agent if and only if its closed-loop dynamics commute with a coarse-graining of the constituent agents, measured by a closure defect. The framework further claims that the composite’s adaptive tempo is bounded by the sum of the parts minus coordination overhead, yielding a formal derivation of Brooks’s Law: if coordination overhead exceeds the baseline correction rate, adding agents causes the composite to fail. It also includes an extreme-composition regime, “symbiogenesis,” in which integration is asymmetric and one agent’s objective is fully absorbed into the host. The search should prioritize both the closest mathematical analogues and older conceptual or formal antecedents. Search broadly across multi-agent systems, reinforcement learning, control theory, complex systems, organizational theory, cybernetics, information theory, and evolutionary dynamics. Relevant matches include formal treatments of composite or macro-agents defined by dynamically valid aggregation, closure, lumpability, commutation with coarse-graining, approximate information states, predictive state abstractions, renormalization, multiscale control, or mathematically close notions of when grouped subsystems behave as a single agent. Also include formal derivations or mathematically close models of coordination overhead, tempo or responsiveness limits, and failure thresholds where adding agents or components degrades collective performance; applications of rate-distortion or related information-theoretic ideas to the fidelity, unity, or coherence of a composite agent based on shared observations or goals; and formal models of asymmetric integration in which one subsystem loses autonomy or its objective is absorbed by another, including evolutionary, game-theoretic, hierarchical-control, organizational, and principal-agent lineages when they are mathematically relevant. Exclude standard cooperative MARL papers that merely share a global reward without analyzing whether the agents constitute a single macro-entity, and exclude informal or empirical software-engineering discussions of Brooks’s Law that do not provide a mathematical, control-theoretic, or dynamical derivation. Restrict the search to academic literature only.

*Found 126 papers · May 21, 2026 · Estimated coverage of relevant papers: 84%*

## Summary of Results

AAT’s closest mathematical antecedents are the lumpability and quotient traditions: a group behaves as a valid macro-entity when microdynamics commute with a coarse-graining to autonomous macrodynamics \[1\], \[2\], with control-theoretic analogues in consistent abstractions, quotients, and bisimulation-preserving reductions \[3\], \[4\], \[5\], \[6\].

#### Dynamic validity of a composite

- Classical aggregation frames the same question as when grouped variables preserve accessibility, reachability, or coherent evolution \[7\], \[8\], \[9\], \[10\].
- Modern control work makes the criterion quantitative: approximate simulation, aggregate manifolds, and compositional abstractions attach explicit error bounds when commutation is imperfect \[11\], \[12\], \[13\], \[14\], \[15\].
- Markov coarse-graining gives the nearest formal template for a “closure defect,” via bounds on lumping/coarse-graining error and intertwining error \[16\], \[17\], \[18\], \[19\], \[20\].

#### Information-theoretic and predictive analogues

- In RL and stochastic processes, MDP homomorphisms, bisimulation metrics, causal states, and approximate information states formalize when an aggregate state is sufficient for closed-loop prediction and control \[21\], \[22\], \[23\], \[24\], \[25\], \[26\].
- Informational closure/autonomy and macro-causal emergence supply adjacent language for agent boundaries and when macroscales are more causally self-contained than microscale descriptions \[27\], \[28\], \[29\], \[30\], \[31\].

#### Tempo limits, coordination overhead, and failure thresholds

- The strongest formal analogues to the Brooks’s-Law claim treat coordination as a throughput or latency tax: collaboration architectures induce unavoidable bottleneck idleness \[32\]; local-feedback collectives lose coherence with scale \[33\], \[34\], \[35\]; communication-rate theorems place hard responsiveness thresholds on stabilization \[36\], \[37\], \[38\], \[39\].

#### Asymmetric integration / symbiogenesis

- Major-transition and endosymbiosis models provide the main precedent for extreme composition in which one subsystem loses autonomy or is effectively absorbed into a host objective \[40\], \[41\], \[42\].

## Paper Catalog (126 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2006 | 1.8 | Lumpability and Commutativity of Markov Processes ([link](https://doi.org/10.1080/07362990600632045)) | J. Tian and D. Kannan | Stochastic Analysis and Applications |
| 2 | 2002 | 3.6 | Consistent abstractions of affine control systems ([link](https://doi.org/10.1109/TAC.2002.1000269)) | George Pappas and S. Simic | IEEE Trans. Autom. Control. |
| 3 | 1994 | 11 | Exact and ordinary lumpability in finite Markov chains ([link](https://doi.org/10.2307/3215235)) | P. Buchholz | Journal of Applied Probability |
| 4 | 1961 | 11 | Aggregation of Variables in Dynamic Systems ([link](https://doi.org/10.1007/978-94-010-9521-1_12)) | H. Simon | Econometrica |
| 5 | 1968 | 8.8 | Control of large-scale dynamic systems by aggregation ([link](https://doi.org/10.1109/TAC.1968.1098900)) | M. Aoki | IEEE Transactions on Automatic Control |
| 6 | 2005 | 2.1 | Quotients of Fully Nonlinear Control Systems ([link](https://doi.org/10.1137/S0363012901399027)) | P. Tabuada and George Pappas | SIAM J. Control. Optim. |
| 7 | 1981 | 0.0 | Aggregability of dynamic systems and lumpability of Markov chains ([link](https://doi.org/10.1109/CDC.1981.269510)) | F. Delebecque, J. Quadrat, and P. Kokotovic | 1981 20th IEEE Conference on Decision and Control including the Symposium on Adaptive Processes |
| 8 | 1984 | 0.4 | A unified view of aggregation and coherency in networks and Markov chains ([link](https://doi.org/10.1080/00207178408933320)) | F. Delebecque, J. Quadrat, and P. Kokotovic | International Journal of Control |
| 9 | 2015 | 5.7 | Compositional Construction of Approximate Abstractions of Interconnected Control Systems ([link](https://doi.org/10.1145/2728606.2728615)) | M. Rungger and Majid Zamani | IEEE Transactions on Control of Network Systems |
| 10 | 2009 |  | A Fundamental Limit on Productivity in Organizations Collaborative Entropy Costs ([link](https://www.semanticscholar.org/paper/bdf23a4e9cadb3f669bb76e24fb51e64814ee2e3)) | R. Janow |  |
| 11 | 2003 | 9.7 | Bisimilar linear systems ([link](https://doi.org/10.1016/j.automatica.2003.07.003)) | George Pappas | Autom. |
| 12 | 2018 | 1.9 | Approximate abstractions of control systems with an application to aggregation ([link](https://doi.org/10.1016/J.AUTOMATICA.2020.109065)) | Stanley W. Smith, M. Arcak, and Majid Zamani | Autom. |
| 13 | 2004 | 2.9 | Equivalence of dynamical systems by bisimulation ([link](https://doi.org/10.1109/TAC.2004.838497)) | A. Schaft | IEEE Trans. Autom. Control. |
| 14 | 2022 | 1.2 | Quantitative Coarse-Graining of Markov Chains ([link](https://doi.org/10.1137/22m1473996)) | Bastian Hilder and U. Sharma | SIAM J. Math. Anal. |
| 15 | 1981 | 4.1 | A singular perturbation approach to modeling and control of Markov chains ([link](https://doi.org/10.1109/TAC.1981.1102780)) | R. Phillips and P. Kokotovic | IEEE Transactions on Automatic Control |
| 16 | 2015 | 2.6 | Collaboration and Multitasking in Networks: Architectures, Bottlenecks, and Capacity ([link](https://doi.org/10.1287/msom.2014.0498)) | I. Gurvich and J. V. Mieghem | Manuf. Serv. Oper. Manag. |
| 17 | 2011 | 30 | Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback ([link](https://doi.org/10.1109/TAC.2012.2202052)) | Bassam Bamieh, M. Jovanović, P. Mitra, and S. Patterson | IEEE Transactions on Automatic Control |
| 18 | 2011 | 0.7 | Bounding the coarse graining error in hidden Markov dynamics ([link](https://doi.org/10.1016/j.aml.2012.02.002)) | D. Andrieux | Appl. Math. Lett. |
| 19 | 2004 | 80 | Control under communication constraints ([link](https://doi.org/10.1109/TAC.2004.831187)) | S. Tatikonda and S. Mitter | IEEE Transactions on Automatic Control |
| 20 | 2004 | 34 | Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates ([link](https://doi.org/10.1137/S0363012902402116)) | G. Nair and R. Evans | SIAM J. Control. Optim. |
| 21 | 2011 | 9.3 | Approximate Bisimulation: A Bridge Between Computer Science and Control Theory ([link](https://doi.org/10.3166/ejc.17.568-578)) | A. Girard and George Pappas | Eur. J. Control |
| 22 | 2018 | 0.8 | Hierarchical Control via an Approximate Aggregate Manifold ([link](https://doi.org/10.23919/ACC.2018.8431887)) | Stanley W. Smith, M. Arcak, and Majid Zamani | 2018 Annual American Control Conference (ACC) |
| 23 | 2006 | 1.6 | Information and closure in systems theory ([link](https://www.semanticscholar.org/paper/846a8c33af45d6175643627b4df8fb0a9b63d423)) | Nils Bertschinger, E. Olbrich, N. Ay, and J. Jost |  |
| 24 | 2006 | 28 | Towards a Unified Theory of State Abstraction for MDPs ([link](https://www.semanticscholar.org/paper/ca9a2d326b9de48c095a6cb5912e1990d2c5ab46)) | Lihong Li, Thomas J. Walsh, and M. Littman | AI&M |
| 25 | 2016 | 15 | When the Map Is Better Than the Territory ([link](https://doi.org/10.3390/e19050188)) | Erik P. Hoel | ArXiv |
| 26 | 2009 | 1.0 | Bounding the lumping error in Markov chain dynamics ([link](https://doi.org/10.1016/j.aml.2009.03.016)) | K. Hoffmann and P. Salamon | Appl. Math. Lett. |
| 27 | 2018 | 2.1 | Approximate lumpability for Markovian agent-based models using local symmetries ([link](https://doi.org/10.1017/jpr.2019.44)) | Wasiur R. KhudaBukhsh, Arnab Auddy, Y. Disser, and H. Koeppl | J. Appl. Probab. |
| 28 | 2021 | 3.2 | Can Decentralized Control Outperform Centralized? The Role of Communication Latency ([link](https://doi.org/10.1109/TCNS.2023.3237483)) | Luca Ballotta, M. Jovanovi’c, and L. Schenato | IEEE Transactions on Control of Network Systems |
| 29 | 1999 | 34 | Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback ([link](https://doi.org/10.1109/9.763226)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 30 | 2016 | 6.7 | Compositional Abstraction for Networks of Control Systems: A Dissipativity Approach ([link](https://doi.org/10.1109/TCNS.2017.2670330)) | Majid Zamani and M. Arcak | IEEE Transactions on Control of Network Systems |
| 31 | 2024 | 3.2 | Formal error bounds for the state space reduction of Markov chains ([link](https://doi.org/10.1016/j.peva.2024.102464)) | Fabian Michel and Markus Siegle | Perform. Evaluation |
| 32 | 2008 | 4.8 | Bounding Performance Loss in Approximate MDP Homomorphisms ([link](https://www.semanticscholar.org/paper/935f58066e63518f4e519ea44119772bc5b4ce1b)) | Jonathan Taylor, Doina Precup, and P. Panangaden | Neural Information Processing Systems |
| 33 | 2015 | 11 | LQG Control With Minimum Directed Information: Semidefinite Programming Approach ([link](https://doi.org/10.1109/TAC.2017.2709618)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | IEEE Transactions on Automatic Control |
| 34 | 2015 | 21 | Biological organisation as closure of constraints. ([link](https://doi.org/10.1016/j.jtbi.2015.02.029)) | Maël Montévil and M. Mossio | Journal of theoretical biology |
| 35 | 2003 | 19 | Equivalence notions and model minimization in Markov decision processes ([link](https://doi.org/10.1016/S0004-3702(02%2900376-4)) | R. Givan, T. Dean, and M. Greig | Artif. Intell. |
| 36 | 2003 | 9.9 | Optimal state-space lumping in Markov chains ([link](https://doi.org/10.1016/S0020-0190(03%2900343-0)) | Salem Derisavi, H. Hermanns, and W. Sanders | Inf. Process. Lett. |
| 37 | 2001 | 74 | Stabilization of linear systems with limited information ([link](https://doi.org/10.1109/9.948466)) | N. Elia and S. Mitter | IEEE Trans. Autom. Control. |
| 38 | 2016 | 12 | Can the macro beat the micro? Integrated information across spatiotemporal scales. ([link](https://doi.org/10.1093/nc/niw012)) | Erik P. Hoel, L. Albantakis, W. Marshall, and G. Tononi | Neuroscience of consciousness |
| 39 | 2008 | 6.0 | Autonomy: An information theoretic perspective ([link](https://doi.org/10.1016/j.biosystems.2007.05.018)) | Nils Bertschinger, E. Olbrich, N. Ay, and J. Jost | Bio Systems |
| 40 | 2001 | 2.7 | Compositional Abstractions of Hybrid Control Systems ([link](https://doi.org/10.1109/CDC.2001.980125)) | P. Tabuada, George Pappas, and P. Lima | Discrete Event Dynamic Systems |
| 41 | 2004 | 218 | Information flow and cooperative control of vehicle formations ([link](https://doi.org/10.3182/20020721-6-ES-1901.00100)) | J. A. Fax and R. Murray | IEEE Transactions on Automatic Control |
| 42 | 1992 | 0.0 | LUMPABILITY AND AGGREGATION OF MARKOVIAN SUBMODELS ([link](https://www.semanticscholar.org/paper/19a406d08c3912bd9acf1163af5a8b4bed567a81)) | P. Buchholz |  |
| 43 | 2014 | 4.6 | A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level ([link](https://doi.org/10.1109/TAC.2015.2500658)) | Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina | IEEE Transactions on Automatic Control |
| 44 | 2015 | 4.1 | Approximations of Stochastic Hybrid Systems: A Compositional Approach ([link](https://doi.org/10.1109/TAC.2016.2619419)) | Majid Zamani, M. Rungger, and Peyman Mohajerin Esfahani | IEEE Transactions on Automatic Control |
| 45 | 2017 | 1.2 | Approximate and Exact Solutions of Intertwining Equations Through Random Spanning Forests ([link](https://doi.org/10.1007/978-3-030-60754-8_3)) | L. Avena, F. Castell, A. Gaudilliere, and Clothilde Mélot | Progress in Probability |
| 46 | 2008 | 4.0 | Bisimilar Finite Abstractions of Interconnected Systems ([link](https://doi.org/10.1007/978-3-540-78929-1_37)) | Y. Tazaki and J. Imura | International Conference on Hybrid Systems: Computation and Control |
| 47 | 2014 | 1.9 | Optimal high-level descriptions of dynamical systems ([link](https://www.semanticscholar.org/paper/ba13d49c5b1c2a274b585094ea89c9a4e74ba5cb)) | D. Wolpert, Joshua A. Grochow, E. Libby, and S. Dedeo | arXiv: Information Theory |
| 48 | 2015 | 23 | Feedback Refinement Relations for the Synthesis of Symbolic Controllers ([link](https://doi.org/10.1109/TAC.2016.2593947)) | G. Reissig, Alexander Weber, and M. Rungger | IEEE Transactions on Automatic Control |
| 49 | 2024 | 2.0 | On Finding Optimal Collective Variables for Complex Systems by Minimizing the Deviation between Effective and Full Dynamics ([link](https://doi.org/10.1137/24m1658917)) | Wei Zhang and Christof Schütte | Multiscale Model. Simul. |
| 50 |  | 102 | Approximate Homomorphisms : A framework for non-exact minimization in Markov Decision Processes ([link](https://www.semanticscholar.org/paper/133583b9c4634702ab2579205ee3eb78714b7feb)) | Balaraman Ravindran |  |
| 51 | 2014 | 2.2 | Network Entropy and Data Rates Required for Networked Control ([link](https://doi.org/10.1109/TCNS.2015.2440551)) | C. Kawan and J. Delvenne | IEEE Transactions on Control of Network Systems |
| 52 | 1989 | 1.4 | On weak lumpability in Markov chains ([link](https://doi.org/10.2307/3214403)) | G. Rubino | Journal of Applied Probability |
| 53 | 2010 | 54 | Networked Control Systems With Communication Constraints: Tradeoffs Between Transmission Intervals, Delays and Performance ([link](https://doi.org/10.1109/TAC.2010.2042352)) | W. Heemels, A. Teel, N. Wouw, and D. Nešić | IEEE Transactions on Automatic Control |
| 54 | 2002 | 9.9 | Towards the Control of Linear Systems with Minimum Bit-Rate ([link](https://www.semanticscholar.org/paper/b72f6715cece3f0d4fc696236313ddac141af641)) | J. Hespanha, Antonio Ortega, and L. Vasudevan |  |
| 55 | 2015 | 31 | Biological Autonomy: A Philosophical and Theoretical Enquiry ([link](https://doi.org/10.1007/978-94-017-9837-2)) | Á. Moreno and M. Mossio |  |
| 56 | 2020 | 20 | Approximate information state for approximate planning and reinforcement learning in partially observed systems ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980)) | Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan | ArXiv |
| 57 | 2008 | 21 | Approximately Bisimilar Symbolic Models for Incrementally Stable Switched Systems ([link](https://doi.org/10.1109/TAC.2009.2034922)) | A. Girard, G. Pola, and P. Tabuada | IEEE Transactions on Automatic Control |
| 58 | 2003 | 2.3 | What Is a Macrostate? Subjective Observations and Objective Dynamics ([link](https://doi.org/10.1007/s10701-024-00814-1)) | C. Shalizi and Cristopher Moore | Foundations of Physics |
| 59 | 2015 | 35 | Toward major evolutionary transitions theory 2.0 ([link](https://doi.org/10.1073/pnas.1421398112)) | E. Szathmáry | Proceedings of the National Academy of Sciences |
| 60 | 2011 | 12 | Bisimulation Metrics for Continuous Markov Decision Processes ([link](https://doi.org/10.1137/10080484X)) | N. Ferns, P. Panangaden, and Doina Precup | SIAM J. Comput. |
| 61 | 2002 | 2.5 | Conditional Expectations and Renormalization ([link](https://doi.org/10.1137/S1540345902405556)) | A. Chorin | Multiscale Model. Simul. |
| 62 | 1997 | 20 | Systems with finite communication bandwidth constraints. I. State estimation problems ([link](https://doi.org/10.1109/9.623096)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 63 | 1993 | 2.1 | Lumpability and marginalisability for continuous-time Markov chains ([link](https://doi.org/10.2307/3214762)) | F. Ball and G. Yeo | Journal of Applied Probability |
| 64 | 1999 | 4.3 | Feedback Designs for Controlling Device Arrays with Communication Channel Bandwidth Constraints ([link](https://www.semanticscholar.org/paper/b58112fcd8f12e784345d7242d47c6a6c9c1e8ec)) | J. Baillieul |  |
| 65 | 2016 | 1.8 | Minimum-information LQG control part I: Memoryless controllers ([link](https://doi.org/10.1109/CDC.2016.7799131)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 66 | 2017 | 19 | Coarse-graining as a downward causation mechanism ([link](https://doi.org/10.1098/rsta.2016.0338)) | J. Flack | Philosophical transactions. Series A, Mathematical, physical, and engineering sciences |
| 67 | 2009 | 1.5 | Hierarchical control system design using approximate simulation ([link](https://doi.org/10.1016/j.automatica.2008.09.016)) | A. Girard and George Pappas | Autom. |
| 68 | 1974 | 34 | Autopoiesis: the organization of living systems, its characterization and a model. ([link](https://doi.org/10.1016/0303-2647(74%2990031-8)) | F. G. Varela, H. Maturana, and R. Uribe | Currents in modern biology |
| 69 | 2024 | 7.9 | Software in the natural world: A computational approach to hierarchical emergence ([link](https://www.semanticscholar.org/paper/533276061cd32694f90daf56b1883afd58e4ac6a)) | F. Rosas et al. |  |
| 70 | 2020 | 1.5 | A macro agent and its actions ([link](https://doi.org/10.1007/978-3-030-71899-2_7)) | L. Albantakis, F. Massari, M. Beheler-Amass, and G. Tononi | ArXiv |
| 71 | 2004 | 14 | Predictive State Representations: A New Theory for Modeling Dynamical Systems ([link](https://www.semanticscholar.org/paper/532c61a2af5cde64628d0cdd2ba0823800118d0f)) | Satinder Singh, Michael R. James, and Matthew R. Rudary | Conference on Uncertainty in Artificial Intelligence |
| 72 | 1999 | 19 | Computational Mechanics: Pattern and Prediction, Structure and Simplicity ([link](https://doi.org/10.1023/A:1010388907793)) | C. Shalizi and J. Crutchfield | Journal of Statistical Physics |
| 73 | 2024 | 1.9 | Characterizing simulation relations through control architectures in abstraction-based control ([link](https://www.semanticscholar.org/paper/f71b45084bf4e2d91e7cb8f73e9fecb90290ee17)) | Julien Calbert, A. Girard, and Raphaël M. Jungers |  |
| 74 | 2021 | 0.2 | Coarse-graining and reconstruction for Markov matrices ([link](https://doi.org/10.4171/zaa/1796)) | Artur Stephan | Zeitschrift für Analysis und ihre Anwendungen |
| 75 | 1978 | 8.0 | Computation and transmission requirements for a decentralized linear-quadratic-Gaussian control problem ([link](https://doi.org/10.1109/CDC.1978.268109)) | J. Speyer | 1978 IEEE Conference on Decision and Control including the 17th Symposium on Adaptive Processes |
| 76 | 2005 | 10 | On the ill-posedness of certain vehicular platoon control problems ([link](https://doi.org/10.1109/TAC.2005.854584)) | M. Jovanović and Bassam Bamieh | IEEE Transactions on Automatic Control |
| 77 | 2002 | 4.8 | Decentralized control information structures preserved under feedback ([link](https://doi.org/10.1109/CDC.2002.1184558)) | M. Rotkowitz and S. Lall | Proceedings of the 41st IEEE Conference on Decision and Control, 2002. |
| 78 | 2004 | 16 | Metrics for Finite Markov Decision Processes ([link](https://www.semanticscholar.org/paper/2c85356cd182c16e0a2e5c4a97112efbc1132cdf)) | N. Ferns, P. Panangaden, and Doina Precup | AAAI Conference on Artificial Intelligence |
| 79 | 2009 | 0.6 | Decentralized Computation and Communication in Stabilization of Distributed Control Systems ([link](https://www.semanticscholar.org/paper/9f36932bd180b4549e07dc822d1271eaa18104e6)) | S. Yüksel |  |
| 80 | 2003 | 1.2 | Adaptation and enslavement in endosymbiont-host associations. ([link](https://doi.org/10.1103/PhysRevE.69.051913)) | Marcus Frean and E. Abraham | Physical review. E, Statistical, nonlinear, and soft matter physics |
| 81 | 2007 | 1.0 | A dual eigenvector condition for strong lumpability of Markov chains ([link](https://www.semanticscholar.org/paper/694701f19056d4e809fc7ea4b752ed1699860679)) | M. Jacobi and Olof Goernerup | arXiv: Probability |
| 82 | 1972 | 10 | Team decision theory and information structures in optimal control problems–Part II ([link](https://doi.org/10.1109/TAC.1972.1099850)) | Y. Ho and K. Chu | IEEE Transactions on Automatic Control |
| 83 | 2010 | 3.2 | Lumpability abstractions of rule-based systems ([link](https://doi.org/10.4204/EPTCS.40.10)) | Jérôme Feret, T. Henzinger, H. Koeppl, and Tatjana Petrov | Theoretical Computer Science |
| 84 | 2013 | 1.4 | Markov chain aggregation and its applications to combinatorial reaction networks ([link](https://doi.org/10.1007/s00285-013-0738-7)) | Arnab Ganguly, Tatjana Petrov, and H. Koeppl | Journal of Mathematical Biology |
| 85 | 2007 | 2.8 | Controller synthesis for bisimulation equivalence ([link](https://doi.org/10.1016/j.sysconle.2007.11.005)) | P. Tabuada | Syst. Control. Lett. |
| 86 | 2001 | 24 | Predictive Representations of State ([link](https://www.semanticscholar.org/paper/4a7de0669fd835b2efcab97c7d3dc28ea7a1e6a3)) | M. Littman, R. Sutton, and Satinder Singh | Neural Information Processing Systems |
| 87 | 2000 | 1.4 | Information Bottlenecks, Causal States, and Statistical Relevance Bases: How to Represent Relevant Information in memoryless transduction ([link](https://doi.org/10.1142/S0219525902000481)) | C. Shalizi and J. Crutchfield | Adv. Complex Syst. |
| 88 | 2009 | 5.2 | Past-future information bottleneck in dynamical systems. ([link](https://doi.org/10.1103/PHYSREVE.79.041925)) | F. Creutzig, A. Globerson, and Naftali Tishby | Physical review. E, Statistical, nonlinear, and soft matter physics |
| 89 | 2014 | 5.1 | Information Bottleneck Approach to Predictive Inference ([link](https://doi.org/10.3390/e16020968)) | Susanne Still | Entropy |
| 90 | 2007 | 2.9 | Optimal causal inference: estimating stored information and approximating causal architecture. ([link](https://doi.org/10.1063/1.3489885)) | Susanne Still, J. Crutchfield, and C. J. Ellison | Chaos |
| 91 | 2017 | 3.3 | Random Forests and Networks Analysis ([link](https://doi.org/10.1007/s10955-018-2124-8)) | L. Avena, F. Castell, A. Gaudilliere, and Clothilde Mélot | Journal of Statistical Physics |
| 92 | 2006 | 4.7 | Methods for Computing State Similarity in Markov Decision Processes ([link](https://www.semanticscholar.org/paper/2f8aaf6d0654e729e47224435aec83d733685cc3)) | N. Ferns, P. S. Castro, Doina Precup, and P. Panangaden | ArXiv |
| 93 |  |  | Quantization and Coding for Decentralized LTI Systems 1 ([link](https://www.semanticscholar.org/paper/9318fb88b89140c16558b5457beed0e78fb8ee9f)) | S. Yüksel and T. Başar |  |
| 94 | 2007 | 3.5 | Communication Constraints for Decentralized Stabilizability With Time-Invariant Policies ([link](https://doi.org/10.1109/TAC.2007.899085)) | S. Yüksel and T. Başar | IEEE Transactions on Automatic Control |
| 95 | 2015 |  | Exact lumping of feller semigroups: A $`C^{\star}`$-algebras approach ([link](https://doi.org/10.3934/PROC.2015.0965)) | L. Roncoroni |  |
| 96 | 2014 | 0.9 | Circumventing the Curse of Dimensionality in Prediction: Causal Rate-Distortion for Infinite-Order Markov Processes ([link](https://www.semanticscholar.org/paper/5308a461868cde8b8d175eee0de4eea699028d14)) | Sarah E. Marzen and J. Crutchfield | ArXiv |
| 97 | 1999 | 3.9 | Control of LQG systems under communication constraints ([link](https://doi.org/10.1109/ACC.1999.786578)) | S. Tatikonda, Anant Sahai, and S. Mitter | Proceedings of the 1999 American Control Conference (Cat. No. 99CH36251) |
| 98 | 2016 | 3.5 | Predictive Rate-Distortion for Infinite-Order Markov Processes ([link](https://doi.org/10.1007/s10955-016-1520-1)) | Sarah E. Marzen and J. Crutchfield | Journal of Statistical Physics |
| 99 | 2016 | 0.5 | The Information Bottleneck method for Optimal Prediction of Multilevel Agent-Based Systems ([link](https://doi.org/10.1142/S0219525916500028)) | Robin Lamarche-Perrin, S. Banisch, and E. Olbrich | Adv. Complex Syst. |
| 100 | 2008 | 15 | Mistuning-Based Control Design to Improve Closed-Loop Stability Margin of Vehicular Platoons ([link](https://doi.org/10.1109/TAC.2009.2026934)) | P. Barooah, P. Mehta, and J. Hespanha | IEEE Transactions on Automatic Control |
| 101 | 2018 | 4.5 | Farming the mitochondrial ancestor as a model of endosymbiotic establishment by natural selection ([link](https://doi.org/10.1073/pnas.1718707115)) | I. Zachar, A. Szilágyi, S. Számadó, and E. Szathmáry | Proceedings of the National Academy of Sciences of the United States of America |
| 102 | 2005 | 0.8 | Communication constraints in the state agreement problem ([link](https://www.semanticscholar.org/paper/edad8f106b2c664cc04c82aa02661516e4cc1d1d)) | R. Carli, F. Fagnani, A. Speranzon, and S. Zampieri |  |
| 103 | 2014 | 5.1 | Bisimulation Metrics are Optimal Value Functions ([link](https://www.semanticscholar.org/paper/24576c9cae62a2f4d94c94cdecd68a5655d2ca40)) | N. Ferns and Doina Precup | Conference on Uncertainty in Artificial Intelligence |
| 104 | 1995 | 41 | String stability of interconnected systems ([link](https://doi.org/10.1109/ACC.1995.531196)) | S. Darbha and J. Hedrick | Proceedings of 1995 American Control Conference - ACC’95 |
| 105 | 2007 | 1.9 | Assessing coordination overhead in control of robot teams ([link](https://doi.org/10.1109/ICSMC.2007.4414055)) | Jijun Wang and M. Lewis | 2007 IEEE International Conference on Systems, Man and Cybernetics |
| 106 | 2013 |  | Closure Measures and the Tent Map Closure Measures and the Tent Map ([link](https://www.semanticscholar.org/paper/4279b20df2a047014cd18b80be55f9dc7864c407)) | E. Olbrich et al. |  |
| 107 | 2006 | 7.0 | Organizational invariance and metabolic closure: analysis in terms of (M,R) systems. ([link](https://doi.org/10.1016/J.JTBI.2005.07.007)) | J. Letelier, J. Soto‐Andrade, Flavio Guíñez Abarzúa, A. Cornish-Bowden, and María Luz Cárdenas | Journal of theoretical biology |
| 108 | 2015 | 3.1 | Conflict and cooperation in eukaryogenesis: implications for the timing of endosymbiosis and the evolution of sex ([link](https://doi.org/10.1098/rsif.2015.0584)) | A. Radzvilavicius and N. Blackstone | bioRxiv |
| 109 | 1995 | 0.9 | Intertwining of Markov semi-groups, some examples ([link](https://doi.org/10.1007/BFB0094197)) | P. Biane |  |
| 110 | 2003 | 5.1 | Autopoietic and (M,R) systems. ([link](https://doi.org/10.1016/S0022-5193(03%2900034-1)) | J. Letelier, G. Marín, and J. Mpodozis | Journal of theoretical biology |
| 111 | 2004 | 16 | A Universal Definition of Life: Autonomy and Open-Ended Evolution ([link](https://doi.org/10.1023/B:ORIG.0000016440.53346.dc)) | K. Ruiz-Mirazo, J. Peretó, and Á. Moreno | Origins of life and evolution of the biosphere |
| 112 | 2004 | 10 | Basic Autonomy as a Fundamental Step in the Synthesis of Life ([link](https://doi.org/10.1162/1064546041255584)) | K. Ruiz-Mirazo and Á. Moreno | Artificial Life |
| 113 | 1998 | 3.6 | Beta-gamma random variables and intertwining relations between certain Markov processes ([link](https://doi.org/10.4171/RMI/241)) | P. Carmona, F. Petit, and M. Yor | Revista Matematica Iberoamericana |
| 114 | 2021 | 0.2 | Optimal Network Topology of Multi-Agent Systems subject to Computation and Communication Latency ([link](https://doi.org/10.1109/MED51440.2021.9480167)) | Luca Ballotta, M. Jovanovi’c, and L. Schenato | 2021 29th Mediterranean Conference on Control and Automation (MED) |
| 115 | 2016 | 1.3 | Minimum-information LQG control Part II: Retentive controllers ([link](https://doi.org/10.1109/CDC.2016.7799130)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 116 | 2015 | 0.9 | Past-future Information Bottleneck for linear feedback systems ([link](https://doi.org/10.1109/CDC.2015.7403120)) | Nadav Amir, Stas Tiomkin, and Naftali Tishby | 2015 54th IEEE Conference on Decision and Control (CDC) |
| 117 | 2007 | 1.7 | Pseudometrics for State Aggregation in Average Reward Markov Decision Processes ([link](https://doi.org/10.1007/978-3-540-75225-7_30)) | R. Ortner | International Conference on Algorithmic Learning Theory |
| 118 | 2026 |  | Community First Theory: How Collective Organization Generates Individual Diversity ([link](https://doi.org/10.3390/e28050523)) | Takashi Ikegami, Hiroki Kojima, and A. Kashiwagi | Entropy |
| 119 | 2026 | 2.0 | Quantifying emergent complexity ([link](https://doi.org/10.1016/j.patter.2025.101472)) | Erik Hoel | Patterns |
| 120 | 2025 |  | Agency at the Interface: Distinguishing Teleological from Structural Self-Organization via Internal Coarse-Graining and Downward Causation ([link](https://www.semanticscholar.org/paper/f56eefe968bd6fcad63b74808924ca2dc69f6d31)) | Kazuya Horibe and Keisuke Suzuki |  |
| 121 | 2012 |  | Lumped Markov chains and entropy rate ([link](https://www.semanticscholar.org/paper/4768af384fe4f8ccc5f915ea5d818d0c64f730ad)) | B. Geiger and Christoph Hofer-Temmel | ArXiv |
| 122 | 2010 | 0.2 | Aggregation and Lumping of DTMCs ([link](https://doi.org/10.1002/9780470400531.EORMS0013)) | M. Thomas |  |
| 123 | 1981 | 3.1 | Optimal control of markov chains admitting strong and weak interactions ([link](https://doi.org/10.1016/0005-1098(81%2990047-9)) | F. Delebecque and J. Quadrat | Autom. |
| 124 | 1981 | 1.5 | Coherency based decomposition and aggregation ([link](https://doi.org/10.1016/0005-1098(82%2990025-5)) | P. Kokotovic, B. Avramovic, J. Chow, and J. Winkelman | Autom. |
| 125 | 1975 | 0.8 | Aggregation of states in a Markov chain with weak interaction ([link](https://doi.org/10.1007/BF01069471)) | V. G. Gaitsgori and A. A. Pervozvanskiĭ | Cybernetics |
| 126 | 1978 | 1.3 | Some approximation methods for estimation and control of large scale systems ([link](https://doi.org/10.1109/TAC.1978.1101705)) | M. Aoki | IEEE Transactions on Automatic Control |

### Paper Details

1\. · 100% match · 2006 · 1.8 cit/yr\
**Lumpability and Commutativity of Markov Processes** ([link](https://doi.org/10.1080/07362990600632045))\
J. Tian and D. Kannan\
*Stochastic Analysis and Applications* · Jul 1, 2006 · 36 citations

------------------------------------------------------------------------

2\. · 100% match · 2002 · 3.6 cit/yr\
**Consistent abstractions of affine control systems** ([link](https://doi.org/10.1109/TAC.2002.1000269))\
George Pappas and S. Simic\
*IEEE Trans. Autom. Control.* · Aug 7, 2002 · 85 citations

> In this paper, we consider the problem of constructing abstractions of affine control systems that preserve reachability properties, and, in particular, local accessibility. In this framework, showing local accessibility of the higher level, abstracted model is equivalent to showing local accessibility of the, more detailed, lower level model. Given an affine control system and a smooth surjective map, we present a canonical construction for extracting an affine control system describing the trajectories of the abstracted variables. We then obtain conditions on the abstraction maps that render the original and abstracted system equivalent from a local accessibility point of view. Such consistent hierarchies of accessibility preserving abstractions of nonlinear control systems are then considered for various classes of affine control systems including linear, bilinear, drift free, and strict feedback systems.

------------------------------------------------------------------------

3\. · 100% match · 1994 · 11 cit/yr\
**Exact and ordinary lumpability in finite Markov chains** ([link](https://doi.org/10.2307/3215235))\
P. Buchholz\
*Journal of Applied Probability* · Mar 1, 1994 · 365 citations

------------------------------------------------------------------------

4\. · 100% match · 1961 · 11 cit/yr\
**Aggregation of Variables in Dynamic Systems** ([link](https://doi.org/10.1007/978-94-010-9521-1_12))\
H. Simon\
*Econometrica* · Apr 1, 1961 · 726 citations

------------------------------------------------------------------------

5\. · 100% match · 1968 · 8.8 cit/yr\
**Control of large-scale dynamic systems by aggregation** ([link](https://doi.org/10.1109/TAC.1968.1098900))\
M. Aoki\
*IEEE Transactions on Automatic Control* · Jun 1, 1968 · 510 citations

> A method is proposed to obtain a model of a dynamic system with a state vector of high dimension. The model is derived by “aggregating” the original system state vector into a lower-dimensional vector. Some properties of the aggregation method are investigated in the paper. The concept of aggregation, a generalization of that of projection, is related to that of state vector partition and is useful not only in building a model of reduced dimension, but also in unifying several topics in the control theory such as regulators with incomplete state feedback, characteristic value computations, model controls, and bounds on the solution of the matrix Riccati equations, etc. Using the quantitative definition of weak coupling proposed by Milne, a suboptimal control policy for the weakly coupled system is derived. Questions of performance degradation and of stability of such suboptimally controlled systems are also answered in the paper.

------------------------------------------------------------------------

6\. · 100% match · 2005 · 2.1 cit/yr\
**Quotients of Fully Nonlinear Control Systems** ([link](https://doi.org/10.1137/S0363012901399027))\
P. Tabuada and George Pappas\
*SIAM J. Control. Optim.* · May 1, 2005 · 44 citations

> In this paper, we introduce and study quotients of fully nonlinear control systems. Our definition is inspired by categorical definitions of quotients as well as recent work on abstractions of affine control systems. We show that quotients exist under mild regularity assumptions and characterize the structure of the quotient state/input space. This allows one to understand how states and inputs of the quotient system are related to states and inputs of the original system. We also introduce a notion of projectability which turns out to be equivalent to controlled invariance. This allows one to regard previous work on symmetries, partial symmetries, and controlled invariance as leading to special types of quotients. We also show the existence of quotients that are not induced by symmetries or controlled invariance. Such decompositions have a potential use in a theory of hierarchical control based on quotients.

------------------------------------------------------------------------

7\. · 100% match · 1981 · 0.0 cit/yr\
**Aggregability of dynamic systems and lumpability of Markov chains** ([link](https://doi.org/10.1109/CDC.1981.269510))\
F. Delebecque, J. Quadrat, and P. Kokotovic\
*1981 20th IEEE Conference on Decision and Control including the Symposium on Adaptive Processes* · Dec 1, 1981 · 1 citations

------------------------------------------------------------------------

8\. · 100% match · 1984 · 0.4 cit/yr\
**A unified view of aggregation and coherency in networks and Markov chains** ([link](https://doi.org/10.1080/00207178408933320))\
F. Delebecque, J. Quadrat, and P. Kokotovic\
*International Journal of Control* · Oct 1, 1984 · 18 citations

> Abstract This paper presents a unified treatment of aggregability, lumpability, coherency, reversibility, partial balance and similar properties appearing in different fields including power systems and queueing theory. A coherency condition, well known in power systems, implies the existence of a finite state filter for Markov chains, while aggregability and coherency yield a new condition for decentralized computation of the invariant measure.

------------------------------------------------------------------------

9\. · 100% match · 2015 · 5.7 cit/yr\
**Compositional Construction of Approximate Abstractions of Interconnected Control Systems** ([link](https://doi.org/10.1145/2728606.2728615))\
M. Rungger and Majid Zamani\
*IEEE Transactions on Control of Network Systems* · Apr 14, 2015 · 63 citations

> We consider a compositional construction of approximate abstractions of interconnected control systems. In our framework, an abstraction acts as a substitute in the controller design process and is itself a continuous control system. The abstraction is related to the concrete control system via a so-called simulation function: a Lyapunov-like function, which is used to establish a quantitative bound between the behavior of the approximate abstraction and the concrete system. In the first part of the paper, we provide a small gain type condition that facilitates the compositional construction of an abstraction of an interconnected control system together with a simulation function from the abstractions and simulation functions of the individual subsystems. In the second part of the paper, we restrict our attention to linear control system and characterize simulation functions in terms of controlled invariant, externally stabilizable subspaces. Based on those characterizations, we propose a particular scheme to construct abstractions for linear control systems. We illustrate the compositional construction of an abstraction on an interconnected system consisting of four linear subsystems. We use the abstraction as a substitute to synthesize a controller to enforce a certain linear temporal logic specification.

------------------------------------------------------------------------

10\. · 100% match · 2009\
**A Fundamental Limit on Productivity in Organizations Collaborative Entropy Costs** ([link](https://www.semanticscholar.org/paper/bdf23a4e9cadb3f669bb76e24fb51e64814ee2e3))\
R. Janow\
0 citations

> Many researchers and managers agree that small workgroups tend to lose productivity and speed as they grow large and that decision-making tends to become sluggish in very large organizations. These effects are attributed to collaborative coordination costs that grow in importance as functions of an organization’s scale. Understanding of these effects has however been primarily empirical and qualitative. This paper presents a first-principles mathematical model that quantitatively predicts such productivity variations. It is based on a fundamental cost mechanism that has been overlooked in the past but which nonetheless dramatically limits knowledge workers’ productivity and timely response: one must account for the information associated with each actor’s range of collaborator choices when trying to understand organizations as systems of human knowledge processors. A Shannon-like “collaborative entropy” is quantified and introduced to model the extra decision information that must be generated when an organization distributes its functions among collaborating internal actors. The implied coordination cost is a fundamental limit on the per capita productivity for knowledge work. The productivity limit would apply even if management made perfect resource allocations. Information is lost if actors try to exceed the maximum rates for exchanging decision information. The model compensates for value gained by accessing specialized expertise and hiding complexity. The productivity metric used assumes constant decision quality. In a single growing workgroup the per capita productivity increases while the group is small and lightly loaded, but it falls off logarithmically rather than remaining constant once the group size exceeds a saturation value at which raw decision capacity is all in use. The productivity fall-off is due entirely to collaborative entropy. For organizations as a whole two additional scale effects may apply: the fraction of an actor’s total effort spent in collaboration versus individual work may grow, and the average number of collaborators per actor may also grow owing to increasing specialization. Productivity is then strongly peaked around an optimum organization size and varies rapidly above or below the peak by a factor in the range of 2 5. The productivity impact of collaborative entropy is large enough to strongly affect competitive advantage. Impact is maximized when the ratio of collaborative to individual effort is large. Large organizations may thus be inherently disadvantaged versus small ones wherever fast decision-making or high knowledgeworker productivity are key drivers. Even a modest amount of collaboration significantly decreases the productivity of actors functioning primarily as individual contributors.

------------------------------------------------------------------------

11\. · 100% match · 2003 · 9.7 cit/yr\
**Bisimilar linear systems** ([link](https://doi.org/10.1016/j.automatica.2003.07.003))\
George Pappas\
*Autom.* · Dec 1, 2003 · 218 citations

> The notion of bisimulation in theoretical computer science is one of the main complexity reduction methods for the analysis and synthesis of labeled transition systems. Bisimulations are special quotients of the state space that preserve many important properties expressible in temporal logics, and, in particular, reachability. In this paper, the framework of bisimilar transition systems is applied to various transition systems that are generated by linear control systems. Given a discrete-time or continuous-time linear system, and a finite observation map, we characterize linear quotient maps that result in quotient transition systems that are bisimilar to the original system. Interestingly, the characterizations for discrete-time systems are more restrictive than for continuous-time systems, due to the existence of an atomic time step. We show that computing the coarsest bisimulation, which results in maximum complexity reduction, corresponds to computing the maximal controlled or reachability invariant subspace inside the kernel of the observations map. These results establish strong connections between complexity reduction concepts in control theory and computer science.

------------------------------------------------------------------------

12\. · 100% match · 2018 · 1.9 cit/yr\
**Approximate abstractions of control systems with an application to aggregation** ([link](https://doi.org/10.1016/J.AUTOMATICA.2020.109065))\
Stanley W. Smith, M. Arcak, and Majid Zamani\
*Autom.* · Sep 10, 2018 · 15 citations

> Previous approaches to constructing abstractions for control systems rely on geometric conditions or, in the case of an interconnected control system, a condition on the interconnection topology. Since these conditions are not always satisfiable, we relax the restrictions on the choice of abstractions, instead opting to select ones which nearly satisfy such conditions via optimization-based approaches. To quantify the resulting effect on the error between the abstraction and concrete control system, we introduce the notions of practical simulation functions and practical storage functions. We show that our approach facilitates the procedure of aggregation, where one creates an abstraction by partitioning agents into aggregate areas. We demonstrate the results on an application where we regulate the temperature in three separate zones of a building.

------------------------------------------------------------------------

13\. · 100% match · 2004 · 2.9 cit/yr\
**Equivalence of dynamical systems by bisimulation** ([link](https://doi.org/10.1109/TAC.2004.838497))\
A. Schaft\
*IEEE Trans. Autom. Control.* · Dec 20, 2004 · 62 citations

> A general notion of bisimulation is defined for linear input-state-output systems, using analogies with the theory of concurrent processes. A characterization of bisimulation and an algorithm for computing the maximal bisimulation relation is derived using geometric control theory. Bisimulation is shown to be a notion which unifies the concepts of state-space equivalence and state-space reduction, and which allows to study equivalence of systems with nonminimal state-space dimension. The notion of bisimulation is especially powerful for “nondeterministic” dynamical systems, and leads in this case to a notion of equivalence which is finer than equality of external behavior. For abstractions of systems it is shown how the results specialize to previously obtained results by other authors. Extensions of the main results to the nonlinear case are provided.

------------------------------------------------------------------------

14\. · 100% match · 2022 · 1.2 cit/yr\
**Quantitative Coarse-Graining of Markov Chains** ([link](https://doi.org/10.1137/22m1473996))\
Bastian Hilder and U. Sharma\
*SIAM J. Math. Anal.* · Jan 25, 2022 · 5 citations

> Coarse-graining techniques play a central role in reducing the complexity of stochastic models, and are typically characterised by a mapping which projects the full state of the system onto a smaller set of variables which captures the essential features of the system. Starting with a continuous-time Markov chain, in this work we propose and analyse an effective dynamics, which approximates the dynamical information in the coarse-grained chain. Without assuming explicit scale-separation, we provide sufficient conditions under which this effective dynamics stays close to the original system and provide quantitative bounds on the approximation error. We also compare the effective dynamics and corresponding error bounds to the averaging literature on Markov chains which involve explicit scale-separation. We demonstrate our findings on an illustrative test example.

------------------------------------------------------------------------

15\. · 100% match · 1981 · 4.1 cit/yr\
**A singular perturbation approach to modeling and control of Markov chains** ([link](https://doi.org/10.1109/TAC.1981.1102780))\
R. Phillips and P. Kokotovic\
*IEEE Transactions on Automatic Control* · Oct 1, 1981 · 184 citations

> Finite state continuous time Markov processes with weak interactions are modeled as singularly perturbed systems. Aggregate states are obtained using a grouping algorithm. Two-time scale expansions simplify cost equations and lead to decentralized optimization algorithms.

------------------------------------------------------------------------

16\. · 100% match · 2015 · 2.6 cit/yr\
**Collaboration and Multitasking in Networks: Architectures, Bottlenecks, and Capacity** ([link](https://doi.org/10.1287/msom.2014.0498))\
I. Gurvich and J. V. Mieghem\
*Manuf. Serv. Oper. Manag.* · 30 citations

> Motivated by the trend toward more collaboration in work flows, we study networks where some activities require the simultaneous processing by multiple types of multitasking human resources. Collaboration imposes constraints on the capacity of the process because multitasking resources have to be simultaneously at the right place. We introduce the notions of collaboration architecture and unavoidable bottleneck idleness to study the maximal throughput or capacity of such networks. Collaboration and multitasking introduce synchronization requirements that may inflict unavoidable idleness of the bottleneck resources: even when the network is continuously busy (processing at capacity), bottleneck resources can never be fully utilized. The conventional approach that equates network capacity with bottleneck capacity is then incorrect because the network capacity is below that of the bottlenecks. In fact, the gap between the two can grow linearly with the number of collaborative activities. Our main result is that networks with nested collaboration architectures have no unavoidable bottleneck idleness. Then, regardless of the processing times of the various activities, the standard bottleneck procedure correctly identifies the network capacity. We also prove necessity in the sense that, for any nonnested architecture, there are values of processing times for which unavoidable idleness persists. The fundamental trade-off between collaboration and capacity does not disappear in multiserver networks and has important ramifications to service-system staffing. Yet, even in multiserver networks, a nested collaboration architecture still guarantees that the bottleneck capacity is achievable. Finally, simultaneous collaboration, as a process constraint, may limit the benefits of flexibility. We study the interplay of flexibility and unavoidable idleness and offer remedies derived from collaboration architectures.

------------------------------------------------------------------------

17\. · 100% match · 2011 · 30 cit/yr\
**Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback** ([link](https://doi.org/10.1109/TAC.2012.2202052))\
Bassam Bamieh, M. Jovanović, P. Mitra, and S. Patterson\
*IEEE Transactions on Automatic Control* · Dec 17, 2011 · 435 citations

> We consider distributed consensus and vehicular formation control problems. Specifically we address the question of whether local feedback is sufficient to maintain coherence in large-scale networks subject to stochastic disturbances. We define macroscopic performance measures which are global quantities that capture the notion of coherence; a notion of global order that quantifies how closely the formation resembles a solid object. We consider how these measures scale asymptotically with network size in the topologies of regular lattices in 1, 2, and higher dimensions, with vehicular platoons corresponding to the 1-D case. A common phenomenon appears where a higher spatial dimension implies a more favorable scaling of coherence measures, with a dimensions of 3 being necessary to achieve coherence in consensus and vehicular formations under certain conditions. In particular, we show that it is impossible to have large coherent 1-D vehicular platoons with only local feedback. We analyze these effects in terms of the underlying energetic modes of motion, showing that they take the form of large temporal and spatial scales resulting in an accordion-like motion of formations. A conclusion can be drawn that in low spatial dimensions, local feedback is unable to regulate large-scale disturbances, but it can in higher spatial dimensions. This phenomenon is distinct from, and unrelated to string instability issues which are commonly encountered in control problems for automated highways.

------------------------------------------------------------------------

18\. · 100% match · 2011 · 0.7 cit/yr\
**Bounding the coarse graining error in hidden Markov dynamics** ([link](https://doi.org/10.1016/j.aml.2012.02.002))\
D. Andrieux\
*Appl. Math. Lett.* · Apr 6, 2011 · 10 citations

> Abstract Lumping a Markov process introduces a coarser level of description that is useful in many contexts and applications. The dynamics on the coarse grained states is often approximated by its Markovian component. In this paper we derive finite-time bounds on the error in this approximation. These results hold for non-reversible dynamics and for probabilistic mappings between microscopic and coarse grained states.

------------------------------------------------------------------------

19\. · 100% match · 2004 · 80 cit/yr\
**Control under communication constraints** ([link](https://doi.org/10.1109/TAC.2004.831187))\
S. Tatikonda and S. Mitter\
*IEEE Transactions on Automatic Control* · Jul 12, 2004 · 1745 citations

------------------------------------------------------------------------

20\. · 100% match · 2004 · 34 cit/yr\
**Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates** ([link](https://doi.org/10.1137/S0363012902402116))\
G. Nair and R. Evans\
*SIAM J. Control. Optim.* · Feb 1, 2004 · 753 citations

> Feedback control with limited data rates is an emerging area which incorporates ideas from both control and information theory. A fundamental question it poses is how low the closed-loop data rate can be made before a given dynamical system is impossible to stabilize by any coding and control law. Analogously to source coding, this defines the smallest error-free data rate sufficient to achieve “reliable” control, and explicit expressions for it have been derived for linear time-invariant systems without disturbances. In this paper, the more general case of finite-dimensional linear systems with process and observation noise is considered, the object being mean square state stability. By inductive arguments employing the entropy power inequality of information theory, and a new quantizer error bound, an explicit expression for the infimum stabilizing data rate is derived, under very mild conditions on the initial state and noise probability distributions.

------------------------------------------------------------------------

21\. · 100% match · 2011 · 9.3 cit/yr\
**Approximate Bisimulation: A Bridge Between Computer Science and Control Theory** ([link](https://doi.org/10.3166/ejc.17.568-578))\
A. Girard and George Pappas\
*Eur. J. Control* · 142 citations

> Fifty years ago, control and computing were part of a broader system science. After a long period of separate development within each discipline, embedded and hybrid systems have challenged us to reunite the, now sophisticated theories of continuous control and discrete computing on a broader system theoretic basis. In this paper, we present a framework of system approximation that applies to both discrete and continuous systems. We deﬁne a hierarchy of approximation metrics between two systems that quantify the quality of the approximation, and capture the established notions in computer science as zero sections. The central notions in this framework are that of approximate simulation and bisimulation relations and their functional characterizations called simulation and bisimulation functions and deﬁned by Lyapunov-type inequalities. In particular, these functions can provide computable upper-bounds on the approximation metrics by solving a static game. Our approximation framework will be illustrated by showing some of its applications in various problems such as reachability analysis of continuous systems and hybrid systems, approximation of continuous and hybrid systems by discrete systems, hierarchical control design, and simulation-based approaches to veriﬁcation of continuous and hybrid systems.

------------------------------------------------------------------------

22\. · 100% match · 2018 · 0.8 cit/yr\
**Hierarchical Control via an Approximate Aggregate Manifold** ([link](https://doi.org/10.23919/ACC.2018.8431887))\
Stanley W. Smith, M. Arcak, and Majid Zamani\
*2018 Annual American Control Conference (ACC)* · Jun 1, 2018 · 6 citations

> Typical aggregation procedures rely on an invariant manifold on which a detailed model of a system reduces to an aggregate model. In this paper we propose using an approximate aggregate manifold which need not be invariant. As a result, there exists a residual term in the dynamics relative to the manifold, whose effect we limit by including additional constraints in a formal synthesis of the controller for the aggregate system. We then refine the aggregate controller into an interface controller resulting in a bound on the error between the concrete and aggregate system, which we formalize using the notion of a simulation function. We demonstrate our approach with two examples: a platoon of vehicles with affine dynamics and a network of water tanks which falls into a particular class of nonlinear systems that we describe.

------------------------------------------------------------------------

23\. · 100% match · 2006 · 1.6 cit/yr\
**Information and closure in systems theory** ([link](https://www.semanticscholar.org/paper/846a8c33af45d6175643627b4df8fb0a9b63d423))\
Nils Bertschinger, E. Olbrich, N. Ay, and J. Jost\
32 citations

> The notion of closure plays a prominent role in systems theory where it is used to identify or deﬁne the system in distinction from its environment and to explain the autonomy of the system. Here, we present a quantitative measure, as opposed to the already existing qualitative notions, of closure. We shall elaborate upon the observation that cognitive systems can achieve informational closure by modeling their environment. Formally, then, a system is informationally closed if (almost) no information ﬂows into it from the environment. A system that is independent from its environment trivially achieves informational closure. Simulations of coupled hidden Markov models demonstrate that informational closure can also be realized non-trivially by modeling or controlling the environment. Our analysis of systems that actively inﬂuence their environment to achieve closure then reveals interesting connections to the related notion of autonomy. This discussion will then call into question the system-environment distinction that seems so innocent to begin with. It turns out that the notion of autonomy depends crucially on whether, not just the state observables, but also the dynamical processes are attributed to either the system or the environment. In that manner, our conceptualization of informational closure also sheds light on other, more ambitious notions of closure, e.g. organizational closure, semantic closure, closure to eﬃcient cause or operational closure, intended as a fundamental (deﬁning) concept of life itself.

------------------------------------------------------------------------

24\. · 100% match · 2006 · 28 cit/yr\
**Towards a Unified Theory of State Abstraction for MDPs** ([link](https://www.semanticscholar.org/paper/ca9a2d326b9de48c095a6cb5912e1990d2c5ab46))\
Lihong Li, Thomas J. Walsh, and M. Littman\
*AI&M* · 560 citations

> State abstraction (or state aggregation) has been extensively studied in the fields of artificial intelligence and operations research. Instead of working in the ground state space, the decision maker usually finds solutions in the abstract state space much faster by treating groups of states as a unit by ignoring irrelevant state information. A number of abstractions have been proposed and studied in the reinforcement-learning and planning literatures, and positive and negative results are known. We provide a unified treatment of state abstraction for Markov decision processes. We study five particular abstraction schemes, some of which have been proposed in the past in different forms, and analyze their usability for planning and learning.

------------------------------------------------------------------------

25\. · 100% match · 2016 · 15 cit/yr\
**When the Map Is Better Than the Territory** ([link](https://doi.org/10.3390/e19050188))\
Erik P. Hoel\
*ArXiv* · Dec 30, 2016 · 139 citations

> The causal structure of any system can be analyzed at a multitude of spatial and temporal scales. It has long been thought that while higher scale (macro) descriptions may be useful to observers, they are at best a compressed description and at worse leave out critical information and causal relationships. However, recent research applying information theory to causal analysis has shown that the causal structure of some systems can actually come into focus and be more informative at a macroscale. That is, a macroscale description of a system (a map) can be more informative than a fully detailed microscale description of the system (the territory). This has been called “causal emergence.” While causal emergence may at first seem counterintuitive, this paper grounds the phenomenon in a classic concept from information theory: Shannon’s discovery of the channel capacity. I argue that systems have a particular causal capacity, and that different descriptions of those systems take advantage of that capacity to various degrees. For some systems, only macroscale descriptions use the full causal capacity. These macroscales can either be coarse-grains, or may leave variables and states out of the model (exogenous, or “black boxed”) in various ways, which can improve the efficacy and informativeness via the same mathematical principles of how error-correcting codes take advantage of an information channel’s capacity. The causal capacity of a system can approach the channel capacity as more and different kinds of macroscales are considered. Ultimately, this provides a general framework for understanding how the causal structure of some systems cannot be fully captured by even the most detailed microscale description.

------------------------------------------------------------------------

26\. · 100% match · 2009 · 1.0 cit/yr\
**Bounding the lumping error in Markov chain dynamics** ([link](https://doi.org/10.1016/j.aml.2009.03.016))\
K. Hoffmann and P. Salamon\
*Appl. Math. Lett.* · Sep 1, 2009 · 17 citations

------------------------------------------------------------------------

27\. · 100% match · 2018 · 2.1 cit/yr\
**Approximate lumpability for Markovian agent-based models using local symmetries** ([link](https://doi.org/10.1017/jpr.2019.44))\
Wasiur R. KhudaBukhsh, Arnab Auddy, Y. Disser, and H. Koeppl\
*J. Appl. Probab.* · Apr 3, 2018 · 17 citations

> We study a Markovian agent-based model (MABM) in this paper. Each agent is endowed with a local state that changes over time as the agent interacts with its neighbours. The neighbourhood structure is given by a graph. Recently, Simon, Taylor, and Kiss \[40\] used the automorphisms of the underlying graph to generate a lumpable partition of the joint state space, ensuring Markovianness of the lumped process for binary dynamics. However, many large random graphs tend to become asymmetric, rendering the automorphism-based lumping approach ineffective as a tool of model reduction. In order to mitigate this problem, we propose a lumping method based on a notion of local symmetry, which compares only local neighbourhoods of vertices. Since local symmetry only ensures approximate lumpability, we quantify the approximation error by means of the Kullback–Leibler divergence rate between the original Markov chain and aliftedMarkov chain. We prove the approximation error decreases monotonically. The connections to fibrations of graphs are also discussed.

------------------------------------------------------------------------

28\. · 100% match · 2021 · 3.2 cit/yr\
**Can Decentralized Control Outperform Centralized? The Role of Communication Latency** ([link](https://doi.org/10.1109/TCNS.2023.3237483))\
Luca Ballotta, M. Jovanovi’c, and L. Schenato\
*IEEE Transactions on Control of Network Systems* · Sep 1, 2021 · 15 citations

> In this article, we examine the influence of communication latency on performance of networked control systems. Even though distributed control architectures offer advantages in terms of communication, maintenance costs, and scalability, it is an open question how communication latency that varies with network topology influences closed-loop performance. For networks in which delays increase with the number of links, we establish the existence of a fundamental performance tradeoff that arises from control architecture. In particular, we utilize consensus dynamics with single- and double-integrator agents to show that, if delays increase fast enough, a sparse controller with nearest neighbor interactions can outperform the centralized one with all-to-all communication topology.

------------------------------------------------------------------------

29\. · 100% match · 1999 · 34 cit/yr\
**Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback** ([link](https://doi.org/10.1109/9.763226))\
W. Wong and R. Brockett\
*IEEE Trans. Autom. Control.* · May 1, 1999 · 930 citations

> For part I, see ibid., vol.42, p.1294-8, 1997. In this paper a new class of feedback control problems is introduced. Unlike classical models, the systems considered here have communication channel constraints. As a result, the issue of coding and communication protocol becomes an integral part of the analysis. Since these systems cannot be asymptotically stabilized if the underlying dynamics are unstable, a weaker stability concept called containability is introduced. A key result connects containability with an inequality equation involving the communication data rate and the rate of change of the state.

------------------------------------------------------------------------

30\. · 100% match · 2016 · 6.7 cit/yr\
**Compositional Abstraction for Networks of Control Systems: A Dissipativity Approach** ([link](https://doi.org/10.1109/TCNS.2017.2670330))\
Majid Zamani and M. Arcak\
*IEEE Transactions on Control of Network Systems* · Aug 4, 2016 · 66 citations

> In this paper, we propose a compositional scheme for the construction of abstractions for networks of control systems by using the interconnection matrix and joint dissipativity-type properties of subsystems and their abstractions. In the proposed framework, the abstraction, itself a control system (possibly with a lower dimension), can be used as a substitution of the original system in the controller design process. Moreover, we provide a procedure for constructing abstractions of a class of nonlinear control systems by using the bounds on the slope of system nonlinearities. We illustrate the proposed results on a network of linear control systems by constructing its abstraction in a compositional way without requiring any condition on the number or gains of the subsystems. We use the abstraction as a substitute to synthesize a controller enforcing a certain linear temporal logic specification. This example particularly elucidates the effectiveness of dissipativity-type compositional reasoning for large-scale systems.

------------------------------------------------------------------------

31\. · 100% match · 2024 · 3.2 cit/yr\
**Formal error bounds for the state space reduction of Markov chains** ([link](https://doi.org/10.1016/j.peva.2024.102464))\
Fabian Michel and Markus Siegle\
*Perform. Evaluation* · Mar 12, 2024 · 7 citations

> We study the approximation of a Markov chain on a reduced state space, for both discrete- and continuous-time Markov chains. In this context, we extend the existing theory of formal error bounds for the approximated transient distributions. As a special case, we consider aggregated (or lumped) Markov chains, where the state space reduction is achieved by partitioning the state space into macro states. In the discrete-time setting, we bound the stepwise increment of the error, and in the continuous-time setting, we bound the rate at which the error grows. In addition, the same error bounds can also be applied to bound how far an approximated stationary distribution is from stationarity. Subsequently, we compare these error bounds with relevant concepts from the literature, such as exact and ordinary lumpability, as well as deflatability and aggregatability. These concepts define stricter than necessary conditions to identify settings in which the aggregation error is zero. We also consider possible algorithms for finding suitable aggregations for which the formal error bounds are low, and we analyse first experiments with these algorithms on a range of different models.

------------------------------------------------------------------------

32\. · 100% match · 2008 · 4.8 cit/yr\
**Bounding Performance Loss in Approximate MDP Homomorphisms** ([link](https://www.semanticscholar.org/paper/935f58066e63518f4e519ea44119772bc5b4ce1b))\
Jonathan Taylor, Doina Precup, and P. Panangaden\
*Neural Information Processing Systems* · Dec 8, 2008 · 83 citations

> We define a metric for measuring behavior similarity between states in a Markov decision process (MDP), which takes action similarity into account. We show that the kernel of our metric corresponds exactly to the classes of states defined by MDP homomorphisms (Ravindran & Barto, 2003). We prove that the difference in the optimal value function of different states can be upper-bounded by the value of this metric, and that the bound is tighter than previous bounds provided by bisimulation metrics (Ferns et al. 2004, 2005). Our results hold both for discrete and for continuous actions. We provide an algorithm for constructing approximate homomorphisms, by using this metric to identify states that can be grouped together, as well as actions that can be matched. Previous research on this topic is based mainly on heuristics.

------------------------------------------------------------------------

33\. · 100% match · 2015 · 11 cit/yr\
**LQG Control With Minimum Directed Information: Semidefinite Programming Approach** ([link](https://doi.org/10.1109/TAC.2017.2709618))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*IEEE Transactions on Automatic Control* · Oct 14, 2015 · 113 citations

> We consider a discrete-time linear–quadratic–Gaussian (LQG) control problem, in which Massey’s directed information from the observed output of the plant to the control input is minimized, while required control performance is attainable. This problem arises in several different contexts, including joint encoder and controller design for data-rate minimization in networked control systems. We show that the optimal control law is a linear–Gaussian randomized policy. We also identify the state-space realization of the optimal policy, which can be synthesized by an efficient algorithm based on semidefinite programming. Our structural result indicates that the filter–controller separation principle from the LQG control theory and the sensor–filter separation principle from the zero-delay rate-distortion theory for Gauss–Markov sources hold simultaneously in the considered problem. A connection to the data-rate theorem for mean-square stability by Nair and Evans is also established.

------------------------------------------------------------------------

34\. · 100% match · 2015 · 21 cit/yr\
**Biological organisation as closure of constraints.** ([link](https://doi.org/10.1016/j.jtbi.2015.02.029))\
Maël Montévil and M. Mossio\
*Journal of theoretical biology* · May 7, 2015 · 233 citations

> We propose a conceptual and formal characterisation of biological organisation as a closure of constraints. We first establish a distinction between two causal regimes at work in biological systems: processes, which refer to the whole set of changes occurring in non-equilibrium open thermodynamic conditions; and constraints, those entities which, while acting upon the processes, exhibit some form of conservation (symmetry) at the relevant time scales. We then argue that, in biological systems, constraints realise closure, i.e. mutual dependence such that they both depend on and contribute to maintaining each other. With this characterisation in hand, we discuss how organisational closure can provide an operational tool for marking the boundaries between interacting biological systems. We conclude by focusing on the original conception of the relationship between stability and variation which emerges from this framework.

------------------------------------------------------------------------

35\. · 100% match · 2003 · 19 cit/yr\
**Equivalence notions and model minimization in Markov decision processes** ([link](https://doi.org/10.1016/S0004-3702(02%2900376-4))\
R. Givan, T. Dean, and M. Greig\
*Artif. Intell.* · Jul 1, 2003 · 435 citations

------------------------------------------------------------------------

36\. · 100% match · 2003 · 9.9 cit/yr\
**Optimal state-space lumping in Markov chains** ([link](https://doi.org/10.1016/S0020-0190(03%2900343-0))\
Salem Derisavi, H. Hermanns, and W. Sanders\
*Inf. Process. Lett.* · Sep 30, 2003 · 224 citations

------------------------------------------------------------------------

37\. · 100% match · 2001 · 74 cit/yr\
**Stabilization of linear systems with limited information** ([link](https://doi.org/10.1109/9.948466))\
N. Elia and S. Mitter\
*IEEE Trans. Autom. Control.* · Sep 1, 2001 · 1817 citations

> We show that the coarsest, or least dense, quantizer that quadratically stabilizes a single input linear discrete time invariant system is logarithmic, and can be computed by solving a special linear quadratic regulator problem. We provide a closed form for the optimal logarithmic base exclusively in terms of the unstable eigenvalues of the system. We show how to design quantized state-feedback controllers, and quantized state estimators. This leads to the design of hybrid output feedback controllers. The theory is then extended to sampling and quantization of continuous time linear systems sampled at constant time intervals. We generalize the definition of density of quantization to the density of sampling and quantization in a natural way, and search for the coarsest sampling and quantization scheme that ensures stability. Finally, by relaxing the definition of quadratic stability, we show how to construct logarithmic quantizers with only finite number of quantization levels and still achieve practical stability of the closed-loop system.

------------------------------------------------------------------------

38\. · 100% match · 2016 · 12 cit/yr\
**Can the macro beat the micro? Integrated information across spatiotemporal scales.** ([link](https://doi.org/10.1093/nc/niw012))\
Erik P. Hoel, L. Albantakis, W. Marshall, and G. Tononi\
*Neuroscience of consciousness* · 127 citations

> Causal interactions within complex systems such as the brain can be analyzed at multiple spatiotemporal levels. It is widely assumed that the micro level is causally complete, thus excluding causation at the macro level. However, by measuring effective information-how much a system’s mechanisms constrain its past and future states-we recently showed that causal power can be stronger at macro rather than micro levels. In this work, we go beyond effective information and consider additional requirements of a proper measure of causal power from the intrinsic perspective of a system: composition (the cause-effect power of the parts), state-dependency (the cause-effect power of the system in a specific state); integration (the causal irreducibility of the whole to its parts), and exclusion (the causal borders of the system). A measure satisfying these requirements, called Φ Max, was developed in the context of integrated information theory. Here, we evaluate Φ Max systematically at micro and macro levels in space and time using simplified neuronal-like systems. We show that for systems characterized by indeterminism and/or degeneracy, Φ can indeed peak at a macro level. This happens if coarse-graining micro elements produces macro mechanisms with high irreducible causal selectivity. These results are relevant to a theoretical account of consciousness, because for integrated information theory the spatiotemporal maximum of integrated information fixes the spatiotemporal scale of consciousness. More generally, these results show that the notions of macro causal emergence and micro causal exclusion hold when causal power is assessed in full and from the intrinsic perspective of a system.

------------------------------------------------------------------------

39\. · 100% match · 2008 · 6.0 cit/yr\
**Autonomy: An information theoretic perspective** ([link](https://doi.org/10.1016/j.biosystems.2007.05.018))\
Nils Bertschinger, E. Olbrich, N. Ay, and J. Jost\
*Bio Systems* · Feb 1, 2008 · 110 citations

------------------------------------------------------------------------

40\. · 100% match · 2001 · 2.7 cit/yr\
**Compositional Abstractions of Hybrid Control Systems** ([link](https://doi.org/10.1109/CDC.2001.980125))\
P. Tabuada, George Pappas, and P. Lima\
*Discrete Event Dynamic Systems* · Dec 4, 2001 · 65 citations

> Abstraction is a natural way to hierarchically decompose the analysis and design of hybrid systems. Given a hybrid control system and some desired properties, one extracts an abstracted system while preserving the properties of interest. Abstractions of purely discrete systems is a mature area, whereas abstractions of continuous systems is a recent activity. In this paper we present a framework for abstraction that applies to discrete, continuous, and hybrid systems. We introduce a composition operator that allows to build complex hybrid systems from simpler ones and show compatibility between abstractions and this compositional operator. Besides unifying the existing methodologies we also propose constructions to obtain abstractions of hybrid control systems.

------------------------------------------------------------------------

41\. · 100% match · 2004 · 218 cit/yr\
**Information flow and cooperative control of vehicle formations** ([link](https://doi.org/10.3182/20020721-6-ES-1901.00100))\
J. A. Fax and R. Murray\
*IEEE Transactions on Automatic Control* · Sep 13, 2004 · 4731 citations

------------------------------------------------------------------------

42\. · 100% match · 1992 · 0.0 cit/yr\
**LUMPABILITY AND AGGREGATION OF MARKOVIAN SUBMODELS** ([link](https://www.semanticscholar.org/paper/19a406d08c3912bd9acf1163af5a8b4bed567a81))\
P. Buchholz\
1 citations

> Hierarchical Markovian models are an adequate paradigm for the modeling of complex systems. For the analysis of such models decomposition and aggregation techniques are very important, since the Markov chain described by a complex model often has a size that exceeds the capacity of contemporary computer equipment by orders of a magnitude. A class of hierarchical Markovian models is deened and a new aggregation technique is presented, which allows the aggregation of isolated submodels and the substitution of submodels by less complex aggregates and often reduces the size of the underlying Markov chain dramatically. The ag-gregation technique is based on the generation of (approximative) lumpable partitions on the submodels state space and allows the construction of aggregates introducing various degrees of approximation.

------------------------------------------------------------------------

43\. · 100% match · 2014 · 4.6 cit/yr\
**A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level** ([link](https://doi.org/10.1109/TAC.2015.2500658))\
Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina\
*IEEE Transactions on Automatic Control* · Jul 1, 2014 · 55 citations

> This paper studies networked control systems closed over noiseless digital channels. We focus on noisy linear time-invariant (LTI) plants with stationary Gaussian disturbances, Gaussian initial state, scalar-valued control inputs and sensor outputs. For this set-up, we show that the absolute minimal directed information rate that allows one to achieve a prescribed level of performance (not necessarily stationary), over all combinations of encoder-controller-decoder, is achieved when the decoder output is jointly Gaussian with the other signals in the system. This directed information rate lower bounds the achievable operational data rates. When restricting our attention to encoder-controller-decoders which make the random processes in the loop (strongly) asymptotically wide-sense stationary, this bound can be expressed in terms of their asymptotic power spectral densities. Then we show that the directed information rate and stationary performance of any such scheme can be achieved when the concatenated encoder, channel, controller and decoder behave as an AWGN channel with LTI filters. We also present a simple coding scheme that allows one to achieve (operational) average data rates that are at most (approximately) 1.254 bits away from the derived lower bound, while satisfying the performance constraint. A numerical example is presented to illustrate our findings.

------------------------------------------------------------------------

44\. · 100% match · 2015 · 4.1 cit/yr\
**Approximations of Stochastic Hybrid Systems: A Compositional Approach** ([link](https://doi.org/10.1109/TAC.2016.2619419))\
Majid Zamani, M. Rungger, and Peyman Mohajerin Esfahani\
*IEEE Transactions on Automatic Control* · Aug 26, 2015 · 44 citations

> In this paper we propose a compositional framework for the construction of approximations of the interconnection of a class of stochastic hybrid systems. As special cases, this class of systems includes both jump linear stochastic systems and linear stochastic hybrid automata. In the proposed framework, an approximation is itself a stochastic hybrid system, which can be used as a replacement of the original stochastic hybrid system in a controller design process. We employ a notion of so-called stochastic simulation function to quantify the error between the approximation and the original system. In the first part of the paper, we derive sufficient conditions which facilitate the compositional quantification of the error between the interconnection of stochastic hybrid subsystems and that of their approximations using the quantified error between the stochastic hybrid subsystems and their corresponding approximations. In particular, we show how to construct stochastic simulation functions for approximations of interconnected stochastic hybrid systems using the stochastic simulation function for the approximation of each component. In the second part of the paper, we focus on a specific class of stochastic hybrid systems, namely, jump linear stochastic systems, and propose a constructive scheme to determine approximations together with their stochastic simulation functions for this class of systems. Finally, we illustrate the effectiveness of the proposed results by constructing an approximation of the interconnection of four jump linear stochastic subsystems in a compositional way.

------------------------------------------------------------------------

45\. · 100% match · 2017 · 1.2 cit/yr\
**Approximate and Exact Solutions of Intertwining Equations Through Random Spanning Forests** ([link](https://doi.org/10.1007/978-3-030-60754-8_3))\
L. Avena, F. Castell, A. Gaudilliere, and Clothilde Mélot\
*Progress in Probability* · Feb 17, 2017 · 11 citations

> For different reversible Markov kernels on finite state spaces, we look for families of probability measures for which the time evolution almost remains in their convex hull. Motivated by signal processing problems and metastability studies we are interested in the case when the size of such families is smaller than the size of the state space, and we want such distributions to be with small overlap among them. To this aim we introduce a squeezing function to measure the common overlap of such families, and we use random forests to build random approximate solutions of the associated intertwining equations for which we can bound from above the expected values of both squeezing and total variation errors. We also explain how to modify some of these approximate solutions into exact solutions by using those eigenvalues of the associated Laplacian with the largest absolute values.

------------------------------------------------------------------------

46\. · 100% match · 2008 · 4.0 cit/yr\
**Bisimilar Finite Abstractions of Interconnected Systems** ([link](https://doi.org/10.1007/978-3-540-78929-1_37))\
Y. Tazaki and J. Imura\
*International Conference on Hybrid Systems: Computation and Control* · Apr 22, 2008 · 72 citations

------------------------------------------------------------------------

47\. · 100% match · 2014 · 1.9 cit/yr\
**Optimal high-level descriptions of dynamical systems** ([link](https://www.semanticscholar.org/paper/ba13d49c5b1c2a274b585094ea89c9a4e74ba5cb))\
D. Wolpert, Joshua A. Grochow, E. Libby, and S. Dedeo\
*arXiv: Information Theory* · Sep 25, 2014 · 22 citations

> To analyze high-dimensional systems, many fields in science and engineering rely on high-level descriptions, sometimes called “macrostates,” “coarse-grainings,” or “effective theories”. Examples of such descriptions include the thermodynamic properties of a large collection of point particles undergoing reversible dynamics, the variables in a macroeconomic model describing the individuals that participate in an economy, and the summary state of a cell composed of a large set of biochemical networks. Often these high-level descriptions are constructed without considering the ultimate reason for needing them in the first place. Here, we formalize and quantify one such purpose: the need to predict observables of interest concerning the high-dimensional system with as high accuracy as possible, while minimizing the computational cost of doing so. The resulting State Space Compression (SSC) framework provides a guide for how to solve for the {optimal} high-level description of a given dynamical system, rather than constructing it based on human intuition alone. In this preliminary report, we introduce SSC, and illustrate it with several information-theoretic quantifications of “accuracy”, all with different implications for the optimal compression. We also discuss some other possible applications of SSC beyond the goal of accurate prediction. These include SSC as a measure of the complexity of a dynamical system, and as a way to quantify information flow between the scales of a system.

------------------------------------------------------------------------

48\. · 100% match · 2015 · 23 cit/yr\
**Feedback Refinement Relations for the Synthesis of Symbolic Controllers** ([link](https://doi.org/10.1109/TAC.2016.2593947))\
G. Reissig, Alexander Weber, and M. Rungger\
*IEEE Transactions on Automatic Control* · Mar 12, 2015 · 258 citations

> We present an abstraction and refinement methodology for the automated controller synthesis to enforce general predefined specifications. The designed controllers require quantized (or symbolic) state information only and can be interfaced with the system via a static quantizer. Both features are particularly important with regard to any practical implementation of the designed controllers and, as we prove, are characterized by the existence of a feedback refinement relation between plant and abstraction. Feedback refinement relations are a novel concept introduced in this paper. Our work builds on a general notion of system with set-valued dynamics and possibly non-deterministic quantizers to permit the synthesis of controllers that robustly, and provably, enforce the specification in the presence of various types of uncertainties and disturbances. We identify a class of abstractions that is canonical in a well-defined sense, and provide a method to efficiently compute canonical abstractions. We demonstrate the practicality of our approach on two examples.

------------------------------------------------------------------------

49\. · 100% match · 2024 · 2.0 cit/yr\
**On Finding Optimal Collective Variables for Complex Systems by Minimizing the Deviation between Effective and Full Dynamics** ([link](https://doi.org/10.1137/24m1658917))\
Wei Zhang and Christof Schütte\
*Multiscale Model. Simul.* · May 3, 2024 · 4 citations

> This paper is concerned with collective variables, or reaction coordinates, that map a discrete-in-time Markov process $`X_n`$ in $`\mathbb{R}^d`$ to a (much) smaller dimension $`k \ll d`$. We define the effective dynamics under a given collective variable map $`\xi`$ as the best Markovian representation of $`X_n`$ under $`\xi`$. The novelty of the paper is that it gives strict criteria for selecting optimal collective variables via the properties of the effective dynamics. In particular, we show that the transition density of the effective dynamics of the optimal collective variable solves a relative entropy minimization problem from certain family of densities to the transition density of $`X_n`$. We also show that many transfer operator-based data-driven numerical approaches essentially learn quantities of the effective dynamics. Furthermore, we obtain various error estimates for the effective dynamics in approximating dominant timescales / eigenvalues and transition rates of the original process $`X_n`$ and how optimal collective variables minimize these errors. Our results contribute to the development of theoretical tools for the understanding of complex dynamical systems, e.g. molecular kinetics, on large timescales. These results shed light on the relations among existing data-driven numerical approaches for identifying good collective variables, and they also motivate the development of new methods.

------------------------------------------------------------------------

50\. · 100% match · 102 cit/yr\
**Approximate Homomorphisms : A framework for non-exact minimization in Markov Decision Processes** ([link](https://www.semanticscholar.org/paper/133583b9c4634702ab2579205ee3eb78714b7feb))\
Balaraman Ravindran\
102 citations

> To operate effectively in complex environments learning agents require the ability to selectively ignore irrelevant details and form useful abstractions. In earlier work we explored in detail what constitutes a useful abstraction in a stochastic sequential decision problem modeled as a Markov Decision Process (MDP). We based our approach on the notion of an MDP homomorphism. In this article we look at relaxing the strict conditions imposed earlier and introduce approximate homomorphisms that allow us to construct useful abstract models even when the homomorphism conditions are not met exactly. We also present a result on bounding the loss resulting from this approximation.

*Showing top 50 of 126 papers. Full details available via CSV or BibTeX export.*
