# Audit routing status — live tracker

The evergreen home for *where each audit currently stands* in the routing pipeline. This is the "routing tracker" the process doc refers to — the live rendezvous that replaces the one-cycle `audit-backlog-triage-2026-05-15.md` spine (now archived at [`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md)).

**How this relates to the other audit-tree files** (each is evergreen; this one is the *index of live state*):

- [`README.md`](README.md) — orientation: what the tree holds, the gold-dir gate, the AAD→AAT read-as note.
- [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md) — the *process*: strengthen-first, the no-go protocol, the disposition enum, the gates. **Read it before routing.**
- [`.integrated/MANIFEST.md`](.integrated/MANIFEST.md) — the *graduated* trail: per-file justification for every audit whose findings all have a verified disposition and which has been `git mv`'d into `.integrated/`. Append-only.
- [`polish-and-sentiment-ledger.md`](polish-and-sentiment-ledger.md) — the durable home for soft/sentiment/considered-declined/research-seed findings (the `S`/`P` rows).
- `pending-findings-*.md` — per-cycle resolution trails for the 2026-04 intake clusters.

**The rule this file serves** (from the routing instructions): an audit is *routed* when every finding has a home; it *graduates* (moves to `.integrated/`, gets a MANIFEST entry) only when every finding has a **verified** disposition closed *in the right direction*, and — for de-novo audits — only after the gold-dir gate is settled with Joseph. "Routed" and "graduated" are distinct states; this tracker shows which an audit is in.

## Open / in-flight

Audits whose disposition is not yet fully closed. Each row names what *remains* open and where the rest was routed.

| Audit | Date | Auditor | State | What remains open |
|---|---|---|---|---|
| `audit-773921-FINAL-2026-05-28` | 2026-05-28 | Gemini 2.5 Pro | **routed, not graduated** | F1 root-ontology decision (→ `PROPOSALS.md` SP-24, awaiting Joseph's Path A/B). F4 → SP-25 (promotion candidate). Seeds/sentiment → ledger S31–S33 + P-block. F2 → TODO (intro-rename item). F3 already-tracked. **Gold dir `AUDIT-WORKING-773921/` untouched** pending the standing gate. |
| `audit-384279-FINAL-2026-05-27` | 2026-05-27 | Claude Opus 4.7 | **resolved, not graduated** | Both structural findings landed in canon (scrbook hierarchy sweep; composition-consistency reframe — CHANGELOG 2026-05-28); three residual spike proposals in `spikes/PROPOSED.md`. Remaining: graduate to `.integrated/` once the residual proposals are dispositioned, and settle the gold dir `AUDIT-WORKING-384279/`. |
| `audit-451729-FINAL-2026-05-10` | 2026-05-10 | — | **open** | Single residual D.1 (first-class in `TODO.md` §2026-05-10). Soft items → ledger S25/S28. Does not graduate until D.1 closes. (Per MANIFEST.) |

## Historical backlog (graduated or trail-tracked elsewhere)

The 2026-03 / 2026-04 audit intake and the standalone-audit backlog were dispositioned during the 2026-05-15/16 cleanup cycle. Their per-finding records live in the durable trails, not here:

- **Graduated** files + their dispositions: [`.integrated/MANIFEST.md`](.integrated/MANIFEST.md).
- **2026-04-21/22/23/25 cluster intakes** (471203 / 584721 / 613842 / 742613 / …): the `pending-findings-2026-04-2{1,2,3,5}.md` resolution ledgers.
- **The cleanup cycle's own working spine** (state machine, evidence hierarchy, per-file partition, agent briefs, the Model-S strengthen-first worked example): archived at [`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md). Its evergreen process content was lifted into `../doc/audit-routing-instructions.md`; the file itself is now reasoning-trail archaeology.

The top-level `audit-findings-*.md` files not named above are de-novo cluster outputs from that backlog; consult the MANIFEST / pending-findings ledgers for their disposition before treating any as un-routed. Status of a file not yet verified against current `src/` is *unknown-until-checked*, not *open* — do not infer either from this table's silence.

---

*Append a row when an audit lands; move it from "open" to a MANIFEST entry when it graduates. Keep this file honest about the difference between "routed" and "graduated", and never record a status you have not verified — an unverified affirmation here is the exact failure the routing instructions' independent-verify gate exists to catch.*
