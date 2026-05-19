# Connection 1 §3, spiked: the energy bound makes the Effects Spiral a theorem by making its unformalized term *unnecessary*

**Thread.** `01` §3 hypothesized the energy budget is the missing coupling variable that closes `#der-adversarial-destabilization`'s discussion-grade Effects-Spiral corollary. Sharp question taken in: does the energy budget give a *shortcut around* the joint-Jacobian equilibrium problem AAT defers, or does it *reduce to* that problem? Derivation attempted at full strength first (strengthen-before-soften), three completion states admitted.

**Result, one line.** It is a shortcut — but not the one the hypothesis guessed. The energy bound does **not** formalize the segment's $\gamma_A(\lVert\delta_B\rVert)$ leg; it makes that leg **unnecessary**. A hard-budget target destabilizes in finite time via *self-depletion* against even a **constant-effectiveness** adversary, and the mechanism is the **decaying-$\alpha$ instantiation of `#result-sector-persistence-template`** — existing exact machinery (same slot as `#schema-strategy-persistence`'s experience-decay), not the deferred symmetric joint-Jacobian analysis. Tier: **conditional** on two introduced resource axioms AAT does not currently carry; the reduction itself is exact-flavored given them.

## 1. The honest precondition: AAT has no resource structure

`#def-strategy-dimension` Open item: *"Resource budget: strategy evaluation requires knowing what paths cost, but costs are currently unmodeled … For resource-constrained agents (military units, development teams), per-action costs and capacity constraints would need to enter the formalism. Open."* This spike therefore *introduces* minimal resource structure; everything below is conditional on it and is a **candidate resource-structure extension**, not a free consequence of existing AAT. Stated up front so the tier is not over-read.

**Two introduced axioms (motivated, not derived):**

- **(A-cost) Correction cost rises with mismatch.** A degrading world-model actuates less efficiently — effort is spent partly in wrong directions, paid for and wasted. Minimal form: resource drain per unit correction effort is $c(\lVert\delta_B\rVert)$ with $c$ increasing, e.g. $c(\lVert\delta\rVert)=c_0(1+\beta\lVert\delta\rVert)$.
- **(A-gate) Correction capacity is resource-gated.** Tempo $\mathcal T_B$ (the $\alpha_B$ of the canonical persistence instantiation, `#def-adaptive-tempo`: $\mathcal T=\sum_k\nu^{(k)}\eta^{(k)\ast}$) throttles when resource is scarce — fewer sensor sweeps, slower control cycle, fewer remaining episode steps. Minimal form: $\alpha_B(E)=\alpha_B^{\max}\,g(E)$, $g$ increasing, $g(0)=0$, $g(\infty)=1$.

## 2. The coupled dynamics

State: target mismatch $\delta_B$ and resource $E\geq 0$.

$$\dot\delta_B = -\alpha_B(E)\,\delta_B + w_B(t), \qquad \lVert w_B\rVert \leq \rho_{B,\text{base}} + \gamma_A\mathcal T_A$$
$$\dot E = -\,c(\lVert\delta_B\rVert)\,\phi\big(\alpha_B(E),\delta_B\big) + r$$

