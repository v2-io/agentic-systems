---
slug: der-resource-bounded-destabilization
type: derived
status: conditional
depends:
  - form-resource-budget
  - result-sector-persistence-template
  - der-adversarial-destabilization
  - schema-strategy-persistence
stage: draft
---

# Derived: Resource-Bounded Destabilization

A hard-budget agent self-depletes to certain finite-time destabilization against even a *constant*-effectiveness adversary — closing #der-adversarial-destabilization's Effects-Spiral not by formalizing its open coupling term but by making that term unnecessary, via the decaying-$\alpha$ instantiation of #result-sector-persistence-template.

## Formal Expression

#der-adversarial-destabilization's Effects-Spiral corollary ($\lVert\delta_B\rVert\uparrow \Rightarrow$ erratic action $\Rightarrow \gamma_A\uparrow \Rightarrow \rho_B\uparrow \Rightarrow \lVert\delta_B\rVert\uparrow$) is *discussion-grade* there because the link "degrading model $\Rightarrow$ stronger adversary coupling" requires specifying how model degradation feeds back into the dynamics, which that segment's machinery does not carry. The resource-budget formulation ( #form-resource-budget) supplies that feedback through a different and cleaner channel — the agent's *own* correction rate, not the adversary's coupling.

### Setup: the resource-coupled adversarial instantiation

Instantiate #result-sector-persistence-template with the target agent $B$'s mismatch as state variable, $\xi=\delta_B$, exactly as #der-adversarial-destabilization does, but with the sector parameter made resource-gated per #form-resource-budget (A-gate):

$$\frac{d\delta_B}{dt}=-\,\alpha_B(\mathcal{B})\,\delta_B+w_B(t),\qquad \lVert w_B(t)\rVert\leq\rho_B^{\text{eff}}=\rho_{B,\text{base}}+\gamma_A\mathcal{T}_A,$$
$$\frac{d\mathcal{B}}{dt}=-\,c\big(\lVert\delta_B\rVert\big)+r_{\mathcal{B}},\qquad \alpha_B(\mathcal{B})=\alpha_B^{\max}\,\psi(\mathcal{B}),$$

with $\rho_B^{\text{eff}}$ the coupling-amplified disturbance of #der-adversarial-destabilization (treated there, and here, with $\gamma_A,\mathcal{T}_A$ exogenous) and $c,\psi$ as posited in #form-resource-budget (A-cost),(A-gate). The novelty is the *coupled pair*: $\delta_B$ and $\mathcal{B}$ co-evolve, with model quality draining the budget and the budget gating correction.

### Regime split

*[Derived (resource-regime-split, from form-resource-budget + sector-persistence-template)]*

**Budget-sufficient regime.** If $\mathcal{B}_t$ stays large enough that $\psi(\mathcal{B}_t)\approx 1$ over the engagement (the pool is effectively infinite relative to the integrated cost), then $\alpha_B(\mathcal{B}_t)\approx\alpha_B^{\max}$ is constant and the system *is* #der-adversarial-destabilization's constant-$\alpha$ instantiation, unchanged. The resource structure adds nothing here. This is the honest boundary: the resource-blind special case ($\psi\equiv 1$) is exactly today's machinery, and it is correct there.

**Budget-scarce hard regime ($r_{\mathcal{B}}=0$).** With no replenishment, $d\mathcal{B}/dt=-c(\lVert\delta_B\rVert)\leq -c(0)\lt 0$ whenever correction runs, so $\mathcal{B}_t$ is strictly decreasing and reaches any level in finite time. Then $\alpha_B(\mathcal{B}_t)$ is a **time-varying, monotonically-decaying** sector parameter — exactly the structure #result-sector-persistence-template's Epistemic Status flags as requiring additional machinery, and the structure #schema-strategy-persistence already instantiates (there $\alpha_\Sigma=1/(n+1)$ decays with experience; persistence then requires the decay be counteracted faster than $\rho_\Sigma/R_\Sigma$). The resource-bounded case is the *same template slot* with budget-depletion in the role experience-accumulation plays for strategy persistence.

### The result

*[Derived (Conditional on A-cost, A-gate; hard regime $r_{\mathcal{B}}=0$)]*

Define the **critical budget** $\mathcal{B}_{\text{crit}}$ by the persistence boundary of #result-sector-persistence-template (Model D) at the coupling-amplified disturbance:

