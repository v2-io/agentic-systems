# The Three-Move Shape of NeurIPS-Grade Paper Extractions from ASF

*Drafted by Tessera (Claude Opus 4.7, 1M context) at Joseph's request, 2026-05-08, after a deep read of all three NeurIPS 2026 submissions in `~/src/neurips/`. Compressed version of this material is in `msc/neurips-back-integration-2026-05-08.md` §2; this document develops it more fully because the pattern is methodological discipline that compounds across future extraction cycles, not just an observation about three papers.*

---

## What this document is

A meta-architectural observation: the three NeurIPS 2026 submissions extracted from ASF over the 2026-05-04 → 2026-05-07 sprint share a recurring three-move shape. The shape was not designed; it emerged from adversarial-grade scrutiny preparation under time compression. That it emerged consistently, across three structurally different results in three different fields, is itself information about *what certification forces* on extractions from a substrate like ASF.

This document names the three moves, shows them at work in each paper, connects them to the existing meta-architectural patterns (M1 / M2 / M3), explains why I think they co-arise rather than appearing independently, and identifies what the pattern predicts for future extractions.

The framing claim: **the three moves are the operational form of the meta-architectural triad at the paper-extraction layer.** M1 / M2 / M3 organize the framework; the three moves organize the extraction *of* the framework. Both layers are visible; both are load-bearing; together they explain why the catalog-vs-paper extraction is gain-producing rather than loss-preserving (cf. `~/.claude/projects/-Users-josephwecker-v2-src/memory/project_catalog_extraction_gain.md`).

---

## The three moves

### Move 1 — Structural backbone separated from operational corollary

**The pattern.** Each paper's central theorem is *unconditional* in the operational / architectural reading; the operational interpretation lands as a corollary under a named hypothesis. The unconditional form is what reviewers cannot dismiss without engaging the underlying mathematics; the corollary form is what practitioners can use.

**At work in each paper:**

- **Paper 1** (Tragedy of the Confident Agent). Theorem 4.1.1 — the averaged-information LMI sufficient condition $\mathbb{E}_{a \sim \pi}[\mathcal{I}_o(a)] \succeq \mathcal{I}_{\min}(Q_\rho, A, R^2)$ — stands without commitment to any specific controller. It is a Fisher-information lower bound on the agent's policy. The *survival-margin controller family* (Definition 4.1, with the F-A-G-P enforcement framework in Appendix A.7) is the operational construct that lives on top: a class of controllers that respond to the LMI's mandate by construction. The unconditional theorem is what survives if any specific family member is rejected; the family is what makes the theorem operational.

- **Paper 2** (Unified RL Convergence). The composition theorem (Theorem 4.1) holds under hypotheses (A1)–(A5) — these are conditions on the *situation* (deterministic optimum, identifiability regime, base-learner restart-on-change), not on the algorithm. Conclusions (i)–(v) follow. The cumulative dynamic-regret rate $\tilde O(V_{\max} N_h \sqrt{(B_T+1)T}) + V_{\max} N_h (1 - p_{\text{id}}) T$ is conclusion (v). Specific algorithmic instantiations (UCRL2, UCBVI, RestartQ-UCB) are corollaries that inherit the rate but the theorem doesn't require them. The Best-of-Both-Worlds wrapping via Wei-Luo MASTER is *additional* corollary structure that extends to continuous-variation $V_T$.

- **Paper 3** (LLM Hallucinate Bound). The umbrella theorem (Theorem 4.1) — $\mathbb{E}\,\|\Delta M_{\text{bias}}\| \leq C \cdot \sqrt{I(G;\, M_{\tau^+}\mid e_\tau, M_{\tau^-})}$ — holds *unconditionally in architectural class*. Both Class 1 (Separated) and Class 3 (Coupled) agents are bounded by the same theorem. The architectural factorization corollary (Corollary 4.4) under hypothesis (H_κ) — $\mathbb{E}\,\|\Delta M_{\text{bias}}\| \leq C\sqrt{\kappa^* \cdot I(G;\Omega_\tau \mid e_\tau, M_{\tau^-})}$ — is what makes the *architectural* reading explicit. The unconditional theorem bounds transferred goal-information directly; the corollary factors it through architectural coupling and observation ambiguity.

