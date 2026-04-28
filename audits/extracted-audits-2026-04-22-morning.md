# Extracted De Novo Audits — 2026-04-22 morning (triple pass)

**Source models:** Codex (OpenAI), Gemini (Google), Opus (Anthropic / fresh local instance)
**Date:** 2026-04-22 (~15:13–15:16Z)
**Session UUID:** `1130893d-5ff9-4446-8d0e-741f1916d65d`
**Record UUIDs:** `2e321395` (Codex paste, line 921), `cfb7c1bd` (Opus paste, line 922), `e262211f` (Gemini re-paste, line 923)

## Context

The morning of 2026-04-22 produced three independent de novo audits (Codex, Gemini, Opus) following the same protocol — audit current `src/`, surface findings with strongest mitigating in-segment counterevidence, then a `msc/` reconciliation pass. These were processed into `audits/pending-findings-2026-04-22.md` (Findings 1–11 by source) and the architectural moves into `msc/architectural-proposals-2026-04-22.md`. The verbatim audit text was not preserved verbatim, however — the pending-findings file is Joseph's structured rewrite. The Gemini "Bigger Picture" architectural moves and Opus's "Bigger-Picture Synthesis" (six structural intuitions, including the *sector-persistence template as the real theory* observation) are particularly worth preserving.

The 2026-04-22 *evening* audit triple (preserved in `audits/audits-2026-04-22-evening.md`) was a separate, post-strengthening-cycle run — different in time and content from this morning batch.

## Disposition

