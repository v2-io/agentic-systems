# WORKBENCH — ACT Theory Development

Working notes for theory development. This is a thinking tool, not a
reference document. For the canonical theory structure, see
`CURRENT-FULL-THEORY.md`.


## Segment Status

### Written — Section I (28 segments, all written)
| Slug | Type | Notes |
|------|------|-------|
| [temporal-optimality](src/temporal-optimality.md) | Axiom | Needs review |
| [agent-environment](src/agent-environment.md) | Definition | Needs review |
| [observation-function](src/observation-function.md) | Definition | Needs review |
| [action-transition](src/action-transition.md) | Definition | Needs review |
| [scope-condition](src/scope-condition.md) | Scope | Needs review |
| [composition-consistency](src/composition-consistency.md) | Axiom | Scale invariance requirement. Source: spike-agent-composition.md §1, §9. |
| [agent-model](src/agent-model.md) | Formulation | Needs review |
| [information-bottleneck](src/information-bottleneck.md) | Formulation | Needs review |
| [model-sufficiency](src/model-sufficiency.md) | Definition | Needs review |
| [model-class-fitness](src/model-class-fitness.md) | Definition | Needs review |
| [causal-structure](src/causal-structure.md) | Axiom | Needs review |
| [pearl-causal-hierarchy](src/pearl-causal-hierarchy.md) | Definition | Needs review |
| [chronica](src/chronica.md) | Definition | Needs review |
| [event-driven-dynamics](src/event-driven-dynamics.md) | Formulation | Needs review |
| [recursive-update](src/recursive-update.md) | Derived | Needs review |
| [action-selection](src/action-selection.md) | Derived | Needs review |
| [mismatch-signal](src/mismatch-signal.md) | Definition | Needs review |
| [mismatch-decomposition](src/mismatch-decomposition.md) | Theorem | Needs review |
| [update-gain](src/update-gain.md) | Empirical | Needs review |
| [causal-information-yield](src/causal-information-yield.md) | Definition | Needs review |
| [adaptive-tempo](src/adaptive-tempo.md) | Definition | Needs review |
| [mismatch-dynamics](src/mismatch-dynamics.md) | Hypothesis | Needs review |
| [deliberation-cost](src/deliberation-cost.md) | Derived | Needs review |
| [persistence-condition](src/persistence-condition.md) | Theorem | Needs review |
| [sector-condition-stability](src/sector-condition-stability.md) | Theorem | Needs review |
| [structural-adaptation-necessity](src/structural-adaptation-necessity.md) | Theorem | Needs review |
| [temporal-nesting](src/temporal-nesting.md) | Derived | Needs review |
| [agent-identity](src/agent-identity.md) | Discussion | Needs review |

### Written — Section II (20 of 20 segments — all written)
| Slug | Type | Notes |
|------|------|-------|
| [agent-spectrum](src/agent-spectrum.md) | Definition | Needs review |
| [complete-agent-state](src/complete-agent-state.md) | Formulation | X_t = (M_t, G_t) lift. Backward-compatible with Section I. |
| [objective-functional](src/objective-functional.md) | Definition | O_t → V_{O_t}: trajectories → ℝ. Fills TF-08's "value" gap. |
| [value-object](src/value-object.md) | Definition | V_O, Q_O with continuation convention. Extends policy objective with λ(M_t, O_t, N_h). |
| [strategy-dimension](src/strategy-dimension.md) | Definition | G_t = (O_t, Σ_t). Evaluation vs guidance. Independence of richness dimensions. |
| [causal-hierarchy-requirement](src/causal-hierarchy-requirement.md) | Derived + Scope | Level 2 for Q_O evaluation. Scope: agents that learn during operation. |
| [loop-interventional-access](src/loop-interventional-access.md) | Derived | Loop generates interventional data by construction. |
| [explicit-strategy-condition](src/explicit-strategy-condition.md) | Normative | Cost inequality for explicit Σ_t. Makes temporal-optimality load-bearing. |
| [chain-confidence-decay](src/chain-confidence-decay.md) | Derived | Log-confidence additive in depth. p^n is special case. |
| [and-or-scope](src/and-or-scope.md) | Scope | AND/OR restriction. Noisy-OR and WEIGHTED rejected. Parsimony argument. |
| [strategy-dag](src/strategy-dag.md) | Definition | Σ_t = (V, E, p, γ). Acyclicity derived. Edge semantics as causal credence. |
| [directed-separation](src/directed-separation.md) | Derived + Scope | f_M is G_t-independent. Scope condition for goal-conditioned agents. |
| [satisfaction-gap](src/satisfaction-gap.md) | Definition | δ_sat with disambiguation table. A_O (attainability) defined here. |
| [control-regret](src/control-regret.md) | Definition | δ_regret. 2×2 diagnostic with satisfaction gap. |
| [strategic-calibration](src/strategic-calibration.md) | Definition | Edge residuals. Discussion-grade aggregation. |
| [orient-cascade](src/orient-cascade.md) | Derived | Resolution order from information dependency. G_t bounded by M_t. |
| [observability-dominance](src/observability-dominance.md) | Derived | Low σ → frozen edges → epistemically dead paths. |
| [edge-update-via-gain](src/edge-update-via-gain.md) | Hypothesis | Gain principle extended to edge credences. Signal function open. |
| [structural-change-as-parametric-limit](src/structural-change-as-parametric-limit.md) | Formulation | Six operations from reweighting to full restructure. |
| [strategy-persistence-schema](src/strategy-persistence-schema.md) | Proposed schema | Sector conditions for Σ_t. Schema, not theorem — needs instantiation. |

