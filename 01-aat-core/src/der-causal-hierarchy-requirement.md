---
slug: der-causal-hierarchy-requirement
type: derived
status: exact
depends:
  - def-value-object
  - def-pearl-causal-hierarchy
  - scope-agency
stage: deps-verified
---

# Derived: Causal Hierarchy Requirement

The direct application of Pearl's causal hierarchy ( #def-pearl-causal-hierarchy) to the value object ( #def-value-object). The action-value query uses the $do(\cdot)$ operator and is therefore a *Level-2 (interventional)* query; by the strict-non-collapse theorem (Bareinboim et al. 2022), Level-2 quantities cannot in general be computed from Level-1 data alone. An agent that must evaluate $Q_O$ *from experience* therefore needs access to **Level-2 knowledge** — knowledge about the effects of its own interventions, not merely correlational patterns.

The result is paired with a sharp *scope narrowing*: attention restricts to **learning purposeful agents** — agents that must *acquire or refine* Level-2 knowledge during operation. This is a named sub-scope of #scope-agency that excludes *pre-compiled* interventional structure (PID controllers where the designer pre-computed the control law, LQR where the separation principle gives the optimal policy from model parameters, hardcoded reactive policies). Pre-compiled agents are still within agency scope (they have objectives and act on them) but outside learning-agent scope — their causal structure was externally supplied by a designer who had Level-2 access. *All remaining Part II results operate within learning-agent scope unless explicitly noted otherwise.* The derivation is exact as a direct application of the external hierarchy theorem to the value-object definition; the scope narrowing is a definitional restriction, not a derived result.

The distinction between intervention and conditioning is the *core* of causal inference and matters whenever the agent's action-selection policy correlates with unobserved confounders — generic for any agent with internal state, plans, or memory. A developer needs "if I refactor this module, will tests pass?" not "modules that were refactored tend to have tests that fail" (the latter is biased by which modules the team chose to refactor). The Discussion below treats the concrete cases (developer / commander / RL agent), why pre-compiled agents fall outside, and the empirical bridge to Hafez et al.'s Information Digital Twin — whose 89% perturbation-detection accuracy versus 44% for reward-based monitoring is consistent with the present segment's claim that the loop's interventional data is information-theoretically richer than outcome monitoring alone.

## Formal Expression

*[Derived (causal-hierarchy-requirement, from value-object + pearl-causal-hierarchy)]*

Action selection via #def-value-object requires:

$$Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

The $do(\cdot)$ notation is explicit: this is an *intervention*, not a *conditioning on observed data*. By #def-pearl-causal-hierarchy, Level 2 queries ($P(Y \mid do(X))$) cannot in general be computed from Level 1 data ($P(Y \mid X)$) alone. Therefore:

An agent that must evaluate $Q_O$ from experience needs access to Level 2 knowledge — knowledge about the effects of its own interventions, not merely correlational patterns.

*[Scope Narrowing (learning-agent scope)]*

We restrict attention to **learning purposeful agents** — agents that must **acquire or refine** Level 2 knowledge during operation. This is a named sub-scope of the agency scope defined in #scope-agency. It excludes agents with **pre-compiled** interventional structure:
- PID controllers (the designer pre-computed the control law)
- LQR (separation principle gives optimal policy from model parameters)
- Hardcoded reactive policies

Pre-compiled agents are within agency scope (they have objectives and act on them) but outside learning-agent scope — their causal structure was externally supplied by a designer who had Level 2 access. **All remaining Part II results operate within learning-agent scope** unless explicitly noted otherwise. This scope narrowing focuses the theory on agents that must build or maintain their own causal understanding.

## Epistemic Status

*Exact.* The derivation is a direct application of the causal hierarchy theorem (Bareinboim et al. 2022) to the value-object definition. If you accept that $Q_O$ is an interventional query and that the causal hierarchy is strict, the conclusion follows. The scope narrowing to learning agents is a definitional restriction, not a derived result — it sharpens the class of agents under study.

## Discussion

