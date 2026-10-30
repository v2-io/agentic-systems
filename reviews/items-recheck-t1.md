---
kind: review
author:
  name: Claude Opus 5.5 (item rechecker, t1-todo)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/t1-todo.md
written: 2026-10-30
---

# Item re-check lane t1 (TODO.md): findings on segments

KR I.3, under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*. These came up while re-checking TODO.md items against HEAD. Findings whose text begins "Working-Note status signal:" are instances of the pilot's §2.8 pattern (a Working Note is the false status signal), counted for I.5. The others are defects in a body found on the way. The lane document (`msc/inside-out-2026-10/items-recheck/t1-todo.md`) says which item led to each.

## F1 (finding)
- target: segment:form-composition-closure

Working-Note status signal: the Working Note "Resolved (2026-05-19): $N$-agent scaling of $\varepsilon^\ast$" (line 358), and the derivation-table row at line 185 whose strength cell reads "Resolved … No exponential regime exists", assert three cases. Case (I) (benign linear-Gaussian-stationary: $\varepsilon^\ast = 0$ for all $N$) rests on the two-Kalman closed form and is supported. The re-typing (per-step residue versus accumulation predicate) is argued in `spikes/.integrated/spike-accumulation-type-confound.md`. Case (II), "graph-Laplacian-bounded with no exponential regime under compression (the consensus operator `#deriv-critical-mass-composition` already names)", has no derivation in canon or in the spike: `#deriv-critical-mass-composition` mentions the graph Laplacian only as adjacent literature (Olfati-Saber and Murray 2004, line 204), and the spike's own sentence (§(a)) asserts the bound without deriving it. "Resolved" therefore labels an asserted bound. Either derive case (II) in a segment, or state it at its real tier.

## C1 (check)
- target: segment:form-composition-closure
- act: rederive
- line: derivation
- criterion: Does the per-step strategy closure error $\varepsilon_\Sigma = \mathbb E\big[\lvert(1/(n_i+2) - \eta_c)(\mathbb 1[\cdot] - p_i)\rvert\big]$ of the Beta-Bernoulli purposeful-sub-agent case (Discussion, line 316) "grow without bound" for a fixed macro-gain $\eta_c \gt 0$?
- committed: before
- outcome: broken
- recheck: bound the two factors: $\lvert 1/(n+2) - \eta_c\rvert \le \max(1/2, \eta_c)$ and $\lvert \mathbb 1[\cdot] - p\rvert \le 1$

It does not. Both factors are bounded, so $\varepsilon_\Sigma \le \max(1/2, \eta_c)$ at every step, and as $n_i \to \infty$ it tends to $\eta_c\,\mathbb E\lvert\mathbb 1[\cdot] - p_i\rvert$: non-vanishing, not divergent. The same error was flagged, but not asserted, in `spikes/.integrated/spike-accumulation-type-confound.md` §(c), and never reached the segment. The conclusion that this case gives a genuine $\varepsilon^\ast \gt 0$ also needs restating, which is my inference and not checked further. $\varepsilon^\ast$ is an infimum over admissible macro-dynamics, and the limiting defect $\eta_c\,\mathbb E\lvert\mathbb 1 - p\rvert$ goes to $0$ as $\eta_c \to 0^+$, so the infimum is approached but not attained. What does not shrink is the bridge-lemma ratio: with linear correction $\alpha_c \approx \eta_c \nu_c$, the trajectory bound $\varepsilon_\Sigma \nu_c / \alpha_c \to \mathbb E\lvert\mathbb 1 - p_i\rvert$, independent of $\eta_c$. The obstruction is that no fixed-gain macro makes the defect small *relative to its own correction rate*. Nothing diverges.

## F2 (finding)
- target: segment:form-composition-closure