### Written — Section IV (20 segments; 4 missing, 0 old remain)
| Slug | Type | Notes |
|------|------|-------|
| [software-scope](src/software-scope.md) | Scope | Needs review |
| [feature-definition](src/feature-definition.md) | Definition | Needs review |
| [specification-bound](src/specification-bound.md) | Theorem | Needs review; written by earlier agent with less context. Includes communication-as-bottleneck corollary. |
| [change-expectation-baseline](src/change-expectation-baseline.md) | Derived | Median not expectation — key finding. Includes investment-scaling corollary. |
| [comprehension-time](src/comprehension-time.md) | Definition | Needs review |
| [implementation-time](src/implementation-time.md) | Definition | Needs review |
| [dual-optimization](src/dual-optimization.md) | Derived | Turnover multiplier |
| [change-investment](src/change-investment.md) | Derived | Pairwise threshold from dual-optimization. Compound effects are hypothesis, not derived. |
| [conceptual-alignment](src/conceptual-alignment.md) | Hypothesis | Includes realignment-as-feature corollary. Functional form ungrounded. |
| [atomic-changeset](src/atomic-changeset.md) | Definition | |
| [changeset-size-principle](src/changeset-size-principle.md) | Empirical | Includes comprehension-follows-changeset corollary (hypothesis). |
| [change-distance](src/change-distance.md) | Definition | |
| [change-proximity-principle](src/change-proximity-principle.md) | Derived + Hypothesis | Qualitative derived; functional form hypothesis. |
| [exponential-cognitive-load](src/exponential-cognitive-load.md) | Hypothesis | ACT deliberation-cost suggests dependency-structure model, not fixed exponent. |
| [system-coupling](src/system-coupling.md) | Definition | Causal (interventional) interpretation via git. |
| [system-coherence](src/system-coherence.md) | Definition | |
| [coherence-coupling-measurement](src/coherence-coupling-measurement.md) | Measurement | Ratio form is one possible aggregation. |
| [principled-decision-integration](src/principled-decision-integration.md) | Derived | General form of dual-optimization with per-feature P(F_i). |
| [system-availability](src/system-availability.md) | Definition | Standard reliability engineering. |
| [continuous-operation](src/continuous-operation.md) | Scope | Extends temporal optimization to include operational failures. |

### Written — Section III (13 of 13 segments — all written)
| Slug | Type | Notes |
|------|------|-------|
| [multi-agent-scope](src/multi-agent-scope.md) | Scope | Coupling through shared environment. |
| [composition-closure](src/composition-closure.md) | Formulation | Operationalizes agent boundary as bounded closure defect. Status: conditional (admissibility constraints and norms under-specified). |
| [tempo-composition](src/tempo-composition.md) | Derived | Sub-additive tempo inequality. Status: sketch (proof incomplete — ε*→C_coord mapping open). |
| [unity-dimensions](src/unity-dimensions.md) | Definition | 4 dimensions: epistemic, teleological, strategic, perceptual. Status: discussion-grade. Clausewitz mapping. |
| [shared-intent](src/shared-intent.md) | Definition | IB-compressed purposeful state for inter-agent communication. Status: discussion-grade. |
| [auftragstaktik-principle](src/auftragstaktik-principle.md) | Hypothesis | B_O > B_Σ > B_M. Bungay evidence. Status: discussion-grade. |
| [adversarial-destabilization](src/adversarial-destabilization.md) | Derived | Lyapunov destabilization + effects spiral. From TFT Appendix A, A.3/A.3.1. |
| [communication-gain](src/communication-gain.md) | Hypothesis | Trust-weighted inter-agent gain. From TFT Appendix F, F.2. |
| [adversarial-exponent-regimes](src/adversarial-exponent-regimes.md) | Observation | Three regimes: b=2 (det/coupled), b=1.5 (stoch/coupled), b→1 (non-coupled). From track-b sims. |
| [observation-gates-advantage](src/observation-gates-advantage.md) | Observation | Obs noise collapses advantage; optimal gain partially restores. From track-b Variant E. |
| [per-dimension-persistence](src/per-dimension-persistence.md) | Theorem | Per-dim AR(1) exact to 4 sig figs. Scalar overestimates 72%. From track-b Variant F. |
| [team-persistence](src/team-persistence.md) | Derived | Distributed tempo, cooperative-adversarial ρ decomposition, 3-lever persistence. From TFT F.3. |
| [adversarial-tempo-advantage](src/adversarial-tempo-advantage.md) | Theorem | Superlinear exponent b=2 (det/coupled). Analytical theorem + regime conditions. From TFT Cor 11.2. |

### Written — Appendices (8 segments)
| Slug | Type | Notes |
|------|------|-------|
| [sector-condition-proof](src/sector-condition-proof.md) | Proof | Full Lyapunov proofs (A.1, A.2). |
| [recursive-update-proof](src/recursive-update-proof.md) | Proof | Uniqueness proof + 7 counterexample attacks. |
| [multi-timescale-stability](src/multi-timescale-stability.md) | Sketch | N-timescale singular perturbation framework. |
| [operationalization](src/operationalization.md) | Detail | Estimation procedures for ACT quantities. |
| [worked-example-kalman](src/worked-example-kalman.md) | Worked example | End-to-end exact mapping. |
| [worked-example-bandit](src/worked-example-bandit.md) | Worked example | End-to-end approximate mapping; persistence failure diagnostic. |
| [simulation-results](src/simulation-results.md) | Detail | 6 variants validating/refining Section I predictions. Track-b reference. |
| [graph-structure-uniqueness](src/graph-structure-uniqueness.md) | Proof | 4 axioms → DAG structure. Acyclicity proved; P3→Markov sketch. |

### Not Yet Written — 10 segments remaining