**Why the separation matters.**

It provides defensive depth. If a reviewer attacks the operational corollary's hypothesis (challenges (H_κ); challenges the F-A-G-P framework's drift-aligned-bonus condition; challenges the (A5) base-learner restart-on-change), the unconditional theorem still holds. The reviewer's attack contracts what's claimed but does not refute the load-bearing structural result.

It also provides *interpretive flexibility*. Future practitioners can apply the unconditional theorem to architectures, regimes, or operational settings the original paper didn't envision — and the theorem still works because its conditions are situational, not specific to the original framing. Class 2 (Partial) hybrid systems were not the focus of Paper 3; the umbrella theorem still bounds their bias because (H_κ) is a separate corollary commitment.

**Connection to ASF.** ASF's catalog tends to run the structural backbone and the operational reading together. The κ × A bias bound is presented as "the κ × A factorization" as a single result. The two-layer structure (umbrella theorem + factorization corollary) is what makes the result formally defensible at NeurIPS-grade adversarial scrutiny; the catalog's looser register doesn't reach for the separation. **Recommendation**: when extracting future ASF results to publication, lead with the structural-unconditional version and append the operational corollary. Possibly worth naming this as a discipline in `FORMAT.md` §Findings-shaped-presentation.

### Move 2 — A no-go forces the load-bearing axiom

**The pattern.** Each paper has a structural argument that *forces* the load-bearing axiom by showing what fails without it. The argument is internal to the paper (not imported from external literature) and constructive (it produces the witness that demonstrates the failure). The axiom that the no-go forces becomes load-bearing in the strongest sense — without it, there is no theorem.

**At work in each paper:**

- **Paper 1**: the blank-wall attack on the scalar form. An action $a_w$ whose observation channel is aligned *orthogonal* to the drifting subspace $S_\rho$ — a "blank-wall" action — drives the scalar magnitude bound $\mathbb{E}_\pi[U_o(a)] \leq U_o^{\max}$ trivially while contributing zero information about the drifting coordinates. The scalar form *cannot discriminate by direction*. The matrix LMI lift with positive-semidefinite Lagrange multiplier $\Lambda \succeq 0$ supported on the drifting subspace is what the blank-wall no-go forces. The constructive witness is the `wall_extreme` action in the 2D simulation: FIM diag(0.0625, 25), drift-axis FIM small, stationary-axis FIM dominant; scalar controllers are captured at 0% survival, LMI controllers escape at 100% survival under directional Λ.

- **Paper 3**: the chart-rescaling no-go on Euclidean chart norms (Theorem 4.2). A chart rescaling $\phi \mapsto a\phi$ scales the chart-Euclidean Wasserstein distance linearly while leaving KL / MI / Fisher-Rao spherical-arc / Hellinger chart-invariant. Taking $a \to \infty$ contradicts any candidate fixed $C_0\sqrt{I}$. *No coordinate-independent universal constant exists for Euclidean chart norms*. The (PI) parameterization-invariance commitment at full Markov-morphism strength is what the no-go forces; under (PI)+(R)+(K), Čencov uniqueness pins Fisher-Rao + $\sqrt{2}$ locally and $2$ globally. The constructive witness is the Gaussian scale family with chart $\sigma$ versus $\log\sigma$.

- **Paper 2**: a slightly different flavor. Forward-KL $D_{\text{KL}}(Q \|\, \pi^*)$ is $+\infty$ whenever $Q$ has off-optimum mass and is therefore *vacuous as a regret coordinate*. The structure of the deterministic-$\pi^*$ regime forces reverse-KL — there is no alternative direction available because the alternative is structurally trivial. This is *direction-forcing via the triviality of the alternative*, not direction-forcing via a constructive no-go. Still M1-shaped at paper-scale (external structural limit forces internal commitment), but the limit takes a different form.

