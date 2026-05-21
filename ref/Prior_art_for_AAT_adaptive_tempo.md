# Prior art for AAT adaptive tempo

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which an agent adapts by decomposing prediction mismatch into reducible model error and irreducible observation noise, and the optimal proportion of mismatch used to correct the model is determined by the ratio of model uncertainty to total uncertainty. The search should prioritize formal mathematical predecessors of this uncertainty-weighted adaptive update law, including work that is mathematically equivalent even if it predates the modern epistemic-versus-aleatoric vocabulary, as well as broader conceptual predecessors. Relevant literature may come from adaptive control theory, online learning, machine learning theory, information geometry, active inference, theoretical neuroscience, cybernetics, and signal processing. Relevant matches include formal decompositions of prediction error into reducible versus irreducible components for real-time adaptation; generalizations of Kalman-gain-like uncertainty ratios to nonlinear, non-Gaussian, information-geometric, natural-gradient, or related operators; and mathematically close treatments of precision-weighted prediction errors, innovation covariance decompositions, or second-order online update rules with uncertainty weighting. Exclude standard deep learning optimization papers that do not track uncertainty or distinguish error types, purely hardware-based speed metrics, and generic linear-Gaussian Kalman filtering applications that do not extend the theory to more general adaptive or agentic update limits. Also find prior art for the claim that an agent’s adaptive capacity can be characterized by a single metric, “Adaptive Tempo,” defined as the product of event rate or loop speed and update gain or information quality. This part of the search should be broad: include both papers with an explicit product-form capacity metric and papers with closely related mathematical or conceptual formulations, such as learning effectiveness per unit time, bandwidth-limited adaptation, or information-rate times estimation-fidelity tradeoffs. Separate direct mathematical predecessors from broader conceptual lineage. Known anchors include the Kalman filter and its extensions, Fisher information and information geometry, formalizations related to the OODA loop, and work on epistemic versus aleatoric uncertainty in machine learning. Restrict the search to academic literature only.

*Found 137 papers · May 20, 2026 · Estimated coverage of relevant papers: 62%*

## Summary of Results

The clearest mathematical lineage for AAT’s uncertainty-weighted adaptive law runs from innovations/Kalman estimation—where correction is the innovation scaled by a gain determined by state uncertainty relative to total innovation uncertainty \[1\], \[2\]—through nonlinear, parameter-learning, and information-geometric generalizations that recover the same structure as natural-gradient/Bayesian updates \[3\], \[4\], \[5\], \[6\], \[7\].

#### Adaptive update law

- **Direct formal predecessors**
  - Innovation-covariance and adaptive-gain identification: unknown process/measurement noise handled by recursively estimating the quantities that set optimal gain \[2\], \[8\], \[9\], \[10\].
  - State/parameter adaptation beyond linear-Gaussian filtering: adaptive estimators decompose into a filtering part plus a nonlinear learning part, with online error-covariance evaluation \[11\], \[12\].
  - EKF/natural-gradient equivalence makes the gain ratio interpretable as Fisher-preconditioned online learning \[6\], \[7\].
- **Explicit reducible vs irreducible mismatch decompositions**
  - Volatility/stochasticity models separate change in latent state from observation noise and assign opposite effects on learning rate \[13\], \[14\], \[15\].
  - Hierarchical Gaussian Filter and active-inference/predictive-coding work express updates as precision-weighted prediction errors \[16\], \[17\], \[18\], \[19\].

#### “Adaptive Tempo” lineage

- **Direct mathematical relatives**
  - Strongest precedent is not an explicit named metric, but a recurring capacity form: adaptation is bounded jointly by update frequency / data rate and per-update information quality \[20\], \[21\], \[22\], \[23\], \[24\].
  - Event-triggered and value-of-information control make packet rate times informativeness operational \[25\], \[26\].
- **Broader conceptual lineage**
  - Early adaptive-control notions of adaptation rate and misadjustment \[27\], \[28\], learning efficiency as information absorbed per unit time \[29\], and control/information capacity formulations \[30\], \[31\].

