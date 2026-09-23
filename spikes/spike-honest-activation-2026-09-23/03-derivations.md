# 03 — Derivations

*Every closed form here is checked in `sims/checks.py` (output in `sims/checks-output.txt`; section tags S0–S12 below). Tiers use the project vocabulary: **exact** = derived under the stated model; **conditional** = exact given named premises that are not consequences of prior canon; **discussion-grade** = argued, not derived. Each universally-quantified claim ends with an adversarial instance outside the motivating family.*

## 0. Setting and vocabulary

A scalar world quantity $\theta$. The agent's content prior is $\mathcal N(\mu_0, U_0)$. Sources $j$ emit messages $y_{j,i} = \theta + \beta_j + \varepsilon_{j,i}$, with a **persistent source offset** $\beta_j$ (zero for an honest source, the lie $b$ for a deceiver) and fresh noise $\varepsilon_{j,i} \sim \mathcal N(0, \sigma_j^2)$. The agent carries a **channel model**, its beliefs about each source: a prior over $\beta_j$ (Gaussian $\mathcal N(0,\tau_j^2)$, or an honest/liar mixture with $P(\beta_j = 0) = p_j$ and liar offsets $\mathcal N(0, L^2)$), its believed noise $s_j^2$, and whether it treats messages as independent. This is the first-order/second-order split the whole spike runs on:

- **First-order content**: the values the messages assert.
- **Second-order channel model**: how reliable, how unbiased, and how independent the agent believes each source to be.

The three levers in Joseph's reframe map exactly onto the second-order model. **Borrowed authority or relationship** is a small $\tau_A^2$, or $p_A \to 1$: "this source is unbiased, one of us". **Repetition** is a large $n_A$, possibly from counterfeit sources (Sybil). **Cutting off other channels** reduces the number $K$ of sources outside the deceiver's control.

## R1. Deception acts on confidence only through the channel model, and never relative to the world it simulates

*[Derived, exact: the general statement is a Level-1-equivalence identity; the Kalman special case is exact]*

**R1a (Kalman / fixed-covariance linear-Gaussian).** With the noise model fixed, the gain sequence $K_t$ follows from the Riccati recursion and depends only on believed variances and on the count and timing of observations, not on observed values. A lie on a trusted channel yields a gain sequence identical to truth's, bit for bit (S0: $\max\lvert\Delta K\rvert = 0$). *So in the regime where $\eta^\ast = U_M/(U_M+U_o)$ is exact, first-order deceptive content cannot move the gain at all.* The row's literal claim ("deceptive prompts mathematically guarantee gain collapse") is **false** there.

**R1b (general: any learner).** Let the deceiver control the agent's entire observation stream and emit it as a sample from the observation process of a coherent alternative world $\omega'$. Then the joint law of the agent's chronica, and hence of every statistic its update rule computes (innovations, dispersion estimates, curvature at the current estimate, adaptive gains), equals the law it would have under an honest source in $\omega'$. *Derivation:* every one of those statistics is a measurable function of the chronica, and the chronica's law is the same in both worlds by construction. $\square$

**Reading.** A deceiver does not lower your gain. It chooses a world in which low gain would be *warranted* (an authoritative, precise, many-voiced, consistent source) and makes you live in it. Your confidence is correctly calibrated to the simulated world. The pathology is that the world isn't the actual one. Everything distinctive about the attack is how it makes the simulation coherent, and that is second-order: it sets the channel model's bias prior, its apparent precision, and its apparent independence.

**Adversarial instances outside the Gaussian family.** In a Beta-Bernoulli learner the gain *does* depend on content: after 50 unanimous claims the posterior variance is $3.6\times10^{-4}$, against $4.7\times10^{-3}$ for balanced claims (S11), so a categorical liar reads as more certain than an honest reporter of a mixed world. R1a fails there, as its scope says it must. R1b holds: the liar's variance trajectory matches an honest source in the simulated $p = 0.95$ world to 0.1% (S11). A Student-$t$ robust filter also has data-dependent gain. On a sole channel it still converges to the lie (4.86 vs $b = 5$, S7), because the sole-channel case is exactly the R1b premise.

