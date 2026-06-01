# Working-Notes discipline — SOP coherence pass + refresh proposal (2026-05-31)

> [!note]
> **Status: PROPOSAL, pending Joseph's gate.** No governing docs edited — the inventory, options, and sketched wording below are decision-support. Two decisions are reserved for Joseph (§6). This is the *full* artifact behind the condensed developing-discipline note in [`../INTEGRATION-CLEANUP-TODO.md`](../INTEGRATION-CLEANUP-TODO.md) ("Developing discipline — what earns a Working-Note"); that note is the durable carrying-summary, this doc is the inventory + options + wording the executor will work from once gated.

## 0. The sharpened discipline being propagated (Joseph, 2026-05-31)

A Working Note earns its place **only if it assists future work.** Three legitimate kinds: **forward pointers** (open follow-on, gating sub-spikes, unresolved questions), **regression-guards** (a disconfirmed prediction / deliberately-corrected-away form, recorded so it is not re-attempted or re-landed), **dead-end warnings** (an approach found not to work). What does *not* belong, even though Working Notes are not canon: **vanity-changelog** (pure past-work narration — that is CHANGELOG's / `.integrated/`'s job, and the urge is strongest exactly when the fix was a *deletion*, so there is no artifact to point at), and **unneeded spike/artifact references** (which also *pin the spike in place*, blocking its move to `.integrated/`). This **narrows** the integration-is-replacement rule's "history → CHANGELOG **+ Working Notes**" to "history → CHANGELOG / `.integrated/`; the Working Note keeps only the future-work-assisting slice." Provisional further thought (Joseph, hedged): *every segment may assume its thinking-traces live in `{spikes,audits}/.integrated/`, so segments need no per-segment histories* — held provisional because it rests on `.integrated/` integrity, which the un-discharged bulk-64 (D-2) currently undermines.

## 1. The finding — consistent, not forked

The rule has **not forked into contradictory forms.** Every site states the same un-narrowed "history → CHANGELOG + Working Notes." That uniform consistency is the situation: they all consistently state the *over-broad* version, so the sharpening is one clean narrowing applied to a well-propagated rule — *not* a contradiction-cleanup. The lone exception is one **gloss-drift** (`spikes/README.md:25`, "belongs there freely") that has slid toward an open-dumping-ground reading the other docs do not carry.

## 2. Inventory — where the rule lives, and where it drifts

- **`FORMAT.md` (owns "what is a Working Note"):** `:419` §Working Notes — forward-looking in spirit, but does not name the exclusions, and "things to check" reads broad enough to admit backward-narration. **`:425` §Voice and provenance — "Date / commit / spike references belong only in `## Working Notes`" — the canonical over-broad statement (DRIFT).** `:429–432` spike-refs "two narrow forms" — form 2 ("brief landing-context provenance") is the sanctioned backward-narration (DRIFT). `:269–277` Gate-4 Notes-disposition — the *closest existing WN-drain process*, but it only fires at `candidate` stage, so a follow-up in a `draft`/`conditional` segment (the common case) has no defined route (relevant to §5).
- **`CLAUDE.md` (project):** `:158` "Landing a strengthened result" — *"the history … lives only in … `CHANGELOG.md`, the cycle tracking file, and the segment's own Working Notes"* — **the primary drift** (the exact "+ Working Notes" co-equal-home formulation, no future-work qualifier).
- **`doc/audit-routing-instructions.md`:** `:171` ("process history … belongs in CHANGELOG / routing tracker / Working Notes") and `:180` (quotes "history lives only in CHANGELOG/Working-Notes") — DRIFT, same shape. `:404` (§0c echo, "Working Notes state what is open") — aligned.
- **`doc/spike-routing.md`:** `:48/:55` (§0c) aligned; `:110–112` (§2-bis(2) need-vs-mention / spike-archivability) is load-bearing *for* the sharpening (it already establishes that an unneeded pointer trips the archivability test) — not drift.
- **`spikes/README.md:25`:** *"a free working attachment … the only place a spike … breadcrumb belongs, and it belongs there freely"* — **the sharpest gloss-drift** (the "not-canon ⇒ free dumping ground" reading the sharpening rejects).
- **Memories:** `~/.claude/memory/epistemic-discipline/integration-is-replacement.md:81–85` and project `feedback_integration_is_replacement.md:12` — the memory-layer carriers of the un-narrowed rule (DRIFT). `feedback_spike_references_only_in_working_notes.md` — pt-3 ("brief landing-context provenance") is the drift; pt-5 ("reduce-or-remove, do not repoint") is the *aligned mechanism* the sharpening leans on. `feedback_prune_completed_from_trackers.md` — aligned, and supplies the WN-hygiene-pass mechanism ("fold into the touch you're already making").
- **Supporting context:** `bin/build-monograph --public` strips `## Working Notes` entirely (`bin/lib/ingest.rb` → `strip_working_notes`), so WN never reaches the published monograph — supports treating WN as intermediate, but does *not* excuse vanity-narration (it still taxes every agent who reads source, and unneeded refs still pin spikes).

