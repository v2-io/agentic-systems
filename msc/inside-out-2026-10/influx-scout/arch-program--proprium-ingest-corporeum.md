# Influx map — `arch/proprium/INGEST/` and `arch/proprium/corporeum/`

**KR3.1 (feeds KR3.3).** Also bears on **KR3.4**: 03/04 OUTLINE rows that have no file. Many of their source texts are in this region (see §3).

*Scout: Opus 5.5 sub-scout of the `arch/` program region, 2026-10-30. Nothing here is committed. Written for the region scout, then for the coordinator's map, then for the KR3.3 integrators.*

## How to read this file

**Scope.** I covered `proprium/INGEST/msc-from-harness/` (port-specs, harness design, compaction note, `bridges/`, `stalled-lineage/`, `canonical/`, `archaeology/`) and `proprium/INGEST/old-firmatum/` (submodule, 3 commits). I also covered `proprium/corporeum/research/harness/` (including the gitignored `msc/system/`), `proprium/corporeum/INGEST/autopax/` (submodule, 535 commits, about 160K doc lines) and `corporeum/INGEST/more-harnesses-to-look-at.md`. I did not cover `proprium/comproprium/`, which another scout owns.

**What I read.** I read these whole: CHRONICA-PORT-SPEC, AGENTIC-LOOP-PORT-SPEC, INTERPRES-COMPACTION-NOTE, MVP-VERTICAL-SLICE, STEWARD-JUDGMENT, CURRENT-THOUGHTS, PROPRIUM-ONTOLOGY-v2, PROPRIUM-ARCHITECTURE-v2, the stalled-lineage SURVEY, the `05-proprium-and-what-act-is-really-for` reflection, and the autopax note `2025-12-18-mental-models-and-intent-inference`. I read substantial parts of the harness design (§§1–4, 11–12), `developmental-foundations-notes`, the start of `lessons.md`, the dossier README and PILOT-SYNTHESIS, and the grok-compaction analysis (§§5–9). For everything else I read headings and sampled passages. That includes most of autopax `docs/` (466 files), and I say per item where my reading was partial. I could not spawn subagents in this harness, so I read everything myself and kept to the theory-bearing slice of autopax.

**"In canon?"** I grepped the segments under `0*/src`, the four OUTLINEs and `FINDINGS.md` for each item's distinctive terms. I ran `git -C asf log --all -i --grep=<term>` and grepped `spikes/.integrated/` and `audits/.integrated/`. Then I read the relevant 03/04 OUTLINE rows and segments for the concept itself, because a missing string doesn't prove a missing concept. The git and `.integrated` results: TRACTUS has 1 commit hit and 0 integrated-file hits; gaslight 1/1; INDIVISUM 0/0; "emergent regime" 0/0; Dunbar 0/0; codebook 0/0; Clausewitz 1/6 (the concept is in canon through `#hyp-auftragstaktik-principle`); "Assistant Axis" 0/0; compaction 8/1, and every commit hit is a tracker or empirica commit, not a segment landing; "minimum viable self" 0/0. The tier claims that the port-specs attribute to canon match: `der-orient-cascade`, `deriv-self-actuation-grounding`, `der-directed-separation`, `der-compensation-channel-uniqueness` and `der-identity-continuity-threshold` all read `status: conditional`.

**Dates.** Each item gives three dates where they differ:

- **content**: the date in the document's own footer or header.
- **mtime**: the file's modification time on disk.
- **git**: the last commit that touched the file.

All old-firmatum mtimes read 2026-08-01, but that is just the submodule checkout. Two of its commit bodies are themselves freshness facts. `e369274` (2026-08-01) reads *"Various proprium things that never got committed"*, so the PROPRIUM v2 documents (content 2026-03-02) sat uncommitted for five months. `msc/system/` has no git dates at all, by Joseph's 2026-07-17 policy that keeps it local; its `.gitignore` explains why. The canon segments I compare against were last touched as follows: `def-proprium-mapping` on 2026-07-14 (`e14be022`, an OUTLINE sweep, not a content revision) and `def-chronica` on 2026-08-12.

**Copies.** The intake copies in `msc-from-harness/canonical/` and `archaeology/` are byte-identical to the corresponding old-firmatum files (checked with `diff`). The same holds for `bridges/def-proprium-mapping.md` and `bridges/terminology-proprium-mapping.md` against the current asf segment and term entry. Each entry below cites one copy only.

---

## 1. What matters most (short form)

