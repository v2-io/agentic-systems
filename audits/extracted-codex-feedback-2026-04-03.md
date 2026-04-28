# Extracted Codex Feedback — 2026-04-03

**Source model:** OpenAI Codex (two passes)
**Date:** 2026-04-03
**Session UUIDs:** `e39166b4-9d21-4184-9d9d-12e9e0b83972` (lines 207, 248, 303, 629), `b40b551e-f8ff-4c2c-94f1-f3213402c252` (line 38)
**Topic:** Strategy persistence δ_s vs δ_strategic confusion; value-object causal-validity smuggling; composition gateway prematurity; loop-Level-2 over-universalization; team-persistence double-counting cooperation benefits; predictive-sufficiency vs causal-identifiability collapse.

## Context

This day produced two notable Codex passes that materially shaped the project's epistemic discipline. The first (line 207) catalyzed Joseph's enduring rule that "Codex's open questions are reader-clarity gaps, not unanswered research" — visible in the immediate follow-up at line 303 and now memorialized in the project's working conventions. Line 629's pass was characteristic of the project's strengthen-vs-soften posture: Joseph instructed Claude not to take Codex's feedback at face value but also not to dismiss it as pedantic.

## Disposition

Findings here partly drove the next day's strengthening cycle. Items 1, 2, 5 from the first pass were directly addressed by the do(.) operator standardization, the directed-separation scope cleanup, and the strategy-persistence δ_s vs δ_strategic disambiguation. Many findings carried forward into the 2026-04-06 audit pass. The "Codex's open questions = reader clarity gaps" methodology landed in CLAUDE.md (now in the Working Conventions section).

## Verbatim feedback Joseph relayed

### First pass — five-finding strategy-persistence audit (`e39166b4` line 207, ts 2026-04-03T01:10:50Z)

> Perfect. Thank you. In the meantime, here are some notes from Codex if you wouldn't mind:
>
> • Findings
>
> 1. **High**: the central "strategy persistence" result is currently stated for the wrong mismatch object. The formal schema says persistence is about zeroing and bounding $\delta_{\text{strategic}}$ in the sense of strategic calibration (`01-act-core/src/strategy-persistence-schema.md:20`, `:28`), but the same file later says the thing actually proved is persistence of plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$, while persistence of $\delta_{\text{strategic}}$ remains open (`01-act-core/src/strategy-persistence-schema.md:48`, `:50`). That is not a cosmetic distinction: $\delta_s$ is a coarse plan-level surrogate, while $\delta_{\text{strategic}}$ is the edge-local value residual the orient cascade actually wants for revision. As written, Section II overclaims theorem coverage.
> 2. **High**: the proved Section II surrogate is not the "true plan success probability" in the domains the theory itself says matter most. The strategy DAG file explicitly says the AND/OR propagation assumes independent edge failures and that $\hat P_\Sigma$ systematically overestimates success, potentially severely, under correlated failures and adversarial/common-cause structure (`01-act-core/src/strategy-dag.md:94`, `:96`). But Proposition B.5 then defines $\Phi = P_\Sigma(\theta)$ as "the true plan success probability" and proves persistence for $\delta_s = \hat P_\Sigma - \Phi$ (`01-act-core/src/strategic-dynamics-derivation.md:288`, `:296`, `:299`). Under correlated failure, $P_\Sigma(\theta)$ is just the same misspecified independence model evaluated at true edge rates; it is not actual plan success. So the persistence proof currently tracks calibration to the surrogate model, not to strategic reality.
> 3. **High**: Section III's composition chain is still open at its key bridge, so downstream composition laws are not yet consequences of the stated ACT machinery. The bridge lemma in composition closure explicitly adds an extra contraction assumption on the full macro update map beyond A4 (`01-act-core/src/composition-closure.md:119`, `:121`, `:129`, `:161`). `tempo-composition` then builds the subadditive tempo inequality and the Brooks's-Law-style overhead story directly on that bridge (`01-act-core/src/tempo-composition.md:27`, `:38`, `:52`). The result is a strong research direction, but not a closed derivation. Right now the composition story should be presented as "ACT plus an additional contraction premise," not as scale invariance already discharged by the core.
> 4. **Medium**: the value object notation hides objective dependence and then states a false independence claim. The definition is explicitly "given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$" (`01-act-core/src/value-object.md:19`, `:25`), but the prose then says $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ "depends on $M_t$ alone" (`01-act-core/src/value-object.md:35`). That cannot be right as written, because $V_{O_t}$ remains inside the expectation, and the same file later makes policy optimization and exploration weighting depend on $O_t$ (`01-act-core/src/value-object.md:60`, `:62`). The likely intended claim is narrower: once $O_t$ is held fixed as an external parameter, the remaining state dependence is via $M_t$, not all of $G_t$. The notation should say that explicitly.
> 5. **Medium**: the "graph structure uniqueness" section still overstates what has been shown. The crucial P3 step only establishes that some local neighborhood must suffice for revision (`01-act-core/src/graph-structure-uniqueness.md:81`, `:85`), then elevates parents from "natural neighborhood" to "therefore the local Markov property" (`01-act-core/src/graph-structure-uniqueness.md:87`, `:93`, `:117`). The same section also concedes that factor-graph-style local computation exists (`01-act-core/src/graph-structure-uniqueness.md:105`), and `strategy-dag` itself says the P3→Markov step is still not theorem-strength (`01-act-core/src/strategy-dag.md:100`, `:102`). The theory has a strong argument for DAGs, exact acyclicity, and a very plausible causal-BN preference. It does not yet have a uniqueness theorem.
>
> Open Questions
>
> - Is the canonical strategic mismatch supposed to be $\delta_s$ or $\delta_{\text{strategic}}$? The current documents switch between them at the theorem boundary.
> - Is $\hat P_\Sigma$ intended as a calibrated probability or explicitly as a tractable heuristic? If the latter, B.5 should stop calling $P_\Sigma(\theta)$ the true success probability.
> - Is contraction of the full macro update map something ACT will derive from A4, or should it become an explicit admissibility assumption in Section III?
> - Are satisfaction gap and control regret meant to be intrinsic architecture diagnostics, or diagnostics relative to a chosen continuation convention and scalarization convention? The docs currently oscillate.
>
> Overall Assessment
> Section I is the strongest part of the theory. The recursive-update framing, gain-to-sector bridge, Lyapunov persistence machinery, and discrete-time closure form a coherent mathematical core, with the documents generally honest about what is exact versus heuristic. Section II has a compelling architecture and several genuinely useful diagnostics, but its current formal center is narrower than the prose sometimes suggests: exactness depends on directed separation, fixed scalar objectives, an explicit continuation convention, and surrogate plan quantities that break in correlated-failure regimes. Section III is promising, but still a research program rather than a finished theorem chain because the closure-to-trajectory bridge is not yet internal to ACT.

