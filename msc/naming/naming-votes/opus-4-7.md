# Opus 4.7 (1M context) — Naming Votes

**Approach.** I read broadly across CLAUDE.md / OUTLINE.md / LEXICON.md / NOTATION.md / FORMAT.md / README.md and sampled segments from AAD-core, TST, and logogenic-agents. I prioritized: (1) overloaded or multi-subscript symbol names that force the reader to carry a decoder ring, (2) meta-segment names whose scope has drifted since their first draft, (3) currently-unnamed recurring patterns that the theory keeps paraphrasing, and (4) section-header and doc-level names whose ubiquity makes them high-ROI. I let pure aesthetic preference appear in +1 votes and reserved +3 for cases where I think a rename (or a firm keep) is load-bearing for reader comprehension.

A few concepts I encountered that deserve their own memorable noun and probably do not have one yet — I flag them as "[unnamed: …]" rows, which I think are the highest-value discoveries of this audit.

## Votes

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| satisfaction gap | satisfaction gap | +3 | Crispest named pair in the project; the 2×2 diagnostic works because both names work. Explicit keep. |
| control regret | control regret | +3 | Pair-partner to satisfaction gap. The pair carries its decomposition load. Keep. |
| #directed-separation | #directed-separation | +3 | Survived the κ-as-scalar category-error rescue; the name now has its architectural Class 1/2/3 classification attached. Don't touch. |
| orient cascade | orient cascade | +3 | The five-phase cycle has an "expand" for actuated agents; "cascade" evokes the forced-by-information-dependency ordering. One of the theory's best names. Keep. |
| chronica | chronica | +3 | Singular Greek-root noun with clean Obsidian/prose pickup; also resolves the $\mathcal H$/entropy collision. Joseph deliberately avoided "history" — don't unwind. |
| the five cycle phases (Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis) | Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis | +3 | Each Greek term names a distinction the English flattens (aporia as productive perplexity is the load-bearer). Do not translate. Keep. |
| logogenic / logozoetic | logogenic / logozoetic | +3 | Etymology carries multiple senses (word / reason / animating force / governance) that no English term carries together. LEXICON makes this explicit. Keep. |
| actuated (agent) | actuated (agent) | +3 | Deliberately chosen over "purposeful" to avoid consciousness baggage while carrying the "driven-toward-setpoint" shape. Named framework half ("Actuation" in AAD). Keep. |
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | +3 | Recent (2026-04-16) rename to resolve the "AI Consciousness Test" collision; further churn dilutes identity. The "Actuation"-vs-Section-II imperfection is a preamble clarification not a rename. |
| #additive-coordinate-forcing | #forced-coordinates | +1 | The Čencov fourth primary instance forces the Fisher metric, which is not log-additive — the current name advertises three-out-of-four. "Forced coordinates" covers both Cauchy-FE and Čencov machineries without overpromising additivity. The segment itself flags this in the Discussion. Candidate. |
| #additive-coordinate-forcing | #uniqueness-coordinate-forcing | +1 | Alternative that matches the "broader discipline" phrasing the segment itself uses. Less snappy than #forced-coordinates; more precise. |
| #additive-coordinate-forcing | #cauchy-coordinates | -1 | Undersells the Čencov instance; would require a second meta-segment to cover the fourth primary instance. Reject. |
| #additive-coordinate-forcing | #coordinate-forcing | +1 | Verb-form variant; fine if #forced-coordinates doesn't land. |
| #identifiability-floor | #identifiability-floor | +3 | Three-word noun that invites both floor-instances and escape-routes; "floor" evokes the structural lower bound and Joseph has already used "escape the floor" as organic prose. Keep. |
| #separability-pattern | #separability-ladder | +1 | The segment itself uses "seven ladders" and each row is a ladder — the organizing concept is ladder-shaped, not pattern-shaped. "Pattern" feels generic for what is a precise three-rung structure. |
| #separability-pattern | #separability-staircase | -1 | Whimsical; prefers #separability-ladder if any rename at all. |
| #separability-pattern | #three-rung-posture | -1 | Too mechanical; loses "separability" which is the content. |
| #approximation-tiering | #approximation-tiering | +1 | Fine but generic — keep unless a better name emerges, since the AT1/AT2/AT3/AT4 component scheme has already landed. |
| #approximation-tiering | #tier-ascension | -1 | Reads like a ranked-climbing metaphor the segment does not actually use. Reject. |
| #sector-persistence-template | #sector-persistence-template | +3 | Names the mechanical content (Lyapunov on sector-bounded correction) and is already cited by six instantiations. Keep. |
| #contraction-template | #contraction-template | +3 | Natural name, Lohmiller-Slotine lineage, aligns with the sibling #sector-persistence-template. Keep. |
| #graph-structure-uniqueness | #dag-structure-derivation | +1 | "Uniqueness" overpromises — the actual result is "four operational postulates + causal sufficiency force a DAG-with-Markov-factorization." The *necessity* direction is noted open (strategy-dag Discussion). "Derivation" is honest about what is proved. |
| #graph-structure-uniqueness | #graph-structure-uniqueness | +1 | Alternative keep-vote. The name has citation velocity already. If rename is disruptive enough to rebaseline cross-refs, keep. |
| #strategic-composition | #equilibrium-composition | +1 | Reduces "strategic" overload in Section III (already have #strategic-tempo, #strategic-calibration, #strategic-dynamics-derivation). The segment's actual content is equilibrium-convergence under Monderer-Shapley / Rosen. |
| #strategic-composition | #game-theoretic-composition | -1 | Too broad — game theory covers more than partially-opposing O_t; the equilibrium-convergence framing is tighter. |
| #interaction-channel-classification | #recipient-regime-classification | +1 | Makes the recipient-side orientation explicit at the name level, since the emitter-side version (#agent-opacity) now exists as a dual. Current name doesn't disambiguate emitter-vs-recipient. |
| #agent-opacity | #agent-opacity | +1 | Fine; "opacity" is the right scalar polarity (emitter side) and has Hafez-lineage citation weight. But see next row. |
| #agent-opacity | #emitter-opacity | +1 | Disambiguates emitter-side from recipient-side in the 16-cell composition. Parallel with #recipient-regime-classification above. |
| #loop-interventional-access | #loop-interventional-access | +3 | Names the distinctive Pearl-Level-2-by-construction move; the segment is load-bearing for both #identifiability-floor and #agent-identity. Don't touch. |
| #strategy-dag | #strategy-dag | +3 | Established; the segment does a lot of work (acyclicity derived, Markov derived, correlation hierarchy). Keep. |
| #strategy-dimension | #strategy-decomposition | +1 | "Dimension" reads as if it's naming a scalar axis; the actual content is the $G_t = (O_t, \Sigma_t)$ **decomposition**. Minor clarity win. |
| #critical-mass-composition | #dyad-closed-form | +1 | "Critical mass" suggests emergence-above-threshold but the segment derives a closed-form composite sector constant for the symmetric-matched-Tier-1 dyad. Honest label. |
| #critical-mass-composition | #critical-mass-composition | +1 | Alternative keep-vote: "critical mass" has intuitive pickup for the threshold nature of composition viability. Content-neutral; reader decides. |
| #persistence-cost | #persistence-cost | +3 | The segment's content is exactly that — information rate required to hold the persistence bound. Name does work without overclaiming. Keep. |
| #detection-latency | #detection-latency | +3 | Standard term, forced by the $\Omega((n_{\min}+1)/\varepsilon)$ bound; the segment's novel content is that latency is structurally forced through the log-odds coordinate. Keep. |
| #consolidation-dynamics | #consolidation-dynamics | +1 | Fine. Inherits "consolidation" from neuroscience (memory consolidation). Keep unless a sharper name emerges. |
| adaptive reserve ($\Delta\rho^\ast$) | adaptive reserve | +3 | Rare English term that reads as *shock tolerance* in prose and ties cleanly to the $\alpha R - \rho$ formula. One of the project's cleanest symbol-to-English pairs. Keep. |
| adaptive tempo ($\mathcal T$) | adaptive tempo | +3 | "Tempo" carries the rate-and-quality compound idea better than "rate" or "speed"; aligns with Boyd OODA lineage. Keep. |
| adaptive tempo | adaptation rate | -1 | Loses the "rate × quality" compound the tempo metaphor delivers. Reject. |
| mismatch signal ($\delta$) | mismatch signal | +3 | In contrast with "error" or "residual"; the word foreshadows the aporia interpretation. Keep. |
| update gain ($\eta^\ast$) | update gain | +3 | Kalman-resonance lineage name, self-descriptive. Keep. |
| #identifiability-floor "escape the floor" | escape route | +1 | Currently referred to variably as "escape the floor," "unique broadly-available escape," "boundary characterization." "Escape route" is a cleaner noun for the reader. Minor pattern-firmer-up. |
| $\alpha_1$ (A2' fixed-gain sub-scope) | derived-gain regime | +1 | "Lands in $\alpha_1$" is cryptic in prose; "lands in the derived-gain regime" reads. Keep $\alpha_1$ as symbolic shorthand but surface the English in segment text. |
| $\alpha_2$ (A2' adaptive-gain sub-scope) | adaptive-gain regime | +1 | Parallel construction to $\alpha_1$ rename. |
| $\beta$ (A2' assumed-not-derived sub-scope) | assumed-regime | +1 | Parallel again; currently reads as "lands in $\beta$" which tells the reader nothing. Alternatively "posited-regime." |
| $\beta$ (A2' sub-scope) | posited-regime | -1 | Slightly more formal than "assumed" but less transparent. Reject. |
| $\alpha_1$ / $\alpha_2$ / $\beta$ naming as a whole | $\alpha$-partition (with English labels above) | +1 | Keep the Greek symbols as shorthand tokens once defined; insist on English equivalents in every new prose usage. Bubble this into FORMAT.md as a convention. |
| $\kappa_{\text{processing}}$ | processing coupling | +1 | Symbol is fine but the name "$\kappa$-as-scalar" was explicitly retired as a category error — the live reading is "processing coupling as a diagnostic for Class 3 agents." Surface that English name consistently. |
| $U_o$ (observation uncertainty) | observation uncertainty | +3 | Standard control-theory baggage; adoption is correct. Keep. |
| $U_M$ (model uncertainty) | model uncertainty | +3 | Parallel to $U_o$. Keep. |
| $U_O$ (teleological unity) | teleological unity | +3 | Clearly distinguishes from $U_o$ by subscript letter-case and by semantic content. Awkward because $U_o$ / $U_O$ are near-homographs in some fonts — see next row. |
| $U_o$ vs $U_O$ collision | consider renaming teleological unity to $U_\Omega$ or $U_\text{goal}$ | +1 | The uppercase/lowercase distinction between observation uncertainty ($U_o$) and teleological unity ($U_O$) is fragile in serif fonts and read-aloud. Worth an audit; a subscript of $\Omega$ or "goal" would be more robust. |
| $\hat P_\Sigma$ (plan confidence) | plan confidence | +1 | LEXICON "Terms to Be Added" flags this. Symbol is fine; adopt the English name as first-class in prose. |
| $\varepsilon^\ast$ (closure defect) | closure defect | +3 | Crisp name for a derived quantity that appears across composition. LEXICON already names it. Keep. |
| $\mathcal C_t^{\text{commit}}$ (committed-state subset) | committed chronica | +1 | TST-specific subset of chronica; prose form would help the 14-EXACT-estimator audit table read more naturally. |
| [concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | pattern anatomy | +1 | Currently a long phrase that the theory uses three to four times per session. "1-anchor-plus-3-theorem" is precise but reads as inventory-counting. "Pattern anatomy" (or "pattern spine") could snapshot the structure. Flagging; low conviction on exact name. [original phrasing: unnamed: the 1-anchor-plus-3-theorem characterization] |
| [concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims] | strengthen-first posture | +3 | Already functionally the name (CLAUDE.md §Working Conventions uses it as a heading). Explicit vote to lock this in as a first-class project methodology name. Adopt as canonical. [original phrasing: unnamed: the "strengthen before soften" work posture] |
| [unnamed: effort/time/risk-ranking considered "false constraints"] | false constraints | +1 | Joseph uses this phrasing; worth canonicalizing so agents (me included) can recognize the pattern. |
| [unnamed: the strengthen-first *attempt* artifact — a spike that tried to derive something stronger and failed] | strengthening attempt / attempt record | +1 | The CLAUDE.md text says "document the strengthening attempt and why it failed even when it does fail." These deserve a noun so the workflow has a vocabulary. |
| [unnamed: the iterated-audit process (Gemini / Opus / Codex de novo, consolidated, three-doc portfolio)] | cross-model audit cycle | +1 | Recurring methodology; currently referred to as "audit cycle" generically and by date. A durable name helps. Low conviction. |
| [unnamed: the "epistemic architecture as AAD's distinctive contribution" frame] | epistemic architecture | +3 | CLAUDE.md §7 now carries this as a load-bearing framing. Surface at segment-preamble level and keep the term consistent. Strong keep as a first-class project concept. |
| [unnamed: "scope-honesty-as-architecture"] | scope honesty | +1 | Already used as a term; "-as-architecture" is the argumentative form. "Scope honesty" alone works as the noun for the commitment (as it already does in several segments). |
| [unnamed: the 2×2 satisfaction-gap × control-regret diagnostic table] | the 2×2 diagnostic | +1 | Used ubiquitously in prose. Worth canonicalizing as a named object so that "see the 2×2 diagnostic" reads naturally. |
| [unnamed: the "functional requirements are the results; formalisms are the engineering" slogan] | functional primacy | +1 | Joseph flagged this as an established project principle (MEMORY.md, Theory Character section); it deserves a pull-quote name. Low conviction; flag for consideration. |
| [unnamed: the three concentric rings of segment content — inevitability core / canonical formulations / empirical-heuristic] | three rings | +1 | FORMAT.md uses exactly this language. Named once; currently paraphrased each time. Adopt "three rings" as the canonical shorthand. |
| [unnamed: "inevitability core"] | inevitability core | +3 | FORMAT.md already uses this. Keep and surface in prose ("this segment sits in the inevitability core" is already idiomatic). Explicit canonicalization vote. |
| [concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate] | projection-contraction slogan | +1 | CLAUDE.md §7(g) flags this as Opus O-BP10, "not yet surfaced at segment level." Deserves a name so it can be referenced before it lands as prose. [original phrasing: unnamed: the organizing-principle slogan — "An adaptive system is a projection whose contraction rate exceeds its target's drift rate"] |
| [concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate] | calibration laboratory | +3 | Load-bearing distinction vs. "best operationalization domain"; TST's OUTLINE.md preamble now uses this. Canonical. Keep. [original phrasing: unnamed: "calibration laboratory" framing for software/TST] |
| [unnamed: the correlation hierarchy (L0 / L1 / L1' / L2)] | Correlation Hierarchy | +3 | The name is already established capitalized-as-proper-noun in #strategy-dag. Explicit vote to preserve the capitalization and treat it like Pearl's Causal Hierarchy (a first-class named object). |
| [unnamed: the convention hierarchy (C1 / C2 / C3)] | Convention Hierarchy | +3 | Same move — capitalize as proper noun, preserve as named object. The monotonicity result is load-bearing and the Hierarchy is what the result is about. |
| [unnamed: Pearl's causal hierarchy (Level 1 / Level 2 / Level 3)] | Pearl Causal Hierarchy | +3 | Named by original author. Keep proper-noun form. |
| "hierarchy" as a project-wide word | flag: four independent hierarchies overloaded | +1 | Pearl's causal, AAD's convention, AAD's correlation, AAD's approximation tiering — four hierarchies in one framework. Not a rename but worth a cross-link convention (always say *which* hierarchy on first use of section). |
| #persistence-condition | #persistence-condition | +3 | The central inequality; eponymous. Keep. |
| "structural persistence" / "operational persistence" / "continuity persistence" | structural / operational / continuity persistence | +3 | LEXICON disambiguates three senses explicitly; the tri-partite naming is doing real work (mentioned as orthogonal in the table). Keep the three names verbatim. |
| #explicit-strategy-condition | #planning-scope | +1 | The segment is a normative scope condition for "when planning beats exploring." Current name reads as condition-on-the-strategy, not condition-for-strategy-to-apply. Minor clarity win. |
| #exploit-explore-deliberate | #exploit-explore-deliberate | +3 | Three-way decomposition is itself the content. Triadic name matches triadic claim. Keep. |
| #causal-insufficiency-detection | #causal-insufficiency-detection | +3 | Names exactly what the result is about; the CHT-driven no-go gives the segment its shape. Keep. |
| #chain-confidence-decay | #chain-confidence-decay | +3 | Inevitability-core segment; name matches the log-decomposition content. Keep. |
| #recursive-update | #recursive-update | +3 | Strongest inevitability-core result; three-constraint uniqueness derivation. Keep. |
| #recursive-update-derivation | #recursive-update-derivation | +3 | Paired with the above. Keep. |
| ## Formal Expression | ## Formal Expression | +3 | Section header is project-wide; renaming would ripple everywhere and buys nothing. Keep. Every segment uses this. |
| ## Epistemic Status | ## Epistemic Status | +3 | Load-bearing header that signals the distinctive AAD convention of epistemic labeling at segment scale. Keep. |
| ## Discussion | ## Discussion | +3 | Standard. Keep. |
| ## Working Notes | ## Working Notes | +3 | Keep; the name plus the rule that Working Notes must be empty at candidate stage has a meaningful pairing. |
| ## What Is Derived vs. What Is Chosen | ## Derivation Audit | +1 | FORMAT.md lists both as acceptable variants for the table heading. "Derivation Audit" is shorter and matches the three-column table's analytical role; "What Is Derived vs. What Is Chosen" is longer but self-documenting. Weak preference for the shorter. |
| CLAUDE.md §"Working Conventions" | CLAUDE.md §"Working Conventions" | +3 | Surfaced as a first-class section 2026-04-23; the name accurately distinguishes from FORMAT.md's segment-mechanics conventions. Keep. |
| CLAUDE.md §"What's Settled vs. Open" | CLAUDE.md §"What's Settled vs. Open" | +3 | The honest binary is the right framing; don't soften to "Current State" or similar. Keep. |
| TODO.md §Archive | TODO.md §Archive | +1 | Fine; conventional. Keep. |
| LOG.md (cycle history document) | LOG.md | +3 | The cycle-by-cycle theoretical contribution record; the name is generic but its load-bearing function is specific. Keep as a stable identifier. |
| #auftragstaktik-principle | #auftragstaktik-principle | +1 | German military lineage name (command-intent autonomy) is doing real work — same reason "directed separation" beat a generic alternative. Keep. |
| #symbiogenic-composition | #symbiogenic-composition | +1 | Etymologically accurate (Margulis lineage; asymmetric absorption). Keep unless cleaner alternative emerges. |
| (R1), (R2) — Result numbering convention in logogenic-agents | keep with cross-component prefixes (L-R1, L-R2) | +1 | As soon as logogenic-agents grows, "Result R1" collides with AAD-core numbering in discussion. Minor. |
| "dark-room critique" citation phrasing (Sun & Firestone) | "dark-room critique" | +1 | Memorable, captures the collapse vividly, already used in two segments. Worth locking as project-wide vocabulary. |
| "Pearl-blanket vs Friston-blanket" terminology (Bruineberg et al.) | Pearl-blanket / Friston-blanket | +3 | Verbatim terminology per Bruineberg 2022 fn 3 (Biehl). Not AAD's name to change; preserve attribution. Keep. |
| #bias-bound-derivation | #bias-bound-derivation | +3 | Newly landed appendix; name matches content. Keep. |
| "Track 1" / "Track 2" in #bias-bound-derivation | transport-inequality track / Fisher-Rao track | +1 | Inside the segment, "Track 1" and "Track 2" are fine as local shorthand. In any cross-segment reference, the English names read better. |
| Bretagnolle-Huber identity | Bretagnolle-Huber identity | +3 | External-theorem attribution; preserve. Keep. |
| "1-anchor-plus-3-theorem" | "1-anchor-plus-3-theorem" | +1 | Precise, reads as a shape-description; used as-is in multiple places. Keep, but also allow "pattern anatomy" as the informal analog. |
| "meta-segment" (for #separability-pattern, #identifiability-floor, #additive-coordinate-forcing) | meta-segment | +3 | The tri-partite meta-architecture needs a noun for its elements; "meta-segment" works. Keep as project-internal vocabulary. |
| "segment" (for claim files) | segment | +3 | Deliberate vs. "section" (which is outline-level) or "claim" (which is what's *in* the segment). Clean distinction. Keep. |
| "the adaptive cycle" (as the theory's fundamental unit) | the adaptive cycle | +3 | LEXICON locks this against "loop" (topology) and "cycle" (traversal). The pair distinction is load-bearing. Keep. |
| "cycle" vs "loop" | cycle vs loop | +3 | See above — the two-word disambiguation is one of the theory's most useful vocabulary moves. Keep. |
| #complete-agent-state | #complete-agent-state | +3 | Canonical formulation — $X_t = (M_t, G_t)$. Self-descriptive. Keep. |
| #agent-spectrum | #agent-spectrum | +1 | Names the ±model × ±objective 2×2 table; the segment's content is exactly that. Fine. |
| #agent-identity | #agent-identity | +3 | Surfaced 2026-04-22 as a formal scope commitment; name carries the token-level commitment honestly. Now (PI) sits here. Keep. |
| #agent-model | #agent-model | +3 | Standard. Keep. |
| #agent-environment | #agent-environment | +3 | Standard; boundary definition. Keep. |
| "logogenic agent" vs "LLM agent" | logogenic agent | +3 | Names the *structural property* (language-constituted), not the technology. Future-proof against AI architectural change. Keep. |
| "actuated agent" vs "purposeful agent" | actuated agent | +3 | Formal-term choice documented in LEXICON; "purposeful" remains fine in informal prose but "actuated" is the formal token. Keep. |
| README.md "What This Is" | README.md "What Agentic Systems Is" | +1 | Current section reads generically; naming the framework in the heading anchors the reader. Minor, opportunistic. |
| README.md "Novel Results" | README.md "Novel Results" | +1 | Fine; perhaps "Results that Emerge at the Joints" to match the theory's integration-over-invention framing, but that's longer and less grep-able. Weak keep. |
| README.md "Convergent Choices" | README.md "Forced-by-Failure Choices" | +1 | "Convergent choices" is accurate but mild. "Forced by failure" captures the spike-everything-else-fails story that the section tells. Low conviction; explicit alternative. |
| README.md "Maturity Gradient" | README.md "Maturity Gradient" | +1 | Fine. Keep. |
| "spike" (in msc/) | spike | +3 | Established project vocabulary; "spike" carries the exploratory-detour-from-main-workflow shape. Keep. |
| "candidate" (stage) | candidate | +3 | Terminal pre-publication stage; works because it's standard academic vocabulary. Keep. |
| `claims-verified` / `deps-verified` / `format-clean` | `claims-verified` / `deps-verified` / `format-clean` | +3 | Each stage name encodes exactly what was verified. Self-documenting. Keep. |
| "cold-start" (in naming-principles.md) | cold start | +1 | Common vocabulary; fine. |
| "communal-imagination test" (in naming-principles.md) | communal-imagination test | +1 | Nicely named; a test-shaped thing that can be referenced by name. Keep as established vocabulary for this audit. |
| "token-level commitment" (for #agent-identity) | token-level commitment | +3 | Type/token distinction is borrowed from philosophy-of-language, used correctly, and now first-class in #agent-identity. Keep. |
| ε-greedy | ε-greedy | +3 | Standard external term (RL). Preserve. |

## Principles-observations

A few notes on where the principles file felt under-specified for me; flagging for round-2 refinement:

1. **Capitalization as a memorable-noun lever.** Several AAD concepts (Correlation Hierarchy, Convention Hierarchy, Pearl Causal Hierarchy) already function as named objects in prose but are inconsistently capitalized across segments. The principles file does not name capitalization-as-first-class-proper-noun as a tool; I started using it in my own votes. Worth making explicit in round 2.

2. **The difference between "locking in an already-idiomatic name" and "renaming."** Several of my +3 keep-votes are for concepts that already have effective names (strengthen-first posture; inevitability core; epistemic architecture; calibration laboratory) but aren't yet canonicalized as first-class project vocabulary. The principles file treats these as if "keep" is a default, but there's a meaningful distinction between "keep, status quo" and "keep, and now *canonicalize* — reference by this name everywhere, stop paraphrasing." The weight scale could have a fourth gradation (or a column flag) for this.

3. **Naming currently-unnamed things ≠ creating a neologism.** A significant fraction of my highest-value rows are "[unnamed: X] → propose name Y" where X is a pattern the theory already uses prose-paraphrases for. These are different in character from "rename established segment Z." The principles file treats them together; separating them might help aggregation.

4. **Symbol-to-English parity.** I voted for surfacing English names for α₁/α₂/β/κ_processing without renaming the Greek symbols. This is a different kind of move than either rename or keep — it's "add an English alias and use it in prose; retain the symbol as shorthand." Might deserve its own weight notation (e.g., +Pe for "parity-enforce English alongside symbol").

5. **Overload-detection as a first-class analysis.** The principles file names overload risk (criterion 4) but doesn't systematize it. The "hierarchy" four-way overload I flagged, the U_o / U_O near-homograph, and the "strategic" proliferation in Section III are all of a kind — project-wide collision audits worth doing once end-to-end rather than row-by-row. Might be a separate analysis to commission.
