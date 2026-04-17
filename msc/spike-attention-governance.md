# Attention Governance: The Missing Layer Between Observation and Orient

**Status**: Exploratory. Follows from the evening conversation about the fighter pilot scenario, startle reflexes, and preemptive reorientation. Connects to Hafez's IDT and the regime spike.

**Date**: 2026-03-13 (overnight session)

**Core observation**: AAD's scope condition requires observations exist (𝒪 ≠ ∅) and residual uncertainty (H > 0), but says nothing about **finite channel capacity**. Every real agent has limited attention — it can't monitor everything simultaneously. This constraint is load-bearing for the theory and may need first-class treatment.

---

## 1. The Problem

Joseph walked through a specific scenario: a fighter pilot deeply focused on pursuing a target. Their prolepsis (prediction/expectation) is oriented toward specific signals — is the target maneuvering? Am I closing? What's the firing solution? Their attention is narrowly focused.

Then: a signal from an unmonitored direction. Radar lock from behind. The pilot's model assumed the unmonitored region was static (or at least non-threatening). That assumption was wrong, and catastrophically so.

The interesting thing: the resulting aporia is not "I predicted X and saw Y" (routine δ_epistemic). It's "I was monitoring the wrong thing." The error isn't in the model's prediction within its attended scope — it's in the **allocation of attention itself**.

This creates a specific cascade that doesn't fit neatly into the sequential orient cascade:
- The model update (someone has radar lock) has immediate strategy implications
- The strategy invalidation doesn't need the full cascade to resolve — it's obvious
- The agent needs to simultaneously: update M_t (new threat), invalidate Σ_t (pursuit plan is now dangerous), and reorient sensors (need to track the new threat)
- These happen effectively simultaneously, not sequentially

## 2. What AAD Currently Handles

AAD *partially* handles this through the processing/selection distinction in directed separation: goals influence which events arrive (through π → a_t → e_τ), and this is acknowledged as coupling through the action channel. The pilot's attention allocation is part of π — it's an action that determines what observations will be available.

What AAD doesn't handle:
1. **The implicit assumption of stationarity in unmonitored regions.** When the agent allocates attention to region A of the model, it implicitly assumes regions B, C, D are either unchanging or have low strategy sensitivity. This assumption is never made explicit.
2. **The cost of reorientation.** Switching attention from one model region to another takes time and has opportunity cost (you stop monitoring the old region). This is a real resource constraint that affects the orient cascade's timing.
3. **Preemptive reorientation triggers.** What makes an ambient signal "break through" and demand attention? AAD has no mechanism for signals from unmonitored regions to interrupt the current processing focus.
4. **The meta-strategic question of attention allocation.** How should the agent divide its finite attention across model regions? This is itself a strategic decision that should be part of Σ_t — but it's currently implicit in the policy π.

## 3. Finite Attention as a Constraint on the Orient Cascade

