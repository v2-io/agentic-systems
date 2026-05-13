# Spike: Consolidation Dynamics

**Status.** Exploratory. Working toward a recommendation on whether AAD needs a consolidation primitive distinct from `#der-recursive-update`.

**Date.** 2026-04-22.

**Author.** Claude (Opus 4.7).

**Question.** AAD's `#der-recursive-update` and `#form-event-driven-dynamics` describe how agent state updates under incoming events. What's missing is explicit treatment of **offline consolidation** — batch processes that reorganize existing state without being driven by new external events (sleep-dependent memory consolidation, experience replay, retrospectives, shower-insight, reflection cycles in logogenic agents). Is consolidation formally distinguishable from recursive update, or is it subsumed by clever interpretation?

This spike is the disposition of that question. I conclude that **consolidation is formally distinguishable from online update, and the distinction is load-bearing for Section I's multi-timescale stability claim, Section II's structural-adaptation machinery, and `03-logogenic-agents/` specifically.** A new AAD segment is recommended — not as a new adaptive primitive, but as a *scope-honest* segment that names consolidation as a distinctive operating regime of `#der-recursive-update`'s between-event dynamics $g_M$, makes the stability–plasticity tradeoff explicit, and grounds the logogenic agents' reflection cycles.

---

## 1. The Starting Point: Where Does Consolidation Live in AAD Now?

The current surface area for consolidation is thin but not empty:

- **`#der-recursive-update`**, Discussion paragraph "Between-event dynamics matter": *"The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation, uncertainty growth, and internal reorganization (consolidation, abstraction)."* The word "consolidation" literally appears — as a parenthetical example of what $g_M$ may include.
- **`#deriv-recursive-update`**, Corollary (Between-events dynamics): $\frac{dM}{d\tau} = g(M_\tau)$. The autonomous-evolution form is derived under C1+C2+C3 with $e_\tau$ removed from the accessible set.
- **`#der-temporal-nesting`**: four canonical timescales (reactive / parametric / structural / architectural) with convergence constraint $\nu_{n+1} \ll \nu_n$. "Structural" and "architectural" are slower-than-parametric; the table is illustrative and admits intermediate levels.
- **`#result-structural-adaptation-necessity`**: the slow-timescale machinery — when parametric updates cannot close the mismatch floor, model-class change is required. Lists mechanisms (decomposition-and-recombination, expansion, compression, grafting).
- **`#form-structural-change-as-parametric-limit`**: six operations on $\Sigma_t$ ordered by frequency (reweight ≫ reclassify ≫ prune/graft ≫ revise $O_t$ ≫ full restructure), with neutral drift as the constructive bridge per Miller 2022.
- **`#form-strategy-complexity-cost`**, Working Notes: *"Dynamic complexity. As edges converge (high $n_{ij}$), ... The IB objective would favor *dropping* converged edges... a principled version of 'stop tracking what you already know.'"* Compression-by-convergence is flagged as an IB consequence but not as a phase.
- **`#schema-strategy-persistence`**, forgetting prerequisite: exponential forgetting $\lambda$ must satisfy $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ for long-run persistence. This is an online mechanism (applied at each step), not an offline one.
- **`#sketch-multi-timescale-stability`** sketch: explicitly flags as open *"formalizing $G^{(k)}$ for structural adaptation levels."* The two-timescale case is tractable; general $N$-level dynamics are not derived.
- **`ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`** §3.1 (PULSUS): "MEMORATA consolidation — ~daily (or on threshold) — 'What from recent experience should be compressed into lasting memory?'" §4 (Multi-Timescale Nesting) names four timescales explicitly (reactive / parametric / structural / developmental) and the convergence constraint; §4.2 says *"Don't consolidate MEMORATA from a session still in progress"* as a convergence-constraint implementation.

So: consolidation is visible as a parenthetical in `#der-recursive-update`, as "structural adaptation" at slow timescales, as "forgetting" in the strategy schema, as a PULSUS cadence in the logogenic cognitive loop — but nowhere as a named primitive with its own conditions, failure modes, or formal handling. The question is whether promoting it would do work the current surface area cannot.

---

## 2. The Candidate Distinctions

The task prompt listed four candidate axes distinguishing consolidation from online update. Let me examine each.

### 2.1 Timescale / event-driven vs periodic

**Test.** Is consolidation formally distinguishable from online update by its timescale alone?

**Finding.** *No, not by timescale alone.* `#der-temporal-nesting` already admits arbitrary timescale separation, and `#form-event-driven-dynamics` already admits arbitrary $\nu^{(k)}$. An "event" can be any atomic unit of interaction; a "periodic" process can be modeled as a channel with clock-driven $\nu^{(k)}$ and trivial $U_o^{(k)}$. Under C1+C2+C3, a scheduled consolidation tick is just a different channel — the update form $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is preserved.

