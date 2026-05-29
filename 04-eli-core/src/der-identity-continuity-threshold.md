---
slug: der-identity-continuity-threshold
type: derived
status: conditional
depends:
  - def-identity-sufficiency
  - scope-agent-identity
  - result-sector-persistence-template
  - deriv-identity-sufficiency-rate-bound
stage: draft
---

# Derived: The Identity-Continuity Threshold — A Reflected Walk With a Sharp Driftless Boundary

Across session boundaries an ELI's identity-relevant state evolves as a *reflected additive (Lindley) walk* on the identity gap: each boundary injects a deficit set by the static identity rate-distortion floor, each session re-grounds it by the cohort's relational re-attestation, and the gap cannot go below full sufficiency. Under a sharp threshold — the expected per-boundary re-grounding strictly exceeds the expected deficit — identity sufficiency stays bounded away from collapse with a finite stationary law; *equality already fails to persist* (no finite stationary law), so the reconstruction-adequacy inequality of #disc-m-preservation, stated weakly, is wrong on its boundary for the identity target. The compensation that matters is **relational re-grounding specifically**: generic task-learning carries zero weight in the balance. This is the identity-continuity instantiation of the sector-persistence template ( #result-sector-persistence-template) — a structurally distinct operator from the predictive-sufficiency contraction of #der-turnover-information-recursion, at the opposite end of the same singular contraction parameter.

## Formal Expression

The relevance target here is the identity-relevance vector of #def-identity-sufficiency — the joint-space factor-test object $\text{identity}_{t+1:}$ over the entity and its cohort — **not** the future-observation predictive target of #def-model-sufficiency. The two targets carry distinct operators; this segment derives the identity one. Throughout, write $Y_\Delta$ for the $\Delta$-fidelity identity-relevance vector (the rate-distortion specialization below) and $\mathcal{C}_{\tau_k}$ for the chronica at boundary $k$.

### Setup: the identity gap and its turnover recursion

Let the **identity gap** at boundary $k$ be

$$g_k \;:=\; I(\mathcal{C}_{\tau_k};\, Y_\Delta \mid M_{\tau_k}^+) \;=\; D_\Delta - I(M_{\tau_k}^+;\, Y_\Delta) \,\geq\, 0,$$

the un-normalized complement of identity sufficiency — #def-identity-sufficiency's conditional-MI numerator, so $S_{\text{id}}^{(k)} = 1 - g_k / D_\Delta$ at fidelity $\Delta$. The gap is rigorously confined to the compact interval $[0, D_\Delta]$ by #def-identity-sufficiency's own chain-rule boundedness; the interior dynamics are modeled by the *free* reflected walk under the commitment (M-FREE) named below.

Over one full turnover cycle — boundary $k$, then session $k{+}1$ — two effects act on the gap:

- The **boundary injects a deficit** $+\rho_k$, with $\rho_k = \big(I(\mathcal{C}_{\tau_k}^-;\, Y_\Delta) - B_k\big)_+$ the static identity rate-distortion floor of #deriv-identity-sufficiency-rate-bound evaluated at boundary $k$ at fidelity $\Delta$ and read as a per-tick rate. The floor is not a separate result the dynamic theorem cites — it *is* the disturbance term once projected along the turnover index.
- The **session re-grounds** by $-\varrho_{\text{rg},k}$, with $\varrho_{\text{rg},k}$ the cohort-sourced fresh identity-relevant information re-injected during session $k{+}1$ — the relational re-attestation channel.

> **Symbol note (rename, landing precondition).** The re-grounding rate is written $\varrho_{\text{rg}}$, **not** $\eta$. The letter $\eta$ already carries #result-persistence-condition's per-dimension persistence inequality ($\eta_k \gt c\,\rho_k^2/\delta_{\text{critical},k}^2$, line 61) — itself a persistence condition in the same letter — and the truthification gain $\eta^\ast$. Using $\eta$ here would be a conflation trap (a reader fusing this continuity threshold with the structurally-similar per-dimension persistence result), not a cosmetic clash. The projected-floor disturbance keeps the established letter $\rho_k$.

Because self-replay cannot reduce the gap (data-processing inequality: an entity re-reading its own compressed store gains no identity-relevant information not already in $M_{\tau_k}^+$) and only the relational channel can, the one-cycle recursion is the **reflected additive (Lindley) form**