$\phi$ = correction effort (increasing in rate $\alpha_B$ and in the mismatch corrected); $r$ = replenishment ($r=0$ is Φ's hard-budget combat episode: battery / torque-integral / episode-length — a finite pool that only depletes).

## 3. The two regimes, and where the content is

**Budget-sufficient regime** ($E_0$ large vs episode length × integrated cost): $E_t$ stays high, $\alpha_B(E_t)\approx\alpha_B^{\max}$ constant — the **constant-$\alpha$ template applies unchanged**; `#der-adversarial-destabilization`'s existing static result is the whole story; the energy bound buys nothing. (This is the honest boundary `01` §3 asserted: the unbounded regime has no loop closure.)

**Budget-scarce regime ($r=0$, ongoing correction).** $\dot E\leq 0$, so $E_t$ is monotone non-increasing; with correction effort bounded below while mismatch persists, $E_t\to 0$ in finite time. Then $\alpha_B(E_t)$ is a **time-varying, monotonically-decaying sector parameter, driven down by the agent's own correction expenditure, accelerated by mismatch through $c(\lVert\delta_B\rVert)$.** This is exactly the structure `#result-sector-persistence-template` Epistemic Status flags as *"Time-varying parameters … require additional machinery,"* and the machinery already exists: `#schema-strategy-persistence` is AAT's canonical decaying-$\alpha$ instantiation (there $\alpha_\Sigma=1/(n+1)$ decays with experience; persistence requires the decay be counteracted at rate $\gt\rho_\Sigma/R_\Sigma$). The energy-bounded spiral is the **same template slot with budget-depletion in the role experience-accumulation plays there.**

## 4. The derived spiral (conditional on §1 axioms)

Persistence in-episode requires $\alpha_B(E_t)\gt\rho_B^{\text{eff}}/R_B$ throughout, with $\rho_B^{\text{eff}}=\rho_{B,\text{base}}+\gamma_A\mathcal T_A$. Define the **critical budget** $E_{\text{crit}}$ by $\alpha_B(E_{\text{crit}})=\rho_B^{\text{eff}}/R_B$, and the destabilization **hitting time** $\tau=\inf\{t: E_t=E_{\text{crit}}\}$. Then:

> **Self-depletion spiral (conditional-derived).** With $r=0$ and ongoing correction, $E_t\downarrow$ monotonically, so $\tau\lt\infty$ is **certain** for any finite $E_0$ (the static persistence inequality holding at $t=0$ does not prevent it — $\alpha_B(E)\to\alpha_B(0)=0\lt\rho_B^{\text{eff}}/R_B$). The positive feedback
> $$\lVert\delta_B\rVert\uparrow \;\Rightarrow\; c(\lVert\delta_B\rVert)\uparrow \;\Rightarrow\; \dot E \text{ more negative} \;\Rightarrow\; \alpha_B(E)\downarrow \;\Rightarrow\; \big(\alpha_B R_B-\rho_B^{\text{eff}}\big)\downarrow \;\Rightarrow\; \lVert\delta_B\rVert\uparrow$$
> brings $\tau$ **forward**: a transient noise-burst excursion in $\delta_B$ accelerates its own future destabilization. Adversarial survival becomes a **budget-vs-episode-length race** — the agent persists iff the episode ends before $\tau$.

Two consequences sharper than the hypothesis predicted:

1. **The unformalized term is eliminated, not formalized.** `#der-adversarial-destabilization`'s spiral is discussion-grade because $\gamma_A(\lVert\delta_B\rVert)$ — the *adversary's* coupling growing as the target flails — is unspecified. The self-depletion spiral closes through $\alpha_B$ *decaying*, with $\gamma_A$ held **constant**. The spiral's substantive content (collapse invisible to the static threshold: a system that *would persist forever at full budget* still dies from a transient excursion) is captured **without ever needing $\gamma_A$ to grow.** The energy bound makes the segment's open leg unnecessary in the resource-bounded regime rather than closing it.
2. **It reduces to existing exact machinery, not to the deferred hard problem.** The route is `#result-sector-persistence-template` (status `exact`) under a decaying $\alpha$, the `#schema-strategy-persistence` precedent supplying the time-varying-$\alpha$ treatment. It is **explicitly orthogonal to** the deferred *symmetric joint-Jacobian / mutual-coupling* equilibrium problem (`#der-adversarial-destabilization` Working Notes → `#deriv-strategic-composition`): that problem is about both agents' mismatch co-evolving and the $\gamma_A(\lVert\delta\rVert)$ leg specifically; this result is single-agent-with-resource and does not touch it. **Guardrail: the energy bound does not crack the joint-Jacobian problem; do not read it as having done so.**

## 5. Tiers (honest)

| Sub-claim | Tier | Basis |
|---|---|---|
| Budget-sufficient regime → constant-$\alpha$ template, no new content | **exact (inherited)** | `#result-sector-persistence-template` (status exact), unchanged |
| Energy-bounded spiral = decaying-$\alpha$ instantiation of the template (the *reduction*) | **exact-flavored, conditional on §1 axioms** | template's time-varying-$\alpha$ slot + `#schema-strategy-persistence` precedent |
| Finite-time certain destabilization in $r=0$ + spiral brings $\tau$ forward | **conditional-derived** | Lyapunov + monotone-budget argument under (A-cost),(A-gate) |
| $\gamma_A$ need not grow; segment's open leg made unnecessary | **conditional-derived** (corollary of above) | constant-$\gamma_A$ suffices in the construction |
| Orthogonal to (does not resolve) the deferred joint-Jacobian problem | **verified relationship** | comparison of which term carries the feedback ($\alpha_B$ vs $\gamma_A$) |
| (A-cost), (A-gate) themselves | **introduced axioms, not derived** | AAT has no resource structure (`#def-strategy-dimension` open) |

## 6. Honest edges / open

- **(E1)** The two resource axioms are the load-bearing assumptions and are *introduced*. The result's real status is "conditional resource-structure extension"; it is a candidate for the acknowledged-open resource gap, not a closure of it from existing machinery.
- **(E2)** Replenishment $r\gt 0$ (regenerative budget) is **not** done — it is the genuine time-varying-$\alpha$ ODE in full and may be quasi-stationary-distribution / absorbing-barrier-flavored (cf. the continuity-persistence spike's open second no-go). Flagged, not attempted.
- **(E3)** $\phi$ and the $g,c$ functional forms are minimal stand-ins; the *qualitative* spiral is form-robust (monotonicity is all that is used), the *rate* ($\tau$ as a function of $E_0$, $\beta$, episode length) is form-specific and not computed.
- Documented dead-end: do not attempt to derive (A-cost)/(A-gate) from current AAT — there is no resource state in the formalism to derive them from; introducing the resource state *is* the move, and it is a definitional extension requiring Joseph's call.

## 7. Landed — exploratory branch (Joseph elected the resource axis 2026-05-19)

Strengthen-before-soften outcome: `#der-adversarial-destabilization`'s Effects-Spiral corollary moved from *discussion-grade* to *conditional-derived* — **in a scoped regime, by a reduction to existing exact machinery plus two named resource posits** — and the cleaner statement (self-depletion; $\gamma_A$ constant; budget-vs-engagement race) is *stronger and simpler* than the original $\gamma_A(\lVert\delta\rVert)$ conjecture. **Landed** as an exploratory off-spine branch (Joseph elected to open the resource axis, 2026-05-19):

- `#form-resource-budget` — `type: formulation, status: conditional` — the minimal $(\mathcal B_t, c, \psi)$ resource structure with posits (A-cost)/(A-gate), addressing `#def-strategy-dimension`'s open resource gap.
- `#der-resource-bounded-destabilization` — `type: derived, status: conditional` — the §4 self-depletion result + §5 tiers as the decaying-$\alpha$ instantiation of `#result-sector-persistence-template`, structurally paralleling `#schema-strategy-persistence`.

Both registered in `01-aat-core/OUTLINE.md` Appendix A (Stage `exploratory`); NOTATION.md carries $\mathcal B_t$ under the exploratory-branch section; no spine segment depends on either (off-spine by construction). Per math-lives-in-segments the math now lives in the segments; this spike is the reasoning trail only. Open follow-ons (regenerative $r_{\mathcal B}\gt 0$ regime; closed-form $\tau$) are in `#der-resource-bounded-destabilization` Working Notes.
