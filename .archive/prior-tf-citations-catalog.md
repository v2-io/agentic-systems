# Temporal Feedback Theory — Citations and Prior Art Catalog

This document maps each conceptual pillar of Temporal Feedback Theory (TFT) to its relevant prior art, organized by the TF document where the concept is introduced. For each citation, the relevance to TFT is noted so that appropriate citation language can be drafted during manuscript preparation.

***

## TF-01: Scope — Adaptive Agents Under Uncertainty

### POMDP Framework

TFT's scope condition — an agent coupled to a partially observable, uncertain environment through observation and action channels — is the setting formalized by the Partially Observable Markov Decision Process (POMDP) literature.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kaelbling, L. P., Littman, M. L., & Cassandra, A. R.** (1998). "Planning and acting in partially observable stochastic domains." *Artificial Intelligence*, 101(1–2), 99–134.[^1] | Canonical POMDP formalization: belief states, optimal policies under partial observability. TF-01's scope condition \(\mathcal{S}_{\text{TFT}}\) is essentially the POMDP setting generalized beyond MDP reward structure. |
| **Cassandra, A. R.** (2003). "A Survey of POMDP Applications."[^2] | Survey showing breadth of POMDP applications; supports TF-01's claim that the scope includes robots, medical systems, organizational decision-making, etc. |

### Shannon Entropy and Information Theory

