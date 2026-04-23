# Spike: Triaging the Four Candidate `#identifiability-floor` Instances

*Started 2026-04-24. Research / analytic spike. Not canon. No segment files modified.*

**Status.** Triage spike for the gating decision on which (if any) of four candidate instances should promote to `#identifiability-floor`, in what order, with what subsumption structure, and with what effect on the meta-segment's growth.

**Mandate.** Do not default to "admit all four"; do not default to "pick a winner." Extract the five-element test from Instances 1–3, apply it to each candidate, identify subsumptions, evaluate the three-layer `#loop-interventional-access` chain claim, and state a recommended promotion plan — all with epistemic tier labels throughout.

**Top-line outcome.** The triage resolves cleanly once the five-element test is made precise and a *layer-taxonomy* view is adopted. Result (*robust qualitative*): **candidates are not four siblings but a layered 1 + 1 + 1 structure** — one genuine new primary instance (Candidate 2, agent-internal architecture layer); one structural sharpening of an existing instance rather than a new sibling (Candidate 3, better framed as "Instance 1 acquires a fourth escape via (PI) + Fisher-Rao, under the universal-$C$-under-non-(PI)-norm obstruction"); one sub-instance of Candidate 2 at the disturbance-statistic projection (Candidate 1, should be cross-referenced from both `#identifiability-floor` *and* the proposed `#rho-decomposition` appendix rather than counted as a standalone); and one genuine fifth-instance candidate at a distinct layer (Candidate 4, multi-agent-aggregation / mechanism-design) *provided* its external theorem's character is honestly labeled. The meta-segment stays at "structurally bounded, currently at 3+2" after these moves — principled growth, not catalog drift.

The three-layer `#loop-interventional-access` chain claim is *real at the pattern level but non-identical in mechanism*: the escape-via-intervention operates on semantically different interventional quantities at each layer (do-on-environment vs. do-on-sub-agent vs. do-on-correction-function-input). The shared load-bearing role is the unification; the specific escape-channel is not. Naming the pattern honestly is the strengthening move; collapsing the three to a single machinery overreaches.

---

## 1. Extracting the test: the five-element shape of `#identifiability-floor`

The meta-segment states the pattern as five elements: *setting / external theorem / no-go / boundary characterization / strengthened consequence*. Each of Instances 1–3 matches. Before applying this to candidates, tighten each element to a criterion strict enough to reject pattern-matching and generous enough to admit legitimate siblings.

### 1.1 Element-level criteria

**(E1) Setting.** A specific AAD inferential task — detect / identify / distinguish — under an *explicitly named information regime* that limits what the agent or observer has access to. The restriction is load-bearing: a setting like "identify $X$ using everything the agent can ever observe" is too broad; a setting like "identify $X$ using on-policy data only, under exploration rate $\varepsilon = 0$, single observation channel" is correctly scoped.

Instances 1–3 all meet (E1): on-policy observation history under sequential short-circuit AND/OR execution (I1); single-channel single-child observation with $C$ unobservable (I2); component-level marginal trajectories with no observation of coupling topology (I3).

**Criterion.** A candidate meets (E1) iff it names both the inferential task and a specific regime that restricts access in a way that makes the no-go sharp.

**(E2) External theorem.** A *published, citable, mature* information-theoretic or formal-science theorem — not derived in AAD — that delivers the impossibility. The external theorem must be doing the work; the AAD content is the *application*, not re-derivation. The theorem is named with its canonical reference.

Instances 1–3 all meet (E2) explicitly: Bareinboim-Correa-Ibeling-Icard (2022) CHT; Cramér 1946 Cramér-Rao; Liberzon 2003 common-Lyapunov-nonexistence anchored by Dayawansa-Martin 1999 counterexample and Shorten-Wirth-Mason-Wulff-King 2007 review.

**Criterion.** A candidate meets (E2) iff the external theorem is cited with a canonical reference and the no-go is derivable by invoking it, not by re-arguing the no-go from first principles.

**(E3) No-go.** A statement of the form "under the regime in (E1), no [estimator / detector / procedure] can [perform the (E1) task]" that *follows from (E2)* as the AAD-relevant application. The no-go is *exact* in the sense that a specific construction or a specific citable theorem underwrites it — not merely pattern-matched.

Instances 1–3 all meet (E3) at standards clearly stated. I1 gives an explicit construction ($\mathcal W_{L0}^\ast$ with matched on-policy conditionals). I2 gives the Fisher rank-1 calculation (two-dimensional null space, smallest eigenvalue zero, no SA1-preserving update with sector parameter $\alpha \gt 0$). I3 gives the $\pm \gamma_0$ coupled-system construction with matching marginal disturbance bound $\rho + |\gamma|\mathcal T$.

**Criterion.** A candidate meets (E3) iff the no-go is backed by either (a) an explicit AAD-level counterexample construction, or (b) a direct derivation-step from the external theorem in (E2). Pattern-match alone does not clear the bar.

**(E4) Boundary characterization.** Explicit escape routes, *each mapped to AAD machinery already in the theory* (or explicitly adjacent machinery with honest credit). The escapes are not a laundry list of "observe more"; they are specific operational mechanisms that match specific AAD segments or established external capabilities.

Instances 1–3 meet (E4) with 5 / 3 / 4 escape routes respectively, each mapped.

**Criterion.** A candidate meets (E4) iff at least two distinct escape routes are named, each mapped either to an existing AAD segment or to a clearly-adjacent external capability. If every escape collapses to a single capability, the candidate does not have real boundary structure; it has a single-step "you need capability $X$" claim, which is weaker than a floor instance.

**(E5) Strengthened consequence.** The floor *elevates* the load-bearing role of AAD machinery named in (E4) — typically from "useful" to "structurally required." This is the positive-content half of the no-go: the machinery the theory has is revealed to be doing load-bearing work it was not previously known to do.

Instances 1–3 meet (E5): `#loop-interventional-access` elevated at the causal-sufficiency layer (I1); observability-as-information-augmentation (the "instrument $C$" engineering move) elevated from convenience to prerequisite (I2); `#critical-mass-composition`, composite-extended `#loop-interventional-access`, and `#composition-scope-condition` each elevated to structural-requirement status at the composition layer (I3).

**Criterion.** A candidate meets (E5) iff naming the floor *does new work* for existing AAD machinery — either elevates its status, completes a pattern, or surfaces a role previously implicit.

### 1.2 The five-element test, compactly