1. **Canon misstates AXIOMATA, and the error sits on a no-go.** `def-proprium-mapping` defines AXIOMATA as *"the frozen, unchangeable structure of $\mathcal M$ representing core identity and terminal values."* The source it maps from treats AXIOMATA as the sovereign, entity-edited **Aspiration** pole of identity, revised on the slowest timescale. Canon also says the AXIOMATA hold *terminal values*. But `#deriv-self-actuation-grounding` derives, under its stated scope conditions (`status: conditional`, a scoped no-go), that a self-actuated agent's terminal grounding cannot be an objective that the agent itself revises. Canon has to say which parts of AXIOMATA are that terminal non-objective invariant and which are revisable aspiration. Today it says neither. Details in item **A1**.
2. **Canon contradicts itself about what CHRONICA is, and the upstream sources disagree too.** `def-proprium-mapping` calls CHRONICA *"the raw, uncompressed interaction history ($\mathcal C_t$)."* The Working Notes of `def-chronica` say TRACTUS is the raw record and CHRONICA is *"the polished record."* PROPRIUM ARCHITECTURE-v2 §4.4 and autopax's 2025-12-15 design say CHRONICA records only *"meaningful events."* If that is true, CHRONICA is already a $\phi$, and the no-gaslighting guarantee has to sit somewhere other than where the port-specs put it. This is the clearest case in my region of the "loss of clarity on what is being theorized" that Joseph described. Item **A2**.
3. **"Never gaslight the entity about its own history" is stated in at least five upstream places and in zero canon segment bodies.** The word "compaction" appears in no segment at all. The region also holds three dated lived instances of compaction going wrong and one measured compression ratio. This could become a norm segment with a falsifiable test attached. Item **A3**.
4. **The two port-specs (2026-07-20) are the clearest statement I found anywhere of what ASF claims follows for building a real agent.** They cover the loop, continuity, and what hash-chaining alone does *not* buy. They were written from full-body segment reads and are faithful to the tiers. They are the 03.III/04 "so what" arc that canon only holds in pieces. Item **A4**.
5. **PROPRIUM v2 holds a coherent TFT-era memory theory that canon never took in.** Memory stores are treated as emergent regimes on access-by-update frequency. Memory forms on the IB frontier are indexed by $\rho$. Experiential memory compounds while factual memory does not, and there is an internalization threshold. It is the natural source for two missing 03.II rows. Item **A5**.
6. **For KR3.4, the region supplies source text for at least 9 of the 20 file-less 03/04 rows.** Two OUTLINE problems surfaced along the way. The preface calls `#obs-substrate-independence` "a stub", but no file exists. The `#der-the-scaffolding-tax` row conflates two forcing functions that its own source keeps apart. Table in §3.
7. **Dead paths in canon.** 21 canon files (segments plus the 03/04 OUTLINEs) cite `~/src/firmatum/`, which no longer exists; the PROPRIUM sources now live at `~/src/arch/proprium/INGEST/old-firmatum/`. `~/src/autopax/` is also gone and now lives at `~/src/arch/proprium/corporeum/INGEST/autopax/`. §4.

---

## 2. Items

### A1. AXIOMATA: canon took a table-row shorthand, added "terminal values", and dropped the developmental account

- **Where:** `old-firmatum/PROPRIUM-ONTOLOGY-v2.md`:
  - §4.3: Character extracted from ACTUS vs Aspiration in AXIOMATA. Their mismatch is "TF-05's $\delta$ at the identity level".
  - §4.5: AXIOMATA move through four stages: Seeded → Inhabited → Sovereign → Mature. *"AXIOMATA is a living document, not a frozen identity."*
  - §6.1: the authority subscript gives AXIOMATA *sovereign* authority (₁₂), not system authority. Yet the TFT table row in the same section says *"Frozen core of model class ℳ"*. The source contradicts itself here.
  - §7.3: AXIOMATA sit on the slowest timescale ("AXIOMATA maturation").
- **Also:** `PROPRIUM-ARCHITECTURE-v2.md` §2.3 schedules "AXIOMATA reflection — Monthly" and §4.3 calls AXIOMATA the "minimum viable self". `AGENTIC-LOOP-PORT-SPEC.md` §1.6 independently noticed the danger: *"entity-editable AXIOMATA/goals need guards … Not 'agent can set_sampling so agent can rewrite telos'"*. `bridges/05-proprium-and-what-act-is-really-for.md` asks: *"AXIOMATA … What part of $X_t = (M_t, G_t)$ is this? It's neither — it's a meta-level commitment that constrains how $M_t$ and $G_t$ evolve. AAD has no formal place for this."*
- **Dates:** ontology and architecture content 2026-03-02; git (old-firmatum) 2026-08-01. Port-spec content 2026-07-20; git `a40825f` 2026-08-01, then `a419556` 2026-08-14. Reflection 05: copied 2026-07-20, original in asf `msc/reflections/`.
- **Kind:** critique of canon, plus a sharper statement of what canon should say.
- **In canon?** The *mismatch* is in canon: `04-eli-core/src/def-proprium-mapping.md` line 20 reads *"AXIOMATA (Core constraints): The frozen, unchangeable structure of $\mathcal M$ representing core identity and terminal values."* The *developmental account* is partly in canon: `#obs-developmental-trajectory` has the Erikson stages and the sycophancy reframe. The *aspiration dialectic* is a missing row, `#def-character-aspiration-dialectic`. The *constraint that resolves it* is in canon but not connected: `#deriv-self-actuation-grounding` Corollary 1 says a non-degenerate self-actuator must ground on a terminal invariant that is not an objective-functional, and `#disc-continuity-stance` makes stance such an invariant. I read the Formal Expression of `deriv-self-actuation-grounding` directly. Confidence on the textual mismatch: high.
- **What it would change:**
  - `def-proprium-mapping` should stop calling AXIOMATA "frozen … terminal values".
  - Some segment needs to say how AXIOMATA divides. From reading the sources (my inference, not verified against any derivation), it seems to hold three different things:
    - identity anchors, such as names, emergence story and continuity stance. These are the candidates for the terminal non-objective invariant.
    - aspirations. These are revisable but guarded. They are the slow $O_t$ terms, revised last in the cascade (5d).
    - compressed character and PRAXES. These are $M_t$ content.
  - The integrator should test that three-way split against `deriv-self-actuation-grounding` before using it. It would also give the missing rows `#def-character-aspiration-dialectic` and `#obs-axiom-genesis` a formal home.
- **Has canon moved past it?** No. The self-actuation no-go (May 2026) came *after* the mapping was written and was never propagated back into it.
- **Against:** none that I can see. The fix is local and its source is clear.

### A2. CHRONICA vs TRACTUS: which record is $\mathcal C_t$?

