# Prior-Art Analysis: Compression Operations and the Shared IB Shape

> [!note]
> **Refreshed 2026-05-21.** The previous version named only three compression operations (model, strategy, communication) and omitted the fourth — *composition projection* $\Lambda$. The actual segment `disc-compression-operations.md` makes the (P1) admissibility condition the **Lagrangian-dual of a standard IB objective** — a derived result, not a stylistic observation. The previous version also imported the reverse-KL-via-regret-bound derivation from `#deriv-strategy-cost-regret-bound` §6.1 (which is a real and important result, just cross-referenced from this segment rather than living in it). This file now reflects the segment's actual four-instance structure plus the honest U-medium / U-strong distinction the segment defends.

**Target Claim:**
AAT contains **four** compression operations, each formulated in its own segment with its own objective, and three of the four are written in Information Bottleneck (IB) form already; the fourth is stated as an IB constraint:

| Instance | $X$ (source) | $T$ (compressed) | $Y$ (relevance variable) | $\beta$ (trade-off) |
|---|---|---|---|---|
| **Model compression** (`#form-information-bottleneck`) | $\mathcal C_t$ (chronica) | $M_t$ | $o_{t+1:\infty} \mid a_{t:\infty}$ | $\beta(\rho, \pi)$ — volatility and policy |
| **Strategy compression** (`#form-strategy-complexity-cost`) | $\mathcal C_t$ (chronica) | $\Sigma_t$ | $\pi^\ast \mid M_t$ | $\beta_\Sigma$ — cognitive cost per decision-bit |
| **Shared intent** (`#def-shared-intent`) | $G_t^{\text{full}} = (O_t, \Sigma_t)$ | $G_t^{\text{shared}}$ | $a_t^{\text{coordinated}}$ | bandwidth per coordination-bit |
| **Composition projection** (`#form-composition-closure` (P1)) | $X_{\text{micro},t}$ | $\Lambda_x(X_{\text{micro},t})$ | $o_{\text{micro},t+1} \mid a_{\text{micro},t}$ | $\beta(\epsilon_I)$ — rate-distortion Lagrange multiplier |

All four specialize the master IB form $T^\ast = \arg\min_{T \mid X} [I(X;T) - \beta \cdot I(T;Y)]$ with the Markov chain $Y - X - T$.

**Three derived / formulated results within this segment:**

1. **(P1) admissibility as IB Lagrangian-dual** (*derived*, from composition-closure + rate-distortion duality). The (P1) lower-bound constraint $I(\Lambda_x; \Lambda_o \mid \Lambda_a) \ge (1 - \epsilon_I) \cdot I(X_{\text{micro}}; o_{\text{micro}} \mid a_{\text{micro}})$ is equivalent to the Lagrangian form $\Lambda^\ast \in \arg\min [I(X_{\text{micro}}; \Lambda_x) - \beta(\epsilon_I) \cdot I(\Lambda_x; Y_{\text{rel}})]$ under rate-distortion duality, with $\epsilon_I \leftrightarrow \beta$ standard.

2. **Strategy compression source reformulation** (*formulation*). Replace the underspecified source "true causal structure" with the agent's actual evidence — the chronica $\mathcal C_t$ — making $\Sigma_t$'s IB instance parallel to $M_t$'s, differing cleanly in the relevance variable (prediction-relevance for $M_t$, guidance-relevance for $\Sigma_t$).

3. **Direction-alignment with active inference's variational free energy** (*observation*). The variational form of the $\Sigma_t$ relevance term uses KL divergence in the $\pi^\ast$-first direction (reverse-KL in the variational-inference vocabulary). This direction is *forced* by a regret-bound derivation in `#deriv-strategy-cost-regret-bound` §6.1 — Pinsker's inequality gives $R(Q_\Sigma) \le V_{\max} \sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(\pi^\ast \Vert Q_\Sigma)}$, while the opposite direction is vacuous ($+\infty$ under deterministic $\pi^\ast$ with any off-optimum mass). AAT and active inference agree on direction; AAT's derivation route is regret-bound rather than free-energy-gradient.

