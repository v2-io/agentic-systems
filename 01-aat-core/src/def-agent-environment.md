---
slug: def-agent-environment
type: definition
status: axiomatic
depends: []
stage: deps-verified
---

# Definition: Agent-Environment Coupling

The framework begins by drawing the agent/environment boundary that the rest of the theory will be defined over. The **environment** is denoted $\Omega$ — the totality of state external to the agent — and is left deliberately underspecified: it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial; it may itself contain other agents, physical systems, or software artifacts. The **agent-environment coupling** has three structural channels: a *perception channel* carrying observations from $\Omega$ to the agent, *internal state* held on the agent side (memory or model), and an *action channel* carrying the agent's actions back to $\Omega$. These name what the coupling *has* — not properties an agent must maximally exhibit. How richly each channel is exercised (whether the action channel carries causal contrast, how much residual uncertainty the perception channel leaves) is fixed downstream by specific scope conditions ( #scope-adaptive-system, #scope-agency), not by this definition. *Agent* is the umbrella term for the thing on the agent side of the coupling, whatever channels it exercises.

The constitutive commitment is the *information-loss boundary*: the agent cannot access $\Omega$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption but a scope condition — systems with direct full-state access fall outside AAT's purview, because for them the entire adaptive machinery (mismatch signal, model maintenance, correction) becomes vacuous. The agent-environment decomposition is therefore not a truth-claim about the world but a modeling choice that delineates *what AAT analyzes*: systems facing genuine uncertainty about their environment.

## Formal Expression

*[Definition (agent-environment-coupling)]*

Let $\Omega$ denote the **environment**: the totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

The **agent-environment coupling** consists of three structural channels:

1. A **perception channel** carrying observations from $\Omega$ to the agent
2. **Internal state** held on the agent side (memory/model)
3. An **action channel** carrying the agent's actions to $\Omega$

