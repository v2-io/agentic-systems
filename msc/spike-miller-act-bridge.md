# Spike: Miller's Ex Machina ↔ AAD Structural Adaptation Bridge

**Status**: Active investigation — mapping structural contact between Miller (2022) and AAD's hand-wavy areas
**Date**: 2026-04-06
**Context**: Joseph suspects AAD's structural adaptation treatment is one of its weakest areas. Miller's coevolving automata model (CAM) provides constructive mechanisms for phenomena AAD currently labels but doesn't formalize.

---

## 1. Where AAD is Hand-Wavy (Honest Audit)

### 1.1 Structural Adaptation Necessity (#structural-adaptation-necessity)

**What's solid:** The *diagnostic* — when model class fitness is insufficient, parametric adaptation cannot close the mismatch floor. This is derived (Prop 10.1 from TFT). The symptoms are clear (persistent irreducible mismatch, gain collapse, systematic residuals).

**What's hand-wavy:** The *mechanisms* of structural change. The Discussion section lists four labels:
- Decomposition and recombination ("Boyd's insight" — but no formalism)
- Expansion (adding capacity — but no model of when or how)
- Compression (removing capacity — but same)
- Grafting (incorporating external structure — but same)

These are *categories*, not mechanisms. No formalism connects the diagnostic ("your model class is inadequate") to the remedy ("here's how to find a better one"). The segment acknowledges this: "The severity of structural change needed depends on how far the current model class is from adequacy" — but provides no measurement of this distance or guidance on what structural change to attempt.

**The gap:** Between detecting the need for structural change and actually executing it, AAD has nothing but hand-waves and domain-specific examples.

### 1.2 Structural Change as Parametric Limit (#structural-change-as-parametric-limit)

**What's solid:** The continuity claim — in a probabilistic DAG, adding/removing edges is a boundary event, not a discontinuity. The six operations are well-ordered by frequency.

**What's hand-wavy:** The "full restructure" case is just "replace entire Σ_t" — the entire DAG is destroyed and rebuilt. This is AAD's version of "then a miracle occurs." The segment claims this is the *limit* of continuous operations, but the limit argument is hand-waved: there's no formal bridge between "many small changes accumulating" and "radical restructuring."

**The gap:** How does a system transition from one structural configuration to a radically different one through incremental changes? This is EXACTLY what Miller's extreme transition motif answers.

### 1.3 Strategy Complexity Cost (#strategy-complexity-cost)

**What's solid:** The depth bound d* (derived for Beta-Bernoulli). The triple depth penalty (combining three independent results).

**What's hand-wavy:** Everything else. The IB objective is "formulation/discussion-grade." The DL formulation applies standard MDL but isn't connected to anything empirical. No enumeration of what strategies are actually *available* at given complexity levels.

**The gap:** Miller provides the exact enumeration (Table 12.2) that would give this substance.

### 1.4 Adversarial Destabilization (#adversarial-destabilization)

**What's solid:** The destabilization threshold (exact under coupling model). The result that getting inside the opponent's loop has a Lyapunov characterization.

**What's hand-wavy:** The effects spiral is discussion-grade. No formalism for what happens *after* destabilization — the segment says the spiral "terminates only when B undergoes structural adaptation or ceases to function" but provides no model of either outcome.

**The gap:** Miller shows what actually happens after destabilization — the system enters a transition period, a new equilibrium emerges through the cascading displacement mechanism, and then consolidates. This is a concrete answer to AAD's open question.

### 1.5 Communication Gain (#communication-gain)

**Status:** Hypothesis. The additive denominator is acknowledged as a "structural heuristic, not a strict variance derivation." Trust is a static meta-model parameter.

**What Miller provides:** Trust is not a static parameter — it's an emergent property of coevolutionary dynamics. TFT and Grim Trigger encode different trust postures in their transition functions. Communication emerges from action, is transitory (most important during transitions), and has a computational threshold (need ≥2 states to condition on inputs).

### 1.6 Composition Dynamics (Section III generally)

**What's solid:** Composition closure as a criterion (when is a group a valid composite). The closure defect framework. Team persistence condition.