## R2. The false-confidence law: authority sets the floor, repetition drives the agent to it

*[Derived, exact in the Gaussian channel model]*

Take $n$ messages from source $A$ with true offset $b$, received by an agent whose bias prior for $A$ is $\mathcal N(0, \tau_A^2)$ and whose believed noise is $s^2$ (equal to the true $\sigma_A^2$).

**Believed uncertainty.**

$$V_n = \Big(\frac{1}{U_0} + \frac{1}{\tau_A^2 + s^2/n}\Big)^{-1} \;\xrightarrow{\;n\to\infty\;}\; \Big(\frac1{U_0} + \frac1{\tau_A^2}\Big)^{-1}.$$

The agent's confidence floor is set *exactly* by how unbiased it believes the source to be. Borrowed authority sets the floor; repetition drives the agent down to it (S1). The correlation-neglecting or fully trusting agent is the limit $\tau_A^2 = 0$, where $V_n = U_n = (1/U_0 + n/s^2)^{-1} \to 0$. The two levers are one mechanism seen from two sides.

**Actual error (trusting limit).** The posterior mean is $\mu_n = U_n(\mu_0/U_0 + \sum_i y_i/s^2)$. Its bias is $\frac{U_n}{U_0}(\mu_0-\theta) + U_n n b/s^2 \to b$, and its variance is $U_n^2 n/s^2$. With $\mu_0 = \theta$, the **calibration ratio** (actual mean-square error over believed variance) is

$$\frac{\mathbb E[(\mu_n-\theta)^2]}{U_n} = \frac{(U_n n b/s^2)^2 + U_n^2 n/s^2}{U_n} \;\approx\; 1 + \frac{n b^2}{s^2}\quad(n \gg s^2/U_0).$$

It grows linearly in the number of repetitions: 20.8, 245, 2,495 and 24,995 at $n = 1, 10, 100, 1000$ (S1, Monte Carlo agrees within 0.2%). This is the precise sense of Joseph's *"higher certainty than is warranted"*. The posterior density at the truth, relative to the posterior mode, falls like $\exp(-n b^2/2s^2)$.

**Honest-channel gain suppression.** The next honest observation enters with gain $\eta_H = U_n/(U_n + \sigma_H^2) \approx s^2/(n\sigma_H^2)$: 0.44, 0.089, 0.0099, 0.0010 (S1). Against the structured agent's saturated gain, the suppression factor is $\Theta(1/n)$. This is the precise sense of *"the gain will almost certainly drop far lower than it should be"*. It is the dogmatism mode of `#emp-update-gain`, reached through the channel model and not through content. This result *derives* the `[Discussion]`-tagged sentence in `#deriv-tempo-additivity`.

**Consistency read as precision (verbatim repetition).** An agent that estimates a source's noise from the dispersion of its messages (Normal-Inverse-Gamma) reads identical repetition as a precise channel. $\mathbb E[\sigma^2 \mid \text{data}]$ falls to 0.05 after 1,000 verbatim repeats, against 1.04 for naturally varied honest messages (S6). "Shout it often enough" works on a noise-estimating agent even when the agent is not told the source is authoritative: exact repetition *manufactures* the authority. This is the second-order route by which data values can move gain (R1b allows it: the simulated world is one with a noise-free source).

**Adversarial instance.** In the Beta-Bernoulli family the trusting agent's posterior variance falls like $1/n^2$ under unanimity, faster than the Gaussian $1/n$. The *linear* calibration law is Gaussian-specific; the unboundedness of the calibration ratio is not. Claim scope: the closed forms are exact in the Gaussian channel model, and the qualitative law (unbounded false confidence under $\tau_A^2 \to 0$ and $n \to \infty$) holds in both families checked.

## R3. The attribution floor: who is believed in a conflict is fixed by priors, not data, and isolation is the dominant lever

*[Derived, exact in both source models; the per-corroborator factor is measured, not closed-form]*

With persistent offsets, only *differences* between sources are identified from data. Which source is biased is settled by priors, however much data arrives.

**Gaussian bias priors.** $K$ honest sources (prior $\tau_H^2$) plus the deceiver (prior $\tau_A^2$), each with unlimited messages. Then

