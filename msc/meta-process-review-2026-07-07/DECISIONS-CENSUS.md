# Decisions Census — what is actually blocked on Joseph (2026-07-07)

*Consolidated from the 10-cluster discovery fan-out. This file is the raw material for the decision-routing mechanism, and also a first prototype of it: every item gives the reconstructed context, why it's genuinely Joseph's, where the full brief lives, and a lead-recommendation with honest uncertainty where one can be formed. Working artifact — not committed, not canon.*

**The one meta-finding first.** Ten agents, working blind on separate slices, independently converged on the same shape: the infrastructure is genuinely good — often excellent — and nearly every stall reduces to *a Joseph-decision that never reached him in actionable form*. Cluster 02 put it sharpest: decision-routing (MP-8) is not one process beside the others, it is the **parent** — every stall in the other processes is one of its children. That convergence, across independent probes, is (by the project's own "convergence as coherence evidence" principle) strong evidence the diagnosis is real and in the system, not in any one agent's head. **The bottleneck is not ideas and not tooling. It is this.**

---

## Part A — Genuinely yours (ranked by leverage)

Each: **what** · *context you'd need* · **why you** · where the brief is · lead-rec.

### A1. The standing gold-dir gate — 22 `AUDIT-WORKING-*` dirs *(highest leverage: one decision unblocks the most)*
*22 de-novo audit "gold" dirs (first-encounter cognition / §14 Wandering Thoughts) are routed but cannot clear the live tree until you decide the gold's disposition. This gate — "consult Joseph, decide with him" — has been convened exactly once (the 2026-05-30 gold-lift, and only for lifting, not graduation). It is the structural cause of **0 of 22 audits having graduated**, and it makes the audit backlog look far more open than it is (STATUS.md's table shows 4; there are 22).* **Why you:** the gate is defined as non-optional-Joseph by `audits/README.md`. **Brief:** needs assembling (partial in audits/STATUS.md). **Lead-rec:** convene *once*, set a standing *policy* (e.g., "lift gold to WN, then archive the dir; here's the default") so it never needs re-convening per-dir — turn a recurring gate into a one-time rule.

### A2. D-2 — the bulk-64 `.integrated/` wipe *(the only item currently in JOSEPH-TODO)*
*64 spikes were bulk-filed to `spikes/.integrated/` in May 2026 without per-spike content verification. `.integrated/` (127 entries) + `.archived/` still exist; the 2026-05-19 wipe you signalled never happened. Before deleting, either verify those 64 landed in canon, or consciously accept the risk of losing any un-landed valid math/no-gos.* Three coupled sub-calls: discharge-vs-set-down; semantics (git-recoverable `rm`+commit vs history-purge); scope (also `02-tst-core/simulations/`? `track-b-nonlinear-sims/`? `ref/`?). **Why you:** irreversible. **Brief:** INTEGRATION-CLEANUP-TODO F3/D-2 (assembled). **Lead-rec:** git-recoverable removal, *after* a cheap verify-pass on the 64 (an agent can do the verify); never history-purge.