Items here became Findings 1–11 in `audits/pending-findings-2026-04-22.md`. By 2026-04-22 evening, Findings 1, 3, 5, 7, 10, 11, 13 were resolved (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`). The Gemini "Bigger Picture" architectural moves (natural-parameter spaces, variational free energy, Fisher-information unification of tempo/gain) became architectural proposals G-BP1, G-BP2 in `architectural-proposals-2026-04-22.md`. Opus's six structural intuitions became O-BP1 through O-BP6+ in the same proposals file. The "sector-persistence-template as real theory" intuition has since shaped the project's organizing principle of separability/identifiability/forcing meta-segments.

## Verbatim audits Joseph relayed

### Codex audit (line 921, ts 2026-04-22T15:16:08Z)

> Codex:
>
> • I audited the current source corpus in `01-aad-core/src`, active `02-tst-core/src`, and `03-logogenic-agents/src`, and only then checked `msc/` for additional context on issues that already cleared the burden of proof in source. I did not count candidates the repo already narrows well in current source, including the DAG sufficiency-vs-necessity caveat, the unity-dimensions update-homogeneity gap, and the observation-ambiguity architecture-contamination issue.
>
> 1. **Section II silently shifts from agency scope to a narrower learning-purposeful scope.**
>    Problematic passage: `01-aad-core/src/causal-hierarchy-requirement.md:30` says "We restrict attention to learning purposeful agents …" and then "All remaining Section II results operate within learning-agent scope."
>    Strongest counterevidence in src: `01-aad-core/src/scope-condition.md:31` says Section II's purposeful machinery becomes non-vacuous at $S_{\text{agency}}$, and `01-aad-core/src/agent-spectrum.md:46` presents Section II as the right column of actuated agents generally.
>    Assessment: still real.
>    Confidence: high.
>    Why: the narrowing itself is defensible, but it is not integrated as a named Section II-wide sub-scope, so the repo still oscillates between "Section II applies to actuated agents" and "Section II applies to learning purposeful agents."
>    msc context not yet integrated enough: `msc/analysis-2026-04-06.md:265`, `msc/spike-purposeful-agent-derivation.md:648`.
> 2. **The loop is still framed as giving Level 2 access more strongly than the repo's own identification conditions warrant.**
>    Problematic passage: `01-aad-core/src/loop-interventional-access.md:14` says agency-scope agents "gain Level 2 access … through the loop itself," and `01-aad-core/src/loop-interventional-access.md:38` calls the loop "a Level 2 engine."
>    Strongest counterevidence in src: `01-aad-core/src/edge-update-causal-validity.md:26` says intervention-produced data does not automatically yield clean causal identification, and `01-aad-core/src/value-object.md:36` says the remaining requirement is that $M_t$ must actually support $P(o \mid do(a), M_t)$.
>    Assessment: still real.
>    Confidence: medium.
>    Why: the source correctly distinguishes "data generated under intervention" from "identified do-estimates," but the headline language still collapses that distinction too often; in Pearl terms, many agents here have intervention-produced data with regime-dependent identifiability, not unconditional Level 2 knowledge.
>    msc context not yet integrated enough: `msc/spike-purposeful-agent-derivation.md:646`.
> 3. **The practical timescale-separation heuristic in composition still outruns the currently verified bridge conditions.**
>    Problematic passage: `01-aad-core/src/composition-consistency.md:38` calls $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ a "reliable practical test" and says the gap between passing that heuristic and meeting Tier 1 conditions is small in common settings.
>    Strongest counterevidence in src: `01-aad-core/src/composition-closure.md:149` says the general case still has open computability and problem-specification choices, `01-aad-core/src/composition-closure.md:151` makes bridge transfer conditional on the stronger incremental sector bound, and `01-aad-core/src/composition-closure.md:199` still asks for a richer purposeful-agent toy case.
>    Assessment: still real.
>    Confidence: high.
>    Why: the repo has substantially tightened Section III, but the exact bridge is still proved only for restricted classes, while the "common organizational settings" language generalizes beyond the current purposeful-composite evidence base.
>    msc context not yet integrated enough: `msc/spike-bridge-lemma-contraction.md:457`, `msc/working-composition-admissibility.md:454`.
> 4. **TST still overstates git as a complete/clean operational record for AAD quantities.**
>    Problematic passage: `02-tst-core/src/software-epistemic-properties.md:56` says git gives "Exact exteriorized chronica," `:58` says git's scope matches chronica "precisely," and `:62` says environment-side AAD quantities are estimable from the historical record "without the sampling and recall biases that afflict other domains."
>    Strongest counterevidence in src: `01-aad-core/src/chronica.md:15` defines $\mathcal C_t$ as the complete record of observations and actions, `02-tst-core/src/developer-as-act-agent.md:89` lists many software observation channels not captured by git, and `02-tst-core/src/causal-discovery-from-git.md:18` explicitly says the git-to-AAD chain is "empirical and unresolved."
>    Assessment: still real.
>    Confidence: high.
>    Why: git records committed state transitions exactly; it does not record the full software chronica, and its causal use remains materially confounded by shared requirements, bundling conventions, and developer knowledge state.
>    msc context not yet integrated enough: `msc/2026-03-13-feedback.md:80`, `msc/2026-03-14-section-iv-paper-outline.md:60`.
>
> The repo's current state is strongest where it explicitly names approximation ladders and scope restrictions. The remaining weaknesses are mostly not missing caveats in the abstract; they are places where narrower caveats exist elsewhere in the repo but still have not been propagated into the source segments that make the headline claims.

### Gemini audit (line 923, ts 2026-04-22T15:16:08Z)

> Sorry-- this is Geminis-- not sure if the pasting worked correctly earlier:
> Here is a de novo audit of the agentic systems framework based solely on the current `src/` directories, followed by historical reconciliation with `msc/`, and a synthesis of bigger-picture architectural improvements.
>
> ### Finding 1: Unbounded Gradient Updates in Credit Assignment
>
> - **Problematic Passage:**
>   In `01-aad-core/src/credit-assignment-boundary.md`, the default signal function is defined as:
>   $$\text{signal}_k(o_t) = p_k + \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert\mathbf{J}\rVert^2}$$
>   Because this updates a probability $p_k \in [0, 1]$, the formula is mathematically unstable. The denominator $\lVert\mathbf{J}\rVert^2$ (the squared norm of the Jacobian) can become arbitrarily small, especially in deep or highly contingent AND/OR DAGs where edge sensitivities decay toward zero. When $\lVert\mathbf{J}\rVert^2 \to 0$, the signal magnitude explodes to $\pm \infty$. When applied to the update rule $p_k^{\text{new}} = p_k + \eta \cdot (\text{signal} - p_k)$, this will violently push the credences outside the valid $[0, 1]$ probability domain.
> - **Strongest Counterevidence in `src/`:**
>   In `01-aad-core/src/edge-update-via-gain.md`, the theory admits that the gradient candidate "inherits $\hat P_\Sigma$'s overestimation bias under correlated failures" and "requires further validation." However, there is no mention of domain bounds or division-by-zero instability.
> - **Status:** **Still real.** The formula as written in the core theory is mechanically broken for bounded probability parameters. It lacks a link function (like a logit transform) or a clipping mechanism.
> - **Confidence Level:** High.
>
> ---
>
> ### Finding 2: Degenerate Mutual Information in Strategy IB Objective
>
> - **Problematic Passage:**
>   In `01-aad-core/src/strategy-complexity-cost.md`, the theoretical Information Bottleneck objective is defined as:
>   $$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) - \beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)\right]$$
>   Under standard Shannon information theory, the optimal policy $\pi^\ast$ is fully determined by the complete epistemic state $M_t$. Because $\pi^\ast$ is a deterministic function of $M_t$, conditioning on $M_t$ makes $\pi^\ast$ a constant. The mutual information between any variable ($\Sigma_t$) and a constant is strictly zero. Therefore, $I(\Sigma_t;\, \pi^\ast \mid M_t) = 0$, causing the entire objective to degenerate into $\arg\min \operatorname{DL}(\Sigma_t)$, which trivially yields an empty strategy.
> - **Strongest Counterevidence in `src/`:**
>   The text explicitly marks the objective as "formulation/discussion-grade" and admits the term is "not operationalized." It also conceptually explains the term as "how much the strategy helps the agent choose good actions beyond what the model already provides," implying an informal nod toward bounded computation (i.e., it takes work to compute $\pi^\ast$ from $M_t$, and $\Sigma_t$ caches that work).
> - **Status:** **Partially caveated but mathematically broken.** While flagged as "not operationalized," the text does not acknowledge that the formula evaluates to exactly zero.
> - **Confidence Level:** High.
>
> ---
>
> ### Historical Reconciliation: Context from `msc/`
>
> Looking at the spikes in `msc/`, we can see that both of these issues were historically recognized in adjacent ways but the insights failed to make the jump into the clean `src/` formalization:
>
> 1. **For the Unbounded Gradient:**
>    In `msc/spike-credit-assignment-boundaries.md` (Lines 259-263), the original derivation explicitly included a scaling factor: "where $c$ is a normalization constant ensuring the signal lies in $[0,1]$." When this formulation was elevated to `credit-assignment-boundary.md`, the safety constant $c$ was dropped. Furthermore, `msc/spike-gain-sector-bridge-nonlinear.md` exhaustively tests gradient descent on a *logistic loss*, noting that natural parameter spaces (logits) inherently satisfy the sector condition while keeping probabilities bounded. The core theory forgot to map the DAG edge credences to log-odds before applying the continuous gradient update.
> 2. **For the Degenerate IB Objective:**
>    In `msc/spike-kappa-session-residual.md`, there is deep discussion of the "recall cost gradient" and bounded computational budgets ("effort competes with other cognitive demands"). The `msc/` files intuitively understand that computing $\pi^\ast$ from $M_t$ is not free, but the formalization in `src/` uses standard Shannon mutual information, which assumes logical omniscience.
>
> ---
>
> ### The Bigger Picture: Architectural Simplifications and Insights
>
> Zooming out from this audit, the friction in AAD stems primarily from attempting to force three distinct mathematical dialects—**Continuous Control Theory** (ODEs, Lyapunov sectors), **Probabilistic Graphical Models** (AND/OR DAGs, Bayesian updating), and **Information Theory** (Compression, Bottlenecks)—to talk to each other directly without proper translation layers.
>
> Here are some intuitions on how the framework could be made more beautiful, concise, and fundamental:
>
> #### 1. Unify via Natural Parameter Spaces (Logits/Log-odds)
> The tension between the continuous-time mismatch dynamics ($d\delta/dt = -\mathcal{T}\delta$) and the discrete probability DAGs ($p \in [0,1]$) is causing the mechanical breaks (like Finding 1).
> **The Fix:** Never apply additive gradient updates directly to probabilities. If you map all beliefs (edge credences, model states) into their *natural exponential family parameters* (e.g., log-odds), the parameter space becomes $\mathbb{R}^n$. Once in $\mathbb{R}^n$, the continuous control theory (mismatch ODEs, Lyapunov stability, sector conditions) works flawlessly and beautifully. The "normalization constant" hacks disappear.
>
> #### 2. Reframe the Strategy DAG as a Variational Approximation
> Finding 2 highlights that Shannon information theory breaks down when you try to model the "cost of thinking." If $M_t$ knows everything, $\Sigma_t$ is mathematically redundant.
> **The Fix:** Borrow from Variational Inference. Reframe the strategy $\Sigma_t$ not as an information bottleneck of the history, but as a *variational approximation* of the true, intractable optimal policy $\pi^\ast$.
> The cognitive cost of a strategy (Description Length) becomes the *KL-divergence* between the tractable DAG structure and the true combinatorial policy space. This automatically solves the degeneracy: the agent minimizes Variational Free Energy, balancing the expected reward of the plan against the informational cost of maintaining the DAG constraints.
>
> #### 3. Collapse "Tempo" and "Gain" into Fisher Information
> Currently, the theory treats $\mathcal{T}$ (Tempo) and $\eta^\ast$ (Update Gain) as semi-independent scalar constructs. But as hinted in `msc/prior-tf-citations-catalog.md` (Amari's Natural Gradients), the optimal turning rate in a probabilistic space is governed by the Fisher Information Matrix.
> **The Fix:** If you define the agent's mismatch $\delta$ in terms of KL-divergence between the model and reality, the "Sector Condition" and "Update Gain" mathematically collapse into a single concept: Natural Gradient Descent. $\mathcal{T}$ stops being a heuristic scalar and becomes the projection of the environment's drift rate onto the agent's Fisher Information manifold. This generalizes the theory effortlessly to $N$-dimensional anisotropic environments without needing separate "per-dimension" caveats.

### Opus audit (line 922, ts 2026-04-22T15:16:08Z) — full verbatim

> Opus:
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
