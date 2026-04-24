---
slug: independence-audit
type: discussion
status: robust-qualitative
depends:
  - directed-separation
  - strategy-dag
  - adaptive-tempo
  - definition-unity-dimensions
  - per-dimension-persistence
  - graph-structure-uniqueness
stage: draft
---

# Discussion: Independence Audit

AAD's results depend on a recurring modeling move: treat some quantity as independent of another to obtain tractable mathematics, then identify the failure regime where independence breaks and specify the repair. This segment enumerates the independence assumptions used across the theory, their failure regimes, their diagnostic signals, and the repair operations AAD provides. The enumeration makes visible what is *not* an independence assumption — acyclicity of $\Sigma_t$, Cox-derived probability, the Lyapunov machinery of #sector-persistence-template — and therefore what survives when a particular independence assumption fails.

## Formal Expression

*[Discussion (independence-audit)]*

Six load-bearing independence assumptions in AAD, each paired with its failure regime and repair:

### 1. Directed separation: $M_t$ update independent of $G_t$

**Statement:** $f_M(M_{\tau^-}, e_\tau)$ has no $G_t$ argument — the epistemic update is goal-blind.

**Where it appears:** #directed-separation, the structural backbone of Section II. Feeds the orient cascade's sequential resolution ( #orient-cascade), the causal validity of $Q_O$ ( #value-object), and the scope of all Section II results to Class 1 (modular) agents.

**Failure regime:** Class 2 (fully merged) architectures — transformer LLMs where attention processes goals and observations together. Motivated reasoning, confirmation bias, prompt-conditioned perception. Partially also Class 3 (partially modular) agents.

**Diagnostic signal:** $\kappa_{\text{processing}} = I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-})/H(G_t \mid e_\tau, M_{\tau^-})$. Zero for modular agents; near one for fully merged; intermediate for partial.

**Repair operation:** Class 3 approximation quality scales with $\kappa_{\text{processing}}$. Class 2 agents require the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without $(M_t, G_t)$ decomposition — the scope of `03-logogenic-agents/`. At the system level, Class 2 components can be wrapped in modular topology (separate observation processing, external monitoring — see `#directed-separation` Working Notes on the IDT pattern).

### 2. Causal sufficiency: no latent common causes among strategy nodes

**Statement:** Every common cause of two or more nodes in $\Sigma_t$ is itself a node in $\Sigma_t$.

**Where it appears:** #graph-structure-uniqueness (precondition for the CMC-based Markov proof); #strategy-dag edge-independence in status propagation; all of Section II's strategy-layer formal results (Props B.1–B.6, the sector condition transfer of B.5, persistence of $\delta_s$).

**Failure regime:** The dominant real-world case in complex, multi-stakeholder, or adversarial environments — shared infrastructure, market conditions, correlated adversary actions, common-mode risks, supply-chain dependencies.

**Diagnostic signal:** Pairwise covariance among sibling edges after edge credences have converged. Positive covariance rejects the independence hypothesis and localizes where a common cause is missing. See #causal-insufficiency-detection.