### Joseph's response (the rule-formation moment)

> Codex isn't going to look in the TODO-- if any of Codex's open questions have a chance of being asked by others, determine how we can preempt them or answer them in the segments (or README / OUTLINEs) themselves.

Followed minutes later by:

> In fact-- if you could add to your memory or CLAUDE.md -- when codex presents "open questions" -- treat them as "Questions a reasonable reader might have even after having read everything," and thus implies areas to improve clarity in form, sequence, or notation usually assuming the answer is known or can be easily decided...

This rule is now in the project's Working Conventions section.

### Second pass — Section II diagnostics audit (`e39166b4` line 629, ts 2026-04-03T14:57:22Z)

> Excellent. First, let's address these additional codex items:
>
> • Findings
>
> 1. Section II's core diagnostics are presented as full goal-feasibility and policy-optimality tests, but under ACT's own default continuation convention they collapse to one-step-improvement quantities. That is explicitly admitted in the definitions, yet the surrounding prose and the orient cascade still use them to distinguish "infeasible goal" from "bad strategy" and to justify objective revision. Without Bellman-style or receding-horizon semantics, those inferences are too strong: a multi-step recoverable objective can look infeasible, and a revisable policy can look near-optimal, simply because continuation is frozen. Refs: `01-act-core/src/value-object.md:41`, `01-act-core/src/satisfaction-gap.md:19`, `:48`, `01-act-core/src/control-regret.md:19`, `01-act-core/src/orient-cascade.md:25`.
> 2. `value-object.md` smuggles a nontrivial causal-validity theorem into a segment labeled `type: definition`, `status: exact`, while omitting the very dependency that makes the theorem conditional. The file itself says causal validity depends on directed separation and degrades for Class 2 agents, and the outline says Section II exactness only holds for Class 1 modular agents. That means the local segment label overstates what has actually been established, and downstream readers can easily miss the architectural scope restriction. Refs: `01-act-core/OUTLINE.md:7`, `01-act-core/src/value-object.md:29`, `:35`, `01-act-core/src/directed-separation.md:72`.
> 3. The actionable strategy-revision loop is not grounded in the same mismatch variable that the strategic persistence math actually proves. The theory proves persistence for plan-confidence error $\delta_s$, but the orient cascade operationalizes revision through $\delta_{\text{strategic}}$, which the docs themselves mark discussion-grade, credit-assignment-dependent, and still open. That leaves the "what should the agent do next?" part of Section II resting on a different and weaker object than the one the mathematics currently supports. Refs: `01-act-core/src/strategic-calibration.md:46`, `:52`, `01-act-core/src/strategy-persistence-schema.md:32`, `:55`, `01-act-core/src/orient-cascade.md:35`, `01-act-core/src/credit-assignment-boundary.md:53`.
> 4. The composition gateway claim is ahead of its proof burden. `composition-consistency.md` presents $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ as a practical sufficient test and says most real groups easily satisfy it, but `composition-closure.md` later admits the key bridge lemma still needs an independent contraction assumption not derived from the stated admissibility constraints. The outline is honest about this; the segment-level prose is not equally restrained. As written, Section III reads more operationally settled than it currently is. Refs: `01-act-core/src/composition-consistency.md:24`, `:32`, `:42`, `01-act-core/src/composition-closure.md:169`, `:196`, `01-act-core/OUTLINE.md:7`.
> 5. `loop-interventional-access.md` over-universalizes Level 2 access and contradicts the theory's own scope split. `scope-condition.md` is explicit that passive observers and nominal agents remain inside adaptive scope but outside agency scope because they lack meaningful action contrasts. The working note in `loop-interventional-access.md` then says all agents within ACT's scope have access to interventional data. That is false under the framework's own definitions and muddies the clean Section I vs Section II boundary. Refs: `01-act-core/src/scope-condition.md:20`, `:31`, `:55`, `01-act-core/src/loop-interventional-access.md:34`, `:53`.
>
> Assessment
> The strongest part of `01-act-core/` is Section I. The persistence stack is substantially tighter than the rest of the project: mismatch, gain, sector-condition stability, structural-vs-task persistence, and structural adaptation all form a coherent chain, and the outline is unusually honest about which pieces are exact, conditional, or open.
>
> The main weakness is not "bad ideas," it is epistemic leakage across boundaries. The outline correctly says Section II is only exact for modular Class 1 agents and Section III still depends on unproven admissibility/bridge assumptions, but several individual segment files still speak as if the stronger generalization already holds. That creates avoidable confusion about what is theorem, what is architecture-contingent, and what is still a research program.
>
> I did not make edits. This was a theory review only; I read the framing docs, the Section I spine, the key Section II/III segments, and ran a metadata/dependency consistency pass over `01-act-core/src`.
>
> Open Questions
>
> - If $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are meant to be local one-step diagnostics rather than global feasibility/optimality diagnostics, the project should say that in the titles, summaries, and orient-cascade prose, not only in the epistemic-status caveats.
> - If $Q_O$ is meant to stay a pure definition, separate the causal-validity discussion into its own conditional segment depending on `#directed-separation`; that would remove most of the current scope ambiguity.
> - If Section III is intentionally postulatory for now, `composition-consistency.md` should be rewritten to present $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ as an intuition or conjectural heuristic, not as an already-usable sufficiency test with broad empirical examples.

