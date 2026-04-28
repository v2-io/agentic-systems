# Prior Art Analysis for ACT Claims (RAW — methodology was flawed, see caveats)

**Date**: 2026-03-13
**Source**: Research agent output from comparative theory analysis session
**Context**: Part of a deep analysis comparing ACT against Hafez et al. (2026) "A Mathematical Theory of Agency and Intelligence" and the broader landscape of unified agency frameworks.

---

I now have comprehensive data for all 10 claims. Let me compile the analysis.

---

# Prior Art Analysis for Agentic Cycle Theory (ACT) Claims

## Claim 1: Uncertainty Ratio eta* = U_M/(U_M+U_o) as a Universal Gain Principle

### What I Found

The formula eta* = U_M/(U_M+U_o) is structurally identical to the Kalman gain K = P_prior/(P_prior + R), which weights new observations by the ratio of model uncertainty to total uncertainty. This structure is well-established in multiple literatures:

- **Neuroscience / associative learning**: Daw and colleagues explicitly frame the Kalman gain as the optimal learning rate in reinforcement learning contexts, showing it unifies Rescorla-Wagner and TD learning under a Bayesian umbrella. Gershman (2015) in [A Unifying Probabilistic View of Associative Learning](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004567) unifies these models via "Kalman TD learning" -- though he does *not* claim universality beyond associative learning.
- **Hierarchical Gaussian Filter (HGF)**: Mathys et al. (2011, 2014) and Behrens et al. (2007) extended the Kalman filter to hierarchical Bayesian settings with volatility estimation, producing precision-weighted prediction errors where the learning rate depends on relative uncertainty. This is essentially the same ratio at each level of the hierarchy.
- **Active Inference (Friston)**: The free energy framework uses precision weighting throughout -- beliefs are updated proportionally to their precision relative to sensory precision. This is structurally equivalent to the Kalman gain generalized across perception, action, and policy selection.
- **Bilokon & Claisse (2025)**: [SSRN paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5272363) explicitly connects the Kalman gain to optimal learning rate schedules.

### Verdict

**(b) Minor repackaging of well-established results.** The uncertainty ratio formula is the Kalman gain. Calling it "universal" is not itself novel -- Friston's active inference framework already positions precision weighting as a universal principle governing perception, learning, and action. The Daw/Gershman line of work already demonstrates it spans RL and Bayesian conditioning. What ACT *may* add is applying this explicitly to organizational learning, but the mathematical content is not new.

**(c) Closest prior art**: Friston's active inference (precision weighting as universal principle), Mathys et al. HGF (hierarchical uncertainty-ratio learning rates), Gershman 2015 (Kalman TD unification). Distance: **very close** -- the core formula and the claim of cross-domain applicability both exist.

---

## Claim 2: Persistence Condition T > rho/||delta_critical|| via Lyapunov Analysis

### What I Found