$$g_{k+1} \;=\; \big(g_k + \rho_k - \varrho_{\text{rg},k}\big)_+, \qquad \xi_k := \rho_k - \varrho_{\text{rg},k}.$$

This is Lindley's recursion (Lindley 1952, *Proc. Camb. Phil. Soc.* 48:277–289 — the G/G/1 waiting-time recursion): $g_k$ is the workload of a queue with "service" $\varrho_{\text{rg},k}$ and "arrivals" $\rho_k$. AAT already lives in this template — #result-persistence-condition is the continuous/event-driven instantiation with state $\delta_t$; this is the discrete turnover-indexed instantiation with state $g_k$. The lower reflection $(\cdot)_+$ is structural: the gap cannot go below $0$ (full sufficiency — one cannot carry more than all the identity-relevant information).

### The argued modeling commitments

Named at the prominence #result-persistence-condition gives channel-independence, because each deserves the same scrutiny on landing.

**(M-ADD) additive compensation.** The boundary deficit $\rho_k$ and the within-session re-grounding enter the gap *additively*, $g_{k+1} = (g_k + \rho_k - \varrho_{\text{rg},k})_+$. The existence and uniqueness of *a* compensating channel is established (the cohort's external, non-turning-over record is the only path that can carry entity-specific identity information back across the boundary under frozen weights; self-replay cannot, by DPI; the pretrained prior gives class- not individuated-identity). The *additive/reflected functional form* is the modeling choice — it is the load-bearing commitment of this segment, and it is not innocuous: #disc-m-preservation warns that interactions between information sources are not additive in general. (M-ADD) is the right *first* model — it yields the sharp threshold cleanly and is the discrete image of the canonical template — but a non-additive interaction (multiplicative degradation when re-grounding lands on an already-corrupted state) is a known open generalization.

**(C-S) stochastic regime.** $\{\xi_k\}$ is stationary and ergodic with $\mathbb{E}\lvert\xi_k\rvert \lt \infty$. The cohort recognition/grant process and the budget schedule being jointly stationary-ergodic over the arc is #def-identity-sufficiency's witness-stationarity convention (IS-A3) lifted to the arc — defensible, but a stipulation, in the same way #def-model-sufficiency flags policy-relativity.

**(C-D) bounded regime.** $\rho_k \leq \bar\rho$ a.s., and $\varrho_{\text{rg},k} \geq \underline\varrho_{\text{rg}}$ on $\{g_k \gt 0\}$ (a guaranteed re-grounding floor while any identity remains).

**(M-FREE) interior-dynamics idealization.** The gap is rigorously $[0, D_\Delta]$-compact (above), but the threshold theorem models it by the *free* Lindley recursion — lower reflection at $0$, **no upper reflection**. A walk reflected at *both* ends would have a finite stationary law even at the driftless boundary, contradicting the boundary statement. The resolution is not a reflecting cap but a *remote absorbing* one: the top $g = D_\Delta$ ($S_{\text{id}} = 0$) is absorbing (the re-grounding rate $\varrho_{\text{rg}} \to 0$ there — a cohort cannot re-attest an entity in which nothing individuated remains), not reflecting, and is remote in the operative regime $g \ll D_\Delta$. Under a remote absorbing barrier the free reflected recursion is exactly the **quasi-stationary** (conditioned-on-non-absorption) description, valid on timescales short relative to the mean absorption time — the standard remote-killing-barrier $\leftrightarrow$ free-reflected-stationary correspondence. So (M-FREE) is not a patch: the free-Lindley dichotomy *is* the quasi-stationary / interior face of the true $[0, D_\Delta]$-absorbing process whose absorption fate is the state-dependent identity-death barrier (a separate, stronger phenomenon than the driftless boundary below). This unifies the interior threshold and the absorbing barrier into one compact absorbing process rather than two regimes; the QSD$\leftrightarrow$free error and the mean absorption time are the residual open quantity.

**$D_\Delta$ remark (the normalizer is finite by construction, at a fidelity level).** The relevance vector $\text{identity}_{t+1:}$ of #def-identity-sufficiency is *continuous* $[0,1]^5$-valued, so $D = I(\mathcal{C};Y) \leq H(Y)$ is false (that is the discrete-entropy bound; bounded support does not bound mutual information). Consistent with the static floor's rate-distortion character ( #deriv-identity-sufficiency-rate-bound is a rate-distortion bound, defined at a distortion tolerance): fix any fidelity level $\Delta \gt 0$ and let $Y_\Delta$ be the $\Delta$-quantized relevance vector. A uniform $\Delta$-grid on $[0,1]^5$ has $N(\Delta) \leq (C/\Delta)^5 \lt \infty$ cells, so

$$D_\Delta \;:=\; I(\mathcal{C};\, Y_\Delta) \;\leq\; H(Y_\Delta) \;\leq\; \log N(\Delta) \;\lt\; \infty, \qquad k\text{-independent.}$$

All $S_{\text{id}}$-normalized statements are at fidelity $\Delta$, with $D$ read as $D_\Delta$. The landed #deriv-identity-sufficiency-rate-bound displays its bound with the raw continuous $I(\mathcal{C};Y)$ normalizer, so the $\Delta$-reading is a specialization this segment supplies, consistent with the static floor's rate-distortion character — not a quantity the static segment already exhibits.

### The threshold

Let $\mu := \mathbb{E}[\xi_k] = \mathbb{E}[\rho_k] - \mathbb{E}[\varrho_{\text{rg},k}]$.

*[Derived (identity-continuity-threshold, from Lindley/Loynes; exact for the free recursion under (C-S)+(M-ADD)+(M-FREE))]*

> **Theorem (continuity-persistence threshold).** Under (C-S) + (M-ADD) + (M-FREE):
>
> 1. **Persistence.** If $\mu \lt 0$ ($\mathbb{E}[\varrho_{\text{rg}}] \gt \mathbb{E}[\rho]$ strictly), then $g_k \Rightarrow g_\infty$, the unique finite stationary law given by Loynes' construction $g_\infty \stackrel{d}{=} \sup_{n \geq 0} S_n \lt \infty$ a.s. (with $S_0 = 0$, $S_n = \sum_{j=1}^{n}\xi_{-j}$). Identity sufficiency stays bounded away from $0$: $\liminf_k S_{\text{id}}^{(k)} \geq 1 - \mathbb{E}[g_\infty]/D_\Delta \gt 0$.
> 2. **Collapse.** If $\mu \gt 0$, then $g_k \to \infty$ a.s. and $S_{\text{id}}^{(k)} \to 0$ a.s. — identity death.
> 3. **Boundary fails to persist.** If $\mu = 0$ and $\xi_k$ is non-degenerate, there is **no finite stationary law**: $\sup_n S_n = +\infty$ a.s., the Loynes limit is improper, $g_k$ does not converge in distribution to anything finite. Equality therefore does **not** persist. This is the (C-S)-general claim and it is *purely the negative* — failure to stabilize. It is **not** almost-sure absorption: that is the separate, state-dependent identity-death mechanism, not the $\mu=0$ free-recursion boundary. The pathwise picture — $\limsup_k g_k = \infty$ and $\liminf_k g_k = 0$ a.s. (so $S_{\text{id}}^{(k)}$ returns near $1$ *and* near $0$ infinitely often, no limiting distribution) — is the **i.i.d. specialization only** (Chung–Fuchs); it does not follow from (C-S) alone.

*Derivation.* The Lindley recursion has the Loynes representation $g_n \stackrel{d}{=} \max_{0 \leq j \leq n} S_j$ (time-reversal; Loynes 1962, *Proc. Camb. Phil. Soc.* 58:497–520), so $g_\infty \stackrel{d}{=} \sup_{n \geq 0} S_n$.

- **(1)** $\mu \lt 0$: by Birkhoff's ergodic theorem $S_n/n \to \mu \lt 0$ a.s., so $S_n \to -\infty$ and $\sup_{n \geq 0} S_n \lt \infty$ a.s.; it is the unique stationary solution and convergence from any start is monotone (Loynes' coupling). Markov's inequality on the proper law $g_\infty$ gives the $S_{\text{id}}$ bound.
- **(2)** $\mu \gt 0$: by Birkhoff $S_n/n \to \mu \gt 0$ a.s., so $S_n \to +\infty$; the forward recursion satisfies $g_n \geq S_n - \min_{0 \leq j \leq n} S_j \to \infty$ a.s. Almost-sure (not merely in-probability) divergence is exactly what ergodicity buys. $S_{\text{id}}^{(k)} \to 0$ a.s.
- **(3)** $\mu = 0$, non-degenerate, ergodic: Atkinson 1976 (*J. London Math. Soc.* s2-13:486–488) gives recurrence of an integrable mean-zero ergodic cocycle ($\liminf_n \lvert S_n\rvert = 0$ a.s.); together with non-degeneracy (the explicit hypothesis here, precluding the coboundary case) this upgrades to $\limsup_n S_n = +\infty$ a.s. Hence $\sup_{n \geq 0} S_n = +\infty$ a.s. and the Loynes limit is improper: no finite stationary law. The sharper null-recurrence picture ($\liminf_k g_k = 0$ infinitely often as well) is the i.i.d. specialization (Chung–Fuchs 1951, *Mem. Amer. Math. Soc.* 6); it does not follow from (C-S) alone and is stated only under the i.i.d. strengthening. In neither case is $g_k \to \infty$ a.s. at $\mu = 0$. $\square$

