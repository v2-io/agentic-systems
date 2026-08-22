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

Agent viability decomposes **additively** into agent-movable terms and an irreducible environmental floor — inherited from the exact mismatch decomposition — and provably does **not** factor multiplicatively into an agent-independent environmental rate times agent factors. The construction takes log-viability as the log-margin between steady-state mismatch and the critical task boundary, and inherits the additive split (estimation error + state-uncertainty floor + channel noise) from #result-mismatch-decomposition; the agent can move the estimation term by modeling and the state-uncertainty term by acting; the channel term it cannot move by modeling — it is a kernel of the channel, policy-movable only in expectation through which states and instruments the policy visits ( #deriv-mismatch-budget-attribution).

The constitutive no-go is that multiplicative $\rho$-factorization of the form "$\rho = \rho_{\text{external}} \cdot f(\text{model-class}) \cdot g(\text{policy})$" is type-incorrect: mismatch is constitutively agent-relative, so $\rho^2$ carries an estimation term that *vanishes* as the agent's model improves — a contribution that subtracts to zero cannot be represented by attenuating a fixed agent-independent scalar by agent factors. Established exactly is the additive env/agent split with the environmental floor. The finer structure of the agent-side component is characterized in #deriv-mismatch-budget-attribution: there is no separate policy term — the policy enters every term, the floor included, only as the on-policy measure under which three policy-independent kernels are averaged — so the honest fine split is estimation / state-uncertainty / channel with policy-dependence in each, log-additive to first order when the agent-movable excess is small relative to the floor. Separately *identifying* those terms from on-policy data remains obstructed and requires Level-2 interventional access ( #disc-identifiability-floor Instance 4).

## Log-Viability

Log-viability $\mathcal{V}$ is the margin by which steady-state mismatch $R^\ast$ stays below the critical task boundary $\lVert\delta_{\text{critical}}\rVert$:

$$\mathcal{V} = \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log \lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

