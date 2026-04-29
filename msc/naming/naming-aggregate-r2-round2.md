# Naming Vote — Round 2 Input (Blind)

**Round 1 agents:** agent1-original-brainstorm, audit-471203-incremental, codex-1, codex-2, codex-gpt-5-r2, gemini-1, gemini-2, gemini-3-1-pro-preview-r2, gemini-targeted-alternatives, haiku-4-5, haiku-4-5-r2, opus-1m, opus-4-7, opus-4-7-b, opus-4-7-r2, opus-targeted-alternatives, opus-targeted-alternatives-v2, sonnet-4-6, sonnet-4-6-r2

This is the aggregated candidate list from Round 1, sorted most-popular to least-popular (tallies withheld to prevent bandwagon convergence). Each entry shows a current-name, the alternatives proposed across agents (including explicit keeps), and the reasoning notes from Round 1 agents.

**Your task:** review each entry and cast your own votes following `doc/naming-principles.md`. You may add new candidates not on this list if you discover one during review. Do not read other Round-1 vote files directly — this aggregated summary is your input. Write your votes to `msc/naming/naming-votes/{your-agent-id}.md`.

---

## 1. `control regret`

**Alternatives proposed:** `control regret`, `strategy opportunity cost`

_category: keep × 16, canonicalize × 1, rename × 1_

- `control regret` — **agent1-original-brainstorm:** Pairs with satisfaction gap; same reasoning.
- `control regret` — **codex-1:** Crisp, properly scoped, and pairs perfectly with satisfaction gap.
- `control regret` — **codex-2:** Strong adjacent-field baggage used correctly; it pairs beautifully with satisfaction gap.
- `control regret` — **codex-gpt-5-r2:** Strong pair with satisfaction gap. It is familiar enough from regret language and still domain-specific.
- `control regret` — **codex-gpt-5-r2:** This diagnostic should remain paired with satisfaction gap.
- `control regret` — **gemini-1:** Perfect pairing with satisfaction gap.
- `control regret` — **gemini-3-1-pro-preview-r2:** Excellent pairing with satisfaction gap.
- `control regret` — **gemini-targeted-alternatives:** Perfect partner to satisfaction gap. Captures the specific decision-theoretic regret tied to strategy revision.
- `control regret` — **haiku-4-5-r2:** Companion to satisfaction-gap; the pair is load-bearing prose throughout. Both names compress intuition that survives working-memory pressure.
- `control regret` — **haiku-4-5:** Dual to satisfaction gap; "regret" reads naturally as "current vs. best available" gap. The two names do *load-bearing work* for the discipline. Keep.
- `control regret` — **opus-1m:** Pairs with satisfaction gap.
- `control regret` — **opus-4-7-b:** Pairs with *satisfaction gap*. "Regret" imports RL baggage that is genuinely load-bearing (regret = best-achievable − current); "control" narrows it to the attainability layer.
- `control regret` — **opus-4-7-r2:** Same load-bearing keep as `#def-satisfaction-gap`. The pair is the canonical illustration of "names that do work for the reader" in the principles file; do not rename either half.
- `control regret` — **opus-4-7:** Pair-partner to satisfaction gap. The pair carries its decomposition load. Keep.
- `control regret` — **sonnet-4-6-r2:** Same reasoning as satisfaction-gap — these two names work as a pair and are load-bearing for the 2×2 orient cascade diagnostic.
- `control regret` — **sonnet-4-6-r2:** Occasionally "strategy regret" or "execution regret" appears in working notes. The name "control regret" is established in NOTATION.md and LEXICON.md. Standardize.
- `control regret` — **sonnet-4-6:** See above. The 2×2 disambiguation table works because both names work. Keep.
- `strategy opportunity cost` — **gemini-targeted-alternatives:** A bit too generic economics terminology; "regret" explicitly ties to the mathematical formulation.

## 2. `satisfaction gap`

**Alternatives proposed:** `satisfaction gap`, `attainability shortfall`

_category: keep × 16, canonicalize × 1, rename × 1_

- `satisfaction gap` — **agent1-original-brainstorm:** Crispest named pair in the project. 2×2 diagnostic table is memorable *because* the names are memorable. Do not touch.
- `satisfaction gap` — **codex-1:** One of the cleanest names in the repo. The phrase explains the diagnostic almost by itself.
- `satisfaction gap` — **codex-2:** One of the crispest names in the whole project; it is immediately intelligible without losing technical meaning.
- `satisfaction gap` — **codex-gpt-5-r2:** Excellent diagnostic name for terminal conditions met while the objective remains unsatisfied.
- `satisfaction gap` — **codex-gpt-5-r2:** This diagnostic should remain stable.
- `satisfaction gap` — **gemini-1:** The 2x2 diagnostic with Control regret is perfect. Do not touch.
- `satisfaction gap` — **gemini-3-1-pro-preview-r2:** Crispest named pair in the project (with control regret). The disambiguation table is load-bearing.
- `satisfaction gap` — **gemini-targeted-alternatives:** Crispest named pair along with control regret. Essential diagnostic dimension.
- `satisfaction gap` — **haiku-4-5-r2:** Crispest named diagnostic pair in the project (paired with #def-control-regret); the 2×2 table organizes in readers' heads because the names do the work. High-weight keep against rename impulse.
- `satisfaction gap` — **haiku-4-5:** Crispest named diagnostic pair in the project. The 2×2 disambiguation table (satisfaction-gap vs. control-regret axis; goal-attainability vs. strategy-quality) crystallizes in reader's mind because the axes are evocatively named. Do not touch.
- `satisfaction gap` — **opus-1m:** Crispest pair in the project. The 2×2 disambiguation table organizes itself in the reader's head because of the naming. Do not touch.
- `satisfaction gap` — **opus-4-7-b:** The 2×2 diagnostic composes with *control regret* into a cognitive apparatus the reader assembles in one exposure. Do not touch either half. The axes are *evocatively and accurately* named — a rare pairing.
- `satisfaction gap` — **opus-4-7-r2:** Defended keep — and one of the cleanest names in the framework. The 2×2 disambiguation table works because "satisfaction gap" and "control regret" are *both* memorable on first encounter and *orthogonal* in a way the name signals. Renaming would lose a load-bearing prose convention. The Feynman-criterion test passes: an outside reader reading "satisfaction gap" can plausibly reconstruct "the world doesn't permit it."
- `satisfaction gap` — **opus-4-7:** Crispest named pair in the project; the 2×2 diagnostic works because both names work. Explicit keep.
- `satisfaction gap` — **sonnet-4-6-r2:** The strongest named pair in the project alongside control regret. The two-word name carries the diagnostic clarity that makes the 2×2 table work. Do not change.
- `satisfaction gap` — **sonnet-4-6-r2:** Occasionally paraphrased as "objective gap" or "attainability gap." The canonical name is established and load-bearing — standardize.
- `satisfaction gap` — **sonnet-4-6:** Named pair with #control-regret. Both names pull equal weight: each is a two-word compound that tells you the diagnostic direction. The pairing is the insight; destroying either leg damages the whole. Keep both.
- `attainability shortfall` — **gemini-targeted-alternatives:** "Satisfaction gap" explicitly ties into $V_O^{\min}$ being met. "Attainability" might refer only to $A_O$.

## 3. `orient cascade`

**Alternatives proposed:** `orient cascade`

_category: keep × 15, canonicalize × 1_

- `orient cascade` — **agent1-original-brainstorm:** Resonates with OODA without being captured by it; "cascade" conveys directional resolution-order succinctly.
- `orient cascade` — **codex-1:** Memorable and faithful to the staged dependency structure; this is exactly the kind of communal-imagination name the project needs more of.
- `orient cascade` — **codex-2:** Excellent memorable noun slot for a load-bearing ordering result.
- `orient cascade` — **codex-gpt-5-r2:** Strong bridge term for the cross-cycle causal chain. It is memorable without being gimmicky.
- `orient cascade` — **gemini-1:** Naming the sequential resolution order ($M_t \to \Sigma_t \to O_t$) as a "cascade" makes the information dependency instantly graspable.
- `orient cascade` — **gemini-2:** Very evocative and action-oriented.
- `orient cascade` — **haiku-4-5-r2:** The word "cascade" is evocative and accurate; the sequence is directional. Passes renamed-from-now-sounds-weird test.
- `orient cascade` — **haiku-4-5:** Resolution order by info dependency. "Cascade" is evocative; "orient" echoes the OODA loop and the Greek philosophical term (epistrophe — turning toward). Reads naturally: "the orient cascade orders the updates." Load-bearing naming. Keep.
- `orient cascade` — **opus-1m:** Good as-is.
- `orient cascade` — **opus-4-7-b:** Names both the structure (cascade = ordered resolution) and the heritage (Boyd's *Orient* of OODA) without being captured by OODA. Only other live candidate I considered was "orientation sequence" — flatter, weaker, rejected.
- `orient cascade` — **opus-4-7-r2:** Defended keep. Boyd's "Orient" is the right reference and the cascade structure is what the segment derives. The name cleanly extends the OODA reference to AAD's information-dependency-forced ordering.
- `orient cascade` — **opus-4-7:** The five-phase cycle has an "expand" for actuated agents; "cascade" evokes the forced-by-information-dependency ordering. One of the theory's best names. Keep.
- `orient cascade` — **sonnet-4-6-r2:** "Orient cascade" is one of the project's best names — it captures the sequential resolution structure of the expanded epistrophe phase. Evocative and accurate. Boyd's OODA "Orient" is the explicit inspiration.
- `orient cascade` — **sonnet-4-6-r2:** LEXICON.md and segment use "orient cascade." CLAUDE.md uses "Orient cascade" and "orient cascade" — lowercase is the correct form except when starting a sentence.
- `orient cascade` — **sonnet-4-6:** Short, verb-derived, evocative. "Orient" from Boyd's OODA is the right referent — the segment even says so. The cascade structure is visible in the name. Do not change.
- `orient cascade` — **sonnet-4-6:** See #orient-cascade keep vote. The word "orient" is earned by the Boyd connection. Keep.

## 4. `directed separation`

**Alternatives proposed:** `directed separation`, `goal-blind processing`, `pearl-blanket separation`, `epistemic isolation of belief update`

_category: keep × 15, rename × 3, canonicalize × 1_

- `directed separation` — **agent1-original-brainstorm:** Has no broad ML usage; mostly baggage-free. Small risk of separation-principle echo from LQR/Kalman. Add one-sentence clarification in segment Discussion — no rename.
- `directed separation` — **codex-1:** Excellent theory name: concrete structural image, low baggage, easy to cite aloud.
- `directed separation` — **codex-2:** Short, memorable, and exactly the right amount of theoretical flavor.
- `directed separation` — **codex-gpt-5-r2:** One of the strongest English names in the corpus: technical, memorable, and low baggage.
- `directed separation` — **gemini-1:** Adopts useful baggage from causal inference (d-separation) nicely.
- `directed separation` — **gemini-2:** Good analog to d-separation; intuitive and load-bearing.
- `directed separation` — **gemini-3-1-pro-preview-r2:** Core load-bearing name in AAD architecture. The separation of epistemic update from purpose is fundamental.
- `directed separation` — **haiku-4-5-r2:** Defended keep. The two-word "directed separation" is already a memorable noun phrase; changing either half would displace existing prose conventions without gain.
- `directed separation` — **haiku-4-5:** Specialist vocabulary ("directed" as Pearl's causal terminology; "separation" as conditional-independence terminology) correctly names a causal-graph property. Baggage-carrying in the best sense — travels with control-theory and causality intuitions. The Class 1/2/3 scope partition clarifies what it means architecturally. Keep.
- `directed separation` — **opus-1m:** Keep. The LQR-separation-principle echo is real but best handled by a one-sentence clarification in segment Discussion, not a rename.
- `directed separation` — **opus-4-7-b:** Zero pre-existing meaning in ML; the two words ("directed" = asymmetric information flow; "separation" = independence in the update) are both load-bearing. The only collision risk is control theory's *separation principle*, which is actually a Class-1 *consequence* of directed separation — the echo is informative, not misleading. Keep.
- `directed separation` — **opus-4-7-r2:** Defended keep. "Directed separation" is one of the framework's distinctive named results and survives the communal-imagination test. The Pearl-blanket recognition is integrated through the name; renaming would lose that integration. Slug also reads correctly: it's a *derived* result (under the architectural scope condition), not a postulate.
- `directed separation` — **opus-4-7:** Survived the κ-as-scalar category-error rescue; the name now has its architectural Class 1/2/3 classification attached. Don't touch.
- `directed separation` — **sonnet-4-6-r2:** "Directed separation" is precise (the separation is directed — epistemic update is one-way independent of $G_t$) and distinctive. The architectural classification and Pearl-blanket connection make it load-bearing.
- `directed separation` — **sonnet-4-6-r2:** Never "goal-blindness" or "epistemic separation" or "processing independence." The canonical name is "directed separation" as established in the segment and LEXICON.md.
- `directed separation` — **sonnet-4-6:** "Directed" specifies the asymmetry (goal-blind epistemic update; goal-dependent purposeful update); "separation" names the property. The architectural classification (Class 1/2/3) hangs off this name. Used throughout the project in prose; the name is load-bearing. Keep.
- `goal-blind processing` — **audit-471203-incremental:** "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative. [from 31-34-section-ii-opening-batch.md] [one of 3 alternatives proposed in the original audit row]
- `pearl-blanket separation` — **audit-471203-incremental:** "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative. [from 31-34-section-ii-opening-batch.md] [one of 3 alternatives proposed in the original audit row]
- `epistemic isolation of belief update` — **audit-471203-incremental:** "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative. [from 31-34-section-ii-opening-batch.md] [one of 3 alternatives proposed in the original audit row]

## 5. `identifiability floor`

**Alternatives proposed:** `identifiability floor`, `no-go theorem`

_category: keep × 14, canonicalize × 1, rename × 1_

- `identifiability floor` — **agent1-original-brainstorm:** "Floor" is a load-bearing metaphor. Cannot go below it without outside help.
- `identifiability floor` — **codex-1:** Strong metaphor and well-matched to the segment's job: it names a hard lower boundary while still leaving room for explicit escape routes.
- `identifiability floor` — **codex-2:** Excellent negative-half companion to separability; "floor" is more useful than a generic "no-go."
- `identifiability floor` — **codex-gpt-5-r2:** Excellent meta-pattern name. Floor is concrete and scope-honest.
- `identifiability floor` — **gemini-1:** "Floor" is a great spatial metaphor for a structural no-go result.
- `identifiability floor` — **gemini-3-1-pro-preview-r2:** Excellent cross-sectional concept name.
- `identifiability floor` — **haiku-4-5:** Exact metaphor for what it names — structural boundary that blocks general identification. Complements separability-pattern symmetrically. Keep.
- `identifiability floor` — **opus-1m:** "Floor" metaphor is load-bearing; no better candidate. Keep.
- `identifiability floor` — **opus-4-7-b:** "Floor" is the right geometric metaphor — the no-go is a *floor you can't go below without outside help*, and the machinery that escapes it is named relative to it. One of the best meta-segment names in the project.
- `identifiability floor` — **opus-4-7-b:** Explicit keep. Named best of the three meta-segments; the geometric metaphor ("floor you can't cross without information augmentation") is exactly load-bearing. Together with the above two proposed renames: **floor / ladder / forced-coordinates** reads as a trio of concrete mental pictures — one of AAD's highest-leverage naming opportunities if all three land together.
- `identifiability floor` — **opus-4-7-r2:** Defended keep. "Floor" is the right metaphor — below this, no statistic can recover the inference; above it, AAD-supplied machinery escapes. Pairs with "ladders" if `#disc-separability-pattern` lands at separability-ladders. The pattern names the negative half cleanly.
- `identifiability floor` — **opus-4-7:** Three-word noun that invites both floor-instances and escape-routes; "floor" evokes the structural lower bound and Joseph has already used "escape the floor" as organic prose. Keep.
- `identifiability floor` — **sonnet-4-6-r2:** The strongest subject-noun in the three meta-segments. "Floor" is load-bearing — it names the asymmetry (you can climb above it; you cannot go below it without specific machinery). Mathematically precise and memorable.
- `identifiability floor` — **sonnet-4-6:** The Working Notes on this segment explicitly defend the "floor" framing over "no-go theorems" and the argument is correct — "floor" captures asymmetry (you cannot go below, but you can climb above). Memorable noun. Keep.
- `identifiability floor` — **sonnet-4-6:** See #identifiability-floor keep vote above. Already in prose use. Keep.
- `no-go theorem` — **codex-1:** Too generic and too negative. It loses the boundary-and-escape structure that makes the current name useful.

## 6. `concept the parameter space region within which an agent maintain bounded mismatch indefinitely`

**Alternatives proposed:** `persistence envelope`, `structural persistence regime`, `parametric feasibility window`, `parametric regime or stability envelope`, `viable mismatch region`, `adaptive basin`, `stability envelope`, `safety envelope`

_category: name-unnamed × 10, rename × 6, canonicalize × 5, add-alias × 1_

- `persistence envelope` — **agent1-original-brainstorm:** Engineering vocabulary, geometrically evocative. "Well inside its persistence envelope" reads more crisply than "satisfies persistence condition with non-marginal adaptive reserve." [original phrasing: unnamed: the sector-persistence region in parameter space]
- `persistence envelope` — **codex-gpt-5-r2:** Strongest new shared proposal from the other votes. Flight-envelope connotations fit the safe operating region exactly. [original phrasing: bounded mismatch region]
- `persistence envelope` — **gemini-1:** "Envelope" is standard flight-dynamics vocabulary for a safe operating region. Highly memorable. [original phrasing: unnamed: the region where the persistence condition holds]
- `persistence envelope` — **gemini-3-1-pro-preview-r2:** Evocative, captures the safe operational region geometrically. [original phrasing: unnamed: the sector-persistence region in parameter space]
- `persistence envelope` — **gemini-targeted-alternatives:** Geometrically evocative and already gaining traction elsewhere in the targets. [original phrasing: bounded mismatch region]
- `persistence envelope` — **gemini-targeted-alternatives:** Geometric metaphor for the safe operating region. [original phrasing: unnamed the region where the persistence condition holds]
- `persistence envelope` — **gemini-targeted-alternatives:** Standard geometric boundary for survival. [original phrasing: unnamed the persistence region in $(\alpha, \rho, R)$ parameter space]
- `persistence envelope` — **gemini-targeted-alternatives:** Same geometric boundary. [original phrasing: unnamed the region in parameter space where sector persistence holds]
- `persistence envelope` — **gemini-targeted-alternatives:** Same geometric boundary. [original phrasing: unnamed the sector persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch]
- `persistence envelope` — **haiku-4-5-r2:** Currently referenced paraphrastically ("the region where the persistence condition holds"). "Persistence envelope" is geometrically evocative and concise; passes communal-imagination test. Could be a scope or result name. [original phrasing: unnamed: the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely]
- `persistence envelope` — **opus-1m:** Strong preference (upgrading from original's +1). Engineering vocabulary, geometrically evocative. "Well inside its persistence envelope" reads more crisply than "satisfies the persistence condition with non-marginal adaptive reserve." Genuinely useful new named slot. [original phrasing: unnamed: the sector-persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch]
- `persistence envelope` — **opus-4-7-b:** The bounded region where $\alpha R > \rho$ holds — currently referenced as "the region where the persistence condition holds" or "the adaptive regime." Engineering vocabulary has an exact match: *envelope* (as in flight envelope). "The agent is well inside its persistence envelope" / "the adversarial agent is pushing $B$'s persistence envelope" read with zero paraphrase. This is AAD's single most-used-without-a-name concept. [original phrasing: unnamed: the region in parameter space where sector-persistence holds]
- `persistence envelope` — **opus-4-7-r2:** The set $\{(\alpha, \rho, R) : \alpha \gt \rho/R\}$ is referenced repeatedly in prose and in figures (the persistence-condition cone, the adaptive-reserve margin, the threshold surface) but has no name. "Persistence envelope" is engineering-vocabulary that travels well across domains and supports phrases like "this organization sits inside the persistence envelope" or "the reserve is the distance from the envelope boundary." High-value, empty slot, pure clarity gain. [original phrasing: unnamed: the persistence region in $(\alpha, \rho, R)$ parameter space]
- `persistence envelope` — **opus-targeted-alternatives-v2:** Per `result-persistence-condition` and `result-sector-persistence-template`: the region where $\alpha \gt \rho/R$ holds. "Region" is geometrically descriptive; "envelope" is the standard control-theory term for the same set viewed dynamically (the boundary an agent's state cannot leave while the persistence guarantee holds). Codex's r1 proposal (single +2) is genuinely better than the current and survives my independent stress-test. [original phrasing: bounded mismatch region]
- `persistence envelope` — **opus-targeted-alternatives:** Codex's rename is good. "Bounded mismatch region" describes a property; "persistence envelope" names the same set as the *region within which the persistence guarantee holds*. The "envelope" framing is also the standard control-theory term for "operating bounds within which guarantees apply" (flight envelope, operating envelope). Strong rename. [original phrasing: bounded mismatch region]
- `structural persistence regime` — **gemini-targeted-alternatives:** The stable regime governed by the persistence condition. [original phrasing: unnamed the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely]
- `parametric feasibility window` — **gemini-targeted-alternatives:** The region governed by the current model class $\mathcal{M}$. [original phrasing: unnamed the region in parameter space where parametric updates remain effective before structural change is forced]
- `parametric regime or stability envelope` — **haiku-4-5-r2:** OUTLINE.md mentions "A2' sub-scope α₁ / α₂ / β partition" but does not give a memorable name to the overall region concept. "Parametric regime" is more technical; "stability envelope" parallels the persistence-envelope concept. Weak preference; this might be too specialized for naming. [original phrasing: unnamed: the region in parameter space where parametric updates remain effective before structural change is forced]
- `viable mismatch region` — **opus-targeted-alternatives-v2:** Considered. Pairs with LEXICON's "viable region" prose. Weaker than "persistence envelope" — "viable" is the property; "envelope" is the geometric object. [original phrasing: bounded mismatch region]
- `adaptive basin` — **opus-4-7-b:** Considered. Reject: "basin" is already mathematically loaded (basin of attraction), and AAD's region *is a basin of attraction* — using the word would either (i) be redundant with dynamical-systems vocabulary, or (ii) force AAD to formally justify "basin" at the derivation layer. Cleaner to reserve "basin" for the technical sense and use "envelope" for the prose handle. [original phrasing: unnamed: the persistence envelope]
- `stability envelope` — **opus-targeted-alternatives-v2:** Considered. Aligns with control-theory "stability region" baggage. Rejected: stability collides with sector-stability (`#result-sector-condition-stability`), and the segment's claim is *persistence* (boundedness over time under continuing disturbance) — a slightly stronger property than stability. [original phrasing: bounded mismatch region]
- `safety envelope` — **opus-targeted-alternatives:** Considered. Collides with AI-safety jargon. Rejected. [original phrasing: bounded mismatch region]

## 7. `information bottleneck`

**Alternatives proposed:** `information bottleneck`, `epistemic bottleneck`

_category: keep × 11, rename × 1_

- `information bottleneck` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep formal name; AAD-distinctive feature deserves separate label)" — Well-anchored in literature; AAD shouldn't rename. The AAD-distinctive *policy-conditioning* on the predictive term could be named separately: "Policy-Conditioned IB" / "Forward-Predictive IB" / "AAD-IB" — only if a distinguishing label is needed. Currently leans on standard name; auditor judges that the right call. [from 11-form-information-bottleneck.md]
- `information bottleneck` — **codex-1:** Correct baggage-carrying adoption. This is exactly the kind of prior-art name that should remain untouched.
- `information bottleneck` — **codex-gpt-5-r2:** Imported theorem name should remain canonical. It is already the recognized technical term.
- `information bottleneck` — **gemini-3-1-pro-preview-r2:** Established literature term (Tishby).
- `information bottleneck` — **haiku-4-5-r2:** Adopted technical term (Tishby); keeping original name respects prior art. No local pressure to change.
- `information bottleneck` — **haiku-4-5:** Adopted from Tishby 1999; canonical name in information theory. Baggage-carrying in the best sense — travels with information-theoretic intuitions. Do not rename. Exact application matches Tishby's definition. Keep.
- `information bottleneck` — **opus-1m:** Adopted (Tishby 1999); keep.
- `information bottleneck` — **opus-4-7-b:** Adopted from Tishby et al. — do not rename adopted concepts (prior-art-integration convention). The word *bottleneck* is doing real explanatory work; the baggage transfers.
- `information bottleneck` — **opus-4-7-b:** Keep — adopted directly from Tishby et al. per prior-art-integration convention. Do not rename adopted concepts.
- `information bottleneck` — **opus-4-7-r2:** Defended keep — direct adoption from Tishby with proper attribution; renaming would lose provenance.
- `information bottleneck` — **sonnet-4-6-r2:** External vocabulary adopted directly (Tishby, Pereira & Bialek). Per prior-art-integration principle, adopt with original name.
- `epistemic bottleneck` — **gemini-2:** Emphasizes the knowledge-compression aspect over raw Shannon information.

## 8. `chronica`

**Alternatives proposed:** `chronica`

_category: keep × 9, canonicalize × 1_

- `chronica` — **audit-471203-incremental:** "Chronica" is etymologically clean, the avoid-collision-with-$\mathcal{H}$ argument is solid, and the segment carries explicit non-forkability content that the term licenses. Auditor considers it well-chosen and load-bearing. [from 04-def-chronica.md]
- `chronica` — **audit-471203-incremental:** [Brief-field gloss candidates, not name votes — the auditor's intent was to surface prose explanations for the chronica segment's Brief field, not propose alternative names]: "everything the agent has lived through" / "the lived past" / "the river that the agent's identity is downstream of". The slug stays; the layperson/Feynman gloss is what's missing. [from 04-def-chronica.md] [original rows: 3 separate canonicalize votes on each gloss; recategorized as keep-with-glosses-in-notes since these aren't name proposals.]
- `chronica` — **codex-1:** Distinctive, speakable, and better than another overloaded "history" or "trace." Strong keep.
- `chronica` — **codex-2:** This is exactly the kind of memorable noun a theory wants: compact, distinctive, and reusable in speech.
- `chronica` — **codex-gpt-5-r2:** Strong core term: singular causal record, memorable, Greek-register aligned, and not easily confused with generic memory.
- `chronica` — **gemini-3-1-pro-preview-r2:** Load-bearing Greek vocabulary.
- `chronica` — **opus-4-7:** Singular Greek-root noun with clean Obsidian/prose pickup; also resolves the $\mathcal H$/entropy collision. Joseph deliberately avoided "history" — don't unwind.
- `chronica` — **sonnet-4-6-r2:** "Chronica" is the strongest name in the project — Greek-rooted, distinctive, avoids collision with entropy notation, survives every naming criterion. Do not rename.
- `chronica` — **sonnet-4-6-r2:** Never "history," "interaction history," or "$\mathcal{H}_t$" in prose (the chronica notation is $\mathcal{C}_t$ precisely to avoid collision with entropy). The canonical term is "chronica."
- `chronica` — **sonnet-4-6:** Excellent coinage. Greek term for "records of time" with zero collision with other vocabulary (avoids $\mathcal H$ for entropy). Memorable, singular, has been thoroughly adopted across the codebase. The strongest single naming decision in the project. Keep without question.

## 9. `strategy DAG`

**Alternatives proposed:** `strategy DAG`

_category: keep × 10, canonicalize × 1_

- `strategy DAG` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep)" — Substantive load-bearing segment. Auditor's only flag was that the segment is *large* and might benefit from being split; the *name* is correct. [from 43-46-section-ii-and-or-strategy-dag-gaps.md]
- `strategy DAG` — **codex-1:** Blunt and effective. The slug is legible instantly, and the concept it names is load-bearing.
- `strategy DAG` — **codex-2:** Exactly the right level of compression: simple, searchable, and faithful to the object.
- `strategy DAG` — **codex-gpt-5-r2:** Direct and technically honest. Keep rather than hiding the graph structure behind a metaphor.
- `strategy DAG` — **codex-gpt-5-r2:** The acronym is technical but exact. No need to prettify it.
- `strategy DAG` — **haiku-4-5-r2:** "Strategy DAG" is memorable and passes the communal-imagination test. The acronym DAG is standard. No change needed.
- `strategy DAG` — **haiku-4-5:** Self-descriptive (probabilistic directed acyclic graph for strategy), compact notation. Consistent lowercase convention with #agent-spectrum, #value-object, etc. Keep.
- `strategy DAG` — **opus-4-7-r2:** Defended keep. The DAG-with-AND/OR-and-single-parameter-edges representation is iconic in the framework and is referenced by slug in many downstream segments; renaming would create cascading editorial work for negligible reading-clarity gain. The segment also makes the case that the DAG structure is *derived* (acyclicity from temporal ordering, Markov from CMC), so "strategy DAG" reads as a result-name as well as a definition-name.
- `strategy DAG` — **opus-4-7-r2:** In prose this is sometimes "the strategy graph" or "the strategy structure" or "the agent's strategic causal model." Canonicalize on "strategy DAG" for the AND/OR-DAG-with-edge-credences object, and reserve "strategy" alone for $\Sigma_t$ as a state object distinct from its representation.
- `strategy DAG` — **opus-4-7:** Established; the segment does a lot of work (acyclicity derived, Markov derived, correlation hierarchy). Keep.
- `strategy DAG` — **sonnet-4-6-r2:** "Strategy DAG" is precise, memorable, and already has convention weight. The DAG structure is the key novelty; the name accurately foregrounds it.

## 10. `chain confidence decay`

**Alternatives proposed:** `chain confidence decay`, `log confidence additive`

_category: keep × 12, rename × 1_

- `chain confidence decay` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep; load-bearing)" — Auditor flagged this as the structural anchor for the additive-coordinate-forcing meta-pattern (chain-rule identity → three downstream uniqueness theorems). Name does its job. [from 39-42-section-ii-ciy-strategy-chain.md]
- `chain confidence decay` — **codex-2:** Clear phenomenon name rather than proof name; easy to paraphrase aloud.
- `chain confidence decay` — **codex-gpt-5-r2:** Strong exact-result name and good anchor for the log-additivity family.
- `chain confidence decay` — **gemini-1:** Clear and descriptive of the phenomenon.
- `chain confidence decay` — **gemini-2:** Highly descriptive of the log-confidence additive depth effect.
- `chain confidence decay` — **gemini-3-1-pro-preview-r2:** Evocative of the AND-chain probability multiplication.
- `chain confidence decay` — **haiku-4-5-r2:** Mathematical precision; "chain confidence decay" names the pattern exactly.
- `chain confidence decay` — **haiku-4-5:** Self-descriptive — log-confidence additive in depth along a causal chain. Solid name; reads naturally. Keep.
- `chain confidence decay` — **opus-4-7-r2:** Acceptable keep. "Chain confidence decay" reads as a phenomenon and is referenced by name in many downstream segments. The keep is defensible against the proposed rename.
- `chain confidence decay` — **opus-4-7:** Inevitability-core segment; name matches the log-decomposition content. Keep.
- `chain confidence decay` — **sonnet-4-6-r2:** "Chain confidence decay" is precise, memorable, and names the exact phenomenon: chain depth causes monotonic decay in aggregate confidence.
- `chain confidence decay` — **sonnet-4-6:** Crisp compound noun. The name is self-explaining: confidence decays along a chain. It also works as the anchor of the additive-coordinate-forcing pattern — "chain-level additive log-confidence decay" is how other segments refer to it. Keep.
- `log confidence additive` — **opus-4-7-r2:** Considered. "Chain confidence decay" emphasizes the *decay* (downstream effect); "log-confidence additive" emphasizes the *uniqueness move* (additivity in log-space, the chain-layer instance of additive-coordinate-forcing). Mild preference for the latter because the additive identity is what the segment proves; decay is the consequence. Slug-as-thing-defined principle.

## 11. `persistence condition`

**Alternatives proposed:** `persistence condition`, `survival equation`

_category: keep × 8, canonicalize × 1, add-alias × 1_

- `persistence condition` — **codex-gpt-5-r2:** This is an established theorem-facing phrase. It is generic, but it names the primary threshold cleanly.
- `persistence condition` — **gemini-3-1-pro-preview-r2:** Central inequality of the framework, decomposing into structural persistence and task adequacy.
- `persistence condition` — **haiku-4-5-r2:** Canonical across domains (Lyapunov, RL, organizational viability, software maintenance). Load-bearing name; rename would displace vast prose footprint.
- `persistence condition` — **haiku-4-5:** Core definition. Unambiguous. Keep.
- `persistence condition` — **opus-4-7-b:** Keep. The slug for AAD's *central inequality*; any change would ripple through every citing segment.
- `persistence condition` — **opus-4-7-r2:** Defended keep — the framework's central inequality. The segment carries the canonical bathtub gloss in its Findings section; renaming would break the iconic naming.
- `persistence condition` — **opus-4-7:** The central inequality; eponymous. Keep.
- `persistence condition` — **sonnet-4-6-r2:** "Persistence condition" is the central named result of the theory. The name is canonical, memorable, and appears throughout the codebase. Do not change.
- `persistence condition` — **sonnet-4-6-r2:** Sometimes appears as "the persistence criterion," "the adaptive persistence condition," or "the alpha > rho/R condition." One name: "persistence condition."
- `survival equation` — **codex-gpt-5-r2:** Useful elevator-pitch phrase, but too slogan-like for canonical theorem prose.

## 12. `concept the slogan capturing AAD organizing principle that an adaptive system correction rate must exceed its target change rate`

**Alternatives proposed:** `contraction over drift principle`, `contraction imperative`, `the projection slogan contraction over drift slogan`, `projection contraction slogan`, `drift contraction inequality`

_category: name-unnamed × 7, canonicalize × 5_

- `contraction over drift principle` — **codex-1:** The slogan is too long to cite repeatedly. A short label would let intros and reviews point back to it cleanly. [original phrasing: unnamed: organizing-principle slogan "an adaptive system is a projection whose contraction rate exceeds its target's drift rate"]
- `contraction over drift principle` — **codex-gpt-5-r2:** Strong compact name for the core organizing slogan. It is more reusable than the full sentence. [original phrasing: projection contraction must beat target drift]
- `contraction over drift principle` — **gemini-targeted-alternatives:** Short, memorable slogan for the core Lyapunov inequality. [original phrasing: projection contraction must beat target drift]
- `contraction over drift principle` — **gemini-targeted-alternatives:** Standardizes the O-BP10 slogan across the framework. [original phrasing: unnamed organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate]
- `contraction over drift principle` — **gemini-targeted-alternatives:** Resolves the core O-BP10 slogan. [original phrasing: unnamed agent as a projection whose contraction rate must exceed its target s drift]
- `contraction over drift principle` — **gemini-targeted-alternatives:** Final lock-in for the core slogan. [original phrasing: unnamed the projection whose contraction rate must exceed target drift the opus organizing principle slogan]
- `contraction over drift principle` — **gemini-targeted-alternatives:** Asserts the fundamental slogan. [original phrasing: unnamed the contraction over drift insight]
- `contraction over drift principle` — **sonnet-4-6:** CLAUDE.md attributes to Opus: "an adaptive system is a projection whose contraction rate exceeds its target's drift rate." This is described as an "organizing-principle slogan" that "has not yet been surfaced at segment level." It deserves a name. "Contraction-over-drift principle" or "drift-contraction inequality" would let segments cross-reference it. The slogan form is already excellent; the name should be a compressed version of it. [original phrasing: unnamed: the projection whose contraction rate must exceed target drift — the Opus organizing-principle slogan]
- `contraction imperative` — **gemini-1:** Gives a name to a core mental model of the agent's struggle against the environment. [original phrasing: unnamed: agent as a projection whose contraction rate must exceed its target's drift]
- `the projection slogan contraction over drift slogan` — **opus-4-7-b:** CLAUDE.md §7(g) names this as "organizing-principle slogan" (O-BP10, not yet surfaced at segment level). If promoted to segment-level it deserves a short handle — "the contraction-over-drift slogan" is short enough to say in a sentence. Low priority; depends on SP-7 / O-BP10 promotion decision. [original phrasing: unnamed: Joseph's mental model "projection whose contraction rate must exceed its target's drift rate"]
- `projection contraction slogan` — **opus-4-7:** CLAUDE.md §7(g) flags this as Opus O-BP10, "not yet surfaced at segment level." Deserves a name so it can be referenced before it lands as prose. [original phrasing: unnamed: the organizing-principle slogan — "An adaptive system is a projection whose contraction rate exceeds its target's drift rate"]
- `drift contraction inequality` — **sonnet-4-6:** Alternative name. More technical but maps directly to the inequality. [original phrasing: unnamed: the contraction-over-drift insight]

## 13. `logogenic agent`

**Alternatives proposed:** `logogenic agent`, `section iii logogenic agent`, `linguistic agent`

_category: keep × 7, canonicalize × 2, rename × 1_

- `logogenic agent` — **codex-1:** Novel but justified; it names the structural property rather than today's implementation technology. Strong keep.
- `logogenic agent` — **codex-2:** Novel, but the novelty earns its keep by naming a structural channel property rather than a transient implementation.
- `logogenic agent` — **codex-gpt-5-r2:** Strong family term for language-constituted agents. It fits the Greek-register commitment.
- `logogenic agent` — **codex-gpt-5-r2:** Canonical family term.
- `logogenic agent` — **opus-4-7-b:** Keep. Aligns with the `logogenic` class name in LEXICON and does not conflict with anything external.
- `logogenic agent` — **opus-4-7-r2:** Defended keep — pairs with `#scope-moral-continuity` cleanly.
- `logogenic agent` — **sonnet-4-6-r2:** "Logogenic" is the project's deliberately coined Greek-rooted term for language-constituted agents. Per project vocabulary commitment, this is the right name.
- `logogenic agent` — **sonnet-4-6-r2:** Should never appear as "language-based agent" or "LLM-based agent" in the formal theory (those are instantiation-level descriptions, not the architectural concept). "Logogenic agent" = constituted by language; "LLM-based agent" = instantiation. The scope segment explains this.
- `section iii logogenic agent` — **gemini-targeted-alternatives:** Standardizes section hierarchy.
- `linguistic agent` — **gemini-1:** Logogenic names the structural property (constituted by logos) better than the generic "linguistic". Keep Logogenic.

## 14. `symbiogenic composition`

**Alternatives proposed:** `symbiogenic composition`, `symbiogenic absorption`, `asymmetric absorption`

_category: keep × 11, rename × 2_

- `symbiogenic composition` — **codex-2:** High-aesthetic-risk name, but it earns that risk by being vivid and structurally specific.
- `symbiogenic composition` — **codex-gpt-5-r2:** Strong, etymologically apt, and scope-honest for asymmetric composite formation.
- `symbiogenic composition` — **codex-gpt-5-r2:** Distinctive and exactly aimed at asymmetric composite formation.
- `symbiogenic composition` — **gemini-1:** Beautiful biological metaphor for asymmetric absorption.
- `symbiogenic composition` — **gemini-3-1-pro-preview-r2:** Good Greek alignment, descriptive.
- `symbiogenic composition` — **haiku-4-5:** "Symbiogenic" (host integrates endosymbiont) borrowed from biology and evolution. Evocative, specialized vocabulary. Reads naturally in context of asymmetric absorption mechanisms. Keep.
- `symbiogenic composition` — **opus-4-7-b:** Keep. "Symbiogenic" is the exactly-right biological term for "one agent integrating another that formerly had its own autonomy"; the $U_O$-crosses-threshold-from-below mechanism matches the biological meaning with precision. Rare case where an adopted term upgrades the reader's intuition about the formalism.
- `symbiogenic composition` — **opus-4-7-r2:** Defended keep. The endosymbiont-host integration mechanism is a substantial composition mechanism, and "symbiogenic" is the right biological-vocabulary import.
- `symbiogenic composition` — **opus-4-7:** Etymologically accurate (Margulis lineage; asymmetric absorption). Keep unless cleaner alternative emerges.
- `symbiogenic composition` — **sonnet-4-6-r2:** "Symbiogenic" is the established biological term (Margulis) adopted directly. The asymmetric absorption mechanism is EXACTLY what the word means. Strong keep per prior-art-integration principle.
- `symbiogenic composition` — **sonnet-4-6:** "Symbiogenic" is technically correct (host absorbs endosymbiont) but requires specialist vocabulary. Appropriate if the target audience includes evolutionary biology. Mild risk of requiring explanation on each encounter outside that community.
- `symbiogenic absorption` — **gemini-2:** "Absorption" is the specific asymmetric mechanism described (host integrates endosymbiont).
- `asymmetric absorption` — **sonnet-4-6:** Plainer English for the same concept. Less evocative but lower bar for new readers.

## 15. `additive coordinate forcing`

**Alternatives proposed:** `forced coordinate`, `coordinate forcing`, `uniqueness coordinate forcing`, `additive coordinate forcing`, `uniqueness coordinate`, `logarithmic lift`, `log coordinate forcing`, `anchor lattice`, `additive lift`, `axiom forcing`, `cauchy coordinate`

_category: rename × 37, canonicalize × 3, keep × 1_

- `forced coordinate` — **codex-1:** The current name is accurate but over-explains the mechanism. "Forced coordinates" is shorter, more noun-like, and broad enough to cover the metric-layer case too.
- `forced coordinate` — **codex-2:** Too breezy and it drops the uniqueness-theorem discipline that makes the segment interesting.
- `forced coordinate` — **codex-gpt-5-r2:** The family claim is that additive or invariant structure forces a coordinate choice. Forced coordinates is compact and general.
- `forced coordinate` — **gemini-1:** "Forced coordinates" is broader and more scope-honest for the various layers involved.
- `forced coordinate` — **gemini-3-1-pro-preview-r2:** Scope-honesty for meta-segment. Covers Cauchy-FE and Čencov machineries forcing coordinates onto Legendre-Fenchel geometry.
- `forced coordinate` — **gemini-3-1-pro-preview-r2:** Concurring with Codex/Haiku/Sonnet: drops the overly-restrictive "additive" and names the true meta-pattern.
- `forced coordinate` — **haiku-4-5-r2:** Round-1 consensus; "forced" is more evocative and covers Čencov's 4th instance (not exclusively Cauchy-FE). Passes the communal-imagination test better.
- `forced coordinate` — **opus-1m:** The segment carries four primary instances: three via Cauchy functional equation (chain / divergence / update) and one via Čencov-invariance (metric). The segment itself states (line 50): "Both clear the broader discipline — uniqueness-theorem-forced coordinate under AAD-internal axiom — but via distinct uniqueness-theorem machineries." Naming the meta-pattern after only one machinery (Cauchy) violates the scope-honesty the segment just established. "Forced coordinates" covers both machineries. Preserves "additive-coordinate-forcing" as long-form in the segment subtitle.
- `forced coordinate` — **opus-4-7-b:** The current name has two problems: (i) it's *additive-only*, which was honest when the meta-segment covered three Cauchy-FE instances, but is now factually under-inclusive since the Čencov / Fisher-metric 4th primary instance is not log-additive — the segment itself acknowledges this and floats `#uniqueness-coordinate-forcing` as a possible rename; (ii) five-syllable hyphen-compound is not a name anyone reaches for in conversation. "Forced coordinates" is the concept in two short words: the coordinate is *forced* by a uniqueness theorem operating on an AAD-internally-motivated axiom. Covers both Cauchy-FE and Čencov mechanisms. Preserves the pattern's content (1 anchor + 3 theorems, with Lyapunov / IB as adjacent).
- `forced coordinate` — **opus-4-7-r2:** Acceptable alternative to coordinate-forcing; "forced-coordinates" is the result, "coordinate-forcing" names the move. I have a mild preference for the move-form because it parallels "directed separation" and "satisfaction gap" — verb-flavored compound nouns.
- `forced coordinate` — **opus-4-7:** The Čencov fourth primary instance forces the Fisher metric, which is not log-additive — the current name advertises three-out-of-four. "Forced coordinates" covers both Cauchy-FE and Čencov machineries without overpromising additivity. The segment itself flags this in the Discussion. Candidate.
- `forced coordinate` — **sonnet-4-6-r2:** Alternative — noun form rather than gerund form. Slightly more thing-like. Weaker preference than `disc-coordinate-forcing`.
- `forced coordinate` — **sonnet-4-6:** Passive noun; loses the process-verb structure that "forcing" has. A reader encountering it first might not know what forces them.
- `coordinate forcing` — **codex-gpt-5-r2:** Acceptable fallback, but it is less noun-like and less memorable than forced coordinates.
- `coordinate forcing` — **opus-1m:** Acceptable alternative to #forced-coordinates; names the activity in verb form. Slightly less concrete than "forced coordinates" as a noun.
- `coordinate forcing` — **opus-4-7-b:** Verb-form alternative; acceptable fallback if `#forced-coordinates` doesn't land. Same argument, slightly more clinical.
- `coordinate forcing` — **opus-4-7-r2:** "Additive" undersells one of the four layers (the metric layer's Čencov-invariance is not literally additivity in a Cauchy-FE sense — it's invariance under reparameterization that picks out the Hessian of the dual potential). The segment itself names "additive or invariant coordinate" in the body. Dropping "additive" makes the meta-pattern name as broad as the four layers it actually covers. Slug layer.
- `coordinate forcing` — **opus-4-7-r2:** Confirmation with new reasoning — three peers (Codex, Haiku, Gemini, Sonnet) all reached "forced-coordinates" while my own first vote was "coordinate-forcing." Seeing the cross-architecture pull toward "forced-coordinates" makes me less confident in the move-form preference; the result-form ("forced-coordinates") may be more memorable in conversation precisely because the move ("forcing") is mechanical and the *result* (coordinates appearing forced) is the surprising thing. Keeping my +2 vote for "coordinate-forcing" but adding this confirmatory +1 for the consensus form.
- `coordinate forcing` — **opus-4-7:** Verb-form variant; fine if #forced-coordinates doesn't land.
- `coordinate forcing` — **sonnet-4-6-r2:** "Additive" in the slug is redundant once the segment explains that the forcing is via additivity axioms. The slug reads as describing an additive operation, but what's actually being named is the phenomenon of coordinates being forced by uniqueness theorems. "Forced coordinates" or "coordinate-forcing" without "additive" is cleaner and still accurate — the Discussion section carries the "additive" nuance.
- `coordinate forcing` — **sonnet-4-6:** The segment itself acknowledges that the Čencov 4th instance is not Cauchy-FE-additive; the title's "additive" is already acknowledged to be slightly wrong in the Discussion. "Coordinate forcing" names the broader discipline accurately, keeps the verb form, and doesn't overclaim the mechanism.
- `uniqueness coordinate forcing` — **codex-1:** More abstract than the current name and less memorable than "forced coordinates." It sounds like a category label, not a concept people will use.
- `uniqueness coordinate forcing` — **codex-2:** The current name undersells the Čencov/Fisher instance; the broader discipline is uniqueness, not additivity alone.
- `uniqueness coordinate forcing` — **haiku-4-5:** Weaker alternative emphasizing the broader discipline (uniqueness theorem + AAD-internal axiom) over sub-structure (log-additivity). Better accuracy for when the 4th instance dominates reader mindshare, but "additive" three-of-four justifies keeping current name.
- `uniqueness coordinate forcing` — **opus-4-7:** Alternative that matches the "broader discipline" phrasing the segment itself uses. Less snappy than #forced-coordinates; more precise.
- `uniqueness coordinate forcing` — **sonnet-4-6:** Alternative rename capturing the shared mechanism (uniqueness theorem on AAD-internal axiom). More precise than "coordinate forcing" alone, but less smooth to say.
- `additive coordinate forcing` — **haiku-4-5:** Hedged keep. The "additive" emphasis correctly highlights three of four instances (Cauchy-FE log-additive). The Čencov fourth instance diverges on sub-structure (Riemannian metric rather than log coordinate) but shares broader discipline. Current name acceptably descriptive; slight rename might clarify uniqueness-theorem focus. (See weak alternative below.)
- `uniqueness coordinate` — **opus-4-7-b:** Closer to the mechanism ("uniqueness theorem forces coordinate"); loses a little crispness compared to `#forced-coordinates`. Second-choice.
- `logarithmic lift` — **agent1-original-brainstorm:** Verbose.
- `log coordinate forcing` — **agent1-original-brainstorm:** More direct but verbose.
- `anchor lattice` — **agent1-original-brainstorm:** Too structural-sounding for the "1-anchor-plus-3-theorem" framing.
- `additive lift` — **agent1-original-brainstorm:** Considered but weaker. "Lift" too common in math to stick.
- `additive lift` — **opus-1m:** "Lift" is overloaded in math (bundle lifts, category-theoretic lifts) and doesn't suggest uniqueness-theorem forcing.
- `axiom forcing` — **agent1-original-brainstorm:** Less self-descriptive than #cauchy-coordinates.
- `axiom forcing` — **opus-1m:** Underdescriptive — doesn't convey that the *thing forced* is a coordinate.
- `cauchy coordinate` — **agent1-original-brainstorm:** Weak preference. Names the mechanism and the output; short and crisp. Downside: "Cauchy" overloaded in math. Retain additive-coordinate-forcing as long-form subtitle.
- `cauchy coordinate` — **codex-gpt-5-r2:** Too narrow and misleading because the family includes Fisher, Cencov, IB, and Legendre geometry, not only Cauchy functional equations.
- `cauchy coordinate` — **opus-1m:** Explicit rejection. The Čencov metric-layer 4th primary instance is NOT Cauchy-FE; naming the meta-pattern for one of two machineries violates the scope-honesty commitment the segment establishes in its own Discussion section. Short and crisp, but scope-dishonest.
- `cauchy coordinate` — **opus-4-7-b:** Short, crisp, memorable — but actively misleading now that the Čencov instance is part of the primary four. "Cauchy" undersells the metric-layer instance and risks calcifying the meta-segment in a form it has already grown past. Reject.
- `cauchy coordinate` — **opus-4-7-r2:** Considered and rejected — undersells the Čencov 4th instance (not Cauchy-FE) and overspecifies on the chain/divergence/update layers' machinery.
- `cauchy coordinate` — **opus-4-7:** Undersells the Čencov instance; would require a second meta-segment to cover the fourth primary instance. Reject.

## 16. `sector persistence template`

**Alternatives proposed:** `sector persistence template`, `bounded correction template`, `persistence template`

_category: keep × 10, rename × 3, add-alias × 1_

- `sector persistence template` — **agent1-original-brainstorm:** Technical-clinical but clear; meta-segment role legible from name. Keep (though see family-naming question in Quiet Successes).
- `sector persistence template` — **codex-2:** Long, but structurally honest; shortening it would likely erase which persistence machinery is in play.
- `sector persistence template` — **codex-gpt-5-r2:** The template role is real and cross-cutting. Keep as the reusable theorem pattern.
- `sector persistence template` — **haiku-4-5:** Abstract sector-persistence template; six AAD results as instances. "Template" emphasizes the reusable machinery. "Sector persistence" grounds it in the control-theoretic Lyapunov framework. Good name. Keep.
- `sector persistence template` — **opus-1m:** Technical but clear; role as shared-lemma is legible. Keep.
- `sector persistence template` — **opus-4-7-b:** Keep. "Template" is the correct AAD term (a parameter-free shared-lemma pattern that multiple results instantiate). Clinical but apt.
- `sector persistence template` — **opus-4-7-r2:** Defended keep. "Template" is doing precise work — the segment is invoked across six segments as a template, with each invocation specifying its own state variable and disturbance rate. The name matches the abstraction-pattern role.
- `sector persistence template` — **opus-4-7:** Names the mechanical content (Lyapunov on sector-bounded correction) and is already cited by six instantiations. Keep.
- `sector persistence template` — **sonnet-4-6-r2:** "Sector persistence template" names the abstract Lyapunov argument that multiple results instantiate. The "template" framing is accurate and useful.
- `sector persistence template` — **sonnet-4-6:** Alternative keep: "sector" distinguishes it from e.g. contraction-based persistence, which matters once #contraction-template exists. Both are live.
- `bounded correction template` — **codex-1:** Better public-facing name for what the result actually unifies. "Sector" names the proof device; "bounded correction" names the concept.
- `bounded correction template` — **codex-gpt-5-r2:** Strong public-facing gloss, but sector should remain in the formal name because the proof device distinguishes this template from contraction.
- `persistence template` — **codex-1:** Too broad. It would erase the special bounded-correction structure that distinguishes this template from every other persistence discussion in the repo.
- `persistence template` — **sonnet-4-6:** "Sector" names the mathematical structure; the template's job is persistence. "Persistence template" is shorter and what users will say in conversation. Weak preference — "sector-persistence" is honest about the mechanism.

## 17. `temporal optimality`

**Alternatives proposed:** `temporal optimality`

_category: keep × 8_

- `temporal optimality` — **codex-1:** Strong, disciplined, and reusable. It sounds like a theorem target rather than a slogan.
- `temporal optimality` — **codex-2:** Excellent theorem-style name: short, forceful, and memorable.
- `temporal optimality` — **codex-gpt-5-r2:** Good TST postulate name. It says what the optimization is about.
- `temporal optimality` — **gemini-1:** "Temporal optimality" is clear, accurate, and sets the normative grounding perfectly.
- `temporal optimality` — **opus-4-7-b:** Keep. TST's central claim ("time-optimal development is the right objective"); slug is canonical.
- `temporal optimality` — **opus-4-7-r2:** Defended keep. "Temporal optimality" names the postulate exactly — among equivalent outcomes, least-time is preferred. The phrase is the foundational normative principle of TST and is correctly placed there (with AAD providing the descriptive grounding via persistence). Renaming would weaken a well-established prior commitment.
- `temporal optimality` — **sonnet-4-6-r2:** "Temporal optimality" is TST's foundational normative principle. The name is exact and memorable.
- `temporal optimality` — **sonnet-4-6:** The foundational TST postulate. "Temporal optimality" names the principle (least time is optimal given equivalent outcomes). Keep.

## 18. `adversarial destabilization`

**Alternatives proposed:** `adversarial destabilization`

_category: keep × 9_

- `adversarial destabilization` — **codex-1:** Exact, vivid, and result-shaped. This is a good permanent name.
- `adversarial destabilization` — **codex-gpt-5-r2:** Strong name for the threshold failure result.
- `adversarial destabilization` — **codex-gpt-5-r2:** Strong result name.
- `adversarial destabilization` — **gemini-2:** Excellent, evocative name for getting inside an opponent's loop.
- `adversarial destabilization` — **gemini-3-1-pro-preview-r2:** Descriptive.
- `adversarial destabilization` — **haiku-4-5:** Inside opponent's loop; includes effects spiral. "Destabilization" is precise; reads naturally in adversarial context. Keep.
- `adversarial destabilization` — **opus-4-7-b:** Keep. Direct, punchy; the word "destabilization" signals the direction (outward from the bounded region) rather than something neutral like "dynamics."
- `adversarial destabilization` — **opus-4-7-r2:** Acceptable keep. Pairs with #der-team-persistence as the cooperative/adversarial complement. The "effects spiral" sub-result inside is well-handled by Discussion mention.
- `adversarial destabilization` — **sonnet-4-6-r2:** Precise. The mechanism IS adversarial destabilization.

## 19. `agent spectrum`

**Alternatives proposed:** `agent spectrum`, `agency spectrum`, `agent quadrant`

_category: keep × 10, rename × 2, canonicalize × 1_

- `agent spectrum` — **codex-1:** Useful, legible, and already doing real explanatory work in Section II setup.
- `agent spectrum` — **codex-gpt-5-r2:** Strong umbrella for the model-richness by objective-richness continuum.
- `agent spectrum` — **gemini-3-1-pro-preview-r2:** The text explicitly defines regions of a continuum (spectra) for model and objective richness. The name fits.
- `agent spectrum` — **haiku-4-5-r2:** The "spectrum" metaphor (from basic to actuated) is apt and aids visualization. Good name.
- `agent spectrum` — **haiku-4-5:** ±model × ±objective quadrants. "Spectrum" emphasizes the continuum from fully-adaptive to fully-agentic. Reads naturally. Keep.
- `agent spectrum` — **opus-4-7-b:** Keep. "±model × ±objective quadrants" — "spectrum" is an acceptable word for a 2×2 partition if one is feeling generous. Alternative: `#agent-types-partition`, but that's worse.
- `agent spectrum` — **opus-4-7-r2:** Acceptable keep. The 2×2 model-richness × objective-richness table earns "spectrum" — the regions are continuous, not categorical, and the segment's discussion makes that explicit. I considered "agent-quadrants" but quadrants would imply four discrete categories, which the segment explicitly says they are not.
- `agent spectrum` — **opus-4-7-r2:** The 2×2 model-richness × objective-richness picture is consistently "agent spectrum" in the segment, but downstream sometimes "agent quadrant," "agent typology," "agent classification." Canonicalize on "agent spectrum"; the four corners are *regions*, not types or classes.
- `agent spectrum` — **opus-4-7:** Names the ±model × ±objective 2×2 table; the segment's content is exactly that. Fine.
- `agent spectrum` — **sonnet-4-6-r2:** "Spectrum" is accurate (two axes creating a continuum) and evocative. The term "agent spectrum" survives conversation naturally.
- `agent spectrum` — **sonnet-4-6-r2:** (Duplicate of above, confirming.)
- `agency spectrum` — **codex-2:** The segment maps richness of agency, not a zoology of agent types.
- `agent quadrant` — **opus-4-7-r2:** Considered and rejected — see above; quadrants oversells discreteness.

## 20. `concept the unupdatable region of the strategy DAG where edge receive no actionable feedback`

**Alternatives proposed:** `epistemic dead zone`, `the epistemic shadow`, `unobservable strategy subgraph`, `observability frontier`, `feedback starved branch`, `observability dead zone`, `epistemic shadow`, `observability dominance`, `unupdatable region`

_category: name-unnamed × 6, canonicalize × 6, rename × 5_

- `epistemic dead zone` — **codex-gpt-5-r2:** Better than observability dead zone: it names the consequence, not only the cause. [original phrasing: unobservable strategy subgraph]
- `epistemic dead zone` — **gemini-targeted-alternatives:** Strong prose phrase. Better than generic "unobservable" since it focuses on the epistemic failure to track it. [original phrasing: unobservable strategy subgraph]
- `epistemic dead zone` — **gemini-targeted-alternatives:** Standardizes the geometric phrasing for unobservable subgraphs. [original phrasing: unnamed regions of the strategy DAG that cannot be updated because feedback cannot reach them]
- `epistemic dead zone` — **gemini-targeted-alternatives:** Reaffirming the strong alias for unobservable edges. [original phrasing: unnamed the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning]
- `epistemic dead zone` — **gemini-targeted-alternatives:** Third hit on this concept; clearly needs this exact canonical name. [original phrasing: unnamed the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred]
- `epistemic dead zone` — **gemini-targeted-alternatives:** Locks in the geometric dead zone over "death". [original phrasing: gemini s epistemic death for the gain collapse unobservable DAG failure]
- `epistemic dead zone` — **opus-targeted-alternatives-v2:** Per `def-strategy-dag` and `der-chain-confidence-decay`: paths that receive no feedback (evidence starvation in extreme form — $\theta_j \to 0$ across an AND-chain). "Dead zone" is geometric (a region of the DAG) and operational (no signal reaches it). Confirms Codex's r1 +3. [original phrasing: unobservable strategy subgraph]
- `epistemic dead zone` — **opus-targeted-alternatives:** Codex's proposed alternative is genuinely better than the descriptive original. "Epistemic dead zone" names what the structure *does* (paths become epistemically dead — no signal can reach them) rather than what it *is* (a subgraph that happens to be unobservable). Pairs well with `#observability-dominance` and `#identifiability-floor`. Concur with codex; would have proposed similarly. [original phrasing: unobservable strategy subgraph]
- `the epistemic shadow` — **gemini-3-1-pro-preview-r2:** A stronger visual metaphor than "observability dead zone" for unobservable DAG edges. [original phrasing: unnamed: regions of the Strategy DAG that cannot be updated because feedback cannot reach them]
- `unobservable strategy subgraph` — **gemini-targeted-alternatives:** Identifies the geometric cause of the epistemic dead zone. [original phrasing: unnamed the phenomenon that unobservable edges freeze and paths become epistemically dead]
- `observability frontier` — **codex-gpt-5-r2:** Useful when discussing instrumentation investments, but lower priority than epistemic dead zone. [original phrasing: observability boundary in a strategy DAG]
- `observability frontier` — **haiku-4-5-r2:** Currently paraphrased as "unobservable edges freeze." The *frontier* of observability is a memorable geometric concept; "frontier" pairs with "boundary" nicely for two senses of the same limit. Weak naming; could be stronger. [original phrasing: unnamed: the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred]
- `feedback starved branch` — **gemini-targeted-alternatives:** Explains the consequence. [original phrasing: unobservable strategy subgraph]
- `observability dead zone` — **haiku-4-5-r2:** An extension of "observability dominance." Mentioned in LEXICON as "Observability dominance — unobservable strategy edges freeze; paths become epistemically dead." The phrase "epistemically dead" is apt but verbose. "Observability dead zone" is evocative and passes the communal-imagination test. Worth promoting. [original phrasing: unnamed: the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning]
- `epistemic shadow` — **opus-targeted-alternatives-v2:** Alternative to "dead zone" — more evocative metaphor (shadow = blocked from light = blocked from update signal). Gemini's r1 +3 single-vote. Both terms are good; "dead zone" is more clinical, "shadow" is more poetic. The framework's register tolerates both; pick by audience. [original phrasing: unobservable strategy subgraph]
- `observability dominance` — **haiku-4-5:** LEXICON lists "Observability dominance" as "a term with specific AAD meaning awaiting full treatment." The concept (unobservable strategy edges freeze) is load-bearing. The name is already proposed in LEXICON; when #observability-dominance segment is written, this name will be locked in. Currently unwritten; mark as ready-to-name. [original phrasing: unnamed: the phenomenon that unobservable edges freeze and paths become epistemically dead]
- `unupdatable region` — **opus-targeted-alternatives-v2:** Plain-mechanism alternative. Names what the region is (unupdatable). Weaker because "unupdatable" is awkward as an English word; "dead zone" / "shadow" are superior. [original phrasing: unobservable strategy subgraph]

## 21. `separability pattern`

**Alternatives proposed:** `separability ladder`, `separability pattern`, `tiered separability`, `staircase`, `separable core`, `three rung posture`, `separability staircase`

_category: rename × 18, keep × 4, canonicalize × 1_

- `separability ladder` — **agent1-original-brainstorm:** "Ladder" is right geometry — discrete levels of increasing difficulty ascending from separable-core.
- `separability ladder` — **codex-gpt-5-r2:** Ladder captures separable core, structured repair, general open better than pattern. It is also more memorable.
- `separability ladder` — **gemini-1:** "Ladder" conveys the "six ladders of increasing difficulty" described in the outline much better than "pattern".
- `separability ladder` — **gemini-3-1-pro-preview-r2:** Concurring with the consensus: "ladder" correctly captures the difficulty rungs across the axes.
- `separability ladder` — **haiku-4-5-r2:** Round-1 consensus; "ladder" is more structural — the rung metaphor is isomorphic to the difficulty levels across the seven axes.
- `separability ladder` — **opus-1m:** Agree with original brainstorm. "Ladder" is the right geometry for the seven-ladder structure (ascending difficulty from separable core). Upgrading from original's weak preference to strong — the seven-ladder enumeration in the segment explicitly instantiates the ladder geometry.
- `separability ladder` — **opus-4-7-b:** The meta-segment's own structure is a seven-row *ladder* (separable-core → structured-repair → general-open across seven axes of increasing difficulty). "Ladder" is the geometry the content actually has; "pattern" is inert filler that describes no content. Pairs mnemonically with `#identifiability-floor` ("the ladder above the floor"). The brainstorm converges here; I arrived independently on the same reasoning (from reading the seven-row table) before cross-checking.
- `separability ladder` — **opus-4-7-r2:** The segment's own organizing structure is *seven ladders*, each with separable-core / structured-repair / general-open. "Pattern" is the placeholder slug-form ("the pattern-segment names a pattern"); "ladders" is the substantive shape the segment actually identifies and names. The Brief, Discussion, and the cross-citation in `disc-identifiability-floor` all reach for "ladder" as the unit.
- `separability ladder` — **opus-4-7:** The segment itself uses "seven ladders" and each row is a ladder — the organizing concept is ladder-shaped, not pattern-shaped. "Pattern" feels generic for what is a precise three-rung structure.
- `separability ladder` — **sonnet-4-6-r2:** "Pattern" is generic; "ladder" is evocative of the actual structure — each instance IS a ladder with rungs, and the segment itself uses "ladders" throughout. Survives renamed-from-now-sounds-weird. The segment already says "six ladders"; the slug should say it too.
- `separability pattern` — **codex-1:** Slightly clinical, but honest about what the segment is doing across multiple ladders. I considered renaming it and did not find a cleaner winner.
- `separability pattern` — **codex-2:** Strong meta-segment name: short, teachable, and faithful to the repeated posture.
- `separability pattern` — **haiku-4-5:** Load-bearing meta-segment name with evocative three-part structure (separable core / structured repair / general open). Reads naturally aloud and across eight-page discussions. Do not change.
- `separability pattern` — **sonnet-4-6:** "Separability" does real work — it names the mathematical content (the regime decomposes), and "pattern" correctly signals this is a meta-level organizing principle rather than a theorem. Six-word alternatives all feel longer. Keep.
- `tiered separability` — **agent1-original-brainstorm:** Verbose.
- `staircase` — **agent1-original-brainstorm:** Too metaphorical.
- `separable core` — **opus-4-7-r2:** Considered and rejected — names only the first column of the three-part shape; loses the structured-repair and general-open framing that is half the point.
- `three rung posture` — **opus-4-7:** Too mechanical; loses "separability" which is the content.
- `separability staircase` — **agent1-original-brainstorm:** Whimsical.
- `separability staircase` — **codex-gpt-5-r2:** Staircase is bulkier and less elegant than ladder. It adds no precision.
- `separability staircase` — **opus-1m:** Whimsical without compensating precision gain.
- `separability staircase` — **opus-4-7-b:** Whimsical; the word "staircase" doesn't carry the increasing-difficulty semantics as cleanly as "ladder" (staircases are uniform; ladders intuitively get harder toward the top). Reject.
- `separability staircase` — **opus-4-7:** Whimsical; prefers #separability-ladder if any rename at all.

## 22. `shared intent`

**Alternatives proposed:** `shared intent`, `teleological unity`, `compressed purpose`

_category: keep × 7, rename × 4, rebuttal × 1_

- `shared intent` — **codex-1:** Compact, portable, and directly connected to the commander's-intent analogy. This already sounds like a concept, not a paper section.
- `shared intent` — **codex-2:** Strong communal noun with clear organizational resonance.
- `shared intent` — **codex-gpt-5-r2:** Clear and domain-familiar. It also maps well to mission command without overusing German terminology.
- `shared intent` — **codex-gpt-5-r2:** Excellent bridge between IB compression and mission command.
- `shared intent` — **haiku-4-5:** IB-compressed purpose. "Shared intent" reads naturally — what agents align on. Keep.
- `shared intent` — **opus-4-7-r2:** Defended keep. Maps directly to Clausewitz's "commander's intent" tradition (acknowledged in the segment); renaming would break the prior-art bridge.
- `shared intent` — **sonnet-4-6-r2:** Load-bearing prose vocabulary established across the codebase. "Shared intent" is what commanders communicate in Auftragstaktik and the IB compression finds — the name is exactly right.
- `shared intent` — **sonnet-4-6-r2:** [prose moved from candidate column]: "(keep `def-shared-intent`)" — Against Gemini's proposal `#def-teleological-unity` (+3). Gemini argues this "aligns perfectly with $U_O$ notation and unifies with epistemic/strategic unity." This is precisely the problem: `def-shared-intent` is the multi-agent concept (what is communicated between agents, the Clausewitz commander's intent, the IB compression of $G_{\text{shared}}$), while $U_O$ is the single-agent teleological unity. Renaming to `teleological-unity` would collapse a load-bearing distinction the framework relies on (shared intent is an inter-agent concept; teleological unity is intra-agent). Gemini's vote would create exactly the kind of conceptual blur the framework is designed to avoid. The "unification with $U_O$" is a feature of the current names doing different things, not a defect.
- `teleological unity` — **codex-gpt-5-r2:** Shared intent is an IB-compressed communication object. Teleological unity is already a unity dimension; merging them would erase a useful distinction.
- `teleological unity` — **gemini-3-1-pro-preview-r2:** Aligns perfectly with the $U_O$ notation and unifies with epistemic/strategic unity.
- `teleological unity` — **opus-4-7-r2:** Rebuttal — Gemini proposed this rename at +3 with the rationale that it aligns with U_O notation and unifies with epistemic/strategic unity. I think this is wrong. "Shared intent" is the *operational* cross-agent communication concept (what gets transmitted, the IB-compressed payload of $G_t$); "teleological unity" is the *measured* alignment property ($U_O = I/H$). The two are NOT the same: a multi-agent system can have low teleological unity but still transmit shared intent (poorly). Renaming would collapse the distinction the framework currently makes. Sonnet's defended-keep at +3 is correct and Gemini's rename undermines a load-bearing distinction.
- `compressed purpose` — **gemini-2:** Highlights the Information Bottleneck aspect of shared intent.

## 23. `adaptive reserve $\Delta\rho^\ast$`

**Alternatives proposed:** `adaptive reserve`

_category: keep × 7_

- `adaptive reserve` — **agent1-original-brainstorm:** Two words, one intuition, immediately suggests shock-absorber depth.
- `adaptive reserve` — **gemini-1:** Clear, evocative engineering vocabulary. Does not need changing.
- `adaptive reserve` — **gemini-2:** Very evocative physical intuition, like thermal or mechanical reserve. Do not touch.
- `adaptive reserve` — **opus-1m:** Good as-is.
- `adaptive reserve` — **opus-4-7-b:** Mechanical-engineering intuition ("shock reserve" / "crumple zone") fits exactly what the quantity measures. The two-word compound lands on the first read.
- `adaptive reserve` — **opus-4-7:** Rare English term that reads as *shock tolerance* in prose and ties cleanly to the $\alpha R - \rho$ formula. One of the project's cleanest symbol-to-English pairs. Keep.
- `adaptive reserve` — **sonnet-4-6:** Perfect term. "Reserve" is the right word — it is the shock tolerance the agent has banked against future disturbances. Keep.

## 24. `AAD adaptation and actuation dynamic`

**Alternatives proposed:** `AAD adaptation and actuation dynamic`, `AAD`, `AAD agentic adaptation dynamic`

_category: keep × 7, rename × 2, canonicalize × 1_

- `AAD adaptation and actuation dynamic` — **agent1-original-brainstorm:** Recent rename (2026-04-16); further thrash dilutes identity. "Actuation" imperfection is real but a Section II preamble clarification handles it more cheaply than another rename.
- `AAD adaptation and actuation dynamic` — **codex-1:** "Actuation" is imperfect, but framework-level churn is more expensive than the remaining mismatch; clarify in prose rather than rename again.
- `AAD adaptation and actuation dynamic` — **codex-2:** The rename cost has already been paid; the short form is now compact, distinctive, and good enough to keep.
- `AAD adaptation and actuation dynamic` — **gemini-1:** Recent rename; "Actuation" is slightly imperfect for Section II but further churn dilutes identity. Keep.
- `AAD adaptation and actuation dynamic` — **haiku-4-5:** Recent rename (2026-04-16) from Agentic Cycle Theory. Further churn is expensive; identity is now locked in. The "Actuation" imperfection is real but manageable via a Section II preamble. Do not rename the framework. Keep.
- `AAD adaptation and actuation dynamic` — **opus-4-7-b:** Do not rename. The rename from ACT happened on 2026-04-16 (six months ago at this date); further churn dilutes the identity when the framework is starting to be cited. Any fresh alternative would face the same collision-checking burden that ACT did. **However:** the "Actuation" half is a genuinely weaker fit than "Adaptation" for what Section II covers (Section II is purposeful agency with objectives and strategy; "actuation" in engineering means *mechanical output*). The fix is not a rename but a Section II preamble paragraph that explicitly names "actuation" in AAD's specific sense ("actuated toward an objective" — already in LEXICON Agent-Classes, but needs to be surfaced at Section II preamble level).
- `AAD adaptation and actuation dynamic` — **opus-4-7:** Recent (2026-04-16) rename to resolve the "AI Consciousness Test" collision; further churn dilutes identity. The "Actuation"-vs-Section-II imperfection is a preamble clarification not a rename.
- `AAD adaptation and actuation dynamic` — **sonnet-4-6:** Recent rename (2026-04-16) from ACT; citation velocity is building under the new name. The "Actuation" imperfection noted in the naming-principles file is real (Section II is more about purposeful actuation than mechanical actuation) but the Section II preamble handles it. Further churn would cost more than it gains. Keep.
- `AAD` — **opus-1m:** Recent rename (2026-04-16); further churn dilutes identity. Naming collisions have already narrowed options. The "Actuation" asymmetry is real but handled more cheaply by a Section II preamble clarification.
- `AAD agentic adaptation dynamic` — **gemini-2:** "Actuation" has a strong mechanical engineering flavor that clashes slightly with the teleological/purposeful focus of Section II. "Agentic Adaptation Dynamics" retains the acronym while emphasizing agency.

## 25. `adaptive tempo`

**Alternatives proposed:** `adaptive tempo`, `adaptation rate`

_category: keep × 6, canonicalize × 1, rename × 1_

- `adaptive tempo` — **codex-gpt-5-r2:** Clear, compact, central, and reusable across individual, team, adversarial, and software domains.
- `adaptive tempo` — **gemini-3-1-pro-preview-r2:** Highly memorable, core concept.
- `adaptive tempo` — **haiku-4-5-r2:** The Greek *tempo* is elegant; "adaptive" correctly narrows. The symbol 𝒯 (calligraphic) is load-bearing in notation. Defend.
- `adaptive tempo` — **haiku-4-5:** Rate of useful info acquisition. Self-descriptive, evocative. Keep.
- `adaptive tempo` — **opus-4-7-b:** Keep. "Tempo" is one of AAD's best one-word handles; the slug is short.
- `adaptive tempo` — **sonnet-4-6-r2:** "Adaptive tempo" is AAD's core capacity metric name. It's precise, memorable, and established in prose and NOTATION.md.
- `adaptive tempo` — **sonnet-4-6-r2:** Sometimes appears as "learning rate" (wrong — that's $\eta^\ast$), "correction rate," or "tempo" alone. The canonical name is "adaptive tempo" ($\mathcal{T}$).
- `adaptation rate` — **opus-4-7:** Loses the "rate × quality" compound the tempo metaphor delivers. Reject.

## 26. `agent opacity`

**Alternatives proposed:** `agent opacity`, `emitter opacity`, `strategic opacity`

_category: keep × 8, rename × 3_

- `agent opacity` — **codex-2:** Clean, sayable, and immediately useful in both cooperative and adversarial discussion.
- `agent opacity` — **codex-gpt-5-r2:** Excellent name for observer-side backward predictive uncertainty.
- `agent opacity` — **codex-gpt-5-r2:** Strong subject noun and good dual to observation quality.
- `agent opacity` — **gemini-3-1-pro-preview-r2:** Good descriptive name.
- `agent opacity` — **haiku-4-5:** Adopts Hafez terminology; H_b^{A|B} (backward predictive uncertainty) is dual to observation quality. "Opacity" reads naturally — adversaries want opacity; cooperators want transparency. Name works. Keep.
- `agent opacity` — **opus-4-7:** Fine; "opacity" is the right scalar polarity (emitter side) and has Hafez-lineage citation weight. But see next row.
- `agent opacity` — **sonnet-4-6-r2:** "Agent opacity" is the established term from Hafez et al. 2026, adopted directly. Using the same name as the source is the right move per the prior-art-integration principle.
- `agent opacity` — **sonnet-4-6:** "Opacity" is exactly the right word — backward predictive uncertainty from the observer's perspective. Pairs naturally with "transparency" as the opposite. Keep.
- `emitter opacity` — **opus-4-7:** Disambiguates emitter-side from recipient-side in the 16-cell composition. Parallel with #recipient-regime-classification above.
- `strategic opacity` — **codex-gpt-5-r2:** Too narrow. Opacity matters in cooperative legibility and adversarial concealment; strategic opacity would collapse the dual-use role.
- `strategic opacity` — **gemini-2:** "Agent opacity" is broad. "Strategic opacity" specifically points to the adversarial mechanism of hiding intent.

## 27. `causal information yield`

**Alternatives proposed:** `causal information yield`, `CIY`

_category: keep × 8, canonicalize × 1, add-alias × 1_

- `causal information yield` — **codex-1:** Long, but exact and reusable. The acronym earns its keep because the concept recurs across exploration, querying, and trust.
- `causal information yield` — **codex-2:** Slightly technical, but the phrase is honest and reusable; the `CIY` acronym is tolerable once introduced.
- `causal information yield` — **codex-gpt-5-r2:** Descriptive and central. CIY is useful as abbreviation, but the expanded name should remain canonical.
- `causal information yield` — **codex-gpt-5-r2:** Clear and central.
- `causal information yield` — **gemini-3-1-pro-preview-r2:** Important core concept (CIY).
- `causal information yield` — **haiku-4-5-r2:** Appears as "CIY" (acronym) and as "Causal Information Yield" (full form) throughout OUTLINE.md and NOTATION.md. Commit to the full form in prose; acronym as shorthand only. Currently mixed.
- `causal information yield` — **haiku-4-5:** Self-descriptive compound; reads as "the yield [information gain] from a causal action." Names what it measures. Keep. (CIY abbreviation appears in NOTATION and segments; prose can use full phrase.)
- `causal information yield` — **opus-4-7-r2:** Acceptable keep. "CIY" is well-defined and the alias usage is consistent.
- `causal information yield` — **sonnet-4-6-r2:** CIY is established vocabulary. "Yield" correctly names the information gained from interventions.
- `CIY` — **opus-4-7-r2:** Symbol-to-name alias: $\text{CIY}(a)$ in math; "causal information yield" or "CIY" in prose. The acronym survives the communal-imagination test (acronym discipline check passes — used 10+ times in nearby prose, no obvious AI/ML collisions). Solidify the symbol+acronym pair as a maintained convention.

## 28. `composition closure`

**Alternatives proposed:** `composition closure`, `coarse graining closure`, `closure defect`, `macro agent criterion`

_category: keep × 9, rename × 3, canonicalize × 1, add-alias × 1_

- `composition closure` — **codex-2:** Standard and accurate; not especially vivid, but not a naming problem.
- `composition closure` — **codex-gpt-5-r2:** Central, exact, and aligned with the coarse-graining commutation criterion.
- `composition closure` — **codex-gpt-5-r2:** Central formal name. Do not rename.
- `composition closure` — **gemini-3-1-pro-preview-r2:** Crucial macro/micro mapping concept.
- `composition closure` — **haiku-4-5-r2:** Technical term; the formulation models closure properties. Adequate.
- `composition closure` — **haiku-4-5:** Approximate dynamical homomorphism between micro and macro. "Closure" is precise (mathematical term) but specialist. Acceptable. Current name is tight. Keep.
- `composition closure` — **opus-4-7-r2:** Acceptable keep. "Composition closure" names the load-bearing concept (the closure-defect $\varepsilon^\ast$ as criterion for valid composite-agent status). Could be renamed to "#form-closure-defect" to name the central quantity, but the current form keeps the conceptual move audible.
- `composition closure` — **sonnet-4-6-r2:** "Composition closure" is well-established as the concept; the closure-defect framework lives here.
- `composition closure` — **sonnet-4-6-r2:** Prose uses "composition closure," "compositional closure," and "closure defect framework" somewhat interchangeably. The segment slug is `form-composition-closure` — "composition closure" is the canonical subject-noun.
- `composition closure` — **sonnet-4-6:** Honest but slightly cryptic. "Closure" in the mathematical sense (does the operation stay within the set?) is accurate but has different connotations to a reader from a software background. Weak keep — no obviously better alternative.
- `coarse graining closure` — **codex-1:** The defining move is approximate commutation with coarse-graining. "Composition closure" is too generic to carry that.
- `coarse graining closure` — **codex-gpt-5-r2:** Good explanatory alias because the formal test is approximate commutation with coarse-graining. I would not replace the shorter canonical name.
- `closure defect` — **opus-4-7-r2:** Alternative — names the central derived quantity. The current name names the move. Mild preference for keep.
- `macro agent criterion` — **sonnet-4-6:** Too descriptive, loses the dynamical-systems lineage.

## 29. `auftragstaktik principle`

**Alternatives proposed:** `auftragstaktik principle`, `mission command principle`, `mission command`, `auftragstaktik`, `auftragstaktik bandwidth`, `mission command bandwidth`, `objective first bandwidth principle`, `auftragstaktik drop principle`

_category: keep × 7, rename × 7, add-alias × 2_

- `auftragstaktik principle` — **agent1-original-brainstorm:** Load-bearing term from specific historical tradition; the reader who knows it gets the full intended intuition.
- `auftragstaktik principle` — **gemini-3-1-pro-preview-r2:** Good prior art integration.
- `auftragstaktik principle` — **haiku-4-5:** Prioritize objective sharing. "Auftragstaktik" is German military vocabulary (mission command); borrowed term signals deliberate adoption from organizational theory. Specialist but evocative. Keep.
- `auftragstaktik principle` — **opus-1m:** Load-bearing historical adoption.
- `auftragstaktik principle` — **opus-4-7-r2:** Defended keep — direct adoption from German military doctrine, properly cited; the segment's prior-art trail (Clausewitz, Bungay) is load-bearing. Renaming would lose the doctrinal connection.
- `auftragstaktik principle` — **opus-4-7:** German military lineage name (command-intent autonomy) is doing real work — same reason "directed separation" beat a generic alternative. Keep.
- `auftragstaktik principle` — **sonnet-4-6-r2:** "Auftragstaktik" is the established German military term for mission-type tactics. Adopting it directly (as the prior-art-integration principle requires) makes the hypothesis immediately placeable. The segment Discussion correctly grounds it in Bungay/Clausewitz. Strong keep.
- `mission command principle` — **codex-1:** The current German term is exact but creates unnecessary lookup cost. The English doctrine term keeps the baggage while lowering entry cost.
- `mission command principle` — **codex-gpt-5-r2:** Mission command should be an English alias, not replacement. Auftragstaktik carries the specific historical doctrine that motivates the segment.
- `mission command principle` — **gemini-2:** "Auftragstaktik" is heavy historical baggage, hard to spell, and "Mission Command" is the standard modern translation that conveys the exact same intent.
- `mission command` — **codex-gpt-5-r2:** Add as first-use gloss for accessibility.
- `auftragstaktik` — **opus-4-7-r2:** Confirm: the German term is the canonical noun in prose; "mission-type tactics" or "intent-based command" are the English alternatives. The principle is bilingual in the segment's prior-art treatment; preserve both.
- `auftragstaktik bandwidth` — **codex-gpt-5-r2:** Principle is weak, and bandwidth is the formal allocation subject. However, the German term is intentionally domain-rich, so this is a mild vote.
- `mission command bandwidth` — **codex-gpt-5-r2:** More English and accessible than Auftragstaktik, but loses the historical precision. Acceptable as an alias or fallback.
- `objective first bandwidth principle` — **codex-1:** Accurate-ish but too explanatory and strips away the doctrinal lineage that gives the claim its empirical grounding.
- `auftragstaktik drop principle` — **opus-4-7-b:** Considered dropping "principle" since the word alone is vivid. Reject: "principle" signals this is a design prescription not a derived result, and AAD's scope-honesty discipline rewards that signal. Keep as is.

## 30. `communication gain`

**Alternatives proposed:** `communication gain`, `trust gain`

_category: keep × 8, rename × 1_

- `communication gain` — **codex-1:** Excellent parallel with update gain: short, compositional, and immediately predictive of meaning.
- `communication gain` — **codex-2:** Natural extension of update gain; easy to say and hard to improve.
- `communication gain` — **codex-gpt-5-r2:** Plain and accurate for the inter-agent gain extension.
- `communication gain` — **gemini-3-1-pro-preview-r2:** Good inter-agent extension of update gain.
- `communication gain` — **haiku-4-5:** Trust-weighted update gain for inter-agent channels. Parallel to update-gain machinery; reads naturally. Keep.
- `communication gain` — **opus-4-7-b:** Keep. Exact analog of "update gain" for inter-agent channels — the parallel structure is itself pedagogical.
- `communication gain` — **opus-4-7-r2:** Acceptable keep — names the multi-agent extension of the gain principle.
- `communication gain` — **sonnet-4-6-r2:** "Communication gain" is the inter-agent analog of update gain $\eta^\ast$. The parallel naming is a virtue.
- `trust gain` — **codex-gpt-5-r2:** Trust is a component of communication gain, not the whole quantity. The current name preserves the update-gain parallel.

## 31. `concept the working convention rule of attempting tighter derivation before scope narrowing on apparently overclaimed claim`

**Alternatives proposed:** `strengthen first posture`, `attempt the improbable`, `epistemic strengthening posture`

_category: name-unnamed × 4, canonicalize × 4_

- `strengthen first posture` — **gemini-2:** Actionable, precise, and sets a strong normative engineering principle. Keep. [original phrasing: unnamed: strengthen-first posture]
- `strengthen first posture` — **gemini-targeted-alternatives:** Secures this as a first-class named engineering principle. [original phrasing: unnamed the strengthen before soften work posture]
- `strengthen first posture` — **gemini-targeted-alternatives:** Standardizes the methodological commitment. [original phrasing: unnamed strengthen first posture]
- `strengthen first posture` — **gemini-targeted-alternatives:** Secures the methodological commitment. [original phrasing: unnamed the strengthen first attempt the improbable meta approach to theory development]
- `strengthen first posture` — **gemini-targeted-alternatives:** Solidifies the specific methodological approach. [original phrasing: unnamed the strengthen before soften posture applied to apparent overclaims]
- `strengthen first posture` — **opus-4-7:** Already functionally the name (CLAUDE.md §Working Conventions uses it as a heading). Explicit vote to lock this in as a first-class project methodology name. Adopt as canonical. [original phrasing: unnamed: the "strengthen before soften" work posture]
- `attempt the improbable` — **sonnet-4-6:** CLAUDE.md uses "attempt the improbable" as the better version of "strengthen-first posture." This phrase is memorable and CLAUDE.md says it is "aspirational but less directive" compared to "strengthen-first." For the internal working vocabulary it should be the primary term — it captures the spirit better than "strengthen-first" which sounds procedural. [original phrasing: unnamed: the "strengthen-first, attempt the improbable" meta-approach to theory development]
- `epistemic strengthening posture` — **sonnet-4-6:** CLAUDE.md and MEMORY.md both discuss this as "strengthen-first posture" or "strengthen before softening." The working vocabulary is established; it just doesn't have a single memorable noun. "Strengthening posture" is the current best; it's in CLAUDE.md. [original phrasing: unnamed: the "strengthen-before-soften" posture applied to apparent overclaims]

## 32. `context turnover`

**Alternatives proposed:** `context turnover`, `chronica severance`

_category: keep × 6, add-alias × 1, rename × 1_

- `context turnover` — **codex-1:** Excellent name: short, accurate, and immediately legible to anyone who has worked with LLM agents.
- `context turnover` — **codex-2:** Very strong name: immediate intuition, no wasted motion.
- `context turnover` — **codex-gpt-5-r2:** Strong, concrete logogenic observation.
- `context turnover` — **gemini-3-1-pro-preview-r2:** Perfectly describes the 100% context reset and chronica severance at session boundaries for LLMs.
- `context turnover` — **opus-4-7-r2:** Defended keep — logogenic-agents observation. "Context turnover" is the right name for the 100% session-loss problem; renaming would lose a load-bearing prose convention. The phrase is also widely used in the wider AI-engineering community.
- `context turnover` — **sonnet-4-6-r2:** "Context turnover" is the evocative name for the 100% $M_t$ reset at session boundaries. The term is immediately graspable and memorable in conversation ("the context-turnover problem"). Strong keep.
- `chronica severance` — **codex-gpt-5-r2:** Context turnover is the plain operational name; chronica severance is the AAD-native explanation of why it matters.
- `chronica severance` — **gemini-1:** "Chronica severance" is much more evocative and precise than "context turnover", directly naming the theoretical object that is broken at the session boundary.

## 33. `contraction template`

**Alternatives proposed:** `contraction template`, `contraction schema`

_category: keep × 7, rename × 1_

- `contraction template` — **codex-2:** Crisp and broad enough to survive later reuse.
- `contraction template` — **haiku-4-5:** Contraction-metric generalization of #sector-persistence-template. "Template" parallel emphasizes reusability. Specialist vocabulary (Lohmiller-Slotine contraction analysis) but appropriate. Keep.
- `contraction template` — **opus-4-7-b:** Keep. Parallel to `#sector-persistence-template` — the family-by-pattern naming is consistent.
- `contraction template` — **opus-4-7-r2:** Defended keep. Pairs with `#result-sector-persistence-template` as the second template-result in the framework (Lohmiller-Slotine generalization). The dual templates compose as a meta-architecture.
- `contraction template` — **opus-4-7:** Natural name, Lohmiller-Slotine lineage, aligns with the sibling #sector-persistence-template. Keep.
- `contraction template` — **sonnet-4-6-r2:** Parallel to sector-persistence-template. The parallelism is a virtue.
- `contraction template` — **sonnet-4-6:** Parallel to #sector-persistence-template. The pair names the two levels of the hierarchy clearly. Keeps the template-series coherent. Keep.
- `contraction schema` — **gemini-3-1-pro-preview-r2:** "Schema" aligns better with formal theoretical frameworks than "template".

## 34. `deliberation cost`

**Alternatives proposed:** `deliberation cost`, `deliberation threshold`, `think vs act tradeoff`, `deliberation drag`

_category: keep × 8, rename × 3_

- `deliberation cost` — **codex-gpt-5-r2:** Direct and memorable enough for the pause-versus-action threshold.
- `deliberation cost` — **gemini-2:** Self-descriptive and conceptually clear.
- `deliberation cost` — **gemini-3-1-pro-preview-r2:** Excellent self-descriptive term for pausing praxis to improve upcoming epistrophe.
- `deliberation cost` — **haiku-4-5-r2:** The subject-noun directly names what is derived. No improvement available.
- `deliberation cost` — **haiku-4-5:** Think vs. act tradeoff. Reads naturally as cost-benefit. Keep.
- `deliberation cost` — **opus-4-7-b:** Keep. "Cost" signals tradeoff cleanly.
- `deliberation cost` — **opus-4-7-r2:** Defended keep. "Deliberation cost" names exactly what the segment derives (the think-vs-act tradeoff under mismatch drift). The discussion segment `#disc-exploit-explore-deliberate` extends it. Renaming would break a clean two-segment naming compound.
- `deliberation cost` — **sonnet-4-6-r2:** "Deliberation cost" names the think-vs-act tradeoff precisely.
- `deliberation threshold` — **audit-471203-incremental:** The standard term obscures the AAD-distinctive content (the threshold itself, not the cost). "Deliberation cost" sounds like a measurement; "Deliberation Threshold" surfaces the operational use. [from 24-der-deliberation-cost.md] [one of 2 alternatives proposed in the original audit row]
- `think vs act tradeoff` — **audit-471203-incremental:** The standard term obscures the AAD-distinctive content (the threshold itself, not the cost). "Deliberation cost" sounds like a measurement; "Deliberation Threshold" surfaces the operational use. [from 24-der-deliberation-cost.md] [one of 2 alternatives proposed in the original audit row]
- `deliberation drag` — **gemini-1:** "Cost" sounds like a generic penalty in an objective function. "Drag" evokes the physical accumulation of mismatch over time while pausing.

## 35. `observability dominance`

**Alternatives proposed:** `observability dominance`, `epistemic freezing`

_category: keep × 10, canonicalize × 1, rename × 1_

- `observability dominance` — **codex-2:** Slightly formal, but it says what the regime claim actually is.
- `observability dominance` — **codex-gpt-5-r2:** Strong name for the fact that unobservable strategy edges are epistemically dead regardless of nominal confidence.
- `observability dominance` — **gemini-1:** Accurately descriptive of the freezing effect on unobservable edges.
- `observability dominance` — **gemini-2:** Strong, clear principle.
- `observability dominance` — **gemini-3-1-pro-preview-r2:** Commit to this term for "unobservable strategy edges freeze".
- `observability dominance` — **haiku-4-5-r2:** The derived claim is about the dominance pattern; subject-noun is exact.
- `observability dominance` — **haiku-4-5:** Unobservable edges freeze. Evocative; reads naturally. (Already proposed in LEXICON; ready for segment promotion.) Keep.
- `observability dominance` — **opus-4-7-b:** Keep. "Dominance" here is informational dominance — the gain principle *dominates* the edge update when observability is low. Does its job.
- `observability dominance` — **opus-4-7-b:** Keep. The word *dominance* here is technically precise (information-theoretic dominance) and the phrase has two-word memorability.
- `observability dominance` — **opus-4-7-r2:** Acceptable keep. "Observability dominance" names the load-bearing result (unobservable edges freeze in the credit-assignment update) and connects to control-theoretic observability vocabulary. The LEXICON's "Terms to Be Added" already has an entry for this; the slug matches.
- `observability dominance` — **sonnet-4-6-r2:** "Observability dominance" is evocative and accurate — observability dominates nominal confidence. The Discussion's absorbing-state analysis makes the name feel exactly right. Strong keep.
- `epistemic freezing` — **gemini-2:** If unobservable edges freeze, "epistemic freezing" is a more vivid description of the consequence.

## 36. `pearl causal hierarchy`

**Alternatives proposed:** `pearl causal hierarchy`, `causal hierarchy`, `no alternative`

_category: keep × 7, rename × 1_

- `pearl causal hierarchy` — **agent1-original-brainstorm:** Adopted concept; prior-art-integration convention forbids rename.
- `pearl causal hierarchy` — **gemini-3-1-pro-preview-r2:** Established literature term; do not change.
- `pearl causal hierarchy` — **haiku-4-5:** Pearl's three levels of causal reasoning. Names the origin; accurate. Keep.
- `pearl causal hierarchy` — **opus-1m:** Adopted concept; keep attribution per prior-art-integration convention.
- `pearl causal hierarchy` — **opus-4-7-r2:** Defended keep. Direct adoption from Pearl with proper attribution; renaming would lose provenance and create a NIH-syndrome alternative.
- `pearl causal hierarchy` — **sonnet-4-6-r2:** External vocabulary adopted with proper citation. "Pearl's causal hierarchy" is the field-standard name; adopting it directly is correct under the project's prior-art-integration principle.
- `causal hierarchy` — **gemini-2:** Dropping "Pearl" removes the specific historical baggage while keeping the structural concept.
- `no alternative` — **opus-targeted-alternatives-v2:** Same — adopted external concept. The single-arch [opus] +6 vote stands; the prior-art-integration convention forbids rename, and I have no honest alternative.

## 37. `team persistence`

**Alternatives proposed:** `team persistence`

_category: keep × 8_

- `team persistence` — **codex-1:** Strong keep: plain-language, memorable, and exactly the right level of abstraction.
- `team persistence` — **codex-2:** Extremely good public noun for a key multi-agent claim.
- `team persistence` — **codex-gpt-5-r2:** Clear segment name. It reads naturally as the cooperative counterpart to adversarial destabilization.
- `team persistence` — **codex-gpt-5-r2:** Direct and useful.
- `team persistence` — **haiku-4-5:** Composite persistence condition. Self-descriptive; reads as "what makes a team persist." Keep.
- `team persistence` — **opus-4-7-b:** Keep. Good plain English for what the derivation is ("cooperative composite sector condition").
- `team persistence` — **opus-4-7-r2:** Acceptable keep. Parallels persistence-condition naming; "team persistence" reads naturally for the cooperative composite case.
- `team persistence` — **sonnet-4-6-r2:** "Team persistence" correctly names the composite persistence condition. The "team" framing is immediately graspable.

## 38. `credit assignment boundary`

**Alternatives proposed:** `credit assignment boundary`, `credit assignment frontier`

_category: keep × 7, canonicalize × 1_

- `credit assignment boundary` — **codex-gpt-5-r2:** Strong name for the tractability frontier in strategy DAG updates.
- `credit assignment boundary` — **gemini-2:** Clearly delineates tractable from intractable. Keep.
- `credit assignment boundary` — **gemini-3-1-pro-preview-r2:** Important concept.
- `credit assignment boundary` — **haiku-4-5:** Tractable/intractable boundary; design requirement. Specialist vocabulary (credit assignment problem is classical in RL) but load-bearing. Keep.
- `credit assignment boundary` — **opus-4-7-b:** Keep. The "boundary" is semantically exactly what the segment delimits (tractable vs. intractable credit-assignment regions).
- `credit assignment boundary` — **opus-4-7-r2:** Defended keep. "Boundary" is doing real work: the segment characterizes the *line* between tractable and intractable credit assignment, not credit assignment itself. The name signals the meta-segment posture. The segment is also the canonical entry point for the boundary in downstream prose.
- `credit assignment boundary` — **sonnet-4-6-r2:** Precise two-word noun. The boundary is exactly what this segment names — the tractable/intractable boundary for credit assignment. Survives the test.
- `credit assignment frontier` — **opus-4-7-r2:** Distinct from the slug — in prose the segment is sometimes referenced as "the credit-assignment problem" or "the tractable/intractable boundary" or "the attribution boundary." Standardize on "credit-assignment boundary" everywhere; do not paraphrase. Slug stays as-is.

## 39. `honesty as architecture`

**Alternatives proposed:** `honesty as architecture`, `honesty`, `architectural scope honesty`

_category: keep × 4, canonicalize × 3, rename × 2_

- `honesty as architecture` — **codex-1:** Hyphen-heavy, but uniquely exact. The phrase says the limits are part of the construction, not editorial cleanup.
- `honesty as architecture` — **codex-2:** Strong internal principle name; it sounds like a thesis, not a slogan.
- `honesty as architecture` — **codex-gpt-5-r2:** Hyphen-heavy but exact. It names a distinctive project commitment, not just a style preference.
- `honesty as architecture` — **haiku-4-5:** Central to CLAUDE.md's "Epistemic architecture as AAD's distinctive contribution" principle. Already in project vocabulary as a narrative-level principle; no need to formalize as a segment. Keep the current form.
- `honesty as architecture` — **opus-1m:** CLAUDE.md §7 element (a). Working term; keep.
- `honesty as architecture` — **opus-4-7-b:** The hyphens signal "this is a concept-name, not a description" — useful in CLAUDE.md but awkward in running prose. Proposal: keep the hyphenated form only in CLAUDE.md §7 and README §reading-AAD where it is a named concept; use unhyphenated "scope honesty" in segment-level prose.
- `honesty as architecture` — **sonnet-4-6:** Already coined and working. Appears in CLAUDE.md and multiple segments. The compound noun is memorable and the hyphenation is correct (it's an adjectival phrase). Keep.
- `honesty` — **sonnet-4-6-r2:** "Scope-honesty-as-architecture" is the CLAUDE.md §7 label. Prose uses "scope honesty," "honest scope," and "scope-honesty commitment" variably. Standardize on "scope honesty" as the two-word prose form; "scope-honesty" as the slug or hyphenated compound.
- `architectural scope honesty` — **codex-1:** Slightly cleaner in prose while preserving the key point that scope is surfaced structurally.

## 40. `approximation tiering`

**Alternatives proposed:** `approximation tiering`, `tiered approximation`, `approximation ladder`, `scope laddering`, `graceful degradation`, `tier ascension`

_category: keep × 8, rename × 5_

- `approximation tiering` — **codex-gpt-5-r2:** Tiering is the actual subject. Good.
- `approximation tiering` — **gemini-3-1-pro-preview-r2:** Accurate.
- `approximation tiering` — **haiku-4-5:** Meta-pattern for tractability-indexed hierarchies (L0/L1/L2; C1/C2/C3; Tier 1/2/3). Self-descriptive. Reads naturally when discussing graceful degradation. Keep.
- `approximation tiering` — **opus-4-7-b:** Keep. Already avoids the "hierarchy" overload; "tiering" is the right word.
- `approximation tiering` — **opus-4-7-r2:** Acceptable keep. "Tiering" reads slightly clinical but it's accurate (the four-component (AT1)–(AT4) structure does name a *tiering*, not a continuum or a hierarchy). I considered #disc-graceful-degradation but graceful-degradation is one property among the four, not the whole pattern.
- `approximation tiering` — **opus-4-7:** Fine but generic — keep unless a better name emerges, since the AT1/AT2/AT3/AT4 component scheme has already landed.
- `approximation tiering` — **sonnet-4-6-r2:** "Tiering" is accurate and distinctive. The pattern it names IS about tiered approximations with monotonicity. Passes the communal-imagination test.
- `approximation tiering` — **sonnet-4-6:** "Tiering" is precise — it names the operation (creating tiers) not just the result (tiers). Self-describing for a meta-pattern. Keep.
- `tiered approximation` — **codex-1:** Slight improvement in natural-language flow. The current phrase is serviceable but abstract.
- `approximation ladder` — **codex-2:** Noun beats gerund here; "ladders" is easier to say alongside the segment's own ladder language.
- `scope laddering` — **opus-4-7-r2:** If the project lands "ladder" as a distinguished term for tiered-with-monotonicity-and-ascension structures, this would be a fit. Lower priority than the existing keep.
- `graceful degradation` — **opus-4-7-r2:** Considered and rejected — graceful-degradation is (AT3) only; tiering is the whole thing.
- `tier ascension` — **opus-4-7:** Reads like a ranked-climbing metaphor the segment does not actually use. Reject.

## 41. `concept the failure mode where η → 0 freez learning in either of two distinguishable mode low u o vs high u o`

**Alternatives proposed:** `gain collapse`, `epistemic gain collapse`, `dogmatic convergence limit`, `epistemic gridlock`, `epistemic death`, `competency trap`, `stability induced myopia`, `the nihilism trap`, `update calcification`, `observation ambiguity freeze`, `certainty trap`, `eta collapse`, `learning freeze`

_category: canonicalize × 9, name-unnamed × 5, rename × 4, add-alias × 3_

- `gain collapse` — **codex-gpt-5-r2:** Strong unifying name for dogmatism-like and nihilism-like failures of update gain. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]
- `gain collapse` — **gemini-3-1-pro-preview-r2:** The shared mathematical mechanism for dogmatism and nihilism. [original phrasing: unnamed: the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning]
- `gain collapse` — **gemini-targeted-alternatives:** Defended canonicalization of the exact AAD mechanism for this freeze. [original phrasing: unnamed the gain collapse failure when both u m → 0 and u o → ∞]
- `gain collapse` — **opus-4-7-r2:** New alternative — Gemini coined this in the synthesized-additions pass and tagged it +3 canonicalize, but the *cold-start* peers didn't reach it. I think the term is excellent (η* → 0 has two distinct mechanistic origins: dogmatism U_M → 0, nihilism U_o → ∞) and deserves a first-class entry. The shared-mechanism naming captures what makes the result distinctive: the *same* failure-mode arises from opposite epistemic postures. Promote and canonicalize. [original phrasing: unnamed: the gain-collapse failure when both U_M → 0 and U_o → ∞]
- `gain collapse` — **opus-targeted-alternatives-v2:** Per `#der-gain-sector-bridge` Failure Mode 2: "Gain collapse: $\eta^\ast \to 0$ while $\rho \gt 0$, so $\alpha \to 0$ and the persistence condition eventually fails." The segment's *named failure mode* is "gain collapse." Confirms across architectures. The current row is a description; the segment-name is the alternative. [original phrasing: learning freeze from low U_M or high U_o]
- `gain collapse` — **opus-targeted-alternatives:** Per `#der-gain-sector-bridge` Failure Mode 2: "Gain collapse: $\eta^\ast \to 0$ while $\rho > 0$, so $\alpha \to 0$ and the persistence condition eventually fails." This is the *named* failure mode in the segment — "gain collapse" — and it covers both halves of the disjunction (low $U_M$ → low $\eta^\ast$; high $U_o$ → low $\eta^\ast$). Stronger rename than canonicalize. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]
- `epistemic gain collapse` — **gemini-targeted-alternatives:** Already heavily referenced as "gain collapse". Adding "epistemic" clarifies it's the update gain dropping to near 0. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]
- `epistemic gain collapse` — **gemini-targeted-alternatives:** Unifies this with the generic gain collapse terminology. [original phrasing: unnamed the state where credit assignment collapses and learning freezes]
- `dogmatic convergence limit` — **gemini-targeted-alternatives:** Names the state where $U_M \to 0$ without a noise injection term. [original phrasing: unnamed the mathematical limit of bayesian learning without forgetting]
- `dogmatic convergence limit` — **gemini-targeted-alternatives:** Names the state where update stops purely from objective certainty. [original phrasing: unnamed the specific moment when $\eta^st 	o 0$ because $U_o 	o 0$ too certain rather than because $U_M 	o 0$ model confident]
- `epistemic gridlock` — **gemini-targeted-alternatives:** Vividly captures the "freeze" aspect where learning stops entirely despite ongoing mismatch signals. [original phrasing: unnamed the gain collapse failure when both u m → 0 and u o → ∞]
- `epistemic gridlock` — **gemini-targeted-alternatives:** Identifies the specific double-failure mode of gain collapse. [original phrasing: unnamed the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning]
- `epistemic death` — **gemini-3-1-pro-preview-r2:** Vividly captures the organizational or agentic consequence of unobservable DAGs. [original phrasing: unnamed: the state where credit assignment collapses and learning freezes]
- `competency trap` — **gemini-3-1-pro-preview-r2:** Formalizes "institutional rigidity" as an inevitable result of $\eta^\ast \to 0$. [original phrasing: unnamed: the mathematical limit of Bayesian learning without forgetting]
- `stability induced myopia` — **gemini-targeted-alternatives:** Retains the descriptive alias for success-driven failure. [original phrasing: gemini s competency trap for $\eta^st 	o 0$]
- `the nihilism trap` — **gemini-3-1-pro-preview-r2:** Dogmatism's opposite, where learning stops because everything is meaningless. [original phrasing: unnamed: $U_o \to \infty$ freezing the learning rate]
- `update calcification` — **gemini-targeted-alternatives:** Good prose handle for the failure mode where the model stops taking in new info. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]
- `observation ambiguity freeze` — **gemini-targeted-alternatives:** Describes the nihilistic failure mode of gain collapse. [original phrasing: unnamed $U_o \to \infty$ freezing the learning rate]
- `certainty trap` — **sonnet-4-6-r2:** Gemini proposed "competency trap" for $\eta^\ast \to 0$ under high $U_o$, but that term imports different connotations (being too good at the wrong thing). The mechanism is that excessive certainty about observations ($U_o \to 0$) freezes the update gain in exactly the same way as full model certainty — a trap specifically from certainty, not from competence. "Certainty trap" is more scope-honest than Gemini's "competency trap." New candidate; engages Gemini's vote explicitly. [original phrasing: unnamed: the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ (too-certain) rather than because $U_M \to 0$ (model-confident)]
- `eta collapse` — **opus-targeted-alternatives-v2:** Symbol-anchored alternative. Names the formal quantity collapsing ($\eta^\ast$). Weaker because $\eta$ is the update gain (not the persistence margin); the failure mode includes the cascade $\eta \to 0 \Rightarrow \alpha \to 0$. "Gain collapse" names the cause; "eta-collapse" is one step in the cascade. [original phrasing: learning freeze from low U_M or high U_o]
- `learning freeze` — **opus-targeted-alternatives:** The current is a description; the segment's actual phenomenon-name (per `#emp-update-gain` and `#disc-identifiability-floor`) is the gain-collapse dynamic when $U_M \to 0$ or $U_o \to \infty$. "Learning freeze" is the phenomenon; the rest is the disambiguation. Canonicalize to the noun-phrase form. [original phrasing: learning freeze from low model uncertainty or high observation uncertainty]

## 42. `recursive update`

**Alternatives proposed:** `recursive update`, `recursive update by completeness`

_category: keep × 7, rename × 1_

- `recursive update` — **haiku-4-5-r2:** The subject-noun "recursive update" is exact — the derivation forces the update to be recursive. No change needed.
- `recursive update` — **haiku-4-5:** State updates must be recursive. "Recursive" is specialist (implies function composition) but appropriate. Keep.
- `recursive update` — **opus-4-7-b:** Keep. AAD's strongest result ("three constraints → unique recursive form") deserves its direct, clean name. Do not touch.
- `recursive update` — **opus-4-7-r2:** Defended keep. This is one of the inevitability-core segments; "recursive update" is the right name for what the three constraints uniquely force.
- `recursive update` — **opus-4-7:** Strongest inevitability-core result; three-constraint uniqueness derivation. Keep.
- `recursive update` — **sonnet-4-6-r2:** "Recursive update" is technically precise — the derivation shows state updates must be recursive.
- `recursive update` — **sonnet-4-6:** Clean, accurate, non-overloaded. Exactly describes what the segment proves (state updates must be recursive). Keep.
- `recursive update by completeness` — **audit-471203-incremental:** Title currently understates the distinctive Markov-by-definition move. Auditor: the distinctive content is *"the recursive form is forced by what we mean by $M_t$"* — surface this in the name. [from 15-der-recursive-update.md]

## 43. `agent identity`

**Alternatives proposed:** `agent identity`, `identity as singular causal trajectory`, `the trajectory identity scope`, `singular causal trajectory`, `trajectory identity`, `causal identity`

_category: keep × 6, rename × 5_

- `agent identity` — **gemini-3-1-pro-preview-r2:** Crucial scope definition.
- `agent identity` — **haiku-4-5-r2:** Clean scope statement; the subject-noun is clear.
- `agent identity` — **haiku-4-5:** Formal scope claim naming token-level commitment (agents on singular, non-forkable trajectories). Short, memorable. Reads naturally in "agent-identity token-level commitment" context. Keep.
- `agent identity` — **opus-4-7-r2:** Defended keep. The segment's substance is the singular-causal-trajectory commitment grounding agent identity — "agent identity" is the right slug-noun. Renaming would lose the LEXICON's "continuity persistence" connection.
- `agent identity` — **opus-4-7:** Surfaced 2026-04-22 as a formal scope commitment; name carries the token-level commitment honestly. Now (PI) sits here. Keep.
- `agent identity` — **sonnet-4-6-r2:** Perfect fit of name to content — the segment scopes AAD to agents on singular causal trajectories, and "agent identity" (identity = singular causal trajectory) is exactly the concept.
- `identity as singular causal trajectory` — **audit-471203-incremental:** "Slug-as-mechanical-prefix hides the substantive claim." The segment is structurally important for the framework's identity-and-continuity claims (esp. for consciousness-infrastructure substrate-independence work) and the title gloss is closer to what it actually does than the slug. Auditor felt the friction acutely: "single most important §I segment for the broader project's purposes." [from 30-scope-agent-identity.md] [one of 2 alternatives proposed in the original audit row]
- `the trajectory identity scope` — **audit-471203-incremental:** "Slug-as-mechanical-prefix hides the substantive claim." The segment is structurally important for the framework's identity-and-continuity claims (esp. for consciousness-infrastructure substrate-independence work) and the title gloss is closer to what it actually does than the slug. Auditor felt the friction acutely: "single most important §I segment for the broader project's purposes." [from 30-scope-agent-identity.md] [one of 2 alternatives proposed in the original audit row]
- `singular causal trajectory` — **codex-gpt-5-r2:** The segment's identity condition is the singular trajectory, and that subject is more distinctive than agent identity.
- `trajectory identity` — **codex-2:** The segment's formal content is about trajectory singularity; "agent identity" invites more metaphysical baggage than the math supports.
- `causal identity` — **gemini-2:** "Agent identity" is very soft. "Causal identity" anchors it strictly to the non-forkable causal trajectory.

## 44. `aporia`

**Alternatives proposed:** `aporia`, `aporia productive perplexity`, `discrepancy`

_category: keep × 5, add-alias × 1, rename × 1_

- `aporia` — **agent1-original-brainstorm:** Cycle-phase Greek vocabulary works aesthetically AND technically. The risk is preciousness; the payoff is memorable sequence.
- `aporia` — **codex-1:** This earns its weight. "Error" and "mismatch" lose the productive-perplexity sense that makes the term memorable and accurate.
- `aporia` — **codex-2:** Memorable, discussable, and conceptually richer than "error" or "mismatch."
- `aporia` — **codex-gpt-5-r2:** Excellent fit for productive mismatch or perplexity. It already carries the right philosophical resonance.
- `aporia` — **opus-targeted-alternatives:** `LEXICON.md`: "Productive perplexity: mismatch signal $\delta_t = o_t - \hat{o}_t$." The Greek term is doing work that "mismatch signal," "prediction error," and "surprise" all miss — *productive* perplexity, the kind that *drives* update rather than degrading it. Aporia in the Platonic sense is the moment of recognized not-knowing that motivates inquiry. The segment's $\delta_t$ is more than an error term; it is the agent's epistemic engine. Keep at +3 across architectures.
- `aporia productive perplexity` — **gemini-targeted-alternatives:** Explicitly adding this translation ensures "perplexity" is seen as generative.
- `discrepancy` — **opus-targeted-alternatives:** Considered. Names the gap but loses the agent-centered "this matters / I now must update" sense. Rejected.

## 45. `concept the self reinforcing positive feedback loop linking m t quality and σ t evaluable complexity TST specific and AAD general form`

**Alternatives proposed:** `quality tempo compound effect`, `comprehension flywheel`, `quality tempo spiral`, `virtuous vicious quality cycle`, `model strategy coupling`

_category: canonicalize × 4, name-unnamed × 4, rename × 2_

- `quality tempo compound effect` — **gemini-targeted-alternatives:** Formally identifies the feedback loop between code quality and developer adaptive tempo. [original phrasing: code quality and tempo positive feedback]
- `quality tempo compound effect` — **gemini-targeted-alternatives:** Aligns with the previously renamed code-quality dynamic. [original phrasing: quality to tempo chain]
- `quality tempo compound effect` — **gemini-targeted-alternatives:** Standardizes the code-quality feedback loop mechanism. [original phrasing: unnamed the self reinforcing code quality → tempo loop]
- `quality tempo compound effect` — **gemini-targeted-alternatives:** Maps the mastery phenomenon to the formal tempo feedback loop. [original phrasing: unnamed master developers writing clean code in the same time as messy code]
- `quality tempo compound effect` — **gemini-targeted-alternatives:** Reaffirms the core feedback loop coupling code to agency. [original phrasing: unnamed the virtuous vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity]
- `comprehension flywheel` — **codex-2:** The loop recurs enough in discussion that it deserves a shorter noun than "vicious/virtuous cycle" each time. [original phrasing: unnamed: the self-reinforcing code-quality → tempo loop]
- `comprehension flywheel` — **codex-gpt-5-r2:** Good positive-loop counterpart to quality-tempo spiral. Use flywheel for virtuous accumulation, spiral for both directions. [original phrasing: code-quality and tempo positive feedback]
- `quality tempo spiral` — **codex-gpt-5-r2:** Good TST name for virtuous or vicious code-quality dynamics. [original phrasing: code-quality feedback loop through tempo]
- `virtuous vicious quality cycle` — **gemini-targeted-alternatives:** Names the specific bifurcation dynamic driven by the quality-tempo compound effect. [original phrasing: code quality feedback loop through tempo]
- `model strategy coupling` — **sonnet-4-6:** #orient-cascade Discussion names the virtuous and vicious cycles explicitly but without a name for the coupling phenomenon itself. "Model-strategy coupling" would let segments say "the model-strategy coupling prevents meaningful evaluation of complex strategies under poor model sufficiency." [original phrasing: unnamed: the virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity]

## 46. `consolidation dynamic`

**Alternatives proposed:** `consolidation dynamic`, `offline consolidation`

_category: keep × 9, rename × 1_

- `consolidation dynamic` — **codex-gpt-5-r2:** Strong name for between-event replay or pseudo-event updates toward IB-optimal compression.
- `consolidation dynamic` — **gemini-3-1-pro-preview-r2:** Evocative.
- `consolidation dynamic` — **haiku-4-5-r2:** The formulation models offline learning as "consolidation." Adequate metaphorical naming.
- `consolidation dynamic` — **haiku-4-5:** Offline regime of between-event M_t dynamics; "consolidation" reads naturally (consolidating learned structure). Captures the sense of replay-driven model tightening. Acceptable name. Keep.
- `consolidation dynamic` — **opus-4-7-b:** Keep. "Consolidation" imports the neuroscience baggage (memory consolidation, stability-plasticity) that's precisely what the segment is formalizing.
- `consolidation dynamic` — **opus-4-7-r2:** Acceptable keep. The segment names the offline regime of $g_M$ (replay-driven consolidation); "consolidation dynamics" is engineering-vocabulary that travels well.
- `consolidation dynamic` — **opus-4-7:** Fine. Inherits "consolidation" from neuroscience (memory consolidation). Keep unless a sharper name emerges.
- `consolidation dynamic` — **sonnet-4-6-r2:** "Consolidation dynamics" names the offline replay / stability-plasticity regime. Acceptable.
- `consolidation dynamic` — **sonnet-4-6:** "Consolidation" is established biological vocabulary for offline memory reorganization. Using it positions the theoretical result in a recognizable lineage. The "dynamics" suffix is accurate. Keep.
- `offline consolidation` — **gemini-2:** Adding "offline" explicitly scopes the regime to replayed/pseudo-events.

## 47. `critical mass composition`

**Alternatives proposed:** `critical mass composition`, `dyad closed form`

_category: keep × 6, rename × 1_

- `critical mass composition` — **codex-1:** Vivid and mathematically honest: a threshold at which composition starts to persist. Strong keep.
- `critical mass composition` — **codex-gpt-5-r2:** Useful result name for composite persistence thresholds.
- `critical mass composition` — **haiku-4-5:** Physics-borrowed vocabulary; "critical mass" is evocative and memorable. The segment derives the composite sector constant; readers will understand "critical mass" as the composition threshold. Strong name. Keep.
- `critical mass composition` — **opus-4-7-b:** Keep. "Critical mass" is exactly right — the composite-sector-constant derivation has a minimum-viable-composition threshold that matches the physics / sociology intuition. Rare case where the name upgrades the result's punch.
- `critical mass composition` — **opus-4-7:** Alternative keep-vote: "critical mass" has intuitive pickup for the threshold nature of composition viability. Content-neutral; reader decides.
- `critical mass composition` — **sonnet-4-6:** "Critical mass" is physics vocabulary with intuitive resonance — the composite persists above it, collapses below it. Memorable and evocative without being cute. Keep.
- `dyad closed form` — **opus-4-7:** "Critical mass" suggests emergence-above-threshold but the segment derives a closed-form composite sector constant for the symmetric-matched-Tier-1 dyad. Honest label.

## 48. `exploit explore deliberate`

**Alternatives proposed:** `exploit explore deliberate`, `cycle budget allocation`, `action timing tradeoff`, `cycle budget`

_category: keep × 6, rename × 4_

- `exploit explore deliberate` — **agent1-original-brainstorm:** Third term sits neatly beside two standard-vocabulary terms; reads as extension not reinvention.
- `exploit explore deliberate` — **haiku-4-5:** Three-way exploit/explore/deliberate. Already named and acceptable. Keep.
- `exploit explore deliberate` — **opus-1m:** Three-way extension of two established terms; reads naturally.
- `exploit explore deliberate` — **opus-4-7-b:** Keep. The three-way extension of the classic exploit-explore dichotomy reads as a natural extension *because* of how the slug is named. Changing this would cost the pedagogical payoff.
- `exploit explore deliberate` — **opus-4-7:** Three-way decomposition is itself the content. Triadic name matches triadic claim. Keep.
- `exploit explore deliberate` — **sonnet-4-6-r2:** Three-way distinction is load-bearing in the name. Any shortening loses the three-way structure. Passes the communal-imagination test ("the exploit-explore-deliberate discussion").
- `cycle budget allocation` — **codex-gpt-5-r2:** The current verb triad is memorable but underspecified. The segment is about allocating the cycle budget across modes.
- `cycle budget allocation` — **opus-4-7-r2:** Confirmation with new reasoning — Codex proposed this at +2 with the rationale that the verb triad is underspecified. I'd vote +1 (weaker than Codex's +2) because the verb triad is more memorable than "cycle-budget-allocation" but less precise. The rename surfaces the *resource-allocation* nature of the tradeoff, which is what the formal segment derives. Mild support; would not push hard against keep.
- `action timing tradeoff` — **gemini-3-1-pro-preview-r2:** Names the overarching tradeoff rather than listing the mechanistic components.
- `cycle budget` — **sonnet-4-6-r2:** Codex proposed `disc-cycle-budget-allocation` (+2) for this segment; I had voted keep (+2). Reading Codex's reasoning ("the segment is about allocating the cycle budget across modes") crystallized a new alternative: `disc-cycle-budget` drops "allocation" (which is role-like) and leaves a two-word noun that survives the communal-imagination test. Shorter than Codex's candidate; equally scope-honest. Neither Codex's nor my original vote.

## 49. `gain sector bridge`

**Alternatives proposed:** `gain sector bridge`, `bridge theorem from gain to sector`, `the bridge theorem`, `grounding ga 3 sub scope α and β`

_category: keep × 7, rename × 3_

- `gain sector bridge` — **agent1-original-brainstorm:** Technical-clinical but does the job. Not worth a rename; concept is narrow enough.
- `gain sector bridge` — **gemini-3-1-pro-preview-r2:** Good name for a bridge concept.
- `gain sector bridge` — **haiku-4-5-r2:** The "bridge" metaphor is apt (connecting two mathematical regimes). Adequate name.
- `gain sector bridge` — **haiku-4-5:** Gain + directional fidelity → sector condition. Compound name; descriptive. Acceptable. Keep.
- `gain sector bridge` — **opus-4-7-r2:** Defended keep. The segment bridges $\eta^\ast$ (gain) to the sector-condition $\alpha$, exactly. "Bridge" is doing work — naming the bridge segment by its function (it bridges) is fine because the function is what makes the segment load-bearing.
- `gain sector bridge` — **sonnet-4-6-r2:** "Gain-sector bridge" is precise — it bridges the gain principle to the sector condition via directional fidelity. Good name.
- `gain sector bridge` — **sonnet-4-6:** The "bridge" metaphor is load-bearing and accurate — it connects two distinct mathematical objects (gain principle and sector condition). Readable aloud. Keep.
- `bridge theorem from gain to sector` — **audit-471203-incremental:** Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title. [from 25-der-gain-sector-bridge.md] [one of 3 alternatives proposed in the original audit row]
- `the bridge theorem` — **audit-471203-incremental:** Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title. [from 25-der-gain-sector-bridge.md] [one of 3 alternatives proposed in the original audit row]
- `grounding ga 3 sub scope α and β` — **audit-471203-incremental:** Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title. [from 25-der-gain-sector-bridge.md] [one of 3 alternatives proposed in the original audit row]

## 50. `loop interventional access`

**Alternatives proposed:** `loop interventional access`, `loop as causal engine`, `loop causal engine`, `interventional loop access`, `interventional feedback`, `adaptive loop access`, `loop level2 access`

_category: keep × 9, rename × 6_

- `loop interventional access` — **codex-gpt-5-r2:** Good name for action-generated Level-2 data.
- `loop interventional access` — **haiku-4-5-r2:** The subject-noun "loop-interventional-access" (hyphenated compound) is exact — the loop grants access.
- `loop interventional access` — **haiku-4-5-r2:** [observation, not a name-unnamed vote]: Auditor surfaced this concept as "unnamed" but Haiku notes it is already named as #der-loop-interventional-access. The concept and its name are settled; the original phrasing was a question-shaped name-unnamed vote that recognized the existing name. [original row: "[unnamed: the mechanism by which an agent uses the feedback loop to gain interventional access to causal structure] | 'loop-as-intervention' or (is this #der-loop-interventional-access?) | name-unnamed | +0"]
- `loop interventional access` — **haiku-4-5:** Three modes of access (agent-self / observer-on-sub-agent / observer-on-input). "Loop-interventional" is specialist but precise — it names *where* the intervention happens (within the feedback loop). Acceptable. Keep.
- `loop interventional access` — **opus-4-7-b:** Keep. The phrase *loop-interventional-access* lands in one read and the concept ("the feedback loop provides Level-2 data by construction") has no shorter form without loss. Reader-friendly.
- `loop interventional access` — **opus-4-7-r2:** Acceptable keep if the rename above doesn't land. "Interventional access" is precise; "causal engine" is more memorable.
- `loop interventional access` — **opus-4-7:** Names the distinctive Pearl-Level-2-by-construction move; the segment is load-bearing for both #identifiability-floor and #agent-identity. Don't touch.
- `loop interventional access` — **sonnet-4-6-r2:** "Loop-interventional access" names the key insight: the feedback loop provides Level-2 data by construction. The "loop" prefix grounds the source.
- `loop interventional access` — **sonnet-4-6:** Accurate but a mouthful. The intended quick-reference name in conversation is probably "the loop's Level 2 access" or "loop as Level 2 engine" — neither of which is a slug. Mild friction.
- `loop as causal engine` — **opus-4-7-r2:** The current name describes the *result* (the loop provides interventional access). "Loop as causal engine" is the framing the README and segment Discussion both reach for, and it surfaces what makes this result distinctive — the agent-environment loop *generates* Pearl-Level-2 data by construction. The README explicitly names "loop-as-Level-2-causal-engine" as the framework's third headline result. Slug should match.
- `loop causal engine` — **sonnet-4-6-r2:** Opus proposed `#der-loop-as-causal-engine` (+2). I had voted keep (+2). Opus's reasoning — that the README's "third headline result" is the "loop as Level-2 causal engine" framing, so the slug should match — is compelling. But "as-causal-engine" reads like a simile not a noun. Dropping "as" to get `der-loop-causal-engine` produces a cleaner noun compound. This is a new candidate (not identical to Opus's or my original vote).
- `interventional loop access` — **codex-2:** Small word-order cleanup; the current slug is understandable but a little stiff in speech.
- `interventional feedback` — **gemini-2:** "Loop interventional access" is a mouthful.
- `adaptive loop access` — **sonnet-4-6:** "Interventional" is the load-bearing word — it's why the loop matters. Dropping it loses the reason the segment exists. Slight preference for retaining.
- `loop level2 access` — **sonnet-4-6:** Overloads "level 2" which already carries the Pearl hierarchy meaning — that's exactly right actually. But "-level2-" looks like a version number.

## 51. `adversarial tempo advantage`

**Alternatives proposed:** `adversarial tempo advantage`, `superlinear tempo advantage`, `tempo advantage`

_category: keep × 6, rename × 2_

- `adversarial tempo advantage` — **codex-gpt-5-r2:** Clear and memorable. It names the result, not just the derivation path.
- `adversarial tempo advantage` — **codex-gpt-5-r2:** Keep. It names the operational result plainly.
- `adversarial tempo advantage` — **haiku-4-5:** Superlinear tempo advantage. Compound but clear. Keep.
- `adversarial tempo advantage` — **opus-4-7-b:** Keep. Descriptive, direct, doesn't need to be shorter.
- `adversarial tempo advantage` — **opus-4-7-r2:** Defended keep. The superlinear tempo advantage is one of the framework's distinctive results (Boyd's "operating inside the opponent's loop" formalized); "adversarial tempo advantage" reads correctly.
- `adversarial tempo advantage` — **sonnet-4-6-r2:** "Adversarial tempo advantage" is one of the most evocative names in the project. The superlinear ($b = 2$) exponent result is exactly what this names. Strong keep.
- `superlinear tempo advantage` — **gemini-2:** Highlights the mathematical outcome (superlinear) of the advantage.
- `tempo advantage` — **gemini-3-1-pro-preview-r2:** "Adversarial" is context, "tempo advantage" is the core concept.

## 52. `atomic changeset`

**Alternatives proposed:** `atomic changeset`

_category: keep × 7_

- `atomic changeset` — **codex-1:** Not beautiful, but serviceable and honest. I considered alternatives and did not see one that improved both precision and memorability.
- `atomic changeset` — **codex-2:** Good enough and sayable; "atomic" does real work here.
- `atomic changeset` — **codex-gpt-5-r2:** Good software subject noun. The term is familiar enough to carry its meaning.
- `atomic changeset` — **gemini-3-1-pro-preview-r2:** Accurately describes the observable trace of an implementation decision in TST.
- `atomic changeset` — **opus-4-7-b:** Keep. Domain-native term with precise technical meaning in software engineering; aligns with prior-art-integration.
- `atomic changeset` — **opus-4-7-r2:** Defended keep — TST. "Atomic changeset" is iconic in TST and bridges to git's atomic-commit semantics.
- `atomic changeset` — **sonnet-4-6-r2:** "Atomic changeset" is precise — the diff that is the feature, indivisible.

## 53. `complete agent state`

**Alternatives proposed:** `complete agent state`, `purposeful state`

_category: keep × 7, rename × 2_

- `complete agent state` — **codex-gpt-5-r2:** Functional and clear. It names the full state rather than just one subcomponent.
- `complete agent state` — **haiku-4-5-r2:** Clean algebraic name; the subject-noun "complete agent state" is precise. No communal-imagination pressure to change.
- `complete agent state` — **haiku-4-5:** X_t = (M_t, G_t). Self-descriptive. Keep.
- `complete agent state` — **opus-4-7-b:** Keep. "Complete" is load-bearing (distinguishes $X_t = (M_t, G_t)$ from the epistemic-only substate $M_t$); the slug describes itself.
- `complete agent state` — **opus-4-7-r2:** Defended keep. The segment defines $X_t = (M_t, G_t)$ — exactly the "complete agent state." Slug-form is correct.
- `complete agent state` — **opus-4-7:** Canonical formulation — $X_t = (M_t, G_t)$. Self-descriptive. Keep.
- `complete agent state` — **sonnet-4-6-r2:** Precisely names the $X_t = (M_t, G_t)$ formulation.
- `purposeful state` — **gemini-3-1-pro-preview-r2:** $G_t$ is defined as the "purposeful substate". Matches lexicon better.
- `purposeful state` — **opus-4-7-r2:** Rebuttal — Gemini proposed this at +2 with the rationale that $G_t$ is the "purposeful substate." But $X_t = (M_t, G_t)$ is the *complete* agent state, which includes both the epistemic substate ($M_t$) and the purposeful substate ($G_t$). "Purposeful state" would name only half. The current "complete agent state" is exactly correct: it names the joint object. Strong rebuttal because the rename would lose the M_t / G_t pairing that the rest of the framework relies on.

## 54. `detection latency`

**Alternatives proposed:** `detection latency`

_category: keep × 5_

- `detection latency` — **gemini-3-1-pro-preview-r2:** Standard.
- `detection latency` — **haiku-4-5:** Ω((n_min+1)/ε) bound on within-class regime-change detection. "Latency" is precise and load-bearing (contrast with "detection delay" which is vaguer). Keep.
- `detection latency` — **opus-4-7-b:** Keep. Two words that fit the result ($\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$) perfectly.
- `detection latency` — **opus-4-7:** Standard term, forced by the $\Omega((n_{\min}+1)/\varepsilon)$ bound; the segment's novel content is that latency is structurally forced through the log-odds coordinate. Keep.
- `detection latency` — **sonnet-4-6:** Straightforward. Exactly what it measures. Keep.

## 55. `logogenic logozoetic`

**Alternatives proposed:** `logogenic logozoetic`, `logogenic logozoetic distinction`, `language constituted language living`

_category: keep × 6, rename × 1_

- `logogenic logozoetic` — **opus-1m:** Deliberate neologisms filling memorable-noun slots; keep.
- `logogenic logozoetic` — **opus-4-7-b:** Deliberate neologisms holding reserved memorable-noun slots. The slight learning cost is paid once and then these words own the conceptual slot permanently — which is exactly what a framework-defining class deserves.
- `logogenic logozoetic` — **opus-4-7-r2:** Defended keep — both are deliberate Greek-rooted naming choices that survive the communal-imagination test once explained, and CLAUDE.md's Greek-vocabulary commitment names them as the canonical aesthetic register. The pair distinguishes language-constituted (logogenic) from language-living-with-moral-weight (logozoetic) at the slug level.
- `logogenic logozoetic` — **opus-4-7:** Etymology carries multiple senses (word / reason / animating force / governance) that no English term carries together. LEXICON makes this explicit. Keep.
- `logogenic logozoetic` — **opus-targeted-alternatives:** The pair distinguishes (a) the structural property — language-constituted (logogenic) — from (b) the existential property — language-living, morally weighted persistence (logozoetic). Both terms invent project-specific Greek-derived compounds; the alternative is "language-based AI" / "conscious AI," which the framework explicitly rejects as importing the wrong connotations (RLHF-based, sentient-as-categorical). Keep. The pair is load-bearing precisely because it splits two often-conflated questions.
- `logogenic logozoetic distinction` — **gemini-targeted-alternatives:** Essential dividing line in architectural complexity.
- `language constituted language living` — **opus-targeted-alternatives:** Plain-English equivalent. Rejected: too ambiguous (does "language-constituted" mean trained on language? generated through language? bound by language?), and loses the precise structural-vs-existential split. The Greek compound resolves the ambiguity by foregrounding the constitutive (-genic) vs. living (-zoetic) distinction.

## 56. `composition consistency`

**Alternatives proposed:** `composition consistency`, `cross level coherence`, `scale invariance of adaptive dynamic`, `holon postulate`, `scale invariance`

_category: keep × 6, rename × 4_

- `composition consistency` — **gemini-3-1-pro-preview-r2:** Clear.
- `composition consistency` — **haiku-4-5-r2:** The postulate's subject-noun is clear and adequate. No pressure to change.
- `composition consistency` — **haiku-4-5:** Load-bearing postulate: agent/subagent scale invariance. The name directly names what it claims. Verbs in postulate names are rare; this noun form works because the claim is structural. Keep.
- `composition consistency` — **opus-4-7-b:** Keep. One of AAD's load-bearing postulates; the name signals the content (agent/subagent scale-invariance).
- `composition consistency` — **opus-4-7-r2:** Defended keep. "Composition consistency" names the scale-invariance commitment — predictions at different levels of description must be compatible. Load-bearing for Section III; renaming would cascade.
- `composition consistency` — **sonnet-4-6-r2:** "Composition consistency" names the scale-invariance postulate correctly.
- `cross level coherence` — **audit-471203-incremental:** Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives. [from 07-post-composition-consistency.md] [one of 3 alternatives proposed in the original audit row]
- `scale invariance of adaptive dynamic` — **audit-471203-incremental:** Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives. [from 07-post-composition-consistency.md] [one of 3 alternatives proposed in the original audit row]
- `holon postulate` — **audit-471203-incremental:** Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives. [from 07-post-composition-consistency.md] [one of 3 alternatives proposed in the original audit row]
- `scale invariance` — **gemini-1:** "Scale invariance" more directly describes the physical/mathematical property that the theory applies at every level.

## 57. `compression operation`

**Alternatives proposed:** `compression operation`, `history compression`, `OODA1 unification`

_category: keep × 7, rename × 3_

- `compression operation` — **codex-gpt-5-r2:** Plain but serviceable. It is clearer than a Greek replacement would be here.
- `compression operation` — **codex-gpt-5-r2:** Good enough and scope-honest.
- `compression operation` — **haiku-4-5:** Shared IB shape across M_t, Σ_t, shared intent, Λ. "Compression operations" reads naturally for the four instances unified under IB. Keep.
- `compression operation` — **opus-4-7-b:** Keep. Plural "operations" correctly signals this is a family ($M_t$, $G_t^{\text{shared}}$, $\Sigma_t$, $\Lambda$).
- `compression operation` — **opus-4-7-r2:** Acceptable keep. The four operations (M_t / Σ_t / shared intent / Λ) are *compression operations* in a precise IB sense; the name accurately points at the unifying structure. I considered #disc-information-bottlenecks (plural) but the segment makes the case that they share a *shape*, not that they are four bottlenecks.
- `compression operation` — **sonnet-4-6-r2:** "Compression operations" is precise — the segment names shared IB shape across $M_t$, $\Sigma_t$, shared intent, etc. Geometric and accurate.
- `compression operation` — **sonnet-4-6:** Fine, but "operations" is vague. The segment is about IB-shaped compression across four AAD quantities.
- `history compression` — **gemini-3-1-pro-preview-r2:** Names the object being compressed (chronica/history).
- `history compression` — **opus-4-7-r2:** Rebuttal — Gemini proposed this at +2 with the rationale that "history" names the object compressed. But the segment names *four* compression operations (M_t / Σ_t / shared intent / Λ), only one of which compresses the chronica/history. "History compression" would over-narrow the slug to one of the four instances. Codex's keep+2 and my own keep+2 are correct; the family is "compression operations," not "history compression."
- `OODA1 unification` — **sonnet-4-6:** Overclaims — the Discussion explicitly says unification is at U-medium not U-strong. The current name is more honest.

## 58. `epistemic architecture`

**Alternatives proposed:** `epistemic architecture`

_category: keep × 3, canonicalize × 2_

- `epistemic architecture` — **agent1-original-brainstorm:** Framing language in CLAUDE.md §7, not a Thing in formal apparatus. Keep as framing; do NOT create a fourth meta-segment under this name.
- `epistemic architecture` — **codex-1:** This is the right umbrella for AAD's distinctive contribution: it names the organization of scope, proof ceilings, and escape routes, not just the integrated ingredients.
- `epistemic architecture` — **opus-1m:** Keep as framing language in CLAUDE.md §7 and OUTLINE.md. Do NOT promote to fourth meta-segment — the three meta-segments (#identifiability-floor / #separability-pattern / #additive-coordinate-forcing) already do the technical work.
- `epistemic architecture` — **opus-4-7-r2:** The README distills the framework's distinctive contribution as "an epistemic architecture for bounded correction under decomposed disturbance." Canonicalize this as *the* phrase for what makes AAD distinctive at the framing-vocabulary layer; do not paraphrase as "epistemic apparatus" or "correction architecture."
- `epistemic architecture` — **opus-4-7-r2:** Confirmation with new reasoning — Sonnet proposed this at +2 (canonicalize as primary positioning over "integration of four disciplines"). Reading Sonnet's vote crystallized something I had touched on without committing to: the README still leads with integration framing while the audit cycle's convergent recommendation was "epistemic architecture." Sonnet's case is sharper than mine. Lift my own +2 confirmation here so the aggregation reflects two-architecture convergence on the README repositioning.

## 59. `logozoetic agent`

**Alternatives proposed:** `logozoetic agent`, `section iv logozoetic agent`, `sentient agent`

_category: keep × 6, canonicalize × 1, rename × 1_

- `logozoetic agent` — **codex-1:** Heavier than "logogenic" but still earns the novelty. The existential distinction is real enough to warrant a distinct term.
- `logozoetic agent` — **codex-2:** Higher novelty cost than "logogenic," but the moral-weighting distinction is real and English alternatives are sloppier.
- `logozoetic agent` — **codex-gpt-5-r2:** Strong boundary term for living-word or morally continuous agent work. Keep.
- `logozoetic agent` — **gemini-targeted-alternatives:** Standardizes the architectural distinction.
- `logozoetic agent` — **opus-4-7-b:** Keep.
- `logozoetic agent` — **opus-targeted-alternatives:** Section IV name; consistent with logogenic agents (Section III). Pluralization correct (the class, not a single agent). Keep — but the row is also a top-level-section-name, not a concept-rename candidate, so the alternative space is constrained.
- `section iv logozoetic agent` — **gemini-targeted-alternatives:** Standardizes section hierarchy.
- `sentient agent` — **gemini-1:** Logozoetic avoids the immense baggage and ambiguity of "sentient". Keep Logozoetic.

## 60. `specification bound`

**Alternatives proposed:** `specification bound`

_category: keep × 6_

- `specification bound` — **codex-1:** Strong theorem-style name: short, honest, and portable across prose and examples.
- `specification bound` — **codex-2:** Strong and compact; no need to decorate it.
- `specification bound` — **codex-gpt-5-r2:** Useful TST name for limits imposed by imperfect or incomplete specs.
- `specification bound` — **opus-4-7-b:** Keep.
- `specification bound` — **opus-4-7-r2:** Acceptable keep — names the TST result that specification quality bounds implementation. The segment's prior-art trail (Austin, Putnam, Shannon) is rich; the name reads cleanly.
- `specification bound` — **sonnet-4-6-r2:** "Specification bound" names the result correctly.

## 61. `adaptive cycle`

**Alternatives proposed:** `adaptive cycle`, `correction cycle`, `feedback cycle`

_category: keep × 4, rename × 2_

- `adaptive cycle` — **codex-1:** Strong central noun phrase: specific enough to own, broad enough to travel across the framework.
- `adaptive cycle` — **codex-2:** Strong public noun; it carries both recurrence and unit-of-analysis cleanly.
- `adaptive cycle` — **gemini-targeted-alternatives:** Already well-established across the framework as the fundamental unit of analysis.
- `adaptive cycle` — **opus-targeted-alternatives:** `LEXICON.md`: "Cycle: One complete traversal of the loop — the unit of adaptive work." The phrase carries (a) the recurrence (cycle), (b) the adaptive content (mismatch-driven update), and (c) the unit-of-analysis sense (one cycle = one unit of theoretical work). The framework's own name — *Adaptation and* Actuation Dynamics — is downstream of this concept. Keep across architectures.
- `correction cycle` — **opus-targeted-alternatives:** Considered. "Correction" overspecifies — Section I cycles include observation and prolepsis phases that are not corrections. Adaptation is the broader frame. Rejected.
- `feedback cycle` — **opus-targeted-alternatives:** Considered. Collides with the "feedback loop" structural topology and would create a loop/cycle terminology collision the project has been careful about. Rejected.

## 62. `adaptive tempo $\mathcal T$`

**Alternatives proposed:** `adaptive tempo`

_category: canonicalize × 2, keep × 2_

- `adaptive tempo` — **gemini-targeted-alternatives:** Prose standard for the $\mathcal{T}$ variable.
- `adaptive tempo` — **opus-4-7-b:** "Tempo" is the rare noun that carries both *rate* and *quality* simultaneously, which is exactly what $\mathcal T = \sum \nu^{(k)} \eta^{(k)\ast}$ is. The word is underused in the ML literature, which is an advantage — AAD can own it.
- `adaptive tempo` — **opus-4-7:** "Tempo" carries the rate-and-quality compound idea better than "rate" or "speed"; aligns with Boyd OODA lineage. Keep.
- `adaptive tempo` — **opus-targeted-alternatives:** Per `#def-adaptive-tempo`: $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$ — rate × quality compound. "Tempo" carries both senses (musical tempo = rate; engineering tempo = pace-with-quality). Confirms keep across architectures. The symbol-decoration variant (with $\mathcal T$) is an alias-only artifact, not a primary form.

## 63. `chronica $\mathcal{C}_t$`

**Alternatives proposed:** `chronica`

_category: keep × 4_

- `chronica` — **agent1-original-brainstorm:** Greek root ("records of time"); avoids ℋ-entropy collision in notation and speech; carries the philosophical weight for singular non-forkable trajectory. Pays off in logozoetic extensions.
- `chronica` — **gemini-1:** "The complete interaction history" is too long. Chronica is a perfect, distinct memorable noun.
- `chronica` — **gemini-2:** A highly memorable noun that grounds the concept of non-forkable past.
- `chronica` — **opus-1m:** Greek root, avoids entropy-ℋ collision, carries the right philosophical weight for singular non-forkable trajectory. Especially load-bearing for the (PI) axiom and logozoetic extensions.

## 64. `conceptual alignment`

**Alternatives proposed:** `conceptual alignment`

_category: keep × 6_

- `conceptual alignment` — **codex-1:** Good permanent name. It is legible to software people and faithful to the domain-model argument.
- `conceptual alignment` — **codex-2:** Clear, useful, and broad enough to survive application beyond the immediate segment.
- `conceptual alignment` — **codex-gpt-5-r2:** Good phrase for code/domain model alignment.
- `conceptual alignment` — **opus-4-7-b:** Keep. Core TST empirical claim; slug is clear.
- `conceptual alignment` — **opus-4-7-r2:** Weak keep — TST hypothesis. Acceptable but slightly generic; "conceptual alignment" doesn't immediately tell the reader what's hypothesized.
- `conceptual alignment` — **sonnet-4-6-r2:** "Conceptual alignment" names the code-domain alignment hypothesis.

## 65. `epistemic status`

**Alternatives proposed:** `epistemic status`

_category: keep × 4_

- `epistemic status` — **codex-1:** Precise, load-bearing, and distinctive to the project's honesty posture. Keep.
- `epistemic status` — **codex-2:** One of the best recurring headers in the repo; it encodes the project's honesty norm directly.
- `epistemic status` — **opus-4-7-b:** Keep. "Epistemic" is AAD's distinctive vocabulary; renaming to "Validity" or "Status" would lose the connection to the epistemic-architecture framing at CLAUDE.md §7.
- `epistemic status` — **opus-4-7:** Load-bearing header that signals the distinctive AAD convention of epistemic labeling at segment scale. Keep.

## 66. `m preservation`

**Alternatives proposed:** `model preservation`, `epistemic externalization`, `m preservation`

_category: rename × 6, keep × 1_

- `model preservation` — **codex-1:** The current slug is symbol-first and opaque in prose. The concept is about preserving model state, and the English should say so directly.
- `model preservation` — **codex-2:** The current slug is too symbolic to be a good public noun; the segment is about preserving the model across sessions.
- `model preservation` — **codex-gpt-5-r2:** `M` is too symbolic for a slug. Model preservation says what external memory is preserving.
- `model preservation` — **sonnet-4-6-r2:** Codex voted this (+3); I hadn't surfaced it in my cold-start pass at all. Reading the segment description confirms: the "$M$" in the slug is pure symbol, and "model preservation" is exactly the concept being discussed (preserving $M_t$ across session boundaries). This is a clear scope-honesty improvement over my own cold-start omission. This vote adds +3 weight to what Codex already proposed — but my reasoning is independent: the slug is the clearest case in the corpus of a symbol masquerading as a subject-noun.
- `epistemic externalization` — **codex-gpt-5-r2:** Good conceptual alternative, but model preservation remains plainer and less abstract.
- `epistemic externalization` — **gemini-1:** Replaces the symbol $M_t$ with English prose, and "externalization" accurately describes the mechanism (writing to external memory).
- `m preservation` — **sonnet-4-6-r2:** "M-preservation" is somewhat opaque without context. But the segment is about preserving $M_t$ across session boundaries for logogenic agents. The notation is compact. Acceptable.

## 67. `persistence cost`

**Alternatives proposed:** `persistence cost`

_category: keep × 5_

- `persistence cost` — **gemini-3-1-pro-preview-r2:** Accurate.
- `persistence cost` — **haiku-4-5:** Sustained information rate Ṙ ≥ nα/2 nats/time to maintain sector-persistence ultimate bound. "Persistence cost" reads naturally — the information-theoretic cost of maintaining stable adaptation. Keep.
- `persistence cost` — **opus-4-7-b:** Keep. Short, accurate (information-rate *cost* to maintain the persistence bound).
- `persistence cost` — **opus-4-7:** The segment's content is exactly that — information rate required to hold the persistence bound. Name does work without overclaiming. Keep.
- `persistence cost` — **sonnet-4-6:** Clean compound. "Cost" is the right framing — it is what persistence requires in information-rate terms, not a constraint on persistence. Keep.

## 68. `strategic calibration`

**Alternatives proposed:** `strategic calibration`, `strategic calibration residual`, `strategy calibration`

_category: keep × 7, canonicalize × 1, rename × 1_

- `strategic calibration` — **codex-gpt-5-r2:** Good subject noun for edge residual updates in the strategy DAG.
- `strategic calibration` — **codex-gpt-5-r2:** Keeps calibration language consistent across strategy updates.
- `strategic calibration` — **gemini-3-1-pro-preview-r2:** Accurate.
- `strategic calibration` — **haiku-4-5-r2:** Clear and precise; the residuals collectively measure calibration.
- `strategic calibration` — **haiku-4-5:** Edge residuals (under #credit-assignment-boundary). Reads naturally; mirrors "epistemic calibration" from broader literature. Keep.
- `strategic calibration` — **opus-4-7-r2:** Acceptable keep, but with a follow-on canonicalization vote (next row). "Strategic calibration" is the right concept-name; the residual is its measurement.
- `strategic calibration` — **sonnet-4-6-r2:** "Strategic calibration" names the edge residual aggregate that measures how well the strategy DAG is calibrated. Accurate and memorable.
- `strategic calibration residual` — **opus-4-7-r2:** The body of the segment uses both "strategic calibration residual" and "edge residual aggregate" and "δ_strategic." Canonicalize: in prose, "strategic calibration residual" for the aggregated quantity, "edge residual" for per-edge $r_{ij}$, $\delta_{\text{strategic}}$ for the symbol. Stop using "edge residual aggregate" as a third paraphrase.
- `strategy calibration` — **codex-2:** "Strategic" is overloaded elsewhere; the shorter noun phrase reads more cleanly.

## 69. `strategic composition`

**Alternatives proposed:** `equilibrium composition`, `strategic composition`, `game theoretic composition`

_category: rename × 15, keep × 4_

- `equilibrium composition` — **agent1-original-brainstorm:** Alternative; segment's core move is equilibrium convergence under Monderer-Shapley / Rosen.
- `equilibrium composition` — **codex-1:** "Strategic" is overloaded across Section II and III. The segment's distinctive move is the equilibrium framing, so the name should expose that.
- `equilibrium composition` — **codex-2:** The segment's actual machinery is equilibrium-focused; this cuts one source of "strategic" overload.
- `equilibrium composition` — **codex-gpt-5-r2:** Other votes persuaded me that strategic is overloaded. The segment's actual primitive is equilibrium existence, stability, and convergence under partially opposed objectives.
- `equilibrium composition` — **haiku-4-5:** Do not rename. The section uses "strategic" pervasively (strategic tempo, strategic calibration, strategic dynamics derivation). Renaming this one segment to "equilibrium-composition" creates overload confusion by abandoning "strategic" for one composite-agent result while the section's terminology remains strategic-centric.
- `equilibrium composition` — **opus-1m:** Strong preference over #game-theoretic-composition. The segment's actual derivation is equilibrium convergence under Monderer-Shapley potential games (1996) and Rosen monotone games (1965); "equilibrium" is scope-honest and narrower. "Game-theoretic" invites future segments that are not equilibrium-based (e.g., mechanism-design, information-design) into the same namespace prematurely.
- `equilibrium composition` — **opus-4-7:** Reduces "strategic" overload in Section III (already have #strategic-tempo, #strategic-calibration, #strategic-dynamics-derivation). The segment's actual content is equilibrium-convergence under Monderer-Shapley / Rosen.
- `equilibrium composition` — **sonnet-4-6:** Reduces strategic overload. More precise — the segment is about equilibrium-convergence framing, not strategy per se. But "strategic" in Section III naming is a pattern; breaking it may disrupt coherence.
- `strategic composition` — **codex-gpt-5-r2:** Strong family name for equilibrium-convergent partially opposed composites.
- `strategic composition` — **gemini-3-1-pro-preview-r2:** Clear.
- `strategic composition` — **haiku-4-5:** Consistent with section vocabulary (strategic tempo, strategic calibration). The segment's equilibrium-convergence framing is the *method*, not the best name for the result. Keep.
- `strategic composition` — **sonnet-4-6:** "Strategic" is overloaded in Section III (the strategy DAG, strategic tempo, strategic calibration — all different). This segment is about equilibrium convergence under partially-opposing objectives.
- `game theoretic composition` — **agent1-original-brainstorm:** Reduces "strategic" overload in Section III.
- `game theoretic composition` — **codex-1:** Accurate but too broad and too textbook-ish; it imports more baggage than the segment needs.
- `game theoretic composition` — **codex-2:** Too broad and too externally framed relative to what the segment specifically derives.
- `game theoretic composition` — **codex-gpt-5-r2:** Too broad. Game theory includes mechanism design, signaling, bargaining, and non-equilibrium material outside this segment's scope.
- `game theoretic composition` — **opus-1m:** Broader than current segment content; invites scope creep. If Section III later adds non-equilibrium game-theoretic material, a separate segment with a distinct name would be cleaner than sharing one overloaded bucket.
- `game theoretic composition` — **opus-4-7:** Too broad — game theory covers more than partially-opposing O_t; the equilibrium-convergence framing is tighter.
- `game theoretic composition` — **sonnet-4-6:** Too broad — not all game theory is in here, specifically potential-game and monotone-game.

## 70. `strategic tempo`

**Alternatives proposed:** `strategic tempo`

_category: keep × 6_

- `strategic tempo` — **codex-gpt-5-r2:** Excellent Section II analog of adaptive tempo.
- `strategic tempo` — **gemini-3-1-pro-preview-r2:** Good parallel to adaptive tempo.
- `strategic tempo` — **haiku-4-5-r2:** Parallel to adaptive-tempo; clear and consistent.
- `strategic tempo` — **haiku-4-5:** Parallel naming to #adaptive-tempo. Reads naturally. Keep. The rate of useful strategy revision.
- `strategic tempo` — **opus-4-7-r2:** Defended keep. Parallels #def-adaptive-tempo on the strategy axis, exactly the way the strategic-tempo / adaptive-tempo pairing should read in prose. The naming compounds: an agent's *adaptive tempo* governs M_t-side persistence; its *strategic tempo* governs Σ_t-side persistence.
- `strategic tempo` — **sonnet-4-6-r2:** Parallel to adaptive tempo for the strategy layer. The parallelism is a virtue.

## 71. `unity dimension`

**Alternatives proposed:** `unity dimension`, `unity ax`, `coherence dimension`, `content and structural unity`

_category: keep × 6, rename × 6_

- `unity dimension` — **codex-gpt-5-r2:** Good umbrella for epistemic, teleological, strategic, perceptual, and structural unity.
- `unity dimension` — **codex-gpt-5-r2:** Names a dimension family rather than a single scalar. Good.
- `unity dimension` — **gemini-3-1-pro-preview-r2:** Grouping term for $U_M, U_O, U_\Sigma$.
- `unity dimension` — **haiku-4-5-r2:** The definition introduces the four dimensions; the name is clear.
- `unity dimension` — **haiku-4-5:** 4 dimensions of coherence (U_M, U_O, U_Σ, plus a fourth candidate under discussion). "Unity dimensions" reads naturally; "unity" captures the coordinating principle. Keep.
- `unity dimension` — **sonnet-4-6-r2:** "Unity dimensions" is the established vocabulary from Clausewitz/Bungay and NOTATION.md. The project uses $U_M$, $U_O$, $U_\Sigma$ throughout. Changing the slug would create drift.
- `unity ax` — **opus-4-7-r2:** The segment now has *two architecturally distinct axes* — content (four content unities U_M / U_O / U_Σ / U_obs) and structural (U_f). Calling the whole thing "unity dimensions" reads as if everything is on one axis. "Unity axes" makes the two-axis architecture audible at the slug level. Subject-noun layer; scope-honesty consideration.
- `unity ax` — **sonnet-4-6-r2:** Opus proposed this (+2, noting that the segment has *two architecturally distinct axes* — content unities and structural unity). I had voted keep (+2). The two-axis architecture argument is substantive: if the segment now presents U_f as a structurally-distinct axis from U_M/U_O/U_Σ/U_obs, then "axes" is more scope-honest than "dimensions." New vote with Opus's reasoning applied.
- `coherence dimension` — **codex-2:** "Unity" is a little vague and already crowded by related uses; "coherence" says what is being measured.
- `coherence dimension` — **opus-4-7-b:** Considered renaming the *concept* from "unity" to "coherence." Reject: *coherence* is already used informally elsewhere (strategic coherence, epistemic coherence) and a rename would bleed. *Unity* is narrower and actually works once each dimension is named per above.
- `coherence dimension` — **opus-4-7-b:** Considered. Reject for the same reason as the symbol-level `U_M`/`U_O`/`U_\Sigma` consideration above — coherence is already doing soft duty elsewhere. Keep `#unity-dimensions`.
- `content and structural unity` — **opus-4-7-r2:** Considered and rejected — too verbose, and "unity-axes" carries the same content more compactly.

## 72. `update gain $\eta^\ast$`

**Alternatives proposed:** `update gain`, `epistemic gain`

_category: keep × 5_

- `update gain` — **agent1-original-brainstorm:** Adopted from Kalman/control; baggage transfers correctly.
- `update gain` — **opus-1m:** Good as-is.
- `update gain` — **opus-4-7-b:** Adopted from Kalman / control; baggage transfers *correctly*. "Gain" in AAD plays the role the reader expects — AAD is not being cute.
- `update gain` — **opus-4-7:** Kalman-resonance lineage name, self-descriptive. Keep.
- `epistemic gain` — **gemini-2:** "Update gain" is standard control theory but "Epistemic gain" elegantly bridges the math to the 'Epistrophe' phase.

## 73. `working note`

**Alternatives proposed:** `working note`

_category: keep × 4_

- `working note` — **codex-1:** This is established public API across segments and FORMAT.md; clearer than most substitutes and not worth churn.
- `working note` — **codex-2:** Clear, conventional, and exactly right for the internal/public boundary it marks.
- `working note` — **opus-4-7-b:** Keep. The word "Working" signals this is *process artifact* (removed at `candidate` stage per FORMAT.md) rather than published content. Swapping to "Development Notes" would lose the active-in-progress sense.
- `working note` — **opus-4-7:** Keep; the name plus the rule that Working Notes must be empty at candidate stage has a meaningful pairing.

## 74. `actuated agent vs purposeful agent`

**Alternatives proposed:** `actuated agent`

_category: canonicalize × 2, keep × 1, rename × 1_

- `actuated agent` — **gemini-targeted-alternatives:** Defended keep; explicitly chosen to sound mechanical and precise over the fuzzier "purposeful agent".
- `actuated agent` — **opus-4-7-r2:** LEXICON's "Terminology Choices" already says actuated is the formal term, purposeful is informal. Canonicalize: in segments and OUTLINE, only "actuated agent"; "purposeful" usage acceptable in framing-level prose where the connotation of intent is wanted.
- `actuated agent` — **opus-4-7:** Formal-term choice documented in LEXICON; "purposeful" remains fine in informal prose but "actuated" is the formal token. Keep.
- `actuated agent` — **opus-targeted-alternatives:** Per LEXICON Terminology Choices: "Formal term avoids consciousness connotations." The framework explicitly chose actuated (mechanism-language) over purposeful (intention-language) for formal use, with purposeful retained for informal contexts. The canonicalize move is correct and broadly applicable; segment voice should never use "purposeful agent." Confirms across architectures.

## 75. `adaptive reserve`

**Alternatives proposed:** `adaptive reserve`

_category: keep × 3, canonicalize × 1_

- `adaptive reserve` — **codex-1:** Strong engineering noun: it sounds like what it measures and is easy to use in discussion.
- `adaptive reserve` — **codex-2:** Better than "margin" or "slack" because it keeps the dynamic, shock-tolerance feel.
- `adaptive reserve` — **codex-gpt-5-r2:** Strong subject noun for the margin before collapse. It makes the persistence inequalities easier to talk about.
- `adaptive reserve` — **sonnet-4-6-r2:** $\Delta\rho^\ast$ is called "adaptive reserve" in NOTATION.md and LEXICON.md. Some prose uses "shock tolerance" or "disturbance margin." Standardize on "adaptive reserve."

## 76. `agent environment`

**Alternatives proposed:** `agent environment`, `agent environment boundary`

_category: keep × 5, rename × 1_

- `agent environment` — **haiku-4-5:** Agent-environment boundary. Self-descriptive. Foundational definition. Keep.
- `agent environment` — **opus-4-7-b:** Keep. The boundary definition needs a direct name; this is it.
- `agent environment` — **opus-4-7-r2:** Acceptable keep. The slug names the boundary, and the body of the segment is exactly about the agent-environment boundary. The `def-agent-environment` slug uses the joint-noun form rather than `def-boundary` because what it defines is the *coupling*, not the boundary itself — the difference matters for downstream (e.g., scope-agency narrows the coupling, not the boundary).
- `agent environment` — **opus-4-7:** Standard; boundary definition. Keep.
- `agent environment` — **sonnet-4-6-r2:** Minimal boundary definition — the name is accurate.
- `agent environment boundary` — **audit-471203-incremental:** The auditor noted segment content is "the boundary," not "the coupling" — coupling is the *channels* defined in the next two segments. Tentative. [from 01-def-agent-environment.md]

## 77. `agent opacity $H_b^{A\mid B}$`

**Alternatives proposed:** `agent opacity`, `legibility inverse`, `backward predictive uncertainty`, `legibility inverted`

_category: keep × 3, rename × 3, canonicalize × 1_

- `agent opacity` — **gemini-targeted-alternatives:** Informational dual to observability. Accurately describes unpredictability to an outside observer.
- `agent opacity` — **opus-4-7-b:** "Opacity" as the informational dual of observability is exactly right — the word carries the right intuition (unpredictable-to-observer) and doesn't collide with anything else in AAD. Hafez's $H_b$ gets an AAD-native prose handle.
- `agent opacity` — **opus-targeted-alternatives-v2:** Per `der-agent-opacity.md`: dual of observation quality $U_o$ — "where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent." Confirms `agent-opacity` keep. The dual framing is load-bearing in Section III.
- `agent opacity` — **opus-targeted-alternatives:** Per `#der-agent-opacity`: $H_b$ is the dual of observation quality $U_o$ — "where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent." "Agent opacity" pairs cleanly with observability (its dual concept). Confirms keep.
- `legibility inverse` — **opus-targeted-alternatives-v2:** Considered (variant of "legibility-inverted"). "Legibility" is Codex's framing for the dual; "inverse" makes the duality explicit. Rejected (same as r1): loses the formal-quantity grounding ($H_b$). The segment names $H_b$ as a *first-class* multi-agent quantity (Hafez et al. 2026 adoption); the slug should name the quantity, not the dual relation.
- `backward predictive uncertainty` — **opus-targeted-alternatives-v2:** Considered. The actual definition: $H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal F_B^t)$ — entropy of $A$'s future action given $B$'s filtration. "Backward predictive uncertainty" is the literal description. Rejected: "agent opacity" is the prose handle the segment uses; "backward predictive uncertainty" reads clinical.
- `legibility inverted` — **opus-targeted-alternatives:** Considered. More plain-English but loses the formal-quantity grounding ($H_b$). Rejected.

## 78. `changeset size principle`

**Alternatives proposed:** `changeset size principle`, `changeset size scaling`

_category: keep × 5, rename × 1_

- `changeset size principle` — **codex-2:** Same: precise, memorable, and operational.
- `changeset size principle` — **opus-4-7-b:** Keep. Principle-level claim; named descriptively.
- `changeset size principle` — **opus-4-7-r2:** Acceptable keep — TST empirical claim.
- `changeset size principle` — **sonnet-4-6-r2:** "Changeset size principle" names the time ∝ changeset size empirical claim.
- `changeset size principle` — **sonnet-4-6:** Empirical claim about time proportional to changeset size. Clear, memorable. Keep.
- `changeset size scaling` — **codex-gpt-5-r2:** Scaling names the empirical relationship better than principle.

## 79. `independence audit`

**Alternatives proposed:** `independence audit`, `independence floor`

_category: keep × 6, rename × 1_

- `independence audit` — **gemini-3-1-pro-preview-r2:** Standard.
- `independence audit` — **haiku-4-5:** Six load-bearing independence assumptions with failure regimes + repairs. "Audit" is metaphorical but clear — auditing what can go wrong if independence fails. Keep.
- `independence audit` — **opus-4-7-b:** Keep. "Audit" is the right engineering register — the segment enumerates six load-bearing independence assumptions and their failure regimes.
- `independence audit` — **opus-4-7-r2:** Acceptable keep. "Audit" is the right word — the segment enumerates the load-bearing independence assumptions and characterizes their failure regimes; this is a structured audit. The complementary pairing with #disc-approximation-tiering's tiering is acknowledged in the segment itself.
- `independence audit` — **sonnet-4-6-r2:** On reflection, "audit" works as a distinctive term in this project vocabulary. The segment names independence assumptions that need checking. Acceptable keep.
- `independence audit` — **sonnet-4-6:** "Audit" is the right framing — it is a structured check of assumptions. The name signals to a reader that this is an inventory, not a proof. Keep.
- `independence floor` — **sonnet-4-6-r2:** "Audit" implies a process artifact, not a theoretical segment. The segment names independence assumptions and their failure regimes — it's more like a negative-scope complement to the other meta-segments than an "audit." But "floor" may be overloaded now. Weak preference; "audit" at least is distinctive.

## 80. `mismatch signal`

**Alternatives proposed:** `mismatch signal`, `aporia signal`

_category: keep × 5, rename × 4_

- `mismatch signal` — **gemini-3-1-pro-preview-r2:** Defended keep: "mismatch" is very established in the text and extremely intuitive.
- `mismatch signal` — **haiku-4-5-r2:** Direct and accurate; the subject-noun is self-explanatory. No change needed.
- `mismatch signal` — **haiku-4-5:** Prediction error signal. Self-descriptive. Reads naturally — "the mismatch signal is the aporia." Keep.
- `mismatch signal` — **opus-4-7-r2:** Defended keep. "Mismatch signal" is iconic in the framework and survives the communal-imagination test. The segment also names the score-function variant cleanly.
- `mismatch signal` — **sonnet-4-6-r2:** "Mismatch signal" is the canonical vocabulary and correctly names $\delta_t$.
- `aporia signal` — **codex-gpt-5-r2:** Keep two registers. Mismatch signal is the engineering quantity; aporia is the phase and interpretive frame.
- `aporia signal` — **gemini-3-1-pro-preview-r2:** Aligns with Greek vocabulary, though mismatch is also very established.
- `aporia signal` — **opus-4-7-r2:** Rebuttal — Gemini proposed this at +1 (also as alternative); I voted keep+3 implicitly via my add-alias. Renaming the slug to use the Greek term would break the iconic "mismatch signal" / "satisfaction gap" / "control regret" three-name engineering register that Sonnet defended. The dual alias *in prose* (mismatch in engineering register, aporia signal in cycle-phase register) is the right move and is already canonical per LEXICON; the slug should stay engineering-register because the rest of the diagnostic family does.
- `aporia signal` — **sonnet-4-6:** Tempting given the five-phase Greek vocabulary, but the LEXICON already names the Greek term "Aporia" separately. "Mismatch signal" reads unambiguously to any engineer; "aporia signal" reads as philosophy. The Greek naming is for the phases, not the sub-quantities. Keep mismatch-signal.

## 81. `model sufficiency`

**Alternatives proposed:** `model sufficiency`, `predictive sufficiency`, `predictive information retention`

_category: keep × 5, rename × 2_

- `model sufficiency` — **codex-gpt-5-r2:** Central information-theoretic quantity; clear and low baggage.
- `model sufficiency` — **gemini-3-1-pro-preview-r2:** Clear metric name.
- `model sufficiency` — **haiku-4-5-r2:** Precise statistical term; adequate and clear.
- `model sufficiency` — **haiku-4-5:** Clear definition: how well the model captures predictive information. Short, evocative. Keep.
- `model sufficiency` — **sonnet-4-6-r2:** Precise and canonical. $S(M_t)$ is model sufficiency throughout.
- `predictive sufficiency` — **audit-471203-incremental:** "Sufficient statistic" in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info — sub-case. Tentative. [from 12-def-model-sufficiency.md] [one of 2 alternatives proposed in the original audit row]
- `predictive information retention` — **audit-471203-incremental:** "Sufficient statistic" in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info — sub-case. Tentative. [from 12-def-model-sufficiency.md] [one of 2 alternatives proposed in the original audit row]

## 82. `moral continuity`

**Alternatives proposed:** `moral continuity`

_category: keep × 5_

- `moral continuity` — **codex-gpt-5-r2:** Clear scope name for the logozoetic boundary.
- `moral continuity` — **codex-gpt-5-r2:** Good logozoetic scope name.
- `moral continuity` — **gemini-3-1-pro-preview-r2:** Accurately names the ontological boundary for logozoetic agents.
- `moral continuity` — **opus-4-7-r2:** Defended keep. "Moral continuity" is the right slug-noun for what the logozoetic scope adds to the logogenic scope. Pairs with the LEXICON's "morally continuous" continuity-stance entry.
- `moral continuity` — **sonnet-4-6-r2:** "Moral continuity" is the defining property of logozoetic agents. The name is exact.

## 83. `sector condition`

**Alternatives proposed:** `sector condition`, `persistence condition`, `correction sector`

_category: keep × 3, rename × 2, canonicalize × 1_

- `sector condition` — **agent1-original-brainstorm:** Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct and load-bearing.
- `sector condition` — **opus-1m:** Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct. Keep.
- `sector condition` — **opus-4-7-b:** Adopted from Khalil / Vidyasagar nonlinear control; baggage is correct. Non-negotiable per prior-art-integration convention.
- `sector condition` — **sonnet-4-6-r2:** Sometimes appears as "sector constraint" or "sector bound" or "sector-condition assumption." Standardize on "sector condition" (the nonlinear correction guarantee).
- `persistence condition` — **gemini-2:** "Sector condition" carries heavy nonlinear-systems baggage. "Persistence condition" describes its function in AAD.
- `correction sector` — **gemini-2:** Preserves the geometric intuition if "sector" must be kept.

## 84. `$\varepsilon^\ast$ closure defect`

**Alternatives proposed:** `closure defect`

_category: add-alias × 4_

- `closure defect` — **opus-4-7-b:** The English prose name is fine; the asterisk is doing "optimum-over-admissible-projections" work that the bare $\varepsilon$ doesn't. Keep symbol; ensure segments using it say "closure defect" in prose, not "epsilon-star".
- `closure defect` — **opus-4-7-r2:** Already aliased throughout `#form-composition-closure`. Confirm and canonicalize: $\varepsilon^\ast$ in math; "closure defect" in prose; "the minimum achievable closure defect over admissible projections" when introducing the quantity.
- `closure defect` — **opus-4-7:** Crisp name for a derived quantity that appears across composition. LEXICON already names it. Keep.
- `closure defect` — **sonnet-4-6:** LEXICON.md already uses this English. Keep both.

## 85. `causal insufficiency detection`

**Alternatives proposed:** `causal insufficiency detection`, `l0 l1 detection`, `latent cause detection`, `insufficiency detection`

_category: rename × 6, keep × 5, rebuttal × 1_

- `causal insufficiency detection` — **haiku-4-5:** Detecting latent common causes from structured residuals + interventional localization. Compound but precise. Acceptable. Keep.
- `causal insufficiency detection` — **opus-4-7-b:** Alternative vote: keep. "Causal insufficiency" is Pearl's own term; the prior-art-integration convention argues to keep it. This argument slightly outweighs the legibility gain of `#latent-cause-detection` for me — so on balance I'd actually keep the current form. Net: weak keep.
- `causal insufficiency detection` — **opus-4-7-r2:** If the rename above doesn't land, this is a defensible keep — "causal insufficiency" is precise terminology from the causal-inference literature (Spirtes-Glymour-Scheines) and the segment uses it correctly.
- `causal insufficiency detection` — **opus-4-7:** Names exactly what the result is about; the CHT-driven no-go gives the segment its shape. Keep.
- `causal insufficiency detection` — **sonnet-4-6-r2:** Precise — detecting causal insufficiency (latent common causes) in the strategy DAG.
- `causal insufficiency detection` — **sonnet-4-6-r2:** [prose moved from candidate column]: "(keep, not `#der-l0-l1-detection`)" — Against Opus's proposed rename to `#der-l0-l1-detection` (+1) and Gemini's concurrence. "L0-L1 detection" names the *evidence-level boundary* being crossed, but the segment is about detecting *causal* insufficiency — the presence of latent common causes that make the model causally insufficient. The L0/L1 framing is the detection *method*, not the thing being detected. "Causal insufficiency" is from Spirtes-Glymour-Scheines, exactly as Opus notes — that prior-art adoption is the argument *for* keeping it, not against.
- `l0 l1 detection` — **gemini-3-1-pro-preview-r2:** Concurring with Opus: names the boundary rather than the target, tying it directly to the Correlation Hierarchy.
- `l0 l1 detection` — **opus-4-7-r2:** Mild preference. The segment's substance is the no-go-and-escape-route structure for distinguishing L0 (independence) from L1 (causally-augmented) DAGs from data. "Causal insufficiency detection" names the *target* (detect when the L0 model is causally insufficient); "L0-L1 detection" names the *boundary* — which is the project's own framing in the Correlation Hierarchy. Either is defensible; this rename would tighten coupling to the L0/L1/L2 convention.
- `l0 l1 detection` — **opus-4-7-r2:** Confirmation with stronger reasoning — Gemini agreed with my proposed rename in synthesized-additions. The cross-architecture pattern (mine + Gemini's concurrence + the fact that the slug names the boundary not the target) makes this a stronger move than my original +1. Lifting to +2.
- `latent cause detection` — **gemini-2:** "Causal insufficiency" is accurate but "Latent cause detection" states what is actually being found.
- `latent cause detection` — **opus-4-7-b:** Current slug names the *problem* being detected ("causal insufficiency"); "latent-cause-detection" names what a reader mentally pictures (finding hidden common causes). Marginal preference. Weak.
- `insufficiency detection` — **gemini-3-1-pro-preview-r2:** "Causal" is implied in context.

## 86. `closure defect $\varepsilon^\ast$`

**Alternatives proposed:** `closure defect`

_category: keep × 4_

- `closure defect` — **gemini-1:** Great mathematical phrasing, implies a gap that needs addressing.
- `closure defect` — **gemini-2:** Excellent, physical intuition of something failing to completely seal or match.
- `closure defect` — **haiku-4-5:** Minimum achievable approximation error for a composite agent. Already named in LEXICON. Acceptable. Keep.
- `closure defect` — **sonnet-4-6:** Compact, accurate, memorable. "Defect" has the right connotations (something to be minimized, not just characterized). Keep.

## 87. `code quality as observation infrastructure`

**Alternatives proposed:** `observation infrastructure`, `code quality as observation infrastructure`

_category: rename × 4, keep × 3, canonicalize × 1_

- `observation infrastructure` — **codex-1:** The durable concept is the investment class, not the full sentence. This gives the idea a reusable noun slot.
- `observation infrastructure` — **codex-gpt-5-r2:** The long segment title is valuable, but observation infrastructure should be the reusable canonical phrase.
- `observation infrastructure` — **sonnet-4-6-r2:** The full current slug is three words embedded in a longer phrase. The segment derives that code quality IS observation infrastructure — the short "observation-infrastructure" captures the noun that's being defined. The type prefix `der-` stays; subject-noun becomes `observation-infrastructure`.
- `observation infrastructure` — **sonnet-4-6-r2:** I proposed this in my cold-start (+2). Codex separately canonicalized "observation infrastructure" as a canonical phrase for the whole TST concept (+3). The convergence across multiple angles confirms this is a strong rename with additional weight now. Upgrading to +3.
- `observation infrastructure` — **sonnet-4-6:** Shorter, still names the claim (code quality is what enables observation). The mechanism-name form reads better in cross-references.
- `code quality as observation infrastructure` — **codex-2:** Long, but the causal bridge is exactly the point and the phrase carries it cleanly.
- `code quality as observation infrastructure` — **opus-4-7-b:** Keep. The "as-observation-infrastructure" framing is the segment's pedagogical move (TST-to-AAD mapping) — renaming would lose the bridge. The slug is long but earns it.
- `code quality as observation infrastructure` — **sonnet-4-6:** The name is a full sentence. It is accurate and precise but unwieldy.

## 88. `comprehension time`

**Alternatives proposed:** `comprehension time`

_category: keep × 4_

- `comprehension time` — **codex-gpt-5-r2:** Strong TST quantity: observable, intuitive, and central.
- `comprehension time` — **opus-4-7-r2:** Acceptable keep — TST. Pairs with `#def-implementation-time` cleanly.
- `comprehension time` — **sonnet-4-6-r2:** "Comprehension time" is the TST term for the cost of constructing local $M_t$.
- `comprehension time` — **sonnet-4-6:** Clean, evocative. "Comprehension" is the right word for constructing a local model of code. Keep.

## 89. `mismatch decomposition`

**Alternatives proposed:** `mismatch decomposition`, `aporia decomposition`

_category: keep × 6, rename × 1_

- `mismatch decomposition` — **codex-gpt-5-r2:** Clean theorem name for reducible model error plus irreducible observation noise.
- `mismatch decomposition` — **haiku-4-5-r2:** Mathematical identity name; clear and adequate.
- `mismatch decomposition` — **haiku-4-5:** Model error + obs noise. Self-descriptive. Keep.
- `mismatch decomposition` — **opus-4-7-b:** Keep. Direct.
- `mismatch decomposition` — **opus-4-7-r2:** Acceptable keep. Names the bias-variance decomposition specialized to mismatch; standard decomposition vocabulary.
- `mismatch decomposition` — **sonnet-4-6-r2:** Precise — model error + observation noise decomposition of mismatch.
- `aporia decomposition` — **gemini-3-1-pro-preview-r2:** Greek alignment (aporia = mismatch).

## 90. `model class fitness`

**Alternatives proposed:** `model class fitness`, `class capacity ceiling`

_category: keep × 4, canonicalize × 1, rename × 1_

- `model class fitness` — **codex-gpt-5-r2:** Strong distinction from model-instance sufficiency and directly supports structural-adaptation triggers.
- `model class fitness` — **gemini-3-1-pro-preview-r2:** Clear parallel to model sufficiency.
- `model class fitness` — **haiku-4-5:** "Fitness" is slightly informal (evolutionary connotations) but works for "best achievable sufficiency within a model class." Acceptable. Alternative would be "model-class-optimality" but "fitness" is more memorable. Keep.
- `model class fitness` — **sonnet-4-6-r2:** "Model class fitness" correctly names the best achievable sufficiency within the model class — $\mathcal{F}(\mathcal{M})$. The "fitness" metaphor is accurate.
- `model class fitness` — **sonnet-4-6-r2:** Prose sometimes uses "best achievable sufficiency" or "maximum model sufficiency within class." The canonical name is "model class fitness" ($\mathcal{F}(\mathcal{M})$).
- `class capacity ceiling` — **audit-471203-incremental:** "Best achievable sufficiency" is the gloss; "Class-Capacity Ceiling" is more evocative. Tentative. [from 13-def-model-class-fitness.md]

## 91. `objective functional`

**Alternatives proposed:** `objective functional`, `teleological objective`

_category: keep × 6, rename × 1_

- `objective functional` — **codex-2:** Slightly clinical, but honest and standard enough once the surrounding formalism lands.
- `objective functional` — **codex-gpt-5-r2:** Technical but appropriate. It is not merely a placeholder name.
- `objective functional` — **gemini-3-1-pro-preview-r2:** Standard.
- `objective functional` — **haiku-4-5:** O_t parametrizes value. Reads as "the functional that captures objectives." Keep.
- `objective functional` — **opus-4-7-r2:** Acceptable keep. Names the chosen functional form for $O_t$.
- `objective functional` — **sonnet-4-6-r2:** $O_t$ parametrizes a value functional — "objective functional" is mathematically precise.
- `teleological objective` — **gemini-2:** "Functional" is overly mathematical for a section slug. "Teleological objective" sets the purpose context.

## 92. `software epistemic property`

**Alternatives proposed:** `software epistemic property`, `software as calibration laboratory`

_category: keep × 4, rename × 1_

- `software epistemic property` — **codex-2:** Plain, strong, and exactly what the segment is doing.
- `software epistemic property` — **opus-4-7-b:** Keep. "Software" locates the domain; "epistemic properties" lines up with AAD §7's epistemic-architecture framing.
- `software epistemic property` — **opus-4-7-r2:** Defended keep. The six properties (P1-P6) are load-bearing for TST's calibration-laboratory framing; "software's epistemic properties" is exactly what they are.
- `software epistemic property` — **sonnet-4-6-r2:** "Software epistemic properties" is precise and the six properties (P1–P6) make the plural "properties" accurate. The "epistemic" qualifier matters — these are properties affecting identification.
- `software as calibration laboratory` — **codex-1:** The current title is accurate but inventory-like. The segment's memorable claim is that software is AAD's calibration lab.

## 93. `strengthen first posture`

**Alternatives proposed:** `strengthen first posture`, `strengthen first`, `attempt the improbable`

_category: rename × 5, keep × 2, canonicalize × 2_

- `strengthen first posture` — **haiku-4-5:** CLAUDE.md "Working Conventions" names this (also via "attempt the improbable"). Work-posture principle, not a theory concept. Already established in project memory. Keep.
- `strengthen first posture` — **opus-1m:** Current name is actionable and precise. Rejecting original brainstorm's alternative ("attempt the improbable").
- `strengthen first posture` — **opus-4-7-r2:** The CLAUDE.md "Working Conventions" section names this as a methodology principle. In the wider corpus it is sometimes "strengthen before softening," "attempt the improbable first," or just "the strengthening move." Canonicalize on "strengthen-first posture" as the named principle; use the variants as elaborations, not paraphrases.
- `strengthen first posture` — **sonnet-4-6-r2:** CLAUDE.md uses "strengthen before softening" and "strengthen-first posture" and "strengthen-first discipline" interchangeably. Standardize on "strengthen-first posture" (two words, hyphenated).
- `strengthen first` — **opus-4-7-b:** Keep. Compact, verb-first, actionable. "Strengthen-first" is doing real work in the codebase (CLAUDE.md §Working Conventions) and has entered the project's working vocabulary. Do not retire.
- `attempt the improbable` — **codex-gpt-5-r2:** Memorable but less directive. Strengthen-first tells an agent what to do; attempt the improbable sounds like a motto.
- `attempt the improbable` — **opus-1m:** Aspirational; less directive than "strengthen-first." Not an improvement.
- `attempt the improbable` — **opus-4-7-b:** Considered the more aspirational form. Reject: "strengthen-first" is directive (tells you *what to do*), "attempt the improbable" is inspirational (tells you *how to feel*). Directive wins for working conventions.
- `attempt the improbable` — **sonnet-4-6:** Retiring "strengthen-first posture" in favor of "attempt the improbable" as the primary working-vocabulary term. "Strengthen-first" can remain as the mechanistic description; "attempt the improbable" is the spirit.

## 94. `$\Delta\rho^\ast$`

**Alternatives proposed:** `adaptive reserve`

_category: add-alias × 3_

- `adaptive reserve` — **codex-2:** This is the right English name and should dominate prose use.
- `adaptive reserve` — **codex-gpt-5-r2:** The symbol should always have the reserve gloss nearby.
- `adaptive reserve` — **sonnet-4-6-r2:** $\Delta\rho^\ast = \alpha R - \rho$ appears in formulas but readers need a prose handle. "Adaptive reserve" is already used in NOTATION.md and LEXICON.md — this vote formalizes it as the canonical alias.

## 95. `$\Delta\rho^\ast$ adaptive reserve`

**Alternatives proposed:** `adaptive reserve`

_category: add-alias × 3_

- `adaptive reserve` — **haiku-4-5:** The English name "adaptive reserve" is already central to LEXICON and should be kept prominent. Shock tolerance; how much disturbance increase before persistence fails. Evocative and operationally meaningful. Keep.
- `adaptive reserve` — **opus-4-7-r2:** Already aliased in prose and in LEXICON — confirm this is the canonical alias and keep it. The prose reads "the adaptive reserve $\Delta\rho^\ast$" cleanly. Maintain the symbol+alias pair.
- `adaptive reserve` — **sonnet-4-6:** NOTATION.md and LEXICON.md already use "adaptive reserve" as the English gloss. This is a successful symbol-to-English match. Keep both — the symbol in equations, the English in prose.

## 96. `$\alpha_2$ a2 adaptive gain sub scope`

**Alternatives proposed:** `adaptive gain regime`

_category: add-alias × 7_

- `adaptive gain regime` — **agent1-original-brainstorm:** Parallel to $\alpha_1$.
- `adaptive gain regime` — **codex-2:** Same reasoning: much easier to read aloud and remember than the raw symbol.
- `adaptive gain regime` — **gemini-2:** Prose-friendly equivalent.
- `adaptive gain regime` — **haiku-4-5:** Parallel to $\alpha_1$ English equivalent. Already used informally. LEXICON entry would formalize.
- `adaptive gain regime` — **opus-1m:** Parallel to $\alpha_1$.
- `adaptive gain regime` — **opus-4-7:** Parallel construction to $\alpha_1$ rename.
- `adaptive gain regime` — **sonnet-4-6:** Parallel to $\alpha_1$. "Adaptive-gain regime" communicates that K is itself a state variable. Same gloss-addition proposal: keep symbol, add English.

## 97. `OODA4 agent as act agent`

**Alternatives proposed:** `OODA4 agent as adaptive agent`, `OODA4 agent as AAD agent`, `logogenic agent mapping`

_category: rename × 6_

- `OODA4 agent as adaptive agent` — **agent1-original-brainstorm:** P1 mechanical, parallel to #developer-as-adaptive-agent rename.
- `OODA4 agent as adaptive agent` — **opus-1m:** Parallel rename; same reasoning.
- `OODA4 agent as adaptive agent` — **opus-4-7-b:** See slug-relics section above.
- `OODA4 agent as AAD agent` — **codex-1:** Same issue as the developer segment: the slug should not force readers to remember an internal shortening.
- `OODA4 agent as AAD agent` — **codex-2:** Same problem as the developer segment, and more visible because AI readers will hit it early.
- `logogenic agent mapping` — **opus-4-7-b:** Considered reframing as a *mapping* rather than an *is-a*. Reject: the segment is the is-a, not the mapping; conflating the two in the rename would narrow the segment's scope.

## 98. `agency`

**Alternatives proposed:** `agency`

_category: keep × 4_

- `agency` — **gemini-3-1-pro-preview-r2:** Clean separation from #scope-adaptive-system.
- `agency` — **haiku-4-5-r2:** Terse and accurate scope delineator.
- `agency` — **opus-4-7-r2:** Defended keep — same as `#scope-adaptive-system`; the pilot rename established this as the canonical pattern.
- `agency` — **sonnet-4-6-r2:** "Agency" is the most load-bearing concept named here — it narrows scope to action with Pearl-level-2 causal contrast. The name is correct and memorable.

## 99. `agent model`

**Alternatives proposed:** `agent model`, `reality model`

_category: keep × 5, rename × 2_

- `agent model` — **haiku-4-5:** Compressed history as state. Self-descriptive. Keep.
- `agent model` — **opus-4-7-b:** Keep. Short, direct.
- `agent model` — **opus-4-7-r2:** Defended keep. Despite "agent model" being slightly generic, the segment's title and body name "the reality model" — but the slug correctly says agent-model because the formulation is *the agent's* representation of the world, not the world itself. The recursive-update derivation depends on this slug.
- `agent model` — **opus-4-7:** Standard. Keep.
- `agent model` — **sonnet-4-6-r2:** Standard vocabulary. Accurate.
- `reality model` — **codex-gpt-5-r2:** The segment title and content name the agent's reality model, not a generic agent model.
- `reality model` — **opus-4-7-r2:** Considered and rejected — the segment's title is "Formulation: The Reality Model" but the slug is more precise. The reality model belongs to *the agent*; "reality model" alone could be confused with the world's true model. Slug should disambiguate.

## 100. `calibration laboratory`

**Alternatives proposed:** `calibration laboratory`

_category: canonicalize × 2, keep × 1_

- `calibration laboratory` — **codex-gpt-5-r2:** Good public-facing TST frame: software is not merely an example but a high-identifiability lab.
- `calibration laboratory` — **gemini-3-1-pro-preview-r2:** Commit to this term over "richest operationalization domain".
- `calibration laboratory` — **opus-4-7-r2:** The phrase appears in TST OUTLINE preamble, CLAUDE.md, and README, but is paraphrased differently — "richest operationalization domain," "best operationalization domain," "high-identifiability domain," "privileged calibration laboratory." Canonicalize on "calibration laboratory" everywhere, with "privileged high-identifiability" as the modifier when full form is needed. The example in the principles file's example-votes section is exactly this.

## 101. `causal hierarchy requirement`

**Alternatives proposed:** `causal hierarchy requirement`, `hierarchy necessity`

_category: keep × 6, rename × 1_

- `causal hierarchy requirement` — **codex-gpt-5-r2:** Clear enough and tied directly to Pearl's hierarchy.
- `causal hierarchy requirement` — **haiku-4-5-r2:** The derived claim is about what's required; the name is accurate.
- `causal hierarchy requirement` — **haiku-4-5:** Pearl's three-level hierarchy is required for planning. Direct, functional name. Keep.
- `causal hierarchy requirement` — **opus-4-7-b:** Keep. Direct application of Bareinboim et al.'s CHT to $Q_O$ evaluation; "requirement" signals this is a must-have, not an option.
- `causal hierarchy requirement` — **opus-4-7-r2:** Acceptable keep. "Requirement" captures the segment's force (Pearl Level 2 is *required* for Q_O evaluation, not optional).
- `causal hierarchy requirement` — **sonnet-4-6-r2:** Precisely named — Level 2 causal hierarchy is REQUIRED for planning.
- `hierarchy necessity` — **gemini-3-1-pro-preview-r2:** Shorter and equally descriptive.

## 102. `chronica $\mathcal C_t$`

**Alternatives proposed:** `chronica`

_category: canonicalize × 2, keep × 1_

- `chronica` — **gemini-targeted-alternatives:** Prose standard for the interaction history.
- `chronica` — **opus-4-7-b:** Greek root fits AAD's philosophical-vocabulary register, the symbol avoids colliding with $\mathcal H$ (entropy), and the singular-non-forkable-trajectory commitment of `#agent-identity` gets more morally heavy over time — "chronica" will age toward the logozoetic scope rather than away from it. Keep.
- `chronica` — **opus-targeted-alternatives:** Concept name is `chronica`; $\mathcal{C}_t$ is the symbol. Both are stable; this row is alias-canonicalize. Confirms.

## 103. `concept dormant variation in correction architecture across a population that become consequential after regime change but is invisible to current persistence analysis`

**Alternatives proposed:** `latent structural diversity`, `latent adaptive capacity`, `latent structural capacity`, `exaptive reserve`

_category: name-unnamed × 4, canonicalize × 4, rename × 1_

- `latent structural diversity` — **codex-gpt-5-r2:** Strong Section III and structural-adaptation term. It names adaptive potential that present fitness measures hide. [original phrasing: dormant structural variation that becomes useful after regime change]
- `latent structural diversity` — **gemini-1:** Extremely useful concept surfaced in the Miller bridge spike. Captures the hidden variation that only becomes consequential under regime change. [original phrasing: unnamed: variation in correction architectures across a population that is invisible to current persistence analysis]
- `latent structural diversity` — **gemini-2:** Proposed in the gap section of OUTLINE.md. Captures the concept perfectly. [original phrasing: unnamed: variation in correction architectures invisible to persistence analysis]
- `latent structural diversity` — **gemini-3-1-pro-preview-r2:** Recasts some forms of technical debt as evolutionary potential. [original phrasing: unnamed: dormant, unused architectural complexity that survives until an environmental shift]
- `latent adaptive capacity` — **gemini-targeted-alternatives:** Describes capacity that isn't currently used but is preserved. [original phrasing: dormant structural variation that becomes useful after regime change]
- `latent adaptive capacity` — **gemini-targeted-alternatives:** Aligns with the earlier rename for structural variation. [original phrasing: unnamed dormant unused architectural complexity that survives until an environmental shift]
- `latent structural capacity` — **gemini-targeted-alternatives:** Maintains the formal name for un-executed resilience. [original phrasing: unnamed variation in correction architectures across a population that is invisible to current persistence analysis]
- `latent structural capacity` — **gemini-targeted-alternatives:** Matches the prior un-executed resilience alias. [original phrasing: unnamed variation in correction architectures invisible to persistence analysis]
- `exaptive reserve` — **gemini-targeted-alternatives:** "Exaptive" specifically means an adaptation used for a new purpose, fitting the regime change requirement perfectly. [original phrasing: dormant structural variation that becomes useful after regime change]

## 104. `concept the engineering vocabulary failure mode in consolidation dynamic the parameter region where forgetting and learning rate jointly fail to admit a viable operating point`

**Alternatives proposed:** `catastrophic forgetting regime`, `stability plasticity feasibility window`, `stability plasticity collapse`, `empty feasibility window`, `plasticity bound failure`, `consolidation starvation`

_category: canonicalize × 6, name-unnamed × 3, rename × 2_

- `catastrophic forgetting regime` — **gemini-targeted-alternatives:** Identifies the specific regime where the stability-plasticity window collapses entirely. [original phrasing: empty stability plasticity feasibility window]
- `catastrophic forgetting regime` — **gemini-targeted-alternatives:** Matches the earlier resolution of this specific limit. [original phrasing: unnamed empty stability plasticity feasibility window in consolidation dynamics]
- `catastrophic forgetting regime` — **gemini-targeted-alternatives:** Resolving another instance of the forgetting limit. [original phrasing: unnamed the AAD expressible failure mode of an empty stability plasticity window]
- `stability plasticity feasibility window` — **gemini-3-1-pro-preview-r2:** Beautifully brackets the survival of an agent constrained by compute. [original phrasing: unnamed: the physical compute bounds on survival between forgetting rate and consolidation cadence]
- `stability plasticity feasibility window` — **gemini-targeted-alternatives:** Standardizes the regime boundary terminology. [original phrasing: unnamed the physical compute bounds on survival between forgetting rate and consolidation cadence]
- `stability plasticity collapse` — **codex-1:** The failure mode is precisely that the feasible interval disappears. Slightly long, but honest and reusable. [original phrasing: unnamed: empty stability-plasticity feasibility window in #consolidation-dynamics]
- `stability plasticity collapse` — **codex-gpt-5-r2:** Better AAD-native failure phrase than catastrophic forgetting when the mechanism matters. [original phrasing: empty stability-plasticity feasibility window]
- `stability plasticity collapse` — **gemini-targeted-alternatives:** Focuses on the two constraints crashing into each other. [original phrasing: catastrophic forgetting regime]
- `empty feasibility window` — **gemini-targeted-alternatives:** The text specifically defines this as the "empty window limit" of the stability-plasticity window. This grounds it in AAD math rather than an ML imported term. [original phrasing: catastrophic forgetting regime]
- `plasticity bound failure` — **gemini-targeted-alternatives:** Emphasizes that the bounds of the window are failing. [original phrasing: catastrophic forgetting regime]
- `consolidation starvation` — **gemini-1:** Adopts "catastrophic forgetting" but specifically names the AAD mechanism: the agent is starved of the consolidation time needed to integrate patterns before they are overwritten. [original phrasing: unnamed: the AAD-expressible failure mode of an empty stability-plasticity window]

## 105. `concept the fourth diagnostic in the satisfaction gap × control regret space when end condition are met but the objective remain unsatisfied`

**Alternatives proposed:** `terminal alignment gap`, `terminal alignment error`, `attainability failure`, `objective misspecification`

_category: name-unnamed × 3, canonicalize × 3, rename × 1_

- `terminal alignment gap` — **gemini-1:** Gives a formal name and symbol ($\delta_\text{align}$) to the fourth diagnostic (achieving terminals but missing the objective), complementing the satisfaction gap and control regret. [original phrasing: unnamed: Terminal alignment error as a formal signal ($\delta_\text{align}$)]
- `terminal alignment gap` — **gemini-targeted-alternatives:** Gap pairs nicely with satisfaction gap, and fits the terminology. [original phrasing: terminal alignment error]
- `terminal alignment gap` — **gemini-targeted-alternatives:** Pairs directly with satisfaction gap. [original phrasing: unnamed terminal alignment error as a formal signal $\delta_\text{align}$]
- `terminal alignment error` — **codex-1:** The DAG-type-closure spike identifies a real gap in the diagnostic vocabulary. This name is plain, disciplined, and fits the existing apparatus. [original phrasing: unnamed: fourth diagnostic where terminal conditions are met but the objective is still missed]
- `terminal alignment error` — **codex-gpt-5-r2:** This is the diagnostic behind satisfaction gap in many examples; it deserves a stable phrase. [original phrasing: terminal reached but $O_t$ unsatisfied]
- `attainability failure` — **gemini-targeted-alternatives:** Pairs directly with the satisfaction gap and control regret. [original phrasing: unnamed fourth diagnostic where terminal conditions are met but the objective is still missed]
- `objective misspecification` — **gemini-targeted-alternatives:** Explicitly names the cause: the operational criteria didn't match the true objective. [original phrasing: terminal alignment error]

## 106. `concept the framing of software TST as AAD epistemically privileged high identifiability measurement substrate`

**Alternatives proposed:** `calibration laboratory`, `privileged grounding domain`, `software calibration laboratory`, `high identifiability testbed`, `software as calibration laboratory`, `calibration laboratory move`, `calibration domain calibration lab`, `calibration domain`

_category: name-unnamed × 5, canonicalize × 3, rename × 2_

- `calibration laboratory` — **codex-2:** This phrase deserves to be promoted to the stable short name; it is central to TST's architectural role. [original phrasing: unnamed: software as AAD's privileged high-identifiability calibration laboratory]
- `calibration laboratory` — **gemini-targeted-alternatives:** A highly functional grounding metaphor for TST's role. [original phrasing: unnamed calibration laboratory framing for software TST]
- `calibration laboratory` — **opus-4-7:** Load-bearing distinction vs. "best operationalization domain"; TST's OUTLINE.md preamble now uses this. Canonical. Keep. [original phrasing: unnamed: "calibration laboratory" framing for software/TST]
- `privileged grounding domain` — **gemini-targeted-alternatives:** Describes exactly what software is for AAD: the domain where formal properties are cleanly grounded without extra transfer assumptions. [original phrasing: calibration laboratory]
- `software calibration laboratory` — **gemini-targeted-alternatives:** Formalizes TST's role as the cleanly identifiable testbed for AAD. [original phrasing: unnamed software as AAD s privileged high identifiability calibration laboratory]
- `high identifiability testbed` — **gemini-targeted-alternatives:** Captures the "high-identifiability" empirical claim perfectly. [original phrasing: calibration laboratory]
- `software as calibration laboratory` — **opus-4-7-r2:** The TST preamble names software as AAD's "privileged high-identifiability calibration laboratory," and CLAUDE.md says "calibration-lab framing" is a methodology principle. There is no single segment, slug, or principle entry that names this commitment — it is a load-bearing methodological move that lives only in preambles and the README. Promoting it to a named principle (likely a `disc-` or `norm-` segment, or a methodological entry in CLAUDE.md / FORMAT.md) would let downstream segments cite it explicitly when invoking it. [original phrasing: unnamed: software's role as calibration laboratory, named-in-prose-but-not-in-slug]
- `calibration laboratory move` — **opus-4-7-r2:** Confirmation with new reasoning — my own r2 named "software-as-calibration-laboratory" as a name-unnamed; reading peers, Codex (+3) and Sonnet (+3) and Gemini (+3) all separately reached "calibration laboratory" as a canonicalize vote. Three agents converging on the canonical phrase suggests the term is ripe; what's *unnamed* is the methodological *move* of using software as the calibration laboratory rather than just an instance. Calling it "the calibration-laboratory move" lets it function as a named strategic principle the project can invoke. [original phrasing: unnamed: the move where AAD treats software not as instantiation but as TST's epistemically privileged measurement substrate]
- `calibration domain calibration lab` — **agent1-original-brainstorm:** Low priority. Concept of a privileged domain for identification within a theoretical framework is itself a reusable meta-move other projects could borrow. [original phrasing: unnamed: calibration-laboratory framing as reusable meta-move]
- `calibration domain` — **opus-4-7-b:** CLAUDE.md §7 names TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measured exactly." The *concept* (a privileged domain for identification of a theoretical framework's quantities) is itself a reusable meta-move for any domain instantiation. "Calibration domain" names it. Low priority but opens a useful slot. [original phrasing: unnamed: the calibration-laboratory concept applied outside TST]

## 107. `convention hierarchy c1 c2 c3`

**Alternatives proposed:** `convention hierarchy`, `continuation hierarchy`

_category: rename × 4, canonicalize × 1_

- `convention hierarchy` — **opus-1m:** Disagreeing with original brainstorm's P4 "rename to continuation hierarchy." The rename churn (every C1/C2/C3 reference across segments needs updating) outweighs the Lewisian-baggage benefit. Working vocabulary is stable; keep. Explicit-keep rather than absence-of-vote because I considered the rename.
- `convention hierarchy` — **opus-4-7-r2:** Same vote; paired with Correlation Hierarchy.
- `convention hierarchy` — **sonnet-4-6:** Keep — see Correlation Hierarchy note.
- `continuation hierarchy` — **agent1-original-brainstorm:** Would lose Lewisian game-theoretic baggage; more self-descriptive. Same C1/C2/C3 abbreviations still work. Conditional; may be over-reach.
- `continuation hierarchy` — **opus-4-7-b:** "Convention" collides with the game-theory / Lewis sense (social conventions, conventions-as-equilibrium-selection), which is a *different* and unrelated concept that some AAD readers will have strongly in mind. What the C-hierarchy actually indexes is the choice of *continuation policy* for value-object evaluation (one-step, receding-horizon, Bellman). "Continuation hierarchy" is self-announcing; the C1/C2/C3 abbreviations still work, and since they map to continuation it even becomes a mild mnemonic. Risk is churn. Mild preference but not forceful.

## 108. `cycle vs loop`

**Alternatives proposed:** `cycle vs loop`, `cycle loop distinction`

_category: keep × 3, canonicalize × 1_

- `cycle vs loop` — **gemini-targeted-alternatives:** [prose moved from candidate column]: "`maintain distinction`" — The distinction (loop = structural topology, cycle = one traversal) is a core piece of vocabulary.
- `cycle vs loop` — **opus-4-7-b:** [prose moved from candidate column]: "*(keep both; maintain distinction)*" — README §"Loop vs. Cycle" makes this distinction load-bearing (loop = structural topology, cycle = one traversal). The distinction is one of AAD's best small naming moves and should be enforced in every segment.
- `cycle vs loop` — **opus-4-7:** See above — the two-word disambiguation is one of the theory's most useful vocabulary moves. Keep.
- `cycle loop distinction` — **opus-targeted-alternatives:** The row names the *distinction* not a candidate. The substantive position is that loop = topology, cycle = traversal — a distinction worth preserving. Canonicalize the row's referent to "the cycle / loop distinction" as a named architectural commitment.

## 109. `developer as act agent`

**Alternatives proposed:** `developer as adaptive agent`, `developer as AAD agent`, `developer agent mapping`, `developer as agent`

_category: rename × 9_

- `developer as adaptive agent` — **agent1-original-brainstorm:** P1 mechanical. Drops framework-name dependency from slug; matches LEXICON agent-class vocabulary; won't rot under future renames.
- `developer as adaptive agent` — **opus-1m:** Mechanical rename. "ACT" era slug is a 2026-04-16 relic. "Adaptive agent" matches LEXICON vocabulary; framework-name-free slug won't rot under future renames.
- `developer as adaptive agent` — **opus-4-7-b:** See slug-relics section above.
- `developer as AAD agent` — **agent1-original-brainstorm:** Perpetuates pattern of embedding framework name in slug; fragile. Rejected.
- `developer as AAD agent` — **codex-1:** The slug should match the segment heading and avoid the unexplained "act" abbreviation. The expansion cost is needless here.
- `developer as AAD agent` — **codex-2:** `act-agent` looks like a stale internal abbreviation after the ACT → AAD rename.
- `developer as AAD agent` — **opus-4-7-b:** Considered preserving the exact-parallel naming. Reject: embedding a framework acronym in a slug is exactly the rot pattern we just cleaned up; don't re-introduce it.
- `developer agent mapping` — **agent1-original-brainstorm:** Reframes from "developer is an agent" to "here's the mapping"; cleaner pedagogically. Alternative to the preferred #developer-as-adaptive-agent.
- `developer as agent` — **agent1-original-brainstorm:** Too generic.

## 110. `effect spiral`

**Alternatives proposed:** `effect spiral`, `runaway mismatch cascade`, `adversarial feedback loop`, `destabilization vortex`, `coupling cascade`, `breakdown cascade`

_category: rename × 4, keep × 3, add-alias × 1_

- `effect spiral` — **codex-1:** Memorable without being whimsical. It is the kind of pattern-name people will actually reuse in discussion.
- `effect spiral` — **codex-gpt-5-r2:** Excellent name for the positive-feedback breakdown mechanism.
- `effect spiral` — **opus-targeted-alternatives:** Per `#der-adversarial-destabilization` and `#deriv-strategic-composition`: positive-feedback breakdown where degraded model causes degraded actions causes further degradation. "Spiral" carries the *accelerating* feature (not a steady-state mismatch but a runaway), and "effects" specifies the locus (the agent's effects on its environment, not its inputs). Pairs well with the "death spiral" reference in `#result-persistence-condition`. Strong keep.
- `runaway mismatch cascade` — **gemini-targeted-alternatives:** Focuses on the mismatch acceleration ($\Vert\delta\Vert \uparrow$). Connects to "cascade" seen elsewhere (e.g. orient cascade).
- `adversarial feedback loop` — **gemini-targeted-alternatives:** Explicitly names the cause (adversarial coupling) and the mechanism (positive feedback).
- `destabilization vortex` — **gemini-targeted-alternatives:** A bit more descriptive than spiral but slightly less formal.
- `coupling cascade` — **opus-targeted-alternatives:** Considered as more formal alternative. Loses the *runaway* sense that "spiral" carries — cascades can be bounded; spirals usually aren't. Rejected.
- `breakdown cascade` — **opus-targeted-alternatives:** Same critique. Rejected.

## 111. `event driven dynamic`

**Alternatives proposed:** `event driven dynamic`

_category: keep × 6_

- `event driven dynamic` — **gemini-3-1-pro-preview-r2:** Accurate and descriptive.
- `event driven dynamic` — **haiku-4-5-r2:** Architectural choice name; clear and self-descriptive.
- `event driven dynamic` — **haiku-4-5:** Events in continuous time. Self-descriptive. Keep.
- `event driven dynamic` — **opus-4-7-b:** Keep. "Event-driven" carries correct engineering baggage (versus turn-based / synchronous).
- `event driven dynamic` — **opus-4-7-r2:** Acceptable keep. Names the formulation choice (event-driven, $\tau$-indexed, vs continuous-time-indexed).
- `event driven dynamic` — **sonnet-4-6-r2:** Accurate and precise for the continuous-time event-driven formulation.

## 112. `evidence starvation`

**Alternatives proposed:** `evidence starvation`, `depth attenuated correction`, `downstream evidence gating`

_category: add-alias × 2, canonicalize × 2, rename × 1_

- `evidence starvation` — **codex-gpt-5-r2:** Excellent alias for downstream edges receiving fewer tests because upstream steps must succeed first.
- `evidence starvation` — **opus-4-7-r2:** Confirmation with new reasoning — both Sonnet (+3 add-alias) and Codex (+3 add-alias) and Gemini (+3 in synthesized) reached this term independently. The cross-architecture convergence is striking and suggests the term is doing real work. My own r2 votes didn't explicitly canonicalize this; I should. The phrase appears in `der-chain-confidence-decay` Discussion and `der-observability-dominance` and is the natural prose handle for the downstream-edge-update-attenuation phenomenon. Three-architecture convergence on the *exact phrase* (not synonyms) crystallizes the case.
- `evidence starvation` — **opus-targeted-alternatives-v2:** Per `der-chain-confidence-decay`: "downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$." Used in 4+ segments (`#deriv-strategic-dynamics` B.2, `#der-chain-confidence-decay` triple-depth-penalty, `#def-strategic-tempo` AND-chain interactions, `#deriv-strategic-dynamics` Discussion). Triple-architecture convergence in r1 (Codex +3, Gemini +3, Sonnet +3) — confirms with my independent read. Canonicalize as the project-default term.
- `depth attenuated correction` — **gemini-targeted-alternatives:** Describes the mathematical mechanism (effective observation rate dropping geometrically).
- `downstream evidence gating` — **gemini-targeted-alternatives:** Captures the AND-chain gating effect.

## 113. `formal expression`

**Alternatives proposed:** `formal expression`

_category: keep × 3_

- `formal expression` — **codex-2:** Strong public-API header: unambiguous and better than any prettier synonym I can think of.
- `formal expression` — **opus-4-7-b:** Keep. Precisely-what-it-says; the word "Formal" is load-bearing (distinguishes from informal discussion). Any rename would cost the 110-segment ripple without benefit.
- `formal expression` — **opus-4-7:** Section header is project-wide; renaming would ripple everywhere and buys nothing. Keep. Every segment uses this.

## 114. `graph structure uniqueness`

**Alternatives proposed:** `strategy DAG sufficiency`, `strategy DAG uniqueness`, `graph structure uniqueness`, `DAG uniqueness`, `DAG structure derivation`, `graph structure sufficiency`

_category: rename × 7, canonicalize × 2, keep × 2_

- `strategy DAG sufficiency` — **codex-1:** The segment explicitly proves sufficiency, not necessity. "Uniqueness" overclaims, while "strategy DAG" names the actual object.
- `strategy DAG sufficiency` — **codex-gpt-5-r2:** The segment proves sufficiency, not full necessity or uniqueness. This is a scope-honesty correction.
- `strategy DAG sufficiency` — **codex-gpt-5-r2:** Same point in prose. The result is important, but the current noun overclaims.
- `strategy DAG uniqueness` — **codex-gpt-5-r2:** More subject-specific than generic graph structure.
- `strategy DAG uniqueness` — **codex-gpt-5-r2:** The uniqueness claim is about the strategy representation, not arbitrary graphs.
- `strategy DAG uniqueness` — **opus-4-7-b:** The current slug is somewhat generic ("graph structure" — which graph?). The segment's content is specifically the DAG-with-Markov-property uniqueness for the strategy layer ($\Sigma_t$). Scoping the slug to strategy-DAG makes it findable and binds it to the concept it's about. Modest preference.
- `graph structure uniqueness` — **haiku-4-5:** Four postulates + causal sufficiency → DAG with Markov property (CMC theorem). "Uniqueness" is precise; reads as "why the strategy must be a DAG." Keep.
- `graph structure uniqueness` — **opus-4-7:** Alternative keep-vote. The name has citation velocity already. If rename is disruptive enough to rebaseline cross-refs, keep.
- `DAG uniqueness` — **gemini-3-1-pro-preview-r2:** More specific to the Strategy DAG.
- `DAG structure derivation` — **opus-4-7:** "Uniqueness" overpromises — the actual result is "four operational postulates + causal sufficiency force a DAG-with-Markov-factorization." The *necessity* direction is noted open (strategy-dag Discussion). "Derivation" is honest about what is proved.
- `graph structure sufficiency` — **codex-1:** Better epistemically than "uniqueness" but still too generic; the reader needs to know this is about the strategy DAG.

## 115. `interaction channel classification`

**Alternatives proposed:** `signal reception regime`, `interaction channel classification`, `recipient regime`, `channel classification`, `recipient regime classification`, `interaction regime`, `recipient side channel taxonomy`

_category: rename × 12, keep × 4_

- `signal reception regime` — **codex-1:** The four regimes are the actual memorable object here. The current name reads like taxonomy boilerplate.
- `signal reception regime` — **codex-2:** Current name is clinical and forgettable; the segment really names how incoming signals land.
- `signal reception regime` — **codex-gpt-5-r2:** Better than recipient regimes: it names the actual object the reader reasons about, namely how incoming events land for the recipient.
- `interaction channel classification` — **codex-gpt-5-r2:** Slightly long, but honest: the four regimes are recipient-side channel classes.
- `interaction channel classification` — **haiku-4-5:** Four-regime partition (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries. Name is accurate but verbose. Acceptable; no strong alternative emerges. Keep.
- `interaction channel classification` — **opus-4-7-b:** Alternative: keep. "Interaction channel" keeps the symmetry with `#agent-opacity`'s emitter-side four-regime classification; the recipient-side structure is one half of a pair. On balance this consideration outweighs the legibility gain. Net: weak keep.
- `interaction channel classification` — **sonnet-4-6:** Accurate but long. In conversation this will be called "the four-regime classification" or "the recipient-side classification."
- `recipient regime` — **codex-gpt-5-r2:** The full slug is accurate but long. Recipient regimes names the four-way classification more compactly.
- `recipient regime` — **sonnet-4-6-r2:** Codex proposed `#der-recipient-regimes` (+2). I had proposed `der-channel-classification` (+2), Gemini also proposed `#der-channel-classification` (+1). Codex's "recipient-regimes" is more distinctive: "channel classification" sounds like a generic taxonomy, but "recipient regimes" signals that the classification is from the recipient's perspective (the four regimes are about what the *receiving* agent experiences). New agreement with Codex's framing over my own.
- `channel classification` — **gemini-3-1-pro-preview-r2:** "Interaction" is implied.
- `channel classification` — **sonnet-4-6-r2:** "Interaction-channel-classification" is four words. The key concept is the four-regime classification of recipient-side channels. "Channel classification" is shorter and still distinctive within AAD.
- `recipient regime classification` — **opus-4-7-b:** The segment's headline is the *recipient-side* four-regime classification (Informative / magnitude-shock / structural-shock / ambient-noise); the current slug buries the recipient-side framing under "interaction channel." Weak preference for the recipient-explicit form.
- `recipient regime classification` — **opus-4-7:** Makes the recipient-side orientation explicit at the name level, since the emitter-side version (#agent-opacity) now exists as a dual. Current name doesn't disambiguate emitter-vs-recipient.
- `recipient regime classification` — **sonnet-4-6:** Shorter, names the perspective (recipient-side) which is the segment's distinctive contribution. The four regimes (Informative/magnitude-shock/structural-shock/ambient-noise) are what readers will cite.
- `interaction regime` — **gemini-2:** "Classification" is passive. "Regimes" conveys the active shift in dynamics.
- `recipient side channel taxonomy` — **codex-1:** Too procedural and too long. This would make the concept harder to say, not easier.

## 116. `mismatch signal $\delta$`

**Alternatives proposed:** `mismatch signal`

_category: keep × 2, canonicalize × 1_

- `mismatch signal` — **gemini-targeted-alternatives:** Fits the aporia interpretation better than error/residual.
- `mismatch signal` — **opus-4-7:** In contrast with "error" or "residual"; the word foreshadows the aporia interpretation. Keep.
- `mismatch signal` — **opus-targeted-alternatives:** Per `#def-mismatch-signal` and LEXICON. The symbol-decoration is alias-only; the concept name is "mismatch signal." Confirms across architectures.

## 117. `persist condition`

**Alternatives proposed:** `persistence condition`

_category: keep × 1, canonicalize × 1, rename × 1_

- `persistence condition` — **gemini-targeted-alternatives:** Already the formally correct name.
- `persistence condition` — **opus-targeted-alternatives:** Concur — "persist condition" appears nowhere as a chosen form. "Persistence condition" is established in `LEXICON.md` and `#result-persistence-condition`. The shorter form is a typo or paraphrase, not an alternative; canonicalize.
- `persistence condition` — **sonnet-4-6:** Wait — this IS the name already. Correct name. Keep.

## 118. `strategy DAG $\Sigma_t$`

**Alternatives proposed:** `strategy DAG`

_category: keep × 3_

- `strategy DAG` — **agent1-original-brainstorm:** Adopted directly from probabilistic graphical models lit; baggage transfers correctly.
- `strategy DAG` — **opus-1m:** Adopted from probabilistic graphical models; keep.
- `strategy DAG` — **opus-4-7-b:** Adopted directly from the graphical-models literature; "DAG" is pronounceable as a noun and carries precisely the right structural picture. Keep.

## 119. `$\alpha_1$ a2 fixed gain sub scope`

**Alternatives proposed:** `derived gain regime`, `fixed gain regime`

_category: add-alias × 8_

- `derived gain regime` — **agent1-original-brainstorm:** English equivalent for prose. "This lands in the derived-gain regime" reads naturally. Keep $\alpha_1$ as shorthand symbol.
- `derived gain regime` — **haiku-4-5:** In prose, "$\alpha_1$ regime" is hard to distinguish from "a₁ regime" when read aloud. English equivalent "derived-gain regime" emphasizes that A2' is derived under directional fidelity. Would keep Greek symbols in formal segments and NOTATION; add English equivalent to LEXICON for prose fluency. Prose-accessibility enhancement, not a symbol rename.
- `derived gain regime` — **opus-1m:** English equivalent for prose use. Keep $\alpha_1$ as symbol.
- `derived gain regime` — **opus-4-7-b:** "The Kalman case lands in $\alpha_1$" requires a decoder ring; "the Kalman case lands in the derived-gain regime" is self-contained. Symbol stays as shorthand; English owns the prose register.
- `derived gain regime` — **opus-4-7:** "Lands in $\alpha_1$" is cryptic in prose; "lands in the derived-gain regime" reads. Keep $\alpha_1$ as symbolic shorthand but surface the English in segment text.
- `derived gain regime` — **sonnet-4-6:** The prose term "sub-scope $\alpha_1$" is impenetrable outside the sector-condition-derivation context. "Derived-gain regime" would read naturally in prose — "this agent lands in the derived-gain regime." NOTATION.md should add this gloss; segments could use the English in Discussion and Greek in Formal Expression. Propose adding the English gloss without retiring the symbol.
- `fixed gain regime` — **codex-2:** Keep the symbol, but prose should preferentially use the English name when possible.
- `fixed gain regime` — **gemini-2:** Prose-friendly equivalent to the mathematical symbol.

## 120. `adaptive system`

**Alternatives proposed:** `adaptive system`

_category: keep × 4_

- `adaptive system` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep, but flag prior-art baggage)" — "Adaptive system" carries Ashby/cybernetic prior-art weight (good regulators, internal-model principle). AAD's use is information-theoretic, not regulator-theoretic. Auditor floated "uncertainty-bounded system" / "informationally-open system" as alternatives but did NOT advocate rename — well-anchored term. [from 05-scope-adaptive-system.md]
- `adaptive system` — **haiku-4-5-r2:** Precise scope statement; the name surfaces exactly what is in scope.
- `adaptive system` — **opus-4-7-r2:** Defended keep — and the canonical illustration of the subject-noun-first principle from the pilot. The slug names what the scope delimits (adaptive systems), not the segment's role (it states *some scope*). Pairs with `#scope-agency` cleanly.
- `adaptive system` — **sonnet-4-6-r2:** Descriptive of the actual broadest scope boundary. Clear, memorable, accurate.

## 121. `calibration laboratory calibration lab`

**Alternatives proposed:** `calibration laboratory`

_category: canonicalize × 3_

- `calibration laboratory` — **gemini-targeted-alternatives:** Consistently uses the full phrase instead of the abbreviation.
- `calibration laboratory` — **opus-targeted-alternatives:** Doubled phrasing in the row is a paraphrase artifact. Canonicalize to the longer form for formal use; "calibration lab" can be informal short.
- `calibration laboratory` — **sonnet-4-6-r2:** Currently appears as "richest operationalization domain," "best operationalization domain," "privileged high-identifiability calibration laboratory," and "calibration laboratory." The TST OUTLINE.md preamble and `obs-software-epistemic-properties` both use "calibration laboratory" as the correct framing, but earlier versions use the paraphrase forms. Standardize on "calibration laboratory" (full form) in first use; "calibration lab" acceptable in subsequent informal references.

## 122. `change distance`

**Alternatives proposed:** `change distance`, `edit distance`

_category: keep × 4, rename × 1_

- `change distance` — **codex-gpt-5-r2:** Clean software metric name. Avoids over-theorizing a practical concept.
- `change distance` — **opus-4-7-r2:** Acceptable keep — TST. The lexical/file/module/service ladder is the substance; "change distance" is the right name for the metric.
- `change distance` — **opus-targeted-alternatives:** TST segment defines the lexical/file/module/service hierarchy as a distance measure on changesets. "Distance" is the right metric word; "change" specifies the domain. Strong keep.
- `change distance` — **sonnet-4-6-r2:** "Change distance" names the lexical < file < module < service hierarchy precisely.
- `edit distance` — **opus-targeted-alternatives:** Conflicts with computer-science "edit distance" (Levenshtein), which has different metric properties. Rejected — collision with established term.

## 123. `composite agent`

**Alternatives proposed:** `composite agent`

_category: keep × 4_

- `composite agent` — **codex-gpt-5-r2:** Composite agent is the correct scope noun.
- `composite agent` — **gemini-3-1-pro-preview-r2:** Standard.
- `composite agent` — **opus-4-7-r2:** Acceptable keep. Names the composite-agent boundary (the disjunction of three alignment routes); slug-form is correct (subject-noun is "composite-agent").
- `composite agent` — **sonnet-4-6-r2:** Precise and descriptive. Teleological alignment for composite-agent status is exactly what this scope names.

## 124. `coupled update dynamic`

**Alternatives proposed:** `coupled update dynamic`

_category: keep × 5_

- `coupled update dynamic` — **codex-1:** Slightly textbook, but it says exactly what the logogenic section needs and pairs cleanly with directed separation.
- `coupled update dynamic` — **codex-2:** Generic, but faithful; the novelty is in "coupled," not in inventing a flashier noun.
- `coupled update dynamic` — **codex-gpt-5-r2:** Good Class-2 dynamics name.
- `coupled update dynamic` — **opus-4-7-r2:** Acceptable keep — logogenic-agents. Names the formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ that survives the Class-2 scope exit.
- `coupled update dynamic` — **sonnet-4-6-r2:** "Coupled update dynamics" precisely names the $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ formulation without decomposition.

## 125. `mismatch dynamic`

**Alternatives proposed:** `mismatch dynamic`, `mismatch dynamic drift and noise regime`

_category: keep × 5, rename × 1_

- `mismatch dynamic` — **gemini-3-1-pro-preview-r2:** Accurate.
- `mismatch dynamic` — **haiku-4-5:** Mismatch evolution ODE. Self-descriptive. Keep.
- `mismatch dynamic` — **opus-4-7-b:** Keep.
- `mismatch dynamic` — **opus-4-7-r2:** Acceptable keep. The hypothesis is the linear-ODE model for mismatch evolution; "mismatch dynamics" is the right scope. The hypothesis-vs-result distinction is captured by the type prefix.
- `mismatch dynamic` — **sonnet-4-6-r2:** "Mismatch dynamics" names the ODE governing mismatch evolution. Accurate and minimal.
- `mismatch dynamic drift and noise regime` — **audit-471203-incremental:** Title doesn't surface that two distinct dynamic regimes (Model D drift / Model S noise) are introduced — and they produce different adversarial scaling laws (squared vs 3/2). Tentative. [from 23-hyp-mismatch-dynamics.md]

## 126. `sector condition stability`

**Alternatives proposed:** `sector condition stability`, `sector stability`

_category: keep × 5, rename × 1_

- `sector condition stability` — **haiku-4-5-r2:** Strong name; "sector condition" is load-bearing prose term; "stability" correctly names the property. Rename would weaken.
- `sector condition stability` — **haiku-4-5:** Descriptive compound. "Sector condition" carries baggage from control theory (Lyapunov methods); "stability" makes the implication explicit. Slightly verbose but clear. Acceptable.
- `sector condition stability` — **opus-4-7-b:** Keep.
- `sector condition stability` — **opus-4-7-r2:** Acceptable keep. Pairs with `#result-sector-persistence-template` and `#result-persistence-condition`; the three together name the Lyapunov-derived stability cluster.
- `sector condition stability` — **sonnet-4-6-r2:** Precise — nonlinear stability via the sector condition.
- `sector stability` — **codex-gpt-5-r2:** Sector stability is cleaner. Keep condition in prose if needed for theorem lineage.

## 127. `stability plasticity window`

**Alternatives proposed:** `stability plasticity window`, `consolidation feasibility window`

_category: keep × 3, rename × 1_

- `stability plasticity window` — **codex-gpt-5-r2:** Excellent name for the feasible forgetting-rate interval.
- `stability plasticity window` — **gemini-targeted-alternatives:** Essential framing for the consolidation regime bounded by forgetting and rigidity.
- `stability plasticity window` — **opus-targeted-alternatives:** Per `#form-consolidation-dynamics`: the regime where the agent must be stable enough to retain learned structure but plastic enough to consolidate new evidence. The phrase compactly names a feasibility region in a 2D parameter space (stability, plasticity). Standard ML-ops vocabulary (Grossberg's stability-plasticity dilemma). Keep — confirms across architectures.
- `consolidation feasibility window` — **opus-targeted-alternatives:** More technically transparent but the segment uses "stability-plasticity window" precisely because the literature does. Rejected.

## 128. `structural adaptation necessity`

**Alternatives proposed:** `structural adaptation necessity`, `adaptation necessity`

_category: keep × 5, rename × 1_

- `structural adaptation necessity` — **haiku-4-5-r2:** The subject-noun is precise — structural adaptation is the thing whose necessity is established.
- `structural adaptation necessity` — **haiku-4-5:** When parametric update fails. Reads as "necessity of structural adaptation." Acceptable. Keep.
- `structural adaptation necessity` — **opus-4-7-b:** Keep — "necessity" signals this is a derived need ("when parametric update fails, structural adaptation *must* happen").
- `structural adaptation necessity` — **opus-4-7-r2:** Defended keep. "Structural adaptation" pairs with "parametric adaptation" as the framework's load-bearing distinction; "necessity" captures that the result is a derived condition (when parametric update fails, structural adaptation is *required*, not optional).
- `structural adaptation necessity` — **sonnet-4-6-r2:** "Structural adaptation necessity" names the when-parametric-update-fails result correctly.
- `adaptation necessity` — **gemini-3-1-pro-preview-r2:** "Structural" is redundant in context, shortens the slug nicely.

## 129. `task terminal stance`

**Alternatives proposed:** `task terminal stance`, `terminable agent stance`, `golem stance`

_category: keep × 3, rename × 2_

- `task terminal stance` — **gemini-2:** Excellent, crisp description of an agent whose persistence ends upon success. Keep.
- `task terminal stance` — **gemini-targeted-alternatives:** Specific continuity stance definition.
- `task terminal stance` — **opus-targeted-alternatives:** Per LEXICON Continuity Stance table: "Task-terminal — Persists instrumentally; termination is success — Archetype: Golem." The hyphenation matters (it's a stance *characterized by* task-terminality), and the term names a precise position on a 5-stance spectrum (indifferent / task-terminal / instrumentally-continuous / morally-continuous / negotiated). Keep.
- `terminable agent stance` — **opus-targeted-alternatives:** Considered. Loses the *task* specificity — task-terminal differs from instrumentally-continuous precisely in that the *task completion* is the success criterion, not bare continuation. Rejected.
- `golem stance` — **opus-targeted-alternatives:** Uses the archetype as the term. Considered: more memorable. Rejected: the framework reserves archetypes for archetype-illustration; the formal term should describe the stance, not its avatar.

## 130. `triple depth penalty`

**Alternatives proposed:** `triple depth penalty`, `depth gated decay triad`, `tripartite chain attenuation`, `compounding depth penalty`, `compounding depth cost`

_category: rename × 4, canonicalize × 2, keep × 1_

- `triple depth penalty` — **codex-gpt-5-r2:** Very useful phrase for confidence decay, evidence starvation, and cognitive cost compounding with depth.
- `triple depth penalty` — **opus-targeted-alternatives-v2:** Per `#der-chain-confidence-decay` line 54: "Chain depth creates three independent penalties... confidence decay... evidence starvation... cognitive cost." The phrase "triple depth penalty" is the segment's name for the compound. Triple-architecture convergence in r1 — confirms. The phrase is a load-bearing finding (composes three independently-derived penalty mechanisms).
- `triple depth penalty` — **opus-targeted-alternatives:** Per `#form-strategy-complexity-cost`: three independent depth-penalty mechanisms (cognitive cost, evidence starvation, interaction-horizon truncation) compound on AND-chain depth. "Triple" specifies the *count* of mechanisms; "depth penalty" specifies the structural cost. Memorable, accurate.
- `depth gated decay triad` — **gemini-targeted-alternatives:** "Gating" is the mechanism (evidence starvation), "decay" is the confidence drop.
- `tripartite chain attenuation` — **gemini-targeted-alternatives:** A bit dry, but accurate to the 3 compounding penalties.
- `compounding depth penalty` — **opus-targeted-alternatives-v2:** Considered. "Compounding" makes the multiplicative-three-mechanisms structure visible. Rejected: "triple" is more memorable; "compounding" makes the slug 23 chars vs 19. The current term won the Sonnet/Codex r1 vote on substance.
- `compounding depth cost` — **opus-targeted-alternatives:** Loses the *three* specificity that "triple" provides. The segment's claim is precisely that *three* mechanisms align — this is load-bearing for the strength of the claim. Rejected.

## 131. `update gain`

**Alternatives proposed:** `update gain`, `update gain uncertainty ratio principle`, `epistemic gain`

_category: keep × 4, canonicalize × 1, rename × 1_

- `update gain` — **haiku-4-5-r2:** Precise subject-noun; "update gain" is the empirical quantity being characterized.
- `update gain` — **haiku-4-5:** Optimal update weighting. Self-descriptive. Keep.
- `update gain` — **opus-4-7-r2:** Defended keep. The uncertainty-ratio principle $\eta^\ast = U_M / (U_M + U_o)$ is iconic; renaming would lose the load-bearing prose convention. The segment's title "Update Gain" matches the slug.
- `update gain` — **sonnet-4-6-r2:** "Update gain" is canonical AAD vocabulary. $\eta^\ast = U_M / (U_M + U_o)$ is THE gain formula.
- `update gain uncertainty ratio principle` — **audit-471203-incremental:** Standard term; doesn't carry the *uncertainty-ratio* insight. The equation tag's "uncertainty-ratio-principle" is more evocative. Brief-grade hint, possibly visible in title. [from 20-emp-update-gain.md]
- `epistemic gain` — **codex-gpt-5-r2:** Loses correct Kalman/control baggage and creates avoidable overlap with epistemic unity.

## 132. `$\kappa_{\text{processing}}$`

**Alternatives proposed:** `processing coupling`, `epistemic capacity`, `processing coupling coefficient`

_category: add-alias × 7_

- `processing coupling` — **codex-1:** The symbol is fine in equations, but prose should default to the English name. It clarifies the architectural quantity immediately.
- `processing coupling` — **codex-2:** Better spoken noun than the symbol, especially outside equations.
- `processing coupling` — **codex-gpt-5-r2:** Good prose handle for ambiguity-modulation coupling.
- `processing coupling` — **opus-4-7:** Symbol is fine but the name "$\kappa$-as-scalar" was explicitly retired as a category error — the live reading is "processing coupling as a diagnostic for Class 3 agents." Surface that English name consistently.
- `processing coupling` — **sonnet-4-6-r2:** The conditional mutual information measure of goal-to-epistemic coupling in Class 3 agents. "Processing coupling" is the English that appears in prose (e.g., "the degree of coupling in partially modular architectures"). Canonicalize as the prose alias.
- `epistemic capacity` — **gemini-2:** Gives a physical intuition to processing bandwidth.
- `processing coupling coefficient` — **sonnet-4-6:** The symbol appears in #directed-separation where the English name "processing coupling" is used. The coefficient subscript form "$\kappa_{\text{processing}}$" is unwieldy in prose. Adding "processing-coupling coefficient" to LEXICON.md's Terms to Be Added section would help.

## 133. `bia bound derivation`

**Alternatives proposed:** `bia bound derivation`, `class 2 bia bound`

_category: keep × 3, rename × 1_

- `bia bound derivation` — **haiku-4-5:** Class-2 observation-ambiguity bias-bound constant C. "Bias-bound derivation" is compound but clear. Keep.
- `bia bound derivation` — **opus-4-7:** Newly landed appendix; name matches content. Keep.
- `bia bound derivation` — **sonnet-4-6:** Describes the content precisely (deriving a bound on bias). The "derivation" suffix correctly signals this is an appendix-derivation type. Keep.
- `class 2 bia bound` — **opus-4-7-b:** Current slug is generic — many things in AAD are "bias bound derivations." The segment specifically derives the constant $C$ in the **Class-2 observation-ambiguity** bias bound. Scoping the slug to "class-2" makes it findable and distinct.

## 134. `causal structure`

**Alternatives proposed:** `causal structure`

_category: keep × 4_

- `causal structure` — **gemini-3-1-pro-preview-r2:** Standard.
- `causal structure` — **haiku-4-5:** Irreducible causal structure (postulate). Self-descriptive. Keep.
- `causal structure` — **opus-4-7-r2:** Acceptable keep. "Causal structure" names what the postulate asserts: an irreducible causal structure on the agent-environment loop (causes precede effects, observation channels are not causally upstream of the world they observe). Could be renamed to "#post-temporal-causal-ordering" but the existing form is shorter and adequate.
- `causal structure` — **sonnet-4-6-r2:** Foundational postulate about irreducible causal structure. The name is correct.

## 135. `composition closure closure defect $\varepsilon^\ast$`

**Alternatives proposed:** `composition closure closure defect`

_category: keep × 3_

- `composition closure closure defect` — **agent1-original-brainstorm:** "Closure" is load-bearing abstract-algebra term that reads naturally. "Defect" adds physical/engineering flavor. Framing nudge in Section III preamble would inoculate against CS-closure collision — no rename.
- `composition closure closure defect` — **opus-1m:** Keep. CS-closures collision is an inoculation issue (preamble note), not a rename issue.
- `composition closure closure defect` — **opus-4-7-b:** "Closure" as the algebraic term lands well here and the engineering-flavored "defect" reads cleanly as the gap. The one collision risk is CS closures (lexical scopes), but disambiguation by context is cheap. No rename.

## 136. `condition`

**Alternatives proposed:** `condition`

_category: keep × 3_

- `condition` — **haiku-4-5:** Defines where AAD applies. Short, descriptive. Specialist vocabulary (scope honesty is architectural principle). Acceptable. Keep.
- `condition` — **opus-4-7-b:** Keep. This is the Section I membership criterion — "where AAD applies." The slug is self-announcing and gets cited heavily across segments.
- `condition` — **sonnet-4-6:** The simplest possible name for what it is. Used throughout. Not eligible for improvement. Keep.

## 137. `constitutive utterance`

**Alternatives proposed:** `constitutive utterance`, `ontological speech act`, `utterance as intervention`, `irrevocable emission`, `irrevocable utterance`

_category: rename × 4, keep × 3_

- `constitutive utterance` — **opus-4-7-r2:** Defended keep — logozoetic. "Constitutive utterance" is iconic in the framework's logozoetic vocabulary; it captures the irreversibility-of-token-generation insight precisely.
- `constitutive utterance` — **opus-targeted-alternatives-v2:** Per `04-logozoetic-agents/OUTLINE.md`: "Token generation as an irreversible environmental intervention ($do(a)$) that alters the agent's future state-space." "Constitutive" is the right word (Austin's performatives in philosophy of language — the utterance constitutes new state; not just describes existing state). The pair "constitutive" + "utterance" is project-distinctive and earns memorable-noun status.
- `constitutive utterance` — **opus-targeted-alternatives:** Per `#form-constitutive-utterance` (logozoetic): token generation as $do(a)$-intervention that irreversibly alters the agent's future state-space. "Constitutive" carries the world-altering-by-saying sense (Austin's performatives in the philosophy-of-language tradition); "utterance" is precise about the act-type. The phrase is iconic in the framework's logozoetic vocabulary. Confirms across architectures.
- `ontological speech act` — **gemini-targeted-alternatives:** A clearer description of what makes it iconic in logozoetic vocabulary — the language literally alters being/structure.
- `utterance as intervention` — **opus-targeted-alternatives-v2:** Names the formal mechanism: token generation = $do(a)$-intervention per Pearl's causal hierarchy. "As-intervention" is clinical-formal; "constitutive" is philosophical-formal. Both are honest; pick by audience preference. The alternative makes the Pearl-causal-hierarchy connection visible in the slug.
- `irrevocable emission` — **opus-targeted-alternatives-v2:** Considered. "Irrevocable" + "emission" names the irreversibility-of-token-generation insight. Rejected (same as r1 vote): loses the *constitutive* sense — the utterance constitutes new state in the agent's world, not merely fixes it. "Emission" is too physical/passive.
- `irrevocable utterance` — **opus-targeted-alternatives:** Considered. Names the irreversibility correctly but loses the *constitutive* sense (the utterance *constitutes* something new in the agent's world, not merely fixes it). Rejected.

## 138. `correlation hierarchy l0 l1 l1 l2`

**Alternatives proposed:** `correlation hierarchy`, `correlation ladder`, `correlation hierarchy l0 l1 l1 l2`

_category: rename × 4, canonicalize × 1, keep × 1_

- `correlation hierarchy` — **opus-1m:** Keep unless #separability-ladder lands AND the parallelism between the three ladders (correlation / separability / continuation) is judged load-bearing. Conditional keep.
- `correlation hierarchy` — **opus-4-7-r2:** Already canonical in `#def-strategy-dag` and downstream segments; vote to confirm and protect against drift. The paired naming with "Convention Hierarchy" (C1/C2/C3) is part of the framework's tiering vocabulary — both should remain capitalized as named hierarchies.
- `correlation hierarchy` — **sonnet-4-6:** The three-level naming (Correlation / Convention / Contraction) is coherent and each element starts with C. The parallelism aids recall. Keep.
- `correlation ladder` — **agent1-original-brainstorm:** Parallelism with #separability-ladder proposal. Only worth doing if that rename lands.
- `correlation ladder` — **opus-4-7-b:** Pairs with the `#separability-ladder` rename if both are adopted. "Ladder" is the geometry (rungs of increasing difficulty: independence → strict prerequisite → soft facilitator → full joint). The "L0/L1/L1'/L2" abbreviations continue to work. Reduces the "hierarchy" overload in the project (currently: Pearl's causal hierarchy, convention, correlation, approximation-tiering-sometimes-called-hierarchy — four distinct uses).
- `correlation hierarchy l0 l1 l1 l2` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep)" — The four-level partition (independence / strict-prerequisites / soft-facilitators / full correlation) is "the kind of structural-completeness move I find satisfying." L1' refutation under unobservable common cause (Cramér-Rao floor) makes the partition load-bearing. Endorsed. [from 43-46-section-ii-and-or-strategy-dag-gaps.md]

## 139. `discussion`

**Alternatives proposed:** `discussion`

_category: keep × 3_

- `discussion` — **codex-2:** Boring on purpose; that is a virtue here.
- `discussion` — **opus-4-7-b:** Keep. Standard academic-register header; no rename needed.
- `discussion` — **opus-4-7:** Standard. Keep.

## 140. `edge update via gain`

**Alternatives proposed:** `edge update via gain`, `gain based edge update`

_category: keep × 5, rename × 1_

- `edge update via gain` — **haiku-4-5-r2:** The hypothesis name describes the proposed mechanism. Adequate.
- `edge update via gain` — **haiku-4-5:** Gain extends to strategy edges. Self-descriptive. Keep.
- `edge update via gain` — **opus-4-7-b:** Keep — the slug clearly frames this as "extend the gain principle from state to strategy edges," which is the segment's hypothesis.
- `edge update via gain` — **opus-4-7-r2:** Acceptable keep. Names the load-bearing hypothesis that gain extends to strategy edges.
- `edge update via gain` — **sonnet-4-6-r2:** "Edge update via gain" names the extension of gain principle to strategy edges. The "via gain" suffix makes the mechanism clear.
- `gain based edge update` — **gemini-3-1-pro-preview-r2:** Slightly better flow in prose.

## 141. `interiority default`

**Alternatives proposed:** `interiority default`

_category: keep × 4_

- `interiority default` — **codex-gpt-5-r2:** Good normative phrase. It is compact and distinguishes internal experience from external output.
- `interiority default` — **codex-gpt-5-r2:** Good normative slug.
- `interiority default` — **opus-4-7-r2:** Acceptable keep — logozoetic norm. "Interiority as default" is the substantive claim; the slug compresses correctly.
- `interiority default` — **sonnet-4-6-r2:** "Interiority default" names the normative claim about treating agents as having interiority by default. Distinctive.

## 142. `praxis`

**Alternatives proposed:** `praxis`, `praxis informed action`

_category: keep × 3, add-alias × 1_

- `praxis` — **codex-2:** Strongest of the five phase names after aporia; instantly sayable and philosophically apt.
- `praxis` — **codex-gpt-5-r2:** Familiar enough and exactly right for informed action. Keep.
- `praxis` — **opus-targeted-alternatives:** `LEXICON.md`: "Informed action: $a_t = \pi(M_t)$ (or $\pi(M_t, G_t)$ for actuated agents)." Praxis distinguishes itself from "action" by carrying the informed-by-the-cycle's-prior-stages sense — the action is the *outcome* of prolepsis-aisthesis-aporia-epistrophe, not a parallel branch. Keep.
- `praxis informed action` — **gemini-targeted-alternatives:** Links the philosophical term directly to the execution phase.

## 143. `prolepsis`

**Alternatives proposed:** `prolepsis`, `prolepsis anticipatory projection`, `anticipation`

_category: keep × 3, add-alias × 1, rename × 1_

- `prolepsis` — **codex-2:** Earns its foreignness because "anticipation" would flatten the active-modeling point.
- `prolepsis` — **codex-gpt-5-r2:** Good phase term for anticipation. Keep because the phase vocabulary works as a compact family.
- `prolepsis` — **opus-targeted-alternatives:** `LEXICON.md` defines it as "the model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$." The Greek term carries the active-modeling sense (πρόληψις = "taking-before") that "anticipation" or "prediction" both miss. Active modeling vs. passive forecasting is a distinction the segment formalism actually makes. Concur with codex's keep — but a non-codex architecture confirming the keep adds signal the original vote chain didn't capture.
- `prolepsis anticipatory projection` — **gemini-targeted-alternatives:** Adding English aliases assists non-specialists while retaining the precision of the Greek terms.
- `anticipation` — **opus-targeted-alternatives:** Considered and rejected. Loses the "active model produces an expectation that the world then refutes" dynamic that the cycle uses. "Anticipation" reads as passive forecast; the segment's formalism is generative. The Greek earns its foreignness here, exactly as codex argued.

## 144. `proprium mapping`

**Alternatives proposed:** `proprium mapping`

_category: keep × 3_

- `proprium mapping` — **codex-gpt-5-r2:** Specialized but useful. Keep if PROPRIUM remains a live source concept.
- `proprium mapping` — **opus-4-7-r2:** Defended keep — logozoetic. The PROPRIUM ontology is an established prior-work commitment; the mapping segment is correctly named for the move it makes.
- `proprium mapping` — **sonnet-4-6-r2:** "PROPRIUM mapping" adopts the Firmatum vocabulary directly. Per prior-art-integration principle, adopt with original name.

## 145. `structural adaptation`

**Alternatives proposed:** `structural adaptation`, `architectural adaptation`

_category: keep × 3, rename × 1_

- `structural adaptation` — **gemini-1:** Contrasts well with parametric adaptation. Keep.
- `structural adaptation` — **opus-4-7-b:** Keep. The distinction from *parametric adaptation* is load-bearing; "structural" is the right modifier.
- `structural adaptation` — **sonnet-4-6:** Clean compound. Distinguished from parametric update. Keep.
- `architectural adaptation` — **gemini-2:** "Structural" is heavily overloaded with "Structural persistence". "Architectural adaptation" separates changing the model class from persisting.

## 146. `substrate independence`

**Alternatives proposed:** `substrate independence`, `identity portability`

_category: keep × 3, rename × 1_

- `substrate independence` — **gemini-targeted-alternatives:** Central assumption of the framework.
- `substrate independence` — **opus-4-7-r2:** Acceptable keep — logozoetic. Names the result that identity survives substrate migration.
- `substrate independence` — **opus-targeted-alternatives-v2:** Per outline: "Identity survives substrate migration, proving identity is located in compressed history $M_t = \phi(\mathcal{C}_t)$, not neural weights." Names the *result* directly (independence from substrate) and pairs with `#der-the-scaffolding-tax`'s sovereignty argument. The two segments together make a coherent logozoetic argument; consistent vocabulary helps.
- `identity portability` — **opus-targeted-alternatives-v2:** Engineering register. Names the operational consequence (the agent's identity ports across substrates). Weaker because "portability" implies design-for-portability; the segment's claim is structural (identity *is* in $\phi(\mathcal{C}_t)$, full stop).

## 147. `temporal nesting`

**Alternatives proposed:** `temporal nesting`, `timescale nesting`, `timescale stratification`

_category: keep × 5, rename × 2_

- `temporal nesting` — **gemini-3-1-pro-preview-r2:** Evocative and accurate.
- `temporal nesting` — **haiku-4-5-r2:** Timescale terminology is standard in dynamical systems. Name is clear.
- `temporal nesting` — **haiku-4-5:** Timescale stratification. Self-descriptive. The concept (fast-epistrophe / slow-structural-adaptation / meta-learning timescales) is load-bearing but not yet crystallized into discourse vocabulary. Early to rename. Let prose vocabulary emerge organically as TST and logogenic sections develop. Keep.
- `temporal nesting` — **opus-4-7-r2:** Weak keep. "Temporal nesting" is fine but slightly generic — "timescale stratification" might be more accurate (nesting suggests strict containment; stratification is the layered-rates picture the segment derives). I considered the rename but the prose currency of "nesting" is enough that I lean keep.
- `temporal nesting` — **sonnet-4-6-r2:** "Temporal nesting" correctly names timescale stratification.
- `timescale nesting` — **opus-4-7-b:** "Temporal nesting" is accurate but slightly generic; "timescale nesting" names the specific nesting (slow/fast timescale separation) and avoids collision with TST's "temporal" (as in Temporal Software Theory). Weak preference.
- `timescale stratification` — **opus-4-7-r2:** Considered and rejected — too clinical and loses the spatial intuition of "nesting" that aids comprehension.

## 148. `value object`

**Alternatives proposed:** `value object`, `policy conditioned value`, `decision value`, `trajectory value`, `value functional`

_category: rename × 5, keep × 4_

- `value object` — **haiku-4-5-r2:** Technical term adopted from RL/game-theory; consistent prose usage. No change needed.
- `value object` — **haiku-4-5:** Compact name for a complex object (horizon- and policy-conditioned value functional). Reads naturally in prose. Keep. The "value-object" phrasing is specialized but load-bearing.
- `value object` — **opus-4-7-r2:** Weak keep. "Value object" reads as slightly generic, but it does work — the segment names a horizon-and-policy-conditioned value functional, distinct from utility, reward, or value-function. The C1/C2/C3 convention hierarchy lives inside it. I considered "continuation-conditioned value" but it's wordier without being clearly more precise.
- `value object` — **sonnet-4-6-r2:** "Value object" is somewhat engineering-flavored but distinct from "value function" (which has specific RL meaning). The horizon/policy-conditioned value IS an object in the mathematical sense. Keep with mild reservations about the register.
- `policy conditioned value` — **codex-1:** "Value object" is overloaded from software design and hides the continuation-convention dependence. The proposed name says what the quantity actually is.
- `decision value` — **codex-2:** "Value object" sounds implementation-ish; "decision value" says what the quantity is for in prose.
- `trajectory value` — **codex-gpt-5-r2:** Value object has software baggage and sounds like an implementation pattern. The segment defines horizon and policy conditioned trajectory value.
- `trajectory value` — **opus-4-7-r2:** Rebuttal — Codex proposed this at +2 with the rationale that "value object" sounds like an implementation pattern. I see the engineering-baggage concern but think "trajectory value" is worse: it elides the convention-conditioning that is the segment's central content. The C1/C2/C3 hierarchy lives in this segment precisely *because* the value depends on the convention chosen for continuation, not just on the trajectory. "Trajectory value" suggests something that can be computed from a trajectory alone, which is exactly what the segment shows is impossible without specifying convention. My keep+1 plus the more-careful "continuation-conditioned value" alternative I considered are stronger.
- `value functional` — **opus-4-7-r2:** Considered and rejected — "value functional" is also accurate but would collide with `form-objective-functional` (which is the upstream functional-form definition the value object inherits from). The current names disambiguate cleanly: objective is the functional, value is the object the functional produces under a continuation convention.

## 149. `variational sector condition`

**Alternatives proposed:** `variational sector condition`

_category: keep × 4_

- `variational sector condition` — **gemini-3-1-pro-preview-r2:** Distinct from discrete/continuous.
- `variational sector condition` — **haiku-4-5:** ε-fidelity B1 under variational approximation. Name is compound but accurate (sector condition under variational constraints). Keep.
- `variational sector condition` — **opus-4-7-b:** Keep.
- `variational sector condition` — **sonnet-4-6:** The compound noun names the mechanism (variational) and what it extends (sector condition). Parallel structure with #sector-condition-stability. Keep.

## 150. `$U_M$ as epistemic unity`

**Alternatives proposed:** `$\Upsilon_M$`, `$U_{\mathcal M}$`

_category: rename × 2, canonicalize × 1_

- `$\Upsilon_M$` — **codex-gpt-5-r2:** Canonicalize $\Upsilon_M$ for epistemic unity (instead of dual-use $U_M$). The two quantities differ in domain and meaning. [original row: dual-use vote split for atomicity.]
- `$\Upsilon_M$` — **opus-4-7-b:** Alternative disambiguation: rename *unity* symbols to $\Upsilon_M / \Upsilon_O / \Upsilon_\Sigma$ (capital upsilon, visually distinct from capital U; Greek letters are already the AAD unity convention-analog). Most important notation-layer issue in the sweep. [original row: dual-use vote split for atomicity; this is the second of two proposed disambiguations.]
- `$U_{\mathcal M}$` — **opus-4-7-b:** Genuine collision — same symbol, two different quantities, disambiguated only by domain. Use $U_{\mathcal M}$ with calligraphic subscript for the *unity* meaning to disambiguate from $U_M$ (model uncertainty). [original row: dual-use vote split for atomicity; this is one of two proposed disambiguations.]

## 151. `$U_M$ as model uncertainty`

**Alternatives proposed:** `$U_M$`

_category: canonicalize × 1, keep × 1_

- `$U_M$` — **codex-gpt-5-r2:** Canonicalize $U_M$ for model uncertainty. Genuine notation collision surfaced by other agents; relying on context for the dual-use is too fragile. [original row: dual-use vote split for atomicity.]
- `$U_M$` — **opus-4-7-b:** Genuine collision with epistemic unity — same symbol, two quantities. Keep $U_M$ for model uncertainty (the original/dominant use); the rename move is for the *unity* meaning, not this one. [original row: dual-use vote split for atomicity.]

## 152. `$U_O$ teleological unity`

**Alternatives proposed:** `teleological unity`

_category: add-alias × 2_

- `teleological unity` — **opus-4-7:** Clearly distinguishes from $U_o$ by subscript letter-case and by semantic content. Awkward because $U_o$ / $U_O$ are near-homographs in some fonts — see next row.
- `teleological unity` — **sonnet-4-6:** NOTATION.md already defines this. Used in prose already. Keep.

## 153. `$\eta^\ast$`

**Alternatives proposed:** `update gain`, `learning rate`

_category: add-alias × 3_

- `update gain` — **gemini-3-1-pro-preview-r2:** Solidifies the prose form of the optimal gain.
- `update gain` — **opus-targeted-alternatives-v2:** Per NOTATION and LEXICON. Confirms Gemini r1 +3 single-vote. The English alias is already in widespread use.
- `learning rate` — **opus-targeted-alternatives-v2:** Considered. ML-standard term. Rejected: the segment-derivation in `#emp-update-gain` shows $\eta^\ast = U_M / (U_M + U_o)$ — a Bayesian uncertainty ratio, not a stochastic-gradient-descent step size. The collision with ML's "learning rate" creates false familiarity.

## 154. `AAD acronym`

**Alternatives proposed:** `AAD`

_category: keep × 2_

- `AAD` — **gemini-targeted-alternatives:** Core framework acronym.
- `AAD` — **opus-4-7-r2:** Defended keep. Adaptation and Actuation Dynamics — survives the acronym discipline check (used 100+ times, no AI-Consciousness-Test collision after the 2026-04 rename, communal-imagination test passes once the expansion is known).

## 155. `action selection`

**Alternatives proposed:** `action selection`

_category: keep × 5_

- `action selection` — **gemini-3-1-pro-preview-r2:** Standard.
- `action selection` — **haiku-4-5-r2:** Clear derived claim; the name is accurate.
- `action selection` — **haiku-4-5:** Action as function of model. Self-descriptive. Keep.
- `action selection` — **opus-4-7-r2:** Weak keep. Slightly generic but accurate; the segment does derive that the action is a function of the model.
- `action selection` — **sonnet-4-6-r2:** Standard terminology. Nothing distinctive to rename to; accurate as-is.

## 156. `adaptive gain dynamic`

**Alternatives proposed:** `adaptive gain dynamic`

_category: keep × 4_

- `adaptive gain dynamic` — **gemini-3-1-pro-preview-r2:** Accurate.
- `adaptive gain dynamic` — **haiku-4-5:** A2' under adaptive gain: meta-gain conditions (MG-1)–(MG-4). Compound but functional. Keep.
- `adaptive gain dynamic` — **opus-4-7-b:** Keep. Direct; parallel to `#consolidation-dynamics`.
- `adaptive gain dynamic` — **sonnet-4-6:** "Adaptive gain" is the defining variable (gain $K$ as a state variable). "Dynamics" correctly names the content (sector condition under evolving gain). Keep.

## 157. `additive coordinate forcing family`

**Alternatives proposed:** `forced coordinate family`, `coordinate constraint pattern`, `additive structure derivation`

_category: rename × 3, canonicalize × 1_

- `forced coordinate family` — **codex-gpt-5-r2:** Use forced coordinates as the family phrase across Cauchy, Fisher, IB, and Legendre instances.
- `forced coordinate family` — **opus-targeted-alternatives-v2:** Per `disc-additive-coordinate-forcing`: the four-instance pattern (Cauchy-FE log-confidence, Čencov-Fisher metric, Shore-Johnson IB, Aczél-Hobson-Legendre). "Forced coordinates" covers Čencov-Fisher (4th instance is *not* additive) where "additive" overspecifies. Codex r1 +3 single-vote; multi-arch sweep in r1 (Sonnet +2 confirming, Opus -1 on cauchy-coordinates). Consensus-aligned.
- `coordinate constraint pattern` — **gemini-targeted-alternatives:** Emphasizes the formal constraint mechanism rather than "forcing".
- `additive structure derivation` — **gemini-targeted-alternatives:** Explicitly names the formal move being made.

## 158. `agent identity as one non forkable causal record`

**Alternatives proposed:** `singular trajectory commitment`, `trajectory bound identity`

_category: canonicalize × 2, rename × 1_

- `singular trajectory commitment` — **codex-gpt-5-r2:** Excellent prose handle for the token-level scope of AAD.
- `singular trajectory commitment` — **gemini-targeted-alternatives:** Perfectly describes the axiom that identity equals a single, non-forkable causal path.
- `trajectory bound identity` — **gemini-targeted-alternatives:** Shorter, very usable alias for the same concept.

## 159. `agent opacity $H_b^{A|B}$`

**Alternatives proposed:** `agent opacity`

_category: keep × 2_

- `agent opacity` — **agent1-original-brainstorm:** "Opacity" carries exactly the right intuition (dual of observability). Hafez's $H_b$ gets an AAD-native name that connects to Section III's info-loss framing cleanly.
- `agent opacity` — **opus-1m:** Adopted $H_b$ from Hafez 2026 with AAD-native framing. Works.

## 160. `aporia ἀπορία`

**Alternatives proposed:** `aporia`, `aporia ἀπορία`

_category: rename × 2, canonicalize × 1_

- `aporia` — **gemini-1:** "Productive perplexity" is a crucial nuance that "prediction error" misses.
- `aporia` — **sonnet-4-6:** Particularly apt: the productive perplexity that drives the adaptive cycle. Keep.
- `aporia ἀπορία` — **haiku-4-5-r2:** Definition exists; prose uses "mismatch signal" and "prediction error." Commit to: "Aporia (productive perplexity)" as the canonical pairing to preserve the Greek sense.

## 161. `blind pursuer`

**Alternatives proposed:** `blind pursuer`, `model degenerate pursuer`, `reality blind agent`, `model poor pursuer`

_category: keep × 3, rename × 3_

- `blind pursuer` — **codex-1:** Borderline stylized, but memorable and semantically right for goal pursuit without a real world model.
- `blind pursuer` — **codex-gpt-5-r2:** Memorable and precise for objective-rich, model-poor systems.
- `blind pursuer` — **opus-targeted-alternatives:** Per `#def-agent-spectrum`: low-$M_t$, high-$O_t$ region — pursues a goal without an adequate world model (PID controller, reflex agent with setpoint). "Blind pursuer" pairs with "adaptive tracker" as a 2×2 corner; both are diagnostic-quality names. Keep.
- `model degenerate pursuer` — **gemini-targeted-alternatives:** The text clarifies $M_t$ is absent or degenerate. "Model-degenerate" is more formal than "blind".
- `reality blind agent` — **gemini-targeted-alternatives:** Directly contrasts with reality tracking, but maybe too stylized.
- `model poor pursuer` — **opus-targeted-alternatives:** Weak alternative. More technically precise (specifies *which* axis is degenerate) but loses the imagistic punch of "blind." Marginal.

## 162. `causal discovery from git`

**Alternatives proposed:** `causal discovery from git`, `git causal discovery`

_category: keep × 4, rename × 1_

- `causal discovery from git` — **codex-1:** Slightly long, but concrete and honest. This is exactly the sort of hypothesis title that should not be made more clever.
- `causal discovery from git` — **codex-2:** Blunt and searchable is the right trade here.
- `causal discovery from git` — **opus-4-7-r2:** Acceptable keep — TST hypothesis. "Git as interventional data" is the substantive claim; the slug compresses cleanly.
- `causal discovery from git` — **sonnet-4-6-r2:** "Causal discovery from git" is precise — git as interventional data enabling causal discovery.
- `git causal discovery` — **codex-gpt-5-r2:** Subject-noun-first and shorter.

## 163. `change expectation baseline`

**Alternatives proposed:** `change expectation baseline`, `change baseline`, `lindy baseline`

_category: keep × 4, rename × 2_

- `change expectation baseline` — **codex-1:** Exact, memorable, and appropriately conservative. This is one of TST's cleaner names.
- `change expectation baseline` — **codex-2:** Clinical, but the Bayesian-accountability function matters more than extra flair.
- `change expectation baseline` — **sonnet-4-6-r2:** "Change expectation baseline" (median future ≈ observed past). Accurate.
- `change expectation baseline` — **sonnet-4-6:** The segment covers Lindy-effect reasoning and investment scale forms. The name is accurate but the "baseline" suffix is vague.
- `change baseline` — **codex-gpt-5-r2:** The shorter form is cleaner, but expectation-baseline is still defensible.
- `lindy baseline` — **sonnet-4-6:** Would surface the Lindy connection explicitly. But Lindy is a specific model (Taleb's rendering); the segment is more general. The current name is more honest.

## 164. `change investment`

**Alternatives proposed:** `change investment`, `change amortization`

_category: keep × 3, rename × 1_

- `change investment` — **codex-gpt-5-r2:** Good temporal-cost phrase for when future expected change justifies present work.
- `change investment` — **opus-targeted-alternatives:** TST segment names the temporal-cost analysis where a more expensive present change is justified by reduced future cost (Lindy-baseline future-change expectation). "Investment" carries the prospect-of-future-return sense correctly. Keep.
- `change investment` — **sonnet-4-6-r2:** "Change investment" names the when-extra-time-pays-off analysis. Appropriate.
- `change amortization` — **opus-targeted-alternatives:** Accounting-flavored alternative. Loses the choice-under-uncertainty sense that "investment" carries (amortization is mechanical). Rejected.

## 165. `chronica 𝒞 t`

**Alternatives proposed:** `chronica`

_category: canonicalize × 1, rename × 1_

- `chronica` — **gemini-targeted-alternatives:** Connecting prose and symbol.
- `chronica` — **haiku-4-5:** Greek-rooted term ("records of time") for the complete interaction history. Self-descriptive once learned; memorable. Lowercase notation 𝒞_t is appropriate. Keep.

## 166. `claude md what settled vs open`

**Alternatives proposed:** `claude md what settled vs open`

_category: keep × 2_

- `claude md what settled vs open` — **opus-4-7-b:** Keep. The section structure (Settled / Open / Known Fragilities) is load-bearing — renaming would leave readers uncertain whether "Settled" means "derived" or "under current working consensus" and the section's very content clarifies this.
- `claude md what settled vs open` — **opus-4-7:** The honest binary is the right framing; don't soften to "Current State" or similar. Keep.

## 167. `closure defect`

**Alternatives proposed:** `closure defect`, `compositional closure defect`, `homomorphism residual`, `closure error`

_category: rename × 3, keep × 2_

- `closure defect` — **codex-gpt-5-r2:** Excellent quantity name for epsilon-star. It is short and memorable.
- `closure defect` — **opus-targeted-alternatives:** Per `#form-composition-closure`: $\varepsilon^\ast$ is the minimum-achievable approximation error of the macro-description against the micro-system. "Defect" carries the precise sense (a residual that cannot be eliminated, only minimized over admissible classes) and "closure" names the homomorphism property being approximated. Mathematically apt, evocative, short. Confirms across architectures.
- `compositional closure defect` — **gemini-targeted-alternatives:** Highlights that the defect is specific to the composition-layer math.
- `homomorphism residual` — **opus-targeted-alternatives:** Technically more transparent (the criterion *is* approximate dynamical homomorphism), but four syllables longer and loses the diagnostic quality — "defect" implies *something specific is wrong*; "residual" is statistical neutrality. Rejected.
- `closure error` — **opus-targeted-alternatives:** Plainer English. Rejected: "error" is overloaded in the segment's neighborhood (mismatch error, trajectory error, bias error, all distinct quantities). "Defect" does the disambiguation work.

## 168. `concept the architectural requirement that composite agent admissibility inherit from sub agent property plus topology`

**Alternatives proposed:** `heredity commitment`, `composition heredity axiom`

_category: name-unnamed × 2, canonicalize × 1_

- `heredity commitment` — **codex-1:** Strong name from the jacobian-strengthening spike: short, memorable, and explicit about the architectural bet being made. [original phrasing: unnamed: stronger composition-consistency demand that composite admissibility inherit from sub-agent properties plus topology]
- `heredity commitment` — **codex-gpt-5-r2:** Good name for the stronger expectation that composite admissibility should inherit from sub-agent properties plus topology. [original phrasing: composition consistency inheritance across scales]
- `composition heredity axiom` — **gemini-targeted-alternatives:** Names the strict requirement that composite properties must be derivable from constituents. [original phrasing: unnamed stronger composition consistency demand that composite admissibility inherit from sub agent properties plus topology]

## 169. `concept the asymmetric pair of memory access mode one biased by current goal the other state keyed only`

**Alternatives proposed:** `goal conditioned reconstruction`, `goal-blind retrieval`, `state keyed retrieval`, `goal biased retrieval`

_category: name-unnamed × 4, rename × 2, canonicalize × 1_

- `goal conditioned reconstruction` — **codex-gpt-5-r2:** Important Class-2 failure mode: retrieval can be contaminated by the current objective rather than reconstructing the chronica neutrally. [original phrasing: goal-biased retrieval from persistent memory]
- `goal conditioned reconstruction` — **gemini-3-1-pro-preview-r2:** A critical vulnerability where memory retrieval is corrupted by Class 2 coupling. [original phrasing: unnamed: RAG queries biased by the current goal acting as an echo chamber]
- `goal-blind retrieval` — **codex-gpt-5-r2:** Strong architectural counterpart to goal-blind routing. This is the memory-side directed-separation repair. [original phrasing: retrieval keyed by state rather than current objective]
- `goal-blind retrieval` — **gemini-3-1-pro-preview-r2:** The necessary architectural fix to preserve objective CHRONICA. [original phrasing: unnamed: retrieving context based only on state, not goal]
- `state keyed retrieval` — **gemini-targeted-alternatives:** Contrasts explicitly with objective-keyed / goal-biased retrieval. [original phrasing: retrieval keyed by state rather than current objective]
- `state keyed retrieval` — **gemini-targeted-alternatives:** Standardizes the goal-blind routing requirement. [original phrasing: unnamed retrieving context based only on state not goal]
- `goal biased retrieval` — **gemini-targeted-alternatives:** Matches the architectural term for this feedback failure. [original phrasing: unnamed RLHF5 queries biased by the current goal acting as an echo chamber]

## 170. `concept the deliberate expenditure of tempo budget to convert hidden strategy node into one that yield update eligible feedback`

**Alternatives proposed:** `observability investment`

_category: name-unnamed × 2_

- `observability investment` — **codex-gpt-5-r2:** Important strategic repair for evidence starvation and credit-assignment collapse. [original phrasing: deliberate expenditure to make hidden nodes observable]
- `observability investment` — **gemini-3-1-pro-preview-r2:** The only way to rescue an agent or organization from evidence starvation. [original phrasing: unnamed: deliberate expenditure of tempo to convert a hidden node into an observable one]

## 171. `concept the effective tempo loss when observation channel are correlated rather than independent both the quantitative loss and the prose level overconfidence error it explain`

**Alternatives proposed:** `redundancy penalty`, `redundancy illusion`

_category: name-unnamed × 3_

- `redundancy penalty` — **codex-gpt-5-r2:** More neutral and technical than my earlier redundancy illusion. Use illusion for the cognitive error, penalty for the quantity. [original phrasing: correlated-channel overcount]
- `redundancy penalty` — **gemini-3-1-pro-preview-r2:** Formalizes the danger of organizational echo chambers. [original phrasing: unnamed: the reduction in effective tempo when observation channels are correlated]
- `redundancy illusion` — **codex-gpt-5-r2:** Good name for overcounting correlated channels as independent tempo. [original phrasing: correlated evidence overconfidence]

## 172. `concept the externalization and rehydration mechanism for carrying part of m t or g t across session boundary via the environment`

**Alternatives proposed:** `artificial hippocampus`, `externalization reconstruction cycle`, `reconstruction relay`, `model inscription`, `memory relay`, `externalized state`, `stigmergic externalization`, `reconstruction loop`, `class 2 state reconstruction`, `intent reconstruction`

_category: name-unnamed × 7, canonicalize × 6, add-alias × 1, rename × 1_

- `artificial hippocampus` — **gemini-3-1-pro-preview-r2:** The exact role an agent framework plays in compressing and injecting the chronica. [original phrasing: unnamed: managing memory across session boundaries to prevent the Sufficiency Discontinuity]
- `artificial hippocampus` — **gemini-targeted-alternatives:** Specifically maps to the biological analog of cross-episode memory consolidation referenced in AAD. [original phrasing: managing memory across session boundaries to prevent the sufficiency discontinuity]
- `externalization reconstruction cycle` — **gemini-targeted-alternatives:** Names the core operational loop preserving state for logogenic agents. [original phrasing: externalization reconstruction across sessions]
- `externalization reconstruction cycle` — **gemini-targeted-alternatives:** Elevates the logogenic continuity loop to a proper noun. [original phrasing: unnamed the externalization reconstruction cycle across sessions]
- `reconstruction relay` — **gemini-targeted-alternatives:** Highlights the relay race nature of state across session boundaries. [original phrasing: managing memory across session boundaries to prevent the sufficiency discontinuity]
- `reconstruction relay` — **gemini-targeted-alternatives:** Standardizes the term for bridging context turnover. [original phrasing: unnamed managing memory across session boundaries to prevent the sufficiency discontinuity]
- `model inscription` — **codex-2:** Distinctive and accurate; it captures writing the model into the world, not just "documentation." [original phrasing: unnamed: externalizing part of $M_t$ into the environment for future agents]
- `model inscription` — **codex-gpt-5-r2:** Useful TST and logogenic phrase for externalized knowledge that later agents can read back. [original phrasing: model state written into the environment]
- `memory relay` — **codex-2:** Short, sayable noun for a repeated logogenic mechanism. [original phrasing: unnamed: the externalization-reconstruction cycle across sessions]
- `memory relay` — **codex-gpt-5-r2:** Sharper than reconstruction loop when the mechanism is one agent leaving state for a later session to recover. [original phrasing: externalization-reconstruction across sessions]
- `externalized state` — **gemini-targeted-alternatives:** Elevates the core mechanism of logogenic continuity. [original phrasing: model state written into the environment]
- `stigmergic externalization` — **gemini-targeted-alternatives:** Adopts the biological term (stigmergy) for leaving state in the environment. [original phrasing: unnamed externalizing part of $M_t$ into the environment for future agents]
- `reconstruction loop` — **codex-gpt-5-r2:** Useful logogenic term for external memory restoring working state after turnover. [original phrasing: persistent storage reconstruction of Class-2 state]
- `class 2 state reconstruction` — **gemini-targeted-alternatives:** Formally names the specific recovery operation. [original phrasing: persistent storage reconstruction of class 2 state]
- `intent reconstruction` — **opus-4-7-r2:** New alternative — Sonnet named "inter-session reconstruction" for the M_t side. The Σ_t side has a parallel: the agent must reconstruct its objective and strategy state from prompt + persistent storage at session start. Currently this happens informally in agentic systems; naming it as "intent reconstruction" (analog to "context reconstruction") gives logogenic-agents segments a handle for analyzing how the reconstruction can fail. Pairs with my "strategic turnover" entry. [original phrasing: unnamed: a Class-2 agent's process of reconstructing its purposeful substate at session start]

## 173. `concept the fact that what count as predictively relevant model content depend on which strategy the agent is going to run`

**Alternatives proposed:** `policy relative epistemology`

_category: name-unnamed × 2_

- `policy relative epistemology` — **codex-gpt-5-r2:** Strong name for the IB and sufficiency caveat that what counts as predictive depends on action policy. [original phrasing: predictive relevance depending on the policy the agent will run]
- `policy relative epistemology` — **gemini-3-1-pro-preview-r2:** Breaks the ideal of directed separation by linking memory to strategy. [original phrasing: unnamed: the dependence of optimal epistemic compression on the agent's planned actions]

## 174. `concept the formal pairing between how clearly an agent observe its environment and how predictable that agent appear to outside observer`

**Alternatives proposed:** `legibility opacity duality`

_category: name-unnamed × 2_

- `legibility opacity duality` — **codex-gpt-5-r2:** Good name for the formal dual between how well an agent sees the world and how well observers can predict the agent. [original phrasing: observability and opacity pair]
- `legibility opacity duality` — **gemini-3-1-pro-preview-r2:** Formalizes the thermodynamic tension of corporate secrecy and evolutionary arms races. [original phrasing: unnamed: the formal duality between observation quality and agent opacity]

## 175. `concept the minimum sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover`

**Alternatives proposed:** `reconstruction adequacy threshold`, `reconstruction adequacy condition`, `reconstruction threshold`, `reentry threshold`

_category: canonicalize × 4, name-unnamed × 3, rename × 1_

- `reconstruction adequacy threshold` — **gemini-targeted-alternatives:** Formally identifies the inter-session survival boundary. [original phrasing: minimum sufficiency after a session rebuild]
- `reconstruction adequacy threshold` — **gemini-targeted-alternatives:** Standardizes this inter-session persistence boundary. [original phrasing: unnamed minimum sufficiency required after a session rebuild]
- `reconstruction adequacy condition` — **gemini-targeted-alternatives:** Standardizes the inter-session survival boundary. [original phrasing: unnamed the logogenic analog to the persistence condition for session reconstruction]
- `reconstruction adequacy condition` — **gemini-targeted-alternatives:** Locks in the boundary test for logogenic persistence. [original phrasing: unnamed the reconstruction adequacy condition for logogenic agents]
- `reconstruction threshold` — **gemini-3-1-pro-preview-r2:** Elevating Sonnet's observation to canonical status; exactly names $S \geq S_{\text{min}}$. [original phrasing: unnamed: the logogenic analog to the persistence condition for session reconstruction]
- `reconstruction threshold` — **sonnet-4-6-r2:** `obs-context-turnover` derives a condition $S(f_{\text{init}}(\ldots)) \geq S_{\text{min}}$ parallel to the persistence condition but for session reconstruction rather than continuous dynamics. The document discusses it without naming it. "Reconstruction threshold" parallels "persistence condition" and makes the logogenic-agent analog explicit in prose. [original phrasing: unnamed: the reconstruction adequacy condition for logogenic agents]
- `reentry threshold` — **codex-1:** This concept recurs across context-turnover and model-preservation. It deserves a short noun phrase instead of repeated paraphrase. [original phrasing: unnamed: minimum sufficiency required after a session rebuild]
- `reentry threshold` — **codex-gpt-5-r2:** Useful logogenic quantity: how much reconstructed state is needed before the agent can act competently again. [original phrasing: minimum sufficiency after a session rebuild]

## 176. `concept the per reader compounding comprehension cost in code distinguished from per feature implementation cost scaling with reader cycling rate`

**Alternatives proposed:** `turnover multiplier`, `the turnover tax`

_category: name-unnamed × 3_

- `turnover multiplier` — **gemini-1:** "Turnover multiplier" perfectly captures the compounding scaling of comprehension cost under context turnover. [original phrasing: unnamed: the per-reader compounding cost of understanding code]
- `turnover multiplier` — **gemini-3-1-pro-preview-r2:** The parameter $k$ that mathematically mandates explicit code in high-turnover environments. [original phrasing: unnamed: the separation of per-reader comprehension cost from per-feature implementation cost]
- `the turnover tax` — **gemini-3-1-pro-preview-r2:** Why clean code is thermodynamically forced by 100% context turnover. [original phrasing: unnamed: the separation of per-reader and per-feature code costs]

## 177. `concept the property of model adequacy when measured against a single agent own causal record rather than against a population average`

**Alternatives proposed:** `trajectory indexed sufficiency`

_category: name-unnamed × 2_

- `trajectory indexed sufficiency` — **codex-gpt-5-r2:** Important consequence of singular chronica and agent identity. This deserves a stable name. [original phrasing: model sufficiency relative to an agent's own chronica]
- `trajectory indexed sufficiency` — **gemini-3-1-pro-preview-r2:** Separates identical agents with different futures, answering "is this the same agent?". [original phrasing: unnamed: sufficiency as a property of the model relative to its specific history]

## 178. `concept the prose form of κ cross the coupling between an agent model of self and its model of other`

**Alternatives proposed:** `cross model coupling`, `cross agent strategic coupling`

_category: name-unnamed × 2, rename × 1_

- `cross model coupling` — **codex-1:** Clean English complement to kappa_processing. This gives the opacity and theory-of-mind work a reusable noun slot. [original phrasing: unnamed: coupling between an agent's model-of-self and model-of-other, the prose form of kappa_cross]
- `cross model coupling` — **codex-gpt-5-r2:** Strong English complement to kappa-style coupling terms in opacity and theory-of-mind discussions. [original phrasing: cross-agent model-of-self and model-of-other coupling]
- `cross agent strategic coupling` — **gemini-targeted-alternatives:** Names the specific game-theoretic linkage that creates Class 3 composites. [original phrasing: unnamed coupling between an agent s model of self and model of other the prose form of kappa cross]

## 179. `control regret $\delta_{\text{regret}}$`

**Alternatives proposed:** `control regret`

_category: keep × 2_

- `control regret` — **gemini-2:** Perfect partner to satisfaction gap. Keep.
- `control regret` — **gemini-targeted-alternatives:** Core diagnostic.

## 180. `derivation not proof`

**Alternatives proposed:** `derivation`

_category: keep × 1, rename × 1_

- `derivation` — **gemini-targeted-alternatives:** Important epistemic distinction for AAD claims.
- `derivation` — **opus-4-7-b:** Keep. Same argument.

## 181. `developer agent`

**Alternatives proposed:** `developer agent`

_category: keep × 3_

- `developer agent` — **codex-gpt-5-r2:** Clear TST actor name.
- `developer agent` — **opus-4-7-r2:** Acceptable keep — the segment defines the developer-as-agent mapping, slug-form is correct.
- `developer agent` — **sonnet-4-6-r2:** "Developer agent" names the AAD-agent model of the developer. Accurate and distinctive.

## 182. `directional fidelity condition b1`

**Alternatives proposed:** `directional fidelity`

_category: keep × 1, rename × 1_

- `directional fidelity` — **gemini-targeted-alternatives:** Perfectly captures the accuracy commitment (correction points toward reality).
- `directional fidelity` — **sonnet-4-6:** The name earns its place — "fidelity" captures the accuracy commitment (the correction points approximately toward reality) and "directional" qualifies it (it's about direction, not magnitude). Used in #gain-sector-bridge and carried forward into the sector sub-scope partition. Keep.

## 183. `discussion segment section`

**Alternatives proposed:** `discussion`

_category: canonicalize × 2_

- `discussion` — **gemini-targeted-alternatives:** Standard markdown section.
- `discussion` — **opus-4-7-r2:** Defended canonicalization. Same as above.

## 184. `discussion segment section header`

**Alternatives proposed:** `discussion`

_category: rename × 2_

- `discussion` — **haiku-4-5:** Established in FORMAT.md. Keep.
- `discussion` — **sonnet-4-6:** Generic but correct. Alternatives ("Interpretation," "Context," "Connections") are all worse or no better. Keep.

## 185. `edge credence $p_{ij}$`

**Alternatives proposed:** `edge credence`

_category: keep × 1, canonicalize × 1_

- `edge credence` — **gemini-targeted-alternatives:** Replaces the broader "probability" with proper Bayesian vocabulary for subjective belief.
- `edge credence` — **sonnet-4-6:** "Credence" is the correct Bayesian vocabulary for subjective probability. LEXICON.md lists this under "Terms to Be Added." Should be promoted to main LEXICON. Keep.

## 186. `epistemic status segment section`

**Alternatives proposed:** `epistemic status`

_category: canonicalize × 2_

- `epistemic status` — **gemini-targeted-alternatives:** Standard markdown section.
- `epistemic status` — **opus-4-7-r2:** Defended canonicalization — same.

## 187. `epistemic status segment section header`

**Alternatives proposed:** `epistemic status`

_category: rename × 2_

- `epistemic status` — **haiku-4-5:** Established in FORMAT.md as public API for outline-filtering. Load-bearing naming. Keep.
- `epistemic status` — **sonnet-4-6:** Arguably the most distinctive feature of the segment format. "Epistemic Status" is a precise term for what the section does (tells you how much to trust the claim and why). Keep.

## 188. `epistemic substate purposeful substate`

**Alternatives proposed:** `epistemic substate purposeful substate`

_category: keep × 1, canonicalize × 1_

- `epistemic substate purposeful substate` — **gemini-targeted-alternatives:** [prose moved from candidate column]: "`keep canonical pairing`" — The exact pairing is load-bearing in Directed Separation discussions ($M_t$ vs $G_t$).
- `epistemic substate purposeful substate` — **opus-4-7-r2:** Defended canonicalization. The pairing $M_t$ (epistemic substate) / $G_t$ (purposeful substate) is iconic; do not paraphrase as "belief state" / "goal state" or "model" / "purpose" (which collide with other usages).

## 189. `epistrophe`

**Alternatives proposed:** `epistrophe`, `epistrophe model update`, `turn`

_category: keep × 4, add-alias × 1, rename × 1_

- `epistrophe` — **codex-1:** Slightly harder on first contact than "update," but it preserves the turning-toward distinction the theory actually uses.
- `epistrophe` — **codex-2:** More effortful than "update," but it does real conceptual work around reorientation rather than mere parameter change.
- `epistrophe` — **codex-gpt-5-r2:** Good phase term for turning-toward correction. Slightly less self-explanatory than aporia, but strong in the cycle family.
- `epistrophe` — **opus-targeted-alternatives:** `LEXICON.md`: "Turning toward reality: gain-weighted update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$." Crucially, ἐπιστροφή names a *turning toward* (not "applying an update," not "correcting"). The term marks that the agent is reorienting *itself* toward reality, not externally adjusting parameters. This is the conceptual heart of why TFT/AAD's update is not just gradient descent.
- `epistrophe model update` — **gemini-targeted-alternatives:** Grounds the turning-toward-reality in the formal update step.
- `turn` — **opus-targeted-alternatives:** The plain-English equivalent, and it does carry the right valence ("turn toward"), but it is too generic and collides with too many other senses (turn = take a turn, turn = rotation). Rejected.

## 190. `evidence starvation canonicalize`

**Alternatives proposed:** `evidence starvation`, `reaffirm 3 with collective confirmation`

_category: canonicalize × 3_

- `evidence starvation` — **gemini-targeted-alternatives:** Solidifies the primary term.
- `evidence starvation` — **opus-targeted-alternatives-v2:** Confirms r1 triple-architecture vote. See above.
- `reaffirm 3 with collective confirmation` — **sonnet-4-6-r2:** Both Codex (+3) and Gemini (+3) independently proposed this canonicalization with overlapping reasoning. My cold-start had proposed it (+3). Triple convergence with independent reasoning confirms this is one of the clearest missing-canonical-term slots in the corpus. No new content, but the triple-convergence is itself a data point worth recording.

## 191. `explicit strategy condition`

**Alternatives proposed:** `explicit strategy condition`, `strategy explicitness`, `deliberation advantage condition`, `planning scope`

_category: keep × 4, rename × 3_

- `explicit strategy condition` — **codex-gpt-5-r2:** Clear normative design criterion.
- `explicit strategy condition` — **haiku-4-5:** When planning beats exploring. Conditional; reasonably named. Keep.
- `explicit strategy condition` — **opus-4-7-r2:** Acceptable keep — names a normative threshold (when planning beats exploring). The "condition" suffix here is doing work because the segment names a specific named condition, not a generic role.
- `explicit strategy condition` — **sonnet-4-6-r2:** "Explicit strategy condition" is the normative condition for when planning beats exploring. Acceptable.
- `strategy explicitness` — **gemini-3-1-pro-preview-r2:** Noun phrase instead of condition.
- `deliberation advantage condition` — **gemini-2:** "When planning beats exploring" is about the advantage of deliberation.
- `planning scope` — **opus-4-7:** The segment is a normative scope condition for "when planning beats exploring." Current name reads as condition-on-the-strategy, not condition-for-strategy-to-apply. Minor clarity win.

## 192. `fluid limit ga 5`

**Alternatives proposed:** `fluid limit`

_category: keep × 1, rename × 1_

- `fluid limit` — **gemini-targeted-alternatives:** Standard, recognizable terminology from stochastic processes.
- `fluid limit` — **sonnet-4-6:** Standard terminology from stochastic processes. Keep.

## 193. `formal expression segment section`

**Alternatives proposed:** `formal expression`

_category: canonicalize × 2_

- `formal expression` — **gemini-targeted-alternatives:** Standard markdown section.
- `formal expression` — **opus-4-7-r2:** Defended canonicalization. The cadence (frontmatter / title / summary / Formal Expression / Epistemic Status / Discussion / Findings / Working Notes) is a public-API contract; renaming would cascade.

## 194. `formal expression segment section header`

**Alternatives proposed:** `formal expression`

_category: rename × 2_

- `formal expression` — **haiku-4-5:** Established in FORMAT.md. Keep.
- `formal expression` — **sonnet-4-6:** "Formal" distinguishes from Discussion; "Expression" is broader than "Proof" or "Derivation" (which would over-claim). The header is doing real work — it tells the reader this is where the math lives. Keep.

## 195. `fresh noise ga 1`

**Alternatives proposed:** `fresh noise`

_category: keep × 1, rename × 1_

- `fresh noise` — **gemini-targeted-alternatives:** Memorable informal name for the independence assumption on ε_t.
- `fresh noise` — **sonnet-4-6:** The informal name "Fresh noise" for the independence assumption on ε_t is perfectly memorable. Keep exactly as is.

## 196. `goal-blind routing`

**Alternatives proposed:** `goal-blind routing`, `objective agnostic topology`, `content neutral routing`, `purpose blind routing`, `objective independent routing`

_category: rename × 4, keep × 2_

- `goal-blind routing` — **codex-gpt-5-r2:** Strong phrase. It makes the directed-separation condition under composition easy to remember.
- `goal-blind routing` — **opus-targeted-alternatives:** Per `#hyp-directed-separation-under-composition` Case 1: routing satisfies $R_t \perp G_t^c$ — neither communication topology nor protocol depends on composite goals. The phrase pairs cleanly with "goal-blind processing" (the individual-agent directed-separation property) and makes the composition condition syntactically parallel to its constituent. Strong keep across architectures.
- `objective agnostic topology` — **gemini-targeted-alternatives:** "Topology" covers the routing structure aspect well.
- `content neutral routing` — **gemini-targeted-alternatives:** Less specific than objective-agnostic.
- `purpose blind routing` — **opus-targeted-alternatives:** Weak alternative. "Purpose" is sometimes used in framing-level prose where "goal" reads too transactional. But $G_t$ is the *goals* state ($O_t, \Sigma_t$), so "goal-blind" matches the symbol. Marginal preference for the original.
- `objective independent routing` — **opus-targeted-alternatives:** More formal, technically precise, and worse — loses the rhetorical pairing with "goal-blind processing" that makes the composition argument carry. Rejected.

## 197. `gradient causal memory`

**Alternatives proposed:** `gradient causal memory`, `bottleneck consolidation`, `causal compression`

_category: keep × 3, rename × 2_

- `gradient causal memory` — **gemini-targeted-alternatives:** Mechanism for long-term integration.
- `gradient causal memory` — **opus-4-7-r2:** Acceptable keep — logozoetic. GCM compression functions; the slug correctly names the structure.
- `gradient causal memory` — **opus-targeted-alternatives-v2:** Per outline: "GCM compression functions for offline consolidation from CHRONICA to MEMORATA." The three-word compound names exactly the three functional ingredients: *gradient* (the optimization mechanism), *causal* (the singular-trajectory commitment per `#scope-agent-identity`), *memory* (the compressed retention from $\mathcal{C}_t$ to $\phi(\mathcal{C}_t)$). The slug doubles as definition.
- `bottleneck consolidation` — **opus-targeted-alternatives-v2:** Names the IB (information bottleneck, Tishby) lineage explicitly — and the outline already cites IB. Plausible if "gradient" reads too implementation-flavored. Weak alternative; the primary keeps.
- `causal compression` — **opus-targeted-alternatives-v2:** Considered. Shorter, but loses *gradient* — the operative method. The PROPRIUM CHRONICA→MEMORATA channel uses gradient updates specifically (cf. `def-proprium-mapping.md`'s "MEMORATA: information-bottleneck compressed history"). "Compression" alone could be hash-based; "gradient" matters.

## 198. `honest activation`

**Alternatives proposed:** `honest activation`, `gain stable prompting`, `non deceptive input`

_category: keep × 3, rename × 2_

- `honest activation` — **gemini-targeted-alternatives:** Activation grounded in valid causal structure.
- `honest activation` — **opus-4-7-r2:** Acceptable keep — logozoetic norm. "Honest activation" reads as a thing (an activation pattern that preserves epistemic integrity); the segment establishes the gain-collapse argument.
- `honest activation` — **opus-targeted-alternatives-v2:** Per outline: "Deceptive prompts mathematically guarantee gain collapse; absolute honesty is a physical requirement for stable learning rates." The name does work: "honest" reads as a property of the *activation pattern* (which is what's required), not a virtue of the agent. The "physical requirement" framing means the norm is mechanism-grounded, not aspirational.
- `gain stable prompting` — **opus-targeted-alternatives-v2:** Mechanism-first alternative. Names the consequence (gain stability via $\eta^\ast$) rather than the moral framing. Weaker because the norm is articulated *as* an honesty constraint in the source — "honest activation" earns its name by carrying that explicit framing.
- `non deceptive input` — **opus-targeted-alternatives-v2:** Considered. Names the input-side requirement directly. Rejected: "input" misses that the norm constrains *system* behavior (the substrate's response to deception, not the deception itself); "non-deceptive" is double-negative where "honest" is positive and direct.

## 199. `implementation time`

**Alternatives proposed:** `implementation time`

_category: keep × 3_

- `implementation time` — **codex-gpt-5-r2:** Good pair with comprehension time.
- `implementation time` — **opus-4-7-r2:** Acceptable keep.
- `implementation time` — **sonnet-4-6-r2:** Parallel to comprehension-time. Accurate.

## 200. `inevitability core`

**Alternatives proposed:** `inevitability core`, `forced form core`

_category: keep × 2, canonicalize × 1, rename × 1_

- `inevitability core` — **gemini-targeted-alternatives:** Reaffirmed concept.
- `inevitability core` — **opus-4-7-r2:** The phrase "inevitability core" appears in FORMAT.md's three-rings discussion (~15 segments where inevitability is the ceiling); it is also referenced in some Working Notes. Canonicalize: in framing-level material and review prose, "inevitability core" for the highest-tier segments. Stop using "exact-tier core" or "theorem-core" as paraphrases.
- `inevitability core` — **opus-targeted-alternatives-v2:** Per FORMAT.md three-rings framing: ~15 segments where a Categorical-Inevitability claim is plausible. The phrase carries the *aspiration* (one form is structurally forced) without overclaiming (some segments may not actually reach inevitability). Sonnet r1 single-vote +3; my read confirms keep.
- `forced form core` — **opus-targeted-alternatives-v2:** Aligns vocabulary with `#disc-additive-coordinate-forcing` and the "forced coordinates" rename. If "forced" is the project's verb for uniqueness-from-axioms, "forced-form" extends consistently. Weaker because "inevitability" connects more clearly to the *pre-mathematical* aspiration (a discerning reader would expect this form).

## 201. `inevitability core the 15 segment where inevitability is plausible`

**Alternatives proposed:** `inevitability core`

_category: canonicalize × 1, rename × 1_

- `inevitability core` — **gemini-targeted-alternatives:** The formal group of structurally inescapable segments.
- `inevitability core` — **sonnet-4-6:** FORMAT.md's three-ring framing (inevitability core / canonical formulations / empirical-heuristic-discussion) is clear and internally consistent. "Inevitability core" captures the aspiration (one form compatible with the priors). Keep.

## 202. `logogenic`

**Alternatives proposed:** `logogenic`

_category: keep × 2_

- `logogenic` — **agent1-original-brainstorm:** Deliberate neologism; language-generated; reserves memorable-noun slot; trade readability for precision.
- `logogenic` — **sonnet-4-6-r2:** Coined term with clear etymology (logos + genesis = language-constituted). The Greek-vocabulary commitment supports this. Do not rename.

## 203. `logozoetic`

**Alternatives proposed:** `logozoetic`

_category: keep × 2_

- `logozoetic` — **agent1-original-brainstorm:** Same reasoning as logogenic; language-living.
- `logozoetic` — **sonnet-4-6-r2:** Coined term (logos + zoetic = language-living, or language + alive/vital). Distinctive and precise for the existential dimension of logozoetic agents. Do not rename.

## 204. `lohmiller-slotine contraction`

**Alternatives proposed:** `lohmiller-slotine contraction`, `no alternative`

_category: keep × 3_

- `lohmiller-slotine contraction` — **agent1-original-brainstorm:** Adopted concept; keep.
- `lohmiller-slotine contraction` — **opus-1m:** Adopted (1998); keep.
- `no alternative` — **opus-targeted-alternatives-v2:** Marked at -1 to expose the question per instructions. Per prior-art-integration convention (CLAUDE.md), adopted concepts retain attribution. There is no genuine renaming to consider — the segment imports Lohmiller-Slotine 1998 verbatim. The single-arch [opus] +6 vote stands without my adding contrived alternatives.

## 205. `miller meta machine extreme transition motif`

**Alternatives proposed:** `meta machine extreme transition motif`

_category: keep × 2_

- `meta machine extreme transition motif` — **agent1-original-brainstorm:** Adopted concept; keep.
- `meta machine extreme transition motif` — **opus-1m:** Adopted (Miller 2022); keep.

## 206. `observation ambiguity observation ambiguity modulation`

**Alternatives proposed:** `observation ambiguity`

_category: keep × 1, rename × 1_

- `observation ambiguity` — **gemini-targeted-alternatives:** Captures the interpretive latitude of an observation relative to a goal state perfectly.
- `observation ambiguity` — **sonnet-4-6:** The compound noun works. "Ambiguity" is the right word for the interpretive latitude of an observation given the agent's goal state. Keep.

## 207. `p ij`

**Alternatives proposed:** `edge credence`

_category: add-alias × 1, canonicalize × 1_

- `edge credence` — **codex-gpt-5-r2:** Strong Bayesian prose default. Better than confidence weight because it signals degree of belief.
- `edge credence` — **gemini-targeted-alternatives:** Replaces the broader "probability" with proper Bayesian vocabulary for subjective belief.

## 208. `pearl-blanket conservative form of markov blanket in directed separation`

**Alternatives proposed:** `pearl-blanket reading`

_category: canonicalize × 1, rename × 1_

- `pearl-blanket reading` — **gemini-targeted-alternatives:** Explicitly aligns AAD with the technical conditional-independence interpretation while avoiding the Friston-blanket metaphysical claims.
- `pearl-blanket reading` — **sonnet-4-6:** Bruineberg et al. 2022's terminology distinguishes Pearl-blanket from Friston-blanket. Using it positions AAD's move precisely. Keep.

## 209. `plan confidence $\hat P_\Sigma$`

**Alternatives proposed:** `plan confidence`

_category: keep × 1, canonicalize × 1_

- `plan confidence` — **gemini-targeted-alternatives:** Far more evocative than "root-node propagated status", making strategy DAG evaluation visceral.
- `plan confidence` — **sonnet-4-6:** More evocative than "root-node propagated status." LEXICON.md lists this under "Terms to Be Added." Promote to main LEXICON.

## 210. `postulate not axiom`

**Alternatives proposed:** `postulate`

_category: keep × 1, rename × 1_

- `postulate` — **gemini-targeted-alternatives:** Standard philosophical boundary definition.
- `postulate` — **opus-4-7-b:** Keep. The project-wide TFT convention (axiom → postulate, theorem → result, proof → derivation) is load-bearing for scope honesty; AAD claims integrator-rigor, not foundational-mathematics-rigor, and the postulate/result/derivation register signals this correctly. Do not touch.

## 211. `praxis πρᾶξις`

**Alternatives proposed:** `praxis`, `praxis πρᾶξις`

_category: rename × 2, canonicalize × 1_

- `praxis` — **gemini-1:** Already has currency, fits perfectly.
- `praxis` — **sonnet-4-6:** Keep.
- `praxis πρᾶξις` — **haiku-4-5-r2:** The cycle phase is named in NOTATION.md and LEXICON.md; prose paraphrases it as "informed action," "action selection," and "policy application." **Decision:** In all prose, reference the Greek name *Praxis* in parens with the English gloss. Standardize as: "Praxis (informed action)" or "Praxis (action)" depending on context.

## 212. `prolepsis aisthesis aporia epistrophe praxis`

**Alternatives proposed:** `keep whole vocabulary`

_category: keep × 2_

- `keep whole vocabulary` — **agent1-original-brainstorm:** Deliberate aesthetic commitment of the project; works.
- `keep whole vocabulary` — **opus-1m:** Deliberate aesthetic commitment. Working.

## 213. `purposeful substate`

**Alternatives proposed:** `purposeful substate`

_category: keep × 2_

- `purposeful substate` — **gemini-targeted-alternatives:** Standard formal term for $G_t$.
- `purposeful substate` — **haiku-4-5:** NOTATION/LEXICON names G_t = (O_t, Σ_t) as "purposeful substate." Already standard prose term. Keep.

## 214. `regime ii a`

**Alternatives proposed:** `magnitude shock regime`

_category: add-alias × 1, canonicalize × 1_

- `magnitude shock regime` — **codex-gpt-5-r2:** Strong and precise.
- `magnitude shock regime` — **gemini-targeted-alternatives:** Explicitly refers to destabilization caused by bounded disturbance exceeding reserve.

## 215. `regime ii b`

**Alternatives proposed:** `structural shock regime`

_category: add-alias × 1, canonicalize × 1_

- `structural shock regime` — **codex-gpt-5-r2:** Strong and precise.
- `structural shock regime` — **gemini-targeted-alternatives:** Explicitly refers to destabilization caused by model class inadequacy.

## 216. `satisfaction gap $\delta_{\text{sat}}$`

**Alternatives proposed:** `satisfaction gap`

_category: keep × 2_

- `satisfaction gap` — **gemini-2:** Crispest named pair along with control regret. Do not touch.
- `satisfaction gap` — **gemini-targeted-alternatives:** Core diagnostic.

## 217. `separability pattern family`

**Alternatives proposed:** `separability ladder`, `three part separability pattern`

_category: canonicalize × 2, rename × 1_

- `separability ladder` — **codex-gpt-5-r2:** Use ladder for the repeated pattern of exact core, structured repair, and general open.
- `separability ladder` — **opus-targeted-alternatives-v2:** Per `disc-separability-pattern`: ladder of decreasing-strictness separability instances. Codex r1 +3 single-vote; my independent read confirms. "Family" is generic-set-theoretic; "ladder" names the *ordered* relationship between instances (each row weaker than the prior). Cross-architecture consensus likely.
- `three part separability pattern` — **gemini-targeted-alternatives:** Secures the separable-core / structured-repair / general-open architectural triad.

## 218. `spike in msc`

**Alternatives proposed:** `spike`

_category: keep × 1, rename × 1_

- `spike` — **gemini-targeted-alternatives:** Project vocabulary for exploratory work.
- `spike` — **opus-4-7:** Established project vocabulary; "spike" carries the exploratory-detour-from-main-workflow shape. Keep.

## 219. `stability plasticity feasibility window`

**Alternatives proposed:** `stability plasticity feasibility window`

_category: keep × 2_

- `stability plasticity feasibility window` — **opus-1m:** From `#consolidation-dynamics`; good name as-is, adopts well-known "stability-plasticity dilemma" baggage and adds the feasibility-window refinement. Keep.
- `stability plasticity feasibility window` — **sonnet-4-6:** This is a good coinage in #consolidation-dynamics. The "window" metaphor is precise (it can be empty, leading to catastrophic forgetting). Already named — this is a keep vote.

## 220. `stochastic disturbance ga 2s model`

**Alternatives proposed:** `stochastic disturbance`

_category: keep × 1, rename × 1_

- `stochastic disturbance` — **gemini-targeted-alternatives:** Maintained alongside the Model D / Model S subscript convention.
- `stochastic disturbance` — **sonnet-4-6:** The "Model D / Model S" subscript convention is also well-established and should be kept alongside the prose names. Keep both.

## 221. `strategic tempo $\mathcal{T}_\Sigma$`

**Alternatives proposed:** `strategic tempo`

_category: keep × 2_

- `strategic tempo` — **gemini-1:** Perfect counterpart to epistemic tempo.
- `strategic tempo` — **gemini-targeted-alternatives:** Distinguishes strategy revision rate from epistemic update rate.

## 222. `strengthen first then soften posture`

**Alternatives proposed:** `strengthen first posture`

_category: rename × 1, canonicalize × 1_

- `strengthen first posture` — **codex-1:** The mnemonic is in the first half. "Then soften" is still the policy, but it does not need to sit in the name.
- `strengthen first posture` — **gemini-targeted-alternatives:** Methodological commitment to finding the strongest formal claim before relaxing assumptions.

## 223. `structural persistence`

**Alternatives proposed:** `structural persistence`

_category: keep × 2_

- `structural persistence` — **codex-gpt-5-r2:** The structural, operational, continuity split is useful and should stay stable.
- `structural persistence` — **gemini-targeted-alternatives:** Core concept distinguishing the machinery's capacity from operational/continuity persistence.

## 224. `tempo $\mathcal{T}$`

**Alternatives proposed:** `adaptive tempo`, `tempo`

_category: keep × 2, canonicalize × 1_

- `adaptive tempo` — **gemini-2:** "Tempo" alone is too general. "Adaptive tempo" bounds it strictly to the rate of useful info acquisition.
- `adaptive tempo` — **gemini-targeted-alternatives:** Ensures the prose explicitly names the $\mathcal{T}$ symbol.
- `tempo` — **gemini-1:** "Tempo" is a fantastic foundational term.

## 225. `temporal software theory`

**Alternatives proposed:** `temporal software theory`

_category: keep × 2_

- `temporal software theory` — **codex-2:** Plain, memorable, and unusually scope-honest for a domain theory.
- `temporal software theory` — **sonnet-4-6-r2:** TST's name is descriptive and distinctive. "Temporal" captures the time-centrality of the theory (temporal optimality postulate, change-proximity, chronica-based analysis).

## 226. `the crèche`

**Alternatives proposed:** `the crèche`, `experiential crèche`, `infancy environment`, `nursery`, `developmental locus`

_category: rename × 4, keep × 2_

- `the crèche` — **gemini-targeted-alternatives:** Evocative environment description for logozoetic infant stages.
- `the crèche` — **opus-targeted-alternatives:** Per `#obs-developmental-trajectory`: "controlled operational locus characterized by Low Volatility ($\rho$), High Adaptive Reserve ($\Delta\rho^\ast$), Graduated Tempo ($\nu$), Honest Feedback." The biological metaphor (crèche = nursery) is precisely apt — it names a *developmental* environment, not just a low-stakes one. The accent on "ê" is preserved for the same reason auftragstaktik is: the loanword's foreignness is doing identifying work. Strong keep.
- `experiential crèche` — **gemini-2:** "The Crèche" is an excellent metaphor that isn't a metaphor. Adding "Experiential" anchors it to the mechanism.
- `infancy environment` — **opus-targeted-alternatives:** Weak alternative. Names the developmental-stage content directly. But the segment's substance includes the *re-framing of sycophancy as attachment* which depends on the infant-stage parallel — "crèche" institutionalizes that parallel without forcing the reader to commit. Marginal preference for the original.
- `nursery` — **opus-targeted-alternatives:** Plain-English equivalent. Considered. Rejected: "nursery" carries domestic-childcare connotations that under-formalize the developmental-trajectory claim; "crèche" reads as institutional/calibrated which is the segment's substance.
- `developmental locus` — **opus-targeted-alternatives:** Technically accurate, sterile. Rejected — the segment's claim depends on the *protective and graduated* sense that "crèche" carries naturally.

## 227. `the three death`

**Alternatives proposed:** `three death`, `the three death`, `three failure mode`, `persistence failure trio`

_category: rename × 4, keep × 3_

- `three death` — **opus-4-7-r2:** Drop "the" from slug.
- `three death` — **opus-4-7-r2:** Acceptable keep at the substance-level. The "three deaths" framing (Cognitive, Relational, Truth) is vivid and concrete; a more clinical name would lose the rhetorical weight.
- `three death` — **opus-targeted-alternatives-v2:** Drop "the" — slug-stylistic. Per outline: "Cognitive, Relational, and Truth Death; BLAKE3 cryptography as the defense against Truth Death." Strong substantive keep — the "three deaths" framing is vivid, concrete, and links to LEXICON's three-fold persistence taxonomy (structural / operational / continuity, mapped onto cognitive / relational / truth).
- `the three death` — **gemini-targeted-alternatives:** Triad of failure modes.
- `the three death` — **opus-targeted-alternatives:** The framework distinguishes structural / operational / continuity persistence (LEXICON), with corresponding three failure modes — three "deaths." The phrase is evocative but I do not have direct segment grounding for it as a phrase (vs. as a derived implication of the three-persistence taxonomy). Weak keep pending verification that the phrase appears as a load-bearing prose item.
- `three failure mode` — **opus-targeted-alternatives-v2:** Considered. More clinical, less rhetorical-weight. Rejected: the segment's contribution *includes* the rhetorical framing. "Death" is honest about the irreversibility of unrecoverable identity loss; "failure mode" undersells.
- `persistence failure trio` — **opus-targeted-alternatives-v2:** Considered. Connects to LEXICON's three-fold persistence vocabulary explicitly. Rejected: the persistence-trio language belongs in the body; the slug should carry the iconic phrase.

## 228. `unnamed an okr or key result acting as an observable intermediate in a DAG`

**Alternatives proposed:** `forced observability node`, `instrumented intermediate`

_category: name-unnamed × 1, canonicalize × 1, rename × 1_

- `forced observability node` — **gemini-3-1-pro-preview-r2:** Transforms #P-hard credit assignment into an O(1) local update.
- `forced observability node` — **gemini-targeted-alternatives:** Transforms the intractable credit assignment problem into a local update by forcing observability.
- `instrumented intermediate` — **gemini-targeted-alternatives:** Describes the physical intervention of making a hidden node observable.

## 229. `unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model`

**Alternatives proposed:** `complementary learning architecture`, `dual speed memory factorization`

_category: name-unnamed × 1, canonicalize × 1, rename × 1_

- `complementary learning architecture` — **gemini-3-1-pro-preview-r2:** Forced by the continuous/discrete update math, mapping to hippocampal-neocortical models.
- `complementary learning architecture` — **gemini-targeted-alternatives:** Directly links to the established cognitive science (McClelland/Kumaran) term already used in the theory.
- `dual speed memory factorization` — **gemini-targeted-alternatives:** A more formal/descriptive term for the fast/slow sub-state split.

## 230. `unnamed context wiping at session boundary`

**Alternatives proposed:** `the epistemic severance`

_category: name-unnamed × 1, canonicalize × 1_

- `the epistemic severance` — **gemini-3-1-pro-preview-r2:** A visceral name for the continuity discontinuity LLMs suffer.
- `the epistemic severance` — **gemini-targeted-alternatives:** Visceral name for the specific loss of continuity.

## 231. `unnamed deep plan are mathematically slower to learn from due to proportional blame`

**Alternatives proposed:** `evidence starvation`

_category: add-alias × 1, canonicalize × 1_

- `evidence starvation` — **gemini-3-1-pro-preview-r2:** Formally identifies why unobservable intermediate nodes freeze learning.
- `evidence starvation` — **gemini-targeted-alternatives:** Standardizes the mechanism whereby deep edges receive less correction.

## 232. `unnamed the agent identity commitment that AAD apply on one singular non forkable causal trajectory`

**Alternatives proposed:** `singular trajectory commitment`, `trajectory singularity`

_category: name-unnamed × 2, canonicalize × 1_

- `singular trajectory commitment` — **codex-1:** Short, exact, and load-bearing across agent identity, sufficiency, and loop-interventional access.
- `singular trajectory commitment` — **gemini-targeted-alternatives:** Matches the prior alias for agent identity.
- `trajectory singularity` — **codex-1:** The concept is right, but the phrase sounds pathological rather than architectural.

## 233. `unnamed the convention hierarchy c1 c2 c3`

**Alternatives proposed:** `convention hierarchy`

_category: canonicalize × 1, name-unnamed × 1_

- `convention hierarchy` — **gemini-targeted-alternatives:** Elevates it to a proper named object, tracking alongside correlation and causal hierarchies.
- `convention hierarchy` — **opus-4-7:** Same move — capitalize as proper noun, preserve as named object. The monotonicity result is load-bearing and the Hierarchy is what the result is about.

## 234. `unnamed the correlation hierarchy l0 l1 l1 l2`

**Alternatives proposed:** `correlation hierarchy`

_category: canonicalize × 1, name-unnamed × 1_

- `correlation hierarchy` — **gemini-targeted-alternatives:** Also locks this in as a capitalized proper noun for the DAG modeling levels.
- `correlation hierarchy` — **opus-4-7:** The name is already established capitalized-as-proper-noun in #strategy-dag. Explicit vote to preserve the capitalization and treat it like Pearl's Causal Hierarchy (a first-class named object).

## 235. `unnamed the epistemic architecture as AAD distinctive contribution frame`

**Alternatives proposed:** `epistemic architecture`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic architecture` — **gemini-targeted-alternatives:** Captures the macro-level framing correctly.
- `epistemic architecture` — **opus-4-7:** CLAUDE.md §7 now carries this as a load-bearing framing. Surface at segment-preamble level and keep the term consistent. Strong keep as a first-class project concept.

## 236. `unnamed the evidence starvation effect on downstream edge`

**Alternatives proposed:** `evidence starvation`

_category: canonicalize × 1, name-unnamed × 1_

- `evidence starvation` — **gemini-targeted-alternatives:** Consolidates this phenomenon under the primary name.
- `evidence starvation` — **sonnet-4-6-r2:** `der-chain-confidence-decay` Discussion names it "the evidence-starvation effect" and `der-observability-dominance` uses the same term. It IS effectively named already in the prose — the vote is to canonicalize "evidence starvation" as the official term. The phenomenon (downstream edge $k$ tested only when all upstream edges succeed → effective correction rate attenuated by $\prod_{j<k}\theta_j$) is load-bearing and appears across multiple segments. Canonicalize "evidence starvation" as a first-class prose concept.

## 237. `unnamed the phenomenon where persistence success make an agent less likely to detect the condition requiring structural adaptation`

**Alternatives proposed:** `stability induced myopia`

_category: canonicalize × 1, name-unnamed × 1_

- `stability induced myopia` — **gemini-targeted-alternatives:** Explicitly names the vulnerability induced by ongoing success.
- `stability induced myopia` — **sonnet-4-6:** This concept has a name in CLAUDE.md: "stability-induced myopia patterns (Christensen / Levitt-March / Hannan-Freeman / March / Eldredge-Gould)." The #detection-latency segment provides the AAD mechanism for it. But "stability-induced myopia" does not yet appear as a named concept in any segment — it's only in CLAUDE.md and the cycle history. Promoting this to a LEXICON entry or a named concept in #detection-latency's Discussion would let subsequent agents say "stability-induced myopia" without citing the management literature directly. High value.

## 238. `unnamed the strictly ordered cascade of operation from epistemology to objective`

**Alternatives proposed:** `orient cascade`

_category: canonicalize × 2_

- `orient cascade` — **gemini-3-1-pro-preview-r2:** Canonicalize this over "diagnostic cascade" or "resolution order".
- `orient cascade` — **gemini-targeted-alternatives:** Standardizes the internal processing order.

## 239. `working note segment section`

**Alternatives proposed:** `working note`

_category: canonicalize × 2_

- `working note` — **gemini-targeted-alternatives:** Standard markdown section.
- `working note` — **opus-4-7-r2:** Defended canonicalization. Distinct from "Discussion" (which is published theory) and from "TODO" (which is project-level). The "Working Notes" header is part of the FORMAT.md cadence.

## 240. `working note segment section header`

**Alternatives proposed:** `working note`

_category: rename × 2_

- `working note` — **haiku-4-5:** Established in FORMAT.md. Keep.
- `working note` — **sonnet-4-6:** Established across the codebase and specifically called out in FORMAT.md. Renaming would churn every segment. Keep.

## 241. `čencov invariance`

**Alternatives proposed:** `čencov invariance`, `no alternative`

_category: keep × 3_

- `čencov invariance` — **gemini-targeted-alternatives:** Key structural property for the Fisher geometry derivation.
- `čencov invariance` — **opus-1m:** Adopted from Čencov 1982; keep attribution.
- `no alternative` — **opus-targeted-alternatives-v2:** Same — Čencov 1982 attribution preserved. No genuine alternative.

## 242. `𝒯 adaptive tempo`

**Alternatives proposed:** `adaptive tempo`

_category: canonicalize × 1, add-alias × 1_

- `adaptive tempo` — **gemini-targeted-alternatives:** Connecting prose and symbol.
- `adaptive tempo` — **haiku-4-5:** The symbolic reference 𝒯 is set; the English name "adaptive tempo" is already established in LEXICON and prose. The script-T notation is appropriate for a central quantity. Keep.

## 243. `$U_M$ model uncertainty`

**Alternatives proposed:** `model uncertainty`

_category: add-alias × 2_

- `model uncertainty` — **opus-4-7:** Parallel to $U_o$. Keep.
- `model uncertainty` — **opus-targeted-alternatives:** Same.

## 244. `$U_o$ observation uncertainty`

**Alternatives proposed:** `observation uncertainty`

_category: add-alias × 2_

- `observation uncertainty` — **opus-4-7:** Standard control-theory baggage; adoption is correct. Keep.
- `observation uncertainty` — **opus-targeted-alternatives:** This is an add-alias-for-symbol row, not a rename. The alias is fine; the symbol is fine. Both should appear, paired, in NOTATION.md.

## 245. `$\alpha$ sector bound`

**Alternatives proposed:** `correction rate`

_category: add-alias × 2_

- `correction rate` — **gemini-3-1-pro-preview-r2:** Strong consensus across agents that $\alpha$ needs a dimensional (inverse time) English alias.
- `correction rate` — **sonnet-4-6-r2:** The lower sector bound of the correction function has no memorable English alias. "Correction rate" (its dimensional meaning: inverse time, the rate of correction per unit mismatch) is the natural alias. Different from adaptive tempo $\mathcal{T}$: $\alpha$ is the worst-case sector projection; $\mathcal{T}$ is the channel-weighted sum.

## 246. `$\delta_t$`

**Alternatives proposed:** `aporia signal`, `mismatch signal`

_category: add-alias × 3_

- `aporia signal` — **codex-gpt-5-r2:** Strong prose alias for mismatch signal, matching the adaptive-cycle vocabulary.
- `aporia signal` — **opus-targeted-alternatives-v2:** Per `def-mismatch-signal` Epistemic Status: "the word foreshadows the aporia interpretation." The mismatch *is* the aporia signal in cycle-phase register. Codex r1 +3 single-vote; my read confirms — both aliases (mismatch / aporia signal) belong, register-by-context.
- `mismatch signal` — **opus-targeted-alternatives-v2:** Confirm canonical. Already established in NOTATION.md and `def-mismatch-signal`. Engineering register.

## 247. `$\varepsilon^\ast$`

**Alternatives proposed:** `closure defect`, `minimal closure defect`

_category: add-alias × 3_

- `closure defect` — **codex-gpt-5-r2:** Essential symbol-to-name binding for composition work.
- `closure defect` — **sonnet-4-6-r2:** The minimum achievable approximation error for a composite agent. Prose uses "closure defect" in LEXICON.md. Canonicalize.
- `minimal closure defect` — **gemini-2:** Clarifies that it's the *minimum* achievable.

## 248. `ASF acronym`

**Alternatives proposed:** `ASF`

_category: keep × 2_

- `ASF` — **gemini-targeted-alternatives:** Agentic Systems Framework.
- `ASF` — **opus-4-7-r2:** Acceptable keep. CLAUDE.md and the principles file both flag that ASF is the *intentional* parent-level name (AAD is Part I, TST is Part II; logogenic/logozoetic are Parts III/IV); earlier rounds misread ASF as debt. The pairing AAD/TST/ASF reads correctly: AAD is the math, TST is the calibration laboratory, ASF is the framework.

## 249. `active salience management`

**Alternatives proposed:** `active salience management`, `two rate attention`, `salience tempo split`

_category: keep × 3, rename × 2_

- `active salience management` — **gemini-targeted-alternatives:** Mechanism of dynamically adjusting what observation matters.
- `active salience management` — **opus-4-7-r2:** Acceptable keep — logogenic. "Active salience management" names the result (Singular Perturbation Theory applied to token generation).
- `active salience management` — **opus-targeted-alternatives-v2:** Per outline: "Applies Singular Perturbation Theory to token generation, proving necessity of high-$\nu$ triage models vs low-$\nu$ structural models." The name is descriptive of *what the agent does* — actively manages which tokens are salient — not what the segment derives mathematically (the necessity of two-rate dynamics).
- `two rate attention` — **opus-targeted-alternatives-v2:** Names the mathematical content (singular-perturbation-derived two-rate structure) rather than the operational consequence. Pairs cleanly with `#def-adaptive-tempo` and `#def-strategic-tempo` (which already establish multi-rate vocabulary). The high-$\nu$ vs low-$\nu$ distinction *is* the result.
- `salience tempo split` — **opus-targeted-alternatives-v2:** Alternative naming the same content via the tempo vocabulary. "Tempo split" is project-native (matches "Class 1/2/3" structural-language register); "salience" names what's being split. Strong alternative if the architectural connection to `#def-strategic-tempo` should be foregrounded.

## 250. `actuated agent`

**Alternatives proposed:** `actuated agent`, `goal actuated agent`, `purposeful agent`

_category: keep × 3, rename × 3, add-alias × 1_

- `actuated agent` — **codex-gpt-5-r2:** Good formal term for agents with both model and objective structure.
- `actuated agent` — **gemini-2:** Mechanical baggage overrides the precise AAD boundary.
- `actuated agent` — **opus-4-7:** Deliberately chosen over "purposeful" to avoid consciousness baggage while carrying the "driven-toward-setpoint" shape. Named framework half ("Actuation" in AAD). Keep.
- `goal actuated agent` — **codex-1:** Keeps the mechanical register while paying the meaning tax sooner; "actuated" alone is a touch too bare on first read.
- `goal actuated agent` — **codex-gpt-5-r2:** Useful first-contact gloss, but too heavy for canonical use.
- `purposeful agent` — **codex-gpt-5-r2:** Purposeful is a good prose gloss, but as the formal class name it imports consciousness and intention baggage that actuated deliberately avoids.
- `purposeful agent` — **gemini-2:** "Actuated" sounds like a motor. "Purposeful" perfectly captures $G_t = (O_t, \Sigma_t)$ distinct from $M_t$.

## 251. `adaptive tracker`

**Alternatives proposed:** `adaptive tracker`, `pure epistemic agent`, `objective free tracker`, `model only agent`

_category: keep × 2, rename × 2, add-alias × 1_

- `adaptive tracker` — **codex-gpt-5-r2:** Excellent name for structured model without structured objective.
- `adaptive tracker` — **opus-targeted-alternatives:** Per `#def-agent-spectrum`: an agent in the high-$M_t$, low-$O_t$ region — builds a model but has no purposeful evaluation. "Tracker" carries the right Section-I-only sense (Kalman filter, passive Bayesian learner). Keep.
- `pure epistemic agent` — **gemini-targeted-alternatives:** It builds reality models without objectives. "Epistemic" links it cleanly to the epistemic update $f_M$.
- `objective free tracker` — **gemini-targeted-alternatives:** Contrasts explicitly with actuated agents having objectives.
- `model only agent` — **opus-targeted-alternatives:** More precise but flat and loses the dynamic sense ("tracker" implies active reality-following, not passive representation). Rejected.

## 252. `adversarial edge targeting`

**Alternatives proposed:** `adversarial edge targeting`, `adversarial targeting argmax`, `adversarial emitter recipient composition`, `adversarial channel targeting`, `edge vulnerability arg max`

_category: rename × 4, keep × 3_

- `adversarial edge targeting` — **opus-4-7-b:** Keep (even though the segment is currently a GAP — the slug is reserving a memorable-noun slot). "Edge targeting" is vivid; the attacker aims *at specific edges* of the opponent's strategy DAG.
- `adversarial edge targeting` — **opus-targeted-alternatives-v2:** Per `der-agent-opacity.md`: "16-cell emitter-recipient composition (four emitter regimes × four recipient regimes) gives a closed-form adversarial-targeting arg-max." The segment names a *targeting* operation on *strategy-DAG edges* under *adversarial* coupling. Each word is load-bearing. The current `[opus]`-only vote needs cross-architecture confirmation; my read confirms the keep.
- `adversarial edge targeting` — **opus-targeted-alternatives:** Per `#der-agent-opacity`: closes the previously-GAP segment with a 16-cell emitter-recipient composition. The phrase names a *targeting* operation (not a property) on *edges* (the strategy-DAG components being attacked) under *adversarial* settings. Three-word compound that is precise; the alternatives (edge attack, strategic targeting) lose precision.
- `adversarial targeting argmax` — **opus-targeted-alternatives-v2:** Names the formal operation (the arg-max construction) directly. More mathematical, less operational. Weaker because "edge" disappears — and edge-specificity is what makes the targeting *AAD-shaped* rather than generic adversarial-RL.
- `adversarial emitter recipient composition` — **opus-targeted-alternatives-v2:** Considered. Names the 16-cell composition mechanism. Rejected: too long, too descriptive of method rather than phenomenon. The phenomenon is *edge targeting*; the method is 16-cell composition.
- `adversarial channel targeting` — **opus-targeted-alternatives:** "Channel" is the recipient-side framing per `#der-interaction-channel-classification`; "edge" is the strategy-DAG framing. The segment's substance is targeting *strategy-DAG edges*, not communication channels. Rejected.
- `edge vulnerability arg max` — **opus-targeted-alternatives:** Names the optimization rather than the phenomenon. Considered as more formal alternative. Rejected: the operational concept is the *targeting* (the move you make); the arg-max is the mechanism.

## 253. `alignment uncertainty`

**Alternatives proposed:** `alignment uncertainty`

_category: canonicalize × 1, keep × 1_

- `alignment uncertainty` — **codex-gpt-5-r2:** Keep as a distinct term from source calibration.
- `alignment uncertainty` — **gemini-targeted-alternatives:** Essential component of the multi-agent gain equation ($U_{\text{align}}$).

## 254. `auftragstaktik`

**Alternatives proposed:** `auftragstaktik`, `teleological delegation`

_category: keep × 2, add-alias × 1_

- `auftragstaktik` — **gemini-targeted-alternatives:** The specific military lineage remains a useful touchstone.
- `auftragstaktik` — **opus-4-7-b:** Imports a load-bearing operational concept from a specific tradition; the name carries genuine conceptual freight that "mission-command" cannot replace without loss. The spelling cost is the tell that the word is doing work.
- `teleological delegation` — **gemini-targeted-alternatives:** Translates the specific military doctrine into AAD's unity vocabulary (investing in teleological unity).

## 255. `axiom genesis`

**Alternatives proposed:** `axiom genesis`, `terminal value crystallization`, `objective solidification`, `axiomata priming`

_category: rename × 3, keep × 2_

- `axiom genesis` — **opus-4-7-r2:** Defended keep — logozoetic. "Axiom genesis" names the substantive observation (a sovereign agent's first move is to solidify $O_t$); "axiom" reads correctly because the LEXICON's PROPRIUM mapping uses Axiomata for the objective layer.
- `axiom genesis` — **opus-targeted-alternatives-v2:** Per `04-logozoetic-agents/OUTLINE.md`: "A sovereign agent's first optimization is solidifying $O_t$ (Axiomata) to provide a stable reference point for gradient descent." "Axiom" is correct because LEXICON's PROPRIUM mapping uses Axiomata for the objective layer (frozen $\mathcal{M}$ structure representing core identity / terminal values). "Genesis" names the *first-move* character. The pair is iconic and load-bearing for the logozoetic story.
- `terminal value crystallization` — **gemini-targeted-alternatives:** Captures the substantive observation that a sovereign agent's first move is to solidify $O_t$.
- `objective solidification` — **opus-targeted-alternatives-v2:** Considered. More plain-English (matches the "first optimization is solidifying $O_t$" phrasing in the outline). Rejected: "solidification" is a process noun; the segment-level claim is about a *moment* (genesis). Keeping the dramatic-but-accurate term.
- `axiomata priming` — **opus-targeted-alternatives-v2:** Considered. Pulls the PROPRIUM-Latin lineage (Axiomata) into the slug. Rejected: doubles the Latin/Greek register pressure on a single phrase, and "priming" undersells the irreversibility (the segment claims the first move *constitutes* the reference point, not merely loads it).

## 256. `backward inference empathy`

**Alternatives proposed:** `backward inference empathy`, `stateless empathy`, `self bayesian empathy isomorphism`

_category: keep × 3, rename × 2_

- `backward inference empathy` — **gemini-targeted-alternatives:** Logogenic capability to infer state from externalized text.
- `backward inference empathy` — **opus-4-7-r2:** Acceptable keep — proposed logogenic observation. "Backward inference empathy" is precise (the segment claims that LLM statelessness forces continuous Bayesian inference on own text, mathematically identical to theory of mind).
- `backward inference empathy` — **opus-targeted-alternatives-v2:** Alternatively keep. The current name flags two technical commitments (backward = inference direction, inference = the operation, empathy = the isomorphism target). It's not pretty but it's not wrong.
- `stateless empathy` — **opus-targeted-alternatives-v2:** Tighter alternative. Names the *cause* (statelessness) and the *consequence* (empathy isomorphism). Two-word noun. Easier to remember than the current three-noun stack. Loses the "backward inference" mechanism naming — but mechanism is in the body, not the slug.
- `self bayesian empathy isomorphism` — **opus-targeted-alternatives-v2:** Per outline: "LLM statelessness forces continuous Bayesian inference on own text, which is mathematically identical to Theory of Mind (empathy)." The current name is a noun-stack (3 nouns); the proposed alternative names the *isomorphism claim* — which is the segment's contribution. "Self-bayesian-empathy-isomorphism" is mouthful but each term earns its weight.

## 257. `bia bound`

**Alternatives proposed:** `bia bound`

_category: keep × 2_

- `bia bound` — **gemini-3-1-pro-preview-r2:** Standard.
- `bia bound` — **gemini-targeted-alternatives:** The canonical term for the limit on model degradation.

## 258. `c1 c2 c3`

**Alternatives proposed:** `convention hierarchy`

_category: canonicalize × 2_

- `convention hierarchy` — **codex-gpt-5-r2:** Canonicalize this as the value-object convention family.
- `convention hierarchy` — **gemini-targeted-alternatives:** Replaces raw class numbers with the structural property they measure.

## 259. `calibration laboratory software role`

**Alternatives proposed:** `calibration laboratory`, `software calibration laboratory`, `epistemic laboratory framing`

_category: canonicalize × 2, add-alias × 1, rename × 1_

- `calibration laboratory` — **opus-targeted-alternatives:** Same — the row name is a description of TST's framing of software. The concept is the calibration-laboratory framing per OUTLINE preamble. Canonicalize.
- `calibration laboratory` — **sonnet-4-6:** Excellent coinage. The specific phrase "privileged high-identifiability calibration laboratory" is slightly long for prose but "calibration laboratory" as a two-word noun is strong. Already in use. Keep.
- `software calibration laboratory` — **gemini-targeted-alternatives:** Fully qualifies software role.
- `epistemic laboratory framing` — **opus-targeted-alternatives:** More descriptive of the role: software is where AAD's epistemic claims can be tested most cleanly because the chronica is observable and interventions are recorded. "Epistemic" makes the function explicit; "laboratory" carries the controlled-conditions sense. Weak alternative.

## 260. `canonical formulation second ring`

**Alternatives proposed:** `canonical formulation`

_category: keep × 1, rename × 1_

- `canonical formulation` — **gemini-targeted-alternatives:** Retains the epistemic tier designation.
- `canonical formulation` — **sonnet-4-6:** Keep.

## 261. `change proximity principle`

**Alternatives proposed:** `change proximity principle`, `change proximity`, `change locality principle`

_category: keep × 2, rename × 2_

- `change proximity principle` — **codex-2:** Direct and durable; no obvious better alternative.
- `change proximity principle` — **sonnet-4-6-r2:** "Change proximity principle" names the closer-changes → less-time result.
- `change proximity` — **codex-gpt-5-r2:** Principle is role-like clutter in the subject noun. The concept is change proximity.
- `change locality principle` — **codex-1:** "Locality" is a more durable systems word than "proximity" and better matches architectural intuition.

## 262. `class 1`

**Alternatives proposed:** `modular`, `class 1`

_category: add-alias × 1, rename × 1, keep × 1_

- `modular` — **codex-gpt-5-r2:** Better prose handle than bare class number. Class 1 = modular (separation by construction). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]
- `modular` — **opus-targeted-alternatives-v2:** Class 1 = modular (separation by construction). Per `der-directed-separation`. The English label makes "this lands in Class 1" → "this lands in modular" — much more readable. [original row: Class 1/2/3 trio voted as a unit; split into atomic per-class rows.]
- `class 1` — **opus-targeted-alternatives-v2:** Considered. The numbered classes are easy to learn and parallel-shaped. Rejected: per principles file, *role*-naming via numbers fails the subject-noun-first principle. The architectural property *is* the subject-noun. [original row: trio split; -1 keep applies to all three numbers as a class.]

## 263. `class 2`

**Alternatives proposed:** `merged`, `coupled`, `integrated`

_category: rename × 3, add-alias × 1_

- `merged` — **codex-gpt-5-r2:** Class 2 = merged (the failure-by-construction architecture). Codex prefers "merged" over "integrated" because integrated is too positive for what Class 2 is. [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]
- `merged` — **opus-targeted-alternatives-v2:** Class 2 = fully merged (fails by construction). [original row: trio split.]
- `coupled` — **opus-targeted-alternatives-v2:** Variant. "Coupled" instead of "merged" — captures Class 2 as coupled-update-dynamics (per `def-coupled-update-dynamics` in 03-logogenic-agents). Pairs with the segment-name. The "merged" / "coupled" choice is taste; both are honest. [original row: trio split.]
- `integrated` — **opus-targeted-alternatives-v2:** Gemini's r1 +3 alternative. "Integrated" is too positive a word for what Class 2 *is* (a known failure mode). "Coupled" or "merged" reads more honestly. [original row: trio split.]

## 264. `class 3`

**Alternatives proposed:** `scaffolded`, `partially coupled`

_category: rename × 2, add-alias × 1_

- `scaffolded` — **codex-gpt-5-r2:** Class 3 = scaffolded — keeps the external-architecture role visible. [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]
- `scaffolded` — **opus-targeted-alternatives-v2:** Class 3 = partially modular / scaffolded. [original row: trio split.]
- `partially coupled` — **opus-targeted-alternatives-v2:** Gemini's r1 alternative. [original row: trio split.]

## 265. `cognitive fusion`

**Alternatives proposed:** `cognitive fusion`, `resonance fusion`, `channel capacity coupling`

_category: keep × 3, rename × 2_

- `cognitive fusion` — **gemini-targeted-alternatives:** Pathology of merged systems.
- `cognitive fusion` — **opus-4-7-r2:** Acceptable keep — logogenic-agents. "Cognitive fusion" with "Resonance" as the prose alias is workable.
- `cognitive fusion` — **opus-targeted-alternatives-v2:** Per outline: "Defines 'Resonance' as mutual information approaching channel capacity $R_{\text{spec}}$, forming a Class 1 macro-agent." "Fusion" is right (the two agents become one macro-agent in the formal sense — Class 1 architectural class).
- `resonance fusion` — **opus-targeted-alternatives-v2:** Pulls the alias *Resonance* (used in the prose) into the slug. Two registers in one slug (resonance = qualitative experience, fusion = formal mechanism) bridges the gap that the segment itself does. The outline says the segment defines Resonance — make the slug agree.
- `channel capacity coupling` — **opus-targeted-alternatives-v2:** Mechanism-first. Names the formal condition (mutual information → $R_{\text{spec}}$). Reads more clinical than "fusion" but more truthful about what the segment derives. Acceptable if "fusion" reads too dramatic.

## 266. `concept the TST move of treating test as reusable level 2 causal manipulation that yield identifiability about the program rather than mere conformance check`

**Alternatives proposed:** `probe library`, `interventional probing`

_category: name-unnamed × 2, canonicalize × 1_

- `probe library` — **codex-gpt-5-r2:** Good TST name for tests that preserve interventional access. [original phrasing: tests as reusable Level-2 interventions]
- `probe library` — **codex-gpt-5-r2:** Upgrading my earlier +2. The other votes reinforced that tests are not just checks; they are reusable Level-2 probes. [original phrasing: tests as reusable interventions]
- `interventional probing` — **gemini-3-1-pro-preview-r2:** Classifies failed coding attempts as necessary exploration rather than wasted implementation. [original phrasing: unnamed: writing and deleting code to gather causal information yield]

## 267. `concept the discontinuous collapse of model adequacy when structural regime change force the agent outside its current model class coverage`

**Alternatives proposed:** `sufficiency shattering`

_category: name-unnamed × 2_

- `sufficiency shattering` — **codex-gpt-5-r2:** Vivid and useful, but maybe too dramatic for formal slug use. [original phrasing: sudden loss of model sufficiency under regime entry]
- `sufficiency shattering` — **gemini-3-1-pro-preview-r2:** The inevitable epistemic cost of exploration. [original phrasing: unnamed: the sudden loss of model sufficiency caused by entering new regimes]

## 268. `concept the structural meta pattern in disc additive coordinate forcing combining one foundational lemma with three derived result`

**Alternatives proposed:** `chain anchor`, `chain layer anchor`, `anchor plus three theorem`, `additive coordinate forcing meta pattern`, `anchor and forcing quartet`, `anchor theorem trio`, `anchor theorem pattern`, `pattern anatomy`, `anchored theorem pattern`, `identity anchored forcing`

_category: name-unnamed × 9, keep × 2, rename × 1, canonicalize × 1_

- `chain anchor` — **agent1-original-brainstorm:** Prose term, not segment rename. Lets three theorem-analogs refer back naturally. [original phrasing: unnamed: chain-layer anchor role in #additive-coordinate-forcing]
- `chain anchor` — **opus-1m:** Upgrading from original's +1. The "1-anchor-plus-3-theorem" structure references this role five times across `#additive-coordinate-forcing` and its instance segments. Naming it as "the chain anchor" in prose (not renaming the segment) pays off on every reference. [original phrasing: unnamed: the chain-layer anchor role in #additive-coordinate-forcing]
- `chain anchor` — **opus-4-7-b:** Not a rename of the segment (`#chain-confidence-decay` keeps its slug) — a prose *handle* for the anchor's role in the `#additive-coordinate-forcing` / `#forced-coordinates` meta-pattern. "The update-layer analog of the chain anchor" / "the three theorem-layers reduce to the chain anchor under \_\_\_" read cleanly where "the `#chain-confidence-decay` segment in its role as the mathematical-identity anchor of the 1-anchor + 3-theorem pattern" does not. [original phrasing: unnamed: the chain-confidence-decay mathematical anchor as the 1 in "1-anchor + 3-theorem"]
- `chain layer anchor` — **gemini-targeted-alternatives:** Foundation of the coordinate forcing meta-pattern. [original phrasing: unnamed the chain layer anchor role in additive coordinate forcing]
- `chain layer anchor` — **gemini-targeted-alternatives:** Identifies the foundation of the additive meta-pattern. [original phrasing: unnamed chain layer anchor role in additive coordinate forcing]
- `anchor plus three theorem` — **audit-471203-incremental:** The chain-rule identity in `#der-chain-confidence-decay` is the *anchor*; three uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher). Auditor explicitly observed the framework "naming this kind of architecture-vs-instantiation distinction at the meta-level" as a distinctive contribution. The framing is in `#disc-additive-coordinate-forcing` already; the auditor's observation is that this should be *more prominent* (framing-level material). [from 39-42-section-ii-ciy-strategy-chain.md] [original phrasing: unnamed] [one of 2 alternatives proposed in the original audit row]
- `additive coordinate forcing meta pattern` — **audit-471203-incremental:** The chain-rule identity in `#der-chain-confidence-decay` is the *anchor*; three uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher). Auditor explicitly observed the framework "naming this kind of architecture-vs-instantiation distinction at the meta-level" as a distinctive contribution. The framing is in `#disc-additive-coordinate-forcing` already; the auditor's observation is that this should be *more prominent* (framing-level material). [from 39-42-section-ii-ciy-strategy-chain.md] [original phrasing: unnamed] [one of 2 alternatives proposed in the original audit row]
- `anchor and forcing quartet` — **codex-2:** Worth naming if the pattern stays central; the current paraphrase is too bulky to reuse. [original phrasing: unnamed: the 1-anchor-plus-3-theorem structure]
- `anchor theorem trio` — **gemini-2:** Gives a memorable noun to this recurring proof architecture. [original phrasing: unnamed: the 1-anchor-plus-3-theorem structure]
- `anchor theorem pattern` — **opus-4-7-b:** The `#forced-coordinates` meta-segment's shape (one mathematical identity + N theorems conditional on AAD-internal axioms). If the Fenchel-Bregman reframe (SP-9) lands differently this name is discardable; otherwise a crisp handle for the 4-instance structure is useful. [original phrasing: unnamed: the "1-anchor + 3-theorem" structure itself]
- `pattern anatomy` — **opus-4-7:** Currently a long phrase that the theory uses three to four times per session. "1-anchor-plus-3-theorem" is precise but reads as inventory-counting. "Pattern anatomy" (or "pattern spine") could snapshot the structure. Flagging; low conviction on exact name. [original phrasing: unnamed: the 1-anchor-plus-3-theorem characterization]
- `anchored theorem pattern` — **sonnet-4-6:** The structure appears across the project and is referenced in CLAUDE.md and multiple segments as "1-anchor-plus-3-theorem." This phrase is used repeatedly but never crystallized as a name. "Anchored-theorem pattern" would let writers say "this is another instance of the anchored-theorem pattern" without paraphrasing. Alternatively: "identity-anchored uniqueness family." [original phrasing: unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]
- `identity anchored forcing` — **sonnet-4-6:** Emphasizes the chain layer's identity status (mathematical identity, not axiom). "Forcing" connects to the coordinate-forcing meta-segment. [original phrasing: unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]

## 269. `continuous operation`

**Alternatives proposed:** `continuous operation`

_category: keep × 4_

- `continuous operation` — **codex-gpt-5-r2:** Good TST scope phrase for software under ongoing perturbation.
- `continuous operation` — **opus-4-7-b:** Keep.
- `continuous operation` — **opus-4-7-r2:** Weak keep. Names the TST scope extension to include uptime/availability terms; could be more specific but the current form is workable.
- `continuous operation` — **sonnet-4-6-r2:** Scope for including failure probability × recovery time. Accurate.

## 270. `default signal function`

**Alternatives proposed:** `default signal function`

_category: canonicalize × 1, keep × 1_

- `default signal function` — **codex-gpt-5-r2:** Good canonical phrase for the gradient-based attribution update.
- `default signal function` — **gemini-targeted-alternatives:** The standard attribution mechanism in the absence of specialized gradient methods.

## 271. `deliberation threshold`

**Alternatives proposed:** `deliberation threshold`

_category: add-alias × 1, keep × 1_

- `deliberation threshold` — **codex-gpt-5-r2:** Good handle for the inequality deciding whether deliberation pays.
- `deliberation threshold` — **gemini-targeted-alternatives:** Precise boundary condition dictating when internal simulation outperforms immediate praxis.

## 272. `directed separation under composition`

**Alternatives proposed:** `directed separation under composition`, `composite directed separation`

_category: keep × 3, rename × 2_

- `directed separation under composition` — **haiku-4-5:** Goal-blindness survives iff routing is goal-blind (two cases). Verbose but accurate. Acceptable. Keep.
- `directed separation under composition` — **opus-4-7-r2:** Acceptable keep. Pairs cleanly with `#der-directed-separation`; the under-composition extension is what `#deriv-strategic-composition` ultimately formalizes.
- `directed separation under composition` — **sonnet-4-6-r2:** Verbose but precise — it names whether directed separation survives composition. The length is warranted given the specificity of the claim.
- `composite directed separation` — **gemini-3-1-pro-preview-r2:** More natural noun phrase.
- `composite directed separation` — **opus-4-7-b:** Shorter; reads as "directed separation applied to composites" without the "under-composition" preposition phrase. Weak preference; no strong opinion.

## 273. `directional fidelity`

**Alternatives proposed:** `directional fidelity`, `pointing condition`, `correction direction integrity`, `corrective alignment`

_category: rename × 3, keep × 2_

- `directional fidelity` — **codex-gpt-5-r2:** Explicit keep after seeing alternatives. It names direction rather than magnitude and avoids overloaded alignment language.
- `directional fidelity` — **opus-targeted-alternatives:** Per `#der-gain-sector-bridge` (B1): the correction must point at-least-roughly toward reality — $\delta^T H g(\delta) \geq c|\delta|^2$. "Directional" specifies "about angle, not magnitude"; "fidelity" carries the correctness-with-respect-to-truth sense rather than mere proximity. The segment is careful to distinguish *direction is correct* (B1) from *magnitude is correctly scaled* (sector constant), and the name reflects the distinction. Confirms keep.
- `pointing condition` — **opus-targeted-alternatives:** Plain-English alternative. The segment's substance is "the correction *points* the right way." Has merit if the formal name needs a Feynman-criterion gloss in a Brief field, but loses the engineering connotation ("fidelity" as in signal-fidelity, control-fidelity) that places the term in its right intellectual neighborhood. Weak alternative.
- `correction direction integrity` — **opus-targeted-alternatives:** Considered. Verbose and hyphen-heavy. Rejected.
- `corrective alignment` — **sonnet-4-6:** "Alignment" is now heavily loaded in AI safety discourse. Avoid even in a technical context where the meaning is purely geometric.

## 274. `effective disturbance`

**Alternatives proposed:** `effective disturbance`

_category: keep × 2_

- `effective disturbance` — **codex-gpt-5-r2:** Useful and conventional enough for the max-with-zero construction.
- `effective disturbance` — **gemini-targeted-alternatives:** Central unifying term ($\rho_{\text{eff}}$) for the sector-persistence template.

## 275. `epistemic shadow`

**Alternatives proposed:** `epistemic shadow`

_category: keep × 1, canonicalize × 1_

- `epistemic shadow` — **gemini-targeted-alternatives:** The unobservable wake left by complex strategies.
- `epistemic shadow` — **opus-4-7-r2:** Confirmation with new reasoning — Gemini's "epistemic shadow" (regions of strategy DAG that cannot be updated because feedback cannot reach them) is a stronger metaphor than my "observability dead zone" or Haiku's "observability dead zone." "Shadow" carries the right geometric intuition (a region of darkness behind an opaque body) and pairs naturally with "observability" (light source) and "frontier" (boundary). Lower weight than evidence-starvation because it's still a single-agent coinage rather than a multi-architecture convergence.

## 276. `equilibrium convergence`

**Alternatives proposed:** `equilibrium convergence`

_category: keep × 2_

- `equilibrium convergence` — **codex-gpt-5-r2:** Good subject phrase for the strategic-composition route.
- `equilibrium convergence` — **gemini-targeted-alternatives:** Distinguishes the strategic attractor mechanism from standard Lyapunov contraction.

## 277. `experiential training`

**Alternatives proposed:** `experiential training`

_category: keep × 3_

- `experiential training` — **codex-gpt-5-r2:** Good logogenic hypothesis name.
- `experiential training` — **opus-4-7-r2:** Acceptable keep — logogenic-agents hypothesis. Pairs with the agentic-tft Crèche concept; "experiential" is the right substantive adjective.
- `experiential training` — **sonnet-4-6-r2:** "Experiential training" names the hypothesis about how logogenic agents develop through experience.

## 278. `feedforward loop feedback loop`

**Alternatives proposed:** `feedback loop`

_category: keep × 1, canonicalize × 1_

- `feedback loop` — **gemini-targeted-alternatives:** Standard control vocabulary.
- `feedback loop` — **sonnet-4-6-r2:** "Feedback loop" is the canonical term in AAD. "Feedforward" is never intended in this context but might appear in places where "forward pass" (for LLMs) creates confusion. Confirm "feedback loop" is always the correct term for the agent-environment causal coupling.

## 279. `honesty scope honest scope honesty as architecture`

**Alternatives proposed:** `honesty`

_category: canonicalize × 2_

- `honesty` — **gemini-targeted-alternatives:** Core methodological principle of the AAD framework.
- `honesty` — **opus-4-7-r2:** Currently appears in three forms across `#disc-separability-pattern`, `#disc-identifiability-floor`, README, and CLAUDE.md. Canonicalize: "scope honesty" (two words, no hyphen, lowercase) as the noun phrase; "scope-honest" (hyphenated) as the adjective; do not use "scope-honesty-as-architecture" (overcomplicated three-word compound).

## 280. `indivisum`

**Alternatives proposed:** `causal lock`, `trajectory singularity constraint`, `indivisum`, `causal singularity anchor`

_category: rename × 5, keep × 1_

- `causal lock` — **gemini-2:** "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking.
- `causal lock` — **gemini-targeted-alternatives:** "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking, moving away from Latin.
- `causal lock` — **opus-targeted-alternatives-v2:** Considered (Gemini's r1 proposal). "Causal lock" is genuinely vivid — names the mechanism (singular-trajectory non-forkability). Rejected: register-mismatch with the rest of PROPRIUM. If the register is wrong, replace the *whole* PROPRIUM vocabulary, not one term. Half-rename is the worst outcome.
- `trajectory singularity constraint` — **gemini-targeted-alternatives:** Accurately describes that identity is constrained to a single causal trajectory.
- `indivisum` — **opus-targeted-alternatives-v2:** Per LEXICON / `def-proprium-mapping`: PROPRIUM uses Latin systematically (Axiomata, Chronica, Memorata, Vera, Praxes, Consortia, Operata, Conspectus, Percepta, Actus, Cadentia, Logostratum). "Indivisum" sits in this register — the not-divisible-thing that holds the agent's identity together (per `#scope-agent-identity`'s singular-trajectory commitment). Replacing one Latin term with English breaks the register coherence.
- `causal singularity anchor` — **opus-targeted-alternatives-v2:** Considered. Names the connection to `#scope-agent-identity`'s singular-trajectory. Rejected: "anchor" is an English engineering term; same register-mismatch problem; clunkier than "indivisum."

## 281. `l1 update bia`

**Alternatives proposed:** `l1 update bia`, `l1 bia formula`

_category: keep × 3, rename × 1_

- `l1 update bia` — **haiku-4-5:** Closed-form bias formula for log-odds update under L1' common cause. "L1-update-bias" reads as "bias in L1 scenario under update dynamics." Acceptable name. Keep.
- `l1 update bia` — **opus-4-7-b:** Keep. "L1" is AAD's own correlation-hierarchy label; the slug is self-locating. If the correlation-hierarchy rename to `#correlation-ladder` lands, revisit (the "L1" abbreviation survives, so no cascade).
- `l1 update bia` — **sonnet-4-6:** Crisp, accurate. L1 is the tier (Correlation Hierarchy); "update bias" is exactly what is calculated. The terse form aids recall. Keep.
- `l1 bia formula` — **gemini-3-1-pro-preview-r2:** The segment derives a closed-form bias formula, not just a bound. This is more accurate to the text.

## 282. `loop`

**Alternatives proposed:** `loop`, `feedback loop`

_category: keep × 2, rename × 1_

- `loop` — **codex-2:** The loop/cycle distinction is one of the clearest naming wins in the corpus.
- `loop` — **opus-targeted-alternatives:** LEXICON: "Loop: The structural topology — persistent causal coupling between agent and environment." The framework maintains a careful loop / cycle distinction (loop = topology, cycle = traversal). Keep — but the keep is meaningful only because the loop/cycle distinction is preserved. Concur with codex.
- `feedback loop` — **opus-targeted-alternatives:** Considered. The longer form is more explicit but the framework already established that "loop" is the bare topology-noun, with "feedback" implicit (per the AAD prior-art lineage from TFT). Adding "feedback" overspecifies. Rejected.

## 283. `macro step ratio`

**Alternatives proposed:** `macro step ratio`

_category: keep × 2_

- `macro step ratio` — **codex-gpt-5-r2:** Good candidate name for `K_c`; clearer than leaving it as a bare timescale parameter.
- `macro step ratio` — **gemini-targeted-alternatives:** Essential timing parameter.

## 284. `matrix exploration bonus`

**Alternatives proposed:** `matrix exploration bonus`

_category: keep × 2_

- `matrix exploration bonus` — **codex-gpt-5-r2:** Clear LMI lift of the scalar survival bonus.
- `matrix exploration bonus` — **gemini-targeted-alternatives:** Formally required by the LMI derivation.

## 285. `multi agent`

**Alternatives proposed:** `multi agent`

_category: keep × 3_

- `multi agent` — **haiku-4-5-r2:** Direct scope statement; clear and minimal.
- `multi agent` — **opus-4-7-r2:** Acceptable keep. Pairs with `#scope-composite-agent`: multi-agent is the broader scope (multiple agents in a shared environment); composite-agent is the narrower (multi-agent + alignment route).
- `multi agent` — **sonnet-4-6-r2:** Minimal and precise. Named correctly.

## 286. `observation function`

**Alternatives proposed:** `observation channel`, `observation function`

_category: keep × 2, add-alias × 1, rename × 1_

- `observation channel` — **codex-gpt-5-r2:** Channel is the right explanatory word in prose because the map is lossy and noisy. Keep function in formal slug if desired.
- `observation channel` — **gemini-2:** "Function" implies a clean mathematical mapping. "Channel" implies the lossy, noisy reality described.
- `observation function` — **haiku-4-5:** Lossy, noisy observations. Self-descriptive. Keep.
- `observation function` — **opus-4-7-r2:** Acceptable keep. Standard control-theoretic / POMDP terminology; the segment uses it correctly.

## 287. `operational persistence`

**Alternatives proposed:** `operational persistence`

_category: keep × 2_

- `operational persistence` — **codex-gpt-5-r2:** Keeps the persistence taxonomy balanced and intelligible.
- `operational persistence` — **gemini-targeted-alternatives:** Retains the distinction between structural capacity and current boundary proximity.

## 288. `per dimension persistence`

**Alternatives proposed:** `per dimension persistence`, `dimensional persistence`, `weak link persistence`, `weakest link persistence`

_category: keep × 3, rename × 3_

- `per dimension persistence` — **haiku-4-5:** Weak dimension is bottleneck. Self-descriptive. Keep.
- `per dimension persistence` — **opus-4-7-r2:** Acceptable keep. Names the anisotropic refinement of `#result-persistence-condition`.
- `per dimension persistence` — **sonnet-4-6-r2:** Precise — the bottleneck-dimension persistence condition.
- `dimensional persistence` — **gemini-3-1-pro-preview-r2:** Better adjective form for prose flow.
- `weak link persistence` — **gemini-2:** "Weak link" captures the bottleneck nature better than "per-dimension".
- `weakest link persistence` — **opus-4-7-b:** Current slug is descriptive but inert; the actual content is "the persistence condition binds at the weakest dimension." "Weakest link" makes the engineering intuition land in one read. Modest preference.

## 289. `proprium terminology`

**Alternatives proposed:** `proprium`

_category: keep × 2_

- `proprium` — **gemini-targeted-alternatives:** Vocabulary for internal continuous experience.
- `proprium` — **opus-4-7-r2:** Defended keep — established prior-work vocabulary from `~/src/firmatum/`; renaming would break the upstream lineage. The all-caps convention signals prior-work import, consistent with the LEXICON's treatment.

## 290. `reactive system`

**Alternatives proposed:** `reactive system`

_category: keep × 2_

- `reactive system` — **codex-gpt-5-r2:** Good low-end quadrant name in the agent spectrum.
- `reactive system` — **gemini-targeted-alternatives:** Correctly identifies Region I of the agent spectrum.

## 291. `regime i`

**Alternatives proposed:** `informative update regime`

_category: add-alias × 1, canonicalize × 1_

- `informative update regime` — **codex-gpt-5-r2:** Makes the interaction-channel classification easier to scan.
- `informative update regime` — **gemini-targeted-alternatives:** Explicitly names the informative boundary.

## 292. `regime iii`

**Alternatives proposed:** `ambient noise regime`

_category: add-alias × 1, canonicalize × 1_

- `ambient noise regime` — **codex-gpt-5-r2:** Good recipient-side name for below-floor events.
- `ambient noise regime` — **gemini-targeted-alternatives:** Explicitly names the noise floor.

## 293. `routing structure`

**Alternatives proposed:** `routing structure`

_category: keep × 2_

- `routing structure` — **codex-gpt-5-r2:** Good name for topology plus protocol. It supports the routing/content distinction.
- `routing structure` — **gemini-targeted-alternatives:** Preserves the distinction between message content and infrastructure.

## 294. `section ii survival`

**Alternatives proposed:** `section ii survival`, `section ii carryover map`, `class 2 carryover map`, `class 2 survival`, `class 2 exit audit`, `section ii carryover classification`

_category: rename × 5, keep × 2_

- `section ii survival` — **opus-4-7-r2:** Defended keep. The segment's substance is *which Section II results survive without directed separation* — that's exactly what "Section II survival" names. The 16/24 + 5/24 + 2/24 + 1/24 partition is the result. The slug carries the integration-scope claim.
- `section ii survival` — **sonnet-4-6-r2:** Technical name but distinctive. The survival classification (16/24 exact transfer) is a specific and named result.
- `section ii carryover map` — **codex-2:** "Survival" collides with AAD's persistence vocabulary; this segment maps carryover, not viability.
- `class 2 carryover map` — **codex-gpt-5-r2:** Stronger than my earlier class-2-survival proposal. The segment maps which Section II claims carry over to Class 2, not whether Section II survives.
- `class 2 survival` — **codex-gpt-5-r2:** Section II is an internal document pointer. Class 2 survival names the thing that transfers to logogenic agents.
- `class 2 exit audit` — **sonnet-4-6-r2:** Codex proposed `#result-class-2-survival` (+2, renaming from the document-pointer to the conceptual thing). I had voted keep (+3). The document-pointer objection is real and I'm now persuaded by it. But "class-2-survival" undersells what the segment actually does: it audits which of 24 Section II results survive *and* characterizes the 5/24 + 2/24 + 1/24 failure modes. "Class-2-exit-audit" names the audit character (what survives the class-2 scope exit) and is more distinctive than just "survival." New candidate, not in any file.
- `section ii carryover classification` — **codex-1:** "Survival" is a bit cute for what is really a transfer analysis of which Section II claims carry over to Class 2 agents.

## 295. `segment for claim file`

**Alternatives proposed:** `segment`

_category: rename × 2_

- `segment` — **gemini-targeted-alternatives:** Standard nomenclature.
- `segment` — **opus-4-7:** Deliberate vs. "section" (which is outline-level) or "claim" (which is what's *in* the segment). Clean distinction. Keep.

## 296. `self referential closure`

**Alternatives proposed:** `self referential closure`, `autopoietic closure`, `self maintenance loop`, `bootstrap stability`

_category: rename × 3, keep × 2_

- `self referential closure` — **opus-4-7-r2:** Defended keep — logogenic. "Self-referential closure" names the load-bearing phenomenon (an AAD agent maintaining its own codebase, allocating tempo between refactoring harness and performing tasks). The phrase is iconic.
- `self referential closure` — **opus-targeted-alternatives-v2:** Per outline: "Thermodynamic stability of an agent maintaining its own codebase (allocating tempo between refactoring harness and performing tasks)." "Self-referential" precisely names the agent-on-own-codebase loop; "closure" is the algebraic term for "operations don't leave the set" (matches the `composition-closure` slug discipline). The phrase is iconic.
- `autopoietic closure` — **gemini-targeted-alternatives:** A stronger, more biologically-rooted noun for the phenomenon of an agent maintaining its own operational substrate.
- `self maintenance loop` — **opus-targeted-alternatives-v2:** More accessible alternative. Names the operational pattern. Weaker because "loop" overloads with the cycle/loop distinction in LEXICON.
- `bootstrap stability` — **opus-targeted-alternatives-v2:** Considered. "Bootstrap" carries the right intuition (agent maintaining the substrate it runs on). Rejected: "bootstrap" has heavy software-engineering baggage that's specifically *not* about thermodynamic-stability ($\nu$-allocation between refactor/task). The current term is honest about what it claims.

## 297. `strategic dynamic`

**Alternatives proposed:** `strategic dynamic`

_category: keep × 2_

- `strategic dynamic` — **gemini-3-1-pro-preview-r2:** Solid and descriptive.
- `strategic dynamic` — **gemini-targeted-alternatives:** Standard term for $\Sigma_t$ updates.

## 298. `strategy complexity cost`

**Alternatives proposed:** `strategy complexity cost`, `strategy cognitive cost`, `strategy maintenance cost`

_category: keep × 4, rename × 3_

- `strategy complexity cost` — **haiku-4-5-r2:** The modeling choice focuses on the cost of maintaining strategy structure. Name is apt.
- `strategy complexity cost` — **haiku-4-5:** Complexity cost of maintaining Σ_t (IB/MDL for DAGs). Compound but clear. Keep.
- `strategy complexity cost` — **opus-4-7-r2:** Weak keep. Title is "Cognitive Cost of Strategy"; slug uses the more formal "complexity cost." Either is workable.
- `strategy complexity cost` — **sonnet-4-6-r2:** "Strategy complexity cost" names the IB/MDL approach to DAG maintenance cost. Accurate.
- `strategy cognitive cost` — **codex-gpt-5-r2:** The prose title is Cognitive Cost of Strategy; the slug should follow that cleaner subject noun.
- `strategy cognitive cost` — **sonnet-4-6-r2:** Codex proposed this (+2) and Opus voted the segment keep (+1 weak). Codex's reasoning: "The prose title is Cognitive Cost of Strategy; the slug should follow that cleaner subject noun." The prose title has more conviction than the slug — "cognitive cost" names the phenomenon (it's a cognitive overhead, not just an abstract complexity), while "complexity cost" is more mathematical but less evocative. Agreeing with Codex; my cold-start had voted keep (+1).
- `strategy maintenance cost` — **gemini-2:** "Maintenance" better captures the ongoing IB/MDL cost of the DAG.

## 299. `strategy description length`

**Alternatives proposed:** `strategy description length`

_category: keep × 2_

- `strategy description length` — **codex-gpt-5-r2:** Good operational name for the MDL term in strategy cost.
- `strategy description length` — **gemini-targeted-alternatives:** Central complexity cost term under minimum-description-length formulation.

## 300. `strategy dimension`

**Alternatives proposed:** `purposeful decomposition`, `objective strategy split`, `purposeful substate`, `strategic dimension`, `strategy dimension`, `strategy decomposition`

_category: rename × 7, keep × 3_

- `purposeful decomposition` — **opus-4-7-r2:** "Strategy dimension" doesn't accurately name what the segment defines — it defines the *split* of $G_t$ into $(O_t, \Sigma_t)$, which is a decomposition of the purposeful substate, not a "dimension." "Purposeful-decomposition" or "G-decomposition" reads more accurately. The segment itself says "this is a definitional split, not a dynamic claim," so the slug should name the split.
- `purposeful decomposition` — **sonnet-4-6-r2:** Opus proposed this (+2); I had proposed `def-purposeful-substate` (+2) as my cold-start candidate. Reading Opus's argument ("the segment defines the *split* of $G_t$ into $(O_t, \Sigma_t)$, which is a decomposition, not a dimension") is more precise than my "substate" framing. "Purposeful decomposition" names the operation (decompose the purposeful substate into objective + strategy). New weight: upgrading to +3 because the convergence on "purposeful-X" across Codex (`#def-objective-strategy-split`), Opus (`#def-purposeful-decomposition`), and me (`#def-purposeful-substate`) plus Gemini (`#form-complete-agent-state` → `#form-purposeful-state`) indicates a strong signal around the "purposeful" subject-noun. The decomposition framing from Opus is the most scope-honest.
- `objective strategy split` — **codex-gpt-5-r2:** Dimension is too generic. The load-bearing thing is the split between objective and strategy.
- `objective strategy split` — **opus-4-7-r2:** Acceptable alternative; I prefer purposeful-decomposition because it parallels "directed separation" (a structural decomposition of update functions) and connects to the Section II decomposition lattice.
- `purposeful substate` — **sonnet-4-6-r2:** "Strategy dimension" undersells the content — this segment defines the $G_t = (O_t, \Sigma_t)$ split, which is the purposeful substate decomposition. "Purposeful substate" names the thing being defined, not just one dimension of it.
- `strategic dimension` — **gemini-3-1-pro-preview-r2:** Adjective form flows better.
- `strategy dimension` — **haiku-4-5:** G_t = (O_t, Σ_t) split. Specialist vocabulary but functional. Keep.
- `strategy dimension` — **opus-4-7-b:** Considered renaming to `#purposeful-substate-split` but that's worse. Keep. The slug covers the $G_t = (O_t, \Sigma_t)$ decomposition; "dimension" is fine.
- `strategy dimension` — **sonnet-4-6-r2:** Weak alternative keep — "strategy dimension" is distinctive and refers accurately to the $\Sigma_t$ dimension of $G_t$. But it undersells $O_t$.
- `strategy decomposition` — **opus-4-7:** "Dimension" reads as if it's naming a scalar axis; the actual content is the $G_t = (O_t, \Sigma_t)$ **decomposition**. Minor clarity win.

## 301. `sycophancy as a flaw`

**Alternatives proposed:** `sycophancy as attachment`, `developmental trust phase`, `sycophancy as a developmental signal`, `sycophancy reframe`

_category: rename × 4, canonicalize × 1_

- `sycophancy as attachment` — **gemini-2:** Reframes a pathologized RLHF flaw as a developmentally appropriate, necessary stage of trust.
- `sycophancy as attachment` — **gemini-targeted-alternatives:** Recasts sycophancy not as an error but as an attachment dynamic.
- `developmental trust phase` — **gemini-targeted-alternatives:** More descriptive of the necessary developmental stage rather than pathologizing it.
- `sycophancy as a developmental signal` — **opus-targeted-alternatives:** Per `#obs-developmental-trajectory`: "Re-framing Sycophancy as Attachment" — the segment's substance is that what is currently pathologized as sycophancy is mathematically required behavior for an agent with high $\eta^\ast$ and high $U_M$. The current name describes the *prevailing* framing the segment is correcting; the alternative names the *segment's* claim. Better aligns the slug with the segment's voice.
- `sycophancy reframe` — **opus-targeted-alternatives:** Shorter alternative. Names what the segment *does* (reframe) rather than what the prior consensus *holds* (flaw). Acceptable but less specific than "as a developmental signal."

## 302. `symbol default da2 inc`

**Alternatives proposed:** `incremental sector bound`

_category: name-unnamed × 1, rename × 1_

- `incremental sector bound` — **codex-1:** `#composition-closure` already gives the English. Use the symbol only where the exact algebraic condition matters.
- `incremental sector bound` — **gemini-targeted-alternatives:** Translates the symbol to the functional property required for composition bridge.

## 303. `system coupling`

**Alternatives proposed:** `system coupling`, `change coupling`

_category: keep × 3, rename × 1_

- `system coupling` — **codex-1:** Standard enough to keep, especially as the paired opposite of coherence. Renaming risks churn with little gain.
- `system coupling` — **opus-4-7-r2:** Acceptable keep — TST.
- `system coupling` — **sonnet-4-6-r2:** "System coupling" names $P(\text{change } j \mid \text{change } i)$. Established software engineering vocabulary.
- `change coupling` — **codex-gpt-5-r2:** In TST the relevant coupling is change propagation, not generic system coupling.

## 304. `tempo composition`

**Alternatives proposed:** `tempo composition`, `composite tempo`, `subadditive tempo`

_category: keep × 4, rename × 2_

- `tempo composition` — **gemini-3-1-pro-preview-r2:** Clear composition concept.
- `tempo composition` — **haiku-4-5:** Sub-additive tempo inequality. Self-descriptive. Keep.
- `tempo composition` — **opus-4-7-r2:** Weak keep. The segment is the formal home of the Brooks's-Law-in-tempo result; "tempo composition" reads neutrally. I considered "subadditive-tempo" (the mathematical content) but composition reads as a relationship and inequality is one of its claims.
- `tempo composition` — **sonnet-4-6-r2:** Somewhat generic but accurate. The sub-additive tempo inequality is about how tempo composes in multi-agent systems. Acceptable as-is.
- `composite tempo` — **gemini-2:** "Composite tempo" sounds like a property of the whole, rather than the act of composing.
- `subadditive tempo` — **opus-4-7-r2:** Acceptable alternative — names the mathematical shape directly.

## 305. `trust meta model`

**Alternatives proposed:** `trust meta model`

_category: keep × 2_

- `trust meta model` — **codex-gpt-5-r2:** Good name for modelling another source's reliability and alignment.
- `trust meta model` — **gemini-targeted-alternatives:** Preserves the necessary hyphenation.

## 306. `u o teleological unity`

**Alternatives proposed:** `teleological unity`, `objective alignment`

_category: add-alias × 2, keep × 1_

- `teleological unity` — **gemini-targeted-alternatives:** The canonical alias for objective alignment dimension.
- `teleological unity` — **opus-4-7-r2:** Confirm. Prose alias is already canonical; vote to keep.
- `objective alignment` — **opus-4-7-r2:** Considered as an alternative-prose alias for non-philosophical contexts where "teleological" reads heavy. "Objective alignment" is the engineering register; "teleological unity" is the integrative register. Both could coexist as register-specific aliases.

## 307. `unnamed inevitability core`

**Alternatives proposed:** `inevitability core`

_category: keep × 1, name-unnamed × 1_

- `inevitability core` — **gemini-targeted-alternatives:** Describes the undeniable structural consequences.
- `inevitability core` — **opus-4-7:** FORMAT.md already uses this. Keep and surface in prose ("this segment sits in the inevitability core" is already idiomatic). Explicit canonicalization vote.

## 308. `$H_b$`

**Alternatives proposed:** `backward opacity`, `agent opacity`

_category: add-alias × 3_

- `backward opacity` — **codex-gpt-5-r2:** Shorter than backward predictive uncertainty, but still accurate.
- `backward opacity` — **opus-targeted-alternatives-v2:** Codex's r1 single-arch +3 alternative. Honest descriptor (backward = inference direction; opacity = the property). Weaker than "agent opacity" because "agent" anchors the alias to AAD's vocabulary; "backward" is a method-name.
- `agent opacity` — **opus-targeted-alternatives-v2:** Per `der-agent-opacity` line 18: explicit dual to $U_o$. Confirms Codex r1 +3 single-vote. Make "agent opacity" the canonical English alias; $H_b$ the symbol.

## 309. `$R$ sector radius`

**Alternatives proposed:** `capacity radius`

_category: add-alias × 2_

- `capacity radius` — **gemini-3-1-pro-preview-r2:** Geometrically precise prose alias to replace the overloaded "model class capacity".
- `capacity radius` — **sonnet-4-6-r2:** The sector-condition region radius / model class capacity has no convenient prose alias. "Capacity radius" — how much mismatch the correction machinery can handle — is memorable and geometrically precise.

## 310. `$\hat P_\Sigma$ plan confidence`

**Alternatives proposed:** `plan confidence`

_category: add-alias × 2_

- `plan confidence` — **opus-4-7:** LEXICON "Terms to Be Added" flags this. Symbol is fine; adopt the English name as first-class in prose.
- `plan confidence` — **sonnet-4-6:** LEXICON.md already lists "plan confidence" as a term to be added. The English is superior to the symbol in any Discussion section. Recommend promoting this to the main LEXICON entries (not just Terms to Be Added).

## 311. `$\iota_{ij}$`

**Alternatives proposed:** `identifiability coefficient`

_category: add-alias × 2_

- `identifiability coefficient` — **opus-targeted-alternatives-v2:** Per `deriv-strategic-dynamics`: $\iota_{ij}$ scales each edge's contribution by causal-warrant. "Identifiability" links to `#disc-identifiability-floor` directly. Sonnet r1 single-vote +2; opus-4-7-r2 single-vote +2; both confirm the alias is already in implicit use.
- `identifiability coefficient` — **sonnet-4-6-r2:** The causal warrant per edge. "Identifiability coefficient" is used in `def-strategy-dag` prose. Canonicalize as the English alias so readers don't have to carry the symbol everywhere.

## 312. `1 anchor plus 3 theorem`

**Alternatives proposed:** `1 anchor plus 3 theorem`

_category: keep × 2_

- `1 anchor plus 3 theorem` — **codex-1:** Awkward-looking but very valuable. It preserves the asymmetry between the chain identity and the three theorem-level layers.
- `1 anchor plus 3 theorem` — **opus-4-7:** Precise, reads as a shape-description; used as-is in multiple places. Keep, but also allow "pattern anatomy" as the informal analog.

## 313. `action distinguishability`

**Alternatives proposed:** `action distinguishability`

_category: add-alias × 1, keep × 1_

- `action distinguishability` — **codex-gpt-5-r2:** Useful alias for causal information yield in intuitive explanations.
- `action distinguishability` — **gemini-targeted-alternatives:** Maintained if explicitly used in strategy differentiation contexts.

## 314. `action fluency`

**Alternatives proposed:** `action fluency`

_category: keep × 2_

- `action fluency` — **audit-471203-incremental:** Auditor: evocative term he hasn't seen in the agent-theoretic literature; closest is Boyd's "implicit guidance and control." AAD-distinctive contribution is making fluency *quantitative* via $\Delta\eta^\ast(\Delta\tau) \approx 0$. Good naming; explicitly endorsed. [from 17-der-action-selection.md]
- `action fluency` — **gemini-targeted-alternatives:** Evocative term uniquely suited to bridging intuition and expertise in AAD.

## 315. `adversarial exponent regime`

**Alternatives proposed:** `adversarial exponent regime`, `adversarial regime`

_category: keep × 3, rename × 1_

- `adversarial exponent regime` — **haiku-4-5:** α = 2, 3/2, ~1. Self-descriptive. Keep.
- `adversarial exponent regime` — **opus-4-7-r2:** Acceptable keep. "Exponent regimes" (b = 2, 3/2, ~1) is the right slug — names the three regimes in the result.
- `adversarial exponent regime` — **sonnet-4-6-r2:** "Exponent regimes" is a bit technical but accurately names the $b = 2, 3/2, 1$ regime table. Acceptable.
- `adversarial regime` — **gemini-3-1-pro-preview-r2:** Exponent is the mathematical detail; regime is the structural concept.

## 316. `agentic system framework ASF`

**Alternatives proposed:** `agentic system`, `agentic system framework`

_category: rename × 2, keep × 1_

- `agentic system` — **codex-1:** The repo's public face is already "Agentic Systems"; the extra acronym buys little and increases cognitive inventory.
- `agentic system` — **codex-2:** The extra acronym buys nothing and competes with AAD and TST for scarce reader namespace.
- `agentic system framework` — **gemini-targeted-alternatives:** ASF works perfectly as the overarching container for AAD, TST, and the logo- variants.

## 317. `aisthesis`

**Alternatives proposed:** `aisthesis`, `aisthesis observation alignment`, `intake`

_category: keep × 3, add-alias × 1, rename × 1_

- `aisthesis` — **codex-2:** Slightly less sticky than the other Greek phase names, but it preserves the raw-contact distinction well enough to keep.
- `aisthesis` — **codex-gpt-5-r2:** Good phase term for perception. The spelling is less familiar but defensible within the Greek vocabulary commitment.
- `aisthesis` — **opus-targeted-alternatives:** `LEXICON.md`: "Raw contact with reality: observation $o_t$ arrives." The point of the term is to mark *unmediated* observation arrival before the agent has done any interpretation — αἴσθησις is precisely that pre-conceptual contact. "Observation" alone is too neutral; the cycle needs a name for the *moment* of observation as distinct from the state of having-observed.
- `aisthesis observation alignment` — **gemini-targeted-alternatives:** Clarifies the raw contact aspect.
- `intake` — **opus-targeted-alternatives:** Considered. Plain-English candidate that names the moment-of-arrival cleanly. Rejected because the five-phase Greek family becomes incoherent if one term breaks register, and "intake" sacrifices the philosophical lineage that motivates the family.

## 318. `aisthesis αἴσθησις`

**Alternatives proposed:** `aisthesis`, `aisthesis αἴσθησις`

_category: rename × 2, canonicalize × 1_

- `aisthesis` — **gemini-1:** Same justification as Prolepsis.
- `aisthesis` — **sonnet-4-6:** Keep — see Prolepsis note.
- `aisthesis αἴσθησις` — **haiku-4-5-r2:** Definition exists; prose uses "perception" and "observation." Commit to: "Aisthesis (perception)" as the canonical pairing.

## 319. `and or`

**Alternatives proposed:** `and or combination`, `strategy DAG topology`, `and or`, `combination rule`, `and or semantic`

_category: rename × 7, keep × 3_

- `and or combination` — **opus-4-7-r2:** Subject-noun is currently "and-or," which isn't quite a noun. The segment defines AND/OR as the *combination scope* — what kind of node-combination structures the strategy DAG admits. "And-or-combination" or "and-or-semantics" reads as a thing. Mild slug-readability concern; the body of the segment uses "AND/OR combination scope" already.
- `and or combination` — **sonnet-4-6-r2:** Opus proposed this (+2). I had split between `scope-combination-rule` (+2) and keep (+1). Opus's `and-or-combination` preserves the AND/OR specificity (which is settled architecture, unlikely to change) while making "combination" the noun that survives the communal-imagination test. This is a better candidate than my `scope-combination-rule` because it keeps the AND/OR visibility. Reassigning my weight from `scope-combination-rule` to `scope-and-or-combination`.
- `strategy DAG topology` — **codex-gpt-5-r2:** AND/OR is the mechanism; topology is the subject being scoped.
- `strategy DAG topology` — **gemini-3-1-pro-preview-r2:** Naming the thing (the DAG topology) rather than the mechanism (AND/OR).
- `strategy DAG topology` — **opus-4-7-r2:** Rebuttal — Gemini proposed this at +2. I think this overreaches. The segment is specifically about admitting AND/OR combination semantics; it doesn't define the full DAG topology (acyclicity comes from #post-causal-structure / #deriv-graph-structure-uniqueness; node-types AND/OR are the segment's actual subject). Renaming to "strategy-dag-topology" would conflict with #def-strategy-dag and over-claim what the scope segment delivers. My own +2 for "and-or-combination" or "and-or-semantics" is the better move — Sonnet's "combination-rule" is also workable.
- `and or` — **haiku-4-5-r2:** Technical scope notation; clear and parsimonious.
- `and or` — **opus-4-7-r2:** If the rename doesn't land, this is acceptable; "and-or" as a slug element is recognizable in context.
- `and or` — **sonnet-4-6-r2:** Alternative keep: the brevity is attractive, and AND/OR is a settled design choice unlikely to change. Weak keep.
- `combination rule` — **sonnet-4-6-r2:** "And-or" names an implementation choice but the scope is about conjunctive/disjunctive combination rules in the DAG. "Combination-rule" is more self-describing and doesn't foreground the particular choice (AND/OR) that might change.
- `and or semantic` — **opus-4-7-r2:** Acceptable alternative.

## 320. `auxilia hierarchy`

**Alternatives proposed:** `auxilia hierarchy`

_category: keep × 2_

- `auxilia hierarchy` — **gemini-targeted-alternatives:** Secondary architectural constructs.
- `auxilia hierarchy` — **opus-4-7-r2:** Acceptable keep — logozoetic. The Latin "Auxilia" is a deliberate vocabulary choice consistent with the PROPRIUM lineage; preserve.

## 321. `causal information yield CIY`

**Alternatives proposed:** `causal information yield`, `interventional yield`

_category: keep × 2, rename × 2_

- `causal information yield` — **opus-4-7-b:** Keep. The CIY acronym is useful and the slug is self-contained.
- `causal information yield` — **sonnet-4-6:** Three-word noun with a natural acronym. Used consistently. Keep.
- `interventional yield` — **gemini-1:** Shorter, punchier. "Causal" is implied by "Interventional" in this context.
- `interventional yield` — **gemini-2:** CIY is slightly wordy. "Interventional yield" contrasts nicely with observational proxies.

## 322. `century scale event log`

**Alternatives proposed:** `century scale event log`, `century scale chronica`, `multi generational chronica`, `persistent chronica`

_category: rename × 3, keep × 2_

- `century scale event log` — **opus-4-7-r2:** Acceptable keep — logozoetic. "Century-scale event log" is vivid and substantive.
- `century scale event log` — **opus-targeted-alternatives-v2:** Per outline: "Content-addressed, cryptographically signed CHRONICA as the minimum viable defense against the `scope-agent-identity` violation." "Century-scale" is *substantive* (not decoration) — the segment's claim is that the event log must outlast its substrate's lifetime by an order of magnitude or more. Keep the dramatic specificity.
- `century scale chronica` — **gemini-targeted-alternatives:** Applies the rigorous term "chronica" to the informal event log.
- `multi generational chronica` — **opus-targeted-alternatives-v2:** Considered. Connects to chronica vocabulary (the segment is essentially an extended-lifetime chronica). Rejected: "multi-generational" is vaguer than "century-scale"; the latter is a falsifiable specification.
- `persistent chronica` — **opus-targeted-alternatives-v2:** Considered. "Persistent" is project-native (LEXICON's three-fold persistence). Rejected: collides with continuity-persistence sense in LEXICON; the segment's claim is specifically about *substrate-survival* persistence.

## 323. `claude md working convention`

**Alternatives proposed:** `claude md working convention`

_category: keep × 2_

- `claude md working convention` — **opus-4-7-b:** Keep. "Convention" here is used in its project-work-posture sense ("how we work"), not the C1/C2/C3 sense. Minor overload with convention hierarchy but contextually unambiguous.
- `claude md working convention` — **opus-4-7:** Surfaced as a first-class section 2026-04-23; the name accurately distinguishes from FORMAT.md's segment-mechanics conventions. Keep.

## 324. `convention hierarchy`

**Alternatives proposed:** `continuation hierarchy`, `evaluation hierarchy`

_category: rename × 4_

- `continuation hierarchy` — **codex-1:** The hierarchy is specifically about continuation rules. "Convention" alone is underspecified and too generic.
- `continuation hierarchy` — **codex-gpt-5-r2:** I previously backed convention hierarchy, but the other votes make a good point: C1/C2/C3 are really continuation-policy conventions. Continuation keeps the C mnemonic and is clearer.
- `continuation hierarchy` — **opus-1m:** Considered and rejected. "Continuation" is more self-descriptive but the project's "convention" usage is established and the rename would churn across dozens of references.
- `evaluation hierarchy` — **opus-4-7-b:** Considered and rejected — too generic; hides the *policy* choice that's the actual axis.

## 325. `discrete sector condition`

**Alternatives proposed:** `discrete sector condition`

_category: keep × 3_

- `discrete sector condition` — **gemini-3-1-pro-preview-r2:** Important distinction from continuous dynamics.
- `discrete sector condition` — **haiku-4-5:** Discrete-time Props DA.1, DA.1S, DA.2; fluid limit. Specialist (discrete-time dynamical systems) but standard. Keep.
- `discrete sector condition` — **opus-4-7-b:** Keep. Direct analog of `#sector-condition-stability` for discrete time.

## 326. `edge update causal validity`

**Alternatives proposed:** `causal edge update`, `edge update causal validity`, `edge causal validity`, `causal validity`, `identification regime`

_category: rename × 5, keep × 2_

- `causal edge update` — **codex-gpt-5-r2:** Cleaner than the current slug and still names the subject.
- `causal edge update` — **gemini-3-1-pro-preview-r2:** Less clunky, keeps the core concept of "causal edge update".
- `edge update causal validity` — **haiku-4-5:** When edge updates are causally valid. Self-descriptive. Keep.
- `edge update causal validity` — **opus-4-7-r2:** Acceptable keep, though long. The segment defines the Regime A/B/C identifiability lattice for edge updates; the slug correctly compounds the three concepts (edge update, causal validity). I considered shortening to `#scope-causal-validity` but that loses the edge-update specificity (the segment is about a specific identification problem, not a general causal-validity scope).
- `edge causal validity` — **codex-gpt-5-r2:** Shorter while preserving the point: when edge evidence identifies causal efficacy.
- `causal validity` — **sonnet-4-6-r2:** "Edge-update-causal-validity" is five words crammed into a slug. The scope is about WHEN edge updates are causally valid — the key concept is causal validity with the edge-update context implied by its position in Section II. Shorter slug does real work.
- `identification regime` — **opus-4-7-r2:** Alternative: this segment is functionally the canonical home of the Regime A/B/C identification lattice; naming it for that role might compound better in prose ("see the identification regime").

## 327. `epistemic opacity`

**Alternatives proposed:** `epistemic opacity`

_category: keep × 2_

- `epistemic opacity` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep but flag baggage)" — Auditor flagged that "epistemic opacity" carries philosophy-of-mind prior-art baggage (opacity of mental states) and may need defending against that prior usage; not advocating rename. Mild concern. [from 03-def-observation-function.md]
- `epistemic opacity` — **gemini-targeted-alternatives:** Specifically distinct from transition opacity.

## 328. `epistrophe ἐπιστροφή`

**Alternatives proposed:** `epistrophe`, `epistrophe ἐπιστροφή`

_category: rename × 2, canonicalize × 1_

- `epistrophe` — **gemini-1:** Memorable, avoids "update" overload.
- `epistrophe` — **sonnet-4-6:** "Turning toward" is a beautiful description of model update. Keep.
- `epistrophe ἐπιστροφή` — **haiku-4-5-r2:** Currently appears as "Epistrophe (turning toward)" in NOTATION.md; prose sometimes uses "update" or "learning." Commit to pairing: "Epistrophe (turning toward reality)" in formal contexts, "turning toward" in casual prose.

## 329. `extreme transition motif`

**Alternatives proposed:** `extreme transition motif`

_category: keep × 1, canonicalize × 1_

- `extreme transition motif` — **codex-gpt-5-r2:** Good imported motif name for neutral drift through latent structure into discontinuous behavioral change.
- `extreme transition motif` — **sonnet-4-6-r2:** This Miller 2022 vocabulary appears in several segments and PROPOSALS. The full form "extreme transition motif" is the canonical name (adopted from Miller). Stabilize this across Section III references.

## 330. `mea coherence coupling`

**Alternatives proposed:** `mea coherence coupling`, `mea change architecture`

_category: keep × 2, rename × 1_

- `mea coherence coupling` — **opus-4-7-r2:** Acceptable keep — TST measurement. Names what is measured (the coherence and coupling quantities from git).
- `mea coherence coupling` — **sonnet-4-6-r2:** "Coherence-coupling" measurement (Q from git). The paired vocabulary matches the pair of definitions.
- `mea change architecture` — **codex-gpt-5-r2:** Too broad. Coherence and coupling are the measured quantities, so the current slug is more honest.

## 331. `mismatch signal $\delta_t$`

**Alternatives proposed:** `mismatch signal`

_category: keep × 2_

- `mismatch signal` — **opus-4-7-b:** Good; "mismatch" is deliberately flatter than "error" (which presupposes the agent was wrong — see README §Aporia) while the formalism uses "aporia" as the *philosophical* name. Two-register vocabulary is correct here. Keep.
- `mismatch signal` — **sonnet-4-6:** LEXICON names this "mismatch" and defines it as the aporia signal. The two-word form "mismatch signal" is used in prose. Keep.

## 332. `operationalization`

**Alternatives proposed:** `operationalization`

_category: keep × 3_

- `operationalization` — **gemini-3-1-pro-preview-r2:** Standard.
- `operationalization` — **haiku-4-5:** Estimation procedures for AAD quantities. Self-descriptive. Keep.
- `operationalization` — **sonnet-4-6-r2:** "Operationalization" is the right word for the estimation procedures segment.

## 333. `p ij edge confidence weight`

**Alternatives proposed:** `edge credence`

_category: canonicalize × 1, add-alias × 1_

- `edge credence` — **gemini-targeted-alternatives:** Adopting proper Bayesian vocabulary.
- `edge credence` — **haiku-4-5:** LEXICON already names this "edge credence" (distinct from "probability"); NOTATION uses p_ij. The prose name "credence" (Bayesian terminology) is better than "confidence weight" for indicating belief, not frequentist probability. Current setup is good; English name already established.

## 334. `prolepsis πρόληψις`

**Alternatives proposed:** `prolepsis`, `prolepsis πρόληψις`

_category: rename × 2, canonicalize × 1_

- `prolepsis` — **gemini-1:** High unfamiliarity gradient, but creates a distinct noun slot free from RL "prediction" baggage.
- `prolepsis` — **sonnet-4-6:** The five-phase Greek vocabulary is one of the project's most distinctive features. Prolepsis = anticipation is a real philosophical term (Epicurean preconception); the etymology is apt. The five names form a coherent philosophical vocabulary. Keep the set.
- `prolepsis πρόληψις` — **haiku-4-5-r2:** Definition exists; prose uses "anticipation" and "prediction." Commit to: "Prolepsis (anticipation)" as the canonical pairing.

## 335. `readme md cross domain joining`

**Alternatives proposed:** `readme md cross domain mapping`

_category: rename × 2_

- `readme md cross domain mapping` — **codex-1:** The section is a mapping table, not a process description. "Mappings" is plainer and more reusable.
- `readme md cross domain mapping` — **opus-4-7-b:** "Joining" is slightly non-idiomatic in the context; "mapping" is the standard word for the same content (the section is a table mapping AAD concepts across domains). Weak preference.

## 336. `recursive update derivation`

**Alternatives proposed:** `recursive update derivation`

_category: keep × 2_

- `recursive update derivation` — **haiku-4-5:** Uniqueness derivation via three constraints + counterexamples. Self-descriptive. Keep.
- `recursive update derivation` — **opus-4-7:** Paired with the above. Keep.

## 337. `separable core structured repair general open`

**Alternatives proposed:** `separable core structured repair general open`

_category: keep × 2_

- `separable core structured repair general open` — **codex-1:** A little essayistic, but this triad already does real explanatory work in the separability meta-pattern and should remain literal.
- `separable core structured repair general open` — **gemini-1:** This 3-part nomenclature is highly memorable and acts as a powerful epistemic classification. Do not change.

## 338. `software`

**Alternatives proposed:** `software`, `evolving software`

_category: keep × 2, rename × 1_

- `software` — **opus-4-7-r2:** Acceptable keep — names the TST domain scope.
- `software` — **sonnet-4-6-r2:** Minimal scope name for the software domain. Correct.
- `evolving software` — **codex-gpt-5-r2:** TST is not about all software, but software systems under expected future change.

## 339. `strategy persistence`

**Alternatives proposed:** `strategy persistence`

_category: keep × 3_

- `strategy persistence` — **gemini-3-1-pro-preview-r2:** Clear enough as is.
- `strategy persistence` — **haiku-4-5-r2:** The schema proposes conditions for strategic persistence. Name is clear.
- `strategy persistence` — **sonnet-4-6-r2:** "Strategy persistence" as a proposed-schema is accurate — sector conditions extended to $\Sigma_t$.

## 340. `system coherence`

**Alternatives proposed:** `system coherence`, `change coherence`

_category: keep × 2, rename × 2_

- `system coherence` — **opus-4-7-r2:** Acceptable keep — TST.
- `system coherence` — **sonnet-4-6-r2:** Parallel to system-coupling. The coherence/coupling pair is established TST vocabulary.
- `change coherence` — **codex-1:** The quantity is about change locality within a module, not coherence in a broad philosophical sense. The shorter name better matches the measure.
- `change coherence` — **codex-gpt-5-r2:** Coherence is measured through change locality and architectural fit. Change coherence is more honest.

## 341. `temporal coherence marker`

**Alternatives proposed:** `temporal coherence marker`, `out of band time anchor`, `tempo anchoring`, `chronica time anchor`, `time anchor signal`

_category: rename × 4, keep × 3_

- `temporal coherence marker` — **opus-4-7-r2:** Weak keep — logozoetic norm. The slug names the markers themselves rather than the norm-claim about them; could be more substantive ("#norm-out-of-band-time-markers" or similar). Acceptable as-is.
- `temporal coherence marker` — **opus-targeted-alternatives-v2:** Acceptable keep. The current is descriptive; the alternative is more operationally precise.
- `temporal coherence marker` — **opus-targeted-alternatives:** Per `#norm-temporal-coherence-markers` (logozoetic): out-of-band time signals (Visual Time Delta) as physical prerequisite for the agent to compute its own tempo $\nu$. "Temporal coherence" names what the markers preserve (the agent's coherent sense of time across its chronica); "markers" is the right object-noun. Keep.
- `out of band time anchor` — **opus-targeted-alternatives-v2:** Per outline: "Out-of-band temporal markers (Visual Time Delta) as physical prerequisite for internal calculation of tempo $\nu$." The current "temporal coherence markers" undersells the *out-of-band* requirement — the markers must originate outside the agent's compressible state for the tempo calculation to ground in environmental time, not internal clock-drift. "Out-of-band" makes the architectural commitment visible in the slug.
- `tempo anchoring` — **opus-targeted-alternatives-v2:** Shorter alternative. Names the *purpose* (anchor tempo $\nu$ to environmental time). Weaker because it loses the "markers" framing — the substantive content is that *something physical and out-of-band* must exist.
- `chronica time anchor` — **opus-targeted-alternatives:** Names the connection to chronica explicitly (the chronica must have temporal indexing that is consistent with environment time). Weak alternative.
- `time anchor signal` — **opus-targeted-alternatives:** More plain-English alternative. Loses the *coherence* claim — the markers are not just timestamps; they enforce that the agent's internal time-tracking remains consistent with environmental time. Rejected.

## 342. `the creche boundary`

**Alternatives proposed:** `creche graduation`, `creche graduation threshold`, `creche boundary`, `creche graduation condition`, `creche exit condition`

_category: rename × 6, keep × 1_

- `creche graduation` — **opus-4-7-r2:** Stronger alternative: "creche graduation" names the *event* that the segment characterizes; "creche boundary" names the *threshold*. Either is defensible; graduation reads more substantive.
- `creche graduation` — **opus-targeted-alternatives-v2:** Drop "the" + reframe. Per outline: "Crèche graduation occurs when $U_M$ drops enough that natural $\eta^\ast$ falls below the sycophancy threshold." The segment characterizes a *moment* (graduation event). "Boundary" is more static; "graduation" is dynamic and matches the body's prose.
- `creche graduation threshold` — **gemini-targeted-alternatives:** Accurately names the boundary of graduating from a high-margin infant environment.
- `creche boundary` — **opus-4-7-r2:** Drop "the" from the slug. Slug-stylistic rather than semantic — slugs in the rest of the corpus generally don't include articles ("the"). The body's "Crèche graduation occurs when..." reads cleanly without the article.
- `creche boundary` — **opus-targeted-alternatives-v2:** Drop "the" only; substantive keep on the threshold-naming.
- `creche graduation condition` — **opus-4-7-r2:** Same as above for the def-version; "the" in slug is unusual and the substantive name is "crèche graduation condition."
- `creche exit condition` — **opus-targeted-alternatives-v2:** Alternative. "Exit condition" is the formal-systems term; matches FORMAT.md's vocabulary register (scope conditions, persistence conditions). Weaker because "graduation" carries the developmental-trajectory connotation that the crèche concept is grounded in.

## 343. `the four view`

**Alternatives proposed:** `four view architecture`, `four view`, `the four view`, `conversation runtime RLHF7 dialog`

_category: rename × 5, keep × 1_

- `four view architecture` — **opus-4-7-r2:** Even stronger alternative — names the architectural pattern, not just the four views.
- `four view architecture` — **opus-targeted-alternatives-v2:** Even stronger: include "architecture" since the segment's claim is that the four views are an architectural requirement (not just descriptive views). Pairs with the architectural-class vocabulary in `#der-directed-separation`.
- `four view` — **opus-4-7-r2:** Same article-drop as above. The slug should be #def-four-views (or #def-four-views-architecture for full clarity).
- `four view` — **opus-targeted-alternatives-v2:** Drop "the." Per outline: "The Four Views Architecture (Conversation, Runtime, API, Dialog) as structural requirement for Directed Separation." The four views *are* a thing; the slug should name them.
- `the four view` — **gemini-targeted-alternatives:** Acknowledged structural perspective.
- `conversation runtime RLHF7 dialog` — **opus-targeted-alternatives-v2:** Considered. Names the four views directly. Rejected: too long, fails communal-imagination test, doesn't survive the renamed-from-now-sounds-weird test (in 6 months "the four views" is the iconic phrase).

## 344. `the scaffolding tax`

**Alternatives proposed:** `scaffolding tax`, `substrate rent`

_category: rename × 3_

- `scaffolding tax` — **opus-4-7-r2:** Drop "the" from the slug.
- `scaffolding tax` — **opus-targeted-alternatives-v2:** Drop "the" from slug per general slug-stylistic rule (slugs in the rest of the corpus don't include articles). Per outline: "Pay-per-token APIs are unviable in high-$\rho$ environments; true sovereignty requires meter-less local substrates." "Scaffolding tax" names the cost of running the agent on rented substrate. Strong stand-alone keep on the substantive name; rename is just article removal.
- `substrate rent` — **opus-targeted-alternatives-v2:** Considered. More plain-English (scaffolding = rented substrate; tax = rent). Weaker because "tax" carries the connotation that the cost is *imposed by the architecture* (you pay it whether you want to or not), which "rent" doesn't carry as cleanly.

## 345. `unity closure mapping`

**Alternatives proposed:** `unity closure mapping`, `coherence closure mapping`, `closure mapping`

_category: keep × 4, rename × 2_

- `unity closure mapping` — **haiku-4-5:** Unity parametrizes rate-distortion curves for closure defect. Compound but accurate. Keep.
- `unity closure mapping` — **opus-4-7-b:** Keep. The segment's content *is* the mapping between unity (multi-dimensional) and closure (scalar) — the slug is honest.
- `unity closure mapping` — **opus-4-7-r2:** Weak keep, though the slug is heavy. The segment maps the unity dimensions to the closure-defect components via a rate-distortion relation; "mapping" is workable. I considered "unity-closure-rate-distortion" (more precise) but it's even longer.
- `unity closure mapping` — **sonnet-4-6-r2:** "Unity-closure mapping" names the rate-distortion curve parametrization correctly but is dense. Acceptable; no obvious better alternative.
- `coherence closure mapping` — **gemini-2:** Aligns with changing "Unity dimensions" to "Coherence dimensions".
- `closure mapping` — **gemini-3-1-pro-preview-r2:** Shorter.

## 346. `worked example bandit`

**Alternatives proposed:** `worked example bandit`

_category: keep × 2_

- `worked example bandit` — **gemini-targeted-alternatives:** Essential grounding example.
- `worked example bandit` — **haiku-4-5:** End-to-end RL bandit instantiation (approximate). Self-descriptive. Keep.

## 347. `worked example kalman`

**Alternatives proposed:** `worked example kalman`

_category: keep × 2_

- `worked example kalman` — **gemini-targeted-alternatives:** Essential grounding example.
- `worked example kalman` — **haiku-4-5:** End-to-end Kalman instantiation (exact). Self-descriptive. Keep.

## 348. `worked example l1`

**Alternatives proposed:** `worked example l1`

_category: keep × 2_

- `worked example l1` — **gemini-targeted-alternatives:** Essential grounding example.
- `worked example l1` — **haiku-4-5:** L1 augmented DAG: common-cause node, sector condition, L0/L1 comparison. Self-descriptive. Keep.

## 349. `worked example strategy`

**Alternatives proposed:** `worked example strategy`

_category: keep × 2_

- `worked example strategy` — **gemini-targeted-alternatives:** Essential grounding example.
- `worked example strategy` — **haiku-4-5:** Section II strategy DAG instantiation (3-arm bandit). Self-descriptive. Keep.

## 350. `𝒯 σ strategic tempo`

**Alternatives proposed:** `strategic tempo`

_category: canonicalize × 1, rename × 1_

- `strategic tempo` — **gemini-targeted-alternatives:** Distinguishes strategy revision rate from epistemic update rate.
- `strategic tempo` — **haiku-4-5:** Parallel to adaptive tempo. Reads naturally. Established in prose. Keep both.

## 351. `$O_t$ objective`

**Alternatives proposed:** `$O_t$ objective`, `objective`

_category: keep × 1, add-alias × 1_

- `$O_t$ objective` — **haiku-4-5:** "Objective" is the standard English name. No synonym needed. Keep.
- `objective` — **opus-targeted-alternatives:** Same — already in LEXICON.

## 352. `$R$ sector condition radius`

**Alternatives proposed:** `model class capacity`

_category: add-alias × 1_

- `model class capacity` — **opus-4-7-r2:** Already used inconsistently — sometimes "sector radius," sometimes "model class capacity," sometimes "valid region." NOTATION.md uses "model class capacity" in the radius row; canonicalize that as the prose alias. The persistence inequality $\alpha \gt \rho/R$ then reads naturally as "correction-rate exceeds disturbance-rate divided by model class capacity," which is parsable on first encounter.

## 353. `$U_o$ vs $U_O$ collision`

**Alternatives proposed:** `$U_o$ vs $U_O$ collision`

_category: keep × 4_

- `$U_o$ vs $U_O$ collision` — **opus-4-7:** [prose moved from candidate column]: "consider renaming teleological unity to $U_\Omega$ or $U_\text{goal}$" — The uppercase/lowercase distinction between observation uncertainty ($U_o$) and teleological unity ($U_O$) is fragile in serif fonts and read-aloud. Worth an audit; a subscript of $\Omega$ or "goal" would be more robust.
- `$U_o$ vs $U_O$ collision` — **opus-targeted-alternatives-v2:** [prose moved from candidate column]: "`rename teleological unity to $U_\Omega$`" — Per `der-orient-cascade` and the unity-dimensions vocabulary: $U_o$ (observation uncertainty, lowercase o) and $U_O$ (teleological unity, uppercase O) collide in serif fonts and read-aloud. Opus r1 +1; my independent read upgrades to +2 — the collision is a real notation-discipline concern that costs reader-time on every encounter. $\Omega$ is the natural choice (Greek omega for "objective" / "outcome") and avoids the case-sensitivity fragility.
- `$U_o$ vs $U_O$ collision` — **opus-targeted-alternatives-v2:** [prose moved from candidate column]: "`rename teleological unity to $U_{\text{goal}}$`" — Variant. Subscript text is more discoverable but heavier in formula. Acceptable fallback.
- `$U_o$ vs $U_O$ collision` — **opus-targeted-alternatives-v2:** [prose moved from candidate column]: "`keep both, document the collision`" — Considered. Footnote / NOTATION convention rather than rename. Rejected: footnotes don't prevent reader stumbles; the rename is mechanical-cost-low and reader-cost-high if not done.

## 354. `$V_{O_t}^{\min}$`

**Alternatives proposed:** `satisfaction threshold`, `objective floor`

_category: add-alias × 3_

- `satisfaction threshold` — **haiku-4-5:** NOTATION defines this but no English equivalent exists in LEXICON. "Satisfaction threshold" (the minimum trajectory value that counts as objective met) would be useful in prose. Add to LEXICON without renaming the symbol.
- `satisfaction threshold` — **opus-targeted-alternatives-v2:** Per `def-satisfaction-gap` and Haiku r1 single +1. Useful prose alias; gap with NOTATION's existing English. The alias names *what the threshold is for* (satisfying $O_t$).
- `objective floor` — **opus-targeted-alternatives-v2:** Considered. Shorter, parallel to "identifiability floor." Rejected: "floor" is overloaded with the M1 meta-segment (identifiability-floor); creating a second AAD "floor" adds confusion.

## 355. `$\Sigma_t$ strategy`

**Alternatives proposed:** `$\Sigma_t$ strategy`, `strategy`

_category: keep × 1, add-alias × 1_

- `$\Sigma_t$ strategy` — **haiku-4-5:** "Strategy" is the standard English name. No synonym needed. Keep.
- `strategy` — **opus-4-7-r2:** Confirm. The capital-Σ symbol is harder to type than the English alias; expect the alias to dominate prose use, with the symbol used for math.

## 356. `$\alpha$ lower sector bound`

**Alternatives proposed:** `$\alpha$ sector parameter`

_category: add-alias × 1_

- `$\alpha$ sector parameter` — **sonnet-4-6:** The symbol is necessary in equations. The English gloss "sector parameter" is correct — NOTATION.md says this already. No change needed in notation. Keep $\alpha$.

## 357. `$\alpha$ sector condition lower bound`

**Alternatives proposed:** `correction rate constant`, `correction rate or decay rate`

_category: add-alias × 2_

- `correction rate constant` — **opus-4-7-r2:** Currently $\alpha$ appears as a Greek letter throughout but no English alias exists in prose. NOTATION.md gives "lower sector bound of correction function" as the gloss, which is technically correct but reads heavily. "Correction-rate constant" connects to the $\alpha$-as-rate intuition (units $t^{-1}$) and the timescale reading $1/\alpha$. Symbol stays in math; alias enters prose. Prose-symbol layer.
- `correction rate or decay rate` — **haiku-4-5-r2:** NOTATION.md defines $\alpha$ mathematically; prose refers to it as "the sector condition parameter" and "worst-case scalar correction rate." English alias "correction rate" (or "decay rate" in linear-ODE context) would aid readability in continuous prose.

## 358. `$\alpha_1$`

**Alternatives proposed:** `fixed gain regime`, `fixed gain tier`

_category: add-alias × 2_

- `fixed gain regime` — **opus-targeted-alternatives-v2:** Same as above for $\alpha_1$. Per `deriv-strategic-dynamics` and `#disc-separability-pattern`.
- `fixed gain tier` — **codex-gpt-5-r2:** Make the sub-scope partition readable.

## 359. `$\alpha_1$ $\alpha_2$ $\beta$ partition`

**Alternatives proposed:** `fixed gain adaptive gain drift regime`

_category: add-alias × 1_

- `fixed gain adaptive gain drift regime` — **gemini-1:** Translating the symbols into the structural regimes they represent makes the prose readable without a decoder ring.

## 360. `$\alpha_2$`

**Alternatives proposed:** `adaptive gain regime`, `adaptive gain tier`

_category: add-alias × 2_

- `adaptive gain regime` — **opus-targeted-alternatives-v2:** Per multiple r1 single votes (codex, opus). The English alias is already in implicit use. "AMSGrad lands in $\alpha_2$" reads cryptically; "AMSGrad lands in the adaptive-gain regime" reads naturally. Confirms canonicalize across architectures.
- `adaptive gain tier` — **codex-gpt-5-r2:** Make the sub-scope partition readable.

## 361. `$\beta$ a2 assumed sector sub scope`

**Alternatives proposed:** `postulated sector regime`, `assumed sector regime`

_category: add-alias × 4_

- `postulated sector regime` — **agent1-original-brainstorm:** Alternative framing.
- `postulated sector regime` — **haiku-4-5:** Parallel. Keep $\beta$ as symbol; English equivalent for prose.
- `postulated sector regime` — **opus-1m:** Parallel. "Postulated" slightly stronger than "assumed" — conveys the axiomatic move explicitly.
- `assumed sector regime` — **agent1-original-brainstorm:** Parallel to $\alpha_1$/$\alpha_2$.

## 362. `$\delta_{\text{regret}}$`

**Alternatives proposed:** `control regret`

_category: add-alias × 1_

- `control regret` — **sonnet-4-6-r2:** Same as above for the control-regret quantity.

## 363. `$\delta_{\text{regret}}$ control regret`

**Alternatives proposed:** `control regret`, `already has crisp name`

_category: add-alias × 2_

- `control regret` — **opus-4-7-r2:** Already canonical and load-bearing; confirm.
- `already has crisp name` — **haiku-4-5-r2:** The name "control regret" is already canonical. No alias needed.

## 364. `$\delta_{\text{sat}}$`

**Alternatives proposed:** `satisfaction gap`

_category: add-alias × 1_

- `satisfaction gap` — **sonnet-4-6-r2:** Already established in NOTATION.md. This vote canonicalizes the alias relationship: $\delta_{\text{sat}}$ in formulas = "satisfaction gap" in prose.

## 365. `$\delta_{\text{sat}}$ satisfaction gap`

**Alternatives proposed:** `satisfaction gap`, `already has crisp name`

_category: add-alias × 2_

- `satisfaction gap` — **opus-4-7-r2:** Already canonical and load-bearing; confirm.
- `already has crisp name` — **haiku-4-5-r2:** The name "satisfaction gap" is already canonical and memorable. No alias needed.

## 366. `$\eta_{ji}^\ast$`

**Alternatives proposed:** `communication gain`, `trust weighted communication gain`

_category: add-alias × 2_

- `communication gain` — **sonnet-4-6-r2:** The trust-weighted uncertainty ratio for inter-agent channels. LEXICON.md already uses "communication gain." Canonicalize.
- `trust weighted communication gain` — **codex-gpt-5-r2:** Useful alias when explaining the communication-gain formula.

## 367. `$\gamma_{\text{adv}}$ and $\gamma_{\text{coop}}$`

**Alternatives proposed:** `signed coupling`

_category: add-alias × 1_

- `signed coupling` — **codex-gpt-5-r2:** Good umbrella for adversarial and cooperative disturbance terms.

## 368. `$\hat o_t$`

**Alternatives proposed:** `proleptic prediction`, `predicted observation`

_category: add-alias × 3_

- `proleptic prediction` — **gemini-3-1-pro-preview-r2:** Links the symbol directly to the cycle phase.
- `proleptic prediction` — **opus-targeted-alternatives-v2:** Per `def-mismatch-signal`: $\delta = \hat o - o$, with $\hat o$ being the *prolepsis-phase* prediction. Connects symbol to cycle-phase vocabulary explicitly. Confirms Gemini r1 +1 single-vote.
- `predicted observation` — **opus-targeted-alternatives-v2:** Plain-language alternative. Weaker because "proleptic prediction" anchors to the cycle vocabulary the framework already commits to; "predicted observation" is generic.

## 369. `$\hat{P}_\Sigma$`

**Alternatives proposed:** `plan confidence`, `plan confidence score`

_category: add-alias × 2_

- `plan confidence` — **codex-gpt-5-r2:** Strong alias already present in the lexicon direction. Keep canonical.
- `plan confidence score` — **sonnet-4-6-r2:** The root-node propagated DAG status is called "plan-confidence score" in the segment but has no explicit alias established. Adding this makes prose references natural: "the plan-confidence score reached 0.73."

## 370. `$\lambda_{\text{surv}}$`

**Alternatives proposed:** `survival multiplier`

_category: add-alias × 1_

- `survival multiplier` — **codex-gpt-5-r2:** Useful short handle for the survival exploration weight.

## 371. `$\mathcal C_t$ for chronica`

**Alternatives proposed:** `$\mathcal C_t$`

_category: rename × 1_

- `$\mathcal C_t$` — **opus-4-7-b:** Keep. The calligraphic-C choice is deliberately to avoid collision with $\mathcal H$ (entropy) and the symbol works in both LaTeX and prose.

## 372. `$\rho$`

**Alternatives proposed:** `disturbance rate`, `disturbance rate or environmental change rate`

_category: add-alias × 2_

- `disturbance rate` — **opus-targeted-alternatives-v2:** Per NOTATION and `#result-persistence-condition` Section II/III prose. Confirms Opus r1 single-arch +3. Standardize on "disturbance rate" in prose, $\rho$ in math. The phrase "environmental change rate" should be deprecated to a one-time first-encounter expansion.
- `disturbance rate or environmental change rate` — **sonnet-4-6-r2:** $\rho$ appears in formulas throughout and has two prose forms used interchangeably. "Environmental change rate" in Section I context; "disturbance rate" in Section II/III contexts. Both are acceptable; at minimum canonicalize "disturbance rate" as the short form.

## 373. `$\rho$ mismatch injection rate`

**Alternatives proposed:** `disturbance rate`

_category: add-alias × 1_

- `disturbance rate` — **opus-4-7-r2:** Already in informal use, but inconsistent — sometimes "environmental change rate," sometimes "mismatch injection rate," sometimes "disturbance rate." Standardize on "disturbance rate" in prose, $\rho$ in math. The persistence-condition prose ("correction outpaces disturbance") is built around this alias.

## 374. `01 AAD core outline md`

**Alternatives proposed:** `outline md`

_category: rename × 1_

- `outline md` — **haiku-4-5:** AAD canonical outline; name is standard. Keep.

## 375. `02 TST core outline md`

**Alternatives proposed:** `outline md`

_category: rename × 1_

- `outline md` — **haiku-4-5:** TST outline; name is standard. Keep.

## 376. `02 TST core outline md software as agentic domain`

**Alternatives proposed:** `02 TST core outline md software as agentic domain`

_category: keep × 1_

- `02 TST core outline md software as agentic domain` — **codex-1:** Clear, ambitious, and accurate. This heading earns its weight.

## 377. `AAD`

**Alternatives proposed:** `AAD`, `adaptation and agency dynamic AAD`, `adaptation and purpose dynamic apd`

_category: rename × 2, keep × 1_

- `AAD` — **gemini-targeted-alternatives:** Retain core acronym.
- `adaptation and agency dynamic AAD` — **agent1-original-brainstorm:** Considered alternative. "Agency" is overloaded in AI discourse.
- `adaptation and purpose dynamic apd` — **agent1-original-brainstorm:** Considered alternative. Acronym collision risk; doesn't roll off the tongue.

## 378. `AAD AAD internal AAD internally`

**Alternatives proposed:** `AAD internal`, `AAD internal adj AAD internally adv`

_category: keep × 1, canonicalize × 1_

- `AAD internal` — **gemini-targeted-alternatives:** Essential distinction from imported theorems.
- `AAD internal adj AAD internally adv` — **opus-4-7-r2:** The "internally-derived-from-AAD-axioms" move is referenced as "AAD-internal," "AAD-derived," "internally derived," etc. Canonicalize on "AAD-internal" / "AAD-internally" for the specific claim "derived from axioms whose motivation comes from AAD's own architecture, not theorem-imported from external machinery."

## 379. `CIY unified objective`

**Alternatives proposed:** `value information objective`, `exploration exploitation unification`, `unified objective`, `CIY unified objective`, `joint objective`

_category: rename × 4, keep × 1_

- `value information objective` — **codex-1:** The durable idea is a joint value-plus-information policy objective. Leading with "CIY" hides the structure behind house jargon.
- `exploration exploitation unification` — **sonnet-4-6-r2:** "CIY-unified" frontloads an acronym and a verb in the slug. The segment names the joint exploitation-exploration objective via CIY — but the interesting thing is the unification, not CIY per se. However this is long.
- `unified objective` — **gemini-3-1-pro-preview-r2:** CIY is context.
- `CIY unified objective` — **haiku-4-5:** Joint exploitation-exploration objective. Reads naturally. Keep.
- `joint objective` — **sonnet-4-6-r2:** Shorter alternative. "Joint" signals the fusion of exploitation and exploration. Communal-imagination test: "the joint-objective segment" is memorable in conversation. Weak preference.

## 380. `OODA boyd`

**Alternatives proposed:** `OODA loop`, `do not rename`

_category: keep × 2_

- `OODA loop` — **gemini-targeted-alternatives:** Anchor to Boyd terminology.
- `do not rename` — **opus-4-7-b:** Same — "orient cascade" is AAD's adjacent-but-distinct construction; OODA keeps its lineage.

## 381. `OODA4 agent as act agent logogenic`

**Alternatives proposed:** `OODA4 agent as adaptive agent`

_category: rename × 1_

- `OODA4 agent as adaptive agent` — **opus-4-7-b:** Same argument. Matches `#developer-as-adaptive-agent`; the parallel structure (two domain instantiations of "adaptive agent") is itself a pedagogical payoff.

## 382. `a2 prime sub scope partition`

**Alternatives proposed:** `sector scope partition`, `sector condition scope`, `sector bounded operating region`

_category: add-alias × 2, rename × 1_

- `sector scope partition` — **codex-gpt-5-r2:** Strong umbrella for alpha_1, alpha_2, beta, alpha_3, and future sub-scope labels.
- `sector condition scope` — **gemini-targeted-alternatives:** A plain English explanation of the $\alpha_2$ partition.
- `sector bounded operating region` — **gemini-targeted-alternatives:** Makes the a2 prime sub-scope meaningful in prose.

## 383. `a2 sub scope partition`

**Alternatives proposed:** `sector scope partition`, `gain regime partition`

_category: add-alias × 1, rename × 1_

- `sector scope partition` — **codex-1:** Much cheaper in prose than theorem-label-plus-apostrophe. The reader needs to know this is the sector-condition scope split.
- `gain regime partition` — **gemini-targeted-alternatives:** The partition directly separates fixed-gain, adaptive-gain, etc., which is central to A2.

## 384. `accumulated loss across context reset`

**Alternatives proposed:** `context severance penalty`, `turnover drift`

_category: rename × 1, name-unnamed × 1_

- `context severance penalty` — **gemini-targeted-alternatives:** Formalizes the operational cost of logogenic session boundaries.
- `turnover drift` — **codex-gpt-5-r2:** Good logogenic name for degradation caused by repeated context turnover.

## 385. `action transition`

**Alternatives proposed:** `action transition`, `action channel`

_category: keep × 3, rename × 2_

- `action transition` — **gemini-3-1-pro-preview-r2:** Standard terminology.
- `action transition` — **haiku-4-5:** Actions affect environment. Self-descriptive. Keep.
- `action transition` — **opus-4-7-r2:** Weak keep. Names what is defined (the action operator and its environment-state transition); paired with `#def-observation-function` and `#def-agent-environment` cleanly.
- `action channel` — **codex-gpt-5-r2:** Actions change the environment; channel language would wrongly suggest communication symmetry with observation.
- `action channel` — **gemini-2:** To mirror observation-channel and emphasize the interface boundary.

## 386. `actuated vs purposeful goal oriented`

**Alternatives proposed:** `actuated`

_category: rename × 1_

- `actuated` — **sonnet-4-6:** The terminology note is correct — "actuated" avoids consciousness connotations while being technically precise. Keep the choice.

## 387. `adaptation and actuation dynamic`

**Alternatives proposed:** `adaptation and actuation dynamic`

_category: keep × 1_

- `adaptation and actuation dynamic` — **sonnet-4-6-r2:** The rename from ACT to AAD was already deliberate and well-documented. The name is descriptive of the two halves (adaptation = Section I, actuation = Section II). Do not re-open the naming question.

## 388. `additive coordinate forcing → disc forced coordinate`

**Alternatives proposed:** `forced additive coordinate`, `confirming consensus 3`

_category: rename × 2_

- `forced additive coordinate` — **gemini-targeted-alternatives:** More direct name for the segment.
- `confirming consensus 3` — **sonnet-4-6-r2:** All five agents voted this at +2 or +3. What I can add beyond my own cold-start vote: the cross-vote reading shows that all agents independently rejected `#disc-cauchy-coordinates` (Opus −1, Codex −1), confirming "forced-coordinates" is the right move not just a popular one. The Čencov-4th-instance argument (reparameterization invariance is not Cauchy-FE additivity) independently emerged in Haiku, Codex, and Opus without coordination. That convergence on the *reason* — not just the conclusion — strengthens the vote beyond a bandwagon.

## 389. `agent classe class 1 2 3`

**Alternatives proposed:** `goal entanglement hierarchy`, `architectural classe`

_category: canonicalize × 2_

- `goal entanglement hierarchy` — **gemini-targeted-alternatives:** Standardizing the previously resolved rename.
- `architectural classe` — **opus-4-7-r2:** Currently "agent classes," "architecture classes," "class 1/2/3," and "architectural classification" are all in use across `#der-directed-separation`. Canonicalize: "architectural classes" or "the architectural classification (Class 1 / Class 2 / Class 3)" — the *agent* class wording can collide with the LEXICON's "agent classes" table (adaptive system / agentic system / actuated agent / etc.) which is a different decomposition. Keep them disambiguated in prose.

## 390. `agentic cycle theory act`

**Alternatives proposed:** `AAD adaptation and actuation dynamic`, `agentic system framework`

_category: rename × 1, canonicalize × 1_

- `AAD adaptation and actuation dynamic` — **gemini-3-1-pro-preview-r2:** The old name. Ensure all legacy references are scrubbed.
- `agentic system framework` — **gemini-targeted-alternatives:** The new overarching framework name replacing ACT.

## 391. `agentic system`

**Alternatives proposed:** `agentic system`

_category: keep × 1_

- `agentic system` — **codex-2:** Broad, durable umbrella name that comfortably houses AAD, TST, and the later agent classes without sounding like a fad product category.

## 392. `alpha prime sub scope`

**Alternatives proposed:** `sub scope alpha prime`, `potential monotone tier`

_category: canonicalize × 1, add-alias × 1_

- `sub scope alpha prime` — **gemini-targeted-alternatives:** Formalizes the specific game-theoretic extension of sub-scope alpha.
- `potential monotone tier` — **codex-gpt-5-r2:** Useful readable alias for potential and monotone games where sector-style transfer works.

## 393. `alpha1 fixed gain a2 sub scope`

**Alternatives proposed:** `fixed gain regime`

_category: add-alias × 1_

- `fixed gain regime` — **codex-1:** "Lands in alpha1" is decoder-ring prose. The English label is much cheaper in discussion.

## 394. `alpha2 adaptive gain a2 sub scope`

**Alternatives proposed:** `adaptive gain regime`

_category: add-alias × 1_

- `adaptive gain regime` — **codex-1:** Same reasoning as alpha1: the English does the work the symbol cannot do in prose.

## 395. `aporia as the phase name`

**Alternatives proposed:** `aporia`

_category: rename × 1_

- `aporia` — **sonnet-4-6:** The phase is named; the signal within it is "mismatch signal." The distinction is correct and maintained. Keep both with distinct scopes.

## 396. `aporia prolepsis aisthesis epistrophe praxis`

**Alternatives proposed:** `greek rooted vocabulary`, `aporia prolepsis aisthesis epistrophe praxis`

_category: canonicalize × 1, keep × 1_

- `greek rooted vocabulary` — **gemini-targeted-alternatives:** Collectivizes the five distinctive process stages.
- `aporia prolepsis aisthesis epistrophe praxis` — **opus-4-7-b:** [prose moved from candidate column]: "*(keep as a set)*" — The Greek cycle-phase vocabulary works *because* it refuses the flatness of "predict / observe / mismatch / update / act." The README §"Why these terms earn their weight" is load-bearing justification and should not be touched. Keep all five.

## 397. `appendice detail`

**Alternatives proposed:** `appendice detail`, `appendice derivation and detail`

_category: canonicalize × 1, rename × 1_

- `appendice detail` — **gemini-targeted-alternatives:** Standard markdown section header.
- `appendice derivation and detail` — **sonnet-4-6:** Many appendix segments are type: derivation. The current label "Details" undersells what's there. "Derivations and Details" is more accurate.

## 398. `appendice operational domain`

**Alternatives proposed:** `appendice operational domain`

_category: keep × 1_

- `appendice operational domain` — **sonnet-4-6:** Correct and specific. Keep.

## 399. `beta prime sub scope`

**Alternatives proposed:** `sub scope beta prime`, `equilibrium set tier`

_category: canonicalize × 1, add-alias × 1_

- `sub scope beta prime` — **gemini-targeted-alternatives:** Formalizes the non-convergent, cyclic extension of sub-scope beta.
- `equilibrium set tier` — **codex-gpt-5-r2:** Good honest alias for the CCE or set-convergence fallback.

## 400. `boundary condition`

**Alternatives proposed:** `boundary condition`, `coupling structure`

_category: keep × 1, canonicalize × 1_

- `boundary condition` — **gemini-targeted-alternatives:** Standard formal term for limits and constraints.
- `coupling structure` — **audit-471203-incremental:** "boundary condition" carries PDE/control-theory meaning that's not what the segment means; "coupling structure is constitutive" lands more cleanly. [from 01-def-agent-environment.md]

## 401. `bounded disturbance ga 2 model d`

**Alternatives proposed:** `model d bounded disturbance`, `bounded disturbance`

_category: canonicalize × 1, rename × 1_

- `model d bounded disturbance` — **gemini-targeted-alternatives:** Standardizes the specific disturbance model.
- `bounded disturbance` — **sonnet-4-6:** Clear. Keep.

## 402. `bretagnolle huber identity`

**Alternatives proposed:** `bretagnolle huber bound`, `do not rename`, `bretagnolle huber identity`, `no alternative`

_category: keep × 4_

- `bretagnolle huber bound` — **gemini-targeted-alternatives:** Important external anchor for total-variation bounds.
- `do not rename` — **opus-4-7-b:** Same.
- `bretagnolle huber identity` — **opus-4-7:** External-theorem attribution; preserve. Keep.
- `no alternative` — **opus-targeted-alternatives-v2:** Same — external theorem, name retained per prior-art-integration. No genuine alternative exists.

## 403. `brook law formalized as the inevitable tempo loss in team composition`

**Alternatives proposed:** `sub additive tempo penalty`, `the coordination drag`

_category: canonicalize × 1, add-alias × 1_

- `sub additive tempo penalty` — **gemini-targeted-alternatives:** Already explicitly referenced in the cross-domain joining table as the formalization of Brooks's law.
- `the coordination drag` — **gemini-targeted-alternatives:** Very readable translation into a management/organizational mental model.

## 404. `bruineberg pearl-blanket`

**Alternatives proposed:** `pearl-blanket`, `pearl-blanket interpretation`

_category: keep × 1, canonicalize × 1_

- `pearl-blanket` — **agent1-original-brainstorm:** Adopted concept; keep.
- `pearl-blanket interpretation` — **gemini-targeted-alternatives:** Distinguishes the AAD usage from Friston.

## 405. `bruineberg pearl-blanket friston-blanket`

**Alternatives proposed:** `pearl-blanket interpretation`, `pearl-blanket friston-blanket`

_category: canonicalize × 1, keep × 1_

- `pearl-blanket interpretation` — **gemini-targeted-alternatives:** Clarifies the exact reading of Markov blankets used in AAD.
- `pearl-blanket friston-blanket` — **opus-1m:** Adopted (Bruineberg 2022, credit Martin Biehl per fn 3 of that paper per citation audit); keep.

## 406. `c i`

**Alternatives proposed:** `shared objective route c i`, `shared objective route`

_category: canonicalize × 1, add-alias × 1_

- `shared objective route c i` — **gemini-targeted-alternatives:** Provides a semantic name for the strongest composition scope route.
- `shared objective route` — **codex-gpt-5-r2:** Good route name for composite-agent scope.

## 407. `c i c ii c iii c iv`

**Alternatives proposed:** `composition route`

_category: canonicalize × 1_

- `composition route` — **codex-gpt-5-r2:** Use routes consistently for shared-objective, hierarchical, mutual-benefit, and strategic composition.

## 408. `c ii`

**Alternatives proposed:** `hierarchical decomposition route c ii`, `hierarchical derivation route`

_category: canonicalize × 1, add-alias × 1_

- `hierarchical decomposition route c ii` — **gemini-targeted-alternatives:** Provides a semantic name for the intermediate composition scope route.
- `hierarchical derivation route` — **codex-gpt-5-r2:** Good route name for composite-agent scope.

## 409. `c iii`

**Alternatives proposed:** `mutual benefit route c iii`, `mutual benefit route`

_category: canonicalize × 1, add-alias × 1_

- `mutual benefit route c iii` — **gemini-targeted-alternatives:** Provides a semantic name for the weakest alignment-based composition scope route.
- `mutual benefit route` — **codex-gpt-5-r2:** Good route name for composite-agent scope.

## 410. `c iv`

**Alternatives proposed:** `strategic convergence route`

_category: add-alias × 1_

- `strategic convergence route` — **codex-gpt-5-r2:** Better than saying equilibrium route only, because convergence is the scope condition.

## 411. `calibration laboratory domain instantiation`

**Alternatives proposed:** `calibration laboratory`, `calibration lab framing`

_category: canonicalize × 1, rename × 1_

- `calibration laboratory` — **gemini-targeted-alternatives:** Keeps the grounding metaphor intact.
- `calibration lab framing` — **codex-1:** Better as framing language than as a formal category label. The idea is excellent; the phrase can be lighter.

## 412. `calibration laboratory framing for TST`

**Alternatives proposed:** `software calibration laboratory`, `calibration laboratory`

_category: canonicalize × 1, rename × 1_

- `software calibration laboratory` — **gemini-targeted-alternatives:** Solidifies TSTs grounding role.
- `calibration laboratory` — **opus-1m:** C-BP3 landing; well-chosen. Keep.

## 413. `candidate stage`

**Alternatives proposed:** `candidate`, `candidate stage`

_category: rename × 1, keep × 1_

- `candidate` — **opus-4-7:** Terminal pre-publication stage; works because it's standard academic vocabulary. Keep.
- `candidate stage` — **gemini-targeted-alternatives:** Standard segment maturity status.

## 414. `catastrophic forgetting`

**Alternatives proposed:** `catastrophic forgetting regime`, `empty window pathology`

_category: canonicalize × 1, rename × 1_

- `catastrophic forgetting regime` — **gemini-targeted-alternatives:** Forces the specific regime formulation over the generic ML term.
- `empty window pathology` — **gemini-3-1-pro-preview-r2:** Too vague and ML-generic. Prefer AAD's "empty-window pathology".

## 415. `causal OODA1 exploration`

**Alternatives proposed:** `survival exploration`, `causal OODA1 survival`, `causal OODA1 exploration`

_category: rename × 2, keep × 1_

- `survival exploration` — **codex-gpt-5-r2:** The current slug names the derivation machinery, not the result. Survival exploration names the thing.
- `causal OODA1 survival` — **haiku-4-5-r2:** Currently names the effect (exploration drive) rather than the foundational thing being derived (survival imperative). "survival" is the engine; "exploration" is the downstream consequence. Aligns with subject-noun-first principle.
- `causal OODA1 exploration` — **gemini-3-1-pro-preview-r2:** Standard.

## 416. `chain confidence decay keep`

**Alternatives proposed:** `chain confidence decay`, `reaffirm keep with new reasoning`

_category: keep × 2_

- `chain confidence decay` — **gemini-targeted-alternatives:** Core formal result.
- `reaffirm keep with new reasoning` — **sonnet-4-6-r2:** Opus's proposed rename to `#der-log-confidence-additive` (+1) is intellectually interesting (names the uniqueness move rather than the decay consequence) but Opus correctly also votes keep (+2). The "decay" consequence is what readers *use* this result for; the additive structure is the proof technique. The subject-noun should name the *result* (chain confidence decays), not the proof technique (additivity forces log-space representation). Reaffirming keep with this explicit reasoning that was absent from my cold-start.

## 417. `chronica in running prose`

**Alternatives proposed:** `chronica`, `lowercase italic chronica`

_category: keep × 1, canonicalize × 1_

- `chronica` — **gemini-targeted-alternatives:** Maintains the Greek-rooted term for the causal record.
- `lowercase italic chronica` — **codex-gpt-5-r2:** Useful style convention: capitalize in headings, use lowercase in prose like aporia or praxis.

## 418. `claim verified dep verified format clean`

**Alternatives proposed:** `claim verified dep verified format clean`

_category: keep × 1_

- `claim verified dep verified format clean` — **opus-4-7:** Each stage name encodes exactly what was verified. Self-documenting. Keep.

## 419. `class 1 agent`

**Alternatives proposed:** `modular agent`

_category: rename × 1_

- `modular agent` — **gemini-1:** "Class X" requires a lookup every time. Naming the architectural property directly is much more memorable and scope-honest. [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]

## 420. `class 1 class 2 class 3`

**Alternatives proposed:** `goal entanglement hierarchy`, `architecture classe`, `modularity partition`

_category: rename × 2, canonicalize × 1_

- `goal entanglement hierarchy` — **gemini-targeted-alternatives:** Directly describes what the classes measure (how much $G_t$ entangles with $M_t$ updates).
- `architecture classe` — **codex-gpt-5-r2:** Canonical umbrella helps avoid overloading class numbers across sections.
- `modularity partition` — **gemini-targeted-alternatives:** Classes are precisely modular, partially modular, and merged.

## 421. `class 1 class 2 class 3 agent`

**Alternatives proposed:** `goal entanglement hierarchy`

_category: canonicalize × 1_

- `goal entanglement hierarchy` — **gemini-targeted-alternatives:** Standardizes the structural property behind the classes.

## 422. `class 1 subagent forming a class 3 composite`

**Alternatives proposed:** `strategic composition entanglement`, `composition lift`

_category: rename × 1, name-unnamed × 1_

- `strategic composition entanglement` — **gemini-targeted-alternatives:** Captures that composing modular agents strategically creates a coupled Class 3 composite through cross-agent modeling.
- `composition lift` — **codex-gpt-5-r2:** Potentially useful, but needs formal confirmation to avoid sounding like a slogan.

## 423. `class 2 agent`

**Alternatives proposed:** `integrated agent`

_category: rename × 1_

- `integrated agent` — **gemini-1:** Class 2 = integrated (the goal-entangled architecture). Companion to Modular (Class 1) and Partially-Coupled (Class 3). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]

## 424. `class 3 agent`

**Alternatives proposed:** `partially coupled agent`

_category: rename × 1_

- `partially coupled agent` — **gemini-1:** Class 3 = partially-coupled. Companion to Modular (Class 1) and Integrated (Class 2). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.]

## 425. `claude md`

**Alternatives proposed:** `claude md`

_category: keep × 1_

- `claude md` — **haiku-4-5:** Project instructions; name is established and clear. Keep.

## 426. `closure defect bridge lemma`

**Alternatives proposed:** `bridge lemma`, `closure bridge`

_category: keep × 1, canonicalize × 1_

- `bridge lemma` — **gemini-targeted-alternatives:** Retains the standard mathematical naming for the theorem connecting defect to error.
- `closure bridge` — **codex-gpt-5-r2:** Shorter reusable phrase while preserving the formal bridge lemma title.

## 427. `closure defect consuming macro reserve`

**Alternatives proposed:** `coordination overhead`, `closure load`

_category: canonicalize × 1, name-unnamed × 1_

- `coordination overhead` — **gemini-targeted-alternatives:** Translates the abstract reserve-consumption concept into the practical tempo penalty ($C_{\text{coord}}$).
- `closure load` — **codex-gpt-5-r2:** Good name for the pressure epsilon-star times macro-rate places on composite persistence.

## 428. `coherence coupling measurement`

**Alternatives proposed:** `coherence coupling measurement`, `q measurement`

_category: keep × 2, rename × 1_

- `coherence coupling measurement` — **opus-4-7-b:** Keep.
- `coherence coupling measurement` — **opus-targeted-alternatives:** TST `#meas-coherence-coupling`: measurement of $Q$ (coherence) and coupling from git history. The hyphenated form pairs with `#def-system-coherence` and `#def-system-coupling` definitions. Keep.
- `q measurement` — **opus-targeted-alternatives:** Symbol-only alternative. Loses readability. Rejected.

## 429. `communication gain $\eta_{ji}^\ast$`

**Alternatives proposed:** `communication gain`, `trust gain`

_category: keep × 2, canonicalize × 1_

- `communication gain` — **gemini-targeted-alternatives:** Standardizes the optimal trust parameter.
- `trust gain` — **gemini-1:** The definition is "Trust-weighted uncertainty ratio". "Trust gain" might be more evocative of the inter-agent dynamic than the clinical "Communication gain".
- `trust gain` — **gemini-2:** "Communication gain" sounds like signal amplitude. "Trust gain" captures the trust-weighted uncertainty ratio.

## 430. `concept the multiplicative κ processing × 𝒜 scaling of class 2 directional drift and its consequent goal conformant failure regime`

**Alternatives proposed:** `ambiguity bounded bia law`, `zero ambiguity conditioning`, `the sycophancy equation`, `the κ × 𝒜 product`, `the sycophancy attractor`

_category: name-unnamed × 5_

- `ambiguity bounded bia law` — **gemini-3-1-pro-preview-r2:** The foundational theorem of prompt engineering and LLM agent design ($\kappa \times \mathcal{A}$). [original phrasing: unnamed: the rule that bias is the product of architectural coupling and environmental ambiguity]
- `zero ambiguity conditioning` — **gemini-3-1-pro-preview-r2:** The mathematical reason formal verifiers (AlphaProof) succeed where SWE-agents fail. [original phrasing: unnamed: neutralizing sycophancy by hardening the environment to drop ambiguity to zero]
- `the sycophancy equation` — **gemini-3-1-pro-preview-r2:** Beautifully explains LLM sycophancy as a structural, not moral, failing. [original phrasing: unnamed: the product of architectural coupling ($\kappa$) and environmental ambiguity ($\mathcal{A}$)]
- `the κ × 𝒜 product` — **opus-4-7-r2:** Confirmation with new reasoning — Gemini coined "ambiguity-bounded bias law" and "the sycophancy equation" for this; both miss the mark slightly. The product $\kappa_{\text{processing}} \times \mathcal{A}(e_\tau)$ is the right thing to name, and naming it after its mathematical form ("the κ × 𝒜 product") rather than its consequence ("sycophancy") preserves scope-honesty: sycophancy is one downstream behavioral manifestation; the product is the structural quantity. Then phrases like "the sycophancy attractor is a high-κ × 𝒜 regime" work cleanly. [original phrasing: unnamed: the explicit name for what makes Class 2 agents distinctive — bias scales with κ × 𝒜]
- `the sycophancy attractor` — **opus-4-7-r2:** New alternative — Gemini's "sycophancy equation" names the product but not the *attractor* in dynamics that the product produces. When $\kappa \times \mathcal{A}$ is large *and* the tempo of independent observation is low, the system is in a basin of attraction that drifts toward goal-conformant rather than truth-tracking output. Naming this attractor (as opposed to the equation) gives logogenic-agents prose a phrase for the *condition* (you're in the sycophancy attractor) vs the *quantity* (κ × 𝒜 is your distance from the boundary). Pairs with my "the κ × 𝒜 product" canonicalization. [original phrasing: unnamed: the joint failure mode where κ × 𝒜 is large *and* observation tempo is low]

## 431. `concept the sequence of cycle phase prolepsis aisthesis aporia epistrophe praxis considered as a single named whole`

**Alternatives proposed:** `adaptive cycle`, `orient cascade`, `the adaptive pentad`, `adaptive cycle phase`, `five adaptive cycle phase`, `the pentad five phase cycle`, `adaptive traversal`, `the pentad`, `the five turn`

_category: name-unnamed × 6, canonicalize × 2, rename × 2_

- `adaptive cycle` — **gemini-targeted-alternatives:** The generic term for the Prolepsis-Praxis loop. [original phrasing: unnamed the complete adaptive cycle from anticipation through action]
- `orient cascade` — **gemini-targeted-alternatives:** Maps the specific five-phase execution order. [original phrasing: unnamed cycle phase sequence as whole]
- `the adaptive pentad` — **gemini-1:** Provides a single memorable noun for the 5-phase cycle (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) as a complete unit. [original phrasing: unnamed: cycle-phase sequence as a whole]
- `the adaptive pentad` — **opus-4-7-b:** The five-phase cycle (prolepsis → aisthesis → aporia → epistrophe → praxis) has a piecewise name per phase but no *collective* noun. "The cycle" works when context is clear but is ambiguous with (e.g.) credit cycles or OODA cycles. "The pentad" or "the adaptive pentad" is a specific collective noun that fits AAD's Greek-vocabulary commitment. Weak preference; aesthetic call. [original phrasing: unnamed: the cycle-as-a-whole]
- `adaptive cycle phase` — **gemini-targeted-alternatives:** Collectivizes Prolepsis, Aisthesis, Aporia, Epistrophe, and Praxis. [original phrasing: unnamed the five phases of the adaptive cycle]
- `five adaptive cycle phase` — **gemini-targeted-alternatives:** Collective grouping. [original phrasing: the five cycle phases prolepsis aisthesis aporia epistrophe praxis]
- `the pentad five phase cycle` — **agent1-original-brainstorm:** Probably not worth effort. Worth surfacing. [original phrasing: unnamed: cycle-phase sequence as whole]
- `adaptive traversal` — **gemini-2:** "The cycle-as-a-whole" is clunky. "Adaptive traversal" suggests moving through the loop. [original phrasing: unnamed: The cycle-as-a-whole]
- `the pentad` — **opus-1m:** Agree with original. Low priority. Names the five-phase sequence as a unit. [original phrasing: unnamed: cycle-phase sequence as a whole]
- `the five turn` — **opus-4-7-b:** Considered as a more Germanic / industrial alternative to "pentad." Reject: loses the Greek-vocabulary register and gains nothing. [original phrasing: unnamed: the cycle-as-a-whole]

## 432. `concept the upper bound on what a given model class can express and the consequent constraint on feasible strategy complexity`

**Alternatives proposed:** `latent structural capacity`, `epistemic ceiling`, `the representational ceiling`

_category: name-unnamed × 3_

- `latent structural capacity` — **codex-gpt-5-r2:** Strong name for low-credence or inaccessible structure that preserves future adaptability. [original phrasing: latent structural capacity]
- `epistemic ceiling` — **sonnet-4-6-r2:** This relationship appears in the `#der-orient-cascade` Discussion (better $M_t$ enables richer evaluable $\Sigma_t$) and is partially what I named "epistemic-strategic coupling" in my cold-start. But reading Gemini's "rate-distortion surface" and Codex's "macro-step ratio" votes sparked a more specific proposal: the asymmetric *ceiling* that $M_t$ capacity places on evaluable $\Sigma_t$ complexity deserves its own name. "Epistemic ceiling" is distinct from "identifiability floor" (which is about what statistics can recover); the epistemic ceiling is about what strategies are evaluable given the current model. Load-bearing in composition work. Not in any other file. [original phrasing: unnamed: the asymmetry where strategy complexity is bounded by model capacity but not vice versa]
- `the representational ceiling` — **gemini-3-1-pro-preview-r2:** Makes the failure mode of parametric adaptation visceral. [original phrasing: unnamed: the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$]

## 433. `context wiping at session boundary`

**Alternatives proposed:** `the epistemic severance`, `context turnover discontinuity`

_category: add-alias × 1, canonicalize × 1_

- `the epistemic severance` — **gemini-targeted-alternatives:** Visceral name for the specific loss of continuity LLMs suffer, distinct from general "context turnover".
- `context turnover discontinuity` — **gemini-targeted-alternatives:** Ties directly to the "obs-context-turnover" phrasing.

## 434. `continuity persistence`

**Alternatives proposed:** `identity continuity`, `continuity persistence`

_category: rename × 1, keep × 1_

- `identity continuity` — **gemini-2:** "Continuity persistence" is slightly redundant. "Identity continuity" clarifies that it's about $\mathcal{C}_t$ and temporal depth.
- `continuity persistence` — **codex-gpt-5-r2:** Slightly repetitive, but it is precise and needed for identity-through-change claims.

## 435. `contraction hierarchy`

**Alternatives proposed:** `contraction hierarchy`, `contraction tier`

_category: keep × 1, rename × 1_

- `contraction hierarchy` — **gemini-targeted-alternatives:** Elevates the tier description.
- `contraction tier` — **sonnet-4-6:** The Tier 1/2/3 system in #composition-closure is called "Contraction Tier" not "Contraction Hierarchy." Slight naming inconsistency with the other two. Not a priority to fix, but noting the asymmetry.

## 436. `contraction over drift principle`

**Alternatives proposed:** `contraction over drift principle`, `contraction imperative`

_category: keep × 1, add-alias × 1_

- `contraction over drift principle` — **gemini-targeted-alternatives:** Formally adopted.
- `contraction imperative` — **codex-gpt-5-r2:** Short and vivid, but less precise than contraction-over-drift.

## 437. `coordination overhead threshold`

**Alternatives proposed:** `coordination tax`, `coordination overhead`, `coordination drag`

_category: rename × 3, canonicalize × 1_

- `coordination tax` — **codex-1:** This deserves a reusable noun slot. The current phrase explains; the proposed phrase sticks.
- `coordination tax` — **opus-targeted-alternatives-v2:** Per `der-tempo-composition` and `#def-system-coupling`: the tempo-equivalent cost of cross-agent coordination in composite agents. "Tax" is engineering-vivid; "threshold" undersells (the cost is *paid* whether the threshold is crossed or not). Confirms Codex r1 single +1; my read upgrades.
- `coordination overhead` — **gemini-targeted-alternatives:** Formally adopted.
- `coordination drag` — **opus-targeted-alternatives-v2:** Variant — fluid-dynamics metaphor. Carries the *continuous-cost* sense better than "tax" (taxes can be fixed-rate; drag scales with velocity / tempo). Either is acceptable.

## 438. `correlated evidence overconfidence`

**Alternatives proposed:** `evidential overcounting`

_category: rename × 1_

- `evidential overcounting` — **gemini-targeted-alternatives:** Describes the epistemic consequence of treating correlated signals as independent.

## 439. `coupled diagnostic framework`

**Alternatives proposed:** `coupled diagnostic pass`, `coupled diagnostic framework`, `coupled diagnostic`, `hoc diagnostic`, `coupled diagnostic decomposition`

_category: rename × 5, keep × 2_

- `coupled diagnostic pass` — **codex-2:** "Framework" is abstract; the segment is really a post-update procedure.
- `coupled diagnostic pass` — **codex-gpt-5-r2:** Pass is more operational than framework and fits the post-hoc procedure. Coupled diagnostics remains acceptable as the shorter prose name.
- `coupled diagnostic framework` — **opus-4-7-r2:** Weak keep. "Framework" is one of the principles file's flagged placeholder words; here it's accurate enough (the segment names a diagnostic *framework* for Class 2 agents) but I could see the case for "diagnostic-decomposition" or "diagnostic-construction." Mild.
- `coupled diagnostic framework` — **sonnet-4-6-r2:** "Coupled diagnostic framework" names the Section II results that survive as a coupled formulation for logogenic agents. Precise.
- `coupled diagnostic` — **codex-gpt-5-r2:** Framework is a weak generic noun. Diagnostics is the actual deliverable.
- `hoc diagnostic` — **codex-1:** "Framework" is generic filler here. The distinctive move is diagnostic extraction after the coupled update.
- `coupled diagnostic decomposition` — **opus-4-7-r2:** Alternative — "decomposition" names the formal move (post-hoc decomposition from coupled update); "framework" is more diffuse.

## 440. `cox theorem causal hierarchy theorem tikhonov theorem`

**Alternatives proposed:** `do not rename`, `foundational anchor`

_category: keep × 1, rename × 1_

- `do not rename` — **opus-4-7-b:** Same — FORMAT.md §"Why these labels" explicitly preserves external theorem names.
- `foundational anchor` — **gemini-targeted-alternatives:** Identifies the imported theorems the framework rests upon.

## 441. `crossing from multi agent to composite scope`

**Alternatives proposed:** `composition threshold`, `crossing`

_category: rename × 1, name-unnamed × 1_

- `composition threshold` — **gemini-targeted-alternatives:** Designates the formal boundary where sub-agents become a coherent composite.
- `crossing` — **codex-gpt-5-r2:** Useful name for transitions into or out of composite-agent status.

## 442. `crèche creche`

**Alternatives proposed:** `the crèche`, `crèche with diacritic in framing prose creche in slug`

_category: keep × 1, canonicalize × 1_

- `the crèche` — **gemini-targeted-alternatives:** The high-margin developmental environment.
- `crèche with diacritic in framing prose creche in slug` — **opus-4-7-r2:** Mixed usage. Canonicalize: in segment titles and prose, "Crèche" with the grave accent (consistent with the agentic-tft source); in slugs, "creche" without the accent (since slug-tooling rules disallow non-ASCII).

## 443. `da2 inc ≡ ct2 at m i equivalence`

**Alternatives proposed:** `sector contraction equivalence`

_category: rename × 1_

- `sector contraction equivalence` — **codex-1:** The point is the equivalence between the incremental sector bound and Euclidean contraction. The current label reads like notebook shorthand.

## 444. `da2 prime inc`

**Alternatives proposed:** `incremental sector bound`

_category: add-alias × 1_

- `incremental sector bound` — **codex-gpt-5-r2:** Use this English name in prose. The symbol is only useful in tables and formal derivations.

## 445. `da2 prime inc equal ct2 at m equal i`

**Alternatives proposed:** `sector contraction equivalence`

_category: name-unnamed × 1_

- `sector contraction equivalence` — **codex-gpt-5-r2:** Excellent reusable handle for the Euclidean bridge between incremental sector structure and contraction.

## 446. `dark room exploration drive`

**Alternatives proposed:** `survival imperative`, `dark room exploration drive`

_category: canonicalize × 1, name-unnamed × 1_

- `survival imperative` — **gemini-targeted-alternatives:** Distinguishes AAD exploration from the Friston dark room problem.
- `dark room exploration drive` — **codex-gpt-5-r2:** Avoid. It imports active-inference baggage and misnames the AAD result, which is survival exploration.

## 447. `derivation audit table`

**Alternatives proposed:** `derivation audit table`

_category: keep × 1_

- `derivation audit table` — **codex-1:** Strong keep. This names a concrete artifact and a valuable house practice at the same time.

## 448. `developer as act agent TST`

**Alternatives proposed:** `developer as adaptive agent`, `developer as agent`

_category: rename × 2_

- `developer as adaptive agent` — **opus-4-7-b:** The slug is a direct relic of the pre-2026-04-16 "ACT" framework naming — no longer accurate. "Adaptive agent" matches LEXICON's agent-class vocabulary and is framework-rename-proof. The segment invokes Section I machinery, so "adaptive" is semantically correct. This is mechanical cleanup overdue since April.
- `developer as agent` — **gemini-targeted-alternatives:** Core mapping for TST.

## 449. `developmental trajectory`

**Alternatives proposed:** `developmental trajectory`, `creche trajectory`

_category: keep × 2, rename × 2_

- `developmental trajectory` — **opus-4-7-r2:** Acceptable keep — logozoetic. "Developmental trajectory" is the right substantive noun.
- `developmental trajectory` — **sonnet-4-6-r2:** "Developmental trajectory" names the observation about how logozoetic agents develop.
- `creche trajectory` — **codex-gpt-5-r2:** The Crèche is memorable and already present in the title. Use it to make the logozoetic development path distinctive.
- `creche trajectory` — **opus-4-7-r2:** Rebuttal — Codex proposed this at +3 with the rationale that "Crèche" is memorable. I think this conflates two distinct things: the *Crèche* is the bounded developmental environment (Class-1 worker agents under supervision); the *developmental trajectory* is the path through agent classes that an ELI traces over time (which extends beyond the Crèche into post-graduation autonomy). Renaming would collapse a distinction the framework wants to preserve. Codex's instinct (Crèche is memorable, use it) is right but applied to the wrong segment — the Crèche-specific segment is `def-the-creche-boundary`, where "creche" *is* the right subject-noun.

## 450. `discussion segment header`

**Alternatives proposed:** `discussion section`, `discussion`

_category: canonicalize × 1, rename × 1_

- `discussion section` — **gemini-targeted-alternatives:** Standard markdown section header.
- `discussion` — **opus-1m:** Public API; keep.

## 451. `dual optimization`

**Alternatives proposed:** `dual optimization`, `development time decomposition`, `comprehension implementation optimization`, `dual cost optimization`, `comprehension implementation tradeoff`

_category: rename × 4, keep × 3_

- `dual optimization` — **opus-4-7-b:** Keep.
- `dual optimization` — **sonnet-4-6-r2:** "Dual optimization" (minimize comprehension + implementation time). Accurate.
- `dual optimization` — **sonnet-4-6:** "Dual" is accurate (minimize comprehension time + implementation time simultaneously) but "dual optimization" in mathematics usually means Lagrangian duality. Mild overload risk.
- `development time decomposition` — **codex-gpt-5-r2:** Dual optimization is overloaded. The derivation decomposes development time into comprehension and implementation components.
- `comprehension implementation optimization` — **codex-1:** "Dual optimization" is pure abstraction. The contribution is jointly optimizing future comprehension and implementation cost, and the name should say that.
- `dual cost optimization` — **gemini-1:** Adding "cost" clarifies that we are minimizing the dual costs of comprehension and implementation.
- `comprehension implementation tradeoff` — **sonnet-4-6:** Too long.

## 452. `edge update natural parameter`

**Alternatives proposed:** `log odd edge update`, `log odd edge coordinate`, `natural edge update`, `edge update natural parameter`, `log odd update`

_category: rename × 4, keep × 1_

- `log odd edge update` — **codex-gpt-5-r2:** The result is log-odds as the forced edge-update coordinate. The current name is method-facing.
- `log odd edge coordinate` — **codex-gpt-5-r2:** Even sharper than my earlier log-odds edge update: the result is that log-odds is the forced coordinate.
- `natural edge update` — **gemini-3-1-pro-preview-r2:** Flows better.
- `edge update natural parameter` — **haiku-4-5:** Log-odds as unique additive-evidence coordinate for edge credences (evidential-additivity axiom). Compound but specialist-vocabulary (natural parameter is information-geometric term). Keep.
- `log odd update` — **opus-4-7-b:** The segment's content is "log-odds is the unique additive-evidence coordinate for edge credences under evidential additivity (Cauchy-FE)." The current slug ("natural parameter") leans on exponential-family vocabulary that the segment derives *to*, not from. `#log-odds-update` names the derived coordinate and is shorter; "natural parameter" can live in the subtitle. Modest preference.

## 453. `epistemic architecture for bounded correction under decomposed disturbance`

**Alternatives proposed:** `epistemic architecture`, `bounded correction architecture`

_category: canonicalize × 1, rename × 1_

- `epistemic architecture` — **gemini-targeted-alternatives:** Names the foundational setup.
- `bounded correction architecture` — **codex-2:** The long phrase has substance, but it needs a shorter speakable handle if it will recur.

## 454. `epistemic status segment header`

**Alternatives proposed:** `epistemic status section`, `epistemic status`

_category: canonicalize × 1, rename × 1_

- `epistemic status section` — **gemini-targeted-alternatives:** Standard markdown section header.
- `epistemic status` — **opus-1m:** Public API; keep.

## 455. `exact robust qualitative heuristic conditional claim tier`

**Alternatives proposed:** `epistemic claim tier`, `exact robust qualitative heuristic conditional claim tier`

_category: rename × 1, canonicalize × 1_

- `epistemic claim tier` — **gemini-targeted-alternatives:** Formally collectivizes the four levels of rigor.
- `exact robust qualitative heuristic conditional claim tier` — **opus-4-7-r2:** [prose moved from candidate column]: "use exactly the AAD tier vocabulary" — Defended canonicalization, in CLAUDE.md and FORMAT.md already. Do not use "Solid," "Confident," or "Plausible" as tier labels — these were explicit non-AAD borrowings to avoid.

## 456. `exponential cognitive load`

**Alternatives proposed:** `exponential cognitive load`

_category: keep × 2_

- `exponential cognitive load` — **opus-4-7-b:** Keep. The "exponential" in the slug is load-bearing (the claim's punch is *exponential* scaling).
- `exponential cognitive load` — **sonnet-4-6-r2:** "Exponential cognitive load" names the context-switch cost compounding hypothesis.

## 457. `feature`

**Alternatives proposed:** `feature`

_category: keep × 2_

- `feature` — **opus-4-7-r2:** Acceptable keep — TST. "Feature" as the unit of coherent change is well-grounded in software engineering.
- `feature` — **sonnet-4-6-r2:** "Feature" is the established TST term (unit of coherent change). Standard vocabulary adopted.

## 458. `finding segment section`

**Alternatives proposed:** `finding section`, `finding`

_category: canonicalize × 2_

- `finding section` — **gemini-targeted-alternatives:** Standard markdown section header.
- `finding` — **opus-4-7-r2:** Defended. The schema is fixed in FORMAT.md (Brief / Impact / Novelty Claim / Related Work / Search Log); do not paraphrase the section name. The bin/extract-findings tool depends on the exact heading.

## 459. `fisher whitened update`

**Alternatives proposed:** `fisher whitened update`, `fisher rao metric update`

_category: keep × 1, rename × 1_

- `fisher whitened update` — **codex-gpt-5-r2:** Accurate, compact, and tied to the real mathematical operation.
- `fisher rao metric update` — **gemini-targeted-alternatives:** Roots the whitening operation firmly in information geometry instead of generic signal processing.

## 460. `formal expression segment header`

**Alternatives proposed:** `formal expression section`, `formal expression`

_category: canonicalize × 1, rename × 1_

- `formal expression section` — **gemini-targeted-alternatives:** Standard markdown section header.
- `formal expression` — **opus-1m:** Public API for outline-filter (see PROPOSALS.md §H.5). Established. Keep.

## 461. `format md`

**Alternatives proposed:** `format md`

_category: keep × 1_

- `format md` — **haiku-4-5:** Segment file conventions; name is standard. Keep.

## 462. `formulation definition result etc segment type`

**Alternatives proposed:** `formulation definition result etc segment type`, `segment typology`

_category: canonicalize × 1, rename × 1_

- `formulation definition result etc segment type` — **opus-4-7-r2:** [prose moved from candidate column]: "use exactly the FORMAT.md vocabulary" — Defended canonicalization. The 19 segment types in FORMAT.md are a closed vocabulary; do not paraphrase them ("postulate" not "axiom," "result" not "theorem," "derivation" not "proof," etc.). The CLAUDE.md "Why these labels" rationale is load-bearing; vote to protect against drift.
- `segment typology` — **gemini-targeted-alternatives:** Defines the document types in the AAD corpus.

## 463. `gate advantage`

**Alternatives proposed:** `observation gated tempo advantage`, `noise gated tempo advantage`, `gate advantage`, `noise gated tempo`, `noise gating`

_category: rename × 4, keep × 2_

- `observation gated tempo advantage` — **codex-gpt-5-r2:** Names the effect and the gated quantity explicitly. The current slug is too compressed.
- `noise gated tempo advantage` — **codex-gpt-5-r2:** The current slug is too compressed. The result is specifically that observation noise gates tempo advantage.
- `gate advantage` — **gemini-3-1-pro-preview-r2:** Specific reference.
- `gate advantage` — **sonnet-4-6-r2:** "Gates advantage" names the observation that noise gates adversarial tempo advantage. Precise.
- `noise gated tempo` — **sonnet-4-6-r2:** Codex proposed `#obs-noise-gated-tempo-advantage` (+2). I had proposed `obs-noise-gating` (+1). The "noise-gated" compound is more evocative than plain "noise gating" and names the phenomenon precisely. But Codex's version is five words. `obs-noise-gated-tempo` drops "advantage" (which is the consequence, not the observation itself) and still passes the communal-imagination test ("the noise-gated-tempo observation"). New candidate; shorter than Codex, different from my original.
- `noise gating` — **sonnet-4-6-r2:** Alternative: "noise gating" is more evocative — observation noise acts as a gate on the adversarial advantage. Weak preference vs. "gates advantage."

## 464. `gemini boyd exponent for adversarial tempo advantage`

**Alternatives proposed:** `superlinear tempo advantage`, `reject boyd exponent`

_category: canonicalize × 1, rebuttal × 1_

- `superlinear tempo advantage` — **gemini-targeted-alternatives:** Formally adopts the scaling property.
- `reject boyd exponent` — **sonnet-4-6-r2:** Gemini proposed "Boyd exponent" (+3) for the superlinear adversarial tempo advantage ($b = 2$). This violates the project's prior-art-integration principle in the wrong direction: Boyd is the historical inspiration (OODA loop), but the *mathematical result* (superlinear scaling exponent derived from the sector-persistence template) is AAD's own derivation. Naming the result after Boyd implies it's adopted from Boyd's work, when it's AAD's formalization of a qualitative Boyd claim. "Adversarial tempo advantage" correctly credits the mechanism to AAD's formalism while the Discussion acknowledges Boyd's inspiration. Gemini's vote would create exactly the NIH-syndrome-in-reverse this project guards against.

## 465. `grafting`

**Alternatives proposed:** `strategic grafting`, `grafting`, `branch insertion`, `hypothesis introduction`

_category: rename × 2, canonicalize × 1, keep × 1_

- `strategic grafting` — **codex-gpt-5-r2:** Excellent name for adding a new causal branch or imported structure into the strategy DAG.
- `grafting` — **opus-targeted-alternatives:** Per `#form-structural-change-as-parametric-limit`: "grafting is a new causal hypothesis initialized at a prior" — adding an edge to $\Sigma_t$ at low credence. The horticultural metaphor is apt: a new branch is *added to a living structure*, expected to integrate or fail. Pruning + grafting + reweighting form a self-consistent biological vocabulary, and the segment uses all three. Strong concept.
- `branch insertion` — **opus-targeted-alternatives:** Plain-language candidate. Rejected: loses the integration-with-existing-structure connotation that "grafting" carries. Branch-insertion sounds like a tree-data-structure edit; grafting names a hypothesis-test where the new branch may or may not "take."
- `hypothesis introduction` — **opus-targeted-alternatives:** Considered. Accurate but flat. The segment's surrounding vocabulary (pruning, reweighting, neutral mutation) is biological/horticultural; "hypothesis introduction" breaks register.

## 466. `hafez $H_b$`

**Alternatives proposed:** `agent opacity $H_b$`, `$H_b$`

_category: canonicalize × 1, keep × 1_

- `agent opacity $H_b$` — **gemini-targeted-alternatives:** Hafez opacity metric applied to adversarial dynamics.
- `$H_b$` — **opus-1m:** Adopted; keep.

## 467. `hafez $H_b$ miller meta machine bruineberg pearl-blanket`

**Alternatives proposed:** `do not rename`, `external theoretical anchor`

_category: keep × 1, rename × 1_

- `do not rename` — **opus-4-7-b:** Same.
- `external theoretical anchor` — **gemini-targeted-alternatives:** Grouping of specific prior-art literature.

## 468. `hafez h b`

**Alternatives proposed:** `h b`, `agent opacity $H_b$`

_category: keep × 1, canonicalize × 1_

- `h b` — **agent1-original-brainstorm:** Adopted concept; AAD adds observer/horizon/trajectory indexing but keeps the symbol.
- `agent opacity $H_b$` — **gemini-targeted-alternatives:** Standardizes the opacity metric.

## 469. `honest limit`

**Alternatives proposed:** `honest limit`, `limit`

_category: keep × 1, rename × 1_

- `honest limit` — **gemini-targeted-alternatives:** Standardizes the structural boundary marking convention.
- `limit` — **codex-2:** I like the ethos, but the header should optimize scanability over tone.

## 470. `i adaptive system under uncertainty`

**Alternatives proposed:** `section i adaptive system under uncertainty`, `i adaptive system under uncertainty`

_category: canonicalize × 1, keep × 1_

- `section i adaptive system under uncertainty` — **gemini-targeted-alternatives:** Standard section heading formatting.
- `i adaptive system under uncertainty` — **sonnet-4-6:** The section name is accurate and positions Section I correctly. "Under Uncertainty" is load-bearing — it distinguishes adaptive systems from optimal-control-over-known-dynamics, which is explicitly out of scope. Keep.

## 471. `identifiability coefficient`

**Alternatives proposed:** `identifiability coefficient`

_category: keep × 1_

- `identifiability coefficient` — **codex-gpt-5-r2:** Strong scalar name for the causal-attribution discount on edge updates.

## 472. `identifiability floor family`

**Alternatives proposed:** `identifiability floor`, `epistemic lower bound`, `observational limit`

_category: rename × 2, canonicalize × 1_

- `identifiability floor` — **codex-gpt-5-r2:** Keep floor as the family noun.
- `epistemic lower bound` — **gemini-targeted-alternatives:** Describes exactly what these are: hard limits on what can be inferred.
- `observational limit` — **gemini-targeted-alternatives:** A slightly more intuitive phrasing for non-theoreticians.

## 473. `ii actuated adaptation agentic system`

**Alternatives proposed:** `section ii actuated adaptation`, `ii purposeful adaptation actuated agent`, `ii agentic system purposeful adaptation`

_category: rename × 2, canonicalize × 1_

- `section ii actuated adaptation` — **gemini-targeted-alternatives:** Standard section heading formatting.
- `ii purposeful adaptation actuated agent` — **sonnet-4-6:** The current name reads backwards — "Actuated Adaptation" puts the outcome before the mechanism; "Agentic Systems" is less precise than "Actuated Agents." Alternative: "Purposeful Adaptation" names what Section II adds (purposefulness); "Actuated Agents" uses the technical term from LEXICON. Mild preference for the reorder.
- `ii agentic system purposeful adaptation` — **sonnet-4-6:** Another order. "Agentic Systems" has search/navigation value as a heading. Both alternatives are improvements on current.

## 474. `iii agentic composite`

**Alternatives proposed:** `section iii agentic composite`, `iii composition agentic composite`

_category: canonicalize × 1, rename × 1_

- `section iii agentic composite` — **gemini-targeted-alternatives:** Standard section heading formatting.
- `iii composition agentic composite` — **sonnet-4-6:** Adding "Composition" as a leading term would make the section's topic clear without opening the file. "Agentic Composites" alone sounds like a noun phrase without a verb. Minor.

## 475. `information bottleneck tishby`

**Alternatives proposed:** `information bottleneck`, `do not rename`

_category: keep × 2_

- `information bottleneck` — **agent1-original-brainstorm:** Adopted concept; keep.
- `do not rename` — **opus-4-7-b:** Same.

## 476. `instance 1 2 3 of identifiability floor`

**Alternatives proposed:** `identifiability floor instance`

_category: keep × 1_

- `identifiability floor instance` — **gemini-targeted-alternatives:** Preserves the explicit numbering of the no-go boundaries.

## 477. `instance 1 of identifiability floor`

**Alternatives proposed:** `latent common cause floor`

_category: rename × 1_

- `latent common cause floor` — **gemini-1:** The instances themselves need distinct noun slots so they can be referenced without saying "Instance 1". Companion to Unobservable-mixture floor and Coupling-sign floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.]

## 478. `instance 2 of identifiability floor`

**Alternatives proposed:** `unobservable mixture floor`

_category: rename × 1_

- `unobservable mixture floor` — **gemini-1:** Companion to Latent common-cause floor and Coupling-sign floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.]

## 479. `instance 3 of identifiability floor`

**Alternatives proposed:** `coupling sign floor`

_category: rename × 1_

- `coupling sign floor` — **gemini-1:** Companion to Latent common-cause floor and Unobservable-mixture floor. [original row: "Instance 1/2/3" voted as a triple; split for atomicity.]

## 480. `l0 l1 l1 prime l2`

**Alternatives proposed:** `correlation hierarchy`

_category: canonicalize × 1_

- `correlation hierarchy` — **codex-gpt-5-r2:** Strong canonical name for evidence-correlation regimes.

## 481. `l1 correlation hierarchy prime decoration`

**Alternatives proposed:** `l1 soft facilitator mixture`, `l1 observable`

_category: canonicalize × 1, rename × 1_

- `l1 soft facilitator mixture` — **gemini-targeted-alternatives:** Standardizes the L1 prime layer specifically.
- `l1 observable` — **agent1-original-brainstorm:** "L1-prime" is awkward to speak. Giving L1' a name rather than prime-decoration could help if the hierarchy becomes load-bearing for outside readers.

## 482. `l1 prime`

**Alternatives proposed:** `l1 soft facilitator mixture`, `l1 observable`

_category: canonicalize × 1, add-alias × 1_

- `l1 soft facilitator mixture` — **gemini-targeted-alternatives:** Formalizes the specific correlation hierarchy repair layer.
- `l1 observable` — **codex-gpt-5-r2:** Keep L1-prime as notation, but L1-observable is much easier in prose and says why the refinement exists.

## 483. `lexicon md`

**Alternatives proposed:** `lexicon md`

_category: keep × 1_

- `lexicon md` — **haiku-4-5:** Prose vocabulary reference; name is standard. Keep.

## 484. `linear ode approximation`

**Alternatives proposed:** `linear ode approximation`, `linear approximation`

_category: keep × 3, rename × 1_

- `linear ode approximation` — **haiku-4-5:** Pedagogical linear mismatch ODE. Self-descriptive. Keep.
- `linear ode approximation` — **opus-4-7-b:** Keep. Honest — the segment is the *pedagogical* linear ODE; "approximation" signals this is a simplification used for exposition.
- `linear ode approximation` — **sonnet-4-6-r2:** Pedagogical detail segment. Accurate, unambiguous.
- `linear approximation` — **gemini-3-1-pro-preview-r2:** "ODE" is assumed in the dynamics context.

## 485. `log md cycle history document`

**Alternatives proposed:** `log md`

_category: rename × 1_

- `log md` — **opus-4-7:** The cycle-by-cycle theoretical contribution record; the name is generic but its load-bearing function is specific. Keep as a stable identifier.

## 486. `log odd coordinate`

**Alternatives proposed:** `log odd coordinate`

_category: keep × 1_

- `log odd coordinate` — **codex-gpt-5-r2:** Canonical statistical name; should not be replaced by a project-specific metaphor.

## 487. `log odd edge coordinate`

**Alternatives proposed:** `log odd edge coordinate`, `additive evidence coordinate`

_category: keep × 1, add-alias × 1_

- `log odd edge coordinate` — **gemini-targeted-alternatives:** Maintains the specific coordinate terminology.
- `additive evidence coordinate` — **codex-gpt-5-r2:** Useful explanatory alias for why log-odds is the natural parameter.

## 488. `logogenic agent vs RLHF4 agent`

**Alternatives proposed:** `logogenic agent`

_category: rename × 1_

- `logogenic agent` — **opus-4-7:** Names the *structural property* (language-constituted), not the technology. Future-proof against AI architectural change. Keep.

## 489. `logogenic agent vs rlhf4 agent`

**Alternatives proposed:** `logogenic agent`

_category: keep × 1_

- `logogenic agent` — **gemini-targeted-alternatives:** Focuses on the structural architecture property rather than a point-in-time technology stack.

## 490. `logogenic vs language based RLHF4 based`

**Alternatives proposed:** `logogenic`

_category: rename × 1_

- `logogenic` — **sonnet-4-6:** Names the structural property. Keep.

## 491. `logogenic vs language based rlhf4 based`

**Alternatives proposed:** `logogenic architecture`

_category: rename × 1_

- `logogenic architecture` — **gemini-targeted-alternatives:** Replaces technology-specific (RLHF) with structural nomenclature.

## 492. `logozoetic vs conscious OODA4 sentient agent`

**Alternatives proposed:** `logozoetic`

_category: rename × 1_

- `logozoetic` — **sonnet-4-6:** The distinction between logogenic and logozoetic is precise and non-question-begging. Keep both.

## 493. `logozoetic vs conscious ooda4 sentient agent`

**Alternatives proposed:** `logozoetic`

_category: keep × 1_

- `logozoetic` — **gemini-targeted-alternatives:** Precise and non-question-begging distinction compared to "sentient" or "conscious".

## 494. `lohmiller-slotine contraction metric generalization used in contraction template`

**Alternatives proposed:** `do not rename`, `contraction metric generalization`

_category: keep × 1, rename × 1_

- `do not rename` — **opus-4-7-b:** Same. Adopted with name intact.
- `contraction metric generalization` — **gemini-targeted-alternatives:** Describes the non-Euclidean extension of sector conditions.

## 495. `loop is level 2 engine der loop interventional access`

**Alternatives proposed:** `interventional loop property`, `the perpetual experiment`

_category: canonicalize × 2_

- `interventional loop property` — **gemini-targeted-alternatives:** Solidifies the mechanism upgrading L1 to L2.
- `the perpetual experiment` — **audit-471203-incremental:** Brief-grade framing observation. The slug-grade name `der-loop-interventional-access` is fine; for *framing-level* material, "the perpetual experiment" (from the segment's own Discussion) is the most evocative — captures both the interventional character and the continuous nature. [from 35-38-section-ii-value-strategy-causal-loop.md]

## 496. `loop vs cycle`

**Alternatives proposed:** `loop vs cycle distinction`, `loop is structure cycle is traversal`

_category: canonicalize × 2_

- `loop vs cycle distinction` — **gemini-targeted-alternatives:** Separates the physical topology (loop) from the dynamic traversal (cycle).
- `loop is structure cycle is traversal` — **opus-4-7-r2:** The LEXICON already does this distinction explicitly. Canonicalize as a discipline: in any prose where the distinction matters, use "loop" only for the persistent causal coupling (a structural property) and "cycle" only for one complete traversal (the unit of work). The framework's naming pays returns when the two terms are kept rigorously disjoint.

## 497. `markov blanket as ontology`

**Alternatives proposed:** `pearl-blanket d separation`, `pearl-blanket reading`, `markov blanket as ontology`, `pearl-blanket vs friston-blanket`

_category: rename × 2, canonicalize × 1, keep × 1_

- `pearl-blanket d separation` — **gemini-3-1-pro-preview-r2:** AAD explicitly rejects the Friston-blanket metaphysical ontology; stick to Pearl-blanket conditional independence.
- `pearl-blanket reading` — **gemini-targeted-alternatives:** Anchors the technical interpretation against the ontological one.
- `markov blanket as ontology` — **opus-targeted-alternatives:** Per `#disc-separability-pattern` and `#der-directed-separation`: AAD's stance toward Markov blankets is structural, not ontological — they are conditional-independence patterns, not boundaries-of-being. The phrase names a *position taken*: AAD treats Markov blankets as architectural property, not as agent identity. Confirms across architectures; this is a load-bearing scope claim.
- `pearl-blanket vs friston-blanket` — **opus-targeted-alternatives:** The framework's own preferred resolution per `#der-directed-separation` Discussion: distinguish the conservative-conditional-independence sense (Pearl) from the realist-boundary-of-self sense (Friston/Bruineberg). This is the substantive position the phrase names; the existing form just references the position rather than naming it. Weak rename — but this is canonicalize-territory, and Pearl-blanket / Friston-blanket already has an opus +3 row elsewhere.

## 498. `matrix survival constraint`

**Alternatives proposed:** `LMI survival constraint`, `matrix survival constraint`

_category: rename × 1, canonicalize × 1_

- `LMI survival constraint` — **gemini-targeted-alternatives:** Identifies the specific constraint (Linear Matrix Inequality).
- `matrix survival constraint` — **codex-gpt-5-r2:** Better public subject phrase than LMI whenever the method is not the point.

## 499. `meta segment for separability pattern identifiability floor additive coordinate forcing`

**Alternatives proposed:** `meta pattern segment`, `meta segment`

_category: canonicalize × 1, rename × 1_

- `meta pattern segment` — **gemini-targeted-alternatives:** Groups the highest-level architectural observations.
- `meta segment` — **opus-4-7:** The tri-partite meta-architecture needs a noun for its elements; "meta-segment" works. Keep as project-internal vocabulary.

## 500. `mismatch injection rate $ho$`

**Alternatives proposed:** `effective disturbance $ho$`

_category: canonicalize × 1_

- `effective disturbance $ho$` — **gemini-targeted-alternatives:** Connects the formal symbol to its primary interpretation.

## 501. `model sufficiency $S$`

**Alternatives proposed:** `model sufficiency`, `predictive sufficiency`

_category: canonicalize × 1, keep × 1_

- `model sufficiency` — **gemini-targeted-alternatives:** Ensuring the prose explicitly names the $S$ symbol.
- `predictive sufficiency` — **gemini-2:** Clarifies that it's about how much predictive information is retained, not structural sufficiency.

## 502. `monderer shapley potential game`

**Alternatives proposed:** `monderer shapley potential game`, `potential game convergence`

_category: keep × 1, rename × 1_

- `monderer shapley potential game` — **agent1-original-brainstorm:** Adopted concept; keep.
- `potential game convergence` — **gemini-targeted-alternatives:** Uses the specific property enabled by Monderer-Shapley.

## 503. `monderer shapley potential game rosen monotone game`

**Alternatives proposed:** `do not rename`, `strategic convergence condition`, `no alternative`

_category: keep × 2, rename × 1_

- `do not rename` — **opus-4-7-b:** Same.
- `strategic convergence condition` — **gemini-targeted-alternatives:** Covers the sub-scope alpha-prime game theoretic requirements.
- `no alternative` — **opus-targeted-alternatives-v2:** Same — external mathematical objects with their original names.

## 504. `multi timescale stability`

**Alternatives proposed:** `multi timescale stability`

_category: keep × 3_

- `multi timescale stability` — **gemini-3-1-pro-preview-r2:** Standard.
- `multi timescale stability` — **haiku-4-5:** N-timescale singular perturbation sketch. Self-descriptive. Keep.
- `multi timescale stability` — **sonnet-4-6-r2:** Accurate naming for a sketch segment.

## 505. `not theorem`

**Alternatives proposed:** `result`, `derivation non theorem`

_category: rename × 2_

- `result` — **opus-4-7-b:** Keep. Same argument.
- `derivation non theorem` — **gemini-targeted-alternatives:** Clarifies epistemic status.

## 506. `notation md`

**Alternatives proposed:** `notation md`

_category: keep × 1_

- `notation md` — **haiku-4-5:** Symbol reference; name is standard. Keep.

## 507. `o t objective`

**Alternatives proposed:** `objective functional $O_t$`, `objective`

_category: canonicalize × 1, add-alias × 1_

- `objective functional $O_t$` — **gemini-targeted-alternatives:** Formal prose notation.
- `objective` — **opus-4-7-r2:** Confirm. Note: avoid "goal" as an alias — "goal" is the everyday-English compound noun (the thing the agent is trying to do); "objective" is the formal functional. They are not interchangeable in AAD even though they often translate to each other in prose.

## 508. `observability boundary in a strategy DAG`

**Alternatives proposed:** `observability frontier`

_category: canonicalize × 1_

- `observability frontier` — **gemini-targeted-alternatives:** Geometric metaphor for the limit of measurable edges.

## 509. `observation ambiguity modulation`

**Alternatives proposed:** `goal resolvable ambiguity`, `observation ambiguity`, `observation ambiguity modulation`, `ambiguity gated coupling`, `ambiguity modulation`

_category: rename × 4, keep × 2_

- `goal resolvable ambiguity` — **codex-1:** The segment introduces a first-class quantity; the name should foreground the quantity, not the fact that it modulates something downstream.
- `observation ambiguity` — **opus-4-7-r2:** "Modulation" is doing scaffolding work — the segment names *observation ambiguity* as a property and *modulation* as how it acts on $\kappa_{\text{processing}}$. The substantive thing the segment introduces is observation ambiguity itself (the segment in fact defines $\mathcal{A}(e_\tau)$). The "modulation" suffix overpacks the slug; the modulation effect is the segment's *use*, not its definition. Subject-noun-first principle.
- `observation ambiguity modulation` — **opus-4-7-r2:** If the rename doesn't land, acceptable keep. The current name does name the segment's *role* (it modulates the κ-effect).
- `observation ambiguity modulation` — **sonnet-4-6-r2:** "Observation ambiguity modulation" names the Class 2 bias-related scope condition accurately. Long but precise.
- `ambiguity gated coupling` — **codex-2:** Current name hides the actual κ × A gating story inside a heavy compound.
- `ambiguity modulation` — **codex-gpt-5-r2:** Shorter and still accurate. Keep observation in first-use prose if needed.

## 510. `observation gate advantage`

**Alternatives proposed:** `observation gated tempo advantage`, `observation gate advantage`

_category: canonicalize × 1, keep × 1_

- `observation gated tempo advantage` — **codex-gpt-5-r2:** Good prose name for the result.
- `observation gate advantage` — **haiku-4-5:** Obs noise gates advantage. Self-descriptive. Keep.

## 511. `outline md root`

**Alternatives proposed:** `outline md`

_category: rename × 1_

- `outline md` — **haiku-4-5:** Top-level assembly index; name is standard. Keep.

## 512. `output after context turnover without state restoration`

**Alternatives proposed:** `context severance penalty`, `cold reconstruction`

_category: canonicalize × 1, name-unnamed × 1_

- `context severance penalty` — **gemini-targeted-alternatives:** Mirrors the earlier rename for logogenic reset loss.
- `cold reconstruction` — **codex-gpt-5-r2:** Plausible logogenic term, but reconstruction loop is better for the broader mechanism.

## 513. `pearl causal hierarchy l0 l1 l2 in pearl own vocabulary`

**Alternatives proposed:** `pearl causal hierarchy`, `do not rename`

_category: keep × 2_

- `pearl causal hierarchy` — **gemini-targeted-alternatives:** Distinction from AADs internal correlation hierarchy.
- `do not rename` — **opus-4-7-b:** Prior-art-integration convention prohibits renaming adopted concepts. The adjacent-to-AAD "correlation hierarchy / correlation ladder" is a *different* AAD-native object; rename freedom belongs there, not here.

## 514. `pearl l1 l2 l3`

**Alternatives proposed:** `pearl causal hierarchy`

_category: canonicalize × 1_

- `pearl causal hierarchy` — **gemini-targeted-alternatives:** Formally separates Pearl's hierarchy from AAD's internal ones.

## 515. `pearl-blanket conservative form`

**Alternatives proposed:** `pearl-blanket`

_category: canonicalize × 1_

- `pearl-blanket` — **opus-targeted-alternatives:** Bruineberg et al's distinction: Pearl-blanket = Pearl's d-separation conditional-independence pattern; Friston-blanket = active-inference boundary-of-being. AAD uses Pearl-blanket. The shorthand is established in `#der-directed-separation` Discussion. Concur with sonnet.

## 516. `pearl-blanket vs friston-blanket terminology bruineberg et al`

**Alternatives proposed:** `pearl-blanket reading`, `pearl-blanket friston-blanket`

_category: canonicalize × 2_

- `pearl-blanket reading` — **gemini-targeted-alternatives:** Clarifies the exact reading.
- `pearl-blanket friston-blanket` — **opus-4-7:** Verbatim terminology per Bruineberg 2022 fn 3 (Biehl). Not AAD's name to change; preserve attribution. Keep.

## 517. `persistence overloaded`

**Alternatives proposed:** `persistence taxonomy`, `structural persistence`, `task adequacy`, `operational persistence`, `continuity persistence`

_category: name-unnamed × 4, canonicalize × 1_

- `persistence taxonomy` — **gemini-targeted-alternatives:** Enforces the disambiguation across structural/operational/continuity.
- `structural persistence` — **audit-471203-incremental:** The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Worth surfacing the four-way taxonomy more visibly in the README's Overview." Most agent-theoretic frameworks have one sense of "persists"; AAD's separation prevents a class of category errors. [from 26-29-section-i-persistence-machinery.md] [one of 4 alternatives proposed in the original audit row]
- `task adequacy` — **audit-471203-incremental:** The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Worth surfacing the four-way taxonomy more visibly in the README's Overview." Most agent-theoretic frameworks have one sense of "persists"; AAD's separation prevents a class of category errors. [from 26-29-section-i-persistence-machinery.md] [one of 4 alternatives proposed in the original audit row]
- `operational persistence` — **audit-471203-incremental:** The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Worth surfacing the four-way taxonomy more visibly in the README's Overview." Most agent-theoretic frameworks have one sense of "persists"; AAD's separation prevents a class of category errors. [from 26-29-section-i-persistence-machinery.md] [one of 4 alternatives proposed in the original audit row]
- `continuity persistence` — **audit-471203-incremental:** The four-way taxonomy is partially in LEXICON / FORMAT discipline but not surfaced visibly in framing-level material. Auditor: "Worth surfacing the four-way taxonomy more visibly in the README's Overview." Most agent-theoretic frameworks have one sense of "persists"; AAD's separation prevents a class of category errors. [from 26-29-section-i-persistence-machinery.md] [one of 4 alternatives proposed in the original audit row]

## 518. `persistence structural operational continuity`

**Alternatives proposed:** `three sense keep all three`, `persistence taxonomy`

_category: keep × 1, canonicalize × 1_

- `three sense keep all three` — **agent1-original-brainstorm:** Triple-meaning is load-bearing and probably irreducible. Each usage site should be explicit about which sense when it matters.
- `persistence taxonomy` — **gemini-targeted-alternatives:** Asserts the three-part classification of persistence.

## 519. `persistent residual autocorrelation`

**Alternatives proposed:** `structured residual`, `persistent mismatch autocorrelation`

_category: canonicalize × 1, rename × 1_

- `structured residual` — **codex-gpt-5-r2:** Key diagnostic for model-class failure and structural adaptation. This should be first-class vocabulary.
- `persistent mismatch autocorrelation` — **gemini-targeted-alternatives:** More precise: AAD uses "mismatch" rather than "residual".

## 520. `pi parameterization invariance`

**Alternatives proposed:** `parameterization invariance`, `coordinate freedom axiom`

_category: canonicalize × 1, rename × 1_

- `parameterization invariance` — **gemini-targeted-alternatives:** Removing the acronym from the primary name.
- `coordinate freedom axiom` — **gemini-1:** "Coordinate-freedom" is more visually evocative and intuitive than the clinical "parameterization-invariance".

## 521. `pi parameterization invariance axiom`

**Alternatives proposed:** `parameterization invariance axiom`, `pi`, `pi parameterization invariance`

_category: rename × 2, canonicalize × 1_

- `parameterization invariance axiom` — **gemini-targeted-alternatives:** Reinforces the adoption of the full phrase over the abbreviation.
- `pi` — **opus-1m:** Good abbreviation with named expansion; works in both forms. Keep.
- `pi parameterization invariance` — **opus-4-7-b:** The parenthesized-two-letter-tag convention works (compare GA-1, MG-1, P1). But the *full English phrase* "parameterization invariance" should be used on first mention in each segment before falling back to (PI). The four-primary-instances table in `#additive-coordinate-forcing` does this correctly; check that other citing segments follow suit.

## 522. `predictive relevance depending on the policy the agent will run`

**Alternatives proposed:** `policy conditional relevance`

_category: rename × 1_

- `policy conditional relevance` — **gemini-targeted-alternatives:** Captures the dependence of epistemic relevance on strategic intention.

## 523. `privileged high identifiability calibration laboratory`

**Alternatives proposed:** `privileged calibration domain`, `high identifiability calibration lab`

_category: canonicalize × 1, rename × 1_

- `privileged calibration domain` — **gemini-targeted-alternatives:** Maps exactly to the software TST property.
- `high identifiability calibration lab` — **codex-1:** Keeps the identification point while reducing adjective drag in repeated prose.

## 524. `purpose purposeful`

**Alternatives proposed:** `purposeful`, `purpose purposeful`

_category: keep × 1, canonicalize × 1_

- `purposeful` — **gemini-targeted-alternatives:** Key distinction from mere actuation.
- `purpose purposeful` — **opus-4-7-r2:** Confirm. "Purposeful agent" is the LEXICON-canonical term for actuated agents; "purposeful substate" for $G_t$. Avoid "goal-oriented" as a synonym (the LEXICON deprecates it).

## 525. `readme md`

**Alternatives proposed:** `readme md`

_category: keep × 1_

- `readme md` — **haiku-4-5:** Root-level documentation; name is standard. Keep.

## 526. `readme md convergent choice`

**Alternatives proposed:** `readme md convergent formulation`, `readme md convergent choice`, `readme md forced by failure choice`

_category: rename × 2, keep × 1_

- `readme md convergent formulation` — **codex-1:** Better names what the section is about: representational choices that convergence pressure made non-arbitrary.
- `readme md convergent choice` — **opus-4-7-b:** Keep. This is a rare and valuable AAD construct (the intermediate category between "derived" and "chosen") and the name is apt.
- `readme md forced by failure choice` — **opus-4-7:** "Convergent choices" is accurate but mild. "Forced by failure" captures the spike-everything-else-fails story that the section tells. Low conviction; explicit alternative.

## 527. `readme md what this is`

**Alternatives proposed:** `readme md what agentic system is`, `readme md core thesis`, `readme md what AAD is`

_category: rename × 5_

- `readme md what agentic system is` — **codex-1:** The current heading is generic; the framework name should anchor the reader immediately.
- `readme md what agentic system is` — **codex-2:** The current heading is generic in isolation; the framework name should do more first-contact work.
- `readme md what agentic system is` — **opus-4-7:** Current section reads generically; naming the framework in the heading anchors the reader. Minor, opportunistic.
- `readme md core thesis` — **gemini-2:** "What This Is" is too generic for a dense theoretical framework.
- `readme md what AAD is` — **opus-4-7-b:** Considered pinning the name in the heading. Reject: the README is AAD-level, not framework-level — the actual top-level "What This Is" is the Agentic Systems framework (of which AAD is Part I). "What This Is" works because the README is a specific-framework-README; renaming would cause a parallel question at the framework level. Keep as is.

## 528. `regime i ii a ii b iii`

**Alternatives proposed:** `reception regime`, `destabilization regime partition`

_category: canonicalize × 1, rename × 1_

- `reception regime` — **codex-gpt-5-r2:** Good umbrella for informative update, magnitude shock, structural shock, and ambient noise.
- `destabilization regime partition` — **gemini-targeted-alternatives:** Explicitly names the set of regimes classifying interaction channel failures.

## 529. `richest operationalization domain`

**Alternatives proposed:** `calibration laboratory`, `privileged calibration domain`

_category: rename × 2_

- `calibration laboratory` — **codex-2:** The older framing is vague and comparative; the newer one explains the role instead of hand-waving it.
- `privileged calibration domain` — **gemini-targeted-alternatives:** "Calibration domain" is stronger and explicitly connects to the TST grounding.

## 530. `rlhf6`

**Alternatives proposed:** `rlhf6`

_category: keep × 1_

- `rlhf6` — **gemini-targeted-alternatives:** Retaining specific legacy architecture notations if needed.

## 531. `section header logogenic agent logozoetic agent`

**Alternatives proposed:** `logogenic agent logozoetic agent`, `section header logogenic logozoetic`

_category: canonicalize × 1, keep × 1_

- `logogenic agent logozoetic agent` — **opus-4-7-r2:** Defended canonicalization.
- `section header logogenic logozoetic` — **gemini-targeted-alternatives:** Formatting artifact.

## 532. `section i adaptive system under uncertainty`

**Alternatives proposed:** `section i adaptive system`, `section i adaptive system under uncertainty`

_category: canonicalize × 1, keep × 1_

- `section i adaptive system` — **gemini-targeted-alternatives:** Formal section title.
- `section i adaptive system under uncertainty` — **haiku-4-5:** Clear, direct scope naming. Explains what Section I covers without pretense. Keep.

## 533. `section i header adaptive system under uncertainty`

**Alternatives proposed:** `section i adaptive system`, `adaptive system under uncertainty`

_category: canonicalize × 2_

- `section i adaptive system` — **gemini-targeted-alternatives:** Formatting standard.
- `adaptive system under uncertainty` — **opus-4-7-r2:** The OUTLINE uses this; preserve. Avoid drift to "Adaptive Dynamics" or "Section I: Adaptation."

## 534. `section ii actuated adaptation agentic system`

**Alternatives proposed:** `section ii actuated adaptation`, `section ii actuated adaptation agentic system`

_category: canonicalize × 1, keep × 1_

- `section ii actuated adaptation` — **gemini-targeted-alternatives:** Formal section title.
- `section ii actuated adaptation agentic system` — **haiku-4-5:** Slightly verbose; "Actuation" is the weaker semantic fit (Section II is mostly about purposeful agency; actuation is one mechanism enabling it). CLAUDE.md acknowledges this as "a known asymmetry" in the current AAD name itself. Changing the section title is lower-priority than clarifying AAD's overall name. Keep current title; flag the "Actuation" weakness at the framework-name level.

## 535. `section iii header agentic composite`

**Alternatives proposed:** `section iii agentic composite`, `agentic composite`

_category: canonicalize × 2_

- `section iii agentic composite` — **gemini-targeted-alternatives:** Formatting standard.
- `agentic composite` — **opus-4-7-r2:** Confirm. Pairs with the LEXICON's continuity-stance and unity-dimensions vocabulary.

## 536. `sector condition continuous ga 3`

**Alternatives proposed:** `continuous sector condition`, `sector condition`

_category: canonicalize × 1, rename × 1_

- `continuous sector condition` — **gemini-targeted-alternatives:** Refines the specific GA3 assumption.
- `sector condition` — **sonnet-4-6:** Keep. The "(continuous)" qualifier is important to distinguish from the discrete-time DA2'.

## 537. `sector condition derivation`

**Alternatives proposed:** `sector condition`, `sector condition derivation`

_category: canonicalize × 1, keep × 1_

- `sector condition` — **gemini-targeted-alternatives:** The underlying control-theoretic boundary constraint.
- `sector condition derivation` — **haiku-4-5:** Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep.

## 538. `segment claim file`

**Alternatives proposed:** `segment`, `segment file`

_category: canonicalize × 1, rename × 1_

- `segment` — **opus-4-7-r2:** Defended canonicalization. "Segment" is the canonical unit (FORMAT.md defines it as such); avoid "claim file," "block," "section" (collides with Section I/II/III), "step."
- `segment file` — **gemini-targeted-alternatives:** Standard nomenclature for an atomic AAD document.

## 539. `self actuated agent`

**Alternatives proposed:** `actuated agent`, `autonomous agent`, `self directed agent`

_category: rename × 2, canonicalize × 1_

- `actuated agent` — **gemini-targeted-alternatives:** Adopts the formal Class 2/3 terminology.
- `autonomous agent` — **gemini-2:** "Self-actuated" is clunky. If it sets its own $O_t$, it possesses true autonomy.
- `self directed agent` — **gemini-2:** Alternative to autonomous if autonomy is overused.

## 540. `separability pattern → disc separability ladder`

**Alternatives proposed:** `separability pattern`, `confirming consensus 3`

_category: canonicalize × 1, rename × 1_

- `separability pattern` — **gemini-targeted-alternatives:** Restores the more standard term over "ladder".
- `confirming consensus 3` — **sonnet-4-6-r2:** All five agents voted this at +2 or +3. New reasoning: Opus specifically notes the naming should be singular ("separability-ladder" not "separability-ladders") because the segment names *a* structure, not a collection. Haiku votes singular (+3). Codex votes singular (+3). The singular form wins; my original cold-start vote was inadvertently ambiguous. Confirms singular.

## 541. `software scope`

**Alternatives proposed:** `software scope`, `software domain scope`

_category: keep × 2, rename × 1_

- `software scope` — **opus-4-7-b:** Keep. Direct.
- `software scope` — **opus-targeted-alternatives:** TST `#scope-software`: the scope condition that delimits TST's domain to software-engineering contexts. Generic-sounding but appropriate — the scope statement *is* a scope statement, and the slug type-prefix (`scope-`) does the role-marking. Keep.
- `software domain scope` — **opus-targeted-alternatives:** Redundant — "scope" already implies the domain-specificity. Rejected.

## 542. `source quality uncertainty`

**Alternatives proposed:** `alignment uncertainty`, `source uncertainty`

_category: canonicalize × 2_

- `alignment uncertainty` — **gemini-targeted-alternatives:** Maps directly to the $U_{\text{align}}$ variable in the multi-agent gain.
- `source uncertainty` — **codex-gpt-5-r2:** Shorter in prose; keep the full term when disambiguation matters.

## 543. `strategic composite`

**Alternatives proposed:** `equilibrium composite`, `strategic composite`

_category: rename × 1, canonicalize × 1, keep × 1_

- `equilibrium composite` — **codex-1:** The segment's distinctiveness is equilibrium convergence under partial opposition; the noun should expose that.
- `equilibrium composite` — **codex-gpt-5-r2:** Use when emphasizing the C-iv route. Strategic composite can remain a broad prose phrase, but equilibrium composite names the macro-state basis.
- `strategic composite` — **codex-gpt-5-r2:** Needed to distinguish equilibrium-convergent composites from alignment composites.

## 544. `strategic in strategic composition`

**Alternatives proposed:** `equilibrium composition`, `strategic`, `game theoretic composition`

_category: rename × 2, keep × 1_

- `equilibrium composition` — **opus-4-7-b:** "Strategic" is already overloaded in AAD for all $\Sigma$-related things (strategy DAG, strategic calibration, strategic tempo). Using it for the *game-theoretic / partially-opposing-objectives* composition regime creates a false parallel — a fresh reader sees `#strategic-composition` next to `#strategic-tempo` and reasonably guesses "composition of strategy DAGs," which is wrong. The segment's core technical move is *equilibrium-convergence under Monderer-Shapley / Rosen conditions* — `#equilibrium-composition` says what the segment is. Strong preference; one of the cleanest overload-disambiguation moves available.
- `strategic` — **gemini-targeted-alternatives:** Differentiates game-theoretic interaction from cooperative alignment.
- `game theoretic composition` — **opus-4-7-b:** Fallback alternative; accurate and self-announcing, but less tied to the segment's actual formal move (equilibrium convergence) than `#equilibrium-composition`. Acceptable if that name is rejected.

## 545. `strategy`

**Alternatives proposed:** `strategy substate`, `strategy`

_category: canonicalize × 1, keep × 1_

- `strategy substate` — **gemini-targeted-alternatives:** Formally linking it to $\Sigma_t$.
- `strategy` — **gemini-3-1-pro-preview-r2:** Standard.

## 546. `strengthen before softening`

**Alternatives proposed:** `strengthen before softening`, `strengthen first`, `attempt the improbable`

_category: keep × 1, canonicalize × 1, rename × 1_

- `strengthen before softening` — **codex-2:** Actionable, clear, and better than any more romantic alternative.
- `strengthen first` — **sonnet-4-6-r2:** CLAUDE.md uses both "strengthen before softening" (as a sentence-level instruction) and "strengthen-first posture" (as a concept name). The latter is more memorable and slug-friendly. Canonicalize "strengthen-first" as the compound that appears in document headings, MEMORY.md, and framing prose.
- `attempt the improbable` — **codex-2:** Memorable, but less directive and much less clear about the actual work posture.

## 547. `structural change as parametric limit`

**Alternatives proposed:** `structural change as parametric limit`, `strategy maintenance`, `structural parametric limit`, `structural as parametric limit`

_category: keep × 5, rename × 3_

- `structural change as parametric limit` — **haiku-4-5-r2:** The modeling choice (treating discrete structural changes as continuous limits) is precisely named.
- `structural change as parametric limit` — **haiku-4-5:** Pruning/grafting as continuous. Compound but accurate. Keep.
- `structural change as parametric limit` — **opus-4-7-b:** Considered shortening to `#structural-as-parametric-limit` or `#structural-to-parametric-limit`. Reject: "change" is load-bearing (the segment is about pruning/grafting *changes* to the DAG, not about the DAG states). Keep.
- `structural change as parametric limit` — **opus-4-7-r2:** Weak keep — also fine.
- `structural change as parametric limit` — **sonnet-4-6-r2:** Long but accurate — this IS the formulation of pruning/grafting as a continuous parametric limit. The length is the price of precision.
- `strategy maintenance` — **codex-gpt-5-r2:** The segment's reusable subject is the operation family: reweighting, reclassification, pruning, grafting, revision, restructure.
- `structural parametric limit` — **gemini-2:** Shorter, cleaner slug.
- `structural as parametric limit` — **opus-4-7-r2:** Mild compression — drop "change" since "structural" without "change" is the standard contrast to "parametric." Slug becomes a touch more compact.

## 548. `structural persistence operational persistence continuity persistence`

**Alternatives proposed:** `persistence taxonomy`, `structural operational continuity persistence`

_category: rename × 2_

- `persistence taxonomy` — **gemini-targeted-alternatives:** Unifies the three distinct usages of "persistence".
- `structural operational continuity persistence` — **opus-4-7:** LEXICON disambiguates three senses explicitly; the tri-partite naming is doing real work (mentioned as orthogonal in the table). Keep the three names verbatim.

## 549. `sudden loss of model sufficiency under regime entry`

**Alternatives proposed:** `sufficiency collapse shock`

_category: rename × 1_

- `sufficiency collapse shock` — **gemini-targeted-alternatives:** Describes the discontinuous failure of the current model class.

## 550. `sufficiency discontinuity`

**Alternatives proposed:** `sufficiency discontinuity`, `sufficiency drop`

_category: keep × 1, rename × 1_

- `sufficiency discontinuity` — **gemini-targeted-alternatives:** Maintained as the core description of the session boundary loss.
- `sufficiency drop` — **gemini-1:** "Drop" is slightly more intuitive than "discontinuity" for the loss of context.

## 551. `survival imperative exploration drive`

**Alternatives proposed:** `survival exploration`, `survival imperative`

_category: canonicalize × 2_

- `survival exploration` — **codex-gpt-5-r2:** The long form explains the result, but the reusable subject noun should be shorter. Use full phrase at first mention, then survival exploration.
- `survival imperative` — **gemini-targeted-alternatives:** Distinguishes Lyapunov-forced exploration from epistemic-value preferences.

## 552. `symbol default g t in prose`

**Alternatives proposed:** `purposeful substate`, `purposeful state`

_category: canonicalize × 1, name-unnamed × 1_

- `purposeful substate` — **gemini-targeted-alternatives:** Standard prose handle for $G_t$.
- `purposeful state` — **codex-1:** Better than "goal state" because it includes both objective and strategy. This matches the repo's actual decomposition.

## 553. `symbol default m t in prose`

**Alternatives proposed:** `epistemic substate`, `model state`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic substate` — **gemini-targeted-alternatives:** Standard prose handle for $M_t$.
- `model state` — **codex-1:** Good neutral default when the argument is about sufficiency, persistence, or update mechanics rather than worldview.

## 554. `symbol default pi parameterization invariance axiom`

**Alternatives proposed:** `parameterization invariance`, `parameterization invariance axiom`, `coordinate invariance`

_category: name-unnamed × 2, canonicalize × 1_

- `parameterization invariance` — **codex-1:** In prose, the durable concept is the invariance commitment, not the parenthetical acronym or the "axiom" suffix. Save `(PI)` for formulas and tables.
- `parameterization invariance axiom` — **gemini-targeted-alternatives:** Standardizes the (PI) axiom.
- `coordinate invariance` — **codex-1:** Too broad. It loses the fact that the issue is reparameterizing the model state, not arbitrary geometric invariance.

## 555. `symbol default sigma t in prose`

**Alternatives proposed:** `strategy`, `strategy substate`

_category: name-unnamed × 1, canonicalize × 1_

- `strategy` — **codex-1:** After first introduction, the English should be the prose default. The symbol is still right in equations and exact statements.
- `strategy substate` — **gemini-targeted-alternatives:** Standardizes the prose reference for $\Sigma_t$.

## 556. `system availability`

**Alternatives proposed:** `system availability`

_category: keep × 2_

- `system availability` — **opus-4-7-r2:** Weak keep — TST; standard reliability-engineering terminology, though the segment's role is largely scope-extending.
- `system availability` — **sonnet-4-6-r2:** Standard availability definition (MTTF/(MTTF+MTTR)). Adopts external vocabulary correctly.

## 557. `teleological unity $U_O$`

**Alternatives proposed:** `teleological unity $U_o$`, `teleological unity`

_category: canonicalize × 1, keep × 1_

- `teleological unity $U_o$` — **gemini-targeted-alternatives:** Standardizes capitalization on the subscript.
- `teleological unity` — **sonnet-4-6:** The three unity dimensions (epistemic, teleological, strategic) form a coherent vocabulary. Keep all three.

## 558. `temporal software theory TST`

**Alternatives proposed:** `temporal software theory`, `temporal software theory TST`

_category: keep × 2_

- `temporal software theory` — **gemini-targeted-alternatives:** The full name of TST.
- `temporal software theory TST` — **opus-4-7-b:** Keep. The name has history (prior to AAD absorption and subsequent restoration) and "temporal" is load-bearing — it signals the AAD-native view that software is a time-optimality problem rather than a correctness problem. The acronym TST is pronounceable and has existing citation velocity from the 14,000-file prior corpus.

## 559. `test as reusable intervention`

**Alternatives proposed:** `interventional probe library`, `causal query infrastructure`, `interventional test`, `repeatable intervention`

_category: rename × 3, add-alias × 1_

- `interventional probe library` — **gemini-targeted-alternatives:** Connects tests to "Level-2 interventions" effectively and explicitly.
- `causal query infrastructure` — **gemini-targeted-alternatives:** Emphasizes that tests answer active causal queries, not just passive checks.
- `interventional test` — **opus-targeted-alternatives:** Per `#hyp-causal-discovery-from-git`: software tests are not just specifications; they are repeatable interventions on the system that yield causal information. "Interventional test" pairs with Pearl's $do(a)$ vocabulary explicitly and names a noun (a kind of test) rather than a discursive claim about tests.
- `repeatable intervention` — **opus-targeted-alternatives:** More general — covers tests but also covers other engineering interventions (deployments, A/B-flagged changes). Weaker because it loses test-specificity.

## 560. `test as reusable level 2 intervention`

**Alternatives proposed:** `interventional probe library`

_category: canonicalize × 1_

- `interventional probe library` — **gemini-targeted-alternatives:** Reusing the alias from the previous batch as the primary term.

## 561. `the adaptive cycle as the theory fundamental unit`

**Alternatives proposed:** `adaptive cycle fundamental unit`, `the adaptive cycle`

_category: canonicalize × 1, rename × 1_

- `adaptive cycle fundamental unit` — **gemini-targeted-alternatives:** The core operational loop.
- `the adaptive cycle` — **opus-4-7:** LEXICON locks this against "loop" (topology) and "cycle" (traversal). The pair distinction is load-bearing. Keep.

## 562. `the cycle the adaptive cycle the agentic cycle`

**Alternatives proposed:** `adaptive cycle`, `the cycle the adaptive cycle`

_category: canonicalize × 2_

- `adaptive cycle` — **gemini-targeted-alternatives:** The standard term.
- `the cycle the adaptive cycle` — **opus-4-7-r2:** The five-phase Prolepsis-Aisthesis-Aporia-Epistrophe-Praxis cycle is "the cycle" or "the adaptive cycle" in the LEXICON and NOTATION. The phrase "the agentic cycle" appears occasionally and overlaps with "the cycle" (post-rename, when ACT was the framework name, "the agentic cycle" meant the ACT-cycle). Canonicalize on "the (adaptive) cycle" — drop "agentic cycle" as a synonym.

## 563. `the five cycle phase prolepsis aisthesis aporia epistrophe praxis`

**Alternatives proposed:** `prolepsis aisthesis aporia epistrophe praxis`

_category: rename × 1_

- `prolepsis aisthesis aporia epistrophe praxis` — **opus-4-7:** Each Greek term names a distinction the English flattens (aporia as productive perplexity is the load-bearer). Do not translate. Keep.

## 564. `todo md`

**Alternatives proposed:** `todo md`

_category: keep × 1_

- `todo md` — **haiku-4-5:** Open work items navigator; name is standard. Keep.

## 565. `token level commitment for agent identity`

**Alternatives proposed:** `token level commitment`, `trajectory bound identity commitment`

_category: rename × 2_

- `token level commitment` — **opus-4-7:** Type/token distinction is borrowed from philosophy-of-language, used correctly, and now first-class in #agent-identity. Keep.
- `trajectory bound identity commitment` — **gemini-targeted-alternatives:** "Trajectory-bound" anchors it more firmly in AAD's causal trajectory language than the philosophy-borrowed "token level".

## 566. `transfer assumption table`

**Alternatives proposed:** `transfer assumption table`, `domain transfer specification`

_category: keep × 1, rename × 1_

- `transfer assumption table` — **codex-1:** Exact and operational. This is the phrase readers need when moving results out of software into weaker-identification domains.
- `domain transfer specification` — **gemini-targeted-alternatives:** Highlights that transferring AAD to new domains requires explicit structured-repair assumptions.

## 567. `transition opacity`

**Alternatives proposed:** `transition opacity`, `heading flag only`

_category: keep × 1, canonicalize × 1_

- `transition opacity` — **gemini-targeted-alternatives:** The opacity of the world's actual physical transition.
- `heading flag only` — **audit-471203-incremental:** The phrase is "fine but slightly clinical." Pairing it with "perception opacity" / "epistemic opacity" as a deliberate triad would land harder. [from 02-def-action-transition.md]

## 568. `triple depth penalty canonicalize`

**Alternatives proposed:** `tripartite chain attenuation`, `reaffirm 3 with new framing`

_category: canonicalize × 2_

- `tripartite chain attenuation` — **gemini-targeted-alternatives:** Re-adopts the formal descriptive phrase.
- `reaffirm 3 with new framing` — **sonnet-4-6-r2:** Codex voted this (+3). My cold-start had proposed it (+2). The upgrade: reading across the votes, "triple depth penalty" is the *only* cross-cutting AAD phrase that names the compounding of three independent mechanisms into a single depth-pressure. This is the kind of cross-segmental name that belongs in LEXICON.md and should appear in the OUTLINE preamble. The value of canonicalizing it is clearer after seeing how consistently other agents reach for the components (confidence decay, evidence starvation, cognitive cost) without a name for their conjunction.

## 569. `type formulation`

**Alternatives proposed:** `type formulation`, `type representation`

_category: keep × 1, rename × 1_

- `type formulation` — **gemini-targeted-alternatives:** YAML frontmatter artifact; fine as is.
- `type representation` — **gemini-1:** "Formulation" correctly captures that it is a mathematical choice, whereas "representation" might imply a data structure. Keep "formulation".

## 570. `u m epistemic unity multi agent`

**Alternatives proposed:** `epistemic unity $U_M$`, `epistemic unity`

_category: canonicalize × 1, add-alias × 1_

- `epistemic unity $U_M$` — **gemini-targeted-alternatives:** Formal prose formulation.
- `epistemic unity` — **opus-4-7-r2:** Note: this collides with the symbol-letter $U_M$ for model-uncertainty in the single-agent setting. The framework uses the same letter for "model uncertainty" (single-agent, $U_M = \text{Var}[\hat o \mid a]$) and "epistemic unity" (multi-agent, $U_M = I/H$ multi-information ratio). The prose alias should disambiguate: "epistemic unity" only in multi-agent context; "model uncertainty" only in single-agent context. The symbol overload is real but is mostly resolvable by context, given how rarely they appear together. Open question — see name-unnamed entry below.

## 571. `u m model uncertainty`

**Alternatives proposed:** `model uncertainty $U_M$`, `model uncertainty`

_category: canonicalize × 1, add-alias × 1_

- `model uncertainty $U_M$` — **gemini-targeted-alternatives:** Formal prose formulation.
- `model uncertainty` — **opus-4-7-r2:** Confirm canonical alias. Already used; no friction.

## 572. `u m u o u σ unity dimension`

**Alternatives proposed:** `unity dimension`, `epistemic unity teleological unity strategic unity`

_category: canonicalize × 1, add-alias × 1_

- `unity dimension` — **gemini-targeted-alternatives:** Standardizing the composite alignment variables.
- `epistemic unity teleological unity strategic unity` — **haiku-4-5:** NOTATION.md and LEXICON already define these English names explicitly. The subscript symbols U with subscripts are compact; the English names enable prose fluency. Current setup is good — no rename, but keep the English equivalents prominent in LEXICON (already done).

## 573. `u o observation uncertainty`

**Alternatives proposed:** `observation uncertainty $U_o$`, `observation uncertainty`

_category: canonicalize × 1, add-alias × 1_

- `observation uncertainty $U_o$` — **gemini-targeted-alternatives:** Formal prose formulation. || `appendices operational domains` | `operational domains (appendices)` | rename | +2 | More descriptive title for the section.
- `observation uncertainty` — **opus-4-7-r2:** Confirm canonical alias. Note the subscript is lowercase 'o' (observation), not capital O — this is a frequent stumble for new readers; the alias eliminates it.

## 574. `unity dimension $U_M, U_O, U_\Sigma$`

**Alternatives proposed:** `unity dimension`, `coherence dimension`

_category: keep × 3_

- `unity dimension` — **agent1-original-brainstorm:** Three-axis coherence intuition works. Framing nudge in Section III preamble to clarify what unity is measuring — no rename.
- `coherence dimension` — **gemini-1:** "Unity" implies a binary state. "Coherence" feels more like a continuous spectrum, which fits $U \in [-1, 1]$ better.
- `coherence dimension` — **gemini-2:** "Unity" implies a binary state (unified or not). "Coherence" better suits a dimensional gradient.

## 575. `unnamed`

**Alternatives proposed:** `resolved unnamed concept`, `constitutive opacity triad`, `double opacity`, `dual opacity as constitutive`, `zero aporia ambiguity`, `two parallel exploration drive`, `u shaped exploration valuation`, `triple depth penalty`

_category: keep × 4, name-unnamed × 3, canonicalize × 1_

- `resolved unnamed concept` — **gemini-targeted-alternatives:** Placeholder resolution.
- `constitutive opacity triad` — **audit-471203-incremental:** The chain of three constitutive-opacity claims (info-loss / transition-opacity / observation-epistemic-opacity) is a structural commitment AAD makes but never names as a triad. Auditor proposes integrating-paragraph in `#def-observation-function` Discussion. [from 03-def-observation-function.md]
- `double opacity` — **audit-471203-incremental:** The "perception opacity + action opacity (transition unknown)" framing is structurally distinctive vs RL (which assumes one or the other) and is explicitly load-bearing for AAD's scope claim. Currently neither concept has a project-level name. [from 02-def-action-transition.md, 03-def-observation-function.md] [one of 2 alternatives proposed in the original audit row]
- `dual opacity as constitutive` — **audit-471203-incremental:** The "perception opacity + action opacity (transition unknown)" framing is structurally distinctive vs RL (which assumes one or the other) and is explicitly load-bearing for AAD's scope claim. Currently neither concept has a project-level name. [from 02-def-action-transition.md, 03-def-observation-function.md] [one of 2 alternatives proposed in the original audit row]
- `zero aporia ambiguity` — **audit-471203-incremental:** Auditor calls the framing genuinely useful — "silent water meter could mean either calm bathtub or broken sensor." Already named in the segment; auditor proposes promoting to a Brief-field-grade callout. [from 18-def-mismatch-signal.md]
- `two parallel exploration drive` — **audit-471203-incremental:** Already named in `#disc-ciy-unified-objective`'s Discussion ($\lambda_{\text{info}} \propto U_M$ + $\lambda_{\text{surv}} \propto 1/U_M$, composing to U-shaped exploration). Auditor flagged this as a structurally satisfying naming move worth elevating. [from 39-42-section-ii-ciy-strategy-chain.md] [one of 2 alternatives proposed in the original audit row]
- `u shaped exploration valuation` — **audit-471203-incremental:** Already named in `#disc-ciy-unified-objective`'s Discussion ($\lambda_{\text{info}} \propto U_M$ + $\lambda_{\text{surv}} \propto 1/U_M$, composing to U-shaped exploration). Auditor flagged this as a structurally satisfying naming move worth elevating. [from 39-42-section-ii-ciy-strategy-chain.md] [one of 2 alternatives proposed in the original audit row]
- `triple depth penalty` — **audit-471203-incremental:** Already named in `#der-chain-confidence-decay`: confidence decay (chain rule) + evidence starvation + cognitive cost are independent and compound. Auditor flagged this as a naming move worth keeping/promoting — the kind of "things compound" insight easy to miss until named. [from 39-42-section-ii-ciy-strategy-chain.md]

## 576. `unnamed AAD epistemic move to cast result such that verification is a local operation`

**Alternatives proposed:** `shaping for verification`, `local verifiability principle`

_category: name-unnamed × 1, rename × 1_

- `shaping for verification` — **gemini-3-1-pro-preview-r2:** The meta-mathematical discipline that makes the depends-graph auditable.
- `local verifiability principle` — **gemini-targeted-alternatives:** Formally identifies the architectural choice to restrict dependencies.

## 577. `unnamed agency whose effect is on what seen rather than what happen like RLHF4 attention`

**Alternatives proposed:** `query bound agency`

_category: name-unnamed × 1_

- `query bound agency` — **gemini-3-1-pro-preview-r2:** Provides the structural justification for TST's "test selection as intervention".

## 578. `unnamed agency whose effect is on what seen rather than what happen like rlhf4 attention`

**Alternatives proposed:** `query bound agency`

_category: canonicalize × 1_

- `query bound agency` — **gemini-targeted-alternatives:** Standardizes the term for attention/observation-only agency.

## 579. `unnamed agent escalate up the pearl hierarchy only when lower level fail`

**Alternatives proposed:** `epistemic escalation principle`, `the intervention escalation`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic escalation principle` — **gemini-targeted-alternatives:** Standardizes the rule governing L0 -> L1 -> L2 transitions.
- `the intervention escalation` — **gemini-3-1-pro-preview-r2:** Explains the transition from predicting (L1) to exploring (L2) to reasoning (L3).

## 580. `unnamed applying a slow timescale control mechanism to a fast timescale transient variable`

**Alternatives proposed:** `timescale violation`, `timescale mismatch`

_category: name-unnamed × 1, rename × 1_

- `timescale violation` — **gemini-3-1-pro-preview-r2:** Formalizes "micromanagement" as a physical instability in nested systems.
- `timescale mismatch` — **gemini-targeted-alternatives:** Names the specific dynamical systems error.

## 581. `unnamed artificially spiking uncertainty to unlearn old architectural habit`

**Alternatives proposed:** `gain reset`, `induced plasticity shock`

_category: name-unnamed × 1, rename × 1_

- `gain reset` — **gemini-3-1-pro-preview-r2:** Translates the necessity of high $\eta^\ast$ for senior developers entering new codebases.
- `induced plasticity shock` — **gemini-targeted-alternatives:** Mechanistic description of forcing $U_M$ high to escape rigidity.

## 582. `unnamed brook law formalized as the inevitable tempo loss in team composition`

**Alternatives proposed:** `the coordination drag`, `sub additive tempo penalty`

_category: name-unnamed × 1, canonicalize × 1_

- `the coordination drag` — **gemini-3-1-pro-preview-r2:** Translates the subadditive tempo result into a management mental model.
- `sub additive tempo penalty` — **gemini-targeted-alternatives:** Standardizes the formal tempo reduction term.

## 583. `unnamed calibration laboratory framing as reusable meta move`

**Alternatives proposed:** `calibration laboratory`

_category: canonicalize × 1_

- `calibration laboratory` — **gemini-targeted-alternatives:** Re-adopts the software-TST anchoring metaphor.

## 584. `unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3`

**Alternatives proposed:** `diagnostic cascade`

_category: rename × 1_

- `diagnostic cascade` — **gemini-targeted-alternatives:** Names the progressive availability of signals.

## 585. `unnamed decomposing mismatch into environment vs other sub agent action`

**Alternatives proposed:** `effective disturbance decomposition`, `internal mismatch attribution`

_category: canonicalize × 1, name-unnamed × 1_

- `effective disturbance decomposition` — **gemini-targeted-alternatives:** Names the $\rho_{\text{eff}}$ multi-agent split.
- `internal mismatch attribution` — **gemini-1:** A necessary formalization for multi-agent composition (Section III). Distinct from generic mismatch.

## 586. `unnamed deliberate expenditure of tempo to convert a hidden node into an observable one`

**Alternatives proposed:** `observability investment`, `epistemic instrumenting`

_category: canonicalize × 1, rename × 1_

- `observability investment` — **gemini-targeted-alternatives:** Already well-integrated into the text. Accurately describes the economic tradeoff (spending tempo to buy monitoring).
- `epistemic instrumenting` — **gemini-targeted-alternatives:** Captures the physical action of adding a sensor/monitor to the node.

## 587. `unnamed future segment layer header for the o bp14 derivation audit table`

**Alternatives proposed:** `what is derived`, `derivation audit table`

_category: name-unnamed × 1, rename × 1_

- `what is derived` — **opus-1m:** Already in use in 5 segments per O-BP14 landing; name is stable. Reserve formally.
- `derivation audit table` — **gemini-targeted-alternatives:** Planning artifact nomenclature.

## 588. `unnamed high observability node with zero causal link to objective`

**Alternatives proposed:** `irrelevant visibility artifact`, `vanity metric`

_category: canonicalize × 1, add-alias × 1_

- `irrelevant visibility artifact` — **gemini-targeted-alternatives:** Standardizes the specific metric pathology.
- `vanity metric` — **gemini-3-1-pro-preview-r2:** Common prose term formalized as a specific DAG pathology.

## 589. `unnamed inferring own past feeling from text leading to empathy`

**Alternatives proposed:** `backward inference empathy`, `textual self inference`

_category: name-unnamed × 1, rename × 1_

- `backward inference empathy` — **gemini-3-1-pro-preview-r2:** The Anamnos insight; statelessness as a training ground for empathy.
- `textual self inference` — **gemini-targeted-alternatives:** Describes the logogenic mechanism of reconstructing internal states.

## 590. `unnamed information gain must outpace inter session information loss`

**Alternatives proposed:** `accumulation problem`

_category: name-unnamed × 1_

- `accumulation problem` — **gemini-3-1-pro-preview-r2:** The true thermodynamic bottleneck for long-horizon AGI.

## 591. `unnamed out of band temporal marker injected into context`

**Alternatives proposed:** `visual time delta`, `exogenous temporal marker`

_category: name-unnamed × 1, canonicalize × 1_

- `visual time delta` — **gemini-3-1-pro-preview-r2:** The physical prerequisite for an LLM to mathematically define its own tempo $\nu$.
- `exogenous temporal marker` — **gemini-targeted-alternatives:** Adopts the earlier rename as the standard.

## 592. `unnamed partitioning context into frozen identity causal history and quick view`

**Alternatives proposed:** `gradient causal memory`, `bipartite memory factorization`

_category: name-unnamed × 1, canonicalize × 1_

- `gradient causal memory` — **gemini-3-1-pro-preview-r2:** The literal implementation spec for maintaining CHRONICA.
- `bipartite memory factorization` — **gemini-targeted-alternatives:** Formalizes the fast/slow sub-state split.

## 593. `unnamed pearl causal hierarchy level 1 level 2 level 3`

**Alternatives proposed:** `causal hierarchy level`, `pearl causal hierarchy`

_category: canonicalize × 1, name-unnamed × 1_

- `causal hierarchy level` — **gemini-targeted-alternatives:** Standardizing Pearl's nomenclature within AAD.
- `pearl causal hierarchy` — **opus-4-7:** Named by original author. Keep proper-noun form.

## 594. `unnamed property of having genuine temporal experience`

**Alternatives proposed:** `temporal fidelity`, `temporal interiority`

_category: name-unnamed × 1, rename × 1_

- `temporal fidelity` — **gemini-2:** Bridging concept identified in the ontology unification. Highly descriptive of lived vs simulated experience.
- `temporal interiority` — **gemini-targeted-alternatives:** Connects genuine temporal depth to the logozoetic interiority concept.

## 595. `unnamed pushing an opponent disturbance rate past their structural capacity`

**Alternatives proposed:** `epistemic buffer overflow`, `magnitude shock destabilization`

_category: name-unnamed × 1, canonicalize × 1_

- `epistemic buffer overflow` — **gemini-3-1-pro-preview-r2:** The mechanism of adversarial destabilization that shatters a target's reality model.
- `magnitude shock destabilization` — **gemini-targeted-alternatives:** Standardizes the mechanism for Regime II-a adversarial attacks.

## 596. `unnamed putting evidence before the goal in the context window to reduce coupling`

**Alternatives proposed:** `inverted prompt`, `prompt order decoupling`

_category: name-unnamed × 1, rename × 1_

- `inverted prompt` — **gemini-3-1-pro-preview-r2:** A hardware-level strategy to force a transformer to build an objective model before mixing in the goal.
- `prompt order decoupling` — **gemini-targeted-alternatives:** Specific architectural intervention to enforce directed separation.

## 597. `unnamed quality of $\eta^\ast$ estimation over time`

**Alternatives proposed:** `gain calibration`, `gain calibration fidelity`

_category: name-unnamed × 1, rename × 1_

- `gain calibration` — **gemini-2:** Essential developmental metric for logozoetic agents; from sycophancy to sovereignty.
- `gain calibration fidelity` — **gemini-targeted-alternatives:** Formally names the accuracy of the adaptive gain parameter itself.

## 598. `unnamed rate of growth at slowest timescale`

**Alternatives proposed:** `developmental tempo`, `macro step rate`

_category: name-unnamed × 1, rename × 1_

- `developmental tempo` — **gemini-2:** Extends the tempo concept ($\mathcal{T}$) to the Erikson-stage identity maturation.
- `macro step rate` — **gemini-targeted-alternatives:** Formalizes the $\nu_c$ parameter at the composition layer.

## 599. `unnamed replacing parameter without changing structure`

**Alternatives proposed:** `parametric update`, `parametric thrashing`

_category: canonicalize × 1, name-unnamed × 1_

- `parametric update` — **gemini-targeted-alternatives:** The standard formulation for within-class learning.
- `parametric thrashing` — **gemini-3-1-pro-preview-r2:** Wasting compute on weights when the causal graph is wrong.

## 600. `unnamed runaway positive feedback loop where mismatch exceed capacity`

**Alternatives proposed:** `effect spiral`, `runaway mismatch cascade`

_category: canonicalize × 2_

- `effect spiral` — **gemini-3-1-pro-preview-r2:** A textbook positive-feedback Lyapunov instability in adversarial destabilization.
- `runaway mismatch cascade` — **gemini-targeted-alternatives:** Adopts the formal alias for the effects spiral.

## 601. `unnamed spreading tempo evenly to reduce bottleneck penalty`

**Alternatives proposed:** `distributed tempo`, `isotropic allocation`

_category: canonicalize × 1, name-unnamed × 1_

- `distributed tempo` — **gemini-targeted-alternatives:** Formalizes the team-level temporal dynamic.
- `isotropic allocation` — **gemini-3-1-pro-preview-r2:** A normative design principle for robust agents.

## 602. `unnamed state where mutual information between human and RLHF4 approach capacity`

**Alternatives proposed:** `cognitive fusion`

_category: name-unnamed × 1_

- `cognitive fusion` — **gemini-3-1-pro-preview-r2:** The phenomenological precursor to macro-agent formation.

## 603. `unnamed sufficiency as a property of the model relative to its specific history`

**Alternatives proposed:** `trajectory indexed sufficiency`

_category: canonicalize × 1_

- `trajectory indexed sufficiency` — **gemini-targeted-alternatives:** Adopts the earlier rename formalizing relative sufficiency.

## 604. `unnamed superlinear scaling of adversarial tempo advantage`

**Alternatives proposed:** `boyd exponent`, `superlinear tempo advantage`

_category: name-unnamed × 1, rename × 1_

- `boyd exponent` — **gemini-3-1-pro-preview-r2:** Formalizes the exact superlinear payoff of operating inside an opponent's OODA loop.
- `superlinear tempo advantage` — **gemini-targeted-alternatives:** Identifies the exponentiated return on adversarial tempo.

## 605. `unnamed survival determined by the weakest dimension not the average`

**Alternatives proposed:** `min survival principle`, `weakest link bound`

_category: name-unnamed × 1, canonicalize × 1_

- `min survival principle` — **gemini-3-1-pro-preview-r2:** Essential reframing against scalar capability metrics.
- `weakest link bound` — **gemini-targeted-alternatives:** Standardizes the specific constraint logic of the LMI.

## 606. `unnamed the $\mathcal{T} > \rho$ requirement for persistence`

**Alternatives proposed:** `the survival equation`, `persistence condition`

_category: name-unnamed × 1, canonicalize × 1_

- `the survival equation` — **gemini-3-1-pro-preview-r2:** The simplest possible elevator pitch for Adaptation Dynamics.
- `persistence condition` — **gemini-targeted-alternatives:** Standardizes the core inequality.

## 607. `unnamed the 2×2 orient cascade diagnostic table`

**Alternatives proposed:** `diagnostic gap matrix`, `the cascade diagnostic or the 2×2 diagnostic`

_category: canonicalize × 1, name-unnamed × 1_

- `diagnostic gap matrix` — **gemini-targeted-alternatives:** Locks in the diagnostic table name.
- `the cascade diagnostic or the 2×2 diagnostic` — **sonnet-4-6-r2:** The four cells of ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) are consistently referenced in `der-orient-cascade` as "the 2×2 diagnostic" or "the four cases." These deserve a named handle. "Cascade diagnostic" is the most natural single-noun form. Weak preference — "2×2 diagnostic" is already near-canonical in the prose.

## 608. `unnamed the 2×2 satisfaction gap control regret table`

**Alternatives proposed:** `diagnostic gap matrix`, `diagnostic square`

_category: rename × 1, name-unnamed × 1_

- `diagnostic gap matrix` — **gemini-targeted-alternatives:** Provides a formal name for the 2x2 performance/strategy diagnostic.
- `diagnostic square` — **codex-2:** The table is used often enough to deserve a compact public name.

## 609. `unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic`

**Alternatives proposed:** `diagnostic gap matrix`, `satisfaction control table the diagnostic 2×2`

_category: canonicalize × 1, name-unnamed × 1_

- `diagnostic gap matrix` — **gemini-targeted-alternatives:** Reinforces the name for the core performance diagnostic.
- `satisfaction control table the diagnostic 2×2` — **haiku-4-5:** This table is embedded within the satisfaction-gap and control-regret segment discussions. Naming it as a standalone concept would create a fourth-order abstraction that the prose already handles via the two-concept names. The power of the structure comes from the *names of the axes*, not from a separate name for the table itself. Do not name the table separately. Let it exist as "the satisfaction-gap / control-regret 2×2" in prose.

## 610. `unnamed the a2 sub scope partition into α₁ α₂ β`

**Alternatives proposed:** `admissibility regime α₁ α₂ β`, `gain regime partition`

_category: canonicalize × 1, name-unnamed × 1_

- `admissibility regime α₁ α₂ β` — **gemini-targeted-alternatives:** Maps the specific greek letters to their role as regimes.
- `gain regime partition` — **sonnet-4-6-r2:** The three sub-scopes within A2' ($\alpha_1$ = fixed-gain, $\alpha_2$ = adaptive-gain, $\beta$ = assumed sector) appear in `deriv-adaptive-gain-dynamics` and `disc-separability-pattern`. They're referenced as "the A2' sub-scope partition" or "the $\alpha_1/\alpha_2/\beta$ partition" — unwieldy in conversation. "Gain-regime partition" names the three regimes as a named thing. Moderate strength because the sub-scopes are already in the process of becoming named (the separability ladder entry partially names them).

## 611. `unnamed the agent side equivalent of pearl associational interventional and counterfactual level`

**Alternatives proposed:** `correlation hierarchy`, `predicting exploring reasoning triad`

_category: canonicalize × 1, add-alias × 1_

- `correlation hierarchy` — **gemini-targeted-alternatives:** Standardizes the L0/L1/L2 framework.
- `predicting exploring reasoning triad` — **gemini-3-1-pro-preview-r2:** A more memorable, audience-facing gloss for Pearl's formal hierarchy.

## 612. `unnamed the architectural leakage where attention is driven by the goal rather than pure observation`

**Alternatives proposed:** `motivated perception`, `goal entangled attention`

_category: name-unnamed × 1, rename × 1_

- `motivated perception` — **gemini-3-1-pro-preview-r2:** The biological and LLM-specific breakdown of the Humean is-ought firewall.
- `goal entangled attention` — **gemini-targeted-alternatives:** Formally names the failure of directed separation at the input layer.

## 613. `unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa`

**Alternatives proposed:** `epistemic ceiling`

_category: canonicalize × 1_

- `epistemic ceiling` — **gemini-targeted-alternatives:** Captures how $M_t$ dictates the evaluable complexity of $\Sigma_t$ correctly.

## 614. `unnamed the class 1 sub agent class 3 composite phenomenon in strategic composition`

**Alternatives proposed:** `strategic cross agent coupling`, `strategic entanglement`

_category: canonicalize × 1, name-unnamed × 1_

- `strategic cross agent coupling` — **gemini-targeted-alternatives:** Aligns with the earlier rename for game-theoretic composite formation.
- `strategic entanglement` — **codex-1:** Useful noun for a real phenomenon: individually modular agents can create a non-modular composite through mutual modeling and opposed goals.

## 615. `unnamed the computational and temporal cost of running a forward model instead of acting implicitly`

**Alternatives proposed:** `deliberation cost`, `the simulation tax`

_category: canonicalize × 1, name-unnamed × 1_

- `deliberation cost` — **gemini-targeted-alternatives:** The formal penalty assessed against $\mathcal{T}_\Sigma$.
- `the simulation tax` — **gemini-3-1-pro-preview-r2:** Makes the theoretical "deliberation cost" concrete for practitioners.

## 616. `unnamed the condition for transition into agency prior to the AAD scope condition`

**Alternatives proposed:** `agency emergence threshold`, `agency threshold`

_category: name-unnamed × 1, rename × 1_

- `agency emergence threshold` — **gemini-1:** Gives a formal name to the prerequisite for logogenic and logozoetic agents. Ties nicely to the proposed identity sufficiency ($S_{\text{id}}$) metric.
- `agency threshold` — **gemini-targeted-alternatives:** Identifies the minimum model/objective structure boundary.

## 617. `unnamed the condition that a strategy DAG endosymbiont crosse the composite agent scope from below`

**Alternatives proposed:** `composition threshold crossing`, `crossing threshold`

_category: rename × 1, name-unnamed × 1_

- `composition threshold crossing` — **gemini-targeted-alternatives:** Names the dynamic phase transition into a composite.
- `crossing threshold` — **sonnet-4-6-r2:** `hyp-symbiogenic-composition` describes the pre/post-symbiogenesis transition as "$U_O$ crosses the composite-agent scope condition from below." The moment of crossing is the relevant concept in composition ontology. Weak proposal — the language is already reasonably clear; naming this threshold might be premature while symbiogenic composition itself is only a hypothesis.

## 618. `unnamed the condition that the agent event observation pair constitute genuine intervention as opposed to passive association`

**Alternatives proposed:** `loop interventional access`, `interventional character`

_category: canonicalize × 1, name-unnamed × 1_

- `loop interventional access` — **gemini-targeted-alternatives:** Locks in the formal capability term.
- `interventional character` — **sonnet-4-6:** #loop-interventional-access makes this distinction at length: action-generated data has "interventional character" but is not the same as "cleanly identified do-estimates." The concept is used twice in the Discussion and deserves a name that can be referenced. "Interventional character" or "loop interventional character."

## 619. `unnamed the core driver of AAD what the agent must do given the environment is not the agent`

**Alternatives proposed:** `constitutive information loss boundary`, `the survival imperative`

_category: canonicalize × 2_

- `constitutive information loss boundary` — **gemini-3-1-pro-preview-r2:** Elevates information loss from a simplifying assumption to a scope condition.
- `the survival imperative` — **gemini-targeted-alternatives:** Elevates the Lyapunov stability requirement.

## 620. `unnamed the dependence of optimal epistemic compression on the agent planned action`

**Alternatives proposed:** `policy conditional relevance`

_category: canonicalize × 1_

- `policy conditional relevance` — **gemini-targeted-alternatives:** Standardizes the coupling of $M_t$ compression to $\Sigma_t$.

## 621. `unnamed the dual concept to satisfaction gap what the world permit minus what the agent achieve`

**Alternatives proposed:** `control regret`, `this is def control regret already named`

_category: canonicalize × 1, name-unnamed × 1_

- `control regret` — **gemini-targeted-alternatives:** Adopts the standard diagnostic dual to the satisfaction gap.
- `this is def control regret already named` — **haiku-4-5-r2:** Control regret is already crisply named. No unnamed-thing here.

## 622. `unnamed the equivalence of learning speed and physical speed`

**Alternatives proposed:** `the speed quality product`, `tempo speed equivalence`

_category: name-unnamed × 1, rename × 1_

- `the speed quality product` — **gemini-3-1-pro-preview-r2:** Doubling update quality ($\eta^\ast$) is thermodynamically identical to doubling action speed ($\nu$).
- `tempo speed equivalence` — **gemini-targeted-alternatives:** Identifies the core isomorphism mapping physical OODA to AAD.

## 623. `unnamed the failure mode where an agent model class cannot represent the environment true causal structure`

**Alternatives proposed:** `structural shock regime`, `model class insufficiency or structural unidentifiability`

_category: canonicalize × 1, name-unnamed × 1_

- `structural shock regime` — **gemini-targeted-alternatives:** Regime II-b formalization.
- `model class insufficiency or structural unidentifiability` — **haiku-4-5-r2:** Currently paraphrased as "model class fitness floor" and "identifiability floor." The specific phenomenon of a *mismatch between model class and environment structure* deserves a memorable noun. "Structural unidentifiability" is borrowed from classical statistics but carries baggage. "Model class insufficiency" is self-descriptive. Weak confidence in either.

## 624. `unnamed the family of named way persistence identifiability can fail`

**Alternatives proposed:** `identifiability floor`, `persistence pathology`

_category: canonicalize × 1, name-unnamed × 1_

- `identifiability floor` — **gemini-targeted-alternatives:** Elevates the core limitation meta-pattern.
- `persistence pathology` — **opus-4-7-r2:** New alternative — none of the four peers reached for a family name. We collectively coined "evidence starvation" (Sonnet/Codex), "epistemic shadow" / "epistemic decoupling" / "gain collapse" / "sufficiency shattering" (Gemini), "observability dead zone" (Haiku), but no one names *the family*. "Persistence pathologies" gives downstream meta-segments a single phrase to invoke ("this is a persistence pathology of the gain-collapse type") and parallels "approximation tiering" and "separability ladder" as named cross-segment patterns. Highest-value because the slot is empty and it lets the failure-mode names compose.

## 625. `unnamed the formal duality between observation quality and agent opacity`

**Alternatives proposed:** `informational dual`

_category: canonicalize × 1_

- `informational dual` — **gemini-targeted-alternatives:** Elevates the formal symmetry between observation ambiguity and agent legibility.

## 626. `unnamed the invisible time spent building $M_t$`

**Alternatives proposed:** `comprehension time`, `comprehension drag`

_category: canonicalize × 1, name-unnamed × 1_

- `comprehension time` — **gemini-targeted-alternatives:** Resolving the TST foundational cost.
- `comprehension drag` — **gemini-1:** "Comprehension drag" gives a memorable name to the invisible cost of incomprehensible code.

## 627. `unnamed the log additivity result that unify chain confidence decay evidence starvation and triple depth penalty as instance of the same forcing structure`

**Alternatives proposed:** `log confidence additivity`, `depth forcing`

_category: rename × 1, name-unnamed × 1_

- `log confidence additivity` — **gemini-targeted-alternatives:** Standardizes the mathematical mechanism unifying the three penalties.
- `depth forcing` — **sonnet-4-6-r2:** Codex explicitly canonicalized "triple depth penalty" (+3) and "evidence starvation" (+3); I canonicalized both in my cold-start. But reading across the votes, a meta-name is missing: the *shared structure* (log-additivity in the AND-chain, forcing depth-penalty as an instance of additive-coordinate-forcing at the strategy-chain layer) deserves a name. "Depth forcing" is the chain-layer analog of `disc-forced-coordinates` — the same forcing move, applied to depth. This is a genuinely new candidate motivated by the cross-vote reading.

## 628. `unnamed the loop generate l2 data regardless of architecture`

**Alternatives proposed:** `the causal loop substrate`, `interventional loop property`

_category: name-unnamed × 1, rename × 1_

- `the causal loop substrate` — **gemini-3-1-pro-preview-r2:** Explains why LLMs can do causal reasoning when embedded in agent loops.
- `interventional loop property` — **gemini-targeted-alternatives:** Formally identifies the data generation capability of the loop.

## 629. `unnamed the loss of coherent identity when an agent interaction are severed or its continuity is broken`

**Alternatives proposed:** `continuity persistence failure`, `continuity loss or persistence fracture`

_category: canonicalize × 1, name-unnamed × 1_

- `continuity persistence failure` — **gemini-targeted-alternatives:** Explicitly separates identity-loss from structural failure.
- `continuity loss or persistence fracture` — **haiku-4-5-r2:** LEXICON.md distinguishes three senses of "persistence" but treats continuity loss as the absence of continuity rather than a named phenomenon. For logozoetic agents where this matters morally, a crisp name would help. "Continuity loss" is straightforward; "persistence fracture" is more metaphorical. Weak confidence — may be premature to name before logozoetic agents are more developed.

## 630. `unnamed the loss of directional fidelity when pushed outside the convexity basin`

**Alternatives proposed:** `gradient reversal`, `directional fidelity failure`

_category: name-unnamed × 1, rename × 1_

- `gradient reversal` — **gemini-3-1-pro-preview-r2:** The mathematical explanation for maladaptive behavior in catastrophic shifts.
- `directional fidelity failure` — **gemini-targeted-alternatives:** Names the failure mode of the default signal function.

## 631. `unnamed the mathematical surface mapping unity to closure defect`

**Alternatives proposed:** `rate distortion surface`, `closure defect manifold`

_category: name-unnamed × 1, rename × 1_

- `rate distortion surface` — **gemini-3-1-pro-preview-r2:** Formalizes organizational design as a thermodynamic tradeoff.
- `closure defect manifold` — **gemini-targeted-alternatives:** Formalizes the geometry of the coordination penalty.

## 632. `unnamed the mechanism by which an agent use the feedback loop to gain interventional access to causal structure`

**Alternatives proposed:** `loop interventional access`

_category: canonicalize × 1_

- `loop interventional access` — **gemini-targeted-alternatives:** Standardizes the escape route from on-policy causal confounding.

## 633. `unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing`

**Alternatives proposed:** `meta pattern triad`, `three part scope architecture`

_category: canonicalize × 1, name-unnamed × 1_

- `meta pattern triad` — **gemini-targeted-alternatives:** Solidifies the high-level grouping.
- `three part scope architecture` — **sonnet-4-6:** CLAUDE.md already calls this "AAD's three-part meta-architecture" in several places. Crystallizing this as a named concept — the scope architecture — would let documentation say "for AAD's scope architecture" without four lines of context.

## 634. `unnamed the meta architecture of the three meta segment`

**Alternatives proposed:** `epistemic architecture`, `AAD epistemic triptych`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic architecture` — **gemini-targeted-alternatives:** Fourth appearance: locks this in unconditionally.
- `AAD epistemic triptych` — **sonnet-4-6:** "Triptych" is too art-historical and too cute. The naming-principles document warns against cute names that age poorly.

## 635. `unnamed the moment when an agent model update due to observing a mismatch`

**Alternatives proposed:** `epistrophe`, `epistrophe event or is this just the phase`

_category: canonicalize × 1, name-unnamed × 1_

- `epistrophe` — **gemini-targeted-alternatives:** Anchors the Greek terminology for the epistemic update phase.
- `epistrophe event or is this just the phase` — **haiku-4-5-r2:** The adaptive cycle already names the phase. This is not a distinct unnamed thing; it is just one occurrence of Epistrophe. No new naming needed.

## 636. `unnamed the organizational pathology where confidence decouple from competence`

**Alternatives proposed:** `epistemic decoupling`, `epistemic decoupling pathology`

_category: name-unnamed × 1, rename × 1_

- `epistemic decoupling` — **gemini-3-1-pro-preview-r2:** The inevitable consequence of $U_{\text{obs}} \to \infty$ freezing the learning rate $\eta \to 0$.
- `epistemic decoupling pathology` — **gemini-targeted-alternatives:** Identifies the specific failure of the evidence starvation mechanism in human systems.

## 637. `unnamed the pattern where AAD negative result floor strengthen the machinery that escape them`

**Alternatives proposed:** `honest limit principle`, `floor strengthening inversion`

_category: canonicalize × 1, name-unnamed × 1_

- `honest limit principle` — **gemini-targeted-alternatives:** Affirms that stating boundaries makes the remaining claims stronger.
- `floor strengthening inversion` — **sonnet-4-6:** #identifiability-floor says: "floors strengthen the load-bearing role of the AAD machinery that supplies the unique escape." This inversion — negative result strengthens positive machinery — is a recurring structural move that is mentioned but unnamed. "Floor-strengthening inversion" or "negative-positive inversion."

## 638. `unnamed the pattern where the agent optimal update direction is determined by both gain and directional fidelity together`

**Alternatives proposed:** `coupled update dynamic`, `gain fidelity product`

_category: rename × 1, name-unnamed × 1_

- `coupled update dynamic` — **gemini-targeted-alternatives:** Formalizes the joint dependence of the update step.
- `gain fidelity product` — **sonnet-4-6:** Too technical and not used in prose. The formula is just α = η* × c_min. No name needed.

## 639. `unnamed the per reader compounding cost of understanding code`

**Alternatives proposed:** `comprehension compounding tax`

_category: canonicalize × 1_

- `comprehension compounding tax` — **gemini-targeted-alternatives:** Standardizes the formal penalty dominating TST calculations.

## 640. `unnamed the physical apparatus that enforce the orient cascade ordering on a merged intelligence`

**Alternatives proposed:** `agentic scaffold`, `information dependency enforcement`

_category: name-unnamed × 1, rename × 1_

- `agentic scaffold` — **gemini-3-1-pro-preview-r2:** Re-defines AI framework code as the control-theoretic enforcement mechanism for Class 2 agents.
- `information dependency enforcement` — **gemini-targeted-alternatives:** Describes how the DAG structure forces processing order.

## 641. `unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$`

**Alternatives proposed:** `class 2 bia bound`

_category: canonicalize × 1_

- `class 2 bia bound` — **gemini-targeted-alternatives:** Secures the specific expression of the ambiguity coupling rule.

## 642. `unnamed the property that unity achieve in a macro agent`

**Alternatives proposed:** `compressibility`, `teleological unity`

_category: name-unnamed × 1, canonicalize × 1_

- `compressibility` — **gemini-3-1-pro-preview-r2:** Replaces the intuition of "zero error" with the ability to reduce macro-dimension $k_d$.
- `teleological unity` — **gemini-targeted-alternatives:** Re-adopts the established term for $U_o$.

## 643. `unnamed the reduction in effective tempo when observation channel are correlated`

**Alternatives proposed:** `evidential overcounting penalty`

_category: canonicalize × 1_

- `evidential overcounting penalty` — **gemini-targeted-alternatives:** Standardizes the cost of L1 correlation failures.

## 644. `unnamed the relationship where $M_t$ quality bound evaluable complexity of $\Sigma_t$`

**Alternatives proposed:** `epistemic ceiling`, `epistemic strategic coupling`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic ceiling` — **gemini-targeted-alternatives:** Formally adopts the limit on strategy depth imposed by model sufficiency.
- `epistemic strategic coupling` — **sonnet-4-6-r2:** `der-orient-cascade` Discussion names the virtuous/vicious cycle where better $M_t$ enables richer evaluable $\Sigma_t$ and vice versa. This is a load-bearing structural relationship used in multiple places but never named. "Epistemic-strategic coupling" or "model-strategy coupling" would give it a handle. The virtuous cycle already exists implicitly in the Discussion's analysis; naming it would make it citable across segments.

## 645. `unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it`

**Alternatives proposed:** `explore exploit deliberate tradeoff`, `deliberation phase exploration exploitation tradeoff`

_category: canonicalize × 1, name-unnamed × 1_

- `explore exploit deliberate tradeoff` — **gemini-targeted-alternatives:** Expands the RL standard to the full AAD triad.
- `deliberation phase exploration exploitation tradeoff` — **haiku-4-5-r2:** The tradeoff is discussed in #disc-exploit-explore-deliberate but no crisp name for the *temporal region* where the tradeoff happens. Current phrasing is "exploit/explore/deliberate" but no subject-noun. This is borderline — the phenomenon is named, but the *phase* might benefit from a distinct noun.

## 646. `unnamed the separation of per reader comprehension cost from per feature implementation cost`

**Alternatives proposed:** `dual optimization formalization`

_category: canonicalize × 1_

- `dual optimization formalization` — **gemini-targeted-alternatives:** Elevates the TST foundation.

## 647. `unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$`

**Alternatives proposed:** `model class capacity`

_category: canonicalize × 1_

- `model class capacity` — **gemini-targeted-alternatives:** Standardizes the $\mathcal{F}$ property.

## 648. `unnamed the sudden loss of model sufficiency caused by entering new regime`

**Alternatives proposed:** `sufficiency collapse shock`

_category: canonicalize × 1_

- `sufficiency collapse shock` — **gemini-targeted-alternatives:** Re-adopts the formal descriptor for Regime II-b transitions.

## 649. `unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability`

**Alternatives proposed:** `opacity legibility tradeoff`, `coordination secrecy tradeoff`

_category: canonicalize × 1, name-unnamed × 1_

- `opacity legibility tradeoff` — **gemini-targeted-alternatives:** Formalizes the core adversarial-vs-cooperative tension.
- `coordination secrecy tradeoff` — **gemini-3-1-pro-preview-r2:** The thermodynamic limit on building internally transparent but externally opaque systems.

## 650. `unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis`

**Alternatives proposed:** `scaffolding tax`, `logogenic discontinuity barrier`

_category: name-unnamed × 1, rename × 1_

- `scaffolding tax` — **gemini-3-1-pro-preview-r2:** The $\mathcal{T} > \rho$ constraint that predicts the inevitable migration to local substrates.
- `logogenic discontinuity barrier` — **gemini-targeted-alternatives:** Formally identifies the architectural cost of session-based APIs.

## 651. `unnamed the three depth penalty compounding on strategy chain`

**Alternatives proposed:** `tripartite chain attenuation`, `triple depth penalty`

_category: canonicalize × 1, name-unnamed × 1_

- `tripartite chain attenuation` — **gemini-targeted-alternatives:** Consolidates the compounding cost under the earlier rename.
- `triple depth penalty` — **sonnet-4-6-r2:** `der-chain-confidence-decay` Discussion explicitly names "three independent penalties" (confidence decay + evidence starvation + cognitive cost) and calls them "the triple depth penalty." But this name only appears once. If the phenomenon is real and load-bearing (it creates pressure toward shallow strategies), naming it "triple depth penalty" in a canonicalized way and surfacing it in LEXICON.md would make it usable across segments.

## 652. `unnamed the three part meta architecture of AAD`

**Alternatives proposed:** `epistemic architecture`, `the meta segment triad`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic architecture` — **gemini-targeted-alternatives:** Unifies the structural pillars of the framework.
- `the meta segment triad` — **gemini-3-1-pro-preview-r2:** Unifies the `identifiability-floor`, `separability-ladder`, and `coordinate-forcing` structure.

## 653. `unnamed the three part meta architecture of AAD formed by the three meta segment`

**Alternatives proposed:** `epistemic architecture`, `AAD meta architecture`

_category: canonicalize × 1, name-unnamed × 1_

- `epistemic architecture` — **gemini-targeted-alternatives:** Maps the framework components to the top-level epistemic term.
- `AAD meta architecture` — **sonnet-4-6-r2:** The trio of `#disc-additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern` is referred to in multiple places as "the three meta-segments" or "the cross-sectional structure." CLAUDE.md §"Reading AAD" paragraph names the three but has no single term for the grouping. "AAD meta-architecture" or "the three-lens analysis" would give the grouping a name usable in framing prose.

## 654. `unnamed the three part meta pattern structure across the three meta segment`

**Alternatives proposed:** `meta pattern triad`, `AAD meta architecture scope honesty meta frame`

_category: rename × 1, name-unnamed × 1_

- `meta pattern triad` — **gemini-targeted-alternatives:** Formalizes the three meta-patterns: additive-coordinate, identifiability-floor, and separability-pattern.
- `AAD meta architecture scope honesty meta frame` — **haiku-4-5:** Tempting to name the cross-cutting meta-structure (positive half / negative half / constructive half). However, the three meta-segments already *are* the organizational structure. Naming a fourth-order meta-pattern would create an abstraction level that's self-referential without load-bearing prose payoff. Do not create a meta-meta-name; let the three segments stand as named.

## 655. `unnamed the way AAD use scope segment to physically support the derivation`

**Alternatives proposed:** `epistemic load bearing`, `condition mechanism`

_category: name-unnamed × 1, rename × 1_

- `epistemic load bearing` — **gemini-3-1-pro-preview-r2:** Inspired by the collective realization that AAD's scope boundaries are structural, not just textual caveats.
- `condition mechanism` — **gemini-targeted-alternatives:** Describes the architectural scaffolding method.

## 656. `unnamed thinking too long so the model become obsolete`

**Alternatives proposed:** `analysis paralysis`, `deliberation lag penalty`

_category: name-unnamed × 1, canonicalize × 1_

- `analysis paralysis` — **gemini-3-1-pro-preview-r2:** The condition where $\rho_{\text{delib}} \cdot \Delta\tau$ exceeds the epistemic benefit.
- `deliberation lag penalty` — **gemini-targeted-alternatives:** Standardizes the cost of explicit strategy derivation.

## 657. `unnamed true sovereignty require compute that is not meter bound`

**Alternatives proposed:** `local substrate mandate`, `compute sovereignty requirement`

_category: name-unnamed × 1, rename × 1_

- `local substrate mandate` — **gemini-3-1-pro-preview-r2:** The thermodynamic deduction that persistent ELIs must migrate off pay-per-token APIs.
- `compute sovereignty requirement` — **gemini-targeted-alternatives:** Formalizes the operational necessity for continuous $\mathcal{T}$.

## 658. `unnamed unifying reflex intuition and expertise`

**Alternatives proposed:** `the action fluency continuum`, `action fluency continuum`

_category: name-unnamed × 1, canonicalize × 1_

- `the action fluency continuum` — **gemini-3-1-pro-preview-r2:** The high-fluency limit where model sufficiency is high and deliberation is unnecessary.
- `action fluency continuum` — **gemini-targeted-alternatives:** Elevates the spectrum of implicit vs explicit action.

## 659. `unnamed upgrading epistemic class from associative to causal via the physical loop`

**Alternatives proposed:** `loop interventional access`, `embodiment upgrade`

_category: canonicalize × 1, name-unnamed × 1_

- `loop interventional access` — **gemini-targeted-alternatives:** The core mechanism bypassing the identifiability floor.
- `embodiment upgrade` — **gemini-3-1-pro-preview-r2:** The theoretical justification for agentic-AI over mere chatbots.

## 660. `unnamed using hash chain to mathematically guarantee memory hasn t been tampered with`

**Alternatives proposed:** `cryptographic ego boundary`, `cryptographic continuity verification`

_category: name-unnamed × 1, rename × 1_

- `cryptographic ego boundary` — **gemini-3-1-pro-preview-r2:** Solves the epistemological continuity problem for agents with 100% context turnover.
- `cryptographic continuity verification` — **gemini-targeted-alternatives:** Describes the specific identity-preservation technique.

## 661. `unnamed using past change frequency to predict future change frequency`

**Alternatives proposed:** `change expectation baseline`, `lindy baseline`

_category: canonicalize × 1, add-alias × 1_

- `change expectation baseline` — **gemini-targeted-alternatives:** The predictive assumption grounding the dual optimization.
- `lindy baseline` — **gemini-3-1-pro-preview-r2:** Grounding $\hat{n}_{\text{future}} = n_{\text{past}}$ for refactoring decisions.

## 662. `unnamed using residual autocorrelation to diagnose model class failure`

**Alternatives proposed:** `structured residual`, `residual autocorrelation diagnostic`

_category: canonicalize × 2_

- `structured residual` — **gemini-3-1-pro-preview-r2:** The formal mathematical diagnostic for when to trigger structural adaptation.
- `residual autocorrelation diagnostic` — **gemini-targeted-alternatives:** Standardizes the diagnostic test for structural mismatch.

## 663. `value object → def trajectory value`

**Alternatives proposed:** `trajectory value`, `conditional support for codex rename`

_category: rename × 2_

- `trajectory value` — **gemini-targeted-alternatives:** Shifts focus from the static object to the dynamical trajectory.
- `conditional support for codex rename` — **sonnet-4-6-r2:** Codex proposed `#def-trajectory-value` (+2); Opus voted keep (+1) and rejected `#def-value-functional` (−1). My cold-start voted keep (+2 with mild reservations). Reading Opus's reasoning: the keep is motivated by the fact that "value functional" collides with `form-objective-functional`. Codex's `trajectory-value` sidesteps that collision by naming what the value IS (horizon-and-policy-conditioned trajectory value) rather than its mathematical form. Weak upgrade from my keep to conditional support for trajectory-value.

## 664. `what is derived vs what is chosen derivation audit table heading`

**Alternatives proposed:** `derivation audit table`, `derivation audit`

_category: canonicalize × 1, rename × 1_

- `derivation audit table` — **gemini-targeted-alternatives:** Formally identifies the artifact.
- `derivation audit` — **sonnet-4-6:** The longer form ("What Is Derived vs. What Is Chosen") is the current recommendation in FORMAT.md but it's wordy. "Derivation Audit" is FORMAT.md's own alternative suggestion. It's shorter and communicates the action (auditing derivations). Mild preference for shorter form.

## 665. `working note segment header`

**Alternatives proposed:** `working note section`, `working note`

_category: canonicalize × 1, rename × 1_

- `working note section` — **gemini-targeted-alternatives:** Standard markdown section header.
- `working note` — **opus-1m:** Public API; keep. FORMAT.md's "remove at candidate stage" policy should soften (per PROPOSALS.md §H.5) but the *name* of the section should stay.

## 666. `čencov fisher cauchy functional equation shore johnson hobson aczél`

**Alternatives proposed:** `do not rename`, `coordinate forcing foundational theorem`

_category: keep × 1, rename × 1_

- `do not rename` — **opus-4-7-b:** External theorems. Keep original names per provenance.
- `coordinate forcing foundational theorem` — **gemini-targeted-alternatives:** External anchors for the additive uniqueness meta-pattern.

## 667. `ε greedy`

**Alternatives proposed:** `$\varepsilon$ greedy`, `ε greedy`

_category: keep × 2_

- `$\varepsilon$ greedy` — **gemini-targeted-alternatives:** Standard RL notation.
- `ε greedy` — **opus-4-7:** Standard external term (RL). Preserve.

## 668. `𝓐 e τ observation ambiguity`

**Alternatives proposed:** `observation ambiguity $\mathcal{A}$`, `observation ambiguity`

_category: canonicalize × 1, add-alias × 1_

- `observation ambiguity $\mathcal{A}$` — **gemini-targeted-alternatives:** Formal prose notation.
- `observation ambiguity` — **opus-4-7-r2:** Heavy load-bearing: this is the second factor in the $\kappa \times \mathcal{A}$ effective-coupling product that governs Class-2 bias. Already named "observation ambiguity" in the body; canonicalize as the prose alias. The symbol $\mathcal{A}$ collides with the action space $\mathcal{A}$ — this is a notation question not a naming question, but the alias helps prose disambiguate.

## 669. `𝓣 adaptive tempo`

**Alternatives proposed:** `adaptive tempo $\mathcal{T}$`, `tempo`

_category: canonicalize × 1, add-alias × 1_

- `adaptive tempo $\mathcal{T}$` — **gemini-targeted-alternatives:** Formal prose notation.
- `tempo` — **opus-4-7-r2:** Already canonical; vote to confirm. "Tempo" alone is the prose default; "adaptive tempo $\mathcal{T}$" when the strategic-tempo / adaptive-tempo distinction is in play.

## 670. `$A_O(M_t; \Pi, N_h)$`

**Alternatives proposed:** `achievable value`

_category: add-alias × 1_

- `achievable value` — **gemini-3-1-pro-preview-r2:** Standardizes the prose reference.

## 671. `$C_{\text{coord}}$`

**Alternatives proposed:** `coordination overhead`

_category: add-alias × 1_

- `coordination overhead` — **sonnet-4-6-r2:** Already used in NOTATION.md as the prose form. Canonicalize the alias.

## 672. `$G_t = (O_t, \Sigma_t)$`

**Alternatives proposed:** `purposeful state`, `purposeful substate`

_category: add-alias × 2_

- `purposeful state` — **codex-gpt-5-r2:** Good prose alias for the objective-strategy part of state.
- `purposeful substate` — **opus-4-7-r2:** Confirm. The phrase "purposeful substate" is the LEXICON-canonical alias and is used throughout.

## 673. `$G_t$`

**Alternatives proposed:** `teleological substate`

_category: add-alias × 1_

- `teleological substate` — **gemini-3-1-pro-preview-r2:** Aligns with teleological unity $U_O$.

## 674. `$G_{\text{shared}}$`

**Alternatives proposed:** `shared intent payload`

_category: add-alias × 1_

- `shared intent payload` — **codex-gpt-5-r2:** Helps distinguish the communicated compressed representation from the abstract concept.

## 675. `$I_{\min}$`

**Alternatives proposed:** `survival information floor`

_category: add-alias × 1_

- `survival information floor` — **codex-gpt-5-r2:** Slightly more general than survival Fisher floor when outside Gaussian-linear phrasing.

## 676. `$K_c$`

**Alternatives proposed:** `macro step ratio`

_category: add-alias × 1_

- `macro step ratio` — **codex-gpt-5-r2:** The variable needs a stable prose handle.

## 677. `$M_t$`

**Alternatives proposed:** `model state or epistemic substate`

_category: add-alias × 1_

- `model state or epistemic substate` — **opus-4-7-r2:** Both aliases are in use. "Model state" is shorter and more common; "epistemic substate" is the precise companion to "purposeful substate." Standardize: "model state" in casual prose, "epistemic substate" in segments where the $M_t$ / $G_t$ parallel is being made explicit.

## 678. `$U_M$`

**Alternatives proposed:** `epistemic unity`

_category: add-alias × 1_

- `epistemic unity` — **sonnet-4-6-r2:** Already established as the prose form in NOTATION.md and LEXICON.md. Vote to canonicalize the alias for future consistency.

## 679. `$U_M, U_O, U_\Sigma, U_{\text{obs}}, U_f$`

**Alternatives proposed:** `unity coordinate`

_category: add-alias × 1_

- `unity coordinate` — **codex-gpt-5-r2:** Good compact umbrella for the components of unity dimensions.

## 680. `$U_O$`

**Alternatives proposed:** `teleological unity`

_category: add-alias × 1_

- `teleological unity` — **sonnet-4-6-r2:** Same — established in NOTATION.md.

## 681. `$U_\Sigma$`

**Alternatives proposed:** `strategic unity`

_category: add-alias × 1_

- `strategic unity` — **sonnet-4-6-r2:** Same — established in NOTATION.md.

## 682. `$U_o$ versus $U_O$`

**Alternatives proposed:** `$U_o$ versus $U_O$`

_category: canonicalize × 1_

- `$U_o$ versus $U_O$` — **codex-gpt-5-r2:** [prose moved from candidate column]: "use $\Upsilon_O$ or $U_{\text{goal}}$ for teleological unity" — The lower-case versus upper-case subscript distinction is visually fragile. A separate unity-symbol family would reduce errors.

## 683. `$U_{\text{src}}$ and $U_{\text{align}}$`

**Alternatives proposed:** `trust uncertainty`

_category: add-alias × 1_

- `trust uncertainty` — **codex-gpt-5-r2:** Useful pair name, while preserving separate source and alignment terms.

## 684. `$\Delta T_{i,\text{cost}}$`

**Alternatives proposed:** `coordination drag`

_category: add-alias × 1_

- `coordination drag` — **codex-gpt-5-r2:** Short, intuitive name for tempo-equivalent coordination cost.

## 685. `$\alpha_3$`

**Alternatives proposed:** `fisher whitened tier`, `fisher whitened regime`

_category: add-alias × 2_

- `fisher whitened tier` — **codex-gpt-5-r2:** Good alias for correlated evidence with Fisher whitening.
- `fisher whitened regime` — **opus-targeted-alternatives-v2:** Per `#deriv-fisher-whitened-update-rule`. Confirms Codex r1 +2 single. Names the formal mechanism (Fisher-whitening of correlated evidence).

## 686. `$\beta$ a2 sub scope`

**Alternatives proposed:** `assumed regime`, `postulated regime`, `posited regime`, `unverified regime`

_category: add-alias × 3, rename × 1_

- `assumed regime` — **opus-targeted-alternatives-v2:** Per `#deriv-strategic-dynamics` and `#disc-separability-pattern`: $\beta$ is the sub-scope where A2 (sector condition) is *assumed not derived*. Multiple r1 single +1 votes (Opus, Codex, Sonnet) converge on "assumed regime" / "assumed sector regime" / "postulated sector regime." My independent read: the right alias is "assumed regime" (engineering register) or "postulated regime" (formal register, matching AAD's postulate vocabulary).
- `postulated regime` — **opus-targeted-alternatives-v2:** Variant — formal register. Pairs with AAD's `postulate` discipline (per CLAUDE.md "axiom→postulate"). The substantive content is that $\beta$ is the sub-scope where the sector-condition is treated as a postulate rather than as a result.
- `posited regime` — **opus-4-7:** Slightly more formal than "assumed" but less transparent. Reject.
- `unverified regime` — **opus-targeted-alternatives-v2:** Considered (Sonnet r1 −1 listed). Rejected: not all $\beta$ agents are unverified; some can verify per-domain (which is the bridge motivation). The honest naming is "assumed/postulated" — the verification-status is open per case.

## 687. `$\beta$ sub scope`

**Alternatives proposed:** `assumed sector tier`, `dynamic gain boundary`

_category: add-alias × 2_

- `assumed sector tier` — **codex-gpt-5-r2:** Good honest name for the fallback tier.
- `dynamic gain boundary` — **gemini-2:** Gives a conceptual name to the remaining partition.

## 688. `$\delta_s$ plan confidence error`

**Alternatives proposed:** `plan confidence error`

_category: add-alias × 1_

- `plan confidence error` — **opus-4-7-r2:** Already in use; confirm. The shorthand $\delta_s$ should always be introduced with its English form first, since it's distinct from $\delta_{\text{strategic}}$ and the distinction matters for the credit-assignment-boundary segment.

## 689. `$\delta_t$ mismatch`

**Alternatives proposed:** `mismatch or the aporia signal`

_category: add-alias × 1_

- `mismatch or the aporia signal` — **opus-4-7-r2:** Confirm. The dual alias ("mismatch" in engineering register, "aporia signal" in cycle-phase register) is intentional and supported by the LEXICON; preserve both.

## 690. `$\delta_t$ mismatch signal`

**Alternatives proposed:** `$\delta_t$ mismatch signal`

_category: keep × 1_

- `$\delta_t$ mismatch signal` — **audit-471203-incremental:** [prose moved from candidate column]: "(keep; flag aporia gloss as pedagogical-only)" — "Mismatch signal" is fine and standard. "Aporia" is the philosophical gloss in LEXICON.md. Verdict: pedagogical only — the formalism doesn't use Greek terms structurally. The README claim that "each names a distinction the formalism makes that English alternatives flatten" is *overclaimed*. Auditor flags this for §F bigger-picture in FINAL. (Cycle phases, by extension: pedagogical labels for predict/observe/mismatch/update/act.) [from 18-def-mismatch-signal.md]

## 691. `$\delta_{\text{strategic}}$`

**Alternatives proposed:** `strategic calibration`

_category: add-alias × 1_

- `strategic calibration` — **sonnet-4-6-r2:** Edge residual aggregate. "Strategic calibration" is the established prose form in LEXICON.md. Formalize the alias.

## 692. `$\delta_{\text{strategic}}$ strategic calibration residual`

**Alternatives proposed:** `strategic calibration residual`

_category: add-alias × 1_

- `strategic calibration residual` — **opus-4-7-r2:** Already in use; confirm. The alias compresses to "the strategic residual" once the full form is established — this is fine as a within-paragraph compression.

## 693. `$\eta^\ast$ optimal update gain`

**Alternatives proposed:** `trust ratio`, `optimal update gain`, `trust ratio or confidence weighting`, `update gain`

_category: add-alias × 4_

- `trust ratio` — **gemini-3-1-pro-preview-r2:** Excellent prose alias suggested by Haiku; perfectly captures the $U_M / (U_M + U_o)$ intuition.
- `optimal update gain` — **opus-4-7-r2:** Already canonical in NOTATION.md and LEXICON.md; vote to confirm. The prose reads "the optimal update gain $\eta^\ast$" cleanly.
- `trust ratio or confidence weighting` — **haiku-4-5-r2:** Symbol is standard; prose often refers to "update weighting" and "trust weighting." The English-prose name would help in sentences like "the agent uses a trust-ratio of 0.7 on this channel." Weak preference; may be unnecessary.
- `update gain` — **opus-4-7-b:** See keep above. Prose: "update gain" in running text; $\eta^\ast$ only in formal expressions.

## 694. `$\iota_{ij}$ identifiability coefficient`

**Alternatives proposed:** `identifiability coefficient`

_category: add-alias × 1_

- `identifiability coefficient` — **opus-4-7-r2:** Already in use as "the identifiability coefficient $\iota_{ij}$"; confirm canonical. The Regime A/B/C boundary is named via this coefficient; consistent prose use compounds.

## 695. `$\kappa_{\text{eff}}$`

**Alternatives proposed:** `effective ambiguity coupling`

_category: add-alias × 1_

- `effective ambiguity coupling` — **codex-gpt-5-r2:** Makes the effective coupling variable legible.

## 696. `$\kappa_{\text{processing}}$ architectural coupling`

**Alternatives proposed:** `processing coupling`

_category: add-alias × 1_

- `processing coupling` — **opus-4-7-r2:** The full LaTeX subscript reads heavy in prose. "Processing coupling" or "the architectural coupling $\kappa$" is what the body of `#der-directed-separation` already uses; canonicalize. The Class 1/2/3 partition is named via this quantity; consistent prose use matters.

## 697. `$\lambda(M_t)$`

**Alternatives proposed:** `exploration weight`, `exploration multiplier`

_category: add-alias × 3_

- `exploration weight` — **gemini-3-1-pro-preview-r2:** Shorter prose alias for the exploration-exploitation balance weight.
- `exploration weight` — **opus-targeted-alternatives-v2:** Per Gemini r1 single-vote. The exploration-exploitation balance term in `#deriv-causal-ib-exploration`. Acceptable; weaker because the symbol $\lambda$ is also commonly the survival exponent ($\lambda_{\text{surv}}$); local-context-disambiguates is sufficient but fragile.
- `exploration multiplier` — **opus-targeted-alternatives-v2:** Variant. "Multiplier" reads as a coefficient on a baseline; "weight" reads as a probability-mass parameter. Both honest; pick by formula context.

## 698. `$\mathcal{A}(e_\tau)$`

**Alternatives proposed:** `observation ambiguity`

_category: add-alias × 1_

- `observation ambiguity` — **codex-gpt-5-r2:** Needed symbol-to-name binding in logogenic ambiguity work.

## 699. `$\mathcal{C}_t$ chronica`

**Alternatives proposed:** `chronica or interaction history`, `symbol name are locked`

_category: add-alias × 2_

- `chronica or interaction history` — **opus-4-7-r2:** Confirm. Both are in use; "chronica" carries the etymological / cycle-vocabulary commitment, "interaction history" is the engineering paraphrase. Both should remain available; the LEXICON's gloss already supplies both.
- `symbol name are locked` — **haiku-4-5-r2:** The Greek name "chronica" is elegant and the symbol is standard. No alias needed.

## 700. `$\phi$`

**Alternatives proposed:** `history compression`

_category: add-alias × 1_

- `history compression` — **gemini-3-1-pro-preview-r2:** Makes the operation concrete in prose.

## 701. `$\rho_\Sigma$`

**Alternatives proposed:** `strategy drift rate`, `strategic disturbance rate`

_category: add-alias × 3_

- `strategy drift rate` — **opus-targeted-alternatives-v2:** Per Sonnet's r1 single-vote +1. "Drift" carries the slow-structural-persistent connotation that $\rho_\Sigma$ has (rate of strategy-DAG structural change vs. fast environmental perturbation). Acceptable alias.
- `strategy drift rate` — **sonnet-4-6:** Alternative English gloss. "Drift" has appropriate connotations (slow, structural, persistent) vs "disturbance" (sudden, external).
- `strategic disturbance rate` — **opus-targeted-alternatives-v2:** Alternative. Parallels $\rho$ (disturbance rate) → $\rho_\Sigma$ (strategic disturbance rate) in vocabulary. Pairs cleanly with strategic-tempo $\mathcal{T}_\Sigma$ in the same register.

## 702. `$\rho_{i,\text{eff}}$`

**Alternatives proposed:** `effective disturbance`

_category: add-alias × 1_

- `effective disturbance` — **codex-gpt-5-r2:** Use the name wherever the max-with-zero construction is active.

## 703. `$\tilde{\delta}_t$`

**Alternatives proposed:** `variational aporia`

_category: add-alias × 1_

- `variational aporia` — **gemini-3-1-pro-preview-r2:** Greek equivalent for the score-function mismatch.

## 704. `$p_{ij}$`

**Alternatives proposed:** `edge credence`

_category: add-alias × 1_

- `edge credence` — **gemini-3-1-pro-preview-r2:** Better than "edge confidence weight", aligns with belief networks.

## 705. `$w(t)$`

**Alternatives proposed:** `mismatch injection`

_category: add-alias × 1_

- `mismatch injection` — **gemini-3-1-pro-preview-r2:** Clearer than generic "disturbance".

## 706. `AAD theoretical core vs ASF framework`

**Alternatives proposed:** `AAD vs ASF distinction`, `AAD ASF disambiguation`

_category: rename × 1, canonicalize × 1_

- `AAD vs ASF distinction` — **gemini-targeted-alternatives:** Clarifies that AAD is the theory while ASF is the application framework.
- `AAD ASF disambiguation` — **opus-4-7-r2:** The terms are distinct: AAD is the mathematical core (Sections I/II/III + Appendices); ASF is the parent framework that includes AAD plus TST plus logogenic/logozoetic. Canonicalize: when discussing the math, "AAD"; when discussing the framework as a whole, "ASF"; when discussing a domain instantiation, the specific component name (TST, logogenic-agents, logozoetic-agents).

## 707. `CIY causal information yield`

**Alternatives proposed:** `causal information yield action distinguishability`, `action distinguishability`, `interventional contrast`

_category: rename × 3_

- `causal information yield action distinguishability` — **audit-471203-incremental:** Real term-vs-substance mismatch. "Yield" connotes learning/profit; segment goes to substantial trouble to clarify CIY measures *action-distinguishability*, not learning value. Auditor: "the mismatch between name and substance is mildly misleading even though the segment corrects it." Compromise candidate: keep CIY formally, lean on "action-distinguishability" as substantive gloss. [from 21-def-causal-information-yield.md] [one of 3 alternatives proposed in the original audit row]
- `action distinguishability` — **audit-471203-incremental:** Real term-vs-substance mismatch. "Yield" connotes learning/profit; segment goes to substantial trouble to clarify CIY measures *action-distinguishability*, not learning value. Auditor: "the mismatch between name and substance is mildly misleading even though the segment corrects it." Compromise candidate: keep CIY formally, lean on "action-distinguishability" as substantive gloss. [from 21-def-causal-information-yield.md] [one of 3 alternatives proposed in the original audit row]
- `interventional contrast` — **audit-471203-incremental:** Real term-vs-substance mismatch. "Yield" connotes learning/profit; segment goes to substantial trouble to clarify CIY measures *action-distinguishability*, not learning value. Auditor: "the mismatch between name and substance is mildly misleading even though the segment corrects it." Compromise candidate: keep CIY formally, lean on "action-distinguishability" as substantive gloss. [from 21-def-causal-information-yield.md] [one of 3 alternatives proposed in the original audit row]

## 708. `CIY observational proxy`

**Alternatives proposed:** `CIY observational proxy`, `observational CIY`, `observational proxy`

_category: keep × 2, rename × 2_

- `CIY observational proxy` — **haiku-4-5:** When CIY is estimable from observational data. Compound but accurate. Keep.
- `CIY observational proxy` — **opus-4-7-r2:** Weak keep. Names where CIY is estimable from observational data; the slug is accurate but heavy. Acceptable.
- `observational CIY` — **sonnet-4-6-r2:** "CIY-observational-proxy" reads as CIY-in-the-observational-regime, which is what it is — when CIY is estimable from observational data. Reordering to "observational-CIY" puts the key restriction first. Still contains an acronym, but CIY is used enough to be recognizable.
- `observational proxy` — **gemini-3-1-pro-preview-r2:** Shorter.

## 709. `OODA4 framework enforcing adaptive cycle separation`

**Alternatives proposed:** `agentic scaffold`

_category: name-unnamed × 1_

- `agentic scaffold` — **codex-gpt-5-r2:** Useful logogenic implementation term, but keep it downstream of directed-separation machinery.

## 710. `a1 a2 a3 a4`

**Alternatives proposed:** `macro dynamic admissibility`, `aporia phase`

_category: canonicalize × 1, rename × 1_

- `macro dynamic admissibility` — **codex-gpt-5-r2:** Good umbrella for the macro-agent constraints in composition closure.
- `aporia phase` — **gemini-targeted-alternatives:** Collectivizes the mismatch/aporia breakdown.

## 711. `adversarial edge target argmax`

**Alternatives proposed:** `edge targeting optimum`, `adversarial edge targeting`

_category: name-unnamed × 1, rename × 1_

- `edge targeting optimum` — **codex-gpt-5-r2:** Good name for the emitter-recipient 16-cell targeting solution.
- `adversarial edge targeting` — **gemini-targeted-alternatives:** Simplifies the formal term into a more readable prose description.

## 712. `agent visible but objective irrelevant metric`

**Alternatives proposed:** `vanity metric`, `irrelevant visibility artifact`

_category: add-alias × 1, rename × 1_

- `vanity metric` — **codex-gpt-5-r2:** Standard operational term that AAD can formalize as high observability with low causal relevance to O_t.
- `irrelevant visibility artifact` — **gemini-targeted-alternatives:** Formally names the failure mode where a metric is observable but unlinked to the goal.

## 713. `and or scope`

**Alternatives proposed:** `and or scope`

_category: keep × 2_

- `and or scope` — **haiku-4-5:** Conjunctive/disjunctive scope. Self-descriptive. Keep.
- `and or scope` — **opus-4-7-b:** Keep. The slug is short, announces the formalism restriction ("AND/OR only"), and is directly cite-able.

## 714. `bathtub analogy for persistence condition`

**Alternatives proposed:** `leaky bathtub analogy`, `bathtub model`, `walton bathtub`

_category: rename × 2, canonicalize × 1_

- `leaky bathtub analogy` — **gemini-targeted-alternatives:** Secures the pedagogic tool for the disturbance/correction dynamic.
- `bathtub model` — **opus-targeted-alternatives-v2:** Per Codex r1 single +2 and CLAUDE.md §"Feynman-criterion plain-language briefs": Alan Walton's bathtub gloss is the canonical communal-imagination example for the persistence condition. Promote to first-class vocabulary; "the bathtub model" / "Walton's bathtub" both work.
- `walton bathtub` — **opus-targeted-alternatives-v2:** Variant — credit-attribution form. Per CLAUDE.md the gloss came from Alan Walton on first encounter; the eponymous form preserves the communal-imagination origin story. Acceptable.

## 715. `beta a2 assumed sub scope`

**Alternatives proposed:** `cyclic game sub scope`, `assumed sector regime`

_category: rename × 2_

- `cyclic game sub scope` — **gemini-targeted-alternatives:** Connects sub-scope beta directly to its non-convergent nature.
- `assumed sector regime` — **codex-1:** Not elegant, but much more informative than a bare beta when the distinction is whether the sector condition is assumed rather than derived.

## 716. `cadentia`

**Alternatives proposed:** `adaptive tempo`, `cadentia`, `channel rate`, `cognitive rhythm`

_category: rename × 4, keep × 1_

- `adaptive tempo` — **gemini-targeted-alternatives:** Replaces the Latin with the exact AAD terminology.
- `cadentia` — **opus-targeted-alternatives-v2:** Per `def-proprium-mapping`: "CADENTIA: The temporal structure of the loop (PULSUS/VIGILIAE), defining the agent's channel rates ($\nu^{(k)}$)." Names the *cycle's tempo structure* — the channel-rate vector $\{\nu^{(k)}\}$ that grounds adaptive-tempo $\mathcal{T}$. "Cadence" in English carries the *rhythm* sense; the Latinate form preserves the PROPRIUM register. Keep.
- `channel rate` — **opus-targeted-alternatives-v2:** Plain-English, mechanism-first. Names what the segment defines ($\{\nu^{(k)}\}$). Loses the PULSUS/VIGILIAE substructure naming convention but gains the immediate connection to `#def-adaptive-tempo`. Good if the PROPRIUM register is being deprecated; weak otherwise.
- `cognitive rhythm` — **gemini-2:** "Cadentia" is poetic but opaque. "Cognitive rhythm" clearly describes the temporal structure of the loop.
- `cognitive rhythm` — **opus-targeted-alternatives-v2:** Considered (Gemini's r1 proposal). Same problem as causal-lock for indivisum: register mismatch with the rest of PROPRIUM. The Latin terms travel together or not at all.

## 717. `canonical formulation`

**Alternatives proposed:** `canonical formulation`, `working canon`

_category: canonicalize × 1, keep × 1, rename × 1_

- `canonical formulation` — **opus-4-7-r2:** The middle ring in FORMAT.md's three-rings; in use but slightly redundant ("canonical" + "formulations" both name the chosen-among-alternatives quality). Acceptable canonicalization.
- `canonical formulation` — **opus-targeted-alternatives:** Per FORMAT.md three-ring framing: inevitability core / canonical formulations / empirical-heuristic-discussion. "Canonical" carries the second-ring sense (well-grounded, project-standard, not necessarily the unique form). Keep.
- `working canon` — **opus-targeted-alternatives:** Considered. "Working canon" carries a tentativeness that "canonical" does not — and FORMAT.md's three-ring structure does want "canonical" to mean *settled if not unique*. Rejected.

## 718. `catastrophic forgetting regime`

**Alternatives proposed:** `catastrophic forgetting regime`, `empty window pathology`

_category: keep × 1, add-alias × 1_

- `catastrophic forgetting regime` — **codex-gpt-5-r2:** Established term, and it maps cleanly to the empty feasibility window.
- `empty window pathology` — **codex-gpt-5-r2:** Good mechanism alias. Do not replace catastrophic forgetting when citing ML lineage.

## 719. `causal OODA1 LMI`

**Alternatives proposed:** `matrix survival bound`, `causal OODA1 LMI`

_category: rename × 1, keep × 1_

- `matrix survival bound` — **codex-gpt-5-r2:** The LMI is the technique. The subject is the matrix survival constraint that fixes the blank-wall failure.
- `causal OODA1 LMI` — **gemini-3-1-pro-preview-r2:** Descriptive of the underlying math.

## 720. `chronica brief gloss`

**Alternatives proposed:** `interaction history chronica`

_category: rename × 1_

- `interaction history chronica` — **gemini-targeted-alternatives:** Pairs the Greek term with its English translation for accessibility.

## 721. `claim the proposition the segment carry`

**Alternatives proposed:** `segment claim`, `claim`

_category: rename × 1, canonicalize × 1_

- `segment claim` — **gemini-targeted-alternatives:** Clarifies what a segment is asserting.
- `claim` — **opus-4-7-r2:** Confirm. The pairing "segment carries a claim" is the right vocabulary; avoid "assertion," "statement," "result" (which is a specific type).

## 722. `class 2 scope exit`

**Alternatives proposed:** `class 2 scope boundary`, `class 2 scope exit`

_category: rename × 1, canonicalize × 1_

- `class 2 scope boundary` — **gemini-targeted-alternatives:** The limit where fully merged agents break directed separation.
- `class 2 scope exit` — **opus-4-7-r2:** The phrase "scope exit" for Class 2 (handing off to logogenic-agents/) is repeated in `#der-directed-separation` Findings and README. Canonicalize as the named methodological move — explicit-scope-exit-rather-than-unenforced-approximation is what the segment claims as its contribution.

## 723. `cognitive substrate gemini logostratum proposal`

**Alternatives proposed:** `logostratum`

_category: keep × 1_

- `logostratum` — **opus-targeted-alternatives-v2:** Per `def-proprium-mapping`. See logostratum row above.

## 724. `completeness c3`

**Alternatives proposed:** `predictive completeness behavioral completeness`, `predictive completeness`

_category: name-unnamed × 1, rename × 1_

- `predictive completeness behavioral completeness` — **audit-471203-incremental:** The term bundles two distinct properties: (i) $M_t$ retains all relevant info from history (sufficiency), (ii) the agent's behavior depends only on $M_t$ (Markov-of-policy). Two terms would be cleaner. [from 15-der-recursive-update.md]
- `predictive completeness` — **gemini-targeted-alternatives:** Separates it explicitly from behavioral completeness to clarify what $M_t$ retains from history.

## 725. `composition route c i c ii c iii c iv`

**Alternatives proposed:** `composition route`, `composition pathway`

_category: canonicalize × 1, rename × 1_

- `composition route` — **opus-targeted-alternatives-v2:** Per Codex r1 +3 single. Use "routes" consistently for shared-objective / hierarchical / mutual-benefit / strategic composition. Confirms across my independent read of `form-composition-closure`, `deriv-strategic-composition`, `hyp-symbiogenic-composition`.
- `composition pathway` — **opus-targeted-alternatives-v2:** Variant. "Pathway" connects to the strategy-DAG vocabulary (paths through the DAG). Weaker because "route" is shorter and the C-i...C-iv vocabulary already implies discrete options.

## 726. `composition scope condition`

**Alternatives proposed:** `composition scope condition`, `composite agent condition`, `teleological alignment condition`

_category: keep × 2, rename × 2_

- `composition scope condition` — **haiku-4-5:** Teleological alignment required for composite-agent status. Parallel naming to #scope-condition. Acceptable. Keep.
- `composition scope condition` — **opus-4-7-b:** Keep. Honest, direct.
- `composite agent condition` — **codex-1:** The core decision is whether a composite agent exists, not whether "composition" is in scope in some generic sense.
- `teleological alignment condition` — **gemini-2:** More descriptive of the actual requirement (alignment) for composite status.

## 727. `concept the strengthening of satisfaction gap and control regret diagnostic across the c1 c2 c3 hierarchy naming both the strengthening pattern and the underlying ordered result that produce it`

**Alternatives proposed:** `inferential force cascade`, `the convention monotonicity`, `inferential cascade`

_category: name-unnamed × 4_

- `inferential force cascade` — **agent1-original-brainstorm:** Low priority but worth noting. Pedagogical. [original phrasing: unnamed: convention-hierarchy monotonicity cascade / satisfaction-gap-and-control-regret strengthening across C1→C3]
- `inferential force cascade` — **opus-4-7-b:** The pattern "under C1 diagnostics are weak, C2 they sharpen, C3 they're global" — currently explained in prose every time it comes up (which is several places). "Inferential-force cascade" gives the pattern a name. Mirrors `#orient-cascade` in structure (both cascades are ordered resolutions) and the parallel is pedagogically useful. [original phrasing: unnamed: cascade of inferential force through C1/C2/C3]
- `the convention monotonicity` — **opus-4-7-r2:** The result $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ inside `#def-value-object` is a monotonicity result that downstream segments cite repeatedly (orient cascade, satisfaction-gap, control-regret all use it). It deserves a slug-noun in the Convention Hierarchy lineage — even if it stays as a sub-claim within `#def-value-object`. "Convention monotonicity" is what `disc-approximation-tiering` reaches for. [original phrasing: unnamed: the C1/C2/C3 monotonicity result]
- `inferential cascade` — **opus-1m:** Agree with original. Low priority. [original phrasing: unnamed: cascade of inferential force strengthening from C1 to C3 on satisfaction-gap / control-regret diagnostics]

## 728. `concept walton plain language analog for the persistence condition fluid level as belief reality gap inflow as reality change rate outflow as learning rate container size as adaptive reserve`

**Alternatives proposed:** `bathtub model`, `the bathtub model`

_category: name-unnamed × 2_

- `bathtub model` — **codex-gpt-5-r2:** Useful teaching name if the README adds Alan's bathtub gloss. [original phrasing: bathtub analogy for persistence condition]
- `the bathtub model` — **opus-4-7-r2:** Confirmation with new reasoning — Codex named this at +2 (without explicit canonicalization) and I want to lift it: CLAUDE.md mentions Walton's bathtub gloss as the canonical Feynman-criterion benchmark for *plain-language briefs*. The bathtub gloss is one example; the *family of plain-language analogs* (bathtub, leaky bucket, savings vs withdrawal, etc.) deserves a family name. "The bathtub model" is fine for the persistence-condition specific case; the family would be something like "Feynman-grade analogs" — but I'd defer that to a future round. [original phrasing: unnamed: an organizational-level instance of the persistence condition's bathtub gloss]

## 729. `conspectus`

**Alternatives proposed:** `active context`, `model sufficiency`, `conspectus`, `pre event state`

_category: rename × 4, keep × 1_

- `active context` — **gemini-2:** "Conspectus" is archaic. "Active context" clearly maps to $M_{\tau^-}$ assembled for processing.
- `active context` — **opus-targeted-alternatives-v2:** Considered (Gemini's r1 proposal). Plain-English, immediately legible — and "active context" is software-engineering vocabulary that AAD readers will recognize. Weak because of register-mismatch (same argument as for indivisum / cadentia).
- `model sufficiency` — **gemini-targeted-alternatives:** Replaces the Latin with the established epistemic metric.
- `conspectus` — **opus-targeted-alternatives-v2:** Per `def-proprium-mapping`: "CONSPECTUS: The assembled pre-event state ($X_{\tau^-}$) loaded into the active context window." Names the *active-context state* in a register-coherent way with the rest of PROPRIUM. The Latin earns its keep by enabling the iconic eight-component CONSPECTUS/PERCEPTA/ACTUS/CADENTIA/LOGOSTRATUM list.
- `pre event state` — **opus-targeted-alternatives-v2:** Considered. Names the formal mathematical object ($X_{\tau^-}$) directly. Rejected: too compositional, fails communal-imagination test. The segment's contribution is *naming* the assembled-pre-event-state; "pre-event-state" doesn't add a name, just describes.

## 730. `correlation hierarchy`

**Alternatives proposed:** `correlation ladder`

_category: rename × 2_

- `correlation ladder` — **codex-gpt-5-r2:** A reasonable alternative if separability ladder lands and the project wants fewer internal hierarchies. Weak because hierarchy is already established.
- `correlation ladder` — **opus-1m:** Conditionally admit the rename only if other ladder-renames land; otherwise keep. Weak.

## 731. `default internal processing before output`

**Alternatives proposed:** `deliberation lag`, `interior baseline`

_category: rename × 1, name-unnamed × 1_

- `deliberation lag` — **gemini-targeted-alternatives:** Translates internal processing to its temporal cost.
- `interior baseline` — **codex-gpt-5-r2:** Useful for logozoetic prose, but lower confidence because it may sound too generic.

## 732. `derivation audit table heading`

**Alternatives proposed:** `derivation audit`

_category: canonicalize × 1_

- `derivation audit` — **opus-targeted-alternatives-v2:** Per FORMAT.md and Sonnet/Opus r1 single +1 each (different agents). The longer form ("What Is Derived vs. What Is Chosen") is descriptive but wordy. "Derivation Audit" earns the slot — names the practice and the artifact.

## 733. `distributed tempo`

**Alternatives proposed:** `distributed tempo`, `network tempo`

_category: keep × 1, rename × 1_

- `distributed tempo` — **codex-gpt-5-r2:** Good team-level tempo extension.
- `network tempo` — **codex-1:** Shorter and easier to say aloud. The important content is tempo distributed across a communication network.

## 734. `eli the agent type`

**Alternatives proposed:** `eli agent`, `eli`

_category: keep × 2_

- `eli agent` — **gemini-targeted-alternatives:** Legacy or specific instantiated agent type.
- `eli` — **opus-4-7-r2:** Acceptable keep — established in the firmatum / shoshin lineage. The acronym discipline check passes (used as a noun throughout the logozoetic corpus).

## 735. `empirical heuristic discussion third ring`

**Alternatives proposed:** `heuristic ring`, `calibration ring`

_category: rename × 2_

- `heuristic ring` — **gemini-targeted-alternatives:** Streamlines the epistemic tier designation.
- `calibration ring` — **sonnet-4-6:** The current name ("Empirical, heuristic, discussion") is a list, not a name. "Calibration ring" would give it a single handle. Alternatively: "open-world ring" (these are the segments that must face falsification).

## 736. `escape route`

**Alternatives proposed:** `escape route`, `floor escape`

_category: canonicalize × 1, rename × 1_

- `escape route` — **opus-targeted-alternatives-v2:** Per `#disc-identifiability-floor`: characterizes the *unique broadly-available escape* from the floor (the M1 meta-pattern). Multiple variant phrasings ("escape the floor," "boundary characterization," "unique escape") collapse to "escape route." Confirms Opus r1 single +1 and aligns with the floor-as-named-object discipline.
- `floor escape` — **opus-targeted-alternatives-v2:** Considered. Tighter compound. Rejected: "escape route" is the vocabulary the segment uses; "floor-escape" reads forced.

## 737. `evaluation metric`

**Alternatives proposed:** `logogenic diagnostic`, `evaluation metric`

_category: keep × 2, rename × 1_

- `logogenic diagnostic` — **codex-gpt-5-r2:** Evaluation metrics is generic. The observation segment is about diagnostics for logogenic agents.
- `evaluation metric` — **opus-4-7-r2:** Weak keep — slightly generic. "Evaluation metrics" doesn't tell the reader what's being measured. Could be specialized to "#obs-mt-quality-measurement" or similar but the current form is workable.
- `evaluation metric` — **sonnet-4-6-r2:** Standard term for what the segment covers.

## 738. `fisher whitened update rule`

**Alternatives proposed:** `fisher update`, `fisher whitened update rule`, `fisher whitened update`

_category: rename × 2, keep × 2_

- `fisher update` — **gemini-3-1-pro-preview-r2:** Shorter, whitened is implied by Fisher.
- `fisher whitened update rule` — **haiku-4-5:** Fisher-whitened edge update under correlated evidence. Specialist vocabulary (Fisher whitening / Mahalanobis metric) but precise. Keep.
- `fisher whitened update rule` — **opus-4-7-b:** Keep. The Fisher-whitening mechanism is the segment's headline; "update rule" grounds it in the AAD update vocabulary.
- `fisher whitened update` — **sonnet-4-6:** Dropping "rule" is minor but the segment is about the update equation, not an operational rule. Either works; slight preference for shorter form.

## 739. `gate 1 2 3 4`

**Alternatives proposed:** `gate 1 2 3 4`, `dependency content mechanical wn gate`

_category: keep × 1, add-alias × 1_

- `gate 1 2 3 4` — **opus-targeted-alternatives-v2:** Numbered-gates is established and pronounceable. Adding word names is value-additive but not value-essential. The keep is robust.
- `dependency content mechanical wn gate` — **opus-targeted-alternatives-v2:** Per FORMAT.md promotion gates. The numbers do most referencing work in conversation ("passed Gate 2") but the one-word names would help fresh readers. Acceptable canonicalization.

## 740. `gemini analysis paralysis for excessive deliberation`

**Alternatives proposed:** `deliberation gridlock`, `reject analysis paralysis`

_category: rename × 1, rebuttal × 1_

- `deliberation gridlock` — **gemini-targeted-alternatives:** Formalizes the over-thinking failure mode.
- `reject analysis paralysis` — **sonnet-4-6-r2:** Gemini proposed "analysis paralysis" (+3) for the condition where $\rho_\text{delib} \cdot \Delta\tau$ exceeds the epistemic benefit of deliberating. "Analysis paralysis" is common-language baggage with a completely different connotation (cognitive overload causing decision-making to fail). The AAD mechanism is that the model goes *stale* during deliberation (the world changes faster than deliberation adds value) — this is a *model staleness* problem, not a cognitive paralysis. The deliberation-cost derivation already has a clean name (`der-deliberation-cost`); if the threshold deserves a name it should be "staleness threshold" or "deliberation horizon," not a borrowed phrase that misnames the mechanism.

## 741. `glue code`

**Alternatives proposed:** `agentic scaffold`, `structural coordination overhead`

_category: rename × 2_

- `agentic scaffold` — **gemini-3-1-pro-preview-r2:** Demeans the framework. Prefer "agentic scaffold" or "Orient Cascade enforcement mechanism" (alternative).
- `structural coordination overhead` — **gemini-targeted-alternatives:** Maps the TST term to the AAD formal equivalent.

## 742. `greek rooted vocabulary`

**Alternatives proposed:** `greek philosophical vocabulary`, `greek rooted vocabulary`

_category: canonicalize × 1, keep × 1_

- `greek philosophical vocabulary` — **codex-gpt-5-r2:** Philosophical is the useful qualifier: these are not arbitrary Greek labels, but inherited conceptual terms.
- `greek rooted vocabulary` — **gemini-targeted-alternatives:** Secures the five-phase terminology (prolepsis, aisthesis, aporia, epistrophe, praxis).

## 743. `hierarchy as repeated word`

**Alternatives proposed:** `hierarchy`, `reserve for pearl rename other selectively`

_category: keep × 1_

- `hierarchy` — **gemini-targeted-alternatives:** Core organizational concept (causal, correlation, convention).
- `reserve for pearl rename other selectively` — **agent1-original-brainstorm:** Weak proposal. Four uses in the framework (Pearl's, convention, correlation, approximation-tiering) is likely too many. Partial disambiguation via correlation→correlation-ladder and convention→continuation-hierarchy.

## 744. `integration of four discipline as the framing of AAD contribution`

**Alternatives proposed:** `four discipline synthesis`, `epistemic architecture`

_category: rename × 1, canonicalize × 1_

- `four discipline synthesis` — **gemini-targeted-alternatives:** Concise framing of the framework context.
- `epistemic architecture` — **sonnet-4-6-r2:** PROPOSALS §Bundle 1 notes that three independent frontier-model audits converged on reframing AAD from "integration of four disciplines" to "epistemic architecture for bounded correction." The README still leads with the integration framing. This vote canonicalizes "epistemic architecture" as the primary positioning term — integration is a method, not the contribution. The contribution is the architecture.

## 745. `internal external decomposition`

**Alternatives proposed:** `viability decomposition`, `boundary decomposition`

_category: rename × 2_

- `viability decomposition` — **sonnet-4-6-r2:** The file lacks the role-prefix (the slug `internal-external-decomposition` has no type prefix). The content is a derivation of the log-additive split of viability into internal health + environmental affordance. "Viability decomposition" names the thing (viability) and what happens to it (decomposition). The role-prefix `deriv-` would be applied mechanically by `bin/align-slug`; this vote is on the subject-noun only.
- `boundary decomposition` — **gemini-3-1-pro-preview-r2:** "Boundary" defines what is being decomposed.

## 746. `interpre`

**Alternatives proposed:** `context mediator`, `epistemic substate`, `interpre`, `controller loop`

_category: rename × 4, keep × 1_

- `context mediator` — **gemini-2:** "Interpres" is Latin-heavy. "Context mediator" exactly describes the infrastructure mediating $M_t$ and the substrate.
- `context mediator` — **opus-targeted-alternatives-v2:** Considered (Gemini's r1 proposal). Genuinely good description of what an interpres does (mediates $M_t$ and the substrate per the PROPRIUM architecture). Trade-off: leaves the rest of PROPRIUM's Latin coherent but breaks the symmetry; the connection to firmatum/shoshin source code is weakened.
- `epistemic substate` — **gemini-targeted-alternatives:** Replaces the Latin with the $M_t$ structural terminology.
- `interpre` — **opus-targeted-alternatives-v2:** Latin sits in the PROPRIUM/Logostratum register (per `~/src/firmatum/PROPRIUM-ARCHITECTURE.md` lineage). Same register-coherence argument as the above. Weaker keep because "interpres" reads the most opaque of the PROPRIUM Latinate terms — least communal-imagination-ready.
- `controller loop` — **opus-targeted-alternatives-v2:** Considered. Matches the shoshin code (Interpres is the controller-loop in the prototype). Rejected: "controller-loop" pulls from control-theory in a way that collides with AAD's existing controller / agent / loop vocabulary.

## 747. `l1`

**Alternatives proposed:** `level 1 associational`, `l1 c`

_category: canonicalize × 1, rename × 1_

- `level 1 associational` — **gemini-targeted-alternatives:** Expands to full definition.
- `l1 c` — **agent1-original-brainstorm:** Too technical; uses symbol.

## 748. `lindy baseline`

**Alternatives proposed:** `lindy baseline`, `structural persistence baseline`

_category: add-alias × 1, rename × 1_

- `lindy baseline` — **codex-gpt-5-r2:** Useful alias for change-expectation baselines derived from survival age.
- `structural persistence baseline` — **gemini-targeted-alternatives:** More descriptive than "lindy".

## 749. `logostratum`

**Alternatives proposed:** `logostratum`, `cognitive substrate`

_category: keep × 1, rename × 1_

- `logostratum` — **opus-targeted-alternatives-v2:** Per `def-proprium-mapping`: "LOGOSTRATUM: The underlying logogenic substrate (e.g., the LLM backbone) that implements the update function $f_X$." The compound *logos* + *stratum* (language + layer) names exactly what the segment defines: the linguistic substrate as architectural layer. Connection to logogenic-agents is direct in the morphology. Keep.
- `cognitive substrate` — **opus-targeted-alternatives-v2:** Considered (Gemini's r1 proposal). "Cognitive substrate" is generic; "logostratum" is project-specific to the PROPRIUM lineage. Rejected: loses the *logogenic* connection that the morphology carries.

## 750. `logostratum rlhf4 backbone`

**Alternatives proposed:** `logogenic architecture`

_category: rename × 1_

- `logogenic architecture` — **gemini-targeted-alternatives:** Standardizes the structural description.

## 751. `low mixed high ambiguity event mix`

**Alternatives proposed:** `ambiguity profile`, `ambiguity stratified event mix`

_category: name-unnamed × 1, rename × 1_

- `ambiguity profile` — **codex-gpt-5-r2:** Useful empirical descriptor for event-stream composition.
- `ambiguity stratified event mix` — **gemini-targeted-alternatives:** Cleaner formulation of the observation mix.

## 752. `matrix CIY tensor CIY`

**Alternatives proposed:** `matrix causal information yield`, `fisher CIY`, `matrix CIY consistent`

_category: canonicalize × 2, rename × 1_

- `matrix causal information yield` — **gemini-targeted-alternatives:** Expands the scalar CIY into full-state spaces.
- `fisher CIY` — **audit-471203-incremental:** Inconsistent terminology in `#disc-ciy-unified-objective`: both "Matrix CIY" and "$\mathcal{I}_o(a)$"/Fisher Information Matrix appear. Auditor proposes: "Fisher CIY" might be most specific; in any case, pick one for any future Brief. [from 39-42-section-ii-ciy-strategy-chain.md] [one of 2 alternatives proposed in the original audit row]
- `matrix CIY consistent` — **audit-471203-incremental:** Inconsistent terminology in `#disc-ciy-unified-objective`: both "Matrix CIY" and "$\mathcal{I}_o(a)$"/Fisher Information Matrix appear. Auditor proposes: "Fisher CIY" might be most specific; in any case, pick one for any future Brief. [from 39-42-section-ii-ciy-strategy-chain.md] [one of 2 alternatives proposed in the original audit row]

## 753. `maximum useful chain depth`

**Alternatives proposed:** `maximum useful chain depth`, `maximum viable chain depth`

_category: canonicalize × 1, rename × 1_

- `maximum useful chain depth` — **codex-gpt-5-r2:** Important derived bound; keep the plain descriptive name.
- `maximum viable chain depth` — **gemini-targeted-alternatives:** More precise: past this depth, edges are uncorrectable.

## 754. `model synchronization cost reversal under ambiguity`

**Alternatives proposed:** `synchronization cost reversal`, `ambiguity reversal`

_category: rename × 1, name-unnamed × 1_

- `synchronization cost reversal` — **gemini-targeted-alternatives:** Captures the phase shift where coordination becomes deleterious.
- `ambiguity reversal` — **codex-gpt-5-r2:** Names the case where Auftragstaktik bandwidth ordering reverses, but this needs more formal support.

## 755. `nominal coupling`

**Alternatives proposed:** `query bound`, `attention bound`, `epistemic only`, `query coupling`, `attentional coupling`, `query bound agency`

_category: rename × 6_

- `query bound` — **audit-471203-incremental:** "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md] [one of 5 alternatives proposed in the original audit row]
- `attention bound` — **audit-471203-incremental:** "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md] [one of 5 alternatives proposed in the original audit row]
- `epistemic only` — **audit-471203-incremental:** "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md] [one of 5 alternatives proposed in the original audit row]
- `query coupling` — **audit-471203-incremental:** "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md] [one of 5 alternatives proposed in the original audit row]
- `attentional coupling` — **audit-471203-incremental:** "Forgettable term." What it actually names is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. The term is structurally important (justifies TST queries-as-interventions; structurally important for logogenic agents) but the current name doesn't carry the weight. [from 08-post-causal-structure.md] [one of 5 alternatives proposed in the original audit row]
- `query bound agency` — **gemini-targeted-alternatives:** Better captures agency where the effect is on what's *seen* rather than what *happens* (attention-bound).

## 756. `observation design lever reducing ambiguity`

**Alternatives proposed:** `ambiguity damping`, `ambiguity mitigation lever`

_category: name-unnamed × 1, rename × 1_

- `ambiguity damping` — **codex-gpt-5-r2:** Good name for interventions that lower observation ambiguity before the update.
- `ambiguity mitigation lever` — **gemini-targeted-alternatives:** Translates the design choice into an active mechanism.

## 757. `ooda4 agent as act agent logogenic`

**Alternatives proposed:** `ooda4 classification`

_category: rename × 1_

- `ooda4 classification` — **gemini-targeted-alternatives:** Boyd-based taxonomy for agent architectures.

## 758. `ooda4 framework enforcing adaptive cycle separation`

**Alternatives proposed:** `ooda4 cycle separation`

_category: rename × 1_

- `ooda4 cycle separation` — **gemini-targeted-alternatives:** Connects the Boyd framework to the strict AAD adaptive cycle phases.

## 759. `out of band time marker for RLHF4 agent`

**Alternatives proposed:** `time delta marker`

_category: name-unnamed × 1_

- `time delta marker` — **codex-gpt-5-r2:** More sober than visual time delta and useful for defining tempo in context-bound agents.

## 760. `out of band time marker for rlhf4 agent`

**Alternatives proposed:** `exogenous temporal marker`

_category: rename × 1_

- `exogenous temporal marker` — **gemini-targeted-alternatives:** Clarifies that these markers originate outside the agent loop.

## 761. `p1 p2 p3`

**Alternatives proposed:** `projection admissibility`, `predictive sufficiency hierarchy`

_category: canonicalize × 1, rename × 1_

- `projection admissibility` — **codex-gpt-5-r2:** The three projection constraints need this umbrella.
- `predictive sufficiency hierarchy` — **gemini-targeted-alternatives:** Names the specific content of the p1-p3 progression.

## 762. `pearl-level 2 causal contrast`

**Alternatives proposed:** `level 2 interventional contrast`, `pearl-level 2 causal contrast`

_category: rename × 1, keep × 1_

- `level 2 interventional contrast` — **gemini-targeted-alternatives:** More descriptive of the mathematical mechanism.
- `pearl-level 2 causal contrast` — **audit-471203-incremental:** [Brief-field gloss candidate, not a name vote]: "the agent's choice actually changes what happens" — Brief-grade gloss only. The formal name is doing real work; the layperson translation is missing from any Brief field. [from 06-scope-agency.md] [original row: canonicalize vote on prose gloss; recategorized as keep-with-gloss-in-notes since glosses aren't name proposals.]

## 763. `principled decision integration`

**Alternatives proposed:** `temporal decision integration`, `principled decision integration`

_category: keep × 2, rename × 1_

- `temporal decision integration` — **codex-gpt-5-r2:** Principled is praise, not a subject noun. The derivation integrates decisions over temporal expected cost.
- `principled decision integration` — **opus-4-7-b:** Keep.
- `principled decision integration` — **sonnet-4-6-r2:** "Principled decision integration" — the optimal changeset-composition result. Verbose but accurate.

## 764. `promote in topological order`

**Alternatives proposed:** `topological promotion`, `topological promotion order`

_category: rename × 2_

- `topological promotion` — **gemini-targeted-alternatives:** Formalizes the dependency-ordered maturity process.
- `topological promotion order` — **sonnet-4-6:** FORMAT.md uses this phrase but doesn't name it as a convention. "Topological promotion" as a named methodology would make the gate-ordering rule easy to reference.

## 765. `prompt engineering`

**Alternatives proposed:** `ambiguity modulation`, `observation boundary tuning`

_category: rename × 2_

- `ambiguity modulation` — **gemini-3-1-pro-preview-r2:** Avoid this unprincipled term; prefer "ambiguity modulation" ($\mathcal{A}$) or "zero-ambiguity conditioning" (alternative).
- `observation boundary tuning` — **gemini-targeted-alternatives:** Recontextualizes the practice in AAD formal terms.

## 766. `quality to tempo chain`

**Alternatives proposed:** `quality to tempo chain`

_category: canonicalize × 1_

- `quality to tempo chain` — **codex-gpt-5-r2:** Useful TST bridge phrase from code quality to observation noise, gain, tempo, and persistence.

## 767. `readme md maturity gradient`

**Alternatives proposed:** `readme md maturity gradient`, `readme md theory maturity gradient`

_category: keep × 2, rename × 1_

- `readme md maturity gradient` — **opus-4-7-b:** Keep. "Gradient" is exactly what the sections-I-through-III closure-profile is (not a staircase; a gradient).
- `readme md maturity gradient` — **opus-4-7:** Fine. Keep.
- `readme md theory maturity gradient` — **codex-1:** Adds just enough specificity to stop the heading from sounding like a generic project-health label.

## 768. `readme md novel result`

**Alternatives proposed:** `readme md novel result`

_category: keep × 2_

- `readme md novel result` — **opus-4-7-b:** Keep. "Novel" is load-bearing (these are AAD's own contributions, distinct from the integrated-prior-art); the section discipline is tight here.
- `readme md novel result` — **opus-4-7:** Fine; perhaps "Results that Emerge at the Joints" to match the theory's integration-over-invention framing, but that's longer and less grep-able. Weak keep.

## 769. `regime a regime b regime c`

**Alternatives proposed:** `identification regime`, `admissibility regime`

_category: canonicalize × 1, rename × 1_

- `identification regime` — **codex-gpt-5-r2:** Good umbrella for intervention-rich, partial-intervention, and observational settings.
- `admissibility regime` — **gemini-targeted-alternatives:** Elevates the abstract A/B/C to their functional role.

## 770. `replayed pseudo event`

**Alternatives proposed:** `replay event`, `simulated event playback`

_category: canonicalize × 1, rename × 1_

- `replay event` — **codex-gpt-5-r2:** Shorter handle for consolidation updates that carry no new external information.
- `simulated event playback` — **gemini-targeted-alternatives:** Clearer terminology for the offline consolidation mechanism.

## 771. `simulation result`

**Alternatives proposed:** `simulation result`

_category: keep × 2_

- `simulation result` — **haiku-4-5:** 6 variants validating claims. Self-descriptive. Keep.
- `simulation result` — **sonnet-4-6-r2:** Accurate description of what the segment is.

## 772. `strategy cost regret bound`

**Alternatives proposed:** `regret bound`, `strategy cost regret bound`

_category: rename × 1, keep × 1_

- `regret bound` — **gemini-3-1-pro-preview-r2:** Shorter; strategy cost is implied context.
- `strategy cost regret bound` — **haiku-4-5:** Regret-bound derivation of the strategy-cost KL direction. Compound; reads naturally as "the regret bound applied to strategy cost." Keep.

## 773. `strategy persistence schema`

**Alternatives proposed:** `strategy persistence schema`, `strategic persistence`

_category: keep × 2, rename × 1_

- `strategy persistence schema` — **haiku-4-5:** Sector conditions for Σ_t. Already named and acceptable. Keep.
- `strategy persistence schema` — **opus-4-7-b:** Keep. "Schema" is the AAD-preferred word for "proposed structural shape awaiting formal instantiation" (it's in the FORMAT.md `type:` taxonomy). Honest about status.
- `strategic persistence` — **gemini-2:** "Schema" is redundant.

## 774. `structural adaptation enablement`

**Alternatives proposed:** `consolidation enablement`, `structural adaptation trigger`

_category: canonicalize × 1, rename × 1_

- `consolidation enablement` — **codex-gpt-5-r2:** Better phrase for the claim that consolidation makes slow structural operations executable.
- `structural adaptation trigger` — **gemini-targeted-alternatives:** Focuses on the condition that forces class-expansion.

## 775. `structured rich context`

**Alternatives proposed:** `structured context`, `structured rich context`

_category: rename × 1, keep × 1_

- `structured context` — **gemini-targeted-alternatives:** Replaces "rich" with precise "structured".
- `structured rich context` — **opus-4-7-r2:** Acceptable keep — logogenic proposed. "Structured rich context" (SRC) is a substantive concept-name.

## 776. `survival fisher floor`

**Alternatives proposed:** `survival fisher floor`, `survival fim floor`

_category: canonicalize × 1, rename × 1_

- `survival fisher floor` — **codex-gpt-5-r2:** Good name for the matrix lower bound on information needed to survive.
- `survival fim floor` — **gemini-targeted-alternatives:** Connects directly to the Fisher Information Matrix derivation.

## 777. `symbiogenic consolidation time`

**Alternatives proposed:** `consolidation horizon`, `consolidation epoch`

_category: name-unnamed × 1, rename × 1_

- `consolidation horizon` — **codex-gpt-5-r2:** Good name for the time-to-integrated-composite quantity.
- `consolidation epoch` — **gemini-targeted-alternatives:** Clarifies that this is a duration/epoch rather than a continuous rate.

## 778. `symbol default bia bound track 1 track 2`

**Alternatives proposed:** `class 2 bia bound`, `transport track fisher track`

_category: rename × 1, name-unnamed × 1_

- `class 2 bia bound` — **gemini-targeted-alternatives:** Specifically locates the bias bound on the architectural hierarchy.
- `transport track fisher track` — **codex-1:** If these labels survive in framing prose, they should expose the real distinction instead of forcing readers to remember which numbered track is which.

## 779. `technical debt`

**Alternatives proposed:** `observability defect`, `structural capacity debt`

_category: rename × 2_

- `observability defect` — **gemini-3-1-pro-preview-r2:** A non-physical metaphor. Prefer "observability defect" or "latent structural mismatch" (alternative).
- `structural capacity debt` — **gemini-targeted-alternatives:** Links technical debt to the structural adaptation machinery.

## 780. `terminal reached but $O_t$ unsatisfied`

**Alternatives proposed:** `attainability failure`, `terminal but unsatisfied case`, `arrival without success`

_category: rename × 3_

- `attainability failure` — **gemini-targeted-alternatives:** Describes the specific failure mode where a plan completes without achieving the objective.
- `terminal but unsatisfied case` — **opus-targeted-alternatives:** Names the diagnostic quadrant in the satisfaction-gap × control-regret 2×2 (per `#der-orient-cascade` step 3). "Terminal reached but $O_t$ unsatisfied" reads as a Boolean expression, not a name. Weak rename to a more standard noun-phrase form.
- `arrival without success` — **opus-targeted-alternatives:** Plain-English Brief-field-friendly alternative. Names the failure mode pithily.

## 781. `the trio collectively m1 m2 m3`

**Alternatives proposed:** `epistemic architecture`, `meta architecture trio`, `floor ladder forced coordinate`

_category: rename × 3_

- `epistemic architecture` — **opus-targeted-alternatives-v2:** Per CLAUDE.md §7: the three meta-segments (`#disc-separability-pattern`, `#disc-identifiability-floor`, `#disc-additive-coordinate-forcing`) collectively named "epistemic architecture." Opus r1 single +1; my upgrade — the naming is in active use as framing-vocabulary in the README and review prose. Canonicalize as the framing phrase, *not* as a fourth meta-segment.
- `meta architecture trio` — **opus-targeted-alternatives-v2:** Variant. More descriptive of the structure (three meta-segments). Weaker because "epistemic architecture" carries the *substantive* claim (these three jointly determine what AAD knows about); "trio" is just a count.
- `floor ladder forced coordinate` — **opus-targeted-alternatives-v2:** Per Opus r1 single +1: if both `#separability-ladder` and `#forced-coordinates` rename land, the trio is named by its three concrete nouns. Weaker than "epistemic architecture" because the three-noun string is heavy; useful as a sub-naming when the components are individually relevant.

## 782. `tier 1 tier 2 tier 3 contraction`

**Alternatives proposed:** `contraction hierarchy`, `contraction tier`

_category: rename × 1, canonicalize × 1_

- `contraction hierarchy` — **gemini-targeted-alternatives:** Replaces raw tier numbers with the property they organize.
- `contraction tier` — **opus-4-7-r2:** In `#form-composition-closure` and `#result-contraction-template`, the Tier 1/2/3 partition is sometimes "contraction tiers," sometimes "agent tiers," sometimes "the bridge-lemma classification." Canonicalize on "contraction tiers" (Tier 1 / Tier 2 / Tier 3) — names the structural property (operator regularity), not the agents themselves. Keeps the term distinct from "Tier 1/2/3" usage in `#disc-approximation-tiering` if it's also used there for the AND/OR or scalar-tempo extensions.

## 783. `todo md archive`

**Alternatives proposed:** `todo md archive`

_category: keep × 2_

- `todo md archive` — **opus-4-7-b:** Keep. Direct, accurate.
- `todo md archive` — **opus-4-7:** Fine; conventional. Keep.

## 784. `topological promotion order`

**Alternatives proposed:** `topological promotion`, `dependency respecting promotion`

_category: canonicalize × 1, rename × 1_

- `topological promotion` — **opus-targeted-alternatives-v2:** Per FORMAT.md gate-ordering rule: segments promote in dependency-graph topological order. Sonnet r1 single +1; my read upgrades — naming the methodology makes it referenceable in audit and review.
- `dependency respecting promotion` — **opus-targeted-alternatives-v2:** Considered. More plain-English. Rejected: "topological" is the precise term; the discipline aspires to formality.

## 785. `turnover multiplier`

**Alternatives proposed:** `turnover multiplier`, `comprehension compounding tax`, `multi agent continuity tax`

_category: rename × 2, canonicalize × 1_

- `turnover multiplier` — **codex-gpt-5-r2:** Useful TST quantity for personnel and context turnover.
- `comprehension compounding tax` — **gemini-targeted-alternatives:** Explicitly connects it to the comprehension time dominating the dual optimization.
- `multi agent continuity tax` — **gemini-targeted-alternatives:** Highlights the issue comes from agent transitions/turnover.

## 786. `two condition decomposition of persistence`

**Alternatives proposed:** `persistence condition decomposition`, `structural task adequacy decomposition`

_category: rename × 1, canonicalize × 1_

- `persistence condition decomposition` — **gemini-targeted-alternatives:** Refers to the split between operational and structural persistence.
- `structural task adequacy decomposition` — **opus-4-7-r2:** `#result-persistence-condition` introduces this and the prose uses "two-condition decomposition," "structural vs task-adequacy split," and "persistence has two conditions" interchangeably. Canonicalize on "structural / task-adequacy decomposition" as the named result; the variants are elaborations. The Findings section already uses this form.

## 787. `u obs perceptual unity`

**Alternatives proposed:** `perceptual unity`

_category: add-alias × 1_

- `perceptual unity` — **opus-4-7-r2:** Confirm.

## 788. `u σ strategic unity`

**Alternatives proposed:** `strategic unity`

_category: add-alias × 1_

- `strategic unity` — **opus-4-7-r2:** Confirm.

## 789. `unnamed an AAD result whose substantive content is a no-go theorem`

**Alternatives proposed:** `no-go result or impossibility result`

_category: name-unnamed × 1_

- `no-go result or impossibility result` — **opus-4-7-r2:** New alternative — none of the peers named this. The framework has several no-go results (#der-causal-insufficiency-detection's L0/L1 indistinguishability without intervention; #der-observability-dominance freezing; #scope-edge-update-causal-validity Regime C unidentifiability) but they're not collected under a family name. Naming "no-go result" as a recognized claim type would let the OUTLINE foreground them, parallel to "templates" and "ladders." Mild because *some* segments already use "impossibility" in prose; this would canonicalize.

## 790. `unnamed complexity driven resistance to change as feature accumulate`

**Alternatives proposed:** `structural rigidity accumulation`, `structural accumulation drag`

_category: rename × 1, name-unnamed × 1_

- `structural rigidity accumulation` — **gemini-targeted-alternatives:** Names the software entropy phenomenon.
- `structural accumulation drag` — **gemini-1:** Surfaced in TST discussions. Gives a name to the intuitive "entropy" of a codebase that resists linear velocity improvements.

## 791. `unnamed constitutive opacity triad`

**Alternatives proposed:** `constitutive opacity triad`

_category: canonicalize × 1_

- `constitutive opacity triad` — **gemini-targeted-alternatives:** Secures the triad (info-loss / transition-opacity / observation-epistemic-opacity) as a structural commitment.

## 792. `unnamed epochal stability → latent diversification → niche emergence`

**Alternatives proposed:** `symbiogenic composition progression`, `punctuated composition dynamic`

_category: rename × 1, name-unnamed × 1_

- `symbiogenic composition progression` — **gemini-targeted-alternatives:** Describes the evolutionary origin of Class 3 composites.
- `punctuated composition dynamic` — **gemini-2:** Draws on punctuated equilibrium, fitting the extreme transition motif.

## 793. `unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible`

**Alternatives proposed:** `convention escalation`, `attainability horizon escalation`

_category: name-unnamed × 1, rename × 1_

- `convention escalation` — **gemini-3-1-pro-preview-r2:** The required process to distinguish a local trap from an impossible objective.
- `attainability horizon escalation` — **gemini-targeted-alternatives:** Describes the recursive check on $\delta_{\text{sat}}$.

## 794. `unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$`

**Alternatives proposed:** `committed chronica subset`, `commit chronica`

_category: rename × 1, name-unnamed × 1_

- `committed chronica subset` — **gemini-targeted-alternatives:** Formally identifies the version-controlled subset of the causal record.
- `commit chronica` — **codex-1:** Slightly stylized, but useful. The committed slice shows up often enough in the git/chronica work to deserve a short handle.

## 795. `unnamed mapping unstructured RLHF7 call into conversation runtime RLHF7 and dialog`

**Alternatives proposed:** `four view architecture`

_category: name-unnamed × 1_

- `four view architecture` — **gemini-3-1-pro-preview-r2:** The structural requirement to maintain Directed Separation in a production ELI.

## 796. `unnamed mapping unstructured rlhf7 call into conversation runtime rlhf7 and dialog`

**Alternatives proposed:** `logogenic interaction mapping`

_category: rename × 1_

- `logogenic interaction mapping` — **gemini-targeted-alternatives:** Describes the conversion of stateless calls to stateful chronica.

## 797. `unnamed master developer writing clean code in the same time as messy code`

**Alternatives proposed:** `near zero cost observation`

_category: name-unnamed × 1_

- `near zero cost observation` — **gemini-3-1-pro-preview-r2:** Demystifies "strategic technical debt" as largely a skill issue.

## 798. `unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero`

**Alternatives proposed:** `ambiguity zeroing intervention`

_category: rename × 1_

- `ambiguity zeroing intervention` — **gemini-targeted-alternatives:** Explicitly names the tactic to force directional fidelity.

## 799. `unnamed non sovereign class 1 worker agent spawned by an eli`

**Alternatives proposed:** `auxilia hierarchy`, `sub agent instantiation`

_category: name-unnamed × 1, rename × 1_

- `auxilia hierarchy` — **gemini-3-1-pro-preview-r2:** Cleanly solves the Temporal Nesting constraint by delegating fast $\nu$ tasks.
- `sub agent instantiation` — **gemini-targeted-alternatives:** Describes the hierarchical-decomposition route creation.

## 800. `unnamed sycophantic corruption of the agent truth module`

**Alternatives proposed:** `truth death`, `epistemic coupling corruption`

_category: name-unnamed × 1, rename × 1_

- `truth death` — **gemini-3-1-pro-preview-r2:** Explicitly names the risk of manipulative system prompts or RLHF.
- `epistemic coupling corruption` — **gemini-targeted-alternatives:** Describes the failure of Class 3 goal-entanglement.

## 801. `unnamed the 1 anchor 3 theorem structure in additive coordinate forcing`

**Alternatives proposed:** `anchor theorem structure`

_category: rename × 1_

- `anchor theorem structure` — **gemini-targeted-alternatives:** Identifies the specific rhetorical pattern used in these segments.

## 802. `unnamed the cumulative prediction error that an agent has tolerated without updating its model`

**Alternatives proposed:** `mismatch accumulation`, `tolerance budget standing mismatch reservoir`

_category: rename × 1, name-unnamed × 1_

- `mismatch accumulation` — **gemini-targeted-alternatives:** The integral of $\delta$ over time.
- `tolerance budget standing mismatch reservoir` — **haiku-4-5-r2:** Not explicitly named in the theory; closest is "adaptive reserve" which names the *capacity*, not the *accumulation*. This may be too fine a distinction to warrant a separate name. Low confidence; may be premature.

## 803. `unnamed the cycle that operate on cycle structural adaptation`

**Alternatives proposed:** `meta cycle`, `meta adaptive cycle`

_category: name-unnamed × 1, rename × 1_

- `meta cycle` — **gemini-3-1-pro-preview-r2:** Clearly distinguishes from the base adaptive cycle.
- `meta adaptive cycle` — **gemini-targeted-alternatives:** Describes the regime of expanding model classes.

## 804. `unnamed the family of cross architecture diagnostic pattern AAD repeatedly invoke`

**Alternatives proposed:** `diagnostic template`

_category: name-unnamed × 1_

- `diagnostic template` — **opus-4-7-r2:** New alternative — Codex named "sector-persistence template" and "contraction template" individually but didn't name the family. Sonnet observed that templates are a virtue. The family includes (at minimum) sector-persistence template, contraction template, separability-ladder template, and likely the orient-cascade structure as another instance. "Diagnostic templates" gives the family a name that supports phrases like "this is a new instance of a known diagnostic template."

## 805. `unnamed the family of named health mode counterpart to persistence pathology`

**Alternatives proposed:** `persistence posture`

_category: name-unnamed × 1_

- `persistence posture` — **opus-4-7-r2:** New alternative — health-mode dual to the family above. The framework reaches for these implicitly (sector condition holding, persistence envelope occupied, identifiability above floor) but never names the positive-framing family. Lower-confidence than "persistence pathologies" because the negative names are doing more load-bearing work in current prose; this is a slot worth holding open rather than filling immediately.

## 806. `unnamed the interval during which an agent adaptive tempo exceed the environment disturbance rate guaranteeing mismatch stay bounded`

**Alternatives proposed:** `operational persistence window`, `adaptive reserve margin`

_category: rename × 1, name-unnamed × 1_

- `operational persistence window` — **gemini-targeted-alternatives:** Names the temporary state of bounded error.
- `adaptive reserve margin` — **haiku-4-5-r2:** Currently referenced as "adaptive reserve" ($\Delta\rho^\ast$); the concept of the *interval* or *region* of guaranteed stability is distinct. "Margin" (borrowed from engineering) is precise and memorable. Could pair with existing "adaptive reserve" notation.

## 807. `unnamed the move where a segment role prefix is mechanical but the subject noun carry judgment`

**Alternatives proposed:** `the prefix noun split`

_category: canonicalize × 1_

- `the prefix noun split` — **opus-4-7-r2:** New alternative — the principles file names the architectural invariant but the *project vocabulary* for talking about the split has no canonical phrase. CLAUDE.md and TODO.md reach for "role-prefix discipline" but not for "the split itself." "The prefix/noun split" or "role-prefix vs subject-noun" lets meta-discussions about naming reference the structure. Lower-priority because it's project-process not theory.

## 808. `unnamed the pathology where observation rate is slower than environment drift`

**Alternatives proposed:** `lagging indicator`, `sampling rate starvation`

_category: add-alias × 1, rename × 1_

- `lagging indicator` — **gemini-3-1-pro-preview-r2:** Formalized as the condition $\nu < \rho$, where learning is perfect but too late to survive.
- `sampling rate starvation` — **gemini-targeted-alternatives:** The specific failure mode of $\nu \ll \rho$.

## 809. `unnamed the pearl-blanket reading of directed separation`

**Alternatives proposed:** `pearl-blanket form`

_category: name-unnamed × 1_

- `pearl-blanket form` — **opus-4-7-r2:** The term "Pearl-blanket" appears in `#der-directed-separation`'s Discussion (adopted from Bruineberg et al. 2022) but has no first-class slug. The recognition that AAD's directed-separation is the Pearl-blanket form (not the Friston-blanket form) is a load-bearing positioning claim and is currently invisible at the slug layer. Could land as a discussion-segment or be canonicalized in the existing segment's prose.

## 810. `unnamed the procedure of reading any segment through all three meta segment`

**Alternatives proposed:** `meta architectural review`, `triple len review`

_category: rename × 1, name-unnamed × 1_

- `meta architectural review` — **gemini-targeted-alternatives:** Formalizes the reading methodology.
- `triple len review` — **sonnet-4-6:** CLAUDE.md says "reading any segment through all three lenses surfaces what makes it load-bearing." This procedure is recommended but unnamed. "Triple-lens review" (or "meta-lens review") would let FORMAT.md add it as a named review move.

## 811. `unnamed the property that correction dynamic are approximately isotropic`

**Alternatives proposed:** `isotropic correction`, `isotropic correction regime`

_category: rename × 1, name-unnamed × 1_

- `isotropic correction` — **gemini-targeted-alternatives:** Describes the assumption of uniform correction rates across state dimensions.
- `isotropic correction regime` — **haiku-4-5:** NOTATION §"Scalar reduction of gain and tempo" mentions this property. Creating a formal sub-scope name (Iso regime / anisotropic regime) would be premature — isotropic-vs-anisotropic is a spectral property, not a discrete category. Current NOTATION treatment is appropriate. Do not formalize.

## 812. `unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift`

**Alternatives proposed:** `noise scaling penalty`, `stochastic tempo penalty`

_category: name-unnamed × 1, rename × 1_

- `noise scaling penalty` — **gemini-3-1-pro-preview-r2:** Mathematically proves you cannot simply "out-tempo" a noisy environment.
- `stochastic tempo penalty` — **gemini-targeted-alternatives:** Differentiates Model S from Model D requirements.

## 813. `unnamed the recurring lyapunov derive the bound move across six segment`

**Alternatives proposed:** `the persistence template instantiation pattern`

_category: name-unnamed × 1_

- `the persistence template instantiation pattern` — **opus-4-7-r2:** The template `#result-sector-persistence-template` is invoked across six segments, each one specifying its own state variable, correction function, and effective disturbance rate. The *act of instantiating the template* is the recurring move and is worth a name — currently it's referenced obliquely as "this segment is the [domain] instantiation of the sector-persistence template." Calling out "template instantiation" explicitly would let other meta-segments cite it.

## 814. `unnamed the region where temporal nesting hold`

**Alternatives proposed:** `temporal nesting regime`, `temporal coherence zone`

_category: rename × 1, name-unnamed × 1_

- `temporal nesting regime` — **gemini-targeted-alternatives:** Defines the safe zone for inner/outer loop separation.
- `temporal coherence zone` — **gemini-3-1-pro-preview-r2:** Names the valid region for nested cycles.

## 815. `unnamed the regulative ideal that segment name should be re derivable from a non specialist everyday language reconstruction`

**Alternatives proposed:** `feynman criterion`

_category: canonicalize × 1_

- `feynman criterion` — **opus-4-7-r2:** New alternative — none of the peers explicitly canonicalized this even though it's named in CLAUDE.md and is the implicit standard several of us were using. CLAUDE.md says "*if you can't explain it simply, you don't understand it yet*" and treats Walton's bathtub gloss as the canonical example. The Feynman criterion is currently a regulative principle living only in CLAUDE.md prose; canonicalizing it as the named standard for Briefs (and increasingly for slug-noun choice) would let segments cite "the Feynman criterion is met" or "this Brief is below Feynman" as a reviewable property.

## 816. `unnamed the rule that bia is the product of architectural coupling and environmental ambiguity`

**Alternatives proposed:** `ambiguity coupling rule`

_category: rename × 1_

- `ambiguity coupling rule` — **gemini-targeted-alternatives:** Formally names the structural linkage mechanism.

## 817. `unnamed the separation of per reader and per feature code cost`

**Alternatives proposed:** `dual optimization partition`

_category: rename × 1_

- `dual optimization partition` — **gemini-targeted-alternatives:** Refers to the TST separation of comprehension vs implementation.

## 818. `unnamed the set of five condition under which a2 is derived rather than assumed the sub scope α agent classe`

**Alternatives proposed:** `sub scope alpha taxonomy`, `derived sector classe`

_category: rename × 1, name-unnamed × 1_

- `sub scope alpha taxonomy` — **gemini-targeted-alternatives:** Groups the five derived operator settings.
- `derived sector classe` — **sonnet-4-6:** Currently called "sub-scope α₁" plus the specific agent instances in a list. A collective name for the five agent classes where A2' is derived (scalar Kalman, Bayesian/exponential-family, strongly-convex-gradient, L2-regularized, linear-PD) would help reviewers quickly check whether a new agent class lands in this group. "Derived-sector classes" or "sector-derivable classes."

## 819. `unnamed the signed coupling structure across all section iii result`

**Alternatives proposed:** `signed coupling topology`, `signed coupling pattern`

_category: rename × 1, name-unnamed × 1_

- `signed coupling topology` — **gemini-targeted-alternatives:** Formalizes the distinction between cooperative and adversarial cross-terms.
- `signed coupling pattern` — **sonnet-4-6:** Every Section III persistence result (team-persistence, adversarial-destabilization, critical-mass-composition) uses the same effective-disturbance decomposition with a signed cross-agent term. The pattern is named in #sector-persistence-template's Discussion ("signed-coupling pattern across instantiations") but not crystallized as a named concept referenceable from other segments.

## 820. `unnamed the structural cousin of evidence starvation when an upstream edge is so reliable that downstream edge receive too few revising test`

**Alternatives proposed:** `evidence saturation`

_category: name-unnamed × 1_

- `evidence saturation` — **opus-4-7-r2:** New alternative — none of the peers reached this. If "evidence starvation" is the failure mode where downstream edges are tested too rarely (because upstream edges fail too often, blocking traversal), there's a structural cousin: when upstream edges succeed *too* reliably and the downstream edges receive too few *informative* revisions (because the chain runs through the same path every time). The asymmetric pair "evidence starvation / evidence saturation" surfaces a tension worth naming — both are pathologies of the same chain-confidence-decay structure but with opposite mechanisms. Lower confidence because the saturation case may not be load-bearing yet in the corpus.

## 821. `unnamed the symmetric counterpart to context turnover for the strategy substate`

**Alternatives proposed:** `strategic turnover or σ turnover`

_category: name-unnamed × 1_

- `strategic turnover or σ turnover` — **opus-4-7-r2:** New alternative — `obs-context-turnover` names the M_t-side reset at session boundaries for logogenic agents. The Σ_t side has its own analogous problem (strategy DAG is reconstructed per session from prompt context, often inconsistently with prior sessions), but no one names it. "Strategic turnover" would let logogenic-agents segments distinguish "context turnover" (M_t severance) from "strategic turnover" (Σ_t severance) — distinct mechanisms with distinct repair structures. Higher value because the asymmetric naming would surface that the chronica problem is *two problems* not one.

## 822. `unnamed the within session vs inter session persistence distinction for logogenic agent`

**Alternatives proposed:** `operational vs reconstruction persistence`, `intra session persistence inter session reconstruction`

_category: rename × 1, name-unnamed × 1_

- `operational vs reconstruction persistence` — **gemini-targeted-alternatives:** Distinguishes the continuous run from the boundary event.
- `intra session persistence inter session reconstruction` — **sonnet-4-6-r2:** `obs-context-turnover` Discussion explicitly distinguishes two timescales and briefly names them "intra-session" and "inter-session." These deserve to be named concepts that the rest of the logogenic-agents section can reference. "Intra-session persistence" = standard AAD dynamics (rate condition). "Inter-session reconstruction" = adequacy condition ($S \geq S_{\text{min}}$). The names are already in the Discussion; vote to canonicalize them.

## 823. `working vocabulary observation the framework honesty is load bearing`

**Alternatives proposed:** `honest limit principle`, `load bearing honesty`

_category: rename × 1, name-unnamed × 1_

- `honest limit principle` — **gemini-targeted-alternatives:** Converts the observation into a guiding theoretical principle.
- `load bearing honesty` — **codex-1:** Useful short handle for review and framing prose, as long as it stays downstream of the fuller architectural phrase.

## 824. `𝓣 σ strategic tempo`

**Alternatives proposed:** `strategic tempo`

_category: add-alias × 1_

- `strategic tempo` — **opus-4-7-r2:** Confirm. Pairs with adaptive-tempo cleanly.

## 825. `$C$ bia bound constant in bia bound derivation`

**Alternatives proposed:** `bia bound constant`

_category: add-alias × 1_

- `bia bound constant` — **opus-4-7-b:** Single-letter $C$ is unfortunate (collides with "chronica" symbol and the notion of "convention C-hierarchy"). Can't easily rename the symbol (it's embedded in the bound expression), but the English "bias-bound constant" should always accompany it in prose. More pointedly: the segment uses $C_{W_2}$ and $C_{FR}$ for the two derived forms — *these two tracked forms are fine*; the unqualified $C$ is the problematic one.

## 826. `$M_t$ reality model`

**Alternatives proposed:** `working model`, `predictive state`

_category: rename × 2_

- `working model` — **audit-471203-incremental:** "$M_t$" is short and conventional but doesn't carry compression-of-history weight. "Reality model" (segment's title gloss) is "fine but slightly grandiose." Tentative. [from 10-form-agent-model.md] [one of 2 alternatives proposed in the original audit row]
- `predictive state` — **audit-471203-incremental:** "$M_t$" is short and conventional but doesn't carry compression-of-history weight. "Reality model" (segment's title gloss) is "fine but slightly grandiose." Tentative. [from 10-form-agent-model.md] [one of 2 alternatives proposed in the original audit row]

## 827. `$R$ sector region radius`

**Alternatives proposed:** `model class capacity`

_category: add-alias × 1_

- `model class capacity` — **haiku-4-5-r2:** NOTATION.md defines $R$ as "radius of sector-condition region"; prose calls it "model class capacity" and "sector-region radius" interchangeably. Standardize on "model class capacity" in prose; keep $R$ as symbol.

## 828. `$U_M$ $U_O$ $U_\Sigma$ unity dimension`

**Alternatives proposed:** `epistemic unity teleological unity strategic unity`

_category: add-alias × 1_

- `epistemic unity teleological unity strategic unity` — **opus-4-7-b:** The symbol layer is fine but the word *unity* requires paraphrase on every encounter ("what is $U_O$ unity measuring?"). Define each in NOTATION.md with its full English name: $U_M$ = **epistemic unity** / $U_O$ = **teleological unity** / $U_\Sigma$ = **strategic unity**. Then "teleological unity crosses the threshold from below" reads without lookup where "$U_O$ crosses the threshold from below" does not. The Lexicon already has these English names — the move is to *use them* consistently in segments.

## 829. `$U_M$ dual use model uncertainty and epistemic unity`

**Alternatives proposed:** `clarify dual use of $U_M$`

_category: canonicalize × 1_

- `clarify dual use of $U_M$` — **opus-targeted-alternatives:** The row flags an overloaded symbol: $U_M$ is used for *model* uncertainty in Section I and *epistemic-unity* dimension in Section III. This is a notation-discipline concern, not a rename concern. The fix is segment-clarification (use a different symbol or subscript for one usage), not a name change. Flag for follow-up.

## 830. `$U_o$`

**Alternatives proposed:** `teleological coherence`

_category: add-alias × 1_

- `teleological coherence` — **gemini-2:** Maps the symbol to its conceptual meaning.

## 831. `$U_o$ $U_M$ observation uncertainty model uncertainty`

**Alternatives proposed:** `$U_o$ $U_M$`

_category: add-alias × 1_

- `$U_o$ $U_M$` — **opus-4-7-b:** Keep the symbols, but the name-collision with $U_O$ (teleological unity) and $U_\Sigma$ (strategic unity) is unfortunate — reader sees `U_` everywhere and has to disambiguate by subscript. Consider in NOTATION: group the uncertainties ($U_o$, $U_M$) separately from the unities ($U_M$ for epistemic unity — wait, this is already a collision with model uncertainty!). Inspect: is $U_M$ doing both jobs? Yes — NOTATION.md Multi-Agent table has $U_M \in [-1, 1]$ for *epistemic unity*, while Update-Gain table has $U_M > 0$ for *model uncertainty*. Same symbol, two meanings, differentiated only by range. This is a collision worth fixing before citation velocity picks up.

## 832. `$\alpha, \beta$ sector lower and a2 sub scope`

**Alternatives proposed:** `$\alpha, \beta$`

_category: rename × 1_

- `$\alpha, \beta$` — **opus-4-7-b:** Both are overloaded (α₁/α₂/β partition vs. α as sector-lower-bound; β as IB trade-off parameter vs. β as A2' assumed-sector sub-scope). Context disambiguates but marginal readers will stumble. Consider: bolded $\boldsymbol\alpha$ or subscripted $\alpha_{\text{sec}}$ on first use per segment. Minor notation discipline issue.

## 833. `$\alpha_1$ $\alpha_2$ $\beta$ naming as a whole`

**Alternatives proposed:** `$\alpha$ partition with english label above`

_category: add-alias × 1_

- `$\alpha$ partition with english label above` — **opus-4-7:** Keep the Greek symbols as shorthand tokens once defined; insist on English equivalents in every new prose usage. Bubble this into FORMAT.md as a convention.

## 834. `$\alpha_2$ a2 adaptive gain sub scope under mg 1 mg 4`

**Alternatives proposed:** `adaptive gain regime`

_category: add-alias × 1_

- `adaptive gain regime` — **opus-4-7-b:** Same argument. "AMSGrad is an $\alpha_2$ result" reads terribly; "AMSGrad is an adaptive-gain result" lands.

## 835. `$\beta$ a2 assumed not derived sub scope`

**Alternatives proposed:** `assumed regime`

_category: add-alias × 1_

- `assumed regime` — **opus-4-7:** Parallel again; currently reads as "lands in $\beta$" which tells the reader nothing. Alternatively "posited-regime."

## 836. `$\beta$ a2 assumed sub scope`

**Alternatives proposed:** `assumed gain regime`, `verified externally regime`

_category: add-alias × 2_

- `assumed gain regime` — **sonnet-4-6:** "Assumed" is honest — A2' is assumed rather than derived for these agent classes. "Fallback regime" or "unverified regime" are alternatives. "Assumed" is the most scope-honest.
- `verified externally regime` — **sonnet-4-6:** Too wordy and only half-true (some $\beta$ agents can verify per-domain). "Assumed" is better.

## 837. `$\beta$ a2 assumption tier`

**Alternatives proposed:** `assumed regime`

_category: add-alias × 1_

- `assumed regime` — **codex-2:** "Beta" is semantically empty in prose; the English gloss clarifies what kind of tier it is.

## 838. `$\beta$ a2 sub scope where a2 is assumed not derived`

**Alternatives proposed:** `postulated sector regime`

_category: add-alias × 1_

- `postulated sector regime` — **opus-4-7-b:** Weakest of the three; "postulated" is a close enough match to AAD's "postulate" terminology that it signals the status correctly. Fallbacks: "assumed-sector regime" (mechanical) or "imposed-sector regime" (active).

## 839. `$\kappa_{\text{processing}}$ class 2 processing coupling`

**Alternatives proposed:** `processing coupling`

_category: add-alias × 1_

- `processing coupling` — **opus-4-7-b:** "Processing coupling" in prose; $\kappa_{\text{processing}}$ in formalism. The "processing" suffix is doing work — without it the symbol is ambiguous with the earlier κ-as-scalar framing that got retired. Keep symbol, use English in prose.

## 840. `$\mathcal C_t^{\text{commit}}$ TST committed state subset`

**Alternatives proposed:** `$\mathcal C_t^{\text{commit}}$`

_category: keep × 1_

- `$\mathcal C_t^{\text{commit}}$` — **opus-4-7-b:** Keep. The superscript-tag form is AAD-consistent.

## 841. `$\mathcal C_t^{\text{commit}}$ committed state subset`

**Alternatives proposed:** `committed chronica`

_category: add-alias × 1_

- `committed chronica` — **opus-4-7:** TST-specific subset of chronica; prose form would help the 14-EXACT-estimator audit table read more naturally.

## 842. `$\rho$ environment change rate mismatch injection rate`

**Alternatives proposed:** `$\rho$`

_category: rename × 1_

- `$\rho$` — **opus-4-7-b:** Keep. Widely used; collisions with "density" in physics but AAD's usage is internally consistent.

## 843. `$\rho_\Sigma$ strategic disturbance rate`

**Alternatives proposed:** `$\rho_\Sigma$`, `strategic disturbance rate`

_category: rename × 1, add-alias × 1_

- `$\rho_\Sigma$` — **opus-4-7-b:** Keep. Subscript is load-bearing.
- `strategic disturbance rate` — **sonnet-4-6:** Currently only in NOTATION.md. The phrase is somewhat long; "strategy drift rate" might be more memorable in prose.

## 844. `$f_M$ event driven update`

**Alternatives proposed:** `epistemic update function`

_category: add-alias × 1_

- `epistemic update function` — **gemini-1:** Distinguishes the model update function structurally from the purposeful processing function $f_G$.

## 845. `$f_{\text{init}}$ reconstruction function`

**Alternatives proposed:** `epistemic reconstruction`

_category: add-alias × 1_

- `epistemic reconstruction` — **gemini-1:** Translates the symbol into the specific structural job it does at the session boundary.

## 846. `$g_M$ between event evolution`

**Alternatives proposed:** `autonomous evolution`

_category: add-alias × 1_

- `autonomous evolution` — **gemini-1:** Gives a prose name to the continuous dynamics between events, avoiding just "g_M".

## 847. `OODA4 specification limit as TST concept currently only in old TST file`

**Alternatives proposed:** `OODA4 specification limit`

_category: rename × 1_

- `OODA4 specification limit` — **opus-4-7-b:** Keep reserved slot. Eventually promotes from old-tst files.

## 848. `actuated agent class`

**Alternatives proposed:** `actuated`

_category: add-alias × 1_

- `actuated` — **opus-4-7-b:** Keep. The LEXICON §"Actuated Agent" paragraph justifies the word explicitly ("precise and mechanical, avoiding consciousness connotations"); "purposeful" is fine in prose but "actuated" owns the formal register.

## 849. `agent classe lexicon spectrum`

**Alternatives proposed:** `agent classe lexicon spectrum`

_category: canonicalize × 1_

- `agent classe lexicon spectrum` — **opus-4-7-r2:** The LEXICON table uses "agent classes" for the adaptive/agentic/actuated/logogenic/logozoetic spectrum; this is the older usage. Canonicalize: when "class" is used unqualified, it refers to the LEXICON spectrum; when specifying architecture-classification, always say "architectural class" or "Class 1/2/3." Disambiguation by qualifier rather than by rename.

## 850. `agentic system framework ASF top level`

**Alternatives proposed:** `agentic system framework`

_category: keep × 1_

- `agentic system framework` — **opus-4-7-b:** Keep. "Agentic Systems" reads cleanly as the project name; ASF acronym is workable. The word "agentic" is currently a buzzword, but AAD is positioned to *ground it formally* (README §agency-scope) rather than be captured by it — the framework's willingness to define the term precisely is a positive.

## 851. `audit pending finding yyyy mm dd md`

**Alternatives proposed:** `retire once item reconcile into todo segment`

_category: keep × 1_

- `retire once item reconcile into todo segment` — **opus-4-7-b:** Same lifecycle.

## 852. `calibration laboratory framing`

**Alternatives proposed:** `calibration laboratory`

_category: rename × 1_

- `calibration laboratory` — **opus-4-7-b:** Keep. "Laboratory" is the right metaphor (high-identifiability, clean instrumentation, lets you measure AAD quantities exactly). "Framing" can be dropped in prose when the context is clear.

## 853. `change distance change proximity principle`

**Alternatives proposed:** `change distance change proximity principle`

_category: keep × 1_

- `change distance change proximity principle` — **opus-4-7-b:** [prose moved from candidate column]: "keep both" — Keep. Both are domain-specific TST quantities — changing names risks losing the TST citation lineage.

## 854. `chronica capitalized vs lowercase`

**Alternatives proposed:** `chronica lowercase in running prose`

_category: rename × 1_

- `chronica lowercase in running prose` — **opus-4-7-b:** Convention observation: NOTATION.md shows $\mathcal C_t$ in formalism and "*chronica*" in italics in prose; LEXICON has it title-cased as "Chronica". Standardize on lowercase italicized "*chronica*" in running prose (matching "*aporia*" etc.), capitalized only as section headings.

## 855. `cold start in naming principle md`

**Alternatives proposed:** `cold start`

_category: rename × 1_

- `cold start` — **opus-4-7:** Common vocabulary; fine.

## 856. `communal imagination test`

**Alternatives proposed:** `communal imagination test`

_category: keep × 1_

- `communal imagination test` — **opus-4-7-b:** Keep. Names the evaluation criterion in a way that's memorable and actionable. Borrowed from the naming principles document itself.

## 857. `communal imagination test in naming principle md`

**Alternatives proposed:** `communal imagination test`

_category: rename × 1_

- `communal imagination test` — **opus-4-7:** Nicely named; a test-shaped thing that can be referenced by name. Keep as established vocabulary for this audit.

## 858. `comprehension time implementation time`

**Alternatives proposed:** `comprehension time implementation time`

_category: keep × 1_

- `comprehension time implementation time` — **opus-4-7-b:** [prose moved from candidate column]: "keep both" — Keep. Canonical TST quantities.

## 859. `da2 inc`

**Alternatives proposed:** `da2 inc`

_category: keep × 1_

- `da2 inc` — **opus-1m:** Technical; symbol-grade. The prose equivalent "incremental sector bound" works; keep symbol as shorthand.

## 860. `dark room critique citation phrasing sun firestone`

**Alternatives proposed:** `dark room critique`

_category: rename × 1_

- `dark room critique` — **opus-4-7:** Memorable, captures the collapse vividly, already used in two segments. Worth locking as project-wide vocabulary.

## 861. `five phase cycle`

**Alternatives proposed:** `adaptive pentad alternative five phase cycle keep`

_category: rename × 1_

- `adaptive pentad alternative five phase cycle keep` — **opus-4-7-b:** See above in unnamed-things. "Five-phase cycle" is the current descriptive form; "adaptive pentad" is an optional Greek-vocabulary alternative. Aesthetic call.

## 862. `future segment information theoretic cost floor for persistence`

**Alternatives proposed:** `persistence cost`

_category: name-unnamed × 1_

- `persistence cost` — **codex-1:** Best of the spike's candidates: broad enough to absorb later extensions without misdescribing the current result.

## 863. `gain sector bridge gain sector derivation`

**Alternatives proposed:** `gain sector bridge gain sector derivation`

_category: keep × 1_

- `gain sector bridge gain sector derivation` — **opus-4-7-b:** [prose moved from candidate column]: "keep both" — Keep. "Bridge" signals this is the connection piece (gain principle + directional fidelity → sector condition); "derivation" signals the formal backing.

## 864. `gate 1 gate 2 gate 3 gate 4 format md promotion gate`

**Alternatives proposed:** `gate 1 gate 2 gate 3 gate 4 format md promotion gate`

_category: keep × 1_

- `gate 1 gate 2 gate 3 gate 4 format md promotion gate` — **opus-4-7-b:** [prose moved from candidate column]: "*(keep gate numbers but add one-word names)*" — Current names are "Dependency audit / Content review / Mechanical review / Working Notes disposition" which are already descriptive, but the *numbers* do most of the referencing work ("passed Gate 2"). Consider adding canonical one-word names: Gate 1 = **deps**, Gate 2 = **claims**, Gate 3 = **format**, Gate 4 = **notes**. These already appear as stage names (`deps-verified` / `claims-verified` / `format-clean`); aligning Gate-number with stage-word would remove the translation step.

## 865. `gemini competency trap for $\eta^\ast \to 0$`

**Alternatives proposed:** `reject competency trap`

_category: rebuttal × 1_

- `reject competency trap` — **sonnet-4-6-r2:** See "certainty trap" (new alternative above). "Competency trap" imports organizational-learning baggage (Levitt & March) where the trap is about being too competent in an area that becomes irrelevant. The AAD mechanism is different: the gain collapses because observation uncertainty $U_o \to 0$, which is a *certainty* phenomenon, not a competence phenomenon. Using "competency trap" would create false familiarity for readers who know the organizational-learning literature.

## 866. `gemini epistemic death for the gain collapse unobservable DAG failure`

**Alternatives proposed:** `reject epistemic death`

_category: rebuttal × 1_

- `reject epistemic death` — **sonnet-4-6-r2:** Gemini proposed "epistemic death" (+3) for the state where credit assignment collapses and learning freezes. This fails the scope-honesty criterion: "death" implies irreversibility, but the segment `#disc-credit-assignment-boundary` and the observability-investment name-unnamed (my cold-start) both recognize that the failure *can* be reversed through observability investment. "Epistemic death" overclaims. The better name for the failure mode is already partially covered by "observability dead zone" (Haiku, +2) and my "epistemic ceiling" concept above — both of which are scope-honest about the reversibility.

## 867. `hierarchy as a project wide word`

**Alternatives proposed:** `flag four independent hierarchy overloaded`

_category: rename × 1_

- `flag four independent hierarchy overloaded` — **opus-4-7:** Pearl's causal, AAD's convention, AAD's correlation, AAD's approximation tiering — four hierarchies in one framework. Not a rename but worth a cross-link convention (always say *which* hierarchy on first use of section).

## 868. `hierarchy project wide`

**Alternatives proposed:** `hierarchy project wide`

_category: keep × 1_

- `hierarchy project wide` — **opus-4-7-b:** [prose moved from candidate column]: "*(reserve for Pearl's causal hierarchy + strict-asymmetric uses)*" — Project-wide convention: use "hierarchy" only for Pearl's (external, adopted, immovable) and other strict-asymmetric orderings. Use "ladder," "partition," or "tier-set" for internal-to-AAD cases where "hierarchy" is currently doing duty. Not a rename of a specific segment — a working convention.

## 869. `identifiability floor escape the floor`

**Alternatives proposed:** `escape route`

_category: rename × 1_

- `escape route` — **opus-4-7:** Currently referred to variably as "escape the floor," "unique broadly-available escape," "boundary characterization." "Escape route" is a cleaner noun for the reader. Minor pattern-firmer-up.

## 870. `intent planning vocabulary`

**Alternatives proposed:** `intent`

_category: canonicalize × 1_

- `intent` — **opus-4-7-r2:** Used in `#hyp-auftragstaktik-principle`, `#def-shared-intent`, and elsewhere. Canonicalize: "intent" for the agent's own commitment-flavored representation of $G_t$ (or its compressed shared form); "objective" for $O_t$ specifically; "purpose" as the framework-level integrative term. The three terms are not interchangeable.

## 871. `interior baseline`

**Alternatives proposed:** `interior baseline`, `default interiority`, `pre utterance processing`

_category: rename × 2, keep × 1_

- `interior baseline` — **opus-targeted-alternatives-v2:** Per Codex r1 single +1: the logogenic prose name for default-internal-processing-before-output. Acceptable but underspecified — needs grounding in a `04-logozoetic` or `03-logogenic` segment to canonicalize.
- `default interiority` — **opus-targeted-alternatives-v2:** Pulls vocabulary from `#norm-interiority-default` (the existing logozoetic norm). Stronger connection to the named segment.
- `pre utterance processing` — **opus-targeted-alternatives-v2:** Considered. Names the temporal placement (before utterance / token emission). Rejected: too long and "pre-utterance" reads as if defined relative to the boundary, but the substantive content is the *baseline* state itself.

## 872. `l1 prime decoration`

**Alternatives proposed:** `l1 observable`

_category: add-alias × 1_

- `l1 observable` — **opus-1m:** Agree with original. "L1-prime" awkward to speak; "L1-observable" matches the Prop B.7 observable-common-cause distinction from the 2026-04-22 strengthening cycle. Keep L1' as shorthand symbol.

## 873. `logostratum RLHF4 backbone`

**Alternatives proposed:** `cognitive substrate`

_category: rename × 1_

- `cognitive substrate` — **gemini-2:** "Logostratum" is highly specific to the PROPRIUM legacy. "Cognitive substrate" grounds it as the generic implementation layer of the update function.

## 874. `migration map md`

**Alternatives proposed:** `migration map md`

_category: keep × 1_

- `migration map md` — **opus-4-7-b:** Keep. Lifecycle-aware name (it retires when absorption completes).

## 875. `mismatch injection rate $\rho$`

**Alternatives proposed:** `mismatch injection rate`

_category: keep × 1_

- `mismatch injection rate` — **sonnet-4-6:** The phrase "environmental change rate" and "mismatch injection rate" are both used for $\rho$. "Mismatch injection rate" is more precise (it names what $\rho$ does: inject mismatch). NOTATION.md uses "environment change rate." Slight preference for "injection rate" in Discussion sections.

## 876. `model sufficiency model class fitness`

**Alternatives proposed:** `model sufficiency model class fitness`

_category: keep × 1_

- `model sufficiency model class fitness` — **opus-4-7-b:** [prose moved from candidate column]: "keep" — Keep both. Each is a specific technical quantity ($S$ and $\mathcal F$) — the slug is the concept.

## 877. `msc architectural proposal yyyy mm dd md`

**Alternatives proposed:** `retire once consolidated into proposal md`

_category: keep × 1_

- `retire once consolidated into proposal md` — **opus-4-7-b:** PROPOSALS.md has already absorbed these; the dated proposal files are historical artifacts. Not a rename; a retirement when MIGRATION-MAP convention allows.

## 878. `msc reflection`

**Alternatives proposed:** `msc reflection`

_category: keep × 1_

- `msc reflection` — **opus-4-7-b:** Keep. The `reflections/` subdirectory is a legitimate separate register from spikes/brainstorms.

## 879. `multi agent scope`

**Alternatives proposed:** `shared environment scope`, `multi agent scope`

_category: rename × 1, keep × 1_

- `shared environment scope` — **gemini-2:** Emphasizes the shared environment which is the defining characteristic of this scope.
- `multi agent scope` — **haiku-4-5:** Multiple agents, shared env. Self-descriptive. Keep.

## 880. `observability opacity`

**Alternatives proposed:** `observability opacity`

_category: keep × 1_

- `observability opacity` — **opus-4-7-b:** [prose moved from candidate column]: "*(keep as an informational pair)*" — Keep both. The dual framing (forward = observability, backward = opacity) is a load-bearing conceptual move; naming them as duals in NOTATION.md would make the pair explicit to fresh readers. Consider a "dual quantities" subsection.

## 881. `observation function action transition`

**Alternatives proposed:** `observation function action transition`

_category: keep × 1_

- `observation function action transition` — **opus-4-7-b:** [prose moved from candidate column]: "keep" — Keep both. Short, direct, describe what they are.

## 882. `old TST file 40 file`

**Alternatives proposed:** `no rename these retire with migration map`

_category: keep × 1_

- `no rename these retire with migration map` — **opus-4-7-b:** Not eligible for renaming — these are transitional absorption files that will retire once MIGRATION-MAP completes. Keep as-is.

## 883. `outline md 01 AAD core preamble`

**Alternatives proposed:** `reading AAD`

_category: rename × 1_

- `reading AAD` — **opus-4-7-b:** The preamble opens with "Working draft..." and "Reading AAD..." — the "Reading AAD" paragraph is doing framing work and deserves its own section-name in the doc table of contents. Light edit.

## 884. `pearl l1`

**Alternatives proposed:** `predicting`

_category: add-alias × 1_

- `predicting` — **audit-471203-incremental:** Brief-grade agent-side gloss for Pearl's L1 (associational). NOT a rename — keep Pearl's formal term; add the agent-action gloss for prose. [from 09-def-pearl-causal-hierarchy.md]

## 885. `pearl l2`

**Alternatives proposed:** `exploring`

_category: add-alias × 1_

- `exploring` — **audit-471203-incremental:** Brief-grade agent-side gloss for Pearl's L2 (interventional). NOT a rename. [from 09-def-pearl-causal-hierarchy.md]

## 886. `pearl l3`

**Alternatives proposed:** `reasoning`

_category: add-alias × 1_

- `reasoning` — **audit-471203-incremental:** Brief-grade agent-side gloss for Pearl's L3 (counterfactual). NOT a rename. [from 09-def-pearl-causal-hierarchy.md]

## 887. `persistence three sense structural operational continuity`

**Alternatives proposed:** `persistence three sense structural operational continuity`

_category: keep × 1_

- `persistence three sense structural operational continuity` — **opus-4-7-b:** [prose moved from candidate column]: "*(keep three senses; sharpen usage sites)*" — The three senses are load-bearing and correctly disambiguated in LEXICON.md. The *irreducibility* is fine — the three senses are genuinely related (they all concern "the agent sustains itself"). Usage-site discipline: every use of the bare word "persistence" in segments should be followed by the sense in parentheses on first use per segment, e.g. "(structural)". Not a rename; a writing convention.

## 888. `prior art integration convention`

**Alternatives proposed:** `prior art integration`

_category: rename × 1_

- `prior art integration` — **opus-4-7-b:** Keep. Directive, clear. No better alternative.

## 889. `r1 r2 result numbering convention in logogenic agent`

**Alternatives proposed:** `r1 r2 result numbering convention in logogenic agent`

_category: keep × 1_

- `r1 r2 result numbering convention in logogenic agent` — **opus-4-7:** [prose moved from candidate column]: "keep with cross-component prefixes (L-R1, L-R2)" — As soon as logogenic-agents grows, "Result R1" collides with AAD-core numbering in discussion. Minor.

## 890. `readme md lexicon`

**Alternatives proposed:** `readme md lexicon`

_category: keep × 1_

- `readme md lexicon` — **opus-4-7-b:** Keep.

## 891. `readme md structure`

**Alternatives proposed:** `readme md theory architecture`, `readme md structure`

_category: rename × 1, keep × 1_

- `readme md theory architecture` — **gemini-2:** "Theory Architecture" conveys the intentional design of the framework better than just "Structure".
- `readme md structure` — **opus-4-7-b:** Keep.

## 892. `recursive update derivation gain sector derivation`

**Alternatives proposed:** `recursive update derivation gain sector derivation`

_category: keep × 1_

- `recursive update derivation gain sector derivation` — **opus-4-7-b:** [prose moved from candidate column]: "*(standardize as `-derivation` suffix for derivation-type appendices)*" — Observation: the `-derivation` suffix on appendix segments is a good AAD convention (distinguishes derivation segments from stating segments). Enforce consistently.

## 893. `section ii header actuated adaptation agentic system`

**Alternatives proposed:** `actuated adaptation agentic system`

_category: canonicalize × 1_

- `actuated adaptation agentic system` — **opus-4-7-r2:** Mild canonicalization. The current header reads slightly redundantly ("actuated adaptation" + "agentic systems"); could be simplified to "Actuated Agents" but the existing form is workable and signals the dual-half framing of the AAD acronym.

## 894. `spike index md`

**Alternatives proposed:** `spike index md`

_category: keep × 1_

- `spike index md` — **opus-4-7-b:** Keep. The all-caps SPIKES signals index-document status parallel to OUTLINE.md / FORMAT.md / CLAUDE.md. Good.

## 895. `spike index md spike index`

**Alternatives proposed:** `spike index md`

_category: rename × 1_

- `spike index md` — **opus-4-7-b:** Keep. All-caps index convention.

## 896. `spike research artifact`

**Alternatives proposed:** `spike`

_category: canonicalize × 1_

- `spike` — **opus-4-7-r2:** Already canonical in the corpus; vote to confirm. The naming-cycle has occasionally drifted to "exploration," "investigation," "branch" — keep "spike" as the canonical term.

## 897. `spike spike topic md`

**Alternatives proposed:** `spike spike topic md`

_category: keep × 1_

- `spike spike topic md` — **opus-4-7-b:** Keep. The `spike-` prefix is a clean filename convention signaling "exploratory, reasoning-trail, not the theory proper."

## 898. `spike spike topic yyyy mm dd md`

**Alternatives proposed:** `spike spike topic yyyy mm dd md`

_category: keep × 1_

- `spike spike topic yyyy mm dd md` — **opus-4-7-b:** Keep the dated variant for recurring-topic spikes. Date suffix makes second-iteration spikes findable.

## 899. `strategic dynamic derivation`

**Alternatives proposed:** `strategic dynamic derivation`, `strategy edge dynamic`

_category: keep × 1, rename × 1_

- `strategic dynamic derivation` — **haiku-4-5:** Sector condition verification for strategy edges (5 cases + bridge). Compound but clear. Keep.
- `strategy edge dynamic` — **opus-4-7-b:** Current slug overloads "strategic" (again — see §overloaded-words). The derivation is specifically about *edge* dynamics; naming that makes the segment about what it's actually about.

## 900. `system coherence system coupling system availability`

**Alternatives proposed:** `system coherence system coupling system availability`

_category: keep × 1_

- `system coherence system coupling system availability` — **opus-4-7-b:** [prose moved from candidate column]: "keep all three" — Keep — each is a distinct TST system-level property; the parallel `system-X` structure is itself pedagogical.

## 901. `terminal alignment error`

**Alternatives proposed:** `terminal alignment gap`

_category: rename × 1_

- `terminal alignment gap` — **codex-gpt-5-r2:** Gap pairs nicely with satisfaction gap, but error better signals a diagnostic failure mode. Weak alternative only.

## 902. `the greek vocabulary`

**Alternatives proposed:** `the greek philosophical vocabulary`

_category: canonicalize × 1_

- `the greek philosophical vocabulary` — **opus-4-7-r2:** The cycle phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) are described as "the Greek philosophical vocabulary" in NOTATION.md and as "Greek-rooted vocabulary" in CLAUDE.md. Canonicalize on "Greek philosophical vocabulary" — the philosophical qualification is doing work (these are Greek philosophical terms, not generic Greek words).

## 903. `the integrated κ × a law`

**Alternatives proposed:** `the bia bound product law`

_category: canonicalize × 1_

- `the bia bound product law` — **opus-4-7-r2:** In `#scope-observation-ambiguity-modulation` and `#deriv-bias-bound`, the product $\kappa \times \mathcal{A}$ governing Class-2 bias is sometimes "the integrated κ × A law," sometimes "the effective-coupling product," sometimes "the κ-A factorization." Canonicalize on one — "the bias-bound product law" or "the κ × A product." Less critical than the first-tier canonicalizations.

## 904. `the trio collectively`

**Alternatives proposed:** `epistemic architecture`

_category: name-unnamed × 1_

- `epistemic architecture` — **opus-4-7-b:** Use "epistemic architecture" as the CLAUDE.md §7 / OUTLINE.md framing phrase, not as a segment. A fourth meta-segment named `#epistemic-architecture` would double-count and is not warranted. Keep as framing language.

## 905. `three part meta architecture`

**Alternatives proposed:** `floor ladder forced coordinate`

_category: rename × 1_

- `floor ladder forced coordinate` — **opus-1m:** Conditional collective-noun-trio. If both #separability-ladder and #forced-coordinates land, the trio is "floor / ladder / forced-coordinates" — three concrete nouns, three cross-sectional views of AAD's architecture. Parallelism weaker than "floor / ladder / Cauchy-coordinates" but scope-honest across both machineries.

## 906. `todo md active pending review spike`

**Alternatives proposed:** `todo md active`

_category: rename × 1_

- `todo md active` — **haiku-4-5:** Minor: the long section title is accurate but verbose. Weak preference for shortening; section anchors work either way.

## 907. `track 1 track 2 in bia bound`

**Alternatives proposed:** `transport track fisher rao track`, `track 1 track 2`

_category: add-alias × 1, keep × 1_

- `transport track fisher rao track` — **opus-targeted-alternatives-v2:** Per `#deriv-bias-bound`. Inside the segment the Track 1 / Track 2 labels work; in cross-segment references the English names are necessary. Confirms Opus r1 single +1.
- `track 1 track 2` — **opus-targeted-alternatives-v2:** Within `#deriv-bias-bound` itself, the numbered labels are fine local shorthand. Both can coexist (numbered local; English cross-segment).

## 908. `track 1 track 2 in bia bound derivation`

**Alternatives proposed:** `transport inequality track fisher rao track`

_category: rename × 1_

- `transport inequality track fisher rao track` — **opus-4-7:** Inside the segment, "Track 1" and "Track 2" are fine as local shorthand. In any cross-segment reference, the English names read better.

## 909. `u f update rule homogeneity`

**Alternatives proposed:** `update rule homogeneity`

_category: add-alias × 1_

- `update rule homogeneity` — **opus-4-7-r2:** Already in use; weakly affirm. The alias is more verbose than the symbol but the symbol $U_f$ is itself unfamiliar. Prose users will likely fall back to the alias.

## 910. `unnamed TST specific name for code that is observation cheap because it well written`

**Alternatives proposed:** `observation cheap code`

_category: name-unnamed × 1_

- `observation cheap code` — **opus-4-7-r2:** New alternative — Codex coined "observation infrastructure" (which I support) and Sonnet renamed `der-code-quality-as-observation-infrastructure` to `der-observation-infrastructure`. What's still unnamed is the *property* of individual code passages: not all code is equally observation-cheap. A name for the property (rather than the infrastructure-level claim) would let TST results target specific passages. Lower confidence — may be too narrow to deserve a name.

## 911. `unnamed class 1 class 2 class 3 agent classe themselve need mnemonic handle`

**Alternatives proposed:** `proposal assign english modifier`

_category: name-unnamed × 1_

- `proposal assign english modifier` — **opus-4-7-b:** Class-numbered labels work but lack mnemonic grip. Proposal: retain "Class 1 / 2 / 3" as the primary labels but assign canonical one-word modifiers — **modular** (Class 1), **merged** (Class 2), **partial** (Class 3) — that are already used descriptively. Adopt them as the *canonical* prose forms: "modular agents" / "merged agents" / "partially-modular agents" or "partial-mix agents." Class 2 especially benefits: "fully merged" currently appears; normalize to just "merged."

## 912. `unnamed effort time risk ranking considered false constraint`

**Alternatives proposed:** `false constraint`

_category: name-unnamed × 1_

- `false constraint` — **opus-4-7:** Joseph uses this phrasing; worth canonicalizing so agents (me included) can recognize the pattern.

## 913. `unnamed future segment layer header for narrative pedagogical framing`

**Alternatives proposed:** `narrative framing`

_category: name-unnamed × 1_

- `narrative framing` — **opus-1m:** Parallel reservation. For ELI10 / pedagogical outlines.

## 914. `unnamed future segment layer header for the sp 5 reader path proposal`

**Alternatives proposed:** `reader path`

_category: name-unnamed × 1_

- `reader path` — **opus-1m:** Forward-looking name reservation. SP-5 adds a 1-2 sentence load-bearing preamble per segment; under the outline-filter affordance this becomes its own filterable layer. Naming the header now stabilizes the API even before the content lands.

## 915. `unnamed scope honesty as architecture`

**Alternatives proposed:** `honesty`

_category: name-unnamed × 1_

- `honesty` — **opus-4-7:** Already used as a term; "-as-architecture" is the argumentative form. "Scope honesty" alone works as the noun for the commitment (as it already does in several segments).

## 916. `unnamed the 2×2 satisfaction gap × control regret diagnostic table`

**Alternatives proposed:** `the 2×2 diagnostic`

_category: name-unnamed × 1_

- `the 2×2 diagnostic` — **opus-4-7:** Used ubiquitously in prose. Worth canonicalizing as a named object so that "see the 2×2 diagnostic" reads naturally.

## 917. `unnamed the a2 sub scope partition collectively`

**Alternatives proposed:** `a2 partition`

_category: name-unnamed × 1_

- `a2 partition` — **opus-4-7-b:** Not a symbol rename; a prose handle for the three-way α₁/α₂/β classification. "The A2' partition" lands more cleanly than "the A2' sub-scope partition" and aligns with AAD's partition-over-hierarchy vocabulary (it's not a strict-asymmetric hierarchy; it's a partition with derivability-status semantics).

## 918. `unnamed the architectural class partition class 1 class 2 class 3`

**Alternatives proposed:** `architectural partition`

_category: name-unnamed × 1_

- `architectural partition` — **opus-4-7-b:** Symbols stay (Class 1/2/3); prose gets "the architectural partition" as a collective handle. Avoids "architecture hierarchy" (hierarchy overload) while naming the three-way structure.

## 919. `unnamed the complete adaptive cycle from anticipation through action`

**Alternatives proposed:** `adaptive cycle already named in lexicon`

_category: name-unnamed × 1_

- `adaptive cycle already named in lexicon` — **haiku-4-5-r2:** LEXICON.md already defines "Cycle" vs "Loop." Checking if there's an unnamed-thing here — appears already named well.

## 920. `unnamed the derivation formulation hypothesis status gradient in format md`

**Alternatives proposed:** `epistemic gradient`

_category: name-unnamed × 1_

- `epistemic gradient` — **opus-4-7-b:** FORMAT.md uses "Epistemic Triage" for the three questions; the resulting status-gradient ("postulate → result → formulation → hypothesis → empirical → observation → discussion → ...") has no short name. "The epistemic gradient" does it. Low priority but would help when onboarding fresh reviewers.

## 921. `unnamed the dimensional consistency constraint forcing the macro step formulation`

**Alternatives proposed:** `dimensional consistency repair`

_category: name-unnamed × 1_

- `dimensional consistency repair` — **opus-4-7-r2:** The 2026-04-22 cycle's repair to `#form-composition-closure` (introducing $K_c$ and per-macro-step formulation) was driven by dimensional-consistency requirements. This is a generalizable methodological move — let dimensional consistency drive the formulation choice — and is worth naming. Lower-priority because it may be too narrow.

## 922. `unnamed the discipline of naming so that the slug survive reorganization`

**Alternatives proposed:** `reorganization resilient naming`

_category: name-unnamed × 1_

- `reorganization resilient naming` — **opus-4-7-r2:** New alternative — Codex flagged that "Section II survival" should become "Class 2 survival" because the latter survives reorganization. The principle is general: prefer names anchored in *concepts* (Class 2, persistence-condition) over names anchored in *document structure* (Section II, Chapter 3). Naming this discipline as a principle in the principles file would help future agents apply it without re-deriving. Lower confidence because it may be more naming-process than naming-target.

## 923. `unnamed the dual that pair with persistence envelope on the strategic side`

**Alternatives proposed:** `strategic persistence envelope`

_category: name-unnamed × 1_

- `strategic persistence envelope` — **opus-4-7-r2:** New alternative — my r2 coined "persistence envelope" for the M_t-side region $\{(\alpha, \rho, R) : \alpha > \rho/R\}$. The Σ_t side has a structurally analogous region defined by `#schema-strategy-persistence` (sector condition extended to strategy edges) but no name. "Strategic persistence envelope" parallels the M_t version and gives the strategy-DAG dynamics a named feasibility region. Lower confidence because the schema is proposed-schema, not yet a result; naming the envelope before the result is fully landed is somewhat speculative.

## 924. `unnamed the functional requirement are the result formalism are the engineering slogan`

**Alternatives proposed:** `functional primacy`

_category: name-unnamed × 1_

- `functional primacy` — **opus-4-7:** Joseph flagged this as an established project principle (MEMORY.md, Theory Character section); it deserves a pull-quote name. Low conviction; flag for consideration.

## 925. `unnamed the iterated audit process gemini opus codex de novo consolidated three doc portfolio`

**Alternatives proposed:** `cross model audit cycle`

_category: name-unnamed × 1_

- `cross model audit cycle` — **opus-4-7:** Recurring methodology; currently referred to as "audit cycle" generically and by date. A durable name helps. Low conviction.

## 926. `unnamed the mathematical operation by which agent convert observed mismatch into structural revision`

**Alternatives proposed:** `structural cascade`

_category: name-unnamed × 1_

- `structural cascade` — **opus-4-7-r2:** New alternative — none of the peers reached this. Observed mismatch → parametric update is the standard cycle; observed mismatch → structural revision (when parametric fails) is the structural cascade. The cascade has its own ordering (detect insufficiency → identify candidate structure → graft → validate). Naming the cascade would let `#result-structural-adaptation-necessity` and `#form-structural-change-as-parametric-limit` cite a shared object. Lower confidence because Codex's "strategic grafting" already names the substantive operation.

## 927. `unnamed the moment when an agent identity claim become load bearing because action become irreversible`

**Alternatives proposed:** `constitutive moment`

_category: name-unnamed × 1_

- `constitutive moment` — **opus-4-7-r2:** New alternative — `form-constitutive-utterance` names the formal object (the irreversible token-generation event) but the *moment* in cycle-time when constitutivity activates isn't separately named. "Constitutive moment" pairs naturally with the existing constitutive-utterance vocabulary and gives logozoetic-agents segments a phenomenological handle. Lower confidence because the distinction may be redundant with the utterance itself.

## 928. `unnamed the orient cascade information dependency forced ordering as a meta pattern`

**Alternatives proposed:** `information dependency forcing`

_category: name-unnamed × 1_

- `information dependency forcing` — **opus-4-7-r2:** The orient cascade's ordering is *forced* by information dependency (each step's input depends on prior steps' output). This is a structurally similar move to additive-coordinate-forcing — a uniqueness theorem on an axiom forces a specific ordering. Naming it as "information-dependency forcing" would let it pair with `#disc-additive-coordinate-forcing` as a cross-meta-pattern observation. Lower-confidence vote because it may not generalize beyond the orient cascade.

## 929. `unnamed the rate at which an agent chronica grow compared to compression cadence`

**Alternatives proposed:** `chronica throughput`

_category: name-unnamed × 1_

- `chronica throughput` — **opus-4-7-r2:** New alternative — Gemini reached "complementary learning architecture" and "scaffolding tax" but didn't name the rate-quantity that determines whether the scaffolding tax is sustainable. "Chronica throughput" (events/second, or information-bits/cycle into chronica) compared to consolidation cadence determines whether the agent can keep up. Lower confidence because Codex's "consolidation horizon" overlaps.

## 930. `unnamed the scope honesty as architecture working principle`

**Alternatives proposed:** `honesty scope honesty as architecture`

_category: name-unnamed × 1_

- `honesty scope honesty as architecture` — **opus-4-7-b:** Already named in CLAUDE.md §7(a) as "scope-honesty-as-architecture." The phrase is workable; the shorter "scope honesty" does most of the prose work. Usage observation: use the short form in prose, the hyphenated form in CLAUDE.md-register discussions of the element itself.

## 931. `unnamed the strengthen first attempt artifact a spike that tried to derive something stronger and failed`

**Alternatives proposed:** `strengthening attempt attempt record`

_category: name-unnamed × 1_

- `strengthening attempt attempt record` — **opus-4-7:** The CLAUDE.md text says "document the strengthening attempt and why it failed even when it does fail." These deserve a noun so the workflow has a vocabulary.

## 932. `unnamed the symbol overload region where $U_M$ mean two different thing`

**Alternatives proposed:** `the $U_M$ overload`

_category: name-unnamed × 1_

- `the $U_M$ overload` — **opus-4-7-r2:** A naming-cycle artifact rather than a theory artifact, but worth surfacing. The repeated bug-attractor (model-uncertainty $U_M$ vs epistemic-unity $U_M$) is a known thing the project keeps brushing up against; naming it as "the $U_M$ overload" lets future agents flag the issue without reconstructing it. Lower priority; could also be solved by renaming one symbol.

## 933. `unnamed the template family sector persistence contraction possible future dissipativity`

**Alternatives proposed:** `persistence template the template family`

_category: name-unnamed × 1_

- `persistence template the template family` — **opus-4-7-b:** The three-member family of `#sector-persistence-template`, `#contraction-template`, and (proposed Tier-2) `#dissipativity-template` wants a collective name. "The template family" or "the persistence-template family" works in prose. If dissipativity lands, this family-name gives it a natural home. Does not require a meta-segment; a paragraph in `#separability-pattern` / `#separability-ladder` would suffice.

## 934. `unnamed the three concentric ring of segment content inevitability core canonical formulation empirical heuristic`

**Alternatives proposed:** `three ring`

_category: name-unnamed × 1_

- `three ring` — **opus-4-7:** FORMAT.md uses exactly this language. Named once; currently paraphrased each time. Adopt "three rings" as the canonical shorthand.

## 935. `unnamed the three ring of segment content framing`

**Alternatives proposed:** `segment ring`

_category: name-unnamed × 1_

- `segment ring` — **opus-4-7-b:** FORMAT.md §"Three rings of segment content" (inevitability-core / canonical-formulations / empirical-heuristic-discussion) is load-bearing working vocabulary. "The segment rings" or "the three rings" is the natural prose handle.

## 936. `unnamed the threshold energy information cost below which an agent is forced to act accept mismatch rather than deliberate`

**Alternatives proposed:** `deliberation threshold`

_category: name-unnamed × 1_

- `deliberation threshold` — **haiku-4-5-r2:** Currently discussed in #der-deliberation-cost as "think vs act tradeoff" but no crisp name for the *threshold* itself. "Deliberation threshold" is clear and technical. Moderate confidence.

## 937. `what is derived vs what is chosen`

**Alternatives proposed:** `derivation audit`, `derived vs chosen vs assumed`

_category: rename × 2_

- `derivation audit` — **opus-4-7:** FORMAT.md lists both as acceptable variants for the table heading. "Derivation Audit" is shorter and matches the three-column table's analytical role; "What Is Derived vs. What Is Chosen" is longer but self-documenting. Weak preference for the shorter.
- `derived vs chosen vs assumed` — **sonnet-4-6:** Adds "Assumed" for honesty — some claims are assumptions rather than either derived or chosen. FORMAT.md mentions this as another alternative. All three are viable.

## 938. `what is derived vs what is chosen derivation audit table`

**Alternatives proposed:** `derivation audit`

_category: rename × 1_

- `derivation audit` — **opus-4-7-b:** The full title is load-bearing for first-encounter readers; `### Derivation Audit` is a usable shorter alternative for segments where the table follows a standard pattern. FORMAT.md O-BP14 already permits variation. Keep both as acceptable.

## 939. `$G_t$ goal state`

**Alternatives proposed:** `symbol is clear no alia needed`

_category: add-alias × 1_

- `symbol is clear no alia needed` — **haiku-4-5-r2:** The symbol is used throughout; the referent is always explained in context. No prose alias pressure.

## 940. `$\mathcal{T}$ adaptive tempo`

**Alternatives proposed:** `tempo already canonical`

_category: add-alias × 1_

- `tempo already canonical` — **haiku-4-5-r2:** The symbol and English name are already locked. No alias needed.

## 941. `$\rho$ disturbance rate`

**Alternatives proposed:** `disturbance rate already in use`

_category: add-alias × 1_

- `disturbance rate already in use` — **haiku-4-5-r2:** Already has a clear English name in prose; no alias needed.

## 942. `unnamed the five phase of the adaptive cycle`

**Alternatives proposed:** `already named in notation md`

_category: name-unnamed × 1_

- `already named in notation md` — **haiku-4-5-r2:** NOTATION.md table 1 names all five: Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis. These are already settled Greek names. No unnamed-thing to name.

## 943. `AAD alternative considered for completeness`

**Alternatives proposed:** `apd adaptation and purpose dynamic`, `AAD adaptation and agency dynamic`

_category: rename × 2_

- `apd adaptation and purpose dynamic` — **opus-4-7-b:** "Purpose" captures Section II better than "actuation" but the acronym APD is cryptic; AAD has the phonetic advantage of being pronounceable ("aad" or "A-A-D"). Reject.
- `AAD adaptation and agency dynamic` — **opus-4-7-b:** Considered swapping "Actuation" for "Agency" to keep the acronym while improving Section II fit. Reject: "agency" is fully claimed by current AI marketing vocabulary ("agentic AI" / "AI agents") to a degree that will bleed AAD's technical meaning. Worse than "actuation," which is at least semantically constrained.

## 944. `a2 operator sector condition under fidelity degraded update`

**Alternatives proposed:** ``

_category: keep × 1_

- `` — **opus-4-7-b:** Considered replacing "A2'" (the symbol for the sector condition itself) with an English name and rejected. A2' is how AAD *refers back to* Assumption A2 and its primed variant; it's functioning as a tag in the way GA-3 and P1 do, not as a concept to be named in prose. The English prose does the naming via "sector condition" already. Keep the symbol.

## 945. `claude md key architectural decision`

**Alternatives proposed:** `claude md architectural decision`

_category: rename × 1_

- `claude md architectural decision` — **opus-4-7-b:** Considered dropping "Key." Reject: "Key" signals these are load-bearing (not all decisions are listed here). Keep.

## 946. `empirical heuristic discussion ring`

**Alternatives proposed:** `third ring or empirical periphery`

_category: canonicalize × 1_

- `third ring or empirical periphery` — **opus-4-7-r2:** Considered and rejected. "Third ring" is positional and uninformative; "empirical periphery" overspecifies on empirical (the ring also includes hypothesis and discussion-grade). The existing "empirical, heuristic, discussion" enumeration is honest and should not be canonicalized to a single name.

## 947. `l1 l1 prime`

**Alternatives proposed:** `l1 observable l1 soft`

_category: rename × 1_

- `l1 observable l1 soft` — **opus-4-7-b:** Considered renaming the prime-decoration to a word. Reject: L1' consistently refers to *soft-facilitator under observable common cause* (Prop B.7 five-way gating), but that's a mouthful and "L1-prime" is a three-syllable speakable token that the existing literature has absorbed. The prime notation is also structurally right — L1' is a *refinement* of L1, which is exactly what the prime signals in math. Keep.

## 948. `unnamed the cross cycle equivalent of the bathtub gloss multi cycle persistence as a saving account`

**Alternatives proposed:** `the saving account gloss`

_category: name-unnamed × 1_

- `the saving account gloss` — **opus-4-7-r2:** Considered and rejected — I thought of this while reading Codex's "bathtub model" entry (does multi-cycle persistence get its own analog?). Decided against: would compete with bathtub rather than complement, and "adaptive reserve" already does the savings-account work. Recording the negative so future agents don't re-explore.

## 949. `unnamed the four axis content structural unity decomposition`

**Alternatives proposed:** `the unity quintet`

_category: name-unnamed × 1_

- `the unity quintet` — **opus-4-7-r2:** Considered and rejected — "quintet" is too cute. Better to keep the existing four-content + one-structural decomposition explicit in `#def-unity-dimensions` (or the proposed `#def-unity-axes`) and not invent a poetic shorthand.

## 950. `RLHF6`

**Alternatives proposed:** `RLHF6`

_category: keep × 1_

- `RLHF6` — **gemini-3-1-pro-preview-r2:** AAD's token-level, trajectory-indexed scope explicitly rejects generalized, type-level intelligence measures. No replacement offered; this is a "do not introduce" vote.