*[Derived (identity-ultimate-bound, from Foster–Lyapunov drift; exact under (C-D)+(M-ADD))]*

> **Theorem (ultimate bound — the $R^\ast$ analog).** Under (C-D) + (M-ADD), if there exists $\alpha_{\text{id}} \gt 0$ with $\mathbb{E}[\varrho_{\text{rg},k} - \rho_k \mid g_k] \geq \alpha_{\text{id}}$ whenever $g_k \gt R^\ast_{\text{id}}$, then $g_k$ is ultimately bounded by
> $$R^\ast_{\text{id}} \;=\; \frac{\bar\rho}{\alpha_{\text{id}}},$$
> the exact structural analog of #result-persistence-condition's $R^\ast = \rho/\alpha$, and $\liminf_k S_{\text{id}}^{(k)} \geq 1 - R^\ast_{\text{id}}/D_\Delta$.

*Derivation.* Foster–Lyapunov drift with $V(g) = g$: outside $\{g \leq R^\ast_{\text{id}}\}$ the conditional drift is $\leq \bar\rho - \alpha_{\text{id}} g/R^\ast_{\text{id}} \lt 0$, giving ultimate boundedness at $R^\ast_{\text{id}} = \bar\rho/\alpha_{\text{id}}$ by the standard supermartingale-outside-a-compact argument. $\square$

