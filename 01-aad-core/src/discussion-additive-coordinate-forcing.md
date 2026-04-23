---
slug: discussion-additive-coordinate-forcing
type: discussion
status: discussion-grade
depends:
  - chain-confidence-decay
  - strategy-cost-regret-bound
  - edge-update-natural-parameter
stage: draft
---

# Discussion: Additive-Coordinate Forcing

AAD carries a family of structurally connected uniqueness results in which a coordinate is **forced by a uniqueness theorem operating on an AAD-internally-motivated axiom**. Three instances share a specific sub-structure — products of independent factors decompose additively by passing to a logarithmic coordinate, under a Cauchy-functional-equation argument (chain / divergence / update layers). A fourth instance shares the broader discipline but forces a Riemannian Fisher metric rather than a log-additive coordinate, via Čencov's 1982 invariance theorem. The pattern is not designed-in: it arises because AAD independently needs to force coordinates at four distinct layers, and three adjacent uniqueness-theorem machineries (Cauchy-FE on additivity, Čencov-invariance) resolve each.

This segment names the pattern as an organizing principle, catalogs the four instances precisely, and documents two adjacent cases that share the *shape* but not the AAD-internal *forcing* structure.

## The pattern

Each instance of coordinate-forcing in AAD has the same three-step shape:

1. **An AAD-internal axiom (or mathematical identity) is posited.** At the chain layer, the commitment is the probability chain rule — a mathematical identity, not an AAD choice. At the divergence and update layers, the commitment is an AAD-internally-motivated additivity axiom asserting that mismatch (resp. belief) should decompose additively along a structural factorization. At the metric layer, the commitment is the parameterization-invariance axiom (PI) named in `#agent-identity` (AAD's theorems should not depend on arbitrary choice of coordinates on $M_t$).

2. **A uniqueness theorem operates on the axiom.** For the chain, divergence, and update layers, the uniqueness theorem is Cauchy's functional equation. For the metric layer, the uniqueness theorem is Čencov's 1982 result (*Statistical Decision Rules and Optimal Inference*, AMS; subsequent Ay-Jost-Lê-Schwachhöfer 2017 extensions) — under parameterization-invariance, the Fisher information metric is uniquely forced on statistical manifolds.

3. **A coordinate is forced uniquely (up to positive affine / up to scale).** The three Cauchy-FE layers force logarithmic coordinates: under smoothness or monotonicity, Cauchy's functional equation (Aczél 1966, *Lectures on Functional Equations and Their Applications*, §2.1) admits only the solution class $\psi(x) = c \log x + d$. The Čencov layer forces the Fisher metric uniquely up to a global scale factor.

The four layers reuse this structural machinery at different quantities. What they share is the discipline: *uniqueness-theorem-forced coordinate under AAD-internally-motivated axiom*. What distinguishes them is *semantic* (what compound object is decomposed or made invariant) and *mechanical* (Cauchy-FE on additivity for the three log-additive instances; Čencov-invariance on parameterization for the Fisher-metric instance).

## The four instances

### Three Cauchy-FE instances (log-additive coordinates)

| Layer | What decomposes | Additivity commitment | Forced coordinate | Source segment |
|---|---|---|---|---|
| **Chain** | Confidence along a causal sub-plan chain | Probability chain rule: $P(E_1, \ldots, E_n) = \prod_i P(E_i \mid E_{\lt i})$ — *mathematical identity, not an AAD axiom* | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ — log-probability | #chain-confidence-decay |
| **Divergence** | Policy mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ over DAG-factorized action sequences | Chain-rule additivity over conditional factorizations: $D(P_{XY}\Vert Q_{XY}) = D(P_X\Vert Q_X) + \mathbb{E}_{P_X}[D(P_{Y\mid X}\Vert Q_{Y\mid X})]$ — AAD-internally motivated as divergence-level analog of the chain layer | $f(t) = c\cdot t\log t$ — reverse-KL up to positive scaling (Hobson 1969; Csiszár 1991; Shore-Johnson 1980; functional-equation derivation per Aczél & Daróczy 1975) | #strategy-cost-regret-bound §6.1 |
| **Update** | Credence evolution under independent Bernoulli evidence | Evidential additivity: $\psi(p_\text{post}) = \psi(p_\text{prior}) + g(y)$ for smooth, strictly monotone $\psi$ — AAD-internally motivated as update-level analog of the chain layer | $\psi(p) = c\log(p/(1-p)) + d$ — log-odds up to positive affine (Aczél 1966 §2.1) | #edge-update-natural-parameter |

### The Čencov-invariance instance (Fisher-metric coordinate)

| Layer | What is invariant | Invariance commitment | Forced coordinate | Source segment |
|---|---|---|---|---|
| **Metric** | AAD's predictions about a singular trajectory $\mathcal C_t$ | Parameterization-invariance (PI): the theory's conclusions do not depend on arbitrary choice of coordinates on $M_t$ — AAD-internally motivated as natural extension of `#agent-identity`'s singular-trajectory scope commitment (trajectory is coordinate-free; any parameterization of $M_t$'s state space is a modeling convention) | Fisher information metric $\mathbf I(\theta)$ uniquely forced on statistical-manifold sub-cases of $M_t$, up to a global scale (Čencov 1982, *Statistical Decision Rules and Optimal Inference*, AMS; Ay, Jost, Lê & Schwachhöfer 2017, *Information Geometry*, Springer) | #gain-sector-bridge "Fisher-metric cases under parameterization-invariance" |