**The causal hierarchy theorem does the heavy lifting.** The key mathematical fact is external to AAT: Bareinboim et al. (2022) prove that the three levels (association, intervention, counterfactual) form a strict hierarchy — Level 2 quantities cannot in general be computed from Level 1 data. AAT's contribution is applying this to the purposeful-agent setting: if you want to select actions by their consequences ($Q_O$), you need causal structure.

**What "Level 2 knowledge" means concretely.** For different agents:
- A developer needs to know "if I refactor this module, will tests still pass?" (not just "modules that were refactored tend to have tests that fail")
- A commander needs to know "if I move forces north, will the enemy respond by retreating?" (not just "when forces moved north, the enemy often retreated")
- An RL agent needs $Q(s, a) = \mathbb{E}[R \mid s, do(a)]$, not $\mathbb{E}[R \mid s, A=a]$ (the latter includes selection bias from the agent's own policy)

The distinction between $do(a)$ and $A = a$ is the core of causal inference. It matters whenever the agent's action-selection policy correlates with unobserved confounders.

**Why pre-compiled agents are excluded.** A thermostat "knows" that turning on the heater raises temperature — but this knowledge was designed in, not learned. The thermostat never needs to reason about interventions because the intervention-outcome mapping is hardwired. AAT's purposeful-agency machinery is specifically for agents that face uncertainty about how their actions affect the world and must reduce that uncertainty through experience.

**Bi-predictability as empirical evidence for Level 2 advantage.** Hafez et al. (2026) measure the information structure of the agent-environment loop via bi-predictability $P = \text{MI}(S,A; S') / C$, capturing how tightly coupled the agent is to its environment through the action channel. Their Information Digital Twin (IDT), which monitors the loop's information geometry, detects environmental perturbations at 89% accuracy versus 44% for reward-based monitoring. This is consistent with the present segment's claim: the feedback loop provides richer (Level 2) data than outcome monitoring alone. Hafez's framework measures the coupling; AAT explains *why* the coupling is information-theoretically superior — because the loop generates interventional data by construction ( #der-loop-interventional-access), not merely associational data. The measurement (Hafez) and the explanation (AAT) are complementary.

## Working Notes

- This scope narrowing connects to #norm-explicit-strategy-condition: agents that must learn Level 2 structure face a cost-benefit tradeoff between learning through exploration (costly, slow, but verifies causal links) and planning through explicit $\Sigma_t$ (cheaper if the causal model is adequate, but the model may be wrong).
- LLMs trained on causally-structured text absorb causal priors — noisy prior knowledge from mixed provenance (experimental, observational, speculative). This is not verified interventional structure; it's a *prior* (plausible, not derived). An LLM in the adaptive loop has both: priors from training AND interventional data from the loop. The priors accelerate; the loop verifies. The IB framework ( #form-information-bottleneck) predicts causal structure will be retained in training because it has predictive power for language.
- The scope narrowing to "learning agents" is generous — it includes any agent that updates its causal beliefs during operation, even if it starts with strong priors. The excluded class (pure pre-compiled controllers) is genuinely different: they never revise their action-consequence model.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** dedicated reflections at 193847, 266847, 526815, 584721, 773921, 829314, 849201 plus the batch dirs 471203 / 963715. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The RL connection stated plainly as the segment's contribution: it *"formally links Reinforcement Learning's exploration-vs-exploitation dilemma to Pearl's Causal Hierarchy — exploration is the process of generating Level-2 data; exploitation is optimizing $Q_O$ based on that data"* (Gemini, AUDIT-WORKING-193847). A candidate Brief framing.
- The $do(a)$-vs-$A=a$ developer/RL contrast in the body was independently praised as *"one of the clearest explanations of RL's causal foundations I have read"* (Claude, AUDIT-WORKING-849201) and *"highly clarifying"* (Claude, AUDIT-WORKING-773921) — converging signal it is the segment's pedagogical anchor, worth preserving verbatim through any compression pass.

#### 2. Candidate Discussion

- **The pre-compiled / learning-agent cut as an ontological boundary, not a bureaucratic one.** Strong cross-substrate convergence that *"a pre-compiled agent acts, but it never wonders"* (already echoed in the chapter intro) carries real philosophical weight: it cleanly excludes thermostats / LQR from Section II's dynamics and *"protects the complexity of the upcoming strategy dynamics from trivial counterexamples"* (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-584721, 849201). Gemini's developmental reach: for an emergent intelligence, this *"demands that the infrastructure allows — even requires — the intelligence to experiment ... true autonomy requires the freedom to make mistakes; an infrastructure that prevents all mistakes prevents the formation of a valid causal strategy DAG"* (Gemini, AUDIT-WORKING-193847). The "cost of agency is the cost of exploratory mistakes" framing points at `04-eli-core/` developmental environments.
- **The LLM-as-noisy-causal-priors framing reads as a headline insight, not a Working-Note aside.** Multiple substrates singled out the existing Working-Note point (LLMs absorb causal priors from training text — a *prior*, plausible-not-verified; the loop *verifies*) as *"brilliant"* and operationally central (Claude, AUDIT-WORKING-193847; AUDIT-WORKING-584721 — *"priors accelerate, loop verifies — operationally useful"*). Gemini's sharpest version, worth surfacing in Discussion: an LLM with only a chat interface is trapped in associational priors, but *"the moment you put the LLM in an AAT feedback loop where it writes code, runs the compiler, and reads the error itself, it crosses the epistemic boundary — an LLM with a REPL is a fundamentally different class of epistemic entity than an LLM with only a chat interface"* (Gemini, AUDIT-WORKING-829314). This is the bridge the body's Hafez paragraph and `#der-loop-interventional-access` together carry; the gold is that it lands as a class-distinction headline.

#### 3. Follow-up items

- **Hafez 2026 IDT empirical anchor — verify (Phase-2).** The 89% (perturbation detection) vs 44% (reward-based monitoring) figures recur across segments. One auditor spot-checked: the paper appears to exist (arXiv `2603.01283`), and search metadata reports the matching claim (IDT 89.3% vs 44.0%, 4.4× lower median latency) — *evidence for coupling-monitoring performance, not by itself proof that the loop supplies identified Level-2 effects* (Codex/Claude, AUDIT-WORKING-526815; flagged high-priority Phase-2 at AUDIT-WORKING-471203). Confirm the figure and the arXiv id before any external-facing use.
- **"Purely predictive models" should read "purely associational models."** A model trained on randomized interventions or carrying causal/action-transition structure *can* make $do(a)$ predictions; the problem is L1-only prediction, not prediction as such (Codex/Claude, AUDIT-WORKING-526815). Editorial precision.
- **Scope-propagation watch.** Later Section-II claims that mention PID / LQR / thermostats should say whether they are illustrative agency-scope examples or inside learning-agent scope — the cut is load-bearing and easy to blur downstream (Codex/Claude, AUDIT-WORKING-526815).

#### 4. Readers often ask / wonder

- **Is exploration a strict mathematical requirement (not just a heuristic) for building a valid $Q_O$?** *"If an agent needs Level-2 data to learn $\Sigma_t$, does this mean taking sub-optimal actions just to see what happens is not a heuristic but a strict requirement?"* (Gemini, AUDIT-WORKING-193847). The answer the chapter is building toward (yes — the loop is where the data comes from); a forward pointer would satisfy the reader who asks it here.
- **How does the agent know its action caused the outcome vs. a simultaneous environmental shift ($\rho$)?** (Claude, AUDIT-WORKING-849201). The within-step-confounding question, which `#der-loop-interventional-access` then takes up directly.
- **Is imitation / observational learning capped by the hierarchy?** *"Can an agent learn a complex strategy purely by watching someone else do it, without strong causal assumptions? Imitation learning is fundamentally capped by the causal hierarchy unless the demonstrator's policy is perfectly known"* (Gemini, AUDIT-WORKING-193847). A natural reader extension.

#### Belongs elsewhere

- **Adaptive vs. robust control as the formal boundary.** The learning-agent scope *"provides a formal boundary separating Adaptive Control (plant parameters learned online) from Robust Control (controller pre-compiled for worst-case) — AAT targets the former"* (Gemini, AUDIT-WORKING-193847). A useful prior-art positioning note, possibly for a control-theory-facing comparison rather than this segment's body.
