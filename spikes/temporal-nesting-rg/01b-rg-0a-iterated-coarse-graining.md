# RG-0a (continued): Iterated Coarse-Graining and Parameter Flow

**Status**: derived — but result demands a sharper distinction (structural-RG vs. critical-RG) than the brief originally framed.
**Date**: 2026-05-09
**Depends on**: `01-rg-0a-two-kalman-Kc-extension.md` §5.

The single-step calculation in §2 of the parent file showed $\varepsilon^* \to 0$ under one application of $\Lambda$. The substantive RG question is whether AAT-shape *and* a non-trivial parameter set survive under *iterated* coarse-graining. This file works that out.

---

## 1. The level-1 composite as a Kalman-shaped agent

From §2.4 of the parent file, the optimal symmetric macro-update of a homogeneous Kalman pair (set $\lambda_1 = \lambda_2 = \lambda$ for clarity) is

$$X_{c, m} = \mu^{(1)} X_{c, m-1} + (1 - \mu^{(1)}) O_{c, m}^{\text{(eff)}}$$

with $\mu^{(1)} = \lambda^{K_c}$ as the macro-persistence factor and $O_c^{\text{(eff)}}$ the geometrically-weighted aggregation of the $K_c$-window. Equivalently, the level-1 macro-gain is $K_c^{*(1)} = 1 - \lambda^{K_c}$.

**This is itself a Kalman-style filter on the macro-observation stream.** It is linear-Gaussian, sector-bounded, AAT-shaped. (A1)–(A4) are satisfied at level 1 by construction.

So **the AAT form is preserved exactly under one application of $\Lambda$ in the homogeneous Kalman case**. This is the "fixed-point-preserving" content of the RG framing's first claim.

## 2. Iterating: a level-2 composite of two level-1 composites

Now take two level-1 composites — call them $A$ and $B$ — and form their level-2 composite. Each level-1 composite has its own macro-persistence factor; if the underlying micro-pairs were homogeneous within each composite, then $\mu_A^{(1)} = \lambda_A^{K_c}$ and $\mu_B^{(1)} = \lambda_B^{K_c}$.

Apply the same construction at level 2 with timescale ratio $K_c'$. By symmetry with §2 of the parent file:

$$\mu^{(2)} = \frac{(\mu_A^{(1)})^{K_c'} + (\mu_B^{(1)})^{K_c'}}{2}$$

For the homogeneous case ($\mu_A = \mu_B = \lambda^{K_c}$), this collapses to

