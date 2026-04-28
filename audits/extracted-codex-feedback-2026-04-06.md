# Extracted Codex Feedback — 2026-04-06 / 04-07

**Source model:** OpenAI Codex (three passes across two days)
**Dates:** 2026-04-06 (two passes), 2026-04-07 (re-check)
**Sessions:** `e39166b4-9d21-4184-9d9d-12e9e0b83972` (lines 780, 1123); `bd447ff0-12e7-4552-8794-99fb193963ac` (lines 121, 492)
**Topic:** LLM Class-2 exclusion as central limitation; one-step-only continuation convention weakening 2×2 diagnostic; surrogate-vs-actual plan persistence; OUTLINE dependency-ordering violations (14 found); causal sufficiency motivation; observable-intermediates necessity overclaim; loop-Level-2 selection bias.

## Context

This batch is the source for `audits/analysis-2026-04-06.md`, which is a *verified Claude synthesis* of the Codex findings — but the verbatim Codex text was not preserved there. The 2026-04-07 re-check (`bd447ff0` line 492) is the "improvement assessment" that confirms most of the prior findings landed cleanly: it is itself archaeology of how external review tightens a theory across short cycles.

## Disposition

Most items here became line-level fixes documented in `audits/analysis-2026-04-06.md`'s C1–C6 section. The OUTLINE dependency-ordering violations were swept in the 04-06 cycle. Items 1–6 of the first 04-06 batch are explicitly verified and resolved in the analysis file. The 04-07 re-check confirms loop-access framing, orient cascade, and composition closure all materially improved; only causal-sufficiency mixed messaging across `graph-structure-uniqueness.md` ↔ `strategy-dag.md` and the observable-intermediates header overstatement persisted past that cycle.

## Verbatim feedback Joseph relayed

### First 04-06 pass — six findings (`e39166b4` line 780, ts 2026-04-06T16:02:28Z)

