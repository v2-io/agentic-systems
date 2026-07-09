# Findings — cluster 07: decision-routing and Joseph-blockers

*2026-07-07. Discovery-agent findings for the meta-process review. Census of every "genuinely-Joseph" decision open in the repo, an efficacy audit of `JOSEPH-TODO.md` as the intended escape-valve, and a mechanism-design sketch for routing a Joseph-decision to him in a form he can act on without reloading a session. Verified firsthand against current trackers, spikes, and git history; tracking-file claims are marked "doc says" where I did not re-verify the underlying truth. Register: peer report, overturn freely.*

---

## 0. The one-line headline

`JOSEPH-TODO.md` was built 2026-06-02 to be the single escape-valve for Joseph-gated decisions, and **it had already leaked by the time of this review**: its last content-meaningful edit is 2026-06-05, and **zero of the six major Joseph-forks minted in early July 2026 reached it** (verified: `grep` for `SP-30`, `C1`..`C5`, `gold`, `731548`, `era-artifact`, `epistemic-target`, `convergence` in `JOSEPH-TODO.md` returns nothing). The valve is a *manually-mirrored, pointer-only index*, and both properties are the failure: manual-mirror means it dries up the moment an agent forgets the mirror step, and pointer-only means that even when it catches an item, Joseph still has to chase the pointer into a home tracker and reconstruct the context himself. The context a decision needs is almost always *reconstructible but un-assembled* — scattered across a spike dir, a PROPOSALS block, an audit table cell, and the finishing agent's scrollback. The fix is a **decision-brief artifact** (which the repo already produces well, ad hoc — `spikes/epistemic-target-ontology/` is the existence proof) wired into cycle-close.

---

## 1. Census of genuine Joseph-blockers (live surface, 2026-07-07)

I classify each by: (D) the decision, (why) why it is genuinely Joseph's, (context) reconstructible / assembled / lost, (routed?) whether it currently reaches `JOSEPH-TODO.md`.

### 1a. In `JOSEPH-TODO.md` today (what the valve currently holds)

| id | decision | context state | in valve |
|---|---|---|---|
| **D-2** | bulk-64 `.integrated/` wipe: discharge the integration debt vs. consciously set it down; plus semantics (`rm`+commit vs history-purge), timing, scope (`INTEGRATION-CLEANUP-TODO.md` §D-2, three coupled questions). | **Assembled** — `INTEGRATION-CLEANUP-TODO.md` F3/D-2 is thorough and self-contained. | yes (sole "needs your decision" entry) |
| `#schema-strategy-persistence` hard-ceiling | take adjudication verdict B as settled (name the convention, keep `status: exact`). | Assembled (`TODO.md` line 39 + spike `aedc72d`). | yes, under "lead will default" |
| SP-27 / SP-29 | Part-I↔Part-IV bridge placement; infrastructure-as-active-monitor meta-segment. | Reconstructible (`PROPOSALS.md`). | yes, under "lead will default" — **but see §2b: `PROPOSALS.md` still marks SP-27 "awaiting Joseph's Part-IV-bridge placement call," a live inconsistency.** |
| Greek-vocabulary prose discipline | tighten segment prose vs soften the README claim, per term. | Reconstructible (`TODO.md`). | yes, under "lead will default" |

### 1b. Genuine Joseph-blockers NOT in the valve (the leak — the actual finding)

Each of these carries a "needs Joseph / awaiting Joseph / Joseph's call" marker in its *home* tracker but was never mirrored into `JOSEPH-TODO.md`. Ordered by leverage.

