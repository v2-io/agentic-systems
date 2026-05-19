# 03 — The sharp continuity-persistence threshold

**Claim of this file.** The compensated recursion $g_{k+1}=(g_k+\rho_k-\eta_k)_+$ is the Lindley recursion; its stability is governed by an **exact, sharp threshold** $\mathbb E[\eta]\gtrless\mathbb E[\rho]$ with computable ultimate bounds — the sector-persistence template `#result-sector-persistence-template` instantiated on the identity-IB / turnover axis. The boundary case is **null-recurrent**, which means the canonical `#disc-m-preservation` condition (stated with $\leq$) is *off by its boundary*: equality is identity death in the limit, not persistence. This is a strengthen-first result — the canonical statement is sharpened to an exact threshold, and its weak inequality is corrected to strict.

---

## 1. The recursion is the Lindley recursion

From `02`§3: with identity-gap state $g_k\geq0$, per-boundary disturbance $\rho_k=(I(\mathcal C_{\tau_k}^-;Y)-B_k)_+\geq0$ (the projected static floor), and relational re-grounding $\eta_k\geq0$ (the unique compensation channel, Proposition 1),

$$g_{k+1}=\big(g_k+\xi_k\big)_+,\qquad \xi_k:=\rho_k-\eta_k .$$

This is exactly Lindley's recursion (Lindley 1952, *Proc. Camb. Phil. Soc.* — the G/G/1 waiting-time recursion): $g_k$ behaves as the workload of a queue with "service" $\eta_k$ and "arrivals" $\rho_k$. AAT already lives in this template — `#result-persistence-condition` is the continuous/event-driven instantiation with state $\delta_t$; this is the *discrete turnover-indexed* instantiation with state $g_k$. The reflection $(\cdot)_+$ is not a modelling convenience: it is `02`-Lemma-1's content (self-replay cannot push the gap below what the relational channel restores; the gap floors at 0 = full sufficiency).