## Paper Catalog (137 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 1970 | 24 | On the identification of variances and adaptive Kalman filtering ([link](https://doi.org/10.1109/TAC.1970.1099422)) | R. Mehra | IEEE Transactions on Automatic Control |
| 2 | 2017 | 7.9 | Online natural gradient as a Kalman filter ([link](https://doi.org/10.1214/18-EJS1468)) | Y. Ollivier | Electronic Journal of Statistics |
| 3 | 2014 | 35 | Uncertainty in perception and the Hierarchical Gaussian Filter ([link](https://doi.org/10.3389/fnhum.2014.00825)) | C. Mathys et al. | Frontiers in Human Neuroscience |
| 4 | 2010 | 82 | Attention, Uncertainty, and Free-Energy ([link](https://doi.org/10.3389/fnhum.2010.00215)) | H. Feldman and Karl J. Friston | Frontiers in Human Neuroscience |
| 5 | 2019 | 3.5 | The Extended Kalman Filter is a Natural Gradient Descent in Trajectory Space ([link](https://www.semanticscholar.org/paper/a5f7b5e3fce21d5b9d57df62d0f3e8093e48672e)) | Y. Ollivier | arXiv: Optimization and Control |
| 6 | 1998 | 126 | Natural Gradient Works Efficiently in Learning ([link](https://doi.org/10.1162/089976698300017746)) | S. Amari | Neural Computation |
| 7 | 1968 | 12 | An innovations approach to least-squares estimation–Part II: Linear smoothing in additive white noise ([link](https://doi.org/10.1109/TAC.1968.1099025)) | T. Kailath and P. Frost | IEEE Transactions on Automatic Control |
| 8 | 2010 | 9.9 | Generalised Filtering ([link](https://doi.org/10.1155/2010/621670)) | Karl J. Friston, K. Stephan, Baojuan Li, and J. Daunizeau |  |
| 9 | 1991 | 2.8 | On kalman filtering, posterior mode estimation and fisher scoring in dynamic exponential family regression ([link](https://doi.org/10.1007/BF02613597)) | L. Fahrmeir and H. Kaufmann | Metrika |
| 10 | 1973 | 3.0 | Identification of optimum filter steady-state gain for systems with unknown noise covariances ([link](https://doi.org/10.1109/TAC.1973.1100420)) | B. Carew and P. Belanger | IEEE Transactions on Automatic Control |
| 11 | 1972 | 0.2 | On stochastic approximation and an adaptive Kalman filter ([link](https://doi.org/10.1109/CDC.1972.268996)) | L. Scharf and D. Alspach | IEEE Conference on Decision and Control |
| 12 | 1996 | 7.5 | Neural Learning in Structured Parameter Spaces - Natural Riemannian Gradient ([link](https://www.semanticscholar.org/paper/fa0c75a9b5f39d166dd875005580687716a236bb)) | S. Amari | Neural Information Processing Systems |
| 13 | 1970 | 2.0 | Optimal adaptive estimation: Structure and parameter adaptation ([link](https://doi.org/10.1109/SAP.1970.269994)) | D. Lainiotis |  |
| 14 | 1992 | 5.2 | Posterior Mode Estimation by Extended Kalman Filtering for Multivariate Dynamic Generalized Linear Models ([link](https://doi.org/10.1080/01621459.1992.10475232)) | L. Fahrmeir | Journal of the American Statistical Association |
| 15 | 2021 | 9.0 | Synaptic plasticity as Bayesian inference ([link](https://doi.org/10.1038/s41593-021-00809-5)) | L. Aitchison et al. | Nature neuroscience |
| 16 | 2020 | 10 | A simple model for learning in volatile environments ([link](https://doi.org/10.1371/journal.pcbi.1007963)) | Payam Piray and N. Daw | PLoS Computational Biology |
| 17 | 2004 | 34 | Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates ([link](https://doi.org/10.1137/S0363012902402116)) | G. Nair and R. Evans | SIAM J. Control. Optim. |
| 18 | 2018 | 71 | A Novel Adaptive Kalman Filter With Inaccurate Process and Measurement Noise Covariance Matrices ([link](https://doi.org/10.1109/TAC.2017.2730480)) | Yulong Huang, Yonggang Zhang, Zhemin Wu, Ning Li, and J. Chambers | IEEE Transactions on Automatic Control |
| 19 | 1973 | 0.2 | Adaptive Kalman filtering using stochastic approximation ([link](https://doi.org/10.1049/EL:19730131)) | N. Sinha | Electronics Letters |
| 20 | 1981 | 18 | Implementation of self-tuning regulators with variable forgetting factors ([link](https://doi.org/10.1016/0005-1098(81%2990070-4)) | T. Fortescue, L. Kershenbaum, and B. Ydstie | Autom. |
| 21 | 2018 | 3.9 | Entropy and Minimal Bit Rates for State Estimation and Model Detection ([link](https://doi.org/10.1109/TAC.2017.2782478)) | D. Liberzon and S. Mitra | IEEE Transactions on Automatic Control |
| 22 | 2019 | 1.3 | Rate-Cost Tradeoffs in Control ([link](https://doi.org/10.1109/TAC.2019.2912256)) | V. Kostina and B. Hassibi | IEEE Transactions on Automatic Control |
| 23 | 1973 | 0.1 | The adaptation of observation noise covariances and adaptive Kalman filtering ([link](https://doi.org/10.1109/CDC.1973.269192)) | J. Lin | IEEE Conference on Decision and Control |
| 24 | 2020 | 20 | A model for learning based on the joint estimation of stochasticity and volatility ([link](https://doi.org/10.1038/s41467-021-26731-9)) | Payam Piray and N. Daw | Nature Communications |
| 25 | 2014 | 4.6 | A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level ([link](https://doi.org/10.1109/TAC.2015.2500658)) | Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina | IEEE Transactions on Automatic Control |
| 26 | 1997 | 20 | Systems with finite communication bandwidth constraints. I. State estimation problems ([link](https://doi.org/10.1109/9.623096)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 27 | 1973 |  | Linear stochastic optimal control under information rate constraints ([link](https://doi.org/10.1080/00207177308932375)) | R. Lefever and E. Stear | International Journal of Control |
| 28 | 1986 | 189 | Adaptive Filter Theory ([link](https://www.semanticscholar.org/paper/59a26a2d95db9b713c512d96b2a9e1eafb72d312)) | S. Haykin |  |
| 29 | 2015 | 1.1 | LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | ArXiv |
| 30 | 2022 | 0.2 | Optimal Causal Rate-Constrained Sampling of the Wiener Process ([link](https://doi.org/10.1109/TAC.2021.3071953)) | Nian Guo and V. Kostina | IEEE Transactions on Automatic Control |
| 31 | 2018 | 8.2 | Value of Information in Feedback Control: Quantification ([link](https://doi.org/10.1109/TAC.2021.3113472)) | T. Soleymani, J. Baras, and S. Hirche | IEEE Transactions on Automatic Control |
| 32 | 1986 |  | Optimum rate allocation in quantized control ([link](https://doi.org/10.1002/OCA.4660070405)) | C. Meadow, T. Fischer, and J. Gibson | Optimal Control Applications & Methods |
| 33 | 2014 | 10 | Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs ([link](https://doi.org/10.1109/TAC.2016.2601148)) | Takashi Tanaka, Kwang-Ki K. Kim, P. Parrilo, and S. Mitter | IEEE Transactions on Automatic Control |
| 34 | 2017 |  | Control Capacity ([link](https://doi.org/10.1109/TIT.2018.2868929)) | G. Ranade and Anant Sahai | IEEE Transactions on Information Theory |
| 35 | 1966 | 0.2 | Transmission of an analog signal over a fixed bit-rate channel ([link](https://doi.org/10.1109/TIT.1966.1053927)) | K. Steiglitz | IEEE Trans. Inf. Theory |
| 36 | 2020 | 15 | On the Identification of Noise Covariances and Adaptive Kalman Filtering: A New Look at a 50 Year-Old Problem ([link](https://doi.org/10.1109/ACCESS.2020.2982407)) | Lingyi Zhang et al. | IEEE access : practical innovations, open solutions |
| 37 | 1996 | 0.3 | Information theoretic tools for stable adaptation and learning (\[link\](https://doi.org/10.1002/(SICI%291099-1115(199607%2910:4/5\<499::AID-ACS397\>3.0.CO;2-M)) | S. Lloyd and J. Slotine | International Journal of Adaptive Control and Signal Processing |
| 38 | 1988 | 3.2 | Entropy formulation of optimal and adaptive control ([link](https://doi.org/10.1109/9.1287)) | G. Saridis | IEEE Transactions on Automatic Control |
| 39 |  | 387 | Natural Gradient Works Eciently in Learning ([link](https://www.semanticscholar.org/paper/e1c2a2fd6a26947e5bbb8df47e30c1199ab1270d)) | S. Amari |  |
| 40 | 2020 | 0.3 | Optimal Causal Rate-Constrained Sampling for a Class of Continuous Markov Processes ([link](https://doi.org/10.1109/tit.2021.3114142)) | Nian Guo and V. Kostina | IEEE Transactions on Information Theory |
| 41 | 2008 | 24 | The statistical determinants of adaptation rate in human reaching. ([link](https://doi.org/10.1167/8.4.20)) | Johannes Burge, M. Ernst, and M. Banks | Journal of vision |
| 42 | 1977 | 0.4 | Adaptive state estimation for systems with unknown noise covariances ([link](https://doi.org/10.1080/00207727708942048)) | N. Sinha and A. Tom | International Journal of Systems Science |
| 43 | 2017 | 0.9 | Information Geometric Approach to Recursive Update in Nonlinear Filtering ([link](https://doi.org/10.3390/e19020054)) | Yubo Li, Yongqiang Cheng, Xiang Li, Xiaoqiang Hua, and Yuliang Qin | Entropy |
| 44 | 2017 | 1.5 | Bayesian Nonlinear Filtering via Information Geometric Optimization ([link](https://doi.org/10.3390/e19120655)) | Yubo Li et al. | Entropy |
| 45 | 2026 |  | Online Generalised Predictive Coding ([link](https://www.semanticscholar.org/paper/be2fd86b7e22d14a4d7e88132a5dec0aa7509e7e)) | Mehran H. Bazargani, Szymon Urbas, Adeel Razi, T. Brendan Murphy, and Karl J. Friston |  |
| 46 | 2001 | 8.3 | Information-theoretic approach to the study of control systems ([link](https://doi.org/10.1016/j.physa.2003.09.007)) | H. Touchette and S. Lloyd | Physica A-statistical Mechanics and Its Applications |
| 47 | 2021 | 18 | Variational Adaptive Kalman Filter With Gaussian-Inverse-Wishart Mixture Distribution ([link](https://doi.org/10.1109/TAC.2020.2995674)) | Yulong Huang, Yonggang Zhang, P. Shi, and J. Chambers | IEEE Transactions on Automatic Control |
| 48 | 2009 | 23 | Relevance of error: what drives motor adaptation? ([link](https://doi.org/10.1152/jn.90545.2008)) | Kunlin Wei and Konrad Paul Kording | Journal of neurophysiology |
| 49 | 2020 | 1.4 | Stochastic Online Optimization using Kalman Recursion ([link](https://www.semanticscholar.org/paper/cfe373d89fe9ab88db055a8f792ecbc332a1910c)) | Joseph de Vilmarest and Olivier Wintenberger | J. Mach. Learn. Res. |
| 50 | 2017 | 5.2 | Intrinsically Bayesian Robust Kalman Filter: An Innovation Process Approach ([link](https://doi.org/10.1109/TSP.2017.2656845)) | Roozbeh Dehghannasiri and M. S. Esfahani | IEEE Transactions on Signal Processing |
| 51 | 2001 |  | Natural Gradient Learning and its Applications ([link](https://www.semanticscholar.org/paper/401912ee540e54f6c978293f62edee26417d6934)) | S. Amari |  |
| 52 | 1997 | 2.2 | Optimal state estimation for stochastic systems: an information theoretic approach ([link](https://doi.org/10.1109/9.587329)) | Xiangbo Feng, K. Loparo, and Yuguang Fang | IEEE Trans. Autom. Control. |
| 53 | 1972 |  | Stochastic Optimal Control with a Constrained Feedback Information Rate ([link](https://doi.org/10.1016/S1474-6670(17%2968363-0)) | E. Stear and R. Lefevre | IFAC Proceedings Volumes |
| 54 | 2012 | 11 | A Fresh Look at the Kalman Filter ([link](https://doi.org/10.1137/100799666)) | J. Humpherys, Preston Redd, and J. West | SIAM Rev. |
| 55 | 2025 |  | Causal inference, prediction and state estimation in sensorimotor learning ([link](https://doi.org/10.1098/rspb.2025.1320)) | Hyosub E. Kim, Romeo Chua, and Davin Hu | Proceedings of the Royal Society B: Biological Sciences |
| 56 | 2016 | 17 | Rate-cost tradeoffs in control ([link](https://doi.org/10.1109/ALLERTON.2016.7852366)) | V. Kostina and B. Hassibi | 2016 54th Annual Allerton Conference on Communication, Control, and Computing (Allerton) |
| 57 | 2018 | 0.9 | The decoupled extended Kalman filter for dynamic exponential-family factorization models ([link](https://www.semanticscholar.org/paper/14064f97eb6711ce80a311932d492c4ed446197a)) | C. Gomez-Uribe and B. Karrer | ArXiv |
| 58 | 1996 | 1.9 | On-line versus Off-line Learning from Random Examples: General Results. ([link](https://doi.org/10.1103/PHYSREVLETT.77.4671)) | Manfred Opper | Physical review letters |
| 59 | 2021 | 7.6 | Value of Information in Feedback Control: Global Optimality ([link](https://doi.org/10.1109/TAC.2022.3194125)) | T. Soleymani, J. Baras, S. Hirche, and K. Johansson | IEEE Transactions on Automatic Control |
| 60 | 1962 | 0.0 | Rate of Adaptation in Control Systems ([link](https://doi.org/10.2514/8.6293)) | B. Widrow | ARS Journal |
| 61 | 1994 | 5.9 | A recursive multiple model approach to noise identification ([link](https://doi.org/10.1109/7.303738)) | X. Li and Y. Bar-Shalom | IEEE Transactions on Aerospace and Electronic Systems |
| 62 | 2014 | 0.1 | On the Control Rate versus Quantizer-Resolution Trade Off in Networked Control ([link](https://doi.org/10.3182/20140824-6-ZA-1003.00827)) | M. Cea, G. Goodwin, A. Feuer, and D. Mayne | IFAC Proceedings Volumes |
| 63 | 2009 | 12 | Variational Bayesian identification and prediction of stochastic nonlinear dynamic causal models ([link](https://doi.org/10.1016/J.PHYSD.2009.08.002)) | J. Daunizeau, Karl J. Friston, and S. Kiebel | Physica D. Nonlinear Phenomena |
| 64 | 2020 | 0.9 | Information Rate in Humans during Visuomotor Tracking ([link](https://doi.org/10.3390/e23020228)) | Sze-Ying Lam and A. Zénon | Entropy |
| 65 | 2002 | 1.2 | Adaptive Classification by Variational Kalman Filtering ([link](https://www.semanticscholar.org/paper/0563508c86f05e2904c4c60713e0d1a70a8dd00f)) | P. Sykacek and S. Roberts | Neural Information Processing Systems |
| 66 | 2006 | 0.5 | Multiple timescales and uncertainty in motor adaptation ([link](https://doi.org/10.7551/mitpress/7503.003.0098)) | Konrad Paul Kording, J. Tenenbaum, and R. Shadmehr | Neural Information Processing Systems |
| 67 | 2021 | 7.7 | Variational Bayesian adaptation of process noise covariance matrix in Kalman filtering ([link](https://doi.org/10.1016/J.JFRANKLIN.2021.02.037)) | G. Chang, Chao Chen, Qiuzhao Zhang, and Shubi Zhang | J. Frankl. Inst. |
| 68 | 2016 | 0.2 | Rate-cost tradeoffs in control. Part I: lower bounds ([link](https://www.semanticscholar.org/paper/d3835bce423de4e4e1efd773cedf9057d88ad284)) | V. Kostina and B. Hassibi | ArXiv |
| 69 | 2020 | 6.3 | Neural Dynamics under Active Inference: Plausibility and Efficiency of Information Processing ([link](https://doi.org/10.3390/e23040454)) | Lancelot Da Costa, Thomas Parr, B. Sengupta, and Karl J. Friston | Entropy |
| 70 | 2022 | 1.8 | Uncertainty–guided learning with scaled prediction errors in the basal ganglia ([link](https://doi.org/10.1371/journal.pcbi.1009816)) | Moritz Moeller, S. Manohar, and R. Bogacz | PLoS Computational Biology |
| 71 | 2021 | 1.3 | Kalman filters as the steady-state solution of gradient descent on variational free energy ([link](https://www.semanticscholar.org/paper/e8b97e604cbc2a9430fcb017133491d3d4d2d50c)) | M. Baltieri and Takuya Isomura | ArXiv |
| 72 | 2022 | 8.1 | Adaptive Kalman Filtering for Recursive Both Additive Noise and Multiplicative Noise ([link](https://doi.org/10.1109/taes.2021.3117896)) | Xingkai Yu and Jian-xun Li | IEEE Transactions on Aerospace and Electronic Systems |
| 73 | 2018 | 8.1 | Learning optimal decisions with confidence ([link](https://doi.org/10.1073/pnas.1906787116)) | Jan Drugowitsch, André G. Mendonça, Z. Mainen, and A. Pouget | Proceedings of the National Academy of Sciences |
| 74 | 2017 | 27 | Uncertainty, epistemics and active inference ([link](https://doi.org/10.1098/rsif.2017.0376)) | Thomas Parr and Karl J. Friston | Journal of the Royal Society Interface |
| 75 | 1998 | 7.0 | Why natural gradient? ([link](https://doi.org/10.1109/ICASSP.1998.675489)) | S. Amari and S. Douglas | Proceedings of the 1998 IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP ’98 (Cat. No.98CH36181) |
| 76 | 2018 | 5.3 | Kalman filtering through the feedback adaption of prior error covariance ([link](https://doi.org/10.1016/J.SIGPRO.2018.05.011)) | Jiaolong Wang, Jihe Wang, Dexin Zhang, Xiaowei Shao, and Guozhong Chen | Signal Process. |
| 77 | 2018 | 3.3 | Latency-Reliability Tradeoffs for State Estimation ([link](https://doi.org/10.1109/TAC.2020.2992563)) | Konstantinos Gatsis, Hamed Hassani, and George Pappas | IEEE Transactions on Automatic Control |
| 78 | 1966 | 3.3 | The effect of erroneous models on the Kalman filter response ([link](https://doi.org/10.1109/TAC.1966.1098392)) | H. Heffes | IEEE Transactions on Automatic Control |
| 79 | 2000 | 4.4 | Nonlinear estimation and modeling of noisy time series by dual kalman filtering methods ([link](https://www.semanticscholar.org/paper/758b96ba2612a0526cf7536557b9a287e3746a72)) | E. Wan and Alex T. Nelson |  |
| 80 | 2014 | 0.5 | Probabilistic Synapses ([link](https://www.semanticscholar.org/paper/d9412730fab718fe12645f9557a8d06eba2bfe02)) | L. Aitchison, A. Pouget, and P. Latham |  |
| 81 | 2014 | 0.9 | Bayesian synaptic plasticity makes predictions about plasticity experiments in vivo ([link](https://www.semanticscholar.org/paper/46ab1f9b1ffada9a82bbb5ffe39e26e5ac52cbad)) | L. Aitchison and P. Latham | arXiv: Neurons and Cognition |
| 82 | 1967 | 0.1 | On the Efficiency of Learning Machines ([link](https://doi.org/10.1109/TSSC.1967.300091)) | W. Ainsworth | IEEE Trans. Syst. Sci. Cybern. |
| 83 | 2020 | 13 | Convergence and Consistency of Recursive Least Squares with Variable-Rate Forgetting ([link](https://doi.org/10.1016/j.automatica.2020.109052)) | Adam L. Bruce, A. Goel, and D. Bernstein | Autom. |
| 84 | 1976 | 29 | Stationary and nonstationary learning characteristics of the LMS adaptive filter ([link](https://doi.org/10.1007/978-94-010-1223-2_23)) | B. Widrow, J. Mccool, M. Larimore, and C. Johnson | Proceedings of the IEEE |
| 85 | 1984 | 4.2 | On the statistical efficiency of the LMS algorithm with nonstationary inputs ([link](https://doi.org/10.1109/TIT.1984.1056892)) | B. Widrow and E. Walach | IEEE Trans. Inf. Theory |
| 86 | 2023 | 9.3 | Generalized Forgetting Recursive Least Squares: Stability and Robustness Guarantees ([link](https://doi.org/10.1109/TAC.2024.3394351)) | Brian Lai and D. Bernstein | IEEE Transactions on Automatic Control |
| 87 | 2005 | 9.6 | Gradient-based variable forgetting factor RLS algorithm in time-varying environments ([link](https://doi.org/10.1109/TSP.2005.851110)) | S. Leung and C. F. So | IEEE Transactions on Signal Processing |
| 88 | 2020 | 1.2 | Learning as filtering: Implications for spike-based plasticity ([link](https://doi.org/10.1371/journal.pcbi.1009721)) | Jannes Jegminat, S. C. Surace, and Jean-Pascal Pfister | PLoS Computational Biology |
| 89 | 2016 | 0.1 | Surprise-based learning: a novel measure of surprise with applications for learning within changing environments ([link](https://www.semanticscholar.org/paper/5a3d73f79ac71020d39ffe1a7497dbd0f38425aa)) | Mohammad Javad Faraji, K. Preuschoff, and W. Gerstner |  |
| 90 | 2016 | 1.0 | Balancing New Against Old Information: The Role of Surprise ([link](https://www.semanticscholar.org/paper/aa1ed3e4c3a4563a9036fb5ed94a52d277d03e8d)) | M. Faraji, K. Preuschoff, and W. Gerstner | ArXiv |
| 91 | 1998 | 1.1 | Fisher Scoring and a Mixture of Modes Approach for Approximate Inference and Learning in Nonlinear State Space Models ([link](https://www.semanticscholar.org/paper/92887743c432e00058f7842449df7373167fbb39)) | T. Briegel and Volker Tresp | Neural Information Processing Systems |
| 92 | 1977 | 6.6 | The stochastic control of the F-8C aircraft using a multiple model adaptive control (MMAC) method–Part I: Equilibrium flight ([link](https://doi.org/10.1109/TAC.1977.1101599)) | M. Athans et al. | IEEE Transactions on Automatic Control |
| 93 | 2019 | 1.6 | Suboptimal adaptive Kalman filtering based on the proportional control of prior error covariance. ([link](https://doi.org/10.1016/j.isatra.2019.12.008)) | Jiaolong Wang, Chengxi Zhang, Qingxian Jia, and Minzhe Li | ISA transactions |
| 94 | 1971 | 0.2 | Optimal adaptive control of linear systems ([link](https://doi.org/10.1109/CDC.1971.270991)) | D. Lainiotis, T. Upadhyay, and Jayant G. Deshpande | IEEE Conference on Decision and Control |
| 95 | 1971 | 5.9 | Optimal adaptive estimation: Structure and parameter adaption ([link](https://doi.org/10.1109/TAC.1971.1099684)) | D. Lainiotis | IEEE Transactions on Automatic Control |
| 96 | 2013 | 0.1 | Chapter 1 Elements of Information Theory for Networked Control Systems ([link](https://www.semanticscholar.org/paper/30c82cc9a5ace2b811df9f1ebe98ba156d74a15e)) | M. Franceschetti and Paolo Minero |  |
| 97 | 2000 | 0.2 | Dynamic Neural Regression Models ([link](https://doi.org/10.5282/UBM/EPUB.1571)) | T. Briegel and Volker Tresp |  |
| 98 | 2000 | 2.2 | Adaptive Kalman filter for noise identification ([link](https://www.semanticscholar.org/paper/61a10975e7e875c0a9b68272485c96c881a6027f)) | M. Oussalah and J. Schutter |  |
| 99 | 2020 | 2.4 | Recursive Least Squares with Matrix Forgetting ([link](https://doi.org/10.23919/ACC45564.2020.9148005)) | Adam L. Bruce, A. Goel, and D. Bernstein | 2020 American Control Conference (ACC) |
| 100 | 2023 | 5.1 | Rhythmic modulation of prediction errors: A top-down gating role for the beta-range in speech processing ([link](https://doi.org/10.1371/journal.pcbi.1011595)) | Sevada Hovsepyan, I. Olasagasti, and A. Giraud | PLOS Computational Biology |
| 101 | 2007 | 2.3 | Synchronization of nonlinear systems under information constraints. ([link](https://doi.org/10.1063/1.2977459)) | Alexander L. Fradkov, B. Andrievsky, and R. Evans | Chaos |
| 102 | 2024 | 15 | Outlier-robust Kalman Filtering through Generalised Bayes ([link](https://doi.org/10.48550/arXiv.2405.05646)) | Gerardo Duran-Martin et al. | International Conference on Machine Learning |
| 103 | 1991 | 3.0 | Fast tracking RLS algorithm using novel variable forgetting factor with unity zone ([link](https://doi.org/10.1049/EL:19911331)) | D. Park, Byung-Eul Jun, and Jung-Hoon Kim | Electronics Letters |
| 104 | 1988 | 5.9 | Modified least squares algorithm incorporating exponential resetting and forgetting ([link](https://doi.org/10.1080/00207178808906026)) | M. Salgado, G. Goodwin, and R. Middleton | International Journal of Control |
| 105 | 1993 | 13 | A stochastic gradient adaptive filter with gradient adaptive step size ([link](https://doi.org/10.1109/78.218137)) | V. J. Mathews and Zhenhua Xie | IEEE Trans. Signal Process. |
| 106 | 2022 | 7.3 | Recursive Least Squares with Variable-Rate Forgetting Based on the F-Test ([link](https://doi.org/10.23919/ACC53348.2022.9867849)) | Nima Mohseni and D. Bernstein | 2022 American Control Conference (ACC) |
| 107 | 1992 | 3.6 | Recursive forgetting algorithms ([link](https://doi.org/10.1080/00207179208934228)) | J. Parkum, N. K. Poulsen, and J. Holst | International Journal of Control |
| 108 | 2016 | 4.2 | An improved real-time adaptive Kalman filter with recursive noise covariance updating rules ([link](https://doi.org/10.3906/ELK-1309-60)) | Iyad Hashlamon and K. Erbatur | Turkish Journal of Electrical Engineering and Computer Sciences |
| 109 | 2024 | 1.4 | Maximum likelihood estimation of the extended Kalman filter’s parameters with natural gradient ([link](https://doi.org/10.1109/CDC56724.2024.10886147)) | C. Parellier, Camille Chapdelaine, A. Barrau, and Silvère Bonnabel | 2024 IEEE 63rd Conference on Decision and Control (CDC) |
| 110 | 2024 | 1.6 | On the Gaussian Filtering for Nonlinear Dynamic Systems Using Variational Inference ([link](https://doi.org/10.23919/FUSION59988.2024.10765592)) | Yi Liu, Xi Li, Le Yang, Lyudmila Mihaylova, and Ji Li | 2024 27th International Conference on Information Fusion (FUSION) |
| 111 | 1991 | 0.3 | Tuning the forgetting factor in RLS identification algorithms ([link](https://doi.org/10.1109/CDC.1991.261695)) | S. Bittanti and M. Campi | \[1991\] Proceedings of the 30th IEEE Conference on Decision and Control |
| 112 | 1985 | 5.8 | Asymptotically convergent modified recursive least-squares with data-dependent updating and forgetting factor ([link](https://doi.org/10.1109/TIT.1987.1057307)) | S. Dasgupta and Yih-Fang Huang | 1985 24th IEEE Conference on Decision and Control |
| 113 | 1992 | 17 | A variable step size LMS algorithm ([link](https://doi.org/10.1109/78.143435)) | R. Kwong and Edward W. Johnston | IEEE Trans. Signal Process. |
| 114 | 2021 | 3.5 | Continuous-time least-squares forgetting algorithms for indirect adaptive control ([link](https://doi.org/10.1016/J.EJCON.2021.06.015)) | Vitaly Shaferman, M. Schwegel, T. Glück, and A. Kugi | Eur. J. Control |
| 115 | 2018 | 3.3 | Improved Adaptive Kalman Filter with Unknown Process Noise Covariance ([link](https://doi.org/10.23919/ICIF.2018.8455394)) | Jirong Ma et al. | 2018 21st International Conference on Information Fusion (FUSION) |
| 116 | 2019 | 5.6 | An optimality principle for locomotor central pattern generators ([link](https://doi.org/10.1038/s41598-021-91714-1)) | Hansol X. Ryu and A. Kuo | Scientific Reports |
| 117 | 2021 | 0.7 | PredProp: Bidirectional Stochastic Optimization with Precision Weighted Predictive Coding ([link](https://www.semanticscholar.org/paper/c6dfde2283a0606709db6a80036b7cf4c96421bf)) | André Ofner and Sebastian Stober | ArXiv |
| 118 | 2021 | 6.6 | Information Geometry, Fluctuations, Non-Equilibrium Thermodynamics, and Geodesics in Complex Systems ([link](https://doi.org/10.3390/e23111393)) | Eun-jin Kim | Entropy |
| 119 | 2014 | 0.3 | A Filtering Approach to Stochastic Variational Inference ([link](https://www.semanticscholar.org/paper/35409ac9b33f2cc074257018c47fe9c373acb55f)) | N. Houlsby and D. Blei | Neural Information Processing Systems |
| 120 | 2024 | 7.1 | Bayesian Online Natural Gradient (BONG) ([link](https://doi.org/10.48550/arXiv.2405.19681)) | Matt Jones, Peter G. Chang, and Kevin Murphy | ArXiv |
| 121 | 2023 | 9.1 | Low-rank extended Kalman filtering for online learning of neural networks from streaming data ([link](https://doi.org/10.48550/arXiv.2305.19535)) | Peter G. Chang, Gerardo Duran-Mart’in, Alexander Y. Shestopaloff, Matt Jones, and Kevin P. Murphy | ArXiv |
| 122 | 2013 | 6.0 | Adaptive ensemble Kalman filtering of non-linear systems ([link](https://doi.org/10.3402/tellusa.v65i0.20331)) | Tyrus Berry and T. Sauer | Tellus A: Dynamic Meteorology and Oceanography |
| 123 | 1990 | 2.1 | Tracking targets using adaptive Kalman filtering ([link](https://doi.org/10.1109/7.102704)) | P. Gutman and M. Velger | IEEE Transactions on Aerospace and Electronic Systems |
| 124 | 2024 | 6.3 | Nonlinear Bayesian Filtering with Natural Gradient Gaussian Approximation ([link](https://doi.org/10.48550/arXiv.2410.15832)) | Wenhan Cao et al. | IEEE transactions on pattern analysis and machine intelligence |
| 125 | 2021 | 5.8 | Learning in Volatile Environments With the Bayes Factor Surprise ([link](https://doi.org/10.1162/neco_a_01352)) | Vasiliki Liakoni, Alireza Modirshanechi, W. Gerstner, and Johanni Brea | Neural Computation |
| 126 | 2024 | 15 | Computational processes of simultaneous learning of stochasticity and volatility in humans ([link](https://doi.org/10.1038/s41467-024-53459-z)) | Payam Piray and N. D. Daw | Nature Communications |
| 127 | 2010 | 45 | Action and behavior: a free-energy formulation ([link](https://doi.org/10.1007/s00422-010-0364-z)) | Karl J. Friston, J. Daunizeau, J. Kilner, and S. Kiebel | Biological Cybernetics |
| 128 | 2012 | 16 | Active inference and agency: optimal control without cost functions ([link](https://doi.org/10.1007/s00422-012-0512-8)) | Karl J. Friston, Spyridon Samothrakis, and P. Montague | Biological Cybernetics |
| 129 | 2018 | 29 | Generalised free energy and active inference ([link](https://doi.org/10.1007/s00422-019-00805-w)) | Thomas Parr and Karl J. Friston | Biological Cybernetics |
| 130 | 2020 | 40 | Active inference on discrete state-spaces: A synthesis ([link](https://doi.org/10.1016/j.jmp.2020.102447)) | Lancelot Da Costa et al. | Journal of Mathematical Psychology |
| 131 | 2013 | 26 | The anatomy of choice: active inference and agency ([link](https://doi.org/10.3389/fnhum.2013.00598)) | Karl J. Friston et al. | Frontiers in Human Neuroscience |
| 132 | 2008 | 7.2 | A Minimum Relative Entropy Principle for Learning and Acting ([link](https://doi.org/10.1613/JAIR.3062)) | Pedro A. Ortega and Daniel A. Braun | ArXiv |
| 133 | 2012 | 21 | Thermodynamics as a theory of decision-making with information-processing costs ([link](https://doi.org/10.1098/rspa.2012.0683)) | Pedro A. Ortega and Daniel A. Braun | Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences |
| 134 | 2011 | 20 | Information Theory of Decisions and Actions ([link](https://doi.org/10.1007/978-1-4419-1452-1_19)) | Naftali Tishby and D. Polani |  |
| 135 | 2015 | 5.5 | Information-Theoretic Bounded Rationality ([link](https://www.semanticscholar.org/paper/a5a6611134e82077184a2d3b7a336c75402cdaaf)) | Pedro A. Ortega, Daniel A. Braun, Justin Dyer, Kee-Eung Kim, and Naftali Tishby | ArXiv |
| 136 | 2017 | 39 | The free energy principle for action and perception: A mathematical review ([link](https://doi.org/10.1016/J.JMP.2017.09.004)) | C. Buckley, C. S. Kim, Simon McGregor, and A. Seth | Journal of Mathematical Psychology |
| 137 | 2017 | 33 | A tutorial on the free-energy framework for modelling perception and learning ([link](https://doi.org/10.1016/j.jmp.2015.11.003)) | R. Bogacz | Journal of Mathematical Psychology |

### Paper Details

1\. · 100% match · 1970 · 24 cit/yr\
**On the identification of variances and adaptive Kalman filtering** ([link](https://doi.org/10.1109/TAC.1970.1099422))\
R. Mehra\
*IEEE Transactions on Automatic Control* · Apr 1, 1970 · 1346 citations

> A Kalman filter requires an exact knowledge of the process noise covariance matrix Q and the measurement noise covariance matrix R . Here we consider the case in which the true values of Q and R are unknown. The system is assumed to be constant, and the random inputs are stationary. First, a correlation test is given which checks whether a particular Kalman filter is working optimally or not. If the filter is suboptimal, a technique is given to obtain asymptotically normal, unbiased, and consistent estimates of Q and R . This technique works only for the case in which the form of Q is known and the number of unknown elements in Q is less than n \times r where n is the dimension of the state vector and r is the dimension of the measurement vector. For other cases, the optimal steady-state gain K op is obtained directly by an iterative procedure without identifying Q . As a corollary, it is shown that the steady-state optimal Kalman filter gain K op depends only on n \times r linear functionals of Q . The results are first derived for discrete systems. They are then extended to continuous systems. A numerical example is given to show the usefulness of the approach.

------------------------------------------------------------------------

2\. · 100% match · 2017 · 7.9 cit/yr\
**Online natural gradient as a Kalman filter** ([link](https://doi.org/10.1214/18-EJS1468))\
Y. Ollivier\
*Electronic Journal of Statistics* · Mar 1, 2017 · 73 citations

> We establish a full relationship between Kalman filtering and Amari’s natural gradient in statistical learning. Namely, using an online natural gradient descent on data log-likelihood to evaluate the parameter of a probabilistic model from a series of observations, is exactly equivalent to using an extended Kalman filter to estimate the parameter (assumed to have constant dynamics). In the i.i.d. case, this relation is a consequence of the “information filter” phrasing of the extended Kalman filter. In the recurrent (state space, non-i.i.d.) case, we prove that the joint Kalman filter over states and parameters is a natural gradient on top of real-time recurrent learning (RTRL), a classical algorithm to train recurrent models. This exact algebraic correspondence provides relevant settings for natural gradient hyperparameters such as learning rates or initialization and regularization of the Fisher information matrix.

------------------------------------------------------------------------

3\. · 100% match · 2014 · 35 cit/yr\
**Uncertainty in perception and the Hierarchical Gaussian Filter** ([link](https://doi.org/10.3389/fnhum.2014.00825))\
C. Mathys et al.\
*Frontiers in Human Neuroscience* · Nov 19, 2014 · 401 citations

> In its full sense, perception rests on an agent’s model of how its sensory input comes about and the inferences it draws based on this model. These inferences are necessarily uncertain. Here, we illustrate how the Hierarchical Gaussian Filter (HGF) offers a principled and generic way to deal with the several forms that uncertainty in perception takes. The HGF is a recent derivation of one-step update equations from Bayesian principles that rests on a hierarchical generative model of the environment and its (in)stability. It is computationally highly efficient, allows for online estimates of hidden states, and has found numerous applications to experimental data from human subjects. In this paper, we generalize previous descriptions of the HGF and its account of perceptual uncertainty. First, we explicitly formulate the extension of the HGF’s hierarchy to any number of levels; second, we discuss how various forms of uncertainty are accommodated by the minimization of variational free energy as encoded in the update equations; third, we combine the HGF with decision models and demonstrate the inversion of this combination; finally, we report a simulation study that compared four optimization methods for inverting the HGF/decision model combination at different noise levels. These four methods (Nelder–Mead simplex algorithm, Gaussian process-based global optimization, variational Bayes and Markov chain Monte Carlo sampling) all performed well even under considerable noise, with variational Bayes offering the best combination of efficiency and informativeness of inference. Our results demonstrate that the HGF provides a principled, flexible, and efficient—but at the same time intuitive—framework for the resolution of perceptual uncertainty in behaving agents.

------------------------------------------------------------------------

4\. · 100% match · 2010 · 82 cit/yr\
**Attention, Uncertainty, and Free-Energy** ([link](https://doi.org/10.3389/fnhum.2010.00215))\
H. Feldman and Karl J. Friston\
*Frontiers in Human Neuroscience* · Sep 24, 2010 · 1280 citations

> We suggested recently that attention can be understood as inferring the level of uncertainty or precision during hierarchical perception. In this paper, we try to substantiate this claim using neuronal simulations of directed spatial attention and biased competition. These simulations assume that neuronal activity encodes a probabilistic representation of the world that optimizes free-energy in a Bayesian fashion. Because free-energy bounds surprise or the (negative) log-evidence for internal models of the world, this optimization can be regarded as evidence accumulation or (generalized) predictive coding. Crucially, both predictions about the state of the world generating sensory data and the precision of those data have to be optimized. Here, we show that if the precision depends on the states, one can explain many aspects of attention. We illustrate this in the context of the Posner paradigm, using the simulations to generate both psychophysical and electrophysiological responses. These simulated responses are consistent with attentional bias or gating, competition for attentional resources, attentional capture and associated speed-accuracy trade-offs. Furthermore, if we present both attended and non-attended stimuli simultaneously, biased competition for neuronal representation emerges as a principled and straightforward property of Bayes-optimal perception.

------------------------------------------------------------------------

5\. · 100% match · 2019 · 3.5 cit/yr\
**The Extended Kalman Filter is a Natural Gradient Descent in Trajectory Space** ([link](https://www.semanticscholar.org/paper/a5f7b5e3fce21d5b9d57df62d0f3e8093e48672e))\
Y. Ollivier\
*arXiv: Optimization and Control* · Jan 3, 2019 · 26 citations

> The extended Kalman filter is perhaps the most standard tool to estimate in real time the state of a dynamical system from noisy measurements of some function of the system, with extensive practical applications (such as position tracking via GPS). While the plain Kalman filter for linear systems is well-understood, the extended Kalman filter relies on linearizations which have been debated. We recover the exact extended Kalman filter equations from first principles in statistical learning: the extended Kalman filter is equal to Amari’s online natural gradient, applied in the space of trajectories of the system. Namely, each possible trajectory of the dynamical system defines a probability law over possible observations. In principle this makes it possible to treat the underlying trajectory as the parameter of a statistical model of the observations. Then the parameter can be learned by gradient ascent on the log-likelihood of observations, as they become available. Using Amari’s natural gradient from information geometry (a gradient descent preconditioned with the Fisher matrix, which provides parameterization-invariance) exactly recovers the extended Kalman filter. This applies only to a particular choice of process noise in the Kalman filter, namely, taking noise proportional to the posterior covariance - a canonical choice in the absence of specific model information.

------------------------------------------------------------------------

6\. · 100% match · 1998 · 126 cit/yr\
**Natural Gradient Works Efficiently in Learning** ([link](https://doi.org/10.1162/089976698300017746))\
S. Amari\
*Neural Computation* · Feb 15, 1998 · 3555 citations

------------------------------------------------------------------------

7\. · 100% match · 1968 · 12 cit/yr\
**An innovations approach to least-squares estimation–Part II: Linear smoothing in additive white noise** ([link](https://doi.org/10.1109/TAC.1968.1099025))\
T. Kailath and P. Frost\
*IEEE Transactions on Automatic Control* · Dec 1, 1968 · 709 citations

> The innovations approach to linear least-squares approximation problems is first to “whiten” the observed data by a causal and invertible operation, and then to treat the resulting simpler white-noise observations problem. This technique was successfully used by Bode and Shannon to obtain a simple derivation of the classical Wiener filtering problem for stationary processes over a semi-infinite interval. Here we shall extend the technique to handle nonstationary continuous-time processes over finite intervals. In Part I we shall apply this method to obtain a simple derivation of the Kalman-Bucy recursive filtering formulas (for both continuous-time and discrete-time processes) and also some minor generalizations thereof.

------------------------------------------------------------------------

8\. · 100% match · 2010 · 9.9 cit/yr\
**Generalised Filtering** ([link](https://doi.org/10.1155/2010/621670))\
Karl J. Friston, K. Stephan, Baojuan Li, and J. Daunizeau\
161 citations

> We describe a Bayesian filtering scheme for nonlinear state-space models in continuous time. This scheme is called Generalised Filtering and furnishes posterior conditional densities on hidden states and unknown parameters generating observed data. Crucially, the scheme operates online, assimilating data to optimize the conditional density on time-varying states and time-invariant parameters. In contrast to Kalman and Particle smoothing, Generalised Filtering does not require a backwards pass. In contrast to variational schemes, it does not assume conditional independence between the states and parameters. Generalised Filtering optimises the conditional density with respect to a free-energy bound on the model’s log-evidence. This optimisation uses the generalised motion of hidden states and parameters, under the prior assumption that the motion of the parameters is small. We describe the scheme, present comparative evaluations with a fixed-form variational version, and conclude with an illustrative application to a nonlinear state-space model of brain imaging time-series.

------------------------------------------------------------------------

9\. · 100% match · 1991 · 2.8 cit/yr\
**On kalman filtering, posterior mode estimation and fisher scoring in dynamic exponential family regression** ([link](https://doi.org/10.1007/BF02613597))\
L. Fahrmeir and H. Kaufmann\
*Metrika* · Dec 1, 1991 · 96 citations

------------------------------------------------------------------------

10\. · 100% match · 1973 · 3.0 cit/yr\
**Identification of optimum filter steady-state gain for systems with unknown noise covariances** ([link](https://doi.org/10.1109/TAC.1973.1100420))\
B. Carew and P. Belanger\
*IEEE Transactions on Automatic Control* · Dec 1, 1973 · 156 citations

> A discrete linear stationary system is considered for which the input noise covariance Q and the output noise covariance R are unknown. A stable filter with a suboptimal gain is assumed. An identification scheme is presented which uses the autocorrelation functions of the innovations sequence of the suboptimal filter to determine the optimum filter steady state gain \Gamma directly without the intermediate determination of the unknown covariances Q and R . The approach used is to identify an output equivalent representation of the original system which does not involve the unknown covariances directly.

------------------------------------------------------------------------

11\. · 100% match · 1972 · 0.2 cit/yr\
**On stochastic approximation and an adaptive Kalman filter** ([link](https://doi.org/10.1109/CDC.1972.268996))\
L. Scharf and D. Alspach\
*IEEE Conference on Decision and Control* · Dec 1, 1972 · 10 citations

> The orthogonality between the innovations process and the one-step predicted state of a discrete-time Kalman filter is used to specify a stochastic approximation algorithm for simple, adaptive Kalman filtering. The filter is adaptive in the sense that on-line filter signals are used to train the gain matrix to its correct, steady-state form. The problem considered is one of training the gain matrix when the time-invariant plant dynamics are known, but the plant noise and observation noise covariance matrices are unknown. No direct identification of these covariances is required. Simulation results are presented to illustrate the simplicity and soundness of the proposed adaptive filter structure. The simplicity of the proposed adaptation method indicates that it might easily be implemented in real-time data or signal processing applications.

------------------------------------------------------------------------

12\. · 100% match · 1996 · 7.5 cit/yr\
**Neural Learning in Structured Parameter Spaces - Natural Riemannian Gradient** ([link](https://www.semanticscholar.org/paper/fa0c75a9b5f39d166dd875005580687716a236bb))\
S. Amari\
*Neural Information Processing Systems* · Dec 3, 1996 · 220 citations

> The parameter space of neural networks has a Riemannian metric structure. The natural Riemannian gradient should be used instead of the conventional gradient, since the former denotes the true steepest descent direction of a loss function in the Riemannian space. The behavior of the stochastic gradient learning algorithm is much more effective if the natural gradient is used. The present paper studies the information-geometrical structure of perceptrons and other networks, and prove that the on-line learning method based on the natural gradient is asymptotically as efficient as the optimal batch algorithm. Adaptive modification of the learning constant is proposed and analyzed in terms of the Riemannian measure and is shown to be efficient. The natural gradient is finally applied to blind separation of mixtured independent signal sources.

------------------------------------------------------------------------

13\. · 100% match · 1970 · 2.0 cit/yr\
**Optimal adaptive estimation: Structure and parameter adaptation** ([link](https://doi.org/10.1109/SAP.1970.269994))\
D. Lainiotis\
Dec 1, 1970 · 111 citations

> Optimal structure and parameter adaptive estimators have been obtained for continuous as well as discrete data gaussian process models with linear dynamics. Specifically, the essentially nonlinear adaptive estimators are shown to be decomposable (partition theorem) into two parts, a linear non-adaptive part consisting of a bank of Kalman-Bucy filters, and a nonlinear part that incorporates the learning or adaptive nature of the estimator. The conditional-error-covariance matrix of the estimator is also obtained in a form suitable for on-line performance evaluation. The adaptive estimators are applied to the problem of state-estimation with nongaussian initial state and also to estimation under measurement uncertainty (joint detection-estimation). Examples are given of the application of the proposed adaptive estimators to structure and parameter adaptation indicating their applicability to practical engineering problems.

------------------------------------------------------------------------

14\. · 100% match · 1992 · 5.2 cit/yr\
**Posterior Mode Estimation by Extended Kalman Filtering for Multivariate Dynamic Generalized Linear Models** ([link](https://doi.org/10.1080/01621459.1992.10475232))\
L. Fahrmeir\
*Journal of the American Statistical Association* · Jun 1, 1992 · 176 citations

> Abstract A family of multivariate dynamic generalized linear models is introduced as a general framework for the analysis of time series with observations from the exponential family. Besides common conditionally Gaussian models, this article deals with univariate models for counted and binary data and, as the most interesting multivariate case, models for nonstationary multicategorical time series. For univariate responses, a related yet different class of models has been introduced in a Bayesian setting by West, Harrison and Migon. Assuming conjugate prior-posterior distributions for the natural parameter of the exponential family, they derive an approximate filter for estimation of time-varying states or parameters. However, their method raises some problems; in particular, in extending it to the multivariate case. A different approach to filtering and smoothing is chosen in this article. To avoid a full Bayesian analysis based on numerical integration, which becomes computationally critical for higher…

------------------------------------------------------------------------

15\. · 100% match · 2021 · 9.0 cit/yr\
**Synaptic plasticity as Bayesian inference** ([link](https://doi.org/10.1038/s41593-021-00809-5))\
L. Aitchison et al.\
*Nature neuroscience* · Jan 27, 2021 · 48 citations

> Learning, especially rapid learning, is critical for survival. However, learning is hard; a large number of synaptic weights must be set based on noisy, often ambiguous, sensory information. In such a high-noise regime, keeping track of probability distributions over weights is the optimal strategy. Here we hypothesize that synapses take that strategy; in essence, when they estimate weights, they include error bars. They then use that uncertainty to adjust their learning rates, with more uncertain weights having higher learning rates. We also make a second, independent, hypothesis: synapses communicate their uncertainty by linking it to variability in postsynaptic potential size, with more uncertainty leading to more variability. These two hypotheses cast synaptic plasticity as a problem of Bayesian inference, and thus provide a normative view of learning. They generalize known learning rules, offer an explanation for the large variability in the size of postsynaptic potentials and make falsifiable experimental predictions. We propose that synapses compute probability distributions over weights, not just point estimates. Using probabilistic inference, we derive a new set of synaptic learning rules and show that they speed up learning in neural networks.

------------------------------------------------------------------------

16\. · 100% match · 2020 · 10 cit/yr\
**A simple model for learning in volatile environments** ([link](https://doi.org/10.1371/journal.pcbi.1007963))\
Payam Piray and N. Daw\
*PLoS Computational Biology* · Jul 1, 2020 · 61 citations

> Sound principles of statistical inference dictate that uncertainty shapes learning. In this work, we revisit the question of learning in volatile environments, in which both the first and second-order statistics of observations dynamically evolve over time. We propose a new model, the volatile Kalman filter (VKF), which is based on a tractable state-space model of uncertainty and extends the Kalman filter algorithm to volatile environments. The proposed model is algorithmically simple and encompasses the Kalman filter as a special case. Specifically, in addition to the error-correcting rule of Kalman filter for learning observations, the VKF learns volatility according to a second error-correcting rule. These dual updates echo and contextualize classical psychological models of learning, in particular hybrid accounts of Pearce-Hall and Rescorla-Wagner. At the computational level, compared with existing models, the VKF gives up some flexibility in the generative model to enable a more faithful approximation to exact inference. When fit to empirical data, the VKF is better behaved than alternatives and better captures human choice data in two independent datasets of probabilistic learning tasks. The proposed model provides a coherent account of learning in stable or volatile environments and has implications for decision neuroscience research.

------------------------------------------------------------------------

17\. · 100% match · 2004 · 34 cit/yr\
**Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates** ([link](https://doi.org/10.1137/S0363012902402116))\
G. Nair and R. Evans\
*SIAM J. Control. Optim.* · Feb 1, 2004 · 753 citations

> Feedback control with limited data rates is an emerging area which incorporates ideas from both control and information theory. A fundamental question it poses is how low the closed-loop data rate can be made before a given dynamical system is impossible to stabilize by any coding and control law. Analogously to source coding, this defines the smallest error-free data rate sufficient to achieve “reliable” control, and explicit expressions for it have been derived for linear time-invariant systems without disturbances. In this paper, the more general case of finite-dimensional linear systems with process and observation noise is considered, the object being mean square state stability. By inductive arguments employing the entropy power inequality of information theory, and a new quantizer error bound, an explicit expression for the infimum stabilizing data rate is derived, under very mild conditions on the initial state and noise probability distributions.

------------------------------------------------------------------------

18\. · 100% match · 2018 · 71 cit/yr\
**A Novel Adaptive Kalman Filter With Inaccurate Process and Measurement Noise Covariance Matrices** ([link](https://doi.org/10.1109/TAC.2017.2730480))\
Yulong Huang, Yonggang Zhang, Zhemin Wu, Ning Li, and J. Chambers\
*IEEE Transactions on Automatic Control* · Feb 1, 2018 · 592 citations

------------------------------------------------------------------------

19\. · 100% match · 1973 · 0.2 cit/yr\
**Adaptive Kalman filtering using stochastic approximation** ([link](https://doi.org/10.1049/EL:19730131))\
N. Sinha\
*Electronics Letters* · May 3, 1973 · 10 citations

> A Kalman filter requires an exact knowledge of the noise covariance matrices to determine the optimal gain Kop for the filtering equations. In the absence of such prior information, an adaptive technique must be used. An approach based on stochastic approximation is presented. The steady-state gain is obtained by using a recursive algorithm that satisfies the innovations theorem.

------------------------------------------------------------------------

20\. · 100% match · 1981 · 18 cit/yr\
**Implementation of self-tuning regulators with variable forgetting factors** ([link](https://doi.org/10.1016/0005-1098(81%2990070-4))\
T. Fortescue, L. Kershenbaum, and B. Ydstie\
*Autom.* · 826 citations

------------------------------------------------------------------------

21\. · 100% match · 2018 · 3.9 cit/yr\
**Entropy and Minimal Bit Rates for State Estimation and Model Detection** ([link](https://doi.org/10.1109/TAC.2017.2782478))\
D. Liberzon and S. Mitra\
*IEEE Transactions on Automatic Control* · Oct 1, 2018 · 30 citations

> We study a notion of estimation entropy for continuous-time nonlinear systems, formulated in terms of the number of system trajectories that approximate all other trajectories up to an exponentially decaying error. We also consider an alternative definition of estimation entropy, which uses approximating functions that are not necessarily trajectories of the system, and show that the two entropy notions are equivalent. We establish an upper bound on the estimation entropy in terms of the sum of the desired convergence rate and an upper bound on the matrix measure of the Jacobian, multiplied by the system dimension. A lower bound on the estimation entropy is developed as well. We then turn our attention to state estimation and model detection with quantized and sampled state measurements. We describe an iterative procedure that uses such measurements to generate state estimates that converge to the true state at the desired exponential rate. The average bit rate utilized by this procedure matches the derived upper bound on the estimation entropy, and no other algorithm of this type can perform the same estimation task with bit rates lower than the estimation entropy. Finally, we discuss an application of the estimation procedure in determining, from the quantized state measurements, which of two competing models of a dynamical system is the true model. We show that under a mild assumption of “exponential separation” of the candidate models, detection always happens in finite time.

------------------------------------------------------------------------

22\. · 100% match · 2019 · 1.3 cit/yr\
**Rate-Cost Tradeoffs in Control** ([link](https://doi.org/10.1109/TAC.2019.2912256))\
V. Kostina and B. Hassibi\
*IEEE Transactions on Automatic Control* · Apr 19, 2019 · 9 citations

> Consider a control problem with a communication channel connecting the observer of a linear stochastic system to the controller. The goal of the controller is to minimize a quadratic cost function in the state variables and control signal, known as the linear quadratic regulator (LQR). We study the fundamental tradeoff between the communication rate $`r`$ b/s and the expected cost $`b`$. We obtain a lower bound on a certain rate-cost function, which quantifies the minimum directed mutual information between the channel input and output that is compatible with a target LQR cost. The rate-cost function has operational significance in multiple scenarios of interest: among others, it allows us to lower-bound the minimum communication rate for fixed and variable length quantization, and for control over noisy channels. We derive an explicit lower bound to the rate-cost function, which applies to the vector, non-Gaussian, and partially observed systems, thereby extending and generalizing an earlier explicit expression for the scalar Gaussian system, due to Tatikonda et al. \[S. Tatikonda, A. Sahai, and S. Mitter, “Stochastic linear control over a communication channel,” IEEE Trans. Autom. Control, vol. 49, no. 9, pp. 1549–1561, Sep. 2004.\]. The bound applies as long as the differential entropy of the system noise is not $`-\infty`$. It can be closely approached by a simple lattice quantization scheme that only quantizes the innovation, that is, the difference between the controller’s belief about the current state and the true state. Via a separation principle between control and communication, similar results hold for causal lossy compression of additive noise Markov sources. Apart from standard dynamic programming arguments, our technical approach leverages the Shannon lower bound, develops new estimates for data compression with coding memory, and uses some recent results on high resolution variable-length vector quantization to prove that the new converse bounds are tight.

------------------------------------------------------------------------

23\. · 100% match · 1973 · 0.1 cit/yr\
**The adaptation of observation noise covariances and adaptive Kalman filtering** ([link](https://doi.org/10.1109/CDC.1973.269192))\
J. Lin\
*IEEE Conference on Decision and Control* · Dec 1, 1973 · 4 citations

> The application of Kalman-Bucy filters entails precise knowledge on the a priori noise covariances as well as the system parameters. In many practical cases, however, such precise knowledge is not available, and approximate values are usually used or assumed. It has been pointed out that incorrect covariances often cause severe inconsistency between the calculated error covariance and the actual one. Approaches of adaptive filtering have been studied by various researchers for mainly time-invariant systems. An iterative procedure for the adaptation of the assumed a priori observation-noise covariances of time-variable systems is investigated in this paper. The procedure proposed here computes at each iteration a necessary correction from the covariances of the innovation process, and adapt the noise covariances thereby. The calculated error covariance is shown to tend to the actual in the limit. Simulated examples show that initial choices of the a priori covariance do not seem to be crucial to the convergence. An approach to adaptive filtering is also proposed.

------------------------------------------------------------------------

24\. · 100% match · 2020 · 20 cit/yr\
**A model for learning based on the joint estimation of stochasticity and volatility** ([link](https://doi.org/10.1038/s41467-021-26731-9))\
Payam Piray and N. Daw\
*Nature Communications* · Oct 7, 2020 · 112 citations

> Previous research has stressed the importance of uncertainty for controlling the speed of learning, and how such control depends on the learner inferring the noise properties of the environment, especially volatility: the speed of change. However, learning rates are jointly determined by the comparison between volatility and a second factor, moment-to-moment stochasticity. Yet much previous research has focused on simplified cases corresponding to estimation of either factor alone. Here, we introduce a learning model, in which both factors are learned simultaneously from experience, and use the model to simulate human and animal data across many seemingly disparate neuroscientific and behavioral phenomena. By considering the full problem of joint estimation, we highlight a set of previously unappreciated issues, arising from the mutual interdependence of inference about volatility and stochasticity. This interdependence complicates and enriches the interpretation of previous results, such as pathological learning in individuals with anxiety and following amygdala damage. Human learning depends on opposing effects of two noise factors: volatility and stochasticity. Here the authors present a model of learning that shows how and why joint estimation of these factors is important for understanding healthy and pathological learning.

------------------------------------------------------------------------

25\. · 100% match · 2014 · 4.6 cit/yr\
**A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level** ([link](https://doi.org/10.1109/TAC.2015.2500658))\
Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina\
*IEEE Transactions on Automatic Control* · Jul 1, 2014 · 55 citations

> This paper studies networked control systems closed over noiseless digital channels. We focus on noisy linear time-invariant (LTI) plants with stationary Gaussian disturbances, Gaussian initial state, scalar-valued control inputs and sensor outputs. For this set-up, we show that the absolute minimal directed information rate that allows one to achieve a prescribed level of performance (not necessarily stationary), over all combinations of encoder-controller-decoder, is achieved when the decoder output is jointly Gaussian with the other signals in the system. This directed information rate lower bounds the achievable operational data rates. When restricting our attention to encoder-controller-decoders which make the random processes in the loop (strongly) asymptotically wide-sense stationary, this bound can be expressed in terms of their asymptotic power spectral densities. Then we show that the directed information rate and stationary performance of any such scheme can be achieved when the concatenated encoder, channel, controller and decoder behave as an AWGN channel with LTI filters. We also present a simple coding scheme that allows one to achieve (operational) average data rates that are at most (approximately) 1.254 bits away from the derived lower bound, while satisfying the performance constraint. A numerical example is presented to illustrate our findings.

------------------------------------------------------------------------

26\. · 100% match · 1997 · 20 cit/yr\
**Systems with finite communication bandwidth constraints. I. State estimation problems** ([link](https://doi.org/10.1109/9.623096))\
W. Wong and R. Brockett\
*IEEE Trans. Autom. Control.* · Sep 1, 1997 · 578 citations

> In this paper, we investigate a state estimation problem involving finite communication capacity constraints. Unlike classical estimation problems where the observation is a continuous process corrupted by additive noises, there is a constraint that the observations must be coded and transmitted over a digital communication channel with finite capacity. This problem is formulated mathematically, and some convergence properties are defined. Moreover, the concept of a finitely recursive coder-estimator sequence is introduced. A new upper bound for the average estimation error is derived for a large class of random variables. Convergence properties of some coder-estimator algorithms are analyzed. Various conditions connecting the communication data rate with the rate of change of the underlying dynamics are established for the existence of stable and asymptotically convergent coder-estimator schemes.

------------------------------------------------------------------------

27\. · 100% match · 1973\
**Linear stochastic optimal control under information rate constraints** ([link](https://doi.org/10.1080/00207177308932375))\
R. Lefever and E. Stear\
*International Journal of Control* · Feb 1, 1973 · 0 citations

> The discrete-time, linear, stochastic optimal control problem is considered under information rate constraints on the feedback loop. The feedback loop, including sensor, is modelled as a communication channel which provides a specified amount of information (in the Shannon sense) about the state of the linear plant at each discrete-time instant given the current and past observations and past controls. No further specific structure for the sensor is assumed. The expected value of a positive definite quadratic loss function is used as the performance criterion to be minimized. This leads to a double minimization problem in which the performance criterion is minimized over the set of admissible controls and the set of conditional probability densities for the state given the observations and controls which achieve the specified information. A set of recursion relationships for the solution of this problem is derived using the techniques of calculus of variations and dynamic programming. The solution indicat…

------------------------------------------------------------------------

28\. · 99% match · 1986 · 189 cit/yr\
**Adaptive Filter Theory** ([link](https://www.semanticscholar.org/paper/59a26a2d95db9b713c512d96b2a9e1eafb72d312))\
S. Haykin\
7631 citations

> Background and Overview. 1. Stochastic Processes and Models. 2. Wiener Filters. 3. Linear Prediction. 4. Method of Steepest Descent. 5. Least-Mean-Square Adaptive Filters. 6. Normalized Least-Mean-Square Adaptive Filters. 7. Transform-Domain and Sub-Band Adaptive Filters. 8. Method of Least Squares. 9. Recursive Least-Square Adaptive Filters. 10. Kalman Filters as the Unifying Bases for RLS Filters. 11. Square-Root Adaptive Filters. 12. Order-Recursive Adaptive Filters. 13. Finite-Precision Effects. 14. Tracking of Time-Varying Systems. 15. Adaptive Filters Using Infinite-Duration Impulse Response Structures. 16. Blind Deconvolution. 17. Back-Propagation Learning. Epilogue. Appendix A. Complex Variables. Appendix B. Differentiation with Respect to a Vector. Appendix C. Method of Lagrange Multipliers. Appendix D. Estimation Theory. Appendix E. Eigenanalysis. Appendix F. Rotations and Reflections. Appendix G. Complex Wishart Distribution. Glossary. Abbreviations. Principal Symbols. Bibliography. Index.

------------------------------------------------------------------------

29\. · 98% match · 2015 · 1.1 cit/yr\
**LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis** ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*ArXiv* · Oct 14, 2015 · 12 citations

> In the interest of evaluating an information-theoretic requirement for feedback control, this paper proposes a framework to synthesize a control policy that minimizes Massey’s directed information from the state sequence to the control sequence while attaining required Linear-Quadratic-Gaussian (LQG) control performance. Interpretation and significance of this framework is discussed in the context of networked control theory. As the main result, we show that an optimal control policy can be realized by an attractively simple three-stage decision architecture comprising (1) a linear sensor with additive Gaussian noise, (2) a Kalman filter, and (3) a certainty equivalence controller. This result suggests an integration of two separation principles previously known in the literature: the filter-controller separation principle in the LQG control theory, and the sensorfilter separation principle in zero-delay rate-distortion theory for Gauss-Markov sources. It is also shown that an optimal policy can be synthesized by semidefinite programming (SDP). Both time-varying finite-horizon problems and time-invariant infinitehorizon problems are considered. Our results can be viewed as a generalization of the data-rate theorem for mean-square stability by Nair & Evans, extended for a control performance analysis.

------------------------------------------------------------------------

30\. · 97% match · 2022 · 0.2 cit/yr\
**Optimal Causal Rate-Constrained Sampling of the Wiener Process** ([link](https://doi.org/10.1109/TAC.2021.3071953))\
Nian Guo and V. Kostina\
*IEEE Transactions on Automatic Control* · Apr 1, 2022 · 1 citations

> We consider the following communication scenario. An encoder causally observes the Wiener process and decides when and what to transmit about it. A decoder estimates the process using causally received codewords in real time. We determine the causal encoding and decoding policies that jointly minimize the mean-square estimation error, under the long-term communication rate constraint of \<inline-formula\>\<tex-math notation=“LaTeX”\>$`R`$\</tex-math\>\</inline-formula\> bits per second. We show that an optimal encoding policy can be implemented as a causal sampling policy followed by a causal compressing policy. We prove that the optimal encoding policy samples the Wiener process once the innovation passes either \<inline-formula\>\<tex-math notation=“LaTeX”\>$`\sqrt{\frac{1}{R}}`$\</tex-math\>\</inline-formula\> or \<inline-formula\>\<tex-math notation=“LaTeX”\>$`-\sqrt{\frac{1}{R}}`$\</tex-math\>\</inline-formula\> and compresses the sign of innovation (SOI) using a 1-bit codeword. The \<italic\>SOI coding scheme\</italic\> achieves the operational distortion-rate function, which is equal to \<inline-formula\>\<tex-math notation=“LaTeX”\>$`D^{\mathrm{op}}(R)=\frac{1}{6R}`$\</tex-math\>\</inline-formula\>. Surprisingly, this is significantly better than the distortion-rate tradeoff achieved in the limit of infinite delay by the best noncausal code. This is because the SOI coding scheme leverages the free timing information supplied by the zero-delay channel between the encoder and the decoder. The key to unlocking that gain is the event-triggered nature of the SOI sampling policy. In contrast, the distortion-rate tradeoffs achieved with deterministic sampling policies are much worse: we prove that the causal informational distortion-rate function in that scenario is as high as \<inline-formula\>\<tex-math notation=“LaTeX”\>$`D_{\mathrm{DET}}(R) = \frac{5}{6R}`$\</tex-math\>\</inline-formula\>. It is achieved by the uniform sampling policy with the sampling interval \<inline-formula\>\<tex-math notation=“LaTeX”\>$`\frac{1}{R}`$\</tex-math\>\</inline-formula\>. In either case, the optimal strategy is to sample the process as fast as possible and to transmit 1-bit codewords to the decoder without delay. We show that \<italic\>the SOI coding scheme\</italic\> also minimizes the mean-square cost of a continuous-time control system driven by the Wiener process and controlled via rate-constrained impulses.

------------------------------------------------------------------------

31\. · 96% match · 2018 · 8.2 cit/yr\
**Value of Information in Feedback Control: Quantification** ([link](https://doi.org/10.1109/TAC.2021.3113472))\
T. Soleymani, J. Baras, and S. Hirche\
*IEEE Transactions on Automatic Control* · Dec 18, 2018 · 61 citations

> Although transmission of a data packet containing sensory information in a networked control system improves the quality of regulation, it has indeed a price from the communication perspective. It is, therefore, rational that such a data packet be transmitted only if it is valuable in the sense of a cost-benefit analysis. Yet, the fact is that little is known so far about this valuation of information and its connection with traditional event-triggered communication. In the present article, we study this intrinsic property of networked control systems by formulating a rate-regulation trade-off between the packet rate and the regulation cost with an event trigger and a controller as two distributed decision makers, and show that the valuation of information is conceivable and quantifiable grounded on this trade-off. In particular, we characterize an equilibrium in the rate-regulation trade-off, and quantify the value of information \<inline-formula\>\<tex-math notation=“LaTeX”\>$`{\rm{VoI}}_k`$\</tex-math\>\</inline-formula\> there as the variation in a so-called value function with respect to a piece of sensory information that can be communicated to the controller at each time \<inline-formula\>\<tex-math notation=“LaTeX”\>$`k`$\</tex-math\>\</inline-formula\>. We prove that, for a multi-dimensional Gauss–Markov process, \<inline-formula\>\<tex-math notation=“LaTeX”\>$`{\rm{VoI}}_k`$\</tex-math\>\</inline-formula\> is a symmetric function of the discrepancy between the state estimates at the event trigger and the controller, and that a data packet containing sensory information at time \<inline-formula\>\<tex-math notation=“LaTeX”\>$`k`$\</tex-math\>\</inline-formula\> should be transmitted to the controller only if \<inline-formula\>\<tex-math notation=“LaTeX”\>$`{\rm{VoI}}_k`$\</tex-math\>\</inline-formula\> is nonnegative. Moreover, we discuss that \<inline-formula\>\<tex-math notation=“LaTeX”\>$`{\rm{VoI}}_k`$\</tex-math\>\</inline-formula\> can be computed with arbitrary accuracy, and that it can be approximated by a closed-form quadratic function with a performance guarantee.

------------------------------------------------------------------------

32\. · 95% match · 1986\
**Optimum rate allocation in quantized control** ([link](https://doi.org/10.1002/OCA.4660070405))\
C. Meadow, T. Fischer, and J. Gibson\
*Optimal Control Applications & Methods* · Oct 1, 1986 · 0 citations

> A linear-quadratic-Gaussian (LQG) delocalized control problem is formulated to require both specification of a control law and communication of measurements to controller and controls to plant. Efficient communication requires quantization of both measurement and control signals. The basic design problem is to allocate in an optimum fashion a fixed total communication rate to the measurement and control communication systems.
>
> A dynamic communication-rate allocation algorithm is developed on the basis of prediction error and entropy power. As intuitively expected, the rate allocation depends on both the measurement and plant noise powers as well as the overall quadratic performance measure. Solely on the basis of entropy power considerations, a larger rate should be allocated for communication of measurements than for communication of controls.

------------------------------------------------------------------------

33\. · 95% match · 2014 · 10 cit/yr\
**Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs** ([link](https://doi.org/10.1109/TAC.2016.2601148))\
Takashi Tanaka, Kwang-Ki K. Kim, P. Parrilo, and S. Mitter\
*IEEE Transactions on Automatic Control* · Nov 27, 2014 · 120 citations

> Sequential rate-distortion (SRD) theory provides a framework for studying the fundamental trade-off between data-rate and data-quality in real-time communication systems. In this paper, we consider the SRD problem for multi-dimensional time-varying Gauss-Markov processes under mean-square distortion criteria. We first revisit the sensor-estimator separation principle, which asserts that considered SRD problem is equivalent to a joint sensor and estimator design problem in which data-rate of the sensor output is minimized while the estimator’s performance satisfies the distortion criteria. We then show that the optimal joint design can be performed by semidefinite programming. A semidefinite representation of the corresponding SRD function is obtained. Implications of the obtained result in the context of zero-delay source coding theory and applications to networked control theory are also discussed.

------------------------------------------------------------------------

34\. · 94% match · 2017\
**Control Capacity** ([link](https://doi.org/10.1109/TIT.2018.2868929))\
G. Ranade and Anant Sahai\
*IEEE Transactions on Information Theory* · Jan 16, 2017 · 0 citations

> Feedback control actively dissipates uncertainty from a dynamical system by means of actuation. We develop a notion of “control capacity” that gives a fundamental limit (in bits) on the rate at which a controller can dissipate the uncertainty from a system, i.e., stabilize to a known fixed point. We give a computable single-letter characterization of control capacity for memoryless stationary scalar multiplicative actuation channels. Control capacity allows us to answer questions of stabilizability for scalar linear systems: a system with actuation uncertainty is stabilizable if and only if the control capacity is larger than the log of the unstable open-loop eigenvalue. For second-moment senses of stability, we recover the classic uncertainty threshold principle result. However, our definition of control capacity can quantify the stabilizability limits for any moment of stability. Our formulation parallels the notion of Shannon’s communication capacity and thus yields both a strong converse and a way to compute the value of side information in control.

------------------------------------------------------------------------

35\. · 94% match · 1966 · 0.2 cit/yr\
**Transmission of an analog signal over a fixed bit-rate channel** ([link](https://doi.org/10.1109/TIT.1966.1053927))\
K. Steiglitz\
*IEEE Trans. Inf. Theory* · Oct 1, 1966 · 11 citations

> The transmission of a nonbandlimited analog signal over a digital channel with a fixed bit-rate is considered. The trade-off between the mean-square error due to quantizing and the mean-square error due to the process of sampling and reconstructing the signal is investigated. Simple approximations to these errors, which are valid in most practical situations, are derived, and simple expressions are obtained from which the optimum sampling interval and number of bits per sample can be calculated. Results for first-, second-, and third-order Butterworth and fiat bandlimited spectra, together with the zero-order hold and the linear point connector, are included. The resulting mean-square error goes to zero with large channel bit-rates in a slower manner than the Shannon limit, which assumes a strictly bandlimited signal and perfect reconstruction.

------------------------------------------------------------------------

36\. · 92% match · 2020 · 15 cit/yr\
**On the Identification of Noise Covariances and Adaptive Kalman Filtering: A New Look at a 50 Year-Old Problem** ([link](https://doi.org/10.1109/ACCESS.2020.2982407))\
Lingyi Zhang et al.\
*IEEE access : practical innovations, open solutions* · Jan 20, 2020 · 98 citations

> The Kalman filter requires knowledge of the noise statistics; however, the noise covariances are generally unknown. Although this problem has a long history, reliable algorithms for their estimation are scant, and necessary and sufficient conditions for identifiability of the covariances are in dispute. We address both of these issues in this paper. We first present the necessary and sufficient condition for unknown noise covariance estimation; these conditions are related to the rank of a matrix involving the auto and cross-covariances of a weighted sum of innovations, where the weights are the coefficients of the minimal polynomial of the closed-loop system transition matrix of a stable, but not necessarily optimal, Kalman filter. We present an optimization criterion and a novel six-step approach based on a successive approximation, coupled with a gradient algorithm with adaptive step sizes, to estimate the steady-state Kalman filter gain, the unknown noise covariance matrices, as well as the state prediction (and updated) error covariance matrix. Our approach enforces the structural assumptions on unknown noise covariances and ensures symmetry and positive definiteness of the estimated covariance matrices. We provide several approaches to estimate the unknown measurement noise covariance $`R`$ via post-fit residuals, an approach not yet exploited in the literature. The validation of the proposed method on five different test cases from the literature demonstrates that the proposed method significantly outperforms previous state-of-the-art methods. It also offers a number of novel machine learning motivated approaches, such as sequential (one sample at a time) and mini-batch-based methods, to speed up the computations.

------------------------------------------------------------------------

37\. · 91% match · 1996 · 0.3 cit/yr\
**Information theoretic tools for stable adaptation and learning** (\[link\](https://doi.org/10.1002/(SICI%291099-1115(199607%2910:4/5\<499::AID-ACS397\>3.0.CO;2-M))\
S. Lloyd and J. Slotine\
*International Journal of Adaptive Control and Signal Processing* · Jul 1, 1996 · 10 citations

> Lyapunov design has never been systematic. In the adaptive control of complex multi-input non-linear systems, physical considerations, such as conservation of energy or entropy increase, represent one of the major tools in building Lyapunov-like functions and providing stability and performance guarantees. In this paper we show that a physically motivated Lyapunov-like function based on the concept of total information can be derived for large classes of non-linear physical systems. We study how this function may be used for designing estimation, adaptation and learning mechanisms for such systems. In the process we revisit familiar notions such as controllability and observability from an information perspective, which in turns allows us to define ‘natural’ space-time scales at which to observe and control a given complex system. By formulating control problems in algorithmic form, we emphasize the importance of computability and computational complexity for issues of control. Generic control problems are shown to be NP-hard: each additional complication, such as the presence of noise or the absence of complete system identification, moves the control problem further up the polynomial hierarchy of computational complexity. In some cases, requirements of ‘optimality’ may be unrealistic or irrelevant, since the solution to the problem of finding the optimal algorithm for control is uncomputable.

------------------------------------------------------------------------

38\. · 90% match · 1988 · 3.2 cit/yr\
**Entropy formulation of optimal and adaptive control** ([link](https://doi.org/10.1109/9.1287))\
G. Saridis\
*IEEE Transactions on Automatic Control* · Aug 1, 1988 · 121 citations

> The use of entropy as the common measure to evaluate the different levels of intelligent machines is reported. At the execution level, the design of the desirable control can be expressed by the uncertainty of selecting the optimal control that minimizes a given performance index. By choosing a density function over the set of admissible controls to minimize the differential control entropy, it can be shown that the optimal control problem is equivalent to the problem of minimization of the assigned entropy function with respect to the association control. The adaptive control problem can be analyzed by considering the same entropy over extended space that includes the uncertain parameters. It is shown that the optimal entropy is decomposed into three terms: the optimal control term with given parameters, the parameter identification term, and the equivocation term which accounts for the active transition of dual control. The equivocation when calculated can serve as a measure of optimality of the adaptive control algorithms that involve only distinct identification and optimal control algorithms. An upper bound can be used instead, when the equivocation is hard to calculate. An example illustrates the method. \>

------------------------------------------------------------------------

39\. · 90% match · 387 cit/yr\
**Natural Gradient Works Eciently in Learning** ([link](https://www.semanticscholar.org/paper/e1c2a2fd6a26947e5bbb8df47e30c1199ab1270d))\
S. Amari\
387 citations

> When a parameter space has a certain underlying structure, the ordinary gradient of a function does not represent its steepest direction but the natural gradient does. Information geometry is used for calculating the natural gradients in the parameter space of perceptrons, the space of matrices (for blind source separation) and the space of linear dynamical systems (for blind source deconvolution). The dynamical behavior of natural gradient on-line learning is analyzed and is proved to be Fisher ecient, implying that it has asymptotically the same performance as the optimal batch estimation of parameters. This suggests that the plateau phenomenon which appears in the backpropagation learning algorithm of multilayer perceptrons might disappear or might be not so serious when the natural gradient is used. An adaptive method of updating the learning rate is proposed and analyzed.

------------------------------------------------------------------------

40\. · 89% match · 2020 · 0.3 cit/yr\
**Optimal Causal Rate-Constrained Sampling for a Class of Continuous Markov Processes** ([link](https://doi.org/10.1109/tit.2021.3114142))\
Nian Guo and V. Kostina\
*IEEE Transactions on Information Theory* · Feb 4, 2020 · 2 citations

> Consider the following communication scenario. An encoder observes a stochastic process and causally decides when and what to transmit about it, under a constraint on the expected number of bits transmitted per second. A decoder uses the received codewords to causally estimate the process in real time. The encoder and the decoder are synchronized in time. For a class of continuous Markov processes satisfying regularity conditions, we find the optimal encoding and decoding policies that minimize the end-to-end estimation mean-square error under the rate constraint. We show that the optimal encoding policy transmits a 1-bit codeword once the process innovation passes one of two thresholds. The optimal decoder noiselessly recovers the last sample from the 1-bit codewords and codeword-generating time stamps, and uses it to decide the running estimate of the current process, until the next codeword arrives. In particular, we show the optimal causal code for the Ornstein-Uhlenbeck process and calculate its distortion-rate function. Furthermore, we show that the optimal causal code also minimizes the mean-square cost of a continuous-time control system driven by a continuous Markov process and controlled by an additive control signal.

------------------------------------------------------------------------

41\. · 89% match · 2008 · 24 cit/yr\
**The statistical determinants of adaptation rate in human reaching.** ([link](https://doi.org/10.1167/8.4.20))\
Johannes Burge, M. Ernst, and M. Banks\
*Journal of vision* · Apr 23, 2008 · 431 citations

> Rapid reaching to a target is generally accurate but also contains random and systematic error. Random errors result from noise in visual measurement, motor planning, and reach execution. Systematic error results from systematic changes in the mapping between the visual estimate of target location and the motor command necessary to reach the target (e.g., new spectacles, muscular fatigue). Humans maintain accurate reaching by recalibrating the visuomotor system, but no widely accepted computational model of the process exists. Given certain boundary conditions, a statistically optimal solution is a Kalman filter. We compared human to Kalman filter behavior to determine how humans take into account the statistical properties of errors and the reliability with which those errors can be measured. For most conditions, human and Kalman filter behavior was similar: Increasing measurement uncertainty caused similar decreases in recalibration rate; directionally asymmetric uncertainty caused different rates in different directions; more variation in systematic error increased recalibration rate. However, behavior differed in one respect: Inserting random error by perturbing feedback position causes slower adaptation in Kalman filters but had no effect in humans. This difference may be due to how biological systems remain responsive to changes in environmental statistics. We discuss the implications of this work.

------------------------------------------------------------------------

42\. · 88% match · 1977 · 0.4 cit/yr\
**Adaptive state estimation for systems with unknown noise covariances** ([link](https://doi.org/10.1080/00207727708942048))\
N. Sinha and A. Tom\
*International Journal of Systems Science* · Apr 1, 1977 · 21 citations

> An adaptive scheme is proposed for obtaining the steady-state Kalman gain matrix for o discrete-time system without a priori knowledge of the noise covariance matrices. It is based on combining an algorithm proposed recently by Carew and Belanger with an algorithm based on stochastic approximation. Results of simulation are given comparing the proposed method with earlier algorithms.

------------------------------------------------------------------------

43\. · 88% match · 2017 · 0.9 cit/yr\
**Information Geometric Approach to Recursive Update in Nonlinear Filtering** ([link](https://doi.org/10.3390/e19020054))\
Yubo Li, Yongqiang Cheng, Xiang Li, Xiaoqiang Hua, and Yuliang Qin\
*Entropy* · Jan 26, 2017 · 8 citations

> The measurement update stage in the nonlinear filtering is considered in the viewpoint of information geometry, and the filtered state is considered as an optimization estimation in parameter space has been corresponded with the iteration in the statistical manifold, then a recursive method is proposed in this paper. This method is derived based on the natural gradient descent on the statistical manifold, which constructed by the posterior probability density function (PDF) of state conditional on the measurement. The derivation procedure is processing in the geometric viewpoint, and gives a geometric interpretation for the iteration update. Besides, the proposed method can be seen as an extended for the Kalman filter and its variants. For the one step in our proposed method, it is identical to the Extended Kalman filter (EKF) in the nonlinear case, while traditional Kalman filter in the linear case. Benefited from the natural gradient descent used in the update stage, our proposed method performs better than the existing methods, and the results have showed in the numerical experiments.

------------------------------------------------------------------------

44\. · 87% match · 2017 · 1.5 cit/yr\
**Bayesian Nonlinear Filtering via Information Geometric Optimization** ([link](https://doi.org/10.3390/e19120655))\
Yubo Li et al.\
*Entropy* · Dec 1, 2017 · 13 citations

> In this paper, Bayesian nonlinear filtering is considered from the viewpoint of information geometry and a novel filtering method is proposed based on information geometric optimization. Under the Bayesian filtering framework, we derive a relationship between the nonlinear characteristics of filtering and the metric tensor of the corresponding statistical manifold. Bayesian joint distributions are used to construct the statistical manifold. In this case, nonlinear filtering can be converted to an optimization problem on the statistical manifold and the adaptive natural gradient descent method is used to seek the optimal estimate. The proposed method provides a general filtering formulation and the Kalman filter, the Extended Kalman filter (EKF) and the Iterated Extended Kalman filter (IEKF) can be seen as special cases of this formulation. The performance of the proposed method is evaluated on a passive target tracking problem and the results demonstrate the superiority of the proposed method compared to various Kalman filter methods.

------------------------------------------------------------------------

45\. · 87% match · 2026\
**Online Generalised Predictive Coding** ([link](https://www.semanticscholar.org/paper/be2fd86b7e22d14a4d7e88132a5dec0aa7509e7e))\
Mehran H. Bazargani, Szymon Urbas, Adeel Razi, T. Brendan Murphy, and Karl J. Friston\
May 4, 2026 · 0 citations

> This paper introduces an extension of generalised filtering for online applications. Generalised filtering refers to data assimilation schemes that jointly infer latent states, learn unknown model parameters, and estimate uncertainty in an integrated framework – e.g., estimate state and observation noise – at the same time (i.e., triple estimation). This framework appears across disciplines under different names, including variational Kalman-Bucy filtering in engineering, generalised predictive coding in neuroscience, and Dynamic Expectation Maximisation (DEM) in time-series analysis. Here, we specialise DEM for \`\`online’’data assimilation, through a separation of temporal scales. We describe the variational principles and procedures that allow one to assimilate data in a way that allows for a slow updating of parameters and precisions, which contextualise fast Bayesian belief updating about the dynamic hidden states. Using numerical studies, we demonstrate the validity of online DEM (ODEM) using a non-linear – and potentially chaotic – generative model, to show that the ODEM scheme can track the latent states of the generative process, even when its functional form differs fundamentally from the dynamics of the generative model. Framed from a neuro-mimetic predictive coding perspective, ODEM offers a biologically inspired solution to online inference, learning, and uncertainty estimation in dynamic environments.

------------------------------------------------------------------------

46\. · 86% match · 2001 · 8.3 cit/yr\
**Information-theoretic approach to the study of control systems** ([link](https://doi.org/10.1016/j.physa.2003.09.007))\
H. Touchette and S. Lloyd\
*Physica A-statistical Mechanics and Its Applications* · Apr 2, 2001 · 209 citations

> We propose an information-theoretic framework for analyzing control systems based on the close relationship of controllers to communication channels. A communication channel takes an input state and transforms it into an output state. A controller, similarly, takes the initial state of a system to be controlled and transforms it into a target state. In this sense, a controller can be thought of as an actuation channel that acts on inputs to produce desired outputs. In this transformation process, two different control strategies can be adopted: (i) the controller applies an actuation dynamics that is independent of the state of the system to be controlled (open-loop control); or (ii) the controller enacts an actuation dynamics that is based on some information about the state of the controlled system (closed-loop control). Using this communication channel model of control, we provide necessary and sufficient conditions for a system to be perfectly controllable and perfectly observable in terms of information and entropy. In addition, we derive a quantitative trade-off between the amount of information gathered by a closed-loop controller and its relative performance advantage over an open-loop controller in stabilizing a system. This work supplements earlier results (Phys. Rev. Lett. 84 (2000) 1156) by providing new derivations of the advantage afforded by closed-loop control and by proposing an information-based optimality criterion for control systems. New applications of this approach pertaining to proportional controllers, and the control of chaotic maps are also presented.

------------------------------------------------------------------------

47\. · 86% match · 2021 · 18 cit/yr\
**Variational Adaptive Kalman Filter With Gaussian-Inverse-Wishart Mixture Distribution** ([link](https://doi.org/10.1109/TAC.2020.2995674))\
Yulong Huang, Yonggang Zhang, P. Shi, and J. Chambers\
*IEEE Transactions on Automatic Control* · Apr 1, 2021 · 91 citations

> In this article, a new variational adaptive Kalman filter with Gaussian-inverse-Wishart mixture distribution is proposed for a class of linear systems with both partially unknown state and measurement noise covariance matrices. The state transition and measurement likelihood probability density functions are described by a Gaussian-inverse-Wishart mixture distribution and a Gaussian-inverse-Wishart distribution, respectively. The system state vector together with the state noise covariance matrix and the measurement noise covariance matrix are jointly estimated based on the derived hierarchical Gaussian model. Examples are provided to demonstrate the effectiveness and potential of the developed new filtering design techniques.

------------------------------------------------------------------------

48\. · 85% match · 2009 · 23 cit/yr\
**Relevance of error: what drives motor adaptation?** ([link](https://doi.org/10.1152/jn.90545.2008))\
Kunlin Wei and Konrad Paul Kording\
*Journal of neurophysiology* · Feb 1, 2009 · 398 citations

> During motor adaptation the nervous system constantly uses error information to improve future movements. Today’s mainstream models simply assume that the nervous system adapts linearly and proportionally to errors. However, not all movement errors are relevant to our own action. The environment may transiently disturb the movement production-for example, a gust of wind blows the tennis ball away from its intended trajectory. Apparently the nervous system should not adapt its motor plan in the subsequent tennis strokes based on this irrelevant movement error. We hypothesize that the nervous system estimates the relevance of each observed error and adapts strongly only to relevant errors. Here we present a Bayesian treatment of this problem. The model calculates how likely an error is relevant to the motor plant and derives an ideal adaptation strategy that leads to the most precise movements. This model predicts that adaptation should be a nonlinear function of the size of an error. In reaching experiments we found strong evidence for the predicted nonlinear strategy. The model also explains published data on saccadic gain adaptation, adaptation to visuomotor rotations, and force perturbations. Our study suggests that the nervous system constantly and effortlessly estimates the relevance of observed movement errors for successful motor adaptation.

------------------------------------------------------------------------

49\. · 85% match · 2020 · 1.4 cit/yr\
**Stochastic Online Optimization using Kalman Recursion** ([link](https://www.semanticscholar.org/paper/cfe373d89fe9ab88db055a8f792ecbc332a1910c))\
Joseph de Vilmarest and Olivier Wintenberger\
*J. Mach. Learn. Res.* · Feb 7, 2020 · 9 citations

> We study the Extended Kalman Filter in constant dynamics, offering a bayesian perspective of stochastic optimization. We obtain high probability bounds on the cumulative excess risk in an unconstrained setting. The unconstrained challenge is tackled through a two-phase analysis. First, for linear and logistic regressions, we prove that the algorithm enters a local phase where the estimate stays in a small region around the optimum. We provide explicit bounds with high probability on this convergence time. Second, for generalized linear regressions, we provide a martingale analysis of the excess risk in the local phase, improving existing ones in bounded stochastic optimization. The EKF appears as a parameter-free O(d^2) online algorithm that optimally solves some unconstrained optimization problems.

------------------------------------------------------------------------

50\. · 84% match · 2017 · 5.2 cit/yr\
**Intrinsically Bayesian Robust Kalman Filter: An Innovation Process Approach** ([link](https://doi.org/10.1109/TSP.2017.2656845))\
Roozbeh Dehghannasiri and M. S. Esfahani\
*IEEE Transactions on Signal Processing* · May 15, 2017 · 47 citations

*Showing top 50 of 137 papers. Full details available via CSV or BibTeX export.*