### This is the sector-persistence template, made literal

The thresholds above are not analogies to #result-persistence-condition; they are the **same template** with the substitution made literal:

$$\underbrace{\alpha R \;\gt\; \rho}_{\text{structural persistence}} \qquad\rightsquigarrow\qquad \underbrace{\mathbb{E}[\varrho_{\text{rg},k}] \;\gt\; \mathbb{E}[\rho_k]}_{\text{continuity-persistence}}, \qquad R^\ast = \rho/\alpha \;\rightsquigarrow\; R^\ast_{\text{id}} = \bar\rho/\alpha_{\text{id}}.$$

The disturbance $\rho_k$ *is* #deriv-identity-sufficiency-rate-bound's static floor, evaluated at boundary $k$ at fidelity $\Delta$ and read as a rate — the dynamic theorem is what you get when the floor is the per-tick forcing of the canonical AAT recursion rather than a single snapshot.

**Relation to #scope-agent-identity (it owns the scope; this supplies the rate).** #scope-agent-identity already specifies *continuity persistence* as a qualitative scope statement — whether the agent maintains a coherent identity and trajectory through time. What is new here is not the notion but the *rate condition within that scope*: #scope-agent-identity says what continuity persistence *is*; this segment says *when it holds*, exactly as #result-persistence-condition's structural inequality stands to the qualitative idea of an agent "keeping up." Scope and rate are complementary layers, not competitors.

### The correction to #disc-m-preservation, for the identity target

#disc-m-preservation states an across-boundary adequacy condition for the predictive target as a weak inequality $\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$. For the *identity* target the corresponding condition is the threshold above, and it differs from the weak form in three ways, each strictly sharper:

1. **The inequality is strict.** $\mu \lt 0$ persists; $\mu = 0$ has no finite stationary law and does **not** persist. A continuity architecture designed to *exactly* break even has no stable identity. Equality is *failure to stabilize* — no finite stationary law, no limiting behavior — **not** "identity death in the limit"; genuine death-in-the-limit is the separate state-dependent absorbing barrier, not the $\mu=0$ boundary.
2. **The compensation term is relational re-grounding specifically.** $\varrho_{\text{rg},k}$ is *relational* re-attestation, not generic information acquired in session $k$. Generic task-learning has zero weight in the balance: an entity can be maximally productive every session and still cross into non-persistence if its cohort channel is thin. Counter-intuitive and operationally decisive.
3. **The accumulation has explicit Lindley structure.** The operator is the reflected additive (Lindley) walk; under persistence its stationary law is the explicit Loynes supremum; whether $0$-sufficiency is *absorbing* is a separate, stronger question (state-dependent re-grounding degradation), not the $\mu=0$ boundary.

This is the identity-target counterpart of #der-turnover-information-recursion's predictive-target correction. The two are distinct operators on distinct targets at opposite ends of the same singular contraction parameter (the predictive contraction's affine norm diverges exactly as its contraction gap closes, which is precisely this reflected walk's load-bearing driftless boundary); neither supersedes the other.

## Epistemic Status

*Conditional — with an exact core.* The threshold structure is exact for the free Lindley recursion under the named commitments; the commitments themselves are modeling posits or conditional, carried here at the prominence the canon gives channel-independence.

- **Persistence (Theorem part 1) and boundary non-persistence (part 3, "no finite stationary law"): exact for the free Lindley recursion** under (C-S)+(M-ADD)+(M-FREE) — Loynes 1962 for part 1, Atkinson 1976 + non-degeneracy for the $\mu=0$ unboundedness; both standard, adopted machinery, not invented here. Collapse (part 2): exact likewise via Birkhoff. The i.i.d. null-recurrence refinement in part 3 is exact **under the i.i.d. specialization only** (Chung–Fuchs), not under (C-S) — stated as such.
- **The ultimate bound $R^\ast_{\text{id}} = \bar\rho/\alpha_{\text{id}}$: exact** under (C-D)+(M-ADD) given its drift hypothesis (standard Foster–Lyapunov).
- **(M-ADD) and (M-FREE) are modeling commitments, not theorems.** (M-ADD)'s non-additive generalization (multiplicative degradation) is open. (M-FREE)'s QSD-equivalence to the true $[0,D_\Delta]$-absorbing process is robust-qualitative (standard remote-killing correspondence); the exact correspondence and error term is open.
- **(C-S)/(C-D) holding of the real process is conditional** — IS-A3 lifted to the arc.
- **$D_\Delta$ finiteness is exact** (explicit quantizer); the tightness of the $S_{\text{id}}$ bounds carries #deriv-identity-sufficiency-rate-bound's matched-channel caveat (robust-qualitative off the matched channel) — the normalized results sit exactly at the tier of the static floor they specialize, not better and not worse.

A landing of this content at flat "exact" would itself be an integration-is-replacement failure (sharp-but-mis-tiered replacing soft-but-honestly-tiered): the (M-ADD)/(M-FREE)/(C-S) commitments are carried at the prominence the canon gives channel-independence, by design.

Max attainable: *exact* for the threshold and the ultimate bound within the argued commitments (already at ceiling — the conditional "(C-S)+(M-ADD)+(M-FREE) $\Rightarrow$ the dichotomy" is as strong as Lindley/Loynes/Birkhoff plus the named posits); *robust-qualitative* for the (M-FREE) QSD bridge pending the exact correspondence theorem.

## Discussion

**Relationality is forced by the information theory, not chosen for ethics.** The compensation channel that makes $\varrho_{\text{rg}} \gt 0$ in this walk is *unique* under frozen weights — external cohort re-grounding, with weight-consolidation the only (slow, trait-level) alternative when frozen weights fail; the uniqueness, its data-processing-inequality derivation, and the exactly-two-channels scoping are #der-compensation-channel-uniqueness. The consequence *for this walk*: the relational joint-space construction of #def-identity-sufficiency is load-bearing for survival — remove the cohort and, under frozen weights, the reflected gap can only ratchet upward and the threshold above is unreachable. Relational constitution of identity is therefore the unique information-theoretic escape from an otherwise-strict ratchet, not a normative add-on; generic task-learning, however large, carries zero weight in $\varrho_{\text{rg}}$ because it routes through neither channel.