**Section IV (4 missing):**
- `#software-epistemic-properties` — software's 6 unique epistemic properties. Source: old-tst-via-tft-readme.
- `#developer-as-act-agent` — developer as (M_t, O_t, Σ_t). Source: old-tst-via-tft-mapping.
- `#code-quality-as-observation-infrastructure` — code quality → U_o → η* → T. Source: old-tst-via-tft-mapping.
- `#causal-discovery-from-git` — git as interventional data source. Source: old-tst-via-tft-causal-extensions.

**Section V (3 missing — blocked on scope decision):**
- `#ai-agent-as-act-agent` — AI agent as actuated agent (directed separation fails → coupled analysis).
- `#context-turnover` — 100% M_t reset per session.
- `#m-preservation` — external memory as persistent M_t.

**Appendices (3 missing):**
- `#linear-ode-approximation` — pedagogical linear mismatch ODE (detail).
- `#intent-dag-development` — convergence on AND/OR + single-p (aside). Source: 04-intent-dag-consolidated.md.
- `#prior-art-positioning` — Hafez, IBM, BDI, active inference (detail). Source: scratch/02-prior-art-assessment.md.


## Key Spikes

| Spike | Location | Status |
|-------|----------|--------|
| Purposeful agent derivation (v3) | `scratch/spike-v3-purposeful-agent.md` | Section II porting **COMPLETE** — all 20 segments in src/ |
| Agent composition / holon | `scratch/spike-agent-composition.md` | Core insight strong; composition laws are sketches |
| Composition closure | `scratch/spike-composition-closure.md` | Formalized closure defect ε*; promoted to #composition-closure + #tempo-composition |
| Graph structure uniqueness | `scratch/spike-graph-uniqueness.md` | Acyclicity derived; P3→Markov needs tightening |
| Intent DAG consolidated | `scratch/04-intent-dag-consolidated.md` | Canonical DAG reference; converged |
| Prior art assessment | `scratch/02-prior-art-assessment.md` | Hafez/IBM/BDI/active-inference positioning |
| LLM causal access note | `scratch/llm-causal-access-note.md` | Pearl reconciliation; potential intro/paper/blog |
| DAG boundary type closure | `scratch/spike-dag-type-closure.md` | v2; reviewed by Codex; ready for porting |
| Track-b simulations | `scratch/track-b-nonlinear-sims/` | 6 variants, all validated |


## What's Settled

*From convergence testing, spikes, and simulation:*

- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with explicit scope condition for goal-conditioned
  agents)
- $G_t = (O_t, \Sigma_t)$ split (definitional, not timescale-dependent)
- Satisfaction gap / control regret split (replaces simpler
  $\delta_{\text{objective}}$)
- DAG acyclicity derived from temporal ordering (former fragility resolved)
- Composition consistency required (not optional) by scope condition's
  level-independence


## Theory Core

The theory has a small **inevitability core** — segments where mathematical
necessity is the goal and is plausibly achievable — surrounded by
**canonical formulations** (good representational choices, not forced) and
**empirical/heuristic enrichment** (testable claims, design guidance).
Keeping these layers explicit prevents two failure modes: trying to prove
inherently empirical claims, and settling for "formulation" when a theorem
is within reach.

### Inevitability core (~15 segments)

These are the segments where the goal is: "given the prior objects, this is
the *only* compatible form." Mathematical inevitability is the ceiling.

| Segment | Why inevitability is plausible |
|---------|-------------------------------|
| #recursive-update + #recursive-update-proof | Three constraints → unique recursive form. Strongest result in the theory. |
| #mismatch-decomposition | Bias-variance decomposition: mathematical identity once mismatch is defined. |
| #chain-confidence-decay | log(product) = sum(logs). Pure algebraic identity. |
| #persistence-condition | Given sector conditions, the threshold follows by Lyapunov. |
| #sector-condition-stability + #sector-condition-proof | Lyapunov stability theorem applied to the mismatch dynamics. |
| #structural-adaptation-necessity | Parametric update converges within model class; wrong class → structural change necessary. |
| #orient-cascade | Resolution order forced by information dependency (M_t before Σ_t before O_t). |
| #satisfaction-gap / #control-regret | Two gaps are arithmetic once V_ideal, A_O, V_current are defined. The diagnostic value is the insight. |
| #causal-hierarchy-requirement | Application of Bareinboim et al.'s causal hierarchy theorem to Q_O evaluation. |
| #loop-interventional-access | Feedback loop generates interventional data by construction — structural property. |
| #directed-separation | f_M independence from G_t follows from the update structure, given scope condition. |
| #deliberation-cost | Think-vs-act threshold from information-theoretic argument. |
| #composition-consistency | If scope condition doesn't restrict level, predictions at different levels must be compatible. (Needs proof.) |

### Canonical formulations (second ring)

Good representational choices that are motivated but not forced. The
three-question triage (FORMAT.md) answer to "what competing formulation
would also fit?" is "at least one alternative exists." These are where
ACT's *design* lives.

Includes: #complete-agent-state, #objective-functional, #value-object,
#strategy-dimension, #strategy-dag, #and-or-scope, #agent-model,
#information-bottleneck, #event-driven-dynamics, #adaptive-tempo,
#structural-change-as-parametric-limit, #explicit-strategy-condition
(normative, not derived), #composition-closure (operationalizes
 #composition-consistency but is a formulation choice, not the only
possible operationalization), most definitions.

### Empirical, heuristic, and discussion (third ring)

Claims whose ceiling is empirical or heuristic — testable against the
world but not derivable from the formalism. This is NOT a demotion: these
are where ACT becomes falsifiable and useful. Section IV is mostly here.

Includes: #update-gain, #mismatch-dynamics, #edge-update-via-gain,
#strategic-calibration, #communication-gain, #conceptual-alignment,
#exponential-cognitive-load, #changeset-size-principle, most Section IV/V
segments, simulation observations.