**The four axioms explicitly invoke adjacent AAD commitments.** The divergence axiom (`#strategy-cost-regret-bound` §6.1) is stated as "the *divergence-level analog* of the additive log-confidence decay in `#chain-confidence-decay`." The update axiom (`#edge-update-natural-parameter`) is stated as "the *update-level analog* of `#chain-confidence-decay`'s chain-level additive log-confidence decomposition and `#strategy-cost-regret-bound` §6.1's divergence-level chain-rule additivity." The (PI) axiom (`#agent-identity` "Natural extension") is stated as "the metric-layer analog motivated by the singular-trajectory scope commitment — the trajectory is coordinate-free; the theory's claims about it should be too." The four layers are not independent applications of a generic mathematical idiom; they are interlocked within AAD by cross-cites, each positioning itself against an adjacent AAD commitment as its motivating anchor (and the first three against the chain-layer identity specifically).

**The chain layer is an anchor, not a theorem.** `#chain-confidence-decay` is `status: exact` because the decomposition is a mathematical identity once the log is applied. The divergence, update, and metric layers are each `status: conditional` (resp. `robust-qualitative`) because each rests on an AAD-internally-motivated axiom that is not itself derived. The four layers together form a **1-anchor + 3-theorem pattern**, not four parallel theorems. This distinction matters for future reviewers: promoting a fifth layer to an instance of the pattern requires showing either (a) the coordinate is forced by a mathematical identity (anchor-style) or (b) an AAD-internal axiom + a uniqueness theorem (Cauchy-FE, Čencov-invariance, or an adjacent machinery) forces the coordinate (theorem-style).

**Two distinct uniqueness machineries under one broader discipline.** The three Cauchy-FE instances share a specific sub-structure: products of independent factors decompose additively by passing to a logarithmic coordinate, under Cauchy's functional equation. The Čencov instance is different: parameterization-invariance forces the Fisher metric via Čencov's 1982 theorem, producing a Riemannian geometric coordinate rather than a log-additive one. Both clear the broader discipline — *uniqueness-theorem-forced coordinate under AAD-internal axiom* — but via distinct uniqueness-theorem machineries. The segment's title ("additive-coordinate-forcing") emphasizes the three Cauchy-FE instances that share log-additivity; the Čencov instance sits within the broader discipline but diverges on the specific sub-structure. A future session could consider renaming the segment to reflect the broader discipline (e.g., `#uniqueness-coordinate-forcing`) — but since three of the four primary instances are additive, the current name remains broadly descriptive. The fact that one instance diverges on mechanism while clearing the same discipline is itself a load-bearing observation about the meta-pattern's shape.

