*Feeds **KR1.1** (O1: "we know, and can say plainly, what the theory is trying to illuminate"). Explorer for AAT Part I, "Adaptive Systems Under Uncertainty." Written 2026-10-30 by a Claude Opus 5.5 explorer at HEAD `4b7123c4`, for the owner-review peer (B).*

# Part I: what it claims about actual agents, and where it says so

## How this was read

I read whole, at HEAD: `01-aat-core/INTRODUCTION.md`; `01-aat-core/OUTLINE.md` lines 1–110; `NOTATION.md` lines 240–263 (GA-1…GA-5); and the bodies (frontmatter through Discussion, plus `## Findings` where present) of all 34 Part I segments in outline order. `result-persistence-condition` and `impl-persistence-and-limits` I read whole, Working Notes included. For the other 32 segments' Working Notes, I read every non-gold note whole and, inside each "Incidental audit gold" block, the "Follow-up items" and "Readers often ask" subsections whole. I skipped the Brief / Candidate Discussion / figures / belongs-elsewhere subsections unless something pointed there. Targeted reads: `deriv-sector-condition.md` (Cor A.1S.1 statement, lines 18, 211–286), `obs-section-i-validation-simulations.md` lines 1–60, `detail-operationalization.md` headings and measurement table, `ref/Prior_art_for_AAT_adaptive_tempo.md` (summary and reference list), and `ref/prior-art-analysis/03-lyapunov-persistence-bounds.md` lines 1–40. I verified two external citations by web search (Lindsey et al. 2013; Bürger & Lynch 1995). Others are marked "from memory" where I use them.

One disclosure, so the coordinator can weigh my verdict on the brief's expectation: before writing I read `owner-review/LOG.md`, including its hypothesis H-A. My agreement with H-A below is therefore a test of it, not an independent arrival.

## 1. What Part I is about, in my own words

Part I is a theory of **lossy tracking**. A system sees its world through a channel that destroys information. It keeps a compressed state. That state's predictions drift away from what actually arrives, and some correction process pulls them back. Everything in Part I concerns one quantity, the mismatch $\delta$ between prediction and observation, and one question: can the correction keep $\delta$ bounded while the world keeps moving? Objectives are absent by design.

- Chapters 1–2 make $\delta$ well-defined: boundary, channels, history, compressed state.
- Chapter 3 assembles the ingredients of the correction rate: gain, event rate, tempo.
- Chapter 4 says when the correction wins and what it costs. It also covers what happens when the correction cannot win however it is tuned.

Underneath the persistence inequality, I think Part I is trying to illuminate this: **failures to keep up come in distinct kinds, each kind has its own remedy, and each kind leaves its own observable trace.** The kinds are:

- correcting too slowly, or facing too much disturbance: fix with tempo or gain;
- holding the wrong kind of model: fix by changing the class;
- having an instrument too poor to see the error: fix the channel;
- correcting fine, but not well enough for the task: change tempo, disturbance, or tolerance.

The chapter-end synthesis comes closest to saying this (`impl-persistence-and-limits.md:89`): what is "most genuinely AAT's is not the inequality … but the stratification of adaptation into levels with different remedies and a residual-structure trigger." Its Working Notes then concede that no segment composes this into a decision procedure (`impl-persistence-and-limits.md:101`, "the operator decision tree … no segment composes them"). The thesis is visible from the end of the Part. It is not what the Part opens with, and not what the volume introduction sells.

## 2. The short answer, and my verdict on the brief's expectation

The brief's expectation was that the corpus answers "derived vs chosen inside the formalism" carefully, and answers "what does this claim about actual agents" in some places and not at all in others. For Part I, **I'd refine that rather than refute it.**

- **Derived vs chosen** is answered nearly everywhere and well: `form-agent-model.md:35`, `der-recursive-update.md:41`, `form-information-bottleneck.md:38–40`, `form-sector-condition.md:54–82`.
- **"What kind of claim about actual agents"** is answered in more places than "some", but in scattered sentences, never collected, and almost never with the two things Joseph is asking for: a concrete external instance where the quantities have been measured, and an observation that would show the claim wrong. The best lines are:
  - `result-persistence-condition.md:23`: a recurring structural pattern, not a model of any one domain; dominance is empirical.
  - `hyp-mismatch-dynamics.md:62`.
  - `persistence-and-limits-intro.md:22`.
  - `form-information-bottleneck.md:46`: "not prescriptive … characterizes what an optimal $\phi$ would look like."
  - `der-deliberation-cost.md:70`: "a *design criterion*, not a real-time decision procedure."
  - `form-sector-condition.md:56–82`: the sub-scope $\alpha$/$\beta$ partition, which is Part I's only real classification of agents.
  - `deriv-sector-condition.md:264`: the sector and bounded-disturbance assumptions "are *empirical claims* about the qualitative behavior of real correction dynamics."
  - `impl-persistence-and-limits.md:79`: "two epistemic strengths by column."
  - `der-mood-timescale.md:49`.

The root of Joseph's confusion, I think, is structural rather than a matter of missing sentences. **The corpus has one epistemic axis and his question needs three.**

- The tier labels (exact / conditional / robust-qualitative / heuristic / discussion-grade) grade the *strength of the inference*.
- Joseph is asking for the *kind of claim about the world*: scope, lens, conditional law, normative optimum, empirical regularity, or diagnostic.
- He is also asking for the *population*: which actual systems verifiably satisfy the hypotheses.

"Exact" on `result-persistence-condition` means the Lyapunov argument is valid. A reader, Joseph included, hears that the inequality is true of agents. Those are different claims, and nothing in the labeling separates them.

## 3. The claim kinds I use below

