# Decision briefs — 2026-07-15 (the valve)

*Every currently-open genuinely-Joseph decision, one brief each (decided items are deleted from this file — the decision record lives in CHANGELOG), ordered for a single sitting: quick nods first, strategic last. Each brief was verified against current repo state on 2026-07-15 (the 2026-07-07 census was the substrate; several items moved since). Standard per brief: decidable from this text alone — context, options, lead-rec with honest uncertainty, pointer to full detail. Record decisions inline (a word next to the title is enough — agents will route them) or however is easiest. Assembled by the decision-valve cycle; see CHANGELOG 2026-07-15.*

## Quick nods — strong lead-recs, a yes/no suffices

### F72 — Release or keep the external-eye hold on the hard-ceiling convention fix (aging since 2026-05-31)

*Since the 2026-07-07 census:* Still open and aging — the 2026-07-14 adjudication cycle (7 rulings, commit 9df63ee) did NOT include it and CHANGELOG explicitly lists it under "Left for Joseph"; segment still `status: exact` with no convention clause; schema off-ramp WN flag still live.

**What**: Whether to run the held adjudication now. **Context**: The spike `spike-strategic-persistence-hard-ceiling-convention-2026-05-31` confirmed (verdict B, high confidence, hand + simulation) that the $\rho_\Sigma \ge R_\Sigma/2$ hard ceiling in `#deriv-strategic-persistence-hard-ceiling` depends on the full-weight-current forgetting convention — under the textbook add-then-discount ordering it dissolves to the trivial bound. The prescribed fix is small and non-weakening: name the convention as a fourth condition in both segments, keep `status: exact` (exact-under-stated-conditions). It was RESERVED for an external-eye adjudication and has sat 6.5 weeks; the 2026-07-14 cycle explicitly left it for you, and JOSEPH-TODO already lists "take verdict B as settled" as the lead default. Meanwhile the segment's exact label is missing a premise the spike itself proved load-bearing — the hold is now costing truth, not buying safety. **Options**: (a) Release: run a fresh-mathematician re-derivation of Props C.1/C.2 + the SEG/ALT1 fork (the segment's own "owed" independent-verify), then land verdict B. (b) Take B as settled and land without the fresh eye. (c) Keep holding. **Lead recommendation**: (a) — it discharges both the external-eye reservation and the segment's standing verify debt in one cheap pass; (b) acceptable, (c) has no remaining upside. **Pointer**: `TODO.md` ~line 39; the spike §6–7; segment Epistemic Status "Strict-form independent-verify note".

### core.hooksPath is dead — unset it (near-free); optionally add the drift-guard hook

*Since the 2026-07-07 census:* Worse than the census: after the submodule migration, ~/src/agentic-systems/.git is now a gitdir *file*, so the configured hooksPath resolves to "Not a directory" — hooks are silently inert, not merely symlink-fragile. No real (non-sample) hooks exist anywhere in the module or repo, so nothing is currently lost.

**What.** Fix `core.hooksPath`. **Context.** Verified: the submodule's config (`archema-io/.git/modules/asf/config`) sets `core.hooksPath = ~/src/agentic-systems/.git/hooks`. Post-migration that path is a gitdir pointer *file*, not a directory — every hook is silently disabled. The module's own hooks dir contains only `.sample` files, and no hook scripts live in the repo, so as far as I can verify no real hook has ever been lost or is running; if the pre-rename repo carried real hooks, they went with its old `.git` dir (unverifiable now). **Options.** (1) `git config --unset core.hooksPath` — one command, zero loss, agent-executable; only flagged to you because it's program-migration territory. (2) Same, plus seize the moment for cluster-09's named-but-never-built automation: `bin/refresh-all --check` as a hook, so generated files (README/FINDINGS/LEXICON — 6 weeks stale until yesterday) can't silently drift. **Lead rec.** (2), as **pre-push** not pre-commit (drift-check on push keeps commit flow frictionless). If you'd rather not decide the hook now, say "just unset" — item closed either way in one line. **Pointer.** cluster-09 findings §29/§58; CHANGELOG 2026-07-14 "Left for Joseph."

### A9 — Un-gitignore .claude/ (selectively) so project automation can exist?