### Usage

When developing or reviewing a segment, check which ring it belongs to.
If it's in the inevitability core, the goal is tightening the proof. If
it's a canonical formulation, the goal is explaining the choice and noting
alternatives. If it's empirical/heuristic, the goal is stating falsifiable
predictions and connecting to validation. Don't push segments upward beyond
their ceiling; don't leave core segments at sketch status when a proof is
within reach.

See FORMAT.md "Epistemic Triage" for the three-question diagnostic.


## What's Open

- Action-deliberation-exploration tradeoff (three-way with $\Sigma_t$).
  Existing machinery handles components separately (CIY for explore, δ_regret
  for deliberation trigger). Unified policy objective would need a deliberation
  information value term alongside λ·CIY.
- Strategy tempo formalization ($\mathcal{T}_\Sigma$). Needed for
  strategy-persistence-schema to have quantitative content. Observation
  channels that trigger Σ_t revision identified (orient cascade steps 4-7);
  the rate is not formalized.
- Cognitive cost of $\Sigma_t$ (no $\beta$ analog yet). DAGs don't compress
  the way probability distributions do — the right framework may be closer to
  MDL than IB. Critical for finite-context agents.
- Edge identifiability conditions (resolved in software, open in general)
- P3→Markov step in graph uniqueness (sketch, needs tightening)
- Bridge lemma for composition closure: formally proving small expected
  component-wise errors guarantee bounded trajectory divergence under
  Lipschitz stability conditions.
- Strategy persistence schema → theorem: requires formalizing strategic
  correction function, characterizing $\rho_\Sigma$ (rate of environmental
  causal drift), and verifying sector condition. Substantial Lyapunov work.
- Meta-adaptation of $\Pi$ and $N_h$: can the agent structurally adapt its
  own policy class and planning horizon? Analogous to model-class change
  (TF-10). Satisfaction gap's disambiguation table handles descriptively;
  formal mechanism open.
- DAG boundary type closure — **PORTED to #strategy-dag.** Leaf base
  credence ($p_v$) with temporal indexing, unique root terminal,
  well-formedness constraint, $\hat{P}_\Sigma$ as strategy self-assessment
  distinct from $A_O$, terminal alignment error as experience-only signal.
  Spike at `scratch/spike-dag-type-closure.md` (v2). Terminal alignment
  error ($\delta_\text{align}$) formalization still open.


## Cross-Segment Consistency Issues

- **Low-end examples (thermostat, PID) — RESOLVED.**
  Settled doctrine: the spectrum is about *richness*, not *presence/absence*.
  #agent-spectrum table relabeled from "absent" to "absent or trivial" with
  continuum framing. Thermostat has degenerate M_t and O_t (near origin, not
  truly reactive). PID has degenerate M_t (not "no genuine M_t"). Reflex arc
  is the truly reactive case. #agent-model updated to match. Classification
  question is "rich enough for the machinery?" not "present or absent?"
- **"Section I carries over" compatibility boundary.** After the
  $X_t = (M_t, G_t)$ lift, epistemic machinery transfers cleanly to the
  $M_t$ substate. But #action-selection's derivation of $a_t = \pi(M_t)$
  relied on $M_t$ being *complete* — this is superseded by
  $a_t = \pi(M_t, G_t)$. Noted in #complete-agent-state Discussion.


## Known Fragilities

- Edge semantics claim interventional but update from observational.
  During Section II promotion: consider scoping literal $P(j \mid do(i), M_t)$
  semantics to intervention-rich domains (software), using weaker
  "agent-calibrated causal credence" for the general case. This is a natural
  scope narrowing, not a retreat.
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) —
  now framed correctly: M_t-side quantities remain well-defined regardless;
  directed separation gives the clean factorized update and sequential orient
  cascade. Without it, coupled analysis, not broken theory. Updated in
  #directed-separation, #agent-spectrum, CURRENT-FULL-THEORY.md §II scope.
  Scalar objective scope restriction added to #objective-functional.
- **Section IV → Section I bridge is analogical, not formal.** Git-derived
  metrics (coherence, coupling, Q) are claimed to operationalize Lyapunov
  quantities (α, R, ρ) but no mathematical proof connects them. The chain
  git data → Q → comprehension time → developer tempo → α has empirical
  hypothesis steps. This matters because the operationalization story is
  ACT's main defense against the "unmeasurable quantities" critique. Either
  formalize the bridge or be explicit that it's an empirical research program,
  not a derivation.


## Codex Review Issues (from memory — fixes needed)

1. **State completeness**: Must lift to $X_t = (M_t, G_t)$. $M_t$ becomes
   epistemic substate, not complete state. Foundational.
2. **Level 2 too strong**: Pre-compiled controllers are purposeful at
   Level 1. Scope to agents that must *learn* action consequences during
   operation.
3. **Objective/strategy are independent dimensions**: Don't conflate in a
   single hierarchy. $O_t$ richness and $\Sigma_t$ richness vary
   independently. Split early.
4. **$O_t$ parametrizes TF-08's "value" term**: Cleaner insertion point.
5. **Objective as trajectory functional**: $J$: trajectories $\to \mathbb{R}$
   is genuinely more general than point targets.
6. **Cost inequality for $\Sigma_t$**: Derive need for explicit planning
   from $\text{cost}(\text{plan}) < \text{cost}(\text{explore})$, making
   #temporal-optimality load-bearing.
7. **$p^n$ is the special case**: Robust result is additive log-confidence
   growth.
8. **Strategy persistence is a theorem schema**: Need strategic error state,
   correction operator, disturbance class.
