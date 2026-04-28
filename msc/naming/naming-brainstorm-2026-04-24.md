# Naming Strategic Sweep — A Brainstorm Over the Whole Project

*Working document, 2026-04-24. This is a thinking-out-loud paper, not a set of proposals to ratify. It surveys the project's naming landscape, flags what's pulling weight and what isn't, and opens a conversation rather than closing one. Tier labels follow the project convention (Robust qualitative / Heuristic / Conditional / Open), with most suggestions tagged Heuristic because naming judgments are irreducibly aesthetic.*

---

## 1. Why naming deserves a dedicated pass

Names are the user interface of a theory. Every reader — every future agent with 100% context turnover, every collaborator returning after months, every external reviewer auditing a section out of context — encounters the concepts through their names before they encounter the mathematics. A good name compresses the key intuition into a few syllables that survive working-memory pressure; a poor name forces the reader to re-derive what the concept means on each encounter, paying compounding interest forever.

Two concrete examples from elsewhere in this project make the stakes visible. *Satisfaction gap* and *control regret* are names that do work for the reader — after one exposure, the 2×2 disambiguation table organizes itself in the reader's head because the two axes are evocatively, memorably, and accurately named. By contrast, the *A2' sub-scope α₁ / α₂ / β partition* captures something load-bearing in the theory but the name is a sequence of subscripts, primes, and Greek letters that requires a decoder ring on every encounter. The mathematics is the same quality in both cases; the naming is not.

