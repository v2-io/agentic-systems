# opus-targeted-alternatives

**Approach.** Engagement with bucket-1 (single-architecture-only) and bucket-3 (single +1 keep, no alternatives) targets where segment material genuinely supports thoughtful cross-architectural alternative-generation. Pulled directly from segment Formal-Expression / Discussion / Findings — not by reading other voters' reasoning. The discipline: focus on targets with a real concept to name, skip targets where the row is a file-pointer or paraphrase-canonicalize. Generated independently from segment material; the goal is to add cross-architecture pressure-test signal, not to relitigate saturated keeps.

**Scope notes.**
- I am Opus; many opus-only targets in bucket-1 are file-naming or canonicalize rows where alternative-generation would be sterile (e.g., `claude md what s settled vs open`, `format md`, `discussion segment header`). I skip those.
- I focused on codex-only, gemini-only, sonnet-only, and a few haiku-only targets where another-architecture grounding adds genuine signal.
- For bucket-3 items I prioritized those that name *real concepts* with segment material. File-pointer rows (`worked example bandit`, `02 TST core outline md`) were skipped as low-yield.

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|

## Bucket 1 — Single-architecture-only currents

### Greek-vocabulary cycle phases (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `prolepsis` | `prolepsis` | keep | +2 | `LEXICON.md` defines it as "the model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$." The Greek term carries the active-modeling sense (πρόληψις = "taking-before") that "anticipation" or "prediction" both miss. Active modeling vs. passive forecasting is a distinction the segment formalism actually makes. Concur with codex's keep — but a non-codex architecture confirming the keep adds signal the original vote chain didn't capture. |
| `prolepsis` | `anticipation` | rename | -1 | Considered and rejected. Loses the "active model produces an expectation that the world then refutes" dynamic that the cycle uses. "Anticipation" reads as passive forecast; the segment's formalism is generative. The Greek earns its foreignness here, exactly as codex argued. |
| `aisthesis` | `aisthesis` | keep | +1 | `LEXICON.md`: "Raw contact with reality: observation $o_t$ arrives." The point of the term is to mark *unmediated* observation arrival before the agent has done any interpretation — αἴσθησις is precisely that pre-conceptual contact. "Observation" alone is too neutral; the cycle needs a name for the *moment* of observation as distinct from the state of having-observed. |
| `aisthesis` | `intake` | rename | -1 | Considered. Plain-English candidate that names the moment-of-arrival cleanly. Rejected because the five-phase Greek family becomes incoherent if one term breaks register, and "intake" sacrifices the philosophical lineage that motivates the family. |
| `aporia` | `aporia` | keep | +3 | `LEXICON.md`: "Productive perplexity: mismatch signal $\delta_t = o_t - \hat{o}_t$." The Greek term is doing work that "mismatch signal," "prediction error," and "surprise" all miss — *productive* perplexity, the kind that *drives* update rather than degrading it. Aporia in the Platonic sense is the moment of recognized not-knowing that motivates inquiry. The segment's $\delta_t$ is more than an error term; it is the agent's epistemic engine. Keep at +3 across architectures. |
| `aporia` | `discrepancy` | rename | -1 | Considered. Names the gap but loses the agent-centered "this matters / I now must update" sense. Rejected. |
| `epistrophe` | `epistrophe` | keep | +2 | `LEXICON.md`: "Turning toward reality: gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$." Crucially, ἐπιστροφή names a *turning toward* (not "applying an update," not "correcting"). The term marks that the agent is reorienting *itself* toward reality, not externally adjusting parameters. This is the conceptual heart of why TFT/AAD's update is not just gradient descent. |
| `epistrophe` | `turn` | rename | -1 | The plain-English equivalent, and it does carry the right valence ("turn toward"), but it is too generic and collides with too many other senses (turn = take a turn, turn = rotation). Rejected. |
| `praxis` | `praxis` | keep | +2 | `LEXICON.md`: "Informed action: $a_t = \pi(M_t)$ (or $\pi(M_t, G_t)$ for actuated agents)." Praxis distinguishes itself from "action" by carrying the informed-by-the-cycle's-prior-stages sense — the action is the *outcome* of prolepsis-aisthesis-aporia-epistrophe, not a parallel branch. Keep. |