- **Viability Theory (Aubin, 1991+)**: Jean-Pierre Aubin's viability theory is an extensive mathematical framework for characterizing the set of initial states from which a system can remain within viability constraints forever. The "viability kernel" is formally defined, and necessary/sufficient conditions for viability are established using differential inclusions. Lyapunov-like functions are explicitly used in viability theory -- Aubin's book has a chapter on extending Lyapunov's second method to viability contexts.
- **Input-to-State Stability (ISS)**: Recent work (e.g., [Modeling and stability analysis of live systems with time-varying dimension](https://arxiv.org/html/2501.15991)) extends ISS to time-varying agent systems with agents entering/leaving, using Lyapunov methods.
- **BEDS / Dissipative Learning Framework** (Caraffa, 2025, [arXiv:2601.17933](https://arxiv.org/abs/2601.17933)): This recent paper explicitly replaces "asymptotic optimality" with "viability" as the primary criterion for adaptive systems, defining viability as "remaining stable, adaptable, and resource-bounded." It uses dissipative structures and information-geometric tools, though does not appear to derive the specific T > rho/||delta|| condition.
- **Ecological persistence theory**: The R* rule in ecology formalizes the minimum resource level needed for species persistence. Lyapunov methods for population persistence are well-established (e.g., Thieme 2003, "Dynamical Systems and Population Persistence").

### Verdict

**(b) Novel in its specific form, but the conceptual territory is well-mapped.** Viability theory already provides the general mathematical machinery for "when can a system persist given constraints and disturbances." Using Lyapunov analysis for adaptive agent persistence is not new. The *specific inequality* T > rho/||delta_critical|| appears to be a particular instantiation that may be novel in its compact form, but the idea that "resources must exceed drain rate relative to environmental disturbance for persistence" is well-established across viability theory and ecological dynamics.

**(c) Closest prior art**: Aubin's viability theory (1991), Thieme's population persistence via Lyapunov functions, and the BEDS framework (2025). Distance: **moderate** -- the specific formula may be new, but the conceptual claim and the method (Lyapunov + viability) are established.

---

## Claim 3: Adversarial Tempo Advantage with Superlinear Scaling (exponent 2 or 1.5)

### What I Found

- **Lanchester's Laws (1916)**: These are exactly about superlinear scaling advantages in adversarial dynamics. Lanchester's square law gives a quadratic (exponent 2) advantage to the numerically superior force. The exponent 1.5 is a well-known intermediate model used when combat conditions fall between the linear law (ancient melee) and the square law (modern ranged combat). This is textbook material in operations research and military modeling.
- **OODA Loop literature**: Boyd's work argues qualitatively that faster adaptation yields advantage, but it has never been rigorously formalized with scaling exponents. The [2022 OODA adversarial analysis paper](https://arxiv.org/abs/2203.15502) uses simulation-based approaches but does not derive scaling laws.
- **No prior work found** that specifically recasts Lanchester-type scaling in terms of *adaptation rate* differentials between agents (as opposed to force-size differentials).

### Verdict

**(b) Partially novel synthesis, but builds on very well-known foundations.** The specific exponents (2 and 1.5) come directly from Lanchester's laws, which are over a century old. The qualitative tempo advantage is pure Boyd/OODA. What might be genuinely new is formalizing the connection between *adaptation rate differences* and superlinear scaling advantages -- mapping the Lanchester framework from "force size" to "adaptation speed." However, I could not find this specific mapping claimed before. If ACT is simply asserting "faster adapters win with superlinear advantage" and citing 2 or 1.5, this is Lanchester restated with different labels.

**(c) Closest prior art**: Lanchester's laws (1916) for the exponents, Boyd/OODA for the tempo concept. Distance: **close** for the exponents, **moderate** for the specific adaptation-rate framing.

---

## Claim 4: Strategy Must Be a DAG -- Derived from Temporal Ordering + Uncertainty + Revisability

### What I Found

- **Partial-order planning (AI planning, 1990s onward)**: Plans are explicitly represented as DAGs with temporal ordering constraints. The fact that a plan with temporal precedence constraints forms a DAG is essentially definitional -- a partial order is acyclic by definition. This is textbook AI planning (Russell & Norvig, Weld 1994, etc.).
- **DAG-Plan (2024)**: Recent work like [DAG-Plan](https://arxiv.org/html/2406.09953v1) generates "directed acyclic dependency graphs" for robotic planning, with "clear temporal relationships."
- **Wikipedia on DAGs**: "Directed acyclic graph representations of partial orderings have many applications in scheduling for systems of tasks with ordering constraints."
- **The derivation**: The claim that temporal ordering *implies* acyclicity is a basic mathematical fact (a strict partial order is by definition irreflexive and transitive, hence acyclic). Adding uncertainty and revisability does not change this.

### Verdict

**(b) Not novel.** That plans/strategies must be DAGs due to temporal ordering constraints is a basic, well-known result in AI planning, scheduling theory, and order theory. The mathematical fact that temporal ordering produces acyclicity is trivial. Adding "uncertainty" and "revisability" to the derivation does not change the conclusion or add substantive novelty -- plans under uncertainty are still DAGs (the uncertainty affects which branches are chosen, not the acyclicity of the structure).

**(c) Closest prior art**: Partial-order planning literature (Weld 1994, UCPOP, etc.), DAG scheduling theory. Distance: **essentially identical** -- this is standard material.

---

## Claim 5: Satisfaction Gap / Control Regret Split

### What I Found

- **Bias-Variance-Noise decomposition**: The standard decomposition of prediction error into irreducible noise + bias + variance is structurally similar: some error is inherent (like "infeasible goal"), some is from the model/strategy.
- **Regret decomposition in RL/online learning**: Regret is decomposed into various terms (approximation error, estimation error, optimization error) in the learning theory literature. "Least regret control" (Lions 1992) decomposes control problems under uncertainty.
- **Satisficing vs. optimizing (Simon 1956)**: Herbert Simon's satisficing framework distinguishes between goal-setting and strategy-execution quality, though not in this mathematical form.
- **No exact match found** for the specific terminology "satisfaction gap" (infeasible goal) vs. "control regret" (bad strategy) as a formal decomposition of goal-reality mismatch.

### Verdict

**(b) Moderately novel terminology/framing applied to well-established concepts.** The idea that poor outcomes can stem from either unrealistic goals or poor execution is ancient wisdom. The bias-variance decomposition, Simon's satisficing, and regret decomposition in control theory all carve up similar conceptual territory. However, the specific formal decomposition into "satisfaction gap" (goals exceed what's achievable) vs. "control regret" (strategy underperforms relative to what's achievable) does not appear to have been named or formalized in exactly this way before.

**(c) Closest prior art**: Bias-variance-noise decomposition, Simon's satisficing, regret decomposition in online learning. Distance: **moderate** -- the conceptual distinction exists but the specific formalization and naming appear new.

---

## Claim 6: Directed Separation -- Epistemic Updates Are Goal-Blind

### What I Found

- **Separation principle in LQG control**: The classic result that optimal estimation (Kalman filter) and optimal control (LQR) can be designed independently. The estimator does not need to know the control objective. This is *exactly* the claim that epistemic updates are goal-blind, in the LQG setting.
- **Separation principle limitations**: It is well-established that the separation principle does **not** hold in general for nonlinear systems, partially observed systems, or systems with non-Gaussian noise. There is active research on extensions (e.g., [separation for prescribed-time nonlinear systems](https://www.sciencedirect.com/science/article/abs/pii/S0005109824004771)), but these are restricted classes.
- **Active inference (Friston)**: In active inference, perception and action are **not** separated -- they jointly minimize free energy. Epistemic actions (exploration) are explicitly goal-directed. This directly *contradicts* the claim of goal-blind epistemic updates.
- **Georgiou & Lindquist**: Extended the separation principle to martingale-driven systems but still within restricted classes.

### Verdict

**(b) This is the separation principle from LQG, and claiming it holds generally is actually a stronger (and likely incorrect) claim.** If ACT claims this as a *derived general principle*, it is either (a) restating the LQG separation principle, which is classic, or (b) claiming it holds more broadly, which contradicts known results about the failure of separation in nonlinear/non-Gaussian systems and contradicts active inference where epistemic foraging is explicitly goal-directed.

**(c) Closest prior art**: Separation principle in stochastic control (Wonham 1968, etc.), LQG separation theorem. Distance: **essentially identical** to the LQG result. If ACT claims it holds generally, this is a contested extension that conflicts with established results.

---

## Claim 7: Orient Cascade -- M_t Updates Before Sigma_t Before O_t, Forced by Information Dependency

### What I Found

- **Boyd's OODA loop**: Boyd emphasized the Orient phase as central, but he never wrote down a formal mathematical treatment. He described it qualitatively as involving "analysis and synthesis" of observations, prior experience, cultural traditions, and genetic heritage. Boyd's presentations are informal -- he never published articles or books with formal mathematical content.
- **No formal treatment found** of a specific ordering within the Orient phase (model update before goal-state update before outcome evaluation).
- **Bayesian decision theory**: Standard Bayesian updating updates beliefs before making decisions, which is a two-step separation (update beliefs, then optimize actions given beliefs). But this does not specify a three-way cascade within the belief update itself.
- **The HGF (Mathys et al.)**: Has a hierarchical cascade where lower-level beliefs update before higher-level volatility estimates, but this is bottom-up, not the specific M -> Sigma -> O ordering ACT describes.

### Verdict

**(b) Appears to be a novel formalization.** The specific claim that within an orient/update phase, model parameters M must update before uncertainty Sigma before objectives O, forced by information dependency, does not appear to have been formalized before. Boyd's work is qualitative. Standard Bayesian theory separates estimation from decision but does not decompose the estimation phase into this three-stage cascade. This seems like a genuinely novel (if potentially debatable) structural claim.

**(c) Closest prior art**: Boyd's informal OODA descriptions, hierarchical Bayesian update structures. Distance: **significant** -- the specific three-part ordering with formal information-dependency justification appears new.

---

## Claim 8: Code Quality as Observation Infrastructure (U_o in Software Development)

### What I Found

- **Technical debt and cognitive load**: There is extensive literature on how poor code quality increases developer cognitive load, slows comprehension, and increases error rates. Google's research on technical debt, the DX framework focusing on cognitive load as a core developer experience dimension, and ISO 25010/5055 quality models all address this.
- **Signal-to-noise in code metrics**: [NDepend blog](https://blog.ndepend.com/code-quality-metrics-signal-noise/) uses "signal vs. noise" framing for code quality metrics, but metaphorically, not as a formal information-theoretic model.
- **No formal model found** that treats code quality as determining observation noise (U_o) in a Kalman-gain-like framework for developer decision-making. The literature treats code quality as affecting "productivity" or "cognitive load" but not as a formal observation channel with quantifiable noise parameters.

### Verdict

**(b) Appears to be a novel application/formalization.** The qualitative insight that bad code makes it harder for developers to "see" what's happening is well-known and discussed extensively in the technical debt literature. But formalizing this as code quality = observation noise parameter U_o in a control-theoretic framework for developer behavior does not appear to exist in the literature.

**(c) Closest prior art**: Technical debt literature, cognitive load research, DX metrics. Distance: **significant** -- the conceptual observation is known, but the formal treatment as observation noise in a control/estimation framework appears genuinely new.

---

## Claim 9: Composition Closure via Timescale Separation

### What I Found

- **Timescale separation in multi-agent systems**: This is extensively studied. Singular perturbation theory applied to multi-agent hierarchies is a mature field. Key results include:
  - Agents in densely connected clusters synchronize on fast timescales, then clusters interact on slow timescales (network singular perturbation).
  - Hierarchical control with timescale separation is standard in robotics and process control.
  - [Taxonomy of Hierarchical Multi-Agent Systems](https://arxiv.org/html/2508.12683) (2025) explicitly describes temporal hierarchy as "long-term planning and short-term reaction."
  - [Time Scale Separation and Hierarchical Control with Koopman Operator](https://arxiv.org/html/2506.15586) (2025) provides formal analysis of cross-scale interactions.
- **Composition/composability**: The idea that timescale separation enables modular composition (you can analyze subsystems independently when they operate on different timescales) is standard in singular perturbation theory (Kokotovic et al.).

### Verdict

**(b) Not novel.** Timescale separation as a mechanism enabling compositional analysis of multi-agent hierarchies is well-established in control theory (singular perturbation), multi-agent systems, and hierarchical reinforcement learning. The term "composition closure" may be new terminology, but the underlying idea -- that timescale separation allows you to analyze coupled systems as approximately independent modules -- is textbook singular perturbation theory.

**(c) Closest prior art**: Kokotovic's singular perturbation methods, network timescale separation (Chow & Kokotovic), recent hierarchical MAS literature. Distance: **very close** -- this is standard material with perhaps new terminology.

---

## Claim 10: Communication Gain eta*_ji with Trust-Dependent Weighting

### What I Found

- **Inverse-variance weighting / precision weighting**: The Bayesian approach to combining information sources by weighting each by its precision (inverse variance) is standard. This is how the Kalman filter combines prior and measurement, and how meta-analyses combine studies.
- **Trust-weighted information in multi-agent systems**: The FIRE model, HAMS model, and many others (surveyed in [ACM Computing Surveys 2015](https://dl.acm.org/doi/10.1145/2816826)) formally model trust as a weight on information from other agents. Bayesian trust updating using pseudomeasurements exists ([arXiv:2403.16956](https://arxiv.org/abs/2403.16956)).
- **Credibility theory (actuarial science)**: The Buhlmann credibility formula is structurally identical to the Kalman gain -- it weights new data by a "credibility factor" that depends on the ratio of process variance to total variance. This is used in insurance to combine individual experience with group averages.
- **Active inference multi-agent**: Friston's framework extends to multi-agent settings with precision-weighted message passing.

### Verdict

**(b) Minor repackaging of established concepts.** Weighting communicated information by trust (which maps to precision/reliability) in a Bayesian framework is well-established in multi-agent trust models, sensor fusion, credibility theory, and precision-weighted message passing. Calling it "communication gain eta*_ji" with trust-dependent weighting is giving a new name to the standard Bayesian information fusion formula applied to inter-agent communication.

**(c) Closest prior art**: Bayesian sensor fusion, credibility theory (Buhlmann), multi-agent trust models (FIRE, HAMS), precision-weighted message passing. Distance: **very close** -- this is standard Bayesian information fusion with trust = precision.

---

# Summary Table

| Claim | Novelty Assessment | Closest Prior Art Distance |
|---|---|---|
| 1. Uncertainty ratio eta* as universal gain | **Low** -- Kalman gain + Friston's precision weighting already claimed universal | Very close |
| 2. Persistence condition T > rho/\|\|delta\|\| via Lyapunov | **Low-Moderate** -- specific formula may be new; concept is Aubin's viability theory | Moderate |
| 3. Adversarial tempo with superlinear scaling | **Low-Moderate** -- exponents are Lanchester's; adaptation-rate framing may be new | Close |
| 4. Strategy must be a DAG | **None** -- textbook partial-order planning / order theory | Essentially identical |
| 5. Satisfaction gap / control regret split | **Moderate** -- concept exists; specific decomposition and naming may be new | Moderate |
| 6. Directed separation (epistemic = goal-blind) | **None to Low** -- LQG separation principle; claiming generality contradicts known results | Essentially identical to LQG |
| 7. Orient cascade (M before Sigma before O) | **Moderate-High** -- specific three-stage ordering with info-dependency appears new | Significant gap from prior art |
| 8. Code quality as observation noise U_o | **Moderate-High** -- qualitative idea known; formal control-theoretic framing appears new | Significant gap from prior art |
| 9. Composition closure via timescale separation | **None to Low** -- standard singular perturbation theory | Very close |
| 10. Communication gain with trust weighting | **Low** -- standard Bayesian precision-weighted fusion | Very close |

**Bottom line**: Of the 10 claims, most (1, 4, 6, 9, 10) are restatements or minor rebranding of well-established results. Two (3, 5) offer moderately novel reframing of known concepts. Two (7, 8) appear to have genuine novelty in their specific formalization, though the underlying intuitions are not new. Claim 2 falls in between -- the method and concept are established but the specific compact inequality may be a novel derivation. The overall pattern is that ACT appears to be a synthesis framework that gives new names and unified notation to results from control theory, Bayesian inference, viability theory, planning theory, and multi-agent systems, with its primary contribution being the integration rather than any individual claim.

Sources:
- [A Unifying Probabilistic View of Associative Learning (Gershman 2015)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004567)
- [Kalman gain and optimal learning rate schedules (Bilokon & Claisse)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5272363)
- [Daw - Advanced Reinforcement Learning](http://www.princeton.edu/~ndaw/d13.pdf)
- [HGF - Uncertainty in perception (Mathys et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4237059/)
- [Bayesian Foundation for Individual Learning Under Uncertainty (Mathys 2011)](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2011.00039/full)
- [Active inference and epistemic value (Friston et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5167251/)
- [Generalised free energy and active inference](https://link.springer.com/article/10.1007/s00422-019-00805-w)
- [Viability Theory (Aubin)](https://link.springer.com/book/10.1007/978-0-8176-4910-4)
- [Survey of Viability Theory](https://epubs.siam.org/doi/10.1137/0328044)
- [Dissipative Learning Framework (BEDS)](https://arxiv.org/abs/2601.17933)
- [Modeling live systems with time-varying dimension](https://arxiv.org/html/2501.15991)
- [Lanchester's Laws - Wikipedia](https://en.wikipedia.org/wiki/Lanchester's_laws)
- [OODA adversarial analysis](https://arxiv.org/abs/2203.15502)
- [Agentic AI's OODA Loop Problem (Schneier)](https://www.schneier.com/blog/archives/2025/10/agentic-ais-ooda-loop-problem.html)
- [Partial-Order Planning (CS 540)](https://pages.cs.wisc.edu/~dyer/cs540/notes/pop.html)
- [DAG-Plan](https://arxiv.org/html/2406.09953v1)
- [Separation principle - Wikipedia](https://en.wikipedia.org/wiki/Separation_principle)
- [Separation principle in stochastic control - Wikipedia](https://en.wikipedia.org/wiki/Separation_principle_in_stochastic_control)
- [Separation principle for nonlinear systems](https://www.sciencedirect.com/science/article/pii/S1474667015386572)
- [Separation Principle Redux (Georgiou & Lindquist)](https://arxiv.org/pdf/1103.3005)
- [Boyd OODA Loop - Wikipedia](https://en.wikipedia.org/wiki/OODA_loop)
- [Trust and Reputation Models for MAS (ACM Survey)](https://dl.acm.org/doi/10.1145/2816826)
- [Bayesian Methods for Trust in Multi-Agent Autonomy](https://arxiv.org/abs/2403.16956)
- [Inverse-variance weighting - Wikipedia](https://en.wikipedia.org/wiki/Inverse-variance_weighting)
- [Timescale Separation on Networks](https://www.researchgate.net/publication/281865947_Time-scale_Separation_on_Networks_Tracking_Consensus_and_State-dependent_Interactions)
- [Taxonomy of Hierarchical Multi-Agent Systems](https://arxiv.org/html/2508.12683)
- [Time Scale Separation and Hierarchical Control (Koopman)](https://arxiv.org/html/2506.15586)
- [Code quality metrics: signal vs noise (NDepend)](https://blog.ndepend.com/code-quality-metrics-signal-noise/)
- [Technical Debt and Developer Experience](https://www.networkperspective.io/devex-book/technical-debt-managing-productivity)
- [Cognitive complexity in engineering organizations](https://getdx.com/blog/cognitive-complexity/)
- [R* rule (ecology) - Wikipedia](https://en.wikipedia.org/wiki/R*_rule_(ecology))
- [Regret Analysis: a control perspective](https://arxiv.org/html/2501.04572v2)