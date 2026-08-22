# Prior Art Assessment

**Date**: March 2026 **Status**: First read assessment. These are initial reactions, not definitive positioning. Each entry may need re-reading as AAD develops.

---

## 1. Hafez et al., "A Mathematical Theory of Agency and Intelligence" (Feb 2026)

### What It Does

Introduces **Bi-predictability (P)** — the fraction of total information shared between observations (S), actions (A), and outcomes (S'):

    P = MI(S, A; S') / [H(S) + H(A) + H(S')]

P measures coupling efficiency: how much of the total informational budget is actually shared between the agent-environment interaction. Key results:

- P ≤ 1/2 for classical systems (provable bound); P can reach 1 for quantum
- Agency introduces internal degrees of freedom that *reduce* P — you trade maximal coherence for the ability to act
- **Forward predictive uncertainty** H_f = H(S'|S,A): how opaque the world is to the agent
- **Backward predictive uncertainty** H_b = H(S,A|S'): how opaque the agent is to the world
- ΔH = H_f - H_b localizes where coupling breaks down

**Agency** is defined as three conditions:
1. Choice: H(A|S) > 0 — actions not fully determined by state
2. Effect: MI(A;S'|S) > 0 — actions actually change outcomes
3. Predictive asymmetry: |ΔH| > 0 — forward and backward uncertainty differ

**Intelligence** adds three more:
1. Learning: increase MI(S,A;S') over time
2. Self-monitoring: compute P from own interaction stream
3. Adaptation: adjust {S}, {A}, {S'} — reshape the interface

They propose an **Information Digital Twin (IDT)** — a sidecar process that monitors P and ΔH in real-time, inspired by thalamocortical regulation. Tested on double pendulum (physical baseline), RL agents (HalfCheetah), and LLM multi-turn conversations.

**Key empirical finding**: Their IDT detects coupling degradation (drift, perturbation) faster and more reliably than reward-based monitoring (89% vs 44% detection rate, 4.4x lower latency). P tracks interaction *structure* rather than task *performance*.

### What It Doesn't Do

- **No treatment of goals or intent.** P measures how tightly the agent-environment coupling works, not what the agent is trying to achieve. The same P value could describe an agent perfectly pursuing the wrong goal or imperfectly pursuing the right one. The goal/intent gap we identified in TFT is equally present here — arguably more so, since they don't even have TFT's black-box value function.

- **No dynamics.** P is a *diagnostic metric*, not a dynamical theory. It measures coupling efficiency at a point in time but doesn't describe how that coupling evolves, what drives it, or what happens when it degrades. AAD/TFT describes the dynamics; Hafez measures the temperature.

- **No adversarial treatment.** No multi-agent coupling, no adversarial tempo advantage, no effects spiral. Their framework is single-agent-environment.

- **No structural adaptation formalism.** Their "adaptation" (adjusting {S},{A},{S'}) is listed as a condition for intelligence but not formalized. TF-10's Prop 10.1 and the destruction-creation cycle are absent.

- **No causal hierarchy.** Despite operating in the information-theoretic space where Pearl's levels would be natural, they don't distinguish associational / interventional / counterfactual information. P aggregates all of it.

- **No multi-agent dynamics.** No treatment of teams, communication, trust, shared intent, or adversarial coupling.

### Relationship to AAD

**Complementary, not competing.** They provide a diagnostic metric (P) that could be used to *measure* quantities that AAD's dynamics *predict*. Specifically:

- Their P might be expressible in terms of TFT quantities. A rough mapping:
  high T (tempo) should correlate with high P (good coupling). Low η* (poor gain) should manifest as high H_f (agent's predictions are poor). The relationship isn't exact — P is a ratio while T is a rate — but the structural correspondence is suggestive.

- Their H_f / H_b decomposition is a different cut than TFT's U_M / U_o but potentially informative. H_f ("world is opaque to agent") relates to U_o + model error. H_b ("agent is opaque to world") relates to action ambiguity — multiple internal states leading to same outcome. This isn't something TFT currently measures.

- Their agency/intelligence distinction maps loosely: their "agency" ≈ TFT's scope condition (TF-01); their "intelligence" ≈ TFT's full machinery (learning = TF-06, self-monitoring ≈ meta-model, adaptation ≈ TF-10).

- Their IDT concept (monitoring P as a sidecar) could be a practical instantiation of what AAD would call "coupling health monitoring" — a meta-observation about the quality of the agent-environment interaction.

**Positioning**: AAD should cite Hafez as a complementary information-theoretic diagnostic, note that P could potentially be derived from or mapped to AAD quantities, and point out that their framework shares the goal/intent gap: measuring coupling quality without asking what the coupling is *for*.

---

## 2. IBM, "Agentic AI Needs a Systems Theory" (Miehling et al., 2025)

### What It Does

A **position paper** / call-to-arms arguing that agentic AI development is too focused on individual model capabilities and needs a systems-theoretic perspective. NOT a theory itself — an argument for why one is needed.

**Functional agency** (Definition 1): A system possesses functional agency if:
1. Action generation: capable of generating actions toward an objective
2. Outcome model: capable of representing action-outcome relationships
3. Adaptation: capable of adapting behavior when the outcome model changes

Each condition exists on a spectrum:
- Action generation: reactive → stateful → epistemic
- Outcome model: association → intervention → counterfactual (Pearl's hierarchy)
- Adaptation: contextual → parametric → reflective

**Key argument**: It's not necessary for every component to be highly functionally agentic for the system as a whole to possess high functional agency. Agency can EMERGE from interaction.

**Three emergence mechanisms:**
1. Environment enhances cognition (embodied cognition, multimodal integration)
2. Prediction enables reasoning (free energy principle, hierarchical predictive processing, prediction error minimization → causal models emerge)
3. Prediction + interaction enables metacognition (confidence calibration through social interaction → shared representations)

**Open challenges they identify:**
- World models (how to build/maintain)
- Causal reasoning (how to achieve beyond correlation)
- Metacognitive awareness (self-monitoring)
- Human-AI interaction dynamics
- Safety and governance in multi-agent settings

### What It Doesn't Do

- **Not a theory.** It's a position paper arguing for the need. It identifies the void but doesn't fill it. No formal definitions beyond functional agency, no dynamics, no proofs, no predictions.

- **Goal/intent is mentioned but not formalized.** Their functional agency requires "action in the direction of some objective" but the objective is given, not modeled. They note the difference between "solution autonomy" (autonomy in means) and "goal autonomy" (autonomy in ends) but don't develop the latter.

- **No feedback dynamics.** No mismatch signal, no gain, no tempo, no persistence condition. Their "adaptation" is a condition, not a process.

- **No adversarial treatment.** Cooperative and competitive interaction is mentioned but not formalized.

- **Pearl's hierarchy is used but not developed.** They place it in the outcome model spectrum but don't build on it the way TF-02 does.

### Relationship to AAD

**They are calling for what AAD provides.** Almost literally:

- "The field would benefit from a common theoretical language" — AAD provides the mathematical language.
- They want to understand emergent behavior from interaction dynamics — AAD's multi-agent framework (from TFT Appendix F) + shared intent formalization provides the tools.
- Their functional agency definition is weaker than AAD's scope but compatible.
  AAD's scope (TF-01 specialized) is more precise; their three conditions map to elements of TF-01 + TF-03 + TF-10.
- Their causal hierarchy usage aligns with TF-02.
- Their emergence mechanisms (predictive processing → causal models) describe at a qualitative level what TFT formalizes quantitatively (mismatch → model update → structural adaptation).

**Positioning**: AAD should cite this paper as articulating the need that AAD addresses. Their functional agency definition can be mapped to AAD's scope. Their emergence mechanisms can be grounded in AAD's formal dynamics. Their open challenges (world models, causal reasoning, metacognition, human-AI dynamics, safety) are all within AAD's scope.

**A specific opportunity**: Their emphasis on emergence — simple agents producing complex system behavior through interaction — is something AAD can formalize through the multi-agent framework. The team persistence condition from Appendix F already shows how cooperative communication tempo enables persistence in environments where individuals fail. AAD could extend this to show how shared intent enables goal-achievement that no individual agent could manage.

---

## 3. FAST Workshop (AAAI 2026) — Selective Assessment

17 papers presented. Most are narrow/applied. The most relevant to AAD:

### High Relevance

**#7: "From Agentic AI to Autonomous Agents"** (Shiwali Mohan)
- Revisits computational agency theory from AI subdisciplines, maps modern foundation models to established theory. Directly relevant to AAD's positioning — we should read this to understand the state of computational agency theory and ensure AAD's framing is well-informed.

**#9: "Leapsight: A Functional Account of Mediation Between Perception and Action"** (Bagiński & Jha)
- Introduces functional account of agency focusing on "sustained coordination between internal representations and environment." Sounds structurally similar to what AAD does. Need to read to check overlap.

### Medium Relevance

**#6: "Formalizing Observability in Agentic AI Systems"** (Lotito & Pronesti)
- Observability layers for monitoring agent-agent and agent-environment interfaces. Related to TFT's observation channels and the Hafez IDT concept.

**#16: "The Multi-Agent Off-Switch Game"** (Agrawal et al.)
- Demonstrates individually corrigible agents become collectively incorrigible through strategic interaction. Related to AAD's persistence/goal tradeoff and multi-agent adversarial dynamics.

**#11: "Proactive Interference Reveals Working Memory Limits in LLMs"** (Wang & Sun)
- Cognitive science paradigm showing LLMs suffer from interference in state maintenance. Directly relevant to the 100% turnover problem.

### Low Relevance (to AAD's foundational theory)

The remaining papers are either applied (evaluation metrics, federated learning, constrained workflows), ethical/governance-focused (AI moral status, safety), or too narrow (AGI measurement, wireheading, scheming) to be directly relevant to AAD's foundational theory work.

---

## 4. Synthesis: Where AAD Stands

### The Void Is Confirmed

Neither Hafez nor IBM fills the void. Hafez provides a diagnostic metric without dynamics or goals. IBM describes the need without providing the theory. The FAST workshop papers are either applied or narrow. BDI (from our earlier survey) provides architecture without dynamics.

**No existing work provides:**
1. Mathematical dynamics for adaptive agents (mismatch, gain, tempo) — TFT does
2. Goals/intent as first-class objects with their own mismatch and update — nobody does
3. Shared intent with information-theoretic weight — nobody does
4. The full continuum from survival to purposeful agency — nobody does
5. Adversarial dynamics with formal tempo advantage — TFT does
6. Domain instantiation with measurable quantities — TST begins to

AAD, built on TFT + the goal/intent extension, would be the first to provide all six. This is the unique contribution.

### Positioning Strategy

1. **Cite Hafez as complementary metric.** Their P could be a diagnostic for AAD's dynamics — measuring coupling quality that AAD's tempo/gain/persistence machinery predicts. Note the shared goal/intent gap.

2. **Cite IBM as articulating the need.** Their position paper calls for what AAD provides. Their functional agency maps to AAD's scope. Their emergence mechanisms get formal grounding in AAD's dynamics.

3. **Cite BDI as the architecture AAD gives dynamics to.** BDI named the parts (Belief ≈ M_t, Desire ≈ G_t, Intention ≈ committed goals). AAD provides the physiology: how beliefs and desires update, interact, and drive action.

4. **Cite active inference as the closest theoretical competitor.** FEP has prior preferences (≈ G_t) and unifies perception/action. AAD differs in foundation (causal feedback vs. free energy), accessibility (measurable quantities vs. free energy), and scope (adversarial, multi-agent, shared intent).

5. **Don't overclaim.** AAD is being developed. The goal/intent extension is speculative. The math hasn't been worked out. Position honestly: TFT provides the adaptive foundation (that's solid); the purposeful agency extension is the hypothesis under development.

### Reading Priorities (Updated)

1. ~~Hafez et al.~~ [READ] — complementary, not competing
2. ~~IBM systems theory~~ [READ] — they call for what we're building
3. **Mohan, "From Agentic AI to Autonomous Agents"** — computational agency theory state-of-the-art
4. **Bagiński & Jha, "Leapsight"** — check for overlap in functional account
5. **Bungay, *The Art of Action*** — shared intent source material
6. **Friston, active inference with prior preferences** — closest competitor, need to understand the precise formal differences

---

## 5. Deeper Cross-Mapping (March 2026, second pass)

Detailed analysis of what each paper can *concretely inform* for AAD, beyond the first-read positioning above.

### Hafez → AAD: Specific Technical Connections

1. **P as measurable proxy for AAD dynamics.** High tempo (T) should correlate with high P. The persistence threshold (T > ρ/δ_critical) may have a P-space analog: P dropping below some value when persistence fails. This could provide an empirical measurement path for AAD's theoretical predictions — especially useful since AAD's quantities (T, η*, ρ) are harder to measure directly in complex systems.

2. **H_f / H_b is a different cut than U_M / U_o.** AAD decomposes mismatch into model uncertainty vs. observation uncertainty. Hafez decomposes into "world opaque to agent" (H_f) vs. "agent opaque to world" (H_b). These are orthogonal. H_b captures action ambiguity — multiple internal states leading to indistinguishable outcomes. AAD currently has no analog of H_b. This matters for legibility, coordination, and shared intent (#410). An agent that is opaque to its environment (high H_b) is harder for teammates to model and coordinate with.

3. **Agency/intelligence distinction maps to AAD's spectrum.** Hafez's "agency without intelligence" ≈ AAD's reactive-to-adaptive quadrants (M_t machinery without self-monitoring). Hafez's "intelligence" requires self-monitoring and adaptation ≈ AAD's structural-adaptation (#200) + meta-level monitoring. This gives AAD a clean external reference point for the agent-spectrum (#210).

4. **IDT as AAD persistence monitor.** The "Information Digital Twin" — a sidecar monitoring P in real-time — is a practical architecture that could instantiate AAD's persistence monitoring. An AAD-informed IDT would monitor not just coupling quality but *purposeful* coupling quality: is the coupling serving O_t? Hafez's IDT detects drift (coupling degradation) but not goal misalignment. AAD could extend it.

### IBM → AAD: The Manifesto Mapping

1. **IBM's functional agency spectra map to AAD's existing structure:**
   - Action generation (reactive → stateful → epistemic) ≈ agent-spectrum (#210)
   - Outcome model (association → intervention → counterfactual) ≈ causal hierarchy (#060, #070)
   - Adaptation (contextual → parametric → reflective) ≈ recursive-update (#130) through structural-adaptation (#200)

2. **IBM's "controlling emergence of subgoals" (§4.3) is directly addressed by AAD.** They note: the longer the chain of subgoals, the weaker the constraint from the human's initial task specification. This IS compound probability decay (#260). AAD already has the math for why this happens and what it implies.

3. **IBM's "residual control rights" maps to δ_sat disambiguation.**
   When should a subordinate agent revise vs. escalate? AAD's cascade (check M_t, then Π, then N_h, then revise O_t) provides a principled answer. Their discussion of risk accumulation from sequences of local decisions connects to compound probability decay and observability dominance (#270).

4. **IBM's "prediction + interaction enables metacognition"** — where confidence calibration through social interaction produces shared representations — connects to AAD's shared-intent gap (#410, #415). AAD's IB-compressed shared intent could be the *formalism* for their qualitative story about shared representations.

### What AAD Currently Answers from the Manifesto

| IBM Requirement | AAD Status | Assessment |
|---|---|---|
| Common theoretical language | Sections I–II vocabulary | Partial — formalism exists but Section II not in src/ yet |
| Emergent behavior from interaction | Section III (multi-agent) | Foundation exists (adversarial tempo proved); cooperative gaps remain |
| Causal reasoning formalization | TF-02 + causal hierarchy + loop-as-Level-2 | Strong — cleaner than IBM's qualitative FEP story |
| Metacognitive awareness | Persistence monitoring, δ_strategic | Partial — pieces exist, not packaged as "metacognition" |
| World model dynamics | M_t update machinery | Strong — TFT's core, simulation-validated |
| Multi-agent safety/governance | Shared intent, adversarial dynamics | Sketched, not formalized |
| Spectrum of agency | Agent-spectrum (#210) | Yes, richer than IBM's |

### Honest Positioning Statement (for eventual paper)

AAD answers IBM's call with a mathematical framework that provides the dynamics IBM identifies as missing, incorporates the coupling diagnostics Hafez develops, extends BDI with formal dynamics, and differentiates from active inference in accessibility and scope.

The honest framing: "IBM called for a theory. We provide a framework with these properties [list]. Here is what's derived, what's hypothesized, and what remains open." Lead with Section I (proved, simulated) and Section II (the purposeful-agent derivation chain), with Sections III–V as "the theory extends to" demonstrations.

The risk is over-claiming. AAD's unique contributions beyond existing fields (control theory, causal inference, BDI) are:
1. The integration itself — connecting fields under one framework with consistent notation and derivation chains
2. Specific novel results: satisfaction gap / control regret split, G_t complexity bounded by M_t capacity, compound probability decay as formal plan fragility, feedback loop as Level 2 causal access, adversarial tempo exponents
3. The software domain as both testbed and recursive instantiation

Don't present as revolutionary new mathematics. Present as a unifying framework with specific novel results embedded within the integration.