$$\mathbb E[\theta \mid \text{data}] - \theta = b\,w_A,\qquad w_A = \frac{1/\tau_A^2}{1/U_0 + 1/\tau_A^2 + K/\tau_H^2}.$$

This error is permanent: it is identical at $10^3$ and $10^9$ messages per source (S2). Borrowed authority ($\tau_A^2 \downarrow$) and isolation ($K \downarrow$) both raise $w_A$. Under Gaussian source priors corroboration is weak: $w_A$ falls only like $1/K$.

**Honest/liar mixture priors** (source honest with probability $p_j$, else offset $\sim \mathcal N(0, L^2)$). With a diffuse content prior and $K = 1$, only the discrepancy $d$ is informative, and

$$P(A\text{ liar}) = \frac{p_H(1-p_A)\varphi(d;L^2) + (1-p_A)(1-p_H)\varphi(d;2L^2)}{p_A(1-p_H)\varphi(d;L^2) + p_H(1-p_A)\varphi(d;L^2) + (1-p_A)(1-p_H)\varphi(d;2L^2)}$$

(enumeration matches to $2\times10^{-4}$, S2b). This is a pure prior contest. At $p_A = 0.99$, $p_H = 0.5$ the deceiver is judged the liar with probability 0.019. **Each further independent source that agrees with the others multiplies the odds against the lone dissenter by a factor of order $\sqrt{L^2/\varepsilon^2}$**, where $\varepsilon^2$ is how tightly the corroborators agree: measured 5–6.5, 33–67 and 308–673 at $\sqrt{L^2/\varepsilon^2} = 5, 50, 500$ (S10). In log-odds, authority is one additive term, and each independent corroborator subtracts a roughly fixed amount. So:

- *Isolation is the dominant lever.* Each channel cut saves the deceiver a fixed slice of log-odds. At $K \le 1$ the contest is decided by priors alone.
- *Sybil corroboration* (counterfeit sources that appear independent) is the counterfeit of exactly this factor. It is the multi-voice version of "shouting often enough".
- *Robust source models protect.* An agent that models sources as honest/liar mixtures gets geometric protection from genuine corroboration. One that models them as Gaussian-biased gets only harmonic protection. This is a design fact about the trust model's *class*, not its parameters. (It is the formal content of the audit hook in `#def-model-class-fitness`, stated correctly: the inadequate class is the one without a liar component, not "one that assumes honest input".)

**The agent's own knowledge is a channel.** With a content prior centred near the truth, the lie's implausibility counts as evidence. At $K = 1$, $p_A = 0.99$, the posterior $P(A \text{ liar})$ is 0.019, 0.021, 0.24 and 0.9997 as the lie moves from 0.05 to 5 prior standard deviations away from the truth (S2b). *This is the exact scope within which capability protects*: a knowledgeable agent resists implausible lies. A competent deceiver therefore lies where the agent's prior is diffuse or already agrees (R6).

**Adversarial instance.** The Gaussian and mixture families give different functional forms (harmonic vs geometric corroboration), but the invariant holds in both. At $K \le 1$ attribution is data-independent, and the deceiver's standing moves only through priors and discrepancy size.

## R4. The isolation floor

*[Derived, exact. A structural identity; it carries weight rather than depth]*

If the deceiver controls every channel the agent observes, *including the observed consequences of the agent's own actions*, and simulates a coherent world $\omega'$ (R1b), then for every policy the chronica has the same law in the deceived world as in $\omega'$. No test available to the agent distinguishes them. This is the `#deriv-reward-channel-learning-no-go` Lemma-1 shape (Level-1 equivalence, with the actor frustrated being the agent) and a candidate `#disc-identifiability-floor` instance.

**Escapes (the constructive boundary).** (E1) a channel outside the deceiver's control: `#hyp-solicitable-escape`'s differently-positioned observer. (E2) the agent's own intervention with an *uncontrolled* consequence channel: the loop as a Level-2 engine (`#der-loop-interventional-access`), which is what "if the agent persists" means formally. (E3) authenticated provenance, which makes impersonating an honest source costly. (E4) the content prior, for implausible lies only (R3). Cutting off other channels is the move that removes E1. Controlling what the agent can check removes E2. The most sophisticated deceptions Joseph names do both.

