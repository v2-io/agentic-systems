# Spike: Scaling of the Composition Closure Defect with Team Size $N$

**Status**: *Scoping spike.* Not an attempt to resolve the question. The purpose is to frame precisely what "closure defect scales with $N$" means, enumerate the structural cases, collect what existing spikes and segments already fix, and name the first moves that would actually resolve it.

**Date**: 2026-04-22

**Motivation.** #composition-closure Working Notes log "$N$-agent scaling of $\varepsilon^\ast$" as an open question (is it polynomial or exponential in team size?), and `TODO.md` flags this as "critical for applying the theory to large teams." For $N = 2$, there is one fully worked case (`msc/spike-composition-correlated-kalman.md`) and a two-agent sketch of the bridge lemma (`msc/spike-composition-bridge-2agent.md`, absorbed). For general $N$, there is nothing but the weakest-link bound $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ from #team-persistence. The conjectural folklore is that coupling *structure* dominates: sparse/tree-like coupling should allow efficient dimensionality reduction, fully-connected coupling should not, and real teams live somewhere between. This spike lays out the scaffolding so a future working pass can attack the question without re-deriving the frame.

**Depends on**: #composition-closure, #scope-composite-agent, #sector-persistence-template, #tempo-composition, #team-persistence, #unity-dimensions, #unity-closure-mapping, #compression-operations, `msc/spike-composition-correlated-kalman.md`, `msc/spike-agent-composition.md`, `msc/speculation-soc-composition.md`, `msc/spike-unity-closure-mapping.md`, `msc/spike-mori-zwanzig-composition.md`.

---

## 1. The Question, Stated Precisely