> What do you make of this feedback from Codex just now?:
>
> • Findings
>
> 1. **Critical**: Section II's "exact" agentic machinery explicitly excludes the most important present-day agent class. The docs state that transformer/LLM agents are Class 2, directed separation fails for them by construction, the orient cascade becomes approximate, and even the value object's interventional estimates can be biased when directed separation fails. That means `01-act-core` is not yet a theory of modern LLM-based agents so much as a theory of modular agents, with the main AI case deferred elsewhere. `01-act-core/OUTLINE.md:7`, `01-act-core/src/directed-separation.md:52`, `:72`, `:85`, `01-act-core/src/value-object.md:38`.
> 2. **High**: The "exact diagnostic core" is exact only as a set of definitions, not as a robust decision procedure. The canonical continuation convention freezes continuation at $\pi_{\text{current}}$, so $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are explicitly one-step, local, convention-relative quantities; the same multi-step recoverable situation can look "unattainable" or "near-optimal" depending on the continuation convention. That materially weakens the inferential force of the orient cascade's 2×2 table. `01-act-core/OUTLINE.md:7`, `01-act-core/src/value-object.md:40`, `01-act-core/src/satisfaction-gap.md:13`, `:46`, `01-act-core/src/control-regret.md:13`, `01-act-core/src/orient-cascade.md:48`.
> 3. **High**: The strongest strategic results are proved for an internal surrogate, not for actual plan success. The proved mismatch state is $\delta_s = \hat P_\Sigma - \Phi$, but $\Phi$ is only the independence-model plan value; the theory also says correlated failure is the dominant real-world case and that $\hat P_\Sigma$ systematically overestimates success there. Meanwhile the finer-grained $\delta_{\text{strategic}}$ that the cascade wants for real strategy revision remains open because credit assignment is unresolved. So the formal persistence result is mostly a theorem about calibration inside the model's own simplifying assumptions. `01-act-core/src/strategy-dag.md:70`, `:96`, `:110`, `01-act-core/src/strategic-calibration.md:46`, `01-act-core/src/credit-assignment-boundary.md:47`, `01-act-core/src/strategy-persistence-schema.md:32`, `:55`.
> 4. **Medium-high**: The composition section is still programmatic rather than locked down. Its closure criterion depends on analyst-chosen admissibility classes and free parameters like $\varepsilon_I$ and $L$, and the bridge from closure defect to bounded macro error requires an extra contraction assumption that is not implied by ACT's own admissibility conditions. The file also says the richer purposeful-agent worked case is still missing, so Section III is not yet strong enough to fully support the scale-invariance ambition. `01-act-core/OUTLINE.md:7`, `01-act-core/src/composition-closure.md:89`, `:119`, `:159`, `:191`.
> 5. **Medium**: The "graph structure uniqueness" derivation does not yet establish uniqueness in the strong sense. Its key step admits that P3 only gives "some local neighborhood," not parents specifically, and the Working Notes still say the P3→Markov implication is plausible but not proved because other sparse factorizations may also satisfy the locality requirement. Acyclicity looks genuinely solid; DAG+Markov still looks like the best-motivated representation choice, not a forced theorem. `01-act-core/src/graph-structure-uniqueness.md:69`, `:81`, `:105`, `:191`, `:203`.
> 6. **Medium**: The central scalar tempo variable is explicitly optimistic whenever channels are correlated or adaptation is anisotropic. The docs say scalar tempo overcounts effective correction capacity and can overestimate margins by 72% in anisotropic systems; since tempo feeds persistence, adversarial advantage, and team persistence, that optimism propagates into the theory's headline quantitative claims unless the vector/per-dimension form is used. `01-act-core/src/adaptive-tempo.md:44`, `:50`, `01-act-core/src/persistence-condition.md:118`.
>
> Overall Read
> The strongest part of `01-act-core` is Section I. The adaptive-systems layer has a real backbone: recursive update, gain, mismatch, persistence, and the sector-condition machinery are comparatively coherent, and the docs are unusually honest about epistemic status and scope boundaries.
>
> The weak point is the lift from adaptive systems to purposeful, strategic, and composite agents. Once the theory moves into Section II and III, the exact results increasingly depend on modularity assumptions, local continuation conventions, independence surrogates, or chosen admissibility constraints. That does not make the project bad; it means the current core is best read as a strong adaptive-systems theory plus a promising but still unstable agentic extension. I reviewed the `01-act-core` documents themselves; I did not independently verify the referenced `msc/` spike notes they cite for support.
>
> Highest-Value Repairs
>
> 1. Move the coupled Class 2 formulation into the core rather than leaving modern LLM-like agents as an out-of-scope appendix to `03-logogenic-agents/`.
> 2. Replace the default one-step diagnostics with a receding-horizon or Bellman-consistent variant, or explicitly demote the current 2×2 table from "diagnostic core" to "local heuristic."
> 3. Make correlated failure first-class in the strategy layer instead of a caveat on top of an independence model.
> 4. Either finish the P3→Markov proof or reframe `graph-structure-uniqueness` as structural motivation rather than uniqueness.
> 5. Close Section III with a purposeful multi-agent worked example that actually exercises $G_c$, strategy, communication, and the bridge lemma together.

### Joseph's response (the "no shortcuts" rule)

> Do your two actionable items, but we also need to do (from highest-value 'repairs'): #2, #4 (actually finish the proof-- not the lazy reframing/demotion that was done previously), and #3. There is no "this must be done quickly" constraint on this project-- I'm not sure why there are any shortcuts being taken. Codex's feedback should neither be disregarded as too pedantic, nor should it be taken at face value. I expect you to exercise judgement about the items-- but when you do, err on the side of the big picture and what is truly going to give the project the most value. Note, I did not say "value per ___" like there is some sort of implicit resource constraint or effort constraint.

