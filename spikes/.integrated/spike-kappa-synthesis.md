# κ Spike Synthesis: What's Real and What's Fog

**Status**: Self-assessment of the overnight spikes. Updated after the causal graph exercise, which produced the strongest observation.

**Date**: 2026-03-13 (overnight session)

---

## The Six Spikes

1. **spike-kappa-regimes.md** — Directed separation as a regime boundary (laminar vs. turbulent); Kelvin-Helmholtz analogy; Hafez's P as inter-layer coupling metric
2. **spike-kappa-hb-operationalization.md** — κ operationalized as I(G_t ; M_τ⁺ | e_τ) / H(G_t | e_τ); decomposition into κ_selection and κ_processing
3. **spike-attention-governance.md** — Finite attention as missing precondition; multi-frequency self-composition; sentinel CIY; severity-proportional response
4. **spike-attention-causal-graphs.md** — Five versions of the attention-observation-orientation causal graph; structural implications
5. **spike-kappa-topology-insight.md** — **KEY OUTPUT #1**: directed separation as a property of processing topology (architecture class), not a tunable parameter. Three classes: modular (separation holds by construction), fully merged (fails by construction), partially shared (parameterizable)
6. **spike-causal-level-4.md** — **KEY OUTPUT #2**: Possible extension of Pearl's hierarchy. Directed separation applies to Levels 1-3 (evidence processing, goal-blind) and correctly FAILS at Level 4 (structural imagination, goal-directed). κ problem reframes as contamination between reasoning modes, not coupling strength. M_t / W_t distinction (grounded beliefs vs. exploratory hypotheticals). Aspiration as productive δ_sat > 0.
7. **spike-causal-level-4-formal.md** — **KEY OUTPUT #3**: Two formal sketch approaches. Approach 1 (structural intervention operator do_s): extends do-calculus to mechanism changes but doesn't create a strict new level. Approach 2 (model uncertainty layer): identifies model-modifying actions as a genuinely new computational task — when actions change causal structure, model identification and inference are inseparable. This is the strongest formal claim. Recommended framing: don't claim hierarchy extension, DO claim AAD identifies a new class of reasoning tasks that maps to the directed separation boundary.

## What's Strongest

### The topology classification (spike 5) — STRONGEST OVERALL
The observation that directed separation is a property of the processing topology — not a tunable parameter — cuts through the κ-as-scalar framing. Three architecture classes (modular, partially shared, fully merged) determine whether separation holds by construction, fails by construction, or is parameterizable. This changes the research program from "bound the error as f(κ)" to "characterize the architecture class, then apply the right analytical tools."

The implication for Section V is strong: LLM agents are in the fully merged class, so directed separation is structurally inapplicable (not just "a poor approximation"). The coupled analysis is needed FROM THE START. But LLM-based agent SYSTEMS can be designed with modular structure around the merged LLM, creating partial separation at the system level.

