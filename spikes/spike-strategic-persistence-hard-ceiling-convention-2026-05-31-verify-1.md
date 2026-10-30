# Verify-1: the strategic-persistence hard ceiling ($\rho_\Sigma \ge R_\Sigma/2$) and its convention spike

**Date:** 2026-10-30  
**Role:** independent adversarial verifier (KR2.3 of `msc/inside-out-2026-10/INTENT.md`). Re-derived from what is written, not from what seems meant.  
**Inputs read in full:** `01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md`, `01-aat-core/src/schema-strategy-persistence.md`, `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md` + `spikes/sim-forgetting-conventions.py`, `01-aat-core/src/result-sector-persistence-template.md`, `01-aat-core/src/deriv-edge-credence-dynamics.md` (Common Setup, Prop B.1, B.4 statement, closing status paragraph), `01-aat-core/src/deriv-discrete-sector-condition.md` (setup through contraction factor), the Codex auditor's note `audits/AUDIT-WORKING-526815/.integrated/66-schema-strategy-persistence.md`, the 526815 findings digest, the 2026-05-20 strengthening spike, and the 2026-05-20 verification `msc/verify-sector-condition-cluster-2026-05-20.md` §3–§4.  
**Scratch checks (not in repo):** `gain_check.py`, `stoch_check.py` in the session scratchpad; every number quoted below came from them.

---

## 0. Verdict

**Prop C.1 is false, and Prop C.2's ceiling falls with it. This is an algebra error, not a convention dependence.** Under the discounted recurrence that both segments state ($\alpha_k \mapsto \lambda\alpha_k + y_k$, $\beta_k \mapsto \lambda\beta_k + (1-y_k)$), the per-observation gain of the point estimate $\hat p = \alpha/n$ is exactly $1/n_t$, where $n_t$ is the count after the update. At the stationary count $n_{\text{eff}} = 1/(1-\lambda)$, that gain is $\alpha_\Sigma^{\text{ss}} = 1-\lambda$ *exactly*, not $(1-\lambda)/(2-\lambda)$. Its supremum over $\lambda$ is $1$, reached at $\lambda = 0$, where $\hat p = y$ and the gain is visibly $1$. So for the single edge, under Model D, the reachable region is $\rho_\Sigma \lt R_\Sigma$. That is the universal one-step floor every no-overshoot corrector faces, and exponential forgetting attains it. There is no forgetting-specific cap.

**The 2026-05-31 spike's verdict (B) should not be ratified.** Its "SEG vs ALT1 convention" is not a convention. The two recursions produce *the same estimator*: ALT1's stored counts are $\lambda$ times SEG's, $\hat p$ sequences agree to $10^{-16}$, and measured gains are identical. The spike's numerical "confirmation" computes $1/(n_{\text{eff}}+1)$ from the count recursion and never measures how $\hat p$ moves. It checks the formula against itself. The Codex auditor's original F72 algebra was right. So was the 526815 verifier's spot-check ("auditor's math correct"). The spike reframed a refutation as a scoping.

**Strengthen-first: a genuine $1/2$ cap does exist, for a different reason and at a different place.** Under B.4's two-arm $\varepsilon$-greedy OR node, each arm is corrected only on the steps it is pulled. Its expected per-step correction rate is at most its pull probability, because every Bayesian/convex-combination update has gain $\le 1$. Keeping both arms calibrated under Model D therefore requires $\rho_\Sigma \lt R_\Sigma \min(\varepsilon, 1-\varepsilon) \le R_\Sigma/2$, *for any update mechanism with gain $\le 1$, forgetting or not*. Generally, a $K$-alternative OR node with one observation per step has the cap $R_\Sigma/K$. An evidence-starved AND edge has the cap $\theta_{\text{upstream}} R_\Sigma$. This evidence-allocation no-go is exact under the stated model (§5.1). It also absorbs F73. The other honest home for a nontrivial cap is stochastic: observation noise injected per step scales as $g^2$, so the $\lambda \to 0$ route that "wins" Model D maximizes noise (§5.2).

