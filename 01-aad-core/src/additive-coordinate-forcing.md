---
slug: additive-coordinate-forcing
type: discussion
status: discussion-grade
depends:
  - chain-confidence-decay
  - strategy-cost-regret-bound
  - edge-update-natural-parameter
stage: draft
---

# Discussion: Additive-Coordinate Forcing

AAD carries three structurally connected uniqueness results in which products of independent factors are made to decompose additively by passing to a logarithmic coordinate. The pattern is not designed-in: it arises because AAD independently needs to decompose compound structures at three distinct layers (chain / divergence / update) and the same Cauchy-functional-equation argument resolves each. This segment names the pattern as an organizing principle, catalogs the three instances precisely, and documents two adjacent cases that share the *shape* but not the AAD-internal *forcing* structure.

## The pattern

Each instance of additive-coordinate forcing in AAD has the same three-step shape:

1. **An additivity commitment is posited or observed.** At the chain layer, the commitment is the probability chain rule — a mathematical identity, not an AAD choice. At the divergence and update layers, the commitment is an AAD-internally-motivated axiom asserting that mismatch (resp. belief) should decompose additively along a structural factorization.

2. **A Cauchy functional equation is imposed on the coordinate.** The commitment fixes the *shape* of the decomposition (addition); the coordinate on which that addition lives is unknown. Requiring the decomposition to hold for all admissible factorizations forces a functional equation of the Cauchy type on the coordinate map.

3. **The coordinate is forced logarithmic.** Under smoothness or monotonicity, Cauchy's functional equation (Aczél 1966, *Lectures on Functional Equations and Their Applications*, §2.1) admits only the solution class $\psi(x) = c \log x + d$, up to positive affine transformation. Products of independent factors become sums on the log-scale coordinate.

The three layers reuse this machinery at different quantities. What they share is *structural*: the forcing argument, the Cauchy-FE machinery, the logarithmic conclusion. What distinguishes them is *semantic*: what compound object is decomposed, what the additivity axiom asserts about independence at that level, and how the forcing interacts with the rest of AAD's apparatus at that layer.

## The three instances

| Layer | What decomposes | Additivity commitment | Forced coordinate | Source segment |
|---|---|---|---|---|
| **Chain** | Confidence along a causal sub-plan chain | Probability chain rule: $P(E_1, \ldots, E_n) = \prod_i P(E_i \mid E_{\lt i})$ — *mathematical identity, not an AAD axiom* | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ — log-probability | #chain-confidence-decay |
| **Divergence** | Policy mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ over DAG-factorized action sequences | Chain-rule additivity over conditional factorizations: $D(P_{XY}\Vert Q_{XY}) = D(P_X\Vert Q_X) + \mathbb{E}_{P_X}[D(P_{Y\mid X}\Vert Q_{Y\mid X})]$ — AAD-internally motivated as divergence-level analog of the chain layer | $f(t) = c\cdot t\log t$ — reverse-KL up to positive scaling (Hobson 1969; Csiszár 1991; Shore-Johnson 1980; functional-equation derivation per Aczél & Daróczy 1975) | #strategy-cost-regret-bound §6.1 |
| **Update** | Credence evolution under independent Bernoulli evidence | Evidential additivity: $\psi(p_\text{post}) = \psi(p_\text{prior}) + g(y)$ for smooth, strictly monotone $\psi$ — AAD-internally motivated as update-level analog of the chain layer | $\psi(p) = c\log(p/(1-p)) + d$ — log-odds up to positive affine (Aczél 1966 §2.1) | #edge-update-natural-parameter |

**The three axioms explicitly invoke each other.** The divergence axiom (`#strategy-cost-regret-bound` §6.1) is stated as "the *divergence-level analog* of the additive log-confidence decay in `#chain-confidence-decay`." The update axiom (`#edge-update-natural-parameter`) is stated as "the *update-level analog* of `#chain-confidence-decay`'s chain-level additive log-confidence decomposition and `#strategy-cost-regret-bound` §6.1's divergence-level chain-rule additivity." The three layers are not independent applications of a generic mathematical idiom; they are interlocked within AAD by cross-cites, each positioning itself against the chain layer as the motivating anchor.

**The chain layer is an anchor, not a theorem.** `#chain-confidence-decay` is `status: exact` because the decomposition is a mathematical identity once the log is applied. The divergence and update layers are `status: conditional` (resp. `robust-qualitative`) because each rests on an additivity axiom that is AAD-internally motivated but not itself derived. The three layers together form a **1-anchor + 2-theorem pattern**, not three parallel theorems. This distinction matters for future reviewers: promoting a fourth layer to an instance of the pattern requires showing either (a) its additivity is a mathematical identity (anchor-style) or (b) an AAD-internal axiom motivates the additivity at that layer (theorem-style with Cauchy-FE derivation).

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