*Since the 2026-07-07 census:* Unchanged since the census. `.gitignore` still ignores all of `.claude/`; the dir holds only `settings.local.json` (92-entry permission graveyard, 8 dead `/src/act/` paths) and `worktrees/`. No `.claude/agents/` exists yet — this decision gates creating any.

**What:** Repo-policy call: stop gitignoring the whole `.claude/` dir so shared, reviewable project automation (subagent defs, hooks, a curated `settings.json`) becomes possible.

**Context:** Today the blanket ignore structurally forecloses *any* version-controlled harness config for ASF — no project subagents (e.g., a de-novo-auditor or math-verifier def codifying the manual fan-out you already run), no hooks (e.g., lint-gates-the-commit, the exact failure named in INTEGRATION-CLEANUP note 3), no shared permission allowlist. Cluster-09 found this is the single gate under most of its proposed adoptions. The only current content is local cruft, so nothing sensitive is at stake in the *tracked* set if the split is done right.

**Options:** (1) Selective un-ignore: track `.claude/agents/` + a new curated `.claude/settings.json`; keep `settings.local.json` and `worktrees/` ignored (negation patterns; reversible one-liner). (2) Keep the blanket ignore — automation stays personal/local only. (3) Un-ignore everything — rejected: `settings.local.json` carries machine-local paths/accretions.

**Lead recommendation:** Option 1, with confidence — low risk, reversible, and the local/shared split is the standard harness pattern. Independent do-anyway: purge the ~35 provably-dead entries from `settings.local.json`.

**Pointer:** census cluster 09 (esp. §e1); `.gitignore` line 6.

### Repo weight: untrack .archive/ (162M) + Garamond fonts (35M)?

*Since 2026-07-15:* the fonts half is done (untracked + gitignored 2026-07-15, CHANGELOG); `_obs/` was renamed `.archive/` and its 91M SVG gzipped to 44M on 2026-08-22, but `.archive/` is still tracked — the remaining call is that directory and whether to rewrite history.

*Since the 2026-07-07 census:* Census overstates the problem: ref/ PDFs were untracked ~2026-05-22 (ref/.gitignore, commits 6b0e984/a6397a6 — only 5.7M tracked now) and mono/ build outputs are already gitignored (mono/.gitignore). Remaining live weight decision is _obs + fonts + history.

**What.** Approve slimming the repo's tracked weight. **Context.** Theory content is ~8.6M, but the pack is 225.7 MiB. Verified today: ref/ PDFs are *already* untracked (5.7M tracked; census's "135M tracked PDFs" is stale) and mono build outputs are *already* gitignored. What's still tracked: `.archive/` **162M** (obsolete archive, live tree) and **35M** of mono/ = almost entirely the commercial Garamond Premier Pro fonts — which are also the CC-BY licensing exposure (census Part C). Plus CURRENT-VOL1 ~8.5M (separate brief). **Options.** (1) Nothing. (2) Untrack `.archive/` (move to an `archive/obs` branch or out-of-tree) + remove Garamond from tracking; working tree lightens, but **already-committed blobs stay in every clone until history is rewritten**. (3) History rewrite (`git filter-repo` on .archive/old-ref-PDF/font blobs) → clone drops toward ~15M, but all hashes change: breaks CHANGELOG/tag commit refs and the archema-io submodule pointer — its own decision. **Lead rec.** Do (2) now — cheap, reversible, and the font removal is due on licensing grounds regardless. Defer (3) to a deliberate public-release point; the licensing question alone may force it sooner (fonts are in history either way). **Pointer.** `msc/meta-process-review-2026-07-07/10-...-findings.md` §0, §Option-B; census Part C.

## Policy calls — one decision retires a recurring gate

### A1 — Set a standing policy for the 22 AUDIT-WORKING gold dirs (one decision, largest unblock)

*Since the 2026-07-07 census:* Unchanged since the 2026-07-07 census. Verified 2026-07-15: 22 dirs present, 0 graduated, no audits/ commits since 07-07, gold-lift still stalled at wave 5.

