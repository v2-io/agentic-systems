# NEXT-UP — DRAINED 2026-07-15 (frozen; was the root live-handoff pointer, last updated 2026-06-30)

> [!note]
> **Drained per its own charter** ("Delete once the queue drains") via the MP-08.2 ritual, Joseph-authorized 2026-07-15. Live residuals migrated: gold-lift wave-5 queue → `audits/STATUS.md`; the two outside-repo Joseph items → `JOSEPH-TODO.md`; all open decisions → `msc/decision-briefs-2026-07-15.md` (the valve). What replaces it: PRACTICA (areas) / TODO (tactics) / JOSEPH-TODO + the decision-briefs valve (Joseph-calls) / CHANGELOG (narrative). Everything below is frozen archaeology of the 2026-06 arc.

> [!note]
> **Transient pointer, not a navigator.** Authoritative homes: `PRACTICA.md` (strategy) / `TODO.md` (tactics) / `PROPOSALS.md` (structural moves) / `audits/STATUS.md` (audit routing) / `INTEGRATION-CLEANUP-TODO.md` (the big cleanup) / `CHANGELOG.md` (narrative). This file only names what is *hot* so a compaction or fresh session resumes momentum. **Delete once the queue drains.**

## Landed since 2026-06-02 (full narrative in CHANGELOG)

**Multi-timescale stability (2026-06-10).** `#der-multi-timescale-stability` promoted to `derived`/`exact` (Model D): per-level sector conditions + bounded interconnection ⇒ composite $N$-level stability, with a closed-form nesting threshold and a warm/cold-start reserve-gap pricing.

**Deaths grounding (2026-06-10) + mood/agency-death arc (2026-06-10→17, latest commit `e420587`).** Back-integration from Inquiry Paper 4: `#def-death-as-factor-loss` replaces the Three-Deaths hypothesis (continuity/relational/agency/truth at per-death tiers, phenomenological predicted-not-adjudicated). Released follow-ons since landed: `#def-mood` (Part I, second-order adaptation) + sovereignty-carve memo; `#der-mood-timescale` (F2, optimal time-constant is a sqrt-law); both agency-death legs — `#der-severed-actuation-dynamics` (output) and `#der-captured-objective-dynamics` (input, the reward-channel no-go / Agentic↔Truth bridge). Plan: `msc/deaths-grounding-plan-2026-06-10.md`. Remainder tracked in TODO §"Deaths taxonomy".

**Stale-navigator find + fix (2026-06-30).** PRACTICA item 4 named "four missing scope segments" (`scope-channel-collapse`, `scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop`) as the other half of the deaths-grounding cycle. On pickup: all four already existed at `stage: draft` with substantive content (landed in `ce99ce6`, the 03/04 dir-harmonization commit) — `03-llm-core/OUTLINE.md` simply never had its `missing` markers updated. Same staleness found on two more rows (`disc-framework-self-diagnostic`, `disc-five-forcing-functions`) — also draft-complete. Fixed (OUTLINE + PRACTICA wording corrected, lint + check-links clean). Genuine remaining work on this cluster is **Gate 1 dependency audit** onward, not authoring — the segments' own Working Notes already say so. One row is genuinely missing: `hyp-checkpoint-forking-failure-modes` (it actually lives in `04-eli-core/src/`; tracked in TODO's cross-component segment-resolution item).

## SOP consolidation — LANDED 2026-06-02 (full narrative in CHANGELOG)

The `doc/sop/` shift is complete. All interments (`naming` / `spikes` / `format` / the **audit pair**), **`agents.sop.md` as the agent-orientation home + SOP index** (root `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` symlinked; body slimmed −20%), the two orphan SOPs (`multi-agent`, `git-hygiene`), the **WN-discipline single-sourced** into `format.sop.md` §"What earns a Working Note", and `bin/check-links` as the integrity gate. Convention charter: [`doc/sop/sop-creation.sop.md`](doc/sop/sop-creation.sop.md); reasoning trail: [`msc/sop-shift-completion-plan-2026-06-02.md`](msc/sop-shift-completion-plan-2026-06-02.md). Auto-loaded layers also condensed: global `~/.claude/CLAUDE.md` −19%, project `MEMORY.md` −40% (back under budget).

**Two things sit in Joseph's court** (neither blocks anything): commit the global `~/.claude/CLAUDE.md` (his in-progress edits are mixed with the condensation — `~/.claude/CLAUDE.md.bak` marks the boundary), and an optional eyeball on the `MEMORY.md` trims. **Deferred:** the global/memory-layer WN-narrowing pass (out of this project-scoped shift). Remaining Joseph-decisions live in [`JOSEPH-TODO.md`](JOSEPH-TODO.md) (all *other* threads — D-2 / G3 / SP-27 / SP-29, Greek-vocab + README-v2; D-citation is a future SOP-*content* discussion).