- **Scope**: says which systems the theory talks about. It cannot be wrong; it can only be badly drawn (too wide to exclude anything, or undecidable from the agent's side).
- **Lens**: a representational commitment ("describe the agent as carrying $M_t = \phi(\mathcal C_t)$"). Always available, so it is not falsifiable. Its value is what it lets you compute.
- **Identity**: a mathematical fact that holds for any system meeting stated hypotheses. Its falsifier is a hypothesis failing, not the identity failing.
- **Certificate**: "if the system has properties P, then guarantee G holds." It is true as mathematics. About an actual agent it says something only after P has been verified for that agent. Survival without the certificate does not refute it.
- **Normative optimum**: "under loss $L$, the best choice is X." It tells you what an agent able to choose *should* do. It predicts behavior only if a separate hypothesis is added: that selection or training pushes real agents toward the optimum.
- **Empirical regularity**: a claim about what real systems of some kind do, refutable by observation.
- **Diagnostic**: "observable O indicates condition C." Refuted by O appearing without C, or C without O.

## 4. Apparatus by apparatus

### 4.1 Information-loss boundary and the adaptive scope (`def-agent-environment`, `scope-adaptive-system`)

- **Kind:** scope.
- **Which agents:** any system with an observation channel and $H(\Omega_t \mid \mathcal C_t) \gt 0$. In practice that is every physical system. The scope excludes only the omniscient and the channel-less (`scope-adaptive-system.md:18`). So it is not a classification with empirical content, and the segment doesn't claim one.
- **Two real issues**, both in the gold and still open:
  - The predicate is evaluated from a God's-eye view over the true $\Omega_t$ (WN line 64). Membership is not decidable by the agent.
  - It carries no quantifier in $t$: an agent that fully identifies a static world exits scope mid-life (WN line 69).
- **Where it says so:** honestly, as scope (`def-agent-environment.md:13`, `:35`).
- **Where it doesn't:** the Part I introduction at `OUTLINE.md:10` reads "thermostats through commanders." That reads as a claim of breadth about results, when it is breadth of scope only. Joseph's own comment at `OUTLINE.md:9` calls this introduction "a mislead."

### 4.2 Agency scope (`scope-agency`)

- **Kind:** scope.
- **Content:** the binary-choice versus causal-contrast split is a real conceptual contribution ("nominal agents"). The "Which contrast counts" paragraph (`scope-agency.md:49`) resolves the active-perception case well.
- **Two issues remain:**
  - Condition 4 uses Pearl's $do$ before it is defined. The gold's strengthen-not-soften repair would state it in Part I primitives $T$, $h$ (WN line 73).
  - The contrast is ontological, not something the agent can know (WN line 81). So "is this system an agent?" is not answerable from the inside.
- **Kinds of agents** are listed (thermostats, RL agents, commanders, developers), but none is worked.

### 4.3 The reality model, recursive update, action selection (`form-agent-model`, `der-recursive-update`, `der-action-selection`)

- **Kind:** lens. The "derived" results are consequences of the lens's own completeness clause.
- **Where it says so:** honestly at the bodies, `form-agent-model.md:35` (alternatives named) and `der-recursive-update.md:41` ("the Markov structure is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete").
- **Where it doesn't:** `the-cycle-in-motion-intro.md:18` tells the reader "both are *derived*, not chosen." The gold flags this (WN line 65) and it is still in the body. A reader then meets `status: exact` on both and reasonably infers a discovered fact about agents.
- **Instance:** none is needed, since a lens has no empirical content.
- **Falsifier:** none.
- **What is missing:** a sentence saying which agents the lens fits badly, meaning where the cheapest faithful $M_t$ is the whole history. The gold's open $M_0$ / pretrained-prior question (`form-agent-model` WN line 62) is the live one for LLMs.

### 4.4 Information bottleneck and model sufficiency/fitness (`form-information-bottleneck`, `def-model-sufficiency`, `def-model-class-fitness`)

- **Kind:** a normative optimum (IB) plus definitions.
- **Which agents:** any compressor of history.
- **Where it says so:** "Characterizes the optimum, not the procedure" (`form-information-bottleneck.md:15`, `:40`, `:46`) is exactly the right statement of kind.
- **What it does not say:**
  - whether real agents approximate IB-optimal compression (the empirical-regularity version);
  - what observation would show they don't.
- **Fitness ceiling:** $\mathcal F(\mathcal M)$ is unobservable by construction. The segment says so (`def-model-class-fitness.md:14`, `:38`) and routes the agent to residual structure (see §4.9).
- **The reader question the corpus leaves open:** the intro's "keep what predicts" against structural adaptation's "keep slack for regime change" (`impl-persistence-and-limits.md:102`). It is a horizon question about the IB target, and it is stated nowhere.

### 4.5 Mismatch decomposition (`result-mismatch-decomposition`)

- **Kind:** identity. This is Part I's best-specified piece.
- **Which agents:** any predictor under GA-1 (fresh noise).
- **Concrete instance, named in the body:** the steady-state Kalman innovation variance $HP^-H^\top + R \gt R$, whose excess is the state-uncertainty floor (`result-mismatch-decomposition.md:45`).
- **Falsifier:** GA-1 fails (colored or history-correlated noise), and cross-terms reappear.
- **What it says about actual agents:** there are three distinct levers, and only one is "model better." The other two are "act to be better informed" and "change the instrument."

### 4.6 The gain principle (`emp-update-gain`)

This is the clearest case of three claim kinds fused under one label.

- **Labels, mutually inconsistent:**
  - frontmatter `type: empirical`;
  - equation tag `*[Empirical Claim (uncertainty-ratio-principle)]*` (`emp-update-gain.md:23`);
  - Epistemic Status opening "*Derived* under the Fisher-local invariance regime" (`:42`).
- **The three claims inside:**
  1. **Normative optimum, exact in the Fisher-local regime:** the Bayes-optimal gain is $U_M/(U_M+U_o)$ (Kalman, conjugate families). Its falsifier is mathematical.
  2. **Universal-rational claim:** "any rational adaptive process must approximate this functional form" (`the-cycle-in-motion-intro.md:26`). This is stronger than (1) and needs a definition of rationality outside Bayes. The gold flags it as an overclaim watch (`emp-update-gain` WN line 106).
  3. **Empirical regularity:** real adaptive systems' effective learning rates rise with their model uncertainty and fall with observation noise. This is the only claim of the three that fits the `empirical` type. It has been tested, in humans: motor adaptation rate against cue reliability, and learning rate against volatility versus stochasticity.
- **Where the empirical tests are:** the project's own prior-art search found them (`ref/Prior_art_for_AAT_adaptive_tempo.md`: Burge, Ernst & Banks 2008, row 41; Wei & Kording 2009, row 48; Piray & Daw 2020/2021/2024, rows 16, 24, 126; Mathys et al. 2014 HGF, row 3; summary at line 22). None is cited in the segment.
- **Where the segment's "Domain validation" table goes instead** (`emp-update-gain.md:69–75`): Kalman (exact), conjugate (exact), Q-learning (approximate), PID (simplified), developer ("structural analogy").
- **What the "Simulation validation" covers** (`:77`): simulation of the theory's own AR(1).
- **Upshot:** the evidence that would make this the one genuinely empirical segment in Part I sits in `ref/`, unconnected.

### 4.7 Event-driven dynamics and adaptive tempo (`form-event-driven-dynamics`, `def-adaptive-tempo`)

- **Kind:** definition, with a conditional operationalization: exact under channel-noise independence and isotropy (`def-adaptive-tempo.md:44`). That is honestly stated, including the *signed* deviation under dependence.
- **What it claims about agents:** speed and quality substitute, and "you cannot outrun a bad observation channel" (`:52`).
- **Instance:** information-form multi-sensor Kalman fusion, implicit but nowhere worked.
- **Falsifier:** correlated channels. The corpus has the correct signed treatment.
- **A narrative issue:** tempo is introduced as "the load-bearing capacity variable" and placed "on the left-hand side of the persistence condition." But the persistence theorem's left-hand side is $\alpha$, not $\mathcal T$. They coincide only for linear correction with $c_{\min} = 1$ (`der-gain-sector-bridge.md:43`, `:133`).
- **A leftover inconsistency:** `result-persistence-condition.md:79` still states the bridge as "$\alpha = \eta^\ast \cdot c_{\min}$", the per-event form, with "$\alpha = \mathcal T$ exactly". The 2026-05-30 fix made the bridge and stability segments per-time. This line was missed.

### 4.8 The persistence condition (`result-sector-condition-stability`, `result-persistence-condition`, with `form-sector-condition`, `der-gain-sector-bridge`)

- **Kind:** a certificate. This is the single most important answer for Joseph about Part I, and the corpus states it only at the end.
  - The theorem is valid Lyapunov ultimate-boundedness mathematics (Khalil ch. 4, 9).
  - About an actual agent, it says: if you can verify a sector floor $\alpha$ on a region $R$ and a disturbance bound $\rho$, containment is guaranteed.
  - By Lemma A.1N it is sufficient for the individual agent and necessary only over the *class* of correctors with that floor (`result-persistence-condition.md:41`, `:95`; `impl-persistence-and-limits.md:31`).
- **The consequence nobody draws:** the inequality as stated **cannot be refuted by observing an agent that survives below the threshold**. That is licensed, because the floor can be slack. An agent that fails above the threshold refutes only the claim that it satisfied the hypotheses. So the theorem's entire empirical content lives in the identification step (measuring $\alpha$, $\rho$, $R$ for a real system). Its natural user is a designer or verifier who can establish the hypotheses, not a scientist predicting which organizations die. The certificate-voice catalog (`impl-persistence-and-limits.md:111`) is the corpus's best text on this. It sits in a Working Note of the last segment.
- **Which agents.** The answer exists and is good; it is just not attached to the headline.
  - Sub-scope $\alpha$ (`form-sector-condition.md:58–68`): Kalman, conjugate Bayes, natural-parameter exponential families on a bounded interior, gradient descent on locally strongly convex losses, L2-regularized convex learners. For these the hypothesis is *derived*.
  - Sub-scope $\beta$ (`:70–82`): PID, rule-based systems, human and organizational judgment, misspecified or variational agents. For these it is *posited*.
  - `impl-persistence-and-limits.md:79` draws the honest consequence: "the engineered columns … satisfy the sector condition *by derivation*, the social columns … *by posit*, so the 'same inequality across domains' claim has two epistemic strengths by column."
- **Where the narrative contradicts this.** `INTRODUCTION.md:26` says the same inequality "governs a Kalman filter tracking a maneuvering target, a software team holding a codebase maintainable, and an organization keeping pace with a market; that it is one inequality and not an analogy among three is itself the result." Read against `impl-persistence-and-limits.md:79` and `result-persistence-condition.md:23`, that sentence is the overclaim the bodies carefully avoid: the Kalman instance is derived; the team and the organization are posited. The `OUTLINE.md:13` figure caption repeats misquotation #1 from the impl catalog ("Persistence fails exactly when drift outpaces gain times capacity"). That is the agent-level iff the corpus elsewhere refutes.
- **Concrete instance.** Kalman is the only one worked. The external instance the corpus is missing is the one it keeps naming as a domain, "extinction":
  - Quantitative genetics has had a measurable version of this inequality since the 1990s. Bürger & Lynch (1995, *Evolution* 49:151–163; verified) analyze a population whose mean phenotype "lags behind the optimum, but on the average evolves parallel to it; the magnitude of the lag determines the vulnerability to extinction." They derive "critical rates of environmental change" of under 10% of a phenotypic standard deviation per generation.
  - In AAT terms: $\rho$ is the optimum's drift rate; the correction rate is set by genetic variance times selection strength (the lag formula is from Lynch & Lande 1993, from memory, unverified); the failure threshold is lag load against reproductive capacity. That makes it a **task-adequacy** failure in AAT's own decomposition, not a structural one.
  - It has experimental tests. Lindsey, Gallie, Taylor & Kerr (2013, *Nature* 494:463–467; verified) evolved 1,255 *E. coli* populations under sudden, moderate and gradual rifampicin increase. Survival dropped "precipitously" with rate.
  - The repo has no citation of this literature (grep: "evolutionary rescue" 0 files; "Lynch" in one audit file only).
- **Falsifier, stated as the corpus could state it.** For a system in sub-scope $\alpha$ with measured $\alpha$, $\rho$, $R$: sustained containment failure while $\alpha R \gt \rho$ falsifies the claimed membership in the sub-scope or the disturbance model. For the cross-domain claim: in a domain where the quantities can be measured (the evolutionary-rescue experiments are one), the observed critical rate should scale as the inequality predicts with the correction-rate proxy. If it doesn't, the "recurring structure" claim fails for that domain.

### 4.9 The two-condition decomposition (structural persistence vs task adequacy)

- **Kind:** a definitional split whose value is diagnostic (routing to remedy). It is not falsifiable as stated, and it doesn't need to be.
- **Where it says so:** the segment's Findings claims *novelty* for it, at intuition-only search depth, with a targeted search "still owed" (`result-persistence-condition.md:139`, `:149`).
- **Two things a reader should know:**
  - For the canonical instance the decomposition collapses. Linear correction has $R \to \infty$, so structural persistence is "trivially satisfied" and only task adequacy binds (`result-persistence-condition.md:45`). It does work only for correctors with finite $R$ (saturating, breakdown, or a gradient learner with a finite basin). Many of these sit in sub-scope $\beta$.
  - The distinction has a long standard neighbor: control engineering's **stability versus performance** split (robust stability vs robust performance; Zhou, Doyle & Glover 1996, from memory). The repo has 0 hits for "robust performance" or "nominal performance." The owed search should start there. I would expect the novelty claim to reduce to "the standard stability/performance split, carried to non-engineered agents." That is still useful, but it is not "no direct anticipation known."

### 4.10 The containment dichotomy (Cor A.1S.1) and the introduction's headline #2

- **Kind:** an identity about sector-bounded SDEs.
  - $P(\tau_R \lt \infty) = 0$ under bounded disturbance with $\alpha R \gt \rho$.
  - $P(\tau_R \lt \infty) = 1$ under non-degenerate additive noise on any bounded region.
  - The segment's own Novelty Claim is honest: "component facts are textbook" (Khalil; Khasminskii). The novelty is packaging as a framework theorem (`deriv-sector-condition.md:286`). Its other line, "new exact result" (`:248`, `:280`), reads stronger than its own `:286`.
- **What the volume introduction makes of it.** `INTRODUCTION.md:27`: "for any sufficiently long-lived agent the need to change *what kind of model it is* … is … a certain eventual event." The same move appears at `deriv-sector-condition.md:18`, `result-persistence-condition.md:109`, and `impl-persistence-and-limits.md:33`. The step from "leaves $\mathcal B_R$" to "needs a new model class" requires $R$ to be the radius beyond which correction *fails*. In the bodies, $R$ is the radius where the sector bound is *certified* (`form-sector-condition.md:36`, `:50`). The two differ in exactly the cases that matter:
  - For the canonical agents, the sector holds globally ($R = \infty$: scalar Kalman, Beta-Bernoulli, strongly convex gradient; `der-gain-sector-bridge.md:67–71`). The dichotomy then says nothing about them.
  - For a corrector valid beyond its certified ball, exit is harmless, and an OU process returns.
  - The corpus's own Working Notes name the gap: "$R$ (dynamical …) and $\mathcal F(\mathcal M)$ (representational …) are distinct objects … no sentence in the chapter distinguishes them" (`impl-persistence-and-limits.md:100`).
  - The honest scope of headline #2 is agents whose correction genuinely breaks down at a finite radius (the "structural breakdown" $g$ of the simulations, `obs-section-i-validation-simulations.md:50`), under disturbance with unbounded support. Unbounded support is a property of the Gaussian idealization. Physical disturbances are bounded. Whether a real agent is "Model S" for this purpose is a fact about its tails, not about its correction strength.
- **A strengthening I'd offer before any softening.** The agent-relevant number is not $P(\text{exit}) = 1$ but the *expected time to exit*. The corpus never computes it (grep: no "Kramers", "Freidlin", "Wentzell"; "exit time" appears only as $\tau_R$'s definition). This is standard small-noise large deviations, my sketch, exact for the linear case and unverified for general sector $F$. For $d\delta = -\alpha\delta\,dt + \sigma_w\,dW$, the quasi-potential barrier at radius $R$ is $\alpha R^2/2$, so $\mathbb E[\tau_R] \asymp \exp(\alpha R^2/\sigma_w^2)$ up to a polynomial prefactor.
  - **Effect on the slogan:** that would turn "no correction strength buys that" into "correction strength buys *exponentially* long expected lifetimes, but never forever." This is both truer to what an agent experiences and sharper.
  - **Effect on the time constant:** it would also give structural adaptation its real time constant, which "generic" currently hides.
  - **Where it would land:** `deriv-sector-condition` beside A.1S.1, with the agent-level reading moved to the introduction.