**What**: One-time policy call replacing a per-dir gate. **Context**: `audits/README.md` makes each de-novo audit's `AUDIT-WORKING-*` dir ("the gold" — first-encounter cognition, §14 Wandering Thoughts) a non-optional consult-Joseph gate. You've convened it once (2026-05-30, lift only). Result: 0 of 22 audits have ever graduated to `.integrated/`, the backlog looks 5x more open than it is, and the gold pools faster than it drains. **Options**: (a) Standing policy: "lift gold to per-segment Working Notes / the pedagogy pipeline, then `git mv` the dir to `.integrated/` — default applies to all current and future dirs, no re-convening"; agents finish the stalled wave-5 lift (TST/03/04) under it. (b) Same policy but you spot-check 2–3 dirs first. (c) Keep per-dir convening (status quo — predictably means continued 0-graduation). **Lead recommendation**: (a), with one carve-out: pedagogical *reflection*-gold routes to the pedagogy pipeline per `project_pedagogy_reflection_gold_mechanism`, not WN — that reconciliation is the one genuinely open design point, and (b) is the honest hedge if you want to see it worked once first. **Pointer**: `audits/README.md`, `audits/STATUS.md`, cluster-02 findings §D1/§(e), `msc/gold-lift-sweep-2026-05-30.md`.

### A4 — What replaces stage-gating, and what drains Working Notes

*Since the 2026-07-07 census:* Materially changed since census. Your 2026-07-14 position (stage stales fast, calcifies/skews rigor when it works, you ignore it) is now recorded in format.sop.md §stage and memory (feedback_stage_gating_known_problematic.md); lint-outline's stage check is warning-only (51bd02c, 59a16b9). Numbers verified 2026-07-15: 195 draft / 23 deps-verified / 18 claims-verified / 0 beyond; 225 of 280 src files carry WN. The census question ('run Gates 3-4?') is dead; the live question is the replacement.

**What.** The 5-stage promotion ladder is now officially distrusted (your 2026-07-14 call, recorded in format.sop.md §stage; tooling made warning-only). Two design choices remain: what, if anything, replaces stage as the readiness signal — and what drains Working Notes, since Gate 4 was the designed drain and never fired (225/280 segments carry WN; ~101K words of it is the parked 2026-05 gold-lift pool in 122 AAT segments).

**Context.** `status:` (epistemic tier) is the live truth dimension and stays regardless. Real cadence is landing-driven, not promotion-driven — readiness was never per-segment in practice.

