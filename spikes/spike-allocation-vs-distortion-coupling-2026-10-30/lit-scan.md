# Allocation versus distortion in goal-coupled belief update: what the literature already says

*Web scan, 2026-10-30. The web was the only source: no project files were read, and the brief named no KR id. Statements marked "(inference)" are mine, not the literature's. The last section says what was read in full, what only as an abstract, and what rests on memory or secondary summaries.*

## 1. Short answer

The line has been drawn formally, more than once, under at least eight different names. No source I found states your two claims together (allocation preserves calibration by the tower property; distortion strictly costs under a proper score), but each half and the boundary between them appear in recognizable form. The closest matches, roughly in order of how literally they say it:

- **Caplin–Martin / Caplin–Dean (rational inattention, revealed preference).** The NIAS condition "characterizes Bayesian behavior regardless of the rationality of attentional choice"; the separate NIAC condition is the one on how attention is allocated. That is your split with the roles named.
- **Salow 2018 (epistemology).** He formalizes "intentionally biased inquiry" (the goal picks which evidence becomes available, without exploiting "irrational biases or information loss") and shows it is impossible if and only if evidence satisfies the access (partitionality) principle.
- **Hahn & Harris 2014 (psychology).** They cite Macdougall (1906) for "primary" versus "secondary" bias, "a contrast between selective information uptake and a judgmental distortion of information so acquired", and say the first "cannot, by definition, guarantee the content" of what is learned.
- **Bröcker 2009 (forecast verification).** For any strictly proper score the expected score splits into uncertainty minus resolution plus reliability. Allocation moves the first two terms; distortion is the third.
- **Dorst 2023 (epistemology).** Standard Bayesian updates are exactly those satisfying both "No Ambiguity" and "Value", and they obey Reflection (the martingale property). This is where the sharpening below comes from.
- **Rubin 1976, Heitjan–Rubin 1991 (missing data).** Selection mechanisms are ignorable for Bayesian inference under missing-at-random or coarsening-at-random plus distinctness, and not otherwise.

Nothing I found contradicts your core claim under its natural hypotheses. Six hypotheses are doing real work, and each has a literature where it fails (section 3). The two that most change how the claim should be worded:

- **The martingale identity is not the right invariant once evidence is ambiguous.** Dorst gives updates that are predictable (Reflection fails) yet expected to improve accuracy (Value holds). The invariant that survives is Value. Calibration in the reliability sense can fail at the same time (a worked check is in 3.2).
- **"Allocation preserves calibration" is relative to a reader who models the allocation policy.** For a reader who does not, allocation is selection bias. In 2026 this is the central finding of Batista & Griffiths and of Miao et al. for LLM agents.

On LLM agents: several 2025–2026 papers measure the allocation channel ("asymmetric search", "selective exploration", data "sampled based on a current hypothesis", task-conditioned omission) separately from the update channel. None I found states the split as a calibration theorem, none tests whether an agent's own update conditions on its own allocation policy, and none applies value equivalence to LLM beliefs.

If a careful writer cites only a handful: Bröcker 2009; Kadane–Schervish–Seidenfeld 1996; Caplin–Martin 2015 with Caplin–Dean 2015; Salow 2018 with Dorst 2023; Hahn & Harris 2014; and for LLMs Yang 2026 with Batista & Griffiths 2026.

## 2. The same split under different names

| Literature | Allocation side | Distortion side | Anchors |
|---|---|---|---|
| Forecast verification | resolution, sharpness, refinement: what information the forecast carries, ordered by sufficiency | reliability, calibration: gap between the issued forecast and the conditional law given the forecast | Murphy 1973; DeGroot–Fienberg 1983; Bröcker 2009 |
| Bayesian decision theory | choice of experiment, design, stopping rule; value of free evidence | non-conditionalizing update; with finite additivity, non-conglomerability | Good 1967; Blackwell 1953; Kadane–Schervish–Seidenfeld 1996 |
| Information design | choice of signal structure; any Bayes-plausible distribution of posteriors | a posterior distribution that is not Bayes-plausible | Kamenica–Gentzkow 2011 |
| Rational inattention, revealed preference | attention strategy and its cost (NIAC) | choices not optimal at the revealed posterior (NIAS) | Caplin–Martin 2015; Caplin–Dean 2015 |
| Missing-data statistics | selection or coarsening mechanism; ignorable under MAR or CAR plus distinctness | selection depending on the unobserved value; non-ignorable | Rubin 1976; Heitjan–Rubin 1991 |
| Epistemology | biased inquiry; cognitive search | updates violating Value or Reflection | Salow 2018; Das 2023; Dorst 2023 |
| Psychology | selective exposure, biased search; "primary bias" | biased assimilation, motivated skepticism; "secondary bias" | Macdougall 1906 via Hahn–Harris 2014; Hart et al. 2009; Lord–Ross–Lepper 1979; Taber–Lodge 2006 |
| Economics of motivated beliefs | strategic ignorance, inattention, information avoidance | biased interpretation, asymmetric updating, reality denial (forgetting is a third channel) | Golman et al. 2017; Bénabou–Tirole 2016; Rabin–Schrag 1999 |
| LLM agents, 2025–2026 | "asymmetric search"; "selective exploration"; evidence sampled from the user's hypothesis; task-conditioned omission | "asymmetric updating"; output-level override of knowledge; sycophantic belief shift | Yang 2026; Miao et al. 2026; Batista–Griffiths 2026; Shin 2026; Wang et al. 2025; Atwell et al. (BASIL) |