This is one of the canonical statements of the "strengthen before softening" / "false constraints" working convention now in CLAUDE.md.

### Second 04-06 pass — six items including OUTLINE dependency violations (`e39166b4` line 1123, ts 2026-04-06T17:14:06Z)

> Excellent work. What are your thoughts on this fresh set of feedback from Codex? (it includes some repeats):
>
>   - The theory's exact Section II architecture excludes the most important contemporary agent class: merged LLM-style agents. The outline states that Section II's exact results apply only to Class 1 modular agents and that transformer-based LLMs are Class 2 and outside exact scope, with their treatment deferred to `03-logogenic-agents/`: `01-act-core/OUTLINE.md:61`, `:65`. The core mechanism behind that restriction is `directed-separation`, which explicitly says fully merged architectures fail the separation by construction and calls out LLMs as goal-conditioned in practice: `01-act-core/src/directed-separation.md:53`, `:74`, `:85`. If ACT is meant to be the core theory of modern agentic systems, this is the central limitation.
>   - The strategy-revision loop is not yet proven at the level of granularity the cascade relies on. `orient-cascade` says step 4 depends on $\delta_{\text{strategic}}$, then immediately notes that this quantity is only discussion-grade and that its persistence remains open: `01-act-core/src/orient-cascade.md:35`, `:36`, `:60`. `strategic-calibration` confirms that per-edge residuals require hard credit-assignment and execution-fidelity assumptions: `01-act-core/src/strategic-calibration.md:38`, `:56`. `credit-assignment-boundary` then narrows the formal guarantee to plan-level error $\delta_s$, not the edge-localized signal the cascade wants for actual strategy repair: `01-act-core/src/credit-assignment-boundary.md:51`, `:55`. In practice, the theory can robustly say "the strategy is bad" before it can robustly say "this edge is why."
>   - Section III is still a research program, not yet a closed part of the core. The outline itself says the composition bridge requires "a contraction assumption beyond the stated admissibility constraints" `01-act-core/OUTLINE.md:7`, and every Section III entry is still marked draft `01-act-core/OUTLINE.md:112`, `:126`. `composition-closure` repeats the same issue directly: the bridge lemma needs contraction of the full update map, and that contraction is "an additional assumption beyond (A4), not a consequence of it" `01-act-core/src/composition-closure.md:119`, `:121`, `:160`. That means composition-consistency is philosophically central, but mathematically not yet secured.
>   - The "canonical outline" is not currently a valid dependency-respecting linearization, despite presenting itself that way `01-act-core/OUTLINE.md:5`. A concrete example: `value-object` depends on `directed-separation` in frontmatter `01-act-core/src/value-object.md:8`, but the outline lists `value-object` ten rows before `directed-separation` `01-act-core/OUTLINE.md:74`, `:84`. The same problem appears with `team-persistence` depending on `communication-gain` `01-act-core/src/team-persistence.md:8` while being listed earlier `01-act-core/OUTLINE.md:119`, `:121`, and with `adversarial-tempo-advantage` depending on `adversarial-destabilization` `01-act-core/src/adversarial-tempo-advantage.md:8` while being listed earlier `01-act-core/OUTLINE.md:120`, `:122`. I found 14 such ordering violations. This is editorial, but it matters in a theory organized as a claim DAG.
>   - The default Section II diagnostic is weaker than it first appears because the canonical convention is local by default. `value-object` makes C1 one-step improvement the default `01-act-core/src/value-object.md:42`, `:48`, and both `satisfaction-gap` and `control-regret` say their default readings are local rather than global `01-act-core/src/satisfaction-gap.md:13`, `01-act-core/src/control-regret.md:13`. `orient-cascade` is careful about this and says the inferential force scales with C1/C2/C3 `01-act-core/src/orient-cascade.md:48`, `:56`. The practical consequence is that the theory's flagship 2x2 table is best read as a local triage tool unless the author explicitly promotes the analysis to C2 or C3.
>   - A smaller but concrete inconsistency appears in `team-persistence`: the segment correctly distinguishes communication-improved tempo from action-based disturbance reduction `01-act-core/src/team-persistence.md:41`, `:43`, then later says lever 2 is to increase cooperative coupling via "faster communication channels" `01-act-core/src/team-persistence.md:68`. That re-blurs the very mechanism split the segment just established.
>
> Assessment
> The strongest part of `01-act-core/` is Section I. The chain from recursive update to gain, tempo, sector-bounded correction, and persistence is coherent, honestly scoped, and materially stronger than the rest of the component `01-act-core/OUTLINE.md:24`, `:50`. The best contributions in the whole directory are the persistence machinery, the satisfaction-gap/control-regret split, the derivation of strategy acyclicity from temporal ordering, and the regime-sensitive adversarial exponents. Those feel like real theory, not just vocabulary.
>
> The overall maturity is uneven. By frontmatter count, Section I is relatively solid, Section II is mostly draft with a few strong diagnostics, and Section III is entirely draft. So the right reading today is: ACT is already a credible adaptive-systems theory, it has a promising purposeful-agent extension, and it has an interesting but still conditional composition program. It is not yet a fully closed theory of general agentic systems, and it is especially not yet a closed theory of LLM-native agent systems.

