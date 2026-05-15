---
slug: disc-approximation-tiering
type: discussion
status: robust-qualitative
depends:
  - def-strategy-dag
  - def-value-object
  - form-composition-closure
stage: draft
---

# Discussion: Approximation Tiering

AAD uses a recurring meta-pattern for handling intractability: when a problem admits no tractable exact treatment in general, introduce a tiered hierarchy of approximations with proved monotonicity between tiers and a diagnostic for ascending when needed. Three such hierarchies exist in the theory — the Correlation Hierarchy (L0/L1/L2) in #def-strategy-dag, the Convention Hierarchy (C1/C2/C3) in #def-value-object, and the Tier 1/2/3 contraction taxonomy in #form-composition-closure. This segment articulates the pattern explicitly, identifies what makes a successful approximation tiering, and notes where other scattered simplifications might fit the same shape.

## Formal Expression

*[Discussion (approximation-tiering)]*

A successful approximation tiering has four components:

**(AT1) A parameter indexing tractability.** Some quantity (correlation modeling depth; continuation-policy fidelity; operator regularity) that admits a natural ordering from least to most demanding computation.

**(AT2) Monotonicity.** A proved ordering of the results produced at each level — each higher tier dominates the lower in the direction of interest (calibration accuracy, diagnostic force, guarantee strength).

**(AT3) Graceful degradation.** Lower tiers produce usable (not vacuous) results, with the specific form of the degradation characterized. An agent stuck at the lowest tier knows what it is missing, not just that it is incomplete.

**(AT4) Ascension diagnostic.** A signal the agent can detect at a lower tier that indicates escalation to a higher tier is warranted. Without this, the tiering is descriptive but not operational.

### The three AAD tierings