## 3. Options

- **(A) Coherence-edit set** — minimal edits making each of the ~6 sites consistent with the narrowed rule.
- **(B) Single-source refresh** — state the discipline *once* in its proper home (`FORMAT.md` owns "what is a Working Note") and have the others *reference* it, rather than restate it. This is the defer-don't-fork pattern the corpus already uses (`doc/spike-routing.md` defers its shared core to `audit-routing-instructions.md` rather than copying it).

## 4. Recommendation — B, with a thin A-style touch on two docs

Re-editing all six sites (A) reproduces the exact fork-then-drift surface the corpus learned to avoid; option B applies the project's own anti-fork discipline to this rule. Sketched wording:

- **`FORMAT.md` §Working Notes (`:419`) — add the spine:** *A Working Note earns its place only if it assists future work. Three legitimate kinds — forward pointers (open follow-on, gating sub-spikes, unresolved questions); regression-guards (a disconfirmed prediction or deliberately-corrected-away form, recorded so it is not re-attempted/re-landed); dead-end warnings (an approach found not to work). What does not belong, even though Working Notes are not canon: vanity-changelog (pure past-work narration — that is `CHANGELOG.md`'s job) and unneeded spike/artifact references (a breadcrumb no future work needs not only clutters, it pins the spike in place — it trips the spike-archivability test, `doc/spike-routing.md` §2-bis(2)). "Not canon" licenses forward-work content, not backward-narration.*
- **`FORMAT.md` §Voice and provenance (`:425`) + spike-refs form 2 (`:432`) — narrow:** date/commit/spike references belong in the history layer (CHANGELOG / cycle tracking file); a Working Note carries one *only* when it is a forward-pointer, regression-guard, or dead-end warning per §Working Notes — not as standalone provenance.
- **`CLAUDE.md:158` / `audit-routing:171,180` / both memories — replace the trailing "+ Working Notes" with a pointer:** *"… `CHANGELOG.md` and the cycle tracking file. A Working Note carries a line from this history only if that line assists future work (forward-pointer / regression-guard / dead-end warning) — see FORMAT.md §Working Notes; pure history is not WN content."*
- **`spikes/README.md:25` — fix the gloss:** keep "Working Notes are by definition not canon," change "and it belongs there freely" to *"— for forward-work content (per FORMAT.md §Working Notes). Not-canon is not a license for vanity-changelog or unneeded references; an unneeded reference pins the spike (§2-bis(2))."*

Net: ~5 small edits, only **one** (FORMAT) carrying the full statement; the rest become one-line pointers.

## 5. The WN-follow-up drain process (the gap Joseph named)

There is no defined route today from "noted in a WN" to "picked up" (FORMAT's Gate-4 disposition only fires at `candidate` stage). Proposed:

- **Route at write-time, don't just note.** A WN forward-pointer is registered in a real tracker when written (the standing cycle per `doc/spike-routing.md` §0c — TODO / PROPOSALS / PRACTICA / the audit cycle / `spikes/PROPOSED.md`); the WN then holds a *pointer* to that tracked obligation, **never the sole obligation.**
- **Periodic WN-hygiene pass, folded not ceremonial** (per `feedback_prune_completed_from_trackers`): whenever a segment is touched, prune satisfied/landed forward-pointers and demote any backward-narration that crept in. No new standing ceremony — it rides existing tracker-touches.

## 6. The two decisions reserved for Joseph

1. **A vs B** — lead's lean: **B** (single-source).
2. **Scope / blast radius.** The footprint reaches the **global layer** — `~/.claude/memory/.../integration-is-replacement.md` and (to verify) the global `~/.claude/CLAUDE.md` before-action prescription — which is cross-project. And `CLAUDE.md` is the maximal-blast-radius / minimal-oversight surface the routing-trail flagged. So: **single-source refresh project-only for now, or extend to the global layer too?**

On the call, the lead drafts the actual edits (and, if the provisional per-segment-history thought is to be acted on, couples it to the D-2 `.integrated/`-integrity discharge — not before).

---

*Authored 2026-05-31 by the SOP coherence pass (agent a48ba87f) + lead synthesis. Working proposal; archive to `_obs/` once the gated edits land (or supersede).*