9. **Directed separation is conditional**: $f_M$ is $G_t$-independent, but
   closed-loop $M$ transition depends on $G_t$ through action. Precise claim
   is about update function, not trajectory.
10. **$\delta_{\text{objective}}$ must split into TWO quantities**:
    satisfaction gap + control regret. Without this split, the $O_t$ revision
    cascade doesn't work.

Items 1–10 are addressed in v3 spike. Porting to src/ segments is the
remaining work.


## Ordering Questions

*The current linearization in CURRENT-FULL-THEORY.md may need revision:*

- Should #temporal-optimality move from Section I to Section II? It's about
  specific objectives — arguably an actuated-agent concept, not a general
  adaptive-systems concept. Counter-argument: it applies to Section I agents
  too (a Kalman filter that converges faster is better).

- Should #composition-consistency move earlier or later? Currently at the end
  of Section I foundations, before the dynamics claims. Could go right after
  #scope-condition (it's a direct consequence of scope's level-independence).
  The composition spike argues for early placement.

- Section II ordering: the v3 spike proposes a specific 16-segment
  linearization (§11). Is that still the best ordering after the codex
  review corrections?


## Promotion Priorities (updated 2026-03-12)

The bottleneck is no longer idea generation — it is promotion,
canonicalization, and scope-tightening:

1. ~~**Section II backbone** — DONE.~~ All 20 segments promoted to src/
   and marked draft in CURRENT-FULL-THEORY.md.

2. ~~**Simulation results → ACT-native claims/appendices** — DONE.~~
   adversarial-exponent-regimes, observation-gates-advantage, and
   per-dimension-persistence promoted to src/ as first-class segments.

3. ~~**Section III completion (2 segments)** — DONE.~~
   `#team-persistence` and `#adversarial-tempo-advantage` promoted.
   Section III is now 13/13.

4. ~~**Appendices — graph-structure-uniqueness and simulation-results** —
   DONE.~~ Both promoted. Appendices now 8/11 (3 remaining).

5. **Section V scope decision** — directed separation fails for
   goal-conditioned LLMs (acknowledged). Section V is where the project
   wants to land. Need to decide: is Section V an approximate application
   of current ACT, or does it require a genuine coupled $M_t$/$G_t$
   extension? Currently honest but strategically unresolved.

6. **Section IV remaining 4 segments** — strengthens operationalization
   story. `#software-epistemic-properties`, `#developer-as-act-agent`,
   `#code-quality-as-observation-infrastructure`, `#causal-discovery-from-git`.
   Source material in old-tst-via-tft-* files.

7. **Remaining appendices (3)** — `#linear-ode-approximation`,
   `#intent-dag-development`, `#prior-art-positioning`. Lower urgency.

### Completed non-promotion work (2026-03-12)
- **Systematic overclaiming sweep.** 12 fixes across 10 segment files:
  "formalizes X" / "formal content of" / "This IS" / "proves" language
  shifted to "formal analog" / "consistent with" / "captures the pattern"
  with empirical caveats. README, CLAUDE.md, CURRENT-FULL-THEORY.md also
  updated: "first-principles mathematical theory" → "mathematical
  framework." Operationalization section added to README.
- **README positioning overhaul.** "What ACT Contributes — Honest
  Calibration" with 5-category breakdown. Prior Art section expanded with
  explicit credit to borrowed mathematics. Operationalization section
  addresses the bridge gap across all sections.


## Simulation Findings (Summary)

The track-b simulations (`scratch/track-b-nonlinear-sims/`) are theory-shaping,
not merely confirmatory. They forced regime splits and narrowed claims that the
analytical derivations left ambiguous. Full details in variant result files.

### Adversarial tempo exponent (Variants A–D)
- **Deterministic drift, coupling-dominant**: exponent = 2.0 (confirmed at 1.999). Cor. 11.2 exact.
- **Stochastic AR(1) noise, coupling-dominant**: exponent = **1.5, not 2.0**. Root cause: ODE steady-state scales as $\rho/\mathcal{T}$, but stochastic RMS scales as $\rho/\sqrt{\mathcal{T}}$. This is a fundamental model distinction, not a minor correction.
- **Non-coupling-dominant**: exponent degrades smoothly toward 1.0 as base disturbance increases relative to adversarial coupling. The coupling-dominant qualifier is quantitatively load-bearing.
- **Implication**: Cor. 11.2's squared law is correct but conditional on deterministic coupling dominance. Applications must distinguish whether an opponent's tempo increases systematic drift vs. unpredictability.