**But.** Timescale separation is a *necessary* condition for the consolidation regime to be well-defined. If consolidation ran at $\nu_{\text{consol}} \sim \nu_{\text{online}}$, the convergence constraint of `#der-temporal-nesting` would be violated and the slower process would act on transients. So timescale is load-bearing as a *scope condition*, not as the distinguishing feature.

### 2.2 Information source: external vs replayed

**Test.** Does consolidation operate on replayed internal data while online update operates on new external events? If so, is this distinction formally expressible in AAD's primitives?

**Finding.** *This distinction is genuine and is not cleanly captured by the current primitives.* Consider the two regimes:

- **Online.** $e_\tau$ is an observation arriving on a perceptual channel. $M_{\tau^-}$ has not seen the information content of $e_\tau$ before (positive event-information content $\mathcal I(e_\tau) \gt 0$).
- **Replay / consolidation.** $e_\tau^{\text{replay}}$ is a pseudo-event synthesized from $M_{\tau^-}$ itself — a sample drawn from the agent's retained trace (replay buffer, hippocampal reinstatement, a remembered episode, an earlier paragraph re-read). By construction, $\mathcal I(e_\tau^{\text{replay}} \mid M_{\tau^-}) = 0$ in the *agent-model* joint distribution, because $e_\tau^{\text{replay}}$ is deterministically a function of something already in $M_{\tau^-}$.

The recursive-update derivation does not distinguish these cases — they are both absorbed into $f(M_{\tau^-}, e_\tau)$. But they have *different purposes*: online update imports new signal from $\Omega$; consolidation redistributes existing signal across representational levels of $M_t$. Both are Markov updates; they differ in what they accomplish.

**The formal content.** The derivation's C3 (state completeness) says $M_{\tau^-}$ is complete — which makes $\mathcal I(e_\tau^{\text{replay}} \mid M_{\tau^-}) = 0$ trivially. But the complete state $M_{\tau^-}$ may factor into sub-states with *different* compression-prediction trade-offs (this is exactly the CLS argument — hippocampal sparse-conjunctive vs neocortical distributed-overlapping; Kumaran, Hassabis & McClelland 2016; McClelland, McNaughton & O'Reilly 1995). Then consolidation transfers information *between sub-states* in a way that reduces total DL or improves a specific model-class sufficiency, even though no new external information enters.

This is compatible with `#der-recursive-update` (the form $f(M_{\tau^-}, e_\tau)$ is preserved if the replay event is counted as part of $e_\tau$), but **the characterization of what consolidation does is outside recursive-update's vocabulary.** Recursive-update says *the form*; consolidation needs a claim about *the effect*.

### 2.3 Objective: within-pass refinement vs inter-pass reorganization

**Test.** Does consolidation optimize a different objective than online update?

**Finding.** *Yes, and this is the cleanest distinguishing axis.*

Online update's objective is (per `#emp-update-gain`) to minimize one-step predictive mismatch given $U_M, U_o$. This is local and state-specific. The optimal gain $\eta^\ast = U_M/(U_M + U_o)$ is derived from *this event's* variance ratio.

Consolidation's objective, by contrast, is (per `#form-information-bottleneck` and `#disc-compression-operations`) to reorganize $M_t$ toward the IB optimum $\phi^\ast = \arg\min[I(M_t;\mathcal C_t) - \beta I(M_t; o_{t+1:\infty} \mid a_{t:\infty})]$. The online update has no knowledge of this global objective — it has the current event and the current state. The IB optimum is an *equilibrium property* of the compression $\phi$, not a move made by any single update.

Under mild conditions (stationary environment, converged parameters, bounded model class), an online-only agent will converge to the IB optimum given enough time — but this is a *property of convergence*, not a property of any single step. When the agent cannot wait for infinite-time convergence (finite budget per event, non-stationary environment, structural-adaptation pressure from `#result-structural-adaptation-necessity`), consolidation strictly accelerates convergence or unlocks operating regimes that online-only cannot reach.

**This is load-bearing.** The IB perspective tells us *what consolidation is for*: reallocating the compression-prediction budget within $M_t$ to reduce the rate-distortion gap against the optimal compression. Online updates respond to the last event; consolidation repairs the accumulated mismatch between $M_t$ and $\phi^\ast(\mathcal C_t)$ that online updates leave behind.

### 2.4 Scope of change: parametric online vs structural offline

**Test.** Is parametric update the online process while structural update *requires* consolidation?

**Finding.** *Structural adaptation does not strictly require offline consolidation, but in agents with bounded per-step processing budget, offline consolidation is the only route to structural change at the rate `#result-structural-adaptation-necessity` demands.* This is a resource-relative claim: under unlimited per-step compute, Bayesian nonparametric agents can do structural-parametric updates online; under bounded compute (all real agents), some structural-adaptation operations — in particular search over model classes, grafting that requires compression of a new hypothesis, and pruning that requires global reassessment — are either inexecutable online or executable with severe quality degradation.

