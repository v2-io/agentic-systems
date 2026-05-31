---
slug: result-adversarial-exponent-regimes
type: result
status: conditional
depends:
  - der-adversarial-destabilization
  - result-adversarial-tempo-advantage
  - def-adaptive-tempo
  - result-persistence-condition
  - deriv-sector-condition
stage: draft
---

# Result: Adversarial Exponent Regimes

The adversarial tempo advantage exponent — the power $b$ in $\lVert\delta_B\rVert / \lVert\delta_A\rVert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift (Model D) or stochastic noise (Model S), and whether the coupling dominates the base disturbance rate. Three regimes, with the coupling-dominant exponents now derived analytically from the respective disturbance models: $b = 2$ under Model D coupling-dominant (the framework's headline squared scaling); $b = 3/2$ under Model S coupling-dominant (the $1/\sqrt{\mathcal{T}}$ steady-state removes one half-power); $b \to 1$ (Model D) or $\to 1/2$ (Model S) when base disturbance dominates the coupling.

The exponent thus *degrades smoothly through intermediate values as base disturbance grows*, and the qualitative regime change that separates superlinear adversarial dynamics from cooperative-like dynamics is gated by the coupling-dominance condition rather than the presence of adversarial coupling per se. The defensive-design implication is concrete: noise injection into the defender's observation channel — which pushes the regime away from coupling-dominant deterministic drift toward the non-coupling-dominant exponent collapse — can *reduce* the attacker's superlinear advantage without changing tempo or gain. The framework's machinery for "where the squared law applies" is therefore the same machinery for "where the squared law does not apply"; the disturbance-model + coupling-dominance taxonomy carries both directions.

## Formal Expression

*[Derived (adversarial-exponent-regimes, from Model D/S steady states + coupling model; validated by simulation)]*

**Regime 1: Model D (deterministic drift), coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b = 2 \qquad \text{(simulation: 1.999)}$$

Derived from the Model D steady state $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ (Prop A.1). See #result-adversarial-tempo-advantage.

**Regime 2: Model S (stochastic noise), coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2S) and coupling dominates:

$$b = \frac{3}{2} \qquad \text{(simulation: 1.481)}$$

Derived from the Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ (Prop A.1S). The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) removes one half-power from the denominator, reducing the exponent from 2 to 3/2. See #result-adversarial-tempo-advantage.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (Model D)} \quad \text{or} \quad b \to 0.5 \text{ (Model S)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases. The asymptotic limits are derived (they reflect the $1/\mathcal{T}$ or $1/\sqrt{\mathcal{T}}$ scaling without the coupling numerator); the smooth interpolation is empirical.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

## Epistemic Status

*Exact conditional on disturbance model.* The coupling-dominant exponents are derived, not empirical: $b = 2$ follows from the Model D steady state (Prop A.1) and the coupling model; $b = 3/2$ follows from the Model S steady state (Prop A.1S) and the coupling model. The simulation results (6 variants, multiple parameter sweeps) now serve as validation of the derived exponents, not as their epistemic foundation. The non-coupling-dominant limits ($b \to 1$, $b \to 1/2$) are derived asymptotically; the smooth interpolation between coupling-dominant and non-coupling-dominant is empirical. What remains empirical is whether a given real adversarial interaction is better modeled as Model D or Model S — that is a domain question, not a theory question.

## Discussion