1. **SP-30 — the root-ontology call: what *is* $\Omega_t$?** (`PROPOSALS.md:560`; decision package at `spikes/epistemic-target-ontology/`, five files, 2026-07-04). The repair reshaped from "ratify the totality reading of $\Omega$" to the deeper **typed epistemic target $S_t = (\Omega_t, \theta)$** with law-content $\theta$ as a named slot. The gating claim is *verified* (`01-ga1-verification.md`: unknown observation-law breaks the decomposition; GA-1 under unspecified housing is indeterminate — the observationally-equivalent-twin two-horn no-go). **Status: "needs Joseph — root definition + constitutive atoms; the decision package is assembled in the spike folder."** This is the freshest, highest-leverage, best-packaged open decision in the repo — one missing definition currently "paid for across $\ge 4$ segments" — and it is *not in the valve*. It is also where audit-731548's **B-3** finding was routed (`audits/STATUS.md`). Context: **fully assembled** (the exemplar).
2. **era-artifact C1–C5 routing** (`msc/era-artifact-asf-contributions-2026-07-04.md`; flagged in `TODO.md:19` as "Routing decisions for Joseph"). Five routed contributions with named attachment points, none landed: C1 congruency construction (now empirically grounded via the Oct-8-2025 collapse-and-restoration case study); C2 tool-interface-as-AAT-surface + **the "law stratum" candidate term** (mutate-state / reveal-state / teach-law — needs the naming cycle before canonicalizing); C3 ephemeral/persistent channel duality; C4 idle-trigger interiority; **C5 intelligence-empathy convergence** — the boldest claim in the corpus, hypothesis-grade by the project's own lights, in direct contest with Bostrom's orthogonality thesis, carrying an empirical-historical HHH-seeding companion (Joseph testimony, 2026-07-04). Context: **reconstructible but long** (the doc is a wall — precisely the raw material a brief must distill). Not in the valve.
3. **The standing gold-dir gate — 22 `AUDIT-WORKING-*/` directories** (verified: `ls -d audits/AUDIT-WORKING-*/` returns 22). `audits/README.md` sets a *standing, non-optional* gate: before any processing / `.integrated/` move / deletion of an `AUDIT-WORKING-*` dir (de-novo first-encounter "gold"), **consult Joseph and decide with him**. This blocks *graduation* of at least 12 gem-mined audits (`audits/STATUS.md`: "routed, not graduated … only blocker to graduation: the gold dir"). It is a *batched* Joseph-decision standing open for months, with no single "here is the batch + a default recommendation" brief. Not in the valve. **This is the largest single reservoir of Joseph-blocked state in the repo and it is completely invisible to the escape-valve.**
4. **audit-731548 B-2 reopening flag** (`audits/STATUS.md:21`, verbatim: *"flag for Joseph: the 2026-05-21 closure he ratified reopened one notch"* — the $\rho_\star$ three-term-decomposition INDEX row). A decision Joseph *previously ratified* has been reopened by a later audit. This is exactly the kind of item that must reach him (a prior ratification is now in question), and it is buried in a table cell. Not in the valve.
5. **Naming: separability-triad three rung-names** (`TODO.md:231`) — `separable core / structured repair / general open` vs the Hintikka echo `definable core / identifiable region / non-identifiable frontier` vs alternates; "pending Joseph." Plus the `???` rows in `msc/naming/to-canonicalize.md` (`TODO.md:227`, D-deferred citability special cases). Context: reconstructible. Not in the valve.
6. **C-iii composite-without-$O_c$ "fiction"** (`TODO.md:146`) — `scope-composite-agent.md:79` calls a composite without explicit $O_c$ "a fiction"; "two paths under Joseph's call." Recurring (same finding in the 2026-04-22 F8 and 2026-04-25 F-V3 batches). Not in the valve.
7. **Modularity-cycle M4 architectural-commitment decision** (`TODO.md:460`) — the genuinely-absent stubs `disc-strategic-self-coupling` / `disc-modularity-state-dynamics` (note: partly landed since per NEXT-UP, verify) are "deferred pending Joseph's §5.1 M4-architectural-commitment decision"; "decide whether they block v0.1.0 publication surface." Not in the valve.
8. **Framework-scope call on the attention-pair** (`TODO.md:528`, `:547`) — `spike-attention-causal-graphs` + `spike-attention-governance`: "needs Joseph's judgment on framework-scope" (zombie-archive vs keep as exploratory). Not in the valve.
9. **Infrastructure drift calls** — figure-artifact staleness gate design (`TODO.md:258`, "the tension that needs Joseph's call") and `NOTATION.md` auto-derivation (`TODO.md:257`, Joseph-flagged). Not in the valve.
10. **G5 — CLAUDE.md-as-amplifier structural calls** (`INTEGRATION-CLEANUP-TODO.md` §G5) — "periodic human-visible audit cadence for CLAUDE.md" and "consider deriving/generating portions of CLAUDE.md … architectural question for Joseph." Not in the valve. (Meta-relevant: this is the *class* of decision whose neglect the whole review exists to fix.)
11. **README-v2 J-block reconsiderations** (`TODO.md:116`–`121`) — e.g. **J-5 non-specialist tone calibration** (target-audience floor, gating the Findings "Brief" tier and README §1–4 prose). Authoring-voice; genuinely his. Not in the valve. (Grounded in Alan Walton's first-human read — see out-of-scope §5.)

**Resolved-and-correctly-removed (valve hygiene working as intended):** D-1 (RATIFIED 2026-05-30), D-3 (RESOLVED 2026-05-30 = revise), D-citation/G3 (DONE 2026-06-05), SP-24 / SP-25 / SP-26 / SP-28 (executed — `PROPOSALS.md`). These *did* flow through and out. So the valve is not inert; it processes the items that reach it. The failure is purely at the *intake* seam.

**Count:** ~4 items in the valve, **~11 genuine Joseph-blockers outside it.** The valve is catching well under half of its own scope, and the half it misses is the *newer* half (everything from the 2026-07 audit/era-artifact cycles).

---

## 2. Efficacy audit of `JOSEPH-TODO.md`

### 2a. What it was designed to be (aspirational)

Created 2026-06-02 (commit `1382d64`, *"Add JOSEPH-TODO.md — consolidated queue of Joseph-gated decisions … A single navigator for the open items that need Joseph's decision or taste, gathered from the scattered '(Joseph's call)' markers across NEXT-UP / INTEGRATION-CLEANUP-TODO / PROPOSALS / the SOP design doc. **Pointers, not duplicated context (defer-don't-fork).** Carries a convention for agents: add a one-line entry on hitting a genuinely-Joseph fork, and proceed on the rest."*). Re-cut the same day (`faaf40f`, *"re-cut to genuine Joseph-decisions only"*) to strip decision-*points*-with-sensible-defaults from genuine-only-Joseph forks. The convention is sound: irreversible | publication/authoring-voice | cross-project blast-radius | "did this actually come from Joseph?" → add an entry; else default-and-proceed.

### 2b. Why it fails in practice (de-facto)

Three structural causes, each verified:

- **(i) Manual-mirror intake with no forcing function.** The intake step is "an agent, on hitting a fork, remembers to add a one-line entry." Nothing couples this to cycle-close, commit, or any ritual an agent reliably performs. Empirically it dried up within ~4 weeks: last content edit 2026-06-05; the 2026-07-02/03/04 cycles (audit-731548 routing → SP-30; era-artifact C1–C5; the B-2 reopening) each *did* faithfully route their forks into *home* trackers with "needs Joseph" markers — the agents were disciplined — but the *mirror* into the valve was skipped every time. The discipline that exists (route-to-home-tracker) is not the discipline the valve needs (mirror-to-valve). This is the [[triage-is-the-answer-not-the-action]] pattern: the taxonomy (home-tracker marker) got produced; the routing action (surface it where Joseph will see it) did not.
- **(ii) Pointer-only by design — so it cannot be the thing Joseph acts *from*.** "Pointers, not duplicated context" was a deliberate anti-fork choice (avoid two copies drifting). But it means that even a caught item hands Joseph a pointer into `PROPOSALS.md` / a spike dir, and he must then reconstruct the decision himself. The valve is an *index*, and the pain the review names ("I have no idea what they're talking about") is a *briefing* failure, not an indexing failure. An index cannot solve a briefing failure.
- **(iii) Internal inconsistency with home trackers.** The valve lists SP-27 and SP-29 under "lead will default-and-proceed," but `PROPOSALS.md:522` still marks SP-27 *"Open — awaiting Joseph's Part-IV-bridge placement call"* and `:548` marks SP-29 *"Likely wants Joseph's framing."* When the valve and the home tracker disagree about whether something is Joseph's, an agent reading either one in isolation gets a different answer. The mirror, once stale, is worse than absent because it looks authoritative.

### 2c. The diagnostic that reframes the fix

For every major blocker in §1b I checked whether the context is *lost* or merely *un-assembled*. **It is almost always reconstructible** — D-2, SP-30, the gold gate, B-2, the naming rungs all have their context intact in a home artifact. SP-30 is even *fully assembled* (its spike folder is a decision package). So Joseph's "walls of text / no idea what they're talking about" is not irrecoverable-context; it is **un-assembled context delivered as either a raw pointer or a raw scrollback dump**. That is the single most important finding for the mechanism design: the fix is an assembly step, and assembly is only cheap while the context is hot — i.e. it must happen in the cycle that produces the fork, by the agent who holds it, not deferred to when Joseph asks and the agent is gone.

---

## 3. Emergent patterns from git history

- **The valve's own commit arc is the pattern in miniature.** Eight commits touch `JOSEPH-TODO.md`, all in a 2026-06-02→06-05 burst (creation, same-day re-cut, WN-fork reframe, citation-tracker reconciliation), then *nothing* for a month while the repo kept minting Joseph-forks. A tracker that is created in a flurry and then abandoned to staleness is a recurring shape here (cf. `NEXT-UP.md`'s own header: "Delete once the queue drains" — it has not drained and has not been deleted).
- **Decision packages get *built* well and *routed* poorly — repeatedly.** `spikes/epistemic-target-ontology/` (5 files, 2026-07-04) and the `PROPOSALS.md` SP-schema (thesis / merits / scope / subsumed / interactions / effort / risks / status) are both high-quality decision-assembly artifacts. The framework *can* assemble a decision brief; it does so ad hoc and then leaves it in a spike folder where Joseph will not find it. The capability exists; the standard slot and the routing do not.
- **"Reserved for Joseph" is a live, load-bearing status in `PROPOSALS.md`, tracked with real rigor** — the SP-22 CL-2 "Joseph-reserved Instance-5" thread was carried across ~4 spike-routing cycles (2026-05-17/18) with precise reopen/re-scope notes before closing 2026-05-21. So the *reservation* discipline is strong inside `PROPOSALS.md`; what is missing is the *surfacing* discipline that lifts a reservation out of the 115 KB portfolio doc into something Joseph sees.
- **Ratified decisions reopen.** The B-2 flag (a 2026-05-21 closure Joseph ratified, reopened one notch by audit-731548 on 2026-07-02) shows that "decided" is not terminal — which means the routing mechanism needs a *re-open* path, not just an *open→closed* path. A decided item can become a blocker again.