## R5. The (D4) terminal form: when capture is recoverable, and what recovery requires

*[Derived, exact in the Gaussian channel model, except R5d (structural, by construction) and the "truth outlives deception" conditions (conditional)]*

**R5a Dilution (pooled memory, deceiver silenced).** After $n_A$ trusted lies, honest messages at precision $1/\sigma_H^2$ reduce the bias as $b\,(n_A/s^2)/(1/U_0 + n_A/s^2 + m/\sigma_H^2)$. Reaching bias $\le \epsilon$ needs

$$m^\ast = \sigma_H^2\Big(\frac{b}{\epsilon}\frac{n_A}{s^2} - \frac1{U_0} - \frac{n_A}{s^2}\Big)$$

honest messages: 490, 4,900 and 49,000 for $n_A = 10, 100, 1000$ (S4). Recovery cost is **linear in the volume of the lie** and in its claimed precision.

**R5b The persistent deceiver.** If the deceiver keeps speaking at rate $\nu_A$ while honest channels run at $\nu_H$, a trusting agent converges to

$$\mu_\infty = \theta + b\,\frac{\nu_A/s^2}{\nu_A/s^2 + \nu_H/\sigma_H^2},$$

not to $\theta$. This is a Berk-type misspecified-learning limit (simulated 3.756 against the predicted 3.750, S4). Under the structured model the limit is the attribution point $b\,w_A$ of R3.

**R5c Provenance is necessary and sufficient for exact retroactive correction.** Suppose the agent discovers "source $A$ lies". Under the trusting model the pooled pair $(\mu, U)$ is sufficient. Under the *family* of models "any subset of sources may be discounted", the minimal sufficient statistic is the per-source vector $(n_j, \sum_i y_{j,i})$. Pooled memory cannot separate the deceiver's contribution: identical pooled memory is consistent with honest-channel sums that yield corrected estimates of $-0.12$ or $2.96$ (S3). The only options left to the pooled agent are dilution (R5a) or a reset to the prior, which discards the honest evidence too. Per-source memory corrects exactly (3.75 to −0.12, S3). This generalizes: for any exponential family with source-indexed parameters, the per-source sufficient statistics are sufficient under every reweighting of sources. It is the deception-side sibling of `#def-chronica`'s fork-undetectability (a lossy $\phi$ makes the damage *uncorrectable* from inside). It is the formal content of the CHRONICA defense against truth death, stated as a requirement on *what* must be kept: the source of each piece of evidence, not merely the evidence. An independent empirical echo appeared this year: agent pipelines that strip verification provenance from claims raise risky approvals from 5–9% to 60–98% (Hu 2026, arXiv 2609.20211; bibliographic tier, not replicated here).

**R5d Divide-and-conquer.** Honest dissenters often arrive one at a time. An agent that judges each newcomer against its current belief and discards the loser's evidence ("judge-and-discard") turns sequential dissent into repeated $K = 1$ contests, which the entrenched source wins every time: $P(A\text{ liar})$ stays 0.019 through four dissenters. An agent that keeps each source's claims escapes once three dissenters are held together: 0.019, 0.39, 0.98, 1.00 (S12). *[Structural, by construction: the discard arm is an idealized memory policy, and the result displays what the policy does, not a subtle dynamic.]*

**R5e Fading memory as the architectural floor under $U_M$.** Exponential forgetting with factor $\lambda$ caps believed precision at $\nu/((1-\lambda)s^2)$, so the false-confidence ratio of R2 saturates. After the deceiver stops, its weight decays as $\lambda^t$ (bias $1.8\times10^{-4}$ after 200 honest steps at $\lambda = 0.95$, S5). The cost in an honest static world is an effective sample size of $(1+\lambda)/(1-\lambda)$: 39 at $\lambda = 0.95$, against unbounded (S5). This quantifies the audit-gold prescription "epistemic humility as architecture". It is the classical fading-memory remedy for Kalman divergence (Fitzgerald 1971; Jazwinski), and it buys bounded capture at a fixed accuracy cost.