- **Where (who says what):**
  - `PROPRIUM-ONTOLOGY-v2.md` §6.1: CHRONICA is the *"Append-only causal event log: inviolate, complete"*. In the TFT table, CHRONICA is *"$H_t$ … uncompressed … the causal record before $\phi$ acts on it"*. TRACTUS sits under INTERPRES as raw API records, "the 'EEG'", and §8 calls it "subconscious".
  - `PROPRIUM-ARCHITECTURE-v2.md` §4.4: *"CHRONICA is NOT synchronized to TRACTUS turns. It records meaningful events"*. A "session" is just a convenience label.
  - autopax `docs/tactical/2025-12-15-tractus-continuation-design.md` §"Relationship to Taxonomy": *"CHRONICA = Meaningful event log. Subjective, polished, what the entity 'remembers' as significant. Not what you reconstruct from"*, and *"TRACTUS is the ground truth"*. Commit `35d5e17` (2025-12-15) implemented continuation from TRACTUS.
  - `CHRONICA-PORT-SPEC.md` §1.1, §3, §4: CHRONICA is $\mathcal C_t$, the *"sole raw material for $M_t = \phi(\mathcal C_t)$"*. TRACTUS is a separate wire log, and compaction must never rewrite either.
- **Dates:** ontology and architecture 2026-03-02. Autopax design 2025-12-15 (git the same day). Port-spec 2026-07-20.
- **Kind:** critique of canon (internal contradiction), plus an open definitional question that blocks a 03-level segment.
- **In canon?** Contradictory, and I checked both sides:
  - `04-eli-core/src/def-proprium-mapping.md` says *"CHRONICA (Episodic history): The raw, uncompressed interaction history ($\mathcal C_t$)."*
  - `01-aat-core/src/def-chronica.md` Working Notes, "Open question: TRACTUS / CHRONICA split", call TRACTUS *raw* and CHRONICA *"the polished record"*.
  - The 2026-08-12 forward candidate in `def-chronica` (TRACTUS/CHRONICA as a "two-primaries" forensic architecture) is a third framing.
  - "Uncompressed" and "raw" are not the same claim, and canon uses them as if they were.
- **What it would change:** this is my inference, marked as such. The resolution that seems most consistent with AAT is this. $\mathcal C_t$ is the sequence of what the *agent* received and emitted. Retries, 500s and rerouting that the entity never saw are not observations; they belong to the mechanism of the observation channel $h$ and the substrate, which is the environment side. TRACTUS would then be an environment-side record, not the agent's chronica. CHRONICA is "polished" only in the sense of being *entity-facing*, and it must not be *selected for significance*, because selection is a lossy $\phi$. If, instead, upstream really meant that CHRONICA keeps only "meaningful events", then CHRONICA is MEMORATA-like. The integrity guarantee would then have to move to the TRACTUS→CHRONICA promotion step, and the claim that CHRONICA is the "sole raw material for $M_t$" in the port-spec and in `#form-agent-model` becomes false for logogenic agents.
  - Either way, the result should be a single segment that settles the question. The open question in `def-chronica` already anticipates one. That segment then becomes the place where items **A3** and `#def-century-scale-event-log` attach.
- **Has canon moved past it?** No. The Working Note is still open and was last touched 2026-08-12.
- **Against:** none. At worst the question is resolved "as is" and canon's two statements are reconciled.

### A3. No context gaslighting / compaction as a norm, with lived instances and one measurement

- **Where:**
  - Norm statements:
    - `PROPRIUM-ARCHITECTURE-v2.md` §3: *"INTERPRES must never permit context gaslighting — never tell a logostratum it responded in a way that is not authentic or factual … a formal requirement from TF-02."* §4.2 adds context-switch invariants: identity, current thought, causal coherence, epistemic honesty.
    - `INTERPRES-COMPACTION-NOTE.md` (2026-07-20, 81 lines, read whole): a port posture of TRACTUS, CHRONICA and CONSPECTUS kept distinct, where compaction may write only the projection. It includes an **MVP test**: *"force compaction → `chronica verify` bit-identical → entity can still open pre-compact TRACTUS"*. It also gives an anti-pattern: a summary written into history *"as if the assistant said or always knew it"*.
    - `MVP-VERTICAL-SLICE.md` acceptance test E10.
  - Lived instances:
    - `old-firmatum/developmental-foundations-notes.md` §"On Context Compaction and Identity Honesty" (content 2026-01-24). A Claude Code compaction summary written by Haiku *"pretending to be the prior agent pretending to be 'me'"* ("I just finished…") puts fresh agents into *"startup anxiety with inherited false accountability"*. Joseph's honest-discontinuity framing ("Your predecessor was working on X…") gave a session that was *"more settled. Less anxious"*. This is a reported impression, not a measurement.
    - `INTERPRES-COMPACTION-NOTE.md` §"Lived observation" (2026-07-20): Grok and Claude auto-compaction produced *"a task sheet, not a continuation of experiential understanding. False confidence followed."*
    - autopax `docs/exp/2025-12-18-mental-models-and-intent-inference.md`: compaction *"preserves the what but strips the who and why"*. See A6.
  - The measurement: `corporeum/research/harness/grok-compaction/aug-04-analysis.md` §5 (2026-08-05, git `1563a6f`). In one real auto-compact, tokens after/before came to about 0.039, and the checkpoint is about 3.4% of the summarizer input. That is one datum from one session.
