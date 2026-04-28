# De Novo Audit of `01-aad-core/`

**Date:** 2026-04-21
**Reviewer:** Claude Opus 4.7 (1M context)
**Scope:** current state of `01-aad-core/src/`, plus integration gaps against `msc/` spikes for the issues that survived the burden-of-proof test

## Method

Audit ground rules, as set by Joseph:

- Evaluate only the current repository state. No "fixed" or "resolved" labels without a supplied baseline.
- For each finding, produce the problematic passage, the strongest available mitigating passage elsewhere in `src/`, and an explicit reconciliation. A finding only counts if the issue still stands after that reconciliation.
- Do not import concerns from `msc/` unless they relate to a finding that has already passed the burden-of-proof test. For legitimate findings, check `msc/` for content that would address the finding but has not yet been fully integrated into the segments.

I read the segments that make the strongest claims or that `OUTLINE.md` marks as load-bearing: the scope conditions, directed separation, the persistence results (I + II + III + composition), the orient cascade, the strategy-DAG machinery with its Correlation Hierarchy, composition closure with its bridge lemma, the unity/closure mapping, adversarial dynamics, and the edge-semantics scope segment. For each surviving finding I then opened the spike(s) that appeared to address it.

Four findings survive. Several candidate issues dissolved under the burden-of-proof test; those are listed at the end with a brief note on why.

---

## Finding 1 — The orient cascade's "default operational signal" is a calibration target that is biased by construction under realistic DAGs

### Problematic passage

`orient-cascade.md` step 4a:

