# Extracted Codex Feedback — 2026-04-22 (round 2)

**Source model:** OpenAI Codex
**Date:** 2026-04-22 (afternoon, second pass)
**Session UUID:** `1130893d-5ff9-4446-8d0e-741f1916d65d`
**Record UUID:** `d4351bcb-bdf2-4a1f-95c7-2929ff2edee9` (line 1001, ts `2026-04-22T15:38:11Z`)
**Topic:** L0 residual / on-policy short-circuiting; logogenic survival statement-level vs operational extractability; L1 default overgeneralization beyond strict-prerequisite; developer-as-act-agent exact-status conflating human vs AI; software "richest domain" overclaim; **Bigger Picture** — three-layer claim separation (defined / causally valid / operationally extractable), the unified "exact core under separability + structured repair + full general open" pattern, software as calibration laboratory not universal exemplar, claim-level vs segment-level status.

## Context

This was the second Codex pass on 2026-04-22, distinguished from the morning pass (`pending-findings-2026-04-22.md` Codex F1–F4) by its line-link format and substantive **Bigger Picture** architectural section. The five findings here are listed as `Codex r2 F1` through `Codex r2 F5` in `pending-findings-2026-04-22.md` (table only, line 47–50), but the verbatim Codex text and especially the Bigger Picture section were not preserved verbatim in any audit file. The Bigger Picture section is materially load-bearing — it identified the C-BP1 architectural proposal (three-layer claim separation) that subsequently became one of the strongest organizing principles of the framework's epistemic architecture.

## Disposition

The five Findings became Codex r2 F1–F5 in `audits/pending-findings-2026-04-22.md`:
- F1 (L0 residual on-policy short-circuiting) → resolved 2026-04-22 (commit `14a6095`); covariance test elevated to primary detection.
- F2 (logogenic statement vs operational extractability) → C-BP1 (claim-level layering); F25 verb-precision pass landed 2026-04-26.
- F3 (L1 as default overgeneralization beyond strict-prerequisite) → resolved 2026-04-22 (commit `4d050c8`) via Prop B.7 + Cramér-Rao refutation.
- F4 (developer-as-act-agent human vs AI conflation) → C-BP4 architectural proposal; partial resolution.
- F5 (software "richest domain" overclaim) → C-BP3.

The Bigger Picture architectural moves became:
- **C-BP1** (three-layer claim separation: defined / causally valid / operationally extractable) — landed as the meta-segment framework that became `#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing` (the three meta-segments now in CLAUDE.md).
- **The "exact core under separability + structured repair + full general open"** pattern — explicitly named in the catalog's M-section and referenced as a project organizing principle.
- **Software as calibration laboratory** — incorporated into TST framing.
- **Claim-level vs segment-level status** — partially adopted via the per-claim Findings schema landing 2026-04-26+.

## Verbatim feedback Joseph relayed