**Repair operation:** L1 augmentation — add common-cause nodes and restructure the DAG so each common cause is factored *above* the correlation it creates ( #strategy-dag Correlation Hierarchy; #strategic-dynamics-derivation Prop B.6). L0 formal results transfer exactly to correctly constructed L1 DAGs because L1 restores causal sufficiency by construction. The orient cascade's step 4c triggers this escalation.

### 3. Channel independence: observation channels contribute non-redundant correction

**Statement:** $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ with each channel contributing independently to effective tempo.

**Where it appears:** #adaptive-tempo (core definition); inherited by #persistence-condition, #adversarial-tempo-advantage, #team-persistence (communication tempo), #derived-tempo-composition, and any result using scalar $\mathcal{T}$.

**Failure regime:** Any system with redundant or correlated information sources — overlapping sensors, correlated teammate reports, redundant telemetry. In multi-agent settings, allies reporting the same intelligence source.

**Diagnostic signal:** $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$ — pairwise mutual information between event streams conditioned on prior model state. Non-zero mutual information signals redundancy.

**Repair operation:** Under correlation, $\mathcal{T}$ satisfies a strict inequality: $\mathcal{T} \leq \sum_k \nu^{(k)}\eta^{(k)\ast}$, with equality iff channels are informationally independent. The additive formula is an upper bound. For precise tempo, the effective capacity must account for mutual information between channels. Propagates as a redundancy penalty into every segment using scalar tempo.

### 4. Unity-dimension independence: $(U_M, U_O, U_\Sigma, U_{\text{obs}})$ substantially independent

**Statement:** The four unity dimensions of #definition-unity-dimensions parametrize composite quality along substantially independent axes.

**Where it appears:** #definition-unity-dimensions framing; #unity-closure-mapping's rate-distortion family indexed by each unity separately.

**Failure regime:** Shared models enable implicit strategic coordination (high $U_M$ → high $U_\Sigma$ without explicit policy sharing); aligned objectives often induce strategic coordination. Also *update-rule heterogeneity* (an axis not covered by any unity dimension) contributes to closure defect independently — the two-Kalman non-degenerate case shows $\varepsilon_x \gt 0$ from differing Kalman gains at perfect $U_M$.

**Diagnostic signal:** No clean one. The hypothesis is empirical and the theory currently logs it as working-position rather than resolved (see #definition-unity-dimensions Working Notes: update-heterogeneity gap).

**Repair operation:** Two options explored in the theory: (a) accept a two-axis structure (unity × homogeneity) for closure defect, (b) add a fifth update-homogeneity dimension. The current working position is (a); formal resolution open. Downstream uses of unity dimensions should not treat them as cleanly orthogonal.

### 5. Independent edge outcomes in AND/OR propagation

**Statement:** In $\hat P_\Sigma$ status propagation, sibling edge outcomes are independent given their parents.

**Where it appears:** #strategy-dag status propagation formula; #and-or-scope; every downstream quantity computed from $\hat P_\Sigma$ (satisfaction gap, control regret via $A_O$, plan-confidence error $\delta_s$).

**Failure regime:** Same as causal sufficiency (item 2) — the CMC theorem makes them the same condition: causal sufficiency ⟺ exogenous noise independence ⟺ edge-outcome independence. When one fails, they all fail.

**Diagnostic signal:** Same as item 2.

**Repair operation:** Same as item 2 (L1 augmentation). The assumption is not a separate modeling choice from causal sufficiency; the theory treats it as the *consequence* of causal sufficiency (via CMC), not an independent axiom.

### 6. Scalar tempo / isotropic correction

**Statement:** $\mathcal{T}$ as a scalar captures the agent's correction capacity.

**Where it appears:** #persistence-condition linear operational form; most Section I results stated in scalar $(\mathcal{T}, \rho, \lVert\delta_{\text{critical}}\rVert)$ form; #strategic-tempo aggregate.

**Failure regime:** Any real multi-dimensional system with non-uniform correction capacity across dimensions. Simulation confirms scalar $\rho/\mathcal{T}$ overestimates by up to 72% in anisotropic systems, with the weak dimension accounting for 84% of total mismatch.

**Diagnostic signal:** Gain variation across dimensions (easily computable when gains are explicit — Kalman, gradient descent with diagonal preconditioning).

**Repair operation:** Per-dimension persistence: $\mathcal{T}_k \gt \rho_k/\lVert\delta_{\text{critical},k}\rVert$ for each dimension. See #per-dimension-persistence. The weakest dimension is the bottleneck. Same structural pattern propagates to strategic tempo ( #strategic-tempo Per-edge persistence) — the bottleneck edge determines persistence, not the aggregate.

## What is *not* an independence assumption

Several results that might appear to depend on independence actually do not:

- **Acyclicity of $\Sigma_t$** is proved from temporal ordering over a finite horizon ( #graph-structure-uniqueness). Independent of any independence assumption.
- **Cox-derived probability structure** at edges is independent of edge-independence — Cox forces the *measure* to be probability, not the joint structure.
- **Sector-persistence template machinery** ( #sector-persistence-template) depends only on the sector condition (T2) and bounded disturbance (T3); it does not require any independence assumption on the state variable or correction function.
- **The DAG structure derivation** (directed edges, acyclicity, representability as a Bayesian network) does not require causal sufficiency — only the *Markov factorization* within the derived structure does.

This is the boundary between AAD's robust results and its conditional ones: robust results survive when the independence assumptions fail; conditional results break and require their specific repair operations.

## Epistemic Status

*Robust-qualitative.* Max attainable: *robust-qualitative*. The enumeration is definitional — each independence assumption is stated in a named segment, and the repair operations are either formally specified (causal sufficiency ↔ L1 augmentation) or named open problems (unity-dimension independence). What this segment adds is the cross-cutting view: the six assumptions are the recurring modeling move that distinguishes AAD's exact-tractable results from its conditional results, and the repairs are (mostly) already present in the theory but scattered across segments.

The enumeration is not exhaustive. Other independence-flavored assumptions exist in specific instantiations (e.g., independent Beta priors across edges in the credit-assignment analysis of #credit-assignment-boundary). The six listed are the load-bearing ones — those whose failure regime the theory has actually characterized and provided a repair for.

## Discussion

**Why enumerate these in one place.** AAD's theoretical contribution is often described as "integration": bringing control theory, causal inference, information theory, and agent architecture under one framework. Integration *is* achieved largely through the independence assumptions listed above: each is a bridge that lets a module from one discipline plug into a module from another. Directed separation lets control-theoretic Lyapunov analysis operate on the epistemic substate without goal-entanglement. Causal sufficiency lets Pearl's DAG machinery apply to strategy without requiring the agent to model every environmental common cause. Channel independence lets the tempo framework sum over heterogeneous observation modalities.

When these bridges fail, the integration does not fail catastrophically — each failure has a characterized repair. But the theory's "exact" claims depend on the bridges holding, and recognizing this is the honest way to present the framework's scope. A reader who understands the six assumptions and their repairs understands where AAD's results apply exactly, where they apply approximately, and where they require structural revision.

**Connection to #approximation-tiering.** The L0/L1 distinction for causal sufficiency (items 2 and 5) is one instance of a meta-pattern: AAD's results are parameterized by approximation level, with proved monotonicity between levels. See #approximation-tiering for the full treatment — the pattern also applies to the C1/C2/C3 value-convention hierarchy and the Tier 1/2/3 bridge-lemma contraction structure.

**What this does NOT say.** The enumeration does not claim the theory's results are fragile or routinely fail. Most independence assumptions hold approximately in most well-behaved domains, and the theory's quantitative predictions are typically within the regime where assumptions apply. The audit is a scope clarification, not a criticism.

## Working Notes

- **Interaction between assumptions.** The six assumptions are not fully orthogonal. Causal sufficiency failure and edge-independence failure are the same failure (item 5 is a consequence of item 2 via CMC). Directed separation failure can propagate through the orient cascade into the strategy-layer results (which inherit their structure from the cascade). A fuller treatment would map the dependency graph among assumptions and characterize cascading failure modes.
- **Quantitative failure modes.** For each independence assumption, the theory has or could have a quantitative failure bound — how much the dependent result degrades as a function of the independence-violation magnitude ($\kappa_{\text{processing}}$, the covariance magnitude, the mutual information between channels). These bounds are partially specified in segment-level caveats; collecting them in one place would strengthen the audit.
- **Empirical audit.** A concrete agent could be scored against the six assumptions to produce an "independence profile." For software agents: directed separation ~holds (modular), causal sufficiency ~holds (test-based Regime A), channel independence ~holds (tests target disjoint behaviors), scalar tempo may fail (component-level gain variation). For LLM agents: directed separation fails structurally (Class 2), causal sufficiency varies by task, channel independence varies. The profile would be a diagnostic for where the theory's exact claims apply to the agent and where they degrade.
