# Unidentifiability and rate class prior art

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Bottom line](#bottom-line)
- [Question 1](#question-1)
  - [Closest negative-result line](#closest-negative-result-line)
  - [Literal same-marginals different-law witnesses](#literal-same-marginals-different-law-witnesses)
  - [Game-theoretic observational-equivalence line](#game-theoretic-observational-equivalence-line)
  - [What was not found](#what-was-not-found)
  - [Q1 verdict](#q1-verdict)
- [Question 2](#question-2)
  - [Strongest near-miss](#strongest-near-miss)
  - [Regime diagnosis is present, but usually not by rate class](#regime-diagnosis-is-present-but-usually-not-by-rate-class)
  - [Named passive diagnostics that are close, but not rate-class based](#named-passive-diagnostics-that-are-close-but-not-rate-class-based)
  - [Q2 verdict](#q2-verdict)
- [Overall assessment for framing](#overall-assessment-for-framing)
- [References](#references)

## Bottom line

The search results do not contain a clean prior-art hit for either target claim in the exact form posed. For Question 1, the literature does contain strong negative results showing that marginals, equilibrium observations, or componentwise trajectories often identify only coarse equivalence classes rather than the underlying coupling law or strategic structure. But I did not find a paper in this set that explicitly constructs a marginally indistinguishable witness separating potential from non-potential, shared-objective from Nash, or cyclic from cooperative structure in the requested Cournot versus shared-target or matching-pennies versus shared-target style. For Question 2, I did not find a paper that explicitly names convergence-rate class itself as a passive classifier of game regime. What does appear is a strong cluster of near-misses that classify regimes by convergence versus recurrence, last-iterate equilibrium versus average-play CCE behavior, or potentialness, with rate differences used as supporting evidence rather than the named classifier \[Ang15, Cum15, Bie11, Hai08, Zia16, Ana22b, Leg24b, Bic25, Mer17, Pan17b, Leg24, Shi19b\].

| Question | Exact-hit verdict | Strongest papers | Working assessment |
|:---|:---|:---|:---|
| Q1 broader-topology-bit unidentifiability | Not found in this set | \[Ang15\], \[Cum15\], \[Bie11\], \[Hai08\], \[Zia16\], \[Cou01b\] | Strong support for broad underidentification and observational equivalence, but not for the exact cross-topology witness you want |
| Q2 rate class as passive regime classifier | Not found as a named move | \[Ana22b\], \[Leg24b\], \[Shi19b\], \[Bic25\], \[Mer17\], \[Leg24\] | The concept is partly in the air, but mostly as convergence versus recurrence or equilibrium versus CCE taxonomy, not as an explicit rate-class classifier |

## Question 1

The strongest conclusion from the search is that the literature repeatedly proves underidentification of hidden coupling structure from reduced observations, but it stops short of your exact target. In other words, the broad impossibility intuition is well supported, while the specific game-topology witness appears absent from this result set.

### Closest negative-result line

The sharpest network-level impossibility paper in the set is \[Ang15\]. Its core claim is that reconstructing even coarse graph properties is generically as hard as reconstructing the full interaction matrix, and that without persistent excitation one should expect indistinguishability across materially different underlying couplings. This is very close in spirit to the claim that per-component observations underdetermine topology. But the paper is about network reconstruction from temporal data in a general dynamical setting, not about potential structure or game-class separation.

A second strong paper is \[Cum15\]. It proves that delay-reconstruction methods can recover at best the transitive closure of the interaction graph, not direct edges, not self-loops, and not the internal orientation of feedback structure inside strongly connected components. This is an explicit negative result about what componentwise trajectory data cannot tell an observer. It is highly relevant to the phrase broader-topology-bit unidentifiability, but again it is not a game-structure witness and it does not separate potential from non-potential or cooperative from cyclic couplings.

### Literal same-marginals different-law witnesses

The cleanest literal same-marginals counterexamples in the set come from the stochastic-process side, not the game-topology side. \[Cou01b\] constructs stationary processes with infinite memory that share the same finite-order marginals as a target Markov process. The earlier sequence \[Cou98\], \[Ham00\], and \[Ham02\] pushes the same theme even harder: finite-dimensional marginals do not determine the generating dependence law. These are excellent precedents for the formal move same marginals, different hidden coupling law, but they do not encode the specific strategic topologies you are asking about.

\[Bie11\] is especially useful because it sits closer to the coupling question itself. It constructs multivariate Markov chains with prescribed component behavior but different joint dependence structures, distinguishing strong from weak Markov consistency. The paper gives a concrete same marginals, different coupling law phenomenon at the level of component processes. That makes it a strong structural analogue for your target, even though the hidden distinction is filtration-level dependence rather than potential versus cyclic game structure.

### Game-theoretic observational-equivalence line

On the game side, \[Hai08\] is the strongest impossibility paper in the set. It shows that, for a single normal-form game, any interior action distribution can be rationalized as a quantal response equilibrium, so the model has essentially no empirical content at that level. That is a much stronger observational-equivalence statement than mere nonidentification, but it concerns payoff perturbations and equilibrium rationalization, not per-component marginal trajectories or cross-topology coupled dynamics.

\[Zia16\] lands nearby from the inverse direction. Instead of point-identifying a game from equilibrium observations, it characterizes a whole consistent set of games and quantifies its diameter. The important implication is that the data often support a broad equivalence class of games rather than a unique underlying game. Again, this is strong support for underidentification, but not the specific topology-bit witness you want.

The information-structure papers \[Pen03\], \[Pen04\], and \[Leh06\] also matter. Their core move is to study when different information structures are observationally compatible or equivalent with respect to outcome distributions or equilibrium distributions. That is another form of deeper hidden structure surviving unchanged at the observable level. But these papers are about information structure, signaling, and mediation, not about potential structure or cyclic best-response topology.

### What was not found

The search did not surface a paper in which the main theorem or main construction is any of the following:

- a marginally indistinguishable potential versus non-potential witness
- a shared-objective versus Nash witness with matched per-component marginals
- a cyclic or matching-pennies versus cooperative witness with matched per-component marginals
- an explicit no-go theorem saying that these game-structure classes are unidentifiable from per-component marginals alone

### Q1 verdict

**Verdict**

Not found as an explicit prior-art result in this set.

**What can be said safely**

- The negative-result template is well established. Finite-order marginals can fail to identify the generating law \[Cou01b, Cou98, Ham00, Ham02\].
- Component observations often recover only coarse structure such as transitive closure or equivalence classes, not the true topology \[Cum15, Ang15\].
- Equilibrium or action observations in games frequently have weak empirical content and admit broad observational equivalence \[Hai08, Zia16, Pen03, Pen04, Leh06\].

**What still looks novel**

The particular move of building a cross-topology game witness beyond the coupling-sign bit, with the hidden distinction being potential versus non-potential or cooperative versus cyclic structure under matched per-component marginals, still looks novel as both construction and naming claim relative to this search set.

## Question 2

The rate-class question lands in a different place. Here the literature is much closer to your idea, but still seems not to have named rate class itself as the passive classifier. The strongest papers instead classify regimes by trajectory type: convergence versus recurrence, last-iterate Nash versus average-play CCE, or learnable versus non-learnable as a function of potentialness.

### Strongest near-miss

The closest conceptual hit is \[Ana22b\]. Its main theorem gives a dichotomy for optimistic mirror descent in bimatrix games: either the dynamics reach an approximate Nash equilibrium, or else the average play is a strong coarse correlated equilibrium. The paper also ties this split to a striking rate statement: outside the Nash regime, cumulative regret becomes negative and decays linearly. This is very close to your idea because a trajectory family together with its rate behavior distinguishes a point-attractor regime from a distributional regime. But the paper does not present this as a general passive classifier of underlying game structure. It is an algorithm-specific dichotomy for OMD in bimatrix games.

\[Shi19b\] is the clearest direct rate-gap paper in the set. In concave Cournot games, policy gradient converges exponentially to the unique Nash equilibrium, while no-regret methods converge only sublinearly. That is exactly the kind of exponential versus sublinear contrast you care about. However, the paper presents this as a comparison of learning rules exploiting structure to different degrees, not as a named diagnostic for inferring whether the underlying regime is potential, cyclic, equilibrium-attractor, or CCE-only.

### Regime diagnosis is present, but usually not by rate class

\[Leg24b\] is probably the strongest paper for the claim that the basic classifier is already in the air. It explicitly frames finite games along a convergence spectrum under exponential weights, with potential games on the convergence side and harmonic or incompressible games on the recurrence side. That is very close to a passive regime taxonomy. The paper’s diagnostic, though, is qualitative dynamics and geometry: convergence, conserved quantities, and Poincare recurrence. Rate class is secondary.

\[Mer17\] makes an important counterpoint. It proves Poincare recurrence for FoReL in zero-sum settings and states explicitly that regret-based analysis cannot distinguish a convergent system from a recurrent cycling one. That sharply limits any attempt to elevate standard regret rates alone into a regime classifier. In effect, this paper says that the right passive discriminator is often qualitative trajectory behavior, not regret rate.

\[Leg24\] sharpens the same point in harmonic games. Standard no-regret guarantees can coexist with recurrent or even divergent last-iterate behavior, and extrapolation is needed to obtain actual trajectory convergence. This supports your equilibrium-attractor versus distributional-regime distinction, but it also shows why average-play rates by themselves are too blunt to do the classificatory work.

### Named passive diagnostics that are close, but not rate-class based

\[Bic25\] is the cleanest named diagnostic in the set. It proposes potentialness as a scalar predictor of convergence success and equilibrium existence. This matters because it weakens any strong uniqueness claim for passive regime diagnosis in general. The novelty does not lie in passive diagnosis per se. What still seems open is passive diagnosis specifically by convergence-rate class.

\[Pan17b\] is another close neighbour. It uses best-reply structure to predict nonconvergence across multiple learning rules with strong empirical fit. Again, the classifier is structural and passive, but it is not rate based.

\[Per20b\] also belongs in the near-miss set. It contrasts recurrent dynamics in unregularized play with convergent dynamics under reward transformation, and it makes the convergence versus recurrence split very explicit. But because the distinction is induced by regularization, it is closer to an intervention story than to the passive observational classifier you asked for.

### Q2 verdict

**Verdict**

No exact hit found for rate class as an explicitly named passive classifier of game regime.

**What can be said safely**

- The literature strongly supports convergence versus recurrence as a passive diagnostic of regime \[Leg24b, Mer17, Leg24\].
- There are papers in which rate gaps align with regime differences or learning-rule differences, most notably \[Ana22b\] and \[Shi19b\].
- There are named passive diagnostics for related aims, such as potentialness in \[Bic25\] and best-reply-cycle structure in \[Pan17b\].

**What still looks distinctive**

The specific proposal to use convergence-rate class itself, especially exponential versus polynomial or sublinear behavior at the joint-trajectory level, as the named escape from a regime-identification floor still looks distinctive relative to this search set. The nearest prior art treats rate as corroborating evidence inside a broader convergence-versus-recurrence or equilibrium-versus-CCE picture, not as the primary classifier.

## Overall assessment for framing

A careful framing claim supported by this search would be:

- For Q1, the literature already contains strong impossibility and observational-equivalence results showing that reduced observations often underdetermine hidden coupling structure. What appears to be missing is the explicit extension from sign-bit ambiguity to a broader game-topology-bit witness built around potential versus non-potential or cooperative versus cyclic couplings.
- For Q2, the literature already contains a mature convergence-versus-recurrence taxonomy and some sharp rate contrasts, but not an explicit canonized move that names rate class itself as the passive classifier of regime.

That makes the safest novelty claim not that the surrounding ideas are absent, but that the exact two moves you care about remain uncodified: the broader-topology marginal-matching witness for Q1, and rate-class as the named passive classifier for Q2.

---

## References

\[Ang15\] M. T. Angulo, J. A. Moreno, A. Barabási, and Y.-Y. Liu, “Fundamental limitations of network reconstruction,” *ArXiv*, vol. abs/1508.03559, Aug. 2015.

\[Cum15\] B. Cummins, T. Gedeon, and K. Spendlove, “On the Efficacy of State Space Reconstruction Methods in Determining Causality,” *SIAM J. Appl. Dyn. Syst.*, vol. 14, pp. 335–381, Mar. 2015, doi: [10.1137/130946344](https://doi.org/10.1137/130946344).

\[Bie11\] T. Bielecki, J. Jakubowski, and M. Niewkeglowski, “Intricacies of dependence between components of multivariate Markov chains: weak Markov consistency and weak Markov copulae,” May 13, 2011. doi: [10.1214/EJP.V18-2238](https://doi.org/10.1214/EJP.V18-2238).

\[Hai08\] P. A. Haile, A. Hortaçsu, and G. Kosenok, “On the Empirical Content of Quantal Response Equilibrium,” Feb. 01, 2008. doi: [10.1257/AER.98.1.180](https://doi.org/10.1257/AER.98.1.180).

\[Zia16\] J. Ziani, V. Chandrasekaran, and K. Ligett, “Efficiently Characterizing Games Consistent with Perturbed Equilibrium Observations,” Mar. 04, 2016. doi: [10.7907/Z91Z42CF.](https://doi.org/10.7907/Z91Z42CF.)

\[Ana22b\] I. Anagnostides, G. Farina, I. Panageas, and T. Sandholm, “Optimistic Mirror Descent Either Converges to Nash or to Strong Coarse Correlated Equilibria in Bimatrix Games,” *ArXiv*, vol. abs/2203.12074, Mar. 2022, doi: [10.48550/arXiv.2203.12074](https://doi.org/10.48550/arXiv.2203.12074).

\[Leg24b\] D. Legacci, P. Mertikopoulos, and B. S. R. Pradelski, “A geometric decomposition of finite games: Convergence vs. recurrence under exponential weights,” *ArXiv*, vol. abs/2405.07224, May 2024, doi: [10.48550/arXiv.2405.07224](https://doi.org/10.48550/arXiv.2405.07224).

\[Bic25\] M. Bichler, D. Legacci, P. Mertikopoulos, M. Oberlechner, and B. S. R. Pradelski, “Characterizing the Convergence of Game Dynamics via Potentialness,” *Trans. Mach. Learn. Res.*, vol. 2025, Mar. 2025, doi: [10.48550/arXiv.2503.16285](https://doi.org/10.48550/arXiv.2503.16285).

\[Mer17\] P. Mertikopoulos, C. Papadimitriou, and G. Piliouras, “Cycles in adversarial regularized learning,” *ACM-SIAM Symposium on Discrete Algorithms*, pp. 2703–2717, Sep. 2017, doi: [10.1137/1.9781611975031.172](https://doi.org/10.1137/1.9781611975031.172).

\[Pan17b\] M. Pangallo, T. Heinrich, T. Heinrich, and J. Farmer, “Best reply structure and equilibrium convergence in generic games,” *Science Advances*, vol. 5, Apr. 2017, doi: [10.1126/sciadv.aat1328](https://doi.org/10.1126/sciadv.aat1328).

\[Leg24\] D. Legacci, P. Mertikopoulos, C. Papadimitriou, G. Piliouras, and B. S. R. Pradelski, “No-regret learning in harmonic games: Extrapolation in the face of conflicting interests,” *ArXiv*, vol. abs/2412.20203, Dec. 2024, doi: [10.48550/arXiv.2412.20203](https://doi.org/10.48550/arXiv.2412.20203).

\[Shi19b\] Y. Shi and B. Zhang, “Learning in Cournot Games with Limited Information Feedback,” *ArXiv*, vol. abs/1906.06612, Jun. 2019.

\[Cou01b\] M. Courbage and D. Hamdan, “A family of stationary processes with infinite memory having the same p-marginals. Ergodic and spectral properties,” 2001. doi: [10.4064/CM90-2-2](https://doi.org/10.4064/CM90-2-2).

\[Cou98\] M. Courbage and D. Hamdan, “An ergodic Markov chain is not determined by its two-dimensional marginal laws,” Jan. 15, 1998. doi: [10.1016/S0167-7152(97)00096-5](https://doi.org/10.1016/S0167-7152(97)00096-5).

\[Ham00\] D. Hamdan, “Markov Chains with Positive Transitions Are Not Determined by Any p-Marginals,” Aug. 21, 2000. doi: [10.1007/S006050070034](https://doi.org/10.1007/S006050070034).

\[Ham02\] D. Hamdan, “An ergodic Markov chain is not determined by any p-marginals,” 2002. doi: [10.1016/S0019-3577(02)80028-3](https://doi.org/10.1016/S0019-3577(02)80028-3).

\[Pen03\] J. S. Penalva and M. D. Ryall, “Causal assessment in finite extensive-form games,” Sep. 01, 2003.

\[Pen04\] J. Penalva-Zuasti, P. Fabra, and M. D. Ryally, “Empirical Implications of Information Structure in Finite-Length Extensive-Form Games,” 2004.

\[Leh06\] E. Lehrer, D. Rosenberg, and E. Shmaya, “Signaling and mediation in Bayesian games,” 2006.

\[Per20b\] J. Pérolat *et al.*, “From Poincaré Recurrence to Convergence in Imperfect Information Games: Finding Equilibrium via Regularization,” *International Conference on Machine Learning*, pp. 8525–8535, Feb. 2020.