> Here is another set of Codex feedback items, including some high-level architectural suggestions. Not sure which ones are already documented:
>
> **Findings**
>
> Scope note: `04-logozoetic-agents/src` is currently empty, so the auditable theory surface is `01`-`03`.
>
> 1. [`causal-insufficiency-detection.md`](01-aad-core/src/causal-insufficiency-detection.md:23) says the L0 residual converges to $\pm\rho$, and [the same segment](01-aad-core/src/causal-insufficiency-detection.md:29) treats a persistently nonzero residual as the detection criterion. The strongest `src` counterevidence is [the precondition block](01-aad-core/src/causal-insufficiency-detection.md:35), which narrows the claim to verified convergence/stationarity/unbiased updates, plus [the sibling-covariance section](01-aad-core/src/causal-insufficiency-detection.md:49), which is a distinct and stronger localization mechanism. Status: **still real**. Those caveats do not cover the on-policy short-circuiting problem, so the residual criterion is still stronger than the repo currently warrants, while the covariance test looks closer to the stable core. Confidence: **medium-high**.
>
> 2. [`section-ii-survival.md`](03-logogenic-agents/src/section-ii-survival.md:37) opens with "16 survive exactly," and [`coupled-diagnostic-framework.md`](03-logogenic-agents/src/coupled-diagnostic-framework.md:18) says the diagnostic quantities "can be computed after each coupled update." The strongest `src` counterevidence is [`section-ii-survival.md`](03-logogenic-agents/src/section-ii-survival.md:127), which explicitly says this is only **statement-level**, not operational extractability, and [`coupled-update-dynamics.md`](03-logogenic-agents/src/coupled-update-dynamics.md:66), which says the $M/G$ decomposition is post-hoc and analytical rather than architectural/computable. Status: **still real**. The logogenic layer still slides from formal well-definedness to runtime measurability before the instrumentation layer has been published into `src/`. Confidence: **high**.
>
> 3. [`strategy-dag.md`](01-aad-core/src/strategy-dag.md:20) says "L1 ... is the practical default in complex domains" and that L0 results transfer exactly to correctly constructed L1 DAGs; [the same segment](01-aad-core/src/strategy-dag.md:122) repeats that the default assumption in complex environments should be L1. The strongest `src` counterevidence is [the Correlation Hierarchy's narrowing](01-aad-core/src/strategy-dag.md:105): L1 is the sweet spot only for **strict-prerequisite** common causes, [soft facilitators require L1'](01-aad-core/src/strategy-dag.md:107), and [formal transfer for L1' is still open](01-aad-core/src/strategy-dag.md:118). Status: **still real**. The right caveat now exists, but the headline/default framing still overgeneralizes beyond the regime actually supported by the segment. Confidence: **high**.
>
> 4. [`developer-as-act-agent.md`](02-tst-core/src/developer-as-act-agent.md:4) is tagged `status: exact`, and [its epistemic-status paragraph](02-tst-core/src/developer-as-act-agent.md:160) says each AAD quantity has a concrete, identifiable software counterpart. The strongest `src` counterevidence is [the earlier distinction](02-tst-core/src/developer-as-act-agent.md:63) that AI agents are "more explicitly representable," plus [the working note](02-tst-core/src/developer-as-act-agent.md:182) that explicit DAG applicability to implicit human planning is an open question. Status: **still real**. The current segment collapses "human developer" and "AI developer with externalized planning artifacts" into one exact mapping even though its own notes distinguish them. Confidence: **high**.
>
> 5. [`software-epistemic-properties.md`](02-tst-core/src/software-epistemic-properties.md:15) says software's six properties "collectively make it the richest operationalization domain for AAD." The strongest `src` counterevidence is [the scope block](02-tst-core/src/software-epistemic-properties.md:27), which narrows major advantages to codebase-only or code-internal regimes, and [the epistemic-status block](02-tst-core/src/software-epistemic-properties.md:70), which says the comparative claim is harder to verify and not systematic. Status: **already caveated**. I would not count this as a deep theory defect, but the headline rhetoric is stronger than the evidential support the segment itself assembles. Confidence: **medium-high**.
>
> I did **not** count composition-bridge, composition-scope, git-as-chronica, or loop-Level-2 claims as current findings, because current `src/` now narrows those substantially enough that the burden of proof is met.
>
> **`msc/` Context**
>
> - The L1 repair already exists in [`spike-L1-worked-example.md`](msc/spike-L1-worked-example.md:276) and is cataloged in [`SPIKES.md`](msc/SPIKES.md:43): the missing integration is to make "factor the common cause above the correlation it creates" and the strict-vs-soft split part of the front-door claim, not only the deep discussion.
> - The strongest off-segment repair for the residual-detection issue is [`pending-findings-2026-04-22.md`](msc/pending-findings-2026-04-22.md:43), which works through the on-policy censoring failure and effectively points toward sibling covariance, not residual size, as the primary detector. That argument is not yet absorbed into `src/`.
> - The missing operational layer for Class 2 agents already exists in [`agentic-tft-evaluation-framework.md`](msc/agentic-tft-evaluation-framework.md:1) and [`spike-hafez-integration-audit.md`](msc/spike-hafez-integration-audit.md:47): measurement of $M_t/\Sigma_t$ quality plus modular sidecar monitoring. The issue is not conceptual absence; it is under-integration into `03-logogenic-agents/src`.
> - The cleaner TST/AAD positioning already appears in [`feedback.md`](msc/feedback.md:43): software as the privileged high-identifiability domain where $\Sigma_t$ edges can sometimes be interventional, with other domains treated as exports under stronger assumptions. I did not find an equally mature `msc` repair for the human-developer exactness claim; that one still looks like a local `src/` reframing task.
>
> **Bigger Picture**
>
> - The deepest simplification is to separate three layers everywhere: `defined`, `causally valid`, and `operationally extractable`. Most of the live frictions are not raw contradictions; they are places where those three layers get collapsed.
> - A lot of the framework already follows one master pattern: exact core under a separability assumption, structured repair when separability fails, full general case expensive/open. `L0/L1/L1'/L2`, `Class 1/2/3`, and `Tier 1/2/3` are all instances of that same pattern. Making that explicit would make the theory cleaner and much easier to teach.
> - Software should be the calibration laboratory, not the universal exemplar. "Highest identifiability / intervention access / logging" is a tighter and more defensible claim than "richest domain," and it gives a clearer rule for what transfers outward and under which additional assumptions.
> - I would move from segment-level epistemic statuses to claim-level statuses. The repo is strongest when the definitional core, the transfer result, and the operationalization layer each carry separate status labels instead of sharing one umbrella tag.