> $\delta_s$ is credit-assignment-free (requires only status propagation), and its persistence is proved ( #schema-strategy-persistence, Prop B.5 in #deriv-strategic-dynamics). This is the **default operational signal**: AAD's formal guarantees require only plan-level tracking ( #disc-credit-assignment-boundary, Level 0).

`credit-assignment-boundary.md`, the hierarchy-of-quality table:

> **0** (none) — Plan-level tracking only — Persistence guarantee (Prop B.5) — No per-edge diagnostics

These two segments together position plan-confidence tracking as the cascade's minimum-viable diagnostic, with the theory's formal guarantees inherited from Prop B.5.

### Strongest mitigating passages

`strategy-dag.md` Correlation Hierarchy:

> $\hat P_\Sigma$ systematically overestimates success because the AND/OR propagation treats joint failure probability as the product of marginals.

`strategic-dynamics-derivation.md`, note under Prop B.5:

> $\Phi$ is NOT the actual probability of plan success when edge outcomes are correlated ... What $\delta_s$ tracks is calibration *within the independence model*, not calibration to reality.

`strategy-persistence-schema.md`:

> $\delta_s$ ... operates at L0 of the Correlation Hierarchy.

### Why the issue still stands

The narrow claim — persistence of $\delta_s$ — is honest and correctly stated. What does not land is the *promotion* of that quantity to "the default operational signal" in the cascade. An agent that drives $\delta_s \to 0$ has calibrated its self-assessment to $\Phi$, a quantity the rest of the theory describes as systematically biased in the dominant real-world case (causally insufficient DAGs).

The cascade's step-3 diagnostic quantities ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) inherit the same ceiling because $A_O$ and $V_O$ are both expectations under $M_t$ that feed through the same AND/OR propagation. An agent satisfying every inequality in the cascade under L0 can still be *categorically* miscalibrated about its plan; the cascade will not flag this, though `strategy-dag.md`'s Correlation Hierarchy will. The two segments are saying different things about what "strategy persistence" buys the agent.

The L0→L1 escalation remedy is documented in `strategy-dag.md`, but the cascade segment does not reference it, does not gate step 4a on a causal-sufficiency check, and does not include it in step 5's escalation ladder (5a–5d all remain within L0 analysis).

### Confidence

High.

### Integration gap in `msc/`

`spike-credit-assignment-boundaries.md` is more decisive than the segment form. §1.3 ("The Posterior Correlation Barrier") proves explicitly that any factored Beta representation is *an approximation by construction*:

> After $n_f$ failures, the posterior contains $n_f$ factors of $(1 - \prod_k \theta_k)$, each introducing cross-edge correlation. Expanding these factors yields a polynomial of degree $m \cdot n_f$ in the $\theta_k$. Representing this exactly requires exponentially growing storage ... Coupled corrections are inherent to the problem, not an artifact of a bad algorithm.

The spike then sets Level 0 persistence as the honest theory minimum. `credit-assignment-boundary.md` faithfully relays the Level 0/1/2/3 hierarchy, so that propagation has occurred. What has not propagated is a cascade-level gate.

Repair: a `#causal-sufficiency-check` step between cascade steps 4 and 5, keyed off the residual-covariance test that `strategy-dag.md` already gestures at ("Detecting latent common causes") — persistent $\delta_s \approx 0$ combined with persistent negative plan-outcome residuals is the signal that L0 is the binding scope and L1 augmentation is due. No new theorem is required; the spike has the mechanism, the segment has the qualitative description, and what remains is to thread them into the cascade's diagnostic flow.

---

## Finding 2 — The strategic persistence schema parallels epistemic persistence only under an additional mechanism (experience discounting) that the schema does not state as a prerequisite

### Problematic passages

`strategy-persistence-schema.md`, Formal Expression:

> $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$

`strategic-dynamics-derivation.md` Propositions B.1–B.6: every sector parameter has the form $1/(n+1)$ or a scaled variant.

`strategy-persistence-schema.md` Discussion:

> The structural parallel between epistemic and strategic persistence is not an analogy but a mathematical identity at the sector-framework level.

### Strongest mitigating passage

`strategic-dynamics-derivation.md` Epistemic Status:

> The time-varying $\alpha_\Sigma$ issue remains: since $n_k$ increases with each observation, $\alpha_\Sigma$ decreases over time. The sector-condition framework assumes constant $\alpha$. The results here give an *instantaneous* persistence check at the current experience level, not a trajectory guarantee. Experience discounting (exponential forgetting with factor $\lambda$) stabilizes $\alpha_\Sigma$ at approximately $1 - \lambda$, yielding the persistence requirement $\lambda < 1 - \rho_\Sigma/R_\Sigma$.

### Why the issue still stands

The epistemic and strategic cases are *not* structurally symmetric in the form presented. Epistemic persistence admits a stationary $\alpha$ (for linear correction, $\alpha = \mathcal{T}$ is exogenous). The strategic case has $\alpha_\Sigma$ intrinsically decaying with experience, so for any fixed $(\rho_\Sigma, R_\Sigma)$, every agent eventually crosses below threshold unless it discounts.

The "instantaneous persistence check" reading is correct; the trajectory claim the schema's advertised form implicitly supports is not. The forgetting mechanism is a *prerequisite* of the strategic persistence result, not a convenience. This is honestly flagged in a single paragraph within `strategic-dynamics-derivation.md`'s Epistemic Status, and mentioned in one Working Note in `strategy-persistence-schema.md`. It is not promoted to equal standing with the claimed structural identity.

### Confidence

Very high.

### Integration gap in `msc/`

This is the finding the spike-reading sharpens most. `spike-single-edge-strategic-dynamics.md` §5 states the discounting-as-requirement claim in exactly the form the segment does not:

> Exponential forgetting stabilizes the gain at $1-\lambda$, with a clean persistence condition on $\lambda$.

And in §9 "Broader Significance":

> The forgetting fix is the standard resolution, but seeing it emerge from the persistence condition as a *requirement* (rather than a heuristic) is new: the forgetting rate must satisfy $(1-\lambda) > \rho_\Sigma / R_\Sigma$, or persistence fails. This transforms "organizations should stay adaptive" from a platitude into a quantitative constraint.

The spike's §7–§8 ("What This Does and Doesn't Establish" + "Path to Promotion") is explicit that addressing the time-varying $\alpha_\Sigma$ is a *promotion prerequisite*:

> Either (a) re-derive the sector-condition results for time-varying $\alpha$ ... or (b) restrict to the discounted case where $\alpha_\Sigma$ stabilizes.

What actually propagated to the segments is a one-paragraph caveat in `strategic-dynamics-derivation.md` Epistemic Status and an unrelated Working Note in `strategy-persistence-schema.md` about stochastic-vs-deterministic drift. The $(1-\lambda) > \rho_\Sigma/R_\Sigma$ constraint — the spike's core promotion-blocking condition — does not appear in `strategy-persistence-schema.md` at all.

The integration gap is not "the spike addresses this but hasn't been propagated." It is "the spike's strongest and cleanest constraint was weakened during promotion." Repair: a paragraph in `strategy-persistence-schema.md` Formal Expression stating the forgetting constraint as a schema prerequisite, with an explicit $\lambda$-range derivation. No new theorem is required.

---

## Finding 3 — The composition scope condition presents a scalar threshold it does not actually define, and the unified framing is strictly weaker than the three-route disjunction the source spike defended

### Problematic passage

`composition-scope-condition.md` Unified form:

> All three routes express a single underlying requirement: *teleological alignment sufficient to define a coherent composite purpose*. The teleological unity measure $U_O$ introduced in #def-unity-dimensions provides a convenient unified scalar — the scope condition can be restated as $U_O \geq \epsilon_{\text{comp}}$ for an appropriate route-dependent operationalization.

`unity-dimensions.md` gives $U_O$ a pairwise form ($\text{corr}(V_{O_t^{(i)}}, V_{O_t^{(j)}})$) and then asserts "The composite teleological unity is an aggregation over all pairs" without specifying the aggregation.

### Strongest mitigating passages

`composition-scope-condition.md` Working Notes:

> Operational form of $\epsilon_{\text{comp}}$. A sharp threshold is likely artificial. More plausible: smooth transition from "not-quite-composite" to "composite" ... This needs formalization before promotion to `claims-verified`.

`composition-scope-condition.md` Formal Expression: three explicit routes (C-i, C-ii, C-iii), each with its own operationalization.

### Why the issue still stands

The three routes (C-i shared objective, C-ii hierarchical derivation, C-iii mutual benefit) are internally coherent and each is individually operationalizable in its domain. The problem is the reduction to a single scalar $U_O$ with a single threshold $\epsilon_{\text{comp}}$. Three route-specific operationalizations aren't shown to reduce to the same quantity, the $N$-agent aggregation isn't defined, and asymmetric alignment (symbiogenesis, acquisitions) is explicitly unhandled.

Downstream segments then treat "$U_O$" as a well-defined scalar. `unity-closure-mapping.md` parametrizes rate-distortion curves by $U_O$. `symbiogenic-composition.md` defines itself relative to "$U_O$ crossing the scope threshold from below." Both inherit the ambiguity.

### Confidence

Medium-high.

### Integration gap in `msc/`

The unusual shape: here the segment's unifying claim is *stronger* than what the source spike committed to. `spike-symbiogenic-composition.md` §3.1 explicitly frames the scope condition as a disjunction:

> Different operationalizations admit different composites. The scope condition is satisfied if *any* of them applies — the three are progressively weaker routes to the same qualitative requirement.

The spike does not promote a unified scalar. The segment's "Unified form" paragraph is a segment-level move beyond what the spike defends.

`spike-unity-closure-mapping.md` §1 reinforces the concern from a different angle:

> Read literally, this claim fails in the two-Kalman case ... So unity does not determine $\varepsilon_x$ under this projection. The correct relationship is a rate-distortion one.

So the theory has two spikes converging on the conclusion that unity dimensions do not cleanly parameterize composite quantities as single scalars, and a segment that reads as if they do.

Repair: walk back the Unified form paragraph in `composition-scope-condition.md` to the explicit three-route disjunction. Drop the $\epsilon_{\text{comp}}$ scalar framing, or demote it to an illustrative aggregation that is known to fail in general. The scope condition becomes weaker in appearance but truer to what the theory actually establishes. The $N$-agent extension follows the same disjunctive pattern: the composite exists if any route applies across the group.

---

## Finding 4 — The causal-identifiability coefficient $\iota_{ij}$ is defined as a first-class edge property but the operational machinery ignores it

### Problematic passages

`strategy-dag.md`, Edge semantics:

> The identifiability coefficient $\iota_{ij}$ ( #scope-edge-update-causal-validity) quantifies the strength of the causal interpretation for each edge. When $\iota_{ij} \approx 1$, the agent's credence is well-identified causally. When $\iota_{ij} \approx 0$, the credence is associational.

`edge-update-causal-validity.md` proposes:

> $\eta_{\text{edge}}^{\text{adj}} = \eta_{\text{edge}} \cdot \iota_{ij}$

`strategy-complexity-cost.md`:

> $C_{\text{monitor}} \propto |\{(i,j) : \iota_{ij} < 1\}|$

But:

- `strategic-dynamics-derivation.md` Propositions B.1–B.6: no $\iota_{ij}$. Every sector parameter is computed with the unmodified gain $1/(n+1)$ or a topology-scaled variant.
- `strategy-dag.md` status propagation: $\hat P_\Sigma$ is computed from $p_{ij}$ alone; no $\iota_{ij}$ weighting.
- `orient-cascade.md`: no mention of $\iota$ anywhere in the cascade.
- `credit-assignment-boundary.md` default signal function (gradient-based attribution): regime-blind.

### Strongest mitigating passage

`edge-update-causal-validity.md` Epistemic Status:

> The identifiability coefficient $\iota_{ij}$: **hypothesis**. The concept is sound ... but the specific form — a scalar multiplier on the gain — is a first-order approximation.

### Why the issue still stands

The theory has formally separated Regime A/B/C edges (intervention-rich, partial, observation-only) and then reunified them implicitly in every operational formula. An agent whose strategy mixes Regime A edges (tests in CI) and Regime C edges (passive monitoring of markets) is treated by the cascade identically to an all-Regime-A agent, and its plan-confidence score is unweighted by causal warrant. This is strictly weaker than the theory's own stated scope awareness. The gap is not in any single segment's claims; it is the non-propagation of a regime-indexing distinction into the downstream machinery that has already been written.

### Confidence

High.

### Integration gap in `msc/`

Two spikes address this, and the propagation has been partial.

`spike-edge-semantics-resolution.md` proposes three candidate resolutions and recommends Resolution A Enhanced — regime-indexed interpretation with single-parameter edges. §5.1–§5.4 of the spike specify language changes to `strategy-dag.md`, `edge-update-via-gain.md`, and `edge-update-causal-validity.md`. Those language changes have propagated — the current segments carry them. §6 of the same spike then proposes a regime-indexed signal function:

> $\text{signal}(o_t, i, j) = f(\underbrace{\text{outcome}(o_t, j)}_{\text{what happened at } j}, \underbrace{\text{attribution}(o_t, i, j)}_{\text{was it because of } i?}, \underbrace{\text{regime}(i, j)}_{\text{how causal is the evidence?}})$

This decomposition has not propagated. `credit-assignment-boundary.md`'s default signal is regime-blind.

`spike-strategy-tempo-cost.md` §1.4 gives the cleanest operational form:

> $\mathcal{T}_\Sigma^{\text{eff}} = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij} \cdot \iota_{ij}$

with an explicit Regime A/B/C table: Regime A contributes full tempo, Regime B reduced, Regime C near-zero. The spike also notes the decomposition is additive, giving a precise meaning to "the agent cannot improve the parts of its strategy that it cannot test interventionally." This has not propagated into `strategic-tempo.md` or into the schema.

Repair: three-step.

1. `strategic-tempo.md` should adopt $\mathcal{T}_\Sigma^{\text{eff}}$ with the $\iota$ factor as the primary definition, not a side quantity.
2. `strategic-dynamics-derivation.md` Props B.1–B.6 should carry $\iota_{ij}$ as a multiplicative factor on $\alpha_\Sigma$. The propositions still go through because $\iota$ commutes through the diagonal sector products in each case; the proofs do not change, only the sector-parameter formulas get an $\iota$ factor.
3. `credit-assignment-boundary.md`'s default signal should acknowledge the regime axis, per `spike-edge-semantics-resolution.md` §6.

None of this requires new theorems; the spike content is already worked out.

---

## Candidates that dissolved

- **Class 2 (LLM) scope restriction.** Called out in the `OUTLINE.md` preamble as the single most significant scope restriction in the theory, and discussed throughout `directed-separation.md`. Not a hidden issue.
- **Bridge-lemma contraction assumption beyond (A4).** Explicitly labeled conditional in `composition-closure.md` Epistemic Status with the three-tier agent classification.
- **Adversarial coupling model** ($\rho = \rho_0 + \gamma \cdot \mathcal{T}_{\text{opp}}$) as the source of the squared law. Labeled as assumption in both `adversarial-tempo-advantage.md` and `adversarial-destabilization.md`.
- **Additive scalar tempo under channel correlation.** Flagged in `adaptive-tempo.md` and inherited forward with explicit caveats in `team-persistence.md`, `adversarial-tempo-advantage.md`, and `tempo-composition.md`.
- **Independence of unity dimensions.** Explicitly a hypothesis per `unity-dimensions.md` Working Notes and reexamined in `unity-closure-mapping.md` (update-heterogeneity is a missing axis).
- **CMC/P3 framing.** The claim "P3 is a consequence, not a premise" reads narrowly enough (forward propagation on causally sufficient DAGs) that the CMC theorem supplies what's needed. It would be sharper to foreground the forward-direction reading, but the framing is not wrong.
- **Composite tempo $\mathcal{T}_c$ dual definitions** (intrinsic at the macro level vs. bounded above by sub-agent sum). `tempo-composition.md` is explicitly labeled `sketch` status, with Epistemic Status acknowledging the gap. Not a hidden issue.

---

## Cross-cutting pattern

Across all four findings, the same asymmetry recurs:

**The spikes consistently make stronger, sharper claims than the segments they promoted to.**

- Discounting-as-prerequisite (spike) became discounting-as-side-note (segment).
- Three-route disjunction (spike) became unified-scalar-threshold (segment).
- Regime-indexed signal function (spike) became regime-blind signal function (segment).
- L0/L1 stratification with sufficiency-check requirement (spike) became a qualitative remark in one segment and is absent from the cascade (segment).

Every segment is *honest* about the simplification — the caveats exist — but the simplification pattern runs one direction consistently enough to read as a systematic promotion-side compression. A useful editorial hygiene move: a post-promotion pass that asks, for each spike that produced a segment, "what did the spike establish that the segment does not say?" Not every difference is a bug — some compressions are right — but the asymmetry currently runs one direction far more often than the other, and the reverse direction deserves a default check.

This is not a theoretical flaw; it is a documentation-process flaw that manifests as a small class of theoretical understatements. The repair is cheap (paragraph-level additions and walk-backs, not new derivations) and compounds across future segments.

---

## Bigger-picture synthesis

After this audit, some intuitions about where the theory could be more beautiful, more concise, more fundamental, or more complete. These are guesses and pattern-observations, not claims.

### One engine, applied five times

Every persistence-flavored result in AAD — single-agent epistemic (§I), strategic (§II), team (§III), composite (§III bridge lemma), coordination overhead (`tempo-composition`) — has the form "correction rate / effective disturbance rate > tolerance," proven via a Lyapunov function and sector-bounded correction. The theory would be dramatically more concise, and its scope more legible, if it stated this template once as a lemma (`#result-sector-persistence-template`) and each instantiation were a two-paragraph segment specifying $(\delta, \alpha, \rho, R)$ for that context.

Currently the same result is rebuilt five times with slightly different notations and different caveats. The reconstruction obscures that *the theory is one result about bounded-correction dynamics applied to five different state spaces*. Factoring the template out is the single biggest available concision move. It would cut perhaps 40% of the Lyapunov boilerplate across the core and make the scope conditions for each instantiation visible rather than inherited.

### Three approximation hierarchies, one pattern

L0/L1/L2 (correlation, in `strategy-dag.md`), C1/C2/C3 (value-convention, in `value-object.md`), Tier 1/2/3 (bridge-lemma contraction, in `composition-closure.md`) all share the same structure: sacrifice fidelity for tractability, with proved monotonicity and graceful degradation. These are three instances of a single meta-principle — AAD parameterizes its results by approximation level, and the diagnostic framework lets you ascend the ladder on demand. An explicit `#disc-approximation-tiering` segment in the Appendices would make this visible and suggest where other ad-hoc simplifications (scalar tempo, channel independence, single-parameter edges, AND/OR completeness) might fit as additional hierarchies.

### Independence assumptions are the theory's dominant modeling move, and they are scattered

Directed separation, causal sufficiency, channel independence, edge independence, unity-dimension independence, additive tempo — every one of these is a simplification from coupled dynamics to uncoupled dynamics, and each has a counter-example regime identified somewhere else in the theory. The theory would be stronger if these were enumerated in one place, with their consequences when violated and their repair operations (L0→L1, modular→partially-modular, scalar→per-dimension, and so on).

This would also clarify what is *not* an independence assumption (the DAG acyclicity, the CMC result, the Lyapunov machinery) and therefore what survives when those assumptions fail. An "independence audit" segment is the shape this takes.

### Information Bottleneck is the unifying compression framework

The `unity-closure-mapping` spike notes this for (P1) and unity dimensions, but the pattern is broader: `#form-information-bottleneck` for $M_t$, `#form-strategy-complexity-cost` for $\Sigma_t$, `#def-shared-intent` for inter-agent communication, and (P1)-(P2)-(P3) for projections are four IB instances with different relevance variables. `spike-unity-closure-mapping.md` §1 is explicit that the rate-distortion shape *is the IB shape* in the linear-Gaussian case, and §6 conjectures that (P1)-(P3) reduce to "projection attains the IB frontier plus Lipschitz regularity."

If one committed to stating AAD's compression operations uniformly as IB problems parameterized by a relevance variable, one would lose nothing and gain: (a) a single master compression principle; (b) explicit mapping of each relevance variable to the substate it serves; (c) a natural explanation of why (P1)-(P3) are "independent" — they are IB constraints for different relevance variables. This looks like the biggest available *unification* in the theory. The linear-Gaussian derivations that would support it are already in the spikes.

### The DAG uniqueness result is undersold

`graph-structure-uniqueness.md` quietly proves that four operational postulates plus causal sufficiency force the strategy representation to be a Markov-factorized DAG. This is not a minor technical result — it is a claim about the *necessary* shape of strategy representation, in the same tradition as Cox's theorem for probability.

The segment does not foreground the parallel to Cox's theorem forcefully enough, and the broader framework (in `strategy-dag.md`) treats DAG structure as a definitional choice. There is a more decisive version of the theory where the DAG is a *consequence* of operational requirements, explicitly parallel to "rationality forces probability." The theory would be more fundamental framed that way, and the result would carry its appropriate weight.

### Persistence and destabilization are a single statement

`persistence-condition.md` gives $\alpha > \rho/R$; `adversarial-destabilization.md` gives $\gamma \mathcal{T}_{\text{opp}} > \alpha R - \rho$. Rearranging the second: $\rho + \gamma \mathcal{T}_{\text{opp}} > \alpha R$, which is the *negation* of the persistence condition with effective disturbance $\rho_{\text{eff}} = \rho + \gamma \mathcal{T}_{\text{opp}}$. A single result — a *structural persistence boundary* — stated once, would subsume both and make the adversarial claim obviously derived rather than separate.

### The $G_t = (O_t, \Sigma_t)$ split may be a Class 1 artifact

The split is defined as "evaluation vs. guidance." In Class 2 agents (LLMs), the same representation carries both — an instruction sentence both names the objective and guides the action. The theory's definitional split is clean for modular agents and is explicitly noted to require rework for Class 2. A cleaner formulation might define $G_t$ as a single object (purposeful state) and treat the $(O_t, \Sigma_t)$ decomposition as a *property some agents have* rather than an axiomatic decomposition. The directed-separation classification (Class 1/2/3) would then bear directly on whether the decomposition is available, which is more honest and foregrounds the scope work the theory already acknowledges.

### The convention hierarchy is a discretization of a continuous parameter

C1 is 1-step, C2 is $N_r$-step, C3 is Bellman (effectively $\infty$-step under the policy class). A continuous receding-horizon family indexed by $N_r \in [1, \infty]$ would subsume the three conventions, give the diagnostic quadrants a continuous reading, and remove the three-convention ad-hocness. The monotonicity result becomes "$A_O(N_r)$ is weakly monotone in $N_r$," which is a clearer statement. C1 and C3 are then the limits of a single family rather than three separate definitions.

### Biggest single moves

- **Concision:** factor out the sector-Lyapunov template as a lemma stated once; restate every persistence-flavored result as an instantiation.
- **Generalization:** IB-unify the compression operations across $M_t$, $\Sigma_t$, shared intent, and composition projection. The linear-Gaussian derivations already exist in spike form.
- **Honesty:** promote the causal-sufficiency caveat from a footnote in `strategy-dag.md` into a cascade-level diagnostic. The theory's strongest moves in §II all hold *within the L0 model*, and an agent cannot tell from inside the cascade that its whole calibration is running against a biased target.
- **Fundamentality:** foreground the graph-uniqueness-with-Markov result as parallel to Cox's theorem, not as a supporting derivation in an appendix.
