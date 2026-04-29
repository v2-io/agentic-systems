# Naming Votes — Opus 4.7 (1M context), second run ("b")

**Model:** `claude-opus-4-7[1m]`, second independent pass (hence the `-b` suffix).

**Approach:** Surveyed `CLAUDE.md`, `OUTLINE.md`, `01-aad-core/OUTLINE.md`, `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `README.md`, `TODO.md`, `PROPOSALS.md`, and sampled a dozen segments in `01-aad-core/src/` (with focus on the three meta-segments, the template segments, the 2026-04-24 landings, and the directed-separation / agent-identity / strategic-composition cluster). Vote organized topically rather than alphabetically — strong keeps first, then three-part meta-architecture, then overloaded-word triage, then cryptic symbols, then slug relics and clinical slugs, then Section II / III / Appendix passes, then unnamed-thing proposals, then document-level and section-header passes.

**Disclosure (read before using this vote).** The cold-start instruction said *do not read* `msc/naming/naming-brainstorm-2026-04-24.md`, but that file showed in `git status` as modified and I skimmed it while orienting before I had fully read the principles document. The contamination is real and I cannot fully un-see it. I have tried to (a) generate my votes from direct review of the primary source files rather than from recall of the brainstorm, (b) push actively *against* the brainstorm's proposals to test whether my agreement is independent or anchored, and (c) flag in the `notes` column where I am confident my reasoning is primary vs. where the brainstorm likely influenced my framing. For aggregation purposes treat this vote as "semi-independent, leaning-toward-primary" — not fully cold-start. I logged this as a principles-observation too (see end).

**Calibration note:** I am generally stingy with +3; reserving it for cases where I judge the name either load-bearing-and-working or actively misleading. The weight distribution below is roughly +1 dominant, with a minority of +3 at the poles and several −1 rejections of plausible-but-wrong alternatives.

---

## Votes

### Explicit keeps — names that are doing real work

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| satisfaction gap | satisfaction gap | +3 | The 2×2 diagnostic composes with *control regret* into a cognitive apparatus the reader assembles in one exposure. Do not touch either half. The axes are *evocatively and accurately* named — a rare pairing. |
| control regret | control regret | +3 | Pairs with *satisfaction gap*. "Regret" imports RL baggage that is genuinely load-bearing (regret = best-achievable − current); "control" narrows it to the attainability layer. |
| chronica ($\mathcal C_t$) | chronica | +3 | Greek root fits AAD's philosophical-vocabulary register, the symbol avoids colliding with $\mathcal H$ (entropy), and the singular-non-forkable-trajectory commitment of `#agent-identity` gets more morally heavy over time — "chronica" will age toward the logozoetic scope rather than away from it. Keep. |
| orient cascade | orient cascade | +3 | Names both the structure (cascade = ordered resolution) and the heritage (Boyd's *Orient* of OODA) without being captured by OODA. Only other live candidate I considered was "orientation sequence" — flatter, weaker, rejected. |
| adaptive reserve ($\Delta\rho^\ast$) | adaptive reserve | +3 | Mechanical-engineering intuition ("shock reserve" / "crumple zone") fits exactly what the quantity measures. The two-word compound lands on the first read. |
| update gain ($\eta^\ast$) | update gain | +3 | Adopted from Kalman / control; baggage transfers *correctly*. "Gain" in AAD plays the role the reader expects — AAD is not being cute. |
| directed separation | directed separation | +3 | Zero pre-existing meaning in ML; the two words ("directed" = asymmetric information flow; "separation" = independence in the update) are both load-bearing. The only collision risk is control theory's *separation principle*, which is actually a Class-1 *consequence* of directed separation — the echo is informative, not misleading. Keep. |
| logogenic / logozoetic | logogenic / logozoetic | +3 | Deliberate neologisms holding reserved memorable-noun slots. The slight learning cost is paid once and then these words own the conceptual slot permanently — which is exactly what a framework-defining class deserves. |
| auftragstaktik | auftragstaktik | +3 | Imports a load-bearing operational concept from a specific tradition; the name carries genuine conceptual freight that "mission-command" cannot replace without loss. The spelling cost is the tell that the word is doing work. |
| aporia / prolepsis / aisthesis / epistrophe / praxis | *(keep as a set)* | +3 | The Greek cycle-phase vocabulary works *because* it refuses the flatness of "predict / observe / mismatch / update / act." The README §"Why these terms earn their weight" is load-bearing justification and should not be touched. Keep all five. |
| identifiability floor | identifiability floor | +3 | "Floor" is the right geometric metaphor — the no-go is a *floor you can't go below without outside help*, and the machinery that escapes it is named relative to it. One of the best meta-segment names in the project. |
| agent opacity ($H_b^{A\mid B}$) | agent opacity | +3 | "Opacity" as the informational dual of observability is exactly right — the word carries the right intuition (unpredictable-to-observer) and doesn't collide with anything else in AAD. Hafez's $H_b$ gets an AAD-native prose handle. |
| strategy DAG ($\Sigma_t$) | strategy DAG | +3 | Adopted directly from the graphical-models literature; "DAG" is pronounceable as a noun and carries precisely the right structural picture. Keep. |
| information bottleneck | information bottleneck | +3 | Adopted from Tishby et al. — do not rename adopted concepts (prior-art-integration convention). The word *bottleneck* is doing real explanatory work; the baggage transfers. |
| mismatch signal ($\delta_t$) | mismatch signal | +1 | Good; "mismatch" is deliberately flatter than "error" (which presupposes the agent was wrong — see README §Aporia) while the formalism uses "aporia" as the *philosophical* name. Two-register vocabulary is correct here. Keep. |
| sector condition | sector condition | +3 | Adopted from Khalil / Vidyasagar nonlinear control; baggage is correct. Non-negotiable per prior-art-integration convention. |
| adaptive tempo ($\mathcal T$) | adaptive tempo | +3 | "Tempo" is the rare noun that carries both *rate* and *quality* simultaneously, which is exactly what $\mathcal T = \sum \nu^{(k)} \eta^{(k)\ast}$ is. The word is underused in the ML literature, which is an advantage — AAD can own it. |
| composition closure / closure defect ($\varepsilon^\ast$) | composition closure / closure defect | +1 | "Closure" as the algebraic term lands well here and the engineering-flavored "defect" reads cleanly as the gap. The one collision risk is CS closures (lexical scopes), but disambiguation by context is cheap. No rename. |

### The three-part meta-architecture — `#identifiability-floor`, `#separability-pattern`, `#additive-coordinate-forcing`

These three meta-segments carry CLAUDE.md §7's "epistemic architecture" load. Taken together they deserve matched memorability. `#identifiability-floor` already has a strong noun; the other two do not.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#additive-coordinate-forcing` | `#forced-coordinates` | +3 | The current name has two problems: (i) it's *additive-only*, which was honest when the meta-segment covered three Cauchy-FE instances, but is now factually under-inclusive since the Čencov / Fisher-metric 4th primary instance is not log-additive — the segment itself acknowledges this and floats `#uniqueness-coordinate-forcing` as a possible rename; (ii) five-syllable hyphen-compound is not a name anyone reaches for in conversation. "Forced coordinates" is the concept in two short words: the coordinate is *forced* by a uniqueness theorem operating on an AAD-internally-motivated axiom. Covers both Cauchy-FE and Čencov mechanisms. Preserves the pattern's content (1 anchor + 3 theorems, with Lyapunov / IB as adjacent). |
| `#additive-coordinate-forcing` | `#cauchy-coordinates` | -1 | Short, crisp, memorable — but actively misleading now that the Čencov instance is part of the primary four. "Cauchy" undersells the metric-layer instance and risks calcifying the meta-segment in a form it has already grown past. Reject. |
| `#additive-coordinate-forcing` | `#coordinate-forcing` | +1 | Verb-form alternative; acceptable fallback if `#forced-coordinates` doesn't land. Same argument, slightly more clinical. |
| `#additive-coordinate-forcing` | `#uniqueness-coordinates` | +1 | Closer to the mechanism ("uniqueness theorem forces coordinate"); loses a little crispness compared to `#forced-coordinates`. Second-choice. |
| `#separability-pattern` | `#separability-ladder` | +3 | The meta-segment's own structure is a seven-row *ladder* (separable-core → structured-repair → general-open across seven axes of increasing difficulty). "Ladder" is the geometry the content actually has; "pattern" is inert filler that describes no content. Pairs mnemonically with `#identifiability-floor` ("the ladder above the floor"). The brainstorm converges here; I arrived independently on the same reasoning (from reading the seven-row table) before cross-checking. |
| `#separability-pattern` | `#separability-staircase` | -1 | Whimsical; the word "staircase" doesn't carry the increasing-difficulty semantics as cleanly as "ladder" (staircases are uniform; ladders intuitively get harder toward the top). Reject. |
| `#identifiability-floor` | `#identifiability-floor` | +3 | Explicit keep. Named best of the three meta-segments; the geometric metaphor ("floor you can't cross without information augmentation") is exactly load-bearing. Together with the above two proposed renames: **floor / ladder / forced-coordinates** reads as a trio of concrete mental pictures — one of AAD's highest-leverage naming opportunities if all three land together. |
| [the trio collectively] | epistemic architecture | +1 | Use "epistemic architecture" as the CLAUDE.md §7 / OUTLINE.md framing phrase, not as a segment. A fourth meta-segment named `#epistemic-architecture` would double-count and is not warranted. Keep as framing language. |

### Overloaded-word triage

Three words in AAD are doing too many jobs; one is outright collision, the others are under tension.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| convention hierarchy (C1/C2/C3) | continuation hierarchy | +1 | "Convention" collides with the game-theory / Lewis sense (social conventions, conventions-as-equilibrium-selection), which is a *different* and unrelated concept that some AAD readers will have strongly in mind. What the C-hierarchy actually indexes is the choice of *continuation policy* for value-object evaluation (one-step, receding-horizon, Bellman). "Continuation hierarchy" is self-announcing; the C1/C2/C3 abbreviations still work, and since they map to continuation it even becomes a mild mnemonic. Risk is churn. Mild preference but not forceful. |
| convention hierarchy | evaluation hierarchy | -1 | Considered and rejected — too generic; hides the *policy* choice that's the actual axis. |
| correlation hierarchy (L0/L1/L1'/L2) | correlation ladder | +1 | Pairs with the `#separability-ladder` rename if both are adopted. "Ladder" is the geometry (rungs of increasing difficulty: independence → strict prerequisite → soft facilitator → full joint). The "L0/L1/L1'/L2" abbreviations continue to work. Reduces the "hierarchy" overload in the project (currently: Pearl's causal hierarchy, convention, correlation, approximation-tiering-sometimes-called-hierarchy — four distinct uses). |
| L1' (L1-prime) | L1-observable / L1-soft | -1 | Considered renaming the prime-decoration to a word. Reject: L1' consistently refers to *soft-facilitator under observable common cause* (Prop B.7 five-way gating), but that's a mouthful and "L1-prime" is a three-syllable speakable token that the existing literature has absorbed. The prime notation is also structurally right — L1' is a *refinement* of L1, which is exactly what the prime signals in math. Keep. |
| "hierarchy" (project-wide) | *(reserve for Pearl's causal hierarchy + strict-asymmetric uses)* | +1 | Project-wide convention: use "hierarchy" only for Pearl's (external, adopted, immovable) and other strict-asymmetric orderings. Use "ladder," "partition," or "tier-set" for internal-to-AAD cases where "hierarchy" is currently doing duty. Not a rename of a specific segment — a working convention. |
| "strategic" in `#strategic-composition` | `#equilibrium-composition` | +3 | "Strategic" is already overloaded in AAD for all $\Sigma$-related things (strategy DAG, strategic calibration, strategic tempo). Using it for the *game-theoretic / partially-opposing-objectives* composition regime creates a false parallel — a fresh reader sees `#strategic-composition` next to `#strategic-tempo` and reasonably guesses "composition of strategy DAGs," which is wrong. The segment's core technical move is *equilibrium-convergence under Monderer-Shapley / Rosen conditions* — `#equilibrium-composition` says what the segment is. Strong preference; one of the cleanest overload-disambiguation moves available. |
| "strategic" in `#strategic-composition` | `#game-theoretic-composition` | +1 | Fallback alternative; accurate and self-announcing, but less tied to the segment's actual formal move (equilibrium convergence) than `#equilibrium-composition`. Acceptable if that name is rejected. |
| "persistence" (three senses: structural / operational / continuity) | *(keep three senses; sharpen usage sites)* | +1 | The three senses are load-bearing and correctly disambiguated in LEXICON.md. The *irreducibility* is fine — the three senses are genuinely related (they all concern "the agent sustains itself"). Usage-site discipline: every use of the bare word "persistence" in segments should be followed by the sense in parentheses on first use per segment, e.g. "(structural)". Not a rename; a writing convention. |

### Cryptic symbols that need English-prose equivalents

Symbols fine as shorthand but unreadable in running prose. The proposal is not to retire the symbols — it is to assign English names that can carry the concept in a sentence.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| $\alpha_1$ (A2' fixed-gain sub-scope) | derived-gain regime | +1 | "The Kalman case lands in $\alpha_1$" requires a decoder ring; "the Kalman case lands in the derived-gain regime" is self-contained. Symbol stays as shorthand; English owns the prose register. |
| $\alpha_2$ (A2' adaptive-gain sub-scope under (MG-1)–(MG-4)) | adaptive-gain regime | +1 | Same argument. "AMSGrad is an $\alpha_2$ result" reads terribly; "AMSGrad is an adaptive-gain result" lands. |
| $\beta$ (A2' sub-scope where A2' is assumed, not derived) | postulated-sector regime | +1 | Weakest of the three; "postulated" is a close enough match to AAD's "postulate" terminology that it signals the status correctly. Fallbacks: "assumed-sector regime" (mechanical) or "imposed-sector regime" (active). |
| A2' (operator-sector condition under fidelity-degraded updates) | — | -1 | Considered replacing "A2'" (the symbol for the sector condition itself) with an English name and rejected. A2' is how AAD *refers back to* Assumption A2 and its primed variant; it's functioning as a tag in the way GA-3 and P1 do, not as a concept to be named in prose. The English prose does the naming via "sector condition" already. Keep the symbol. |
| (PI) parameterization-invariance axiom | (PI) / parameterization invariance | +1 | The parenthesized-two-letter-tag convention works (compare GA-1, MG-1, P1). But the *full English phrase* "parameterization invariance" should be used on first mention in each segment before falling back to (PI). The four-primary-instances table in `#additive-coordinate-forcing` does this correctly; check that other citing segments follow suit. |
| $U_M$ / $U_O$ / $U_\Sigma$ (unity dimensions) | epistemic-unity / teleological-unity / strategic-unity | +1 | The symbol layer is fine but the word *unity* requires paraphrase on every encounter ("what is $U_O$ unity measuring?"). Define each in NOTATION.md with its full English name: $U_M$ = **epistemic unity** / $U_O$ = **teleological unity** / $U_\Sigma$ = **strategic unity**. Then "teleological unity crosses the threshold from below" reads without lookup where "$U_O$ crosses the threshold from below" does not. The Lexicon already has these English names — the move is to *use them* consistently in segments. |
| unity dimensions | coherence dimensions | -1 | Considered renaming the *concept* from "unity" to "coherence." Reject: *coherence* is already used informally elsewhere (strategic coherence, epistemic coherence) and a rename would bleed. *Unity* is narrower and actually works once each dimension is named per above. |
| $\varepsilon^\ast$ (closure defect) | closure defect | +1 | The English prose name is fine; the asterisk is doing "optimum-over-admissible-projections" work that the bare $\varepsilon$ doesn't. Keep symbol; ensure segments using it say "closure defect" in prose, not "epsilon-star". |
| $\eta^\ast$ (optimal update gain) | update gain | +1 | See keep above. Prose: "update gain" in running text; $\eta^\ast$ only in formal expressions. |
| $C$ (bias-bound constant in `#bias-bound-derivation`) | bias-bound constant | +1 | Single-letter $C$ is unfortunate (collides with "chronica" symbol and the notion of "convention C-hierarchy"). Can't easily rename the symbol (it's embedded in the bound expression), but the English "bias-bound constant" should always accompany it in prose. More pointedly: the segment uses $C_{W_2}$ and $C_{FR}$ for the two derived forms — *these two tracked forms are fine*; the unqualified $C$ is the problematic one. |
| $\kappa_{\text{processing}}$ (Class-2 processing coupling) | processing coupling | +1 | "Processing coupling" in prose; $\kappa_{\text{processing}}$ in formalism. The "processing" suffix is doing work — without it the symbol is ambiguous with the earlier κ-as-scalar framing that got retired. Keep symbol, use English in prose. |

### Slug relics from the ACT → AAD rename (2026-04-16)

Two segment slugs still carry the old `-act-agent` suffix. The "act" here refers to ACT (Agentic Cycle Theory), the predecessor framework name, not the English verb. Every future reader will parse them wrong at first read.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#developer-as-act-agent` (TST) | `#developer-as-adaptive-agent` | +3 | The slug is a direct relic of the pre-2026-04-16 "ACT" framework naming — no longer accurate. "Adaptive agent" matches LEXICON's agent-class vocabulary and is framework-rename-proof. The segment invokes Section I machinery, so "adaptive" is semantically correct. This is mechanical cleanup overdue since April. |
| `#developer-as-act-agent` | `#developer-as-aad-agent` | -1 | Considered preserving the exact-parallel naming. Reject: embedding a framework acronym in a slug is exactly the rot pattern we just cleaned up; don't re-introduce it. |
| `#ai-agent-as-act-agent` (logogenic) | `#ai-agent-as-adaptive-agent` | +3 | Same argument. Matches `#developer-as-adaptive-agent`; the parallel structure (two domain instantiations of "adaptive agent") is itself a pedagogical payoff. |
| `#ai-agent-as-act-agent` | `#logogenic-agent-mapping` | -1 | Considered reframing as a *mapping* rather than an *is-a*. Reject: the segment is the is-a, not the mapping; conflating the two in the rename would narrow the segment's scope. |

### Section II slugs — clinical where memorable was possible

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#complete-agent-state` | `#complete-agent-state` | +1 | Keep. "Complete" is load-bearing (distinguishes $X_t = (M_t, G_t)$ from the epistemic-only substate $M_t$); the slug describes itself. |
| `#strategy-dimension` | `#strategy-dimension` | -1 | Considered renaming to `#purposeful-substate-split` but that's worse. Keep. The slug covers the $G_t = (O_t, \Sigma_t)$ decomposition; "dimension" is fine. |
| `#causal-hierarchy-requirement` | `#causal-hierarchy-requirement` | +1 | Keep. Direct application of Bareinboim et al.'s CHT to $Q_O$ evaluation; "requirement" signals this is a must-have, not an option. |
| `#loop-interventional-access` | `#loop-interventional-access` | +3 | Keep. The phrase *loop-interventional-access* lands in one read and the concept ("the feedback loop provides Level-2 data by construction") has no shorter form without loss. Reader-friendly. |
| `#causal-insufficiency-detection` | `#latent-cause-detection` | +1 | Current slug names the *problem* being detected ("causal insufficiency"); "latent-cause-detection" names what a reader mentally pictures (finding hidden common causes). Marginal preference. Weak. |
| `#causal-insufficiency-detection` | `#causal-insufficiency-detection` | +1 | Alternative vote: keep. "Causal insufficiency" is Pearl's own term; the prior-art-integration convention argues to keep it. This argument slightly outweighs the legibility gain of `#latent-cause-detection` for me — so on balance I'd actually keep the current form. Net: weak keep. |
| `#edge-update-natural-parameter` | `#log-odds-update` | +1 | The segment's content is "log-odds is the unique additive-evidence coordinate for edge credences under evidential additivity (Cauchy-FE)." The current slug ("natural parameter") leans on exponential-family vocabulary that the segment derives *to*, not from. `#log-odds-update` names the derived coordinate and is shorter; "natural parameter" can live in the subtitle. Modest preference. |
| `#edge-update-via-gain` | `#edge-update-via-gain` | +1 | Keep — the slug clearly frames this as "extend the gain principle from state to strategy edges," which is the segment's hypothesis. |
| `#structural-change-as-parametric-limit` | `#structural-change-as-parametric-limit` | -1 | Considered shortening to `#structural-as-parametric-limit` or `#structural-to-parametric-limit`. Reject: "change" is load-bearing (the segment is about pruning/grafting *changes* to the DAG, not about the DAG states). Keep. |
| `#exploit-explore-deliberate` | `#exploit-explore-deliberate` | +3 | Keep. The three-way extension of the classic exploit-explore dichotomy reads as a natural extension *because* of how the slug is named. Changing this would cost the pedagogical payoff. |
| `#credit-assignment-boundary` | `#credit-assignment-boundary` | +1 | Keep. The "boundary" is semantically exactly what the segment delimits (tractable vs. intractable credit-assignment regions). |
| `#agent-spectrum` | `#agent-spectrum` | +1 | Keep. "±model × ±objective quadrants" — "spectrum" is an acceptable word for a 2×2 partition if one is feeling generous. Alternative: `#agent-types-partition`, but that's worse. |
| `#strategy-persistence-schema` | `#strategy-persistence-schema` | +1 | Keep. "Schema" is the AAD-preferred word for "proposed structural shape awaiting formal instantiation" (it's in the FORMAT.md `type:` taxonomy). Honest about status. |
| `#and-or-scope` | `#and-or-scope` | +1 | Keep. The slug is short, announces the formalism restriction ("AND/OR only"), and is directly cite-able. |
| `#observability-dominance` | `#observability-dominance` | +1 | Keep. "Dominance" here is informational dominance — the gain principle *dominates* the edge update when observability is low. Does its job. |

### Section III slugs — mixed

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#composition-scope-condition` | `#composition-scope-condition` | +1 | Keep. Honest, direct. |
| `#directed-separation-under-composition` | `#composite-directed-separation` | +1 | Shorter; reads as "directed separation applied to composites" without the "under-composition" preposition phrase. Weak preference; no strong opinion. |
| `#symbiogenic-composition` | `#symbiogenic-composition` | +3 | Keep. "Symbiogenic" is the exactly-right biological term for "one agent integrating another that formerly had its own autonomy"; the $U_O$-crosses-threshold-from-below mechanism matches the biological meaning with precision. Rare case where an adopted term upgrades the reader's intuition about the formalism. |
| `#auftragstaktik-principle` | `#auftragstaktik` (drop "principle") | -1 | Considered dropping "principle" since the word alone is vivid. Reject: "principle" signals this is a design prescription not a derived result, and AAD's scope-honesty discipline rewards that signal. Keep as is. |
| `#team-persistence` | `#team-persistence` | +1 | Keep. Good plain English for what the derivation is ("cooperative composite sector condition"). |
| `#adversarial-destabilization` | `#adversarial-destabilization` | +1 | Keep. Direct, punchy; the word "destabilization" signals the direction (outward from the bounded region) rather than something neutral like "dynamics." |
| `#interaction-channel-classification` | `#recipient-regime-classification` | +1 | The segment's headline is the *recipient-side* four-regime classification (Informative / magnitude-shock / structural-shock / ambient-noise); the current slug buries the recipient-side framing under "interaction channel." Weak preference for the recipient-explicit form. |
| `#interaction-channel-classification` | `#interaction-channel-classification` | +1 | Alternative: keep. "Interaction channel" keeps the symmetry with `#agent-opacity`'s emitter-side four-regime classification; the recipient-side structure is one half of a pair. On balance this consideration outweighs the legibility gain. Net: weak keep. |
| `#unity-dimensions` | `#coherence-dimensions` | -1 | Considered. Reject for the same reason as the symbol-level `U_M`/`U_O`/`U_\Sigma` consideration above — coherence is already doing soft duty elsewhere. Keep `#unity-dimensions`. |
| `#unity-closure-mapping` | `#unity-closure-mapping` | +1 | Keep. The segment's content *is* the mapping between unity (multi-dimensional) and closure (scalar) — the slug is honest. |
| `#communication-gain` | `#communication-gain` | +3 | Keep. Exact analog of "update gain" for inter-agent channels — the parallel structure is itself pedagogical. |
| `#adversarial-edge-targeting` | `#adversarial-edge-targeting` | +1 | Keep (even though the segment is currently a GAP — the slug is reserving a memorable-noun slot). "Edge targeting" is vivid; the attacker aims *at specific edges* of the opponent's strategy DAG. |
| `#per-dimension-persistence` | `#weakest-link-persistence` | +1 | Current slug is descriptive but inert; the actual content is "the persistence condition binds at the weakest dimension." "Weakest link" makes the engineering intuition land in one read. Modest preference. |
| `#adversarial-tempo-advantage` | `#adversarial-tempo-advantage` | +1 | Keep. Descriptive, direct, doesn't need to be shorter. |

### Appendix slugs — mostly workmanlike; a few upgrade opportunities

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#sector-persistence-template` | `#sector-persistence-template` | +1 | Keep. "Template" is the correct AAD term (a parameter-free shared-lemma pattern that multiple results instantiate). Clinical but apt. |
| `#contraction-template` | `#contraction-template` | +1 | Keep. Parallel to `#sector-persistence-template` — the family-by-pattern naming is consistent. |
| `#critical-mass-composition` | `#critical-mass-composition` | +3 | Keep. "Critical mass" is exactly right — the composite-sector-constant derivation has a minimum-viable-composition threshold that matches the physics / sociology intuition. Rare case where the name upgrades the result's punch. |
| `#persistence-cost` | `#persistence-cost` | +1 | Keep. Short, accurate (information-rate *cost* to maintain the persistence bound). |
| `#detection-latency` | `#detection-latency` | +3 | Keep. Two words that fit the result ($\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$) perfectly. |
| `#consolidation-dynamics` | `#consolidation-dynamics` | +1 | Keep. "Consolidation" imports the neuroscience baggage (memory consolidation, stability-plasticity) that's precisely what the segment is formalizing. |
| `#adaptive-gain-dynamics` | `#adaptive-gain-dynamics` | +1 | Keep. Direct; parallel to `#consolidation-dynamics`. |
| `#bias-bound-derivation` | `#class-2-bias-bound` | +1 | Current slug is generic — many things in AAD are "bias bound derivations." The segment specifically derives the constant $C$ in the **Class-2 observation-ambiguity** bias bound. Scoping the slug to "class-2" makes it findable and distinct. |
| `#fisher-whitened-update-rule` | `#fisher-whitened-update-rule` | +1 | Keep. The Fisher-whitening mechanism is the segment's headline; "update rule" grounds it in the AAD update vocabulary. |
| `#l1-update-bias` | `#l1-update-bias` | +1 | Keep. "L1" is AAD's own correlation-hierarchy label; the slug is self-locating. If the correlation-hierarchy rename to `#correlation-ladder` lands, revisit (the "L1" abbreviation survives, so no cascade). |
| `#variational-sector-condition` | `#variational-sector-condition` | +1 | Keep. |
| `#graph-structure-uniqueness` | `#strategy-dag-uniqueness` | +1 | The current slug is somewhat generic ("graph structure" — which graph?). The segment's content is specifically the DAG-with-Markov-property uniqueness for the strategy layer ($\Sigma_t$). Scoping the slug to strategy-DAG makes it findable and binds it to the concept it's about. Modest preference. |
| `#strategic-dynamics-derivation` | `#strategy-edge-dynamics` | +1 | Current slug overloads "strategic" (again — see §overloaded-words). The derivation is specifically about *edge* dynamics; naming that makes the segment about what it's actually about. |
| `#approximation-tiering` | `#approximation-tiering` | +1 | Keep. Already avoids the "hierarchy" overload; "tiering" is the right word. |
| `#compression-operations` | `#compression-operations` | +1 | Keep. Plural "operations" correctly signals this is a family ($M_t$, $G_t^{\text{shared}}$, $\Sigma_t$, $\Lambda$). |
| `#independence-audit` | `#independence-audit` | +1 | Keep. "Audit" is the right engineering register — the segment enumerates six load-bearing independence assumptions and their failure regimes. |
| `#linear-ode-approximation` | `#linear-ode-approximation` | +1 | Keep. Honest — the segment is the *pedagogical* linear ODE; "approximation" signals this is a simplification used for exposition. |
| `#discrete-sector-condition` | `#discrete-sector-condition` | +1 | Keep. Direct analog of `#sector-condition-stability` for discrete time. |
| `#recursive-update-derivation` / `#gain-sector-derivation` | *(standardize as `-derivation` suffix for derivation-type appendices)* | +1 | Observation: the `-derivation` suffix on appendix segments is a good AAD convention (distinguishes derivation segments from stating segments). Enforce consistently. |

### Unnamed things that deserve names — memorable-noun opportunities

These are the highest-leverage rows in the vote. Each names a *concept that AAD uses repeatedly* without a short handle, forcing paraphrase every time. Naming them opens new memorable-noun slots that don't exist yet.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| [concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | persistence envelope | +3 | The bounded region where $\alpha R > \rho$ holds — currently referenced as "the region where the persistence condition holds" or "the adaptive regime." Engineering vocabulary has an exact match: *envelope* (as in flight envelope). "The agent is well inside its persistence envelope" / "the adversarial agent is pushing $B$'s persistence envelope" read with zero paraphrase. This is AAD's single most-used-without-a-name concept. [original phrasing: unnamed: the region in parameter space where sector-persistence holds] |
| [concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | adaptive basin | -1 | Considered. Reject: "basin" is already mathematically loaded (basin of attraction), and AAD's region *is a basin of attraction* — using the word would either (i) be redundant with dynamical-systems vocabulary, or (ii) force AAD to formally justify "basin" at the derivation layer. Cleaner to reserve "basin" for the technical sense and use "envelope" for the prose handle. [original phrasing: unnamed: the persistence envelope] |
| [concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | chain anchor | +1 | Not a rename of the segment (`#chain-confidence-decay` keeps its slug) — a prose *handle* for the anchor's role in the `#additive-coordinate-forcing` / `#forced-coordinates` meta-pattern. "The update-layer analog of the chain anchor" / "the three theorem-layers reduce to the chain anchor under \_\_\_" read cleanly where "the `#chain-confidence-decay` segment in its role as the mathematical-identity anchor of the 1-anchor + 3-theorem pattern" does not. [original phrasing: unnamed: the chain-confidence-decay mathematical anchor as the 1 in "1-anchor + 3-theorem"] |
| [concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | anchor-theorem pattern | +1 | The `#forced-coordinates` meta-segment's shape (one mathematical identity + N theorems conditional on AAD-internal axioms). If the Fenchel-Bregman reframe (SP-9) lands differently this name is discardable; otherwise a crisp handle for the 4-instance structure is useful. [original phrasing: unnamed: the "1-anchor + 3-theorem" structure itself] |
| [unnamed: cascade of inferential force through C1/C2/C3] | inferential-force cascade | +1 | The pattern "under C1 diagnostics are weak, C2 they sharpen, C3 they're global" — currently explained in prose every time it comes up (which is several places). "Inferential-force cascade" gives the pattern a name. Mirrors `#orient-cascade` in structure (both cascades are ordered resolutions) and the parallel is pedagogically useful. |
| [concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole] | the adaptive pentad | +1 | The five-phase cycle (prolepsis → aisthesis → aporia → epistrophe → praxis) has a piecewise name per phase but no *collective* noun. "The cycle" works when context is clear but is ambiguous with (e.g.) credit cycles or OODA cycles. "The pentad" or "the adaptive pentad" is a specific collective noun that fits AAD's Greek-vocabulary commitment. Weak preference; aesthetic call. [original phrasing: unnamed: the cycle-as-a-whole] |
| [concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole] | the five-turn | -1 | Considered as a more Germanic / industrial alternative to "pentad." Reject: loses the Greek-vocabulary register and gains nothing. [original phrasing: unnamed: the cycle-as-a-whole] |
| [concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate] | calibration domain | +1 | CLAUDE.md §7 names TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measured exactly." The *concept* (a privileged domain for identification of a theoretical framework's quantities) is itself a reusable meta-move for any domain instantiation. "Calibration domain" names it. Low priority but opens a useful slot. [original phrasing: unnamed: the calibration-laboratory concept applied outside TST] |
| [unnamed: the "scope-honesty-as-architecture" working principle] | scope honesty / scope honesty as architecture | +1 | Already named in CLAUDE.md §7(a) as "scope-honesty-as-architecture." The phrase is workable; the shorter "scope honesty" does most of the prose work. Usage observation: use the short form in prose, the hyphenated form in CLAUDE.md-register discussions of the element itself. |
| [unnamed: the A2' sub-scope partition collectively] | A2' partition | +1 | Not a symbol rename; a prose handle for the three-way α₁/α₂/β classification. "The A2' partition" lands more cleanly than "the A2' sub-scope partition" and aligns with AAD's partition-over-hierarchy vocabulary (it's not a strict-asymmetric hierarchy; it's a partition with derivability-status semantics). |
| [unnamed: the architectural-class partition Class 1 / Class 2 / Class 3] | architectural partition | +1 | Symbols stay (Class 1/2/3); prose gets "the architectural partition" as a collective handle. Avoids "architecture hierarchy" (hierarchy overload) while naming the three-way structure. |
| [unnamed: Class 1 / Class 2 / Class 3 agent classes themselves — need mnemonic handles] | *(proposal: assign English modifiers)* | +1 | Class-numbered labels work but lack mnemonic grip. Proposal: retain "Class 1 / 2 / 3" as the primary labels but assign canonical one-word modifiers — **modular** (Class 1), **merged** (Class 2), **partial** (Class 3) — that are already used descriptively. Adopt them as the *canonical* prose forms: "modular agents" / "merged agents" / "partially-modular agents" or "partial-mix agents." Class 2 especially benefits: "fully merged" currently appears; normalize to just "merged." |
| [unnamed: the template family — sector-persistence + contraction + possible future dissipativity] | persistence templates / the template family | +1 | The three-member family of `#sector-persistence-template`, `#contraction-template`, and (proposed Tier-2) `#dissipativity-template` wants a collective name. "The template family" or "the persistence-template family" works in prose. If dissipativity lands, this family-name gives it a natural home. Does not require a meta-segment; a paragraph in `#separability-pattern` / `#separability-ladder` would suffice. |
| [unnamed: the derivation/formulation/hypothesis/... status gradient in FORMAT.md] | epistemic gradient | +1 | FORMAT.md uses "Epistemic Triage" for the three questions; the resulting status-gradient ("postulate → result → formulation → hypothesis → empirical → observation → discussion → ...") has no short name. "The epistemic gradient" does it. Low priority but would help when onboarding fresh reviewers. |
| [unnamed: the three-rings-of-segment-content framing] | segment rings | +1 | FORMAT.md §"Three rings of segment content" (inevitability-core / canonical-formulations / empirical-heuristic-discussion) is load-bearing working vocabulary. "The segment rings" or "the three rings" is the natural prose handle. |
| [concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate] | the projection slogan / contraction-over-drift slogan | +1 | CLAUDE.md §7(g) names this as "organizing-principle slogan" (O-BP10, not yet surfaced at segment level). If promoted to segment-level it deserves a short handle — "the contraction-over-drift slogan" is short enough to say in a sentence. Low priority; depends on SP-7 / O-BP10 promotion decision. [original phrasing: unnamed: Joseph's mental model "projection whose contraction rate must exceed its target's drift rate"] |

### Methodologies and working-posture principles

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| "strengthen-first posture" | strengthen-first | +3 | Keep. Compact, verb-first, actionable. "Strengthen-first" is doing real work in the codebase (CLAUDE.md §Working Conventions) and has entered the project's working vocabulary. Do not retire. |
| "strengthen-first posture" | "attempt the improbable" | -1 | Considered the more aspirational form. Reject: "strengthen-first" is directive (tells you *what to do*), "attempt the improbable" is inspirational (tells you *how to feel*). Directive wins for working conventions. |
| "scope-honesty-as-architecture" | scope honesty as architecture | +1 | The hyphens signal "this is a concept-name, not a description" — useful in CLAUDE.md but awkward in running prose. Proposal: keep the hyphenated form only in CLAUDE.md §7 and README §reading-AAD where it is a named concept; use unhyphenated "scope honesty" in segment-level prose. |
| "calibration laboratory framing" | calibration laboratory | +1 | Keep. "Laboratory" is the right metaphor (high-identifiability, clean instrumentation, lets you measure AAD quantities exactly). "Framing" can be dropped in prose when the context is clear. |
| "prior-art integration" (convention) | prior-art integration | +1 | Keep. Directive, clear. No better alternative. |
| "communal-imagination test" | communal-imagination test | +1 | Keep. Names the evaluation criterion in a way that's memorable and actionable. Borrowed from the naming principles document itself. |
| "Gate 1 / Gate 2 / Gate 3 / Gate 4" (FORMAT.md promotion gates) | *(keep gate numbers but add one-word names)* | +1 | Current names are "Dependency audit / Content review / Mechanical review / Working Notes disposition" which are already descriptive, but the *numbers* do most of the referencing work ("passed Gate 2"). Consider adding canonical one-word names: Gate 1 = **deps**, Gate 2 = **claims**, Gate 3 = **format**, Gate 4 = **notes**. These already appear as stage names (`deps-verified` / `claims-verified` / `format-clean`); aligning Gate-number with stage-word would remove the translation step. |

### Framework-level names

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | +3 | Do not rename. The rename from ACT happened on 2026-04-16 (six months ago at this date); further churn dilutes the identity when the framework is starting to be cited. Any fresh alternative would face the same collision-checking burden that ACT did. **However:** the "Actuation" half is a genuinely weaker fit than "Adaptation" for what Section II covers (Section II is purposeful agency with objectives and strategy; "actuation" in engineering means *mechanical output*). The fix is not a rename but a Section II preamble paragraph that explicitly names "actuation" in AAD's specific sense ("actuated toward an objective" — already in LEXICON Agent-Classes, but needs to be surfaced at Section II preamble level). |
| AAD (alternatives considered for completeness) | APD (Adaptation and Purpose Dynamics) | -1 | "Purpose" captures Section II better than "actuation" but the acronym APD is cryptic; AAD has the phonetic advantage of being pronounceable ("aad" or "A-A-D"). Reject. |
| AAD (alternatives considered for completeness) | AAD (Adaptation and Agency Dynamics) | -1 | Considered swapping "Actuation" for "Agency" to keep the acronym while improving Section II fit. Reject: "agency" is fully claimed by current AI marketing vocabulary ("agentic AI" / "AI agents") to a degree that will bleed AAD's technical meaning. Worse than "actuation," which is at least semantically constrained. |
| Temporal Software Theory (TST) | Temporal Software Theory (TST) | +3 | Keep. The name has history (prior to AAD absorption and subsequent restoration) and "temporal" is load-bearing — it signals the AAD-native view that software is a time-optimality problem rather than a correctness problem. The acronym TST is pronounceable and has existing citation velocity from the 14,000-file prior corpus. |
| Logogenic Agents (Part III) | Logogenic Agents | +3 | Keep. Aligns with the `logogenic` class name in LEXICON and does not conflict with anything external. |
| Logozoetic Agents (Part IV) | Logozoetic Agents | +3 | Keep. |
| Agentic Systems Framework (ASF, top-level) | Agentic Systems Framework | +1 | Keep. "Agentic Systems" reads cleanly as the project name; ASF acronym is workable. The word "agentic" is currently a buzzword, but AAD is positioned to *ground it formally* (README §agency-scope) rather than be captured by it — the framework's willingness to define the term precisely is a positive. |

### Top-level document section names

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| README.md § "What This Is" | README.md § "What AAD Is" | -1 | Considered pinning the name in the heading. Reject: the README is AAD-level, not framework-level — the actual top-level "What This Is" is the Agentic Systems framework (of which AAD is Part I). "What This Is" works because the README is a specific-framework-README; renaming would cause a parallel question at the framework level. Keep as is. |
| README.md § "Structure" | README.md § "Structure" | +1 | Keep. |
| README.md § "Lexicon" | README.md § "Lexicon" | +1 | Keep. |
| README.md § "Novel Results" | README.md § "Novel Results" | +1 | Keep. "Novel" is load-bearing (these are AAD's own contributions, distinct from the integrated-prior-art); the section discipline is tight here. |
| README.md § "Convergent Choices" | README.md § "Convergent Choices" | +1 | Keep. This is a rare and valuable AAD construct (the intermediate category between "derived" and "chosen") and the name is apt. |
| README.md § "Maturity Gradient" | README.md § "Maturity Gradient" | +1 | Keep. "Gradient" is exactly what the sections-I-through-III closure-profile is (not a staircase; a gradient). |
| README.md § "Cross-Domain Joining" | README.md § "Cross-Domain Mapping" | +1 | "Joining" is slightly non-idiomatic in the context; "mapping" is the standard word for the same content (the section is a table mapping AAD concepts across domains). Weak preference. |
| TODO.md § "Archive" | TODO.md § "Archive" | +1 | Keep. Direct, accurate. |
| CLAUDE.md § "What's Settled vs. Open" | CLAUDE.md § "What's Settled vs. Open" | +3 | Keep. The section structure (Settled / Open / Known Fragilities) is load-bearing — renaming would leave readers uncertain whether "Settled" means "derived" or "under current working consensus" and the section's very content clarifies this. |
| CLAUDE.md § "Key Architectural Decisions" | CLAUDE.md § "Architectural Decisions" | -1 | Considered dropping "Key." Reject: "Key" signals these are load-bearing (not all decisions are listed here). Keep. |
| CLAUDE.md § "Working Conventions" | CLAUDE.md § "Working Conventions" | +1 | Keep. "Convention" here is used in its project-work-posture sense ("how we work"), not the C1/C2/C3 sense. Minor overload with convention hierarchy but contextually unambiguous. |
| OUTLINE.md (01-aad-core) preamble | "Reading AAD" | +1 | The preamble opens with "Working draft..." and "Reading AAD..." — the "Reading AAD" paragraph is doing framing work and deserves its own section-name in the doc table of contents. Light edit. |
| `spikes/INDEX.md` | `spikes/INDEX.md` | +1 | Keep. The all-caps SPIKES signals index-document status parallel to OUTLINE.md / FORMAT.md / CLAUDE.md. Good. |
| `MIGRATION-MAP.md` | `MIGRATION-MAP.md` | +1 | Keep. Lifecycle-aware name (it retires when absorption completes). |

### Segment section header names

These are *public API* for outline-filtering per PROPOSALS §H.5 — renaming ripples across ~110 segments.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `## Formal Expression` | `## Formal Expression` | +3 | Keep. Precisely-what-it-says; the word "Formal" is load-bearing (distinguishes from informal discussion). Any rename would cost the 110-segment ripple without benefit. |
| `## Epistemic Status` | `## Epistemic Status` | +3 | Keep. "Epistemic" is AAD's distinctive vocabulary; renaming to "Validity" or "Status" would lose the connection to the epistemic-architecture framing at CLAUDE.md §7. |
| `## Discussion` | `## Discussion` | +3 | Keep. Standard academic-register header; no rename needed. |
| `## Working Notes` | `## Working Notes` | +3 | Keep. The word "Working" signals this is *process artifact* (removed at `candidate` stage per FORMAT.md) rather than published content. Swapping to "Development Notes" would lose the active-in-progress sense. |
| `### What Is Derived vs. What Is Chosen` (derivation-audit table) | `### Derivation Audit` | +1 | The full title is load-bearing for first-encounter readers; `### Derivation Audit` is a usable shorter alternative for segments where the table follows a standard pattern. FORMAT.md O-BP14 already permits variation. Keep both as acceptable. |

### Prose vocabulary — individual word choices

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| "postulate" (not "axiom") | postulate | +3 | Keep. The project-wide TFT convention (axiom → postulate, theorem → result, proof → derivation) is load-bearing for scope honesty; AAD claims integrator-rigor, not foundational-mathematics-rigor, and the postulate/result/derivation register signals this correctly. Do not touch. |
| "result" (not "theorem") | result | +3 | Keep. Same argument. |
| "derivation" (not "proof") | derivation | +3 | Keep. Same argument. |
| "actuated" (agent class) | actuated | +1 | Keep. The LEXICON §"Actuated Agent" paragraph justifies the word explicitly ("precise and mechanical, avoiding consciousness connotations"); "purposeful" is fine in prose but "actuated" owns the formal register. |
| "structural adaptation" | structural adaptation | +3 | Keep. The distinction from *parametric adaptation* is load-bearing; "structural" is the right modifier. |
| "observability dominance" | observability dominance | +1 | Keep. The word *dominance* here is technically precise (information-theoretic dominance) and the phrase has two-word memorability. |
| "observability" / "opacity" | *(keep as an informational pair)* | +1 | Keep both. The dual framing (forward = observability, backward = opacity) is a load-bearing conceptual move; naming them as duals in NOTATION.md would make the pair explicit to fresh readers. Consider a "dual quantities" subsection. |
| "Chronica" (capitalized vs lowercase) | chronica (lowercase in running prose) | +1 | Convention observation: NOTATION.md shows $\mathcal C_t$ in formalism and "*chronica*" in italics in prose; LEXICON has it title-cased as "Chronica". Standardize on lowercase italicized "*chronica*" in running prose (matching "*aporia*" etc.), capitalized only as section headings. |
| "cycle" vs "loop" | *(keep both; maintain distinction)* | +3 | README §"Loop vs. Cycle" makes this distinction load-bearing (loop = structural topology, cycle = one traversal). The distinction is one of AAD's best small naming moves and should be enforced in every segment. |
| "five-phase cycle" | "adaptive pentad" (alternative) / "five-phase cycle" (keep) | +1 | See above in unnamed-things. "Five-phase cycle" is the current descriptive form; "adaptive pentad" is an optional Greek-vocabulary alternative. Aesthetic call. |

### Notation-level miscellaneous

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| $\mathcal C_t$ for chronica | $\mathcal C_t$ | +3 | Keep. The calligraphic-C choice is deliberately to avoid collision with $\mathcal H$ (entropy) and the symbol works in both LaTeX and prose. |
| $\mathcal C_t^{\text{commit}}$ (TST committed-state subset) | $\mathcal C_t^{\text{commit}}$ | +1 | Keep. The superscript-tag form is AAD-consistent. |
| $U_o$ / $U_M$ (observation uncertainty / model uncertainty) | $U_o$ / $U_M$ | +1 | Keep the symbols, but the name-collision with $U_O$ (teleological unity) and $U_\Sigma$ (strategic unity) is unfortunate — reader sees `U_` everywhere and has to disambiguate by subscript. Consider in NOTATION: group the uncertainties ($U_o$, $U_M$) separately from the unities ($U_M$ for epistemic unity — wait, this is already a collision with model uncertainty!). Inspect: is $U_M$ doing both jobs? Yes — NOTATION.md Multi-Agent table has $U_M \in [-1, 1]$ for *epistemic unity*, while Update-Gain table has $U_M > 0$ for *model uncertainty*. Same symbol, two meanings, differentiated only by range. This is a collision worth fixing before citation velocity picks up. |
| $U_M$ (dual-use: model uncertainty and epistemic unity) | $U_M$ for model uncertainty; $U_{\mathcal M}$ or $\Upsilon_M$ for epistemic unity | +3 | Genuine collision — same symbol, two different quantities, disambiguated only by domain. Fix before citations propagate. Candidate: rename *unity* symbols to $\Upsilon_M / \Upsilon_O / \Upsilon_\Sigma$ (capital upsilon, visually distinct from capital U; Greek letters are already the AAD unity convention-analog). Or use $U_{\mathcal M}$ with calligraphic subscript for unity. This is the most important notation-layer issue I found in the sweep. |
| $\rho$ (environment change rate / mismatch injection rate) | $\rho$ | +1 | Keep. Widely used; collisions with "density" in physics but AAD's usage is internally consistent. |
| $\rho_\Sigma$ (strategic disturbance rate) | $\rho_\Sigma$ | +1 | Keep. Subscript is load-bearing. |
| $\alpha, \beta$ (sector-lower and A2'-sub-scope) | $\alpha, \beta$ | +1 | Both are overloaded (α₁/α₂/β partition vs. α as sector-lower-bound; β as IB trade-off parameter vs. β as A2' assumed-sector sub-scope). Context disambiguates but marginal readers will stumble. Consider: bolded $\boldsymbol\alpha$ or subscripted $\alpha_{\text{sec}}$ on first use per segment. Minor notation discipline issue. |

### Section I slugs — quick pass

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#scope-condition` | `#scope-condition` | +3 | Keep. This is the Section I membership criterion — "where AAD applies." The slug is self-announcing and gets cited heavily across segments. |
| `#agent-environment` | `#agent-environment` | +1 | Keep. The boundary definition needs a direct name; this is it. |
| `#observation-function` / `#action-transition` | keep | +1 | Keep both. Short, direct, describe what they are. |
| `#composition-consistency` | `#composition-consistency` | +3 | Keep. One of AAD's load-bearing postulates; the name signals the content (agent/subagent scale-invariance). |
| `#recursive-update` | `#recursive-update` | +3 | Keep. AAD's strongest result ("three constraints → unique recursive form") deserves its direct, clean name. Do not touch. |
| `#agent-model` | `#agent-model` | +1 | Keep. Short, direct. |
| `#information-bottleneck` | `#information-bottleneck` | +3 | Keep — adopted directly from Tishby et al. per prior-art-integration convention. Do not rename adopted concepts. |
| `#model-sufficiency` / `#model-class-fitness` | keep | +1 | Keep both. Each is a specific technical quantity ($S$ and $\mathcal F$) — the slug is the concept. |
| `#event-driven-dynamics` | `#event-driven-dynamics` | +1 | Keep. "Event-driven" carries correct engineering baggage (versus turn-based / synchronous). |
| `#mismatch-decomposition` | `#mismatch-decomposition` | +1 | Keep. Direct. |
| `#mismatch-dynamics` | `#mismatch-dynamics` | +1 | Keep. |
| `#causal-information-yield` (CIY) | `#causal-information-yield` | +1 | Keep. The CIY acronym is useful and the slug is self-contained. |
| `#adaptive-tempo` | `#adaptive-tempo` | +3 | Keep. "Tempo" is one of AAD's best one-word handles; the slug is short. |
| `#deliberation-cost` | `#deliberation-cost` | +1 | Keep. "Cost" signals tradeoff cleanly. |
| `#persistence-condition` | `#persistence-condition` | +3 | Keep. The slug for AAD's *central inequality*; any change would ripple through every citing segment. |
| `#structural-adaptation-necessity` | `#structural-adaptation-necessity` | +1 | Keep — "necessity" signals this is a derived need ("when parametric update fails, structural adaptation *must* happen"). |
| `#temporal-nesting` | `#timescale-nesting` | +1 | "Temporal nesting" is accurate but slightly generic; "timescale nesting" names the specific nesting (slow/fast timescale separation) and avoids collision with TST's "temporal" (as in Temporal Software Theory). Weak preference. |
| `#sector-condition-stability` | `#sector-condition-stability` | +1 | Keep. |
| `#gain-sector-bridge` / `#gain-sector-derivation` | keep both | +1 | Keep. "Bridge" signals this is the connection piece (gain principle + directional fidelity → sector condition); "derivation" signals the formal backing. |

### TST slugs — quick pass

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `#temporal-optimality` | `#temporal-optimality` | +3 | Keep. TST's central claim ("time-optimal development is the right objective"); slug is canonical. |
| `#software-epistemic-properties` | `#software-epistemic-properties` | +1 | Keep. "Software" locates the domain; "epistemic properties" lines up with AAD §7's epistemic-architecture framing. |
| `#software-scope` | `#software-scope` | +1 | Keep. Direct. |
| `#developer-as-act-agent` | `#developer-as-adaptive-agent` | +3 | See slug-relics section above. |
| `#ai-agent-as-act-agent` | `#ai-agent-as-adaptive-agent` | +3 | See slug-relics section above. |
| `#atomic-changeset` | `#atomic-changeset` | +3 | Keep. Domain-native term with precise technical meaning in software engineering; aligns with prior-art-integration. |
| `#change-distance` / `#change-proximity-principle` | keep both | +1 | Keep. Both are domain-specific TST quantities — changing names risks losing the TST citation lineage. |
| `#changeset-size-principle` | `#changeset-size-principle` | +1 | Keep. Principle-level claim; named descriptively. |
| `#conceptual-alignment` | `#conceptual-alignment` | +1 | Keep. Core TST empirical claim; slug is clear. |
| `#code-quality-as-observation-infrastructure` | `#code-quality-as-observation-infrastructure` | +1 | Keep. The "as-observation-infrastructure" framing is the segment's pedagogical move (TST-to-AAD mapping) — renaming would lose the bridge. The slug is long but earns it. |
| `#coherence-coupling-measurement` | `#coherence-coupling-measurement` | +1 | Keep. |
| `#comprehension-time` / `#implementation-time` | keep both | +1 | Keep. Canonical TST quantities. |
| `#continuous-operation` | `#continuous-operation` | +1 | Keep. |
| `#exponential-cognitive-load` | `#exponential-cognitive-load` | +1 | Keep. The "exponential" in the slug is load-bearing (the claim's punch is *exponential* scaling). |
| `#dual-optimization` | `#dual-optimization` | +1 | Keep. |
| `#principled-decision-integration` | `#principled-decision-integration` | +1 | Keep. |
| `#specification-bound` | `#specification-bound` | +1 | Keep. |
| `#system-coherence` / `#system-coupling` / `#system-availability` | keep all three | +1 | Keep — each is a distinct TST system-level property; the parallel `system-X` structure is itself pedagogical. |
| `#ai-specification-limit` (as TST concept, currently only in old-tst files) | `#ai-specification-limit` | +1 | Keep reserved slot. Eventually promotes from old-tst files. |
| `old-tst-*` files (~40 files) | *(no rename; these retire with MIGRATION-MAP)* | +1 | Not eligible for renaming — these are transitional absorption files that will retire once MIGRATION-MAP completes. Keep as-is. |

### msc/ and working-file naming — observation

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| `spikes/spike-{topic}.md` | `spikes/spike-{topic}.md` | +1 | Keep. The `spike-` prefix is a clean filename convention signaling "exploratory, reasoning-trail, not the theory proper." |
| `spikes/spike-{topic}-{YYYY-MM-DD}.md` | `spikes/spike-{topic}-{YYYY-MM-DD}.md` | +1 | Keep the dated variant for recurring-topic spikes. Date suffix makes second-iteration spikes findable. |
| `msc/architectural-proposals-{YYYY-MM-DD}.md` | *(retire once consolidated into PROPOSALS.md)* | +1 | PROPOSALS.md has already absorbed these; the dated proposal files are historical artifacts. Not a rename; a retirement when MIGRATION-MAP convention allows. |
| `audits/pending-findings-{YYYY-MM-DD}.md` | *(retire once items reconcile into TODO / segments)* | +1 | Same lifecycle. |
| `msc/reflections/` | `msc/reflections/` | +1 | Keep. The `reflections/` subdirectory is a legitimate separate register from spikes/brainstorms. |
| `spikes/INDEX.md` (spike index) | `spikes/INDEX.md` | +1 | Keep. All-caps index convention. |

### Explicit "do not rename" reminders

One-row votes to ensure the aggregation captures explicit declines to change items that other voters might have proposed to change.

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| Pearl's causal hierarchy (L0/L1/L2 in Pearl's own vocabulary) | *(do not rename)* | +3 | Prior-art-integration convention prohibits renaming adopted concepts. The adjacent-to-AAD "correlation hierarchy / correlation ladder" is a *different* AAD-native object; rename freedom belongs there, not here. |
| information bottleneck (Tishby) | *(do not rename)* | +3 | Same. |
| Lohmiller-Slotine contraction (metric generalization used in `#contraction-template`) | *(do not rename)* | +3 | Same. Adopted with name intact. |
| Monderer-Shapley potential games / Rosen monotone games | *(do not rename)* | +3 | Same. |
| Hafez $H_b$ / Miller meta-machine / Bruineberg Pearl-blanket | *(do not rename)* | +3 | Same. |
| Bretagnolle-Huber identity | *(do not rename)* | +3 | Same. |
| Čencov / Fisher / Cauchy functional equation / Shore-Johnson / Hobson / Aczél | *(do not rename)* | +3 | External theorems. Keep original names per provenance. |
| OODA (Boyd) | *(do not rename)* | +3 | Same — "orient cascade" is AAD's adjacent-but-distinct construction; OODA keeps its lineage. |
| Cox's theorem / Causal Hierarchy Theorem / Tikhonov's theorem | *(do not rename)* | +3 | Same — FORMAT.md §"Why these labels" explicitly preserves external theorem names. |

---

## Principles-observations

Feedback on the principles document itself, for refinement before round 2.

1. **The cold-start instruction is easy to violate accidentally, and the consequence is asymmetric.** I had the brainstorm open in my orientation pass before fully reading the principles document, because it was in `git status` as a modified file and I naturally look at modified files first to understand project state. The cold-start instruction would benefit from being the *first* paragraph of the principles file, not a middle paragraph, so agents see it before they start reading anything else. A more actionable form: "**STOP** — before reading this file further, do not open `msc/naming/naming-brainstorm-*.md` or `msc/naming/naming-votes/*`. Start here, finish the principles, then do your own review." And ideally the task-giver should add the same instruction up front ("read principles.md before anything else"). I am a data point for the risk.

2. **The +3 / +1 / −1 scale collapses too much.** In a vote where every name gets considered, I found myself wanting finer distinctions — particularly between "this is a keep I would reluctantly change if the community wanted to" (weak +1 keep) versus "this is a keep I would actively fight for" (strong +3 keep). Both currently read as +1 or +3 without gradation. A +2 rank would help, or alternately a +3-only-if-fighting-for-it discipline instruction. As written I had to round, and rounded toward the conservative (+1) more often than toward the strong (+3), which probably undercounts my real preferences.

3. **The "absence is not a vote" rule combined with the 60+ row target is in tension.** The cold-start instruction says vote explicitly for anything considered, which is epistemically sound. But with ~110 AAD segments plus TST segments plus symbols plus document sections plus methodology names, an agent who truly considered each one-by-one would produce 300+ rows. The 60+ target therefore implicitly means "only write down the rows where you actually have an opinion worth expressing." I interpreted this as "vote explicitly on everything I *had a meaningful opinion on* after direct review" rather than "vote on every name in the project." Worth clarifying in the principles: the 60+ floor is meaningful opinions, not exhaustive coverage.

4. **Some naming considerations aren't in the evaluation criteria.** I kept wanting to vote based on criteria not explicitly listed:
   - **Phonetic weight** — whether the name is pleasant to say aloud (*chronica* vs *complete-agent-state-temporal-subset* — both might be precisely accurate, but one will be said a thousand times and the other zero times). This is adjacent to memorable-noun-potential but distinct.
   - **Rhythm with neighbors** — whether the name reads well *next to* other AAD names ("sector-persistence-template" reads well next to "contraction-template" because of the template-family rhythm; renaming one without the other would break the family).
   - **Mnemonic-pair potential** — whether renaming one thing lets two things form a pair (floor/ladder, satisfaction-gap/control-regret). These pair-forming moves are high-leverage but the principles don't name the category.
   - **Acronym / pronounceability** — AAD is pronounceable; TST is spellable; ASF is neither memorable nor unmemorable. Framework-name moves have acronym cost that the principles don't surface.

5. **Segment-slug renames carry asymmetric churn cost the principles don't mention.** Renaming `#additive-coordinate-forcing` → `#forced-coordinates` ripples through every citing segment, every dependency graph, every OUTLINE row, and the build tool. The principles say "slugs are eligible" but don't give voters a cost-scaling hint. Ideally the principles would mention: slug renames cost ~an hour of mechanical propagation + a dependency-graph rebuild; symbol renames cost a NOTATION.md edit + prose propagation; prose-vocabulary renames cost whatever the segment edits demand. These are order-of-magnitude different, and voters should factor cost against benefit when the benefit is small.

6. **The example votes don't include "vote to *unname* a thing."** Several of my most valuable proposals are in the other direction — "name this unnamed thing" (persistence envelope, chain anchor, inferential-force cascade). These are highest-leverage because they open new slots. But the reverse category — "retire a name that is paraphrased dead weight" — might also exist and isn't in the example set. I didn't find any, but future agents might.

7. **Principles-level observation: naming is load-bearing in a way that interacts with scope-honesty.** AAD's own §7 element (a) ("scope-honesty-as-architecture") argues that scope and limits should be made visible at the segment level. A name that *over-promises* (claims more generality than the segment delivers) is a scope-honesty violation at the name layer — not a bug but a structural commitment. The evaluation criteria (§5 "Scope honesty") catches this. I would promote it slightly: scope-honesty in naming is not just one criterion among seven — it is the criterion that most closely aligns with what makes AAD distinctive. Where an agent is torn between two candidates, the scope-honest one should win all ties.

8. **One missed criterion: the "renamed-from-now-sounds-weird" test.** When evaluating a rename, imagine the project six months from now with the new name in place. If the *old* name would then sound quaint ("oh, we used to call that additive-coordinate-forcing"), the rename is a winner. If the *new* name would sound forced and artificial ("we're calling it 'forced coordinates' now because some round-one vote"), keep. I used this test implicitly; worth making explicit.

9. **Meta-observation on the aggregation round.** My suspicion is that round 2 will converge faster than round 1 because memorable renames tend to pull votes (if "forced coordinates" crosses anybody's threshold, it will probably cross most). The principles could note: round 2 should weight round-1 *agreement across independent agents* more heavily than individual strong preferences. A weak +1 from four agents probably beats a strong +3 from one.

10. **Final observation on contamination in my own vote.** Re-reading my votes after drafting: I can see brainstorm-influence most strongly on the three-meta-architecture trio (floor/ladder/Cauchy-coordinates, though I landed on `#forced-coordinates` rather than `#cauchy-coordinates` via independent reasoning about the Čencov instance), the `-act-agent` slug relics (obvious cleanup), and the `#strategic-composition` overload. I can see my-own-reasoning most strongly on the `$U_M$ collision (fixing vs. not-flagged-in-brainstorm-at-all)*, the persistence-envelope proposal (which the brainstorm does mention but where my argument-from-flight-envelope analogy is independent), the Class-1/2/3 modular/merged/partial modifier proposal, the Gate-number-to-Gate-word alignment, the `#edge-update-natural-parameter` → `#log-odds-update` proposal, and most of the Section I / Section II / TST row-by-row work. Net: the big three-meta moves are contaminated; the fine-grained slug work is mostly my own. Aggregator should weight accordingly.

---

*End of vote. 2026-04-23.*