| Hierarchy | Parameter | Monotonicity | Lowest tier | Highest tier | Ascension diagnostic |
|---|---|---|---|---|---|
| **Correlation** ( #def-strategy-dag) | Modeling depth of inter-edge dependence | L0 is conservative; L1 is unbiased on augmented graph; L2 is the full joint | L0 (independence model, $O(\lvert V\rvert + \lvert E\rvert)$ propagation) | L2 (full joint, $O(2^m)$ in general) | Sibling-edge covariance after credence convergence ( #der-causal-insufficiency-detection) |
| **Convention** ( #def-value-object) | Continuation-policy fidelity | $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ (proved monotonicity) | C1 (one-step improvement) | C3 (Bellman optimal) | Persistent $\delta_{\text{sat}} \gt 0$ under C1 that C2 replanning may resolve |
| **Contraction** ( #form-composition-closure) | Operator regularity for bridge lemma | Tier 1 $\supset$ Tier 2 $\supset$ Tier 3 in terms of proved contraction strength | Tier 3 (domain-specific verification required) | Tier 1 (contraction proved for full class) | Structural test: is the correction strongly monotone, locally convex, or neither? |

Each row satisfies (AT1)–(AT4) fully — these are mature tierings in the theory. Each tiering is independently motivated by a different source of intractability, and each has its own ascension mechanism. Their structural similarity is not designed-in; it is the consequence of facing three separate intractable problems with the same modeling strategy.

### Candidate future tierings

Several other scattered simplifications in the theory have the right shape to become tierings but are not currently organized that way:

- **Scalar vs. per-dimension tempo** (around #def-adaptive-tempo, #result-per-dimension-persistence). Tier 0 (scalar isotropic), Tier 1 (per-dimension), Tier 2 (full tensor with off-diagonal coupling). Monotonicity: scalar overestimates margin, per-dimension is exact for diagonal-gain systems, full tensor handles off-diagonal gain coupling. Ascension diagnostic: gain variance across dimensions.
- **AND/OR parameterization** ( #scope-and-or). Tier 0 (AND/OR, $O(k)$ parameters per node), Tier 1 (weighted/threshold, $O(k)$ additional parameters), Tier 2 (full CPT, $O(2^k)$ parameters). Monotonicity: expressiveness. Ascension diagnostic: systematic miscalibration at AND/OR nodes that survives L1 augmentation.
- **Identifiability regimes** ( #scope-edge-update-causal-validity). Regime A/B/C is already a tiering of causal identification quality, with $\iota_{ij}$ as the indexing parameter. Monotonicity: interventional $\succeq$ partial $\succeq$ observational. Ascension diagnostic: available intervention opportunities in the domain.

Promoting these to named tierings with explicit (AT1)–(AT4) structure would make AAD's scope parameterization more uniform. This is not pursued here — it is noted as a direction for editorial consolidation.

## Epistemic Status

*Robust-qualitative.* Max attainable: *robust-qualitative*. The meta-pattern is an editorial observation: three existing hierarchies in the theory share the same four-component structure, and the shared structure is worth naming because it makes the theory's scope-parameterization move visible rather than implicit. The pattern itself is not a theorem — there is no result that says "every intractable AAD problem admits a (AT1)–(AT4) tiering." The candidate future tierings are conjectures about where the pattern could be extended; each would require its own monotonicity proof and ascension diagnostic.

The three existing tierings are individually grounded: the L0→L1 monotonicity holds under the CMC theorem and augmentation construction; the C1→C2→C3 monotonicity is proved in #def-value-object; the Tier 1/2/3 taxonomy is grounded in operator theory (strong monotonicity, local convexity, arbitrary).

## Discussion

**Why this matters.** AAD's results are often presented as "exact under assumption X." A reader can misread this as "the theory works when X holds and breaks otherwise." The tiering pattern reveals a different structure: when X fails, a named lower tier takes over with a characterized weaker result, and the theory provides a diagnostic for when to escalate to reinstating X by structural repair. This is graceful degradation — a property that a theory wanting to apply across a range of agents and domains needs, and that AAD achieves in three places independently.

Reading AAD through the tiering lens: the theory's "exact" core is what it guarantees at the highest tier of each hierarchy. Its "conditional" periphery is where specific tiers are in force. The claim is not that agents should always operate at the highest tier — that would often be intractable — but that the theory tells the agent which tier it is in and how to get to a higher one when the binding constraint changes.

**Connection to #disc-independence-audit.** The two meta-segments are complementary. #disc-independence-audit enumerates the independence assumptions whose failure drops a result from exact to conditional. This segment enumerates the tierings that provide the structured *recovery* from those drops. Together they characterize AAD's scope parameterization: the independence audit says where the boundaries are; the tiering pattern says how to navigate within them.

**What a full tiering promotion would look like.** If the scattered simplifications listed above were promoted to named tierings, the theory's scope-parameterization would be dramatically more uniform: every conditional result would come with its own tiering and ascension diagnostic. This is aspirational. The three existing tierings took substantial segment-work to formalize (a full Appendix derivation for the CMC, a monotonicity proof for the convention hierarchy, a spike for the incremental sector bound). Extending the pattern to five or six hierarchies would be correspondingly substantial.

**The pattern is not unique to AAD.** Approximation tiering is a common move in applied mathematics — numerical methods (low-order vs. high-order integrators with error bounds), information theory (typical vs. exact coding with rate-distortion monotonicity), statistical inference (maximum-likelihood vs. Bayesian vs. nonparametric). AAD's contribution is not the tiering pattern itself but its deployment across the specific intractable problems that adaptive-agent theory faces.

## Working Notes

- **Formal characterization of the tiering pattern.** Is there a mathematical structure that unifies approximation tiering across domains? Candidates: lattices of model classes ordered by inclusion, rate-distortion curves with explicit corners, hierarchies of Galerkin approximations. None of these is an exact match; the AAD tierings are closer to "ordered families of sufficient conditions" than to any standard mathematical hierarchy. Worth investigating whether a cleaner abstract pattern exists.
- **Interaction between tierings.** An agent operating at L1 correlation, C2 convention, and Tier 2 contraction is in a specific combined regime. The cross-hierarchy interactions are not worked out — is there cross-hierarchy monotonicity? (E.g., does L1 change anything about the convention hierarchy's guarantees?) Each tiering is independently-grounded but the joint structure is not yet mapped.
- **Diagnostic costs.** Each ascension diagnostic has a cost: detecting sibling covariance requires observing convergence; detecting C1-inadequacy requires comparing replanning values; detecting Tier 1 violations requires verifying strong monotonicity. A unified treatment of "when is the diagnostic itself worth running?" would connect this segment to #der-deliberation-cost and the allocation analysis in #disc-exploit-explore-deliberate.
