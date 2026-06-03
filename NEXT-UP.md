# NEXT-UP — live handoff pointer (updated 2026-06-02)

> [!note]
> **Transient pointer, not a navigator.** Authoritative homes: `PRACTICA.md` (strategy) / `TODO.md` (tactics) / `PROPOSALS.md` (structural moves) / `audits/STATUS.md` (audit routing) / `INTEGRATION-CLEANUP-TODO.md` (the big cleanup) / `CHANGELOG.md` (narrative). This file only names what is *hot* so a compaction or fresh session resumes momentum. **Delete once the queue drains.**

## Hottest thread — SOP consolidation (June 2026)

**The `doc/sop/` home is open and the interment sweep is running.** Scattered process-SOPs are being consolidated into `doc/sop/` under the `.sop.md` (leaf) / `.sop/` (branch) convention; the auto-loaded layer (CLAUDE.md + memory) demotes to index + disposition + before-action triggers. Charter + convention: [`doc/sop/sop-creation.sop.md`](doc/sop/sop-creation.sop.md). Full inventory + migration plan + ratified gate decisions: [`msc/sop-consolidation-design-2026-06-01.md`](msc/sop-consolidation-design-2026-06-01.md).

**The interment pattern (proven over two docs):** rewrite live forward-pointers · regenerate generated outputs at source (scripts / README partials) · leave frozen archaeology period-correct · no tombstone stubs · `bin/check-links` is the gate after each (it backstops the ref-split — it has caught live refs the recon agents missed). `bin/check-links` excludes archaeology and defers `…-core/src/` segment links to lint-outline; repo-specific exemptions live in `.check-links-ignore`.

**Landed this cycle:** `naming.sop` fully interred — `methodology.sop.md` (`ad59d57`) + `principles.sop.md` (`305c541`) under the `naming.sop.md` index; **`spike-routing.md` interred → `doc/sop/spikes.sop.md`**; `bin/check-links` built (`f6ffaa5`); 3 stale links fixed (`5bb5177`); `JOSEPH-TODO.md` created (`1382d64`); legacy `bin/build-tex` sunset (`60a201f`); **`format.sop` interred** (`038e2ed` — `FORMAT.md` is now a symlink to it).

**Remaining — full plan in [`msc/sop-shift-completion-plan-2026-06-02.md`](msc/sop-shift-completion-plan-2026-06-02.md).** Phase A (mechanical; a fast agent + `check-links`): the **audit pair** (de-novo + audit-routing → `doc/sop/audit.sop/`) via the **symlink trick** — leave the old paths as symlinks so all ~300 inbound refs resolve untouched; only fix the moved files' outbound (+2 depth) + their two mutual cross-refs. Phase B (the substantive value, in order): **author the orphan SOPs** (`multi-agent`, `git-hygiene`) from the memory files; **single-source the drifted disciplines** (WN-discipline → FORMAT, etc.); then **slim `CLAUDE.md`** to disposition + index + before-action triggers; then the `sop.md` master index. Slim CLAUDE.md *last* — it points at the homes Phase B settles.

**Decisions for Joseph → [`JOSEPH-TODO.md`](JOSEPH-TODO.md)** is now the single queue for everything needing him (the WN-discipline gate, the `doc/sop/sop.md` master-index question, the TODO-freshness reframes, D-2 / G3 / SP-27 / SP-29, the Greek-vocab + README-v2 taste calls).

## Also active — the audit-gold two-track

**Discovery (2026-05-30).** The de-novo audit process yields two intertwined outputs: (1) *certified findings* — theory-fixes, the fast queue, already handled; and (2) **incidental orthogonal gold** in the per-segment "wandering thoughts" / §14 ideation — pedagogical framing, analogies, candidate figures, naming, forward-vision, aspirational reach (Gemini especially: reach that sometimes becomes real *because* imagined). This gold has been pooling unrouted in `audits/AUDIT-WORKING-*/`. It belongs **per-segment** — lifted into the segment's Working Notes, eventually promoted to its Brief / Discussion — **not** a separate catalog. The early finding-vs-framing *conflation is itself signal* and must be preserved, not sanitized.