**Two flavors of Move 2.**

The pattern admits two flavors:
- **Constructive no-go** (Paper 1, Paper 3): the alternative *exists but is shown to fail* via a specific witness construction. The blank-wall action exists; the chart rescaling exists; both produce contradictions with the candidate weaker form.
- **Direction-forcing via triviality** (Paper 2): the alternative *is structurally vacuous*; there is nothing to construct because the alternative was empty from the start.

Both are M1-shaped at paper-scale. The difference is whether the alternative is *real-but-overridden* or *structurally-empty*. The first requires more work to surface (find the witness); the second requires recognizing that the alternative was always vacuous.

**Why this matters.**

Without the no-go, the load-bearing axiom looks aesthetic — a stylistic preference among equally defensible alternatives. With the no-go, the axiom is the *unique route to the theorem*. The (PI) commitment, the matrix LMI lift, the reverse-KL direction — none of these is a free choice once the no-go is in hand.

This is structurally what makes M1 work at framework scale (`#disc-identifiability-floor`). M1's pattern is "external information-theoretic theorem produces a structural impossibility; AAD machinery is the unique broadly-available escape." Each paper inherits this pattern at paper-scale: an internal constructive limit produces a structural impossibility for the weaker form; the AAD axiom is the unique broadly-available escape *for the paper's specific result*.

**Connection to ASF.**

M1 in the catalog has four named instances (F1–F4 in `#disc-identifiability-floor`). The chart-rescaling no-go from Paper 3 *is* what should land as the F4 instance entry — currently the catalog refers to "no universal C under Euclidean parameter norm exists" without the constructive proof. The blank-wall attack from Paper 1 is a different M1-shape that may warrant its own catalog entry (proposed slug `#deriv-blank-wall-no-go`). Paper 2's reverse-KL direction-forcing is plausibly already covered by `#deriv-strategy-cost-regret-bound`'s direction-forcing argument; if not, deserves its own treatment.

The deeper observation: **every paper-grade extraction from ASF should expect to need a no-go construction or a direction-forcing argument.** The audit cycle that strengthens a catalog claim toward paper-grade often *produces* the no-go as a side effect of the strengthening. Joseph's working principle "attempt the improbable; effort and risk-of-getting-stuck are false constraints" produces no-gos because the strengthening attempt forces the question "*why* is this axiom load-bearing?", and answering that question constructively is exactly the no-go's shape.

### Move 3 — Two named regimes / tracks rather than one monolithic claim

