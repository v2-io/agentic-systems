# Spike: Composition Bridge Lemma — 2-Agent Cases

**Status**: Exploratory derivation — attempting to close the composition-closure → trajectory-error gap for the simplest cases.
**Date**: 2026-03-14
**Motivation**: All three independent reviews flagged the missing bridge lemma as a HIGH priority. The composition-closure criterion defines ε* but doesn't prove that bounded ε* implies bounded trajectory error. Without this, Section III's results are conditional on an unresolved step.

**Strategy**: Start with the simplest case (orthogonal), extend to unidirectional coupling (which reuses the adversarial-destabilization machinery), then attempt the bidirectional case. Each case should produce a concrete bound.

---

## Case 1: Orthogonal Agents (Independent Channels, Non-Overlapping Actions)

### Setup

Two agents $A$ and $B$ with:
- Independent observation channels: $o_A \perp o_B$
- Non-overlapping action spaces: $\mathcal{A}_A \cap \mathcal{A}_B = \emptyset$
- Shared environment but no mutual disturbance: $\rho_A$ and $\rho_B$ are independent of each other's actions

Each satisfies the sector condition individually:

$$\delta_A^T F_A \geq \alpha_A \Vert\delta_A\Vert^2 \quad \text{for } \Vert\delta_A\Vert \leq R_A$$

$$\delta_B^T F_B \geq \alpha_B \Vert\delta_B\Vert^2 \quad \text{for } \Vert\delta_B\Vert \leq R_B$$

### The composite agent

No projection needed — the composite state is the full pair:

$$X_c = (M_A, M_B, G_A, G_B)$$

$$\delta_c = (\delta_A, \delta_B) \in \mathbb{R}^{n_A + n_B}$$

### Joint Lyapunov function

$$V(\delta_c) = \frac{1}{2}\Vert\delta_A\Vert^2 + \frac{1}{2}\Vert\delta_B\Vert^2 = \frac{1}{2}\Vert\delta_c\Vert^2$$

Time derivative (using independence — no cross-coupling terms):

$$\dot{V} = \delta_A^T(-F_A + w_A) + \delta_B^T(-F_B + w_B)$$

$$\leq -\alpha_A\Vert\delta_A\Vert^2 + \rho_A\Vert\delta_A\Vert - \alpha_B\Vert\delta_B\Vert^2 + \rho_B\Vert\delta_B\Vert$$

### Persistence condition

