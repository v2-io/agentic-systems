# Extracted Codex + Gemini Audits — 2026-04-21

**Source models:** OpenAI Codex (two passes) and Google Gemini (two passes)
**Date:** 2026-04-21
**Sessions:** `afc424e8-2764-4890-9949-82478099a3b7` (lines 488, 616, 823); `968a5f16-b46c-4d83-b7e9-9fc7539fe3eb` (line 993)
**Topics:** TST principled-decision-integration term loss; git-as-causal overstatement; composition-consistency overgeneralization; Level-3-replay overclaim; tempo-composition dimensional mismatch; Prop B.5 contradiction with B.3a; per-dimension persistence L1 vs L2 norm mixing; adversarial destabilization Model D vs S framing; composition-closure existence vs quality entry-criterion conflict; unity-dimensions four-axis claim with missing fifth axis; software Ω_t scope ambiguity; soft-facilitator failure of L1 augmentation; composition-closure prohibits temporal coarse-graining.

## Context

The 2026-04-21 audit cycle was substantial: Joseph relayed three Codex passes and two Gemini passes within a single session day. Some findings (the soft-facilitator L1 issue, the temporal coarse-graining issue) were captured in `audits/pending-findings-2026-04-21.md` as Findings A and B. Most of the rest were never preserved verbatim; they shaped Joseph's planning for the 2026-04-22 work cycle (where they appeared as additional pressure on architectural moves).

## Disposition

- The TST `principled-decision-integration` finding (loss of $\hat n_{\text{future}}$) was processed and led to fixes in `02-tst-core/src/principled-decision-integration.md`.
- The git-as-causal finding led to a substantial qualifying pass on `system-coupling.md` and `coherence-coupling-measurement.md`.
- The Level-3-replay finding led to scope tightening on `software-epistemic-properties.md`.
- The dimensional-mismatch finding (tempo-composition) led to a derivation rewrite tying coordination overhead to disturbance-rate scaling.
- The Prop B.5 / B.3a contradiction was addressed by the natural-parameter / log-odds reframe (G-BP1 architectural proposal landed in commit `a14682e`).
- The L1 vs L2 norm mixing in per-dimension persistence was caveated.
- The composition-closure temporal coarse-graining finding became `pending-findings-2026-04-21.md` Finding A and was resolved 2026-04-22 with the per-macro-step formulation (Option 3).
- The L1 soft-facilitator finding became Finding B and was resolved by the L1' explicit treatment.
- The unity-dimensions fifth-axis finding became part of the F29 unity-dimensions two-axis structure landing 2026-04-25.

## Verbatim feedback Joseph relayed

### Codex audit — TST + composition + Level-3-replay (`afc424e8` line 488, ts 2026-04-21T21:07:11Z)

