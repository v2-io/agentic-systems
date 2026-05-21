# Prior-Art Analysis: Agent Spectrum and the Moore-Machine Social Threshold

> [!note]
> **Refreshed 2026-05-21.** The previous version of this file featured *Unity Dimensions* (4 content + 1 structural axis for composite agency) — content that properly belongs to row 08 / `def-unity-dimensions.md`. The actual row-20 topic, per the prompt file `20-agent-spectrum-and-moore-machine-threshold.md` and the load-bearing AAT segment `def-agent-spectrum.md`, is the two-axis individual-agent spectrum and the minimal-complexity social threshold. This file now matches that scope.

**Target Claim:**
Agents partition along **two independent continuous dimensions** — *model richness* (how rich the internal predictive model is, from absent/degenerate through error/integral/derivative through full world-model) and *objective richness* (how rich the purposive structure is, from absent through scalar setpoint through trajectory functional). The cross of degenerate/structured on each axis names four region-archetypes (reactive system, adaptive tracker, blind seeker, actuated agent), but the axes are **continuum regions, not discrete categories** — agents migrate as auto-tuning, exploration, or training changes their effective structure.

A separate, sharp threshold story for **social** agency: a one-state Moore machine occupies the reactive region (fixed output regardless of input) and is provably incapable of contingent social behavior in any game-theoretic setting; the two-state machine is the minimal architecture for branching, one-bit-of-history strategies (Tit-for-Tat-class). The **2-state machine is the minimal AAT agent**.