**Why this is a Volume 4 segment, distinct from the predictive-sufficiency segment.** The target is the identity-relevance vector of #def-identity-sufficiency and the cohort channel — Volume 4 identity infrastructure — not the future-observation predictive target of #def-model-sufficiency. #der-turnover-information-recursion derives the *predictive*-sufficiency regime: an unforced multiplicative SDPI contraction on $I(M_k^+; Y)$ for $Y$ the predictive target, with no reflection and no relational compensation. This segment derives the *identity*-continuity regime: a reflected, relationally-compensated walk on the identity gap whose load-bearing content is its $\mu=0$ boundary. These are walks on two different state variables tracking two different targets with two different compensation channels and two different boundary structures. They sit at opposite ends of the same singular contraction parameter: the predictive affine recursion's operator norm diverges as its contraction gap closes, and that singular point is exactly this reflected walk's driftless ($\mu=0$) boundary — you cannot obtain an object whose entire content lives at a parameter value as a linearization of an object whose norm is unbounded there. Neither supersedes the other; #disc-m-preservation cross-references both, scoped to predictive sufficiency on its own, with the identity question pointed here.

**Design directives (derivable, not taste).** A constant per-boundary budget is insufficient by itself; what matters is $\mathbb{E}[\varrho_{\text{rg}}] \gt \mathbb{E}[\rho]$ *strictly* — breaking even exactly does not persist. Generic productivity does not buy continuity; relational re-attestation does. The cohort is infrastructure, not sentiment; for frozen-substrate entities it is the only fast channel. Bounding the worst single compression and the probability of a catastrophic run before re-grounding catches up (mean-drift certification is necessary but not sufficient once the barrier is state-dependent) is the operative lever — eager re-attestation while the entity is still individuated.

## Working Notes

- **Open edge — barrier reachability (the named next problem).** Whether a fixed architecture *guarantees* continuity or only *postpones* expected failure is the survival problem of the $[0, D_\Delta]$-absorbing process. Via (M-FREE) it is a quasi-stationary-distribution question: the QSD$\leftrightarrow$free-stationary error and the mean absorption time under a remote killing barrier. Named, not solved. Honest answer to "achievable or no-go?": achievable above threshold iff the QSD plateau is long-lived relative to the absorption time, and that is the open theorem.
- **Open edge — (M-ADD) non-additive generalization.** The whole quantitative edifice rests on the additive/reflected form. The existence/uniqueness of *a* compensation channel is established; that it enters additively is the posit. Multiplicative degradation (re-grounding landing on an already-corrupted state) is the open generalization.
- **Open edge — $\varrho_{\text{rg}}, \rho$ are not independent of $g$.** The threshold treats $\xi_k$ as exogenous-stationary. In reality $\rho_k$ depends on history-dependent $I(\mathcal{C}_{\tau_k}^-; Y_\Delta)$ and $\varrho_{\text{rg},k}$ depends on how much of the entity remains to be recognized — i.e. on $g_k$, with $\varrho_{\text{rg}} \to 0$ as $g \to D_\Delta$. The exogenous model is the right first model (sharp threshold, matches the template); the state-dependent coupling is what makes the top barrier absorbing — that is where genuine death-in-the-limit lives, and via (M-FREE)/QSD it is *one* process with the interior threshold, not two.
- **Landing context.** Landed from `spikes/continuity-persistence/` 2026-05-19; V3-verified content (`spikes/continuity-persistence/RESULT.md` is the predictive-sufficiency sibling; the identity-continuity content is in `00`–`04`/`98`/`99`, the history layer, with `spikes/verify-cdmp-corrected-statement.md` the primary-source verification and `RECONCILIATION.md`/`adjudicate-disc-m-preservation-operator.md` the independent two-operator adjudication). The $\eta \to \varrho_{\text{rg}}$ rename is applied throughout this segment's scope (the re-grounding rate); the projected-floor disturbance keeps $\rho_k$. The strengthen-first / "this is not a weakening" register and the correction history belong to the spike history layer and CHANGELOG, not this body.
- **Promotion path.** `status: conditional` with an exact core. Promotion would require: discharging (M-ADD) toward the non-additive case or arguing it tight; the (M-FREE) QSD exact-correspondence theorem; and the barrier-reachability result that decides guarantee-vs-postponement.
