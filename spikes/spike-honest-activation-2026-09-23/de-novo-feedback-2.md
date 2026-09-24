# De-novo feedback 2: re-check of revision 1

*Same auditor as `de-novo-feedback-1.md`, 2026-09-23. Scope: commit `b4640a46`. I read `de-novo-feedback-1-response.md`, the whole of `03-derivations.md` revision 1, the revised debrief, outsider statement, integration plan and README, and the diffs to `00`–`02` and `sims/checks.py`. Re-running `sims/checks.py` (now with S13) gives output byte-identical to `sims/checks-output.txt`. My new probes are in `de-novo-feedback-2-checks.py`, with output in `de-novo-feedback-2-checks-output.txt`. The S13 simulation core there is copied unchanged and extended with two knobs: the deceiver's voice count, and dissent present from the start.*

## Summary

The revision is honest and substantive. F1, F2, F3, F4, F5, F7, F9, F10, F11 and F12 are addressed correctly and in the right register. Two changes do especially well:

- The clause-1 verdict now runs through canon's own definition of gain collapse.
- R7's restatement is accurate, and the spiker's added nuance on it is right: the interior policy in my check C was chosen knowing $qB$, which is exactly why case (b) is the real dilemma.

The response also records a failed strengthening hypothesis in S13, which is primary content and exactly what it should do. The two places the coordinator asked about need more work, and one smaller verdict issue remains:

1. **R5d's "sustained isolation" is half the right name, and S13 contains no borrowed-authority lever at all.** Under the consensus-trust rule, the deceiver's initial trust has no effect once the deceiver has been the sole source for a while: the beliefs are identical to two decimals at initial trust 0.99, 0.5 and 0.1. And the escape threshold is not "one dissenter". It is relative to the deceiver's own voice count: a deceiver with 2 Sybil voices holds against 2 concurrent dissenters, and one with 3 voices holds against 4. What S13 exhibits is capture held by **incumbency plus a concurrent-voice plurality**, and isolation is one way of keeping the plurality. (G1)
2. **R8's rebuttal is half right.** The "necessary and sufficient" biconditional fails in both of the senses the revision appeals to. Honest error breaks sufficiency. A known inverter breaks necessity in the ordinary sense of lying. What is exact is narrower: deception strictly lowers capacity *below the source's honest-error capacity*, and non-deception is the unique maximizer on $q \in [0,1/2]$. That is still a clean result, and it still carries clause 2's intent. (G2)
3. **The clause-1 verdict merges the conditions of its two routes and drops "static world".** (G3)

## G1. R5d and S13: what the simulation actually exhibits

**Probe 1: authority is inert after isolation.** With 300 steps of the deceiver alone, followed by one dissenter, the final beliefs are 4.72, 5.04, 4.99, 5.25 and 4.47 across 5 seeds. They are identical to two decimals whether the deceiver's initial trust is 0.99, 0.5 or 0.1. The reliability update $r_j \leftarrow r_j + \alpha(\text{agree}_j - r_j)$ forgets the initial value on a $1/\alpha \approx 20$-step timescale. During the isolation period the deceiver agrees perfectly with a consensus it alone sets, so its trust goes to about 1 whatever it started at.

**Probe 2: authority matters only when there is no incumbency.** With the dissenter present from $t = 0$, initial trust 0.99 captures (5/5 seeds), and initial trust 0.5 does not (0/5). One caution on the 0.5 case: `run_consensus` starts the consensus at $\mu = 0$, which is the truth. That hands the honest source a small incumbency, so the symmetric case is not a clean no-authority baseline.

**Probe 4: the threshold is voice-relative.** With $n_A$ deceiver voices (Sybil identities, all asserting $b$, present from the start) against $K$ concurrent dissenters:

| Deceiver voices $n_A$ | Captured at $K$ | Escapes at $K$ |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 2, 3, 4 | 5 |

So under this rule, escape needs concurrent dissent to *outnumber* the deceiver's concurrent voices, with a margin that grows with $n_A$ (incumbency). "Isolation" (few independent channels) is one of the adversary's two ways to keep that plurality. Sybil voice count is the other, and it is exactly the lever R7(d) already names. Kernel width and rate don't change the qualitative picture at $n_A = 1$, $K = 2$ (probe 6). At $\alpha = 0.2$ one seed in five stays captured. Wide kernels ($c = 3$, $6$) leave a residual bias of 0.3–1.9 even in escape, which is partial capture.

**Consequences:**