The Tier-1 bridge-lemma contraction (§"Bridge-lemma contraction in the $H^\top H$-norm", lines 256 to 282) proves $\lVert f_c(X,o) - f_c(X',o)\rVert_{H^\top H} \le \lambda_{\text{eff}}\lVert X - X'\rVert_{H^\top H}$, and the algebra is right. But $\lVert v\rVert_{H^\top H} = \lVert Hv\rVert$ is a norm only when $H$ has full column rank; no hypothesis says so. When $\dim o \lt \dim X$, the update $X^+ = X + \eta\, g(\delta)$ (which carries no process dynamics) leaves the null-space component of the trajectory error uncontracted. A two-line witness: $X \in \mathbb R^2$, $H = [1\ 0]$, $g(\delta) = (k_1\delta, k_2\delta)$; then the update matrix on the error is $\begin{pmatrix}1-k_1 & 0\\ -k_2 & 1\end{pmatrix}$, with eigenvalue $1$, so a closure defect entering the second coordinate accumulates without bound and $\limsup\lVert e_m\rVert \le \varepsilon^\ast\nu_c/\alpha_c$ fails in the full state norm. The Tier-1 roster names "Kalman filters" without qualification. A Kalman filter's error contracts through $(I-KH)A$ under detectability over several steps, which this one-step argument does not use. Repair options: add "$H$ has full column rank" to (C2), or redo the bound with process dynamics and a multi-step observability (detectability) condition. My own derivation, not independently checked.

## F3 (finding)
- target: segment:deriv-adaptive-gain-dynamics

The composed persistence result (§"Composed persistence result", lines 58 to 70) says completing the square on the cross term "requires $c\sqrt{c_v}$ small compared to $\underline\alpha \cdot c\alpha_K$, i.e., (MG-3) timescale separation plus (MG-4) coupling smallness". The comparison is not dimensionally homogeneous, and (MG-3) appears nowhere in the algebra. Redoing the step: $c\sqrt{c_v}\lVert\delta\rVert\lVert\tilde K\rVert \le \tfrac{\underline\alpha}{4}\lVert\delta\rVert^2 + \tfrac{c^2 c_v}{\underline\alpha}\lVert\tilde K\rVert^2$, which is absorbed when $c\,c_v \le \underline\alpha\,\alpha_K/4$, and the free weight $c$ can always be chosen that small. The real constraint comes from staying inside the gain-error ball $\lVert\tilde K\rVert \le r_K$ where (MG-1) and (MG-2) hold. With $\mu = \min(\underline\alpha, \alpha_K)$, the ultimate bound gives $\lVert\tilde K\rVert^2 \lesssim \rho^2/(\underline\alpha\, c\,\mu) + \sigma_{K,0}^2/(\alpha_K \mu)$, which grows as $c \to 0$. Feasibility is then a joint smallness condition, roughly $\rho^2 c_v \lesssim \underline\alpha^2 \alpha_K \mu\, r_K^2$. Under (MG-3), $\mu = \alpha_K$, so making $\alpha_K$ smaller *tightens* the condition. As derived, the result does not use timescale separation, and (MG-3) works against the only place the rates enter. Either the result holds without (MG-3) (then the sub-scope partition should say so), or (MG-3) belongs to a different argument (singular perturbation), which the segment does not give. A secondary point: (MG-4) bounds a conditional second moment, but the displayed $\dot V$ treats $v$ as a deterministic bound. A mean-square argument needs the Itô or variance term. My derivation, not independently checked; the constants are loose.

## F4 (finding)
- target: segment:deriv-observation-ambiguity-bias-bound

Working-Note status signal: the Working Note "Causal-discipline cross-link (2026-05-31)" calls this segment "the landed $\varepsilon(\kappa)$ bound for the causal-discipline scoping rule" and says "the bound already carried the factor-$\kappa$ form". The factor-$\kappa$ form is asserted, not derived (F5). A second Working Note in the same segment ("Class 2 (Partial) bias-bound analog — open derivation") says the $\kappa_{\text{processing}} \in (0,1)$ bound is open. That one is the true status, so the two notes contradict each other. The first note matters because `#der-directed-separation`:113 hangs the typology's "one *earned* directional fact" (less coupling tracks reality strictly better) on "the bound".

## F5 (finding)
- target: segment:deriv-observation-ambiguity-bias-bound

The boxed Track 1 result and the Track 2 result are tagged *[Derived]* and carry $\kappa_{\text{processing}}$ as a multiplicative factor on $I(G;\Omega_\tau \mid e_\tau, M_{\tau^-})$. The step that puts it there (§2 Step 4; §3 Step 3) is a sentence, "$\kappa_{\text{processing}}$ … multiplies the goal-conditional reweighting strength", with no derivation. The body's own Track 2 Step 2, before that sentence, ends at $2\,I$, with no $\kappa$. $\kappa_{\text{processing}}$ is defined in `#der-directed-separation` (line 85) as $I(G_t; M_{\tau^+}\mid e_\tau, M_{\tau^-})/H(G_t\mid e_\tau, M_{\tau^-})$, a normalized information on the *output*, not a reweighting strength. In the segment's coupling model (the goal-conditioned posterior over $\Omega$, pushed forward to $M$), data processing bounds the *full*-coupling displacement by $I(G;\Omega\mid\cdot)$. Nothing derives the interpolation to partial coupling with the factor $\kappa$. A tempered or mixture partial conditioning, for instance, gives a factor set by the tempering, which relates to $\kappa$ only through a further argument. A route that does follow (my derivation, not independently checked): with $M_{\tau^+}$ random given $G$, $\mathbb E_G\,\mathrm{KL}(P_{M^+\mid e,G}\Vert P_{M^+\mid e}) = I(G;M_{\tau^+}\mid e_\tau,M_{\tau^-}) = \kappa_{\text{processing}}\,H(G\mid e_\tau,M_{\tau^-})$ by the definition of $\kappa$. Through the same small-distance Fisher-Rao expansion, that gives $\mathbb E\,d_{FR}^2 \le 2\,\kappa_{\text{processing}}\,H(G\mid e_\tau, M_{\tau^-})(1+o(1))$, a $\kappa$-linear bound for every class, against $H$ rather than $I(G;\Omega\mid\cdot)$. Whether the stated product form also holds (perhaps as a minimum of the two) is the open Class 2 question.

## C2 (check)
- target: segment:deriv-causal-ib-lmi
- act: run
- line: simulation
- criterion: Is the LMI $\mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}(Q_\rho, A, R^2)$, with $\mathcal I_{\min}$ symmetric positive-definite, *necessary* as well as sufficient for a stabilizing steady state with $\lambda_{\max}(\Sigma_\delta) \lt R^2$ (§"LMI survival constraint", lines 57 to 63: "if and only if")?
- committed: before
- outcome: broken
- recheck: iterate $\Sigma \leftarrow \big((A\Sigma A^\top + Q)^{-1} + J\big)^{-1}$ to steady state with $A$ a $90^\circ$ rotation, $Q = 0.01\,I_2$ and rank-one $J = \mathrm{diag}(j, 0)$ for $j \in \{10, 100\}$; compare $A = I_2$

