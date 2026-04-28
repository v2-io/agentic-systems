# Extracted Claude Feedback — 2026-04-22 evening (3546217a)

**Source model:** Claude Opus 4.7 (1M context) — `claude-opus-4-7`
**Date:** 2026-04-22
**Session UUID:** `3546217a-a5eb-4307-a793-5fb04585a11f`
**Record UUID:** `8a33be5b-9b99-49a5-9e57-8aa1e4481ab8` (line 270, ts `2026-04-22T20:04:54.595Z`)
**Triggering prompt:** Joseph's standard de novo audit prompt (problematic passage / counterevidence / status / confidence; burden of proof on auditor; bigger-picture insights afterward).
**Audit length:** 26,728 chars.

## Context

This is the **third** Claude-as-auditor session Joseph ran on 2026-04-22 with the same de novo audit prompt — after `bf945f78` (15:00 UTC, the "morning" Opus audit whose 5 findings were extracted into `audits/pending-findings-2026-04-22.md`) and `6d858f28` (17:38 UTC, the "post-strengthening evening" audit whose abridged form lives in `audits/audits-2026-04-22-evening.md` under `## Opus`). This session ran at 19:52 UTC, after the strengthening commits had landed; the audit was performed against the post-strengthening repository state.

The findings are **distinct from both prior sessions** — neither of the earlier sessions surfaced these specific items (ρ_Σ as unmeasurable threshold; update-rule heterogeneity as independent closure-defect axis; Class 1 *and* learning-purposeful sub-scope as the actual exact-results frontier; bridge-lemma Tier 3 not characterized; orient-cascade step 4c SNR question; "DAG is forced" overstatement of what `#graph-structure-uniqueness` actually proves). This is a genuinely third independent reading of the same snapshot.

## Disposition

**The session ended with the audit** — no follow-up user messages. Joseph's task spec notes "Joseph clipboard-copied the full audit at the time, so it may have been pasted somewhere later." We confirmed:

