---
slug: disc-separability-pattern
type: discussion
status: discussion-grade
depends:
  - def-strategy-dag
  - def-value-object
  - der-directed-separation
  - form-composition-closure
  - scope-edge-update-causal-validity
  - def-agent-spectrum
  - disc-approximation-tiering
  - disc-identifiability-floor
stage: draft
---

# Discussion: The Separability Pattern — Separable Core, Structured Repair, General Open

AAD consistently runs a three-part epistemic posture across state spaces that admit no tractable exact treatment in general: name the **separable core** where identification is clean, name the **structured repair** that recovers identification under explicitly-added machinery, and name the **general open** case where the problem is either intractable or structurally unidentifiable. Six ladders in the current theory share this shape. This segment names the pattern as an organizing principle, catalogs the instances, and makes the complementarity with `#disc-identifiability-floor` (which names the *negative half* of AAD's scope) explicit.

## The pattern

Each instance of the separability pattern has the form:

1. **Separable core.** A sub-class of problem in which identification is tractable by construction — the quantity of interest has a clean estimator that requires only assumptions the agent can verify or control. "Separability" here is broader than statistical independence: it names the regime in which the quantity decomposes along a structural axis (independence, additive decomposition, directed separation, strong contraction, clean intervention, etc.) without interaction terms requiring additional machinery.

2. **Structured repair.** A sub-class where the separability assumption fails but a *specific, named, bounded-cost* additional mechanism recovers identification. The repair is structured: it identifies the failure mode, adds a specific compensating construction, and typically carries a characterized loss in tightness or generality. Repairs are not "apply heuristics"; they are "augment with observability of $C$ and accept $O(1)$ per-node parameter cost," "run receding-horizon replanning at cost $\mathrm{DL}(\Sigma_t)$," or similar.

3. **General open.** The fully-general case where no tractable repair is known. This is where `#disc-identifiability-floor` instances live — structural no-go results that characterize *why* the general case remains open. Naming this boundary positively (as a known frontier) rather than negatively (as a failure) is part of AAD's load-bearing scope honesty.

## Current instances — six ladders

| Ladder | Separable core | Structured repair | General open |
|---|---|---|---|
| **Correlation** (#def-strategy-dag) | **L0** — independence model, $O(\lvert V\rvert + \lvert E\rvert)$ propagation | **L1** — strict-prerequisite augmentation with explicit common-cause node; **L1'** — soft-facilitator mixture with five-way gating under observable $C$ + facilitator monotonicity (#deriv-strategic-dynamics Prop B.7) | **L2** — full joint; **L1' unobservable-$C$** single-channel is *refuted* by Cramér-Rao floor (#disc-identifiability-floor Instance 2) |
| **Convention** (#def-value-object) | **C1** — one-step improvement | **C2** — receding-horizon replanning | **C3** — Bellman optimal; intractable for large state spaces |
| **Architecture** (#der-directed-separation) | **Class 1** — modular; directed separation holds by construction | **Class 3** — partially modular; directed separation holds for identified submodules | **Class 2** — fully merged / coupled / logogenic; needs non-modular coupled formulation (future work) |
| **Contraction** (#form-composition-closure) | **Tier 1** — strong monotonicity; bridge lemma applies with proved $\varepsilon^\ast$ | **Tier 2** — local convexity; bridge applies within a specified basin | **Tier 3** — neither; domain-specific verification required per instance |
| **Identification regime** (#scope-edge-update-causal-validity) | **Regime A** — interventional ($\iota_{ij} = 1$); action is a literal $do(\cdot)$ | **Regime B** — partial intervention ($0 \lt \iota_{ij} \lt 1$); confounder adjustment, side-channel observation | **Regime C** — observational ($\iota_{ij} \approx 0$); identification depends on external assumptions (e.g., unconfoundedness) |
| **Scope hierarchy** (#def-agent-spectrum) | **Adaptive** — basic feedback loop; #scope-adaptive-system satisfied | **Agency** — goal-bearing with $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect; adds $O_t$ and $\Sigma_t$ machinery (Section II); #scope-agency satisfied | **Composite** — multi-agent / team / logogenic; Section III gaps listed at the OUTLINE level (latent structural diversity, endogenous coupling, composition transition dynamics, agent opacity) |
| **A2'-scope** (#result-contraction-template) | **metric-α₁** — Euclidean metric, AAD-internally derived via DA2'-inc ≡ (CT2) at $M = I$ (scalar Kalman, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) | **metric-α₂** — non-Euclidean metric under explicit conditions; includes five cases (information-metric Kalman, Fisher-metric exp-family, Hessian-metric ill-conditioned, Lyapunov-metric linear-Hurwitz-non-symmetric, Lyapunov-metric PID-bounded-plant). Two of five (Fisher cases) AAD-internally forced under (PI)/Čencov per `#disc-additive-coordinate-forcing`; remaining three theorem-imported from Lohmiller-Slotine 1998 | **metric-β** — contraction-metric formulation fails (variational-to-projected-target; rule-based / non-smooth; severely misspecified; per-step SGD / human judgment) |

Each row independently satisfies the three-part shape. The shared shape is not designed-in: it arises because AAD faces seven distinct sources of intractability and applies the same posture (name the clean case, name the repair, name what remains open) to each.

## Complementarity with the identifiability floor

The **separability pattern** names the *positive half* of AAD's scope: for each ladder, what succeeds under what conditions. Each separable-core entry is a positive identification claim; each structured-repair entry is a positive identification claim *conditional on* an explicitly-named added mechanism.

The `#disc-identifiability-floor` names the *negative half*: structural no-go results (impossibility under limited information) that characterize why specific general-open cases remain open. Two floors are currently derived:

- **Instance 1** (on-policy L0-insufficiency detection via Causal Hierarchy Theorem) — forbids L0/L1 distinction from purely on-policy data. The positive counterpart: the **separable core under observable sibling covariance** is the unique broadly-available violation of the no-go's scope, naming what the agent *can* observe to escape the floor.
- **Instance 2** (L1' unobservable-$C$ single-channel via Cramér-Rao) — forbids mixture-parameter identification when $C$ is unobservable. The positive counterpart: the **structured repair under observable $C$** (Prop B.7 with facilitator monotonicity) is the identification-succeeds-under-augmentation claim matching the no-go's "unless $C$ is observable or multi-child observation is available" scope exit.

Together, the two meta-segments mark AAD's scope at two epistemic layers:

- **Separability pattern** — "here is what succeeds, with clean conditions and explicit repairs."
- **Identifiability floor** — "here is what structurally cannot succeed without specific information augmentation."

Neither alone gives the full picture. A theory stating only the positive half looks unbounded in its claims; a theory stating only the negative half looks conservative in a way that hides its achievements. Together they give scope honesty at both extremes.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. The segment is a presentational organizing principle. It names a shared shape that AAD already runs across multiple ladders; the pattern itself is not derived and has no theorem of its own. The individual ladder entries retain their own epistemic status — Correlation hierarchy results are at the tier specified in #def-strategy-dag and #deriv-strategic-dynamics; Convention hierarchy monotonicity is at the tier specified in #def-value-object; Contraction tier taxonomy is at the tier specified in #form-composition-closure; etc.

Max attainable: *discussion-grade* for the meta-pattern (it is an organizing principle, not a derivation). Individual instances are at their own tiers as above. The six-ladder enumeration could become *robust-qualitative* if a uniqueness argument were derived showing that separable-core / structured-repair / general-open is the unique viable posture across scope-parameterized hierarchies under AAD's scope-honesty architectural principle — but this is not currently in hand, nor clearly attainable.

## Discussion

**The pattern is load-bearing for how AAD presents its results.** A common failure mode of applied theories is the binary "exact under assumption X, breaks otherwise" presentation. The separability pattern refuses this presentation across six instances: where X fails, a named lower tier takes over with a characterized weaker result, and the theory provides a diagnostic for when to escalate (per #disc-approximation-tiering's AT4 component). Readers who learn the pattern once can navigate any instance; this is what makes AAD tractable as an integrating framework rather than a pile of instantiations.

**Relationship to #disc-approximation-tiering.** This segment is complementary to #disc-approximation-tiering, not redundant with it. #disc-approximation-tiering names the *structural template* (AT1 parameter indexing tractability; AT2 proved monotonicity between tiers; AT3 graceful degradation; AT4 ascension diagnostic) — the how-it-works of each tiering. This segment names the *epistemic posture* (separable core, structured repair, general open) — the what-each-tier-commits-to. Both are needed: #disc-approximation-tiering explains what makes a successful tiering; this segment explains the shape of the commitment each tier makes about identification.

**Relationship to #disc-independence-audit.** #disc-independence-audit catalogs the *independence assumptions* whose failure degrades results; this segment catalogs the *ladders of recovery*. Together with #disc-approximation-tiering they form a three-part characterization of AAD's scope:

- **#disc-independence-audit** — where the boundaries are (which assumptions, what breaks if they fail).
- **#disc-approximation-tiering** — how to navigate within the boundaries (parameterized hierarchy + monotonicity + ascension).
- **#disc-separability-pattern** (this) — what each tier positively commits to (separable core / structured repair / general open).

**The pattern is distinctive to AAD's integration-over-invention character.** Approximation tiering with a separability posture is a common move in applied mathematics — it appears in numerical methods (exact vs. high-order vs. low-order with error bounds), in statistical inference (parametric separable-core / semiparametric repair / nonparametric open), in causal identification (Pearl's three-layer hierarchy is itself an instance). AAD's contribution is not the pattern but its deployment across the six specific intractable problems adaptive-agent theory faces, each with its own positive-half identification claims and negative-half floor instances.

**The A2' sub-scope partition is a proper three-part ladder via #result-contraction-template.** The A2' partition carries three tiers: sub-scope α (A2' derived under `#der-gain-sector-bridge` directional fidelity) as the separable core; sub-scope metric-α₂ (non-Euclidean metric under explicit conditions — five cases, with two Fisher-metric cases AAD-internally forced under the (PI)/Čencov fourth primary instance of `#disc-additive-coordinate-forcing`) as the structured-repair middle tier; sub-scope β (A2' assumed) as the general-open tier. A2'-scope therefore qualifies as the seventh ladder of this meta-pattern, as enumerated in the table above. The structured-repair middle tier closes what would otherwise be a binary α/β partition lacking a derivable middle ground.

**The software calibration-lab framing (#obs-software-epistemic-properties) is a specific instance.** C-BP3's calibration-lab reframing (commit `d0373fc`) partitions operational domains into "separable core" (software, where identification conditions P1–P6 are cleanly satisfied) and "structured-repair / general open" (other domains, which inherit under explicitly-named transfer assumptions). This is a domain-axis instance of the same pattern — software is the domain-axis separable core; the transfer-assumption table is the domain-axis structured-repair specification.

## Working Notes

- **Standalone-paper candidacy.** This meta-pattern is a candidate for standalone publication per the *B-N-Sep* portfolio entry. The strategic plan (paper structure, prior-art landscape, cite-and-extend anchors, venue analysis, effort estimate) lives at [`msc/separability-standalone-paper-proposal.md`](../../msc/separability-standalone-paper-proposal.md), which subsumes the equivalent section in `~/src/ops/papers/03-asf-tier2-and-cross-segment.md`. **Verified novel** by independent prior-art search: Undermind 31-paper full-text sweep (2026-05-04) returned no exact named cross-domain meta-pattern; closest neighbors are Hintikka 1991 (general theory of identifiability), Pearl/Shpitser ID lineage (most-developed within-domain instance), Bareinboim 2022 (cross-hierarchy meta-discussion at N=2-3 hierarchies), Basse-Bojinov 2020 (modern formal abstraction across fields), Maclaren-Nicholson 2019 (ill-posed inverse problems as cross-field dual structure). Full report at [`ref/separability-ladder-prior-art-report.md`](../../ref/separability-ladder-prior-art-report.md).

- **Citations to land on promotion to draft / when paper drafting begins:**
   - **Hintikka, J. (1991).** *"Towards a General Theory of Identifiability."* In *Definitions and Definability: Philosophical Perspectives*, J. H. Fetzer et al. (eds.), Kluwer Academic. DOI: 10.1007/978-94-011-3346-3_7. Locally at [`ref/towards-a-general-theory-of-identifiability.pdf`](../../ref/towards-a-general-theory-of-identifiability.pdf). **Strongest older abstract anchor**: tripartite *definable / identifiable / non-identifiable* trichotomy. Hintikka §1: "P is identifiable on the basis of T[P]" when "the interpretation of P is not determined on the basis of the theory alone, but is determined by the theory together with a number of auxiliary empirical results." The pattern's middle rung in Hintikka's vocabulary; ASF's structured repair generalizes "auxiliary empirical results" to "named bounded-cost structural augmentation" (a real but small extension).
   - **Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022).** *"On Pearl's Hierarchy and the Foundations of Causal Inference."* In *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books. DOI: 10.1145/3501714.3501743. Treats Pearl's hierarchy as a logical and epistemic hierarchy and compares it to formal-language and complexity hierarchies — closest existing cross-hierarchy meta-discussion at N=2-3, but stops short of the cross-domain meta-pattern this segment names.
   - **Robins, J., Richardson, T. & Shpitser, I. (2020).** *"An Interventionist Approach to Mediation Analysis."* In *Probabilistic and Causal Inference*, ACM Books. DOI: 10.1145/3501714.3501754. Cleanest in-domain cite-and-extend anchor: clean separable case + structured-repair via expanded-graph decomposition + recanting-witness no-go.
   - **Shpitser, I. & Pearl, J. (2006, 2008).** *"Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models"* (AAAI); *"Complete Identification Methods for the Causal Hierarchy"* (JMLR 9). Foundational ID completeness papers — the cleanest verified no-go-plus-recovery pairing; the ID algorithm IS this template within causal inference.
   - **Bareinboim, E. & Pearl, J. (2012, 2014); Lee, S., Correa, J. D. & Bareinboim, E. (2019).** Surrogate experiments (z-identifiability), transportability with limited experiments, general identifiability with arbitrary surrogates. Each is a structured-repair instance with a named bounded augmentation. Several locally at `ref/`.
   - **Basse, G. W. & Bojinov, I. (2020).** *"A general theory of identification."* Closest modern formal abstraction across fields (identifiable / partially-identified / strongly-non-identifiable regimes); lacks the bounded-cost-repair operator as middle rung.
   - **Maclaren, O. J. & Nicholson, R. (2019).** *"What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems."* arXiv 1904.02826. Best dual-structure cross-field neighbor (causal identification ↔ ill-posed inverse problems); centers on stability/regularization rather than structured-repair.
   - **Restricted-intervention lineage:** Robins 1986 (treatment-regime semantics; locally at `ref/`); Richardson 2013 SWIGs; Dawid 2000 ("causal inference without counterfactuals"; locally at `ref/`); Dawid 2020 (decision-theoretic foundations); Richardson-Robins 2023 (SWIG/decision-theoretic bridge). Patches the missing-prior-art lineage for restricted/regime-defined intervention semantics.
   - **Neighboring recurrence inside causal identification:** Robins-Richardson 2010 (alternative graphical models, expanded graphs); Stensrud et al. 2019 (separable effects in competing events); Díaz 2022 (non-agency interventions); Shpitser-Tchetgen 2014 (intervention hierarchy unification). Pattern recurs in mediation, competing-events, edge-intervention settings within wider causal-identification literature.
   - **Adjacent abstractions that stop short:** Iwasaki-Simon 1994 (causality and model abstraction; near-decomposability); Hoover 2012 (causal structure and hierarchies of models; well-made-toaster vs repairman cases). Strong philosophy-and-Simon-line parallels; not a formal tractability/identifiability ladder. Downey-Fellows 1995/1999 (parameterized complexity, FPT/W[1]/paraNP-hard) and Simpson 1999 (reverse mathematics) for hierarchy-of-strength formalisms; verified weak connection to applied-identifiability ladders.

- **Pending family rename and rung-rename decision.** The family name is queued for rename: `discussion-separability-pattern` → `discussion-separability-ladder`, on Round-1 consensus rationale that "ladder" is more evocative for the three-rung shape than "pattern" (which is generic). See [`msc/naming/naming-rename-plan.md`](../../msc/naming/naming-rename-plan.md) §"Deferred to refined Round 1 / Round 2". The **three rung-names** (currently *separable core* / *structured repair* / *general open*) are also under consideration for refinement; Hintikka 1991's *definable / identifiable / non-identifiable* trichotomy is a strong candidate for an aligned echo (modulo a small extension on the middle rung from "auxiliary empirical results" to "named bounded-cost structural augmentation"). Decision deferred (2026-05-04). The standalone-paper proposal (above) is ready to draft against either the status-quo names or any of the alternates — the rename can land separately with no impact on paper-drafting tractability.

- **Cross-ladder monotonicity.** The six ladders interact — an agent operating at L0 correlation + C2 convention + Class 1 architecture + Tier 1 contraction + Regime A identification + Agency scope is in a specific combined regime. Does cross-ladder monotonicity hold in any direction? E.g., does moving from L0 to L1 change anything about the Convention hierarchy's guarantees, or do the ladders factor independently? `#disc-approximation-tiering`'s Working Notes flag this as an open question; the separability pattern's complementarity with the identifiability floor adds a further axis (which combinations are known-unidentifiable per #disc-identifiability-floor).

- **Extension candidates beyond the six.** Three candidate future ladders noted in #disc-approximation-tiering — scalar-vs-per-dimension tempo, AND/OR parameterization, A/B/C identification (now promoted here) — fit the separability-pattern shape. Promoting them to named ladders with explicit separable-core / structured-repair / general-open entries would extend the pattern to 8–9 ladders. Each promotion requires its own per-instance work.

- **Necessity argument for the pattern itself.** Is there a scope-honesty theorem of the form "any theory that claims exactness under Class-1-style assumptions *and* claims coverage beyond those assumptions must exhibit the separability pattern (or an equivalent three-part decomposition) to avoid latent overclaim"? If so, AAD's deployment of the pattern six times would be a *derived* structural necessity rather than a stylistic consistency. Speculative; not pursued.

- **Does C-BP2 belong in AAD core or in the wider framework narrative?** The segment currently lives in `01-aad-core/` because its instances are AAD segments. If TST adopts the same pattern across its own ladders (e.g., software-calibration-lab as a domain-axis ladder), the segment may want to move up to the root framework level. Deferred; the current placement is defensible while TST adoption is partial.