**Confidence: Hypothesis level.** The classification feels correct and useful. The formal characterization of "topology class" needs work (real agents don't have clean boundaries).

### The κ_selection / κ_processing decomposition (spike 2)
This is the tightest formal contribution. It cleanly separates two kinds of coupling that AAD currently lumps together under "directed separation":

- **κ_selection**: Goal influences which events arrive. This goes through π → a → e and is ALREADY ACCOUNTED FOR in AAD's processing/selection distinction. This coupling is expected and doesn't violate directed separation.
- **κ_processing**: Goal influences how events are processed. This is the actual violation of directed separation — f_M depends on G_t.

The information-theoretic definition κ_processing = I(G_t ; M_τ⁺ | e_τ) / H(G_t | e_τ) is the precise formal content of directed separation's scope condition, expressed as a continuous quantity rather than a binary condition. This feels like a genuine step from discussion to definition.

**Confidence: Hypothesis level.** The definition is clean. What's unverified is whether it characterizes anything useful (a regime boundary, an approximation error bound, or just a number).

### The H_b connection to Hafez (spike 2, section 4.2 of spike 1)
High H_b between epistemic and purposeful layers = goal-blind processing = directed separation. This is essentially a restatement of directed separation in Hafez's language. It's valid but not deep — it's a translation, not a new result.

Where it becomes potentially deep: if you can MEASURE H_b from the agent's interaction stream (without access to internals), then you have an empirical test for directed separation. Hafez showed this is feasible for RL agents and LLMs. Whether it's feasible for AAD's more abstract formulation is unclear.

**Confidence: Pattern level.** The mapping is correct. The empirical utility is uncertain.

### The regime reframing (spike 1)
The idea that directed separation is a laminar regime, not a binary scope condition, is conceptually appealing and generates the right intuitions (the pilot in the Kelvin-Helmholtz vortex). But I'm honest: the fluid dynamics analogy might be misleading.

Key question: Is the transition between "separation holds" and "separation fails" actually sharp (like laminar → turbulent) or smooth (like increasing drag with increasing Re, with turbulence as an eventual threshold)? I genuinely don't know. If it's smooth, the "regime" framing is suggestive but not deeply informative — you're just saying "the approximation gets worse as coupling increases," which is obvious.

What would make the regime framing non-trivial: a proof that there exists a critical κ_processing below which the sequential cascade converges to a fixed point (stable) and above which it diverges (unstable). This would be a real bifurcation — a regime boundary, not just a smooth degradation. I don't know if this is true.

**Confidence: Guess → Pattern level.** The analogy is generative but might not map to the actual mathematical structure.

## What's Weakest

### The Kelvin-Helmholtz specifics
The Kelvin-Helmholtz image is vivid and the qualitative mapping is suggestive. But fluid dynamics and information processing have very different mathematical structures. KH instability arises from the Navier-Stokes equations (PDEs over continuous fields). AAD's coupling dynamics would be governed by different mathematics (stochastic processes, information geometry, maybe dynamical systems). The vortex structure, the specific instability mechanism, and the transition criteria won't transfer directly.

Keep as intuition pump. Don't lean on it for formal results.

### The multi-frequency self-composition (spike 3)
The idea of primary/sentinel/strategic loops is plausible as an engineering description of how complex agents work. But it's not clear whether this is:
- A genuine theoretical contribution (something derivable from AAD's existing principles)
- An engineering pattern (a good design, but not load-bearing for the theory)
- Already captured by the temporal nesting claim (#der-temporal-nesting)

The "sentinel CIY" concept is interesting but thin. It might collapse into the existing exploration/exploitation tradeoff (sentinel actions are just a specific kind of exploration — exploring the assumption that unmonitored regions are stable).

### The severity-proportional response mapping (spike 3)
Appealing but currently just a table. The actual mapping (what severity threshold triggers what response?) depends on specifics that the theory doesn't provide: how to combine δ magnitude with ∂Σ/∂M with time pressure with commitment cost. This is a concrete research question, not a result.

## What To Present to Joseph

When we resume, I'd suggest focusing on:

1. **The topology classification** (spike 5) — this is the strongest output. Directed separation is an architectural property, not a tunable parameter. Three classes of architectures. LLMs are in the fully merged class. This reframes the entire κ discussion.

2. **The κ_selection / κ_processing decomposition** (spike 2) — this is concrete, formal, and directly actionable. It clarifies what directed separation actually claims and what violates it. The information-theoretic operationalization gives a candidate definition.

3. **The causal graph insights** (spike 4) — especially: (a) the severity signal as δ × ∂Σ/∂M (multiplicative, not additive), (b) the bootstrap problem of estimating sensitivity in unmonitored regions, (c) the dual-loop competition for action space as a causal structure (not just an optimization tradeoff), (d) intra-agent composition as the framework for attention governance.

4. **The regime language** — use it as framing (it's generative and captures the intuition) but note that the topology classification gives it more precise content than the fluid dynamics analogy alone.

5. **The attention governance observation** (spike 3) — present as a structural gap that's been identified, not a solution. The connection to Hafez's IDT and the thalamocortical analogy is suggestive. The connection to Section III composition dynamics is potentially load-bearing.

## What NOT to Present

- Don't claim the Kelvin-Helmholtz analogy is more than an analogy
- Don't present the multi-frequency loop decomposition as if it's derived (it's an engineering pattern)
- Don't present the severity-proportional response mapping as if it's a result (it's a research question)
- Don't claim the Reynolds number formula is more than dimensional analysis

## What Might Be Worth Investigating Next

In rough priority order:

1. **Can κ_processing be computed for a concrete example?** Take the Kalman filter (where κ_processing = 0 exactly) and a simple goal-conditioned variant (where the Kalman gain depends on the objective). Compute κ_processing analytically. See if the approximation error of the separated cascade is bounded by κ_processing.

2. **Is there a bifurcation?** Take the same system and increase the goal-conditioning continuously. Run both the sequential cascade and the coupled update. Plot approximation error vs. κ_processing. Is there a sharp transition or a smooth degradation?

3. **Does H_b from Hafez's framework correspond to κ_processing?** Take an RL agent (Hafez has code for this), add goal-conditioning to the observation processing, and measure H_b. See if it tracks the theoretical κ_processing.

4. **Is finite attention derivable from IB?** The information bottleneck already constrains how much of the observation the model retains. Does this naturally produce attention-like behavior (allocating representation capacity to the most informative regions)? If so, the "missing precondition" might already be present.

---

*This is the honest assessment. The κ_processing definition and the regime question are the core contributions. Everything else is scaffolding that may or may not be load-bearing. Morning Joseph should vet the definition and the open questions.*