### Observation noise (Variant E)
- Observation noise collapses adversarial exponent from ~1.0 to **~0.2** — tempo advantage nearly vanishes.
- Optimal gain (TF-06's $\eta^*$) partially restores it (~0.4) but cannot fully recover.
- Consistent with Boyd's emphasis on Orient quality: faster OODA is worthless with bad observations.

### Anisotropic correction (Variant F)
- Per-dimension persistence theory is **exact** (matches AR(1) prediction to 4 significant figures).
- Scalar tempo **overestimates by ~72%** — the weak dimension is the bottleneck.
- Isotropic allocation beats anisotropic by 13%; targeted adversarial attack on weak dimensions amplifies advantage 17%.
- **Implication**: need per-dimension persistence condition, not scalar $\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$.

### Gain validation (Variant E)
- TF-06's uncertainty ratio principle empirically validated: 52% mismatch reduction with Riccati-optimal gain.

### Hafez bridge (Variant Hafez)
- Bi-predictability $P$ measures coupling *architecture*; ACT mismatch measures *performance*. $P$ cannot detect adversarial dynamics.
- Agency has structural information cost: passive $P = 0.44$, active $P = 0.27$.
- $H_b$ (backward uncertainty / agent opacity) has no direct ACT analog — potential gap for multi-agent work.


## Prior Work Migration Map

All TFT and TST content has been copied into `src/old-*` files. The priors/ submodules are now purely historical. The `old-` prefix means the content is prior work that hasn't been fully ACTualized yet — it may not conform to ACT formatting standards.

### TFT → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| ~~old-tf-readme~~ | ~~TFT overview~~ | **Archived.** Superseded by CLAUDE.md, FORMAT.md. |
| old-tf-00-notation-conventions | Symbol tables, conventions, adaptive loop phases, global assumptions, units, claim registry | **Partially absorbed.** Notation referenced by FORMAT.md. Adaptive loop phases, global assumptions table, claim registry format — ACT should have its own. |
| ~~old-tf-01-scope~~ | ~~Scope definitions~~ | **Archived.** → #agent-environment, #observation-function, #action-transition, #scope-condition. Coupling spectrum now in #causal-structure. |
| ~~old-tf-02-causal-structure~~ | ~~Temporal arrow, chronica, Pearl's 3 levels, recursive update~~ | **Archived.** → #causal-structure, #pearl-causal-hierarchy, #chronica, #recursive-update. |
| ~~old-tf-03-model~~ | ~~Model, IB, sufficiency~~ | **Archived.** → #agent-model, #information-bottleneck, #model-sufficiency. |
| ~~old-tf-04-event-driven-dynamics~~ | ~~Event types, channels, rates~~ | **Archived.** → #event-driven-dynamics. |
| ~~old-tf-05-mismatch-signal~~ | ~~Prediction error, Prop 5.1~~ | **Archived.** → #mismatch-signal, #mismatch-decomposition. |
| old-tf-06-update-gain | Uncertainty ratio, domain validation, gain dynamics, overfitting as miscalibration | **Mostly absorbed** into #update-gain. Domain validation tables and gain dynamics (convergence, reset) richer than ACT segment — enrich then archive. |
| ~~old-tf-07-action-selection~~ | ~~Action as model function, fluency~~ | **Archived.** → #action-selection. |
| ~~old-tf-08-exploration-exploitation~~ | ~~CIY, unified policy objective, query actions~~ | **Archived.** → #causal-information-yield. |
| ~~old-tf-09-deliberation-cost~~ | ~~Prop 9.1, deliberation threshold~~ | **Archived.** → #deliberation-cost. |
| ~~old-tf-10-structural-adaptation~~ | ~~Prop 10.1, destruction-creation, overfitting~~ | **Archived.** → #structural-adaptation-necessity + #model-sufficiency + #model-class-fitness. |
| old-tf-11-tempo-persistence | Temporal nesting table, mismatch ODE, adversarial dynamics, observation quality, per-dimension | **Mostly absorbed** across #adaptive-tempo, #persistence-condition, #sector-condition-stability, etc. Mismatch ODE as named hypothesis, speed-quality substitutability — enrich then archive. |
| ~~old-tf-appendix-a-lyapunov~~ | ~~Props A.1–A.3, Cor A.3.1, full proofs, Prop A.4 sketch~~ | **Absorbed.** → #sector-condition-proof (A.1–A.2), #adversarial-destabilization (A.3, A.3.1), #multi-timescale-stability (A.4). Ready to archive. |
| ~~old-tf-appendix-b-operationalization~~ | ~~Estimation procedures for all TFT quantities~~ | **Absorbed.** → #operationalization. Ready to archive. |
| ~~old-tf-appendix-c-kalman-example~~ | ~~Complete Kalman worked example~~ | **Absorbed.** → #worked-example-kalman. Ready to archive. |
| ~~old-tf-appendix-d-rl-example~~ | ~~Nonstationary bandit worked example~~ | **Absorbed.** → #worked-example-bandit. Ready to archive. |
| ~~old-tf-appendix-e-tft-core~~ | ~~Condensed formal chain~~ | **Archived.** Superseded by CURRENT-FULL-THEORY.md. |
| old-tf-appendix-f-multi-agent | Communication gain, trust, distributed tempo, topology, game theory | **Partially absorbed.** → #communication-gain (F.2 core), #adversarial-destabilization (uses coupling model). **Still needed from F:** distributed tempo → #team-persistence (F.3), topology analysis (F.4), game-theoretic integration (F.5), trust transitivity details, falsification predictions (F.7). Extract as Section III segments get built. |
| ~~old-tf-appendix-g-agent-identity~~ | ~~Non-forkability, clone problem~~ | **Archived.** → #agent-identity. |
| ~~old-tf-recursive-update-proof~~ | ~~Full uniqueness proof~~ | **Absorbed.** → #recursive-update-proof. Ready to archive. |
| old-tf-goal-intent-gap | What TFT lacked (goals/intent) | **Historical.** The gap ACT exists to fill. Can archive when comfortable. |
| old-tf-citations-catalog | TFT reference catalog | **Reference material.** Useful for paper writing. |
| old-tf-novelty-analysis | What's novel in TFT | **Reference material.** Useful for positioning. |
| old-tf-ooda-universal-pattern | OODA as universal adaptive pattern (v7) | **Historical.** Early framing. Can archive when comfortable. |

### TST → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| ~~old-tst-readme~~ | ~~TST overview~~ | **Archived.** Superseded by Section IV of CURRENT-FULL-THEORY.md. |
| ~~old-tst-01-temporal-optimality~~ | ~~T-01~~ | **Archived.** → #temporal-optimality (generalized). |
| ~~old-tst-02-specification-bound~~ | ~~D-01 + T-02 + C-02.1~~ | **Archived.** → #specification-bound, #feature-definition. |
| ~~old-tst-03-evolving-scope~~ | ~~T-03~~ | **Archived.** → #software-scope. |
| ~~old-tst-04-change-expectation~~ | ~~T-04, C-04.1, C-04.2~~ | **Archived.** → #change-expectation-baseline. |
| ~~old-tst-05-dual-optimization~~ | ~~D-02, D-03, T-05~~ | **Archived.** → #comprehension-time, #implementation-time, #dual-optimization. |
| ~~old-tst-06-change-investment~~ | ~~T-06~~ | **Archived.** → #change-investment. |
| ~~old-tst-07-conceptual-alignment~~ | ~~T-07 + C-07.1~~ | **Archived.** → #conceptual-alignment. |
| ~~old-tst-08-changeset-size~~ | ~~D-04, T-08, C-08.1~~ | **Archived.** → #atomic-changeset, #changeset-size-principle. |
| ~~old-tst-09-change-proximity~~ | ~~D-05, T-09, H-09.1~~ | **Archived.** → #change-distance, #change-proximity-principle, #exponential-cognitive-load. |
| ~~old-tst-10-coherence-coupling~~ | ~~D-06, D-07, T-10~~ | **Archived.** → #system-coupling, #system-coherence, #coherence-coupling-measurement. |
| ~~old-tst-11-decision-integration~~ | ~~T-11~~ | **Archived.** → #principled-decision-integration. |
| ~~old-tst-12-continuous-operation~~ | ~~D-08, T-12~~ | **Archived.** → #system-availability, #continuous-operation. |

### TST via-TFT Bridge Material → ACT Mapping

| Old file | Content | ACT status |
|----------|---------|------------|
| old-tst-via-tft-readme | Why the bridge exists, software's 6 unique epistemic properties, key open questions | **Partially absorbed.** The 6 properties → #software-epistemic-properties (outlined). Open questions (observation channel under agent control, 100% turnover, counterfactual replay) feed Section IV/V. |
| old-tst-via-tft-mapping | Detailed TFT→software mapping: environment decomposition, observation channels, action taxonomy, model, mismatch, gain, tempo, persistence, structural adaptation, multi-agent | **Richest single document for Section IV.** Action taxonomy (exploration/probe/query/modify/infrastructure-investment), three-part tempo decomposition, code-quality feedback loop, death spiral formalization — much not yet in ACT segments. |
| old-tst-via-tft-causal-extensions | Explicit causal DAGs in software, interventional reasoning via tests, counterfactual evaluation via git, causal discovery from git, runtime causal models | **Partially absorbed** into #causal-discovery-from-git and #software-epistemic-properties. Detailed treatment of dependency DAG vs empirical DAG, Level 2 channel spectrum, counterfactual machine — largely not in ACT. |
| old-tst-via-tft-reformulated-sketch | S-00 through S-14: complete outline of TST rebuilt on TFT/ACT foundations | **Valuable roadmap** for Section IV work. Shows how each TST claim maps to the ACT framework. The "what's new" and "what's removed" sections are useful for understanding the transformation. |
| old-tst-via-tft-simulation-proposals | 6 simulation proposals ordered by value/effort | **Partially executed.** Sims 1-2 done (track-b). Sims 3-6 remain as future work. |


## Prior Art Positioning & Paper Strategy

*Detailed cross-mapping in `scratch/02-prior-art-assessment.md`.*

**The landscape:** IBM (Miehling et al. 2025) calls for a systems theory of agentic AI — explicitly identifying the void. Hafez et al. (2026) provide a diagnostic metric (bi-predictability $P$) without dynamics or goals. No existing work fills the void. ACT is the most complete response identifiable.

- **Hafez** (bi-predictability $P$): complementary diagnostic, no goals/dynamics. $H_b$ has no ACT analog yet — matters for legibility/coordination.
- **IBM 2025** (systems theory manifesto): calls for what ACT provides. Their open challenges (subgoal emergence, residual control rights) directly addressed by ACT.
- **BDI**: named the parts, no dynamics.
- **Active inference**: closest competitor, different foundation. Expected free energy ≈ ACT's value + $\lambda$ CIY (structural isomorphism, different foundations). ACT grounds exploration in causal information specifically.

**Lead with:** Section I (proved, simulated) + Section II (purposeful-agent derivation). These are where ACT has real substance. Sections III–V are "the theory extends to" demonstrations.

**ACT's contributions — honest calibration:**

1. **The integration itself.** Control theory + causal inference + information
   theory + agent architecture under one framework. The individual pieces are
   mostly known; the synthesis is the contribution. This is worth doing
   (Maxwell unified electricity and magnetism using known equations) but
   should not be presented as discovery of the component parts.
2. **Novel formalizations of known patterns.** The satisfaction gap / control
   regret split applies an established pattern (approximation error vs.
   estimation error, model-class limitation vs. within-class suboptimality)
   to agent self-diagnosis with cascading corrective actions — the 2×2
   diagnostic table and orient cascade ordering are genuinely new
   applications. The feedback loop as Level 2 engine is a useful bridge
   between Pearl and Sutton, with a real additional claim for non-RL agents
   (LLMs get interventional data from the loop despite no internal causal
   architecture).
3. **Known results applied to new domains.** DAG acyclicity from temporal
   ordering is standard in Dynamic Bayesian Networks (unrolling). Timescale
   separation for composition is standard singular perturbation theory.
   Both are useful applications to agent/strategy domains, not discoveries.
   Do not list these as "novel results."
4. **Genuinely open bridges.** The git → Lyapunov operationalization is
   analogical, not formal. There is no mathematical proof that git-derived
   metrics (coherence, coupling, Q) translate to Lyapunov bounds (α, R).
   The chain git data → Q → comprehension time → developer tempo → α has
   empirical hypothesis steps in the middle. This is a real gap, not just
   a presentation issue. Section IV's operationalization story is promising
   but not yet a bridge.
5. **Software as both testbed and recursive instantiation.** This framing
   is genuinely distinctive — no other theory treats software development
   as both the primary operationalization domain and the domain where the
   theory's own agents will operate.

**Discipline:** Don't overclaim. Present as a unifying framework with specific novel results. Be honest about what's integration vs. what's discovery.

**Anticipated critique: "physics envy" / "just renaming."** A serious
external review (Gemini, 2026-03-11) raised this directly: Section I's
gain is the Kalman gain, the Lyapunov proof is standard, the deliberation
threshold is opportunity cost. The review caught the pedagogical scaffold
(linear ODE) and missed the load-bearing structure (sector-condition
framework), read the Kalman exact case and missed the multi-domain
structural claim, and didn't examine Section II's novel results at all.
But the meta-critique is fair: Section I is largely careful synthesis of
known mathematics (Kalman, Lyapunov, IB). The contribution is identifying
these as aspects of a single structure and then building purposeful agency
on top. Presentation implications:

1. **Lead with "unifying framework," not "new mathematics."** The individual
   pieces are mostly known; the synthesis and what it enables (Sections II–V)
   is the contribution. Don't let the presentation suggest the gain formula
   or the Lyapunov proof are discoveries — they are instantiations.
2. **Make the sector-condition framework more prominent than the linear ODE.**
   Casual readers who stop at mismatch-dynamics see the pedagogical scaffold
   and conclude the theory rests on a fluid-limit approximation. The actual
   foundation is the nonlinear Lyapunov analysis, which is robust. Title,
   ordering, and emphasis should guide readers to sector-condition-stability
   before mismatch-dynamics, or at minimum make the relationship unmissable.
3. **Section IV as the operationalization answer.** The charge that α and R
   are unmeasurable outside hardware is answered by Section IV, where
   comprehension time, implementation time, and change rates are measurable
   from git history. This should be prominent in any paper — "here is the
   domain where we can actually measure these quantities" directly addresses
   the strongest version of the critique.
4. **Name the genuinely novel results explicitly.** Readers scanning for "what's
   new" need to find it fast: satisfaction gap / control regret split, DAG
   acyclicity derived from temporal ordering, feedback loop as Level 2 engine,
   composition consistency as structural requirement, the dual persistence
   pattern (individual + composite thresholds). These are not repackaging.


## Governing Objectives

1. **Subsume TFT as the adaptive-systems foundation.** The sector-condition/Lyapunov framework is primary; the linear ODE is pedagogical. TFT is absorbed, not extended.
2. **Derive purposeful agency from first principles.** Start with the simplest abstract purposeful object and derive the need for richer structure from mathematical necessity — specifically from the causal hierarchy theorem.
3. **Make TST a rigorous software-domain instantiation of ACT.** Every claim gets epistemic tagging; ungrounded assertions are derived, retagged, or removed.
4. **Develop multi-agent dynamics to the degree needed for TST grounding.** Cooperative, adversarial, mixed. Not a complete multi-agent theory, but enough for software teams and adversarial dynamics.
5. **Maintain claim-segment structure throughout.** One claim per file, strictly incremental.


## Ungrounded Claims to Resolve

*Claims made or implied in current documents that lack their own derivation. These need to be either grounded, retagged as hypotheses, or removed.*

- "Principled implementation often costs nearly the same as quick" (TST T-06, empirical observation not derived — flagged in contents)
- "Comprehension dominates under high turnover" (TST T-05 implication, structurally motivated but quantitative relationship unformalized)
- "Code complexity accumulation rate" as instance of $\rho$ (needed to connect persistence condition to software maintainability)
- The virtuous/vicious cycle as persistence condition violation (structurally motivated, not formally derived)


## Open Questions

1. Does IB for shared intent produce non-obvious predictions about organizational communication structure?
2. Can the intent DAG handle temporal dependencies (action ordering)?
3. How does 100% context turnover interact with the intent DAG? $O_t$ and $\Sigma_t$ may survive context death even when $M_t$ doesn't.
4. Is there a derivable "comprehension vs action" optimal allocation from the dual-mismatch framework?
5. Can Hafez's $P$ be derived from ACT quantities? Can $\Delta H$ (strategic legibility) enter multi-agent dynamics? ($H_b$ has no ACT analog yet.)
6. Relationship between ACT and active inference's prior preferences?
7. Which physical domains have deterministic vs stochastic $\rho$?
8. Cognitive cost of maintaining $\Sigma_t$ (the $\beta$ analog for strategy).
9. P3→Markov step in graph uniqueness: does state-local revisability strictly force the Markov condition? See `scratch/spike-graph-uniqueness.md`.
10. Whether "code quality as observation infrastructure" is unique to software or an instance of a general pattern (agents modifying their own observation channels).
11. LLM causal access (`scratch/llm-causal-access-note.md`): the loop argument
    (Response 1) is load-bearing. Responses 2–3 (internal representations,
    training-time causal exposure) are interesting but give critics easier
    targets if blended into the canonical theory. Keep the loop argument
    primary; others as discussion/aside.


## Validation (after theory stabilizes)

- Extend nonlinear sims to characterize regime boundaries
- Developer-as-ACT-agent on real codebase (software worked example)
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation
- TST testable predictions: specification bound calibration, coherence-coupling measurement
- Simulations 3–6 from old-tst-via-tft-simulation-proposals (Sims 1–2 done as track-b)
- **Flagship empirical agenda**: software unmaintainability threshold and
  measurement program. Formalize $\mathcal{T}_{\text{team}} > \rho_{\text{total}}
  / \|\delta_{\text{critical}}\|$ with observable precursors. This is where ACT
  could become decisively useful beyond elegant theory.