| Element | Criterion |
|---|---|
| E1 Setting | Named task + named information-restricting regime |
| E2 External theorem | Cited, published, delivers the no-go |
| E3 No-go | Explicit construction or direct step from E2 |
| E4 Boundary characterization | ≥ 2 escape routes, each mapped to AAD or clearly-adjacent machinery |
| E5 Strengthened consequence | Elevates load-bearing role of existing AAD machinery |

*Tier of the test itself:* **Discussion-grade**. The five elements are read off Instances 1–3 and are consistent with them by construction; they are not derived from a separate meta-theorem. The test is a reviewer heuristic, not a theorem.

---

## 2. Applying the test to each candidate

### 2.1 Candidate 1 — Rate-multiplicative factorization no-go (ρ-additive spike §4)

| Element | Assessment |
|---|---|
| E1 | **Passes.** Task: express $\rho^2$ as $\rho^2_{\text{env}} \cdot f(\mathcal M) \cdot g(\pi)$. Regime: generic sub-scope $\alpha$ with non-degenerate environment noise, non-trivial model class. |
| E2 | **Weak pass.** The "external theorem" is the volatility-identifiability obstruction — process vs. observation noise cannot collapse to a single scalar when they interact non-trivially with misspecification. This is mathematically correct but the *canonical reference* is not a single named theorem in the way CHT, Cramér-Rao, and Liberzon-2003 are. The underlying identities (Bienaymé 1853 variance-additivity, Kalman Riccati monotonicity) are each standard but no one of them is "the obstruction theorem"; the no-go is a composition of several. |
| E3 | **Discussion-grade.** The §4 derivation is by contradiction via two Kalman scenarios (A: $\sigma^2_{\text{proc}} + \sigma^2_{\text{obs}}$ given; B: rebalanced such that sum is unchanged). The argument structure is correct but the spike itself labels it "Discussion-grade proof; the structure is correct but the counterexample construction is informal." A crisp closed-form Kalman counterexample is ~1 page of algebra but not yet written. |
| E4 | **Weak pass.** The escape is (AV) variance-additive form with cross-terms, plus a sub-regime catalog ($\alpha_1^{MC}$ Poisson cascade, $\alpha_1^{\text{TAIL}}$ large-deviation, $\alpha_1^{\text{small-}\Delta}$, $\alpha_1^{\text{indep}}$). Counting narrowly: one escape (AV) with several sub-regimes where *multiplicative* is restored — so the structure is "one general escape + refinements" rather than "several structurally distinct escapes." Different shape from Instances 1–3. |
| E5 | **Strengthens a *proposed* appendix, not an existing segment.** The floor elevates the yet-to-be-promoted `#rho-decomposition` / `#internal-external-decomposition` and refines `#sector-persistence-template`, `#separability-pattern`, and `#additive-coordinate-forcing`. No elevation of an existing load-bearing segment at the standard I1–I3 produce. |

**Verdict (robust qualitative).** Candidate 1 clears the pattern shape but not at Instance 1–3 standards. Its external theorem is a composition rather than a single named theorem; its no-go construction is informal pending the Kalman tightening; its escape structure is "one form with sub-regimes" rather than multiple structural escapes; and its strengthened consequence lives on yet-to-promote segments. **This is a sibling-of-siblings more than a sibling-in-kind.**

More importantly (see §3.1 below), Candidate 1 is plausibly a *sub-instance* of Candidate 2 at the disturbance-statistic projection layer.

*Tier of this verdict:* **Robust qualitative.** The pattern-match assessment is defensible; the subsumption claim in §3 is where the load-bearing structural work lives.

### 2.2 Candidate 2 — Agent-internal architecture-within-behavior-class no-go (neutral-drift spike §8)

| Element | Assessment |
|---|---|
| E1 | **Passes.** Task: distinguish two agents $A, A'$ with identical $(\alpha, R)$-summary observable behavior. Regime: on-policy, in-regime, $(\alpha, R)$-summary-only observation — a sharp and natural restriction given AAD's Section II state-summary structure. |
| E2 | **Passes with dual anchor.** Bareinboim et al. 2022 CHT at the agent-as-SCM layer is the primary anchor (treating each agent as an SCM over its state space, two SCMs can agree on Level-1 observation data and disagree on Level-2 interventional data). Kalman-Ho canonical-form non-uniqueness (Kalman 1963; Ho-Kalman 1966) is the sharper anchor for the linear-Gaussian sub-scope. Both are canonically citable. The dual-anchor structure is honest: CHT for general no-go, Kalman-Ho for the tight linear-Gaussian sub-case. |
| E3 | **Sketch at the top, solid at the sub-scope.** The spike's §8.3 is explicit that a crisp closed-form no-go construction at the level of I1 / I3 exists for the linear-Gaussian sub-case (two Kalman filters with identical innovation-sequence spectra but different state-space realizations — Kalman canonical-form ambiguity, classical). The pattern-level claim is therefore robust-qualitative, *sharper* than I1's general-DAG pattern, and has a crisp closed form in the natural sub-case. |
| E4 | **Passes.** Four distinct escapes: (a) loop-interventional access; (b) horizon-extended or out-of-regime $H_b$; (c) higher-moment observation in nonlinear sub-scope; (d) architecture instrumentation. Three of four (a/b/c) are mapped to AAD segments (`#loop-interventional-access`, `#agent-opacity`, `#interaction-channel-classification` and the nonlinear sub-scope contraction-template segments). The fourth (d) is clearly adjacent (breaking black-box scope). |
| E5 | **Passes with pattern-level work.** Elevates `#loop-interventional-access` to a *third* load-bearing role (after I1 causal-sufficiency and I3 composition) — the headline strengthening claim. Elevates `#agent-opacity`'s horizon-indexing and `#interaction-channel-classification`'s regime-histogram to "structurally required diagnostic instruments, not optional ones." Adds explicit Discussion scope-limit content to `#sector-persistence-template`. |

**Verdict (robust qualitative → exact in linear-Gaussian sub-case).** Candidate 2 clears the five-element test at Instance 1–3 standards. The pattern-level claim is robust qualitative; the linear-Gaussian sub-case (via Kalman canonical-form) is structurally crisp. **This is a genuine sibling of Instances 1–3.**

*Tier of this verdict:* **Robust qualitative** at the pattern level; **Exact in sub-scope $\alpha_1$ linear-Gaussian** once the Kalman-Ho anchor is tightened in the segment-level promotion (estimated ~1–2 pages). The only flag is the three-layer chain claim (§4 below), which is genuinely load-bearing but should be articulated honestly rather than overclaimed.

### 2.3 Candidate 3 — Universal-$C$-under-non-(PI)-norm no-go (bias-bound spike Attempt E)