- **The scaling half of the "two physics."** The $1/\alpha$ vs $1/\sqrt\alpha$ scaling is called "one of the volume's striking results" (`result-sector-condition-stability.md:19`). The project's prior-art analysis attributes exactly this lag-vs-gradient-noise dichotomy to Widrow et al. 1976 and Ljung & Priouret 1991 (`ref/prior-art-analysis/03-lyapunov-persistence-bounds.md:22–24`). Neither is cited in any Part I segment (grep: Widrow/Ljung only in `deriv-strategic-persistence-hard-ceiling` and `schema-strategy-persistence`).

### 4.11 Information-rate cost (`deriv-persistence-cost`, surfaced in the persistence segments and impl §2)

- **Kind:** a conditional lower bound (Model S, independent OU, high-resolution regime). Tight for Kalman–Bucy (Mitter & Newton 2005, cited).
- **What it says about agents:** persistence has a sustained information price, $\dot R \geq n\alpha/2$ nats/time.
- **Instance:** Kalman–Bucy.
- **Falsifier:** within scope, an estimator holding the bound at a lower supply rate. The impl's extension to LLM context budgets is honestly marked *[Hypothesis]* and proposed as an experiment (`impl-persistence-and-limits.md:41`, `:103`).
- **Neighbor literature:** the data-rate theorem (Nair & Evans 2004; Tatikonda & Mitter 2004) is named in `ref/prior-art-analysis/03…:28`. It is absent from `src/` (grep 0). `deriv-persistence-cost` cites Cover & Thomas and Mitter–Newton.