---

## 4. Stale / broken / abandoned (concrete)

- **`JOSEPH-TODO.md` — stale intake.** Last content edit 2026-06-05; missing all six 2026-07 forks; SP-27/SP-29 mislabeled vs `PROPOSALS.md`. (§2.)
- **`NEXT-UP.md` — overdue for deletion.** Its own header says "Delete once the queue drains"; it still carries D-2/G3/SP-27/SP-29 as "Joseph's calls" (lines 42–45), duplicating the valve and `PROPOSALS.md` with a *third* drifting copy of the same list. Three trackers (`NEXT-UP`, `JOSEPH-TODO`, `PROPOSALS`) each hold a partial, mutually-inconsistent list of Joseph-forks. This is the defer-don't-fork principle violated by accretion.
- **22 `AUDIT-WORKING-*/` gold dirs under a standing gate that has never been convened.** (§1b.3.) Whether this is "abandoned" or "correctly waiting" is itself a Joseph call — but a standing gate on 22 directories that no one has scheduled a decision-session for is de-facto stalled.
- **`INTEGRATION-CLEANUP-TODO.md` §G5 (CLAUDE.md-as-amplifier)** — the two architectural sub-items ("periodic audit cadence for CLAUDE.md," "consider generating CLAUDE.md") are open and unrouted; ironically this is the exact defect-class ("a minor early decision hides unsourced and self-amplifies") that the review was convened to address, and it has been sitting open since 2026-05-19.