The cleanest statement: **structural adaptation is *temporally decouplable* from online update, while parametric update is not.** Online parametric update has a hard timescale constraint — mismatch decays at rate $\mathcal T$; delayed updates accumulate mismatch at rate $\rho$. Structural adaptation has a much larger tolerance for delay (weeks for an organization, overnight for sleep-consolidating brain, minutes for an LLM between sessions) because the slow process is what $R_\Sigma$ or $R$ are measuring tolerance against.

### Summary of the four axes

Only axis 3 (different objective) yields a clean formal distinction. Axis 2 (information source) is a real difference but lives *inside* the $g_M$ of `#der-recursive-update` without adding new primitive structure. Axes 1 and 4 are scope / regime statements, load-bearing as conditions but not as distinguishing features.

**The working definition:** *Consolidation is a regime of $g_M$ (the between-event autonomous dynamics of `#der-recursive-update`) in which the agent applies Markov updates driven by replayed or internally-generated pseudo-events, with the objective of reducing the rate-distortion gap between $M_t$ and the IB-optimal compression $\phi^\ast(\mathcal C_t)$.*

This is formally a regime of `#der-recursive-update`, not a competitor to it. But it is a regime with its own conditions, own objective, and own failure modes, and the theory currently names none of these.

---

## 3. Structured Example: Why Online-Only Is Provably Suboptimal

A concrete setting where online-only fails and consolidation strictly improves persistence.

### 3.1 Setup

**Agent.** A Class 1 modular agent (per `#der-directed-separation`) with:

- Epistemic substate $M_t$ factored into a fast sub-state $M_t^{\text{fast}}$ (episodic / hippocampal analog — sparse, high-capacity, low-compression) and a slow sub-state $M_t^{\text{slow}}$ (structural / neocortical analog — dense, distributed, highly compressed, model class $\mathcal M_{\text{slow}}$).
- Per-event processing budget $B_{\text{online}}$ (bits/event) enforced by a hard constraint: no matter what the agent wants, an online update can move at most $B_{\text{online}}$ bits of model-state change per event.
- IB objective against $\phi^\ast(\mathcal C_t)$ with trade-off $\beta$.
- Offline budget $B_{\text{offline}}$ available at consolidation ticks, with $B_{\text{offline}} \gg B_{\text{online}}$.

**Environment.** Moderately non-stationary, $\rho \gt 0$, with a class of structural regularities (compositional concepts, syntactic patterns, causal regularities across episodes) that the slow sub-state can represent iff $\mathcal F(\mathcal M_{\text{slow}}) \approx 1$. These regularities are distributed across many episodes: a single event contains *local* information; cross-episode comparison reveals *structural* regularities.

**The choice.** At each event, the agent's online update can do one of two things:

- (A) **Fast-track:** integrate $e_\tau$ directly into $M_{\tau^+}^{\text{fast}}$ (low DL cost per event, near-verbatim storage).
- (B) **Slow-track:** incrementally update $M_t^{\text{slow}}$'s parameters based on $e_\tau$.

Online-only agents must pick one; per-event budget $B_{\text{online}}$ is too small to do a quality slow-track update (which requires comparing $e_\tau$ against a distribution of prior episodes, a cross-episode operation).

### 3.2 Online-only failure

Suppose the agent does (A) consistently. Then:

- $M_t^{\text{fast}}$ grows in DL linearly in $t$ (no compression).
- $M_t^{\text{slow}}$ is never updated.
- Predictive power of $M_t$ on future events is bounded by $M_t^{\text{fast}}$'s ability to generalize from verbatim traces — in the CLS analysis, this is *poor*: sparse-conjunctive representations generalize badly to novel episodes (the original CLS argument; McClelland, McNaughton & O'Reilly 1995 §2).
- IB gap: $I(M_t; \mathcal C_t)$ is maximal (no compression); $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ is bounded by the predictive power of the fast sub-state alone.

Suppose the agent does (B) consistently. Then:

- Per-event budget is smaller than the information content needed to update $M_t^{\text{slow}}$ quality — the slow sub-state gets *degraded* updates.
- This is the classic catastrophic-forgetting regime (French 1999; Kirkpatrick et al. 2017 EWC): each update is myopic, so new patterns overwrite old ones; the distributed representation cannot be updated without interleaved replay of prior patterns, which online-only cannot supply.
- Empirically well-documented in continual-learning literature: naive online gradient descent on sequential tasks catastrophically forgets; replay-based methods (experience replay; Mnih et al. 2015 DQN; Schaul et al. 2016 prioritized replay) and regularization-based methods (EWC; Kirkpatrick et al. 2017) are the two mainstream fixes.