$$\alpha_B(\mathcal{B}_{\text{crit}})=\frac{\rho_B^{\text{eff}}}{R_B}\qquad\Longleftrightarrow\qquad \psi(\mathcal{B}_{\text{crit}})=\frac{\rho_B^{\text{eff}}}{\alpha_B^{\max}R_B},$$

and the destabilization **hitting time** $\tau=\inf\{t:\mathcal{B}_t=\mathcal{B}_{\text{crit}}\}$. Then, in the hard regime with correction ongoing:

1. **Certain finite-time destabilization.** $\mathcal{B}_t\downarrow$ strictly, so $\tau\lt\infty$ for any finite $\mathcal{B}_0$. Because $\psi(0)=0$, once $\mathcal{B}_t\lt\mathcal{B}_{\text{crit}}$ the persistence condition $\alpha_B(\mathcal{B}_t)\gt\rho_B^{\text{eff}}/R_B$ fails and #der-adversarial-destabilization's destabilization threshold is crossed. **The static persistence inequality holding at $t=0$ does not prevent this** — an agent that would persist forever at full budget ($\alpha_B^{\max}R_B\gt\rho_B^{\text{eff}}$) still destabilizes once the fuel drains the rate below threshold.

2. **The spiral, derived.** Substituting (A-cost), a mismatch excursion accelerates its own destabilization:
$$\lVert\delta_B\rVert\uparrow\;\Rightarrow\;c(\lVert\delta_B\rVert)\uparrow\;\Rightarrow\;\dot{\mathcal{B}}\ \text{more negative}\;\Rightarrow\;\alpha_B(\mathcal{B})\downarrow\;\Rightarrow\;\big(\alpha_B R_B-\rho_B^{\text{eff}}\big)\downarrow\;\Rightarrow\;\lVert\delta_B\rVert\uparrow,$$
which brings $\tau$ forward: a transient noise burst in $w_B$ permanently advances the destabilization time. This is #der-adversarial-destabilization's Effects-Spiral, now a derived consequence of (A-cost)/(A-gate) rather than a discussion-grade schematic.

3. **The adversary's coupling need not grow.** The spiral closes through $\alpha_B$ *decaying* with $\gamma_A$ held **constant**. The Effects-Spiral's substantive content — collapse invisible to the static threshold — is captured *without* the unspecified $\gamma_A(\lVert\delta_B\rVert)$ leg #der-adversarial-destabilization could not formalize. Adversarial survival reduces to a **budget-versus-engagement-length race**: $B$ persists iff the engagement ends before $\tau$.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Budget-sufficient regime ≡ constant-$\alpha$ template, unchanged | #result-sector-persistence-template (status `exact`), $\psi\equiv 1$ limit | Inherited exact |
| Resource-scarce case is the decaying-$\alpha$ template slot (the reduction) | #result-sector-persistence-template time-varying-$\alpha$ + #schema-strategy-persistence precedent | Derived, conditional on (A-cost),(A-gate) |
| Certain finite-time destabilization, $r_{\mathcal{B}}=0$ | Monotone-budget + Lyapunov persistence-boundary crossing | Derived (conditional) |
| Effects-Spiral as derived feedback; $\tau$ advanced by excursions | (A-cost) substituted into the depletion law | Derived (conditional) |
| Adversary coupling need not grow ($\gamma_A$ constant suffices) | Corollary of the above | Derived (conditional) |
| Orthogonal to — not a resolution of — the deferred symmetric joint-Jacobian problem | Comparison of which term carries the feedback ($\alpha_B$ vs $\gamma_A$) | Verified relationship |
| (A-cost), (A-gate) | #form-resource-budget | Introduced posits, not derived |
| Regenerative regime $r_{\mathcal{B}}\gt 0$ | — | Open (not attempted) |

## Epistemic Status

*Conditional* on #form-resource-budget's two introduced posits (A-cost),(A-gate) and the hard regime $r_{\mathcal{B}}=0$. Given those, the chain is tight: the reduction to the decaying-$\alpha$ slot of #result-sector-persistence-template is exact-flavored (it is that template's own machinery, the same instantiation #schema-strategy-persistence makes for experience-decay), and certain finite-time destabilization follows by a monotone-budget + Lyapunov-boundary argument with no further assumption. The status is `conditional` rather than `exact` because the load-bearing premises are modeling posits about an agent's physical realization, not consequences of prior segments — inherited honestly from #form-resource-budget's own ceiling.