### Codex pass on team-persistence + predictive-vs-causal collapse (`b40b551e` ts 2026-04-02T23:48:49Z & 2026-04-03T00:16:37Z)

> I've got another agent working on some of the open problems. In the meantime, could I ask you to fix some things? Codex identified the following:
>
> • Findings
>
> 1. **High**: Section III appears to double-count the benefit of cooperation. `team-persistence.md:23` adds allied messages to an agent's corrective capacity as extra tempo, then `team-persistence.md:41` says those same cooperative communication events also subtract from disturbance by "effectively canceling" it. Unless the state equations explicitly separate "faster correction" from "reduced exogenous disturbance" as different physical mechanisms, the current formulation gives one message two benefits. That makes the persistence threshold in `team-persistence.md:55` systematically optimistic.
> 2. **High**: The composition bridge is presented as a derived result, but the file itself still treats its key step as an unproved extra assumption. The bridge lemma in `composition-closure.md` requires contraction of the full update map, declared "additional, beyond A4." (Continued.)

> Here's a new set of feedback from codex if you wouldn't mind addressing the issues:
>
> • Findings
>
> 1. **High**: ACT currently treats predictive sufficiency as if it implied causal identifiability. `01-act-core/src/value-object.md:27` says $S(M_t) = 1$ makes interventional and conditional expectations coincide because $M_t$ screens off confounders, but `01-act-core/src/model-sufficiency.md:19` defines $S$ only as retained predictive information, and `01-act-core/src/causal-hierarchy-requirement.md:24` separately insists Level 2 cannot in general be recovered from Level 1. Unless $S$ is upgraded to a causal-state notion, this collapses a distinction the theory otherwise treats as load-bearing.
> 2. **High**: Section I's scope boundary contradicts itself on passive observers. `01-act-core/src/scope-condition.md:29` explicitly includes passive Kalman filters and passive Bayesian learners in adaptive scope, while `01-act-core/src/causal-structure.md:35` says zero-coupling passive estimation is outside ACT's scope and that ACT is "a theory of agency, not passive estimation." That is not a minor wording issue; it changes what Section I is actually about.
> 3. **High**: The verified strategic dynamics do not instantiate the published edge-gain formula. `01-act-core/src/edge-update-via-gain.md:26` defines $\eta_{\text{edge}}$ as $U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$ with Beta posterior variance as $U_{\text{edge}}$, but `01-act-core/src/strategic-dynamics-derivation.md:28` and `:30` use exact Beta-Bernoulli gain $1/(n+1)$ and say it matches the earlier form. As written, that equivalence is missing and generally false without an additional mapping for $U_{\text{obs}}$.
> 4. **Medium-high**: The default strategy-revision rule is pointed at the wrong object in the regime the theory itself calls dominant. `01-act-core/src/strategy-dag.md:64` and `:90` say $\hat P_\Sigma$ systematically overestimates success under correlated failures, and `01-act-core/src/credit-assignment-boundary.md:37` then uses $y_G - \hat P_\Sigma$ as the default residual for edge updates. `01-act-core/src/credit-assignment-boundary.md:47` admits this blames individual edges for omitted correlation structure, which means the default learner will often revise edge weights when the real fix is adding shared-cause structure.
> 5. **Medium**: The "exact" Section II core only holds for a narrower architecture class than the prose suggests. `01-act-core/OUTLINE.md:7` describes an exact diagnostic core, but `01-act-core/src/directed-separation.md:53`, `:73`, `:85` explicitly classify transformer/LLM-style agents as failing directed separation by construction, while `01-act-core/src/orient-cascade.md:16` presents the cascade ordering as forced. For the main modern agent class, the cascade is only an approximation.
> 6. **Medium**: The core diagnostics are definitionally exact but operationally underdetermined unless policy class, horizon, and continuation convention are fixed everywhere. `01-act-core/src/value-object.md:31` says $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$ change with continuation convention, while `01-act-core/src/satisfaction-gap.md:19` and `01-act-core/src/control-regret.md:19` present them as clean diagnostics. That makes the diagnostic core fragile to bookkeeping choices unless the repo enforces one convention much more aggressively than it currently does.
> 7. **Medium**: Section III's composition story is still an agenda rather than a closed theorem chain. `01-act-core/src/composition-consistency.md:12` states cross-level compatibility as a postulate, but `01-act-core/src/composition-closure.md:121` and `:161` show the bridge from closure defect to bounded macro-error needs an extra contraction assumption not implied by the admissibility axioms. `01-act-core/src/team-persistence.md:85` then builds on modeling choices that are still explicitly conditional.
>
> Open Questions
>
> - Is ACT meant to be a theory of adaptive systems under uncertainty broadly, or only of agents with at least weak intervention capability? The passive-observer contradiction needs a single canonical answer.
> - Do you want $S(M_t)$ to remain purely predictive, or do you want a stronger causal-state notion that can legitimately support do-style claims? Right now those two roles are being conflated.
> - Is Section II supposed to apply directly to current LLM agents, or only to modularized agent systems wrapped around them? The present docs point in both directions.
> - Do you want the strategy layer to default to independent-edge DAGs, or should shared-cause/correlated-failure structure be part of the core representation rather than treated as a caveat?
>
> Overall Read
> Section I is the strongest part of the theory once the scope contradiction is resolved. Section II has a useful architecture, but its cleanest results depend on stronger separability and causal assumptions than the top-level framing currently advertises. Section III is promising, but it is still mostly a conditional research program built on admissibility choices and extra bridge assumptions rather than a closed formal extension of Section I.