$\dot{V} < 0$ when:
- $\Vert\delta_A\Vert > \rho_A / \alpha_A$ (Agent A's individual persistence), AND
- $\Vert\delta_B\Vert > \rho_B / \alpha_B$ (Agent B's individual persistence)

More precisely: $\dot{V} < 0$ everywhere on the boundary of the set $\{(\delta_A, \delta_B) : \Vert\delta_A\Vert \leq R_A^* \text{ and } \Vert\delta_B\Vert \leq R_B^*\}$ where $R_i^* = \rho_i / \alpha_i$.

### Result (Case 1)

*[Derived (trivially from independence + individual persistence)]*

**If both agents persist individually ($\alpha_A > \rho_A/R_A$ and $\alpha_B > \rho_B/R_B$), the orthogonal composite persists with:**

$$\Vert\delta_c\Vert \leq \sqrt{(R_A^*)^2 + (R_B^*)^2} = \sqrt{\left(\frac{\rho_A}{\alpha_A}\right)^2 + \left(\frac{\rho_B}{\alpha_B}\right)^2}$$

The composite tempo: $\mathcal{T}_c = \mathcal{T}_A + \mathcal{T}_B$ (independent channels, tempos add).

The closure defect: $\varepsilon^* = 0$ (no projection, no information loss).

The coordination overhead: $C_{\text{coord}} = 0$ (no coordination needed for non-interacting agents).

**This is trivial but establishes the baseline**: orthogonal composition preserves persistence and adds tempos. The interesting cases are below. $\square$

---

## Case 2: Unidirectional Coupling (A Affects B's Environment)

### Setup

Same as Case 1 except: Agent $A$'s actions contribute to Agent $B$'s disturbance rate:

$$\rho_B = \rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A$$

where $\gamma_{AB} \in \mathbb{R}$ is the coupling effectiveness:
- $\gamma_{AB} > 0$: adversarial — A's actions disturb B (the case analyzed in #adversarial-destabilization)
- $\gamma_{AB} < 0$: cooperative — A's actions reduce B's disturbance (the composition case)
- $\gamma_{AB} = 0$: independent — reduces to Case 1

Agent $A$ is unaffected by $B$: $\rho_A = \rho_{A,\text{base}}$.

### Joint Lyapunov analysis

$$\dot{V} = \delta_A^T(-F_A + w_A) + \delta_B^T(-F_B + w_B + w_{AB})$$

where $w_{AB}$ is the coupling disturbance (from A's actions).

$$\leq -\alpha_A\Vert\delta_A\Vert^2 + \rho_A\Vert\delta_A\Vert - \alpha_B\Vert\delta_B\Vert^2 + (\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A)\Vert\delta_B\Vert$$

### Persistence condition for the composite

Agent $A$ persists independently: $\alpha_A > \rho_A / R_A$ (unchanged).

Agent $B$ persists under coupled disturbance iff:

$$\alpha_B > \frac{\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A}{R_B}$$

### Result (Case 2)

*[Derived (from sector-condition-stability + coupling model — this is the adversarial-destabilization result with the sign of γ generalized)]*

**Cooperative subcase ($\gamma_{AB} < 0$):** A's actions *reduce* B's effective disturbance. B's persistence condition is *easier* to satisfy than in isolation. The composite persists more easily than the individuals alone:

$$R_B^* = \frac{\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A}{\alpha_B} < \frac{\rho_{B,\text{base}}}{\alpha_B}$$

This is the formal content of "teams persist where individuals can't" for the simplest case: if A's actions reduce B's effective disturbance enough, B can persist even when $\alpha_B < \rho_{B,\text{base}} / R_B$ (below individual persistence threshold).

**Adversarial subcase ($\gamma_{AB} > 0$):** A's actions *increase* B's disturbance. This is exactly #adversarial-destabilization. B diverges when $\gamma_{AB} \cdot \mathcal{T}_A > \Delta\rho_B^*$.

**Composite tempo:**

$$\mathcal{T}_c = \mathcal{T}_A + \mathcal{T}_B - C_{\text{coord}}$$

where $C_{\text{coord}} \geq 0$ accounts for time/tempo spent on coordination. For the cooperative case, coordination overhead must be less than the benefit from reduced disturbance:

$$C_{\text{coord}} < \lvert\gamma_{AB}\rvert \cdot \mathcal{T}_A / \alpha_B$$

(i.e., the tempo cost of coordinating must be less than the persistence margin gained from cooperation).

**Composite mismatch bound:**

$$\Vert\delta_c\Vert \leq \sqrt{(R_A^*)^2 + (R_{B,\text{coupled}}^*)^2}$$

where $R_{B,\text{coupled}}^* = (\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A) / \alpha_B$. $\square$

---

## Case 3: Bidirectional Coupling (Both Affect Each Other)

### Setup

Full bidirectional coupling:

$$\rho_A = \rho_{A,\text{base}} + \gamma_{BA} \cdot \mathcal{T}_B$$

$$\rho_B = \rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A$$

### Joint Lyapunov analysis

$$\dot{V} \leq -\alpha_A\Vert\delta_A\Vert^2 + (\rho_{A,\text{base}} + \gamma_{BA} \cdot \mathcal{T}_B)\Vert\delta_A\Vert - \alpha_B\Vert\delta_B\Vert^2 + (\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A)\Vert\delta_B\Vert$$

This is the sum of two individual persistence analyses, each with modified disturbance rates. The composite persists iff BOTH modified persistence conditions hold simultaneously:

$$\alpha_A > \frac{\rho_{A,\text{base}} + \gamma_{BA} \cdot \mathcal{T}_B}{R_A}$$

$$\alpha_B > \frac{\rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A}{R_B}$$

### The cooperative-cooperative case (both γ < 0)

When $\gamma_{AB} < 0$ AND $\gamma_{BA} < 0$: each agent's actions reduce the other's disturbance. Both persistence conditions are easier to satisfy. The composite is strictly more robust than either individual.

This is the formal justification for team composition: mutual cooperation reduces effective disturbance on both sides, widening the persistence margin for each.

### The mixed case ($\gamma_{AB} < 0$, $\gamma_{BA} > 0$ or vice versa)

One agent helps the other while being harmed in return — an asymmetric dependency. The composite persists iff the harmed agent's modified persistence condition still holds. This formalizes "asymmetric teams" where one member bears a disproportionate coordination burden.

### The bridge to composition closure

For the bidirectional case with a projection (the composite's macro-model $M_c$ is a lossy compression of $(M_A, M_B)$):

**Theorem sketch (Bridge Lemma — 2 agents):**

If agents $A$ and $B$ satisfy:
1. Individual persistence: $\alpha_i > \rho_i / R_i$ for each $i$
2. Coupling is bounded: $\lvert\gamma_{AB}\rvert \cdot \mathcal{T}_A + \lvert\gamma_{BA}\rvert \cdot \mathcal{T}_B < \min(\Delta\rho_A^*, \Delta\rho_B^*)$
3. The projection $\Lambda_x: (M_A, M_B) \to M_c$ is $L$-Lipschitz
4. The closure defect $\varepsilon^* \leq \varepsilon_{\max}$

Then the composite mismatch is bounded:

$$\Vert\delta_c\Vert \leq L \cdot \sqrt{(R_{A,\text{coupled}}^*)^2 + (R_{B,\text{coupled}}^*)^2} + \varepsilon^*$$

and the composite persists as an AAD agent.

**Condition 2 is the key content:** the total coupling energy must not exhaust either agent's adaptive reserve. This is the bridge between "bounded component errors" and "bounded trajectory errors" — it works because the Lyapunov analysis guarantees that individual mismatch stays bounded (condition 1), the coupling doesn't push either agent past its boundary (condition 2), and the projection doesn't amplify errors unboundedly (condition 3).

---

## What This Establishes

1. **The orthogonal case** is trivial: individual persistence implies composite persistence, tempos add, closure defect is zero.

2. **The unidirectional cooperative case** gives the formal mechanism for "teams persist where individuals can't" — cooperative coupling reduces effective disturbance, widening the persistence margin.

3. **The bidirectional case** produces a concrete persistence condition for the composite that depends on the coupling structure. The bridge lemma has explicit conditions.

4. **The adversarial case** is already covered by #adversarial-destabilization — this spike extends the same machinery to cooperative and mixed coupling.

## What Remains Open

- **The Lipschitz condition on the projection** (condition 3) is assumed, not derived. For specific projection operators (weighted average, information-bottleneck compression), the Lipschitz constant should be computable. Whether natural projections satisfy reasonable Lipschitz bounds is domain-dependent.

- **The n-agent case** should follow by induction (any n-agent system decomposes into nested 2-agent compositions), but the coupling structure becomes a matrix and the conditions become spectral conditions on the coupling matrix. Whether the 2-agent result extends cleanly or degrades with n is an open question.

- **The steady-state coupling model** ($\rho_B = \rho_{B,\text{base}} + \gamma_{AB} \cdot \mathcal{T}_A$) treats tempo as exogenous. A fully dynamic model where A's mismatch state affects B's disturbance in real time (and vice versa) would be the joint Lyapunov analysis mentioned in #adversarial-destabilization's Working Notes. The steady-state analysis gives the persistence boundary; the dynamic analysis would give the transient behavior.

- **The γ coefficients** are assumed known. In practice, estimating coupling strength between agents is itself an estimation problem. For software teams, coupling is estimable from the dependency graph (#system-coupling). For military units, it's estimated from doctrine and intelligence. For AI agent compositions, it could be measured from interaction logs.

---

## Assessment

The 2-agent cases are largely straightforward applications of the existing Lyapunov machinery. The orthogonal case is trivial. The unidirectional case is the adversarial-destabilization result with a sign change. The bidirectional case requires simultaneous satisfaction of two modified persistence conditions.

The bridge lemma (Theorem sketch in Case 3) is plausible and the conditions are concrete, but the Lipschitz condition on the projection is the genuine assumption that needs attention. For the "keep everything" projection (no information loss), L = 1 and the lemma is just the bidirectional persistence condition. For lossy projections, L and ε* are load-bearing.

**Confidence:** Case 1 is proved (trivial). Case 2 is proved (sign change of existing result). Case 3's bridge lemma is a sketch — the Lyapunov analysis holds, but the projection step needs formalization. The conditions are concrete enough to be checked in specific domains.

**Recommendation:** Cases 1 and 2 are ready for promotion to src/ as part of a strengthened #composition-closure or a new #composition-bridge-2agent segment. Case 3's bridge lemma should remain sketch-level until the projection conditions are tightened.