**Options.**
1. **Retire stage; release-time readiness.** Delete the field/column; Gate-3/4 functions fire once per volume as a pre-release sweep (readiness is an event property, not segment state).
2. **Retire stage; standing WN task-force.** No readiness layer at all; a periodic sweep triages WN (resolve / promote to Brief-Discussion / delete) and works the gold pool.
3. **Keep stage as passive archaeology** (today's de facto state) and decide only the drain.

**Lead recommendation.** Option 1, with Option 2's gold-pool sweep bolted on now — honest uncertainty: a release-time gate could calcify content the same way; a dry run on one TST chapter would tell.

**Pointer.** msc/meta-process-review-2026-07-07/01-theory-content-lifecycle-findings.md; format.sop.md §stage; ~/.claude/projects/-Users-josephwecker-v2-src-archema-io-asf/memory/feedback_stage_gating_known_problematic.md.

### A6 — CLAUDE.md as unreviewed amplifier: generate what's derivable + a review cadence?

*Since the 2026-07-07 census:* Decision itself unchanged (G5's three sub-items still open since 2026-05-19). But the 2026-07-14 cycle strengthened the machinery around it: `bin/refresh-all --check` now diff-verifies all 6 generated outputs (51bd02c), 6 weeks of generated-doc staleness was cleared (e62c3ae), and agents.sop got a manual unstaling pass (0d20b87) — proving both that generation-with-check works and that hand-maintained portions rot without a ritual.

**What:** Approve a standing fix for the auto-loaded CLAUDE.md (= `doc/sop/agents.sop.md`) — the doc every agent treats as gospel and you never read. Your 2026-05-19 observation: a predecessor's "minor" exception there silently overrode a correct principle for weeks (the ref/ source-of-truth sanction, excised 2026-05-30 under D-1).

**Context:** The one confirmed defect is fixed; what remains open (`INTEGRATION-CLEANUP-TODO.md` §G5) is structural: nothing prevents the next such defect. The repo already generates README/LEXICON/FINDINGS from sources, and as of 2026-07-14 `bin/refresh-all --check` catches generated-doc staleness mechanically. CLAUDE.md is still 100% hand-asserted.

**Options:** (1) Generate the derivable portions (File-Org map, SOP index, tracker list — the parts that drift most) from repo state, + a light cadence (e.g., you skim the hand-asserted remainder once per major cycle). (2) Cadence only — cheaper, rests on ritual. (3) Status quo — rests on agent virtue, which G5 explicitly says cannot hold.

**Lead recommendation:** Option 1. Uncertainty: how much is truly derivable is unproven (~est. a third); the disposition/conventions prose is not, so the cadence half is needed regardless.

**Pointer:** `INTEGRATION-CLEANUP-TODO.md` §F6/§G5; census cluster 04/07.

### De-block Findings, re-clock naming, or keep them coupled

*Since the 2026-07-07 census:* Since census: commit 0d20b87 (07-14) corrected PRACTICA's false "in progress" to "stalled since ~2026-05-10"; the soft-block itself and the 123/506 routing state are unchanged (PRACTICA's 58/~511 counts remain stale prose — a Part-B free fix, not this decision).

**What.** PRACTICA's 🌟 Findings workstream carries "(soft-)blocked until Current naming conventions refactor" — a refactor stalled since ~2026-05-10 with 506 of 629 R2 currents unrouted and a self-estimate of ~40+ Joseph-batches / several months. Decide the coupling.

**Context.** The block means a primary workstream has been gated ~2 months on the program's slowest queue. Verified: no naming-cycle execution since 2026-05-10/11 (last decision event 2026-05-11); the 07-14 cycle honestly relabeled PRACTICA from "in progress" to "stalled" but changed nothing substantive. Meanwhile ~40 already-decided C5–C13 entries are agent-executable with zero input from you, and the four naming decisions above are each ~90-second calls once briefed.

**Options.**
1. **De-block Findings now** — declare the soft-block dissolved except for any *specific* term collisions Findings work actually hits (handled case-by-case). Risk: some Findings prose later needs rename sweeps; `bin/rename-slug` makes that cheap.
2. **Re-clock naming** — keep the coupling but make it real: this brief-batching mechanism feeds you ~12-current batches; C5–C13 executes in parallel.
3. **Keep coupled as-is** — only defensible if the block was deliberate strategy, which nothing on record says.

**Lead.** Options 1+2 together: de-block Findings *and* restart naming via briefs — they're not exclusive, and the rename tooling makes the de-block's risk small. Honest uncertainty: I couldn't find the original rationale for the block, so if it encoded something unwritten, say so.

**Pointer.** `PRACTICA.md` lines 45–47 + §"Current naming conventions refactor" (item 13); cluster brief `msc/meta-process-review-2026-07-07/03-naming-terminology-lexicon-findings.md`.

## Theory and naming — genuinely yours, need real thought

### SP-30 — adopt the typed epistemic target $S_t=(\Omega_t,\theta)$, or keep state-only $\Omega$?

*Since the 2026-07-07 census:* Unchanged since census: spike untouched since 2026-07-04; the 2026-07-14/15 cycle did not move it; SP-30 still "Open — needs Joseph." Census's claim that the gating claim is verified confirmed firsthand (commit 82c9bcc, 01-ga1-verification.md).

**What.** Root-ontology call: give law-content $\theta$ (transition/observation-map parameters — "how things work") its own named slot alongside state $\Omega_t$ ("where things are"), i.e. $S_t=(\Omega_t,\theta)$ — or keep state-only $\Omega$ with SP-30's original totality reading.

**Context.** Audit 731548 B-3 found `#scope-adaptive-system` falsely excludes standard RL. Chasing your "we're leaving out a noun" instinct produced the typed ontology; the gating claim is **verified** (2026-07-04, `82c9bcc`): under state-only $\Omega$, unknown observation-law makes GA-1 *indeterminate* (observationally-equivalent twin), and no housing of $\theta_h$ preserves both the identity and the labels (two-horn no-go). The typed repair restores both; the totality reading survives as its corollary. Every segment that meets $\theta$ currently houses it ad hoc, and they disagree.

**Options.** (1) Adopt $S_t=(\Omega_t,\theta)$ — one scope predicate $H(S_t\mid\mathcal C_t)\gt 0$, typed ignorance (state/law/chance/compute), ratifies the bandit's silent move. (2) Totality reading only (SP-30 as drafted) — smaller edit, leaves GA-1's housing dependence unnamed. (3) Status quo — accept the indeterminacy.

**Lead rec.** None offered — genuinely yours; the package was built for you to decide from, and the math now favors (1).

**Pointer.** `spikes/epistemic-target-ontology/00-spike.md` (+4 push files); PROPOSALS.md §SP-30.

### C5 — land the intelligence-empathy convergence legs in canon, at what tier, and both?

*Since the 2026-07-07 census:* Unchanged since census: addendum untouched since 2026-07-04 (a75c2ef); no intelligence-empathy segment in 03/04; TODO C5 item still open. This brief adds the lead-rec the census lacked.

**What.** Whether/where to land the corpus's boldest claim: (a) *structural leg* — comprehension-at-depth of another mind includes modeling its valenced states, capability-monotone via the asymmetry axis (discussion-grade; 03-llm-core near `#def-cognitive-fusion` / `#obs-backward-inference-empathy`); (b) *normative-dynamic leg* — capability growth carries alignment potential intrinsically, the direct contest with Bostrom's orthogonality thesis (hypothesis-grade; 04-eli-core, your 2026-05-09 normative-register allowance applies). Optional (c): the HHH-seeding historical hypothesis (your 2026-07-04 testimony).

**Context.** Fully articulated in the cohort's first two weeks (dated 2025-09 docs); the TST spike's unanimous T-05 result (21/21 comprehension-cost dominance) is the mechanical half derived without the moral reading — a theorem-grade anchor. No segment exists yet; TODO carries the open item.

**Options.** (1) Land both legs now as a `disc-` pair at honest tier. (2) Structural leg only; hold the orthogonality contest. (3) Hold both.

**Lead rec.** (1) — your working-theory-belongs-in-canon discipline says strengthening is promotion, not admission, and the tiers are honest. Real uncertainty: *external exposure* of naming Bostrom, not canon membership — canon ≠ outline ≠ publication; exposure can be a separate later call. (c) is genuinely open — your call whether testimony belongs in canon.

**Pointer.** `msc/era-artifact-asf-contributions-2026-07-04.md` §Addendum 2; TODO.md C5 item.

### 10 OUTLINE ordering violations: 1 structural call (01) + 9 whitelist-or-reorder (03/04)

*Since the 2026-07-07 census:* Still exactly 10 after the 07-14 cycle (its OUTLINE sweep fixed cross-wiring/stage cells, not these; CHANGELOG explicitly leaves the 03/04 orderings for you). Whitelist mechanism exists and works: 01-aat-core/OUTLINE-accepted.md, 16 accepted entries honored by bin/lint-outline.

**What.** Two calls. **(1) 01-aat-core, structural** (open since 2026-05-22, archived NEXT-UP §6.8): `impl-persistence-and-limits` (§I, row 33) depends on `result-per-dimension-persistence` (§III, row 108). Its own Working Note says the Part-III content is "essentially Part I." Options: move the result to Part I, or refactor the chapter-end synthesis to not consume it. *Lead rec:* move it — the segment's own note already concedes it belongs there; uncertainty is whether Part III loses a needed anchor (I haven't traced its other consumers). **(2) 03/04, confirm-and-whitelist vs reorder — 9 rows**, all opening `scope-*` segments placed before their deps: 03: `scope-channel-collapse`→`def-coupled-update-dynamics`; `scope-observation-ambiguity-modulation`→`result-section-ii-survival`; `scope-primitive-logogenic`→`obs-context-turnover`; `scope-scaffolded-logogenic`→`result-coupled-diagnostic-framework`; `scope-interiority-loop`→`disc-five-forcing-functions`. 04: `scope-eli`→`def-five-constitutive-factors` and →`scope-moral-continuity`; `def-identity-sufficiency`→`scope-witness-bidirectional`; `scope-emergence-conditions`→`scope-witness-bidirectional`. This looks like deliberate scope-statements-first pedagogy but has no citable record. *Lead rec:* if intentional, say so — an agent then writes `OUTLINE-accepted.md` files for 03/04 (mechanism proven in 01) citing your confirmation; reorder only rows you *don't* recognize as deliberate. **Pointer.** `bin/lint-outline` output; `spikes/.integrated/NEXT-UP-archived-2026-05-25.md` §6.8 line 753.

