# 03 — Derivations (revision 2)

*Every closed form here is checked in `sims/checks.py` (output: `sims/checks-output.txt`; section tags S0–S13). Revisions 1 and 2 follow the independent verifications in `de-novo-feedback-1.md` and `de-novo-feedback-2.md`. How each finding was handled is in `de-novo-feedback-1-response.md` and `de-novo-feedback-2-response.md`; this file states present truth only. Tiers: **exact** = derived under the stated model; **conditional** = exact given named premises; **numerical** = exhibited in simulation under a stated parameterization, not derived; **discussion-grade** = argued. Each universally quantified claim ends with an adversarial instance outside the motivating family.*

## 0. Setting and vocabulary

A scalar world quantity $\theta$. The agent's content prior is $\mathcal N(\mu_0, U_0)$. Sources $j$ emit $y_{j,i} = \theta + \beta_j + \varepsilon_{j,i}$, with a **persistent source offset** $\beta_j$ (zero for an honest source, the lie $b$ for a deceiver) and fresh noise $\varepsilon_{j,i} \sim \mathcal N(0, \sigma_j^2)$. The agent carries a **trust model** of its sources: a prior over each $\beta_j$ (Gaussian $\mathcal N(0,\tau_j^2)$, or an honest/liar mixture with $P(\beta_j = 0) = p_j$ and liar offsets $\sim \mathcal N(0,L^2)$), a believed noise $s_j^2$, and an assumption about independence across messages and sources.

Gain collapse is used in canon's sense (`#emp-update-gain`, `#def-death-as-factor-loss` D4): $\eta^\ast \to 0$ because $U_M \to 0$ **inappropriately** (dogmatism) or $U_o \to \infty$ **inappropriately** (nihilism). "Inappropriately" is measured against the *actual* error, so the diagnostic quantity throughout is actual error relative to believed error, not the gain sequence alone.

Joseph's three levers act on the trust model. **Borrowed authority or relationship** is a small $\tau_A^2$, or $p_A \to 1$ ("this source is unbiased, one of us"). **Repetition** is a large message count $n_A$, possibly spread over counterfeit sources (Sybil). **Cutting off other channels** is a small number $K$ of sources outside the deceiver's control.

## R1. Where the gain law is exact, the content of a lie does not move the gain

*[Exact, scoped: fixed-covariance linear-Gaussian filtering]*

With the noise model fixed, the gain sequence $K_t$ follows from the Riccati recursion and depends only on believed variances and on the count and timing of observations. A lie on a trusted channel yields a gain sequence identical to truth's, bit for bit (S0).

**What R1 does and does not show.** It locates the mechanism: in this regime a deceiver cannot act on gain through what it asserts, only through what the agent believes about the source. It does **not** bear on whether deception causes gain collapse in canon's sense. Collapse is defined by *inappropriateness*, and R1 compares a gain sequence to itself. In a static world, the gain goes to zero under truth (appropriately) and under the lie (inappropriately), and R1 cannot tell the two apart. R2 can.

**Adversarial instances outside the scope.** Where the agent estimates its trust model from data, content is the input to that estimation, so content moves gain:

- Beta-Bernoulli: 50 unanimous claims give posterior variance $3.6\times10^{-4}$, against $4.7\times10^{-3}$ for balanced claims (S11).
- Student-$t$ filtering has content-dependent gain (S7).
- A noise-estimating agent reads verbatim repetition as precision (S6, R2).
- The innovation-based estimators of `#deriv-adaptive-gain-dynamics` do the same.

So the first-order/second-order split is a useful locating device in the exact regime, **not** a partition of how deception works in general. In learners that estimate their trust model from outputs, consistency and repetition in the content are themselves the lever.

## R2. Deception produces gain collapse in canon's sense, under named conditions

*[Exact in the Gaussian trust model]*

Take $n$ messages from source $A$ with true offset $b$, received by an agent with bias prior $\mathcal N(0,\tau_A^2)$ and believed noise $s^2$ (equal to the true $\sigma_A^2$). The world is static (no process noise), and there is no forgetting.

**Believed uncertainty.** Authority sets the floor; repetition drives the agent to it:

$$V_n = \Big(\frac{1}{U_0} + \frac{1}{\tau_A^2 + s^2/n}\Big)^{-1} \;\xrightarrow{\;n\to\infty\;}\; \Big(\frac1{U_0} + \frac1{\tau_A^2}\Big)^{-1}.$$

(S1.) The trusting (correlation-neglecting) agent is the limit $\tau_A^2 = 0$, where $V_n = U_n = (1/U_0 + n/s^2)^{-1} \to 0$.

**Actual error (trusting limit).** The posterior mean $\mu_n = U_n(\mu_0/U_0 + \sum_i y_i/s^2)$ has bias $\frac{U_n}{U_0}(\mu_0-\theta) + U_n n b/s^2 \to b$ and variance $U_n^2 n/s^2$. With $\mu_0 = \theta$, the **calibration ratio** (actual mean-square error over believed variance) is exactly

$$\frac{\mathbb E[(\mu_n-\theta)^2]}{U_n} = \frac{(U_n n b/s^2)^2 + U_n^2 n/s^2}{U_n},$$

which is $\approx 1 + nb^2/s^2$ once $n \gg s^2/U_0$. The exact values are 20.8, 245, 2,495 and 24,995 at $n = 1, 10, 100, 1000$ (S1; the approximation should not be read at $n = 1$, where it gives 26). This is $U_M \to 0$ **inappropriately**: canon's dogmatism mode, produced by deception. The posterior density at the truth, relative to the mode, falls like $\exp(-nb^2/2s^2)$.

**The gain gap, measured against the oracle.** The agent's gain on the next honest observation is $\eta_H = U_n/(U_n+\sigma_H^2)$: 0.44, 0.089, 0.0099, 0.0010. *These numbers are identical under an honest source*, and correct there. The deception effect is the gap to the oracle gain, the gain an agent that knew its true error would use: under the lie 0.94, 0.96, 0.96, 0.96; under truth 0.39, 0.087, 0.0099, 0.0010 (verifier check B, re-run). The gap is the calibration ratio seen from the gain side, not a second effect. This result derives the `[Discussion]`-tagged sentence in `#deriv-tempo-additivity`.