- **Finding A** (ρ_Σ unmeasurability): the *finding* was preserved in `msc/AUDIT-WORKING-584721/51-schema-strategy-persistence.md` as "Opus A finding (F28 territory): ρ_Σ is the unmeasurable threshold parameter on which the trajectory guarantee depends" — but the full reasoning here was not landed verbatim anywhere.
- **Findings B, C, D, E, F**: not surfaced in any existing `audits/`, `msc/`, or segment file we could find. The full reasoning here is **not** preserved elsewhere.
- **Bigger-picture sections 1–7**: not preserved elsewhere. Sections 4 (two-tier presentation discipline), 5 (composition-closure may be over-engineered), 6 (most-novel-contribution-isn't-where-claimed), and 7 (dual-edged identifiability-floor pattern) are particularly distinctive.

So this extraction fills a real archaeological gap.

## Verbatim audit content

> Now I have what I need to write up the audit. Here is my full report.
>
> ---
>
> # De Novo Audit of Agentic Systems Framework (current repository state)
>
> ## Methodological note
>
> I read systematically through `01-aad-core/src/`, `02-tst-core/src/`, and the four component OUTLINEs. I evaluated current segment text only — no priors imported from `msc/` for the rejection pass. Most candidate findings I considered turned out to be *already* explicitly caveated or scope-narrowed. The repo's "honesty as load-bearing architecture" principle is real and visible at the segment level; it sets a high bar for "still real" findings.
>
> What follows is the small subset that survives the strict standard. For each, I quote both the problematic passage and the strongest mitigating passage, then explain why the issue still stands or why it dissolves.
>
> ---
>
> ## Findings that survive
>
> ### Finding A — Strategic disturbance rate $\rho_\Sigma$ is an unmeasurable threshold parameter on which a "structural persistence" guarantee depends
>
> **Problematic passage** (`#strategy-persistence-schema`, Forgetting prerequisite, lines 53–62):
>
> > Combining with the schema's persistence form: $(1-\lambda) > \rho_\Sigma / R_\Sigma \iff \lambda < 1 - \rho_\Sigma / R_\Sigma$. This is a **prerequisite of the schema's trajectory guarantee, not a tunable heuristic**. An agent without forgetting has no long-run strategic persistence regardless of its initial $\alpha_\Sigma$. The forgetting rate $(1-\lambda)$ must exceed the disturbance-to-reserve ratio…
>
> **Strongest mitigating passage** (same segment, Discussion §3, "Strategic disturbance"):
>
> > 3. **Strategic disturbance**: The rate at which the environment invalidates causal links in $\Sigma_t$. **Still open** as a formalized quantity — currently a domain parameter ($\rho_\Sigma$), analogous to how $\rho$ for epistemic disturbance is a domain parameter in #persistence-condition.
>
> **Status: real, partially caveated, framing is asymmetric.** The mitigating passage acknowledges $\rho_\Sigma$ is open. But the problematic passage states a *trajectory guarantee* contingent on $\lambda < 1 - \rho_\Sigma/R_\Sigma$ — and the agent has no on-line estimator for $\rho_\Sigma$. The asymmetry with epistemic $\rho$ is sharper than the segment admits: epistemic $\rho$ is at least *observable through the same channel that produces $\delta_t$* (the agent sees its model errors and can infer disturbance rate). The strategic analogue would require observing how often the agent's *causal links* become invalid — but the agent's evidence about edge truth comes through the very edge updates that are being calibrated by $\lambda$. This is closer to a circularity than a parameter-estimation problem. The "schema" framing softens this honestly, but a reader following the cascade `#orient-cascade → #strategy-persistence-schema` should notice that the strategic-side persistence guarantee is not yet operational.
>
> **Confidence: high** that the gap is real; **medium** that it is a substantive flaw rather than an honest open question.
>
> ---
>
> ### Finding B — Update-rule heterogeneity is established as an independent axis of closure defect, but `#unity-dimensions` still presents the four-unity framework as the closure-quality decomposition
>
> **Problematic passage** (`#unity-dimensions`, opening paragraph):
>
> > The quality of a composite agent's composition … decomposes along four substantially independent *quality* dimensions: epistemic ($U_M$), teleological ($U_O$), strategic ($U_\Sigma$), and perceptual ($U_{\text{obs}}$). These dimensions parametrize rate-distortion curves for the component closure defects…
>
> **Strongest mitigating passage** (`#unity-closure-mapping`, "Two-axis structure" §):
>
> > Update heterogeneity is not captured by any of the four unity dimensions as defined in #unity-dimensions. The four unities measure shared *content* (information, goals, policies, observations); $\Delta K$ measures differential *structure*… This is an independent dimension of the closure-defect rate-distortion surface.
>
> And `#unity-dimensions` Working Notes:
>
> > **Update-rule heterogeneity is a missing axis** … (C) accept that the closure defect has a two-axis structure (unity × homogeneity) rather than a single unity axis. Option (C) is the current working position — it preserves the four-unity framework without overclaiming coverage. Formal resolution open.
>
> **Status: real, half-integrated.** The Working Note documents the gap and even names the chosen resolution (Option C). But the *Formal Expression* of `#unity-dimensions` still names four dimensions and introduces them as "the" decomposition, with the two-axis structure deferred to Discussion + Working Notes + a sister segment. Independence-audit (item 4) catalogs the failure but routes the reader to "log it as working-position rather than resolved." The gap between "we know the framework is two-axis" and "the framework is presented as four-axis with a footnote" is the real issue. A reader who consults `#unity-dimensions` first sees a four-axis claim that the theory has internally rejected.
>
> **msc/ context that should be promoted**: `msc/spike-unity-closure-mapping.md` §"Two-axis structure" derives the closed form $\varepsilon_x^2 = (\Delta K/2)^2[S_- - C_{+-}^2/S_+]$ explicitly and recommends Option C. The integration into the formal expression of `#unity-dimensions` (not just its Working Notes) hasn't been done.
>
> **Confidence: high.**
>
> ---
>
> ### Finding C — Section II's exact-results scope requires *both* Class 1 (modular) architecture *and* the "learning purposeful agent" sub-scope, but only the Class 1 narrowing is foregrounded at OUTLINE level
>
> **Problematic passage** (`01-aad-core/OUTLINE.md`, Section II preamble):
>
> > **Architectural scope.** Section II's exact results apply to **Class 1 (modular) agents** — architectures where epistemic processing ($f_M$) is structurally separated from purposeful processing ($f_G$). This includes: Kalman filter + LQR, modular RL with separate world model… **This is the most significant scope restriction in the theory**…
>
> **Counter-passage from the same theory** (`#causal-hierarchy-requirement`, Scope Narrowing):
>
> > We restrict attention to **learning purposeful agents** — agents that must **acquire or refine** Level 2 knowledge during operation. … Pre-compiled agents are within agency scope (they have objectives and act on them) but outside learning-agent scope — their causal structure was externally supplied by a designer who had Level 2 access. **All remaining Section II results operate within learning-agent scope** unless explicitly noted otherwise.
>
> **Status: real, two scope narrowings stack but only one is visible at the architectural top.** Reading the OUTLINE, Kalman+LQR is the canonical example of Class 1 — but per `#causal-hierarchy-requirement`, LQR is *also* outside Section II's exact scope, because its causal structure was "externally supplied by a designer." The same example is *in* the architectural scope but *out* of the learning scope. The two scopes intersect rather than coincide. The OUTLINE's "most significant scope restriction" framing is misleading because it implies Class 1 → Section II applies, when in fact Class 1 ∩ learning-agent → Section II applies. A reader designing a control system would reasonably believe Section II covers Kalman+LQR and be wrong by the theory's own internal logic.
>
> The mitigating passage is buried in a single segment and uses scope language that reads more like an editorial choice than a load-bearing restriction. The OUTLINE preamble for Section II should mention the learning-agent narrowing alongside the architectural one.
>
> **Confidence: high.**
>
> ---
>
> ### Finding D — The composition-closure bridge lemma's Tier 3 is "per-domain verification required" with no characterization of how often Tier 3 binds
>
> **Problematic passage** (`#composition-closure`, Epistemic Status):
>
> > - **Tier 3 (independent verification):** Non-convex optimization, discontinuous/rule-based corrections, agents with non-mismatch-driven state components. Contraction must be verified per-domain.
>
> **Strongest mitigating passage** (same segment, "Composite (A4) from sub-agent properties"):
>
> > Composite (A4) from sub-agent properties: $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$, $R_c \leq \min_i R_i$ — Weakest-link bound; `msc/working-composition-admissibility.md` §6.2 — Derived (conditional on bounded coordination cost…)
>
> **Status: real and structurally severe.** The weakest-link bound says: a composite of Tier-1 + Tier-3 agents is Tier-3 dominant. Therefore *most* practical composites — any team with even one rule-based or non-convex component (most human teams, most multi-LLM systems, most hybrid architectures) — fall in Tier 3, where the bridge lemma "must be verified per-domain." The composition theory's central transferability result is unavailable in exactly the regime where composition is most interesting empirically. This is acknowledged but the *frequency* of Tier 3 binding isn't characterized, and downstream segments that invoke composite persistence (e.g., `#team-persistence`'s "Composite description applies") implicitly assume Tier 1 or Tier 2 conditions hold.
>
> The framing emphasizes that Tier 1 covers "Bayesian updaters / strongly-convex-gradient / linear-PD" — a substantial mathematical class but a thin slice of practical agents. The claim "the composite description holds for Tier 1" is true; the harder claim — "most practical composites of interest are Tier 1" — is not made and would not be defensible.
>
> **Confidence: medium-high.** The reframing this would warrant: position composition closure as "exact for a narrow class of estimation-flavored composites; structural template for everything else." This is honest about what's load-bearing.
>
> ---
>
> ### Finding E — The orient cascade prescribes a step (4c, causal-sufficiency check) whose practical operation depends on the agent's ability to separate sibling-covariance signal from edge-credence noise at convergence; this signal-to-noise question is not addressed in the segments that prescribe the step
>
> **Problematic passage** (`#orient-cascade` step 4c):
>
> > **(4c) Causal-sufficiency check (L0→L1 escalation).** If persistent $\delta_s \approx 0$ coincides with persistent negative plan-outcome residuals … this is evidence that the DAG is causally insufficient … The diagnostic is pairwise sibling covariance under an augmented test ( #causal-insufficiency-detection) …
>
> **Counter-passage** (`#causal-insufficiency-detection`, Epistemic Status):
>
> > The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: standard hypothesis testing applied to interventional data from the feedback loop, with explicit preconditions. **Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence**; in adversarial or fast-drifting environments the test's effective sample size shrinks.
>
> **Status: real, half-caveated.** The detection segment honestly flags the signal-to-noise issue. But the cascade segment cites step 4c as the *unique broadly-available* diagnostic for L0→L1 escalation — backed by the no-go theorem that forbids on-policy detection. So the cascade depends on a step whose practical sensitivity is acknowledged as "depends on how cleanly the agent can separate signal from noise" without further analysis. Two regimes that probably matter — adversarial environments and fast-drifting environments — are exactly where the test's power degrades, but they are also where causal-insufficiency detection matters most. The combination ("step 4c is the unique escape" + "step 4c is least powerful where you need it most") is not surfaced in the cascade.
>
> **Confidence: medium.** The framing is internally consistent; the issue is that a reader following the cascade as a procedure will reach a step whose practical effectiveness is treated as a secondary detail in a sister segment.
>
> ---
>
> ### Finding F — The "DAG is forced" framing in `#strategy-dag` slightly overstates what `#graph-structure-uniqueness` actually proves
>
> **Problematic passage** (`#strategy-dag`, "Why a DAG"):
>
> > The DAG structure is not a modeling convenience but a *consequence* of operational requirements on any causally-reasoning bounded agent — at the level of sufficiency, not yet necessity.
>
> (Phrasing is honest *if* the reader catches "at the level of sufficiency, not yet necessity.")
>
> Same segment downstream:
>
> > **The graph structure is derived; the parameterization is chosen.** The DAG structure follows from temporal ordering (acyclicity — proved) and the Causal Markov Condition theorem under causal sufficiency (Markov factorization — proved conditional). This is a theorem-backed result, not a sketch …
>
> **Mitigating passage** (`#graph-structure-uniqueness` opening):
>
> > The argument parallels Cox's theorem for probability in *form* but not yet in *strength*: Cox's theorem is necessary-and-sufficient (the only measure satisfying the desiderata is probability); this result is sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them).
>
> **Status: ambiguous; minor.** The graph-uniqueness segment is exemplary in flagging the asymmetry. But strategy-dag's "graph structure is derived" reads stronger than the underlying theorem warrants. A reader who reads strategy-dag without consulting graph-structure-uniqueness will get an overconfident sense of "DAG is forced." This is not a substantive theory issue — alternative representations (factor graphs, junction trees) really do satisfy the Markov factorization, so the practical claim survives — but the framing tension is real.
>
> **Confidence: low-medium.** This is more an editorial finding than a structural one.
>
> ---
>
> ## Findings I considered and rejected (because the repo already adequately frames them)
>
> A representative sample, with the rejection rationale:
>
> - **"Pinsker bound is loose; segment retains linear KL form for IB-shape, not regret-tightness"** — `#strategy-cost-regret-bound` §7 explicitly catalogs both forms and explains the trade-off. Self-aware.
> - **"Channel independence in scalar tempo overestimates by up to 72%"** — `#independence-audit` item 6 names this and points to per-dimension extension; `#per-dimension-persistence` instantiates the repair.
> - **"$G_t = (O_t, \Sigma_t)$ is 'definitional' but acts load-bearing"** — `#strategy-dimension` Discussion explicitly says "the decomposition resolves a type error" and reframes it as load-bearing.
> - **"Causal sufficiency assumption is the dominant failure mode"** — Treated as a first-class concern across `#strategy-dag` Correlation Hierarchy, `#causal-insufficiency-detection`, `#identifiability-floor`, `#independence-audit`. This is one of the framework's most honest treatments.
> - **"$V_{\max} < \infty$ assumption for regret bound is 'mild but not automatic'"** — `#strategy-cost-regret-bound` §8 names this as a vacuity regime and `#strategy-complexity-cost` Epistemic Status explicitly states the assumption.
> - **"L1' under unobservable common cause is identifiability-blocked"** — Refuted, not "open." `#strategy-dag` and `#identifiability-floor` Instance 2 give the Cramér-Rao argument and three explicit repair routes.
> - **"K_c timescale ratio in composition-closure is part of the problem specification, not derived"** — Acknowledged. The 2026-04-22 repair (`#composition-closure` Working Note) made K_c explicit specifically to avoid the previous synchronous-only bug. The honest framing — "K_c is application-specific" — is consistent with `#temporal-nesting`'s singular-perturbation logic.
> - **"Section III contains five `--GAP--` rows in the OUTLINE"** — These are flagged as gaps in the outline itself; they are not concealed.
> - **"Logogenic agents are out of formal scope of `#agent-identity` (type-like, not token-like)"** — `#agent-identity` Discussion explicitly addresses the clone problem and frames it as scope, with `03-logogenic-agents/` carrying the framework-stage handoff.
> - **"Pre-compiled controllers (PID, LQR) outside learning-agent scope"** — Acknowledged in `#causal-hierarchy-requirement`. (See Finding C above for what *isn't* adequate about this.)
>
> ---
>
> ## msc/ context for the surviving findings
>
> **For Finding A** (ρ_Σ underspecified): `msc/sketch-strategy-dynamics-gaps.md` lines 195–225 and `msc/spike-strategy-tempo-cost.md` line 392 both describe ρ_Σ in terms identical to the segment — "qualitatively different sources" with no estimator. There is no msc material that addresses how an agent could measure ρ_Σ from its own data. The gap is not a missing-integration issue; it is a genuinely unaddressed question.
>
> **For Finding B** (two-axis closure structure not integrated): `msc/spike-unity-closure-mapping.md` §"Two-axis structure" already derives the closed form and recommends Option C explicitly. The work to update `#unity-dimensions`'s formal expression from four-axis to two-axis is mechanical and not yet done. This is an integration debt, not an open question.
>
> **For Finding C** (stacked Class-1 + learning-agent scopes): No msc/ material addresses the OUTLINE-level visibility gap. The fix is editorial (mention learning-agent scope in the OUTLINE preamble alongside Class 1).
>
> **For Finding D** (Tier 3 prevalence): `msc/spike-bridge-lemma-contraction.md` derives the tier taxonomy. No msc/ material characterizes the prevalence of Tier 3 in practical composites. This is a research gap, not an integration debt.
>
> **For Finding E** (4c signal-to-noise): No msc/ material I found addresses the practical sensitivity of the covariance test. The honest path forward is either (a) characterize sensitivity bounds in `#causal-insufficiency-detection`, or (b) qualify the cascade's reliance on 4c with the corresponding sensitivity caveat.
>
> ---
>
> ## Big-picture reflections
>
> These are intuitions formed from reading the whole — speculative, not derived. I'm naming them as observations the author may or may not find generative.
>
> ### 1. The deepest unifying pattern in the framework is *one principle stated four times*
>
> The 2026-04-22/23 strengthening cycle named three Cauchy-functional-equation uniqueness theorems (chain-confidence, reverse-KL, log-odds). The note flags this as "candidate for promotion to explicit meta-segment." But the same pattern appears at least twice more if you look:
>
> - **Sector-condition-stability** (Lyapunov) is the Lagrangian *of the same shape* — quadratic candidate forced by inner-product structure, with the sector condition as the local additivity-of-correction axiom.
> - **The IB Lagrangian** in `#compression-operations` decomposes information-theoretic objectives into (compression-cost) − β·(predictive-relevance), which is the rate-distortion *additive* form, with β as the Lagrange multiplier on the additivity constraint.
>
> The deeper claim might be: *AAD repeatedly forces additive decompositions on log/quadratic coordinates because all four of its core operations (model update, strategy update, persistence, compression) face the same structural problem — independent factors composing to a measure on which the optimization-to-be-derived is convex.* The promotion to a meta-segment would be more powerful if it asserted this five- or six-instance pattern rather than just the three-instance one. The candidate name is something like **`#additive-coordinate-forcing`** — and it would sit in the same architectural row as `#identifiability-floor` and `#separability-pattern` as a third meta-pattern segment, plausibly the most fundamental of the three.
>
> ### 2. The "calibration laboratory" framing for software is a template that could generalize
>
> `#software-epistemic-properties`' transfer-assumption table is one of the most beautiful structural moves in the framework. The pattern: name the AAD-core quantity, the identification condition, the software configuration that satisfies it, and the non-software transfer requirement.
>
> This pattern could be generalized to *every* AAD instantiation. A `domain-instantiation-template.md` (or a section of FORMAT.md) could prescribe: any new domain instantiation must produce a transfer-assumption table with rows for each AAD-core identification condition. This would make TST less of an exception and more of an exemplar. Logogenic and logozoetic instantiations could then be evaluated against the same template, and the gap between "what TST does well" and "what 03-logogenic-agents/ doesn't yet do" becomes structural instead of stylistic.
>
> ### 3. The framework's "agent identity = singular trajectory" commitment is doing more architectural work than it gets credit for
>
> `#agent-identity` is presented as a scope statement, but it's actually a *philosophical commitment* with major downstream consequences. The interventional reading of loop data, the rejection of cross-trajectory model merging, the sub-scoping of logogenic agents — all rest on this commitment. It might deserve elevation from "scope" to something closer to an architectural postulate: AAD is a theory of *token-level adaptation under causal embedding*, not a theory of *type-level agent populations*. This framing would also clarify why type-level claims about "the model" require additional machinery (population dynamics, statistical aggregation) that AAD doesn't supply natively.
>
> ### 4. The honesty discipline produces a heavy reading load that might benefit from a "two-tier" presentation
>
> Every segment carries equation-level tags, scope conditions, epistemic-status caveats, and "what is derived vs chosen" tables. This is rigorous and right for the formal core. But a reader trying to *understand the framework's shape* must process all this surface-level qualification before reaching the load-bearing content.
>
> A possible structural move: each segment could carry a "Reader's Path" preamble that states the load-bearing content in 1–2 sentences without qualification, with the formal apparatus following. This would not change the substance — only the reader's first contact. The cost is mild redundancy; the benefit is that the framework becomes teachable. (TST's calibration-laboratory framing is already moving in this direction.)
>
> ### 5. The composition-closure machinery may be over-engineered for what it actually delivers
>
> The bridge lemma requires the incremental sector bound (DA2'-inc), which is "strictly stronger than (A4)" and only proved for Tier 1. The (A1)–(A4) admissibility, the (P1)–(P3) projection conditions, the K_c timescale ratio, the Mahalanobis norm choice, the closure-defect components $\varepsilon_x, \varepsilon_a, \varepsilon_o$ — together these define a beautiful framework, but its "central theorem" (bridge lemma) only applies to a subclass of agents whose composition can mostly be analyzed by simpler estimation-theoretic tools (Kalman filter consistency under coupling).
>
> The simpler claim — *composite agents are AAD agents iff their effective dynamics admit an AAD-shaped reduction* — might be enough for the framework's needs, with the bridge lemma machinery scoped explicitly to the linear-Gaussian and exponential-family cases where it actually delivers a clean theorem. The current presentation lifts the apparatus to a generality that the proofs don't underwrite. A consolidation pass might trade some apparent generality for substantial simplification.
>
> ### 6. The framework's most novel contribution may not be where it claims to be
>
> The CLAUDE.md and theory-character notes emphasize *integration* — connecting control theory, causal inference, information theory, and agent architecture. But reading the segments, the genuinely novel structural moves are:
>
> - The **separability pattern** as an organizing principle (positive half) and **identifiability floor** (negative half) — this pair-of-meta-segments approach to scope characterization is structurally distinctive and not obvious from any of the source disciplines.
> - The **scope-honesty-as-load-bearing-architecture** posture — this is a methodological commitment that I've never seen expressed at this clarity in adjacent literature.
> - The **calibration-laboratory** framing for domain instantiation — same.
>
> The integration narrative is true but downplays the strongest contribution. The framework's distinctive value may be its *epistemic architecture* (how it organizes claims, scopes, repairs, and meta-patterns) more than the specific results it integrates. A future README or paper introduction could foreground this — "what's distinctive about AAD is not which results it imports but how it organizes the conditions under which results apply."
>
> ### 7. The "dual-edged" axis of the identifiability-floor pattern is partially hidden
>
> Each identifiability floor instance is presented with strengthened-machinery framing: "the floor strengthens machinery X as the unique escape." This is honest and load-bearing. But the dual reading is also true: each floor *bounds the framework's reach*. The current presentation emphasizes the positive (X is necessary; AAD provides X) over the negative (without X, AAD is forbidden from inferring this). Both are accurate; foregrounding both might produce a more complete scope-mapping.
>
> The same observation applies to `#separability-pattern`'s "general open" column — it is presented as "honest scope-marking" but it might equally be read as "the territory the framework cannot enter." Naming both faces might strengthen the architecture.
>
> ---
>
> ## Summary
>
> Six findings survive strict scrutiny, ranging from high-confidence integration debts (Finding B) to medium-confidence framing concerns (Findings D, E) to one editorial-but-real visibility gap (Finding C). The deepest substantive finding is A (ρ_Σ as an unmeasurable threshold parameter on which a stated guarantee depends); the deepest structural one is D (the bridge lemma's central transferability claim is unavailable for most practical composites). Most candidate findings I considered dissolved into "already adequately caveated" — the honesty discipline really is doing the work it claims to do.
>
> The big-picture intuitions point toward consolidation moves (the additive-coordinate-forcing meta-pattern; calibration-laboratory as a generalizable template; agent-identity as architectural rather than scope) rather than additions. The framework's strongest unrealized leverage is probably elevating its own organizing principles (scope honesty, identifiability floors, separability patterns, calibration laboratories) to the status of distinctive contributions — currently they read as careful methodology, but they are actually the framework's most architecturally novel content.