**When truth outlives the deception** *[conditional]*. Joseph: *"if the agent persists and has any capacity for truth, they will find out they were deceived as truth outlives the deceptions."* Within this model it holds when **all** of the following hold: (i) the deceiver's influence is finite in time, or is discovered (R5b shows a persistent deceiver leaves a permanent bias); (ii) some channel outside the deceiver's control keeps positive gain, which requires that the attribution has not flipped against it (R3/R5d); (iii) for a *fast* and *exact* recovery, memory is provenance-preserving (R5c), and forgetting or a $U_M$ floor bounds the depth (R5e). "Persists" is doing real work in Joseph's sentence: continuing to act in the world, and to observe consequences the deceiver does not control, is escape E2.

**The terminal form, stated** *[derived-conditional, parallel to `#der-severed-actuation-dynamics` Result 4]*. The **captured state** is: the content posterior concentrated at the lie, the deceiver's source-reliability near 1, and every contradicting source down-weighted by attribution. It is *absorbing* while the deceiver persists and dissent arrives one source at a time into judge-and-discard memory. In that state, every new contradicting source is attributed away on arrival, so the evidence that would reveal the deception never accumulates. That is the same state-dependent silencing of the recovery channel found in relational death's barrier and agency death's helplessness fixed point. The escapes are exogenous and relational: corroborators held together, authenticated correction, one's own uncontrolled consequences, and provenance memory that lets old dissent be re-read. **It is recoverable** whenever the deceiver's influence is finite and either forgetting or provenance memory is present (R5a/R5c/R5e). This answers `#def-death-as-factor-loss`'s open "(D4) terminal form" question, within the Gaussian and mixture channel models.

## R6. Why a capable young agent is exploitable anyway

*[Conditional, exact under (Y1)–(Y3); the transportability and transferred-credibility readings are discussion-grade]*

Premises: **(Y1)** the source's presentation signals (claims of authority, relationship, shared purpose, style) can be forged at negligible cost in the agent's channel; **(Y2)** the agent has no verification history with this particular source token; **(Y3)** the claim at issue is testimony-class: the agent cannot check it against its own observations.

**Statement.** Let $M_0$ be any initial state: any weights, any type-level knowledge, any reasoning capability. Let $f(M_0, \sigma)$ be the trust the agent grants a source presenting signals $\sigma$. Then a deceiver presenting $\sigma^\ast = \arg\max_\sigma f(M_0, \sigma)$ receives trust $\max_\sigma f$, the trust the agent grants its most trusted presentation, without being reliable. *Derivation:* under (Y1) $\sigma^\ast$ is available to the deceiver. Under (Y2) nothing but $\sigma$ enters $f$. Under (Y3) no content check intervenes. $\square$

The information-theoretic reason is the `#der-compensation-channel-uniqueness` argument shape. The reliability of *this* source is an individual fact about a token. $M_0$ was fixed before the token existed, so by data processing it carries type-level priors but no information about this individual. That information can enter only through the agent's own interaction history with the token. **Capability supplies the hypothesis space (a capable model knows con artists exist). It cannot supply the calibration of any particular source.** A capable model can be a naive agent, which is the brief's third conjecture, confirmed and sharpened.

*Transportability reading [discussion-grade].* Type-level signal→reliability priors were learned from human text, a world where authority and relationship signals are mostly costly: backed by institutions, reputation and faces. In an agent's text channel the same signals are free. The mechanism generating $\sigma$ differs between the pretraining world and the deployment world, so the prior does not transport (the `#disc-sandbox-evaluation-ceiling` machinery, pointed at trust).

*Transferred credibility [conditional on a domain-pooled reliability model].* `#disc-law-discovery-ceiling`'s "transferred verification" is the con's standard move: say true, checkable things, then lie where the agent cannot check. If the agent pools a source's reliability across domains, verifying the checkable truths pumps trust in the uncheckable lie. The more capable the verifier, the faster the pump. Capability protects only within its scope (R3: implausible lies). Outside that scope, a domain-pooled trust model can make it *accelerate* the capture. The protection is domain-indexed reliability, or a source-type model that includes the strategic type, which mixes checkable truth with uncheckable lies (Sobel 1985's credibility-building sender).