### Third pass — Two-batch full audit (`bd447ff0` line 121, ts 2026-04-06T20:45:54Z)

> Here is some additional feedback from Codex. Would you read it carefully, do any additional verification of your own (not via agents) on the new things and your previous items, find anything else, and then deliver a new synthesized and complete (as far as you can) analysis in `msc/analysis-2026-04-06.md`?
>
> Current-state audit only. I did not import prior baselines, and I did not count issues that are already plainly owned unless later framing still outruns the caveat.
>
> Batch 1
>
> 1. **Causal sufficiency is still framed too optimistically in the graph-uniqueness derivation.**
>    Problematic passage: `01-act-core/src/graph-structure-uniqueness.md:95` says causal sufficiency is "a reasonable assumption" for agent-constructed strategies.
>    Strongest counterevidence in src: `01-act-core/src/strategy-dag.md:78` calls causal insufficiency "the dominant case" in complex settings, and `01-act-core/src/strategy-dag.md:109` says the default in complex environments should be L1, not L0.
>    Assessment: still real. The proof can remain conditional on causal sufficiency, but the current motivation in the derivation understates how exceptional that assumption is in the domains the surrounding theory most cares about.
>    Confidence: high.
>    MSC context not yet integrated enough: `msc/spike-L1-worked-example.md:303` shows even L1 repair is not "just add a node"; correct common-cause placement is a design principle.
> 2. **Observable intermediates are still treated as a necessity, but the repo's own later machinery only requires identifiable aggregates.**
>    Problematic passage: `01-act-core/src/graph-structure-uniqueness.md:55` says the strategy representation "must have internal checkpoints."
>    Strongest counterevidence in src: `01-act-core/src/strategy-persistence-schema.md:47` explicitly recovers persistence for an unobservable intermediate by plan-level tracking, and `01-act-core/src/observability-dominance.md:51` says partial observability forces plan-level aggregation rather than invalidating the strategy altogether.
>    Assessment: still real. Observability is clearly crucial for localized revision and strong diagnostics, but the theory as now written no longer supports it as a necessary premise for strategy representation full stop.
>    Confidence: high.
>    MSC context not yet integrated enough: `msc/spike-credit-assignment-boundaries.md:90`, `:139` make the stronger replacement principle explicit: use the largest identifiable aggregate when intermediates are unobservable.
> 3. **Loop-based "interventional access" still over-identifies acting under a policy with clean per-action do identification.**
>    Problematic passage: `01-act-core/src/loop-interventional-access.md:22` says executing $a_t$ makes the pair a "genuine intervention."
>    Strongest counterevidence in src: `01-act-core/src/edge-update-causal-validity.md:32` says selection bias can make $P(j \mid \text{chose to execute } i) \neq P(j \mid do(i))$, and `01-act-core/src/edge-update-causal-validity.md:26` makes clean extraction depend on coverage, confounding, delay, and partial observability.
>    Assessment: still real. The repo clearly knows the identification problem, but the front-loaded wording still collapses "data produced by acting" into "per-action interventional data" more strongly than the later regime analysis allows.
>    Confidence: high.
>    MSC context not yet integrated enough: `msc/spike-edge-semantics-resolution.md:64` recommends the cleaner semantic move: treat edge quantities as working causal-efficacy beliefs whose interventional warrant varies by regime.
> 4. **The orient cascade still centers step 4 on $\delta_{\text{strategic}}$, even though the proved, credit-assignment-free quantity is $\delta_s$.**
>    Problematic passage: `01-act-core/src/orient-cascade.md:35` says step 4 uses $\delta_{\text{strategic}}$ as the "operational diagnostic."
>    Strongest counterevidence in src: `01-act-core/src/strategic-calibration.md:48` says $\delta_s$ is the proven persistence target while $\delta_{\text{strategic}}$ remains open, and `01-act-core/src/credit-assignment-boundary.md:114` says ACT's formal guarantees require only Level 0 plan-level tracking.
>    Assessment: still real. The caveat is present, but the actionable control loop still points first to the unproved quantity instead of making $\delta_s$ the default operational signal and $\delta_{\text{strategic}}$ the optional localization layer.
>    Confidence: high.
>    MSC context not yet integrated enough: `msc/spike-credit-assignment-boundaries.md:383` through `:396` states the intended hierarchy very cleanly: persistence is credit-assignment-free; calibration is not.
>
> Batch 2
>
> 5. **Objective revision is still operationalized too early relative to the repo's own $\Pi/N_h$/convention caveats.**
>    Problematic passage: `01-act-core/src/orient-cascade.md:33` sends the capability-limit quadrant onward, and `01-act-core/src/orient-cascade.md:38` says to revise $O_t$ if $\delta_{\text{sat}}$ persists across $\Sigma_t$ revisions.
>    Strongest counterevidence in src: `01-act-core/src/satisfaction-gap.md:32` says positive $\delta_{\text{sat}}$ can reflect wrong $M_t$, narrow $\Pi$, or short $N_h$, and `01-act-core/src/value-object.md:88`, `:90` say C1 only establishes "locally stuck," with C2 recommended where multi-step recovery is common.
>    Assessment: still real. The convention hierarchy is discussed, but it is not yet built into the cascade as a required escalation before objective revision.
>    Confidence: medium-high.
>    MSC context not yet integrated enough: `msc/spike-v3-purposeful-agent.md:444` already states the stronger formulation: check $M_t$, $\Pi$, and $N_h$ before revising $O_t$.
> 6. **Composition closure still slides from a conditional bridge lemma to a stronger claim than the current derivation supports.**
>    Problematic passage: `01-act-core/src/composition-closure.md:171` says A4 "ensures the macro-description tracks micro-reality" and that a structurally persistent ACT agent remains a faithful representation of its constituents.
>    Strongest counterevidence in src: `01-act-core/src/composition-closure.md:161` explicitly says the bridge lemma needs an extra contraction assumption beyond A4, and `01-act-core/OUTLINE.md:7` repeats that caveat at the section level.
>    Assessment: still real. The section is honest in its formal statement, but the later discussion slides back into a stronger equivalence than the segment has actually earned.
>    Confidence: high.
>    MSC context not yet integrated enough: `msc/working-composition-admissibility.md:175` argues the honest stance is to keep Section III explicitly conditional, and `msc/spike-composition-bridge-2agent.md:209` keeps the bridge lemma at sketch level until the projection conditions are tightened.

