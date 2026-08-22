# ACT: Agentic Cycle Theory — Contents

**Working draft.** This is a best-effort outline of the theory's current shape — a map of what we think we know and where the gaps are. The ordering, grouping, and even which claims exist will evolve as the theory develops. Claims will fill in from both directions: general theory pushing toward domain instantiation, and domain-specific results pushing requirements back up. Treat this as a living proof sketch, not a specification.

A first-principles theory of adaptive, purposeful agents under uncertainty.

## How to Read This

Each entry has: **number · slug** — Type, then a one-sentence summary.

**Claim types** (following TFT conventions from TF-00):
- **Axiom**: Tautological or foundational — cannot be derived, only accepted
- **Definition**: Introduces a quantity, object, or notation
- **Scope**: Restricts or broadens the domain under discussion
- **Formulation**: Representational or modeling choice (could be different)
- **Derived**: Logical consequence of prior claims under stated assumptions
- **Theorem**: Formally stated and proved (or proof-sketched)
- **Corollary**: Follows directly from a theorem
- **Hypothesis**: Structurally motivated, needs validation
- **Normative**: Grounded in axioms but requiring a precondition that must be verified
- **Empirical**: Generalization supported by data, not fully derived
- **Observation**: Finding from simulation or empirical investigation
- **Discussion**: Conceptual or normative claim used for interpretation
- **Measurement**: Operationalization of a theoretical quantity
- **Proposed schema**: Mathematical shape identified, formal content pending
- **Gap**: Known missing step — we know something belongs here

**Epistemic tiers** (combining TFT's claim registry with TST's precision):
- **First-principled**: Axiomatic or tautological — cannot be derived, only accepted
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions
- **Empirical**: Supported by data or simulation, not fully derived
- **Discussion-grade**: Argued qualitatively or by analogy, not derived
- **Sketch**: Direction identified but formalization incomplete
- **Gap**: Placeholder — we know the step is needed

Epistemic tiers appear in each segment file's **Epistemic Status** paragraph, not in this contents listing. This listing shows only the claim **type**. When a type label includes a qualifier (e.g., "Hypothesis," "Empirical," "Derived + Discussion"), that is a signal about the claim's epistemic character. Absence of qualifier on a Definition, Axiom, or Scope entry is normal — these are definitional, not truth-claims.

**References** use `#slug-name` tags. Dependencies are mostly sequential;
explicit only when reaching back to non-adjacent claims.

**Numbering** by 10s in general, by 5s within dense sections. The slugs in YAML frontmatter are the stable cross-references — numbers may be renormalized as the structure settles.

---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through observation and action channels, where the environment is not fully observable. This is the general case — thermostats through commanders. The claims in this section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which developed the adaptive-systems foundation that ACT subsumes.*

**010 · temporal-optimality** — Axiom Among agents achieving identical outcomes across all non-temporal dimensions, the one requiring least time is optimal. *(Generalizes TST T-01 beyond software.)*

**020 · agent-environment** — Definition An agent receives observations from an environment, maintains internal state, and produces actions that affect the environment. The agent cannot access the environment directly — observations are necessarily lossy. This is constitutive: the theory applies where the agent-environment boundary entails information loss. *(From TF-01.)*

**030 · observation-function** — Definition Observations are lossy, possibly noisy functions of environment state: o_t = h(Ω_t, a_{t-1}, ε_t). The agent knows neither h nor the noise distribution exactly. *(From TF-01.)*

**040 · action-transition** — Definition Actions affect environment: Ω_{t+1} ~ T(· | Ω_t, a_t). The transition function T is unknown to the agent and possibly stochastic. *(From TF-01.)*

**050 · scope-condition** — Scope ACT applies where: observations exist, the agent has at least binary choice (|A| ≥ 2, the minimum for interventional contrast and causal learning), and residual uncertainty persists: H(Ω_t | C_t) > 0. *(From TF-01.)*

**055 · composition-consistency** — Axiom Any system satisfying the scope condition may be composed of subsystems that themselves satisfy the scope condition. ACT's predictions at the composite level must be compatible with the aggregate of sub-level predictions plus coordination structure. The scope condition does not restrict level of description — the theory applies at every level where it applies at all. This means composition laws for tempo, persistence, gain, and mismatch are *required* for internal consistency, not optional extensions. *(From composition spike §1. The consistency argument is strong — if ACT claims level-independence, predictions at different levels must be non-contradictory. Specific composition laws are sketches; the requirement for their existence is near-derived.)*

**060 · causal-structure** — Axiom The agent-environment interaction has irreducible causal structure. Temporal ordering is constitutive, not incidental. The interaction creates a causal DAG from which associations, interventions, and counterfactuals derive. *(From TF-02, grounded in Pearl.)*