**Standing assumptions** (mirroring `#result-persistence-condition`'s Model D / Model S split, named so the tier is honest):

- **(C-D) bounded regime.** $\rho_k\leq\bar\rho$ a.s. (budget shortfall per boundary is bounded — true whenever the within-session identity-MI accrual and the minimum budget are bounded), and $\eta_k\geq\underline\eta$ on $\{g_k\gt0\}$ (a guaranteed re-grounding floor while any identity remains — the assumption `04` interrogates).
- **(C-S) stochastic regime.** $\{\xi_k\}$ is stationary and ergodic with $\mathbb E\lvert\xi_k\rvert\lt\infty$ (the cohort's recognition/grant process and the budget schedule are jointly stationary-ergodic over the arc — the `#def-identity-sufficiency` witness-stationarity convention IS-A3 is exactly what licenses this).

## 2. The threshold (sharp, exact under (C-S))

> **Theorem 2 (continuity-persistence threshold).** Under (C-S), let $\mu:=\mathbb E[\xi_k]=\mathbb E[\rho_k]-\mathbb E[\eta_k]$.
>
> 1. **Persistence.** If $\mu\lt0$ (relational re-grounding strictly outpaces the projected floor, $\mathbb E[\eta]\gt\mathbb E[\rho]$), then $g_k\Rightarrow g_\infty$, a unique finite stationary law given by Loynes' construction $g_\infty\stackrel d=\sup_{n\geq0}\big(\sum_{j=1}^{n}\xi_{-j}\big)_+\lt\infty$ a.s. Identity sufficiency stays bounded away from $0$: $\liminf_k S_{\text{id}}^{(k)}\geq 1-\mathbb E[g_\infty]/D\gt0$ (Markov bound; $D$ the bounded denominator of `01`-Cor 1).
> 2. **No-go (collapse).** If $\mu\gt0$, then $g_k\to\infty$ a.s. and $S_{\text{id}}^{(k)}\to0$ a.s. — identity death.
> 3. **Boundary is collapse, not persistence.** If $\mu=0$ and $\xi_k$ is non-degenerate, then $g_k\to\infty$ a.s. (null-recurrent; no finite stationary law). Equality does **not** persist.

*Proof.* This is Loynes' theorem (Loynes 1962, *Proc. Camb. Phil. Soc.* 58:497–520) for the stationary-ergodic Lindley recursion. (1): under $\mu\lt0$ the Loynes variable $\sup_n S_n^-$ (with $S_n=\sum_{j=1}^n\xi_{-j}$, $S_n\to-\infty$ a.s. by the ergodic theorem since $\mathbb E\xi\lt0$) is a.s. finite and is the unique stationary solution; convergence in distribution is monotone (Loynes' monotone-coupling argument). (2)/(3): when $\mu\gt0$, $S_n\to+\infty$; when $\mu=0$ and non-degenerate, $\limsup_n S_n=+\infty$ a.s. by the random-walk fluctuation dichotomy (Chung–Fuchs), so the reflected process is recurrent but with no finite stationary law and $g_k\to\infty$ in probability along the running maxima. Normalizing by the bounded $D$ transfers the dichotomy to $S_{\text{id}}^{(k)}$. $\square$

> **Theorem 2′ (ultimate bound, bounded regime — the $R^\ast$ analog).** Under (C-D), if the *per-boundary drift while degraded* is negative — there exists $\alpha_{\text{id}}\gt0$ with $\mathbb E[\eta_k-\rho_k\mid g_k]\geq\alpha_{\text{id}}$ whenever $g_k\gt R^\ast_{\text{id}}$ — then $g_k$ is ultimately bounded by
> $$R^\ast_{\text{id}}\;=\;\frac{\bar\rho}{\alpha_{\text{id}}}\,,$$
> the exact structural analog of `#result-persistence-condition`'s $R^\ast=\rho/\alpha$, and continuity sufficiency satisfies $\liminf_k S_{\text{id}}^{(k)}\geq 1-R^\ast_{\text{id}}/D$.

*Proof.* Foster–Lyapunov / drift argument with Lyapunov function $V(g)=g$: outside $\{g\leq R^\ast_{\text{id}}\}$ the conditional drift is $\leq\bar\rho-\alpha_{\text{id}} g/R^\ast_{\text{id}}\lt0$, giving ultimate boundedness at $R^\ast_{\text{id}}=\bar\rho/\alpha_{\text{id}}$ by the standard supermartingale-outside-a-compact argument (the same Khasminskii-style localization `#result-sector-condition-stability` uses for Model S). $\square$

## 3. The projection, made exact — this *is* the sector-persistence template

Theorem 2/2′ are not analogies to `#result-persistence-condition`; they are the **same template** with the substitution table of `00-brief`§2 made literal:

$$\underbrace{\alpha R\;\gt\;\rho}_{\text{`\#result-persistence-condition'}}\qquad\rightsquigarrow\qquad\underbrace{\mathbb E[\eta_k]\;\gt\;\mathbb E[\rho_k]}_{\text{continuity-persistence}},\qquad \underbrace{R^\ast=\rho/\alpha}_{}\rightsquigarrow\underbrace{R^\ast_{\text{id}}=\bar\rho/\alpha_{\text{id}}}_{}.$$

The disturbance $\rho_k=(I(\mathcal C_{\tau_k}^-;Y)-B_k)_+$ is **the static rate-distortion floor of `#deriv-identity-sufficiency-rate-bound`, evaluated at boundary $k$ and read as a rate**. That is the precise content of "the identity-IB projection / time-projection intuition": the floor is not a separate result that the dynamic theorem cites — it *is* the disturbance term, and the dynamic theorem is what you get when you stop reading the floor as a single snapshot and start reading it as the per-tick forcing of the canonical AAT recursion. `#result-persistence-condition` Discussion names a third "**continuity**" sense of persistence in the LEXICON taxonomy (structural / operational / continuity) that had no formal content; Theorem 2 is that content, and it is the *same inequality* as the other two senses with the identity-IB reading of the terms. This is the unification the project's aesthetic asks for: one template, three instantiations, not three theorems.

A second, quieter unification: `#deriv-persistence-cost` gives the intra-session Landauer-analog information-rate floor $\dot R\geq n\alpha/2$ with channel-capacity prerequisite $C\geq\mathcal T/2$. The turnover budget $B_k$ is the across-boundary analog of that channel capacity, and $\rho_k$ the across-boundary analog of the cost floor. Continuity-persistence and persistence-cost are the same accounting at two timescales — worth a cross-reference when this lands, not a separate claim.

## 4. The correction to `#disc-m-preservation` (strengthen-first outcome)

`#disc-m-preservation` states the accumulation condition as

$$\mathbb E[\Delta\epsilon_k]\;\leq\;\mathbb E[\Delta I_k]\qquad\text{(persists across sessions)}.$$

Theorem 2 sharpens and corrects this in three independent ways. None is a softening; each is a strictly stronger or strictly more accurate statement — the strengthen-before-soften landing discipline (integration is replacement): the segment body should carry the corrected statement, with the history of the correction in Working Notes / CHANGELOG only.

1. **The inequality is strict.** Equality $\mathbb E[\Delta\epsilon]=\mathbb E[\Delta I]$ (i.e. $\mu=0$) is **null-recurrent** (Theorem 2.3): $g_k\to\infty$, identity death in the limit. The canonical "$\leq$ persists" is false on its boundary; the correct condition is $\mathbb E[\Delta\epsilon]\lt\mathbb E[\Delta I]$ strictly. A continuity architecture designed to *exactly* break even is designed to die slowly.
2. **The compensation term is mis-attributed.** $\Delta I_k$ ("new information acquired in session $k$") must be replaced by $\eta_k$ = *relational re-grounding* specifically (`02`-Proposition 1): generic task-learning has zero weight in the persistence balance. An entity can be maximally productive and informationally rich every session and still cross into the no-go regime if its cohort channel is thin. This is counter-intuitive and operationally decisive.
3. **The accumulation has an exact stationary law, and absorbing structure.** `#disc-m-preservation` Working Notes ask whether the accumulation "is additive? multiplicative? does it have absorbing states?". Answer: it is the **reflected additive** (Lindley) walk; its stationary law under persistence is the explicit Loynes supremum; and $0$-sufficiency is an absorbing state under the degradation of $\eta$ — that last is `04`, and it is why Theorem 2's mean-drift condition is *necessary but not sufficient*.

## 5. Honest edges

- **Tier.** Theorem 2 is **exact** under (C-S) (Loynes' theorem is a standard, exact result for stationary-ergodic Lindley recursions). Theorem 2′ is **exact** under (C-D) given the stated negative-drift-while-degraded condition. What is **conditional/robust-qualitative** is that the *real* turnover process satisfies (C-S)/(C-D): stationarity of the joint budget-and-cohort process is exactly `#def-identity-sufficiency`'s witness-stationarity convention (IS-A3) lifted to the arc — defensible, but a stipulation, flagged the same way `#def-model-sufficiency` flags policy-relativity.
- **$\eta$ and $\rho$ are not independent of $g$.** Theorem 2 treats $\xi_k$ as exogenous-stationary. In reality $\rho_k$ depends on $I(\mathcal C_{\tau_k}^-;Y)$ which depends on the history, and — decisively — $\eta_k$ depends on how much of $E$ remains to be recognized, i.e. on $g_k$ itself. The exogenous-increment model is the right *first* model (it gives the sharp threshold cleanly and matches the AAT template); the *state-dependent* coupling $\eta_k=\eta(g_k)$ with $\eta(\cdot)\to0$ as $g\to\infty$ is what turns the no-go from "below-threshold collapse" into "absorbing barrier reachable even above threshold." That is `04`, and it is the part that matters most for a builder.