**What's hand-wavy:** No dynamics of *how composites form, evolve, and dissolve*. The current framework asks "is this a valid composite?" — a snapshot question. No model of transition between composite states. No explanation of how social structure emerges from interacting agents.

---

## 2. What Miller Provides (Concrete Mechanisms)

### 2.1 The Extreme Transition Motif as a Mechanism for Structural Change

Miller's five-phase motif (Table 6.1):

1. **Pre-transition**: Two homogeneous populations in stable equilibrium. Neither can be directly invaded. (= AAD: persistence condition satisfied, both populations within adaptive reserve)

2. **Neutral invasion**: An environmentally neutral mutant ν appears in the dominant population. It behaves identically to incumbents against the current opposition. (= AAD: structural slack — the agent has unused representational capacity, like inaccessible states in an automaton)

3. **Neutral drift**: ν drifts to a nontrivial proportion through stochastic reproduction. Observable behavior unchanged. (= AAD: no AAD analog currently. This is the mechanism AAD lacks — how latent variation accumulates without performance change)

4. **Niche creation + mutant invasion**: ν's structural difference creates a new niche. A mutant μ in the subordinate population exploits this niche. Self-reinforcing feedback: ν's growth enables μ, μ's growth enables ν. (= AAD: this is the effects spiral from #adversarial-destabilization, but *constructive* rather than destructive, and between populations rather than against a target)

5. **Consolidation**: Both populations taken over by new mutants. Simplified forms emerge that capture the new behavior more efficiently. (= AAD: structural adaptation completed. The new "model class" is in place.)

**Key insight for AAD:** The transition between structural configurations proceeds through *neutral variation accumulation* → *niche construction* → *cascading displacement*. This is not deliberate restructuring — it's emergent structural change. And it bridges the gap between "many small changes" and "radical transformation" that `structural-change-as-parametric-limit` claims but doesn't prove.

### 2.2 The Meta-Machine as Composition Algebra