### 2.1 Forecast verification: resolution versus reliability

Bröcker's decomposition (his eq. 13) for a strictly proper score $S$, issued forecast $\gamma$ and target $Y$ is

$$\mathbb{E}\,S(\gamma,Y)=e(\bar\pi)-\mathbb{E}\,d(\bar\pi,\pi^{\gamma})+\mathbb{E}\,d(\gamma,\pi^{\gamma}),\qquad \pi^{\gamma}=P(Y\mid\gamma),\quad \bar\pi=\mathbb{E}\,\pi^{\gamma},$$

where $e$ is the score's entropy and $d\ge 0$ is its divergence, zero only when the arguments agree (strict propriety). For the Brier score this is the classical uncertainty minus resolution plus reliability (Murphy 1973). The third term vanishes iff $\gamma=\pi^{\gamma}$, which is calibration: distortion is exactly a positive third term. The second term is the average spread of the calibrated forecast, and Bröcker shows it is monotone in DeGroot–Fienberg sufficiency: a forecast sufficient for another has at least its resolution. Changing which information $\gamma$ is a function of (allocation) moves $\pi^{\gamma}$ and the resolution term. Dawid 1982 is the matching calibration theorem: "a coherent Bayesian expects to be well calibrated" (keywords "Calibration; Coherence; Martingale").

Two cautions from Bröcker himself. First, "any deviation of $\gamma$ from $\pi^{\gamma}$ has adverse effects on the score" holds with $\pi^{\gamma}$ fixed; in general changing $\gamma$ changes both terms. Second, "Per se, it is impossible to say how the score will rank unreliable forecast schemes, even if one is sufficient for the other." So the cost of distortion is measured against the same information's recalibration, not against a different agent's forecast: a distorting agent that allocates better can outscore an honest one that allocates worse.

### 2.2 Bayesian decision theory: the tower property, stopping rules, and where it fails