- The name is doing more work than the evidence. A more accurate statement of what S13 exhibits: *under consensus-estimated trust, capture is absorbing while the deceiver keeps incumbency and a plurality of concurrent voices*. Isolation reduces the honest count; Sybil identities raise the deceiver's. "Sustained isolation" names only the first, and outsider claim 3 ("Capture is held by sustained isolation … Two concurrent independent dissenters break it") would mislead an AISI reader about the second. Against a deceiver running three identities, two dissenters do nothing.
- **Borrowed authority has no role in R5d.** That is fine as a finding, and it arguably supports Joseph's "cutting off channels is decisive". But the verdict's condition list ("a trust model that treats the deceiver as unbiased or as a trusted honest type … sustained isolation") reads as if authority carries R5d. In S13, authority is the first-contact lever (probe 2), and incumbency plus plurality carry the rest. This is a property of this trust rule, which has no persistent reliability prior. A Dawid–Skene-style EM with a proper reliability prior would retain some authority weight. That leads to the next point.
- **"Fixed-point structure of Dawid–Skene / truth-discovery … the principled choice when no ground truth is available"** overstates what `run_consensus` is. It is an exponentially smoothed agreement-with-consensus heuristic: no latent-class likelihood, no prior on reliability, no EM. It resembles truth-discovery iterations, and I'd call it that, "a truth-discovery-style heuristic". Whether authority survives in the principled version is exactly what would tell you if probe 1 is a real phenomenon or an artifact of a prior-less rule. That makes it the right next check.
- **"Absorbing exactly while …"** — "exactly" is not available from one parameterization. The terminal-form statement should read "in the exhibited parameterization, absorbing while …". The tier line below it already says so; the headline sentence should match.
- **The (D4) terminal-form parallel still holds, and is better than before.** The silencing is now produced by the agent's own trust dynamics, not assumed. I'd suggest the integration plan's item 2(a) land it at the tier the evidence supports (numerical, one rule), with the plurality condition rather than "isolation" as the named condition.

**A closed-form handle, if the spiker wants the strengthening target.** At a captured fixed point with consensus $\mu \approx b$, a lone dissenter reporting $\mathcal N(0,1)$ has expected agreement $\frac{c}{\sqrt{c^2+1}}\exp\!\big(-\mu^2/2(c^2+1)\big)$, so its reliability settles near that value. That is about 0.03 at $\mu = 4.7$, $c = 1.5$, consistent with S13's 0.02. The deceiver's settles near 1. Escape looks like a stability question for the fixed point as a function of voice ratio, $b/c$ and $\kappa$: when does the reliability-weighted pull of $K$ dissenters, each starting near that low weight, move $\mu$ far enough that the deceiver's agreement falls? I haven't solved it. It looks like the tractable fixed-point analysis the integration plan already names, with $n_A$ added as a variable.

## G2. R8's partial rebuttal: right target, wrong biconditional

The response argues that, read as non-deception, honesty is exactly what R8a characterizes: *"full capacity holds iff the receiver can predict each claim's truth-value, which is iff the source never deceives."* The first "iff" is correct. The second fails in both directions:

- **Sufficiency fails with honest error.** A sincere but fallible source (honest error rate $e$) never deceives, yet its capacity is $1 - H(e) \lt 1$: 0.859 at $e = 0.02$, 0.714 at $e = 0.05$ (probe 8). The receiver cannot predict honest errors any more than lies. R8a's BSC argument never distinguishes a lie from a mistake. "Not deceiving is necessary and sufficient for a channel's full capacity" (R8d, the debrief, the integration plan item 1) is therefore false as written.
- **Necessity fails in the ordinary sense.** A known always-inverter asserts what it believes false, with intent, so it lies in the ordinary sense, and it has full capacity. The revision escapes this by defining deception as *indistinguishable* falsehood. But that is a receiver-relative, technical definition, and the response presents it as the ordinary meaning. You can have the technical definition (then "necessary" holds) or the ordinary one (then the result is about something slightly different). The argument currently uses both.

**What is exact, and I think carries clause 2's intent cleanly:**

- A source with honest error rate $e \lt 1/2$ that also deceives at rate $q$ presents a flip rate $e + q - 2eq$. Its capacity $1 - H(e + q - 2eq)$ is strictly decreasing in $q$ on $[0, 1/2]$. So **deception strictly lowers a channel's capacity below what the source's honesty alone would give, and $q = 0$ is the unique maximizer given $e$.** For example, at $e = 0.02$, a 5% deception rate drops capacity from 0.859 to 0.642.
- "Deception" here means falsehood the receiver's model cannot predict. That is the technical sense, and it should be stated as such. The ordinary-sense question ("is a known liar dishonest?") is then a separate, philosophical one. Joseph can decide how the normative segment words it.

