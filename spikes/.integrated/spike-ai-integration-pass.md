# Spike: Active Inference Integration Pass

**Status**: Spike — proposed integration text for review. No segments edited.

**Date**: 2026-04-22

**Trigger**: AI vs AAD positioning spike (`spikes/spike-active-inference-vs-aad.md`) §H identified two overlap-underclaim findings: (Overlap 1) `#der-loop-interventional-access` overlaps more with implicit AI content than acknowledged; (Overlap 2) compression operations and AI's hierarchical generative models share more than `#disc-compression-operations` acknowledged. The same spike's §I action 1 recommended executing G-BP2 V-medium (variational form of strategy-cost objective; closes Gemini Finding 2). Joseph's directive (2026-04-22): "prioritize properly integrating AI into the discussion (and even formalization or as an equivalent formulization etc., with footnote citations as you see for a few other papers)."

This spike produces ready-to-apply proposed text for the integration. Each section gives the proposed segment-level edit and the rationale.

**Read alongside.** The AI vs AAD positioning spike is the load-bearing reference document — its §B mapping table, §C distinctive claims, §D refusals, §E G-BP2 verdict, §F reviewer Q&A, and §H underclaim/overlap findings are the substantive backbone. This spike implements the segment-level changes those findings imply.

---

## 1. Citation Convention

**Current AAD convention.** Inline prose author-year. External theorems are named in prose with citation (e.g., `#der-causal-hierarchy-requirement` cites "Bareinboim et al. 2022"; `#form-information-bottleneck` cites "Tishby, Pereira & Bialek 1999" and "Cover & Thomas §I.12–13"; `#der-causal-hierarchy-requirement` cites "Hafez et al. 2026"; `#form-strategy-complexity-cost` cites "Miller 2022 Table 12.2"). Only one segment currently cites the AI literature: `#disc-ciy-unified-objective` line 54 has a "Connection to active inference" paragraph mentioning the FEP and EFE without formal citation.

**Proposal for this pass.** Continue inline prose author-year for all AI integrations. The "footnote citations" framing in Joseph's directive likely refers to "auxiliary citations that don't disrupt the main argument" rather than literal footnotes; the existing convention satisfies that read. If Joseph wants explicit footnote markup (e.g., a numbered references block at the bottom of each segment), the integration text below is easy to convert; for now I produce inline prose to match the existing convention and avoid format drift.

**Reference shorthand.** Throughout this spike I use abbreviated references — full forms collected in §6 below. These can be expanded in segment text or kept terse depending on the segment's existing density.

---

## 2. Phase A — G-BP2 V-Medium Implementation (Formalization-Level Integration)

The AI vs AAD spike §E.6 specified the V-medium move: replace Shannon mutual information in the strategy-IB objective with a KL-divergence to the optimal-policy posterior, resolving Gemini Finding 2 (Shannon zero-MI degeneracy under deterministic $\pi^\ast$) and bringing AAD into clean dialogue with AI's variational machinery without committing to preferences-as-priors or EFE-as-master-objective.

### 2.1 `#form-strategy-complexity-cost` — primary edit

**Affected subsection.** "Strategy IB objective" (lines 34–55).

**Current theoretical form** (line 42):

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) - \beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)\right]$$

**Issue.** When $\pi^\ast$ is a deterministic function of $M_t$ (the standard scope), $I(\Sigma_t; \pi^\ast \mid M_t) = 0$ identically (Shannon MI to a constant is zero). The objective collapses to $\arg\min \operatorname{DL}(\Sigma_t)$ — trivially the empty strategy. This is Gemini Finding 2.

**Proposed revised theoretical form:**

