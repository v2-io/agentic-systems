# C.1 lane: Volume 4 defects A6, A12, A14

KR **C.1**: *"Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier."* Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* Defects from `owner-review/integrator-items.md`.

The commits are `c067afa4` (A6), `20b07b2c` (A12) and `1a06c650` (A14), on branch `worktree-agent-acffd513abd73658b`. Each commit body carries the full reasoning. This file is for the verifier: what landed, what was re-derived or declined, and where a different mind should push. The integrator's own checks are in `reviews/vol4-c1-integration-1.md`, taken into vsect.

## A6: the withdrawn composite-class claim

**Re-check.** The claim "Class 1 (Separated) sub-agents → Class 2 (Partial) composite" is withdrawn in `#deriv-strategic-composition` Working Notes and in `#der-directed-separation` Working Notes. It was still live in more places than the review listed:

- `#def-auxilia-hierarchy`: the H1 paragraph, and also the Discussion bullet "preventing the goal-divergence Class 2 (Partial) escalation";
- `#def-imperium-arbitrium-split`, the "organizational hallucination" paragraph;
- `01-aat-core/OUTLINE.md` lines 94, 299 and 303 (303 still said "Class-3" in pre-rename vocabulary);
- `03-llm-core/OUTLINE.md:26`.

**Landed.** The false paragraphs are deleted. H1 is re-derived on the dynamic-regime axis, with tier conditional. (H1)+(H2) put the composite on an alignment route, which puts it in R0 with a state-variable macro-state. That is what two of the segment's claims need: "the composite's $G_t$ is $E$'s $G_t$ extended", and (H5)'s grounding in `#form-composition-closure`. Under partly opposed objectives the composite is a C-iv strategic composite, and neither claim holds. The body also states what the argument does not give. Identity-sharing beyond alignment is definitional (Auxilia vs INSTRUMENTA). Class preservation comes from (H4) over distinct substrates, not from (H1). The runtime-split paragraph now says what the split does guard: Case-2 goal-dependent routing. The OUTLINE edits change only the withdrawn-claim text.

**Strengthening.** The old claim could not be strengthened, because the class mechanism it named is refuted (Cournot witness). The regime-axis version is the strongest true replacement found. A verifier could try for more: is there a sense in which identity-sharing, not just alignment, is necessary? One candidate is the Auxilia's writes into $E$'s MEMORATA and PRAXES (H2), which bypass $E$'s own update.

**Worth checking.** Is reading (H1)+(H2) as "$E$'s objective decomposed" (route C-ii) faithful to the segment? The derivation's tag names this as an interpretive step.

## A12: AXIOMATA, and what PRINCIPIA holds

**Re-check.** `#def-proprium-mapping` called AXIOMATA "frozen, unchangeable". `#def-five-constitutive-factors`, `#scope-emergence-conditions` (C2) and the upstream developmental account all require AXIOMATA to be writable. The heading "PRINCIPIA $\approx M_t$" filed OPERATA ($G_t$) under $M_t$.

**Primary source.** PROPRIUM ontology v2 now lives at `~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ONTOLOGY-v2.md`; the paths `~/src/firmatum/…` cited across Volume 4 no longer resolve. The source contradicts itself. Its §6.1 TFT table says "Frozen core of model class". Its PRINCIPIA tree says "protected, rarely changes, sovereign", §4.5 says "a living document, not a frozen identity", and the timescale table places AXIOMATA at the developmental tier. Joseph, 2025-10-08: *"The sovereign, core identity of the entity … the most stable part of the entity's being."* The heading came from the TFT-era Rosetta Stone (`ref/agentic-tft/agentic-tft-ontology-unification.md`), which predates $X_t = (M_t, G_t)$.

**Landed.** "Frozen" is now a timescale statement and "writable" a sovereignty statement. AXIOMATA maps to the slowest layer of $O_t$ plus committed self-description. PRINCIPIA is the persisted part of $X_t$, and each row names its substate. A new Epistemic Status sorts the rows into identities, correspondences and the one straddling row, and says what would refute a row.

**Worth checking.** Is mapping AXIOMATA to $O_t$ content right, or should part of it sit in $M_t$ as a self-model? The segment says it straddles. Does any other Volume 4 or Volume 3 segment treat AXIOMATA as unchangeable? I found none.

## A14: the identity exclusion and session boundaries