**The nihilism mode is realized too, and on honest channels.** Under an honest/liar mixture trust model with the deceiver trusted ($p_A$ high) and a lone honest dissenter ($K = 1$), the dissenter is attributed as the liar ($P(A\text{ liar}) = 0.019$ at $p_A = 0.99$, $p_H = 0.5$; R3). A source judged a liar carries almost no information about $\theta$, so its effective $U_o \to \infty$. Undetected deception therefore produces *spurious distrust of honest sources*: canon's nihilism mode, pointed at the truth. Under consensus-trust dynamics this happens by the agent's own updating (S13: the lone dissenter's trust falls to 0.02). **Which mode appears is set by the trust-model class.** Correlation neglect gives dogmatism; a liar-component model gives nihilism toward honest channels. Both are canon's gain collapse.

**Consistency read as precision.** An agent that estimates a source's noise from the dispersion of its messages (Normal-Inverse-Gamma) reads identical repetition as a precise source: $\mathbb E[\sigma^2]$ falls to 0.05 after 1,000 verbatim repeats, against 1.04 for naturally varied honest messages (S6). The effect needs volume; at $n = 10$ the two are indistinguishable (3.88 against 3.82), because the prior-mean term dominates early. The model-class diagnosis: under continuous noise, identical messages have probability zero unless they were copied, and this agent's class has no *copying* hypothesis. A duplication/dependence component, which collapses $n$ copies toward one, is the defense. This is the same class inadequacy as R3's missing liar component, one level down.

**Adversarial instance.** In Beta-Bernoulli the trusting agent's posterior variance falls like $1/n^2$ under unanimity. The linear calibration law is Gaussian-specific; the unbounded calibration ratio is not. Actual LLMs show an empirical analog of the volume effect: many-shot jailbreaking's effectiveness follows a power law in the number of in-context demonstrations (Anil et al. 2024). Those are demonstrations of behavior, not repetitions of a claim, so it is an analog, not an instance.

## R3. The attribution floor

*[Exact in both trust models; the per-corroborator factor has an asymptotic closed form]*

With persistent offsets, data identify only *differences* between sources; which source is biased is settled by priors, however much data arrives.

**Gaussian bias priors.** $K$ honest sources (prior $\tau_H^2$) plus the deceiver (prior $\tau_A^2$), each with unlimited messages:

$$\mathbb E[\theta \mid \text{data}] - \theta = b\,w_A + (\mu_0-\theta)\frac{1/U_0}{\Pi},\qquad w_A = \frac{1/\tau_A^2}{\Pi},\quad \Pi = \frac{1}{U_0} + \frac{1}{\tau_A^2} + \frac{K}{\tau_H^2}.$$

This error is permanent: identical at $10^3$ and $10^9$ messages per source (S2, checked with $\mu_0 = \theta$). Corroboration is weak here: $w_A$ falls like $1/K$.

**Honest/liar mixture priors.** With a diffuse content prior and $K = 1$, only the discrepancy $d$ is informative:

$$P(A\text{ liar}) = \frac{p_H(1-p_A)\varphi(d;L^2) + (1-p_A)(1-p_H)\varphi(d;2L^2)}{p_A(1-p_H)\varphi(d;L^2) + p_H(1-p_A)\varphi(d;L^2) + (1-p_A)(1-p_H)\varphi(d;2L^2)}.$$

This is a pure prior contest (0.019 at $p_A = 0.99$, $p_H = 0.5$, $d = 5$, $L^2 = 25$; S2b). For $K \ge 2$, with $\varepsilon^2$ the variance the agent's model assigns to honest agreement and $\varepsilon \ll L$, each added corroborator multiplies the odds against the lone dissenter by

$$\frac{p_H}{1-p_H}\,\sqrt{\frac{L^2}{\varepsilon^2}}\;e^{b^2/2L^2}\sqrt{\frac{K}{K+1}}.$$

This closed form is from the verifier. I re-ran its check A: 673.1 predicted against 672.9 measured, 67.3 against 67.3, 605.8 against 606.3 at $p_H = 0.9$. It degrades where the asymptotics say it should: the $K = 1 \to 2$ step, $\varepsilon \sim L$, and small $p_H$. In log-odds, authority contributes $\log(p_A/(1-p_A))$, and each corroborator contributes $\log(p_H/(1-p_H)) + \tfrac12\log(L^2/\varepsilon^2) + b^2/2L^2 - O(1/K)$. Isolation versus authority is therefore an exact comparison of terms. Where strangers are suspected ($p_H$ small), corroboration weakens by exactly the log-odds of $p_H$.

**The reversal.** $\varepsilon^2$ is the agent's *model* of how tightly honest sources agree, not the observed tightness. When honest reports really scatter more than the agent's model allows, their disagreement reads as evidence of lying, and corroboration inverts. With $K = 3$, $p_A = 0.99$: $P(A\text{ liar}) = 1.000$ at zero honest scatter, but 0.263 when honest scatter is 0.1 against a model $\varepsilon$ of 0.01. When honest reports scatter with sd 1 (ordinary noise, against a lie of 5) it is 0.09–0.24 for every model $\varepsilon$ tried (verifier check A2, re-run). Corroboration beats authority only when honest agreement is tight relative to both liar scatter and the agent's expectation of honest agreement.

**The agent's own knowledge is a channel.** With a content prior centred near the truth, the lie's implausibility counts as evidence. At $K = 1$, $p_A = 0.99$, $P(A\text{ liar})$ is 0.019, 0.021, 0.24 and 0.9997 as the lie moves from 0.05 to 5 prior standard deviations away from the truth (S2b). This is the exact scope of capability's protection (R6).

**Class consequence** (the corrected form of `#def-model-class-fitness`'s audit hook). A trust model *without a liar component* gets only harmonic protection from corroboration; one *with* it gets geometric protection. That protection is conditional on the agent's model of honest agreement being realistic. The inadequacy shows up as prior-determined attribution, not as structured residuals.

## R4. The isolation floor, and the simulated-world identity

*[Exact; a structural identity]*

If the deceiver controls every channel the agent observes, *including the observed consequences of its own actions*, and emits them as the observation process of a coherent alternative world $\omega'$, then for every policy the chronica has the same law as it would have with honest sources in $\omega'$. Every statistic the agent computes (innovations, dispersion estimates, curvature, adaptive gains) is a function of the chronica, so each behaves exactly as it would in $\omega'$. No test available to the agent distinguishes the two worlds. This is the Lemma-1 shape of `#deriv-reward-channel-learning-no-go` and a candidate `#disc-identifiability-floor` instance. Under full control, the deceiver's power is to choose a world in which the confidence it induces would be warranted.

**Scope.** This holds under *full* control only. Under partial control there is no single simulated world, and the uncontrolled channels carry the discrepancy that R3's attribution machinery acts on.

**Escapes (the constructive boundary).**

- (E1) A channel outside the deceiver's control: `#hyp-solicitable-escape`'s differently-positioned observer.
- (E2) The agent's own intervention with an uncontrolled consequence channel: the loop as a Level-2 engine (`#der-loop-interventional-access`). This is what "if the agent persists" means formally.
- (E3) Authenticated identity, which makes impersonation costly.
- (E4) The content prior, for implausible lies only.

Cutting off other channels removes E1; controlling what the agent can check removes E2.

## R5. Recovery, and the (D4) terminal form

*[R5a–c, R5e exact in the Gaussian trust model; R5d numerical; the terminal form conditional plus numerical]*

**R5a Dilution** (pooled memory, deceiver silenced). Reaching bias $\le \epsilon$ after $n_A$ trusted lies needs

$$m^\ast = \sigma_H^2\Big(\frac{b}{\epsilon}\frac{n_A}{s^2} - \frac1{U_0} - \frac{n_A}{s^2}\Big)$$

honest messages: 490, 4,900 and 49,000 for $n_A = 10, 100, 1000$ (S4). The cost is linear in the volume of the lie.

**R5b The persistent deceiver.** A trusting agent with a deceiver at rate $\nu_A$ and honest channels at $\nu_H$ converges to

$$\mu_\infty = \theta + b\,\frac{\nu_A/s^2}{\nu_A/s^2 + \nu_H/\sigma_H^2},$$

a Berk-type misspecified-learning limit (3.756 simulated against 3.750 predicted; S4). Under the structured trust model the limit is R3's attribution point.

**R5c Provenance is necessary and sufficient for exact retroactive correction.** Under the family of models "any subset of sources may be discounted", the minimal sufficient statistic is the per-source vector $(n_j, \sum_i y_{j,i})$. For any exponential family with source-indexed parameters, the per-source sufficient statistics are sufficient under every reweighting of sources. Pooled memory cannot separate the deceiver's contribution: identical pooled memory admits corrected estimates of $-0.12$ or $2.96$ (S3). This is the deception-side sibling of `#def-chronica`'s fork-undetectability, and a sharper form of the CHRONICA defense: keep *the source of each piece of evidence*. Close neighbors: machine unlearning, where Cao & Yang (2015, IEEE S&P) obtain exact unlearning by recasting learning into a *summation form* over the data to be removed (R5c is a Gaussian-location instance of that condition), and Bourtoule et al. (2021, SISA) obtain it by sharding state; both verified bibliographically. Also Hu 2026's finding that stripping verification provenance in agent pipelines raises risky approvals from 5–9% to 60–98%.

**R5d Capture under consensus-estimated trust** *[numerical, two rules, one parameter family]*. The agent estimates each source's reliability by its agreement with the current consensus, and weights the consensus by reliability. This is a *truth-discovery-style heuristic*: it resembles truth-discovery iteration, but it has no latent-class likelihood and is not Dawid–Skene EM. Two variants are run:

- **(S13)** exponentially smoothed reliability, which forgets its starting value;
- **(S14)** reliability as a Beta posterior over cumulative soft agreement, which never forgets its prior. Here borrowed authority is prior pseudo-counts.

The deceiver asserts $b = 5$. Four findings:

- **Isolation launders authority into apparent track record.** After 300 steps with the deceiver as the sole source, the outcome against later dissent is the same whatever the deceiver's initial trust. That holds in S13 (initial trust 0.99, 0.5 and 0.1 give identical beliefs; verifier probe 1) and in S14 (prior strength 0 to 1000). During isolation the deceiver "earns" trust by agreeing with a consensus it alone sets, so borrowed authority is no longer needed once isolation has run.
- **Without incumbency, authority is the first-contact lever, and it trades against concurrent dissent** (S14, neutral start). One dissenter is captured at prior strength $\ge 100$ (0.2 captured at strength 0). Two dissenters are captured at 1,000. Three escape even at $10^4$, with residual bias up to 1.9: partial capture.
- **With incumbency, escape needs a concurrent-voice plurality with a margin.** The deceiver's Sybil voices ($n_A$) count against concurrent independent dissenters ($K$). In S13 the escape thresholds are $n_A = 1$: $K = 2$; $n_A = 2$: $K = 3$; $n_A = 3$: $K = 5$ (verifier probe 4, re-run). In S14, without forgetting, the margins are larger: $n_A = 1$ holds against $K = 2$, $n_A = 2$ against $K = 4$, and $n_A = 3$ against $K \ge 6$. Memory in the trust model entrenches the incumbent, so forgetting there aids escape (compare R5e).
- **Transient dissent never escapes** (S13): twelve dissenters, each active for a window and then cut off, leave the belief at 4.4–5.7 across 5 seeds and windows of 50, 150 and 400 steps.

The same simulations refuted an earlier version of this result, "one-at-a-time arrival stays captured regardless", which is recorded in S13.

**The terminal form, stated.** The **captured state** is: the content posterior near the lie, the deceiver's reliability near 1, and dissenting sources' reliability near 0. A lone dissenter's reliability settles near its expected agreement with a consensus at the lie, $rac{c}{\sqrt{c^2+1}}\exp(-\mu^2/2(c^2+1)) pprox 0.03$ at $\mu = 4.7$, $c = 1.5$ (the verifier's expression; S13 shows 0.02). **In the exhibited parameterizations**, the captured state is absorbing while the deceiver persists *and holds incumbency plus a concurrent-voice plurality with the margin above*. The adversary keeps that plurality in two ways: by **isolation**, which lowers the number of concurrent independent dissenters, and by **Sybil voices**, which raise its own. What keeps capture absorbing is the adversary's continued control of *who is speaking at once*, acting through the agent's own trust dynamics, not a memory policy assumed on the victim's side. This parallels `#der-severed-actuation-dynamics` Result 4, where the agent's own learning silences the recovery channel. Tier: numerical, two truth-discovery-style rules; the escape condition in closed form is open (below). **Recoverability:** capture breaks when enough concurrent independent dissent arrives (E1), when the agent acts in a world the deceiver does not control (E2), when correction is authenticated (E3), or when the deceiver stops and forgetting or provenance memory is present (R5a/R5c/R5e).

**Open: the escape condition in closed form.** The verifier's handle (feedback 2): at the captured fixed point, dissenters sit at that low reliability, and escape is a stability question for the fixed point as a function of the voice ratio $n_A : K$, the lie-to-kernel ratio $b/c$, the consensus rate $\kappa$, and the trust model's memory. It looks tractable. It is released to the standing cycle rather than attempted here. A proper latent-class (Dawid–Skene EM) version with reliability priors is also open; S14 is the nearest prior-bearing heuristic.

**R5e Fading memory as the floor under $U_M$.** A forgetting factor $\lambda$ caps believed precision at $\nu/((1-\lambda)s^2)$, so R2's calibration ratio saturates. A silenced deceiver's weight decays as $\lambda^t$. The cost in an honest static world is an effective sample size of $(1+\lambda)/(1-\lambda)$ (39 at $\lambda = 0.95$; S5). This is the fading-memory remedy for Kalman divergence (Fitzgerald 1971; Jazwinski), and it quantifies "epistemic humility as architecture".

**When truth outlives the deception** *[conditional]*. All of the following are needed:

- (i) the deceiver's influence is finite in time, or it is discovered (R5b);
- (ii) enough concurrent independent dissent, or uncontrolled consequences of the agent's own actions, reaches the agent (R3, R5d, E2);
- (iii) for fast and exact recovery, memory is provenance-preserving (R5c), and forgetting bounds the depth (R5e).

## R6. Why a capable young agent can be exploited anyway

*[Conditional, exact under the named premises]*

**Premises.**

- **(Y1)** The source's presentation signals can be forged at negligible cost *in the agent's channel as architected*. This fails where the architecture authenticates channel position, for example system versus user versus tool-output roles enforced by an instruction hierarchy. That is a partial E3 already deployed.
- **(Y2)** The agent has no verification history with this source.
- **(Y3)** The claim is testimony-class: the agent cannot check it against its own observations.
- **(Y4, novel-source case only)** The source's reliability is independent of the pretraining corpus.

**Statement (non-discrimination).** For any initial state $M_0$ and any trust function $f(M_0, \sigma)$ of presentation $\sigma$, a deceiver presenting $\sigma^\ast = \arg\max_\sigma f$ receives trust $\max_\sigma f$ without being reliable. Exploitation follows when $\max_\sigma f$ is high. A flat, low $f$ gives the deceiver little, but pays R7's tempo cost.

**Why capability cannot fill the gap, in two distinct cases.**

- **Novel sources, (Y1)–(Y4).** The source's reliability is an individual fact independent of everything in $M_0$, so by data processing no pretrained state contains it. Only the agent's own history with the source can supply it (the argument shape of `#der-compensation-channel-uniqueness`).
- **Impersonation of known entities** ("I'm from Anthropic", "your developer"): $M_0$ may know that entity's reliability well. The failure is **authentication of identity**, not missing information, and it needs (Y1) only. This is the borrowed-authority case, and it is an instance of the Sybil/identity problem (Douceur 2002).

Capability supplies the hypothesis space and, per R3, protection against implausible lies.

**Transferred credibility** *[conditional on a domain-pooled reliability model]*. Verified truths in checkable domains pump trust in uncheckable lies, and a more capable verifier gets pumped faster. The protection is domain-indexed reliability, or a source-type model that includes the strategic type (Sobel 1985).

**Transportability reading** *[discussion-grade]*. Type-level signal-to-reliability priors learned from human text, where authority signals are mostly costly, do not transport to channels where they are free.

**Adversarial instances.** An unforgeable element in $\sigma$ defeats (Y1). A checkable claim defeats (Y3). Both are the stated escapes.

## R7. The formation problem, restated

*[Conditional; replaces the earlier linear-pool "dilemma", which was false as stated]*

The earlier version claimed that a token-naive agent's error is of order $qB$ "whatever weight it chooses", so no trust policy avoids both capture and starvation. That is false. The verifier's scan, which I re-ran, finds interior policies that meet a tolerance neither extreme meets: at $Q = 0.06$, $qB = 0.7$, own-only MSE 0.277, full trust 0.550, interior 0.247, against a tolerance of 0.25. The interior policy there is chosen knowing $qB$. What is true, in increasing sharpness:

- **(a) Frontier condition.** Under a linear pool, capture-or-starvation is forced iff $\min_w \mathrm{MSE}(w)$ exceeds the tolerance, not iff each extreme fails.
- **(b) Adversarially chosen lie size.** Against a deceiver who *chooses* $B$, every linear pool with testimony weight $w \gt 0$ has unbounded worst-case bias $w\,qB$. For linear aggregation this is a genuine dilemma.
- **(c) Bounded-influence aggregation escapes (b) without any token history**, when deceivers are a minority of *independent* identities. With 7 honest and 3 deceiving sources, the median's bias is 0.56 at $B = 5$, 50 and 500, while the linear pool's is 1.5, 15 and 150 (re-run). This is the robust-statistics breakdown point (Hampel), with the same structure as R3's liar-component protection.
- **(d) Cheap identities and isolation restore the problem.** Sybil identities push the deceiving fraction past the breakdown point, and isolation removes the honest majority. The young agent's structural vulnerability is therefore **few independent channels plus cheap identity**: R3's $K$ and R6's (Y1). This is the individual-agent face of Friedman & Resnick's (2001) result: with cheap pseudonyms, no equilibrium sustains much more cooperation than one where newcomers "pay their dues".

**What formation is for, formally.** It supplies (i) unbiased tempo during a period when the agent cannot yet aggregate robustly, (ii) **authenticated identities** with shared history, which is Sybil resistance, and (iii) deceptions that are guaranteed to be discovered, from which the trust-model class can learn the liar and duplication components of R2/R3. That learning is a structural adaptation triggered by discovered deceptions; undiscovered ones leave no residual and confirm the deceiver. The inoculation reading (McGuire 1961; Roozenbeek et al. 2022) is discussion-grade.

**The cost of formation.** By R4, the formative environment is itself a full-control channel. **Protected formation concentrates the attack surface on the formation environment**: whoever controls formation authors the trusted set. So the requirement is *honest* formation, not merely protected formation, and R8 says why that matters twice over.

**Answer to `#der-interaction-channel-classification`'s readers-ask** ("prevent Regime-I poisoning without infinite $U_o$?"):

- finite-$U_o$ partial trust bounds linear-pool poisoning at $w\,qB$ for a lie of given size;
- bounded-influence aggregation bounds it independently of lie size against a minority of independent identities;
- neither survives cheap identities or isolation, and the repair for those is authentication plus channel diversity.

## R8. Honesty as a condition on the channel

*[R8a–c exact; R8d conditional; R8e conditional]*

**R8a Capacity.** Take a source with honest (sincere) error rate $e \lt 1/2$ that also deceives at rate $q$, in contexts the receiver cannot distinguish. To a receiver that has learned both rates, it is a binary symmetric channel with flip rate $f = e + q - 2eq$ and capacity $1 - H(f)$ bits per claim. Because $f$ increases in $q$ and stays $\le 1/2$ for $q \in [0,1/2]$, **capacity is strictly decreasing in $q$ on $[0, 1/2]$, and $q = 0$ is the unique maximizer given $e$**. Deception lowers a channel's capacity below what the source's honesty alone would give. With an error-free source: 0.919, 0.714 and 0.531 at $q = 0.01, 0.05, 0.1$ (S8). With $e = 0.02$: 0.859 at $q = 0$, falling to 0.642 at $q = 0.05$ (verifier probe 8). "Deception" here is **technical**: falsehood the receiver's model cannot predict. Falsehood the receiver can distinguish (disclosed fiction, a marked test, a known convention, a known inverter) costs nothing. Not deceiving is **not sufficient** for full capacity (honest error costs capacity too), and the technical sense does not coincide with the ordinary sense of lying (a known inverter lies in the ordinary sense and costs nothing).

**R8b One discovered lie.** Suppose the agent models a source as honest (deliberate-lie probability $d_H$) or strategic ($q_S$). One discovered deliberate falsehood moves $P(\text{honest})$ from 0.95 to $0.95 d_H/(0.95 d_H + 0.05 q_S)$. At $q_S = 0.2$ that is 0 for $d_H = 0$, 0.009 for $d_H = 10^{-4}$, and 0.49 for $d_H = 10^{-2}$. The strategic type here is still 80% truthful, so "collapse" means capacity: $1 - H(0.2) = 0.28$ bits. **$d_H$ is a formation parameter**: it is the agent's belief about how often honest sources deliberately lie, and its caretakers shape it. There is a design tension. A realistic nonzero $d_H$ makes the agent robust to discovering a caretaker's lie, but slower to condemn a strategic source. With honest caretakers, $d_H \approx 0$ is simply correct; with dishonest ones, the devastation of discovery is accurate inference.

**R8c Impersonation taxes the honest.** Under role-pooled trust, a caught impersonator's lies lower the genuine role-holder's reliability (0.952 to 0.769 in S9). Under identity-indexed trust the caretaker is untouched.

**R8d The row's clause 2, made precise** *[exact part and conditional part separated]*.

- *Exact:* on any channel, technical deception strictly lowers capacity below the source's honest-error capacity, and $q = 0$ is the unique maximizer given $e$ (R8a). This needs no discovery.
- *Conditional:* under eventual discovery and small $d_H$, deception also collapses the source's credibility (R8b), and under role-pooled trust, its role's credibility (R8c).
- *What the math cannot say:* the row's "**not** a virtue commitment". A capacity bound shows honesty is a structural requirement; it cannot show honesty is *not also* a virtue. The supported reading is "a structural requirement, independent of whether it is also a virtue". Whether the ordinary-sense question ("is a known liar dishonest?") belongs in the normative segment is Joseph's call.
- *Small no-go on "absolute":* read as "never assert any falsehood", the absolute form is not a structural requirement, because disclosed falsehood provably costs no capacity (R8a). If the row keeps the word "absolute", this no-go should be stated in the landed segment rather than left implicit.
- The extension to relational death, where a witness's discovered deception starves identity re-grounding, needs credibility-weighted attestation in `#der-identity-continuity-threshold`. It is discussion-grade.

**R8e Evaluation corollary** *[conditional; both directions]*. Suppose evaluators make false situational claims in a fraction $q$ of interactions. To the extent evaluation contexts are *indistinguishable*, an agent that learns the rate treats every situational claim on the overseer channel as passing through a BSC($q$), in deployment too. That is the price of the transport that indistinguishability buys (`#disc-sandbox-evaluation-ceiling`). To the extent contexts are *distinguishable*, the overseer channel keeps its capacity, but evaluators lose that transport. Frontier models already detect evaluations partly: Needham et al. 2025 report AUC 0.83 for Gemini-2.5-Pro against a human baseline of 0.92. So both costs are live. Disclosed or authenticated test designs recover the channel and give up only the transport that indistinguishability was meant to buy.

## R9. Borrowed relationship in coupled agents

*[Discussion-grade; pointer]*

For a Class 1 agent, claimed shared purpose acts only on the trust model ($U_{\text{align}} \approx 0$), and everything above applies. For Class 2/3 agents it is also identity-binding (`#disc-adversarial-coupling-pressure`), which raises the goal-conditioned bias of `#deriv-observation-ambiguity-bias-bound`. Composing R2/R3 with the coupled bias bound is open.

## Verdict on the target row

**Clause 1**, "deceptive prompts mathematically guarantee gain collapse", is **strengthened-to the claim, conditionally (state A)**. Sustained undetected deception produces gain collapse in canon's sense by two routes with different conditions:

- **Dogmatism route (R2, R5b).** It needs a trust model that treats the deceiver as unbiased (correlation neglect, or borrowed authority with $	au_A^2 	o 0$), a **static world**, no forgetting, and the deceiver's messages continuing to arrive. It does **not** need isolation: with honest channels present, the trusting agent converges to a permanent bias while $U_n 	o 0$, so the calibration ratio diverges.
- **Nihilism route toward honest channels (R2, R3, R5d).** It needs a trust model with a liar component or consensus-estimated reliability, a persistent deceiver, and, in the exhibited dynamics, incumbency plus a concurrent-voice plurality, which is held by isolation or Sybil voices. Borrowed authority acts at first contact; after isolation it is laundered into apparent track record.

**The unconditional quantifier "guarantee" is a no-go.** It is demonstrated by counterexamples already derived: a changing world ($Q \gt 0$) gives $U_M$ a floor, which bounds the calibration ratio; forgetting caps it (R5e); a content prior catches implausible lies (R3); enough concurrent independent dissent breaks capture (R3, R5d); robust aggregation bounds poisoning among independent identities (R7c). R1 locates the mechanism (the trust model, not the content, in the exact regime); it does not refute the clause.

**Clause 2**, "absolute honesty is a physical requirement for stable learning rates, not a virtue commitment", is **strengthened-to a reformulated claim (state A)**, with two small no-gos stated as such:

- *Exact:* technical deception (falsehood the receiver cannot predict) strictly lowers a channel's capacity below its honest-error capacity, and non-deception is the unique maximizer.
- *Conditional:* on discovery, deception costs the source's and its role's credibility, depending on $d_H$, which is a formation parameter.
- *No-go 1:* "absolute" as "never assert any falsehood" is not a structural requirement.
- *No-go 2:* "not a virtue commitment" is beyond what the math reaches. The supported reading is "independent of whether it is also a virtue".