The formal object is $\varepsilon^\ast(N)$: the minimal achievable closure defect ( #composition-closure) for a composite of $N$ sub-agents, as defined by

$$\varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert.$$

"Scales with $N$" is not yet a single well-formed question. Four distinct readings exist, and the answer probably differs across them:

1. **Pointwise $\varepsilon^\ast(N)$ at a fixed coupling structure.** Fix an $N$-agent system with a specified interaction graph $\mathcal G_N$, admissible projection class $\mathcal P_{\text{adm}}$, and macro-dynamics class $\mathcal M_{\text{adm}}$. Ask for $\varepsilon^\ast$ as $N \to \infty$ along a family $\{\mathcal G_N\}$ (e.g., stars, trees, complete graphs, $k$-regular graphs). This is the most operational reading.

2. **Expectation over random coupling.** Fix an ensemble over $\mathcal G_N$ (Erdős–Rényi at density $p$, preferential-attachment, small-world) and ask for $\mathbb E[\varepsilon^\ast(N)]$ or $\mathbb P(\varepsilon^\ast(N) \gt \varepsilon_{\text{max}})$. The right framing if the theory is to make claims about "typical" large teams.

3. **Worst case over admissible couplings.** $\sup_{\mathcal G_N} \varepsilon^\ast(N)$ subject to some structural budget (bounded max degree, bounded pairwise coupling strength, etc.). This is the pessimism bound relevant for robustness claims ("how bad can it get?").

4. **Best achievable projection class as $N$ grows.** Fix the sub-agents and coupling, but allow $\mathcal P_{\text{adm}}$ to grow in expressive power with $N$ (e.g., macro-dimension $\dim \mathcal X_c = k(N)$ chosen adaptively). Ask for the Pareto frontier $\varepsilon^\ast(N, k)$. This is the rate-distortion reading connecting naturally to #unity-closure-mapping.

Reading 1 is the easiest to attack; reading 4 is the most honest, because (P3) dimensionality-reduction is meaningful only relative to $\dim \mathcal X_{\text{micro}}$, which itself grows with $N$. Subsequent sections use reading 1 unless noted.

*[Scope caveat]* The question presumes #scope-composite-agent is satisfied for the $N$-agent system — i.e., there is at least one alignment route (shared objective, hierarchical derivation, mutual benefit) that makes the group a composite rather than a multi-agent system. Without scope-satisfaction, $\varepsilon^\ast$ is still well-defined as a projection property of the micro-dynamics but has no interpretation as composition quality. Large $N$ plausibly *stresses* scope-satisfaction — maintaining shared objectives or hierarchical derivation over many agents is itself expensive — but this spike treats scope as given and focuses on the defect conditional on it.

## 2. Why It Matters (Load-Bearing Downstream)

- **#composition-closure Working Notes** explicitly logs "$N$-agent scaling of $\varepsilon^\ast$" as open. The bridge lemma's trajectory bound $\varepsilon^\ast \nu_c / \alpha_c$ becomes unusable if $\varepsilon^\ast$ grows exponentially with $N$.
- **#tempo-composition** derives Brooks's Law as an instance of the sector-persistence template: adding an agent increases $\sum_i \mathcal T_i$ but may increase $\varepsilon^\ast \nu_c$ faster. Whether this happens *in practice* depends on how $\varepsilon^\ast$ actually scales with $N$ under typical couplings.
- **#team-persistence** supplies $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ (weakest-link). This is an $\alpha_c$ bound, not a $\varepsilon^\ast$ bound, and the two interact in the bridge lemma in opposite directions. Clarifying their joint scaling with $N$ is prerequisite to any composite-persistence claim for large teams.
- **TODO.md ("Composition scaling with $N$")** names this as critical for applying the theory to large teams; it is currently listed without an associated spike.

## 3. What's Already Known (Honestly, Very Little)

### 3.1 $N = 2$, Kalman composite ( `spike-composition-correlated-kalman.md`)

For two scalar Kalman filters tracking a correlated bivariate random walk with no communication, under the means-only projection $\Lambda_x(\hat\omega_1, P_1, \hat\omega_2, P_2) = (\hat\omega_1, \hat\omega_2)$:

$$\varepsilon^\ast = 0 \quad \text{for all } \rho_{\text{corr}} \in (-1, 1) \text{ at steady state.}$$

This is a *representability* result, not optimality — the cost of independence shows up as a performance gap $\Delta_{\text{perf}} \approx 2\rho^2 q^2 r / (S^\ast)^2$ (quadratic in correlation, small-$\rho$ expansion), not a closure defect. The first genuine $\varepsilon^\ast \gt 0$ in the spike arises from purposeful sub-agents with Beta-Bernoulli edge updates, where the discarded auxiliary state $n$ *diverges* (the Beta-Bernoulli $1/(n+2)$ gain cannot be matched by a fixed-gain macro-dynamics). The $N = 2$ case is therefore ambiguous as a scaling baseline: its "natural" closure defect is zero under linear-Gaussian estimation and non-zero under the simplest purposeful extension. Which of the two carries over to $N \gg 2$ is the open question.

### 3.2 $N = 2$, non-degenerate Kalman ( `spike-unity-closure-mapping.md` §Two-axis structure)

For two Kalman filters with heterogeneous gains $K_1^\ast \neq K_2^\ast$, projected to the 1D sum $\hat\omega_+ = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$:

$$\varepsilon_x^2 = (\Delta K/2)^2 \big[S_- - C_{+-}^2/S_+\big].$$

Two independent drivers of $\varepsilon_x$: sub-agent unity (process correlation, $U_M$) and update-rule heterogeneity ($\Delta K = K_1^\ast - K_2^\ast$). This is the two-axis structure flagged in #unity-closure-mapping and as a gap in #unity-dimensions. For $N$-scaling purposes, the pertinent question is whether either axis has a natural $N$-generalization — e.g., "aggregate heterogeneity" $\sum_{i \lt j} \lvert K_i - K_j \rvert^2$ — and whether $\varepsilon_x^2$ in a $k$-dimensional projection grows linearly, polynomially, or worse in those aggregates.

### 3.3 Weakest-link bound on $\alpha_c$ ( #team-persistence, #composition-closure Discussion)

$$\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}}), \qquad R_c \leq \min_i R_i.$$

This bounds the *correction rate* at the composite level, not the closure defect itself. As $N$ grows, the minimum over $i$ can only decrease (the weakest link gets weaker or stays the same). Combined with the bridge lemma's $\varepsilon^\ast \nu_c / \alpha_c$ ultimate-bound form, the implication is that the *trajectory error* bound grows at least $\propto 1/\alpha_c$ as the weakest sub-agent degrades — but this is driven by $\alpha_c$ deterioration, not by $\varepsilon^\ast$ itself.

### 3.4 Coordination-overhead tempo lower bound ( #tempo-composition)