Persistence holds exactly when $\mathcal{V} \gt 0$. Under linear Model D, $R^\ast = \rho/\alpha$ ( #result-persistence-condition), so

$$\mathcal{V} = \log \lVert\delta_{\text{critical}}\rVert - \log \rho + \log \alpha$$

*[Derived]* — exact algebra (logarithm of a ratio); independent of how $\rho$ itself is structured.

## The disturbance is additive, not multiplicative

The decomposition of viability into "what the environment imposes" versus "what the agent controls" runs through the structure of $\rho$. That structure is fixed by an existing exact result, not a free modeling choice.

**The exact mismatch decomposition.** By #result-mismatch-decomposition (`status: exact`, via the fresh-noise assumption GA-1), expected squared mismatch splits with vanishing cross-terms:

*[Derived (exact, inherited from #result-mismatch-decomposition GA-1)]*

$$\mathbb{E}[\lVert\delta_t\rVert^2] = \underbrace{\mathbb{E}[\lVert\hat o_t - \hat o_t^{\mathrm B}\rVert^2]}_{\text{estimation — reducible by modeling}} \;+\; \underbrace{\mathbb{E}[\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})]}_{\text{state uncertainty — movable by acting}} \;+\; \underbrace{\mathbb{E}[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{channel noise — irreducible}}$$

All cross-terms are zero by orthogonality (not independence), exactly as that result establishes. The first two terms are **agent-side**: the estimation term shrinks as the model improves, vanishing at the Bayes predictor; the state-uncertainty floor binds every model — well-specified or not — and yields only to *acting* (more informative interaction history), never to better modeling alone. The third is the **irreducible environmental floor**: a property of the observation channel the agent cannot reduce. A boundary note, because the working record has drawn it in two places: "the environmental floor" can be placed at the channel term alone (as here — everything else is agent-movable, by model or by policy) or at the full Bayes floor (state uncertainty + channel — everything no *model* can remove); the two placements differ by exactly the state-uncertainty term. This segment uses the first placement because the viability split is about what the agent — model and policy together — can move.

**Rate-lift (stated convention).** The persistence condition uses the disturbance *rate* $\rho$, related to expected squared mismatch by a fluid-limit identification $\rho^2 = \nu \cdot \mathbb{E}[\lVert\delta_t\rVert^2]$ for a positive throughput factor $\nu$:

*[Formulation — stated fluid-limit convention, introduced here; not a pre-existing canon identity. The structural conclusion below is convention-robust: any $\nu \gt 0$ preserves additivity, since positive scaling of a sum is a sum.]*

**The viability decomposition.** Substituting the exact split gives

*[Derived (conditional on the stated rate-lift convention)]*

$$\mathcal{V} = \mathcal{V}_{\text{env}} + \mathcal{V}_{\text{agent}}$$

where the first term $\mathcal{V}_{\text{env}}$ collects the channel-floor contribution (environmental affordance) and the second collects the estimation and state-uncertainty contributions together with the $\log\alpha$ tempo/gain terms (internal-operational health: the estimation part improves as the model improves; the state-uncertainty part as the agent's interaction history grows more informative).

**No multiplicative factorization (constitutive no-go).**

*[Derived — constitutive impossibility; exact under the constitutive definition of mismatch]*

There is no agent-independent scalar $\rho_{\text{external}}$ with $\rho = \rho_{\text{external}} \cdot f(\mathcal{M}) \cdot g(\pi)$. Mismatch is constitutively agent-relative ($\delta_t \equiv o_t - \hat o_t$, #def-mismatch-signal), so $\rho^2$ carries the estimation term, which **vanishes as the agent's model improves**. A multiplicative form attenuates a fixed agent-independent scalar by agent factors; it cannot represent a contribution that *subtracts to zero* under an agent-internal change. Multiplicative-in-rate and additive-in-(squared-mismatch) are type-incompatible, and $\sqrt{A+B} \neq \sqrt{A}\,\sqrt{B}$ blocks recovering the product form under the rate-lift. The decomposition is additive by construction, not by choice.

## Epistemic Status

The mismatch decomposition is **exact** ( #result-mismatch-decomposition, under GA-1). The viability decomposition in $\rho$-units is **conditional on the stated fluid-limit rate-lift** — a modeling convention introduced in this segment, not a pre-existing canonical identity; the *additive structure* (versus multiplicative) is robust to it for any positive throughput factor. The constitutive no-go is exact given the definition of mismatch. A general (non-isotropic, state/policy-dependent) diffusion $\Sigma(\delta,t)$ preserves additivity by linearity of the Itô generator in the diffusion matrix — this is an elementary extension *beyond* #deriv-sector-condition Prop A.1S's constant-isotropic $\sigma_w^2 I_n$ case, correct but not itself part of that result's `exact` scope.

## Discussion

**The finer split: structure exact, identification obstructed.** Decomposing $\mathcal{V}_{\text{agent}}$ further is not a model-vs-policy question. By #deriv-mismatch-budget-attribution, the estimation, state-uncertainty, and channel terms are expectations of policy-independent kernels under the on-policy law; the policy is the *measure*, not a term, so "policy benignity" is the policy concentrating the trajectory where the model class is adequate — one kernel modulated by one measure, entangled at the source rather than two independent factors — and the multiplicative intuition is recovered only as a first-order expansion in the excess-to-floor ratio, with the "factors" being floor-relative exponentials of the additive estimation and state-uncertainty terms. What *is* obstructed is identification: an on-policy observer sees only the sum, and separating the terms from observational data alone is the identifiability-floor phenomenon ( #disc-identifiability-floor Instance 4, via #der-architecture-noidentifiability) — in a feedback system high internal capacity itself lowers future environmental difficulty, and Level-2 interventional access (rotating agents across environments, or changing instrument / actions / model) is required to resolve it. This segment asserts the exact two-term env/agent split and the no-go; the attribution structure lives in #deriv-mismatch-budget-attribution and the identification floor in #der-architecture-noidentifiability.

**Why this matters.** The two-term split is the honest form of the internal/external diagnostic the persistence condition invites: it identifies exactly what an agent can improve by modeling (estimation error) and by acting (state uncertainty, and the on-policy channel term) versus the kernel-level floor no model touches (channel noise), without the false promise that the environmental rate is an agent-independent quantity one can read off and attribute blame to.

## Working Notes

- Provenance (process history, not theory content): this segment previously asserted a multiplicative $\rho = \rho_{\text{external}}\cdot f(\mathcal{M})\cdot g(\pi)$ split, was honesty-marked `status: false`, and was rebuilt on the exact mismatch decomposition. The constitutive no-go and the canon-forcing of the additive form were established by an independent recheck and confirmed by an independent verifier that also caught two pedigree over-claims (the $\nu$ rate-lift is *not* a pre-existing `#hyp-mismatch-dynamics` identity — landed here as a stated convention; the general-$\Sigma$ additivity exceeds Prop A.1S's constant-isotropic scope — labeled as an elementary extension). Full trail: CHANGELOG 2026-05-18; `spikes/ROUTING.md`.
- Boundary regression-guard (2026-07-03, audit 731548 B-2): the working layer twice defined the environmental floor $\rho_\star^2$ at *different* boundaries — the 2026-04-24 additive-variance spike at the full Bayes floor (state uncertainty + channel), the 2026-05-18 recheck at channel-instant variance only — differing by exactly the state-uncertainty term, and this segment's earlier gloss "vanishes for a well-specified model" was false under either placement (the Bayes-optimal predictor retains the state-uncertainty floor; see the Kalman anchor in #result-mismatch-decomposition). The three-term form now inherited from #result-mismatch-decomposition states the boundary explicitly; if a future edit re-merges the middle term into either neighbor, check it against that segment's derivation first. History: CHANGELOG 2026-07-03; the $\rho$-family row in `spikes/INDEX.md`.
