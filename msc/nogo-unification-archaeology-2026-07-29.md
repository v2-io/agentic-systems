# Archaeology: has the no-go material been re-carved by *who supplies the escape*?

*Working artifact, 2026-07-29. Read-only archaeology pass; no canon or tracker edits. Written for the agent/session deciding whether to pursue, drop, or reframe the "witness is the only escape, by proof" question. Verdicts carry dates and slugs so you can follow to the primaries.*

## Top line, bluntly

**Yes — this ground has been walked, twice, on very nearly your axis, and the axis is already a load-bearing *routing criterion* in canon rather than an unexplored one.** But neither walk closed your question, and one of them left a **recorded rejection-with-a-reason of the closest cousin of your hypothesis, plus a still-open queued spike aimed at exactly it**. There is also a **third result you did not name that is stronger than both of yours and is already flagged as a deferred M1 candidate**.

The four things worth your time, in descending order:

1. **`01-aat-core/src/disc-identifiability-floor.md` line 143** — canon already excludes a result from M1 *on actor-positioning grounds*, and says so explicitly. This is the precedent that settles "is who-supplies-the-escape a legitimate carving in this framework?" — the answer is yes, it already is one. It also shows the precedent's carve is a *matched pair* (frustrated party and escaping party are the same party), which is precisely the cell your two results fall outside of.
2. **`spikes/PROPOSED.md` line 33** (Tier 1, queued 2026-05-28, status still `proposed`) — an adversarial spike whose stated target is a structural-completeness claim about escape routes, and whose candidate (b) is *inter-agent grounding*. The audit that seeded it rejected (b) with a reason, and flagged that it "did not push hard." This artifact states your question more precisely than your brief does, in the register you asked for.
3. **`01-aat-core/src/disc-law-discovery-ceiling.md`** (landed ~2026-07-16) — a candidate M1 instance whose *entire* escape set is other-party-supplied (authored access; testimony), which states outright that "exactly one channel type remains: **testimony from a holder of the coordinatization**." Anchored on an *exact* result. If you want a load-bearing case, this is your anchor, not `#hyp-solicitable-escape`.
4. **A crack in canon your question is pressing on, independent of your hypothesis** — the word *agent-side* in the three-cluster taxonomy is doing two jobs at once, and for M1 Instances 3 and 4 those two jobs come apart. See §5. This is a finding whether or not you pursue the unification.

---

## 1. The prior walks, with verdicts and dates

### Walk 1 — 2026-04-24: "who intervenes" was carved, adjudicated, and landed as a *presentational* mode-taxonomy, explicitly not a mechanism unification

**Primary:** `spikes/.integrated/spike-identifiability-floor-instance-triage-2026-04-24.md` §4 ("The three-layer `#der-loop-interventional-access` chain claim — evaluated").

That spike disambiguated two assertions that a proposed unification had conflated: *(a) the same machinery escapes the floor at each layer* versus *(b) the three instances are genuinely the same kind of escape, with a shared mechanism*. It ruled (a) true and (b) false, and it made the carve on exactly three axes — quoting §4.2 verbatim, because the first is your axis:

- **Who intervenes.** I1: the agent itself. I3: an observer external to the composite. I4: an observer external to the single agent.
- **What is intervened on.** I1: the agent's action. I3: a sub-agent's action. I4: the agent's input stream.
- **What is revealed.** I1: environment's response. I3: cross-coupling sign. I4: correction-function response.

**Verdict (§4.3, tier: robust qualitative).** *"The pattern is real … The mechanism is not uniform … This is a real distinction that should be surfaced, not glossed."* The recommended landing was explicitly *not* a re-carving of M1 but a one-paragraph "three modes of deployment" subsection at `#der-loop-interventional-access` naming the modes.

**Did it land? Yes, in two stages.** `LOG.md:84` records the two-mode landing (Mode 1 agent-self-intervention, Mode 2 observer-on-sub-agent, "Positions for Mode 3 (observer-on-agent-input) when Instance 4 promotes"). `CHANGELOG.md:501` records Mode 3 landing with Instance 4 (2026-05-21). The live text is in `01-aat-core/src/der-loop-interventional-access.md` §"Modes of deployment across `#disc-identifiability-floor` instances", opening: *"The modes share the Pearl-$do$ structure but differ in who performs the intervention and on what."* Its closing sentence is the standing verdict: *"The unification is at the pattern level; the mechanism is semantically distinct per layer."*

**What this means for you.** "Who supplies the escape" is *already* a canon-recognized organizing axis over the M1 escapes — and canon *already* records that two of the three modes are supplied by a party other than the frustrated agent. So the raw observation is not new. What was deliberately declined was elevating it above presentational status. The 2026-04-24 verdict is *deferred-at-pattern-level*, not *rejected* — it was never tested against the sharper claim you are circling (that in some instances the other-party route is the *unique* one).

