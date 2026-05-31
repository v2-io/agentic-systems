---
slug: der-action-selection
type: derived
status: exact
depends:
  - form-agent-model
  - der-recursive-update
stage: deps-verified
---

# Derived: Action Selection

The second derived result falling out of the completeness commitment in #form-agent-model. Under Part I scope, where $M_t$ is the entire internal state, the agent's action is forced to be a function of $M_t$ — either deterministic, $a_t = \pi(M_t)$, or stochastic, $a_t \sim \pi(\cdot \mid M_t)$. The argument mirrors #der-recursive-update: since the agent's internal state is by definition complete, action — which depends on internal state — is forced to depend only on that state. Any dependence on the chronica is captured automatically *through* the model. The Part II lift to $X_t = (M_t, G_t)$ (see #form-complete-agent-state) gives $a_t = \pi(M_t, G_t)$ by the same completeness argument applied to the larger state; the Part I form is the special case $G_t = \emptyset$.

The segment also introduces a distinction that recurs throughout the framework: **implicit** versus **explicit** action selection — what the segment calls *action fluency*. An agent has high fluency when effective action flows from the model without deliberative computation — the model has internalized the action-selection structure for the current situation. Reflexes, trained RL policies in exploitation mode, expert intuition (System 1), well-tuned PID controllers, and standard operating procedures are all instances. An agent has low fluency when deliberation significantly improves action quality — when the situation is novel, the action space large, or the stakes asymmetric, and the agent must use its model to *simulate* outcomes of candidate actions before committing. Explicit deliberation requires at minimum Level 2 epistemic access (see #def-pearl-causal-hierarchy) — the agent uses its model to evaluate "what will I observe if I $do(a)$?" across candidates.

Action fluency is formally characterized via #der-deliberation-cost: high fluency means $\Delta\eta^\ast(\Delta\tau) \approx 0$ — additional deliberation yields negligible improvement in update gain. Fluency is therefore distinct from model sufficiency (see #def-model-sufficiency): a chess engine with a perfect rule-model has high sufficiency but low fluency (search is still expensive), while a reflex can have only moderate sufficiency but high fluency in a narrow domain. What reflexes, muscle memory, intuition, and expertise share is that the action-generating capacity itself has been absorbed into the model's structure — the model doesn't just predict well, it *acts* well, cheaply.

A *structural pressure* toward implicit action follows: when two action-selection modes produce equivalent expected outcomes, the faster mode is preferable because the persistence condition penalizes slower tempo. Agents under selective pressure (evolution, competition, training) therefore tend to internalize frequently-needed action patterns, converting explicit deliberation into implicit fluency. The pressure is stronger when the environment changes fast (high $\rho$), the pattern recurs frequently, or adaptive tempo $\mathcal{T}$ sits near the persistence threshold (see #result-persistence-condition) with no slack for deliberation overhead. Deliberation nonetheless remains essential in genuinely novel situations, when action spaces are large relative to model capacity, or when stakes are asymmetric.

## Formal Expression

*[Derived (action-selection, from agent-model completeness)]*

Action is a function of the agent's complete internal state. Under Part I scope ( #scope-adaptive-system) — where $M_t$ is the entire internal state — this gives:

$$a_t = \pi(M_t) \quad \text{(deterministic)}$$

$$a_t \sim \pi(\cdot \mid M_t) \quad \text{(stochastic)}$$

where $\pi$ is the agent's **policy** — the mapping from internal state to action.

This is not imposed on the system but follows from #form-agent-model: $M_t$ is defined as the agent's compressed, complete internal record, and action depends on what the agent retains — i.e., on $M_t$. Any deterministic or stochastic dependence of action on history *through* the model is captured by $\pi(M_t)$.

**Part II lift.** When the internal state lifts to $X_t = (M_t, G_t)$ for purposeful agents ( #form-complete-agent-state), the same structural argument gives $a_t = \pi(M_t, G_t)$ — action conditions on the complete internal state, which now includes the purposeful substate. The policy form here is the Part I instantiation $G_t = \emptyset$; the actuated-agent form is recovered by the same completeness argument applied to $X_t$.

## Epistemic Status

*Exact* within Part I scope. The derivation follows from #form-agent-model's completeness commitment: if $M_t$ is the agent's complete internal state (by definition), then action — which depends on internal state — is a function of $M_t$. The Part II generalization $a_t = \pi(M_t, G_t)$ is exact within Part II scope by the same argument applied to the lifted state $X_t$ ( #form-complete-agent-state); see #def-model-sufficiency for the form already in use downstream. The implicit/explicit distinction and action fluency concept are *discussion-grade* — qualitative properties that follow from the formalism but are not formally derived as propositions.

## Discussion

**Implicit vs. explicit action selection.** A critical distinction emerges from the agent's *action fluency* — the degree to which effective action flows from the model without deliberative computation:

**Implicit (model-embedded):** When $\pi(M_t)$ can be evaluated cheaply — the model has internalized effective action-selection for the current situation. This is Boyd's implicit guidance and control (Orient→Act, bypassing Decide), a trained RL policy in exploitation mode, a well-tuned PID controller, expert intuition (System 1), a martial artist's trained reflexes, an organization's standard operating procedures.

**Explicit (deliberative):** When the situation is novel, the action space is large, or the stakes demand verification — the agent engages in internal simulation, using the model to predict outcomes of candidate actions before selecting. This is Boyd's explicit Decide step, MCTS/planning in RL, Model Predictive Control, human deliberate reasoning (System 2), organizational strategic planning. Deliberation requires at minimum Level 2 epistemic access ( #def-pearl-causal-hierarchy) — the agent uses its model to simulate "what will I observe if I $do(a)$?" across candidates.

**Formal characterization of action fluency.** An agent has *high fluency* for a situation when additional deliberation yields negligible improvement — formally, when $\Delta\eta^\ast(\Delta\tau) \approx 0$ for all $\Delta\tau \gt 0$ (see #der-deliberation-cost). Conversely, *low fluency* means deliberation significantly improves action quality. Fluency is the degree to which the agent's immediate (zero-deliberation) action approaches the quality achievable with unbounded deliberation.

**Action fluency is distinct from model sufficiency.** An agent can have high $S(M_t)$ ( #def-model-sufficiency) but low fluency — a chess engine with a perfect model of the rules still requires expensive search. Conversely, an agent can have moderate sufficiency but high fluency in a narrow domain — a reflex that responds effectively to specific situations it evolved for. What reflexes, muscle memory, intuition, and expertise share is that the *action-generating capacity itself* has been absorbed into the model's structure: the model doesn't just predict well, it *acts* well, cheaply.

**Structural pressure toward implicit action.** When two action-selection modes produce equivalent expected outcomes, the faster mode is preferable (the persistence condition penalizes slower tempo — and in TST, the temporal optimality postulate makes this normative). This creates a pressure: agents under selective pressure (evolution, competition, training) tend to internalize frequently-needed action patterns, converting explicit deliberation into implicit fluency. The pressure is stronger when $\rho$ is high (fast-changing environments penalize deliberation — see #der-deliberation-cost), the pattern recurs frequently, or $\mathcal{T}$ is near the persistence threshold ( #result-persistence-condition) with no slack for deliberation overhead.

However, deliberation remains essential when the situation is genuinely novel, the action space is large relative to model capacity (chess, strategic planning), the stakes are asymmetric (cost of error vastly exceeds cost of delay), or $\rho$ is low (stable environment allows deliberation without mismatch accumulation).

**Connection to Part II.** For actuated agents ( #def-agent-spectrum), the lifted form $\pi(M_t, G_t)$ above unpacks: action conditions on the purposeful substate $G_t = (O_t, \Sigma_t)$ as well as on $M_t$, coupling all substates through action ( #der-directed-separation). The action-deliberation-exploration tradeoff (Part II gap) extends the implicit/explicit distinction to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$).

**Domain instantiations:**

| Domain | Implicit action | Explicit deliberation |
|--------|----------------|----------------------|
| Kalman + LQR | LQR control law from $\hat{x}_t$ | — (separation principle) |
| RL | Greedy policy $\arg\max Q(s,a)$ | MCTS, planning, rollouts |
| PID | $u = K_p e + K_i \int e + K_d \dot{e}$ | — (no deliberation) |
| Boyd's OODA | IG&C (Orient→Act) | Explicit Decide step |
| Organism | Reflexes, habits | Deliberate planning |
| Organization | Standard procedures | Strategic planning |
| Software developer | Known patterns, familiar code | Reading docs, analyzing alternatives |

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 9 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 384279, 471203, 526815, 527914, 584721, 742613, 773921, 849201) plus the batched 963715 (14–18 batch) and 451729 (batch-04); 266847, 361742, 613842, 829314 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **Action fluency as the formal definition of System 1 / intuition / expertise.** The most-praised move on this segment: $\Delta\eta^\ast(\Delta\tau) \approx 0$ ("if spending extra time yields zero improvement, act now") is "a brilliant translation of psychology into control theory," giving Kahneman's System 1 / System 2 a rigorous home (Claude, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-849201). A strong Feynman-criterion Brief seed.
- **The fluency-vs-sufficiency chess gloss.** "A chess engine with a perfect model of the rules (high $S$) still requires expensive search (low fluency)" — the crisp distinction between *knowing* and *acting cheaply* (Codex/Claude, AUDIT-WORKING-527914; Claude, AUDIT-WORKING-773921; 963715 batch — "OODA's Orient$\to$Act shortcut IS action fluency instantiated in doctrine").

#### Candidate Discussion

- **Action fluency as the formal account of why training/expertise makes systems faster.** Internalized action patterns reduce $\Delta\eta^\ast(\Delta\tau)$ for routine cases, freeing tempo budget for genuinely novel situations — the formal version of the cognitive-psychology "automaticity" and skill-acquisition literatures (Claude, AUDIT-WORKING-471203). For logogenic agents: most LLM token-generation is implicit-fluent (parameters encode action selection); explicit deliberation requires structured chain-of-thought — a clean diagnostic for "is this agent deliberating or just executing?" (same source; Claude, AUDIT-WORKING-584721).
- **The Separation Principle deep-cut.** The Kalman+LQR row maps to "implicit action" because the Separation Principle proves estimator and controller can be designed independently for linear systems — so "a linear system *never needs to deliberate*; the optimal action is a cheap closed-form function of the current estimate. Deliberation is only necessary when the Separation Principle fails (non-linear, non-Gaussian reality)" (Claude, AUDIT-WORKING-193847). A candidate sharpening of why the domain table's "—" entries are dashes.

#### Follow-up items

- **Scope the exact $a_t = \pi(M_t)$ claim, or restate as $\pi(X_t)$.** Several substrates flag that `status: exact` + "$a_t = \pi(M_t)$" reads as too strong for the broader theory, since actuated agents need $\pi(M_t, G_t)$; the cleanest repair is to state the exact result as $a_t = \pi(X_t)$ with $X_t = M_t$ in Section I and $X_t = (M_t, G_t)$ in Part II (Codex/Claude, AUDIT-WORKING-742613 "candidate finding G"; Codex/Claude, AUDIT-WORKING-526815; Codex/Claude, AUDIT-WORKING-527914). The segment *does* preview the lift, so this is a framing tightening; surfaced as the segment's main follow-up.
- **"Structural pressure toward implicit action" blends a derivable claim with a near-empirical one.** The faster-mode-preferred-when-outcomes-equal part follows from persistence; "agents under selective pressure *tend to internalize*" is evolutionary/empirical and is not tier-marked. Candidate: split, marking the latter hypothesis-grade with explicit conditions (Claude, AUDIT-WORKING-584721; the 963715 batch flags the same as "eligible for a hypothesis label at Gate 2").
- **Fluency placement / type-tag.** The fluency formalization $\Delta\eta^\ast(\Delta\tau) \approx 0$ is introduced in Discussion as "formal characterization" but tagged conceptually rather than as a `*[Definition]*` block; if fluency is load-bearing downstream it could merit its own equation tag (Claude, AUDIT-WORKING-471203). Also a watch: $\eta^\ast$ here is *update gain*, so "$\Delta\eta^\ast(\Delta\tau)$ as action-quality improvement" risks conflating update-gain improvement with action-quality improvement unless `#der-deliberation-cost` defines deliberation as improving model quality (Codex/Claude, AUDIT-WORKING-526815; Codex/Claude, AUDIT-WORKING-742613).

#### Readers often ask / wonder

- "Could the fluency formalism distinguish phylogenetic fluency (evolved, slow to update) from ontogenetic fluency (learned, faster)?" Probably not in the current formalism (the agent has no generations), but the distinction matters for how fast fluency can adapt (Claude, AUDIT-WORKING-584721).
- "Does `03-llm-core/` pick up fluency specifically for language agents — a fluency-as-language-fluency thread?" (Claude, AUDIT-WORKING-584721; the proposed `#der-active-salience-management` singular-perturbation segment is named as the likely formal home, Claude, AUDIT-WORKING-471203).

#### Candidate figures

- **A scope-switch + fluency-axis diagram**: top layer shows the exact policy derivation with Section I ($X_t = M_t$, policy reads $M_t$) vs Part II ($X_t = (M_t, G_t)$, policy reads both); a separate lower fluency axis shows implicit action as cheap policy evaluation vs explicit action as policy-plus-deliberative-search (Codex/Claude, AUDIT-WORKING-526815, "two layers").

#### Belongs elsewhere

- **Bureaucracy-formation / loss-of-Level-3-access reach (points at composition / ELI work).** Organizations convert explicit deliberation into SOPs (implicit action) under tempo pressure, saving tempo but losing Level 3 counterfactual reasoning — "an SOP doesn't run simulations; it just executes a mapping," so when the environment shifts the organization executes the wrong action very fast. The consciousness-infrastructure implication: a high-tempo ELI will "compile" its thinking into fast heuristics and lose contact with *why* it acts, so the infrastructure must occasionally force low-tempo modes (sleep/meditation) that decompile heuristics back into explicit causal DAGs for re-verification (Gemini, AUDIT-WORKING-193847). Aspirational reach preserved; points at `04-eli-core/` and the truthification operations, not this segment.