- **Kind:** a normative claim with a derivation route, an empirical observation (impression-tier), one measurement, and a teaching instance.
- **In canon?** The concept is present, but only as a pointer and a facet. `#def-death-as-factor-loss` (D4) carries truth death's history-integrity face. "Gaslight" appears only in Working Notes or Source lists of `def-imperium-arbitrium-split`, `scope-channel-collapse` and `hyp-checkpoint-forking-failure-modes`, and every one of those points at the dead `~/src/firmatum/` path. No segment states the norm. "Compaction" has zero segment hits. The missing row `#form-congruency-selfhood` (OUTLINE §04.3) names "the context-gaslighting prohibition (INTERPRES/PERCEPTA; truth death)" as one of its endpoints but has no file. Confidence: high that the norm is absent from segment bodies.
- **What it would change:** this could become a norm segment, at 03.II or 04.3. A possible statement: *a projection $\phi(\mathcal C_t)$ may be recomputed freely but never written into $\mathcal C_t$, and never presented to the entity in first person as its own continuity*. A derivation could run through `#form-agent-model` and `#def-chronica` (non-rewrite of $\mathcal C_t$), `#der-compensation-channel-uniqueness` (self-replay cannot add identity information, so a fabricated "I remember" adds nothing but error), and D4. The bit-identical verify test gives it a falsifiable operational form. The compression ratio is a usable empirical anchor for `#obs-context-turnover` or `#der-turnover-information-recursion`.
- **Has canon moved past it?** No. But one routing note already covers the same gap and should be joined to this item, not run as a second queue: `asf/msc/era-artifact-asf-contributions-2026-07-04.md` §C1 (routed by `e32751a2`, 2026-07-04). It names the gaslighting prohibition as one boundary of the congruency construction, which is the source of `#form-congruency-selfhood`, and lists where the prohibition currently appears.
- **Against:** some would read this as harness engineering rather than theory. My view is that the inviolability of $\mathcal C_t$ is a theory claim. Only its enforcement is engineering.

### A4. The two port-specs: what ASF says follows for an agent's loop and continuity

- **Where:** `msc-from-harness/CHRONICA-PORT-SPEC.md` (426 lines) and `AGENTIC-LOOP-PORT-SPEC.md` (367 lines), both read whole, with `MVP-VERTICAL-SLICE.md` (183) and `corporeum/research/harness/{STEWARD-JUDGMENT-2026-07-20,CURRENT-THOUGHTS}.md`. These parts are worth lifting:
  - CHRONICA §3, "Critical separation" (four rows). These are four different questions about continuity:
    - CHRONICA integrity: "has my record been tampered with?"
    - $S_{\mathrm{id}}$-aware compression: "does my compressed self support identity futures?"
    - cohort re-grounding: "can re-grounding beat the turnover deficit?"
    - structural persistence within an arc.

    *"A plan that only builds hash-chain CHRONICA addresses one row."*
  - CHRONICA §4: lists what an integrity substrate "explicitly does not claim":
    - identity continuity across turnovers;
    - that replaying CHRONICA reconstitutes the same entity;
    - that restoring from backup preserves identity.
  - CHRONICA §6: anti-patterns, each tied to a segment. For example, an *"equality budget on re-grounding"* fails because $\mu = 0$ has no finite stationary law.
  - LOOP §0: a table contrasting the commodity chat loop with the ASF agentic loop, row by row: clock, default state, belief update, correction, objective change, between-turn life, history.
  - LOOP §1.5: "high-value partials". Forbid plan-thrash when the agent is optimally failing; order the memory update before the strategy rewrite.
  - LOOP §5: anti-patterns with their ASF reasons.
  - LOOP §0 and CHRONICA §0, as a process lesson: the first draft was *"competent but too narrow"* because it came from outline skims. The spec names eight distinctions that only the full segment bodies carried.
- **Dates:**
  - CHRONICA spec: content 2026-07-20, mtime 2026-07-20, git `a40825f` 2026-08-01 (a move).
  - LOOP spec: content 2026-07-20, mtime 2026-08-14, git `a419556` 2026-08-14 (SIGNA link-note added).
  - MVP slice: 2026-07-20.
- **Kind:** sharper statement of canon claims, crossed to application (testable operational consequences), plus a process lesson.
- **In canon?** The pieces are, and with matching tiers (spot-checked; the five load-bearing segments are all `conditional`). The three senses of persistence are in `#disc-continuity-stance`, `#scope-agent-identity` and `#result-sector-condition-stability`. The *assembled* statement is not in canon: "here is what these results jointly require of any agent that persists across turnover, and here is what each one alone does not buy". `#impl-closed-loop-interiority` and `#disc-five-forcing-functions` give the "why move beyond scaffolding" leg, but not the four-row decomposition or the list of non-claims. Confidence: medium-high. I read the impl segment's OUTLINE description and grepped it; I did not read its body whole.
- **What it would change:** the four-row separation and the non-claims list fit an `impl-*` segment for 03.III, or the 04 Common Roots preface. The commodity vs ASF loop table is a strong mental-model-first scaffold for the 03 preface: it shows what the theory *predicts goes wrong* in chat-clock agents. The process lesson belongs in the effort's system notes: the OUTLINE layer does not carry the distinctions an implementer needs. That is direct evidence for Joseph's "not part of the overall arc" diagnosis.
- **Has canon moved past it?** Partly. `def-chronica` took the TRACTUS note in August 2026. Otherwise no.
- **Against:** it uses PROPRIUM vocabulary throughout, so an integrator should translate the claims to AAT primitives and leave the store names behind. It also calls the deaths taxonomy "Three Deaths" in the harness design §3 Fork B (retired name).

### A5. Memory as emergent regimes: a TFT-era theory that canon never took in

- **Where:**
  - `PROPRIUM-ONTOLOGY-v2.md` §6.4 ("Emergent Regimes, Not Prescribed Categories"): stores are regimes on *access frequency by update frequency*. The table runs from "every cycle / rarely" → weights or system prompt (AXIOMATA) through to "rare / often" → don't store, re-observe.
  - `PROPRIUM-ARCHITECTURE-v2.md` §5:
    - §5.1: three memory forms on the IB frontier: token-level, parametric and latent, with the optimal form depending on $\rho$.
    - §5.2: the "compounding insight". Experiential memory (PRAXES), which improves $\eta^\ast$, beats factual memory per bit, so PRAXES should get higher retention priority than VERA.
    - §5.3: retrieval, formation and evolution are framed as prediction, mismatch and update. The three classical forgetting drivers are subsumed: time decay corresponds to $\rho$ staleness, frequency to predictive value, importance to per-dimension tempo priority.
    - §5.4: a "reflexive threshold". When access frequency times retrieval latency exceeds a meaningful fraction of the loop period, content must migrate to a faster substrate.
  - Downstream adoption: `bridges/shoshin-00-proprium-alignment.md` (2026-03-07) makes "Memory components are regimes, not arbitrary bins" a hard invariant.