**"Not a virtue commitment".** Clause 2's contrast was Joseph's addition (F11). The math shows honesty is *also* a structural requirement: capacity, and credibility under discovery. It cannot show honesty is *not* a virtue commitment; "not X" is a claim no capacity bound reaches. An honest rendering is "a structural requirement independent of whether it is also a virtue". The integration plan's "keep 'not a virtue commitment' only in the precise sense R8d supports" is the right instinct. I'd say that precise sense is "independent of", not "instead of", and flag the choice to Joseph.

**Completion-state label.** "Strengthened-to a reformulated claim (state A)", with "absolute … is not supported", is fine by me in substance. By the ghost discipline, though, the unsupported "absolute" reading is a small no-go worth stating as one in the landed segment: disclosed falsehood provably costs no capacity. It should not be left implicit in a relabel. The integration plan's item 1 ("There is no FALSE-marking step, because no no-go applies to the row as a whole") is consistent with that, as long as the word "absolute" does not survive into the landed row.

## G3. The clause-1 verdict's condition list

The verdict lists one combined set of conditions: trusted deceiver, no forgetting, sustained isolation, persistent deceiver. The two routes have different conditions:

- **Dogmatism route (R2, trusting model).** It needs neither isolation nor persistence to diverge while messages keep arriving. Even with honest channels present, R5b's trusting agent converges to a permanent bias while $U_n \to 0$, so the calibration ratio diverges. It does need a **static world**: with process noise $Q \gt 0$, $U_M$ has a floor and the ratio is bounded. R2 states the static world, but the verdict and the list of counterexamples to "guarantee" both omit it. It was one of the counterexamples in F1 (S0's own setting).
- **Nihilism route (liar-component models, S13).** This one does need the plurality/isolation condition (G1) and a persistent deceiver.

Suggested fix: state the conditions per route, and add $Q \gt 0$ (a changing world) to the counterexamples to "guarantee".

## Smaller items

- **Outsider claim 3** says "stays captured through any number of dissenters who each speak briefly". That was tested at twelve, in one parameterization, and it is an unqualified universal in the AISI-facing document. The tier in `03` ("numerical, one parameterization") should travel with the claim. So should the voice-relative threshold (G1).
- **Outsider claim 5 and the debrief's "about 71% of an honest source's information at 5%"** assume an infallible honest source. With honest error the relative cost differs: at $e = 0.02$, $0.642/0.859 = 75\%$. That is minor, but the "honest source" baseline should say "error-free".
- **R5c now names machine unlearning as a "close neighbor" in `03`'s body.** In `02` it is correctly marked as the verifier's working knowledge, not verified. Keep that tier visible wherever it is cited, or verify it: Cao & Yang 2015 and Bourtoule et al. 2021 are easy to confirm.
- **Lint.** `md-press --math --check` makes no changes to the spike files. The two notices it prints on my own `de-novo-feedback-1.md` are prose-proposal notices, not edits.

## Verified in this pass

| Item | Check |
|---|---|
| F1 | The verdict change is correct. R1 is now scoped as mechanism-locating, and the `01` tension-1 correction is candid about the adopted guess. |
| F2 | The mode assignment is corrected, and the D4 severing-source amendment is in integration-plan item 2(b), tied to 2(a) as "must land together". |
| F3 | The oracle-gain framing is correct. The numbers match my check B. |
| F4 | The R1b merge into R4 is correct, with the full-control scope. The duplication-component point is placed correctly. Outsider claim 1 is now accurate. |
| F5 | R7 (a)–(d) is accurate, and the readers-ask answer is correct. The attack-surface point is carried with the right tier in the do-not-inherit list. |
| F7 | The closed form and the reversal are carried correctly. The $\mu_0 \neq \theta$ term is right: $(\mu_0-\theta)(1/U_0)/\Pi$. The S2b check is renamed honestly. |
| F9 | (Y1)–(Y4) and the two-case split are correct. |
| F10, F11, F12 | Correct. The literature table now separates verified from working-knowledge entries. |
| S13 failure record | It is honestly recorded, and the refuted first hypothesis is kept in the script. |

I'm staying on the line. If useful, I can run the Dawid–Skene-with-prior version of S13 (G1) or attempt the fixed-point escape condition.
