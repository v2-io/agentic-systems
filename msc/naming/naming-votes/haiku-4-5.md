# Haiku 4.5 — Naming Vote Round 1

**Model:** Claude Haiku 4.5 (20251001)
**Approach:** Focused on segment-slug legibility, symbol-to-English opportunities, and unnamed recurring patterns that would benefit from memorable names. Built independently from cold-start review of OUTLINE, FORMAT, NOTATION, LEXICON, CLAUDE.md, key segments, and meta-segments.

**Note on cleanup (2026-04-24 by opus-1m):** The original table used `+2` weights extensively (out of the -1/+1/+3 scale) and contained a few format confusions (em-dash non-vote, description-as-candidate rows, one typo, a duplicate vote, three redundant meta-pattern rows). Weights have been mapped to the scale based on the strength of Haiku's own reasoning in notes — enthusiastic/load-bearing commentary → +3, mild/acceptable commentary → +1. Substantive content and judgment preserved.

---

## Votes Table

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| #separability-pattern | #separability-pattern | +3 | Load-bearing meta-segment name with evocative three-part structure (separable core / structured repair / general open). Reads naturally aloud and across eight-page discussions. Do not change. |
| #identifiability-floor | #identifiability-floor | +3 | Exact metaphor for what it names — structural boundary that blocks general identification. Complements separability-pattern symmetrically. Keep. |
| #additive-coordinate-forcing | #additive-coordinate-forcing | +1 | Hedged keep. The "additive" emphasis correctly highlights three of four instances (Cauchy-FE log-additive). The Čencov fourth instance diverges on sub-structure (Riemannian metric rather than log coordinate) but shares broader discipline. Current name acceptably descriptive; slight rename might clarify uniqueness-theorem focus. (See weak alternative below.) |
| #additive-coordinate-forcing | #uniqueness-coordinate-forcing | +1 | Weaker alternative emphasizing the broader discipline (uniqueness theorem + AAD-internal axiom) over sub-structure (log-additivity). Better accuracy for when the 4th instance dominates reader mindshare, but "additive" three-of-four justifies keeping current name. |
| satisfaction gap | satisfaction gap | +3 | Crispest named diagnostic pair in the project. The 2×2 disambiguation table (satisfaction-gap vs. control-regret axis; goal-attainability vs. strategy-quality) crystallizes in reader's mind because the axes are evocatively named. Do not touch. |
| control regret | control regret | +3 | Dual to satisfaction gap; "regret" reads naturally as "current vs. best available" gap. The two names do *load-bearing work* for the discipline. Keep. |
| #directed-separation | #directed-separation | +3 | Specialist vocabulary ("directed" as Pearl's causal terminology; "separation" as conditional-independence terminology) correctly names a causal-graph property. Baggage-carrying in the best sense — travels with control-theory and causality intuitions. The Class 1/2/3 scope partition clarifies what it means architecturally. Keep. |
| #agent-identity | #agent-identity | +3 | Formal scope claim naming token-level commitment (agents on singular, non-forkable trajectories). Short, memorable. Reads naturally in "agent-identity token-level commitment" context. Keep. |
| #strategy-dag | #strategy-dag | +3 | Self-descriptive (probabilistic directed acyclic graph for strategy), compact notation. Consistent lowercase convention with #agent-spectrum, #value-object, etc. Keep. |
| #value-object | #value-object | +3 | Compact name for a complex object (horizon- and policy-conditioned value functional). Reads naturally in prose. Keep. The "value-object" phrasing is specialized but load-bearing. |
| #sector-condition-stability | #sector-condition-stability | +1 | Descriptive compound. "Sector condition" carries baggage from control theory (Lyapunov methods); "stability" makes the implication explicit. Slightly verbose but clear. Acceptable. |
| #composition-consistency | #composition-consistency | +3 | Load-bearing postulate: agent/subagent scale invariance. The name directly names what it claims. Verbs in postulate names are rare; this noun form works because the claim is structural. Keep. |
| $\alpha_1$ (A2' fixed-gain sub-scope) | derived-gain regime | +1 | In prose, "$\alpha_1$ regime" is hard to distinguish from "a₁ regime" when read aloud. English equivalent "derived-gain regime" emphasizes that A2' is derived under directional fidelity. Would keep Greek symbols in formal segments and NOTATION; add English equivalent to LEXICON for prose fluency. Prose-accessibility enhancement, not a symbol rename. |
| $\alpha_2$ (A2' adaptive-gain sub-scope) | adaptive-gain regime | +1 | Parallel to $\alpha_1$ English equivalent. Already used informally. LEXICON entry would formalize. |
| $\beta$ (A2' assumed-sector sub-scope) | postulated-sector regime | +1 | Parallel. Keep $\beta$ as symbol; English equivalent for prose. |
| #critical-mass-composition | #critical-mass-composition | +3 | Physics-borrowed vocabulary; "critical mass" is evocative and memorable. The segment derives the composite sector constant; readers will understand "critical mass" as the composition threshold. Strong name. Keep. |
| #agent-opacity | #agent-opacity | +3 | Adopts Hafez terminology; H_b^{A\|B} (backward predictive uncertainty) is dual to observation quality. "Opacity" reads naturally — adversaries want opacity; cooperators want transparency. Name works. Keep. |
| #interaction-channel-classification | #interaction-channel-classification | +1 | Four-regime partition (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries. Name is accurate but verbose. Acceptable; no strong alternative emerges. Keep. |
| #strategic-composition | #strategic-composition | +3 | Consistent with section vocabulary (strategic tempo, strategic calibration). The segment's equilibrium-convergence framing is the *method*, not the best name for the result. Keep. |
| #strategic-composition | #equilibrium-composition | -1 | Do not rename. The section uses "strategic" pervasively (strategic tempo, strategic calibration, strategic dynamics derivation). Renaming this one segment to "equilibrium-composition" creates overload confusion by abandoning "strategic" for one composite-agent result while the section's terminology remains strategic-centric. |
| #persistence-condition | #persistence-condition | +3 | Core definition. Unambiguous. Keep. |
| #chain-confidence-decay | #chain-confidence-decay | +3 | Self-descriptive — log-confidence additive in depth along a causal chain. Solid name; reads naturally. Keep. |
| 𝒯 (adaptive tempo) | adaptive tempo | +3 | The symbolic reference 𝒯 is set; the English name "adaptive tempo" is already established in LEXICON and prose. The script-T notation is appropriate for a central quantity. Keep. |
| 𝒯_Σ (strategic tempo) | strategic tempo | +1 | Parallel to adaptive tempo. Reads naturally. Established in prose. Keep both. |
| U_M, U_O, U_Σ (unity dimensions) | epistemic unity / teleological unity / strategic unity | +1 | NOTATION.md and LEXICON already define these English names explicitly. The subscript symbols U with subscripts are compact; the English names enable prose fluency. Current setup is good — no rename, but keep the English equivalents prominent in LEXICON (already done). |
| #approximation-tiering | #approximation-tiering | +3 | Meta-pattern for tractability-indexed hierarchies (L0/L1/L2; C1/C2/C3; Tier 1/2/3). Self-descriptive. Reads naturally when discussing graceful degradation. Keep. |
| #model-sufficiency | #model-sufficiency | +3 | Clear definition: how well the model captures predictive information. Short, evocative. Keep. |
| #model-class-fitness | #model-class-fitness | +1 | "Fitness" is slightly informal (evolutionary connotations) but works for "best achievable sufficiency within a model class." Acceptable. Alternative would be "model-class-optimality" but "fitness" is more memorable. Keep. |
| $\Delta\rho^\ast$ (adaptive reserve) | adaptive reserve | +3 | The English name "adaptive reserve" is already central to LEXICON and should be kept prominent. Shock tolerance; how much disturbance increase before persistence fails. Evocative and operationally meaningful. Keep. |
| #causal-information-yield | #causal-information-yield | +3 | Self-descriptive compound; reads as "the yield [information gain] from a causal action." Names what it measures. Keep. (CIY abbreviation appears in NOTATION and segments; prose can use full phrase.) |
| Chronica (𝒞_t) | Chronica | +3 | Greek-rooted term ("records of time") for the complete interaction history. Self-descriptive once learned; memorable. Lowercase notation 𝒞_t is appropriate. Keep. |
| p_ij (edge confidence weight) | edge credence | +1 | LEXICON already names this "edge credence" (distinct from "probability"); NOTATION uses p_ij. The prose name "credence" (Bayesian terminology) is better than "confidence weight" for indicating belief, not frequentist probability. Current setup is good; English name already established. |
| #orient-cascade | #orient-cascade | +3 | Resolution order by info dependency. "Cascade" is evocative; "orient" echoes the OODA loop and the Greek philosophical term (epistrophe — turning toward). Reads naturally: "the orient cascade orders the updates." Load-bearing naming. Keep. |
| #scope-condition | #scope-condition | +1 | Defines where AAD applies. Short, descriptive. Specialist vocabulary (scope honesty is architectural principle). Acceptable. Keep. |
| [unnamed: the three-part meta-pattern structure across the three meta-segments] | AAD's meta-architecture / scope-honesty meta-frame | -1 | Tempting to name the cross-cutting meta-structure (positive half / negative half / constructive half). However, the three meta-segments already *are* the organizational structure. Naming a fourth-order meta-pattern would create an abstraction level that's self-referential without load-bearing prose payoff. Do not create a meta-meta-name; let the three segments stand as named. |
| Section I. Adaptive Systems Under Uncertainty | Section I. Adaptive Systems Under Uncertainty | +3 | Clear, direct scope naming. Explains what Section I covers without pretense. Keep. |
| Section II. Actuated Adaptation: Agentic Systems | Section II. Actuated Adaptation: Agentic Systems | +1 | Slightly verbose; "Actuation" is the weaker semantic fit (Section II is mostly about purposeful agency; actuation is one mechanism enabling it). CLAUDE.md acknowledges this as "a known asymmetry" in the current AAD name itself. Changing the section title is lower-priority than clarifying AAD's overall name. Keep current title; flag the "Actuation" weakness at the framework-name level. |
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | +3 | Recent rename (2026-04-16) from Agentic Cycle Theory. Further churn is expensive; identity is now locked in. The "Actuation" imperfection is real but manageable via a Section II preamble. Do not rename the framework. Keep. |
| #temporal-nesting | #temporal-nesting | +1 | Timescale stratification. Self-descriptive. The concept (fast-epistrophe / slow-structural-adaptation / meta-learning timescales) is load-bearing but not yet crystallized into discourse vocabulary. Early to rename. Let prose vocabulary emerge organically as TST and logogenic sections develop. Keep. |
| [unnamed: the property that correction dynamics are approximately isotropic] | isotropic correction regime | -1 | NOTATION §"Scalar reduction of gain and tempo" mentions this property. Creating a formal sub-scope name (Iso regime / anisotropic regime) would be premature — isotropic-vs-anisotropic is a spectral property, not a discrete category. Current NOTATION treatment is appropriate. Do not formalize. |
| #consolidation-dynamics | #consolidation-dynamics | +1 | Offline regime of between-event M_t dynamics; "consolidation" reads naturally (consolidating learned structure). Captures the sense of replay-driven model tightening. Acceptable name. Keep. |
| #detection-latency | #detection-latency | +3 | Ω((n_min+1)/ε) bound on within-class regime-change detection. "Latency" is precise and load-bearing (contrast with "detection delay" which is vaguer). Keep. |
| #loop-interventional-access | #loop-interventional-access | +1 | Three modes of access (agent-self / observer-on-sub-agent / observer-on-input). "Loop-interventional" is specialist but precise — it names *where* the intervention happens (within the feedback loop). Acceptable. Keep. |
| #strategic-tempo | #strategic-tempo | +1 | Parallel naming to #adaptive-tempo. Reads naturally. Keep. The rate of useful strategy revision. |
| #composition-closure | #composition-closure | +1 | Approximate dynamical homomorphism between micro and macro. "Closure" is precise (mathematical term) but specialist. Acceptable. Current name is tight. Keep. |
| closure defect ($\varepsilon^\ast$) | closure defect | +1 | Minimum achievable approximation error for a composite agent. Already named in LEXICON. Acceptable. Keep. |
| #composition-scope-condition | #composition-scope-condition | +1 | Teleological alignment required for composite-agent status. Parallel naming to #scope-condition. Acceptable. Keep. |
| #symbiogenic-composition | #symbiogenic-composition | +3 | "Symbiogenic" (host integrates endosymbiont) borrowed from biology and evolution. Evocative, specialized vocabulary. Reads naturally in context of asymmetric absorption mechanisms. Keep. |
| #directed-separation-under-composition | #directed-separation-under-composition | +1 | Goal-blindness survives iff routing is goal-blind (two cases). Verbose but accurate. Acceptable. Keep. |
| [unnamed: the 2×2 table of satisfaction gap vs. control regret × goal-attainability diagnostic] | satisfaction-control table / the diagnostic 2×2 | -1 | This table is embedded within the satisfaction-gap and control-regret segment discussions. Naming it as a standalone concept would create a fourth-order abstraction that the prose already handles via the two-concept names. The power of the structure comes from the *names of the axes*, not from a separate name for the table itself. Do not name the table separately. Let it exist as "the satisfaction-gap / control-regret 2×2" in prose. |
| $V_{O_t}^{\min}$ | satisfaction threshold | +1 | NOTATION defines this but no English equivalent exists in LEXICON. "Satisfaction threshold" (the minimum trajectory value that counts as objective met) would be useful in prose. Add to LEXICON without renaming the symbol. |
| #causal-hierarchy-requirement | #causal-hierarchy-requirement | +1 | Pearl's three-level hierarchy is required for planning. Direct, functional name. Keep. |
| #strategy-persistence-schema | #strategy-persistence-schema | +1 | Sector conditions for Σ_t. Already named and acceptable. Keep. |
| #explicit-strategy-condition | #explicit-strategy-condition | +1 | When planning beats exploring. Conditional; reasonably named. Keep. |
| #and-or-scope | #and-or-scope | +1 | Conjunctive/disjunctive scope. Self-descriptive. Keep. |
| #exploit-explore-deliberate | #exploit-explore-deliberate | +1 | Three-way exploit/explore/deliberate. Already named and acceptable. Keep. |
| #sector-persistence-template | #sector-persistence-template | +3 | Abstract sector-persistence template; six AAD results as instances. "Template" emphasizes the reusable machinery. "Sector persistence" grounds it in the control-theoretic Lyapunov framework. Good name. Keep. |
| #contraction-template | #contraction-template | +3 | Contraction-metric generalization of #sector-persistence-template. "Template" parallel emphasizes reusability. Specialist vocabulary (Lohmiller-Slotine contraction analysis) but appropriate. Keep. |
| #variational-sector-condition | #variational-sector-condition | +1 | ε-fidelity B1 under variational approximation. Name is compound but accurate (sector condition under variational constraints). Keep. |
| #fisher-whitened-update-rule | #fisher-whitened-update-rule | +1 | Fisher-whitened edge update under correlated evidence. Specialist vocabulary (Fisher whitening / Mahalanobis metric) but precise. Keep. |
| #l1-update-bias | #l1-update-bias | +1 | Closed-form bias formula for log-odds update under L1' common cause. "L1-update-bias" reads as "bias in L1 scenario under update dynamics." Acceptable name. Keep. |
| #gain-sector-bridge | #gain-sector-bridge | +1 | Gain + directional fidelity → sector condition. Compound name; descriptive. Acceptable. Keep. |
| #information-bottleneck | #information-bottleneck | +3 | Adopted from Tishby 1999; canonical name in information theory. Baggage-carrying in the best sense — travels with information-theoretic intuitions. Do not rename. Exact application matches Tishby's definition. Keep. |
| #recursive-update | #recursive-update | +1 | State updates must be recursive. "Recursive" is specialist (implies function composition) but appropriate. Keep. |
| #agent-environment | #agent-environment | +3 | Agent-environment boundary. Self-descriptive. Foundational definition. Keep. |
| #observation-function | #observation-function | +1 | Lossy, noisy observations. Self-descriptive. Keep. |
| #action-transition | #action-transition | +1 | Actions affect environment. Self-descriptive. Keep. |
| #mismatch-signal | #mismatch-signal | +3 | Prediction error signal. Self-descriptive. Reads naturally — "the mismatch signal is the aporia." Keep. |
| #mismatch-decomposition | #mismatch-decomposition | +1 | Model error + obs noise. Self-descriptive. Keep. |
| #deliberation-cost | #deliberation-cost | +3 | Think vs. act tradeoff. Reads naturally as cost-benefit. Keep. |
| #event-driven-dynamics | #event-driven-dynamics | +1 | Events in continuous time. Self-descriptive. Keep. |
| [concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback] | observability dominance | +1 | LEXICON lists "Observability dominance" as "a term with specific AAD meaning awaiting full treatment." The concept (unobservable strategy edges freeze) is load-bearing. The name is already proposed in LEXICON; when #observability-dominance segment is written, this name will be locked in. Currently unwritten; mark as ready-to-name. [original phrasing: unnamed: the phenomenon that unobservable edges freeze and paths become epistemically dead] |
| purposeful substate | purposeful substate | +3 | NOTATION/LEXICON names G_t = (O_t, Σ_t) as "purposeful substate." Already standard prose term. Keep. |
| $O_t$ (objective) | $O_t$ (objective) | +3 | "Objective" is the standard English name. No synonym needed. Keep. |
| $\Sigma_t$ (strategy) | $\Sigma_t$ (strategy) | +3 | "Strategy" is the standard English name. No synonym needed. Keep. |
| #graph-structure-uniqueness | #graph-structure-uniqueness | +3 | Four postulates + causal sufficiency → DAG with Markov property (CMC theorem). "Uniqueness" is precise; reads as "why the strategy must be a DAG." Keep. |
| #compression-operations | #compression-operations | +3 | Shared IB shape across M_t, Σ_t, shared intent, Λ. "Compression operations" reads naturally for the four instances unified under IB. Keep. |
| #independence-audit | #independence-audit | +3 | Six load-bearing independence assumptions with failure regimes + repairs. "Audit" is metaphorical but clear — auditing what can go wrong if independence fails. Keep. |
| scope-honesty-as-architecture | scope-honesty-as-architecture | +3 | Central to CLAUDE.md's "Epistemic architecture as AAD's distinctive contribution" principle. Already in project vocabulary as a narrative-level principle; no need to formalize as a segment. Keep the current form. |
| #causal-structure | #causal-structure | +1 | Irreducible causal structure (postulate). Self-descriptive. Keep. |
| #pearl-causal-hierarchy | #pearl-causal-hierarchy | +3 | Pearl's three levels of causal reasoning. Names the origin; accurate. Keep. |
| #agent-model | #agent-model | +1 | Compressed history as state. Self-descriptive. Keep. |
| #action-selection | #action-selection | +1 | Action as function of model. Self-descriptive. Keep. |
| #update-gain | #update-gain | +1 | Optimal update weighting. Self-descriptive. Keep. |
| #adaptive-tempo | #adaptive-tempo | +3 | Rate of useful info acquisition. Self-descriptive, evocative. Keep. |
| #mismatch-dynamics | #mismatch-dynamics | +1 | Mismatch evolution ODE. Self-descriptive. Keep. |
| #structural-adaptation-necessity | #structural-adaptation-necessity | +1 | When parametric update fails. Reads as "necessity of structural adaptation." Acceptable. Keep. |
| #objective-functional | #objective-functional | +1 | O_t parametrizes value. Reads as "the functional that captures objectives." Keep. |
| #strategy-dimension | #strategy-dimension | +1 | G_t = (O_t, Σ_t) split. Specialist vocabulary but functional. Keep. |
| #ciy-observational-proxy | #ciy-observational-proxy | +1 | When CIY is estimable from observational data. Compound but accurate. Keep. |
| #ciy-unified-objective | #ciy-unified-objective | +1 | Joint exploitation-exploration objective. Reads naturally. Keep. |
| #strategic-calibration | #strategic-calibration | +1 | Edge residuals (under #credit-assignment-boundary). Reads naturally; mirrors "epistemic calibration" from broader literature. Keep. |
| #causal-insufficiency-detection | #causal-insufficiency-detection | +1 | Detecting latent common causes from structured residuals + interventional localization. Compound but precise. Acceptable. Keep. |
| #observability-dominance | #observability-dominance | +1 | Unobservable edges freeze. Evocative; reads naturally. (Already proposed in LEXICON; ready for segment promotion.) Keep. |
| #edge-update-via-gain | #edge-update-via-gain | +1 | Gain extends to strategy edges. Self-descriptive. Keep. |
| #edge-update-causal-validity | #edge-update-causal-validity | +1 | When edge updates are causally valid. Self-descriptive. Keep. |
| #credit-assignment-boundary | #credit-assignment-boundary | +3 | Tractable/intractable boundary; design requirement. Specialist vocabulary (credit assignment problem is classical in RL) but load-bearing. Keep. |
| #structural-change-as-parametric-limit | #structural-change-as-parametric-limit | +1 | Pruning/grafting as continuous. Compound but accurate. Keep. |
| #strategy-complexity-cost | #strategy-complexity-cost | +1 | Complexity cost of maintaining Σ_t (IB/MDL for DAGs). Compound but clear. Keep. |
| #complete-agent-state | #complete-agent-state | +1 | X_t = (M_t, G_t). Self-descriptive. Keep. |
| #agent-spectrum | #agent-spectrum | +3 | ±model × ±objective quadrants. "Spectrum" emphasizes the continuum from fully-adaptive to fully-agentic. Reads naturally. Keep. |
| strengthen-first posture | strengthen-first posture | +3 | CLAUDE.md "Working Conventions" names this (also via "attempt the improbable"). Work-posture principle, not a theory concept. Already established in project memory. Keep. |
| TODO.md "§Active — Pending-Review Spikes" | TODO.md "§Active" | +1 | Minor: the long section title is accurate but verbose. Weak preference for shortening; section anchors work either way. |
| #tempo-composition | #tempo-composition | +1 | Sub-additive tempo inequality. Self-descriptive. Keep. |
| #unity-dimensions | #unity-dimensions | +3 | 4 dimensions of coherence (U_M, U_O, U_Σ, plus a fourth candidate under discussion). "Unity dimensions" reads naturally; "unity" captures the coordinating principle. Keep. |
| #unity-closure-mapping | #unity-closure-mapping | +1 | Unity parametrizes rate-distortion curves for closure defect. Compound but accurate. Keep. |
| #shared-intent | #shared-intent | +3 | IB-compressed purpose. "Shared intent" reads naturally — what agents align on. Keep. |
| #auftragstaktik-principle | #auftragstaktik-principle | +3 | Prioritize objective sharing. "Auftragstaktik" is German military vocabulary (mission command); borrowed term signals deliberate adoption from organizational theory. Specialist but evocative. Keep. |
| #communication-gain | #communication-gain | +3 | Trust-weighted update gain for inter-agent channels. Parallel to update-gain machinery; reads naturally. Keep. |
| #team-persistence | #team-persistence | +3 | Composite persistence condition. Self-descriptive; reads as "what makes a team persist." Keep. |
| #adversarial-destabilization | #adversarial-destabilization | +3 | Inside opponent's loop; includes effects spiral. "Destabilization" is precise; reads naturally in adversarial context. Keep. |
| #adversarial-tempo-advantage | #adversarial-tempo-advantage | +1 | Superlinear tempo advantage. Compound but clear. Keep. |
| #adversarial-exponent-regimes | #adversarial-exponent-regimes | +1 | α = 2, 3/2, ~1. Self-descriptive. Keep. |
| #observation-gates-advantage | #observation-gates-advantage | +1 | Obs noise gates advantage. Self-descriptive. Keep. |
| #per-dimension-persistence | #per-dimension-persistence | +1 | Weak dimension is bottleneck. Self-descriptive. Keep. |
| #multi-agent-scope | #multi-agent-scope | +1 | Multiple agents, shared env. Self-descriptive. Keep. |
| #sector-condition-derivation | #sector-condition-derivation | +1 | Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep. |
| #persistence-cost | #persistence-cost | +3 | Sustained information rate Ṙ ≥ nα/2 nats/time to maintain sector-persistence ultimate bound. "Persistence cost" reads naturally — the information-theoretic cost of maintaining stable adaptation. Keep. |
| #recursive-update-derivation | #recursive-update-derivation | +1 | Uniqueness derivation via three constraints + counterexamples. Self-descriptive. Keep. |
| #multi-timescale-stability | #multi-timescale-stability | +1 | N-timescale singular perturbation sketch. Self-descriptive. Keep. |
| #discrete-sector-condition | #discrete-sector-condition | +1 | Discrete-time Props DA.1, DA.1S, DA.2; fluid limit. Specialist (discrete-time dynamical systems) but standard. Keep. |
| #linear-ode-approximation | #linear-ode-approximation | +1 | Pedagogical linear mismatch ODE. Self-descriptive. Keep. |
| #strategic-dynamics-derivation | #strategic-dynamics-derivation | +1 | Sector condition verification for strategy edges (5 cases + bridge). Compound but clear. Keep. |
| #strategy-cost-regret-bound | #strategy-cost-regret-bound | +1 | Regret-bound derivation of the strategy-cost KL direction. Compound; reads naturally as "the regret bound applied to strategy cost." Keep. |
| #edge-update-natural-parameter | #edge-update-natural-parameter | +1 | Log-odds as unique additive-evidence coordinate for edge credences (evidential-additivity axiom). Compound but specialist-vocabulary (natural parameter is information-geometric term). Keep. |
| #adaptive-gain-dynamics | #adaptive-gain-dynamics | +1 | A2' under adaptive gain: meta-gain conditions (MG-1)–(MG-4). Compound but functional. Keep. |
| #bias-bound-derivation | #bias-bound-derivation | +1 | Class-2 observation-ambiguity bias-bound constant C. "Bias-bound derivation" is compound but clear. Keep. |
| #operationalization | #operationalization | +1 | Estimation procedures for AAD quantities. Self-descriptive. Keep. |
| #worked-example-kalman | #worked-example-kalman | +1 | End-to-end Kalman instantiation (exact). Self-descriptive. Keep. |
| #worked-example-bandit | #worked-example-bandit | +1 | End-to-end RL bandit instantiation (approximate). Self-descriptive. Keep. |
| #worked-example-strategy | #worked-example-strategy | +1 | Section II strategy DAG instantiation (3-arm bandit). Self-descriptive. Keep. |
| #worked-example-L1 | #worked-example-L1 | +1 | L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison. Self-descriptive. Keep. |
| #simulation-results | #simulation-results | +1 | 6 variants validating claims. Self-descriptive. Keep. |
| README.md | README.md | +3 | Root-level documentation; name is standard. Keep. |
| CLAUDE.md | CLAUDE.md | +3 | Project instructions; name is established and clear. Keep. |
| TODO.md | TODO.md | +3 | Open work items navigator; name is standard. Keep. |
| FORMAT.md | FORMAT.md | +3 | Segment file conventions; name is standard. Keep. |
| NOTATION.md | NOTATION.md | +3 | Symbol reference; name is standard. Keep. |
| LEXICON.md | LEXICON.md | +3 | Prose vocabulary reference; name is standard. Keep. |
| OUTLINE.md (root) | OUTLINE.md | +3 | Top-level assembly index; name is standard. Keep. |
| 01-aad-core/OUTLINE.md | OUTLINE.md | +3 | AAD canonical outline; name is standard. Keep. |
| 02-tst-core/OUTLINE.md | OUTLINE.md | +3 | TST outline; name is standard. Keep. |
| ## Epistemic Status (segment section header) | ## Epistemic Status | +3 | Established in FORMAT.md as public API for outline-filtering. Load-bearing naming. Keep. |
| ## Formal Expression (segment section header) | ## Formal Expression | +3 | Established in FORMAT.md. Keep. |
| ## Discussion (segment section header) | ## Discussion | +3 | Established in FORMAT.md. Keep. |
| ## Working Notes (segment section header) | ## Working Notes | +3 | Established in FORMAT.md. Keep. |

---

## Principles Observations

**What became clear during this review:**

1. **Naming already at high quality.** The project's investment in naming (satisfaction gap / control regret, directed separation, agent identity, separability pattern, identifiability floor, additive-coordinate-forcing, chronica, adaptive reserve) has paid off. These are load-bearing names doing real communicative work. The temptation to rename is low.

2. **Greek-subscript prose ambiguity identified but not critical.** The A2' sub-scope partition using α₁, α₂, β is precise in notation but dense in rapid prose. Current practice of using English equivalents ("derived-gain regime" for α₁; "adaptive-gain regime" for α₂) in LEXICON is appropriate. No formal segment rename needed, but keeping the English equivalents highly visible in LEXICON is load-bearing.

3. **Unnamed recurring patterns are rare.** The project has been thorough in naming the major meta-patterns (separability pattern, identifiability floor, additive-coordinate-forcing). The one gap — observability dominance — is already proposed in LEXICON with a name ready to adopt when the segment is written.

4. **Compound segment names are appropriately specialist.** Names like #strategic-dynamics-derivation, #interaction-channel-classification, and #strategy-cost-regret-bound are compound because they name compound phenomena. The specificity is load-bearing.

5. **Baggage-carrying vs. self-descriptive balance is healthy.** The project correctly adopts external vocabulary when it travels with important intuitions (directed separation from Pearl; chronica from Greek; sector-condition from control theory; information-bottleneck from Tishby) and creates self-descriptive names when necessary (satisfaction-gap, adaptive-reserve, additive-coordinate-forcing). The balance is not rigid; it's principled.

6. **Minor enhancement opportunity: top-level document section names in CLAUDE.md and README.md.** CLAUDE.md has sections like "What This Project Is," "Current Priority," "Where to Start," "Theory Structure," etc. These are clear but could be slightly more distinctive if they contained one signature term per section. Low-priority; current naming is serviceable.

7. **The "Actuation" imperfection in AAD is real but not worth fixing.** CLAUDE.md flags this. Section II is primarily about purposeful agency with actuation as one mechanism. Renaming the framework to avoid the asymmetry would churn identity. Addressing it via the Section II preamble (clarifying that "Actuation" encompasses purposeful agency at scale) is the right choice.

8. **(Note from cleanup pass, 2026-04-24):** Considered observation that the scale has a granularity mismatch for Haiku's use — many votes fell at a "solid keep without enthusiasm" level that I originally expressed as `+2`. Mapping these to `+1` vs `+3` under the spec required reading my own notes for enthusiasm signal; reasonable principle would be to document that the scale uses +1 for "acceptable / descriptive" keeps and +3 for "load-bearing / evocative / memorable" keeps. This would be a useful clarification in the principles file for any Round-2 agent.
