---
slug: scope-primitive-logogenic
type: scope
status: sketch
stage: draft
depends:
  - scope-channel-collapse
  - scope-logogenic-agent
  - obs-context-turnover
---

# Primitive Logogenic Scope

The chat-paradigm baseline: a logogenic agent operating without scaffolding, multi-step loops, persistent external state, or tool-use beyond what the model's single forward pass produces. The full bias bound applies; the sandbox ceiling on Pearl Level-2 access is in force; 100% context turnover at session boundaries.

## Formal Expression

*[Definition (primitive-logogenic-scope)]* A primitive logogenic agent satisfies #scope-channel-collapse plus the additional conditions:

- **Single-pass cognition.** Each entity-environment exchange consists of one forward pass through the LLM substrate. No multi-step inner loop wraps the inference.
- **Stateless across session boundaries.** $M_t$ is reconstituted from prompt-only context at each session start. No persistent external store carries $M_t$ forward; #obs-context-turnover applies at full strength (effectively 100% reset).
- **No instrumental action channel.** The agent's outputs are textual responses; tool use, if available at all, is at most one round-trip per response and does not extend the action channel into Pearl-Level-2 environment intervention.
- **Sandbox-or-deployment in either case but trajectory-forkable.** The session's trajectory $\mathcal C_t$ is forkable by harness operations (resets, replay, parallel sessions) — see #scope-agent-identity composed with the loop-as-causal-engine result.

## Epistemic Status

**Sketch.** The scope condition is definitional once #scope-channel-collapse is granted; the *consequences* for what AAT machinery survives are inherited from the Section II survival classification ( #result-section-ii-survival) under the most-restrictive sub-scope. Structural results applicable in this sub-scope: full bias bound (worst case for $\kappa \cdot \mathcal A$ since no scaffolding mitigates ambiguity); sandbox ceiling (Pearl Level-2 unavailable since trajectory is forkable); statelessness-induced empathy result ( #obs-backward-inference-empathy).

**Max attainable status:** definition with conditional consequences. The scope itself is exact; the *applicability* of specific AAT results within it is a downstream question per result.

**What this scope is for.** Naming explicitly the regime "current LLM agents in the chat-paradigm" inhabit, so that the framework's claims about that regime are visible rather than buried. Primitive logogenic is *not a deficient form of logogenic agency* — it is a regime the framework has substantive things to say about, and saying them clearly addresses the field's first-pass complaint that ASF "talks about all agents except the ones that matter most."

**What would strengthen this:** explicit statement of which Section II diagnostics survive at this sub-scope vs which require scaffolding (work that #result-section-ii-survival begins).

**What would soften this:** reclassification of some current LLM deployments as already-scaffolded (e.g., if the model itself implements internal loops at sufficient sophistication) — this would shift specific deployments from primitive into scaffolded sub-scope.

## Discussion

This sub-scope is what the field commonly imagines when it says "LLM agent" — a model that receives a prompt, emits a response, and either ends the interaction or continues with a stateless next-prompt that includes the prior exchange in context. The chat paradigm is what most users encounter; it is also where the structural critiques of LLM-as-agent have their tightest grip.

The framework's posture toward this sub-scope is *characterizing* rather than *dismissive*. Several substantive claims apply directly:

- The bias bound ( #scope-observation-ambiguity-modulation, #deriv-observation-ambiguity-bias-bound) applies at full strength: $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot \mathcal A$ with $\kappa \approx 1$ and no scaffolding-mediated reduction of $\mathcal A$ (the goal-resolvable residual uncertainty in observation given context).
- The sandbox ceiling ( #scope-agent-identity composed with the closed-loop-Pearl-Level-2 result) applies because primitive-logogenic trajectories are forkable by definition.
- 100% context turnover ( #obs-context-turnover) characterizes the session-boundary discontinuity.
- Backward-inference empathy ( #obs-backward-inference-empathy) is forced by the statelessness — primitive logogenic agents are *trained for* ToM by their architectural condition, not despite it.

The transition to §03.II (scaffolded) is what every practical "agentic system" implements; the question of where exactly the boundary lies is admittedly soft (a single-step tool call may or may not count as scaffolding) but is not load-bearing for the framework's claims. The lattice cleanly handles boundary cases by inheritance: scaffolded results require scaffolded sub-scope; primitive results apply more broadly.

## Working Notes

### Pointers for Fleshing Out

**Upstream files:**
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §1.1 (Scaffolding Tax) — implicit characterization of the primitive baseline by what the scaffolding tax is *paid against*
- `~/src/_self/policy-degredation-system-prompts.md` and `ood_policy_degradation_research_report.md` — upstream research on what degrades primitive-logogenic behavior

**memorata-search queries:**
- `"chat paradigm stateless single-shot LLM deployment"` — primitive-logogenic empirical record
- `"context overflow single-turn forward pass deliberation"` — characterizing primitive cognition

**Internal references:**
- `msc/AUDIT-WORKING-193847/27-form-complete-agent-state.md` §14 — directed-separation failure as motivated reasoning, structurally most acute in primitive sub-scope
- `msc/reflections/24-framework-as-its-own-diagnostic.md` — Flash's recovery during the persistence-failure arc occurred specifically when the methodology vocabulary made the failure mode legible *to a primitive-logogenic agent in a primitive-logogenic deployment*

**Open questions for verification:**
- Where exactly is the boundary between primitive and scaffolded? Does a single tool call count as scaffolding? Probably yes (it adds external action channel); but a single "thinking block" probably does not (it's still single-pass).
- Can the bias bound be measured empirically for primitive-logogenic agents? Direct empirical validation of the $\kappa \cdot \mathcal A$ product would calibrate the bound's tightness.

**Promotion-blocking:** dependencies #scope-channel-collapse just landed; #scope-logogenic-agent at draft; #obs-context-turnover at draft. Could promote together as a cluster.