Three primary instances (chain / divergence / update) form the core of the additive-coordinate-forcing pattern: each is backed by an AAD-internal axiom (or identity) that forces a logarithmic coordinate via Cauchy's functional equation. Two adjacent cases (Lyapunov quadratic, IB Lagrangian) share the additive-decomposition shape without the AAD-internal forcing structure — Lyapunov because the coordinate is chosen and matched rather than forced, IB because the axiomatic derivation is imported from information-theoretic foundations rather than re-motivated internally. Future structural moves should be audited against both the primary and adjacent positions, rather than treated as generic instances.

## Complementarity with #identifiability-floor and #separability-pattern

The three meta-segments form AAD's scope-and-structure meta-architecture:

- **#additive-coordinate-forcing** (this) — the *constructive* half: when AAD forces a coordinate, it forces the logarithmic one via Cauchy-FE on an additivity axiom. Names what the theory *does* at its deepest structural moves.
- **#separability-pattern** — the *positive scope* half: for each ladder of increasing difficulty, name the separable core, the structured repair, and the general open. Names what the theory *covers* across its instantiations.
- **#identifiability-floor** — the *negative scope* half: for each known structural no-go, name the external information-theoretic theorem that enforces it and the unique escape available. Names what the theory *cannot do* without explicit information augmentation.

Each meta-segment captures a different cross-sectional view of AAD's architecture:

| Meta-segment | Cross-section | Presentation flavor |
|---|---|---|
| #additive-coordinate-forcing | AAD's forcing moves across coordinates | "When a coordinate is forced, it is logarithmic." |
| #separability-pattern | AAD's scope across ladders of difficulty | "Separable core, structured repair, general open." |
| #identifiability-floor | AAD's structural no-gos | "No-go from external theorem; unique escape from AAD machinery." |

The three compose. A ladder's separable core typically admits an additive-coordinate-forcing move that makes the clean identification clean; a ladder's general-open case typically sits at an identifiability floor that names the information-theoretic obstruction. Reading any segment through all three meta-lenses is a reviewer move that surfaces what makes the segment load-bearing.

## Epistemic Status

*Discussion-grade* at the meta-pattern level. This segment is a presentational organizing principle: it names a structural shape that AAD already runs across three segments and excludes two adjacent cases where the shape is imported rather than internally forced. The meta-pattern itself is not derived and carries no theorem of its own; it is an observation about what the theory does.

The individual instances retain their own epistemic statuses:

- `#chain-confidence-decay` — *exact* (mathematical identity via probability chain rule + logarithm)
- `#strategy-cost-regret-bound` §6.1 — *derived (conditional on chain-rule additivity axiom)* — axiom AAD-internally motivated as divergence-level analog of the chain layer
- `#edge-update-natural-parameter` — *derived (conditional on evidential-additivity axiom)* — axiom AAD-internally motivated as update-level analog of the chain layer

Max attainable: *discussion-grade* for the meta-pattern (it is an organizing principle, not a derivation). Individual instances are at their own tiers as above. The 1-anchor-2-theorem characterization could be strengthened to a necessity argument of the form "any AAD layer where independent factors compose to a quantity that must decompose additively under an AAD-internal axiom must force a logarithmic coordinate via Cauchy-FE." This would promote the meta-pattern to *robust qualitative* at the cost of stating a precondition that is already specific to Cauchy-FE territory — not clearly worth the promotion cost, and deferred as a Working Note.

## Discussion

**Why the 1-anchor-2-theorem characterization matters.** A sloppier reading of the pattern would promote all three layers to "uniqueness theorems forcing logarithmic coordinates." This reading blurs the distinction between the chain layer (where the decomposition is a mathematical identity under the standard chain rule of probability) and the divergence / update layers (where the decomposition is a theorem conditional on an AAD-internal additivity axiom). The distinction matters because the strength of the pattern depends on the *motivation* of the two theorem-level axioms, and their motivation is precisely that they are analogs of the chain-layer identity. Collapsing the three layers to "three parallel theorems" severs the motivational structure that gives the two theorems their AAD-internal force.