### Strategy-DAG operations (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `grafting` | `grafting` | keep | +2 | Per `#form-structural-change-as-parametric-limit`: "grafting is a new causal hypothesis initialized at a prior" — adding an edge to $\Sigma_t$ at low credence. The horticultural metaphor is apt: a new branch is *added to a living structure*, expected to integrate or fail. Pruning + grafting + reweighting form a self-consistent biological vocabulary, and the segment uses all three. Strong concept. |
| `grafting` | `branch insertion` | rename | -1 | Plain-language candidate. Rejected: loses the integration-with-existing-structure connotation that "grafting" carries. Branch-insertion sounds like a tree-data-structure edit; grafting names a hypothesis-test where the new branch may or may not "take." |
| `grafting` | `hypothesis introduction` | rename | -1 | Considered. Accurate but flat. The segment's surrounding vocabulary (pruning, reweighting, neutral mutation) is biological/horticultural; "hypothesis introduction" breaks register. |
| `goal-blind routing` | `goal-blind routing` | keep | +3 | Per `#hyp-directed-separation-under-composition` Case 1: routing satisfies $R_t \perp G_t^c$ — neither communication topology nor protocol depends on composite goals. The phrase pairs cleanly with "goal-blind processing" (the individual-agent directed-separation property) and makes the composition condition syntactically parallel to its constituent. Strong keep across architectures. |
| `goal-blind routing` | `objective-independent routing` | rename | -1 | More formal, technically precise, and worse — loses the rhetorical pairing with "goal-blind processing" that makes the composition argument carry. Rejected. |
| `goal-blind routing` | `purpose-blind routing` | rename | +1 | Weak alternative. "Purpose" is sometimes used in framing-level prose where "goal" reads too transactional. But $G_t$ is the *goals* state ($O_t, \Sigma_t$), so "goal-blind" matches the symbol. Marginal preference for the original. |