$$C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \lVert \delta_{\text{critical}}\rVert.$$

This converts $\varepsilon^\ast$ into a tempo penalty. Additive (negotiation, synchronization, conflict) costs are acknowledged but uncharacterized. For $N$-scaling, the structural move would be bounding these additive costs by a function of $\mathcal G_N$ — plausibly edge-count for negotiation, diameter for synchronization, triangle-density for conflict — and stacking them against the linear growth of $\sum_i \mathcal T_i$.

### 3.5 Original composition spike ( `spike-agent-composition.md` §2.3–2.4, §8)

The original composition spike contains the first qualitative intuition for $N$-scaling (distinct from anything derived):

- Tempo composition: $\mathcal T_c \leq \sum_i \mathcal T_i$, with equality when channels are independent and coordination is lossless.
- The "composition gap" $\Delta \mathcal T = \sum_i \mathcal T_i - \mathcal T_c \geq 0$ is hypothesized to have a lower bound structurally (analogy to entropy of a mixture).
- §7 open question 2 asks whether there is an *irreducible* coordination cost — which, if it exists, would force $\varepsilon^\ast$ to be bounded below by something that scales with $N$ even for perfectly coordinated teams.

None of this is derived. It is the pre-formalized folklore that motivated the closure-defect formalism in the first place.

**Overall.** Everything above is either $N = 2$ exact, or structural bounds on related quantities ($\alpha_c$, $C_{\text{coord}}$) not on $\varepsilon^\ast$ itself. No claim about $\varepsilon^\ast(N)$ for $N \geq 3$ is currently derived anywhere in the theory.

## 4. The Structural Cases

Enumerate the coupling families that plausibly give distinct $N$-scaling behavior. *Intuitions below are intuitions — directional guesses about what the derivation might yield, not derivations.*

### 4.1 Tree-structured coupling (hierarchies)

Sub-agents connected via a tree with depth $d \sim \log N$ (balanced) or $d \sim N$ (linear chain). Each agent couples only to its parent and children. Motivates: military chain of command, managerial hierarchies, decomposable distributed algorithms.

*Intuition.* Trees admit natural hierarchical projections — coarse-grain each subtree to a summary statistic and recurse. If each subtree-projection incurs defect $\varepsilon_{\text{tree}}$, a balanced-tree composite plausibly has $\varepsilon^\ast(N) \sim \varepsilon_{\text{tree}} \cdot \log N$ or $\sim \varepsilon_{\text{tree}}$ (if subtree defects do not accumulate). Linear chains may accumulate defect over depth, giving $\sim N$ in the worst case.

*Why this intuition might be wrong.* The admissibility constraints (A1)–(A4) apply at every level of the hierarchy. If the per-level bridge lemma is multiplicative (trajectory error amplification per level), defects could compound geometrically in depth. Whether balanced-tree structure permits the same template to instantiate cleanly at each level is exactly the Section III composition-consistency question.

### 4.2 Fully-connected coupling (every-to-every)

Each pair $(i, j)$ interacts through a coupling of bounded strength. Motivates: flat teams with all-to-all communication, fully-connected neural ensembles, small committees.

*Intuition.* Number of pairwise couplings is $O(N^2)$, number of triangles $O(N^3)$, etc. Every sub-agent's state enters every other's update (directly or with small lag). The projection must either (i) preserve enough pairwise state to capture all couplings — forcing $\dim \mathcal X_c \geq O(N^2)$ and violating (P3) in any useful sense — or (ii) compress pairwise coupling into a mean-field summary statistic, accepting defect. Mean-field compression in interacting-particle systems incurs defect $\sim 1/\sqrt N$ when the system is close to a Gaussian fluctuation regime (law-of-large-numbers plus central-limit scaling), but $\sim O(1)$ away from it. So the intuition is: fully-connected $\varepsilon^\ast(N)$ might be bounded independently of $N$ in a mean-field regime (favorable) or grow like $O(1)$ forever (unfavorable), with a phase transition somewhere.

*Why this intuition might be wrong.* The interacting-particle-system analogy relies on exchangeability (de Finetti) or mean-field decoupling (propagation of chaos). AAD sub-agents are not exchangeable in general — heterogeneity of $K_i$ is exactly the driver identified in #unity-closure-mapping. Without exchangeability, mean-field intuitions may not apply.