> Pushed! Thank you. The following is some feedback from a fresh audit by Codex for your evaluation:
>
> • Audit scope: I reviewed the active segment corpus in `01-aad-core/src`, `02-tst-core/src`, and `03-logogenic-agents/src`, with `04-logozoetic-agents` limited to its outline because it has no current segments. I treated `02-tst-core/src/old-*` as retained source material rather than canonical current claims, because `02-tst-core/OUTLINE.md:53` explicitly frames them that way.
>
> 1. `#principled-decision-integration` drops the future-change-count term while claiming to generalize `#dual-optimization`. Problematic passage: `02-tst-core/src/principled-decision-integration.md:27` defines total expected time as $t_0(C) + \sum_i P(F_i) \cdot (...)$ and then says this is "the general form of `#dual-optimization`" at `02-tst-core/src/principled-decision-integration.md:29`. Strongest counterevidence elsewhere in src: `02-tst-core/src/dual-optimization.md:21` makes the lifecycle term explicitly $\hat n_{\text{future}} \cdot (...)$, and `02-tst-core/src/change-expectation-baseline.md:33` defines $\hat n_{\text{future}}$ while `02-tst-core/src/change-expectation-baseline.md:55` says downstream claims must carry it as a median prediction. Assessment: still real. As written, the "general form" prices one expected future feature-type draw unless $\sum_i P(F_i)$ is silently allowed to exceed 1, which the segment never says. Confidence: high.
> 2. Git-derived coupling is still framed as already causal in places where the repo elsewhere only supports it as a conditional empirical program. Problematic passage: `02-tst-core/src/system-coupling.md:31` says the quantity is "genuinely causal, not just correlational," and `02-tst-core/src/coherence-coupling-measurement.md:36` plus `:52` say git provides interventional data that gives the estimates a causal interpretation. Strongest counterevidence elsewhere in src: `02-tst-core/src/causal-discovery-from-git.md:72` says usable causal estimation is only a discussion-grade hypothesis, `:76` says the confounders are the typical case, and `:104` says the existing measurements may be only descriptive statistics if confounding dominates. Assessment: still real. The repo now has the caveat segment, but the definition and measurement segments still speak as if the causal bridge were already secured. Confidence: high.
> 3. `#composition-consistency` operationalizes scale-invariance more broadly than the current closure machinery supports. Problematic passage: `01-aad-core/src/composition-consistency.md:12` says "a team of agents is itself an agent," and `:43` says every subsequent result is understood to apply at every compositional level where the timescale condition holds. Strongest counterevidence elsewhere in src: `01-aad-core/src/composition-closure.md:161` says the bridge lemma is not derivable from (A4) alone and needs the stronger incremental sector bound; `:165` leaves Tier 3 agents on per-domain verification; `:202` says the Mori-Zwanzig connection is only partial; and `:206` explicitly says the contraction assumption cannot be proved from (A4) alone. Assessment: still real. The meta-postulate of cross-level compatibility is fine, but the segment's operational gloss currently outruns the closure theory that is supposed to justify it. Confidence: medium-high.
> 4. `#software-epistemic-properties` overstates version-control replay as literal Pearl Level 3 access. Problematic passage: `02-tst-core/src/software-epistemic-properties.md:29` says version control provides "literal counterfactual execution" and "Level 3 epistemic access … with ground-truth verification." Strongest counterevidence elsewhere in src: the same segment later admits at `:70` that path dependence and environmental coupling cannot be replayed, and `02-tst-core/src/causal-discovery-from-git.md:78` says the chain from git data to AAD quantities is empirical and unresolved. Assessment: still real. Those caveats make the method valuable, but they also make "literal Level 3 with ground-truth verification" too strong. At most the segment has shown an unusually strong executable proxy for some counterfactual questions, not a clean Pearlian Level 3 bridge. Confidence: high.
>
> msc Pass
>
> - Composition: `msc/spike-bridge-lemma-contraction.md:522` already recommends restating `#composition-closure` with a Tier 1/2/3 condition hierarchy, and `msc/spike-mori-zwanzig-composition.md:349` explicitly says the MZ anchor is only partial and breaks where purposeful composition is most load-bearing. That narrowing has not been propagated back into the stronger front-door framing of `#composition-consistency`.
> - Git causal status: `msc/2026-03-13-feedback.md:80` and `msc/2026-03-14-section-iv-paper-outline.md:56` already say the right thing: treat git/co-change as a promising empirical mapping, not a secured causal bridge. That language has not been pushed back into `#system-coupling` and `#coherence-coupling-measurement`.
> - Decision integration: `msc/2026-03-14-section-iv-paper-outline.md:41` preserves the correct dual-optimization form with $\hat n_{\text{future}}$, and `msc/2026-03-13-feedback.md:98` explicitly says downstream decision rules must carry the median/stationarity qualifications more clearly. The current `#principled-decision-integration` segment does not.
> - Level 3 replay: I did not find an `msc/` note that actually repairs this claim. The closest material instead sharpens the gap: `msc/spike-purposeful-agent-derivation.md:156` says Level 3 requires structural assumptions, then `:186` repeats the unqualified git checkout claim. The missing integration is the absent structural-assumption argument, not an unincorporated fix.
>
> Non-Findings
>
> - I did not count `03-logogenic-agents/src/section-ii-survival.md` as a finding. Its scorecard is precise to a fault, but the segment already marks the classification conditional and inherits the underlying segments' weaker statuses.
> - I did not count `03-logogenic-agents/src/context-turnover.md` as a finding. Its headline is aggressive, but the active logogenic segments already narrow it with explicit reconstruction and external-memory caveats.

