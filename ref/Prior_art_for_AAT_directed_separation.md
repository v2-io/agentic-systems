# Prior art for AAT directed separation

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which agent architectures are categorized by whether epistemic state (what is true, belief update, inference) and teleological or goal state (what is desired, action selection, planning) are causally separated or entangled. The core claim is that some architectures strictly separate belief updates from goals or control, while others entangle goals with observation processing and policy formation. The search should prioritize papers that formally categorize or compare agent architectures along this separation-versus-entanglement dimension, including work in AI safety, cognitive architectures, systems engineering for machine learning, active inference, control and estimation, cybernetics, theoretical neuroscience, cognitive science, and adjacent philosophical or systems-theoretic lineages when they provide clear conceptual or mathematical antecedents. Also find prior art for the claim that systems with entangled architectures can be externally scaffolded or wrapped so that belief-oriented queries and goal-oriented queries are strictly segregated, thereby coercing an entangled system into a more modular architecture at the cost of execution tempo or cognitive speed. Relevant matches include architectural taxonomies based on causal separation of perception, inference, valuation, and control; discussions distinguishing Friston blankets from Pearl blankets where this bears on goal-entangled perception; theoretical or empirical treatments of scaffolding, wrappers, or external orchestration around end-to-end models such as LLMs to enforce separation of concerns; and analyses of tempo, latency, serial bottlenecks, coordination overhead, communication constraints, or related speed costs that arise when modularizing or externally structuring cognitive or agentic systems. Broad antecedents are useful even if no paper states the full class unification directly. Exclude generic software modularity papers that do not specifically address the epistemic-versus-teleological divide in agents, and exclude active inference papers that simply assume entangled perception-action without comparing it to separated architectures or discussing scaffolding. Restrict the search to academic literature only.

*Found 107 papers · May 21, 2026 · Estimated coverage of relevant papers: 59%*

## Summary of Results

The strongest formal precedent for an AAT-style separation/entanglement taxonomy is the control-theoretic contrast between architectures where state estimation is sufficient and policy-independent \[1\], \[2\], \[3\], \[4\] and architectures with **dual effect**, where actions alter future information and estimation/control become intrinsically coupled \[5\], \[6\], \[7\].

#### Two recurring architectural families

- **Separated architectures**
  - Classical stochastic control and POMDP work factorizes belief update from action choice via an information state or filter feeding a controller/planner \[8\], \[9\], \[10\], \[11\].
  - AI agent architectures instantiate the same pattern more explicitly: world model / belief layer, then goal or intention management, then execution \[12\], \[13\], \[14\], \[15\].
- **Entangled architectures**
  - Active inference absorbs value into priors/preferences, making action selection and belief updating part of one variational process rather than a belief-then-control pipeline \[16\], \[17\], \[18\], \[19\].
  - Baltieri/Buckley make this contrast explicit, reading classical modularity through the separation principle and active inference as its nonmodular alternative \[20\], \[21\], \[22\].

#### Wrapping entangled systems into separated interfaces

- Prior art is weaker but present: hybrid/reactive-deliberative architectures and planner wrappers externally segregate modeling/querying from acting without changing the underlying substrate \[23\], \[24\], \[25\], \[26\].
- The main stated cost is **tempo**: bounded reaction time, serial bottlenecks, query/backtracking overhead, and communication-rate limits \[25\], \[26\], \[27\], \[28\], \[29\].
- For blanket terminology, the key antecedent is the Pearl-vs-Friston distinction, which clarifies when “perception-action coupling” is epistemic versus architectural/metaphysical \[30\].