### 4.12 Structural adaptation necessity (`result-structural-adaptation-necessity`)

- **Kind:** the theorem is near-tautological: if no member of the class reaches the Bayes predictor, parametric search in the class can't reach it. The content is in the **diagnostic corollary**: persistent structured residuals after convergence indicate class inadequacy (`:17`, `:46`).
- **The observable:** "structured residuals versus white residuals" is the classical innovations whiteness test (Kailath; Mehra 1970). It is cited elsewhere in `src/` (`deriv-adaptive-gain-dynamics` and others) but not here.
- **What the whiteness test actually detects** is suboptimality *relative to what the history could support*, not class inadequacy specifically.
  - In a Kalman filter, a mis-set gain (wrong $Q$/$R$) produces correlated innovations; that is how Mehra's adaptive filtering detects it.
  - So the corollary distinguishes class failure from gain miscalibration only by excluding gain miscalibration in its hypothesis ("after excluding … gain-miscalibration causes", `:17`).
- **Contradiction:** `impl-persistence-and-limits.md:59` calls the residual corollary "the operational answer" to telling gain collapse (FM-2) from misspecification (FM-5). The corollary's own hypothesis puts that discrimination outside its reach. So the discrimination question the gold raises three times (`der-gain-sector-bridge` WN line 167) is still open, not answered.
- **"Necessity" is relative to the objective** (gold, WN line 113). An agent can also lower its tolerance or change its channel; the impl repeats this caveat (`impl-persistence-and-limits.md:61`).
- **A missing instance with a twist:** Lindsey et al. 2013 (above) found that gradual change *opened mutational paths* that sudden change closed. The *rate* of change shaped *which structural changes were reachable*. That bears directly on the rational-conservatism and neutral-variation material here (`:27`, `:73`), and it is a measured case.

