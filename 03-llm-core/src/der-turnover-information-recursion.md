---
slug: der-turnover-information-recursion
type: derived
status: conditional
depends:
  - result-sector-persistence-template
  - obs-context-turnover
  - form-information-bottleneck
stage: draft
---

# Derived: The Across-Turnover Information Recursion — Persistence Is Imported, Not Intrinsic

Across session boundaries the scaffolded logogenic agent's relevant epistemic content evolves as an *affine information recursion* — multiplicative strong-data-processing contraction at each lossy reconstruction, plus additive reinjection of fresh information. The self-compressing destroy-and-reconstruct walk with no reinjection decays geometrically to zero; there is no inter-session analog of the rate-regime persistence condition $\alpha \gt \rho/R$, and the sector-persistence template ( #result-sector-persistence-template) provably does not transfer to this regime. Persistence across turnover is therefore not a property the composite can possess intrinsically: it is wholly imported through a non-vanishing reinjection channel — structurally, the §03.II scaffold — at a level set by reinjection over the contraction gap.

## Formal Expression

The intra-session regime is governed by the rate-condition persistence machinery of Part I, applied to the coupled update. The inter-session regime is qualitatively different: per #obs-context-turnover the state is not perturbed but *destroyed and reconstructed* through the lossy stochastic kernel $f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{w}})$. This segment derives the dynamics of that regime under modeling commitments argued from the structure of the turnover boundary itself.

### Setup: the state variable and the boundary channel

Let $Y$ be the **predictive-sufficiency target** of #disc-m-preservation — the future-observation continuant about which model sufficiency ( #def-model-sufficiency) is defined. Write the relevant-information state at the start of session $k$ as

$$I_k \;:=\; I(M_k^+;\, Y) \,\in\, [0,\, H_\Delta],$$

the (un-normalized) mutual information between the reconstructed start-of-session state and $Y$, finite at any reconstruction fidelity $\Delta \gt 0$. The predictive-sufficiency readout is a normalization of $I_k$: $S(M) = I_k / I(\mathcal{C};Y)$ for $Y$ the predictive target, not a distinct dynamical object. The task-adequacy floor $S_{\min}$ enters only as the line below which the composite is operationally dead ($I_k \geq S_{\min}\, I(\mathcal{C};Y)$); it is a readout, not a barrier in the dynamics.

Identity continuity is a *different* target — the identity-relevance vector of #def-identity-sufficiency, a walk on the identity gap under a reflected, relationally-compensated operator with a load-bearing $\mu=0$ boundary. It is **not** a normalization of $I_k$: it is a structurally distinct operator at the opposite end of the same singular contraction parameter, with its own segment ( #der-identity-continuity-threshold). This segment is the predictive-sufficiency regime only; the cross-reference at the end of the Discussion states the relationship precisely.

### The argued modeling commitments

The inter-session dynamics are under-specified by AAT: the accumulation operator, the state variable, and the driving process are choices, not theorems to extract. They are committed here and argued from the exact content of #obs-context-turnover, not assumed for convenience.

