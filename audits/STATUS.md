# Audit routing status — live tracker

The evergreen home for *where each audit currently stands* in the routing pipeline. This is the "routing tracker" the process doc refers to — the live rendezvous that replaces the one-cycle `audit-backlog-triage-2026-05-15.md` spine (now archived at [`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md)).

**How this relates to the other audit-tree files** (each is evergreen; this one is the *index of live state*):

- [`README.md`](README.md) — orientation: what the tree holds, the gold-dir gate, the AAD→AAT read-as note.
- [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md) — the *process*: strengthen-first, the no-go protocol, the disposition enum, the gates. **Read it before routing.**
- [`.integrated/MANIFEST.md`](.integrated/MANIFEST.md) — the *graduated* trail: per-file justification for every audit whose findings all have a verified disposition and which has been `git mv`'d into `.integrated/`. Append-only.
- [`polish-and-sentiment-ledger.md`](polish-and-sentiment-ledger.md) — the durable home for soft/sentiment/considered-declined/research-seed findings (the `S`/`P` rows).
- `pending-findings-*.md` — per-cycle resolution trails for the 2026-04 intake clusters.

**Gold-lift sweep (live queue, migrated from the drained root NEXT-UP.md 2026-07-15):** waves 1–4 swept (122 gold-bearing AAT segments); **wave 5 (A18–A21) + TST / logogenic / logozoetic remain**, then the held batched/paired-note reconciliation and the OUTLINE C-iv idiom-drift fix. Durable plan + per-wave progress + deferral state + the open batch-file/taxonomy sub-decisions: [`.gem-hunt-trail/gold-lift-sweep-2026-05-30.md`](.gem-hunt-trail/gold-lift-sweep-2026-05-30.md). The gold-dir gate itself is decision `gold-dir-standing-gate` in [`../msc/decision-briefs-2026-07-15.md`](../msc/decision-briefs-2026-07-15.md).

**The rule this file serves** (from the routing instructions): an audit is *routed* when every finding has a home; it *graduates* (moves to `.integrated/`, gets a MANIFEST entry) only when every finding has a **verified** disposition closed *in the right direction*, and — for de-novo audits — only after the gold-dir gate is settled with Joseph. "Routed" and "graduated" are distinct states; this tracker shows which an audit is in.

## Open / in-flight

Audits whose disposition is not yet fully closed. Each row names what *remains* open and where the rest was routed.

| Audit | Date | Auditor | State | What remains open |
|---|---|---|---|---|
| `audit-731548-FINAL-2026-07-02` | 2026-07-02 | Claude Fable 5 (de-novo: AAT Part I main chain + 9 impl-* + 6-agent verification round) | **routed (2026-07-03); Tier-1 + mood executed** | Executed portion (B-1 / B-2 + detection-signature companion / B-4 / mood MG-discharge) — CHANGELOG 2026-07-03. Open: **B-3** → PROPOSALS **SP-30** (awaits Joseph — root definition + constitutive atoms); **flag for Joseph:** the $\rho_\star$ INDEX row's 2026-05-21 closure he ratified reopened one notch under B-2 (reopened-and-re-closed — needs his eyes). Remaining routed items (TODO §2026-07-03): impl status-tagging pass (6 of 9 AAT segments landed 2026-08-22 — CHANGELOG; first gold lift from `AUDIT-WORKING-731548/26–35` → `.integrated/`); legacy quantifier sweep; chronica absorb-into-$\phi$ staged promotion; nominal-coupling→query-only-coupling rename (naming process); floor-routing segment; shadow-catalogue appendix; SOP additions (Gate-2 instantiate-check, gold-deferral); INDEX FULLY-RESOLVED spot-check. Gold lift for the 36 reflections not started; gold dir `AUDIT-WORKING-731548/` under the standing gate. Does not graduate until the routed remainder closes and the gold dir settles with Joseph. |
| `audit-773921-FINAL-2026-05-28` | 2026-05-28 | Gemini 2.5 Pro | **routed, not graduated** | Findings all closed or routed (F1/F4 via SP-24/SP-25 — CHANGELOG 2026-05-28; F2 → TODO intro-rename; F3 already-tracked; seeds/sentiment → ledger S31–S33 + P-block). **Only blocker to graduation: the gold dir `AUDIT-WORKING-773921/`** — the gate was resolved for lifted material 2026-08-22 (routing.sop); its files move to `.integrated/` per-file as each is lifted (`34-deriv-matrix-persistence-condition.md` moved 2026-08-22), and the audit graduates when the dir is empty. |
| `audit-384279-FINAL-2026-05-27` | 2026-05-27 | Claude Opus 4.7 | **resolved, not graduated** | Structural findings landed (CHANGELOG 2026-05-28); three residual spike proposals live in `spikes/PROPOSED.md`. Remaining: graduate to `.integrated/` once the residual proposals are dispositioned, and settle the gold dir `AUDIT-WORKING-384279/`. |
| `audit-451729-FINAL-2026-05-10` | 2026-05-10 | — | **open** | Single residual D.1 (first-class in `TODO.md` §2026-05-10). Soft items → ledger S25/S28. Does not graduate until D.1 closes. (Per MANIFEST.) |

## Gem-hunt pass (2026-05-29) — live state

The whole de-novo audit-findings backlog (twelve audits across two waves — five never-mined + seven partially-mined) has had a verify-against-canon-first gem-hunt pass; everything surfaced was routed (math fixes landed `f8d9151`; SP-26/27/28/29 → PROPOSALS; research-seeds → ledger S34–S41; actionables → TODO; methodology → ledger P-block). Full outcome narrative: CHANGELOG 2026-05-29 + the committed trails `.gem-hunt-trail/GEM-WORKING-<id>/`. **These audits do not graduate to `.integrated/` yet:** the de-novo `AUDIT-WORKING-<id>/` gold dirs remain under the standing consult-Joseph gate, and the FINAL files' full burden-of-proof rows were not exhaustively re-verified (the gem-hunt targeted gem-bearing sections + dispositioned-away findings, not every §B row — 526815's ~200 F-rows explicitly flagged stale-until-re-grepped).

## Historical backlog (graduated or trail-tracked elsewhere)

The 2026-03 / 2026-04 audit intake and the standalone-audit backlog were dispositioned during the 2026-05-15/16 cleanup cycle. Their per-finding records live in the durable trails, not here:

- **Graduated** files + their dispositions: [`.integrated/MANIFEST.md`](.integrated/MANIFEST.md).
- **2026-04-21/22/23/25 cluster intakes** (471203 / 584721 / 613842 / 742613 / …): the `pending-findings-2026-04-2{1,2,3,5}.md` resolution ledgers.
- **The cleanup cycle's own working spine** (state machine, evidence hierarchy, per-file partition, agent briefs, the Model-S strengthen-first worked example): archived at [`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md). Its evergreen process content was lifted into `../doc/audit-routing-instructions.md`; the file itself is now reasoning-trail archaeology.

The top-level `audit-findings-*.md` files not named above are de-novo cluster outputs from that backlog; consult the MANIFEST / pending-findings ledgers for their disposition before treating any as un-routed. Status of a file not yet verified against current `src/` is *unknown-until-checked*, not *open* — do not infer either from this table's silence.

---

*Append a row when an audit lands; move it from "open" to a MANIFEST entry when it graduates. Keep this file honest about the difference between "routed" and "graduated", and never record a status you have not verified — an unverified affirmation here is the exact failure the routing instructions' independent-verify gate exists to catch.*