### 4.3 Sparse / $k$-regular coupling

Each agent couples to $k$ neighbors, $k$ fixed as $N$ grows. Motivates: distributed systems with bounded fan-out, modular teams with limited interfaces, lattice-organized processes.

*Intuition.* $k$-regular gives $O(N)$ edges rather than $O(N^2)$; local-neighborhood projections should give $\varepsilon^\ast(N)$ bounded or growing sublinearly if the coupling is local and contracting. Close in spirit to Mori–Zwanzig projection on lattice systems — the zero-lag kernel bound ( #composition-closure Working Notes, Mori-Zwanzig partial note) is the candidate quantitative estimate.

*Why this intuition might be wrong.* Long-range correlations can propagate through short-range couplings (critical phenomena, percolation). Even with $k$ fixed, correlation lengths can diverge and the mean-field approximation fails near criticality — the SOC speculation (`msc/speculation-soc-composition.md`) is exactly the claim that AAD composites may sit near such a critical point.

### 4.4 Small-world coupling

Mostly local with a few long-range shortcuts; short average path length, high clustering coefficient. Motivates: real organizations (Milgram), real biological networks, realistic human teams.

*Intuition.* Small-world sits between $k$-regular and fully-connected. Short shortcuts let information propagate globally in $O(\log N)$ steps while preserving mostly-local structure. Plausibly permits hierarchical-plus-shortcut projections: local neighborhoods coarse-grained, shortcuts preserved. $\varepsilon^\ast(N)$ then depends on shortcut density and might interpolate polynomially between the tree and fully-connected cases.

*Why this intuition might be wrong.* Network topology alone doesn't determine what dynamics can be coarse-grained. Nothing about a small-world graph tells us whether the per-edge coupling is contracting or amplifying.

### 4.5 Summary table

| Coupling family | Edge count | Naive intuition for $\varepsilon^\ast(N)$ | Derivation effort |
|---|---|---|---|
| Balanced tree | $N-1$ | $\log N$ (if bridge lemma instantiates per-level) or bounded | Moderate — recursion on subtrees |
| Linear chain | $N-1$ | $N$ at worst (compounding) | Low — 1D should be tractable |
| $k$-regular | $kN/2$ | bounded or $1/\sqrt N$ if mean-field | High — local interaction analysis |
| Small-world | $N \log N$ ish | interpolates | Very high |
| Fully-connected | $N(N-1)/2$ | bounded in mean-field, $O(1)$ otherwise | High — requires mean-field machinery |

All rows are intuition-grade. None are derivations.

## 5. Axes the Question Composes With

$N$-scaling does not sit in isolation. Three other axes of the closure-defect formalism bear on how $N$ enters.

### 5.1 Macro-timescale ratio $K_c$

#composition-closure's macro-step formulation introduces the timescale ratio $K_c \geq 1$: the number of micro-timesteps per macro-step. When $K_c \gg 1$ the composite lives at a strictly slower timescale and only macro-boundary states enter $\varepsilon_x$. For large-$N$ composites this is plausibly the natural regime ( #temporal-nesting asserts that composites typically update more slowly than their constituents). If $K_c$ grows with $N$ (e.g., $K_c \sim N^\beta$ for $\beta \gt 0$), the closure-defect is measured against more averaged observation windows, which may reduce $\varepsilon^\ast$ independent of any structural coupling effect.

*Implication.* Any scaling claim $\varepsilon^\ast(N) \sim f(N)$ must specify how $K_c$ scales. A fair comparison probably requires fixing $K_c$ (e.g., $K_c = 1$ or $K_c$ independent of $N$) and isolating the coupling effect, or else jointly characterizing $\varepsilon^\ast(N, K_c)$ as a two-parameter surface.

### 5.2 Unity dimensions × update heterogeneity

#unity-closure-mapping established that $\varepsilon^\ast$ depends on *both* sub-agent unity (captured by $U_M, U_O, U_\Sigma, U_{\text{obs}}$) *and* update-rule heterogeneity (not captured by any unity dimension as currently defined). For large $N$, each of these becomes an aggregate:

- Aggregate unity: e.g., pairwise average $\bar U_M = \frac{2}{N(N-1)}\sum_{i \lt j} U_M^{(i,j)}$ or the multi-information fraction as originally defined.
- Aggregate heterogeneity: e.g., variance of $K_i$ across sub-agents, or a suitable operator-norm distance across $f_{M,i}$.

Either aggregate may scale non-trivially with $N$. For random sub-agents drawn from a distribution of update rules, update heterogeneity likely scales like $\sqrt{N}$ (standard deviation of sample variance), which would in turn make $\varepsilon_x^2 \propto (\Delta K)^2$ contributions to the defect aggregate additively.

*Implication.* An honest $N$-scaling result likely requires a two-parameter statement of the form "$\varepsilon^\ast(N) \sim f(N, \bar U, \bar \Delta)$," not a single scaling exponent.

### 5.3 The macro-state dimension $k = \dim \mathcal X_c$

(P3) requires $\dim \mathcal X_c \lt \dim \mathcal X_{\text{micro}}$. But $\dim \mathcal X_{\text{micro}}$ grows with $N$. Whether $k$ is held fixed, grows with $N$, or is optimized adaptively determines which of the four readings from §1 we are answering:

- $k$ fixed: the most aggressive compression, most likely to drive $\varepsilon^\ast \to \infty$ as $N \to \infty$.
- $k \sim N$: linear budget; analogous to retaining one macro-coordinate per agent. Expected to preserve enough structure that $\varepsilon^\ast$ remains bounded for benign couplings.
- $k = o(\dim \mathcal X_{\text{micro}})$: the rate-distortion Pareto frontier.

Reading 4 from §1 (allowing $k$ to grow) is the cleanest framing for large-$N$: it produces $\varepsilon^\ast(N, k)$ as a surface, and the relevant question becomes "what is the minimum $k(N)$ such that $\varepsilon^\ast(N, k) \leq \varepsilon_{\text{max}}$?"

## 6. Candidate First Moves (What Would Need to Be Worked)

The following are ordered by expected effort and epistemic payoff. The spike does not attempt them.

### 6.1 $N$-Kalman linear-chain extension ($K_c = 1$, $k = N$)

Easiest starting point. $N$ Kalman filters tracking components of a bivariate-extended-to-$N$ random walk with tridiagonal (chain) process-noise covariance. Natural projection: means-only. By the same argument as `spike-composition-correlated-kalman.md`, the means decouple from covariances at steady state and $\varepsilon_x = 0$ for any chain correlation. This would establish that the *trivial* $\varepsilon^\ast = 0$ result of $N = 2$ extends to linear chains without structural modification.

Effort: low (direct generalization of the $N = 2$ algebra). Payoff: a clean "baseline" result that distinguishes coupling-structure-driven defect from scaling-driven defect. If $\varepsilon^\ast(N) = 0$ in the benign chain case for all $N$, then the non-zero cases of interest are driven by (i) update heterogeneity, (ii) purposeful substates, or (iii) non-local coupling — not by $N$ per se.

### 6.2 Hierarchical tree case (balanced, $K_c = 1$)

Balanced binary tree of depth $d = \log_2 N$. Each internal node is itself an AAD agent receiving aggregated state from its children. Natural projection: recursive means-only, propagating upward.

Ask: does the bridge lemma instantiate cleanly at each level? If yes, is the per-level defect additive in $d$? This tests whether the sector-persistence template's recursive-application in the holonic framework is consistent.

Effort: moderate. Payoff: a constructive demonstration that hierarchical composition is $\varepsilon^\ast$-benign, with a computable defect that scales at most $\log N$ (optimistic) or as $N$ (chain-like) in worst-case balance. Also exercises composition-consistency at multiple levels, which is a stated open item from `msc/spike-agent-composition.md`.

### 6.3 Fully-connected $N$-agent Beta-Bernoulli strategy composite

Generalize Part 2 of `spike-composition-correlated-kalman.md` to $N$ agents, each with a single-edge Beta-Bernoulli strategy DAG. Ask what happens to $\varepsilon^\ast$ as $N$ grows.

Effort: moderate-to-high. Payoff: attacks the purposeful-substate case directly. The auxiliary-state divergence phenomenon ($n_i \to \infty$ forcing fixed-gain defect) almost certainly worsens with $N$; the question is whether in a specific, quantifiable way.

### 6.4 Mori–Zwanzig $N$-agent zero-lag bound

Apply the zero-lag kernel bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ (from the MZ partial note in #composition-closure Working Notes) to structured $N$-agent propagators — tridiagonal (chains), dense-symmetric (complete graphs), block-diagonal (hierarchies). This gives *lower* bounds on $\varepsilon^\ast(N)$ in each structural case, complementing the *upper* bounds from explicit projections.

Effort: moderate if restricted to linear-propagator cases; high in general. Payoff: concrete quantitative claims about which coupling structures can achieve $\varepsilon^\ast \to 0$ and which cannot, derived from standard spectral machinery rather than constructed per-case.

### 6.5 Rate-distortion $\varepsilon^\ast(N, k)$ surface

Using the IB framing ( #compression-operations), construct the $\varepsilon^\ast(N, k)$ rate-distortion surface for at least one tractable $N$-agent family (linear-Gaussian with specified coupling). Extract scaling of the minimum $k$ at fixed $\varepsilon^\ast = \varepsilon_{\text{max}}$.

Effort: high. Payoff: the cleanest framing of the question, and the one most likely to produce a universal answer of the form "$\varepsilon^\ast(N, k) = g(N/k, \bar U, \bar \Delta)$ for large $N$."

## 7. Connection to Other Open Questions

- **SOC / RG speculation** ( `msc/speculation-soc-composition.md`). Scaling of $\varepsilon^\ast$ with $N$ is *exactly* the question the RG inverse-argument addresses: requiring scale-invariance of agent-level distributions constrains which composition operations are admissible. If the inverse argument goes through, it would characterize $\varepsilon^\ast(N)$ as the fixed-point property rather than as a separately-derived scaling law. This is speculation-grade; it is not available as machinery yet.

- **Mori–Zwanzig connection** ( #composition-closure Working Notes, `msc/spike-mori-zwanzig-composition.md`). The zero-lag kernel bound gives a lower bound on $\varepsilon^\ast$ in terms of an operator-norm quantity that depends explicitly on the micro-propagator's spectrum. For structured $N$-agent propagators, this spectrum has known $N$-scaling (tridiagonal: $O(1/N^2)$ gap; dense: $O(1)$; hierarchical: level-dependent). The MZ bound is the most direct link between $N$-structure and $\varepsilon^\ast$ currently available — but it closes only on the zero-lag piece, not the full kernel, and relies on stationarity (which fails for Beta-Bernoulli purposeful agents).

- **Tempo-composition coordination costs** ( #tempo-composition, Working Notes). The additive $C_{\text{negotiation}}, C_{\text{sync}}, C_{\text{conflict}}$ terms are uncharacterized in general. Closing them into specific functions of $\mathcal G_N$ would give the tempo-side analog of the $\varepsilon^\ast$ scaling — and via the tempo $\to$ closure-defect conversion $C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert$, an independent handle on $\varepsilon^\ast(N)$.

- **Symbiogenic composition** ( `msc/spike-symbiogenic-composition.md`). Hierarchical absorption ("symbiogenesis") is one of three composition mechanisms distinguished in the spike and now promoted to #symbiogenic-composition. It reframes teleological unity $U_O$ as a *scope* condition rather than a quality metric. The $N$-scaling question may split differently depending on which mechanism is dominant: peer coupling may scale differently from hierarchical absorption, and mixed mechanisms (symbiogenesis *embedded in* peer coupling) may be typical.

- **Team-persistence topological structure** ( #team-persistence Working Notes, item 1). The spike notes that topology-dependent analysis (peer networks, ensembles, hierarchies) was deferred from TFT Appendix F.4. That deferred work is adjacent to this one — topology enters both $\alpha_c$ (weakest-link or improved by cooperation) and $\varepsilon^\ast$ (coupling structure), and a joint treatment could share machinery.

## 8. Where This Sits in the "Inevitability Core" Classification

Per FORMAT.md's three-ring analysis, a scaling result $\varepsilon^\ast(N) \sim f(N, \mathcal G, \bar U, \bar \Delta)$ is almost certainly **not** an inevitability-core candidate:

- *Multiple formulations fit.* For each coupling family there are several plausible scaling laws (polynomial with various exponents, bounded, logarithmic). Which is right depends on the coupling dynamics and the projection class — both of which admit multiple reasonable choices.
- *The right framing is empirical in part.* "What does $\varepsilon^\ast$ do for realistic large teams?" is ultimately a question about which couplings occur in practice, not only about what the formalism forces.

The honest ring placement is **canonical formulation** (second ring) for the framing — what counts as "the" scaling law, which aggregates to measure, which normalizations to use. Specific scaling claims for specific families (tree vs complete vs $k$-regular) are probably **empirical/heuristic** (third ring) at their ceiling: derivable exactly in tractable special cases (linear-Gaussian, exchangeable, stationary), heuristic elsewhere.

*Exception.* If the RG inverse argument from `msc/speculation-soc-composition.md` works, the scaling exponents would fall out as universal properties of the composition operation's fixed points, which is inevitability-core shape. This is speculation; nothing in this spike assumes it.

The "max attainable status" for a future #composition-scaling-N segment is therefore *robust-qualitative* (or *conditional*) in general, *exact* in tractable special cases. Promoting it beyond that without the RG argument would be overreach.

## 9. What This Spike Does Not Do

Explicitly:

- No derivation of $\varepsilon^\ast(N)$ for any $N \geq 3$.
- No decision among the four readings in §1; the choice is deferred to whoever picks up the resolution work.
- No formalization of the aggregate unity or heterogeneity measures; current #unity-dimensions does not cover this, and §5.2 only flags the need.
- No bounds on the $K_c$-dependence; §5.1 only notes it matters.
- No attempt to derive the coordination-cost decomposition for general $\mathcal G_N$; §7 notes it would be one independent handle.
- No use of the RG / SOC machinery; it remains speculation.

Any one of these is a multi-session task. This spike's purpose is to ensure that whoever attempts them starts from a framed question, not from folklore.

## 10. Working Notes and Open Questions

- **Reading selection is the first substantive decision.** Reading 1 (pointwise) is easiest; reading 4 (rate-distortion surface) is most honest. Reading 2 (expectation over random coupling) is most useful for applications but requires specifying an ensemble — and the ensemble choice is itself a research question.
- **Exchangeability assumption.** Much of the fully-connected intuition in §4.2 relies on exchangeable or nearly-exchangeable sub-agents. Real teams are not exchangeable (heterogeneous skills, heterogeneous update rules). The #unity-closure-mapping two-axis structure is precisely the non-exchangeable case; how it generalizes to $N \gg 2$ is open.
- **Purposeful-substate scaling is probably the critical case.** Part 2 of `spike-composition-correlated-kalman.md` already showed that $\varepsilon^\ast \gt 0$ arises generically in purposeful agents via auxiliary-state divergence. If this persists (likely) and aggregates across $N$ (possibly), then purposeful large-team composites may have $\varepsilon^\ast(N)$ that grows in $N$ even under benign structural coupling. This would make the Section III composite-persistence claims load-bearing on an *unfavorable* scaling, which is important to know.
- **Note on terminology.** "Scaling with $N$" invites the language of exponents and asymptotic notation; whether the theory produces exponents or only qualitative "grows / stays bounded" depends on how many of the tractable special cases can be worked in closed form. Do not commit to exponents before the machinery is in place to compute them.
- **Question for the outline.** Should there eventually be a dedicated segment (`#composition-scaling-N` or similar) or does this scaling live as Working-Notes content within #composition-closure? The volume of structural content here (four coupling families, four composing axes, five candidate first moves) argues for its own segment; the lack of derived content argues for keeping it as Working Notes until something is derivable. The call is premature until a resolution spike lands at least one tractable case.

## 11. Flagged Elsewhere-Repairs (Do Not Edit Here)

Items this spike surfaced that belong in other files, recorded here per the guardrails in the spike brief:

- #unity-dimensions currently does not define aggregate unity for $N \gt 2$; §5.2 notes this as a gap. Resolution (if any) belongs in the #unity-dimensions Working Notes, not here.
- #tempo-composition's Working Notes acknowledge that $\varepsilon^\ast$ scaling with $N$ is open (§last bullet of that segment). The present spike is the formalization of what that note pointed at; a cross-reference could be added there when a resolution lands.
- `TODO.md`'s "Composition scaling with $N$" entry currently has no spike reference. Once this spike stabilizes, that entry should be updated to point to this file. Per the brief, this spike does not modify `msc/SPIKES.md`; that update is a separate pass.