A complementary bridge: Hafez et al. (2026) measure **bi-predictability** $P = \text{MI}(S, A; S') / C$ as a *scale-invariant architecture* measurement of the agent-environment coupling, distinct from the *performance-bound* tempo $\mathcal{T}$. The two are complementary measurements of the same coupling.

---

## 1. State of the Field & Scientific Precedence

The Undermind search surfaces strong ancestry on each flank separately, but no close precursor for the joint two-axis decomposition.

### Pillar 1: World-Model Necessity (the Model-Richness Axis)
The claim that flexible goal-directed behavior requires internal predictive structure has both classical and very recent precedents.
- **Schmidhuber (1991)** in *A possibility for implementing curiosity and boredom in model-building neural controllers* gives an early model-building-controller argument.
- **Still (2007)** *Information-theoretic approach to interactive learning* and the predictive-state-compression lineage (Still & Crutchfield 2007, Creutzig et al. 2009) supply the IB-shaped past→future compression story for belief-state construction.
- **Richens, Abel, Bellot, and Everitt (2025)** *General agents contain world models* sharpens this to a theorem shape: sufficiently general multi-step goal-directed behavior *forces* an implicit world model.
- **Virgo, Biehl, Baltieri, and Capucci (2025)** *A "good regulator theorem" for embodied agents* extends Conant–Ashby's good regulator argument with embodiment constraints.

Effect on AAT's novelty: the *existence* of model richness as a structural dimension is not novel. AAT must not claim discovery here; the move is to make it one axis of a coordinate system.

### Pillar 2: Objective Richness as a Separate Continuous Axis
This is the less-developed side.
- **Genewein, Leibfried, Grau-Moya, and Braun (2015)** *Bounded Rationality, Abstraction, and Hierarchical Decision-Making* and **Ortega, Braun, Dyer, Kim, and Tishby (2015)** *Information-Theoretic Bounded Rationality* trade utility against information cost — but these are *bounded-rational decision* frameworks, not taxonomies that treat objective structure as a continuous coordinate of *agency*.
- **Gerrit (2014)** *Informational Constraints and Organisation of Behaviour* studies how informational constraints organize behavior — partial ancestry.

The literature talks readily about whether agents have *models*; it talks much less cleanly about how *richly structured* their objectives are as an architectural variable distinct from preferences/utilities. The memo identifies this as the clearer novelty opening of the axis decomposition.

### Pillar 3: Finite-Automata Social Threshold
The minimal-state-count threshold for contingent social behavior is well established in evolutionary game theory.
- **Rubinstein (1986)** *Finite automata play the repeated prisoner's dilemma* pioneered bounded-rationality-as-finite-automata.
- **Abreu & Rubinstein (1988)** and **Kalai & Stanford (1988)** characterized Nash-equilibrium structure under finite-state complexity costs.
- **Linster (1992)** *Evolutionary Stability in the Infinitely Repeated Prisoners' Dilemma Played by Two-State Moore Machines* gives a direct 2-state analysis.
- **Zagorsky, Reiter, Chatterjee, and Nowak (2013)** *Forgiver Triumphs in Alternating Prisoner's Dilemma* makes the threshold visually concrete: ALLC and ALLD are the one-state strategies; forgiving and reciprocal strategies live in the two-state region.
- **Romero (2011)** *Finite Automata in Undiscounted Repeated Games with Private Monitoring* extends this to private-monitoring regimes.
- **Miller (1996)** *The coevolution of automata in the repeated Prisoner's Dilemma* and **Miller (2022)** *Ex Machina: Coevolving Machines and the Origins of the Social Universe* are the direct empirical anchor: a co-evolutionary process moves a population of automata from the one-state asocial morass to the two-state social regime — Miller frames this as the "origin of the social universe."

Effect on AAT's novelty: the 1-state→2-state threshold for contingent social behavior is *not* AAT's discovery. The framework's contribution is **mapping** Miller's threshold to the AAT agent spectrum — naming the 2-state machine as the minimal AAT agent within the broader continuum.

### Pillar 4: Structural Agency Measures Distinct from Reward Success
A maturing lineage measures agency at the architecture level, not at the task-performance level.
- **Bertschinger, Olbrich, Ay, and Jost (2006)** *Information and closure in systems theory* and **Bertschinger et al. (2008)** *Autonomy: An information theoretic perspective* define informational closure for cognitive systems.
- **Kolchinsky and Wolpert (2018)** *Semantic information, autonomous agency and non-equilibrium statistical physics* define semantic information as that which is causally necessary for self-maintenance — explicitly architecture-level, not reward-level.
- **Albantakis (2021)** *Quantifying the Autonomy of Structurally Diverse Automata* explicitly separates task performance from internal structural and causal autonomy measures.
- **Hafez, Reid, and Nazeri (2026)** *The Informational Cost of Agency* and **Hafez, Wei, Felipe, Nazeri, and Reid (2026)** *A Mathematical Theory of Agency and Intelligence* introduce *bipredictability* as a bounded interaction-efficiency measure and sharply distinguish agency from intelligence.

Effect on AAT's novelty: the *possibility* of measuring agency structurally rather than behaviorally is well established. The AAT/Hafez bridge — where bi-predictability measures the *architecture* of the coupling (scale-invariant) and tempo measures the *performance* within it (scale-dependent) — is the AAT-side contribution, validated empirically in `spikes/track-b-nonlinear-sims/variants/variant_hafez_results.md`.

### Adjacent: Empowerment and Plasticity
- **Klyubin, Polani, and Nehaniv (2005)** and **Klyubin & Polani (2008)** *Empowerment* — an information-theoretic measure of an agent's control over its future, agency-relevant but not a model/objective-richness decomposition.
- **Abel et al. (2025)** *Plasticity as the Mirror of Empowerment* — recent companion result.

---

## 2. Key Anchor Papers Identified

1. **Richens, J., Abel, D., Bellot, A., & Everitt, T. (2025).** *General agents contain world models.*
   *Significance:* The current strongest theorem-shape statement that sufficiently general goal-directed behavior forces an implicit world model. Anchors the model-richness axis.
2. **Miller, J. H. (2022).** *Ex Machina: Coevolving Machines and the Origins of the Social Universe.* (Santa Fe Institute Press; DOI 10.37911/9781947864429)
   *Significance:* The direct empirical anchor for the 1-state→2-state social threshold. AAT's `def-agent-spectrum.md` cites this explicitly; #worked-example-cam is planned to formalize the AAT-↔-Moore-machine mapping.
3. **Hafez, W., Wei, C., Felipe, R., Nazeri, A., & Reid, C. (2026).** *A Mathematical Theory of Agency and Intelligence.* (arXiv:2602.22519)
   *Significance:* Provides the bi-predictability measure $P = \text{MI}(S, A; S')/C$ that complements tempo. The AAT/Hafez bridge (architecture vs performance measurement) is documented in `def-agent-spectrum.md` §Discussion and the variant_hafez bridge simulation.
4. **Albantakis, L. (2021).** *Quantifying the Autonomy of Structurally Diverse Automata.* (Entropy 23:1415)
   *Significance:* Demonstrates that structural autonomy measures genuinely separate from task-performance measures across architectural variants — supports the broader stance that architecture-level agency measurement is well-founded.
5. **Linster, B. G. (1992).** *Evolutionary Stability in the Infinitely Repeated Prisoners' Dilemma Played by Two-State Moore Machines.*
   *Significance:* The clearest formal result on two-state Moore machines as the minimal architecture for forgiving / reciprocal strategies.
6. **Rubinstein, A. (1986).** *Finite automata play the repeated prisoner's dilemma.*
   *Significance:* Foundational bounded-rationality-as-finite-automata paper; precedent for treating state-count as a structural complexity variable.

---

## 3. Conclusion on Novelty & Overlap

The individual flanks are well-precedented. World-model necessity has very recent strong support (Ric25, Vir25). The 1-state→2-state social threshold is settled in evolutionary game theory (Rub86, Lin92b, Zag13, Mil22c). Structural agency measures distinct from reward success have a mature lineage (Ber06, Kol18b, Alb21, Haf26b).

**Where AAT actually contributes:**

1. **Joint two-axis decomposition (synthetic novelty — the strongest center).** No close precursor in the search treats model richness *and* objective richness as **independent continuous axes** of a single agency coordinate system. The 2×2 region-archetype framing (reactive / adaptive tracker / blind seeker / actuated agent) is itself an analytic move — making the four named regions of `def-agent-spectrum.md` *regions of a continuum*, not categories. Agents migrate across the space; a PID controller with auto-tuning is moving from blind seeker toward actuated agent; an RL agent in pure exploration is temporarily an adaptive tracker.

2. **Anchoring the spectrum at the empirical Moore-machine threshold (architectural synthesis).** AAT does not discover the 1-state→2-state threshold. The contribution is the **mapping**: the one-state Moore machine occupies the reactive region (degenerate $M_t$); the two-state machine sits at the adaptive-tracker / blind-seeker boundary (the minimal $M_t$ capable of holding one bit of mismatch signal). This grounds AAT's continuum in an empirically replicable computational threshold. (`#worked-example-cam` is planned per `def-agent-spectrum.md`; not yet landed.)

3. **The Hafez bridge — scale-invariant architecture vs scale-dependent performance.** AAT's tempo $\mathcal{T}$ and Hafez's bi-predictability $P$ measure complementary aspects of the same agent-environment coupling: $P$ is *scale-invariant* and characterizes the coupling architecture; $\mathcal{T}$ is *scale-dependent* and characterizes corrective performance within the coupling. Empirically, $P$ increases monotonically with $\mathcal{T}$, but they remain distinct objects. This bridge is documented in `def-agent-spectrum.md` §Discussion and is supported by the variant_hafez bridge simulation. It is a genuinely novel architecture-vs-performance distinction at the AAT/Hafez interface.

**Where AAT does *not* claim novelty:**
- The existence of a model-richness dimension (Ric25, Vir25, Sch91 establish this).
- The 1-state→2-state social threshold itself (Mil22c, Lin92b, Zag13, Rub86 establish this).
- The possibility of measuring agency structurally rather than behaviorally (Kol18b, Alb21, Haf26b establish this).

**Epistemic status of the load-bearing segment.** `def-agent-spectrum.md` is `status: axiomatic` (definitional commitment), `stage: deps-verified`. The two-axis decomposition is *qualitatively motivated* by correspondence with $M_t$ and $O_t$ in the AAT formal apparatus. The continuum-vs-discrete claim is hypothesis-grade. The Moore-machine mapping references a planned `#worked-example-cam` not yet landed. The bi-predictability bridge is supported by simulation but not by a theorem-grade comparison.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **None** at the spectrum level; no theorem here. (Adjacent segments contain math; this row's load-bearing segment is definitional/discussion-grade.)
- *Arch Novelty:* **Medium.** The 2×2 continuum with migration is an architectural framing.
- *Synth Novelty:* **High.** The joint two-axis coordinate system + Moore-machine anchoring + Hafez bridge unifies four otherwise-disjoint literatures (world-model necessity, finite-automata sociality, structural autonomy measures, information-theoretic agency measures) under one taxonomy.
- *Appl Novelty:* **None.** No concrete real-world instantiation in this row.
- *Impact:* **Medium.** The vocabulary could become standard, but the absence of a theorem-shaped result limits the immediate ceiling.