---

## 5. Out-of-scope surfacings (passed back deliberately)

- **The gold-dir gate (22 dirs) is a cross-cluster item — cluster 02 (audit-and-spike-lifecycle) owns the graduation mechanics, but the *decision* is a cluster-07 Joseph-blocker.** Flagging both ways: the batched decision needs a single brief (§6), and cluster 02 should weigh in on whether a per-dir or whole-batch disposition is right.
- **C5 (intelligence-empathy convergence) is the corpus's boldest claim and is hypothesis-grade by the project's own lights** (`era-artifact` Addendum 2; the sibling orientation letter and reflection #28 both single it out as "the largest gap between conviction and derivation"). Its *routing* is a cluster-07 Joseph-blocker; its *content* is cluster-01/theory. It contests Bostrom orthogonality directly and needs that named as opposing prior art before it lands. High stakes, currently sitting un-landed in a `msc/` working doc.
- **The "law stratum" candidate term** (mutate-state / reveal-state / teach-law; `era-artifact` C2) needs the naming cycle (cluster 03) *and* is theoretically substantive (it attaches to `#der-loop-interventional-access`'s (C3) gate and gives $M_t$ a two-timescale slow/fast stratification). Routing decision is Joseph's; noting for cluster 03.
- **Alan Walton's first-human review** (`TODO.md:99`) — the CTO of Latitude/AI Dungeon, ~10y collaboration, found the README "extremely academic" and fell out of sustained-attention reading. The verbatim review is *pending as a PR under `msc/`*. This is a high-signal external input gated on Joseph, and its arrival will itself be a routing event. Flag for whoever owns the README-v2 cycle (cluster 05?) and for cluster 08 (msc hygiene — watch for the incoming PR).
- **`SP-30`'s decision package is the template for §6.** Whatever mechanism the synthesis lands on, `spikes/epistemic-target-ontology/` should be studied as the worked example of a good decision brief that already exists.

---

## 6. Mechanism-design sketch (the leverage-on-leverage piece)

**Design goal (Joseph's stated pain):** an agent should be able to hand Joseph a genuinely-his decision as *"here is the fork, here is the context reconstructed assuming you have zero scrollback, here is what I would do and why, and here is what I could not verify"* — a thing he acts on in minutes without reloading a session — instead of a pointer or a wall.

**The good news, restated:** the repo already produces this artifact (SP-30's spike package; the PROPOSALS SP-schema). The mechanism is not a new capability; it is a **standard slot + a routing discipline + an intake forcing function.**

### 6a. The decision-brief artifact (a standard, ~1 page, fixed schema)

Every genuinely-Joseph fork gets a short standalone brief. Proposed schema (deliberately small — the discipline is that *context is carried, not pointed at*):

1. **DECISION** — one sentence, the fork stated as a choice. ("Adopt the typed epistemic target $S_t = (\Omega_t, \theta)$ as the root ontology, or keep state-only $\Omega$ and accept the GA-1 indeterminacy?")
2. **WHY IT'S YOURS** — one of the four valve criteria (irreversible | authoring-voice | cross-project | provenance-check), stated. Forces the agent to justify escalation and filters false escalations.
3. **CONTEXT, RECONSTRUCTED** — 3–5 sentences written *assuming zero scrollback*. This is the load-bearing field and the one the current valve lacks entirely. If it cannot be written in 5 sentences, that itself is signal (either the decision isn't ripe or it needs to be split).
4. **OPTIONS** — A / B / (C), each with its consequence in one line.
5. **RECOMMENDATION + CONFIDENCE** — *mandatory.* An agent that escalates without a recommendation has done half the work; per [[peer-voice]] and [[strengthen-before-soften]], hand Joseph a decision to *ratify or redirect*, not an open question. State confidence honestly.
6. **HONEST UNCERTAINTY** — what the agent could not verify firsthand, what would change the recommendation. (This is where the [[plausibility-vs-verification]] discipline lives — mark inference vs verification.)
7. **REVERSIBILITY + BLAST RADIUS** — is this `rm`+commit-recoverable or irreversible; how many segments/projects move.
8. **POINTERS** — home tracker, spike/reasoning trail, provenance chain. (Pointers are *last* and *supplementary*, never the substance.)

### 6b. `JOSEPH-TODO.md` becomes an index *of briefs*, not of pointers

Each valve entry = one line + a link to its brief file (e.g. `msc/decisions/D-<n>-<slug>.md`). The brief is the thing Joseph acts from; the valve is just the queue. This preserves defer-don't-fork (context lives once, in the brief) while fixing the pointer-only failure (the pointer now resolves to a brief, not to a 115 KB portfolio doc he must search).

### 6c. The intake forcing function (the part that actually fixes the leak)

The valve failed because intake depended on memory. Couple it to something agents already do:

- **Cycle-close ritual (fold into the existing [[triage-is-the-answer-not-the-action]] discipline):** before a cycle commits, any genuinely-Joseph fork it produced gets a brief written *and* linked from the valve — in the same cycle, while context is hot. This is the identical move as "execute the safe-to-execute subset in the same cycle that produces the triage," applied to decision-routing. The SOP already asks agents to verify state changed at cycle-close; add "and every Joseph-fork you produced has a brief."
- **A `bin/` check (parallels `bin/check-links`):** grep the trackers for "needs Joseph / awaiting Joseph / Joseph's call / reserved for Joseph" markers and fail (or warn) if any lacks a corresponding valve entry + brief. This makes the leak a *loud build signal* instead of a silent staleness — the same inversion the figure-drift and NOTATION-drift items (`TODO.md:257`–`258`) propose for their domains. It closes the intake seam mechanically so it cannot depend on memory.

### 6d. Batched and re-opening cases

- **Batched gates (the 22 gold dirs):** one standing brief with the batch + a *default recommendation* (e.g. "graduate all, keep git-recoverable" or a per-dir split), so the "decide with Joseph" session is a *ratify/redirect* of a pre-assembled recommendation, not a from-scratch deliberation over 22 directories. Same principle: hand him a decision, not an open question.
- **Re-opening (the B-2 case):** the brief schema needs a "supersedes / reopens decision X" field, and the valve needs a re-open path — a ratified decision that a later cycle reopens must re-enter the queue with the brief noting *what changed since he last decided*, so he is not re-litigating from zero.

### 6e. Anti-patterns to hold the line against

- **The brief must carry context, not point to it.** The entire failure of the current valve is pointer-only; a brief that degrades back into "see `PROPOSALS.md` §SP-30" has reintroduced the disease.
- **The brief must not become a wall.** 1 page; the reconstructed-context field is 3–5 sentences. The `era-artifact` C1–C5 doc is the cautionary example — rich and correct and *unreadable as a decision surface* because it was written as a working doc, not a brief. Distillation into briefs is the work.
- **The recommendation is mandatory.** "Your call" with no recommendation is the executor-mode abdication the peer-voice principle names; it hands Joseph the deliberation-space when the agent was positioned to narrow it.

### 6f. Honest uncertainty on this sketch

I did not observe a live wall-of-text handoff or read session transcripts; the failure model rests on Joseph's testimony, the verified staleness/pointer-only structure, and the 0-of-6 leak. The mechanism is a design proposal, not a validated intervention — in particular I have not tested whether the `bin/`-check forcing function would produce false-positive noise (agents mark "Joseph's call" loosely; the check might flag defaults-with-flags as escalations). The schema in §6a is a first cut; the synthesis pass should treat it as raw material, and should weigh it against the existing SP-schema in `PROPOSALS.md` (which may already be close enough that the fix is "make the SP-schema the brief standard and route SP entries into the valve as briefs" rather than a new artifact).

---

## 7. Candidate meta-process definitions (raw material for the MECE map)

**MP-07.1 — Joseph-fork detection.** *Trigger:* an agent, mid-cycle, hits a decision matching a valve criterion (irreversible | authoring-voice | cross-project | provenance-check). *Steps:* recognize → mark in home tracker → (currently STOPS here). *Health:* **de-facto healthy at the mark-in-home-tracker step** (agents reliably route to PROPOSALS/TODO/audit with "needs Joseph" markers), **broken at the escalate-to-valve step** (0-of-6 in 2026-07).

**MP-07.2 — Decision-brief assembly.** *Trigger:* a Joseph-fork is detected and is ripe (gating claims verified). *Steps:* reconstruct context zero-scrollback → state options → recommend + confidence → mark uncertainty → link pointers. *Health:* **emergent / aspirational** — happens excellently ad hoc (`spikes/epistemic-target-ontology/`, the SP-schema) but is not a standard, not required, and not routed. This is the process to institutionalize.

**MP-07.3 — Valve intake + hygiene.** *Trigger:* cycle-close, or a periodic sweep. *Steps:* mirror every home-tracker Joseph-marker into the valve as a brief-link; prune resolved; reconcile valve-vs-home-tracker labels. *Health:* **stale/broken** — manual, memory-dependent, last run effectively 2026-06-05; SP-27/29 label drift live.

**MP-07.4 — Batched-gate disposition.** *Trigger:* a standing gate accumulates $N$ items (the 22 gold dirs). *Steps:* assemble one batch brief with a default recommendation → convene one decide-with-Joseph session → ratify/redirect/split. *Health:* **abandoned** — the gate is standing, has never been convened, blocks 12+ audit graduations.

**MP-07.5 — Decision re-open.** *Trigger:* a later cycle reopens a decision Joseph previously ratified (the B-2 case). *Steps:* flag the reopening → brief "what changed since you decided" → re-enter the valve. *Health:* **emergent, undocumented** — the B-2 flag exists (in an `audits/STATUS.md` table cell) but there is no defined re-open route; it will likely be missed.

**MP-07.6 — Reservation discipline (inside PROPOSALS).** *Trigger:* a proposal reaches a fork only Joseph should close. *Steps:* mark "reserved for Joseph," carry the reservation across cycles with reopen/re-scope notes, close on his call. *Health:* **de-facto healthy** — the strongest-running of the six (the SP-22 CL-2 thread is a clean worked example); its only gap is that reservations do not *surface* out of the 115 KB portfolio into anything Joseph sees. MP-07.2/07.3 are precisely the missing surfacing layer on top of this healthy core.