### 4.13 Deliberation cost, mood timescale, temporal nesting

- **`der-deliberation-cost`:** a normative optimum, self-described as a design criterion (`:70`).
  - Its benefit term is *update-gain* improvement. Most of its examples (MCTS, chess, war-gaming) improve *action quality*. The gold flags the scope mismatch (WN line 118), and it stands.
  - Empirical-regularity version: high-drift environments favor fluency. That is testable against the speed–accuracy literature, but not tested or cited.
- **`der-mood-timescale`:** a normative optimum for a leaky-integrator estimator. It is exemplary in marking its tiers (`:39–43`) and its directional empirical corroboration (Kuppens et al. 2010, `:49`).
  - Falsifier available: in experience-sampling data, affective inertia should fall as environmental volatility rises, sublinearly as $\tau^\ast \propto \sqrt{\tau_{\mathrm{env}}}$.
  - It is the one Part I segment that names a population (humans), a measured quantity, and a direction.
- **`der-temporal-nesting`:** robust-qualitative, honestly attributed to singular perturbation (`:45`).
  - The machine-learning instance with a theorem is two-timescale stochastic approximation (Borkar; actor–critic needs a faster critic). It is cited in `deriv-adaptive-gain-dynamics` but not here, where it would serve as the RL instance ("policy updates before value function converges", `:59`).
  - `der-temporal-nesting.md:17` calls rational conservatism "a derived consequence of temporal nesting," but no inequality is derived. It is an argument.

### 4.14 Identity scope (`scope-agent-identity`)

- **Kind:** scope. It fixes which object (the trajectory token, not the type) the theorems index.
- **Where it says so:** honestly, including "whether the mathematical structure grounds something that deserves to be called 'identity' … is beyond AAT" (`:49`).
- **Claims it asserts, not derives:**
  - "No generally optimal merge exists" (`:31`). It depends on the criterion (gold WN line 93).
  - The (PI)/Čencov block. Several readers found it misplaced here, and the gold records why it is anchored here.
- **What it is for:** licensing the later volumes. It makes no claim about agents' behavior, and it shouldn't be read as making one.

### 4.15 CIY (`def-causal-information-yield`)

- **Kind:** definition. Its exploration use is a heuristic surrogate for expected information gain, honestly marked (`:31`, `:39`).
- **Placement:** most of its Discussion (query actions, deception, Part III) belongs elsewhere (gold WN line 77). It is not a Part I claim about agents.

## 5. Arc findings: where Part I's narrative and its bodies part ways

1. **There is no Part I introduction that says what kind of claims follow.** `OUTLINE.md:10` is one scope sentence, and `OUTLINE.md:9` is Joseph's own comment that it misleads. The scope cascade promised in `INTRODUCTION.md:39–41` never says, per tier, what kind of result each narrowing buys.
2. **The headline sentences overclaim relative to the bodies.**
   - `INTRODUCTION.md:26` ("one inequality and not an analogy among three") against `impl-persistence-and-limits.md:79` ("suggestion, not derivation … two epistemic strengths by column").
   - `INTRODUCTION.md:27` (certain need for class change) against the $R$ / $\mathcal F$ distinction the impl admits is never drawn (`:100`).
   - The figure caption at `OUTLINE.md:13`, which commits the agent-level iff.
   - The bodies have done the careful work; the front door undoes it.