This is not a cosmetic concern. AAD is trying to seed communal imagination around a set of structural ideas that the reader has never seen assembled this way before. **Memorable names are the substrate of communal imagination** — a community can argue about, extend, and apply *directed separation* more easily than it can argue about a thing with a clinical multi-word label, because the name has enough shape for a group of minds to get purchase on collectively. (Joseph's own framing in `msc/joseph-working-notes.md` §2: *"memorable names for the right concepts open up the communal imagination."*) This matters for a framework whose value is integrative — the work is done when others can wield the concepts without the original authors in the room.

The question is not "should we rename everything." It is: **which names are doing load-bearing work, which are coasting, which are causing friction, and where are the missing memorable-noun slots that would repay a deliberate act of naming?** Some names were early placeholders that just propagated via shear momentum and an unjustified assumption that they were named deliberately or carefully. *Now* is the time to revisit all of those assumptions.

## 2. Evaluation criteria

Extracted from Joseph's working-notes framing plus project conventions:

1. **Self-descriptive vs. baggage-carrying.** A name can either try to *describe* its referent from scratch ("information bottleneck") or *adopt* existing baggage from an adjacent field ("sector condition," "Lyapunov function"). Both can be right. Self-descriptive wins when the field lacks prior art; baggage-adoption wins when the prior art's structural intuitions should travel with the name. The worst outcome is a name whose *only* content is the baggage, when the theory means something subtly different than the baggage implies (e.g., "Update Cycle", "LLM", ...).

2. **Familiarity gradient.** For each named concept: how many seconds of unfamiliarity does a trained reader in the adjacent field experience? Zero (they see "Lyapunov" and know what to expect) is usually good but occasionally dangerous (if AAD's usage differs from the baggage, the name creates false confidence). High unfamiliarity is usually bad but occasionally good (a novel name signals a novel concept).

3. **Memorable-noun potential.** Does the name render as a *thing* that can be named in discussion without paraphrase? "Chronica" is a thing. "The AAD complete interaction history with temporal ordering" is not. The asymmetry compounds across every conversation the community will ever have.

4. **Overload risk.** Does the word collide with other uses in the same project, or in adjacent AI/ML vocabulary? The word "hierarchy" appears in Pearl's causal hierarchy, in AAD's convention hierarchy, in AAD's correlation hierarchy, and in approximation tiering — four distinct uses in one framework, which is likely too many.

5. **Scope honesty.** Does the name over-promise relative to what the concept actually delivers? This is AAD's own distinctive epistemic posture applied to naming: if a name suggests more generality, more exactness, or more novelty than the concept provides, it violates the same scope-honesty commitment that the rest of the framework holds itself to.

6. **Aging potential.** Names age differently: some harden into standard vocabulary, some drift into embarrassment, some become locked in by citation velocity even when better options become available. Names that are too cute age poorly; names that are too clinical never attract citation in the first place.


# One Agent's Brainstorm


## 1. What's working — names that are pulling their weight

These should not be touched. Listing them matters because a brainstorm that only surfaces weaknesses creates a false impression that everything needs changing.

- **Satisfaction gap / control regret** — the crispest pair in the project. The 2×2 diagnostic table is memorable *because* the names are memorable. Leave alone.
- **Chronica (𝒞_t)** — Greek root ("records of time"), avoids the collision with ℋ (Shannon entropy) in notation and speech, carries the right philosophical weight for the singular non-forkable trajectory commitment. The etymology pays off in Class 5 (logozoetic) extensions where temporal depth becomes morally load-bearing. Keep.
- **Aporia** (and the cycle-phase vocabulary: *prolepsis / aisthesis / aporia / epistrophe / praxis*) — adopts ancient philosophical vocabulary with intentional resonance to what the cycle-phase does. The risk is preciousness; the payoff is that the five phases become memorable as a sequence rather than as five separate technical terms. This is a deliberate aesthetic commitment of the project and it works. Keep.
- **Orient cascade** — resonates with OODA without being captured by it; "cascade" conveys the directional resolution-order (𝑀 update → Σ edge revision → feasibility check → 𝑂 revision) succinctly. Keep.
- **Adaptive reserve** (Δρ*) — two words, one intuition, immediately suggests the right mental model (shock absorber depth). Keep.
- **Update gain** (η*) — adopted from Kalman/control, baggage transfers correctly because AAD's η* plays exactly the role the control-theory reader expects. Keep.
- **Logogenic / Logozoetic** — deliberate neologisms that trade readability for precision and for memorable-noun slot ownership. Anyone who decodes "language-generated" vs. "language-living" gets something valuable; anyone who doesn't has to learn the term once. For framework-defining classes this is a good trade. Keep. See §9 for why the Greek-roots commitment specifically works for this tier of concept.
- **Identifiability floor** (meta-segment) — "floor" is a load-bearing metaphor. Cannot go below it without outside help; the machinery that escapes it is named as such. Keep.
- **Strategy DAG (Σ_t)** — adopted directly from the probabilistic graphical models literature; baggage transfers correctly. Keep.
- **Agent opacity** (𝐻_b^{A|B}) — "opacity" carries exactly the right intuition (the dual of observability; how unpredictable A is to B). Hafez et al.'s original 𝐻_b gets an AAD-native name that connects to Section III's information-loss framing cleanly. Keep.
- **Exploit / Explore / Deliberate** — the third term sits neatly beside two standard-vocabulary terms; the extension reads as an extension rather than a reinvention. Keep.
- **Sector-persistence template** — technical-clinical but clear; the meta-segment's role as shared lemma is legible from the name. Keep (but see §4 for the template-family naming question).
- **Auftragstaktik principle** — adopts a load-bearing term from a specific historical tradition; the reader who knows it gets the full intended intuition, the reader who doesn't gets an interesting keyword to look up. Keep.

## 2. Quiet successes — names that could be a little louder

A category for names that are technically adequate but could do more work with a small tweak.

- **Composition closure / closure defect (ε*).** "Closure" is a load-bearing abstract-algebra term that reads naturally here (the macro-dynamics closes against the micro-dynamics; the defect is the failure of that closure). "Defect" adds just enough of a physical/engineering flavor to make it memorable. *These are fine.* The small opportunity: the word "closure" alone is overloaded with computer-science closures (lexical scopes), so any casual mention out of context can land confusingly. A one-phrase prefix in Section III preamble (*"composition closure — the macro-level agent's dynamics close against its constituent agents' dynamics"*) inoculates the reader. Not a rename — a framing nudge.

- **Unity dimensions (𝑈_𝑀, 𝑈_𝑂, 𝑈_Σ).** "Unity" captures the three-axis coherence intuition well. But the term is floating — a reader hits $U_M$ unity and has to backtrack to the segment to remember what "unity" is measuring. A small framing move: in Section III preamble, state the *telos* unity is measuring ("how aligned are these agents' reality-models / objectives / strategies?"). The term stays; its referent becomes self-evident.

- **Sector-persistence template, contraction template, dissipativity template (proposed).** Good family name (*template*), but the three-member family could be introduced as a family explicitly in `#separability-pattern` or a new meta-segment, with naming rules. Currently each template reads as an independent piece; the family is the structure worth surfacing. If the bridge-lemma spike's proposed `#dissipativity-template` lands, the three-member family will be load-bearing enough to name as a family. Candidate family name: *persistence-template family* or *contraction/dissipation/sector trio*.

- **Correlation hierarchy (L0/L1/L1'/L2).** Pedagogically clean. The "L1'" notation (L1-prime) is a little awkward to speak; in conversation it tends to get glossed as "L1-prime" or "observable-C L1." If this hierarchy becomes load-bearing for outside readers (and it will, because it parallels Pearl's hierarchy), giving L1' a *name* rather than just a prime-decoration might help: e.g., *L1-observable* / *L1-latent* or *L1-C* / *L1-Ĉ*. Not urgent.

## 3. Drift risks — names with hidden baggage or ambiguity

Names that *work* for trained-in readers but carry baggage that might mislead others.

- **Directed separation.** The meaning in AAD is specific: the epistemic substate update *f_M* is not influenced by the purposeful substate *G_t*. The term has no broad usage in ML so it's mostly baggage-free — good. The small risk: "separation" in control theory evokes the separation principle (LQR/Kalman: optimal control policy can be designed independently of optimal state estimation). AAD's directed separation is a *different* kind of separation, but any control-theory reader will hear the echo. The connection is real — LQR is a canonical Class 1 agent — so the echo is not false, but it over-promises. A control-theorist reader may expect "directed separation" to deliver the separation-principle result specifically, and it doesn't. *Conditional proposal:* a one-sentence clarification in `#directed-separation` Discussion: "Directed separation is a structural property of architecture (goal-blind epistemic update); the classical separation principle is a consequence of linearity + Gaussianity, a stronger condition holding in LQR/Kalman as a special case." This is already partially done; could be sharpened. No rename.

- **Composition closure.** As noted above, the word "closure" is overloaded. Not bad enough to rename, but worth the framing nudge.

- **Strategic composition (§III segment).** The word "strategic" in AAD's `#strategic-composition` refers to multi-agent partially-opposing objectives — game-theoretic composition. But the word "strategic" is *also* used in AAD for anything Σ-related (strategy DAG, strategic calibration, strategic tempo). Two meanings in the same section. A reader hitting `#strategic-composition` for the first time can't tell whether this is "composition of strategy DAGs" or "composition of agents under game-theoretic strategy." It's the latter. *Heuristic proposal:* rename to `#game-theoretic-composition` or `#equilibrium-composition` (the segment's core move is equilibrium convergence under Monderer-Shapley / Rosen). This reduces the "strategic" overload and makes the segment self-announcing.

- **Convention hierarchy (C1/C2/C3).** The term "convention" is fine within AAD but for an outside reader, "convention" has a game-theory meaning (Lewis conventions, social convention) that is unrelated. The C-hierarchy is about *continuation policy choice* for value-object evaluation (one-step / receding-horizon / Bellman). *Conditional proposal:* rename to `continuation hierarchy` — more self-descriptive, loses the Lewisian baggage, same acronyms (C1/C2/C3) still work. No strong opinion; this may be over-reach.

- **Persistence — three senses (structural / operational / continuity).** The word "persistence" is carrying three distinct technical meanings in AAD, flagged in LEXICON. The three senses *are* related (they're all about the agent sustaining itself), and LEXICON disambiguates. But readers encountering "persistence condition" vs. "structural persistence" vs. "continuity persistence" need the LEXICON on hand. *Observation, not proposal:* the triple-meaning is load-bearing and probably irreducible. But each usage site could be explicit about which sense applies when it matters.

## 4. Anonymous technical names — accurate but forgettable

These names do their job but don't compound into community vocabulary. They are not *bad*; they are *quiet*.

- **Additive-coordinate-forcing.** This is arguably AAD's most distinctive structural move — a cross-cutting meta-pattern. The name accurately describes the machinery (Cauchy functional equation on additivity axioms forces logarithmic coordinates). But it is a five-syllable compound that no one will say twice in a conversation; in practice people will say "the Cauchy thing" or "the additive pattern" or just "forcing." The name has no *handle* for communal imagination to grip. **This is the single most important naming opportunity in the project** by my read: it's a load-bearing meta-pattern with multiple theorem-level instances, and it has no memorable name.
  
  *Brainstorm-grade candidates (Heuristic):*
  - **Cauchy coordinates** — names the mechanism and the output; short; crisp. Downside: "Cauchy" is overloaded in math (Cauchy-Schwarz, Cauchy sequences, Cauchy's integral formula).
  - **Additive lift / logarithmic lift** — names what happens (a logarithmic coordinate is lifted from an additivity axiom). "Lift" is the right verb structurally. Downside: "lift" is a common math term and may not stick.
  - **Axiom-forcing** — short, memorable, but less self-descriptive.
  - **Log-coordinate forcing** — more direct but verbose.
  - **Primary instance / anchor lattice** — if the "1-anchor-plus-3-theorem" structure becomes the frame, naming the lattice of forced coordinates as a *lattice* could work.
  
  My weak preference, pending Joseph's read: **Cauchy coordinates** for the named meta-pattern (mnemonic: "Cauchy forces the coordinate"); retain "additive-coordinate-forcing" as the long-form technical description in the segment title. The segment can be `#cauchy-coordinates` or `#additive-coordinate-forcing` — ideally the first with the latter as subtitle.

- **Separability pattern.** Similar issue. The concept is load-bearing (positive-half scope posture: separable core / structured repair / general open) but the name is a two-word clinical label. A reader will remember "the three-tier separability thing" but won't reach for the phrase in conversation. *Heuristic candidates:* 
  - **Separability ladder** (if the seven-ladder structure is the headline — "ladder" suggests climbing from easy cases to open cases, which is the geometry).
  - **Tiered separability** (less good; verbose).
  - **Separability staircase** (whimsical).
  - **Scope staircase** or just **the staircase** as shorthand.
  
  Weak preference: rename to `#separability-ladder` (ladder is the right geometry — discrete levels of increasing difficulty, ascending from separable-core upward). The current name survives as description.

- **Identifiability floor.** Already discussed in §3 as a success — "floor" works. Keep.

So of the three meta-segments forming AAD's "cross-sectional epistemic structure" per CLAUDE.md §7: `#identifiability-floor` has a good name; `#separability-pattern` is a candidate for `#separability-ladder`; `#additive-coordinate-forcing` is a candidate for `#cauchy-coordinates`. Together: **floor, ladder, coordinates** — three short concrete nouns for the three-part meta-architecture. The parallelism is a happy coincidence and might not survive scrutiny, but the mnemonic is lovely if it does.

- **Sector condition.** Adopted from nonlinear control (Khalil, Vidyasagar). The baggage is correct and load-bearing. Keep. No opportunity.

- **Gain-sector bridge.** Technical and clinical; does the job. A reader will remember what it does but not reach for the phrase. Not worth a rename; the concept is narrow enough that a slightly forgettable name is fine.

- **A2' sub-scope partition (α₁ / α₂ / β).** Genuinely load-bearing technical classification, but the naming is cryptic. "A2'" is the operator-sector condition under fidelity-degraded updates; α₁ is fixed-gain; α₂ is adaptive-gain; β is where A2' is assumed rather than derived. The names are fine as *symbols* but have no English equivalents the community can use. *Brainstorm-grade:*
  - α₁ → **derived-gain regime**
  - α₂ → **adaptive-gain regime**  
  - β → **assumed-sector regime** or **postulated-sector regime**
  
  Value: replace "this lands in α₁" with "this lands in derived-gain," which reads naturally in prose without requiring the reader to remember what α₁ means. The subscripts stay as shorthand; the English becomes pronounceable. *Weak proposal, low priority.*

## 5. The overloaded-word problem

Three words are doing too many jobs in AAD:

1. **Hierarchy** — Pearl's causal hierarchy (external, adopted), convention hierarchy (AAD-native, C1/C2/C3), correlation hierarchy (AAD-native, L0/L1/L1'/L2), approximation tiering (meta-pattern also called a hierarchy). Four uses. My read: the word is probably over-used but the four usages are all genuinely hierarchical (strict ordering with induced asymmetry), so the word isn't *wrong*. **Weak proposal:** reserve "hierarchy" for Pearl's and retain it for strict-asymmetry cases; rename correlation hierarchy to *correlation ladder* or *correlation tiers* if parallelism with the separability-ladder proposal is desired; convention hierarchy can stay (or become continuation hierarchy per §5). Approximation tiering already avoids "hierarchy."

2. **Strategic / strategy** — covers both Σ-related-anything and game-theoretic-strategy. Flagged in §5 re: `#strategic-composition`. Small rename on that segment suffices.

3. **Persistence** — three senses, flagged in §5. Probably irreducible.

## 6. The `-act-agent` slug relics

Two segments carry slugs that predate the 2026-04-16 ACT → AAD rename: `#developer-as-act-agent` (TST) and `#ai-agent-as-act-agent` (logogenic). Both read as relics — the "act" prefix was the old ACT (Agentic Cycle Theory) branding, not the English verb. Renaming is probably overdue.

Candidates:
- **`#developer-as-aad-agent`** — exact parallel to the old name. Pros: minimal change, preserves symbol alignment. Cons: perpetuates the pattern of embedding a framework name in a slug (fragile under further renames).
- **`#developer-as-adaptive-agent`** — drops the framework-name dependency; reads naturally. Pros: framework-agnostic slug; won't rot under future renames.  
- **`#developer-as-agent`** — simplest possible. Might be too generic.
- **`#developer-agent-mapping`** — reframes from "developer *is* an agent" to "here's the mapping from developer to AAD agent." Cleaner pedagogically.

My preference, weak: `#developer-as-adaptive-agent` and `#ai-agent-as-adaptive-agent`. These match the existing LEXICON agent-class vocabulary ("adaptive system / adaptive agent / actuated agent / logogenic agent / logozoetic agent") and won't rot. Both the current segments invoke the adaptive-systems layer (Section I's machinery applied to the domain), so "adaptive" is semantically accurate.

This is a mechanical rename once decided — I can execute it with appropriate dependency-propagation if you bless one of the candidates.

## 7. Memorable-noun opportunities

The meta-question: are there currently-unnamed *things* in the project that deserve a name? Joseph's working-notes phrasing: "possible 'Noun' category naming opportunities."

**Two flavors of opportunity** appear in this section, and the distinction is worth holding consciously when the naming-survey agents are briefed:

- **Existing mathematical objects without first-class handles.** A quantity, region, or pattern is referenced in the mathematics under multi-word descriptions but lacks a noun. The persistence envelope (the parameter region where the persistence condition holds), the chain anchor (the mathematical-identity foundation of `#disc-additive-coordinate-forcing`), the inferential-force cascade across the convention hierarchy. Naming these is largely *retrieval* — the math is there; the handle is missing.

- **Conceptual nuance the framework gestures at without formalizing.** A pattern the mental model uses pedagogically and operationally, but where the formal mathematics is fragmented across several segments under partial handles. The active-subset-of-$\Sigma_t$ bullet below is the canonical example: $E_{\text{load}}$ shows up in one segment, "active edges" in another, "current plan's critical path" in informal narrative — but the *thing*, the highest-level engaged subset of strategy that informs Praxis, isn't a first-class definitional object even though the mental model uses it constantly. Naming these is partly *retrieval* and partly *invitation to formalize* — choosing a name signals that the concept is load-bearing enough to deserve its own definition segment, even if the math underneath stays as fragmented as it is now.

The second flavor is rich ground for the project: a list of *areas waiting for new concepts to be named*, whether they have strict mathematical analogs or only conceptual nuance, becomes itself a research artifact — it tells the next round of segment-promotion work where the missing definitional segments are. This section is allowed to grow as those areas surface; the naming-survey agents should be briefed to flag candidates of either flavor.

My survey:

- **The sector-persistence template's persistence region.** AAD's persistence machinery produces, in each instantiation, a region of parameter space where the agent is guaranteed to maintain bounded mismatch. This region has no name. It's referenced as "the region where the persistence condition holds" or "the adaptive regime." Naming it — e.g., *persistence envelope*, *adaptive basin*, *ultimate bound region* — would give community discussions a handle. "The agent is well inside its persistence envelope" reads more crisply than "the agent satisfies the persistence condition with non-marginal adaptive reserve." *Brainstorm:* **persistence envelope** is my favorite (engineering vocabulary, geometrically evocative).

- **The "one point where AAD anchors the additive-coordinate-forcing family."** The chain-confidence-decay segment plays a special role: it is the *mathematical identity* (probability chain rule) that the three other theorem-instances (divergence, update, metric) each analogize. In the "1-anchor-plus-3-theorem" framing, the anchor has no name beyond its segment slug. Naming it — e.g., *the chain anchor*, *the additive anchor* — would let the three analog-theorems refer back to it naturally ("the update-layer analog of the chain anchor," etc.). *Brainstorm:* keep the segment slug as `#chain-confidence-decay`, but refer to the pattern's anchor as **the chain anchor** in prose.

- **The "convention hierarchy monotonicity corollary" — satisfaction gap decreasing, control regret increasing.** This *cascade of inferential force* is a key pedagogical point: under C1 you have weak diagnostics; under C3 you have strong ones; the 2×2 table's cells mean different things at different conventions. This pattern — cells that strengthen as the convention strengthens — is unnamed. Candidate name: **inferential force cascade** or just **inferential cascade**. Probably low priority but worth noting.

- **The "calibration laboratory" frame for TST.** CLAUDE.md positions TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measured exactly." This framing is already first-class but the *concept of a calibration laboratory* (a privileged domain for identification within a theoretical framework) is itself a reusable meta-move that other theoretical projects could borrow. Worth promoting the term to a memorable-noun slot: **calibration domain** or **calibration lab**. Low priority.

- **The cycle-phase sequence as a whole.** The five-phase sequence (prolepsis → aisthesis → aporia → epistrophe → praxis) is named piecewise but the sequence itself — the "full cycle of adaptation" as a Thing — has no collective name. "The adaptive cycle" works as description but is clinical; candidates like **the pentad**, **the five-turn**, or **the five-phase cycle** give the community a handle. Probably not worth a rename effort, but worth surfacing.

- **The active subset of $\Sigma_t$ — the strategy edges currently informing Praxis.** *Surfaced 2026-04-28 from a side conversation about what to name the project's portfolio file.* The theory has the concept under several partial handles: $E_{\text{load}}$ in `#deriv-detection-latency` (formal, "load-bearing edges on the current active plan," used to derive $n_{\min}$), "active edges" in `#def-strategic-calibration` with criticality weights $w_{ij}$, and "current plan's critical path" as the underlying narrative phrase. But no single first-class noun exists for the *thing*: the highest-level nodes of $\Sigma_t$ that are bearing the agent's weight in the current execution, and whose credences therefore directly inform the next $a_t = \pi(M_t, G_t)$. Joseph's reframing (more precise than my initial $E_{\text{load}}$ pitch): it's *closer to the highest-level nodes of the strategy DAG itself* — the strategy's currently-engaged frontier or root-set, not just the load-bearing edges. This distinction matters: edges bear weight; nodes are the action-relevant decision points where Praxis attaches.

  This is rich ground for refining the *mental model* even if the mathematical model stays as it is. Candidate names from the side conversation, all Heuristic, with classical flavor matching the cycle vocabulary:
  - **Φέροντα (Pheronta)** — Greek present participle of φέρω, "the bearing things." Maps directly onto $E_{\text{load}}$ but at edge-level, not node-level. English -phore root carries through.
  - **Πρακτέα (Praktea)** — Greek gerundive of πράττω, "things-to-be-acted-on." Pairs structurally with **Praxis** as cycle-phase: Praxis is the act, Praktea are its targets. Doesn't map directly onto $E_{\text{load}}$ but matches the "active strategy subset feeding action" sense better at the *node* level than the edge level.
  - **Practica** — pseudo-classical English-memorable form (Greek root πράττω + Latin -ica adjectival ending). Less archaic, more accessible than Praktea while preserving the structural pairing with Praxis. *Joseph's choice for the project's portfolio file* (OPERATA → PRACTICA, 2026-04-28) — sets a precedent for the larger naming convention if it earns its keep there.
  - **Στρατηγικά (Strategika)** — "the strategic things" (neuter plural). Very direct semantic mapping to "active areas of $\Sigma_t$." Modern-Greek tonality may make it too clinical.

  **Held in reserve:** **Ἔργα (Erga)** — Hesiod's "works/labors." Considered for the portfolio-file role and not chosen there (semantically closer to "the works underway" than to "active strategy nodes"), but may earn placement for some part of the **logozoetic taxonomy** (where weight-of-engagement / labor-of-being maps onto the moral-persistence machinery) or for some yet-unnamed quantity/attribute in the existing segments — perhaps something around the *cumulative-engagement* dimension that the framework currently doesn't formalize but that adjacent quantities (accumulated experience $n$, persistence-cost integral $\int \dot R\,dt$, lifetime tempo budget) gesture at.

  **Why this candidate area matters for the naming refactor.** The active-subset-of-$\Sigma_t$ concept is referenced *at least* three times in formal segments (detection latency, strategic calibration, schema-strategy-persistence) without a unified name. The mental model — "what is the agent currently working on" — is doing work in pedagogical conversations even though the mathematical formulation is fragmented. A first-class noun (and possibly a first-class definition segment promoting the concept) would: (a) tighten the load-bearing role of `#deriv-detection-latency`'s $n_{\min}$ argument, which currently has to redefine $E_{\text{load}}$ each time; (b) let `#def-strategic-calibration`'s "active edges" + criticality weights link into the same vocabulary; (c) give Section II a memorable-noun handle for what informs $\pi(M_t, G_t)$, instead of always saying "the strategy as a whole" when the agent is really only operating on a subset; (d) provide a natural pairing to Praxis at the cycle vocabulary level, completing the asymmetry where Praxis has a name but its targets don't. Worth feeding into the naming-refactor pipeline (OPERATA / PRACTICA's "Current naming conventions refactor" step 1) as a candidate-area in the survey instructions.

## 8. The "Actuation" problem in AAD itself

The framework's own name — *Adaptation and Actuation Dynamics* — has an asymmetry worth acknowledging. "Adaptation" captures Section I beautifully (it's exactly what Section I is). "Actuation" is supposed to capture Section II, which is about *purposeful* agency with explicit objectives and strategy. But "actuation" in engineering vocabulary (and in the reader's ear) means *the mechanical conversion of a control signal into movement*. It is the *output* step of a control loop, not the strategic/purposeful layer. A control theorist hearing "actuation dynamics" will expect servo-motor modeling, not strategy-DAG updating.

This is a real gap between the name and the thing. The alternatives previously considered — ACT (collided with AI Consciousness Test), TFT (narrower than what AAD now covers) — are worse, so the rename happened in April. But *Actuation* is semantically weaker than *Adaptation* for what Section II actually is.

Candidate alternatives (all Heuristic, all uncomfortable because framework renames are expensive):
- **Adaptation and Agency Dynamics (AAD)** — keeps the acronym; "agency" is a better fit for Section II's content. Downside: "agency" is extremely overloaded in AI discourse (agentic systems, AI agents, etc.) to the point of being marketing vocabulary.
- **Adaptation and Purpose Dynamics (APD)** — captures Section II's teleological content directly. Downside: acronym collision risk; doesn't roll off the tongue.
- **Adaptation and Actuation Dynamics**, with *re-framing* of "actuation" — retain the name; use the Section II preamble to explicitly name "actuation" as "the purposeful layer that actuates goal-directed action through strategy and objective." This is the lowest-cost move and probably right.

My read: **do not rename AAD itself.** It's a recent rename (2026-04-16); further thrash dilutes the identity. But the Section II preamble could do more work to establish what "actuation" means in this framework specifically, explicitly contrasting with the engineering actuator sense. A two-sentence addition would suffice.

## 9. The epistemic architecture naming question

CLAUDE.md §7 and the OUTLINE.md "Reading AAD" preamble establish that AAD's distinctive contribution — the thing that makes it more than "integration of [four subfields]" — is its **epistemic architecture** (scope-honesty-as-architecture, the three meta-patterns, the seven elements).

"Epistemic architecture" is a good phrase for this. It's also a *framing* phrase rather than a *thing* in the theory's formal apparatus. The question: should it become a named Thing — with a segment, a LEXICON entry, a formal definition?

*Weak observation:* the phrase is already operationalized through the three meta-segments (`#identifiability-floor`, `#separability-pattern`, `#additive-coordinate-forcing`). Naming a fourth meta-segment `#epistemic-architecture` would risk creating an umbrella term that simply re-states what the three meta-segments individually assert. Better: retain "epistemic architecture" as framing language in OUTLINE.md and CLAUDE.md, and let the three concrete meta-segments do the technical work.

*Counter-consideration:* if the meta-segments get renamed (floor / ladder / Cauchy-coordinates per §6), they form a trio whose collective noun might be worth naming. *Epistemic architecture* fits. **Lowest-priority proposal:** if and when the three meta-segments are renamed as a trio, the collective-noun slot is **the epistemic architecture** (not a segment, but an OUTLINE-level section heading in §A).

## 10. Proposals, prioritized

Pulling the above together. All proposals are Heuristic unless marked otherwise; none is load-bearing enough to execute without your read.

**Priority 1 — mechanical, high confidence:**
- Rename `#developer-as-act-agent` → `#developer-as-adaptive-agent` (TST)
- Rename `#ai-agent-as-act-agent` → `#ai-agent-as-adaptive-agent` (logogenic)
- Update all depends-graph references accordingly

**Priority 2 — naming refinements, judgment call:**
- Rename `#additive-coordinate-forcing` → `#cauchy-coordinates` (retain the long-form as subtitle)
- Rename `#separability-pattern` → `#separability-ladder`
- Together with `#identifiability-floor`, this gives the trio **floor / ladder / Cauchy-coordinates** — three concrete nouns for the three-part meta-architecture
- Rename `#strategic-composition` → `#game-theoretic-composition` or `#equilibrium-composition` (reduces "strategic" overload)

**Priority 3 — framing nudges, no rename:**
- Add a Section II preamble clarification of "actuation" (distinguishes from engineering actuator sense)
- Add a Section III preamble clarification of "composition closure" (inoculates against the CS closures collision)
- Add LEXICON entry for **persistence envelope** as the named region (not currently named)
- Add a "reading AAD" framing sentence in OUTLINE.md for **chain anchor** as the mnemonic for the additive-coordinate-forcing structure (the mathematical identity + three theorem analogs)

**Priority 4 — optional, aesthetic:**
- Rename `convention hierarchy` → `continuation hierarchy` (self-descriptive; same C1/C2/C3 abbreviations)
- Rename `correlation hierarchy` → `correlation ladder` (parallelism with separability-ladder)
- Introduce English labels for A2' sub-scopes: *derived-gain regime* (α₁), *adaptive-gain regime* (α₂), *postulated-sector regime* (β)

**Non-proposals (explicit DO NOT):**
- Do not rename AAD itself
- Do not rename adopted concepts from external work (Pearl's hierarchy, Lohmiller-Slotine contraction, Monderer-Shapley potential games, Hafez's 𝐻_b, Tishby's information bottleneck, Bruineberg's Pearl-blanket, Miller's meta-machine and extreme transition motif, etc.) — the prior-art-integration convention forbids it and the integration value is lost if renaming
- Do not rename logogenic / logozoetic — they are deliberate neologisms holding reserved memorable-noun slots
- Do not rename the cycle-phase Greek vocabulary (prolepsis / aisthesis / aporia / epistrophe / praxis) — the aesthetic commitment is working

## 11. Meta-observations about the naming landscape

Three patterns worth noting beyond the individual proposals.

**Observation 1 — AAD's naming is stronger at the conceptual level than at the meta-structural level.** The individual concepts (satisfaction gap, chronica, orient cascade, update gain, adaptive reserve, directed separation, etc.) are well-named. The meta-structure (the three cross-cutting patterns, the A2' sub-scope partition, the "calibration laboratory" frame) is less-well-named. This is the normal trajectory — conceptual work comes first, meta-structural work comes later, and the naming lags. The naming sweep is well-timed because the meta-structure recently stabilized (2026-04 cycles).

**Observation 2 — AAD has a latent Greek-vocabulary commitment that could be made explicit.** Chronica, prolepsis, aisthesis, aporia, epistrophe, praxis, logogenic, logozoetic — the project uses Greek roots for its most-load-bearing conceptual names. This is a deliberate aesthetic-and-technical move (per the project's "integration, not invention" posture: the vocabulary is old; the synthesis is the contribution). **It may be worth stating this commitment explicitly somewhere** (README or LEXICON preamble) so that future renames and extensions honor it. Candidate future-Greek slots: a name for the *cycle-as-a-whole* (the pentad), a name for the *persistence region* (the envelope/horos), a name for the *epistemic architecture* (the schema/paideia).

**Observation 3 — The "communal imagination" test is the right test.** For every name in the project, the test question is: *could a skilled reader, six months after first encounter, refer to this concept in a conversation without looking it up?* Names that pass: satisfaction gap, control regret, chronica, orient cascade, identifiability floor, directed separation. Names that fail: additive-coordinate-forcing, separability-pattern, A2' sub-scope α₁/α₂/β, convention hierarchy. The communal-imagination test correlates with memorable-noun-slot ownership, not with self-descriptiveness — an evocative imprecise name beats a precise forgettable name.

## 12. Questions for Joseph

Things I cannot decide alone.

1. **Cauchy coordinates — yes / no / alternative?** The most consequential proposal in the paper. If yes, the three-meta-segment trio gets mnemonically unified; if no, stay with the current technical-clinical name.

2. **The separability-ladder rename — yes / no?** Lower stakes than Cauchy coordinates but part of the same trio move.

3. **The `-act-agent` relic renames — yes / no, and which target?** My default is `adaptive-agent`, but I want your blessing before touching segment filenames and their dependency propagation.

4. **Framework-level "actuation" re-framing — do you want the Section II preamble nudge, or is the current state fine?**

5. **Is there a *named* Greek-vocabulary commitment you want to make explicit, or should it remain implicit?** The project's aesthetic coherence around Greek roots is real; whether to document it is a style call.

6. **Did I miss anything big?** I deliberately stayed inside the 01-aad-core / 02-tst-core / LEXICON / OUTLINE landscape. If there are naming landmines in 03-logogenic-agents or 04-logozoetic-agents that I didn't surface, those are the areas most likely to need a second pass.

## 13. Epistemic status of this paper

*Heuristic throughout.* Naming is a judgment call, not a derivation. I have tried to apply the project's scope-honesty posture to the proposals themselves (each with an explicit tradeoff, none with "this is clearly correct"). Where I have a weak preference I have said so; where I am uncertain I have flagged it. None of the proposals should be treated as settled by this paper — the paper is the opening move of a conversation, not its resolution.

The communal-imagination criterion is itself a hypothesis: *names that pass the six-months-later-in-conversation test compound into community vocabulary; names that fail it don't.* I believe this but it is empirical. If it turns out that some technical-clinical names (e.g., `#sector-persistence-template`) do acquire communal currency, the criterion was wrong and the proposals based on it are weakened.

---

*Working-notes closure: this paper stays in `msc/` pending discussion. If proposals are accepted, they land as segment renames + LEXICON updates + CLAUDE.md §7 updates, not as a new segment. The paper's job is to end. — 2026-04-24*