### Gemini audit — Four mathematical issues + msc reconciliation (`afc424e8` line 616, ts 2026-04-21T21:23:42Z)

> Great work. Here is another new audit from Gemini for your evaluation:
> ✦ Here is a rigorous de novo audit of the current state of `01-aad-core/src/`, followed by an analysis of the unintegrated context found in the `msc/` directory.
>
> Part 1: De Novo Audit of `01-aad-core/src/`
>
> **Finding 1: Dimensional Mismatch in Sub-Additive Tempo Derivation**
> - Problematic passage: `tempo-composition.md`
>   > "The fraction of macro-tempo consumed by closure correction: $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$ ... This is the coordination overhead: a lower bound equal to the closure error rate. ... The realized external tempo: $\mathcal T_c^{\text{ext}} = \mathcal T_c - C_{\text{coord}} \leq \sum \mathcal T_i - \varepsilon^\ast \nu_c$ ... Brooks's Law occurs when $\Delta\varepsilon^\ast \nu_c > \Delta\mathcal T_i$"
> - Strongest counterevidence: `composition-closure.md` (Bridge Lemma)
>   > "Since the closure defect $\varepsilon^\ast$ is the per-step error and $\varepsilon^\ast \nu_c$ is the closure error rate (per-step error × steps per unit time), this bound has the same structure as $\rho / \alpha$ from `#persistence-condition` — a ratio of disturbance rate to correction rate."
> - Status: Real mathematical error. The derivation equates and subtracts quantities with fundamentally incompatible physical units.
>     - Adaptive tempo ($\mathcal{T}_i$) has units of inverse time ($[\text{time}^{-1}]$) (event rate $\times$ dimensionless gain).
>     - Closure defect ($\varepsilon^\ast$) measures error in state/action space, meaning it has units of distance ($[\text{dist}]$).
>     - Therefore, the closure error rate ($\varepsilon^\ast \nu_c$) has units of distance per time ($[\text{dist}] \cdot [\text{time}^{-1}]$) (a disturbance rate).
>   Subtracting $\varepsilon^\ast \nu_c$ directly from $\sum \mathcal T_i$ is dimensionally invalid. To convert the internal disturbance rate into a tempo-equivalent penalty, it must be divided by a scalar distance constraint.
> - Confidence level: Very High.
>
> **Finding 2: Contradiction in Transferring the Sector Condition for Coupled Edges**
> - Problematic passage: `strategic-dynamics-derivation.md` (Proposition B.5c)
>   > "When does it fail? When edge corrections are coupled... This occurs for: Unobservable intermediates (B.3): The marginal Bayesian update couples edge posteriors. ... For coupled corrections, the general Cauchy-Schwarz bound gives: $\alpha_s \geq \frac{\alpha_c}{\kappa(\mathbf{J})^2}$"
> - Strongest counterevidence: `strategic-dynamics-derivation.md` (Proposition B.3a)
>   > "(a) The per-edge sector condition fails: the marginal Bayesian update violates (SA1) with systematic bias $O(1/n)$... Evaluating at truth ($\hat p_k = \theta_k$): $\mathbb{E}[\Delta \hat p_1]\big\rvert_{\hat p = \theta} = -\frac{\theta_1(1-\theta_1)(1-\theta_2)}{n_1+1} \neq 0$"
> - Status: Real logical contradiction. Proposition B.5 relies heavily on the premise that a valid base per-edge sector parameter ($\alpha_c > 0$) exists to transfer into plan-confidence error via the Jacobian. However, Proposition B.3a rigorously proves that for unobservable intermediates under Bayesian updates, the per-edge sector condition *fails entirely* because it violates the zero-mismatch assumption (SA1). You cannot mathematically use a Cauchy-Schwarz bound to push a non-existent, invalid $\alpha_c$ through the Jacobian to recover a valid plan-level $\alpha_s$.
> - Confidence level: Very High.
>
> **Finding 3: Inconsistent Error Norms in Stochastic Persistence Thresholds**
> - Problematic passage: `per-dimension-persistence.md`
>   > "Model S: Stochastic Per-Dimension Steady State... $E[|\delta_k|] = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$ ... Persistence requires (from $E[|\delta_k|] < \delta_{\text{critical},k}$...) $\eta_k > \frac{\rho_k^2}{\pi \cdot \delta_{\text{critical},k}^2}$"
> - Strongest counterevidence: `persistence-condition.md`
>   > "Model S (stochastic disturbance, GA-2S): $\alpha > \frac{n\sigma_w^2}{2R^2}$ ... The ultimately bounded mismatch is ... $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ ... Task adequacy requires $R^*_S < \lVert\delta_{\text{critical}}\rVert$." (Yielding the 1D operational form $\eta^\ast > \frac{\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2}$)
> - Status: Quantitative incoherence. `persistence-condition.md` explicitly sets the task adequacy threshold using the Root Mean Square (RMS) error against the critical mismatch ($L_2$ norm). `per-dimension-persistence.md` abruptly shifts to bounding the Mean Absolute Error ($E[|\delta_k|]$, $L_1$ norm). Because MAE and RMS differ by a constant factor of $\sqrt{2/\pi}$ for Gaussian distributions, applying the same $\delta_{\text{critical}}$ to both breaks quantitative coherence between the scalar operational forms and per-dimension threshold bounds.
> - Confidence level: High.
>
> **Finding 4: Ambiguous Disturbance Model in Destabilization Threshold**
> - Problematic passage: `adversarial-destabilization.md`
>   > "Result. B's ultimately bounded radius under coupled dynamics is: $R^*_B = \frac{\rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\alpha_B}$ ... B diverges (exits its sector-condition region) when $R^\ast_B > R_B$, i.e., when: ... $\mathcal{T}_A > \frac{\alpha_B R_B - \rho_{B,\text{base}}}{\gamma_A}$"
> - Strongest counterevidence: `adversarial-exponent-regimes.md`
>   > "The adversarial tempo advantage exponent ... is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift (Model D) or stochastic noise (Model S)..."
> - Status: Incomplete framing. The divergence threshold presented in `adversarial-destabilization.md` is strictly true only for deterministic drift (Model D), relying on the $R^\ast = \rho/\alpha$ scaling. If the adversarial coupling enters as stochastic noise (Model S), the boundary scales with $1/\sqrt{\alpha}$. The core segment treats the deterministic equation as the general divergence result, failing to caveat that it requires a Model D environment.
> - Confidence level: High.
>
> ---
>
> Part 2: Contextual Reconciliation from `msc/`
>
> A search of the working documents in `msc/` reveals that most of these issues are known but suffer from a failure of integration.
>
> - **Regarding Finding 1 (Dimensional Mismatch):** The spike `msc/spike-composition-closure.md` carefully refers to the coordination penalty as $C_{\text{coord}}(\varepsilon^\ast)$ — treating it as a *function* of the closure defect, not an equivalent value. However, the spike never actually derives the conversion factor required to map a distance error into a tempo cost. When this concept was written into `tempo-composition.md`, the functional dependence was lazily swapped for direct subtraction, introducing the dimensional error. **What's missing in `msc/`:** A formal derivation dividing $\varepsilon^\ast \nu_c$ by the relevant constraint distance (analogous to the persistence condition's $\rho / R$).
> - **Regarding Finding 2 (Prop B.5 Contradiction):** This is beautifully resolved in `msc/spike-credit-assignment-boundaries.md`. The spike realizes that marginal Bayesian updates doom the sector condition (violating SA1) and formally recommends swapping them for a gradient-based attribution scheme. The spike proves that gradient-based attribution restores SA1, yielding a valid $\alpha_c$ that allows Prop B.5 and the Cauchy-Schwarz bound to function perfectly (albeit with a condition-number penalty). The actual issue: This architectural fix is trapped in the spike and was never ported into `strategic-dynamics-derivation.md`, which still attempts to use the mathematically incompatible Bayesian premise.
> - **Regarding Findings 3 & 4 (Model S / Model D Mixing):** The spike `msc/spike-disturbance-model-split.md` is dedicated entirely to untangling this. It explicitly catches the $L_1$ vs $L_2$ norm mixing in `#per-dimension-persistence` and mandates that the core theory strictly separate "Model D (deterministic)" from "Model S (stochastic)". The actual issue: The integration of this spike into the core segments is incomplete. Furthermore, the spike itself misses Finding 4; it explicitly claims (L418) that the "adversarial destabilization threshold" remains unchanged by the split, failing to realize that the algebraic threshold in `adversarial-destabilization.md` is structurally dependent on Model D scaling and must be branched for Model S.