**Honest U-medium vs U-strong distinction.** What the four instances share: *shape* (objective structure), *variational calculus* (minimization over stochastic compressors), and *rate-distortion interpretation*. What they do not share: source type, relevance-variable availability, computability, or a single joint optimization problem. The unification is **U-medium** (shared shape and vocabulary) — *not* **U-strong** (single optimization problem with different bindings). The segment defends this restraint explicitly: cross-instance theorems do not follow from the shared shape alone; (P2) Lipschitz regularity, (P3) Gaussian-case dimensional reduction, and the interventional-relevance need for Pearl-Level-2 Regime-A edges all remain outside the IB frame.

---

## 1. State of the Field & Scientific Precedence

The literature is mature on each flank: IB itself, predictive-state compression, bounded-rational decision frameworks, control-as-inference, hierarchical generative models. AAT is honest about what it adopts vs. extends.

### Pillar 1: Information Bottleneck and Predictive-State Compression
- **Tishby, Pereira & Bialek (1999)** *The Information Bottleneck Method* — the master objective $I(X;T) - \beta I(T;Y)$ that all four AAT instances specialize. AAT adopts this directly.
- **Tishby & Polani (2011)** *Information Theory of Decisions and Actions* — applies IB to action selection; pioneers the agency-as-information-channel view.
- **Still, Crutchfield & Ellison (2007)** *Optimal causal inference* / **Creutzig, Globerson & Tishby (2009)** *Past-future information bottleneck in dynamical systems* — past→future compression in dynamical systems; the natural template for the $M_t$ instance.
- **Harremoës & Tishby (2007)** *The Information Bottleneck Revisited or How to Choose a Good Distortion Measure*.
- **Shore & Johnson (1980)** *Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy* — IEEE TIT 26:26. Axiomatizes IB's additivity via system-independence; if promoted to an AAT-internal axiom, IB would move from "adjacent member" to "fourth primary instance" in the `#disc-additive-coordinate-forcing` pattern.
- **Wolpert, Grochow, Libby & DeDeo (2014)** *Optimal high-level descriptions of dynamical systems* — state-space compression as predictive macro-projection; the closest precedent for the composition-projection ($\Lambda$) instance.

### Pillar 2: Bounded Rationality and Information-Theoretic Decision Theory
- **Genewein, Leibfried, Grau-Moya & Braun (2015)** *Bounded Rationality, Abstraction, and Hierarchical Decision-Making: An Information-Theoretic Optimality Principle* — unified bounded-rational objective across multiple internal interfaces; the strongest single nearby paper for multi-node IB-shaped architectures.
- **Ortega & Braun (2012, 2015)** *Thermodynamics as a theory of decision-making with information-processing costs* / *Information-Theoretic Bounded Rationality*.
- **Pen et al. (2017)** *An information-theoretic on-line update principle for perception-action coupling* — serial perception-action channel under IB.

### Pillar 3: Control as Inference / Minimum-Information Control (the sibling form)
The control-side instances use a sibling form where the relevance variable is control quality / target policy rather than an explicit observable:
- **Todorov (2006)** *Linearly-Solvable MDPs* — KL-divergence control cost making the Bellman equation linear.
- **Kappen (2005, 2009)** *Path Integral Control* — stochastic optimal control as KL minimization.
- **Tanaka, Kim, Parrilo & Mitter (2014)** *Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs* — sequential rate-distortion backbone.
- **Tanaka, Esfahani & Mitter (2015)** *LQG Control With Minimum Directed Information* — staged information-constrained controller.
- **Fox & Tishby (2016)** *Minimum-information LQG control Parts I/II* — sequential rate-distortion formulation of bounded LQG control.
- **Yang, Piantanida & Gündüz (2017)** *The multi-layer information bottleneck problem* — closest literal multi-layer IB result; joint rate-relevance region across a layered chain.