$$\mu^{(2)} = \lambda^{K_c K_c'}$$

Iterating $n$ levels (each with its own $K_c^{(i)}$):

$$\mu^{(n)} = \lambda^{\prod_{i=1}^n K_c^{(i)}}$$

*[Derived (homogeneous-iterated-flow)]* The persistence factor under $n$-fold iterated coarse-graining is the original $\lambda$ raised to the product of timescale ratios.

## 3. The parameter flow

Treat the dimensionless parameter $\lambda \in (0, 1)$ as the AAT agent's "running coupling." The flow under one coarse-graining step at ratio $K_c$:

$$\lambda \longmapsto \lambda^{K_c}$$

Fixed points: $\lambda^* = \lambda^{*K_c}$. Solutions:
- $\lambda^* = 0$ (memoryless agent: every step overwrites with the latest observation)
- $\lambda^* = 1$ (frozen agent: never updates)

For $K_c > 1$ and any $\lambda \in (0, 1)$, $\lambda^{K_c} < \lambda$ — the flow is monotonically decreasing. Iterating drives $\lambda$ toward $0$.

*[Derived (homogeneous-flow-attractor)]* The unique attracting fixed point of the iterated $K_c$-flow on $\lambda \in (0, 1)$ is $\lambda^* = 0$ — the memoryless / saturated-gain limit.

## 4. The honest reading: structural-RG, not critical-RG

This is a genuinely important refinement of the brief's framing. Two things are simultaneously true:

(a) **The AAT form is preserved at every level.** Level-1 is Kalman-shaped, level-2 is Kalman-shaped, every level is Kalman-shaped. (A1)–(A4) hold by construction at every scale. This is structural-RG fixed-point: the *shape* survives.

(b) **The parameter flow has only a degenerate attractor.** The "running" $\lambda$ flows to $0$ under iterated coarse-graining. There is no non-trivial scale-invariant fixed point — no AAT-Kalman that *reproduces itself* under $K_c > 1$ coarse-graining with a finite, non-degenerate $\lambda$.

In physics RG, (a) is the form-preservation that makes RG well-defined, and (b) is the parameter flow whose fixed points are critical points (scale-invariant systems at phase transitions). What the linear-Kalman case shows is: AAT has the structural fixed point of (a), but there are no critical-point fixed points in the (b) sense — at least within this linear-Gaussian sub-class.

## 5. Is this a problem for the RG framing?

Not necessarily, but it sharpens the claim. Three readings:

### Reading 1: The framing's strong form fails

If "AAT as RG" was meant to claim AAT admits non-trivial scale-invariant fixed points (analogous to Wilson-Fisher critical points in physics), this reading is unsupported in the linear-Kalman case. The parameter flow has only the degenerate $\lambda^* = 0$ attractor.

### Reading 2: The framing's structural form holds

If "AAT as RG" was meant to claim AAT's *form* is preserved under coarse-graining — that (A1)–(A4) are form-preservation requirements expressing scale-invariance of the AAT shape — this reading holds. Every level of the iteration is AAT-shaped. The persistence template applies at every level *because of this preserved form*.

This is the Schwab et al. 2017 (PNAS) flavor of RG-deep-learning correspondence: structural mapping, not critical-point claim. It's also the flavor of categorical-RG approaches that emphasize functorial scale-invariance.

### Reading 3: The framing may have non-trivial fixed points outside linear-Kalman

The linear-Kalman setup has only one running parameter ($\lambda$) and one degenerate flow direction. Richer agent classes — strategy-DAG agents with both $M_t$ and $G_t$ dynamics, agents with multiple update channels at different rates, agents whose update rule is itself state-dependent — may admit non-trivial flow structure.

For example: a strategy-DAG agent with strategic-tempo $\mathcal{T}_\Sigma$ and epistemic-tempo $\mathcal{T}_M$ has a *ratio* $\mathcal{T}_\Sigma / \mathcal{T}_M$ that may flow non-trivially. Critical agents — those whose strategic and epistemic flows balance — would be candidates for non-trivial fixed points. This is speculative and outside the present test.

## 6. Implications for the RG-0 verdict

The brief's first-cut hypothesis (relevant/irrelevant operator separation, classical-RG-style critical points) is **not supported** in the linear-Kalman case. Two possible conclusions:

- **Drop the strong RG framing.** Replace with the weaker but still useful "AAT as form-preserving structure across scales." This is essentially what `#post-composition-consistency` already says; the value-add is naming it explicitly and connecting it to the persistence template's "applies at every level."
- **Preserve the framing as a research direction.** Test richer agent classes (strategy-DAG, multi-channel) for non-trivial flow structure. The linear-Kalman case is too simple to expose RG-relevant operators if they exist.

I lean toward the first — the structural framing is strong and useful even without critical points, and overclaiming RG content that we haven't demonstrated would violate the project's epistemic discipline. The richer-agent-class question becomes a separate research thread, *not* a load-bearing claim about AAT-as-RG.

## 7. What gets built (downstream of this verdict)

If we accept Reading 2 as the conservative-but-real result:

- **RG-1 (revised)**: State (A1)–(A4) explicitly as form-preservation conditions. New segment / appendix in `#form-composition-closure` titled something like "Composition-closure as scale-invariance of the AAT form." Cite Schwab et al. 2017 for the structural-RG-correspondence concept. **Drop language about "fixed points" and "RG flow"; replace with "form preservation under coarse-graining" and "parameter flow."**
- **RG-2 (preserved)**: (O, Σ) recursion as another instance of the same form-preservation principle, applied to the strategy layer rather than the composition layer. The strategy DAG decomposes into sub-strategies, each of which is itself a strategy DAG — same form, smaller scale. This is genuinely a self-similarity claim and is independent of whether the parameter flow has critical points.
- **RG-3 (weakened)**: Directed-separation classes as form-preservation classes — Class 1 preserves $M \perp O$ at macro, Class 3 doesn't. This is honest and useful. The "fixed-point types" language was overreach; the right language is "agent classes for which AAT-shape preservation under $\Lambda$ does or does not hold."
- **RG-4 (drop)**: The strong-form RG flow of the persistence condition does not get the critical-point interpretation. The N-level template-stability result (original Spike B) remains valid as nested template instantiation; it does not require RG framing. Promote `#sketch-multi-timescale-stability` via the template-stacking argument, not via RG.

## 8. Self-review

**Tier**: Derived (the iterated flow $\lambda \to \lambda^{K_c}$ in the homogeneous-Kalman case is exact; the absence of non-trivial fixed points in this case is exact).

**Honest disclosure**: I have *not* tested richer agent classes. The linear-Kalman case is the simplest possible test, and its negative result for critical-RG fixed points doesn't preclude their existence elsewhere. But making strong claims about "AAT as RG" based only on form-preservation is honest scope; making strong claims about non-trivial scale-invariance would be overclaim.

**What I would still want before fully closing this thread**:
1. The (O, Σ) recursion check (RG-0c) — is the fractal structure on the strategy side genuine?
2. Schwab et al. 2017 + IB-as-RG prior art — to know whether the structural framing is novel or already done. (Pending from sub-agent.)
3. A check that the heterogeneous iterated case doesn't hide a non-trivial fixed point. Quick sketch: if $\mu_A \neq \mu_B$, then $\mu^{(2)} = (\mu_A^{K_c'} + \mu_B^{K_c'})/2$, which is bounded below by $\min(\mu_A, \mu_B)^{K_c'}$ and above by $\max(\mu_A, \mu_B)^{K_c'}$. Iterating still drives toward $\lambda \to 0$. Heterogeneity at one level dies out at the next. So no, no hidden fixed points.

---

This refines the verdict in `99-verdict.md`: the **structural** RG framing holds and is useful; the **critical-point** RG framing fails on the linear-Kalman case and is not yet warranted by any positive test.
