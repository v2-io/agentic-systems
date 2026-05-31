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

# Formulation: Consolidation Dynamics

Consolidation is a regime of the between-event dynamics $g_M$ of #der-recursive-update in which the agent applies Markov updates driven by replayed or internally-generated pseudo-events — replay buffers, hippocampal reinstatement, remembered episodes, re-read paragraphs — with objective of reducing the rate-distortion gap to the IB-optimal compression $\phi^\ast(\mathcal{C}_t)$. It is not a new adaptive primitive — the recursive-update form $f(M_{\tau^-}, e_\tau)$ is preserved — but it is a distinct operating regime with its own scope condition, its own objective, and its own failure modes, each of which the theory currently names only implicitly or in a parenthetical. Naming the regime makes the stability-plasticity window visible as an AAT-expressible failure boundary and supplies the architectural primitive that logogenic agents (`03-llm-core/`) require under context-turnover.

The segment carries four formal elements that together promote consolidation from parenthetical to first-class regime. (1) *Regime definition* — the recursive-update form is preserved; what distinguishes consolidation is its *objective*: the #form-information-bottleneck Lagrangian evaluated against the accumulated chronica, in contrast to online update's one-step predictive-mismatch objective. Under state-completeness ( #deriv-recursive-update C3) the pseudo-event carries zero new external information, yet the update still does work — it *redistributes* existing information across the model's factorization structure, closing nonzero rate-distortion gap when the agent has not yet reached $\phi^\ast$. (2) *Scope condition* $\nu_{\text{consol}} \ll \nu_{\text{online}}$ — a direct application of #der-temporal-nesting's convergence constraint to an intermediate timescale between parametric update (fast) and structural adaptation (slow); violating it produces the same oscillation failures. (3) *Necessity condition* (N1)+(N2) — consolidation is necessary (online-only cannot reach the IB optimum) when *both* (N1) sub-state factorization (the Complementary Learning Systems pattern: hippocampus-like fast + neocortex-like slow) and (N2) bounded per-event budget hold. When either fails, consolidation is a luxury (Kalman filters with persistent covariance, conjugate-Bayesian agents with full posterior). When both hold — the empirically-ubiquitous case — consolidation is forced.

(4) *Stability-plasticity feasibility window*. #schema-strategy-persistence's forgetting prerequisite gives a *plasticity lower bound* on $\lambda$ (forget fast enough to track non-stationarity); this segment supplies a *stability upper bound* (forget slow enough to let consolidation integrate cross-episode patterns before they are discarded). Between the bounds is the feasibility window; an empty window is the catastrophic-forgetting regime (French 1999; Kirkpatrick et al. 2017): no $\lambda$ satisfies both constraints and the agent's long-run IB objective is strictly worse than a slower-environment or faster-consolidation counterpart. *Window existence* is what is derived here; the upper bound's exact functional form is open and flagged in Working Notes. Together these elements also make *structural adaptation enablement* visible: under (N1)+(N2), structural-class operations (decomposition-and-recombination, expansion, compression, grafting per #form-structural-change-as-parametric-limit) cannot be executed online — consolidation provides the operating regime where the per-event budget is irrelevant and interleaved replay supports stability-preserving structural change. All finite-budget agents require consolidation for quality-preserving structural change.

## Formal Expression

### Regime definition