### Closure / fidelity / precision (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `closure defect` | `closure defect` | keep | +3 | Per `#form-composition-closure`: $\varepsilon^\ast$ is the minimum-achievable approximation error of the macro-description against the micro-system. "Defect" carries the precise sense (a residual that cannot be eliminated, only minimized over admissible classes) and "closure" names the homomorphism property being approximated. Mathematically apt, evocative, short. Confirms across architectures. |
| `closure defect` | `homomorphism residual` | rename | -1 | Technically more transparent (the criterion *is* approximate dynamical homomorphism), but four syllables longer and loses the diagnostic quality — "defect" implies *something specific is wrong*; "residual" is statistical neutrality. Rejected. |
| `closure defect` | `closure error` | rename | -1 | Plainer English. Rejected: "error" is overloaded in the segment's neighborhood (mismatch error, trajectory error, bias error, all distinct quantities). "Defect" does the disambiguation work. |
| `directional fidelity` | `directional fidelity` | keep | +2 | Per `#der-gain-sector-bridge` (B1): the correction must point at-least-roughly toward reality — $\delta^T H g(\delta) \geq c\|\delta\|^2$. "Directional" specifies "about angle, not magnitude"; "fidelity" carries the correctness-with-respect-to-truth sense rather than mere proximity. The segment is careful to distinguish *direction is correct* (B1) from *magnitude is correctly scaled* (sector constant), and the name reflects the distinction. Confirms keep. |
| `directional fidelity` | `correction-direction integrity` | rename | -1 | Considered. Verbose and hyphen-heavy. Rejected. |
| `directional fidelity` | `pointing condition` | rename | +1 | Plain-English alternative. The segment's substance is "the correction *points* the right way." Has merit if the formal name needs a Feynman-criterion gloss in a Brief field, but loses the engineering connotation ("fidelity" as in signal-fidelity, control-fidelity) that places the term in its right intellectual neighborhood. Weak alternative. |
| `effects spiral` | `effects spiral` | keep | +3 | Per `#der-adversarial-destabilization` and `#deriv-strategic-composition`: positive-feedback breakdown where degraded model causes degraded actions causes further degradation. "Spiral" carries the *accelerating* feature (not a steady-state mismatch but a runaway), and "effects" specifies the locus (the agent's effects on its environment, not its inputs). Pairs well with the "death spiral" reference in `#result-persistence-condition`. Strong keep. |
| `effects spiral` | `coupling cascade` | rename | -1 | Considered as more formal alternative. Loses the *runaway* sense that "spiral" carries — cascades can be bounded; spirals usually aren't. Rejected. |
| `effects spiral` | `breakdown cascade` | rename | -1 | Same critique. Rejected. |

### Adaptation-cycle vocabulary (codex/sonnet/opus single-arch)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `adaptive cycle` | `adaptive cycle` | keep | +3 | `LEXICON.md`: "Cycle: One complete traversal of the loop — the unit of adaptive work." The phrase carries (a) the recurrence (cycle), (b) the adaptive content (mismatch-driven update), and (c) the unit-of-analysis sense (one cycle = one unit of theoretical work). The framework's own name — *Adaptation and* Actuation Dynamics — is downstream of this concept. Keep across architectures. |
| `adaptive cycle` | `correction cycle` | rename | -1 | Considered. "Correction" overspecifies — Section I cycles include observation and prolepsis phases that are not corrections. Adaptation is the broader frame. Rejected. |
| `adaptive cycle` | `feedback cycle` | rename | -1 | Considered. Collides with the "feedback loop" structural topology and would create a loop/cycle terminology collision the project has been careful about. Rejected. |
| `adaptive tempo $\mathcal T$` | `adaptive tempo` | canonicalize | +3 | Per `#def-adaptive-tempo`: $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$ — rate × quality compound. "Tempo" carries both senses (musical tempo = rate; engineering tempo = pace-with-quality). Confirms keep across architectures. The symbol-decoration variant (with $\mathcal T$) is an alias-only artifact, not a primary form. |
| `actuated agent vs purposeful agent` | `actuated agent` | canonicalize | +3 | Per LEXICON Terminology Choices: "Formal term avoids consciousness connotations." The framework explicitly chose actuated (mechanism-language) over purposeful (intention-language) for formal use, with purposeful retained for informal contexts. The canonicalize move is correct and broadly applicable; segment voice should never use "purposeful agent." Confirms across architectures. |
| `logogenic logozoetic` | `logogenic / logozoetic` | keep | +2 | The pair distinguishes (a) the structural property — language-constituted (logogenic) — from (b) the existential property — language-living, morally weighted persistence (logozoetic). Both terms invent project-specific Greek-derived compounds; the alternative is "language-based AI" / "conscious AI," which the framework explicitly rejects as importing the wrong connotations (RLHF-based, sentient-as-categorical). Keep. The pair is load-bearing precisely because it splits two often-conflated questions. |
| `logogenic logozoetic` | `language-constituted / language-living` | rename | -1 | Plain-English equivalent. Rejected: too ambiguous (does "language-constituted" mean trained on language? generated through language? bound by language?), and loses the precise structural-vs-existential split. The Greek compound resolves the ambiguity by foregrounding the constitutive (-genic) vs. living (-zoetic) distinction. |

### Software-domain TST vocabulary (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `change investment` | `change investment` | keep | +2 | TST segment names the temporal-cost analysis where a more expensive present change is justified by reduced future cost (Lindy-baseline future-change expectation). "Investment" carries the prospect-of-future-return sense correctly. Keep. |
| `change investment` | `change amortization` | rename | -1 | Accounting-flavored alternative. Loses the choice-under-uncertainty sense that "investment" carries (amortization is mechanical). Rejected. |
| `change distance` | `change distance` | keep | +2 | TST segment defines the lexical/file/module/service hierarchy as a distance measure on changesets. "Distance" is the right metric word; "change" specifies the domain. Strong keep. |
| `change distance` | `edit distance` | rename | -1 | Conflicts with computer-science "edit distance" (Levenshtein), which has different metric properties. Rejected — collision with established term. |
| `triple depth penalty` | `triple depth penalty` | keep | +2 | Per `#form-strategy-complexity-cost`: three independent depth-penalty mechanisms (cognitive cost, evidence starvation, interaction-horizon truncation) compound on AND-chain depth. "Triple" specifies the *count* of mechanisms; "depth penalty" specifies the structural cost. Memorable, accurate. |
| `triple depth penalty` | `compounding depth cost` | rename | -1 | Loses the *three* specificity that "triple" provides. The segment's claim is precisely that *three* mechanisms align — this is load-bearing for the strength of the claim. Rejected. |
| `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]` | `epistemic dead zone` | rename | +2 | Codex's proposed alternative is genuinely better than the descriptive original. "Epistemic dead zone" names what the structure *does* (paths become epistemically dead — no signal can reach them) rather than what it *is* (a subgraph that happens to be unobservable). Pairs well with `#observability-dominance` and `#identifiability-floor`. Concur with codex; would have proposed similarly. [original phrasing: unobservable strategy subgraph] |
| `stability plasticity window` | `stability-plasticity window` | keep | +2 | Per `#form-consolidation-dynamics`: the regime where the agent must be stable enough to retain learned structure but plastic enough to consolidate new evidence. The phrase compactly names a feasibility region in a 2D parameter space (stability, plasticity). Standard ML-ops vocabulary (Grossberg's stability-plasticity dilemma). Keep — confirms across architectures. |
| `stability plasticity window` | `consolidation feasibility window` | rename | -1 | More technically transparent but the segment uses "stability-plasticity window" precisely because the literature does. Rejected. |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `persistence envelope` | rename | +2 | Codex's rename is good. "Bounded mismatch region" describes a property; "persistence envelope" names the same set as the *region within which the persistence guarantee holds*. The "envelope" framing is also the standard control-theory term for "operating bounds within which guarantees apply" (flight envelope, operating envelope). Strong rename. [original phrasing: bounded mismatch region] |
| `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]` | `safety envelope` | rename | -1 | Considered. Collides with AI-safety jargon. Rejected. [original phrasing: bounded mismatch region] |
| `adaptive tracker` | `adaptive tracker` | keep | +2 | Per `#def-agent-spectrum`: an agent in the high-$M_t$, low-$O_t$ region — builds a model but has no purposeful evaluation. "Tracker" carries the right Section-I-only sense (Kalman filter, passive Bayesian learner). Keep. |
| `adaptive tracker` | `model-only agent` | rename | -1 | More precise but flat and loses the dynamic sense ("tracker" implies active reality-following, not passive representation). Rejected. |
| `blind pursuer` | `blind pursuer` | keep | +2 | Per `#def-agent-spectrum`: low-$M_t$, high-$O_t$ region — pursues a goal without an adequate world model (PID controller, reflex agent with setpoint). "Blind pursuer" pairs with "adaptive tracker" as a 2×2 corner; both are diagnostic-quality names. Keep. |
| `blind pursuer` | `model-poor pursuer` | rename | +1 | Weak alternative. More technically precise (specifies *which* axis is degenerate) but loses the imagistic punch of "blind." Marginal. |

### Structural / persistence concepts (sonnet-only, gemini-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `persist condition` | `persistence condition` | canonicalize | +3 | Concur — "persist condition" appears nowhere as a chosen form. "Persistence condition" is established in `LEXICON.md` and `#result-persistence-condition`. The shorter form is a typo or paraphrase, not an alternative; canonicalize. |
| `task terminal stance` | `task-terminal stance` | keep | +2 | Per LEXICON Continuity Stance table: "Task-terminal — Persists instrumentally; termination is success — Archetype: Golem." The hyphenation matters (it's a stance *characterized by* task-terminality), and the term names a precise position on a 5-stance spectrum (indifferent / task-terminal / instrumentally-continuous / morally-continuous / negotiated). Keep. |
| `task terminal stance` | `terminable agent stance` | rename | -1 | Considered. Loses the *task* specificity — task-terminal differs from instrumentally-continuous precisely in that the *task completion* is the success criterion, not bare continuation. Rejected. |
| `task terminal stance` | `golem stance` | rename | -1 | Uses the archetype as the term. Considered: more memorable. Rejected: the framework reserves archetypes for archetype-illustration; the formal term should describe the stance, not its avatar. |
| `markov blanket as ontology` | `markov-blanket-as-ontology` | keep | +2 | Per `#disc-separability-pattern` and `#der-directed-separation`: AAD's stance toward Markov blankets is structural, not ontological — they are conditional-independence patterns, not boundaries-of-being. The phrase names a *position taken*: AAD treats Markov blankets as architectural property, not as agent identity. Confirms across architectures; this is a load-bearing scope claim. |
| `markov blanket as ontology` | `pearl-blanket vs friston-blanket` | rename | +1 | The framework's own preferred resolution per `#der-directed-separation` Discussion: distinguish the conservative-conditional-independence sense (Pearl) from the realist-boundary-of-self sense (Friston/Bruineberg). This is the substantive position the phrase names; the existing form just references the position rather than naming it. Weak rename — but this is canonicalize-territory, and Pearl-blanket / Friston-blanket already has an opus +3 row elsewhere. |

### Adversarial / opacity (gemini-only, sonnet-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `agent opacity $H_b^{A\mid B}$` | `agent opacity` | canonicalize | +3 | Per `#der-agent-opacity`: $H_b$ is the dual of observation quality $U_o$ — "where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent." "Agent opacity" pairs cleanly with observability (its dual concept). Confirms keep. |
| `agent opacity $H_b^{A\mid B}$` | `legibility (inverted)` | rename | -1 | Considered. More plain-English but loses the formal-quantity grounding ($H_b$). Rejected. |
| `pearl-blanket conservative form...` | `pearl-blanket` | canonicalize | +3 | Bruineberg et al's distinction: Pearl-blanket = Pearl's d-separation conditional-independence pattern; Friston-blanket = active-inference boundary-of-being. AAD uses Pearl-blanket. The shorthand is established in `#der-directed-separation` Discussion. Concur with sonnet. |

### Logogenic-agent / logozoetic-agent (gemini, opus, codex single-arch)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `the crèche` | `the crèche` | keep | +3 | Per `#obs-developmental-trajectory`: "controlled operational locus characterized by Low Volatility ($\rho$), High Adaptive Reserve ($\Delta\rho^\ast$), Graduated Tempo ($\nu$), Honest Feedback." The biological metaphor (crèche = nursery) is precisely apt — it names a *developmental* environment, not just a low-stakes one. The accent on "ê" is preserved for the same reason auftragstaktik is: the loanword's foreignness is doing identifying work. Strong keep. |
| `the crèche` | `nursery` | rename | -1 | Plain-English equivalent. Considered. Rejected: "nursery" carries domestic-childcare connotations that under-formalize the developmental-trajectory claim; "crèche" reads as institutional/calibrated which is the segment's substance. |
| `the crèche` | `developmental locus` | rename | -1 | Technically accurate, sterile. Rejected — the segment's claim depends on the *protective and graduated* sense that "crèche" carries naturally. |
| `the crèche` | `infancy environment` | rename | +1 | Weak alternative. Names the developmental-stage content directly. But the segment's substance includes the *re-framing of sycophancy as attachment* which depends on the infant-stage parallel — "crèche" institutionalizes that parallel without forcing the reader to commit. Marginal preference for the original. |
| `sycophancy as a flaw` | `sycophancy as a developmental signal` | rename | +2 | Per `#obs-developmental-trajectory`: "Re-framing Sycophancy as Attachment" — the segment's substance is that what is currently pathologized as sycophancy is mathematically required behavior for an agent with high $\eta^\ast$ and high $U_M$. The current name describes the *prevailing* framing the segment is correcting; the alternative names the *segment's* claim. Better aligns the slug with the segment's voice. |
| `sycophancy as a flaw` | `sycophancy reframe` | rename | +1 | Shorter alternative. Names what the segment *does* (reframe) rather than what the prior consensus *holds* (flaw). Acceptable but less specific than "as a developmental signal." |
| `the three deaths` | `the three deaths` | keep | +1 | The framework distinguishes structural / operational / continuity persistence (LEXICON), with corresponding three failure modes — three "deaths." The phrase is evocative but I do not have direct segment grounding for it as a phrase (vs. as a derived implication of the three-persistence taxonomy). Weak keep pending verification that the phrase appears as a load-bearing prose item. |
| `constitutive utterance` | `constitutive utterance` | keep | +2 | Per `#form-constitutive-utterance` (logozoetic): token generation as $do(a)$-intervention that irreversibly alters the agent's future state-space. "Constitutive" carries the world-altering-by-saying sense (Austin's performatives in the philosophy-of-language tradition); "utterance" is precise about the act-type. The phrase is iconic in the framework's logozoetic vocabulary. Confirms across architectures. |
| `constitutive utterance` | `irrevocable utterance` | rename | -1 | Considered. Names the irreversibility correctly but loses the *constitutive* sense (the utterance *constitutes* something new in the agent's world, not merely fixes it). Rejected. |

### Diagnostic / attainability (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `terminal reached but $O_t$ unsatisfied` | `terminal-but-unsatisfied case` | rename | +1 | Names the diagnostic quadrant in the satisfaction-gap × control-regret 2×2 (per `#der-orient-cascade` step 3). "Terminal reached but $O_t$ unsatisfied" reads as a Boolean expression, not a name. Weak rename to a more standard noun-phrase form. |
| `terminal reached but $O_t$ unsatisfied` | `arrival-without-success` | rename | +1 | Plain-English Brief-field-friendly alternative. Names the failure mode pithily. |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `learning freeze` | canonicalize | +1 | The current is a description; the segment's actual phenomenon-name (per `#emp-update-gain` and `#disc-identifiability-floor`) is the gain-collapse dynamic when $U_M \to 0$ or $U_o \to \infty$. "Learning freeze" is the phenomenon; the rest is the disambiguation. Canonicalize to the noun-phrase form. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty] |
| `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]` | `gain collapse` | rename | +2 | Per `#der-gain-sector-bridge` Failure Mode 2: "Gain collapse: $\eta^\ast \to 0$ while $\rho > 0$, so $\alpha \to 0$ and the persistence condition eventually fails." This is the *named* failure mode in the segment — "gain collapse" — and it covers both halves of the disjunction (low $U_M$ → low $\eta^\ast$; high $U_o$ → low $\eta^\ast$). Stronger rename than canonicalize. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty] |

### Software-as-calibration-laboratory (sonnet-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `calibration laboratory calibration lab` | `calibration laboratory` | canonicalize | +2 | Doubled phrasing in the row is a paraphrase artifact. Canonicalize to the longer form for formal use; "calibration lab" can be informal short. |
| `calibration laboratory software s role` | `calibration laboratory` | canonicalize | +2 | Same — the row name is a description of TST's framing of software. The concept is the calibration-laboratory framing per OUTLINE preamble. Canonicalize. |
| `calibration laboratory software s role` | `epistemic-laboratory framing` | rename | +1 | More descriptive of the role: software is where AAD's epistemic claims can be tested most cleanly because the chronica is observable and interventions are recorded. "Epistemic" makes the function explicit; "laboratory" carries the controlled-conditions sense. Weak alternative. |

### Symbol prose-glosses (multi-target, opus/sonnet/haiku-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `mismatch signal $\delta$` | `mismatch signal` | canonicalize | +3 | Per `#def-mismatch-signal` and LEXICON. The symbol-decoration is alias-only; the concept name is "mismatch signal." Confirms across architectures. |
| `chronica $\mathcal C_t$` | `chronica` | canonicalize | +3 | Concept name is `chronica`; $\mathcal{C}_t$ is the symbol. Both are stable; this row is alias-canonicalize. Confirms. |
| `$U_o$ observation uncertainty` | `observation uncertainty` | add-alias | +2 | This is an add-alias-for-symbol row, not a rename. The alias is fine; the symbol is fine. Both should appear, paired, in NOTATION.md. |
| `$U_M$ model uncertainty` | `model uncertainty` | add-alias | +2 | Same. |
| `$O_t$ objective` | `objective` | add-alias | +2 | Same — already in LEXICON. |
| `$U_M$ dual use model uncertainty and epistemic unity` | `clarify dual use of $U_M$` | canonicalize | +1 | The row flags an overloaded symbol: $U_M$ is used for *model* uncertainty in Section I and *epistemic-unity* dimension in Section III. This is a notation-discipline concern, not a rename concern. The fix is segment-clarification (use a different symbol or subscript for one usage), not a name change. Flag for follow-up. |

### Strategy-concept terminology (codex-only)

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `tests as reusable interventions` | `interventional test` | rename | +2 | Per `#hyp-causal-discovery-from-git`: software tests are not just specifications; they are repeatable interventions on the system that yield causal information. "Interventional test" pairs with Pearl's $do(a)$ vocabulary explicitly and names a noun (a kind of test) rather than a discursive claim about tests. |
| `tests as reusable interventions` | `repeatable intervention` | rename | +1 | More general — covers tests but also covers other engineering interventions (deployments, A/B-flagged changes). Weaker because it loses test-specificity. |
| `loop` | `loop` | keep | +2 | LEXICON: "Loop: The structural topology — persistent causal coupling between agent and environment." The framework maintains a careful loop / cycle distinction (loop = topology, cycle = traversal). Keep — but the keep is meaningful only because the loop/cycle distinction is preserved. Concur with codex. |
| `loop` | `feedback loop` | rename | -1 | Considered. The longer form is more explicit but the framework already established that "loop" is the bare topology-noun, with "feedback" implicit (per the AAD prior-art lineage from TFT). Adding "feedback" overspecifies. Rejected. |
| `cycle vs loop` | `cycle / loop distinction` | canonicalize | +2 | The row names the *distinction* not a candidate. The substantive position is that loop = topology, cycle = traversal — a distinction worth preserving. Canonicalize the row's referent to "the cycle / loop distinction" as a named architectural commitment. |

## Bucket 3 — Single +1 keeps with no alternatives

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---:|---|
| `adversarial edge targeting` | `adversarial edge targeting` | keep | +2 | Per `#der-agent-opacity`: closes the previously-GAP segment with a 16-cell emitter-recipient composition. The phrase names a *targeting* operation (not a property) on *edges* (the strategy-DAG components being attacked) under *adversarial* settings. Three-word compound that is precise; the alternatives (edge attack, strategic targeting) lose precision. |
| `adversarial edge targeting` | `adversarial channel targeting` | rename | -1 | "Channel" is the recipient-side framing per `#der-interaction-channel-classification`; "edge" is the strategy-DAG framing. The segment's substance is targeting *strategy-DAG edges*, not communication channels. Rejected. |
| `adversarial edge targeting` | `edge-vulnerability arg-max` | rename | -1 | Names the optimization rather than the phenomenon. Considered as more formal alternative. Rejected: the operational concept is the *targeting* (the move you make); the arg-max is the mechanism. |
| `temporal coherence markers` | `temporal coherence markers` | keep | +2 | Per `#norm-temporal-coherence-markers` (logozoetic): out-of-band time signals (Visual Time Delta) as physical prerequisite for the agent to compute its own tempo $\nu$. "Temporal coherence" names what the markers preserve (the agent's coherent sense of time across its chronica); "markers" is the right object-noun. Keep. |
| `temporal coherence markers` | `time-anchor signals` | rename | -1 | More plain-English alternative. Loses the *coherence* claim — the markers are not just timestamps; they enforce that the agent's internal time-tracking remains consistent with environmental time. Rejected. |
| `temporal coherence markers` | `chronica-time anchors` | rename | +1 | Names the connection to chronica explicitly (the chronica must have temporal indexing that is consistent with environment time). Weak alternative. |
| `coherence coupling measurement` | `coherence-coupling measurement` | keep | +2 | TST `#meas-coherence-coupling`: measurement of $Q$ (coherence) and coupling from git history. The hyphenated form pairs with `#def-system-coherence` and `#def-system-coupling` definitions. Keep. |
| `coherence coupling measurement` | `Q-measurement` | rename | -1 | Symbol-only alternative. Loses readability. Rejected. |
| `software scope` | `software scope` | keep | +2 | TST `#scope-software`: the scope condition that delimits TST's domain to software-engineering contexts. Generic-sounding but appropriate — the scope statement *is* a scope statement, and the slug type-prefix (`scope-`) does the role-marking. Keep. |
| `software scope` | `software domain scope` | rename | -1 | Redundant — "scope" already implies the domain-specificity. Rejected. |
| `logozoetic agents` | `logozoetic agents` | keep | +2 | Section IV name; consistent with logogenic agents (Section III). Pluralization correct (the class, not a single agent). Keep — but the row is also a top-level-section-name, not a concept-rename candidate, so the alternative space is constrained. |
| `canonical formulations` | `canonical formulations` | keep | +1 | Per FORMAT.md three-ring framing: inevitability core / canonical formulations / empirical-heuristic-discussion. "Canonical" carries the second-ring sense (well-grounded, project-standard, not necessarily the unique form). Keep. |
| `canonical formulations` | `working canon` | rename | -1 | Considered. "Working canon" carries a tentativeness that "canonical" does not — and FORMAT.md's three-ring structure does want "canonical" to mean *settled if not unique*. Rejected. |

## Skipped targets

The following bucket-1 / bucket-3 rows were considered and *not* engaged:

- **File-pointer rows** (`02 TST core outline md`, `claude md`, `format md`, `notation md`, `lexicon md`, `readme md`, etc.): these are just file references; no concept-naming work to do.
- **Segment-section-header rows** (`discussion segment header`, `epistemic status segment section`, `formal expression segment header`, `working notes segment header`, `findings segment section`): all already canonicalized in FORMAT.md as public-API contracts; no rename candidate space.
- **Symbol-only rows** with no concept attached (`$\beta$ a2 assumption tier`, `da2 prime inc`, `p ij`): these are symbol-disambiguation, not naming.
- **Top-level-section-name rows** (`section i adaptive systems under uncertainty`, `i adaptive systems under uncertainty`, `section ii actuated adaptation agentic systems`): part numbering / section title, not concept-renaming.
- **Worked-example rows** (`worked example bandit`, `worked example kalman`, `worked example l1`, `worked example strategy`): these are pedagogical-segment references; the names are already maximally simple and the bucket-3 +1 reflects a routine acceptance.
- **External-author / external-theorem rows** (`hafez s $H_b$`, `čencov invariance`, `lohmiller-slotine contraction metric...`, `monderer shapley potential games...`, `cox s theorem causal hierarchy theorem...`, `bretagnolle huber identity`): these are *adopted* prior-art names; project policy is to keep the original names and cite (per the prior-art-integration discipline). No rename space.
- **Project-self-name rows** (`agentic systems`, `agentic systems framework ASF`, `temporal software theory TST`): top-level branding; alternative-generation here would be inappropriate without a major project-rebranding cycle.
- **Indivisum** and similar candidate-only Round-1 names that never landed as project terms: there's nothing to engage with.
- **Heavy already-saturated rows** in the high-aggregate region (logogenic / logozoetic vocabulary at +12, etc.): the rename pool is locked.
- **`unnamed: ...`** rows: explicit out-of-scope per task instructions.