Two interacting Moore machines form a product automaton (meta-machine). Properties:
- State space = S₁ × S₂ (product of constituent state spaces)
- Deterministic transitions (each output determines the other's input)
- Always falls into a cycle (finite states + deterministic transitions → recurrence)
- The meta-machine IS an automaton — same formalism at every level

This provides what AAD's composition closure currently lacks: a **constructive composition operation** where ε* = 0. The interesting AAD question (when does a *compressed* macro-description work?) is then about when a smaller automaton approximates the product meta-machine.

### 2.3 Computational Compression as Strategy Complexity Grounding

Miller's Table 12.2:

| States | Unique minimized | 1 round | 2 rounds | 3 rounds | 4 rounds | ... |
|--------|-----------------|---------|----------|----------|----------|-----|
| 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | 26 | 2 | 8 | 26 | 26 | 26 |
| 3 | 1,054 | 2 | 8 | 116 | 690 | 1,054 |
| 4 | 57,068 | 2 | 8 | 128 | 5,936 | 33,302 |

Key result: effective_complexity = min(machine_complexity, interaction_horizon_complexity). This is a *concrete, enumerable* version of AAD's d* bound.

### 2.4 The ICE Threshold

Social behavior requires ≥2 states AND ≥2 rounds of interaction. This is a **hard** threshold, not a gradual degradation. Possible AAD analog: a minimum complexity threshold below which agents cannot participate in composition dynamics.

---

## 3. Mapping the Formalisms

### 3.1 FSA ↔ AAD Agent Model

| Miller (FSA) | AAD |
|-------------|-----|
| State set S | Model space M |
| Initial state s₀ | Initial model M₀ |
| Output function λ: S → A | Action selection: a_t = π(X_t) |
| Transition function δ: S × A~ → S | Recursive update: M_{t+1} = f(M_t, o_{t+1}) |
| Number of states |S| | Model class expressiveness F(M) |
| Accessible states | Effective model capacity |
| Inaccessible states | Latent/unused representational capacity |
| Minimized machine | Optimal IB compression of M_t |
| Mutation | Structural adaptation |
| Neutral mutation (structural) | Change that doesn't affect minimized machine → operational no-op |
| Neutral mutation (environmental) | Change that doesn't affect behavior in current environment → no performance change but different structural potential |

### 3.2 What the FSA Formalism Captures That AAD Doesn't

1. **Exact enumeration of behavioral possibilities** at each complexity level
2. **Mutation network topology** — which structural changes are adjacent
3. **Environmental neutrality** — behavioral equivalence in context (not just structural equivalence)
4. **Meta-machine construction** — exact composition
5. **Cycle structure** — all interactions eventually enter periodic cycles

### 3.3 What AAD Captures That the FSA Formalism Doesn't

1. **Within-agent adaptation** — FSAs don't learn during their lifetime
2. **Continuous dynamics** — Lyapunov stability, sector conditions
3. **Purposeful agency** — goals, strategies, orient cascade
4. **Information-theoretic foundations** — IB, CIY, mutual information
5. **Graded mismatch** — continuous error signals, not just behavioral equivalence
6. **Causal reasoning** — Pearl hierarchy, do-calculus

---

## 4. Open Questions (what I need to investigate to recommend a path)

### Q1: Does the neutral-drift → niche-creation → cascading-displacement mechanism generalize beyond game-theoretic settings?

Miller's agents only observe the opponent's last action. Real agents observe rich signals. Does the mechanism work when:
- Agents have continuous state spaces (not finite)?
- Agents adapt within their lifetime (not just across generations)?
- The environment is richer than a payoff matrix?

Hypothesis: The mechanism generalizes because it depends on structural properties (neutral variation, niche construction, positive feedback) not on the specific FSA representation. But this needs verification.

### Q2: What is the relationship between FSA transition graphs and AAD's strategy DAG?

The strategy DAG encodes *causal structure* (what causes what). The FSA encodes *sequential contingent plans* (if I see X, do Y). These seem to capture different aspects of strategy.

One possibility: the DAG is a *static shadow* of the FSA's dynamic structure. The DAG says "step A must succeed before step B"; the FSA says "if I'm in state s and see input x, go to state s' and output y." The DAG captures the causal dependencies between goals; the FSA captures the full sequential behavior.

Another possibility: they're orthogonal representations. The DAG is about *why* actions matter (causal structure); the FSA is about *what* actions to take (behavioral policy). You might need both.

### Q3: Can AAD's sector condition be expressed in automata-theoretic terms?

The sector condition requires: correction function bounded, disturbance bounded, contraction dominates perturbation. In FSA terms:
- "Correction" = transition toward a state that produces better output against the current environment
- "Disturbance" = mutations or environmental changes that move the system away from the current optimum
- "Contraction dominates perturbation" = selection pressure toward better-performing automata exceeds mutation rate

This looks like it might connect to the replicator dynamics / Moran process analysis in Miller's Appendix C. The sector condition might be the continuous-time limit of the discrete evolutionary stability condition.

### Q4: Can the extreme transition motif be formalized within AAD's Lyapunov framework?

The motif has clear phases that map to Lyapunov concepts:
- Epoch = V(δ) bounded (within invariant region)
- Neutral drift = V unchanged (neutral mutant has same fitness)
- Niche creation = change in the Jacobian of the coupled system (the landscape shifts)
- Cascading displacement = V̇ > 0 for the old equilibrium (positive feedback drives departure)
- Consolidation = V(δ') bounded at new equilibrium

This seems formalizable but I haven't verified it.

---

## 5. Possible Paths Forward

### Path A: Miller as Empirical Grounding for AAD Section III

Add Miller's results as concrete instances and mechanisms within the existing framework:
- Meta-machine as a worked example of composition closure
- Extreme transition motif as mechanism for structural adaptation in composites
- ICE threshold as concrete scope condition for social behavior
- Table 12.2 as constructive grounding for strategy-complexity-cost

Effort: Medium. Value: Real but incremental. Doesn't address the structural weaknesses.

### Path B: Restructure Section III with Dynamic Half

Split Section III into statics (composition closure — when is a composite valid?) and dynamics (how do composites form, evolve, and dissolve?). The dynamics half draws on Miller:
- Behavioral epochs as persistence intervals
- Transitions via the extreme transition motif
- Communication as emergent and transitory
- Computational thresholds for social behavior

Also restructure the adversarial dynamics segments to fit the dynamics framework, since the current #adversarial-destabilization is really about transition dynamics.

Effort: Significant. Value: Addresses the deepest weakness of Section III.

### Path C: Automata as AAD's Discrete Foundation

Ground AAD's agent model in automata theory. The FSA is the discrete base case; AAD's continuous dynamics are the large-state / long-horizon limit. This would:
- Make composition exact (via product automaton)
- Make complexity first-class (via state count)
- Make structural adaptation concrete (via mutation networks)
- Provide constructive enumeration at each complexity level

The Lyapunov machinery would then be derived as a continuous approximation, not postulated.

Effort: Massive. Risk: High — the limit argument may not work cleanly. Reward: If it works, it would be a much stronger foundation for the entire theory.

### Path D: Hybrid — FSA for Strategy, Continuous for Model

A less radical variant of Path C:
- Keep M_t as continuous (Lyapunov, sector conditions, gain)
- Recast Σ_t as an FSA or FSA-like structure (finite states, transitions, outputs)
- Composition of strategies via product automaton
- Model adaptation is continuous; strategy adaptation is discrete (mutation-like)

This preserves the continuous adaptive machinery for the epistemic side while giving the strategy side the clean algebra of automata. The strategy DAG might be reconceived as the transition graph of the strategy automaton.

Effort: Significant but bounded. Risk: Moderate — needs to show the FSA strategy captures what the DAG captures. Reward: Clean composition algebra for strategies; constructive complexity bounds.

---

## 6. Sub-Spike Results (2026-04-06)

### 6.1 FSA ↔ Strategy-DAG Relationship (see spike-fsa-dag-relationship.md)

**Finding: They are orthogonal representations, not competing ones.**

- The Moore machine is a *reactive policy* (behavioral surface — what you do given inputs)
- The strategy DAG is a *causal plan* (epistemic interior — why you act, what you believe about causal structure)
- Moore machine → DAG: partial embedding via finite-horizon unrolling, but requires external credence information
- DAG → Moore machine: lossy compilation — discards credences, AND/OR, causal semantics
- Neither is strictly more general. The FSA *cannot replace* the DAG because adaptation requires knowing *why*, not just *what*

**Implications for paths:**
- Path C (full automata grounding) is **not recommended** — would destroy what makes AAD's strategy layer useful
- Path D (FSA for strategy, continuous for model) is **less motivated** than expected — the FSA captures the behavioral surface but not the epistemic interior that drives adaptation
- Behavioral composition IS exact via product automaton, but agent-level composition still needs the approximate framework (ε* comes from projecting internal state, not from composing the policy)

### 6.2 Neutral Drift in AAD's Lyapunov Framework (see spike-neutral-drift-lyapunov.md)

**Finding: The sector condition is structurally blind to Miller's Phases 2-3. AAD needs a new composition-level concept: "latent structural diversity."**

| Phase | AAD Analog | Quality of Mapping |
|-------|-----------|-------------------|
| 1. Stable epoch | Persistence condition + adversarial threshold | Clean |
| 2. Neutral invasion | *None* — invisible to sector condition | **Gap** |
| 3. Neutral drift | *None* — no population-level diversity tracking | **Gap** |
| 4. Niche creation | Effects spiral (constructive) + team persistence | Partial — coupling emergence missing |
| 5. Consolidation | Structural change as parametric limit | Clean |

**The critical gap:** AAD's sector condition defines an equivalence class over correction functions — any F satisfying δᵀF ≥ α‖δ‖² is treated identically. Miller's motif depends on variation *within* that equivalence class: agents that are behaviorally indistinguishable under current disturbance but architecturally different. The Lyapunov analysis literally cannot see this.

**The missing concept: Latent structural diversity** — variation in correction architectures across a population that is invisible to persistence analysis under current conditions but becomes consequential under regime change. This is a *composition-level* property (Section III territory), not a single-agent property.

**The endogenous coupling problem:** In #adversarial-destabilization, γ is a parameter. In Miller's motif, γ *emerges* from population composition. Formalizing the transition motif requires γ(composition) as a dynamical variable — coupling coefficients that are functions of the population state, not exogenous inputs.

---

## 7. Revised Assessment

Both sub-spikes converge on the same conclusion: **Miller's contribution to AAD is primarily at the composition level (Section III).** Sections I/II don't need restructuring because:

1. The FSA and DAG are orthogonal (different aspects of strategy — §6.1)
2. The sector condition works fine for individual agents
3. The gap is at the *population/composition level* — tracking latent structural diversity (§6.2)

**Path B (restructure Section III with dynamics) is the clear recommendation**, now enriched with specifics from the sub-spikes:

### Proposed Section III Restructuring

**Existing material (statics):** Keep composition-closure, team-persistence, adversarial-destabilization, communication-gain, unity-dimensions. These describe *when composition is valid* and *how persistent composites behave*.

**New material (dynamics):** Add a dynamics subsection covering:

1. **Latent structural diversity** — the new concept. Variation in agent architectures within a composite that is invisible to current persistence analysis. Formally: the distribution of correction functions F within the behavioral equivalence class defined by the sector condition. Measures diversity across agents that all satisfy α > ρ/R but differ in their response to novel disturbance regimes.

2. **Endogenous coupling** — coupling coefficients γ that emerge from population composition rather than being exogenous parameters. As population composition changes (through drift, replacement, or immigration), the effective γ between sub-agents changes, which can cross the adversarial destabilization threshold even when no individual agent's parameters change.

3. **Composition transition motif** — Miller's five-phase pattern, formalized within AAD:
   - **Epochal stability**: composite persists, sector condition satisfied, all γ below destabilization thresholds
   - **Latent diversification**: agents join or mutate within the behavioral equivalence class. No observable change in composite dynamics. Latent structural diversity increases.
   - **Niche emergence**: diversity crosses a threshold where the effective γ between some agent pair becomes nonzero or changes sign. New coupling pathways appear.
   - **Cascading restructuring**: positive feedback — new coupling enables agents that couldn't previously thrive; their success further changes coupling for others. The effects spiral mechanism from #adversarial-destabilization, potentially running constructively (team-persistence-style) or destructively.
   - **Re-equilibration**: new composite stabilizes with different architecture but persistence condition re-satisfied at updated parameters.

4. **Computational thresholds for social behavior** — Miller's ICE finding as a concrete scope condition: composite dynamics require individual agents with sufficient computation (≥2-state equivalent: ability to condition behavior on interaction history) AND sufficient interaction depth (≥2-round equivalent: enough repeated interaction for conditional strategies to be distinguishable). This would connect to #strategy-complexity-cost's d* bound and give it empirical content.

5. **Communication as transitional phenomenon** — Miller shows communication is most important during transitions and wanes during stable epochs. This reframes #communication-gain: trust calibration matters most when the composite is restructuring, not during routine operation. Complements the existing segment without replacing it.

### What This Buys AAD

- **Fills the structural adaptation gap** with a concrete, well-characterized mechanism (not just "Boyd's insight")
- **Makes Section III dynamic**, not just static
- **Connects adversarial and cooperative dynamics** through the same coupling framework with sign-dependent effects
- **Grounds strategy-complexity-cost** in constructive enumeration (Miller's Table 12.2)
- **Provides a composition-level concept (latent structural diversity)** that the theory currently lacks
- **Does NOT require restructuring Sections I/II** — the single-agent machinery stays as-is

### What This Does NOT Address

- The FSA ↔ DAG orthogonality means we don't get a clean composition algebra for strategies (product automaton doesn't apply because strategies are DAGs, not policies). The composition closure framework with ε* remains the approach.
- Within-agent structural adaptation (how a *single agent* restructures its strategy) is still not formalized beyond the labels in #structural-change-as-parametric-limit. Miller's mechanism operates at the population level, not the individual level. For single-agent structural change, a different mechanism is needed — possibly deliberation-driven (#exploit-explore-deliberate) or prompted by the diagnostic in #structural-adaptation-necessity.
- Miller's specific game-theoretic setting (binary actions, repeated games, evolutionary dynamics) is narrower than AAD's scope. The *patterns* (epochal dynamics, transition motifs, computational thresholds) generalize plausibly but this needs argument, not assumption.