**Validated by pilot — commit `7594391`.** `#result-persistence-condition` swept: cross-audit gold lifted into its WN in six categories (Brief-prose · Discussion · follow-ups · readers-ask · figures · belongs-elsewhere), deduped across substrates and attributed. Standouts: a transient-adequacy *third* condition $1/\alpha \lt T_{\text{tolerance}}$; Gemini's crèche/nursery reading $\to$ `04-eli-core`; "adding developers *accelerates* collapse"; a $2\times2$ two-gate figure two substrates asked for; four substrates praising the existing Brief as a Feynman exemplar.

**Filing convention — clarifies dirs by degrees.** As each segment is swept, its *dedicated* source-note moves into a per-dir `audits/AUDIT-WORKING-<id>/.integrated/`; each dir's top level then shows only still-to-sweep notes, and graduates once empty. **Match by content, never by note-number** — the same segment was filed #15/#20/#21/#22/#23/#29/#30/#32 across audits. Move ONLY the exact segment; the adjacent persistence-*family* segments are distinct and stay.

**Plan / live queue for this thread:**
- **Flow-fix — DONE 2026-05-30** (commit `bbf642f`): `doc/de-novo-audit-instructions.md` §7.15 (auditor-side) + `doc/audit-routing-instructions.md` §8 "gold lift" (integrator-side) route future audits' incidental gold per-segment, separate from certified findings.
- **Sweep — IN PROGRESS:** waves 1–4 swept (AAT core through Appendix-A set 2 — 122 gold-bearing segments); **wave 5** (A18–A21) + TST / logogenic / logozoetic remain, then the held batched/paired-note reconciliation + the OUTLINE C-iv idiom-drift fix. Lift-agents edit segment Working Notes, lead files sources + commits per wave. **Durable plan + per-wave progress + deferral state: [`audits/.gem-hunt-trail/gold-lift-sweep-2026-05-30.md`](audits/.gem-hunt-trail/gold-lift-sweep-2026-05-30.md).**
- **Open decisions:** batch-file dirs (451729 / 471203 / 613842 / 963715 hold notes inside multi-segment batch files — leave-until-fully-swept vs. split, lean leave); the **Brief-as-section** FORMAT move (a Brief between title and Formal Expression, absorbing today's `Findings#brief`) — well-supported, Joseph's call; per-dir `.integrated/` vs. top-level mirror (chose per-dir; redirectable); taxonomy = your 1–5 + agent's *Candidate figures* + a confusion-vs-placement split.
- **Gold-dir gate** still stands for anything beyond this agreed sweep.

## Also hot — directed-separation arc (LANDED) + the WN-discipline gate (your call)
**Foundation pass landed + internally consistent** (CHANGELOG 2026-05-31): the W₁ correctness-fix → the `causal discipline` re-founding of `#der-directed-separation` (`fbcb36a`/`ed11222`/`7d062f6` sweep/`be1b2c4`/`bd8a0d6`/`7655ba2` intro-fix; framing core independently reviewed — all three normativity guards pass), the Stage-1-completion propagation to `03/04` (`c0f5936`), and the spike-corpus cleanup (`352a8bb` — 4 spikes filed to `.integrated/`; sims/figures stay in place pending the G3 sim-integration discipline). Full design archived at `_obs/directed-separation-foundation-execution-plan-superseded-2026-05-31.md`.

**Freshest decision waiting on you — the WN-discipline coherence gate:** A-vs-B (lead's lean **B**, single-source the discipline in FORMAT, others reference) + scope (project-only vs the global `~/.claude/` layer where the discipline also lives). Self-contained in [`msc/wn-discipline-coherence-pass-2026-05-31.md`](msc/wn-discipline-coherence-pass-2026-05-31.md); condensed carry + the provisional developing-discipline in `INTEGRATION-CLEANUP-TODO.md`. The SOP edits stay proposal-grade until you call it.

**Reserved adjudication:** the `#schema-strategy-persistence` hard-ceiling convention (`aedc72d`, verdict B — name the convention, keep `status: exact`). **Tracked-open in `TODO.md`:** the two exploratory-spike findings (the `#def-auxilia-hierarchy` necessity over-claim — separate-substrate is sufficient-not-necessary; the goal-flow-duality discussion-grade landing) and the foundation tail (Stage-2 vocabulary + the pedagogy pass). The sim/empirical integration gap (G3) is carried in `INTEGRATION-CLEANUP-TODO.md`.

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