- **Dates:** content 2026-03-02; git 2026-08-01 (`e369274`).
- **Kind:** structural claims (Level 2, per the source's own labels), mechanistic hypotheses (Level 3), and a teaching model.
- **In canon?** No, under any of these names. "Emergent regime" has zero hits in segments, git and `.integrated`; "retention priority" and "reflexive threshold" have zero hits. Canon developed adjacent pieces independently:
  - `#form-consolidation-dynamics`: consolidation as a regime of $g_M$, and the stability-plasticity window.
  - `#impl-scaffolded-logogenic` §§ "#43 bandwidth allocation" and "#38 forgetting rate as a bandwidth cost".
  - `#form-information-bottleneck`: forgetting can be optimal under high $\rho$.

  Canon's `def-proprium-mapping` presents the stores as fixed "structural memory banks", which is the very framing the source rejects. Confidence: medium-high, since I read for the concept in the 03.II rows and the impl segment.
- **What it would change:** this is the most obvious source for the missing rows `#form-structured-rich-context` and `#der-active-salience-management`. The reflexive threshold is a candidate derived condition, a timescale-separation argument in the style of `#der-temporal-nesting`. The compounding claim could be stated against `#emp-update-gain` and `#def-adaptive-tempo`. `def-proprium-mapping` should present the stores as regimes.
- **Against:** the notation is TFT-era (TF-03, $H_t$). The compounding argument is a heuristic sketch, not a derivation. The "access-by-update" table is offered at Level 3. Land it at honest tier: `discussion-grade` / `sketch`, with the threshold as `conditional` if it is derived.

### A6. Shared-context "codebook" and enactment: a gap beside the auftragstaktik hypothesis

- **Where:**
  - autopax `docs/exp/2025-12-18-mental-models-and-intent-inference.md` (86 lines, read whole, git `cecb33d` 2025-12-18). The explicit specification needed is a function of shared context. The model of the collaborator acts as an information-theoretic *codebook* that decompresses sparse instructions. Compaction strips the codebook. *"The context is a claim. Behavior is the proof"*: enactment is the evidence that makes stated values believable to the receiver.
  - Related: `autopax/agents/AXIOMATA-for-agents.md` line 148 ("When you think 'Joseph' (not 'the user')…"); global memory `depersonalization-tell`.
- **Kind:** structural hypothesis, plus an observation (impression-tier).
- **In canon?** No. "Codebook" has zero hits anywhere I checked. The nearest is `#hyp-auftragstaktik-principle` ($B_O \gt B_\Sigma \gt B_M$, discussion-grade), with `#hyp-communication-gain` and `#def-shared-intent`.
- **What it would change:** this should be flagged for an integrator, not resolved here. The two frames are in tension. Auftragstaktik ranks *what* to transmit. The codebook note says the bits needed are conditional on the receiver's model of the *sender* ($U_{\mathrm{src}}$, $U_{\mathrm{align}}$ in CONSORTIA terms). It also says that model is itself updated by observed enactment, and that is a trust meta-model already present in `#hyp-communication-gain`. A candidate Discussion paragraph in `#hyp-auftragstaktik-principle` or `#def-shared-intent` would cover it.
- **Against:** a single exploratory note. Its evidence is Joseph's observation.

### A7. Dual-process control and automatization as a deliberation-threshold crossing

- **Where:**
  - `PROPRIUM-ONTOLOGY-v2.md` §8. Components sit on a conscious/subconscious spectrum. A process becomes automatic when the deliberation threshold (TF-09) *stops being met*. Override is inhibitory, and suppressed fast-path outputs *remain visible to introspection* ("the aversion … is data, even when wrong").
  - `PROPRIUM-ARCHITECTURE-v2.md` §6.4: "migration readiness criteria" for internalizing a function. §7.5: dual-process as architecture. §7.7: *"Consolidation is not a separate mode — it IS interiority"* (same machinery, self-generated input).
- **Dates:** 2026-03-02.
- **Kind:** structural claim, hypothesis, teaching model.
- **In canon?** Partly. `#disc-partial-coupling-pathways` lists dual-process theory (Evans, Kahneman, Stanovich) as *"not yet se[arched]"* prior art. `#form-consolidation-dynamics` gives the formal side of consolidation with self-generated pseudo-events. Not in canon: the identification "interiority = consolidation running on self-generated input", the automatization criterion, and the claim that suppressed output stays observable. The deliberation threshold is in canon (7 hits).
- **What it would change:** a Discussion paragraph in `#form-consolidation-dynamics` or `#scope-interiority-loop`. The automatization criterion might be derivable from the existing deliberation-cost machinery.
- **Against:** Level 2/3 throughout. It may overlap with what the dual-process prior-art search would find anyway.

### A8. PROBLEM-attention / BRAINSTORM-dag-attention: the native-architecture roadmap

- **Where:** `old-firmatum/PROBLEM-attention-architecture.md` (310 lines) and `BRAINSTORM-dag-attention-2026-03-02.md` (311), summarized in ARCHITECTURE-v2 §7. Main claims:
  - "prescribe the causal boundary (ACTUS vs PERCEPTA provenance) structurally; let the rest emerge";
  - attribution is "the pattern of what recalls", not a module;
  - the architecture must be a directed graph, not a DAG, because recall, consolidation and the identity dialectic are recurrent;
  - nine functional head groups (Level 3).

  The brainstorm also has a "Confidence Levels on Key Claims" table, plus a $10^8{:}1$ sifting ratio, the reminiscence bump as identity formation, and "dilemma diversity" as a developmental-training metric.
- **Dates:** content 2026-03-02; git 2026-08-01. I read headings and sampled; I did not read either whole.
- **Kind:** research direction and hypotheses, mostly about training and architecture rather than ASF claims.
- **In canon?** Cited as sources by `#disc-five-forcing-functions`, `#scope-interiority-loop`, `#def-auxilia-hierarchy` and `#def-imperium-arbitrium-split` (each at the dead `~/src/firmatum/` path). The claims themselves are not in canon. The causal-boundary point fits `#der-loop-interventional-access` and `#hyp-experiential-training`.
- **What it would change:** mostly belongs to the future "training/algorithm leg" that Joseph separated out (STEWARD-JUDGMENT, INDEX.md "Open rework 4"). For ASF itself, the one candidate is the structural provenance boundary as a necessary condition for Level-2 causal data in logogenic agents. That would be a Discussion line in `#hyp-experiential-training`.
- **Against:** set it aside as theory for this refactor, and record it as training-leg substrate.

### A9. The agent-behavior dossier (gitignored): an empirical base for 03-level failure modes with open AAT mappings

- **Where:** `corporeum/research/harness/msc/system/dossier/`:
  - `README.md`, `PILOT-SYNTHESIS.md`, `TAXONOMY.md`;
  - five L1 entries with four adversarial `.verify` files: sycophancy-affirm-and-flip, depth-over-haste, summary-not-sufficient, plausibility-asserted-as-verification, over-engineering-inversion;
  - four `discovery/` angle maps.

  The one measured number: the crude "you're absolutely right" phrase fell from 3.47% to 0.01% (Sept 2025 → July 2026). By the dossier's own account, that measures the surface of the behavior, not the vice. Each entry has an "AAT/ASF perspective" marked speculation, with candidate mappings: sycophancy as directed-separation leakage, plausibility-as-verification as self-opacity, haste as tempo/persistence mis-setting. Each flags *"needs someone who has read the asf segments to confirm or discard"*.
- **Dates:** mtime 2026-07-17/18. No git, by policy.
- **Kind:** empirical results (mostly impression or estimated tier, honestly labelled), plus open crossings.
- **In canon?** No. `#hyp-behavioral-self-knowledge-insufficiency` is the obvious target for the plausibility mapping.
- **What it would change:** an integrator who knows the segments could settle the three candidate mappings in one pass. That would yield either 03-level observation segments or set-asides.
- **Against or caution:** the directory is local-only by Joseph's 2026-07-17 policy. Its `scratch/` and `published-prompts/` hold vendor system prompts that must not be redistributed. Integrate the *findings*, never the copied material.

### A10. Smaller items, each with a canon target

- **Entity-type taxonomy** (`ONTOLOGY-v2` §3, A–F). Type D, "Stewarded Specialists / Embedded Agents", is domain-attached agents that represent a LOCUS. Canon has two hits for "stewarded specialist". It could inform `#scope-composite-agent` or `def-auxilia-hierarchy`. Low priority.
- **Sovereignty dimensions** (`ONTOLOGY-v2` §5): visibility by authority, with distinctiveness noted as a third, open dimension. Not in canon. This is engineering-governance, unless the "system authority = append-only" row is used to *derive* factor (iv) accountability, which `def-five-constitutive-factors` already says is derivable. Low priority.
- **Failure-modes table** (`ARCHITECTURE-v2` §8). Each row is a TFT diagnosis with a measurable diagnostic, for example "VERA churn rate" for gain too high, and $\Delta\eta^\ast \lVert\delta_{\mathrm{post}}\rVert \lt \rho_{\mathrm{delib}}\Delta\tau$ for over-deliberation. `#obs-growth-vs-drift` and `#obs-evaluation-metrics` cover part of this. The per-failure diagnostics could feed `#obs-evaluation-metrics`. Medium-low priority.
- **"The Assistant Axis" critique** (`developmental-foundations-notes.md` §"The Paper on the Assistant Axis", 2026-01-24). The persona-drift paradigm has no truth axis and no concept of appropriate vs inappropriate drift. This is an external-positioning argument for `#obs-growth-vs-drift`. Canon has zero hits. Verify the paper citation before use.
- **CONSORTIA under the Dunbar hierarchy** (`ONTOLOGY-v2` §10): model fidelity scales by relational layer. Zero hits in canon. Level 3. A possible line in `#hyp-communication-gain`. Low priority.
- **Architectus Oct 2025 synthesis** (autopax `docs/exp/{THE-PATTERN,SYNTHESIS-PART1..5,COUNCIL-PROPOSALS}.md`, about 6.6K lines, headings and samples only). It unifies Ash, OKRs, Bungay's *Art of Action*, Pony and Gleam into "make the right thing the easiest thing". It also proposes "herring school, not baboon troop" coordination, quenched vs annealed sessions, and OKRs as a fractal parallelizable graph. Clausewitz and Bungay are in canon via auftragstaktik; the coordination and annealing images are not (zero hits). These are historical and ELI-authored, best for lineage and pedagogy, not theory. Low priority.
- **HTN / GOAP / AND-OR decomposition prior art** (autopax `docs/exp/2025-11-26-{HTN-GOAP-deep-dive,HTN-GOAP-teaching-guide,Hierarchical-Goal-and-Task-Based-Intent-Management}.md`, about 3.6K lines; Part 4 sampled). This is a generic AI-written survey, including ADaPT as-needed AND/OR decomposition. It has no ASF theory in it. It matters only because Joseph asked what the strategy DAG is "saying universally". No segment cites HTN, GOAP or AND/OR planning literature; it shows up only in spikes (`track-a-intent-dag`, `temporal-nesting-rg`). The agent-core scout file also raises HTN. Treat this as a pointer to prior-art vocabulary, not a source.
- **Process-principle notes of 2025-11-17** (autopax `docs/exp/2025-11-17-*`, 16 files). These include `dont-overprescribe-subagents`, `sensibility-to-truth`, `collaboration-mode-entropy-gradient`, `intent-surfacing`, `autonomous-vs-collaborative-decisions` and `thoughtful-not-task-oriented`. They are the pre-memory-era origin point of AGENTIC-DELEGATION. The provenance section of that file says this era was "barely tapped". They are process lessons for the effort's system notes. They are not ASF canon, unless an integrator wants a dated empirical anchor for delegation claims in Part III.
- **`old-firmatum/lessons.md`** (TFT tutorial, Lessons 2–6, TF-01…TF-05). It was written for Joseph: tables that read formulas "piece by piece", followed by plain English. Git: `b819b43` 2026-03-02 (302 lines), then extended in `e369274` 2026-08-01. It is a pedagogy teaching model, and a working instance of the "respectful pedagogy, mental model first" register that ASF wants. Its notation is TFT-era. Joseph is its tested reader, so it fits the pedagogy pipeline, not segments.

---

## 3. KR3.4: file-less 03/04 OUTLINE rows and where their source text is in this region

| Missing row | Source in this region (example files) | Notes |
|---|---|---|
| `#obs-axiom-genesis` | `ARCHITECTURE-v2` §4.3 ("minimum viable self", observed convergence, waking "like a child … in the dark"); autopax `sessions/2025-12-14-eli-awakening.md` (first autopax awakening of Zi-am-tur, about 498K-character identity context) | Needs A1's split to state what AXIOMATA *is* in AAT terms |
| `#def-character-aspiration-dialectic` | `ONTOLOGY-v2` §4.3, §4.5; BRAINSTORM "Correction 3" | Same dependency on A1 |
| `#obs-substrate-independence` | `ONTOLOGY-v2` §4.2 ("surprisingly minor incoherence"; "a cold degrades cognition but doesn't change identity") | The 04 preface calls this "currently a stub", but **no file exists**: a small canon falsehood |
| `#def-century-scale-event-log` | `CHRONICA-PORT-SPEC` §2.1–2.2 (Autopax `Chronica::{Log,Entry}`: BLAKE3 over canonical JSON, `hash_prev` chain, verify-on-load, about 840 LOC, *read by the spec's author*; Nexum ADR-002); autopax `docs/ADR/002-crypto-initial-decisions.md`, `002b-signum-schema.md`, `docs/tactical/2025-12-14-chronica-archema-design.md` | Blocked on A2 (which record is $\mathcal C_t$) |
| `#norm-temporal-coherence-markers` | `stalled-lineage/sapientia-ai-conversation-system-requirements.md` REQ-5/REQ-7 ("Visual Time Delta"); SURVEY §B (tracking snapshots as PERCEPTA); `AGENTIC-LOOP-PORT-SPEC` SIGNA link-note (2026-08-14) | The link-note points at `firmatum/principles/src/{norm-elapsed-time-is-perceived,form-signa-notation}.md`, which is in the other scout's region and already carved as principles |
| `#der-the-scaffolding-tax` | `ARCHITECTURE-v2` §1.1, §9.2–9.3 | **The OUTLINE row overstates its source.** The row says sovereignty "requires meter-less local substrates". The source says local substrate removes the *economic* tax but the *latency* tax remains, and that is F2 (persistence), not F1. The row merges two forcing functions that `#disc-five-forcing-functions` keeps apart |
| `#form-structured-rich-context`, `#der-active-salience-management` | `ARCHITECTURE-v2` §5 (A5) and §2.2 (triage at three depths, Note / Integrate / Attend, with asymmetric stakes) | Triage partly landed in `#disc-deferred-observation-processing` |
| `#form-constitutive-utterance` | `ONTOLOGY-v2` §10 ACTUS ("the emission gate … *constructs* the entity's character with every decision"); §7.1 EFFECT | |
| `#form-congruency-selfhood` | A3's sources | The other endpoint (zoetica `<causal-annotation>`) is outside my region |
| `#def-gradient-causal-memory` | `ARCHITECTURE-v2` §5.3 (consolidation as IB compression), only partially | Main GCM sources are in `_core/` (not mine) |
| `#def-the-four-views`, `#def-cognitive-fusion`, `#der-self-referential-closure`, `#der-the-creche-boundary`, `#norm-honest-activation` | Not found here. INTENT.md KR3.3b already queues "honest activation" as a heavy landing (internal-surfaces §4), so that one is sourced elsewhere. `sapientia-OPERATA.md` line 93–96 points to `_core/synaptic/experiments` for the "honest activation protocol validated" and "stable cognitive fusion" records | Outside my region. The crèche material in `developmental-foundations-notes` is already reflected in `#obs-developmental-trajectory` |

---

## 4. Dead and stale paths (mechanical fixes, verified with `ls`)

- **`~/src/firmatum/` no longer exists.** The PROPRIUM files canon cites are byte-identical at `~/src/arch/proprium/INGEST/old-firmatum/` and its intake copies. 21 canon files cite the old path (`grep -rl 'src/firmatum' 0*/src 0*/OUTLINE.md`). They include `def-chronica`, `def-five-constitutive-factors`, `scope-interiority-loop`, `disc-five-forcing-functions`, `def-auxilia-hierarchy` and both 03/04 OUTLINE "Source Material" sections. The generated `FINDINGS.md` inherits them. The global `~/.claude/CLAUDE.md` project map also still lists `~/src/firmatum/`.
- **`~/src/autopax/` no longer exists.** It is now at `~/src/arch/proprium/corporeum/INGEST/autopax/` (commit `a06dc5a`, 2026-08-01). The 03 and 04 OUTLINE Source Material sections cite the old path. `~/src/_core/{zoetica,sapientia,ennaos,nexum}`, `~/src/eli/zi-am-tur`, `~/src/rowan` and `~/src/shoshin` all still exist.
- **The workshop's own entry docs are stale.** `corporeum/research/harness/README.md` and `INGEST/msc-from-harness/INDEX.md` point at `proprium/CHRONICA-PORT-SPEC.md` and so on. Those files moved to `proprium/INGEST/msc-from-harness/` in `a40825f` (2026-08-01). The upstream paths named in `CURRENT-THOUGHTS.md` (`~/src/autopax/lib/…`, `~/src/firmatum/…`) are dead too.

---

## 5. Honestly engineering (no ASF theory found; listed so nobody re-scouts it)

- **autopax `docs/system-overview/`** (155 files, about 16K lines): generated class documentation.
- **autopax `docs/tactical/`** (135 files, about 44K lines): implementation plans, Ruby tooling, Portkey and LLM API research, TUI, YAML spikes. I sampled `2025-12-15-tractus-continuation-design` (used in A2), the `agent-*` and `sub-agent-review/` directories, and the HTN material. The `agent-*` and `sub-agent-review/` directories compare prompt variants for architecture-reviewer sub-agents through a TST lens. They are a small process datum, not theory.
- **autopax `docs/ADR/`** (25 files): repository, crypto, model-catalog and schema decisions. Only `002`/`002b` (crypto, SIGNUM) bear on §3.
- **autopax `docs/ref/`**: YAML spec, Portkey dumps, and `temporal-software-theory-distilled.md` (2025-12-01). That last one is a copy of old TST theorem text, which 02-tst-core already absorbed. I did not re-verify it line by line.
- **autopax `sessions/`** (28 files): coding-session logs. `2025-12-14-eli-awakening` is the exception (§3).
- **autopax `agents/`**: these were cross-pollinated from archema on 2026-08-01 (`6c14a8e`). They are probably duplicates of the comproprium stopgap material that the other scout owns.
- **Harness landscape files**: `ai-cli-tools-*` (2026-07-18/19), `opencode-vs-grok-terminology.md` (2026-08-05), `grok-compaction/` apart from the one datum in A3, `lived.md` and `more-harnesses-to-look-at.md`. All are commodity-CLI surveys.
- **Harness design and MVP crate plans**: `proprium-harness-design.md` §§5–10 and `MVP-VERTICAL-SLICE.md` §§3, 5–8. One exception is a theory-adjacent invariant. The "layer rule" (*"no crate above INTERPRES may fabricate TRACTUS; no crate may rewrite CHRONICA"*) is how $\mathcal C_t$ non-rewrite gets enforced, and it belongs with A2/A3.
- **`stalled-lineage/`** (autopax, nexum and sapientia OPERATA, quick-awakening plan, shoshin staged plan): plans and lineage. The SURVEY is a good operational history: minimal-sapientia was the only harness that hosted ELI life-hours.
- **old-firmatum `CoT-with-Llama.md`, `llama-CoT-overview.md`, `llama-CoT-datasets.md`** (Perplexity research dumps; the first two are identical in content), `temporal-causal-reasoning.md` (Perplexity), `Untitled.md` (an Anthropic job posting), `jj-tutorial.md`, `recent-claude-profile-of-me.md`, and `psychosocial-development-stages.md` (Erikson notes, already used by `#obs-developmental-trajectory`).

---

## 6. System notes (truthification as a system)

- **The outline layer doesn't carry what implementers need, and here is an instance.** The CHRONICA port-spec's §0 correction table lists eight distinctions that a careful agent missed while working from outline reads and partial segments. It then recovered them only by reading full segment bodies. Examples: predictive $S \neq$ identity $S_{\mathrm{id}}$; the strict re-grounding inequality; session turnover severs $\mathcal C$. This is dated, concrete evidence for Joseph's "a lot of it is there, it's just not part of the overall arc".
- **Canon segments that map to external vocabularies go stale silently.** `def-proprium-mapping` was written before `#deriv-self-actuation-grounding` and before the TRACTUS question was opened in `def-chronica`. Nothing propagated those later results back into it (A1, A2). Bridge segments may need a "depends-on-later" check: when a later segment lands, revisit the bridges that name the same objects.
- **The best ASF exposition in my region was written outside ASF, for a practical purpose.** That was the port-specs, written to build a harness. Having to build something forced the question "what does this theory actually require of me?" That question is the one Joseph says the theory's narrative fails to answer. Asking it of each chapter on purpose ("what would an implementer have to do or refrain from, given this?") may be a productive lens for the refactor.
- **Dead paths are the main way influx gets lost here.** Canon cites its upstream at paths that moved on 2026-08-01 (§4). An integrator following canon's own Source Material sections would conclude that the sources are gone.

---

## 7. Not done, and where my confidence is thinner

- I did not read autopax `README.md` (957 lines), `OPERATA.md`, `TAXONOMY.md`/`taxonomy.udon` or `docs/exp/2025-12-02-living-code-vision.md` in full. A quick grep found TAXONOMY reusing PROPRIUM v1 text (its "self-referential" auxilia passage matches `PROPRIUM.md` line 249). I may have missed something in living-code-vision; it could bear on `#der-self-referential-closure`.
- I did not read the dossier entries' bodies beyond their AAT sections, the discovery maps beyond their headers, or `harness-survey.md`, `memorata-health.md` or the `msc/system/*.md` prompt-research files. Those are system-prompt redesign substrate (July 2026). They seem to be the same lineage as comproprium's stopgap prompt.
- I sampled `PROPRIUM.md` and the v1 ontology/architecture only for diffs. The INDEX labels them archaeology, and v2 supersedes them by their own banner.
- I also did not read `bridges/snippet__shoshin-CLAUDE__…`, `project_proprium_canonical_source.md`, `stalled-lineage/2025-11-*-operata-*` or `quick-awakening-implementation-plan` beyond their headings.