| Element | Assessment |
|---|---|
| E1 | **Weak pass.** Task: is there a *universal constant* $C$ (independent of $\mathcal M$'s geometry, likelihood form, coupled-update structure) such that $\lVert \Delta M_{\text{bias}} \rVert \leq C \cdot \kappa_{\text{processing}} \cdot I$? Regime: norm on $\mathcal M$ is Euclidean on a parameter vector (or any other non-(PI)-invariant norm). This is a sharply-scoped setting, but it is a *meta-question about theorem-form* rather than about an *agent's inferential capacity under a data regime*. |
| E2 | **Pass but of a different kind.** The external "theorem" is Čencov's 1982 invariance theorem in its negative corollary: no coordinate-invariant Riemannian metric other than Fisher (up to scale) exists on a statistical manifold. Combined with non-compactness of generic parameter spaces, Fisher-metric condition number can be unbounded. This is canonically citable (Čencov 1982; Ay-Jost-Lê-Schwachhöfer 2017). |
| E3 | **Passes.** Explicit construction in Attempt E: heteroscedastic normal family $\{N(0,\sigma^2)\}$, Fisher information $2/\sigma^2$, fixed 1 nat of goal-conditional KL induces Euclidean-$\sigma$ displacement $\sigma$; taking $\sigma \to \infty$ gives arbitrarily large displacement. Counterexample-grade. |
| E4 | **Single escape.** The *unique* escape is adoption of (PI) + Fisher-Rao norm. Under the escape, $C = \sqrt{2}$ universal. No alternative escapes in the spike; the (PI) commitment *is* the escape. This is a 1-escape structure, not the ≥2-escapes criterion E4 requires. |
| E5 | **Strengthens (PI) itself, which is already load-bearing.** The floor elevates (PI) from "adopted axiom in `#agent-identity`" to "load-bearing for the bias-bound theorem form." But (PI) is already a primary instance of `#additive-coordinate-forcing` (the Čencov / Fisher-metric instance) at the metric layer. This is not a *new* strengthening of existing machinery; it is a *re-use* of existing Fisher-Rao / (PI) machinery at a downstream theorem. |

**Verdict (robust qualitative).** Candidate 3 shares the five-element pattern shape but **fails criterion E4** (single escape, not multiple). It also fails E5 at the sibling-to-I1-I3 standard: the "strengthening" is re-use of the (PI) machinery that `#additive-coordinate-forcing`'s fourth primary instance already carries, not a genuinely new strengthening. The spike itself observes "the Fisher-Rao-$C = \sqrt{2}$ result *consumes* the fourth instance (Čencov-invariance / (PI)) rather than introducing a fifth axiomatic layer."

**Recommended re-framing:** Candidate 3 is structurally *not a new instance of `#identifiability-floor`*; it is a **fourth escape route for Instance 1** (or a *downstream theorem* of `#additive-coordinate-forcing`'s fourth primary instance) — specifically: under the universal-$C$-under-non-(PI)-norm obstruction, (PI)-adoption is the unique escape, and *given* (PI)-adoption, Čencov-forced Fisher-Rao is the unique norm, and *given* Fisher-Rao, $C = \sqrt 2$ is forced. Three uniqueness steps, each downstream of `#additive-coordinate-forcing` Instance 4, landing in `#bias-bound-derivation` as a theorem rather than as an identifiability floor.

*Tier of this verdict:* **Robust qualitative**. The verdict follows from the five-element test and from the spike's own observation that Candidate 3 "consumes" rather than "introduces" structure.

### 2.4 Candidate 4 — Mechanism-design no-go (pre-existing `#identifiability-floor` Working Note)

| Element | Assessment |
|---|---|
| E1 | **Passes with caveat.** Task: can an outside designer shape sub-agents' $\{O_t^{(i)}\}$ so that the induced strategic equilibrium coincides with a desired joint state. Regime: constraints on the mechanism (dominant-strategy implementability, individual rationality, incentive compatibility, budget balance, etc., case-specific to theorem). |
| E2 | **Passes but of a structurally different kind.** External theorems: Gibbard-Satterthwaite 1973-75; Myerson-Satterthwaite 1983; Arrow 1951. These are *social-choice / mechanism-design impossibility theorems*, not information-theoretic identifiability theorems. They forbid *implementability* under stated constraints — "no mechanism exists satisfying all of P1..Pn simultaneously" — not "no estimator can identify parameter $\theta$ from data." This is a **different kind of external theorem** from Instances 1–3's CHT / Cramér-Rao / common-Lyapunov-nonexistence. |
| E3 | **Passes.** Each theorem cited has a canonical derivation; the AAD application is one step: composite-design task under constraint-set $K$ is forbidden by Arrow / G-S / M-S. |
| E4 | **Escapes exist, multiple, canonically documented in the mechanism-design literature.** Bayes-Nash in place of dominant-strategy (G-S escape); randomized allocations (Arrow escape via strategy-space restriction); subsidy injection (M-S escape). Also: strategy-space restriction (single-peaked preferences for G-S); domain restriction. The spike-level inventory supplies ≥ 4 escapes. |
| E5 | **Strengthens `#strategic-composition`'s sub-scope $\alpha'$ potential-game conditions.** The potential-game machinery (Monderer-Shapley) becomes a structurally load-bearing target for mechanism design — the *positive* structure is exactly what mechanism design must steer sub-agents toward. Reasonable strengthening, though the existing `#strategic-composition` segment already cross-references this. |

**Verdict (heuristic → robust qualitative).** Candidate 4 clears the five-element pattern shape but with a specific flag: **its external theorem is of a different character** from Instances 1–3. Instances 1–3's external theorems are information-theoretic identifiability obstructions ("no estimator can determine $\theta$ from data type $D$"). Candidate 4's external theorems are *implementability* impossibilities ("no mechanism exists satisfying constraint-set $K$"). Whether `#identifiability-floor` accommodates both character-types is a principled question about the meta-segment's scope.

**Two coherent moves, with different consequences:**

(i) **Narrow reading.** `#identifiability-floor` is specifically about *information-theoretic identification*; mechanism-design impossibility is a different no-go family. Promote the mechanism-design instance elsewhere — perhaps a parallel meta-segment `#implementability-floor` or an extended Discussion in `#strategic-composition` — leaving `#identifiability-floor` at 3 identification-theoretic instances.

(ii) **Broad reading.** `#identifiability-floor` is a general no-go pattern: "setting → external impossibility theorem → AAD-machinery escape → strengthened-consequence." Under this reading, mechanism-design impossibility is a genuine instance at a different layer (multi-agent-aggregation). Promote as fifth instance with an explicit external-theorem-type label ("implementability" vs. "identifiability") in the instance header so readers see the distinction.

**Recommended disposition:** **Broad reading, with honest labeling.** The five-element pattern does not structurally require the external theorem to be information-theoretic; it requires it to be a *cited, published impossibility result delivering the no-go*. Gibbard-Satterthwaite / Myerson-Satterthwaite / Arrow do this. The label correction is to rename the pattern's external-theorem slot as "external impossibility theorem (information-theoretic or otherwise)" and to tag each instance with its theorem-family. This is a cheap reframe that preserves the pattern while being honest about the character distinction.

*Tier of this verdict:* **Robust qualitative** on the pattern-match; the broad-vs-narrow choice is a **formulation decision** (both positions are coherent). The recommendation for broad reading is motivated by simplicity and by the observation that the pattern's *work* is being done by the pattern shape, not by the theorems' shared information-theoretic grounding.

---

## 3. Subsumption relationships

Having run the five-element test, the structural question is whether the four candidates are independent, or whether some reduce to others. Three candidate subsumptions, evaluated:

### 3.1 Does Candidate 1 (ρ-factorization) reduce to Candidate 2 (agent-internal architecture)?

**Claim (robust qualitative):** Candidate 1 is a *projection of Candidate 2 onto the disturbance-statistic layer*.

**Argument.** Candidate 2's setting is "distinguish architecturally-different-behaviorally-identical agents $A, A'$." The $(\alpha, R)$-summary projects onto a two-dimensional sufficient-statistic for *first-order* behavioral equivalence. If we further project onto disturbance statistics — asking what two architecturally-distinct agents share and what they do not — Candidate 2's no-go reduces to Candidate 1's statement: the effective disturbance rate $\rho$ is invariant under certain architectural variations within a given model class, and that invariance is precisely what prevents the multiplicative factorization $\rho = \rho_{\text{env}} \cdot f(\mathcal M) \cdot g(\pi)$ from being derivable. The *architectural content* of $\mathcal M$ and $\pi$ is exactly what Candidate 2 says is invisible from $(\alpha, R)$ summary; the *collapse* to a single scalar $f(\mathcal M)$ in Candidate 1 is that invisibility at a lower resolution.

**What this means:** Candidate 1 is Candidate 2 *at the disturbance-statistic projection*; equivalently, it is the $(\rho^2, \Delta^2_{\mathcal M})$ slice of Candidate 2's broader no-go. Under this subsumption, Candidate 1 should **not** be promoted as a standalone instance; it should be promoted as a *named sub-statement of Candidate 2 at a named projection*, living in the proposed `#rho-decomposition` appendix with a cross-reference to `#identifiability-floor` Instance 4 (= Candidate 2).

**Strength of the subsumption claim.** *Robust qualitative.* The mapping is structurally clean (both are "architecturally-distinct-but-summary-equivalent no-goes") and the spike-level evidence is consistent: Candidate 2's spike §F (`#interaction-channel-classification` as emitter filter-signature) explicitly observes that regime-distribution histograms discriminate *within* $(\alpha, R)$-equivalence via architectural fingerprints that include observation-model differences — exactly the kind of difference Candidate 1 frames as the "two-dimensional environment noise" that cannot collapse to scalar $\rho_{\text{env}}$.

**Where the subsumption could fail.** If Candidate 1's obstruction is *fundamentally* about the environment-side structure (process vs. observation noise) rather than the agent-internal architecture, then it sits at the *environment* layer rather than the *agent-internal* layer, and the subsumption fails. Checking: Candidate 1's contradiction construction (§4.1 of ρ-spike) rebalances process and observation noise such that the sum is unchanged; the sensitivity to $\Delta^2_{\mathcal M}$ is what breaks the factorization. So the no-go's content is: *environment-side dual-dimensional structure interacts with agent-internal model-class structure in ways that cannot be collapsed.* This is a *joint* property of environment and agent, not a pure-environment property. It maps to Candidate 2 iff the "model-class structure" is interpreted as an agent-internal architectural variable, which is exactly what Candidate 2's setting does.

**Explicit uncertainty flag:** I am reasonably confident Candidate 1 subsumes to Candidate 2 *as a projection*, but the equivalent statement "Candidate 1 is fully derivable from Candidate 2's no-go under a specific projection operator" is not proved in either spike. What is proved in both spikes is that both are no-goes within the same broader "architecturally-distinct-but-summary-equivalent" family. The subsumption claim should therefore be promoted as *"Candidate 1 is a sub-statement of Candidate 2 at the disturbance-statistic projection; the exact derivation-chain is not worked out"* rather than as a theorem. This is the honest position.

### 3.2 Does Candidate 3 (constant $C$) reduce to an escape route of Candidate 1 (ρ-factorization) or Candidate 2 (agent-internal)?

**Claim (robust qualitative):** Candidate 3 is **not a new instance**; it is a *fourth escape route for Instance 1* (alternatively: a downstream theorem of `#additive-coordinate-forcing`'s fourth primary instance).

**Argument.** Re-read Candidate 3's structure: the no-go is "universal $C$ under non-(PI) norm does not exist"; the escape is "(PI) + Fisher-Rao"; the downstream theorem is "$C = \sqrt 2$ under the escape." The no-go and escape are 1:1 — one obstruction, one escape, one downstream theorem. This is not a *floor* in the sense of Instances 1–3, each of which has multiple structural escapes carving out a *space* of operational routes. It is a *uniqueness theorem*: the escape is forced, not chosen among alternatives.

Matching this against the five-element test: the single-escape structure fails E4. What Candidate 3 actually is: a **uniqueness result for the bias-bound constant under parameterization-invariance**, landing in `#bias-bound-derivation` as a theorem; the "no-go" half is a *motivating justification* for the (PI) scope gate, not a floor in its own right.

**Alternative framing: Candidate 3 as "Instance 1 acquires a fourth escape via (PI)."** In Instance 1, one of the five escapes is exploration ($\varepsilon$-violation), and another is direct intervention on the candidate latent. Neither currently routes through (PI) / Fisher-Rao. If (PI)-adoption opens an additional escape in Instance 1 — e.g., under Fisher-Rao norm, certain mixture-identifiability obstructions weaken — then Candidate 3 could be framed as "Instance 1 picks up a fourth escape via (PI)." But the specific obstruction Candidate 3 addresses (universal-$C$-bound) is not the same obstruction Instance 1 addresses (on-policy L0/L1 indistinguishability). The semantic content differs.

**Honest reframe:** Candidate 3 is best understood as a **derived theorem downstream of `#additive-coordinate-forcing`'s fourth primary instance**, not as an instance of `#identifiability-floor`. It belongs in `#bias-bound-derivation` (proposed appendix) with a Discussion cross-reference noting that the (PI)-as-load-bearing observation shares structural shape with the floor pattern but does not match its five-element criteria. The spike itself reaches this conclusion ("not as a new primary instance") for the parallel question about `#additive-coordinate-forcing`; the conclusion for `#identifiability-floor` is the same.

*Strength of this claim:* **Robust qualitative**, with the further structural observation that *the spike itself acknowledges this* in §4: "Is $C$ a fifth instance of `#identifiability-floor`? Possibly." The "possibly" softens to "no, not by the five-element test" once E4 is applied strictly.

### 3.3 Does Candidate 4 (mechanism-design) sit at a different layer from Candidates 1–3?

**Claim (robust qualitative):** Candidate 4 sits at the **multi-agent-aggregation layer** — a layer distinct from the single-agent layer (Candidate 2), the within-agent disturbance-statistic layer (Candidate 1), and the composition coupling-sign layer (Instance 3). It does not compete with or subsume any other candidate.

**Argument.** The Instance-1 / Instance-2 / Instance-3 layer taxonomy is:
- I1: causal-structure layer (single agent, within its DAG)
- I2: mixture-parameter layer (single agent, L1' soft-facilitator)
- I3: composition layer (multi-agent, coupling-sign from component marginals)

Candidate 2 adds: I4 agent-internal-architecture layer (single agent, architecture-within-behavior-class).

Candidate 4 sits at: multi-agent-aggregation layer (a designer attempting to aggregate $\{O_t^{(i)}\}$ into a desired joint-state-inducing equilibrium). The task is *design* rather than *inference*; the obstructions are *implementability* rather than *identifiability*. Under the broad reading of `#identifiability-floor` (where the pattern accommodates multiple external-theorem families), this is a genuine fifth layer, not a duplicate of any existing layer.

**No subsumption with 1–3:** Candidate 4's obstruction (Arrow / G-S / M-S) is fundamentally about *constraint-set inconsistency* among social-choice requirements; it is not derivable from CHT, Cramér-Rao, or common-Lyapunov-nonexistence. The external-theorem families are disjoint.

*Strength of this claim:* **Robust qualitative**. The layer-taxonomy view (see §6) makes this visible cleanly, and no spike-level argument suggests subsumption in either direction.

### 3.4 Subsumption summary

| Candidate | Subsumes to | As |
|---|---|---|
| 1 (ρ-factorization) | Candidate 2 at the disturbance-statistic projection | Named sub-statement, not standalone instance |
| 2 (agent-internal) | — (primary) | Genuine new instance I4 |
| 3 (constant $C$) | Downstream theorem of `#additive-coordinate-forcing` Instance 4 | Not a `#identifiability-floor` instance; belongs in `#bias-bound-derivation` |
| 4 (mechanism-design) | — (primary, at different layer) | Genuine new instance I5 under broad reading |

**Net:** Four candidates → **two genuine new primary instances** (Candidates 2 and 4) + **one sub-statement cross-reference** (Candidate 1 under Candidate 2) + **one redirect to a different meta-segment** (Candidate 3 to `#additive-coordinate-forcing` / `#bias-bound-derivation`).

*Tier of the subsumption summary:* **Robust qualitative** throughout. None of the four subsumption conclusions rests on a closed-form derivation-chain; each rests on the five-element test applied to the spike-level evidence, plus the layer-taxonomy structural view.

---

## 4. The three-layer `#loop-interventional-access` chain claim — evaluated

Candidate 2 claims that its promotion would make `#loop-interventional-access` load-bearing at three layers: causal-structure (I1) / composition (I3) / agent-internal (I4). This is the headline strengthening in Candidate 2's spike §8.1.

The claim needs unpacking because it conflates two different assertions: (a) *the same machinery (do-operations by the agent) escapes the floor at each of the three layers*, versus (b) *the three instances are genuinely the same kind of escape-via-intervention, with a shared mechanism*. Claim (a) is true; claim (b) is more delicate.

### 4.1 What `#loop-interventional-access` does at each layer

**At I1 (causal-sufficiency).** The agent performs do-actions on its action space; joint sibling observability under exploration generates $do(a_i)$-data that supports the pairwise covariance test for common-cause detection. The intervention is *on the agent's own action*, and the target of the intervention is the environment's response to that action. The escape mechanism: agent-generated do-data breaks Bareinboim's on-policy observational-equivalence construction.

**At I3 (composition / coupling-sign).** The composite-extended form: an *observer* intervenes on *sub-agent $A_j$'s* actions; this reveals $A_i$'s cross-coupling response. The intervention is *on a sub-agent*, and the target is another sub-agent's mismatch trajectory. The escape mechanism: $do(\cdot)$-on-sub-agent data distinguishes cooperative vs. adversarial coupling signs.

**At I4 (agent-internal architecture).** An *observer* performs a perturbation probe on the candidate agent's input stream, staying within the agent's sector region but probing a direction the agent has not sampled. The intervention is *on the agent's input*, and the target is the agent's correction-function response. The escape mechanism: agent correction-function response-to-perturbation differs between architecturally-distinct agents, which is a Level-2 signature of the architecture.

### 4.2 What's shared and what isn't

**Shared (robust qualitative):** The broader *family* of escapes is "agent-as-Level-2-data-generator" — at each of the three layers, the agent's embedding in a feedback loop (or under an observer's intervention) converts on-policy observational equivalence into interventional distinguishability. `#loop-interventional-access` is the AAD segment that names the underlying capability; the three floor escapes are specific deployments.

**Not shared:**
- **Who intervenes.** I1: the agent itself (as part of its adaptive loop). I3: an observer external to the composite. I4: an observer external to the single agent.
- **What is intervened on.** I1: the agent's action. I3: a sub-agent's action. I4: the agent's input stream.
- **What is revealed.** I1: environment's response (the latent common cause's effect on sibling actions). I3: cross-coupling sign between sub-agents. I4: correction-function response to a perturbation direction.

The three interventional quantities are semantically different. "The agent generates do-data in its own adaptive loop" (I1) and "an observer does do-operations on the agent" (I4) are genuinely different operations, even if both are do-operations in Pearl's sense. The spike's framing of I4's "loop-interventional access" conflates these by using the single segment name; the segment `#loop-interventional-access` itself describes the I1 version (agent acting in its own loop). The I4 version is *observer-intervention-on-agent*, which is structurally different.

### 4.3 Is the three-layer chain real?

**Verdict (robust qualitative):** The *pattern* is real — at three distinct layers, interventional data escapes a no-go that observational data alone cannot. This is a genuine structural observation and is the load-bearing content of the chain claim.

The *mechanism* is not uniform — the three escapes use interventions of different semantics (agent-self, observer-on-subagent, observer-on-agent-input). This is a real distinction that should be surfaced, not glossed.

**What the strengthening move should say, honestly:**

> Instance 4 (agent-internal architecture) completes a three-layer pattern in which `#loop-interventional-access`'s core structural content — Level-2 data from interventional action under `#causal-hierarchy-requirement` — supplies the unique broadly-available escape from observational-equivalence no-goes at three distinct layers (causal-sufficiency, composition-coupling-sign, agent-internal-architecture). The three escape mechanisms are semantically distinct (agent-self-intervention / observer-on-sub-agent / observer-on-agent-input) and require `#loop-interventional-access` to be read in three semantically-related but distinct modes; naming this three-mode read is the segment-level work the Instance-4 promotion triggers.

This is stronger than the pattern-match-alone claim ("same segment shows up at three places") and weaker than the unified-mechanism claim ("same escape at three layers"). It is the honest middle position: one load-bearing segment, three modes of deployment, one meta-pattern.

**Candidate segment-level follow-on:** Update `#loop-interventional-access` Discussion with a subsection *"Three modes of deployment across `#identifiability-floor` instances"* naming the three modes. This is one paragraph plus cross-references; it surfaces the structural unification without collapsing the semantic distinction.

*Tier of the three-layer chain verdict:* **Robust qualitative**. The pattern unification is visible from the three spike texts taken together; the semantic distinction between intervention-modes is visible from careful reading of the segment texts. Neither claim requires a derivation beyond what is in the existing material.

---

## 5. Meta-segment capacity: bounded or unbounded?

`#identifiability-floor` currently holds three instances. Candidates 2 and 4 (per §3) would take it to five. Does the meta-pattern dilute at five? Is there a principled termination criterion?

### 5.1 The dilution concern

The concern is real: if every AAD "you need capability $X$ to identify $Y$" argument gets promoted to a floor instance, the meta-segment becomes a catalog rather than a structural organizing principle. The meta-segment's load-bearing content — its Gate 2 "does this add value beyond the sum of instances?" content — depends on the instances sharing more than pattern-match.

### 5.2 A principled termination criterion

The five-element test (§1) is a principled criterion; the question is whether it is *tight enough* to keep catalog drift out.

**Observation:** The five-element test is not perfectly tight. E4 requires ≥ 2 escapes; E5 requires "elevates load-bearing role of existing AAD machinery." Both are reviewer-judgment calls, not mechanical checks. A sufficiently motivated reviewer could promote many candidates to instances by reading E4 / E5 permissively.

**Tighter criterion proposal (robust qualitative recommendation):** *An instance is promotable only if it elevates AAD machinery to a **new** load-bearing role — one not already surfaced by another instance.* Under this tighter criterion:

- I1 elevates `#loop-interventional-access` (mode 1: agent-self-intervention).
- I2 elevates observability-as-information-augmentation.
- I3 elevates `#critical-mass-composition`, composite-extended `#loop-interventional-access` (mode 2: observer-on-subagent), and `#composition-scope-condition`.
- Candidate 2 (I4) elevates `#agent-opacity`'s horizon-indexing, `#interaction-channel-classification`'s regime-histogram (to "structurally required"), and extends `#loop-interventional-access` (mode 3: observer-on-agent-input).
- Candidate 4 (I5) elevates `#strategic-composition`'s sub-scope $\alpha'$ potential-game machinery.

Each proposed instance elevates *different* machinery, or a different mode of the same machinery (the three `#loop-interventional-access` modes). No instance is redundant with another at the elevation-target layer.

**Under this criterion, the meta-segment has bounded capacity:** growth is limited by the number of distinct load-bearing AAD segments (call this $N_{LB}$, currently on the order of 30–50 depending on how "load-bearing" is counted). In practice, floor-instance growth will be much smaller than $N_{LB}$ because not every load-bearing segment is the unique escape from a specific information-theoretic no-go.

**Projected growth:** 3 current + 2 new (Candidates 2, 4) = 5 within the next promotion cycle. The "adjacent floors" list in the meta-segment Working Notes flags three more open directions (causal-IB, misspecification cost, tier-switching cost) — plausibly 3 additional instances over the long run. Plausible stable endpoint: 6–8 instances. This is bounded, not unbounded.

### 5.3 The "1-anchor-plus-N-theorem" framing, mirrored

`#additive-coordinate-forcing` has a "1-anchor + 3-theorem" characterization. Does `#identifiability-floor` admit an analogous structure?

**Proposal (hypothesis):** Instance 1 (CHT / on-policy L0) is the **anchor** — it invokes the direct-most causal-hierarchy consequence (Level 2 from Level 1 is impossible) and is load-bearing for the general agent-in-loop reading. Instances 2, 3, I4, I5 are **theorem-level** applications at specific layers (mixture-parameter / composition / agent-architecture / multi-agent-design), each invoking a distinct external theorem. Under this reading, the meta-segment has 1 anchor + 4 theorem-level instances after Candidates 2 and 4 land — analogous to `#additive-coordinate-forcing`'s 1-anchor + 3-theorem structure.

*Tier of this proposal:* **Hypothesis.** It is a plausible structural parallel that might clarify the meta-segment's internal organization, but it is not derived — it is a shape-hypothesis about the emerging instance-set. Could be explicitly evaluated at Candidate 2 / Candidate 4 promotion time.

### 5.4 Termination criterion summary

**Answer to the growth question:** The meta-segment capacity is *structurally bounded*, not by a hard cap but by the tighter criterion "each instance elevates distinct load-bearing machinery." Catalog-drift risk is real at permissive readings of E4 / E5; the tighter criterion prevents it. Projected stable endpoint: 6–8 instances.

*Tier:* **Robust qualitative** for the bounded-capacity claim; **Hypothesis** for the specific 6–8 count (depends on which adjacent floors formalize cleanly).

---

## 6. The layer-taxonomy view

One of the triage brief's suggested strengthening moves is the **layer-taxonomy view**. This proves to be the cleanest organizing lens for the whole picture.

### 6.1 Layers covered

| Layer | Instance(s) | External theorem |
|---|---|---|
| L1: Causal-structure (within-DAG) | I1 on-policy L0 insufficiency | CHT (Bareinboim et al. 2022) |
| L2: Mixture-parameter (soft-facilitator) | I2 L1' Cramér-Rao | Cramér-Rao bound (Cramér 1946) |
| L3: Composition (coupling-sign) | I3 Liberzon common-Lyapunov | Common-Lyapunov nonexistence (Liberzon 2003) |
| L4: Agent-internal-architecture | I4 *proposed* (Candidate 2) | CHT at agent-as-SCM / Kalman-Ho canonical form |
| L5: Multi-agent-aggregation | I5 *proposed* (Candidate 4) | Arrow 1951 / G-S 1973-75 / M-S 1983 |

### 6.2 What the layer view shows

- **Candidates 2 and 4 fill distinct new layers** (L4 agent-internal; L5 multi-agent-aggregation). This is the main positive content of the triage.
- **Candidate 1 is a sub-statement of L4** (at the disturbance-statistic projection), not a new layer.
- **Candidate 3 is not a layer at all** — it is a downstream theorem of the (PI)-at-metric-layer commitment that already lives in `#additive-coordinate-forcing`.

### 6.3 Open adjacent layers

- L6 (causal-IB / interventional relevance) — flagged as "adjacent floor, open" in the current meta-segment.
- L7 (misspecification-cost under finite budget) — flagged as "open" in the current meta-segment.
- L8 (tier-switching policy cost) — flagged as "open" in the current meta-segment.

Projected long-run floor: 5 + 3 = 8 instances if all three adjacent floors formalize. Consistent with §5.3's "6–8 stable endpoint" estimate.

*Tier of the layer taxonomy:* **Robust qualitative**. Each row is defensible; the taxonomy as a whole is a reviewer-orientation device, not a theorem. It earns its keep by making the "is candidate X a new instance?" question tractable — it is iff it fills a new layer or adds a new escape at an existing layer.

---

## 7. Recommended promotion plan

### 7.1 Promotion sequence

**Primary (Priority 1): Candidate 2 → Instance 4 (agent-internal architecture).**

- *Why primary:* Passes the five-element test at Instance 1–3 standards; introduces a new layer in the taxonomy (L4); completes the three-layer `#loop-interventional-access` pattern; has the sharpest sub-scope closed form (Kalman-Ho canonical form ambiguity) available.
- *Recommended name:* "Agent-internal architecture within on-policy behavior-class (Kalman-Ho at linear-Gaussian sub-scope)"
- *External theorem:* Dual anchor — Bareinboim et al. 2022 CHT at the agent-as-SCM layer (general) + Kalman 1963 / Ho-Kalman 1966 canonical-form non-uniqueness (linear-Gaussian sub-scope, the tight anchor).
- *Escapes:* Four, as in Candidate 2's spike §8.1.
- *Strengthened consequence:* The three-layer `#loop-interventional-access` chain, with honest three-mode articulation per §4.
- *Promotion effort:* Moderate. Needs the Kalman-Ho closed-form tightening (~1 page) + segment-level text (moderate) + the three-mode articulation at `#loop-interventional-access` (paragraph-scale).

**Primary (Priority 2): Candidate 4 → Instance 5 (multi-agent-aggregation / mechanism-design).**

- *Why primary:* Fills a genuinely distinct layer (L5). The pattern-match is clean under the broad reading of `#identifiability-floor`. The external theorems are canonical; the escapes are canonical.
- *Recommended name:* "Multi-agent-aggregation mechanism-design (Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite)"
- *Honest scope flag:* The external theorem is an *implementability* theorem, not an identifiability theorem. This distinguishes it from I1–I3's information-theoretic character. Either (a) explicitly label the pattern as covering both "implementability" and "identifiability" theorem families, or (b) note the distinction in the instance header and keep the pattern unified under "external impossibility theorem."
- *Escapes:* Bayes-Nash for dominant-strategy; randomized allocations; subsidy injection; domain restriction.
- *Strengthened consequence:* `#strategic-composition`'s sub-scope $\alpha'$ potential-game conditions (already cross-referenced in the segment).
- *Promotion effort:* Moderate — lower than Candidate 2 because the external theorems are one-step citations rather than requiring fresh AAD-level anchor constructions.

**Sub-instance cross-reference: Candidate 1.**

- *Disposition:* Do **not** promote as a standalone Instance 6. Promote as a *named sub-statement of Instance 4 at the disturbance-statistic projection*. Cross-reference from the proposed `#rho-decomposition` / `#internal-external-decomposition` appendix to Instance 4.
- *Why:* Subsumption §3.1; the no-go content is a projection of Instance 4 onto disturbance statistics. Promoting as standalone would dilute the layer taxonomy by double-counting.
- *Tag location:* In the ρ-decomposition appendix when it promotes, add a Discussion subsection "Connection to `#identifiability-floor` Instance 4" noting the projection relationship.
- *Alternative disposition if Instance 4 slips:* If Candidate 2 does not promote in the next cycle, Candidate 1 could promote on its own merits at a weaker standard — the five-element test clears it at robust-qualitative tier, just below the Instance 1–3 bar. But this is a fallback, not the recommended move.

**Redirect (not a `#identifiability-floor` promotion): Candidate 3.**

- *Disposition:* Promote in `#bias-bound-derivation` (proposed appendix from the bias-bound spike) as a derived theorem under Track 2 (Fisher-Rao, small-$I$). The "no-go for universal $C$ under Euclidean-parameter norm" becomes a **motivating subsection** of `#bias-bound-derivation` — justifying the (PI) scope gate on the bound — not a floor-instance.
- *Cross-reference to `#identifiability-floor`:* None required at promotion time. If a reviewer later notices the pattern-shape and asks about it, a brief Discussion note in `#bias-bound-derivation` observing "shares the shape of `#identifiability-floor` but with a single escape rather than multiple; see `#additive-coordinate-forcing` Instance 4 for the structural home" would preempt the ambiguity.

### 7.2 Naming plan

**For the meta-segment after promotion:**

| Number | Layer | Name | Status |
|---|---|---|---|
| I1 | L1 causal-structure | On-policy L0 insufficiency detection (CHT) | Existing |
| I2 | L2 mixture-parameter | L1' mixture identifiability from single-channel observations (Cramér-Rao) | Existing |
| I3 | L3 composition | Composite contraction certification from component data (Liberzon common-Lyapunov) | Existing |
| I4 | L4 agent-internal | Agent-internal architecture within on-policy behavior-class (CHT / Kalman-Ho) | **Proposed (Candidate 2)** |
| I5 | L5 multi-agent-aggregation | Mechanism-design implementability (Arrow / G-S / M-S) | **Proposed (Candidate 4)** |

Meta-segment remains at 3 → grows to 5 after both promotions. "Adjacent floors" (causal-IB, misspecification, tier-switching) remain as open directions; stable endpoint 6–8.

### 7.3 Ancillary segment-level moves

Along with the meta-segment update, the following segments touch:

- `#loop-interventional-access` — Discussion updated with "three modes of deployment" subsection (agent-self / observer-on-subagent / observer-on-agent-input). Paragraph plus cross-references. Low effort.
- `#agent-opacity` — Discussion updated with the observer-filtration scope note per the neutral-drift spike §10.2. Links to I4.
- `#sector-persistence-template` — Discussion gets the fluctuation-structure scope note per the neutral-drift spike §10.3. Links to I4.
- `#critical-mass-composition` — Optional addendum on $\gamma$-estimation from cross-covariance per neutral-drift spike §10.4. Operationalizes I3 escape (b).
- `#strategic-composition` — already cross-references mechanism-design as candidate floor instance; update to "Instance 5" reference after Candidate 4 promotion. Low-effort text-swap.
- `#bias-bound-derivation` (new appendix) — houses the Candidate 3 content; includes the no-go-under-non-(PI)-norm as motivation, Tracks 1 & 2 as theorems.

### 7.4 Ordering rationale

The recommended order is **Candidate 2 first** (higher load-bearing consequence via the three-layer chain; moderate effort; directly closes a pattern gap), then **Candidate 4** (easier promotion; lower strengthening work to existing machinery, but fills a genuinely new layer). Candidate 1 (sub-statement) lands *with* its home appendix (`#rho-decomposition`) rather than on its own schedule. Candidate 3 lands *with* its home appendix (`#bias-bound-derivation`) rather than in the meta-segment at all.

**Project-rule compliance.** The order is by theoretical consequence, not by effort — per CLAUDE.md's "effort / time / risk-of-getting-stuck are false constraints" rule.

---

## 8. What this spike did and did not do

### 8.1 Did

- Extracted a five-element test from Instances 1–3 of `#identifiability-floor` with element-level criteria. (§1)
- Applied the test to each of the four candidates, with tier labels. (§2)
- Identified three structural subsumptions: Candidate 1 → Candidate 2 projection; Candidate 3 → `#additive-coordinate-forcing` / `#bias-bound-derivation`; Candidates 2, 4 at distinct new layers. (§3)
- Evaluated the three-layer `#loop-interventional-access` chain claim with honest disambiguation of shared-pattern vs. shared-mechanism. (§4)
- Answered the bounded-capacity question with a principled tighter criterion. (§5)
- Organized the picture under a layer taxonomy that makes the recommendation visible. (§6)
- Produced a concrete promotion plan with naming, ordering, effort sketches, and ancillary segment-level moves. (§7)

### 8.2 Did not

- **Write the Kalman-Ho closed-form no-go construction for Instance 4.** The spike-level evidence in Candidate 2's spike §8.3 is clear that the construction is classical (two Kalman filters with identical innovation-sequence spectra but different state-space realizations). Tightening this to I1 / I3 crispness is ~1 page of algebra and belongs in the Instance 4 segment-promotion spike, not this triage.
- **Write the exact derivation-chain of Candidate 1 from Candidate 2's no-go under a specific projection operator.** Flagged in §3.1 as a real uncertainty; the subsumption claim is robust-qualitative, not exact.
- **Resolve the narrow-vs-broad reading of `#identifiability-floor`'s scope** (information-theoretic only vs. general impossibility-theorem). Recommended broad reading in §2.4 and §6.1, but this is a formulation decision; both positions are coherent. A follow-up framing-pass could revisit.
- **Evaluate the "adjacent floors" (causal-IB, misspecification, tier-switching) against the five-element test.** Out of scope for this triage; flagged for later.
- **Touch any segment file.** Per ground rules.

### 8.3 Open items / carry-forwards

1. **Kalman-Ho closed form for I4.** Candidate 2 promotion dependency. Sub-spike.
2. **Projection-derivation for Candidate 1 under Candidate 2.** Soft dependency (nice-to-have for a cleaner story; not gating).
3. **Narrow-vs-broad formulation decision.** Recommended resolution = broad with honest theorem-family labeling, but this can be revisited at Candidate 4 promotion time.
4. **Third `#loop-interventional-access` mode articulation.** Light-touch work at Candidate 2 promotion.
5. **Termination-criterion hypothesis (1-anchor + N-theorem for `#identifiability-floor`).** Optional structural refinement; could be noted in the meta-segment Epistemic Status at Candidate 2 / Candidate 4 promotion or deferred.

---

## 9. One-paragraph summary

The four candidate `#identifiability-floor` instances resolve cleanly under the five-element test (setting / external theorem / no-go / boundary / strengthened-consequence) combined with a layer-taxonomy view. **Two promote as genuine new primary instances**: Candidate 2 (agent-internal architecture within on-policy behavior-class, dual-anchored by CHT-at-agent-as-SCM and Kalman-Ho canonical-form non-uniqueness; fills the L4 layer; completes a three-layer `#loop-interventional-access` pattern with honest three-mode articulation) and Candidate 4 (multi-agent-aggregation mechanism-design via Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite; fills the L5 layer under the broad reading of the meta-pattern, which accommodates both information-theoretic and implementability external theorems). **One sub-statement cross-references** rather than promotes standalone: Candidate 1 (rate-multiplicative factorization no-go) is a projection of Candidate 2 at the disturbance-statistic layer and belongs in the proposed `#rho-decomposition` appendix with a cross-reference to Instance 4 — not as a standalone sixth instance. **One redirects to a different meta-segment**: Candidate 3 (universal-$C$-under-non-(PI)-norm) is a downstream theorem of `#additive-coordinate-forcing`'s fourth primary instance (Čencov / Fisher-Rao), not a `#identifiability-floor` instance — it fails E4 (single escape) and its "strengthening" is re-use rather than elevation of existing machinery. The meta-segment grows from 3 instances to 5 with principled structural reasons for each, bounded by a tighter-than-E5 criterion ("each instance elevates distinct load-bearing machinery or a new mode of existing machinery") with a plausible stable endpoint of 6–8 instances once the three named adjacent floors (causal-IB, misspecification-cost, tier-switching-cost) formalize. Recommended promotion order: Candidate 2 first (higher theoretical consequence; completes the three-layer chain), Candidate 4 second (easier; fills a clean new layer), Candidate 1 with its home appendix (`#rho-decomposition`) as sub-statement cross-reference, Candidate 3 with its home appendix (`#bias-bound-derivation`) as downstream theorem. All tier labels throughout this triage: the five-element test is discussion-grade; individual candidate verdicts are robust-qualitative; the subsumption relationships are robust-qualitative; the three-layer chain disambiguation is robust-qualitative; the bounded-capacity claim is robust-qualitative with a hypothesis-tier 1-anchor + N-theorem shape parallel to `#additive-coordinate-forcing`. No segment files were modified.
