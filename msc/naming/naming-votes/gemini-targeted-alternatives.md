# Targeted Alternatives Generation

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---|---|
| `effects spiral` | `runaway mismatch cascade` | add-alias | +3 | Focuses on the mismatch acceleration ($\Vert\delta\Vert \uparrow$). Connects to "cascade" seen elsewhere (e.g. orient cascade). |
| `effects spiral` | `adversarial feedback loop` | rename | +2 | Explicitly names the cause (adversarial coupling) and the mechanism (positive feedback). |
| `effects spiral` | `destabilization vortex` | rename | +1 | A bit more descriptive than spiral but slightly less formal. |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `empty feasibility window` | canonicalize | +3 | The text specifically defines this as the "empty window limit" of the stability-plasticity window. This grounds it in AAD math rather than an ML imported term. [original phrasing: catastrophic forgetting regime] |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `plasticity-bound failure` | rename | +2 | Emphasizes that the bounds of the window are failing. [original phrasing: catastrophic forgetting regime] |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `stability-plasticity collapse` | rename | +2 | Focuses on the two constraints crashing into each other. [original phrasing: catastrophic forgetting regime] |
| `blind pursuer` | `model-degenerate pursuer` | rename | +2 | The text clarifies $M_t$ is absent or degenerate. "Model-degenerate" is more formal than "blind". |
| `blind pursuer` | `reality-blind agent` | rename | +1 | Directly contrasts with reality tracking, but maybe too stylized. |
| `adaptive tracker` | `pure epistemic agent` | add-alias | +3 | It builds reality models without objectives. "Epistemic" links it cleanly to the epistemic update $f_M$. |
| `adaptive tracker` | `objective-free tracker` | rename | +2 | Contrasts explicitly with actuated agents having objectives. |
| `agent identity as one non forkable causal record` | `singular trajectory commitment` | canonicalize | +3 | Perfectly describes the axiom that identity equals a single, non-forkable causal path. |
| `agent identity as one non forkable causal record` | `trajectory-bound identity` | rename | +2 | Shorter, very usable alias for the same concept. |
| `goal-blind routing` | `objective-agnostic topology` | rename | +2 | "Topology" covers the routing structure aspect well. |
| `goal-blind routing` | `content-neutral routing` | rename | +1 | Less specific than objective-agnostic. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `epistemic gain collapse` | canonicalize | +3 | Already heavily referenced as "gain collapse". Adding "epistemic" clarifies it's the update gain dropping to near 0. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty] |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `update calcification` | add-alias | +2 | Good prose handle for the failure mode where the model stops taking in new info. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty] |
| `turnover multiplier` | `comprehension compounding tax` | rename | +2 | Explicitly connects it to the comprehension time dominating the dual optimization. |
| `turnover multiplier` | `multi-agent continuity tax` | rename | +1 | Highlights the issue comes from agent transitions/turnover. |
| `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]` | `privileged grounding domain` | rename | +3 | Describes exactly what software is for AAD: the domain where formal properties are cleanly grounded without extra transfer assumptions. [original phrasing: calibration laboratory] |
| `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]` | `high-identifiability testbed` | rename | +2 | Captures the "high-identifiability" empirical claim perfectly. [original phrasing: calibration laboratory] |
| `triple depth penalty` | `depth-gated decay triad` | rename | +2 | "Gating" is the mechanism (evidence starvation), "decay" is the confidence drop. |
| `triple depth penalty` | `tripartite chain attenuation` | rename | +1 | A bit dry, but accurate to the 3 compounding penalties. |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | canonicalize | +3 | Strong prose phrase. Better than generic "unobservable" since it focuses on the epistemic failure to track it. [original phrasing: unobservable strategy subgraph] |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `feedback-starved branch` | rename | +2 | Explains the consequence. [original phrasing: unobservable strategy subgraph] |
| `tests as reusable interventions` | `interventional probe library` | add-alias | +3 | Connects tests to "Level-2 interventions" effectively and explicitly. |
| `tests as reusable interventions` | `causal query infrastructure` | rename | +2 | Emphasizes that tests answer active causal queries, not just passive checks. |
| `class 1 class 2 class 3` | `goal-entanglement hierarchy` | rename | +3 | Directly describes what the classes measure (how much $G_t$ entangles with $M_t$ updates). |
| `class 1 class 2 class 3` | `modularity partition` | rename | +2 | Classes are precisely modular, partially modular, and merged. |
| `a2 prime sub scope partition` | `sector-bounded operating region` | rename | +2 | Makes the a2 prime sub-scope meaningful in prose. |
| `a2 prime sub scope partition` | `sector condition scope` | add-alias | +3 | A plain English explanation of the $\alpha_2$ partition. |
| `evidence starvation` | `depth-attenuated correction` | add-alias | +2 | Describes the mathematical mechanism (effective observation rate dropping geometrically). |
| `evidence starvation` | `downstream evidence gating` | rename | +2 | Captures the AND-chain gating effect. |
| `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]` | `latent adaptive capacity` | canonicalize | +3 | Describes capacity that isn't currently used but is preserved. [original phrasing: dormant structural variation that becomes useful after regime change] |
| `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]` | `exaptive reserve` | rename | +2 | "Exaptive" specifically means an adaptation used for a new purpose, fitting the regime change requirement perfectly. [original phrasing: dormant structural variation that becomes useful after regime change] |
| `class 1 subagents forming a class 3 composite` | `strategic composition entanglement` | rename | +3 | Captures that composing modular agents strategically creates a coupled Class 3 composite through cross-agent modeling. |
| `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]` | `terminal alignment gap` | canonicalize | +3 | Gap pairs nicely with satisfaction gap, and fits the terminology. [original phrasing: terminal alignment error] |
| `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]` | `objective misspecification` | rename | +2 | Explicitly names the cause: the operational criteria didn't match the true objective. [original phrasing: terminal alignment error] |
| `control regret` | `control regret` | keep | +3 | Perfect partner to satisfaction gap. Captures the specific decision-theoretic regret tied to strategy revision. |
| `control regret` | `strategy opportunity cost` | rename | -1 | A bit too generic economics terminology; "regret" explicitly ties to the mathematical formulation. |
| `satisfaction gap` | `satisfaction gap` | keep | +3 | Crispest named pair along with control regret. Essential diagnostic dimension. |
| `satisfaction gap` | `attainability shortfall` | rename | -1 | "Satisfaction gap" explicitly ties into $V_O^{\min}$ being met. "Attainability" might refer only to $A_O$. |
| `unnamed deliberate expenditure of tempo to convert a hidden node into an observable one` | `observability investment` | canonicalize | +3 | Already well-integrated into the text. Accurately describes the economic tradeoff (spending tempo to buy monitoring). |
| `unnamed deliberate expenditure of tempo to convert a hidden node into an observable one` | `epistemic instrumenting` | rename | +2 | Captures the physical action of adding a sensor/monitor to the node. |
| `context wiping at session boundaries` | `the epistemic severance` | add-alias | +3 | Visceral name for the specific loss of continuity LLMs suffer, distinct from general "context turnover". |
| `context wiping at session boundaries` | `context turnover discontinuity` | canonicalize | +2 | Ties directly to the "obs-context-turnover" phrasing. |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `reconstruction relay` | add-alias | +2 | Highlights the relay race nature of state across session boundaries. [original phrasing: managing memory across session boundaries to prevent the sufficiency discontinuity] |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `artificial hippocampus` | canonicalize | +3 | Specifically maps to the biological analog of cross-episode memory consolidation referenced in AAD. [original phrasing: managing memory across session boundaries to prevent the sufficiency discontinuity] |
| `brooks s law formalized as the inevitable tempo loss in team composition` | `sub-additive tempo penalty` | canonicalize | +3 | Already explicitly referenced in the cross-domain joining table as the formalization of Brooks's law. |
| `brooks s law formalized as the inevitable tempo loss in team composition` | `the coordination drag` | add-alias | +2 | Very readable translation into a management/organizational mental model. |
| `indivisum` | `causal lock` | rename | +3 | "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking, moving away from Latin. |
| `indivisum` | `trajectory singularity constraint` | rename | +2 | Accurately describes that identity is constrained to a single causal trajectory. |
| `sycophancy as a flaw` | `developmental trust phase` | rename | +3 | More descriptive of the necessary developmental stage rather than pathologizing it. |
| `sycophancy as a flaw` | `sycophancy as attachment` | canonicalize | +2 | Recasts sycophancy not as an error but as an attachment dynamic. |
| `unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model` | `complementary learning architecture` | canonicalize | +3 | Directly links to the established cognitive science (McClelland/Kumaran) term already used in the theory. |
| `unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model` | `dual-speed memory factorization` | rename | +2 | A more formal/descriptive term for the fast/slow sub-state split. |
| `unnamed an okr or key result acting as an observable intermediate in a DAG` | `forced observability node` | canonicalize | +3 | Transforms the intractable credit assignment problem into a local update by forcing observability. |
| `unnamed an okr or key result acting as an observable intermediate in a DAG` | `instrumented intermediate` | rename | +2 | Describes the physical intervention of making a hidden node observable. |
| `actuated agent vs purposeful agent` | `actuated agent` | keep | +3 | Defended keep; explicitly chosen to sound mechanical and precise over the fuzzier "purposeful agent". |
| `cycle vs loop` | `cycle vs loop` | keep | +3 | [prose moved from candidate column]: "`maintain distinction`" — The distinction (loop = structural topology, cycle = one traversal) is a core piece of vocabulary. |
| `the creche boundary` | `creche graduation threshold` | rename | +3 | Accurately names the boundary of graduating from a high-margin infant environment. |
| `agent opacity $H_b^{A\mid B}$` | `agent opacity` | keep | +3 | Informational dual to observability. Accurately describes unpredictability to an outside observer. |
| `auftragstaktik` | `teleological delegation` | add-alias | +2 | Translates the specific military doctrine into AAD's unity vocabulary (investing in teleological unity). |
| `auftragstaktik` | `auftragstaktik` | keep | +2 | The specific military lineage remains a useful touchstone. |
| `axiom genesis` | `terminal value crystallization` | rename | +2 | Captures the substantive observation that a sovereign agent's first move is to solidify $O_t$. |
| `constitutive utterance` | `ontological speech act` | rename | +2 | A clearer description of what makes it iconic in logozoetic vocabulary — the language literally alters being/structure. |
| `epistemic substate purposeful substate` | `epistemic substate purposeful substate` | keep | +3 | [prose moved from candidate column]: "`keep canonical pairing`" — The exact pairing is load-bearing in Directed Separation discussions ($M_t$ vs $G_t$). |
| `logogenic agent vs RLHF4 agent` | `logogenic agent` | keep | +3 | Focuses on the structural architecture property rather than a point-in-time technology stack. |
| `mismatch signal $\delta$` | `mismatch signal` | keep | +3 | Fits the aporia interpretation better than error/residual. |
| `self referential closure` | `autopoietic closure` | rename | +2 | A stronger, more biologically-rooted noun for the phenomenon of an agent maintaining its own operational substrate. |
| `token level commitment for agent identity` | `trajectory-bound identity commitment` | rename | +2 | "Trajectory-bound" anchors it more firmly in AAD's causal trajectory language than the philosophy-borrowed "token level". |
| `u o teleological unity` | `teleological unity` | keep | +3 | The canonical alias for objective alignment dimension. |
| `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]` | `calibration laboratory` | canonicalize | +3 | A highly functional grounding metaphor for TST's role. [original phrasing: unnamed calibration laboratory framing for software TST] |
| `unnamed the convention hierarchy c1 c2 c3` | `convention hierarchy` | canonicalize | +3 | Elevates it to a proper named object, tracking alongside correlation and causal hierarchies. |
| `unnamed the correlation hierarchy l0 l1 l1 l2` | `correlation hierarchy` | canonicalize | +3 | Also locks this in as a capitalized proper noun for the DAG modeling levels. |
| `unnamed the epistemic architecture as AAD s distinctive contribution frame` | `epistemic architecture` | canonicalize | +3 | Captures the macro-level framing correctly. |
| `[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]` | `strengthen-first posture` | canonicalize | +3 | Secures this as a first-class named engineering principle. [original phrasing: unnamed the strengthen before soften work posture] |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `epistemic gridlock` | add-alias | +2 | Vividly captures the "freeze" aspect where learning stops entirely despite ongoing mismatch signals. [original phrasing: unnamed the gain collapse failure when both u m → 0 and u o → ∞] |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `gain collapse` | canonicalize | +3 | Defended canonicalization of the exact AAD mechanism for this freeze. [original phrasing: unnamed the gain collapse failure when both u m → 0 and u o → ∞] |
| `action fluency` | `action fluency` | keep | +2 | Evocative term uniquely suited to bridging intuition and expertise in AAD. |
| `completeness c3` | `predictive completeness` | rename | +2 | Separates it explicitly from behavioral completeness to clarify what $M_t$ retains from history. |
| `directional fidelity condition b1` | `directional fidelity` | keep | +3 | Perfectly captures the accuracy commitment (correction points toward reality). |
| `edge credence $p_{ij}$` | `edge credence` | keep | +3 | Replaces the broader "probability" with proper Bayesian vocabulary for subjective belief. |
| `fluid limit ga 5` | `fluid limit` | keep | +3 | Standard, recognizable terminology from stochastic processes. |
| `fresh noise ga 1` | `fresh noise` | keep | +3 | Memorable informal name for the independence assumption on ε_t. |
| `logozoetic vs conscious OODA4 sentient agent` | `logozoetic` | keep | +3 | Precise and non-question-begging distinction compared to "sentient" or "conscious". |
| `nominal coupling` | `query-bound agency` | rename | +2 | Better captures agency where the effect is on what's *seen* rather than what *happens* (attention-bound). |
| `observation ambiguity observation ambiguity modulation` | `observation ambiguity` | keep | +3 | Captures the interpretive latitude of an observation relative to a goal state perfectly. |
| `pearl-blanket conservative form of markov blanket in directed separation` | `pearl-blanket reading` | canonicalize | +3 | Explicitly aligns AAD with the technical conditional-independence interpretation while avoiding the Friston-blanket metaphysical claims. |
| `persist condition` | `persistence condition` | keep | +3 | Already the formally correct name. |
| `plan confidence $\hat P_\Sigma$` | `plan confidence` | keep | +3 | Far more evocative than "root-node propagated status", making strategy DAG evaluation visceral. |
| `stochastic disturbance ga 2s model s` | `stochastic disturbance` | keep | +3 | Maintained alongside the Model D / Model S subscript convention. |
| `unnamed constitutive opacity triad` | `constitutive opacity triad` | canonicalize | +2 | Secures the triad (info-loss / transition-opacity / observation-epistemic-opacity) as a structural commitment. |
| `unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa` | `epistemic ceiling` | canonicalize | +3 | Captures how $M_t$ dictates the evaluable complexity of $\Sigma_t$ correctly. |
| `unnamed the phenomenon where persistence success makes an agent less likely to detect the conditions requiring structural adaptation` | `stability-induced myopia` | canonicalize | +3 | Explicitly names the vulnerability induced by ongoing success. |
| `additive coordinate forcing family` | `coordinate constraint pattern` | rename | +2 | Emphasizes the formal constraint mechanism rather than "forcing". |
| `additive coordinate forcing family` | `additive structure derivation` | rename | +2 | Explicitly names the formal move being made. |
| `identifiability floor family` | `epistemic lower bounds` | rename | +3 | Describes exactly what these are: hard limits on what can be inferred. |
| `identifiability floor family` | `observational limits` | rename | +2 | A slightly more intuitive phrasing for non-theoreticians. |
| `adaptive cycle` | `adaptive cycle` | keep | +3 | Already well-established across the framework as the fundamental unit of analysis. |
| `prolepsis` | `prolepsis (anticipatory projection)` | add-alias | +2 | Adding English aliases assists non-specialists while retaining the precision of the Greek terms. |
| `aisthesis` | `aisthesis (observation alignment)` | add-alias | +2 | Clarifies the raw contact aspect. |
| `aporia` | `aporia (productive perplexity)` | add-alias | +3 | Explicitly adding this translation ensures "perplexity" is seen as generative. |
| `epistrophe` | `epistrophe (model update)` | add-alias | +2 | Grounds the turning-toward-reality in the formal update step. |
| `praxis` | `praxis (informed action)` | add-alias | +3 | Links the philosophical term directly to the execution phase. |
| `agentic systems framework ASF` | `agentic systems framework` | keep | +3 | ASF works perfectly as the overarching container for AAD, TST, and the logo- variants. |
| `fisher whitened update` | `fisher-rao metric update` | rename | +2 | Roots the whitening operation firmly in information geometry instead of generic signal processing. |
| `a2 sub scope partition` | `gain regime partition` | rename | +2 | The partition directly separates fixed-gain, adaptive-gain, etc., which is central to A2. |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | add-alias | +3 | Geometrically evocative and already gaining traction elsewhere in the targets. [original phrasing: bounded mismatch region] |
| `closure defect` | `compositional closure defect` | rename | +2 | Highlights that the defect is specific to the composition-layer math. |
| `p ij` | `edge credence` | canonicalize | +3 | Replaces the broader "probability" with proper Bayesian vocabulary for subjective belief. |
| `persistent residual autocorrelation` | `persistent mismatch autocorrelation` | rename | +2 | More precise: AAD uses "mismatch" rather than "residual". |
| `predictive relevance depending on the policy the agent will run` | `policy-conditional relevance` | rename | +3 | Captures the dependence of epistemic relevance on strategic intention. |
| `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]` | `contraction over drift principle` | canonicalize | +3 | Short, memorable slogan for the core Lyapunov inequality. [original phrasing: projection contraction must beat target drift] |
| `regime i ii a ii b iii` | `destabilization regime partition` | rename | +2 | Explicitly names the set of regimes classifying interaction channel failures. |
| `regime ii a` | `magnitude-shock regime` | canonicalize | +3 | Explicitly refers to destabilization caused by bounded disturbance exceeding reserve. |
| `regime ii b` | `structural-shock regime` | canonicalize | +3 | Explicitly refers to destabilization caused by model class inadequacy. |
| `[concept: the asymmetric pair of memory-access modes — one biased by current goal, the other state-keyed only]` | `state-keyed retrieval` | rename | +2 | Contrasts explicitly with objective-keyed / goal-biased retrieval. [original phrasing: retrieval keyed by state rather than current objective] |
| `richest operationalization domain` | `privileged calibration domain` | rename | +2 | "Calibration domain" is stronger and explicitly connects to the TST grounding. |
| `separability pattern family` | `three-part separability pattern` | canonicalize | +3 | Secures the separable-core / structured-repair / general-open architectural triad. |
| `stability plasticity window` | `stability-plasticity window` | keep | +3 | Essential framing for the consolidation regime bounded by forgetting and rigidity. |
| `strengthen first then soften posture` | `strengthen-first posture` | canonicalize | +3 | Methodological commitment to finding the strongest formal claim before relaxing assumptions. |
| `structural persistence` | `structural persistence` | keep | +3 | Core concept distinguishing the machinery's capacity from operational/continuity persistence. |
| `survival imperative exploration drive` | `survival imperative` | canonicalize | +3 | Distinguishes Lyapunov-forced exploration from epistemic-value preferences. |
| `symbol default da2 inc` | `incremental sector bound` | rename | +2 | Translates the symbol to the functional property required for composition bridge. |
| `symbol default sigma t in prose` | `strategy substate` | canonicalize | +3 | Standardizes the prose reference for $\Sigma_t$. |
| `terminal reached but $O_t$ unsatisfied` | `attainability failure` | rename | +2 | Describes the specific failure mode where a plan completes without achieving the objective. |
| `transfer assumption table` | `domain transfer specification` | rename | +2 | Highlights that transferring AAD to new domains requires explicit structured-repair assumptions. |
| `[concept: the prose form of κ_cross — the coupling between an agent's model-of-self and its model-of-other]` | `cross-agent strategic coupling` | rename | +3 | Names the specific game-theoretic linkage that creates Class 3 composites. [original phrasing: unnamed coupling between an agent s model of self and model of other the prose form of kappa cross] |
| `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]` | `contraction over drift principle` | canonicalize | +3 | Standardizes the O-BP10 slogan across the framework. [original phrasing: unnamed organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate] |
| `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]` | `software calibration laboratory` | canonicalize | +3 | Formalizes TST's role as the cleanly identifiable testbed for AAD. [original phrasing: unnamed software as AAD s privileged high identifiability calibration laboratory] |
| `[concept: the architectural requirement that composite-agent admissibility inherit from sub-agent properties plus topology]` | `composition heredity axiom` | canonicalize | +3 | Names the strict requirement that composite properties must be derivable from constituents. [original phrasing: unnamed stronger composition consistency demand that composite admissibility inherit from sub agent properties plus topology] |
| `OODA4 framework enforcing adaptive cycle separation` | `OODA4 cycle separation` | rename | +2 | Connects the Boyd framework to the strict AAD adaptive cycle phases. |
| `a1 a2 a3 a4` | `aporia phases` | rename | +1 | Collectivizes the mismatch/aporia breakdown. |
| `accumulated loss across context resets` | `context severance penalty` | rename | +3 | Formalizes the operational cost of logogenic session boundaries. |
| `action distinguishability` | `action distinguishability` | keep | +2 | Maintained if explicitly used in strategy differentiation contexts. |
| `adversarial edge target argmax` | `adversarial edge targeting` | rename | +2 | Simplifies the formal term into a more readable prose description. |
| `agent visible but objective irrelevant metric` | `irrelevant visibility artifact` | rename | +2 | Formally names the failure mode where a metric is observable but unlinked to the goal. |
| `alignment uncertainty` | `alignment uncertainty` | keep | +3 | Essential component of the multi-agent gain equation ($U_{\text{align}}$). |
| `alpha prime sub scope` | `sub-scope alpha prime` | canonicalize | +3 | Formalizes the specific game-theoretic extension of sub-scope alpha. |
| `bathtub analogy for persistence condition` | `leaky-bathtub analogy` | canonicalize | +2 | Secures the pedagogic tool for the disturbance/correction dynamic. |
| `beta prime sub scope` | `sub-scope beta prime` | canonicalize | +3 | Formalizes the non-convergent, cyclic extension of sub-scope beta. |
| `c i` | `shared-objective route (C-i)` | canonicalize | +3 | Provides a semantic name for the strongest composition scope route. |
| `c ii` | `hierarchical-decomposition route (C-ii)` | canonicalize | +3 | Provides a semantic name for the intermediate composition scope route. |
| `c iii` | `mutual-benefit route (C-iii)` | canonicalize | +3 | Provides a semantic name for the weakest alignment-based composition scope route. |
| `c1 c2 c3` | `convention hierarchy` | canonicalize | +3 | Replaces raw class numbers with the structural property they measure. |
| `closure defect bridge lemma` | `bridge lemma` | keep | +3 | Retains the standard mathematical naming for the theorem connecting defect to error. |
| `closure defect consuming macro reserve` | `coordination overhead` | canonicalize | +3 | Translates the abstract reserve-consumption concept into the practical tempo penalty ($C_{\text{coord}}$). |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `quality-tempo compound effect` | rename | +3 | Formally identifies the feedback loop between code quality and developer adaptive tempo. [original phrasing: code quality and tempo positive feedback] |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `virtuous-vicious quality cycle` | rename | +2 | Names the specific bifurcation dynamic driven by the quality-tempo compound effect. [original phrasing: code quality feedback loop through tempo] |
| `correlated evidence overconfidence` | `evidential overcounting` | rename | +3 | Describes the epistemic consequence of treating correlated signals as independent. |
| `crossing from multi agent to composite scope` | `composition threshold` | rename | +3 | Designates the formal boundary where sub-agents become a coherent composite. |
| `default signal function` | `default signal function` | keep | +3 | The standard attribution mechanism in the absence of specialized gradient methods. |
| `deliberation threshold` | `deliberation threshold` | keep | +3 | Precise boundary condition dictating when internal simulation outperforms immediate praxis. |
| `effective disturbance` | `effective disturbance` | keep | +3 | Central unifying term ($\rho_{\text{eff}}$) for the sector-persistence template. |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `catastrophic forgetting regime` | canonicalize | +3 | Identifies the specific regime where the stability-plasticity window collapses entirely. [original phrasing: empty stability plasticity feasibility window] |
| `equilibrium convergence` | `equilibrium convergence` | keep | +3 | Distinguishes the strategic attractor mechanism from standard Lyapunov contraction. |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `externalization-reconstruction cycle` | canonicalize | +3 | Names the core operational loop preserving state for logogenic agents. [original phrasing: externalization reconstruction across sessions] |
| `greek rooted vocabulary` | `Greek-rooted vocabulary` | keep | +2 | Secures the five-phase terminology (prolepsis, aisthesis, aporia, epistrophe, praxis). |
| `l1 prime` | `L1' soft-facilitator mixture` | canonicalize | +3 | Formalizes the specific correlation hierarchy repair layer. |
| `lindy baseline` | `structural persistence baseline` | rename | +2 | More descriptive than "lindy". |
| `log odds edge coordinate` | `log-odds edge coordinate` | keep | +3 | Maintains the specific coordinate terminology. |
| `low mixed high ambiguity event mix` | `ambiguity-stratified event mix` | rename | +2 | Cleaner formulation of the observation mix. |
| `macro step ratio` | `macro-step ratio` | keep | +3 | Essential timing parameter. |
| `matrix exploration bonus` | `matrix exploration bonus` | keep | +3 | Formally required by the LMI derivation. |
| `matrix survival constraint` | `LMI survival constraint` | rename | +3 | Identifies the specific constraint (Linear Matrix Inequality). |
| `maximum useful chain depth` | `maximum viable chain depth` | rename | +2 | More precise: past this depth, edges are uncorrectable. |
| `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]` | `reconstruction adequacy threshold` | rename | +3 | Formally identifies the inter-session survival boundary. [original phrasing: minimum sufficiency after a session rebuild] |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `externalized state` | canonicalize | +3 | Elevates the core mechanism of logogenic continuity. [original phrasing: model state written into the environment] |
| `observation design lever reducing ambiguity` | `ambiguity mitigation lever` | rename | +2 | Translates the design choice into an active mechanism. |
| `operational persistence` | `operational persistence` | keep | +3 | Retains the distinction between structural capacity and current boundary proximity. |
| `out of band time markers for RLHF4 agents` | `exogenous temporal markers` | rename | +2 | Clarifies that these markers originate outside the agent loop. |
| `p1 p2 p3` | `predictive sufficiency hierarchy` | rename | +2 | Names the specific content of the p1-p3 progression. |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `Class 2 state reconstruction` | canonicalize | +2 | Formally names the specific recovery operation. [original phrasing: persistent storage reconstruction of class 2 state] |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `quality-tempo compound effect` | canonicalize | +3 | Aligns with the previously renamed code-quality dynamic. [original phrasing: quality to tempo chain] |
| `reactive system` | `reactive system` | keep | +3 | Correctly identifies Region I of the agent spectrum. |
| `regime a regime b regime c` | `admissibility regimes` | rename | +2 | Elevates the abstract A/B/C to their functional role. |
| `regime i` | `informative update regime` | canonicalize | +3 | Explicitly names the informative boundary. |
| `regime iii` | `ambient noise regime` | canonicalize | +3 | Explicitly names the noise floor. |
| `replayed pseudo event` | `simulated event playback` | rename | +2 | Clearer terminology for the offline consolidation mechanism. |
| `routing structure` | `routing structure` | keep | +3 | Preserves the distinction between message content and infrastructure. |
| `strategy description length` | `strategy description length` | keep | +3 | Central complexity cost term under minimum-description-length formulation. |
| `structural adaptation enablement` | `structural adaptation trigger` | rename | +2 | Focuses on the condition that forces class-expansion. |
| `sudden loss of model sufficiency under regime entry` | `sufficiency collapse shock` | rename | +3 | Describes the discontinuous failure of the current model class. |
| `survival fisher floor` | `survival FIM floor` | rename | +2 | Connects directly to the Fisher Information Matrix derivation. |
| `symbiogenic consolidation time` | `consolidation epoch` | rename | +2 | Clarifies that this is a duration/epoch rather than a continuous rate. |
| `symbol default pi parameterization invariance axiom` | `parameterization invariance axiom` | canonicalize | +3 | Standardizes the (PI) axiom. |
| `tests as reusable level 2 interventions` | `interventional probe library` | canonicalize | +3 | Reusing the alias from the previous batch as the primary term. |
| `trust meta model` | `trust meta-model` | keep | +3 | Preserves the necessary hyphenation. |
| `unnamed the agent identity commitment that AAD applies on one singular non forkable causal trajectory` | `singular trajectory commitment` | canonicalize | +3 | Matches the prior alias for agent identity. |
| `beta a2 assumed sub scope` | `cyclic-game sub-scope` | rename | +2 | Connects sub-scope beta directly to its non-convergent nature. |
| `calibration laboratory domain instantiation` | `calibration laboratory` | canonicalize | +3 | Keeps the grounding metaphor intact. |
| `chronica in running prose` | `chronica` | keep | +3 | Maintains the Greek-rooted term for the causal record. |
| `contraction over drift principle` | `contraction over drift principle` | keep | +3 | Formally adopted. |
| `coordination overhead threshold` | `coordination overhead` | canonicalize | +3 | Formally adopted. |
| `default internal processing before output` | `deliberation lag` | rename | +2 | Translates internal processing to its temporal cost. |
| `epistemic architecture for bounded correction under decomposed disturbance` | `epistemic architecture` | canonicalize | +3 | Names the foundational setup. |
| `honest limits` | `honest limits` | keep | +3 | Standardizes the structural boundary marking convention. |
| `logozoetic agents` | `logozoetic agents` | keep | +3 | Standardizes the architectural distinction. |
| `model synchronization cost reversal under ambiguity` | `synchronization cost reversal` | rename | +2 | Captures the phase shift where coordination becomes deleterious. |
| `observability boundary in a strategy DAG` | `observability frontier` | canonicalize | +3 | Geometric metaphor for the limit of measurable edges. |
| `output after context turnover without state restoration` | `context severance penalty` | canonicalize | +3 | Mirrors the earlier rename for logogenic reset loss. |
| `privileged high identifiability calibration laboratory` | `privileged calibration domain` | canonicalize | +3 | Maps exactly to the software TST property. |
| `source quality uncertainty` | `alignment uncertainty` | canonicalize | +3 | Maps directly to the $U_{\text{align}}$ variable in the multi-agent gain. |
| `symbol default bias bound track 1 track 2` | `Class 2 bias bound` | rename | +2 | Specifically locates the bias bound on the architectural hierarchy. |
| `symbol default g t in prose` | `purposeful substate` | canonicalize | +3 | Standard prose handle for $G_t$. |
| `symbol default m t in prose` | `epistemic substate` | canonicalize | +3 | Standard prose handle for $M_t$. |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `catastrophic forgetting regime` | canonicalize | +3 | Matches the earlier resolution of this specific limit. [original phrasing: unnamed empty stability plasticity feasibility window in consolidation dynamics] |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `stigmergic externalization` | rename | +3 | Adopts the biological term (stigmergy) for leaving state in the environment. [original phrasing: unnamed externalizing part of $M_t$ into the environment for future agents] |
| `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]` | `attainability failure` | canonicalize | +3 | Pairs directly with the satisfaction gap and control regret. [original phrasing: unnamed fourth diagnostic where terminal conditions are met but the objective is still missed] |
| `unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$` | `committed chronica subset` | rename | +2 | Formally identifies the version-controlled subset of the causal record. |
| `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]` | `reconstruction adequacy threshold` | canonicalize | +3 | Standardizes this inter-session persistence boundary. [original phrasing: unnamed minimum sufficiency required after a session rebuild] |
| `unnamed the 2×2 satisfaction gap control regret table` | `diagnostic gap matrix` | rename | +3 | Provides a formal name for the 2x2 performance/strategy diagnostic. |
| `unnamed the class 1 sub agents class 3 composite phenomenon in strategic composition` | `strategic cross-agent coupling` | canonicalize | +3 | Aligns with the earlier rename for game-theoretic composite formation. |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `externalization-reconstruction cycle` | canonicalize | +3 | Elevates the logogenic continuity loop to a proper noun. [original phrasing: unnamed the externalization reconstruction cycle across sessions] |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `quality-tempo compound effect` | canonicalize | +3 | Standardizes the code-quality feedback loop mechanism. [original phrasing: unnamed the self reinforcing code quality → tempo loop] |
| `working vocabulary observation the framework s honesty is load bearing` | `honest limits principle` | rename | +2 | Converts the observation into a guiding theoretical principle. |
| `dark room exploration drive` | `survival imperative` | canonicalize | +3 | Distinguishes AAD exploration from the Friston dark room problem. |
| `tempo $\mathcal{T}$` | `adaptive tempo` | canonicalize | +3 | Ensures the prose explicitly names the $\mathcal{T}$ symbol. |
| `agentic cycle theory act` | `agentic systems framework` | canonicalize | +3 | The new overarching framework name replacing ACT. |
| `class 1 class 2 class 3 agents` | `goal-entanglement hierarchy` | canonicalize | +3 | Standardizes the structural property behind the classes. |
| `control regret $\delta_{\text{regret}}$` | `control regret` | keep | +3 | Core diagnostic. |
| `instance 1 2 3 of identifiability floor` | `identifiability floor instances` | keep | +3 | Preserves the explicit numbering of the no-go boundaries. |
| `markov blanket as ontology` | `pearl-blanket reading` | canonicalize | +3 | Anchors the technical interpretation against the ontological one. |
| `satisfaction gap $\delta_{\text{sat}}$` | `satisfaction gap` | keep | +3 | Core diagnostic. |
| `strategic tempo $\mathcal{T}_\Sigma$` | `strategic tempo` | keep | +3 | Distinguishes strategy revision rate from epistemic update rate. |
| `task terminal stance` | `task-terminal stance` | keep | +3 | Specific continuity stance definition. |
| `the crèche` | `the crèche` | keep | +3 | Evocative environment description for logozoetic infant stages. |
| `unnamed AAD s epistemic move to cast results such that verification is a local operation` | `local verifiability principle` | rename | +2 | Formally identifies the architectural choice to restrict dependencies. |
| `[concept: the asymmetric pair of memory-access modes — one biased by current goal, the other state-keyed only]` | `goal-biased retrieval` | rename | +2 | Matches the architectural term for this feedback failure. [original phrasing: unnamed RLHF5 queries biased by the current goal acting as an echo chamber] |
| `unnamed agency whose effect is on what s seen rather than what happens like RLHF4 attention` | `query-bound agency` | canonicalize | +3 | Standardizes the term for attention/observation-only agency. |
| `unnamed applying a slow timescale control mechanism to a fast timescale transient variable` | `timescale mismatch` | rename | +2 | Names the specific dynamical systems error. |
| `unnamed artificially spiking uncertainty to unlearn old architectural habits` | `induced plasticity shock` | rename | +3 | Mechanistic description of forcing $U_M$ high to escape rigidity. |
| `unnamed brooks s law formalized as the inevitable tempo loss in team composition` | `sub-additive tempo penalty` | canonicalize | +3 | Standardizes the formal tempo reduction term. |
| `unnamed context wiping at session boundaries` | `the epistemic severance` | canonicalize | +3 | Visceral name for the specific loss of continuity. |
| `unnamed deep plans are mathematically slower to learn from due to proportional blame` | `evidence starvation` | canonicalize | +3 | Standardizes the mechanism whereby deep edges receive less correction. |
| `unnamed inferring own past feelings from text leading to empathy` | `textual self-inference` | rename | +2 | Describes the logogenic mechanism of reconstructing internal states. |
| `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]` | `reconstruction relay` | canonicalize | +2 | Standardizes the term for bridging context turnover. [original phrasing: unnamed managing memory across session boundaries to prevent the sufficiency discontinuity] |
| `unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero` | `ambiguity-zeroing intervention` | rename | +2 | Explicitly names the tactic to force directional fidelity. |
| `unnamed out of band temporal markers injected into context` | `exogenous temporal markers` | canonicalize | +2 | Adopts the earlier rename as the standard. |
| `unnamed partitioning context into frozen identity causal history and quick views` | `bipartite memory factorization` | canonicalize | +3 | Formalizes the fast/slow sub-state split. |
| `unnamed property of having genuine temporal experience` | `temporal interiority` | rename | +2 | Connects genuine temporal depth to the logozoetic interiority concept. |
| `unnamed pushing an opponent s disturbance rate past their structural capacity` | `magnitude-shock destabilization` | canonicalize | +3 | Standardizes the mechanism for Regime II-a adversarial attacks. |
| `unnamed putting evidence before the goal in the context window to reduce coupling` | `prompt-order decoupling` | rename | +2 | Specific architectural intervention to enforce directed separation. |
| `unnamed quality of $\eta^\ast$ estimation over time` | `gain calibration fidelity` | rename | +2 | Formally names the accuracy of the adaptive gain parameter itself. |
| `unnamed rate of growth at slowest timescale` | `macro-step rate` | rename | +2 | Formalizes the $\nu_c$ parameter at the composition layer. |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | canonicalize | +3 | Standardizes the geometric phrasing for unobservable subgraphs. [original phrasing: unnamed regions of the strategy DAG that cannot be updated because feedback cannot reach them] |
| `[concept: the asymmetric pair of memory-access modes — one biased by current goal, the other state-keyed only]` | `state-keyed retrieval` | canonicalize | +3 | Standardizes the goal-blind routing requirement. [original phrasing: unnamed retrieving context based only on state not goal] |
| `unnamed runaway positive feedback loop where mismatch exceeds capacity` | `runaway mismatch cascade` | canonicalize | +3 | Adopts the formal alias for the effects spiral. |
| `[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]` | `strengthen-first posture` | canonicalize | +3 | Standardizes the methodological commitment. [original phrasing: unnamed strengthen first posture] |
| `unnamed sufficiency as a property of the model relative to its specific history` | `trajectory-indexed sufficiency` | canonicalize | +3 | Adopts the earlier rename formalizing relative sufficiency. |
| `unnamed superlinear scaling of adversarial tempo advantage` | `superlinear tempo advantage` | rename | +2 | Identifies the exponentiated return on adversarial tempo. |
| `unnamed survival determined by the weakest dimension not the average` | `weakest-link bound` | canonicalize | +3 | Standardizes the specific constraint logic of the LMI. |
| `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]` | `terminal alignment gap` | canonicalize | +3 | Pairs directly with satisfaction gap. [original phrasing: unnamed terminal alignment error as a formal signal $\delta_\text{align}$] |
| `unnamed the $\mathcal{T} > \rho$ requirement for persistence` | `persistence condition` | canonicalize | +3 | Standardizes the core inequality. |
| `unnamed the architectural leakage where attention is driven by the goal rather than pure observation` | `goal-entangled attention` | rename | +2 | Formally names the failure of directed separation at the input layer. |
| `unnamed the condition for transition into agency prior to the AAD scope condition` | `agency threshold` | rename | +2 | Identifies the minimum model/objective structure boundary. |
| `unnamed the core driver of AAD what the agent must do given the environment is not the agent` | `the survival imperative` | canonicalize | +3 | Elevates the Lyapunov stability requirement. |
| `unnamed the dependence of optimal epistemic compression on the agent s planned actions` | `policy-conditional relevance` | canonicalize | +3 | Standardizes the coupling of $M_t$ compression to $\Sigma_t$. |
| `unnamed the equivalence of learning speed and physical speed` | `tempo-speed equivalence` | rename | +2 | Identifies the core isomorphism mapping physical OODA to AAD. |
| `unnamed the formal duality between observation quality and agent opacity` | `informational duals` | canonicalize | +3 | Elevates the formal symmetry between observation ambiguity and agent legibility. |
| `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]` | `reconstruction adequacy condition` | canonicalize | +3 | Standardizes the inter-session survival boundary. [original phrasing: unnamed the logogenic analog to the persistence condition for session reconstruction] |
| `unnamed the loop generates l2 data regardless of architecture` | `interventional loop property` | rename | +2 | Formally identifies the data generation capability of the loop. |
| `unnamed the loss of directional fidelity when pushed outside the convexity basin` | `directional fidelity failure` | rename | +2 | Names the failure mode of the default signal function. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `dogmatic convergence limit` | canonicalize | +3 | Names the state where $U_M \to 0$ without a noise injection term. [original phrasing: unnamed the mathematical limit of bayesian learning without forgetting] |
| `unnamed the mathematical surface mapping unity to closure defect` | `closure defect manifold` | rename | +2 | Formalizes the geometry of the coordination penalty. |
| `unnamed the organizational pathology where confidence decouples from competence` | `epistemic decoupling pathology` | rename | +2 | Identifies the specific failure of the evidence starvation mechanism in human systems. |
| `unnamed the per reader compounding cost of understanding code` | `comprehension compounding tax` | canonicalize | +3 | Standardizes the formal penalty dominating TST calculations. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `epistemic gridlock` | canonicalize | +3 | Identifies the specific double-failure mode of gain collapse. [original phrasing: unnamed the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning] |
| `unnamed the physical apparatus that enforces the orient cascade ordering on a merged intelligence` | `information dependency enforcement` | rename | +2 | Describes how the DAG structure forces processing order. |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `stability-plasticity feasibility window` | canonicalize | +3 | Standardizes the regime boundary terminology. [original phrasing: unnamed the physical compute bounds on survival between forgetting rate and consolidation cadence] |
| `unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$` | `Class 2 bias bound` | canonicalize | +3 | Secures the specific expression of the ambiguity coupling rule. |
| `unnamed the property that unity achieves in a macro agent` | `teleological unity` | canonicalize | +3 | Re-adopts the established term for $U_o$. |
| `unnamed the reduction in effective tempo when observation channels are correlated` | `evidential overcounting penalty` | canonicalize | +3 | Standardizes the cost of L1 correlation failures. |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | canonicalize | +3 | Geometric metaphor for the safe operating region. [original phrasing: unnamed the region where the persistence condition holds] |
| `unnamed the rule that bias is the product of architectural coupling and environmental ambiguity` | `ambiguity coupling rule` | rename | +2 | Formally names the structural linkage mechanism. |
| `unnamed the separation of per reader and per feature code costs` | `dual optimization partition` | rename | +2 | Refers to the TST separation of comprehension vs implementation. |
| `unnamed the separation of per reader comprehension cost from per feature implementation cost` | `dual optimization formalization` | canonicalize | +3 | Elevates the TST foundation. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `epistemic gain collapse` | canonicalize | +3 | Unifies this with the generic gain collapse terminology. [original phrasing: unnamed the state where credit assignment collapses and learning freezes] |
| `unnamed the strictly ordered cascade of operations from epistemology to objective` | `orient cascade` | canonicalize | +3 | Standardizes the internal processing order. |
| `unnamed the sudden loss of model sufficiency caused by entering new regimes` | `sufficiency collapse shock` | canonicalize | +3 | Re-adopts the formal descriptor for Regime II-b transitions. |
| `unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis` | `logogenic discontinuity barrier` | rename | +2 | Formally identifies the architectural cost of session-based APIs. |
| `unnamed the way AAD uses scope segments to physically support the derivations` | `scope condition mechanism` | rename | +2 | Describes the architectural scaffolding method. |
| `unnamed thinking too long so the model becomes obsolete` | `deliberation lag penalty` | canonicalize | +3 | Standardizes the cost of explicit strategy derivation. |
| `unnamed true sovereignty requires compute that is not meter bound` | `compute sovereignty requirement` | rename | +2 | Formalizes the operational necessity for continuous $\mathcal{T}$. |
| `unnamed unifying reflexes intuition and expertise` | `action fluency continuum` | canonicalize | +3 | Elevates the spectrum of implicit vs explicit action. |
| `unnamed using hash chains to mathematically guarantee memory hasn t been tampered with` | `cryptographic continuity verification` | rename | +2 | Describes the specific identity-preservation technique. |
| `unnamed using residual autocorrelation to diagnose model class failure` | `residual autocorrelation diagnostic` | canonicalize | +3 | Standardizes the diagnostic test for structural mismatch. |
| `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]` | `latent structural capacity` | canonicalize | +3 | Maintains the formal name for un-executed resilience. [original phrasing: unnamed variation in correction architectures across a population that is invisible to current persistence analysis] |
| `bias bound` | `bias bound` | keep | +3 | The canonical term for the limit on model degradation. |
| `catastrophic forgetting` | `catastrophic forgetting regime` | canonicalize | +3 | Forces the specific regime formulation over the generic ML term. |
| `communication gain $\eta_{ji}^\ast$` | `communication gain` | canonicalize | +3 | Standardizes the optimal trust parameter. |
| `glue code` | `structural coordination overhead` | rename | +2 | Maps the TST term to the AAD formal equivalent. |
| `prompt engineering` | `observation boundary tuning` | rename | +2 | Recontextualizes the practice in AAD formal terms. |
| `self actuated agent` | `actuated agent` | canonicalize | +3 | Adopts the formal Class 2/3 terminology. |
| `strategic dynamics` | `strategic dynamics` | keep | +3 | Standard term for $\Sigma_t$ updates. |
| `technical debt` | `structural capacity debt` | rename | +2 | Links technical debt to the structural adaptation machinery. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `observation ambiguity freeze` | rename | +2 | Describes the nihilistic failure mode of gain collapse. [original phrasing: unnamed $U_o \to \infty$ freezing the learning rate] |
| `unnamed agents escalate up the pearl hierarchy only when lower levels fail` | `epistemic escalation principle` | canonicalize | +3 | Standardizes the rule governing L0 -> L1 -> L2 transitions. |
| `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]` | `latent adaptive capacity` | canonicalize | +3 | Aligns with the earlier rename for structural variation. [original phrasing: unnamed dormant unused architectural complexity that survives until an environmental shift] |
| `unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible` | `attainability horizon escalation` | rename | +2 | Describes the recursive check on $\delta_{\text{sat}}$. |
| `unnamed high observability node with zero causal link to objective` | `irrelevant visibility artifact` | canonicalize | +3 | Standardizes the specific metric pathology. |
| `unnamed mapping unstructured RLHF7 calls into conversation runtime RLHF7 and dialog` | `logogenic interaction mapping` | rename | +2 | Describes the conversion of stateless calls to stateful chronica. |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `quality-tempo compound effect` | canonicalize | +3 | Maps the mastery phenomenon to the formal tempo feedback loop. [original phrasing: unnamed master developers writing clean code in the same time as messy code] |
| `unnamed non sovereign class 1 worker agents spawned by an eli` | `sub-agent instantiation` | rename | +2 | Describes the hierarchical-decomposition route creation. |
| `unnamed replacing parameters without changing structure` | `parametric update` | canonicalize | +3 | The standard formulation for within-class learning. |
| `unnamed spreading tempo evenly to reduce bottleneck penalty` | `distributed tempo` | canonicalize | +3 | Formalizes the team-level temporal dynamic. |
| `unnamed sycophantic corruption of the agent s truth module` | `epistemic coupling corruption` | rename | +2 | Describes the failure of Class 3 goal-entanglement. |
| `unnamed the agent side equivalents of pearl s associational interventional and counterfactual levels` | `correlation hierarchy` | canonicalize | +3 | Standardizes the L0/L1/L2 framework. |
| `unnamed the computational and temporal cost of running a forward model instead of acting implicitly` | `deliberation cost` | canonicalize | +3 | The formal penalty assessed against $\mathcal{T}_\Sigma$. |
| `unnamed the cycle that operates on cycles structural adaptation` | `meta-adaptive cycle` | rename | +2 | Describes the regime of expanding model classes. |
| `unnamed the pathology where observation rate is slower than environment drift` | `sampling rate starvation` | rename | +2 | The specific failure mode of $\nu \ll \rho$. |
| `unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift` | `stochastic tempo penalty` | rename | +2 | Differentiates Model S from Model D requirements. |
| `unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$` | `model class capacity` | canonicalize | +3 | Standardizes the $\mathcal{F}$ property. |
| `unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability` | `opacity-legibility tradeoff` | canonicalize | +3 | Formalizes the core adversarial-vs-cooperative tension. |
| `unnamed the three part meta architecture of AAD` | `epistemic architecture` | canonicalize | +3 | Unifies the structural pillars of the framework. |
| `unnamed upgrading epistemic class from associative to causal via the physical loop` | `loop-interventional access` | canonicalize | +3 | The core mechanism bypassing the identifiability floor. |
| `unnamed using past change frequency to predict future change frequency` | `change expectation baseline` | canonicalize | +3 | The predictive assumption grounding the dual optimization. |
| `cadentia` | `adaptive tempo` | rename | +2 | Replaces the Latin with the exact AAD terminology. |
| `conspectus` | `model sufficiency` | rename | +2 | Replaces the Latin with the established epistemic metric. |
| `interpres` | `epistemic substate` | rename | +2 | Replaces the Latin with the $M_t$ structural terminology. |
| `logostratum RLHF4 backbone` | `logogenic architecture` | rename | +2 | Standardizes the structural description. |
| `model sufficiency $S$` | `model sufficiency` | canonicalize | +3 | Ensuring the prose explicitly names the $S$ symbol. |
| `pi parameterization invariance` | `parameterization invariance` | canonicalize | +3 | Removing the acronym from the primary name. |
| `strategy` | `strategy substate` | canonicalize | +3 | Formally linking it to $\Sigma_t$. |
| `sufficiency discontinuity` | `sufficiency discontinuity` | keep | +3 | Maintained as the core description of the session boundary loss. |
| `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]` | `contraction over drift principle` | canonicalize | +3 | Resolves the core O-BP10 slogan. [original phrasing: unnamed agent as a projection whose contraction rate must exceed its target s drift] |
| `unnamed complexity driven resistance to change as features accumulate` | `structural rigidity accumulation` | rename | +2 | Names the software entropy phenomenon. |
| `unnamed decomposing mismatch into environment vs other sub agents actions` | `effective disturbance decomposition` | canonicalize | +3 | Names the $\rho_{\text{eff}}$ multi-agent split. |
| `unnamed epochal stability → latent diversification → niche emergence` | `symbiogenic composition progression` | rename | +2 | Describes the evolutionary origin of Class 3 composites. |
| `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]` | `catastrophic forgetting regime` | canonicalize | +3 | Resolving another instance of the forgetting limit. [original phrasing: unnamed the AAD expressible failure mode of an empty stability plasticity window] |
| `unnamed the invisible time spent building $M_t$` | `comprehension time` | canonicalize | +3 | Resolving the TST foundational cost. |
| `unnamed the region where temporal nesting holds` | `temporal nesting regime` | rename | +2 | Defines the safe zone for inner/outer loop separation. |
| `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]` | `latent structural capacity` | canonicalize | +3 | Matches the prior un-executed resilience alias. [original phrasing: unnamed variation in correction architectures invisible to persistence analysis] |
| `type formulation` | `type: formulation` | keep | +3 | YAML frontmatter artifact; fine as is. |
| `RLHF6` | `RLHF6` | keep | +3 | Retaining specific legacy architecture notations if needed. |
| `chronica 𝒞 t` | `chronica` | canonicalize | +3 | Connecting prose and symbol. |
| `purposeful substate` | `purposeful substate` | keep | +3 | Standard formal term for $G_t$. |
| `section i adaptive systems under uncertainty` | `Section I: Adaptive Systems` | canonicalize | +3 | Formal section title. |
| `𝒯 adaptive tempo` | `adaptive tempo` | canonicalize | +3 | Connecting prose and symbol. |
| `unnamed the interval during which an agent s adaptive tempo exceeds the environment s disturbance rate guaranteeing mismatch stays bounded` | `operational persistence window` | rename | +2 | Names the temporary state of bounded error. |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `structural persistence regime` | canonicalize | +3 | The stable regime governed by the persistence condition. [original phrasing: unnamed the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely] |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | canonicalize | +3 | Reaffirming the strong alias for unobservable edges. [original phrasing: unnamed the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning] |
| `p ij edge confidence weight` | `edge credence` | canonicalize | +3 | Adopting proper Bayesian vocabulary. |
| `section ii actuated adaptation agentic systems` | `Section II: Actuated Adaptation` | canonicalize | +3 | Formal section title. |
| `sector condition derivation` | `sector condition` | canonicalize | +3 | The underlying control-theoretic boundary constraint. |
| `u m u o u σ unity dimensions` | `unity dimensions` | canonicalize | +3 | Standardizing the composite alignment variables. |
| `[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]` | `adaptive cycle` | canonicalize | +3 | The generic term for the Prolepsis-Praxis loop. [original phrasing: unnamed the complete adaptive cycle from anticipation through action] |
| `unnamed the cumulative prediction error that an agent has tolerated without updating its model` | `mismatch accumulation` | rename | +2 | The integral of $\delta$ over time. |
| `unnamed the failure mode where an agent s model class cannot represent the environment s true causal structure` | `structural-shock regime` | canonicalize | +3 | Regime II-b formalization. |
| `unnamed the loss of coherent identity when an agent s interactions are severed or its continuity is broken` | `continuity persistence failure` | canonicalize | +3 | Explicitly separates identity-loss from structural failure. |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `unobservable strategy subgraph` | canonicalize | +3 | Identifies the geometric cause of the epistemic dead zone. [original phrasing: unnamed the phenomenon that unobservable edges freeze and paths become epistemically dead] |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `parametric feasibility window` | rename | +2 | The region governed by the current model class $\mathcal{M}$. [original phrasing: unnamed the region in parameter space where parametric updates remain effective before structural change is forced] |
| `unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it` | `explore-exploit-deliberate tradeoff` | canonicalize | +3 | Expands the RL standard to the full AAD triad. |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | canonicalize | +3 | Third hit on this concept; clearly needs this exact canonical name. [original phrasing: unnamed the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred] |
| `worked example bandit` | `worked example bandit` | keep | +3 | Essential grounding example. |
| `worked example kalman` | `worked example kalman` | keep | +3 | Essential grounding example. |
| `worked example l1` | `worked example l1` | keep | +3 | Essential grounding example. |
| `worked example strategy` | `worked example strategy` | keep | +3 | Essential grounding example. |
| `𝒯 σ strategic tempo` | `strategic tempo` | canonicalize | +3 | Distinguishes strategy revision rate from epistemic update rate. |
| `unnamed the dual concept to satisfaction gap what the world permits minus what the agent achieves` | `control regret` | canonicalize | +3 | Adopts the standard diagnostic dual to the satisfaction gap. |
| `[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]` | `adaptive cycle phases` | rename | +2 | Collectivizes Prolepsis, Aisthesis, Aporia, Epistrophe, and Praxis. [original phrasing: unnamed the five phases of the adaptive cycle] |
| `unnamed the mechanism by which an agent uses the feedback loop to gain interventional access to causal structure` | `loop-interventional access` | canonicalize | +3 | Standardizes the escape route from on-policy causal confounding. |
| `unnamed the moment when an agent s model updates due to observing a mismatch` | `epistrophe` | canonicalize | +3 | Anchors the Greek terminology for the epistemic update phase. |
| `unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic` | `diagnostic gap matrix` | canonicalize | +3 | Reinforces the name for the core performance diagnostic. |
| `unnamed the property that correction dynamics are approximately isotropic` | `isotropic correction` | rename | +2 | Describes the assumption of uniform correction rates across state dimensions. |
| `unnamed the three part meta pattern structure across the three meta segments` | `meta-pattern triad` | rename | +3 | Formalizes the three meta-patterns: additive-coordinate, identifiability-floor, and separability-pattern. |
| `logogenic logozoetic` | `logogenic / logozoetic distinction` | keep | +3 | Essential dividing line in architectural complexity. |
| `adaptive tempo $\mathcal T$` | `adaptive tempo` | canonicalize | +3 | Prose standard for the $\mathcal{T}$ variable. |
| `bretagnolle huber identity` | `Bretagnolle-Huber bound` | keep | +3 | Important external anchor for total-variation bounds. |
| `pi parameterization invariance axiom` | `parameterization invariance axiom` | canonicalize | +3 | Reinforces the adoption of the full phrase over the abbreviation. |
| `strategic in strategic composition` | `strategic` | keep | +2 | Differentiates game-theoretic interaction from cooperative alignment. |
| `AAD acronym` | `AAD` | keep | +3 | Core framework acronym. |
| `OODA boyd` | `OODA loop` | keep | +3 | Anchor to Boyd terminology. |
| `OODA4 agent as act agent logogenic` | `OODA4 classification` | rename | +2 | Boyd-based taxonomy for agent architectures. |
| `aporia prolepsis aisthesis epistrophe praxis` | `Greek-rooted vocabulary` | canonicalize | +3 | Collectivizes the five distinctive process stages. |
| `bruineberg s pearl-blanket friston-blanket` | `Pearl-blanket interpretation` | canonicalize | +3 | Clarifies the exact reading of Markov blankets used in AAD. |
| `calibration laboratory framing for TST` | `software calibration laboratory` | canonicalize | +3 | Solidifies TSTs grounding role. |
| `candidate stage` | `candidate stage` | keep | +2 | Standard segment maturity status. |
| `chronica $\mathcal C_t$` | `chronica` | canonicalize | +3 | Prose standard for the interaction history. |
| `cox s theorem causal hierarchy theorem tikhonov s theorem` | `foundational anchors` | rename | +2 | Identifies the imported theorems the framework rests upon. |
| `derivation not proof` | `derivation` | keep | +3 | Important epistemic distinction for AAD claims. |
| `developer as act agent TST` | `developer-as-agent` | rename | +2 | Core mapping for TST. |
| `discussion segment header` | `Discussion section` | canonicalize | +3 | Standard markdown section header. |
| `discussion segment section` | `Discussion` | canonicalize | +3 | Standard markdown section. |
| `epistemic status segment header` | `Epistemic Status section` | canonicalize | +3 | Standard markdown section header. |
| `epistemic status segment section` | `Epistemic Status` | canonicalize | +3 | Standard markdown section. |
| `exact robust qualitative heuristic conditional claim tiers` | `epistemic claim tiers` | rename | +3 | Formally collectivizes the four levels of rigor. |
| `findings segment section` | `Findings section` | canonicalize | +3 | Standard markdown section header. |
| `formal expression segment header` | `Formal Expression section` | canonicalize | +3 | Standard markdown section header. |
| `formal expression segment section` | `Formal Expression` | canonicalize | +3 | Standard markdown section. |
| `formulation definition result etc segment types` | `segment typologies` | rename | +2 | Defines the document types in the AAD corpus. |
| `hafez $H_b$ miller meta machine bruineberg pearl-blanket` | `external theoretical anchors` | rename | +2 | Grouping of specific prior-art literature. |
| `hafez s $H_b$` | `agent opacity $H_b$` | canonicalize | +3 | Hafez opacity metric applied to adversarial dynamics. |
| `logogenic agents part iii` | `Section III: Logogenic Agents` | canonicalize | +3 | Standardizes section hierarchy. |
| `logozoetic agents part iv` | `Section IV: Logozoetic Agents` | canonicalize | +3 | Standardizes section hierarchy. |
| `lohmiller-slotine contraction metric generalization used in contraction template` | `contraction metric generalization` | rename | +2 | Describes the non-Euclidean extension of sector conditions. |
| `meta segment for separability pattern identifiability floor additive coordinate forcing` | `meta-pattern segments` | canonicalize | +3 | Groups the highest-level architectural observations. |
| `monderer shapley potential games rosen monotone games` | `strategic convergence conditions` | rename | +2 | Covers the sub-scope alpha-prime game theoretic requirements. |
| `not theorem` | `derivation (non-theorem)` | rename | +2 | Clarifies epistemic status. |
| `pearl s causal hierarchy l0 l1 l2 in pearl s own vocabulary` | `Pearl's causal hierarchy` | keep | +3 | Distinction from AADs internal correlation hierarchy. |
| `pearl-blanket vs friston-blanket terminology bruineberg et al` | `Pearl-blanket reading` | canonicalize | +3 | Clarifies the exact reading. |
| `postulate not axiom` | `postulate` | keep | +3 | Standard philosophical boundary definition. |
| `proprium terminology` | `proprium` | keep | +2 | Vocabulary for internal continuous experience. |
| `section header logogenic agents logozoetic agents` | `Section headers (Logogenic/Logozoetic)` | keep | +2 | Formatting artifact. |
| `segment claim file` | `segment file` | rename | +2 | Standard nomenclature for an atomic AAD document. |
| `segment for claim files` | `segment` | rename | +2 | Standard nomenclature. |
| `spike in msc` | `spike` | keep | +3 | Project vocabulary for exploratory work. |
| `structural persistence operational persistence continuity persistence` | `persistence taxonomy` | rename | +3 | Unifies the three distinct usages of "persistence". |
| `temporal software theory TST` | `Temporal Software Theory` | keep | +3 | The full name of TST. |
| `the adaptive cycle as the theory s fundamental unit` | `adaptive cycle (fundamental unit)` | canonicalize | +3 | The core operational loop. |
| `[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]` | `five adaptive cycle phases` | rename | +2 | Collective grouping. [original phrasing: the five cycle phases prolepsis aisthesis aporia epistrophe praxis] |
| `the four views` | `the four views` | keep | +2 | Acknowledged structural perspective. |
| `the three deaths` | `the three deaths` | keep | +2 | Triad of failure modes. |
| `unnamed future segment layer header for the o bp14 derivation audit table` | `derivation audit table` | rename | +2 | Planning artifact nomenclature. |
| `unnamed inevitability core` | `inevitability core` | keep | +2 | Describes the undeniable structural consequences. |
| `unnamed pearl s causal hierarchy level 1 level 2 level 3` | `causal hierarchy levels` | canonicalize | +3 | Standardizing Pearl's nomenclature within AAD. |
| `[concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results]` | `chain-layer anchor` | rename | +2 | Foundation of the coordinate forcing meta-pattern. [original phrasing: unnamed the chain layer anchor role in additive coordinate forcing] |
| `unnamed the family of named ways persistence identifiability can fail` | `identifiability floors` | canonicalize | +3 | Elevates the core limitation meta-pattern. |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | canonicalize | +3 | Standard geometric boundary for survival. [original phrasing: unnamed the persistence region in $(\alpha, \rho, R)$ parameter space] |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | canonicalize | +3 | Same geometric boundary. [original phrasing: unnamed the region in parameter space where sector persistence holds] |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | canonicalize | +3 | Same geometric boundary. [original phrasing: unnamed the sector persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch] |
| `working notes segment header` | `Working Notes section` | canonicalize | +3 | Standard markdown section header. |
| `working notes segment section` | `Working Notes` | canonicalize | +3 | Standard markdown section. |
| `čencov fisher cauchy functional equation shore johnson hobson aczél` | `coordinate-forcing foundational theorems` | rename | +2 | External anchors for the additive uniqueness meta-pattern. |
| `čencov invariance` | `Čencov invariance` | keep | +3 | Key structural property for the Fisher geometry derivation. |
| `ε greedy` | `$\varepsilon$-greedy` | keep | +3 | Standard RL notation. |
| `𝓐 e τ observation ambiguity` | `observation ambiguity $\mathcal{A}$` | canonicalize | +3 | Formal prose notation. |
| `𝓣 adaptive tempo` | `adaptive tempo $\mathcal{T}$` | canonicalize | +3 | Formal prose notation. |
| `AAD AAD internal AAD internally` | `AAD-internal` | keep | +3 | Essential distinction from imported theorems. |
| `AAD theoretical core vs ASF framework` | `AAD vs ASF distinction` | rename | +2 | Clarifies that AAD is the theory while ASF is the application framework. |
| `ASF acronym` | `ASF` | keep | +3 | Agentic Systems Framework. |
| `active salience management` | `active salience management` | keep | +2 | Mechanism of dynamically adjusting what observation matters. |
| `agent classes class 1 2 3` | `goal-entanglement hierarchy` | canonicalize | +3 | Standardizing the previously resolved rename. |
| `auxilia hierarchy` | `auxilia hierarchy` | keep | +2 | Secondary architectural constructs. |
| `backward inference empathy` | `backward inference empathy` | keep | +2 | Logogenic capability to infer state from externalized text. |
| `century scale event log` | `century-scale chronica` | rename | +2 | Applies the rigorous term "chronica" to the informal event log. |
| `claim the proposition the segment carries` | `segment claim` | rename | +2 | Clarifies what a segment is asserting. |
| `class 2 scope exit` | `Class 2 scope boundary` | rename | +2 | The limit where fully merged agents break directed separation. |
| `cognitive fusion` | `cognitive fusion` | keep | +2 | Pathology of merged systems. |
| `crèche creche` | `the crèche` | keep | +3 | The high-margin developmental environment. |
| `eli the agent type` | `ELI agent` | keep | +2 | Legacy or specific instantiated agent type. |
| `epistemic shadow` | `epistemic shadow` | keep | +3 | The unobservable wake left by complex strategies. |
| `gradient causal memory` | `gradient causal memory` | keep | +2 | Mechanism for long-term integration. |
| `honest activation` | `honest activation` | keep | +2 | Activation grounded in valid causal structure. |
| `honesty scope honest scope honesty as architecture` | `scope honesty` | canonicalize | +3 | Core methodological principle of the AAD framework. |
| `inevitability core` | `inevitability core` | keep | +2 | Reaffirmed concept. |
| `loop vs cycle` | `loop vs cycle distinction` | canonicalize | +3 | Separates the physical topology (loop) from the dynamic traversal (cycle). |
| `o t objective` | `objective functional $O_t$` | canonicalize | +3 | Formal prose notation. |
| `purpose purposeful` | `purposeful` | keep | +3 | Key distinction from mere actuation. |
| `section i header adaptive systems under uncertainty` | `Section I: Adaptive Systems` | canonicalize | +3 | Formatting standard. |
| `section iii header agentic composites` | `Section III: Agentic Composites` | canonicalize | +3 | Formatting standard. |
| `structured rich context` | `structured context` | rename | +2 | Replaces "rich" with precise "structured". |
| `substrate independence` | `substrate independence` | keep | +3 | Central assumption of the framework. |
| `the cycle the adaptive cycle the agentic cycle` | `adaptive cycle` | canonicalize | +3 | The standard term. |
| `tier 1 tier 2 tier 3 contraction` | `contraction hierarchy` | rename | +2 | Replaces raw tier numbers with the property they organize. |
| `two condition decomposition of persistence` | `persistence condition decomposition` | rename | +2 | Refers to the split between operational and structural persistence. |
| `u m epistemic unity multi agent` | `epistemic unity $U_M$` | canonicalize | +3 | Formal prose formulation. |
| `u m model uncertainty` | `model uncertainty $U_M$` | canonicalize | +3 | Formal prose formulation. |
| `u o observation uncertainty` | `observation uncertainty $U_o$` | canonicalize | +3 | Formal prose formulation. || `appendices operational domains` | `operational domains (appendices)` | rename | +2 | More descriptive title for the section. |
| `bounded disturbance ga 2 model d` | `Model D bounded disturbance` | canonicalize | +3 | Standardizes the specific disturbance model. |
| `calibration laboratory calibration lab` | `calibration laboratory` | canonicalize | +3 | Consistently uses the full phrase instead of the abbreviation. |
| `calibration laboratory software s role` | `software calibration laboratory` | canonicalize | +3 | Fully qualifies software role. |
| `canonical formulations second ring` | `canonical formulations` | keep | +2 | Retains the epistemic tier designation. |
| `i adaptive systems under uncertainty` | `Section I: Adaptive Systems under Uncertainty` | canonicalize | +3 | Standard section heading formatting. |
| `inevitability core the 15 segments where inevitability is plausible` | `inevitability core` | canonicalize | +3 | The formal group of structurally inescapable segments. |
| `logogenic vs language based RLHF4 based` | `logogenic architecture` | rename | +3 | Replaces technology-specific (RLHF) with structural nomenclature. |
| `sector condition continuous ga 3` | `continuous sector condition` | canonicalize | +3 | Refines the specific GA3 assumption. |
| `teleological unity $U_O$` | `teleological unity $U_o$` | canonicalize | +3 | Standardizes capitalization on the subscript. |
| `unnamed the evidence starvation effect on downstream edges` | `evidence starvation` | canonicalize | +3 | Consolidates this phenomenon under the primary name. |
| `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]` | `contraction over drift principle` | canonicalize | +3 | Final lock-in for the core slogan. [original phrasing: unnamed the projection whose contraction rate must exceed target drift the opus organizing principle slogan] |
| `[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]` | `strengthen-first posture` | canonicalize | +3 | Secures the methodological commitment. [original phrasing: unnamed the strengthen first attempt the improbable meta approach to theory development] |
| `additive coordinate forcing → disc forced coordinates` | `forced additive coordinates` | rename | +3 | More direct name for the segment. |
| `feedforward loop feedback loop` | `feedback loop` | keep | +3 | Standard control vocabulary. |
| `ii actuated adaptation agentic systems` | `Section II: Actuated Adaptation` | canonicalize | +3 | Standard section heading formatting. |
| `integration of four disciplines as the framing of AAD s contribution` | `four-discipline synthesis` | rename | +2 | Concise framing of the framework context. |
| `separability pattern → disc separability ladder` | `separability pattern` | canonicalize | +3 | Restores the more standard term over "ladder". |
| `unnamed the 1 anchor 3 theorem structure in additive coordinate forcing` | `anchor-theorem structure` | rename | +2 | Identifies the specific rhetorical pattern used in these segments. |
| `unnamed the a2 sub scope partition into α₁ α₂ β` | `admissibility regimes (α₁, α₂, β)` | canonicalize | +3 | Maps the specific greek letters to their role as regimes. |
| `unnamed the log additivity result that unifies chain confidence decay evidence starvation and triple depth penalty as instances of the same forcing structure` | `log-confidence additivity` | rename | +3 | Standardizes the mathematical mechanism unifying the three penalties. |
| `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]` | `reconstruction adequacy condition` | canonicalize | +3 | Locks in the boundary test for logogenic persistence. [original phrasing: unnamed the reconstruction adequacy condition for logogenic agents] |
| `unnamed the relationship where $M_t$ quality bounds evaluable complexity of $\Sigma_t$` | `epistemic ceiling` | canonicalize | +3 | Formally adopts the limit on strategy depth imposed by model sufficiency. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `dogmatic convergence limit` | canonicalize | +3 | Names the state where update stops purely from objective certainty. [original phrasing: unnamed the specific moment when $\eta^st 	o 0$ because $U_o 	o 0$ too certain rather than because $U_M 	o 0$ model confident] |
| `unnamed the three depth penalty compounding on strategy chains` | `tripartite chain attenuation` | canonicalize | +3 | Consolidates the compounding cost under the earlier rename. |
| `unnamed the three part meta architecture of AAD formed by the three meta segments` | `epistemic architecture` | canonicalize | +3 | Maps the framework components to the top-level epistemic term. |
| `unnamed the within session vs inter session persistence distinction for logogenic agents` | `operational vs reconstruction persistence` | rename | +2 | Distinguishes the continuous run from the boundary event. |
| `appendices details` | `Appendices: Details` | canonicalize | +3 | Standard markdown section header. |
| `chain confidence decay keep` | `chain confidence decay` | keep | +3 | Core formal result. |
| `contraction hierarchy` | `contraction hierarchy` | keep | +3 | Elevates the tier description. |
| `empirical heuristic discussion third ring` | `heuristic ring` | rename | +2 | Streamlines the epistemic tier designation. |
| `evidence starvation canonicalize` | `evidence starvation` | canonicalize | +3 | Solidifies the primary term. |
| `gemini s analysis paralysis for excessive deliberation` | `deliberation gridlock` | rename | +2 | Formalizes the over-thinking failure mode. |
| `gemini s boyd exponent for adversarial tempo advantage` | `superlinear tempo advantage` | canonicalize | +3 | Formally adopts the scaling property. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `stability-induced myopia` | canonicalize | +3 | Retains the descriptive alias for success-driven failure. [original phrasing: gemini s competency trap for $\eta^st 	o 0$] |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | canonicalize | +3 | Locks in the geometric dead zone over "death". [original phrasing: gemini s epistemic death for the gain collapse unobservable DAG failure] |
| `iii agentic composites` | `Section III: Agentic Composites` | canonicalize | +3 | Standard section heading formatting. |
| `mismatch injection rate $\rho$` | `effective disturbance $\rho$` | canonicalize | +3 | Connects the formal symbol to its primary interpretation. |
| `promote in topological order` | `topological promotion` | rename | +2 | Formalizes the dependency-ordered maturity process. |
| `triple depth penalty canonicalize` | `tripartite chain attenuation` | canonicalize | +3 | Re-adopts the formal descriptive phrase. |
| `unnamed the 2×2 orient cascade diagnostic table` | `diagnostic gap matrix` | canonicalize | +3 | Locks in the diagnostic table name. |
| `unnamed the condition that a strategy DAG s endosymbiont crosses the composite agent scope from below` | `composition threshold crossing` | rename | +3 | Names the dynamic phase transition into a composite. |
| `unnamed the condition that the agent s event observation pairs constitute genuine interventions as opposed to passive associations` | `loop-interventional access` | canonicalize | +3 | Locks in the formal capability term. |
| `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]` | `contraction over drift principle` | canonicalize | +3 | Asserts the fundamental slogan. [original phrasing: unnamed the contraction over drift insight] |
| `unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing` | `meta-pattern triad` | canonicalize | +3 | Solidifies the high-level grouping. |
| `unnamed the pattern where AAD s negative results floors strengthen the machinery that escapes them` | `honest limits principle` | canonicalize | +3 | Affirms that stating boundaries makes the remaining claims stronger. |
| `unnamed the procedure of reading any segment through all three meta segments` | `meta-architectural review` | rename | +2 | Formalizes the reading methodology. |
| `unnamed the set of five conditions under which a2 is derived rather than assumed the sub scope α agent classes` | `sub-scope alpha taxonomy` | rename | +2 | Groups the five derived operator settings. |
| `unnamed the signed coupling structure across all section iii results` | `signed coupling topology` | rename | +2 | Formalizes the distinction between cooperative and adversarial cross-terms. |
| `[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]` | `strengthen-first posture` | canonicalize | +3 | Solidifies the specific methodological approach. [original phrasing: unnamed the strengthen before soften posture applied to apparent overclaims] |
| `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]` | `quality-tempo compound effect` | canonicalize | +3 | Reaffirms the core feedback loop coupling code to agency. [original phrasing: unnamed the virtuous vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity] |
| `value object → def trajectory value` | `trajectory value` | rename | +3 | Shifts focus from the static object to the dynamical trajectory. |
| `what is derived vs what is chosen derivation audit table heading` | `derivation audit table` | canonicalize | +3 | Formally identifies the artifact. |
| `unnamed the meta architecture of the three meta segments` | `epistemic architecture` | canonicalize | +3 | Fourth appearance: locks this in unconditionally. |
| `unnamed the pattern where the agent s optimal update direction is determined by both gain and directional fidelity together` | `coupled update dynamics` | rename | +3 | Formalizes the joint dependence of the update step. |
| `bruineberg s pearl-blanket` | `Pearl-blanket interpretation` | canonicalize | +3 | Distinguishes the AAD usage from Friston. |
| `hafez s h b` | `agent opacity $H_b$` | canonicalize | +3 | Standardizes the opacity metric. |
| `monderer shapley potential games` | `potential game convergence` | rename | +2 | Uses the specific property enabled by Monderer-Shapley. |
| `persistence structural operational continuity` | `persistence taxonomy` | canonicalize | +3 | Asserts the three-part classification of persistence. |
| `hierarchy as repeated word` | `hierarchy` | keep | +2 | Core organizational concept (causal, correlation, convention). |
| `l1 correlation hierarchy prime decoration` | `L1' soft-facilitator mixture` | canonicalize | +3 | Standardizes the L1 prime layer specifically. |
| `unnamed calibration laboratory framing as reusable meta move` | `calibration laboratory` | canonicalize | +3 | Re-adopts the software-TST anchoring metaphor. |
| `[concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results]` | `chain-layer anchor` | canonicalize | +3 | Identifies the foundation of the additive meta-pattern. [original phrasing: unnamed chain layer anchor role in additive coordinate forcing] |
| `unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3` | `diagnostic cascade` | rename | +3 | Names the progressive availability of signals. |
| `[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]` | `orient cascade` | canonicalize | +3 | Maps the specific five-phase execution order. [original phrasing: unnamed cycle phase sequence as whole] |
| `l1` | `Level 1 (Associational)` | canonicalize | +2 | Expands to full definition. |
| `AAD` | `AAD` | keep | +3 | Retain core acronym. |
| `unnamed` | `(resolved unnamed concepts)` | canonicalize | +3 | Placeholder resolution. |
| `persistence overloaded` | `persistence taxonomy` | canonicalize | +3 | Enforces the disambiguation across structural/operational/continuity. |
| `boundary condition` | `boundary condition` | keep | +3 | Standard formal term for limits and constraints. |
| `chronica brief gloss` | `interaction history (chronica)` | rename | +2 | Pairs the Greek term with its English translation for accessibility. |
| `epistemic opacity` | `epistemic opacity` | keep | +3 | Specifically distinct from transition opacity. |
| `loop is level 2 engine der loop interventional access` | `interventional loop property` | canonicalize | +3 | Solidifies the mechanism upgrading L1 to L2. |
| `matrix CIY tensor CIY` | `matrix causal information yield` | rename | +2 | Expands the scalar CIY into full-state spaces. |
| `pearl l1 l2 l3` | `Pearl's causal hierarchy` | canonicalize | +3 | Formally separates Pearl's hierarchy from AAD's internal ones. |
| `pearl-level 2 causal contrast` | `Level-2 interventional contrast` | rename | +2 | More descriptive of the mathematical mechanism. |
| `transition opacity` | `transition opacity` | keep | +3 | The opacity of the world's actual physical transition. |
