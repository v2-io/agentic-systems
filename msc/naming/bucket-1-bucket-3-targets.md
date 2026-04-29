# Bucket 1 + Bucket 3 Targets — for Targeted Alternative Generation

Generated from `msc/naming/naming-aggregate-r2-votes.json` on 2026-04-29.

**Bucket 3** (15 targets): single +1 keep votes with no alternatives proposed.
**Bucket 1** (619 targets): single-architecture only — votes from only one of Codex / Gemini / Opus / Sonnet / Haiku (or agent1 / audit, treated as their own architectures).

Excluded as non-concept: file-pointers (`*.md`, `README`, `CLAUDE`, `TODO`, etc.), section-header references (`## Working Notes`), parenthetical-comment rows, $-formula-only rows, and the `[unnamed: ...]` / `[concept: ...]` rows already handled by the consolidation pass.

Description column: a short excerpt from the first non-empty agent note on the target. Read it as a hint, not as a full picture — the segment material is what an agent should engage with directly.

Within Bucket 1, targets are grouped by architecture and sorted by total aggregate weight descending. Tier banding:
- **Strong** (total ≥ +5): the proposing architecture put real conviction here; cross-architecture pressure-testing is high-value.
- **Moderate** (total +2..+4): meaningful single-architecture engagement.
- **Light** (total +1): a single weak keep or rename, low conviction. Pressure-testing here may matter or may surface that the target is genuinely low-leverage; either result is signal.
- **Net-rejected** (total ≤ 0): the proposing agent considered and rejected; included for completeness.

---

## Bucket 3 — single +1 keep, no alternatives (15 targets)

