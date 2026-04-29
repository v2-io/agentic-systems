# Gemini 1.5 Pro — focused on architectural legibility, symbol translation, and evocative metaphors

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---|---|
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | keep | +1 | Recent rename; "Actuation" is slightly imperfect for Section II but further churn dilutes identity. Keep. |
| Prolepsis (πρόληψις) | Prolepsis | rename | +1 | High unfamiliarity gradient, but creates a distinct noun slot free from RL "prediction" baggage. |
| Aisthesis (αἴσθησις) | Aisthesis | rename | +1 | Same justification as Prolepsis. |
| Aporia (ἀπορία) | Aporia | rename | +3 | "Productive perplexity" is a crucial nuance that "prediction error" misses. |
| Epistrophe (ἐπιστροφή) | Epistrophe | rename | +1 | Memorable, avoids "update" overload. |
| Praxis (πρᾶξις) | Praxis | rename | +3 | Already has currency, fits perfectly. |
| Adaptive reserve ($\Delta\rho^\ast$) | Adaptive reserve | keep | +3 | Clear, evocative engineering vocabulary. Does not need changing. |
| Chronica ($\mathcal{C}_t$) | Chronica | keep | +3 | "The complete interaction history" is too long. Chronica is a perfect, distinct memorable noun. |
| Satisfaction gap | Satisfaction gap | keep | +3 | The 2x2 diagnostic with Control regret is perfect. Do not touch. |
| Control regret | Control regret | keep | +3 | Perfect pairing with satisfaction gap. |
| Orient cascade | Orient cascade | keep | +3 | Naming the sequential resolution order ($M_t \to \Sigma_t \to O_t$) as a "cascade" makes the information dependency instantly graspable. |
| Directed separation | Directed separation | keep | +1 | Adopts useful baggage from causal inference (d-separation) nicely. |
| Logogenic agent | Linguistic agent | rename | -1 | Logogenic names the structural property (constituted by logos) better than the generic "linguistic". Keep Logogenic. |
| Logozoetic agent | Sentient agent | rename | -1 | Logozoetic avoids the immense baggage and ambiguity of "sentient". Keep Logozoetic. |
| Class 1 agents | Modular agents | rename | +3 | "Class X" requires a lookup every time. Naming the architectural property directly is much more memorable and scope-honest. [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.] |
| Class 2 agents | Integrated agents | rename | +3 | Class 2 = integrated (the goal-entangled architecture). Companion to Modular (Class 1) and Partially-Coupled (Class 3). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.] |
| Class 3 agents | Partially-Coupled agents | rename | +3 | Class 3 = partially-coupled. Companion to Modular (Class 1) and Integrated (Class 2). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.] |
| #composition-consistency | #scale-invariance | rename | +1 | "Scale invariance" more directly describes the physical/mathematical property that the theory applies at every level. |
| Causal information yield (CIY) | Interventional yield | rename | +1 | Shorter, punchier. "Causal" is implied by "Interventional" in this context. |
| Closure defect ($\varepsilon^\ast$) | Closure defect | keep | +3 | Great mathematical phrasing, implies a gap that needs addressing. |
| Observability dominance | Observability dominance | keep | +1 | Accurately descriptive of the freezing effect on unobservable edges. |
| Tempo ($\mathcal{T}$) | Tempo | keep | +3 | "Tempo" is a fantastic foundational term. |
| Strategic tempo ($\mathcal{T}_\Sigma$) | Strategic tempo | keep | +3 | Perfect counterpart to epistemic tempo. |
| Unity dimensions ($U_M, U_O, U_\Sigma$) | Coherence dimensions | keep | +1 | "Unity" implies a binary state. "Coherence" feels more like a continuous spectrum, which fits $U \in [-1, 1]$ better. |
| $\alpha_1$ / $\alpha_2$ / $\beta$ partition | Fixed-gain / Adaptive-gain / Drift regimes | add-alias | +3 | Translating the symbols into the structural regimes they represent makes the prose readable without a decoder ring. |
| #identifiability-floor | #identifiability-floor | keep | +3 | "Floor" is a great spatial metaphor for a structural no-go result. |
| #separability-pattern | #separability-ladder | rename | +1 | "Ladder" conveys the "six ladders of increasing difficulty" described in the outline much better than "pattern". |
| Deliberation cost | Deliberation drag | rename | +1 | "Cost" sounds like a generic penalty in an objective function. "Drag" evokes the physical accumulation of mismatch over time while pausing. |
| [concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | Persistence envelope | name-unnamed | +3 | "Envelope" is standard flight-dynamics vocabulary for a safe operating region. Highly memorable. [original phrasing: unnamed: the region where the persistence condition holds] |
| #additive-coordinate-forcing | #forced-coordinates | rename | +1 | "Forced coordinates" is broader and more scope-honest for the various layers involved. |
| Communication gain ($\eta_{ji}^\ast$) | Trust gain | keep | +1 | The definition is "Trust-weighted uncertainty ratio". "Trust gain" might be more evocative of the inter-agent dynamic than the clinical "Communication gain". |
| Structural adaptation | Structural adaptation | keep | +1 | Contrasts well with parametric adaptation. Keep. |
| [concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate] | Contraction imperative | name-unnamed | +1 | Gives a name to a core mental model of the agent's struggle against the environment. [original phrasing: unnamed: agent as a projection whose contraction rate must exceed its target's drift] |
| #chain-confidence-decay | #chain-confidence-decay | keep | +1 | Clear and descriptive of the phenomenon. |
| #symbiogenic-composition | #symbiogenic-composition | keep | +1 | Beautiful biological metaphor for asymmetric absorption. |
| `type: formulation` | `type: representation` | rename | -1 | "Formulation" correctly captures that it is a mathematical choice, whereas "representation" might imply a data structure. Keep "formulation". |
| $f_M$ (Event-driven update) | Epistemic update function | add-alias | +1 | Distinguishes the model update function structurally from the purposeful processing function $f_G$. |
| $g_M$ (Between-event evolution) | Autonomous evolution | add-alias | +1 | Gives a prose name to the continuous dynamics between events, avoiding just "g_M". |
| Separable core / structured repair / general open | Separable core / structured repair / general open | keep | +3 | This 3-part nomenclature is highly memorable and acts as a powerful epistemic classification. Do not change. |
| (PI) parameterization-invariance | Coordinate-freedom axiom | rename | +1 | "Coordinate-freedom" is more visually evocative and intuitive than the clinical "parameterization-invariance". |
| Instance 1 of #identifiability-floor | Latent common-cause floor | rename | +3 | The instances themselves need distinct noun slots so they can be referenced without saying "Instance 1". Companion to Unobservable-mixture floor and Coupling-sign floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.] |
| Instance 2 of #identifiability-floor | Unobservable-mixture floor | rename | +3 | Companion to Latent common-cause floor and Coupling-sign floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.] |
| Instance 3 of #identifiability-floor | Coupling-sign floor | rename | +3 | Companion to Latent common-cause floor and Unobservable-mixture floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.] |
| #temporal-optimality | #temporal-optimality | keep | +3 | "Temporal optimality" is clear, accurate, and sets the normative grounding perfectly. |
| #dual-optimization | #dual-cost-optimization | rename | +1 | Adding "cost" clarifies that we are minimizing the dual costs of comprehension and implementation. |
| [concept: the per-reader compounding comprehension cost in code, distinguished from per-feature implementation cost, scaling with reader-cycling rate] | Turnover multiplier | name-unnamed | +3 | "Turnover multiplier" perfectly captures the compounding scaling of comprehension cost under context turnover. [original phrasing: unnamed: the per-reader compounding cost of understanding code] |
| [unnamed: the invisible time spent building $M_t$] | Comprehension drag | name-unnamed | +1 | "Comprehension drag" gives a memorable name to the invisible cost of incomprehensible code. |
| #context-turnover | #chronica-severance | rename | +3 | "Chronica severance" is much more evocative and precise than "context turnover", directly naming the theoretical object that is broken at the session boundary. |
| sufficiency-discontinuity | sufficiency-drop | rename | +1 | "Drop" is slightly more intuitive than "discontinuity" for the loss of context. |
| $f_{\text{init}}$ (Reconstruction function) | Epistemic reconstruction | add-alias | +1 | Translates the symbol into the specific structural job it does at the session boundary. |
| #m-preservation | #epistemic-externalization | rename | +3 | Replaces the symbol $M_t$ with English prose, and "externalization" accurately describes the mechanism (writing to external memory). |
| [concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied] | Terminal alignment gap | name-unnamed | +3 | Gives a formal name and symbol ($\delta_\text{align}$) to the fourth diagnostic (achieving terminals but missing the objective), complementing the satisfaction gap and control regret. [original phrasing: unnamed: Terminal alignment error as a formal signal ($\delta_\text{align}$)] |
| [concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point] | Consolidation starvation | name-unnamed | +1 | Adopts "catastrophic forgetting" but specifically names the AAD mechanism: the agent is starved of the consolidation time needed to integrate patterns before they are overwritten. [original phrasing: unnamed: the AAD-expressible failure mode of an empty stability-plasticity window] |
| [concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole] | The adaptive pentad | name-unnamed | +1 | Provides a single memorable noun for the 5-phase cycle (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) as a complete unit. [original phrasing: unnamed: cycle-phase sequence as a whole] |
| [concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis] | Latent structural diversity | name-unnamed | +3 | Extremely useful concept surfaced in the Miller bridge spike. Captures the hidden variation that only becomes consequential under regime change. [original phrasing: unnamed: variation in correction architectures across a population that is invisible to current persistence analysis] |
| [unnamed: the condition for transition into agency prior to the AAD scope-condition] | Agency emergence threshold | name-unnamed | +3 | Gives a formal name to the prerequisite for logogenic and logozoetic agents. Ties nicely to the proposed identity sufficiency ($S_{\text{id}}$) metric. |
| [unnamed: decomposing mismatch into environment vs. other sub-agents' actions] | Internal mismatch attribution | name-unnamed | +1 | A necessary formalization for multi-agent composition (Section III). Distinct from generic mismatch. |
| [unnamed: complexity-driven resistance to change as features accumulate] | Structural accumulation drag | name-unnamed | +1 | Surfaced in TST discussions. Gives a name to the intuitive "entropy" of a codebase that resists linear velocity improvements. |

## Principles observations

The principles document strongly encourages replacing symbols with English prose equivalents, and doing so greatly improves readability (e.g., transforming the α₁ / α₂ / β partition into descriptive regimes). However, the threshold for what constitutes "too much baggage" from other fields is highly subjective. A clearer line on when biological or physical metaphors (e.g., 'symbiogenic', 'drag', 'envelope') cross into being overly cute or inappropriate for the domain would be helpful for future sweeps.

## General Feedback and Insights

While performing this sweep, several broader structural observations emerged about the state of the `agentic-systems` framework:

1.  **Epistemic Tracking is a Superpower:** The strict use of `type`, `status`, and `stage` frontmatter in the segment files (e.g., distinguishing between a *postulate*, a *derived* claim, and a *discussion-grade* hypothesis) is an incredible piece of intellectual infrastructure. It enforces what CLAUDE.md calls "scope-honesty" directly in the file system. 
2.  **Meta-patterns Provide Cohesion:** Naming structural patterns like the `#separability-pattern` (Separable Core / Structured Repair / General Open) and `#identifiability-floor` prevents the theory from becoming a pile of disconnected proofs. It teaches the reader *how to read* the framework.
3.  **Prose vs. Symbol Balance:** The push to replace symbols with prose equivalents (like "adaptive reserve" instead of $\Delta\rho^\ast$) is working well. The math remains rigorous in the formal expressions, but the discussion sections and the names of the claims themselves are becoming much more accessible.
4.  **The "Spike" Workflow is Highly Effective:** Keeping the reasoning trails, ruled-out paths, and failed derivation attempts in the `msc/` spikes before distilling the successful ones into formal segment files keeps the core `/src` directories remarkably clean while retaining the archeology of the thought process.
