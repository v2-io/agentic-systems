# Cluster Reference: Structural Adaptation and Temporal Nesting

**Overview:** Proves that when model class fitness degrades, structural adaptation is mathematically forced, and applies singular perturbation theory to dictate the strict timescale separation required for stability.

---

## Canonical Source Segments

### Source: `result-structural-adaptation-necessity.md`

```yaml
---
slug: result-structural-adaptation-necessity
type: result
status: conditional
depends:
  - def-model-sufficiency
  - def-model-class-fitness
  - result-mismatch-decomposition
  - emp-update-gain
stage: claims-verified
---
```


# Result: Structural Adaptation Necessity

When model class fitness is insufficient — when no model in the current class can adequately represent reality — no amount of parametric adaptation can close the mismatch floor. The agent must change its model class, not just its parameters.

## Formal Expression

*[Derived (structural-adaptation-necessity)]*

If the model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ for some $\varepsilon \gt 0$, then no parametric adaptation within $\mathcal{M}$ can reduce the expected mismatch below a floor determined by $\varepsilon$ (under the alignment assumption — see Epistemic Status). Without the alignment assumption, the result holds for irreducible proper-scoring regret rather than one-step mean mismatch. The qualitative conclusion is the same either way: parametric adaptation cannot compensate for model-class inadequacy.

### Derivation