**Max attainable: `conditional`** for the formulation-dependent result; a specific agent class that satisfies (A-cost)/(A-gate) by construction (measured actuation energy, power-throttled control loop) lifts *its* instance to that class's tighter status, but the general statement stays conditional by the nature of its premises.

**Scope honesty — what this does not do.** It does *not* resolve the symmetric joint-best-response / joint-Jacobian equilibrium problem #der-adversarial-destabilization defers to #deriv-strategic-composition. That deferred problem is about both agents' mismatch co-evolving and specifically about the adversary's $\gamma_A(\lVert\delta\rVert)$ leg; this result closes a *different* leg (the target's own resource-gated $\alpha_B$) and is single-agent-with-resource. The two are orthogonal: this result needs no claim about $\gamma_A$ growing, and makes none. Reading it as having cracked the symmetric equilibrium problem would be an overclaim — it routes *around* that problem by adding resource structure, at the cost of two posits AAT otherwise lacks.

The regenerative regime ($r_{\mathcal{B}}\gt 0$) is genuinely open and not attempted here (see Working Notes).

## Discussion

**Why this is a strengthening, not a softening.** The honest move when facing #der-adversarial-destabilization's discussion-grade Effects-Spiral is not "leave it discussion-grade." It is to ask whether the spiral can be made a theorem. It can — in the resource-bounded regime, by a reduction to existing exact machinery — and the resulting statement is *sharper* than the original conjecture: it eliminates the need for the unformalized $\gamma_A(\lVert\delta_B\rVert)$ term rather than supplying a guessed functional form for it. A constant-effectiveness adversary against a hard-budget target is already sufficient for certain finite-time collapse. The strengthen-before-soften discipline produced a cleaner result than the discussion-grade original gestured at.

**The reframing is the payoff.** "Can the adversary destabilize me?" becomes "does the engagement outlast my fuel?" Persistence under a competent constant adversary is no longer a static inequality on $(\alpha,\rho,R)$ but a race between the hitting time $\tau$ and the engagement horizon — and $\tau$ is endogenous, advanced by every mismatch excursion the agent suffers. This is the precise sense in which a degrading embodied agent under hard physical limits "spirals": not because the opponent gets stronger, but because being wrong is expensive and the agent is spending a finite pool to be wrong in.

**Relationship to #schema-strategy-persistence.** That schema and this result are the two non-epistemic instantiations of #result-sector-persistence-template's *time-varying-$\alpha$* extension. Strategy persistence's $\alpha_\Sigma$ decays with accumulated experience and is rescued by forgetting; here $\alpha_B$ decays with spent budget and is rescued only by replenishment or by ending the engagement before $\tau$. Same template slot, different decay driver, structurally parallel rescue conditions. The parallel is itself evidence the template's time-varying-$\alpha$ extension is the right general object, with these as two of its instances.

## Findings

### Resource Depletion Closes the Effects Spiral by Eliminating Its Open Term

**Brief:** A robot fighting another robot on a finite battery does not lose because its opponent gets cleverer as it falters — it loses because faltering is expensive. A wrong model wastes actuation, the wasted actuation drains the battery, the drained battery slows the control loop, the slower loop lets the model fall further behind: a self-reinforcing collapse that needs no help from the adversary. The everyday version: a tired driver makes more mistakes, each mistake costs more energy to recover from, and the exhaustion that follows makes the next mistake likelier — the spiral is in the fuel, not in the road. AAT had this spiral only as an informal sketch because it could not say how a worse model makes an opponent stronger. The resource view removes the question: the opponent's strength can be held fixed; a finite, mismatch-sensitive fuel pool is enough to force certain collapse in finite time, with the only open question being whether the fight ends before the fuel does.