## Adjacent cases that share the shape but not the forcing structure

Two further AAD segments exhibit additive decompositions on a distinguished coordinate, but the coordinate is not *forced* by an AAD-internally-motivated axiom in the same sense. They are documented here so future work does not mistakenly promote them to primary instances.

### Lyapunov quadratic (`#sector-condition-derivation`)

The sector-Lyapunov argument uses $V(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$, under which $\dot V$ decomposes additively into a correction term $\delta^T(-F)$ and a disturbance term $\delta^T w$ along trajectories. The sector condition (A2') $\delta^T F(\delta) \geq \alpha \lVert\delta\rVert^2$ is *matched* to this coordinate.

**Why the quadratic is not forced.** The `#sector-condition-derivation` derivation-audit table labels the quadratic candidate $V = \tfrac{1}{2}\lVert\delta\rVert^2$ a **formulation choice**, not a derived coordinate. A converse-Lyapunov argument (Khalil 2002, *Nonlinear Systems*, Theorem 4.17) guarantees that *some* quadratic-equivalent $V_\ast$ exists when persistence holds — but not that $V_\ast$ equals the Euclidean norm. Under a weighted candidate $V(\delta) = \tfrac{1}{2}\delta^T P \delta$, the natural sector condition becomes $\delta^T P F(\delta) \geq \alpha \delta^T P \delta$, and the matrix-Kalman case lives in the $(P^-)^{-1}$-weighted inner product rather than Euclidean A2'. The sector condition and the quadratic coordinate are *matched* to each other; neither forces the other.

**Contrast with the three primary instances.** At the chain / divergence / update layers, the logarithmic coordinate is *uniquely forced* (up to positive affine) by Cauchy's functional equation under AAD-motivated additivity axioms. At the Lyapunov layer, the quadratic coordinate is *chosen* to match the posited sector form; the axioms (A1)–(A3) do not force the coordinate over alternative quadratic-equivalent candidates. The Lyapunov case therefore belongs to a different structural family — the converse-Lyapunov existence family — not the Cauchy-FE additive-coordinate-forcing family.

### IB Lagrangian (`#information-bottleneck`, `#compression-operations`)

The Information Bottleneck objective $T^\ast = \arg\min [I(X;T) - \beta \cdot I(T;Y)]$ is an additive Lagrangian form that `#compression-operations` applies at four AAD compression instances ($M_t$, $\Sigma_t$, shared intent, $\Lambda$). The additive separation of compression cost and predictive relevance on a log-scale (mutual information is logarithmic by construction) is the shape the primary instances share.

**Why IB is adjacent rather than primary.** `#information-bottleneck` is labeled `type: formulation` / `status: exact, applied external theorem`; the Epistemic Status paragraph explicitly states that the IB form is *adopted* from Tishby, Pereira & Bialek 1999 (with the Lagrangian-dual reading standard per Cover & Thomas §I.12–13). AAD's invocation is *adoption*, not *re-derivation under AAD-internal motivation*. The Shore-Johnson 1980 system-independence axioms that axiomatize the information-theoretic additivity of IB are cited in `#strategy-cost-regret-bound` §6.1 — so there is a legitimate Cauchy-FE derivation available in the background — but AAD does not re-derive the Lagrangian form under an AAD-internally-motivated axiom parallel to the three primary instances' chain / divergence / update motivations.

**The U-medium ceiling.** `#compression-operations` explicitly states that the four-instance unification is at U-medium (shared shape, variational calculus, rate-distortion interpretation), not U-strong (same optimization problem with different bindings). This is structurally consistent with IB being an *adjacent family member* to the additive-coordinate-forcing pattern: the four IB instances share a shape imported from an external theorem, rather than instantiating a uniqueness theorem derived from AAD-internal axioms.

### Net characterization

Four primary instances (chain / divergence / update / metric) form the core of the meta-pattern: each is backed by an AAD-internal axiom (or identity) and forces a coordinate via a uniqueness theorem — Cauchy's functional equation for the three log-additive instances, Čencov's 1982 invariance theorem for the Fisher-metric instance. Two adjacent cases (Lyapunov quadratic, IB Lagrangian) share the pattern's *shape* without the AAD-internal forcing structure — Lyapunov because the coordinate is chosen and matched rather than forced, IB because the axiomatic derivation is imported from information-theoretic foundations rather than re-motivated internally.

The Čencov instance has a specific adjacency relationship to the three Cauchy-FE instances worth noting: the Fisher metric's second-order expansion near a point is the KL divergence, which decomposes additively across independent distributions. So there is a structural hand-off between the Fisher-metric coordinate (forced at the metric layer by Čencov-invariance) and the log-additive coordinate of KL-style divergence (forced at the divergence layer by Cauchy-FE on chain-rule additivity). The two layers force different kinds of coordinates for different purposes, but they are consistent with each other and — in the Kalman / exponential-family cases — measure the same geometric content through different analytic machineries.

Future structural moves should be audited against both the primary and adjacent positions, rather than treated as generic instances.

## Complementarity with #discussion-identifiability-floor and #discussion-separability-pattern

The three meta-segments form AAD's scope-and-structure meta-architecture:

- **#discussion-additive-coordinate-forcing** (this) — the *constructive* half: when AAD forces a coordinate, it forces the logarithmic one via Cauchy-FE on an additivity axiom. Names what the theory *does* at its deepest structural moves.
- **#discussion-separability-pattern** — the *positive scope* half: for each ladder of increasing difficulty, name the separable core, the structured repair, and the general open. Names what the theory *covers* across its instantiations.
- **#discussion-identifiability-floor** — the *negative scope* half: for each known structural no-go, name the external information-theoretic theorem that enforces it and the unique escape available. Names what the theory *cannot do* without explicit information augmentation.

Each meta-segment captures a different cross-sectional view of AAD's architecture:

| Meta-segment | Cross-section | Presentation flavor |
|---|---|---|
| #discussion-additive-coordinate-forcing | AAD's forcing moves across coordinates | "When a coordinate is forced, it is forced by a uniqueness theorem on an AAD-internal axiom — logarithmic via Cauchy-FE at chain/divergence/update layers, Fisher-Riemannian via Čencov-invariance at the metric layer." |
| #discussion-separability-pattern | AAD's scope across ladders of difficulty | "Separable core, structured repair, general open." |
| #discussion-identifiability-floor | AAD's structural no-gos | "No-go from external theorem; unique escape from AAD machinery." |

The three compose. A ladder's separable core typically admits an additive-coordinate-forcing move that makes the clean identification clean; a ladder's general-open case typically sits at an identifiability floor that names the information-theoretic obstruction. Reading any segment through all three meta-lenses is a reviewer move that surfaces what makes the segment load-bearing.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. This segment is a presentational organizing principle: it names a structural shape that AAD already runs across three segments and excludes two adjacent cases where the shape is imported rather than internally forced. The meta-pattern itself is not derived and carries no theorem of its own; it is an observation about what the theory does.

The individual instances retain their own epistemic statuses:

- `#chain-confidence-decay` — *exact* (mathematical identity via probability chain rule + logarithm)
- `#strategy-cost-regret-bound` §6.1 — *derived (conditional on chain-rule additivity axiom)* — axiom AAD-internally motivated as divergence-level analog of the chain layer
- `#edge-update-natural-parameter` — *derived (conditional on evidential-additivity axiom)* — axiom AAD-internally motivated as update-level analog of the chain layer
- `#gain-sector-bridge` "Fisher-metric cases under parameterization-invariance" — *derived (conditional on (PI) parameterization-invariance axiom)* — axiom AAD-internally motivated as metric-layer analog of the trajectory-centered scope commitment in `#agent-identity`

Max attainable: *discussion-grade* for the meta-pattern (it is an organizing principle, not a derivation). Individual instances are at their own tiers as above. The 1-anchor-3-theorem characterization could be strengthened to a necessity argument of the form "any AAD layer where a coordinate must be forced from an AAD-internally-motivated axiom admits a uniqueness-theorem derivation (Cauchy-FE, Čencov-invariance, or an adjacent mechanism)." This would promote the meta-pattern to *robust qualitative* at the cost of stating a precondition that is already specific to uniqueness-theorem territory — not clearly worth the promotion cost, and deferred as a Working Note.

## Discussion

**Why the 1-anchor-3-theorem characterization matters.** A sloppier reading of the pattern would promote all four layers to "uniqueness theorems forcing coordinates." This reading blurs the distinction between the chain layer (where the decomposition is a mathematical identity under the standard chain rule of probability) and the divergence / update / metric layers (where the coordinate is forced by a uniqueness theorem conditional on an AAD-internal axiom). The distinction matters because the strength of the pattern depends on the *motivation* of the three theorem-level axioms: the chain-rule-additivity axiom and the evidential-additivity axiom are each motivated as analogs of the chain-layer identity; the (PI) parameterization-invariance axiom is motivated as an extension of `#agent-identity`'s singular-trajectory scope commitment. Collapsing the four layers to "four parallel theorems" severs the motivational structure that gives the three theorem-level axioms their AAD-internal force.

**The Cauchy-FE / Čencov distinction within the broader discipline.** The three Cauchy-FE instances share a specific sub-structure (additivity axiom + Cauchy's functional equation → log-coordinate forced). The Čencov instance has a different structural type (invariance axiom + Čencov 1982 → Fisher metric forced). Both clear the *broader discipline* — uniqueness theorem on AAD-internal axiom — but via distinct machineries. This is load-bearing for future reviewers: the discipline is not "always Cauchy-FE"; it is "always a uniqueness theorem on an AAD-internal axiom, of which Cauchy-FE is one clean machinery and Čencov-invariance is another." Future structural moves should be audited against the broader discipline, not against the narrower Cauchy-FE-only version. Candidate additional uniqueness-theorem machineries that could plausibly generate fifth-instance candidates include Dempster-Shafer combination theorems under belief-function axiom structures, Bregman-divergence characterizations under dual-flat-affine invariance (Amari-Nagaoka 2000), and Minty-Browder theorems under monotone-operator axiom structures — but none of these has an AAD-internal motivating axiom as cleanly available as Cauchy-FE and (PI) did.

**Why the pattern is distinctive to AAD.** Cauchy's functional equation is classical. Its application to derive logarithmic coordinates is also classical (Aczél 1966 is the canonical reference). What is distinctive about AAD's use of the machinery is *where it lands*: three specific layers of the agent's architecture — causal chain confidence, policy-divergence mismatch, and edge-credence update — each requiring an additive decomposition that the surrounding apparatus (DAG factorization, regret bound, Bayesian coherence) already depends on. The motivational chain from `#chain-confidence-decay` outward is not a generic application of functional equations; it is a specific pattern of architectural forcing where each layer's axiom is independently grounded in adjacent AAD commitments.

**Using the pattern as a diagnostic.** When a new structural move in AAD introduces a quantity that must decompose under some factorization, reviewers should audit: (a) is the decomposition multiplicative across independent factors? (b) is there an AAD-internal commitment that the decomposition should be additive? If yes to both, the coordinate is probably logarithmic and the Cauchy-FE machinery applies. If (a) holds but (b) does not, the move is likely an adjacent family member (coordinate chosen, not forced) rather than a primary instance. This diagnostic is the main way the meta-segment earns its keep.

**Relationship to `#chain-confidence-decay`'s role in AAD.** The chain-layer identity is normally cited as a Section II structural-pressure result: long plans are fragile because log-confidence accumulates negative terms. Its anchor role for the two theorem-layer uniqueness results is a separate job, exposed only by the meta-pattern. Future work that touches `#chain-confidence-decay` should be reviewed against both roles: a change that makes the Section II structural-pressure reading cleaner but severs the anchor role would weaken the foundation of the divergence- and update-layer theorems.

**What the pattern does not do.** It does not justify adding arbitrary additivity axioms across AAD to "unlock" more logarithmic coordinates. Each axiom must be independently motivated by adjacent AAD commitments, the way chain / divergence / update each are. The pattern catalogs what is; it does not license manufacture of further instances.

## Working Notes

- **Candidate future layers.** Three plausible additional places where coordinate-forcing might be derivable: (a) credit assignment along temporal chains, where accumulated blame distributes additively — candidate axiom: path-independence of accumulated blame; (b) composition-closure defect across nested levels, where macro-level error accumulates from micro-level errors — candidate axiom: level-additivity under coarse-graining projection; (c) shared-intent compression across agent boundaries, where communication cost aggregates additively across pairwise channels — candidate axiom: channel-independence of coordination-bit costs. Each candidate would need (i) an AAD-internally-motivated axiom parallel to the existing four, and (ii) either a Cauchy-FE derivation (for log-additive candidates) or a different uniqueness-theorem machinery (for geometric candidates) forcing the coordinate. Speculative; not pursued here. (A prior version of this Working Notes list treated the metric-layer Čencov instance as a candidate; it is now a primary instance in the four-instance table above, promoted after `msc/spike-jacobian-b1-strengthening.md` established the (PI)-as-metric-layer-analog motivation.)

- **Necessity argument for the meta-pattern.** Is there a scope-and-structure theorem of the form "any AAD layer where independent factors compose to a quantity required to decompose additively under an AAD-internal axiom must force a logarithmic coordinate via Cauchy's functional equation"? The content would be: Cauchy-FE uniqueness as a corollary of the axioms rather than an added derivation technique. Speculative; not pursued.

- **IB adjacency and the Shore-Johnson connection.** The IB Lagrangian's additivity is axiomatizable via Shore-Johnson 1980's system-independence axiom, which is itself a Cauchy-FE-type additivity axiom. An alternative framing would count IB as a *fourth primary instance* with the Shore-Johnson axiom as its AAD-internal motivation. This framing is defensible if AAD commits to Shore-Johnson as an AAD-internal axiom (analogous to how the chain layer grounds the divergence and update axioms). Currently `#information-bottleneck` adopts IB from Tishby-Pereira-Bialek 1999 without re-motivating the axiom; the adjacency classification reflects that adoption posture. If a future framing pass promotes Shore-Johnson to an explicit AAD axiom, IB would move from adjacent family member to fourth primary instance.

- **Lyapunov and the Fisher-information extension.** Under a Fisher-information metric generalization (G-BP3 in the architectural portfolio), the Lyapunov coordinate could become forced by the information-geometric structure rather than chosen. Whether that would move Lyapunov to a primary instance depends on whether the Fisher-Lyapunov coordinate is forced by an AAD-internally-motivated additivity axiom parallel to chain / divergence / update, or whether it inherits its coordinate from the Fisher metric (which is itself forced by Čencov's invariance theorem — a different structural family). The question is a sub-question of the G-BP3 scoping spike, not something to resolve here.

- **SP-1 proposals-doc entry is truncated.** The entry in `msc/architectural-proposals-2026-04-22.md` §SP-1 was silently truncated mid-table (only the Chain row is partially present; Divergence and Update rows are missing or corrupted). The canonical statement of the pattern is now this segment; the proposals-doc entry should be reduced to a brief pointer.