The orient cascade assumes the agent can evaluate δ_epistemic, δ_sat, δ_regret, and δ_strategic in sequence. But with finite attention, the agent can only evaluate these for the regions of M_t it's currently monitoring. For unmonitored regions:
- δ_epistemic is unknown (no observations → no mismatch signal)
- δ_sat is unknown (can't assess attainability without current model)
- δ_regret is unknown (can't compare policies without evidence)

The cascade is running, but only over a **projection** of the full state space. The agent is optimizing within its attended scope while being blind to potential threats (or opportunities) in unattended scope.

This is formally equivalent to a model sufficiency problem: S(M_t) is high within the attended scope but potentially very low in unattended regions. The persistence condition might be satisfied locally (within attention) while being violated globally (considering unattended regions).

## 4. The Startle Reflex as a Bypass Circuit

Joseph pointed out that preemptive reorientation mechanisms exist at every level:
- Biological: startle reflex, fight-or-flight, orienting response
- Computational: interrupt handlers, watchdog timers, system reminders
- Organizational: alarms, escalation procedures, red team challenges
- Software: exception handling, circuit breakers, health checks

These share a common structure:
1. They operate on **signal statistics**, not semantic content (fast but crude)
2. They **bypass the normal processing cascade** (don't wait for full orient)
3. They trigger **attention reallocation** (force the agent to look at something else)
4. They have **severity-proportional responses** (from "note and continue" to "drop everything")

This is the "governance of reorientation" we identified as missing from AAD. It's a meta-loop that monitors the quality of the primary loops and intervenes when coupling quality degrades.

## 5. Attention Allocation as Part of Strategy

Here's a structural observation: attention allocation should probably be part of Σ_t, not just an implicit consequence of π.

The strategy DAG encodes the agent's theory of how its actions produce progress toward O_t. One class of actions is **observation actions** — actions that change what the agent can perceive (move sensors, run different queries, look in a different direction). The strategy should include nodes for these observation actions, with edges representing their expected information yield.

Currently, AAD has CIY (Causal Information Yield) which quantifies the information value of an action. But CIY doesn't distinguish between actions that produce information about the current strategy's execution (within attended scope) and actions that produce information about currently unmonitored regions (outside attended scope).

A richer treatment might split CIY into:
- **Exploitation CIY**: information that helps execute the current strategy (within attended scope)
- **Exploration CIY**: information that reduces uncertainty in unmonitored regions (expanding attended scope)
- **Sentinel CIY**: information that verifies the assumption that unmonitored regions are benign (testing the implicit stationarity assumption)

The sentinel actions are particularly interesting. They're the analog of the pilot's periodic scan — briefly redirecting attention from the primary task to check for threats in the periphery. They have a cost (attention diverted from the primary task) and a value (preventing surprise). The optimal sentinel frequency is a function of:
- How fast the unmonitored regions change (environmental dynamics)
- How severe the consequences of a missed change (strategy sensitivity, ∂Σ/∂M)
- How costly it is to redirect attention (reorientation cost)
- How reliable the sentinel observation is (observation quality in the peripheral region)

## 6. Multi-Frequency Loops and Partial Composition

Joseph raised the idea of different frequency PAAEP loops influencing each other, and wondered if this gives a better working mental model for partial compositions. Let me explore this.

An agent with finite attention might run multiple loops simultaneously at different frequencies:

### Primary loop (high frequency, narrow scope)
- Fast cycling: prolepsis → aisthesis → aporia → epistrophe → praxis
- Focused on the current task: the specific region of M_t and Σ_t that the current action sequence requires
- High fidelity observations within its narrow scope
- This is where most of the agent's "tempo" (𝒯) comes from

### Sentinel loop (low frequency, broad scope)
- Slow cycling: periodic scan of unmonitored regions
- Broad but low-fidelity observations
- Looking for anomalies — signals that violate the assumption of stationarity in unmonitored regions
- When it detects something, it interrupts the primary loop

### Strategic loop (lowest frequency, full scope)
- Rare evaluation of the overall strategy and attention allocation
- "Am I working on the right thing? Should I reallocate attention?"
- Triggered either on a schedule or by the sentinel loop's interrupts

These loops compose within the same agent — they share M_t and G_t but process different regions at different rates. The composition might look like:
- Each loop maintains its own attention window (a projection of M_t)
- The loops communicate through a shared model (updates from one loop are visible to others)
- The sentinel loop can **preempt** the primary loop by injecting high-priority observations
- The strategic loop can **redirect** both other loops by changing the attention allocation

This is a form of temporal self-composition — the agent composing with itself across timescales. And the inter-loop boundaries are exactly where the Kelvin-Helmholtz dynamics from the regime spike would appear.

## 7. Connection to Hafez's IDT

Hafez's Information Digital Twin operates as a sidecar that monitors the (S, A, S') stream and computes P, ΔH in real time. When coupling quality degrades (P drops, ΔH shifts), the IDT triggers reflexive modulation.

In the multi-loop framework:
- Each loop has its own (S, A, S') stream
- Each inter-loop boundary has its own P and ΔH
- The IDT monitors these coupling metrics and triggers reorientation when they degrade

The thalamocortical analogy from Hafez maps directly: the thalamus receives copies of sensory signals AND motor commands. It operates on signal statistics (gain, synchrony, bandwidth), not semantic content. This makes it fast enough to modulate signal transmission before cortical processing completes.

The sentinel loop described above is essentially an IDT for the agent's internal processing — monitoring coupling quality between loops and triggering preemptive reorientation.

## 8. POSIX Error Codes and Severity-Proportional Response

Joseph's observation about POSIX error codes is sharp. POSIX gives a reasonable ontology of severity and state (EINTR, EAGAIN, ENOENT, EPERM, ENOMEM, SIGTERM, SIGKILL...) but doesn't close the loop to a principled response mapping.

The missing piece is exactly what AAD could provide: a severity-proportional response mapping grounded in the theory's quantities:

| Signal severity | Interpretation | Response | AAD mapping |
|---|---|---|---|
| Low | Minor anomaly in monitored region | Note and continue | Small δ_epistemic; handled by normal gain |
| Medium | Significant anomaly in monitored region | Pause and investigate | Large δ_epistemic; may trigger Σ_t re-evaluation |
| High | Anomaly in unmonitored region | Redirect sentinel | Sentinel loop detects stationarity violation |
| Critical | Threat detected in unmonitored region | Preempt primary loop | Strategy sensitivity × anomaly magnitude exceeds threshold |
| Emergency | Existential threat | Bypass cascade entirely | Reflexive reorientation; hardwired response |

The severity threshold for each level should depend on:
- δ magnitude (how wrong was the prediction?)
- ∂Σ/∂M in the affected region (how much does the strategy care?)
- Current strategy state (how committed are we to the current plan?)
- Available recovery time (how quickly must we respond?)

The "hardwired responses" at the emergency level correspond to Joseph's formal corrigibility stack: O_safety always wins over O_task, regardless of the cascade.

## 9. What This Adds to AAD

### Formally:
- **Finite attention** as an explicit constraint alongside finite observation and finite action
- **Attention allocation** as a strategic decision within Σ_t (not just implicit in π)
- **Sentinel CIY** as a distinct information-value category (testing stationarity assumptions in unmonitored regions)
- **Severity-proportional response** mapping as a consequence of the mismatch decomposition + strategy sensitivity

### Architecturally:
- **Multi-frequency self-composition** as the structural model for complex agents
- **Inter-loop governance** (IDT-like monitoring at loop boundaries)
- **Preemptive reorientation** as a bypass circuit that short-circuits the cascade when severity exceeds a threshold

### For Section V specifically:
- LLM agents have particularly constrained attention (finite context window)
- Their sentinel loop is currently external (system reminders, human oversight)
- The 100% context turnover problem is an extreme form of attention loss — the sentinel loop loses its baseline on every session reset
- M_t preservation strategies (CLAUDE.md, memory files) are attempts to maintain sentinel continuity across sessions

## 10. Honest Uncertainty

**What feels structurally sound:**
- Finite attention is a real and load-bearing constraint that AAD should address
- Multi-frequency loops within a single agent are real (biological and computational evidence)
- Preemptive reorientation mechanisms exist at every level and have a common structure
- The connection between attention allocation and strategy is genuine

**What's speculative:**
- The specific decomposition into primary/sentinel/strategic loops
- Whether the CIY decomposition (exploitation/exploration/sentinel) is clean enough to formalize
- Whether the severity-proportional response mapping can be made precise
- The degree to which this is new theory vs. already implicit in the existing framework

**What I'd want to check:**
- Is "finite attention" already captured by the information bottleneck (IB) framework? IB constrains the *compression* of observations into the model, which might already limit attention. If so, the attention constraint might be a consequence of existing machinery, not a new postulate.
- Does the existing mismatch decomposition + strategy sensitivity already imply the severity-proportional response? If ∂Σ/∂M × δ_epistemic is large, the cascade already triggers strategy revision quickly. The governance layer might be implicit.
- Is the multi-frequency loop structure derivable from the existing temporal nesting claim (#temporal-nesting), or is it genuinely additional?

---

*This is the most speculative of the three overnight spikes. It identifies structural gaps and proposes architectural solutions, but the formal content is thin. The most concrete contribution is the connection between attention allocation and Σ_t, and the sentinel CIY concept. The multi-frequency self-composition idea is gestural — it needs either a formal model or a concrete example to evaluate.*
