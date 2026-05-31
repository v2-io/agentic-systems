# NEXT-UP — live handoff pointer (updated 2026-05-30)

> [!note]
> **Transient pointer, not a navigator.** Authoritative homes: `PRACTICA.md` (strategy) / `TODO.md` (tactics) / `PROPOSALS.md` (structural moves) / `audits/STATUS.md` (audit routing) / `INTEGRATION-CLEANUP-TODO.md` (the big cleanup) / `CHANGELOG.md` (narrative). This file only names what is *hot* so a compaction or fresh session resumes momentum. **Delete once the queue drains.**

## Hottest thread — the audit-gold two-track

**Discovery (2026-05-30).** The de-novo audit process yields two intertwined outputs: (1) *certified findings* — theory-fixes, the fast queue, already handled; and (2) **incidental orthogonal gold** in the per-segment "wandering thoughts" / §14 ideation — pedagogical framing, analogies, candidate figures, naming, forward-vision, aspirational reach (Gemini especially: reach that sometimes becomes real *because* imagined). This gold has been pooling unrouted in `audits/AUDIT-WORKING-*/`. It belongs **per-segment** — lifted into the segment's Working Notes, eventually promoted to its Brief / Discussion — **not** a separate catalog. The early finding-vs-framing *conflation is itself signal* and must be preserved, not sanitized.

**Validated by pilot — commit `7594391`.** `#result-persistence-condition` swept: cross-audit gold lifted into its WN in six categories (Brief-prose · Discussion · follow-ups · readers-ask · figures · belongs-elsewhere), deduped across substrates and attributed. Standouts: a transient-adequacy *third* condition $1/\alpha \lt T_{\text{tolerance}}$; Gemini's crèche/nursery reading $\to$ `04-eli-core`; "adding developers *accelerates* collapse"; a $2\times2$ two-gate figure two substrates asked for; four substrates praising the existing Brief as a Feynman exemplar.

**Filing convention — clarifies dirs by degrees.** As each segment is swept, its *dedicated* source-note moves into a per-dir `audits/AUDIT-WORKING-<id>/.integrated/`; each dir's top level then shows only still-to-sweep notes, and graduates once empty. **Match by content, never by note-number** — the same segment was filed #15/#20/#21/#22/#23/#29/#30/#32 across audits. Move ONLY the exact segment; the adjacent persistence-*family* segments are distinct and stay.

**Plan / live queue for this thread:**
- **Flow-fix first (stop the influx, then empty the pool):** proposed changes to `doc/de-novo-audit-instructions.md` so future audits route incidental gold per-segment immediately, separate from certified findings, in the six-category structure. *[in progress 2026-05-30]*
- **Then the sweep:** segment-by-segment lift across the rest; agents, pre-indexed (6 of 21 dirs are partial / naming-only / predictions-only — skip). Effort ~20–50 min/segment (hub segments worst-case).
- **Open decisions:** batch-file dirs (451729 / 471203 / 613842 / 963715 hold notes inside multi-segment batch files — leave-until-fully-swept vs. split, lean leave); the **Brief-as-section** FORMAT move (a Brief between title and Formal Expression, absorbing today's `Findings#brief`) — well-supported, Joseph's call; per-dir `.integrated/` vs. top-level mirror (chose per-dir; redirectable); taxonomy = your 1–5 + agent's *Candidate figures* + a confusion-vs-placement split.
- **Gold-dir gate** still stands for anything beyond this agreed sweep.

## Other open threads (Joseph's calls)
- **SP-27** — introspective-fork-undetectability; Part-I ↔ Part-IV (moral-core) bridge, his placement/framing call. → `PROPOSALS.md`.
- **SP-29** — `#disc-infrastructure-as-active-monitor` meta-segment candidate; gated: verify constituents first-hand + check `~/src/practica`. → `PROPOSALS.md`.
- **D-2** — wipe of `spikes/.integrated/` + `.archived/` (semantics / timing / scope); G2 de-risked it but the bulk-64 is still un-discharged. → `INTEGRATION-CLEANUP-TODO.md`.
- **G3** — citation infrastructure / `ref/` reconciliation; publication-critical-path. → `INTEGRATION-CLEANUP-TODO.md` §G3.

## Self-contained — no decision needed
- **Standalone-backlog gem-hunt:** the `.integrated/MANIFEST.md` + `pending-findings-*.md` backlog, not yet done under the verify-first lens. → `audits/STATUS.md`.
- **Research-seeds** S31–S41 in `audits/polish-and-sentiment-ledger.md` (each gated on a per-item re-check).
- **FORMAT `depends:` forward-ref field** (`strengthens:` / `forward-ref:` separating logical-prerequisite from forward-pointer). → `TODO.md` §"Editorial hygiene".

## Landed 2026-05-30 (full narrative in CHANGELOG)
D-1 ratified + D-3 resolved (`0ca46bf`, `b7d9b9c`); **G2 reference-cleanup** — canon→artifact integration across 38 segments + buried-gold landings (bridge-lemma Theorem 2, the $2\delta+3\sin\delta$ counterexample, two-Kalman closed form, $\alpha\approx0.118$) (`9099e58`); `bin/lint-md` conservative bare-Greek `--fix` (`aa75c7a`); governing-doc banners truthified (`36d1242`); `spike-routing.md` hard-wrap reflow 241→1 (`9686985`); audit-gold pilot (`7594391`).

## Disposition that still governs audit-findings work

Audit findings are stale, mostly-unverified *hints*: verify against current canon first-hand (dispositions drift); strengthen before softening; lint *gates* the commit; non-loss is the hard constraint. Full stance: project memory `feedback_audit_findings_as_gem_hints`; `doc/audit-routing-instructions.md`.
