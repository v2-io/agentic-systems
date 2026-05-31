# Reflection 32 — der-causal-hierarchy-requirement (Section II row 7)

## §4.2 dependency check

`depends: [def-value-object, def-pearl-causal-hierarchy, scope-agency]`. All upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "Level 2 needed for planning. Depends [def-pearl-causal-hierarchy, def-value-object]." ✓ exactly. Plus scope-agency in depends, plus the scope-narrowing to learning purposeful agents (excluding PID/LQR/hardcoded reactive policies). **Pretty much what I expected.**

**2. Cross-segment consistency.** Cross-refs all internally consistent. The "learning-agent scope" narrowing is a clean structural move — distinguishes AAD's machinery from pre-compiled control.

**3. Math verification (at discretion).** Skip — Bareinboim CHT does the heavy lifting; application to $Q_O$ via $do(a)$ is direct.

**4. What direction next?** Row 8 = `der-loop-interventional-access`. The feedback loop → Level 2 data by construction. Per CLAUDE-2.md priming: three-mode subsection (Mode 1 agent-self / Mode 2 observer-on-sub-agent / Mode 3 reserved).

**5. What errors should I now watch for?**
- Future segments treating Level 2 access as automatic for all agents (it's restricted to learning agents).
- Conflation of $do(a)$ with $A=a$ (the segment is explicit they differ).
- Treating pre-compiled agents (PID, LQR) as if Section II machinery applies to them (excluded by scope).

**6. Predictions for next segments.** Row 8 = `der-loop-interventional-access`. status:draft per OUTLINE. Probably depends on der-causal-hierarchy-requirement, def-pearl-causal-hierarchy, scope-agent-identity (for the trajectory-singularity grounding).

**7. What would I change?** The Hafez 2026 IDT empirical anchor (89% vs 44%) is good — gives an empirical handle on the theoretical claim. The "LLMs trained on causally-structured text absorb causal priors" Working Note is interesting framing: LLMs have noisy priors from training, which the loop then verifies. Operationally significant for LLM analysis.

**8. What am I now curious about?**

The "noisy priors from mixed provenance (experimental, observational, speculative)" framing for LLMs is sharp — it explains why LLMs have *some* causal capacity (training data includes causal information) but *limited* causal verification (the priors aren't all interventional). The framework's combination — priors accelerate, loop verifies — is operationally useful.

The scope-narrowing to learning agents excludes pre-compiled controllers. Question: is there a hybrid case where an agent has a pre-compiled core (LQR controller) but learning peripheral processes (parameter adaptation)? Probably yes; would need per-component analysis.

**9. What new knowledge enabled.** Formal connection between value-object evaluation and Pearl's causal hierarchy. Scope narrowing to learning agents. Bareinboim CHT applied to action selection.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** No new findings.

**12. How valuable does this segment *feel* to me?**

Medium. Clean derivation that connects two prior segments (value-object + Pearl-hierarchy) via Bareinboim's theorem. The scope-narrowing to learning agents is operationally useful. The Hafez IDT empirical anchor is good. Not as foundational as der-directed-separation but does its derivation work cleanly.

Magnitude: middle of pack. Type: clean derived result with external-theorem application.

**13. What does the framework now potentially contribute?**

- **RL practitioners** get a formal statement of why associational training data is insufficient for action selection — Bareinboim's CHT applied to $Q_O$.
- **Causal-inference researchers** get an applied case study: action-value evaluation as Level 2 query.
- **AI-architecture taxonomists** get a learning-agent scope distinct from pre-compiled control. Operationally separates AAD's domain from classical control.
- **LLM analysts** get the priors-from-training + loop-verifies framing. Explains why LLMs have causal capacity (data) and loop-amplification (deployment).

Most distinctive: explicit connection of decision-theoretic value-evaluation to Pearl's causal hierarchy with formal scope (learning agents only). Most decision-theory literature is implicit about whether Level 1 or Level 2 reasoning is being used.

## Status-label / discipline

`status: exact`. The derivation is a direct application of CHT. `stage: deps-verified`.

## Cadence check

Holding. Next: row 8 = `der-loop-interventional-access`.