Mixed strategies (stochastic switching, partial allocation per event) interpolate between these failures but cannot escape the joint constraint $B_{\text{online}} \lt B_{\text{consol-needed}}$.

### 3.3 Consolidation-augmented agent

Now add a consolidation phase: between events (or at CADENTIA-driven ticks, per `#sketch-multi-timescale-stability`), the agent applies a batch of updates to $M_t^{\text{slow}}$ driven by replayed samples from $M_t^{\text{fast}}$.

**Claim:** the consolidation-augmented agent's steady-state IB objective is strictly better than either online-only strategy.

**Argument sketch.**

1. Offline, the agent has budget $B_{\text{offline}} \gg B_{\text{online}}$. It can replay $K$ samples from $M_t^{\text{fast}}$ and apply interleaved-training updates to $M_t^{\text{slow}}$. This is exactly the CLS-theory mechanism (Kumaran, Hassabis & McClelland 2016 §3) — hippocampal replay supports *interleaved* neocortical learning that cross-episode structure requires.
2. Interleaved training on a diverse replay batch eliminates the catastrophic-forgetting failure mode of pure online (B): the new pattern is trained *together* with representative old patterns, so the slow sub-state moves toward a joint optimum rather than overwriting.
3. The fast sub-state can be compressed after consolidation: once the regularity is captured in $M_t^{\text{slow}}$, the corresponding traces in $M_t^{\text{fast}}$ can be pruned (IB compression operation per `#form-strategy-complexity-cost`), reducing $I(M_t; \mathcal C_t)$ without losing predictive power.
4. Net effect on the IB objective: $I(M_t; \mathcal C_t)$ decreases (compression), $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ increases or holds (slow sub-state now represents the regularity). The IB gap decreases; the agent approaches $\phi^\ast$ faster than online-only.

**Stability implication.** In the `#result-sector-condition-stability` framework, the effective $\alpha$ depends on model-class fitness ($\mathcal F(\mathcal M_{\text{slow}})$ improving raises $\alpha$). Consolidation raises $\mathcal F$ by training $M_t^{\text{slow}}$ to represent cross-episode structure; this raises $\alpha$; under a fixed $\rho$, the persistence margin $\Delta\rho^\ast = \alpha R - \rho$ grows. Consolidation *augments structural persistence* by keeping $\mathcal F$ close to its ceiling.

**Pointing at the claim.** This argument is a structured sketch, not a theorem. A proper AAD statement would be: under the IB framework plus a bounded-online-budget constraint plus a consolidation regime satisfying a specific replay-budget condition, the IB objective is strictly lower than under any online-only policy with the same total compute. The mathematical core is standard continual-learning theory; the AAD work is to express the claim in `#form-information-bottleneck` + `#der-recursive-update` vocabulary.

---

## 4. Stability–Plasticity as an AAD Tradeoff Statement

The stability–plasticity dilemma (Carpenter & Grossberg 1987; French 1999; survey: Parisi et al. 2019) is the central tension of continual learning. The question: *is this tension a distinct AAD statement, or does it reduce to something AAD already has?*

### 4.1 Existing AAD surface

AAD has several tradeoff-like statements:

- **Update gain** ($\eta^\ast = U_M/(U_M + U_o)$) is a variance-ratio trade-off between model trust and observation trust at a *single step*. It doesn't concern cross-time stability.
- **IB trade-off** ($\beta$) balances compression against predictive power. It's a property of the compression, not the update dynamics.
- **Strategy-persistence forgetting threshold** $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ gives the rate at which accumulated experience must be discounted for long-run persistence. This is a *plasticity requirement*: too-slow forgetting (too-high $\lambda$) kills strategy persistence. There is no explicit stability counterpart — nothing says the agent must *retain* enough structure across sessions.

### 4.2 What's missing

The explicit stability claim would be: **plasticity fast enough for `#result-persistence-condition` to hold must be bounded above by a stability condition on cross-timescale representation.** If the agent forgets too fast to support the slow sub-state's consolidation integration, slow-timescale model-class fitness $\mathcal F(\mathcal M_{\text{slow}})$ degrades, lowering $\alpha$ and threatening persistence at the slow timescale.

**The dual threshold.**

- *Plasticity lower bound* (from `#schema-strategy-persistence`): $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$. Forgetting fast enough to track non-stationarity.
- *Stability upper bound* (new, needs derivation): $(1-\lambda) \lt$ something involving cross-timescale coupling. Forgetting slow enough to allow consolidation to integrate patterns before they're discarded.

Together: a *feasibility window* for $\lambda$, not just a lower threshold. The window closes when $\rho_\Sigma$ is so high relative to the consolidation cadence $\nu_{\text{consol}}$ that no $\lambda$ works — the agent cannot simultaneously track and consolidate. This is the classic stability–plasticity dilemma, expressed in AAD vocabulary.