### Codex audit (round 2) — Composition / unity / TST headline overclaims (`afc424e8` line 823, ts 2026-04-21T21:53:02Z)

> Excellent work. Next, some more feedback (potentially already addressed) from Codex:
>
> • Findings
>
> 1. `01-aad-core/src/composition-closure.md:51`: Problematic passage: "A set of agents forms a meaningful composite agent when $\varepsilon^* \leq \varepsilon_{\max}$." Strongest counterevidence in src: `01-aad-core/src/composition-scope-condition.md:14` says composition machinery "does not apply" without sufficient teleological alignment, and `01-aad-core/src/multi-agent-scope.md:71` says composite-level machinery applies only when that scope condition holds. Assessment: still real. Confidence: high. Why: current src still contains two incompatible entry criteria for composite status: low closure defect versus prior teleological alignment.
> 2. `01-aad-core/src/composition-consistency.md:42`: Problematic passage: timescale separation is called a "reliable practical test," "easily satisfied in common organizational settings," and usable because the gap to Tier 1 is "small"; the same segment then says "the theory applies broadly" `01-aad-core/src/composition-consistency.md:60`. Strongest counterevidence in src: `01-aad-core/src/composition-closure.md:161` says the bridge lemma needs the stronger incremental sector bound, splits agents into Tier 1/2/3, and `01-aad-core/src/composition-closure.md:208` says a richer two-purposeful-agent case is still needed. Assessment: still real. Confidence: medium-high. Why: src has a tiered, conditional transfer story, but `composition-consistency` still generalizes from a heuristic screen to broad real-world applicability.
> 3. `03-logogenic-agents/src/section-ii-survival.md:125`: Problematic passage: "An LLM agent system designer can rely on Section II's full conceptual architecture ... without modification." Strongest counterevidence in src: `03-logogenic-agents/src/coupled-update-dynamics.md:70` says identifying $X_t = (M_t, G_t)$ is only approximate, `:96` says the response decomposition is analytical with "no claim that it is computable in general," and `03-logogenic-agents/src/ai-agent-as-act-agent.md:56` calls the mapping representational. Assessment: still real. Confidence: high. Why: the 16/24 "exact survival" count is about statement-level dependence on directed separation; it does not by itself make the surviving objects operationally extractable or engineerable.
> 4. `01-aad-core/src/unity-dimensions.md:15`: Problematic passage: "The quality of a composite agent's composition can be decomposed along four substantially independent dimensions." Strongest counterevidence in src: `01-aad-core/src/unity-closure-mapping.md:79` says update heterogeneity "is not captured by any of the four unity dimensions," and `01-aad-core/src/unity-dimensions.md:78` itself now calls that a missing axis. Assessment: still real. Confidence: high. Why: the caveat exists, but the lead framing still presents the four-axis decomposition as if it were complete.
> 5. `02-tst-core/src/software-epistemic-properties.md:23`: Problematic passage: "The codebase state $\Omega_t$ is fully observable in principle." Strongest counterevidence in src: `02-tst-core/src/developer-as-act-agent.md:41` says "The full $\Omega_t$ is larger than 'the codebase'" and that restricting $\Omega$ to source code underestimates disturbance, while `02-tst-core/src/software-epistemic-properties.md:29` narrows literal Level 3 to code-internal deterministic counterfactuals. Assessment: still real. Confidence: high. Why: current TST switches between "software environment" and "codebase" without keeping $\Omega_t$ scoped, so the observability and counterfactual claims read more broadly than the repo's fuller environment model allows.
>
> msc/ Pass
>
> I did not use msc/ as a prior-baseline source. I used it only after establishing the above issues from current src.
>
> - For findings 1 and 4, `msc/spike-symbiogenic-composition.md:22` already lays out the cleaner structure: existence gate first ($U_O \geq \varepsilon_{\text{comp}}$), then quality metrics; `msc/spike-symbiogenic-composition.md:266` explicitly recommends splitting Section III into scope/mechanisms, quality, and dynamics. That architecture is not fully carried into src yet.
> - For finding 2, `msc/spike-bridge-lemma-contraction.md:457` and `:528` already sharpen the bridge lemma to the C1-C3 / DA2'a-inc conditions and a strict Tier 1/2/3 split. `composition-consistency` still leans on a softer "common settings" heuristic than that sharper formulation warrants.
> - For finding 3, `msc/spike-coupled-survival-analysis.md:40` explicitly distinguishes "well-defined" from "identifiable," `:71` says only the notation survives exactly while the factorized dynamics do not, and `:518` points to the missing post-hoc extraction machinery. The operational follow-through already exists in `msc/agentic-tft-evaluation-framework.md:5` and `msc/agentic-tft-cognitive-loop-spec.md:5`, but those ideas are not yet integrated enough into `03-logogenic-agents/src/`.
> - For finding 4, `msc/spike-unity-closure-mapping.md:261` says the reframing downgrades `unity-dimensions` as a quantitative segment unless paired with a companion mapping segment, and `msc/spike-unity-closure-mapping.md:304` makes the two-axis result explicit. src has absorbed the caveat, but not the headline reframing.
> - I did not find an equally strong msc/ correction for finding 5. That one looks less like "missing promotion from msc/" and more like a current wording/symbol-integration problem internal to TST's src text.

