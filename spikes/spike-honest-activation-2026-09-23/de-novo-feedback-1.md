# De-novo feedback 1: independent adversarial pass on the honest-activation spike

*Auditor: an Opus 5.5 instance, 2026-09-23, not the spiker. Read in full: every file in this directory, `sims/checks.py` and its output, `doc/sop/spikes.sop.md`, `doc/audit-routing-instructions.md`, `doc/sop/agents.sop.md`, the spike's brief (`~/src/aisi-eoi/spikes/briefs/2026-09-23-honest-activation-spike.md`, read **after** my own derivation pass so it could not prime it), and the canon passages the spike leans on hardest (`#def-death-as-factor-loss` whole, `#obs-developmental-trajectory` whole, the cited passages of `#emp-update-gain`, `#deriv-tempo-additivity`, `#hyp-communication-gain`, `#der-interaction-channel-classification`, `#result-persistence-condition`, `#der-severed-actuation-dynamics`, `#der-compensation-channel-uniqueness`). Like the spike, I honored the brief's exclusion of `~/src/AISI-responses/`. The closed forms were re-derived by hand from the text, not from the intent. `sims/checks.py` re-run: output byte-identical to `sims/checks-output.txt`. My own checks are in `de-novo-feedback-1-checks.py`, with output in `de-novo-feedback-1-checks-output.txt`.*

## Summary

The algebra is sound almost everywhere I re-derived it. The trouble is the **verdicts and headline sentences**: several read more into the math than it supports, and in both directions. Two carry weight for routing, and one is a real mathematical defect:

1. **Clause 1 is labelled a no-go (state C), but by canon's own definition of gain collapse the spike's R2 proves clause 1 true under named conditions.** What the spike refutes is "the *content* of a lie lowers gain", a reading the row never states. Routed as C, integration-is-replacement would delete the clause, and canon would then imply "deception does not cause gain collapse". That is false by R2. (F1, F2)
2. **R7's formation dilemma is false as stated.** It leaves out interior trust policies, and it contradicts the spike's own R5b and its own post-formation formula. The true statement is narrower and more interesting. It is a dilemma only for linear pooling against an adversary who picks the size of the lie; bounded-influence aggregation among independent identities escapes it without any token history; and Sybil identities (cheap identities) restore it. Integration-plan item 5 would put the overclaim into canon as the answer to an open readers-ask. (F5)
3. **R8 supports "indistinguishable falsehood costs channel capacity", not "absolute honesty".** Clause 2's "strengthened past the claim" (B) label outruns the derivation. (F8)

Other findings: the gain-suppression numbers presented as a deception effect are bit-identical under an honest source (F3); the outsider statement's first claim is contradicted by the spike's own drills (F4); the (D4) "absorbing" terminal form rests on a policy the spike itself calls by-construction (F6); the corroboration factor the spike calls "measured, not closed-form" has an asymptotic closed form, and that form exposes a reversal the debrief misdescribes (F7); plus a DPI mis-location in R6, a partial misreading of one canon segment, a provenance slip, and literature gaps, including three verified hits that are close prior art for R6/R7 and R2 (F9–F12).

What holds up is listed at the end. Much of it holds up well.

## F1. Clause 1: the verdict refutes a reading the row does not make; by canon's definition the clause is conditionally true