**Impact:** Converts #der-adversarial-destabilization's Effects-Spiral corollary from discussion-grade to conditional-derived — not by formalizing its unspecified adversary-coupling term but by making that term unnecessary, via a reduction to the decaying-$\alpha$ slot of #result-sector-persistence-template (the same machinery #schema-strategy-persistence uses for experience-decay). Reframes adversarial survival under a competent constant adversary from a static $(\alpha,\rho,R)$ inequality to a budget-versus-engagement-length race with an endogenous, excursion-advanced hitting time. Opens the resource-structure axis #def-strategy-dimension records as an explicit gap, as an exploratory branch off the spine. Explicitly does *not* resolve the deferred symmetric joint-Jacobian problem ( #deriv-strategic-composition) — it is orthogonal, and the Finding marks that boundary so the result is not over-read.

**Novelty Claim:** *Claim differentiation* on #der-adversarial-destabilization's Effects-Spiral: the contribution is showing the spiral becomes a derived finite-time-destabilization result once a minimal resource state is added, and that the strengthening *removes* rather than supplies the previously-open coupling functional form. The sector-Lyapunov and decaying-$\alpha$ machinery are AAT-internal and standard; resource-constrained control and energy-bounded games are established external territory; the differentiation is the specific recognition that the energy bound is the feedback variable that closes AAT's own named-open spiral by eliminating its open leg, conditional on two explicit posits.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Resource/energy budgets shaping control behavior | Energy-bounded / resource-constrained control and RL (broad external literature) | *adjacent literature* — supplies the modeling milieu (depletable budgets, cost-of-control); AAT's contribution is the coupling of model quality into drain and budget into the sector parameter, closing a specific AAT-internal spiral |
| Decaying-gain → eventual instability | #schema-strategy-persistence (experience-decay forgetting prerequisite) | *formal antecedent (AAT-internal)* — the same time-varying-$\alpha$ template slot; resource-depletion is its second non-epistemic instantiation |
| Effects-Spiral as informal panic mechanism | #der-adversarial-destabilization Corollary (discussion-grade) | *formalized by this finding* — the prior segment's open feedback term is here made unnecessary, not filled in |

**Search Log:**
- 2026-05-19 (*intuition-only*): The resource-constrained-control and energy-bounded-games literatures are large and were not searched; the AAT-internal claim (energy bound as the feedback variable that closes the Effects-Spiral by eliminating its open $\gamma_A(\lVert\delta\rVert)$ leg, conditional on (A-cost)/(A-gate)) has not been searched against that literature. The constituent machinery (sector-Lyapunov, decaying-$\alpha$) is AAT-internal and standard; the differentiation claim is plausibly distinctive but unverified. Targeted future search: cost-of-control / energy-aware MPC, budgeted-RL regret under adversaries, lazy-control and event-triggered control under depletable actuation. Pre-search expectation: constituent moves well-precedented externally; the AAT-internal "closes its own named-open spiral by removal" framing is the candidate-distinctive part.

## Working Notes

- Reasoning trail: `spikes/fight/03-energy-bound-effects-spiral.md` (the Φ-prompted derivation attempt that produced this branch) and `spikes/fight/99-verdict.md` §2–3. The math lands here per math-lives-in-segments; the spike is the trail only.
- **Open — regenerative regime.** $r_{\mathcal{B}}\gt 0$ with a finite-capacity pool is the full time-varying-$\alpha$ ODE and is not attempted. It is plausibly quasi-stationary-distribution / absorbing-barrier-flavored (structural cousin of the open second no-go in the continuity-persistence reasoning trail). The natural next spike: classify whether bounded replenishment can guarantee $\mathcal{B}_t\gt\mathcal{B}_{\text{crit}}$ indefinitely or only postpone $\tau$ in expectation (a Feller-test / absorbed-chain boundary question, exactly parallel to the continuity-persistence barrier-reachability open problem).
- **Open — rate constants.** $\tau$ as an explicit function of $(\mathcal{B}_0,\beta_{\mathcal{B}},\psi,\text{engagement length})$ is not computed; only its finiteness and monotone advancement under excursions are derived. A closed-form $\tau$ under the linear $c$ and a specific $\psi$ (e.g. saturating $\psi(\mathcal{B})=\mathcal{B}/(\mathcal{B}+\mathcal{B}_{1/2})$) is a tractable follow-on if the branch is pursued.
- Exploratory-branch status: no spine segment depends on this or on #form-resource-budget; OUTLINE marks both `exploratory`. Promotion past `draft` is gated on Joseph electing to develop the resource axis (regenerative case + a worked agent class satisfying (A-cost)/(A-gate) by construction would be the path to lifting an instance above `conditional`).