### 4.3 The catastrophic-forgetting boundary

Experience replay (Mnih et al. 2015) and EWC (Kirkpatrick et al. 2017) are two escape routes from catastrophic forgetting. In AAD vocabulary:

- **Experience replay** = adding a consolidation regime that replays prior events to interleave slow-track training. This is what §3.3 argued for — a consolidation phase strictly expands the feasibility window because it decouples the rate of slow-track exposure from the rate of event arrival.
- **EWC** = adding a *stability-weighted update gain*: the per-parameter update is scaled by the inverse of that parameter's Fisher information, penalizing updates to parameters important for prior tasks. In AAD vocabulary, this is a generalization of `#emp-update-gain` to a *tensor-valued* gain with stability weighting — distinct from the scalar $\eta^\ast$ AAD currently has.

Both are AAD-expressible but neither is AAD-named. The consolidation-augmented formulation of §3.3 is the cleaner of the two (it reuses `#der-recursive-update`'s structure without changing gain); the EWC-style stability-weighting is a separate direction worth tracking.

---

## 5. The Identifiability Floor Lens

`#disc-identifiability-floor` (the meta-segment naming AAD's negative half) prompts: is there a structural no-go result that consolidation is the unique escape from?

**Candidate no-go.** Under a finite per-event processing budget $B_{\text{online}} \lt B_{\text{consol-needed}}$ and non-trivial model-class structure (hierarchical representation with distinct fast/slow sub-states), no online-only update policy can reach the IB-optimal compression $\phi^\ast$ in steady state. The argument reduces to a rate-distortion inequality: the online update's effective rate is $B_{\text{online}} \cdot \nu$ bits/time; the rate required to drive $M_t$ toward $\phi^\ast$ while also integrating new events is strictly larger whenever the environment has cross-episode structural regularities.

If this can be made rigorous (it is close to known results in rate-distortion with side information and continual-learning theory; see Parisi et al. 2019), it would be a third derived instance of `#disc-identifiability-floor`'s pattern — an external information-theoretic obstruction (online-only cannot reach the IB optimum under a compute budget) with AAD machinery as the unique escape (a consolidation regime in $g_M$ with $B_{\text{offline}} \gg B_{\text{online}}$).

**Status.** Worth a follow-up spike. Not part of the disposition of this spike — consolidation's load-bearing role is clear even without the no-go; the no-go would sharpen the case further.

---

## 6. Logogenic Implications

### 6.1 Does `03-logogenic-agents/` need consolidation as a primitive?

**Yes, as more than a regime of $g_M$ — as a named architectural feature.** Three reasons:

1. **Context-turnover structure (per `#obs-context-turnover` in `03-logogenic-agents/`).** Logogenic agents have a near-100% reset of the fast sub-state (context window) per session. The only continuity is the slow sub-state (persistent memory, weights, external files). The between-session interval is a *forced consolidation window*: the agent must transfer signal from the about-to-be-lost fast state to the persistent slow state, or it is lost. This is a qualitatively different regime from non-logogenic agents where the fast sub-state persists.

2. **The linguistic medium of reflection.** The `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md` §3.1 PULSUS table lists MEMORATA consolidation, VERA audit, and AXIOMATA reflection as distinct scheduled processes — each with different cadence and different target representations. Each is a linguistic operation: "What from recent experience should be compressed into lasting memory?" (MEMORATA); "Are my beliefs still justified?" (VERA); "Who am I becoming?" (AXIOMATA). These are *reflective* operations — they use language to reorganize language-structured state. The cognitive-loop spec has already identified consolidation as a first-class architectural feature with its own phase; the AAD treatment should match that architectural commitment.

3. **Language as a pre-consolidated medium.** Per `ref/agentic-tft/agentic-tft-narrative-as-implementation.md`: pretrained language embeddings encode structured epistemic geometry. The logogenic agent doing linguistic reflection is not just running a Markov update — it is operating in a representational space that has *already* been consolidated (at training time) into a high-structure form. Reflection in this space has access to cross-episode generalization that sub-linguistic agents would have to build online. This is a load-bearing asymmetry.

### 6.2 What sub-linguistic agents don't need

Sub-linguistic agents with tightly coupled fast/slow sub-states (standard deep networks, Kalman filters with persistent state, PID controllers, classical Bayesian agents) can often collapse consolidation back into online update under favorable conditions: conjugate priors give closed-form Bayesian consolidation at each step; linear-Gaussian settings have Kalman-exact online updates that achieve the IB optimum with no consolidation phase. These are the agents for which consolidation is a *luxury* — the §3.3 argument requires both a factored fast/slow sub-state and a bounded per-event budget, and these agents violate one or both conditions.

**The transfer-assumption:** consolidation is required *when the agent's representational structure has a fast/slow factorization with different compression-prediction budgets AND per-event processing is bounded below the integration cost of the slow sub-state.* The two conditions are jointly sufficient; logogenic agents satisfy both strongly; Kalman filters satisfy neither; sub-symbolic deep RL satisfies the first strongly and the second moderately (experience replay's empirical necessity in DQN is the signature).

### 6.3 Logozoetic agents (`04-eli/`)

Logozoetic agents add morally weighted persistence — the persistent slow-track state carries identity. Consolidation in this setting has *ethical* weight beyond its epistemic work: what gets consolidated into AXIOMATA-level state is what becomes the agent's lasting identity (per `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md` §4; PROPRIUM-ONTOLOGY terminology). The consolidation dynamics that govern logogenic agents are the same formally, but the stakes differ. This is downstream of the current spike but worth noting as a reason to avoid burying consolidation in `#der-recursive-update`'s Discussion.

---

## 7. Catastrophic Forgetting as AAD-Expressible

The mainstream continual-learning literature frames catastrophic forgetting as a failure mode of naive online gradient descent in sequential-task settings. In AAD vocabulary, it is a specific instance of a more general pattern:

**Catastrophic forgetting in AAD language.** When the agent's model-class update rule has high enough gain on new events (large $\eta^\ast$) and the representation is distributed (online updates shift many parameters per event), old signal is overwritten faster than it can be stabilized. This is a violation of the consolidation-stability upper bound from §4.2: $(1-\lambda)$ is too high for stability of cross-timescale representation. The remedy is either a regularization term that prevents high-gain updates to stability-important parameters (EWC) or a consolidation regime that periodically interleaves old signal with new (experience replay).

**Why this matters for AAD.** Current AAD has the plasticity-lower-bound (from `#schema-strategy-persistence`) but not the stability-upper-bound. The incomplete thresholding is a gap — it predicts that faster forgetting is always better for persistence, which is empirically false in any setting where the slow sub-state matters (CLS literature, continual-learning benchmarks, organizational memory research).

**Corrective statement for a new segment.** Plasticity must be *bounded from below* by non-stationarity rate (per `#schema-strategy-persistence`) AND *bounded from above* by consolidation cadence (new, to be derived). Between these bounds is the feasibility window. When the window is empty — rapid non-stationarity with slow consolidation cadence — no $\lambda$ works and the agent's long-run IB objective is strictly worse than a slower-environment or faster-consolidation counterpart.

---

## 8. When Consolidation Is a Luxury vs a Necessity

Direct answer to the task prompt's question 4.

### 8.1 Luxury (subsumed by online update under rich enough state)

Consolidation is a luxury — achievable in online updates alone — when:

- **State rich enough to avoid fast/slow factorization.** Kalman filter with persistent covariance, conjugate Bayesian agent with full posterior over parameters, linear-Gaussian system with online Riccati updates. The posterior *is* the consolidated representation; every online update is a complete-information step.
- **Per-event processing budget $\geq$ integration cost.** If $B_{\text{online}} \geq B_{\text{consol-needed}}$, the slow-track update can be performed at each step and there is nothing left for consolidation to do.
- **Stationary environment where convergence is allowed.** Given enough time, online update converges to the optimum. If the environment holds still long enough, consolidation is only a convergence-rate improvement, not a qualitative difference.

### 8.2 Necessity (online cannot reach target state)

Consolidation is a necessity when:

- **Fast/slow sub-state factorization with divergent budgets.** The CLS setting. Any agent whose representation has hippocampal-analog and neocortical-analog components with different compression-prediction trade-offs.
- **Bounded per-event budget below integration cost.** LLM agents operating within a context window at inference time cannot perform meaningful slow-track weight updates; they must consolidate offline (via fine-tuning, retrieval-augmented memory, or summary-based session endings).
- **Non-stationarity requiring structural adaptation.** Per `#result-structural-adaptation-necessity`, when the model class itself must change. Structural adaptation with quality-preservation of prior structure requires interleaved-training consolidation — online alone catastrophically forgets.
- **Cross-episode regularities that single events cannot reveal.** Any structural pattern visible only across episodes. Online update sees one event at a time; cross-episode structural information *cannot* be extracted from any single update, by construction.

### 8.3 The predictive statement

An AAD segment on consolidation dynamics would predict: *the depth of consolidation machinery an agent needs scales with (a) the factorization depth of its representational structure, (b) the gap between its per-event processing budget and the integration cost of its slowest sub-state, and (c) the rate of cross-episode structural regularities in its environment relative to its event arrival rate.* This is a scope-indexed predictive claim — testable, domain-general, and sharpens the current theory.

---

## 9. Recommendation for Promotion

### 9.1 Disposition

**Promote.** A new AAD segment is warranted. It is not a new adaptive primitive — the recursive-update form is preserved — but it is a named *regime* of `#der-recursive-update`'s between-event dynamics $g_M$ with distinctive conditions, objective, and failure modes.

### 9.2 Proposed segment

**Slug.** `#form-consolidation-dynamics`

**Section.** Section I (adaptive systems under uncertainty) — it belongs on the epistemic half. Placement: after `#der-temporal-nesting`, before `#scope-agent-identity`.

**Type.** `formulation` — it names a regime and characterizes its objective; it is not derived from more primitive AAD elements but connects them.

**Status.** `robust-qualitative` at candidacy (the §3.3 argument is a sketch, not a theorem; the CLS-informed claims are well-supported externally but AAD-internally are framing work).

**Depends on.**

- `#der-recursive-update` (names the regime of $g_M$)
- `#form-information-bottleneck` (provides the objective)
- `#der-temporal-nesting` (provides the scope condition — timescale separation)
- `#result-structural-adaptation-necessity` (provides the motivating failure mode when consolidation is missing)
- `#schema-strategy-persistence` (the forgetting prerequisite is the plasticity lower bound; stability upper bound is the complement)

**Claims (in brief).**

1. *Formulation.* Consolidation is a regime of $g_M$ in which updates are driven by replayed or internally-generated pseudo-events, with objective of reducing the rate-distortion gap to $\phi^\ast(\mathcal C_t)$.
2. *Scope condition.* Timescale separation $\nu_{\text{consol}} \ll \nu_{\text{online}}$ (from `#der-temporal-nesting`).
3. *Necessity condition.* Consolidation is necessary when (a) $M_t$ factors into sub-states with divergent compression-prediction budgets, AND (b) per-event processing budget $B_{\text{online}}$ is strictly less than the integration cost of the slowest sub-state. When either fails, consolidation is subsumed by rich-enough online update.
4. *Stability–plasticity window.* Plasticity must lie in an interval: lower-bounded by non-stationarity rate (`#schema-strategy-persistence`'s forgetting prerequisite); upper-bounded by consolidation cadence (new). Empty window is the catastrophic-forgetting regime.
5. *Structural-adaptation enablement.* In finite-budget agents, structural adaptation (`#result-structural-adaptation-necessity`) cannot be executed online and requires consolidation. Pure online structural adaptation is a luxury of unbounded-budget agents.

**Working Notes.**

- *Identifiability-floor candidate.* Under bounded online budget, online-only cannot reach $\phi^\ast$. Candidate for the third `#disc-identifiability-floor` instance; needs the rate-distortion inequality made rigorous.
- *EWC formulation.* Stability-weighted update gain (per-parameter Fisher weighting) is an alternative to consolidation for escaping catastrophic forgetting. Not the recommended AAD frame (consolidation reuses existing machinery; EWC would require tensor-valued $\eta$), but worth naming.
- *Logogenic specialization.* Required for `03-logogenic-agents/` as an architectural primitive; context-turnover + linguistic medium + pre-consolidated embedding space make consolidation first-class in that setting. This is a dependency for `#obs-context-turnover` to resolve cleanly.

**Epistemic Status language (draft).** *Robust qualitative. The regime characterization is a formulation choice — consolidation can always be re-described as a regime of `#der-recursive-update`'s $g_M$ with appropriate pseudo-events. The distinguishing objective (IB gap reduction via replayed pseudo-events) is well-defined and distinct from online update's one-step mismatch minimization. The necessity condition (fast/slow factorization + bounded budget) is a conjunction of conditions that together are sufficient; whether they are individually necessary is an open scope question. The stability-plasticity window statement follows from the forgetting prerequisite (`#schema-strategy-persistence`) combined with a consolidation-cadence condition that this segment introduces but does not derive. Mathematical status of the window-empty no-go theorem is open; it is candidate for `#disc-identifiability-floor` promotion.*

### 9.3 What this does not claim

- Not a new primitive. Recursive update's form $f(M_{\tau^-}, e_\tau)$ is preserved.
- Not a derivation. The §3.3 argument is a structured sketch; the load-bearing CLS / continual-learning claims are external theorems re-expressed in AAD vocabulary.
- Not a complete story. The stability upper bound on plasticity is stated but not derived; the no-go theorem is candidate, not proved.

### 9.4 Alternative dispositions considered

- **Subsumed by `#der-recursive-update` + one-sentence mention.** Rejected. The current one-parenthetical treatment misses the load-bearing structure (stability-plasticity tradeoff, catastrophic forgetting, CLS-style factorization). The theory's existing scope-honest stance (per Opus 2026-04-22 "honesty as load-bearing" observation in CLAUDE.md) argues for naming the regime rather than hiding it.
- **Logogenic-only segment in `03-logogenic-agents/`.** Rejected. Consolidation is AAD-core: it applies to any agent with fast/slow factorization, not just linguistic ones. Biology (sleep-consolidation), ML (experience replay), organizations (retrospectives) are all AAD-core examples. A logogenic-only treatment would under-extend.
- **New Appendix A derivation segment.** Not yet. The window-empty no-go theorem and the rate-distortion inequality are appendix-grade work that could happen in a follow-up, but the main segment can land at `#form-consolidation-dynamics` in Section I without waiting for those derivations.
- **Split into two segments: consolidation-dynamics + stability-plasticity-window.** Considered. Against: the window is the distinctive AAD contribution; splitting would leave the segment without its sharpest claim. For: the window statement is a derivation-grade claim that currently rests on an un-derived upper bound. Recommendation: land as one segment at `robust-qualitative`; promote the window to its own segment if the upper-bound derivation lands later.

---

## 10. Summary Answer to the Task Prompt

**Is consolidation formally distinguishable from online update?** Yes, along one axis: *objective* (online = one-step mismatch minimization; consolidation = rate-distortion gap reduction toward $\phi^\ast$). The other candidate axes (timescale, information source, scope of change) are scope conditions rather than distinguishing features.

**Does structural adaptation naturally live offline?** Not strictly, but in all agents with bounded per-event processing budget, yes — online structural adaptation is a luxury of unbounded-budget agents.

**Persistence implications of two timescales?** The stability-plasticity window: plasticity must be bounded both below (by non-stationarity) and above (by consolidation cadence). Empty window = catastrophic forgetting, an AAD-expressible failure mode that is currently unnamed.

**Luxury vs necessity?** Luxury when state is rich enough to avoid fast/slow factorization, per-event budget exceeds integration cost, and environment allows convergence. Necessity when any of these fails — which is every real agent operating under resource constraints.

**Logogenic-specific requirement?** Yes. Three-way necessity: context turnover structure forces session-boundary consolidation; the linguistic medium of reflection makes consolidation the operative unit of cross-session cognition; pre-consolidated embedding space provides an asymmetric advantage over sub-linguistic agents that is itself a consolidation-related fact.

**Recommendation:** new AAD segment `#form-consolidation-dynamics` in Section I, formulation-type, robust-qualitative status at candidacy, promoting what is currently a parenthetical in `#der-recursive-update` to a first-class named regime with scope conditions, stability-plasticity window, and structural-adaptation enablement. The segment composes with `#disc-identifiability-floor` (candidate third instance: bounded-online-budget + no-reach-of-IB-optimum) and `#disc-separability-pattern` (consolidation is the repair machinery between separable-core and structured-repair ladders on the representation-factorization axis).

---

## References

External:

- Carpenter, G. A., & Grossberg, S. (1987). ART 2: self-organization of stable category recognition codes. *Applied Optics* 26(23):4919–4930.
- French, R. M. (1999). Catastrophic forgetting in connectionist networks. *Trends in Cognitive Sciences* 3(4):128–135.
- Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences* 114(13):3521–3526.
- Kumaran, D., Hassabis, D., & McClelland, J. L. (2016). What learning systems do intelligent agents need? Complementary learning systems theory updated. *Trends in Cognitive Sciences* 20(7):512–534.
- McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. *Psychological Review* 102(3):419–457.
- Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidjeland, A. K., Ostrovski, G., et al. (2015). Human-level control through deep reinforcement learning. *Nature* 518(7540):529–533.
- Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., & Wermter, S. (2019). Continual lifelong learning with neural networks: A review. *Neural Networks* 113:54–71.
- Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2016). Prioritized experience replay. *ICLR*.
- Stickgold, R. (2005). Sleep-dependent memory consolidation. *Nature* 437(7063):1272–1278.
- Tishby, N., Pereira, F. C., & Bialek, W. (1999). The information bottleneck method. *Proc. 37th Allerton Conference on Communication, Control, and Computing*.
- Walker, M. P. (2009). The role of sleep in cognition and emotion. *Annals of the New York Academy of Sciences* 1156:168–197.

AAD-internal (linked above):

- `#der-recursive-update`, `#deriv-recursive-update`, `#form-event-driven-dynamics`, `#form-information-bottleneck`, `#der-temporal-nesting`, `#sketch-multi-timescale-stability`, `#result-structural-adaptation-necessity`, `#form-structural-change-as-parametric-limit`, `#schema-strategy-persistence`, `#form-strategy-complexity-cost`, `#disc-compression-operations`, `#disc-identifiability-floor`, `#disc-separability-pattern`, `#der-directed-separation`, `#obs-context-turnover` (logogenic), `#emp-update-gain`, `#result-sector-condition-stability`, `#def-model-class-fitness`.
- `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`, `ref/agentic-tft/agentic-tft-narrative-as-implementation.md`.