### Gemini evening audit — L1 + temporal coarse-graining (`968a5f16` line 993, ts 2026-04-21T23:06:06Z)

> I apologize-- I removed the TODO file as it was drained of its original items. I forgot there were items we had added. You can check it out from the last commit, or here are the items from Gemini again:
>
> ✦ Here is the de novo audit of `01-aad-core/` evaluating the current repository state for structural and theoretical gaps, followed by context from `msc/`.
>
> **Finding 1: L1 Augmented DAG Construction Fails for Soft Facilitators**
>
> - Problematic passage: `01-aad-core/src/strategy-dag.md`: "The construction principle: place the common-cause node as an AND-prerequisite above the OR/AND structure whose children it correlates. This ensures that, conditional on the common cause being satisfied, the children are independent and standard AND/OR propagation is correct."
> - Strongest counterevidence: `01-aad-core/src/worked-example-L1.md` (Section: When Correct L1 Construction Is Not Possible) acknowledges topological limitations: "The factoring-above principle works when the common cause cleanly gates all correlated children through a single AND-relationship. When this is not structurally possible... a conditioning-based propagation is needed: $P(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$."
> - Status: Real and inadequately framed. While the theory caveats topological limitations, it completely misses the semantic limitation. Factoring a common cause above an OR-node via an AND-relationship strictly forces the success probability of the entire sub-plan to 0 when the common cause is absent. This works perfectly for strict prerequisites (e.g., shared infrastructure goes down, everything fails). However, if the common cause is a soft facilitator (e.g., favorable market conditions) where success is merely less likely without it, the AND-prerequisite construction is mathematically incorrect.
> - Confidence Level: High. The text frames L1 augmentation as a "practical sweet spot" for restoring causal sufficiency under correlated failure, but a standard AND/OR DAG cannot represent soft common causes without losing the ability to succeed when the common cause is absent.
>
> **Finding 2: Composition Closure Criterion Prohibits Temporal Coarse-Graining**
>
> - Problematic passage: `01-aad-core/src/composition-closure.md` (Formal Expression) defines the state closure defect as an expected sum over micro-timesteps:
>   $$\varepsilon_x = \mathbb E_\tau \Big[ \frac{1}{H} \sum_{t=1}^H \big\lVert \Lambda_x\big(f_{\text{micro}}(X_{\text{micro}, t}, o_{\text{micro}, t+1})\big) - f_c\big(\Lambda_x(X_{\text{micro}, t}), \Lambda_o(o_{\text{micro}, t+1})\big) \big\rVert_\mathcal{X} \Big]$$
> - Strongest counterevidence: `01-aad-core/src/temporal-nesting.md` states "An agent's adaptive processes stratify naturally by timescale... $\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$". Additionally, `composition-closure.md`'s Working Notes explicitly mention Mori-Zwanzig and zero-lag memory-kernel bounds as partial connections.
> - Status: Real. The formal definition of the closure defect evaluates the macro-dynamics $f_c$ at every single micro-timestep $t$. This strictly forces the composite macro-agent to update at the exact same clock rate as the micro-agents. However, composite agents inherently operate on slower timescales than their constituents, aggregating many micro-events before a macro-state update occurs. The equation mathematically prohibits temporal coarse-graining.
> - Confidence Level: High. The formulation requires the macro-dynamics to ingest micro-level observations $o_{\text{micro}, t+1}$ and update synchronously, breaking the concept of temporal abstraction for macro-agents.
>
> ---
>
> Additional Context from `msc/`
>
> Context for Finding 1 (L1 DAG Construction):
> A review of `msc/spike-L1-worked-example.md` confirms the actual issue is that soft correlation hasn't been properly integrated. The spike explicitly hardcodes the assumption that the alternatives fail when the infrastructure is down (i.e., $\theta_{1| \neg C} = 0$). The spike's derivation of the "factoring above" principle relies entirely on the common cause being a strict prerequisite. There is no working document that successfully reconciles standard single-pass AND/OR propagation with soft correlation; the theory jumps straight from strict prerequisites to exponentially complex conditioning-based propagation without acknowledging the gap.
>
> Context for Finding 2 (Temporal Coarse-Graining):
> Extensive discussion of timescale nesting exists in `msc/spike-discrete-time-sector.md`, `msc/spike-purposeful-agent-derivation.md`, and `msc/agentic-tft-ontology-unification.md` (e.g., "the faster level must complete many correction cycles before the slower level takes a single step"). However, none of this timescale separation math has been incorporated into the `composition-closure.md` formulation. The spike that originally generated the composition logic (`msc/spike-agent-composition.md`) failed to bridge singular perturbation theory/Tikhonov's theorem into the $\varepsilon^\ast$ closure defect equation, leaving the core mathematical expression stranded at zero-timescale-separation.