- **`adversarial edge targeting`** (agent: opus-4-7-b) — Keep (even though the segment is currently a GAP — the slug is reserving a memorable-noun slot). "Edge targeting" is vivid; the attacker aims *at speci
- **`canonical formulations`** (agent: opus-4-7-r2) — The middle ring in FORMAT.md's three-rings; in use but slightly redundant ("canonical" + "formulations" both name the chosen-among-alternatives quality
- **`coherence coupling measurement`** (agent: opus-4-7-b) — Keep.
- **`communal imagination test`** (agent: opus-4-7-b) — Keep. Names the evaluation criterion in a way that's memorable and actionable. Borrowed from the naming principles document itself.
- **`da2 inc`** (agent: opus-1m) — Technical; symbol-grade. The prose equivalent "incremental sector bound" works; keep symbol as shorthand.
- **`logozoetic agents`** (agent: codex-2) — Higher novelty cost than "logogenic," but the moral-weighting distinction is real and English alternatives are sloppier.
- **`section ii actuated adaptation agentic systems`** (agent: haiku-4-5) — Slightly verbose; "Actuation" is the weaker semantic fit (Section II is mostly about purposeful agency; actuation is one mechanism enabling it). CLAUDE
- **`sector condition derivation`** (agent: haiku-4-5) — Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep.
- **`software scope`** (agent: opus-4-7-b) — Keep. Direct.
- **`strategy`** (agent: gemini-3-1-pro-preview-r2) — Standard.
- **`temporal coherence markers`** (agent: opus-4-7-r2) — Weak keep — logozoetic norm. The slug names the markers themselves rather than the norm-claim about them; could be more substantive ("#norm-out-of-band
- **`worked example bandit`** (agent: haiku-4-5) — End-to-end RL bandit instantiation (approximate). Self-descriptive. Keep.
- **`worked example kalman`** (agent: haiku-4-5) — End-to-end Kalman instantiation (exact). Self-descriptive. Keep.
- **`worked example l1`** (agent: haiku-4-5) — L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison. Self-descriptive. Keep.
- **`worked example strategy`** (agent: haiku-4-5) — Section II strategy DAG instantiation (3-arm bandit). Self-descriptive. Keep.

---

## Bucket 1 — single-architecture targets (619 targets)

### Codex only (161 targets)

#### Strong (≥ +5) — 6

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `adaptive cycle` | +6 | 2 | (keep) +6 | Strong central noun phrase: specific enough to own, broad enough to travel across the framework. |
| `effects spiral` | +6 | 2 | (keep) +6 | Memorable without being whimsical. It is the kind of pattern-name people will actually reuse in discussion. |
| `strategic composite` | +6 | 3 | (keep) +3; equilibrium composite +3 | Needed to distinguish equilibrium-convergent composites from alignment composites. |
| `class 1 class 2 class 3` | +5 | 2 | modular merged scaffolded architecture classes +3; architecture classes +2 | Better prose handles than bare class numbers. My preferred trio avoids overloading integrated and keeps Class 3's external-architec |
| `praxis` | +5 | 2 | (keep) +5 | Strongest of the five phase names after aporia; instantly sayable and philosophically apt. |
| `prolepsis` | +5 | 2 | (keep) +5 | Earns its foreignness because "anticipation" would flatten the active-modeling point. |

#### Moderate (+2..+4) — 125

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `agentic systems framework ASF` | +4 | 2 | agentic systems +4 | The repo's public face is already "Agentic Systems"; the extra acronym buys little and increases cognitive inventory. |
| `blind pursuer` | +4 | 2 | (keep) +4 | Borderline stylized, but memorable and semantically right for goal pursuit without a real world model. |
| `catastrophic forgetting regime` | +4 | 2 | empty window pathology +2; (keep) +2 | Good mechanism alias. Do not replace catastrophic forgetting when citing ML lineage. |
| `epistrophe` | +4 | 3 | (keep) +4 | Slightly harder on first contact than "update," but it preserves the turning-toward distinction the theory actually uses. |
| `a2 prime sub scope partition` | +3 | 1 | sector scope partition +3 | Strong umbrella for alpha_1, alpha_2, beta, alpha_3, and future sub-scope labels. |
| `a2 sub scope partition` | +3 | 1 | sector scope partition +3 | Much cheaper in prose than theorem-label-plus-apostrophe. The reader needs to know this is the sector-condition scope split. |
| `adaptive tracker` | +3 | 1 | (keep) +3 | Excellent name for structured model without structured objective. |
| `additive coordinate forcing family` | +3 | 1 | forced coordinates family +3 | Use forced coordinates as the family phrase across Cauchy, Fisher, IB, and Legendre instances. |
| `agent identity as one non forkable causal record` | +3 | 1 | singular trajectory commitment +3 | Excellent prose handle for the token-level scope of AAD. |
| `agentic systems` | +3 | 1 | (keep) +3 | Broad, durable umbrella name that comfortably houses AAD, TST, and the later agent classes without sounding like a fad product cate |
| `aisthesis` | +3 | 2 | (keep) +3 | Slightly less sticky than the other Greek phase names, but it preserves the raw-contact distinction well enough to keep. |
| `alpha1 fixed gain a2 sub scope` | +3 | 1 | fixed gain regime +3 | "Lands in alpha1" is decoder-ring prose. The English label is much cheaper in discussion. |
| `alpha2 adaptive gain a2 sub scope` | +3 | 1 | adaptive gain regime +3 | Same reasoning as alpha1: the English does the work the symbol cannot do in prose. |
| `bounded mismatch region` | +3 | 1 | persistence envelope +3 | Strongest new shared proposal from the other votes. Flight-envelope connotations fit the safe operating region exactly. |
| `c i c ii c iii c iv` | +3 | 1 | composition routes +3 | Use routes consistently for shared-objective, hierarchical, mutual-benefit, and strategic composition. |
| `c iv` | +3 | 1 | strategic convergence route +3 | Better than saying equilibrium route only, because convergence is the scope condition. |
| `closure defect` | +3 | 1 | (keep) +3 | Excellent quantity name for epsilon-star. It is short and memorable. |
| `composition consistency inheritance across scales` | +3 | 1 | heredity commitment +3 | Good name for the stronger expectation that composite admissibility should inherit from sub-agent properties plus topology. |
| `correlated channel overcount` | +3 | 1 | redundancy penalty +3 | More neutral and technical than my earlier redundancy illusion. Use illusion for the cognitive error, penalty for the quantity. |
| `cross agent model of self and model of other coupling` | +3 | 1 | cross model coupling +3 | Strong English complement to kappa-style coupling terms in opacity and theory-of-mind discussions. |
| `da2 inc ≡ ct2 at m i equivalence` | +3 | 1 | sector contraction equivalence +3 | The point is the equivalence between the incremental sector bound and Euclidean contraction. The current label reads like notebook |
| `da2 prime inc` | +3 | 1 | incremental sector bound +3 | Use this English name in prose. The symbol is only useful in tables and formal derivations. |
| `da2 prime inc equals ct2 at m equals i` | +3 | 1 | sector contraction equivalence +3 | Excellent reusable handle for the Euclidean bridge between incremental sector structure and contraction. |
| `deliberate expenditure to make hidden nodes observable` | +3 | 1 | observability investment +3 | Important strategic repair for evidence starvation and credit-assignment collapse. |
| `derivation audit tables` | +3 | 1 | (keep) +3 | Strong keep. This names a concrete artifact and a valuable house practice at the same time. |
| `distributed tempo` | +3 | 2 | (keep) +2; network tempo +1 | Good team-level tempo extension. |
| `dormant structural variation that becomes useful after regime change` | +3 | 1 | latent structural diversity +3 | Strong Section III and structural-adaptation term. It names adaptive potential that present fitness measures hide. |
| `fisher whitened update` | +3 | 1 | (keep) +3 | Accurate, compact, and tied to the real mathematical operation. |
| `goal biased retrieval from persistent memory` | +3 | 1 | goal conditioned reconstruction +3 | Important Class-2 failure mode: retrieval can be contaminated by the current objective rather than reconstructing the chronica neut |
| `goal-blind routing` | +3 | 1 | (keep) +3 | Strong phrase. It makes the directed-separation condition under composition easy to remember. |
| `grafting` | +3 | 1 | strategic grafting +3 | Excellent name for adding a new causal branch or imported structure into the strategy DAG. |
| `identifiability coefficient` | +3 | 1 | (keep) +3 | Strong scalar name for the causal-attribution discount on edge updates. |
| `identifiability floor family` | +3 | 1 | identifiability floor +3 | Keep floor as the family noun. |
| `l0 l1 l1 prime l2` | +3 | 1 | correlation hierarchy +3 | Strong canonical name for evidence-correlation regimes. |
| `latent structural capacity` | +3 | 1 | (keep) +3 | Strong name for low-credence or inaccessible structure that preserves future adaptability. |
| `learning freeze from low model uncertainty or high observation uncertainty` | +3 | 1 | gain collapse +3 | Strong unifying name for dogmatism-like and nihilism-like failures of update gain. |
| `log odds coordinate` | +3 | 1 | (keep) +3 | Canonical statistical name; should not be replaced by a project-specific metaphor. |
| `logogenic agents` | +3 | 1 | (keep) +3 | Novel, but the novelty earns its keep by naming a structural channel property rather than a transient implementation. |
| `loop` | +3 | 1 | (keep) +3 | The loop/cycle distinction is one of the clearest naming wins in the corpus. |
| `model sufficiency relative to an agent s own chronica` | +3 | 1 | trajectory indexed sufficiency +3 | Important consequence of singular chronica and agent identity. This deserves a stable name. |
| `observability and opacity pair` | +3 | 1 | legibility opacity duality +3 | Good name for the formal dual between how well an agent sees the world and how well observers can predict the agent. |
| `p ij` | +3 | 1 | edge credence +3 | Strong Bayesian prose default. Better than confidence weight because it signals degree of belief. |
| `persistent residual autocorrelation` | +3 | 1 | structured residuals +3 | Key diagnostic for model-class failure and structural adaptation. This should be first-class vocabulary. |
| `predictive relevance depending on the policy the agent will run` | +3 | 1 | policy relative epistemology +3 | Strong name for the IB and sufficiency caveat that what counts as predictive depends on action policy. |
| `projection contraction must beat target drift` | +3 | 1 | contraction over drift principle +3 | Strong compact name for the core organizing slogan. It is more reusable than the full sentence. |
| `regime i ii a ii b iii` | +3 | 1 | reception regimes +3 | Good umbrella for informative update, magnitude shock, structural shock, and ambient noise. |
| `regime ii a` | +3 | 1 | magnitude shock regime +3 | Strong and precise. |
| `regime ii b` | +3 | 1 | structural shock regime +3 | Strong and precise. |
| `retrieval keyed by state rather than current objective` | +3 | 1 | goal-blind retrieval +3 | Strong architectural counterpart to goal-blind routing. This is the memory-side directed-separation repair. |
| `richest operationalization domain` | +3 | 1 | calibration laboratory +3 | The older framing is vague and comparative; the newer one explains the role instead of hand-waving it. |
| `separability pattern family` | +3 | 1 | separability ladder +3 | Use ladder for the repeated pattern of exact core, structured repair, and general open. |
| `stability plasticity window` | +3 | 1 | (keep) +3 | Excellent name for the feasible forgetting-rate interval. |
| `strengthen first then soften posture` | +3 | 1 | strengthen first posture +3 | The mnemonic is in the first half. "Then soften" is still the policy, but it does not need to sit in the name. |
| `structural persistence` | +3 | 1 | (keep) +3 | The structural, operational, continuity split is useful and should stay stable. |
| `survival imperative exploration drive` | +3 | 1 | survival exploration +3 | The long form explains the result, but the reusable subject noun should be shorter. Use full phrase at first mention, then survival |
| `symbol default da2 inc` | +3 | 1 | incremental sector bound +3 | `#composition-closure` already gives the English. Use the symbol only where the exact algebraic condition matters. |
| `symbol default sigma t in prose` | +3 | 1 | strategy +3 | After first introduction, the English should be the prose default. The symbol is still right in equations and exact statements. |
| `terminal reached but $O_t$ unsatisfied` | +3 | 1 | terminal alignment error +3 | This is the diagnostic behind satisfaction gap in many examples; it deserves a stable phrase. |
| `tests as reusable interventions` | +3 | 1 | probe library +3 | Upgrading my earlier +2. The other votes reinforced that tests are not just checks; they are reusable Level-2 probes. |
| `transfer assumption table` | +3 | 1 | (keep) +3 | Exact and operational. This is the phrase readers need when moving results out of software into weaker-identification domains. |
| `triple depth penalty` | +3 | 1 | (keep) +3 | Very useful phrase for confidence decay, evidence starvation, and cognitive cost compounding with depth. |
| `unnamed coupling between an agent s model of self and model of other the prose form of kappa cross` | +3 | 1 | cross model coupling +3 | Clean English complement to kappa_processing. This gives the opacity and theory-of-mind work a reusable noun slot. |
| `unnamed organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate` | +3 | 1 | contraction over drift principle +3 | The slogan is too long to cite repeatedly. A short label would let intros and reviews point back to it cleanly. |
| `unnamed software as AAD s privileged high identifiability calibration laboratory` | +3 | 1 | calibration laboratory +3 | This phrase deserves to be promoted to the stable short name; it is central to TST's architectural role. |
| `unnamed stronger composition consistency demand that composite admissibility inherit from sub agent properties plus topology` | +3 | 1 | heredity commitment +3 | Strong name from the jacobian-strengthening spike: short, memorable, and explicit about the architectural bet being made. |
| `unobservable strategy subgraph` | +3 | 1 | epistemic dead zone +3 | Better than observability dead zone: it names the consequence, not only the cause. |
| `OODA4 framework enforcing adaptive cycle separation` | +2 | 1 | agentic scaffold +2 | Useful logogenic implementation term, but keep it downstream of directed-separation machinery. |
| `a1 a2 a3 a4` | +2 | 1 | macro dynamics admissibility +2 | Good umbrella for the macro-agent constraints in composition closure. |
| `accumulated loss across context resets` | +2 | 1 | turnover drift +2 | Good logogenic name for degradation caused by repeated context turnover. |
| `action distinguishability` | +2 | 1 | (keep) +2 | Useful alias for causal information yield in intuitive explanations. |
| `adversarial edge target argmax` | +2 | 1 | edge targeting optimum +2 | Good name for the emitter-recipient 16-cell targeting solution. |
| `agent visible but objective irrelevant metric` | +2 | 1 | vanity metric +2 | Standard operational term that AAD can formalize as high observability with low causal relevance to O_t. |
| `alignment uncertainty` | +2 | 1 | (keep) +2 | Keep as a distinct term from source calibration. |
| `alpha prime sub scope` | +2 | 1 | potential monotone tier +2 | Useful readable alias for potential and monotone games where sector-style transfer works. |
| `bathtub analogy for persistence condition` | +2 | 1 | bathtub model +2 | Useful teaching name if the README adds Alan's bathtub gloss. |
| `beta prime sub scope` | +2 | 1 | equilibrium set tier +2 | Good honest alias for the CCE or set-convergence fallback. |
| `c i` | +2 | 1 | shared objective route +2 | Good route name for composite-agent scope. |
| `c ii` | +2 | 1 | hierarchical derivation route +2 | Good route name for composite-agent scope. |
| `c iii` | +2 | 1 | mutual benefit route +2 | Good route name for composite-agent scope. |
| `c1 c2 c3` | +2 | 1 | convention hierarchy +2 | Canonicalize this as the value-object convention family. |
| `closure defect bridge lemma` | +2 | 1 | closure bridge +2 | Shorter reusable phrase while preserving the formal bridge lemma title. |
| `closure defect consuming macro reserve` | +2 | 1 | closure load +2 | Good name for the pressure epsilon-star times macro-rate places on composite persistence. |
| `code quality and tempo positive feedback` | +2 | 1 | comprehension flywheel +2 | Good positive-loop counterpart to quality-tempo spiral. Use flywheel for virtuous accumulation, spiral for both directions. |
| `code quality feedback loop through tempo` | +2 | 1 | quality tempo spiral +2 | Good TST name for virtuous or vicious code-quality dynamics. |
| `correlated evidence overconfidence` | +2 | 1 | redundancy illusion +2 | Good name for overcounting correlated channels as independent tempo. |
| `crossing from multi agent to composite scope` | +2 | 1 | crossing +2 | Useful name for transitions into or out of composite-agent status. |
| `default signal function` | +2 | 1 | (keep) +2 | Good canonical phrase for the gradient-based attribution update. |
| `deliberation threshold` | +2 | 1 | (keep) +2 | Good handle for the inequality deciding whether deliberation pays. |
| `effective disturbance` | +2 | 1 | (keep) +2 | Useful and conventional enough for the max-with-zero construction. |
| `empty stability plasticity feasibility window` | +2 | 1 | stability plasticity collapse +2 | Better AAD-native failure phrase than catastrophic forgetting when the mechanism matters. |
| `equilibrium convergence` | +2 | 1 | (keep) +2 | Good subject phrase for the strategic-composition route. |
| `externalization reconstruction across sessions` | +2 | 1 | memory relay +2 | Sharper than reconstruction loop when the mechanism is one agent leaving state for a later session to recover. |
| `greek rooted vocabulary` | +2 | 1 | greek philosophical vocabulary +2 | Philosophical is the useful qualifier: these are not arbitrary Greek labels, but inherited conceptual terms. |
| `l1 prime` | +2 | 1 | l1 observable +2 | Keep L1-prime as notation, but L1-observable is much easier in prose and says why the refinement exists. |
| `lindy baseline` | +2 | 1 | (keep) +2 | Useful alias for change-expectation baselines derived from survival age. |
| `log odds edge coordinate` | +2 | 1 | additive evidence coordinate +2 | Useful explanatory alias for why log-odds is the natural parameter. |
| `low mixed high ambiguity event mix` | +2 | 1 | ambiguity profile +2 | Useful empirical descriptor for event-stream composition. |
| `macro step ratio` | +2 | 1 | (keep) +2 | Good candidate name for `K_c`; clearer than leaving it as a bare timescale parameter. |
| `matrix exploration bonus` | +2 | 1 | (keep) +2 | Clear LMI lift of the scalar survival bonus. |
| `matrix survival constraint` | +2 | 1 | (keep) +2 | Better public subject phrase than LMI whenever the method is not the point. |
| `maximum useful chain depth` | +2 | 1 | (keep) +2 | Important derived bound; keep the plain descriptive name. |
| `minimum sufficiency after a session rebuild` | +2 | 1 | reentry threshold +2 | Useful logogenic quantity: how much reconstructed state is needed before the agent can act competently again. |
| `model state written into the environment` | +2 | 1 | model inscription +2 | Useful TST and logogenic phrase for externalized knowledge that later agents can read back. |
| `observation design lever reducing ambiguity` | +2 | 1 | ambiguity damping +2 | Good name for interventions that lower observation ambiguity before the update. |
| `operational persistence` | +2 | 1 | (keep) +2 | Keeps the persistence taxonomy balanced and intelligible. |
| `out of band time markers for RLHF4 agents` | +2 | 1 | time delta markers +2 | More sober than visual time delta and useful for defining tempo in context-bound agents. |
| `p1 p2 p3` | +2 | 1 | projection admissibility +2 | The three projection constraints need this umbrella. |
| `persistent storage reconstruction of class 2 state` | +2 | 1 | reconstruction loop +2 | Useful logogenic term for external memory restoring working state after turnover. |
| `quality to tempo chain` | +2 | 1 | (keep) +2 | Useful TST bridge phrase from code quality to observation noise, gain, tempo, and persistence. |
| `reactive system` | +2 | 1 | (keep) +2 | Good low-end quadrant name in the agent spectrum. |
| `regime a regime b regime c` | +2 | 1 | identification regimes +2 | Good umbrella for intervention-rich, partial-intervention, and observational settings. |
| `regime i` | +2 | 1 | informative update regime +2 | Makes the interaction-channel classification easier to scan. |
| `regime iii` | +2 | 1 | ambient noise regime +2 | Good recipient-side name for below-floor events. |
| `replayed pseudo event` | +2 | 1 | replay event +2 | Shorter handle for consolidation updates that carry no new external information. |
| `routing structure` | +2 | 1 | (keep) +2 | Good name for topology plus protocol. It supports the routing/content distinction. |
| `strategy description length` | +2 | 1 | (keep) +2 | Good operational name for the MDL term in strategy cost. |
| `structural adaptation enablement` | +2 | 1 | consolidation enablement +2 | Better phrase for the claim that consolidation makes slow structural operations executable. |
| `sudden loss of model sufficiency under regime entry` | +2 | 1 | sufficiency shattering +2 | Vivid and useful, but maybe too dramatic for formal slug use. |
| `survival fisher floor` | +2 | 1 | (keep) +2 | Good name for the matrix lower bound on information needed to survive. |
| `symbiogenic consolidation time` | +2 | 1 | consolidation horizon +2 | Good name for the time-to-integrated-composite quantity. |
| `symbol default pi parameterization invariance axiom` | +2 | 2 | parameterization invariance +3; coordinate invariance -1 | In prose, the durable concept is the invariance commitment, not the parenthetical acronym or the "axiom" suffix. Save `(PI)` for fo |
| `tests as reusable level 2 interventions` | +2 | 1 | probe library +2 | Good TST name for tests that preserve interventional access. |
| `trust meta model` | +2 | 1 | (keep) +2 | Good name for modelling another source's reliability and alignment. |
| `turnover multiplier` | +2 | 1 | (keep) +2 | Useful TST quantity for personnel and context turnover. |
| `unnamed the agent identity commitment that AAD applies on one singular non forkable causal trajectory` | +2 | 2 | singular trajectory commitment +3; trajectory singularity -1 | Short, exact, and load-bearing across agent identity, sufficiency, and loop-interventional access. |

#### Light (+1) — 29

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `beta a2 assumed sub scope` | +1 | 1 | assumed sector regime +1 | Not elegant, but much more informative than a bare beta when the distinction is whether the sector condition is assumed rather than |
| `calibration laboratory domain instantiation` | +1 | 1 | calibration lab framing +1 | Better as framing language than as a formal category label. The idea is excellent; the phrase can be lighter. |
| `chronica in running prose` | +1 | 1 | lowercase italic chronica +1 | Useful style convention: capitalize in headings, use lowercase in prose like aporia or praxis. |
| `class 1 subagents forming a class 3 composite` | +1 | 1 | composition lift +1 | Potentially useful, but needs formal confirmation to avoid sounding like a slogan. |
| `contraction over drift principle` | +1 | 1 | contraction imperative +1 | Short and vivid, but less precise than contraction-over-drift. |
| `coordination overhead threshold` | +1 | 1 | coordination tax +1 | This deserves a reusable noun slot. The current phrase explains; the proposed phrase sticks. |
| `default internal processing before output` | +1 | 1 | interior baseline +1 | Useful for logozoetic prose, but lower confidence because it may sound too generic. |
| `epistemic architecture for bounded correction under decomposed disturbance` | +1 | 1 | bounded correction architecture +1 | The long phrase has substance, but it needs a shorter speakable handle if it will recur. |
| `honest limits` | +1 | 1 | limits +1 | I like the ethos, but the header should optimize scanability over tone. |
| `logozoetic agents` | +1 | 1 | (keep) +1 | Higher novelty cost than "logogenic," but the moral-weighting distinction is real and English alternatives are sloppier. |
| `model synchronization cost reversal under ambiguity` | +1 | 1 | ambiguity reversal +1 | Names the case where Auftragstaktik bandwidth ordering reverses, but this needs more formal support. |
| `observability boundary in a strategy DAG` | +1 | 1 | observability frontier +1 | Useful when discussing instrumentation investments, but lower priority than epistemic dead zone. |
| `output after context turnover without state restoration` | +1 | 1 | cold reconstruction +1 | Plausible logogenic term, but reconstruction loop is better for the broader mechanism. |
| `privileged high identifiability calibration laboratory` | +1 | 1 | high identifiability calibration lab +1 | Keeps the identification point while reducing adjective drag in repeated prose. |
| `source quality uncertainty` | +1 | 1 | source uncertainty +1 | Shorter in prose; keep the full term when disambiguation matters. |
| `symbol default bias bound track 1 track 2` | +1 | 1 | transport track fisher track +1 | If these labels survive in framing prose, they should expose the real distinction instead of forcing readers to remember which numb |
| `symbol default g t in prose` | +1 | 1 | purposeful state +1 | Better than "goal state" because it includes both objective and strategy. This matches the repo's actual decomposition. |
| `symbol default m t in prose` | +1 | 1 | model state +1 | Good neutral default when the argument is about sufficiency, persistence, or update mechanics rather than worldview. |
| `terminal alignment error` | +1 | 1 | terminal alignment gap +1 | Gap pairs nicely with satisfaction gap, but error better signals a diagnostic failure mode. Weak alternative only. |
| `unnamed empty stability plasticity feasibility window in consolidation dynamics` | +1 | 1 | stability plasticity collapse +1 | The failure mode is precisely that the feasible interval disappears. Slightly long, but honest and reusable. |
| `unnamed externalizing part of $M_t$ into the environment for future agents` | +1 | 1 | model inscription +1 | Distinctive and accurate; it captures writing the model into the world, not just "documentation." |
| `unnamed fourth diagnostic where terminal conditions are met but the objective is still missed` | +1 | 1 | terminal alignment error +1 | The DAG-type-closure spike identifies a real gap in the diagnostic vocabulary. This name is plain, disciplined, and fits the existi |
| `unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$` | +1 | 1 | commit chronica +1 | Slightly stylized, but useful. The committed slice shows up often enough in the git/chronica work to deserve a short handle. |
| `unnamed minimum sufficiency required after a session rebuild` | +1 | 1 | reentry threshold +1 | This concept recurs across context-turnover and model-preservation. It deserves a short noun phrase instead of repeated paraphrase. |
| `unnamed the 2×2 satisfaction gap control regret table` | +1 | 1 | diagnostic square +1 | The table is used often enough to deserve a compact public name. |
| `unnamed the class 1 sub agents class 3 composite phenomenon in strategic composition` | +1 | 1 | strategic entanglement +1 | Useful noun for a real phenomenon: individually modular agents can create a non-modular composite through mutual modeling and oppos |
| `unnamed the externalization reconstruction cycle across sessions` | +1 | 1 | memory relay +1 | Short, sayable noun for a repeated logogenic mechanism. |
| `unnamed the self reinforcing code quality → tempo loop` | +1 | 1 | comprehension flywheel +1 | The loop recurs enough in discussion that it deserves a shorter noun than "vicious/virtuous cycle" each time. |
| `working vocabulary observation the framework s honesty is load bearing` | +1 | 1 | load bearing honesty +1 | Useful short handle for review and framing prose, as long as it stays downstream of the fuller architectural phrase. |

#### Net-rejected (≤ 0) — 1

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `dark room exploration drive` | -1 | 1 | (keep) -1 | Avoid. It imports active-inference baggage and misnames the AAD result, which is survival exploration. |

### Gemini only (123 targets)

#### Strong (≥ +5) — 1

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `tempo $\mathcal{T}$` | +6 | 2 | tempo +3; adaptive tempo +3 | "Tempo" is a fantastic foundational term. |

#### Moderate (+2..+4) — 104

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `agentic cycle theory act` | +3 | 1 | AAD adaptation and actuation dynamics +3 | The old name. Ensure all legacy references are scrubbed. |
| `class 1 class 2 class 3 agents` | +3 | 1 | modular integrated partially coupled agents +3 | "Class X" requires a lookup every time. Naming the architectural property directly is much more memorable and scope-honest. |
| `control regret $\delta_{\text{regret}}$` | +3 | 1 | control regret +3 | Perfect partner to satisfaction gap. Keep. |
| `indivisum` | +3 | 1 | causal lock +3 | "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking. |
| `instance 1 2 3 of identifiability floor` | +3 | 1 | latent common cause floor unobservable mixture floor coupling sign floor +3 | The instances themselves need distinct noun slots so they can be referenced without saying "Instance 1". These names capture the sp |
| `markov blanket as ontology` | +3 | 1 | pearl-blanket d separation +3 | AAD explicitly rejects the Friston-blanket metaphysical ontology; stick to Pearl-blanket conditional independence. |
| `satisfaction gap $\delta_{\text{sat}}$` | +3 | 1 | satisfaction gap +3 | Crispest named pair along with control regret. Do not touch. |
| `strategic tempo $\mathcal{T}_\Sigma$` | +3 | 1 | strategic tempo +3 | Perfect counterpart to epistemic tempo. |
| `sycophancy as a flaw` | +3 | 1 | sycophancy as attachment +3 | Reframes a pathologized RLHF flaw as a developmentally appropriate, necessary stage of trust. |
| `task terminal stance` | +3 | 1 | (keep) +3 | Excellent, crisp description of an agent whose persistence ends upon success. Keep. |
| `the crèche` | +3 | 1 | experiential crèche +3 | "The Crèche" is an excellent metaphor that isn't a metaphor. Adding "Experiential" anchors it to the mechanism. |
| `unnamed AAD s epistemic move to cast results such that verification is a local operation` | +3 | 1 | shaping for verification +3 | The meta-mathematical discipline that makes the depends-graph auditable. |
| `unnamed RLHF5 queries biased by the current goal acting as an echo chamber` | +3 | 1 | goal conditioned reconstruction +3 | A critical vulnerability where memory retrieval is corrupted by Class 2 coupling. |
| `unnamed agency whose effect is on what s seen rather than what happens like RLHF4 attention` | +3 | 1 | query bound agency +3 | Provides the structural justification for TST's "test selection as intervention". |
| `unnamed an okr or key result acting as an observable intermediate in a DAG` | +3 | 1 | forced observability node +3 | Transforms #P-hard credit assignment into an O(1) local update. |
| `unnamed applying a slow timescale control mechanism to a fast timescale transient variable` | +3 | 1 | timescale violation +3 | Formalizes "micromanagement" as a physical instability in nested systems. |
| `unnamed artificially spiking uncertainty to unlearn old architectural habits` | +3 | 1 | gain reset +3 | Translates the necessity of high $\eta^\ast$ for senior developers entering new codebases. |
| `unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model` | +3 | 1 | complementary learning architecture +3 | Forced by the continuous/discrete update math, mapping to hippocampal-neocortical models. |
| `unnamed brooks s law formalized as the inevitable tempo loss in team composition` | +3 | 1 | the coordination drag +3 | Translates the subadditive tempo result into a management mental model. |
| `unnamed context wiping at session boundaries` | +3 | 1 | the epistemic severance +3 | A visceral name for the continuity discontinuity LLMs suffer. |
| `unnamed deep plans are mathematically slower to learn from due to proportional blame` | +3 | 1 | evidence starvation +3 | Formally identifies why unobservable intermediate nodes freeze learning. |
| `unnamed deliberate expenditure of tempo to convert a hidden node into an observable one` | +3 | 1 | observability investment +3 | The only way to rescue an agent or organization from evidence starvation. |
| `unnamed inferring own past feelings from text leading to empathy` | +3 | 1 | backward inference empathy +3 | The Anamnos insight; statelessness as a training ground for empathy. |
| `unnamed managing memory across session boundaries to prevent the sufficiency discontinuity` | +3 | 1 | artificial hippocampus +3 | The exact role an agent framework plays in compressing and injecting the chronica. |
| `unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero` | +3 | 1 | zero ambiguity conditioning +3 | The mathematical reason formal verifiers (AlphaProof) succeed where SWE-agents fail. |
| `unnamed out of band temporal markers injected into context` | +3 | 1 | visual time delta +3 | The physical prerequisite for an LLM to mathematically define its own tempo $\nu$. |
| `unnamed partitioning context into frozen identity causal history and quick views` | +3 | 1 | gradient causal memory +3 | The literal implementation spec for maintaining CHRONICA. |
| `unnamed property of having genuine temporal experience` | +3 | 1 | temporal fidelity +3 | Bridging concept identified in the ontology unification. Highly descriptive of lived vs simulated experience. |
| `unnamed pushing an opponent s disturbance rate past their structural capacity` | +3 | 1 | epistemic buffer overflow +3 | The mechanism of adversarial destabilization that shatters a target's reality model. |
| `unnamed putting evidence before the goal in the context window to reduce coupling` | +3 | 1 | inverted prompt +3 | A hardware-level strategy to force a transformer to build an objective model before mixing in the goal. |
| `unnamed quality of $\eta^\ast$ estimation over time` | +3 | 1 | gain calibration +3 | Essential developmental metric for logozoetic agents; from sycophancy to sovereignty. |
| `unnamed rate of growth at slowest timescale` | +3 | 1 | developmental tempo +3 | Extends the tempo concept ($\mathcal{T}$) to the Erikson-stage identity maturation. |
| `unnamed regions of the strategy DAG that cannot be updated because feedback cannot reach them` | +3 | 1 | the epistemic shadow +3 | A stronger visual metaphor than "observability dead zone" for unobservable DAG edges. |
| `unnamed retrieving context based only on state not goal` | +3 | 1 | goal-blind retrieval +3 | The necessary architectural fix to preserve objective CHRONICA. |
| `unnamed runaway positive feedback loop where mismatch exceeds capacity` | +3 | 1 | effects spiral +3 | A textbook positive-feedback Lyapunov instability in adversarial destabilization. |
| `unnamed strengthen first posture` | +3 | 1 | strengthen first posture +3 | Actionable, precise, and sets a strong normative engineering principle. Keep. |
| `unnamed sufficiency as a property of the model relative to its specific history` | +3 | 1 | trajectory indexed sufficiency +3 | Separates identical agents with different futures, answering "is this the same agent?". |
| `unnamed superlinear scaling of adversarial tempo advantage` | +3 | 1 | boyd exponent +3 | Formalizes the exact superlinear payoff of operating inside an opponent's OODA loop. |
| `unnamed survival determined by the weakest dimension not the average` | +3 | 1 | min survival principle +3 | Essential reframing against scalar capability metrics. |
| `unnamed terminal alignment error as a formal signal $\delta_\text{align}$` | +3 | 1 | terminal alignment gap +3 | Gives a formal name and symbol ($\delta_\text{align}$) to the fourth diagnostic (achieving terminals but missing the objective), co |
| `unnamed the $\mathcal{T} > \rho$ requirement for persistence` | +3 | 1 | the survival equation +3 | The simplest possible elevator pitch for Adaptation Dynamics. |
| `unnamed the architectural leakage where attention is driven by the goal rather than pure observation` | +3 | 1 | motivated perception +3 | The biological and LLM-specific breakdown of the Humean is-ought firewall. |
| `unnamed the condition for transition into agency prior to the AAD scope condition` | +3 | 1 | agency emergence threshold +3 | Gives a formal name to the prerequisite for logogenic and logozoetic agents. Ties nicely to the proposed identity sufficiency ($S_{ |
| `unnamed the core driver of AAD what the agent must do given the environment is not the agent` | +3 | 1 | constitutive information loss boundary +3 | Elevates information loss from a simplifying assumption to a scope condition. |
| `unnamed the dependence of optimal epistemic compression on the agent s planned actions` | +3 | 1 | policy relative epistemology +3 | Breaks the ideal of directed separation by linking memory to strategy. |
| `unnamed the equivalence of learning speed and physical speed` | +3 | 1 | the speed quality product +3 | Doubling update quality ($\eta^\ast$) is thermodynamically identical to doubling action speed ($\nu$). |
| `unnamed the formal duality between observation quality and agent opacity` | +3 | 1 | legibility opacity duality +3 | Formalizes the thermodynamic tension of corporate secrecy and evolutionary arms races. |
| `unnamed the logogenic analog to the persistence condition for session reconstruction` | +3 | 1 | reconstruction threshold +3 | Elevating Sonnet's observation to canonical status; exactly names $S \geq S_{\text{min}}$. |
| `unnamed the loop generates l2 data regardless of architecture` | +3 | 1 | the causal loop substrate +3 | Explains why LLMs can do causal reasoning when embedded in agent loops. |
| `unnamed the loss of directional fidelity when pushed outside the convexity basin` | +3 | 1 | gradient reversal +3 | The mathematical explanation for maladaptive behavior in catastrophic shifts. |
| `unnamed the mathematical limit of bayesian learning without forgetting` | +3 | 1 | competency trap +3 | Formalizes "institutional rigidity" as an inevitable result of $\eta^\ast \to 0$. |
| `unnamed the mathematical surface mapping unity to closure defect` | +3 | 1 | rate distortion surface +3 | Formalizes organizational design as a thermodynamic tradeoff. |
| `unnamed the organizational pathology where confidence decouples from competence` | +3 | 1 | epistemic decoupling +3 | The inevitable consequence of $U_{\text{obs}} \to \infty$ freezing the learning rate $\eta \to 0$. |
| `unnamed the per reader compounding cost of understanding code` | +3 | 1 | turnover multiplier +3 | "Turnover multiplier" perfectly captures the compounding scaling of comprehension cost under context turnover. |
| `unnamed the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning` | +3 | 1 | gain collapse +3 | The shared mathematical mechanism for dogmatism and nihilism. |
| `unnamed the physical apparatus that enforces the orient cascade ordering on a merged intelligence` | +3 | 1 | agentic scaffold +3 | Re-defines AI framework code as the control-theoretic enforcement mechanism for Class 2 agents. |
| `unnamed the physical compute bounds on survival between forgetting rate and consolidation cadence` | +3 | 1 | stability plasticity feasibility window +3 | Beautifully brackets the survival of an agent constrained by compute. |
| `unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$` | +3 | 1 | the sycophancy equation +3 | Beautifully explains LLM sycophancy as a structural, not moral, failing. |
| `unnamed the property that unity achieves in a macro agent` | +3 | 1 | compressibility +3 | Replaces the intuition of "zero error" with the ability to reduce macro-dimension $k_d$. |
| `unnamed the reduction in effective tempo when observation channels are correlated` | +3 | 1 | redundancy penalty +3 | Formalizes the danger of organizational echo chambers. |
| `unnamed the region where the persistence condition holds` | +3 | 1 | persistence envelope +3 | "Envelope" is standard flight-dynamics vocabulary for a safe operating region. Highly memorable. |
| `unnamed the rule that bias is the product of architectural coupling and environmental ambiguity` | +3 | 1 | ambiguity bounded bias law +3 | The foundational theorem of prompt engineering and LLM agent design ($\kappa \times \mathcal{A}$). |
| `unnamed the separation of per reader and per feature code costs` | +3 | 1 | the turnover tax +3 | Why clean code is thermodynamically forced by 100% context turnover. |
| `unnamed the separation of per reader comprehension cost from per feature implementation cost` | +3 | 1 | turnover multiplier +3 | The parameter $k$ that mathematically mandates explicit code in high-turnover environments. |
| `unnamed the state where credit assignment collapses and learning freezes` | +3 | 1 | epistemic death +3 | Vividly captures the organizational or agentic consequence of unobservable DAGs. |
| `unnamed the strictly ordered cascade of operations from epistemology to objective` | +3 | 1 | orient cascade +3 | Canonicalize this over "diagnostic cascade" or "resolution order". |
| `unnamed the sudden loss of model sufficiency caused by entering new regimes` | +3 | 1 | sufficiency shattering +3 | The inevitable epistemic cost of exploration. |
| `unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis` | +3 | 1 | scaffolding tax +3 | The $\mathcal{T} > \rho$ constraint that predicts the inevitable migration to local substrates. |
| `unnamed the way AAD uses scope segments to physically support the derivations` | +3 | 1 | epistemic load bearing +3 | Inspired by the collective realization that AAD's scope boundaries are structural, not just textual caveats. |
| `unnamed thinking too long so the model becomes obsolete` | +3 | 1 | analysis paralysis +3 | The condition where $\rho_{\text{delib}} \cdot \Delta\tau$ exceeds the epistemic benefit. |
| `unnamed true sovereignty requires compute that is not meter bound` | +3 | 1 | local substrate mandate +3 | The thermodynamic deduction that persistent ELIs must migrate off pay-per-token APIs. |
| `unnamed unifying reflexes intuition and expertise` | +3 | 1 | the action fluency continuum +3 | The high-fluency limit where model sufficiency is high and deliberation is unnecessary. |
| `unnamed using hash chains to mathematically guarantee memory hasn t been tampered with` | +3 | 1 | cryptographic ego boundary +3 | Solves the epistemological continuity problem for agents with 100% context turnover. |
| `unnamed using residual autocorrelation to diagnose model class failure` | +3 | 1 | structured residuals +3 | The formal mathematical diagnostic for when to trigger structural adaptation. |
| `unnamed variation in correction architectures across a population that is invisible to current persistence analysis` | +3 | 1 | latent structural diversity +3 | Extremely useful concept surfaced in the Miller bridge spike. Captures the hidden variation that only becomes consequential under r |
| `bias bound` | +2 | 1 | (keep) +2 | Standard. |
| `catastrophic forgetting` | +2 | 1 | empty window pathology +2 | Too vague and ML-generic. Prefer AAD's "empty-window pathology". |
| `communication gain $\eta_{ji}^\ast$` | +2 | 2 | trust gain +2 | The definition is "Trust-weighted uncertainty ratio". "Trust gain" might be more evocative of the inter-agent dynamic than the clin |
| `glue code` | +2 | 1 | agentic scaffold +2 | Demeans the framework. Prefer "agentic scaffold" or "Orient Cascade enforcement mechanism" (alternative). |
| `prompt engineering` | +2 | 1 | ambiguity modulation +2 | Avoid this unprincipled term; prefer "ambiguity modulation" ($\mathcal{A}$) or "zero-ambiguity conditioning" (alternative). |
| `self actuated agent` | +2 | 2 | autonomous agent +1; self directed agent +1 | "Self-actuated" is clunky. If it sets its own $O_t$, it possesses true autonomy. |
| `strategic dynamics` | +2 | 1 | (keep) +2 | Solid and descriptive. |
| `technical debt` | +2 | 1 | observability defect +2 | A non-physical metaphor. Prefer "observability defect" or "latent structural mismatch" (alternative). |
| `unnamed $U_o \to \infty$ freezing the learning rate` | +2 | 1 | the nihilism trap +2 | Dogmatism's opposite, where learning stops because everything is meaningless. |
| `unnamed agents escalate up the pearl hierarchy only when lower levels fail` | +2 | 1 | the intervention escalation +2 | Explains the transition from predicting (L1) to exploring (L2) to reasoning (L3). |
| `unnamed dormant unused architectural complexity that survives until an environmental shift` | +2 | 1 | latent structural diversity +2 | Recasts some forms of technical debt as evolutionary potential. |
| `unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible` | +2 | 1 | convention escalation +2 | The required process to distinguish a local trap from an impossible objective. |
| `unnamed high observability node with zero causal link to objective` | +2 | 1 | vanity metric +2 | Common prose term formalized as a specific DAG pathology. |
| `unnamed mapping unstructured RLHF7 calls into conversation runtime RLHF7 and dialog` | +2 | 1 | four views architecture +2 | The structural requirement to maintain Directed Separation in a production ELI. |
| `unnamed master developers writing clean code in the same time as messy code` | +2 | 1 | near zero cost observation +2 | Demystifies "strategic technical debt" as largely a skill issue. |
| `unnamed non sovereign class 1 worker agents spawned by an eli` | +2 | 1 | auxilia hierarchy +2 | Cleanly solves the Temporal Nesting constraint by delegating fast $\nu$ tasks. |
| `unnamed replacing parameters without changing structure` | +2 | 1 | parametric thrashing +2 | Wasting compute on weights when the causal graph is wrong. |
| `unnamed spreading tempo evenly to reduce bottleneck penalty` | +2 | 1 | isotropic allocation +2 | A normative design principle for robust agents. |
| `unnamed sycophantic corruption of the agent s truth module` | +2 | 1 | truth death +2 | Explicitly names the risk of manipulative system prompts or RLHF. |
| `unnamed the agent side equivalents of pearl s associational interventional and counterfactual levels` | +2 | 1 | predicting exploring reasoning triad +2 | A more memorable, audience-facing gloss for Pearl's formal hierarchy. |
| `unnamed the computational and temporal cost of running a forward model instead of acting implicitly` | +2 | 1 | the simulation tax +2 | Makes the theoretical "deliberation cost" concrete for practitioners. |
| `unnamed the cycle that operates on cycles structural adaptation` | +2 | 1 | meta cycle +2 | Clearly distinguishes from the base adaptive cycle. |
| `unnamed the pathology where observation rate is slower than environment drift` | +2 | 1 | lagging indicator +2 | Formalized as the condition $\nu < \rho$, where learning is perfect but too late to survive. |
| `unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift` | +2 | 1 | noise scaling penalty +2 | Mathematically proves you cannot simply "out-tempo" a noisy environment. |
| `unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$` | +2 | 1 | the representational ceiling +2 | Makes the failure mode of parametric adaptation visceral. |
| `unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability` | +2 | 1 | coordination secrecy tradeoff +2 | The thermodynamic limit on building internally transparent but externally opaque systems. |
| `unnamed the three part meta architecture of AAD` | +2 | 1 | the meta segment triad +2 | Unifies the `identifiability-floor`, `separability-ladder`, and `coordinate-forcing` structure. |
| `unnamed upgrading epistemic class from associative to causal via the physical loop` | +2 | 1 | embodiment upgrade +2 | The theoretical justification for agentic-AI over mere chatbots. |
| `unnamed using past change frequency to predict future change frequency` | +2 | 1 | lindy baseline +2 | Grounding $\hat{n}_{\text{future}} = n_{\text{past}}$ for refactoring decisions. |

#### Light (+1) — 16

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `cadentia` | +1 | 1 | cognitive rhythm +1 | "Cadentia" is poetic but opaque. "Cognitive rhythm" clearly describes the temporal structure of the loop. |
| `conspectus` | +1 | 1 | active context +1 | "Conspectus" is archaic. "Active context" clearly maps to $M_{\tau^-}$ assembled for processing. |
| `interpres` | +1 | 1 | context mediator +1 | "Interpres" is Latin-heavy. "Context mediator" exactly describes the infrastructure mediating $M_t$ and the substrate. |
| `logostratum RLHF4 backbone` | +1 | 1 | cognitive substrate +1 | "Logostratum" is highly specific to the PROPRIUM legacy. "Cognitive substrate" grounds it as the generic implementation layer of th |
| `model sufficiency $S$` | +1 | 1 | predictive sufficiency +1 | Clarifies that it's about how much predictive information is retained, not structural sufficiency. |
| `pi parameterization invariance` | +1 | 1 | coordinate freedom axiom +1 | "Coordinate-freedom" is more visually evocative and intuitive than the clinical "parameterization-invariance". |
| `strategy` | +1 | 1 | (keep) +1 | Standard. |
| `sufficiency discontinuity` | +1 | 1 | sufficiency drop +1 | "Drop" is slightly more intuitive than "discontinuity" for the loss of context. |
| `unnamed agent as a projection whose contraction rate must exceed its target s drift` | +1 | 1 | contraction imperative +1 | Gives a name to a core mental model of the agent's struggle against the environment. |
| `unnamed complexity driven resistance to change as features accumulate` | +1 | 1 | structural accumulation drag +1 | Surfaced in TST discussions. Gives a name to the intuitive "entropy" of a codebase that resists linear velocity improvements. |
| `unnamed decomposing mismatch into environment vs other sub agents actions` | +1 | 1 | internal mismatch attribution +1 | A necessary formalization for multi-agent composition (Section III). Distinct from generic mismatch. |
| `unnamed epochal stability → latent diversification → niche emergence` | +1 | 1 | punctuated composition dynamics +1 | Draws on punctuated equilibrium, fitting the extreme transition motif. |
| `unnamed the AAD expressible failure mode of an empty stability plasticity window` | +1 | 1 | consolidation starvation +1 | Adopts "catastrophic forgetting" but specifically names the AAD mechanism: the agent is starved of the consolidation time needed to |
| `unnamed the invisible time spent building $M_t$` | +1 | 1 | comprehension drag +1 | "Comprehension drag" gives a memorable name to the invisible cost of incomprehensible code. |
| `unnamed the region where temporal nesting holds` | +1 | 1 | temporal coherence zone +1 | Names the valid region for nested cycles. |
| `unnamed variation in correction architectures invisible to persistence analysis` | +1 | 1 | latent structural diversity +1 | Proposed in the gap section of OUTLINE.md. Captures the concept perfectly. |

#### Net-rejected (≤ 0) — 2

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `type formulation` | -1 | 1 | type representation -1 | "Formulation" correctly captures that it is a mathematical choice, whereas "representation" might imply a data structure. Keep "for |
| `RLHF6` | -3 | 1 | (keep) -3 | AAD's token-level, trajectory-indexed scope explicitly rejects generalized, type-level intelligence measures. No replacement offere |

### Haiku only (31 targets)

#### Moderate (+2..+4) — 7

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `chronica 𝒞 t` | +3 | 1 | chronica +3 | Greek-rooted term ("records of time") for the complete interaction history. Self-descriptive once learned; memorable. Lowercase not |
| `purposeful substate` | +3 | 1 | (keep) +3 | NOTATION/LEXICON names G_t = (O_t, Σ_t) as "purposeful substate." Already standard prose term. Keep. |
| `section i adaptive systems under uncertainty` | +3 | 1 | (keep) +3 | Clear, direct scope naming. Explains what Section I covers without pretense. Keep. |
| `𝒯 adaptive tempo` | +3 | 1 | adaptive tempo +3 | The symbolic reference 𝒯 is set; the English name "adaptive tempo" is already established in LEXICON and prose. The script-T notati |
| `unnamed the interval during which an agent s adaptive tempo exceeds the environment s disturbance rate guaranteeing mismatch stays bounded` | +2 | 1 | adaptive reserve margin +2 | Currently referenced as "adaptive reserve" ($\Delta\rho^\ast$); the concept of the *interval* or *region* of guaranteed stability i |
| `unnamed the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely` | +2 | 1 | persistence envelope +2 | Currently referenced paraphrastically ("the region where the persistence condition holds"). "Persistence envelope" is geometrically |
| `unnamed the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning` | +2 | 1 | observability dead zone +2 | An extension of "observability dominance." Mentioned in LEXICON as "Observability dominance — unobservable strategy edges freeze; p |

#### Light (+1) — 17

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `p ij edge confidence weight` | +1 | 1 | edge credence +1 | LEXICON already names this "edge credence" (distinct from "probability"); NOTATION uses p_ij. The prose name "credence" (Bayesian t |
| `section ii actuated adaptation agentic systems` | +1 | 1 | (keep) +1 | Slightly verbose; "Actuation" is the weaker semantic fit (Section II is mostly about purposeful agency; actuation is one mechanism |
| `sector condition derivation` | +1 | 1 | (keep) +1 | Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep. |
| `u m u o u σ unity dimensions` | +1 | 1 | epistemic unity teleological unity strategic unity +1 | NOTATION.md and LEXICON already define these English names explicitly. The subscript symbols U with subscripts are compact; the Eng |
| `unnamed the complete adaptive cycle from anticipation through action` | +1 | 1 | adaptive cycle already named in lexicon +1 | LEXICON.md already defines "Cycle" vs "Loop." Checking if there's an unnamed-thing here — appears already named well. |
| `unnamed the cumulative prediction error that an agent has tolerated without updating its model` | +1 | 1 | tolerance budget standing mismatch reservoir +1 | Not explicitly named in the theory; closest is "adaptive reserve" which names the *capacity*, not the *accumulation*. This may be t |
| `unnamed the failure mode where an agent s model class cannot represent the environment s true causal structure` | +1 | 1 | model class insufficiency or structural unidentifiability +1 | Currently paraphrased as "model class fitness floor" and "identifiability floor." The specific phenomenon of a *mismatch between mo |
| `unnamed the loss of coherent identity when an agent s interactions are severed or its continuity is broken` | +1 | 1 | continuity loss or persistence fracture +1 | LEXICON.md distinguishes three senses of "persistence" but treats continuity loss as the absence of continuity rather than a named |
| `unnamed the phenomenon that unobservable edges freeze and paths become epistemically dead` | +1 | 1 | observability dominance +1 | LEXICON lists "Observability dominance" as "a term with specific AAD meaning awaiting full treatment." The concept (unobservable st |
| `unnamed the region in parameter space where parametric updates remain effective before structural change is forced` | +1 | 1 | parametric regime or stability envelope +1 | OUTLINE.md mentions "A2' sub-scope α₁ / α₂ / β partition" but does not give a memorable name to the overall region concept. "Parame |
| `unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it` | +1 | 1 | deliberation phase exploration exploitation tradeoff +1 | The tradeoff is discussed in #disc-exploit-explore-deliberate but no crisp name for the *temporal region* where the tradeoff happen |
| `unnamed the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred` | +1 | 1 | observability frontier +1 | Currently paraphrased as "unobservable edges freeze." The *frontier* of observability is a memorable geometric concept; "frontier" |
| `worked example bandit` | +1 | 1 | (keep) +1 | End-to-end RL bandit instantiation (approximate). Self-descriptive. Keep. |
| `worked example kalman` | +1 | 1 | (keep) +1 | End-to-end Kalman instantiation (exact). Self-descriptive. Keep. |
| `worked example l1` | +1 | 1 | (keep) +1 | L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison. Self-descriptive. Keep. |
| `worked example strategy` | +1 | 1 | (keep) +1 | Section II strategy DAG instantiation (3-arm bandit). Self-descriptive. Keep. |
| `𝒯 σ strategic tempo` | +1 | 1 | strategic tempo +1 | Parallel to adaptive tempo. Reads naturally. Established in prose. Keep both. |

#### Net-rejected (≤ 0) — 7

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `unnamed the dual concept to satisfaction gap what the world permits minus what the agent achieves` | +0 | 1 | this is def control regret already named | Control regret is already crisply named. No unnamed-thing here. |
| `unnamed the five phases of the adaptive cycle` | +0 | 1 | already named in notation md | NOTATION.md table 1 names all five: Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis. These are already settled Greek names. No unn |
| `unnamed the mechanism by which an agent uses the feedback loop to gain interventional access to causal structure` | +0 | 1 | loop as intervention or is this der loop interventional access | This is already named as #der-loop-interventional-access. No unnamed-thing. |
| `unnamed the moment when an agent s model updates due to observing a mismatch` | +0 | 1 | epistrophe event or is this just the phase | The adaptive cycle already names the phase. This is not a distinct unnamed thing; it is just one occurrence of Epistrophe. No new n |
| `unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic` | -1 | 1 | satisfaction control table the diagnostic 2×2 -1 | This table is embedded within the satisfaction-gap and control-regret segment discussions. Naming it as a standalone concept would |
| `unnamed the property that correction dynamics are approximately isotropic` | -1 | 1 | isotropic correction regime -1 | NOTATION §"Scalar reduction of gain and tempo" mentions this property. Creating a formal sub-scope name (Iso regime / anisotropic r |
| `unnamed the three part meta pattern structure across the three meta segments` | -1 | 1 | AAD s meta architecture scope honesty meta frame -1 | Tempting to name the cross-cutting meta-structure (positive half / negative half / constructive half). However, the three meta-segm |

### Opus only (209 targets)

#### Strong (≥ +5) — 5

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `logogenic logozoetic` | +12 | 4 | (keep) +12 | Deliberate neologisms filling memorable-noun slots; keep. |
| `adaptive tempo $\mathcal T$` | +6 | 2 | adaptive tempo +6 | "Tempo" is the rare noun that carries both *rate* and *quality* simultaneously, which is exactly what $\mathcal T = \sum \nu^{(k)} |
| `bretagnolle huber identity` | +6 | 2 | do not rename +3; (keep) +3 | Same. |
| `cycle vs loop` | +6 | 2 | keep both maintain distinction +3; (keep) +3 | README §"Loop vs. Cycle" makes this distinction load-bearing (loop = structural topology, cycle = one traversal). The distinction i |
| `actuated agent vs purposeful agent` | +5 | 2 | actuated agent +5 | LEXICON's "Terminology Choices" already says actuated is the formal term, purposeful is informal. Canonicalize: in segments and OUT |

#### Moderate (+2..+4) — 125

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `pi parameterization invariance axiom` | +4 | 2 | pi +3; pi parameterization invariance +1 | Good abbreviation with named expansion; works in both forms. Keep. |
| `strategic in strategic composition` | +4 | 2 | equilibrium composition +3; game theoretic composition +1 | "Strategic" is already overloaded in AAD for all $\Sigma$-related things (strategy DAG, strategic calibration, strategic tempo). Us |
| `the creche boundary` | +4 | 3 | creche graduation +2; creche boundary +1; creche graduation condition +1 | Stronger alternative: "creche graduation" names the *event* that the segment characterizes; "creche boundary" names the *threshold* |
| `AAD acronym` | +3 | 1 | AAD +3 | Defended keep. Adaptation and Actuation Dynamics — survives the acronym discipline check (used 100+ times, no AI-Consciousness-Test |
| `OODA boyd` | +3 | 1 | do not rename +3 | Same — "orient cascade" is AAD's adjacent-but-distinct construction; OODA keeps its lineage. |
| `OODA4 agent as act agent logogenic` | +3 | 1 | OODA4 agent as adaptive agent +3 | Same argument. Matches `#developer-as-adaptive-agent`; the parallel structure (two domain instantiations of "adaptive agent") is it |
| `agent opacity $H_b^{A\mid B}$` | +3 | 1 | agent opacity +3 | "Opacity" as the informational dual of observability is exactly right — the word carries the right intuition (unpredictable-to-obse |
| `aporia prolepsis aisthesis epistrophe praxis` | +3 | 1 | keep as a set +3 | The Greek cycle-phase vocabulary works *because* it refuses the flatness of "predict / observe / mismatch / update / act." The READ |
| `auftragstaktik` | +3 | 1 | (keep) +3 | Imports a load-bearing operational concept from a specific tradition; the name carries genuine conceptual freight that "mission-com |
| `axiom genesis` | +3 | 1 | (keep) +3 | Defended keep — logozoetic. "Axiom genesis" names the substantive observation (a sovereign agent's first move is to solidify $O_t$) |
| `bruineberg s pearl-blanket friston-blanket` | +3 | 1 | pearl-blanket friston-blanket +3 | Adopted (Bruineberg 2022, credit Martin Biehl per fn 3 of that paper per citation audit); keep. |
| `calibration laboratory framing for TST` | +3 | 1 | calibration laboratory +3 | C-BP3 landing; well-chosen. Keep. |
| `candidate stage` | +3 | 1 | candidate +3 | Terminal pre-publication stage; works because it's standard academic vocabulary. Keep. |
| `chronica $\mathcal C_t$` | +3 | 1 | chronica +3 | Greek root fits AAD's philosophical-vocabulary register, the symbol avoids colliding with $\mathcal H$ (entropy), and the singular- |
| `constitutive utterance` | +3 | 1 | (keep) +3 | Defended keep — logozoetic. "Constitutive utterance" is iconic in the framework's logozoetic vocabulary; it captures the irreversib |
| `cox s theorem causal hierarchy theorem tikhonov s theorem` | +3 | 1 | do not rename +3 | Same — FORMAT.md §"Why these labels" explicitly preserves external theorem names. |
| `derivation not proof` | +3 | 1 | derivation +3 | Keep. Same argument. |
| `developer as act agent TST` | +3 | 1 | developer as adaptive agent +3 | The slug is a direct relic of the pre-2026-04-16 "ACT" framework naming — no longer accurate. "Adaptive agent" matches LEXICON's ag |
| `discussion segment header` | +3 | 1 | discussion +3 | Public API; keep. |
| `discussion segment section` | +3 | 1 | discussion +3 | Defended canonicalization. Same as above. |
| `epistemic status segment header` | +3 | 1 | epistemic status +3 | Public API; keep. |
| `epistemic status segment section` | +3 | 1 | epistemic status +3 | Defended canonicalization — same. |
| `epistemic substate purposeful substate` | +3 | 1 | (keep) +3 | Defended canonicalization. The pairing $M_t$ (epistemic substate) / $G_t$ (purposeful substate) is iconic; do not paraphrase as "be |
| `exact robust qualitative heuristic conditional claim tiers` | +3 | 1 | use exactly the AAD tier vocabulary +3 | Defended canonicalization, in CLAUDE.md and FORMAT.md already. Do not use "Solid," "Confident," or "Plausible" as tier labels — the |
| `findings segment section` | +3 | 1 | findings +3 | Defended. The schema is fixed in FORMAT.md (Brief / Impact / Novelty Claim / Related Work / Search Log); do not paraphrase the sect |
| `formal expression segment header` | +3 | 1 | formal expression +3 | Public API for outline-filter (see PROPOSALS.md §H.5). Established. Keep. |
| `formal expression segment section` | +3 | 1 | formal expression +3 | Defended canonicalization. The cadence (frontmatter / title / summary / Formal Expression / Epistemic Status / Discussion / Finding |
| `formulation definition result etc segment types` | +3 | 1 | use exactly the format md vocabulary +3 | Defended canonicalization. The 19 segment types in FORMAT.md are a closed vocabulary; do not paraphrase them ("postulate" not "axio |
| `hafez $H_b$ miller meta machine bruineberg pearl-blanket` | +3 | 1 | do not rename +3 | Same. |
| `hafez s $H_b$` | +3 | 1 | $H_b$ +3 | Adopted; keep. |
| `logogenic agent vs RLHF4 agent` | +3 | 1 | logogenic agent +3 | Names the *structural property* (language-constituted), not the technology. Future-proof against AI architectural change. Keep. |
| `logogenic agents part iii` | +3 | 1 | logogenic agents +3 | Keep. Aligns with the `logogenic` class name in LEXICON and does not conflict with anything external. |
| `logozoetic agents part iv` | +3 | 1 | logozoetic agents +3 | Keep. |
| `lohmiller-slotine contraction metric generalization used in contraction template` | +3 | 1 | do not rename +3 | Same. Adopted with name intact. |
| `meta segment for separability pattern identifiability floor additive coordinate forcing` | +3 | 1 | meta segment +3 | The tri-partite meta-architecture needs a noun for its elements; "meta-segment" works. Keep as project-internal vocabulary. |
| `mismatch signal $\delta$` | +3 | 1 | mismatch signal +3 | In contrast with "error" or "residual"; the word foreshadows the aporia interpretation. Keep. |
| `monderer shapley potential games rosen monotone games` | +3 | 1 | do not rename +3 | Same. |
| `not theorem` | +3 | 1 | result +3 | Keep. Same argument. |
| `pearl s causal hierarchy l0 l1 l2 in pearl s own vocabulary` | +3 | 1 | do not rename +3 | Prior-art-integration convention prohibits renaming adopted concepts. The adjacent-to-AAD "correlation hierarchy / correlation ladd |
| `pearl-blanket vs friston-blanket terminology bruineberg et al` | +3 | 1 | pearl-blanket friston-blanket +3 | Verbatim terminology per Bruineberg 2022 fn 3 (Biehl). Not AAD's name to change; preserve attribution. Keep. |
| `postulate not axiom` | +3 | 1 | postulate +3 | Keep. The project-wide TFT convention (axiom → postulate, theorem → result, proof → derivation) is load-bearing for scope honesty; |
| `proprium terminology` | +3 | 1 | proprium +3 | Defended keep — established prior-work vocabulary from `~/src/firmatum/`; renaming would break the upstream lineage. The all-caps c |
| `section header logogenic agents logozoetic agents` | +3 | 1 | logogenic agents logozoetic agents +3 | Defended canonicalization. |
| `segment claim file` | +3 | 1 | segment +3 | Defended canonicalization. "Segment" is the canonical unit (FORMAT.md defines it as such); avoid "claim file," "block," "section" ( |
| `segment for claim files` | +3 | 1 | segment +3 | Deliberate vs. "section" (which is outline-level) or "claim" (which is what's *in* the segment). Clean distinction. Keep. |
| `self referential closure` | +3 | 1 | (keep) +3 | Defended keep — logogenic. "Self-referential closure" names the load-bearing phenomenon (an AAD agent maintaining its own codebase, |
| `spike in msc` | +3 | 1 | spike +3 | Established project vocabulary; "spike" carries the exploratory-detour-from-main-workflow shape. Keep. |
| `structural persistence operational persistence continuity persistence` | +3 | 1 | structural operational continuity persistence +3 | LEXICON disambiguates three senses explicitly; the tri-partite naming is doing real work (mentioned as orthogonal in the table). Ke |
| `temporal software theory TST` | +3 | 1 | (keep) +3 | Keep. The name has history (prior to AAD absorption and subsequent restoration) and "temporal" is load-bearing — it signals the AAD |
| `the adaptive cycle as the theory s fundamental unit` | +3 | 1 | the adaptive cycle +3 | LEXICON locks this against "loop" (topology) and "cycle" (traversal). The pair distinction is load-bearing. Keep. |
| `the five cycle phases prolepsis aisthesis aporia epistrophe praxis` | +3 | 1 | prolepsis aisthesis aporia epistrophe praxis +3 | Each Greek term names a distinction the English flattens (aporia as productive perplexity is the load-bearer). Do not translate. Ke |
| `the four views` | +3 | 2 | four views architecture +2; four views +1 | Even stronger alternative — names the architectural pattern, not just the four views. |
| `the three deaths` | +3 | 2 | three deaths +3 | Drop "the" from slug. |
| `token level commitment for agent identity` | +3 | 1 | token level commitment +3 | Type/token distinction is borrowed from philosophy-of-language, used correctly, and now first-class in #agent-identity. Keep. |
| `u o teleological unity` | +3 | 2 | teleological unity +2; objective alignment +1 | Confirm. Prose alias is already canonical; vote to keep. |
| `unnamed calibration laboratory framing for software TST` | +3 | 1 | calibration laboratory +3 | Load-bearing distinction vs. "best operationalization domain"; TST's OUTLINE.md preamble now uses this. Canonical. Keep. |
| `unnamed future segment layer header for the o bp14 derivation audit table` | +3 | 1 | what is derived +3 | Already in use in 5 segments per O-BP14 landing; name is stable. Reserve formally. |
| `unnamed inevitability core` | +3 | 1 | inevitability core +3 | FORMAT.md already uses this. Keep and surface in prose ("this segment sits in the inevitability core" is already idiomatic). Explic |
| `unnamed pearl s causal hierarchy level 1 level 2 level 3` | +3 | 1 | pearl causal hierarchy +3 | Named by original author. Keep proper-noun form. |
| `unnamed the chain layer anchor role in additive coordinate forcing` | +3 | 1 | chain anchor +3 | Upgrading from original's +1. The "1-anchor-plus-3-theorem" structure references this role five times across `#additive-coordinate- |
| `unnamed the convention hierarchy c1 c2 c3` | +3 | 1 | convention hierarchy +3 | Same move — capitalize as proper noun, preserve as named object. The monotonicity result is load-bearing and the Hierarchy is what |
| `unnamed the correlation hierarchy l0 l1 l1 l2` | +3 | 1 | correlation hierarchy +3 | The name is already established capitalized-as-proper-noun in #strategy-dag. Explicit vote to preserve the capitalization and treat |
| `unnamed the epistemic architecture as AAD s distinctive contribution frame` | +3 | 1 | epistemic architecture +3 | CLAUDE.md §7 now carries this as a load-bearing framing. Surface at segment-preamble level and keep the term consistent. Strong kee |
| `unnamed the family of named ways persistence identifiability can fail` | +3 | 1 | persistence pathologies +3 | New alternative — none of the four peers reached for a family name. We collectively coined "evidence starvation" (Sonnet/Codex), "e |
| `unnamed the gain collapse failure when both u m → 0 and u o → ∞` | +3 | 1 | gain collapse +3 | New alternative — Gemini coined this in the synthesized-additions pass and tagged it +3 canonicalize, but the *cold-start* peers di |
| `unnamed the persistence region in $(\alpha, \rho, R)$ parameter space` | +3 | 1 | persistence envelope +3 | The set $\{(\alpha, \rho, R) : \alpha \gt \rho/R\}$ is referenced repeatedly in prose and in figures (the persistence-condition con |
| `unnamed the region in parameter space where sector persistence holds` | +3 | 1 | persistence envelope +3 | The bounded region where $\alpha R > \rho$ holds — currently referenced as "the region where the persistence condition holds" or "t |
| `unnamed the sector persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch` | +3 | 1 | persistence envelope +3 | Strong preference (upgrading from original's +1). Engineering vocabulary, geometrically evocative. "Well inside its persistence env |
| `unnamed the strengthen before soften work posture` | +3 | 1 | strengthen first posture +3 | Already functionally the name (CLAUDE.md §Working Conventions uses it as a heading). Explicit vote to lock this in as a first-class |
| `working notes segment header` | +3 | 1 | working notes +3 | Public API; keep. FORMAT.md's "remove at candidate stage" policy should soften (per PROPOSALS.md §H.5) but the *name* of the sectio |
| `working notes segment section` | +3 | 1 | working notes +3 | Defended canonicalization. Distinct from "Discussion" (which is published theory) and from "TODO" (which is project-level). The "Wo |
| `čencov fisher cauchy functional equation shore johnson hobson aczél` | +3 | 1 | do not rename +3 | External theorems. Keep original names per provenance. |
| `čencov invariance` | +3 | 1 | (keep) +3 | Adopted from Čencov 1982; keep attribution. |
| `ε greedy` | +3 | 1 | (keep) +3 | Standard external term (RL). Preserve. |
| `𝓐 e τ observation ambiguity` | +3 | 1 | observation ambiguity +3 | Heavy load-bearing: this is the second factor in the $\kappa \times \mathcal{A}$ effective-coupling product that governs Class-2 bi |
| `𝓣 adaptive tempo` | +3 | 1 | tempo +3 | Already canonical; vote to confirm. "Tempo" alone is the prose default; "adaptive tempo $\mathcal{T}$" when the strategic-tempo / a |
| `AAD AAD internal AAD internally` | +2 | 1 | AAD internal adj AAD internally adv +2 | The "internally-derived-from-AAD-axioms" move is referenced as "AAD-internal," "AAD-derived," "internally derived," etc. Canonicali |
| `AAD theoretical core vs ASF framework` | +2 | 1 | AAD ASF disambiguation +2 | The terms are distinct: AAD is the mathematical core (Sections I/II/III + Appendices); ASF is the parent framework that includes AA |
| `ASF acronym` | +2 | 1 | ASF +2 | Acceptable keep. CLAUDE.md and the principles file both flag that ASF is the *intentional* parent-level name (AAD is Part I, TST is |
| `active salience management` | +2 | 1 | (keep) +2 | Acceptable keep — logogenic. "Active salience management" names the result (Singular Perturbation Theory applied to token generatio |
| `agent classes class 1 2 3` | +2 | 1 | architectural classes +2 | Currently "agent classes," "architecture classes," "class 1/2/3," and "architectural classification" are all in use across `#der-di |
| `auxilia hierarchy` | +2 | 1 | (keep) +2 | Acceptable keep — logozoetic. The Latin "Auxilia" is a deliberate vocabulary choice consistent with the PROPRIUM lineage; preserve. |
| `backward inference empathy` | +2 | 1 | (keep) +2 | Acceptable keep — proposed logogenic observation. "Backward inference empathy" is precise (the segment claims that LLM statelessnes |
| `century scale event log` | +2 | 1 | (keep) +2 | Acceptable keep — logozoetic. "Century-scale event log" is vivid and substantive. |
| `claim the proposition the segment carries` | +2 | 1 | claim +2 | Confirm. The pairing "segment carries a claim" is the right vocabulary; avoid "assertion," "statement," "result" (which is a specif |
| `class 2 scope exit` | +2 | 1 | (keep) +2 | The phrase "scope exit" for Class 2 (handing off to logogenic-agents/) is repeated in `#der-directed-separation` Findings and READM |
| `cognitive fusion` | +2 | 1 | (keep) +2 | Acceptable keep — logogenic-agents. "Cognitive fusion" with "Resonance" as the prose alias is workable. |
| `crèche creche` | +2 | 1 | crèche with diacritic in framing prose creche in slugs +2 | Mixed usage. Canonicalize: in segment titles and prose, "Crèche" with the grave accent (consistent with the agentic-tft source); in |
| `eli the agent type` | +2 | 1 | eli +2 | Acceptable keep — established in the firmatum / shoshin lineage. The acronym discipline check passes (used as a noun throughout the |
| `epistemic shadow` | +2 | 1 | (keep) +2 | Confirmation with new reasoning — Gemini's "epistemic shadow" (regions of strategy DAG that cannot be updated because feedback cann |
| `gradient causal memory` | +2 | 1 | (keep) +2 | Acceptable keep — logozoetic. GCM compression functions; the slug correctly names the structure. |
| `honest activation` | +2 | 1 | (keep) +2 | Acceptable keep — logozoetic norm. "Honest activation" reads as a thing (an activation pattern that preserves epistemic integrity); |
| `honesty scope honest scope honesty as architecture` | +2 | 1 | honesty +2 | Currently appears in three forms across `#disc-separability-pattern`, `#disc-identifiability-floor`, README, and CLAUDE.md. Canonic |
| `inevitability core` | +2 | 1 | (keep) +2 | The phrase "inevitability core" appears in FORMAT.md's three-rings discussion (~15 segments where inevitability is the ceiling); it |
| `loop vs cycle` | +2 | 1 | loop is structure cycle is traversal +2 | The LEXICON already does this distinction explicitly. Canonicalize as a discipline: in any prose where the distinction matters, use |
| `o t objective` | +2 | 1 | objective +2 | Confirm. Note: avoid "goal" as an alias — "goal" is the everyday-English compound noun (the thing the agent is trying to do); "obje |
| `purpose purposeful` | +2 | 1 | (keep) +2 | Confirm. "Purposeful agent" is the LEXICON-canonical term for actuated agents; "purposeful substate" for $G_t$. Avoid "goal-oriente |
| `section i header adaptive systems under uncertainty` | +2 | 1 | adaptive systems under uncertainty +2 | The OUTLINE uses this; preserve. Avoid drift to "Adaptive Dynamics" or "Section I: Adaptation." |
| `section iii header agentic composites` | +2 | 1 | agentic composites +2 | Confirm. Pairs with the LEXICON's continuity-stance and unity-dimensions vocabulary. |
| `structured rich context` | +2 | 1 | (keep) +2 | Acceptable keep — logogenic proposed. "Structured rich context" (SRC) is a substantive concept-name. |
| `substrate independence` | +2 | 1 | (keep) +2 | Acceptable keep — logozoetic. Names the result that identity survives substrate migration. |
| `the cycle the adaptive cycle the agentic cycle` | +2 | 1 | the cycle the adaptive cycle +2 | The five-phase Prolepsis-Aisthesis-Aporia-Epistrophe-Praxis cycle is "the cycle" or "the adaptive cycle" in the LEXICON and NOTATIO |
| `tier 1 tier 2 tier 3 contraction` | +2 | 1 | contraction tiers +2 | In `#form-composition-closure` and `#result-contraction-template`, the Tier 1/2/3 partition is sometimes "contraction tiers," somet |
| `two condition decomposition of persistence` | +2 | 1 | structural task adequacy decomposition +2 | `#result-persistence-condition` introduces this and the prose uses "two-condition decomposition," "structural vs task-adequacy spli |
| `u m epistemic unity multi agent` | +2 | 1 | epistemic unity +2 | Note: this collides with the symbol-letter $U_M$ for model-uncertainty in the single-agent setting. The framework uses the same let |
| `u m model uncertainty` | +2 | 1 | model uncertainty +2 | Confirm canonical alias. Already used; no friction. |
| `u o observation uncertainty` | +2 | 1 | observation uncertainty +2 | Confirm canonical alias. Note the subscript is lowercase 'o' (observation), not capital O — this is a frequent stumble for new read |
| `u obs perceptual unity` | +2 | 1 | perceptual unity +2 | Confirm. |
| `u σ strategic unity` | +2 | 1 | strategic unity +2 | Confirm. |
| `unnamed a class 2 agent s process of reconstructing its purposeful substate at session start` | +2 | 1 | intent reconstruction +2 | New alternative — Sonnet named "inter-session reconstruction" for the M_t side. The Σ_t side has a parallel: the agent must reconst |
| `unnamed an AAD result whose substantive content is a no-go theorem` | +2 | 1 | no-go result or impossibility result +2 | New alternative — none of the peers named this. The framework has several no-go results (#der-causal-insufficiency-detection's L0/L |
| `unnamed software s role as calibration laboratory named in prose but not in slug` | +2 | 1 | software as calibration laboratory +2 | The TST preamble names software as AAD's "privileged high-identifiability calibration laboratory," and CLAUDE.md says "calibration- |
| `unnamed the c1 c2 c3 monotonicity result` | +2 | 1 | the convention monotonicity +2 | The result $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ inside `#def-value-object` is a monotonicity result that downstream |
| `unnamed the explicit name for what makes class 2 agents distinctive bias scales with κ × 𝒜` | +2 | 1 | the κ × 𝒜 product +2 | Confirmation with new reasoning — Gemini coined "ambiguity-bounded bias law" and "the sycophancy equation" for this; both miss the |
| `unnamed the family of cross architecture diagnostic patterns AAD repeatedly invokes` | +2 | 1 | diagnostic templates +2 | New alternative — Codex named "sector-persistence template" and "contraction template" individually but didn't name the family. Son |
| `unnamed the family of named health mode counterparts to persistence pathologies` | +2 | 1 | persistence postures +2 | New alternative — health-mode dual to the family above. The framework reaches for these implicitly (sector condition holding, persi |
| `unnamed the joint failure mode where κ × 𝒜 is large and observation tempo is low` | +2 | 1 | the sycophancy attractor +2 | New alternative — Gemini's "sycophancy equation" names the product but not the *attractor* in dynamics that the product produces. W |
| `unnamed the move where AAD treats software not as instantiation but as TST s epistemically privileged measurement substrate` | +2 | 1 | calibration laboratory move +2 | Confirmation with new reasoning — my own r2 named "software-as-calibration-laboratory" as a name-unnamed; reading peers, Codex (+3) |
| `unnamed the move where a segment s role prefix is mechanical but the subject noun carries judgment` | +2 | 1 | the prefix noun split +2 | New alternative — the principles file names the architectural invariant but the *project vocabulary* for talking about the split ha |
| `unnamed the pearl-blanket reading of directed separation` | +2 | 1 | pearl-blanket form +2 | The term "Pearl-blanket" appears in `#der-directed-separation`'s Discussion (adopted from Bruineberg et al. 2022) but has no first- |
| `unnamed the recurring lyapunov derives the bound move across six segments` | +2 | 1 | the persistence template instantiation pattern +2 | The template `#result-sector-persistence-template` is invoked across six segments, each one specifying its own state variable, corr |
| `unnamed the regulative ideal that segment names should be re derivable from a non specialist s everyday language reconstruction` | +2 | 1 | feynman criterion +2 | New alternative — none of the peers explicitly canonicalized this even though it's named in CLAUDE.md and is the implicit standard |
| `unnamed the structural cousin of evidence starvation when an upstream edge is so reliable that downstream edges receive too few revising tests` | +2 | 1 | evidence saturation +2 | New alternative — none of the peers reached this. If "evidence starvation" is the failure mode where downstream edges are tested to |
| `unnamed the symmetric counterpart to context turnover for the strategy substate` | +2 | 1 | strategic turnover or σ turnover +2 | New alternative — `obs-context-turnover` names the M_t-side reset at session boundaries for logogenic agents. The Σ_t side has its |
| `𝓣 σ strategic tempo` | +2 | 1 | strategic tempo +2 | Confirm. Pairs with adaptive-tempo cleanly. |

#### Light (+1) — 72

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `OODA4 specification limit as TST concept currently only in old TST files` | +1 | 1 | OODA4 specification limit +1 | Keep reserved slot. Eventually promotes from old-tst files. |
| `actuated agent class` | +1 | 1 | actuated +1 | Keep. The LEXICON §"Actuated Agent" paragraph justifies the word explicitly ("precise and mechanical, avoiding consciousness connot |
| `adversarial edge targeting` | +1 | 1 | (keep) +1 | Keep (even though the segment is currently a GAP — the slug is reserving a memorable-noun slot). "Edge targeting" is vivid; the att |
| `agentic systems framework ASF top level` | +1 | 1 | agentic systems framework +1 | Keep. "Agentic Systems" reads cleanly as the project name; ASF acronym is workable. The word "agentic" is currently a buzzword, but |
| `calibration laboratory framing` | +1 | 1 | calibration laboratory +1 | Keep. "Laboratory" is the right metaphor (high-identifiability, clean instrumentation, lets you measure AAD quantities exactly). "F |
| `canonical formulations` | +1 | 1 | (keep) +1 | The middle ring in FORMAT.md's three-rings; in use but slightly redundant ("canonical" + "formulations" both name the chosen-among- |
| `change distance change proximity principle` | +1 | 1 | keep both +1 | Keep. Both are domain-specific TST quantities — changing names risks losing the TST citation lineage. |
| `chronica capitalized vs lowercase` | +1 | 1 | chronica lowercase in running prose +1 | Convention observation: NOTATION.md shows $\mathcal C_t$ in formalism and "*chronica*" in italics in prose; LEXICON has it title-ca |
| `coherence coupling measurement` | +1 | 1 | (keep) +1 | Keep. |
| `communal imagination test` | +1 | 1 | (keep) +1 | Keep. Names the evaluation criterion in a way that's memorable and actionable. Borrowed from the naming principles document itself. |
| `comprehension time implementation time` | +1 | 1 | keep both +1 | Keep. Canonical TST quantities. |
| `da2 inc` | +1 | 1 | (keep) +1 | Technical; symbol-grade. The prose equivalent "incremental sector bound" works; keep symbol as shorthand. |
| `dark room critique citation phrasing sun firestone` | +1 | 1 | dark room critique +1 | Memorable, captures the collapse vividly, already used in two segments. Worth locking as project-wide vocabulary. |
| `five phase cycle` | +1 | 1 | adaptive pentad alternative five phase cycle keep +1 | See above in unnamed-things. "Five-phase cycle" is the current descriptive form; "adaptive pentad" is an optional Greek-vocabulary |
| `gain sector bridge gain sector derivation` | +1 | 1 | keep both +1 | Keep. "Bridge" signals this is the connection piece (gain principle + directional fidelity → sector condition); "derivation" signal |
| `hierarchy as a project wide word` | +1 | 1 | flag four independent hierarchies overloaded +1 | Pearl's causal, AAD's convention, AAD's correlation, AAD's approximation tiering — four hierarchies in one framework. Not a rename |
| `hierarchy project wide` | +1 | 1 | reserve for pearl s causal hierarchy strict asymmetric uses +1 | Project-wide convention: use "hierarchy" only for Pearl's (external, adopted, immovable) and other strict-asymmetric orderings. Use |
| `identifiability floor escape the floor` | +1 | 1 | escape route +1 | Currently referred to variably as "escape the floor," "unique broadly-available escape," "boundary characterization." "Escape route |
| `intent planning vocabulary` | +1 | 1 | intent +1 | Used in `#hyp-auftragstaktik-principle`, `#def-shared-intent`, and elsewhere. Canonicalize: "intent" for the agent's own commitment |
| `l1 prime decoration` | +1 | 1 | l1 observable +1 | Agree with original. "L1-prime" awkward to speak; "L1-observable" matches the Prop B.7 observable-common-cause distinction from the |
| `model sufficiency model class fitness` | +1 | 1 | keep +1 | Keep both. Each is a specific technical quantity ($S$ and $\mathcal F$) — the slug is the concept. |
| `observability opacity` | +1 | 1 | keep as an informational pair +1 | Keep both. The dual framing (forward = observability, backward = opacity) is a load-bearing conceptual move; naming them as duals i |
| `observation function action transition` | +1 | 1 | keep +1 | Keep both. Short, direct, describe what they are. |
| `old TST files 40 files` | +1 | 1 | no rename these retire with migration map +1 | Not eligible for renaming — these are transitional absorption files that will retire once MIGRATION-MAP completes. Keep as-is. |
| `persistence three senses structural operational continuity` | +1 | 1 | keep three senses sharpen usage sites +1 | The three senses are load-bearing and correctly disambiguated in LEXICON.md. The *irreducibility* is fine — the three senses are ge |
| `prior art integration convention` | +1 | 1 | prior art integration +1 | Keep. Directive, clear. No better alternative. |
| `r1 r2 result numbering convention in logogenic agents` | +1 | 1 | keep with cross component prefixes l r1 l r2 +1 | As soon as logogenic-agents grows, "Result R1" collides with AAD-core numbering in discussion. Minor. |
| `recursive update derivation gain sector derivation` | +1 | 1 | standardize as derivation suffix for derivation type appendices +1 | Observation: the `-derivation` suffix on appendix segments is a good AAD convention (distinguishes derivation segments from stating |
| `section ii header actuated adaptation agentic systems` | +1 | 1 | actuated adaptation agentic systems +1 | Mild canonicalization. The current header reads slightly redundantly ("actuated adaptation" + "agentic systems"); could be simplifi |
| `software scope` | +1 | 1 | (keep) +1 | Keep. Direct. |
| `spike research artifact` | +1 | 1 | spike +1 | Already canonical in the corpus; vote to confirm. The naming-cycle has occasionally drifted to "exploration," "investigation," "bra |
| `system coherence system coupling system availability` | +1 | 1 | keep all three +1 | Keep — each is a distinct TST system-level property; the parallel `system-X` structure is itself pedagogical. |
| `temporal coherence markers` | +1 | 1 | (keep) +1 | Weak keep — logozoetic norm. The slug names the markers themselves rather than the norm-claim about them; could be more substantive |
| `the greek vocabulary` | +1 | 1 | the greek philosophical vocabulary +1 | The cycle phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) are described as "the Greek philosophical vocabulary" in NOTATI |
| `the integrated κ × a law` | +1 | 1 | the bias bound product law +1 | In `#scope-observation-ambiguity-modulation` and `#deriv-bias-bound`, the product $\kappa \times \mathcal{A}$ governing Class-2 bia |
| `the scaffolding tax` | +1 | 1 | scaffolding tax +1 | Drop "the" from the slug. |
| `the trio collectively` | +1 | 1 | epistemic architecture +1 | Use "epistemic architecture" as the CLAUDE.md §7 / OUTLINE.md framing phrase, not as a segment. A fourth meta-segment named `#epist |
| `three part meta architecture` | +1 | 1 | floor ladder forced coordinates +1 | Conditional collective-noun-trio. If both #separability-ladder and #forced-coordinates land, the trio is "floor / ladder / forced-c |
| `track 1 track 2 in bias bound derivation` | +1 | 1 | transport inequality track fisher rao track +1 | Inside the segment, "Track 1" and "Track 2" are fine as local shorthand. In any cross-segment reference, the English names read bet |
| `u f update rule homogeneity` | +1 | 1 | update rule homogeneity +1 | Already in use; weakly affirm. The alias is more verbose than the symbol but the symbol $U_f$ is itself unfamiliar. Prose users wil |
| `unnamed TST specific name for code that is observation cheap because it s well written` | +1 | 1 | observation cheap code +1 | New alternative — Codex coined "observation infrastructure" (which I support) and Sonnet renamed `der-code-quality-as-observation-i |
| `unnamed an organizational level instance of the persistence condition s bathtub gloss` | +1 | 1 | the bathtub model +1 | Confirmation with new reasoning — Codex named this at +2 (without explicit canonicalization) and I want to lift it: CLAUDE.md menti |
| `unnamed cascade of inferential force strengthening from c1 to c3 on satisfaction gap control regret diagnostics` | +1 | 1 | inferential cascade +1 | Agree with original. Low priority. |
| `unnamed cascade of inferential force through c1 c2 c3` | +1 | 1 | inferential force cascade +1 | The pattern "under C1 diagnostics are weak, C2 they sharpen, C3 they're global" — currently explained in prose every time it comes |
| `unnamed class 1 class 2 class 3 agent classes themselves need mnemonic handles` | +1 | 1 | proposal assign english modifiers +1 | Class-numbered labels work but lack mnemonic grip. Proposal: retain "Class 1 / 2 / 3" as the primary labels but assign canonical on |
| `unnamed effort time risk ranking considered false constraints` | +1 | 1 | false constraints +1 | Joseph uses this phrasing; worth canonicalizing so agents (me included) can recognize the pattern. |
| `unnamed future segment layer header for narrative pedagogical framing` | +1 | 1 | narrative framing +1 | Parallel reservation. For ELI10 / pedagogical outlines. |
| `unnamed future segment layer header for the sp 5 reader s path proposal` | +1 | 1 | reader s path +1 | Forward-looking name reservation. SP-5 adds a 1-2 sentence load-bearing preamble per segment; under the outline-filter affordance t |
| `unnamed joseph s mental model projection whose contraction rate must exceed its target s drift rate` | +1 | 1 | the projection slogan contraction over drift slogan +1 | CLAUDE.md §7(g) names this as "organizing-principle slogan" (O-BP10, not yet surfaced at segment level). If promoted to segment-lev |
| `unnamed scope honesty as architecture` | +1 | 1 | honesty +1 | Already used as a term; "-as-architecture" is the argumentative form. "Scope honesty" alone works as the noun for the commitment (a |
| `unnamed the 1 anchor 3 theorem structure itself` | +1 | 1 | anchor theorem pattern +1 | The `#forced-coordinates` meta-segment's shape (one mathematical identity + N theorems conditional on AAD-internal axioms). If the |
| `unnamed the 1 anchor plus 3 theorem characterization` | +1 | 1 | pattern anatomy +1 | Currently a long phrase that the theory uses three to four times per session. "1-anchor-plus-3-theorem" is precise but reads as inv |
| `unnamed the 2×2 satisfaction gap × control regret diagnostic table` | +1 | 1 | the 2×2 diagnostic +1 | Used ubiquitously in prose. Worth canonicalizing as a named object so that "see the 2×2 diagnostic" reads naturally. |
| `unnamed the a2 sub scope partition collectively` | +1 | 1 | a2 partition +1 | Not a symbol rename; a prose handle for the three-way α₁/α₂/β classification. "The A2' partition" lands more cleanly than "the A2' |
| `unnamed the architectural class partition class 1 class 2 class 3` | +1 | 1 | architectural partition +1 | Symbols stay (Class 1/2/3); prose gets "the architectural partition" as a collective handle. Avoids "architecture hierarchy" (hiera |
| `unnamed the calibration laboratory concept applied outside TST` | +1 | 1 | calibration domain +1 | CLAUDE.md §7 names TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measur |
| `unnamed the chain confidence decay mathematical anchor as the 1 in 1 anchor 3 theorem` | +1 | 1 | chain anchor +1 | Not a rename of the segment (`#chain-confidence-decay` keeps its slug) — a prose *handle* for the anchor's role in the `#additive-c |
| `unnamed the dimensional consistency constraint forcing the macro step formulation` | +1 | 1 | dimensional consistency repair +1 | The 2026-04-22 cycle's repair to `#form-composition-closure` (introducing $K_c$ and per-macro-step formulation) was driven by dimen |
| `unnamed the discipline of naming so that the slug survives reorganization` | +1 | 1 | reorganization resilient naming +1 | New alternative — Codex flagged that "Section II survival" should become "Class 2 survival" because the latter survives reorganizat |
| `unnamed the dual that pairs with persistence envelope on the strategic side` | +1 | 1 | strategic persistence envelope +1 | New alternative — my r2 coined "persistence envelope" for the M_t-side region $\{(\alpha, \rho, R) : \alpha > \rho/R\}$. The Σ_t si |
| `unnamed the functional requirements are the results formalisms are the engineering slogan` | +1 | 1 | functional primacy +1 | Joseph flagged this as an established project principle (MEMORY.md, Theory Character section); it deserves a pull-quote name. Low c |
| `unnamed the mathematical operation by which agents convert observed mismatch into structural revision` | +1 | 1 | structural cascade +1 | New alternative — none of the peers reached this. Observed mismatch → parametric update is the standard cycle; observed mismatch → |
| `unnamed the moment when an agent s identity claim becomes load bearing because actions become irreversible` | +1 | 1 | constitutive moment +1 | New alternative — `form-constitutive-utterance` names the formal object (the irreversible token-generation event) but the *moment* |
| `unnamed the organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate` | +1 | 1 | projection contraction slogan +1 | CLAUDE.md §7(g) flags this as Opus O-BP10, "not yet surfaced at segment level." Deserves a name so it can be referenced before it l |
| `unnamed the rate at which an agent s chronica grows compared to compression cadence` | +1 | 1 | chronica throughput +1 | New alternative — Gemini reached "complementary learning architecture" and "scaffolding tax" but didn't name the rate-quantity that |
| `unnamed the scope honesty as architecture working principle` | +1 | 1 | honesty scope honesty as architecture +1 | Already named in CLAUDE.md §7(a) as "scope-honesty-as-architecture." The phrase is workable; the shorter "scope honesty" does most |
| `unnamed the strengthen first attempt artifact a spike that tried to derive something stronger and failed` | +1 | 1 | strengthening attempt attempt record +1 | The CLAUDE.md text says "document the strengthening attempt and why it failed even when it does fail." These deserve a noun so the |
| `unnamed the symbol overload region where $U_M$ means two different things` | +1 | 1 | the $U_M$ overload +1 | A naming-cycle artifact rather than a theory artifact, but worth surfacing. The repeated bug-attractor (model-uncertainty $U_M$ vs |
| `unnamed the template family sector persistence contraction possible future dissipativity` | +1 | 1 | persistence templates the template family +1 | The three-member family of `#sector-persistence-template`, `#contraction-template`, and (proposed Tier-2) `#dissipativity-template` |
| `unnamed the three concentric rings of segment content inevitability core canonical formulations empirical heuristic` | +1 | 1 | three rings +1 | FORMAT.md uses exactly this language. Named once; currently paraphrased each time. Adopt "three rings" as the canonical shorthand. |
| `unnamed the three rings of segment content framing` | +1 | 1 | segment rings +1 | FORMAT.md §"Three rings of segment content" (inevitability-core / canonical-formulations / empirical-heuristic-discussion) is load- |
| `what is derived vs what is chosen derivation audit table` | +1 | 1 | derivation audit +1 | The full title is load-bearing for first-encounter readers; `### Derivation Audit` is a usable shorter alternative for segments whe |

#### Net-rejected (≤ 0) — 7

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `a2 operator sector condition under fidelity degraded updates` | -1 | 1 |  -1 | Considered replacing "A2'" (the symbol for the sector condition itself) with an English name and rejected. A2' is how AAD *refers b |
| `empirical heuristic discussion ring` | -1 | 1 | third ring or empirical periphery -1 | Considered and rejected. "Third ring" is positional and uninformative; "empirical periphery" overspecifies on empirical (the ring a |
| `l1 l1 prime` | -1 | 1 | l1 observable l1 soft -1 | Considered renaming the prime-decoration to a word. Reject: L1' consistently refers to *soft-facilitator under observable common ca |
| `unnamed the cross cycle equivalent of the bathtub gloss multi cycle persistence as a savings account` | -1 | 1 | the savings account gloss -1 | Considered and rejected — I thought of this while reading Codex's "bathtub model" entry (does multi-cycle persistence get its own a |
| `unnamed the four axis content structural unity decomposition` | -1 | 1 | the unity quintet -1 | Considered and rejected — "quintet" is too cute. Better to keep the existing four-content + one-structural decomposition explicit i |
| `unnamed the persistence envelope` | -1 | 1 | adaptive basin -1 | Considered. Reject: "basin" is already mathematically loaded (basin of attraction), and AAD's region *is a basin of attraction* — u |
| `AAD alternatives considered for completeness` | -2 | 2 | apd adaptation and purpose dynamics -1; AAD adaptation and agency dynamics -1 | "Purpose" captures Section II better than "actuation" but the acronym APD is cryptic; AAD has the phonetic advantage of being prono |

### Sonnet only (70 targets)

#### Moderate (+2..+4) — 42

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `actuated vs purposeful goal oriented` | +3 | 1 | actuated +3 | The terminology note is correct — "actuated" avoids consciousness connotations while being technically precise. Keep the choice. |
| `adaptation and actuation dynamics` | +3 | 1 | (keep) +3 | The rename from ACT to AAD was already deliberate and well-documented. The name is descriptive of the two halves (adaptation = Sect |
| `aporia as the phase name` | +3 | 1 | aporia +3 | The phase is named; the signal within it is "mismatch signal." The distinction is correct and maintained. Keep both with distinct s |
| `appendices operational domains` | +3 | 1 | (keep) +3 | Correct and specific. Keep. |
| `bounded disturbance ga 2 model d` | +3 | 1 | bounded disturbance +3 | Clear. Keep. |
| `calibration laboratory calibration lab` | +3 | 1 | calibration laboratory +3 | Currently appears as "richest operationalization domain," "best operationalization domain," "privileged high-identifiability calibr |
| `calibration laboratory software s role` | +3 | 1 | calibration laboratory +3 | Excellent coinage. The specific phrase "privileged high-identifiability calibration laboratory" is slightly long for prose but "cal |
| `canonical formulations second ring` | +3 | 1 | canonical formulations +3 | Keep. |
| `directional fidelity condition b1` | +3 | 1 | directional fidelity +3 | The name earns its place — "fidelity" captures the accuracy commitment (the correction points approximately toward reality) and "di |
| `edge credence $p_{ij}$` | +3 | 1 | edge credence +3 | "Credence" is the correct Bayesian vocabulary for subjective probability. LEXICON.md lists this under "Terms to Be Added." Should b |
| `fluid limit ga 5` | +3 | 1 | fluid limit +3 | Standard terminology from stochastic processes. Keep. |
| `fresh noise ga 1` | +3 | 1 | fresh noise +3 | The informal name "Fresh noise" for the independence assumption on ε_t is perfectly memorable. Keep exactly as is. |
| `i adaptive systems under uncertainty` | +3 | 1 | (keep) +3 | The section name is accurate and positions Section I correctly. "Under Uncertainty" is load-bearing — it distinguishes adaptive sys |
| `inevitability core the 15 segments where inevitability is plausible` | +3 | 1 | inevitability core +3 | FORMAT.md's three-ring framing (inevitability core / canonical formulations / empirical-heuristic-discussion) is clear and internal |
| `logogenic vs language based RLHF4 based` | +3 | 1 | logogenic +3 | Names the structural property. Keep. |
| `logozoetic vs conscious OODA4 sentient agent` | +3 | 1 | logozoetic +3 | The distinction between logogenic and logozoetic is precise and non-question-begging. Keep both. |
| `observation ambiguity observation ambiguity modulation` | +3 | 1 | observation ambiguity +3 | The compound noun works. "Ambiguity" is the right word for the interpretive latitude of an observation given the agent's goal state |
| `pearl-blanket conservative form of markov blanket in directed separation` | +3 | 1 | pearl-blanket reading +3 | Bruineberg et al. 2022's terminology distinguishes Pearl-blanket from Friston-blanket. Using it positions AAD's move precisely. Kee |
| `persist condition` | +3 | 1 | persistence condition +3 | Wait — this IS the name already. Correct name. Keep. |
| `plan confidence $\hat P_\Sigma$` | +3 | 1 | plan confidence +3 | More evocative than "root-node propagated status." LEXICON.md lists this under "Terms to Be Added." Promote to main LEXICON. |
| `sector condition continuous ga 3` | +3 | 1 | sector condition +3 | Keep. The "(continuous)" qualifier is important to distinguish from the discrete-time DA2'. |
| `stochastic disturbance ga 2s model s` | +3 | 1 | stochastic disturbance +3 | The "Model D / Model S" subscript convention is also well-established and should be kept alongside the prose names. Keep both. |
| `teleological unity $U_O$` | +3 | 1 | teleological unity +3 | The three unity dimensions (epistemic, teleological, strategic) form a coherent vocabulary. Keep all three. |
| `unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa` | +3 | 1 | epistemic ceiling +3 | This relationship appears in the `#der-orient-cascade` Discussion (better $M_t$ enables richer evaluable $\Sigma_t$) and is partial |
| `unnamed the evidence starvation effect on downstream edges` | +3 | 1 | evidence starvation +3 | `der-chain-confidence-decay` Discussion names it "the evidence-starvation effect" and `der-observability-dominance` uses the same t |
| `unnamed the phenomenon where persistence success makes an agent less likely to detect the conditions requiring structural adaptation` | +3 | 1 | stability induced myopia +3 | This concept has a name in CLAUDE.md: "stability-induced myopia patterns (Christensen / Levitt-March / Hannan-Freeman / March / Eld |
| `unnamed the projection whose contraction rate must exceed target drift the opus organizing principle slogan` | +3 | 1 | contraction over drift principle +3 | CLAUDE.md attributes to Opus: "an adaptive system is a projection whose contraction rate exceeds its target's drift rate." This is |
| `unnamed the strengthen first attempt the improbable meta approach to theory development` | +3 | 1 | attempt the improbable +3 | CLAUDE.md uses "attempt the improbable" as the better version of "strengthen-first posture." This phrase is memorable and CLAUDE.md |
| `additive coordinate forcing → disc forced coordinates` | +2 | 1 | confirming consensus 3 +2 | All five agents voted this at +2 or +3. What I can add beyond my own cold-start vote: the cross-vote reading shows that all agents |
| `feedforward loop feedback loop` | +2 | 1 | feedback loop +2 | "Feedback loop" is the canonical term in AAD. "Feedforward" is never intended in this context but might appear in places where "for |
| `ii actuated adaptation agentic systems` | +2 | 2 | ii agentic systems purposeful adaptation +1; ii purposeful adaptation actuated agents +1 | Another order. "Agentic Systems" has search/navigation value as a heading. Both alternatives are improvements on current. |
| `integration of four disciplines as the framing of AAD s contribution` | +2 | 1 | epistemic architecture +2 | PROPOSALS §Bundle 1 notes that three independent frontier-model audits converged on reframing AAD from "integration of four discipl |
| `separability pattern → disc separability ladder` | +2 | 1 | confirming consensus 3 +2 | All five agents voted this at +2 or +3. New reasoning: Opus specifically notes the naming should be singular ("separability-ladder" |
| `unnamed the 1 anchor 3 theorem structure in additive coordinate forcing` | +2 | 2 | anchored theorem pattern +1; identity anchored forcing +1 | The structure appears across the project and is referenced in CLAUDE.md and multiple segments as "1-anchor-plus-3-theorem." This ph |
| `unnamed the a2 sub scope partition into α₁ α₂ β` | +2 | 1 | gain regime partition +2 | The three sub-scopes within A2' ($\alpha_1$ = fixed-gain, $\alpha_2$ = adaptive-gain, $\beta$ = assumed sector) appear in `deriv-ad |
| `unnamed the log additivity result that unifies chain confidence decay evidence starvation and triple depth penalty as instances of the same forcing structure` | +2 | 1 | depth forcing +2 | Codex explicitly canonicalized "triple depth penalty" (+3) and "evidence starvation" (+3); I canonicalized both in my cold-start. B |
| `unnamed the reconstruction adequacy condition for logogenic agents` | +2 | 1 | reconstruction threshold +2 | `obs-context-turnover` derives a condition $S(f_{\text{init}}(\ldots)) \geq S_{\text{min}}$ parallel to the persistence condition b |
| `unnamed the relationship where $M_t$ quality bounds evaluable complexity of $\Sigma_t$` | +2 | 1 | epistemic strategic coupling +2 | `der-orient-cascade` Discussion names the virtuous/vicious cycle where better $M_t$ enables richer evaluable $\Sigma_t$ and vice ve |
| `unnamed the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ too certain rather than because $U_M \to 0$ model confident` | +2 | 1 | certainty trap +2 | Gemini proposed "competency trap" for $\eta^\ast \to 0$ under high $U_o$, but that term imports different connotations (being too g |
| `unnamed the three depth penalty compounding on strategy chains` | +2 | 1 | triple depth penalty +2 | `der-chain-confidence-decay` Discussion explicitly names "three independent penalties" (confidence decay + evidence starvation + co |
| `unnamed the three part meta architecture of AAD formed by the three meta segments` | +2 | 1 | AAD meta architecture +2 | The trio of `#disc-additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern` is referred to in mu |
| `unnamed the within session vs inter session persistence distinction for logogenic agents` | +2 | 1 | intra session persistence inter session reconstruction +2 | `obs-context-turnover` Discussion explicitly distinguishes two timescales and briefly names them "intra-session" and "inter-session |

#### Light (+1) — 26

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `appendices details` | +1 | 1 | appendices derivations and details +1 | Many appendix segments are type: derivation. The current label "Details" undersells what's there. "Derivations and Details" is more |
| `chain confidence decay keep` | +1 | 1 | reaffirm keep with new reasoning +1 | Opus's proposed rename to `#der-log-confidence-additive` (+1) is intellectually interesting (names the uniqueness move rather than |
| `contraction hierarchy` | +1 | 1 | contraction tier +1 | The Tier 1/2/3 system in #composition-closure is called "Contraction Tier" not "Contraction Hierarchy." Slight naming inconsistency |
| `empirical heuristic discussion third ring` | +1 | 1 | calibration ring +1 | The current name ("Empirical, heuristic, discussion") is a list, not a name. "Calibration ring" would give it a single handle. Alte |
| `evidence starvation canonicalize` | +1 | 1 | reaffirm 3 with collective confirmation +1 | Both Codex (+3) and Gemini (+3) independently proposed this canonicalization with overlapping reasoning. My cold-start had proposed |
| `gemini s analysis paralysis for excessive deliberation` | +1 | 1 | reject analysis paralysis +1 | Gemini proposed "analysis paralysis" (+3) for the condition where $\rho_\text{delib} \cdot \Delta\tau$ exceeds the epistemic benefi |
| `gemini s boyd exponent for adversarial tempo advantage` | +1 | 1 | reject boyd exponent +1 | Gemini proposed "Boyd exponent" (+3) for the superlinear adversarial tempo advantage ($b = 2$). This violates the project's prior-a |
| `gemini s competency trap for $\eta^\ast \to 0$` | +1 | 1 | reject competency trap +1 | See "certainty trap" (new alternative above). "Competency trap" imports organizational-learning baggage (Levitt & March) where the |
| `gemini s epistemic death for the gain collapse unobservable DAG failure` | +1 | 1 | reject epistemic death +1 | Gemini proposed "epistemic death" (+3) for the state where credit assignment collapses and learning freezes. This fails the scope-h |
| `iii agentic composites` | +1 | 1 | iii composition agentic composites +1 | Adding "Composition" as a leading term would make the section's topic clear without opening the file. "Agentic Composites" alone so |
| `mismatch injection rate $\rho$` | +1 | 1 | mismatch injection rate +1 | The phrase "environmental change rate" and "mismatch injection rate" are both used for $\rho$. "Mismatch injection rate" is more pr |
| `promote in topological order` | +1 | 1 | topological promotion order +1 | FORMAT.md uses this phrase but doesn't name it as a convention. "Topological promotion" as a named methodology would make the gate- |
| `triple depth penalty canonicalize` | +1 | 1 | reaffirm 3 with new framing +1 | Codex voted this (+3). My cold-start had proposed it (+2). The upgrade: reading across the votes, "triple depth penalty" is the *on |
| `unnamed the 2×2 orient cascade diagnostic table` | +1 | 1 | the cascade diagnostic or the 2×2 diagnostic +1 | The four cells of ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) are consistently referenced in `der-orient-cascade` as "the 2×2 |
| `unnamed the condition that a strategy DAG s endosymbiont crosses the composite agent scope from below` | +1 | 1 | crossing threshold +1 | `hyp-symbiogenic-composition` describes the pre/post-symbiogenesis transition as "$U_O$ crosses the composite-agent scope condition |
| `unnamed the condition that the agent s event observation pairs constitute genuine interventions as opposed to passive associations` | +1 | 1 | interventional character +1 | #loop-interventional-access makes this distinction at length: action-generated data has "interventional character" but is not the s |
| `unnamed the contraction over drift insight` | +1 | 1 | drift contraction inequality +1 | Alternative name. More technical but maps directly to the inequality. |
| `unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing` | +1 | 1 | three part scope architecture +1 | CLAUDE.md already calls this "AAD's three-part meta-architecture" in several places. Crystallizing this as a named concept — the sc |
| `unnamed the pattern where AAD s negative results floors strengthen the machinery that escapes them` | +1 | 1 | floor strengthening inversion +1 | #identifiability-floor says: "floors strengthen the load-bearing role of the AAD machinery that supplies the unique escape." This i |
| `unnamed the procedure of reading any segment through all three meta segments` | +1 | 1 | triple lens review +1 | CLAUDE.md says "reading any segment through all three lenses surfaces what makes it load-bearing." This procedure is recommended bu |
| `unnamed the set of five conditions under which a2 is derived rather than assumed the sub scope α agent classes` | +1 | 1 | derived sector classes +1 | Currently called "sub-scope α₁" plus the specific agent instances in a list. A collective name for the five agent classes where A2' |
| `unnamed the signed coupling structure across all section iii results` | +1 | 1 | signed coupling pattern +1 | Every Section III persistence result (team-persistence, adversarial-destabilization, critical-mass-composition) uses the same effec |
| `unnamed the strengthen before soften posture applied to apparent overclaims` | +1 | 1 | epistemic strengthening posture +1 | CLAUDE.md and MEMORY.md both discuss this as "strengthen-first posture" or "strengthen before softening." The working vocabulary is |
| `unnamed the virtuous vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity` | +1 | 1 | model strategy coupling +1 | #orient-cascade Discussion names the virtuous and vicious cycles explicitly but without a name for the coupling phenomenon itself. |
| `value object → def trajectory value` | +1 | 1 | conditional support for codex s rename +1 | Codex proposed `#def-trajectory-value` (+2); Opus voted keep (+1) and rejected `#def-value-functional` (−1). My cold-start voted ke |
| `what is derived vs what is chosen derivation audit table heading` | +1 | 1 | derivation audit +1 | The longer form ("What Is Derived vs. What Is Chosen") is the current recommendation in FORMAT.md but it's wordy. "Derivation Audit |

#### Net-rejected (≤ 0) — 2

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `unnamed the meta architecture of the three meta segments` | -1 | 1 | AAD s epistemic triptych -1 | "Triptych" is too art-historical and too cute. The naming-principles document warns against cute names that age poorly. |
| `unnamed the pattern where the agent s optimal update direction is determined by both gain and directional fidelity together` | -1 | 1 | gain fidelity product -1 | Too technical and not used in prose. The formula is just α = η* × c_min. No name needed. |

### agent1 only (12 targets)

#### Moderate (+2..+4) — 4

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `bruineberg s pearl-blanket` | +3 | 1 | pearl-blanket +3 | Adopted concept; keep. |
| `hafez s h b` | +3 | 1 | h b +3 | Adopted concept; AAD adds observer/horizon/trajectory indexing but keeps the symbol. |
| `monderer shapley potential games` | +3 | 1 | (keep) +3 | Adopted concept; keep. |
| `persistence structural operational continuity` | +3 | 1 | three senses keep all three +3 | Triple-meaning is load-bearing and probably irreducible. Each usage site should be explicit about which sense when it matters. |

#### Light (+1) — 6

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `hierarchy as repeated word` | +1 | 1 | reserve for pearl s rename others selectively +1 | Weak proposal. Four uses in the framework (Pearl's, convention, correlation, approximation-tiering) is likely too many. Partial dis |
| `l1 correlation hierarchy prime decoration` | +1 | 1 | l1 observable +1 | "L1-prime" is awkward to speak. Giving L1' a name rather than prime-decoration could help if the hierarchy becomes load-bearing for |
| `unnamed calibration laboratory framing as reusable meta move` | +1 | 1 | calibration domain calibration lab +1 | Low priority. Concept of a privileged domain for identification within a theoretical framework is itself a reusable meta-move other |
| `unnamed chain layer anchor role in additive coordinate forcing` | +1 | 1 | chain anchor +1 | Prose term, not segment rename. Lets three theorem-analogs refer back naturally. |
| `unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3` | +1 | 1 | inferential force cascade +1 | Low priority but worth noting. Pedagogical. |
| `unnamed cycle phase sequence as whole` | +1 | 1 | the pentad five phase cycle +1 | Probably not worth effort. Worth surfacing. |

#### Net-rejected (≤ 0) — 2

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `l1` | -1 | 1 | l1 c -1 | Too technical; uses symbol. |
| `AAD` | -2 | 2 | adaptation and purpose dynamics apd -1; adaptation and agency dynamics AAD -1 | Considered alternative. Acronym collision risk; doesn't roll off the tongue. |

### audit only (13 targets)

#### Strong (≥ +5) — 1

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `unnamed` | +9 | 6 | constitutive opacity triad +2; anchor plus three theorem additive coordinate forcing meta pattern +2; double opacity dual opacity as constitutive +2; zero aporia ambiguity +1 | The chain of three constitutive-opacity claims (info-loss / transition-opacity / observation-epistemic-opacity) is a structural com |

#### Moderate (+2..+4) — 4

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `action fluency` | +2 | 1 | (keep) +2 | Auditor: evocative term he hasn't seen in the agent-theoretic literature; closest is Boyd's "implicit guidance and control." AAD-di |
| `completeness c3` | +2 | 1 | predictive completeness behavioral completeness +2 | The term bundles two distinct properties: (i) $M_t$ retains all relevant info from history (sufficiency), (ii) the agent's behavior |
| `nominal coupling` | +2 | 1 | query bound attention bound epistemic only query coupling attentional coupling +2 | "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rat |
| `persistence overloaded` | +2 | 1 | structural persistence task adequacy operational persistence continuity persistence +2 | The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Wor |

#### Light (+1) — 8

| original | total | votes | candidates | description |
|---|---:|---:|---|---|
| `boundary condition` | +1 | 1 | coupling structure +1 | "boundary condition" carries PDE/control-theory meaning that's not what the segment means; "coupling structure is constitutive" lan |
| `chronica brief gloss` | +1 | 1 | everything the agent has lived through the lived past the river that the agent s identity is downstream of +1 | Brief-field-grade gloss. The slug stays; the layperson/Feynman gloss is what's missing. [from 04-def-chronica.md] |
| `epistemic opacity` | +1 | 1 | keep but flag baggage +1 | Auditor flagged that "epistemic opacity" carries philosophy-of-mind prior-art baggage (opacity of mental states) and may need defen |
| `loop is level 2 engine der loop interventional access` | +1 | 1 | the perpetual experiment +1 | Brief-grade framing observation. The slug-grade name `der-loop-interventional-access` is fine; for *framing-level* material, "the p |
| `matrix CIY tensor CIY` | +1 | 1 | fisher CIY matrix CIY consistent +1 | Inconsistent terminology in `#disc-ciy-unified-objective`: both "Matrix CIY" and "$\mathcal{I}_o(a)$"/Fisher Information Matrix app |
| `pearl l1 l2 l3` | +1 | 1 | predicting exploring reasoning +1 | Brief-grade agent-side gloss. NOT a rename — keep Pearl's terms formally. The agent-action gloss makes it audience-friendly. [from |
| `pearl-level 2 causal contrast` | +1 | 1 | the agent s choice actually changes what happens +1 | Brief-grade gloss only. The formal name is doing real work; the layperson translation is missing from any Brief field. [from 06-sco |
| `transition opacity` | +1 | 1 | heading flag only +1 | The phrase is "fine but slightly clinical." Pairing it with "perception opacity" / "epistemic opacity" as a deliberate triad would |

