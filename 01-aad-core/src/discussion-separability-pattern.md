---
slug: discussion-separability-pattern
type: discussion
status: discussion-grade
depends:
  - strategy-dag
  - value-object
  - directed-separation
  - composition-closure
  - edge-update-causal-validity
  - agent-spectrum
  - approximation-tiering
  - discussion-identifiability-floor
stage: draft
---

# Discussion: The Separability Pattern — Separable Core, Structured Repair, General Open

AAD consistently runs a three-part epistemic posture across state spaces that admit no tractable exact treatment in general: name the **separable core** where identification is clean, name the **structured repair** that recovers identification under explicitly-added machinery, and name the **general open** case where the problem is either intractable or structurally unidentifiable. Six ladders in the current theory share this shape. This segment names the pattern as an organizing principle, catalogs the instances, and makes the complementarity with `#discussion-identifiability-floor` (which names the *negative half* of AAD's scope) explicit.

## The pattern

Each instance of the separability pattern has the form:

1. **Separable core.** A sub-class of problem in which identification is tractable by construction — the quantity of interest has a clean estimator that requires only assumptions the agent can verify or control. "Separability" here is broader than statistical independence: it names the regime in which the quantity decomposes along a structural axis (independence, additive decomposition, directed separation, strong contraction, clean intervention, etc.) without interaction terms requiring additional machinery.

2. **Structured repair.** A sub-class where the separability assumption fails but a *specific, named, bounded-cost* additional mechanism recovers identification. The repair is structured: it identifies the failure mode, adds a specific compensating construction, and typically carries a characterized loss in tightness or generality. Repairs are not "apply heuristics"; they are "augment with observability of $C$ and accept $O(1)$ per-node parameter cost," "run receding-horizon replanning at cost $\mathrm{DL}(\Sigma_t)$," or similar.

3. **General open.** The fully-general case where no tractable repair is known. This is where `#discussion-identifiability-floor` instances live — structural no-go results that characterize *why* the general case remains open. Naming this boundary positively (as a known frontier) rather than negatively (as a failure) is part of AAD's load-bearing scope honesty.

## Current instances — six ladders

| Ladder | Separable core | Structured repair | General open |
|---|---|---|---|
| **Correlation** (#strategy-dag) | **L0** — independence model, $O(\lvert V\rvert + \lvert E\rvert)$ propagation | **L1** — strict-prerequisite augmentation with explicit common-cause node; **L1'** — soft-facilitator mixture with five-way gating under observable $C$ + facilitator monotonicity (#strategic-dynamics-derivation Prop B.7) | **L2** — full joint; **L1' unobservable-$C$** single-channel is *refuted* by Cramér-Rao floor (#discussion-identifiability-floor Instance 2) |
| **Convention** (#value-object) | **C1** — one-step improvement | **C2** — receding-horizon replanning | **C3** — Bellman optimal; intractable for large state spaces |
| **Architecture** (#directed-separation) | **Class 1** — modular; directed separation holds by construction | **Class 3** — partially modular; directed separation holds for identified submodules | **Class 2** — fully merged / coupled / logogenic; needs non-modular coupled formulation (future work) |
| **Contraction** (#composition-closure) | **Tier 1** — strong monotonicity; bridge lemma applies with proved $\varepsilon^\ast$ | **Tier 2** — local convexity; bridge applies within a specified basin | **Tier 3** — neither; domain-specific verification required per instance |
| **Identification regime** (#edge-update-causal-validity) | **Regime A** — interventional ($\iota_{ij} = 1$); action is a literal $do(\cdot)$ | **Regime B** — partial intervention ($0 \lt \iota_{ij} \lt 1$); confounder adjustment, side-channel observation | **Regime C** — observational ($\iota_{ij} \approx 0$); identification depends on external assumptions (e.g., unconfoundedness) |
| **Scope hierarchy** (#agent-spectrum) | **Adaptive** — basic feedback loop; #scope-adaptive-system satisfied | **Agency** — goal-bearing with $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect; adds $O_t$ and $\Sigma_t$ machinery (Section II); #scope-agency satisfied | **Composite** — multi-agent / team / logogenic; Section III gaps listed at the OUTLINE level (latent structural diversity, endogenous coupling, composition transition dynamics, agent opacity) |
| **A2'-scope** (#contraction-template) | **metric-α₁** — Euclidean metric, AAD-internally derived via DA2'-inc ≡ (CT2) at $M = I$ (scalar Kalman, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) | **metric-α₂** — non-Euclidean metric under explicit conditions; includes five cases (information-metric Kalman, Fisher-metric exp-family, Hessian-metric ill-conditioned, Lyapunov-metric linear-Hurwitz-non-symmetric, Lyapunov-metric PID-bounded-plant). Two of five (Fisher cases) AAD-internally forced under (PI)/Čencov per `#discussion-additive-coordinate-forcing`; remaining three theorem-imported from Lohmiller-Slotine 1998 | **metric-β** — contraction-metric formulation fails (variational-to-projected-target; rule-based / non-smooth; severely misspecified; per-step SGD / human judgment) |

Each row independently satisfies the three-part shape. The shared shape is not designed-in: it arises because AAD faces seven distinct sources of intractability and applies the same posture (name the clean case, name the repair, name what remains open) to each.

## Complementarity with the identifiability floor

The **separability pattern** names the *positive half* of AAD's scope: for each ladder, what succeeds under what conditions. Each separable-core entry is a positive identification claim; each structured-repair entry is a positive identification claim *conditional on* an explicitly-named added mechanism.

The `#discussion-identifiability-floor` names the *negative half*: structural no-go results (impossibility under limited information) that characterize why specific general-open cases remain open. Two floors are currently derived:

- **Instance 1** (on-policy L0-insufficiency detection via Causal Hierarchy Theorem) — forbids L0/L1 distinction from purely on-policy data. The positive counterpart: the **separable core under observable sibling covariance** is the unique broadly-available violation of the no-go's scope, naming what the agent *can* observe to escape the floor.
- **Instance 2** (L1' unobservable-$C$ single-channel via Cramér-Rao) — forbids mixture-parameter identification when $C$ is unobservable. The positive counterpart: the **structured repair under observable $C$** (Prop B.7 with facilitator monotonicity) is the identification-succeeds-under-augmentation claim matching the no-go's "unless $C$ is observable or multi-child observation is available" scope exit.

Together, the two meta-segments mark AAD's scope at two epistemic layers:

- **Separability pattern** — "here is what succeeds, with clean conditions and explicit repairs."
- **Identifiability floor** — "here is what structurally cannot succeed without specific information augmentation."

Neither alone gives the full picture. A theory stating only the positive half looks unbounded in its claims; a theory stating only the negative half looks conservative in a way that hides its achievements. Together they give scope honesty at both extremes.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. The segment is a presentational organizing principle. It names a shared shape that AAD already runs across multiple ladders; the pattern itself is not derived and has no theorem of its own. The individual ladder entries retain their own epistemic status — Correlation hierarchy results are at the tier specified in #strategy-dag and #strategic-dynamics-derivation; Convention hierarchy monotonicity is at the tier specified in #value-object; Contraction tier taxonomy is at the tier specified in #composition-closure; etc.

Max attainable: *discussion-grade* for the meta-pattern (it is an organizing principle, not a derivation). Individual instances are at their own tiers as above. The six-ladder enumeration could become *robust-qualitative* if a uniqueness argument were derived showing that separable-core / structured-repair / general-open is the unique viable posture across scope-parameterized hierarchies under AAD's scope-honesty architectural principle — but this is not currently in hand, nor clearly attainable.

## Discussion

**The pattern is load-bearing for how AAD presents its results.** A common failure mode of applied theories is the binary "exact under assumption X, breaks otherwise" presentation. The separability pattern refuses this presentation across six instances: where X fails, a named lower tier takes over with a characterized weaker result, and the theory provides a diagnostic for when to escalate (per #approximation-tiering's AT4 component). Readers who learn the pattern once can navigate any instance; this is what makes AAD tractable as an integrating framework rather than a pile of instantiations.

**Relationship to #approximation-tiering.** This segment is complementary to #approximation-tiering, not redundant with it. #approximation-tiering names the *structural template* (AT1 parameter indexing tractability; AT2 proved monotonicity between tiers; AT3 graceful degradation; AT4 ascension diagnostic) — the how-it-works of each tiering. This segment names the *epistemic posture* (separable core, structured repair, general open) — the what-each-tier-commits-to. Both are needed: #approximation-tiering explains what makes a successful tiering; this segment explains the shape of the commitment each tier makes about identification.

**Relationship to #independence-audit.** #independence-audit catalogs the *independence assumptions* whose failure degrades results; this segment catalogs the *ladders of recovery*. Together with #approximation-tiering they form a three-part characterization of AAD's scope:

- **#independence-audit** — where the boundaries are (which assumptions, what breaks if they fail).
- **#approximation-tiering** — how to navigate within the boundaries (parameterized hierarchy + monotonicity + ascension).
- **#discussion-separability-pattern** (this) — what each tier positively commits to (separable core / structured repair / general open).

**The pattern is distinctive to AAD's integration-over-invention character.** Approximation tiering with a separability posture is a common move in applied mathematics — it appears in numerical methods (exact vs. high-order vs. low-order with error bounds), in statistical inference (parametric separable-core / semiparametric repair / nonparametric open), in causal identification (Pearl's three-layer hierarchy is itself an instance). AAD's contribution is not the pattern but its deployment across the six specific intractable problems adaptive-agent theory faces, each with its own positive-half identification claims and negative-half floor instances.

**The A2' sub-scope partition is a proper three-part ladder via #contraction-template.** The A2' partition carries three tiers: sub-scope α (A2' derived under `#gain-sector-bridge` directional fidelity) as the separable core; sub-scope metric-α₂ (non-Euclidean metric under explicit conditions — five cases, with two Fisher-metric cases AAD-internally forced under the (PI)/Čencov fourth primary instance of `#discussion-additive-coordinate-forcing`) as the structured-repair middle tier; sub-scope β (A2' assumed) as the general-open tier. A2'-scope therefore qualifies as the seventh ladder of this meta-pattern, as enumerated in the table above. The structured-repair middle tier closes what would otherwise be a binary α/β partition lacking a derivable middle ground.

**The software calibration-lab framing (#software-epistemic-properties) is a specific instance.** C-BP3's calibration-lab reframing (commit `d0373fc`) partitions operational domains into "separable core" (software, where identification conditions P1–P6 are cleanly satisfied) and "structured-repair / general open" (other domains, which inherit under explicitly-named transfer assumptions). This is a domain-axis instance of the same pattern — software is the domain-axis separable core; the transfer-assumption table is the domain-axis structured-repair specification.

## Working Notes

- **Cross-ladder monotonicity.** The six ladders interact — an agent operating at L0 correlation + C2 convention + Class 1 architecture + Tier 1 contraction + Regime A identification + Agency scope is in a specific combined regime. Does cross-ladder monotonicity hold in any direction? E.g., does moving from L0 to L1 change anything about the Convention hierarchy's guarantees, or do the ladders factor independently? `#approximation-tiering`'s Working Notes flag this as an open question; the separability pattern's complementarity with the identifiability floor adds a further axis (which combinations are known-unidentifiable per #discussion-identifiability-floor).

- **Extension candidates beyond the six.** Three candidate future ladders noted in #approximation-tiering — scalar-vs-per-dimension tempo, AND/OR parameterization, A/B/C identification (now promoted here) — fit the separability-pattern shape. Promoting them to named ladders with explicit separable-core / structured-repair / general-open entries would extend the pattern to 8–9 ladders. Each promotion requires its own per-instance work.

- **Necessity argument for the pattern itself.** Is there a scope-honesty theorem of the form "any theory that claims exactness under Class-1-style assumptions *and* claims coverage beyond those assumptions must exhibit the separability pattern (or an equivalent three-part decomposition) to avoid latent overclaim"? If so, AAD's deployment of the pattern six times would be a *derived* structural necessity rather than a stylistic consistency. Speculative; not pursued.

- **Does C-BP2 belong in AAD core or in the wider framework narrative?** The segment currently lives in `01-aad-core/` because its instances are AAD segments. If TST adopts the same pattern across its own ladders (e.g., software-calibration-lab as a domain-axis ladder), the segment may want to move up to the root framework level. Deferred; the current placement is defensible while TST adoption is partial.