> *[Formulation (strategy-IB-objective-variational)]*
>
> The strategy is a tractable variational approximation of the optimal-policy posterior $Q^\ast(\pi \mid M_t)$. The strategy-cost objective in variational form:
>
> $$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(Q_{\Sigma_t}(\pi \mid M_t) \,\big\|\, \pi^\ast(\cdot \mid M_t)\bigr) \,\right]$$
>
> where $Q_{\Sigma_t}(\pi \mid M_t)$ is the action-distribution induced by the strategy DAG given the current model state, and $\pi^\ast(\cdot \mid M_t)$ is the optimal-policy reference. The KL-divergence is well-defined when $\pi^\ast$ is deterministic-from-$M_t$ — it measures how far the agent's tractable strategy departs from the optimum, including cases where $Q_{\Sigma_t}$ places mass on suboptimal actions (the suboptimality cost is then unbounded if $\pi^\ast$ is a point mass and $Q_{\Sigma_t}$ has support elsewhere; in practice the KL is regularized by $Q_{\Sigma_t}$'s own diffuseness).
>
> This variational form is the strategy-layer analog of variational free energy minimization in active inference (Friston 2017; Da Costa et al. 2020; Sajid et al. 2021; Parr & Pezzulo 2022). AAD borrows the variational form as the appropriate generalization of the Shannon-MI relevance term — Shannon $I(\Sigma_t; \pi^\ast \mid M_t)$ vanishes when $\pi^\ast$ is deterministic, and the KL form captures what the original mutual-information term was reaching for: distance between the strategy-induced policy and the policy-relevant target. AAD adopts the form without committing to preferences-as-priors (AI's $C(o) = \log P_{\mathrm{pref}}(o)$ encoding — AAD's $O_t$ remains a value functional on trajectories per #form-objective-functional) or to expected free energy as master objective (AAD's CIY-unified objective is a related but distinct decomposition — see #disc-ciy-unified-objective).
>
> **Operational form unchanged.** The DL surrogate for $I(\mathcal C_t; \Sigma_t)$ remains as in the previous subsection; the operational minimization replaces $\beta_\Sigma \cdot D_{\mathrm{KL}}$ with a sample-based estimate (a per-edge calibration discrepancy weighted by decision-relevance — see #disc-credit-assignment-boundary for the gradient form). The two forms agree in the limit where the DAG encoding is rate-distortion optimal and the policy posterior is sample-recoverable.

**Why this works.** Replaces the structurally broken Shannon-MI term with a well-defined KL term. The KL form is the standard variational object in active inference, so the fix simultaneously closes the finding and opens the literature connection. The operational form needs only a sample-based estimator update, not a structural change.

**Update to Epistemic Status (line 121):** add a sentence:

> The variational form replaces the Shannon-MI relevance term with KL-divergence to the optimal-policy posterior, fixing the Shannon-zero degeneracy that arises when $\pi^\ast$ is deterministic-from-$M_t$. The form is the strategy-layer analog of variational free energy minimization in active inference (Friston 2017; Parr & Pezzulo 2022); AAD borrows the form without committing to AI's preferences-as-priors or EFE-as-master-objective stances (see `spikes/spike-active-inference-vs-aad.md` §E for the tier-strength analysis on this borrowing).

### 2.2 `#disc-compression-operations` — synthesis update

**Affected subsections.** "Strategy compression: source reformulation" (lines 39–62) and "What stays separate from the IB frame" (lines 82–90).

**Proposed insertion** at end of §"Strategy compression: source reformulation" (after line 62):

> **Variational form.** The Shannon mutual information $I(\mathcal C_t; \Sigma_t)$ in the source term and $I(\Sigma_t; \pi^\ast \mid M_t)$ in the relevance term can both be replaced with KL divergences to make the objective robust to deterministic $\pi^\ast$ (Gemini Finding 2; see #form-strategy-complexity-cost variational subsection). The variational form aligns the strategy compression with the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ in active inference (Friston 2017; Da Costa et al. 2020): under the AI variant, the AAD $\Sigma_t$ is a tractable approximation of the policy-relevant posterior, and the KL term measures approximation quality. The shared-IB-shape framing of the four AAD compression operations is the rate-distortion specialization of this variational picture; AAD's commitment is to the rate-distortion form (which gives the (P1) Lagrangian-dual derivation and the four-instance unification at U-medium), not to the full variational free-energy interpretation.

**Update to "What stays separate" subsection** (line 87 about interventional relevance — already mentions "causal IB, Wieczorek & Roth 2017"). Extend the paragraph:

> Causal IB extension (Wieczorek & Roth 2017 and follow-ups) is the natural framework for Regime A edges, but is also a known frontier in the AI literature itself (active-inference work has not extensively engaged with Pearl-Level-2 relevance variables). The cross-engagement is an open research direction common to both lineages — see `spikes/spike-active-inference-vs-aad.md` §G.1.

### 2.3 `#disc-exploit-explore-deliberate` — Discussion cross-reference

**Affected location.** Discussion section (after the current "Control regret as deliberation ceiling" subsection, line ~80).

**Proposed insertion** as new Discussion subsection:

> **Connection to active inference.** The exploit/explore decomposition maps cleanly onto the expected free energy (EFE) decomposition into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states) in active inference (Friston 2017; Da Costa et al. 2020 §2.4; Sajid et al. 2021). Under the mapping, AAD's exploit term $Q_O$ corresponds to EFE's pragmatic value when the value functional $V_{O_t}$ is read as expected log-preferences, and AAD's CIY corresponds to EFE's epistemic value when the relevance variable is read as the hidden-state posterior. The structural correspondence is U-medium in the IB-unification spike's vocabulary (`spikes/spike-ib-unification-plan.md` §1.2): shared shape, not unified objective. AAD does *not* commit to AI's preferences-as-priors form (preserving the satisfaction-gap diagnostic in #def-satisfaction-gap, which the priors-as-preferences collapse would erase — see `spikes/spike-active-inference-vs-aad.md` §C.2).
>
> **Deliberation as recursive policy reasoning.** The deliberation axis — internal exploration in model-space rather than environment-space — is structurally adjacent to "sophisticated active inference" (Friston, Da Costa, Hafner, Hesp & Parr 2021), which handles bounded computation via recursive expected free energy with depth-limited belief-about-belief reasoning. AAD's machinery for deliberation cost (#der-deliberation-cost) and extended deliberation threshold above derives the same trade-off via per-edge persistence and evidence starvation, with the structural advantage that the depth bound $d^\ast$ is causally derived from the strategy DAG rather than from belief-recursion depth. The two frameworks address the same problem with different machinery; AAD can credit the AI lineage as a co-developed alternative.

### 2.4 `#disc-ciy-unified-objective` — extend existing AI mention

**Affected location.** Discussion subsection "Connection to active inference" (line 54).

**Current text:**

> The Free Energy Principle's "expected free energy" decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking). AAD's formulation is structurally isomorphic: expected value ≈ extrinsic, CIY ≈ epistemic. Whether this convergence is deep or superficial is an open question. AAD grounds exploration in explicitly *causal* information rather than entropy reduction — not all uncertainty reduction is equally valuable; causal information specifically enables better *intervention*.

**Proposed expansion:**

> **Connection to active inference.** The expected free energy (EFE) in active inference (Friston 2017; Da Costa et al. 2020; Sajid et al. 2021) decomposes into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states). AAD's unified objective is structurally isomorphic: $Q_O$ ≈ pragmatic, CIY ≈ epistemic. The convergence is at the U-medium level in the IB-unification spike's vocabulary — shared shape (objective decomposes into value-and-information terms), not unified content. Two substantive differences remain. First, AAD grounds exploration in explicitly *causal* information (action-distinguishability under $do$) rather than entropy reduction over hidden states — not all uncertainty reduction is equally valuable for purposeful action; causal information specifically enables better *intervention* (see #der-causal-hierarchy-requirement; the gap between CIY and proper expected information gain is logged in this segment's Epistemic Status as a known surrogate). Second, AAD does not encode preferences as priors over outcomes ($C(o) = \log P_{\mathrm{pref}}(o)$ in the AI form): AAD's $O_t$ is a value functional on trajectories (#form-objective-functional), and the satisfaction-gap / control-regret diagnostic in #def-satisfaction-gap, #def-control-regret depends on this distinction — the diagnostic structure does not survive the priors-as-preferences collapse (Sun & Firestone 2020 dark-room critique; see `spikes/spike-active-inference-vs-aad.md` §C.2 for the analysis).

---

## 3. Phase B — §H Overlap Integrations

The AI vs AAD spike's §H Overlap 1 and Overlap 2 are the explicit findings Joseph's directive points at. Both call for honest acknowledgment that AAD overlaps with AI more than the project currently states, while preserving and articulating AAD's distinctive additions.

### 3.1 `#der-loop-interventional-access` — Overlap 1 integration

**Affected location.** Discussion section (after "Even agents without explicit causal models benefit," line ~47).

**Finding (AI spike §H Overlap 1).** "The substantive observation (the agent's actions cause its observations, so loop data is intervention-generated) is implicit in any agent-environment loop framing, including AI's. AAD's distinctive contribution is naming this as a load-bearing theorem and connecting it to Pearl Level 2 via Bareinboim et al. (2022). The framing is distinctive; the substantive content is closer to shared than current AAD treatment suggests. Honest credit to AI's implicit treatment is appropriate."

**Proposed Discussion addition:**

> **Honest credit to the action-perception-loop framing.** The substantive observation that the agent's actions cause its observations — and therefore that loop data is interventional in character — is implicit in any framework built around an action-perception loop, including active inference (Friston 2017 §2; Parr & Pezzulo 2022 ch. 3) and the broader cybernetic-and-control lineage (Wiener 1948; Conant & Ashby 1970 — "every good regulator of a system must be a model of that system"). AAD's distinctive contribution is not the observation that loop data is interventional but the *explicit lift* of this observation to a load-bearing theorem connected to Pearl's causal hierarchy (#def-pearl-causal-hierarchy) via Bareinboim, Correa, Ibeling & Icard (2022). Three specific moves AAD makes that the implicit treatments do not:
>
> 1. **The Bareinboim-hierarchy connection.** Active inference and the cybernetic lineage rest on Bayesian-network generative models (Pearl Level 1, associational). They do not invoke the causal-hierarchy theorem to argue that the loop's action-generated data is the substrate Level-2 queries require. AAD does — and the consequence is that $\Sigma_t$ is positioned as a *causal* DAG rather than a *Bayesian-network* DAG.
>
> 2. **Regime-indexed strength of causal identification.** Even granting that loop data is interventional in character, the strength of usable causal identification varies by domain. AAD partitions this into Regime A (intervention-rich, software/laboratory), B (partial intervention, organizational), C (observation-only — see #scope-edge-update-causal-validity). The AI literature treats causal identifiability uniformly within its modeling assumptions and does not surface the regime distinction at the segment level.
>
> 3. **Explicit scope honesty.** This segment carefully distinguishes "data generated under intervention" from "cleanly identified do-estimates" (see Formal Expression). The AI literature, as Bruineberg, Dolega, Dewhurst & Baltieri (2022) document in their Pearl-vs-Friston critique, sometimes elides this distinction — using the action-perception loop language to support stronger causal claims than the formal apparatus delivers. AAD's careful split is the conservative form.
>
> The reframing here is rhetorical, not substantive: the headline result (the loop is a Level-2 engine) stays; what changes is the explicit acknowledgment that the observation about loop data being action-generated is shared with the broader literature. AAD's distinctive content sits in the three specific moves above, which are the load-bearing differences.

**Working Notes update.** Add to the existing Working Notes:

> - **Cross-segment connection to AI engagement.** This honest-credit framing is part of the broader AI integration described in `spikes/spike-active-inference-vs-aad.md` §H Overlap 1. The companion underclaim move on #der-directed-separation (Pearl-blanket vs. Friston-blanket form of Markov blanket; see `spikes/spike-active-inference-vs-aad.md` §H Underclaim 2) makes AAD's conservative-form positioning visible across both architectural and access-channel segments.

### 3.2 `#disc-compression-operations` — Overlap 2 integration

**Already partially addressed in Phase A §2.2 above** (the variational-form insertion). Additional explicit acknowledgment needed in the Discussion:

**Affected location.** Discussion section, after "Why not go further" subsection (around line 102).

**Proposed Discussion subsection:**

> **Honest credit to the hierarchical-generative-model lineage.** AAD's four compression operations are a structurally narrower family than the operations a hierarchical generative model in the predictive-coding lineage (Friston 2008, 2010; Clark 2013; Hohwy 2013) could express. A hierarchical generative model layers compressions of compressions, with each layer producing a representation tuned to the next layer's prediction target — and the AAD compressions ($M_t$ for prediction, $\Sigma_t$ for guidance, shared intent for coordination, $\Lambda$ for level-bridging) are all expressible within that frame as specific layer-bindings. What AAD adds is structural: (a) the *relevance variables* $Y$ are made first-class with explicit per-instance bindings ($o_{t+1:\infty} \mid a$, $\pi^\ast \mid M_t$, $a^{\text{coordinated}}$, $o_{\text{micro},t+1} \mid a_{\text{micro}}$ — see the table in §"The shared IB shape"); (b) the (P1)–(P3) admissibility conditions for composition give a measurable closure-defect bound that hierarchical-generative-model layering does not natively produce (#form-composition-closure); (c) regime-indexed edges (#scope-edge-update-causal-validity) introduce Pearl-Level-2 relevance for Regime A, which standard hierarchical generative models do not address. The shared family is real; AAD's additions are also real. The honest framing is "AAD's compressions are a structured subset of the hierarchical-generative-model family with additional structure load-bearing for AAD's specific results."

---

## 4. Phase C — §H Underclaim Positioning

The AI vs AAD spike's §H Underclaims 1, 2, 3 identify three places where AAD currently *under*claims its distinctive contributions. The fix is rhetorical positioning, not theoretical change — naming the distinctive moves where they are load-bearing, with citations to the AI critiques that motivate the conservative-form reading.

### 4.1 `#result-sector-persistence-template` — Underclaim 1: broader validity than FEP-flow

**Affected location.** Epistemic Status (line ~68) or Discussion section (after "Instantiations in AAD").

**Proposed Discussion subsection** (insert after the "Instantiations in AAD" table and before Epistemic Status):

> **Comparison with the FEP-flow stability argument.** Active inference's stability arguments come from the geometry of the variational free-energy landscape — agents are argued to flow toward the minimum of variational free energy on a non-equilibrium-steady-state (NESS) density (Friston 2019; Friston, Da Costa et al. 2023). Aguilera, Millidge, Tschantz & Buckley (2022) showed that this argument's mathematical validity is narrow: the NESS-density framing for the FEP-flow holds only in a small parameter regime for non-equilibrium linear stochastic systems, and natural extensions (nonlinear, non-Gaussian, non-equilibrium) often fall outside the proven regime. The AAD persistence template is structurally different: it is a Lyapunov-based argument requiring only (T1) zero-correction-at-zero-state, (T2) local sector condition (correction points inward), and (T3) bounded disturbance — all of which are checked locally for each instantiation (#deriv-sector-condition Props A.1, A.1S, A.2). The template applies to bounded and to mean-square-stochastic disturbance, gives explicit ultimate-bound and adaptive-reserve formulas, and does not depend on NESS structure or on a free-energy gradient. The breadth difference is not rhetorical: where the FEP-flow argument's parameter regime is debated in the AI literature itself, the sector-Lyapunov apparatus is the standard machinery of nonlinear control theory (Khalil 2002 Ch. 4) and applies wherever (T1)–(T3) hold. This is one of AAD's stronger structural positions and is worth making explicit when comparing AAD to active inference.

**Working Notes update:**

> - **Cross-segment positioning.** This comparison surfaces the broader-validity advantage flagged in `spikes/spike-active-inference-vs-aad.md` §H Underclaim 1. The cite to Aguilera et al. 2022 and Friston 2019 anchors the comparison in the AI literature's own self-critique rather than in an external attack on active inference.

### 4.2 `#der-directed-separation` — Underclaim 2: Pearl-blanket form

**Affected location.** Discussion section (the existing "Why the classification is not a smooth parameter" subsection or a new subsection after it).

**Proposed Discussion subsection:**

> **Directed separation as the conservative form of the Markov blanket.** The Markov blanket apparatus from active inference (Friston 2013, 2019; Friston, Da Costa et al. 2023) provides the same statistical-conditional-independence machinery the directed-separation condition above invokes. Bruineberg, Dolega, Dewhurst & Baltieri (2022, "The Emperor's New Markov Blankets") distinguish two readings of the Markov-blanket apparatus in the AI literature: a **Pearl-blanket** reading — the technical conditional-independence statement, well-defined and substantively informative — and a **Friston-blanket** reading — the metaphysical claim that Markov blankets demarcate self-from-other and that every self-organizing system has one ontologically. Bruineberg et al. argue that the Friston-blanket reading overruns what the formalism delivers: the conditional-independence statement does not by itself license the metaphysical demarcation.
>
> AAD's directed-separation condition is structurally a Pearl-blanket move: the architectural classification (Class 1 / Class 2 / Class 3) names the conditional-independence structure of the agent's processing graph, with explicit operational measurement $\kappa_{\mathrm{processing}}$, and admits the structure *fails* by construction for Class 2 architectures (transformer LLMs, where attention processes goals and observations together). The classification's explicit failure mode for Class 2 is the scope honesty Bruineberg et al. argue the Friston-blanket reading lacks. AAD adopts the Pearl-blanket conditional-independence statement as the technical content of directed separation; AAD does not adopt the Friston-blanket metaphysical reading. The architectural classification, the operational $\kappa$, and the explicit Class 2 scope exit (with the coupled formulation handed off to `03-logogenic-agents/`) are AAD's load-bearing additions to the Pearl-blanket form.
>
> Two consequences worth surfacing for reviewers. First: the question "isn't directed separation just the Markov blanket?" has the answer "directed separation is the *Pearl-blanket form*; it is also the architectural-classification refinement that the standard Markov-blanket framing does not produce." Second: AAD's scope honesty about Class 2 (Section II's exact results do not apply; logogenic agents need the coupled formulation) is itself an *answer* to the Bruineberg critique — AAD's apparatus admits where it fails, while the Friston-blanket framing is contested precisely because it does not.

**Update to Epistemic Status** (current text says "Conditional"). Append:

> The Pearl-blanket vs. Friston-blanket distinction (Bruineberg et al. 2022) is the literature signal that motivates AAD's conservative form: directed separation is the conditional-independence statement with explicit architectural scope and operational measurement, not a metaphysical demarcation of self-from-other.

### 4.3 `#def-satisfaction-gap` and `#def-control-regret` — Underclaim 3: diagnostic content

**Affected segments.** Both `#def-satisfaction-gap` and `#def-control-regret` Discussion sections. The integration is parallel; one paragraph in each.

**Proposed Discussion subsection (for `#def-satisfaction-gap`):**

> **Diagnostic content vs. AI's expected-free-energy decomposition.** Active inference's expected free energy (EFE) decomposes into *pragmatic value* (how preferred are the outcomes the policy expects?) and *epistemic value* (how much does the policy reduce uncertainty?) (Friston 2017; Da Costa et al. 2020 §2.4; Sajid et al. 2021). The decomposition supports policy ranking but does not separate two distinct diagnoses that AAD's apparatus does separate: "the goal is unattainable from here" ($\delta_{\mathrm{sat}} > 0$, this segment) versus "the current policy is not the best available" (the $\delta_{\mathrm{regret}} > 0$ companion in #def-control-regret). Both increase EFE without distinguishing the cause. The 2×2 cell map in this segment's Discussion (low/high $\delta_{\mathrm{sat}}$ × low/high $\delta_{\mathrm{regret}}$) gives the four diagnoses the orient cascade (#der-orient-cascade) acts on differently — strategy revision, objective revision, action vs. learning. AI's pragmatic-epistemic split does not produce this disambiguation. The diagnostic structure depends on $V_{O_t}$ being a *value functional* on trajectories (#form-objective-functional) and $A_O$ being an *attainability supremum*, not on outcomes encoded as log-priors — AI's preferences-as-priors form ($C(o) = \log P_{\mathrm{pref}}(o)$) collapses the diagnostic by making "wanting $o$" and "expecting $o$" formally the same operation (Sun & Firestone 2020 "dark room" critique). AAD's value-functional framing is what makes the diagnostic available; this is a deliberate divergence from AI, not an oversight (see `spikes/spike-active-inference-vs-aad.md` §C.2 and §D.1).

**Proposed Discussion subsection (for `#def-control-regret`):** essentially the same paragraph as above with focus on $\delta_{\mathrm{regret}}$'s role in the 2×2 — a brief cross-reference to `#def-satisfaction-gap`'s expanded discussion is sufficient to avoid duplication. Joseph's call on whether the duplication is worth it for reader-navigation reasons.

---

## 5. Phase D — Discussion-Level Cross-References

Smaller integrations in segments where the AI connection is real but the segment is not load-bearing for either an underclaim or an overlap finding.

### 5.1 `#form-information-bottleneck` — VFE accuracy-complexity equivalence

**Affected location.** Discussion section (after "Broader applicability," line ~42).

**Proposed Discussion paragraph:**

> **Connection to variational free energy.** The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference (Friston 2010, 2017; Parr & Pezzulo 2022 ch. 2): the compression cost $I(M_t; \mathcal{C}_t)$ is the complexity term (KL between posterior and prior over latent states); the negative predictive power $-I(M_t; o_{t+1:\infty})$ is the accuracy term (negative expected log-likelihood). The two formulations are mathematically equivalent under the Markov-chain factorization $Y - X - T$ (see Tishby & Zaslavsky 2015 for the deep-learning instantiation, which connects the two literatures explicitly). AAD adopts the IB form as the rate-distortion characterization of optimal compression; the variational free-energy form is the AI-side cousin and motivates the variational treatment of strategy compression in #disc-compression-operations and #form-strategy-complexity-cost.

### 5.2 `#def-shared-intent` — IB-form-already-present

The segment already writes its objective in IB form and cites Tishby. No new integration needed — but a brief AI cross-reference paragraph would parallel the integrations elsewhere. **Joseph's call on whether to include or skip.**

---

## 6. Reference Bibliography

Full forms of references used above. AAD's existing convention does not maintain a per-segment bibliography — citations are in prose only. This bibliography is for the spike's reference; per-segment placements above use abbreviated inline forms.

**Active inference / Free Energy Principle (primary):**
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience* 11: 127–138.
- Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., Pezzulo, G. (2017). Active inference: a process theory. *Neural Computation* 29: 1–49.
- Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V., Friston, K. (2020). Active inference on discrete state-spaces: a synthesis. *Journal of Mathematical Psychology* 99: 102447.
- Sajid, N., Ball, P. J., Parr, T., Friston, K. J. (2021). Active inference: demystified and compared. *Neural Computation* 33: 674–712.
- Parr, T., Pezzulo, G., Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Friston, K., Da Costa, L., Hafner, D., Hesp, C., Parr, T. (2021). Sophisticated inference. *Neural Computation* 33: 713–763.

**FEP foundations and extensions:**
- Friston, K. (2013). Life as we know it. *Journal of the Royal Society Interface* 10: 20130475.
- Friston, K. (2019). A free energy principle for a particular physics. arXiv:1906.10184.
- Friston, K., Da Costa, L., Sakthivadivel, D. A. R., Heins, C., Pavliotis, G. A., Ramstead, M., Parr, T. (2023). Path integrals, particular kinds, and strange things. *Physics of Life Reviews* 47: 35–62.
- Friston, K. (2008). Hierarchical models in the brain. *PLoS Computational Biology* 4: e1000211.
- Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences* 36: 181–204.
- Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press.

**FEP critiques (essential — AI is contested within its own community):**
- Aguilera, M., Millidge, B., Tschantz, A., Buckley, C. L. (2022). How particular is the physics of the free energy principle? *Physics of Life Reviews* 40: 24–50.
- Bruineberg, J., Dolega, K., Dewhurst, J., Baltieri, M. (2022). The Emperor's New Markov Blankets. *Behavioral and Brain Sciences* 45: e183.
- Andrews, M. (2021). The math is not the territory: navigating the free energy principle. *Biology & Philosophy* 36: 30.
- Colombo, M., Wright, C. (2021). First principles in the life sciences: the free-energy principle, organicism, and mechanism. *Synthese* 198: 3463–3488.
- Litwin, P., Miłkowski, M. (2020). Unification by fiat: arrested development of predictive processing. *Cognitive Science* 44: e12867.
- Gershman, S. J. (2019). What does the free energy principle tell us about the brain? *Neurons, Behavior, Data Analysis, and Theory* 2: 1–10.
- Sun, Z., Firestone, C. (2020). The dark room problem. *Trends in Cognitive Sciences* 24: 346–348.

**Causal inference (already cited in AAD, listed for completeness):**
- Bareinboim, E., Correa, J. D., Ibeling, D., Icard, T. (2022). On Pearl's hierarchy and the foundations of causal inference. In *Probabilistic and Causal Inference: The Works of Judea Pearl*: 507–556.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

**Causal IB extension (open research direction):**
- Wieczorek, A., Roth, V. (2017). Causal compression. arXiv:1611.00261.

**Cybernetic-and-control lineage (for #der-loop-interventional-access overlap acknowledgment):**
- Wiener, N. (1948). *Cybernetics: or Control and Communication in the Animal and the Machine*. MIT Press.
- Conant, R. C., Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science* 1: 89–97.
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. [Standard reference for Lyapunov machinery.]

**Information theory (already cited in AAD, listed for completeness):**
- Tishby, N., Pereira, F. C., Bialek, W. (1999). The information bottleneck method. *Proc. 37th Allerton*.
- Tishby, N., Zaslavsky, N. (2015). Deep learning and the information bottleneck principle. *IEEE ITW*.
- Cover, T. M., Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

---

## 7. Open Questions for Joseph

1. **Citation format.** I've used inline prose author-year throughout, matching AAD's existing convention (Bareinboim 2022, Tishby 1999, Hafez 2026, etc.). Your directive mentioned "footnote citations as you see for a few other papers." If you intend literal footnote markup (numbered references at the bottom of segments), the inline citations above convert easily. The current convention's downside: AI integrations are dense in citations, which may visually clutter the prose. Recommend continuing inline; flag for your decision.

2. **Phase A vs Phase B vs Phase C ordering for execution.** All three phases are independent. My recommended order is Phase A first (G-BP2 V-medium closes Gemini Finding 2 and is recommended action 1 in the AI vs AAD spike); Phase B second (Overlap integrations are honesty work and unlock further claims); Phase C third (Underclaim positioning is rhetorical and benefits from the Phase B groundwork). Phase D is opportunistic — execute alongside any of the others.

3. **Strategy IB objective in `#form-strategy-complexity-cost`.** Phase A §2.1 *replaces* the Shannon-MI relevance term with KL. The DL form for the source term (operational) and $I(\mathcal{C}_t; \Sigma_t)$ for the source term (theoretical) both stay. The variational form for the relevance is the substantive change. Confirm this is the right scope — alternative is to also reformulate the source term variationally, but that escalates beyond the V-medium move's purpose.

4. **Duplicated AI-engagement paragraph in `#def-satisfaction-gap` and `#def-control-regret`.** I drafted full text for `#def-satisfaction-gap` and proposed a brief cross-reference for `#def-control-regret`. Alternative: full duplication in both for reader-navigation; or full text in `#def-satisfaction-gap` only with a single-sentence pointer in `#def-control-regret`. Your call.

5. **`#def-shared-intent` AI cross-reference.** The segment already writes its objective in IB form and cites Tishby. A brief AI cross-reference paragraph would parallel the other segments. Worth adding for consistency, or skip because the segment is already AI-aligned in form?

6. **Honest dissenting note from AI vs AAD spike §H also recommends paper-introduction-level positioning** (see AI vs AAD spike §I action 2). That work is *paper-writing-time*, not segment-time; flagged for the right moment but not in this spike's scope.

7. **Cross-references to AI in MIGRATION-MAP.md, OUTLINE.md preambles, or LEXICON.md?** The integration above is segment-level. Should the OUTLINE Section II preamble also acknowledge the AI lineage? CLAUDE.md's "Theory Character" section currently says nothing about AI. These higher-level edits are out of this spike's scope but flag-worthy.

8. **Effort to apply.** Phase A: 1–2 sessions for `#form-strategy-complexity-cost` rewrite + cross-segment touches. Phase B: 1 session for `#der-loop-interventional-access` and `#disc-compression-operations` updates. Phase C: 1–2 sessions for the three positioning moves (the prose is drafted; mostly insertion + frontmatter touches). Phase D: 30 min. Total: 3–5 sessions if executed comprehensively; smaller if you want to land subsets.

---

## 8. What This Spike Does Not Touch

- **Foundational ontology.** No claim is changed about what AAD *is* — only how it is positioned and cross-referenced. The §H Underclaim moves in Phase C make AAD's distinctive content visible against AI; they do not change the content.
- **The G-BP2 vs O-BP2 tension.** AI vs AAD spike §G.4 notes the two architectural proposals are compatible, and the V-medium move on G-BP2 (Phase A) is independent of O-BP2's (deferred) compressions-as-projections move. Joint adoption would push AAD closer to AI's framing than either alone; the AI vs AAD spike flags this as a paper-writing-time decision.
- **The deeper `causal IB extension` for Regime A edges.** Logged as open research direction in Phase A §2.2 and AI vs AAD spike §G.1; not implemented here.
- **OUTLINE.md, CLAUDE.md, LEXICON.md cross-references to AI.** Out of scope for this spike (open Q 7).
- **Active engagement with continuous-state active inference** (vs. the discrete-state form used as the cleanest reference throughout). Logged as open in AI vs AAD spike's Working Notes; not implemented here.