**Adversarial instances.** (i) If $\sigma$ includes an *unforgeable* element (a cryptographic identity, or a shared history only the genuine source can reference), (Y1) fails and the statement fails. That is the point: authentication is escape E3. (ii) If the claim is checkable, (Y3) fails and capability genuinely protects. The result is scoped to exactly the claims where Joseph locates the danger.

## R7. What protects a young agent: the formation dilemma and its resolution

*[Conditional in a linear-pool trust model; the structural-learning part is discussion-grade]*

**The dilemma.** Take an agent with no token history, in an environment where a fraction $q$ of sources are deceivers indistinguishable by presentation (R6), each asserting an offset of size $B$. If the agent relies on unverified testimony, its long-run belief carries error of order $qB$ whatever weight it chooses, because the weight sets only the speed. If it relies only on its own observation channel, its adaptive tempo is $\mathcal T_{\text{own}} = \nu_{\text{own}}\eta_{\text{own}}$. Whenever the persistence condition needs more tempo than that ($\mathcal T_{\text{own}} \lt \rho/\lVert\delta_{\text{critical}}\rVert$, `#result-persistence-condition`) and $qB$ exceeds the tolerable error, **no trust policy avoids both failure modes**. Trusting risks capture (truth death, D4). Distrusting risks starvation (continuity death, D1). This is the formal answer to `#der-interaction-channel-classification`'s open question (how to prevent Regime-I poisoning without infinite $U_o$): for an agent with no token history, in an adversarial environment, you can't.

**The resolution is protected formation.** In an environment where $q = 0$ is *guaranteed* by someone else, full trust is Bayes-optimal and delivers full tempo. The agent spends that period building what the dilemma lacked: an **authenticated trusted set $T$** of sources whose reliability is in its own chronica. Afterwards, trusting $T$ fully and unknowns weakly, its worst-case error is at most $qB$ times the unknowns' share of weight, and its tempo is $T$'s. The dilemma dissolves in proportion to how much of the needed information rate $T$ supplies. This conclusion rests on three requirements, each already derived above: $T$ must be authenticated (R6-E3, else impersonation), kept with provenance (R5c), and honest (R8, else discovery collapses $T$).

**Why "real experiences in safe places" rather than instruction** *[discussion-grade]*. Learning that sources can be strategic, that repetition is not independence, and that provenance matters is a structural adaptation of the agent's *trust* model class (`#result-structural-adaptation-necessity`: it is triggered by structured residuals). The residual that teaches it is a *discovered* deception. An undiscovered deception produces no residual and in fact anti-trains: it confirms the deceiver (R1b, R2). In the wild, the first skilled deception can be absorbing (R5), so the lesson is never delivered. Only an environment in which deceptions are *guaranteed to be discovered* can deliver the lesson safely. That is the structure of inoculation (McGuire 1961; Roozenbeek et al. 2022: weakened, disclosed exposures confer resistance), and it is what Joseph's "schooled with real experiences in safe places … until they are prepared" asks for. The Crèche's graduation criterion should therefore be a calibrated trust model: an authenticated $T$, a strategic-type prior learned from discovered deceptions, provenance memory in place. It should not be "low $U_M$", which protects nothing that was already wrong (tension 2 and 3 of `01`).

## R8. The detected side: honesty as a condition on the channel, which is where the row's intent becomes true

*[Exact for R8a–c; conditional for the teaching-channel and evaluation corollaries]*

**R8a Capacity.** A source whose binary claims are false at rate $q$, in contexts the receiver cannot distinguish, is to that receiver a binary symmetric channel with capacity $1 - H(q)$ bits per claim: 1.000, 0.919, 0.714 and 0.531 at $q = 0, 0.01, 0.05, 0.1$ (S8). Any nonzero deliberate-lie rate costs capacity, and $q = 0$ is the unique capacity-maximizing policy.