3. **"Mathematically closed with simulation validation" (`INTRODUCTION.md:58`) needs its referent stated.**
   - What was validated: the simulations are AR(1) runs of the theory's own mismatch equation with five chosen $g$ functions (`obs-section-i-validation-simulations.md:44–50`). They check discrete-to-continuous consistency and exponent regimes.
   - What they don't show: that any real agent satisfies the equations.
   - What exists empirically: `empirica/` holds only these simulations (`track-b-nonlinear/`) and the glyph study. No Part I quantity has been measured on an agent the theory did not construct.
   - What could be measured: `detail-operationalization` has a usable estimator cookbook for $U_M$, $U_o$, $\hat\rho$, $\hat\alpha$, $\hat R$, $\delta_{\text{critical}}$. I found no record of it being applied to any real system.
4. **The worked anchor is promised but absent.** `INTRODUCTION.md:60` promises the snow driver "introduced where it does work." It appears in no Part I segment body (grep: "snow"/"wiper" only in `OUTLINE.md:12–13`). The only worked instance through Part I is the Kalman filter.
5. **The corpus asked "is it new?" and did not ask "is it true of real agents?"** The prior-art program in `ref/` (Undermind searches, 21 analyses) found the behavioral learning-rate experiments, Widrow's tracking dichotomy, and the data-rate theorem. These were used as *precedence* evidence. In the Part I segments I read, none appears as an *empirical anchor* or *instance*. Joseph's question is exactly the second use. This is integration debt with a specific shape, and the cheapest high-value fix in Part I.
6. **Falsifiers are named almost nowhere.** "Whether the mechanism is dominant is empirical" recurs (`result-persistence-condition.md:23`, `hyp-mismatch-dynamics.md:62`, `der-deliberation-cost.md:62`, `der-action-selection.md:53`). No segment says what observation would decide it.

## 6. What would make Part I answer Joseph's question

These are offered as directions, not a plan.

- **A one-paragraph claim card per load-bearing result**, carrying:
  - kind (from §3);
  - population (sub-scope $\alpha$ / $\beta$ or similar);
  - one external measured instance;
  - the observable;
  - what would show it wrong;
  - the inference tier (the existing label).

  Most of the content already exists, scattered; §4 above shows where.
- **A Part I introduction that states the thesis in §1.** Failures to keep up separate into kinds with different remedies and different observable traces. The persistence inequality is a certificate that a designer can establish for engineered correctors and can only posit for social ones.
- **Three external instances, all already in the literature:**
  - human learning-rate adaptation (already found in `ref/`) for the gain principle;
  - evolutionary rescue and the critical rate of environmental change (Bürger & Lynch 1995; Lindsey et al. 2013) for the persistence inequality and task adequacy;
  - two-timescale stochastic approximation for nesting.

  Each would turn a "structural analogy" row into a measured one, or show where the mapping breaks.
- **The exit-time strengthening of §4.10**, and an explicit $R$-versus-$\mathcal F(\mathcal M)$ paragraph at `form-sector-condition`. These make the containment headline say something true about actual agents.
- **Split `emp-update-gain` into its three claims**, with the empirical one carrying the citations it already has in `ref/`.

## 7. Adjacent notes and feedback

- **The Working-Notes gold contains resolved items that don't say so.** Two are self-annotated (`form-event-driven-dynamics` WN line 105; `der-recursive-update` WN line 70). Others I met were resolved silently, such as the per-time $\alpha$ fix. A reader mining gold re-raises closed issues; the annotator who found the first two said so.
- **Stale per-event form.** `result-persistence-condition.md:79` still carries the per-event bridge form after the 2026-05-30 per-time fix (§4.7).
- **Part-I-shaped results stored elsewhere.** `result-per-dimension-persistence` and `deriv-matrix-persistence-condition` are Part-I-shaped but live in Part III and Appendix A (`impl-persistence-and-limits.md:98`). A linear reader meets the per-dimension claim before it exists.
- **On the brief.** It worked well for me. The verbatim frame, the honest offered expectation marked "to be refuted," and the pointer to the gold as testimony were exactly the context I needed. The one thing I'd have liked earlier is the pointer to `ref/prior-art-analysis/` and `ref/Prior_art_*`. I found them late. They turned out to hold the empirical anchors Joseph's question needs, which is itself a finding about where the project keeps what it knows.
- **Scope honesty on this document.**
  - What I didn't read whole: the Appendix A derivations behind Part I (`deriv-sector-condition`, `deriv-gain-sector`, `deriv-recursive-update`, `deriv-persistence-cost`, `deriv-adaptive-gain-dynamics`, `der-multi-timescale-stability`, `result-sector-persistence-template`). I read only the lines cited.
  - My claims about their content rest on those lines and on the Part I bodies that summarize them.
  - The exit-time scaling in §4.10 and the Lynch & Lande and Zhou–Doyle–Glover attributions are unverified.
  - This document's finding list, not its silence, is its content.

## 8. Follow-up: the exit-time strengthening of the containment dichotomy (added 2026-10-30 at the owner-review peer's request)

*What was checked and what wasn't is marked at each step. Scripts and their full output are beside this file: `part-i-exit-time.py`, `part-i-exit-time-slope.py`, `part-i-exit-time-output.txt` (numpy 2.4.1, scipy 1.17.1, seed 20261030).*

### 8.1 The statement