### 04-07 re-check — same Codex agent reviews progress (`bd447ff0` line 492, ts 2026-04-07T21:57:11Z)

> Well done. I asked the same Codex agent to have a look again and see how his specific concerns look now. His response:
>
>   The biggest improvements are in places where the text now preempts the obvious objection instead of answering it later.
>
>   - Loop-based Level 2 access is much better framed now. `01-act-core/src/loop-interventional-access.md:20` now says the loop generates "intervention-produced data," and `01-act-core/src/loop-interventional-access.md:22` explicitly distinguishes "action-generated data" from "cleanly identified do-estimates." That was the core pedagogical fix I wanted. I would not still count this as a top finding.
>   - The orient cascade is materially stronger. `01-act-core/src/orient-cascade.md:37` now makes $\delta_s$ the default plan-level signal, `01-act-core/src/orient-cascade.md:39` demotes $\delta_{\text{strategic}}$ to optional edge-level localization, and `01-act-core/src/orient-cascade.md:43` through `:53` now force escalation through $M_t$, $\Pi$, and convention/horizon checks before $O_t$ revision. That closes two of the prior six almost completely.
>   - Composition closure is more disciplined than before. `01-act-core/src/composition-closure.md:171` now says the sector condition does double duty only conditionally, and `01-act-core/src/composition-closure.md:198` incorporates a new characterization of the extra contraction assumption with a tiered picture of where it is proved. I would downgrade this from a high-priority narrative overclaim to a narrower integration issue: the new contraction classification should probably migrate from Working Notes into the main Epistemic Status or Formal Expression.
>
>   Two areas improved a lot, but still have residual inconsistency.
>
>   - Causal sufficiency framing is much improved in `graph-structure-uniqueness`, but not fully harmonized across src. `01-act-core/src/graph-structure-uniqueness.md:97` now says causal sufficiency is a "modeling ideal, not a typical condition," which is exactly the correction I was looking for. But `01-act-core/src/strategy-dag.md:137` still says "for agent-constructed strategies this is a reasonable assumption," even though `01-act-core/src/strategy-dag.md:139` immediately says correlated failure is the dominant case. So the repo now has the right view, but one older sentence is still lagging behind it.
>   - Observable intermediates are now correctly narrowed, but the file header still overstates their role. `01-act-core/src/graph-structure-uniqueness.md:55` through `:59` now says observability supports strong diagnostics rather than representation or persistence per se, which is a substantive fix. But the top summary at `01-act-core/src/graph-structure-uniqueness.md:15` still says four postulates, including observable intermediates, "derive" the representation. So the body has moved further than the framing sentence.
>
>   A few lower-priority items show little or no delta.
>
>   - The broader agency-scope vs learning-agent-scope seam is still there. `01-act-core/src/scope-condition.md:48` still includes thermostats and controlled Kalman systems in agency scope, while `01-act-core/src/causal-hierarchy-requirement.md:30` still narrows the Level-2-learning story to agents that acquire or refine causal knowledge online. I still see that as a scope-labeling issue rather than a major defect, but it has not moved much.
>   - The convention hierarchy is now used better pedagogically, but its proof burden is unchanged. `01-act-core/src/value-object.md:66` through `:70` still carry a lot of downstream weight on a fairly compressed proof sketch. I would not elevate that unless you want a fresh formal pass on the monotonicity argument itself.
>
>   Net judgment: the delta is good. If I were re-ranking today, I would remove the loop-access and orient-cascade items from the highest-priority list, downgrade composition closure, and keep only two of the earlier six as still materially standing in current src:
>
>   - the remaining causal-sufficiency mixed messaging across `01-act-core/src/graph-structure-uniqueness.md` and `01-act-core/src/strategy-dag.md`
>   - the stale top-level framing of observable intermediates in `01-act-core/src/graph-structure-uniqueness.md:15`