---

## 1. What the segments claim

- `#deriv-strategic-persistence-hard-ceiling` Prop C.1 says that under the discounted Beta-Bernoulli recurrence, $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$. The proof substitutes the stationary count $n_{\text{eff}} = 1/(1-\lambda)$ into Prop B.1's $\alpha_\Sigma = 1/(n+1)$.
- Prop C.2 says $\sup_\lambda \alpha_\Sigma^{\text{ss}} = 1/2$, so the reachable region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$. It is labeled `status: exact`, "independent of topology", and "a class-level no-go."
- `#schema-strategy-persistence` carries the same exact form and ceiling in its intro, §"Forgetting as Prerequisite", Epistemic Status, Discussion §6 and Findings. It calls the linear form $1-\lambda$ "the slow-forgetting asymptote … unsafe outside its asymptotic regime (it permits $\lambda$ values that violate the actual prerequisite)".
- The spike (2026-05-31) says the ceiling holds under "SEG" (discount the prior pool, then add the current observation at full weight) and dissolves under "ALT1" (add, then discount). It argues SEG is AAT-canonical via the log-odds coordinate and recommends naming the convention and keeping `exact`.

## 2. Re-derivation: the gain the stated recurrence actually produces

Take the recurrence exactly as the appendix and schema write it. Let $n = \alpha + \beta$ and $\hat p = \alpha/n$ be the state before observing $y$. After the update:

$$\hat p' = \frac{\lambda\alpha + y}{\lambda n + 1}, \qquad \hat p' - \hat p = \frac{n(\lambda\alpha + y) - \alpha(\lambda n + 1)}{n(\lambda n + 1)} = \frac{n y - \alpha}{n(\lambda n + 1)} = \frac{y - \hat p}{\lambda n + 1}.$$

So the gain on this step is

