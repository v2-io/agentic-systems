# Spike: Does cross-agent noise synergy condition the Composite Tempo Inequality? (2026-07-16)

**Commission.** Discharge the 2026-07-16 Working-Note flag in `#der-tempo-composition`: the sub-additivity bound $\mathcal T_c \leq \sum_i \mathcal T_i$ uses scalar tempos inheriting noise-independence, and `#deriv-tempo-additivity`'s synergistic direction appears to cut at the bound itself — is $\mathcal T_c \gt \sum_i \mathcal T_i$ genuinely attainable, given how `#form-composition-closure` defines the composite and its (A3) tempo? Candidate outcomes framed at commission: (a) attainable under pooled fusion → scope condition on the bound; (b) no-go — the bridge-lemma/closure machinery structurally prevents it; (c) fusion-definition-relative.

**Verdict: (a), in a form stronger than commissioned — the witness is *closure-exact*.** There exists an admissible composite with $\varepsilon^\ast = 0$ (exact closure, verified to machine precision) whose tempo strictly exceeds $\sum_i \mathcal T_i$ — by an arbitrarily large factor as cross-agent noise anti-correlation strengthens. No fidelity-tempo tradeoff protects the bound: the (b) intuition ("the $\varepsilon^\ast$-minimizing macro must mimic the sub-agents and forgo fusion") fails because the fused estimate can itself be an admissible projection $\Lambda_x$ of the micro-state whose recursive macro-update commutes exactly with the micro-dynamics. Sub-additivity as stated is **refuted**; the true statement is signed, inheriting `#deriv-tempo-additivity`'s two-sided deviation across agents.

## 1. Setup