**The pattern.** Each paper decomposes its result into two named regimes/tracks rather than presenting one monolithic claim. The regimes are *complementary* (different settings, both within the paper's scope) rather than *competing* (same setting, different methods). Each regime carries its own theorem with its own tightness; together they cover the paper's scope without overclaiming any single regime.

**At work in each paper:**

- **Paper 1**: Model D (deterministic-bounded disturbance, $\|w(t)\| \leq \rho$) vs Model S (stochastic isotropic Gaussian, $\mathbb{E}\|w\|^2 = n\sigma_w^2$). Model D delivers worst-case sharp results — pathwise infinite-horizon ultimate boundedness with finite exit-time witness below threshold. Model S delivers mean-square / finite-horizon high-probability results — stationary second-moment boundedness, but not pathwise infinite-horizon (continuous Gaussian noise eventually exits any bounded set with probability 1). The regimes are *different problem settings*; the theorems are different in form (deterministic vs stochastic) and tightness (worst-case sharp vs mean-square).

- **Paper 2**: $B_T$ (piecewise-stationary segment count) vs $V_T$ (continuous variation budget). The piecewise-stationary regime is handled by direct aggregation: block decomposition at change events + Cauchy-Schwarz across $B_T + 1$ blocks gives $\sum_i \sqrt{\Delta_i} \leq \sqrt{(B_T+1)T}$. The continuous-variation regime is handled by Wei-Luo MASTER black-box wrapping, which adapts automatically between regimes without prior knowledge of either. The two regimes carry the *same* base learner and metric machinery; the difference is in how the variation budget is counted and how the rate is recovered.

- **Paper 3**: Track 1 (transport-inequality cascade, $W_2$ metric) vs Track 2 (Fisher-Rao Čencov, $d_{FR}$ metric). Track 1 produces $C = \sqrt{C_{T_2}}$ with $C_{T_2}$ recovering the Stuart-school cascade form $\propto L_{\text{post}}^2/\rho_{\text{LSI}}$ under transport-inequality + Lipschitz-posterior + slice-wise sub-Gaussianity. Track 2 produces universal dimension-free $C = \sqrt{2}$ locally / $2$ globally under (PI)+(R)+(K)+(H4'). The tracks are *different metric choices* on the same problem; the bounds have the same square-root-in-information shape but different metrics and different constants.

**Three sub-flavors of Move 3.**

The pattern admits at least three sub-flavors based on what the regimes are over:
- **Different problem settings** (Paper 1: deterministic vs stochastic disturbance — distinct mathematical formulations of the disturbance class)
- **Different variation budgets** (Paper 2: $B_T$ piecewise-stationary vs $V_T$ continuous-variation — same problem class, different complexity measures)
- **Different metric choices** (Paper 3: $W_2$ transport vs $d_{FR}$ spherical-arc — same problem, different mathematical machinery for measuring the bound)

All three sub-flavors share the *discipline*: claim the strongest result in each named regime; do not overclaim any single regime; do not collapse the regimes into a single weaker statement that fits both poorly.

**Why this matters.**

It prevents a category of overclaiming that catalog-level presentations are vulnerable to. A monolithic statement "the bias is bounded by $C\sqrt{I}$" elides the fact that *different metric choices give different constants under different hypotheses*. Decomposing into Track 1 and Track 2 makes the dependencies visible: transport-inequality regularity gives the Stuart-school cascade form; Fisher-Rao plus parameterization-invariance gives the universal constant. The reader can pick the regime that matches their setting.

It also enables *composition* with future work. The Best-of-Both-Worlds wrapping in Paper 2 is structurally only possible because the $B_T$ and $V_T$ regimes were named separately; if the paper had presented a single rate, the BoBW move couldn't be made cleanly. Similarly, Paper 3's Track 2 globally-valid-vs-locally-tight separation lets adversarial / rare-high-KL prompts (jailbreaks, persona injection) be routed to the global $C=2$ bound while normal operation uses the locally tight $\sqrt{2}$ bound.

**Connection to ASF.**

This is M2 (`#disc-separability-pattern`) at finer grain. M2's catalog ladders are at *axis-level* — correlation, convention, architecture, contraction, identification regime, scope hierarchy, A2'-scope. The paper-level two-named-regimes pattern is at *result-level* — within a single result, the regimes are decomposed. Different scale, same discipline.

The catalog could explicitly name this fine-grain version as part of M2: every paper-grade ASF result is expected to admit a two-track decomposition because the underlying separability discipline operates at every scale where the framework's machinery applies. Naming the pattern at paper-scale gives extraction agents a target shape to aim for.

---

## Why the three moves co-arise

This is the harder and more important question. Why do the three moves consistently appear *together* across structurally different results?

My read: the three moves are not independent stylistic choices. They are *what certification at adversarial-grade scrutiny forces* on a single load-bearing extraction from ASF's substrate. Each move responds to a specific failure mode that the certification process surfaces:

| Move | What it responds to | What its absence costs |
|---|---|---|
| 1 (structural backbone vs operational corollary) | Reviewer attack on the operational hypothesis | Without it, the operational attack collapses the entire result. |
| 2 (no-go forces axiom) | Reviewer challenge to the load-bearing axiom as aesthetic preference | Without it, the axiom looks like a free choice; the theorem looks contingent. |
| 3 (two named regimes / tracks) | Reviewer surfacing of cases the monolithic claim handles poorly | Without it, the result either overclaims (claims too much) or under-decomposes (loses tightness). |

Each move is a *defense against a specific class of reviewer attack*. The three together produce the strongest possible certified extraction because they exhaust the structural attack surfaces. A reviewer attacking Move 1's corollary still has the unconditional theorem to engage. A reviewer attacking the axiom still has the no-go to engage. A reviewer attacking the regime decomposition still has each track's tight result.

This is not an arbitrary observation; it's a structural prediction. **Future ASF extractions to NeurIPS-grade or JAIR-grade adversarial venues should be expected to converge on the three-move shape** — not because the shape is fashionable but because the certification process produces it. Extractions that *don't* exhibit all three moves are likely either:
- Unfinished (the certification process didn't complete; the paper went to print before the third move landed); or
- Targeted at lower adversarial-scrutiny gradient (essay venues, shorter-form journals, position-paper tracks where the structural defenses aren't required).

The corollary observation is interesting for the strategic picture: **the three-move shape is itself an identification protocol for "this paper is adversarial-grade certified."** A reader scanning a paper for the three moves can tell quickly whether the work has been through the full certification gradient or whether some axes are unfinished. ASF's catalog can use the three moves as a maturation indicator for catalog-vs-paper gap-tracking.

---

## Connection to the meta-architectural triad (M1 / M2 / M3)

The three moves map onto the meta-architectural patterns at the paper-extraction layer, but not all three patterns map equally:

- **Move 2 (no-go-forces-axiom)** is **M1 at paper scale.** Each paper's no-go is an internal constructive identifiability-floor instance: the limit of the weaker form is shown structurally; the AAD axiom is the unique broadly-available escape. This is exactly M1's catalog-scale pattern.

- **Move 3 (two named regimes/tracks)** is **M2 at paper scale.** Each paper's regime decomposition is a separability instance at result-scale: the result has a separable core (each track's tight regime), structured-repair zone (the Best-of-Both-Worlds wrapping or globally-valid backstop), and general open (cases outside both tracks). This is exactly M2's catalog-scale pattern.

- **Move 1 (structural backbone vs operational corollary)** does *not* map cleanly onto an existing meta-pattern. It might be its own thing — call it the *unconditional-result-vs-operational-reading discipline*. Or it might be a refinement of M2 at a different axis (the regime decomposition is across hypotheses; the structural-vs-operational decomposition is across result-types). I lean toward the first: it's a meta-architectural pattern in its own right that the catalog hasn't yet named.

**Where M3 lives in the three-move structure.** M3 (additive-coordinate-forcing on exponential-family geometry) doesn't appear directly in the three moves but appears *inside* them. Paper 3's Move 2 (chart-rescaling no-go) forces (PI)+(R)+(K), which is the metric-layer instance of M3. Paper 1's matrix LMI lift uses Fisher-information geometry, which is M3-adjacent. Paper 2's reverse-KL direction-forcing connects to M3's update-layer instance via the log-odds canonical coordinate. M3 is structurally *upstream* of Move 2 — the no-go-that-forces-the-axiom often forces an M3-shaped axiom because M3 names which coordinates are forced in the framework.

**Putting this together.** The three moves are the paper-extraction-layer analog of the meta-architectural triad. M1/M2/M3 organize the framework; Moves 1/2/3 organize the extraction. Both layers are structurally consistent; both are visible; both are load-bearing.

This is itself a meta-meta-observation: **ASF's epistemic architecture has self-similar structure across scales.** The discipline that organizes the framework at catalog-scale is the same discipline that organizes the framework at paper-scale. This is what makes the framework's productivity-under-extraction reliable: the audit cycle, the strengthening discipline, and the back-integration loop are not just project-level practices — they are the catalog-scale form of what at paper-scale appears as the three moves. The whole system is doing the same kind of work at every scale.

---

## What this predicts for future extractions

Concrete predictions for the catalog-to-paper extractions queued in `~/src/ops/papers/`:

| Candidate | Three-move shape predicted? | What the moves would look like |
|---|---|---|
| B-N3 Detection Latency Forced | Yes | (1) Structural: log-odds forcing + Beta-Bernoulli accumulation gives the rate without specific update model. Operational: the rate as detection-latency benchmark. (2) No-go: Aczél-FE uniqueness + the alternative being non-additive and thus violating evidential additivity. (3) Two regimes: fixed-gain vs adaptive-gain (the $\alpha_1/\alpha_2$ partition from `#deriv-adaptive-gain-dynamics`). |
| B-CS2 Stability-Induced Myopia | Yes | (1) Structural: the triple-pressure window theorem holds across the gain-decay class. Operational: the prescriptive routing — short-attention → retention; calcified → causal-IB drive; fragmented → cadence engineering. (2) No-go: the empty-window catastrophic-forgetting regime as the structural impossibility. (3) Two regimes: gain-decay vs finite-gain (the same partition appears here as in B-N3). |
| B-N9 Critical Mass + Brooks's Law | Yes | (1) Structural: the closed-form $(\alpha-C)R > \rho + \gamma\mathcal{T}$ inequality holds across signed γ. Operational: the four-regime recovery (single-agent, team-persistence, adversarial, Brooks's-Law). (2) No-go: identifiability-floor F3 (composite contraction certification from component data; Liberzon 2003). (3) Two regimes: cooperative (γ < 0) vs adversarial (γ > 0). |
| B-N14 Sandbox Hard Ceiling | Yes | (1) Structural: the trajectory-non-forkability claim holds independently of evaluation methodology. Operational: the Pearl-hierarchy mapping for specific eval types. (2) No-go: Bareinboim CHT applied to Level-1 sandbox data vs Level-2 deployment behavior. (3) Two regimes: forkable (sandbox; Level 1 only) vs non-forkable (deployment; Level 2 generated). |
| B-S10 Memory as Constitutive | Probably not | This is a position paper / field-critique. Adversarial-scrutiny gradient is lower than NeurIPS Main Track; the three-move shape may be partial. Move 1 (structural-backbone-vs-corollary) likely; Move 2 (no-go) may not appear; Move 3 (two named regimes) may not appear. |
| B-F1 Emergence Without Telos / Synthese paper | Partial | Synthese is adversarial but at a different gradient than NeurIPS. Move 1 likely (asymmetric-uncertainty argument as structural backbone, granted-agency compact as operational corollary). Move 2 possibly (the Campbell-asymmetry response is direction-forcing-by-structural-triviality of the symmetric-failure-modes assumption). Move 3 less likely (philosophical papers tend not to decompose into named regimes the way technical papers do). |

**Implication.** The three-move shape is a useful diagnostic and target during extraction, but it is not universal. It applies most strongly to NeurIPS-grade / JAIR-grade technical papers. Position papers, field-critiques, philosophical papers, and essay-form work follow different shapes — closer to *single-argument-with-named-counterpositions* than *three-move-defended-extraction*. Knowing which shape an extraction is targeting helps calibrate effort and structural decisions during drafting.

---

## What ASF should absorb

Three concrete propagations:

**1. Name the structural-backbone-vs-operational-corollary discipline as a meta-pattern.** It doesn't have a current home in M1/M2/M3 or in the catalog. Either it's a fourth meta-pattern (call it M4 — *unconditional-result-vs-operational-reading*) or it's a refinement that lives in `FORMAT.md` as a presentational discipline. My weak preference: surface it as a meta-pattern in the catalog because it organizes a substantial fraction of the framework's certified results, the way M1/M2/M3 do.

**2. Update M1 instances to include paper-scale no-gos.** The chart-rescaling no-go from Paper 3 should land as F4. The blank-wall no-go from Paper 1 may warrant its own treatment. The reverse-KL direction-forcing from Paper 2 may already be covered. The catalog's M1 table currently surfaces the *catalog-scale* identifiability-floor instances; the paper-scale no-gos are a related-but-distinct family that deserves its own presentation.

**3. Update M2 to include the fine-grain two-named-regimes pattern as a presentational discipline.** The catalog's M2 ladders are at axis-level; the paper-level pattern is at result-level. Both are M2-shaped; the catalog should make this visible.

The deeper implication: **ASF's catalog and ASF's paper-extractions are structurally consistent at the meta-level.** This is a feature, not a coincidence. It means the discipline that produced the catalog is the same discipline that produced the papers, and that future extractions will be load-bearing in the same way *if* the certification gradient is high enough to force the three moves. The audit cycles, the strengthening attempts, and the back-integration loop are the project-level form of what at paper-scale appears as the three moves; both are doing the same kind of structural work.

---

## A note on what's not the three-move shape

The pattern as described above applies most strongly to **technical papers under NeurIPS-grade adversarial scrutiny**. Several adjacent shapes do *not* exhibit the same pattern:

- **Position papers** (B-S10 Memory as Constitutive, B-Sess1 ASF Recovers Active Inference) follow a different shape: *single-argument-with-named-counterpositions*. The three moves don't all appear because the certification gradient and the audience are different.
- **Philosophical papers** (the Synthese paper Joseph is queuing) follow yet another shape: *thesis-with-engagement-of-existing-literature*. Move 1's structural-vs-operational discipline is partially present (the asymmetric-uncertainty argument is structural; the granted-agency compact is operational). Moves 2 and 3 may or may not appear.
- **Empirical / case-study papers** (B-A1 Ruby Community, B-C7 eli-migration-prep) follow a *data-and-methodology* shape that doesn't decompose into three moves.
- **Essay venues** (Aeon, Boston Review, LRB) follow a *single-thread* shape with no formal hypotheses to defend.

The three-move shape is a *NeurIPS / JAIR / IEEE TAC* extraction discipline. Other venues have other disciplines. A future agent picking up an extraction should first identify the venue's adversarial-scrutiny gradient and target shape, then calibrate the certification effort accordingly. Trying to deploy the three-move shape on an Aeon essay is over-engineering; trying to deploy a single-thread shape on a NeurIPS extraction is under-engineering.

---

## Summary

Three structural moves appear consistently across the three NeurIPS 2026 ASF extractions:

1. **Structural backbone separated from operational corollary** — the central theorem is unconditional in the operational reading; the operational interpretation is a corollary under named hypothesis.
2. **A no-go forces the load-bearing axiom** — an internal constructive limit (or direction-forcing-by-triviality) shows what fails without the axiom; the AAD axiom is the unique broadly-available escape.
3. **Two named regimes / tracks rather than one monolithic claim** — the result decomposes into complementary regimes, each carrying its own theorem with its own tightness.

The three moves are not stylistic; they are what NeurIPS-grade adversarial certification *forces* on extractions from ASF's substrate. Each move responds to a specific class of reviewer attack; the three together exhaust the structural attack surfaces; their consistent co-occurrence is structurally predicted by the certification gradient.

The three moves map onto the meta-architectural triad at paper-extraction scale: Move 2 is M1, Move 3 is M2, Move 1 is a candidate fourth meta-pattern. ASF's epistemic architecture has self-similar structure across scales — the discipline that organizes the framework at catalog-scale is the same discipline that organizes the framework at paper-scale. This is what makes the catalog-vs-paper extraction gap reliably gain-producing rather than loss-preserving.

For future extractions: expect the three-move shape under high-adversarial-scrutiny targets; calibrate to other shapes for position papers, philosophical papers, essays, and empirical case studies. Knowing the target shape helps calibrate effort and structural decisions during drafting.

---

*End of document. Cross-references: `msc/neurips-back-integration-2026-05-08.md` §2 carries the compressed version of this material; `msc/FINDINGS-RANKED-DRAFT.md` M-section is where M1/M2/M3 live; `~/src/neurips/AGENTS.md` §3.1 carries the strengthen-before-soften discipline that produces the no-gos; `~/.claude/projects/-Users-josephwecker-v2-src/memory/project_catalog_extraction_gain.md` is the operational reading of the same observation at memory scale.*