## Also active — the audit-gold two-track

**Discovery (2026-05-30).** The de-novo audit process yields two intertwined outputs: (1) *certified findings* — theory-fixes, the fast queue, already handled; and (2) **incidental orthogonal gold** in the per-segment "wandering thoughts" / §14 ideation — pedagogical framing, analogies, candidate figures, naming, forward-vision, aspirational reach (Gemini especially: reach that sometimes becomes real *because* imagined). This gold has been pooling unrouted in `audits/AUDIT-WORKING-*/`. It belongs **per-segment** — lifted into the segment's Working Notes, eventually promoted to its Brief / Discussion — **not** a separate catalog. The early finding-vs-framing *conflation is itself signal* and must be preserved, not sanitized.

**Validated by pilot — commit `7594391`.** `#result-persistence-condition` swept: cross-audit gold lifted into its WN in six categories (Brief-prose · Discussion · follow-ups · readers-ask · figures · belongs-elsewhere), deduped across substrates and attributed. Standouts: a transient-adequacy *third* condition $1/\alpha \lt T_{\text{tolerance}}$; Gemini's crèche/nursery reading $\to$ `04-eli-core`; "adding developers *accelerates* collapse"; a $2\times2$ two-gate figure two substrates asked for; four substrates praising the existing Brief as a Feynman exemplar.

**Filing convention — clarifies dirs by degrees.** As each segment is swept, its *dedicated* source-note moves into a per-dir `audits/AUDIT-WORKING-<id>/.integrated/`; each dir's top level then shows only still-to-sweep notes, and graduates once empty. **Match by content, never by note-number** — the same segment was filed #15/#20/#21/#22/#23/#29/#30/#32 across audits. Move ONLY the exact segment; the adjacent persistence-*family* segments are distinct and stay.

**Plan / live queue for this thread:**
- **Flow-fix — DONE 2026-05-30** (commit `bbf642f`): `doc/de-novo-audit-instructions.md` §7.15 (auditor-side) + `doc/audit-routing-instructions.md` §8 "gold lift" (integrator-side) route future audits' incidental gold per-segment, separate from certified findings.
- **Sweep — IN PROGRESS:** waves 1–4 swept (AAT core through Appendix-A set 2 — 122 gold-bearing segments); **wave 5** (A18–A21) + TST / logogenic / logozoetic remain, then the held batched/paired-note reconciliation + the OUTLINE C-iv idiom-drift fix. Lift-agents edit segment Working Notes, lead files sources + commits per wave. **Durable plan + per-wave progress + deferral state: [`audits/.gem-hunt-trail/gold-lift-sweep-2026-05-30.md`](audits/.gem-hunt-trail/gold-lift-sweep-2026-05-30.md).**
- **Open decisions:** batch-file dirs (451729 / 471203 / 613842 / 963715 hold notes inside multi-segment batch files — leave-until-fully-swept vs. split, lean leave); the **Brief-as-section** FORMAT move (a Brief between title and Formal Expression, absorbing today's `Findings#brief`) — well-supported, Joseph's call; per-dir `.integrated/` vs. top-level mirror (chose per-dir; redirectable); taxonomy = your 1–5 + agent's *Candidate figures* + a confusion-vs-placement split.
- **Gold-dir gate** still stands for anything beyond this agreed sweep.

## Also hot — directed-separation arc (LANDED)
**Foundation pass landed + internally consistent** (CHANGELOG 2026-05-31): the W₁ correctness-fix → the `causal discipline` re-founding of `#der-directed-separation` (`fbcb36a`/`ed11222`/`7d062f6` sweep/`be1b2c4`/`bd8a0d6`/`7655ba2` intro-fix; framing core independently reviewed — all three normativity guards pass), the Stage-1-completion propagation to `03/04` (`c0f5936`), and the spike-corpus cleanup (`352a8bb` — 4 spikes filed to `.integrated/`; sims/figures stay in place pending the G3 sim-integration discipline). Full design archived at `_obs/directed-separation-foundation-execution-plan-superseded-2026-05-31.md`.

**WN-discipline — LANDED 2026-06-02 (B2).** Single-sourced into `format.sop.md` §"What earns a Working Note" (a WN earns its place only if it assists future work: forward-pointer / regression-guard / dead-end warning; no vanity-changelog, no unneeded spike refs). Repo sites narrowed to pointers; the coherence-pass doc [`msc/wn-discipline-coherence-pass-2026-05-31.md`](msc/wn-discipline-coherence-pass-2026-05-31.md) is bannered landed. Memory-layer carriers (project `feedback_*` + global `~/.claude/`) inherit the narrowing in the deferred global/memory pass.

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