Necessity fails whenever $A$ mixes directions. With $A$ a $90^\circ$ rotation and information in one direction only, $\lambda_{\max}(\Sigma_\infty) = 0.046$ at $j = 10$ and $0.017$ at $j = 100$, so the survival requirement holds for any $R^2$ above those values. Yet no symmetric positive-definite $\mathcal I_{\min}$ satisfies $\mathcal I_{\min} \preceq \mathrm{diag}(j,0)$, since a matrix below a rank-one matrix in the Loewner order is singular. With $A = I_2$ the same $J$ fails (the unobserved direction's variance grows without bound), which is the case the segment's intuition describes. In general the feasible set of information matrices is upward-closed but has a frontier of minimal elements, not a single minimum. The "iff" holds only when that frontier is one point, e.g. when $A$ and $Q_\rho$ are simultaneously diagonal and the observation directions align with them. Consequences to check: the KKT analysis treats the LMI as the exact constraint; and under a mixing $A$, information in a non-drifting direction *can* help survive, because the dynamics carry it into the drifting directions. The blank-wall resolution needs the separable-subspaces hypothesis stated, which the Empirical-signature paragraph (line 132) assumes but the derivation does not name.

## F6 (finding)
- target: segment:hyp-communication-gain

Working-Note status signal: the first Working Note (line 59) states the distributed tempo $\mathcal T_i = \sum_k \nu_i^{(k)}\eta_i^{(k)\ast} + \sum_j \nu_{ji}^{\text{comm}}\eta_{ji}^\ast$ without scope and calls it "the formal basis for #der-team-persistence — teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo". Since ba4bf598 (2026-07-16), `#der-team-persistence` (lines 19, 37) carries the sum only under the cross-channel noise-independence scope of `#deriv-tempo-additivity`, with a signed deviation: correlated (common-source) allies are sub-additive, anti-correlated ones triangulate. The 2026-08-22 impl pass called this note "the refuted linear distributed-tempo sum". "Unscoped" is more exact than "refuted", but either way the note states as basis what the cited body now scopes.

## F7 (finding)
- target: segment:hyp-communication-gain

The communication gain $\eta_{ji}^\ast = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$ cannot represent a *known* adversary. $U_{\text{align},ji}$ is $i$'s *uncertainty* about $j$'s alignment, so certainty that $j$ is misaligned sets $U_{\text{align}} \to 0$ and *raises* the gain toward the full-trust value. The Epistemic Status (line 39) says additivity "is conservative: it correctly drives $\eta_{ji}^\ast$ toward zero when teleological-unity uncertainty is high". That is true of uncertain alignment and false of known misalignment. A known-misaligned source is a *bias* (a mean shift the receiver could correct or refuse), not dispersion, and no variance-only denominator holds it. Repair candidates: a bias term the receiver subtracts (and its estimation cost), or defining $U_{\text{align}}$ as expected squared misalignment, which is large under certain misalignment, rather than as uncertainty about it. Surfaced by the 2026-08-22 impl pass (CHANGELOG 2026-08-22, `impl-unity-communication`), never landed.

## F8 (finding)
- target: segment:def-agent-environment

The Working-Note figure candidate "Lossy-aperture two-panel" (line 78) says "AAT's scope is exactly the region where the aperture is not fully open" and specifies the figure to draw from it (in-scope: aperture partly closed; out-of-scope: fully open). Since the A.1 landing, `#scope-adaptive-system` makes residual uncertainty necessary, not sufficient, for adaptive-scope membership (item (a)); the same gloss at this segment's line 43 is already an open finding. "Exactly" makes line 78 a second carrier of the superseded criterion, and a figure built to its specification would teach it. Found while checking the 29 "AAT's scope" uses for TODO.md:271.