$$g = \frac{1}{\lambda n + 1} = \frac{1}{n'}, \qquad n' = \lambda n + 1 \ \text{(the post-update count)}.$$

Three facts follow, each exact.

1. **The count dynamics are deterministic.** $n_t = \lambda^t n_0 + (1-\lambda^t)/(1-\lambda)$, independent of the data. Prop C.1's "fixed point in expectation" ($\alpha^\ast = \theta/(1-\lambda)$, etc.) is needed only for $\hat p$, not for $n$. The gain sequence $g_t = 1/n_t$ is deterministic.
2. **The stationary gain is $1-\lambda$.** At $n = n_{\text{eff}} = 1/(1-\lambda)$, $\lambda n_{\text{eff}} + 1 = n_{\text{eff}}$, so $g = 1/n_{\text{eff}} = 1-\lambda$. The expected correction is exactly linear, $\mathbb{E}[\Delta\hat p] = (1-\lambda)(\theta - \hat p)$. By the same sector-product algebra as B.1, the sector parameter is $\alpha_\Sigma^{\text{ss}} = 1-\lambda$, tight.
3. **Initialized at its stationary count, the discounted Beta estimator *is* the EWMA.** With $n_0 = 1/(1-\lambda)$, $\hat p_{t+1} = \lambda\hat p_t + (1-\lambda) y_t$ from the first step.

**Where Prop C.1 goes wrong.** In Prop B.1, $\Delta\hat p = (y-\hat p)/(n+1)$, and $n$ is *the count the new observation is added to*. Under the stated recurrence, that count is the discounted $\lambda n$, not $n$. Substituting the stationary $n_{\text{eff}}$ into $1/(n+1)$ evaluates B.1 at a count the update never adds to. The correct evaluation is $1/(\lambda n_{\text{eff}} + 1) = 1-\lambda$. The 2026-05-20 strengthening spike made this substitution, and the 2026-05-20 verification (`msc/verify-sector-condition-cluster-2026-05-20.md` §3) re-did *the arithmetic of the substitution* ($1/(1/(1-\lambda)+1) = (1-\lambda)/(2-\lambda)$). Neither computed $\Delta\hat p$. Both were checking the arithmetic when the substitution itself was the error.

**The segment's own boundary paragraph shows the error.** The appendix says that at $\lambda = 0$, "every observation fully replaces the prior … giving $\alpha_\Sigma = 1/2$". Full replacement *is* gain $1$: with $\lambda = 0$ the recurrence gives $\alpha = y$, $\beta = 1-y$, $\hat p = y$. A gain of $1/2$ would mean averaging the new observation with the old estimate, which this recurrence never does.

**Numerical check (scratch `gain_check.py`).** I simulated the recurrence on Bernoulli data and measured $(\hat p_{t+1} - \hat p_t)/(y_t - \hat p_t)$ directly. Over the last 500 steps of 4000:

| $\lambda$ | measured gain (SEG) | measured gain (ALT1) | $1-\lambda$ | $(1-\lambda)/(2-\lambda)$ |
|---|---|---|---|---|
| 0.0 | 1.000000 | n/a (degenerate) | 1.0 | 0.5 |
| 0.1 | 0.900000 | 0.900000 | 0.9 | 0.4737 |
| 0.5 | 0.500000 | 0.500000 | 0.5 | 0.3333 |
| 0.9 | 0.100000 | 0.100000 | 0.1 | 0.0909 |
| 0.99 | 0.010000 | 0.010000 | 0.01 | 0.0099 |

Min and max over the window equal the mean to six decimals, because the gain is deterministic. With ALT1 initialized at $\lambda$ times the SEG state, $\max_t \lvert\hat p^{\text{SEG}}_t - \hat p^{\text{ALT1}}_t\rvert$ was $1.1\times 10^{-16}$ at $\lambda = 0.3$ and $2.2\times 10^{-16}$ at $\lambda = 0.9$.

## 3. Why the "convention" framing does not survive

- **SEG and ALT1 are one estimator with two bookkeeping choices.** If $a_t = \lambda s_t$ (ALT1 state vs SEG state), then $a_{t+1} = \lambda(a_t + y) = \lambda(\lambda s_t + y) = \lambda s_{t+1}$. The ratio $\hat p$ is the same, and so is its gain. "Where the discount lands relative to the $+1$" changes which number you *call* the count. It does not change the estimator. The gain is a property of the $\hat p$ sequence, which is fully determined, so there is nothing for a convention to decide.
- **ALT1's $n_{\text{eff}} = \lambda/(1-\lambda)$ is SEG's discounted pre-observation count $\lambda n_{\text{eff}}$.** Plugging it into $1/(n+1)$ is the *correct* application of B.1. That explains why ALT1 "gives" $1-\lambda$.
- **No single-rate exponential-forgetting recursion of this type yields $(1-\lambda)/(2-\lambda)$.** That value is the steady gain of a recursion with a different discount, $\lambda' = 1/(2-\lambda)$. As $\lambda$ ranges over $[0,1)$, $\lambda'$ covers only $[1/2, 1)$. That is the whole origin of the $\sup = 1/2$.
- **The spike's EWMA disqualification is a parameterization artifact.** EWMA is §2 fact 3, the stationary SEG estimator. The $\lambda = 1$ reduction test compares the two at different count states, not different estimator families.
- **The log-odds canonicity argument (spike §4.2) concerns a different recursion.** $\Lambda_{t+1} = \lambda\Lambda_t + \ell(y_{t+1})$ discounts accumulated log-odds, which is a different estimator from discounting Beta pseudo-counts. Its stationary gain properties would need their own derivation, and none is given. It cannot adjudicate between SEG and ALT1 because there is nothing to adjudicate.
- **The spike's simulation does not test the claim.** `sim-forgetting-conventions.py` iterates $n \mapsto \lambda n + 1$ (or $\lambda(n+1)$) and prints $1/(n+1)$. It never builds $\hat p$ or measures a correction. Its agreement with the formula is the formula's arithmetic, not evidence about the estimator.

## 4. What holds for the single edge (B.1 under forgetting), under exactly which conditions

**Conditions:** Beta-Bernoulli edge, discounted recurrence as stated, $\lambda \in [0,1)$, mismatch $\delta_\Sigma = \hat p - \theta$, and the Model D reading the schema uses: deterministic drift $\lvert\theta_{t+1} - \theta_t\rvert \le \rho_\Sigma$ per step, applied to the mean dynamics as in B.1.

**C.1, corrected (exact).** $\alpha_\Sigma^{\text{ss}} = 1-\lambda$. The linear form is not an asymptote; it is the exact value. The schema's warning that the linear form is "unsafe … permits $\lambda$ values that violate the actual prerequisite" reverses the truth. $(1-\lambda)/(2-\lambda)$ understates the gain, so it *forbids* feasible $\lambda$.

**Trajectory guarantee: a strengthening the segments can now state.** Write $m_t = \mathbb{E}[\hat p_t] - \theta_t$. Because $g_t$ is deterministic, the mean dynamics are exactly $m_{t+1} = (1-g_t)m_t - d_t$, with $\lvert d_t\rvert \le \rho_\Sigma$ and $g_t = 1/n_t \in (0,1]$. If the initial count satisfies $n_0 \le 1/(1-\lambda)$, then $n_t$ rises monotonically to $n_{\text{eff}}$ and $g_t \ge 1-\lambda$ for all $t$. Induction gives $\sup_t \lvert m_t\rvert \le \max(\lvert m_0\rvert, \rho_\Sigma/(1-\lambda))$: if $\lvert m_t\rvert \le M$, then $\lvert m_{t+1}\rvert \le \lambda M + \rho_\Sigma \le M$. So $1-\lambda \gt \rho_\Sigma/R_\Sigma$ with $\lvert m_0\rvert \lt R_\Sigma$ is an all-time guarantee, not only an asymptotic one. With a uniform prior ($n_0 = 2$) the initialization condition is $\lambda \ge 1/2$. If $n_0 \gt n_{\text{eff}}$, the gains rise toward $1-\lambda$ from below and the guarantee is asymptotic. This directly answers the template's "time-varying $\alpha$" caveat for this instance.

**C.2, corrected (exact).** The prerequisite is $1-\lambda \gt \rho_\Sigma/R_\Sigma \iff \lambda \lt 1 - \rho_\Sigma/R_\Sigma$. Some $\lambda \in [0,1)$ satisfies it iff $\rho_\Sigma \lt R_\Sigma$. That bound is not specific to forgetting. Under Model D with a scalar linear corrector of gain $g$, the ultimate bound is $\rho/g$ for $g \le 1$ and $\rho/(2-g)$ for $g \in (1,2)$ (`#deriv-discrete-sector-condition` DA.1: discrete equals continuous under Model D). Both are $\ge \rho$, with equality only at $g = 1$. So $\rho_\Sigma \lt R_\Sigma$ is the best any no-overshoot corrector can do, and exponential forgetting reaches it. The appendix's Impact paragraph says the agent "must change … the update mechanism class (away from gain-decay-plus-forgetting toward constant-step finite-gain)". It has no support: discounted Beta at stationarity *is* constant-step EWMA (§2 fact 3).

**What stands untouched:** the no-forgetting no-go. With $\lambda = 1$, $g_t = 1/n_t \to 0$, so every positive $\rho_\Sigma$ is eventually fatal. That is the real content of "forgetting as prerequisite" and of the NeurIPS Paper 2 $\mathcal A_{\text{decay}}$ theorem.

## 5. Strengthen-first: where a nontrivial cap genuinely lives

The ceiling was asserted for a reason, so before landing "no cap" I looked for where the intuition is true.

### 5.1 Evidence-allocation no-go (exact under the stated model)

**Setup.** Take a strategy node whose $K$ alternatives (or edges) must all stay calibrated, as SA3 and B.4's weakest-link require. One observation arrives per time step. Edge $i$ is observed with probability $\pi_i$ and updated by any rule with per-observation gain $g_i \le 1$. That includes every Bayesian/convex-combination update ("posterior between prior and data", `#deriv-discrete-sector-condition`), with or without forgetting. The model is Model D drift of each $\theta_i$, at most $\rho_\Sigma$ per *time* step, observed or not.

**Claim.** Persistence of every edge requires $\rho_\Sigma \lt R_\Sigma \min_i \pi_i$.

**Derivation.** Under a fixed allocation, edge $i$'s mean mismatch obeys $m_{i,t+1} = (1 - \pi_i g_i) m_{i,t} - d_{i,t}$. Its effective per-step sector parameter is $\pi_i g_i \le \pi_i$, so its Model-D ultimate bound is at least $\rho_\Sigma/\pi_i$. That is exact for constant-sign drift.

**Instances:**

- **Two-arm $\varepsilon$-greedy OR (B.4).** $\pi = (1-\varepsilon, \varepsilon)$, so $\rho_\Sigma \lt R_\Sigma\min(\varepsilon, 1-\varepsilon) \le R_\Sigma/2$, with equality only at $\varepsilon = 1/2$ and $g = 1$. **This is a true, sharp $1/2$ ceiling.** It is mechanism-independent and comes from evidence allocation, not from forgetting algebra. With forgetting at stationary gain $1-\lambda$, the admissible exploration interval is $\rho_\Sigma/((1-\lambda)R_\Sigma) \lt \varepsilon \lt 1 - \rho_\Sigma/((1-\lambda)R_\Sigma)$. It is non-empty iff $\rho_\Sigma \lt (1-\lambda)R_\Sigma/2$. This is exactly F73's two-sided interval, which the schema states only as a lower bound ($\varepsilon \gt \rho_\Sigma(n_{\max}+1)/R_\Sigma$).
- **$K$-alternative OR node.** $\min_i \pi_i \le 1/K$, so $\rho_\Sigma \lt R_\Sigma/K$.
- **Evidence-starved AND edge (B.2).** The downstream edge is observed only when the upstream link fires: $\pi_2 = \theta_1$, so $\rho_\Sigma \lt \theta_1 R_\Sigma$ for that edge.

The cap is exactly as strong as the fixed-allocation reading B.4 already uses. A state-dependent greedy allocation would need its own treatment.

### 5.2 Stochastic: the $\lambda \to 0$ route maximizes noise (derived under a named model; sanity-checked, not landed)

The Model D sup is reached at $g = 1$, where $\hat p = y \in \{0,1\}$. Including observation noise, with $\varepsilon_t = y_t - \theta_t$ and variance $v = \theta(1-\theta) \le 1/4$:

$$\xi_{t+1} = (1-g)\xi_t + g\,\varepsilon_t - d_t.$$

Under constant-sign drift the steady state is $\mathbb{E}\xi = -\rho_\Sigma/g$ and $\operatorname{Var}\xi = g v/(2-g)$, so

$$\mathbb{E}[\xi^2]_{\text{ss}} = \frac{\rho_\Sigma^2}{g^2} + \frac{g\,v}{2-g}.$$

Unlike the template's Model S with fixed $\sigma$, the injected noise ($g^2 v$ per step) scales with the gain. This is the bias–variance trade-off the schema's own Discussion mentions, and it is the "bidirectional threshold" of NeurIPS Paper 2. In the mean-square sense, persistence is feasible iff $\min_{g \in (0,1]} [\rho_\Sigma^2/g^2 + g v/(2-g)] \lt R_\Sigma^2$. In the small-gain regime ($\rho_\Sigma^2 \ll v$) the optimum is $g^\ast \approx (4\rho_\Sigma^2/v)^{1/3}$, and feasibility is approximately $\rho_\Sigma \lesssim 0.77\,R_\Sigma^3/v$. That is a genuinely nontrivial cap with $R^3$ scaling, unlike Model D's $\rho \lt R$.

Scratch `stoch_check.py` ran the actual discounted estimator with $\theta \in [0.3, 0.7]$ and drift reversing at the walls. Simulated MSE vs the formula with $v = 1/4$: $0.0126$ vs $0.0136$ ($\lambda = 0.9$, $\rho = 0.002$); $0.0787$ vs $0.0834$ ($\lambda = 0.5$); $0.0038$ vs $0.0041$ ($\lambda = 0.97$, $\rho = 0.0005$). The formula is consistently a slight overestimate, as expected since $v \lt 1/4$ off-center and the drift reverses. Idealization caveat: constant-sign drift cannot persist inside $[0,1]$. That is the same idealization Model D makes. I would land this at `conditional` at most, after its own independent check.

## 6. The convention question that is real (and open)

For intermittently observed edges there is a genuine modeling choice. Is the discount applied **per observation of that edge**, or **per time step**? The single edge never sees it. B.2 and B.4 do.

- Per-observation discounting: the per-step expected gain is $\pi(1-\lambda)$ exactly.
- Per-time-step discounting: the count decays between observations, so each observation lands with a larger gain. Roughly, the per-step expected gain is $\pi(1-\lambda)/(1-\lambda(1-\pi))$ (approximation; Jensen gap). That is close to $1-\lambda$ for slow forgetting, which partially cancels evidence starvation.

Scratch simulation at $\pi = 0.3$: per-observation $0.0300$ vs per-step $0.0870$ ($\lambda = 0.9$); $0.0030$ vs $0.0099$ ($\lambda = 0.99$). The supremum over $\lambda$ is $\pi$ under both choices, so §5.1's cap is unaffected. The *threshold $\lambda$* for B.2/B.4 under forgetting does depend on this choice. Canon never states it, and it is the convention a careful reader would actually need named.

## 7. What the segments should say

Under integration-is-replacement, the refuted claim is deleted, not kept softened with a pointer to a "convention". Per surface:

**`#deriv-strategic-persistence-hard-ceiling`.** Its title claim and both propositions are false as stated. The owner has to choose what replaces them:
- **(a) Re-scope** the segment to the true results: corrected C.1 ($\alpha_\Sigma^{\text{ss}} = 1-\lambda$ exact, with the deterministic-gain derivation of §2 and the all-time trajectory guarantee of §4), plus the §5.1 evidence-allocation no-go as the place a $1/2$ cap genuinely appears (two-arm OR), generalized to $1/K$ and $\theta_1$. This keeps a real no-go on the critical path. It would need a new slug and title, and the segment's `depends:` would gain the B.2/B.4 machinery.
- **(b) Delete** it, put the corrected C.1 into the schema, and give the allocation no-go its own segment near `#deriv-edge-credence-dynamics`.

In both cases the Impact's "must change the update-mechanism class" claim goes, the Novelty "§D.3 strengthen-first work … had hidden the ceiling" goes, and the "topology-independent" claim goes. Even on the segment's own premises, that last claim was unsupported: B.2's $\theta_1$ and B.4's $\varepsilon$ factors scale $\alpha_\Sigma$.

**`#schema-strategy-persistence`.** Replace $(1-\lambda)/(2-\lambda)$ with $1-\lambda$ (exact) everywhere: intro paragraphs 2–3, §Forgetting as Prerequisite, the threshold equivalence (it becomes $\lambda \lt 1 - \rho_\Sigma/R_\Sigma$, valid for all $\rho_\Sigma \lt R_\Sigma$), Epistemic Status, Discussion §6, and Findings Brief/Impact/Novelty ("the $1/(2-\lambda)$ damping factor" goes). Delete the "slow-forgetting asymptote / unsafe" language and every $\rho_\Sigma \ge R_\Sigma/2$ ceiling sentence, including the Impact's "keep the strategic disturbance well below half the reserve". In the Epistemic Status instance list, item 4 should carry the two-sided $\varepsilon$ interval. Working Notes: the D.3 line should move to CHANGELOG as history. The off-ramp flag (F72/F73) resolves with a pointer to this file. The "Model S … $\alpha \gt n\sigma^2/(2R^2)$" sentence deserves a note that observation noise here is gain-modulated (§5.2).

**Other carriers of the false form or the ceiling (from a repo grep):**
- `01-aat-core/src/deriv-edge-credence-dynamics.md` line 662: $(1-\lambda)/(2-\lambda)$ becomes $1-\lambda$.
- `01-aat-core/src/disc-constructive-impossibility-posture.md`: Instance E row, line 29 "Prop C.2's $\rho_\Sigma \lt R_\Sigma/2$ cap", the `depends:` entry, and line 102. The no-forgetting $\mathcal A_{\text{decay}}$ no-go (escape: finite gain) or the §5.1 allocation no-go (escape: more evidence channels or fewer alternatives) are true candidates for Instance E.
- `01-aat-core/OUTLINE.md` line 333 ("a design space half of which is unreachable under a given update mechanism") and the row at line 358.
- Generated: `FINDINGS.md`, `README.md`, `doc/readme/src/_findings-summary.md` line 73, `CURRENT-VOL1*.md`. Regenerate these after the source edits.

**Already correct, no change needed:** `result-sector-persistence-template` line 101 and `impl-strategy-dynamics` line 30 carry $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$, which is the exact form. Leave them alone, or drop any "slow-forgetting" qualifier.

**Trackers.**
- `JOSEPH-TODO.md` line 32 ("take adjudication verdict B as settled … keep `status: exact`") should not be acted on.
- `TODO.md` line 39 and `spikes/INDEX.md` lines 138–144 and 256: re-word (the 05-20 "math independently verified" row overstates what was checked).
- The 05-31 spike: its verdict is superseded by this file.

**NeurIPS Paper 2 (outside this repo; flag only).** `~/src/neurips/02-unified-convergence-rl/adjudicated/residue.md` §4 records "One-line convention decision owed (SEG vs ALT1)" and calls the paper's $1-\lambda$ a residue to rewrite. The paper's $1-\lambda$ under the Beta-Bernoulli premise is correct. What it needs is its $\approx$ (Key Lemma 2) upgraded to $=$ with the §2 derivation, not a switch to $(1-\lambda)/(2-\lambda)$.

## 8. Confidence, scope, and what I did not check

- **High confidence** in §2–§4. The algebra is three lines and the direct gain measurement agrees to six decimals across five $\lambda$ values.
- **High confidence** in the §5.1 derivation within its model: fixed allocation, gain $\le 1$, per-time-step Model-D drift on every alternative, all alternatives required to persist. Whether SA3's "all OR alternatives" requirement is the right persistence target for an OR node is a theory question I did not adjudicate. If only the chosen arm must persist, the cap changes.
- **Moderate confidence** in §5.2's closed forms as a model of the schema's setting. They are exact for the linear recursion under the stated idealization, and the small-gain feasibility constant is an approximation.
- **Not checked:** B.2–B.7's own algebra beyond the statements quoted; the log-odds recursion's gain; NeurIPS Paper 2's $\mathcal A_{\text{decay}}$ proof; whether any other segment uses $n_{\text{eff}}+1$ the same way. That last pattern ("substitute a stationary count into a gain formula indexed by the pre-update count") is worth one grep by whoever lands this.

## 9. Feedback (process, offered as data)

- Two independent agents got this right early: the Codex auditor (F72) and the 526815 verifier's spot-check. The error survived because the strengthening spike, its "independent verification" and the convention spike all verified *the substitution's arithmetic*, never the substitution itself. A check that would have caught it at every stage: compute $\Delta\hat p$ from the recurrence, or run the estimator and measure its gain. For any claimed gain or rate formula, measuring the quantity rather than evaluating the formula is a cheap habit worth adding to the spike SOP's verification snippet.
- The 05-31 spike shows a specific failure mode. A refutation arrived framed as "convention-dependent". The spike accepted the framing and built a canonicity argument for the false branch, and the "strengthen-first" posture ended up defending the claim instead of testing it. The tell was in the segment: its own $\lambda = 0$ boundary prose contradicted its formula.
- The $1/2$ in the two-arm OR node (§5.1) suggests the original intuition that some cap near $1/2$ exists was reaching toward something real, even though the stated derivation was wrong.
