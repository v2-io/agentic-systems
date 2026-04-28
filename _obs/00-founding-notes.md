# ACT: Agentic Cycle Theory — Founding Notes

> *"Ignoranti quem portum petat nullus suus ventus est."* > ("If a man knows not to which port he sails, no wind is favorable.") > — Seneca, *Epistulae Morales*, LXXI

**Date**: March 2026 **Status**: Genesis. These notes capture the origin of ACT as a restructuring and extension of Temporal Feedback Theory (TFT) and Temporal Software Theory (TST), prompted by the identification of a structural gap in TFT: the absence of goal/intent as a first-class object.

---

## 1. What ACT Is

Agentic Cycle Theory is a first-principles mathematical theory of adaptive, purposeful agents operating under uncertainty. It unifies:

- **Adaptive feedback dynamics** — how agents build and maintain models of reality under environmental change (the contribution of TFT)
- **Purposeful agency** — how agents hold, pursue, and revise goals/intent, closing the gap between desired and actual reality (the identified extension)
- **Shared intent** — how agents communicate purpose to enable coordinated action under uncertainty (the Auftragstaktik / directed opportunism insight)

The theory applies to any system that observes, models, aims, and acts under uncertainty — from thermostats to military commanders, from software developers to AI agents, from immune systems to organizations.

## 2. Origin Story

### 2.1 TFT: The Adaptive Foundation

Temporal Feedback Theory (priors/tft/) formalizes the universal feedback loop: Prolepsis -> Aisthesis -> Aporia -> Epistrophe -> Praxis. Core machinery:

- Mismatch signal: delta_t = o_t - hat{o}_t (prediction vs. observation)
- Update gain: eta* = U_M / (U_M + U_o) (uncertainty ratio principle)
- Adaptive tempo: T = sum_k nu^(k) * eta^(k)* (effective adaptation rate)
- Persistence condition: T > rho / ||delta_critical|| (minimum viable adaptation)
- Adversarial dynamics: squared tempo advantage, effects spiral
- Multi-agent: cooperative/adversarial coupling, trust meta-models
- Structural adaptation: when model class fitness F(M) < 1 - epsilon

TFT is rigorous, well-structured, and internally consistent. It provides a complete theory of *adaptive systems* — how agents learn about and track reality.

### 2.2 TST: The Software Domain

Temporal Software Theory (priors/tst/) applies temporal reasoning to software engineering optimization. 12 theorems (T-01 through T-12) covering specification bounds, change investment, coherence-coupling, and continuous operation.

TST-via-TFT (priors/tst/via-tft/) began mapping TST's practical insights onto TFT's formal foundations. Key contributions:
- Six unique properties of software as a TFT domain
- Three-part tempo decomposition: T_obs + T_explore + T_probe
- The action/observation distinction (reading code = exploration action, not observation; compiler output = true aisthesis)
- Causal DAG extensions (explicit dependency graphs, git counterfactuals)
- Six simulation proposals for empirical validation

### 2.3 The Goal/Intent Gap

During a close reading session (March 2026), a structural gap was identified in TFT: its mismatch signal is purely epistemic. TFT formalizes how agents learn about reality but not how they pursue goals. Specifically:

**Evidence from TFT's own structure:**
1. The PID instantiation in TF-05 lists e_t = r_t - y_t (setpoint - measurement) as a mismatch signal, but this is a *goal-reality* mismatch, not the *prediction-observation* mismatch that TF-05 actually formalizes.
2. TF-08's value function is a black box where all goals hide, unexamined.
3. The persistence condition (T > rho) is TFT's sole implicit goal: "stay alive."
4. Boyd's Orient — the most important OODA stage — is where goals get redefined, not just where the model gets updated. TFT reduces Orient to model updating.
5. Directed Opportunism (Auftragstaktik) puts *goal revision* at center stage and treats the model of reality as a support system.