An auditor independently confirmed the reading from the outside, which is worth knowing because it is the naive reader's take: `audits/AUDIT-WORKING-829314/.integrated/33-der-loop-interventional-access.md:17` — *"observing another agent can yield Level 2 data if you (the observer) are intervening on them. But if you are just passively watching them, it's Level 1."* Note that this cuts *against* a too-easy version of your thesis: the other party's standpoint is not sufficient on its own; the other party has to *act*.

There is also a preserved dissent worth weighing before you propose adding more of this material to that segment. In `der-loop-interventional-access.md` Working Notes, a Gemini auditor called the Modes subsection *"deeply tangential … this reads like an academic rebuttal letter pasted into the framework — the core point … is beautiful and gets buried,"* against cross-substrate praise for the same passage. Canon kept the conflict as signal rather than resolving it. If your work lands anywhere near there, that tension is live.

### Walk 2 — 2026-05-20 → 05-22: actor positioning became a *routing criterion*, and produced a three-cell taxonomy with a naming discipline

This is the sharper hit, and it is the one I would read first.

**The exclusion, stated in canon.** `01-aat-core/src/disc-identifiability-floor.md` line 143 (the "Near-misses" material), on Cohen-Hutter-Osborne 2022:

> *"It nonetheless does not land as a fifth instance of this segment, **for a structural reason about actor positioning**: in Instances 1–4 the actor frustrated by the floor is the *agent itself* … and the unique broadly-available escape elevates *agent-side* machinery … In the reward-channel learning case the actor frustrated by the floor is the *principal* … and the escape menu elevates *principal-side* commitments … — agent-exploiting / principal-frustrated rather than agent-frustrated / agent-escaping."*