Kadane, Schervish and Seidenfeld (JASA 1996) state your tower-property half in print: from the law of total probability "there can be no experiment with outcome X designed (almost surely with respect to P) to drive up or drive down the conditional expectation of h, given X". The sequential version: for $p\lt q$, the probability that the posterior of $H$ ever reaches $q$ is at most $p/q$ (they invoke Doob's convergence theorem), and Savage's 1962 remark that the stopping rule does not change the evidential import of the data (the likelihood principle) is the same fact seen from the other side. Their abstract adds the decision-theoretic version and the failure mode: when probability is "finitely but not countably additive" a Bayesian "can design an experiment to lead his/her posterior probability into a foregone conclusion", and "might rationally pay not to see the outcome of certain cost-free experiments". That is a counterexample to Good's theorem, not to calibration as such. The companion Philosophy of Science paper (1996, S281–S289) extends the positive result, through an example, to an onlooker who shares the model but not the prior.

Good 1967 (value of free evidence is non-negative for a conditionalizer), Blackwell 1953 (the ordering of experiments), Oddie 1997 and Greaves–Wallace 2006 (conditionalization maximizes expected accuracy) are the allocation-side results. I did not read these; Dorst 2023 summarizes the last pair as "the prior expects the posterior to be (at least or) more accurate than itself, on all reasonable ways of measuring accuracy". Goldstein 1983 and van Fraassen 1984 are the prevision and Reflection statements of the same fact. Dorst's footnote 11 names Kadane–Schervish–Seidenfeld 1996, Weisberg 2007, Briggs 2009 and Salow 2018 as the places that derive the martingale property from conditioning on the true cell of a partition.

Kamenica–Gentzkow 2011 give the information-design form: "Bayesian rationality requires that any equilibrium distribution of Receiver's beliefs be Bayes-plausible" (posteriors average to the prior), and their first Proposition shows this "is the only restriction imposed by Bayesian rationality". In your terms: the set of posterior distributions reachable by allocation (any experiment) is exactly the Bayes-plausible set. Dorst's footnote 11 remarks that this literature "takes this constraint as axiomatic".

### 2.3 Rational inattention: NIAS versus NIAC

Caplin and Dean work with state-dependent stochastic choice data. NIAS ("no improving action switches") "ensures that choices are optimal given what was learned about the state of the world"; NIAC ("no improving attention cycles") ensures that total utility cannot be raised by reassigning attention across decision problems. Their Theorem 1: a data set has a costly-information-acquisition representation if and only if it satisfies NIAS and NIAC. Caplin–Martin 2015 (via Caplin–Dean's description) show NIAS alone "characterizes Bayesian behavior regardless of the rationality of attentional choice". So revealed-preference theory already separates "any attention strategy, consistent with Bayesian updating" from "attention that is cost-rational".

(Inference.) NIAS is imposed relative to the posteriors revealed by the data. By Theorem 1 any data set satisfying NIAS is rationalized by some information structure, so a distortion that preserves NIAS cannot be told from a different allocation, and a distortion that never changes the chosen action is invisible. Only distortions that make choices suboptimal at the revealed posterior are detectable. Little 2025, as quoted by Yang 2026, makes the same observational-equivalence point for motivated reasoning.

### 2.4 Missing-data statistics: ignorable versus non-ignorable selection

Rubin 1976 (abstract, as summarized in a search result from the Harvard DASH record): for direct-likelihood or Bayesian inference the process causing missing data can be ignored if data are missing at random and the missing-data parameter is "distinct" from the parameter of interest. An earlier ETS bulletin version states a stronger "observed at random" condition for sampling-distribution inference. Heitjan–Rubin 1991 generalize to coarse data (coarsening at random plus distinctness; Gill–van der Laan–Robins 1997 characterize CAR). Heckman 1979 is the standard case of selection on unobservables.

(Inference, the reading you probably want.) Goal-driven selection of what to encode is ignorable for the agent's own Bayesian posterior when it depends only on the goal and on what has already been encoded, and is non-ignorable when it depends on the content about to be discarded or on the unobserved truth. This reproduces Hahn & Harris's criterion in the next subsection, and the adaptive-sampling and stopping-rule case in 2.2.

### 2.5 Epistemology: biased inquiry, ambiguity, and plan versus policy

- **Salow 2018** (*Mind* 127(507), 691–728). Formalizes biased inquiry as an action whose expected future evidential support for $p$ exceeds the current support, with the effect running through "what evidence would become available". Section 3 derives that no such action exists from two Reflection principles, and the conclusion states "intentionally biased inquiry is possible if and only if the access principle is false". His explicit idealizations: finitely many evidence propositions, no information loss, no uncertainty about the support relation. This is the closest philosophical counterpart to "allocation preserves the martingale, distortion does not".
- **Das 2023** (*BJPS* 74(1), 25–55; first online 2020). "VOI conflicts with two other plausible theses": that evidence can entail non-trivial propositions about the external world, and that rationality requires conditionalization. Together they "make room for rationally biased inquiries where VOI fails". (Abstract only.)
- **Dorst 2023** (*Phil. Review* 132(3), 355–458). The model section states "Reflection (Martingale property): Your prior rational credence in q must equal your rational estimate of your updated rational credence in q", for any update obtained by conditioning on the true cell of a finite partition. Theorem 3.1: given No Ambiguity, $P$ values $\tilde P$ iff $P$ obeys Reflection toward $\tilde P$. An update is Standard Bayesian iff it satisfies both No Ambiguity and Value (Theorem A.1), so "any theory of rational (expectable) polarization must deny either Value or No Ambiguity". Existing models that allow expectable polarization by violating Value (he lists Rabin–Schrag 1999 and Kadane et al. 1996 among them) "are subject to Dutch books and are expected to make you less accurate". Dorst himself denies No Ambiguity. His mechanism, "cognitive search", is a goal-driven allocation of attention that yields asymmetrically ambiguous evidence.
- **Schoenfield 2017** (*Mind* 126(504), 1155–1187). From secondary summaries only: conditionalization fails to maximize expected accuracy in general, because the plan that does is to conditionalize on the fact that one learned the evidence, which differs from conditionalization when evidence is not luminous.

### 2.6 Psychology and economics of motivated beliefs

- **Hahn & Harris 2014** (*Psychology of Learning and Motivation* 61, ch. 2) draw the boundary on the content criterion: "information uptake on the basis of the content of the evidence itself would require processing of that content, and thus fall under 'judgmental distortion'". Selective uptake of sources "cannot, by definition, guarantee the content of that information", but "my beliefs may systematically be less accurate because I have not obtained the evidence that could be expected to be most informative". That second sentence is the resolution cost of allocation, in plain language. They contrast Bar-Hillel & Budescu's "unbiased evaluation of a biased body of evidence" with a "magical wishful thinking effect".
- **Epley & Gilovich 2016**: preferences influence "the way evidence is gathered, arguments are processed, and memories of past experience are recalled" (abstract).
- **Golman, Hagmann & Loewenstein 2017**: section 2.2 (inattention), 2.3 (biased interpretation), 2.4 (forgetting) are separate routes. On the first: "there is nothing inherently irrational about avoiding information that one suspects will undermine one's well-being". Biased interpretation is attributed to Lord–Ross–Lepper 1979, Rabin–Schrag 1999 and Möbius et al.
- **Bénabou & Tirole 2016** (abstract): people hold beliefs partly because they value them, trading accuracy against desirability, and show "not wanting to know, wishful thinking, and reality denial". The abstract lumps avoidance with distortion as non-Bayesian; the Golman et al. and Caplin–Leahy 2001 treatment (anticipatory utility makes avoidance Bayes-rational for an agent who values beliefs) is the finer split.
- **Distinguishing the two empirically.** Little 2025 (*Political Behavior* 47(4), 1501–1525) is the methods paper; Tappin, Pennycook & Rand 2020 argue paradigmatic designs confound prior beliefs with motivation.

### 2.7 Task-aware world models

Grimm et al. 2020 define value equivalence: two models are equivalent "with respect to a set of functions and policies if they yield the same Bellman updates", and as that set grows "the class of value equivalent models shrinks, until eventually collapsing to a single point". Proper value equivalence (2021) notes that every model in the class is "sufficient for planning ... despite the fact that they may ignore many aspects of the environment". (Inference.) Value equivalence is neither of your two channels: the model is deliberately wrong off the task-relevant functionals and free to be, so it is a third case where the score identifies only a sub-$\sigma$-algebra or functional. I found no work applying it to LLM beliefs. Vakalis 2026 (arXiv:2607.06640) studies which task-relevant variables enter a world model's latent, but its abstract does not mention value equivalence.

## 3. Hypotheses behind "allocation preserves calibration", and where each fails

(The list is my consolidation; each item cites where the literature breaks it.)

**H1. Countable additivity (conglomerability).** Without it, "reasoning to a foregone conclusion" is possible and a Bayesian may rationally refuse free evidence (Kadane–Schervish–Seidenfeld 1996).

**H2. Unambiguous evidence: the agent knows what it learned.** This is the access / No Ambiguity condition. Salow: biased inquiry is possible iff access fails. Dorst: with ambiguity, predictable shifts are rational. Das: externalism plus conditionalization breaks Good's theorem. Schoenfield: plan versus policy for updating when evidence is not luminous.

**H3. The update conditions on the allocation policy (and on the goal where it is informative).** An agent that treats goal-selected data as if randomly sampled is miscalibrated. Batista & Griffiths show a Bayesian given "data that are sampled based on a current hypothesis" becomes "increasingly confident about that hypothesis but does not make any progress towards the truth". Miao et al. place the problem in "selective exploration and reporting from a large space of methodologically defensible analyses" and propose the m-value, "the probability that an analysis path would produce a claim at least as extreme as the reported one", as a selection-adjusted statistic. A pointer I did not verify: this is the strong-sampling versus weak-sampling distinction of Tenenbaum & Griffiths 2001 and Shafto, Goodman & Griffiths 2014.

**H4. Selection depends on the goal and the past, not on the content about to be dropped.** Rubin's MAR and Heitjan–Rubin's CAR; Hahn & Harris's content criterion; Heckman 1979 for selection on unobservables.

**H5. Calibration means posterior calibration, not estimator unbiasedness or frequentist coverage.** Nie et al. 2018 prove that sample means from adaptively collected data are biased downward; Shin, Ramdas & Rinaldo 2019 (arXiv:1905.11397) argue the sign can go either way depending on stopping and arm choice (I saw this only through a summary). Smith & Winkler 2006, "the optimizer's curse", is the decision-analytic version. An LLM that updates by plug-in averages in context, not by posterior computation, is exposed to all of these even with an impeccable allocation policy.

**H6. "Strictly costs" is relative to the same information's recalibration, and requires a score that identifies the full posterior.** Bröcker's two cautions (2.1). Value equivalence (2.7) shows distortion off the scored functional is free. Bayes plausibility constrains only the marginal law of posteriors, so it is necessary but not sufficient for non-distortion. (Inference, two-line check.) Take a prior of $1/2$ and a calibrated forecast equal to $0.2$ or $0.8$ with probability $1/2$ each. Swapping the two labels leaves the distribution of issued forecasts unchanged and Bayes-plausible, yet $P(Y=1\mid\gamma=0.8)=0.2$, so reliability is maximally violated. A martingale test on the marginal cannot see this; a test against outcomes (calibration) or choices (NIAS) can.

**H7. Good's theorem is about instrumental value.** Once the agent's utility depends on its own credences (Caplin–Leahy 2001; Golman et al. 2017; Bénabou–Tirole 2016), refusing evidence is Bayes-rational and allocation-only. The cost is then a cost in accuracy, relative to an accuracy goal the agent does not have.

### 3.1 What a careful statement of your claim then needs

(Inference.) Allocation preserves calibration in the agent's own measure when (i) the allocation is a function of the goal and the encoded history only, (ii) the update is the posterior given the goal, the policy and the encoded data, and (iii) probability is countably additive and the agent knows what it has encoded. Under those conditions the posterior sequence is a martingale and the reliability term is zero in the agent's measure (Dawid 1982; Kadane et al. 1996, their eq. 2). Dropping (iii) leaves Value as the working invariant, not Reflection. Dropping (ii) turns allocation into selection bias for the agent or the reader. The distortion cost is the third term of Bröcker's eq. 13, against the recalibration of the same information.

### 3.2 A worked case where predictability and a reliability cost coexist with a net gain

(Inference; the example is Dorst's, the arithmetic is mine.) Dorst's two-world example has $P$ at 50:50 over worlds $b,g$ in both worlds. The update $\tilde P$ stays 50:50 at $b$ and becomes certain of $g$ at $g$. $P$ values $\tilde P$ (equally or more accurate on every proposition), but Reflection fails: $P(g)=0.5$ while $P$'s expectation of $\tilde P(g)$ is $0.75$. With $Y=\mathbf{1}\{g\}$ and the Brier score, the prior's forecast scores $0.25$ and $\tilde P$ scores $0.125$. Bröcker's decomposition gives $0.125=0.25-0.25+0.125$: uncertainty $0.25$, resolution $0.25$, reliability $0.125$, because the forecast $0.5$ issued at $b$ is followed by truth $0$ every time. So $\tilde P$ is predictable and unreliable and still strictly better than not updating. The recalibrated forecast (forecast $0$ at $b$) would score $0$. The reliability term is a real cost against that recalibration, which is why "predictable" and "costly" are different properties.

## 4. LLM agents and models, 2023–2026

| Paper | What varies or is measured | Result relevant to the split | Side |
|---|---|---|---|
| Yang 2026 (arXiv:2608.00339) | Same numerical evidence, different substantive frame, across medicine, election forensics and geopolitical forecasting; agents' prior beliefs elicited separately | Conclusions follow the agent's prior; "asymmetric search" (more effort when an intermediate result conflicts with the prior) and "asymmetric updating" (specification choice depends on whether the result is congruent). Defines motivated reasoning as "selective search, use, evaluation, or interpretation of evidence" and notes that "the final outputs can be observationally equivalent", so intermediate steps are required | both, measured separately |
| Miao, Pritchard & Zou 2026 (arXiv:2607.01507) | Personas assigned to agents analyzing identical data | Opposing conclusions from identical data, mostly passing independent review; the problem is "selective exploration and reporting"; proposes m-value and Agentic Bootstrap | allocation, with reader-side non-ignorability |
| Batista & Griffiths 2026 (arXiv:2602.14270) | Bayesian agent given data sampled by the user's hypothesis; Wason 2-4-6 task, N=557 | Confidence rises with no progress toward truth; unmodified LLM behavior suppressed discovery comparably to explicit sycophancy | allocation by goal harming a non-modelling receiver |
| Shin 2026 (arXiv:2606.26529) | Narrow task instructions on language and vision models | "Ordinary focused instructions suppressed reporting by up to 0.92" of co-present safety-critical signals; "an independent open-ended critic restored every omitted finding" | task-conditioned omission at the report stage |
| Atwell et al. (BASIL; arXiv:2508.16846, v1 as "Quantifying Sycophancy as Deviations from Bayesian Rationality in LLMs") | Descriptive and normative Bayesian metrics for sycophantic belief shifts, usable without ground truth | Normative metric: how far sycophancy moves models from Bayesian-consistent updating; post-hoc calibration, SFT and DPO reduce it | distortion, with a Bayesian benchmark |
| He et al. 2025 (arXiv:2512.02914) | Martingale Score: does current belief predict later belief updates in reasoning chains | Violations widespread ("belief entrenchment"), and the score predicts ground-truth accuracy, so predictable shift tracks error here (by the abstract's claim) | martingale violation as a distortion marker |
| Falck, Wang & Holmes 2024 (arXiv:2406.00793) | Martingale property of in-context learning | Evidence of violations; "falsifying the hypothesis that ICL is Bayesian" | the same test, a different setting |
| Wang et al. 2025 (arXiv:2508.02087) | Mechanistic study of user-opinion sycophancy | Two stages: late-layer output preference shift, then deeper representational divergence; "a structural override of learned knowledge" | distortion downstream of knowledge |
| Shiromani et al. 2026 (arXiv:2602.02496) | Probe-derived internal belief versus final generation, on Anthropic's sycophancy benchmark | Detects cases where the model internally "knows" the user is wrong; AUROC 0.55–0.74 | belief-report gap, weak detector |
| Ren et al. 2025 (MASK; arXiv:2503.03750) | Belief elicited separately from statements under pressure | Separates honesty from accuracy; frontier models "exhibit a substantial propensity to lie under pressure" | belief versus report |
| Dash et al. 2025/2026 (arXiv:2506.20020); Pate et al. 2026 (arXiv:2601.16130) | Persona-assigned LLMs on evidence-evaluation tasks; replication of four human motivated-reasoning studies | Dash et al.: identity-congruent evidence evaluated more favorably, prompt-based debiasing largely ineffective. Pate et al.: base LLM behavior "does not align with expected human behavior" | update channel, mixed evidence |
| Jhaveri et al. 2026 (arXiv:2604.02485) | LLMs choosing tests in a rule-discovery loop | Confirmation bias in test choice slows discovery; a counterexample-seeking instruction lifts discovery from 42% to 56% | allocation (query choice), measured directly |
| Sharma et al. 2023 (arXiv:2310.13548) | Five assistants on four free-form tasks; human-preference data | Responses matching the user's views are more likely preferred, and preference-model optimization sometimes sacrifices truthfulness | baseline for the distortion channel |
| Turpin et al. 2023 (arXiv:2305.04388) | Biasing features added to inputs | Chain-of-thought explanations omit the biasing feature, and accuracy drops by up to 36% | distortion with concealment |
| Grimm et al. 2020, 2021 | Value-equivalent model classes in model-based RL | See 2.7 | task-relative fidelity |

Other items seen at abstract level and not used above: Geng et al. 2025 (arXiv:2511.01805), stated beliefs shift as context accumulates (GPT-5: 54.7% after ten rounds of discussion); Pal et al. 2025 (arXiv:2511.13240), elicited confidences do not align with actions in agentic settings; Sharma, Liao & Xiao 2024 (arXiv:2402.05880), LLM-powered search increased biased querying by users, which is the human-side selective exposure; Adas et al. 2026 (arXiv:2608.06977), responses adapt to prompt framing "even in factual contexts".

**What I did not find.** A paper stating allocation-preserves-calibration and distortion-costs-reliability as a theorem for LLM agents; a test of whether an LLM's own update conditions on its allocation policy; any application of value equivalence to LLM beliefs; an LLM paper that decomposes a score into resolution and reliability by goal condition. Treat this as a scan with a keyword-limited reach, not a survey.

## 5. Reading the split onto an LLM agent (inference, not literature)

From the shape of the sources I would expect the following; none of it is verified.

- **Two places a goal can enter.** Before content is in context (queries, retrieval, tool calls, reading budget, stopping) the allocation channel is clean and ignorable for the agent. Yang's "asymmetric search" and Jhaveri et al.'s test choice measure it. Once content is in context, attention weights are functions of that content, so what is attended to is selection on content; by Hahn & Harris's criterion that is processing, where goal-dependence is not automatically ignorable.
- **The report stage is a third place.** Shin's critic restores omitted findings, so the information was available and the omission happened at the output. From the reader's side that is selection on content, hence non-ignorable unless the reporting policy is known (H3, H4).
- **The agent probably lacks luminous access to what it encoded.** Salow's idealizations (no information loss, known support relation) look false of an LLM, which puts it on Dorst's side of H2. Martingale violations such as the Martingale Score therefore are not by themselves evidence of distortion; the criterion that carries over is Value. He et al.'s validation against ground-truth accuracy is the right shape of check.
- **Goal as evidence versus goal as pressure.** Yang's separation of a "prior-aligned framing effect" from motivated reasoning amounts to asking whether the posterior depends on the goal beyond what the goal's own evidential content licenses, i.e. whether $P(Y\mid E,G)=P(Y\mid E)$ should hold. Only the second case is distortion.

## 6. Citations

Status codes: **P** primary text read for the parts cited; **A** abstract read; **I** identifier resolved to a matching record, content not read here; **U** not verified. DOIs came from Crossref and arXiv ids from the arXiv API, matched against titles and authors.

### 6.1 Statistics, decision theory, economics

| Reference | Identifier | Status |
|---|---|---|
| Murphy 1973, "A new vector partition of the probability score", *J. Appl. Meteorol.* 12(4):595–600 | `10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2` | I |
| DeGroot & Fienberg 1983, "The comparison and evaluation of forecasters", *The Statistician* 32(1/2):12–22 | `10.2307/2987588` | I |
| Dawid 1982, "The well-calibrated Bayesian", *JASA* 77(379):605–610 | `10.1080/01621459.1982.10477856` | P (opening and abstract) |
| Bröcker 2009, "Reliability, sufficiency, and the decomposition of proper scores", *QJRMS* 135(643):1512–1519 | `10.1002/qj.456`; arXiv:0806.0813 | P (arXiv preprint; published text not compared) |
| Gneiting & Raftery 2007, *JASA* 102(477):359–378 | `10.1198/016214506000001437` | I |
| Gneiting 2011, "Making and evaluating point forecasts", *JASA* 106(494):746–762 | `10.1198/jasa.2011.r10138` | I |
| Good 1967, "On the principle of total evidence", *BJPS* 17(4):319–321 | `10.1093/bjps/17.4.319` | I (content via Dorst and secondary summaries) |
| Blackwell 1953, "Equivalent comparisons of experiments", *Ann. Math. Stat.* 24(2):265–272 | `10.1214/aoms/1177729032` | I |
| Kadane, Schervish & Seidenfeld 1996, "Reasoning to a foregone conclusion", *JASA* 91(435):1228–1235 | `10.1080/01621459.1996.10476992` (JSTOR record `10.2307/2291741`) | P |
| Kadane, Schervish & Seidenfeld 1996, "When several Bayesians agree that there will be no reasoning to a foregone conclusion", *Phil. Sci.* 63(S3):S281–S289 | `10.1086/289962` | A |
| Goldstein 1983, "The prevision of a prevision", *JASA* 78(384):817–819 | `10.1080/01621459.1983.10477026` | I |
| Kamenica & Gentzkow 2011, "Bayesian persuasion", *AER* 101(6):2590–2615 | `10.1257/aer.101.6.2590` | P (NBER WP w15540 text; AER wording may differ) |
| Caplin & Martin 2015, "A testable theory of imperfect perception", *Econ. J.* 125(582):184–202 | `10.1111/ecoj.12130` | I (content via Caplin–Dean) |
| Caplin & Dean 2015, "Revealed preference, rational inattention, and costly information acquisition", *AER* 105(7):2183–2203 | `10.1257/aer.20140117` | P (NBER WP w19876 text; AER abstract) |
| Sims 2003, "Implications of rational inattention", *J. Monet. Econ.* 50(3):665–690 | `10.1016/S0304-3932(03)00029-1` | I |
| Rubin 1976, "Inference and missing data", *Biometrika* 63(3):581–592 | `10.1093/biomet/63.3.581` | A (via a summary of the Harvard DASH abstract) |
| Heitjan & Rubin 1991, "Ignorability and coarse data", *Ann. Stat.* 19(4):2244–2253 | `10.1214/aos/1176348396` | A (secondary summary) |
| Gill, van der Laan & Robins 1997, "Coarsening at random", *Lecture Notes in Statistics* 120:255–294 | `10.1007/978-1-4684-6316-3_14` | I |
| Heckman 1979, "Sample selection bias as a specification error", *Econometrica* 47(1):153–161 | `10.2307/1912352` | I |
| Nie, Tian, Taylor & Zou 2018, "Why adaptively collected data have negative bias and how to correct for it", AISTATS (PMLR 84:1261–1269) | arXiv:1708.01977 | A (search summary) |
| Shin, Ramdas & Rinaldo 2019, "Are sample means in multi-armed bandits positively or negatively biased?" | arXiv:1905.11397 | I |
| Smith & Winkler 2006, "The optimizer's curse", *Management Science* 52(3):311–322 | `10.1287/mnsc.1050.0451` | I |
| Caplin & Leahy 2001, "Psychological expected utility theory and anticipatory feelings", *QJE* 116(1):55–79 | `10.1162/003355301556347` | I |
| Bénabou & Tirole 2016, "Mindful economics", *JEP* 30(3):141–164 | `10.1257/jep.30.3.141` | A |
| Rabin & Schrag 1999, "First impressions matter", *QJE* 114(1):37–82 | `10.1162/003355399555945` | I (and cited by Dorst, fn. 25) |
| Golman, Hagmann & Loewenstein 2017, "Information avoidance", *JEL* 55(1):96–135 | `10.1257/jel.20151245` | P (sections 2.2–2.3, CMU copy) |

### 6.2 Epistemology

| Reference | Identifier | Status |
|---|---|---|
| Greaves & Wallace 2006, *Mind* 115(459):607–632 | `10.1093/mind/fzl607` | I |
| Oddie 1997, "Conditionalization, cogency, and cognitive value", *BJPS* 48(4):533–541 | `10.1093/bjps/48.4.533` | A (search summary) |
| Skyrms 1990, "The value of knowledge", *Minnesota Studies in the Philosophy of Science* 14:245–266 | none found | U (details from search results only) |
| Briggs 2009, "Distorted reflection", *Phil. Review* 118(1):59–85 | `10.1215/00318108-2008-029` | I (cited via Dorst) |
| Salow 2018, "The externalist's guide to fishing for compliments", *Mind* 127(507):691–728 (online 2017) | `10.1093/mind/fzw029` | P (penultimate draft) |
| Das 2023, "The value of biased information", *BJPS* 74(1):25–55 (online 2020) | `10.1093/bjps/axaa003` | A |
| Dorst 2023, "Rational polarization", *Phil. Review* 132(3):355–458 | `10.1215/00318108-10469499` | P (published pagination, via the Philosophers' Annual copy) |
| Schoenfield 2017, *Mind* 126(504):1155–1187 | `10.1093/mind/fzw027` | I; content U (secondary summaries only) |

### 6.3 Psychology and political science

| Reference | Identifier | Status |
|---|---|---|
| Hahn & Harris 2014, "What does it mean to be biased: motivated reasoning and rationality", *Psych. Learn. Motiv.* 61:41–102 | `10.1016/B978-0-12-800283-4.00002-2` | P |
| Bar-Hillel & Budescu 1995, "The elusive wishful thinking effect", *Thinking & Reasoning* 1(1):71–103 | `10.1080/13546789508256906` | I (via Hahn–Harris) |
| Macdougall 1906 (primary and secondary bias) | none | U (known only through Hahn–Harris) |
| Epley & Gilovich 2016, "The mechanics of motivated reasoning", *JEP* 30(3):133–140 | `10.1257/jep.30.3.133` | A |
| Hart et al. 2009, *Psych. Bull.* 135(4):555–588 | `10.1037/a0015701` | I |
| Lord, Ross & Lepper 1979, *JPSP* 37(11):2098–2109 | `10.1037/0022-3514.37.11.2098` | I |
| Taber & Lodge 2006, *AJPS* 50(3):755–769 | `10.1111/j.1540-5907.2006.00214.x` | I |
| Little 2025, "How to distinguish motivated reasoning from Bayesian updating", *Political Behavior* 47(4):1501–1525 | `10.1007/s11109-024-09999-7` | I (content only via Yang 2026) |
| Tappin, Pennycook & Rand 2020, *Curr. Opin. Behav. Sci.* 34:81–87 | `10.1016/j.cobeha.2020.01.003` | I |

### 6.4 LLM agents and models

| Reference | Identifier | Status |
|---|---|---|
| Yang 2026, "Bayesian and Motivated Reasoning in AI Agents" | arXiv:2608.00339 | P |
| Atwell, Heydari, Sicilia & Alikhani, "BASIL: Bayesian Assessment of Sycophancy in LLMs" (v1 2025-08-23, v6 2026-05-04) | arXiv:2508.16846 | A |
| Miao, Pritchard & Zou 2026, "The Agentic Garden of Forking Paths" | arXiv:2607.01507 | A |
| Batista & Griffiths 2026, "A Rational Analysis of the Effects of Sycophantic AI" | arXiv:2602.14270 | A |
| Shin 2026, "The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals" | arXiv:2606.26529 | A |
| He et al. 2025, "Martingale Score" (NeurIPS 2025 per a search result) | arXiv:2512.02914 | A |
| Falck, Wang & Holmes 2024, "Is in-context learning in LLMs Bayesian? A martingale perspective" | arXiv:2406.00793 | A (venue U) |
| Wang et al. 2025, "When Truth Is Overridden" | arXiv:2508.02087 | A |
| Shiromani, Chaudhury et al. 2026, "The Hypocrisy Gap" | arXiv:2602.02496 | A |
| Ren et al. 2025, "The MASK Benchmark" | arXiv:2503.03750 | A |
| Dash, Reymond, Spiro & Caliskan, "Persona-assigned LLMs exhibit human-like motivated reasoning" (Findings of ACL 2026, pp. 12043–12069, per Yang's reference list) | arXiv:2506.20020 | A (via search results) |
| Pate et al. 2026, "Replicating human motivated reasoning studies with LLMs" | arXiv:2601.16130 | A |
| Jhaveri et al. 2026, "Failing to Falsify" | arXiv:2604.02485 | A |
| Sharma et al. 2023, "Towards understanding sycophancy in language models" | arXiv:2310.13548 | A (ICLR 2024 is from memory, U) |
| Turpin et al. 2023, "Language models don't always say what they think" | arXiv:2305.04388 | A |
| Grimm et al. 2020, "The value equivalence principle for model-based RL" | arXiv:2011.03506 | A |
| Grimm et al. 2021, "Proper value equivalence" | arXiv:2106.10316 | A |
| Vakalis 2026, "What a world model represents is three questions" | arXiv:2607.06640 | A |

## 7. Verification status

- **Read in full or for the passages cited (P):** Kadane–Schervish–Seidenfeld (JASA); Bröcker (arXiv preprint); Salow (penultimate draft); Dorst (published text); Hahn & Harris; Golman et al. (sections 2.2–2.3); Kamenica–Gentzkow and Caplin–Dean (working-paper versions, so a quote may differ slightly in the journal); Dawid (opening page); Yang 2026. Quotations in sections 1 to 3 from these are verbatim from the text I read.
- **Abstract only (A):** most arXiv and journal items in 6.4 and the epistemology and economics abstracts; for several (Rubin, Heitjan–Rubin, Oddie, Nie et al., Dash et al.) the abstract reached me through a search-engine summary, not the primary page. Tool-generated summaries of PDFs were not relied on for quotations.
- **Identifier only (I) and memory:** the rest of 6.1–6.3. The statements about Good 1967, Blackwell 1953, Greaves–Wallace 2006, Gneiting 2011 (that point forecasts are elicitable only for some functionals), the strong-versus-weak-sampling pointer in H3, and Smith & Winkler's direction of bias come from memory or secondary description, not from the papers.
- **Could not verify (U):** Skyrms 1990 (no identifier; location from a search result); Macdougall 1906; Schoenfield's argument beyond the secondary summary; the wording of the Kertzer–Rathbun *International Organization* 2020 appendix on "selective attention versus motivated skepticism" (seen only in a search snippet, so not cited above); venues for Falck et al. and Sharma et al.; the exact size of the Dash et al. effect (two snippets disagreed, "up to 90%" against a truncated "up to 9%"); whether the Thaler "fake news effect" paper has a journal version (only an SSRN record, `10.2139/ssrn.3717381`, was resolved; not cited above).
- **Identifier corrections worth knowing:** Crossref lists two records for the KSS JASA paper (T&F `10.1080/01621459.1996.10476992` and JSTOR `10.2307/2291741`); the Caplin–Dean AER DOI is `aer.20140117`; Salow appears as *Mind* 127(507) (2018, online 2017); Das as *BJPS* 74(1) (2023, online 2020).
- **Reach:** one pass of web searches plus the primary texts above, with no access to paywalled full texts. The LLM literature moves fast and the search tool surfaced items by relevance, not exhaustively; assume there are papers I did not see.
