---
slug: internal-external-decomposition
type: derivation
status: conditional
depends:
  - result-mismatch-decomposition
  - result-persistence-condition
  - hyp-mismatch-dynamics
  - def-adaptive-tempo
stage: draft
---

# Derivation: Internal-External Decomposition of Agent Viability

Agent viability decomposes **additively** into a reducible agent-internal term and an irreducible environmental floor — inherited from the exact mismatch decomposition — and provably does **not** factor multiplicatively into an agent-independent environmental rate times agent factors.

## Log-Viability

Log-viability $\mathcal{V}$ is the margin by which steady-state mismatch $R^\ast$ stays below the critical task boundary $\lVert\delta_{\text{critical}}\rVert$:

$$\mathcal{V} = \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

Persistence holds exactly when $\mathcal{V} \gt 0$. Under linear Model D, $R^\ast = \rho/\alpha$ ( #result-persistence-condition), so

$$\mathcal{V} = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$$

*[Derived]* — exact algebra (logarithm of a ratio); independent of how $\rho$ itself is structured.

## The disturbance is additive, not multiplicative

The decomposition of viability into "what the environment imposes" versus "what the agent controls" runs through the structure of $\rho$. That structure is fixed by an existing exact result, not a free modeling choice.

**The exact mismatch decomposition.** By #result-mismatch-decomposition (`status: exact`, via the fresh-noise assumption GA-1), expected squared mismatch splits with a vanishing cross-term:

*[Derived (exact, inherited from #result-mismatch-decomposition GA-1)]*

$$\mathbb{E}[\lVert\delta_t\rVert^2] = \underbrace{\mathbb{E}[\lVert\hat o_t - \bar o_t\rVert^2]}_{\text{model error — reducible}} \;+\; \underbrace{\mathbb{E}[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise — irreducible}}$$

The cross-term is zero by orthogonality (not independence), exactly as that result establishes. The first term is **agent-internal**: it shrinks as the model class $\mathcal{M}$ improves and vanishes for a well-specified model. The second is the **irreducible environmental floor**: a property of the observation channel the agent cannot reduce.

**Rate-lift (stated convention).** The persistence condition uses the disturbance *rate* $\rho$, related to expected squared mismatch by a fluid-limit identification $\rho^2 = \nu \cdot \mathbb{E}[\lVert\delta_t\rVert^2]$ for a positive throughput factor $\nu$:

*[Formulation — stated fluid-limit convention, introduced here; not a pre-existing canon identity. The structural conclusion below is convention-robust: any $\nu \gt 0$ preserves additivity, since positive scaling of a sum is a sum.]*

**The viability decomposition.** Substituting the exact split gives

*[Derived (conditional on the stated rate-lift convention)]*

$$\mathcal{V} = \mathcal{V}_{\text{env}} + \mathcal{V}_{\text{agent}}$$

where the first term $\mathcal{V}_{\text{env}}$ collects the irreducible-floor contribution (environmental affordance) and the second collects the reducible model-error contribution together with the $\log\alpha$ tempo/gain terms (internal-operational health that improves as the agent improves).

**No multiplicative factorization (constitutive no-go).**

*[Derived — constitutive impossibility; exact under the constitutive definition of mismatch]*

There is no agent-independent scalar $\rho_{\text{external}}$ with $\rho = \rho_{\text{external}} \cdot f(\mathcal{M}) \cdot g(\pi)$. Mismatch is constitutively agent-relative ($\delta_t \equiv o_t - \hat o_t$, #def-mismatch-signal), so $\rho^2$ carries the reducible model-error term, which **vanishes as the agent's model improves**. A multiplicative form attenuates a fixed agent-independent scalar by agent factors; it cannot represent a contribution that *subtracts to zero* under an agent-internal change. Multiplicative-in-rate and additive-in-(squared-mismatch) are type-incompatible, and $\sqrt{A+B} \neq \sqrt{A}\,\sqrt{B}$ blocks recovering the product form under the rate-lift. The decomposition is additive by construction, not by choice.

## Epistemic Status

The mismatch decomposition is **exact** ( #result-mismatch-decomposition, under GA-1). The viability decomposition in $\rho$-units is **conditional on the stated fluid-limit rate-lift** — a modeling convention introduced in this segment, not a pre-existing canonical identity; the *additive structure* (versus multiplicative) is robust to it for any positive throughput factor. The constitutive no-go is exact given the definition of mismatch. A general (non-isotropic, state/policy-dependent) diffusion $\Sigma(\delta,t)$ preserves additivity by linearity of the Itô generator in the diffusion matrix — this is an elementary extension *beyond* #deriv-sector-condition Prop A.1S's constant-isotropic $\sigma_w^2 I_n$ case, correct but not itself part of that result's `exact` scope.

## Discussion

**The finer split is conditional, not exact.** Decomposing $\mathcal{V}_{\text{agent}}$ further into model-class ($\mathcal{M}$), policy ($\pi$), and cross contributions is a *mediation* question, not an identity: it is identifiable under interventional regimes (rotating the same agent across environments, or environments across agents) and **confounded** otherwise — in a feedback system high internal capacity itself lowers future environmental difficulty, entangling the terms. That confound is an identifiability-floor phenomenon ( #disc-identifiability-floor): separating the agent-internal sub-terms from observational data alone is formally obstructed; Level-2 interventional access is required. This segment asserts only the exact two-term env/agent split and the no-go; the finer $\mathcal{M}/\pi$/cross decomposition and its precise floor characterization are under separate investigation and are deliberately not asserted here.

**Why this matters.** The two-term split is the honest form of the internal/external diagnostic the persistence condition invites: it identifies exactly what an agent can improve (model error) versus the floor it cannot (channel noise), without the false promise that the environmental rate is an agent-independent quantity one can read off and attribute blame to.

## Working Notes

- Provenance (process history, not theory content): this segment previously asserted a multiplicative $\rho = \rho_{\text{external}}\cdot f(\mathcal{M})\cdot g(\pi)$ split, was honesty-marked `status: false`, and was rebuilt on the exact mismatch decomposition. The constitutive no-go and the canon-forcing of the additive form were established by an independent recheck and confirmed by an independent verifier that also caught two pedigree over-claims (the $\nu$ rate-lift is *not* a pre-existing `#hyp-mismatch-dynamics` identity — landed here as a stated convention; the general-$\Sigma$ additivity exceeds Prop A.1S's constant-isotropic scope — labeled as an elementary extension). Full trail: CHANGELOG 2026-05-18; `msc/spike-routing-2026-05-17.md`.
- Open (reserved, under independent investigation): the conditional $\mathcal{M}/\pi$/cross refinement and whether its Regime-C confound is a distinct `#disc-identifiability-floor` instance. Do not assert the three-way split until that resolves.
