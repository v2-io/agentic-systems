---
slug: deriv-tempo-additivity
type: derivation
status: conditional
depends:
  - def-adaptive-tempo
  - emp-update-gain
  - deriv-fisher-local-update-gain
stage: draft
---

# Derivation: Scope of Tempo Additivity — Redundancy, Synergy, and the Echo-Chamber Bound

The additive tempo formula $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)\ast}$ ( #def-adaptive-tempo) is exact when the observation channels carry cross-channel-independent noise, and its deviation from the true joint capacity under correlated noise is **signed**: correlated channels can deliver *less* joint information than the additive accounting claims (redundancy — the additive form overcounts) or *more* (synergy — correlated noise can be cancelled, and the additive form undercounts). This segment derives the exact deviation in the Fisher-local regime, proves the additive form is an exact upper bound with an explicit, closed-form redundancy penalty in the **common-source noise regime** (the "echo chamber": a shared persistent bias contaminating several channels), proves an information-**saturation** theorem for persistent shared bias (no number of correlated channels buys information past the shared-bias floor), and establishes two no-gos: no sign-blind dependence measure (conditional mutual information, total correlation) can be the exact correction term, and no convention-free channel-local attribution of the deviation exists for three or more channels (the partial-information-decomposition obstruction). The joint tempo and the *total* deviation are canonical; per-channel corrected contributions are not.

## Formal Expression

### Setup — the information reading of tempo

*[Definition (effective tempo, Fisher-local regime)]*

Work in the Fisher-local / Gaussian location regime of #deriv-fisher-local-update-gain: environment parameter $\theta$, model uncertainty $U_M$ (posterior variance), channels $k = 1, \dots, n$ with independent Poisson event rates $\nu^{(k)}$ and per-event observations $o^{(k)} = \theta + n^{(k)}$, noise variance $U_o^{(k)} = \mathrm{Var}(n^{(k)})$. Let $\mathfrak{J}$ denote the posterior-precision inflow rate delivered by the *optimal joint filter* (Fisher information about $\theta$ acquired per unit time). The **effective tempo** is the fractional uncertainty-contraction rate

$$\mathcal T_{\text{eff}} := -\frac{d}{dt}\log U_M(t) = U_M \cdot \mathfrak{J},$$

the second equality since $\tfrac{d}{dt}(1/U_M) = \mathfrak{J}$. Single-channel consistency: $\mathfrak{J} = \nu/U_o$ gives $\mathcal T_{\text{eff}} = \nu\,U_M/U_o$, which agrees with $\nu \eta^\ast = \nu\,U_M/(U_M + U_o)$ to first order in the per-event information ratio $U_M/U_o$ — the same first-order-in-step-size regime (R2) under which #deriv-fisher-local-update-gain operates and under which tempo is a rate at all. All statements below are exact at the Fisher-information level and transfer to gain-form tempo at that order.

### Additivity under noise independence

*[Derived (additivity-under-independence)]*

If the channel noises are independent across channels and events (conditional independence of the pooled event stream given $\theta$), scores add and score cross-covariances vanish, so Fisher information is exactly additive:

$$\mathfrak J_{\text{joint}} = \sum_k \nu^{(k)} \, \frac{1}{U_o^{(k)}} = \mathfrak J_{\text{add}} \quad\Longrightarrow\quad \mathcal T_{\text{eff}} = \sum_k \nu^{(k)} \eta^{(k)\ast} \;\text{(first order)}.$$

Independence is **sufficient but not necessary** for equality (see the harmonic-mean hypersurface below).

*[Derived (asynchrony refinement)]*

Independent Poisson streams almost surely have no simultaneous events. If noise is *fresh per event* (i.i.d. across events), instantaneous cross-channel noise correlation is never sampled and additivity remains exact regardless of it. What breaks additivity is noise dependence **across events** — a persistent shared noise component. The redundancy question is governed by the ratio of the noise-correlation timescale to event interarrival times.

### The exact deviation, and its indefinite sign

*[Derived (signed-deviation)]*

For a synchronized batch (one event per channel, jointly Gaussian noise $\Sigma_n$, $(\Sigma_n)_{kk} = U_o^{(k)}$), the joint Fisher information and the deviation from additivity are

$$J_{\text{joint}} = \mathbf{1}^{\top} \Sigma_n^{-1} \mathbf{1}, \qquad \Delta := \sum_k \frac{1}{U_o^{(k)}} - J_{\text{joint}},$$

and for two channels with noise covariance $c$ (writing $U_1, U_2$ for the variances):

$$J_{\text{joint}} = \frac{U_1 + U_2 - 2c}{U_1 U_2 - c^2}, \qquad \Delta = \frac{c\,\bigl(2 U_1 U_2 - c\,(U_1 + U_2)\bigr)}{U_1 U_2\,(U_1 U_2 - c^2)}.$$

$\Delta = 0$ iff $c = 0$ or $c = 2U_1U_2/(U_1 + U_2)$ (the harmonic mean of the variances — admissible whenever $U_1 \neq U_2$): equality holds on a strictly larger set than independence, with redundancy and synergy cancelling exactly. $\Delta$ has **no definite sign**:

- **Anti-correlated noise (synergy).** $U_1 = U_2 = \sigma^2$, $\rho \lt 0$: $J_{\text{joint}} = 2/(\sigma^2(1+\rho)) \gt 2/\sigma^2$. Averaging cancels the noise; the additive form *under*counts.
- **Positively correlated, heterogeneous variances (synergy).** $U_1 = 1$, $U_2 = 100$, $c = 9.9$: $J_{\text{joint}} = 81.2/1.99 \approx 40.8 \gg 1.01$. The noisy channel serves as a noise *reference*; the combination $o^{(1)} - (c/U_2)\,o^{(2)}$ nearly cancels channel 1's noise.
- **Nonnegative equal-variance correlation, $n = 3$ (synergy).** Correlations $\rho_{12} = \rho_{23} = 0.7$, $\rho_{13} = 0$ (positive-definite): $\mathbf{1}^{\top} R^{-1} \mathbf{1} = 10 \gt 3$.

So "correlated channels $\Rightarrow$ the additive formula overcounts" is false as a general claim; overcounting is the *redundant* half of a two-sided phenomenon whose other half is noise-cancelling synergy.

### The echo-chamber regime — redundancy penalty and saturation

*[Derived (common-source-redundancy-penalty)]*

**Common-source noise model:** $n^{(k)} = s + w^{(k)}$ with shared bias $s \sim \mathcal{N}(0, \sigma_s^2)$ and independent $w^{(k)} \sim \mathcal{N}(0, \sigma_{w,k}^2)$, so $\Sigma_n = \sigma_s^2 \mathbf{1}\mathbf{1}^{\top} + \mathrm{diag}(\sigma_{w,k}^2)$. By Sherman-Morrison, with $q_k := 1/\sigma_{w,k}^2$, $q := \sum_k q_k$, and $f(x) := x/(1 + \sigma_s^2 x)$:

$$J_{\text{joint}} = f(q) \;\leq\; \sum_k f(q_k) = \sum_k \frac{1}{\sigma_s^2 + \sigma_{w,k}^2} = \sum_k J^{(k)},$$

by strict concavity of $f$ with $f(0) = 0$ (strict subadditivity), with equality iff $\sigma_s^2 = 0$ or at most one channel is active. The **redundancy penalty** is explicit and closed-form: $R_s = \sum_k f(q_k) - f(q) \gt 0$. In this regime the additive tempo *is* an exact upper bound on effective tempo, for arbitrarily heterogeneous channels.

*[Derived (saturation-under-persistent-bias)]*

If the shared bias $s$ is **persistent across events**, every observation measures $\theta + s$ plus fresh noise: the pooled data identify $\theta + s$ at additive rate, but the posterior precision about $\theta$ itself is bounded for all time by $1/U_M^{(0)} + 1/\sigma_s^2$, since $\mathrm{Var}(\theta \mid \theta + s) = (1/U_M^{(0)} + 1/\sigma_s^2)^{-1}$ and conditioning on the data is coarser than conditioning on $\theta + s$. Additive accounting claims precision growing without bound; the true joint information **saturates** at the shared-bias floor. No number of common-source channels, at any event rate, buys information past $1/\sigma_s^2$.

### Two no-gos

*[Derived (no-sign-blind-penalty)]*

No exact correction of the form $\mathcal T_{\text{eff}} = \mathcal T_{\text{add}} - g(D)$ exists for any dependence measure $D$ invariant under noise-correlation sign flip — conditional mutual information $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$, total correlation (Watanabe 1960), or any such functional. Proof: $\rho$ and $-\rho$ in the equal-variance two-channel family give identical Gaussian conditional mutual information $-\tfrac12\log(1 - \rho^2)$ but different joint informations $2/(\sigma^2(1 \pm \rho))$. The deviation depends on the dependence *geometry*, not the dependence *strength*; the exact correction is the Fisher deficit $\Delta$, which requires $\Sigma_n$, not a scalar dependence summary. Conditional mutual information survives as a **witness**: in the Gaussian location model $\Delta \neq 0 \Rightarrow I \gt 0$ (converse false on the harmonic-mean hypersurface), and in the common-source regime both $I$ and $R_s$ increase with $\sigma_s^2$.

*[Derived (no-canonical-channel-local-decomposition — imported)]*

A channel-local, convention-free additive decomposition of the joint information rate into per-channel redundancy-corrected contributions is the demand of the **partial information decomposition** program, and it is known not to exist in general: Williams & Beer 2010 define the redundancy lattice; Bertschinger, Rauh, Olbrich, Jost & Ay 2014 give the two-source unique-information measure; Rauh, Bertschinger, Olbrich & Jost 2014 prove no nonnegative decomposition on the Williams-Beer lattice satisfying the identity axiom exists for three or more sources; Barrett 2015 shows the Gaussian collapse of the main two-source candidates. Consequence: $\mathcal T_{\text{joint}}$ and the total deviation $\Delta$ are canonical and exact; "channel $k$'s corrected tempo contribution" is not a well-defined quantity for $n \geq 3$, and any AAT use of one must declare its attribution convention explicitly.

## Epistemic Status

*Conditional.* The derivations are exact within the Fisher-local / Gaussian location regime of #deriv-fisher-local-update-gain (conditions (R1)–(R3)) plus the stated noise models (jointly Gaussian batch noise for the deviation formula; the common-source structure for the penalty and saturation theorems); the transfer from Fisher-information statements to gain-form tempo is first-order in the per-event information ratio, the same regime in which tempo is a rate. Additivity-under-independence is general (standard Fisher additivity, not merely Gaussian); the counterexamples are exact and finite, computed in-segment. The two-source PID landscape and the $n \geq 3$ impossibility are imported results, cited by their real names; the mapping of the PID obstruction onto channel-local tempo attribution is AAT's reading and is stated at that grade. Citation details for the imported PID results are flagged for primary-source verification before promotion past `draft` (see Working Notes). This segment supplies the derivation behind the channel-independence condition named in #def-adaptive-tempo's Epistemic Status; it *refutes* the previously asserted general upper bound (the deviation is signed) and *establishes* the bound on its true scope (common-source regime), so downstream uses of "additive tempo is conservative" are unsafe unless the common-source (or general nonpositive-$\Delta$) structure is verified for the application.

## Discussion

**What the correction to the prior assertion changes.** The earlier claim — additive tempo is always an upper bound, equality iff channels informationally independent — read channel correlation as pure overlap. The derivation shows correlation is two-sided: overlapping *information* (common source) makes the additive form overcount, but correlated *noise* is also a resource — a correlated reference channel lets the filter cancel noise it could never average away, and then the additive form undercounts, potentially by large factors. Both directions matter for agent design: the redundant direction is the echo-chamber warning (diversity of observation *sources*, not count of observers), and the synergistic direction says a channel that is nearly useless in isolation (huge $U_o$, negligible $\eta^\ast$) can be extremely valuable jointly — a reason to retain "bad" sensors that are correlated with good ones' failure modes.

**The echo chamber, quantitatively.** The common-source saturation theorem is the formal content of the organizational intuition: three VPs reading one broken dashboard are one channel with extra steps, and past the shared-bias floor their combined reports carry zero marginal information about the world. A filter that *models* the channels as independent additionally manufactures false confidence — its internal $U_M$ shrinks at the additive rate while true error stalls at the bias floor, driving $\eta^\ast \to 0$ while genuinely wrong: the gain-collapse pathology of #emp-update-gain arrived at through mis-modeled channel structure rather than miscalibrated uncertainty *[Discussion]*.

**Why no simple penalty formula exists.** The no-gos localize the obstruction precisely. A scalar dependence summary cannot carry the correction (sign-blindness), and a per-channel attribution cannot be made canonical for $n \geq 3$ (PID impossibility). What *is* available exactly: the joint object $\mathbf{1}^{\top}\Sigma_n^{-1}\mathbf{1}$ (tensor case: $A^{\top}\Sigma_n^{-1}A$) whenever the noise covariance structure is known or estimable, and the closed-form penalty on the common-source scope. This is a scope-precision result in the CS sense: the boundary of the additive form is now characterized rather than gestured at.

**Anisotropy is orthogonal.** With multivariate $\theta$ and channel maps $A_k$, cross-channel noise independence gives exact *matrix* additivity $\mathcal{J} = \sum_k \nu^{(k)} A_k^{\top}(\Sigma_n^{(k)})^{-1} A_k$ — channels "measuring different aspects" is handled by the tensor form of #def-adaptive-tempo, not by redundancy corrections. Redundancy/synergy is an off-block-diagonal-noise phenomenon; anisotropy is an eigenbasis/observation-map phenomenon; the common-source subadditivity holds in the Loewner order by the same Sherman-Morrison-Woodbury argument.

**Composition consequence.** #der-team-persistence inherits both directions: allied reports drawing on one upstream source are the common-source regime (additive communication tempo overcounts, saturating at the source's bias floor), while allies with anti-correlated errors triangulate — a genuinely super-additive composition effect the additive accounting misses in the favorable direction.

## Working Notes

- **Citation verification before promotion.** The PID citations (Williams-Beer 2010 arXiv:1004.2515; Bertschinger-Rauh-Olbrich-Jost-Ay 2014 *Entropy* 16(4); Rauh et al. 2014 ISIT; Barrett 2015 *PRE* 91; Watanabe 1960 *IBM J. Res. Dev.* 4) are from literature memory and must be primary-source-verified (relata pass) before `claims-verified`. The mathematical content here does not lean on them — they scope the no-go's external grounding.
- **Finite-correlation-time interpolation.** §Asynchrony gives the two exact endpoints (fresh noise: additive exact; persistent bias: saturation). The intermediate regime (noise correlation time comparable to interarrival times) should interpolate via an effective $\sigma_s^2(\nu)$; a small spike could make the crossover explicit (OU-process shared bias, exactly solvable).
- **Loewner-order statement.** The tensor versions of the deviation and the common-source bound are asserted from the same arguments but not written out; mechanical, worth landing when a tensor-tempo consumer needs them.
- **Attribution conventions.** If a downstream segment ever needs per-channel corrected contributions (e.g. for channel-investment decisions in TST), Shapley/sequential attribution over the ordered filter is the natural declared-convention candidate — flagged so the convention-dependence is chosen consciously, not rediscovered.
- **Provenance.** Derived in `spikes/spike-adaptive-tempo-redundancy-penalty-2026-07-15.md` (full trail, counterexample arithmetic, ripple-site record). Ripple sites deliberately not executed in that cycle: `disc-independence-audit` §3 (states the refuted general inequality and needs re-pointing here), `der-team-persistence` (both-directions note), `def-strategic-tempo` (same scope conditions, unaudited).