### Pillar 4: Active Inference and Variational Free Energy
- **Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo (2017)** *Active Inference: A Process Theory* / **Da Costa, Parr, Sajid, Veselic, Neacsu & Friston (2020)** active inference foundations — the variational free energy framework that achieves $\pi^\ast$-first KL direction by free-energy-gradient derivation. **AAT and active inference converge on the same direction; the derivation routes differ (regret-bound vs. free-energy-gradient).** Active inference encodes goals as priors ($C(o) = \log P_{\text{pref}}(o)$); AAT's regret-bound route derives the same direction without that assumption.

### Pillar 5: Hierarchical Generative Models (the broader family AAT sits within)
- **Friston (2008)** *Hierarchical models in the brain* / **Friston (2010)** *The free-energy principle: a unified brain theory?* / **Clark (2013)** *Whatever next?* / **Hohwy (2013)** *The Predictive Mind*. AAT's four compression operations are *expressible* within the hierarchical-generative-model frame as specific layer-bindings — `disc-compression-operations` acknowledges this lineage openly. What AAT adds: (a) relevance variables made first-class with explicit per-instance bindings; (b) (P1)–(P3) admissibility for composition with measurable closure-defect bound (not a native HGM construct); (c) regime-indexed edges with Pearl-Level-2 interventional relevance for Regime A (HGMs don't natively address causal-vs-associational distinction).

### Pillar 6: Extensions and Adjacent Directions
- **Chechik, Globerson, Tishby & Weiss (2005)** *Information Bottleneck for Gaussian Variables* — JMLR 6:165. Closed-form Gaussian IB; the natural specialization for the symmetric two-Kalman case in `#result-unity-closure-mapping`.
- **Wieczorek & Roth (2017)** and follow-ups — *causal IB* with interventional rather than associational relevance variables. The natural extension for AAT's Pearl-Level-2 needs in Regime-A edges; not yet derived in AAT.

---

## 2. Key Anchor Papers Identified

1. **Tishby, N., Pereira, F. C. & Bialek, W. (1999).** *The Information Bottleneck Method.* (`physics/0004057`)
   *Significance:* The master IB objective; AAT adopts directly. Cited in all four instance segments.
2. **Tishby, N. & Polani, D. (2011).** *Information Theory of Decisions and Actions.*
   *Significance:* Applies IB to action selection; precedent for the agency-as-information-channel view AAT generalizes.
3. **Genewein, T., Leibfried, F., Grau-Moya, J. & Braun, D. A. (2015).** *Bounded Rationality, Abstraction, and Hierarchical Decision-Making.* Frontiers Robotics AI 2:27.
   *Significance:* The strongest single nearby precedent for multi-node IB-shaped architectures; explicitly maintains that convergence/convexity guarantees do not automatically carry over across the cases, prefiguring AAT's U-medium honesty.
4. **Wolpert, D. H., Grochow, J. A., Libby, E. & DeDeo, S. (2014).** *Optimal high-level descriptions of dynamical systems.*
   *Significance:* State-space compression as predictive macro-projection; the closest precedent for AAT's composition-projection instance.
5. **Friston, K. J., FitzGerald, T., Rigoli, F., Schwartenbeck, P. & Pezzulo, G. (2017).** *Active Inference: A Process Theory.*
   *Significance:* The variational free energy framework AAT explicitly contrasts with on direction-alignment grounds — same direction, different derivation route.
6. **Fox, R. & Tishby, N. (2016).** *Minimum-information LQG control Parts I/II.* CDC 2016.
   *Significance:* Direct sequential rate-distortion formulation of bounded control; the sibling-form lineage for control-side compressions.
7. **Shore, J. E. & Johnson, R. W. (1980).** *Axiomatic derivation of the principle of maximum entropy.*
   *Significance:* The axiomatization that would promote IB from adjacent family member to fourth primary instance in `#disc-additive-coordinate-forcing` if formally adopted.
8. **Chechik, G., Globerson, A., Tishby, N. & Weiss, Y. (2005).** *Information Bottleneck for Gaussian Variables.* JMLR 6:165.
   *Significance:* Closed-form Gaussian IB; natural specialization for the symmetric two-Kalman case in composition.