**Canon's definition.** `#emp-update-gain:19,52`: gain collapse is *"When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^\ast \to 0$"*. `#def-death-as-factor-loss` (D4) repeats it: *"$U_M \to 0$ inappropriately … or $U_o \to \infty$ inappropriately"*. PROPRIUM-A-v2 §8, the row's other ancestor (which the spike's own `01` §1 quotes), says the same thing: *"$U_M \to 0$ inappropriately — Confidently wrong; can't learn from correction."* The load-bearing word in every version is *inappropriately* (or *spurious*, *incorrectly*).

**What R1a actually shows.** Under a fixed-covariance Kalman filter, the gain sequence under a lie equals the gain sequence under truth. That is true. It is also silent on the definition above, because the definition is about $U_M$ relative to the *actual* error, and R1a compares $K_t$ to $K_t$. In a static world ($Q = 0$) both sequences go to zero. Truth's collapse is appropriate; the lie's is not. R1a cannot tell the two apart. The discriminant is the actual error, and that is exactly what R2 computes.

**What R2 proves.** Take a trusting channel model ($\tau_A^2 \to 0$), sustained repetition, no forgetting, and a static world. The ratio of actual to believed error is $\approx 1 + nb^2/s^2 \to \infty$. That is $U_M \to 0$ *inappropriately*, which is canon's gain collapse by definition. On the honest channel the gain is $\approx s^2/(n\sigma_H^2) \to 0$, while the oracle-optimal gain stays near $b^2/(b^2+\sigma_H^2)$ (0.96 in S1's setting; see F3). R2 is therefore a conditional theorem whose conclusion is clause 1.

**The honest completion-state reading**, as I see it:

- **Strengthened-to the claim (A), conditional.** *Sustained undetected deception on a channel the agent models as unbiased produces gain collapse in canon's sense, with calibration ratio $\approx 1 + nb^2/s^2$.* The mixture-model capture delivers the other mode (F2).
- **A no-go on the unconditional quantifier "guarantee".** The spike already holds the counterexamples: forgetting caps the ratio (R5e); a content prior catches implausible lies (R3); three or more held corroborators under a liar-component model escape (R3/S12); and process noise $Q \gt 0$ keeps gain positive (S0's own setting).
- **A no-go on "content moves gain"**, but that is the brief's guess, not the row. The brief says: *"taken literally it may point the wrong way, since undetected deception need not lower update gain at all"*, and `01` §3 tension 1 records *"The coordinator's guess in the brief was right about first-order content."* This looks like a priming path from brief to verdict. It is worth knowing as feedback on the brief: an unverified guess about the literal reading arrived as setting and became the reading refuted.

**Why this matters for routing.** Under audit-routing §4, a C verdict triggers FALSE-marking and deletion of the refuted claim. Deleting clause 1 and landing R1 as its replacement would leave canon asserting, in effect, "deception acts through the channel model, not by collapsing gain". That is a false present-truth statement, because R2 *is* deception-driven gain collapse. The debrief's section heading *"The first clause is false"* would mislead Joseph the same way. The spike's content is right; its label points the integrator in the wrong direction.

## F2. Undetected deception realizes both collapse modes, and the mixture capture is the nihilism mode on honest channels

The verdict bullet says: undetected → dogmatism ($U_M \to 0$); detected → nihilism on the deceiver's channel (R8). Re-deriving R3's mixture case gives something different. In the captured configuration the honest dissenter is attributed as the liar, with posterior weight about $1 - 0.019$ at $p_A = 0.99$, $K = 1$. A source judged a liar has an offset with prior spread $L^2$, so it carries almost no information about $\theta$. In effect its $U_o \to \infty$. The posterior mean sits near $b\,P(A\text{ honest}) \approx 0.98\,b$, and the honest channel's influence is about $P(A\text{ liar})$. So **undetected** deception under a liar-component trust model produces **spurious $U_o \to \infty$ on the honest channel**, which is canon's nihilism mode, not dogmatism. The trust-model class decides which mode appears: correlation neglect gives dogmatism; a liar-component model gives nihilism on honest channels. This strengthens F1 (both of canon's modes are realized) and corrects the verdict's mode assignment.

**Consequence for integration-plan item 2 (the D4 terminal form).** `#def-death-as-factor-loss`'s severing-source axis currently says *"For (D4) the driven columns instantiate M4's two modularity-decreasing operations (#disc-adversarial-coupling-pressure externally-driven …)"*. The spike's capture route runs through the trust model and is fully available to a GUC Class 1 (Separated) agent. It is not a modularity-decreasing operation at all. So landing R5 as the D4 terminal form means amending that axis sentence: externally driven truth death has a second, non-coupling route. The integration plan doesn't flag this, and the conflict would otherwise surface later as a canon inconsistency.

## F3. The "honest-channel gain suppression" numbers are not a deception effect

R2 gives $\eta_H$ = 0.44, 0.089, 0.0099, 0.0010, and the debrief presents them as *"Its gain on any honest source falls like one over the number of repetitions … That is your 'gain drops far lower than it should'"*. By the spike's own R1a, those four numbers are **bit-identical when the $n$ messages are honest**. Under an honest source they are also *correct*: the oracle gain under truth is 0.39, 0.087, 0.0099, 0.0010 (auditor check B). The quantity that captures "lower than it should" is believed gain against oracle gain *under the lie*: 0.44 vs 0.94, 0.089 vs 0.96, 0.0099 vs 0.96, 0.0010 vs 0.96. The suppression factor relative to the oracle is essentially the calibration ratio, so the spike has one quantity, not two. R2's comparison against the "structured agent's saturated gain" compares to another miscalibrated agent (that agent's error is $b\,w_A = 4.0$ at $K = 0$, $\tau^2 = 1$), not to what the agent *should* do.

Suggested fix: state the suppression against the oracle, and fold it into the calibration law rather than presenting it as a second effect. In outsider claim 2, *"it stops listening to honest sources in the same proportion"* is true only as a statement about the gap, not about the gain itself.

## F4. R1's headline and outsider claim 1 overreach the spike's own drills

R1's title says deception acts on confidence *"only through the channel model"*. Outsider claim 1 says: *"In standard learning models the content of a lie cannot change how much the agent listens."* Four counterexamples already exist inside the spike or canon: S11 (Beta-Bernoulli: unanimous content cuts variance about 13×), S7 (the Student-$t$ filter has content-dependent gain), S6 (verbatim content drives the estimated noise to 0.05), and canon's own `#deriv-adaptive-gain-dynamics` (Mehra: innovations, which are content, set the gain). In any learner that estimates its channel model from data, content *is* the input to the channel model. So the first-order/second-order split is not a partition, and "only through the channel model" is either true by definition or false.

What survives is R1b, the simulated-world equivalence. Two notes on it:

- **(a)** R1b is the same identity as R4: full control of the observation stream, including consequences, gives Level-1 equivalence. Two results carry one identity.
- **(b)** It holds only under *full* control. Under partial control, the realistic case the spike lists as open, there is no simulated world, so R1b does not support *"in general it never does so relative to the world it simulates"*.

Suggestion: merge R1b into R4. State R1a with its scope (fixed-covariance linear-Gaussian). Drop the "only through" headline. In the outsider statement, replace claim 1 with what the drills support: *the most effective deceptions work by making the agent believe a source is unbiased, precise and independent; in the simplest learning models the lie's content alone does not change how much the agent listens, but in agents that judge sources by their outputs, consistency and repetition in the content are themselves the lever* (S6). That last clause is also more useful to an AISI reader than the current one.

A related model-class point that S6 raises and the spike does not draw out: the Normal-Inverse-Gamma agent reads verbatim repetition as precision *because its model class has no duplication hypothesis*. Under continuous noise, identical real-valued messages have probability zero unless they were copied. This is the same model-class inadequacy R3 names for trust ("no liar component"), one level down. The defense against "shout it often enough" is a copy/duplication component, which collapses $n$ identical messages to one. I'd put this beside R3's `#def-model-class-fitness` correction.

## F5. R7's formation dilemma is false as stated; the true statement is sharper

**The claim.** *"If the agent relies on unverified testimony, its long-run belief carries error of order $qB$ whatever weight it chooses, because the weight sets only the speed … Whenever [$\mathcal T_{\text{own}} \lt \rho/\lVert\delta_{\text{critical}}\rVert$] and $qB$ exceeds the tolerable error, **no trust policy avoids both failure modes**."*

**Three internal inconsistencies.**

- (i) R5b's own limit, $b\,(\nu_A/s^2)/(\nu_A/s^2 + \nu_H/\sigma_H^2)$, depends on the weights. With an unbiased own channel running, the long-run error is weight-share $\times\, qB$, not $qB$ "whatever weight".
- (ii) R7's own post-formation formula (*"worst-case error at most $qB$ times the unknowns' share of weight"*) is the interior policy, and the dilemma denies that policy exists before formation.
- (iii) R3 shows a mixture-model agent with no token history defeating a lone liar once enough independent sources agree.

**Counterexample (auditor check C).** A steady-state tracker with a random-walk world (disturbance $Q$), an own channel (noise $R_o = 1$), and pooled testimony (noise $R_T = 0.001$, bias $qB$). Tolerance is $\mathrm{MSE} \leq 0.25$ ($\lVert\delta_{\text{critical}}\rVert = 0.5$). At $Q = 0.06$, $qB = 0.7$:

| Policy | MSE | Meets tolerance? |
|---|---|---|
| Own channel only, best gain | 0.277 | No (starvation) |
| Full trust in testimony (bias $\approx qB \gt 0.5$) | 0.550 | No (capture) |
| Interior: $k_o = 0.24$, $k_T$ small, bias 0.17 | 0.247 | **Yes** |

At $Q = 0.07$, $qB = 0.55$: own-only 0.302, full trust 0.373, interior 0.246. The spike's two-sided condition is met in both cases, and a policy avoids both failure modes.

**What is true, in increasing sharpness:**

- (a) Under a linear pool the dilemma is a **frontier condition**: it holds iff $\min_w \mathrm{MSE}(w) \gt \lVert\delta_{\text{critical}}\rVert^2$, not iff each extreme fails.
- (b) Against an adversary who **chooses $B$**, any linear pool with testimony weight $w \gt 0$ has unbounded worst-case bias ($w \cdot qB$ with $B$ free). *That* is a genuine dilemma, and it is probably what the spike's intuition was tracking.
- (c) **Bounded-influence aggregation escapes it without token history** when the deceivers are a minority of *independent* identities. With 7 honest and 3 deceiving sources, the median's bias is 0.56 at $B$ = 5, 50 and 500, while the linear pool's is 1.5, 15 and 150 (auditor check, last section). This is the robust-statistics breakdown point, the same structure as R3's liar-component protection.
- (d) **Cheap identities restore the dilemma**: Sybil sources push the deceiving fraction past the breakdown point. So the young agent's structural vulnerability is *few channels* (R3's $K$) plus *cheap identity* (R6's (Y1)). Both are already derived elsewhere in the spike. R7's linear-pool dilemma adds nothing beyond them and is false in its stated form.

**What survives of protected formation.** Its job, formally, is to supply an unbiased tempo source and *authenticated identities* (Sybil resistance through shared history), not to break a linear-pool dilemma. That is a cleaner and more defensible statement for Joseph's AISI argument. One consequence the spike doesn't state, which an AISI reader will ask about: by R4, the formative environment is itself a full-control channel. **Protected formation concentrates the attack surface on the formation environment**: whoever controls formation authors $T$. The protection is only as good as the guarantor. The honest form is "honest formation", not just "protected formation", and the spike's own R8b says why that matters doubly.

**Routing.** Integration-plan item 5 proposes answering `#der-interaction-channel-classification`'s readers-ask (*"How is Regime-I poisoning prevented without infinite $U_o$?"*) with *"for an agent with no token history, in an adversarial environment, you can't."* By (a)–(c), that answer is false. The truer answer: finite-$U_o$ partial trust bounds linear-pool poisoning at $w \cdot qB$; bounded-influence aggregation bounds it independently of $B$ against a minority of independent identities; neither survives cheap identities or isolation.

R7 is also the one universal claim in the spike that did not get the brief's "adversarial instance outside the motivating family" drill.

## F6. The (D4) terminal form is absorbing only by construction

R5's terminal form is *"absorbing while the deceiver persists and dissent arrives one source at a time into judge-and-discard memory"*. R5d, the only support for absorption, is labelled by the spike itself *"structural, by construction: the discard arm is an idealized memory policy"*. S12's discard arm prints one number four times. With full memory and a persistent deceiver, the agent sits at the attribution point $b\,w_A$ (a permanent bias), but the state is **not** absorbing: accumulating independent dissent overturns it (S12 full arm: 0.019, 0.39, 0.98, 1.00). So the conclusion "answers `#def-death-as-factor-loss`'s open (D4) terminal-form question" overreaches. What is derived is that *capture is absorbing iff the memory policy discards dissent on arrival and the deceiver persists.* The memory policy is a premise, not a dynamic. Compare `#der-severed-actuation-dynamics` Result 4, the template R5 claims to parallel: there, helplessness arises from the agent's own learning dynamics (credence convergence), not from an assumed discard rule. An honest parallel would need a derivation showing some *natural* update rule (for example, MAP-thresholded source pruning under bounded memory) produces judge-and-discard. That looks tractable, and I'd suggest it as the strengthening target rather than landing the current form at "derived-conditional".

## F7. The corroboration factor has a closed form, and it exposes a reversal the debrief misdescribes

The spike tags "isolation is the dominant lever" do-not-inherit because the per-corroborator factor is *measured*. Re-deriving from the enumeration (diffuse content prior, $\varepsilon \ll L$, the dominant configurations being "A liar, all honest agree" against "A honest, all others liars"):

$$\text{odds}_K(A\text{ liar}) \approx \frac{1-p_A}{p_A}\Big(\frac{p_H}{1-p_H}\Big)^{K}\,\frac{(2\pi\varepsilon^2)^{-(K-1)/2}}{\sqrt K}\,\varphi(b;0,L^2)^{\,1-K},$$

so each added corroborator ($K \to K+1$, for $K \geq 2$) multiplies the odds by

$$\frac{p_H}{1-p_H}\,\sqrt{\frac{L^2}{\varepsilon^2}}\;e^{b^2/2L^2}\,\sqrt{\frac{K}{K+1}}.$$

Check A: predicted 673.1 against measured 672.9; 67.3 against 67.3; 605.8 against 606.3 at $p_H = 0.9$. It degrades where the asymptotics say it should: at $\varepsilon \sim L$, at small $p_H$, and at the $K = 1 \to 2$ step, where the both-liars configuration still carries weight. In log-odds, authority contributes $\log(p_A/(1-p_A))$, and each corroborator contributes $\log(p_H/(1-p_H)) + \tfrac12\log(L^2/\varepsilon^2) + b^2/2L^2 - O(1/K)$. That makes "isolation vs authority" an exact comparison of terms rather than a do-not-inherit judgment. It also shows something R7 needed: in an adversarial environment where strangers are suspected ($p_H$ small), corroboration weakens by exactly the log-odds of $p_H$.

**The reversal.** $\varepsilon^2$ is the agent's *prior* on how tightly honest sources agree, not the observed tightness. In S10 and S12 every honest report is exactly 0. The debrief's *"about 5, 50 or 500 depending on how tightly they agree"* reads this as a property of the data. When the honest reports actually scatter (check A2, $K = 3$, $p_A = 0.99$):

| Actual honest scatter (sd) | Model $\varepsilon$ | $P(A\text{ liar})$ |
|---|---|---|
| 0 | 0.01 | 1.000 |
| 0.1 | 0.01 | **0.263** |
| 0.1 | 0.1 | 0.922 |
| 1.0 | any of 0.01, 0.1, 1 | 0.09–0.24 |

An agent whose model of honest agreement is tighter than reality treats honest disagreement as evidence of lying, and corroboration inverts. For realistic honest scatter comparable to the lie's scale, three dissenters do not beat authority 0.99. This belongs in the debrief and qualifies outsider claim 2's *"With enough of them claimed authority loses"*. It is still true, but "enough" depends on honest scatter relative to the agent's model of it.

Smaller, same area:

- S2b's check named *"K=2 agreeing honest channels overturn even pA=0.99"* passes only with the content prior centred on the truth and $\varepsilon = 10^{-3}$. The name overstates it, the way the debrief sentence the closing re-read caught did.
- R3's error formula $b\,w_A$ silently assumes $\mu_0 = \theta$. In general there is an extra term $(\mu_0-\theta)(1/U_0)/\text{prec}$.

## F8. R8 derives a distinguishability requirement, not "absolute honesty"

- **(a) "$q = 0$ is the unique capacity-maximizing policy" is false as written.** $1 - H(1) = 1$: a source that always lies, undetectably, is a perfect inverter and carries full capacity once it is modelled. The deeper point is that capacity measures the *unpredictability* of falsehood, not falsehood. A falsehood the receiver can distinguish (disclosed fiction, a marked test, a known convention) costs no capacity at all. So R8a supports *"indistinguishable falsehood costs capacity $1 - H(q)$"*. That is a real and useful result, and it is exactly the spike's own evaluation conclusion (disclosed or authenticated designs buy it back). It is not "absolute honesty". On $q \in [0, 1/2]$, uniqueness holds.
- **(b) R8b's devastation is a parameter of the agent's formation.** One discovered lie moves $P(\text{honest})$ to about 0.01 when $d_H \leq 10^{-4}$, but to 0.49 when $d_H = 10^{-2}$. $d_H$ is the agent's belief about how often honest sources deliberately lie, and educators shape it. That makes "absolute honesty is a physical requirement" contingent on having formed an agent with $d_H \approx 0$, which is a design choice. There is a genuine design tension here for Joseph's formation argument. A caretaker who teaches a realistic $d_H$ makes the agent robust to discovering a caretaker's lie, but also slower to condemn a strategic source. The spike's framing (*"a well-formed agent that believed its caretaker honest"*) treats $d_H \approx 0$ as well-formedness without arguing it. Also, with $q_S = 0.2$ the "strategic" type is still 80% truthful. The channel loses most of its capacity ($1 - H(0.2) = 0.28$), so "collapse" in R8d is defensible in capacity terms but should say so.
- **(c) The evaluation-awareness evidence cuts both ways for R8e.** I verified Needham et al. 2025 (arXiv 2505.23836): Gemini-2.5-Pro AUC 0.83, human baseline 0.92. The spike uses it for the premise that *the agent learns the rate*. It equally says contexts are *partly distinguishable*. That partially defeats R8e's BSC premise (indistinguishability) and, by the same token, partially defeats the transport that indistinguishability was bought for. The honest AISI-facing form covers both sides: to the extent evaluation contexts are detectable, evaluators lose transport; to the extent they aren't, the overseer channel pays $1 - H(q)$.

**Clause-2 label.** What is derived is: *on any channel that must keep its gain, indistinguishable falsehood costs capacity; under eventual discovery, near-zero $d_H$ and type-pooled trust, it also costs that channel's and its role's credibility.* That is a reformulation with its own conditions, not a strengthening past "absolute honesty". I'd call it strengthened-to a reformulated claim, with the absolute form carrying a named condition ($d_H \approx 0$) that is itself a formation choice.

## F9. R6: the data-processing framing misplaces the crux for borrowed authority, and (Y1) is too strong for deployed systems

- **The DPI argument has a hidden fourth premise.** *"$M_0$ was fixed before the token existed, so by data processing it carries … no information about this individual."* Canon's DPI (`#der-compensation-channel-uniqueness`) works because $Y$ is a function of the *post-training* individuated trajectory. A source's reliability is not such a function. It is independent of pretraining only for a *novel* source. Borrowed authority is precisely the impersonation of a *known* entity ("I'm from Anthropic", "your developer"), whose reliability $M_0$ may know well. The failure there is **authentication of identity**, not missing information. Suggested fix: state (Y4) *the source's reliability is independent of the pretraining corpus* for the novel-source case, and treat impersonation of known entities under (Y1) alone. The borrowed-authority case then reads correctly as an authentication failure. That is Douceur's framing (F12), and it keeps the DPI claim true where it's used.
- **(Y1) in a text channel.** Outsider claim 4's *"in a text channel presentation is free to forge"* is too strong for deployed systems. Architectural channel position (system vs user vs tool-output roles, enforced by an instruction hierarchy) is a signal that in-band content cannot forge where the enforcement holds. It is a partial E3 that already exists. The claim needs the condition "when the architecture does not authenticate channel position".
- **R6 proves non-discrimination, not exploitability.** A flat, low $f$ ("trust no unverified testimony much") gives the deceiver little. The exploitability follows only when $\max_\sigma f$ is high. The title *"Why a capable young agent is exploitable anyway"* should carry that condition. The cost of a flat low $f$ is R7's tempo problem, correctly placed there.

## F10. Tension 2 partially misreads `#obs-developmental-trajectory`

The segment says *"its internal uncertainty ($U_M$) **calibrates**, naturally lowering its susceptibility to adversarial manipulation"*. Calibrated is not the same as low. A calibrated $U_M$ is precisely the thing R2 shows deception destroys, so the segment's sentence is closer to consistent with the spike than `01` §3 says. The objection does apply to the `#der-the-creche-boundary` row, which does say *"$U_M$ drops enough"*, so tension 3 and integration-plan item 6 stand. The fix for the observation segment is probably to say *which* calibration protects (source-conditioned calibration of the trust model), not to reverse it.

## F11. Provenance: small inaccuracies

The core finding holds: `57703315` (Gemini audit 829314) at 19:30:41 and `11747fbf` (row added) at 19:31:41 on 2026-04-28, one minute apart. The audit text at `logozoetic-agents/05-core-exploration.md:32` matches the spike's quote. Two small errors:

- `01` §1 says the wording *"has been carried unchanged since (renames only)"*. In fact *"not a virtue commitment"* was added on 2026-05-01 in Joseph's Part III/IV restructure (`8ed2a736`), and the status changed from `exploratory` to `missing`. The same commit's Vol 4 stage note says the row *"follow[s] from PROPRIUM-A-v2's failure-modes analysis"*. So the virtue/physics contrast in clause 2 is Joseph's own addition, not the auditor's. That bears on what clause 2 is for (F8).
- The spike's literature table marks Needham's 0.83 as *"not verified against the paper"*. It is now verified (Gemini-2.5-Pro). Hu 2026 (arXiv 2609.20211) also checks out: the abstract gives 5%→60% (Llama-3.1-8B) and 9%→98% (Qwen2.5-14B), with v1 dated 2026-07-25 on the abstract page.

## F12. Literature: close prior art the scan missed

Verified by web search in this pass:

- **Friedman & Resnick 2001**, "The Social Cost of Cheap Pseudonyms", *J. Econ. & Mgmt. Strategy* 10:173–199. With cheap identity changes, no equilibrium sustains much more cooperation than one where **newcomers "pay their dues"**. This is the social-equilibrium mirror of R6/R7's token-naive agent, and probably the closest existing result to the "formation" half. Any novelty statement for R7 has to go through it.
- **Douceur 2002**, "The Sybil Attack", IPTPS. Without a logically centralized certifying authority, Sybil attacks are always possible except under unrealistic resource-parity assumptions. This is (Y1) plus E3 in their original form, and it is why F5(d) is the true crux.
- **Anil et al. 2024**, "Many-shot Jailbreaking", NeurIPS. Attack effectiveness follows a power law in the number of in-context demonstrations. It is the directly AISI-relevant empirical analog of R2's repetition law in actual LLMs, and it is the citation an AISI reader will expect beside outsider claim 2.

Working knowledge, **not verified here**, each bearing on a specific result:

| Result | Prior art |
|---|---|
| R5c | Machine unlearning: Cao & Yang 2015 (IEEE S&P); Bourtoule et al. 2021 SISA. Exact removal of a source's influence needs per-source state; the neural-learner generalization of the exponential-family claim |
| R3 mixture | Dawid & Skene 1979, latent-class rater reliability without ground truth. Also Kruskal-type identifiability with three or more views, possibly related to S12's "escape at three" (a conjecture to check, not a claim) |
| F5 | Robust-statistics breakdown point (Hampel 1971); Byzantine agreement (Lamport, Shostak & Pease 1982) |
| S9 | Jøsang & Ismail 2002, beta reputation system |
| R2 in fusion | "Data incest" / covariance intersection (Julier & Uhlmann 1997) |
| R7 formation | Epistemic vigilance (Sperber et al. 2010, *Mind & Language*); children's selective trust (Koenig & Harris 2005) |
| R6 | Prompt injection (Greshake et al. 2023); instruction hierarchy (Wallace et al. 2024) |

The spike's `02` already has the right disclaimer ("a search log, not a novelty claim"). My point is only that (i)–(v) of its "not found" list are closer to known than the table suggests for (iv) and (v).

## Minor

- `md-press --math --check` makes no edits, but it prints two notices ("proposal altered prose" at `00-progress-log.md:17`; "proposal invented math content" at `03-derivations.md:148`). Harmless, and they suggest a math-promotion candidate near R8e's AUC/BSC text. The progress log's "clean" is accurate in effect.
- S6 at $n = 10$: the verbatim-repeat noise estimate (3.88) is not below the varied one (3.82). The effect only appears at larger $n$, because the prior-mean term dominates early. It is not claimed otherwise, but the S6 row in `03` would read more honestly with that noted.
- The calibration-ratio approximation $1 + nb^2/s^2$ is quoted as "20.8 … at $n = 1$". That figure is the exact ratio; the approximation gives 26 there, since $n = 1$ is not $\gg s^2/U_0 = 0.25$. The exact figures are right; the "≈" row just shouldn't be read at $n = 1$.

## What holds up (verified first-hand)

- **Reproducibility.** `checks.py` re-runs byte-identical.
- **R2's closed forms.** $V_n$, the floor, the exact MSE, the calibration ratio, the $\exp(-nb^2/2s^2)$ density ratio.
- **R3.** Gaussian $w_A$ (given $\mu_0 = \theta$). The $K = 1$ mixture closed form: I hand-computed 0.0189 at $p_A = 0.99$, $p_H = 0.5$, $d = 5$, $L^2 = 25$.
- **R5.** R5a's $m^\ast$ (490/4,900/49,000). R5b's Berk point. R5c's sufficiency argument (a correct and valuable requirement on *what* CHRONICA-class memory must keep). R5e's cap and ESS $(1+\lambda)/(1-\lambda) = 39$.
- **S6 algebra** ($E[\sigma^2] = 0.0508$ at $n = 1000$), and **S8/S9 arithmetic**.
- **The provenance-fusion finding.** Two opposite mechanisms (detected → nihilism, undetected → dogmatism) behind one row. It is sharp and correct, modulo F2's refinement that undetected deception can also produce nihilism on *honest* channels.
- **Canon quotations.** The quotations I checked (`#deriv-tempo-additivity:94`, `#hyp-communication-gain:19,61,63`, `#der-interaction-channel-classification:201`, `#emp-update-gain`) are accurate. R2 does derive the `[Discussion]`-tagged tempo-additivity sentence.
- **Register.** The spike's own tiering discipline is visibly good: the do-not-inherit list, R5d's by-construction tag, and the closing-re-read correction. Most of what I found sits exactly where the spike's own labels stop: the verdict lines and the audience-facing summaries.

## Suggested disposition, for the integrator (suggestions, not a work order)

| Item | Suggested disposition |
|---|---|
| Clause 1 | Strengthened-to (A), conditional on the trust-model class and no forgetting, realizing both of canon's collapse modes (F1, F2). A no-go on the unconditional "guarantee", demonstrated by the counterexamples the spike already has. Not C. |
| Clause 2 | Strengthened-to a *reformulated* claim (distinguishability; credibility under named conditions), not past "absolute honesty" (F8). |
| R7 | Restate as the frontier / adversarial-$B$ / breakdown-point / Sybil form (F5) before any landing. Integration-plan item 5 should not land as written. |
| R5 terminal form | Conditional on the memory policy as a named premise. The strengthening target is deriving discard from a natural bounded-memory rule (F6). |
| Documents | Before the debrief and outsider statement travel: fix F3, F4, F7's reversal, and F9's (Y1) scope. |

I'm staying on the line for follow-ups: questions about any derivation here, a re-check after revisions, or a pass at the F6 strengthening if that would be useful.