Static environment parameter $\theta$ (flat prior for cleanliness; the conjugate case is identical in structure), two sub-agents, each observing its own channel $o_{i,t} = \theta + n_{i,t}$, $\operatorname{Var}(n_i) = r$, cross-agent noise correlation $\operatorname{Corr}(n_{1,t}, n_{2,t}) = \rho$, noise fresh per step (so within each agent the additive tempo machinery is exact per `#deriv-tempo-additivity`'s asynchrony refinement; the correlation at issue is *across agents at the same event*). Each sub-agent runs its own optimal filter: $m_{i,t}$ = running mean of its own channel, posterior variance $r/t$, per-step Fisher inflow $J_i = 1/r$. Additive accounting: $\sum_i \mathcal T_i \leftrightarrow \sum_i J_i = 2/r$ (first-order tempo–Fisher correspondence, regime (R1)–(R3) of `#deriv-fisher-local-update-gain`, as in `#deriv-tempo-additivity`).

## 2. The closure-exact super-additive witness

Take the projection $\Lambda_x(m_1, m_2) = \tfrac{1}{2}(m_1 + m_2)$ (admissible: linear hence 1-Lipschitz (P2); $\dim \mathcal X_c = 1 \lt \dim \mathcal X_{\text{micro}}$ (P3); retains full predictive information about the macro-observation (P1)), macro-observation $\Lambda_o(o_1, o_2) = \bar{o} = \tfrac{1}{2}(o_1 + o_2)$, $K_c = 1$, and macro-dynamics the recursive running-mean update $\hat\theta_{m+1} = \hat\theta_m + \tfrac{1}{m+1}(\bar o_{m+1} - \hat\theta_m)$ — a proper (A1)–(A4) AAT agent (recursive update, well-defined mismatch $\bar o - \hat\theta$, well-defined tempo, sector-bounded linear correction).

**Exact commutation.** Both sides are running means of the same stream: $\Lambda_x$ of the micro-evolved state equals the macro-evolved state *identically*, so $\varepsilon_x = 0$ exactly (not asymptotically; numerically confirmed to $6 \times 10^{-15}$ over 20{,}000 trials, 400 steps). $\varepsilon_o = \varepsilon_a = 0$ trivially in this passive-estimation instance.

**Tempo.** The macro's single channel $\bar o$ has noise variance $\operatorname{Var}(\bar n) = \tfrac{r}{2}(1 + \rho)$, so its Fisher inflow is $J_c = \tfrac{2}{r(1+\rho)}$ and

$$\frac{\mathcal{T}_c}{\sum_i \mathcal{T}_i} = \frac{J_c}{J_1 + J_2} = \frac{1}{1 + \rho} \quad\Longrightarrow\quad \mathcal{T}_c \gt \sum_i \mathcal{T}_i \;\text{ for all } \rho \lt 0,$$

unboundedly as $\rho \to -1$. Numerical check at $\rho = -0.8$: predicted ratio $5.0$, measured $4.995$ (posterior-variance ratio at horizon, 20{,}000 trials). The same witness with $\rho \gt 0$ gives $\mathcal T_c \lt \sum_i \mathcal T_i$ *at zero closure defect and zero coordination cost* (measured: fused variance $1.77\times$ the additive-accounting prediction at $\rho = 0.8$) — the redundant direction.

## 3. What was wrong with the "capacity from nothing" intuition

The refuted grounding read sub-additivity as "composition cannot create corrective capacity out of nothing." But the composite's channel is not the disjoint union of the parts' channels: cross-channel noise structure is corrective capacity that *no individual part has and the pooled stream does* — the average channel $\bar o$ is a genuinely better sensor than either $o_i$ when noises anti-correlate. Nothing is created; the additive accounting simply cannot see interaction terms, exactly as `#deriv-tempo-additivity` established within one agent. Symmetrically, under common-source noise the additive accounting inflates the baseline, so the *defined* overhead $C_{\text{coord}} := \sum_i \mathcal T_i - \mathcal T_c$ conflates genuine internal-reconciliation cost with mere accounting error — it can be strictly positive in a composite with exact closure and no coordination activity at all, and strictly negative in a triangulating team.

## 4. The repair (landed in `#der-tempo-composition`)

Replace the additive baseline with the joint one. Let $\mathcal T_{\text{joint}}$ be the pooled-channel joint tempo of the sub-agents' combined observation set (the exact object of `#deriv-tempo-additivity`: $U \cdot \mathbf{1}^{\top}\Sigma_n^{-1}\mathbf{1}$ in the Fisher-local regime). Then:

- $\mathcal T_c \leq \mathcal T_{\text{joint}}$ — the corrected sub-additivity: no admissible composite outruns the joint information in its parts' pooled streams (data-processing at the Fisher level; this is the honest content the old bound reached for);
- $C_{\text{coord}} := \mathcal T_{\text{joint}} - \mathcal T_c \geq \varepsilon^\ast \nu_c / \lVert\delta_{\text{critical}}\rVert$ — coordination overhead measured against the right baseline, keeping the bridge-lemma lower bound and the Brooks's-Law reading intact;
- $\mathcal T_{\text{joint}} \lessgtr \sum_i \mathcal T_i$ with the signed deviation of `#deriv-tempo-additivity` applied across agents: equality iff cross-agent noise independence (plus the measure-zero cancellation set); $\lt$ under common-source (echo-chamber team); $\gt$ under anti-correlation (triangulating team) — so the *old* inequality $\mathcal T_c \leq \sum_i \mathcal T_i$ survives exactly on the cross-agent noise-independence scope and is false in general.

## 5. Honest scope

First-order tempo–Fisher identification throughout (the regime where tempo is a rate, as in `#deriv-tempo-additivity`); the witness itself (commutation, variances) is exact. The witness is passive estimation ($K_c = 1$, no actions) — deliberately minimal; action-coupled versions would need $\varepsilon_a$ treatment but the tempo arithmetic is unchanged. The organizational reading: a team whose members' *errors* anti-correlate (deliberately diverse instruments, adversarially-paired review) composes super-additively, and this is achieved by an arbitrarily simple fusion (averaging) — no exotic architecture required; conversely a team echoing one source composes sub-additively before any coordination cost is paid.

## 6. Status

- Landed in `#der-tempo-composition` (integration-is-replacement: refuted claim deleted; signed formulation in the body; WN flag discharged) with an (A3) scope clause in `#form-composition-closure`.
- **Requires confirmer≠author verification before commit** — new single-author theorem-grade math modifying an existing bound (flagged in the fork report; numerics script inline above is re-runnable).

## Appendix: verification script (preserved in-file per the l1-bias lesson — scripts die in /tmp)

```python
import numpy as np
rng = np.random.default_rng(7)
# Static theta; two channels o_i = theta + n_i, Var r, cross-agent Corr rho (fresh per step).
# Sub-agent i: running mean of own channel. Composite: running mean of the channel-average.
r, rho, T, trials = 1.0, -0.8, 400, 20000
cov = r*np.array([[1,rho],[rho,1]]); Ls = np.linalg.cholesky(cov)
theta = rng.normal(0,1,trials)
o = theta[:,None,None] + rng.normal(0,1,(trials,T,2)) @ Ls.T
m = np.cumsum(o,axis=1)/np.arange(1,T+1)[None,:,None]      # sub-agent means
fused = m.mean(axis=2)                                      # Lambda_x = mean of means
mac = np.zeros(trials)
for t in range(T):                                          # recursive macro update
    mac = mac + (o[:,t,:].mean(axis=1) - mac)/(t+1)
print("commutation:", np.abs(mac - fused[:,-1]).max())      # ~6e-15 (exact)
v_add, v_fused = r/(2*T), ((fused[:,-1]-theta)**2).mean()
print("ratio:", v_add/v_fused, "predicted:", 1/(1+rho))     # 4.995 vs 5.0
```

## 7. Post-verification addendum (2026-07-16, confirmer≠author pass)

Core fully confirmed (commutation independently re-derived + simulated at $7.1 \times 10^{-15}$; ratio reproduced at all tested $\rho$; the DPI bound judged the strongest, convention-robust claim). Verification sharpened two things, landed in the segment: (1) the $1/(1+\rho)$ ratio and the $\rho \lt 0$ threshold are stated in the matched-uncertainty (Fisher-inflow) convention — under dynamic $\theta$ with own-steady-state evaluation the ratio is $\sqrt{1/(2(1+\rho))}$ with threshold $\rho \lt -1/2$; the refutation survives every tested reading, only ratio/threshold are convention-tied. (2) In the dynamic regime the optimal-gain fused composite no longer commutes exactly (measured $\varepsilon^\ast \gt 0$) — a fidelity-tempo tradeoff absent from the static witness; the commuting composite still wins for $\rho \lt -1/2$. Verifier's script: session scratchpad `verify_tempo.py` (conventions differ from §Appendix deliberately — that was the point).
