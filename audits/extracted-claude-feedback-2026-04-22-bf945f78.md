# Extracted Claude Feedback — 2026-04-22 morning Opus audit (bf945f78)

**Source model:** Claude Opus 4.7 (1M context) — `claude-opus-4-7`
**Date:** 2026-04-22
**Session UUID:** `bf945f78-535c-4313-b8cf-18b19355a2cd`
**Record UUID:** `4307380e-3377-48f1-a139-521e682f5df4` (line 178, ts `2026-04-22T15:11:46.608Z`)
**Triggering prompt:** Joseph's standard de novo audit prompt (problematic passage / counterevidence / status / confidence; burden of proof on auditor; bigger-picture insights afterward).
**Audit length:** 22,084 chars.

## Context

This is the **first** of three Claude-as-auditor sessions Joseph ran on 2026-04-22 with the same de novo audit prompt. It ran at 15:00 UTC, **before** the strengthening cycle's commits had landed. The 5 findings here are the "Opus" batch in `audits/pending-findings-2026-04-22.md` (cited as "Opus F1" through "Opus F5" in the findings index).

The five findings:

1. `#causal-insufficiency-detection` — the ±ρ residual is asserted as universal but vanishes under rational on-policy execution (medium-high confidence).
2. (C-iii) mutual-benefit composites do not supply the decomposable G_c that downstream A1 requires.
3. The Section II preamble's Class-2 framing understates what `#section-ii-survival` actually establishes.
4. `#form-information-bottleneck` marked `discussion-grade, deps-verified` conflicts with the unification role it carries.
5. Orient-cascade step 4c's ascension diagnostic requires convergence that may never happen in the environments where L1 is most needed.

The "Bigger picture" sections (1–7) cover sector-persistence template as the real theory; four compressions wanting to be one hierarchy; approximation-tiering as parameter not enumeration; DAG-Boolean vs reality-continuous; orient cascade as itself an adaptive cycle; identity + non-forkable trajectory as hidden load-bearing result; what's missing.

## Disposition

**The session ended with the audit** — no follow-up user messages. The five findings were extracted in summary form into `audits/pending-findings-2026-04-22.md` as "Opus F1–F5" with severity tags and subsumption-by-architectural-proposal mappings. Subsequent strengthening commits (`14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`) resolved Findings 1 (no-go theorem strengthening, covariance test promoted to primary), 3 (subsumed by G-BP2 V-medium), and partially 5 (step 4c reframed as the unique broadly-available diagnostic given the no-go).

The full reasoning trail of each finding (including the strongest-counterevidence-elsewhere passages and the "still real vs. already caveated" reconciliation) is **not** preserved in `pending-findings-2026-04-22.md` — only the bullet-form summary. The bigger-picture sections (1–7) are not preserved verbatim anywhere; their substance partially informed `msc/architectural-proposals-2026-04-22.md` (specifically O-BP1 sector-persistence-template-as-real-theory, O-BP2 four-compressions-as-hierarchy, etc.) but the auditor's reasoning that produced those proposals is preserved here.

This extraction preserves the verbatim audit prose so the audit→architectural-proposal lineage is recoverable.

## Verbatim audit content

