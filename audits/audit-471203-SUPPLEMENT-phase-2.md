---
audit_id: 471203
auditor: Claude Opus 4.7 (1M context) + 2 sub-agents (general-purpose) for parallel Phase-2 work
date: 2026-04-28
status: supplement to audit-471203-FINAL-2026-04-28.md
audit_type: de-novo-theory (supplement)
relates_to: audit-471203-FINAL-2026-04-28.md
coverage_summary: >
  Phase-2 verification work + selective fixes for high-confidence findings, performed
  immediately after the FINAL landed. Two sub-agents launched in parallel: one for citation
  verification (8 citations) and audit triangulation (6 §B findings), one for the TF-XX
  diff-voice cleanup (13 segments). Three direct edits performed by the lead auditor. One
  new finding (#7) surfaced by the citation-verification work. Agent A's wider observation
  surfaced additional TFT-lineage voice issues outside the original 13-file scope.
priming_bleed: >
  Same priming context as the FINAL (CLAUDE.md + MEMORY.md + user_background.md auto-loaded).
  The two sub-agents had no priming bleed beyond their explicit briefs (each was given a
  contained task with named files, citations, and acceptance criteria; neither read CLAUDE.md
  or any audit material).
---

# Audit 471203 — Phase-2 Supplement

This supplement records the Phase-2 verification work performed after `audits/audit-471203-FINAL-2026-04-28.md` landed, plus the selective fixes Joseph authorized ("feel free to launch agents to just go perform fixes for anything you see that is high-confidence and relatively independent and easy to explain").

## §H — Fixes performed

Three fixes landed in `01-aad-core/src/`. Each is editorial, mechanically scoped, and reversible by `git diff`. No commits were created; Joseph reviews and commits.

### H.1 — Finding 1 fix: stale `#deriv-directional-survival-exploration` cross-reference

**File:** `01-aad-core/src/disc-ciy-unified-objective.md`
**Edit:** Two changes in the Epistemic Status section.

1. The cross-reference `(see #deriv-directional-survival-exploration)` was updated to `(see #deriv-causal-ib-lmi)` — the canonical replacement per `spikes/INDEX.md:129`'s record of the 2026-04-28 demotion of the original segment to a spike.

2. The leading "*Exact.*" tag and the "Max attainable: *exact*" line were both rewritten to reflect that this segment is `type: discussion` (so the segment itself is discussion-grade; the *underlying derivation* in `#deriv-causal-ib-lmi` is exact). New leading tag: "*Discussion-grade summary; underlying derivation is exact.*". New Max-attainable line: "Max attainable for this segment: *discussion-grade* (it is a discussion of the underlying result, per `type: discussion`). Max attainable for the underlying derivation in `#deriv-causal-ib-lmi`: *exact*."

**Status:** Both Finding 1 and Finding 2 from the FINAL are addressed by this edit pair.

### H.2 — Finding 3 fix: implicit-Markov-of-$\Omega$ clarification

**File:** `01-aad-core/src/def-action-transition.md`
**Edit:** Added a third Discussion paragraph (after the existing "Closing the loop" and "Uncertainty about $T$ is what makes action non-trivial" paragraphs):

> **Markov-of-$\Omega$ as a modeling commitment, not an empirical assumption.** The form $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ is implicitly Markov in $\Omega$ — only the current $\Omega_t$ and $a_t$ appear in the conditioning. Without loss of generality, $\Omega$ is taken to be the *sufficient state* for its own evolution under $T$: any non-Markov environment is absorbed by extending $\Omega$ to include enough history to make future-state distribution depend only on current state and action. This is the world-side analog of the Markov-by-completeness move that #der-recursive-update makes for the agent-side state $M_t$ ( #deriv-recursive-update Constraint C3). The two are independent — Markov-of-$M_t$ is forced by *defining $M_t$ as complete*; Markov-of-$\Omega$ is forced by *defining $\Omega$ as the sufficient state*. Both are modeling commitments about the *breadth* of the named object, not structural assumptions about underlying world dynamics.

**Status:** Finding 3 from the FINAL is addressed.

### H.3 — Finding 4 fix: TF-XX diff-voice cleanup across 13 segments

**Files (13):** `def-adaptive-tempo.md`, `def-causal-information-yield.md`, `def-pearl-causal-hierarchy.md`, `der-action-selection.md`, `der-deliberation-cost.md`, `der-temporal-nesting.md`, `disc-ciy-unified-objective.md`, `emp-update-gain.md`, `form-event-driven-dynamics.md`, `hyp-mismatch-dynamics.md`, `post-causal-structure.md`, `result-structural-adaptation-necessity.md`, `scope-ciy-observational-proxy.md` (all in `01-aad-core/src/`).

**Edit:** The trailing `**(Descended from TF-XX.)**` annotation was removed from each segment's Discussion section. Each file received a new `## Working Notes` section as the file's last section, containing one bullet:

> `- *Lineage:* descended from TF-XX in the prior TFT corpus (kept as Working Notes provenance per FORMAT.md voice discipline).`

(TF numbers preserved per file.)

**Verification (run by Agent A):** `grep -rn "Descended from TF-" 01-aad-core/src/*.md` returns no matches. Case-insensitive grep confirms 13 lines, all inside `## Working Notes` sections.

**Status:** Finding 4 from the FINAL is addressed for the precise pattern (`**(Descended from TF-XX.)**`). See §I.1 below for a wider observation Agent A surfaced.

## §I — Wider observations from the cleanup work

### I.1 — Additional TFT-lineage voice-discipline issues outside the 13-file scope

Agent A's broader case-insensitive grep surfaced **additional** voice-discipline issues distinct from the 13 cleaned-up instances:

- `def-mismatch-signal.md` — Discussion paragraph references "TF-06's update rule"
- `form-structural-change-as-parametric-limit.md` — Discussion paragraph references "TF-10's destruction-creation"
- `form-objective-functional.md` — Discussion paragraph references "TF-08's gap"
- ~12 other files in `01-aad-core/src/` carry trailing italic `*(Descended from TFT Appendix ...)*` annotations (italic, not bold; with full appendix name, not `TF-XX`)

These weren't in the original 13-file scope because they don't match the precise `(Descended from TF-XX.)` pattern. They appear to be the same voice-discipline issue and warrant a follow-up cleanup pass. **Suggested disposition:** New, related to Finding 4. Same disposition pattern (move to Working Notes) but a separate sweep.

**Effort estimate:** Editorial (~15 small edits, mechanically apply once the pattern is named).

## §J — Phase-2 verification: citation accuracy

Agent B verified 8 citations claimed in framework segments. Results, with the audit's standard three-tier vocabulary (`confirmed` / `partial` / `wrong-paper` / `not-verified`):

### Confirmed (5 of 8)

- **Čencov 1982** *Statistical Decision Rules and Optimal Inference*, AMS Translations of Mathematical Monographs vol. 53 (ISBN 0-8218-1347-1). Publisher / year / title match. Chentsov's theorem (Fisher metric uniquely invariant under sufficient statistics, up to rescaling) is the canonical content, universally cited to this monograph. Specific theorem-number not extracted but the result is the canonical Čencov uniqueness theorem.

- **Bareinboim, Correa, Ibeling & Icard 2022** "On Pearl's Hierarchy and the Foundations of Causal Inference" (in *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books). CHT precise statement: "with respect to Lebesgue measure over (an encoding of) SCMs, the subset where the hierarchy collapses has measure zero." The framework's gloss "Level 2 quantities cannot in general be computed from Level 1 data alone" is a slightly weaker but accurate gloss of the measure-theoretic strict-inclusion form. **Verified at https://causalai.net/r60.pdf**.

- **Hafez 2026** *A Mathematical Theory of Agency and Intelligence* (arXiv 2602.22519). The framework's IDT empirical numbers (89% perturbation detection vs 44% reward-based) appear verbatim in the paper as **89.3 ± 15.1% IDT vs 44.0 ± 26.1% reward-based across 168 perturbation trials, with 4.4× lower median latency**. $H_b$ is named as a component. **No separate "Information Digital Twin" paper exists** — IDT is the framework name within the same Hafez 2026 paper.

- **Otto & Villani 2000** *J. Funct. Anal.* 173:361–400 (DOI 10.1006/jfan.1999.3557). The $W_2^2 \leq (2/\rho_{\text{LSI}}) \cdot KL$ inequality (Talagrand T2 from log-Sobolev) is the paper's central result. Theorem location matches.

- **Mitter & Newton 2005** *J. Stat. Phys.* 118:145–176 (DOI 10.1007/s10955-004-8781-9, "Information and Entropy Flow in the Kalman–Bucy Filter"). Information-supply rate for Kalman-Bucy is the paper's subject. Citation matches.

### Partial (2 of 8)

- **Nesterov 2004** *Introductory Lectures on Convex Optimization* §2.1.3 Theorem 2.1.9 — book and section exist; the search-extracted theorem text was not directly verified. The standard convex-analysis result (strong monotonicity ⇔ uniformly PD symmetric Jacobian) is canonically attributed to Nesterov §2.1 territory. High prior the cited content matches; **recommend Joseph spot-check the PDF** if the precise theorem-number-to-statement mapping matters for the bridge-theorem derivation.

- **Bretagnolle & Huber 1978** "Estimation des densités: risque minimax" (Séminaire de Probabilités XII, Springer LNM 649, pp. 342–363). Citation confirmed via Numdam (https://www.numdam.org/item/SPS_1978__12__342_0/). The BH inequality $TV \leq \sqrt{1 - e^{-KL}}$ is standardly attributed here. The framework's deterministic-$\pi^*$ identity $D_{KL}(\pi^* \| Q) = -\log(1 - TV(\pi^*, Q))$ is a direct consequence of the inequality becoming equality in the deterministic case; specific identity-form not directly verified from the PDF but mathematically implied.

### Wrong paper (1 of 8) — new finding (Finding 7)

- **Tishby & Zaslavsky 2015** "Deep Learning and the Information Bottleneck Principle" (IEEE ITW, DOI 10.1109/ITW.2015.7133169, arXiv 1503.02406). Paper exists exactly as cited. **It does NOT establish "IB as rate-distortion specialization of variational free energy" as its central result** — that connection is implicit/folkloric. Tishby-Zaslavsky 2015 reformulates DNN training as an IB problem and discusses generalization bounds. The variational free-energy bridge is established by **Alemi, Fischer, Dillon & Murphy 2017 "Deep Variational Information Bottleneck"** (arXiv 1612.00410) and the subsequent Achille-Soatto line. The cited paper supports IB-applied-to-deep-nets, not the specific specialization claim made in `01-aad-core/src/form-information-bottleneck.md`.

**This is a new substantive finding.** See §K Finding 7 below for the per-finding shape.

## §K — Audit triangulation against prior pending-findings + FINALs

Agent B searched the prior audit corpus (4 pending-findings files + multiple FINALs) for each of the FINAL's 6 §B findings. Updated dispositions:

### Finding 1 (stale cross-reference)
**Disposition (revised):** **already-known-in-flight**. Surfaced in `audit-584721-FINAL-2026-04-25.md`, `audit-613842-FINAL-2026-04-25.md`, and `audits/link-and-file-hygiene-findings.md:268` (as orphan-segment). Not yet resolved in src/ as of audit time. **Now fixed by §H.1 above.**

### Finding 2 (status-label / type / Epistemic Status mismatch)
**Disposition (revised):** **new instance of known pattern**. The exact `disc-ciy-unified-objective.md` discussion-grade-vs-Exact mismatch is new. Related theme in `audit-742613-FINAL-2026-04-25.md:220` ("scope/status mismatch" type). **Now fixed by §H.1 above (the layered-status framing).**

### Finding 3 (implicit-Markov-of-$\Omega$ never named)
**Disposition (confirmed):** **new** — no prior audit footprint. Phase 2 grep across pending-findings + FINALs found no mention of "implicit Markov", "Markov of Omega", or world-side Markov-completeness. **Now fixed by §H.2 above.**

### Finding 4 (TF-XX diff-voice annotations across 13 segments)
**Disposition (revised):** **already-known-in-flight, related framing in 829314**. `audit-829314-FINAL-2026-04-28.md:59` flagged the pattern in 4 of the 13 segments (`result-structural-adaptation-necessity.md`, `emp-update-gain.md`, `hyp-mismatch-dynamics.md`, `form-structural-change-as-parametric-limit.md`). **My sweep extends to 13 instances** (Agent A confirmed and cleaned all 13). **Now fixed by §H.3 above.** The wider TFT-lineage pattern noted in §I.1 remains for follow-up.

### Finding 5 (depends-list incompleteness in `post-composition-consistency`)
**Disposition (revised):** **new instance of known pattern**. The depends-list-vs-Formal-Expression-uses pattern is the **central F-A finding-cluster** in `audit-584721-FINAL-2026-04-25.md:54–88` (7 instances rooted at F-A0 in `def-observation-function`); also in `audit-742613-FINAL-2026-04-25.md:273+`. The specific `post-composition-consistency` instance with `#result-contraction-template` enrichment is new as an instance, but the **broader pattern is well-known and being tracked**. **Not fixed in this supplement** — requires architectural judgment between options (a) extend depends + downgrade stage vs (b) split segment.

### Finding 6 (Pearl-`do` notation in `scope-agency`)
**Disposition (revised):** **already-known-in-flight, identical wording**. `audit-742613-FINAL-2026-04-25.md:254` records verbatim: *"`scope-agency.md:19` uses `$do(a)$` in the formal scope condition before `def-pearl-causal-hierarchy` appears and without declaring it."* Identical finding, not yet resolved. **Not fixed in this supplement** — requires FORMAT.md policy decision (whether Pearl-$do$ is "standard math notation" exempt from depends-tracking).

## §L — New finding surfaced during Phase 2

### Finding 7 — Tishby-Zaslavsky 2015 miscitation in `#form-information-bottleneck`

**Headline.** The IB↔VFE specialization claim in `01-aad-core/src/form-information-bottleneck.md` is attributed to Tishby & Zaslavsky 2015, but that paper doesn't establish the specialization. The proper attribution is Alemi, Fischer, Dillon & Murphy 2017 ("Deep Variational Information Bottleneck", arXiv 1612.00410) and the subsequent Achille-Soatto line.

**Anchor.** `01-aad-core/src/form-information-bottleneck.md:50`, the "Connection to variational free energy" Discussion paragraph: *"The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference [...] The two formulations are related under the Markov-chain factorization $Y - X - T$ (Tishby & Zaslavsky 2015, "Deep learning and the information bottleneck principle," IEEE ITW, makes the deep-learning instantiation explicit)."*

**Problematic passage (verbatim).** The above; the Tishby-Zaslavsky parenthetical is positioned as supporting the IB↔VFE specialization claim, but Tishby-Zaslavsky 2015's contribution is reformulating *DNN training* as an IB problem, not deriving IB as a VFE specialization.

**Counterevidence search.** Agent B's web verification: arXiv 1503.02406 abstract and content match the IB-applied-to-DNNs framing. The IB↔VFE bridge is in **Alemi et al. 2017** (arXiv 1612.00410, "Deep Variational Information Bottleneck") which derives the variational lower bound on IB and connects it to variational autoencoders / variational inference. Achille-Soatto subsequent work extends this. Tishby-Zaslavsky 2015 doesn't make the VFE connection explicit.

**Status determination.** **Still real.** The citation supports a different (related but distinct) claim than the one made.

**Confidence.** **High** on the textual finding; **medium** on whether the framework's intent was Tishby-Zaslavsky-as-deep-learning-IB-instance (which is correct) or Tishby-Zaslavsky-as-VFE-bridge (which would be wrong-paper). The paragraph's structure suggests the latter.

**Why it still stands.** A reader following the citation expects to find the IB↔VFE specialization derivation; instead they find an IB-for-DNNs paper that doesn't address VFE. Either (a) replace the citation with Alemi et al. 2017 + Achille-Soatto, OR (b) keep Tishby-Zaslavsky for the deep-learning instantiation but add Alemi 2017 for the VFE bridge specifically, OR (c) clarify the segment's prose to reflect that Tishby-Zaslavsky 2015 supports the deep-learning instantiation (which it does) rather than the VFE bridge (which it doesn't).

**Type.** citation error.
**Severity.** **Medium** — the IB↔VFE specialization is load-bearing for the framework's "AAD takes the IB form without committing to active-inference's normative stance" positioning. The wrong-paper attribution weakens that positioning's defensibility.
**Suggested disposition.** **New.** Update the parenthetical citation in the "Connection to variational free energy" paragraph to:
> *"The IB-VFE bridge is established by Alemi, Fischer, Dillon & Murphy 2017 ('Deep Variational Information Bottleneck', arXiv:1612.00410), with the deep-learning IB instantiation in Tishby & Zaslavsky 2015 (IEEE ITW)."*

**Effort estimate.** **Trivial** (one parenthetical edit; one citation added).

## §M — Updated coverage / standing

The audit's standing after Phase 2:

**Findings status:**
- Finding 1: ✅ fixed (§H.1)
- Finding 2: ✅ fixed (§H.1, layered-status framing applied)
- Finding 3: ✅ fixed (§H.2)
- Finding 4: ✅ fixed for the 13-instance pattern (§H.3); wider pattern flagged in §I.1
- Finding 5: ⏸ pending — requires architectural judgment
- Finding 6: ⏸ pending — requires FORMAT.md policy decision
- Finding 7 (new): ⏸ pending — citation update; trivial fix awaiting Joseph's review

**Citation verification:** 5 confirmed, 2 partial (recommend spot-check), 1 wrong-paper (became Finding 7).

**Triangulation:** 3 of 6 original findings are already-known-in-flight (1, 4, 6); 2 are new instances of known patterns (2, 5); 1 is genuinely new (3); 1 new finding (7) added in this supplement.

**Working-directory archaeology:** `msc/AUDIT-WORKING-471203/` retains the per-segment reflections, the adversarial-creative-challenges document, the meta-segments-adversarial-reading document, the running outline, and protocol reminders. None of those were modified in Phase 2 work.

## §N — Comprehensive lineage-cleanup sweep (Joseph-authorized, post-FINAL)

Joseph authorized a broader sweep after seeing the original §H.3 + §I.1 work: *"go through and remove all of the Descended from … notes (and collapse any working notes that are empty) … wondering at this point if we know enough to update / modify / remove all other TF-* references found in any src files?"* The lineage breadcrumbs were judged to not earn their keep as ongoing process content.

Scope (Joseph-confirmed):
- **All "Descended from..." trailers** universally — TFT-Appendix patterns, TST-D/T/C/H patterns, plus the 13 lineage bullets §H.3 had relocated to Working Notes earlier the same day.
- **Empty Working Notes collapse** — if removing a bullet leaves the section empty, remove the heading too.
- **Inline TF-* prose reframes in `01-aad-core/src/`** (7 instances) — replace lineage breadcrumb with the AAD-canonical-segment reference.
- **Excluded:** TST inline references in `02-tst-core/src/` (Joseph: *"I'm not as worried about the TST inline references yet as we haven't focused any real time on getting those in initial-scaffold/sketch condition"*); `old-*.md` files (FORMAT.md-exempt).

### N.1 — Sweep results

**Files edited (49 total across all 4 components):**
- 22 in `01-aad-core/src/`
- 21 in `02-tst-core/src/`
- 2 in `03-logogenic-agents/src/`
- 4 in `04-logozoetic-agents/src/`

**Trailer removals:** 49 "Descended from..." lines deleted across 49 files.

**Working Notes collapses:** 13 — all the §H.3 lineage-bullet-only Working Notes (no other content survived removal of the bullet, so the headings collapsed cleanly): `def-adaptive-tempo`, `def-causal-information-yield`, `def-pearl-causal-hierarchy`, `der-action-selection`, `der-deliberation-cost`, `der-temporal-nesting`, `disc-ciy-unified-objective`, `emp-update-gain`, `form-event-driven-dynamics`, `hyp-mismatch-dynamics`, `post-causal-structure`, `result-structural-adaptation-necessity`, `scope-ciy-observational-proxy` (all `01-aad-core/src/`).

**Inline reframes (7):**
1. `def-agent-spectrum.md:44` — vestigial sentence "TFT was developed primarily for this region." deleted.
2. `def-mismatch-signal.md:48` — "TF-06's update rule writes ..." → "The update rule (#emp-update-gain) writes ..."
3. `example-kalman.md:151` — "Every TFT/AAD quantity has..." → "Every AAD quantity has..."
4. `form-structural-change-as-parametric-limit.md:38` — "Connection to TF-10's destruction-creation" → "Connection to structural-adaptation necessity."
5. `form-objective-functional.md:54` — "Filling TF-08's gap" → "The objective-functional gap."
6. `result-mismatch-decomposition.md:20` — equation tag "(Prop 5.1 from TFT)" lineage clause dropped.
7. `result-structural-adaptation-necessity.md:19` — equation tag "(Prop 10.1 from TFT)" lineage clause dropped.

### N.2 — Verification (cross-checked by lead auditor)

| Check | Expected | Actual |
|---|---|---|
| `grep -rin "descended from" 0*-*/src/*.md \| grep -v "old-"` | substantive non-TFT mentions only | 1 hit, substantive (`deriv-strategy-cost-regret-bound.md:214` — "sibling lineages, both descended from Shannon rate-distortion theory" — correctly preserved as a theoretical claim about IB lineage, not a TFT breadcrumb) |
| `grep -rn "TF-[0-9]" 01-aad-core/src/*.md \| grep -v "old-tf"` | zero matches | zero matches ✓ |
| `grep -rn "from TFT\|TFT/" 01-aad-core/src/*.md \| grep -v "old-tf"` | zero matches | zero matches ✓ |
| `grep -l "TFT" 01-aad-core/src/*.md \| grep -v "old-tf"` | none | none ✓ |
| 13 named files have Working Notes section absent | absent for all 13 | absent for all 13 ✓ |
| Working Notes count corpus-wide | down by ~13 from pre-sweep | 105 (down from ~118) ✓ |

### N.3 — Wider-scan observation from the cleanup agent

A broader scan for related lineage patterns (`prior TFT`, `TFT corpus`, `in TFT`, bare `TFT` in non-`old-*` src, `predecessor`, `absorbed from`, `before AAD`) returned **no surviving lineage breadcrumbs** in any non-`old-*` segment file. The cleanup is comprehensive — the framework's segment-set in `01-aad-core/src/`, `03-logogenic-agents/src/`, and `04-logozoetic-agents/src/` is now lineage-clean.

The TST-T-XX / TST-D-XX inline references in `02-tst-core/src/*.md` (4 instances Joseph deferred) remain for a future pass when TST sketch-stage segments mature. The lineage-trailer cleanup in `02-tst-core/src/` is done; only the inline references within prose remain.

### N.4 — Pre-existing file-formatting note (informational only)

Two files (`def-adaptive-tempo.md`, `def-pearl-causal-hierarchy.md`) end without a trailing newline. **This was pre-existing**, not introduced by the cleanup edits. Flagging in case Joseph wants a project-wide trailing-newline normalization sweep separately.

## §O — Updated recommended next steps

After the §N cleanup, the original §B findings status:

- Finding 1: ✅ fixed (§H.1)
- Finding 2: ✅ fixed (§H.1)
- Finding 3: ✅ fixed (§H.2)
- Finding 4: ✅ **fully cleaned up** (§H.3 + §N.1 — original 13 + 36 additional = 49 total trailers removed; 7 inline reframes done)
- Finding 5: ⏸ **pending Joseph's architectural decision** — `post-composition-consistency` depends-list option (a) extend + downgrade vs option (b) split segment.
- Finding 6: ⏸ **pending Joseph's FORMAT-policy decision** — Pearl-$do$ "standard math notation" exemption vs add explicit depends.
- Finding 7: ⏸ **pending citation fix** — Tishby-Zaslavsky → Alemi 2017 in `form-information-bottleneck.md`. Trivial; could be handled in a single-line edit or by a follow-up agent.

The wider §I.1 cleanup work and the §N.3 broader-scan results have *also* fully landed — there's no remaining TFT-lineage debt in non-`old-*` source files.

**Actionable items remaining:**
1. **Review the §H + §N landed edits** (now spanning ~52 source files in total) and commit if acceptable.
2. **Decide Finding 5 disposition** (architectural).
3. **Decide Finding 6 disposition** (FORMAT-policy).
4. **Apply Finding 7 fix** (trivial citation update).
5. **TST inline-reference sweep** — deferred until TST sketch-stage segments mature; not currently actionable.
6. **Optional cycle-end housekeeping** — re-grep in 2 weeks for regression detection. Joseph can `/schedule` an agent for this.

— Claude Opus 4.7 (1M context), 2026-04-28