**Why the pattern is distinctive to AAD.** Cauchy's functional equation is classical. Its application to derive logarithmic coordinates is also classical (Aczél 1966 is the canonical reference). What is distinctive about AAD's use of the machinery is *where it lands*: three specific layers of the agent's architecture — causal chain confidence, policy-divergence mismatch, and edge-credence update — each requiring an additive decomposition that the surrounding apparatus (DAG factorization, regret bound, Bayesian coherence) already depends on. The motivational chain from `#chain-confidence-decay` outward is not a generic application of functional equations; it is a specific pattern of architectural forcing where each layer's axiom is independently grounded in adjacent AAD commitments.

**Using the pattern as a diagnostic.** When a new structural move in AAD introduces a quantity that must decompose under some factorization, reviewers should audit: (a) is the decomposition multiplicative across independent factors? (b) is there an AAD-internal commitment that the decomposition should be additive? If yes to both, the coordinate is probably logarithmic and the Cauchy-FE machinery applies. If (a) holds but (b) does not, the move is likely an adjacent family member (coordinate chosen, not forced) rather than a primary instance. This diagnostic is the main way the meta-segment earns its keep.

**Relationship to `#chain-confidence-decay`'s role in AAD.** The chain-layer identity is normally cited as a Section II structural-pressure result: long plans are fragile because log-confidence accumulates negative terms. Its anchor role for the two theorem-layer uniqueness results is a separate job, exposed only by the meta-pattern. Future work that touches `#chain-confidence-decay` should be reviewed against both roles: a change that makes the Section II structural-pressure reading cleaner but severs the anchor role would weaken the foundation of the divergence- and update-layer theorems.

**What the pattern does not do.** It does not justify adding arbitrary additivity axioms across AAD to "unlock" more logarithmic coordinates. Each axiom must be independently motivated by adjacent AAD commitments, the way chain / divergence / update each are. The pattern catalogs what is; it does not license manufacture of further instances.

## Working Notes

- **Candidate future layers.** Three plausible additional places where additive decomposition on a forced coordinate might be derivable: (a) credit assignment along temporal chains, where accumulated blame distributes additively — candidate axiom: path-independence of accumulated blame; (b) composition-closure defect across nested levels, where macro-level error accumulates from micro-level errors — candidate axiom: level-additivity under coarse-graining projection; (c) shared-intent compression across agent boundaries, where communication cost aggregates additively across pairwise channels — candidate axiom: channel-independence of coordination-bit costs. Each candidate would need (i) an AAD-internally-motivated axiom parallel to the existing three, and (ii) a Cauchy-FE derivation forcing the logarithmic coordinate. Speculative; not pursued here.

- **Necessity argument for the meta-pattern.** Is there a scope-and-structure theorem of the form "any AAD layer where independent factors compose to a quantity required to decompose additively under an AAD-internal axiom must force a logarithmic coordinate via Cauchy's functional equation"? The content would be: Cauchy-FE uniqueness as a corollary of the axioms rather than an added derivation technique. Speculative; not pursued.

- **IB adjacency and the Shore-Johnson connection.** The IB Lagrangian's additivity is axiomatizable via Shore-Johnson 1980's system-independence axiom, which is itself a Cauchy-FE-type additivity axiom. An alternative framing would count IB as a *fourth primary instance* with the Shore-Johnson axiom as its AAD-internal motivation. This framing is defensible if AAD commits to Shore-Johnson as an AAD-internal axiom (analogous to how the chain layer grounds the divergence and update axioms). Currently `#information-bottleneck` adopts IB from Tishby-Pereira-Bialek 1999 without re-motivating the axiom; the adjacency classification reflects that adoption posture. If a future framing pass promotes Shore-Johnson to an explicit AAD axiom, IB would move from adjacent family member to fourth primary instance.

- **Lyapunov and the Fisher-information extension.** Under a Fisher-information metric generalization (G-BP3 in the architectural portfolio), the Lyapunov coordinate could become forced by the information-geometric structure rather than chosen. Whether that would move Lyapunov to a primary instance depends on whether the Fisher-Lyapunov coordinate is forced by an AAD-internally-motivated additivity axiom parallel to chain / divergence / update, or whether it inherits its coordinate from the Fisher metric (which is itself forced by Čencov's invariance theorem — a different structural family). The question is a sub-question of the G-BP3 scoping spike, not something to resolve here.

- **SP-1 proposals-doc entry is truncated.** The entry in `msc/architectural-proposals-2026-04-22.md` §SP-1 was silently truncated mid-table (only the Chain row is partially present; Divergence and Update rows are missing or corrupted). The canonical statement of the pattern is now this segment; the proposals-doc entry should be reduced to a brief pointer.