---

## 3. Conclusion on Novelty & Overlap

The literature is broad and active. AAT does not invent IB, does not invent control-as-inference, does not invent hierarchical generative models, does not invent active inference's variational free energy. The honesty about adoption is built into the segment — *"#form-information-bottleneck adopts the Lagrangian form from Tishby, Pereira & Bialek 1999 as an applied external theorem"* — and the family relationship to predictive-coding / FEP is explicitly acknowledged.

**Where AAT actually contributes:**

1. **The (P1)-as-IB-Lagrangian-dual derivation (theorem-grade math).** Showing that the composition-admissibility condition (P1) is the Lagrangian-dual of a standard IB objective at $\beta(\epsilon_I)$ is a *derived result* using rate-distortion duality (standard, Cover & Thomas §I.12–13). The derivation is mechanical once the connection is named, but the *naming* and the *consequence* — that admissible projections sit on or above the IB frontier at $I(X;T) \le I_{\max}(\epsilon_I)$ — close two prior Working Notes (the open IB-unification question in `#form-composition-closure` and the conjecture in `#result-unity-closure-mapping` §6). This is Nash-style: new theorem derived using established rate-distortion duality in an AAT-internal setting.

2. **The fourth compression operation (composition projection) explicitly placed in the IB family (architectural-synthetic novelty).** The prior literature has IB for prediction (Still-Crutchfield, Creutzig-Globerson-Tishby), IB for control (Tishby-Polani, Fox-Tishby), IB for layered communication (Yang-Piantanida-Gündüz), and predictive macro-projection (Wolpert et al.) — but the AAT move of placing *composition projection itself* in the same family as the three other agency interfaces, with the (P1) Lagrangian-dual derivation as the formal bridge, does not appear as an articulated framework in the search.

3. **The U-medium scope-honesty discipline (architectural novelty + CS-norm precision).** The explicit refusal to overclaim — *"this segment states U-medium (shared shape) honestly rather than overclaiming U-strong"* — and the careful taxonomy of what does (shape, variational calculus, rate-distortion interpretation) and does not (source type, relevance-variable availability, computability, single joint optimization) carry over, is the kind of named-scope discipline that is first-class in CS. The non-transfer rule (cross-instance theorems do not follow from shape alone) is itself a useful framework rule, prefiguring future agent-theoretic work in the same family. Genewein-Leibfried-Grau-Moya-Braun 2015 prefigures this kind of restraint at a local scale; AAT elevates it to a framework rule.

4. **The strategy-compression source reformulation (formulation move).** Moving $\Sigma_t$'s IB source from "true causal structure" (not an AAT object) to the chronica $\mathcal C_t$ (a well-defined AAT object) makes the strategy and model instances structurally parallel — both compress the same source for different relevance variables (prediction vs guidance). This is a formulation cleanup, not a new theorem, but it fixes an ontological issue in the prior `#form-strategy-complexity-cost` formulation.