## Paper Catalog (107 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2018 | 2.4 | The modularity of action and perception revisited using control theory and active inference ([link](https://doi.org/10.1162/isal_a_00031)) | Manuel Baltieri and C. Buckley | IEEE Symposium on Artificial Life |
| 2 | 1968 | 9.2 | On the Separation Theorem of Stochastic Control ([link](https://doi.org/10.1137/0306023)) | W. Wonham | Siam Journal on Control |
| 3 | 1971 | 10 | Separation of estimation and control for discrete time systems ([link](https://doi.org/10.1109/PROC.1971.8488)) | H. Witsenhausen |  |
| 4 | 2020 | 1.8 | On Kalman-Bucy filters, linear quadratic control and active inference ([link](https://www.semanticscholar.org/paper/c378ef9646a7c705d41ee9f77420b5259b797403)) | Manuel Baltieri and C. Buckley | arXiv: Neurons and Cognition |
| 5 | 1973 | 33 | The Optimal Control of Partially Observable Markov Processes over a Finite Horizon ([link](https://doi.org/10.1287/opre.21.5.1071)) | R. Smallwood and E. Sondik | Oper. Res. |
| 6 | 1969 | 0.5 | Separation theorem for nonlinear measurements ([link](https://doi.org/10.1109/JACC.1969.4169190)) | R. Curry | IEEE Transactions on Automatic Control |
| 7 | 2015 | 1.1 | LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | ArXiv |
| 8 | 2015 | 11 | LQG Control With Minimum Directed Information: Semidefinite Programming Approach ([link](https://doi.org/10.1109/TAC.2017.2709618)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | IEEE Transactions on Automatic Control |
| 9 | 1974 | 7.7 | Dual effect, certainty equivalence, and separation in stochastic control ([link](https://doi.org/10.1109/TAC.1974.1100635)) | Y. Bar-Shalom and E. Tse | IEEE Transactions on Automatic Control |
| 10 | 2014 | 1.4 | Partial-Information State-Based Optimization of Partially Observable Markov Decision Processes and the Separation Principle ([link](https://doi.org/10.1109/TAC.2013.2293397)) | Xi-Ren Cao, De-Xin Wang, and L. Qiu | IEEE Transactions on Automatic Control |
| 11 | 2012 | 16 | Active inference and agency: optimal control without cost functions ([link](https://doi.org/10.1007/s00422-012-0512-8)) | Karl J. Friston, Spyridon Samothrakis, and P. Montague | Biological Cybernetics |
| 12 | 1998 | 25 | The Belief-Desire-Intention Model of Agency ([link](https://doi.org/10.1007/3-540-49057-4_1)) | M. Georgeff, B. Pell, M. Pollack, Milind Tambe, and M. Wooldridge | ATAL |
| 13 | 2011 | 4.2 | The Separation Principle in Stochastic Control, Redux ([link](https://doi.org/10.1109/TAC.2013.2259207)) | T. Georgiou and A. Lindquist | IEEE Transactions on Automatic Control |
| 14 | 2001 | 3.8 | Teleo-Reactive Programs and the Triple-Tower Architecture ([link](https://www.semanticscholar.org/paper/77acafa1404f2fcaf02723f6366211e34d1fc8e6)) | N. Nilsson | Electron. Trans. Artif. Intell. |
| 15 | 1997 | 29 | On Three-Layer Architectures ([link](https://www.semanticscholar.org/paper/9b28b296a0225049d241cfe0ff1b39d7a14f68da)) | E. Gat |  |
| 16 | 2020 | 20 | Approximate information state for approximate planning and reinforcement learning in partially observed systems ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980)) | Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan | ArXiv |
| 17 | 1971 | 0.9 | On the optimal control of stochastic linear systems ([link](https://doi.org/10.1109/TAC.1971.1099840)) | E. Tse | IEEE Transactions on Automatic Control |
| 18 | 2023 |  | Intrinsic separation principles ([link](https://doi.org/10.1016/j.automatica.2025.112661)) | B. Houska | Autom. |
| 19 | 2021 | 22 | The Emperor’s New Markov Blankets ([link](https://doi.org/10.1017/S0140525X21002351)) | J. Bruineberg, K. Dołęga, Joe E. Dewhurst, and Manuel Baltieri | Behavioral and Brain Sciences |
| 20 | 2016 | 1.8 | Minimum-information LQG control part I: Memoryless controllers ([link](https://doi.org/10.1109/CDC.2016.7799131)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 21 | 2016 | 1.3 | Minimum-information LQG control Part II: Retentive controllers ([link](https://doi.org/10.1109/CDC.2016.7799130)) | Roy Fox and Naftali Tishby | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 22 | 1987 | 30 | Reactive Reasoning and Planning ([link](https://www.semanticscholar.org/paper/ceeae1a4e84591d26babdfe8969fad746853e40c)) | M. Georgeff and A. Lansky | AAAI Conference on Artificial Intelligence |
| 23 | 1973 | 3.2 | Wide-sense adaptive dual control for nonlinear stochastic systems ([link](https://doi.org/10.1109/TAC.1973.1100238)) | E. Tse, Y. Bar-Shalom, and L. Meier | IEEE Transactions on Automatic Control |
| 24 | 2019 | 1.5 | Nonmodular Architectures of Cognitive Systems based on Active Inference ([link](https://doi.org/10.1109/IJCNN.2019.8852048)) | Manuel Baltieri and C. Buckley | 2019 International Joint Conference on Neural Networks (IJCNN) |
| 25 | 1991 | 23 | Outline for a theory of intelligence ([link](https://doi.org/10.1109/21.97471)) | J. Albus | IEEE Trans. Syst. Man Cybern. |
| 26 | 2020 | 12 | On the Relationship Between Active Inference and Control as Inference ([link](https://doi.org/10.1007/978-3-030-64919-7_1)) | Beren Millidge, Alexander Tschantz, A. Seth, and C. Buckley | International Workshop on Affective Interactions |
| 27 | 2021 | 7.0 | Separation of learning and control for cyber-physical systems ([link](https://doi.org/10.1016/j.automatica.2023.110912)) | Andreas A. Malikopoulos | Autom. |
| 28 | 2020 | 0.3 | The Emperor’s New Markov Blankets ([link](https://www.semanticscholar.org/paper/774c759095801227de71454d7ce6e24669a4f28e)) | J. Bruineberg |  |
| 29 | 1974 | 3.0 | Optimization of stochastic linear systems with additive measurement and process noise using exponential performance criteria ([link](https://doi.org/10.1109/TAC.1974.1100606)) | J. Speyer, J. Deyst, and D. Jacobson | IEEE Transactions on Automatic Control |
| 30 | 2020 | 1.4 | Causal blankets: Theory and algorithmic framework ([link](https://doi.org/10.1007/978-3-030-64919-7_19)) | F. Rosas, P. Mediano, Martin Biehl, S. Chandaria, and D. Polani | International Workshop on Affective Interactions |
| 31 | 2004 | 0.5 | Utilizing Volatile External Information During Planning ([link](https://www.semanticscholar.org/paper/1b8148c90c2e15587a09741afa50c0f1106638b2)) | T. Au, Dana S. Nau, and V. Subrahmanian | European Conference on Artificial Intelligence |
| 32 | 1971 | 12 | The role and use of the stochastic linear-quadratic-Gaussian problem in control system design ([link](https://doi.org/10.1109/TAC.1971.1099818)) | M. Athans | Advances in Computers |
| 33 | 2021 | 32 | Active Inference: Demystified and Compared ([link](https://doi.org/10.1162/neco_a_01357)) | Noor Sajid, Philip J. Ball, and Karl J. Friston | Neural Computation |
| 34 | 1994 | 5.3 | Risk-sensitive control and dynamic games for partially observed discrete-time nonlinear systems ([link](https://doi.org/10.1109/9.286253)) | M. James, J. Baras, and R. Elliott | IEEE Trans. Autom. Control. |
| 35 | 2004 | 2.6 | Optimal LQG Control Across a Packet-Dropping Link ([link](https://www.semanticscholar.org/paper/584942eaded1d601688112ff9c637053e9f32cc3)) | V. Gupta, D. Spanos, B. Hassibi, and R. Murray |  |
| 36 | 2018 | 36 | Hierarchical Active Inference: A Theory of Motivated Control ([link](https://doi.org/10.1016/j.tics.2018.01.009)) | G. Pezzulo, Francesco Rigoli, and Karl J. Friston | Trends in Cognitive Sciences |
| 37 | 1981 | 1.6 | The certainty equivalence property in stochastic control theory ([link](https://doi.org/10.1109/TAC.1981.1102781)) | H. V. D. Water and J. Willems | IEEE Transactions on Automatic Control |
| 38 | 1983 | 1.5 | The adaptive LQG problem–Part I ([link](https://doi.org/10.1109/TAC.1983.1103212)) | O. Hijab | IEEE Transactions on Automatic Control |
| 39 | 1975 | 0.8 | Generalized certainty equivalence and dual effect in stochastic control ([link](https://doi.org/10.1109/TAC.1975.1101108)) | E. Tse and Y. Bar-Shalom | IEEE Transactions on Automatic Control |
| 40 | 2018 | 103 | Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review ([link](https://www.semanticscholar.org/paper/6ecc4b1ab05f3ec12484a0ea36abfd6271c5c5ba)) | S. Levine | ArXiv |
| 41 | 2023 | 1.2 | Dual Effect, Certainty Equivalence, and Separation Revisited: A Counterexample and a Relaxed Characterization for Optimality ([link](https://doi.org/10.1109/TAC.2022.3151189)) | M. Derpich and S. Yüksel | IEEE Transactions on Automatic Control |
| 42 | 1982 | 3.9 | Optimal Control for Partially Observed Diffusions ([link](https://doi.org/10.1137/0320021)) | W. Fleming and É. Pardoux | Siam Journal on Control and Optimization |
| 43 | 1972 | 10 | Team decision theory and information structures in optimal control problems–Part II ([link](https://doi.org/10.1109/TAC.1972.1099850)) | Y. Ho and K. Chu | IEEE Transactions on Automatic Control |
| 44 | 2017 | 26 | Stochastic model predictive control with active uncertainty learning: A Survey on dual control ([link](https://doi.org/10.1016/j.arcontrol.2017.11.001)) | A. Mesbah | Annu. Rev. Control. |
| 45 | 1976 | 0.5 | The Separation Principle in Stochastic Control via Girsanov Solutions ([link](https://doi.org/10.1137/0314015)) | Mark H. A. Davis | Siam Journal on Control and Optimization |
| 46 | 2009 | 24 | Optimal control as a graphical model inference problem ([link](https://doi.org/10.1007/s10994-012-5278-7)) | H. Kappen, V. Gómez, and M. Opper | Machine Learning |
| 47 | 2017 | 39 | The free energy principle for action and perception: A mathematical review ([link](https://doi.org/10.1016/J.JMP.2017.09.004)) | C. Buckley, C. S. Kim, Simon McGregor, and A. Seth | Journal of Mathematical Psychology |
| 48 | 1982 | 0.2 | Optimal control of partially observed diffusions via the separation principle ([link](https://doi.org/10.1007/BFB0044310)) | U. Haussmann |  |
| 49 | 2017 | 102 | Active Inference: A Process Theory ([link](https://doi.org/10.1162/NECO_a_00912)) | Karl J. Friston, Thomas H. B. FitzGerald, Francesco Rigoli, P. Schwartenbeck, and G. Pezzulo | Neural Computation |
| 50 | 1994 | 12 | Structured control for autonomous robots ([link](https://doi.org/10.1109/70.285583)) | R. Simmons | IEEE Trans. Robotics Autom. |
| 51 | 1965 | 15 | Optimal control of Markov processes with incomplete state information ([link](https://doi.org/10.1016/0022-247X(65%2990154-X)) | K. Åström | Journal of Mathematical Analysis and Applications |
| 52 | 1996 | 2.7 | Partially Observed Differential Games, Infinite-Dimensional Hamilton–Jacobi–Isaacs Equations, and Nonlinear $`H_\infty`$ Control ([link](https://doi.org/10.1137/S0363012994273337)) | M. James and J. Baras | Siam Journal on Control and Optimization |
| 53 | 1995 | 3.3 | Robust H/sub /spl infin// output feedback control for nonlinear systems ([link](https://doi.org/10.1109/9.388678)) | M. James and J. Baras | IEEE Transactions on Automatic Control |
| 54 | 2020 | 0.7 | A Bayesian perspective on classical control ([link](https://doi.org/10.1109/IJCNN48605.2020.9206617)) | Manuel Baltieri | 2020 International Joint Conference on Neural Networks (IJCNN) |
| 55 | 2018 | 29 | Generalised free energy and active inference ([link](https://doi.org/10.1007/s00422-019-00805-w)) | Thomas Parr and Karl J. Friston | Biological Cybernetics |
| 56 | 2019 | 0.7 | Active Inference: Computational Models of Motor Control without Efference Copy ([link](https://doi.org/10.32470/ccn.2019.1144-0)) | Manuel Baltieri and C. Buckley | 2019 Conference on Cognitive Computational Neuroscience |
| 57 | 2022 | 0.3 | On Separation Between Learning and Control in Partially Observed Markov Decision Processes ([link](https://www.semanticscholar.org/paper/1c75994d9034f6e4bbf22b9383d6c714badee7d7)) | Andreas A. Malikopoulos |  |
| 58 | 2015 | 61 | Active inference and epistemic value ([link](https://doi.org/10.1080/17588928.2015.1020053)) | Karl J. Friston et al. | Cognitive Neuroscience |
| 59 | 1990 | 6.9 | Plan guided reaction ([link](https://doi.org/10.1109/21.61207)) | D. Payton, Julio K. Rosenblatt, and D. Keirsey | IEEE Trans. Syst. Man Cybern. |
| 60 | 2009 | 27 | Reinforcement Learning or Active Inference? ([link](https://doi.org/10.1371/journal.pone.0006421)) | Karl J. Friston, J. Daunizeau, and S. Kiebel | PLoS ONE |
| 61 | 2020 | 6.6 | Modules or Mean-Fields? ([link](https://doi.org/10.3390/e22050552)) | Thomas Parr, Noor Sajid, and Karl J. Friston | Entropy |
| 62 | 1992 | 14 | Integrating Planning and Reacting in a Heterogeneous Asynchronous Architecture for Controlling Real-World Mobile Robots ([link](https://www.semanticscholar.org/paper/e8e7adda29ba259b29728a3b0c4dd0142e54c4fd)) | E. Gat | AAAI Conference on Artificial Intelligence |
| 63 | 2020 | 5.6 | Predictions in the eye of the beholder: an active inference account of Watt governors ([link](https://doi.org/10.1162/isal_a_00288)) | Manuel Baltieri, C. Buckley, and J. Bruineberg | IEEE Symposium on Artificial Life |
| 64 | 1966 | 1.3 | Stochastic Optimal Control with Noisy Observations ([link](https://doi.org/10.1080/00207176608921439)) | R. Mortensen | International Journal of Control |
| 65 | 1965 | 1.2 | Optimal control of partially observable Markovian systems ([link](https://doi.org/10.1016/0016-0032(65%2990528-4)) | M. Aoki | Journal of The Franklin Institute-engineering and Applied Mathematics |
| 66 | 2002 | 2.2 | Adaptive dual control ([link](https://www.semanticscholar.org/paper/9c1fe4c9791bab12e3a494664a71acd442c496af)) | B. Wittenmark |  |
| 67 | 2018 | 3.5 | Expanding the Active Inference Landscape: More Intrinsic Motivations in the Perception-Action Loop ([link](https://doi.org/10.3389/fnbot.2018.00045)) | Martin Biehl, C. Guckelsberger, Christoph Salge, Simón C. Smith, and D. Polani | Frontiers in Neurorobotics |
| 68 | 2019 | 17 | Learning action-oriented models through active inference ([link](https://doi.org/10.1371/journal.pcbi.1007805)) | Alexander Tschantz, A. Seth, and C. Buckley | PLoS Computational Biology |
| 69 | 1992 | 20 | Stochastic Control of Partially Observable Systems ([link](https://doi.org/10.1017/cbo9780511526503)) | A. Bensoussan |  |
| 70 | 1989 | 0.5 | Integrating Planning and Reactive Control ([link](https://www.semanticscholar.org/paper/3c583aee83460f0fbb98abc454fb94b23efed20d)) | S. Rosenschein and L. Kaelbling |  |
| 71 | 1987 | 11 | Reasoning about beliefs and actions under computational resource constraints ([link](https://doi.org/10.1016/0888-613x(88%2990148-x)) | E. Horvitz | ArXiv |
| 72 | 1999 | 0.7 | Integrating Planning and Reacting Architecture for Controlling ([link](https://www.semanticscholar.org/paper/b4bc8f2c9eab7f4b0f259408b83c5d0cc9d473cd)) | E. Gat |  |
| 73 | 2016 | 15 | Scene Construction, Visual Foraging, and Active Inference ([link](https://doi.org/10.3389/fncom.2016.00056)) | M. Berk Mirza, Rick A Adams, C. Mathys, and Karl J. Friston | Frontiers in Computational Neuroscience |
| 74 | 1994 | 1.0 | Planning to Behave: A Hybrid Deliberative/Reactive Robot Control Architecture for Mobile Manipulation ([link](https://www.semanticscholar.org/paper/152c2ca8353efea496683afc5ea6a5114e7fbb91)) | R. Arkin and D. MacKenzie |  |
| 75 | 1992 | 15 | An architecture for real-time reasoning and system control ([link](https://doi.org/10.1109/64.180407)) | F. Ingrand, M. Georgeff, and Anand Srinivasa Rao | IEEE Expert |
| 76 | 1990 | 1.5 | Managing Deliberation and Reasoning in Real-Time AI Systems ([link](https://www.semanticscholar.org/paper/f8f5d0dd872d4a1a26a8d9d3a98f12c9123f39dc)) | F. Ingrand and Michael Georgee |  |
| 77 | 1966 | 16 | Information Value Theory ([link](https://doi.org/10.1109/TSSC.1966.300074)) | R. Howard | IEEE Trans. Syst. Sci. Cybern. |
| 78 | 2011 | 6.1 | A graded BDI agent model to represent and reason about preferences ([link](https://doi.org/10.1016/j.artint.2010.12.006)) | Ana Casali, L. Godo, and C. Sierra | Artif. Intell. |
| 79 | 2015 |  | A design study for an Attention Filter Penetration architecture ([link](https://www.semanticscholar.org/paper/3add0a1cb956ecdd2beb216907bbdd210b036c25)) | B. Logan |  |
| 80 | 1993 | 2.2 | On the Role of Stored Internal State in the Control of Autonomous Mobile Robots ([link](https://doi.org/10.1609/aimag.v14i1.1034)) | E. Gat | AI Mag. |
| 81 | 2023 | 2.7 | Combining learning and control in linear systems ([link](https://doi.org/10.1016/j.ejcon.2024.101043)) | Andreas A. Malikopoulos | Eur. J. Control |
| 82 | 1975 | 0.2 | On certainty equivalence of stochastic optimal control problem ([link](https://doi.org/10.1080/00207177508922040)) | H. Akashi and K. Nose | International Journal of Control |
| 83 | 1992 | 0.2 | A Survey of Reactivity ([link](https://www.semanticscholar.org/paper/3a35c679e4a65b7be0308a69b979ca464b0e8e4a)) | S. Ravela |  |
| 84 | 2024 | 18 | Agents Thinking Fast and Slow: A Talker-Reasoner Architecture ([link](https://doi.org/10.48550/arXiv.2410.08328)) | Konstantina Christakopoulou, Shibl Mourad, and Maja Matari’c | ArXiv |
| 85 | 1972 | 0.2 | Linear stochastic control: An extended separation principle ([link](https://doi.org/10.1016/0022-247X(72%2990069-8)) | R. A. Brooks | Journal of Mathematical Analysis and Applications |
| 86 | 2006 | 28 | Probabilistic inference for solving discrete and continuous state Markov Decision Processes ([link](https://doi.org/10.1145/1143844.1143963)) | Marc Toussaint and A. Storkey | Proceedings of the 23rd international conference on Machine learning |
| 87 | 2023 | 2217 | LANGUAGE MODELS ([link](https://www.semanticscholar.org/paper/99832586d55f540f603637e458a292406a0ed75d)) | Shunyu Yao et al. |  |
| 88 | 2015 | 2.2 | The Umwelt of an embodied agent—a measure-theoretic definition ([link](https://doi.org/10.1007/s12064-015-0217-3)) | N. Ay and Wolfgang Löhr | Theory in Biosciences |
| 89 | 2025 | 12 | Position: Agent Should Invoke External Tools ONLY When Epistemically Necessary ([link](https://www.semanticscholar.org/paper/5cc514aa3991704514015539a61547f7838e039e)) | Hongru Wang et al. |  |
| 90 | 2017 | 2.7 | Stochastic Model Predictive Control: Output-Feedback, Duality and Guaranteed Performance ([link](https://doi.org/10.1016/j.automatica.2018.04.013)) | Martin A. Sehr and R. Bitmead |  |
| 91 | 2009 | 3.5 | Probabilistic inference as a model of planned behavior ([link](https://www.semanticscholar.org/paper/ab01cdba07ffc7163ea53640965e0057025a5456)) | Marc Toussaint | Künstliche Intell. |
| 92 | 2024 | 6.7 | Agent-state based policies in POMDPs: Beyond belief-state MDPs ([link](https://doi.org/10.1109/CDC56724.2024.10886046)) | Amit Sinha and Aditya Mahajan | 2024 IEEE 63rd Conference on Decision and Control (CDC) |
| 93 | 1994 | 0.3 | A Strong Separation Principle for Stochastic Control Systems Driven by a Hidden Markov Model ([link](https://doi.org/10.1137/S0363012992232233)) | R. Rishel | Siam Journal on Control and Optimization |
| 94 | 2025 | 2.0 | Compositional AI Beyond LLMs: System Implications of Neuro-Symbolic-Probabilistic Architectures ([link](https://doi.org/10.1145/3760250.3762235)) | Zishen Wan et al. | Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1 |
| 95 | 1981 | 0.3 | The separation principle for impulse control problems ([link](https://doi.org/10.1090/S0002-9939-1981-0612736-6)) | J. Menaldi |  |
| 96 | 2021 | 3.6 | Interpreting Dynamical Systems as Bayesian Reasoners ([link](https://doi.org/10.1007/978-3-030-93736-2_52)) | N. Virgo, Martin Biehl, and Simon McGregor | ArXiv |
| 97 | 2020 |  | Policy Distillation from World Models ([link](https://www.semanticscholar.org/paper/73ab50b009d3f0ee9b1f5adfb151b71d1a548b24)) |  |  |
| 98 | 2002 | 0.0 | A Framework for Splitting BDI Agents ([link](https://doi.org/10.1007/3-540-36078-6_11)) | Xiaocong Fan and J. Yen | Logic Programming and Automated Reasoning |
| 99 | 2021 | 11 | The Markov blanket trick: On the scope of the free energy principle and active inference. ([link](https://doi.org/10.1016/j.plrev.2021.09.001)) | Vicente Raja, Dinesh Valluri, E. Baggs, A. Chemero, and Michael L. Anderson | Physics of life reviews |
| 100 | 1984 | 0.2 | The separation principle for partially observed linear control systems: A general framework ([link](https://doi.org/10.1007/BFB0006562)) | N. Christopeit and K. Helmes |  |
| 101 | 1984 |  | An admissible systems approach to separation in partially observed stochastic control problems ([link](https://doi.org/10.1080/00207178408933218)) | T. Yoneyama | International Journal of Control |
| 102 | 2007 | 0.4 | Bayesian inference for motion control and planning ([link](https://doi.org/10.14279/DEPOSITONCE-10308)) | Marc Toussaint |  |
| 103 | 2007 | 1.5 | A separation principle for the H2-control of continuous-time infinite markov jump linear systems with partial observations ([link](https://doi.org/10.23919/ECC.2007.7068362)) | O. Costa and M. Fragoso | 2007 European Control Conference (ECC) |
| 104 | 2006 | 0.3 | Are Parallel BDI Agents Really Better? ([link](https://www.semanticscholar.org/paper/febcd6502d928a70c0b4cf7eea00ac74bf9415eb)) | Huiliang Zhang and Shell-Ying Huang | European Conference on Artificial Intelligence |
| 105 | 2026 |  | StreamVLA: Breaking the Reason-Act Cycle via Completion-State Gating ([link](https://doi.org/10.48550/arXiv.2602.01100)) | Tong Chen, Hang Wu, Jiasen Wang, Xiaotao Li, and Lu Fang | ArXiv |
| 106 | 2026 |  | The Separation Principle and the Dual-Certainty Equivalence Gap in Model Predictive Control ([link](https://www.semanticscholar.org/paper/3446ee6dcde9fd20323906e1bb7df000de908184)) | T. Baltussen, Nathan P. Lawrence, Alexander Katriniok, Ali Mesbah, and M. Heemels |  |
| 107 | 2025 |  | At the Intersection of Learning and Control for Emerging Mobility Systems ([link](https://doi.org/10.1109/CDC57313.2025.11312279)) | Andreas A. Malikopoulos | 2025 IEEE 64th Conference on Decision and Control (CDC) |

### Paper Details

1\. · 100% match · 2018 · 2.4 cit/yr\
**The modularity of action and perception revisited using control theory and active inference** ([link](https://doi.org/10.1162/isal_a_00031))\
Manuel Baltieri and C. Buckley\
*IEEE Symposium on Artificial Life* · Jun 7, 2018 · 19 citations

> The assumption that action and perception can be investigated independently is entrenched in theories, models and experimental approaches across the brain and mind sciences. In cognitive science, this has been a central point of contention between computationalist and 4Es (enactive, embodied, extended and embedded) theories of cognition, with the former embracing the “classical sandwich”, modular, architecture of the mind and the latter actively denying this separation can be made. In this work we suggest that the modular independence of action and perception strongly resonates with the separation principle of control theory and furthermore that this principle provides formal criteria within which to evaluate the implications of the modularity of action and perception. We will also see that real-time feedback with the environment, often considered necessary for the definition of 4Es ideas, is not however a sufficient condition to avoid the “classical sandwich”. Finally, we argue that an emerging framework in the cognitive and brain sciences, active inference, extends ideas derived from control theory to the study of biological systems while disposing of the separation principle, describing non-modular models of behaviour strongly aligned with 4Es theories of cognition.

------------------------------------------------------------------------

2\. · 100% match · 1968 · 9.2 cit/yr\
**On the Separation Theorem of Stochastic Control** ([link](https://doi.org/10.1137/0306023))\
W. Wonham\
*Siam Journal on Control* · May 1, 1968 · 536 citations

> Optimal control and filtering problem for stochastic linear dynamic system reduced to independent equations

------------------------------------------------------------------------

3\. · 100% match · 1971 · 10 cit/yr\
**Separation of estimation and control for discrete time systems** ([link](https://doi.org/10.1109/PROC.1971.8488))\
H. Witsenhausen\
Nov 1, 1971 · 556 citations

> An attempt is made to coordinate the numerous results relating to separation of estimation and control in discrete time stochastic control theory. The results vary widely depending upon the assumptions about linearity, criteria, information pattern, constraints, and noise distributions. Some of the less well-known underlying concepts are discussed with the help of a fairly general model.

------------------------------------------------------------------------

4\. · 100% match · 2020 · 1.8 cit/yr\
**On Kalman-Bucy filters, linear quadratic control and active inference** ([link](https://www.semanticscholar.org/paper/c378ef9646a7c705d41ee9f77420b5259b797403))\
Manuel Baltieri and C. Buckley\
*arXiv: Neurons and Cognition* · May 13, 2020 · 11 citations

> Linear Quadratic Gaussian (LQG) control is a framework first introduced in control theory that provides an optimal solution to linear problems of regulation in the presence of uncertainty. This framework combines Kalman-Bucy filters for the estimation of hidden states with Linear Quadratic Regulators for the control of their dynamics. Nowadays, LQG is also a common paradigm in neuroscience, where it is used to characterise different approaches to sensorimotor control based on state estimators, forward and inverse models. According to this paradigm, perception can be seen as a process of Bayesian inference and action as a process of optimal control. Recently, active inference has been introduced as a process theory derived from a variational approximation of Bayesian inference problems that describes, among others, perception and action in terms of (variational and expected) free energy minimisation. Active inference relies on a mathematical formalism similar to LQG, but offers a rather different perspective on problems of sensorimotor control in biological systems based on a process of biased perception. In this note we compare the mathematical treatments of these two frameworks for linear systems, focusing on their respective assumptions and highlighting their commonalities and technical differences.

------------------------------------------------------------------------

5\. · 100% match · 1973 · 33 cit/yr\
**The Optimal Control of Partially Observable Markov Processes over a Finite Horizon** ([link](https://doi.org/10.1287/opre.21.5.1071))\
R. Smallwood and E. Sondik\
*Oper. Res.* · Oct 1, 1973 · 1737 citations

> This paper formulates the optimal control problem for a class of mathematical models in which the system to be controlled is characterized by a finite-state discrete-time Markov process. The states of this internal process are not directly observable by the controller; rather, he has available a set of observable outputs that are only probabilistically related to the internal state of the system. The formulation is illustrated by a simple machine-maintenance example, and other specific application areas are also discussed. The paper demonstrates that, if there are only a finite number of control intervals remaining, then the optimal payoff function is a piecewise-linear, convex function of the current state probabilities of the internal Markov process. In addition, an algorithm for utilizing this property to calculate the optimal control policy and payoff function for any finite horizon is outlined. These results are illustrated by a numerical example for the machine-maintenance problem.

------------------------------------------------------------------------

6\. · 100% match · 1969 · 0.5 cit/yr\
**Separation theorem for nonlinear measurements** ([link](https://doi.org/10.1109/JACC.1969.4169190))\
R. Curry\
*IEEE Transactions on Automatic Control* · Oct 1, 1969 · 29 citations

> General solutions to the optimal stochastic control problem, or the combined estimation and control problem, are extremely difficult to compute since dynamic programming is required. However, if the system is linear, if the measurements are linear, and if the cost is quadratic, then the optimal stochastic controller is separated into 1) a filter to generate the conditional mean of the state, and 2) the optimum (linear) controller that results when all uncertainties are neglected. By altering the system configuration a new separation theorem is derived for arbitrary nonlinear measurements, discrete-time linear systems, and a quadratic cost. If a feedback loop is placed around the nonlinear measurement device (e.g., an analog-to-digital converter), then the stochastic control can be found without dynamic programming and is computed by cascading a nonlinear filter and the optimum (linear) controller. The primary advantage is the significant saving in computation. The performance of this new system configuration relative to the system without feedback depends on the nonlinearity, and it is not necessarily superior. A numerical example is presented.

------------------------------------------------------------------------

7\. · 100% match · 2015 · 1.1 cit/yr\
**LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis** ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*ArXiv* · Oct 14, 2015 · 12 citations

> In the interest of evaluating an information-theoretic requirement for feedback control, this paper proposes a framework to synthesize a control policy that minimizes Massey’s directed information from the state sequence to the control sequence while attaining required Linear-Quadratic-Gaussian (LQG) control performance. Interpretation and significance of this framework is discussed in the context of networked control theory. As the main result, we show that an optimal control policy can be realized by an attractively simple three-stage decision architecture comprising (1) a linear sensor with additive Gaussian noise, (2) a Kalman filter, and (3) a certainty equivalence controller. This result suggests an integration of two separation principles previously known in the literature: the filter-controller separation principle in the LQG control theory, and the sensorfilter separation principle in zero-delay rate-distortion theory for Gauss-Markov sources. It is also shown that an optimal policy can be synthesized by semidefinite programming (SDP). Both time-varying finite-horizon problems and time-invariant infinitehorizon problems are considered. Our results can be viewed as a generalization of the data-rate theorem for mean-square stability by Nair & Evans, extended for a control performance analysis.

------------------------------------------------------------------------

8\. · 100% match · 2015 · 11 cit/yr\
**LQG Control With Minimum Directed Information: Semidefinite Programming Approach** ([link](https://doi.org/10.1109/TAC.2017.2709618))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*IEEE Transactions on Automatic Control* · Oct 14, 2015 · 113 citations

> We consider a discrete-time linear–quadratic–Gaussian (LQG) control problem, in which Massey’s directed information from the observed output of the plant to the control input is minimized, while required control performance is attainable. This problem arises in several different contexts, including joint encoder and controller design for data-rate minimization in networked control systems. We show that the optimal control law is a linear–Gaussian randomized policy. We also identify the state-space realization of the optimal policy, which can be synthesized by an efficient algorithm based on semidefinite programming. Our structural result indicates that the filter–controller separation principle from the LQG control theory and the sensor–filter separation principle from the zero-delay rate-distortion theory for Gauss–Markov sources hold simultaneously in the considered problem. A connection to the data-rate theorem for mean-square stability by Nair and Evans is also established.

------------------------------------------------------------------------

9\. · 100% match · 1974 · 7.7 cit/yr\
**Dual effect, certainty equivalence, and separation in stochastic control** ([link](https://doi.org/10.1109/TAC.1974.1100635))\
Y. Bar-Shalom and E. Tse\
*IEEE Transactions on Automatic Control* · Oct 1, 1974 · 396 citations

> In this paper the various policies in fixed end-time stochastic control are discussed first. The emphasis is on the difference between the feedback and closed-loop policies. It is shown how the closed-loop policy has the important property that it can be actively adaptive, while the feedback policy can only be passively adaptive. The feature of being actively adaptive is possible when the control has a dual effect, i.e., in addition to its effect on the state it affects the state uncertainty. The intimate connection between the neutrality (lack of dual effect) and certainty equivalence properties for a class of problems is proved. This new result is then used to widen the class of problems for which it was previously known that the certainty equivalence property holds.

------------------------------------------------------------------------

10\. · 100% match · 2014 · 1.4 cit/yr\
**Partial-Information State-Based Optimization of Partially Observable Markov Decision Processes and the Separation Principle** ([link](https://doi.org/10.1109/TAC.2013.2293397))\
Xi-Ren Cao, De-Xin Wang, and L. Qiu\
*IEEE Transactions on Automatic Control* · Jan 27, 2014 · 17 citations

------------------------------------------------------------------------

11\. · 100% match · 2012 · 16 cit/yr\
**Active inference and agency: optimal control without cost functions** ([link](https://doi.org/10.1007/s00422-012-0512-8))\
Karl J. Friston, Spyridon Samothrakis, and P. Montague\
*Biological Cybernetics* · Oct 1, 2012 · 223 citations

> This paper describes a variational free-energy formulation of (partially observable) Markov decision problems in decision making under uncertainty. We show that optimal control can be cast as active inference. In active inference, both action and posterior beliefs about hidden states minimise a free energy bound on the negative log-likelihood of observed states, under a generative model. In this setting, reward or cost functions are absorbed into prior beliefs about state transitions and terminal states. Effectively, this converts optimal control into a pure inference problem, enabling the application of standard Bayesian filtering techniques. We then consider optimal trajectories that rest on posterior beliefs about hidden states in the future. Crucially, this entails modelling control as a hidden state that endows the generative model with a representation of agency. This leads to a distinction between models with and without inference on hidden control states; namely, agency-free and agency-based models, respectively.

------------------------------------------------------------------------

12\. · 100% match · 1998 · 25 cit/yr\
**The Belief-Desire-Intention Model of Agency** ([link](https://doi.org/10.1007/3-540-49057-4_1))\
M. Georgeff, B. Pell, M. Pollack, Milind Tambe, and M. Wooldridge\
*ATAL* · Jul 4, 1998 · 705 citations

------------------------------------------------------------------------

13\. · 100% match · 2011 · 4.2 cit/yr\
**The Separation Principle in Stochastic Control, Redux** ([link](https://doi.org/10.1109/TAC.2013.2259207))\
T. Georgiou and A. Lindquist\
*IEEE Transactions on Automatic Control* · Mar 15, 2011 · 64 citations

> Over the last 50 years, a steady stream of accounts have been written on the separation principle of stochastic control. Even in the context of the linear-quadratic regulator in continuous time with Gaussian white noise, subtle difficulties arise, unexpected by many, that are often overlooked. In this paper we propose a new framework for establishing the separation principle. This approach takes the viewpoint that stochastic systems are well-defined maps between sample paths rather than stochastic processes per se and allows us to extend the separation principle to systems driven by martingales with possible jumps. While the approach is more in line with “real-life” engineering thinking where signals travel around the feedback loop, it is unconventional from a probabilistic point of view in that control laws for which the feedback equations are satisfied almost surely, and not deterministically for every sample path, are excluded.

------------------------------------------------------------------------

14\. · 100% match · 2001 · 3.8 cit/yr\
**Teleo-Reactive Programs and the Triple-Tower Architecture** ([link](https://www.semanticscholar.org/paper/77acafa1404f2fcaf02723f6366211e34d1fc8e6))\
N. Nilsson\
*Electron. Trans. Artif. Intell.* · 95 citations

> I describe an architecture for linking perception and action in a robot. It consists of three “towers” of layered components. The “perception tower” contains rules that create increasingly abstract descriptions of the current environmental situation starting with the primitive predicates produced by the robot’s sensory apparatus. These descriptions are deposited in a “model tower” which is continuously kept faithful to the current environmental situation by a “truthmaintenance” system. The predicates in the model tower, in turn, evoke appropriate action-producing programs in the “action tower.” It is proposed that the actions be written as “teleo-reactive” programs—ones that react dynamically to changing situations in ways that lead inexorably toward their goals. Programs in the action tower are organized more-or-less hierarchically—bottoming out in programs that cause the robot to take primitive actions in its environment. The effects of the actions are sensed by the robot’s sensory mechanism, completing a sense-model-act cycle that is quiescent only at those times when the robot’s goal is perceived to be satisfied. I illustrate the operation of the architecture using a simple block-stacking task. I. Agent Architectures Can anything in general be said about intelligent agent architectures? Just as there are millions of species of animals, occupying millions of different niches, I expect that there will be many species of artificial agents—each a specialist for one of a countless number of tasks. The exact forms of their architectures will depend on their tasks and their environments. For example, some will work in time-stressed situations in which reactions to unpredictable and changing environmental states must be fast and unequivocal. Others will have the time and the knowledge to predict the effects of future courses of action so that more rational choices can be made. Even though there will probably never be a single, all-purpose agent architecture, there is one that I think might play a prominent role in many future systems. It can be viewed as an elaboration of 1 Parts of this section are adapted from Chapter 25 of my book, Artificial Intelligence: A New Synthesis, San Francisco: Morgan Kaufmann, 1998. 2 the first two levels of the popular three-level architectures that have been prominent in robotics research. A. Three-Level Architectures One of the first integrated intelligent agent systems was a collection of computer programs and hardware known as “Shakey the Robot” (Nilsson, 1984). Shakey’s design was an early example of what has come to be called a three-level architecture. The levels correspond to different paths from sensory signals to motor commands. At the lowest level of such architectures are actions that use a short and fast path from sensory signals to effectors. Important “reflexes” are handled by this pathway—such as “stop” when touch sensors detect a close object ahead. Servo control of motors for achieving set-point targets for shaft angles and so on are also handled by these low-level mechanisms. The intermediate level combines the low level actions into more complex behaviors—ones whose realization depends on the situation (as sensed and modeled) at the time of execution. This level uses more abstract (or more “coarse”) perceptual predicates and more complex actions than do the lower ones. Whereas reflex actions are typically evoked by primitive sensory signals, the coordination of intermediate-level actions requires more elaborate perceptual processing. The third level usually involves systems that can generate plans consisting of a sequence of intermediate level programs. The three-level architecture has been used in a variety of robot systems. As a typical example, see (Connell, 1992). B. The Triple-Tower Architecture A generalization of the three-level architecture has been proposed by Albus and colleagues (Albus, 1991; Albus, McCain, & Lumia, 1989). They envision hierarchies or “towers” of perceptual, modeling, and action processing. We propose here a particular instantiation of their triple-tower architecture. The novel features of our proposal are: 1. The use of teleo-reactive programs in the action tower 2. The use of perceptual rules in the perception tower. These rules create increasingly abstract predicates from simpler ones 3. The use of a truth-maintenance system (TMS) to keep the predicates in the model tower continuously faithful to changes in the sensed environment My version of this triple-tower architecture is illustrated in Figure 1. The operation of such a system would proceed as follows: Aspects of the environment that are relevant to the agent’s roles are sensed and converted to primitive predicates and values. These are stored at the lowest level of the model tower. Their presence there may immediately evoke primitive actions at the bottom of the action tower. These actions, in turn, affect the environment, and some of these effects may be sensed—creating a loop in which the environment itself might play an important computational role. 3 The perception tower consists of rules that convert predicates stored in the model tower into more abstract predicates which are then deposited at higher levels in the model tower. These processes can continue until even the highest levels of the model tower are populated. Fig. 1. A Triple-Tower Architecture The action tower consists of a loose hierarchy of action routines that are triggered by the contents of the model tower. The lowest level action routines are simple reflexes—evoked by predicates corresponding to primitive percepts. More complex actions are evoked by more abstract predicates appropriate for those actions. High-level actions “call” other actions until the process bottoms out at the primitive actions that actually affect the environment. We also allow for the possibility that the actions themselves might affect the model tower directly (in addition to the loop through the environment) by writing additional and/or altered content. With the ability both to read from and write in memory, the triple-tower structure is a perfectly general computational architecture. Sensors Model Tower (Predicates + TMS) Perception Tower (Rules) Action Tower (Action Routines)

------------------------------------------------------------------------

15\. · 100% match · 1997 · 29 cit/yr\
**On Three-Layer Architectures** ([link](https://www.semanticscholar.org/paper/9b28b296a0225049d241cfe0ff1b39d7a14f68da))\
E. Gat\
853 citations

> In the mid-1980’s Rodney Brooks touched off a firestorm of interest in autonomous robots with the introduction of the Subsumption architecture1 \[Brooks86\]. At the time, the dominant view in the AI community was that a control system for an autonomous mobile robot should be decomposed into three functional elements: a sensing system, a planning system, and an execution system \[Nilsson80\]. The job of the sensing system is to translate raw sensor input (usually sonar or vision data) into a world model. The job of the planner is to take the world model and a goal and generate a plan to achieve the goal. The job of the execution system is to take the plan and generate the actions it prescribes.

------------------------------------------------------------------------

16\. · 100% match · 2020 · 20 cit/yr\
**Approximate information state for approximate planning and reinforcement learning in partially observed systems** ([link](https://www.semanticscholar.org/paper/abde7540643e5093cba41a2e4554116bb9241980))\
Jayakumar Subramanian, Amit Sinha, Raihan Seraj, and A. Mahajan\
*ArXiv* · Oct 17, 2020 · 112 citations

> We propose a theoretical framework for approximate planning and learning in partially observed systems. Our framework is based on the fundamental notion of information state. We provide two equivalent definitions of information state—i) a function of history which is sufficient to compute the expected reward and predict its next value; ii) equivalently, a function of the history which can be recursively updated and is sufficient to compute the expected reward and predict the next observation. An information state always leads to a dynamic programming decomposition. Our key result is to show that if a function of the history (called approximate information state (AIS)) approximately satisfies the properties of the information state, then there is a corresponding approximate dynamic program. We show that the policy computed using this is approximately optimal with bounded loss of optimality. We show that several approximations in state, observation and action spaces in literature can be viewed as instances of AIS. In some of these cases, we obtain tighter bounds. A salient feature of AIS is that it can be learnt from data. We present AIS based multi-time scale policy gradient algorithms. and detailed numerical experiments with low, moderate and high dimensional environments.

------------------------------------------------------------------------

17\. · 100% match · 1971 · 0.9 cit/yr\
**On the optimal control of stochastic linear systems** ([link](https://doi.org/10.1109/TAC.1971.1099840))\
E. Tse\
*IEEE Transactions on Automatic Control* · Dec 1, 1971 · 47 citations

> The problem of controlling stochastic linear systems with quadratic criteria is considered. It is proved that the optimal control law can be realized by the cascade of a Kalman filter and a linear feedback. The importance of different assumptions required in this proof is discussed in detail. This discussion provides some motivation for different extension results.

------------------------------------------------------------------------

18\. · 100% match · 2023\
**Intrinsic separation principles** ([link](https://doi.org/10.1016/j.automatica.2025.112661))\
B. Houska\
*Autom.* · Jul 9, 2023 · 0 citations

> This paper is about output-feedback control problems for general linear systems in the presence of given state-, control-, disturbance-, and measurement error constraints. Because the traditional separation theorem in stochastic control is inapplicable to such constrained systems, a novel information-theoretic framework is proposed. It leads to an intrinsic separation principle that can be used to break the dual control problem for constrained linear systems into a meta-learning problem that minimizes an intrinsic information measure and a robust control problem that minimizes an extrinsic risk measure. The theoretical results in this paper can be applied in combination with modern polytopic computing methods in order to approximate a large class of dual control problems by finite-dimensional convex optimization problems.

------------------------------------------------------------------------

19\. · 100% match · 2021 · 22 cit/yr\
**The Emperor’s New Markov Blankets** ([link](https://doi.org/10.1017/S0140525X21002351))\
J. Bruineberg, K. Dołęga, Joe E. Dewhurst, and Manuel Baltieri\
*Behavioral and Brain Sciences* · Oct 22, 2021 · 100 citations

> Abstract The free energy principle, an influential framework in computational neuroscience and theoretical neurobiology, starts from the assumption that living systems ensure adaptive exchanges with their environment by minimizing the objective function of variational free energy. Following this premise, it claims to deliver a promising integration of the life sciences. In recent work, Markov blankets, one of the central constructs of the free energy principle, have been applied to resolve debates central to philosophy (such as demarcating the boundaries of the mind). The aim of this paper is twofold. First, we trace the development of Markov blankets starting from their standard application in Bayesian networks, via variational inference, to their use in the literature on active inference. We then identify a persistent confusion in the literature between the formal use of Markov blankets as an epistemic tool for Bayesian inference, and their novel metaphysical use in the free energy framework to demarcate the physical boundary between an agent and its environment. Consequently, we propose to distinguish between “Pearl blankets” to refer to the original epistemic use of Markov blankets and “Friston blankets” to refer to the new metaphysical construct. Second, we use this distinction to critically assess claims resting on the application of Markov blankets to philosophical problems. We suggest that this literature would do well in differentiating between two different research programmes: “inference with a model” and “inference within a model.” Only the latter is capable of doing metaphysical work with Markov blankets, but requires additional philosophical premises and cannot be justified by an appeal to the success of the mathematical framework alone.

------------------------------------------------------------------------

20\. · 100% match · 2016 · 1.8 cit/yr\
**Minimum-information LQG control part I: Memoryless controllers** ([link](https://doi.org/10.1109/CDC.2016.7799131))\
Roy Fox and Naftali Tishby\
*2016 IEEE 55th Conference on Decision and Control (CDC)* · Jun 6, 2016 · 18 citations

> With the increased demand for power efficiency in feedback-control systems, communication is becoming a limiting factor, raising the need to trade off the external cost that they incur with the capacity of the controller’s communication channels. With a proper design of the channels, this translates into a sequential rate-distortion problem, where we minimize the rate of information required for the controller’s operation under a constraint on its external cost. Memoryless controllers are of particular interest both for the simplicity and frugality of their implementation and as a basis for studying more complex controllers. In this paper we present the optimality principle for memoryless linear controllers that utilize minimal information rates to achieve a guaranteed external-cost level. We also study the interesting and useful phenomenology of the optimal controller, such as the principled reduction of its order.

------------------------------------------------------------------------

21\. · 100% match · 2016 · 1.3 cit/yr\
**Minimum-information LQG control Part II: Retentive controllers** ([link](https://doi.org/10.1109/CDC.2016.7799130))\
Roy Fox and Naftali Tishby\
*2016 IEEE 55th Conference on Decision and Control (CDC)* · Jun 6, 2016 · 13 citations

> Retentive (memory-utilizing) sensing-acting agents may operate under limitations on the communication between their sensing, memory and acting components, requiring them to trade off the external cost that they incur with the capacity of their communication channels. In this paper we formulate this problem as a sequential rate-distortion problem of minimizing the rate of information required for the controller’s operation under a constraint on its external cost. We reduce this bounded retentive control problem to the memoryless one, studied in Part I of this work \[1\], by viewing the memory reader as one more sensor and the memory writer as one more actuator. We further investigate the structure of the resulting optimal solution and demonstrate its interesting phenomenology.

------------------------------------------------------------------------

22\. · 100% match · 1987 · 30 cit/yr\
**Reactive Reasoning and Planning** ([link](https://www.semanticscholar.org/paper/ceeae1a4e84591d26babdfe8969fad746853e40c))\
M. Georgeff and A. Lansky\
*AAAI Conference on Artificial Intelligence* · Jul 13, 1987 · 1172 citations

> In this paper, the reasoning and planning capabilities of an autonomous mobile robot are described. The reasoning system that controls the robot is designed to exhibit the kind of behavior expected of a rational agent, and is endowed with the psychological attitudes of belief, desire, and intention. Because these attitudes are explicitly represented, they can be manipulated and reasoned about, resulting in complex goal-directed and reflective behaviors. Unlike most planning systems, the plans or intentions formed by the robot need only be partly elaborated before it decides to act. This allows the robot to avoid overly strong expectations about the environment, overly constrained plans of action, and other forms of overcommitment common to previous planners. In addition, the robot is continuously reactive and has the ability to change its goals and intentions as situations warrant. The system has been tested with SRI’s autonomous robot (Flakey) in a space station scenario involving navigation and the performance of emergency tasks.

------------------------------------------------------------------------

23\. · 100% match · 1973 · 3.2 cit/yr\
**Wide-sense adaptive dual control for nonlinear stochastic systems** ([link](https://doi.org/10.1109/TAC.1973.1100238))\
E. Tse, Y. Bar-Shalom, and L. Meier\
*IEEE Transactions on Automatic Control* · Apr 1, 1973 · 170 citations

> A new approach is presented for the problem of stochastic control of nonlinear systems. It is well known that, except for the linear-quadratic problem, the optimal stochastic controller cannot be obtained in practice. In general it is the curse of dimensionality that makes the strict application of the principle of optimality infeasible. The two subproblems of stochastic control, estimation and control proper, are, except for the linear-quadratic case, intercoupled. As pointed out by Feldbaum, in addition to its effects on the state of the system, the control also affects the estimation performance. In this paper, the control problem is formulated such that this dual property of the control appears explicitly. The resulting control sequence exhibits the closed-loop property, i.e., it takes into account the past observations and also the future observation program. Thus, in addition to being adaptive, this control also plans its future learning according to the control objective. Some preliminary simulation results illustrate these properties of the control.

------------------------------------------------------------------------

24\. · 100% match · 2019 · 1.5 cit/yr\
**Nonmodular Architectures of Cognitive Systems based on Active Inference** ([link](https://doi.org/10.1109/IJCNN.2019.8852048))\
Manuel Baltieri and C. Buckley\
*2019 International Joint Conference on Neural Networks (IJCNN)* · Mar 22, 2019 · 11 citations

> In psychology and neuroscience it is common to describe cognitive systems as input/output devices where perceptual and motor functions are implemented in a purely feedforward, open-loop fashion. On this view, perception and action are often seen as encapsulated modules with limited interaction between them. While embodied and enactive approaches to cognitive science have challenged the idealisation of the brain as an input/output device, we argue that even the more recent attempts to model systems using closed-loop architectures still heavily rely on a strong separation between motor and perceptual functions. Previously, we have suggested that the mainstream notion of modularity strongly resonates with the separation principle of control theory. In this work we present a minimal model of a sensorimotor loop implementing an architecture based on the separation principle. We link this to popular formulations of perception and action in the cognitive sciences, and show its limitations when, for instance, external forces are not modelled by an agent. These forces can be seen as variables that an agent cannot directly control, i.e., a perturbation from the environment or an interference caused by other agents. As an alternative approach inspired by embodied cognitive science, we then propose a nonmodular architecture based on active inference. We demonstrate the robustness of this architecture to unknown external inputs and show that the mechanism with which this is achieved in linear models is equivalent to integral control.

------------------------------------------------------------------------

25\. · 100% match · 1991 · 23 cit/yr\
**Outline for a theory of intelligence** ([link](https://doi.org/10.1109/21.97471))\
J. Albus\
*IEEE Trans. Syst. Man Cybern.* · May 1, 1991 · 801 citations

> Intelligence is defined as that which produces successful behavior. Intelligence is assumed to result from natural selection. A model is proposed that integrates knowledge from research in both natural and artificial systems. The model consists of a hierarchical system architecture wherein: (1) control bandwidth decreases about an order of magnitude at each higher level, (2) perceptual resolution of spatial and temporal patterns contracts about an order-of-magnitude at each higher level, (3) goals expand in scope and planning horizons expand in space and time about an order-of-magnitude at each higher level, and (4) models of the world and memories of events expand their range in space and time by about an order-of-magnitude at each higher level. At each level, functional modules perform behavior generation (task decomposition planning and execution), world modeling, sensory processing, and value judgment. Sensory feedback control loops are closed at every level. \>

------------------------------------------------------------------------

26\. · 100% match · 2020 · 12 cit/yr\
**On the Relationship Between Active Inference and Control as Inference** ([link](https://doi.org/10.1007/978-3-030-64919-7_1))\
Beren Millidge, Alexander Tschantz, A. Seth, and C. Buckley\
*International Workshop on Affective Interactions* · Jun 23, 2020 · 73 citations

> Active Inference (AIF) is an emerging framework in the brain sciences which suggests that biological agents act to minimise a variational bound on model evidence. Control-as-Inference (CAI) is a framework within reinforcement learning which casts decision making as a variational inference problem. While these frameworks both consider action selection through the lens of variational inference, their relationship remains unclear. Here, we provide a formal comparison between them and demonstrate that the primary difference arises from how value is incorporated into their respective generative models. In the context of this comparison, we highlight several ways in which these frameworks can inform one another.

------------------------------------------------------------------------

27\. · 100% match · 2021 · 7.0 cit/yr\
**Separation of learning and control for cyber-physical systems** ([link](https://doi.org/10.1016/j.automatica.2023.110912))\
Andreas A. Malikopoulos\
*Autom.* · Jul 13, 2021 · 34 citations

> Most cyber-physical systems (CPS) encounter a large volume of data which is added to the system gradually in real time and not altogether in advance. In this paper, we provide a theoretical framework that yields optimal control strategies for such CPS at the intersection of control theory and learning. In the proposed framework, we use the actual CPS, i.e., the”true”system that we seek to optimally control online, in parallel with a model of the CPS that is available. We then institute an information state for the system which does not depend on the control strategy. An important consequence of this independence is that for any given choice of a control strategy and a realization of the system’s variables until time t, the information states at future times do not depend on the choice of the control strategy at time t but only on the realization of the decision at time t, and thus they are related to the concept of separation between estimation of the state and control. Namely, the future information states are separated from the choice of the current control strategy. Such control strategies are called separated control strategies. Hence, we can derive offline the optimal control strategy of the system with respect to the information state, which might not be precisely known due to model uncertainties or complexity of the system, and then use standard learning approaches to learn the information state online while data are added gradually to the system in real time. We show that after the information state becomes known, the separated control strategy of the CPS model derived offline is optimal for the actual system. We illustrate the proposed framework in a dynamic system consisting of two subsystems with a delayed sharing information structure.

------------------------------------------------------------------------

28\. · 100% match · 2020 · 0.3 cit/yr\
**The Emperor’s New Markov Blankets** ([link](https://www.semanticscholar.org/paper/774c759095801227de71454d7ce6e24669a4f28e))\
J. Bruineberg\
2 citations

> Markov blankets have been used to settle disputes central to philosophy of mind and cognition. Their development from a technical concept in Bayesian inference to a central concept within the free-energy principle is analysed. We propose to distinguish between instrumental Pearl blankets and realist Friston blankets. Pearl blankets are substantiated by the empirical literature but can do limited philosophical work. Friston blankets can do philosophical work, but require strong theoretical assumptions. Both are conflated in the current literature on the free-energy principle. Consequently, we propose that distinguishing between an instrumental and a realist research program will help clarify the literature.

------------------------------------------------------------------------

29\. · 100% match · 1974 · 3.0 cit/yr\
**Optimization of stochastic linear systems with additive measurement and process noise using exponential performance criteria** ([link](https://doi.org/10.1109/TAC.1974.1100606))\
J. Speyer, J. Deyst, and D. Jacobson\
*IEEE Transactions on Automatic Control* · Aug 1, 1974 · 156 citations

> The expected value of a multiplicative performance criterion, represented by the exponential of a quadratic function of the state and control variables, is minimized subject to a discrete stochastic linear system with additive Gaussian measurement and process noise. This cost function, which is a generalization of the mean quadratic cost criterion, allows a degree of shaping of the probability density function of the quadratic cost criterion. In general, the control law depends upon a gain matrix which operates linearly on the smoothed history of the state vector from the initial to the current time. This gain matrix explicitly includes the covariance of the estimation errors of the entire state history. The separation theorem holds although the certainty equivalence principle does not. Two special cases are of importance. The first occurs when only the terminal state is costed. A feedback control law, linear in the current estimate of the state, results where the feedback gains are functionally dependent upon the error covariance of the current state estimate. The second occurs if all the intermediate states are costed but there is no process noise except for an initial condition uncertainty. A feedback law results which depends not only upon the current dynamical state estimate but also on an additional vector which is path dependent.

------------------------------------------------------------------------

30\. · 100% match · 2020 · 1.4 cit/yr\
**Causal blankets: Theory and algorithmic framework** ([link](https://doi.org/10.1007/978-3-030-64919-7_19))\
F. Rosas, P. Mediano, Martin Biehl, S. Chandaria, and D. Polani\
*International Workshop on Affective Interactions* · Aug 28, 2020 · 8 citations

> We introduce a novel framework to identify perception-action loops (PALOs) directly from data based on the principles of computational mechanics. Our approach is based on the notion of causal blanket, which captures sensory and active variables as dynamical sufficient statistics – i.e. as the “differences that make a difference.” Moreover, our theory provides a broadly applicable procedure to construct PALOs that requires neither a steady-state nor Markovian dynamics. Using our theory, we show that every bipartite stochastic process has a causal blanket, but the extent to which this leads to an effective PALO formulation varies depending on the integrated information of the bipartition.

------------------------------------------------------------------------

31\. · 100% match · 2004 · 0.5 cit/yr\
**Utilizing Volatile External Information During Planning** ([link](https://www.semanticscholar.org/paper/1b8148c90c2e15587a09741afa50c0f1106638b2))\
T. Au, Dana S. Nau, and V. Subrahmanian\
*European Conference on Artificial Intelligence* · Aug 22, 2004 · 11 citations

> There are many practical planning situations in which planners may need information from external sources during the planning process. We describe the following:
>
> • Wrappers that may be placed around conventional (isolated) planners. The wrapper replaces some of the planner’s memory accesses with queries to external information sources. When appropriate, the wrapper will automatically backtrack the planner to a previous point in its operation.
>
> • Query-management strategies for wrappers. These dictate when to issue queries, and when/how to backtrack the planner.
>
> • Mathematical analysis and experimental tests. Our results show conditions under which different query management strategies are preferable, and demonstrate that certain kinds of planning paradigms are more suited than others for planning with volatile information.

------------------------------------------------------------------------

32\. · 100% match · 1971 · 12 cit/yr\
**The role and use of the stochastic linear-quadratic-Gaussian problem in control system design** ([link](https://doi.org/10.1109/TAC.1971.1099818))\
M. Athans\
*Advances in Computers* · Dec 1, 1971 · 679 citations

> The role of the linear-quadratic stochastic control problem in engineering design is reviewed in tutorial fashion. The design approach is motivated by considering the control of a non-linear uncertain plant about a desired input-output response. It is demonstrated how a design philosophy based on 1) deterministic perturbation control, 2) stochastic state estimation, and 3) linearized stochastic control leads to an overall closed-loop control system. The emphasis of the paper is on the philosophy of the design process, the modeling issue, and the formulation of the problem; the results are given for the sake of completeness, but no proofs are included. The systematic off-line nature of the design process is stressed throughout.

------------------------------------------------------------------------

33\. · 99% match · 2021 · 32 cit/yr\
**Active Inference: Demystified and Compared** ([link](https://doi.org/10.1162/neco_a_01357))\
Noor Sajid, Philip J. Ball, and Karl J. Friston\
*Neural Computation* · Jan 5, 2021 · 173 citations

> Active inference is a first principle account of how autonomous agents operate in dynamic, nonstationary environments. This problem is also considered in reinforcement learning, but limited work exists on comparing the two approaches on the same discrete-state environments. In this letter, we provide (1) an accessible overview of the discrete-state formulation of active inference, highlighting natural behaviors in active inference that are generally engineered in reinforcement learning, and (2) an explicit discrete-state comparison between active inference and reinforcement learning on an OpenAI gym baseline. We begin by providing a condensed overview of the active inference literature, in particular viewing the various natural behaviors of active inference agents through the lens of reinforcement learning. We show that by operating in a pure belief-based setting, active inference agents can carry out epistemic exploration—and account for uncertainty about their environment—in a Bayes-optimal fashion. Furthermore, we show that the reliance on an explicit reward signal in reinforcement learning is removed in active inference, where reward can simply be treated as another observation we have a preference over; even in the total absence of rewards, agent behaviors are learned through preference learning. We make these properties explicit by showing two scenarios in which active inference agents can infer behaviors in reward-free environments compared to both Q-learning and Bayesian model-based reinforcement learning agents and by placing zero prior preferences over rewards and learning the prior preferences over the observations corresponding to reward. We conclude by noting that this formalism can be applied to more complex settings (e.g., robotic arm movement, Atari games) if appropriate generative models can be formulated. In short, we aim to demystify the behavior of active inference agents by presenting an accessible discrete state-space and time formulation and demonstrate these behaviors in a OpenAI gym environment, alongside reinforcement learning agents.

------------------------------------------------------------------------

34\. · 98% match · 1994 · 5.3 cit/yr\
**Risk-sensitive control and dynamic games for partially observed discrete-time nonlinear systems** ([link](https://doi.org/10.1109/9.286253))\
M. James, J. Baras, and R. Elliott\
*IEEE Trans. Autom. Control.* · Apr 1, 1994 · 169 citations

> Solves a finite-horizon partially observed risk-sensitive stochastic optimal control problem for discrete-time nonlinear systems and obtains small noise and small risk limits. The small noise limit is interpreted as a deterministic partially observed dynamic game, and new insights into the optimal solution of such game problems are obtained. Both the risk-sensitive stochastic control problem and the deterministic dynamic game problem are solved using information states, dynamic programming, and associated separated policies. A certainty equivalence principle is also discussed. The authors’ results have implications for the nonlinear robust stabilization problem. The small risk limit is a standard partially observed risk-neutral stochastic optimal control problem. \>

------------------------------------------------------------------------

35\. · 97% match · 2004 · 2.6 cit/yr\
**Optimal LQG Control Across a Packet-Dropping Link** ([link](https://www.semanticscholar.org/paper/584942eaded1d601688112ff9c637053e9f32cc3))\
V. Gupta, D. Spanos, B. Hassibi, and R. Murray\
59 citations

> We examine optimal Linear Quadratic Gaussian control for a system in which communication between the sensor (output of the plant) and the controller occurs across a packet-dropping link. We extend the familiar LQG separation principle to this problem that allows us to solve this problem using a standard LQR state-feedback design, along with an optimal algorithm for propagating and using the information across the unreliable link. We present one such optimal algorithm, which consists of a Kalman Filter at the sensor side of the link, and a switched linear filter at the controller side. Our design does not assume any statistical model of the packet drop events, and is thus optimal for an arbitrary packet drop pattern. Further, the solution is appealing from a practical point of view because it can be implemented as a small modification of an existing LQG control design.

------------------------------------------------------------------------

36\. · 96% match · 2018 · 36 cit/yr\
**Hierarchical Active Inference: A Theory of Motivated Control** ([link](https://doi.org/10.1016/j.tics.2018.01.009))\
G. Pezzulo, Francesco Rigoli, and Karl J. Friston\
*Trends in Cognitive Sciences* · Apr 1, 2018 · 295 citations

> Motivated control refers to the coordination of behaviour to achieve affectively valenced outcomes or goals. The study of motivated control traditionally assumes a distinction between control and motivational processes, which map to distinct (dorsolateral versus ventromedial) brain systems. However, the respective roles and interactions between these processes remain controversial. We offer a novel perspective that casts control and motivational processes as complementary aspects − goal propagation and prioritization, respectively − of active inference and hierarchical goal processing under deep generative models. We propose that the control hierarchy propagates prior preferences or goals, but their precision is informed by the motivational context, inferred at different levels of the motivational hierarchy. The ensuing integration of control and motivational processes underwrites action and policy selection and, ultimately, motivated behaviour, by enabling deep inference to prioritize goals in a context-sensitive way.

------------------------------------------------------------------------

37\. · 95% match · 1981 · 1.6 cit/yr\
**The certainty equivalence property in stochastic control theory** ([link](https://doi.org/10.1109/TAC.1981.1102781))\
H. V. D. Water and J. Willems\
*IEEE Transactions on Automatic Control* · Oct 1, 1981 · 73 citations

> In this paper we will give a general formulation of the certainty equivalence principle for stochastic optimal control problems. Special attention is paid to the question: “What do we mean by a certainty equivalence control law?” It is then shown that in this context the LQG-problem is indeed certainty equivalent.

------------------------------------------------------------------------

38\. · 94% match · 1983 · 1.5 cit/yr\
**The adaptive LQG problem–Part I** ([link](https://doi.org/10.1109/TAC.1983.1103212))\
O. Hijab\
*IEEE Transactions on Automatic Control* · Feb 1, 1983 · 65 citations

> This paper is concerned with a rigorous study of the “dual control” problem of Fel’dbaum, i.e., the LQG optimal control problem in the presence of Bayesian parameter uncertainty. The solution of this problem involves two parts, one relating to filtering and one to control. Although we establish our filtering result in complete generality in the last section, most of the paper concentrates on the finite parameter case to ease the exposition. The control result that we establish is incomplete in the sense that the smoothness of the optimal cost function is assumed rather than proved. Nevertheless, our results and methods are such that we arrive at a new proof of the classical separation theorem showing that the well-known LQG feedback law is optimal within the widest possible class of admissible controls. As this new proof avoids all talk of “dependence of the sigma algebra on the control,” “weak solutions,” “measure transformation techniques,” etc., we feel that this result will help to clarify what is involved in the classical separation theorem.

------------------------------------------------------------------------

39\. · 92% match · 1975 · 0.8 cit/yr\
**Generalized certainty equivalence and dual effect in stochastic control** ([link](https://doi.org/10.1109/TAC.1975.1101108))\
E. Tse and Y. Bar-Shalom\
*IEEE Transactions on Automatic Control* · Dec 1, 1975 · 39 citations

> This correspondence presents a generalized formulation of the certainty equivalence property for an arbitrary stochastic control problem. Using the definition of dual effect as introduced in earlier works, further results on the interrelation between dual effect and certainty equivalence property are obtained.

------------------------------------------------------------------------

40\. · 91% match · 2018 · 103 cit/yr\
**Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review** ([link](https://www.semanticscholar.org/paper/6ecc4b1ab05f3ec12484a0ea36abfd6271c5c5ba))\
S. Levine\
*ArXiv* · May 2, 2018 · 826 citations

> The framework of reinforcement learning or optimal control provides a mathematical formalization of intelligent decision making that is powerful and broadly applicable. While the general form of the reinforcement learning problem enables effective reasoning about uncertainty, the connection between reinforcement learning and inference in probabilistic models is not immediately obvious. However, such a connection has considerable value when it comes to algorithm design: formalizing a problem as probabilistic inference in principle allows us to bring to bear a wide array of approximate inference tools, extend the model in flexible and powerful ways, and reason about compositionality and partial observability. In this article, we will discuss how a generalization of the reinforcement learning or optimal control problem, which is sometimes termed maximum entropy reinforcement learning, is equivalent to exact probabilistic inference in the case of deterministic dynamics, and variational inference in the case of stochastic dynamics. We will present a detailed derivation of this framework, overview prior work that has drawn on this and related ideas to propose new reinforcement learning and control algorithms, and describe perspectives on future research.

------------------------------------------------------------------------

41\. · 90% match · 2023 · 1.2 cit/yr\
**Dual Effect, Certainty Equivalence, and Separation Revisited: A Counterexample and a Relaxed Characterization for Optimality** ([link](https://doi.org/10.1109/TAC.2022.3151189))\
M. Derpich and S. Yüksel\
*IEEE Transactions on Automatic Control* · Feb 1, 2023 · 4 citations

> In this article, we study the optimality of control policies admitting certainty equivalence or separation (of estimation and control) in discrete-time stochastic control, with the following two main contributions. We first revisit the influential theorem given in the seminal 1974 paper by Bar-Shalom and Tse, which studies the equivalence between certainty equivalence (CE) and no-dual-effect (NDE) properties in discrete-time stochastic control problems involving a linear dynamic system with a possibly nonlinear measurement function. We show that there is a subtle error in Bar-Shalom and Tse’s proof of the claim that CE implies NDE. Moreover, we prove that the claim does not hold by providing a counterexample. As our second and primary contribution, we introduce an alternative and a more relaxed notion of dual freeness and establish that this new notion is sufficient to guarantee the separation of estimation and control and CE in the same control problem considered by Bar-Shalom and Tse.

------------------------------------------------------------------------

42\. · 90% match · 1982 · 3.9 cit/yr\
**Optimal Control for Partially Observed Diffusions** ([link](https://doi.org/10.1137/0320021))\
W. Fleming and É. Pardoux\
*Siam Journal on Control and Optimization* · Mar 1, 1982 · 171 citations

> Stochastic control problems are considered in which a state process $`X_t`$ and an observation process $`Y_t`$ are governed by Ito-sense stochastic differential equations driven by independent Brownian motions. The control $`U_t`$ enters linearly in the dynamics of $`X_t`$. A “separated”control problem is introduced, in which the state at any time t is a measure $`\Lambda_t`$ representing an unnormalized conditional distribution for $`X_t`$ given $`Y_s`$, $`U_s`$ for $`s \leqq t`$. The method depends on introducing a pathwise version of $`\Lambda_t`$ which depends continuously on observation and control trajectories Y, U. Existence of an optimal control is obtained in a suitable class, larger than the usual class of controls admissible in the strict sense that $`U_t`$ is measurable on the \$\sigma \$-algebra $`\mathcal{F}_t (Y)`$ generated by observations $`Y_s`$, $`s \leqq t`$. The dynamics of $`\Lambda_t`$ are studied using a method of forward and backward partial differential equations. Under a suitable nondegeneracy condition, the m…

------------------------------------------------------------------------

43\. · 89% match · 1972 · 10 cit/yr\
**Team decision theory and information structures in optimal control problems–Part II** ([link](https://doi.org/10.1109/TAC.1972.1099850))\
Y. Ho and K. Chu\
*IEEE Transactions on Automatic Control* · Feb 1, 1972 · 563 citations

> General dynamic team decision problems with linear information structures and quadratic payoff functions are studied. The primitive random variables are jointly Gaussian. No constraints on the information structures are imposed except causality. Equivalence relations in information and in control functions among different systems are developed. These equivalence relations aid in the solving of many general problems by relating their solutions to those of the systems with “perfect memory.” The latter can be obtained by the method derived in Part I. A condition is found which enables each decision maker to infer the information available to his precedents, while at the same time the controls which will affect the information assessed can be proven optimal. When this condition fails, upper and lower bounds of the payoff function can still be obtained systematically, and suboptimal controls can be obtained.

------------------------------------------------------------------------

44\. · 87% match · 2017 · 26 cit/yr\
**Stochastic model predictive control with active uncertainty learning: A Survey on dual control** ([link](https://doi.org/10.1016/j.arcontrol.2017.11.001))\
A. Mesbah\
*Annu. Rev. Control.* · Nov 20, 2017 · 217 citations

------------------------------------------------------------------------

45\. · 86% match · 1976 · 0.5 cit/yr\
**The Separation Principle in Stochastic Control via Girsanov Solutions** ([link](https://doi.org/10.1137/0314015))\
Mark H. A. Davis\
*Siam Journal on Control and Optimization* · 26 citations

> This paper deals with the separation of estimation and control for linear systems with additive Gaussian white noise and nonquadratic cost function. All measurable functions of the observations are admissible as controls, the corresponding solutions being defined by the Girsanov measure transformation. The separation principle is established, under certain conditions, if the dimension of the observation process is equal to that of the state; if there are fewer observations, then additional ones of arbitrarily low signal-to-noise ratio can be adjoined such that there is a separated policy based on the augmented observations which is superior to any policy using the original observations.

------------------------------------------------------------------------

46\. · 85% match · 2009 · 24 cit/yr\
**Optimal control as a graphical model inference problem** ([link](https://doi.org/10.1007/s10994-012-5278-7))\
H. Kappen, V. Gómez, and M. Opper\
*Machine Learning* · Jan 6, 2009 · 410 citations

> We reformulate a class of non-linear stochastic optimal control problems introduced by Todorov (in Advances in Neural Information Processing Systems, vol. 19, pp. 1369–1376, 2007) as a Kullback-Leibler (KL) minimization problem. As a result, the optimal control computation reduces to an inference computation and approximate inference methods can be applied to efficiently compute approximate optimal controls. We show how this KL control theory contains the path integral control method as a special case. We provide an example of a block stacking task and a multi-agent cooperative game where we demonstrate how approximate inference can be successfully applied to instances that are too complex for exact computation. We discuss the relation of the KL control approach to other inference approaches to control.

------------------------------------------------------------------------

47\. · 85% match · 2017 · 39 cit/yr\
**The free energy principle for action and perception: A mathematical review** ([link](https://doi.org/10.1016/J.JMP.2017.09.004))\
C. Buckley, C. S. Kim, Simon McGregor, and A. Seth\
*Journal of Mathematical Psychology* · May 24, 2017 · 352 citations

> The ‘free energy principle’ (FEP) has been suggested to provide a unified theory of the brain, integrating data and theory relating to action, perception, and learning. The theory and implementation of the FEP combines insights from Helmholtzian ‘perception as inference’, machine learning theory, and statistical thermodynamics. Here, we provide a detailed mathematical evaluation of a suggested biologically plausible implementation of the FEP that has been widely used to develop the theory. Our objectives are (i) to describe within a single article the mathematical structure of this implementation of the FEP; (ii) provide a simple but complete agent-based model utilising the FEP and (iii) to disclose the assumption structure of this implementation of the FEP to help elucidate its significance for the brain sciences.

------------------------------------------------------------------------

48\. · 84% match · 1982 · 0.2 cit/yr\
**Optimal control of partially observed diffusions via the separation principle** ([link](https://doi.org/10.1007/BFB0044310))\
U. Haussmann\
11 citations

------------------------------------------------------------------------

49\. · 83% match · 2017 · 102 cit/yr\
**Active Inference: A Process Theory** ([link](https://doi.org/10.1162/NECO_a_00912))\
Karl J. Friston, Thomas H. B. FitzGerald, Francesco Rigoli, P. Schwartenbeck, and G. Pezzulo\
*Neural Computation* · 951 citations

> This article describes a process theory based on active inference and belief propagation. Starting from the premise that all neuronal processing (and action selection) can be explained by maximizing Bayesian model evidence—or minimizing variational free energy—we ask whether neuronal responses can be described as a gradient descent on variational free energy. Using a standard (Markov decision process) generative model, we derive the neuronal dynamics implicit in this description and reproduce a remarkable range of well-characterized neuronal phenomena. These include repetition suppression, mismatch negativity, violation responses, place-cell activity, phase precession, theta sequences, theta-gamma coupling, evidence accumulation, race-to-bound dynamics, and transfer of dopamine responses. Furthermore, the (approximately Bayes’ optimal) behavior prescribed by these dynamics has a degree of face validity, providing a formal explanation for reward seeking, context learning, and epistemic foraging. Technically, the fact that a gradient descent appears to be a valid description of neuronal activity means that variational free energy is a Lyapunov function for neuronal dynamics, which therefore conform to Hamilton’s principle of least action.

------------------------------------------------------------------------

50\. · 83% match · 1994 · 12 cit/yr\
**Structured control for autonomous robots** ([link](https://doi.org/10.1109/70.285583))\
R. Simmons\
*IEEE Trans. Robotics Autom.* · Feb 1, 1994 · 398 citations

> To operate in rich, dynamic environments, autonomous robots must be able to effectively utilize and coordinate their limited physical and computational resources. As complexity increases, it becomes necessary to impose explicit constraints on the control of planning, perception, and action to ensure that unwanted interactions between behaviors do not occur. This paper advocates developing complex robot systems by layering reactive behaviors onto deliberative components. In this structured control approach, the deliberative components handle normal situations and the reactive behaviors, which are explicitly constrained as to when and how they are activated, handle exceptional situations. The Task Control Architecture (TCA) has been developed to support this approach. TCA provides an integrated set of control constructs useful for implementing deliberative and reactive behaviors. The control constructs facilitate modular and evolutionary system development: they are used to integrate and coordinate planning, perception, and execution, and to incrementally improve the efficiency and robustness of the robot systems. To date, TCA has been used in implementing a half-dozen mobile robot systems, including an autonomous six-legged rover and indoor mobile manipulator. \>

*Showing top 50 of 107 papers. Full details available via CSV or BibTeX export.*