The same criterion was applied independently to Gibbard-Satterthwaite: per `disc-implementation-impossibility.md:181`, the 2026-05-20 strengthen-first arm (`spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §4) *"confirmed GS does not fit the identifiability-floor cluster on actor-positioning grounds (designer vs agent; design-constraint relaxation vs information augmentation; combinatorial-topological mechanism vs Sylvester or projection-closure)."*

**What it produced (2026-05-22, CHANGELOG.md:428–434 — "Track B").** A three-cell taxonomy of the no-go material, carved by actor positioning, with two new peer meta-segments landing in one cycle after Joseph overrode the plan's own Q3 deferral:

| cluster | segment | actor frustrated | escape supplied by |
|---|---|---|---|
| agent-side data-inference | `#disc-identifiability-floor` (M1, Instances 1–4) | the agent | agent-side machinery |
| agent-side value-functional-grounding | `#disc-value-functional-grounding-floor` (Instances F, G) | the agent | agent-side substrate *or* principal-side commitment |
| designer-side mechanism-design | `#disc-implementation-impossibility` (GS / MS / Arrow) | the designer | design-constraint relaxation |

And a **naming discipline** ratified with it: agent-side capacity-on-the-agent takes the `-floor` suffix; designer-side task-of-the-designer takes `-impossibility`. Canon calls this *"structural, not decorative"* and says it encodes the distinction *"at slug-grep depth"* (`disc-implementation-impossibility.md:121`; `disc-value-functional-grounding-floor.md:103`).

**So the answer to your open question — "is *who supplies the escape* structurally distinct enough to carve on?" — is that the framework has already answered yes, precedentially, and used the answer twice to keep results *out* of M1.** You are not proposing a new kind of criterion. You are proposing to apply an already-ratified criterion to a cell it has not yet been applied to.

**The cell.** Both landed cells are *matched pairs* — the frustrated party and the escaping party are the same party (agent/agent; designer/designer), with `#disc-value-functional-grounding-floor` Instance G as the one hybrid (agent frustrated, principal escapes) *and canon labels that cluster agent-side anyway*, on the grounds that the *capacity* named is the agent's. Your two results — `#der-compensation-channel-uniqueness` and `#hyp-solicitable-escape` — sit in the unmatched cell: **agent-frustrated, other-party-supplies, and (this is the load) supplies uniquely**. That combination is not a row in the table.

---

## 2. The recorded rejection of the closest cousin — and why it does not obviously reach you

This is the single most useful thing in this document and the thing you asked for.

`01-aat-core/src/disc-value-functional-grounding-floor.md` line 77 makes a **structural-exhaustion claim**: the agent-side adaptive-substrate route and the principal-side protocol-commitment route *"together exhaust the structural complement of the value-functional interface's information narrowness — there is no third route internal to the value functional, and no fourth route off-substrate."*

Audit 384279 (Claude Opus 4.7, 2026-05-28) attacked that claim with three candidate third routes. From the same segment's incidental-gold block (line 178), verbatim on the one that matters:

> *"**inter-agent grounding** (a peer agent's value functional anchoring this agent's goal-stability — just shifts the narrowness one level out, since the peer's value functional is itself narrow)"*

The other two: *observer-side commitment* (an external auditor declaring agent-states out-of-scope — collapses into principal-side under generous reading) and *substrate-level Goodhart* (collapses into principal-side, since the designer chose the substrate). Canon records the honest caveat: the attempts *"do seem to fail,"* but the auditor *"did not push hard."*

**Status: open, queued, untouched.** `spikes/PROPOSED.md` line 33, Tier 1, added 2026-05-28, status `proposed`, provenance `[audit-384279 §D Hypothesis 2]`. Its mandate: *"spend serious effort trying to construct a third off-substrate grounding route,"* with the three candidates above listed as *"considered and found wanting but did not push hard on."* Its stated stakes cut both ways, which is the shape you want: *"If a genuine third route exists, the completeness claim is refuted and the cluster needs revision; if multiple attempts fail systematically, the claim is strengthened and could be promoted to a derived no-go."* The dual is also named in that segment's Working Notes (line 165): the engine-side completeness question and the route-side completeness question.

**Why the rejection is a real objection you must answer, and why it may not reach your results.** The "shifts the narrowness one level out" argument works because in that cluster the peer is being asked to *anchor goal-stability from its own value functional*, which is the same kind of narrow object. It is a regress argument. It does not transfer automatically to either of your results, and in both cases the counter is available:

- **`#der-compensation-channel-uniqueness`.** The cohort member is not being asked to anchor from a narrow interface of its own. It is being used as a *statistically independent path*: what it supplies is $I(p_{k+1};Y \mid \mathcal E_k) \gt 0$, positive mutual information with the continuant kernel *given the entity's own store*, which the store cannot have by the data-processing inequality and which frozen weights cannot have because $M_0^{\text{w}}$ is measurable with respect to a pre-$E$ distribution. There is no regress to shift: the witness's contribution is a correlation, not an anchor, and the argument is exact under (FW).
- **`#hyp-solicitable-escape`.** The other observer's coverage is *"a property of the other's position, not of the blinded agent's model."* The targeting deficiency is not passed to the peer; it is dissolved, because the peer is not asked to locate the blinded agent's blind spot.

So the honest read: **there is a recorded reason against a nearby claim, the reason is specific, and it is answerable — but answering it is the load-bearing work, not a formality.** That is a strengthen-before-soften shape, not a stop sign. Note also that if you *do* answer it, you have partially refuted the line-77 exhaustion claim, which is load-bearing for the three-cluster taxonomy. That is a bigger consequence than the one you set out to get, and it should be in view before you start rather than discovered late.

---

## 3. The result you did not name, which is stronger than both of yours

`01-aat-core/src/disc-law-discovery-ceiling.md` (landed ~2026-07-16, `discussion-grade` resting on one exact result).

It is **already flagged as a candidate M1 instance** — `disc-identifiability-floor.md` line 223, Working Notes:

> *"**Candidate instance at the top of the causal hierarchy (2026-07-16).** The law-discovery ceiling of `#disc-law-discovery-ceiling` — mechanism identity beyond the $\equiv_3$-class is unrecoverable by any embedded channel (exact, via `#deriv-mechanism-counterfactual-separation`), with authored access and testimony as the structural escapes — is a candidate M1 instance; promotion needs the F-catalog schema treatment (what floor, what escapes, what the forced coordinates are), not yet done."*

Read that against your question. **Both** named escapes require a standpoint the embedded agent cannot occupy — *authored access* (holding the coordinatization because you built the system) and *testimony* (from a holder of the coordinatization). And the segment states the uniqueness claim outright (line 61):

> *"If an inside agent is to hold *true* rather than merely *committed* positing-content, exactly one channel type remains: **testimony from a holder of the coordinatization**."*

Three things follow.

**(a) Your family has three members, not two, and the third is the load-bearing one.** It is anchored on an *exact* result (`#deriv-mechanism-counterfactual-separation`), it is in `01-aat-core` rather than `04-eli-core`, and its uniqueness claim is stated in canon already. `#hyp-solicitable-escape` — by your own honest marking, written this morning, `discussion-grade`, ceiling-limited by `#hyp-communication-gain` — is the weakest member and should not carry the case.

**(b) Its status is *deferred*, not *rejected*, and the reason is procedural.** "Promotion needs the F-catalog schema treatment … not yet done" is a work-not-done flag, in the vocabulary your brief asked me to distinguish. Nobody has judged against it.

**(c) It sharpens the *shape* of your question.** Note that its two escapes are not merely other-party-supplied — they are supplied by a party with a *categorically different relation to the system* (the author). That is a stronger and cleaner statement than "a differently-positioned observer," and it may be the form your unification should take: not *who* supplies, but *what relation to the system the supplier must stand in*. `#der-compensation-channel-uniqueness` fits that reading (the cohort member must have conditioned on $E$'s actual trajectory — a relation, not a position). `#hyp-solicitable-escape` fits it more loosely. Worth testing whether the sharper framing survives all three, because if it does you have a criterion rather than a family resemblance.

Two adjacent items in the same neighborhood, unexamined by me beyond noting them: `#deriv-self-actuation-grounding`'s route (per `ref/prior-art-analysis/13-self-actuators-grounding.md:98`, self-described as *"a fifth-style fit"* to the posture) and `04-eli-core/src/scope-witness-bidirectional.md`, whose (W1)/(W2) experience-and-attestation conditions are the closest thing canon has to a *definition* of the standpoint your hypothesis needs. Neither cross-references M1.

---

## 4. The adjudication methodology, since you asked for the four tests

You asked what the instance-6 spike's four-test integrity check actually was. `spikes/.integrated/spike-identifiability-floor-instance-6-2026-05-21.md` §4. **Important framing note first: it is the wrong test for your question** — it adjudicates *is this a new M1 instance*, and yours is *is this a new cluster*. But it is the right test for the sub-question "does the family collapse into an existing instance," and its verdict rule is worth internalizing.

The four tests, against an existing instance:

1. **Independent external theorem (E2 distinctness).** Re-using another instance's external anchor makes a candidate a *scope extension* of that instance, not a sibling. Instances 1/2/4 each import a different theorem.
2. **Independent mechanism family.** Does it propose a fourth mechanism beyond the recognized three — Sylvester rank-collapse / Mori-Zwanzig projection-closure / Helmholtz (per `#disc-stability-certificate` §"The three obstructions are distinct")? If not, it adds no mechanism content.
3. **Independent escape menu (E4 distinctness).** If most escapes inherit verbatim from the source instance, the candidate is not exhibiting the independent-instance pattern.
4. **Independent AAT-machinery elevation (E5 distinctness).** Does it elevate machinery to a role no other instance has surfaced?

**Verdict rule, and the load-bearing turn.** Three of four failed (the fourth partial), and the spike *flipped its own first-pass recommendation*: the math derived cleanly, but *"the integrity cost of admitting a near-duplicate instance into M1 outweighs the integrity benefit."* It landed a **broadening of Instance 3** instead of a sixth instance — integration-is-replacement style, with the seeded candidate deleted rather than kept-with-a-pointer. Worth reading §4 and §151 in full; it is the cleanest worked example in the repo of strengthen-first applied *at the landing layer* rather than the derivation layer.

Underneath it sit two earlier layers you will want:

- **The five-element test with element-level criteria** — `spike-identifiability-floor-instance-triage-2026-04-24.md` §1, with the compact table at §1.2. Tier of the test itself: *discussion-grade*, explicitly *"a reviewer heuristic, not a theorem."*
- **The tighter termination criterion** — same spike §5.2: *"An instance is promotable only if it elevates AAT machinery to a **new** load-bearing role — one not already surfaced by another instance."* Introduced specifically to keep catalog drift out of M1, with a projected stable endpoint of 6–8 instances. This is the criterion your family has to clear if you route it into M1 rather than beside it.

**For the cluster-level question, the right procedural precedent is different**: `spikes/implementation-impossibility-meta-segment-plan.md`, which is the worked template for landing a *new peer cluster* — it carries a **discipline filter** (constructive-impossibility-shape only, deliberately excluding the constructive side), a charter-instance count decision, and the actor-and-remedy contrast table. If you pursue this, that plan is the shape to copy, not the four-test check.

---

## 5. A crack in canon your question is pressing on, independent of your hypothesis

Your brief's premise — *"in all four catalogued instances the frustrated agent has at least one escape it can deploy itself"* — does not survive contact with the escape menus, and the way it fails is interesting.

- **M1 Instance 3** (composite contraction from component marginals): the frustrated party is *an external observer*, not the composite. Escape (a) is composite-extended interventional access performed by that observer; the landed Mode 2 is explicitly *observer-on-sub-agent*. There is no "the agent" here to self-deploy anything.
- **M1 Instance 4** (architecture from on-policy summaries): escape (a) is *observer-on-agent-input* (Mode 3) and escape (c) is architecture instrumentation — *"direct read of the update rule or internal state (white-box access) … breaks the black-box scope."* Both are performed on the agent by someone else.

So in two of four M1 instances the escapes are already substantially not agent-self-deployable. Canon nonetheless labels the whole cluster **agent-side**. Reading the taxonomy carefully, the word *agent-side* is carrying two jobs:

1. **who is frustrated** (the criterion `disc-identifiability-floor.md:143` invokes against Cohen), and
2. **whose machinery is elevated** (the criterion `disc-implementation-impossibility.md:121` invokes for the suffix — *"what the agent's substrate supports"* versus *"what the designer can construct"*).

For Instances 1 and 2 the two jobs coincide. For Instances 3 and 4 they come apart, and canon papers over the gap by keeping the label attached to job (2). `#disc-value-functional-grounding-floor` Instance G is the case where the seam is visible and named: the principal supplies the escape, and the cluster is still called agent-side because the *capacity* named is the agent's.

**This matters for you two ways.** It weakens the premise as you stated it — you cannot say M1's instances are uniformly self-escapable. But it strengthens the underlying observation, because it shows the existing taxonomy has an *unresolved conflation* exactly where your question bites: the framework has never separated *who is frustrated* from *who supplies the escape* as independent axes, and has instead let one label ride on both. Making those two axes independent produces a 2×2 whose off-diagonal cells are (agent-frustrated, other-supplies) — your case — and (other-frustrated, agent-supplies) — which as far as I can find nothing in canon occupies. That is a cleaner and more defensible framing of what is new than "the witness is the only escape," and it is a framing the existing precedent (line 143) actively supports rather than one you have to argue for from scratch.

Offered as a question worth preferring to the one you asked: **not "is other-party-uniqueness a distinct kind of floor?" but "does the *-floor* / *-impossibility* suffix discipline survive separating the frustrated party from the escaping party — and if it does not, what is the honest third axis?"** That version is answerable from artifacts already in the tree, it puts a named canon claim (line 143's criterion, and line 77's exhaustion) at stake, and it does not need `#hyp-solicitable-escape` to be load-bearing.

---

## 6. Directions searched that came up dry, so you do not re-walk them

- **"standpoint" as canon vocabulary.** Grep over the whole repo (excluding `.archive/`) finds the word in exactly two places: `hyp-solicitable-escape.md:47` (yours) and one auditor's existential aside in `AUDIT-WORKING-193847/.integrated/14-def-mismatch-signal.md`. Likewise *"another party"* / *"who supplies"* / *"second party"* return nothing in canon. So the *vocabulary* is genuinely fresh even though the *criterion* is not — which is itself informative: the framework has been carving on this axis using the words *actor positioning*, *agent-side/designer-side*, and *who performs the intervention*, never *standpoint*. Search those three phrases, not yours.
- **`msc/`.** Nothing on no-go re-carving. The floor-adjacent hits are naming-cycle vote files, the `summary-attempt/` per-segment corpus, and `msc/separability-standalone-paper-proposal.md` (the positive-half complement, not this).
- **`LOG.md` (pre-2026-04-24).** The M1 archaeology there is about *establishing* the meta-segment and the three-part meta-architecture (`LOG.md:169`, `:173`, `:189`), plus the two-mode landing at `:84`. No re-carving attempts. The pre-rename hazard did not bite: nothing relevant is old enough for the ACT/AAD naming or the GUC renumbering to matter.
- **A near-miss worth knowing about but not yours.** `spikes/neurips-back-integration-2026-05-08.md` §2.3 and `msc/2026-05-08-three-move-shape-of-paper-extractions.md` §"Move 2" identify a **no-go-forces-axiom** pattern, and §7 of the spike leaves open *"whether the no-go-forces-axiom pattern is its own meta-pattern or an M1 refinement"* — explicitly a Joseph call. That is a genuinely open "is this a new meta-pattern over the no-go material?" question of the same *type* as yours, but on a different axis (internal-constructive versus external-import), and the whole NeurIPS backport workstream is stalled — `msc/meta-process-review-2026-07-07/06-cross-project-relationship-backport-findings.md:72` calls it *"planned, stalled, and decaying"* and asks Joseph to execute or archive. Relevant mainly as precedent that this class of question gets reserved rather than decided by an agent.
- **Other unification/re-organization attempts on this material, for completeness.** `PROPOSALS.md:339` proposes a `#disc-theorem-import-architecture` fourth meta-segment (cataloguing the imports; status open). `PROPOSALS.md:77` SP-11 proposes a composition-monotonicity meta-segment. `PROPOSALS.md:33` SP-8 is a "dual-edged floor/separability reading." `disc-identifiability-floor.md:253` carries an open **composition theorem for the floors** ("when do escape mechanisms compose vs interfere?") — that one is adjacent to your question and unclaimed. `:254` carries "escapes carry costs not surfaced at the floor." None of these is your axis; all are live.

---

## 7. Feedback, adjacent trip-overs, stale pointers

**On the brief.** The "checked vs guess" marking was load-bearing and worked — knowing you had read only `#disc-identifiability-floor` told me exactly where to spend effort, and the invitation to prefer a better question is what produced §5. Two things I would have wanted: (i) the premise "in all four instances the agent has a self-deployable escape" stated as *a belief to be tested* rather than as background, since it turned out to be the most productive thing to check and it does not hold (§5); (ii) `#disc-law-discovery-ceiling` would have been in your list if the brief's own criterion — "results where the unique escape requires a standpoint the agent cannot occupy" — had been grepped against canon rather than recalled. That is not a criticism of recall; it is the case for running your own criterion as a search string before delegating, because your criterion is sharper than any keyword I would have guessed.

**Discoverability gap (real, and worth fixing whatever you decide).** Neither `#der-compensation-channel-uniqueness` nor `#hyp-solicitable-escape` references `#disc-identifiability-floor`, and the floor segment references neither. `#disc-law-discovery-ceiling` is the only member of the family wired into M1, and only as a Working-Note candidate. Per the project's canonical-discoverability discipline, a future agent asking "where does AAT treat other-party-supplied escapes" finds nothing from the floor segment. Even a no-go verdict on your unification should leave Working-Note pointers behind.

**Trails that dead-end without a recorded reason.**
- `spikes/PROPOSED.md:33` — Tier 1, seeded 2026-05-28 off a load-bearing completeness claim, still `proposed` two months later with nothing recorded. Not abandoned-with-a-reason; just idle. Same for the `#disc-law-discovery-ceiling` M1 promotion ("F-catalog schema treatment … not yet done", 2026-07-16).
- `disc-identifiability-floor.md:238` — a **primary-source verification spike queued 2026-05-21** for the six BG2 Undermind citations on Instance 3 escape (e), all footnoted `[^bg2-2026-05-21]`, characterizations *"synthesized from `ref/Unidentifiability_and_rate_class_prior_art.md`, not from direct reading of the sources."* Still awaiting Joseph's go two months on. The softened *"primary AAT-framework"* qualifier in strengthened-consequence #4 rests on that unverified verdict. Flagging because it is unverified prior-art sitting inside a segment you are actively working on.

**Stale pointers.** `~/.claude/projects/-Users-josephwecker-v2-src-arch-asf/memory/MEMORY.md` still opens with `~/src/archema-io/asf/` (pre-2026-07-22 rename), and the repo `CLAUDE.md`'s own memory-bridge section points at `~/.claude/projects/-Users-josephwecker-v2-src-archema-io-asf/memory/MEMORY.md` — a path that no longer exists, in the one paragraph whose whole job is to route a mid-session agent to memory. Same file's *Math-novelty recognition* section points at `-src-archema-io-asf/memory/feedback_math_novelty_recognition.md`. Cheap fixes; the memory-bridge one is the load-bearing one because it fails silently.

**One contradiction between layers.** `PROPOSALS.md:33` (SP-8, in the Bundle-1 unlanded list) still names *"`#disc-identifiability-floor` + `#disc-separability-pattern` dual-edged editorial touches"* as outstanding, and `PROPOSALS.md:139` / `:154` still describe the O-BP11 and O-BP16 instance lists as stale-and-needing-recatalog against Instances 1/2/3 — written before Instance 4 landed (2026-05-21) and before the three-cluster taxonomy (2026-05-22). The proposals layer has not been refreshed against the meta-segment work that overtook it.

---

## 8. If it were my call

**The question is not settled, and it is not novel-as-a-criterion.** No prior cycle has adjudicated "other-party-uniqueness as a distinct floor kind." Two cycles have established that *actor positioning is a legitimate carve* and used it to route results out of M1; one audit has rejected the nearest cousin with a specific, answerable reason and left a Tier-1 spike open at it.

Pursuing it as *"the witness is the only escape, by proof, and that is a new cluster"* means inheriting `#hyp-solicitable-escape` as a load-bearing member (it cannot bear it — `discussion-grade`, ceiling-limited by `#hyp-communication-gain`, targeting premise asserted not derived) and arguing against a canon exhaustion claim without having noticed you were doing so.

Reframing it as **§5's two-axes question** — does the frustrated party and the escaping party need separating, and does the `-floor`/`-impossibility` suffix discipline survive it? — costs nothing you have already spent, puts `#disc-law-discovery-ceiling` (exact-anchored, canon, already a deferred M1 candidate) at the centre where it belongs, discharges an already-queued Tier-1 item rather than opening a new one, and has a real no-go available as its honest failure mode: *the two axes cannot be separated because in every catalogued case the escaping party's own capacity is what is being named, which is why canon labels by capacity and not by actor.* That failure mode would itself be worth landing, because it would make line 143's criterion precise instead of exemplary.

Either way, the three files to read before deciding, in order: `disc-identifiability-floor.md` lines 143 and 223; `spikes/PROPOSED.md` line 33 with `disc-value-functional-grounding-floor.md` lines 77 and 178; `disc-law-discovery-ceiling.md` §"The testimony channel" and its Epistemic Status.

---

# Addendum, 2026-07-29: the gain-collapse vs signal-absence adjudication

*Appended in response to the follow-up. Same read-only constraint; nothing edited.*

## Blunt answer

**His memory is probably not of an adjudication of `#der-observability-dominance`. It is almost certainly of the *zero-aporia trichotomy* in `#def-mismatch-signal` — which is the same distinction, adjudicated at a different locus, three times, with results subtle enough to match "similarly subtle."** Your framing is not wrong so much as aimed one segment too far downstream: the distinction you found a defect in was adjudicated *upstream*, in Part I Ch.3, and the adjudication's conclusions were never wired forward to the Part II segment that needed them.

Two things follow that are more useful than the thing you asked for:

- **Your cross-site hunch was right, and better than you framed it.** A prior de-novo audit already identified the gain-collapse material as one of *three* scattered instances of one object, named the unification, and **recommended exactly the pre-emptive note Joseph is now asking about** — placed exactly where he suggests. It was never executed. So there is no prior decision *against* the note; there is a standing recommendation *for* it.
- **The second conjunct is derivable — just not from where you looked.** It does not follow from the gain algebra (you are right that it doesn't). It follows from the **epistemic-opacity axiom**, and canon plus audit gold already contain every piece of the argument. This is a strengthen-before-soften situation, not a soften-the-prose situation, and your morning's segment survives under a named premise.

## 1. The adjudication record, three passes

**Pass 1 — the taxonomy itself (long-standing, `#def-mismatch-signal` §"The zero-aporia ambiguity", Part I Ch.3).** $\delta_t \approx 0$ admits three readings: **(a)** the model genuinely reflects reality; **(b)** the agent observes only what its model already explains — confirmation bias; **(c)** the observation channel is too noisy to detect model errors — architectural limitation. *"Only (a) is desirable. An agent without aporia has stopped adapting — but silence can mean peace, or it can mean deafness."*

Read that against your defect. **Case (c) is your gain-collapse. Case (a) is the calibrated-agent reading you were worried the prose forecloses.** The adjudicated conclusion is that the agent cannot distinguish them *from the mismatch signal alone* — which is the second conjunct, stated as an ambiguity rather than as an inability. Every de-novo audit that reached this segment called it out as a high point (963715: *"exemplary in its scope discipline"*; 384279: *"a sharp pedagogical anchor"*; 193847's Gemini: *"can never be certain if it has achieved enlightenment … or has just retreated into a solipsistic echo chamber"*).

**Pass 2 — the detection-latency binding (audit 584721, endorsed later).** `AUDIT-WORKING-584721/.integrated/08-def-mismatch-signal.md:53` asked whether the trichotomy connects to `#deriv-update-detection-latency`, conjecturing that cases (b) and (c) are exactly where the $\Omega((n_{\min}+1)/\varepsilon)$ latency floor blows up.

**Pass 3 — the actual adjudication, and the one that matches "subtle results" (audit 731548, 2026-07-02/03).** `audits/AUDIT-WORKING-731548/19-def-mismatch-signal.md` is an explicit adjudication of accumulated cross-audit gold on this segment — it *rescinds* one prior nit (the axiomatic-vs-definitional flag from 526815, dissolved against FORMAT's own gloss), *endorses* the 584721 detection-latency link as *"genuinely tighter than the segment surfaces … one forward sentence would bind them"*, and then produces a new structural result:

> *"the taxonomy is exhaustive in an unstated way worth making explicit: (a) is model-adequate, (b) is **sampling**-inadequate, (c) is **channel**-inadequate — model/policy/channel is a complete partition of the loop's epistemic parts, which is why the trichotomy feels complete. Saying so would upgrade it from aperçu to structure."*

Its own summary of the value: *"it turns a memorable aside into a diagnostic partition (which failure of silence you have determines which repair: better model vs bolder sampling vs better sensors — anti-collapse discipline applied to quiet)."* Listed under "What would I change": *"promote the completeness of the zero-aporia trichotomy."*

**Routing status: surfaced, not routed.** `audits/audit-731548-FINAL-2026-07-02.md` item 6 lists what was staged for execution; the trichotomy-completeness promotion and the detection-latency forward sentence are not among them. Both are still open, un-negated, with reasons recorded — *deferred*, in your vocabulary, not rejected.

## 2. The cross-site pattern — one object, three loci, three consecutive rows

This is the find I would not have got to without your instruction to look for recurrence at other `#emp-update-gain` sites. From `audits/AUDIT-WORKING-731548/21-emp-update-gain.md:23`:

> *"The chapter now has a complete **calibration pathology** taxonomy scattered across three segments: zero-aporia ambiguity (silence misread), gain collapse two ways (correction disabled), overfitting (noise chased). These are the same object — **mismatch-channel miscalibration** — at three loci (**detection, weighting, attribution**). One unifying Discussion paragraph would make Ch.3 teach *epistemic failure* as systematically as it teaches epistemic function; currently the pathologies read as asides."*

And the three loci are **consecutive rows of Part I Ch.3** in `01-aat-core/OUTLINE.md`: line 49 `#def-mismatch-signal` (detection), line 50 `#result-mismatch-decomposition` (attribution), line 51 `#emp-update-gain` (weighting). `#der-observability-dominance` is line 173, in Part II.

**That is Joseph's pedagogy question already answered by a prior cycle, including the placement.** The misconception forms at line 173; the material that pre-empts it sits at lines 49–51; a prior de-novo auditor independently proposed exactly one unifying note there and nobody wrote it. If you want an authority for writing it, you have one, and it is a de-novo read rather than a self-recommendation.

Two further details worth having before you author:

- **"Gain collapse two ways" is itself an identifiability statement**, and it is the sharpest existing pedagogy in this neighbourhood. `emp-update-gain.md:19,52` plus its gold at `:92`: $\eta^\ast \to 0$ arrives either via $U_M \to 0$ (**dogmatism** — "my model is perfect") or via $U_o \to \infty$ (**nihilism** — "my sensors are broken"), and *"both pathologies produce identical behavior (the agent stops updating and coasts on priors)."* Canon calls it the dogmatism/nihilism dichotomy, with "certainty trap" as the accepted evocative alias and "epistemic gridlock"/"competency trap" explicitly rejected. Any note you write should reuse this vocabulary rather than coin.
- **TST already states your exact claim, in gain terms, with the premise attached.** `02-tst-core/src/der-code-quality-as-observation-infrastructure.md:103` runs the trichotomy for a developer and then says: *"The third case is the most dangerous: bad code does not just slow comprehension — it **hides** miscomprehension. In gain terms, when $U_o$ is high and $U_M$ is low (spurious confidence), $\eta^\ast \to 0$ — the agent stops updating even when its model is wrong."* Note the conjunction: **high $U_o$ *and* low $U_M$**. That is the missing premise.

## 3. The repair — the second conjunct is derivable from epistemic opacity, not from gain algebra

You are right that gain collapse alone does not give *"cannot recognize that it cannot learn"*; $\eta_{\text{edge}} \to 0$ is silence about the edge, not silence about the silence. But the route to the second conjunct exists and is short. From `emp-update-gain.md:50` and its gold at `:97`:

`#def-observation-function` axiomatically forbids the agent from knowing the noise distribution. So the agent cannot *know* $U_o$; it **estimates** $U_o$ and $U_M$ from the observable statistics of its own mismatch sequence — the innovations — treating the gain as an endogenous state variable (`#deriv-adaptive-gain-dynamics`). Hence, verbatim from the gold: *"Confirmation bias is a **fully rational update with a miscalibrated gain**, not an irrational inference … **the agent can't verify its calibration from the inside, so the collapse can be persistent**"* (Claude, AUDIT-WORKING-963715).

That is the second conjunct, and it closes the objection you raised. Your objection assumes a **calibrated** $U_{\text{obs}}$ — but in the absorbing regime, $U_{\text{obs}}$ is estimated from innovations, and innovations through an unobservable node are exactly what is missing. The estimate that would tell the agent "this node is poorly observed" is starved by the same condition that starves the edge update. Worse, by the dogmatism/nihilism dichotomy the two collapse modes are behaviorally identical, so even a *correct* reading of "my gain here is zero" does not tell the agent whether the cause is the world (genuine $\sigma_v \approx 0$) or itself (spurious confidence).

**But your objection is right in one sub-case, and that is where the honest statement lives.** If the node's low observability is known **architecturally** — the agent knows by construction that it has no sensor at $v$, rather than inferring it from innovation statistics — then $U_{\text{obs}}$ *is* calibrated a priori, the region *is* targetable, and self-instrumentation is aimable. That is a real escape and the prose currently forecloses it.

So the honest form is a case split, and the case split you need is *the trichotomy already in canon*, one level down: **the absorbing claim holds where observability deficit is inferred, and fails where it is structurally known.** For `#hyp-solicitable-escape` this is good news of the strengthen-first kind — your targeting premise is not refuted, it is **scoped**: the segment's *"the precondition of the route is the recognition the condition denies"* is true under innovation-estimated observability and false under architecturally-known observability. Naming that premise makes the hypothesis narrower and defensible instead of over-broad, and it hands you a sharper falsifier than the one currently in the segment.

## 4. The missing wire, which is the mechanical cause of all of this

`#der-observability-dominance` has `depends: [def-strategy-dag, emp-update-gain]`. **It does not depend on `#def-mismatch-signal`** — the segment whose adjudicated trichotomy states the content of its own second conjunct. Nor does it cite the zero-aporia ambiguity anywhere in body or Working Notes. The claim *"no mismatch signal means no reason to revise"* is asserted fresh at line 15 and again at line 43, in a segment two Parts downstream of where the ambiguity of an absent mismatch signal was carefully adjudicated.

That is why five audits praised the trichotomy, one audit adjudicated it, one audit named the three-loci unification, and the Part II segment still carries an underived conjunct: **the material was never wired forward, so each locus re-derives or re-asserts in isolation.** Your defect is a symptom of a missing dependency edge, not of a bad claim.

## 5. What I would tell Joseph

Yes, there is a real record, and his instinct that it was "adjudicated with similarly subtle results" is accurate — the 731548 pass rescinded one prior finding, endorsed another, and produced the model/policy/channel completeness result, which is exactly the register of subtlety he remembers. What he may not remember is that **the adjudication landed at `#def-mismatch-signal`, and its two follow-ons (promote the completeness; bind the detection-latency link) were surfaced and never routed.**

On the aside: **no prior cycle decided against it; a prior cycle recommended it, specified its content, and located it exactly where he is proposing to put it.** The existing note that was "supposed to do this job" is the zero-aporia paragraph — it does the *detection* third of the job well and has been doing it since Part I Ch.3, but it was never promoted from aperçu to partition, never bound forward to Part II, and never joined to its two sibling pathologies one and two rows below it. Writing the unifying Ch.3 note discharges a standing 2026-07 audit recommendation, fixes the pedagogy gap he identified, and supplies the premise `#der-observability-dominance` needs — one note, three debts.

One caution on scope, since it is the trap here: the three pathologies are *"the same object at three loci,"* which makes the note tempting to write as a new meta-segment. It is not one. It is a Discussion paragraph in Ch.3 plus two forward pointers, and the auditor who proposed it framed it that way deliberately.