TF-01 uses \(H(\Omega_t \mid \mathcal{H}_t) > 0\) as the constitutive condition for residual uncertainty.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Shannon, C. E.** (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379–423. | Foundation for conditional entropy as a measure of residual uncertainty. TF-01's scope condition is stated in Shannon's formalism. |

***

## TF-02: Causal Structure

### Pearl's Causal Hierarchy

TF-02 grounds its three levels of epistemic access (associational, interventional, counterfactual) in Pearl's causal hierarchy, reinterpreted through the temporal structure of the feedback loop.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Pearl, J.** (2000; 2nd ed. 2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.[^3][^4] | Foundational treatment of structural causal models, do-calculus, and the three-level causal hierarchy. TF-02 adopts Pearl's hierarchy as levels of epistemic access. |
| **Bareinboim, E., Correa, J. D., Ibeling, D., & Icard, T.** (2022). "Pearl's Hierarchy and the Foundations of Causal Inference." In *Probabilistic and Causal Inference* (eds. Geffner et al.).[^5] | Modern formalization of the Pearl Causal Hierarchy (PCH); proves the Causal Hierarchy Theorem showing layers almost always separate. Supports TF-02's claim that interventional information is qualitatively different from associational. |
| **Pearl, J.** (2018). *The Book of Why*. Basic Books. | General-audience presentation of causal reasoning; useful for the motivation behind TF-02's grounding of CIY in interventional semantics. |

### Causal Information Yield

The concept of actions generating information about causal structure connects to:

| Citation | Relevance to TFT |
|----------|-------------------|
| **Feldbaum, A. A.** (1960). "Dual control theory I–IV." *Avtomatika i Telemekhanika*, 21(9).[^6][^7] | Introduced the idea that control actions serve a *dual* purpose: directing (exploitation) and investigating (exploration). TF-02's CIY formalizes the "investigating" component as causal information. |

***

## TF-03: The Model

### Sufficient Statistics

TF-03's core claim — that the model is a compression of the interaction history functioning as a sufficient statistic — draws on classical statistics.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Fisher, R. A.** (1922). "On the mathematical foundations of theoretical statistics." *Phil. Trans. Royal Society A*, 222, 309–368. | Introduced the concept of sufficient statistics. TF-03's model sufficiency \(S(M_t)\) generalizes Fisher's concept to the agent-environment setting. |
| **Neyman, J.** (1935). "Sur un teorema concernente le cosiddette statistiche sufficienti." *Giornale dell'Istituto Italiano degli Attuari*, 6, 320–334. | Fisher-Neyman factorization theorem; the mathematical basis for sufficiency. |

### Information Bottleneck

TF-03 uses the information bottleneck framework to characterize optimal model compression.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Tishby, N., Pereira, F. C., & Bialek, W.** (2000). "The information bottleneck method." *arXiv:physics/0004057*.[^8][^9] | The IB method minimizes \(I(X;T) - \beta I(T;Y)\). TF-03's model formulation is directly an IB problem: minimize retained history (compression) while maximizing predictive information about future observations. |
| **Shwartz-Ziv, R. & Tishby, N.** (2017). "Opening the black box of deep neural networks via information." *arXiv:1703.00810*. | Extended IB to deep learning; relevant to TF-03's claim that neural networks can be analyzed through the sufficiency/compression lens. |

### Rate-Distortion Theory

| Citation | Relevance to TFT |
|----------|-------------------|
| **Cover, T. M. & Thomas, J. A.** (2006). *Elements of Information Theory* (2nd ed.). Wiley. | Standard reference for rate-distortion theory, mutual information, and entropy; underpins TF-03's information-theoretic formulations. |

***

## TF-04: Event-Driven Dynamics

### Asynchronous and Multi-Rate Systems

TF-04 generalizes the discrete-time formulation to event-driven, multi-channel, multi-rate dynamics.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Åström, K. J. & Bernhardsson, B.** (2002). "Comparison of Riemann and Lebesgue sampling for first order stochastic systems." *Proc. 41st IEEE Conf. on Decision and Control*. | Event-triggered vs. periodic sampling in control; directly relevant to TF-04's event-driven formulation. |
| **Tabuada, P.** (2007). "Event-triggered real-time scheduling of stabilizing control tasks." *IEEE Trans. Automatic Control*, 52(9), 1680–1685. | Event-triggered control theory; supports TF-04's claim that event-driven dynamics are more natural for many adaptive systems. |

***

## TF-05: The Mismatch Signal

### Prediction Error / Innovation

TF-05's mismatch signal is the prediction error — the difference between predicted and actual observation. This concept appears independently across many fields.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kalman, R. E.** (1960). "A new approach to linear filtering and prediction problems." *J. Basic Engineering (ASME)*, 82(1), 35–45.[^10] | The innovation sequence in the Kalman filter is the exact linear-Gaussian instantiation of TF-05's mismatch signal \(\delta_t = o_t - \hat{o}_t\). |
| **Rao, R. P. N. & Ballard, D. H.** (1999). "Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects." *Nature Neuroscience*, 2(1), 79–87.[^11][^12] | Predictive coding in neuroscience: feedback connections carry predictions, feedforward connections carry prediction errors. TF-05's mismatch signal is the computational equivalent of the prediction error signal in cortical hierarchies. |
| **Friston, K.** (2005). "A theory of cortical responses." *Phil. Trans. Royal Society B*, 360(1456), 815–836. | Generalized predictive coding under the free energy principle; the precision-weighted prediction error is an instance of TF-05's mismatch with TF-06's gain. |
| **Sutton, R. S. & Barto, A. G.** (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.[^13][^14] | The TD error \(\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)\) is the RL instantiation of TF-05's mismatch signal. Standard reference for RL. |

### Bias-Variance Decomposition

TF-05's Proposition 5.1 decomposes expected squared mismatch into model error (bias²) and irreducible noise (variance).

| Citation | Relevance to TFT |
|----------|-------------------|
| **Geman, S., Bienenstock, E., & Doursat, R.** (1992). "Neural networks and the bias/variance dilemma." *Neural Computation*, 4(1), 1–58. | Foundational treatment of bias-variance decomposition for learning systems. TF-05's decomposition is the agent-environment generalization. |

***

## TF-06: The Update Gain

### Kalman Filter and Kalman Gain

TF-06's central empirical claim — that the optimal update gain has the form \(\eta^* = U_M / (U_M + U_o)\) — is exact for the Kalman filter.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kalman, R. E.** (1960). "A new approach to linear filtering and prediction problems." *J. Basic Engineering (ASME)*, 82(1), 35–45.[^10] | The Kalman gain \(K_t = P_{t|t-1}H^T(HP_{t|t-1}H^T + R)^{-1}\) is the exact matrix form of TF-06's uncertainty ratio principle. The scalar case reduces exactly to \(U_M/(U_M + U_o)\). |

### Bayesian Posterior Weighting

| Citation | Relevance to TFT |
|----------|-------------------|
| **Bernardo, J. M. & Smith, A. F. M.** (1994). *Bayesian Theory*. Wiley. | Conjugate Bayesian updating with effective sample size \(\kappa\) is an exact instantiation of TF-06's uncertainty ratio for exponential families. |
| **Diaconis, P. & Ylvisaker, D.** (1979). "Conjugate priors for exponential families." *Annals of Statistics*, 7(2), 269–281. | Formal treatment of conjugate priors and the prior-data weighting that TF-06 identifies as the uncertainty ratio. |

### Adaptive Optimizers

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kingma, D. P. & Ba, J.** (2015). "Adam: A Method for Stochastic Optimization." *Proc. ICLR*.[^15][^16] | Adam's per-parameter adaptive learning rates approximate TF-06's uncertainty ratio per-dimension. |
| **Amari, S.** (1998). "Natural gradient works efficiently in learning." *Neural Computation*, 10(2), 251–276.[^17][^18] | Natural gradient descent uses the Fisher information matrix as a curvature metric, effectively implementing a matrix version of TF-06's gain in distribution space. |

***

## TF-07: Action Selection

### Dual-Process Theory (System 1 / System 2)

TF-07's implicit/explicit action-selection distinction maps onto dual-process theory in cognitive science.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kahneman, D.** (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.[^19][^20] | System 1 (fast, intuitive) and System 2 (slow, deliberate) map directly onto TF-07's implicit (high action fluency) and explicit (deliberative) action selection. |
| **Evans, J. St. B. T. & Stanovich, K. E.** (2013). "Dual-process theories of higher cognition: Advancing the debate." *Perspectives on Psychological Science*, 8(3), 223–241. | More rigorous academic treatment of dual-process theory; relevant nuances for TF-07's implicit/explicit distinction. |

### Separation Principle in Control

| Citation | Relevance to TFT |
|----------|-------------------|
| **Wonham, W. M.** (1968). "On the separation theorem of stochastic control." *SIAM J. Control*, 6(2), 312–326. | The separation principle (estimate state, then apply optimal control) is the control-theoretic foundation for TF-07's claim that action is a function of the model. |

***

## TF-08: Exploration-Exploitation Balance

### Multi-Armed Bandits

| Citation | Relevance to TFT |
|----------|-------------------|
| **Thompson, W. R.** (1933). "On the likelihood that one unknown probability exceeds another in view of the evidence of two samples." *Biometrika*, 25(3/4), 285–294.[^21][^22] | Original Thompson sampling paper. The earliest formal treatment of the exploration-exploitation trade-off that TF-08 generalizes. |
| **Gittins, J. C.** (1979). "Bandit processes and dynamic allocation indices." *J. Royal Statistical Society B*, 41(2), 148–177.[^23][^24] | The Gittins index theorem: optimal solution for discounted multi-armed bandits. TF-08's unified policy objective reduces to the Gittins index in the appropriate setting. |
| **Auer, P., Cesa-Bianchi, N., & Fischer, P.** (2002). "Finite-time analysis of the multiarmed bandit problem." *Machine Learning*, 47(2–3), 235–256.[^25][^26] | UCB1 algorithm; TF-08 maps UCB's confidence bonus to an approximate CIY. |

### Information-Directed Sampling

| Citation | Relevance to TFT |
|----------|-------------------|
| **Russo, D. & Van Roy, B.** (2014/2018). "Learning to Optimize via Information-Directed Sampling." *Operations Research*, 66(1).[^27][^28] | Minimizes the ratio of squared regret to information gain. TF-08's unified objective (value + λ·CIY) is structurally similar; Russo-Van Roy's information ratio is a specific operationalization of TF-08's \(\lambda(M_t)\). |
| **Russo, D. & Van Roy, B.** (2016). "An Information-Theoretic Analysis of Thompson Sampling." *JMLR*, 17(68), 1–30.[^29][^30] | Information-theoretic regret bounds for Thompson sampling; supports TF-08's claim that information measures are central to optimal exploration. |

### Active Inference and the Free Energy Principle

TF-08 notes structural isomorphism between TFT's unified policy objective and the Free Energy Principle's expected free energy decomposition.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Friston, K.** (2010). "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience*, 11(2), 127–138.[^31] | The FEP decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking), structurally matching TF-08's value + CIY. TFT grounds exploration in *causal* information rather than entropy reduction. |
| **Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G.** (2017). "Active Inference: A Process Theory." *Neural Computation*, 29(1), 1–49.[^32] | Detailed process-theory formulation; policy selection, perception, and learning all minimize variational free energy. Relevant comparison point for TF-08's unified objective. |
| **Gershman, S. J.** (2019). "What does the free energy principle tell us about the brain?" *arXiv:1907.05954*.[^33] | Critical analysis of FEP; helps delineate where TFT agrees (structure of objectives) and diverges (causal vs. entropy-reduction grounding). |

### Dual Control Theory

| Citation | Relevance to TFT |
|----------|-------------------|
| **Feldbaum, A. A.** (1960). "Dual control theory I–IV." *Avtomatika i Telemekhanika*, 21(9).[^6][^34][^7] | The dual control concept — directing + investigating — is the control-theoretic precursor to TF-08's value + CIY objective. |

***

## TF-09: The Cost of Deliberation

### Bounded Rationality

| Citation | Relevance to TFT |
|----------|-------------------|
| **Simon, H. A.** (1955). "A behavioral model of rational choice." *Quarterly Journal of Economics*, 69(1), 99–118.[^35][^36] | Introduced bounded rationality and satisficing. TF-09 formalizes the insight that deliberation has costs, and optimal agents satisfice temporally. |
| **Simon, H. A.** (1957). *Models of Man*. Wiley.[^37] | Extended treatment of bounded rationality; the "scissors" analogy (cognitive limitations + environmental structure) parallels TF-09's deliberation-drift trade-off. |

### Metareasoning

| Citation | Relevance to TFT |
|----------|-------------------|
| **Russell, S. & Wefald, E.** (1991). "Principles of Metareasoning." *Artificial Intelligence*, 49, 361–395.[^38][^39] | Formalized the value of computation in terms of its effect on the agent's next decision. TF-09's Proposition 9.1 is a temporal-mismatch instantiation of Russell & Wefald's metareasoning framework. |
| **Russell, S. & Wefald, E.** (1991). *Do the Right Thing: Studies in Limited Rationality*. MIT Press.[^40] | Book-length treatment of rational metareasoning; the "metalevel MDP" concept anticipates TF-09's formalization of deliberation as a nested loop. |

***

## TF-10: Structural Adaptation

### Boyd's OODA Loop and Destruction/Creation

TF-10's destruction-creation cycle for structural adaptation is directly inspired by Boyd.

| Citation | Relevance to TFT |
|----------|-------------------|
| **Boyd, J. R.** (1976). "Destruction and Creation." Unpublished paper.[^41][^42][^43] | Boyd's only written work; describes the dialectic of shattering existing mental models and synthesizing new ones. TF-10's six-phase destruction-creation cycle formalizes Boyd's insight. |
| **Boyd, J. R.** (1987/1996). "The Essence of Winning and Losing." Briefing slides. | Boyd's full OODA loop sketch; the Orient phase — with its feedback links to Observe and Act — is what TFT formalizes as the model \(M_t\). |
| **Coram, R.** (2002). *Boyd: The Fighter Pilot Who Changed the Art of War*. Little, Brown and Company.[^44] | Best biography of Boyd; clarifies that the OODA loop is not a simple cycle but a complex system with implicit guidance and control (IGC) links — exactly TF-07's implicit action. |
| **Richards, C.** (2012). "Boyd's OODA Loop." *Necesse* / Proceedings.[^43] | Scholarly analysis of the full OODA loop; emphasizes that speed alone is not the point — it is the quality of orientation that matters. Supports TF-11's tempo = rate × quality. |

### Kuhn's Paradigm Shifts

| Citation | Relevance to TFT |
|----------|-------------------|
| **Kuhn, T. S.** (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.[^45] | Normal science (parametric adaptation within a paradigm) vs. paradigm shifts (structural adaptation). TF-10 maps Kuhn's framework directly: anomaly accumulation → recognition → decomposition → exploration → recombination → rapid adaptation. |

### Organizational Learning

| Citation | Relevance to TFT |
|----------|-------------------|
| **Argyris, C.** (1977). "Double loop learning in organizations." *Harvard Business Review*, 55(5), 115–125.[^46][^47][^48] | Single-loop learning = TF-06 parametric adaptation within governing variables. Double-loop learning = TF-10 structural adaptation that questions and changes the governing variables themselves. |
| **Argyris, C. & Schön, D. A.** (1978). *Organizational Learning: A Theory of Action Perspective*. Addison-Wesley. | Extended treatment; organizational theory-in-use maps to TFT's model \(M_t\) at the organizational level. |
| **Senge, P. M.** (1990). *The Fifth Discipline*. Doubleday. | Systems thinking in organizational learning; the "learning organization" concept relates to TF-10's claim that organizations must maintain capacity for structural adaptation. |

### Neural Architecture Search and Bayesian Model Selection

| Citation | Relevance to TFT |
|----------|-------------------|
| **Zoph, B. & Le, Q. V.** (2017). "Neural Architecture Search with Reinforcement Learning." *Proc. ICLR*. | ML instantiation of TF-10's structural adaptation: searching over model classes \(\mathcal{M}\) using RL. |
| **Kass, R. E. & Raftery, A. E.** (1995). "Bayes factors." *J. American Statistical Association*, 90(430), 773–795. | Bayesian model selection via marginal likelihood; the principled statistical approach to choosing between model classes, relevant to TF-10's model class fitness \(F(\mathcal{M})\). |

***

## TF-11: Temporal Nesting and Adaptive Tempo

### Boyd's Tempo Concept

| Citation | Relevance to TFT |
|----------|-------------------|
| **Boyd, J. R.** (1976). "New Conception for Air-to-Air Combat." Briefing.[^41] | Boyd's original articulation that "operating at a faster tempo than our adversaries" generates "confusion and disorder." TF-11 formalizes tempo as \(\mathcal{T} = \nu \cdot \kappa\) (rate × quality). |
| **Osinga, F. P. B.** (2007). *Science, Strategy and War: The Strategic Theory of John Boyd*. Routledge. | The most rigorous academic treatment of Boyd's strategic theory; essential for grounding TF-11's tempo and adversarial dynamics in Boyd's original intent. |

### Two-Timescale Stochastic Approximation

| Citation | Relevance to TFT |
|----------|-------------------|
| **Borkar, V. S.** (1997). "Stochastic approximation with two time scales." *Systems & Control Letters*, 29(5), 291–294.[^49][^50][^51] | Foundation for two-timescale convergence analysis in stochastic systems. TF-11's temporal nesting constraint (\(\nu_{n+1} \ll \nu_n\)) is the qualitative version of Borkar's convergence condition. |
| **Konda, V. R. & Tsitsiklis, J. N.** (2004). "Convergence rate of linear two-time-scale stochastic approximation." *Annals of Applied Probability*, 14(2), 796–819.[^50] | Convergence rate analysis for two-timescale methods; supports TF-11's claim about convergence constraints between nested loops. |

### Singular Perturbation Theory

| Citation | Relevance to TFT |
|----------|-------------------|
| **Khalil, H. K.** (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall.[^52][^53] | Standard textbook for Lyapunov stability theory and singular perturbation methods (Tikhonov's theorem). TF-11's fast/slow timescale separation is an instance of singular perturbation structure. |
| **Kokotović, P. V., Khalil, H. K., & O'Reilly, J.** (1986). *Singular Perturbation Methods in Control: Analysis and Design*. Academic Press. | Detailed treatment of singular perturbation methods in control; supports TF-11's temporal nesting formalization. |

***

## Appendix A: Lyapunov Stability Analysis

### Lyapunov Theory

| Citation | Relevance to TFT |
|----------|-------------------|
| **Khalil, H. K.** (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall.[^52][^53] | Chapters 4 (Lyapunov stability), 9 (input-output stability), 14 (singular perturbations). Appendix A's sector conditions, ultimate boundedness, and Lyapunov function construction follow Khalil's framework. |
| **Vidyasagar, M.** (2002). *Nonlinear Systems Analysis* (2nd ed.). SIAM. | Alternative treatment of sector conditions and absolute stability; relevant to Appendix A's sector-condition assumption on the correction function. |

### Input-to-State Stability

| Citation | Relevance to TFT |
|----------|-------------------|
| **Sontag, E. D.** (1989). "Smooth stabilization implies coprime factorization." *IEEE Trans. Automatic Control*, 34(4), 435–443.[^54][^55] | Introduced input-to-state stability (ISS). Appendix A's bounded-mismatch result (Proposition A.1) is structurally an ISS result: bounded disturbance \(\rho\) produces bounded state (mismatch). |
| **Sontag, E. D. & Wang, Y.** (1996). "New characterizations of input-to-state stability." *IEEE Trans. Automatic Control*, 41(9), 1283–1294. | Extended ISS characterizations; relevant to Appendix A's comparison function arguments. |

### Absolute Stability and Sector Conditions

| Citation | Relevance to TFT |
|----------|-------------------|
| **Lur'e, A. I.** (1957). *Some Nonlinear Problems in the Theory of Automatic Control* (in Russian; English translation by H.M. Stationery Office, 1957). | Original sector-condition framework for absolute stability. Appendix A's sector condition on the correction function \(F(\mathcal{T}, \delta)\) descends from Lur'e's approach. |
| **Popov, V. M.** (1961). "Absolute stability of nonlinear systems of automatic control." *Automation and Remote Control*, 22(8), 857–875. | Popov criterion for absolute stability; closely related to Appendix A's sector-condition stability analysis. |

***

## Cross-Cutting: Control Theory

### PID Control

| Citation | Relevance to TFT |
|----------|-------------------|
| **Åström, K. J. & Murray, R. M.** (2008). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press. | Modern textbook covering PID, MPC, and adaptive control from a feedback perspective. TFT's entire framework can be read as a generalization of the feedback control paradigm. |
| **Ziegler, J. G. & Nichols, N. B.** (1942). "Optimum settings for automatic controllers." *Trans. ASME*, 64(11), 759–768. | Classic PID tuning method. TF-06 references Ziegler-Nichols as a one-time gain calibration (estimating the uncertainty ratio once at design time). |

### Model Predictive Control

| Citation | Relevance to TFT |
|----------|-------------------|
| **Rawlings, J. B., Mayne, D. Q., & Diehl, M.** (2017). *Model Predictive Control: Theory, Computation, and Design* (2nd ed.). Nob Hill Publishing. | MPC is the richer control-theoretic instantiation of TF-07's explicit deliberation: the agent uses its model to simulate future trajectories and optimize actions online. |

***

## Cross-Cutting: Reinforcement Learning

### Core RL

| Citation | Relevance to TFT |
|----------|-------------------|
| **Sutton, R. S. & Barto, A. G.** (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.[^13][^14] | Primary RL reference. TD error = TF-05 mismatch; learning rate α = TF-06 degenerate gain; ε-greedy/UCB = TF-08 exploration heuristics. |
| **Watkins, C. J. C. H. & Dayan, P.** (1992). "Q-learning." *Machine Learning*, 8(3–4), 279–292. | Q-learning convergence; the Q-update is a core instantiation of TF-06's update rule with fixed gain. |

### Bayesian RL

| Citation | Relevance to TFT |
|----------|-------------------|
| **Ghavamzadeh, M., Mannor, S., Pineau, J., & Tamar, A.** (2015). "Bayesian reinforcement learning: A survey." *Foundations and Trends in Machine Learning*, 8(5–6), 359–483. | Survey of Bayesian RL methods; these are the RL approaches that most closely implement TF-06's full uncertainty-ratio gain (maintaining posterior over Q-values). |

***

## Cross-Cutting: Biological and Cognitive Science

### Predictive Processing / Predictive Coding

| Citation | Relevance to TFT |
|----------|-------------------|
| **Clark, A.** (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences*, 36(3), 181–204. | Broad argument that brains are "prediction machines." TFT's entire framework — predict, compare (mismatch), update — is the formal skeleton of predictive processing. |
| **Rao, R. P. N. & Ballard, D. H.** (1999). *Nature Neuroscience*, 2(1), 79–87.[^11][^12] | Specific neural implementation of predictive coding; see TF-05 entry above. |

### Immune System as Adaptive Agent

| Citation | Relevance to TFT |
|----------|-------------------|
| **Perelson, A. S. & Weisbuch, G.** (1997). "Immunology for physicists." *Reviews of Modern Physics*, 69(4), 1219–1268. | Formal treatment of immune system dynamics as an adaptive system; relevant to TF-01's scope claim that immune systems are within TFT's purview (affinity maturation = parametric adaptation; novel antibody generation = structural adaptation). |

***

## Cross-Cutting: Mathematical Foundations

### Information Geometry

| Citation | Relevance to TFT |
|----------|-------------------|
| **Amari, S. & Nagaoka, H.** (2000). *Methods of Information Geometry*. AMS/Oxford University Press. | The mathematical framework underlying natural gradients and the Fisher information metric; relevant to TF-06's generalization of the gain to non-Euclidean model spaces. |

### Stochastic Filtering

| Citation | Relevance to TFT |
|----------|-------------------|
| **Bain, A. & Crisan, D.** (2009). *Fundamentals of Stochastic Filtering*. Springer. | Rigorous treatment of nonlinear filtering; the general filtering problem is the mathematical setting that TF-03 (model as sufficient statistic) and TF-06 (optimal gain) address in TFT's more general agent-environment framework. |

***

## Summary: Priority Citation Tiers

### Tier 1 — Must Cite (foundational, directly invoked)

- Kalman (1960) — Kalman gain as exact instantiation of TF-06
- Pearl (2000/2009) — Causal hierarchy for TF-02
- Tishby et al. (2000) — Information bottleneck for TF-03
- Sutton & Barto (2018) — RL framework, TD error, learning rate
- Boyd (1976) — OODA, destruction/creation for TF-10, TF-11
- Khalil (2002) — Lyapunov stability for Appendix A
- Sontag (1989) — ISS for Appendix A
- Kahneman (2011) — System 1/2 for TF-07
- Simon (1955/1957) — Bounded rationality for TF-09
- Friston (2010) — FEP comparison for TF-08
- Feldbaum (1960) — Dual control for TF-08

### Tier 2 — Should Cite (important related work)

- Rao & Ballard (1999) — Predictive coding
- Russo & Van Roy (2014) — Information-directed sampling
- Auer et al. (2002) — UCB
- Gittins (1979) — Gittins index
- Thompson (1933) — Thompson sampling
- Russell & Wefald (1991) — Metareasoning
- Argyris (1977) — Double-loop learning
- Kuhn (1962) — Paradigm shifts
- Kingma & Ba (2015) — Adam optimizer
- Amari (1998) — Natural gradient
- Borkar (1997) — Two-timescale stochastic approximation
- Bareinboim et al. (2022) — PCH formal treatment

### Tier 3 — Nice to Cite (supporting, enriching)

- Cover & Thomas (2006) — Information theory textbook
- Åström & Murray (2008) — Feedback systems textbook
- Osinga (2007) — Academic Boyd analysis
- Clark (2013) — Predictive processing in cognitive science
- Kass & Raftery (1995) — Bayes factors for model selection
- Senge (1990) — Learning organizations
- Wonham (1968) — Separation principle
- Geman et al. (1992) — Bias-variance decomposition

---

## References

1. [[PDF] Planning and acting in partially observable stochastic domains](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf) - Littman, A.R. Cassandra and L.P. Kaelbling, Efficient dynamic-programming updates in partially obser...

2. [[PDF] A Survey of POMDP Applications - Semantic Scholar](https://www.semanticscholar.org/paper/A-Survey-of-POMDP-Applications-Cassandra/9c830d8655a9be25d1c0b0c74e00c7535b5e2de7) - The main purpose of this paper is to show the wider applicability of the pomdp model by way of surve...

3. [Causality (book)](https://en.wikipedia.org/wiki/Causality_(book)) - Causality: Models, Reasoning, and Inference (2000; updated 2009) is a book by Judea Pearl. It is an ...

4. [Causality](https://www.cambridge.org/core/books/causality/B0046844FAE10CBF274D4ACBDAEB5F5B) - Written by one of the preeminent researchers in the field, this book provides a comprehensive exposi...

5. [[PDF] Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf) - In this chapter, we develop a novel and comprehensive treatment of the. PCH through two complementar...

6. [[PDF] A Historical Perspective of Adaptive Control and Learning - arXiv](https://arxiv.org/pdf/2108.11336.pdf) - Abstract. This article provides a historical perspective of the field of adaptive control over the p...

7. [Dual control theory - Wikipedia](https://en.wikipedia.org/wiki/Dual_control_theory) - Dual control theory was developed by Alexander Aronovich Fel'dbaum in 1960. He showed that in princi...

8. [[PDF] The information bottleneck method - Semantic Scholar](https://www.semanticscholar.org/paper/The-information-bottleneck-method-Tishby-Pereira/4ef483f819e11873822416042a4b6dc4652e010c) - The information bottleneck method · Naftali Tishby, Fernando C Pereira, W. Bialek · Published in arX...

9. [[PDF] The information bottleneck method - Princeton University](https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf) - Slonim and N. Tishby, “Agglomerative information bottleneck,” To appear in Advances in Neural Inform...

10. [A New Approach to Linear Filtering and Prediction Problems](https://resourcium.org/resource/new-approach-linear-filtering-and-prediction-problems) - The new method developed here is applied to two well-known problems, confirming and extending earlie...

11. [[PDF] Predictive coding in the visual cortex: a functional interpretation of ...](https://homes.cs.washington.edu/~rao/Rao-Ballard-NN-1999.pdf) - Rao, R. P. N. & Ballard, D. H. Dynamic model of visual recognition predicts neural response properti...

12. [a functional interpretation of some extra-classical receptive-field effects](https://pubmed.ncbi.nlm.nih.gov/10195184/) - Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptiv...

13. [[PDF] Reinforcement Learning - andrew.cmu.ed](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf) - ... edition. Richard S. Sutton and Andrew G. Barto. The MIT Press. Cambridge, Massachusetts. London,...

14. [Barto Book: Reinforcement Learning: An Introduction - Sutton](http://incompleteideas.net/book/the-book-2nd.html) - Richard S. Sutton and Andrew G. Barto, Second Edition (see here for the first edition), MIT Press, C...

15. [[PDF] Adam: A Method for Stochastic Optimization - Intel](https://www.intel.com/content/dam/www/public/us/en/ai/documents/1412.6980.pdf) - We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective ...

16. [[1412.6980] Adam: A Method for Stochastic Optimization - arXiv.org](https://arxiv.org/abs/1412.6980) - We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective ...

17. [Natural Gradient Works Efficiently in Learning - IEEE Xplore](https://ieeexplore.ieee.org/document/6790500/) - Information geometry is used for calculating the natural gradients in the ... 15 February 1998. ISSN...

18. [[PDF] Natural Gradient Works Eciently in Learning - Semantic Scholar](https://www.semanticscholar.org/paper/Natural-Gradient-Works-Eciently-in-Learning-Amari/e1c2a2fd6a26947e5bbb8df47e30c1199ab1270d) - Neural Learning in Structured Parameter Spaces - Natural Riemannian Gradient · S. Amari. Computer Sc...

19. [Adaptive Decision‐Making “Fast” and “Slow”: A Model of Creative ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC11892090/) - The late Daniel Kahneman introduced the concept of fast and slow thinking, representing two distinct...

20. [[PDF] Daniel Kahneman-Thinking, Fast and Slow .pdf](https://dn790002.ca.archive.org/0/items/DanielKahnemanThinkingFastAndSlow/Daniel%20Kahneman-Thinking,%20Fast%20and%20Slow%20%20.pdf) - Every author, I suppose, has in mind a setting in which readers of his or her work could benefit fro...

21. [Thompson sampling - Wikipedia](https://en.wikipedia.org/wiki/Thompson_sampling) - Thompson sampling was originally described by Thompson in 1933. It was subsequently rediscovered num...

22. [On the Likelihood that One Unknown Probability Exceeds Another in ...](https://www.jstor.org/stable/2332286) - ON THE LIKELIHOOD THAT ONE UNKNOWN. PROBABILITY EXCEEDS ANOTHER IN VIEW. OF THE EVIDENCE OF TWO SAMP...

23. [[PDF] Multi-armed Bandits and the Gittins Index Theorem](https://www.statslab.cam.ac.uk/~rrw1/oc/ocgittins.pdf) - “Bandit problems embody in essential form a conflict evident in all human action: information versus...

24. [A Generalized Gittins Index for a Class of Multiarmed Bandits with ...](https://pubsonline.informs.org/doi/10.1287/moor.1080.0342) - A Generalized Gittins Index for a Class of Multiarmed Bandits ... bandit indices that reduce to thos...

25. [Upper Confidence Bound - Wikipedia](https://en.wikipedia.org/wiki/Upper_Confidence_Bound) - Introduced by Auer, Cesa-Bianchi & Fischer in 2002, UCB and its variants have become standard techni...

26. [[PDF] Finite-time Analysis of the Multiarmed Bandit Problem*](https://people.eecs.berkeley.edu/~russell/classes/cs294/s11/readings/Auer+al:2002.pdf) - Our policies are deterministic and based on upper confidence bounds, with the exception of εn-GREEDY...

27. [Learning to Optimize via Information-Directed Sampling](https://arxiv.org/abs/1403.5556) - We propose information-directed sampling -- a new approach to online optimization problems in which ...

28. [Learning to Optimize via Information-Directed Sampling - PubsOnLine](https://pubsonline.informs.org/doi/10.1287/opre.2017.1663) - We propose information-directed sampling—a new approach to online optimization problems in which a d...

29. [An Information-Theoretic Analysis of Thompson Sampling](https://jmlr.org/papers/v17/14-087.html) - Daniel Russo, Benjamin Van Roy; 17(68):1−30, 2016. Abstract. We provide an information-theoretic ana...

30. [[PDF] An Information-Theoretic Analysis of Thompson Sampling](https://www.jmlr.org/papers/volume17/14-087/14-087.pdf) - Though Thompson sampling was first proposed in 1933 (Thompson, 1933), until recently it was largely ...

31. [Free energy principle - Wikipedia](https://en.wikipedia.org/wiki/Free_energy_principle) - Friston, Karl (2010). "The free-energy principle: a unified brain theory ... Active Inference: The F...

32. [[PDF] Active Inference: A Process Theory - Free Energy Principle](https://activeinference.github.io/papers/process_theory.pdf) - This article describes a process theory based on active inference and be- lief propagation. Starting...

33. [[PDF] What does the free energy principle tell us about the brain?](https://gershmanlab.com/pubs/free_energy.pdf) - Friston and colleagues refer to the minimization of expected free energy with respect to actions as ...

34. [[PDF] EECE 574 - Adaptive Control - Overview](https://courses.ece.ubc.ca/574/EECE574_Beamer01.pdf) - 1960: Feldbaum develops the dual controller in which the control action serves a dual purpose as it ...

35. [Bounded Rationality - Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/bounded-rationality/) - Simon's remark that people satisfice when they haven't the wits to maximize (Simon 1957a: xxiv) poin...

36. [[PDF] Herbert A. Simon - Prize Lecture](https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf) - But the important thing about the search and satisficing theory is that it showed how choice could a...

37. [Bounded rationality](https://en.wikipedia.org/wiki/Bounded_rationality) - Decision-makers, in this view, act as satisficers, seeking a satisfactory solution, with everything ...

38. [Stuart Russell -- Foundations: Rationality and Intelligence](https://people.eecs.berkeley.edu/~russell/research-bo.html) - Stuart Russell and Eric Wefald ``Principles of Metareasoning.'' Artificial Intelligence 49, 1991. Da...

39. [[PDF] Principles of Metareasoning](http://iiif.library.cmu.edu/file/Newell_box00014_fld01011_doc0001/Newell_box00014_fld01011_doc0001.pdf) - In this paper we outline a general approach to the study of formalized metareasoning, not in the sen...

40. [Russell & Wefald 1991: Do the right thing (Chapter 1) - Jim Davies](http://www.jimdavies.org/summaries/russell1991.html) - AI = Designing bounded rational agents, i.e. maximizing the agent's utility over all the behaviors e...

41. [[PDF] Coming Full Circle with Boyd's OODA Loop Ideas - Team One Network](https://teamonenetwork.com/wp-content/uploads/2019/03/COMING-FULL-CIRCLE-WITH-BOYD%E2%80%99S-OODA-LOOP-IDEAS.pdf) - Later, Boyd continued to lay out conceptual groundwork for his OODA Loop conceptualizations in his o...

42. [Destruction and Creation, John Boyd, IOHAI, OODA Loop, Resources](https://iohai.com/iohai-resources/destruction-and-creation.html) - According to Grant Hammond in "The Mind of War", "Destruction and Creation" is the only prose Boyd e...

43. [[PDF] Boyd's OODA Loop](https://ooda.de/media/chet_richards_-_boyds_ooda_loop.pdf) - Boston: Wisdom Publications. - Boyd, J. R. (1976 a). Destruction and creation. (Unpublished paper). ...

44. [OODA your OODA Loop - LessWrong](https://www.lesswrong.com/posts/StBjd8esuXzhqLGNt/ooda-your-ooda-loop) - The process is not a simple loop. Below is a paper Boyd wrote about Destruction and Creation or Dedu...

45. [The Structure of Scientific Revolutions - Wikipedia](https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions) - The Structure of Scientific Revolutions is a 1962 book about the history of science by the philosoph...

46. [Chris Argyris: theories of action, double-loop learning and ... - infed.org](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) - The work of Chris Argyris (1923-2013) has influenced thinking about the relationship of people and o...

47. [[PDF] Double Loop Learning in Organizations - Antonie van Nistelrooij](https://www.avannistelrooij.nl/wp/wp-content/uploads/2017/11/Argyris-1977-Double-Loop-Learning-in-Organisations-HBR.pdf) - q 1977 by the President and Fellows of Harvard College. All rights reserved ... Chris Argyris and Do...

48. [Double Loop Learning in Organizations](https://hbr.org/1977/09/double-loop-learning-in-organizations) - Double Loop Learning in Organizations. by Chris Argyris · From the Magazine (September 1977) · Post;...

49. [[2412.19872] Stochastic Approximation with Two Time Scales - arXiv](https://arxiv.org/abs/2412.19872) - Abstract:Two time scale stochastic approximation is analyzed when the iterates on either or both tim...

50. [Convergence rate of linear two-time-scale stochastic approximation](https://projecteuclid.org/journals/annals-of-applied-probability/volume-14/issue-2/Convergence-rate-of-linear-two-time-scale-stochastic-approximation/10.1214/105051604000000116.pdf) - 1. Introduction. Two-time-scale stochastic approximation methods [Borkar. (1997)] are recursive algo...

51. [Stochastic approximation with two time scales - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0167691197900153) - Abstract. Asymptotic behaviour of a two time scale stochastic approximation algorithm is analysed in...

52. [[PDF] Nonlinear Systems](https://flyingv.ucsd.edu/krstic/files/Khalil-3rd.pdf) - Stability theory plays a central role in systems theory and engineering. ... the energy Lyapunov fun...

53. [[PDF] Nonlinear Systems - Third Edition](https://dl.icdst.org/pdfs/files3/d83d2dc7280085b61da330c9a8ff5e13.pdf) - In particular, we present tools for the stability analysis of nonlinear systems, with emphasis on Ly...

54. [Input-to-state stability - Wikipedia](https://en.wikipedia.org/wiki/Input-to-state_stability) - The notion of ISS was introduced for systems described by ordinary differential equations by Eduardo...

55. [[PDF] On the Input-to-State Stability Property - Sontag Lab](http://www.sontaglab.org/FTPDIR/iss-ejc.pdf) - The “input to state stability” (iss) property provides a natural framework in which to formulate not...

