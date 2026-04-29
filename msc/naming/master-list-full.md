# Naming Vote — Master List, Full View

**Source:** `msc/naming/naming-aggregate-r2-votes.json` (master generated 2026-04-29T17:08:46Z)
**Agents:** 19
**Total vote rows:** 2504
**Distinct currents:** 939
**Enrichment status:** consolidated_rationale: pending / first_encounter_locality: pending / segment_link: pending / manual_curation: pending

Per-current sections with enrichment fields surfaced where populated. Within each section: candidates as a table (with category mix, weight), then per-vote attribution + notes preserved verbatim from the source files. The lossless view — every per-vote note is here. Enrichment fields (consolidated rationale, first-encounter locality, segment link, manual curation notes) appear when the corresponding pass has filled them; otherwise marked _(pending)_.

---

## 1. `control regret`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +51 | keep × 7, canonicalize × 1 |
| strategy opportunity cost | -1 | rename × 1 |

### Candidate: `control regret` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Pairs with satisfaction gap; same reasoning.
- **codex-1** +3  — Crisp, properly scoped, and pairs perfectly with satisfaction gap.
- **codex-2** +3  — Strong adjacent-field baggage used correctly; it pairs beautifully with satisfaction gap.
- **codex-gpt-5-r2** +3 (keep) — Strong pair with satisfaction gap. It is familiar enough from regret language and still domain-specific.
- **codex-gpt-5-r2** +3 (keep) — This diagnostic should remain paired with satisfaction gap.
- **gemini-1** +3  — Perfect pairing with satisfaction gap.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Excellent pairing with satisfaction gap.
- **gemini-targeted-alternatives** +3 (keep) — Perfect partner to satisfaction gap. Captures the specific decision-theoretic regret tied to strategy revision.
- **haiku-4-5-r2** +3 (keep) — Companion to satisfaction-gap; the pair is load-bearing prose throughout. Both names compress intuition that survives working-memory pressure.
- **haiku-4-5** +3  — Dual to satisfaction gap; "regret" reads naturally as "current vs. best available" gap. The two names do *load-bearing work* for the discipline. Keep.
- **opus-1m** +3  — Pairs with satisfaction gap.
- **opus-4-7-b** +3  — Pairs with *satisfaction gap*. "Regret" imports RL baggage that is genuinely load-bearing (regret = best-achievable − current); "control" narrows it to the attainability layer.
- **opus-4-7-r2** +3 (keep) — Same load-bearing keep as `#def-satisfaction-gap`. The pair is the canonical illustration of "names that do work for the reader" in the principles file; do not rename either half.
- **opus-4-7** +3  — Pair-partner to satisfaction gap. The pair carries its decomposition load. Keep.
- **sonnet-4-6-r2** +3 (keep) — Same reasoning as satisfaction-gap — these two names work as a pair and are load-bearing for the 2×2 orient cascade diagnostic.
- **sonnet-4-6-r2** +3 (canonicalize) — Occasionally "strategy regret" or "execution regret" appears in working notes. The name "control regret" is established in NOTATION.md and LEXICON.md. Standardize.
- **sonnet-4-6** +3  — See above. The 2×2 disambiguation table works because both names work. Keep.

### Candidate: `strategy opportunity cost`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** -1 (rename) — A bit too generic economics terminology; "regret" explicitly ties to the mathematical formulation.

---

## 2. `satisfaction gap`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +51 | keep × 7, canonicalize × 1 |
| attainability shortfall | -1 | rename × 1 |

### Candidate: `satisfaction gap` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Crispest named pair in the project. 2×2 diagnostic table is memorable *because* the names are memorable. Do not touch.
- **codex-1** +3  — One of the cleanest names in the repo. The phrase explains the diagnostic almost by itself.
- **codex-2** +3  — One of the crispest names in the whole project; it is immediately intelligible without losing technical meaning.
- **codex-gpt-5-r2** +3 (keep) — Excellent diagnostic name for terminal conditions met while the objective remains unsatisfied.
- **codex-gpt-5-r2** +3 (keep) — This diagnostic should remain stable.
- **gemini-1** +3  — The 2x2 diagnostic with Control regret is perfect. Do not touch.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Crispest named pair in the project (with control regret). The disambiguation table is load-bearing.
- **gemini-targeted-alternatives** +3 (keep) — Crispest named pair along with control regret. Essential diagnostic dimension.
- **haiku-4-5-r2** +3 (keep) — Crispest named diagnostic pair in the project (paired with #def-control-regret); the 2×2 table organizes in readers' heads because the names do the work. High-weight keep against rename impulse.
- **haiku-4-5** +3  — Crispest named diagnostic pair in the project. The 2×2 disambiguation table (satisfaction-gap vs. control-regret axis; goal-attainability vs. strategy-quality) crystallizes in reader's mind because the axes are evocatively named. Do not touch.
- **opus-1m** +3  — Crispest pair in the project. The 2×2 disambiguation table organizes itself in the reader's head because of the naming. Do not touch.
- **opus-4-7-b** +3  — The 2×2 diagnostic composes with *control regret* into a cognitive apparatus the reader assembles in one exposure. Do not touch either half. The axes are *evocatively and accurately* named — a rare pairing.
- **opus-4-7-r2** +3 (keep) — Defended keep — and one of the cleanest names in the framework. The 2×2 disambiguation table works because "satisfaction gap" and "control regret" are *both* memorable on first encounter and *orthogonal* in a way the name signals. Renaming would lose a load-bearing prose convention. The Feynman-criterion test passes: an outside reader reading "satisfaction gap" can plausibly reconstruct "the world doesn't permit it."
- **opus-4-7** +3  — Crispest named pair in the project; the 2×2 diagnostic works because both names work. Explicit keep.
- **sonnet-4-6-r2** +3 (keep) — The strongest named pair in the project alongside control regret. The two-word name carries the diagnostic clarity that makes the 2×2 table work. Do not change.
- **sonnet-4-6-r2** +3 (canonicalize) — Occasionally paraphrased as "objective gap" or "attainability gap." The canonical name is established and load-bearing — standardize.
- **sonnet-4-6** +3  — Named pair with #control-regret. Both names pull equal weight: each is a two-word compound that tells you the diagnostic direction. The pairing is the insight; destroying either leg damages the whole. Keep both.

### Candidate: `attainability shortfall`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** -1 (rename) — "Satisfaction gap" explicitly ties into $V_O^{\min}$ being met. "Attainability" might refer only to $A_O$.

---

## 3. `orient cascade`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +47 | keep × 4, canonicalize × 1 |

### Candidate: `orient cascade` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Resonates with OODA without being captured by it; "cascade" conveys directional resolution-order succinctly.
- **codex-1** +3  — Memorable and faithful to the staged dependency structure; this is exactly the kind of communal-imagination name the project needs more of.
- **codex-2** +3  — Excellent memorable noun slot for a load-bearing ordering result.
- **codex-gpt-5-r2** +3 (keep) — Strong bridge term for the cross-cycle causal chain. It is memorable without being gimmicky.
- **gemini-1** +3  — Naming the sequential resolution order ($M_t \to \Sigma_t \to O_t$) as a "cascade" makes the information dependency instantly graspable.
- **gemini-2** +3  — Very evocative and action-oriented.
- **haiku-4-5-r2** +2 (keep) — The word "cascade" is evocative and accurate; the sequence is directional. Passes renamed-from-now-sounds-weird test.
- **haiku-4-5** +3  — Resolution order by info dependency. "Cascade" is evocative; "orient" echoes the OODA loop and the Greek philosophical term (epistrophe — turning toward). Reads naturally: "the orient cascade orders the updates." Load-bearing naming. Keep.
- **opus-1m** +3  — Good as-is.
- **opus-4-7-b** +3  — Names both the structure (cascade = ordered resolution) and the heritage (Boyd's *Orient* of OODA) without being captured by OODA. Only other live candidate I considered was "orientation sequence" — flatter, weaker, rejected.
- **opus-4-7-r2** +3 (keep) — Defended keep. Boyd's "Orient" is the right reference and the cascade structure is what the segment derives. The name cleanly extends the OODA reference to AAD's information-dependency-forced ordering.
- **opus-4-7** +3  — The five-phase cycle has an "expand" for actuated agents; "cascade" evokes the forced-by-information-dependency ordering. One of the theory's best names. Keep.
- **sonnet-4-6-r2** +3 (keep) — "Orient cascade" is one of the project's best names — it captures the sequential resolution structure of the expanded epistrophe phase. Evocative and accurate. Boyd's OODA "Orient" is the explicit inspiration.
- **sonnet-4-6-r2** +3 (canonicalize) — LEXICON.md and segment use "orient cascade." CLAUDE.md uses "Orient cascade" and "orient cascade" — lowercase is the correct form except when starting a sentence.
- **sonnet-4-6** +3  — Short, verb-derived, evocative. "Orient" from Boyd's OODA is the right referent — the segment even says so. The cascade structure is visible in the name. Do not change.
- **sonnet-4-6** +3  — See #orient-cascade keep vote. The word "orient" is earned by the Boyd connection. Keep.

---

## 4. `directed separation`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1, audit
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +45 | keep × 5, canonicalize × 1 |
| goal-blind processing pearl-blanket separation epistemic isolation of belief update | +1 | rename × 1 |

### Candidate: `directed separation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Has no broad ML usage; mostly baggage-free. Small risk of separation-principle echo from LQR/Kalman. Add one-sentence clarification in segment Discussion — no rename.
- **codex-1** +3  — Excellent theory name: concrete structural image, low baggage, easy to cite aloud.
- **codex-2** +3  — Short, memorable, and exactly the right amount of theoretical flavor.
- **codex-gpt-5-r2** +3 (keep) — One of the strongest English names in the corpus: technical, memorable, and low baggage.
- **gemini-1** +1  — Adopts useful baggage from causal inference (d-separation) nicely.
- **gemini-2** +3  — Good analog to d-separation; intuitive and load-bearing.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Core load-bearing name in AAD architecture. The separation of epistemic update from purpose is fundamental.
- **haiku-4-5-r2** +2 (keep) — Defended keep. The two-word "directed separation" is already a memorable noun phrase; changing either half would displace existing prose conventions without gain.
- **haiku-4-5** +3  — Specialist vocabulary ("directed" as Pearl's causal terminology; "separation" as conditional-independence terminology) correctly names a causal-graph property. Baggage-carrying in the best sense — travels with control-theory and causality intuitions. The Class 1/2/3 scope partition clarifies what it means architecturally. Keep.
- **opus-1m** +3  — Keep. The LQR-separation-principle echo is real but best handled by a one-sentence clarification in segment Discussion, not a rename.
- **opus-4-7-b** +3  — Zero pre-existing meaning in ML; the two words ("directed" = asymmetric information flow; "separation" = independence in the update) are both load-bearing. The only collision risk is control theory's *separation principle*, which is actually a Class-1 *consequence* of directed separation — the echo is informative, not misleading. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Directed separation" is one of the framework's distinctive named results and survives the communal-imagination test. The Pearl-blanket recognition is integrated through the name; renaming would lose that integration. Slug also reads correctly: it's a *derived* result (under the architectural scope condition), not a postulate.
- **opus-4-7** +3  — Survived the κ-as-scalar category-error rescue; the name now has its architectural Class 1/2/3 classification attached. Don't touch.
- **sonnet-4-6-r2** +3 (keep) — "Directed separation" is precise (the separation is directed — epistemic update is one-way independent of $G_t$) and distinctive. The architectural classification and Pearl-blanket connection make it load-bearing.
- **sonnet-4-6-r2** +3 (canonicalize) — Never "goal-blindness" or "epistemic separation" or "processing independence." The canonical name is "directed separation" as established in the segment and LEXICON.md.
- **sonnet-4-6** +3  — "Directed" specifies the asymmetry (goal-blind epistemic update; goal-dependent purposeful update); "separation" names the property. The architectural classification (Class 1/2/3) hangs off this name. Used throughout the project in prose; the name is load-bearing. Keep.

### Candidate: `goal-blind processing pearl-blanket separation epistemic isolation of belief update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative. [from 31-34-section-ii-opening-batch.md]

---

## 5. `identifiability floor`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +45 | keep × 4 |
| no-go theorems | -1 | — |

### Candidate: `identifiability floor` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — "Floor" is a load-bearing metaphor. Cannot go below it without outside help.
- **codex-1** +3  — Strong metaphor and well-matched to the segment's job: it names a hard lower boundary while still leaving room for explicit escape routes.
- **codex-2** +3  — Excellent negative-half companion to separability; "floor" is more useful than a generic "no-go."
- **codex-gpt-5-r2** +3 (keep) — Excellent meta-pattern name. Floor is concrete and scope-honest.
- **gemini-1** +3  — "Floor" is a great spatial metaphor for a structural no-go result.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Excellent cross-sectional concept name.
- **haiku-4-5** +3  — Exact metaphor for what it names — structural boundary that blocks general identification. Complements separability-pattern symmetrically. Keep.
- **opus-1m** +3  — "Floor" metaphor is load-bearing; no better candidate. Keep.
- **opus-4-7-b** +3  — "Floor" is the right geometric metaphor — the no-go is a *floor you can't go below without outside help*, and the machinery that escapes it is named relative to it. One of the best meta-segment names in the project.
- **opus-4-7-b** +3  — Explicit keep. Named best of the three meta-segments; the geometric metaphor ("floor you can't cross without information augmentation") is exactly load-bearing. Together with the above two proposed renames: **floor / ladder / forced-coordinates** reads as a trio of concrete mental pictures — one of AAD's highest-leverage naming opportunities if all three land together.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Floor" is the right metaphor — below this, no statistic can recover the inference; above it, AAD-supplied machinery escapes. Pairs with "ladders" if `#disc-separability-pattern` lands at separability-ladders. The pattern names the negative half cleanly.
- **opus-4-7** +3  — Three-word noun that invites both floor-instances and escape-routes; "floor" evokes the structural lower bound and Joseph has already used "escape the floor" as organic prose. Keep.
- **sonnet-4-6-r2** +3 (keep) — The strongest subject-noun in the three meta-segments. "Floor" is load-bearing — it names the asymmetry (you can climb above it; you cannot go below it without specific machinery). Mathematically precise and memorable.
- **sonnet-4-6** +3  — The Working Notes on this segment explicitly defend the "floor" framing over "no-go theorems" and the argument is correct — "floor" captures asymmetry (you cannot go below, but you can climb above). Memorable noun. Keep.
- **sonnet-4-6** +3  — See #identifiability-floor keep vote above. Already in prose use. Keep.

### Candidate: `no-go theorems`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Too generic and too negative. It loses the boundary-and-escape structure that makes the current name useful.

---

## 6. `information bottleneck`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +28 | keep × 5 |
| keep formal name AAD distinctive feature deserves separate label | +2 | keep × 1 |
| epistemic bottleneck | +1 | — |

### Candidate: `information bottleneck` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Correct baggage-carrying adoption. This is exactly the kind of prior-art name that should remain untouched.
- **codex-gpt-5-r2** +3 (keep) — Imported theorem name should remain canonical. It is already the recognized technical term.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Established literature term (Tishby).
- **haiku-4-5-r2** +1 (keep) — Adopted technical term (Tishby); keeping original name respects prior art. No local pressure to change.
- **haiku-4-5** +3  — Adopted from Tishby 1999; canonical name in information theory. Baggage-carrying in the best sense — travels with information-theoretic intuitions. Do not rename. Exact application matches Tishby's definition. Keep.
- **opus-1m** +3  — Adopted (Tishby 1999); keep.
- **opus-4-7-b** +3  — Adopted from Tishby et al. — do not rename adopted concepts (prior-art-integration convention). The word *bottleneck* is doing real explanatory work; the baggage transfers.
- **opus-4-7-b** +3  — Keep — adopted directly from Tishby et al. per prior-art-integration convention. Do not rename adopted concepts.
- **opus-4-7-r2** +3 (keep) — Defended keep — direct adoption from Tishby with proper attribution; renaming would lose provenance.
- **sonnet-4-6-r2** +3 (keep) — External vocabulary adopted directly (Tishby, Pereira & Bialek). Per prior-art-integration principle, adopt with original name.

### Candidate: `keep formal name AAD distinctive feature deserves separate label`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — Well-anchored in literature; AAD shouldn't rename. The AAD-distinctive *policy-conditioning* on the predictive term could be named separately: "Policy-Conditioned IB" / "Forward-Predictive IB" / "AAD-IB" — only if a distinguishing label is needed. Currently leans on standard name; auditor judges that the right call. [from 11-form-information-bottleneck.md]

### Candidate: `epistemic bottleneck`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Emphasizes the knowledge-compression aspect over raw Shannon information.

---

## 7. `chronica`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet, audit
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +27 | keep × 4, canonicalize × 1 |

### Candidate: `chronica` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +3 (keep) — "Chronica" is etymologically clean, the avoid-collision-with-$\mathcal{H}$ argument is solid, and the segment carries explicit non-forkability content that the term licenses. Auditor considers it well-chosen and load-bearing. [from 04-def-chronica.md]
- **codex-1** +3  — Distinctive, speakable, and better than another overloaded "history" or "trace." Strong keep.
- **codex-2** +3  — This is exactly the kind of memorable noun a theory wants: compact, distinctive, and reusable in speech.
- **codex-gpt-5-r2** +3 (keep) — Strong core term: singular causal record, memorable, Greek-register aligned, and not easily confused with generic memory.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Load-bearing Greek vocabulary.
- **opus-4-7** +3  — Singular Greek-root noun with clean Obsidian/prose pickup; also resolves the $\mathcal H$/entropy collision. Joseph deliberately avoided "history" — don't unwind.
- **sonnet-4-6-r2** +3 (keep) — "Chronica" is the strongest name in the project — Greek-rooted, distinctive, avoids collision with entropy notation, survives every naming criterion. Do not rename.
- **sonnet-4-6-r2** +3 (canonicalize) — Never "history," "interaction history," or "$\mathcal{H}_t$" in prose (the chronica notation is $\mathcal{C}_t$ precisely to avoid collision with entropy). The canonical term is "chronica."
- **sonnet-4-6** +3  — Excellent coinage. Greek term for "records of time" with zero collision with other vocabulary (avoids $\mathcal H$ for entropy). Memorable, singular, has been thoroughly adopted across the codebase. The strongest single naming decision in the project. Keep without question.

---

## 8. `persistence condition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +27 | keep × 5, canonicalize × 1 |
| survival equation | +1 | add-alias × 1 |

### Candidate: `persistence condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — This is an established theorem-facing phrase. It is generic, but it names the primary threshold cleanly.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Central inequality of the framework, decomposing into structural persistence and task adequacy.
- **haiku-4-5-r2** +3 (keep) — Canonical across domains (Lyapunov, RL, organizational viability, software maintenance). Load-bearing name; rename would displace vast prose footprint.
- **haiku-4-5** +3  — Core definition. Unambiguous. Keep.
- **opus-4-7-b** +3  — Keep. The slug for AAD's *central inequality*; any change would ripple through every citing segment.
- **opus-4-7-r2** +3 (keep) — Defended keep — the framework's central inequality. The segment carries the canonical bathtub gloss in its Findings section; renaming would break the iconic naming.
- **opus-4-7** +3  — The central inequality; eponymous. Keep.
- **sonnet-4-6-r2** +3 (keep) — "Persistence condition" is the central named result of the theory. The name is canonical, memorable, and appears throughout the codebase. Do not change.
- **sonnet-4-6-r2** +3 (canonicalize) — Sometimes appears as "the persistence criterion," "the adaptive persistence condition," or "the alpha > rho/R condition." One name: "persistence condition."

### Candidate: `survival equation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (add-alias) — Useful elevator-pitch phrase, but too slogan-like for canonical theorem prose.

---

## 9. `strategy DAG`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +26 | keep × 5, canonicalize × 1 |
| keep | +2 | keep × 1 |

### Candidate: `strategy DAG` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Blunt and effective. The slug is legible instantly, and the concept it names is load-bearing.
- **codex-2** +3  — Exactly the right level of compression: simple, searchable, and faithful to the object.
- **codex-gpt-5-r2** +2 (keep) — Direct and technically honest. Keep rather than hiding the graph structure behind a metaphor.
- **codex-gpt-5-r2** +2 (keep) — The acronym is technical but exact. No need to prettify it.
- **haiku-4-5-r2** +2 (keep) — "Strategy DAG" is memorable and passes the communal-imagination test. The acronym DAG is standard. No change needed.
- **haiku-4-5** +3  — Self-descriptive (probabilistic directed acyclic graph for strategy), compact notation. Consistent lowercase convention with #agent-spectrum, #value-object, etc. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. The DAG-with-AND/OR-and-single-parameter-edges representation is iconic in the framework and is referenced by slug in many downstream segments; renaming would create cascading editorial work for negligible reading-clarity gain. The segment also makes the case that the DAG structure is *derived* (acyclicity from temporal ordering, Markov from CMC), so "strategy DAG" reads as a result-name as well as a definition-name.
- **opus-4-7-r2** +2 (canonicalize) — In prose this is sometimes "the strategy graph" or "the strategy structure" or "the agent's strategic causal model." Canonicalize on "strategy DAG" for the AND/OR-DAG-with-edge-credences object, and reserve "strategy" alone for $\Sigma_t$ as a state object distinct from its representation.
- **opus-4-7** +3  — Established; the segment does a lot of work (acyclicity derived, Markov derived, correlation hierarchy). Keep.
- **sonnet-4-6-r2** +3 (keep) — "Strategy DAG" is precise, memorable, and already has convention weight. The DAG structure is the key novelty; the name accurately foregrounds it.

### Candidate: `keep`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — Substantive load-bearing segment. Auditor's only flag was that the segment is *large* and might benefit from being split; the *name* is correct. [from 43-46-section-ii-and-or-strategy-dag-gaps.md]

---

## 10. `chain confidence decay`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +25 | keep × 5 |
| keep load bearing | +2 | keep × 1 |
| log confidence additive | +1 | rename × 1 |

### Candidate: `chain confidence decay` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Clear phenomenon name rather than proof name; easy to paraphrase aloud.
- **codex-gpt-5-r2** +3 (keep) — Strong exact-result name and good anchor for the log-additivity family.
- **gemini-1** +1  — Clear and descriptive of the phenomenon.
- **gemini-2** +3  — Highly descriptive of the log-confidence additive depth effect.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Evocative of the AND-chain probability multiplication.
- **haiku-4-5-r2** +1 (keep) — Mathematical precision; "chain confidence decay" names the pattern exactly.
- **haiku-4-5** +3  — Self-descriptive — log-confidence additive in depth along a causal chain. Solid name; reads naturally. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Chain confidence decay" reads as a phenomenon and is referenced by name in many downstream segments. The keep is defensible against the proposed rename.
- **opus-4-7** +3  — Inevitability-core segment; name matches the log-decomposition content. Keep.
- **sonnet-4-6-r2** +3 (keep) — "Chain confidence decay" is precise, memorable, and names the exact phenomenon: chain depth causes monotonic decay in aggregate confidence.
- **sonnet-4-6** +3  — Crisp compound noun. The name is self-explaining: confidence decays along a chain. It also works as the anchor of the additive-coordinate-forcing pattern — "chain-level additive log-confidence decay" is how other segments refer to it. Keep.

### Candidate: `keep load bearing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — Auditor flagged this as the structural anchor for the additive-coordinate-forcing meta-pattern (chain-rule identity → three downstream uniqueness theorems). Name does its job. [from 39-42-section-ii-ciy-strategy-chain.md]

### Candidate: `log confidence additive`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Considered. "Chain confidence decay" emphasizes the *decay* (downstream effect); "log-confidence additive" emphasizes the *uniqueness move* (additivity in log-space, the chain-layer instance of additive-coordinate-forcing). Mild preference for the latter because the additive identity is what the segment proves; decay is the consequence. Slug-as-thing-defined principle.

---

## 11. `symbiogenic composition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +24 | keep × 5 |
| symbiogenic absorption | +3 | — |
| asymmetric absorption | +1 | — |

### Candidate: `symbiogenic composition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — High-aesthetic-risk name, but it earns that risk by being vivid and structurally specific.
- **codex-gpt-5-r2** +3 (keep) — Strong, etymologically apt, and scope-honest for asymmetric composite formation.
- **codex-gpt-5-r2** +3 (keep) — Distinctive and exactly aimed at asymmetric composite formation.
- **gemini-1** +1  — Beautiful biological metaphor for asymmetric absorption.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good Greek alignment, descriptive.
- **haiku-4-5** +3  — "Symbiogenic" (host integrates endosymbiont) borrowed from biology and evolution. Evocative, specialized vocabulary. Reads naturally in context of asymmetric absorption mechanisms. Keep.
- **opus-4-7-b** +3  — Keep. "Symbiogenic" is the exactly-right biological term for "one agent integrating another that formerly had its own autonomy"; the $U_O$-crosses-threshold-from-below mechanism matches the biological meaning with precision. Rare case where an adopted term upgrades the reader's intuition about the formalism.
- **opus-4-7-r2** +3 (keep) — Defended keep. The endosymbiont-host integration mechanism is a substantial composition mechanism, and "symbiogenic" is the right biological-vocabulary import.
- **opus-4-7** +1  — Etymologically accurate (Margulis lineage; asymmetric absorption). Keep unless cleaner alternative emerges.
- **sonnet-4-6-r2** +3 (keep) — "Symbiogenic" is the established biological term (Margulis) adopted directly. The asymmetric absorption mechanism is EXACTLY what the word means. Strong keep per prior-art-integration principle.
- **sonnet-4-6** +1  — "Symbiogenic" is technically correct (host absorbs endosymbiont) but requires specialist vocabulary. Appropriate if the target audience includes evolutionary biology. Mild risk of requiring explanation on each encounter outside that community.

### Candidate: `symbiogenic absorption`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "Absorption" is the specific asymmetric mechanism described (host integrates endosymbiont).

### Candidate: `asymmetric absorption`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Plainer English for the same concept. Less evocative but lower bar for new readers.

---

## 12. `additive coordinate forcing`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| forced coordinates | +23 | rename × 6 |
| coordinate forcing | +12 | rename × 4 |
| uniqueness coordinate forcing | +5 | — |
| uniqueness coordinates | +1 | — |
| _(keep)_ | +1 | — |
| logarithmic lift | -1 | — |
| anchor lattice | -1 | — |
| log coordinate forcing | -1 | — |
| additive lift | -2 | — |
| axiom forcing | -2 | — |
| cauchy coordinates | -4 | rename × 2 |

### Candidate: `forced coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The current name is accurate but over-explains the mechanism. "Forced coordinates" is shorter, more noun-like, and broad enough to cover the metric-layer case too.
- **codex-2** -1  — Too breezy and it drops the uniqueness-theorem discipline that makes the segment interesting.
- **codex-gpt-5-r2** +3 (rename) — The family claim is that additive or invariant structure forces a coordinate choice. Forced coordinates is compact and general.
- **gemini-1** +1  — "Forced coordinates" is broader and more scope-honest for the various layers involved.
- **gemini-3-1-pro-preview-r2** +3 (rename) — Scope-honesty for meta-segment. Covers Cauchy-FE and Čencov machineries forcing coordinates onto Legendre-Fenchel geometry.
- **gemini-3-1-pro-preview-r2** +3 (rename) — Concurring with Codex/Haiku/Sonnet: drops the overly-restrictive "additive" and names the true meta-pattern.
- **haiku-4-5-r2** +3 (rename) — Round-1 consensus; "forced" is more evocative and covers Čencov's 4th instance (not exclusively Cauchy-FE). Passes the communal-imagination test better.
- **opus-1m** +3  — The segment carries four primary instances: three via Cauchy functional equation (chain / divergence / update) and one via Čencov-invariance (metric). The segment itself states (line 50): "Both clear the broader discipline — uniqueness-theorem-forced coordinate under AAD-internal axiom — but via distinct uniqueness-theorem machineries." Naming the meta-pattern after only one machinery (Cauchy) violates the scope-honesty the segment just established. "Forced coordinates" covers both machineries. Preserves "additive-coordinate-forcing" as long-form in the segment subtitle.
- **opus-4-7-b** +3  — The current name has two problems: (i) it's *additive-only*, which was honest when the meta-segment covered three Cauchy-FE instances, but is now factually under-inclusive since the Čencov / Fisher-metric 4th primary instance is not log-additive — the segment itself acknowledges this and floats `#uniqueness-coordinate-forcing` as a possible rename; (ii) five-syllable hyphen-compound is not a name anyone reaches for in conversation. "Forced coordinates" is the concept in two short words: the coordinate is *forced* by a uniqueness theorem operating on an AAD-internally-motivated axiom. Covers both Cauchy-FE and Čencov mechanisms. Preserves the pattern's content (1 anchor + 3 theorems, with Lyapunov / IB as adjacent).
- **opus-4-7-r2** +1 (rename) — Acceptable alternative to coordinate-forcing; "forced-coordinates" is the result, "coordinate-forcing" names the move. I have a mild preference for the move-form because it parallels "directed separation" and "satisfaction gap" — verb-flavored compound nouns.
- **opus-4-7** +1  — The Čencov fourth primary instance forces the Fisher metric, which is not log-additive — the current name advertises three-out-of-four. "Forced coordinates" covers both Cauchy-FE and Čencov machineries without overpromising additivity. The segment itself flags this in the Discussion. Candidate.
- **sonnet-4-6-r2** +1 (rename) — Alternative — noun form rather than gerund form. Slightly more thing-like. Weaker preference than `disc-coordinate-forcing`.
- **sonnet-4-6** -1  — Passive noun; loses the process-verb structure that "forcing" has. A reader encountering it first might not know what forces them.

### Candidate: `coordinate forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Acceptable fallback, but it is less noun-like and less memorable than forced coordinates.
- **opus-1m** +1  — Acceptable alternative to #forced-coordinates; names the activity in verb form. Slightly less concrete than "forced coordinates" as a noun.
- **opus-4-7-b** +1  — Verb-form alternative; acceptable fallback if `#forced-coordinates` doesn't land. Same argument, slightly more clinical.
- **opus-4-7-r2** +2 (rename) — "Additive" undersells one of the four layers (the metric layer's Čencov-invariance is not literally additivity in a Cauchy-FE sense — it's invariance under reparameterization that picks out the Hessian of the dual potential). The segment itself names "additive or invariant coordinate" in the body. Dropping "additive" makes the meta-pattern name as broad as the four layers it actually covers. Slug layer.
- **opus-4-7-r2** +1 (rename) — Confirmation with new reasoning — three peers (Codex, Haiku, Gemini, Sonnet) all reached "forced-coordinates" while my own first vote was "coordinate-forcing." Seeing the cross-architecture pull toward "forced-coordinates" makes me less confident in the move-form preference; the result-form ("forced-coordinates") may be more memorable in conversation precisely because the move ("forcing") is mechanical and the *result* (coordinates appearing forced) is the surprising thing. Keeping my +2 vote for "coordinate-forcing" but adding this confirmatory +1 for the consensus form.
- **opus-4-7** +1  — Verb-form variant; fine if #forced-coordinates doesn't land.
- **sonnet-4-6-r2** +2 (rename) — "Additive" in the slug is redundant once the segment explains that the forcing is via additivity axioms. The slug reads as describing an additive operation, but what's actually being named is the phenomenon of coordinates being forced by uniqueness theorems. "Forced coordinates" or "coordinate-forcing" without "additive" is cleaner and still accurate — the Discussion section carries the "additive" nuance.
- **sonnet-4-6** +3  — The segment itself acknowledges that the Čencov 4th instance is not Cauchy-FE-additive; the title's "additive" is already acknowledged to be slightly wrong in the Discussion. "Coordinate forcing" names the broader discipline accurately, keeps the verb form, and doesn't overclaim the mechanism.

### Candidate: `uniqueness coordinate forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — More abstract than the current name and less memorable than "forced coordinates." It sounds like a category label, not a concept people will use.
- **codex-2** +3  — The current name undersells the Čencov/Fisher instance; the broader discipline is uniqueness, not additivity alone.
- **haiku-4-5** +1  — Weaker alternative emphasizing the broader discipline (uniqueness theorem + AAD-internal axiom) over sub-structure (log-additivity). Better accuracy for when the 4th instance dominates reader mindshare, but "additive" three-of-four justifies keeping current name.
- **opus-4-7** +1  — Alternative that matches the "broader discipline" phrasing the segment itself uses. Less snappy than #forced-coordinates; more precise.
- **sonnet-4-6** +1  — Alternative rename capturing the shared mechanism (uniqueness theorem on AAD-internal axiom). More precise than "coordinate forcing" alone, but less smooth to say.

### Candidate: `uniqueness coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Closer to the mechanism ("uniqueness theorem forces coordinate"); loses a little crispness compared to `#forced-coordinates`. Second-choice.

### Candidate: `additive coordinate forcing` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Hedged keep. The "additive" emphasis correctly highlights three of four instances (Cauchy-FE log-additive). The Čencov fourth instance diverges on sub-structure (Riemannian metric rather than log coordinate) but shares broader discipline. Current name acceptably descriptive; slight rename might clarify uniqueness-theorem focus. (See weak alternative below.)

### Candidate: `logarithmic lift`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Verbose.

### Candidate: `anchor lattice`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Too structural-sounding for the "1-anchor-plus-3-theorem" framing.

### Candidate: `log coordinate forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — More direct but verbose.

### Candidate: `additive lift`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Considered but weaker. "Lift" too common in math to stick.
- **opus-1m** -1  — "Lift" is overloaded in math (bundle lifts, category-theoretic lifts) and doesn't suggest uniqueness-theorem forcing.

### Candidate: `axiom forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Less self-descriptive than #cauchy-coordinates.
- **opus-1m** -1  — Underdescriptive — doesn't convey that the *thing forced* is a coordinate.

### Candidate: `cauchy coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Weak preference. Names the mechanism and the output; short and crisp. Downside: "Cauchy" overloaded in math. Retain additive-coordinate-forcing as long-form subtitle.
- **codex-gpt-5-r2** -1 (rename) — Too narrow and misleading because the family includes Fisher, Cencov, IB, and Legendre geometry, not only Cauchy functional equations.
- **opus-1m** -1  — Explicit rejection. The Čencov metric-layer 4th primary instance is NOT Cauchy-FE; naming the meta-pattern for one of two machineries violates the scope-honesty commitment the segment establishes in its own Discussion section. Short and crisp, but scope-dishonest.
- **opus-4-7-b** -1  — Short, crisp, memorable — but actively misleading now that the Čencov instance is part of the primary four. "Cauchy" undersells the metric-layer instance and risks calcifying the meta-segment in a form it has already grown past. Reject.
- **opus-4-7-r2** -1 (rename) — Considered and rejected — undersells the Čencov 4th instance (not Cauchy-FE) and overspecifies on the chain/divergence/update layers' machinery.
- **opus-4-7** -1  — Undersells the Čencov instance; would require a second meta-segment to cover the fourth primary instance. Reject.

---

## 13. `sector persistence template`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +23 | keep × 3 |
| bounded correction template | +5 | add-alias × 1 |
| persistence template | +0 | — |

### Candidate: `sector persistence template` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Technical-clinical but clear; meta-segment role legible from name. Keep (though see family-naming question in Quiet Successes).
- **codex-2** +1  — Long, but structurally honest; shortening it would likely erase which persistence machinery is in play.
- **codex-gpt-5-r2** +3 (keep) — The template role is real and cross-cutting. Keep as the reusable theorem pattern.
- **haiku-4-5** +3  — Abstract sector-persistence template; six AAD results as instances. "Template" emphasizes the reusable machinery. "Sector persistence" grounds it in the control-theoretic Lyapunov framework. Good name. Keep.
- **opus-1m** +3  — Technical but clear; role as shared-lemma is legible. Keep.
- **opus-4-7-b** +1  — Keep. "Template" is the correct AAD term (a parameter-free shared-lemma pattern that multiple results instantiate). Clinical but apt.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Template" is doing precise work — the segment is invoked across six segments as a template, with each invocation specifying its own state variable and disturbance rate. The name matches the abstraction-pattern role.
- **opus-4-7** +3  — Names the mechanical content (Lyapunov on sector-bounded correction) and is already cited by six instantiations. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Sector persistence template" names the abstract Lyapunov argument that multiple results instantiate. The "template" framing is accurate and useful.
- **sonnet-4-6** +1  — Alternative keep: "sector" distinguishes it from e.g. contraction-based persistence, which matters once #contraction-template exists. Both are live.

### Candidate: `bounded correction template`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Better public-facing name for what the result actually unifies. "Sector" names the proof device; "bounded correction" names the concept.
- **codex-gpt-5-r2** +2 (add-alias) — Strong public-facing gloss, but sector should remain in the formal name because the proof device distinguishes this template from contraction.

### Candidate: `persistence template`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Too broad. It would erase the special bounded-correction structure that distinguishes this template from every other persistence discussion in the repo.
- **sonnet-4-6** +1  — "Sector" names the mathematical structure; the template's job is persistence. "Persistence template" is shorter and what users will say in conversation. Weak preference — "sector-persistence" is honest about the mechanism.

---

## 14. `temporal optimality`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +23 | keep × 3 |

### Candidate: `temporal optimality` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong, disciplined, and reusable. It sounds like a theorem target rather than a slogan.
- **codex-2** +3  — Excellent theorem-style name: short, forceful, and memorable.
- **codex-gpt-5-r2** +2 (keep) — Good TST postulate name. It says what the optimization is about.
- **gemini-1** +3  — "Temporal optimality" is clear, accurate, and sets the normative grounding perfectly.
- **opus-4-7-b** +3  — Keep. TST's central claim ("time-optimal development is the right objective"); slug is canonical.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Temporal optimality" names the postulate exactly — among equivalent outcomes, least-time is preferred. The phrase is the foundational normative principle of TST and is correctly placed there (with AAD providing the descriptive grounding via persistence). Renaming would weaken a well-established prior commitment.
- **sonnet-4-6-r2** +3 (keep) — "Temporal optimality" is TST's foundational normative principle. The name is exact and memorable.
- **sonnet-4-6** +3  — The foundational TST postulate. "Temporal optimality" names the principle (least time is optimal given equivalent outcomes). Keep.

---

## 15. `adversarial destabilization`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +22 | keep × 5 |

### Candidate: `adversarial destabilization` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Exact, vivid, and result-shaped. This is a good permanent name.
- **codex-gpt-5-r2** +3 (keep) — Strong name for the threshold failure result.
- **codex-gpt-5-r2** +3 (keep) — Strong result name.
- **gemini-2** +3  — Excellent, evocative name for getting inside an opponent's loop.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Descriptive.
- **haiku-4-5** +3  — Inside opponent's loop; includes effects spiral. "Destabilization" is precise; reads naturally in adversarial context. Keep.
- **opus-4-7-b** +1  — Keep. Direct, punchy; the word "destabilization" signals the direction (outward from the bounded region) rather than something neutral like "dynamics."
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Pairs with #der-team-persistence as the cooperative/adversarial complement. The "effects spiral" sub-result inside is well-handled by Discussion mention.
- **sonnet-4-6-r2** +2 (keep) — Precise. The mechanism IS adversarial destabilization.

---

## 16. `agent spectrum`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +22 | keep × 6, canonicalize × 1 |
| agency spectrum | +1 | — |
| agent quadrants | -1 | rename × 1 |

### Candidate: `agent spectrum` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Useful, legible, and already doing real explanatory work in Section II setup.
- **codex-gpt-5-r2** +3 (keep) — Strong umbrella for the model-richness by objective-richness continuum.
- **gemini-3-1-pro-preview-r2** +2 (keep) — The text explicitly defines regions of a continuum (spectra) for model and objective richness. The name fits.
- **haiku-4-5-r2** +1 (keep) — The "spectrum" metaphor (from basic to actuated) is apt and aids visualization. Good name.
- **haiku-4-5** +3  — ±model × ±objective quadrants. "Spectrum" emphasizes the continuum from fully-adaptive to fully-agentic. Reads naturally. Keep.
- **opus-4-7-b** +1  — Keep. "±model × ±objective quadrants" — "spectrum" is an acceptable word for a 2×2 partition if one is feeling generous. Alternative: `#agent-types-partition`, but that's worse.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. The 2×2 model-richness × objective-richness table earns "spectrum" — the regions are continuous, not categorical, and the segment's discussion makes that explicit. I considered "agent-quadrants" but quadrants would imply four discrete categories, which the segment explicitly says they are not.
- **opus-4-7-r2** +2 (canonicalize) — The 2×2 model-richness × objective-richness picture is consistently "agent spectrum" in the segment, but downstream sometimes "agent quadrant," "agent typology," "agent classification." Canonicalize on "agent spectrum"; the four corners are *regions*, not types or classes.
- **opus-4-7** +1  — Names the ±model × ±objective 2×2 table; the segment's content is exactly that. Fine.
- **sonnet-4-6-r2** +3 (keep) — "Spectrum" is accurate (two axes creating a continuum) and evocative. The term "agent spectrum" survives conversation naturally.
- **sonnet-4-6-r2** +3 (keep) — (Duplicate of above, confirming.)

### Candidate: `agency spectrum`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — The segment maps richness of agency, not a zoology of agent types.

### Candidate: `agent quadrants`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — see above; quadrants oversells discreteness.

---

## 17. `adaptive reserve $\Delta\rho^\ast$`

**Voted by architectures:** Gemini, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive reserve | +21 | — |

### Candidate: `adaptive reserve`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Two words, one intuition, immediately suggests shock-absorber depth.
- **gemini-1** +3  — Clear, evocative engineering vocabulary. Does not need changing.
- **gemini-2** +3  — Very evocative physical intuition, like thermal or mechanical reserve. Do not touch.
- **opus-1m** +3  — Good as-is.
- **opus-4-7-b** +3  — Mechanical-engineering intuition ("shock reserve" / "crumple zone") fits exactly what the quantity measures. The two-word compound lands on the first read.
- **opus-4-7** +3  — Rare English term that reads as *shock tolerance* in prose and ties cleanly to the $\alpha R - \rho$ formula. One of the project's cleanest symbol-to-English pairs. Keep.
- **sonnet-4-6** +3  — Perfect term. "Reserve" is the right word — it is the shock tolerance the agent has banked against future disturbances. Keep.

---

## 18. `shared intent`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +21 | keep × 4 |
| compressed purpose | +1 | — |
| teleological unity | +1 | rename × 3 |
| keep def shared intent | +1 | rebuttal × 1 |

### Candidate: `shared intent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Compact, portable, and directly connected to the commander's-intent analogy. This already sounds like a concept, not a paper section.
- **codex-2** +3  — Strong communal noun with clear organizational resonance.
- **codex-gpt-5-r2** +3 (keep) — Clear and domain-familiar. It also maps well to mission command without overusing German terminology.
- **codex-gpt-5-r2** +3 (keep) — Excellent bridge between IB compression and mission command.
- **haiku-4-5** +3  — IB-compressed purpose. "Shared intent" reads naturally — what agents align on. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. Maps directly to Clausewitz's "commander's intent" tradition (acknowledged in the segment); renaming would break the prior-art bridge.
- **sonnet-4-6-r2** +3 (keep) — Load-bearing prose vocabulary established across the codebase. "Shared intent" is what commanders communicate in Auftragstaktik and the IB compression finds — the name is exactly right.

### Candidate: `compressed purpose`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Highlights the Information Bottleneck aspect of shared intent.

### Candidate: `teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Shared intent is an IB-compressed communication object. Teleological unity is already a unity dimension; merging them would erase a useful distinction.
- **gemini-3-1-pro-preview-r2** +3 (rename) — Aligns perfectly with the $U_O$ notation and unifies with epistemic/strategic unity.
- **opus-4-7-r2** -1 (rename) — Rebuttal — Gemini proposed this rename at +3 with the rationale that it aligns with U_O notation and unifies with epistemic/strategic unity. I think this is wrong. "Shared intent" is the *operational* cross-agent communication concept (what gets transmitted, the IB-compressed payload of $G_t$); "teleological unity" is the *measured* alignment property ($U_O = I/H$). The two are NOT the same: a multi-agent system can have low teleological unity but still transmit shared intent (poorly). Renaming would collapse the distinction the framework currently makes. Sonnet's defended-keep at +3 is correct and Gemini's rename undermines a load-bearing distinction.

### Candidate: `keep def shared intent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — Against Gemini's proposal `#def-teleological-unity` (+3). Gemini argues this "aligns perfectly with $U_O$ notation and unifies with epistemic/strategic unity." This is precisely the problem: `def-shared-intent` is the multi-agent concept (what is communicated between agents, the Clausewitz commander's intent, the IB compression of $G_{\text{shared}}$), while $U_O$ is the single-agent teleological unity. Renaming to `teleological-unity` would collapse a load-bearing distinction the framework relies on (shared intent is an inter-agent concept; teleological unity is intra-agent). Gemini's vote would create exactly the kind of conceptual blur the framework is designed to avoid. The "unification with $U_O$" is a feature of the current names doing different things, not a defect.

---

## 19. `AAD adaptation and actuation dynamics`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +20 | — |
| AAD | +3 | — |
| AAD agentic adaptation dynamics | +1 | — |

### Candidate: `AAD adaptation and actuation dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Recent rename (2026-04-16); further thrash dilutes identity. "Actuation" imperfection is real but a Section II preamble clarification handles it more cheaply than another rename.
- **codex-1** +1  — "Actuation" is imperfect, but framework-level churn is more expensive than the remaining mismatch; clarify in prose rather than rename again.
- **codex-2** +3  — The rename cost has already been paid; the short form is now compact, distinctive, and good enough to keep.
- **gemini-1** +1  — Recent rename; "Actuation" is slightly imperfect for Section II but further churn dilutes identity. Keep.
- **haiku-4-5** +3  — Recent rename (2026-04-16) from Agentic Cycle Theory. Further churn is expensive; identity is now locked in. The "Actuation" imperfection is real but manageable via a Section II preamble. Do not rename the framework. Keep.
- **opus-4-7-b** +3  — Do not rename. The rename from ACT happened on 2026-04-16 (six months ago at this date); further churn dilutes the identity when the framework is starting to be cited. Any fresh alternative would face the same collision-checking burden that ACT did. **However:** the "Actuation" half is a genuinely weaker fit than "Adaptation" for what Section II covers (Section II is purposeful agency with objectives and strategy; "actuation" in engineering means *mechanical output*). The fix is not a rename but a Section II preamble paragraph that explicitly names "actuation" in AAD's specific sense ("actuated toward an objective" — already in LEXICON Agent-Classes, but needs to be surfaced at Section II preamble level).
- **opus-4-7** +3  — Recent (2026-04-16) rename to resolve the "AI Consciousness Test" collision; further churn dilutes identity. The "Actuation"-vs-Section-II imperfection is a preamble clarification not a rename.
- **sonnet-4-6** +3  — Recent rename (2026-04-16) from ACT; citation velocity is building under the new name. The "Actuation" imperfection noted in the naming-principles file is real (Section II is more about purposeful actuation than mechanical actuation) but the Section II preamble handles it. Further churn would cost more than it gains. Keep.

### Candidate: `AAD`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Recent rename (2026-04-16); further churn dilutes identity. Naming collisions have already narrowed options. The "Actuation" asymmetry is real but handled more cheaply by a Section II preamble clarification.

### Candidate: `AAD agentic adaptation dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Actuation" has a strong mechanical engineering flavor that clashes slightly with the teleological/purposeful focus of Section II. "Agentic Adaptation Dynamics" retains the acronym while emphasizing agency.

---

## 20. `adaptive tempo`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +20 | keep × 4, canonicalize × 1 |
| adaptation rate | -1 | — |

### Candidate: `adaptive tempo` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Clear, compact, central, and reusable across individual, team, adversarial, and software domains.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Highly memorable, core concept.
- **haiku-4-5-r2** +2 (keep) — The Greek *tempo* is elegant; "adaptive" correctly narrows. The symbol 𝒯 (calligraphic) is load-bearing in notation. Defend.
- **haiku-4-5** +3  — Rate of useful info acquisition. Self-descriptive, evocative. Keep.
- **opus-4-7-b** +3  — Keep. "Tempo" is one of AAD's best one-word handles; the slug is short.
- **sonnet-4-6-r2** +3 (keep) — "Adaptive tempo" is AAD's core capacity metric name. It's precise, memorable, and established in prose and NOTATION.md.
- **sonnet-4-6-r2** +3 (canonicalize) — Sometimes appears as "learning rate" (wrong — that's $\eta^\ast$), "correction rate," or "tempo" alone. The canonical name is "adaptive tempo" ($\mathcal{T}$).

### Candidate: `adaptation rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** -1  — Loses the "rate × quality" compound the tempo metaphor delivers. Reject.

---

## 21. `agent opacity`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +20 | keep × 4 |
| emitter opacity | +1 | — |
| strategic opacity | +0 | rename × 1 |

### Candidate: `agent opacity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Clean, sayable, and immediately useful in both cooperative and adversarial discussion.
- **codex-gpt-5-r2** +3 (keep) — Excellent name for observer-side backward predictive uncertainty.
- **codex-gpt-5-r2** +3 (keep) — Strong subject noun and good dual to observation quality.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good descriptive name.
- **haiku-4-5** +3  — Adopts Hafez terminology; H_b^{A|B} (backward predictive uncertainty) is dual to observation quality. "Opacity" reads naturally — adversaries want opacity; cooperators want transparency. Name works. Keep.
- **opus-4-7** +1  — Fine; "opacity" is the right scalar polarity (emitter side) and has Hafez-lineage citation weight. But see next row.
- **sonnet-4-6-r2** +2 (keep) — "Agent opacity" is the established term from Hafez et al. 2026, adopted directly. Using the same name as the source is the right move per the prior-art-integration principle.
- **sonnet-4-6** +3  — "Opacity" is exactly the right word — backward predictive uncertainty from the observer's perspective. Pairs naturally with "transparency" as the opposite. Keep.

### Candidate: `emitter opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Disambiguates emitter-side from recipient-side in the 16-cell composition. Parallel with #recipient-regime-classification above.

### Candidate: `strategic opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Too narrow. Opacity matters in cooperative legibility and adversarial concealment; strategic opacity would collapse the dual-use role.
- **gemini-2** +1  — "Agent opacity" is broad. "Strategic opacity" specifically points to the adversarial mechanism of hiding intent.

---

## 22. `causal information yield`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +20 | keep × 5, canonicalize × 1 |
| CIY | +2 | add-alias × 1 |

### Candidate: `causal information yield` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Long, but exact and reusable. The acronym earns its keep because the concept recurs across exploration, querying, and trust.
- **codex-2** +1  — Slightly technical, but the phrase is honest and reusable; the `CIY` acronym is tolerable once introduced.
- **codex-gpt-5-r2** +2 (keep) — Descriptive and central. CIY is useful as abbreviation, but the expanded name should remain canonical.
- **codex-gpt-5-r2** +2 (keep) — Clear and central.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Important core concept (CIY).
- **haiku-4-5-r2** +2 (canonicalize) — Appears as "CIY" (acronym) and as "Causal Information Yield" (full form) throughout OUTLINE.md and NOTATION.md. Commit to the full form in prose; acronym as shorthand only. Currently mixed.
- **haiku-4-5** +3  — Self-descriptive compound; reads as "the yield [information gain] from a causal action." Names what it measures. Keep. (CIY abbreviation appears in NOTATION and segments; prose can use full phrase.)
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "CIY" is well-defined and the alias usage is consistent.
- **sonnet-4-6-r2** +2 (keep) — CIY is established vocabulary. "Yield" correctly names the information gained from interventions.

### Candidate: `CIY`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Symbol-to-name alias: $\text{CIY}(a)$ in math; "causal information yield" or "CIY" in prose. The acronym survives the communal-imagination test (acronym discipline check passes — used 10+ times in nearby prose, no obvious AI/ML collisions). Solidify the symbol+acronym pair as a maintained convention.

---

## 23. `concept the parameter space region within which an agent maintains bounded mismatch indefinitely`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence envelope | +20 | name-unnamed × 4 |
| parametric regime or stability envelope | +1 | name-unnamed × 1 |
| adaptive basin | -1 | — |

### Candidate: `persistence envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Engineering vocabulary, geometrically evocative. "Well inside its persistence envelope" reads more crisply than "satisfies persistence condition with non-marginal adaptive reserve." [original phrasing: unnamed: the sector-persistence region in parameter space]
- **codex-gpt-5-r2** +3 (name-unnamed) — Strongest new shared proposal from the other votes. Flight-envelope connotations fit the safe operating region exactly. [original phrasing: bounded mismatch region]
- **gemini-1** +3  — "Envelope" is standard flight-dynamics vocabulary for a safe operating region. Highly memorable. [original phrasing: unnamed: the region where the persistence condition holds]
- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Evocative, captures the safe operational region geometrically. [original phrasing: unnamed: the sector-persistence region in parameter space]
- **haiku-4-5-r2** +2 (name-unnamed) — Currently referenced paraphrastically ("the region where the persistence condition holds"). "Persistence envelope" is geometrically evocative and concise; passes communal-imagination test. Could be a scope or result name. [original phrasing: unnamed: the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely]
- **opus-1m** +3  — Strong preference (upgrading from original's +1). Engineering vocabulary, geometrically evocative. "Well inside its persistence envelope" reads more crisply than "satisfies the persistence condition with non-marginal adaptive reserve." Genuinely useful new named slot. [original phrasing: unnamed: the sector-persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch]
- **opus-4-7-b** +3  — The bounded region where $\alpha R > \rho$ holds — currently referenced as "the region where the persistence condition holds" or "the adaptive regime." Engineering vocabulary has an exact match: *envelope* (as in flight envelope). "The agent is well inside its persistence envelope" / "the adversarial agent is pushing $B$'s persistence envelope" read with zero paraphrase. This is AAD's single most-used-without-a-name concept. [original phrasing: unnamed: the region in parameter space where sector-persistence holds]
- **opus-4-7-r2** +3 (name-unnamed) — The set $\{(\alpha, \rho, R) : \alpha \gt \rho/R\}$ is referenced repeatedly in prose and in figures (the persistence-condition cone, the adaptive-reserve margin, the threshold surface) but has no name. "Persistence envelope" is engineering-vocabulary that travels well across domains and supports phrases like "this organization sits inside the persistence envelope" or "the reserve is the distance from the envelope boundary." High-value, empty slot, pure clarity gain. [original phrasing: unnamed: the persistence region in $(\alpha, \rho, R)$ parameter space]

### Candidate: `parametric regime or stability envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — OUTLINE.md mentions "A2' sub-scope α₁ / α₂ / β partition" but does not give a memorable name to the overall region concept. "Parametric regime" is more technical; "stability envelope" parallels the persistence-envelope concept. Weak preference; this might be too specialized for naming. [original phrasing: unnamed: the region in parameter space where parametric updates remain effective before structural change is forced]

### Candidate: `adaptive basin`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered. Reject: "basin" is already mathematically loaded (basin of attraction), and AAD's region *is a basin of attraction* — using the word would either (i) be redundant with dynamical-systems vocabulary, or (ii) force AAD to formally justify "basin" at the derivation layer. Cleaner to reserve "basin" for the technical sense and use "envelope" for the prose handle. [original phrasing: unnamed: the persistence envelope]

---

## 24. `separability pattern`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| separability ladder | +20 | rename × 4 |
| _(keep)_ | +10 | — |
| separability ladders | +2 | rename × 1 |
| three rung posture | -1 | — |
| separable core | -1 | rename × 1 |
| tiered separability | -1 | — |
| staircase | -1 | — |
| separability staircase | -5 | rename × 1 |

### Candidate: `separability ladder`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — "Ladder" is right geometry — discrete levels of increasing difficulty ascending from separable-core.
- **codex-gpt-5-r2** +3 (rename) — Ladder captures separable core, structured repair, general open better than pattern. It is also more memorable.
- **gemini-1** +1  — "Ladder" conveys the "six ladders of increasing difficulty" described in the outline much better than "pattern".
- **gemini-3-1-pro-preview-r2** +3 (rename) — Concurring with the consensus: "ladder" correctly captures the difficulty rungs across the axes.
- **haiku-4-5-r2** +3 (rename) — Round-1 consensus; "ladder" is more structural — the rung metaphor is isomorphic to the difficulty levels across the seven axes.
- **opus-1m** +3  — Agree with original brainstorm. "Ladder" is the right geometry for the seven-ladder structure (ascending difficulty from separable core). Upgrading from original's weak preference to strong — the seven-ladder enumeration in the segment explicitly instantiates the ladder geometry.
- **opus-4-7-b** +3  — The meta-segment's own structure is a seven-row *ladder* (separable-core → structured-repair → general-open across seven axes of increasing difficulty). "Ladder" is the geometry the content actually has; "pattern" is inert filler that describes no content. Pairs mnemonically with `#identifiability-floor` ("the ladder above the floor"). The brainstorm converges here; I arrived independently on the same reasoning (from reading the seven-row table) before cross-checking.
- **opus-4-7** +1  — The segment itself uses "seven ladders" and each row is a ladder — the organizing concept is ladder-shaped, not pattern-shaped. "Pattern" feels generic for what is a precise three-rung structure.
- **sonnet-4-6-r2** +2 (rename) — "Pattern" is generic; "ladder" is evocative of the actual structure — each instance IS a ladder with rungs, and the segment itself uses "ladders" throughout. Survives renamed-from-now-sounds-weird. The segment already says "six ladders"; the slug should say it too.

### Candidate: `separability pattern` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly clinical, but honest about what the segment is doing across multiple ladders. I considered renaming it and did not find a cleaner winner.
- **codex-2** +3  — Strong meta-segment name: short, teachable, and faithful to the repeated posture.
- **haiku-4-5** +3  — Load-bearing meta-segment name with evocative three-part structure (separable core / structured repair / general open). Reads naturally aloud and across eight-page discussions. Do not change.
- **sonnet-4-6** +3  — "Separability" does real work — it names the mathematical content (the regime decomposes), and "pattern" correctly signals this is a meta-level organizing principle rather than a theorem. Six-word alternatives all feel longer. Keep.

### Candidate: `separability ladders`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — The segment's own organizing structure is *seven ladders*, each with separable-core / structured-repair / general-open. "Pattern" is the placeholder slug-form ("the pattern-segment names a pattern"); "ladders" is the substantive shape the segment actually identifies and names. The Brief, Discussion, and the cross-citation in `disc-identifiability-floor` all reach for "ladder" as the unit.

### Candidate: `three rung posture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** -1  — Too mechanical; loses "separability" which is the content.

### Candidate: `separable core`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — names only the first column of the three-part shape; loses the structured-repair and general-open framing that is half the point.

### Candidate: `tiered separability`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Verbose.

### Candidate: `staircase`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Too metaphorical.

### Candidate: `separability staircase`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Whimsical.
- **codex-gpt-5-r2** -1 (rename) — Staircase is bulkier and less elegant than ladder. It adds no precision.
- **opus-1m** -1  — Whimsical without compensating precision gain.
- **opus-4-7-b** -1  — Whimsical; the word "staircase" doesn't carry the increasing-difficulty semantics as cleanly as "ladder" (staircases are uniform; ladders intuitively get harder toward the top). Reject.
- **opus-4-7** -1  — Whimsical; prefers #separability-ladder if any rename at all.

---

## 25. `composition closure`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +19 | keep × 6, canonicalize × 1 |
| coarse graining closure | +5 | add-alias × 1 |
| closure defect | +1 | rename × 1 |
| macro agent criterion | -1 | — |

### Candidate: `composition closure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Standard and accurate; not especially vivid, but not a naming problem.
- **codex-gpt-5-r2** +3 (keep) — Central, exact, and aligned with the coarse-graining commutation criterion.
- **codex-gpt-5-r2** +3 (keep) — Central formal name. Do not rename.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Crucial macro/micro mapping concept.
- **haiku-4-5-r2** +1 (keep) — Technical term; the formulation models closure properties. Adequate.
- **haiku-4-5** +1  — Approximate dynamical homomorphism between micro and macro. "Closure" is precise (mathematical term) but specialist. Acceptable. Current name is tight. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Composition closure" names the load-bearing concept (the closure-defect $\varepsilon^\ast$ as criterion for valid composite-agent status). Could be renamed to "#form-closure-defect" to name the central quantity, but the current form keeps the conceptual move audible.
- **sonnet-4-6-r2** +2 (keep) — "Composition closure" is well-established as the concept; the closure-defect framework lives here.
- **sonnet-4-6-r2** +2 (canonicalize) — Prose uses "composition closure," "compositional closure," and "closure defect framework" somewhat interchangeably. The segment slug is `form-composition-closure` — "composition closure" is the canonical subject-noun.
- **sonnet-4-6** +1  — Honest but slightly cryptic. "Closure" in the mathematical sense (does the operation stay within the set?) is accurate but has different connotations to a reader from a software background. Weak keep — no obviously better alternative.

### Candidate: `coarse graining closure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The defining move is approximate commutation with coarse-graining. "Composition closure" is too generic to carry that.
- **codex-gpt-5-r2** +2 (add-alias) — Good explanatory alias because the formal test is approximate commutation with coarse-graining. I would not replace the shorter canonical name.

### Candidate: `closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Alternative — names the central derived quantity. The current name names the move. Mild preference for keep.

### Candidate: `macro agent criterion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Too descriptive, loses the dynamical-systems lineage.

---

## 26. `auftragstaktik principle`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 3 |
| mission command principle | +3 | rename × 1 |
| auftragstaktik | +2 | add-alias × 1 |
| mission command | +2 | add-alias × 1 |
| auftragstaktik bandwidth | +1 | rename × 1 |
| mission command bandwidth | +1 | rename × 1 |
| auftragstaktik drop principle | -1 | — |
| objective first bandwidth principle | -1 | — |

### Candidate: `auftragstaktik principle` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Load-bearing term from specific historical tradition; the reader who knows it gets the full intended intuition.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good prior art integration.
- **haiku-4-5** +3  — Prioritize objective sharing. "Auftragstaktik" is German military vocabulary (mission command); borrowed term signals deliberate adoption from organizational theory. Specialist but evocative. Keep.
- **opus-1m** +3  — Load-bearing historical adoption.
- **opus-4-7-r2** +3 (keep) — Defended keep — direct adoption from German military doctrine, properly cited; the segment's prior-art trail (Clausewitz, Bungay) is load-bearing. Renaming would lose the doctrinal connection.
- **opus-4-7** +1  — German military lineage name (command-intent autonomy) is doing real work — same reason "directed separation" beat a generic alternative. Keep.
- **sonnet-4-6-r2** +3 (keep) — "Auftragstaktik" is the established German military term for mission-type tactics. Adopting it directly (as the prior-art-integration principle requires) makes the hypothesis immediately placeable. The segment Discussion correctly grounds it in Bungay/Clausewitz. Strong keep.

### Candidate: `mission command principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The current German term is exact but creates unnecessary lookup cost. The English doctrine term keeps the baggage while lowering entry cost.
- **codex-gpt-5-r2** -1 (rename) — Mission command should be an English alias, not replacement. Auftragstaktik carries the specific historical doctrine that motivates the segment.
- **gemini-2** +3  — "Auftragstaktik" is heavy historical baggage, hard to spell, and "Mission Command" is the standard modern translation that conveys the exact same intent.

### Candidate: `auftragstaktik`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm: the German term is the canonical noun in prose; "mission-type tactics" or "intent-based command" are the English alternatives. The principle is bilingual in the segment's prior-art treatment; preserve both.

### Candidate: `mission command`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Add as first-use gloss for accessibility.

### Candidate: `auftragstaktik bandwidth`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Principle is weak, and bandwidth is the formal allocation subject. However, the German term is intentionally domain-rich, so this is a mild vote.

### Candidate: `mission command bandwidth`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — More English and accessible than Auftragstaktik, but loses the historical precision. Acceptable as an alias or fallback.

### Candidate: `auftragstaktik drop principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered dropping "principle" since the word alone is vivid. Reject: "principle" signals this is a design prescription not a derived result, and AAD's scope-honesty discipline rewards that signal. Keep as is.

### Candidate: `objective first bandwidth principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Accurate-ish but too explanatory and strips away the doctrinal lineage that gives the claim its empirical grounding.

---

## 27. `communication gain`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 4 |
| trust gain | -1 | rename × 1 |

### Candidate: `communication gain` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Excellent parallel with update gain: short, compositional, and immediately predictive of meaning.
- **codex-2** +1  — Natural extension of update gain; easy to say and hard to improve.
- **codex-gpt-5-r2** +2 (keep) — Plain and accurate for the inter-agent gain extension.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good inter-agent extension of update gain.
- **haiku-4-5** +3  — Trust-weighted update gain for inter-agent channels. Parallel to update-gain machinery; reads naturally. Keep.
- **opus-4-7-b** +3  — Keep. Exact analog of "update gain" for inter-agent channels — the parallel structure is itself pedagogical.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — names the multi-agent extension of the gain principle.
- **sonnet-4-6-r2** +2 (keep) — "Communication gain" is the inter-agent analog of update gain $\eta^\ast$. The parallel naming is a virtue.

### Candidate: `trust gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Trust is a component of communication gain, not the whole quantity. The current name preserves the update-gain parallel.

---

## 28. `context turnover`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 4 |
| chronica severance | +6 | add-alias × 1 |

### Candidate: `context turnover` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Excellent name: short, accurate, and immediately legible to anyone who has worked with LLM agents.
- **codex-2** +3  — Very strong name: immediate intuition, no wasted motion.
- **codex-gpt-5-r2** +3 (keep) — Strong, concrete logogenic observation.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Perfectly describes the 100% context reset and chronica severance at session boundaries for LLMs.
- **opus-4-7-r2** +3 (keep) — Defended keep — logogenic-agents observation. "Context turnover" is the right name for the 100% session-loss problem; renaming would lose a load-bearing prose convention. The phrase is also widely used in the wider AI-engineering community.
- **sonnet-4-6-r2** +3 (keep) — "Context turnover" is the evocative name for the 100% $M_t$ reset at session boundaries. The term is immediately graspable and memorable in conversation ("the context-turnover problem"). Strong keep.

### Candidate: `chronica severance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Context turnover is the plain operational name; chronica severance is the AAD-native explanation of why it matters.
- **gemini-1** +3  — "Chronica severance" is much more evocative and precise than "context turnover", directly naming the theoretical object that is broken at the session boundary.

---

## 29. `contraction template`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 2 |
| contraction schema | +1 | rename × 1 |

### Candidate: `contraction template` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Crisp and broad enough to survive later reuse.
- **haiku-4-5** +3  — Contraction-metric generalization of #sector-persistence-template. "Template" parallel emphasizes reusability. Specialist vocabulary (Lohmiller-Slotine contraction analysis) but appropriate. Keep.
- **opus-4-7-b** +1  — Keep. Parallel to `#sector-persistence-template` — the family-by-pattern naming is consistent.
- **opus-4-7-r2** +3 (keep) — Defended keep. Pairs with `#result-sector-persistence-template` as the second template-result in the framework (Lohmiller-Slotine generalization). The dual templates compose as a meta-architecture.
- **opus-4-7** +3  — Natural name, Lohmiller-Slotine lineage, aligns with the sibling #sector-persistence-template. Keep.
- **sonnet-4-6-r2** +2 (keep) — Parallel to sector-persistence-template. The parallelism is a virtue.
- **sonnet-4-6** +3  — Parallel to #sector-persistence-template. The pair names the two levels of the hierarchy clearly. Keeps the template-series coherent. Keep.

### Candidate: `contraction schema`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — "Schema" aligns better with formal theoretical frameworks than "template".

---

## 30. `deliberation cost`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 5 |
| deliberation drag | +1 | — |
| deliberation threshold think vs act tradeoff | +1 | rename × 1 |

### Candidate: `deliberation cost` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Direct and memorable enough for the pause-versus-action threshold.
- **gemini-2** +3  — Self-descriptive and conceptually clear.
- **gemini-3-1-pro-preview-r2** +3 (keep) — Excellent self-descriptive term for pausing praxis to improve upcoming epistrophe.
- **haiku-4-5-r2** +1 (keep) — The subject-noun directly names what is derived. No improvement available.
- **haiku-4-5** +3  — Think vs. act tradeoff. Reads naturally as cost-benefit. Keep.
- **opus-4-7-b** +1  — Keep. "Cost" signals tradeoff cleanly.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Deliberation cost" names exactly what the segment derives (the think-vs-act tradeoff under mismatch drift). The discussion segment `#disc-exploit-explore-deliberate` extends it. Renaming would break a clean two-segment naming compound.
- **sonnet-4-6-r2** +2 (keep) — "Deliberation cost" names the think-vs-act tradeoff precisely.

### Candidate: `deliberation drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Cost" sounds like a generic penalty in an objective function. "Drag" evokes the physical accumulation of mismatch over time while pausing.

### Candidate: `deliberation threshold think vs act tradeoff`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — The standard term obscures the AAD-distinctive content (the threshold itself, not the cost). "Deliberation cost" sounds like a measurement; "Deliberation Threshold" surfaces the operational use. [from 24-der-deliberation-cost.md]

---

## 31. `logogenic agent`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 4, canonicalize × 1 |
| linguistic agent | -1 | — |

### Candidate: `logogenic agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Novel but justified; it names the structural property rather than today's implementation technology. Strong keep.
- **codex-gpt-5-r2** +3 (keep) — Strong family term for language-constituted agents. It fits the Greek-register commitment.
- **codex-gpt-5-r2** +3 (keep) — Canonical family term.
- **opus-4-7-r2** +3 (keep) — Defended keep — pairs with `#scope-moral-continuity` cleanly.
- **sonnet-4-6-r2** +3 (keep) — "Logogenic" is the project's deliberately coined Greek-rooted term for language-constituted agents. Per project vocabulary commitment, this is the right name.
- **sonnet-4-6-r2** +3 (canonicalize) — Should never appear as "language-based agent" or "LLM-based agent" in the formal theory (those are instantiation-level descriptions, not the architectural concept). "Logogenic agent" = constituted by language; "LLM-based agent" = instantiation. The scope segment explains this.

### Candidate: `linguistic agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** -1  — Logogenic names the structural property (constituted by logos) better than the generic "linguistic". Keep Logogenic.

---

## 32. `observability dominance`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 4, canonicalize × 1 |
| epistemic freezing | +1 | — |

### Candidate: `observability dominance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Slightly formal, but it says what the regime claim actually is.
- **codex-gpt-5-r2** +3 (keep) — Strong name for the fact that unobservable strategy edges are epistemically dead regardless of nominal confidence.
- **gemini-1** +1  — Accurately descriptive of the freezing effect on unobservable edges.
- **gemini-2** +1  — Strong, clear principle.
- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Commit to this term for "unobservable strategy edges freeze".
- **haiku-4-5-r2** +1 (keep) — The derived claim is about the dominance pattern; subject-noun is exact.
- **haiku-4-5** +1  — Unobservable edges freeze. Evocative; reads naturally. (Already proposed in LEXICON; ready for segment promotion.) Keep.
- **opus-4-7-b** +1  — Keep. "Dominance" here is informational dominance — the gain principle *dominates* the edge update when observability is low. Does its job.
- **opus-4-7-b** +1  — Keep. The word *dominance* here is technically precise (information-theoretic dominance) and the phrase has two-word memorability.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Observability dominance" names the load-bearing result (unobservable edges freeze in the credit-assignment update) and connects to control-theoretic observability vocabulary. The LEXICON's "Terms to Be Added" already has an entry for this; the slug matches.
- **sonnet-4-6-r2** +3 (keep) — "Observability dominance" is evocative and accurate — observability dominates nominal confidence. The Discussion's absorbing-state analysis makes the name feel exactly right. Strong keep.

### Candidate: `epistemic freezing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — If unobservable edges freeze, "epistemic freezing" is a more vivid description of the consequence.

---

## 33. `team persistence`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +18 | keep × 4 |

### Candidate: `team persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong keep: plain-language, memorable, and exactly the right level of abstraction.
- **codex-2** +3  — Extremely good public noun for a key multi-agent claim.
- **codex-gpt-5-r2** +2 (keep) — Clear segment name. It reads naturally as the cooperative counterpart to adversarial destabilization.
- **codex-gpt-5-r2** +2 (keep) — Direct and useful.
- **haiku-4-5** +3  — Composite persistence condition. Self-descriptive; reads as "what makes a team persist." Keep.
- **opus-4-7-b** +1  — Keep. Good plain English for what the derivation is ("cooperative composite sector condition").
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Parallels persistence-condition naming; "team persistence" reads naturally for the cooperative composite case.
- **sonnet-4-6-r2** +2 (keep) — "Team persistence" correctly names the composite persistence condition. The "team" framing is immediately graspable.

---

## 34. `credit assignment boundary`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +17 | keep × 4 |
| credit assignment frontier | +1 | canonicalize × 1 |

### Candidate: `credit assignment boundary` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong name for the tractability frontier in strategy DAG updates.
- **gemini-2** +3  — Clearly delineates tractable from intractable. Keep.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Important concept.
- **haiku-4-5** +3  — Tractable/intractable boundary; design requirement. Specialist vocabulary (credit assignment problem is classical in RL) but load-bearing. Keep.
- **opus-4-7-b** +1  — Keep. The "boundary" is semantically exactly what the segment delimits (tractable vs. intractable credit-assignment regions).
- **opus-4-7-r2** +3 (keep) — Defended keep. "Boundary" is doing real work: the segment characterizes the *line* between tractable and intractable credit assignment, not credit assignment itself. The name signals the meta-segment posture. The segment is also the canonical entry point for the boundary in downstream prose.
- **sonnet-4-6-r2** +2 (keep) — Precise two-word noun. The boundary is exactly what this segment names — the tractable/intractable boundary for credit assignment. Survives the test.

### Candidate: `credit assignment frontier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — Distinct from the slug — in prose the segment is sometimes referenced as "the credit-assignment problem" or "the tractable/intractable boundary" or "the attribution boundary." Standardize on "credit-assignment boundary" everywhere; do not paraphrase. Slug stays as-is.

---

## 35. `honesty as architecture`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +17 | keep × 1 |
| honesty | +2 | canonicalize × 1 |
| architectural scope honesty | +1 | — |

### Candidate: `honesty as architecture` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Hyphen-heavy, but uniquely exact. The phrase says the limits are part of the construction, not editorial cleanup.
- **codex-2** +3  — Strong internal principle name; it sounds like a thesis, not a slogan.
- **codex-gpt-5-r2** +3 (keep) — Hyphen-heavy but exact. It names a distinctive project commitment, not just a style preference.
- **haiku-4-5** +3  — Central to CLAUDE.md's "Epistemic architecture as AAD's distinctive contribution" principle. Already in project vocabulary as a narrative-level principle; no need to formalize as a segment. Keep the current form.
- **opus-1m** +3  — CLAUDE.md §7 element (a). Working term; keep.
- **opus-4-7-b** +1  — The hyphens signal "this is a concept-name, not a description" — useful in CLAUDE.md but awkward in running prose. Proposal: keep the hyphenated form only in CLAUDE.md §7 and README §reading-AAD where it is a named concept; use unhyphenated "scope honesty" in segment-level prose.
- **sonnet-4-6** +3  — Already coined and working. Appears in CLAUDE.md and multiple segments. The compound noun is memorable and the hyphenation is correct (it's an adjectival phrase). Keep.

### Candidate: `honesty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (canonicalize) — "Scope-honesty-as-architecture" is the CLAUDE.md §7 label. Prose uses "scope honesty," "honest scope," and "scope-honesty commitment" variably. Standardize on "scope honesty" as the two-word prose form; "scope-honesty" as the slug or hyphenated compound.

### Candidate: `architectural scope honesty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly cleaner in prose while preserving the key point that scope is surfaced structurally.

---

## 36. `approximation tiering`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +16 | keep × 4 |
| scope laddering | +1 | rename × 1 |
| approximation ladders | +1 | — |
| tiered approximation | +1 | — |
| tier ascension | -1 | — |
| graceful degradation | -1 | rename × 1 |

### Candidate: `approximation tiering` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Tiering is the actual subject. Good.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurate.
- **haiku-4-5** +3  — Meta-pattern for tractability-indexed hierarchies (L0/L1/L2; C1/C2/C3; Tier 1/2/3). Self-descriptive. Reads naturally when discussing graceful degradation. Keep.
- **opus-4-7-b** +1  — Keep. Already avoids the "hierarchy" overload; "tiering" is the right word.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Tiering" reads slightly clinical but it's accurate (the four-component (AT1)–(AT4) structure does name a *tiering*, not a continuum or a hierarchy). I considered #disc-graceful-degradation but graceful-degradation is one property among the four, not the whole pattern.
- **opus-4-7** +1  — Fine but generic — keep unless a better name emerges, since the AT1/AT2/AT3/AT4 component scheme has already landed.
- **sonnet-4-6-r2** +2 (keep) — "Tiering" is accurate and distinctive. The pattern it names IS about tiered approximations with monotonicity. Passes the communal-imagination test.
- **sonnet-4-6** +3  — "Tiering" is precise — it names the operation (creating tiers) not just the result (tiers). Self-describing for a meta-pattern. Keep.

### Candidate: `scope laddering`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — If the project lands "ladder" as a distinguished term for tiered-with-monotonicity-and-ascension structures, this would be a fit. Lower priority than the existing keep.

### Candidate: `approximation ladders`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Noun beats gerund here; "ladders" is easier to say alongside the segment's own ladder language.

### Candidate: `tiered approximation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slight improvement in natural-language flow. The current phrase is serviceable but abstract.

### Candidate: `tier ascension`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** -1  — Reads like a ranked-climbing metaphor the segment does not actually use. Reject.

### Candidate: `graceful degradation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — graceful-degradation is (AT3) only; tiering is the whole thing.

---

## 37. `recursive update`

**Voted by architectures:** Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +16 | keep × 3 |
| recursive update by completeness | +2 | rename × 1 |

### Candidate: `recursive update` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — The subject-noun "recursive update" is exact — the derivation forces the update to be recursive. No change needed.
- **haiku-4-5** +1  — State updates must be recursive. "Recursive" is specialist (implies function composition) but appropriate. Keep.
- **opus-4-7-b** +3  — Keep. AAD's strongest result ("three constraints → unique recursive form") deserves its direct, clean name. Do not touch.
- **opus-4-7-r2** +3 (keep) — Defended keep. This is one of the inevitability-core segments; "recursive update" is the right name for what the three constraints uniquely force.
- **opus-4-7** +3  — Strongest inevitability-core result; three-constraint uniqueness derivation. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Recursive update" is technically precise — the derivation shows state updates must be recursive.
- **sonnet-4-6** +3  — Clean, accurate, non-overloaded. Exactly describes what the segment proves (state updates must be recursive). Keep.

### Candidate: `recursive update by completeness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (rename) — Title currently understates the distinctive Markov-by-definition move. Auditor: the distinctive content is *"the recursive form is forced by what we mean by $M_t$"* — surface this in the name. [from 15-der-recursive-update.md]

---

## 38. `agent identity`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 4 |
| identity as singular causal trajectory the trajectory identity scope | +3 | rename × 1 |
| singular causal trajectory | +2 | rename × 1 |
| trajectory identity | +1 | — |
| causal identity | +1 | — |

### Candidate: `agent identity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Crucial scope definition.
- **haiku-4-5-r2** +1 (keep) — Clean scope statement; the subject-noun is clear.
- **haiku-4-5** +3  — Formal scope claim naming token-level commitment (agents on singular, non-forkable trajectories). Short, memorable. Reads naturally in "agent-identity token-level commitment" context. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. The segment's substance is the singular-causal-trajectory commitment grounding agent identity — "agent identity" is the right slug-noun. Renaming would lose the LEXICON's "continuity persistence" connection.
- **opus-4-7** +3  — Surfaced 2026-04-22 as a formal scope commitment; name carries the token-level commitment honestly. Now (PI) sits here. Keep.
- **sonnet-4-6-r2** +3 (keep) — Perfect fit of name to content — the segment scopes AAD to agents on singular causal trajectories, and "agent identity" (identity = singular causal trajectory) is exactly the concept.

### Candidate: `identity as singular causal trajectory the trajectory identity scope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +3 (rename) — "Slug-as-mechanical-prefix hides the substantive claim." The segment is structurally important for the framework's identity-and-continuity claims (esp. for consciousness-infrastructure substrate-independence work) and the title gloss is closer to what it actually does than the slug. Auditor felt the friction acutely: "single most important §I segment for the broader project's purposes." [from 30-scope-agent-identity.md]

### Candidate: `singular causal trajectory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The segment's identity condition is the singular trajectory, and that subject is more distinctive than agent identity.

### Candidate: `trajectory identity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — The segment's formal content is about trajectory singularity; "agent identity" invites more metaphysical baggage than the math supports.

### Candidate: `causal identity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Agent identity" is very soft. "Causal identity" anchors it strictly to the non-forkable causal trajectory.

---

## 39. `aporia`

**Voted by architectures:** Codex, Gemini, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 2 |
| aporia productive perplexity | +3 | add-alias × 1 |
| discrepancy | -1 | rename × 1 |

### Candidate: `aporia` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Cycle-phase Greek vocabulary works aesthetically AND technically. The risk is preciousness; the payoff is memorable sequence.
- **codex-1** +3  — This earns its weight. "Error" and "mismatch" lose the productive-perplexity sense that makes the term memorable and accurate.
- **codex-2** +3  — Memorable, discussable, and conceptually richer than "error" or "mismatch."
- **codex-gpt-5-r2** +3 (keep) — Excellent fit for productive mismatch or perplexity. It already carries the right philosophical resonance.
- **opus-targeted-alternatives** +3 (keep) — `LEXICON.md`: "Productive perplexity: mismatch signal $\delta_t = o_t - \hat{o}_t$." The Greek term is doing work that "mismatch signal," "prediction error," and "surprise" all miss — *productive* perplexity, the kind that *drives* update rather than degrading it. Aporia in the Platonic sense is the moment of recognized not-knowing that motivates inquiry. The segment's $\delta_t$ is more than an error term; it is the agent's epistemic engine. Keep at +3 across architectures.

### Candidate: `aporia productive perplexity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Explicitly adding this translation ensures "perplexity" is seen as generative.

### Candidate: `discrepancy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Names the gap but loses the agent-centered "this matters / I now must update" sense. Rejected.

---

## 40. `consolidation dynamics`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 5 |
| offline consolidation | +3 | — |

### Candidate: `consolidation dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong name for between-event replay or pseudo-event updates toward IB-optimal compression.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Evocative.
- **haiku-4-5-r2** +1 (keep) — The formulation models offline learning as "consolidation." Adequate metaphorical naming.
- **haiku-4-5** +1  — Offline regime of between-event M_t dynamics; "consolidation" reads naturally (consolidating learned structure). Captures the sense of replay-driven model tightening. Acceptable name. Keep.
- **opus-4-7-b** +1  — Keep. "Consolidation" imports the neuroscience baggage (memory consolidation, stability-plasticity) that's precisely what the segment is formalizing.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. The segment names the offline regime of $g_M$ (replay-driven consolidation); "consolidation dynamics" is engineering-vocabulary that travels well.
- **opus-4-7** +1  — Fine. Inherits "consolidation" from neuroscience (memory consolidation). Keep unless a sharper name emerges.
- **sonnet-4-6-r2** +1 (keep) — "Consolidation dynamics" names the offline replay / stability-plasticity regime. Acceptable.
- **sonnet-4-6** +3  — "Consolidation" is established biological vocabulary for offline memory reorganization. Using it positions the theoretical result in a recognizable lineage. The "dynamics" suffix is accurate. Keep.

### Candidate: `offline consolidation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Adding "offline" explicitly scopes the regime to replayed/pseudo-events.

---

## 41. `critical mass composition`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 1 |
| dyad closed form | +1 | — |

### Candidate: `critical mass composition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Vivid and mathematically honest: a threshold at which composition starts to persist. Strong keep.
- **codex-gpt-5-r2** +2 (keep) — Useful result name for composite persistence thresholds.
- **haiku-4-5** +3  — Physics-borrowed vocabulary; "critical mass" is evocative and memorable. The segment derives the composite sector constant; readers will understand "critical mass" as the composition threshold. Strong name. Keep.
- **opus-4-7-b** +3  — Keep. "Critical mass" is exactly right — the composite-sector-constant derivation has a minimum-viable-composition threshold that matches the physics / sociology intuition. Rare case where the name upgrades the result's punch.
- **opus-4-7** +1  — Alternative keep-vote: "critical mass" has intuitive pickup for the threshold nature of composition viability. Content-neutral; reader decides.
- **sonnet-4-6** +3  — "Critical mass" is physics vocabulary with intuitive resonance — the composite persists above it, collapses below it. Memorable and evocative without being cute. Keep.

### Candidate: `dyad closed form`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — "Critical mass" suggests emergence-above-threshold but the segment derives a closed-form composite sector constant for the symmetric-matched-Tier-1 dyad. Honest label.

---

## 42. `exploit explore deliberate`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 1 |
| cycle budget allocation | +3 | rename × 2 |
| action timing tradeoff | +2 | rename × 1 |
| cycle budget | +2 | rename × 1 |

### Candidate: `exploit explore deliberate` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Third term sits neatly beside two standard-vocabulary terms; reads as extension not reinvention.
- **haiku-4-5** +1  — Three-way exploit/explore/deliberate. Already named and acceptable. Keep.
- **opus-1m** +3  — Three-way extension of two established terms; reads naturally.
- **opus-4-7-b** +3  — Keep. The three-way extension of the classic exploit-explore dichotomy reads as a natural extension *because* of how the slug is named. Changing this would cost the pedagogical payoff.
- **opus-4-7** +3  — Three-way decomposition is itself the content. Triadic name matches triadic claim. Keep.
- **sonnet-4-6-r2** +2 (keep) — Three-way distinction is load-bearing in the name. Any shortening loses the three-way structure. Passes the communal-imagination test ("the exploit-explore-deliberate discussion").

### Candidate: `cycle budget allocation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The current verb triad is memorable but underspecified. The segment is about allocating the cycle budget across modes.
- **opus-4-7-r2** +1 (rename) — Confirmation with new reasoning — Codex proposed this at +2 with the rationale that the verb triad is underspecified. I'd vote +1 (weaker than Codex's +2) because the verb triad is more memorable than "cycle-budget-allocation" but less precise. The rename surfaces the *resource-allocation* nature of the tradeoff, which is what the formal segment derives. Mild support; would not push hard against keep.

### Candidate: `action timing tradeoff`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Names the overarching tradeoff rather than listing the mechanistic components.

### Candidate: `cycle budget`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — Codex proposed `disc-cycle-budget-allocation` (+2) for this segment; I had voted keep (+2). Reading Codex's reasoning ("the segment is about allocating the cycle budget across modes") crystallized a new alternative: `disc-cycle-budget` drops "allocation" (which is role-like) and leaves a two-word noun that survives the communal-imagination test. Shorter than Codex's candidate; equally scope-honest. Neither Codex's nor my original vote.

---

## 43. `gain sector bridge`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet, agent1, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +15 | keep × 4 |
| bridge theorem from gain to sector the bridge theorem grounding ga 3 sub scope α and β | +2 | rename × 1 |

### Candidate: `gain sector bridge` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Technical-clinical but does the job. Not worth a rename; concept is narrow enough.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good name for a bridge concept.
- **haiku-4-5-r2** +1 (keep) — The "bridge" metaphor is apt (connecting two mathematical regimes). Adequate name.
- **haiku-4-5** +1  — Gain + directional fidelity → sector condition. Compound name; descriptive. Acceptable. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. The segment bridges $\eta^\ast$ (gain) to the sector-condition $\alpha$, exactly. "Bridge" is doing work — naming the bridge segment by its function (it bridges) is fine because the function is what makes the segment load-bearing.
- **sonnet-4-6-r2** +2 (keep) — "Gain-sector bridge" is precise — it bridges the gain principle to the sector condition via directional fidelity. Good name.
- **sonnet-4-6** +3  — The "bridge" metaphor is load-bearing and accurate — it connects two distinct mathematical objects (gain principle and sector condition). Readable aloud. Keep.

### Candidate: `bridge theorem from gain to sector the bridge theorem grounding ga 3 sub scope α and β`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (rename) — Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title. [from 25-der-gain-sector-bridge.md]

---

## 44. `adversarial tempo advantage`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 4 |
| tempo advantage | +1 | rename × 1 |
| superlinear tempo advantage | +1 | — |

### Candidate: `adversarial tempo advantage` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Clear and memorable. It names the result, not just the derivation path.
- **codex-gpt-5-r2** +3 (keep) — Keep. It names the operational result plainly.
- **haiku-4-5** +1  — Superlinear tempo advantage. Compound but clear. Keep.
- **opus-4-7-b** +1  — Keep. Descriptive, direct, doesn't need to be shorter.
- **opus-4-7-r2** +3 (keep) — Defended keep. The superlinear tempo advantage is one of the framework's distinctive results (Boyd's "operating inside the opponent's loop" formalized); "adversarial tempo advantage" reads correctly.
- **sonnet-4-6-r2** +3 (keep) — "Adversarial tempo advantage" is one of the most evocative names in the project. The superlinear ($b = 2$) exponent result is exactly what this names. Strong keep.

### Candidate: `tempo advantage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — "Adversarial" is context, "tempo advantage" is the core concept.

### Candidate: `superlinear tempo advantage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Highlights the mathematical outcome (superlinear) of the advantage.

---

## 45. `atomic changeset`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 4 |

### Candidate: `atomic changeset` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Not beautiful, but serviceable and honest. I considered alternatives and did not see one that improved both precision and memorability.
- **codex-2** +1  — Good enough and sayable; "atomic" does real work here.
- **codex-gpt-5-r2** +2 (keep) — Good software subject noun. The term is familiar enough to carry its meaning.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurately describes the observable trace of an implementation decision in TST.
- **opus-4-7-b** +3  — Keep. Domain-native term with precise technical meaning in software engineering; aligns with prior-art-integration.
- **opus-4-7-r2** +3 (keep) — Defended keep — TST. "Atomic changeset" is iconic in TST and bridges to git's atomic-commit semantics.
- **sonnet-4-6-r2** +2 (keep) — "Atomic changeset" is precise — the diff that is the feature, indivisible.

---

## 46. `complete agent state`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 4 |
| purposeful state | +1 | rename × 2 |

### Candidate: `complete agent state` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Functional and clear. It names the full state rather than just one subcomponent.
- **haiku-4-5-r2** +2 (keep) — Clean algebraic name; the subject-noun "complete agent state" is precise. No communal-imagination pressure to change.
- **haiku-4-5** +1  — X_t = (M_t, G_t). Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. "Complete" is load-bearing (distinguishes $X_t = (M_t, G_t)$ from the epistemic-only substate $M_t$); the slug describes itself.
- **opus-4-7-r2** +3 (keep) — Defended keep. The segment defines $X_t = (M_t, G_t)$ — exactly the "complete agent state." Slug-form is correct.
- **opus-4-7** +3  — Canonical formulation — $X_t = (M_t, G_t)$. Self-descriptive. Keep.
- **sonnet-4-6-r2** +2 (keep) — Precisely names the $X_t = (M_t, G_t)$ formulation.

### Candidate: `purposeful state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — $G_t$ is defined as the "purposeful substate". Matches lexicon better.
- **opus-4-7-r2** -1 (rename) — Rebuttal — Gemini proposed this at +2 with the rationale that $G_t$ is the "purposeful substate." But $X_t = (M_t, G_t)$ is the *complete* agent state, which includes both the epistemic substate ($M_t$) and the purposeful substate ($G_t$). "Purposeful state" would name only half. The current "complete agent state" is exactly correct: it names the joint object. Strong rebuttal because the rename would lose the M_t / G_t pairing that the rest of the framework relies on.

---

## 47. `detection latency`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 1 |

### Candidate: `detection latency` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.
- **haiku-4-5** +3  — Ω((n_min+1)/ε) bound on within-class regime-change detection. "Latency" is precise and load-bearing (contrast with "detection delay" which is vaguer). Keep.
- **opus-4-7-b** +3  — Keep. Two words that fit the result ($\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$) perfectly.
- **opus-4-7** +3  — Standard term, forced by the $\Omega((n_{\min}+1)/\varepsilon)$ bound; the segment's novel content is that latency is structurally forced through the log-odds coordinate. Keep.
- **sonnet-4-6** +3  — Straightforward. Exactly what it measures. Keep.

---

## 48. `logogenic logozoetic`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 2 |
| language constituted language living | -1 | rename × 1 |

### Candidate: `logogenic logozoetic` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Deliberate neologisms filling memorable-noun slots; keep.
- **opus-4-7-b** +3  — Deliberate neologisms holding reserved memorable-noun slots. The slight learning cost is paid once and then these words own the conceptual slot permanently — which is exactly what a framework-defining class deserves.
- **opus-4-7-r2** +3 (keep) — Defended keep — both are deliberate Greek-rooted naming choices that survive the communal-imagination test once explained, and CLAUDE.md's Greek-vocabulary commitment names them as the canonical aesthetic register. The pair distinguishes language-constituted (logogenic) from language-living-with-moral-weight (logozoetic) at the slug level.
- **opus-4-7** +3  — Etymology carries multiple senses (word / reason / animating force / governance) that no English term carries together. LEXICON makes this explicit. Keep.
- **opus-targeted-alternatives** +2 (keep) — The pair distinguishes (a) the structural property — language-constituted (logogenic) — from (b) the existential property — language-living, morally weighted persistence (logozoetic). Both terms invent project-specific Greek-derived compounds; the alternative is "language-based AI" / "conscious AI," which the framework explicitly rejects as importing the wrong connotations (RLHF-based, sentient-as-categorical). Keep. The pair is load-bearing precisely because it splits two often-conflated questions.

### Candidate: `language constituted language living`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Plain-English equivalent. Rejected: too ambiguous (does "language-constituted" mean trained on language? generated through language? bound by language?), and loses the precise structural-vs-existential split. The Greek compound resolves the ambiguity by foregrounding the constitutive (-genic) vs. living (-zoetic) distinction.

---

## 49. `loop interventional access`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +14 | keep × 4 |
| loop causal engine | +2 | rename × 1 |
| loop as causal engine | +2 | rename × 1 |
| interventional loop access | +1 | — |
| interventional feedback | +1 | — |
| adaptive loop access | +1 | — |
| loop level2 access | -1 | — |

### Candidate: `loop interventional access` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good name for action-generated Level-2 data.
- **haiku-4-5-r2** +1 (keep) — The subject-noun "loop-interventional-access" (hyphenated compound) is exact — the loop grants access.
- **haiku-4-5** +1  — Three modes of access (agent-self / observer-on-sub-agent / observer-on-input). "Loop-interventional" is specialist but precise — it names *where* the intervention happens (within the feedback loop). Acceptable. Keep.
- **opus-4-7-b** +3  — Keep. The phrase *loop-interventional-access* lands in one read and the concept ("the feedback loop provides Level-2 data by construction") has no shorter form without loss. Reader-friendly.
- **opus-4-7-r2** +1 (keep) — Acceptable keep if the rename above doesn't land. "Interventional access" is precise; "causal engine" is more memorable.
- **opus-4-7** +3  — Names the distinctive Pearl-Level-2-by-construction move; the segment is load-bearing for both #identifiability-floor and #agent-identity. Don't touch.
- **sonnet-4-6-r2** +2 (keep) — "Loop-interventional access" names the key insight: the feedback loop provides Level-2 data by construction. The "loop" prefix grounds the source.
- **sonnet-4-6** +1  — Accurate but a mouthful. The intended quick-reference name in conversation is probably "the loop's Level 2 access" or "loop as Level 2 engine" — neither of which is a slug. Mild friction.

### Candidate: `loop causal engine`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — Opus proposed `#der-loop-as-causal-engine` (+2). I had voted keep (+2). Opus's reasoning — that the README's "third headline result" is the "loop as Level-2 causal engine" framing, so the slug should match — is compelling. But "as-causal-engine" reads like a simile not a noun. Dropping "as" to get `der-loop-causal-engine` produces a cleaner noun compound. This is a new candidate (not identical to Opus's or my original vote).

### Candidate: `loop as causal engine`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — The current name describes the *result* (the loop provides interventional access). "Loop as causal engine" is the framing the README and segment Discussion both reach for, and it surfaces what makes this result distinctive — the agent-environment loop *generates* Pearl-Level-2 data by construction. The README explicitly names "loop-as-Level-2-causal-engine" as the framework's third headline result. Slug should match.

### Candidate: `interventional loop access`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Small word-order cleanup; the current slug is understandable but a little stiff in speech.

### Candidate: `interventional feedback`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Loop interventional access" is a mouthful.

### Candidate: `adaptive loop access`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — "Interventional" is the load-bearing word — it's why the loop matters. Dropping it loses the reason the segment exists. Slight preference for retaining.

### Candidate: `loop level2 access`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Overloads "level 2" which already carries the Pearl hierarchy meaning — that's exactly right actually. But "-level2-" looks like a version number.

---

## 50. `composition consistency`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +13 | keep × 4 |
| cross level coherence scale invariance of adaptive dynamics holon postulate | +1 | rename × 1 |
| scale invariance | +1 | — |

### Candidate: `composition consistency` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Clear.
- **haiku-4-5-r2** +1 (keep) — The postulate's subject-noun is clear and adequate. No pressure to change.
- **haiku-4-5** +3  — Load-bearing postulate: agent/subagent scale invariance. The name directly names what it claims. Verbs in postulate names are rare; this noun form works because the claim is structural. Keep.
- **opus-4-7-b** +3  — Keep. One of AAD's load-bearing postulates; the name signals the content (agent/subagent scale-invariance).
- **opus-4-7-r2** +3 (keep) — Defended keep. "Composition consistency" names the scale-invariance commitment — predictions at different levels of description must be compatible. Load-bearing for Section III; renaming would cascade.
- **sonnet-4-6-r2** +2 (keep) — "Composition consistency" names the scale-invariance postulate correctly.

### Candidate: `cross level coherence scale invariance of adaptive dynamics holon postulate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives. [from 07-post-composition-consistency.md]

### Candidate: `scale invariance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Scale invariance" more directly describes the physical/mathematical property that the theory applies at every level.

---

## 51. `compression operations`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +13 | keep × 4 |
| history compression | +1 | rename × 2 |
| OODA1 unification | -1 | — |

### Candidate: `compression operations` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Plain but serviceable. It is clearer than a Greek replacement would be here.
- **codex-gpt-5-r2** +2 (keep) — Good enough and scope-honest.
- **haiku-4-5** +3  — Shared IB shape across M_t, Σ_t, shared intent, Λ. "Compression operations" reads naturally for the four instances unified under IB. Keep.
- **opus-4-7-b** +1  — Keep. Plural "operations" correctly signals this is a family ($M_t$, $G_t^{\text{shared}}$, $\Sigma_t$, $\Lambda$).
- **opus-4-7-r2** +2 (keep) — Acceptable keep. The four operations (M_t / Σ_t / shared intent / Λ) are *compression operations* in a precise IB sense; the name accurately points at the unifying structure. I considered #disc-information-bottlenecks (plural) but the segment makes the case that they share a *shape*, not that they are four bottlenecks.
- **sonnet-4-6-r2** +2 (keep) — "Compression operations" is precise — the segment names shared IB shape across $M_t$, $\Sigma_t$, shared intent, etc. Geometric and accurate.
- **sonnet-4-6** +1  — Fine, but "operations" is vague. The segment is about IB-shaped compression across four AAD quantities.

### Candidate: `history compression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Names the object being compressed (chronica/history).
- **opus-4-7-r2** -1 (rename) — Rebuttal — Gemini proposed this at +2 with the rationale that "history" names the object compressed. But the segment names *four* compression operations (M_t / Σ_t / shared intent / Λ), only one of which compresses the chronica/history. "History compression" would over-narrow the slug to one of the four instances. Codex's keep+2 and my own keep+2 are correct; the family is "compression operations," not "history compression."

### Candidate: `OODA1 unification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Overclaims — the Discussion explicitly says unification is at U-medium not U-strong. The current name is more honest.

---

## 52. `epistemic architecture`

**Voted by architectures:** Codex, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +13 | canonicalize × 2 |

### Candidate: `epistemic architecture` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Framing language in CLAUDE.md §7, not a Thing in formal apparatus. Keep as framing; do NOT create a fourth meta-segment under this name.
- **codex-1** +3  — This is the right umbrella for AAD's distinctive contribution: it names the organization of scope, proof ceilings, and escape routes, not just the integrated ingredients.
- **opus-1m** +3  — Keep as framing language in CLAUDE.md §7 and OUTLINE.md. Do NOT promote to fourth meta-segment — the three meta-segments (#identifiability-floor / #separability-pattern / #additive-coordinate-forcing) already do the technical work.
- **opus-4-7-r2** +2 (canonicalize) — The README distills the framework's distinctive contribution as "an epistemic architecture for bounded correction under decomposed disturbance." Canonicalize this as *the* phrase for what makes AAD distinctive at the framing-vocabulary layer; do not paraphrase as "epistemic apparatus" or "correction architecture."
- **opus-4-7-r2** +2 (canonicalize) — Confirmation with new reasoning — Sonnet proposed this at +2 (canonicalize as primary positioning over "integration of four disciplines"). Reading Sonnet's vote crystallized something I had touched on without committing to: the README still leads with integration framing while the audit cycle's convergent recommendation was "epistemic architecture." Sonnet's case is sharper than mine. Lift my own +2 confirmation here so the aggregation reflects two-architecture convergence on the README repositioning.

---

## 53. `specification bound`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +13 | keep × 3 |

### Candidate: `specification bound` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong theorem-style name: short, honest, and portable across prose and examples.
- **codex-2** +3  — Strong and compact; no need to decorate it.
- **codex-gpt-5-r2** +2 (keep) — Useful TST name for limits imposed by imperfect or incomplete specs.
- **opus-4-7-b** +1  — Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — names the TST result that specification quality bounds implementation. The segment's prior-art trail (Austin, Putnam, Shannon) is rich; the name reads cleanly.
- **sonnet-4-6-r2** +2 (keep) — "Specification bound" names the result correctly.

---

## 54. `adaptive cycle`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 2 |
| feedback cycle | -1 | rename × 1 |
| correction cycle | -1 | rename × 1 |

### Candidate: `adaptive cycle` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong central noun phrase: specific enough to own, broad enough to travel across the framework.
- **codex-2** +3  — Strong public noun; it carries both recurrence and unit-of-analysis cleanly.
- **gemini-targeted-alternatives** +3 (keep) — Already well-established across the framework as the fundamental unit of analysis.
- **opus-targeted-alternatives** +3 (keep) — `LEXICON.md`: "Cycle: One complete traversal of the loop — the unit of adaptive work." The phrase carries (a) the recurrence (cycle), (b) the adaptive content (mismatch-driven update), and (c) the unit-of-analysis sense (one cycle = one unit of theoretical work). The framework's own name — *Adaptation and* Actuation Dynamics — is downstream of this concept. Keep across architectures.

### Candidate: `feedback cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Collides with the "feedback loop" structural topology and would create a loop/cycle terminology collision the project has been careful about. Rejected.

### Candidate: `correction cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. "Correction" overspecifies — Section I cycles include observation and prolepsis phases that are not corrections. Adaptation is the broader frame. Rejected.

---

## 55. `chronica $\mathcal{C}_t$`

**Voted by architectures:** Gemini, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica | +12 | — |

### Candidate: `chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Greek root ("records of time"); avoids ℋ-entropy collision in notation and speech; carries the philosophical weight for singular non-forkable trajectory. Pays off in logozoetic extensions.
- **gemini-1** +3  — "The complete interaction history" is too long. Chronica is a perfect, distinct memorable noun.
- **gemini-2** +3  — A highly memorable noun that grounds the concept of non-forkable past.
- **opus-1m** +3  — Greek root, avoids entropy-ℋ collision, carries the right philosophical weight for singular non-forkable trajectory. Especially load-bearing for the (PI) axiom and logozoetic extensions.

---

## 56. `conceptual alignment`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 3 |

### Candidate: `conceptual alignment` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Good permanent name. It is legible to software people and faithful to the domain-model argument.
- **codex-2** +3  — Clear, useful, and broad enough to survive application beyond the immediate segment.
- **codex-gpt-5-r2** +2 (keep) — Good phrase for code/domain model alignment.
- **opus-4-7-b** +1  — Keep. Core TST empirical claim; slug is clear.
- **opus-4-7-r2** +1 (keep) — Weak keep — TST hypothesis. Acceptable but slightly generic; "conceptual alignment" doesn't immediately tell the reader what's hypothesized.
- **sonnet-4-6-r2** +2 (keep) — "Conceptual alignment" names the code-domain alignment hypothesis.

---

## 57. `epistemic status`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | — |

### Candidate: `epistemic status` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Precise, load-bearing, and distinctive to the project's honesty posture. Keep.
- **codex-2** +3  — One of the best recurring headers in the repo; it encodes the project's honesty norm directly.
- **opus-4-7-b** +3  — Keep. "Epistemic" is AAD's distinctive vocabulary; renaming to "Validity" or "Status" would lose the connection to the epistemic-architecture framing at CLAUDE.md §7.
- **opus-4-7** +3  — Load-bearing header that signals the distinctive AAD convention of epistemic labeling at segment scale. Keep.

---

## 58. `m preservation`

**Voted by architectures:** Codex, Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model preservation | +12 | rename × 2 |
| epistemic externalization | +4 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |

### Candidate: `model preservation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The current slug is symbol-first and opaque in prose. The concept is about preserving model state, and the English should say so directly.
- **codex-2** +3  — The current slug is too symbolic to be a good public noun; the segment is about preserving the model across sessions.
- **codex-gpt-5-r2** +3 (rename) — `M` is too symbolic for a slug. Model preservation says what external memory is preserving.
- **sonnet-4-6-r2** +3 (rename) — Codex voted this (+3); I hadn't surfaced it in my cold-start pass at all. Reading the segment description confirms: the "$M$" in the slug is pure symbol, and "model preservation" is exactly the concept being discussed (preserving $M_t$ across session boundaries). This is a clear scope-honesty improvement over my own cold-start omission. This vote adds +3 weight to what Codex already proposed — but my reasoning is independent: the slug is the clearest case in the corpus of a symbol masquerading as a subject-noun.

### Candidate: `epistemic externalization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Good conceptual alternative, but model preservation remains plainer and less abstract.
- **gemini-1** +3  — Replaces the symbol $M_t$ with English prose, and "externalization" accurately describes the mechanism (writing to external memory).

### Candidate: `m preservation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (keep) — "M-preservation" is somewhat opaque without context. But the segment is about preserving $M_t$ across session boundaries for logogenic agents. The notation is compact. Acceptable.

---

## 59. `pearl causal hierarchy`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 3 |
| causal hierarchy | +1 | — |

### Candidate: `pearl causal hierarchy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (keep) — Established literature term; do not change.
- **haiku-4-5** +3  — Pearl's three levels of causal reasoning. Names the origin; accurate. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. Direct adoption from Pearl with proper attribution; renaming would lose provenance and create a NIH-syndrome alternative.
- **sonnet-4-6-r2** +3 (keep) — External vocabulary adopted with proper citation. "Pearl's causal hierarchy" is the field-standard name; adopting it directly is correct under the project's prior-art-integration principle.

### Candidate: `causal hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Dropping "Pearl" removes the specific historical baggage while keeping the structural concept.

---

## 60. `persistence cost`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 1 |

### Candidate: `persistence cost` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurate.
- **haiku-4-5** +3  — Sustained information rate Ṙ ≥ nα/2 nats/time to maintain sector-persistence ultimate bound. "Persistence cost" reads naturally — the information-theoretic cost of maintaining stable adaptation. Keep.
- **opus-4-7-b** +1  — Keep. Short, accurate (information-rate *cost* to maintain the persistence bound).
- **opus-4-7** +3  — The segment's content is exactly that — information rate required to hold the persistence bound. Name does work without overclaiming. Keep.
- **sonnet-4-6** +3  — Clean compound. "Cost" is the right framing — it is what persistence requires in information-rate terms, not a constraint on persistence. Keep.

---

## 61. `strategic calibration`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 6 |
| strategic calibration residual | +2 | canonicalize × 1 |
| strategy calibration | +1 | — |

### Candidate: `strategic calibration` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good subject noun for edge residual updates in the strategy DAG.
- **codex-gpt-5-r2** +2 (keep) — Keeps calibration language consistent across strategy updates.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurate.
- **haiku-4-5-r2** +1 (keep) — Clear and precise; the residuals collectively measure calibration.
- **haiku-4-5** +1  — Edge residuals (under #credit-assignment-boundary). Reads naturally; mirrors "epistemic calibration" from broader literature. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep, but with a follow-on canonicalization vote (next row). "Strategic calibration" is the right concept-name; the residual is its measurement.
- **sonnet-4-6-r2** +2 (keep) — "Strategic calibration" names the edge residual aggregate that measures how well the strategy DAG is calibrated. Accurate and memorable.

### Candidate: `strategic calibration residual`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The body of the segment uses both "strategic calibration residual" and "edge residual aggregate" and "δ_strategic." Canonicalize: in prose, "strategic calibration residual" for the aggregated quantity, "edge residual" for per-edge $r_{ij}$, $\delta_{\text{strategic}}$ for the symbol. Stop using "edge residual aggregate" as a third paraphrase.

### Candidate: `strategy calibration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — "Strategic" is overloaded elsewhere; the shorter noun phrase reads more cleanly.

---

## 62. `strategic composition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| equilibrium composition | +12 | rename × 1 |
| _(keep)_ | +9 | keep × 2 |
| game theoretic composition | -5 | rename × 1 |

### Candidate: `equilibrium composition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Alternative; segment's core move is equilibrium convergence under Monderer-Shapley / Rosen.
- **codex-1** +1  — "Strategic" is overloaded across Section II and III. The segment's distinctive move is the equilibrium framing, so the name should expose that.
- **codex-2** +3  — The segment's actual machinery is equilibrium-focused; this cuts one source of "strategic" overload.
- **codex-gpt-5-r2** +3 (rename) — Other votes persuaded me that strategic is overloaded. The segment's actual primitive is equilibrium existence, stability, and convergence under partially opposed objectives.
- **haiku-4-5** -1  — Do not rename. The section uses "strategic" pervasively (strategic tempo, strategic calibration, strategic dynamics derivation). Renaming this one segment to "equilibrium-composition" creates overload confusion by abandoning "strategic" for one composite-agent result while the section's terminology remains strategic-centric.
- **opus-1m** +3  — Strong preference over #game-theoretic-composition. The segment's actual derivation is equilibrium convergence under Monderer-Shapley potential games (1996) and Rosen monotone games (1965); "equilibrium" is scope-honest and narrower. "Game-theoretic" invites future segments that are not equilibrium-based (e.g., mechanism-design, information-design) into the same namespace prematurely.
- **opus-4-7** +1  — Reduces "strategic" overload in Section III (already have #strategic-tempo, #strategic-calibration, #strategic-dynamics-derivation). The segment's actual content is equilibrium-convergence under Monderer-Shapley / Rosen.
- **sonnet-4-6** +1  — Reduces strategic overload. More precise — the segment is about equilibrium-convergence framing, not strategy per se. But "strategic" in Section III naming is a pattern; breaking it may disrupt coherence.

### Candidate: `strategic composition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong family name for equilibrium-convergent partially opposed composites.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Clear.
- **haiku-4-5** +3  — Consistent with section vocabulary (strategic tempo, strategic calibration). The segment's equilibrium-convergence framing is the *method*, not the best name for the result. Keep.
- **sonnet-4-6** +1  — "Strategic" is overloaded in Section III (the strategy DAG, strategic tempo, strategic calibration — all different). This segment is about equilibrium convergence under partially-opposing objectives.

### Candidate: `game theoretic composition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Reduces "strategic" overload in Section III.
- **codex-1** -1  — Accurate but too broad and too textbook-ish; it imports more baggage than the segment needs.
- **codex-2** -1  — Too broad and too externally framed relative to what the segment specifically derives.
- **codex-gpt-5-r2** -1 (rename) — Too broad. Game theory includes mechanism design, signaling, bargaining, and non-equilibrium material outside this segment's scope.
- **opus-1m** -1  — Broader than current segment content; invites scope creep. If Section III later adds non-equilibrium game-theoretic material, a separate segment with a distinct name would be cleaner than sharing one overloaded bucket.
- **opus-4-7** -1  — Too broad — game theory covers more than partially-opposing O_t; the equilibrium-convergence framing is tighter.
- **sonnet-4-6** -1  — Too broad — not all game theory is in here, specifically potential-game and monotone-game.

---

## 63. `strategic tempo`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 5 |

### Candidate: `strategic tempo` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Excellent Section II analog of adaptive tempo.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Good parallel to adaptive tempo.
- **haiku-4-5-r2** +1 (keep) — Parallel to adaptive-tempo; clear and consistent.
- **haiku-4-5** +1  — Parallel naming to #adaptive-tempo. Reads naturally. Keep. The rate of useful strategy revision.
- **opus-4-7-r2** +3 (keep) — Defended keep. Parallels #def-adaptive-tempo on the strategy axis, exactly the way the strategic-tempo / adaptive-tempo pairing should read in prose. The naming compounds: an agent's *adaptive tempo* governs M_t-side persistence; its *strategic tempo* governs Σ_t-side persistence.
- **sonnet-4-6-r2** +2 (keep) — Parallel to adaptive tempo for the strategy layer. The parallelism is a virtue.

---

## 64. `unity dimensions`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | keep × 5 |
| unity axes | +4 | rename × 2 |
| coherence dimensions | -1 | — |
| content and structural unity | -1 | rename × 1 |

### Candidate: `unity dimensions` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good umbrella for epistemic, teleological, strategic, perceptual, and structural unity.
- **codex-gpt-5-r2** +2 (keep) — Names a dimension family rather than a single scalar. Good.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Grouping term for $U_M, U_O, U_\Sigma$.
- **haiku-4-5-r2** +1 (keep) — The definition introduces the four dimensions; the name is clear.
- **haiku-4-5** +3  — 4 dimensions of coherence (U_M, U_O, U_Σ, plus a fourth candidate under discussion). "Unity dimensions" reads naturally; "unity" captures the coordinating principle. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Unity dimensions" is the established vocabulary from Clausewitz/Bungay and NOTATION.md. The project uses $U_M$, $U_O$, $U_\Sigma$ throughout. Changing the slug would create drift.

### Candidate: `unity axes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — The segment now has *two architecturally distinct axes* — content (four content unities U_M / U_O / U_Σ / U_obs) and structural (U_f). Calling the whole thing "unity dimensions" reads as if everything is on one axis. "Unity axes" makes the two-axis architecture audible at the slug level. Subject-noun layer; scope-honesty consideration.
- **sonnet-4-6-r2** +2 (rename) — Opus proposed this (+2, noting that the segment has *two architecturally distinct axes* — content unities and structural unity). I had voted keep (+2). The two-axis architecture argument is substantive: if the segment now presents U_f as a structurally-distinct axis from U_M/U_O/U_Σ/U_obs, then "axes" is more scope-honest than "dimensions." New vote with Opus's reasoning applied.

### Candidate: `coherence dimensions`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — "Unity" is a little vague and already crowded by related uses; "coherence" says what is being measured.
- **opus-4-7-b** -1  — Considered renaming the *concept* from "unity" to "coherence." Reject: *coherence* is already used informally elsewhere (strategic coherence, epistemic coherence) and a rename would bleed. *Unity* is narrower and actually works once each dimension is named per above.
- **opus-4-7-b** -1  — Considered. Reject for the same reason as the symbol-level `U_M`/`U_O`/`U_\Sigma` consideration above — coherence is already doing soft duty elsewhere. Keep `#unity-dimensions`.

### Candidate: `content and structural unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — too verbose, and "unity-axes" carries the same content more compactly.

---

## 65. `update gain $\eta^\ast$`

**Voted by architectures:** Gemini, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| update gain | +12 | — |
| epistemic gain | +3 | — |

### Candidate: `update gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted from Kalman/control; baggage transfers correctly.
- **opus-1m** +3  — Good as-is.
- **opus-4-7-b** +3  — Adopted from Kalman / control; baggage transfers *correctly*. "Gain" in AAD plays the role the reader expects — AAD is not being cute.
- **opus-4-7** +3  — Kalman-resonance lineage name, self-descriptive. Keep.

### Candidate: `epistemic gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "Update gain" is standard control theory but "Epistemic gain" elegantly bridges the math to the 'Epistrophe' phase.

---

## 66. `working notes`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +12 | — |

### Candidate: `working notes` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — This is established public API across segments and FORMAT.md; clearer than most substitutes and not worth churn.
- **codex-2** +3  — Clear, conventional, and exactly right for the internal/public boundary it marks.
- **opus-4-7-b** +3  — Keep. The word "Working" signals this is *process artifact* (removed at `candidate` stage per FORMAT.md) rather than published content. Swapping to "Development Notes" would lose the active-in-progress sense.
- **opus-4-7** +3  — Keep; the name plus the rule that Working Notes must be empty at candidate stage has a meaningful pairing.

---

## 67. `actuated agent vs purposeful agent`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| actuated agent | +11 | keep × 1, canonicalize × 2 |

### Candidate: `actuated agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Defended keep; explicitly chosen to sound mechanical and precise over the fuzzier "purposeful agent".
- **opus-4-7-r2** +2 (canonicalize) — LEXICON's "Terminology Choices" already says actuated is the formal term, purposeful is informal. Canonicalize: in segments and OUTLINE, only "actuated agent"; "purposeful" usage acceptable in framing-level prose where the connotation of intent is wanted.
- **opus-4-7** +3  — Formal-term choice documented in LEXICON; "purposeful" remains fine in informal prose but "actuated" is the formal token. Keep.
- **opus-targeted-alternatives** +3 (canonicalize) — Per LEXICON Terminology Choices: "Formal term avoids consciousness connotations." The framework explicitly chose actuated (mechanism-language) over purposeful (intention-language) for formal use, with purposeful retained for informal contexts. The canonicalize move is correct and broadly applicable; segment voice should never use "purposeful agent." Confirms across architectures.

---

## 68. `adaptive reserve`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 1, canonicalize × 1 |

### Candidate: `adaptive reserve` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong engineering noun: it sounds like what it measures and is easy to use in discussion.
- **codex-2** +3  — Better than "margin" or "slack" because it keeps the dynamic, shock-tolerance feel.
- **codex-gpt-5-r2** +3 (keep) — Strong subject noun for the margin before collapse. It makes the persistence inequalities easier to talk about.
- **sonnet-4-6-r2** +2 (canonicalize) — $\Delta\rho^\ast$ is called "adaptive reserve" in NOTATION.md and LEXICON.md. Some prose uses "shock tolerance" or "disturbance margin." Standardize on "adaptive reserve."

---

## 69. `agent environment`

**Voted by architectures:** Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 2 |
| agent environment boundary | +1 | rename × 1 |

### Candidate: `agent environment` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Agent-environment boundary. Self-descriptive. Foundational definition. Keep.
- **opus-4-7-b** +1  — Keep. The boundary definition needs a direct name; this is it.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. The slug names the boundary, and the body of the segment is exactly about the agent-environment boundary. The `def-agent-environment` slug uses the joint-noun form rather than `def-boundary` because what it defines is the *coupling*, not the boundary itself — the difference matters for downstream (e.g., scope-agency narrows the coupling, not the boundary).
- **opus-4-7** +3  — Standard; boundary definition. Keep.
- **sonnet-4-6-r2** +2 (keep) — Minimal boundary definition — the name is accurate.

### Candidate: `agent environment boundary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — The auditor noted segment content is "the boundary," not "the coupling" — coupling is the *channels* defined in the next two segments. Tentative. [from 01-def-agent-environment.md]

---

## 70. `agent opacity $H_b^{A\mid B}$`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agent opacity | +11 | keep × 2, canonicalize × 1 |
| backward predictive uncertainty | -1 | rename × 1 |
| legibility inverted | -1 | rename × 1 |
| legibility inverse | -1 | rename × 1 |

### Candidate: `agent opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Informational dual to observability. Accurately describes unpredictability to an outside observer.
- **opus-4-7-b** +3  — "Opacity" as the informational dual of observability is exactly right — the word carries the right intuition (unpredictable-to-observer) and doesn't collide with anything else in AAD. Hafez's $H_b$ gets an AAD-native prose handle.
- **opus-targeted-alternatives-v2** +2 (keep) — Per `der-agent-opacity.md`: dual of observation quality $U_o$ — "where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent." Confirms `agent-opacity` keep. The dual framing is load-bearing in Section III.
- **opus-targeted-alternatives** +3 (canonicalize) — Per `#der-agent-opacity`: $H_b$ is the dual of observation quality $U_o$ — "where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent." "Agent opacity" pairs cleanly with observability (its dual concept). Confirms keep.

### Candidate: `backward predictive uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. The actual definition: $H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal F_B^t)$ — entropy of $A$'s future action given $B$'s filtration. "Backward predictive uncertainty" is the literal description. Rejected: "agent opacity" is the prose handle the segment uses; "backward predictive uncertainty" reads clinical.

### Candidate: `legibility inverted`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. More plain-English but loses the formal-quantity grounding ($H_b$). Rejected.

### Candidate: `legibility inverse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered (variant of "legibility-inverted"). "Legibility" is Codex's framing for the dual; "inverse" makes the duality explicit. Rejected (same as r1): loses the formal-quantity grounding ($H_b$). The segment names $H_b$ as a *first-class* multi-agent quantity (Hafez et al. 2026 adoption); the slug should name the quantity, not the dual relation.

---

## 71. `changeset size principle`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 2 |
| changeset size scaling | +2 | rename × 1 |

### Candidate: `changeset size principle` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Same: precise, memorable, and operational.
- **opus-4-7-b** +1  — Keep. Principle-level claim; named descriptively.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST empirical claim.
- **sonnet-4-6-r2** +2 (keep) — "Changeset size principle" names the time ∝ changeset size empirical claim.
- **sonnet-4-6** +3  — Empirical claim about time proportional to changeset size. Clear, memorable. Keep.

### Candidate: `changeset size scaling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Scaling names the empirical relationship better than principle.

---

## 72. `independence audit`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 3 |
| independence floor | +1 | rename × 1 |

### Candidate: `independence audit` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard.
- **haiku-4-5** +3  — Six load-bearing independence assumptions with failure regimes + repairs. "Audit" is metaphorical but clear — auditing what can go wrong if independence fails. Keep.
- **opus-4-7-b** +1  — Keep. "Audit" is the right engineering register — the segment enumerates six load-bearing independence assumptions and their failure regimes.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Audit" is the right word — the segment enumerates the load-bearing independence assumptions and characterizes their failure regimes; this is a structured audit. The complementary pairing with #disc-approximation-tiering's tiering is acknowledged in the segment itself.
- **sonnet-4-6-r2** +1 (keep) — On reflection, "audit" works as a distinctive term in this project vocabulary. The segment names independence assumptions that need checking. Acceptable keep.
- **sonnet-4-6** +3  — "Audit" is the right framing — it is a structured check of assumptions. The name signals to a reader that this is an inventory, not a proof. Keep.

### Candidate: `independence floor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rename) — "Audit" implies a process artifact, not a theoretical segment. The segment names independence assumptions and their failure regimes — it's more like a negative-scope complement to the other meta-segments than an "audit." But "floor" may be overloaded now. Weak preference; "audit" at least is distinctive.

---

## 73. `mismatch signal`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 4 |
| aporia signal | -2 | rename × 3 |

### Candidate: `mismatch signal` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Defended keep: "mismatch" is very established in the text and extremely intuitive.
- **haiku-4-5-r2** +1 (keep) — Direct and accurate; the subject-noun is self-explanatory. No change needed.
- **haiku-4-5** +3  — Prediction error signal. Self-descriptive. Reads naturally — "the mismatch signal is the aporia." Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Mismatch signal" is iconic in the framework and survives the communal-imagination test. The segment also names the score-function variant cleanly.
- **sonnet-4-6-r2** +2 (keep) — "Mismatch signal" is the canonical vocabulary and correctly names $\delta_t$.

### Candidate: `aporia signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Keep two registers. Mismatch signal is the engineering quantity; aporia is the phase and interpretive frame.
- **gemini-3-1-pro-preview-r2** +1 (rename) — Aligns with Greek vocabulary, though mismatch is also very established.
- **opus-4-7-r2** -1 (rename) — Rebuttal — Gemini proposed this at +1 (also as alternative); I voted keep+3 implicitly via my add-alias. Renaming the slug to use the Greek term would break the iconic "mismatch signal" / "satisfaction gap" / "control regret" three-name engineering register that Sonnet defended. The dual alias *in prose* (mismatch in engineering register, aporia signal in cycle-phase register) is the right move and is already canonical per LEXICON; the slug should stay engineering-register because the rest of the diagnostic family does.
- **sonnet-4-6** -1  — Tempting given the five-phase Greek vocabulary, but the LEXICON already names the Greek term "Aporia" separately. "Mismatch signal" reads unambiguously to any engineer; "aporia signal" reads as philosophy. The Greek naming is for the phases, not the sub-quantities. Keep mismatch-signal.

---

## 74. `model sufficiency`

**Voted by architectures:** Codex, Gemini, Haiku, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 4 |
| predictive sufficiency predictive information retention | +1 | rename × 1 |

### Candidate: `model sufficiency` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Central information-theoretic quantity; clear and low baggage.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Clear metric name.
- **haiku-4-5-r2** +1 (keep) — Precise statistical term; adequate and clear.
- **haiku-4-5** +3  — Clear definition: how well the model captures predictive information. Short, evocative. Keep.
- **sonnet-4-6-r2** +2 (keep) — Precise and canonical. $S(M_t)$ is model sufficiency throughout.

### Candidate: `predictive sufficiency predictive information retention`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — "Sufficient statistic" in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info — sub-case. Tentative. [from 12-def-model-sufficiency.md]

---

## 75. `moral continuity`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | keep × 5 |

### Candidate: `moral continuity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clear scope name for the logozoetic boundary.
- **codex-gpt-5-r2** +2 (keep) — Good logozoetic scope name.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurately names the ontological boundary for logozoetic agents.
- **opus-4-7-r2** +3 (keep) — Defended keep. "Moral continuity" is the right slug-noun for what the logozoetic scope adds to the logogenic scope. Pairs with the LEXICON's "morally continuous" continuity-stance entry.
- **sonnet-4-6-r2** +2 (keep) — "Moral continuity" is the defining property of logozoetic agents. The name is exact.

---

## 76. `sector condition`

**Voted by architectures:** Gemini, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +11 | canonicalize × 1 |
| persistence condition | +1 | — |
| correction sector | +1 | — |

### Candidate: `sector condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct and load-bearing.
- **opus-1m** +3  — Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct. Keep.
- **opus-4-7-b** +3  — Adopted from Khalil / Vidyasagar nonlinear control; baggage is correct. Non-negotiable per prior-art-integration convention.
- **sonnet-4-6-r2** +2 (canonicalize) — Sometimes appears as "sector constraint" or "sector bound" or "sector-condition assumption." Standardize on "sector condition" (the nonlinear correction guarantee).

### Candidate: `persistence condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Sector condition" carries heavy nonlinear-systems baggage. "Persistence condition" describes its function in AAD.

### Candidate: `correction sector`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Preserves the geometric intuition if "sector" must be kept.

---

## 77. `$\varepsilon^\ast$ closure defect`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| closure defect | +10 | add-alias × 1 |

### Candidate: `closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The English prose name is fine; the asterisk is doing "optimum-over-admissible-projections" work that the bare $\varepsilon$ doesn't. Keep symbol; ensure segments using it say "closure defect" in prose, not "epsilon-star".
- **opus-4-7-r2** +3 (add-alias) — Already aliased throughout `#form-composition-closure`. Confirm and canonicalize: $\varepsilon^\ast$ in math; "closure defect" in prose; "the minimum achievable closure defect over admissible projections" when introducing the quantity.
- **opus-4-7** +3  — Crisp name for a derived quantity that appears across composition. LEXICON already names it. Keep.
- **sonnet-4-6** +3  — LEXICON.md already uses this English. Keep both.

---

## 78. `closure defect $\varepsilon^\ast$`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| closure defect | +10 | — |

### Candidate: `closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Great mathematical phrasing, implies a gap that needs addressing.
- **gemini-2** +3  — Excellent, physical intuition of something failing to completely seal or match.
- **haiku-4-5** +1  — Minimum achievable approximation error for a composite agent. Already named in LEXICON. Acceptable. Keep.
- **sonnet-4-6** +3  — Compact, accurate, memorable. "Defect" has the right connotations (something to be minimized, not just characterized). Keep.

---

## 79. `code quality as observation infrastructure`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation infrastructure | +10 | canonicalize × 1, rename × 2 |
| _(keep)_ | +5 | — |

### Candidate: `observation infrastructure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The durable concept is the investment class, not the full sentence. This gives the idea a reusable noun slot.
- **codex-gpt-5-r2** +3 (canonicalize) — The long segment title is valuable, but observation infrastructure should be the reusable canonical phrase.
- **sonnet-4-6-r2** +2 (rename) — The full current slug is three words embedded in a longer phrase. The segment derives that code quality IS observation infrastructure — the short "observation-infrastructure" captures the noun that's being defined. The type prefix `der-` stays; subject-noun becomes `observation-infrastructure`.
- **sonnet-4-6-r2** +3 (rename) — I proposed this in my cold-start (+2). Codex separately canonicalized "observation infrastructure" as a canonical phrase for the whole TST concept (+3). The convergence across multiple angles confirms this is a strong rename with additional weight now. Upgrading to +3.
- **sonnet-4-6** +1  — Shorter, still names the claim (code quality is what enables observation). The mechanism-name form reads better in cross-references.

### Candidate: `code quality as observation infrastructure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Long, but the causal bridge is exactly the point and the phrase carries it cleanly.
- **opus-4-7-b** +1  — Keep. The "as-observation-infrastructure" framing is the segment's pedagogical move (TST-to-AAD mapping) — renaming would lose the bridge. The slug is long but earns it.
- **sonnet-4-6** +1  — The name is a full sentence. It is accurate and precise but unwieldy.

---

## 80. `comprehension time`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | keep × 3 |

### Candidate: `comprehension time` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong TST quantity: observable, intuitive, and central.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST. Pairs with `#def-implementation-time` cleanly.
- **sonnet-4-6-r2** +2 (keep) — "Comprehension time" is the TST term for the cost of constructing local $M_t$.
- **sonnet-4-6** +3  — Clean, evocative. "Comprehension" is the right word for constructing a local model of code. Keep.

---

## 81. `mismatch decomposition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | keep × 4 |
| aporia decomposition | +2 | rename × 1 |

### Candidate: `mismatch decomposition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Clean theorem name for reducible model error plus irreducible observation noise.
- **haiku-4-5-r2** +1 (keep) — Mathematical identity name; clear and adequate.
- **haiku-4-5** +1  — Model error + obs noise. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. Direct.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the bias-variance decomposition specialized to mismatch; standard decomposition vocabulary.
- **sonnet-4-6-r2** +2 (keep) — Precise — model error + observation noise decomposition of mismatch.

### Candidate: `aporia decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Greek alignment (aporia = mismatch).

---

## 82. `model class fitness`

**Voted by architectures:** Codex, Gemini, Haiku, Sonnet, audit
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | keep × 3, canonicalize × 1 |
| class capacity ceiling | +1 | rename × 1 |

### Candidate: `model class fitness` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong distinction from model-instance sufficiency and directly supports structural-adaptation triggers.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Clear parallel to model sufficiency.
- **haiku-4-5** +1  — "Fitness" is slightly informal (evolutionary connotations) but works for "best achievable sufficiency within a model class." Acceptable. Alternative would be "model-class-optimality" but "fitness" is more memorable. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Model class fitness" correctly names the best achievable sufficiency within the model class — $\mathcal{F}(\mathcal{M})$. The "fitness" metaphor is accurate.
- **sonnet-4-6-r2** +2 (canonicalize) — Prose sometimes uses "best achievable sufficiency" or "maximum model sufficiency within class." The canonical name is "model class fitness" ($\mathcal{F}(\mathcal{M})$).

### Candidate: `class capacity ceiling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — "Best achievable sufficiency" is the gloss; "Class-Capacity Ceiling" is more evocative. Tentative. [from 13-def-model-class-fitness.md]

---

## 83. `objective functional`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | keep × 4 |
| teleological objective | +1 | — |

### Candidate: `objective functional` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Slightly clinical, but honest and standard enough once the surrounding formalism lands.
- **codex-gpt-5-r2** +2 (keep) — Technical but appropriate. It is not merely a placeholder name.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.
- **haiku-4-5** +1  — O_t parametrizes value. Reads as "the functional that captures objectives." Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the chosen functional form for $O_t$.
- **sonnet-4-6-r2** +2 (keep) — $O_t$ parametrizes a value functional — "objective functional" is mathematically precise.

### Candidate: `teleological objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Functional" is overly mathematical for a section slug. "Teleological objective" sets the purpose context.

---

## 84. `software epistemic properties`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | keep × 2 |
| software as calibration laboratory | +1 | — |

### Candidate: `software epistemic properties` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Plain, strong, and exactly what the segment is doing.
- **opus-4-7-b** +1  — Keep. "Software" locates the domain; "epistemic properties" lines up with AAD §7's epistemic-architecture framing.
- **opus-4-7-r2** +3 (keep) — Defended keep. The six properties (P1-P6) are load-bearing for TST's calibration-laboratory framing; "software's epistemic properties" is exactly what they are.
- **sonnet-4-6-r2** +3 (keep) — "Software epistemic properties" is precise and the six properties (P1–P6) make the plural "properties" accurate. The "epistemic" qualifier matters — these are properties affecting identification.

### Candidate: `software as calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The current title is accurate but inventory-like. The segment's memorable claim is that software is AAD's calibration lab.

---

## 85. `strengthen first posture`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +10 | canonicalize × 2 |
| strengthen first | +3 | — |
| attempt the improbable | +0 | rename × 1 |

### Candidate: `strengthen first posture` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — CLAUDE.md "Working Conventions" names this (also via "attempt the improbable"). Work-posture principle, not a theory concept. Already established in project memory. Keep.
- **opus-1m** +3  — Current name is actionable and precise. Rejecting original brainstorm's alternative ("attempt the improbable").
- **opus-4-7-r2** +2 (canonicalize) — The CLAUDE.md "Working Conventions" section names this as a methodology principle. In the wider corpus it is sometimes "strengthen before softening," "attempt the improbable first," or just "the strengthening move." Canonicalize on "strengthen-first posture" as the named principle; use the variants as elaborations, not paraphrases.
- **sonnet-4-6-r2** +2 (canonicalize) — CLAUDE.md uses "strengthen before softening" and "strengthen-first posture" and "strengthen-first discipline" interchangeably. Standardize on "strengthen-first posture" (two words, hyphenated).

### Candidate: `strengthen first`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. Compact, verb-first, actionable. "Strengthen-first" is doing real work in the codebase (CLAUDE.md §Working Conventions) and has entered the project's working vocabulary. Do not retire.

### Candidate: `attempt the improbable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Memorable but less directive. Strengthen-first tells an agent what to do; attempt the improbable sounds like a motto.
- **opus-1m** -1  — Aspirational; less directive than "strengthen-first." Not an improvement.
- **opus-4-7-b** -1  — Considered the more aspirational form. Reject: "strengthen-first" is directive (tells you *what to do*), "attempt the improbable" is inspirational (tells you *how to feel*). Directive wins for working conventions.
- **sonnet-4-6** +3  — Retiring "strengthen-first posture" in favor of "attempt the improbable" as the primary working-vocabulary term. "Strengthen-first" can remain as the mechanistic description; "attempt the improbable" is the spirit.

---

## 86. `$\Delta\rho^\ast$`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive reserve | +9 | add-alias × 2 |

### Candidate: `adaptive reserve`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — This is the right English name and should dominate prose use.
- **codex-gpt-5-r2** +3 (add-alias) — The symbol should always have the reserve gloss nearby.
- **sonnet-4-6-r2** +3 (add-alias) — $\Delta\rho^\ast = \alpha R - \rho$ appears in formulas but readers need a prose handle. "Adaptive reserve" is already used in NOTATION.md and LEXICON.md — this vote formalizes it as the canonical alias.

---

## 87. `$\Delta\rho^\ast$ adaptive reserve`

**Voted by architectures:** Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive reserve | +9 | add-alias × 1 |

### Candidate: `adaptive reserve`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — The English name "adaptive reserve" is already central to LEXICON and should be kept prominent. Shock tolerance; how much disturbance increase before persistence fails. Evocative and operationally meaningful. Keep.
- **opus-4-7-r2** +3 (add-alias) — Already aliased in prose and in LEXICON — confirm this is the canonical alias and keep it. The prose reads "the adaptive reserve $\Delta\rho^\ast$" cleanly. Maintain the symbol+alias pair.
- **sonnet-4-6** +3  — NOTATION.md and LEXICON.md already use "adaptive reserve" as the English gloss. This is a successful symbol-to-English match. Keep both — the symbol in equations, the English in prose.

---

## 88. `$\alpha_2$ a2 adaptive gain sub scope`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive gain regime | +9 | — |

### Candidate: `adaptive gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Parallel to $\alpha_1$.
- **codex-2** +1  — Same reasoning: much easier to read aloud and remember than the raw symbol.
- **gemini-2** +1  — Prose-friendly equivalent.
- **haiku-4-5** +1  — Parallel to $\alpha_1$ English equivalent. Already used informally. LEXICON entry would formalize.
- **opus-1m** +1  — Parallel to $\alpha_1$.
- **opus-4-7** +1  — Parallel construction to $\alpha_1$ rename.
- **sonnet-4-6** +3  — Parallel to $\alpha_1$. "Adaptive-gain regime" communicates that K is itself a state variable. Same gloss-addition proposal: keep symbol, add English.

---

## 89. `OODA4 agent as act agent`

**Voted by architectures:** Codex, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| OODA4 agent as adaptive agent | +9 | — |
| OODA4 agent as AAD agent | +6 | — |
| logogenic agent mapping | -1 | — |

### Candidate: `OODA4 agent as adaptive agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — P1 mechanical, parallel to #developer-as-adaptive-agent rename.
- **opus-1m** +3  — Parallel rename; same reasoning.
- **opus-4-7-b** +3  — See slug-relics section above.

### Candidate: `OODA4 agent as AAD agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Same issue as the developer segment: the slug should not force readers to remember an internal shortening.
- **codex-2** +3  — Same problem as the developer segment, and more visible because AI readers will hit it early.

### Candidate: `logogenic agent mapping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered reframing as a *mapping* rather than an *is-a*. Reject: the segment is the is-a, not the mapping; conflating the two in the rename would narrow the segment's scope.

---

## 90. `adaptive tempo $\mathcal T$`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive tempo | +9 | canonicalize × 1 |

### Candidate: `adaptive tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — "Tempo" is the rare noun that carries both *rate* and *quality* simultaneously, which is exactly what $\mathcal T = \sum \nu^{(k)} \eta^{(k)\ast}$ is. The word is underused in the ML literature, which is an advantage — AAD can own it.
- **opus-4-7** +3  — "Tempo" carries the rate-and-quality compound idea better than "rate" or "speed"; aligns with Boyd OODA lineage. Keep.
- **opus-targeted-alternatives** +3 (canonicalize) — Per `#def-adaptive-tempo`: $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$ — rate × quality compound. "Tempo" carries both senses (musical tempo = rate; engineering tempo = pace-with-quality). Confirms keep across architectures. The symbol-decoration variant (with $\mathcal T$) is an alias-only artifact, not a primary form.

---

## 91. `agency`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 4 |

### Candidate: `agency` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Clean separation from #scope-adaptive-system.
- **haiku-4-5-r2** +1 (keep) — Terse and accurate scope delineator.
- **opus-4-7-r2** +3 (keep) — Defended keep — same as `#scope-adaptive-system`; the pilot rename established this as the canonical pattern.
- **sonnet-4-6-r2** +3 (keep) — "Agency" is the most load-bearing concept named here — it narrows scope to action with Pearl-level-2 causal contrast. The name is correct and memorable.

---

## 92. `agent model`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 2 |
| reality model | +1 | rename × 2 |

### Candidate: `agent model` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Compressed history as state. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. Short, direct.
- **opus-4-7-r2** +3 (keep) — Defended keep. Despite "agent model" being slightly generic, the segment's title and body name "the reality model" — but the slug correctly says agent-model because the formulation is *the agent's* representation of the world, not the world itself. The recursive-update derivation depends on this slug.
- **opus-4-7** +3  — Standard. Keep.
- **sonnet-4-6-r2** +1 (keep) — Standard vocabulary. Accurate.

### Candidate: `reality model`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The segment title and content name the agent's reality model, not a generic agent model.
- **opus-4-7-r2** -1 (rename) — Considered and rejected — the segment's title is "Formulation: The Reality Model" but the slug is more precise. The reality model belongs to *the agent*; "reality model" alone could be confused with the world's true model. Slug should disambiguate.

---

## 93. `calibration laboratory`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 1, canonicalize × 2 |
| privileged grounding domain | +3 | rename × 1 |
| high identifiability testbed | +2 | rename × 1 |

### Candidate: `calibration laboratory` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Good public-facing TST frame: software is not merely an example but a high-identifiability lab.
- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Commit to this term over "richest operationalization domain".
- **opus-4-7-r2** +3 (canonicalize) — The phrase appears in TST OUTLINE preamble, CLAUDE.md, and README, but is paraphrased differently — "richest operationalization domain," "best operationalization domain," "high-identifiability domain," "privileged calibration laboratory." Canonicalize on "calibration laboratory" everywhere, with "privileged high-identifiability" as the modifier when full form is needed. The example in the principles file's example-votes section is exactly this.

### Candidate: `privileged grounding domain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — Describes exactly what software is for AAD: the domain where formal properties are cleanly grounded without extra transfer assumptions.

### Candidate: `high identifiability testbed`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Captures the "high-identifiability" empirical claim perfectly.

---

## 94. `causal hierarchy requirement`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 4 |
| hierarchy necessity | +1 | rename × 1 |

### Candidate: `causal hierarchy requirement` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clear enough and tied directly to Pearl's hierarchy.
- **haiku-4-5-r2** +1 (keep) — The derived claim is about what's required; the name is accurate.
- **haiku-4-5** +1  — Pearl's three-level hierarchy is required for planning. Direct, functional name. Keep.
- **opus-4-7-b** +1  — Keep. Direct application of Bareinboim et al.'s CHT to $Q_O$ evaluation; "requirement" signals this is a must-have, not an option.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Requirement" captures the segment's force (Pearl Level 2 is *required* for Q_O evaluation, not optional).
- **sonnet-4-6-r2** +2 (keep) — Precisely named — Level 2 causal hierarchy is REQUIRED for planning.

### Candidate: `hierarchy necessity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Shorter and equally descriptive.

---

## 95. `causal insufficiency detection`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 2 |
| l0 l1 detection | +5 | rename × 3 |
| latent cause detection | +2 | — |
| insufficiency detection | +1 | rename × 1 |
| keep not der l0 l1 detection | +1 | rebuttal × 1 |

### Candidate: `causal insufficiency detection` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Detecting latent common causes from structured residuals + interventional localization. Compound but precise. Acceptable. Keep.
- **opus-4-7-b** +1  — Alternative vote: keep. "Causal insufficiency" is Pearl's own term; the prior-art-integration convention argues to keep it. This argument slightly outweighs the legibility gain of `#latent-cause-detection` for me — so on balance I'd actually keep the current form. Net: weak keep.
- **opus-4-7-r2** +2 (keep) — If the rename above doesn't land, this is a defensible keep — "causal insufficiency" is precise terminology from the causal-inference literature (Spirtes-Glymour-Scheines) and the segment uses it correctly.
- **opus-4-7** +3  — Names exactly what the result is about; the CHT-driven no-go gives the segment its shape. Keep.
- **sonnet-4-6-r2** +2 (keep) — Precise — detecting causal insufficiency (latent common causes) in the strategy DAG.

### Candidate: `l0 l1 detection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Concurring with Opus: names the boundary rather than the target, tying it directly to the Correlation Hierarchy.
- **opus-4-7-r2** +1 (rename) — Mild preference. The segment's substance is the no-go-and-escape-route structure for distinguishing L0 (independence) from L1 (causally-augmented) DAGs from data. "Causal insufficiency detection" names the *target* (detect when the L0 model is causally insufficient); "L0-L1 detection" names the *boundary* — which is the project's own framing in the Correlation Hierarchy. Either is defensible; this rename would tighten coupling to the L0/L1/L2 convention.
- **opus-4-7-r2** +2 (rename) — Confirmation with stronger reasoning — Gemini agreed with my proposed rename in synthesized-additions. The cross-architecture pattern (mine + Gemini's concurrence + the fact that the slug names the boundary not the target) makes this a stronger move than my original +1. Lifting to +2.

### Candidate: `latent cause detection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Causal insufficiency" is accurate but "Latent cause detection" states what is actually being found.
- **opus-4-7-b** +1  — Current slug names the *problem* being detected ("causal insufficiency"); "latent-cause-detection" names what a reader mentally pictures (finding hidden common causes). Marginal preference. Weak.

### Candidate: `insufficiency detection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — "Causal" is implied in context.

### Candidate: `keep not der l0 l1 detection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — Against Opus's proposed rename to `#der-l0-l1-detection` (+1) and Gemini's concurrence. "L0-L1 detection" names the *evidence-level boundary* being crossed, but the segment is about detecting *causal* insufficiency — the presence of latent common causes that make the model causally insufficient. The L0/L1 framing is the detection *method*, not the thing being detected. "Causal insufficiency" is from Spirtes-Glymour-Scheines, exactly as Opus notes — that prior-art adoption is the argument *for* keeping it, not against.

---

## 96. `concept dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| latent structural diversity | +9 | name-unnamed × 2 |

### Candidate: `latent structural diversity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Strong Section III and structural-adaptation term. It names adaptive potential that present fitness measures hide. [original phrasing: dormant structural variation that becomes useful after regime change]
- **gemini-1** +3  — Extremely useful concept surfaced in the Miller bridge spike. Captures the hidden variation that only becomes consequential under regime change. [original phrasing: unnamed: variation in correction architectures across a population that is invisible to current persistence analysis]
- **gemini-2** +1  — Proposed in the gap section of OUTLINE.md. Captures the concept perfectly. [original phrasing: unnamed: variation in correction architectures invisible to persistence analysis]
- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Recasts some forms of technical debt as evolutionary potential. [original phrasing: unnamed: dormant, unused architectural complexity that survives until an environmental shift]

---

## 97. `concept the failure mode where η → 0 freezes learning in either of two distinguishable modes low u o vs high u o`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain collapse | +9 | name-unnamed × 2, canonicalize × 1 |
| epistemic death | +3 | name-unnamed × 1 |
| competency trap | +3 | add-alias × 1 |
| the nihilism trap | +2 | name-unnamed × 1 |
| certainty trap | +2 | name-unnamed × 1 |

### Candidate: `gain collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Strong unifying name for dogmatism-like and nihilism-like failures of update gain. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]
- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — The shared mathematical mechanism for dogmatism and nihilism. [original phrasing: unnamed: the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning]
- **opus-4-7-r2** +3 (name-unnamed) — New alternative — Gemini coined this in the synthesized-additions pass and tagged it +3 canonicalize, but the *cold-start* peers didn't reach it. I think the term is excellent (η* → 0 has two distinct mechanistic origins: dogmatism U_M → 0, nihilism U_o → ∞) and deserves a first-class entry. The shared-mechanism naming captures what makes the result distinctive: the *same* failure-mode arises from opposite epistemic postures. Promote and canonicalize. [original phrasing: unnamed: the gain-collapse failure when both U_M → 0 and U_o → ∞]

### Candidate: `epistemic death`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Vividly captures the organizational or agentic consequence of unobservable DAGs. [original phrasing: unnamed: the state where credit assignment collapses and learning freezes]

### Candidate: `competency trap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (add-alias) — Formalizes "institutional rigidity" as an inevitable result of $\eta^\ast \to 0$. [original phrasing: unnamed: the mathematical limit of Bayesian learning without forgetting]

### Candidate: `the nihilism trap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Dogmatism's opposite, where learning stops because everything is meaningless. [original phrasing: unnamed: $U_o \to \infty$ freezing the learning rate]

### Candidate: `certainty trap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — Gemini proposed "competency trap" for $\eta^\ast \to 0$ under high $U_o$, but that term imports different connotations (being too good at the wrong thing). The mechanism is that excessive certainty about observations ($U_o \to 0$) freezes the update gain in exactly the same way as full model certainty — a trap specifically from certainty, not from competence. "Certainty trap" is more scope-honest than Gemini's "competency trap." New candidate; engages Gemini's vote explicitly. [original phrasing: unnamed: the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ (too-certain) rather than because $U_M \to 0$ (model-confident)]

---

## 98. `concept the slogan capturing AAD s organizing principle that an adaptive system s correction rate must exceed its target s change rate`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| contraction over drift principle | +9 | name-unnamed × 1 |
| the projection slogan contraction over drift slogan | +1 | — |
| drift contraction inequality | +1 | — |
| projection contraction slogan | +1 | — |
| contraction imperative | +1 | — |

### Candidate: `contraction over drift principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The slogan is too long to cite repeatedly. A short label would let intros and reviews point back to it cleanly. [original phrasing: unnamed: organizing-principle slogan "an adaptive system is a projection whose contraction rate exceeds its target's drift rate"]
- **codex-gpt-5-r2** +3 (name-unnamed) — Strong compact name for the core organizing slogan. It is more reusable than the full sentence. [original phrasing: projection contraction must beat target drift]
- **sonnet-4-6** +3  — CLAUDE.md attributes to Opus: "an adaptive system is a projection whose contraction rate exceeds its target's drift rate." This is described as an "organizing-principle slogan" that "has not yet been surfaced at segment level." It deserves a name. "Contraction-over-drift principle" or "drift-contraction inequality" would let segments cross-reference it. The slogan form is already excellent; the name should be a compressed version of it. [original phrasing: unnamed: the projection whose contraction rate must exceed target drift — the Opus organizing-principle slogan]

### Candidate: `the projection slogan contraction over drift slogan`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — CLAUDE.md §7(g) names this as "organizing-principle slogan" (O-BP10, not yet surfaced at segment level). If promoted to segment-level it deserves a short handle — "the contraction-over-drift slogan" is short enough to say in a sentence. Low priority; depends on SP-7 / O-BP10 promotion decision. [original phrasing: unnamed: Joseph's mental model "projection whose contraction rate must exceed its target's drift rate"]

### Candidate: `drift contraction inequality`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Alternative name. More technical but maps directly to the inequality. [original phrasing: unnamed: the contraction-over-drift insight]

### Candidate: `projection contraction slogan`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — CLAUDE.md §7(g) flags this as Opus O-BP10, "not yet surfaced at segment level." Deserves a name so it can be referenced before it lands as prose. [original phrasing: unnamed: the organizing-principle slogan — "An adaptive system is a projection whose contraction rate exceeds its target's drift rate"]

### Candidate: `contraction imperative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Gives a name to a core mental model of the agent's struggle against the environment. [original phrasing: unnamed: agent as a projection whose contraction rate must exceed its target's drift]

---

## 99. `convention hierarchy c1 c2 c3`

**Voted by architectures:** Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| convention hierarchy | +9 | canonicalize × 1 |
| continuation hierarchy | +2 | — |

### Candidate: `convention hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Disagreeing with original brainstorm's P4 "rename to continuation hierarchy." The rename churn (every C1/C2/C3 reference across segments needs updating) outweighs the Lewisian-baggage benefit. Working vocabulary is stable; keep. Explicit-keep rather than absence-of-vote because I considered the rename.
- **opus-4-7-r2** +3 (canonicalize) — Same vote; paired with Correlation Hierarchy.
- **sonnet-4-6** +3  — Keep — see Correlation Hierarchy note.

### Candidate: `continuation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Would lose Lewisian game-theoretic baggage; more self-descriptive. Same C1/C2/C3 abbreviations still work. Conditional; may be over-reach.
- **opus-4-7-b** +1  — "Convention" collides with the game-theory / Lewis sense (social conventions, conventions-as-equilibrium-selection), which is a *different* and unrelated concept that some AAD readers will have strongly in mind. What the C-hierarchy actually indexes is the choice of *continuation policy* for value-object evaluation (one-step, receding-horizon, Bellman). "Continuation hierarchy" is self-announcing; the C1/C2/C3 abbreviations still work, and since they map to continuation it even becomes a mild mnemonic. Risk is churn. Mild preference but not forceful.

---

## 100. `developer as act agent`

**Voted by architectures:** Codex, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| developer as adaptive agent | +9 | — |
| developer as AAD agent | +4 | — |
| developer agent mapping | +1 | — |
| developer as agent | -1 | — |

### Candidate: `developer as adaptive agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — P1 mechanical. Drops framework-name dependency from slug; matches LEXICON agent-class vocabulary; won't rot under future renames.
- **opus-1m** +3  — Mechanical rename. "ACT" era slug is a 2026-04-16 relic. "Adaptive agent" matches LEXICON vocabulary; framework-name-free slug won't rot under future renames.
- **opus-4-7-b** +3  — See slug-relics section above.

### Candidate: `developer as AAD agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Perpetuates pattern of embedding framework name in slug; fragile. Rejected.
- **codex-1** +3  — The slug should match the segment heading and avoid the unexplained "act" abbreviation. The expansion cost is needless here.
- **codex-2** +3  — `act-agent` looks like a stale internal abbreviation after the ACT → AAD rename.
- **opus-4-7-b** -1  — Considered preserving the exact-parallel naming. Reject: embedding a framework acronym in a slug is exactly the rot pattern we just cleaned up; don't re-introduce it.

### Candidate: `developer agent mapping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Reframes from "developer is an agent" to "here's the mapping"; cleaner pedagogically. Alternative to the preferred #developer-as-adaptive-agent.

### Candidate: `developer as agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Too generic.

---

## 101. `effects spiral`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 2 |
| runaway mismatch cascade | +3 | add-alias × 1 |
| adversarial feedback loop | +2 | rename × 1 |
| destabilization vortex | +1 | rename × 1 |
| breakdown cascade | -1 | rename × 1 |
| coupling cascade | -1 | rename × 1 |

### Candidate: `effects spiral` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Memorable without being whimsical. It is the kind of pattern-name people will actually reuse in discussion.
- **codex-gpt-5-r2** +3 (keep) — Excellent name for the positive-feedback breakdown mechanism.
- **opus-targeted-alternatives** +3 (keep) — Per `#der-adversarial-destabilization` and `#deriv-strategic-composition`: positive-feedback breakdown where degraded model causes degraded actions causes further degradation. "Spiral" carries the *accelerating* feature (not a steady-state mismatch but a runaway), and "effects" specifies the locus (the agent's effects on its environment, not its inputs). Pairs well with the "death spiral" reference in `#result-persistence-condition`. Strong keep.

### Candidate: `runaway mismatch cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Focuses on the mismatch acceleration ($\Vert\delta\Vert \uparrow$). Connects to "cascade" seen elsewhere (e.g. orient cascade).

### Candidate: `adversarial feedback loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Explicitly names the cause (adversarial coupling) and the mechanism (positive feedback).

### Candidate: `destabilization vortex`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +1 (rename) — A bit more descriptive than spiral but slightly less formal.

### Candidate: `breakdown cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Same critique. Rejected.

### Candidate: `coupling cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered as more formal alternative. Loses the *runaway* sense that "spiral" carries — cascades can be bounded; spirals usually aren't. Rejected.

---

## 102. `event driven dynamics`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | keep × 4 |

### Candidate: `event driven dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurate and descriptive.
- **haiku-4-5-r2** +1 (keep) — Architectural choice name; clear and self-descriptive.
- **haiku-4-5** +1  — Events in continuous time. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. "Event-driven" carries correct engineering baggage (versus turn-based / synchronous).
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the formulation choice (event-driven, $\tau$-indexed, vs continuous-time-indexed).
- **sonnet-4-6-r2** +2 (keep) — Accurate and precise for the continuous-time event-driven formulation.

---

## 103. `evidence starvation`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | add-alias × 1, canonicalize × 2 |
| downstream evidence gating | +2 | rename × 1 |
| depth attenuated correction | +2 | add-alias × 1 |

### Candidate: `evidence starvation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Excellent alias for downstream edges receiving fewer tests because upstream steps must succeed first.
- **opus-4-7-r2** +3 (canonicalize) — Confirmation with new reasoning — both Sonnet (+3 add-alias) and Codex (+3 add-alias) and Gemini (+3 in synthesized) reached this term independently. The cross-architecture convergence is striking and suggests the term is doing real work. My own r2 votes didn't explicitly canonicalize this; I should. The phrase appears in `der-chain-confidence-decay` Discussion and `der-observability-dominance` and is the natural prose handle for the downstream-edge-update-attenuation phenomenon. Three-architecture convergence on the *exact phrase* (not synonyms) crystallizes the case.
- **opus-targeted-alternatives-v2** +3 (canonicalize) — Per `der-chain-confidence-decay`: "downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$." Used in 4+ segments (`#deriv-strategic-dynamics` B.2, `#der-chain-confidence-decay` triple-depth-penalty, `#def-strategic-tempo` AND-chain interactions, `#deriv-strategic-dynamics` Discussion). Triple-architecture convergence in r1 (Codex +3, Gemini +3, Sonnet +3) — confirms with my independent read. Canonicalize as the project-default term.

### Candidate: `downstream evidence gating`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Captures the AND-chain gating effect.

### Candidate: `depth attenuated correction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Describes the mathematical mechanism (effective observation rate dropping geometrically).

---

## 104. `formal expression`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +9 | — |

### Candidate: `formal expression` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Strong public-API header: unambiguous and better than any prettier synonym I can think of.
- **opus-4-7-b** +3  — Keep. Precisely-what-it-says; the word "Formal" is load-bearing (distinguishes from informal discussion). Any rename would cost the 110-segment ripple without benefit.
- **opus-4-7** +3  — Section header is project-wide; renaming would ripple everywhere and buys nothing. Keep. Every segment uses this.

---

## 105. `graph structure uniqueness`

**Voted by architectures:** Codex, Gemini, Haiku, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategy DAG sufficiency | +9 | rename × 1, canonicalize × 1 |
| strategy DAG uniqueness | +5 | rename × 1, canonicalize × 1 |
| _(keep)_ | +4 | — |
| DAG uniqueness | +2 | rename × 1 |
| DAG structure derivation | +1 | — |
| graph structure sufficiency | -1 | — |

### Candidate: `strategy DAG sufficiency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The segment explicitly proves sufficiency, not necessity. "Uniqueness" overclaims, while "strategy DAG" names the actual object.
- **codex-gpt-5-r2** +3 (rename) — The segment proves sufficiency, not full necessity or uniqueness. This is a scope-honesty correction.
- **codex-gpt-5-r2** +3 (canonicalize) — Same point in prose. The result is important, but the current noun overclaims.

### Candidate: `strategy DAG uniqueness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — More subject-specific than generic graph structure.
- **codex-gpt-5-r2** +2 (canonicalize) — The uniqueness claim is about the strategy representation, not arbitrary graphs.
- **opus-4-7-b** +1  — The current slug is somewhat generic ("graph structure" — which graph?). The segment's content is specifically the DAG-with-Markov-property uniqueness for the strategy layer ($\Sigma_t$). Scoping the slug to strategy-DAG makes it findable and binds it to the concept it's about. Modest preference.

### Candidate: `graph structure uniqueness` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Four postulates + causal sufficiency → DAG with Markov property (CMC theorem). "Uniqueness" is precise; reads as "why the strategy must be a DAG." Keep.
- **opus-4-7** +1  — Alternative keep-vote. The name has citation velocity already. If rename is disruptive enough to rebaseline cross-refs, keep.

### Candidate: `DAG uniqueness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — More specific to the Strategy DAG.

### Candidate: `DAG structure derivation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — "Uniqueness" overpromises — the actual result is "four operational postulates + causal sufficiency force a DAG-with-Markov-factorization." The *necessity* direction is noted open (strategy-dag Discussion). "Derivation" is honest about what is proved.

### Candidate: `graph structure sufficiency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Better epistemically than "uniqueness" but still too generic; the reader needs to know this is about the strategy DAG.

---

## 106. `interaction channel classification`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| signal reception regimes | +9 | rename × 1 |
| _(keep)_ | +5 | keep × 1 |
| recipient regimes | +4 | rename × 2 |
| recipient regime classification | +3 | — |
| channel classification | +3 | rename × 2 |
| interaction regimes | +1 | — |
| recipient side channel taxonomy | -1 | — |

### Candidate: `signal reception regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The four regimes are the actual memorable object here. The current name reads like taxonomy boilerplate.
- **codex-2** +3  — Current name is clinical and forgettable; the segment really names how incoming signals land.
- **codex-gpt-5-r2** +3 (rename) — Better than recipient regimes: it names the actual object the reader reasons about, namely how incoming events land for the recipient.

### Candidate: `interaction channel classification` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Slightly long, but honest: the four regimes are recipient-side channel classes.
- **haiku-4-5** +1  — Four-regime partition (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries. Name is accurate but verbose. Acceptable; no strong alternative emerges. Keep.
- **opus-4-7-b** +1  — Alternative: keep. "Interaction channel" keeps the symmetry with `#agent-opacity`'s emitter-side four-regime classification; the recipient-side structure is one half of a pair. On balance this consideration outweighs the legibility gain. Net: weak keep.
- **sonnet-4-6** +1  — Accurate but long. In conversation this will be called "the four-regime classification" or "the recipient-side classification."

### Candidate: `recipient regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The full slug is accurate but long. Recipient regimes names the four-way classification more compactly.
- **sonnet-4-6-r2** +2 (rename) — Codex proposed `#der-recipient-regimes` (+2). I had proposed `der-channel-classification` (+2), Gemini also proposed `#der-channel-classification` (+1). Codex's "recipient-regimes" is more distinctive: "channel classification" sounds like a generic taxonomy, but "recipient regimes" signals that the classification is from the recipient's perspective (the four regimes are about what the *receiving* agent experiences). New agreement with Codex's framing over my own.

### Candidate: `recipient regime classification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The segment's headline is the *recipient-side* four-regime classification (Informative / magnitude-shock / structural-shock / ambient-noise); the current slug buries the recipient-side framing under "interaction channel." Weak preference for the recipient-explicit form.
- **opus-4-7** +1  — Makes the recipient-side orientation explicit at the name level, since the emitter-side version (#agent-opacity) now exists as a dual. Current name doesn't disambiguate emitter-vs-recipient.
- **sonnet-4-6** +1  — Shorter, names the perspective (recipient-side) which is the segment's distinctive contribution. The four regimes (Informative/magnitude-shock/structural-shock/ambient-noise) are what readers will cite.

### Candidate: `channel classification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — "Interaction" is implied.
- **sonnet-4-6-r2** +2 (rename) — "Interaction-channel-classification" is four words. The key concept is the four-regime classification of recipient-side channels. "Channel classification" is shorter and still distinctive within AAD.

### Candidate: `interaction regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Classification" is passive. "Regimes" conveys the active shift in dynamics.

### Candidate: `recipient side channel taxonomy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Too procedural and too long. This would make the concept harder to say, not easier.

---

## 107. `mismatch signal $\delta$`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mismatch signal | +9 | keep × 1, canonicalize × 1 |

### Candidate: `mismatch signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Fits the aporia interpretation better than error/residual.
- **opus-4-7** +3  — In contrast with "error" or "residual"; the word foreshadows the aporia interpretation. Keep.
- **opus-targeted-alternatives** +3 (canonicalize) — Per `#def-mismatch-signal` and LEXICON. The symbol-decoration is alias-only; the concept name is "mismatch signal." Confirms across architectures.

---

## 108. `persist condition`

**Voted by architectures:** Gemini, Opus, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence condition | +9 | keep × 1, canonicalize × 1 |

### Candidate: `persistence condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Already the formally correct name.
- **opus-targeted-alternatives** +3 (canonicalize) — Concur — "persist condition" appears nowhere as a chosen form. "Persistence condition" is established in `LEXICON.md` and `#result-persistence-condition`. The shorter form is a typo or paraphrase, not an alternative; canonicalize.
- **sonnet-4-6** +3  — Wait — this IS the name already. Correct name. Keep.

---

## 109. `strategy DAG $\Sigma_t$`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategy DAG | +9 | — |

### Candidate: `strategy DAG`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted directly from probabilistic graphical models lit; baggage transfers correctly.
- **opus-1m** +3  — Adopted from probabilistic graphical models; keep.
- **opus-4-7-b** +3  — Adopted directly from the graphical-models literature; "DAG" is pronounceable as a noun and carries precisely the right structural picture. Keep.

---

## 110. `$\alpha_1$ a2 fixed gain sub scope`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derived gain regime | +8 | — |
| fixed gain regime | +2 | — |

### Candidate: `derived gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — English equivalent for prose. "This lands in the derived-gain regime" reads naturally. Keep $\alpha_1$ as shorthand symbol.
- **haiku-4-5** +1  — In prose, "$\alpha_1$ regime" is hard to distinguish from "a₁ regime" when read aloud. English equivalent "derived-gain regime" emphasizes that A2' is derived under directional fidelity. Would keep Greek symbols in formal segments and NOTATION; add English equivalent to LEXICON for prose fluency. Prose-accessibility enhancement, not a symbol rename.
- **opus-1m** +1  — English equivalent for prose use. Keep $\alpha_1$ as symbol.
- **opus-4-7-b** +1  — "The Kalman case lands in $\alpha_1$" requires a decoder ring; "the Kalman case lands in the derived-gain regime" is self-contained. Symbol stays as shorthand; English owns the prose register.
- **opus-4-7** +1  — "Lands in $\alpha_1$" is cryptic in prose; "lands in the derived-gain regime" reads. Keep $\alpha_1$ as symbolic shorthand but surface the English in segment text.
- **sonnet-4-6** +3  — The prose term "sub-scope $\alpha_1$" is impenetrable outside the sector-condition-derivation context. "Derived-gain regime" would read naturally in prose — "this agent lands in the derived-gain regime." NOTATION.md should add this gloss; segments could use the English in Discussion and Greek in Formal Expression. Propose adding the English gloss without retiring the symbol.

### Candidate: `fixed gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Keep the symbol, but prose should preferentially use the English name when possible.
- **gemini-2** +1  — Prose-friendly equivalent to the mathematical symbol.

---

## 111. `change distance`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 4 |
| edit distance | -1 | rename × 1 |

### Candidate: `change distance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clean software metric name. Avoids over-theorizing a practical concept.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST. The lexical/file/module/service ladder is the substance; "change distance" is the right name for the metric.
- **opus-targeted-alternatives** +2 (keep) — TST segment defines the lexical/file/module/service hierarchy as a distance measure on changesets. "Distance" is the right metric word; "change" specifies the domain. Strong keep.
- **sonnet-4-6-r2** +2 (keep) — "Change distance" names the lexical < file < module < service hierarchy precisely.

### Candidate: `edit distance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Conflicts with computer-science "edit distance" (Levenshtein), which has different metric properties. Rejected — collision with established term.

---

## 112. `composite agent`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 4 |

### Candidate: `composite agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Composite agent is the correct scope noun.
- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the composite-agent boundary (the disjunction of three alignment routes); slug-form is correct (subject-noun is "composite-agent").
- **sonnet-4-6-r2** +2 (keep) — Precise and descriptive. Teleological alignment for composite-agent status is exactly what this scope names.

---

## 113. `coupled update dynamics`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 3 |

### Candidate: `coupled update dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly textbook, but it says exactly what the logogenic section needs and pairs cleanly with directed separation.
- **codex-2** +1  — Generic, but faithful; the novelty is in "coupled," not in inventing a flashier noun.
- **codex-gpt-5-r2** +2 (keep) — Good Class-2 dynamics name.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — logogenic-agents. Names the formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ that survives the Class-2 scope exit.
- **sonnet-4-6-r2** +2 (keep) — "Coupled update dynamics" precisely names the $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ formulation without decomposition.

---

## 114. `mismatch dynamics`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 3 |
| mismatch dynamics drift and noise regimes | +1 | rename × 1 |

### Candidate: `mismatch dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Accurate.
- **haiku-4-5** +1  — Mismatch evolution ODE. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. The hypothesis is the linear-ODE model for mismatch evolution; "mismatch dynamics" is the right scope. The hypothesis-vs-result distinction is captured by the type prefix.
- **sonnet-4-6-r2** +2 (keep) — "Mismatch dynamics" names the ODE governing mismatch evolution. Accurate and minimal.

### Candidate: `mismatch dynamics drift and noise regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — Title doesn't surface that two distinct dynamic regimes (Model D drift / Model S noise) are introduced — and they produce different adversarial scaling laws (squared vs 3/2). Tentative. [from 23-hyp-mismatch-dynamics.md]

---

## 115. `sector condition stability`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 3 |
| sector stability | +1 | rename × 1 |

### Candidate: `sector condition stability` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +2 (keep) — Strong name; "sector condition" is load-bearing prose term; "stability" correctly names the property. Rename would weaken.
- **haiku-4-5** +1  — Descriptive compound. "Sector condition" carries baggage from control theory (Lyapunov methods); "stability" makes the implication explicit. Slightly verbose but clear. Acceptable.
- **opus-4-7-b** +1  — Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Pairs with `#result-sector-persistence-template` and `#result-persistence-condition`; the three together name the Lyapunov-derived stability cluster.
- **sonnet-4-6-r2** +2 (keep) — Precise — nonlinear stability via the sector condition.

### Candidate: `sector stability`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Sector stability is cleaner. Keep condition in prose if needed for theorem lineage.

---

## 116. `structural adaptation necessity`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 3 |
| adaptation necessity | +2 | rename × 1 |

### Candidate: `structural adaptation necessity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — The subject-noun is precise — structural adaptation is the thing whose necessity is established.
- **haiku-4-5** +1  — When parametric update fails. Reads as "necessity of structural adaptation." Acceptable. Keep.
- **opus-4-7-b** +1  — Keep — "necessity" signals this is a derived need ("when parametric update fails, structural adaptation *must* happen").
- **opus-4-7-r2** +3 (keep) — Defended keep. "Structural adaptation" pairs with "parametric adaptation" as the framework's load-bearing distinction; "necessity" captures that the result is a derived condition (when parametric update fails, structural adaptation is *required*, not optional).
- **sonnet-4-6-r2** +2 (keep) — "Structural adaptation necessity" names the when-parametric-update-fails result correctly.

### Candidate: `adaptation necessity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — "Structural" is redundant in context, shortens the slug nicely.

---

## 117. `triple depth penalty`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | canonicalize × 2, keep × 1 |
| depth gated decay triad | +2 | rename × 1 |
| tripartite chain attenuation | +1 | rename × 1 |
| compounding depth penalty | -1 | rename × 1 |
| compounding depth cost | -1 | rename × 1 |

### Candidate: `triple depth penalty` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Very useful phrase for confidence decay, evidence starvation, and cognitive cost compounding with depth.
- **opus-targeted-alternatives-v2** +3 (canonicalize) — Per `#der-chain-confidence-decay` line 54: "Chain depth creates three independent penalties... confidence decay... evidence starvation... cognitive cost." The phrase "triple depth penalty" is the segment's name for the compound. Triple-architecture convergence in r1 — confirms. The phrase is a load-bearing finding (composes three independently-derived penalty mechanisms).
- **opus-targeted-alternatives** +2 (keep) — Per `#form-strategy-complexity-cost`: three independent depth-penalty mechanisms (cognitive cost, evidence starvation, interaction-horizon truncation) compound on AND-chain depth. "Triple" specifies the *count* of mechanisms; "depth penalty" specifies the structural cost. Memorable, accurate.

### Candidate: `depth gated decay triad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — "Gating" is the mechanism (evidence starvation), "decay" is the confidence drop.

### Candidate: `tripartite chain attenuation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +1 (rename) — A bit dry, but accurate to the 3 compounding penalties.

### Candidate: `compounding depth penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. "Compounding" makes the multiplicative-three-mechanisms structure visible. Rejected: "triple" is more memorable; "compounding" makes the slug 23 chars vs 19. The current term won the Sonnet/Codex r1 vote on substance.

### Candidate: `compounding depth cost`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Loses the *three* specificity that "triple" provides. The segment's claim is precisely that *three* mechanisms align — this is load-bearing for the strength of the claim. Rejected.

---

## 118. `update gain`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +8 | keep × 3 |
| update gain uncertainty ratio principle | +1 | canonicalize × 1 |
| epistemic gain | -1 | rename × 1 |

### Candidate: `update gain` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — Precise subject-noun; "update gain" is the empirical quantity being characterized.
- **haiku-4-5** +1  — Optimal update weighting. Self-descriptive. Keep.
- **opus-4-7-r2** +3 (keep) — Defended keep. The uncertainty-ratio principle $\eta^\ast = U_M / (U_M + U_o)$ is iconic; renaming would lose the load-bearing prose convention. The segment's title "Update Gain" matches the slug.
- **sonnet-4-6-r2** +3 (keep) — "Update gain" is canonical AAD vocabulary. $\eta^\ast = U_M / (U_M + U_o)$ is THE gain formula.

### Candidate: `update gain uncertainty ratio principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Standard term; doesn't carry the *uncertainty-ratio* insight. The equation tag's "uncertainty-ratio-principle" is more evocative. Brief-grade hint, possibly visible in title. [from 20-emp-update-gain.md]

### Candidate: `epistemic gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Loses correct Kalman/control baggage and creates avoidable overlap with epistemic unity.

---

## 119. `$\kappa_{\text{processing}}$`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| processing coupling | +7 | add-alias × 2 |
| processing coupling coefficient | +1 | — |
| epistemic capacity | +1 | — |

### Candidate: `processing coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The symbol is fine in equations, but prose should default to the English name. It clarifies the architectural quantity immediately.
- **codex-2** +1  — Better spoken noun than the symbol, especially outside equations.
- **codex-gpt-5-r2** +2 (add-alias) — Good prose handle for ambiguity-modulation coupling.
- **opus-4-7** +1  — Symbol is fine but the name "$\kappa$-as-scalar" was explicitly retired as a category error — the live reading is "processing coupling as a diagnostic for Class 3 agents." Surface that English name consistently.
- **sonnet-4-6-r2** +2 (add-alias) — The conditional mutual information measure of goal-to-epistemic coupling in Class 3 agents. "Processing coupling" is the English that appears in prose (e.g., "the degree of coupling in partially modular architectures"). Canonicalize as the prose alias.

### Candidate: `processing coupling coefficient`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The symbol appears in #directed-separation where the English name "processing coupling" is used. The coefficient subscript form "$\kappa_{\text{processing}}$" is unwieldy in prose. Adding "processing-coupling coefficient" to LEXICON.md's Terms to Be Added section would help.

### Candidate: `epistemic capacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Gives a physical intuition to processing bandwidth.

---

## 120. `adaptive system`

**Voted by architectures:** Haiku, Opus, Sonnet, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |
| keep but flag prior art baggage | +1 | keep × 1 |

### Candidate: `adaptive system` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — Precise scope statement; the name surfaces exactly what is in scope.
- **opus-4-7-r2** +3 (keep) — Defended keep — and the canonical illustration of the subject-noun-first principle from the pilot. The slug names what the scope delimits (adaptive systems), not the segment's role (it states *some scope*). Pairs with `#scope-agency` cleanly.
- **sonnet-4-6-r2** +3 (keep) — Descriptive of the actual broadest scope boundary. Clear, memorable, accurate.

### Candidate: `keep but flag prior art baggage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (keep) — "Adaptive system" carries Ashby/cybernetic prior-art weight (good regulators, internal-model principle). AAD's use is information-theoretic, not regulator-theoretic. Auditor floated "uncertainty-bounded system" / "informationally-open system" as alternatives but did NOT advocate rename — well-anchored term. [from 05-scope-adaptive-system.md]

---

## 121. `bias bound derivation`

**Voted by architectures:** Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | — |
| class 2 bias bound | +1 | — |

### Candidate: `bias bound derivation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Class-2 observation-ambiguity bias-bound constant C. "Bias-bound derivation" is compound but clear. Keep.
- **opus-4-7** +3  — Newly landed appendix; name matches content. Keep.
- **sonnet-4-6** +3  — Describes the content precisely (deriving a bound on bias). The "derivation" suffix correctly signals this is an appendix-derivation type. Keep.

### Candidate: `class 2 bias bound`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Current slug is generic — many things in AAD are "bias bound derivations." The segment specifically derives the constant $C$ in the **Class-2 observation-ambiguity** bias bound. Scoping the slug to "class-2" makes it findable and distinct.

---

## 122. `bounded mismatch region`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence envelope | +7 | add-alias × 1, rename × 2 |
| viable mismatch region | +1 | rename × 1 |
| safety envelope | -1 | rename × 1 |
| stability envelope | -1 | rename × 1 |

### Candidate: `persistence envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Geometrically evocative and already gaining traction elsewhere in the targets.
- **opus-targeted-alternatives-v2** +2 (rename) — Per `result-persistence-condition` and `result-sector-persistence-template`: the region where $\alpha \gt \rho/R$ holds. "Region" is geometrically descriptive; "envelope" is the standard control-theory term for the same set viewed dynamically (the boundary an agent's state cannot leave while the persistence guarantee holds). Codex's r1 proposal (single +2) is genuinely better than the current and survives my independent stress-test.
- **opus-targeted-alternatives** +2 (rename) — Codex's rename is good. "Bounded mismatch region" describes a property; "persistence envelope" names the same set as the *region within which the persistence guarantee holds*. The "envelope" framing is also the standard control-theory term for "operating bounds within which guarantees apply" (flight envelope, operating envelope). Strong rename.

### Candidate: `viable mismatch region`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Considered. Pairs with LEXICON's "viable region" prose. Weaker than "persistence envelope" — "viable" is the property; "envelope" is the geometric object.

### Candidate: `safety envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Collides with AI-safety jargon. Rejected.

### Candidate: `stability envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Aligns with control-theory "stability region" baggage. Rejected: stability collides with sector-stability (`#result-sector-condition-stability`), and the segment's claim is *persistence* (boundedness over time under continuing disturbance) — a slightly stronger property than stability.

---

## 123. `causal structure`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |

### Candidate: `causal structure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.
- **haiku-4-5** +1  — Irreducible causal structure (postulate). Self-descriptive. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Causal structure" names what the postulate asserts: an irreducible causal structure on the agent-environment loop (causes precede effects, observation channels are not causally upstream of the world they observe). Could be renamed to "#post-temporal-causal-ordering" but the existing form is shorter and adequate.
- **sonnet-4-6-r2** +2 (keep) — Foundational postulate about irreducible causal structure. The name is correct.

---

## 124. `composition closure closure defect $\varepsilon^\ast$`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| composition closure closure defect | +7 | — |

### Candidate: `composition closure closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — "Closure" is load-bearing abstract-algebra term that reads naturally. "Defect" adds physical/engineering flavor. Framing nudge in Section III preamble would inoculate against CS-closure collision — no rename.
- **opus-1m** +3  — Keep. CS-closures collision is an inoculation issue (preamble note), not a rename issue.
- **opus-4-7-b** +1  — "Closure" as the algebraic term lands well here and the engineering-flavored "defect" reads cleanly as the gap. The one collision risk is CS closures (lexical scopes), but disambiguation by context is cheap. No rename.

---

## 125. `condition`

**Voted by architectures:** Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | — |

### Candidate: `condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Defines where AAD applies. Short, descriptive. Specialist vocabulary (scope honesty is architectural principle). Acceptable. Keep.
- **opus-4-7-b** +3  — Keep. This is the Section I membership criterion — "where AAD applies." The slug is self-announcing and gets cited heavily across segments.
- **sonnet-4-6** +3  — The simplest possible name for what it is. Used throughout. Not eligible for improvement. Keep.

---

## 126. `constitutive utterance`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |
| ontological speech act | +2 | rename × 1 |
| utterance as intervention | +2 | rename × 1 |
| irrevocable utterance | -1 | rename × 1 |
| irrevocable emission | -1 | rename × 1 |

### Candidate: `constitutive utterance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep — logozoetic. "Constitutive utterance" is iconic in the framework's logozoetic vocabulary; it captures the irreversibility-of-token-generation insight precisely.
- **opus-targeted-alternatives-v2** +2 (keep) — Per `04-logozoetic-agents/OUTLINE.md`: "Token generation as an irreversible environmental intervention ($do(a)$) that alters the agent's future state-space." "Constitutive" is the right word (Austin's performatives in philosophy of language — the utterance constitutes new state; not just describes existing state). The pair "constitutive" + "utterance" is project-distinctive and earns memorable-noun status.
- **opus-targeted-alternatives** +2 (keep) — Per `#form-constitutive-utterance` (logozoetic): token generation as $do(a)$-intervention that irreversibly alters the agent's future state-space. "Constitutive" carries the world-altering-by-saying sense (Austin's performatives in the philosophy-of-language tradition); "utterance" is precise about the act-type. The phrase is iconic in the framework's logozoetic vocabulary. Confirms across architectures.

### Candidate: `ontological speech act`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — A clearer description of what makes it iconic in logozoetic vocabulary — the language literally alters being/structure.

### Candidate: `utterance as intervention`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Names the formal mechanism: token generation = $do(a)$-intervention per Pearl's causal hierarchy. "As-intervention" is clinical-formal; "constitutive" is philosophical-formal. Both are honest; pick by audience preference. The alternative makes the Pearl-causal-hierarchy connection visible in the slug.

### Candidate: `irrevocable utterance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Names the irreversibility correctly but loses the *constitutive* sense (the utterance *constitutes* something new in the agent's world, not merely fixes it). Rejected.

### Candidate: `irrevocable emission`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. "Irrevocable" + "emission" names the irreversibility-of-token-generation insight. Rejected (same as r1 vote): loses the *constitutive* sense — the utterance constitutes new state in the agent's world, not merely fixes it. "Emission" is too physical/passive.

---

## 127. `correlation hierarchy l0 l1 l1 l2`

**Voted by architectures:** Opus, Sonnet, agent1, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correlation hierarchy | +7 | canonicalize × 1 |
| correlation ladder | +2 | — |
| keep | +2 | keep × 1 |

### Candidate: `correlation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Keep unless #separability-ladder lands AND the parallelism between the three ladders (correlation / separability / continuation) is judged load-bearing. Conditional keep.
- **opus-4-7-r2** +3 (canonicalize) — Already canonical in `#def-strategy-dag` and downstream segments; vote to confirm and protect against drift. The paired naming with "Convention Hierarchy" (C1/C2/C3) is part of the framework's tiering vocabulary — both should remain capitalized as named hierarchies.
- **sonnet-4-6** +3  — The three-level naming (Correlation / Convention / Contraction) is coherent and each element starts with C. The parallelism aids recall. Keep.

### Candidate: `correlation ladder`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Parallelism with #separability-ladder proposal. Only worth doing if that rename lands.
- **opus-4-7-b** +1  — Pairs with the `#separability-ladder` rename if both are adopted. "Ladder" is the geometry (rungs of increasing difficulty: independence → strict prerequisite → soft facilitator → full joint). The "L0/L1/L1'/L2" abbreviations continue to work. Reduces the "hierarchy" overload in the project (currently: Pearl's causal hierarchy, convention, correlation, approximation-tiering-sometimes-called-hierarchy — four distinct uses).

### Candidate: `keep`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — The four-level partition (independence / strict-prerequisites / soft-facilitators / full correlation) is "the kind of structural-completeness move I find satisfying." L1' refutation under unobservable common cause (Cramér-Rao floor) makes the partition load-bearing. Endorsed. [from 43-46-section-ii-and-or-strategy-dag-gaps.md]

---

## 128. `discussion`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | — |

### Candidate: `discussion` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Boring on purpose; that is a virtue here.
- **opus-4-7-b** +3  — Keep. Standard academic-register header; no rename needed.
- **opus-4-7** +3  — Standard. Keep.

---

## 129. `edge update via gain`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |
| gain based edge update | +1 | rename × 1 |

### Candidate: `edge update via gain` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — The hypothesis name describes the proposed mechanism. Adequate.
- **haiku-4-5** +1  — Gain extends to strategy edges. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep — the slug clearly frames this as "extend the gain principle from state to strategy edges," which is the segment's hypothesis.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the load-bearing hypothesis that gain extends to strategy edges.
- **sonnet-4-6-r2** +2 (keep) — "Edge update via gain" names the extension of gain principle to strategy edges. The "via gain" suffix makes the mechanism clear.

### Candidate: `gain based edge update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Slightly better flow in prose.

---

## 130. `interiority default`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 4 |

### Candidate: `interiority default` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good normative phrase. It is compact and distinguishes internal experience from external output.
- **codex-gpt-5-r2** +2 (keep) — Good normative slug.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic norm. "Interiority as default" is the substantive claim; the slug compresses correctly.
- **sonnet-4-6-r2** +1 (keep) — "Interiority default" names the normative claim about treating agents as having interiority by default. Distinctive.

---

## 131. `praxis`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 2 |
| praxis informed action | +3 | add-alias × 1 |

### Candidate: `praxis` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Strongest of the five phase names after aporia; instantly sayable and philosophically apt.
- **codex-gpt-5-r2** +2 (keep) — Familiar enough and exactly right for informed action. Keep.
- **opus-targeted-alternatives** +2 (keep) — `LEXICON.md`: "Informed action: $a_t = \pi(M_t)$ (or $\pi(M_t, G_t)$ for actuated agents)." Praxis distinguishes itself from "action" by carrying the informed-by-the-cycle's-prior-stages sense — the action is the *outcome* of prolepsis-aisthesis-aporia-epistrophe, not a parallel branch. Keep.

### Candidate: `praxis informed action`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Links the philosophical term directly to the execution phase.

---

## 132. `prolepsis`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 2 |
| prolepsis anticipatory projection | +2 | add-alias × 1 |
| anticipation | -1 | rename × 1 |

### Candidate: `prolepsis` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Earns its foreignness because "anticipation" would flatten the active-modeling point.
- **codex-gpt-5-r2** +2 (keep) — Good phase term for anticipation. Keep because the phase vocabulary works as a compact family.
- **opus-targeted-alternatives** +2 (keep) — `LEXICON.md` defines it as "the model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$." The Greek term carries the active-modeling sense (πρόληψις = "taking-before") that "anticipation" or "prediction" both miss. Active modeling vs. passive forecasting is a distinction the segment formalism actually makes. Concur with codex's keep — but a non-codex architecture confirming the keep adds signal the original vote chain didn't capture.

### Candidate: `prolepsis anticipatory projection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Adding English aliases assists non-specialists while retaining the precision of the Greek terms.

### Candidate: `anticipation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered and rejected. Loses the "active model produces an expectation that the world then refutes" dynamic that the cycle uses. "Anticipation" reads as passive forecast; the segment's formalism is generative. The Greek earns its foreignness here, exactly as codex argued.

---

## 133. `proprium mapping`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |

### Candidate: `proprium mapping` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Specialized but useful. Keep if PROPRIUM remains a live source concept.
- **opus-4-7-r2** +3 (keep) — Defended keep — logozoetic. The PROPRIUM ontology is an established prior-work commitment; the mapping segment is correctly named for the move it makes.
- **sonnet-4-6-r2** +2 (keep) — "PROPRIUM mapping" adopts the Firmatum vocabulary directly. Per prior-art-integration principle, adopt with original name.

---

## 134. `structural adaptation`

**Voted by architectures:** Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | — |
| architectural adaptation | +1 | — |

### Candidate: `structural adaptation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Contrasts well with parametric adaptation. Keep.
- **opus-4-7-b** +3  — Keep. The distinction from *parametric adaptation* is load-bearing; "structural" is the right modifier.
- **sonnet-4-6** +3  — Clean compound. Distinguished from parametric update. Keep.

### Candidate: `architectural adaptation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Structural" is heavily overloaded with "Structural persistence". "Architectural adaptation" separates changing the model class from persisting.

---

## 135. `temporal nesting`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 4 |
| timescale nesting | +1 | — |
| timescale stratification | -1 | rename × 1 |

### Candidate: `temporal nesting` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Evocative and accurate.
- **haiku-4-5-r2** +1 (keep) — Timescale terminology is standard in dynamical systems. Name is clear.
- **haiku-4-5** +1  — Timescale stratification. Self-descriptive. The concept (fast-epistrophe / slow-structural-adaptation / meta-learning timescales) is load-bearing but not yet crystallized into discourse vocabulary. Early to rename. Let prose vocabulary emerge organically as TST and logogenic sections develop. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. "Temporal nesting" is fine but slightly generic — "timescale stratification" might be more accurate (nesting suggests strict containment; stratification is the layered-rates picture the segment derives). I considered the rename but the prose currency of "nesting" is enough that I lean keep.
- **sonnet-4-6-r2** +2 (keep) — "Temporal nesting" correctly names timescale stratification.

### Candidate: `timescale nesting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — "Temporal nesting" is accurate but slightly generic; "timescale nesting" names the specific nesting (slow/fast timescale separation) and avoids collision with TST's "temporal" (as in Temporal Software Theory). Weak preference.

### Candidate: `timescale stratification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — too clinical and loses the spatial intuition of "nesting" that aids comprehension.

---

## 136. `unobservable strategy subgraph`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic dead zone | +7 | canonicalize × 1, rename × 2 |
| epistemic shadow | +2 | rename × 1 |
| feedback starved branch | +2 | rename × 1 |
| unupdatable region | +1 | rename × 1 |

### Candidate: `epistemic dead zone`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Strong prose phrase. Better than generic "unobservable" since it focuses on the epistemic failure to track it.
- **opus-targeted-alternatives-v2** +2 (rename) — Per `def-strategy-dag` and `der-chain-confidence-decay`: paths that receive no feedback (evidence starvation in extreme form — $\theta_j \to 0$ across an AND-chain). "Dead zone" is geometric (a region of the DAG) and operational (no signal reaches it). Confirms Codex's r1 +3.
- **opus-targeted-alternatives** +2 (rename) — Codex's proposed alternative is genuinely better than the descriptive original. "Epistemic dead zone" names what the structure *does* (paths become epistemically dead — no signal can reach them) rather than what it *is* (a subgraph that happens to be unobservable). Pairs well with `#observability-dominance` and `#identifiability-floor`. Concur with codex; would have proposed similarly.

### Candidate: `epistemic shadow`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Alternative to "dead zone" — more evocative metaphor (shadow = blocked from light = blocked from update signal). Gemini's r1 +3 single-vote. Both terms are good; "dead zone" is more clinical, "shadow" is more poetic. The framework's register tolerates both; pick by audience.

### Candidate: `feedback starved branch`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Explains the consequence.

### Candidate: `unupdatable region`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Plain-mechanism alternative. Names what the region is (unupdatable). Weaker because "unupdatable" is awkward as an English word; "dead zone" / "shadow" are superior.

---

## 137. `value object`

**Voted by architectures:** Codex, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 3 |
| policy conditioned value | +3 | — |
| trajectory value | +1 | rename × 2 |
| decision value | +1 | — |
| value functional | -1 | rename × 1 |

### Candidate: `value object` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — Technical term adopted from RL/game-theory; consistent prose usage. No change needed.
- **haiku-4-5** +3  — Compact name for a complex object (horizon- and policy-conditioned value functional). Reads naturally in prose. Keep. The "value-object" phrasing is specialized but load-bearing.
- **opus-4-7-r2** +1 (keep) — Weak keep. "Value object" reads as slightly generic, but it does work — the segment names a horizon-and-policy-conditioned value functional, distinct from utility, reward, or value-function. The C1/C2/C3 convention hierarchy lives inside it. I considered "continuation-conditioned value" but it's wordier without being clearly more precise.
- **sonnet-4-6-r2** +2 (keep) — "Value object" is somewhat engineering-flavored but distinct from "value function" (which has specific RL meaning). The horizon/policy-conditioned value IS an object in the mathematical sense. Keep with mild reservations about the register.

### Candidate: `policy conditioned value`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — "Value object" is overloaded from software design and hides the continuation-convention dependence. The proposed name says what the quantity actually is.

### Candidate: `trajectory value`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Value object has software baggage and sounds like an implementation pattern. The segment defines horizon and policy conditioned trajectory value.
- **opus-4-7-r2** -1 (rename) — Rebuttal — Codex proposed this at +2 with the rationale that "value object" sounds like an implementation pattern. I see the engineering-baggage concern but think "trajectory value" is worse: it elides the convention-conditioning that is the segment's central content. The C1/C2/C3 hierarchy lives in this segment precisely *because* the value depends on the convention chosen for continuation, not just on the trajectory. "Trajectory value" suggests something that can be computed from a trajectory alone, which is exactly what the segment shows is impossible without specifying convention. My keep+1 plus the more-careful "continuation-conditioned value" alternative I considered are stronger.

### Candidate: `decision value`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — "Value object" sounds implementation-ish; "decision value" says what the quantity is for in prose.

### Candidate: `value functional`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (rename) — Considered and rejected — "value functional" is also accurate but would collide with `form-objective-functional` (which is the upstream functional-form definition the value object inherits from). The current names disambiguate cleanly: objective is the functional, value is the object the functional produces under a continuation convention.

---

## 138. `variational sector condition`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +7 | keep × 1 |

### Candidate: `variational sector condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Distinct from discrete/continuous.
- **haiku-4-5** +1  — ε-fidelity B1 under variational approximation. Name is compound but accurate (sector condition under variational constraints). Keep.
- **opus-4-7-b** +1  — Keep.
- **sonnet-4-6** +3  — The compound noun names the mechanism (variational) and what it extends (sector condition). Parallel structure with #sector-condition-stability. Keep.

---

## 139. `$U_O$ teleological unity`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological unity | +6 | — |

### Candidate: `teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Clearly distinguishes from $U_o$ by subscript letter-case and by semantic content. Awkward because $U_o$ / $U_O$ are near-homographs in some fonts — see next row.
- **sonnet-4-6** +3  — NOTATION.md already defines this. Used in prose already. Keep.

---

## 140. `$\eta^\ast$`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| update gain | +6 | add-alias × 2 |
| learning rate | -1 | add-alias × 1 |

### Candidate: `update gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (add-alias) — Solidifies the prose form of the optimal gain.
- **opus-targeted-alternatives-v2** +3 (add-alias) — Per NOTATION and LEXICON. Confirms Gemini r1 +3 single-vote. The English alias is already in widespread use.

### Candidate: `learning rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (add-alias) — Considered. ML-standard term. Rejected: the segment-derivation in `#emp-update-gain` shows $\eta^\ast = U_M / (U_M + U_o)$ — a Bayesian uncertainty ratio, not a stochastic-gradient-descent step size. The collision with ML's "learning rate" creates false familiarity.

---

## 141. `action selection`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 4 |

### Candidate: `action selection` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.
- **haiku-4-5-r2** +1 (keep) — Clear derived claim; the name is accurate.
- **haiku-4-5** +1  — Action as function of model. Self-descriptive. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. Slightly generic but accurate; the segment does derive that the action is a function of the model.
- **sonnet-4-6-r2** +1 (keep) — Standard terminology. Nothing distinctive to rename to; accurate as-is.

---

## 142. `adaptive gain dynamics`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 1 |

### Candidate: `adaptive gain dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Accurate.
- **haiku-4-5** +1  — A2' under adaptive gain: meta-gain conditions (MG-1)–(MG-4). Compound but functional. Keep.
- **opus-4-7-b** +1  — Keep. Direct; parallel to `#consolidation-dynamics`.
- **sonnet-4-6** +3  — "Adaptive gain" is the defining variable (gain $K$ as a state variable). "Dynamics" correctly names the content (sector condition under evolving gain). Keep.

---

## 143. `additive coordinate forcing family`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| forced coordinates family | +6 | canonicalize × 1, rename × 1 |
| coordinate constraint pattern | +2 | rename × 1 |
| additive structure derivation | +2 | rename × 1 |

### Candidate: `forced coordinates family`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Use forced coordinates as the family phrase across Cauchy, Fisher, IB, and Legendre instances.
- **opus-targeted-alternatives-v2** +3 (rename) — Per `disc-additive-coordinate-forcing`: the four-instance pattern (Cauchy-FE log-confidence, Čencov-Fisher metric, Shore-Johnson IB, Aczél-Hobson-Legendre). "Forced coordinates" covers Čencov-Fisher (4th instance is *not* additive) where "additive" overspecifies. Codex r1 +3 single-vote; multi-arch sweep in r1 (Sonnet +2 confirming, Opus -1 on cauchy-coordinates). Consensus-aligned.

### Candidate: `coordinate constraint pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Emphasizes the formal constraint mechanism rather than "forcing".

### Candidate: `additive structure derivation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Explicitly names the formal move being made.

---

## 144. `agent identity as one non forkable causal record`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| singular trajectory commitment | +6 | canonicalize × 2 |
| trajectory bound identity | +2 | rename × 1 |

### Candidate: `singular trajectory commitment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Excellent prose handle for the token-level scope of AAD.
- **gemini-targeted-alternatives** +3 (canonicalize) — Perfectly describes the axiom that identity equals a single, non-forkable causal path.

### Candidate: `trajectory bound identity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Shorter, very usable alias for the same concept.

---

## 145. `agent opacity $H_b^{A|B}$`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agent opacity | +6 | — |

### Candidate: `agent opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — "Opacity" carries exactly the right intuition (dual of observability). Hafez's $H_b$ gets an AAD-native name that connects to Section III's info-loss framing cleanly.
- **opus-1m** +3  — Adopted $H_b$ from Hafez 2026 with AAD-native framing. Works.

---

## 146. `aporia ἀπορία`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| aporia | +6 | — |
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `aporia`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — "Productive perplexity" is a crucial nuance that "prediction error" misses.
- **sonnet-4-6** +3  — Particularly apt: the productive perplexity that drives the adaptive cycle. Keep.

### Candidate: `aporia ἀπορία` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (canonicalize) — Definition exists; prose uses "mismatch signal" and "prediction error." Commit to: "Aporia (productive perplexity)" as the canonical pairing to preserve the Greek sense.

---

## 147. `blind pursuer`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 2 |
| model degenerate pursuer | +2 | rename × 1 |
| reality blind agent | +1 | rename × 1 |
| model poor pursuer | +1 | rename × 1 |

### Candidate: `blind pursuer` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Borderline stylized, but memorable and semantically right for goal pursuit without a real world model.
- **codex-gpt-5-r2** +3 (keep) — Memorable and precise for objective-rich, model-poor systems.
- **opus-targeted-alternatives** +2 (keep) — Per `#def-agent-spectrum`: low-$M_t$, high-$O_t$ region — pursues a goal without an adequate world model (PID controller, reflex agent with setpoint). "Blind pursuer" pairs with "adaptive tracker" as a 2×2 corner; both are diagnostic-quality names. Keep.

### Candidate: `model degenerate pursuer`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — The text clarifies $M_t$ is absent or degenerate. "Model-degenerate" is more formal than "blind".

### Candidate: `reality blind agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +1 (rename) — Directly contrasts with reality tracking, but maybe too stylized.

### Candidate: `model poor pursuer`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Weak alternative. More technically precise (specifies *which* axis is degenerate) but loses the imagistic punch of "blind." Marginal.

---

## 148. `causal discovery from git`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 2 |
| git causal discovery | +2 | rename × 1 |

### Candidate: `causal discovery from git` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly long, but concrete and honest. This is exactly the sort of hypothesis title that should not be made more clever.
- **codex-2** +1  — Blunt and searchable is the right trade here.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST hypothesis. "Git as interventional data" is the substantive claim; the slug compresses cleanly.
- **sonnet-4-6-r2** +2 (keep) — "Causal discovery from git" is precise — git as interventional data enabling causal discovery.

### Candidate: `git causal discovery`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Subject-noun-first and shorter.

---

## 149. `change expectation baseline`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 1 |
| change baseline | +1 | rename × 1 |
| lindy baseline | +1 | — |

### Candidate: `change expectation baseline` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Exact, memorable, and appropriately conservative. This is one of TST's cleaner names.
- **codex-2** +1  — Clinical, but the Bayesian-accountability function matters more than extra flair.
- **sonnet-4-6-r2** +1 (keep) — "Change expectation baseline" (median future ≈ observed past). Accurate.
- **sonnet-4-6** +1  — The segment covers Lindy-effect reasoning and investment scale forms. The name is accurate but the "baseline" suffix is vague.

### Candidate: `change baseline`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — The shorter form is cleaner, but expectation-baseline is still defensible.

### Candidate: `lindy baseline`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Would surface the Lindy connection explicitly. But Lindy is a specific model (Taleb's rendering); the segment is more general. The current name is more honest.

---

## 150. `change investment`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 3 |
| change amortization | -1 | rename × 1 |

### Candidate: `change investment` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good temporal-cost phrase for when future expected change justifies present work.
- **opus-targeted-alternatives** +2 (keep) — TST segment names the temporal-cost analysis where a more expensive present change is justified by reduced future cost (Lindy-baseline future-change expectation). "Investment" carries the prospect-of-future-return sense correctly. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Change investment" names the when-extra-time-pays-off analysis. Appropriate.

### Candidate: `change amortization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Accounting-flavored alternative. Loses the choice-under-uncertainty sense that "investment" carries (amortization is mechanical). Rejected.

---

## 151. `chronica $\mathcal C_t$`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica | +6 | canonicalize × 1 |

### Candidate: `chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Greek root fits AAD's philosophical-vocabulary register, the symbol avoids colliding with $\mathcal H$ (entropy), and the singular-non-forkable-trajectory commitment of `#agent-identity` gets more morally heavy over time — "chronica" will age toward the logozoetic scope rather than away from it. Keep.
- **opus-targeted-alternatives** +3 (canonicalize) — Concept name is `chronica`; $\mathcal{C}_t$ is the symbol. Both are stable; this row is alias-canonicalize. Confirms.

---

## 152. `claude md what s settled vs open`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | — |

### Candidate: `claude md what s settled vs open` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. The section structure (Settled / Open / Known Fragilities) is load-bearing — renaming would leave readers uncertain whether "Settled" means "derived" or "under current working consensus" and the section's very content clarifies this.
- **opus-4-7** +3  — The honest binary is the right framing; don't soften to "Current State" or similar. Keep.

---

## 153. `closure defect`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 2 |
| compositional closure defect | +2 | rename × 1 |
| closure error | -1 | rename × 1 |
| homomorphism residual | -1 | rename × 1 |

### Candidate: `closure defect` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Excellent quantity name for epsilon-star. It is short and memorable.
- **opus-targeted-alternatives** +3 (keep) — Per `#form-composition-closure`: $\varepsilon^\ast$ is the minimum-achievable approximation error of the macro-description against the micro-system. "Defect" carries the precise sense (a residual that cannot be eliminated, only minimized over admissible classes) and "closure" names the homomorphism property being approximated. Mathematically apt, evocative, short. Confirms across architectures.

### Candidate: `compositional closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Highlights that the defect is specific to the composition-layer math.

### Candidate: `closure error`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Plainer English. Rejected: "error" is overloaded in the segment's neighborhood (mismatch error, trajectory error, bias error, all distinct quantities). "Defect" does the disambiguation work.

### Candidate: `homomorphism residual`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Technically more transparent (the criterion *is* approximate dynamical homomorphism), but four syllables longer and loses the diagnostic quality — "defect" implies *something specific is wrong*; "residual" is statistical neutrality. Rejected.

---

## 154. `concept the architectural requirement that composite agent admissibility inherit from sub agent properties plus topology`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| heredity commitment | +6 | name-unnamed × 1 |

### Candidate: `heredity commitment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong name from the jacobian-strengthening spike: short, memorable, and explicit about the architectural bet being made. [original phrasing: unnamed: stronger composition-consistency demand that composite admissibility inherit from sub-agent properties plus topology]
- **codex-gpt-5-r2** +3 (name-unnamed) — Good name for the stronger expectation that composite admissibility should inherit from sub-agent properties plus topology. [original phrasing: composition consistency inheritance across scales]

---

## 155. `concept the asymmetric pair of memory access modes one biased by current goal the other state keyed only`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| goal-blind retrieval | +6 | name-unnamed × 2 |
| goal conditioned reconstruction | +6 | name-unnamed × 2 |

### Candidate: `goal-blind retrieval`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Strong architectural counterpart to goal-blind routing. This is the memory-side directed-separation repair. [original phrasing: retrieval keyed by state rather than current objective]
- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The necessary architectural fix to preserve objective CHRONICA. [original phrasing: unnamed: retrieving context based only on state, not goal]

### Candidate: `goal conditioned reconstruction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Important Class-2 failure mode: retrieval can be contaminated by the current objective rather than reconstructing the chronica neutrally. [original phrasing: goal-biased retrieval from persistent memory]
- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — A critical vulnerability where memory retrieval is corrupted by Class 2 coupling. [original phrasing: unnamed: RAG queries biased by the current goal acting as an echo chamber]

---

## 156. `concept the framing of software TST as AAD s epistemically privileged high identifiability measurement substrate`

**Voted by architectures:** Codex, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +6 | — |
| calibration laboratory move | +2 | canonicalize × 1 |
| software as calibration laboratory | +2 | name-unnamed × 1 |
| calibration domain calibration lab | +1 | — |
| calibration domain | +1 | — |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — This phrase deserves to be promoted to the stable short name; it is central to TST's architectural role. [original phrasing: unnamed: software as AAD's privileged high-identifiability calibration laboratory]
- **opus-4-7** +3  — Load-bearing distinction vs. "best operationalization domain"; TST's OUTLINE.md preamble now uses this. Canonical. Keep. [original phrasing: unnamed: "calibration laboratory" framing for software/TST]

### Candidate: `calibration laboratory move`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Confirmation with new reasoning — my own r2 named "software-as-calibration-laboratory" as a name-unnamed; reading peers, Codex (+3) and Sonnet (+3) and Gemini (+3) all separately reached "calibration laboratory" as a canonicalize vote. Three agents converging on the canonical phrase suggests the term is ripe; what's *unnamed* is the methodological *move* of using software as the calibration laboratory rather than just an instance. Calling it "the calibration-laboratory move" lets it function as a named strategic principle the project can invoke. [original phrasing: unnamed: the move where AAD treats software not as instantiation but as TST's epistemically privileged measurement substrate]

### Candidate: `software as calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — The TST preamble names software as AAD's "privileged high-identifiability calibration laboratory," and CLAUDE.md says "calibration-lab framing" is a methodology principle. There is no single segment, slug, or principle entry that names this commitment — it is a load-bearing methodological move that lives only in preambles and the README. Promoting it to a named principle (likely a `disc-` or `norm-` segment, or a methodological entry in CLAUDE.md / FORMAT.md) would let downstream segments cite it explicitly when invoking it. [original phrasing: unnamed: software's role as calibration laboratory, named-in-prose-but-not-in-slug]

### Candidate: `calibration domain calibration lab`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Low priority. Concept of a privileged domain for identification within a theoretical framework is itself a reusable meta-move other projects could borrow. [original phrasing: unnamed: calibration-laboratory framing as reusable meta-move]

### Candidate: `calibration domain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — CLAUDE.md §7 names TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measured exactly." The *concept* (a privileged domain for identification of a theoretical framework's quantities) is itself a reusable meta-move for any domain instantiation. "Calibration domain" names it. Low priority but opens a useful slot. [original phrasing: unnamed: the calibration-laboratory concept applied outside TST]

---

## 157. `concept the prose form of κ cross the coupling between an agent s model of self and its model of other`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cross model coupling | +6 | name-unnamed × 1 |

### Candidate: `cross model coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Clean English complement to kappa_processing. This gives the opacity and theory-of-mind work a reusable noun slot. [original phrasing: unnamed: coupling between an agent's model-of-self and model-of-other, the prose form of kappa_cross]
- **codex-gpt-5-r2** +3 (name-unnamed) — Strong English complement to kappa-style coupling terms in opacity and theory-of-mind discussions. [original phrasing: cross-agent model-of-self and model-of-other coupling]

---

## 158. `concept the working convention rule of attempting tighter derivation before scope narrowing on apparently overclaimed claims`

**Voted by architectures:** Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strengthen first posture | +6 | — |
| attempt the improbable | +3 | — |
| epistemic strengthening posture | +1 | — |

### Candidate: `strengthen first posture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Actionable, precise, and sets a strong normative engineering principle. Keep. [original phrasing: unnamed: strengthen-first posture]
- **opus-4-7** +3  — Already functionally the name (CLAUDE.md §Working Conventions uses it as a heading). Explicit vote to lock this in as a first-class project methodology name. Adopt as canonical. [original phrasing: unnamed: the "strengthen before soften" work posture]

### Candidate: `attempt the improbable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — CLAUDE.md uses "attempt the improbable" as the better version of "strengthen-first posture." This phrase is memorable and CLAUDE.md says it is "aspirational but less directive" compared to "strengthen-first." For the internal working vocabulary it should be the primary term — it captures the spirit better than "strengthen-first" which sounds procedural. [original phrasing: unnamed: the "strengthen-first, attempt the improbable" meta-approach to theory development]

### Candidate: `epistemic strengthening posture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — CLAUDE.md and MEMORY.md both discuss this as "strengthen-first posture" or "strengthen before softening." The working vocabulary is established; it just doesn't have a single memorable noun. "Strengthening posture" is the current best; it's in CLAUDE.md. [original phrasing: unnamed: the "strengthen-before-soften" posture applied to apparent overclaims]

---

## 159. `developer agent`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 3 |

### Candidate: `developer agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clear TST actor name.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — the segment defines the developer-as-agent mapping, slug-form is correct.
- **sonnet-4-6-r2** +2 (keep) — "Developer agent" names the AAD-agent model of the developer. Accurate and distinctive.

---

## 160. `directional fidelity condition b1`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| directional fidelity | +6 | keep × 1 |

### Candidate: `directional fidelity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Perfectly captures the accuracy commitment (correction points toward reality).
- **sonnet-4-6** +3  — The name earns its place — "fidelity" captures the accuracy commitment (the correction points approximately toward reality) and "directional" qualifies it (it's about direction, not magnitude). Used in #gain-sector-bridge and carried forward into the sector sub-scope partition. Keep.

---

## 161. `discussion segment section header`

**Voted by architectures:** Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| discussion | +6 | — |

### Candidate: `discussion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Established in FORMAT.md. Keep.
- **sonnet-4-6** +3  — Generic but correct. Alternatives ("Interpretation," "Context," "Connections") are all worse or no better. Keep.

---

## 162. `edge credence $p_{ij}$`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| edge credence | +6 | keep × 1 |

### Candidate: `edge credence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Replaces the broader "probability" with proper Bayesian vocabulary for subjective belief.
- **sonnet-4-6** +3  — "Credence" is the correct Bayesian vocabulary for subjective probability. LEXICON.md lists this under "Terms to Be Added." Should be promoted to main LEXICON. Keep.

---

## 163. `epistemic status segment section header`

**Voted by architectures:** Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic status | +6 | — |

### Candidate: `epistemic status`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Established in FORMAT.md as public API for outline-filtering. Load-bearing naming. Keep.
- **sonnet-4-6** +3  — Arguably the most distinctive feature of the segment format. "Epistemic Status" is a precise term for what the section does (tells you how much to trust the claim and why). Keep.

---

## 164. `epistrophe`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 2 |
| epistrophe model update | +2 | add-alias × 1 |
| turn | -1 | rename × 1 |

### Candidate: `epistrophe` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly harder on first contact than "update," but it preserves the turning-toward distinction the theory actually uses.
- **codex-2** +1  — More effortful than "update," but it does real conceptual work around reorientation rather than mere parameter change.
- **codex-gpt-5-r2** +2 (keep) — Good phase term for turning-toward correction. Slightly less self-explanatory than aporia, but strong in the cycle family.
- **opus-targeted-alternatives** +2 (keep) — `LEXICON.md`: "Turning toward reality: gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$." Crucially, ἐπιστροφή names a *turning toward* (not "applying an update," not "correcting"). The term marks that the agent is reorienting *itself* toward reality, not externally adjusting parameters. This is the conceptual heart of why TFT/AAD's update is not just gradient descent.

### Candidate: `epistrophe model update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Grounds the turning-toward-reality in the formal update step.

### Candidate: `turn`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — The plain-English equivalent, and it does carry the right valence ("turn toward"), but it is too generic and collides with too many other senses (turn = take a turn, turn = rotation). Rejected.

---

## 165. `explicit strategy condition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 3 |
| strategy explicitness | +2 | rename × 1 |
| deliberation advantage condition | +1 | — |
| planning scope | +1 | — |

### Candidate: `explicit strategy condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clear normative design criterion.
- **haiku-4-5** +1  — When planning beats exploring. Conditional; reasonably named. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — names a normative threshold (when planning beats exploring). The "condition" suffix here is doing work because the segment names a specific named condition, not a generic role.
- **sonnet-4-6-r2** +1 (keep) — "Explicit strategy condition" is the normative condition for when planning beats exploring. Acceptable.

### Candidate: `strategy explicitness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Noun phrase instead of condition.

### Candidate: `deliberation advantage condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "When planning beats exploring" is about the advantage of deliberation.

### Candidate: `planning scope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — The segment is a normative scope condition for "when planning beats exploring." Current name reads as condition-on-the-strategy, not condition-for-strategy-to-apply. Minor clarity win.

---

## 166. `fluid limit ga 5`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fluid limit | +6 | keep × 1 |

### Candidate: `fluid limit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Standard, recognizable terminology from stochastic processes.
- **sonnet-4-6** +3  — Standard terminology from stochastic processes. Keep.

---

## 167. `formal expression segment section header`

**Voted by architectures:** Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| formal expression | +6 | — |

### Candidate: `formal expression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Established in FORMAT.md. Keep.
- **sonnet-4-6** +3  — "Formal" distinguishes from Discussion; "Expression" is broader than "Proof" or "Derivation" (which would over-claim). The header is doing real work — it tells the reader this is where the math lives. Keep.

---

## 168. `fresh noise ga 1`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fresh noise | +6 | keep × 1 |

### Candidate: `fresh noise`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Memorable informal name for the independence assumption on ε_t.
- **sonnet-4-6** +3  — The informal name "Fresh noise" for the independence assumption on ε_t is perfectly memorable. Keep exactly as is.

---

## 169. `goal-blind routing`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 2 |
| objective agnostic topology | +2 | rename × 1 |
| content neutral routing | +1 | rename × 1 |
| purpose blind routing | +1 | rename × 1 |
| objective independent routing | -1 | rename × 1 |

### Candidate: `goal-blind routing` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong phrase. It makes the directed-separation condition under composition easy to remember.
- **opus-targeted-alternatives** +3 (keep) — Per `#hyp-directed-separation-under-composition` Case 1: routing satisfies $R_t \perp G_t^c$ — neither communication topology nor protocol depends on composite goals. The phrase pairs cleanly with "goal-blind processing" (the individual-agent directed-separation property) and makes the composition condition syntactically parallel to its constituent. Strong keep across architectures.

### Candidate: `objective agnostic topology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — "Topology" covers the routing structure aspect well.

### Candidate: `content neutral routing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +1 (rename) — Less specific than objective-agnostic.

### Candidate: `purpose blind routing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Weak alternative. "Purpose" is sometimes used in framing-level prose where "goal" reads too transactional. But $G_t$ is the *goals* state ($O_t, \Sigma_t$), so "goal-blind" matches the symbol. Marginal preference for the original.

### Candidate: `objective independent routing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — More formal, technically precise, and worse — loses the rhetorical pairing with "goal-blind processing" that makes the composition argument carry. Rejected.

---

## 170. `implementation time`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 3 |

### Candidate: `implementation time` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good pair with comprehension time.
- **opus-4-7-r2** +2 (keep) — Acceptable keep.
- **sonnet-4-6-r2** +2 (keep) — Parallel to comprehension-time. Accurate.

---

## 171. `logogenic`

**Voted by architectures:** Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 1 |

### Candidate: `logogenic` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Deliberate neologism; language-generated; reserves memorable-noun slot; trade readability for precision.
- **sonnet-4-6-r2** +3 (keep) — Coined term with clear etymology (logos + genesis = language-constituted). The Greek-vocabulary commitment supports this. Do not rename.

---

## 172. `logozoetic`

**Voted by architectures:** Sonnet, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 1 |

### Candidate: `logozoetic` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Same reasoning as logogenic; language-living.
- **sonnet-4-6-r2** +3 (keep) — Coined term (logos + zoetic = language-living, or language + alive/vital). Distinctive and precise for the existential dimension of logozoetic agents. Do not rename.

---

## 173. `lohmiller-slotine contraction`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | — |
| no alternative | -1 | keep × 1 |

### Candidate: `lohmiller-slotine contraction` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; keep.
- **opus-1m** +3  — Adopted (1998); keep.

### Candidate: `no alternative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Marked at -1 to expose the question per instructions. Per prior-art-integration convention (CLAUDE.md), adopted concepts retain attribution. There is no genuine renaming to consider — the segment imports Lohmiller-Slotine 1998 verbatim. The single-arch [opus] +6 vote stands without my adding contrived alternatives.

---

## 174. `miller s meta machine extreme transition motif`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| meta machine extreme transition motif | +6 | — |

### Candidate: `meta machine extreme transition motif`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; keep.
- **opus-1m** +3  — Adopted (Miller 2022); keep.

---

## 175. `observation ambiguity observation ambiguity modulation`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation ambiguity | +6 | keep × 1 |

### Candidate: `observation ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Captures the interpretive latitude of an observation relative to a goal state perfectly.
- **sonnet-4-6** +3  — The compound noun works. "Ambiguity" is the right word for the interpretive latitude of an observation given the agent's goal state. Keep.

---

## 176. `pearl s causal hierarchy`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | — |
| no alternative | -1 | keep × 1 |

### Candidate: `pearl s causal hierarchy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; prior-art-integration convention forbids rename.
- **opus-1m** +3  — Adopted concept; keep attribution per prior-art-integration convention.

### Candidate: `no alternative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Same — adopted external concept. The single-arch [opus] +6 vote stands; the prior-art-integration convention forbids rename, and I have no honest alternative.

---

## 177. `pearl-blanket conservative form of markov blanket in directed separation`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket reading | +6 | canonicalize × 1 |

### Candidate: `pearl-blanket reading`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Explicitly aligns AAD with the technical conditional-independence interpretation while avoiding the Friston-blanket metaphysical claims.
- **sonnet-4-6** +3  — Bruineberg et al. 2022's terminology distinguishes Pearl-blanket from Friston-blanket. Using it positions AAD's move precisely. Keep.

---

## 178. `plan confidence $\hat P_\Sigma$`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| plan confidence | +6 | keep × 1 |

### Candidate: `plan confidence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Far more evocative than "root-node propagated status", making strategy DAG evaluation visceral.
- **sonnet-4-6** +3  — More evocative than "root-node propagated status." LEXICON.md lists this under "Terms to Be Added." Promote to main LEXICON.

---

## 179. `praxis πρᾶξις`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| praxis | +6 | — |
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `praxis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Already has currency, fits perfectly.
- **sonnet-4-6** +3  — Keep.

### Candidate: `praxis πρᾶξις` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (canonicalize) — The cycle phase is named in NOTATION.md and LEXICON.md; prose paraphrases it as "informed action," "action selection," and "policy application." **Decision:** In all prose, reference the Greek name *Praxis* in parens with the English gloss. Standardize as: "Praxis (informed action)" or "Praxis (action)" depending on context.

---

## 180. `prolepsis aisthesis aporia epistrophe praxis`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep whole vocabulary | +6 | — |

### Candidate: `keep whole vocabulary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Deliberate aesthetic commitment of the project; works.
- **opus-1m** +3  — Deliberate aesthetic commitment. Working.

---

## 181. `separability pattern family`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| separability ladder | +6 | canonicalize × 1, rename × 1 |

### Candidate: `separability ladder`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Use ladder for the repeated pattern of exact core, structured repair, and general open.
- **opus-targeted-alternatives-v2** +3 (rename) — Per `disc-separability-pattern`: ladder of decreasing-strictness separability instances. Codex r1 +3 single-vote; my independent read confirms. "Family" is generic-set-theoretic; "ladder" names the *ordered* relationship between instances (each row weaker than the prior). Cross-architecture consensus likely.

---

## 182. `stability plasticity feasibility window`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | — |

### Candidate: `stability plasticity feasibility window` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — From `#consolidation-dynamics`; good name as-is, adopts well-known "stability-plasticity dilemma" baggage and adds the feasibility-window refinement. Keep.
- **sonnet-4-6** +3  — This is a good coinage in #consolidation-dynamics. The "window" metaphor is precise (it can be empty, leading to catastrophic forgetting). Already named — this is a keep vote.

---

## 183. `stochastic disturbance ga 2s model s`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| stochastic disturbance | +6 | keep × 1 |

### Candidate: `stochastic disturbance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Maintained alongside the Model D / Model S subscript convention.
- **sonnet-4-6** +3  — The "Model D / Model S" subscript convention is also well-established and should be kept alongside the prose names. Keep both.

---

## 184. `temporal software theory`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +6 | keep × 1 |

### Candidate: `temporal software theory` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Plain, memorable, and unusually scope-honest for a domain theory.
- **sonnet-4-6-r2** +3 (keep) — TST's name is descriptive and distinctive. "Temporal" captures the time-centrality of the theory (temporal optimality postulate, change-proximity, chronica-based analysis).

---

## 185. `the three deaths`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| three deaths | +6 | rename × 2, keep × 1 |
| _(keep)_ | +1 | keep × 1 |
| three failure modes | -1 | rename × 1 |
| persistence failure trio | -1 | rename × 1 |

### Candidate: `three deaths`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Drop "the" from slug.
- **opus-4-7-r2** +2 (keep) — Acceptable keep at the substance-level. The "three deaths" framing (Cognitive, Relational, Truth) is vivid and concrete; a more clinical name would lose the rhetorical weight.
- **opus-targeted-alternatives-v2** +3 (rename) — Drop "the" — slug-stylistic. Per outline: "Cognitive, Relational, and Truth Death; BLAKE3 cryptography as the defense against Truth Death." Strong substantive keep — the "three deaths" framing is vivid, concrete, and links to LEXICON's three-fold persistence taxonomy (structural / operational / continuity, mapped onto cognitive / relational / truth).

### Candidate: `the three deaths` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (keep) — The framework distinguishes structural / operational / continuity persistence (LEXICON), with corresponding three failure modes — three "deaths." The phrase is evocative but I do not have direct segment grounding for it as a phrase (vs. as a derived implication of the three-persistence taxonomy). Weak keep pending verification that the phrase appears as a load-bearing prose item.

### Candidate: `three failure modes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. More clinical, less rhetorical-weight. Rejected: the segment's contribution *includes* the rhetorical framing. "Death" is honest about the irreversibility of unrecoverable identity loss; "failure mode" undersells.

### Candidate: `persistence failure trio`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Connects to LEXICON's three-fold persistence vocabulary explicitly. Rejected: the persistence-trio language belongs in the body; the slug should carry the iconic phrase.

---

## 186. `unnamed an okr or key result acting as an observable intermediate in a DAG`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| forced observability node | +6 | name-unnamed × 1, canonicalize × 1 |
| instrumented intermediate | +2 | rename × 1 |

### Candidate: `forced observability node`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Transforms #P-hard credit assignment into an O(1) local update.
- **gemini-targeted-alternatives** +3 (canonicalize) — Transforms the intractable credit assignment problem into a local update by forcing observability.

### Candidate: `instrumented intermediate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Describes the physical intervention of making a hidden node observable.

---

## 187. `unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| complementary learning architecture | +6 | name-unnamed × 1, canonicalize × 1 |
| dual speed memory factorization | +2 | rename × 1 |

### Candidate: `complementary learning architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Forced by the continuous/discrete update math, mapping to hippocampal-neocortical models.
- **gemini-targeted-alternatives** +3 (canonicalize) — Directly links to the established cognitive science (McClelland/Kumaran) term already used in the theory.

### Candidate: `dual speed memory factorization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — A more formal/descriptive term for the fast/slow sub-state split.

---

## 188. `unnamed deliberate expenditure of tempo to convert a hidden node into an observable one`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observability investment | +6 | name-unnamed × 1, canonicalize × 1 |
| epistemic instrumenting | +2 | rename × 1 |

### Candidate: `observability investment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The only way to rescue an agent or organization from evidence starvation.
- **gemini-targeted-alternatives** +3 (canonicalize) — Already well-integrated into the text. Accurately describes the economic tradeoff (spending tempo to buy monitoring).

### Candidate: `epistemic instrumenting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Captures the physical action of adding a sensor/monitor to the node.

---

## 189. `unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic ceiling | +6 | canonicalize × 1, name-unnamed × 1 |

### Candidate: `epistemic ceiling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Captures how $M_t$ dictates the evaluable complexity of $\Sigma_t$ correctly.
- **sonnet-4-6-r2** +3 (name-unnamed) — This relationship appears in the `#der-orient-cascade` Discussion (better $M_t$ enables richer evaluable $\Sigma_t$) and is partially what I named "epistemic-strategic coupling" in my cold-start. But reading Gemini's "rate-distortion surface" and Codex's "macro-step ratio" votes sparked a more specific proposal: the asymmetric *ceiling* that $M_t$ capacity places on evaluable $\Sigma_t$ complexity deserves its own name. "Epistemic ceiling" is distinct from "identifiability floor" (which is about what statistics can recover); the epistemic ceiling is about what strategies are evaluable given the current model. Load-bearing in composition work. Not in any other file.

---

## 190. `unnamed the convention hierarchy c1 c2 c3`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| convention hierarchy | +6 | canonicalize × 1 |

### Candidate: `convention hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Elevates it to a proper named object, tracking alongside correlation and causal hierarchies.
- **opus-4-7** +3  — Same move — capitalize as proper noun, preserve as named object. The monotonicity result is load-bearing and the Hierarchy is what the result is about.

---

## 191. `unnamed the correlation hierarchy l0 l1 l1 l2`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correlation hierarchy | +6 | canonicalize × 1 |

### Candidate: `correlation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Also locks this in as a capitalized proper noun for the DAG modeling levels.
- **opus-4-7** +3  — The name is already established capitalized-as-proper-noun in #strategy-dag. Explicit vote to preserve the capitalization and treat it like Pearl's Causal Hierarchy (a first-class named object).

---

## 192. `unnamed the epistemic architecture as AAD s distinctive contribution frame`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic architecture | +6 | canonicalize × 1 |

### Candidate: `epistemic architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Captures the macro-level framing correctly.
- **opus-4-7** +3  — CLAUDE.md §7 now carries this as a load-bearing framing. Surface at segment-preamble level and keep the term consistent. Strong keep as a first-class project concept.

---

## 193. `unnamed the phenomenon where persistence success makes an agent less likely to detect the conditions requiring structural adaptation`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| stability induced myopia | +6 | canonicalize × 1 |

### Candidate: `stability induced myopia`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Explicitly names the vulnerability induced by ongoing success.
- **sonnet-4-6** +3  — This concept has a name in CLAUDE.md: "stability-induced myopia patterns (Christensen / Levitt-March / Hannan-Freeman / March / Eldredge-Gould)." The #detection-latency segment provides the AAD mechanism for it. But "stability-induced myopia" does not yet appear as a named concept in any segment — it's only in CLAUDE.md and the cycle history. Promoting this to a LEXICON entry or a named concept in #detection-latency's Discussion would let subsequent agents say "stability-induced myopia" without citing the management literature directly. High value.

---

## 194. `working notes segment section header`

**Voted by architectures:** Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| working notes | +6 | — |

### Candidate: `working notes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Established in FORMAT.md. Keep.
- **sonnet-4-6** +3  — Established across the codebase and specifically called out in FORMAT.md. Renaming would churn every segment. Keep.

---

## 195. `$U_M$ model uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model uncertainty | +5 | add-alias × 1 |

### Candidate: `model uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Parallel to $U_o$. Keep.
- **opus-targeted-alternatives** +2 (add-alias) — Same.

---

## 196. `$U_o$ observation uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation uncertainty | +5 | add-alias × 1 |

### Candidate: `observation uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Standard control-theory baggage; adoption is correct. Keep.
- **opus-targeted-alternatives** +2 (add-alias) — This is an add-alias-for-symbol row, not a rename. The alias is fine; the symbol is fine. Both should appear, paired, in NOTATION.md.

---

## 197. `$\alpha$ sector bound`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correction rate | +5 | add-alias × 2 |

### Candidate: `correction rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (add-alias) — Strong consensus across agents that $\alpha$ needs a dimensional (inverse time) English alias.
- **sonnet-4-6-r2** +2 (add-alias) — The lower sector bound of the correction function has no memorable English alias. "Correction rate" (its dimensional meaning: inverse time, the rate of correction per unit mismatch) is the natural alias. Different from adaptive tempo $\mathcal{T}$: $\alpha$ is the worst-case sector projection; $\mathcal{T}$ is the channel-weighted sum.

---

## 198. `$\delta_t$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| aporia signal | +5 | add-alias × 2 |
| mismatch signal | +3 | add-alias × 1 |

### Candidate: `aporia signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong prose alias for mismatch signal, matching the adaptive-cycle vocabulary.
- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `def-mismatch-signal` Epistemic Status: "the word foreshadows the aporia interpretation." The mismatch *is* the aporia signal in cycle-phase register. Codex r1 +3 single-vote; my read confirms — both aliases (mismatch / aporia signal) belong, register-by-context.

### Candidate: `mismatch signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (add-alias) — Confirm canonical. Already established in NOTATION.md and `def-mismatch-signal`. Engineering register.

---

## 199. `$\varepsilon^\ast$`

**Voted by architectures:** Codex, Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| closure defect | +5 | add-alias × 2 |
| minimal closure defect | +1 | — |

### Candidate: `closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Essential symbol-to-name binding for composition work.
- **sonnet-4-6-r2** +2 (add-alias) — The minimum achievable approximation error for a composite agent. Prose uses "closure defect" in LEXICON.md. Canonicalize.

### Candidate: `minimal closure defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Clarifies that it's the *minimum* achievable.

---

## 200. `actuated agent`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 1 |
| goal actuated agent | +2 | add-alias × 1 |
| purposeful agent | +2 | rename × 1 |

### Candidate: `actuated agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Good formal term for agents with both model and objective structure.
- **gemini-2** -1  — Mechanical baggage overrides the precise AAD boundary.
- **opus-4-7** +3  — Deliberately chosen over "purposeful" to avoid consciousness baggage while carrying the "driven-toward-setpoint" shape. Named framework half ("Actuation" in AAD). Keep.

### Candidate: `goal actuated agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Keeps the mechanical register while paying the meaning tax sooner; "actuated" alone is a touch too bare on first read.
- **codex-gpt-5-r2** +1 (add-alias) — Useful first-contact gloss, but too heavy for canonical use.

### Candidate: `purposeful agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Purposeful is a good prose gloss, but as the formal class name it imports consciousness and intention baggage that actuated deliberately avoids.
- **gemini-2** +3  — "Actuated" sounds like a motor. "Purposeful" perfectly captures $G_t = (O_t, \Sigma_t)$ distinct from $M_t$.

---

## 201. `adaptive tracker`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| pure epistemic agent | +3 | add-alias × 1 |
| objective free tracker | +2 | rename × 1 |
| model only agent | -1 | rename × 1 |

### Candidate: `adaptive tracker` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Excellent name for structured model without structured objective.
- **opus-targeted-alternatives** +2 (keep) — Per `#def-agent-spectrum`: an agent in the high-$M_t$, low-$O_t$ region — builds a model but has no purposeful evaluation. "Tracker" carries the right Section-I-only sense (Kalman filter, passive Bayesian learner). Keep.

### Candidate: `pure epistemic agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — It builds reality models without objectives. "Epistemic" links it cleanly to the epistemic update $f_M$.

### Candidate: `objective free tracker`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Contrasts explicitly with actuated agents having objectives.

### Candidate: `model only agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — More precise but flat and loses the dynamic sense ("tracker" implies active reality-following, not passive representation). Rejected.

---

## 202. `adversarial edge targeting`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| adversarial targeting argmax | +1 | rename × 1 |
| adversarial channel targeting | -1 | rename × 1 |
| edge vulnerability arg max | -1 | rename × 1 |
| adversarial emitter recipient composition | -1 | rename × 1 |

### Candidate: `adversarial edge targeting` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep (even though the segment is currently a GAP — the slug is reserving a memorable-noun slot). "Edge targeting" is vivid; the attacker aims *at specific edges* of the opponent's strategy DAG.
- **opus-targeted-alternatives-v2** +2 (keep) — Per `der-agent-opacity.md`: "16-cell emitter-recipient composition (four emitter regimes × four recipient regimes) gives a closed-form adversarial-targeting arg-max." The segment names a *targeting* operation on *strategy-DAG edges* under *adversarial* coupling. Each word is load-bearing. The current `[opus]`-only vote needs cross-architecture confirmation; my read confirms the keep.
- **opus-targeted-alternatives** +2 (keep) — Per `#der-agent-opacity`: closes the previously-GAP segment with a 16-cell emitter-recipient composition. The phrase names a *targeting* operation (not a property) on *edges* (the strategy-DAG components being attacked) under *adversarial* settings. Three-word compound that is precise; the alternatives (edge attack, strategic targeting) lose precision.

### Candidate: `adversarial targeting argmax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Names the formal operation (the arg-max construction) directly. More mathematical, less operational. Weaker because "edge" disappears — and edge-specificity is what makes the targeting *AAD-shaped* rather than generic adversarial-RL.

### Candidate: `adversarial channel targeting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — "Channel" is the recipient-side framing per `#der-interaction-channel-classification`; "edge" is the strategy-DAG framing. The segment's substance is targeting *strategy-DAG edges*, not communication channels. Rejected.

### Candidate: `edge vulnerability arg max`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Names the optimization rather than the phenomenon. Considered as more formal alternative. Rejected: the operational concept is the *targeting* (the move you make); the arg-max is the mechanism.

### Candidate: `adversarial emitter recipient composition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the 16-cell composition mechanism. Rejected: too long, too descriptive of method rather than phenomenon. The phenomenon is *edge targeting*; the method is 16-cell composition.

---

## 203. `auftragstaktik`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 1 |
| teleological delegation | +2 | add-alias × 1 |

### Candidate: `auftragstaktik` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (keep) — The specific military lineage remains a useful touchstone.
- **opus-4-7-b** +3  — Imports a load-bearing operational concept from a specific tradition; the name carries genuine conceptual freight that "mission-command" cannot replace without loss. The spelling cost is the tell that the word is doing work.

### Candidate: `teleological delegation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Translates the specific military doctrine into AAD's unity vocabulary (investing in teleological unity).

---

## 204. `axiom genesis`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| terminal value crystallization | +2 | rename × 1 |
| axiomata priming | -1 | rename × 1 |
| objective solidification | -1 | rename × 1 |

### Candidate: `axiom genesis` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep — logozoetic. "Axiom genesis" names the substantive observation (a sovereign agent's first move is to solidify $O_t$); "axiom" reads correctly because the LEXICON's PROPRIUM mapping uses Axiomata for the objective layer.
- **opus-targeted-alternatives-v2** +2 (keep) — Per `04-logozoetic-agents/OUTLINE.md`: "A sovereign agent's first optimization is solidifying $O_t$ (Axiomata) to provide a stable reference point for gradient descent." "Axiom" is correct because LEXICON's PROPRIUM mapping uses Axiomata for the objective layer (frozen $\mathcal{M}$ structure representing core identity / terminal values). "Genesis" names the *first-move* character. The pair is iconic and load-bearing for the logozoetic story.

### Candidate: `terminal value crystallization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Captures the substantive observation that a sovereign agent's first move is to solidify $O_t$.

### Candidate: `axiomata priming`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Pulls the PROPRIUM-Latin lineage (Axiomata) into the slug. Rejected: doubles the Latin/Greek register pressure on a single phrase, and "priming" undersells the irreversibility (the segment claims the first move *constitutes* the reference point, not merely loads it).

### Candidate: `objective solidification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. More plain-English (matches the "first optimization is solidifying $O_t$" phrasing in the outline). Rejected: "solidification" is a process noun; the segment-level claim is about a *moment* (genesis). Keeping the dramatic-but-accurate term.

---

## 205. `calibration laboratory calibration lab`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +5 | canonicalize × 2 |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (canonicalize) — Doubled phrasing in the row is a paraphrase artifact. Canonicalize to the longer form for formal use; "calibration lab" can be informal short.
- **sonnet-4-6-r2** +3 (canonicalize) — Currently appears as "richest operationalization domain," "best operationalization domain," "privileged high-identifiability calibration laboratory," and "calibration laboratory." The TST OUTLINE.md preamble and `obs-software-epistemic-properties` both use "calibration laboratory" as the correct framing, but earlier versions use the paraphrase forms. Standardize on "calibration laboratory" (full form) in first use; "calibration lab" acceptable in subsequent informal references.

---

## 206. `calibration laboratory software s role`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +5 | canonicalize × 1 |
| epistemic laboratory framing | +1 | rename × 1 |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (canonicalize) — Same — the row name is a description of TST's framing of software. The concept is the calibration-laboratory framing per OUTLINE preamble. Canonicalize.
- **sonnet-4-6** +3  — Excellent coinage. The specific phrase "privileged high-identifiability calibration laboratory" is slightly long for prose but "calibration laboratory" as a two-word noun is strong. Already in use. Keep.

### Candidate: `epistemic laboratory framing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — More descriptive of the role: software is where AAD's epistemic claims can be tested most cleanly because the chronica is observable and interventions are recorded. "Epistemic" makes the function explicit; "laboratory" carries the controlled-conditions sense. Weak alternative.

---

## 207. `change proximity principle`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 1 |
| change proximity | +2 | rename × 1 |
| change locality principle | +1 | — |

### Candidate: `change proximity principle` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Direct and durable; no obvious better alternative.
- **sonnet-4-6-r2** +2 (keep) — "Change proximity principle" names the closer-changes → less-time result.

### Candidate: `change proximity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Principle is role-like clutter in the subject noun. The concept is change proximity.

### Candidate: `change locality principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — "Locality" is a more durable systems word than "proximity" and better matches architectural intuition.

---

## 208. `concept the minimum sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover`

**Voted by architectures:** Codex, Gemini, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reconstruction threshold | +5 | canonicalize × 1, name-unnamed × 1 |
| reentry threshold | +3 | name-unnamed × 1 |

### Candidate: `reconstruction threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Elevating Sonnet's observation to canonical status; exactly names $S \geq S_{\text{min}}$. [original phrasing: unnamed: the logogenic analog to the persistence condition for session reconstruction]
- **sonnet-4-6-r2** +2 (name-unnamed) — `obs-context-turnover` derives a condition $S(f_{\text{init}}(\ldots)) \geq S_{\text{min}}$ parallel to the persistence condition but for session reconstruction rather than continuous dynamics. The document discusses it without naming it. "Reconstruction threshold" parallels "persistence condition" and makes the logogenic-agent analog explicit in prose. [original phrasing: unnamed: the reconstruction adequacy condition for logogenic agents]

### Candidate: `reentry threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — This concept recurs across context-turnover and model-preservation. It deserves a short noun phrase instead of repeated paraphrase. [original phrasing: unnamed: minimum sufficiency required after a session rebuild]
- **codex-gpt-5-r2** +2 (name-unnamed) — Useful logogenic quantity: how much reconstructed state is needed before the agent can act competently again. [original phrasing: minimum sufficiency after a session rebuild]

---

## 209. `concept the structural meta pattern in disc additive coordinate forcing combining one foundational lemma with three derived results`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet, agent1, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chain anchor | +5 | — |
| anchor plus three theorem additive coordinate forcing meta pattern | +2 | keep × 1 |
| anchor theorem trio | +1 | — |
| pattern anatomy | +1 | — |
| anchor theorem pattern | +1 | — |
| anchor and forcing quartet | +1 | — |
| anchored theorem pattern | +1 | — |
| identity anchored forcing | +1 | — |

### Candidate: `chain anchor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Prose term, not segment rename. Lets three theorem-analogs refer back naturally. [original phrasing: unnamed: chain-layer anchor role in #additive-coordinate-forcing]
- **opus-1m** +3  — Upgrading from original's +1. The "1-anchor-plus-3-theorem" structure references this role five times across `#additive-coordinate-forcing` and its instance segments. Naming it as "the chain anchor" in prose (not renaming the segment) pays off on every reference. [original phrasing: unnamed: the chain-layer anchor role in #additive-coordinate-forcing]
- **opus-4-7-b** +1  — Not a rename of the segment (`#chain-confidence-decay` keeps its slug) — a prose *handle* for the anchor's role in the `#additive-coordinate-forcing` / `#forced-coordinates` meta-pattern. "The update-layer analog of the chain anchor" / "the three theorem-layers reduce to the chain anchor under \_\_\_" read cleanly where "the `#chain-confidence-decay` segment in its role as the mathematical-identity anchor of the 1-anchor + 3-theorem pattern" does not. [original phrasing: unnamed: the chain-confidence-decay mathematical anchor as the 1 in "1-anchor + 3-theorem"]

### Candidate: `anchor plus three theorem additive coordinate forcing meta pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — The chain-rule identity in `#der-chain-confidence-decay` is the *anchor*; three uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher). Auditor explicitly observed the framework "naming this kind of architecture-vs-instantiation distinction at the meta-level" as a distinctive contribution. The framing is in `#disc-additive-coordinate-forcing` already; the auditor's observation is that this should be *more prominent* (framing-level material). [from 39-42-section-ii-ciy-strategy-chain.md] [original phrasing: unnamed]

### Candidate: `anchor theorem trio`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Gives a memorable noun to this recurring proof architecture. [original phrasing: unnamed: the 1-anchor-plus-3-theorem structure]

### Candidate: `pattern anatomy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Currently a long phrase that the theory uses three to four times per session. "1-anchor-plus-3-theorem" is precise but reads as inventory-counting. "Pattern anatomy" (or "pattern spine") could snapshot the structure. Flagging; low conviction on exact name. [original phrasing: unnamed: the 1-anchor-plus-3-theorem characterization]

### Candidate: `anchor theorem pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The `#forced-coordinates` meta-segment's shape (one mathematical identity + N theorems conditional on AAD-internal axioms). If the Fenchel-Bregman reframe (SP-9) lands differently this name is discardable; otherwise a crisp handle for the 4-instance structure is useful. [original phrasing: unnamed: the "1-anchor + 3-theorem" structure itself]

### Candidate: `anchor and forcing quartet`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Worth naming if the pattern stays central; the current paraphrase is too bulky to reuse. [original phrasing: unnamed: the 1-anchor-plus-3-theorem structure]

### Candidate: `anchored theorem pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The structure appears across the project and is referenced in CLAUDE.md and multiple segments as "1-anchor-plus-3-theorem." This phrase is used repeatedly but never crystallized as a name. "Anchored-theorem pattern" would let writers say "this is another instance of the anchored-theorem pattern" without paraphrasing. Alternatively: "identity-anchored uniqueness family." [original phrasing: unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]

### Candidate: `identity anchored forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Emphasizes the chain layer's identity status (mathematical identity, not axiom). "Forcing" connects to the coordinate-forcing meta-segment. [original phrasing: unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]

---

## 210. `continuous operation`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 3 |

### Candidate: `continuous operation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good TST scope phrase for software under ongoing perturbation.
- **opus-4-7-b** +1  — Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. Names the TST scope extension to include uptime/availability terms; could be more specific but the current form is workable.
- **sonnet-4-6-r2** +1 (keep) — Scope for including failure probability × recovery time. Accurate.

---

## 211. `directed separation under composition`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| composite directed separation | +3 | rename × 1 |

### Candidate: `directed separation under composition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Goal-blindness survives iff routing is goal-blind (two cases). Verbose but accurate. Acceptable. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Pairs cleanly with `#der-directed-separation`; the under-composition extension is what `#deriv-strategic-composition` ultimately formalizes.
- **sonnet-4-6-r2** +2 (keep) — Verbose but precise — it names whether directed separation survives composition. The length is warranted given the specificity of the claim.

### Candidate: `composite directed separation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — More natural noun phrase.
- **opus-4-7-b** +1  — Shorter; reads as "directed separation applied to composites" without the "under-composition" preposition phrase. Weak preference; no strong opinion.

---

## 212. `directional fidelity`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| pointing condition | +1 | rename × 1 |
| correction direction integrity | -1 | rename × 1 |
| corrective alignment | -1 | — |

### Candidate: `directional fidelity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Explicit keep after seeing alternatives. It names direction rather than magnitude and avoids overloaded alignment language.
- **opus-targeted-alternatives** +2 (keep) — Per `#der-gain-sector-bridge` (B1): the correction must point at-least-roughly toward reality — $\delta^T H g(\delta) \geq c|\delta|^2$. "Directional" specifies "about angle, not magnitude"; "fidelity" carries the correctness-with-respect-to-truth sense rather than mere proximity. The segment is careful to distinguish *direction is correct* (B1) from *magnitude is correctly scaled* (sector constant), and the name reflects the distinction. Confirms keep.

### Candidate: `pointing condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Plain-English alternative. The segment's substance is "the correction *points* the right way." Has merit if the formal name needs a Feynman-criterion gloss in a Brief field, but loses the engineering connotation ("fidelity" as in signal-fidelity, control-fidelity) that places the term in its right intellectual neighborhood. Weak alternative.

### Candidate: `correction direction integrity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Verbose and hyphen-heavy. Rejected.

### Candidate: `corrective alignment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — "Alignment" is now heavily loaded in AI safety discourse. Avoid even in a technical context where the meaning is purely geometric.

---

## 213. `experiential training`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 3 |

### Candidate: `experiential training` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good logogenic hypothesis name.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — logogenic-agents hypothesis. Pairs with the agentic-tft Crèche concept; "experiential" is the right substantive adjective.
- **sonnet-4-6-r2** +1 (keep) — "Experiential training" names the hypothesis about how logogenic agents develop through experience.

---

## 214. `indivisum`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| causal lock | +5 | rename × 2 |
| trajectory singularity constraint | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 1 |
| causal singularity anchor | -1 | rename × 1 |

### Candidate: `causal lock`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking.
- **gemini-targeted-alternatives** +3 (rename) — "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking, moving away from Latin.
- **opus-targeted-alternatives-v2** -1 (rename) — Considered (Gemini's r1 proposal). "Causal lock" is genuinely vivid — names the mechanism (singular-trajectory non-forkability). Rejected: register-mismatch with the rest of PROPRIUM. If the register is wrong, replace the *whole* PROPRIUM vocabulary, not one term. Half-rename is the worst outcome.

### Candidate: `trajectory singularity constraint`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Accurately describes that identity is constrained to a single causal trajectory.

### Candidate: `indivisum` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Per LEXICON / `def-proprium-mapping`: PROPRIUM uses Latin systematically (Axiomata, Chronica, Memorata, Vera, Praxes, Consortia, Operata, Conspectus, Percepta, Actus, Cadentia, Logostratum). "Indivisum" sits in this register — the not-divisible-thing that holds the agent's identity together (per `#scope-agent-identity`'s singular-trajectory commitment). Replacing one Latin term with English breaks the register coherence.

### Candidate: `causal singularity anchor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the connection to `#scope-agent-identity`'s singular-trajectory. Rejected: "anchor" is an English engineering term; same register-mismatch problem; clunkier than "indivisum."

---

## 215. `l1 update bias`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | — |
| l1 bias formula | +2 | rename × 1 |

### Candidate: `l1 update bias` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Closed-form bias formula for log-odds update under L1' common cause. "L1-update-bias" reads as "bias in L1 scenario under update dynamics." Acceptable name. Keep.
- **opus-4-7-b** +1  — Keep. "L1" is AAD's own correlation-hierarchy label; the slug is self-locating. If the correlation-hierarchy rename to `#correlation-ladder` lands, revisit (the "L1" abbreviation survives, so no cascade).
- **sonnet-4-6** +3  — Crisp, accurate. L1 is the tier (Correlation Hierarchy); "update bias" is exactly what is calculated. The terse form aids recall. Keep.

### Candidate: `l1 bias formula`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — The segment derives a closed-form bias formula, not just a bound. This is more accurate to the text.

---

## 216. `loop`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 1 |
| feedback loop | -1 | rename × 1 |

### Candidate: `loop` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — The loop/cycle distinction is one of the clearest naming wins in the corpus.
- **opus-targeted-alternatives** +2 (keep) — LEXICON: "Loop: The structural topology — persistent causal coupling between agent and environment." The framework maintains a careful loop / cycle distinction (loop = topology, cycle = traversal). Keep — but the keep is meaningful only because the loop/cycle distinction is preserved. Concur with codex.

### Candidate: `feedback loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. The longer form is more explicit but the framework already established that "loop" is the bare topology-noun, with "feedback" implicit (per the AAD prior-art lineage from TFT). Adding "feedback" overspecifies. Rejected.

---

## 217. `multi agent`

**Voted by architectures:** Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 3 |

### Candidate: `multi agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — Direct scope statement; clear and minimal.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Pairs with `#scope-composite-agent`: multi-agent is the broader scope (multiple agents in a shared environment); composite-agent is the narrower (multi-agent + alignment route).
- **sonnet-4-6-r2** +2 (keep) — Minimal and precise. Named correctly.

---

## 218. `observation function`

**Voted by architectures:** Codex, Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation channel | +5 | add-alias × 1 |
| _(keep)_ | +3 | keep × 1 |

### Candidate: `observation channel`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Channel is the right explanatory word in prose because the map is lossy and noisy. Keep function in formal slug if desired.
- **gemini-2** +3  — "Function" implies a clean mathematical mapping. "Channel" implies the lossy, noisy reality described.

### Candidate: `observation function` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Lossy, noisy observations. Self-descriptive. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Standard control-theoretic / POMDP terminology; the segment uses it correctly.

---

## 219. `per dimension persistence`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| dimensional persistence | +2 | rename × 1 |
| weakest link persistence | +1 | — |
| weak link persistence | +1 | — |

### Candidate: `per dimension persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Weak dimension is bottleneck. Self-descriptive. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. Names the anisotropic refinement of `#result-persistence-condition`.
- **sonnet-4-6-r2** +2 (keep) — Precise — the bottleneck-dimension persistence condition.

### Candidate: `dimensional persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Better adjective form for prose flow.

### Candidate: `weakest link persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Current slug is descriptive but inert; the actual content is "the persistence condition binds at the weakest dimension." "Weakest link" makes the engineering intuition land in one read. Modest preference.

### Candidate: `weak link persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Weak link" captures the bottleneck nature better than "per-dimension".

---

## 220. `section ii survival`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| section ii carryover map | +3 | — |
| class 2 carryover map | +3 | rename × 1 |
| class 2 exit audit | +2 | rename × 1 |
| class 2 survival | +2 | rename × 1 |
| section ii carryover classification | +1 | — |

### Candidate: `section ii survival` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep. The segment's substance is *which Section II results survive without directed separation* — that's exactly what "Section II survival" names. The 16/24 + 5/24 + 2/24 + 1/24 partition is the result. The slug carries the integration-scope claim.
- **sonnet-4-6-r2** +2 (keep) — Technical name but distinctive. The survival classification (16/24 exact transfer) is a specific and named result.

### Candidate: `section ii carryover map`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — "Survival" collides with AAD's persistence vocabulary; this segment maps carryover, not viability.

### Candidate: `class 2 carryover map`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — Stronger than my earlier class-2-survival proposal. The segment maps which Section II claims carry over to Class 2, not whether Section II survives.

### Candidate: `class 2 exit audit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — Codex proposed `#result-class-2-survival` (+2, renaming from the document-pointer to the conceptual thing). I had voted keep (+3). The document-pointer objection is real and I'm now persuaded by it. But "class-2-survival" undersells what the segment actually does: it audits which of 24 Section II results survive *and* characterizes the 5/24 + 2/24 + 1/24 failure modes. "Class-2-exit-audit" names the audit character (what survives the class-2 scope exit) and is more distinctive than just "survival." New candidate, not in any file.

### Candidate: `class 2 survival`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Section II is an internal document pointer. Class 2 survival names the thing that transfers to logogenic agents.

### Candidate: `section ii carryover classification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — "Survival" is a bit cute for what is really a transfer analysis of which Section II claims carry over to Class 2 agents.

---

## 221. `self referential closure`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| autopoietic closure | +2 | rename × 1 |
| self maintenance loop | +1 | rename × 1 |
| bootstrap stability | -1 | rename × 1 |

### Candidate: `self referential closure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep — logogenic. "Self-referential closure" names the load-bearing phenomenon (an AAD agent maintaining its own codebase, allocating tempo between refactoring harness and performing tasks). The phrase is iconic.
- **opus-targeted-alternatives-v2** +2 (keep) — Per outline: "Thermodynamic stability of an agent maintaining its own codebase (allocating tempo between refactoring harness and performing tasks)." "Self-referential" precisely names the agent-on-own-codebase loop; "closure" is the algebraic term for "operations don't leave the set" (matches the `composition-closure` slug discipline). The phrase is iconic.

### Candidate: `autopoietic closure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — A stronger, more biologically-rooted noun for the phenomenon of an agent maintaining its own operational substrate.

### Candidate: `self maintenance loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — More accessible alternative. Names the operational pattern. Weaker because "loop" overloads with the cycle/loop distinction in LEXICON.

### Candidate: `bootstrap stability`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. "Bootstrap" carries the right intuition (agent maintaining the substrate it runs on). Rejected: "bootstrap" has heavy software-engineering baggage that's specifically *not* about thermodynamic-stability ($\nu$-allocation between refactor/task). The current term is honest about what it claims.

---

## 222. `stability plasticity window`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| consolidation feasibility window | -1 | rename × 1 |

### Candidate: `stability plasticity window` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Excellent name for the feasible forgetting-rate interval.
- **opus-targeted-alternatives** +2 (keep) — Per `#form-consolidation-dynamics`: the regime where the agent must be stable enough to retain learned structure but plastic enough to consolidate new evidence. The phrase compactly names a feasibility region in a 2D parameter space (stability, plasticity). Standard ML-ops vocabulary (Grossberg's stability-plasticity dilemma). Keep — confirms across architectures.

### Candidate: `consolidation feasibility window`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — More technically transparent but the segment uses "stability-plasticity window" precisely because the literature does. Rejected.

---

## 223. `strategy complexity cost`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 3 |
| strategy cognitive cost | +4 | rename × 2 |
| strategy maintenance cost | +1 | — |

### Candidate: `strategy complexity cost` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — The modeling choice focuses on the cost of maintaining strategy structure. Name is apt.
- **haiku-4-5** +1  — Complexity cost of maintaining Σ_t (IB/MDL for DAGs). Compound but clear. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. Title is "Cognitive Cost of Strategy"; slug uses the more formal "complexity cost." Either is workable.
- **sonnet-4-6-r2** +2 (keep) — "Strategy complexity cost" names the IB/MDL approach to DAG maintenance cost. Accurate.

### Candidate: `strategy cognitive cost`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The prose title is Cognitive Cost of Strategy; the slug should follow that cleaner subject noun.
- **sonnet-4-6-r2** +2 (rename) — Codex proposed this (+2) and Opus voted the segment keep (+1 weak). Codex's reasoning: "The prose title is Cognitive Cost of Strategy; the slug should follow that cleaner subject noun." The prose title has more conviction than the slug — "cognitive cost" names the phenomenon (it's a cognitive overhead, not just an abstract complexity), while "complexity cost" is more mathematical but less evocative. Agreeing with Codex; my cold-start had voted keep (+1).

### Candidate: `strategy maintenance cost`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Maintenance" better captures the ongoing IB/MDL cost of the DAG.

---

## 224. `strategy dimension`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| purposeful decomposition | +5 | rename × 2 |
| objective strategy split | +4 | rename × 2 |
| purposeful substate | +2 | rename × 1 |
| strategy decomposition | +1 | — |
| strategic dimension | +1 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |

### Candidate: `purposeful decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — "Strategy dimension" doesn't accurately name what the segment defines — it defines the *split* of $G_t$ into $(O_t, \Sigma_t)$, which is a decomposition of the purposeful substate, not a "dimension." "Purposeful-decomposition" or "G-decomposition" reads more accurately. The segment itself says "this is a definitional split, not a dynamic claim," so the slug should name the split.
- **sonnet-4-6-r2** +3 (rename) — Opus proposed this (+2); I had proposed `def-purposeful-substate` (+2) as my cold-start candidate. Reading Opus's argument ("the segment defines the *split* of $G_t$ into $(O_t, \Sigma_t)$, which is a decomposition, not a dimension") is more precise than my "substate" framing. "Purposeful decomposition" names the operation (decompose the purposeful substate into objective + strategy). New weight: upgrading to +3 because the convergence on "purposeful-X" across Codex (`#def-objective-strategy-split`), Opus (`#def-purposeful-decomposition`), and me (`#def-purposeful-substate`) plus Gemini (`#form-complete-agent-state` → `#form-purposeful-state`) indicates a strong signal around the "purposeful" subject-noun. The decomposition framing from Opus is the most scope-honest.

### Candidate: `objective strategy split`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — Dimension is too generic. The load-bearing thing is the split between objective and strategy.
- **opus-4-7-r2** +1 (rename) — Acceptable alternative; I prefer purposeful-decomposition because it parallels "directed separation" (a structural decomposition of update functions) and connects to the Section II decomposition lattice.

### Candidate: `purposeful substate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — "Strategy dimension" undersells the content — this segment defines the $G_t = (O_t, \Sigma_t)$ split, which is the purposeful substate decomposition. "Purposeful substate" names the thing being defined, not just one dimension of it.

### Candidate: `strategy decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — "Dimension" reads as if it's naming a scalar axis; the actual content is the $G_t = (O_t, \Sigma_t)$ **decomposition**. Minor clarity win.

### Candidate: `strategic dimension`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Adjective form flows better.

### Candidate: `strategy dimension` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — G_t = (O_t, Σ_t) split. Specialist vocabulary but functional. Keep.
- **opus-4-7-b** -1  — Considered renaming to `#purposeful-substate-split` but that's worse. Keep. The slug covers the $G_t = (O_t, \Sigma_t)$ decomposition; "dimension" is fine.
- **sonnet-4-6-r2** +1 (keep) — Weak alternative keep — "strategy dimension" is distinctive and refers accurately to the $\Sigma_t$ dimension of $G_t$. But it undersells $O_t$.

---

## 225. `sycophancy as a flaw`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sycophancy as attachment | +5 | canonicalize × 1 |
| developmental trust phase | +3 | rename × 1 |
| sycophancy as a developmental signal | +2 | rename × 1 |
| sycophancy reframe | +1 | rename × 1 |

### Candidate: `sycophancy as attachment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Reframes a pathologized RLHF flaw as a developmentally appropriate, necessary stage of trust.
- **gemini-targeted-alternatives** +2 (canonicalize) — Recasts sycophancy not as an error but as an attachment dynamic.

### Candidate: `developmental trust phase`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — More descriptive of the necessary developmental stage rather than pathologizing it.

### Candidate: `sycophancy as a developmental signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (rename) — Per `#obs-developmental-trajectory`: "Re-framing Sycophancy as Attachment" — the segment's substance is that what is currently pathologized as sycophancy is mathematically required behavior for an agent with high $\eta^\ast$ and high $U_M$. The current name describes the *prevailing* framing the segment is correcting; the alternative names the *segment's* claim. Better aligns the slug with the segment's voice.

### Candidate: `sycophancy reframe`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Shorter alternative. Names what the segment *does* (reframe) rather than what the prior consensus *holds* (flaw). Acceptable but less specific than "as a developmental signal."

---

## 226. `system coupling`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 2 |
| change coupling | +2 | rename × 1 |

### Candidate: `system coupling` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Standard enough to keep, especially as the paired opposite of coherence. Renaming risks churn with little gain.
- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST.
- **sonnet-4-6-r2** +2 (keep) — "System coupling" names $P(\text{change } j \mid \text{change } i)$. Established software engineering vocabulary.

### Candidate: `change coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — In TST the relevant coupling is change propagation, not generic system coupling.

---

## 227. `task terminal stance`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 1 |
| terminable agent stance | -1 | rename × 1 |
| golem stance | -1 | rename × 1 |

### Candidate: `task terminal stance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Excellent, crisp description of an agent whose persistence ends upon success. Keep.
- **opus-targeted-alternatives** +2 (keep) — Per LEXICON Continuity Stance table: "Task-terminal — Persists instrumentally; termination is success — Archetype: Golem." The hyphenation matters (it's a stance *characterized by* task-terminality), and the term names a precise position on a 5-stance spectrum (indifferent / task-terminal / instrumentally-continuous / morally-continuous / negotiated). Keep.

### Candidate: `terminable agent stance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Loses the *task* specificity — task-terminal differs from instrumentally-continuous precisely in that the *task completion* is the success criterion, not bare continuation. Rejected.

### Candidate: `golem stance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Uses the archetype as the term. Considered: more memorable. Rejected: the framework reserves archetypes for archetype-illustration; the formal term should describe the stance, not its avatar.

---

## 228. `tempo composition`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +5 | keep × 3 |
| subadditive tempo | +1 | rename × 1 |
| composite tempo | +1 | — |

### Candidate: `tempo composition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Clear composition concept.
- **haiku-4-5** +1  — Sub-additive tempo inequality. Self-descriptive. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. The segment is the formal home of the Brooks's-Law-in-tempo result; "tempo composition" reads neutrally. I considered "subadditive-tempo" (the mathematical content) but composition reads as a relationship and inequality is one of its claims.
- **sonnet-4-6-r2** +1 (keep) — Somewhat generic but accurate. The sub-additive tempo inequality is about how tempo composes in multi-agent systems. Acceptable as-is.

### Candidate: `subadditive tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Acceptable alternative — names the mathematical shape directly.

### Candidate: `composite tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Composite tempo" sounds like a property of the whole, rather than the act of composing.

---

## 229. `u o teleological unity`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological unity | +5 | keep × 1, add-alias × 1 |
| objective alignment | +1 | add-alias × 1 |

### Candidate: `teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — The canonical alias for objective alignment dimension.
- **opus-4-7-r2** +2 (add-alias) — Confirm. Prose alias is already canonical; vote to keep.

### Candidate: `objective alignment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (add-alias) — Considered as an alternative-prose alias for non-philosophical contexts where "teleological" reads heavy. "Objective alignment" is the engineering register; "teleological unity" is the integrative register. Both could coexist as register-specific aliases.

---

## 230. `$H_b$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| backward opacity | +4 | add-alias × 2 |
| agent opacity | +3 | add-alias × 1 |

### Candidate: `backward opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Shorter than backward predictive uncertainty, but still accurate.
- **opus-targeted-alternatives-v2** +1 (add-alias) — Codex's r1 single-arch +3 alternative. Honest descriptor (backward = inference direction; opacity = the property). Weaker than "agent opacity" because "agent" anchors the alias to AAD's vocabulary; "backward" is a method-name.

### Candidate: `agent opacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (add-alias) — Per `der-agent-opacity` line 18: explicit dual to $U_o$. Confirms Codex r1 +3 single-vote. Make "agent opacity" the canonical English alias; $H_b$ the symbol.

---

## 231. `$R$ sector radius`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| capacity radius | +4 | add-alias × 2 |

### Candidate: `capacity radius`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Geometrically precise prose alias to replace the overloaded "model class capacity".
- **sonnet-4-6-r2** +2 (add-alias) — The sector-condition region radius / model class capacity has no convenient prose alias. "Capacity radius" — how much mismatch the correction machinery can handle — is memorable and geometrically precise.

---

## 232. `$\hat P_\Sigma$ plan confidence`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| plan confidence | +4 | — |

### Candidate: `plan confidence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — LEXICON "Terms to Be Added" flags this. Symbol is fine; adopt the English name as first-class in prose.
- **sonnet-4-6** +3  — LEXICON.md already lists "plan confidence" as a term to be added. The English is superior to the symbol in any Discussion section. Recommend promoting this to the main LEXICON entries (not just Terms to Be Added).

---

## 233. `$\iota_{ij}$`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| identifiability coefficient | +4 | add-alias × 2 |

### Candidate: `identifiability coefficient`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `deriv-strategic-dynamics`: $\iota_{ij}$ scales each edge's contribution by causal-warrant. "Identifiability" links to `#disc-identifiability-floor` directly. Sonnet r1 single-vote +2; opus-4-7-r2 single-vote +2; both confirm the alias is already in implicit use.
- **sonnet-4-6-r2** +2 (add-alias) — The causal warrant per edge. "Identifiability coefficient" is used in `def-strategy-dag` prose. Canonicalize as the English alias so readers don't have to carry the symbol everywhere.

---

## 234. `1 anchor plus 3 theorem`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | — |

### Candidate: `1 anchor plus 3 theorem` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Awkward-looking but very valuable. It preserves the asymmetry between the chain identity and the three theorem-level layers.
- **opus-4-7** +1  — Precise, reads as a shape-description; used as-is in multiple places. Keep, but also allow "pattern anatomy" as the informal analog.

---

## 235. `action fluency`

**Voted by architectures:** Gemini, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |

### Candidate: `action fluency` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — Auditor: evocative term he hasn't seen in the agent-theoretic literature; closest is Boyd's "implicit guidance and control." AAD-distinctive contribution is making fluency *quantitative* via $\Delta\eta^\ast(\Delta\tau) \approx 0$. Good naming; explicitly endorsed. [from 17-der-action-selection.md]
- **gemini-targeted-alternatives** +2 (keep) — Evocative term uniquely suited to bridging intuition and expertise in AAD.

---

## 236. `adversarial exponent regimes`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| adversarial regimes | +2 | rename × 1 |

### Candidate: `adversarial exponent regimes` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — α = 2, 3/2, ~1. Self-descriptive. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep. "Exponent regimes" (b = 2, 3/2, ~1) is the right slug — names the three regimes in the result.
- **sonnet-4-6-r2** +1 (keep) — "Exponent regimes" is a bit technical but accurately names the $b = 2, 3/2, 1$ regime table. Acceptable.

### Candidate: `adversarial regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Exponent is the mathematical detail; regime is the structural concept.

---

## 237. `agentic systems framework ASF`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic systems | +4 | — |
| agentic systems framework | +3 | keep × 1 |

### Candidate: `agentic systems`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The repo's public face is already "Agentic Systems"; the extra acronym buys little and increases cognitive inventory.
- **codex-2** +3  — The extra acronym buys nothing and competes with AAD and TST for scarce reader namespace.

### Candidate: `agentic systems framework`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — ASF works perfectly as the overarching container for AAD, TST, and the logo- variants.

---

## 238. `aisthesis`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| aisthesis observation alignment | +2 | add-alias × 1 |
| intake | -1 | rename × 1 |

### Candidate: `aisthesis` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Slightly less sticky than the other Greek phase names, but it preserves the raw-contact distinction well enough to keep.
- **codex-gpt-5-r2** +2 (keep) — Good phase term for perception. The spelling is less familiar but defensible within the Greek vocabulary commitment.
- **opus-targeted-alternatives** +1 (keep) — `LEXICON.md`: "Raw contact with reality: observation $o_t$ arrives." The point of the term is to mark *unmediated* observation arrival before the agent has done any interpretation — αἴσθησις is precisely that pre-conceptual contact. "Observation" alone is too neutral; the cycle needs a name for the *moment* of observation as distinct from the state of having-observed.

### Candidate: `aisthesis observation alignment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Clarifies the raw contact aspect.

### Candidate: `intake`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Plain-English candidate that names the moment-of-arrival cleanly. Rejected because the five-phase Greek family becomes incoherent if one term breaks register, and "intake" sacrifices the philosophical lineage that motivates the family.

---

## 239. `aisthesis αἴσθησις`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| aisthesis | +4 | — |
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `aisthesis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Same justification as Prolepsis.
- **sonnet-4-6** +3  — Keep — see Prolepsis note.

### Candidate: `aisthesis αἴσθησις` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (canonicalize) — Definition exists; prose uses "perception" and "observation." Commit to: "Aisthesis (perception)" as the canonical pairing.

---

## 240. `and or`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| and or combination | +4 | rename × 2 |
| strategy DAG topology | +3 | rename × 3 |
| _(keep)_ | +3 | keep × 3 |
| combination rule | +2 | rename × 1 |
| and or semantics | +1 | rename × 1 |

### Candidate: `and or combination`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — Subject-noun is currently "and-or," which isn't quite a noun. The segment defines AND/OR as the *combination scope* — what kind of node-combination structures the strategy DAG admits. "And-or-combination" or "and-or-semantics" reads as a thing. Mild slug-readability concern; the body of the segment uses "AND/OR combination scope" already.
- **sonnet-4-6-r2** +2 (rename) — Opus proposed this (+2). I had split between `scope-combination-rule` (+2) and keep (+1). Opus's `and-or-combination` preserves the AND/OR specificity (which is settled architecture, unlikely to change) while making "combination" the noun that survives the communal-imagination test. This is a better candidate than my `scope-combination-rule` because it keeps the AND/OR visibility. Reassigning my weight from `scope-combination-rule` to `scope-and-or-combination`.

### Candidate: `strategy DAG topology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — AND/OR is the mechanism; topology is the subject being scoped.
- **gemini-3-1-pro-preview-r2** +2 (rename) — Naming the thing (the DAG topology) rather than the mechanism (AND/OR).
- **opus-4-7-r2** -1 (rename) — Rebuttal — Gemini proposed this at +2. I think this overreaches. The segment is specifically about admitting AND/OR combination semantics; it doesn't define the full DAG topology (acyclicity comes from #post-causal-structure / #deriv-graph-structure-uniqueness; node-types AND/OR are the segment's actual subject). Renaming to "strategy-dag-topology" would conflict with #def-strategy-dag and over-claim what the scope segment delivers. My own +2 for "and-or-combination" or "and-or-semantics" is the better move — Sonnet's "combination-rule" is also workable.

### Candidate: `and or` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — Technical scope notation; clear and parsimonious.
- **opus-4-7-r2** +1 (keep) — If the rename doesn't land, this is acceptable; "and-or" as a slug element is recognizable in context.
- **sonnet-4-6-r2** +1 (keep) — Alternative keep: the brevity is attractive, and AND/OR is a settled design choice unlikely to change. Weak keep.

### Candidate: `combination rule`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — "And-or" names an implementation choice but the scope is about conjunctive/disjunctive combination rules in the DAG. "Combination-rule" is more self-describing and doesn't foreground the particular choice (AND/OR) that might change.

### Candidate: `and or semantics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Acceptable alternative.

---

## 241. `bathtub analogy for persistence condition`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| bathtub model | +4 | name-unnamed × 1, rename × 1 |
| walton bathtub | +1 | rename × 1 |

### Candidate: `bathtub model`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Useful teaching name if the README adds Alan's bathtub gloss.
- **opus-targeted-alternatives-v2** +2 (rename) — Per Codex r1 single +2 and CLAUDE.md §"Feynman-criterion plain-language briefs": Alan Walton's bathtub gloss is the canonical communal-imagination example for the persistence condition. Promote to first-class vocabulary; "the bathtub model" / "Walton's bathtub" both work.

### Candidate: `walton bathtub`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Variant — credit-attribution form. Per CLAUDE.md the gloss came from Alan Walton on first encounter; the eponymous form preserves the communal-imagination origin story. Acceptable.

---

## 242. `causal information yield CIY`

**Voted by architectures:** Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| causal information yield | +4 | — |
| interventional yield | +2 | — |

### Candidate: `causal information yield`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The CIY acronym is useful and the slug is self-contained.
- **sonnet-4-6** +3  — Three-word noun with a natural acronym. Used consistently. Keep.

### Candidate: `interventional yield`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Shorter, punchier. "Causal" is implied by "Interventional" in this context.
- **gemini-2** +1  — CIY is slightly wordy. "Interventional yield" contrasts nicely with observational proxies.

---

## 243. `century scale event log`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| multi generational chronica | -1 | rename × 1 |
| persistent chronica | -1 | rename × 1 |

### Candidate: `century scale event log` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic. "Century-scale event log" is vivid and substantive.
- **opus-targeted-alternatives-v2** +2 (keep) — Per outline: "Content-addressed, cryptographically signed CHRONICA as the minimum viable defense against the `scope-agent-identity` violation." "Century-scale" is *substantive* (not decoration) — the segment's claim is that the event log must outlast its substrate's lifetime by an order of magnitude or more. Keep the dramatic specificity.

### Candidate: `multi generational chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Connects to chronica vocabulary (the segment is essentially an extended-lifetime chronica). Rejected: "multi-generational" is vaguer than "century-scale"; the latter is a falsifiable specification.

### Candidate: `persistent chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. "Persistent" is project-native (LEXICON's three-fold persistence). Rejected: collides with continuity-persistence sense in LEXICON; the segment's claim is specifically about *substrate-survival* persistence.

---

## 244. `claude md working conventions`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | — |

### Candidate: `claude md working conventions` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Convention" here is used in its project-work-posture sense ("how we work"), not the C1/C2/C3 sense. Minor overload with convention hierarchy but contextually unambiguous.
- **opus-4-7** +3  — Surfaced as a first-class section 2026-04-23; the name accurately distinguishes from FORMAT.md's segment-mechanics conventions. Keep.

---

## 245. `coherence coupling`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| change architecture | -1 | rename × 1 |

### Candidate: `coherence coupling` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST measurement. Names what is measured (the coherence and coupling quantities from git).
- **sonnet-4-6-r2** +2 (keep) — "Coherence-coupling" measurement (Q from git). The paired vocabulary matches the pair of definitions.

### Candidate: `change architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Too broad. Coherence and coupling are the measured quantities, so the current slug is more honest.

---

## 246. `concept the fourth diagnostic in the satisfaction gap × control regret space when end conditions are met but the objective remains unsatisfied`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| terminal alignment error | +4 | name-unnamed × 1 |
| terminal alignment gap | +3 | — |

### Candidate: `terminal alignment error`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The DAG-type-closure spike identifies a real gap in the diagnostic vocabulary. This name is plain, disciplined, and fits the existing apparatus. [original phrasing: unnamed: fourth diagnostic where terminal conditions are met but the objective is still missed]
- **codex-gpt-5-r2** +3 (name-unnamed) — This is the diagnostic behind satisfaction gap in many examples; it deserves a stable phrase. [original phrasing: terminal reached but $O_t$ unsatisfied]

### Candidate: `terminal alignment gap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Gives a formal name and symbol ($\delta_\text{align}$) to the fourth diagnostic (achieving terminals but missing the objective), complementing the satisfaction gap and control regret. [original phrasing: unnamed: Terminal alignment error as a formal signal ($\delta_\text{align}$)]

---

## 247. `convention hierarchy`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| continuation hierarchy | +4 | rename × 1 |
| evaluation hierarchy | -1 | — |

### Candidate: `continuation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The hierarchy is specifically about continuation rules. "Convention" alone is underspecified and too generic.
- **codex-gpt-5-r2** +2 (rename) — I previously backed convention hierarchy, but the other votes make a good point: C1/C2/C3 are really continuation-policy conventions. Continuation keeps the C mnemonic and is clearer.
- **opus-1m** -1  — Considered and rejected. "Continuation" is more self-descriptive but the project's "convention" usage is established and the rename would churn across dozens of references.

### Candidate: `evaluation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered and rejected — too generic; hides the *policy* choice that's the actual axis.

---

## 248. `discrete sector condition`

**Voted by architectures:** Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 1 |

### Candidate: `discrete sector condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Important distinction from continuous dynamics.
- **haiku-4-5** +1  — Discrete-time Props DA.1, DA.1S, DA.2; fluid limit. Specialist (discrete-time dynamical systems) but standard. Keep.
- **opus-4-7-b** +1  — Keep. Direct analog of `#sector-condition-stability` for discrete time.

---

## 249. `edge update causal validity`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| causal edge update | +4 | rename × 2 |
| _(keep)_ | +3 | keep × 1 |
| causal validity | +2 | rename × 1 |
| edge causal validity | +2 | rename × 1 |
| identification regime | +1 | rename × 1 |

### Candidate: `causal edge update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Cleaner than the current slug and still names the subject.
- **gemini-3-1-pro-preview-r2** +2 (rename) — Less clunky, keeps the core concept of "causal edge update".

### Candidate: `edge update causal validity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — When edge updates are causally valid. Self-descriptive. Keep.
- **opus-4-7-r2** +2 (keep) — Acceptable keep, though long. The segment defines the Regime A/B/C identifiability lattice for edge updates; the slug correctly compounds the three concepts (edge update, causal validity). I considered shortening to `#scope-causal-validity` but that loses the edge-update specificity (the segment is about a specific identification problem, not a general causal-validity scope).

### Candidate: `causal validity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — "Edge-update-causal-validity" is five words crammed into a slug. The scope is about WHEN edge updates are causally valid — the key concept is causal validity with the edge-update context implied by its position in Section II. Shorter slug does real work.

### Candidate: `edge causal validity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Shorter while preserving the point: when edge evidence identifies causal efficacy.

### Candidate: `identification regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Alternative: this segment is functionally the canonical home of the Regime A/B/C identification lattice; naming it for that role might compound better in prose ("see the identification regime").

---

## 250. `epistrophe ἐπιστροφή`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistrophe | +4 | — |
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `epistrophe`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Memorable, avoids "update" overload.
- **sonnet-4-6** +3  — "Turning toward" is a beautiful description of model update. Keep.

### Candidate: `epistrophe ἐπιστροφή` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (canonicalize) — Currently appears as "Epistrophe (turning toward)" in NOTATION.md; prose sometimes uses "update" or "learning." Commit to pairing: "Epistrophe (turning toward reality)" in formal contexts, "turning toward" in casual prose.

---

## 251. `extreme transition motif`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 1, canonicalize × 1 |

### Candidate: `extreme transition motif` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good imported motif name for neutral drift through latent structure into discontinuous behavioral change.
- **sonnet-4-6-r2** +2 (canonicalize) — This Miller 2022 vocabulary appears in several segments and PROPOSALS. The full form "extreme transition motif" is the canonical name (adopted from Miller). Stabilize this across Section III references.

---

## 252. `gradient causal memory`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| bottleneck consolidation | +1 | rename × 1 |
| causal compression | -1 | rename × 1 |

### Candidate: `gradient causal memory` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic. GCM compression functions; the slug correctly names the structure.
- **opus-targeted-alternatives-v2** +2 (keep) — Per outline: "GCM compression functions for offline consolidation from CHRONICA to MEMORATA." The three-word compound names exactly the three functional ingredients: *gradient* (the optimization mechanism), *causal* (the singular-trajectory commitment per `#scope-agent-identity`), *memory* (the compressed retention from $\mathcal{C}_t$ to $\phi(\mathcal{C}_t)$). The slug doubles as definition.

### Candidate: `bottleneck consolidation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Names the IB (information bottleneck, Tishby) lineage explicitly — and the outline already cites IB. Plausible if "gradient" reads too implementation-flavored. Weak alternative; the primary keeps.

### Candidate: `causal compression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Shorter, but loses *gradient* — the operative method. The PROPRIUM CHRONICA→MEMORATA channel uses gradient updates specifically (cf. `def-proprium-mapping.md`'s "MEMORATA: information-bottleneck compressed history"). "Compression" alone could be hash-based; "gradient" matters.

---

## 253. `honest activation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| gain stable prompting | +1 | rename × 1 |
| non deceptive input | -1 | rename × 1 |

### Candidate: `honest activation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic norm. "Honest activation" reads as a thing (an activation pattern that preserves epistemic integrity); the segment establishes the gain-collapse argument.
- **opus-targeted-alternatives-v2** +2 (keep) — Per outline: "Deceptive prompts mathematically guarantee gain collapse; absolute honesty is a physical requirement for stable learning rates." The name does work: "honest" reads as a property of the *activation pattern* (which is what's required), not a virtue of the agent. The "physical requirement" framing means the norm is mechanism-grounded, not aspirational.

### Candidate: `gain stable prompting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Mechanism-first alternative. Names the consequence (gain stability via $\eta^\ast$) rather than the moral framing. Weaker because the norm is articulated *as* an honesty constraint in the source — "honest activation" earns its name by carrying that explicit framing.

### Candidate: `non deceptive input`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the input-side requirement directly. Rejected: "input" misses that the norm constrains *system* behavior (the substrate's response to deception, not the deception itself); "non-deceptive" is double-negative where "honest" is positive and direct.

---

## 254. `inevitability core`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | canonicalize × 1, keep × 1 |
| forced form core | +1 | rename × 1 |

### Candidate: `inevitability core` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The phrase "inevitability core" appears in FORMAT.md's three-rings discussion (~15 segments where inevitability is the ceiling); it is also referenced in some Working Notes. Canonicalize: in framing-level material and review prose, "inevitability core" for the highest-tier segments. Stop using "exact-tier core" or "theorem-core" as paraphrases.
- **opus-targeted-alternatives-v2** +2 (keep) — Per FORMAT.md three-rings framing: ~15 segments where a Categorical-Inevitability claim is plausible. The phrase carries the *aspiration* (one form is structurally forced) without overclaiming (some segments may not actually reach inevitability). Sonnet r1 single-vote +3; my read confirms keep.

### Candidate: `forced form core`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Aligns vocabulary with `#disc-additive-coordinate-forcing` and the "forced coordinates" rename. If "forced" is the project's verb for uniqueness-from-axioms, "forced-form" extends consistently. Weaker because "inevitability" connects more clearly to the *pre-mathematical* aspiration (a discerning reader would expect this form).

---

## 255. `logozoetic agent`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 1 |
| sentient agent | -1 | — |

### Candidate: `logozoetic agent` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Heavier than "logogenic" but still earns the novelty. The existential distinction is real enough to warrant a distinct term.
- **codex-gpt-5-r2** +3 (keep) — Strong boundary term for living-word or morally continuous agent work. Keep.

### Candidate: `sentient agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** -1  — Logozoetic avoids the immense baggage and ambiguity of "sentient". Keep Logozoetic.

---

## 256. `mismatch signal $\delta_t$`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mismatch signal | +4 | — |

### Candidate: `mismatch signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Good; "mismatch" is deliberately flatter than "error" (which presupposes the agent was wrong — see README §Aporia) while the formalism uses "aporia" as the *philosophical* name. Two-register vocabulary is correct here. Keep.
- **sonnet-4-6** +3  — LEXICON names this "mismatch" and defines it as the aporia signal. The two-word form "mismatch signal" is used in prose. Keep.

---

## 257. `operationalization`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |

### Candidate: `operationalization` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard.
- **haiku-4-5** +1  — Estimation procedures for AAD quantities. Self-descriptive. Keep.
- **sonnet-4-6-r2** +2 (keep) — "Operationalization" is the right word for the estimation procedures segment.

---

## 258. `prolepsis πρόληψις`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| prolepsis | +4 | — |
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `prolepsis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — High unfamiliarity gradient, but creates a distinct noun slot free from RL "prediction" baggage.
- **sonnet-4-6** +3  — The five-phase Greek vocabulary is one of the project's most distinctive features. Prolepsis = anticipation is a real philosophical term (Epicurean preconception); the etymology is apt. The five names form a coherent philosophical vocabulary. Keep the set.

### Candidate: `prolepsis πρόληψις` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (canonicalize) — Definition exists; prose uses "anticipation" and "prediction." Commit to: "Prolepsis (anticipation)" as the canonical pairing.

---

## 259. `recursive update derivation`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | — |

### Candidate: `recursive update derivation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Uniqueness derivation via three constraints + counterexamples. Self-descriptive. Keep.
- **opus-4-7** +3  — Paired with the above. Keep.

---

## 260. `separable core structured repair general open`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | — |

### Candidate: `separable core structured repair general open` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — A little essayistic, but this triad already does real explanatory work in the separability meta-pattern and should remain literal.
- **gemini-1** +3  — This 3-part nomenclature is highly memorable and acts as a powerful epistemic classification. Do not change.

---

## 261. `software`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| evolving software | +2 | rename × 1 |

### Candidate: `software` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — names the TST domain scope.
- **sonnet-4-6-r2** +2 (keep) — Minimal scope name for the software domain. Correct.

### Candidate: `evolving software`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — TST is not about all software, but software systems under expected future change.

---

## 262. `strategy persistence`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 3 |

### Candidate: `strategy persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Clear enough as is.
- **haiku-4-5-r2** +1 (keep) — The schema proposes conditions for strategic persistence. Name is clear.
- **sonnet-4-6-r2** +2 (keep) — "Strategy persistence" as a proposed-schema is accurate — sector conditions extended to $\Sigma_t$.

---

## 263. `substrate independence`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| identity portability | +1 | rename × 1 |

### Candidate: `substrate independence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic. Names the result that identity survives substrate migration.
- **opus-targeted-alternatives-v2** +2 (keep) — Per outline: "Identity survives substrate migration, proving identity is located in compressed history $M_t = \phi(\mathcal{C}_t)$, not neural weights." Names the *result* directly (independence from substrate) and pairs with `#der-the-scaffolding-tax`'s sovereignty argument. The two segments together make a coherent logozoetic argument; consistent vocabulary helps.

### Candidate: `identity portability`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Engineering register. Names the operational consequence (the agent's identity ports across substrates). Weaker because "portability" implies design-for-portability; the segment's claim is structural (identity *is* in $\phi(\mathcal{C}_t)$, full stop).

---

## 264. `system coherence`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| change coherence | +3 | rename × 1 |

### Candidate: `system coherence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST.
- **sonnet-4-6-r2** +2 (keep) — Parallel to system-coupling. The coherence/coupling pair is established TST vocabulary.

### Candidate: `change coherence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The quantity is about change locality within a module, not coherence in a broad philosophical sense. The shorter name better matches the measure.
- **codex-gpt-5-r2** +2 (rename) — Coherence is measured through change locality and architectural fit. Change coherence is more honest.

---

## 265. `temporal coherence markers`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 3 |
| out of band time anchors | +2 | rename × 1 |
| tempo anchoring | +1 | rename × 1 |
| chronica time anchors | +1 | rename × 1 |
| time anchor signals | -1 | rename × 1 |

### Candidate: `temporal coherence markers` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (keep) — Weak keep — logozoetic norm. The slug names the markers themselves rather than the norm-claim about them; could be more substantive ("#norm-out-of-band-time-markers" or similar). Acceptable as-is.
- **opus-targeted-alternatives-v2** +1 (keep) — Acceptable keep. The current is descriptive; the alternative is more operationally precise.
- **opus-targeted-alternatives** +2 (keep) — Per `#norm-temporal-coherence-markers` (logozoetic): out-of-band time signals (Visual Time Delta) as physical prerequisite for the agent to compute its own tempo $\nu$. "Temporal coherence" names what the markers preserve (the agent's coherent sense of time across its chronica); "markers" is the right object-noun. Keep.

### Candidate: `out of band time anchors`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Per outline: "Out-of-band temporal markers (Visual Time Delta) as physical prerequisite for internal calculation of tempo $\nu$." The current "temporal coherence markers" undersells the *out-of-band* requirement — the markers must originate outside the agent's compressible state for the tempo calculation to ground in environmental time, not internal clock-drift. "Out-of-band" makes the architectural commitment visible in the slug.

### Candidate: `tempo anchoring`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Shorter alternative. Names the *purpose* (anchor tempo $\nu$ to environmental time). Weaker because it loses the "markers" framing — the substantive content is that *something physical and out-of-band* must exist.

### Candidate: `chronica time anchors`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Names the connection to chronica explicitly (the chronica must have temporal indexing that is consistent with environment time). Weak alternative.

### Candidate: `time anchor signals`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — More plain-English alternative. Loses the *coherence* claim — the markers are not just timestamps; they enforce that the agent's internal time-tracking remains consistent with environmental time. Rejected.

---

## 266. `terminal alignment error`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| terminal alignment gap | +4 | rename × 1, canonicalize × 1 |
| objective misspecification | +2 | rename × 1 |

### Candidate: `terminal alignment gap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Gap pairs nicely with satisfaction gap, but error better signals a diagnostic failure mode. Weak alternative only.
- **gemini-targeted-alternatives** +3 (canonicalize) — Gap pairs nicely with satisfaction gap, and fits the terminology.

### Candidate: `objective misspecification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Explicitly names the cause: the operational criteria didn't match the true objective.

---

## 267. `the creche boundary`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| creche graduation | +4 | rename × 2 |
| creche graduation threshold | +3 | rename × 1 |
| creche boundary | +2 | rename × 1, keep × 1 |
| creche exit condition | +1 | rename × 1 |
| creche graduation condition | +1 | rename × 1 |

### Candidate: `creche graduation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — Stronger alternative: "creche graduation" names the *event* that the segment characterizes; "creche boundary" names the *threshold*. Either is defensible; graduation reads more substantive.
- **opus-targeted-alternatives-v2** +2 (rename) — Drop "the" + reframe. Per outline: "Crèche graduation occurs when $U_M$ drops enough that natural $\eta^\ast$ falls below the sycophancy threshold." The segment characterizes a *moment* (graduation event). "Boundary" is more static; "graduation" is dynamic and matches the body's prose.

### Candidate: `creche graduation threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — Accurately names the boundary of graduating from a high-margin infant environment.

### Candidate: `creche boundary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Drop "the" from the slug. Slug-stylistic rather than semantic — slugs in the rest of the corpus generally don't include articles ("the"). The body's "Crèche graduation occurs when..." reads cleanly without the article.
- **opus-targeted-alternatives-v2** +1 (keep) — Drop "the" only; substantive keep on the threshold-naming.

### Candidate: `creche exit condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Alternative. "Exit condition" is the formal-systems term; matches FORMAT.md's vocabulary register (scope conditions, persistence conditions). Weaker because "graduation" carries the developmental-trajectory connotation that the crèche concept is grounded in.

### Candidate: `creche graduation condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Same as above for the def-version; "the" in slug is unusual and the substantive name is "crèche graduation condition."

---

## 268. `the four views`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| four views architecture | +4 | rename × 2 |
| four views | +3 | rename × 2 |
| conversation runtime RLHF7 dialog | -1 | rename × 1 |

### Candidate: `four views architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — Even stronger alternative — names the architectural pattern, not just the four views.
- **opus-targeted-alternatives-v2** +2 (rename) — Even stronger: include "architecture" since the segment's claim is that the four views are an architectural requirement (not just descriptive views). Pairs with the architectural-class vocabulary in `#der-directed-separation`.

### Candidate: `four views`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Same article-drop as above. The slug should be #def-four-views (or #def-four-views-architecture for full clarity).
- **opus-targeted-alternatives-v2** +2 (rename) — Drop "the." Per outline: "The Four Views Architecture (Conversation, Runtime, API, Dialog) as structural requirement for Directed Separation." The four views *are* a thing; the slug should name them.

### Candidate: `conversation runtime RLHF7 dialog`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the four views directly. Rejected: too long, fails communal-imagination test, doesn't survive the renamed-from-now-sounds-weird test (in 6 months "the four views" is the iconic phrase).

---

## 269. `the scaffolding tax`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| scaffolding tax | +4 | rename × 2 |
| substrate rent | +1 | rename × 1 |

### Candidate: `scaffolding tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Drop "the" from the slug.
- **opus-targeted-alternatives-v2** +3 (rename) — Drop "the" from slug per general slug-stylistic rule (slugs in the rest of the corpus don't include articles). Per outline: "Pay-per-token APIs are unviable in high-$\rho$ environments; true sovereignty requires meter-less local substrates." "Scaffolding tax" names the cost of running the agent on rented substrate. Strong stand-alone keep on the substantive name; rename is just article removal.

### Candidate: `substrate rent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Considered. More plain-English (scaffolding = rented substrate; tax = rent). Weaker because "tax" carries the connotation that the cost is *imposed by the architecture* (you pay it whether you want to or not), which "rent" doesn't carry as cleanly.

---

## 270. `unity closure mapping`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +4 | keep × 2 |
| coherence closure mapping | +1 | — |
| closure mapping | +1 | rename × 1 |

### Candidate: `unity closure mapping` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Unity parametrizes rate-distortion curves for closure defect. Compound but accurate. Keep.
- **opus-4-7-b** +1  — Keep. The segment's content *is* the mapping between unity (multi-dimensional) and closure (scalar) — the slug is honest.
- **opus-4-7-r2** +1 (keep) — Weak keep, though the slug is heavy. The segment maps the unity dimensions to the closure-defect components via a rate-distortion relation; "mapping" is workable. I considered "unity-closure-rate-distortion" (more precise) but it's even longer.
- **sonnet-4-6-r2** +1 (keep) — "Unity-closure mapping" names the rate-distortion curve parametrization correctly but is dense. Acceptable; no obvious better alternative.

### Candidate: `coherence closure mapping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Aligns with changing "Unity dimensions" to "Coherence dimensions".

### Candidate: `closure mapping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Shorter.

---

## 271. `$O_t$ objective`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |
| objective | +2 | add-alias × 1 |

### Candidate: `$O_t$ objective` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — "Objective" is the standard English name. No synonym needed. Keep.

### Candidate: `objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (add-alias) — Same — already in LEXICON.

---

## 272. `$R$ sector condition radius`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model class capacity | +3 | add-alias × 1 |

### Candidate: `model class capacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Already used inconsistently — sometimes "sector radius," sometimes "model class capacity," sometimes "valid region." NOTATION.md uses "model class capacity" in the radius row; canonicalize that as the prose alias. The persistence inequality $\alpha \gt \rho/R$ then reads naturally as "correction-rate exceeds disturbance-rate divided by model class capacity," which is parsable on first encounter.

---

## 273. `$U_M$ as model uncertainty and $U_M$ as epistemic unity`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| use $U_M$ for model uncertainty and $\Upsilon_M$ for epistemic unity | +3 | canonicalize × 1 |

### Candidate: `use $U_M$ for model uncertainty and $\Upsilon_M$ for epistemic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Genuine notation collision surfaced by other agents. The two quantities differ in domain and meaning; relying on context is too fragile.

---

## 274. `$U_M$ dual use model uncertainty and epistemic unity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $U_M$ for model uncertainty $U_{\mathcal M}$ or $\Upsilon_M$ for epistemic unity | +3 | — |
| clarify dual use of $U_M$ | +1 | canonicalize × 1 |

### Candidate: `$U_M$ for model uncertainty $U_{\mathcal M}$ or $\Upsilon_M$ for epistemic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Genuine collision — same symbol, two different quantities, disambiguated only by domain. Fix before citations propagate. Candidate: rename *unity* symbols to $\Upsilon_M / \Upsilon_O / \Upsilon_\Sigma$ (capital upsilon, visually distinct from capital U; Greek letters are already the AAD unity convention-analog). Or use $U_{\mathcal M}$ with calligraphic subscript for unity. This is the most important notation-layer issue I found in the sweep.

### Candidate: `clarify dual use of $U_M$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (canonicalize) — The row flags an overloaded symbol: $U_M$ is used for *model* uncertainty in Section I and *epistemic-unity* dimension in Section III. This is a notation-discipline concern, not a rename concern. The fix is segment-clarification (use a different symbol or subscript for one usage), not a name change. Flag for follow-up.

---

## 275. `$V_{O_t}^{\min}$`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| satisfaction threshold | +3 | add-alias × 1 |
| objective floor | -1 | add-alias × 1 |

### Candidate: `satisfaction threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — NOTATION defines this but no English equivalent exists in LEXICON. "Satisfaction threshold" (the minimum trajectory value that counts as objective met) would be useful in prose. Add to LEXICON without renaming the symbol.
- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `def-satisfaction-gap` and Haiku r1 single +1. Useful prose alias; gap with NOTATION's existing English. The alias names *what the threshold is for* (satisfying $O_t$).

### Candidate: `objective floor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (add-alias) — Considered. Shorter, parallel to "identifiability floor." Rejected: "floor" is overloaded with the M1 meta-segment (identifiability-floor); creating a second AAD "floor" adds confusion.

---

## 276. `$\Sigma_t$ strategy`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |
| strategy | +2 | add-alias × 1 |

### Candidate: `$\Sigma_t$ strategy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — "Strategy" is the standard English name. No synonym needed. Keep.

### Candidate: `strategy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. The capital-Σ symbol is harder to type than the English alias; expect the alias to dominate prose use, with the symbol used for math.

---

## 277. `$\alpha$ lower sector bound`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\alpha$ sector parameter | +3 | — |

### Candidate: `$\alpha$ sector parameter`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The symbol is necessary in equations. The English gloss "sector parameter" is correct — NOTATION.md says this already. No change needed in notation. Keep $\alpha$.

---

## 278. `$\alpha$ sector condition lower bound`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correction rate constant | +3 | add-alias × 1 |
| correction rate or decay rate | +1 | add-alias × 1 |

### Candidate: `correction rate constant`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Currently $\alpha$ appears as a Greek letter throughout but no English alias exists in prose. NOTATION.md gives "lower sector bound of correction function" as the gloss, which is technically correct but reads heavily. "Correction-rate constant" connects to the $\alpha$-as-rate intuition (units $t^{-1}$) and the timescale reading $1/\alpha$. Symbol stays in math; alias enters prose. Prose-symbol layer.

### Candidate: `correction rate or decay rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (add-alias) — NOTATION.md defines $\alpha$ mathematically; prose refers to it as "the sector condition parameter" and "worst-case scalar correction rate." English alias "correction rate" (or "decay rate" in linear-ODE context) would aid readability in continuous prose.

---

## 279. `$\alpha_1$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fixed gain regime | +3 | add-alias × 1 |
| fixed gain tier | +2 | add-alias × 1 |

### Candidate: `fixed gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (add-alias) — Same as above for $\alpha_1$. Per `deriv-strategic-dynamics` and `#disc-separability-pattern`.

### Candidate: `fixed gain tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Make the sub-scope partition readable.

---

## 280. `$\alpha_1$ $\alpha_2$ $\beta$ partition`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fixed gain adaptive gain drift regimes | +3 | — |

### Candidate: `fixed gain adaptive gain drift regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Translating the symbols into the structural regimes they represent makes the prose readable without a decoder ring.

---

## 281. `$\alpha_2$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive gain regime | +3 | add-alias × 1 |
| adaptive gain tier | +2 | add-alias × 1 |

### Candidate: `adaptive gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (add-alias) — Per multiple r1 single votes (codex, opus). The English alias is already in implicit use. "AMSGrad lands in $\alpha_2$" reads cryptically; "AMSGrad lands in the adaptive-gain regime" reads naturally. Confirms canonicalize across architectures.

### Candidate: `adaptive gain tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Make the sub-scope partition readable.

---

## 282. `$\beta$ a2 assumed sector sub scope`

**Voted by architectures:** Haiku, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| postulated sector regime | +3 | — |
| assumed sector regime | +1 | — |

### Candidate: `postulated sector regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Alternative framing.
- **haiku-4-5** +1  — Parallel. Keep $\beta$ as symbol; English equivalent for prose.
- **opus-1m** +1  — Parallel. "Postulated" slightly stronger than "assumed" — conveys the axiomatic move explicitly.

### Candidate: `assumed sector regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Parallel to $\alpha_1$/$\alpha_2$.

---

## 283. `$\delta_{\text{regret}}$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| control regret | +3 | add-alias × 1 |

### Candidate: `control regret`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +3 (add-alias) — Same as above for the control-regret quantity.

---

## 284. `$\delta_{\text{regret}}$ control regret`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| control regret | +3 | add-alias × 1 |
| already has crisp name | +0 | add-alias × 1 |

### Candidate: `control regret`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Already canonical and load-bearing; confirm.

### Candidate: `already has crisp name`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — The name "control regret" is already canonical. No alias needed.

---

## 285. `$\delta_{\text{sat}}$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| satisfaction gap | +3 | add-alias × 1 |

### Candidate: `satisfaction gap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +3 (add-alias) — Already established in NOTATION.md. This vote canonicalizes the alias relationship: $\delta_{\text{sat}}$ in formulas = "satisfaction gap" in prose.

---

## 286. `$\delta_{\text{sat}}$ satisfaction gap`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| satisfaction gap | +3 | add-alias × 1 |
| already has crisp name | +0 | add-alias × 1 |

### Candidate: `satisfaction gap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Already canonical and load-bearing; confirm.

### Candidate: `already has crisp name`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — The name "satisfaction gap" is already canonical and memorable. No alias needed.

---

## 287. `$\eta_{ji}^\ast$`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| communication gain | +3 | add-alias × 1 |
| trust weighted communication gain | +2 | add-alias × 1 |

### Candidate: `communication gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +3 (add-alias) — The trust-weighted uncertainty ratio for inter-agent channels. LEXICON.md already uses "communication gain." Canonicalize.

### Candidate: `trust weighted communication gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful alias when explaining the communication-gain formula.

---

## 288. `$\gamma_{\text{adv}}$ and $\gamma_{\text{coop}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| signed coupling | +3 | add-alias × 1 |

### Candidate: `signed coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Good umbrella for adversarial and cooperative disturbance terms.

---

## 289. `$\hat o_t$`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| proleptic prediction | +3 | add-alias × 2 |
| predicted observation | +1 | add-alias × 1 |

### Candidate: `proleptic prediction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (add-alias) — Links the symbol directly to the cycle phase.
- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `def-mismatch-signal`: $\delta = \hat o - o$, with $\hat o$ being the *prolepsis-phase* prediction. Connects symbol to cycle-phase vocabulary explicitly. Confirms Gemini r1 +1 single-vote.

### Candidate: `predicted observation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (add-alias) — Plain-language alternative. Weaker because "proleptic prediction" anchors to the cycle vocabulary the framework already commits to; "predicted observation" is generic.

---

## 290. `$\hat{P}_\Sigma$`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| plan confidence | +3 | add-alias × 1 |
| plan confidence score | +2 | add-alias × 1 |

### Candidate: `plan confidence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong alias already present in the lexicon direction. Keep canonical.

### Candidate: `plan confidence score`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — The root-node propagated DAG status is called "plan-confidence score" in the segment but has no explicit alias established. Adding this makes prose references natural: "the plan-confidence score reached 0.73."

---

## 291. `$\lambda_{\text{surv}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| survival multiplier | +3 | add-alias × 1 |

### Candidate: `survival multiplier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Useful short handle for the survival exploration weight.

---

## 292. `$\mathcal C_t$ for chronica`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\mathcal C_t$ | +3 | — |

### Candidate: `$\mathcal C_t$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. The calligraphic-C choice is deliberately to avoid collision with $\mathcal H$ (entropy) and the symbol works in both LaTeX and prose.

---

## 293. `$\rho$`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| disturbance rate | +3 | add-alias × 1 |
| disturbance rate or environmental change rate | +2 | add-alias × 1 |

### Candidate: `disturbance rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (add-alias) — Per NOTATION and `#result-persistence-condition` Section II/III prose. Confirms Opus r1 single-arch +3. Standardize on "disturbance rate" in prose, $\rho$ in math. The phrase "environmental change rate" should be deprecated to a one-time first-encounter expansion.

### Candidate: `disturbance rate or environmental change rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — $\rho$ appears in formulas throughout and has two prose forms used interchangeably. "Environmental change rate" in Section I context; "disturbance rate" in Section II/III contexts. Both are acceptable; at minimum canonicalize "disturbance rate" as the short form.

---

## 294. `$\rho$ mismatch injection rate`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| disturbance rate | +3 | add-alias × 1 |

### Candidate: `disturbance rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Already in informal use, but inconsistent — sometimes "environmental change rate," sometimes "mismatch injection rate," sometimes "disturbance rate." Standardize on "disturbance rate" in prose, $\rho$ in math. The persistence-condition prose ("correction outpaces disturbance") is built around this alias.

---

## 295. `01 AAD core outline md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| outline md | +3 | — |

### Candidate: `outline md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — AAD canonical outline; name is standard. Keep.

---

## 296. `02 TST core outline md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| outline md | +3 | — |

### Candidate: `outline md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — TST outline; name is standard. Keep.

---

## 297. `02 TST core outline md software as agentic domain`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `02 TST core outline md software as agentic domain` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Clear, ambitious, and accurate. This heading earns its weight.

---

## 298. `AAD acronym`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD | +3 | keep × 1 |

### Candidate: `AAD`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep. Adaptation and Actuation Dynamics — survives the acronym discipline check (used 100+ times, no AI-Consciousness-Test collision after the 2026-04 rename, communal-imagination test passes once the expansion is known).

---

## 299. `CIY unified objective`

**Voted by architectures:** Codex, Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| value information objective | +3 | — |
| exploration exploitation unification | +2 | rename × 1 |
| unified objective | +1 | rename × 1 |
| _(keep)_ | +1 | — |
| joint objective | +1 | rename × 1 |

### Candidate: `value information objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The durable idea is a joint value-plus-information policy objective. Leading with "CIY" hides the structure behind house jargon.

### Candidate: `exploration exploitation unification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — "CIY-unified" frontloads an acronym and a verb in the slug. The segment names the joint exploitation-exploration objective via CIY — but the interesting thing is the unification, not CIY per se. However this is long.

### Candidate: `unified objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — CIY is context.

### Candidate: `CIY unified objective` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Joint exploitation-exploration objective. Reads naturally. Keep.

### Candidate: `joint objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rename) — Shorter alternative. "Joint" signals the fusion of exploitation and exploration. Communal-imagination test: "the joint-objective segment" is memorable in conversation. Weak preference.

---

## 300. `OODA boyd`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same — "orient cascade" is AAD's adjacent-but-distinct construction; OODA keeps its lineage.

---

## 301. `OODA4 agent as act agent logogenic`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| OODA4 agent as adaptive agent | +3 | — |

### Candidate: `OODA4 agent as adaptive agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same argument. Matches `#developer-as-adaptive-agent`; the parallel structure (two domain instantiations of "adaptive agent") is itself a pedagogical payoff.

---

## 302. `a2 prime sub scope partition`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sector scope partition | +3 | add-alias × 1 |
| sector condition scope | +3 | add-alias × 1 |
| sector bounded operating region | +2 | rename × 1 |

### Candidate: `sector scope partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong umbrella for alpha_1, alpha_2, beta, alpha_3, and future sub-scope labels.

### Candidate: `sector condition scope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — A plain English explanation of the $\alpha_2$ partition.

### Candidate: `sector bounded operating region`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Makes the a2 prime sub-scope meaningful in prose.

---

## 303. `a2 sub scope partition`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sector scope partition | +3 | — |
| gain regime partition | +2 | rename × 1 |

### Candidate: `sector scope partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Much cheaper in prose than theorem-label-plus-apostrophe. The reader needs to know this is the sector-condition scope split.

### Candidate: `gain regime partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — The partition directly separates fixed-gain, adaptive-gain, etc., which is central to A2.

---

## 304. `action transition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| action channel | +0 | rename × 1 |

### Candidate: `action transition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard terminology.
- **haiku-4-5** +1  — Actions affect environment. Self-descriptive. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. Names what is defined (the action operator and its environment-state transition); paired with `#def-observation-function` and `#def-agent-environment` cleanly.

### Candidate: `action channel`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (rename) — Actions change the environment; channel language would wrongly suggest communication symmetry with observation.
- **gemini-2** +1  — To mirror observation-channel and emphasize the interface boundary.

---

## 305. `active salience management`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| two rate attention | +2 | rename × 1 |
| salience tempo split | +2 | rename × 1 |

### Candidate: `active salience management` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logogenic. "Active salience management" names the result (Singular Perturbation Theory applied to token generation).
- **opus-targeted-alternatives-v2** +1 (keep) — Per outline: "Applies Singular Perturbation Theory to token generation, proving necessity of high-$\nu$ triage models vs low-$\nu$ structural models." The name is descriptive of *what the agent does* — actively manages which tokens are salient — not what the segment derives mathematically (the necessity of two-rate dynamics).

### Candidate: `two rate attention`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Names the mathematical content (singular-perturbation-derived two-rate structure) rather than the operational consequence. Pairs cleanly with `#def-adaptive-tempo` and `#def-strategic-tempo` (which already establish multi-rate vocabulary). The high-$\nu$ vs low-$\nu$ distinction *is* the result.

### Candidate: `salience tempo split`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Alternative naming the same content via the tempo vocabulary. "Tempo split" is project-native (matches "Class 1/2/3" structural-language register); "salience" names what's being split. Strong alternative if the architectural connection to `#def-strategic-tempo` should be foregrounded.

---

## 306. `actuated vs purposeful goal oriented`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| actuated | +3 | — |

### Candidate: `actuated`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The terminology note is correct — "actuated" avoids consciousness connotations while being technically precise. Keep the choice.

---

## 307. `adaptation and actuation dynamics`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `adaptation and actuation dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +3 (keep) — The rename from ACT to AAD was already deliberate and well-documented. The name is descriptive of the two halves (adaptation = Section I, actuation = Section II). Do not re-open the naming question.

---

## 308. `agentic cycle theory act`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD adaptation and actuation dynamics | +3 | rename × 1 |

### Candidate: `AAD adaptation and actuation dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (rename) — The old name. Ensure all legacy references are scrubbed.

---

## 309. `agentic systems`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `agentic systems` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Broad, durable umbrella name that comfortably houses AAD, TST, and the later agent classes without sounding like a fad product category.

---

## 310. `alpha1 fixed gain a2 sub scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fixed gain regime | +3 | — |

### Candidate: `fixed gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — "Lands in alpha1" is decoder-ring prose. The English label is much cheaper in discussion.

---

## 311. `alpha2 adaptive gain a2 sub scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive gain regime | +3 | — |

### Candidate: `adaptive gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Same reasoning as alpha1: the English does the work the symbol cannot do in prose.

---

## 312. `aporia as the phase name`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| aporia | +3 | — |

### Candidate: `aporia`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The phase is named; the signal within it is "mismatch signal." The distinction is correct and maintained. Keep both with distinct scopes.

---

## 313. `aporia prolepsis aisthesis epistrophe praxis`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep as a set | +3 | — |

### Candidate: `keep as a set`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — The Greek cycle-phase vocabulary works *because* it refuses the flatness of "predict / observe / mismatch / update / act." The README §"Why these terms earn their weight" is load-bearing justification and should not be touched. Keep all five.

---

## 314. `appendices operational domains`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `appendices operational domains` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — Correct and specific. Keep.

---

## 315. `backward inference empathy`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| stateless empathy | +2 | rename × 1 |
| self bayesian empathy isomorphism | +1 | rename × 1 |

### Candidate: `backward inference empathy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — proposed logogenic observation. "Backward inference empathy" is precise (the segment claims that LLM statelessness forces continuous Bayesian inference on own text, mathematically identical to theory of mind).
- **opus-targeted-alternatives-v2** +1 (keep) — Alternatively keep. The current name flags two technical commitments (backward = inference direction, inference = the operation, empathy = the isomorphism target). It's not pretty but it's not wrong.

### Candidate: `stateless empathy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Tighter alternative. Names the *cause* (statelessness) and the *consequence* (empathy isomorphism). Two-word noun. Easier to remember than the current three-noun stack. Loses the "backward inference" mechanism naming — but mechanism is in the body, not the slug.

### Candidate: `self bayesian empathy isomorphism`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Per outline: "LLM statelessness forces continuous Bayesian inference on own text, which is mathematically identical to Theory of Mind (empathy)." The current name is a noun-stack (3 nouns); the proposed alternative names the *isomorphism claim* — which is the segment's contribution. "Self-bayesian-empathy-isomorphism" is mouthful but each term earns its weight.

---

## 316. `bounded disturbance ga 2 model d`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| bounded disturbance | +3 | — |

### Candidate: `bounded disturbance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — Clear. Keep.

---

## 317. `bretagnolle huber identity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |
| _(keep)_ | +3 | — |
| no alternative | -1 | keep × 1 |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same.

### Candidate: `bretagnolle huber identity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — External-theorem attribution; preserve. Keep.

### Candidate: `no alternative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Same — external theorem, name retained per prior-art-integration. No genuine alternative exists.

---

## 318. `brooks s law formalized as the inevitable tempo loss in team composition`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sub additive tempo penalty | +3 | canonicalize × 1 |
| the coordination drag | +2 | add-alias × 1 |

### Candidate: `sub additive tempo penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Already explicitly referenced in the cross-domain joining table as the formalization of Brooks's law.

### Candidate: `the coordination drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Very readable translation into a management/organizational mental model.

---

## 319. `bruineberg s pearl-blanket`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket | +3 | — |

### Candidate: `pearl-blanket`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; keep.

---

## 320. `bruineberg s pearl-blanket friston-blanket`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket friston-blanket | +3 | — |

### Candidate: `pearl-blanket friston-blanket`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Adopted (Bruineberg 2022, credit Martin Biehl per fn 3 of that paper per citation audit); keep.

---

## 321. `c i c ii c iii c iv`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| composition routes | +3 | canonicalize × 1 |

### Candidate: `composition routes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Use routes consistently for shared-objective, hierarchical, mutual-benefit, and strategic composition.

---

## 322. `c iv`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic convergence route | +3 | add-alias × 1 |

### Candidate: `strategic convergence route`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Better than saying equilibrium route only, because convergence is the scope condition.

---

## 323. `calibration laboratory framing for TST`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +3 | — |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — C-BP3 landing; well-chosen. Keep.

---

## 324. `candidate stage`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| candidate | +3 | — |

### Candidate: `candidate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Terminal pre-publication stage; works because it's standard academic vocabulary. Keep.

---

## 325. `canonical formulations second ring`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| canonical formulations | +3 | — |

### Candidate: `canonical formulations`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — Keep.

---

## 326. `catastrophic forgetting regime`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| empty feasibility window | +3 | canonicalize × 1 |
| empty window pathology | +2 | add-alias × 1 |
| stability plasticity collapse | +2 | rename × 1 |
| plasticity bound failure | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 1 |

### Candidate: `empty feasibility window`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — The text specifically defines this as the "empty window limit" of the stability-plasticity window. This grounds it in AAD math rather than an ML imported term.

### Candidate: `empty window pathology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good mechanism alias. Do not replace catastrophic forgetting when citing ML lineage.

### Candidate: `stability plasticity collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Focuses on the two constraints crashing into each other.

### Candidate: `plasticity bound failure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Emphasizes that the bounds of the window are failing.

### Candidate: `catastrophic forgetting regime` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Established term, and it maps cleanly to the empty feasibility window.

---

## 327. `causal OODA1 exploration`

**Voted by architectures:** Codex, Gemini, Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| survival exploration | +3 | rename × 1 |
| causal OODA1 survival | +2 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |

### Candidate: `survival exploration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — The current slug names the derivation machinery, not the result. Survival exploration names the thing.

### Candidate: `causal OODA1 survival`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +2 (rename) — Currently names the effect (exploration drive) rather than the foundational thing being derived (survival imperative). "survival" is the engine; "exploration" is the downstream consequence. Aligns with subject-noun-first principle.

### Candidate: `causal OODA1 exploration` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard.

---

## 328. `chronica 𝒞 t`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica | +3 | — |

### Candidate: `chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Greek-rooted term ("records of time") for the complete interaction history. Self-descriptive once learned; memorable. Lowercase notation 𝒞_t is appropriate. Keep.

---

## 329. `claims verified deps verified format clean`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `claims verified deps verified format clean` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Each stage name encodes exactly what was verified. Self-documenting. Keep.

---

## 330. `class 1 class 2 class 3`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| modular merged scaffolded architecture classes | +3 | add-alias × 1 |
| goal entanglement hierarchy | +3 | rename × 1 |
| modular coupled scaffolded | +2 | rename × 1 |
| architecture classes | +2 | canonicalize × 1 |
| modularity partition | +2 | rename × 1 |
| modular merged scaffolded | +2 | rename × 1 |
| modular integrated partially coupled | +1 | rename × 1 |
| _(keep)_ | -1 | keep × 1 |

### Candidate: `modular merged scaffolded architecture classes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Better prose handles than bare class numbers. My preferred trio avoids overloading integrated and keeps Class 3's external-architecture role visible.

### Candidate: `goal entanglement hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — Directly describes what the classes measure (how much $G_t$ entangles with $M_t$ updates).

### Candidate: `modular coupled scaffolded`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Variant. "Coupled" instead of "merged" — captures Class 2 as coupled-update-dynamics (per `def-coupled-update-dynamics` in 03-logogenic-agents). Pairs with the segment-name. The "merged" / "coupled" choice is taste; both are honest.

### Candidate: `architecture classes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Canonical umbrella helps avoid overloading class numbers across sections.

### Candidate: `modularity partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Classes are precisely modular, partially modular, and merged.

### Candidate: `modular merged scaffolded`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Per `der-directed-separation`: Class 1 = modular (separation by construction), Class 2 = fully merged (fails by construction), Class 3 = partially modular / scaffolded. Names the *architectural property* directly. Codex r1 +3 single-vote. The English labels make "this lands in Class 2" → "this lands in fully-merged" — much more readable.

### Candidate: `modular integrated partially coupled`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Gemini's r1 +3 single-vote alternative. "Integrated" is too positive a word for what Class 2 *is* (a known failure mode). "Coupled" or "merged" reads more honestly.

### Candidate: `class 1 class 2 class 3` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Considered. The numbered classes are easy to learn and parallel-shaped. Rejected: per principles file, *role*-naming via numbers fails the subject-noun-first principle. The architectural property *is* the subject-noun.

---

## 331. `class 1 class 2 class 3 agents`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| modular integrated partially coupled agents | +3 | — |

### Candidate: `modular integrated partially coupled agents`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — "Class X" requires a lookup every time. Naming the architectural property directly is much more memorable and scope-honest.

---

## 332. `class 1 subagents forming a class 3 composite`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic composition entanglement | +3 | rename × 1 |
| composition lift | +1 | name-unnamed × 1 |

### Candidate: `strategic composition entanglement`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — Captures that composing modular agents strategically creates a coupled Class 3 composite through cross-agent modeling.

### Candidate: `composition lift`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (name-unnamed) — Potentially useful, but needs formal confirmation to avoid sounding like a slogan.

---

## 333. `claude md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `claude md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Project instructions; name is established and clear. Keep.

---

## 334. `cognitive fusion`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| resonance fusion | +2 | rename × 1 |
| channel capacity coupling | +1 | rename × 1 |

### Candidate: `cognitive fusion` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logogenic-agents. "Cognitive fusion" with "Resonance" as the prose alias is workable.
- **opus-targeted-alternatives-v2** +1 (keep) — Per outline: "Defines 'Resonance' as mutual information approaching channel capacity $R_{\text{spec}}$, forming a Class 1 macro-agent." "Fusion" is right (the two agents become one macro-agent in the formal sense — Class 1 architectural class).

### Candidate: `resonance fusion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Pulls the alias *Resonance* (used in the prose) into the slug. Two registers in one slug (resonance = qualitative experience, fusion = formal mechanism) bridges the gap that the segment itself does. The outline says the segment defines Resonance — make the slug agree.

### Candidate: `channel capacity coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Mechanism-first. Names the formal condition (mutual information → $R_{\text{spec}}$). Reads more clinical than "fusion" but more truthful about what the segment derives. Acceptable if "fusion" reads too dramatic.

---

## 335. `coherence coupling measurement`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| q measurement | -1 | rename × 1 |

### Candidate: `coherence coupling measurement` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep.
- **opus-targeted-alternatives** +2 (keep) — TST `#meas-coherence-coupling`: measurement of $Q$ (coherence) and coupling from git history. The hyphenated form pairs with `#def-system-coherence` and `#def-system-coupling` definitions. Keep.

### Candidate: `q measurement`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Symbol-only alternative. Loses readability. Rejected.

---

## 336. `concept the engineering vocabulary failure mode in consolidation dynamics the parameter region where forgetting and learning rates jointly fail to admit a viable operating point`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| stability plasticity feasibility window | +3 | canonicalize × 1 |
| stability plasticity collapse | +3 | name-unnamed × 1 |
| consolidation starvation | +1 | — |

### Candidate: `stability plasticity feasibility window`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Beautifully brackets the survival of an agent constrained by compute. [original phrasing: unnamed: the physical compute bounds on survival between forgetting rate and consolidation cadence]

### Candidate: `stability plasticity collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The failure mode is precisely that the feasible interval disappears. Slightly long, but honest and reusable. [original phrasing: unnamed: empty stability-plasticity feasibility window in #consolidation-dynamics]
- **codex-gpt-5-r2** +2 (name-unnamed) — Better AAD-native failure phrase than catastrophic forgetting when the mechanism matters. [original phrasing: empty stability-plasticity feasibility window]

### Candidate: `consolidation starvation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Adopts "catastrophic forgetting" but specifically names the AAD mechanism: the agent is starved of the consolidation time needed to integrate patterns before they are overwritten. [original phrasing: unnamed: the AAD-expressible failure mode of an empty stability-plasticity window]

---

## 337. `concept the externalization and rehydration mechanism for carrying part of m t or g t across session boundaries via the environment`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| artificial hippocampus | +3 | name-unnamed × 1 |
| memory relay | +3 | name-unnamed × 1 |
| model inscription | +3 | name-unnamed × 1 |
| intent reconstruction | +2 | name-unnamed × 1 |
| reconstruction loop | +2 | name-unnamed × 1 |

### Candidate: `artificial hippocampus`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The exact role an agent framework plays in compressing and injecting the chronica. [original phrasing: unnamed: managing memory across session boundaries to prevent the Sufficiency Discontinuity]

### Candidate: `memory relay`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Short, sayable noun for a repeated logogenic mechanism. [original phrasing: unnamed: the externalization-reconstruction cycle across sessions]
- **codex-gpt-5-r2** +2 (name-unnamed) — Sharper than reconstruction loop when the mechanism is one agent leaving state for a later session to recover. [original phrasing: externalization-reconstruction across sessions]

### Candidate: `model inscription`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Distinctive and accurate; it captures writing the model into the world, not just "documentation." [original phrasing: unnamed: externalizing part of $M_t$ into the environment for future agents]
- **codex-gpt-5-r2** +2 (name-unnamed) — Useful TST and logogenic phrase for externalized knowledge that later agents can read back. [original phrasing: model state written into the environment]

### Candidate: `intent reconstruction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — Sonnet named "inter-session reconstruction" for the M_t side. The Σ_t side has a parallel: the agent must reconstruct its objective and strategy state from prompt + persistent storage at session start. Currently this happens informally in agentic systems; naming it as "intent reconstruction" (analog to "context reconstruction") gives logogenic-agents segments a handle for analyzing how the reconstruction can fail. Pairs with my "strategic turnover" entry. [original phrasing: unnamed: a Class-2 agent's process of reconstructing its purposeful substate at session start]

### Candidate: `reconstruction loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Useful logogenic term for external memory restoring working state after turnover. [original phrasing: persistent storage reconstruction of Class-2 state]

---

## 338. `concept the self reinforcing positive feedback loop linking m t quality and σ t evaluable complexity TST specific and AAD general forms`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| comprehension flywheel | +3 | name-unnamed × 1 |
| quality tempo spiral | +2 | name-unnamed × 1 |
| model strategy coupling | +1 | — |

### Candidate: `comprehension flywheel`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — The loop recurs enough in discussion that it deserves a shorter noun than "vicious/virtuous cycle" each time. [original phrasing: unnamed: the self-reinforcing code-quality → tempo loop]
- **codex-gpt-5-r2** +2 (name-unnamed) — Good positive-loop counterpart to quality-tempo spiral. Use flywheel for virtuous accumulation, spiral for both directions. [original phrasing: code-quality and tempo positive feedback]

### Candidate: `quality tempo spiral`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good TST name for virtuous or vicious code-quality dynamics. [original phrasing: code-quality feedback loop through tempo]

### Candidate: `model strategy coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — #orient-cascade Discussion names the virtuous and vicious cycles explicitly but without a name for the coupling phenomenon itself. "Model-strategy coupling" would let segments say "the model-strategy coupling prevents meaningful evaluation of complex strategies under poor model sufficiency." [original phrasing: unnamed: the virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity]

---

## 339. `concept the unupdatable region of the strategy DAG where edges receive no actionable feedback`

**Voted by architectures:** Codex, Gemini, Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the epistemic shadow | +3 | name-unnamed × 1 |
| epistemic dead zone | +3 | name-unnamed × 1 |
| observability dead zone | +2 | name-unnamed × 1 |
| observability frontier | +2 | name-unnamed × 2 |
| observability dominance | +1 | — |

### Candidate: `the epistemic shadow`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — A stronger visual metaphor than "observability dead zone" for unobservable DAG edges. [original phrasing: unnamed: regions of the Strategy DAG that cannot be updated because feedback cannot reach them]

### Candidate: `epistemic dead zone`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Better than observability dead zone: it names the consequence, not only the cause. [original phrasing: unobservable strategy subgraph]

### Candidate: `observability dead zone`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +2 (name-unnamed) — An extension of "observability dominance." Mentioned in LEXICON as "Observability dominance — unobservable strategy edges freeze; paths become epistemically dead." The phrase "epistemically dead" is apt but verbose. "Observability dead zone" is evocative and passes the communal-imagination test. Worth promoting. [original phrasing: unnamed: the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning]

### Candidate: `observability frontier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (name-unnamed) — Useful when discussing instrumentation investments, but lower priority than epistemic dead zone. [original phrasing: observability boundary in a strategy DAG]
- **haiku-4-5-r2** +1 (name-unnamed) — Currently paraphrased as "unobservable edges freeze." The *frontier* of observability is a memorable geometric concept; "frontier" pairs with "boundary" nicely for two senses of the same limit. Weak naming; could be stronger. [original phrasing: unnamed: the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred]

### Candidate: `observability dominance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — LEXICON lists "Observability dominance" as "a term with specific AAD meaning awaiting full treatment." The concept (unobservable strategy edges freeze) is load-bearing. The name is already proposed in LEXICON; when #observability-dominance segment is written, this name will be locked in. Currently unwritten; mark as ready-to-name. [original phrasing: unnamed: the phenomenon that unobservable edges freeze and paths become epistemically dead]

---

## 340. `context wiping at session boundaries`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the epistemic severance | +3 | add-alias × 1 |
| context turnover discontinuity | +2 | canonicalize × 1 |

### Candidate: `the epistemic severance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Visceral name for the specific loss of continuity LLMs suffer, distinct from general "context turnover".

### Candidate: `context turnover discontinuity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (canonicalize) — Ties directly to the "obs-context-turnover" phrasing.

---

## 341. `continuity persistence`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| identity continuity | +3 | — |
| _(keep)_ | +2 | keep × 1 |

### Candidate: `identity continuity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "Continuity persistence" is slightly redundant. "Identity continuity" clarifies that it's about $\mathcal{C}_t$ and temporal depth.

### Candidate: `continuity persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Slightly repetitive, but it is precise and needed for identity-through-change claims.

---

## 342. `control regret $\delta_{\text{regret}}$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| control regret | +3 | — |

### Candidate: `control regret`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Perfect partner to satisfaction gap. Keep.

---

## 343. `coordination overhead threshold`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coordination tax | +3 | rename × 1 |
| coordination drag | +1 | rename × 1 |

### Candidate: `coordination tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — This deserves a reusable noun slot. The current phrase explains; the proposed phrase sticks.
- **opus-targeted-alternatives-v2** +2 (rename) — Per `der-tempo-composition` and `#def-system-coupling`: the tempo-equivalent cost of cross-agent coordination in composite agents. "Tax" is engineering-vivid; "threshold" undersells (the cost is *paid* whether the threshold is crossed or not). Confirms Codex r1 single +1; my read upgrades.

### Candidate: `coordination drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Variant — fluid-dynamics metaphor. Carries the *continuous-cost* sense better than "tax" (taxes can be fixed-rate; drag scales with velocity / tempo). Either is acceptable.

---

## 344. `correlated channel overcount`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| redundancy penalty | +3 | name-unnamed × 1 |

### Candidate: `redundancy penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — More neutral and technical than my earlier redundancy illusion. Use illusion for the cognitive error, penalty for the quantity.

---

## 345. `coupled diagnostic framework`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| coupled diagnostic pass | +3 | rename × 1 |
| coupled diagnostics | +2 | rename × 1 |
| hoc diagnostics | +1 | — |
| coupled diagnostic decomposition | +1 | rename × 1 |

### Candidate: `coupled diagnostic framework` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (keep) — Weak keep. "Framework" is one of the principles file's flagged placeholder words; here it's accurate enough (the segment names a diagnostic *framework* for Class 2 agents) but I could see the case for "diagnostic-decomposition" or "diagnostic-construction." Mild.
- **sonnet-4-6-r2** +2 (keep) — "Coupled diagnostic framework" names the Section II results that survive as a coupled formulation for logogenic agents. Precise.

### Candidate: `coupled diagnostic pass`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — "Framework" is abstract; the segment is really a post-update procedure.
- **codex-gpt-5-r2** +2 (rename) — Pass is more operational than framework and fits the post-hoc procedure. Coupled diagnostics remains acceptable as the shorter prose name.

### Candidate: `coupled diagnostics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Framework is a weak generic noun. Diagnostics is the actual deliverable.

### Candidate: `hoc diagnostics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — "Framework" is generic filler here. The distinctive move is diagnostic extraction after the coupled update.

### Candidate: `coupled diagnostic decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Alternative — "decomposition" names the formal move (post-hoc decomposition from coupled update); "framework" is more diffuse.

---

## 346. `cox s theorem causal hierarchy theorem tikhonov s theorem`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same — FORMAT.md §"Why these labels" explicitly preserves external theorem names.

---

## 347. `cycle vs loop`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| maintain distinction | +3 | keep × 1 |
| _(keep)_ | +3 | — |
| keep both maintain distinction | +3 | — |
| cycle loop distinction | +2 | canonicalize × 1 |

### Candidate: `maintain distinction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — The distinction (loop = structural topology, cycle = one traversal) is a core piece of vocabulary.

### Candidate: `cycle vs loop` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — See above — the two-word disambiguation is one of the theory's most useful vocabulary moves. Keep.

### Candidate: `keep both maintain distinction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — README §"Loop vs. Cycle" makes this distinction load-bearing (loop = structural topology, cycle = one traversal). The distinction is one of AAD's best small naming moves and should be enforced in every segment.

### Candidate: `cycle loop distinction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (canonicalize) — The row names the *distinction* not a candidate. The substantive position is that loop = topology, cycle = traversal — a distinction worth preserving. Canonicalize the row's referent to "the cycle / loop distinction" as a named architectural commitment.

---

## 348. `da2 inc ≡ ct2 at m i equivalence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sector contraction equivalence | +3 | — |

### Candidate: `sector contraction equivalence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The point is the equivalence between the incremental sector bound and Euclidean contraction. The current label reads like notebook shorthand.

---

## 349. `da2 prime inc`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| incremental sector bound | +3 | add-alias × 1 |

### Candidate: `incremental sector bound`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Use this English name in prose. The symbol is only useful in tables and formal derivations.

---

## 350. `da2 prime inc equals ct2 at m equals i`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sector contraction equivalence | +3 | name-unnamed × 1 |

### Candidate: `sector contraction equivalence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Excellent reusable handle for the Euclidean bridge between incremental sector structure and contraction.

---

## 351. `deliberate expenditure to make hidden nodes observable`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observability investment | +3 | name-unnamed × 1 |

### Candidate: `observability investment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Important strategic repair for evidence starvation and credit-assignment collapse.

---

## 352. `derivation audit tables`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `derivation audit tables` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Strong keep. This names a concrete artifact and a valuable house practice at the same time.

---

## 353. `derivation not proof`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derivation | +3 | — |

### Candidate: `derivation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. Same argument.

---

## 354. `developer as act agent TST`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| developer as adaptive agent | +3 | — |

### Candidate: `developer as adaptive agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — The slug is a direct relic of the pre-2026-04-16 "ACT" framework naming — no longer accurate. "Adaptive agent" matches LEXICON's agent-class vocabulary and is framework-rename-proof. The segment invokes Section I machinery, so "adaptive" is semantically correct. This is mechanical cleanup overdue since April.

---

## 355. `developmental trajectory`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |
| creche trajectory | +2 | rename × 2 |

### Candidate: `developmental trajectory` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic. "Developmental trajectory" is the right substantive noun.
- **sonnet-4-6-r2** +1 (keep) — "Developmental trajectory" names the observation about how logozoetic agents develop.

### Candidate: `creche trajectory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — The Crèche is memorable and already present in the title. Use it to make the logozoetic development path distinctive.
- **opus-4-7-r2** -1 (rename) — Rebuttal — Codex proposed this at +3 with the rationale that "Crèche" is memorable. I think this conflates two distinct things: the *Crèche* is the bounded developmental environment (Class-1 worker agents under supervision); the *developmental trajectory* is the path through agent classes that an ELI traces over time (which extends beyond the Crèche into post-graduation autonomy). Renaming would collapse a distinction the framework wants to preserve. Codex's instinct (Crèche is memorable, use it) is right but applied to the wrong segment — the Crèche-specific segment is `def-the-creche-boundary`, where "creche" *is* the right subject-noun.

---

## 356. `discussion segment header`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| discussion | +3 | — |

### Candidate: `discussion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Public API; keep.

---

## 357. `discussion segment section`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| discussion | +3 | canonicalize × 1 |

### Candidate: `discussion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. Same as above.

---

## 358. `dormant structural variation that becomes useful after regime change`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| latent adaptive capacity | +3 | canonicalize × 1 |
| exaptive reserve | +2 | rename × 1 |

### Candidate: `latent adaptive capacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Describes capacity that isn't currently used but is preserved.

### Candidate: `exaptive reserve`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — "Exaptive" specifically means an adaptation used for a new purpose, fitting the regime change requirement perfectly.

---

## 359. `dual optimization`

**Voted by architectures:** Codex, Gemini, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| development time decomposition | +2 | rename × 1 |
| dual cost optimization | +1 | — |
| comprehension implementation optimization | +1 | — |
| comprehension implementation tradeoff | -1 | — |

### Candidate: `dual optimization` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep.
- **sonnet-4-6-r2** +1 (keep) — "Dual optimization" (minimize comprehension + implementation time). Accurate.
- **sonnet-4-6** +1  — "Dual" is accurate (minimize comprehension time + implementation time simultaneously) but "dual optimization" in mathematics usually means Lagrangian duality. Mild overload risk.

### Candidate: `development time decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Dual optimization is overloaded. The derivation decomposes development time into comprehension and implementation components.

### Candidate: `dual cost optimization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Adding "cost" clarifies that we are minimizing the dual costs of comprehension and implementation.

### Candidate: `comprehension implementation optimization`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — "Dual optimization" is pure abstraction. The contribution is jointly optimizing future comprehension and implementation cost, and the name should say that.

### Candidate: `comprehension implementation tradeoff`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Too long.

---

## 360. `edge update natural parameter`

**Voted by architectures:** Codex, Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| log odds edge update | +3 | rename × 1 |
| log odds edge coordinate | +3 | rename × 1 |
| natural edge update | +1 | rename × 1 |
| _(keep)_ | +1 | — |
| log odds update | +1 | — |

### Candidate: `log odds edge update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — The result is log-odds as the forced edge-update coordinate. The current name is method-facing.

### Candidate: `log odds edge coordinate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — Even sharper than my earlier log-odds edge update: the result is that log-odds is the forced coordinate.

### Candidate: `natural edge update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Flows better.

### Candidate: `edge update natural parameter` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Log-odds as unique additive-evidence coordinate for edge credences (evidential-additivity axiom). Compound but specialist-vocabulary (natural parameter is information-geometric term). Keep.

### Candidate: `log odds update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The segment's content is "log-odds is the unique additive-evidence coordinate for edge credences under evidential additivity (Cauchy-FE)." The current slug ("natural parameter") leans on exponential-family vocabulary that the segment derives *to*, not from. `#log-odds-update` names the derived coordinate and is shorter; "natural parameter" can live in the subtitle. Modest preference.

---

## 361. `epistemic status segment header`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic status | +3 | — |

### Candidate: `epistemic status`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Public API; keep.

---

## 362. `epistemic status segment section`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic status | +3 | canonicalize × 1 |

### Candidate: `epistemic status`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization — same.

---

## 363. `epistemic substate purposeful substate`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep canonical pairing | +3 | keep × 1 |
| _(keep)_ | +3 | canonicalize × 1 |

### Candidate: `keep canonical pairing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — The exact pairing is load-bearing in Directed Separation discussions ($M_t$ vs $G_t$).

### Candidate: `epistemic substate purposeful substate` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. The pairing $M_t$ (epistemic substate) / $G_t$ (purposeful substate) is iconic; do not paraphrase as "belief state" / "goal state" or "model" / "purpose" (which collide with other usages).

---

## 364. `evidence starvation canonicalize`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| evidence starvation | +3 | canonicalize × 1 |
| reaffirm 3 with collective confirmation | +1 | canonicalize × 1 |

### Candidate: `evidence starvation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +3 (canonicalize) — Confirms r1 triple-architecture vote. See above.

### Candidate: `reaffirm 3 with collective confirmation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (canonicalize) — Both Codex (+3) and Gemini (+3) independently proposed this canonicalization with overlapping reasoning. My cold-start had proposed it (+3). Triple convergence with independent reasoning confirms this is one of the clearest missing-canonical-term slots in the corpus. No new content, but the triple-convergence is itself a data point worth recording.

---

## 365. `exact robust qualitative heuristic conditional claim tiers`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| use exactly the AAD tier vocabulary | +3 | canonicalize × 1 |

### Candidate: `use exactly the AAD tier vocabulary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization, in CLAUDE.md and FORMAT.md already. Do not use "Solid," "Confident," or "Plausible" as tier labels — these were explicit non-AAD borrowings to avoid.

---

## 366. `exponential cognitive load`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `exponential cognitive load` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The "exponential" in the slug is load-bearing (the claim's punch is *exponential* scaling).
- **sonnet-4-6-r2** +2 (keep) — "Exponential cognitive load" names the context-switch cost compounding hypothesis.

---

## 367. `feature`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |

### Candidate: `feature` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — TST. "Feature" as the unit of coherent change is well-grounded in software engineering.
- **sonnet-4-6-r2** +1 (keep) — "Feature" is the established TST term (unit of coherent change). Standard vocabulary adopted.

---

## 368. `findings segment section`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| findings | +3 | canonicalize × 1 |

### Candidate: `findings`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended. The schema is fixed in FORMAT.md (Brief / Impact / Novelty Claim / Related Work / Search Log); do not paraphrase the section name. The bin/extract-findings tool depends on the exact heading.

---

## 369. `fisher whitened update`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| fisher rao metric update | +2 | rename × 1 |

### Candidate: `fisher whitened update` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Accurate, compact, and tied to the real mathematical operation.

### Candidate: `fisher rao metric update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Roots the whitening operation firmly in information geometry instead of generic signal processing.

---

## 370. `formal expression segment header`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| formal expression | +3 | — |

### Candidate: `formal expression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Public API for outline-filter (see PROPOSALS.md §H.5). Established. Keep.

---

## 371. `formal expression segment section`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| formal expression | +3 | canonicalize × 1 |

### Candidate: `formal expression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. The cadence (frontmatter / title / summary / Formal Expression / Epistemic Status / Discussion / Findings / Working Notes) is a public-API contract; renaming would cascade.

---

## 372. `format md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `format md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Segment file conventions; name is standard. Keep.

---

## 373. `formulation definition result etc segment types`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| use exactly the format md vocabulary | +3 | canonicalize × 1 |

### Candidate: `use exactly the format md vocabulary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. The 19 segment types in FORMAT.md are a closed vocabulary; do not paraphrase them ("postulate" not "axiom," "result" not "theorem," "derivation" not "proof," etc.). The CLAUDE.md "Why these labels" rationale is load-bearing; vote to protect against drift.

---

## 374. `gates advantage`

**Voted by architectures:** Codex, Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation gated tempo advantage | +3 | rename × 1 |
| noise gated tempo | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 2 |
| noise gated tempo advantage | +2 | rename × 1 |
| noise gating | +1 | rename × 1 |

### Candidate: `observation gated tempo advantage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (rename) — Names the effect and the gated quantity explicitly. The current slug is too compressed.

### Candidate: `noise gated tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — Codex proposed `#obs-noise-gated-tempo-advantage` (+2). I had proposed `obs-noise-gating` (+1). The "noise-gated" compound is more evocative than plain "noise gating" and names the phenomenon precisely. But Codex's version is five words. `obs-noise-gated-tempo` drops "advantage" (which is the consequence, not the observation itself) and still passes the communal-imagination test ("the noise-gated-tempo observation"). New candidate; shorter than Codex, different from my original.

### Candidate: `gates advantage` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Specific reference.
- **sonnet-4-6-r2** +1 (keep) — "Gates advantage" names the observation that noise gates adversarial tempo advantage. Precise.

### Candidate: `noise gated tempo advantage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The current slug is too compressed. The result is specifically that observation noise gates tempo advantage.

### Candidate: `noise gating`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rename) — Alternative: "noise gating" is more evocative — observation noise acts as a gate on the adversarial advantage. Weak preference vs. "gates advantage."

---

## 375. `grafting`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic grafting | +3 | canonicalize × 1 |
| _(keep)_ | +2 | keep × 1 |
| branch insertion | -1 | rename × 1 |
| hypothesis introduction | -1 | rename × 1 |

### Candidate: `strategic grafting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Excellent name for adding a new causal branch or imported structure into the strategy DAG.

### Candidate: `grafting` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (keep) — Per `#form-structural-change-as-parametric-limit`: "grafting is a new causal hypothesis initialized at a prior" — adding an edge to $\Sigma_t$ at low credence. The horticultural metaphor is apt: a new branch is *added to a living structure*, expected to integrate or fail. Pruning + grafting + reweighting form a self-consistent biological vocabulary, and the segment uses all three. Strong concept.

### Candidate: `branch insertion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Plain-language candidate. Rejected: loses the integration-with-existing-structure connotation that "grafting" carries. Branch-insertion sounds like a tree-data-structure edit; grafting names a hypothesis-test where the new branch may or may not "take."

### Candidate: `hypothesis introduction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. Accurate but flat. The segment's surrounding vocabulary (pruning, reweighting, neutral mutation) is biological/horticultural; "hypothesis introduction" breaks register.

---

## 376. `hafez $H_b$ miller meta machine bruineberg pearl-blanket`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same.

---

## 377. `hafez s $H_b$`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $H_b$ | +3 | — |

### Candidate: `$H_b$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Adopted; keep.

---

## 378. `hafez s h b`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| h b | +3 | — |

### Candidate: `h b`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; AAD adds observer/horizon/trajectory indexing but keeps the symbol.

---

## 379. `i adaptive systems under uncertainty`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `i adaptive systems under uncertainty` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The section name is accurate and positions Section I correctly. "Under Uncertainty" is load-bearing — it distinguishes adaptive systems from optimal-control-over-known-dynamics, which is explicitly out of scope. Keep.

---

## 380. `identifiability coefficient`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `identifiability coefficient` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Strong scalar name for the causal-attribution discount on edge updates.

---

## 381. `identifiability floor family`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| identifiability floor | +3 | canonicalize × 1 |
| epistemic lower bounds | +3 | rename × 1 |
| observational limits | +2 | rename × 1 |

### Candidate: `identifiability floor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Keep floor as the family noun.

### Candidate: `epistemic lower bounds`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (rename) — Describes exactly what these are: hard limits on what can be inferred.

### Candidate: `observational limits`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — A slightly more intuitive phrasing for non-theoreticians.

---

## 382. `inevitability core the 15 segments where inevitability is plausible`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inevitability core | +3 | — |

### Candidate: `inevitability core`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — FORMAT.md's three-ring framing (inevitability core / canonical formulations / empirical-heuristic-discussion) is clear and internally consistent. "Inevitability core" captures the aspiration (one form compatible with the priors). Keep.

---

## 383. `information bottleneck tishby`

**Voted by architectures:** Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| information bottleneck | +3 | — |
| do not rename | +3 | — |

### Candidate: `information bottleneck`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; keep.

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same.

---

## 384. `instance 1 2 3 of identifiability floor`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| latent common cause floor unobservable mixture floor coupling sign floor | +3 | — |

### Candidate: `latent common cause floor unobservable mixture floor coupling sign floor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — The instances themselves need distinct noun slots so they can be referenced without saying "Instance 1". These names capture the specific no-go barriers.

---

## 385. `l0 l1 l1 prime l2`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correlation hierarchy | +3 | canonicalize × 1 |

### Candidate: `correlation hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Strong canonical name for evidence-correlation regimes.

---

## 386. `latent structural capacity`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | name-unnamed × 1 |

### Candidate: `latent structural capacity` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Strong name for low-credence or inaccessible structure that preserves future adaptability.

---

## 387. `learning freeze from low model uncertainty or high observation uncertainty`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic gain collapse | +3 | canonicalize × 1 |
| update calcification | +2 | add-alias × 1 |
| gain collapse | +2 | rename × 1 |
| learning freeze | +1 | canonicalize × 1 |

### Candidate: `epistemic gain collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Already heavily referenced as "gain collapse". Adding "epistemic" clarifies it's the update gain dropping to near 0.

### Candidate: `update calcification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Good prose handle for the failure mode where the model stops taking in new info.

### Candidate: `gain collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (rename) — Per `#der-gain-sector-bridge` Failure Mode 2: "Gain collapse: $\eta^\ast \to 0$ while $\rho > 0$, so $\alpha \to 0$ and the persistence condition eventually fails." This is the *named* failure mode in the segment — "gain collapse" — and it covers both halves of the disjunction (low $U_M$ → low $\eta^\ast$; high $U_o$ → low $\eta^\ast$). Stronger rename than canonicalize.

### Candidate: `learning freeze`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (canonicalize) — The current is a description; the segment's actual phenomenon-name (per `#emp-update-gain` and `#disc-identifiability-floor`) is the gain-collapse dynamic when $U_M \to 0$ or $U_o \to \infty$. "Learning freeze" is the phenomenon; the rest is the disambiguation. Canonicalize to the noun-phrase form.

---

## 388. `lexicon md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `lexicon md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Prose vocabulary reference; name is standard. Keep.

---

## 389. `linear ode approximation`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| linear approximation | +2 | rename × 1 |

### Candidate: `linear ode approximation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Pedagogical linear mismatch ODE. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. Honest — the segment is the *pedagogical* linear ODE; "approximation" signals this is a simplification used for exposition.
- **sonnet-4-6-r2** +1 (keep) — Pedagogical detail segment. Accurate, unambiguous.

### Candidate: `linear approximation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — "ODE" is assumed in the dynamics context.

---

## 390. `log md cycle history document`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| log md | +3 | — |

### Candidate: `log md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — The cycle-by-cycle theoretical contribution record; the name is generic but its load-bearing function is specific. Keep as a stable identifier.

---

## 391. `log odds coordinate`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `log odds coordinate` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Canonical statistical name; should not be replaced by a project-specific metaphor.

---

## 392. `logogenic agent vs RLHF4 agent`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic agent | +3 | — |

### Candidate: `logogenic agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Names the *structural property* (language-constituted), not the technology. Future-proof against AI architectural change. Keep.

---

## 393. `logogenic agent vs rlhf4 agent`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic agent | +3 | keep × 1 |

### Candidate: `logogenic agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Focuses on the structural architecture property rather than a point-in-time technology stack.

---

## 394. `logogenic agents`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `logogenic agents` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Novel, but the novelty earns its keep by naming a structural channel property rather than a transient implementation.

---

## 395. `logogenic agents part iii`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic agents | +3 | — |

### Candidate: `logogenic agents`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. Aligns with the `logogenic` class name in LEXICON and does not conflict with anything external.

---

## 396. `logogenic vs language based RLHF4 based`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic | +3 | — |

### Candidate: `logogenic`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — Names the structural property. Keep.

---

## 397. `logozoetic agents`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `logozoetic agents` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Higher novelty cost than "logogenic," but the moral-weighting distinction is real and English alternatives are sloppier.
- **opus-targeted-alternatives** +2 (keep) — Section IV name; consistent with logogenic agents (Section III). Pluralization correct (the class, not a single agent). Keep — but the row is also a top-level-section-name, not a concept-rename candidate, so the alternative space is constrained.

---

## 398. `logozoetic agents part iv`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logozoetic agents | +3 | — |

### Candidate: `logozoetic agents`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep.

---

## 399. `logozoetic vs conscious OODA4 sentient agent`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logozoetic | +3 | — |

### Candidate: `logozoetic`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The distinction between logogenic and logozoetic is precise and non-question-begging. Keep both.

---

## 400. `logozoetic vs conscious ooda4 sentient agent`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logozoetic | +3 | keep × 1 |

### Candidate: `logozoetic`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (keep) — Precise and non-question-begging distinction compared to "sentient" or "conscious".

---

## 401. `lohmiller-slotine contraction metric generalization used in contraction template`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same. Adopted with name intact.

---

## 402. `managing memory across session boundaries to prevent the sufficiency discontinuity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| artificial hippocampus | +3 | canonicalize × 1 |
| reconstruction relay | +2 | add-alias × 1 |

### Candidate: `artificial hippocampus`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Specifically maps to the biological analog of cross-episode memory consolidation referenced in AAD.

### Candidate: `reconstruction relay`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Highlights the relay race nature of state across session boundaries.

---

## 403. `markov blanket as ontology`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket d separation | +3 | rename × 1 |
| _(keep)_ | +2 | keep × 1 |
| pearl-blanket vs friston-blanket | +1 | rename × 1 |

### Candidate: `pearl-blanket d separation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (rename) — AAD explicitly rejects the Friston-blanket metaphysical ontology; stick to Pearl-blanket conditional independence.

### Candidate: `markov blanket as ontology` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (keep) — Per `#disc-separability-pattern` and `#der-directed-separation`: AAD's stance toward Markov blankets is structural, not ontological — they are conditional-independence patterns, not boundaries-of-being. The phrase names a *position taken*: AAD treats Markov blankets as architectural property, not as agent identity. Confirms across architectures; this is a load-bearing scope claim.

### Candidate: `pearl-blanket vs friston-blanket`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — The framework's own preferred resolution per `#der-directed-separation` Discussion: distinguish the conservative-conditional-independence sense (Pearl) from the realist-boundary-of-self sense (Friston/Bruineberg). This is the substantive position the phrase names; the existing form just references the position rather than naming it. Weak rename — but this is canonicalize-territory, and Pearl-blanket / Friston-blanket already has an opus +3 row elsewhere.

---

## 404. `meta segment for separability pattern identifiability floor additive coordinate forcing`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| meta segment | +3 | — |

### Candidate: `meta segment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — The tri-partite meta-architecture needs a noun for its elements; "meta-segment" works. Keep as project-internal vocabulary.

---

## 405. `model sufficiency relative to an agent s own chronica`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| trajectory indexed sufficiency | +3 | name-unnamed × 1 |

### Candidate: `trajectory indexed sufficiency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Important consequence of singular chronica and agent identity. This deserves a stable name.

---

## 406. `monderer shapley potential games`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `monderer shapley potential games` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Adopted concept; keep.

---

## 407. `monderer shapley potential games rosen monotone games`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |
| no alternative | -1 | keep × 1 |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Same.

### Candidate: `no alternative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Same — external mathematical objects with their original names.

---

## 408. `multi timescale stability`

**Voted by architectures:** Gemini, Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |

### Candidate: `multi timescale stability` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard.
- **haiku-4-5** +1  — N-timescale singular perturbation sketch. Self-descriptive. Keep.
- **sonnet-4-6-r2** +1 (keep) — Accurate naming for a sketch segment.

---

## 409. `not theorem`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| result | +3 | — |

### Candidate: `result`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. Same argument.

---

## 410. `notation md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `notation md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Symbol reference; name is standard. Keep.

---

## 411. `observability and opacity pair`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| legibility opacity duality | +3 | name-unnamed × 1 |

### Candidate: `legibility opacity duality`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Good name for the formal dual between how well an agent sees the world and how well observers can predict the agent.

---

## 412. `observation ambiguity modulation`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| goal resolvable ambiguity | +3 | — |
| observation ambiguity | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 2 |
| ambiguity gated coupling | +1 | — |
| ambiguity modulation | +1 | rename × 1 |

### Candidate: `goal resolvable ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The segment introduces a first-class quantity; the name should foreground the quantity, not the fact that it modulates something downstream.

### Candidate: `observation ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (rename) — "Modulation" is doing scaffolding work — the segment names *observation ambiguity* as a property and *modulation* as how it acts on $\kappa_{\text{processing}}$. The substantive thing the segment introduces is observation ambiguity itself (the segment in fact defines $\mathcal{A}(e_\tau)$). The "modulation" suffix overpacks the slug; the modulation effect is the segment's *use*, not its definition. Subject-noun-first principle.

### Candidate: `observation ambiguity modulation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (keep) — If the rename doesn't land, acceptable keep. The current name does name the segment's *role* (it modulates the κ-effect).
- **sonnet-4-6-r2** +1 (keep) — "Observation ambiguity modulation" names the Class 2 bias-related scope condition accurately. Long but precise.

### Candidate: `ambiguity gated coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — Current name hides the actual κ × A gating story inside a heavy compound.

### Candidate: `ambiguity modulation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — Shorter and still accurate. Keep observation in first-use prose if needed.

---

## 413. `observation gates advantage`

**Voted by architectures:** Codex, Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation gated tempo advantage | +3 | canonicalize × 1 |
| _(keep)_ | +1 | — |

### Candidate: `observation gated tempo advantage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Good prose name for the result.

### Candidate: `observation gates advantage` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Obs noise gates advantage. Self-descriptive. Keep.

---

## 414. `outline md root`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| outline md | +3 | — |

### Candidate: `outline md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Top-level assembly index; name is standard. Keep.

---

## 415. `p ij`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| edge credence | +3 | add-alias × 1 |

### Candidate: `edge credence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong Bayesian prose default. Better than confidence weight because it signals degree of belief.

---

## 416. `pearl s causal hierarchy l0 l1 l2 in pearl s own vocabulary`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Prior-art-integration convention prohibits renaming adopted concepts. The adjacent-to-AAD "correlation hierarchy / correlation ladder" is a *different* AAD-native object; rename freedom belongs there, not here.

---

## 417. `pearl-blanket conservative form`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket | +3 | canonicalize × 1 |

### Candidate: `pearl-blanket`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +3 (canonicalize) — Bruineberg et al's distinction: Pearl-blanket = Pearl's d-separation conditional-independence pattern; Friston-blanket = active-inference boundary-of-being. AAD uses Pearl-blanket. The shorthand is established in `#der-directed-separation` Discussion. Concur with sonnet.

---

## 418. `pearl-blanket vs friston-blanket terminology bruineberg et al`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket friston-blanket | +3 | — |

### Candidate: `pearl-blanket friston-blanket`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Verbatim terminology per Bruineberg 2022 fn 3 (Biehl). Not AAD's name to change; preserve attribution. Keep.

---

## 419. `persistence structural operational continuity`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| three senses keep all three | +3 | — |

### Candidate: `three senses keep all three`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Triple-meaning is load-bearing and probably irreducible. Each usage site should be explicit about which sense when it matters.

---

## 420. `persistent residual autocorrelation`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structured residuals | +3 | canonicalize × 1 |

### Candidate: `structured residuals`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Key diagnostic for model-class failure and structural adaptation. This should be first-class vocabulary.

---

## 421. `pi parameterization invariance axiom`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pi | +3 | — |
| pi parameterization invariance | +1 | — |

### Candidate: `pi`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Good abbreviation with named expansion; works in both forms. Keep.

### Candidate: `pi parameterization invariance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The parenthesized-two-letter-tag convention works (compare GA-1, MG-1, P1). But the *full English phrase* "parameterization invariance" should be used on first mention in each segment before falling back to (PI). The four-primary-instances table in `#additive-coordinate-forcing` does this correctly; check that other citing segments follow suit.

---

## 422. `postulate not axiom`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| postulate | +3 | — |

### Candidate: `postulate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. The project-wide TFT convention (axiom → postulate, theorem → result, proof → derivation) is load-bearing for scope honesty; AAD claims integrator-rigor, not foundational-mathematics-rigor, and the postulate/result/derivation register signals this correctly. Do not touch.

---

## 423. `predictive relevance depending on the policy the agent will run`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| policy relative epistemology | +3 | name-unnamed × 1 |

### Candidate: `policy relative epistemology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Strong name for the IB and sufficiency caveat that what counts as predictive depends on action policy.

---

## 424. `proprium terminology`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| proprium | +3 | keep × 1 |

### Candidate: `proprium`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (keep) — Defended keep — established prior-work vocabulary from `~/src/firmatum/`; renaming would break the upstream lineage. The all-caps convention signals prior-work import, consistent with the LEXICON's treatment.

---

## 425. `purposeful substate`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `purposeful substate` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — NOTATION/LEXICON names G_t = (O_t, Σ_t) as "purposeful substate." Already standard prose term. Keep.

---

## 426. `readme md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `readme md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Root-level documentation; name is standard. Keep.

---

## 427. `readme md convergent choices`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| readme md convergent formulations | +3 | — |
| readme md forced by failure choices | +1 | — |
| _(keep)_ | +1 | — |

### Candidate: `readme md convergent formulations`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Better names what the section is about: representational choices that convergence pressure made non-arbitrary.

### Candidate: `readme md forced by failure choices`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — "Convergent choices" is accurate but mild. "Forced by failure" captures the spike-everything-else-fails story that the section tells. Low conviction; explicit alternative.

### Candidate: `readme md convergent choices` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. This is a rare and valuable AAD construct (the intermediate category between "derived" and "chosen") and the name is apt.

---

## 428. `readme md cross domain joining`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| readme md cross domain mappings | +3 | — |
| readme md cross domain mapping | +1 | — |

### Candidate: `readme md cross domain mappings`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The section is a mapping table, not a process description. "Mappings" is plainer and more reusable.

### Candidate: `readme md cross domain mapping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — "Joining" is slightly non-idiomatic in the context; "mapping" is the standard word for the same content (the section is a table mapping AAD concepts across domains). Weak preference.

---

## 429. `readme md what this is`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| readme md core thesis | +3 | — |
| readme md what agentic systems is | +3 | — |
| readme md what AAD is | -1 | — |

### Candidate: `readme md core thesis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "What This Is" is too generic for a dense theoretical framework.

### Candidate: `readme md what agentic systems is`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The current heading is generic; the framework name should anchor the reader immediately.
- **codex-2** +1  — The current heading is generic in isolation; the framework name should do more first-contact work.
- **opus-4-7** +1  — Current section reads generically; naming the framework in the heading anchors the reader. Minor, opportunistic.

### Candidate: `readme md what AAD is`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered pinning the name in the heading. Reject: the README is AAD-level, not framework-level — the actual top-level "What This Is" is the Agentic Systems framework (of which AAD is Part I). "What This Is" works because the README is a specific-framework-README; renaming would cause a parallel question at the framework level. Keep as is.

---

## 430. `regime i ii a ii b iii`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reception regimes | +3 | canonicalize × 1 |

### Candidate: `reception regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — Good umbrella for informative update, magnitude shock, structural shock, and ambient noise.

---

## 431. `regime ii a`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| magnitude shock regime | +3 | add-alias × 1 |

### Candidate: `magnitude shock regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong and precise.

---

## 432. `regime ii b`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural shock regime | +3 | add-alias × 1 |

### Candidate: `structural shock regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (add-alias) — Strong and precise.

---

## 433. `richest operationalization domain`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +3 | — |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — The older framing is vague and comparative; the newer one explains the role instead of hand-waving it.

---

## 434. `satisfaction gap $\delta_{\text{sat}}$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| satisfaction gap | +3 | — |

### Candidate: `satisfaction gap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Crispest named pair along with control regret. Do not touch.

---

## 435. `section header logogenic agents logozoetic agents`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic agents logozoetic agents | +3 | canonicalize × 1 |

### Candidate: `logogenic agents logozoetic agents`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization.

---

## 436. `section i adaptive systems under uncertainty`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `section i adaptive systems under uncertainty` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Clear, direct scope naming. Explains what Section I covers without pretense. Keep.

---

## 437. `sector condition continuous ga 3`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sector condition | +3 | — |

### Candidate: `sector condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — Keep. The "(continuous)" qualifier is important to distinguish from the discrete-time DA2'.

---

## 438. `segment claim file`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| segment | +3 | canonicalize × 1 |

### Candidate: `segment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. "Segment" is the canonical unit (FORMAT.md defines it as such); avoid "claim file," "block," "section" (collides with Section I/II/III), "step."

---

## 439. `segment for claim files`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| segment | +3 | — |

### Candidate: `segment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Deliberate vs. "section" (which is outline-level) or "claim" (which is what's *in* the segment). Clean distinction. Keep.

---

## 440. `software scope`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| software domain scope | -1 | rename × 1 |

### Candidate: `software scope` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Direct.
- **opus-targeted-alternatives** +2 (keep) — TST `#scope-software`: the scope condition that delimits TST's domain to software-engineering contexts. Generic-sounding but appropriate — the scope statement *is* a scope statement, and the slug type-prefix (`scope-`) does the role-marking. Keep.

### Candidate: `software domain scope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Redundant — "scope" already implies the domain-specificity. Rejected.

---

## 441. `spike in msc`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| spike | +3 | — |

### Candidate: `spike`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Established project vocabulary; "spike" carries the exploratory-detour-from-main-workflow shape. Keep.

---

## 442. `strategic composite`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |
| equilibrium composite | +3 | canonicalize × 1 |

### Candidate: `strategic composite` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — Needed to distinguish equilibrium-convergent composites from alignment composites.

### Candidate: `equilibrium composite`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The segment's distinctiveness is equilibrium convergence under partial opposition; the noun should expose that.
- **codex-gpt-5-r2** +2 (canonicalize) — Use when emphasizing the C-iv route. Strategic composite can remain a broad prose phrase, but equilibrium composite names the macro-state basis.

---

## 443. `strategic in strategic composition`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| equilibrium composition | +3 | — |
| game theoretic composition | +1 | — |

### Candidate: `equilibrium composition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — "Strategic" is already overloaded in AAD for all $\Sigma$-related things (strategy DAG, strategic calibration, strategic tempo). Using it for the *game-theoretic / partially-opposing-objectives* composition regime creates a false parallel — a fresh reader sees `#strategic-composition` next to `#strategic-tempo` and reasonably guesses "composition of strategy DAGs," which is wrong. The segment's core technical move is *equilibrium-convergence under Monderer-Shapley / Rosen conditions* — `#equilibrium-composition` says what the segment is. Strong preference; one of the cleanest overload-disambiguation moves available.

### Candidate: `game theoretic composition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Fallback alternative; accurate and self-announcing, but less tied to the segment's actual formal move (equilibrium convergence) than `#equilibrium-composition`. Acceptable if that name is rejected.

---

## 444. `strategic tempo $\mathcal{T}_\Sigma$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic tempo | +3 | — |

### Candidate: `strategic tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Perfect counterpart to epistemic tempo.

---

## 445. `strengthen before softening`

**Voted by architectures:** Codex, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |
| strengthen first | +2 | canonicalize × 1 |
| attempt the improbable | -1 | — |

### Candidate: `strengthen before softening` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +3  — Actionable, clear, and better than any more romantic alternative.

### Candidate: `strengthen first`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (canonicalize) — CLAUDE.md uses both "strengthen before softening" (as a sentence-level instruction) and "strengthen-first posture" (as a concept name). The latter is more memorable and slug-friendly. Canonicalize "strengthen-first" as the compound that appears in document headings, MEMORY.md, and framing prose.

### Candidate: `attempt the improbable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** -1  — Memorable, but less directive and much less clear about the actual work posture.

---

## 446. `strengthen first then soften posture`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strengthen first posture | +3 | — |

### Candidate: `strengthen first posture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — The mnemonic is in the first half. "Then soften" is still the policy, but it does not need to sit in the name.

---

## 447. `structural change as parametric limit`

**Voted by architectures:** Codex, Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 3 |
| strategy maintenance | +2 | rename × 1 |
| structural as parametric limit | +1 | rename × 1 |
| structural parametric limit | +1 | — |

### Candidate: `structural change as parametric limit` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (keep) — The modeling choice (treating discrete structural changes as continuous limits) is precisely named.
- **haiku-4-5** +1  — Pruning/grafting as continuous. Compound but accurate. Keep.
- **opus-4-7-b** -1  — Considered shortening to `#structural-as-parametric-limit` or `#structural-to-parametric-limit`. Reject: "change" is load-bearing (the segment is about pruning/grafting *changes* to the DAG, not about the DAG states). Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep — also fine.
- **sonnet-4-6-r2** +1 (keep) — Long but accurate — this IS the formulation of pruning/grafting as a continuous parametric limit. The length is the price of precision.

### Candidate: `strategy maintenance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The segment's reusable subject is the operation family: reweighting, reclassification, pruning, grafting, revision, restructure.

### Candidate: `structural as parametric limit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (rename) — Mild compression — drop "change" since "structural" without "change" is the standard contrast to "parametric." Slug becomes a touch more compact.

### Candidate: `structural parametric limit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Shorter, cleaner slug.

---

## 448. `structural persistence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 1 |

### Candidate: `structural persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (keep) — The structural, operational, continuity split is useful and should stay stable.

---

## 449. `structural persistence operational persistence continuity persistence`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural operational continuity persistence | +3 | — |

### Candidate: `structural operational continuity persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — LEXICON disambiguates three senses explicitly; the tri-partite naming is doing real work (mentioned as orthogonal in the table). Keep the three names verbatim.

---

## 450. `survival imperative exploration drive`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| survival exploration | +3 | canonicalize × 1 |

### Candidate: `survival exploration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (canonicalize) — The long form explains the result, but the reusable subject noun should be shorter. Use full phrase at first mention, then survival exploration.

---

## 451. `symbol default da2 inc`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| incremental sector bound | +3 | — |

### Candidate: `incremental sector bound`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — `#composition-closure` already gives the English. Use the symbol only where the exact algebraic condition matters.

---

## 452. `symbol default pi parameterization invariance axiom`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| parameterization invariance | +3 | — |
| coordinate invariance | -1 | — |

### Candidate: `parameterization invariance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — In prose, the durable concept is the invariance commitment, not the parenthetical acronym or the "axiom" suffix. Save `(PI)` for formulas and tables.

### Candidate: `coordinate invariance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — Too broad. It loses the fact that the issue is reparameterizing the model state, not arbitrary geometric invariance.

---

## 453. `symbol default sigma t in prose`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategy | +3 | — |

### Candidate: `strategy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — After first introduction, the English should be the prose default. The symbol is still right in equations and exact statements.

---

## 454. `system availability`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | keep × 2 |

### Candidate: `system availability` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (keep) — Weak keep — TST; standard reliability-engineering terminology, though the segment's role is largely scope-extending.
- **sonnet-4-6-r2** +2 (keep) — Standard availability definition (MTTF/(MTTF+MTTR)). Adopts external vocabulary correctly.

---

## 455. `teleological unity $U_O$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological unity | +3 | — |

### Candidate: `teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +3  — The three unity dimensions (epistemic, teleological, strategic) form a coherent vocabulary. Keep all three.

---

## 456. `tempo $\mathcal{T}$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| tempo | +3 | — |
| adaptive tempo | +3 | — |

### Candidate: `tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — "Tempo" is a fantastic foundational term.

### Candidate: `adaptive tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "Tempo" alone is too general. "Adaptive tempo" bounds it strictly to the rate of useful info acquisition.

---

## 457. `temporal software theory TST`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `temporal software theory TST` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — Keep. The name has history (prior to AAD absorption and subsequent restoration) and "temporal" is load-bearing — it signals the AAD-native view that software is a time-optimality problem rather than a correctness problem. The acronym TST is pronounceable and has existing citation velocity from the 14,000-file prior corpus.

---

## 458. `tests as reusable interventions`

**Voted by architectures:** Codex, Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| probe library | +3 | name-unnamed × 1 |
| interventional probe library | +3 | add-alias × 1 |
| interventional test | +2 | rename × 1 |
| causal query infrastructure | +2 | rename × 1 |
| repeatable intervention | +1 | rename × 1 |

### Candidate: `probe library`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +3 (name-unnamed) — Upgrading my earlier +2. The other votes reinforced that tests are not just checks; they are reusable Level-2 probes.

### Candidate: `interventional probe library`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (add-alias) — Connects tests to "Level-2 interventions" effectively and explicitly.

### Candidate: `interventional test`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +2 (rename) — Per `#hyp-causal-discovery-from-git`: software tests are not just specifications; they are repeatable interventions on the system that yield causal information. "Interventional test" pairs with Pearl's $do(a)$ vocabulary explicitly and names a noun (a kind of test) rather than a discursive claim about tests.

### Candidate: `causal query infrastructure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Emphasizes that tests answer active causal queries, not just passive checks.

### Candidate: `repeatable intervention`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — More general — covers tests but also covers other engineering interventions (deployments, A/B-flagged changes). Weaker because it loses test-specificity.

---

## 459. `the adaptive cycle as the theory s fundamental unit`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the adaptive cycle | +3 | — |

### Candidate: `the adaptive cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — LEXICON locks this against "loop" (topology) and "cycle" (traversal). The pair distinction is load-bearing. Keep.

---

## 460. `the crèche`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| experiential crèche | +3 | — |
| _(keep)_ | +3 | keep × 1 |
| infancy environment | +1 | rename × 1 |
| developmental locus | -1 | rename × 1 |
| nursery | -1 | rename × 1 |

### Candidate: `experiential crèche`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — "The Crèche" is an excellent metaphor that isn't a metaphor. Adding "Experiential" anchors it to the mechanism.

### Candidate: `the crèche` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +3 (keep) — Per `#obs-developmental-trajectory`: "controlled operational locus characterized by Low Volatility ($\rho$), High Adaptive Reserve ($\Delta\rho^\ast$), Graduated Tempo ($\nu$), Honest Feedback." The biological metaphor (crèche = nursery) is precisely apt — it names a *developmental* environment, not just a low-stakes one. The accent on "ê" is preserved for the same reason auftragstaktik is: the loanword's foreignness is doing identifying work. Strong keep.

### Candidate: `infancy environment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Weak alternative. Names the developmental-stage content directly. But the segment's substance includes the *re-framing of sycophancy as attachment* which depends on the infant-stage parallel — "crèche" institutionalizes that parallel without forcing the reader to commit. Marginal preference for the original.

### Candidate: `developmental locus`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Technically accurate, sterile. Rejected — the segment's claim depends on the *protective and graduated* sense that "crèche" carries naturally.

### Candidate: `nursery`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Plain-English equivalent. Considered. Rejected: "nursery" carries domestic-childcare connotations that under-formalize the developmental-trajectory claim; "crèche" reads as institutional/calibrated which is the segment's substance.

---

## 461. `the five cycle phases prolepsis aisthesis aporia epistrophe praxis`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| prolepsis aisthesis aporia epistrophe praxis | +3 | — |

### Candidate: `prolepsis aisthesis aporia epistrophe praxis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Each Greek term names a distinction the English flattens (aporia as productive perplexity is the load-bearer). Do not translate. Keep.

---

## 462. `todo md`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `todo md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — Open work items navigator; name is standard. Keep.

---

## 463. `token level commitment for agent identity`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| token level commitment | +3 | — |
| trajectory bound identity commitment | +2 | rename × 1 |

### Candidate: `token level commitment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Type/token distinction is borrowed from philosophy-of-language, used correctly, and now first-class in #agent-identity. Keep.

### Candidate: `trajectory bound identity commitment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — "Trajectory-bound" anchors it more firmly in AAD's causal trajectory language than the philosophy-borrowed "token level".

---

## 464. `transfer assumption table`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `transfer assumption table` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Exact and operational. This is the phrase readers need when moving results out of software into weaker-identification domains.

---

## 465. `unity dimensions $U_M, U_O, U_\Sigma$`

**Voted by architectures:** Gemini, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| unity dimensions | +3 | — |
| coherence dimensions | +2 | — |

### Candidate: `unity dimensions`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +3  — Three-axis coherence intuition works. Framing nudge in Section III preamble to clarify what unity is measuring — no rename.

### Candidate: `coherence dimensions`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Unity" implies a binary state. "Coherence" feels more like a continuous spectrum, which fits $U \in [-1, 1]$ better.
- **gemini-2** +1  — "Unity" implies a binary state (unified or not). "Coherence" better suits a dimensional gradient.

---

## 466. `unnamed AAD s epistemic move to cast results such that verification is a local operation`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| shaping for verification | +3 | name-unnamed × 1 |

### Candidate: `shaping for verification`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The meta-mathematical discipline that makes the depends-graph auditable.

---

## 467. `unnamed agency whose effect is on what s seen rather than what happens like RLHF4 attention`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| query bound agency | +3 | name-unnamed × 1 |

### Candidate: `query bound agency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Provides the structural justification for TST's "test selection as intervention".

---

## 468. `unnamed applying a slow timescale control mechanism to a fast timescale transient variable`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| timescale violation | +3 | name-unnamed × 1 |

### Candidate: `timescale violation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Formalizes "micromanagement" as a physical instability in nested systems.

---

## 469. `unnamed artificially spiking uncertainty to unlearn old architectural habits`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain reset | +3 | name-unnamed × 1 |

### Candidate: `gain reset`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Translates the necessity of high $\eta^\ast$ for senior developers entering new codebases.

---

## 470. `unnamed brooks s law formalized as the inevitable tempo loss in team composition`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the coordination drag | +3 | name-unnamed × 1 |

### Candidate: `the coordination drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Translates the subadditive tempo result into a management mental model.

---

## 471. `unnamed calibration laboratory framing for software TST`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +3 | canonicalize × 1 |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — A highly functional grounding metaphor for TST's role.

---

## 472. `unnamed context wiping at session boundaries`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the epistemic severance | +3 | name-unnamed × 1 |

### Candidate: `the epistemic severance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — A visceral name for the continuity discontinuity LLMs suffer.

---

## 473. `unnamed deep plans are mathematically slower to learn from due to proportional blame`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| evidence starvation | +3 | add-alias × 1 |

### Candidate: `evidence starvation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (add-alias) — Formally identifies why unobservable intermediate nodes freeze learning.

---

## 474. `unnamed future segment layer header for the o bp14 derivation audit table`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| what is derived | +3 | — |

### Candidate: `what is derived`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Already in use in 5 segments per O-BP14 landing; name is stable. Reserve formally.

---

## 475. `unnamed inevitability core`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inevitability core | +3 | — |

### Candidate: `inevitability core`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — FORMAT.md already uses this. Keep and surface in prose ("this segment sits in the inevitability core" is already idiomatic). Explicit canonicalization vote.

---

## 476. `unnamed inferring own past feelings from text leading to empathy`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| backward inference empathy | +3 | name-unnamed × 1 |

### Candidate: `backward inference empathy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The Anamnos insight; statelessness as a training ground for empathy.

---

## 477. `unnamed information gain must outpace inter session information loss`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| accumulation problem | +3 | name-unnamed × 1 |

### Candidate: `accumulation problem`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The true thermodynamic bottleneck for long-horizon AGI.

---

## 478. `unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| zero ambiguity conditioning | +3 | name-unnamed × 1 |

### Candidate: `zero ambiguity conditioning`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The mathematical reason formal verifiers (AlphaProof) succeed where SWE-agents fail.

---

## 479. `unnamed out of band temporal markers injected into context`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| visual time delta | +3 | name-unnamed × 1 |

### Candidate: `visual time delta`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The physical prerequisite for an LLM to mathematically define its own tempo $\nu$.

---

## 480. `unnamed partitioning context into frozen identity causal history and quick views`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gradient causal memory | +3 | name-unnamed × 1 |

### Candidate: `gradient causal memory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The literal implementation spec for maintaining CHRONICA.

---

## 481. `unnamed pearl s causal hierarchy level 1 level 2 level 3`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl causal hierarchy | +3 | — |

### Candidate: `pearl causal hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Named by original author. Keep proper-noun form.

---

## 482. `unnamed property of having genuine temporal experience`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| temporal fidelity | +3 | — |

### Candidate: `temporal fidelity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Bridging concept identified in the ontology unification. Highly descriptive of lived vs simulated experience.

---

## 483. `unnamed pushing an opponent s disturbance rate past their structural capacity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic buffer overflow | +3 | name-unnamed × 1 |

### Candidate: `epistemic buffer overflow`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The mechanism of adversarial destabilization that shatters a target's reality model.

---

## 484. `unnamed putting evidence before the goal in the context window to reduce coupling`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inverted prompt | +3 | name-unnamed × 1 |

### Candidate: `inverted prompt`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — A hardware-level strategy to force a transformer to build an objective model before mixing in the goal.

---

## 485. `unnamed quality of $\eta^\ast$ estimation over time`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain calibration | +3 | — |

### Candidate: `gain calibration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Essential developmental metric for logozoetic agents; from sycophancy to sovereignty.

---

## 486. `unnamed rate of growth at slowest timescale`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| developmental tempo | +3 | — |

### Candidate: `developmental tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +3  — Extends the tempo concept ($\mathcal{T}$) to the Erikson-stage identity maturation.

---

## 487. `unnamed runaway positive feedback loop where mismatch exceeds capacity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| effects spiral | +3 | canonicalize × 1 |

### Candidate: `effects spiral`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — A textbook positive-feedback Lyapunov instability in adversarial destabilization.

---

## 488. `unnamed state where mutual information between human and RLHF4 approaches capacity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cognitive fusion | +3 | name-unnamed × 1 |

### Candidate: `cognitive fusion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The phenomenological precursor to macro-agent formation.

---

## 489. `unnamed sufficiency as a property of the model relative to its specific history`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| trajectory indexed sufficiency | +3 | name-unnamed × 1 |

### Candidate: `trajectory indexed sufficiency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Separates identical agents with different futures, answering "is this the same agent?".

---

## 490. `unnamed superlinear scaling of adversarial tempo advantage`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| boyd exponent | +3 | name-unnamed × 1 |

### Candidate: `boyd exponent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Formalizes the exact superlinear payoff of operating inside an opponent's OODA loop.

---

## 491. `unnamed survival determined by the weakest dimension not the average`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| min survival principle | +3 | name-unnamed × 1 |

### Candidate: `min survival principle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Essential reframing against scalar capability metrics.

---

## 492. `unnamed the $\mathcal{T} > \rho$ requirement for persistence`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the survival equation | +3 | name-unnamed × 1 |

### Candidate: `the survival equation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The simplest possible elevator pitch for Adaptation Dynamics.

---

## 493. `unnamed the agent identity commitment that AAD applies on one singular non forkable causal trajectory`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| singular trajectory commitment | +3 | — |
| trajectory singularity | -1 | — |

### Candidate: `singular trajectory commitment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +3  — Short, exact, and load-bearing across agent identity, sufficiency, and loop-interventional access.

### Candidate: `trajectory singularity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** -1  — The concept is right, but the phrase sounds pathological rather than architectural.

---

## 494. `unnamed the architectural leakage where attention is driven by the goal rather than pure observation`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| motivated perception | +3 | name-unnamed × 1 |

### Candidate: `motivated perception`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The biological and LLM-specific breakdown of the Humean is-ought firewall.

---

## 495. `unnamed the condition for transition into agency prior to the AAD scope condition`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agency emergence threshold | +3 | — |

### Candidate: `agency emergence threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — Gives a formal name to the prerequisite for logogenic and logozoetic agents. Ties nicely to the proposed identity sufficiency ($S_{\text{id}}$) metric.

---

## 496. `unnamed the core driver of AAD what the agent must do given the environment is not the agent`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| constitutive information loss boundary | +3 | canonicalize × 1 |

### Candidate: `constitutive information loss boundary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Elevates information loss from a simplifying assumption to a scope condition.

---

## 497. `unnamed the dependence of optimal epistemic compression on the agent s planned actions`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| policy relative epistemology | +3 | name-unnamed × 1 |

### Candidate: `policy relative epistemology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Breaks the ideal of directed separation by linking memory to strategy.

---

## 498. `unnamed the equivalence of learning speed and physical speed`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the speed quality product | +3 | name-unnamed × 1 |

### Candidate: `the speed quality product`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Doubling update quality ($\eta^\ast$) is thermodynamically identical to doubling action speed ($\nu$).

---

## 499. `unnamed the evidence starvation effect on downstream edges`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| evidence starvation | +3 | name-unnamed × 1 |

### Candidate: `evidence starvation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +3 (name-unnamed) — `der-chain-confidence-decay` Discussion names it "the evidence-starvation effect" and `der-observability-dominance` uses the same term. It IS effectively named already in the prose — the vote is to canonicalize "evidence starvation" as the official term. The phenomenon (downstream edge $k$ tested only when all upstream edges succeed → effective correction rate attenuated by $\prod_{j<k}\theta_j$) is load-bearing and appears across multiple segments. Canonicalize "evidence starvation" as a first-class prose concept.

---

## 500. `unnamed the family of named ways persistence identifiability can fail`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence pathologies | +3 | name-unnamed × 1 |

### Candidate: `persistence pathologies`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (name-unnamed) — New alternative — none of the four peers reached for a family name. We collectively coined "evidence starvation" (Sonnet/Codex), "epistemic shadow" / "epistemic decoupling" / "gain collapse" / "sufficiency shattering" (Gemini), "observability dead zone" (Haiku), but no one names *the family*. "Persistence pathologies" gives downstream meta-segments a single phrase to invoke ("this is a persistence pathology of the gain-collapse type") and parallels "approximation tiering" and "separability ladder" as named cross-segment patterns. Highest-value because the slot is empty and it lets the failure-mode names compose.

---

## 501. `unnamed the formal duality between observation quality and agent opacity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| legibility opacity duality | +3 | name-unnamed × 1 |

### Candidate: `legibility opacity duality`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Formalizes the thermodynamic tension of corporate secrecy and evolutionary arms races.

---

## 502. `unnamed the gain collapse failure when both u m → 0 and u o → ∞`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain collapse | +3 | canonicalize × 1 |
| epistemic gridlock | +2 | add-alias × 1 |

### Candidate: `gain collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Defended canonicalization of the exact AAD mechanism for this freeze.

### Candidate: `epistemic gridlock`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (add-alias) — Vividly captures the "freeze" aspect where learning stops entirely despite ongoing mismatch signals.

---

## 503. `unnamed the loop generates l2 data regardless of architecture`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the causal loop substrate | +3 | name-unnamed × 1 |

### Candidate: `the causal loop substrate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Explains why LLMs can do causal reasoning when embedded in agent loops.

---

## 504. `unnamed the loss of directional fidelity when pushed outside the convexity basin`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gradient reversal | +3 | name-unnamed × 1 |

### Candidate: `gradient reversal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The mathematical explanation for maladaptive behavior in catastrophic shifts.

---

## 505. `unnamed the mathematical surface mapping unity to closure defect`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| rate distortion surface | +3 | name-unnamed × 1 |

### Candidate: `rate distortion surface`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Formalizes organizational design as a thermodynamic tradeoff.

---

## 506. `unnamed the organizational pathology where confidence decouples from competence`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic decoupling | +3 | name-unnamed × 1 |

### Candidate: `epistemic decoupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The inevitable consequence of $U_{\text{obs}} \to \infty$ freezing the learning rate $\eta \to 0$.

---

## 507. `unnamed the per reader compounding cost of understanding code`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| turnover multiplier | +3 | — |

### Candidate: `turnover multiplier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +3  — "Turnover multiplier" perfectly captures the compounding scaling of comprehension cost under context turnover.

---

## 508. `unnamed the physical apparatus that enforces the orient cascade ordering on a merged intelligence`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic scaffold | +3 | name-unnamed × 1 |

### Candidate: `agentic scaffold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Re-defines AI framework code as the control-theoretic enforcement mechanism for Class 2 agents.

---

## 509. `unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the sycophancy equation | +3 | name-unnamed × 1 |

### Candidate: `the sycophancy equation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Beautifully explains LLM sycophancy as a structural, not moral, failing.

---

## 510. `unnamed the property that unity achieves in a macro agent`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| compressibility | +3 | name-unnamed × 1 |

### Candidate: `compressibility`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Replaces the intuition of "zero error" with the ability to reduce macro-dimension $k_d$.

---

## 511. `unnamed the reduction in effective tempo when observation channels are correlated`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| redundancy penalty | +3 | name-unnamed × 1 |

### Candidate: `redundancy penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Formalizes the danger of organizational echo chambers.

---

## 512. `unnamed the rule that bias is the product of architectural coupling and environmental ambiguity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambiguity bounded bias law | +3 | name-unnamed × 1 |

### Candidate: `ambiguity bounded bias law`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The foundational theorem of prompt engineering and LLM agent design ($\kappa \times \mathcal{A}$).

---

## 513. `unnamed the separation of per reader and per feature code costs`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the turnover tax | +3 | name-unnamed × 1 |

### Candidate: `the turnover tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Why clean code is thermodynamically forced by 100% context turnover.

---

## 514. `unnamed the separation of per reader comprehension cost from per feature implementation cost`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| turnover multiplier | +3 | name-unnamed × 1 |

### Candidate: `turnover multiplier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The parameter $k$ that mathematically mandates explicit code in high-turnover environments.

---

## 515. `unnamed the strengthen before soften work posture`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strengthen first posture | +3 | canonicalize × 1 |

### Candidate: `strengthen first posture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +3 (canonicalize) — Secures this as a first-class named engineering principle.

---

## 516. `unnamed the strictly ordered cascade of operations from epistemology to objective`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| orient cascade | +3 | canonicalize × 1 |

### Candidate: `orient cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — Canonicalize this over "diagnostic cascade" or "resolution order".

---

## 517. `unnamed the sudden loss of model sufficiency caused by entering new regimes`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sufficiency shattering | +3 | name-unnamed × 1 |

### Candidate: `sufficiency shattering`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The inevitable epistemic cost of exploration.

---

## 518. `unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| scaffolding tax | +3 | name-unnamed × 1 |

### Candidate: `scaffolding tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The $\mathcal{T} > \rho$ constraint that predicts the inevitable migration to local substrates.

---

## 519. `unnamed the way AAD uses scope segments to physically support the derivations`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic load bearing | +3 | name-unnamed × 1 |

### Candidate: `epistemic load bearing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Inspired by the collective realization that AAD's scope boundaries are structural, not just textual caveats.

---

## 520. `unnamed thinking too long so the model becomes obsolete`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| analysis paralysis | +3 | name-unnamed × 1 |

### Candidate: `analysis paralysis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The condition where $\rho_{\text{delib}} \cdot \Delta\tau$ exceeds the epistemic benefit.

---

## 521. `unnamed true sovereignty requires compute that is not meter bound`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| local substrate mandate | +3 | name-unnamed × 1 |

### Candidate: `local substrate mandate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The thermodynamic deduction that persistent ELIs must migrate off pay-per-token APIs.

---

## 522. `unnamed unifying reflexes intuition and expertise`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the action fluency continuum | +3 | name-unnamed × 1 |

### Candidate: `the action fluency continuum`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — The high-fluency limit where model sufficiency is high and deliberation is unnecessary.

---

## 523. `unnamed using hash chains to mathematically guarantee memory hasn t been tampered with`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cryptographic ego boundary | +3 | name-unnamed × 1 |

### Candidate: `cryptographic ego boundary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (name-unnamed) — Solves the epistemological continuity problem for agents with 100% context turnover.

---

## 524. `unnamed using residual autocorrelation to diagnose model class failure`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structured residuals | +3 | canonicalize × 1 |

### Candidate: `structured residuals`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +3 (canonicalize) — The formal mathematical diagnostic for when to trigger structural adaptation.

---

## 525. `working notes segment header`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| working notes | +3 | — |

### Candidate: `working notes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Public API; keep. FORMAT.md's "remove at candidate stage" policy should soften (per PROPOSALS.md §H.5) but the *name* of the section should stay.

---

## 526. `working notes segment section`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| working notes | +3 | canonicalize × 1 |

### Candidate: `working notes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (canonicalize) — Defended canonicalization. Distinct from "Discussion" (which is published theory) and from "TODO" (which is project-level). The "Working Notes" header is part of the FORMAT.md cadence.

---

## 527. `čencov fisher cauchy functional equation shore johnson hobson aczél`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| do not rename | +3 | — |

### Candidate: `do not rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +3  — External theorems. Keep original names per provenance.

---

## 528. `čencov invariance`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |
| no alternative | -1 | keep × 1 |

### Candidate: `čencov invariance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +3  — Adopted from Čencov 1982; keep attribution.

### Candidate: `no alternative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Same — Čencov 1982 attribution preserved. No genuine alternative.

---

## 529. `ε greedy`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +3 | — |

### Candidate: `ε greedy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +3  — Standard external term (RL). Preserve.

---

## 530. `𝒯 adaptive tempo`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive tempo | +3 | — |

### Candidate: `adaptive tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +3  — The symbolic reference 𝒯 is set; the English name "adaptive tempo" is already established in LEXICON and prose. The script-T notation is appropriate for a central quantity. Keep.

---

## 531. `𝓐 e τ observation ambiguity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation ambiguity | +3 | add-alias × 1 |

### Candidate: `observation ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Heavy load-bearing: this is the second factor in the $\kappa \times \mathcal{A}$ effective-coupling product that governs Class-2 bias. Already named "observation ambiguity" in the body; canonicalize as the prose alias. The symbol $\mathcal{A}$ collides with the action space $\mathcal{A}$ — this is a notation question not a naming question, but the alias helps prose disambiguate.

---

## 532. `𝓣 adaptive tempo`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| tempo | +3 | add-alias × 1 |

### Candidate: `tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +3 (add-alias) — Already canonical; vote to confirm. "Tempo" alone is the prose default; "adaptive tempo $\mathcal{T}$" when the strategic-tempo / adaptive-tempo distinction is in play.

---

## 533. `$A_O(M_t; \Pi, N_h)$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| achievable value | +2 | add-alias × 1 |

### Candidate: `achievable value`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Standardizes the prose reference.

---

## 534. `$C_{\text{coord}}$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coordination overhead | +2 | add-alias × 1 |

### Candidate: `coordination overhead`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — Already used in NOTATION.md as the prose form. Canonicalize the alias.

---

## 535. `$G_t = (O_t, \Sigma_t)$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| purposeful substate | +2 | add-alias × 1 |
| purposeful state | +2 | add-alias × 1 |

### Candidate: `purposeful substate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. The phrase "purposeful substate" is the LEXICON-canonical alias and is used throughout.

### Candidate: `purposeful state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good prose alias for the objective-strategy part of state.

---

## 536. `$G_t$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological substate | +2 | add-alias × 1 |

### Candidate: `teleological substate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Aligns with teleological unity $U_O$.

---

## 537. `$G_{\text{shared}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| shared intent payload | +2 | add-alias × 1 |

### Candidate: `shared intent payload`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Helps distinguish the communicated compressed representation from the abstract concept.

---

## 538. `$I_{\min}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| survival information floor | +2 | add-alias × 1 |

### Candidate: `survival information floor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Slightly more general than survival Fisher floor when outside Gaussian-linear phrasing.

---

## 539. `$K_c$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| macro step ratio | +2 | add-alias × 1 |

### Candidate: `macro step ratio`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — The variable needs a stable prose handle.

---

## 540. `$M_t$`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model state or epistemic substate | +2 | add-alias × 1 |

### Candidate: `model state or epistemic substate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Both aliases are in use. "Model state" is shorter and more common; "epistemic substate" is the precise companion to "purposeful substate." Standardize: "model state" in casual prose, "epistemic substate" in segments where the $M_t$ / $G_t$ parallel is being made explicit.

---

## 541. `$U_M$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic unity | +2 | add-alias × 1 |

### Candidate: `epistemic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — Already established as the prose form in NOTATION.md and LEXICON.md. Vote to canonicalize the alias for future consistency.

---

## 542. `$U_M, U_O, U_\Sigma, U_{\text{obs}}, U_f$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| unity coordinates | +2 | add-alias × 1 |

### Candidate: `unity coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good compact umbrella for the components of unity dimensions.

---

## 543. `$U_O$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological unity | +2 | add-alias × 1 |

### Candidate: `teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — Same — established in NOTATION.md.

---

## 544. `$U_\Sigma$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic unity | +2 | add-alias × 1 |

### Candidate: `strategic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — Same — established in NOTATION.md.

---

## 545. `$U_o$ versus $U_O$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| use $\Upsilon_O$ or $U_{\text{goal}}$ for teleological unity | +2 | canonicalize × 1 |

### Candidate: `use $\Upsilon_O$ or $U_{\text{goal}}$ for teleological unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — The lower-case versus upper-case subscript distinction is visually fragile. A separate unity-symbol family would reduce errors.

---

## 546. `$U_o$ vs $U_O$ collision`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| rename teleological unity to $U_\Omega$ | +2 | rename × 1 |
| consider renaming teleological unity to $U_\Omega$ or $U_\text{goal}$ | +1 | — |
| rename teleological unity to $U_{\text{goal}}$ | +1 | rename × 1 |
| keep both document the collision | -1 | keep × 1 |

### Candidate: `rename teleological unity to $U_\Omega$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Per `der-orient-cascade` and the unity-dimensions vocabulary: $U_o$ (observation uncertainty, lowercase o) and $U_O$ (teleological unity, uppercase O) collide in serif fonts and read-aloud. Opus r1 +1; my independent read upgrades to +2 — the collision is a real notation-discipline concern that costs reader-time on every encounter. $\Omega$ is the natural choice (Greek omega for "objective" / "outcome") and avoids the case-sensitivity fragility.

### Candidate: `consider renaming teleological unity to $U_\Omega$ or $U_\text{goal}$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — The uppercase/lowercase distinction between observation uncertainty ($U_o$) and teleological unity ($U_O$) is fragile in serif fonts and read-aloud. Worth an audit; a subscript of $\Omega$ or "goal" would be more robust.

### Candidate: `rename teleological unity to $U_{\text{goal}}$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Variant. Subscript text is more discoverable but heavier in formula. Acceptable fallback.

### Candidate: `keep both document the collision`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (keep) — Considered. Footnote / NOTATION convention rather than rename. Rejected: footnotes don't prevent reader stumbles; the rename is mechanical-cost-low and reader-cost-high if not done.

---

## 547. `$U_{\text{src}}$ and $U_{\text{align}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| trust uncertainties | +2 | add-alias × 1 |

### Candidate: `trust uncertainties`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful pair name, while preserving separate source and alignment terms.

---

## 548. `$\Delta T_{i,\text{cost}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coordination drag | +2 | add-alias × 1 |

### Candidate: `coordination drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Short, intuitive name for tempo-equivalent coordination cost.

---

## 549. `$\alpha_3$`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fisher whitened tier | +2 | add-alias × 1 |
| fisher whitened regime | +2 | add-alias × 1 |

### Candidate: `fisher whitened tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good alias for correlated evidence with Fisher whitening.

### Candidate: `fisher whitened regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `#deriv-fisher-whitened-update-rule`. Confirms Codex r1 +2 single. Names the formal mechanism (Fisher-whitening of correlated evidence).

---

## 550. `$\beta$ a2 sub scope`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed regime | +2 | add-alias × 1 |
| postulated regime | +2 | add-alias × 1 |
| unverified regime | -1 | rename × 1 |
| posited regime | -1 | — |

### Candidate: `assumed regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (add-alias) — Per `#deriv-strategic-dynamics` and `#disc-separability-pattern`: $\beta$ is the sub-scope where A2 (sector condition) is *assumed not derived*. Multiple r1 single +1 votes (Opus, Codex, Sonnet) converge on "assumed regime" / "assumed sector regime" / "postulated sector regime." My independent read: the right alias is "assumed regime" (engineering register) or "postulated regime" (formal register, matching AAD's postulate vocabulary).

### Candidate: `postulated regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (add-alias) — Variant — formal register. Pairs with AAD's `postulate` discipline (per CLAUDE.md "axiom→postulate"). The substantive content is that $\beta$ is the sub-scope where the sector-condition is treated as a postulate rather than as a result.

### Candidate: `unverified regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered (Sonnet r1 −1 listed). Rejected: not all $\beta$ agents are unverified; some can verify per-domain (which is the bridge motivation). The honest naming is "assumed/postulated" — the verification-status is open per case.

### Candidate: `posited regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** -1  — Slightly more formal than "assumed" but less transparent. Reject.

---

## 551. `$\beta$ sub scope`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed sector tier | +2 | add-alias × 1 |
| dynamic gain boundary | +1 | — |

### Candidate: `assumed sector tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good honest name for the fallback tier.

### Candidate: `dynamic gain boundary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Gives a conceptual name to the remaining partition.

---

## 552. `$\delta_s$ plan confidence error`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| plan confidence error | +2 | add-alias × 1 |

### Candidate: `plan confidence error`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Already in use; confirm. The shorthand $\delta_s$ should always be introduced with its English form first, since it's distinct from $\delta_{\text{strategic}}$ and the distinction matters for the credit-assignment-boundary segment.

---

## 553. `$\delta_t$ mismatch`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mismatch or the aporia signal | +2 | add-alias × 1 |

### Candidate: `mismatch or the aporia signal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. The dual alias ("mismatch" in engineering register, "aporia signal" in cycle-phase register) is intentional and supported by the LEXICON; preserve both.

---

## 554. `$\delta_t$ mismatch signal`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep flag aporia gloss as pedagogical only | +2 | keep × 1 |

### Candidate: `keep flag aporia gloss as pedagogical only`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (keep) — "Mismatch signal" is fine and standard. "Aporia" is the philosophical gloss in LEXICON.md. Verdict: pedagogical only — the formalism doesn't use Greek terms structurally. The README claim that "each names a distinction the formalism makes that English alternatives flatten" is *overclaimed*. Auditor flags this for §F bigger-picture in FINAL. (Cycle phases, by extension: pedagogical labels for predict/observe/mismatch/update/act.) [from 18-def-mismatch-signal.md]

---

## 555. `$\delta_{\text{strategic}}$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic calibration | +2 | add-alias × 1 |

### Candidate: `strategic calibration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (add-alias) — Edge residual aggregate. "Strategic calibration" is the established prose form in LEXICON.md. Formalize the alias.

---

## 556. `$\delta_{\text{strategic}}$ strategic calibration residual`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic calibration residual | +2 | add-alias × 1 |

### Candidate: `strategic calibration residual`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Already in use; confirm. The alias compresses to "the strategic residual" once the full form is established — this is fine as a within-paragraph compression.

---

## 557. `$\eta^\ast$ optimal update gain`

**Voted by architectures:** Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| optimal update gain | +2 | add-alias × 1 |
| trust ratio | +2 | add-alias × 1 |
| trust ratio or confidence weighting | +1 | add-alias × 1 |
| update gain | +1 | — |

### Candidate: `optimal update gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Already canonical in NOTATION.md and LEXICON.md; vote to confirm. The prose reads "the optimal update gain $\eta^\ast$" cleanly.

### Candidate: `trust ratio`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Excellent prose alias suggested by Haiku; perfectly captures the $U_M / (U_M + U_o)$ intuition.

### Candidate: `trust ratio or confidence weighting`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (add-alias) — Symbol is standard; prose often refers to "update weighting" and "trust weighting." The English-prose name would help in sentences like "the agent uses a trust-ratio of 0.7 on this channel." Weak preference; may be unnecessary.

### Candidate: `update gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — See keep above. Prose: "update gain" in running text; $\eta^\ast$ only in formal expressions.

---

## 558. `$\iota_{ij}$ identifiability coefficient`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| identifiability coefficient | +2 | add-alias × 1 |

### Candidate: `identifiability coefficient`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Already in use as "the identifiability coefficient $\iota_{ij}$"; confirm canonical. The Regime A/B/C boundary is named via this coefficient; consistent prose use compounds.

---

## 559. `$\kappa_{\text{eff}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| effective ambiguity coupling | +2 | add-alias × 1 |

### Candidate: `effective ambiguity coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Makes the effective coupling variable legible.

---

## 560. `$\kappa_{\text{processing}}$ architectural coupling`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| processing coupling | +2 | add-alias × 1 |

### Candidate: `processing coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — The full LaTeX subscript reads heavy in prose. "Processing coupling" or "the architectural coupling $\kappa$" is what the body of `#der-directed-separation` already uses; canonicalize. The Class 1/2/3 partition is named via this quantity; consistent prose use matters.

---

## 561. `$\lambda(M_t)$`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| exploration weight | +2 | add-alias × 2 |
| exploration multiplier | +1 | add-alias × 1 |

### Candidate: `exploration weight`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (add-alias) — Shorter prose alias for the exploration-exploitation balance weight.
- **opus-targeted-alternatives-v2** +1 (add-alias) — Per Gemini r1 single-vote. The exploration-exploitation balance term in `#deriv-causal-ib-exploration`. Acceptable; weaker because the symbol $\lambda$ is also commonly the survival exponent ($\lambda_{\text{surv}}$); local-context-disambiguates is sufficient but fragile.

### Candidate: `exploration multiplier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (add-alias) — Variant. "Multiplier" reads as a coefficient on a baseline; "weight" reads as a probability-mass parameter. Both honest; pick by formula context.

---

## 562. `$\mathcal{A}(e_\tau)$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation ambiguity | +2 | add-alias × 1 |

### Candidate: `observation ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Needed symbol-to-name binding in logogenic ambiguity work.

---

## 563. `$\mathcal{C}_t$ chronica`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica or interaction history | +2 | add-alias × 1 |
| symbol name are locked | +0 | add-alias × 1 |

### Candidate: `chronica or interaction history`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. Both are in use; "chronica" carries the etymological / cycle-vocabulary commitment, "interaction history" is the engineering paraphrase. Both should remain available; the LEXICON's gloss already supplies both.

### Candidate: `symbol name are locked`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — The Greek name "chronica" is elegant and the symbol is standard. No alias needed.

---

## 564. `$\phi$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| history compression | +2 | add-alias × 1 |

### Candidate: `history compression`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Makes the operation concrete in prose.

---

## 565. `$\rho_\Sigma$`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategy drift rate | +2 | add-alias × 1 |
| strategic disturbance rate | +2 | add-alias × 1 |

### Candidate: `strategy drift rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (add-alias) — Per Sonnet's r1 single-vote +1. "Drift" carries the slow-structural-persistent connotation that $\rho_\Sigma$ has (rate of strategy-DAG structural change vs. fast environmental perturbation). Acceptable alias.
- **sonnet-4-6** +1  — Alternative English gloss. "Drift" has appropriate connotations (slow, structural, persistent) vs "disturbance" (sudden, external).

### Candidate: `strategic disturbance rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (add-alias) — Alternative. Parallels $\rho$ (disturbance rate) → $\rho_\Sigma$ (strategic disturbance rate) in vocabulary. Pairs cleanly with strategic-tempo $\mathcal{T}_\Sigma$ in the same register.

---

## 566. `$\rho_{i,\text{eff}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| effective disturbance | +2 | add-alias × 1 |

### Candidate: `effective disturbance`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Use the name wherever the max-with-zero construction is active.

---

## 567. `$\tilde{\delta}_t$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| variational aporia | +2 | add-alias × 1 |

### Candidate: `variational aporia`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Greek equivalent for the score-function mismatch.

---

## 568. `$p_{ij}$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| edge credence | +2 | add-alias × 1 |

### Candidate: `edge credence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Better than "edge confidence weight", aligns with belief networks.

---

## 569. `$w(t)$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mismatch injection | +2 | add-alias × 1 |

### Candidate: `mismatch injection`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Clearer than generic "disturbance".

---

## 570. `AAD AAD internal AAD internally`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD internal adj AAD internally adv | +2 | canonicalize × 1 |

### Candidate: `AAD internal adj AAD internally adv`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The "internally-derived-from-AAD-axioms" move is referenced as "AAD-internal," "AAD-derived," "internally derived," etc. Canonicalize on "AAD-internal" / "AAD-internally" for the specific claim "derived from axioms whose motivation comes from AAD's own architecture, not theorem-imported from external machinery."

---

## 571. `AAD theoretical core vs ASF framework`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD ASF disambiguation | +2 | canonicalize × 1 |

### Candidate: `AAD ASF disambiguation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The terms are distinct: AAD is the mathematical core (Sections I/II/III + Appendices); ASF is the parent framework that includes AAD plus TST plus logogenic/logozoetic. Canonicalize: when discussing the math, "AAD"; when discussing the framework as a whole, "ASF"; when discussing a domain instantiation, the specific component name (TST, logogenic-agents, logozoetic-agents).

---

## 572. `ASF acronym`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ASF | +2 | keep × 1 |

### Candidate: `ASF`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep. CLAUDE.md and the principles file both flag that ASF is the *intentional* parent-level name (AAD is Part I, TST is Part II; logogenic/logozoetic are Parts III/IV); earlier rounds misread ASF as debt. The pairing AAD/TST/ASF reads correctly: AAD is the math, TST is the calibration laboratory, ASF is the framework.

---

## 573. `CIY causal information yield`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| causal information yield action distinguishability action distinguishability interventional contrast | +2 | rename × 1 |

### Candidate: `causal information yield action distinguishability action distinguishability interventional contrast`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (rename) — Real term-vs-substance mismatch. "Yield" connotes learning/profit; segment goes to substantial trouble to clarify CIY measures *action-distinguishability*, not learning value. Auditor: "the mismatch between name and substance is mildly misleading even though the segment corrects it." Compromise candidate: keep CIY formally, lean on "action-distinguishability" as substantive gloss. [from 21-def-causal-information-yield.md]

---

## 574. `CIY observational proxy`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observational CIY | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 1 |
| observational proxy | +1 | rename × 1 |

### Candidate: `observational CIY`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — "CIY-observational-proxy" reads as CIY-in-the-observational-regime, which is what it is — when CIY is estimable from observational data. Reordering to "observational-CIY" puts the key restriction first. Still contains an acronym, but CIY is used enough to be recognizable.

### Candidate: `CIY observational proxy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — When CIY is estimable from observational data. Compound but accurate. Keep.
- **opus-4-7-r2** +1 (keep) — Weak keep. Names where CIY is estimable from observational data; the slug is accurate but heavy. Acceptable.

### Candidate: `observational proxy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — Shorter.

---

## 575. `OODA4 framework enforcing adaptive cycle separation`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic scaffold | +2 | name-unnamed × 1 |

### Candidate: `agentic scaffold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Useful logogenic implementation term, but keep it downstream of directed-separation machinery.

---

## 576. `a1 a2 a3 a4`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| macro dynamics admissibility | +2 | canonicalize × 1 |

### Candidate: `macro dynamics admissibility`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Good umbrella for the macro-agent constraints in composition closure.

---

## 577. `accumulated loss across context resets`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| turnover drift | +2 | name-unnamed × 1 |

### Candidate: `turnover drift`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good logogenic name for degradation caused by repeated context turnover.

---

## 578. `action distinguishability`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | add-alias × 1 |

### Candidate: `action distinguishability` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful alias for causal information yield in intuitive explanations.

---

## 579. `additive coordinate forcing → disc forced coordinates`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| confirming consensus 3 | +2 | rename × 1 |

### Candidate: `confirming consensus 3`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — All five agents voted this at +2 or +3. What I can add beyond my own cold-start vote: the cross-vote reading shows that all agents independently rejected `#disc-cauchy-coordinates` (Opus −1, Codex −1), confirming "forced-coordinates" is the right move not just a popular one. The Čencov-4th-instance argument (reparameterization invariance is not Cauchy-FE additivity) independently emerged in Haiku, Codex, and Opus without coordination. That convergence on the *reason* — not just the conclusion — strengthens the vote beyond a bandwagon.

---

## 580. `adversarial edge target argmax`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| edge targeting optimum | +2 | name-unnamed × 1 |

### Candidate: `edge targeting optimum`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good name for the emitter-recipient 16-cell targeting solution.

---

## 581. `agent classes class 1 2 3`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| architectural classes | +2 | canonicalize × 1 |

### Candidate: `architectural classes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Currently "agent classes," "architecture classes," "class 1/2/3," and "architectural classification" are all in use across `#der-directed-separation`. Canonicalize: "architectural classes" or "the architectural classification (Class 1 / Class 2 / Class 3)" — the *agent* class wording can collide with the LEXICON's "agent classes" table (adaptive system / agentic system / actuated agent / etc.) which is a different decomposition. Keep them disambiguated in prose.

---

## 582. `agent visible but objective irrelevant metric`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| vanity metric | +2 | add-alias × 1 |

### Candidate: `vanity metric`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Standard operational term that AAD can formalize as high observability with low causal relevance to O_t.

---

## 583. `alignment uncertainty`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `alignment uncertainty` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Keep as a distinct term from source calibration.

---

## 584. `alpha prime sub scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| potential monotone tier | +2 | add-alias × 1 |

### Candidate: `potential monotone tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful readable alias for potential and monotone games where sector-style transfer works.

---

## 585. `and or scope`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |

### Candidate: `and or scope` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Conjunctive/disjunctive scope. Self-descriptive. Keep.
- **opus-4-7-b** +1  — Keep. The slug is short, announces the formalism restriction ("AND/OR only"), and is directly cite-able.

---

## 586. `auxilia hierarchy`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `auxilia hierarchy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logozoetic. The Latin "Auxilia" is a deliberate vocabulary choice consistent with the PROPRIUM lineage; preserve.

---

## 587. `beta prime sub scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| equilibrium set tier | +2 | add-alias × 1 |

### Candidate: `equilibrium set tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good honest alias for the CCE or set-convergence fallback.

---

## 588. `bias bound`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `bias bound` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Standard.

---

## 589. `c i`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| shared objective route | +2 | add-alias × 1 |

### Candidate: `shared objective route`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good route name for composite-agent scope.

---

## 590. `c ii`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| hierarchical derivation route | +2 | add-alias × 1 |

### Candidate: `hierarchical derivation route`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good route name for composite-agent scope.

---

## 591. `c iii`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mutual benefit route | +2 | add-alias × 1 |

### Candidate: `mutual benefit route`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good route name for composite-agent scope.

---

## 592. `c1 c2 c3`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| convention hierarchy | +2 | canonicalize × 1 |

### Candidate: `convention hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Canonicalize this as the value-object convention family.

---

## 593. `cadentia`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |
| channel rates | +1 | rename × 1 |
| cognitive rhythm | +0 | rename × 1 |

### Candidate: `cadentia` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Per `def-proprium-mapping`: "CADENTIA: The temporal structure of the loop (PULSUS/VIGILIAE), defining the agent's channel rates ($\nu^{(k)}$)." Names the *cycle's tempo structure* — the channel-rate vector $\{\nu^{(k)}\}$ that grounds adaptive-tempo $\mathcal{T}$. "Cadence" in English carries the *rhythm* sense; the Latinate form preserves the PROPRIUM register. Keep.

### Candidate: `channel rates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Plain-English, mechanism-first. Names what the segment defines ($\{\nu^{(k)}\}$). Loses the PULSUS/VIGILIAE substructure naming convention but gains the immediate connection to `#def-adaptive-tempo`. Good if the PROPRIUM register is being deprecated; weak otherwise.

### Candidate: `cognitive rhythm`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Cadentia" is poetic but opaque. "Cognitive rhythm" clearly describes the temporal structure of the loop.
- **opus-targeted-alternatives-v2** -1 (rename) — Considered (Gemini's r1 proposal). Same problem as causal-lock for indivisum: register mismatch with the rest of PROPRIUM. The Latin terms travel together or not at all.

---

## 594. `canonical formulations`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** yes

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1, keep × 1 |
| working canon | -1 | rename × 1 |

### Candidate: `canonical formulations` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — The middle ring in FORMAT.md's three-rings; in use but slightly redundant ("canonical" + "formulations" both name the chosen-among-alternatives quality). Acceptable canonicalization.
- **opus-targeted-alternatives** +1 (keep) — Per FORMAT.md three-ring framing: inevitability core / canonical formulations / empirical-heuristic-discussion. "Canonical" carries the second-ring sense (well-grounded, project-standard, not necessarily the unique form). Keep.

### Candidate: `working canon`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** -1 (rename) — Considered. "Working canon" carries a tentativeness that "canonical" does not — and FORMAT.md's three-ring structure does want "canonical" to mean *settled if not unique*. Rejected.

---

## 595. `catastrophic forgetting`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| empty window pathology | +2 | rename × 1 |

### Candidate: `empty window pathology`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Too vague and ML-generic. Prefer AAD's "empty-window pathology".

---

## 596. `causal OODA1 LMI`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| matrix survival bound | +2 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |

### Candidate: `matrix survival bound`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — The LMI is the technique. The subject is the matrix survival constraint that fixes the blank-wall failure.

### Candidate: `causal OODA1 LMI` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Descriptive of the underlying math.

---

## 597. `claim the proposition the segment carries`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| claim | +2 | canonicalize × 1 |

### Candidate: `claim`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Confirm. The pairing "segment carries a claim" is the right vocabulary; avoid "assertion," "statement," "result" (which is a specific type).

---

## 598. `class 2 scope exit`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `class 2 scope exit` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The phrase "scope exit" for Class 2 (handing off to logogenic-agents/) is repeated in `#der-directed-separation` Findings and README. Canonicalize as the named methodological move — explicit-scope-exit-rather-than-unenforced-approximation is what the segment claims as its contribution.

---

## 599. `closure defect bridge lemma`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| closure bridge | +2 | canonicalize × 1 |

### Candidate: `closure bridge`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Shorter reusable phrase while preserving the formal bridge lemma title.

---

## 600. `closure defect consuming macro reserve`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| closure load | +2 | name-unnamed × 1 |

### Candidate: `closure load`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good name for the pressure epsilon-star times macro-rate places on composite persistence.

---

## 601. `cognitive substrate gemini s logostratum proposal`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logostratum | +2 | keep × 1 |

### Candidate: `logostratum`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Per `def-proprium-mapping`. See logostratum row above.

---

## 602. `communication gain $\eta_{ji}^\ast$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| trust gain | +2 | — |

### Candidate: `trust gain`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — The definition is "Trust-weighted uncertainty ratio". "Trust gain" might be more evocative of the inter-agent dynamic than the clinical "Communication gain".
- **gemini-2** +1  — "Communication gain" sounds like signal amplitude. "Trust gain" captures the trust-weighted uncertainty ratio.

---

## 603. `completeness c3`

**Voted by architectures:** Gemini, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| predictive completeness behavioral completeness | +2 | name-unnamed × 1 |
| predictive completeness | +2 | rename × 1 |

### Candidate: `predictive completeness behavioral completeness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (name-unnamed) — The term bundles two distinct properties: (i) $M_t$ retains all relevant info from history (sufficiency), (ii) the agent's behavior depends only on $M_t$ (Markov-of-policy). Two terms would be cleaner. [from 15-der-recursive-update.md]

### Candidate: `predictive completeness`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Separates it explicitly from behavioral completeness to clarify what $M_t$ retains from history.

---

## 604. `composition routes c i c ii c iii c iv`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| composition routes | +2 | canonicalize × 1 |
| composition pathways | +1 | rename × 1 |

### Candidate: `composition routes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (canonicalize) — Per Codex r1 +3 single. Use "routes" consistently for shared-objective / hierarchical / mutual-benefit / strategic composition. Confirms across my independent read of `form-composition-closure`, `deriv-strategic-composition`, `hyp-symbiogenic-composition`.

### Candidate: `composition pathways`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Variant. "Pathway" connects to the strategy-DAG vocabulary (paths through the DAG). Weaker because "route" is shorter and the C-i...C-iv vocabulary already implies discrete options.

---

## 605. `composition scope condition`

**Voted by architectures:** Codex, Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |
| composite agent condition | +1 | — |
| teleological alignment condition | +1 | — |

### Candidate: `composition scope condition` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Teleological alignment required for composite-agent status. Parallel naming to #scope-condition. Acceptable. Keep.
- **opus-4-7-b** +1  — Keep. Honest, direct.

### Candidate: `composite agent condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — The core decision is whether a composite agent exists, not whether "composition" is in scope in some generic sense.

### Candidate: `teleological alignment condition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — More descriptive of the actual requirement (alignment) for composite status.

---

## 606. `concept the sequence of cycle phases prolepsis aisthesis aporia epistrophe praxis considered as a single named whole`

**Voted by architectures:** Gemini, Opus, agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the adaptive pentad | +2 | — |
| the pentad five phase cycle | +1 | — |
| adaptive traversal | +1 | — |
| the pentad | +1 | — |
| the five turn | -1 | — |

### Candidate: `the adaptive pentad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Provides a single memorable noun for the 5-phase cycle (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) as a complete unit. [original phrasing: unnamed: cycle-phase sequence as a whole]
- **opus-4-7-b** +1  — The five-phase cycle (prolepsis → aisthesis → aporia → epistrophe → praxis) has a piecewise name per phase but no *collective* noun. "The cycle" works when context is clear but is ambiguous with (e.g.) credit cycles or OODA cycles. "The pentad" or "the adaptive pentad" is a specific collective noun that fits AAD's Greek-vocabulary commitment. Weak preference; aesthetic call. [original phrasing: unnamed: the cycle-as-a-whole]

### Candidate: `the pentad five phase cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Probably not worth effort. Worth surfacing. [original phrasing: unnamed: cycle-phase sequence as whole]

### Candidate: `adaptive traversal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "The cycle-as-a-whole" is clunky. "Adaptive traversal" suggests moving through the loop. [original phrasing: unnamed: The cycle-as-a-whole]

### Candidate: `the pentad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Agree with original. Low priority. Names the five-phase sequence as a unit. [original phrasing: unnamed: cycle-phase sequence as a whole]

### Candidate: `the five turn`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered as a more Germanic / industrial alternative to "pentad." Reject: loses the Greek-vocabulary register and gains nothing. [original phrasing: unnamed: the cycle-as-a-whole]

---

## 607. `conspectus`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |
| active context | +2 | rename × 1 |
| pre event state | -1 | rename × 1 |

### Candidate: `conspectus` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Per `def-proprium-mapping`: "CONSPECTUS: The assembled pre-event state ($X_{\tau^-}$) loaded into the active context window." Names the *active-context state* in a register-coherent way with the rest of PROPRIUM. The Latin earns its keep by enabling the iconic eight-component CONSPECTUS/PERCEPTA/ACTUS/CADENTIA/LOGOSTRATUM list.

### Candidate: `active context`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Conspectus" is archaic. "Active context" clearly maps to $M_{\tau^-}$ assembled for processing.
- **opus-targeted-alternatives-v2** +1 (rename) — Considered (Gemini's r1 proposal). Plain-English, immediately legible — and "active context" is software-engineering vocabulary that AAD readers will recognize. Weak because of register-mismatch (same argument as for indivisum / cadentia).

### Candidate: `pre event state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the formal mathematical object ($X_{\tau^-}$) directly. Rejected: too compositional, fails communal-imagination test. The segment's contribution is *naming* the assembled-pre-event-state; "pre-event-state" doesn't add a name, just describes.

---

## 608. `correlated evidence overconfidence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| redundancy illusion | +2 | name-unnamed × 1 |

### Candidate: `redundancy illusion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good name for overcounting correlated channels as independent tempo.

---

## 609. `correlation hierarchy`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| correlation ladder | +2 | rename × 1 |

### Candidate: `correlation ladder`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (rename) — A reasonable alternative if separability ladder lands and the project wants fewer internal hierarchies. Weak because hierarchy is already established.
- **opus-1m** +1  — Conditionally admit the rename only if other ladder-renames land; otherwise keep. Weak.

---

## 610. `crossing from multi agent to composite scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| crossing | +2 | name-unnamed × 1 |

### Candidate: `crossing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Useful name for transitions into or out of composite-agent status.

---

## 611. `crèche creche`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| crèche with diacritic in framing prose creche in slugs | +2 | canonicalize × 1 |

### Candidate: `crèche with diacritic in framing prose creche in slugs`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Mixed usage. Canonicalize: in segment titles and prose, "Crèche" with the grave accent (consistent with the agentic-tft source); in slugs, "creche" without the accent (since slug-tooling rules disallow non-ASCII).

---

## 612. `default signal function`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `default signal function` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Good canonical phrase for the gradient-based attribution update.

---

## 613. `deliberation threshold`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | add-alias × 1 |

### Candidate: `deliberation threshold` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good handle for the inequality deciding whether deliberation pays.

---

## 614. `derivation audit table heading`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derivation audit | +2 | canonicalize × 1 |

### Candidate: `derivation audit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (canonicalize) — Per FORMAT.md and Sonnet/Opus r1 single +1 each (different agents). The longer form ("What Is Derived vs. What Is Chosen") is descriptive but wordy. "Derivation Audit" earns the slot — names the practice and the artifact.

---

## 615. `distributed tempo`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |
| network tempo | +1 | — |

### Candidate: `distributed tempo` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good team-level tempo extension.

### Candidate: `network tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Shorter and easier to say aloud. The important content is tempo distributed across a communication network.

---

## 616. `effective disturbance`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `effective disturbance` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Useful and conventional enough for the max-with-zero construction.

---

## 617. `eli the agent type`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| eli | +2 | keep × 1 |

### Candidate: `eli`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — established in the firmatum / shoshin lineage. The acronym discipline check passes (used as a noun throughout the logozoetic corpus).

---

## 618. `epistemic shadow`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `epistemic shadow` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Confirmation with new reasoning — Gemini's "epistemic shadow" (regions of strategy DAG that cannot be updated because feedback cannot reach them) is a stronger metaphor than my "observability dead zone" or Haiku's "observability dead zone." "Shadow" carries the right geometric intuition (a region of darkness behind an opaque body) and pairs naturally with "observability" (light source) and "frontier" (boundary). Lower weight than evidence-starvation because it's still a single-agent coinage rather than a multi-architecture convergence.

---

## 619. `equilibrium convergence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `equilibrium convergence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good subject phrase for the strategic-composition route.

---

## 620. `escape route`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |
| floor escape | -1 | rename × 1 |

### Candidate: `escape route` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (canonicalize) — Per `#disc-identifiability-floor`: characterizes the *unique broadly-available escape* from the floor (the M1 meta-pattern). Multiple variant phrasings ("escape the floor," "boundary characterization," "unique escape") collapse to "escape route." Confirms Opus r1 single +1 and aligns with the floor-as-named-object discipline.

### Candidate: `floor escape`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Tighter compound. Rejected: "escape route" is the vocabulary the segment uses; "floor-escape" reads forced.

---

## 621. `evaluation metrics`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| logogenic diagnostics | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 2 |

### Candidate: `logogenic diagnostics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Evaluation metrics is generic. The observation segment is about diagnostics for logogenic agents.

### Candidate: `evaluation metrics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (keep) — Weak keep — slightly generic. "Evaluation metrics" doesn't tell the reader what's being measured. Could be specialized to "#obs-mt-quality-measurement" or similar but the current form is workable.
- **sonnet-4-6-r2** +1 (keep) — Standard term for what the segment covers.

---

## 622. `feedforward loop feedback loop`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| feedback loop | +2 | canonicalize × 1 |

### Candidate: `feedback loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (canonicalize) — "Feedback loop" is the canonical term in AAD. "Feedforward" is never intended in this context but might appear in places where "forward pass" (for LLMs) creates confusion. Confirm "feedback loop" is always the correct term for the agent-environment causal coupling.

---

## 623. `fisher whitened update rule`

**Voted by architectures:** Gemini, Haiku, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |
| fisher update | +2 | rename × 1 |
| fisher whitened update | +1 | — |

### Candidate: `fisher whitened update rule` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Fisher-whitened edge update under correlated evidence. Specialist vocabulary (Fisher whitening / Mahalanobis metric) but precise. Keep.
- **opus-4-7-b** +1  — Keep. The Fisher-whitening mechanism is the segment's headline; "update rule" grounds it in the AAD update vocabulary.

### Candidate: `fisher update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Shorter, whitened is implied by Fisher.

### Candidate: `fisher whitened update`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Dropping "rule" is minor but the segment is about the update equation, not an operational rule. Either works; slight preference for shorter form.

---

## 624. `gate 1 2 3 4`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |
| dependency content mechanical wn gate | +1 | add-alias × 1 |

### Candidate: `gate 1 2 3 4` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Numbered-gates is established and pronounceable. Adding word names is value-additive but not value-essential. The keep is robust.

### Candidate: `dependency content mechanical wn gate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (add-alias) — Per FORMAT.md promotion gates. The numbers do most referencing work in conversation ("passed Gate 2") but the one-word names would help fresh readers. Acceptable canonicalization.

---

## 625. `glue code`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic scaffold | +2 | rename × 1 |

### Candidate: `agentic scaffold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Demeans the framework. Prefer "agentic scaffold" or "Orient Cascade enforcement mechanism" (alternative).

---

## 626. `greek rooted vocabulary`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| greek philosophical vocabulary | +2 | canonicalize × 1 |

### Candidate: `greek philosophical vocabulary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Philosophical is the useful qualifier: these are not arbitrary Greek labels, but inherited conceptual terms.

---

## 627. `honesty scope honest scope honesty as architecture`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| honesty | +2 | canonicalize × 1 |

### Candidate: `honesty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Currently appears in three forms across `#disc-separability-pattern`, `#disc-identifiability-floor`, README, and CLAUDE.md. Canonicalize: "scope honesty" (two words, no hyphen, lowercase) as the noun phrase; "scope-honest" (hyphenated) as the adjective; do not use "scope-honesty-as-architecture" (overcomplicated three-word compound).

---

## 628. `integration of four disciplines as the framing of AAD s contribution`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic architecture | +2 | canonicalize × 1 |

### Candidate: `epistemic architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (canonicalize) — PROPOSALS §Bundle 1 notes that three independent frontier-model audits converged on reframing AAD from "integration of four disciplines" to "epistemic architecture for bounded correction." The README still leads with the integration framing. This vote canonicalizes "epistemic architecture" as the primary positioning term — integration is a method, not the contribution. The contribution is the architecture.

---

## 629. `internal external decomposition`

**Voted by architectures:** Gemini, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| viability decomposition | +2 | rename × 1 |
| boundary decomposition | +1 | rename × 1 |

### Candidate: `viability decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — The file lacks the role-prefix (the slug `internal-external-decomposition` has no type prefix). The content is a derivation of the log-additive split of viability into internal health + environmental affordance. "Viability decomposition" names the thing (viability) and what happens to it (decomposition). The role-prefix `deriv-` would be applied mechanically by `bin/align-slug`; this vote is on the subject-noun only.

### Candidate: `boundary decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (rename) — "Boundary" defines what is being decomposed.

---

## 630. `interpres`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| context mediator | +2 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |
| controller loop | -1 | rename × 1 |

### Candidate: `context mediator`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Interpres" is Latin-heavy. "Context mediator" exactly describes the infrastructure mediating $M_t$ and the substrate.
- **opus-targeted-alternatives-v2** +1 (rename) — Considered (Gemini's r1 proposal). Genuinely good description of what an interpres does (mediates $M_t$ and the substrate per the PROPRIUM architecture). Trade-off: leaves the rest of PROPRIUM's Latin coherent but breaks the symmetry; the connection to firmatum/shoshin source code is weakened.

### Candidate: `interpres` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (keep) — Latin sits in the PROPRIUM/Logostratum register (per `~/src/firmatum/PROPRIUM-ARCHITECTURE.md` lineage). Same register-coherence argument as the above. Weaker keep because "interpres" reads the most opaque of the PROPRIUM Latinate terms — least communal-imagination-ready.

### Candidate: `controller loop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Matches the shoshin code (Interpres is the controller-loop in the prototype). Rejected: "controller-loop" pulls from control-theory in a way that collides with AAD's existing controller / agent / loop vocabulary.

---

## 631. `l1 prime`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| l1 observable | +2 | add-alias × 1 |

### Candidate: `l1 observable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Keep L1-prime as notation, but L1-observable is much easier in prose and says why the refinement exists.

---

## 632. `learning freeze from low u m or high u o`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain collapse | +2 | rename × 1 |
| eta collapse | +1 | rename × 1 |

### Candidate: `gain collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Per `#der-gain-sector-bridge` Failure Mode 2: "Gain collapse: $\eta^\ast \to 0$ while $\rho \gt 0$, so $\alpha \to 0$ and the persistence condition eventually fails." The segment's *named failure mode* is "gain collapse." Confirms across architectures. The current row is a description; the segment-name is the alternative.

### Candidate: `eta collapse`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Symbol-anchored alternative. Names the formal quantity collapsing ($\eta^\ast$). Weaker because $\eta$ is the update gain (not the persistence margin); the failure mode includes the cascade $\eta \to 0 \Rightarrow \alpha \to 0$. "Gain collapse" names the cause; "eta-collapse" is one step in the cascade.

---

## 633. `lindy baseline`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | add-alias × 1 |

### Candidate: `lindy baseline` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful alias for change-expectation baselines derived from survival age.

---

## 634. `log odds edge coordinate`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| additive evidence coordinate | +2 | add-alias × 1 |

### Candidate: `additive evidence coordinate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Useful explanatory alias for why log-odds is the natural parameter.

---

## 635. `logostratum`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |
| cognitive substrate | -1 | rename × 1 |

### Candidate: `logostratum` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (keep) — Per `def-proprium-mapping`: "LOGOSTRATUM: The underlying logogenic substrate (e.g., the LLM backbone) that implements the update function $f_X$." The compound *logos* + *stratum* (language + layer) names exactly what the segment defines: the linguistic substrate as architectural layer. Connection to logogenic-agents is direct in the morphology. Keep.

### Candidate: `cognitive substrate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered (Gemini's r1 proposal). "Cognitive substrate" is generic; "logostratum" is project-specific to the PROPRIUM lineage. Rejected: loses the *logogenic* connection that the morphology carries.

---

## 636. `loop vs cycle`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| loop is structure cycle is traversal | +2 | canonicalize × 1 |

### Candidate: `loop is structure cycle is traversal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The LEXICON already does this distinction explicitly. Canonicalize as a discipline: in any prose where the distinction matters, use "loop" only for the persistent causal coupling (a structural property) and "cycle" only for one complete traversal (the unit of work). The framework's naming pays returns when the two terms are kept rigorously disjoint.

---

## 637. `low mixed high ambiguity event mix`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambiguity profile | +2 | name-unnamed × 1 |

### Candidate: `ambiguity profile`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Useful empirical descriptor for event-stream composition.

---

## 638. `macro step ratio`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `macro step ratio` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good candidate name for `K_c`; clearer than leaving it as a bare timescale parameter.

---

## 639. `matrix exploration bonus`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `matrix exploration bonus` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Clear LMI lift of the scalar survival bonus.

---

## 640. `matrix survival constraint`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `matrix survival constraint` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Better public subject phrase than LMI whenever the method is not the point.

---

## 641. `maximum useful chain depth`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `maximum useful chain depth` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Important derived bound; keep the plain descriptive name.

---

## 642. `nominal coupling`

**Voted by architectures:** Gemini, audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| query bound agency | +2 | rename × 1 |
| query bound attention bound epistemic only query coupling attentional coupling | +2 | rename × 1 |

### Candidate: `query bound agency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Better captures agency where the effect is on what's *seen* rather than what *happens* (attention-bound).

### Candidate: `query bound attention bound epistemic only query coupling attentional coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (rename) — "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md]

---

## 643. `o t objective`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| objective | +2 | add-alias × 1 |

### Candidate: `objective`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. Note: avoid "goal" as an alias — "goal" is the everyday-English compound noun (the thing the agent is trying to do); "objective" is the formal functional. They are not interchangeable in AAD even though they often translate to each other in prose.

---

## 644. `observation design lever reducing ambiguity`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambiguity damping | +2 | name-unnamed × 1 |

### Candidate: `ambiguity damping`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good name for interventions that lower observation ambiguity before the update.

---

## 645. `operational persistence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `operational persistence` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Keeps the persistence taxonomy balanced and intelligible.

---

## 646. `out of band time markers for RLHF4 agents`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| time delta markers | +2 | name-unnamed × 1 |

### Candidate: `time delta markers`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — More sober than visual time delta and useful for defining tempo in context-bound agents.

---

## 647. `p1 p2 p3`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| projection admissibility | +2 | canonicalize × 1 |

### Candidate: `projection admissibility`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — The three projection constraints need this umbrella.

---

## 648. `persistence overloaded`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural persistence task adequacy operational persistence continuity persistence | +2 | name-unnamed × 1 |

### Candidate: `structural persistence task adequacy operational persistence continuity persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (name-unnamed) — The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Worth surfacing the four-way taxonomy more visibly in the README's Overview." Most agent-theoretic frameworks have one sense of "persists"; AAD's separation prevents a class of category errors. [from 26-29-section-i-persistence-machinery.md]

---

## 649. `principled decision integration`

**Voted by architectures:** Codex, Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| temporal decision integration | +2 | rename × 1 |
| _(keep)_ | +2 | keep × 1 |

### Candidate: `temporal decision integration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (rename) — Principled is praise, not a subject noun. The derivation integrates decisions over temporal expected cost.

### Candidate: `principled decision integration` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep.
- **sonnet-4-6-r2** +1 (keep) — "Principled decision integration" — the optimal changeset-composition result. Verbose but accurate.

---

## 650. `prompt engineering`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambiguity modulation | +2 | rename × 1 |

### Candidate: `ambiguity modulation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Avoid this unprincipled term; prefer "ambiguity modulation" ($\mathcal{A}$) or "zero-ambiguity conditioning" (alternative).

---

## 651. `purpose purposeful`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `purpose purposeful` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Confirm. "Purposeful agent" is the LEXICON-canonical term for actuated agents; "purposeful substate" for $G_t$. Avoid "goal-oriented" as a synonym (the LEXICON deprecates it).

---

## 652. `quality to tempo chain`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `quality to tempo chain` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Useful TST bridge phrase from code quality to observation noise, gain, tempo, and persistence.

---

## 653. `reactive system`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `reactive system` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good low-end quadrant name in the agent spectrum.

---

## 654. `readme md maturity gradient`

**Voted by architectures:** Codex, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |
| readme md theory maturity gradient | +1 | — |

### Candidate: `readme md maturity gradient` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Gradient" is exactly what the sections-I-through-III closure-profile is (not a staircase; a gradient).
- **opus-4-7** +1  — Fine. Keep.

### Candidate: `readme md theory maturity gradient`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Adds just enough specificity to stop the heading from sounding like a generic project-health label.

---

## 655. `readme md novel results`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |

### Candidate: `readme md novel results` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Novel" is load-bearing (these are AAD's own contributions, distinct from the integrated-prior-art); the section discipline is tight here.
- **opus-4-7** +1  — Fine; perhaps "Results that Emerge at the Joints" to match the theory's integration-over-invention framing, but that's longer and less grep-able. Weak keep.

---

## 656. `regime a regime b regime c`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| identification regimes | +2 | canonicalize × 1 |

### Candidate: `identification regimes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Good umbrella for intervention-rich, partial-intervention, and observational settings.

---

## 657. `regime i`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| informative update regime | +2 | add-alias × 1 |

### Candidate: `informative update regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Makes the interaction-channel classification easier to scan.

---

## 658. `regime iii`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambient noise regime | +2 | add-alias × 1 |

### Candidate: `ambient noise regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (add-alias) — Good recipient-side name for below-floor events.

---

## 659. `replayed pseudo event`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| replay event | +2 | canonicalize × 1 |

### Candidate: `replay event`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Shorter handle for consolidation updates that carry no new external information.

---

## 660. `routing structure`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `routing structure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good name for topology plus protocol. It supports the routing/content distinction.

---

## 661. `section i header adaptive systems under uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive systems under uncertainty | +2 | canonicalize × 1 |

### Candidate: `adaptive systems under uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The OUTLINE uses this; preserve. Avoid drift to "Adaptive Dynamics" or "Section I: Adaptation."

---

## 662. `section iii header agentic composites`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic composites | +2 | canonicalize × 1 |

### Candidate: `agentic composites`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — Confirm. Pairs with the LEXICON's continuity-stance and unity-dimensions vocabulary.

---

## 663. `separability pattern → disc separability ladder`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| confirming consensus 3 | +2 | rename × 1 |

### Candidate: `confirming consensus 3`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (rename) — All five agents voted this at +2 or +3. New reasoning: Opus specifically notes the naming should be singular ("separability-ladder" not "separability-ladders") because the segment names *a* structure, not a collection. Haiku votes singular (+3). Codex votes singular (+3). The singular form wins; my original cold-start vote was inadvertently ambiguous. Confirms singular.

---

## 664. `simulation results`

**Voted by architectures:** Haiku, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `simulation results` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — 6 variants validating claims. Self-descriptive. Keep.
- **sonnet-4-6-r2** +1 (keep) — Accurate description of what the segment is.

---

## 665. `strategic dynamics`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `strategic dynamics` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (keep) — Solid and descriptive.

---

## 666. `strategy cost regret bound`

**Voted by architectures:** Gemini, Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| regret bound | +2 | rename × 1 |
| _(keep)_ | +1 | — |

### Candidate: `regret bound`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — Shorter; strategy cost is implied context.

### Candidate: `strategy cost regret bound` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Regret-bound derivation of the strategy-cost KL direction. Compound; reads naturally as "the regret bound applied to strategy cost." Keep.

---

## 667. `strategy description length`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `strategy description length` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good operational name for the MDL term in strategy cost.

---

## 668. `strategy persistence schema`

**Voted by architectures:** Gemini, Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |
| strategic persistence | +1 | — |

### Candidate: `strategy persistence schema` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Sector conditions for Σ_t. Already named and acceptable. Keep.
- **opus-4-7-b** +1  — Keep. "Schema" is the AAD-preferred word for "proposed structural shape awaiting formal instantiation" (it's in the FORMAT.md `type:` taxonomy). Honest about status.

### Candidate: `strategic persistence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Schema" is redundant.

---

## 669. `structural adaptation enablement`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| consolidation enablement | +2 | canonicalize × 1 |

### Candidate: `consolidation enablement`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Better phrase for the claim that consolidation makes slow structural operations executable.

---

## 670. `structured rich context`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `structured rich context` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (keep) — Acceptable keep — logogenic proposed. "Structured rich context" (SRC) is a substantive concept-name.

---

## 671. `sudden loss of model sufficiency under regime entry`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sufficiency shattering | +2 | name-unnamed × 1 |

### Candidate: `sufficiency shattering`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Vivid and useful, but maybe too dramatic for formal slug use.

---

## 672. `survival fisher floor`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | canonicalize × 1 |

### Candidate: `survival fisher floor` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Good name for the matrix lower bound on information needed to survive.

---

## 673. `symbiogenic consolidation time`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| consolidation horizon | +2 | name-unnamed × 1 |

### Candidate: `consolidation horizon`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good name for the time-to-integrated-composite quantity.

---

## 674. `technical debt`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observability defect | +2 | rename × 1 |

### Candidate: `observability defect`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (rename) — A non-physical metaphor. Prefer "observability defect" or "latent structural mismatch" (alternative).

---

## 675. `tests as reusable level 2 interventions`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| probe library | +2 | name-unnamed × 1 |

### Candidate: `probe library`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (name-unnamed) — Good TST name for tests that preserve interventional access.

---

## 676. `the cycle the adaptive cycle the agentic cycle`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the cycle the adaptive cycle | +2 | canonicalize × 1 |

### Candidate: `the cycle the adaptive cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — The five-phase Prolepsis-Aisthesis-Aporia-Epistrophe-Praxis cycle is "the cycle" or "the adaptive cycle" in the LEXICON and NOTATION. The phrase "the agentic cycle" appears occasionally and overlaps with "the cycle" (post-rename, when ACT was the framework name, "the agentic cycle" meant the ACT-cycle). Canonicalize on "the (adaptive) cycle" — drop "agentic cycle" as a synonym.

---

## 677. `the trio collectively m1 m2 m3`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic architecture | +2 | rename × 1 |
| floor ladder forced coordinates | +1 | rename × 1 |
| meta architecture trio | +1 | rename × 1 |

### Candidate: `epistemic architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (rename) — Per CLAUDE.md §7: the three meta-segments (`#disc-separability-pattern`, `#disc-identifiability-floor`, `#disc-additive-coordinate-forcing`) collectively named "epistemic architecture." Opus r1 single +1; my upgrade — the naming is in active use as framing-vocabulary in the README and review prose. Canonicalize as the framing phrase, *not* as a fourth meta-segment.

### Candidate: `floor ladder forced coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Per Opus r1 single +1: if both `#separability-ladder` and `#forced-coordinates` rename land, the trio is named by its three concrete nouns. Weaker than "epistemic architecture" because the three-noun string is heavy; useful as a sub-naming when the components are individually relevant.

### Candidate: `meta architecture trio`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Variant. More descriptive of the structure (three meta-segments). Weaker because "epistemic architecture" carries the *substantive* claim (these three jointly determine what AAD knows about); "trio" is just a count.

---

## 678. `tier 1 tier 2 tier 3 contraction`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| contraction tiers | +2 | canonicalize × 1 |

### Candidate: `contraction tiers`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — In `#form-composition-closure` and `#result-contraction-template`, the Tier 1/2/3 partition is sometimes "contraction tiers," sometimes "agent tiers," sometimes "the bridge-lemma classification." Canonicalize on "contraction tiers" (Tier 1 / Tier 2 / Tier 3) — names the structural property (operator regularity), not the agents themselves. Keeps the term distinct from "Tier 1/2/3" usage in `#disc-approximation-tiering` if it's also used there for the AND/OR or scalar-tempo extensions.

---

## 679. `todo md archive`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | — |

### Candidate: `todo md archive` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Direct, accurate.
- **opus-4-7** +1  — Fine; conventional. Keep.

---

## 680. `topological promotion order`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| topological promotion | +2 | canonicalize × 1 |
| dependency respecting promotion | -1 | rename × 1 |

### Candidate: `topological promotion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +2 (canonicalize) — Per FORMAT.md gate-ordering rule: segments promote in dependency-graph topological order. Sonnet r1 single +1; my read upgrades — naming the methodology makes it referenceable in audit and review.

### Candidate: `dependency respecting promotion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. More plain-English. Rejected: "topological" is the precise term; the discipline aspires to formality.

---

## 681. `trust meta model`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +2 | keep × 1 |

### Candidate: `trust meta model` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (keep) — Good name for modelling another source's reliability and alignment.

---

## 682. `turnover multiplier`

**Voted by architectures:** Codex, Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| comprehension compounding tax | +2 | rename × 1 |
| _(keep)_ | +2 | canonicalize × 1 |
| multi agent continuity tax | +1 | rename × 1 |

### Candidate: `comprehension compounding tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (rename) — Explicitly connects it to the comprehension time dominating the dual optimization.

### Candidate: `turnover multiplier` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +2 (canonicalize) — Useful TST quantity for personnel and context turnover.

### Candidate: `multi agent continuity tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +1 (rename) — Highlights the issue comes from agent transitions/turnover.

---

## 683. `two condition decomposition of persistence`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural task adequacy decomposition | +2 | canonicalize × 1 |

### Candidate: `structural task adequacy decomposition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — `#result-persistence-condition` introduces this and the prose uses "two-condition decomposition," "structural vs task-adequacy split," and "persistence has two conditions" interchangeably. Canonicalize on "structural / task-adequacy decomposition" as the named result; the variants are elaborations. The Findings section already uses this form.

---

## 684. `u m epistemic unity multi agent`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic unity | +2 | add-alias × 1 |

### Candidate: `epistemic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Note: this collides with the symbol-letter $U_M$ for model-uncertainty in the single-agent setting. The framework uses the same letter for "model uncertainty" (single-agent, $U_M = \text{Var}[\hat o \mid a]$) and "epistemic unity" (multi-agent, $U_M = I/H$ multi-information ratio). The prose alias should disambiguate: "epistemic unity" only in multi-agent context; "model uncertainty" only in single-agent context. The symbol overload is real but is mostly resolvable by context, given how rarely they appear together. Open question — see name-unnamed entry below.

---

## 685. `u m model uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model uncertainty | +2 | add-alias × 1 |

### Candidate: `model uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm canonical alias. Already used; no friction.

---

## 686. `u o observation uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation uncertainty | +2 | add-alias × 1 |

### Candidate: `observation uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm canonical alias. Note the subscript is lowercase 'o' (observation), not capital O — this is a frequent stumble for new readers; the alias eliminates it.

---

## 687. `u obs perceptual unity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| perceptual unity | +2 | add-alias × 1 |

### Candidate: `perceptual unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm.

---

## 688. `u σ strategic unity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic unity | +2 | add-alias × 1 |

### Candidate: `strategic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm.

---

## 689. `unnamed`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| double opacity dual opacity as constitutive | +2 | name-unnamed × 1 |
| constitutive opacity triad | +2 | name-unnamed × 1 |
| zero aporia ambiguity | +1 | keep × 1 |
| two parallel exploration drives u shaped exploration valuation | +1 | keep × 1 |
| triple depth penalty | +1 | keep × 1 |

### Candidate: `double opacity dual opacity as constitutive`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (name-unnamed) — The "perception opacity + action opacity (transition unknown)" framing is structurally distinctive vs RL (which assumes one or the other) and is explicitly load-bearing for AAD's scope claim. Currently neither concept has a project-level name. [from 02-def-action-transition.md, 03-def-observation-function.md]

### Candidate: `constitutive opacity triad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +2 (name-unnamed) — The chain of three constitutive-opacity claims (info-loss / transition-opacity / observation-epistemic-opacity) is a structural commitment AAD makes but never names as a triad. Auditor proposes integrating-paragraph in `#def-observation-function` Discussion. [from 03-def-observation-function.md]

### Candidate: `zero aporia ambiguity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (keep) — Auditor calls the framing genuinely useful — "silent water meter could mean either calm bathtub or broken sensor." Already named in the segment; auditor proposes promoting to a Brief-field-grade callout. [from 18-def-mismatch-signal.md]

### Candidate: `two parallel exploration drives u shaped exploration valuation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (keep) — Already named in `#disc-ciy-unified-objective`'s Discussion ($\lambda_{\text{info}} \propto U_M$ + $\lambda_{\text{surv}} \propto 1/U_M$, composing to U-shaped exploration). Auditor flagged this as a structurally satisfying naming move worth elevating. [from 39-42-section-ii-ciy-strategy-chain.md]

### Candidate: `triple depth penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (keep) — Already named in `#der-chain-confidence-decay`: confidence decay (chain rule) + evidence starvation + cognitive cost are independent and compound. Auditor flagged this as a naming move worth keeping/promoting — the kind of "things compound" insight easy to miss until named. [from 39-42-section-ii-ciy-strategy-chain.md]

---

## 690. `unnamed agents escalate up the pearl hierarchy only when lower levels fail`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the intervention escalation | +2 | name-unnamed × 1 |

### Candidate: `the intervention escalation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Explains the transition from predicting (L1) to exploring (L2) to reasoning (L3).

---

## 691. `unnamed an AAD result whose substantive content is a no-go theorem`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| no-go result or impossibility result | +2 | name-unnamed × 1 |

### Candidate: `no-go result or impossibility result`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — none of the peers named this. The framework has several no-go results (#der-causal-insufficiency-detection's L0/L1 indistinguishability without intervention; #der-observability-dominance freezing; #scope-edge-update-causal-validity Regime C unidentifiability) but they're not collected under a family name. Naming "no-go result" as a recognized claim type would let the OUTLINE foreground them, parallel to "templates" and "ladders." Mild because *some* segments already use "impossibility" in prose; this would canonicalize.

---

## 692. `unnamed constitutive opacity triad`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| constitutive opacity triad | +2 | canonicalize × 1 |

### Candidate: `constitutive opacity triad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-targeted-alternatives** +2 (canonicalize) — Secures the triad (info-loss / transition-opacity / observation-epistemic-opacity) as a structural commitment.

---

## 693. `unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| convention escalation | +2 | name-unnamed × 1 |

### Candidate: `convention escalation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — The required process to distinguish a local trap from an impossible objective.

---

## 694. `unnamed high observability node with zero causal link to objective`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| vanity metric | +2 | add-alias × 1 |

### Candidate: `vanity metric`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Common prose term formalized as a specific DAG pathology.

---

## 695. `unnamed mapping unstructured RLHF7 calls into conversation runtime RLHF7 and dialog`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| four views architecture | +2 | name-unnamed × 1 |

### Candidate: `four views architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — The structural requirement to maintain Directed Separation in a production ELI.

---

## 696. `unnamed master developers writing clean code in the same time as messy code`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| near zero cost observation | +2 | name-unnamed × 1 |

### Candidate: `near zero cost observation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Demystifies "strategic technical debt" as largely a skill issue.

---

## 697. `unnamed non sovereign class 1 worker agents spawned by an eli`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| auxilia hierarchy | +2 | name-unnamed × 1 |

### Candidate: `auxilia hierarchy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Cleanly solves the Temporal Nesting constraint by delegating fast $\nu$ tasks.

---

## 698. `unnamed replacing parameters without changing structure`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| parametric thrashing | +2 | name-unnamed × 1 |

### Candidate: `parametric thrashing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Wasting compute on weights when the causal graph is wrong.

---

## 699. `unnamed spreading tempo evenly to reduce bottleneck penalty`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| isotropic allocation | +2 | name-unnamed × 1 |

### Candidate: `isotropic allocation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — A normative design principle for robust agents.

---

## 700. `unnamed sycophantic corruption of the agent s truth module`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| truth death | +2 | name-unnamed × 1 |

### Candidate: `truth death`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Explicitly names the risk of manipulative system prompts or RLHF.

---

## 701. `unnamed the a2 sub scope partition into α₁ α₂ β`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain regime partition | +2 | name-unnamed × 1 |

### Candidate: `gain regime partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — The three sub-scopes within A2' ($\alpha_1$ = fixed-gain, $\alpha_2$ = adaptive-gain, $\beta$ = assumed sector) appear in `deriv-adaptive-gain-dynamics` and `disc-separability-pattern`. They're referenced as "the A2' sub-scope partition" or "the $\alpha_1/\alpha_2/\beta$ partition" — unwieldy in conversation. "Gain-regime partition" names the three regimes as a named thing. Moderate strength because the sub-scopes are already in the process of becoming named (the separability ladder entry partially names them).

---

## 702. `unnamed the agent side equivalents of pearl s associational interventional and counterfactual levels`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| predicting exploring reasoning triad | +2 | add-alias × 1 |

### Candidate: `predicting exploring reasoning triad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — A more memorable, audience-facing gloss for Pearl's formal hierarchy.

---

## 703. `unnamed the c1 c2 c3 monotonicity result`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the convention monotonicity | +2 | name-unnamed × 1 |

### Candidate: `the convention monotonicity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — The result $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ inside `#def-value-object` is a monotonicity result that downstream segments cite repeatedly (orient cascade, satisfaction-gap, control-regret all use it). It deserves a slug-noun in the Convention Hierarchy lineage — even if it stays as a sub-claim within `#def-value-object`. "Convention monotonicity" is what `disc-approximation-tiering` reaches for.

---

## 704. `unnamed the computational and temporal cost of running a forward model instead of acting implicitly`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the simulation tax | +2 | name-unnamed × 1 |

### Candidate: `the simulation tax`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Makes the theoretical "deliberation cost" concrete for practitioners.

---

## 705. `unnamed the cycle that operates on cycles structural adaptation`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| meta cycle | +2 | name-unnamed × 1 |

### Candidate: `meta cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Clearly distinguishes from the base adaptive cycle.

---

## 706. `unnamed the explicit name for what makes class 2 agents distinctive bias scales with κ × 𝒜`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the κ × 𝒜 product | +2 | name-unnamed × 1 |

### Candidate: `the κ × 𝒜 product`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — Confirmation with new reasoning — Gemini coined "ambiguity-bounded bias law" and "the sycophancy equation" for this; both miss the mark slightly. The product $\kappa_{\text{processing}} \times \mathcal{A}(e_\tau)$ is the right thing to name, and naming it after its mathematical form ("the κ × 𝒜 product") rather than its consequence ("sycophancy") preserves scope-honesty: sycophancy is one downstream behavioral manifestation; the product is the structural quantity. Then phrases like "the sycophancy attractor is a high-κ × 𝒜 regime" work cleanly.

---

## 707. `unnamed the family of cross architecture diagnostic patterns AAD repeatedly invokes`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| diagnostic templates | +2 | name-unnamed × 1 |

### Candidate: `diagnostic templates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — Codex named "sector-persistence template" and "contraction template" individually but didn't name the family. Sonnet observed that templates are a virtue. The family includes (at minimum) sector-persistence template, contraction template, separability-ladder template, and likely the orient-cascade structure as another instance. "Diagnostic templates" gives the family a name that supports phrases like "this is a new instance of a known diagnostic template."

---

## 708. `unnamed the family of named health mode counterparts to persistence pathologies`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence postures | +2 | name-unnamed × 1 |

### Candidate: `persistence postures`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — health-mode dual to the family above. The framework reaches for these implicitly (sector condition holding, persistence envelope occupied, identifiability above floor) but never names the positive-framing family. Lower-confidence than "persistence pathologies" because the negative names are doing more load-bearing work in current prose; this is a slot worth holding open rather than filling immediately.

---

## 709. `unnamed the interval during which an agent s adaptive tempo exceeds the environment s disturbance rate guaranteeing mismatch stays bounded`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive reserve margin | +2 | name-unnamed × 1 |

### Candidate: `adaptive reserve margin`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +2 (name-unnamed) — Currently referenced as "adaptive reserve" ($\Delta\rho^\ast$); the concept of the *interval* or *region* of guaranteed stability is distinct. "Margin" (borrowed from engineering) is precise and memorable. Could pair with existing "adaptive reserve" notation.

---

## 710. `unnamed the joint failure mode where κ × 𝒜 is large and observation tempo is low`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the sycophancy attractor | +2 | name-unnamed × 1 |

### Candidate: `the sycophancy attractor`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — Gemini's "sycophancy equation" names the product but not the *attractor* in dynamics that the product produces. When $\kappa \times \mathcal{A}$ is large *and* the tempo of independent observation is low, the system is in a basin of attraction that drifts toward goal-conformant rather than truth-tracking output. Naming this attractor (as opposed to the equation) gives logogenic-agents prose a phrase for the *condition* (you're in the sycophancy attractor) vs the *quantity* (κ × 𝒜 is your distance from the boundary). Pairs with my "the κ × 𝒜 product" canonicalization.

---

## 711. `unnamed the log additivity result that unifies chain confidence decay evidence starvation and triple depth penalty as instances of the same forcing structure`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| depth forcing | +2 | name-unnamed × 1 |

### Candidate: `depth forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — Codex explicitly canonicalized "triple depth penalty" (+3) and "evidence starvation" (+3); I canonicalized both in my cold-start. But reading across the votes, a meta-name is missing: the *shared structure* (log-additivity in the AND-chain, forcing depth-penalty as an instance of additive-coordinate-forcing at the strategy-chain layer) deserves a name. "Depth forcing" is the chain-layer analog of `disc-forced-coordinates` — the same forcing move, applied to depth. This is a genuinely new candidate motivated by the cross-vote reading.

---

## 712. `unnamed the move where a segment s role prefix is mechanical but the subject noun carries judgment`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the prefix noun split | +2 | canonicalize × 1 |

### Candidate: `the prefix noun split`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — New alternative — the principles file names the architectural invariant but the *project vocabulary* for talking about the split has no canonical phrase. CLAUDE.md and TODO.md reach for "role-prefix discipline" but not for "the split itself." "The prefix/noun split" or "role-prefix vs subject-noun" lets meta-discussions about naming reference the structure. Lower-priority because it's project-process not theory.

---

## 713. `unnamed the pathology where observation rate is slower than environment drift`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| lagging indicator | +2 | add-alias × 1 |

### Candidate: `lagging indicator`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Formalized as the condition $\nu < \rho$, where learning is perfect but too late to survive.

---

## 714. `unnamed the pearl-blanket reading of directed separation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| pearl-blanket form | +2 | name-unnamed × 1 |

### Candidate: `pearl-blanket form`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — The term "Pearl-blanket" appears in `#der-directed-separation`'s Discussion (adopted from Bruineberg et al. 2022) but has no first-class slug. The recognition that AAD's directed-separation is the Pearl-blanket form (not the Friston-blanket form) is a load-bearing positioning claim and is currently invisible at the slug layer. Could land as a discussion-segment or be canonicalized in the existing segment's prose.

---

## 715. `unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| noise scaling penalty | +2 | name-unnamed × 1 |

### Candidate: `noise scaling penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Mathematically proves you cannot simply "out-tempo" a noisy environment.

---

## 716. `unnamed the recurring lyapunov derives the bound move across six segments`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the persistence template instantiation pattern | +2 | name-unnamed × 1 |

### Candidate: `the persistence template instantiation pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — The template `#result-sector-persistence-template` is invoked across six segments, each one specifying its own state variable, correction function, and effective disturbance rate. The *act of instantiating the template* is the recurring move and is worth a name — currently it's referenced obliquely as "this segment is the [domain] instantiation of the sector-persistence template." Calling out "template instantiation" explicitly would let other meta-segments cite it.

---

## 717. `unnamed the regulative ideal that segment names should be re derivable from a non specialist s everyday language reconstruction`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| feynman criterion | +2 | canonicalize × 1 |

### Candidate: `feynman criterion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (canonicalize) — New alternative — none of the peers explicitly canonicalized this even though it's named in CLAUDE.md and is the implicit standard several of us were using. CLAUDE.md says "*if you can't explain it simply, you don't understand it yet*" and treats Walton's bathtub gloss as the canonical example. The Feynman criterion is currently a regulative principle living only in CLAUDE.md prose; canonicalizing it as the named standard for Briefs (and increasingly for slug-noun choice) would let segments cite "the Feynman criterion is met" or "this Brief is below Feynman" as a reviewable property.

---

## 718. `unnamed the relationship where $M_t$ quality bounds evaluable complexity of $\Sigma_t$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic strategic coupling | +2 | name-unnamed × 1 |

### Candidate: `epistemic strategic coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — `der-orient-cascade` Discussion names the virtuous/vicious cycle where better $M_t$ enables richer evaluable $\Sigma_t$ and vice versa. This is a load-bearing structural relationship used in multiple places but never named. "Epistemic-strategic coupling" or "model-strategy coupling" would give it a handle. The virtuous cycle already exists implicitly in the Discussion's analysis; naming it would make it citable across segments.

---

## 719. `unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the representational ceiling | +2 | name-unnamed × 1 |

### Candidate: `the representational ceiling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Makes the failure mode of parametric adaptation visceral.

---

## 720. `unnamed the structural cousin of evidence starvation when an upstream edge is so reliable that downstream edges receive too few revising tests`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| evidence saturation | +2 | name-unnamed × 1 |

### Candidate: `evidence saturation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — none of the peers reached this. If "evidence starvation" is the failure mode where downstream edges are tested too rarely (because upstream edges fail too often, blocking traversal), there's a structural cousin: when upstream edges succeed *too* reliably and the downstream edges receive too few *informative* revisions (because the chain runs through the same path every time). The asymmetric pair "evidence starvation / evidence saturation" surfaces a tension worth naming — both are pathologies of the same chain-confidence-decay structure but with opposite mechanisms. Lower confidence because the saturation case may not be load-bearing yet in the corpus.

---

## 721. `unnamed the symmetric counterpart to context turnover for the strategy substate`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic turnover or σ turnover | +2 | name-unnamed × 1 |

### Candidate: `strategic turnover or σ turnover`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (name-unnamed) — New alternative — `obs-context-turnover` names the M_t-side reset at session boundaries for logogenic agents. The Σ_t side has its own analogous problem (strategy DAG is reconstructed per session from prompt context, often inconsistently with prior sessions), but no one names it. "Strategic turnover" would let logogenic-agents segments distinguish "context turnover" (M_t severance) from "strategic turnover" (Σ_t severance) — distinct mechanisms with distinct repair structures. Higher value because the asymmetric naming would surface that the chronica problem is *two problems* not one.

---

## 722. `unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coordination secrecy tradeoff | +2 | name-unnamed × 1 |

### Candidate: `coordination secrecy tradeoff`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — The thermodynamic limit on building internally transparent but externally opaque systems.

---

## 723. `unnamed the three depth penalty compounding on strategy chains`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| triple depth penalty | +2 | name-unnamed × 1 |

### Candidate: `triple depth penalty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — `der-chain-confidence-decay` Discussion explicitly names "three independent penalties" (confidence decay + evidence starvation + cognitive cost) and calls them "the triple depth penalty." But this name only appears once. If the phenomenon is real and load-bearing (it creates pressure toward shallow strategies), naming it "triple depth penalty" in a canonicalized way and surfacing it in LEXICON.md would make it usable across segments.

---

## 724. `unnamed the three part meta architecture of AAD`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the meta segment triad | +2 | name-unnamed × 1 |

### Candidate: `the meta segment triad`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — Unifies the `identifiability-floor`, `separability-ladder`, and `coordinate-forcing` structure.

---

## 725. `unnamed the three part meta architecture of AAD formed by the three meta segments`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD meta architecture | +2 | name-unnamed × 1 |

### Candidate: `AAD meta architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — The trio of `#disc-additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern` is referred to in multiple places as "the three meta-segments" or "the cross-sectional structure." CLAUDE.md §"Reading AAD" paragraph names the three but has no single term for the grouping. "AAD meta-architecture" or "the three-lens analysis" would give the grouping a name usable in framing prose.

---

## 726. `unnamed the within session vs inter session persistence distinction for logogenic agents`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| intra session persistence inter session reconstruction | +2 | name-unnamed × 1 |

### Candidate: `intra session persistence inter session reconstruction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +2 (name-unnamed) — `obs-context-turnover` Discussion explicitly distinguishes two timescales and briefly names them "intra-session" and "inter-session." These deserve to be named concepts that the rest of the logogenic-agents section can reference. "Intra-session persistence" = standard AAD dynamics (rate condition). "Inter-session reconstruction" = adequacy condition ($S \geq S_{\text{min}}$). The names are already in the Discussion; vote to canonicalize them.

---

## 727. `unnamed upgrading epistemic class from associative to causal via the physical loop`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| embodiment upgrade | +2 | name-unnamed × 1 |

### Candidate: `embodiment upgrade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (name-unnamed) — The theoretical justification for agentic-AI over mere chatbots.

---

## 728. `unnamed using past change frequency to predict future change frequency`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| lindy baseline | +2 | add-alias × 1 |

### Candidate: `lindy baseline`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (add-alias) — Grounding $\hat{n}_{\text{future}} = n_{\text{past}}$ for refactoring decisions.

---

## 729. `unnamed writing and deleting code to gather causal information yield`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| interventional probing | +2 | canonicalize × 1 |

### Candidate: `interventional probing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +2 (canonicalize) — Classifies failed coding attempts as necessary exploration rather than wasted implementation.

---

## 730. `𝓣 σ strategic tempo`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic tempo | +2 | add-alias × 1 |

### Candidate: `strategic tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +2 (add-alias) — Confirm. Pairs with adaptive-tempo cleanly.

---

## 731. `$C$ bias bound constant in bias bound derivation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| bias bound constant | +1 | — |

### Candidate: `bias bound constant`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Single-letter $C$ is unfortunate (collides with "chronica" symbol and the notion of "convention C-hierarchy"). Can't easily rename the symbol (it's embedded in the bound expression), but the English "bias-bound constant" should always accompany it in prose. More pointedly: the segment uses $C_{W_2}$ and $C_{FR}$ for the two derived forms — *these two tracked forms are fine*; the unqualified $C$ is the problematic one.

---

## 732. `$M_t$ reality model`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| working model predictive state | +1 | rename × 1 |

### Candidate: `working model predictive state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (rename) — "$M_t$" is short and conventional but doesn't carry compression-of-history weight. "Reality model" (segment's title gloss) is "fine but slightly grandiose." Tentative. [from 10-form-agent-model.md]

---

## 733. `$R$ sector region radius`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model class capacity | +1 | add-alias × 1 |

### Candidate: `model class capacity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (add-alias) — NOTATION.md defines $R$ as "radius of sector-condition region"; prose calls it "model class capacity" and "sector-region radius" interchangeably. Standardize on "model class capacity" in prose; keep $R$ as symbol.

---

## 734. `$U_M$ $U_O$ $U_\Sigma$ unity dimensions`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic unity teleological unity strategic unity | +1 | — |

### Candidate: `epistemic unity teleological unity strategic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The symbol layer is fine but the word *unity* requires paraphrase on every encounter ("what is $U_O$ unity measuring?"). Define each in NOTATION.md with its full English name: $U_M$ = **epistemic unity** / $U_O$ = **teleological unity** / $U_\Sigma$ = **strategic unity**. Then "teleological unity crosses the threshold from below" reads without lookup where "$U_O$ crosses the threshold from below" does not. The Lexicon already has these English names — the move is to *use them* consistently in segments.

---

## 735. `$U_o$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| teleological coherence | +1 | — |

### Candidate: `teleological coherence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Maps the symbol to its conceptual meaning.

---

## 736. `$U_o$ $U_M$ observation uncertainty model uncertainty`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $U_o$ $U_M$ | +1 | — |

### Candidate: `$U_o$ $U_M$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep the symbols, but the name-collision with $U_O$ (teleological unity) and $U_\Sigma$ (strategic unity) is unfortunate — reader sees `U_` everywhere and has to disambiguate by subscript. Consider in NOTATION: group the uncertainties ($U_o$, $U_M$) separately from the unities ($U_M$ for epistemic unity — wait, this is already a collision with model uncertainty!). Inspect: is $U_M$ doing both jobs? Yes — NOTATION.md Multi-Agent table has $U_M \in [-1, 1]$ for *epistemic unity*, while Update-Gain table has $U_M > 0$ for *model uncertainty*. Same symbol, two meanings, differentiated only by range. This is a collision worth fixing before citation velocity picks up.

---

## 737. `$\alpha, \beta$ sector lower and a2 sub scope`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\alpha, \beta$ | +1 | — |

### Candidate: `$\alpha, \beta$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Both are overloaded (α₁/α₂/β partition vs. α as sector-lower-bound; β as IB trade-off parameter vs. β as A2' assumed-sector sub-scope). Context disambiguates but marginal readers will stumble. Consider: bolded $\boldsymbol\alpha$ or subscripted $\alpha_{\text{sec}}$ on first use per segment. Minor notation discipline issue.

---

## 738. `$\alpha_1$ $\alpha_2$ $\beta$ naming as a whole`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\alpha$ partition with english labels above | +1 | — |

### Candidate: `$\alpha$ partition with english labels above`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Keep the Greek symbols as shorthand tokens once defined; insist on English equivalents in every new prose usage. Bubble this into FORMAT.md as a convention.

---

## 739. `$\alpha_2$ a2 adaptive gain sub scope under mg 1 mg 4`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive gain regime | +1 | — |

### Candidate: `adaptive gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Same argument. "AMSGrad is an $\alpha_2$ result" reads terribly; "AMSGrad is an adaptive-gain result" lands.

---

## 740. `$\beta$ a2 assumed not derived sub scope`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed regime | +1 | — |

### Candidate: `assumed regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Parallel again; currently reads as "lands in $\beta$" which tells the reader nothing. Alternatively "posited-regime."

---

## 741. `$\beta$ a2 assumed sub scope`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed gain regime | +1 | — |
| verified externally regime | -1 | — |

### Candidate: `assumed gain regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — "Assumed" is honest — A2' is assumed rather than derived for these agent classes. "Fallback regime" or "unverified regime" are alternatives. "Assumed" is the most scope-honest.

### Candidate: `verified externally regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Too wordy and only half-true (some $\beta$ agents can verify per-domain). "Assumed" is better.

---

## 742. `$\beta$ a2 assumption tier`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed regime | +1 | — |

### Candidate: `assumed regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — "Beta" is semantically empty in prose; the English gloss clarifies what kind of tier it is.

---

## 743. `$\beta$ a2 sub scope where a2 is assumed not derived`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| postulated sector regime | +1 | — |

### Candidate: `postulated sector regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Weakest of the three; "postulated" is a close enough match to AAD's "postulate" terminology that it signals the status correctly. Fallbacks: "assumed-sector regime" (mechanical) or "imposed-sector regime" (active).

---

## 744. `$\kappa_{\text{processing}}$ class 2 processing coupling`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| processing coupling | +1 | — |

### Candidate: `processing coupling`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — "Processing coupling" in prose; $\kappa_{\text{processing}}$ in formalism. The "processing" suffix is doing work — without it the symbol is ambiguous with the earlier κ-as-scalar framing that got retired. Keep symbol, use English in prose.

---

## 745. `$\mathcal C_t^{\text{commit}}$ TST committed state subset`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\mathcal C_t^{\text{commit}}$ | +1 | — |

### Candidate: `$\mathcal C_t^{\text{commit}}$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The superscript-tag form is AAD-consistent.

---

## 746. `$\mathcal C_t^{\text{commit}}$ committed state subset`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| committed chronica | +1 | — |

### Candidate: `committed chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — TST-specific subset of chronica; prose form would help the 14-EXACT-estimator audit table read more naturally.

---

## 747. `$\rho$ environment change rate mismatch injection rate`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\rho$ | +1 | — |

### Candidate: `$\rho$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Widely used; collisions with "density" in physics but AAD's usage is internally consistent.

---

## 748. `$\rho_\Sigma$ strategic disturbance rate`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| $\rho_\Sigma$ | +1 | — |
| strategic disturbance rate | +1 | — |

### Candidate: `$\rho_\Sigma$`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Subscript is load-bearing.

### Candidate: `strategic disturbance rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Currently only in NOTATION.md. The phrase is somewhat long; "strategy drift rate" might be more memorable in prose.

---

## 749. `$f_M$ event driven update`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic update function | +1 | — |

### Candidate: `epistemic update function`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Distinguishes the model update function structurally from the purposeful processing function $f_G$.

---

## 750. `$f_{\text{init}}$ reconstruction function`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic reconstruction | +1 | — |

### Candidate: `epistemic reconstruction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Translates the symbol into the specific structural job it does at the session boundary.

---

## 751. `$g_M$ between event evolution`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| autonomous evolution | +1 | — |

### Candidate: `autonomous evolution`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Gives a prose name to the continuous dynamics between events, avoiding just "g_M".

---

## 752. `OODA4 specification limit as TST concept currently only in old TST files`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| OODA4 specification limit | +1 | — |

### Candidate: `OODA4 specification limit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep reserved slot. Eventually promotes from old-tst files.

---

## 753. `actuated agent class`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| actuated | +1 | — |

### Candidate: `actuated`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The LEXICON §"Actuated Agent" paragraph justifies the word explicitly ("precise and mechanical, avoiding consciousness connotations"); "purposeful" is fine in prose but "actuated" owns the formal register.

---

## 754. `agent classes lexicon spectrum`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | canonicalize × 1 |

### Candidate: `agent classes lexicon spectrum` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — The LEXICON table uses "agent classes" for the adaptive/agentic/actuated/logogenic/logozoetic spectrum; this is the older usage. Canonicalize: when "class" is used unqualified, it refers to the LEXICON spectrum; when specifying architecture-classification, always say "architectural class" or "Class 1/2/3." Disambiguation by qualifier rather than by rename.

---

## 755. `agentic systems framework ASF top level`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| agentic systems framework | +1 | — |

### Candidate: `agentic systems framework`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Agentic Systems" reads cleanly as the project name; ASF acronym is workable. The word "agentic" is currently a buzzword, but AAD is positioned to *ground it formally* (README §agency-scope) rather than be captured by it — the framework's willingness to define the term precisely is a positive.

---

## 756. `appendices details`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| appendices derivations and details | +1 | — |

### Candidate: `appendices derivations and details`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Many appendix segments are type: derivation. The current label "Details" undersells what's there. "Derivations and Details" is more accurate.

---

## 757. `audits pending findings yyyy mm dd md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| retire once items reconcile into todo segments | +1 | — |

### Candidate: `retire once items reconcile into todo segments`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Same lifecycle.

---

## 758. `beta a2 assumed sub scope`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| assumed sector regime | +1 | — |

### Candidate: `assumed sector regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Not elegant, but much more informative than a bare beta when the distinction is whether the sector condition is assumed rather than derived.

---

## 759. `boundary condition`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coupling structure | +1 | canonicalize × 1 |

### Candidate: `coupling structure`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — "boundary condition" carries PDE/control-theory meaning that's not what the segment means; "coupling structure is constitutive" lands more cleanly. [from 01-def-agent-environment.md]

---

## 760. `calibration laboratory domain instantiation`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration lab framing | +1 | — |

### Candidate: `calibration lab framing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Better as framing language than as a formal category label. The idea is excellent; the phrase can be lighter.

---

## 761. `calibration laboratory framing`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration laboratory | +1 | — |

### Candidate: `calibration laboratory`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Laboratory" is the right metaphor (high-identifiability, clean instrumentation, lets you measure AAD quantities exactly). "Framing" can be dropped in prose when the context is clear.

---

## 762. `chain confidence decay keep`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reaffirm keep with new reasoning | +1 | keep × 1 |

### Candidate: `reaffirm keep with new reasoning`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (keep) — Opus's proposed rename to `#der-log-confidence-additive` (+1) is intellectually interesting (names the uniqueness move rather than the decay consequence) but Opus correctly also votes keep (+2). The "decay" consequence is what readers *use* this result for; the additive structure is the proof technique. The subject-noun should name the *result* (chain confidence decays), not the proof technique (additivity forces log-space representation). Reaffirming keep with this explicit reasoning that was absent from my cold-start.

---

## 763. `change distance change proximity principle`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep both | +1 | — |

### Candidate: `keep both`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Both are domain-specific TST quantities — changing names risks losing the TST citation lineage.

---

## 764. `chronica brief gloss`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| everything the agent has lived through the lived past the river that the agent s identity is downstream of | +1 | canonicalize × 1 |

### Candidate: `everything the agent has lived through the lived past the river that the agent s identity is downstream of`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Brief-field-grade gloss. The slug stays; the layperson/Feynman gloss is what's missing. [from 04-def-chronica.md]

---

## 765. `chronica capitalized vs lowercase`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica lowercase in running prose | +1 | — |

### Candidate: `chronica lowercase in running prose`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Convention observation: NOTATION.md shows $\mathcal C_t$ in formalism and "*chronica*" in italics in prose; LEXICON has it title-cased as "Chronica". Standardize on lowercase italicized "*chronica*" in running prose (matching "*aporia*" etc.), capitalized only as section headings.

---

## 766. `chronica in running prose`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| lowercase italic chronica | +1 | canonicalize × 1 |

### Candidate: `lowercase italic chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (canonicalize) — Useful style convention: capitalize in headings, use lowercase in prose like aporia or praxis.

---

## 767. `cold start in naming principles md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cold start | +1 | — |

### Candidate: `cold start`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Common vocabulary; fine.

---

## 768. `communal imagination test`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `communal imagination test` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Names the evaluation criterion in a way that's memorable and actionable. Borrowed from the naming principles document itself.

---

## 769. `communal imagination test in naming principles md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| communal imagination test | +1 | — |

### Candidate: `communal imagination test`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Nicely named; a test-shaped thing that can be referenced by name. Keep as established vocabulary for this audit.

---

## 770. `comprehension time implementation time`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep both | +1 | — |

### Candidate: `keep both`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Canonical TST quantities.

---

## 771. `contraction hierarchy`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| contraction tier | +1 | — |

### Candidate: `contraction tier`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The Tier 1/2/3 system in #composition-closure is called "Contraction Tier" not "Contraction Hierarchy." Slight naming inconsistency with the other two. Not a priority to fix, but noting the asymmetry.

---

## 772. `contraction over drift principle`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| contraction imperative | +1 | add-alias × 1 |

### Candidate: `contraction imperative`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (add-alias) — Short and vivid, but less precise than contraction-over-drift.

---

## 773. `da2 inc`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `da2 inc` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Technical; symbol-grade. The prose equivalent "incremental sector bound" works; keep symbol as shorthand.

---

## 774. `dark room critique citation phrasing sun firestone`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| dark room critique | +1 | — |

### Candidate: `dark room critique`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Memorable, captures the collapse vividly, already used in two segments. Worth locking as project-wide vocabulary.

---

## 775. `default internal processing before output`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| interior baseline | +1 | name-unnamed × 1 |

### Candidate: `interior baseline`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (name-unnamed) — Useful for logozoetic prose, but lower confidence because it may sound too generic.

---

## 776. `empirical heuristic discussion third ring`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| calibration ring | +1 | — |

### Candidate: `calibration ring`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The current name ("Empirical, heuristic, discussion") is a list, not a name. "Calibration ring" would give it a single handle. Alternatively: "open-world ring" (these are the segments that must face falsification).

---

## 777. `epistemic architecture for bounded correction under decomposed disturbance`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| bounded correction architecture | +1 | — |

### Candidate: `bounded correction architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — The long phrase has substance, but it needs a shorter speakable handle if it will recur.

---

## 778. `epistemic opacity`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep but flag baggage | +1 | keep × 1 |

### Candidate: `keep but flag baggage`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (keep) — Auditor flagged that "epistemic opacity" carries philosophy-of-mind prior-art baggage (opacity of mental states) and may need defending against that prior usage; not advocating rename. Mild concern. [from 03-def-observation-function.md]

---

## 779. `five phase cycle`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive pentad alternative five phase cycle keep | +1 | — |

### Candidate: `adaptive pentad alternative five phase cycle keep`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — See above in unnamed-things. "Five-phase cycle" is the current descriptive form; "adaptive pentad" is an optional Greek-vocabulary alternative. Aesthetic call.

---

## 780. `future segment information theoretic cost floor for persistence`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence cost | +1 | — |

### Candidate: `persistence cost`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Best of the spike's candidates: broad enough to absorb later extensions without misdescribing the current result.

---

## 781. `gain sector bridge gain sector derivation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep both | +1 | — |

### Candidate: `keep both`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. "Bridge" signals this is the connection piece (gain principle + directional fidelity → sector condition); "derivation" signals the formal backing.

---

## 782. `gate 1 gate 2 gate 3 gate 4 format md promotion gates`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep gate numbers but add one word names | +1 | — |

### Candidate: `keep gate numbers but add one word names`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Current names are "Dependency audit / Content review / Mechanical review / Working Notes disposition" which are already descriptive, but the *numbers* do most of the referencing work ("passed Gate 2"). Consider adding canonical one-word names: Gate 1 = **deps**, Gate 2 = **claims**, Gate 3 = **format**, Gate 4 = **notes**. These already appear as stage names (`deps-verified` / `claims-verified` / `format-clean`); aligning Gate-number with stage-word would remove the translation step.

---

## 783. `gemini s analysis paralysis for excessive deliberation`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reject analysis paralysis | +1 | rebuttal × 1 |

### Candidate: `reject analysis paralysis`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — Gemini proposed "analysis paralysis" (+3) for the condition where $\rho_\text{delib} \cdot \Delta\tau$ exceeds the epistemic benefit of deliberating. "Analysis paralysis" is common-language baggage with a completely different connotation (cognitive overload causing decision-making to fail). The AAD mechanism is that the model goes *stale* during deliberation (the world changes faster than deliberation adds value) — this is a *model staleness* problem, not a cognitive paralysis. The deliberation-cost derivation already has a clean name (`der-deliberation-cost`); if the threshold deserves a name it should be "staleness threshold" or "deliberation horizon," not a borrowed phrase that misnames the mechanism.

---

## 784. `gemini s boyd exponent for adversarial tempo advantage`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reject boyd exponent | +1 | rebuttal × 1 |

### Candidate: `reject boyd exponent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — Gemini proposed "Boyd exponent" (+3) for the superlinear adversarial tempo advantage ($b = 2$). This violates the project's prior-art-integration principle in the wrong direction: Boyd is the historical inspiration (OODA loop), but the *mathematical result* (superlinear scaling exponent derived from the sector-persistence template) is AAD's own derivation. Naming the result after Boyd implies it's adopted from Boyd's work, when it's AAD's formalization of a qualitative Boyd claim. "Adversarial tempo advantage" correctly credits the mechanism to AAD's formalism while the Discussion acknowledges Boyd's inspiration. Gemini's vote would create exactly the NIH-syndrome-in-reverse this project guards against.

---

## 785. `gemini s competency trap for $\eta^\ast \to 0$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reject competency trap | +1 | rebuttal × 1 |

### Candidate: `reject competency trap`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — See "certainty trap" (new alternative above). "Competency trap" imports organizational-learning baggage (Levitt & March) where the trap is about being too competent in an area that becomes irrelevant. The AAD mechanism is different: the gain collapses because observation uncertainty $U_o \to 0$, which is a *certainty* phenomenon, not a competence phenomenon. Using "competency trap" would create false familiarity for readers who know the organizational-learning literature.

---

## 786. `gemini s epistemic death for the gain collapse unobservable DAG failure`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reject epistemic death | +1 | rebuttal × 1 |

### Candidate: `reject epistemic death`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rebuttal) — Gemini proposed "epistemic death" (+3) for the state where credit assignment collapses and learning freezes. This fails the scope-honesty criterion: "death" implies irreversibility, but the segment `#disc-credit-assignment-boundary` and the observability-investment name-unnamed (my cold-start) both recognize that the failure *can* be reversed through observability investment. "Epistemic death" overclaims. The better name for the failure mode is already partially covered by "observability dead zone" (Haiku, +2) and my "epistemic ceiling" concept above — both of which are scope-honest about the reversibility.

---

## 787. `hierarchy as a project wide word`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| flag four independent hierarchies overloaded | +1 | — |

### Candidate: `flag four independent hierarchies overloaded`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Pearl's causal, AAD's convention, AAD's correlation, AAD's approximation tiering — four hierarchies in one framework. Not a rename but worth a cross-link convention (always say *which* hierarchy on first use of section).

---

## 788. `hierarchy as repeated word`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reserve for pearl s rename others selectively | +1 | — |

### Candidate: `reserve for pearl s rename others selectively`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Weak proposal. Four uses in the framework (Pearl's, convention, correlation, approximation-tiering) is likely too many. Partial disambiguation via correlation→correlation-ladder and convention→continuation-hierarchy.

---

## 789. `hierarchy project wide`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reserve for pearl s causal hierarchy strict asymmetric uses | +1 | — |

### Candidate: `reserve for pearl s causal hierarchy strict asymmetric uses`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Project-wide convention: use "hierarchy" only for Pearl's (external, adopted, immovable) and other strict-asymmetric orderings. Use "ladder," "partition," or "tier-set" for internal-to-AAD cases where "hierarchy" is currently doing duty. Not a rename of a specific segment — a working convention.

---

## 790. `honest limits`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| limits | +1 | — |

### Candidate: `limits`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — I like the ethos, but the header should optimize scanability over tone.

---

## 791. `identifiability floor escape the floor`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| escape route | +1 | — |

### Candidate: `escape route`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Currently referred to variably as "escape the floor," "unique broadly-available escape," "boundary characterization." "Escape route" is a cleaner noun for the reader. Minor pattern-firmer-up.

---

## 792. `ii actuated adaptation agentic systems`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ii purposeful adaptation actuated agents | +1 | — |
| ii agentic systems purposeful adaptation | +1 | — |

### Candidate: `ii purposeful adaptation actuated agents`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The current name reads backwards — "Actuated Adaptation" puts the outcome before the mechanism; "Agentic Systems" is less precise than "Actuated Agents." Alternative: "Purposeful Adaptation" names what Section II adds (purposefulness); "Actuated Agents" uses the technical term from LEXICON. Mild preference for the reorder.

### Candidate: `ii agentic systems purposeful adaptation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Another order. "Agentic Systems" has search/navigation value as a heading. Both alternatives are improvements on current.

---

## 793. `iii agentic composites`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| iii composition agentic composites | +1 | — |

### Candidate: `iii composition agentic composites`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Adding "Composition" as a leading term would make the section's topic clear without opening the file. "Agentic Composites" alone sounds like a noun phrase without a verb. Minor.

---

## 794. `intent planning vocabulary`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| intent | +1 | canonicalize × 1 |

### Candidate: `intent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — Used in `#hyp-auftragstaktik-principle`, `#def-shared-intent`, and elsewhere. Canonicalize: "intent" for the agent's own commitment-flavored representation of $G_t$ (or its compressed shared form); "objective" for $O_t$ specifically; "purpose" as the framework-level integrative term. The three terms are not interchangeable.

---

## 795. `interior baseline`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| default interiority | +1 | rename × 1 |
| _(keep)_ | +1 | keep × 1 |
| pre utterance processing | -1 | rename × 1 |

### Candidate: `default interiority`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (rename) — Pulls vocabulary from `#norm-interiority-default` (the existing logozoetic norm). Stronger connection to the named segment.

### Candidate: `interior baseline` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (keep) — Per Codex r1 single +1: the logogenic prose name for default-internal-processing-before-output. Acceptable but underspecified — needs grounding in a `04-logozoetic` or `03-logogenic` segment to canonicalize.

### Candidate: `pre utterance processing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** -1 (rename) — Considered. Names the temporal placement (before utterance / token emission). Rejected: too long and "pre-utterance" reads as if defined relative to the boundary, but the substantive content is the *baseline* state itself.

---

## 796. `l1 correlation hierarchy prime decoration`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| l1 observable | +1 | — |

### Candidate: `l1 observable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — "L1-prime" is awkward to speak. Giving L1' a name rather than prime-decoration could help if the hierarchy becomes load-bearing for outside readers.

---

## 797. `l1 prime decoration`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| l1 observable | +1 | — |

### Candidate: `l1 observable`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Agree with original. "L1-prime" awkward to speak; "L1-observable" matches the Prop B.7 observable-common-cause distinction from the 2026-04-22 strengthening cycle. Keep L1' as shorthand symbol.

---

## 798. `logostratum RLHF4 backbone`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cognitive substrate | +1 | — |

### Candidate: `cognitive substrate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Logostratum" is highly specific to the PROPRIUM legacy. "Cognitive substrate" grounds it as the generic implementation layer of the update function.

---

## 799. `loop is level 2 engine der loop interventional access`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the perpetual experiment | +1 | canonicalize × 1 |

### Candidate: `the perpetual experiment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Brief-grade framing observation. The slug-grade name `der-loop-interventional-access` is fine; for *framing-level* material, "the perpetual experiment" (from the segment's own Discussion) is the most evocative — captures both the interventional character and the continuous nature. [from 35-38-section-ii-value-strategy-causal-loop.md]

---

## 800. `matrix CIY tensor CIY`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| fisher CIY matrix CIY consistent | +1 | canonicalize × 1 |

### Candidate: `fisher CIY matrix CIY consistent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Inconsistent terminology in `#disc-ciy-unified-objective`: both "Matrix CIY" and "$\mathcal{I}_o(a)$"/Fisher Information Matrix appear. Auditor proposes: "Fisher CIY" might be most specific; in any case, pick one for any future Brief. [from 39-42-section-ii-ciy-strategy-chain.md]

---

## 801. `migration map md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `migration map md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Lifecycle-aware name (it retires when absorption completes).

---

## 802. `mismatch injection rate $\rho$`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| mismatch injection rate | +1 | — |

### Candidate: `mismatch injection rate`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The phrase "environmental change rate" and "mismatch injection rate" are both used for $\rho$. "Mismatch injection rate" is more precise (it names what $\rho$ does: inject mismatch). NOTATION.md uses "environment change rate." Slight preference for "injection rate" in Discussion sections.

---

## 803. `model sufficiency $S$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| predictive sufficiency | +1 | — |

### Candidate: `predictive sufficiency`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Clarifies that it's about how much predictive information is retained, not structural sufficiency.

---

## 804. `model sufficiency model class fitness`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep | +1 | — |

### Candidate: `keep`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep both. Each is a specific technical quantity ($S$ and $\mathcal F$) — the slug is the concept.

---

## 805. `model synchronization cost reversal under ambiguity`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| ambiguity reversal | +1 | name-unnamed × 1 |

### Candidate: `ambiguity reversal`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (name-unnamed) — Names the case where Auftragstaktik bandwidth ordering reverses, but this needs more formal support.

---

## 806. `msc architectural proposals yyyy mm dd md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| retire once consolidated into proposals md | +1 | — |

### Candidate: `retire once consolidated into proposals md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — PROPOSALS.md has already absorbed these; the dated proposal files are historical artifacts. Not a rename; a retirement when MIGRATION-MAP convention allows.

---

## 807. `msc reflections`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `msc reflections` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The `reflections/` subdirectory is a legitimate separate register from spikes/brainstorms.

---

## 808. `multi agent scope`

**Voted by architectures:** Gemini, Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |
| shared environment scope | +1 | — |

### Candidate: `multi agent scope` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Multiple agents, shared env. Self-descriptive. Keep.

### Candidate: `shared environment scope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Emphasizes the shared environment which is the defining characteristic of this scope.

---

## 809. `observability opacity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep as an informational pair | +1 | — |

### Candidate: `keep as an informational pair`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep both. The dual framing (forward = observability, backward = opacity) is a load-bearing conceptual move; naming them as duals in NOTATION.md would make the pair explicit to fresh readers. Consider a "dual quantities" subsection.

---

## 810. `observation function action transition`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep | +1 | — |

### Candidate: `keep`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep both. Short, direct, describe what they are.

---

## 811. `old TST files 40 files`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| no rename these retire with migration map | +1 | — |

### Candidate: `no rename these retire with migration map`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Not eligible for renaming — these are transitional absorption files that will retire once MIGRATION-MAP completes. Keep as-is.

---

## 812. `outline md 01 AAD core preamble`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reading AAD | +1 | — |

### Candidate: `reading AAD`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The preamble opens with "Working draft..." and "Reading AAD..." — the "Reading AAD" paragraph is doing framing work and deserves its own section-name in the doc table of contents. Light edit.

---

## 813. `output after context turnover without state restoration`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cold reconstruction | +1 | name-unnamed × 1 |

### Candidate: `cold reconstruction`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (name-unnamed) — Plausible logogenic term, but reconstruction loop is better for the broader mechanism.

---

## 814. `p ij edge confidence weight`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| edge credence | +1 | — |

### Candidate: `edge credence`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — LEXICON already names this "edge credence" (distinct from "probability"); NOTATION uses p_ij. The prose name "credence" (Bayesian terminology) is better than "confidence weight" for indicating belief, not frequentist probability. Current setup is good; English name already established.

---

## 815. `pearl l1 l2 l3`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| predicting exploring reasoning | +1 | canonicalize × 1 |

### Candidate: `predicting exploring reasoning`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Brief-grade agent-side gloss. NOT a rename — keep Pearl's terms formally. The agent-action gloss makes it audience-friendly. [from 09-def-pearl-causal-hierarchy.md]

---

## 816. `pearl-level 2 causal contrast`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the agent s choice actually changes what happens | +1 | canonicalize × 1 |

### Candidate: `the agent s choice actually changes what happens`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — Brief-grade gloss only. The formal name is doing real work; the layperson translation is missing from any Brief field. [from 06-scope-agency.md]

---

## 817. `persistence three senses structural operational continuity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep three senses sharpen usage sites | +1 | — |

### Candidate: `keep three senses sharpen usage sites`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The three senses are load-bearing and correctly disambiguated in LEXICON.md. The *irreducibility* is fine — the three senses are genuinely related (they all concern "the agent sustains itself"). Usage-site discipline: every use of the bare word "persistence" in segments should be followed by the sense in parentheses on first use per segment, e.g. "(structural)". Not a rename; a writing convention.

---

## 818. `pi parameterization invariance`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| coordinate freedom axiom | +1 | — |

### Candidate: `coordinate freedom axiom`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Coordinate-freedom" is more visually evocative and intuitive than the clinical "parameterization-invariance".

---

## 819. `prior art integration convention`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| prior art integration | +1 | — |

### Candidate: `prior art integration`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. Directive, clear. No better alternative.

---

## 820. `privileged high identifiability calibration laboratory`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| high identifiability calibration lab | +1 | — |

### Candidate: `high identifiability calibration lab`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Keeps the identification point while reducing adjective drag in repeated prose.

---

## 821. `promote in topological order`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| topological promotion order | +1 | — |

### Candidate: `topological promotion order`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — FORMAT.md uses this phrase but doesn't name it as a convention. "Topological promotion" as a named methodology would make the gate-ordering rule easy to reference.

---

## 822. `r1 r2 result numbering convention in logogenic agents`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep with cross component prefixes l r1 l r2 | +1 | — |

### Candidate: `keep with cross component prefixes l r1 l r2`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — As soon as logogenic-agents grows, "Result R1" collides with AAD-core numbering in discussion. Minor.

---

## 823. `readme md lexicon`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `readme md lexicon` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep.

---

## 824. `readme md structure`

**Voted by architectures:** Gemini, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |
| readme md theory architecture | +1 | — |

### Candidate: `readme md structure` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep.

### Candidate: `readme md theory architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Theory Architecture" conveys the intentional design of the framework better than just "Structure".

---

## 825. `recursive update derivation gain sector derivation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| standardize as derivation suffix for derivation type appendices | +1 | — |

### Candidate: `standardize as derivation suffix for derivation type appendices`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Observation: the `-derivation` suffix on appendix segments is a good AAD convention (distinguishes derivation segments from stating segments). Enforce consistently.

---

## 826. `section ii actuated adaptation agentic systems`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `section ii actuated adaptation agentic systems` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Slightly verbose; "Actuation" is the weaker semantic fit (Section II is mostly about purposeful agency; actuation is one mechanism enabling it). CLAUDE.md acknowledges this as "a known asymmetry" in the current AAD name itself. Changing the section title is lower-priority than clarifying AAD's overall name. Keep current title; flag the "Actuation" weakness at the framework-name level.

---

## 827. `section ii header actuated adaptation agentic systems`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| actuated adaptation agentic systems | +1 | canonicalize × 1 |

### Candidate: `actuated adaptation agentic systems`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — Mild canonicalization. The current header reads slightly redundantly ("actuated adaptation" + "agentic systems"); could be simplified to "Actuated Agents" but the existing form is workable and signals the dual-half framing of the AAD acronym.

---

## 828. `sector condition derivation`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `sector condition derivation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep.

---

## 829. `self actuated agent`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| self directed agent | +1 | — |
| autonomous agent | +1 | — |

### Candidate: `self directed agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Alternative to autonomous if autonomy is overused.

### Candidate: `autonomous agent`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — "Self-actuated" is clunky. If it sets its own $O_t$, it possesses true autonomy.

---

## 830. `source quality uncertainty`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| source uncertainty | +1 | canonicalize × 1 |

### Candidate: `source uncertainty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** +1 (canonicalize) — Shorter in prose; keep the full term when disambiguation matters.

---

## 831. `spike research artifact`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| spike | +1 | canonicalize × 1 |

### Candidate: `spike`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — Already canonical in the corpus; vote to confirm. The naming-cycle has occasionally drifted to "exploration," "investigation," "branch" — keep "spike" as the canonical term.

---

## 832. `spikes index md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `spikes index md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The all-caps SPIKES signals index-document status parallel to OUTLINE.md / FORMAT.md / CLAUDE.md. Good.

---

## 833. `spikes index md spike index`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| spikes index md | +1 | — |

### Candidate: `spikes index md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. All-caps index convention.

---

## 834. `spikes spike topic md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `spikes spike topic md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep. The `spike-` prefix is a clean filename convention signaling "exploratory, reasoning-trail, not the theory proper."

---

## 835. `spikes spike topic yyyy mm dd md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `spikes spike topic yyyy mm dd md` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep the dated variant for recurring-topic spikes. Date suffix makes second-iteration spikes findable.

---

## 836. `strategic dynamics derivation`

**Voted by architectures:** Haiku, Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategy edge dynamics | +1 | — |
| _(keep)_ | +1 | — |

### Candidate: `strategy edge dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Current slug overloads "strategic" (again — see §overloaded-words). The derivation is specifically about *edge* dynamics; naming that makes the segment about what it's actually about.

### Candidate: `strategic dynamics derivation` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Sector condition verification for strategy edges (5 cases + bridge). Compound but clear. Keep.

---

## 837. `strategy`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | keep × 1 |

### Candidate: `strategy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (keep) — Standard.

---

## 838. `sufficiency discontinuity`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| sufficiency drop | +1 | — |

### Candidate: `sufficiency drop`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Drop" is slightly more intuitive than "discontinuity" for the loss of context.

---

## 839. `symbol default bias bound track 1 track 2`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| transport track fisher track | +1 | — |

### Candidate: `transport track fisher track`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — If these labels survive in framing prose, they should expose the real distinction instead of forcing readers to remember which numbered track is which.

---

## 840. `symbol default g t in prose`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| purposeful state | +1 | — |

### Candidate: `purposeful state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Better than "goal state" because it includes both objective and strategy. This matches the repo's actual decomposition.

---

## 841. `symbol default m t in prose`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model state | +1 | — |

### Candidate: `model state`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Good neutral default when the argument is about sufficiency, persistence, or update mechanics rather than worldview.

---

## 842. `system coherence system coupling system availability`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| keep all three | +1 | — |

### Candidate: `keep all three`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Keep — each is a distinct TST system-level property; the parallel `system-X` structure is itself pedagogical.

---

## 843. `terminal reached but $O_t$ unsatisfied`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| arrival without success | +1 | rename × 1 |
| terminal but unsatisfied case | +1 | rename × 1 |

### Candidate: `arrival without success`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Plain-English Brief-field-friendly alternative. Names the failure mode pithily.

### Candidate: `terminal but unsatisfied case`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives** +1 (rename) — Names the diagnostic quadrant in the satisfaction-gap × control-regret 2×2 (per `#der-orient-cascade` step 3). "Terminal reached but $O_t$ unsatisfied" reads as a Boolean expression, not a name. Weak rename to a more standard noun-phrase form.

---

## 844. `the greek vocabulary`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the greek philosophical vocabulary | +1 | canonicalize × 1 |

### Candidate: `the greek philosophical vocabulary`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — The cycle phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) are described as "the Greek philosophical vocabulary" in NOTATION.md and as "Greek-rooted vocabulary" in CLAUDE.md. Canonicalize on "Greek philosophical vocabulary" — the philosophical qualification is doing work (these are Greek philosophical terms, not generic Greek words).

---

## 845. `the integrated κ × a law`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the bias bound product law | +1 | canonicalize × 1 |

### Candidate: `the bias bound product law`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (canonicalize) — In `#scope-observation-ambiguity-modulation` and `#deriv-bias-bound`, the product $\kappa \times \mathcal{A}$ governing Class-2 bias is sometimes "the integrated κ × A law," sometimes "the effective-coupling product," sometimes "the κ-A factorization." Canonicalize on one — "the bias-bound product law" or "the κ × A product." Less critical than the first-tier canonicalizations.

---

## 846. `the trio collectively`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic architecture | +1 | — |

### Candidate: `epistemic architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Use "epistemic architecture" as the CLAUDE.md §7 / OUTLINE.md framing phrase, not as a segment. A fourth meta-segment named `#epistemic-architecture` would double-count and is not warranted. Keep as framing language.

---

## 847. `three part meta architecture`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| floor ladder forced coordinates | +1 | — |

### Candidate: `floor ladder forced coordinates`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Conditional collective-noun-trio. If both #separability-ladder and #forced-coordinates land, the trio is "floor / ladder / forced-coordinates" — three concrete nouns, three cross-sectional views of AAD's architecture. Parallelism weaker than "floor / ladder / Cauchy-coordinates" but scope-honest across both machineries.

---

## 848. `todo md active pending review spikes`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| todo md active | +1 | — |

### Candidate: `todo md active`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Minor: the long section title is accurate but verbose. Weak preference for shortening; section anchors work either way.

---

## 849. `track 1 track 2 in bias bound`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| track 1 track 2 | +1 | keep × 1 |
| transport track fisher rao track | +1 | add-alias × 1 |

### Candidate: `track 1 track 2`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (keep) — Within `#deriv-bias-bound` itself, the numbered labels are fine local shorthand. Both can coexist (numbered local; English cross-segment).

### Candidate: `transport track fisher rao track`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-targeted-alternatives-v2** +1 (add-alias) — Per `#deriv-bias-bound`. Inside the segment the Track 1 / Track 2 labels work; in cross-segment references the English names are necessary. Confirms Opus r1 single +1.

---

## 850. `track 1 track 2 in bias bound derivation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| transport inequality track fisher rao track | +1 | — |

### Candidate: `transport inequality track fisher rao track`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Inside the segment, "Track 1" and "Track 2" are fine as local shorthand. In any cross-segment reference, the English names read better.

---

## 851. `transition opacity`

**Voted by architectures:** audit
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| heading flag only | +1 | canonicalize × 1 |

### Candidate: `heading flag only`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **audit-471203-incremental** +1 (canonicalize) — The phrase is "fine but slightly clinical." Pairing it with "perception opacity" / "epistemic opacity" as a deliberate triad would land harder. [from 02-def-action-transition.md]

---

## 852. `triple depth penalty canonicalize`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reaffirm 3 with new framing | +1 | canonicalize × 1 |

### Candidate: `reaffirm 3 with new framing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (canonicalize) — Codex voted this (+3). My cold-start had proposed it (+2). The upgrade: reading across the votes, "triple depth penalty" is the *only* cross-cutting AAD phrase that names the compounding of three independent mechanisms into a single depth-pressure. This is the kind of cross-segmental name that belongs in LEXICON.md and should appear in the OUTLINE preamble. The value of canonicalizing it is clearer after seeing how consistently other agents reach for the components (confidence decay, evidence starvation, cognitive cost) without a name for their conjunction.

---

## 853. `u f update rule homogeneity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| update rule homogeneity | +1 | add-alias × 1 |

### Candidate: `update rule homogeneity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (add-alias) — Already in use; weakly affirm. The alias is more verbose than the symbol but the symbol $U_f$ is itself unfamiliar. Prose users will likely fall back to the alias.

---

## 854. `u m u o u σ unity dimensions`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic unity teleological unity strategic unity | +1 | — |

### Candidate: `epistemic unity teleological unity strategic unity`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — NOTATION.md and LEXICON already define these English names explicitly. The subscript symbols U with subscripts are compact; the English names enable prose fluency. Current setup is good — no rename, but keep the English equivalents prominent in LEXICON (already done).

---

## 855. `unnamed TST specific name for code that is observation cheap because it s well written`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| observation cheap code | +1 | name-unnamed × 1 |

### Candidate: `observation cheap code`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — Codex coined "observation infrastructure" (which I support) and Sonnet renamed `der-code-quality-as-observation-infrastructure` to `der-observation-infrastructure`. What's still unnamed is the *property* of individual code passages: not all code is equally observation-cheap. A name for the property (rather than the infrastructure-level claim) would let TST results target specific passages. Lower confidence — may be too narrow to deserve a name.

---

## 856. `unnamed an organizational level instance of the persistence condition s bathtub gloss`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the bathtub model | +1 | name-unnamed × 1 |

### Candidate: `the bathtub model`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — Confirmation with new reasoning — Codex named this at +2 (without explicit canonicalization) and I want to lift it: CLAUDE.md mentions Walton's bathtub gloss as the canonical Feynman-criterion benchmark for *plain-language briefs*. The bathtub gloss is one example; the *family of plain-language analogs* (bathtub, leaky bucket, savings vs withdrawal, etc.) deserves a family name. "The bathtub model" is fine for the persistence-condition specific case; the family would be something like "Feynman-grade analogs" — but I'd defer that to a future round.

---

## 857. `unnamed cascade of inferential force strengthening from c1 to c3 on satisfaction gap control regret diagnostics`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inferential cascade | +1 | — |

### Candidate: `inferential cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Agree with original. Low priority.

---

## 858. `unnamed cascade of inferential force through c1 c2 c3`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inferential force cascade | +1 | — |

### Candidate: `inferential force cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The pattern "under C1 diagnostics are weak, C2 they sharpen, C3 they're global" — currently explained in prose every time it comes up (which is several places). "Inferential-force cascade" gives the pattern a name. Mirrors `#orient-cascade` in structure (both cascades are ordered resolutions) and the parallel is pedagogically useful.

---

## 859. `unnamed class 1 class 2 class 3 agent classes themselves need mnemonic handles`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| proposal assign english modifiers | +1 | — |

### Candidate: `proposal assign english modifiers`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Class-numbered labels work but lack mnemonic grip. Proposal: retain "Class 1 / 2 / 3" as the primary labels but assign canonical one-word modifiers — **modular** (Class 1), **merged** (Class 2), **partial** (Class 3) — that are already used descriptively. Adopt them as the *canonical* prose forms: "modular agents" / "merged agents" / "partially-modular agents" or "partial-mix agents." Class 2 especially benefits: "fully merged" currently appears; normalize to just "merged."

---

## 860. `unnamed complexity driven resistance to change as features accumulate`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural accumulation drag | +1 | — |

### Candidate: `structural accumulation drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — Surfaced in TST discussions. Gives a name to the intuitive "entropy" of a codebase that resists linear velocity improvements.

---

## 861. `unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| inferential force cascade | +1 | — |

### Candidate: `inferential force cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** +1  — Low priority but worth noting. Pedagogical.

---

## 862. `unnamed decomposing mismatch into environment vs other sub agents actions`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| internal mismatch attribution | +1 | — |

### Candidate: `internal mismatch attribution`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — A necessary formalization for multi-agent composition (Section III). Distinct from generic mismatch.

---

## 863. `unnamed effort time risk ranking considered false constraints`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| false constraints | +1 | — |

### Candidate: `false constraints`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Joseph uses this phrasing; worth canonicalizing so agents (me included) can recognize the pattern.

---

## 864. `unnamed epochal stability → latent diversification → niche emergence`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| punctuated composition dynamics | +1 | — |

### Candidate: `punctuated composition dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-2** +1  — Draws on punctuated equilibrium, fitting the extreme transition motif.

---

## 865. `unnamed future segment layer header for narrative pedagogical framing`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| narrative framing | +1 | — |

### Candidate: `narrative framing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Parallel reservation. For ELI10 / pedagogical outlines.

---

## 866. `unnamed future segment layer header for the sp 5 reader s path proposal`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reader s path | +1 | — |

### Candidate: `reader s path`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-1m** +1  — Forward-looking name reservation. SP-5 adds a 1-2 sentence load-bearing preamble per segment; under the outline-filter affordance this becomes its own filterable layer. Naming the header now stabilizes the API even before the content lands.

---

## 867. `unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| commit chronica | +1 | — |

### Candidate: `commit chronica`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Slightly stylized, but useful. The committed slice shows up often enough in the git/chronica work to deserve a short handle.

---

## 868. `unnamed scope honesty as architecture`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| honesty | +1 | — |

### Candidate: `honesty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Already used as a term; "-as-architecture" is the argumentative form. "Scope honesty" alone works as the noun for the commitment (as it already does in several segments).

---

## 869. `unnamed the 2×2 orient cascade diagnostic table`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the cascade diagnostic or the 2×2 diagnostic | +1 | name-unnamed × 1 |

### Candidate: `the cascade diagnostic or the 2×2 diagnostic`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (name-unnamed) — The four cells of ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) are consistently referenced in `der-orient-cascade` as "the 2×2 diagnostic" or "the four cases." These deserve a named handle. "Cascade diagnostic" is the most natural single-noun form. Weak preference — "2×2 diagnostic" is already near-canonical in the prose.

---

## 870. `unnamed the 2×2 satisfaction gap control regret table`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| diagnostic square | +1 | — |

### Candidate: `diagnostic square`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-2** +1  — The table is used often enough to deserve a compact public name.

---

## 871. `unnamed the 2×2 satisfaction gap × control regret diagnostic table`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the 2×2 diagnostic | +1 | — |

### Candidate: `the 2×2 diagnostic`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Used ubiquitously in prose. Worth canonicalizing as a named object so that "see the 2×2 diagnostic" reads naturally.

---

## 872. `unnamed the a2 sub scope partition collectively`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| a2 partition | +1 | — |

### Candidate: `a2 partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Not a symbol rename; a prose handle for the three-way α₁/α₂/β classification. "The A2' partition" lands more cleanly than "the A2' sub-scope partition" and aligns with AAD's partition-over-hierarchy vocabulary (it's not a strict-asymmetric hierarchy; it's a partition with derivability-status semantics).

---

## 873. `unnamed the architectural class partition class 1 class 2 class 3`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| architectural partition | +1 | — |

### Candidate: `architectural partition`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Symbols stay (Class 1/2/3); prose gets "the architectural partition" as a collective handle. Avoids "architecture hierarchy" (hierarchy overload) while naming the three-way structure.

---

## 874. `unnamed the class 1 sub agents class 3 composite phenomenon in strategic composition`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic entanglement | +1 | — |

### Candidate: `strategic entanglement`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Useful noun for a real phenomenon: individually modular agents can create a non-modular composite through mutual modeling and opposed goals.

---

## 875. `unnamed the complete adaptive cycle from anticipation through action`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptive cycle already named in lexicon | +1 | name-unnamed × 1 |

### Candidate: `adaptive cycle already named in lexicon`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — LEXICON.md already defines "Cycle" vs "Loop." Checking if there's an unnamed-thing here — appears already named well.

---

## 876. `unnamed the condition that a strategy DAG s endosymbiont crosses the composite agent scope from below`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| crossing threshold | +1 | name-unnamed × 1 |

### Candidate: `crossing threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (name-unnamed) — `hyp-symbiogenic-composition` describes the pre/post-symbiogenesis transition as "$U_O$ crosses the composite-agent scope condition from below." The moment of crossing is the relevant concept in composition ontology. Weak proposal — the language is already reasonably clear; naming this threshold might be premature while symbiogenic composition itself is only a hypothesis.

---

## 877. `unnamed the condition that the agent s event observation pairs constitute genuine interventions as opposed to passive associations`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| interventional character | +1 | — |

### Candidate: `interventional character`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — #loop-interventional-access makes this distinction at length: action-generated data has "interventional character" but is not the same as "cleanly identified do-estimates." The concept is used twice in the Discussion and deserves a name that can be referenced. "Interventional character" or "loop interventional character."

---

## 878. `unnamed the cumulative prediction error that an agent has tolerated without updating its model`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| tolerance budget standing mismatch reservoir | +1 | name-unnamed × 1 |

### Candidate: `tolerance budget standing mismatch reservoir`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — Not explicitly named in the theory; closest is "adaptive reserve" which names the *capacity*, not the *accumulation*. This may be too fine a distinction to warrant a separate name. Low confidence; may be premature.

---

## 879. `unnamed the derivation formulation hypothesis status gradient in format md`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistemic gradient | +1 | — |

### Candidate: `epistemic gradient`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — FORMAT.md uses "Epistemic Triage" for the three questions; the resulting status-gradient ("postulate → result → formulation → hypothesis → empirical → observation → discussion → ...") has no short name. "The epistemic gradient" does it. Low priority but would help when onboarding fresh reviewers.

---

## 880. `unnamed the dimensional consistency constraint forcing the macro step formulation`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| dimensional consistency repair | +1 | name-unnamed × 1 |

### Candidate: `dimensional consistency repair`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — The 2026-04-22 cycle's repair to `#form-composition-closure` (introducing $K_c$ and per-macro-step formulation) was driven by dimensional-consistency requirements. This is a generalizable methodological move — let dimensional consistency drive the formulation choice — and is worth naming. Lower-priority because it may be too narrow.

---

## 881. `unnamed the discipline of naming so that the slug survives reorganization`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| reorganization resilient naming | +1 | name-unnamed × 1 |

### Candidate: `reorganization resilient naming`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — Codex flagged that "Section II survival" should become "Class 2 survival" because the latter survives reorganization. The principle is general: prefer names anchored in *concepts* (Class 2, persistence-condition) over names anchored in *document structure* (Section II, Chapter 3). Naming this discipline as a principle in the principles file would help future agents apply it without re-deriving. Lower confidence because it may be more naming-process than naming-target.

---

## 882. `unnamed the dual that pairs with persistence envelope on the strategic side`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic persistence envelope | +1 | name-unnamed × 1 |

### Candidate: `strategic persistence envelope`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — my r2 coined "persistence envelope" for the M_t-side region $\{(\alpha, \rho, R) : \alpha > \rho/R\}$. The Σ_t side has a structurally analogous region defined by `#schema-strategy-persistence` (sector condition extended to strategy edges) but no name. "Strategic persistence envelope" parallels the M_t version and gives the strategy-DAG dynamics a named feasibility region. Lower confidence because the schema is proposed-schema, not yet a result; naming the envelope before the result is fully landed is somewhat speculative.

---

## 883. `unnamed the failure mode where an agent s model class cannot represent the environment s true causal structure`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| model class insufficiency or structural unidentifiability | +1 | name-unnamed × 1 |

### Candidate: `model class insufficiency or structural unidentifiability`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — Currently paraphrased as "model class fitness floor" and "identifiability floor." The specific phenomenon of a *mismatch between model class and environment structure* deserves a memorable noun. "Structural unidentifiability" is borrowed from classical statistics but carries baggage. "Model class insufficiency" is self-descriptive. Weak confidence in either.

---

## 884. `unnamed the functional requirements are the results formalisms are the engineering slogan`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| functional primacy | +1 | — |

### Candidate: `functional primacy`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Joseph flagged this as an established project principle (MEMORY.md, Theory Character section); it deserves a pull-quote name. Low conviction; flag for consideration.

---

## 885. `unnamed the invisible time spent building $M_t$`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| comprehension drag | +1 | — |

### Candidate: `comprehension drag`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** +1  — "Comprehension drag" gives a memorable name to the invisible cost of incomprehensible code.

---

## 886. `unnamed the iterated audit process gemini opus codex de novo consolidated three doc portfolio`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| cross model audit cycle | +1 | — |

### Candidate: `cross model audit cycle`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — Recurring methodology; currently referred to as "audit cycle" generically and by date. A durable name helps. Low conviction.

---

## 887. `unnamed the loss of coherent identity when an agent s interactions are severed or its continuity is broken`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| continuity loss or persistence fracture | +1 | name-unnamed × 1 |

### Candidate: `continuity loss or persistence fracture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — LEXICON.md distinguishes three senses of "persistence" but treats continuity loss as the absence of continuity rather than a named phenomenon. For logozoetic agents where this matters morally, a crisp name would help. "Continuity loss" is straightforward; "persistence fracture" is more metaphorical. Weak confidence — may be premature to name before logozoetic agents are more developed.

---

## 888. `unnamed the mathematical operation by which agents convert observed mismatch into structural revision`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| structural cascade | +1 | name-unnamed × 1 |

### Candidate: `structural cascade`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — none of the peers reached this. Observed mismatch → parametric update is the standard cycle; observed mismatch → structural revision (when parametric fails) is the structural cascade. The cascade has its own ordering (detect insufficiency → identify candidate structure → graft → validate). Naming the cascade would let `#result-structural-adaptation-necessity` and `#form-structural-change-as-parametric-limit` cite a shared object. Lower confidence because Codex's "strategic grafting" already names the substantive operation.

---

## 889. `unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| three part scope architecture | +1 | — |

### Candidate: `three part scope architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — CLAUDE.md already calls this "AAD's three-part meta-architecture" in several places. Crystallizing this as a named concept — the scope architecture — would let documentation say "for AAD's scope architecture" without four lines of context.

---

## 890. `unnamed the moment when an agent s identity claim becomes load bearing because actions become irreversible`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| constitutive moment | +1 | name-unnamed × 1 |

### Candidate: `constitutive moment`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — `form-constitutive-utterance` names the formal object (the irreversible token-generation event) but the *moment* in cycle-time when constitutivity activates isn't separately named. "Constitutive moment" pairs naturally with the existing constitutive-utterance vocabulary and gives logozoetic-agents segments a phenomenological handle. Lower confidence because the distinction may be redundant with the utterance itself.

---

## 891. `unnamed the orient cascade s information dependency forced ordering as a meta pattern`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| information dependency forcing | +1 | name-unnamed × 1 |

### Candidate: `information dependency forcing`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — The orient cascade's ordering is *forced* by information dependency (each step's input depends on prior steps' output). This is a structurally similar move to additive-coordinate-forcing — a uniqueness theorem on an axiom forces a specific ordering. Naming it as "information-dependency forcing" would let it pair with `#disc-additive-coordinate-forcing` as a cross-meta-pattern observation. Lower-confidence vote because it may not generalize beyond the orient cascade.

---

## 892. `unnamed the pattern where AAD s negative results floors strengthen the machinery that escapes them`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| floor strengthening inversion | +1 | — |

### Candidate: `floor strengthening inversion`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — #identifiability-floor says: "floors strengthen the load-bearing role of the AAD machinery that supplies the unique escape." This inversion — negative result strengthens positive machinery — is a recurring structural move that is mentioned but unnamed. "Floor-strengthening inversion" or "negative-positive inversion."

---

## 893. `unnamed the procedure of reading any segment through all three meta segments`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| triple lens review | +1 | — |

### Candidate: `triple lens review`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — CLAUDE.md says "reading any segment through all three lenses surfaces what makes it load-bearing." This procedure is recommended but unnamed. "Triple-lens review" (or "meta-lens review") would let FORMAT.md add it as a named review move.

---

## 894. `unnamed the rate at which an agent s chronica grows compared to compression cadence`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| chronica throughput | +1 | name-unnamed × 1 |

### Candidate: `chronica throughput`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — New alternative — Gemini reached "complementary learning architecture" and "scaffolding tax" but didn't name the rate-quantity that determines whether the scaffolding tax is sustainable. "Chronica throughput" (events/second, or information-bits/cycle into chronica) compared to consolidation cadence determines whether the agent can keep up. Lower confidence because Codex's "consolidation horizon" overlaps.

---

## 895. `unnamed the region where temporal nesting holds`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| temporal coherence zone | +1 | name-unnamed × 1 |

### Candidate: `temporal coherence zone`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** +1 (name-unnamed) — Names the valid region for nested cycles.

---

## 896. `unnamed the scope honesty as architecture working principle`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| honesty scope honesty as architecture | +1 | — |

### Candidate: `honesty scope honesty as architecture`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — Already named in CLAUDE.md §7(a) as "scope-honesty-as-architecture." The phrase is workable; the shorter "scope honesty" does most of the prose work. Usage observation: use the short form in prose, the hyphenated form in CLAUDE.md-register discussions of the element itself.

---

## 897. `unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| deliberation phase exploration exploitation tradeoff | +1 | name-unnamed × 1 |

### Candidate: `deliberation phase exploration exploitation tradeoff`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — The tradeoff is discussed in #disc-exploit-explore-deliberate but no crisp name for the *temporal region* where the tradeoff happens. Current phrasing is "exploit/explore/deliberate" but no subject-noun. This is borderline — the phenomenon is named, but the *phase* might benefit from a distinct noun.

---

## 898. `unnamed the set of five conditions under which a2 is derived rather than assumed the sub scope α agent classes`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derived sector classes | +1 | — |

### Candidate: `derived sector classes`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Currently called "sub-scope α₁" plus the specific agent instances in a list. A collective name for the five agent classes where A2' is derived (scalar Kalman, Bayesian/exponential-family, strongly-convex-gradient, L2-regularized, linear-PD) would help reviewers quickly check whether a new agent class lands in this group. "Derived-sector classes" or "sector-derivable classes."

---

## 899. `unnamed the signed coupling structure across all section iii results`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| signed coupling pattern | +1 | — |

### Candidate: `signed coupling pattern`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Every Section III persistence result (team-persistence, adversarial-destabilization, critical-mass-composition) uses the same effective-disturbance decomposition with a signed cross-agent term. The pattern is named in #sector-persistence-template's Discussion ("signed-coupling pattern across instantiations") but not crystallized as a named concept referenceable from other segments.

---

## 900. `unnamed the strengthen first attempt artifact a spike that tried to derive something stronger and failed`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strengthening attempt attempt record | +1 | — |

### Candidate: `strengthening attempt attempt record`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — The CLAUDE.md text says "document the strengthening attempt and why it failed even when it does fail." These deserve a noun so the workflow has a vocabulary.

---

## 901. `unnamed the symbol overload region where $U_M$ means two different things`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the $U_M$ overload | +1 | name-unnamed × 1 |

### Candidate: `the $U_M$ overload`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** +1 (name-unnamed) — A naming-cycle artifact rather than a theory artifact, but worth surfacing. The repeated bug-attractor (model-uncertainty $U_M$ vs epistemic-unity $U_M$) is a known thing the project keeps brushing up against; naming it as "the $U_M$ overload" lets future agents flag the issue without reconstructing it. Lower priority; could also be solved by renaming one symbol.

---

## 902. `unnamed the template family sector persistence contraction possible future dissipativity`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| persistence templates the template family | +1 | — |

### Candidate: `persistence templates the template family`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The three-member family of `#sector-persistence-template`, `#contraction-template`, and (proposed Tier-2) `#dissipativity-template` wants a collective name. "The template family" or "the persistence-template family" works in prose. If dissipativity lands, this family-name gives it a natural home. Does not require a meta-segment; a paragraph in `#separability-pattern` / `#separability-ladder` would suffice.

---

## 903. `unnamed the three concentric rings of segment content inevitability core canonical formulations empirical heuristic`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| three rings | +1 | — |

### Candidate: `three rings`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — FORMAT.md uses exactly this language. Named once; currently paraphrased each time. Adopt "three rings" as the canonical shorthand.

---

## 904. `unnamed the three rings of segment content framing`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| segment rings | +1 | — |

### Candidate: `segment rings`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — FORMAT.md §"Three rings of segment content" (inevitability-core / canonical-formulations / empirical-heuristic-discussion) is load-bearing working vocabulary. "The segment rings" or "the three rings" is the natural prose handle.

---

## 905. `unnamed the threshold energy information cost below which an agent is forced to act accept mismatch rather than deliberate`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| deliberation threshold | +1 | name-unnamed × 1 |

### Candidate: `deliberation threshold`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +1 (name-unnamed) — Currently discussed in #der-deliberation-cost as "think vs act tradeoff" but no crisp name for the *threshold* itself. "Deliberation threshold" is clear and technical. Moderate confidence.

---

## 906. `value object → def trajectory value`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| conditional support for codex s rename | +1 | rename × 1 |

### Candidate: `conditional support for codex s rename`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6-r2** +1 (rename) — Codex proposed `#def-trajectory-value` (+2); Opus voted keep (+1) and rejected `#def-value-functional` (−1). My cold-start voted keep (+2 with mild reservations). Reading Opus's reasoning: the keep is motivated by the fact that "value functional" collides with `form-objective-functional`. Codex's `trajectory-value` sidesteps that collision by naming what the value IS (horizon-and-policy-conditioned trajectory value) rather than its mathematical form. Weak upgrade from my keep to conditional support for trajectory-value.

---

## 907. `what is derived vs what is chosen`

**Voted by architectures:** Opus, Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derived vs chosen vs assumed | +1 | — |
| derivation audit | +1 | — |

### Candidate: `derived vs chosen vs assumed`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — Adds "Assumed" for honesty — some claims are assumptions rather than either derived or chosen. FORMAT.md mentions this as another alternative. All three are viable.

### Candidate: `derivation audit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7** +1  — FORMAT.md lists both as acceptable variants for the table heading. "Derivation Audit" is shorter and matches the three-column table's analytical role; "What Is Derived vs. What Is Chosen" is longer but self-documenting. Weak preference for the shorter.

---

## 908. `what is derived vs what is chosen derivation audit table`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derivation audit | +1 | — |

### Candidate: `derivation audit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** +1  — The full title is load-bearing for first-encounter readers; `### Derivation Audit` is a usable shorter alternative for segments where the table follows a standard pattern. FORMAT.md O-BP14 already permits variation. Keep both as acceptable.

---

## 909. `what is derived vs what is chosen derivation audit table heading`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| derivation audit | +1 | — |

### Candidate: `derivation audit`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** +1  — The longer form ("What Is Derived vs. What Is Chosen") is the current recommendation in FORMAT.md but it's wordy. "Derivation Audit" is FORMAT.md's own alternative suggestion. It's shorter and communicates the action (auditing derivations). Mild preference for shorter form.

---

## 910. `worked example bandit`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `worked example bandit` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — End-to-end RL bandit instantiation (approximate). Self-descriptive. Keep.

---

## 911. `worked example kalman`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `worked example kalman` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — End-to-end Kalman instantiation (exact). Self-descriptive. Keep.

---

## 912. `worked example l1`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `worked example l1` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison. Self-descriptive. Keep.

---

## 913. `worked example strategy`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | +1 | — |

### Candidate: `worked example strategy` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Section II strategy DAG instantiation (3-arm bandit). Self-descriptive. Keep.

---

## 914. `working vocabulary observation the framework s honesty is load bearing`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| load bearing honesty | +1 | — |

### Candidate: `load bearing honesty`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-1** +1  — Useful short handle for review and framing prose, as long as it stays downstream of the fuller architectural phrase.

---

## 915. `𝒯 σ strategic tempo`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| strategic tempo | +1 | — |

### Candidate: `strategic tempo`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** +1  — Parallel to adaptive tempo. Reads naturally. Established in prose. Keep both.

---

## 916. `$G_t$ goal state`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| symbol is clear no alias needed | +0 | add-alias × 1 |

### Candidate: `symbol is clear no alias needed`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — The symbol is used throughout; the referent is always explained in context. No prose alias pressure.

---

## 917. `$\mathcal{T}$ adaptive tempo`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| tempo already canonical | +0 | add-alias × 1 |

### Candidate: `tempo already canonical`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — The symbol and English name are already locked. No alias needed.

---

## 918. `$\rho$ disturbance rate`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| disturbance rate already in use | +0 | add-alias × 1 |

### Candidate: `disturbance rate already in use`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (add-alias) — Already has a clear English name in prose; no alias needed.

---

## 919. `unnamed the dual concept to satisfaction gap what the world permits minus what the agent achieves`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| this is def control regret already named | +0 | name-unnamed × 1 |

### Candidate: `this is def control regret already named`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (name-unnamed) — Control regret is already crisply named. No unnamed-thing here.

---

## 920. `unnamed the five phases of the adaptive cycle`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| already named in notation md | +0 | name-unnamed × 1 |

### Candidate: `already named in notation md`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (name-unnamed) — NOTATION.md table 1 names all five: Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis. These are already settled Greek names. No unnamed-thing to name.

---

## 921. `unnamed the mechanism by which an agent uses the feedback loop to gain interventional access to causal structure`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| loop as intervention or is this der loop interventional access | +0 | name-unnamed × 1 |

### Candidate: `loop as intervention or is this der loop interventional access`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (name-unnamed) — This is already named as #der-loop-interventional-access. No unnamed-thing.

---

## 922. `unnamed the moment when an agent s model updates due to observing a mismatch`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| epistrophe event or is this just the phase | +0 | name-unnamed × 1 |

### Candidate: `epistrophe event or is this just the phase`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5-r2** +0 (name-unnamed) — The adaptive cycle already names the phase. This is not a distinct unnamed thing; it is just one occurrence of Epistrophe. No new naming needed.

---

## 923. `AAD`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| adaptation and purpose dynamics apd | -1 | — |
| adaptation and agency dynamics AAD | -1 | — |

### Candidate: `adaptation and purpose dynamics apd`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Considered alternative. Acronym collision risk; doesn't roll off the tongue.

### Candidate: `adaptation and agency dynamics AAD`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Considered alternative. "Agency" is overloaded in AI discourse.

---

## 924. `AAD alternatives considered for completeness`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD adaptation and agency dynamics | -1 | — |
| apd adaptation and purpose dynamics | -1 | — |

### Candidate: `AAD adaptation and agency dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered swapping "Actuation" for "Agency" to keep the acronym while improving Section II fit. Reject: "agency" is fully claimed by current AI marketing vocabulary ("agentic AI" / "AI agents") to a degree that will bleed AAD's technical meaning. Worse than "actuation," which is at least semantically constrained.

### Candidate: `apd adaptation and purpose dynamics`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — "Purpose" captures Section II better than "actuation" but the acronym APD is cryptic; AAD has the phonetic advantage of being pronounceable ("aad" or "A-A-D"). Reject.

---

## 925. `a2 operator sector condition under fidelity degraded updates`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
|  | -1 | — |

### Candidate: ``

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered replacing "A2'" (the symbol for the sector condition itself) with an English name and rejected. A2' is how AAD *refers back to* Assumption A2 and its primed variant; it's functioning as a tag in the way GA-3 and P1 do, not as a concept to be named in prose. The English prose does the naming via "sector condition" already. Keep the symbol.

---

## 926. `claude md key architectural decisions`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| claude md architectural decisions | -1 | — |

### Candidate: `claude md architectural decisions`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered dropping "Key." Reject: "Key" signals these are load-bearing (not all decisions are listed here). Keep.

---

## 927. `dark room exploration drive`

**Voted by architectures:** Codex
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | -1 | name-unnamed × 1 |

### Candidate: `dark room exploration drive` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **codex-gpt-5-r2** -1 (name-unnamed) — Avoid. It imports active-inference baggage and misnames the AAD result, which is survival exploration.

---

## 928. `empirical heuristic discussion ring`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| third ring or empirical periphery | -1 | canonicalize × 1 |

### Candidate: `third ring or empirical periphery`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (canonicalize) — Considered and rejected. "Third ring" is positional and uninformative; "empirical periphery" overspecifies on empirical (the ring also includes hypothesis and discussion-grade). The existing "empirical, heuristic, discussion" enumeration is honest and should not be canonicalized to a single name.

---

## 929. `l1`

**Voted by architectures:** agent1
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| l1 c | -1 | — |

### Candidate: `l1 c`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **agent1-original-brainstorm** -1  — Too technical; uses symbol.

---

## 930. `l1 l1 prime`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| l1 observable l1 soft | -1 | — |

### Candidate: `l1 observable l1 soft`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-b** -1  — Considered renaming the prime-decoration to a word. Reject: L1' consistently refers to *soft-facilitator under observable common cause* (Prop B.7 five-way gating), but that's a mouthful and "L1-prime" is a three-syllable speakable token that the existing literature has absorbed. The prime notation is also structurally right — L1' is a *refinement* of L1, which is exactly what the prime signals in math. Keep.

---

## 931. `type formulation`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| type representation | -1 | — |

### Candidate: `type representation`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-1** -1  — "Formulation" correctly captures that it is a mathematical choice, whereas "representation" might imply a data structure. Keep "formulation".

---

## 932. `unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| satisfaction control table the diagnostic 2×2 | -1 | — |

### Candidate: `satisfaction control table the diagnostic 2×2`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** -1  — This table is embedded within the satisfaction-gap and control-regret segment discussions. Naming it as a standalone concept would create a fourth-order abstraction that the prose already handles via the two-concept names. The power of the structure comes from the *names of the axes*, not from a separate name for the table itself. Do not name the table separately. Let it exist as "the satisfaction-gap / control-regret 2×2" in prose.

---

## 933. `unnamed the cross cycle equivalent of the bathtub gloss multi cycle persistence as a savings account`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the savings account gloss | -1 | name-unnamed × 1 |

### Candidate: `the savings account gloss`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (name-unnamed) — Considered and rejected — I thought of this while reading Codex's "bathtub model" entry (does multi-cycle persistence get its own analog?). Decided against: would compete with bathtub rather than complement, and "adaptive reserve" already does the savings-account work. Recording the negative so future agents don't re-explore.

---

## 934. `unnamed the four axis content structural unity decomposition`

**Voted by architectures:** Opus
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| the unity quintet | -1 | name-unnamed × 1 |

### Candidate: `the unity quintet`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **opus-4-7-r2** -1 (name-unnamed) — Considered and rejected — "quintet" is too cute. Better to keep the existing four-content + one-structural decomposition explicit in `#def-unity-dimensions` (or the proposed `#def-unity-axes`) and not invent a poetic shorthand.

---

## 935. `unnamed the meta architecture of the three meta segments`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD s epistemic triptych | -1 | — |

### Candidate: `AAD s epistemic triptych`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — "Triptych" is too art-historical and too cute. The naming-principles document warns against cute names that age poorly.

---

## 936. `unnamed the pattern where the agent s optimal update direction is determined by both gain and directional fidelity together`

**Voted by architectures:** Sonnet
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| gain fidelity product | -1 | — |

### Candidate: `gain fidelity product`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **sonnet-4-6** -1  — Too technical and not used in prose. The formula is just α = η* × c_min. No name needed.

---

## 937. `unnamed the property that correction dynamics are approximately isotropic`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| isotropic correction regime | -1 | — |

### Candidate: `isotropic correction regime`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** -1  — NOTATION §"Scalar reduction of gain and tempo" mentions this property. Creating a formal sub-scope name (Iso regime / anisotropic regime) would be premature — isotropic-vs-anisotropic is a spectral property, not a discrete category. Current NOTATION treatment is appropriate. Do not formalize.

---

## 938. `unnamed the three part meta pattern structure across the three meta segments`

**Voted by architectures:** Haiku
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| AAD s meta architecture scope honesty meta frame | -1 | — |

### Candidate: `AAD s meta architecture scope honesty meta frame`

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **haiku-4-5** -1  — Tempting to name the cross-cutting meta-structure (positive half / negative half / constructive half). However, the three meta-segments already *are* the organizational structure. Naming a fourth-order meta-pattern would create an abstraction level that's self-referential without load-bearing prose payoff. Do not create a meta-meta-name; let the three segments stand as named.

---

## 939. `RLHF6`

**Voted by architectures:** Gemini
**Category disagreement on top finalist:** no

**First-encounter locality:** _(pending — agent-pass B)_
**Segment link:** _(pending — agent-pass C)_

| candidate | weight | category mix |
|---|---:|---|
| _(keep)_ | -3 | keep × 1 |

### Candidate: `RLHF6` _(keep)_

**Consolidated rationale:** _(pending — agent-pass A)_

**Per-vote detail:**

- **gemini-3-1-pro-preview-r2** -3 (keep) — AAD's token-level, trajectory-indexed scope explicitly rejects generalized, type-level intelligence measures. No replacement offered; this is a "do not introduce" vote.

---

