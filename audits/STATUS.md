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
| `audit-731548-FINAL-2026-07-02` | 2026-07-02 | Claude Fable 5 (de-novo: AAT Part I main chain + 9 impl-* + 6-agent verification round) | **routed (2026-07-03); Tier-1 + mood executed** | Executed 2026-07-03 (CHANGELOG): **B-1** strengthen-by-split landed (Lemma A.1N + counterexample Remark + certificate-voice register fixes; gated on a *second* independent re-derivation, which refuted necessity by fresh construction); **B-2** three-term decomposition + $\rho_\star$ INDEX row reopened-and-re-closed (**flag for Joseph: the 2026-05-21 closure he ratified reopened one notch**) + detection-signature companion; **B-4** Regime-III correctness fix. **B-3** → PROPOSALS **SP-30** (awaits Joseph — root definition + constitutive atoms). Mood MG-discharge executed ($g$-band/complacency floor + MG-1..4 instantiation + estimator-role ES clause). Remaining open (TODO §2026-07-03): impl status-tagging pass; legacy quantifier sweep; chronica absorb-into-$\phi$ staged promotion; nominal-coupling→query-only-coupling rename (naming process); floor-routing segment; shadow-catalogue appendix; SOP additions (Gate-2 instantiate-check, gold-deferral); INDEX FULLY-RESOLVED spot-check. Gold lift for the 36 reflections not started; gold dir `AUDIT-WORKING-731548/` under the standing gate. Does not graduate until the routed remainder closes and the gold dir settles with Joseph. |
| `audit-773921-FINAL-2026-05-28` | 2026-05-28 | Gemini 2.5 Pro | **routed, not graduated** | **F1 + F4 both resolved** — SP-24 executed (`#def-agent-environment` coupling-structure reframe + umbrella `agent` LEXICON entry) and SP-25 executed (`#disc-sandbox-evaluation-ceiling` promoted to Appendix A with Findings); CHANGELOG 2026-05-28. Routed: F2 → TODO (intro-rename item); F3 already-tracked; seeds/sentiment → ledger S31–S33 + P-block. **Only blocker to graduation: the gold dir `AUDIT-WORKING-773921/`** (committed-untouched; disposition pending the standing gate with Joseph). Once that settles, every finding is closed and the audit graduates to `.integrated/`. |
| `audit-384279-FINAL-2026-05-27` | 2026-05-27 | Claude Opus 4.7 | **resolved, not graduated** | Both structural findings landed in canon (scrbook hierarchy sweep; composition-consistency reframe — CHANGELOG 2026-05-28); three residual spike proposals in `spikes/PROPOSED.md`. Remaining: graduate to `.integrated/` once the residual proposals are dispositioned, and settle the gold dir `AUDIT-WORKING-384279/`. |
| `audit-451729-FINAL-2026-05-10` | 2026-05-10 | — | **open** | Single residual D.1 (first-class in `TODO.md` §2026-05-10). Soft items → ledger S25/S28. Does not graduate until D.1 closes. (Per MANIFEST.) |

## Gem-hunt cycle (2026-05-29) — five under-mined audits mined for un-captured gems

A qualitative pass (Joseph 2026-05-29: audit findings as stale hints, mined for meat/gems improving the theory in strength/wisdom/beauty; non-loss is the hard constraint — see `feedback-audit-findings-as-gem-hints` in project memory). Five audit-findings files with zero ledger / zero-or-near-zero MANIFEST hits (never mined, never dispositioned) were each read first-hand against current canon by a general-purpose agent (pilot 472913 + background 526815/963715/542891/184930); the parent verified each gem first-hand before landing/routing. Trails: `.gem-hunt-trail/GEM-WORKING-<id>/` (committed).