**(C1) The boundary map contracts mutual information multiplicatively.** Only the externalized-and-reconstructed state crosses the boundary; nothing else carries over ( #obs-context-turnover). The information path is the Markov chain $Y \to X_k \to M_{k+1}^+$, where $X_k$ is the end-of-session-$k$ content and $M_{k+1}^+$ is the reconstruction through $f_{\text{init}}$. The strong data-processing inequality (SDPI) states that mutual information through any non-degenerate noisy or rate-limited channel contracts by a multiplicative coefficient strictly below one:

*[Derived (turnover-sdpi-contraction, from form-information-bottleneck + Ahlswede–Gács 1976)]*

$$I(M_{k+1}^+;\, Y) \;\leq\; \eta_k\, I(X_k;\, Y), \qquad \eta_k \in [0,1],$$

with $\eta_k \lt 1$ strictly whenever the boundary is genuinely lossy — budget below the $Y$-content, or noisy reconstruction, which is the *characteristic* 100%-reset condition of #obs-context-turnover — and $\eta_k = 1$ only in the non-characteristic lossless case. The purely-additive break-even accumulation $\epsilon^{(n)} = \sum_k \Delta\epsilon_k$ previously written in #disc-m-preservation presumed additive loss with a break-even threshold; under multiplicative contraction that bookkeeping is the wrong shape for the predictive-sufficiency accumulation (R3).

**(C2) The state variable is $I_k = I(M_k^+;Y)$.** SDPI acts natively on mutual information; the dichotomy below is assumption-free in this coordinate. The reconstruction-distance $\epsilon_{\text{recon}}$ is not a global monotone transform of $I_k$, which is why $I_k$ is fixed as primary and the sufficiency readouts are derived from it.

**(C3) Reinjection is the conditional fresh information $\rho_k := I(X_k;\, Y \mid M_k^+) \geq 0$** — the $Y$-information in the end-of-session content $X_k$ *conditional on* the reconstructed start state, i.e. exactly the part not derivable from the compressed state. The conditional definition is what makes the next bound an exact chain-rule identity rather than a (false) sub-additivity claim. Structurally this is the §03.II scaffold: the durable-artifact, curated-narrative, and relational-re-attestation layer of #scope-scaffolded-logogenic's external persistent state $M^{\text{ext}}_t$. It is left as a general non-negative sequence, so the result is proven robust across its sub-models (R4).

**(C4) Uniform contraction: $\sup_k \eta_k \leq \bar\eta \lt 1$.** Honest scope: #obs-context-turnover's 100%-reset gives *per-boundary* lossiness ($\eta_k \lt 1$ pointwise). *Uniform* boundedness away from one is an additional stated commitment — a fidelity-ever-improving externalization schedule with $\eta_k \to 1$ satisfies pointwise lossiness yet evades the uniform bar. Write $a_k := \eta_k \rho_k$, a general non-negative sequence.

### The affine information recursion

The mutual-information chain rule gives $I\big((X_k, M_k^+);\, Y\big) = I(M_k^+;Y) + I(X_k;Y \mid M_k^+) = I_k + \rho_k$. Adjoining a variable cannot decrease mutual information, so $I(X_k;Y) \leq I\big((X_k,M_k^+);Y\big) = I_k + \rho_k$.

*[Derived (turnover-affine-recursion, from chain rule + MI-monotonicity; exact)]*

This bound is exact via the chain rule and the monotonicity of mutual information under adjoining variables — it is **not** a sub-additivity claim (mutual information is not sub-additive; the XOR/synergy construction $I(A;Y)=I(B;Y)=0$, $I(A,B;Y)=1$ is the standard counterexample). Composing with (C1):

$$\boxed{\;I_{k+1} \;\leq\; \eta_k\,(I_k + \rho_k) \;=\; \eta_k I_k + a_k, \qquad a_k := \eta_k \rho_k, \qquad \text{and} \quad I_{k+1} \leq B_k \;\text{(budget cap)}.\;}$$

This is the affine information recursion: multiplicative contraction on the carried state plus additive reinjection. The two regimes AAT carries — the intra-session rate regime and this inter-session destroy-and-reconstruct regime — are connected here for the first time, and the connection is a *non*-connection: the recursion is structurally a different recurrence class from the sector dynamics.

### R1 — the no-go (exact under (C1)+(C4); critical path)

For the isolated walk with no reinjection, $a_k \equiv 0$:

*[Derived (turnover-geometric-decay, no-go; exact under (C1)+(C4))]*

$$I_n \;\leq\; \Big(\textstyle\prod_{j=1}^{n} \eta_j\Big)\, I_0 \;\leq\; \bar\eta^{\,n}\, I_0 \;\xrightarrow[n\to\infty]{}\; 0 \quad \text{geometrically.}$$

There is **no inter-session persistence condition**. Persistence is impossible by construction for the self-compressing destroy-and-reconstruct walk; the relevant-information half-life is $\approx 1/\log_2(1/\bar\eta)$ boundaries.

**The sector-persistence template does not transfer.** #result-sector-persistence-template requires (T1) zero correction at zero state, (T2) a local sector condition $\xi^T F(\xi) \geq \alpha\lVert\xi\rVert^2$ in which a correction function $F$ points the state inward, and (T3) a bounded disturbance being rejected by that correction — persistence then reading $\alpha \gt \rho/R$. The destroy-and-reconstruct walk has no perturbation being rejected and no internal restoring term: only multiplicative information decay. No $(\alpha,\rho,R)$ instantiation exists, because the template's structural ingredients have no counterpart in an unforced contraction. The non-transfer is definite, not a scope caveat: it is the resolved answer to whether AAT's persistence apparatus reaches this regime, and the answer is that it does not, by theorem.

### R2 — conditional positive (corollary)

With reinjection, unrolling the affine recursion:

*[Derived (turnover-discounted-sum, from R1 + affine recursion; exact)]*

$$I_n \;\leq\; \bar\eta^{\,n} I_0 \;+\; \sum_{j=1}^{n} \bar\eta^{\,n-j}\, a_j, \qquad\text{hence}\qquad \limsup_{n} I_n \;\leq\; \frac{\bar a}{1-\bar\eta} \quad (\bar a := \limsup_k a_k),$$

and $\liminf_n I_n \gt 0$ **iff** $\liminf_k a_k \gt 0$. Persistence across turnover holds *iff the reinjection channel is non-vanishing*, at level $\bar a/(1-\bar\eta)$. The content, stated plainly because it is the point: persistence is **not intrinsically possessable** by the composite — it is wholly *imported* through the reinjection channel, and the achievable level is reinjection over the contraction gap, not any internal correction outpacing any internal drift. The "persistence condition" here is structural and architectural — *a non-vanishing reinjection channel exists* — categorically not a rate inequality. The positive statement appears only by exhibiting why the destroy-reconstruct structure admits it (an exogenous forcing term), not by assuming the rate regime transfers.

### R3 — the corrected form of the accumulation condition

The discussion-grade accumulation condition this segment replaces presumed *additive* loss with a break-even threshold ($\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$). Under multiplicative contraction that form is not merely unproven but the wrong shape: with any $\bar\eta \lt 1$ and vanishing reinjection, $I_k \to 0$ geometrically however the additive bookkeeping balances. The corrected exact statement is R1+R2 together — persistence $\iff \liminf_k a_k \gt 0$, at level $\bar a/(1-\bar\eta)$; break-even is not the threshold because the loss is multiplicative, not additive.

### What is derived vs. what is committed

| Claim | Status | Source |
|---|---|---|
| Affine recursion $I_{k+1} \leq \eta_k I_k + a_k$ | Exact | Chain rule + MI-monotonicity (no sub-additivity) |
| (C1) multiplicative SDPI contraction | Committed, argued | #obs-context-turnover lossy $f_{\text{init}}$ + SDPI (Ahlswede–Gács 1976; Polyanskiy–Wu) |
| (C4) uniform $\bar\eta \lt 1$ | Committed, argued (pointwise) + stated (uniform) | #obs-context-turnover 100%-reset; uniformity is the additional commitment |
| R1 geometric no-go + non-transfer | Exact given (C1)+(C4) | Product of contraction coefficients; (T1)–(T3) have no counterpart |
| R2 conditional positive, level $\bar a/(1-\bar\eta)$ | Exact given the same | Discounted-geometric-sum |
| R3 corrected accumulation form | Exact (correction of form) | R1+R2; level inherits the matched-channel caveat |
| R4 robustness across (C3)/(C4) sub-models | Robust-qualitative | Argued across the natural sub-models; full generality open (Working Notes) |

## Epistemic Status

*Conditional* — exact given the *argued* commitment (C1) (multiplicative SDPI contraction at the boundary) and (C4) (uniform $\bar\eta \lt 1$, genuine lossiness). The Markov chain $Y \to X_k \to M_{k+1}^+$ is forced by #obs-context-turnover's own exact content — the only thing crossing the boundary is the reconstructed state through $f_{\text{init}}$ — and SDPI is established, adopted machinery (Ahlswede & Gács 1976, "Spreading of sets in product spaces and hypercontraction of the Markov operator," *Ann. Probab.* 4; Polyanskiy & Wu, contraction-coefficient theory), not invented here. The honest tier is therefore *conditional* per FORMAT's definition — exact strength under explicitly named local assumptions beyond the `depends:` chain: the conclusion is exact given the commitment, and the commitment is argued from structure rather than presented as an extracted theorem.

- **R1 (geometric no-go) and the non-transfer of #result-sector-persistence-template: exact** under (C1)+(C4). The non-transfer is verified against what the template's (T1)–(T3) actually require: an unforced multiplicative contraction has neither a correction function nor a disturbance being rejected.
- **R2 (the $\bar a/(1-\bar\eta)$ bound and the $\liminf I_n \gt 0 \iff \liminf a_k \gt 0$ characterization): exact** under the same commitment (standard affine-recursion / discounted-geometric-sum).
- **R3: exact** as a correction of *form*. The numerical *level* $\bar a/(1-\bar\eta)$ inherits the generic rate-distortion floor's matched-channel caveat — the SDPI coefficient $\eta_k$'s tightness is architecture- and matched-channel-dependent — which is the same status #deriv-identity-sufficiency-rate-bound carries as the identity instance of the generic floor (cited here as that instance, not as a prerequisite).
- **R4 (robustness): robust-qualitative.** The R1/R2 dichotomy is invariant across (C3)'s reinjection sub-models (exogenous-stationary / channel-bounded / state-correlated) and (C4)'s stationary-vs-non-stationary driving; those change the *level* and the *regularity* (a.s. vs in-expectation; $\limsup$ vs convergence) but never the qualitative outcome. The invariance is argued across the natural sub-models; a fully general proof over every reinjection model is the remaining open edge.

**The no-go is about *uniformly* lossy turnover.** R1's geometric decay needs $\sup_k \eta_k \leq \bar\eta \lt 1$. The 100%-reset of #obs-context-turnover gives *per-boundary* lossiness ($\eta_k \lt 1$ each $k$), which alone does **not** yield geometric decay: a reconstruction schedule whose fidelity improves without bound across turnovers ($\eta_k \to 1$, contraction weakening toward losslessness) satisfies pointwise lossiness yet evades the uniform bar. The result is stated for uniformly lossy turnover; whether any realizable externalization architecture can sustain $\eta_k \to 1$ against the 100%-reset is the honest scope question, named as an open edge below — the segment must not be read as if per-boundary lossiness alone forces decay.

Max attainable: *exact* for R1/R2/R3 within the argued commitment (already at ceiling — the conditional "(C1)+(C4) $\Rightarrow$ geometric decay / discounted-sum bound" is as strong as SDPI plus affine-recursion algebra); *robust-qualitative* for R4 pending the general-reinjection-model proof.

## Discussion

**The architectural question dominates every modeling-detail question (R4).** The R1/R2 dichotomy is invariant across the reinjection sub-models and the driving process: those parameters set the *level* $\bar a/(1-\bar\eta)$ and the *regularity* of the guarantee, never whether persistence is possible at all. The single question that decides persistence is structural — *does a non-vanishing reinjection channel exist?* — not any rate or threshold quantity. This is the most directly load-bearing consequence for any scaffolded system whose continuity across session boundaries matters: the design effort that buys persistence is the construction and maintenance of the reinjection channel, and no tuning of internal dynamics substitutes for it.

**Why this is a §03.II result.** The reinjection channel *is* the scaffold. #scope-scaffolded-logogenic's defining move is external persistent state $M^{\text{ext}}_t$ carried across session boundaries, realized through the W₁/W₂ wrapping of #der-logogenic-as-wrapping. R1 is the structural argument that this scaffold is not engineering convenience but *provably necessary*: without a non-vanishing reinjection channel, the primitive-logogenic agent's relevant epistemic content decays geometrically to zero by theorem. The primitive sub-scope ( #scope-primitive-logogenic, #obs-context-turnover) is precisely the $a_k \equiv 0$ isolated walk; the scaffolded sub-scope is precisely the regime where $\liminf a_k \gt 0$ can be engineered.

**Relationship to #disc-m-preservation.** That segment frames inter-session persistence as reconstruction adequacy and is correct in its framing; what it lacked was the dynamical reduction *for its own target*. This segment supplies it: the per-boundary predictive-sufficiency adequacy condition iterated under the SDPI-faithful operator gives the affine recursion, and the accumulation question it left open ("is it additive? multiplicative? does it have absorbing states?") is answered for the predictive-sufficiency regime — multiplicative, the break-even additive form is the wrong shape. #disc-m-preservation's discussion-grade accumulation section is superseded **for the predictive-sufficiency accumulation question only**: it is the $\mathcal A_D$ regime — uniformly-lossy contraction of predictive mutual information toward the predictive target. The identity-continuity accumulation question is a *distinct operator on a distinct target* (the reflected, relationally-compensated walk on the identity gap, with a load-bearing $\mu=0$ boundary) and has its own segment, #der-identity-continuity-threshold. The two are not the same object in two normalizations and neither supersedes the other; they sit at opposite ends of the same singular contraction parameter (the $\mathcal A_D$ recursion's norm diverges as the contraction gap closes, which is exactly the reflected walk's load-bearing driftless boundary). #disc-m-preservation carries the cross-reference to the identity-continuity segment for the reader who needs the identity regime.

**Relationship to #result-sector-persistence-template.** The template is the interior facet of the stability certificate — a bounded perturbation rejected by an internal restoring term within capacity. The destroy-and-reconstruct regime has none of those ingredients. This is the cleanest demonstration in the framework that the sector-persistence apparatus is *not* universal across AAT's persistence-flavored questions: it is a rate-regime result, and the inter-session regime is categorically not a rate regime ( #obs-context-turnover states this in its own voice). Surfacing the non-transfer as a first-class derived fact, rather than leaving the inter-session question to look like an unfilled instantiation of the template, is the load-bearing move.

**Two information channels, asymmetric defensibility.** R1+R2 say persistence is imported through reinjection only. For a scaffolded logogenic agent the reinjection channel is the engineered externalization layer — durable artifacts, curated narrative, relational re-attestation. The biological analog ( #disc-m-preservation): morning cognition depends on overnight consolidation quality, not on the previous day's terminal state. The structural sharpening this segment adds is that consolidation quality is not enough on its own — it must be *non-vanishing in the limit*, because any uniformly-lossy schedule with eventually-vanishing reinjection still decays to zero regardless of how good any single consolidation is.

## Working Notes

- **Open edge — the SDPI coefficient $\eta_k$ is not computed for the concrete $f_{\text{init}}$ kernel.** Only $\bar\eta \lt 1$ (genuine lossiness) is argued. Its value, hence the half-life and the level $\bar a/(1-\bar\eta)$, is architecture- and matched-channel-dependent — same status and same openness as #deriv-identity-sufficiency-rate-bound's tightness caveat. Computing $\eta_k$ for a specific reconstruction architecture is a clean follow-on.
- **Open edge — R4's full generality over adversarially-correlated reinjection (the named next spike).** If $\rho_k$ is state-correlated so as to vanish exactly when $I_k$ is low (re-grounding fails precisely when there is little left to re-ground), then $\bar a \gt 0$ marginally is *not* sufficient and R1 can reassert: with $a_k = c\, I_k$ the recursion reads $I_{k+1} \leq (\bar\eta + c) I_k$, still geometric unless $c$ overcomes the gap. This is a candidate *second no-go* — an absorbing-barrier refinement of R2 — and is the single most valuable follow-on. Flagged first-class, not resolved here.
- **Open edge — pointwise vs uniform contraction (the evasion regime).** R1 needs uniform $\bar\eta \lt 1$; an externalization schedule with $\eta_k \to 1$ evades it. Whether any realizable architecture can sustain $\eta_k \to 1$ against the 100%-reset (which plausibly forces a uniform bar) is the honest scope question.
- The budget-cap branch $I_{k+1} \leq B_k$ yields a bottleneck-monotonicity statement as a degenerate special case of R1/R2; subsumed, not separately load-bearing.
- **Open — is R1/R2 a genuinely new $\mathcal A_D$ object, or the bridge-lemma resolvent applied to the turnover channel?** Whether the geometric no-go and the discounted-sum corollary are a new result or an instance of the existing affine-resolvent ($\mathcal A_D$) family (regime-I/II $\varepsilon^\ast(N)$, the bridge lemma) is genuinely open — orthogonal to this landing and not asserted from structural feel (the trigger to test, not assert). It changes only whether this is a standalone segment or a worked instance of the $\mathcal A_D$ family, not the present claims (which are exact within the argued commitment) and not the distinctness from the identity-continuity operator. If it resolves to "subsumed," the segment is honestly demotable to a worked instance later. *(Indexed: `spikes/PROPOSED.md` Tier 3 — "`der-turnover` novelty-vs-subsumed (C10)".)* Reasoning trail: `spikes/.integrated/continuity-persistence/RECONCILIATION.md` §4.
- **Landing context.** Landed from `spikes/continuity-persistence/` (the contraction–reinjection no-go), 2026-05-19; the practica-authored frame is `FRAMING.md` there, the result is `RESULT.md`, independently reviewed (Opus 4.7, 1M; CONCUR with two landing-time fixes applied: the III→IV `depends:` inversion and the eq-(2) chain-rule wording). This segment replaces the discussion-grade accumulation section of #disc-m-preservation per *integration-is-replacement*; see CHANGELOG 2026-05-19. The reasoning trail and the superseded single-branch additive exploration are the spike's history layer, not live references.
- **Tier note (2026-07-14).** `status:` set to `conditional` (was `exact`): (C1)/(C4) are locally-stated commitments beyond the `depends:` chain, and (C4)'s uniformity is not derivable from #obs-context-turnover's pointwise lossiness (the $\eta_k \to 1$ evasion regime above is genuinely open). Upgrade path to `exact`: establish (C4) from the depends chain (resolve the evasion-regime open edge) and move the commitments into `depends:`, per the terminology entry for `conditional`.
- **Promotion-blocking:** depends on #result-sector-persistence-template (exact), #obs-context-turnover (exact-as-observation), #form-information-bottleneck (exact). Strong dependency graph. Open edges above are the strengthening targets; none block the present claims, which are exact within the argued commitment.