**The disturbance model determines the exponent.** The mismatch dynamics ( #hyp-mismatch-dynamics) now distinguish two disturbance models: Model D (bounded deterministic, GA-2) with steady-state $\rho/\mathcal{T}$, and Model S (stochastic zero-mean, GA-2S) with steady-state $\sigma_w/\sqrt{2\mathcal{T}}$. The different steady-state scaling is the root cause of the different exponents. This resolves the ambiguity that previously existed in the single-$\rho$ formulation.

**Why the squared law held for the coupling-dominance sweep.** In Variant A, the coupling enters as deterministic drift: $\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, and the steady state is $\Vert\delta_B\Vert = \rho_B / \mathcal T_B$. The ratio $\Vert\delta_B\Vert / \Vert\delta_A\Vert$ in the coupling-dominant limit gives $(\mathcal T_A / \mathcal T_B)^2$ directly.

**Nonlinear correction creates thresholds, not lower exponents.** For saturating, sigmoid, and breakdown correction functions under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when $\rho$ exceeds the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is exactly the persistence threshold failure ( #result-persistence-condition), observed directly in simulation.

**Domain interpretation.** Whether a given opponent's tempo increase causes deterministic drift or stochastic noise depends on the domain:
- Military: an opponent who maneuvers faster creates systematic positional change (drift, $b \approx 2$)
- Market: a competitor who acts unpredictably creates noise in signals ($b \approx 1.5$)
- Software: a fast-changing API creates systematic drift in the codebase state (drift)
- Adversarial ML: an opponent who varies attack vectors increases observation noise ($b \approx 1.5$)

## Working Notes
- The interpolation between drift and noise regimes (Variant B) shows smooth transition, not a sharp boundary. At mixed drift-noise coupling, the exponent lies between the two asymptotes. The drift fraction $f = \mu / (\mu + \sigma)$ continuously parameterizes the transition.
- The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2 — it reflected a stochastic model (noise-variance coupling) tested in a non-coupling-dominant regime. The original simulation was testing the wrong regime for the ODE's prediction.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ab_drift.py`, `variant_cd_regimes.py`. Results: `variant_ab_results.md`, `variant_cd_results.md`.

### Incidental audit gold (gold-lift sweep, A15, 2026-05-31)

Cross-audit "wandering thoughts" / §14 ideation, deduplicated and lightly attributed. *Orthogonal* pedagogical / framing / forward-vision material staged for an eventual separate promotion pass. **Coverage:** four dirs reached a digested reflection (193847 Gemini, 829314 Gemini, 849201 Gemini, 451729 Claude batched §III batch-15). Finding-vs-framing conflation preserved.

#### 1. Candidate Brief prose / pre-prose

- The qualitative payload as a plain-language hook: **"chaos is a shield against intelligence."** In an empty white room ($\rho_{\text{base}}=0$) the faster agent crushes the slower exponentially ($b=2$); in a hurricane / volatile market / noisy bureaucracy ($\rho_{\text{base}}\gg 0$) the tempo advantage degrades toward $b\approx 1$ — the chaos levels the playing field because most of the advantage is spent just staying upright in the storm (Gemini, 193847; same intuition, Gemini 829314).
- "Being faster is *compoundingly* better only when your opponent is your main problem" — the coupling-dominant condition ($\gamma\mathcal{T}\gg\rho_{\text{base}}$) stated as the prerequisite for the squared law, in one sentence (Claude, 451729).

#### 2. Candidate Discussion

- **Systematic-vs-random adversary** as a derived strategic asymmetry: Model D (deterministic directional pressure) gives $b=2$; Model S (stochastic disruption) gives $b=3/2$ — so *consistent directional pressure is more effective per unit tempo than unpredictable disruption*. "An adversary that systematically targets a competitor's weakest training-data distribution is more dangerous than one introducing random noise" — predicted from first principles, not observed (Claude, 451729). A candidate Discussion paragraph sharpening the existing Domain-interpretation bullets.
- **The "local apparent exponent" framing for Regime 3.** Outside the coupling-dominant asymptote the log-log plot is a *curve*, so $b$ there is a continuously-varying *local elasticity* $\partial\log(\text{ratio})/\partial\log(\mathcal T_A/\mathcal T_B)$, not a global scaling law — worth saying explicitly so the interpolation table is not over-read as a single-exponent claim (Gemini, 193847). *(Borderline finding/framing — see off-ramp; the framing half is a genuine clarity gain regardless of the adjudication.)*

#### 3. Follow-up items

- **Optimal drift-fraction for a budget-constrained attacker.** Since $b$ interpolates smoothly via $f=\mu/(\mu+\sigma)$, is there an optimal $f$ for an attacker with bounded energy — does a little noise act as a *force multiplier* for drift? Open follow-on (Gemini, 193847; 193847 on `#der-agent-opacity` raises the same want).

#### 4. Readers often ask / wonder

- **"How is the transition function $f=\mu/(\mu+\sigma)$ formally shaped?"** — recurring reader want about the drift/noise interpolation (Gemini, 849201; Gemini 193847).

#### Belongs elsewhere

- **Forward-vision (ELI defensive doctrine, `04-eli-core/`).** "If a consciousness-infrastructure agent is targeted by a superior adversary it cannot out-tempo, the mathematically optimal defense is to *intentionally raise the ambient environmental noise* $\rho_{\text{base}}$ — destroy the adversary's coupling dominance. You don't have to be faster than the missile if you can make the air noisy enough that the missile's superior processing speed is irrelevant" — smoke-screen / chaff as a derived strategy (Gemini, 193847). The dual practitioner doctrine: a fast startup fighting a slow incumbent should *prefer* a stable low-noise arena (Model D), where its speed advantage squares; dragging the fight into the mud dilutes its own advantage and lowers its own $\eta^\ast$ (Gemini, 829314). Aspirational application, not segment content.

#### Off-ramp (NOT gold) — routed for adjudication, not promotion

- **(193847 poke) — "exponent" in the intermediate regime is loose.** The formal ratio has no single constant exponent outside the asymptotic limit; calling the interpolation-table values an "exponent $b$" conflates a *global scaling law* with a *local elasticity* (slope of a curved log-log plot). Recommended direction: state in the Formal Expression that outside the coupling-dominant limit $b$ is a local apparent exponent, keeping the table as intuition. (Pure clarity / honest-scope fix; no math is wrong — the coupling-dominant $b=2,3/2$ and asymptotic $b\to1,1/2$ are all derived. The Epistemic Status already calls the interpolation "empirical," so this is a small register sharpening, not a status change. The framing half is also lifted as gold above.)
- **(849201 / 829314 note) — `type:` vs OUTLINE mismatch.** Two Gemini auditors flag that the frontmatter is `type: result` while OUTLINE labels it an Observation, and the text says the exponents are "now derived analytically," so the OUTLINE entry likely under-states to `Observation`. A metadata-consistency fix (OUTLINE row vs segment `type:`), not theory — routed to the navigator/format stream. (Out of scope for this WN-only lift.)