> I have read enough to stand behind specific claims. Below are the findings that meet the burden-of-proof test — each with the problematic passage and the strongest mitigating passage, and an honest read on whether the issue still stands.
>
> ---
>
> # De Novo Audit — Current State
>
> ## Finding 1 — `#causal-insufficiency-detection`: the ±ρ residual is asserted as universal but vanishes under rational on-policy execution
>
> **Problematic passage** (`01-aad-core/src/causal-insufficiency-detection.md` lines 21–33):
>
> > "After edge credences converge (p̂ₖ ≈ θₖ, low gain), the plan-confidence error δ_s ≈ 0… The **L0 residual** — the gap between the independence-model reference value and actual success — converges to: Φ^L0 − ȳ_G ⟶ { +ρ OR-heavy; −ρ AND-heavy }… **Detection criterion.** A persistently nonzero L0 residual after edge-credence convergence is a strong indicator of causal insufficiency."
>
> The three preconditions in that segment (marginal convergence, stationarity, no systematic update bias) do not gate for the substantive issue.
>
> **Strongest available counterevidence in `src/`**: none. `#orient-cascade` step 4c cites this segment's pairwise-sibling-covariance mechanism (which does survive — it requires off-policy sampling by construction). No segment contradicts the ±ρ claim.
>
> **Why the issue still stands**: a rational agent executing an AND/OR strategy short-circuits. Under OR, if A₁ succeeds A₂ is never executed; under AND, if A₁ fails A₂ is never executed. Learned credence for the second sibling therefore converges to a *conditional* probability, not the marginal. Plugging conditionals into the L0 formula recovers the true joint exactly, so Φ^L0 − ȳ_G → 0 under pure on-policy execution. The ±ρ bias appears only under off-policy/exploratory sampling. The "strong indicator" framing overclaims for any agent that executes its own strategy rationally.
>
> **Confidence: high.** The math is clean and structural; this is not a marginal objection.
>
> **msc/ has the repair but it is not integrated**: `msc/pending-findings-2026-04-22.md` already characterizes this exact issue and proposes the repair (elevate the covariance test to primary; demote the residual to an exploration-rate-gated secondary signal with ≈ ε·ρ scaling). That finding was logged 2026-04-22 after the promotion work and has not yet been absorbed into the segment text. The segment still asserts the ±ρ formula as if it held universally. The *theoretical* issue is captured; the *segment* still misleads a reader who doesn't know the pending-findings file exists.
>
> ---
>
> ## Finding 2 — Gap between (C-iii) mutual-benefit composites and the (A1) requirement of a decomposable G_c
>
> **Problematic passage 1** (`composition-scope-condition.md` lines 38–44):
>
> > "**(C-iii) Mutual-benefit alignment.** There exists a relevance variable Y such that the sub-agents' joint actions raise E[Y] above the non-cooperation baseline for each sub-agent… **Weakest route.** No explicit common objective, but interactions are positive-sum in some dimension."
>
> **Problematic passage 2** (`composition-closure.md` line 73–77):
>
> > "**(A1) AAD agent structure.** The macro-state decomposes as X_c = (M_c, G_c)."
>
> And lines 64–65:
>
> > "The closure-defect framework applies to sets that satisfy #composition-scope-condition — i.e., that form composites via at least one of the three alignment routes… Given scope-satisfaction, a set forms a *meaningful* composite agent…"
>
> **Strongest mitigating passage** (`composition-scope-condition.md` Epistemic Status and Working Notes):
>
> > "The three alternative routes are not exhaustive but cover the well-understood cases. The relationship between the routes (whether they partition or overlap) and whether there is a single underlying scalar that reduces them all is open."
>
> **Why the issue still stands**: the mitigating passage acknowledges the disjunction is open in principle, but does *not* address the specific structural gap: (C-iii) scope-satisfaction admits composites with no explicit O_c, while (A1) of the closure framework requires G_c = (O_c, Σ_c) as a state decomposition. For trading partners aligned only on a mutual-benefit Y, O_c cannot be naturally defined without strengthening the route — e.g., by positing O_c = "maximize E[Y]," which then collapses (C-iii) into (C-i). So either the three routes are not independently sufficient for the full closure framework, or the relationship between routes is not the honest disjunction currently advertised. The current text says both things in different places.
>
> **Confidence: medium.** Clear logical gap; I cannot rule out that a reasonable restriction of admissibility (A1) to "composites satisfying (C-i) or (C-ii)" would repair it, leaving (C-iii) admitted only to #multi-agent-scope. But that is not what the current text says.
>
> **msc/ status**: I did not find a msc document that closes this. `spike-agent-composition.md` and `spike-symbiogenic-composition.md` are the likely homes.
>
> ---
>
> ## Finding 3 — The Section II preamble's Class 2 framing understates what `#section-ii-survival` actually establishes
>
> **Problematic passage** (`01-aad-core/OUTLINE.md`, Section II preamble):
>
> > "**Class 2 (fully merged) agents** — including transformer-based LLMs where attention processes goals and observations together — fall outside Section II's exact scope because directed separation (#directed-separation) fails by construction. The coupled formulation these agents require is the subject of `03-logogenic-agents/`… This is the most significant scope restriction in the theory: the most important present-day agent class (LLM-based) requires work beyond Section II."
>
> **Strongest mitigating passage** (`03-logogenic-agents/src/section-ii-survival.md` §Scorecard and §Discussion):
>
> > "Exact: 15.5/24, Approximate: 5.5/24, Modified: 2/24, Fails: 1/24… Section II's *conceptual architecture* applies to Class 2 agents (16/24 exact survival is a claim about this), but Section II's *operational deployment* on Class 2 agents requires additional instrumentation…"
>
> Reinforced by `#observation-ambiguity-modulation`:
>
> > "A Class 2 agent (κ ≈ 1) operating in a domain with low observation ambiguity (𝒜 ≪ 1) has κ_eff ≈ 𝒜 ≪ 1… the Section II results classified as 'approximately surviving' become *good approximations* despite the agent being fully merged."
>
> **Why the issue still stands**: the preamble's "falls outside Section II's exact scope" and "requires work beyond Section II" are literally correct but read as if Section II is non-applicable to LLM agents. The survival analysis + ambiguity modulation together say the opposite: the bulk of Section II's statement-level architecture transfers, and in low-ambiguity domains the approximate results become quantitatively tight. The OUTLINE's framing is the first thing a reader sees; the nuanced picture lives three documents deep.
>
> **Confidence: medium-high.** This is a framing rather than a correctness issue, but it affects how a reader of the whole theory situates Class 2 agents — and given the project's emphasis on logogenic agents, that framing carries weight.
>
> **msc/ status**: `msc/spike-coupled-survival-analysis.md` contains the full 24-result classification. Its findings are absorbed into `section-ii-survival.md`. They have not been back-propagated to the Section II preamble.
>
> ---
>
> ## Finding 4 — `#information-bottleneck` marked `status: discussion-grade, stage: deps-verified` conflicts with the unification role it carries
>
> **Problematic passage** (`#information-bottleneck` frontmatter and Epistemic Status):
>
> > "status: discussion-grade… This is a *formulation* — it provides a principled framework for understanding compression trade-offs, not a claim about how actual agents compute their models."
>
> **Tension** (`#compression-operations` and `#composition-closure`):
>
> `#compression-operations` now treats IB as the *shared shape* of four AAD compression operations — a substantial unification role — and derives that composition-closure's (P1) is the Lagrangian-dual of IB. This derivation implicitly depends on IB being a rigorous rate-distortion statement, not merely discussion-grade.
>
> **Strongest mitigating passage** (`#compression-operations` Epistemic Status):
>
> > "The claim that the four compression operations share IB shape is *discussion-grade*… The (P1) as Lagrangian-dual of IB is *derived* — rate-distortion duality is standard (see §I.12–13 of Cover & Thomas) and the constraint-form ↔ Lagrangian-form equivalence is mechanical."
>
> **Why the issue only partially stands**: the segment is honest about what's derived and what isn't. But `#information-bottleneck` itself is labeled discussion-grade, while `#composition-operations` uses it as a *fixed point* for four different compression operations. This is consistent only because the duality invoked in compression-operations is external (Cover & Thomas), not internal to AAD. The labeling of `#information-bottleneck` as discussion-grade rather than "exact formulation (external theorem)" under-sells what the theory actually leans on.
>
> **Confidence: low-medium.** Editorial inconsistency more than substantive error.
>
> ---
>
> ## Finding 5 — Orient cascade step 4c's ascension diagnostic requires convergence that may never happen in the environments where L1 is most needed
>
> **Problematic passage** (`#orient-cascade` step 4c):
>
> > "If persistent δ_s ≈ 0 coincides with persistent negative plan-outcome residuals (y_G < P̂_Σ on average, after edge credences have converged), this is evidence that the DAG is causally insufficient and L0 calibration is converging to a biased target."
>
> **Strongest mitigating passage** (`#orient-cascade` Epistemic Status):
>
> > "What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding, and how long δ_s ≈ 0 must persist before 4c's signal is trusted."
>
> And `#strategy-dag`:
>
> > "The default assumption in complex environments should be L1, not L0."
>
> **Why the issue still partially stands**: convergence of δ_s ≈ 0 requires the per-edge credences to have stabilized, which presumes a stationary environment for long enough to wait out transient dynamics. The environments where latent common causes are most dominant (adversarial, organizational, multi-stakeholder) are often non-stationary — precisely where the ascension signal may never fire. The mitigating passage's "use L1 by default" is a good practical answer but breaks the "cascade driven by information dependency" framing: in those regimes, the agent should not operate at L0 at all, making 4c's trigger superfluous.
>
> Additionally, Finding 1 (the ±ρ residual not actually firing under on-policy execution) compounds this: even in stationary environments, the step 4c signal is weaker than the segment implies.
>
> **Confidence: medium.** Partially caveated; partially broken by Finding 1.
>
> ---
>
> ## Other places I looked and found the caveat load is adequate
>
> These are places I pushed hard on and concluded the theory is already honest enough to not constitute a finding:
>
> - **Directed-separation's κ_processing estimator**: the segment explicitly admits that behavioral estimation via processor-probing requires the reference interpreter to have κ > 0, and that κ is architectural-structural not a smooth knob. The ambiguity-modulation segment extends this cleanly.
> - **Causal sufficiency for the strategy DAG CMC proof**: `#graph-structure-uniqueness` explicitly narrows this to "sufficient, not necessary"; `#strategy-dag` and `#independence-audit` both openly flag that causal sufficiency is the exception not the rule in complex domains; the Correlation Hierarchy is the characterized remedy.
> - **Bridge lemma vs. sector condition strength**: `#composition-closure` names the incremental sector bound (DA2'-inc) as strictly stronger than the template's (T2); the Tier 1/2/3 taxonomy makes the conditionality visible.
> - **Forgetting prerequisite in strategy persistence**: explicitly promoted from heuristic to prerequisite in the segment, with the (1−λ) > ρ_Σ/R_Σ form stated.
> - **α–𝒯 relationship**: `#gain-sector-bridge` derives this for linear correction, gradient-on-convex, exponential-family; the "verified for all tested correction functions" claim in `#persistence-condition` is consistent with that derivation.
> - **Acyclicity of Σ_t**: derived from temporal ordering over finite horizon; the iteration objection is handled.
>
> ---
>
> # Bigger-Picture Synthesis
>
> Some intuitions that accumulate after a close read of the whole. I'm marking each by confidence, in the spirit of the epistemic ladder.
>
> ## 1. The sector-persistence template is the real theory; everything else is instantiation *(confidence: high)*
>
> `#sector-persistence-template` is already factored out. But the implications are larger than the segment credits. Reading AAD through this lens:
>
> - **Section I** is the template applied to epistemic mismatch δ with environmental disturbance rate ρ.
> - **Section II strategy persistence** is the template applied to plan-confidence error δ_s (or per-edge δ_c) with strategic disturbance ρ_Σ, under experience-discounted α_Σ.
> - **Adversarial destabilization** is the template with disturbance augmented by γ_A·𝒯_A.
> - **Team persistence** is the template with disturbance decomposed into env + adversarial − cooperative terms.
> - **Composition closure bridge** is the template applied to trajectory error e_m with closure-defect disturbance ε*·ν_c (plus the strong-monotonicity upgrade).
> - **Tempo composition** is the template with internal-plus-external effective disturbance.
>
> Six "results" collapse to *one* result + six different ways of accounting for effective disturbance. The distinctive content of each segment is the characterization of its ρ_eff; the persistence conclusion is mechanical. This is already stated in the template segment's Discussion but could become the organizing principle of the whole presentation: **AAD is the theory of how to decompose disturbance for bounded-correction dynamics at each scale.**
>
> This reframe would make `temporal-optimality` (TST's postulate) read as: "the scarce resource is correction capacity relative to effective disturbance; time is the metering unit." That elevates the postulate from "almost tautological" to "the normative statement of a structural fact from AAD."
>
> ## 2. The four compression operations want to be one compression hierarchy *(confidence: medium)*
>
> `#compression-operations` stops at U-medium: shared IB shape across M_t, Σ_t, shared intent, Λ. It explicitly refuses U-strong.
>
> But I think the U-medium stance undersells what's actually there. The four operations differ in *relevance variable* but share source (history) and structure (rate-distortion over a stochastic compressor). An ontology that makes this fundamental:
>
> > *An agent is a collection of compression maps over its causal history, each tuned to a different relevance variable: prediction (M_t), guidance (Σ_t), coordination (shared intent), abstraction (Λ).*
>
> Under this view, M_t vs. Σ_t is not two different *objects* but two different *projections* of the same source with different Y. This addresses a problem I noticed in Finding-adjacent territory: L1 augmentation asks Σ_t to absorb environmental common causes, which pushes it toward M_t. If both are compressions of the same history, there's no boundary to police — just different rate-distortion operating points for different decision purposes.
>
> This would also make Class 2 (LLM) agents *natural* rather than an awkward scope exit. An LLM's forward pass is a single compression producing all four projections simultaneously; modularity is a special case where the four projections are computed on disjoint sub-graphs. The TODO.md tier-C deferral "G_t as single object; (O_t, Σ_t) as a property" points in this direction.
>
> ## 3. The approximation-tiering pattern is hinting at a parameter, not an enumeration *(confidence: medium)*
>
> L0/L1/L2, C1/C2/C3, Tier 1/2/3 all share the shape. The segment names this and lists candidate future tierings. The *pattern* is: every tractable AAD result is a rate-distortion operating point, with monotonicity to finer resolutions and an ascension diagnostic.
>
> A cleaner formulation might treat the tier as a **parameter of the agent's operating regime**, not a discrete label. Under `#continuous-convention-hierarchy` (TODO tier-C deferral), N_r ∈ [1, ∞] unifies C1/C2/C3. The correlation hierarchy could similarly be indexed by "information retained about common causes" as a continuous quantity (0 at L0, 1 at L2). The contraction tier is already a structural property of the operator.
>
> If all three tierings were continuous-parameter families, the *shape* of the theory becomes: results are defined at a point in a 3D operating-regime space (convention × correlation × contraction), with monotonicity along each axis. This is closer to information geometry than to the current enumerative treatment.
>
> ## 4. The DAG is Boolean; reality is continuous *(confidence: medium)*
>
> The strategy DAG has AND/OR nodes and binary-success edges. `#and-or-scope` explicitly scopes this to binary outcomes. But most real strategic progress is continuous: "approach target," "reduce defect rate," "close the gap." Chess engines use continuous value estimates, not AND/OR on win/loss.
>
> A continuous extension: edges carry expected-progress rates; nodes aggregate progress fields; terminal satisfaction is a continuous threshold. The `status propagation` in the Boolean case is multiplicative; in the continuous case it's additive-convex or tropical-semiring depending on the combination rule. This is likely a substantial rewrite of the strategy layer, but it would dissolve the hacks currently needed for continuous-value objectives (the scope note in `#strategy-dag` about "setting an operational threshold" for continuous objectives).
>
> Related: the Correlation Hierarchy's L1 soft-facilitator case (L1' mixture form) is already a stretch of the Boolean machinery. A continuous formulation would handle soft facilitators natively as graded parent influences.
>
> ## 5. The orient cascade is itself an adaptive cycle *(confidence: medium-low)*
>
> Steps 1–5 of the cascade consume prior outputs, produce diagnostic signals, and trigger structural adaptation when the parameters don't close the gap. This is an adaptive cycle operating over the agent's *internal* state (diagnostics), nested inside the outer cycle operating over external state (reality).
>
> Deliberation in `#exploit-explore-deliberate` is described as "internal exploration in model-space." Put these together: the agent's reasoning process is a miniature AAD system whose environment is its own model-state. This is gestured at in several places but never formalized. A recursive formulation — "AAD applies at every level where a state variable has a correction function and bounded disturbance" — is already the spirit of `#composition-consistency`. Making the inner-cycle recursion explicit would unify deliberation, orient cascade, and composition.
>
> ## 6. Identity + non-forkable trajectory is the hidden load-bearing result *(confidence: low)*
>
> `#agent-identity` is currently discussion-grade and deliberately minimal. But it establishes something formally consequential: *sufficiency is defined relative to a singular causal trajectory*. A duplicated M_t is *not* sufficient for either copy's trajectory; merging divergent models is lossy; continuity is what gives the sufficient statistic its meaning.
>
> This is load-bearing for the logozoetic work. It may also be load-bearing for the rest of the theory in ways not currently made explicit — e.g., the reason Level 2 data from the feedback loop is interventional is precisely because the loop is a singular causal trajectory; replaying is not intervening. The identity argument could be promoted from discussion-grade to a formal scope statement: *AAD applies to agents instantiated on singular causal trajectories.*
>
> ## 7. What's missing from the big picture
>
> A partial list of structural absences that would raise the ceiling:
>
> - **No formal treatment of when the agent should switch tiers** (L0 → L1, C1 → C2, Tier 3 → Tier 1). Approximation-tiering enumerates the patterns but doesn't derive the switching policy. This is the natural target for applying AAD's own cost-benefit machinery to itself.
> - **No formalization of what "model misspecification" costs beyond triggering structural adaptation.** `#structural-adaptation-necessity` says when to switch; nothing quantifies the continuous degradation from a mildly misspecified model. This seems adjacent to `#observation-ambiguity-modulation`'s κ·𝒜 bound.
> - **No cross-hierarchy monotonicity**: the three tierings interact (e.g., does L0→L1 change the C1/C2/C3 ordering?). `#approximation-tiering` flags this.
> - **The CIY / EIG gap**: the exploration objective uses CIY as a surrogate for expected information gain; the honest substitution is unresolved.
>
> ---
>
> # Summary of what I'd queue as actionable
>
> 1. **Execute the repair for `#causal-insufficiency-detection`** per `msc/pending-findings-2026-04-22.md`. It's the only live-and-unresolved issue in this audit. Effort: 60–90 min as logged.
> 2. **Reconcile `#composition-scope-condition` and `#composition-closure`** on whether (C-iii)-only composites admit (A1). Either restrict (A1)'s scope explicitly or treat (C-iii) as a route to a weaker closure concept. Pick one.
> 3. **Rewrite the Section II preamble** in `01-aad-core/OUTLINE.md` to carry the survival-classification framing instead of the "requires work beyond" framing. The substance is elsewhere; the outline should reflect it.
> 4. **Consider whether `#information-bottleneck` frontmatter still matches its role** after `#compression-operations` landed.
> 5. **Consider whether the sector-persistence-template reframe should be promoted to an organizing principle** in the OUTLINE preamble — it already carries more weight than it is advertised for.
>
> None of this requires new theory; it requires one real repair (Finding 1) and three consistency passes (Findings 2, 3, 4 plus the editorial consolidation).

