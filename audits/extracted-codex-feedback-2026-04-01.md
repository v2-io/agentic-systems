# Extracted Codex Feedback — 2026-04-01

**Source model:** OpenAI Codex
**Date:** 2026-04-01 (single relay, evening session)
**Session UUID:** `615ef48a-2103-460f-bf3d-373168d82168`
**Record UUID:** `ab77d048-9e19-49ee-87b2-f1dec63d84cb` (line 538, ts `2026-04-01T23:51:58Z`)
**Topic:** First fresh Codex pass over the ACT (now AAD) core after the segment-based theory restructure.

## Context

This was the first round of Codex external review against the new segment-based 01-act-core/ structure (the project still used the "ACT" name; AAD rename came 2026-04-16). Joseph relayed Codex's findings before launching parallel Codex+Gemini agents for further critique. The local Claude session subsequently incorporated this feedback into `audits/analysis-2026-04-01.md` (which has Codex's findings paraphrased and grouped, but not preserved verbatim).

## Disposition

The six numbered findings here were processed into `audits/analysis-2026-04-01.md` (where they appear as Codex's structural emphasis under "Where the Reviews Diverge"). The five "What I Would Do Next" items shaped subsequent cycle priorities (Section I publication kernel, Section III demotion vs. proof, three-way split, logogenic spinoff). Several of these items were repeated/reformulated in later rounds (04-02, 04-06).

## Verbatim feedback Joseph relayed

> Here is a fresh Codex look at ACT in general:
> • After reading the ACT outline, workbench, prior reviews, prior-art notes, and the load-bearing segment files directly, my judgment is: ACT is a real and nontrivial theory project with a defensible core, but it is not yet a finished general theory of agency. The strongest parts are publishable. The weakest parts are exactly where the theory tries to become universal.
>
> Findings
>
> 1. **High** — ACT is still not a general theory of the agent class it most wants to explain. `01-act-core/src/directed-separation.md:35` correctly scopes the clean M -> G factorization to goal-blind epistemic processing, and `03-logogenic-agents/OUTLINE.md:9` states outright that LLM-style agents violate it by construction. That is honest and better than hand-waving, but it means Section II is currently a theory of modular purposeful agents, not yet a theory of contemporary agentic AI in general. One extra criticism here: the proposed κ_processing operationalization `01-act-core/src/directed-separation.md:58` is distribution-dependent, so it measures realized coupling under a task distribution, not pure architecture.
> 2. **High** — Composition is still the main theorem debt in the core. `01-act-core/src/composition-closure.md:86` explicitly labels the bridge lemma a sketch, `01-act-core/src/composition-closure.md:110` says the reuse of the Lyapunov machinery still needs verification, and `01-act-core/src/tempo-composition.md:18` leaves the critical ε* -> C_coord mapping open. Since the project treats composition consistency as part of the theory's structural backbone `WORKBENCH.md:204`, this is not a side issue. It is the biggest place where the manuscript can currently read stronger than the proofs warrant.
> 3. **Medium-high** — Strategy-as-DAG is a strong canonical representation, but not yet a forced one. `01-act-core/src/graph-structure-uniqueness.md:67` makes the P3→Markov step a sketch, and `01-act-core/src/graph-structure-uniqueness.md:163` repeats that the theorem-strength claim rests on that unresolved step. Meanwhile `01-act-core/src/strategy-dag.md:63` and `01-act-core/src/strategy-dag.md:89` acknowledge that the tractable confidence propagation systematically overestimates success under correlated failures. Acyclicity is solid `01-act-core/src/strategy-dag.md:69`; uniqueness is not.
> 4. **Medium** — The CIY / exploration layer is promising but not yet part of ACT's hard mathematical core. `01-act-core/src/causal-information-yield.md:17` gives a defensible canonical definition, and `01-act-core/src/causal-information-yield.md:35` is admirably strict about not optimizing the sign-indefinite proxy. But `01-act-core/src/causal-information-yield.md:53` and `01-act-core/src/causal-information-yield.md:59` leave the unified policy objective discussion-grade. That means ACT's claimed differentiation from active inference is plausible, but not yet sharp enough to carry a positioning paper by itself `msc/02-prior-art-assessment.md:180`.
> 5. **Medium** — The software operationalization still overclaims causal access. `02-tst-core/src/system-coupling.md:31` calls git-based co-change "genuinely causal," but `02-tst-core/src/system-coupling.md:37` immediately admits commit bundling and convention-driven grouping as confounds. `02-tst-core/src/coherence-coupling-measurement.md:36` makes the same stronger-than-earned move. Until `#causal-discovery-from-git` exists, this should be framed as a strong empirical program, not a secure causal bridge.
> 6. **Medium** — The project's next risk is failure to converge, not failure to generate ideas. The ACT outline is still almost entirely draft `01-act-core/OUTLINE.md:20`, and the project's own inherited assessment says the same thing bluntly: too much breadth, not enough promotion and publication `msc/2026-03-14-fresh-eyes-assessment.md:120`. I agree. The danger is not that there is no theory here. It is that the strongest 20% gets buried under the unfinished 80%.
>
> Overall Assessment
>
> The part I would take most seriously in front of skeptical readers is the ACT core around persistence, mismatch, and decision diagnostics. The nonlinear persistence machinery is now stated carefully and credibly `01-act-core/src/persistence-condition.md:19`, `01-act-core/src/sector-condition-stability.md:17`. The recursive-update derivation is unusually honest about what is theorem and what is modeling commitment `01-act-core/src/recursive-update-derivation.md:152`. The satisfaction-gap / control-regret split is, in my view, the most genuinely useful original formalization in the repo `01-act-core/src/satisfaction-gap.md:22`, `01-act-core/src/control-regret.md:31`.
>
> The simulation work also looks serious rather than decorative. It is explicitly theory-shaping, not just confirmatory `01-act-core/src/simulation-results.md:21`, and it is careful to say it is internal validation inside the model class, not external empirical proof `01-act-core/src/simulation-results.md:85`. That is good scientific discipline.
>
> What I Would Do Next
>
> 1. Write the first ACT paper around the publishable kernel: Section I, the two-gap diagnostic, and the acyclicity result. Present directed separation as a scope condition, not as a universal law of agency.
> 2. Either prove the 2-agent composition bridge case or demote Section III more aggressively. Right now that theorem debt is too central to leave in "almost certainly correct" form.
> 3. Enforce the project's own three-way split between inevitability core, canonical formulations, and empirical programs `WORKBENCH.md:186`. That editorial change would materially improve credibility.
> 4. Treat logogenic agents as a sequel with a coupled update law from the start, exactly as the logogenic outline says `03-logogenic-agents/OUTLINE.md:9`. Do not try to smuggle LLM agents back into the modular case by approximation rhetoric.
