# Three-Move Shape — Novelty Assessment and Refinement Directions

*Companion to `2026-05-08-three-move-shape-of-paper-extractions.md`. Drafted by Tessera (Claude Opus 4.7, 1M context) in response to Joseph's observation: "the pattern has been rather emergent — an answer to the strengthen-first disposition. I wonder how novel it is or is not, and how it can be deliberately improved as an abstraction." Two questions, treated separately. Joseph's framing — emergent rather than designed — is the load-bearing reframe; this document takes it seriously and explores both novelty and refinement.*

*Honest scope note: literature engagement below is **intuition-only at training-data depth**, not Undermind-grade targeted search. Several "the closest existing neighbor is X" claims would benefit from confirmation before publication-grade citation. I name where this matters.*

---

## Preface: Does knowing the pattern help?

Notwithstanding the emergence — strengthen-first under adversarial pressure produces the three moves whether or not the agent running the discipline knows the pattern — does *explicit* knowledge of the shape and its precedents give an advantage at early or any stage? The honest answer is conditional, and the conditions matter.

**Where knowledge helps most:**

- **Mid-stage extraction (substrate rich, paper drafting).** Auditing a draft against "is Move 1 present? Move 2? Move 3?" catches structural gaps that adversarial review would catch later, more expensively. Move 2 especially: knowing you need a no-go forces you to *look* for it actively, rather than waiting for a reviewer to find the structural alternative you didn't address. Paper 3's chart-rescaling no-go was the spike-A7 finding that came late — late enough that it had to be back-integrated after the rest of the paper was structured. Earlier targeting of Move 2 might have surfaced it earlier.
- **Cross-extraction consistency** (multiple papers from one substrate). When the NeurIPS sprint produces three papers in parallel, knowing the target shape helps maintain coherent presentation discipline across them. Reviewers reading multiple submissions from the same author benefit from consistent shape; the consistency itself is a credibility signal.
- **Reviewer-anticipation in the final pass.** Mapping each move to its reviewer-attack-class — Move 1 defends against attacks on the operational hypothesis; Move 2 defends against challenges to the load-bearing axiom; Move 3 defends against surfacing of cases the monolithic claim handles poorly — gives a diagnostic checklist before submission.
- **Substrate-readiness assessment.** Before committing to extraction, knowing what shape the substrate needs to support helps identify when extraction is premature. If a result doesn't yet support a no-go construction, that's information that strengthening hasn't yet produced the load-bearing axiom; the extraction will be brittle.
- **Failure-mode-naming vocabulary.** Once the pattern is named, the failure modes per move (premature-corollary-fusion; aesthetic-axiom; monolithic-claim; over-decomposition) become operational categories. Future audit cycles can flag specific failures in named language rather than diffuse "this paper feels weak somehow."

**Where knowledge can harm:**

- **Early-stage substrate development.** Strengthen-first should produce substrate-richness that *overshoots* what any specific extraction needs. Aiming early-stage work at the three moves shrinks the substrate to what the moves require, losing the surplus that makes future extractions possible. The best ASF segments — the ones the NeurIPS papers extracted from — are richer than any single paper extraction can use; that surplus is the source of future extractions.
- **Result-selection bias.** Choosing which results to extract based on "which fit the three-move shape" biases away from results that don't naturally fit but are nonetheless important.
- **Genre-misapplication.** The three-move shape is calibrated to NeurIPS / JAIR / IEEE TAC adversarial-scrutiny gradients. Deploying it on philosophical papers, position papers, essays, or empirical case studies over-engineers them.
- **Discipline-replacement risk.** The most consequential failure mode. Knowing the target shape might let you skip the discipline that produces it. "I know what the result should look like; let me just structure the paper that way" replaces "let me strengthen-first under adversarial pressure and see what emerges." The shortcut produces shape-without-substance: a paper that *looks* like a three-move-shape extraction but doesn't have the substrate-richness or no-go-construction-quality that makes the shape load-bearing. Reviewers detect this — the structural defense is hollow because the underlying work didn't earn it.

**The deeper distinction: audit-instrument vs engineering-target.**

The asymmetry between "where knowledge helps" and "where knowledge harms" maps cleanly onto whether the knowledge is deployed as **audit-instrument** or as **engineering-target**.