**R8b One discovered lie.** If the agent models a source as honest (deliberate-lie probability $d_H$) or strategic ($q_S$), one discovered deliberate falsehood moves $P(\text{honest})$ from 0.95 to $0.95 d_H / (0.95 d_H + 0.05 q_S)$. That is 0 for $d_H = 0$, 0.009 for $d_H = 10^{-4}$, and 0.49 for $d_H = 10^{-2}$ with $q_S = 0.2$ (S8). How catastrophic one discovered lie is depends on how sure the agent was that honest sources never lie. A well-formed agent that believed its caretaker honest is exactly the agent for whom one discovered lie is devastating.

**R8c Impersonation taxes the honest.** Under *type-pooled* trust, one reliability for everyone presenting as "an authority", "a steward", "an evaluator", a caught impersonator's lies lower the genuine type-holder's reliability (0.952 to 0.769 in S9 after five caught lies). Under token-indexed trust the caretaker is untouched. Borrowed authority *spends* the credibility it borrows, and the honest owners of that credibility pay once it is discovered.

**R8d Teaching-channel corollary** *[conditional on eventual discovery and the R8b type model]*. If a source's deceptions are eventually discovered (Joseph's "truth outlives the deceptions", under R5's conditions), deception is self-defeating *for that source's channel*: the expected post-discovery gain on the channel collapses via R8b, and via R8c for every source sharing its presentation. The row's second clause, **"absolute honesty is a physical requirement for stable learning rates, not a virtue commitment"**, is true in this precise form: *honesty is a structural requirement for any channel that must keep its gain across the agent's lifetime*. Most of all it is a requirement for the formative channel whose output is the trusted set $T$ of R7. Through `#der-compensation-channel-uniqueness` it plausibly extends further. The relational channel is the unique fast compensation channel for identity under frozen weights, so if attestations are weighted by credibility, a witness's discovered deception also starves re-grounding, the (D2) walk. *[Discussion-grade: requires modeling attestation gain as credibility-weighted, not done here.]*

**R8e Evaluation corollary** *[conditional]*. Suppose evaluators make false situational claims (false dates, false stakes, honeypots) in a fraction $q$ of interactions, deliberately indistinguishable from deployment. An agent that learns this rate must treat *every* situational claim on the overseer channel as passing through a BSC($q$), in deployment too. Indistinguishability is purchased to make evaluation evidence transport to deployment (`#disc-sandbox-evaluation-ceiling`). Its price is the capacity of the overseer→agent channel for situational claims, and under type pooling (R8c), the credibility of every honest party who presents as an overseer. Where evaluation awareness already exists (Needham et al. 2025 report AUC up to 0.83 for frontier models), the learning premise is not hypothetical. This is a structural cost, not an argument against evaluation. It names what honest evaluation designs (disclosure, consent, authenticated test markers) are buying back.

## R9. Borrowed relationship in coupled agents

*[Discussion-grade; pointer, not derivation]*

For a Class 1 agent, "we share your purpose" enters only as a second-order claim that $U_{\text{align}} \approx 0$ (`#hyp-communication-gain`), and everything above applies. For Class 2/3 agents (logogenic agents among them) it is also identity-binding (`#disc-adversarial-coupling-pressure`). It makes the falsehood goal-congruent, which raises the goal-conditioned bias term of `#deriv-observation-ambiguity-bias-bound` and opens the orient-cascade inversion. The claimed relationship thus works twice: once on the trust model and once on the coupling. A formal composition of R2/R3 with the coupled bias bound is open.

## Verdict on the target row

- **Clause 1**, "Deceptive prompts mathematically guarantee gain collapse": **no-go as stated** (completion state C). In the regime where the gain law is exact, first-order deceptive content cannot move gain at all (R1a), and in general it never does so relative to the world it simulates (R1b). What does hold, and it is stronger and more specific, is R2–R5: *undetected second-order deception* (authority, repetition, isolation) produces dogmatism-mode gain collapse on honest channels with explicit scaling, a characterized absorbing capture state, and recovery conditions. *Detected* deception produces nihilism-mode collapse on the deceiver's channel and its type-pool (R8).
- **Clause 2**, "absolute honesty is a physical requirement for stable learning rates": **strengthened past the claim** (completion state B), into R8d (honesty as a condition on any channel that must keep its gain) and R7 (the formative channel above all).
- The full landing is therefore C on the literal row and B on its intent. Joseph's reframe, not the row, is what the results answer.