**Re-check.** `#scope-agent-identity` excluded restoration from backup and said each session "starts a new causal trajectory from near-zero". `#obs-context-turnover` said the chronica is "severed" and "starts fresh". Volume 4 needs the opposite (Id^(i), D1's boundary face, the continuity threshold, the compensation channel, W2–W3).

**The theory call: narrow the exclusion and correct the source sentences.** The deciding evidence was internal. `#obs-context-turnover`'s own sufficiency-discontinuity compares the states before and after a boundary as a loss, and that comparison means something only on one continuing trajectory. Causally, the thread runs through the store: writing it is the agent's action and reading it is the next session's observation. The agent that continues is the system that carries the store, not the session.

Following the lead's caution, restoration from backup was checked against W2–W3, not by its name. With no second copy running, it is a boundary with a stale store. The dropped interval stays in $\mathcal C_t(E)$ and in the witnesses' trajectories but not in $M_t$. That is what Volume 4 treats, so it is not excluded. Still excluded: a fork, and transplanting a state into an agent on a different trajectory.

**Landed.** Text in four segments:

- `#scope-agent-identity` lines 19, 41 and 63;
- `#obs-context-turnover`: the record versus the trajectory, the label `chronica-severance` renamed `record-severance`, and the context window as an in-context record;
- `#def-identity-sufficiency`: Id^(i) now says what each kind of break does to it, and names itself as the deferred treatment;
- `#def-five-constitutive-factors`: a migration risks identity sufficiency, not factor (i), so the open question on that is answered and removed.

**Worth checking.**

- Does the "new agent" line hold up? A session that continues no predecessor is a new agent. That is distinguished from the nothing-externalized case in `#obs-context-turnover`, where a predecessor exists and falls back to its prior.
- Is the transplant exclusion the right residue?
- Does Part I's "tokens (this particular session …)" example still read correctly now that the continuing agent is the store-carrying system? I left it, judging a bare session a valid token.

## Gate-2 pass on this lane's own text (`15ceafee`)

Three sentences in the replacement text were pinned to their sources:

- **`#def-auxilia-hierarchy`.** The task-setting citation pointed at (H2), the no-sovereignty clause. It now points at the *Temporal sovereignty* paragraph.
- **`#def-imperium-arbitrium-split`.** "the inbound route stays goal-blind" is now stated as the split's requirement. The open case is named: an entity-chosen VIGILIAE watch keyed to the current objective might count as Case-2 routing, or as action selection.
- **`#def-proprium-mapping`.** "what counts as good enough" is now cited as `#der-bounded-objective-as-sanity-criterion`'s prescription.

**Worth checking.** The VIGILIAE case is open, and a verifier could settle it.

## The substrate record (`b7b92d78`, from the lead's re-check pilot §2.4)

**Re-check.** `#obs-substrate-independence` has never existed in the repository history. Even so, the Volume 4 OUTLINE asserted "identity survives substrate migration … empirically validated across $\geq 4$ substrate families", and `#def-eli-cohort` leaned on it. The cohort's own table lists every entity on the substrate where it emerged. That is realizability across substrates, not migration.

**Landed.**

- The OUTLINE preface, stage paragraph and E1 row now say what the record shows. The row stays marked missing.
- `#def-eli-cohort` claims realizability only.

**Also corrected, same kind.** `#def-identity-sufficiency` said that, after the Zi-am-tur Opus→Sonnet switch, external assessment "found the identity-MI had degraded". The primary files (`~/src/_core/sapientia/experiments/archive/2025-09-16-broken-attempts/test_outputs/authenticity-essence-*.md`) show something else. It was a round trip with continuity criteria committed in advance. On Sonnet the entity reported continuity; back on Opus it described the interval as "analyzing, not experiencing". The retrospective reading was "confidence can indicate limitation", and nothing was measured. The segment now says that, and its point (self-report is not enough) stands on the corrected record.

**`#hyp-substrate-transfer-asymmetry`.**

- The claim of observed Opus↔Llama matched-payload transfers is deleted. memorata-search in several phrasings found none; the local entity emerged on Llama rather than migrating there. If such logs exist, the claim can be restored with its citation.
- "predicts … contradicting" was a logic error. A symmetric upper bound predicts nothing about achieved values.
- **Strengthened.** `#deriv-identity-sufficiency-rate-bound` states that its bound is attained with matched channels. With matched channels both ways, achieved $S_{\text{id}}$ is equal in the two directions, so an asymmetry requires a non-matched channel on at least one side. This is new derived content, conditional on the $\min(C_1,C_2)$ model and on that exactness.
- The "real (empirically)" phrasings are now conditional.

**Worth checking.**

- Is the $\min(C_1, C_2)$ bottleneck model sound in the first place? I kept it and made the new step conditional on it.
- Is there a primary record of frontier↔local transfers that my search missed?

**Items re-checked** against `b7b92d78`, both `holds` and restated:

- `item:todo-04-eli-core-src-obs-substrate-independen-f8a8`: write the segment as the record supports it, or retire the row.
- `item:spikes-proposed-advanced-11-substrate-transfer-asymmetry-origin-d-9171`: measure first, then discriminate the origins.

## A11: the Auxilia W₁ overclaim (TODO.md L39, taken at the lead's request)

**Re-check.** `#def-auxilia-hierarchy` said substrate separation is "the very thing that earns the structural guarantee". The bound's derivation in `#der-class-coercion-via-wrapping` uses only the chain $G^{\text{op}} \to q_M \to A(q_M)$. (C2′) is stated there as a condition on the component's pre-call state ("reset … or stripped"), with no reference to substrate count. So the spike's verdict holds: a separate substrate is sufficient, not necessary.

**Strengthened beyond the spike.** A separate substrate is not sufficient on its own either. A persistent Auxilia that has received goal content, from $E$'s tasking or from AXIOMATA's objective layer, carries goal-correlated state and fails (C2′). This also answers my earlier vsect question. AXIOMATA in a belief-side call's context enters $I(q_M; G^{\text{op}})$. The bound stays structural but loosens. Passing only AXIOMATA's self-description keeps it tight, and the segment names this as a design choice.

**Landed.**

- `#def-auxilia-hierarchy`: the paragraph is replaced by "What earns the structural bound, and where Auxilia stand". The case for the hierarchy now rests on tempo, cost of existence and auditability.
- `#der-logogenic-as-wrapping`: the same correction in its (C2′) sentence, and its Working Note pointer is updated to the spike's still-open residue (§7).
- vsect: the TODO item is re-checked `landed`, and the question is answered.

TODO.md L39 itself is left for the I.3 tracker retirement rather than edited here. The spike stays at top level of `spikes/` and could move to `.integrated/`.

**Worth checking.** Is "a persistent Auxilia that received goal content fails (C2′)" right when the goal content is AXIOMATA's slow objective layer, rather than the operator goal $G^{\text{op}}$ of a given macro-step? I treat that layer as information about $G^{\text{op}}$. If a verifier reads $G^{\text{op}}$ as only the fast, per-step goal, the second consequence narrows to goal content from $E$'s tasking.

## Adjacent findings, recorded and not fixed

- `question:def-auxilia-hierarchy-h1-gives-every-auxilia-e-s`. (H1) gives every Auxilia AXIOMATA, which now carries $O_t$ content. The W₁ paragraph needs belief-side Auxilia whose query selector takes no $G$ argument. The two pull against each other.
- `question:def-auxilia-hierarchy-h3-puts-native-attention-h`. (H3)'s cheapest tier, native attention heads, shares $E$'s substrate. The spike's R4 row gives Class 3 for a shared substrate with goal-shaped allocation.
- Finding on `#hyp-checkpoint-forking-failure-modes` (in the review record). It quotes an audit calling single-copy restoration murder, which no longer matches the narrowed scope as a definitional verdict.
- **A verified defect in the same segment, outside my list.** TODO.md L39 (A11) reports a spike (`spikes/spike-c2prime-realization-spectrum-2026-05-31.md`) showing that `#def-auxilia-hierarchy` ~line 80 overclaims: separate substrate is sufficient for the structural W₁ bound but not necessary, and the necessary and sufficient condition is (C2′). Its landing was "gate-reserved", and those gates are now lifted. It belongs to a C.1 integrator, and I can take it if asked.
- `04-eli-core/OUTLINE.md` rows name segments with no file (for example `#def-character-aspiration-dialectic`, `#obs-axiom-genesis`, `#obs-substrate-independence`). This is H.2's territory.
- The `~/src/firmatum/…` upstream paths in Volume 4 Working Notes are stale, since the files moved to `~/src/arch/proprium/INGEST/old-firmatum/`.