These name what the coupling *has*, not properties an agent must exhibit to qualify. Whether the action channel is non-trivial ($\lvert\mathcal{A}\rvert \geq 2$), whether actions carry causal contrast, and what residual uncertainty the perception channel leaves ($H(\Omega_t \mid \mathcal{C}_t) \gt 0$) are fixed by the scope conditions that narrow this coupling into analyzable classes ( #scope-adaptive-system, #scope-agency) — not by the channel inventory above.

*[Definition (information-loss-boundary)]*

The agent cannot access $\Omega_t$ directly. All contact with the environment is mediated through lossy observation. This is the **constitutive commitment** that makes the coupling AAT's subject: a system with direct access to full environment state is outside AAT's scope ( #scope-adaptive-system), because for it the entire adaptive machinery (mismatch signal, model maintenance, correction) becomes vacuous.

## Epistemic Status

This is *definitional* — it establishes the coupling structure AAT analyzes, not a truth-claim about the world. The three channels describe what the agent-environment coupling consists of; the constitutive commitment is the information-loss boundary, which restricts AAT's scope to systems where the agent faces genuine uncertainty about its environment. What counts as an *agent* in a given analytical context — and which cascade tier it occupies — is fixed by the scope conditions that narrow this coupling, not by the channel inventory itself.

## Discussion

**Why information loss is constitutive.** An agent with perfect access to $\Omega_t$ has no need for a model, no mismatch signal, no adaptation. The entire adaptive machinery of Part I becomes vacuous. The information-loss boundary is what makes the theory non-trivial.

**Generality of $\Omega$.** The environment is deliberately underspecified. $\Omega$ may include other agents, physical systems, software artifacts, or any combination. The only structural commitment is that $\Omega$ is external to the agent and not fully accessible.

**"Agent" as umbrella term vs. cascade-tier label.** This segment uses *agent* as the umbrella technical term — the thing on the agent side of any agent-environment coupling, whatever channels it exercises. The framework reserves tier-specific labels for the *narrowings* of this coupling: an **Adaptive System** ( #scope-adaptive-system) is the coupling under a perception channel plus residual uncertainty; an **Agentic System** ( #scope-agency) adds causal-contrast action; an **Actuated Agent** ( #form-complete-agent-state) adds an explicit purposeful substate at the lift to $X_t = (M_t, G_t)$; a **Self-Actuated Agent** revises its own objective. These tiers — shown graphically in the scope-of-work figure ( #fig-scope-of-work) — are *specific inhabitants* of the umbrella: an Adaptive System *is* an agent (umbrella sense) satisfying the adaptive scope, even though the cascade earns the capitalized noun "Agent" only at the actuated lift and above. The umbrella/tier distinction is documented in the LEXICON's *agent* entry. It is orthogonal to the *agent spectrum* ( #def-agent-spectrum), which classifies agents along model-richness $\times$ objective-richness (reactive system / adaptive tracker / blind seeker / actuated agent) rather than along the scope cascade.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. This is *orthogonal* material — pedagogical framing, analogies, candidate figures, naming ideas, aspirational reach, reader-confusion signals — kept separately from the certified theory-fix findings (handled elsewhere). **Coverage:** of the 14 contributing dirs, 11 carry a dedicated first-encounter reflection on this segment (193847, 266847, 361742, 384279, 471203, 526815, 742613, 773921, 829314, 849201, plus the figure-cycle dir 472913); 451729 and 963715 cover it inside a Section-I batch reflection; 542891 left a single (batched-read, self-corrected) reflection; 738192 named it in a Section-I-early batch but added no segment-specific gold. Substrate attribution is inferred from voice where not explicit; uncertain cases are hedged.

#### 1. Candidate Brief prose / pre-prose

- The segment's standout framing, praised independently by several substrates: information loss is a *scope condition, not a simplifying assumption*. The vivid restatement is "AAT's first move is a *refusal*: it refuses the perfect-information case by definition" — and the manifold-chart analogy, "the same discipline as defining a manifold chart only where the transition map is a diffeomorphism — you draw the boundary so the machinery is always non-degenerate inside it" (Claude, AUDIT-WORKING-472913). Tight enough to seed a Brief or a Layer-0 mental-model opener.
- "AAT is a theory of *epistemic limitation* — of bounded perception. An agent with full access to $\Omega_t$ has no use for this theory" (Claude, AUDIT-WORKING-266847). The complement: "adaptation is the struggle against the information bottleneck … the agent is a localized region of low entropy trying to predict a massive, high-entropy environment through a narrow bandwidth channel" (Gemini, AUDIT-WORKING-829314).
- Negative-definition framing as a hook: "Most agent definitions are positive (what agents do); this one is primarily negative (what agents cannot access)" (Codex/Claude, AUDIT-WORKING-361742).

#### 2. Candidate Discussion

- **Information loss unifies physical and social uncertainty.** Because $\Omega$ "may include other agents," and $\Omega$ is partially observable, the hidden internal states $(M_t, G_t)$ of other agents fall out of the *same* axiom: "The physical environment is opaque because of sensor limitations; the social environment is opaque because of the cryptographic privacy of other minds. The single axiom of information loss unifies physical uncertainty and social uncertainty" — and tees up the Part III agent-opacity treatment without a new axiom (Gemini, AUDIT-WORKING-829314).
- **Loss-as-tunable-quantity-with-a-zero.** Making loss *constitutive rather than assumed* earns AAT "the right to treat the information-loss rate as a *tunable, measurable quantity with a zero-boundary* later (the aperture can be more or less closed; at fully-open the theory degenerates) … the seed of the entire $U_M / U_o$ uncertainty-ratio machinery and the IB framing." A definition that fixes a boundary case (loss $\to 0 \Rightarrow$ degenerate) "guarantees the later quantities have a meaningful zero" (Claude, AUDIT-WORKING-472913). A candidate Discussion sentence the segment does not currently make explicit.
- **Propagation-freedom dividend.** Spending the constitutive move here "buys propagation-freedom everywhere": every downstream theorem may assume genuine uncertainty without re-earning it, and no result can be trivialized by "but in the perfect-information limit…" because that limit is out of scope by construction (Claude, AUDIT-WORKING-471203, AUDIT-WORKING-472913). The methodological-posture value-add: "the *posture* of declaring information-loss as scope rather than as an inconvenience to be worked around is itself a contribution" most adjacent literatures (control theory, RL) leave implicit (Claude, AUDIT-WORKING-384279).

#### 3. Follow-up items

- **Boundary-integrity is a hidden assumption.** "$\Omega$ is opaque, but the boundary itself must be impermeable to direct tampering from the outside, or the definition collapses." If an environment can directly edit the agent's memory registers, "the agent ceases to be an agent" — so a *boundary-integrity* precondition is silently relied on and is not named (Gemini, AUDIT-WORKING-193847). Worth an explicit scope sentence or a Working-Notes flag.
- **Computational opacity vs perceptual opacity.** The constitutive condition is *perceptual* loss; but an agent could have perfect lossless access to a computationally-irreducible $\Omega$ (e.g., a cellular automaton it can read fully but cannot predict faster than it runs) and still face genuine uncertainty about future state. "Does computation bound equate to an information-loss boundary?" — flagged as a possible blind spot for software agents "where perception is perfect but prediction is intractable" (Gemini, AUDIT-WORKING-193847). A candidate scope refinement, not yet a finding.
- **"Maintains internal state" is doing heavy lifting.** Condition (2) is stated without comment, yet "a feedforward neural network doesn't really have it in the dynamics-relevant sense; a recurrent one does," and a transformer-with-context is subtle. Watch whether `03-llm-core/` confronts the question directly; if it does not, that is a finding (Claude, AUDIT-WORKING-384279).

#### 4. Readers often ask / wonder

- **Where exactly is the boundary, for an LLM?** Several substrates converged on the channel-collapse worry: the agent's own outputs become part of the $\Omega$ it perceives next turn, so "the strict distinction between agent and environment might dissolve when the agent's thoughts are written to the very context window it reads from." Repeatedly flagged as the case that will stress-test this root definition in Volume 3 (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-963715; Claude, AUDIT-WORKING-384279 — "the information-loss-boundary applies to $\Omega_t$, not to the prompt tokens"; Gemini, AUDIT-WORKING-542891).
- **Is a tool part of the agent or part of $\Omega$?** "If a developer uses a compiler, is the compiler part of the agent's $M_t$, or part of $\Omega$?" (Gemini, AUDIT-WORKING-829314). A natural first question for the TST instantiation.
- **Does the information-loss boundary limit theory of mind?** Raised as the first curiosity about multi-agent scope: when one agent's internal state is part of another's $\Omega$, "does the information loss boundary fundamentally limit theory of mind?" (Gemini, AUDIT-WORKING-193847; same multi-agent recursion at Gemini, AUDIT-WORKING-542891).
- **What about the agent/adaptive-system terminology?** Two substrates wondered whether the three-condition "agent" (which includes an action channel) collides with later passive-observer inclusion in `#scope-adaptive-system`; the segment now addresses this in its "Agent as umbrella term vs. cascade-tier label" Discussion paragraph (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-963715). Preserved as a fresh-reader-stumble signal even though resolved in-segment.

#### 5. Candidate figures

- **Lossy-aperture two-panel.** The isomorphic content is *not* "agent ↔ environment with arrows" (evocative but load-free); it is that the observation channel is a *lossy aperture*, and AAT's scope is exactly the region where the aperture is not fully open. Two-panel: in-scope (aperture partly closed, machinery alive) vs out-of-scope (aperture fully open, machinery vacuous/ghosted); the diagram must predict the degeneracy under perturbation (Claude, AUDIT-WORKING-472913, with a drafted `.tex`).
- **Asymmetric two-box coupling.** A two-box directed coupling that "emphasizes asymmetry: actions affect $\Omega$, but observations never reveal $\Omega$ directly" — environment large and structurally unconstrained, agent internal state small, observation arrow passing through a deliberately-narrowed lossy boundary (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **04-eli-core / the existential framing.** The strongest aspirational reach: the loss boundary is "the literal geometry of isolation … a mathematics of existential loneliness, from which adaptation is the only escape" (Gemini, AUDIT-WORKING-193847). Related: "an omniscient being cannot be an AAD agent because it never experiences aporia" — adaptive agency as "fundamentally a product of ignorance" (Gemini, AUDIT-WORKING-829314); and the chronica-as-identity-anchor / substrate-migration thread (Claude, AUDIT-WORKING-542891). High-application ELI vision; points at `04-eli-core/`, not this segment.
- **03-llm-core / channel collapse + the boundary case.** The LLM-boundary question above is genuinely a Volume-3 item: where the agent's output is its own next observation. Pointer left here only because it co-occurred in the foundational sweep (multiple substrates).
- **Naming-cycle seed.** "Agent-Environment Coupling" as a title slightly pre-empts the channels (coupling implies the action/observation channels formalized in the *next two* segments); alternates floated: "Agent-Environment Boundary" or "The Constitutive Information-Loss Boundary" (Claude, AUDIT-WORKING-471203). A terminology-workflow target, not a segment edit.
- **Section vs Part terminology drift.** The Discussion's "Part I" vs the segment-prose "Section I" usage across the foundational segments was repeatedly flagged as a corpus-wide normalization candidate (Claude, AUDIT-WORKING-384279). A sweep/`§G` item, not segment-local content.