**070 · pearl-causal-hierarchy** — Definition Three levels of causal reasoning: Level 1 (association — "what if I observe?"), Level 2 (intervention — "what if I do?"), Level 3 (counterfactual — "what if I had done differently?"). The binary action requirement ( #scope-condition) ensures Level 2 access. *(From TF-02.)*

**080 · chronica** — Definition The interaction history C_t = (o_1, a_1, ..., o_t) is the complete record of agent-environment interaction. All the agent can ever know derives from this sequence. *(From TF-02.)*

**090 · agent-model** — Formulation M_t = φ(C_t): the agent's compressed representation of how the world works, mapping interaction history to model space M. This is a formulation choice — we commit to analyzing the agent as having a complete state M_t that subsumes all retained information from its history. *(From TF-03.)*

**100 · information-bottleneck** — Formulation Optimal model compression balances retained history against predictive power: φ* = argmin[I(M_t; C_t) − β·I(M_t; o_{t+1:∞} | a_{t:∞})]. The trade-off β depends on environment volatility ρ: volatile → aggressive compression (low β); stable → dense retention (high β). *(From TF-03.)*

**110 · model-sufficiency** — Definition S(M_t) measures what fraction of predictive information the model retains relative to the full history. S = 1 means M_t is a sufficient statistic. S < 1 means predictive information has been lost. *(From TF-03/TF-10.)*

**115 · model-class-fitness** — Definition F(M) = sup_{M ∈ M} S(M). When F(M) < 1 − ε, no model in the current class can adequately represent reality, regardless of parameter tuning. This is the trigger for structural change ( #structural-adaptation-necessity). *(From TF-10.)*

**120 · event-driven-dynamics** — Formulation The primary formulation is event-driven: observations and actions occur as events in continuous time at potentially different and variable rates. Discrete-time notation is the special case of uniform-interval events on a single channel. *(From TF-04.)*

**130 · recursive-update** — Derived Agent state updates must be recursive: M_{τ+} = f_M(M_{τ−}, e_τ). Between events, the model evolves autonomously: dM/dτ = g_M(M_τ). The agent cannot re-derive M_t from scratch at each event — this is computational necessity for finite agents, and architectural choice for others. *(From TF-04.)*

**140 · mismatch-signal** — Definition δ_t = o_t − ô_t: the discrepancy between observation and prediction. This is the fundamental error signal that drives all adaptation. Zero mismatch can mean accurate model, confirmation bias, or high observation noise masking miscomprehension. *(From TF-05.)*

**150 · mismatch-decomposition** — Theorem E[||δ||²] = E[||model_error||²] + E[||obs_noise||²]. Mismatch decomposes into reducible model error (improvable by learning) and irreducible observation noise (a property of the channel). This is Prop 5.1, proven. *(From TF-05.)*

**160 · update-gain** — Empirical Claim η* = U_M / (U_M + U_o): the optimal update weight balances model uncertainty against observation uncertainty. High model uncertainty → trust observations. Low model uncertainty → trust the model. Riccati-optimal gain validated empirically with 52% mismatch reduction. *(From TF-06.)*

**170 · adaptive-tempo** — Definition T = Σ ν^(k) · η*^(k): adaptive tempo is the sum across observation channels of event rate × gain. This measures the agent's total rate of useful information acquisition. *(From TF-06/TF-08.)*

**180 · persistence-condition** — Theorem The agent maintains bounded mismatch (persists) iff T > ρ / ||δ_critical||, where ρ is the rate of environment change and δ_critical is the maximum tolerable mismatch. Robust across all correction functions tested. *(From TF-07, Appendix A.)*

**190 · sector-condition-stability** — Theorem The general nonlinear persistence result: the correction function must satisfy sector bounds with α > ρ/R. This is the Lyapunov/sector-condition framework — more general than the linear ODE, handles arbitrary nonlinear correction functions. Includes adaptive reserve Δρ* = αR − ρ. The linear ODE is a pedagogical special case. *(From Appendix A, promoted to primary.)*

**200 · structural-adaptation-necessity** — Theorem When model class fitness F(M) < 1 − ε, no parametric update closes the mismatch floor. The agent must change its model class (structural adaptation), not just its parameters. Catastrophic breakdown observed at predicted threshold. Prop 10.1, proven. *(From TF-10.)*

---

## II. Actuated Adaptive Systems

*Scope narrowing: agents that not only track reality but aim at something. This adds objectives and strategy alongside the reality model. The adaptive machinery from Section I carries over unchanged ( #directed-separation) — what we add is the goal-directed layer.*

*The derivation chain for this section is mature (see `scratch/spike-v3-purposeful-agent.md`). Most of it provides better justification and epistemic labels for architecture that already existed. The genuinely novel results are: the satisfaction gap / control regret split (§270– 275), the G_t complexity bound (in §285), and the graph structure uniqueness argument (see `scratch/spike-graph-uniqueness.md`).*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*

**210 · agent-spectrum** — Definition Two independent dimensions create an agent spectrum: {±model} × {±objective}. Four quadrants: reactive system (thermostat), adaptive tracker (Kalman filter), blind pursuer (PID controller), actuated agent (commander, developer, AI agent). These are regions of a continuum, not discrete categories.

**215 · complete-agent-state** — Formulation X_t = (M_t, G_t): the complete agent state lifts M_t from "the" state (as in TFT) to the epistemic substate, adding G_t (the purposeful substate — what the agent wants and how it plans to get it). Section I is the special case X_t = (M_t, ∅). Update dynamics: f_M has no G_t argument; f_G references M_{τ+}; policy couples all three. *(From v3 spike §1.)*

**220 · objective-functional** — Definition O_t parametrizes TF-08's "value" term: given objective O_t, the induced value functional V_{O_t}: trajectories → ℝ measures how well a trajectory satisfies the objective. O_t can be a point target, region, constraint set, utility, or trajectory functional — all unified through V_{O_t}. The trajectory functional is the most general form; the others are special cases. *(From v3 spike §2.)*

**225 · value-object** — Definition V_O(M_t, π; N_h) and Q_O(M_t, a; π_cont, N_h): horizon- and policy-conditioned value objects. Continuation policy π_cont is a parameter, not derived. Common choices: one-step improvement (natural default), Bellman fixed point, receding horizon. λ depends on (M_t, O_t, N_h) — exploration price depends on objective and horizon, not just epistemic state. *(From v3 spike §2.2.)*

**230 · strategy-dimension** — Definition G_t = (O_t, Σ_t): the purposeful substate decomposes into objective (evaluation criterion — "is this trajectory satisfactory?") and strategy (action guidance — "which action sequence produces a satisfactory trajectory?"). This is a definitional split reflecting different kinds of information, not a dynamic or timescale claim. Strategy representations range from none (reactive), through cached policies, subgoal sequences, to full causal DAGs. *(From v3 spike §3.)*

**235 · causal-hierarchy-requirement** — Derived + Scope Evaluating Q_O(M_t, a; ·) is a Level 2 query ("what happens if I *do* a?"). The causal hierarchy theorem (Bareinboim et al. 2022) proves Level 2 knowledge requires causal structure beyond predictive models. *Scope narrowing*: we restrict to agents that must acquire or refine Level 2 knowledge during operation, as opposed to pre-compiled controllers (PID, LQR) where the designer supplied it. *(From v3 spike §4.)*

**240 · loop-interventional-access** — Derived An agent in the feedback loop generates interventional data: a_t causally precedes o_{t+1}, so the mismatch δ_t conditioned on a_t carries interventional information. The loop provides *access* to Level 2 data; whether the agent *exploits* it depends on its update mechanism and model class. LLM training data provides causal priors (noisy, mixed provenance); the loop verifies. *(From TF-02 + temporal ordering; v3 spike §4.3.)*

**245 · explicit-strategy-condition** — Normative An agent benefits from explicit Σ_t when C_plan + C_maintain < C_explore + C_repair. Labeled *normative*, not *derived*, because #temporal-optimality requires identical non-temporal outcomes as a precondition — loop-based and model-based approaches may differ in final value, risk, and model bias. When the precondition holds, this makes #temporal-optimality load-bearing for the purposeful layer. *(From v3 spike §5.)*

**250 · chain-confidence-decay** — Derived log P(chain) = Σ log P(E_i | E_{<i}): chain confidence decays monotonically with depth. The robust result is additive log-confidence, not the special case p^n (which assumes independence and uniformity). Longer chains are structurally less confident, creating pressure toward short plans, parallel fallback paths, high-confidence critical links, and early failure monitoring. *(From v3 spike §6.1. Generalizes the earlier compound-probability-decay result.)*

**255 · and-or-scope** — Scope We restrict to environments where causal combination is approximately conjunctive (AND) or disjunctive (OR), without strong interaction effects. Converged across three independent formalism attempts. The excluded case (complementarity, substitutability, interaction effects) requires richer combination rules — a legitimate divergence point for future work. *(From v3 spike §6.2.)*

**260 · strategy-dag** — Definition Post-narrowing: the agent's strategy Σ_t = (V, E, p, γ) is a probabilistic causal DAG. Nodes are propositions; edges carry confidence weights p ∈ [0,1]; combination rules γ(v) ∈ {AND, OR}. *Graph structure is strongly motivated*: temporal ordering → directed edges (proved), Cox's theorem → probabilistic uncertainty (proved), local revisability → Markov factorization (sketch — needs tightening), finite horizon → acyclicity (derived, resolves a former known fragility). The AND/OR parameterization is a formulation choice within the forced graph structure, motivated by Boolean completeness + parsimony under bounded cognition. *(From intent-dag-consolidated + graph uniqueness spike.)*

**265 · directed-separation** — Derived + Scope f_M has no G_t argument; f_G references M_{τ+}. The epistemic update is goal-blind *conditional on the realized event*. The policy couples all substates through action selection. *Scope condition*: this requires that goals influence event *selection* (through action) but not event *processing*. Many agents (including LLMs with goal-conditioned prompts) violate this to some degree. The approximation is better when goal-conditioning affects attention more than interpretation, and worse when the agent exhibits confirmation bias. A future extension: coupled M_t/G_t dynamics formalizing motivated reasoning. *(From v3 spike §8.)*

**270 · satisfaction-gap** — Definition δ_sat = V_{O_t}^min − A_O(M_t; Π, N_h): the gap between the minimum acceptable value and the best achievable under current model, policy class, and horizon. δ_sat > 0 means the objective is unmet, but this does NOT automatically mean the goal is wrong — it may indicate narrow Π, short N_h, or incorrect M_t. The revised cascade checks M_t, Π, N_h adequacy *before* revising O_t. Objective revision is last resort. *(From v3 spike §7.3. Replaces the simpler "δ_objective" from earlier formulations.)*

**275 · control-regret** — Definition δ_regret = A_O(M_t; Π, N_h) − V_O(M_t, π_current; N_h) ≥ 0: the gap between best achievable and current performance. This is the signal for Σ_t revision. *Diagnostic*: large δ_sat + small δ_regret = doing the best possible but goal may be infeasible → check M_t/Π/N_h then consider revising O_t. Large δ_sat + large δ_regret = bad strategy → revise Σ_t first. *(From v3 spike §7.4.)*

**280 · strategic-calibration** — Definition Edge residuals r_ij: predicted ΔV_O − observed ΔV_O per edge traversal. δ_strategic = (Σ w_ij · r_ij²)^{1/2}, aggregated across active edges with criticality weighting. This is a second-order inference — inherently slower to evaluate than δ_epistemic, requires accumulating evidence over multiple edge traversals. Connects to the persistence schema ( #strategy-persistence-schema) as the candidate strategic mismatch state. *(From v3 spike §7.5.)*

**285 · orient-cascade** — Derived Resolution ordering forced by information dependency: (1) reduce δ_epistemic (prerequisite — M_t appears in every subsequent formula), (2) evaluate δ_sat (requires adequate M_t), (3) evaluate δ_regret (requires adequate M_t + meaningful A_O), (4) evaluate δ_strategic (requires feasible O_t + evidence of suboptimal execution), (5) revise O_t (last resort, after Σ_t revisions exhaust). *G_t evaluable complexity bounded by M_t capacity*: an agent with poor S(M_t) cannot meaningfully evaluate a complex Σ_t. This creates virtuous/vicious cycles at the purposeful level. *(From v3 spike §7.6.)*

**290 · observability-dominance** — Derived Unobservable edges freeze beliefs — the agent cannot update confidence on what it cannot see. Strategy effectiveness is gated by which edges the agent can observe. Observability enables strategy; its absence disables it, regardless of the strategy's structural quality. *(From intent-dag-consolidated.)*

**295 · edge-update-via-gain** — Hypothesis Strategy edges update via the same uncertainty ratio principle: η_edge = U_edge / (U_edge + U_obs). TFT's gain machinery ( #update-gain) extends to strategy revision. *Parallel to M_t gain but not independently validated.* *(From intent-dag-consolidated.)*

**300 · structural-change-as-parametric-limit** — Formulation In the probabilistic DAG, pruning (edge → 0) and grafting (0 → edge) are continuous operations on edge weights, not discrete structural events. TF-10's destruction-creation cycle is the rare limiting case. *(From intent-dag- consolidated, converged.)*

**305 · strategy-persistence-schema** — Proposed schema If strategic update dynamics satisfy sector conditions analogous to
#sector-condition-stability — (SA1) zero correction at zero strategic mismatch,
(SA2') local sector bound on strategic correction, bounded strategic disturbance — then Σ_t persists iff α_Σ > ρ_Σ / R_Σ. Awaiting: formal strategic mismatch state (candidate: #strategic-calibration residual), correction function (edge confidence revision via gain), disturbance characterization (rate at which environment invalidates causal links). *(From v3 spike §9.)*

**310 · ???** — Gap *Action-deliberation-exploration tradeoff. Three-way: exploit (pursue O_t via Σ_t), explore (improve M_t), deliberate (revise Σ_t). How does the agent allocate? TF-07/08/09 treat explore/exploit for M_t; adding Σ_t creates a richer tradeoff. Connects to CIY (TF-09) and the exploration price λ.*

**315 · ???** — Gap *Strategy tempo. The analog of #adaptive-tempo for Σ_t updates. What observation channels contribute to strategy revision? How fast must the agent revise Σ_t to maintain strategy persistence ( #strategy-persistence-schema)?*

**320 · ???** — Gap *Cognitive cost of Σ_t. The IB analog for strategy maintenance: a 500-node DAG is qualitatively different from a 12-node one. For finite-context agents, the DAG must fit in working memory. Connects to #information-bottleneck, shared intent compression ( #shared-intent), and the cost inequality ( #explicit-strategy- condition) — part of C_maintain is cognitive cost.*

**325 · ???** — Gap *Edge identifiability. Edges claim interventional semantics (p_ij = P(j | do(i), M_t)) but update from observational signals. In confounded domains (military, organizational), this is a real causal-identification problem. In software, genuine interventions (tests, deploys, git bisect) are available. Resolution may come from the software domain pushing requirements back up.*

---

## III. Composition and Coordination

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition axiom ( #composition-consistency) ensures the theory applies at every level of description; this section develops what happens when composition is imperfect and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Two sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations), and the composition spike (`scratch/spike-agent-composition.md`) which derives the requirement for composition consistency from the scope condition's level-independence.*

**400 · multi-agent-scope** — Scope Multiple agents interact through shared environment. Each agent has its own X_t = (M_t, G_t) state. Observations may be correlated. Agents may be cooperative, adversarial, or mixed — positions on a continuous spectrum, not discrete categories. A composite agent A_c satisfies the scope condition and can be analyzed as a single agent at a higher level ( #composition-consistency). *(From TF-11/Appendix F, extended by composition spike.)*

**405 · unity-dimensions** — Definition (sketch) Four substantially independent dimensions characterize a composite agent's internal coherence: epistemic unity U_M (shared model), teleological unity U_O (shared objective), strategic unity U_Σ (coordinated action), perceptual unity U_obs (shared observation). These map to Clausewitz's three gaps (Bungay): knowledge gap ↔ 1 − U_M, alignment gap ↔ 1 − U_O, effects gap ↔ (1 − U_Σ)(1 − U_obs). *(From composition spike §3–4. Unity metrics are discussion-grade; Clausewitz mapping is hypothesis.)*

**410 · shared-intent** — Definition + Discussion (sketch) IB-compressed purpose communicated between agents for coordinated action. The Auftragstaktik insight: communicate *enough* intent to enable local adaptation, not so much that you constrain it. The information bottleneck principle ( #information-bottleneck) applied to inter-agent purpose rather than intra-agent compression. *(From intent-dag-consolidated.)*

**415 · auftragstaktik-principle** — Hypothesis Optimal allocation of communication bandwidth across unity dimensions prioritizes teleological unity (B_O) over strategic coordination (B_Σ) over model sharing (B_M). The IB framework predicts this when objectives change slowly, strategies moderately, and models fast. *(From composition spike §4, grounded in Bungay's analysis of military history.)*

**420 · tempo-composition** — Derived (sketch) Under perfect communication and independent channels, tempos add: T_c = Σ T_i. With overlapping channels, diminishing returns. Communication overhead subtracts: T_c = Σ T_i^local + Σ T_{i→j}^shared − C_coord. The composition gap ΔT = Σ T_i − T_c ≥ 0 measures the cost of being multiple. *(From composition spike §2.3.)*

**425 · team-persistence** — Derived (sketch) A team of sub-agents, each below individual persistence threshold, persists as a composite when Σ T_i − C_coord > ρ_c / ||δ_critical^c||. Coordination overhead C_coord directly subtracts from composite persistence margin — a team with high individual tempos but terrible coordination can fall below the threshold. *(From composition spike §2.4.)*

**430 · adversarial-tempo-advantage** — Theorem Tempo advantage is superlinear: the ratio of adversarial mismatch scales as (T_A/T_B)^α where α > 1 in all coupling-dominant regimes. Faster adaptation doesn't just help linearly — it compounds. This is the formal grounding of Boyd's OODA loop insight. *(From TF-11, validated across 6 simulation variants.)*

**435 · adversarial-destabilization** — Derived If adversary A injects disturbance into agent B's environment (ρ_B = ρ_{B,base} + γ_A · T_A), A destabilizes B when γ_A · T_A > Δρ*_B (adaptive reserve, #sector-condition-stability). Formally defines "getting inside the opponent's loop" as Lyapunov instability. Once B exceeds its invariant region, erratic actions increase A's coupling effectiveness in a positive-feedback loop. *(Derived from sector-condition analysis applied to adversarial coupling.)*

**440 · adversarial-exponent-regimes** — Observation The exponent α depends on the disturbance mechanism: α = 2 under deterministic drift (coupling-dominant); α = 3/2 under stochastic disturbances; α ≈ 1 when coupling doesn't dominate base noise. The linear ODE is correct in the deterministic regime; the stochastic regime needs separate treatment. *(From simulation variants C/D.)*

**450 · observation-gates-advantage** — Observation Observation noise (U_o) collapses adversarial exponent from ~1.0 to ~0.2. Optimal gain ( #update-gain) partially restores it to ~0.4. Formally grounds Boyd's emphasis on Orient quality over raw OODA speed — a fast agent with bad observations loses most of its advantage. *(From simulation variant E.)*

**460 · per-dimension-persistence** — Theorem Scalar tempo is a poor summary for anisotropic systems (72% overestimate in simulation). The per-dimension persistence condition is exact: T_k > ρ_k / δ_critical_k for each dimension k. The weak dimension is the bottleneck (84% of total mismatch). Targeted adversarial attack on the weak dimension amplifies advantage by 17%. *(From simulation variant F.)*

**470 · ???** — Gap *Adversarial DAG targeting. Which strategy edges are most valuable to attack? Centrality in the DAG, inter-agent coupling edges, edges observable to the adversary. #chain-confidence-decay as a weapon: disrupting one AND-edge in a deep chain collapses the whole path.* *(From track-a/04.)*

**475 · ???** — Gap *Directed separation at the composite level. If each sub-agent's f_M is G_t-independent, is the composite's f_M^c independent of G_t^c? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent.* *(From composition spike §2.5.)*

**480 · ???** — Gap *Minimum unity for meaningful composition. At what point is a "composite agent" a useful fiction vs a genuine entity? Is there a phase transition or continuous degradation? What is the irreducible cost of being multiple (compositional entropy)?* *(From composition spike §7.)*

---

## IV. Evolving Software Systems

*Domain instantiation: software development as an ACT domain. This section re-grounds TST (Temporal Software Theory) in ACT's formal machinery — adding the causal mathematics and adaptive dynamics that TST was developed without. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.*

*The temporal optimality axiom ( #temporal-optimality) now has full backing:
tempo advantage ( #adversarial-tempo-advantage), persistence conditions ( #persistence-condition), and gain dynamics ( #update-gain) explain WHY time-optimal development practices work, not just THAT they do.*

**500 · software-scope** — Scope ACT's software domain applies to systems with non-negligible future change probability: P(n_future > 0) > ε. For such systems, total lifetime cost dominates initial implementation cost. Stable subsystems with P(change) < ε operate at "infinite velocity" — consuming zero future time. *(Regrounding TST T-03 in ACT.)*

**510 · software-epistemic-properties** — Observation Software has six unique epistemic properties: (1) fully inspectable environment — partial observability from cognitive bandwidth, not physics; (2) Level 3 counterfactuals executable via git; (3) causal DAG partially explicit — imports, types, dependencies; (4) history perfectly recorded — git as complete chronica; (5) multi-agent through shared versioned artifact; (6) observation channel quality under agent control — code quality IS observation infrastructure. *(From via-tft.)*

**520 · feature-definition** — Definition A unit of functionality that coherently changes the codebase and/or running system, as perceived by those who requested, implement, or use it. Includes refactoring (alters future implementation time), excludes true no-ops. *(TST D-01.)*

**530 · specification-bound** — Theorem time_min(F) ≥ time_specify(F, context). You cannot implement what you cannot specify. Information-theoretic necessity: Shannon entropy of the feature specification bounds implementation time below, modulated by shared context between specifier and implementer. As AI approaches instant implementation, software engineering becomes specification engineering. *(TST T-02. One of TST's strongest claims.)*

**535 · communication-as-bottleneck** — Corollary As implementation time approaches the specification bound, communication speed and quality become the limiting factor. *(TST C-02.1.)*

**540 · change-expectation-baseline** — Theorem E[n_future | n_past] = n_past. The Bayesian consequence of maximum ignorance (Jeffrey's prior, scale-invariant). Not a heuristic — the mathematical null hypothesis of temporal prediction. Any deviation requires information that justifies it. Creates intellectual accountability for abstraction decisions. *(TST T-04. Genuinely well-grounded.)*

**545 · investment-scaling** — Corollary Abstraction investment should scale with n_past. Systems with n_past < 3 warrant minimal structural investment. *(TST C-04.1.)*

**550 · developer-as-act-agent** — Definition The developer's M_t = codebase understanding (mental model of architecture, dependencies, conventions, state). O_t = task objective ("implement OAuth," "fix the race condition"). Σ_t = implementation strategy (the plan, with AND/OR structure, observable checkpoints, contingency branches). *(From ACT-03 software section.)*

**560 · comprehension-time** — Definition Time from initial idea to first surviving change. Reading, understanding, discovering hidden dependencies, building and validating mental model. This is the cost of constructing M_t for the relevant portion of the codebase. *(TST D-02.)*

**565 · implementation-time** — Definition Time from first change to complete feature. Writing, testing, addressing immediate issues. *(TST D-03.)*

**570 · dual-optimization** — Derived Principled decisions minimize both comprehension time and implementation time for future features. Under high turnover (especially 100% context turnover per AI instance), comprehension cost compounds across every new reader. *(TST T-05, derived from #temporal-optimality + #change-expectation-baseline. The claim that comprehension dominates under high turnover is structurally motivated but the quantitative relationship needs formalization.)*

**580 · change-investment** — Derived Accept X extra minutes now to save Y per future change when X < n_future × Y. The threshold form is derived from #temporal-optimality + #change-expectation- baseline. *(TST T-06. TST also claims that principled implementation "often costs nearly the same" as quick implementation — this is an empirical observation, not derived from the formalism.)*

**590 · code-quality-as-observation-infrastructure** — Discussion + Hypothesis Past actions (writing code) affect future observation quality (reading code). Well-written code has low U_o for future readers; obfuscated code has high U_o. This creates a second-order feedback loop: code quality → U_o → η* ( #update-gain) → T ( #adaptive-tempo) → slack → code quality. *[Plausible]* The structural argument is sound — code quality does affect comprehension, and comprehension does affect effective tempo. Whether this is distinctive to software or an instance of a more general pattern (agents modifying their own observation channels) is an open question. The quantitative claim that
#persistence-condition formalizes the virtuous/vicious threshold requires
formalizing "code complexity accumulation rate" as ρ. *(From via-tft mapping.)*

**600 · conceptual-alignment** — Hypothesis time_comprehension ∝ 1/alignment(code, domain). Misalignment (code says "user_score," domain says "reputation") taxes every future comprehension. Not just naming — module boundaries, relationship structure, abstraction levels. *(TST T-07.)*

**605 · realignment-as-feature** — Corollary — Derived As domain understanding evolves, realigning code is a principled investment when T_align < n_future × Δt_comprehension. This isn't cleanup — it's temporal optimization with measurable ROI. *(TST C-07.1.)*

**610 · atomic-changeset** — Definition The diff between codebase states before and after feature implementation, excluding generated artifacts. Crosses architectural boundaries: source, schema, config, tests, infrastructure, documentation. If it must change to deliver the feature, it's part of the changeset. *(TST D-04.)*

**620 · changeset-size-principle** — Empirical — Hypothesis time_implementation(F) ∝ |changeset(F)|. Nearly tautological (more changes take more time), but reveals that good architecture minimizes FUTURE changeset sizes. The proportionality constant is unvalidated. *(TST T-08.)*

**625 · comprehension-follows-changeset** — Corollary + Hypothesis Understanding a feature that touched 20 files requires comprehending 20 contexts. Double the changeset ≈ double the comprehension burden. Creates double penalty for unnecessarily large changesets. *(TST C-08.1.)*

**630 · change-distance** — Definition Distance between changes in a codebase: lexical < file < module < service. *(TST D-05.)*

**640 · change-proximity-principle** — Derived + Hypothesis Given identical changeset sizes, closer changes require less implementation time. Explains why modules group co-changing code, layers localize changes, domain boundaries contain related changes. *(TST T-09.)*

**645 · exponential-cognitive-load** — Hypothesis time_actual = time_baseline × k^discontinuities, where k > 1. If context- switching compounds multiplicatively, even modest k (1.1–1.2) creates substantial differences across many discontinuities. Requires empirical validation — the actual relationship may be linear or sub-exponential. *(TST H-09.1.)*

**650 · system-coupling** — Definition coupling(module_i, module_j) = P(change(module_j) | change(module_i)). *(TST D-06.)*

**655 · system-coherence** — Definition coherence(module) = E[proximity(changes within module)]. *(TST D-07.)*

**660 · coherence-coupling-measurement** — Measurement quality = Σ coherence / Σ coupling. Computable from git history. Transforms architectural discussions from opinion to empirical observation. Requires sufficient history, stable boundaries, representative feature distribution. *(TST T-10.)*

**670 · principled-decision-integration** — Integration C* = argmin E[T|C] where expected time integrates across future features, weighting comprehension ( #conceptual-alignment), changeset size ( #changeset- size-principle), and proximity ( #change-proximity-principle). Perfect optimization is impossible (requires knowing all future features), but the framework structures the decision space and makes tradeoffs explicit. *(TST T-11.)*

**680 · system-availability** — Definition availability = MTTF / (MTTF + MTTR). *(TST D-08.)*

**685 · continuous-operation** — Scope Extension For operational systems: T_effective = T_implementation + P(failure) × T_recovery. A non-operational system has infinite implementation time from the user's perspective. Fault-tolerant design (accept failure, minimize recovery) can be time-optimal vs defensive programming (prevent failure, complex recovery). Explains supervision trees, circuit breakers, bulkheads, health checks. *(TST T-12.)*

**690 · causal-discovery-from-git** — Principle — Plausible Git provides temporal ordering + interventional data (every commit is an intervention). Proper causal analysis — not just co-change correlation — is possible. Software is in Pearl's Regime A (randomized interventions) for causal discovery. The gap between declared dependencies and empirical causal structure reveals hidden coupling or stable interfaces. *(From via-tft causal-extensions.)*

**695 · ???** — Gap *Three-part tempo decomposition for software: T_obs (compiler, linter, tests) + T_explore (code reading, navigation) + T_probe (test runs, staging). Which component is the bottleneck? How does each connect to code quality as observation infrastructure ( #code-quality-as-observation-infrastructure)?*

**698 · ???** — Gap *Software persistence condition: the unmaintainability threshold formalized. T_team > ρ_total / ||δ_critical||. When does a codebase cross from maintainable to unmaintainable? What are the observable precursors? How does this connect to the virtuous/vicious cycle ( #code-quality-as-observation-infrastructure)?*

---

## V. Software-Grounded Agentic Systems

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory → software domain → agents that embody ACT. This is where the 100% context turnover problem, M_t preservation, and the cognitive loop connect the theory back to the systems being built with it.*

**700 · ai-agent-as-act-agent** — Definition An AI coding agent is an actuated adaptive agent with 100% context turnover per session. It inhabits the actuated quadrant ( #agent-spectrum): it has M_t (context window + retrieved memory), O_t (task objective), and Σ_t (approach plan). *(From via-tft mapping, agentic-tft.)*

**710 · context-turnover** — Observation M_t resets to near-zero at session start. Not gradual degradation but catastrophic loss. The agent must reconstruct M_t from the environment (codebase, CLAUDE.md, memory files) at each session. This is fundamentally different from human developers who retain M_t across sessions. In composition terms ( #composition-consistency), this is an epistemic unity problem: each session starts with U_M ≈ 0 relative to previous sessions. *(From via-tft mapping.)*

**720 · m-preservation** — Discussion External memory (CLAUDE.md, memory directories, well-structured code) converts ephemeral M_t into persistent environmental state. The agent's past actions modify the environment to make future M_t reconstruction faster. This is
#code-quality-as-observation-infrastructure applied to agent infrastructure
itself. *(From via-tft mapping.)*

**730 · ???** — Gap *Cognitive loop formalization. The cycle: read environment → construct M_t → form/revise Σ_t → select action → observe result → update M_t. How does this differ from the generic orient cascade ( #orient-cascade)? What's specific to language-based agents? Agentic-tft docs 10-14 have substantial thinking on this.* *(From agentic-tft.)*

**740 · ???** — Gap *Evaluation framework. How do you measure an AI agent's ACT quantities? M_t quality (can the agent predict what it will find?), Σ_t quality (does the plan lead to O_t?), tempo (how fast does the agent acquire useful information?). Connects to crèche and training design.* *(From agentic-tft.)*

**750 · ???** — Gap *Crèche concept. Experiential training environments where agents develop their adaptive capacity. What does an ACT-grounded training regime look like? How do you train for good M_t construction, effective Σ_t formation, appropriate gain calibration?* *(From agentic-tft.)*

**760 · ???** — Gap *The recursive completion. An agent using ACT to guide its own behavior while operating on a codebase that implements ACT. Self-referential but not paradoxical — the agent's understanding of tempo, persistence, and gain directly informs its development decisions. What does this look like in practice?*

---

## Appendices (Evidence & Reference)

*These support specific claims above with detailed evidence, worked examples, or historical development.*

**A · linear-ode-approximation** — Reference The linear ODE from TF-11: dδ/dt = ρ − T·g(δ). Correct for deterministic drift in continuous time. Pedagogically valuable, not the general case. The sector- condition framework ( #sector-condition-stability) is primary. *(From TF-11, demoted.)*

**B · simulation-results** — Evidence Six simulation variants validating and refining claims from Sections I–III. Variant A/B: deterministic drift confirms α = 2. Variant C/D: stochastic gives α = 1.5. Variant E: observation noise gates advantage. Variant F: per-dimension persistence exact. *(From track-b-nonlinear-sims.)*

**C · worked-examples** — Reference Kalman filter (M_t only), PID controller (O_t only), LQG (M_t + O_t without explicit Σ_t), RL agent (full triple), developer (software domain).

**D · intent-dag-development** — Historical Three independent formalism attempts converging on AND/OR + single-parameter edges. Documents the convergence testing and what was settled vs open. *(From track-a-intent-dag/ and 04-intent-dag-consolidated.md.)*

**E · prior-art-positioning** — Reference Assessment of Hafez (bi-predictability P — complementary diagnostic, no goals/dynamics; H_b has no ACT analog yet), IBM 2025 (calls for what ACT provides; their open challenges directly addressed by ACT), BDI (named the parts, no dynamics), active inference (closest competitor, different foundation). *(From scratch/02-prior-art-assessment.md.)*

**F · graph-structure-uniqueness** — Research direction Four axioms (directed temporal ordering, probabilistic uncertainty, state-local revisability, observable intermediates) strongly motivate DAG structure for strategy representation. Acyclicity is *derived* from temporal ordering over finite planning horizon (resolves former known fragility). P3→Markov step is a sketch (local revisability may be achievable by other sparse factorizations). AND/OR parameterization follows from Boolean completeness + parsimony (hypothesis for binary outcomes). *(From scratch/spike-graph-uniqueness.md.)*

---

## Dependency Summary

The claim graph is mostly sequential, but key non-local dependencies include:

- **#update-gain** is used throughout: in M_t updates (Section I), Σ_t edge updates ( #edge-update-via-gain), observation-quality analysis ( #observation-gates-advantage, #code-quality-as-observation-infrastructure), and the policy objective's exploration-exploitation term

- **#persistence-condition** grounds both M_t persistence (Section I), strategy persistence ( #strategy-persistence-schema), software maintainability ( #code-quality-as-observation-infrastructure), team resilience ( #team-persistence), and adversarial destabilization ( #adversarial-destabilization)

- **#temporal-optimality** is the optimization criterion that everything serves:
  it motivates adaptive tempo (Section I), grounds the explicit strategy condition ( #explicit-strategy-condition), grounds TST's practical claims (Section IV), and explains why adversarial dynamics are superlinear (Section III)

- **#information-bottleneck** applies to M_t compression (Section I), shared intent compression ( #shared-intent), cognitive cost of Σ_t (#320), and the Auftragstaktik communication principle ( #auftragstaktik-principle)

- **#composition-consistency** (Section I) is the foundation for all of Section III. Tempo composition, team persistence, and adversarial dynamics are all instances of the composition principle applied at different points on the unity spectrum

- The software domain (Section IV) both *applies* the general theory AND *pushes requirements back up* — e.g., #code-quality-as-observation- infrastructure reveals a feedback loop that the general theory should accommodate, and edge identifiability (#325) is resolved in software but not in general

- **#satisfaction-gap + #control-regret** (the split of the old δ_objective) are load-bearing for the orient cascade ( #orient-cascade) — without this split, the cascade cannot distinguish infeasible goals from bad strategies