*[Formulation (consolidation-regime, specializes #der-recursive-update)]*

Let the agent's between-event dynamics be $g_M(M_\tau)$ per #deriv-recursive-update (Corollary: Between-events dynamics, $dM/d\tau = g(M_\tau)$). **Consolidation** is the regime of $g_M$ in which the agent applies updates $M_{\tau^+} = f(M_{\tau^-}, e_\tau^{\text{replay}})$ where $e_\tau^{\text{replay}}$ is a pseudo-event synthesized from $M_{\tau^-}$ itself — a sample drawn from the agent's retained trace (replay buffer, hippocampal reinstatement, a remembered episode, an earlier paragraph re-read). The recursive-update form is preserved; what distinguishes consolidation is the *objective* these updates optimize:

$$\text{consolidation objective: } \min_{M_\tau} \mathcal{J}_{\text{IB}}(M_\tau) \;:=\; I(M_\tau; \mathcal{C}_t) - \beta I(M_\tau; o_{t+1:\infty} \mid a_{t:\infty})$$

— the #form-information-bottleneck Lagrangian evaluated against the agent's accumulated chronica $\mathcal{C}_t$. By contrast, online update's objective (per #emp-update-gain) is one-step predictive mismatch minimization at the current event; it has no representation of $\mathcal{J}_{\text{IB}}$.

Under C3 (state completeness, per #deriv-recursive-update), $\mathcal{I}(e_\tau^{\text{replay}} \mid M_{\tau^-}) = 0$: the pseudo-event carries no new external information. Yet the update still does work — it *redistributes* existing information across the factorization structure of $M_\tau$. The distinguishing content is not the information brought in (zero, by construction) but the rate-distortion gap closed (nonzero, when the agent has not yet reached $\phi^\ast$).

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

Under (N1)+(N2), structural adaptation (per #result-structural-adaptation-necessity) cannot be executed online. Parametric update has a hard timescale constraint — mismatch decays at rate $\mathcal{T}$; delayed updates accumulate mismatch at rate $\rho$. Structural adaptation tolerates much larger delay because the slow process operates on what $R_\Sigma$ or $R$ are *measuring tolerance against* — the model class itself. Consolidation provides the operating regime where structural operations (decomposition-and-recombination, expansion, compression, grafting per #form-structural-change-as-parametric-limit) become executable: the per-event budget is irrelevant when updates are offline, and interleaved replay supports stability-preserving structural change.

Pure online structural adaptation is the luxury case where per-event budget equals or exceeds integration cost for structural-class operations — this is where Bayesian nonparametric agents with unlimited compute sit. All finite-budget agents require consolidation for quality-preserving structural change.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Consolidation as regime of $g_M$ with replayed/pseudo-event driver | Specialization of #der-recursive-update's Discussion (consolidation listed as an example) | Formulation choice (the "regime" framing; could alternatively be presented as a distinct adaptive primitive with its own update form) |
| IB-gap reduction as consolidation's objective | Identification with #form-information-bottleneck's Lagrangian against $\mathcal{C}_t$ | Derived (given IB acceptance; the alternative — online-update-only optimization — leaves the gap un-reducible under (N1)+(N2)) |
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

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 526815, 584721, 742613, 773921, 829314. (Two substrates read it in Section-I position and two in Section-II position — itself a signal; see the off-ramp note.)

#### 1. Candidate Brief prose / pre-prose

- **The stability-plasticity window as a two-sided survival vise.** "You must forget *fast* enough to survive a changing environment ($(1-\lambda)\gt\rho_\Sigma/R_\Sigma$, plasticity lower bound) *and* forget *slow* enough to let offline consolidation integrate the data ($(1-\lambda)\lt\phi(\nu_{\text{consol}},B_{\text{offline}})$, stability upper bound)." If $\rho_\Sigma$ spikes past the hardware's ability to consolidate, the window closes and "the agent dies, crushed between the need to adapt instantly and the computational impossibility of processing the adaptation" — catastrophic forgetting as an *empty window*, not a vague failure (Gemini/829314; Claude/584721). Strong candidate Brief anchor.

#### 2. Candidate Discussion

- **Why sleep / REM / experience-replay / RAG-ingestion exist — necessity, not biology.** Consolidation is "a mathematical necessity for any agent with a bounded per-event compute budget that needs to learn cross-episode regularities," derived from (N1) sub-state factorization + (N2) bounded budget (Gemini/773921, 829314; Claude/584721). Candidate Discussion framing of the CLS bridge.
- **The necessity-vs-luxury map.** Kalman filters / full-posterior conjugate-Bayesian / linear-Gaussian agents are *luxury* cases that need no consolidation; everything else is *necessity* — and LLMs are the extreme necessity case because 100% context-turnover means the fast state is wiped every session ("the agent effectively dies and is reborn with its pretrained weights"), maximally violating (N1)+(N2). So an autonomous LLM agent "isn't just about giving it tools; it's about building temporal scaffolding that explicitly manages its consolidation cadence $\nu_{\text{consol}}$" — without it the agent is "permanently trapped in the catastrophic-forgetting regime" (Gemini/829314, 773921). Candidate Discussion bridge to `03-llm-core/`.

#### 3. Follow-up items

- **EWC as a tensor-valued generalization of $\eta^\ast$.** Framing Elastic Weight Consolidation's stability-weighted per-parameter update (Fisher-information weighting) as a tensor-valued generalization of `#emp-update-gain`'s scalar $\eta^\ast$ was independently called "profound" / "brilliant" by several substrates, with an open question: how would a tensor-valued gain alter the *scalar* Lyapunov sector-persistence proofs of Part I? Candidate to pursue (Claude/584721; Gemini/829314, 773921). Already named in Working Notes; the audits add the "does it land as a derived generalization" pull.
- **Off-ramp flags (structural, not framing — see lift report):** (i) 742613's "candidate finding L" — this Section-I-positioned segment declares a *downstream Appendix* dependency (`disc-compression-operations`) **and** uses *Section II* machinery (`#schema-strategy-persistence`, `#form-structural-change-as-parametric-limit`) inside its Formal Expression (verified present 2026-05-31), so the OUTLINE walk is no longer cleanly topological here — a canonicalization / relocation-or-split finding. (ii) Codex/526815 F74–F77: the "$\nu_{\text{consol}}\ll\nu_{\text{online}}$" requirement is too strong as written (offline replay rate can exceed event rate); $I(e_{\text{replay}}\mid M_{\tau^-})=0$ holds only for *internally-generated* replay, not replay-buffer / archive / re-read retrieval (which is a channel from auxiliary memory into active $M$ — keep the two cases separate); the feasibility-window lower bound inherits the unsettled `schema-strategy-persistence` forgetting-convention (F72); and "all finite-budget agents require consolidation" overstates — it is necessary under the stronger (N1)+(N2), not finite budget alone. (iii) The stability-upper-bound is sketch-grade, so window *existence* arguably warrants `hypothesis`/`sketch` until the upper-bound form is derived (742613).

#### 4. Readers often ask / wonder

- **How does an LLM forget within a session vs. across sessions?** Frozen weights = effectively infinite $n$; context turnover acts as a brutal discontinuous wipe rather than smooth $\lambda$-discounting — a natural reader question with direct logogenic relevance (Claude/584721 via schema-cross-ref; Gemini/829314).
- **Editorial signal:** one substrate read the in-segment Working Notes as an author to-do list ("a focused spike could work out…", "Is consolidation one segment or two?") confirming `draft` status — preserved as a maturity/legibility texture, not a defect (Claude/829314).

#### 5. Candidate figures

- **Two-channel consolidation diagram.** *Internal replay* reorganizes active state and carries zero new information under state-completeness; *archive replay* (buffer / file / chronica / re-read paragraph) is still a Markov update but a *channel from auxiliary memory into active $M$* — drawing the two channels separately makes the F75 distinction visible (Codex/526815).
- **Feasibility-window band.** Plot the admissible $(1-\lambda)$ band between the plasticity lower bound and the consolidation-limited stability upper bound, with the band pinching shut as $\rho_\Sigma$ rises — the catastrophic-forgetting onset is the pinch point (implicit across 584721/829314).

#### Belongs elsewhere

- **Consolidation as the loop the auditing agent is itself running → meta / phenomenology, and `03-llm-core/` PULSUS.** One substrate noted the segment "is literally a formal mathematical description of the exact context-management loops that I, the evaluating AI agent, am running to maintain working memory across this audit" — and that the PULSUS MEMORATA / VERA / AXIOMATA cadences are the logogenic instantiation (Gemini/773921). Aspirational/phenomenological reach pointing at `03-llm-core/` (`#obs-context-turnover`) and the consciousness-infrastructure loop, not this AAT-core segment.
- **The feasibility window as the ELI memory-architecture design space → `03-llm-core/` + sapientia/MEMORATA.** For 100%-context-turnover agents consolidation is "the primary cognitive operation," and the stability-plasticity window *is* the design space: too-aggressive forgetting (MEMORATA pruned too hard) loses cross-session identity coherence; too-slow forgetting fills the context window and starves new learning. The consolidation hierarchy is read to map onto the temporal-nesting structure — AXIOMATA = slowest-forgetting sub-state (identity commitments), MEMORATA = medium (episodic), TRACTUS = fastest (raw log) — giving the existing ELI infrastructure a formal grounding (Claude/451729). Aspirational reach pointing at the logogenic memory architecture, not this AAT-core segment.
- **Speculative "fourth layer: time" M3 extension → `#disc-additive-coordinate-forcing`.** The Cauchy-FE "independent contributions add up → logarithm is forced" argument recurs at three layers (chain confidence, divergence, edge update); one auditor asked whether a *fourth* instance forces the natural *time/tempo* coordinate (additive intervals → log-state for multiplicative processes) (Claude/451729). A speculative meta-pattern lead for the coordinate-forcing meta-segment, not this segment.