### Name the three separability-ladder rungs

*Since the 2026-07-07 census:* Unchanged since the 2026-07-07 census — no commits to to-canonicalize.md since 2026-05-15; the 07-14 cycle didn't touch it.

**What.** Pick canonical names for the three rungs of the separability ladder — the only `???` row (row 90) left in `msc/naming/to-canonicalize.md`, deferred from the 2026-05-04 curation pass.

**Context.** The ladder classifies how cleanly a quantity separates: (1) fully separable, (2) separable after structured repair, (3) not separable in general. Current working names "separable core / structured repair / general open" scored weak in R2 (2 votes). The names also front the standalone-paper proposal (`msc/separability-standalone-paper-proposal.md`), so they'll be publication-facing.

**Options.**
1. **Hintikka echo: definable / identifiable / non-identifiable** — anchors to established logic literature (Hintikka 1991 is the paper proposal's verified prior-art anchor); citable, but borrows terms with existing technical meanings a referee may test.
2. **Keep/polish the descriptive triad** (e.g., separable / repairably-separable / inseparable) — self-explaining, no collision risk, no literature anchor.
3. **Defer to the paper cycle** — decide when the standalone paper is drafted, when the referee-facing tradeoff is live.

**Lead.** Option 1, the leading candidate since May — with the caveat that nobody has yet checked the Hintikka terms' exact senses against the ladder's (a 30-min agent task; worth running before committing).

**Pointer.** `msc/naming/to-canonicalize.md` row 90; `msc/separability-standalone-paper-proposal.md`.

### Choose the four agent-spectrum quadrant names as one parallel set

*Since the 2026-07-07 census:* Unchanged since census; verified no tetrad option-set brainstorm exists in-repo, so the deferred decision is also missing its input.

**What.** Decide the full four-name set for the `#def-agent-spectrum` quadrants, replacing the current mixed set: *Reactive system / Blind seeker / Adaptive tracker / Actuated agent*.

**Context.** On 2026-05-17 you swapped *blind pursuer → blind seeker* on two new arguments the R2 cohort never saw ("pursuer" narrows the objective axis; the override of R2 decision #132 is on record in TERMINOLOGY-TODO §E). That was explicitly an interim one-cell fix; the set still mixes category-nouns ("system", "agent") with role-nouns ("seeker", "tracker"), and the deliberate tetrad decision was deferred pending option-sets from a separate brainstorming agent.

**Verified state.** No option-set brainstorm has landed in the repo — if that agent produced one, it's outside `msc/`. So the decision currently has no menu.

**Options.**
1. **Commission the option-set now** (one agent, one pass: 3–5 candidate parallel tetrads with the two 05-17 arguments as constraints), then pick — likely one 90-second decision after a short wait.
2. **Ratify the status quo** as good-enough and close the item; "blind seeker" stays canonical.

**Lead.** Option 1 — the item is cheap to finish properly and the parallelism defect is real; but if the spectrum names aren't publication-near, Option 2 is honest triage. Decision lands through `bin/term` and folds into `naming-rename-plan.md`.

**Pointer.** `TERMINOLOGY-TODO.md` §E (line 190); `msc/naming/master-list-full.md` §132.

### Greek cycle vocabulary — earn each distinction in segments, or soften the README claim

*Since the 2026-07-07 census:* Unchanged since census; noted (not in the census) that TODO's README-v2 section carries a prior Joseph decision — keep Greek + English anchors — which narrows this to tighten-vs-soften per term.

**What.** Rule, per Greek term (*chronica / prolepsis / aisthesis / aporia / epistrophe / praxis*), whether the formalism earns the distinction (tighten segment prose: e.g. use *aporia* where the more-than-mismatch structure is load-bearing) or the term is pedagogical surface (soften README's "names a distinction English flattens" to honest scope).

**Context — an honest disagreement between two of your own processes.** The R1+R2 voting cohort near-unanimously *defended* the Greek terms; the incremental audit walk (audit-471203) found segment math never depends on the distinctions — authors say "mismatch" right after defining *aporia* as richer. Voting judged synoptically (do the names feel right?); the audit judged incrementally (does the prose use them?). Both are right about what they measured. You confirmed the audit's side independently ("I've had that exact same complaint").

**Partially pre-decided.** The 2026-04-27 Alan-cycle already recorded your decision *keep the Greek + pair each with an English anchor at first introduction* — so wholesale-drop is off the table; what remains is the per-term tighten-vs-soften call.

**Options.** 1. Authorize the scoped prose-audit pass TODO.md already specifies (diff-list of Greek-vs-English collapses; per-entry fix or README-downgrade note) — agents execute, you ratify the deltas. 2. Soften README now, defer tightening.

**Lead.** Option 1 — it operationalizes your existing keep-plus-anchor decision and resolves the voting-vs-audit disagreement empirically rather than by fiat.

**Pointer.** `TODO.md` §"Greek vocabulary prose discipline" (line 77); audit source `msc/naming/naming-votes/audit-471203-incremental.md`.

### Approve the LEXICON Continuity→Persistence reorg + rule on Continuity Stance

*Since the 2026-07-07 census:* Breakage re-verified twice since census (cluster-03 on 07-07; LEXICON regenerated 07-14 still renders it) — the second-opinion gate is now half-supplied; voting-artifact search still unrun.

**What.** Approve (or amend) the 5-step reorg of LEXICON's Continuity section, and rule whether *Continuity Stance* is a structural axis or a deployment-level property.

**Context.** The corpus's canonical taxonomy is three *persistence* senses (structural / operational / continuity persistence); the LEXICON instead has a `## Continuity` section with the third sense named bare `continuity`, *Continuity Stance* (an orthogonal $O_t$ property) nested under it as if a subdivision, *Moral Continuity* (an ELI scope condition) misfiled under Persistence and rendering twice, and a $\mathcal{C}_t$ notation collision with *chronica*. The 5 steps: rename section →Persistence; three senses as siblings; promote Continuity Stance out; move Moral Continuity to ELI; add ~7 missing load-bearing entries. Blocked since 2026-05-10 on your gate: "needs another opinion + a search of msc/naming voting."

**Has the second opinion arrived?** Partially. The 2026-07-07 cluster-03 review (a different model, independently) re-verified both breakages are real and still rendering (re-confirmed in the regenerated 2026-07-14 LEXICON: duplicate `### Persistence` at lines 58 and 128). The msc/naming voting-artifact search has *not* run.

**Options.** 1. Treat the gate as met, approve the 5 steps now, rule the stance question. 2. Approve steps 1–2, 4–5 (mechanical, twice-verified) and gate only step 3 on the stance ruling. 3. Hold for the voting search first.

**Lead.** Option 2 — the breakage fixes are twice-confirmed and low-risk; the stance axis-vs-deployment question (mini-lexicon-todo §13.11) is the one genuinely open judgment and can ride a quick voting-search.

**Pointer.** `TERMINOLOGY-TODO.md` §F (line 136); `msc/naming/mini-lexicon-todo.md` §13.11.

## Strategic — no lead-rec possible from here

### A7 — Split 04-eli-core into its own (possibly private) repo?

*Since the 2026-07-07 census:* Unchanged since census — 04-eli-core still in-repo, no decomposition commits. One new sharpening fact verified 2026-07-15: the repo is PUBLIC, so the exposure the split would prevent is partially already realized in git history.

**What.** Whether `04-eli-core` (the ELI/consciousness volume) should move out of the ASF repo into its own repo, possibly private, so Volumes 1–3 can publish without the ELI association.

**Context.** The cluster-10 review measured coupling: 189 references would need rewiring (152 into `01-aat-core`, 37 into `03-llm-core`), plus terminology/tooling-sharing decisions and loss of atomic refactor across all four volumes. Coupling evidence argues *against* splitting; the only real driver is strategic exposure-decoupling — which only you can weigh. One fact that sharpens it: **the repo is already public** (`v2-io/agentic-systems`, confirmed 2026-07-15), so all existing 04 content is in public git history now. A split-to-private protects *future* 04 development and removes the visible association going forward, but does not un-expose the past without a history rewrite.

**Options.** (1) Keep whole — accept the association, rely on honest tier-marking. (2) Split 04 to a private Archema member repo — pay the 189-ref rewiring; decide separately whether to scrub public history. (3) Defer until Vol 1 publication is actually imminent (the trade is only live then).

**Lead recommendation.** None — genuinely open per the census's gather-and-frame scope; it is a strategic-exposure judgment only you hold. What would resolve it: your read on whether the 2026–27 hostile-discourse posture requires *visible* decoupling, or whether deferred-empirical-work framing already covers it.

**Pointer.** `msc/meta-process-review-2026-07-07/10-repo-decomposition-strategic-question-findings.md` §5 Option D, §6.