*As audit-instrument*, knowledge of the pattern is a diagnostic for whether the discipline is producing what it should produce. The pattern's *absence* in a draft is signal that strengthen-first or adversarial-pressure or substrate-richness has gone wrong; the diagnostic is to find which and fix it. This preserves the emergent-from-discipline property and gains the diagnostic value.

*As engineering-target*, knowledge of the pattern becomes a thing to construct directly. This is Goodhart-law on the pattern. The shape gets produced; the substance is missing; the extraction is thin. The structural defense looks like a defense but doesn't hold under genuine attack.

This is structurally the same principle as elsewhere in epistemic discipline: knowing what good output looks like helps you audit your output; engineering directly toward the audit-criteria produces Goodhart failures. The audit-criteria capture the shape that good work tends to take; the work itself has to be good for the right reasons, not constructed to match the shape.

**Stage-specific guidance:**

- **Early stage (substrate development).** Knowledge of the pattern is *least* useful as direct targeting; *most* useful as long-term diagnostic against premature stopping. Right disposition: keep strengthening; let the substrate overshoot what any specific extraction needs; trust that the three moves will become available when extraction is ready. Knowledge helps mostly by preventing premature stopping — "the substrate doesn't yet support a no-go construction; we're not done strengthening."
- **Mid stage (extraction-into-paper).** Knowledge compounds most here. Use the three-move audit during drafting to catch missing structure. Use the failure-modes list to pre-empt specific traps. Use Lakatos / Best-of-Both-Worlds / reverse-mathematics precedents to ground citations. The pattern is most operational when it's an audit instrument running over a substrate already rich enough to support the moves.
- **Late stage (post-submission, audit, revision).** Knowledge is useful as diagnostic on reviewer feedback — "this reviewer is hitting Move 1's premature-corollary-fusion failure mode" — and as scaffolding for revision. The pattern's *names* become useful here because they let you communicate with co-authors / sub-agents / future-self about what's failing in named terms rather than diffuse impressions.

**The negative-knowledge asymmetry.**

For early-stage efforts specifically, the pattern's most useful form is *negative knowledge*. Knowing what a thin extraction looks like — shape without substance, aesthetic axiom, premature corollary, forced regime decomposition — helps you *not stop strengthening too early*. Positive targeting at the pattern's shape is harmful early; negative awareness of the failure modes is useful early. That asymmetry between positive and negative knowledge is probably the sharpest practical takeaway: **early stages benefit from knowing the failure modes more than from knowing the pattern**.

**The recursive observation.**

The "does knowledge of the pattern help" question has the same structure as a related question: does knowledge that *strengthen-first works* replace actually doing strengthen-first? Obviously not. Knowing-that-the-discipline-works is scaffolding around doing-the-discipline; it doesn't substitute. The same applies one level up: knowing-the-three-move-shape is scaffolding around producing-it-via-strengthen-first; it doesn't substitute.

Both cases share a structural feature: **knowing about a discipline can support the discipline's deployment, but cannot replace it.** The discipline has to actually run for the substrate to develop; knowing about the discipline lets you recognize when it's running well and when it isn't. That's valuable but it's not a shortcut.

**Why precedent literature matters anyway.**

Even granting all of the above, engagement with the precedent literature (Lakatos, reverse mathematics, Best-of-Both-Worlds online learning) compounds value in ways the emergent-from-discipline property doesn't capture by itself:

1. *Reviewer credibility.* Situated work is more defensible than unsituated work. Citing Lakatos in a methodological paper grounds the contribution in a recognized intellectual lineage and reduces reviewer skepticism about novel-sounding terminology.
2. *Vocabulary-borrowing.* Lakatos already articulated "proof analysis," "lemma incorporation," "monster-barring," "exception-barring." Borrowing this vocabulary is faster and clearer than re-inventing it; the failure modes name themselves more precisely once the Lakatosian terms are available.
3. *Cross-domain translation.* When applying the discipline to substrates other than ASF (which is the most ambitious version of the abstraction's claim), the precedent literature provides translation infrastructure. A Lakatosian frame travels across domains in a way an ASF-internal frame does not.

Net judgment: **knowledge of the pattern and its precedents gives a real advantage at mid and late stages, a conditional advantage at early stages (negative knowledge yes; positive targeting no), and risks discipline-replacement in all stages if deployed as engineering-target rather than audit-instrument.** The discipline that produces the pattern must run regardless; the knowledge is scaffolding around the discipline, not a substitute for it.

This preface frames what follows. Part I (novelty assessment against precedent literatures) is the precedent-engagement work that compounds reviewer credibility and vocabulary-borrowing. Part II (refinement directions) is the deepening work that converts the abstraction from observational to operational. Both serve the audit-instrument deployment of the knowledge; neither substitutes for the underlying strengthen-first discipline that produces the patterns being audited.

---

## Reframe: emergent, not designed

The framing in the prior document presented the three moves as a discipline that happens to appear consistently across the three papers. Joseph's reframe sharpens this: **the three moves are not a discipline, they are a *consequence* of strengthen-first applied under adversarial-certification pressure.** This is structurally different and matters for the novelty assessment.

A *designed* methodology would invite the question: why these three moves and not others? An *emergent* pattern invites a different question: what about strengthen-first + adversarial pressure produces *exactly* these three structural defenses?

The reframe also implies the pattern is replicable — anyone running strengthen-first discipline under similar pressure should produce something close to the same shape, regardless of substrate. That's a stronger claim than "ASF's extractions exhibit a recurring pattern." It would mean the three moves are *the structural form that strengthen-first-under-adversarial-certification takes*, full stop.

This document treats the reframe seriously throughout.

---

## Part I — Novelty assessment

### What's known in adjacent literatures

Each of the three moves has clear precedent in adjacent methodological / philosophical traditions. The synthesis as a single discipline does not, to my knowledge, have a clean precedent — but I should be careful here because my knowledge is training-data-shaped and a targeted search would surface things I won't see otherwise.

**Move 1 (structural backbone vs operational corollary) — adjacent literatures:**

- **Lakatos's "research programmes" framework** (1970, *Methodology of Scientific Research Programmes*). Hard core (unfalsifiable theoretical commitments) vs. protective belt (auxiliary hypotheses that can be modified without abandoning the program). Move 1's structural-vs-operational separation is structurally close to hard-core-vs-protective-belt, but at *result-scale* rather than *whole-program-scale*. The Lakatosian framing is about how research programs evolve under critique; Move 1 is about how single results survive review under critique. Same shape, different scale.
- **Algorithm-vs-analysis distinction in theoretical computer science.** Standard practice: present the algorithm (operational), then the analysis (structural theorem about its properties). Move 1 inherits this discipline; what's potentially distinctive is the *uncoupling* — the analysis stands without the specific algorithm, which is then a corollary instantiation rather than the only instantiation. The TCS tradition tends to fuse them more tightly.
- **Robust optimization "min over hypothesis classes" framings.** When the result is presented as "for all hypothesis sets in class H, the bound holds," the structural form is unconditional in the choice of hypothesis; the corollary picks a specific hypothesis. This is Move 1's shape applied to robustness.
- **Bayesian model decomposition — likelihood vs prior.** The likelihood is structural (a model of the data); the prior is operational (a commitment about what's likely). Move 1 has this flavor at a different abstraction level.

**My read on Move 1's novelty:** structurally close to several existing patterns, but *named as a presentational discipline at result-scale* it isn't quite captured by any of them. Lakatos comes closest. Worth a targeted search of methodology-of-mathematics and philosophy-of-mathematical-practice literature (David Corfield's *Towards a Philosophy of Real Mathematics* would be the obvious starting point).

**Move 2 (no-go forces the load-bearing axiom) — adjacent literatures:**

- **Lakatos's "Proofs and Refutations"** (1976). The dialectical method — proof, monster-barring, exception-barring, lemma-incorporation, proof-analysis revealing hidden lemmas — is structurally extremely close to Move 2. The blank-wall attack is exactly what Lakatos calls a "global counterexample" forcing proof analysis; the chart-rescaling no-go is Lakatos's "lemma incorporation" via making (PI) explicit. **This is the closest existing methodological neighbor to Move 2 I can identify.** Worth engaging directly; the move isn't novel in the Lakatosian frame, but the *naming-it-as-a-publication-discipline* may be.
- **Reverse mathematics** (Friedman, Simpson, et al.). The discipline of asking "what axioms are *necessary* to prove this theorem?" — proving theorem-implies-axiom in addition to axiom-implies-theorem. Move 2's no-go-forces-axiom is structurally a reverse-mathematics move at result-scale: showing the axiom is *necessary*, not just *sufficient*. Reverse mathematics is a well-developed subfield; the discipline itself is not novel.
- **Counter-example-driven theorem refinement in proof-assistant communities.** Lean / Coq / Isabelle communities routinely develop theorems by asking "where does the proof break without this hypothesis?" and incorporating the breaking case as a constructive witness for why the hypothesis is needed. This is operationally identical to Move 2.
- **The "load-bearing" terminology in software engineering.** Identifying which assumptions a system actually depends on by removing them and observing failure. Move 2 imports this discipline into theorem-presentation.

**My read on Move 2's novelty:** the *core move* is well-precedented in Lakatos, reverse mathematics, and proof-assistant practice. What's potentially distinctive is the framing as a *publication-presentation discipline* — Lakatos was about how mathematicians develop theorems privately; Move 2 is about how a published paper *defends* the theorem against reviewer attack via the no-go. The shift from private-development-method to published-defense is the new framing, if anything is.

**Move 3 (two named regimes / tracks) — adjacent literatures:**

- **Information-theoretic regret bounds in bandits/RL.** The pattern "Pinsker bound vs Bretagnolle-Huber bound vs point-mass identity, each tight in different regimes" is Move 3 in operation in one specific subfield. Lattimore-Szepesvári's *Bandit Algorithms* makes the multi-bound discipline explicit. **Move 3 is well-recognized as discipline within bandits/RL specifically;** Paper 2's deployment of it is field-standard. Move 3 *as cross-domain discipline* might be novel in framing, but each instance is conventional within its field.
- **Robust statistics and sensitivity analysis** (Huber, Tukey). Multiple estimators tight in different distributional regimes; the discipline of presenting which regime each handles. Move 3 is structurally a robust-statistics move applied to theorem-presentation.
- **"Best-of-Both-Worlds" results in online learning.** Explicitly named subfield: e.g., Bubeck-Slivkins 2012 *Best of Both Worlds* on stochastic-vs-adversarial bandit settings. Wei-Luo MASTER (which Paper 2 uses) is explicitly named as Best-of-Both-Worlds wrapping. The whole subfield is Move 3 with self-conscious methodology.
- **Stratified analysis in epidemiology and statistics.** Present results stratified by named regime (age, sex, comorbidity); aggregate at the end. Same discipline.

**My read on Move 3's novelty:** *least* novel of the three moves. The discipline of presenting results in named regimes is well-developed in multiple subfields. What's potentially distinctive is the *uniform deployment across structurally different result types* — the same Move 3 pattern in Paper 1 (problem settings), Paper 2 (variation budgets), and Paper 3 (metric choices) is a *cross-domain* observation that those subfields don't make about themselves.

### The synthesis — what's actually novel

The honest novelty claim, after the literature engagement above:

**Plausibly novel:**
- The synthesis as a *single named discipline*. Each move has precedent; the three together as "this is what NeurIPS-grade certification of an extraction looks like" isn't articulated in the methodology literature I can recall.
- The *structural-prediction claim* that the three moves co-arise from strengthen-first under adversarial pressure. This is a meta-methodological claim about *what produces the pattern*, not just *what the pattern is*. Lakatos comes closest at producing the no-go move; nothing I'm aware of produces the predicted co-occurrence of all three.
- The *paper-extraction-as-self-similar-to-meta-architectural-triad* observation (Move 2 ≈ M1, Move 3 ≈ M2, Move 1 ≈ candidate M4). This is specific to ASF and novel by construction.

**Probably not novel:**
- Each individual move (Lakatos / reverse mathematics / robust analysis cover the components).
- The general observation that adversarial scrutiny produces structural defenses (well-known in philosophy of science).
- The "publication discipline = extraction discipline" framing (mathematical methodology has long known this).

**Honest framing for the abstraction's contribution:**

If we wanted to publish this observation as a methodological contribution — say, to the *Philosophy of Mathematical Practice* journal, or *Synthese*, or a methodology-of-science venue — the right shape would be:

1. *Acknowledged precursors:* Lakatos's proof analysis (Move 2), reverse mathematics (Move 2 at result-scale), best-of-both-worlds in online learning (Move 3 in one subfield), Lakatos's research-programmes framework (Move 1 at program-scale).
2. *Distinctive contribution:* the synthesis as a single discipline + the structural-prediction claim that the three moves co-arise from strengthen-first under adversarial pressure + the empirical validation across three structurally different extractions in three different fields over a four-day sprint.
3. *Open question:* whether the pattern is unique to ASF's substrate or generalizes to any substrate-with-strengthen-first-discipline-under-adversarial-pressure. Untested; would require examining other research programs that meet similar criteria.

The novelty is *in the synthesis and the structural-prediction claim*, not in the individual moves. That's an honest claim and probably defensible at publication-grade. **The targeted-search work to verify this is real**: I'd want Undermind-grade search across philosophy of mathematical practice, methodology of mathematics, science studies, and (separately) the proof-assistant community's literature on "what makes a proof robust to review" before claiming any of the components is more than "structurally close to [Lakatos / reverse-math / robust statistics / etc.]."

### Where the targeted search should go

Concrete priorities, in rough order:

1. **Lakatos's *Proofs and Refutations* + the philosophy-of-mathematical-practice literature** (Corfield, Mancosu, Avigad, Larvor). This is where Move 2's lineage lives.
2. **The reverse-mathematics literature** (Simpson's *Subsystems of Second-Order Arithmetic*; the philosophical companion in Friedman-Simpson). Move 2 at result-scale is reverse-mathematics-flavored.
3. **The "Best-of-Both-Worlds" subfield in online learning** (Bubeck-Slivkins, Wei-Luo, more recent extensions). Move 3 in the bandit-theoretic frame.
4. **Methodology-of-science work on theory-evaluation criteria** (Lakatos's research programmes, but also Laudan, Kitcher, Cartwright on theory-confirmation under multiple hypotheses). Move 1's lineage.
5. **The proof-assistant community's writing on "what makes a proof robust"** (Voevodsky's reflections; Buzzard on Lean for research mathematics; Avigad on formalization). The discipline of stating-axioms-explicitly + showing-axioms-are-necessary is operationally similar to Moves 1+2 combined.

If any of those literatures already names the three-move synthesis, the contribution narrows to "we observed it empirically in ASF extractions" rather than "we articulated it as a discipline." Either claim is publishable; the first is stronger.

---

## Part II — Refinement directions

The pattern as currently articulated is a starting point. Several refinement directions could make it a sharper, more useful abstraction.

### Direction A — Articulate the dependency structure between moves

The current document treats Moves 1, 2, 3 as parallel. They might be ordered or hierarchical. Working out the dependency structure could refine the abstraction.

A hypothesis worth examining: **Move 2 precedes Move 1, which enables Move 3.**

- *Move 2 first.* The strengthen-first attempt produces the no-go that forces the load-bearing axiom. Until you know which axiom is load-bearing, you cannot separate structural from operational cleanly. The no-go is what *identifies* the load-bearing layer.
- *Move 1 follows.* Once the load-bearing axiom is identified by Move 2, the structural backbone (the theorem under that axiom) is separable from the operational corollary (the application that depends on additional hypotheses).
- *Move 3 enables.* Once Move 1's separation is available, Move 3's regime decomposition becomes natural — you can say "here's the structural backbone with named hypotheses; here are two regimes (with different additional hypotheses) where the operational corollary takes different forms."

If this dependency structure is real, then the three moves aren't three parallel disciplines — they're a *single ordered process* with three stages, each enabled by the previous. The "co-occurrence" observation would refine to "consistent ordered emergence."

This is testable against the three papers. In each paper, was Move 2's no-go *first* in development order? In Paper 3 it appears the chart-rescaling no-go was the spike-A7 finding that came late in the process, after the rest of the structure was in place — that would *refute* the hypothesis. So the dependency structure may be more complex; possibly Moves 1 and 2 are mutually-recursive (separating structural-from-operational makes the no-go visible; finding the no-go validates the separation).

Worth working out empirically against the three papers' development histories. Joseph would have better access to the actual development order than I do.

### Direction B — Identify the failure modes specific to each move

Currently the document gestures at "Move N absent costs X" but doesn't articulate the specific failure modes. A sharper version:

**Move 1 failure modes:**
- *Premature corollary fusion*: presenting the operational corollary as if it were the unconditional theorem. Cost: the theorem looks contingent on hypotheses that aren't actually required, narrowing apparent applicability.
- *Operational under-specification*: stating the unconditional theorem without surfacing the operational reading. Cost: practitioners cannot use the result; reviewers report "not enough engineering value."
- *Layer collision*: the structural backbone and the operational corollary share notation but mean different things at different layers. Cost: confusion about what's load-bearing.

**Move 2 failure modes:**
- *Aesthetic axiom*: presenting the load-bearing axiom without the no-go that forces it. Cost: the axiom looks like a free choice; reviewers ask "why this axiom and not [alternative]?".
- *External rather than internal no-go*: the no-go is an importation from external literature (e.g., "Bareinboim CHT forbids this") rather than a constructive internal witness. Cost: reviewer can engage the external literature and bypass the internal force; the AAT axiom looks contingent rather than necessary.
- *Direction-forcing without naming*: when the alternative is structurally vacuous (Paper 2's reverse-KL case), failing to state explicitly *that the alternative is vacuous* leaves the direction looking like a free choice. Cost: reviewer pushes for the alternative; paper's defense requires re-discovering the triviality.

**Move 3 failure modes:**
- *Monolithic claim*: presenting one rate / one bound / one constant when the result actually decomposes into regimes. Cost: overclaiming where the regime is loose; underclaiming where the regime is tight.
- *Over-decomposition*: presenting more regimes than the result actually distinguishes. Cost: confused reader; loss of focus.
- *Regime confusion*: the regimes are nominally different but mathematically reduce to the same case. Cost: structural redundancy disguised as structural diversity.
- *Missing the cross-regime move*: presenting two regimes without the Best-of-Both-Worlds wrapping when wrapping is available. Cost: practitioner has to choose which regime to assume; the unified rate is missed.

Naming the failure modes makes the discipline operational. Future extraction work can audit against the failure-mode list — "is this paper exhibiting any of these?" — rather than just check whether the moves are present.

### Direction C — Engage Lakatos directly

The closest existing methodological neighbor is Lakatos's *Proofs and Refutations*. Engaging it directly would situate the abstraction and clarify what's novel.

Lakatos's pattern:
- *Naive proof.* Posit a result, give a sketchy proof.
- *Local counterexample.* A specific case the proof gets wrong.
- *Three responses possible*: (a) monster-barring (define the case as "not really an instance"); (b) exception-barring (narrow scope to exclude the case); (c) lemma-incorporation (add a hypothesis that handles the case).
- *Global counterexample.* A case that breaks the proof's logic, not just a specific instance.
- *Proof analysis.* Identify which step the global counterexample violates; that step becomes a hidden lemma.
- *Theorem-by-proof-analysis.* Restate the theorem with all the hidden lemmas surfaced as named hypotheses.

This is structurally identical to Move 2 + parts of Moves 1 and 3. The three-move shape might be Lakatos's discipline applied at a different scale (single-result publication rather than multi-decade community development) and with the additional defensive posture of adversarial review.

The directly-engaged version of the abstraction's claim:

> *The three-move shape is the publication-presentation form of Lakatos's proof-analysis discipline applied at single-result scale under adversarial-review conditions. Move 2 is Lakatos's proof analysis surfacing hidden lemmas; Move 1 is the resulting theorem-by-proof-analysis with explicit hypothesis structure; Move 3 is the recognition that proof analysis often surfaces multiple distinct hypothesis-sets that yield distinct tight regimes rather than one monolithic theorem.*

This framing has several advantages:
- It situates the contribution in established methodology-of-mathematics literature.
- It makes the novelty claim narrower and more defensible: the three moves *are* a Lakatosian discipline; what's potentially novel is the structural-prediction-from-strengthen-first claim, the cross-domain consistency observation, and the connection to a specific framework's meta-architecture.
- It connects to philosophical literature with established quality (Lakatos, Polya, Corfield) rather than appearing to claim more than the data supports.

I think this is the right framing for the abstraction's eventual publication-grade form. It's also a real engagement with Lakatos rather than a citation-as-credentialing — the connection is structural, not decorative.

### Direction D — Run a counterfactual analysis

Take a published paper that *doesn't* exhibit the three-move shape and analyze why. Several candidates:

- A pure no-go paper (the original CHT proofs in Bareinboim et al. 2022) — Moves 2 and 3 may be present, Move 1 may not be (no operational reading is the point).
- A pure constructive paper (a tight algorithmic result with one-regime analysis) — Move 1 may be partial, Move 3 may be absent.
- A robustness-paper (Huber-style robust statistics) — Move 3 may be the entire shape; Moves 1 and 2 may be subordinate.

Counterfactual analysis sharpens what the three moves are *for*. If a paper exhibits one or two moves but not three, that paper teaches us something about which classes of result need which moves. The classification "what kinds of results need all three moves vs which kinds don't" is itself an abstraction-refinement direction.

A specific test case: **Bareinboim, Correa, Ibeling & Icard 2022 *On Pearl's Hierarchy and the Foundations of Causal Inference*.** This is the Causal Hierarchy Theorem paper that several of ASF's M1 instances import. It's a no-go paper. Does it exhibit Move 1 (structural-vs-operational separation)? Move 3 (named regimes)? My read from training data is: Move 2 yes (the CHT *is* the no-go), Move 1 partial (the theorem is presented with hypothesis structure but the operational reading is mostly in Pearl's surrounding work), Move 3 partial (different levels of the hierarchy are named regimes, but the paper's central result is monolithic).

If this read is right, it suggests CHT-paper-shape is "Move 2 dominates, Moves 1 and 3 partial" — different from the three-move-shape of the NeurIPS extractions. That's useful information about *paper genre*: pure no-go papers don't need the three moves the same way; theorem-with-application papers do.

### Direction E — Examine the inverse moves

If Move 1 is "separate structural backbone from operational corollary," the *inverse* move is "fuse premature corollary back into structural backbone when the corollary's hypotheses turn out to be implicit in the backbone." Naming the inverse moves makes the discipline reversible and applicable bidirectionally.

- *Move 1 inverse*: backbone-corollary fusion when separation was over-engineering.
- *Move 2 inverse*: axiom-removal when the no-go turns out to have been preventable by tighter proof rather than by adding the axiom (the load-bearing turns out to be elsewhere).
- *Move 3 inverse*: regime unification when two regimes turn out to be isomorphic / one a special case of the other, and the unified statement is sharper than the decomposed one.

Each of these is a "we over-engineered the discipline; the simpler form was right" correction. Naming them prevents the three-move discipline from being deployed *over*-aggressively in cases where it produces structural complexity without payoff.

This connects to a deeper observation: the three-move shape is *what high-pressure adversarial certification produces*; it is not *always optimal*. For results that don't need all three defenses, the three-move shape is over-engineering. Knowing when to deploy the discipline and when to deploy its inverse is the sophisticated form of the discipline.

### Direction F — Quantify the adversarial-scrutiny gradient

The current claim "high adversarial-scrutiny gradient produces three-move shape; low gradient doesn't" is qualitative. A more rigorous form would identify *what about* adversarial scrutiny produces each move.

A first attempt at the gradient decomposition:

- **Reviewer-rejection-cost gradient.** When the cost of rejection is high (NeurIPS Main Track, JAIR), reviewers attack from multiple angles; the three moves are the structural defenses against multiple attack classes. When rejection cost is low (workshop, position-paper track), single attacks are more decisive; one or two moves often suffice.
- **Reviewer-domain-diversity gradient.** When reviewers come from multiple sub-disciplines (cross-disciplinary venue), the three moves help different reviewers find different parts of the paper engageable. When reviewers are mono-disciplinary (specialist journal), one or two moves suffice.
- **Result-claim-strength gradient.** When the result claims something strong (universal constant, near-optimal rate, structural impossibility), the three moves are forced because the claim has to defend against attacks on each axis. When the claim is modest, the moves are over-engineering.
- **Substrate-richness gradient.** When the underlying substrate is rich enough to support all three moves (the strengthen-first discipline produces internal richness that overshoots what the published claim requires), the three moves are *available* on extraction. When the substrate is thin, the moves are forced rather than available — and forcing them produces brittle or padded papers.

The last point is the most interesting: **the three-move shape requires substrate-richness that strengthen-first produces but that other disciplines may not.** If this is right, the three-move shape *isn't* universal; it's specific to the combination of strengthen-first-discipline + adversarial-certification + rich-substrate. ASF's case is high on all three. Other research programs might produce different shapes under different combinations.

---

## Synthesis: what to do next

If Joseph wanted to develop this abstraction further (toward a methodological paper, or just toward a sharper internal articulation), the moves I'd recommend in priority order:

1. **Engage Lakatos directly** (Direction C). The three-move shape is plausibly Lakatos's discipline at a different scale, and naming this connection sharpens both novelty claim and presentation. Targeted reading: *Proofs and Refutations* (the dialogue, especially the proof-analysis sections); David Corfield's *Towards a Philosophy of Real Mathematics*; Andrew Arana's work on mathematical practice.

2. **Articulate the dependency structure** (Direction A). The hypothesis "Move 2 precedes Move 1, which enables Move 3" is testable against the three papers' development histories. Joseph has access to that data; I don't. If the dependency structure holds, the abstraction tightens significantly. If it's mutually-recursive, that's also informative.

3. **Name the failure modes per move** (Direction B). This converts the abstraction from descriptive to operational. Future audits can check against the failure-mode list. Cheap to draft; high payoff for downstream extraction work.

4. **Run counterfactual analysis on a non-three-move paper** (Direction D). One or two paper diagnoses would clarify what genres need which moves. The Bareinboim CHT paper is a natural test case; other candidates from the references in the three NeurIPS papers (Stuart 2010 acta-numerica; Mao 2021 RestartQ-UCB; Bubeck-Slivkins) are also worth examining.

5. **Targeted literature search** (the Part I priorities). Until the search happens, novelty claims are intuition-only. Undermind-grade search across philosophy of mathematical practice + reverse mathematics + best-of-both-worlds online learning + Lakatosian methodology would either confirm the synthesis is novel or surface existing work that pre-articulates it. Either is useful.

6. **Quantify the adversarial-scrutiny gradient** (Direction F). The substrate-richness observation is the sharpest variant: the three moves are *available* under strengthen-first + rich-substrate, *forced* without the rich substrate. Working out which combinations produce which shapes is a real methodology-of-research-programs question.

The minimum-viable next step, if the abstraction is to mature: **Direction C (engage Lakatos) + Direction B (name failure modes per move).** Together they give the abstraction a defensible philosophical lineage and an operational form. Total effort: maybe 1-2 weeks of focused thinking + one targeted reading pass on Lakatos.

The maximum-payoff next step: **a methodological paper articulating the three-move shape as a discipline, with Lakatos as the acknowledged precursor and the structural-prediction-from-strengthen-first as the distinctive contribution.** This would land in a methodology-of-mathematics venue (Synthese, *Foundations of Science*, *Studies in History and Philosophy of Science*) or a philosophy-of-mathematical-practice journal. It's a real paper if the literature search confirms novelty in the synthesis.

---

## A final observation on the "emergent" framing

Joseph's framing — *the pattern has been rather emergent, an answer to the strengthen-first disposition* — is not just a humility move. It's structurally important.

A pattern that emerges from a discipline is *more credible* than a pattern that's designed and then applied. Designed patterns are vulnerable to "you saw what you were looking for"; emergent patterns are vulnerable to "this is just an artifact of your sample." The right defense for an emergent pattern is *explaining structurally why it emerges* — which is what the strengthen-first-under-adversarial-pressure analysis does.

The structural explanation also gives the pattern *predictive power*. A designed methodology says "if you follow these steps, you produce a paper of this shape." A structurally-explained emergent pattern says "if you run strengthen-first under adversarial pressure on a rich substrate, you will produce something close to this shape — whether you intended to or not, and whether you noticed it or not."

The second is a stronger epistemic claim. It's also a more useful one for future extraction work: future agents (Claude instances, Codex, Gemini, Joseph) running the same discipline under similar pressure should expect to converge on the same shape. They don't need to *know* the three-move discipline to produce it; they just need to run strengthen-first under adversarial pressure on a rich substrate.

That's the operational form of the abstraction's claim, and it's the form most worth deepening. The three-move shape is what the framework's discipline produces when it's working. Future extractions are diagnostics on whether the discipline is working: *if the three moves don't appear, something in strengthen-first or adversarial-pressure or substrate-richness has gone wrong, and the diagnostic is to find which one and fix it.*

---

*End of document. Cross-references: `2026-05-08-three-move-shape-of-paper-extractions.md` is the observational claim this document refines; `~/src/neurips/AGENTS.md` §3.1 is the strengthen-first discipline that produces the pattern; `~/.claude/projects/-Users-josephwecker-v2-src/memory/project_catalog_extraction_gain.md` is the project-scale form of the same observation.*