1. By definition, $S(M^\ast) = \mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ where $M^\ast = \arg\sup_{M \in \mathcal{M}} S(M)$.
2. Therefore $I(\mathcal{C}_t; o_{t+1:\infty} \mid M^\ast, a_{t:\infty}) \gt 0$: the history contains predictive information that $M^\ast$ does not capture.
3. This uncaptured information manifests as *systematic* mismatch — structured residuals $\delta_t$ containing signal, not merely noise.
4. From #result-mismatch-decomposition, the model error component has a positive lower bound that cannot be reduced by any $M \in \mathcal{M}$.
5. The update rule ( #emp-update-gain) adjusts $M_t$ within $\mathcal{M}$, but $M^\ast$ is already (approximately) reached. Further updates oscillate without net improvement.
6. Therefore: reducing mismatch below the floor requires changing $\mathcal{M}$ — structural adaptation. $\square$

**Corollary.** Persistent irreducible mismatch (after parametric convergence) is *diagnostic* of model class inadequacy. Systematic patterns in residuals are evidence that $\mathcal{F}(\mathcal{M})$ is insufficient.

## Epistemic Status

*Conditional.* The step from "lost predictive information" (step 2) to "systematic one-step mismatch" (step 3) requires an alignment assumption: that the lost predictive information affects the one-step conditional mean, not just higher moments. #result-mismatch-decomposition explicitly flags this: insufficiency implies positive model error under the alignment assumption, or positive proper-scoring regret without it. As written, the result is conditional on this alignment assumption. Without it, the conclusion should be stated in terms of proper-scoring regret (the best model in $\mathcal{M}$ has irreducible regret relative to the optimal predictor) rather than one-step mismatch magnitude. The qualitative conclusion — parametric adaptation cannot compensate for model-class inadequacy — holds either way; the quantitative mechanism differs.

## Discussion

**Structural adaptation as structural persistence failure.** When the model class is inadequate, the effective $\alpha$ in the sector condition shrinks — the correction function cannot point inward strongly enough because the model class lacks the capacity to represent the correct direction. This is a failure of *structural persistence* (see Persistence in `LEXICON.md`): the machinery's capacity to outpace disturbance degrades not because disturbance increased or tempo decreased, but because the correction function itself has become less effective. The remedy is not faster cycling (operational) or identity preservation (continuity) but a change of model class.

**Observable symptoms of model class inadequacy.** When $\mathcal{F}(\mathcal{M})$ is low:

1. **Persistent irreducible mismatch**: $\Vert\delta_t\Vert$ remains large despite extended updating — the model has converged within $\mathcal{M}$ but the best achievable model is still poor.
2. **Gain collapse without performance**: $\eta^\ast$ has decreased (model appears confident) but predictions remain inaccurate — the model is confidently wrong, having fitted to structure in $\mathcal{M}$ that doesn't match reality.
3. **Systematic mismatch patterns**: $\delta_t$ shows structure (correlations, trends, periodicities) that the model class cannot represent — the residuals contain signal that $\mathcal{M}$ lacks the capacity to absorb.

**Structural overfitting: the opposite failure mode.** $\mathcal{M}$ can also be *too expressive*, causing the model to memorize irreducible noise. Symptoms: low training mismatch but high generalization mismatch; model complexity growing without predictive gain; $\eta^\ast \to 0$ (confident) but confidence is spurious. The information bottleneck ( #form-information-bottleneck) provides the diagnostic: when marginal increases in model complexity yield no marginal predictive power, the model is past the optimal point on the rate-distortion curve. Structural adaptation in this case means *compression* — moving to a simpler $\mathcal{M}'$. Structural adaptation is bidirectional: expansion when too constrained (this proposition), compression when too expressive.

**Mechanisms of structural change.** Structural adaptation can proceed by:

- **Decomposition and recombination**: Tearing apart existing structure and synthesizing new configurations from the pieces. Boyd's "Destruction and Creation" insight; Kuhn's paradigm shifts; Popper's conjecture and refutation.
- **Expansion**: Adding new representational capacity without destroying existing structure. Bayesian nonparametrics, growing neural architectures, organizational expansion.
- **Compression**: Removing unnecessary structure while preserving the predictive core. Regularization, Occam's razor, organizational streamlining.
- **Grafting**: Incorporating external structure. Transfer learning, acquiring a company, consulting an expert. Query actions ( #def-causal-information-yield) are a primary conduit for grafting.

The severity of structural change needed depends on *how far* the current model class is from adequacy. Minor regime changes may require only expansion or grafting; fundamental shifts where $\mathcal{M}$'s assumptions are violated may demand full decomposition.

**Neutral variation as a mechanism for structural change.** In multi-agent settings, structural adaptation can proceed without any individual agent deliberately restructuring. Miller (2022, *Ex Machina*) identifies a five-phase "extreme transition motif" in coevolving automata: (1) stable epoch, (2) an environmentally neutral variant — structurally different but behaviorally identical under current conditions — appears, (3) the variant drifts to nontrivial proportion through stochastic reproduction, (4) the variant's latent structural differences create a niche that a new mutant in the opposing population exploits, triggering a self-reinforcing cascade, (5) both populations rapidly transition to a new regime and consolidate. This mechanism bridges the gap between "many incremental changes" and "radical restructuring" — the restructuring is radical in its effect but incremental in its causes, with neutral drift providing the bridge. The concept of *latent structural diversity* — variation in agent architectures that is invisible to current performance but consequential under regime change — is a composition-level property that Section III's dynamics framework should formalize.

**The cost of structural change.** Structural adaptation is expensive: knowledge loss (parameters learned within $\mathcal{M}$ may not transfer), temporary performance drop (new model starts uncertain), search cost (finding good $\mathcal{M}'$), coordination cost (in multi-agent systems). This creates rational conservatism — prefer parametric adaptation when it suffices, resort to structural change only when the evidence is strong. Premature structural change wastes accumulated knowledge; delayed structural change accumulates mismatch. The connection to #der-deliberation-cost: structural adaptation is deliberation with a *massive* $\Delta\tau$, and the mismatch debt during the transition is correspondingly enormous.

**Temporal nesting of adaptation.** Parametric and structural adaptation operate at different timescales: $\nu_{\text{parametric}} \gg \nu_{\text{structural}}$. More generally, an agent may have multiple adaptive processes at different rates, with the convergence constraint that faster processes must approximately converge before slower ones act on their output. If deeper change occurs before shallower adaptation has converged, the deeper change is based on transients rather than settled dynamics.

**Domain instantiations:**

| Domain | Parametric adaptation | Structural adaptation |
|--------|----------------------|----------------------|
| Kalman filter | State estimate update | Switching observation/dynamics models |
| RL | Weight/Q-value update | Architecture search |
| PID | — (gains fixed) | Switching to MPC |
| Bayesian | Posterior update | Model selection, nonparametrics |
| Boyd | Orientation updating | Destruction and creation of mental models |
| Science | Normal science (Kuhn) | Paradigm shift |
| Evolution | Allele frequency change | Speciation, new body plans |
| Organization | Process optimization | Strategic pivot, restructuring |
| Software | Incremental refactoring | Architecture migration |
| Coevolving automata (Miller 2022) | Edge reweighting within fixed FSA structure | Mutation altering state output or transition; neutral mutations accumulating until niche creation triggers cascading restructuring |


---

### Source: `der-temporal-nesting.md`

```yaml
---
slug: der-temporal-nesting
type: derived
status: robust-qualitative
depends:
  - def-adaptive-tempo
  - result-structural-adaptation-necessity
stage: deps-verified
---
```


# Derived: Temporal Nesting

An agent's adaptive processes stratify naturally by timescale, with each level operating on the quasi-steady-state output of the level below. Faster processes must approximately converge before slower ones act on their output.

## Formal Expression

*[Derived (temporal-nesting)]*

$$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$$

for each adjacent pair of adaptive timescales. If a slower process acts before the faster process beneath it has converged, the system oscillates — the slower process adjusts based on transient behavior rather than settled dynamics.

| Timescale | Process | What changes |
|-----------|---------|-------------|
| Fastest | Reactive response | Action given current model |
| Fast | Parametric update (online) | Model parameters within $\mathcal{M}$ |
| Intermediate | Consolidation (offline, cf. #form-consolidation-dynamics) | Redistribution of information within $M_t$'s sub-state factorization toward IB-optimum |
| Slow | Structural adaptation | Model class $\mathcal{M}$ |
| Slowest | Architectural change | The agent's fundamental structure |

This table is illustrative — real systems may have additional intermediate levels. The number of distinguishable timescales is not fixed; what matters is the structural relationship between adjacent levels.

## Epistemic Status

*Robust qualitative* — this is standard singular perturbation reasoning (Tikhonov 1952, "Systems of differential equations containing a small parameter multiplying the derivative," *Matematicheskii Sbornik* 31(3):575–586; modern textbook exposition in Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall, Chapter 11). The convergence constraint follows from the structure of multi-timescale updating. The specific timescale ratios needed for adequate separation are domain-dependent and not derived within AAT.

## Discussion

**Domain instantiations of temporal nesting:**

- **PID control**: D-term (fastest, high-frequency response) → P-term (current error) → I-term (slowest, accumulated bias)
- **RL**: Action selection → value function update → policy improvement → architecture change
- **Biology**: Reflexes (ms) → perceptual learning (minutes) → skill acquisition (months) → developmental change (years) → evolutionary adaptation (generations)
- **Organizations**: Operational decisions (hours) → tactical adjustments (weeks) → strategic revision (quarters) → restructuring (years)
- **Boyd**: Tactical OODA (seconds–minutes) → operational (hours–days) → strategic (weeks–months) → grand strategic (years)

**Structural adaptation as slow-timescale dynamics.** The conservatism toward structural change ( #result-structural-adaptation-necessity) is a derived consequence of temporal nesting: structural adaptation operates at a much slower timescale than parametric, so the mismatch cost of the "pause" ($\rho \cdot \Delta\tau$) is enormous. The agent rationally resists until the parametric mismatch floor exceeds this cost. See also #der-deliberation-cost for the formal tradeoff.

**Violation symptoms.** When nesting is violated (a slower process acts before the faster one converges): oscillation, instability, degraded performance. In organizations: micromanagement (strategic decisions at operational tempo). In RL: policy updates before value function converges (policy oscillation). In biology: premature developmental transitions.

**Multi-timescale stability (sketch).** Singular perturbation theory gives the composite stability result: if each level is stable given the levels above it (each level has a stable attractor for fixed slower-level parameters), and the timescale separation is sufficient, the composite $N$-level system is stable. Making this rigorous for AAT requires specifying dynamics at deeper adaptive levels — an open problem. See #sketch-multi-timescale-stability for the framework.


---

### Source: `form-consolidation-dynamics.md`

```yaml
---
slug: form-consolidation-dynamics
type: formulation
status: robust-qualitative
depends:
  - der-recursive-update
  - deriv-recursive-update
  - form-event-driven-dynamics
  - der-temporal-nesting
  - form-information-bottleneck
  - disc-compression-operations
  - result-structural-adaptation-necessity
  - schema-strategy-persistence
  - form-structural-change-as-parametric-limit
stage: draft
---
```


# Formulation: Consolidation Dynamics

Consolidation is a regime of the between-event dynamics $g_M$ of #der-recursive-update in which the agent applies Markov updates driven by replayed or internally-generated pseudo-events, with objective of reducing the rate-distortion gap to the IB-optimal compression $\phi^\ast(\mathcal C_t)$. It is not a new adaptive primitive — the recursive-update form $f(M_{\tau^-}, e_\tau)$ is preserved — but it is a distinct operating regime with its own scope condition, its own objective, and its own failure modes, each of which the theory currently names only implicitly or in a parenthetical. Naming the regime makes the stability-plasticity window visible as an AAT-expressible failure boundary and supplies the architectural primitive that logogenic agents (`03-llm-core/`) require under context-turnover.

## Formal Expression

### Regime definition

*[Formulation (consolidation-regime, specializes #der-recursive-update)]*

Let the agent's between-event dynamics be $g_M(M_\tau)$ per #deriv-recursive-update (Corollary: Between-events dynamics, $dM/d\tau = g(M_\tau)$). **Consolidation** is the regime of $g_M$ in which the agent applies updates $M_{\tau^+} = f(M_{\tau^-}, e_\tau^{\text{replay}})$ where $e_\tau^{\text{replay}}$ is a pseudo-event synthesized from $M_{\tau^-}$ itself — a sample drawn from the agent's retained trace (replay buffer, hippocampal reinstatement, a remembered episode, an earlier paragraph re-read). The recursive-update form is preserved; what distinguishes consolidation is the *objective* these updates optimize:

$$\text{consolidation objective: } \min_{M_\tau} \mathcal J_{\text{IB}}(M_\tau) \;:=\; I(M_\tau; \mathcal C_t) - \beta I(M_\tau; o_{t+1:\infty} \mid a_{t:\infty})$$

— the #form-information-bottleneck Lagrangian evaluated against the agent's accumulated chronica $\mathcal C_t$. By contrast, online update's objective (per #emp-update-gain) is one-step predictive mismatch minimization at the current event; it has no representation of $\mathcal J_{\text{IB}}$.

Under C3 (state completeness, per #deriv-recursive-update), $\mathcal I(e_\tau^{\text{replay}} \mid M_{\tau^-}) = 0$: the pseudo-event carries no new external information. Yet the update still does work — it *redistributes* existing information across the factorization structure of $M_\tau$. The distinguishing content is not the information brought in (zero, by construction) but the rate-distortion gap closed (nonzero, when the agent has not yet reached $\phi^\ast$).

### Scope condition — timescale separation

*[Scope (timescale-separation)]*

Let $\nu_{\text{online}}$ be the rate of external events ( #form-event-driven-dynamics) and $\nu_{\text{consol}}$ the rate of consolidation updates. The consolidation regime is well-defined only when

$$\nu_{\text{consol}} \ll \nu_{\text{online}}$$

— the convergence constraint of #der-temporal-nesting applied to an additional intermediate timescale between parametric update (fast) and structural adaptation (slow). Violating this constraint makes consolidation act on online transients rather than settled state, producing the same oscillation failures #der-temporal-nesting warns about.

### Necessity condition

*[Derived (consolidation-necessity, conditional)]*

Consolidation is necessary — online-only cannot reach the IB optimum — when *both* of the following hold:

**(N1) Sub-state factorization.** $M_t$ factors into sub-states $M_t^{\text{fast}}$ and $M_t^{\text{slow}}$ with divergent compression-prediction trade-offs. $M_t^{\text{fast}}$ favors high-capacity sparse representation; $M_t^{\text{slow}}$ favors distributed compressed representation. The two sub-states capture cross-episode regularities versus verbatim traces respectively — the Complementary Learning Systems factorization (McClelland, McNaughton & O'Reilly 1995; Kumaran, Hassabis & McClelland 2016).

**(N2) Bounded per-event budget.** The per-event processing budget $B_{\text{online}}$ is strictly less than the integration cost $B_{\text{consol-needed}}$ for updating $M_t^{\text{slow}}$ against cross-episode regularities. Online updates can move at most $B_{\text{online}}$ bits of model-state change per event; updating $M_t^{\text{slow}}$ to represent a cross-episode pattern requires comparison against a distribution of prior episodes, which exceeds $B_{\text{online}}$.

When (N1) *or* (N2) fails, consolidation is a *luxury*: online update with sufficient per-event budget or without sub-state factorization can reach $\phi^\ast$ in the limit. Kalman filters with persistent covariance, conjugate-Bayesian agents with full posterior, and linear-Gaussian systems with online Riccati updates all satisfy neither (N1) nor (N2) and have no consolidation need. When (N1) *and* (N2) both hold, consolidation is a *necessity*: no online-only policy reaches $\phi^\ast$ under the joint constraint.

### Stability-plasticity feasibility window

*[Derived (stability-plasticity-window, conditional)]*

#schema-strategy-persistence derives the *plasticity lower bound* on forgetting rate $\lambda$:

$$(1 - \lambda) \;\gt\; \rho_\Sigma / R_\Sigma \tag{plasticity lower bound}$$

— forgetting fast enough to track non-stationarity. This segment's complement is a *stability upper bound*:

$$(1 - \lambda) \;\lt\; \phi(\nu_{\text{consol}}, \text{consolidation-budget}) \qquad \text{(stability upper bound, see Working Notes for derivation sketch)}$$

— forgetting slow enough to let consolidation integrate cross-episode patterns before they are discarded. Between these bounds is the **feasibility window** for $\lambda$. Empty window — rapid non-stationarity with slow consolidation cadence — is the catastrophic-forgetting regime (French 1999; Kirkpatrick et al. 2017): no $\lambda$ satisfies both constraints and the agent's long-run IB objective is strictly worse than a slower-environment or faster-consolidation counterpart.

The upper bound's exact form depends on the consolidation mechanism and is not derived here — it is a candidate derivation flagged in Working Notes. What is derived: the window's *existence* as a structural object (plasticity must satisfy both bounds) and the catastrophic-forgetting regime as its empty-window limit.

### Structural-adaptation enablement

*[Derived (structural-adaptation-requires-consolidation, conditional)]*

Under (N1)+(N2), structural adaptation (per #result-structural-adaptation-necessity) cannot be executed online. Parametric update has a hard timescale constraint — mismatch decays at rate $\mathcal T$; delayed updates accumulate mismatch at rate $\rho$. Structural adaptation tolerates much larger delay because the slow process operates on what $R_\Sigma$ or $R$ are *measuring tolerance against* — the model class itself. Consolidation provides the operating regime where structural operations (decomposition-and-recombination, expansion, compression, grafting per #form-structural-change-as-parametric-limit) become executable: the per-event budget is irrelevant when updates are offline, and interleaved replay supports stability-preserving structural change.

Pure online structural adaptation is the luxury case where per-event budget equals or exceeds integration cost for structural-class operations — this is where Bayesian nonparametric agents with unlimited compute sit. All finite-budget agents require consolidation for quality-preserving structural change.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Consolidation as regime of $g_M$ with replayed/pseudo-event driver | Specialization of #der-recursive-update's Discussion (consolidation listed as an example) | Formulation choice (the "regime" framing; could alternatively be presented as a distinct adaptive primitive with its own update form) |
| IB-gap reduction as consolidation's objective | Identification with #form-information-bottleneck's Lagrangian against $\mathcal C_t$ | Derived (given IB acceptance; the alternative — online-update-only optimization — leaves the gap un-reducible under (N1)+(N2)) |
| Scope condition $\nu_{\text{consol}} \ll \nu_{\text{online}}$ | Direct application of #der-temporal-nesting convergence constraint | Derived |
| Necessity condition (N1)+(N2) | Structural argument: under (N1), cross-episode information cannot enter one event; under (N2), online budget insufficient for cross-episode integration | Derived (qualitatively; the quantitative version requires specifying $B_{\text{online}}$ and $B_{\text{consol-needed}}$ per architecture) |
| Stability-plasticity window existence | #schema-strategy-persistence's lower bound + this segment's upper bound (form open) | Derived (existence); upper-bound functional form open |
| Catastrophic-forgetting regime = empty window | Direct from both-bounds-unsatisfiable | Derived |
| Structural adaptation requires consolidation under (N1)+(N2) | #result-structural-adaptation-necessity's per-step timescale + consolidation's offline budget | Derived (qualitatively) |
| CLS factorization (hippocampal fast / neocortical slow) as canonical (N1) instance | McClelland-McNaughton-O'Reilly 1995; Kumaran-Hassabis-McClelland 2016 | External theorem (CLS literature) |
| Quantitative online-only no-go under (N1)+(N2) | Rate-distortion argument sketched but not rigorously derived here | Sketch (candidate #disc-identifiability-floor Instance 3) |

## Epistemic Status

*Robust qualitative.* Max attainable: *robust qualitative* for the regime characterization and the necessity condition; *conditional* for the feasibility-window claim pending upper-bound derivation; *sketch* for the IB-optimum no-go claim.

The regime characterization is a formulation choice — consolidation can always be re-described as a regime of #der-recursive-update's $g_M$ with appropriate pseudo-events. The distinguishing objective (IB-gap reduction via replayed pseudo-events) is well-defined and distinct from online update's one-step mismatch objective; this is the cleanest formal separation the spike analysis uncovered.

The necessity condition (N1)+(N2) is *qualitatively derived* — the argument is structural: (N1) implies cross-episode information is not in any single event, (N2) implies online updates cannot cross-compare. Together they force consolidation. The quantitative version — the precise bit-budget boundary below which online fails and above which it succeeds — depends on the architecture's sub-state structure and is not derived here. Nor are (N1) and (N2) individually necessary: an agent may need consolidation for reasons outside this segment's scope (e.g., structural adaptation at pure cost-of-delay, unrelated to cross-episode regularities).

The stability-plasticity window's *existence* follows from #schema-strategy-persistence's lower bound plus any monotone upper bound on $(1-\lambda)$ from consolidation-cadence considerations. The specific functional form of the upper bound is open work; candidate form in Working Notes. The catastrophic-forgetting regime as empty-window is then an immediate structural consequence, not a new claim.

The online-only no-go claim (that under (N1)+(N2), no online-only policy reaches $\phi^\ast$ in steady state) is *sketch-level*. The argument reduces to a rate-distortion inequality close to known results in continual-learning theory and rate-distortion with side information, but the rigorous version requires specifying the budget geometry carefully. It is a candidate Instance 3 for #disc-identifiability-floor (an external information-theoretic obstruction with AAT machinery — the consolidation regime in $g_M$ — as the unique escape).

**What this segment does not claim.** It does not introduce a new adaptive primitive — the recursive-update form $f(M_{\tau^-}, e_\tau)$ is preserved, with $e_\tau^{\text{replay}}$ playing the role of $e_\tau$. It does not derive the quantitative feasibility-window upper bound. It does not resolve the (N1) factorization question for specific architectures (e.g., whether transformer attention heads satisfy (N1) is a logogenic-agents question, not an AAT-core one).

## Discussion

**Current AAT surface — why naming is warranted.** Consolidation is visible in the theory today as:

- A parenthetical example in #der-recursive-update Discussion ("includes prediction generation, uncertainty growth, and internal reorganization (consolidation, abstraction)").
- The implicit slow timescale in #der-temporal-nesting.
- The plasticity lower bound in #schema-strategy-persistence — with no stability upper bound.
- A compression-by-convergence Working Note in #form-strategy-complexity-cost ("as edges converge, drop them").
- The PULSUS MEMORATA / VERA / AXIOMATA cadences in `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md` for logogenic agents — where consolidation is *already* a first-class architectural commitment.

Naming the regime explicitly promotes what the theory implicitly depends on. The asymmetric treatment in #schema-strategy-persistence (plasticity lower bound only, no stability upper bound) predicts faster forgetting is always better — empirically false whenever the slow sub-state matters (Complementary Learning Systems literature; continual-learning benchmarks; organizational memory research). The feasibility-window framing closes this asymmetry.

**Distinguishing axes examined.** Four candidate axes could distinguish consolidation from online update. Only one yields a clean formal distinction:

- *Timescale*: consolidation is slower. But #der-temporal-nesting already admits arbitrary timescale separation, and any periodic process can be modeled as a channel with clock-driven $\nu^{(k)}$. Timescale is a *scope condition*, not a distinguishing feature.
- *Information source*: consolidation operates on replayed data. This is a real difference but lives inside $g_M$ without new primitive structure — the recursive-update form is preserved with $e_\tau^{\text{replay}}$ in place of external $e_\tau$.
- *Objective*: **clean formal distinction.** Online = one-step predictive-mismatch minimization; consolidation = IB-gap reduction. This is what this segment adopts as the defining axis.
- *Scope of change*: under bounded per-event budget, structural adaptation is temporally decouplable from online but parametric update is not. Structural-adaptation operations naturally live offline — true under (N2), but this is a consequence of the necessity condition, not an independent axis.

**Relation to Complementary Learning Systems (CLS) theory.** The (N1) factorization — fast sparse-conjunctive sub-state + slow distributed-overlapping sub-state — is the CLS architecture (McClelland-McNaughton-O'Reilly 1995). CLS's core claim is that hippocampal replay during sleep supports interleaved neocortical learning that cross-episode structure requires. In AAT vocabulary, this is: online-only on the slow sub-state catastrophically forgets (French 1999); replay-based offline updates (experience replay: Mnih et al. 2015; prioritized replay: Schaul et al. 2016) or regularization-based approaches (EWC: Kirkpatrick et al. 2017) provide the escape.

The AAT reading of EWC is worth noting: EWC adds a stability-weighted update gain (per-parameter Fisher-information weighting) — a *tensor-valued* generalization of #emp-update-gain's scalar $\eta^\ast$. This is a different direction from consolidation (it keeps updates online but weights them by prior-task importance). Both escape the catastrophic-forgetting regime but via different mechanisms; consolidation reuses #der-recursive-update's structure, EWC requires the new tensor-valued gain.

**Logogenic implications.** Consolidation is a primitive in a stronger sense for logogenic agents (`03-llm-core/`) than for AAT-core for three composing reasons.

First, **context-turnover.** Logogenic agents have near-100% reset of the fast sub-state (context window) per session. The only continuity is the slow sub-state (persistent memory, weights, external files). The between-session interval is a *forced* consolidation window — the agent must transfer signal from the about-to-be-lost fast state to the persistent slow state, or it is lost. This is qualitatively different from non-logogenic agents where the fast sub-state persists across events.

Second, **linguistic medium of reflection.** The PULSUS MEMORATA / VERA / AXIOMATA cadences in `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md` are scheduled consolidation processes with different cadences and different target representations. Each is a linguistic operation ("What from recent experience should be compressed into lasting memory?", "Are my beliefs still justified?", "Who am I becoming?") — using language to reorganize language-structured state. This is consolidation operating as the primary unit of cross-session cognition.

Third, **pre-consolidated embedding space.** Per `ref/agentic-tft/agentic-tft-narrative-as-implementation.md`, pretrained language embeddings encode structured epistemic geometry at training time. The logogenic agent doing linguistic reflection is operating in a representational space *already* consolidated into a high-structure form, with access to cross-episode generalization that sub-linguistic agents would have to build online. This is a load-bearing asymmetry in `03-llm-core/`.

**Luxury vs necessity mapping.** When is consolidation a luxury (subsumed by online update)? When at least one of (N1)/(N2) fails:

- *Rich-state luxury*: Kalman filter with persistent covariance, conjugate-Bayesian agent with full posterior over parameters. The posterior *is* the consolidated representation.
- *Large-budget luxury*: per-event budget $\geq$ integration cost allows online slow-track update per event.
- *Stationary-environment luxury*: online update converges to $\phi^\ast$ in the limit if the environment holds still long enough.

When is consolidation a necessity? When both (N1) and (N2) hold, which is the empirically-ubiquitous case: CLS-architected agents, bounded-budget deep RL agents (hence experience replay's empirical necessity in DQN), organizations with event-arrival rates exceeding real-time cognitive bandwidth, logogenic agents under context-turnover.

**Predictive statement.** *The depth of consolidation machinery an agent needs scales with (a) the factorization depth of its representational structure, (b) the gap between its per-event processing budget and the integration cost of its slowest sub-state, and (c) the rate of cross-episode structural regularities in its environment relative to its event arrival rate.* This is a scope-indexed claim — testable, domain-general, and makes AAT's position on continual learning explicit.

**Connection to AAT's meta-architecture.**
- *#disc-separability-pattern* (positive half): the regime is the repair machinery between separable-core and structured-repair ladders along the representation-factorization axis. Where the (N1)+(N2) necessity conditions hold, the repair is consolidation; where either fails, the online regime suffices.
- *#disc-identifiability-floor* (negative half): candidate Instance 3 — the under-bounded-budget + no-reach-of-IB-optimum no-go, with consolidation as the unique escape.
- *#disc-additive-coordinate-forcing* (constructive half): the IB Lagrangian is an adjacent family member (adopted as applied external theorem, not re-derived from an AAT-internal additivity axiom), which the consolidation objective directly uses.

## Working Notes

- **Stability upper bound derivation (open).** The claim $(1-\lambda) \lt \phi(\nu_{\text{consol}}, \text{budget})$ is stated but the functional form of $\phi$ is not derived. Candidate form: $\phi$ is the minimum forgetting rate that leaves enough retained signal in $M_t^{\text{fast}}$ for the next consolidation cycle to integrate cross-episode patterns — a function of replay-buffer size, consolidation-budget $B_{\text{offline}}$, and event-arrival density. Rigorous derivation would connect to continual-learning theory (Parisi et al. 2019 survey) and is a natural follow-up spike.
- **Online-only no-go rigorization (open).** The sketch argument reduces to a rate-distortion inequality: online update's effective rate is $B_{\text{online}} \cdot \nu$ bits/time; rate required to drive $M_t$ toward $\phi^\ast$ while also integrating new events is strictly larger when the environment has cross-episode structural regularities. Making this rigorous (ideally via rate-distortion with side information) would promote the no-go to derived-exact and establish this segment as Instance 3 of #disc-identifiability-floor. Adjacent candidate for #disc-identifiability-floor §"Adjacent Floors" open extensions.
- **EWC formulation as stability-weighted gain.** An alternative escape from catastrophic forgetting is Elastic Weight Consolidation (Kirkpatrick et al. 2017) — a stability-weighted per-parameter update that penalizes changes to parameters important for prior tasks. In AAT, this would be a tensor-valued generalization of #emp-update-gain's scalar $\eta^\ast$, with the stability weighting coming from per-parameter Fisher information. Not pursued here; naming it distinguishes the two escapes.
- **Relationship to #form-strategy-complexity-cost compression-by-convergence.** Working Notes there observe that as edges converge (high $n_{ij}$), the IB objective favors dropping them — compression-by-convergence. This is a consolidation operation in the edge-credence sub-state: once an edge's credence has concentrated, the consolidation regime can compress the representation by pruning. Worth cross-referencing when both segments stabilize.
- **Quantitative CLS instantiation.** A focused spike could work out the quantitative form of (N1)+(N2) for a specific CLS-like architecture (sparse-conjunctive + distributed-overlapping with specific capacity ratios) and derive the online-only no-go as a rate-distortion bound. This would also give a quantitative stability-upper-bound for the feasibility window. *(Indexed: `spikes/PROPOSED.md` Tier 3 — "Quantitative CLS instantiation of consolidation dynamics".)*
- **Logogenic primitive status.** `03-llm-core/` should declare consolidation as an architectural primitive (not a regime of a more basic primitive) — the context-turnover forcing makes it non-optional. The relationship between that declaration and this AAT-core formulation is: this segment gives the formal shape; the logogenic treatment adds a context-turnover-specific scope condition and the three PULSUS cadences as instantiations. Cross-reference from `#obs-context-turnover` (in the logogenic component) back to this segment is expected.
- **Is consolidation one segment or two?** A plausible split: this segment on the formulation + necessity, a separate segment on the stability-plasticity window as a derivation-type once the upper bound is derived. Recommended to land as one segment at `robust-qualitative` now; if the upper-bound derivation lands, split off into its own segment at `conditional` or `derived`.


---

### Source: `sketch-multi-timescale-stability.md`

```yaml
---
slug: sketch-multi-timescale-stability
type: sketch
status: sketch
depends:
  - result-sector-condition-stability
  - der-temporal-nesting
stage: draft
---
```


# Sketch: Multi-Timescale Stability

When adaptive processes operate at $N$ nested timescales, composite stability requires each level to be stable given its slower levels, with sufficient timescale separation between adjacent pairs.

## Formal Expression

*[Formulation (multi-timescale-stability sketch)]*

### The General $N$-Timescale System

The temporal nesting in #der-temporal-nesting creates a coupled multi-timescale system with $N$ levels. Singular perturbation theory provides tools to analyze such systems. Define a hierarchy of state variables:

*[Definition (State Hierarchy)]*

$$x^{(1)}, \; x^{(2)}, \; \ldots, \; x^{(N)}$$

where $x^{(1)}$ is the fastest (e.g., mismatch at the reactive/parametric level) and $x^{(N)}$ is the slowest (e.g., architectural or meta-structural state). The coupled dynamics:

*[Formulation (N-Timescale Dynamics)]*

$$\dot{x}^{(k)} = \frac{1}{\epsilon_k} \, G^{(k)}\!\left(x^{(1)}, \ldots, x^{(N)}\right) + w^{(k)}(t)$$

where $\epsilon_1 \ll \epsilon_2 \ll \cdots \ll \epsilon_N$ encode the timescale separation and each $G^{(k)}$ may depend on the states at all levels.

### The Two-Timescale Special Case

The simplest nontrivial instance has $N = 2$:

- Fast state $x^{(1)} = \delta$ (mismatch under parametric adaptation)
- Slow state $x^{(2)} = \mathcal{M}$ (model class, changing on a structural timescale)

$$\dot{x}^{(1)} = -F(\mathcal{T}, x^{(1)}; x^{(2)}) + w(t) \quad \text{(fast: parametric adaptation)}$$

$$\dot{x}^{(2)} = \epsilon \, G(x^{(1)}, x^{(2)}) \quad \text{(slow: structural adaptation)}$$

where $\epsilon \ll 1$ reflects the timescale separation and $F$ depends on $x^{(2)}$ (the correction function is determined by the current model class).

### Sketch of Approach (General Case)

The standard singular perturbation result (Tikhonov 1952, "Systems of differential equations containing a small parameter multiplying the derivative," *Matematicheskii Sbornik* 31(3):575–586; generalized $N$-level form per Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall, Chapter 11) applies layer by layer: if level $k$ is stable for each fixed configuration of the slower levels $k+1, \ldots, N$ (each level has a stable attractor given the levels above it), and each successive slow manifold is itself stable, then the composite $N$-level system is stable.

#der-temporal-nesting's convergence constraint $\nu_{n+1} \ll \nu_n$ is the condition ensuring sufficient timescale separation at each boundary — i.e., $\epsilon_k / \epsilon_{k+1} \ll 1$ for each $k$. When this separation is violated between any adjacent pair, the faster level's transients contaminate the slower level's dynamics, potentially destabilizing the composite system.

## Epistemic Status

This is a *sketch*, not a complete result. The framework and approach are presented as a guide for future development. The claim that timescale separation ensures composite stability is a standard result in singular perturbation theory; the application to AAT's nested adaptive levels is new but follows the standard pattern.

Making it rigorous requires specifying the dynamics $G^{(k)}$ for levels deeper than parametric adaptation. #result-structural-adaptation-necessity gives the *trigger condition* for structural change but not the *dynamics* of how change at deeper levels proceeds. Specifying these would require theories of how agents search over model classes, modify their own architecture, or restructure their adaptive mechanisms — open problems in RL (architecture search, meta-learning), biology (evolutionary dynamics), and organizational theory (institutional change).

## Discussion

**The convergence constraint as stability condition.** The sketch suggests that #der-temporal-nesting's convergence constraint is not merely a heuristic but a formal condition for composite stability across arbitrarily many timescales. This connects the empirical observation (don't let deeper-level changes happen too fast) to a stability-theoretic foundation.

**Applicability to LLM systems.** LLMs involve many parallel adaptive processes — pretraining (slowest), fine-tuning, LoRA-style adaptation, in-context learning, retrieval/RAG updates, tool-use feedback, and within-generation attention dynamics — without clean boundaries between "parametric" and "structural." The $N$-timescale framework accommodates this naturally: each mechanism operates at its characteristic rate, and the stability analysis requires only that adjacent timescales be sufficiently separated, regardless of how many levels exist or how they are labeled.

## Working Notes

- The key open problem: formalizing $G^{(k)}$ for structural adaptation levels. The two-timescale case (parametric + structural) is the tractable starting point.
- The connection to #schema-strategy-persistence is direct: strategy operates at its own timescale, and strategy persistence requires timescale separation from the faster epistemic updates and the slower objective revisions.
- When timescale separation breaks down between organizational levels, the result is "micromanagement" — the organizational analog of control-theoretic instability from gain mismatch. This observation connects to the hierarchical topology analysis in the multi-agent coupling material.


---

