# Prior Art Assessment

**Date**: March 2026
**Status**: First read assessment. These are initial reactions, not definitive
positioning. Each entry may need re-reading as ACT develops.

---

## 1. Hafez et al., "A Mathematical Theory of Agency and Intelligence" (Feb 2026)

### What It Does

Introduces **Bi-predictability (P)** — the fraction of total information shared
between observations (S), actions (A), and outcomes (S'):

    P = MI(S, A; S') / [H(S) + H(A) + H(S')]

P measures coupling efficiency: how much of the total informational budget is
actually shared between the agent-environment interaction. Key results:

- P ≤ 1/2 for classical systems (provable bound); P can reach 1 for quantum
- Agency introduces internal degrees of freedom that *reduce* P — you trade
  maximal coherence for the ability to act
- **Forward predictive uncertainty** H_f = H(S'|S,A): how opaque the world is
  to the agent
- **Backward predictive uncertainty** H_b = H(S,A|S'): how opaque the agent is
  to the world
- ΔH = H_f - H_b localizes where coupling breaks down

**Agency** is defined as three conditions:
1. Choice: H(A|S) > 0 — actions not fully determined by state
2. Effect: MI(A;S'|S) > 0 — actions actually change outcomes
3. Predictive asymmetry: |ΔH| > 0 — forward and backward uncertainty differ

**Intelligence** adds three more:
1. Learning: increase MI(S,A;S') over time
2. Self-monitoring: compute P from own interaction stream
3. Adaptation: adjust {S}, {A}, {S'} — reshape the interface

They propose an **Information Digital Twin (IDT)** — a sidecar process that
monitors P and ΔH in real-time, inspired by thalamocortical regulation. Tested
on double pendulum (physical baseline), RL agents (HalfCheetah), and LLM
multi-turn conversations.

**Key empirical finding**: Their IDT detects coupling degradation (drift,
perturbation) faster and more reliably than reward-based monitoring (89% vs 44%
detection rate, 4.4x lower latency). P tracks interaction *structure* rather
than task *performance*.

### What It Doesn't Do

- **No treatment of goals or intent.** P measures how tightly the
  agent-environment coupling works, not what the agent is trying to achieve.
  The same P value could describe an agent perfectly pursuing the wrong goal
  or imperfectly pursuing the right one. The goal/intent gap we identified in
  TFT is equally present here — arguably more so, since they don't even have
  TFT's black-box value function.

- **No dynamics.** P is a *diagnostic metric*, not a dynamical theory. It
  measures coupling efficiency at a point in time but doesn't describe how
  that coupling evolves, what drives it, or what happens when it degrades.
  ACT/TFT describes the dynamics; Hafez measures the temperature.

- **No adversarial treatment.** No multi-agent coupling, no adversarial tempo
  advantage, no effects spiral. Their framework is single-agent-environment.

- **No structural adaptation formalism.** Their "adaptation" (adjusting
  {S},{A},{S'}) is listed as a condition for intelligence but not formalized.
  TF-10's Prop 10.1 and the destruction-creation cycle are absent.

- **No causal hierarchy.** Despite operating in the information-theoretic space
  where Pearl's levels would be natural, they don't distinguish associational /
  interventional / counterfactual information. P aggregates all of it.

- **No multi-agent dynamics.** No treatment of teams, communication, trust,
  shared intent, or adversarial coupling.

### Relationship to ACT

**Complementary, not competing.** They provide a diagnostic metric (P) that
could be used to *measure* quantities that ACT's dynamics *predict*. Specifically:

- Their P might be expressible in terms of TFT quantities. A rough mapping:
  high T (tempo) should correlate with high P (good coupling). Low η* (poor
  gain) should manifest as high H_f (agent's predictions are poor). The
  relationship isn't exact — P is a ratio while T is a rate — but the
  structural correspondence is suggestive.

- Their H_f / H_b decomposition is a different cut than TFT's U_M / U_o but
  potentially informative. H_f ("world is opaque to agent") relates to U_o +
  model error. H_b ("agent is opaque to world") relates to action ambiguity —
  multiple internal states leading to same outcome. This isn't something TFT
  currently measures.

- Their agency/intelligence distinction maps loosely: their "agency" ≈ TFT's
  scope condition (TF-01); their "intelligence" ≈ TFT's full machinery
  (learning = TF-06, self-monitoring ≈ meta-model, adaptation ≈ TF-10).

- Their IDT concept (monitoring P as a sidecar) could be a practical
  instantiation of what ACT would call "coupling health monitoring" — a
  meta-observation about the quality of the agent-environment interaction.

**Positioning**: ACT should cite Hafez as a complementary information-theoretic
diagnostic, note that P could potentially be derived from or mapped to ACT
quantities, and point out that their framework shares the goal/intent gap:
measuring coupling quality without asking what the coupling is *for*.

---

## 2. IBM, "Agentic AI Needs a Systems Theory" (Miehling et al., 2025)

### What It Does

A **position paper** / call-to-arms arguing that agentic AI development is too
focused on individual model capabilities and needs a systems-theoretic
perspective. NOT a theory itself — an argument for why one is needed.

**Functional agency** (Definition 1): A system possesses functional agency if:
1. Action generation: capable of generating actions toward an objective
2. Outcome model: capable of representing action-outcome relationships
3. Adaptation: capable of adapting behavior when the outcome model changes

Each condition exists on a spectrum:
- Action generation: reactive → stateful → epistemic
- Outcome model: association → intervention → counterfactual (Pearl's hierarchy)
- Adaptation: contextual → parametric → reflective

**Key argument**: It's not necessary for every component to be highly
functionally agentic for the system as a whole to possess high functional
agency. Agency can EMERGE from interaction.

**Three emergence mechanisms:**
1. Environment enhances cognition (embodied cognition, multimodal integration)
2. Prediction enables reasoning (free energy principle, hierarchical predictive
   processing, prediction error minimization → causal models emerge)
3. Prediction + interaction enables metacognition (confidence calibration
   through social interaction → shared representations)

**Open challenges they identify:**
- World models (how to build/maintain)
- Causal reasoning (how to achieve beyond correlation)
- Metacognitive awareness (self-monitoring)
- Human-AI interaction dynamics
- Safety and governance in multi-agent settings

### What It Doesn't Do

- **Not a theory.** It's a position paper arguing for the need. It identifies
  the void but doesn't fill it. No formal definitions beyond functional agency,
  no dynamics, no proofs, no predictions.

- **Goal/intent is mentioned but not formalized.** Their functional agency
  requires "action in the direction of some objective" but the objective is
  given, not modeled. They note the difference between "solution autonomy"
  (autonomy in means) and "goal autonomy" (autonomy in ends) but don't develop
  the latter.

- **No feedback dynamics.** No mismatch signal, no gain, no tempo, no
  persistence condition. Their "adaptation" is a condition, not a process.

- **No adversarial treatment.** Cooperative and competitive interaction is
  mentioned but not formalized.

- **Pearl's hierarchy is used but not developed.** They place it in the
  outcome model spectrum but don't build on it the way TF-02 does.

### Relationship to ACT

**They are calling for what ACT provides.** Almost literally:

- "The field would benefit from a common theoretical language" — ACT provides
  the mathematical language.
- They want to understand emergent behavior from interaction dynamics — ACT's
  multi-agent framework (from TFT Appendix F) + shared intent formalization
  provides the tools.
- Their functional agency definition is weaker than ACT's scope but compatible.
  ACT's scope (TF-01 specialized) is more precise; their three conditions map
  to elements of TF-01 + TF-03 + TF-10.
- Their causal hierarchy usage aligns with TF-02.
- Their emergence mechanisms (predictive processing → causal models) describe
  at a qualitative level what TFT formalizes quantitatively (mismatch →
  model update → structural adaptation).

**Positioning**: ACT should cite this paper as articulating the need that ACT
addresses. Their functional agency definition can be mapped to ACT's scope.
Their emergence mechanisms can be grounded in ACT's formal dynamics. Their
open challenges (world models, causal reasoning, metacognition, human-AI
dynamics, safety) are all within ACT's scope.

**A specific opportunity**: Their emphasis on emergence — simple agents producing
complex system behavior through interaction — is something ACT can formalize
through the multi-agent framework. The team persistence condition from
Appendix F already shows how cooperative communication tempo enables persistence
in environments where individuals fail. ACT could extend this to show how
shared intent enables goal-achievement that no individual agent could manage.

---

## 3. FAST Workshop (AAAI 2026) — Selective Assessment

17 papers presented. Most are narrow/applied. The most relevant to ACT:

### High Relevance

**#7: "From Agentic AI to Autonomous Agents"** (Shiwali Mohan)
- Revisits computational agency theory from AI subdisciplines, maps modern
  foundation models to established theory. Directly relevant to ACT's
  positioning — we should read this to understand the state of computational
  agency theory and ensure ACT's framing is well-informed.

**#9: "Leapsight: A Functional Account of Mediation Between Perception and
Action"** (Bagiński & Jha)
- Introduces functional account of agency focusing on "sustained coordination
  between internal representations and environment." Sounds structurally
  similar to what ACT does. Need to read to check overlap.

### Medium Relevance

**#6: "Formalizing Observability in Agentic AI Systems"** (Lotito & Pronesti)
- Observability layers for monitoring agent-agent and agent-environment
  interfaces. Related to TFT's observation channels and the Hafez IDT concept.

**#16: "The Multi-Agent Off-Switch Game"** (Agrawal et al.)
- Demonstrates individually corrigible agents become collectively incorrigible
  through strategic interaction. Related to ACT's persistence/goal tradeoff
  and multi-agent adversarial dynamics.

**#11: "Proactive Interference Reveals Working Memory Limits in LLMs"**
(Wang & Sun)
- Cognitive science paradigm showing LLMs suffer from interference in state
  maintenance. Directly relevant to the 100% turnover problem.

### Low Relevance (to ACT's foundational theory)

The remaining papers are either applied (evaluation metrics, federated learning,
constrained workflows), ethical/governance-focused (AI moral status, safety),
or too narrow (AGI measurement, wireheading, scheming) to be directly relevant
to ACT's foundational theory work.

---

## 4. Synthesis: Where ACT Stands

### The Void Is Confirmed

Neither Hafez nor IBM fills the void. Hafez provides a diagnostic metric
without dynamics or goals. IBM describes the need without providing the theory.
The FAST workshop papers are either applied or narrow. BDI (from our earlier
survey) provides architecture without dynamics.

**No existing work provides:**
1. Mathematical dynamics for adaptive agents (mismatch, gain, tempo) — TFT does
2. Goals/intent as first-class objects with their own mismatch and update — nobody does
3. Shared intent with information-theoretic weight — nobody does
4. The full continuum from survival to purposeful agency — nobody does
5. Adversarial dynamics with formal tempo advantage — TFT does
6. Domain instantiation with measurable quantities — TST begins to

ACT, built on TFT + the goal/intent extension, would be the first to provide
all six. This is the unique contribution.

### Positioning Strategy

1. **Cite Hafez as complementary metric.** Their P could be a diagnostic for
   ACT's dynamics — measuring coupling quality that ACT's tempo/gain/persistence
   machinery predicts. Note the shared goal/intent gap.

2. **Cite IBM as articulating the need.** Their position paper calls for what
   ACT provides. Their functional agency maps to ACT's scope. Their emergence
   mechanisms get formal grounding in ACT's dynamics.

3. **Cite BDI as the architecture ACT gives dynamics to.** BDI named the parts
   (Belief ≈ M_t, Desire ≈ G_t, Intention ≈ committed goals). ACT provides
   the physiology: how beliefs and desires update, interact, and drive action.

4. **Cite active inference as the closest theoretical competitor.** FEP has
   prior preferences (≈ G_t) and unifies perception/action. ACT differs in
   foundation (causal feedback vs. free energy), accessibility (measurable
   quantities vs. free energy), and scope (adversarial, multi-agent, shared
   intent).

5. **Don't overclaim.** ACT is being developed. The goal/intent extension is
   speculative. The math hasn't been worked out. Position honestly: TFT provides
   the adaptive foundation (that's solid); the purposeful agency extension is
   the hypothesis under development.

### Reading Priorities (Updated)

1. ~~Hafez et al.~~ [READ] — complementary, not competing
2. ~~IBM systems theory~~ [READ] — they call for what we're building
3. **Mohan, "From Agentic AI to Autonomous Agents"** — computational agency
   theory state-of-the-art
4. **Bagiński & Jha, "Leapsight"** — check for overlap in functional account
5. **Bungay, *The Art of Action*** — shared intent source material
6. **Friston, active inference with prior preferences** — closest competitor,
   need to understand the precise formal differences