Cor A.1S.1 says that under additive stochastic forcing the persistence region is left with probability one, whatever $\alpha$ is. The agent-relevant quantity is *when*. For the Model S mismatch dynamics $d\delta = -F(\delta)\,dt + \sigma_w\,dW_t$ ($W$ standard $n$-dimensional, $\sigma_w$ per coordinate), started inside, with $F$ satisfying A1/A2' on $\mathcal B_R$:

$$\liminf_{\sigma_w \to 0}\; \sigma_w^2 \log \mathbb E[\tau_R] \;\geq\; \alpha R^2,$$

with equality when $F$ is linear with symmetric part $\alpha I$ (for example $F(\delta) = \alpha\delta$, or $\alpha\delta$ plus a rotation). Write $\kappa = \alpha R^2/\sigma_w^2$. In the persistence segment's own quantities, $\kappa = \tfrac{n}{2}(R/R^\ast_S)^2$, where $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ is the Model S RMS radius. So the exponent is "how many RMS radii fit inside the certified region," squared, times $n/2$.

How each part of the statement stands:
- **Linear scalar case:** checked, and exact (§8.2).
- **Lower bound for general sector $F$:** derived, with my own proof of the barrier (§8.3), plus the Freidlin–Wentzell theorem for the barrier-to-exit-time step. Checked numerically on linear cases only.
- **Prefactor for general $F$:** not derived.

### 8.2 Linear scalar case: closed form, asymptotic, Monte Carlo (checked)

For $d\delta = -\alpha\delta\,dt + \sigma_w\,dW$ on $(-R, R)$ from $0$, the scale-function solution of $\tfrac{\sigma_w^2}{2}T'' - \alpha x T' = -1$ with $T(\pm R) = 0$ gives

$$\mathbb E_0[\tau_R] = \frac{2}{\sigma_w^2}\int_0^R e^{\alpha y^2/\sigma_w^2}\int_0^y e^{-\alpha z^2/\sigma_w^2}\,dz\,dy \;\sim\; \frac{\sqrt\pi}{2\alpha}\,\kappa^{-1/2}\,e^{\kappa} \quad (\kappa \to \infty).$$

At $\sigma_w = R = 1$ (so $\kappa = \alpha$), the exact quadrature against Euler–Maruyama Monte Carlo (2,000 paths, $dt = 10^{-4}$):

| $\kappa$ | exact $\mathbb E[\tau]$ | $\alpha\,\mathbb E[\tau]$ | Kramers asymptotic | exact/asymptotic | Monte Carlo (mean, s.e.) |
|---|---|---|---|---|---|
| 0.5 | 1.192 | 0.60 | 4.13 | 0.29 | 1.181, 0.022 |
| 1 | 1.445 | 1.45 | 2.41 | 0.60 | 1.460, 0.029 |
| 2 | 2.251 | 4.50 | 2.32 | 0.97 | 2.400, 0.048 |
| 3 | 3.787 | 11.4 | 3.43 | 1.11 | 3.859, 0.082 |
| 4 | 6.858 | 27.4 | 6.05 | 1.13 | 7.011, 0.152 |
| 6 | 26.98 | 162 | 24.3 | 1.11 | — |

What the table shows:
- **Monte Carlo matches the closed form** within about two standard errors. Discrete monitoring biases it upward slightly: at $\kappa = 2$, $dt = 10^{-3}$ gives 2.424 and $dt = 2\times10^{-5}$ gives 2.252, against an exact 2.251.
- **The asymptotic form is accurate to about 10% from $\kappa \approx 2$ on**, and wrong below $\kappa \approx 1$, which is the diffusive regime.
- **Exit becomes memoryless.** The exit times' coefficient of variation is about 0.97–0.98 at $\kappa = 4$ in the scalar case and at $\kappa \approx 4$ in the 2-D case below. That matches the known small-noise result that $\tau/\mathbb E[\tau]$ tends to an exponential law (from memory, not checked beyond this). Exit then behaves as a **hazard** with rate $1/\mathbb E[\tau]$, not a deadline.

### 8.3 General sector $F$: the barrier lower bound (derived; checked on linear cases)

Freidlin–Wentzell (*Random Perturbations of Dynamical Systems*, ch. 4, from memory) applies to $D = \mathcal B_R$ when four conditions hold:
- the noiseless flow $\dot\delta = -F(\delta)$ has a unique equilibrium in $D$ attracting all of $D$;
- the drift points inward on $\partial D$;
- $F$ is locally Lipschitz;
- the noise is additive and non-degenerate.

Under those conditions, $\sigma_w^2 \log \mathbb E[\tau_R] \to \min_{\partial D} V$, where $V(x) = \inf \tfrac12\int_0^T \lVert\dot\varphi + F(\varphi)\rVert^2 dt$ over paths from $0$ to $x$. A2' on $\mathcal B_R$ supplies the first two: $\tfrac{d}{dt}\lVert\delta\rVert^2 \leq -2\alpha\lVert\delta\rVert^2$, $F(\delta) \neq 0$ for $\delta \neq 0$, and $\delta^\top(-F) \leq -\alpha R^2 \lt 0$ on the boundary. Lipschitz regularity is the one extra hypothesis.

**The bound $V(x) \geq \alpha\lVert x\rVert^2$** (my derivation, not independently checked):
1. Take any path $\varphi$ in $\bar{\mathcal B}_R$ from $0$ to $\lVert x\rVert = R$. Set $u = \dot\varphi + F(\varphi)$ and $r = \lVert\varphi\rVert$.
2. Almost everywhere, $\dot r = \varphi^\top u/r - \varphi^\top F(\varphi)/r \leq \lVert u\rVert - \alpha r$.
3. Let $\varrho$ solve the scalar equation $\dot\varrho = \lVert u\rVert - \alpha\varrho$ with $\varrho(0) = 0$. By comparison, $r \leq \varrho$, so $\varrho(T) \geq R$.
4. For the scalar path, $\tfrac12\int(\dot\varrho + \alpha\varrho)^2 = \tfrac12\int(\dot\varrho - \alpha\varrho)^2 + \alpha\varrho(T)^2 \geq \alpha R^2$.
5. Therefore $\tfrac12\int\lVert u\rVert^2 \geq \alpha R^2$, and $V \geq \alpha R^2$ on the boundary.