**The key insight (Seneca's port):** TFT is a theory of how to sail — optimal response to wind and current. But it has no port. Without a destination, no wind is favorable, CIY is meaningless, and even adversarial tempo advantage loses its force.

**Three distinct mismatch signals:**
1. delta_epistemic: o_t - hat{o}_t ("my model of reality is wrong") -> learn
2. delta_goal: G_t - Omega_current ("reality isn't where I want it") -> act
3. delta_feasibility: ("what I want may be unrealizable") -> revise the goal

**The continuum from adaptation to agency:**
- Pure survival: G_t = persist. TFT is complete for this case.
- Explicit purpose: G_t = externally specified target. PID, developer with spec.
- Deliberate agency: G_t = self-generated, negotiated, revised intent.

Survival is a powerful source of agency with limitless variety and complexity.
But once purpose exists beyond survival, persistence becomes a (negotiable) prerequisite subsumed by higher purpose. This is what distinguishes an *agent* from a merely *adaptive system*.

### 2.4 Mathematical Similarity of M_t and G_t

A crucial structural observation: M_t (model of reality) and G_t (model of desired future reality) live in the *same state space* and may share mathematical form:

- Both are compressed representations of states in state space S
- Both have uncertainty (U_M, U_G)
- Both have update dynamics (mismatch -> gain -> correction)
- Both have compression objectives (IB for M_t; an analogous principle for G_t)
- delta_goal = G_t - M_t is naturally defined in the same space

This suggests the extension may be a second instance of similar machinery with different source terms and compression objectives, not fundamentally new mathematics. The LQG separation principle is the formal statement that M_t and G_t dynamics can be designed independently in simple cases.

## 3. Proposed Architecture

    ACT: Agentic Cycle Theory │ ├── Adaptive Systems Foundation (absorbs TFT) │   Agents coupled to uncertain environments. │   Mismatch, gain, tempo, persistence. │   The survival space. The prerequisite. │   Scope: any system that observes, models, and acts under uncertainty. │   Implicit goal: persist (T > rho). │   [Note: even survival needs Σ_t in non-trivial environments.] │ ├── Purposeful Agency (ACT's novel contribution) │   Adaptive systems that also AIM. │   O_t (objective) and Σ_t (strategy DAG) alongside M_t. │   δ_objective and δ_feasibility as additional mismatch signals. │   Goal revision (directed opportunism). │   Shared intent with mathematical weight (IB-compressed purpose). │   Orient in its full Boydian sense (M_t × O_t/Σ_t interaction). │   The persistence-purpose tradeoff. │   Scope: adaptive systems with explicit or implicit purpose │   beyond mere persistence. │ └── Domain Instantiations (branches)
        ├── Software Development (TST, refined) ├── Military Strategy (Boyd, Clausewitz, Auftragstaktik) ├── Organizational Adaptation (Art of Action, Bungay) ├── AI Agent Design (the 100% turnover problem, CLAUDE.md as intent) └── ...

## 4. What Distinguishes ACT from Existing Work

### 4.1 vs. BDI (Belief-Desire-Intention)

BDI named the parts 30 years ago: Beliefs (~ M_t), Desires (~ G_t), Intentions (committed goals). But BDI explicitly "lacks any specific mechanisms to learn from past behavior and adapt." It's the anatomy without the physiology. ACT provides the dynamics: mismatch signals, gain calibration, tempo, persistence conditions, adversarial coupling, structural adaptation — all applied to both the belief (M_t) and desire (G_t) tracks.

### 4.2 vs. Active Inference / Free Energy Principle

Active inference includes "prior preferences" (~ G_t) and unifies perception and action under free energy minimization. ACT differs in:
- **Foundation**: Causal feedback dynamics rather than variational free energy
- **Accessibility**: TFT's machinery (gain, tempo, persistence) maps directly to measurable quantities; free energy is often criticized as unfalsifiable
- **Scope**: ACT's adversarial dynamics, shared intent, and multi-agent coupling go beyond active inference's primarily single-agent treatment
- **The causal hierarchy**: ACT inherits TFT's explicit use of Pearl's three levels; active inference operates primarily at Level 1

### 4.3 vs. Hafez et al. "A Mathematical Theory of Agency and Intelligence" (2026)

Recent and information-theoretic. Introduces "bipredictability" — how much information is shared between observations/actions/outcomes. Narrow: doesn't address goals, intent, feedback dynamics, adversarial coupling, persistence, shared intent, or domain instantiation. Complementary rather than competing.

### 4.4 vs. "Agentic AI Needs a Systems Theory" (IBM, 2025)

A call for what ACT aims to provide. Argues the void exists. ACT is the answer, not just for AI but for agents of all kinds.

### 4.5 vs. Optimal Control (LQG, MPC, etc.)

Classical optimal control has the M_t/G_t separation (Kalman + LQR), but:
- Assumes known dynamics (TFT's scope IS unknown/uncertain dynamics)
- No structural adaptation (model class is fixed)
- No adversarial coupling
- No multi-agent intent sharing
- Linear/quadratic assumptions in the standard case

ACT inherits TFT's generality (nonlinear, uncertain, adversarial, multi-agent) and adds the goal/intent layer that control theory handles only in the well-specified case.

### 4.6 The Unique Contribution

ACT would be the first theory that:
1. Provides mathematical dynamics (not just architecture) for adaptive agents
2. Treats goals/intent as first-class objects with their own mismatch and update
3. Formalizes shared intent (Auftragstaktik) with information-theoretic weight
4. Handles the full continuum from pure survival to deliberate purposeful agency
5. Connects to measurable quantities in specific domains (software, military, etc.)
6. Incorporates adversarial dynamics, multi-agent coupling, and structural adaptation

## 5. Key Open Questions

1. **How far does the M_t/G_t mathematical parallel extend?** Can TFT's existing formalism (mismatch, gain, tempo, persistence) be applied to G_t with minimal modification, or do the different sources and compression objectives require genuinely new machinery?

2. **What triggers goal revision?** Analogous to Prop 10.1 (structural adaptation triggered by model class inadequacy), what triggers G_t revision? Persistent delta_goal despite adequate model and competent action? Discovered opportunity?

3. **How do goals interact with persistence?** When does goal-pursuit justify risking the persistence condition?

4. **Is there a "goal tempo"?** An analog of T that measures the rate of delta_goal closure?

5. **How should shared intent be compressed?** The IB framework for M_t (compress to predict) has an analog for G_t (compress to prescribe). The Auftragstaktik sweet spot is the optimal compression level. Can this be formalized?

6. **What is the separation principle for ACT?** When can M_t dynamics and G_t dynamics be designed independently, and when are they inseparably coupled?

7. **How does the 100% turnover problem interact with goals?** An AI agent loses M_t at session boundary but may retain G_t (via CLAUDE.md, task description). The goal survives context death even when the model doesn't.

## 6. Immediate Next Steps (as of founding — most now done)

1. ~~Read the prior art in detail~~ — Done (see 01, 02)
2. ~~Develop the G_t formalism~~ — Done (see 03, track-a/). Now O_t/Σ_t.
3. ~~Test against domain instantiations~~ — Partially done (simulations)
4. ~~Decide on document structure~~ — ACT supersedes TFT; structure to emerge from content (see PLANS.md Phase 3)
5. ~~Relationship to TFT~~ — Decided: ACT absorbs TFT.