### A3. SP-30 — the root-ontology call *(freshest, highest theory-leverage; a good brief already exists)*
*Adopt the typed epistemic target $S_t=(\Omega_t,\theta)$ — giving law-content $\theta$ (the agent's ability to simulate the world) its own named slot, distinct from state $\Omega$ — or keep state-only $\Omega$ and accept the GA-1 observational-equivalence indeterminacy. Every segment that currently meets $\theta$ houses it ad hoc and they disagree. The gating claim is verified (`82c9bcc`).* **Why you:** root-ontology, reshapes the theory's spine. **Brief:** `spikes/epistemic-target-ontology/` (5 files — **this is the worked example of a good decision-brief; the mechanism should be shaped from it**). **Lead-rec:** none — genuinely yours; the package is built for you to decide from.

### A4. Segment-promotion policy — is `draft`+honest-tier the intended terminus? *(unblocks the WN deluge)*
*0 of 235 segments have reached `format-clean` or `candidate`; the ladder stalls at `claims-verified`. Gate 4 (candidate) is the designed Working-Notes drain and has never fired — which is the structural root of the WN deluge (95% of segments carry Working Notes). Your answer decides whether the fix is "run Gates 3–4" or "drain WN another way."* **Why you:** a framework-policy call (breadth-over-polish may be deliberate — but it's undocumented). **Brief:** cluster-01 findings. **Lead-rec:** state the policy explicitly either way; if breadth-first is intended, define an alternate WN-drain so the deluge stops being structural.

### A5. C5 — intelligence-empathy convergence routing *(the corpus's boldest claim)*
*Whether/where to land the structural leg (03-llm-core, near cognitive-fusion) and the normative-dynamic leg (04-eli-core, the orthogonality-thesis contest, Bostrom named) at honest tier. This is the corpus's largest conviction-vs-derivation gap — hypothesis-grade by the project's own lights.* **Why you:** authoring-voice + framework-identity on the highest-stakes claim; the normative-register allowance is yours. **Brief:** `msc/era-artifact-asf-contributions-2026-07-04.md` §Addendum-2. **Lead-rec:** none yet — I'd want to read the full era-artifact doc first.

### A6. G5 — CLAUDE.md-as-unreviewed-amplifier *(meta: the exact defect-class this review exists to fix)*
*The auto-loaded onboarding doc every agent treats as gospel, that you don't routinely read, with a demonstrated case of a predecessor's exception silently overriding a correct principle for weeks. Open since 2026-05-19, unowned. Fix options: a periodic human-visible review cadence, and/or generate portions the way LEXICON/README are generated (the pattern already exists).* **Why you:** governance architecture; "can't rest on agent virtue." **Brief:** INTEGRATION-CLEANUP §F6/§G5. **Lead-rec:** generate what's derivable + a light cadence for the rest; fold into the mechanism from Phase 2.

### A7. 04-eli-core → its own (possibly private) repo? *(strategic exposure)*
*The one repo-decomposition option with a real distinct driver: defensive/exposure decoupling, so Vols 1–3 can publish without the ELI/consciousness association — despite a 189-reference coupling cost (152→01, 37→03).* **Why you:** a strategic-exposure trade (publication posture, ELI-sensitivity), not an engineering one. **Brief:** cluster-10 findings §Option-D. **Lead-rec:** none — gather-and-frame only, per scope.

### A8. Fresh archival (Zenodo) release? *(irreversible publication act)*
*CITATION.cff / .zenodo.json are frozen at v0.1.0 / 2026-05-02 (one Zenodo concept DOI ever cut); volumes are now AAT 0.3.0 / TST 0.2.0. Minting a version DOI is irreversible.* **Why you:** a publication act only you can authorize. **Brief:** cluster-05. **Lead-rec:** defer until a deliberate release point; but fix the 2 stale AAD keyword residues in the metadata now regardless.

### A9. `.claude/` un-gitignore? *(gates most automation adoption)*
*The whole `.claude/` dir is gitignored, which structurally forecloses any shared/reviewable/version-controlled project automation — subagent defs, curated settings, hooks. This gates most of cluster-09's proposed adoptions.* **Why you:** a repo-policy call with a real privacy/shareability tradeoff. **Brief:** cluster-09. **Lead-rec:** un-ignore at least `agents/` + a curated `settings.json`; keep `settings.local.json` (secrets/paths) ignored.

### A10. Authoring-voice naming calls (a cluster, all yours) — lower individual leverage, but they gate the naming program
- **Separability-triad rung-names** (3 names; Hintikka echo *definable / identifiable / non-identifiable* leading). **Brief:** to-canonicalize.md.
- **Agent-spectrum tetrad** — choose 4 quadrant names as one parallel set (blind-seeker was only an interim one-cell swap). **Brief:** TERMINOLOGY-TODO §E.
- **Greek-vocabulary per-term** — tighten the segment prose to earn each Greek distinction, or soften the README claim. *Note: the voting cohort defended the terms; the incremental audit found they do no formal work — the two processes disagree, which is itself a calibration signal.*
- **§F Continuity/Persistence LEXICON reorg** — approve the 5-step reorg + rule whether "Continuity Stance" is a structural axis or a deployment-level property (blocked on a second opinion since 2026-05-10).

*(Also parked, lower stakes, lead can mostly default: gold-lift resume-vs-retire · the 184930 predictions-doc gold disposition · Brief-as-section FORMAT move · README-v2 J-block · CURRENT-VOL1 committed-artifact policy · the several FORMAT-TODO open-questions Q2/Q3/Q4 · chapter groupings C17.)*

---

## Part B — Free wins (agent-executable now, zero Joseph input)

These need no decision — they're already-decided or pure fact-fixes. Motion available immediately:

1. **C5–C13 terminology entries** — ~40 already-decided canonicalize commitments, verified missing as entries; one workflow executes them (03).
2. **Stale OUTLINE `missing` markers** — 6 in 04-eli-core + 1 in 03-llm-core mark segments that exist at `draft` (01).
3. **Memory ratification-sync** — the auto-loaded `feedback_spike_references_only_in_working_notes.md` still carries the "need vs mention" framing you rejected on 2026-05-30; the post-ratification pass never ran (04).
4. **NEXT-UP.md is actively misleading** — stale by the entire 07-03/04 arc; its job is resume-momentum and it would mislead a fresh session. Drain-or-refresh (07, 08).
5. **File-Org map is missing 7 live root trackers** (JOSEPH-TODO, TODO-big-picture, TST-IDEAS, HISTORICAL-CONTEXT, BIBLIOGRAPHY-TODO, CURRENT-VOL1, + DOMAINS.md) — every agent loads this map (04, 08).
6. **Stale counts in prose** — routing says "58 marked / ~511 unrouted"; actual is 123 / 506 (03). terminology/README describes a pre-migration state that's already done.
7. **2 AAD keyword residues** in CITATION.cff / .zenodo.json survived the AAD→AAT rename (05).

---

## Part C — Surprises / risks you may not know

- **Licensing exposure (real):** a full commercial *Garamond Premier Pro* family (37 `.otf`, ~35 MB) is committed to the CC-BY-4.0 repo at `mono/scrbook/fonts/garamond/` — a plausible redistribution violation if the repo is public. (Inter/FiraCode alongside are open-licensed; Garamond is the exposure.) (05)
- **The "monolith" feeling is mostly a packaging illusion:** the theory is **8.6 MB of a 225 MB tracked repo**; the bulk is `ref/` (135M, git-tracked PDFs) + `_obs/` (162M obsolete, in the live tree) + `mono/` (116M build output, largely un-gitignored). The measured *coupling* argues the theory core should stay cohesive; the felt pressure to decompose is very likely just clone-weight. Cheapest high-value fix in the whole review, and it's orthogonal to the strategic decomposition question (10).
- **The gold pools faster than it drains — and this review adds to it.** `msc/reflections/` (36 files incl. #28) *is* un-lifted audit gold; these 20 findings files are more. **Any "map the meta-processes" output must define its own drain or it becomes the next un-lifted pool.** (02, self-aware and correct — I'll build the drain into Phase 2.)
- **The memorata memory-curation workshop is confirmed frozen at 2026-05-12** (~8 weeks); ~63 planned global detail files never written (methodology/ 0-of-28, research-xref/ 0-of-25). Matches your "got somewhere but wasn't done" recollection exactly (04).

---

## Known coverage gap

The **ELI / `_core` operational-substrate / empirical-cohort-record** territory was scoped lightly on purpose (advanced, sensitive) — cluster 06 touched `firmatum/` and `_core/*` only at `ls`-level, and cluster 01 explicitly deferred moral-status framing. If a canary of Joseph's lives there, that's the known thin spot; a dedicated agent can close it.