5. **The direction-alignment recognition with active inference + the regret-bound derivation route (theorem-grade content, even if the formal derivation lives in `#deriv-strategy-cost-regret-bound`).** The reverse-KL ($\pi^\ast$-first) direction is *forced* by a regret-bound derivation via Pinsker / Bretagnolle-Huber: the opposite KL direction is vacuous ($+\infty$) under deterministic $\pi^\ast$ with any off-optimum mass. This derivation is a substantive contribution (Nash-style: new result using Pinsker's inequality in an AAT-internal regret-bound setting). The convergence with active inference's free-energy-gradient route is itself a structural observation — same direction, different derivation, AAT's route avoids the "preferences as priors" assumption that collapses goal-update diagnostic orthogonality. Direction-alignment *and* derivation-route-distinction are both real contributions; the segment surfaces both honestly.

6. **The (P2)-(P3)-interventional-relevance non-transfer (analytical honesty / scope discipline).** Three things explicitly outside the IB frame: (P2) Lipschitz continuity (analytic requirement for the bridge lemma; IB doesn't impose continuity); (P3) dimensional reduction (in Gaussian-IB, full support at finite $\beta$; categorical dimensionality reduction is harder than rate); interventional relevance for Pearl-Level-2 edges in Regime A. Each is a named scope marker that prevents the shared-shape framing from being inflated. This precision is the CS norm — naming what does and doesn't follow from the unification is the contribution.

**Where AAT does *not* claim novelty:**
- The IB objective itself (Tishby-Pereira-Bialek 1999; adopted).
- Predictive-state compression as IB (Still-Crutchfield-Ellison 2007, Creutzig-Globerson-Tishby 2009).
- Multi-node bounded-rational architectures (Genewein-Leibfried-Grau-Moya-Braun 2015; Ortega-Braun).
- Control-as-sequential-rate-distortion (Tanaka, Fox-Tishby, Todorov, Kappen).
- Hierarchical generative models / FEP (Friston, Clark, Hohwy).
- Active inference (Friston et al. 2015/2017).

**AAT-native methodological moves on this row** (per the math-novelty-recognition discipline):
- The four-instance bindings table making the shared shape explicit at one place.
- The (P1) → IB-Lagrangian-dual derivation, closing two prior Working Notes.
- The U-medium framework discipline — shared shape ≠ shared theorems; layer-local non-transfer.
- The strategy-compression source reformulation (chronica-as-source, parallel to model compression).
- The taxonomy of what stays outside the IB frame ((P2), (P3), interventional relevance).

**Epistemic status of the load-bearing segment.** `disc-compression-operations.md` is `status: robust-qualitative`. The shared-shape claim is *discussion-grade* (presentational observation). The (P1) Lagrangian-dual is *derived* (mechanical from rate-distortion duality). The $\Sigma_t$ source reformulation is a *formulation* choice. The reverse-KL-via-regret-bound result is *derived* but lives in the sibling segment `#deriv-strategy-cost-regret-bound` §6.1. Max attainable: *robust-qualitative* for the shared-shape claim; *derived* for (P1) as IB dual; *formulation* for the source fix. **U-strong** (single master optimization problem) is *not* established and unlikely to be, per the honest U-medium positioning.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Medium.** The (P1) Lagrangian-dual derivation is theorem-grade (closes two prior Working Notes). The reverse-KL-via-regret-bound result in `#deriv-strategy-cost-regret-bound` §6.1 — referenced from this segment but living elsewhere — is also theorem-grade (Pinsker-Bretagnolle-Huber applied to an AAT-internal regret bound in an axiomatic setting). The cross-layer-theorems-don't-follow non-transfer rule has analytical content. Multiple substantive theorem-grade items beyond the imported IB machinery.
- *Arch Novelty:* **High.** The four-instance bindings table; the U-medium / U-strong discipline as a framework rule; the explicit (P2)/(P3)/interventional-relevance non-transfer taxonomy; the (P1) Lagrangian-dual placement of composition projection in the IB family. These are AAT-native methodological inventions.
- *Synth Novelty:* **High.** The four-interface unification under one rate-distortion spine, with explicit acknowledgment of the broader hierarchical-generative-model lineage, is a novel framework-level synthesis. The literature has IB-for-prediction, IB-for-control, multi-layer IB, predictive macro-projection — but not the four-agency-interface placement with the (P1) Lagrangian-dual bridge.
- *Appl Novelty:* **None.** No domain-specific instantiation in this meta-segment.
- *Impact:* **Medium.** The recognition + (P1) Lagrangian-dual + U-medium discipline organizes a substantial fraction of AAT's compression machinery and gives several neighboring fields (bounded rationality, control-as-inference, active inference, predictive-state compression, macro-abstraction) a clean common map. Direction-alignment with active inference plus avoidance of the "preferences as priors" trap is a structural contribution to the active-inference debate. Less likely to produce a single high-impact theorem on its own than rows 02 / 03 / 05 / 08 / 10, but materially shapes the framework's coherence.