Outcomes (all routed; nothing buried):
- **Two real math errors fixed** (CHANGELOG/commit `f8d9151`): `#form-strategy-complexity-cost` $d^\ast$ table cell (5→0); `#def-unity-dimensions` epistemic-unity normalization ($(n{-}1)$ factor — strengthen-first, not soften).
- **Two headline gems → PROPOSALS** (both wanting Joseph's call): SP-26 (the cross-cycle-triangulated which-parameter-disambiguation novelty signature, gated on an instance sweep); SP-27 (introspective-fork-undetectability — the Part-I↔Part-IV bridge grounding "the Three Deaths are *experienced*", verified real gap).
- **Research-seeds → ledger** S34–S38; **actionable items → TODO** (nominal-terminology contradiction; C-iv route-count mismatch; lint eq-tag-priority); **audit-methodology → ledger P-block**.
- **Confirmed non-losses** with loci across all five; **drift correction**: every audit's flagship finding had already been resolved by a later cycle (the central confirmation that audit dispositions are drifted proxies).

These five audits are now *gem-mined and routed*. They do **not** graduate to `.integrated/` yet — the de-novo `AUDIT-WORKING-<id>/` "gold" dirs remain under the standing consult-Joseph gate, and the FINAL files' full burden-of-proof rows were not exhaustively re-verified (the gem-hunt targeted gem-bearing sections + dispositioned-away findings, not every §B row — 526815's ~200 F-rows explicitly flagged stale-until-re-grepped).

**Wave 2 (same day) — seven *partially-mined* audits** (193847 / 849201 / 742613 / 829314 / 471203 / 613842 / 738192): each cross-checked what was already routed and targeted only the un-captured remainder. Lower-treasure than wave 1 (expected — picked-over): mostly careful negatives + confirmed non-losses with loci, *every* flagship finding already resolved-in-canon (uniform drift). Real output, all routed: a convergent agency-boundary strengthen-first gem (742613 + 193847 → **SP-28**); a PROPOSALS-grade meta-segment candidate (193847 B6 → **SP-29**); research-seeds → ledger **S39–S41** (two converging with prior findings: goal-blind-retrieval ~ S32; the `depends:` forward-reference hygiene → TODO, converging with the lint eq-tag item + 472913 GEM 6). Trails: `.gem-hunt-trail/GEM-WORKING-<id>/` (committed). Same non-loss posture — nothing graduated; gold dirs gated; remainder routed not landed. The whole de-novo audit-findings backlog has now had a verify-against-canon-first gem-hunt pass (twelve audits across the two waves); the standalone backlog's earlier dispositions live in the MANIFEST / pending-findings ledgers.

## Historical backlog (graduated or trail-tracked elsewhere)

The 2026-03 / 2026-04 audit intake and the standalone-audit backlog were dispositioned during the 2026-05-15/16 cleanup cycle. Their per-finding records live in the durable trails, not here:

- **Graduated** files + their dispositions: [`.integrated/MANIFEST.md`](.integrated/MANIFEST.md).
- **2026-04-21/22/23/25 cluster intakes** (471203 / 584721 / 613842 / 742613 / …): the `pending-findings-2026-04-2{1,2,3,5}.md` resolution ledgers.
- **The cleanup cycle's own working spine** (state machine, evidence hierarchy, per-file partition, agent briefs, the Model-S strengthen-first worked example): archived at [`.integrated/audit-backlog-triage-2026-05-15.md`](.integrated/audit-backlog-triage-2026-05-15.md). Its evergreen process content was lifted into `../doc/audit-routing-instructions.md`; the file itself is now reasoning-trail archaeology.

The top-level `audit-findings-*.md` files not named above are de-novo cluster outputs from that backlog; consult the MANIFEST / pending-findings ledgers for their disposition before treating any as un-routed. Status of a file not yet verified against current `src/` is *unknown-until-checked*, not *open* — do not infer either from this table's silence.

---

*Append a row when an audit lands; move it from "open" to a MANIFEST entry when it graduates. Keep this file honest about the difference between "routed" and "graduated", and never record a status you have not verified — an unverified affirmation here is the exact failure the routing instructions' independent-verify gate exists to catch.*
