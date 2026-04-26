# Reflection 31 — def-strategy-dimension (Section II row 6)

## §4.2 dependency check

`depends: [form-complete-agent-state, form-objective-functional]`. Both upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "$G_t = (O_t, \Sigma_t)$ split — $O_t$ evaluation, $\Sigma_t$ guidance." ✓ exactly. Plus the strategy-representations ladder (none → cached → subgoals → causal DAG) I didn't predict — operationally useful. **Pretty much what I expected.**

**2. Cross-segment consistency.** Cross-refs all internally consistent. The "richness independence" observation (objective and strategy richness vary independently) is structural.

**3. Math verification (at discretion).** Skip — definitional.

**4. What direction next?** Row 7 = `der-causal-hierarchy-requirement`. The "Level 2 needed for planning" claim per OUTLINE.

**5. What errors should I now watch for?**
- Future segments treating the $O_t$ / $\Sigma_t$ split as a timescale claim (it's definitional, per explicit framing).
- Conflation of objective-richness with strategy-richness as a single hierarchy.
- Re-emergence of the $\delta_{\text{goal}} = G_t - M_t$ type-error pattern (the segment explicitly notes this was previously wrong).

**6. Predictions for next segments.** Row 7 = `der-causal-hierarchy-requirement`. status:deps-verified per OUTLINE. Probably depends [def-pearl-causal-hierarchy, def-value-object]. Argues that evaluating $Q_O$ requires Level 2 (interventional) causal access — connects to the Bareinboim CHT.

**7. What would I change?** The "Working Notes" includes three open issues (cognitive cost of $\Sigma_t$, commitment state $D_t/I_t$, resource budget). All explicitly listed as open. The commitment state issue is interesting — "considering" vs "executing" branches in $\Sigma_t$ aren't formally distinguished. Could matter for multi-agent commitments. Honest framing.

**8. What am I now curious about?**

(a) **The richness-independence claim.** Chess player has simple $O_t$ (win) and complex $\Sigma_t$ (opening theory, tactics). Multi-objective optimizer has complex $O_t$ (Pareto) and simple $\Sigma_t$ (gradient descent). This makes operational sense and gives a clean design-space framing.

(b) **Cognitive cost of $\Sigma_t$ for LLMs.** Working Note: "the DAG must fit in the context window. No formal analog of $\beta$ (compression cost) exists yet for strategy; this is an open question." Per CLAUDE-2.md priming, `#deriv-strategy-cost-regret-bound` (forward) addresses this — the strategy-cost objective uses KL-to-reference-policy (IT-MDP form, not IB form). So there's a formal analog, just structurally different from the IB Lagrangian.

(c) **The "type error in $\delta_{\text{goal}} = G_t - M_t$" historical reference.** This was an earlier formulation that didn't typecheck (subtracting a graph from a state vector). Worth noting: the segment shows the framework's discipline of catching and naming type errors. Section E candidate.

**9. What new knowledge enabled.** $G_t$'s structural decomposition. Strategy-representations ladder (4 levels). Independence of richness on the two axes. Type-clean replacement of the $\delta_{\text{goal}}$ type error via properly-typed satisfaction-gap and control-regret.

**10. Should the audit process change?** Continuing.

**11. Outline updates.** No new findings. Section E confirmation: the type-error catch-and-rename pattern (from $\delta_{\text{goal}}$ to satisfaction-gap/control-regret) is a discipline observation worth surfacing.

**12. How valuable does this segment *feel* to me?**

Medium. Clean definitional split — necessary scaffolding but not structurally novel. The richness-independence observation is the most operationally useful piece. The strategy-representations ladder gives a clear progression for agent architects.

Magnitude: middle of pack. Type: clean definition. Engagement: read easily; the historical type-error note caught my attention as a discipline indicator.

**13. What does the framework now potentially contribute to the field?**

- **Agent architects** get a clean design-space separation: upgrade strategy engine without changing objective, or vice versa.
- **LLM agent designers** get the cognitive-cost framing for $\Sigma_t$ — finite context window forces strategy compression. Connects to deriv-strategy-cost-regret-bound's KL-to-reference-policy formulation (per CLAUDE-2.md priming).
- **RL theorists** get a clean type-distinction between value-evaluation ($O_t$ → $V_{O_t}$) and policy-guidance ($\Sigma_t$ → action). Most RL conflates these into Q-functions; AAD splits them.
- **Cognitive scientists** get a structural framework for "what an agent wants" vs "the agent's theory of how to get it" — useful for distinguishing motivation from competence.

Most distinctive: the **independence-of-richness-axes** observation makes it explicit that objective complexity and strategy complexity are separate design dimensions. This is operationally useful but rare to see stated formally.

## Status-label / discipline

`status: axiomatic` for a definition. `stage: deps-verified`.

## Cadence check

Holding. Next: row 7 = `der-causal-hierarchy-requirement`.