**Equality holds for the linear isotropic case**, where the stationary density gives $V = \alpha\lVert x\rVert^2$ exactly. More generally, for linear $F(\delta) = A\delta$ the barrier is $\min_{\lVert x\rVert = R} V = R^2/(2\lambda_{\max}(\Sigma))$, with $A\Sigma + \Sigma A^\top = I$.

**Numerical checks:**
- Over 20,000 random 2-D/3-D matrices $A$ with $\alpha = \lambda_{\min}(\mathrm{sym}\,A) \gt 0$, the smallest ratio of barrier to $\alpha R^2$ was 1.0000. The bound held in every case and was attained.
- A rotation $\alpha I + \omega J$ is tight, at ratio 1.0000.
- The non-normal $A = \begin{pmatrix}1 & 1.2\\ 0 & 1\end{pmatrix}$ has $\alpha = 0.400$ and barrier 0.486. A 2-D Monte Carlo at $\sigma_w \in \{0.5, 0.44, 0.39, 0.35\}$ (barrier/$\sigma_w^2$ from 1.9 to 4.0) gives local slopes of $\log\mathbb E[\tau]$ against $1/\sigma_w^2$ of 0.476, 0.479, 0.450 (overall 0.468). That approaches the barrier 0.486, not the sector floor 0.400.
- At larger $\sigma_w$ (barrier/$\sigma_w^2 \lt 1.6$) the fitted slope was 0.80. That is the diffusive pre-asymptotic regime, consistent with the scalar case, where the local slope of $\log(\alpha\,\mathbb E[\tau])$ against $\kappa$ exceeds 1 below $\kappa \approx 1.5$. I report it so nobody reruns at large noise and is surprised.
- Nonlinear gradient $F$ was checked in 1-D only. $F = \alpha\delta + \beta\delta^3$ has barrier $\alpha R^2 + \beta R^4/2$, and its exact $\mathbb E[\tau]$ exceeded the linear-$\alpha$ value: 2.11 vs 1.45 at $\alpha = 1$, $\beta = 2$. That is the expected direction: the floor only bounds from below.

**Not checked or not derived:**
- the prefactor for general sector $F$;
- non-isotropic noise $\Sigma_w$ (presumably an $\alpha$ measured in the $\Sigma_w^{-1}$ metric);
- discrete-time correctors (DA2'), which need the discrete small-noise theory;
- state-dependent noise;
- and, decisively for the agent reading, heavy tails. Under jump or Lévy disturbance, exit is driven by a single large jump. Expected exit time then scales *polynomially* in the noise, not exponentially (Imkeller & Pavlyukevich and successors, from memory). Heavy-tailed environments are where the exponential reserve genuinely fails. That is a sharper statement of the heavy-tail gap the gold already flags at `result-sector-condition-stability` WN line 85.

### 8.4 What this changes in Part I, if it holds

1. **The dichotomy's agent-level reading inverts.** "No correction strength buys containment" is true only in the limit $T \to \infty$. At every finite horizon, correction strength buys expected tenure *exponentially* in $\kappa$. Going from $\kappa = 3$ to $\kappa = 6$ multiplies the expected time to leave the certified region by about 14 (exact table: $\alpha\,\mathbb E[\tau]$ goes from 11.4 to 162). "Certain eventual event" stays true, but the informative object is the hazard rate, about $1/\mathbb E[\tau]$, which $\alpha$, $R$ and $\sigma_w$ control.
2. **The Model S persistence condition, as stated, is weak.** The condition is $\alpha \gt n\sigma_w^2/(2R^2)$ (`result-persistence-condition.md:39`). That is exactly $\kappa \gt n/2$. At $\kappa = 1/2$ in one dimension, $\alpha\,\mathbb E[\tau] \approx 0.60$: the certified region is left, on average, in less than one correction time constant. So the condition certifies the *typical scale* of mismatch and almost nothing about *staying in the region*. A Model S condition indexed by lifetime would carry the content the current one lacks. To leading order, that condition is $\mathbb E[\tau_R] \geq T_{\text{req}}$, roughly $\kappa \gtrsim \ln(\alpha T_{\text{req}})$.
3. **The hand-off to structural adaptation becomes quantitative**, with the $R$-versus-$\mathcal F(\mathcal M)$ caveat of §4.10 unchanged. In a Gaussian-noise world, an agent whose correction truly breaks at $R$ faces class-failure events as a hazard with rate about $\alpha\sqrt{\kappa}\,e^{-\kappa}$. "Generic over an unbounded horizon" becomes a rate one could estimate with `detail-operationalization`'s existing estimators for $\hat\alpha$, $\hat R$ and $\hat\sigma_w$.
4. **Placement.** Natural canon landing: a companion corollary beside A.1S.1 in `deriv-sector-condition` (statement and §8.3 argument), with the reading in §8.4.1–2 carried by `result-persistence-condition` and the volume introduction. Before that, two things are owed:
   - an independent check of the §8.3 comparison argument, and of the Freidlin–Wentzell hypotheses as applied;
   - a literature check: the barrier bound under a one-point strong-monotonicity drift may already be stated in the large-deviations or stochastic-stability literature, in which case canon should cite it rather than derive it.

**Verdict:** the sketch held up. The linear case is exact and numerically confirmed. The general sector bound has a short proof, and on the cases tested it is attained when the symmetric part is isotropic and strict otherwise. It falls apart where I expected: the prefactor for general $F$, and heavy-tailed disturbance.
