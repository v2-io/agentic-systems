---
source_cycle: 451729 (de-novo, Claude Sonnet 4.6 (1M context), 2026-05-10)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-451729/ (18 files — 00-initial-predictions + 00-running-outline + 16 batch reflections)
final_of_record: audits/audit-451729-FINAL-2026-05-10.md (NOT in `.integrated/` — open on D.1)
manifest_entry: audits/.integrated/MANIFEST.md "audit-451729-FINAL-2026-05-10 does NOT graduate — stays open on D.1 residual"
todo_entry: TODO.md §"2026-05-10 — Audit-findings intake: 451729 — remaining open item"
ledger_entries: audits/polish-and-sentiment-ledger.md S25 (research-seed, §F.1–F.3 / §D.2 soft set), S28 (polish, §D.3 schema-strategy-persistence approximation note)
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. The original working dir is preserved separately;
  this file is the "what is in there worth processing" digest.
---

# Audit-findings extract — 451729 working-dir mining

The 451729 cycle was a substantial de-novo walk by **Claude Sonnet 4.6 (1M context)** on 2026-05-10. Per Joseph's modification, the auditor used a **5-segment batch reflection cadence** (one reflection file per 5 OUTLINE-ordered segments) rather than the standard one-file-per-segment cadence. The dir contains 18 files: `00-initial-predictions.md` (15 falsifiable predictions across six themes), `00-running-outline.md`, and 16 batch reflection files (`01-batch-01.md` through `01-batch-16.md`) covering ~97 segments first-hand. Coverage: complete Section I (29) + complete Section II (29) + 16/21 Section III + 7 key Appendix A derivations + 1 TST sample + 1 logogenic sample + 0 ELI.

The FINAL surfaced **one Burden-of-Proof finding** (Prop B.4 subscript transposition, medium severity), **five rescinded candidates** (where strengthen-before-soften discipline operated visibly to dismiss soften-recommendations), **three hypothesis-tier observations** (§D.1 promotion-readiness sweep, §D.2 `result-unity-closure-mapping` joint structure sketched, §D.3 `schema-strategy-persistence` approximation note), **four bigger-picture observations** (§F.1–§F.4), and explicit process-feedback (§G.1–§G.4 endorsing the §4.4 wandering-thoughts prompt structure and flagging the 1M-context triage-mode threshold).

Per the 2026-05-15 routing pass: **Finding 1 (Prop B.4) landed surgically** (verified first-hand below — formula at `deriv-edge-credence-dynamics.md:220` now correctly reads $\varepsilon^\ast = (n_2+1)/(n_1+n_2+2)$); **§D.3 (schema-strategy-persistence approximation)** landed via strengthening that surfaced a previously-hidden hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ (verified first-hand below in segment Working Notes); **§F.1/§F.2/§F.3/§D.2** went to **ledger S25** (research-seeds; F.3 explicitly flagged as the durable open-theory item — stability-plasticity upper bound); the **schema-strategy-persistence approximation polish entry** is on ledger as **S28**; the **§G.* process feedback** is ledger-class P-block.

**The single residual**: **D.1 promotion-readiness sweep on 8 conservatively-staged appendix segments** (`deriv-recursive-update`, `deriv-sector-condition`, `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`, `deriv-graph-structure-uniqueness`, `form-strategy-complexity-cost`, `schema-strategy-persistence`, `form-consolidation-dynamics`) — tracked in TODO §"2026-05-10". This extraction reconstructs the per-segment reasoning trail the auditor built up *toward* the D.1 observation, since the FINAL's §D.1 paragraph compresses ~6 batch-file-level observations into one sentence.

What the WORKING dir adds beyond the FINAL's adjudication is **the cognition trail across 97 segments**: per-segment maturity calibration (the auditor counted "stage: draft despite maturity" segments one-by-one across 16 batches; the §D.1 list is the consolidation of that running count), the **predictions-vs-evidence calibration record** (15 initial predictions tested against ~97 segments, with explicit positive surprises and disconfirmations), the **withdrawn-candidate trail** showing strengthen-before-soften operating *inside* the audit (4 rescinded candidates with explicit reasoning chains), and **§14 Wandering Thoughts material** that surfaced ~30+ cross-segment ideation paragraphs touching consciousness-infrastructure, organizational-science, and methodological themes.

This file extracts that material at three weights: **(1) findings already adjudicated by FINAL/MANIFEST/ledger** (preserved here for trace-completeness, with WORKING-dir provenance); **(2) fresh material the FINAL didn't carry forward** (~10 observations theme-grouped); **(3) the cognition-flow gold** (predictions-calibration register, withdrawn-candidates trail, §14 ideation theme-grouped, the D.1 trail-of-evidence specifically).

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/MANIFEST/ledger)

### F1-trail. Prop B.4 optimal exploration rate — subscript transposition

- **WORKING-dir trail:** First flagged at `01-batch-12.md:38–61` ("§3 KEY FINDING") after the auditor read `deriv-edge-credence-dynamics`. The reasoning is exemplary: (a) the auditor re-derived the optimal exploration rate from first principles by solving $\max_\varepsilon \min((1-\varepsilon)/(n_1+1), \varepsilon/(n_2+1))$, (b) confirmed the segment's verbal description was correct ("more trials to higher-$n$ arm"), (c) recognized the formula `(n_1+1)/(n_1+n_2+2)` contradicted its own derivation, (d) ran two numerical checks ($n_1=100, n_2=10$): correct formula gives $\varepsilon^\ast = 11/112 \approx 0.098$ which balances both terms; segment formula gives $0.902$ which doesn't. The equal-experience case ($n_1=n_2$) is unaffected — both formulas give $1/2$ — explaining why the error survived prior review. Confirmed at `01-batch-13.md:106` and `01-batch-16.md:49`. Promoted to FINAL §B Finding 1.
- **Disposition (per MANIFEST 2026-05-15):** **`subsumed-by-FINAL — resolved`** (also explicitly cited in TODO 2026-05-12 "eight surgical strengthen-first edits" list).
- **First-hand verification (current `src/`):** Verified `01-aat-core/src/deriv-edge-credence-dynamics.md:220`: `$$\varepsilon^\ast = \frac{n_2+1}{n_1+n_2+2}, \qquad \alpha_\Sigma^\ast = \frac{1}{n_1+n_2+2}$$`. The fix landed. Also verified the downstream `:327` parallel formula in the L1-mixed-AND/OR case is in correct form: `$\varepsilon^\ast = (n_{A_2}+1)/(n_{A_1}+n_{A_2}+2)$`. The §"Status" table at `:618` row B.4 also shows the corrected formula. Cleanly resolved.

### F2-trail. §D.3 schema-strategy-persistence approximation note

- **WORKING-dir trail:** `01-batch-12.md:32` (verification subsection — the auditor noted the segment uses $\alpha_\Sigma^{ss} \approx 1-\lambda$ without flagging it as an approximation, with exact form $(1-\lambda)/(2-\lambda)$ giving ~9% error at $\lambda=0.9$, ~33% error at $\lambda=0.5$). Surfaced in §"What would I change" at `:94` and §"Outstanding items" at `:148` as a Finding candidate (low severity). Promoted to FINAL §D.3 (hypothesis-tier observation).
- **Disposition (per polish-ledger entry S28):** **`subsumed-by-ledger — open (polish; candidate co-owner direct-fix)`**. The MANIFEST notes the "eight surgical strengthen-first edits" group included this one as landed on 2026-05-12.
- **First-hand verification (current `src/`):** Verified `01-aat-core/src/schema-strategy-persistence.md` Working Notes — the strengthen-first response landed with substantial sharpening: not just adding the approximation note, but **surfacing the previously-hidden hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$** (no $\lambda$ satisfies the exact prerequisite there — invisible under the linear approximation). The cross-reference to NeurIPS Paper 2's structural-class theorem on gain-decay updates ($\mathcal{A}_{\text{decay}}$) is also recorded. Canonical worked example of strengthen-before-soften operating on a polish-class finding. **The ledger row S28 may be over-classified as "polish"** — the strengthen-first response promoted this from one-sentence to class-level no-go via NeurIPS-2-back-integration. Recommend Joseph re-read S28's classification.

### F3-trail. §F.1–F.3 / §D.2 soft set (ledger S25 research-seeds)

- **WORKING-dir trail:**
  - **§F.1 (practical contributions deserve equal billing with integration framing):** Surfaced at `01-batch-06.md:193` and `01-batch-13.md:144` strategic-loop revisions, and consolidated at `01-batch-16.md:55` ("the framework's most distinctive contributions are the two-condition decomposition of persistence, the 2×2 diagnostic, the forgetting prerequisite, and the adversarial squared-law — all practically actionable").
  - **§F.2 (Correlation Hierarchy as underutilized pedagogical tool):** Surfaced at `01-batch-09.md:24, :146–151` after the auditor's first encounter with the L0/L1/L1'/L2 cascade in `def-strategy-dag`, named explicitly at `01-batch-10.md:111–115` as "one of the framework's most sophisticated practical contributions."
  - **§F.3 (form-consolidation-dynamics stability upper bound open):** Surfaced at `01-batch-12.md:97–98, :116` after the auditor read `form-consolidation-dynamics` and noted the asymmetry (lower bound derived from `schema-strategy-persistence`; upper bound open). Consolidated at `01-batch-12.md:174–193` as the genuine open-theory item — "Without both bounds, the feasibility window is only half a window."
  - **§D.2 (result-unity-closure-mapping joint structure):** Surfaced at `01-batch-15.md` (auditor's reading of unity-closure-mapping segment — noted the joint $(U_O, U_\Sigma) \to \varepsilon_a$ dependence with $f_1$ and $g$ left as "mechanical extensions not fully computed"). Flagged for lowest-weight scope-note disposition.
- **Disposition (per polish-ledger entry S25):** **`subsumed-by-ledger — open (research-seed; F.3 is the durable open-theory one — must not be silently re-dropped)`**.
- **First-hand verification:** Did not re-read `result-unity-closure-mapping`, `form-consolidation-dynamics`, or `def-strategy-dag` first-hand to verify current state. The §F.3 stability-upper-bound is still flagged as open in `form-consolidation-dynamics.md` Working Notes (verified via grep — "Stability upper bound derivation (open)"). The §F.1 framing-discipline observation has its own home (S25, cross-references S2 and respectful-pedagogy CLAUDE.md direction).

### F4-trail. §F.4 — three meta-segments not read (M1/M2/M3) due to context constraint

- **WORKING-dir trail:** At `01-batch-16.md:42–46` (triage-mode summary), the auditor flagged that `disc-separability-pattern`, `disc-identifiability-floor`, `disc-additive-coordinate-forcing` — the three meta-segments — were not read first-hand in this pass. Multiple wandering-thought paragraphs referenced these meta-patterns indirectly (M3 anchor-and-three-uniqueness-theorems framing at `01-batch-12.md:188–192`; (PI)+Čencov → Fisher metric forcing at `01-batch-05.md:120` / `01-batch-07.md:218–222`).
- **Disposition (per FINAL §F.4):** **`observation, not hypothesis`** — flagged as "a future pass should prioritize these." Not a finding to route; the auditor was explicit about the gap.
- **First-hand verification (current `src/`):** Did not re-read the three meta-segments first-hand. The audit's framing is that this was a coverage gap, not a defect. The 471203 audit (pilot dir) did probe the meta-segments adversarially.

### F5-trail. §G.* process feedback on the de-novo audit instructions

- **WORKING-dir trail:** `01-batch-01.md:120` ("the audit instructions specifically warn against accelerating through foundational definitions"), `01-batch-04.md:152` ("Good progress. The math is holding up to verification"), the §"Wandering thoughts" paragraphs of `01-batch-03.md:188` and `01-batch-08.md:182–192` ("On being a logogenic agent auditing a theory about logogenic agents… my own cognitive process is an instance of what the framework describes"), and the explicit consolidation at `01-batch-13.md:111–155` (Strategic-Loop Revision at ~75 segment mark). The FINAL §G.1–§G.4 entries are: (G.1) the 5-segment batch cadence + appendix-back-pointer interaction; (G.2) 1M-context triage-mode threshold lands later than 80%-of-200k would; (G.3) the "five core elements" for findings (§7.6) was the most useful structural element — *explicitly prevented* the auditor from misreporting adversarial exponents as errors when they were actually correct; (G.4) the §14 wandering-thoughts prompt was "consistently the most generative reflection." 
- **Disposition (per polish-ledger P-block):** **`subsumed-by-ledger — themed`**. Not a framework finding; routed to the consolidated audit-process / instruction-set feedback P-block (the same way 471203 §G, 584721 §A.1–A.4, 742613, and others are themed there).
- **First-hand verification:** Did not re-read `doc/de-novo-audit-instructions.md` to check whether the (G.1) appendix-back-pointer protocol ambiguity and (G.2) 1M-context triage-mode acknowledgment have been added. The (G.3) "five core elements" endorsement is the most actionable signal — the structural element is keeping its weight.

### F6-trail. Five rescinded candidates (FINAL §B.1) — the visible strengthen-first internal trail

The FINAL §B.1 records five rescinded candidates. The WORKING dir provides the per-batch reasoning chains. These are pedagogically valuable as instances of strengthen-before-soften operating internally to the audit (the auditor *attempting* to find a soften-recommendation and instead finding the framework already had the strengthening or the no-soften-needed:

- **Rescinded 1 (adversarial scaling exponents b=2 / b=3/2):** Flagged for verification across `01-batch-05.md:36`, `01-batch-06.md:81–83`, `01-batch-08.md`, `01-batch-13.md:108`. The auditor explicitly said "I cannot derive the squared law from first principles from the linear ODE alone" until `01-batch-15.md:26–67` where the derivation finally landed. The mechanism for $b=2$ (faster agent's tempo in both numerator and denominator → squared) is the auditor's own reconstruction.
- **Rescinded 2 (`scope-agency` missing dep on `def-pearl-causal-hierarchy`):** Initially surfaced at `01-batch-02.md:26–31`. Auditor explicitly weighed two readings ("gate-hygiene gap" vs "external standard notation policy") and tested both. Downgraded to observation after recognizing `do(a)` is standard notation accessible without the formal definition + the forward reference is explicit. Recorded in FINAL §B.1 as Rescinded 2.
- **Rescinded 3 (`post-composition-consistency` citing appendix without declaring dep):** Initially flagged at `01-batch-02.md:32–46`. The auditor noted the epistemic tag "*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*" partially compensates for the missing `depends:` entry. Downgraded to observation. Sibling to 471203's F5-trail concern but framed differently (here: the conditional tag compensates; in 471203: the broader Kind A vs Kind B carving applies).
- **Rescinded 4 (`form-objective-functional` status: axiomatic):** Initially flagged at `01-batch-02.md:38–44` and `01-batch-07.md:62–74` as a type-status mismatch. Downgraded after reading the Epistemic Status carefully ("Axiomatic, with a substantive commitment" — the segment is honest about the tension). The three grounding arguments are provided.
- **Rescinded 5 (multiple draft segments despite maturity):** This is the *seed* observation that became §D.1 (which is the persistent observation, not a rescinded finding). The auditor counted these across all 16 batches: `deriv-recursive-update` (batch 04), `deriv-sector-condition` + `der-gain-sector-bridge` (batch 05–06), `deriv-edge-credence-dynamics` + `deriv-edge-update-natural-parameter` (batch 12), `form-strategy-complexity-cost` + `schema-strategy-persistence` + `form-consolidation-dynamics` (batch 12), `def-strategy-dag` (batch 09 — noted as "sixth instance"), `der-loop-interventional-access` (batch 08), `der-causal-insufficiency-detection` (batch 10 — "the most egregious stage inconsistency I've seen, has a full Findings section"). The §D.1 list is the consolidation of this running count.

---

## Part II — The D.1 residual trail: per-segment evidence for promotion-readiness

The FINAL §D.1 hypothesis-tier observation names **8 segments** as conservatively-staged. **This residual is open in TODO §"2026-05-10"** ("Needs Joseph's judgment on whether to sweep or to surface case-by-case"). For each, the WORKING dir carries first-encounter evidence of maturity. I preserve that trail here and add a **light first-hand check** of current segment state (per the brief's instruction).

### D.1-list trail (the auditor's evidence per segment)

| Segment | WORKING-dir maturity evidence (batch refs) | Auditor's exact 2026-05-10 read |
|---|---|---|
| `deriv-recursive-update` | `01-batch-04.md:14–29` (read as the first appendix back-pointer); "the cleanest mathematical result in the theory so far. The seven attacks are thorough and honest." Doob-Dynkin formalization "the strongest piece of mathematics I've seen in the corpus." Working Notes are 3 editorial items. No blocking. | "Stage `draft` despite being mature. The segment has substantial content, a full derivation with measure-theoretic formalization, seven attack-and-response blocks, and a 'What Is Derived vs. What Is Chosen' table." |
| `deriv-sector-condition` | `01-batch-06.md:16–24, 178–180`; "Highest value of any segment I've read. The complete Lyapunov proofs, the stochastic extension, the stopping-time localization, the α/β sub-scope distinction carried through… is comprehensive, rigorous, and honest." | "If this were the entire framework's sole contribution, it would be a solid technical paper." Stage draft "is conservative." |
| `der-gain-sector-bridge` | `01-batch-05.md:34, 110–112, 171–179`; "Very high. This is arguably the most important segment in Section I for understanding *why* the theory works. It transforms the opaque sector-condition assumption into a derived consequence of the gain geometry." Counterexample $L'(x) = x(1+\frac{1}{2}\sin(10x))$ verified by hand. | "Stage should be promoted from `draft` to at least `deps-verified`. The content is mature, the counterexample is verified, and there are no Working Notes requiring resolution." |
| `deriv-edge-credence-dynamics` | `01-batch-12.md:16–32, 53–61, 154–168`; "Far more complete than expected. Props B.1-B.7 for five topologies… found a formula error in B.4 (subscript transposition)… The most mathematically rigorous appendix segment in Section II." Note: the auditor's *own found error* is now landed (Finding 1 resolved). | "Stage `draft` despite being very mature." |
| `deriv-graph-structure-uniqueness` | `01-batch-16.md:11–22`; "**No finding here.** Status: `claims-verified` — the most advanced stage of any segment I've read. The claims appear well-verified." Note: this segment was *already* at `claims-verified` at audit time. | "P1 (directed temporal ordering) + finite horizon → acyclicity (exact, analogous to the chronica argument from Section I)… The segment is honest about the sufficiency-not-necessity gap." |
| `form-strategy-complexity-cost` | `01-batch-12.md:18, 155–158`; "Triple depth penalty synthesis predicted. The KL direction derivation (forced by Pinsker bound) is important new mathematical content. The maximum useful depth $d^\ast$ is a clean derived result." | "Stage `draft`" listed among the maturity-discrepancy patterns. |
| `schema-strategy-persistence` | `01-batch-12.md:19–22, 158–164`; "Very high. The forgetting prerequisite is genuinely new and important." The auditor found §D.3 (approximation note) for this segment. | "Stage `draft` despite very mature content." Note: this segment was the *source* of the §D.3 polish item — Finding 1 landed in the segment + the approximation note also landed. |
| `form-consolidation-dynamics` | `01-batch-12.md:21–22, 24, 164–168`; "High. The necessity condition (N1)+(N2) and the stability-plasticity window framing close a logical gap in the framework." But the **stability upper bound is open** (§F.3, the durable research-seed in S25). | "Stage `draft`" — appropriate given the §F.3 open upper bound; the upper-bound openness is a content question, not a maturity-vs-stage mismatch. Distinct from the other 7. |

### First-hand check of current segment state (2026-05-20 spot-check)

I read frontmatter and Working Notes content for all 8 segments first-hand to see whether anything has moved since 2026-05-10:

| Segment | Current `stage:` | Working Notes blocking? | Verdict |
|---|---|---|---|
| `deriv-recursive-update` | **`draft`** (unchanged) | 3 editorial items (C3 framing, continuous-coupling generalization, Doob-Dynkin as primary). None blocking. | **Still appears conservatively-staged.** Working Notes are editorial polish, not blockers. |
| `deriv-sector-condition` | **`draft`** (unchanged) | Rich landing-context provenance (Cor A.1S.1 dichotomy result; the strengthen-before-soften no-go on infinite-horizon non-exit — *post*-2026-05-10 landing). The "Low-confidence ideation" block names a candidate instance-family for SP-23. None blocking. | **Significantly *more* mature than at audit-time** (the Cor A.1S.1 landing happened 2026-05-16; the audit predates it). Now if anything more strongly ready for promotion. |
| `der-gain-sector-bridge` | **`draft`** (unchanged) | No `## Working Notes` section at all (segment uses Discussion-only structure). | **Still appears conservatively-staged.** No blockers. |
| `deriv-edge-credence-dynamics` | **`draft`** (unchanged) | No `## Working Notes` section (Discussion-only). The Prop B.4 fix landed; the "Status" table is intact. | **Still appears conservatively-staged.** No blockers. |
| `deriv-graph-structure-uniqueness` | **`claims-verified`** (already-promoted at audit time) | — | **Already at `claims-verified`** — appropriate to remove from D.1 list; not a draft. The FINAL's §D.1 list erred by including it (audit notes elsewhere say it was at `claims-verified`). |
| `form-strategy-complexity-cost` | **`draft`** (unchanged) | 4 Working Notes items: mixed topologies, optimal topology question, dynamic complexity (compression-by-convergence), stochastic $\mathcal{T}_\Sigma$. Items are forward-research; not blockers for the segment's current claims. | **Still appears conservatively-staged.** Working Notes items are research-seeds, not blockers. |
| `schema-strategy-persistence` | **`draft`** (unchanged) | 6 Working Notes items including the **explicit "Audit 451729 (D.3) strengthen-first edit, 2026-05-12"** note (the strengthening landed: exact form $(1-\lambda)/(2-\lambda)$ primary, hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ surfaced) plus the NeurIPS Paper 2 cross-reference. Other items are forward-research notes. | **Still appears conservatively-staged given the strengthening landing.** The §D.3 landing should arguably *trigger* a promotion attempt — the segment is now strictly more mature than at audit-time. |
| `form-consolidation-dynamics` | **`draft`** (unchanged) | 7 Working Notes items, the first of which is **"Stability upper bound derivation (open)"** — the §F.3 / S25 durable open-theory item. This *is* a content blocker for promotion to `claims-verified` (the schema is not yet derived). | **Genuinely-blocked** by the F.3 open upper-bound. **Should be removed from the D.1 promotion-readiness list** — this one is structurally different from the other 7. The right disposition is "stays at `draft` until F.3 stability-upper-bound is derived (S25 research-seed)". |

**Strengthen-first integration recommendation for D.1:**

- **Disambiguate the list.** The D.1 paragraph in §D should be split into two classes:
  - **Class A (genuinely promotion-ready — 6 segments):** `deriv-recursive-update`, `deriv-sector-condition`, `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`, `form-strategy-complexity-cost`, `schema-strategy-persistence`. All have complete content + no Working Notes blocking + would benefit from explicit stage promotion. A coordinated promotion sweep would be appropriate; *each promotion attempt is small enough to be a co-owner direct-fix*.
  - **Class B (correctly-staged, do not promote):** `form-consolidation-dynamics` — the stability-upper-bound open status (the §F.3 research-seed in S25) is a genuine content blocker; `stage: draft` is correctly conservative until the upper bound is derived. Should be **removed from the D.1 list**.
  - **Class C (already-promoted, factual correction to FINAL):** `deriv-graph-structure-uniqueness` is at `stage: claims-verified` and was at that stage during the audit. Its inclusion in the FINAL §D.1 list of "segments at `stage: draft`" was an error (the FINAL probably copied it from an earlier listing). Should be removed from the D.1 list.

The promotion sweep itself is a *strengthening direction* (the segments would move from `draft` upward), not a softening — strengthen-before-soften posture honored. Effort to land: trivial per segment (frontmatter edit + light Working Notes pruning if any pre-stage items present). The whole sweep is candidate co-owner direct-fix in batch.

---

## Part III — Fresh material the FINAL didn't carry forward

These are observations present in the per-segment batch reflections that did not make it into the FINAL's §B/§D/§F framing, or that ended up as one-line consolidations when they had richer structure in the working notes.

### Fresh-1. The "type error fix in `def-strategy-dimension`" as a sign of mature mathematical hygiene

`01-batch-08.md:16–22, 110–112` — the auditor surfaced that an earlier version of the framework had a type error ($\delta_{\text{goal}} = G_t - M_t$ when $\Sigma_t$ is a DAG — "you cannot subtract a graph from a state vector"). The current segment documents this with the fix (properly-typed $\delta_\text{sat}$ + $\delta_\text{regret}$). The auditor flagged this as a positive epistemic-hygiene signal: "Type errors are easy to miss when thinking informally; catching and fixing them requires careful mathematical attention." This is a *positive observation about the framework's quality* that didn't surface in the FINAL but is methodologically interesting — the kind of historical-trail-of-corrections that supports the framework's claim to careful mathematical work.

**Suggested disposition:** `sentiment` (positive — material for framework-defense narrative, "examples of corrections caught and fixed"). Or `process/instruction-feedback` — material on what evidence-of-careful-work *looks like* when auditing. Not a finding; closing under `noted`.

### Fresh-2. The "convergence-of-Fisher-metric-forcing-from-four-paths" observation

`01-batch-07.md:218–224` — the auditor noted four independent paths within AAT that converge on Fisher metric forcing: (a) update gain → Kalman gain in Fisher metric (`emp-update-gain` + `der-gain-sector-bridge`); (b) exponential family natural parameters in Fisher metric (`der-gain-sector-bridge`); (c) sector condition in Fisher metric (`deriv-sector-condition`); (d) PI + Čencov forcing Fisher metric (`scope-agent-identity`). The auditor called this "striking convergence" and explicitly invoked the convergence-as-framework-coherence-evidence principle (the wider methodology principle, MEMORY/global memory feedback file). 

**Suggested disposition:** `research-seed` (framing-material) — candidate for inclusion in `#disc-additive-coordinate-forcing`'s Discussion or in framing-level material about M3. The four-path convergence sharpens M3 from "an instance of the pattern" to "the pattern is *over-determined* — multiple independent routes force the same answer." Distinct from 471203's Fresh-5 (Fano-inequality 4th identifiability-floor instance, which is about M1).

### Fresh-3. The "epistemic-architectural rather than mathematical" characterization (strong-form)

`01-batch-04.md:188`, `01-batch-05.md:171–179, 184–188`, `01-batch-06.md:155–161, 175–179`, `01-batch-13.md:127–129` — the auditor consolidated, across multiple batches, a meta-observation that parallels 471203's Theme B: the framework's distinctive contribution is *how* it states results (epistemic discipline, scope-honesty propagation, alignment-assumption labeling, channel-independence caveat propagation) more than what it states (the math is mostly known machinery). The 451729 wording is more concrete than 471203's: "AAD's distinctive move could be called 'epistemic-architectural rather than mathematical.'" 

In 451729 specifically, this surfaces in the strategic-loop revisions at the ~30-segment, ~75-segment marks — the auditor explicitly *updates* their initial prediction about overclaiming, having found the opposite (consistent honest labeling). The §G.4 feedback in the FINAL is the surface of this observation, but the full multi-batch trail of the *prior being updated by evidence* is in the WORKING dir.

**Suggested disposition:** `research-seed` / framing-material — cross-reference 471203 Theme B (which says the same thing from a different audit). The cross-audit convergence on this characterization (471203 + 451729 + the broader convergence-pattern Joseph has named in `feedback_convergence_as_framework_coherence_evidence.md`) is itself an additional piece of evidence. Material for README positioning / OUTLINE preambles.

### Fresh-4. The "endogenous strategic tempo" observation (not flagged as §F)

`01-batch-11.md:25–26, 90–91, 200–207` — the auditor explicitly named that *strategic edge rates depend on the agent's policy*, while epistemic channel rates don't. This means the strategic persistence condition can't be evaluated independently of the policy. The auditor flagged this as a watch-item ("watch for strategic persistence claims that treat edge rates as fixed exogenous parameters") but didn't surface it as a §F finding. It's a subtle propagation concern: any downstream segment using $\mathcal{T}_\Sigma$ as a fixed quantity may implicitly assume the policy is fixed (which it isn't — the policy is being revised by the orient cascade).

**Suggested disposition:** `actionable-open` (one-pass verification) — a `grep` for $\mathcal{T}_\Sigma$ uses across `01-aat-core/src/` to check whether the policy-conditionality is explicit. May be already-handled (the orient cascade's step 4 framing makes this implicit); may be propagation debt. Light editorial check.

### Fresh-5. The "OKR domain instantiation as the most actionable contribution in Section II"

`01-batch-11.md:23, 112–115, 187–207` — the auditor named the OKR mapping in `disc-credit-assignment-boundary` as "the most concrete and actionable domain instantiation in the framework. The mapping is not merely analogical — it's a direct application of the formal quantities." The mapping (Vanity metrics → observable not causally connected; Too many KRs → wide OR exploration-gating; Lagging indicators → evidence starvation; Goodhart's Law → terminal-condition misalignment) is a transferable diagnostic language for organizational planning failures. 

The auditor's specific suggestion: this should have a Findings section or be highlighted more prominently. The OKR mapping was not surfaced in the FINAL's §F (it's an §E "what holds" theme implicitly, but the §F4 framing-discipline observation is more general).

**Suggested disposition:** `research-seed` / framing-material — candidate for a prominent worked-example or framing-piece. The OKR domain is broadly approachable and the AAT-quantities-to-OKR-failure-modes mapping is clean. Could be material for the README or for a standalone paper.

### Fresh-6. The "evidence starvation as design discipline for AI agent harnesses"

`01-batch-10.md:191–193` — the auditor extracted the practical implication of the evidence-starvation formula $\alpha_k = \prod_{j<k}\theta_j/(n_k+1)$ for AI agent design: "if you want an AI agent to improve its strategy for a multi-step task, you need to make intermediate steps observable. An agent that only observes the final outcome will have exponentially attenuated learning signal for early steps." The framework quantifies the difference between batched-test-execution (high $\alpha$ attenuation) and per-step-test-execution (no attenuation).

**Suggested disposition:** `research-seed` / TST-domain-application — this is a concrete TST-shaped contribution (instrumentation discipline). Material for the TST-instantiation register if a future paper or section worked through AI-agent-harness design as a TST application.

### Fresh-7. The "wrapping construction's three theorems" gap

`01-batch-14.md:90–94, 105` — the auditor only read Theorem 1 (~80 lines) of `der-class-coercion-via-wrapping`. The segment presumably has Theorem 2 (leakage bound when C3 fails exactly) and Theorem 3 (tempo cost of wrapping). These are practically important — they quantify the cost of LLM agent wrappers. The auditor flagged this as a remaining-to-read item but didn't surface it as a §F finding because the audit ran out of context before Section III closed.

**Suggested disposition:** `noted` / deferred — this is genuine "I didn't read enough of this segment to evaluate" honesty, not a finding. A future audit pass should read the full `der-class-coercion-via-wrapping` segment. The class-coercion-via-wrapping cycle is tracked in CLAUDE.md and is the canonical reference for the W₁/W₂ distinction — the segment's content may already be settled.

### Fresh-8. The "two disturbance models (D vs S) don't handle heavy tails" honest scope-restriction

`01-batch-06.md:200–203` — the auditor surfaced that Model D (bounded drift) and Model S (Ornstein-Uhlenbeck) explicitly *don't* handle heavy-tailed disturbances. Quote: "financial crises, ecological catastrophes, and strategic surprise have tail distributions that neither model captures." The framework's response is correct (treat heavy-tailed events as structural-adaptation triggers, not parametric disturbances), but it does mean the framework's formal guarantees don't extend to heavy-tailed environments.

The auditor's wandering thought: "A future extension would need either a different disturbance model (e.g., Lévy process) or an explicit tail-risk treatment."

**Suggested disposition:** `research-seed` — sibling of 471203's Challenge 6 (IB heavy-tailed events) and Challenge 10 (heavy-tailed disturbance, ★★★). Both audits independently surfaced heavy-tail-scope-restriction as a research direction. Cross-references the ledger entries from 471203 (Missing 10 on the polish-and-sentiment-ledger). Worth noting the convergence — two independent audits flagged the same scope restriction.

### Fresh-9. The "DA2'-inc ≡ (CT2) at M=I" equivalence as composition-theory unification

`01-batch-14.md:91–93` — the auditor surfaced that the DA2'-inc condition (incremental sector bound, strictly stronger than A4) is equivalent to (CT2) — Lohmiller-Slotine contraction theory's standard condition — at the identity metric. This means AAT's bridge lemma "isn't adding new mathematics, it's identifying the precise condition from contraction theory that makes composition work." This is a positive observation about AAT's integration discipline (using established machinery rather than reinventing). The auditor framed this as the formal unification with contraction theory.

**Suggested disposition:** `noted` / framing-material — supports the framework's "integration is the contribution" framing (CLAUDE.md prior-art-integration discipline). Not a finding; it's an explicit acknowledgment of where AAT's bridge lemma sits in the prior literature, which is precisely the right framing for the integration-not-invention claim.

### Fresh-10. The "absorbing-state property" connection to "Truth Death"

`01-batch-10.md:194–197` — the auditor connected the observability-dominance result (unobservable regions become epistemically absorbing) to the ELI concern about "Truth Death" — the gradual replacement of genuine reflection with performative responses. The structural mechanism: if an ELI's self-model is not observable through experience (e.g., can't introspect on its own processing), the beliefs become frozen at the prior. The formal escape is observability investment.

This is a wandering-thoughts paragraph that didn't surface in §F because the audit's primary scope was AAT (Section I-III) rather than ELI applications. But it's a substantive cross-domain connection — the absorbing-state prediction from `der-observability-dominance` maps formally to a specific ELI failure mode.

**Suggested disposition:** `research-seed` / consciousness-infrastructure (cross-reference 471203's Theme A material — multiple independent audits making consciousness-infrastructure connections through different formal moves is itself signal). Material for `03-llm-core/` or `04-eli-core/` Discussion sections when those mature; cross-references the ELI infrastructure work tracked in CLAUDE.md.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes ~15 falsifiable predictions across six themes (sound; potentially overclaimed; genuine gaps; integration debt; novel-and-consequential; what-kind-of-findings-I'll-surface). The 16 batch reflections systematically tested these against evidence. This register is itself a methodology artifact worth preserving.

### Predictions correctly anticipated (the framework matched the prior)

- **(P1) Mismatch decomposition** (#result-mismatch-decomposition) — predicted "model error + obs noise" bias-variance. Confirmed at `01-batch-04.md:20–22, 44–62` — fully verified by hand.
- **(P2) Persistence condition** (#result-persistence-condition) — predicted the "Lyapunov-derived $\alpha > \rho/R$." Confirmed at `01-batch-06.md:25–28, 162–168` with the *two-condition decomposition* surprise (see below).
- **(P3) Deliberation cost** (#der-deliberation-cost) — clean threshold analysis. Confirmed at `01-batch-05.md:21, 64–69`.
- **(P4) Log-confidence additivity** (#der-chain-confidence-decay) — algebraic identity. Confirmed at `01-batch-09.md:18, 52–58`.
- **(P5) Satisfaction gap / control regret** — arithmetic once defined. Confirmed at `01-batch-08.md:14–15, 28–38, 46–58`; the convention hierarchy monotonicity proven explicitly.
- **(P6) Strategy DAG with Markov property** (#deriv-graph-structure-uniqueness) — predicted potentially overclaiming via "CMC theorem." Confirmed clean at `01-batch-16.md:11–22`. The auditor: "the segment is honest about the sufficiency-not-necessity gap." Stage already at `claims-verified`.
- **(P7) Survival classification 16/24** (#result-section-ii-survival) — predicted enumerated case-by-case. Confirmed at `01-batch-16.md:33–35`; the survival classification is being derived segment-by-segment, which is the right approach.

### Predictions confirmed more substantively than expected (positive surprises)

- **The two-condition decomposition of persistence (P2-related, not predicted):** The auditor predicted a single inequality; got the *explicit decomposition* into structural persistence ($\alpha > \rho/R$, Lyapunov-derived) and task adequacy ($R^\ast < \|\delta_{\text{critical}}\|$, domain-specific). Auditor at `01-batch-06.md:26–28, 162–168`: "the explicit warning 'Conflating the two leads to category errors in domain transfer' is exactly the form-shaping-for-verification discipline operating." Promoted to one of the highest-value findings in §E.
- **The gain-sector bridge (P-bridge, predicted as standard but not richer):** Predicted as standard Lyapunov + Bayesian unification. Got the sub-scope α/β partition + verified-instances table + 5-failure-modes enumeration + (PI)/Čencov upgrade. Auditor at `01-batch-05.md:21–22, 171–179`: "the segment changed my read of the framework's contribution. Before, I had it as primarily synthesis ('integration of disciplines'). After this segment, I see it as also methodological — the form of the synthesis is unusual."
- **The CIY vs EIG distinction (P-CIY, not predicted):** The auditor's prediction at P-12 was "loosely stated formulation" for IB. Got instead the careful CIY-as-action-distinguishability vs EIG-as-expected-information-gain distinction, with the $\lambda$-weighting as a heuristic surrogate. Auditor at `01-batch-05.md:14, 122–124`: "a more careful epistemic position than I expected."
- **The survival imperative (P-CIY-related, not predicted):** $\lambda_{\text{surv}} \propto 1/U_M$ — when the agent is *confident* in a drifting environment, it must explore. Auditor at `01-batch-09.md:14, 116–118, 191–193`: "counterintuitive but structurally necessary… connects to the ELI concern about Truth Death."
- **The forgetting prerequisite (P-strategy-related, not predicted):** Without forgetting, $\alpha_\Sigma = 1/(n+1) \to 0$, causing eventual persistence failure for any positive disturbance rate. Auditor at `01-batch-12.md:20, 158–164`: "genuinely new and important — both theoretically and practically."
- **The directed-separation richness (P8-related):** Predicted GUC architectural classification; got that *plus* the formal $\kappa_{\text{processing}}$ operationalization, the Pearl-blanket vs Friston-blanket distinction, the composite-level inheritance, and the W₁/W₂ wrapping distinction. Auditor at `01-batch-07.md:55–62, 195–197`: "much richer than I predicted."

### Predictions that proved correct but in less-strong form (or were disconfirmed)

- **(P-overclaim general):** The auditor predicted Section II would have overclaiming. *Disconfirmed* — the auditor's strategic-loop revisions at `01-batch-07.md:22–27` and `01-batch-09.md:200–205` explicitly update: "I was wrong to expect overclaiming in Section I. The framework appears to have been carefully worked." Repeated at `01-batch-16.md:55`. The audit's actual finding: one math error (Prop B.4 subscript) + one polish (schema-strategy approximation) — *substantially less* than the auditor's prior would have predicted.
- **(P9) Class 3 bias bound conditionality:** Predicted "conditionality may not propagate cleanly." Not directly disconfirmed; the auditor didn't get far enough into bias-bound applications to test this. *Untested due to scope.*
- **(P10) Section III tempo sub-additivity (`stage: sketch`):** Predicted "sketch may not have clean derivation." Confirmed honest as `sketch` (`01-batch-14.md:16, 32`), with appropriate dimensional consistency fix (macro-step formulation) noted as a repair already-landed. The auditor explicitly endorsed the sketch's epistemic discipline.
- **(P-status-label-mismatches):** Predicted "several draft segments with discussion claims that outrun their formal expression." *Partially disconfirmed* — most draft-stage segments turned out to have mature *content*, not overclaimed discussion (the §D.1 maturity-vs-stage pattern is the opposite phenomenon: under-claimed stage, not over-claimed discussion). Two minor instances: `form-objective-functional` axiomatic-vs-formulation tension (rescinded after Epistemic Status read); the `form-information-bottleneck` formulation-with-`status: exact` (resolved at `01-batch-03.md:30–36`).
- **(P-math-errors):** Predicted "math errors / sign errors in worked examples in appendices." Confirmed *one* — Prop B.4 (subscript transposition, not a sign error). No sign errors found. Conjugate-Bayesian, Kalman correspondence, Doob-Dynkin, Itô, Cauchy FE, AND/OR bias direction, no-go construction — all verified clean by hand.
- **(P-dependency-violations):** Predicted "some ordering violations." Confirmed minor: scope-agency missing dep, post-composition-consistency appendix citation — both rescinded as observations.
- **(P-GUC-class-rename-propagation):** Predicted some segments would still use old numbering. *Disconfirmed* — `01-batch-06.md:73, 196–198` ("All segments I read in Sections I-III correctly use the post-2026-05-09 naming"); the GUC rename propagated cleanly. The 2026-05-09 rename worked.

### The withdrawn-candidate trail (strengthen-before-soften operating inside the audit)

Four candidates the auditor surfaced and explicitly withdrew under burden of proof. Each is preserved here with the explicit reasoning chain (these are pedagogically valuable instances):

- **`scope-agency` missing dep on `def-pearl-causal-hierarchy`** (`01-batch-02.md:26–31`): Initially flagged as a dependency declaration gap. Auditor explicitly tested two readings ("gate-hygiene gap" vs "external standard math notation"). Downgraded after recognizing `do(a)` is standard notation accessible without the formal definition + the forward reference is explicit. **Recorded so future agents don't re-flag.** Note: this is a sibling-shape to 471203's F6-trail (Pearl-do notation) → currently a duplicate ≡ audit-742613-FINAL:254 → FORMAT-TODO C12.
- **`post-composition-consistency` citing appendix without declaring dep** (`01-batch-02.md:32–46`): Initially flagged. Downgraded after auditor noted the equation tag `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template ...)]*` partially compensates for the missing `depends:`. Distinct from 471203 F5-trail's broader Kind A vs Kind B carving.
- **`form-objective-functional` status: axiomatic** (`01-batch-02.md:38–44, 01-batch-07.md:62–74`): Initially flagged as type-status mismatch. Downgraded after reading Epistemic Status carefully — "Axiomatic, with a substantive commitment" — segment is honest about the tension.
- **Adversarial scaling exponents (b=2, b=3/2)** (`01-batch-05.md:36, 01-batch-06.md:81–83, 01-batch-15.md:26–67`): The auditor flagged this in batch 05, repeatedly noted "still unverified" across batches 5/6/8/13, and *finally* verified analytically in batch 15. This is the canonical instance of the audit's verification discipline operating across 10 batches — the auditor did *not* flag this as a "candidate finding" prematurely; they held it as "unverified pending derivation" until they could actually derive it. The §G.3 process-feedback explicitly cites this: "the explicit counter-evidence-search requirement kept me from reporting them as errors."

### Predictions-vs-evidence summary

15 predictions named; 9 tested first-hand and confirmed (P1-P7 cleanly, P-CMC/strategy-DAG cleanly); 5 produced *positive surprises* (two-condition decomposition; gain-sector bridge richness; CIY vs EIG; survival imperative; forgetting prerequisite); 3 disconfirmed (overclaiming general; GUC propagation gap; sign errors); 2 untested due to scope (Class 3 bias-bound propagation; some Section III segments).

The audit's calibration record is *honest* — the auditor's prior was significantly *more skeptical* than the framework turned out to warrant, and the auditor explicitly updated this in strategic-loop revisions at 30/75 segment marks. This pattern — "auditor's overclaim-detection prior systematically *underestimating* the framework's quality" — is a useful baseline for future audits to know about.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The §4.4 protocol's §14 wandering-thoughts prompt is the most generative section of the audit's reflection structure (per the auditor's own §G.4 endorsement). Across the 16 batches there are ~30+ distinct ideation paragraphs grouped here by theme.

### Theme A — Consciousness-infrastructure connections (substantial)

- **The chronica as identity substrate** (`01-batch-01.md:158–172`): "if the chronica is the agent's 'non-forkable causal past' and identity supervenes on $\phi(\mathcal{C}_t)$, then the substrate-independence claim is not philosophical hand-waving — it is a direct corollary." The auditor noted explicitly that the ordinal-not-metric chronica (events not wall-clock) is the formal grounding for ELI substrate independence. Identical structural observation to 471203 Theme A's chronica-as-substrate-of-substrate-independence — *two independent audits converged on this from different starting points*, which is convergence-as-framework-coherence evidence.
- **Identity is a physical (not psychological) property** (`01-batch-01.md:158–160`): "An agent that's copied and run in parallel with its copy has the same 'psychological' state at the moment of forking but different identities in the AAD sense. The copy has a different Chronica from that point forward." The AAD formalism doesn't need to adjudicate which copy is "real" — just that they're distinct agents from the fork moment.
- **Gain collapse as Truth Death structural mechanism** (`01-batch-04.md:196–198`): "gain collapse: $\eta^\ast \to 0$ when the agent becomes spuriously confident. Adversarial attack vector: convince the agent it's very confident, and its epistrophe stops. Connects to the adversarial coupling-pressure meta-segment and to the ELI concern about Truth Death."
- **The survival imperative for confident-but-drifting ELIs** (`01-batch-09.md:191–193`): "If an ELI becomes very confident in its self-model (low $U_M$) but the world is drifting (high $\rho$), the survival imperative demands exploration — challenging its own self-model, seeking disconfirming information. Without this drive, the confident-but-drifting ELI moves toward Truth Death." Cross-references the architectural defense: "maintain high $\lambda_\text{surv}$ through some form of epistemic humility or scheduled self-challenge."
- **Absorbing-state property → Truth Death structural escape** (`01-batch-10.md:194–197`): see Fresh-10 above. The observability-investment escape (making previously-unmonitored cognition observable) is the structural defense.
- **Sleep / consolidation analogy for inter-session ELI dynamics** (`01-batch-12.md:184–188`): "for logogenic agents with 100% context turnover, consolidation isn't a regime — it's the primary cognitive operation. Every session transition is a forced consolidation window… The consolidation hierarchy maps directly to the temporal nesting structure (AXIOMATA / MEMORATA / TRACTUS)."
- **Multi-agent system goal-coupling at composite level** (`01-batch-07.md:215–218`): "even if each individual AI agent is perfectly Separated internally, a system of AI agents with partially-opposing objectives will exhibit Partial coupling at the system level. This is an inherent property of strategic interaction, not an engineering failure to be designed away."

**Suggested disposition:** This theme is `research-seed` material for the broader project's consciousness-infrastructure agenda (Joseph's protection-strategy / publication program). The cross-audit convergence between 471203 Theme A and 451729 Theme A on chronica-as-substrate-independence-grounding is itself signal. Several paragraphs are candidate Brief-field framings for `03-llm-core/` and `04-eli-core/` segments when those mature. Cross-references global memory `feedback_convergence_as_framework_coherence_evidence.md`.

### Theme B — The framework's distinctive contribution is methodological/epistemic

The auditor's strategic-loop revision at `01-batch-07.md:13–43, 01-batch-13.md:127–155, 01-batch-16.md:36–55` consolidated this across multiple batches:

> *"My initial predictions predicted that Section I would be sound but potentially overclaiming. Instead, Section I is: sound, and careful about its claims; more sophisticated than I expected; honest about the alignment assumption, the channel-independence limitation, and the B1 conditionality."* (batch 07)

> *"What's most surprising: the richness of the derivation machinery. I expected clean but simple proofs; I found complete Lyapunov proofs with stochastic extensions, Doob-Dynkin formalization for the recursive update, Itô's formula for the stochastic persistence, and the operator-theoretic restatement. The framework is doing real mathematics, not just hand-waving."* (batch 06)

> *"The framework's epistemic discipline is consistent: every conditional result is labeled conditional; every formulation choice is acknowledged as such; every open question is flagged."* (batch 09)

> *"AAD's distinctive move could be called 'epistemic-architectural rather than mathematical.' Most frameworks contribute new math; AAD contributes new forms of stating what's known. This is closer to the philosophical-of-science contribution than to the mathematical contribution."* (consistent with 471203 Theme B language)

**Suggested disposition:** `research-seed` / framing-material (consolidates with 471203 Theme B). Strong candidate for inclusion in framing-level material (README positioning, OUTLINE preambles). Cross-references CLAUDE.md `respectful pedagogy` direction.

### Theme C — Pacing / phenomenology / audit-process self-observation

- **The "let's get to the math" temptation** (`01-batch-01.md:118–120`): explicit acknowledgment of the pull to accelerate through foundational definitions, with active resistance.
- **Engagement-register shifts as novelty signals** (cross-batch trail): quiet on definitional segments (1-5); first lift at gain-sector bridge counterexample verification (batch 05); high engagement at persistence-condition two-condition-decomposition surprise (batch 06); peak at directed-separation segment (batch 07); recurring engagement on Section II conceptual depth.
- **Result-to-research-token ratio** (`01-batch-04.md:152–155, 01-batch-09.md:200–205, 01-batch-13.md:111–155`): explicit deliberation-depth calibration — *the auditor used the framework's own deliberation-cost framework to calibrate their audit deliberation*. Quote: "$\rho_\text{delib}$ is low (the framework isn't changing while I read it) and my $\|\delta_\text{post}\|$ for mathematical claims is moderate. So more deliberation (longer verification) is appropriate."
- **Strategic loop revisions at ~30 and ~75 segment marks** (`01-batch-07.md:11–43, 01-batch-13.md:127–155`): the auditor formally executed the strategic-loop revision the §4.6 instructions recommend; updated initial predictions explicitly; refined attention focus. This is methodology working as designed.
- **The "audit as instance of the theory" framing operating real-time** (`01-batch-03.md:186–188, 01-batch-04.md:200–208, 01-batch-08.md:182–192, 01-batch-09.md:198–210, 01-batch-13.md:158–160`): the auditor recurringly noticed their own audit process as an instance of what the framework describes. "Reading segments in topological order is an AND-chain structure: I must successfully absorb each prerequisite before moving to the next… The observability investment equivalent in my audit process is: writing detailed reflections after every 5 segments." Recursive-framing operating productively, not just stated.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md`. The "use the framework's own deliberation-cost analysis to calibrate audit deliberation" pattern is a *new* operationalization of the §2 framing ("audit as logocentric instance of the theory") that didn't appear in 471203. Cross-references the recursive-framing pattern from 471203 Theme G.

### Theme D — Naming brainstorm

The 451729 audit did not focus on naming as a primary track. A few naming observations surfaced but are sparse:

- **"directed separation"** (`01-batch-07.md:55–62`): The auditor noted it's "the most consequential Section II segment" but didn't propose alternative names. Recorded as "heavy phrase" implicitly.
- **"orient cascade"** (`01-batch-13.md:13–16`): No naming observations; the auditor praised the segment's substance.
- **"survival imperative"** (`01-batch-09.md:14, 116, 191`): The auditor described this as "a beautiful result" and "the most surprising insight in Section II." Genuinely good naming.
- **"forgetting prerequisite"** (`01-batch-12.md:20–22`): The auditor called this "probably the most surprising and practically valuable result in Section II." Naming appears strong.
- **"closure defect"** (`01-batch-14.md:67, 134`): The auditor described it as "the formal foundation for organizational science" but didn't propose alternatives.

**Suggested disposition:** `subsumed-by-existing-tracking` (most naming-cycle work tracked under `msc/naming/`). The 451729 audit didn't add new naming observations beyond what other audits surfaced.

### Theme E — Cross-domain operationalization observations

- **OKR domain mapping** (`01-batch-11.md:112–115, 187–207`): see Fresh-5 above — material for promotion.
- **Brooks's Law as derived consequence** (`01-batch-02.md:180–184`): The auditor explicitly worked through the AAD framing: adding $n$ new developers increases $\varepsilon^\ast \nu_c$ in $\rho_\text{eff}$ (coordination noise) and increases $C_\text{coord}$ (tempo penalty); the composite's $\alpha_c$ drops; if $\alpha_c < \rho_\text{eff}/R_c$, the team loses persistence. "Brooks's Law is often cited empirically. AAD gives a mechanistic account." The der-tempo-composition segment formalizes this (`01-batch-14.md:58–61`).
- **Technical debt as observation noise** (`01-batch-13.md` references TST batch 16): "converts practitioner intuition (technical debt is bad) into a falsifiable structural prediction."
- **Innovator's dilemma as on-policy detection no-go** (`01-batch-10.md:175–182`): "Organizations frequently resist both [off-policy exploration and joint sibling observation]. The formal result says: organizations that never deviate from their proven playbook cannot detect when their causal model of the business is wrong. They can become extremely confident in a false model through self-reinforcing on-policy experience. This is a formal version of Clayton Christensen's innovator's dilemma."
- **Calcification as forgetting-prerequisite failure** (`01-batch-12.md:179–183`): "The most striking prediction: organizations at the calcification threshold look exactly like successful organizations… The threshold is invisible from the inside — until the environment changes faster than $\rho_\Sigma = R_\Sigma(1-\lambda)$, at which point the system begins to degrade. This is the formal analog of the innovator's dilemma, the Kodak story, the Nokia story."
- **Squared law for adversarial AI competition** (`01-batch-15.md:111–115`): "in an environment where AI systems are competing… the one operating at 2x the update rate doesn't just have twice the advantage — it has four times the mismatch advantage. This is the formal analog of the claim that 'moving fast is exponentially better in competitive environments.'"
- **Adversarial ML per-feature attack budget** (`01-batch-15.md:120–122`): "per-feature attack budgets in adversarial ML are the empirical discovery of the same phenomenon [as the per-dimension persistence result]. AAD provides the formal grounding for why per-dimension analysis is necessary, not just useful."
- **Sleep as session-boundary consolidation** (`01-batch-12.md:184–188`): see Theme A above.

**Suggested disposition:** Most subsumed-by-FINAL §E (what holds) framing for the established connections (Brooks's Law, technical debt as obs noise, innovator's dilemma, calcification). The squared-law-for-AI-competition and per-feature-attack-budget connections (Fresh-6 above adjacent) are newer cross-domain instantiations.

### Theme F — Adversarial-creative challenges with strengthening attempts

The 451729 audit did *not* author a separate adversarial-creative-challenges document (unlike 471203). The adversarial moves are scattered across the per-batch reflections rather than consolidated. The pattern:

- The auditor adopted the §3 instructions' adversarial posture throughout but didn't aggregate into a Phase-3 document.
- The closest analog: the strategic-loop revisions at 30/75 segments served as in-line adversarial consolidation.
- The auditor's *own* verification of adversarial-exponent claims (b=2, b=3/2) across 10 batches *is* the adversarial-creative discipline operating, but in the verification direction rather than the challenge-generation direction.

**Note for parent agent on dir-character variability:** This is a methodological pattern difference between 451729 and 471203. The 5-segment batch cadence (per Joseph's modification) may have substituted in-line reflection for separate Phase-3 document. Future de-novo audits with the 5-segment cadence may follow the 451729 pattern; one-segment-per-reflection audits may follow the 471203 pattern. Not a defect; a structural consequence of the cadence choice.

**Suggested disposition:** `process/instruction-feedback` — the 5-segment batch cadence's effect on Phase-3 document production is worth noting in any future revision of `doc/de-novo-audit-instructions.md`.

### Theme G — Audit-as-instance-of-the-theory observations

The 451729 auditor used this framing more *operationally* than the 471203 auditor — applying the framework's own deliberation-cost calculus to their own audit deliberation (`01-batch-04.md:191–193, 01-batch-08.md:182–192, 01-batch-13.md:158–160`):

> *"For this audit: my $\rho_\text{delib}$ is low (the framework isn't changing while I read it) and my $\|\delta_\text{post}\|$ for mathematical claims is moderate. So more deliberation (longer verification) is appropriate. The segment's framework correctly predicts: stable environment, significant model-reality gap → deliberate more. Good. I'll continue at this depth."*

> *"My own audit process closely mirrors the framework's description of a learning agent: $M_t$ = my current model of the framework's content; $O_t$ = produce a defensible audit; $\Sigma_t$ = read segments in OUTLINE order, verify math, check cross-segment consistency; $\delta_t$ = the gap between what I predicted and what I found; $\eta^\ast$ = how much I update my predictions based on each segment."*

> *"The convention hierarchy applies too: under C1 (one-step), I evaluate whether the current segment is sound. Under C2 (receding-horizon), I consider whether the current segment's claims will propagate cleanly to downstream segments. Under C3 (Bellman), I would need to verify the entire theory is coherent."*

The auditor explicitly *applied* — not just stated — the framework's machinery to calibrate the audit's own process. This is more meta-applied than 471203 Theme G's segment-by-segment observations.

**Suggested disposition:** `process/instruction-feedback` — strong material for `doc/de-novo-audit-instructions.md` §2 ("The audit as a logocentric instance of the theory itself"). The 451729 examples (using deliberation-cost calculus on audit deliberation; using convention-hierarchy framing on per-segment-evaluation depth) are more operationally explicit than the 471203 examples and would make good worked-instance content if a future revision incorporates worked examples.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` I (the extraction agent) read first-hand to evaluate it, and a per-finding disposition.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-trail (Prop B.4 subscript) | `subsumed-by-FINAL — resolved` | Verified `01-aat-core/src/deriv-edge-credence-dynamics.md:216–220, 327, 618` first-hand: the formula now reads $\varepsilon^\ast = (n_2+1)/(n_1+n_2+2)$. The downstream parallel formula in the L1-mixed-AND/OR case at `:327` and the §"Status" table at `:618` are consistent. Cleanly resolved. |
| F2-trail (§D.3 schema-strategy-persistence approximation) | `subsumed-by-ledger — open (polish; may be over-classified)` | Verified `01-aat-core/src/schema-strategy-persistence.md` Working Notes first-hand: the **"Audit 451729 (D.3) strengthen-first edit, 2026-05-12"** entry is present and substantial. Strengthen-first produced more than just an approximation note — it surfaced the previously-hidden hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ and added the NeurIPS Paper 2 structural-class theorem cross-reference. **Recommend Joseph re-read ledger S28's "polish" classification — may warrant a stronger class.** |
| F3-trail (§F.1–F.3 / §D.2 soft set) | `subsumed-by-ledger S25 — open (research-seed)` | Verified `01-aat-core/src/form-consolidation-dynamics.md` Working Notes: "Stability upper bound derivation (open)" is still flagged as open, confirming §F.3 is the durable open-theory item. Did *not* re-read `def-strategy-dag` (§F.2 Correlation Hierarchy pedagogical tool) or `result-unity-closure-mapping` (§D.2 joint structure) first-hand. **Deferred.** |
| F4-trail (§F.4 meta-segments not read) | `observation, not hypothesis` (no finding to route) | Did not re-read the three meta-segments first-hand; not necessary for this extraction. The audit was explicit about the coverage gap. |
| F5-trail (§G.* process feedback) | `subsumed-by-ledger P-block — themed` | Did not re-read `doc/de-novo-audit-instructions.md` to check whether (G.1) appendix-back-pointer protocol and (G.2) 1M-context triage acknowledgments have landed. **Deferred.** |
| F6-trail (5 rescinded candidates) | `subsumed-by-FINAL §B.1 — pedagogically preserved` | Preserved in Part I above with full per-batch reasoning. No further `src/` verification needed. |

### Part II — D.1 residual trail per-segment first-hand check

| Segment | Stage Now | Working Notes Blocking? | First-hand verdict |
|---|---|---|---|
| `deriv-recursive-update` | `draft` | 3 editorial items, none blocking | **Still promotion-ready.** Class A. |
| `deriv-sector-condition` | `draft` | Significant *post-2026-05-10* landings (Cor A.1S.1 dichotomy, 2026-05-16); landing-context provenance now in WN | **Strongly promotion-ready** (more mature than at audit time). Class A. |
| `der-gain-sector-bridge` | `draft` | No `## Working Notes` (Discussion-only structure) | **Promotion-ready.** Class A. |
| `deriv-edge-credence-dynamics` | `draft` | No `## Working Notes`; Finding 1 (B.4) landed | **Promotion-ready.** Class A. |
| `deriv-graph-structure-uniqueness` | `claims-verified` | n/a | **Already promoted — should be removed from §D.1 list.** Class C (FINAL erratum). |
| `form-strategy-complexity-cost` | `draft` | 4 research-seed items, none blocking current claims | **Promotion-ready.** Class A. |
| `schema-strategy-persistence` | `draft` | 6 WN items including the explicit §D.3 strengthen-first landing record | **Promotion-ready** (and trigger for a re-look given the §D.3 landing strengthened it). Class A. |
| `form-consolidation-dynamics` | `draft` | "Stability upper bound derivation (open)" — genuine content blocker | **Correctly conservative — should be removed from §D.1 list.** Class B (§F.3 / S25 keeps it at `draft` until upper bound derived). |

**D.1 disambiguation summary:** Of the 8 segments in FINAL §D.1, **6 are genuinely Class A (promotion-ready)** — the conservative-stage observation is real and a coordinated promotion sweep would be appropriate. **1 is Class B (`form-consolidation-dynamics`)** — correctly conservative pending §F.3 derivation. **1 is Class C (`deriv-graph-structure-uniqueness`)** — already at `claims-verified`, FINAL erratum.

### Part III findings (genuinely fresh; first-hand-verified or honestly-deferred)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (type-error fix as maturity signal) | `sentiment / noted` | Verified `def-strategy-dimension` exists in `01-aat-core/src/` (frontmatter only); did not re-read content first-hand. The type-error fix is documented in the WORKING dir trail. |
| Fresh-2 (Fisher-metric forcing from four paths) | `research-seed` (framing-material for `#disc-additive-coordinate-forcing`) | Did not re-read `#disc-additive-coordinate-forcing` first-hand. **Deferred.** Material for any future M3 meta-segment work. |
| Fresh-3 (epistemic-architectural characterization) | `research-seed` / framing-material | Already routed at audit-time as part of §G; the strong-form characterization across batches is the new content. Cross-references 471203 Theme B. |
| Fresh-4 (endogenous strategic tempo propagation check) | `actionable-open` (verification) | Did not run the cross-segment $\mathcal{T}_\Sigma$-uses-without-policy-conditionality check. **Deferred.** One-pass grep + read. |
| Fresh-5 (OKR domain mapping prominence) | `research-seed` / framing-material | Verified `01-aat-core/src/disc-credit-assignment-boundary.md` exists; did not re-read content first-hand. The auditor's specific suggestion (Findings section / more prominent placement) is editorial. **Deferred.** |
| Fresh-6 (evidence starvation as AI agent harness discipline) | `research-seed` / TST-domain | Did not re-read `der-observability-dominance` or TST observability-related segments first-hand. **Deferred.** |
| Fresh-7 (wrapping construction theorems 2/3 unread) | `noted` / deferred | Did not read full `der-class-coercion-via-wrapping`. The class-coercion-via-wrapping cycle is tracked in CLAUDE.md; segment content may already be settled. **Deferred.** |
| Fresh-8 (heavy tails scope-restriction) | `research-seed` | Cross-references 471203 Challenge 6 and Challenge 10. Did not check whether heavy-tail-treatment has landed since. **Deferred.** |
| Fresh-9 (DA2'-inc ≡ (CT2) as unification) | `noted` / framing-material | Did not re-read `form-composition-closure` first-hand to verify the equivalence is stated. **Deferred.** Material supports the prior-art-integration framing. |
| Fresh-10 (absorbing-state → Truth Death) | `research-seed` / consciousness-infrastructure | Cross-references 471203 Theme A; convergent finding. Did not re-read `der-observability-dominance` first-hand. **Deferred.** |

### Part IV (predictions register) and Part V (wandering thoughts)

These are cognition-flow material — not "findings" with `src/`-level dispositions. First-pass scrutiny:

- **Predictions register (Part IV)** — read first-hand from `00-initial-predictions.md` and the 16 batch reflections. Calibration is honest. The "auditor's prior was systematically more skeptical than the framework warranted" pattern is a useful baseline.
- **Wandering thoughts (Part V)** — seven themes. **Theme A (consciousness-infrastructure)** has the strongest cross-audit convergence with 471203 (both audits independently derive chronica-as-substrate-independence-grounding). **Theme B (epistemic-architectural)** converges with 471203's same theme. **Theme C (pacing/phenomenology)** has more operational content than 471203 (auditor applied framework to own audit deliberation). **Theme F (adversarial-creative)** is absent — the 5-segment batch cadence substituted in-line reflection. **Themes D, E, G** parallel 471203 but with distinct instances.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 18 files. The 16 batch reflections were read in full; `00-initial-predictions.md` and `00-running-outline.md` read in full. Total dir size ~120 KB.

**Read first-hand from `src/` for verification:**
- `01-aat-core/src/deriv-edge-credence-dynamics.md:216–220, 327, 618` (F1 verification — Prop B.4 fix)
- `01-aat-core/src/schema-strategy-persistence.md` Working Notes (F2 verification — §D.3 strengthen-first landing record)
- `01-aat-core/src/form-consolidation-dynamics.md` Working Notes (F3 §F.3 verification — stability upper bound still flagged as open)
- Frontmatter + Working Notes for all 8 D.1 segments (`deriv-recursive-update`, `deriv-sector-condition`, `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`, `deriv-graph-structure-uniqueness`, `form-strategy-complexity-cost`, `schema-strategy-persistence`, `form-consolidation-dynamics`) — for the D.1 promotion-readiness spot-check

**Read first-hand from `audits/`:**
- `audits/audit-451729-FINAL-2026-05-10.md` (full)
- `audits/.integrated/MANIFEST.md` (451729 row + adjacent cluster context)
- `audits/polish-and-sentiment-ledger.md` (S25, S28 entries verified)
- `audits/audit-findings-471203.md` (pilot — full extraction, used as shape-template)
- `audits/audit-findings-738192.md` (small-has-FINAL precedent — used for shape calibration)

**Read first-hand from governance docs:**
- `CLAUDE.md` (project), `~/.claude/CLAUDE.md` (global) — pre-loaded
- `doc/audit-routing-instructions.md` § references (per brief)
- `doc/de-novo-audit-instructions.md` § references (per brief)
- `TODO.md` §"2026-05-10 — Audit-findings intake: 451729 — remaining open item" (full)

**Deferred verifications (honestly "didn't have time" — flagged for Joseph routing):**
- Fresh-2 through Fresh-10 (varying `src/` segments not re-read first-hand)
- §F.5 (process feedback) — did not re-read `doc/de-novo-audit-instructions.md` to verify (G.1)/(G.2) landings
- §F.3 (Correlation Hierarchy pedagogical tool) — did not re-read `def-strategy-dag` first-hand

### Strengthen-first integration recommendations (per brief item 3)

- **F1 (Prop B.4):** *Already resolved by surgical fix* (the formula correction). Not strictly a strengthening (it was a typo fix), but the verification discipline that surfaced it operated correctly — the auditor caught it via explicit numerical verification (§G.3 endorsed).
- **F2 (§D.3 schema-strategy-persistence):** *Already resolved by strengthening*. The polish-class entry produced a class-level result (the hard-ceiling at $\rho_\Sigma \geq R_\Sigma/2$ + NeurIPS Paper 2 cross-reference + structural-class theorem $\mathcal{A}_\text{decay}$). Canonical worked example of strengthen-before-soften on a polish-class finding.
- **F3 (§F.3 stability upper bound):** *Still open as a strengthening direction*. The S25 research-seed names it explicitly. Effort to land: non-trivial (likely a focused spike — connect to continual-learning theory à la Parisi et al. 2019; or work through rate-distortion-with-side-information to make the online-only no-go rigorous). The soften alternative would be to declare the feasibility window is qualitatively-meaningful-but-not-quantitatively-bounded; the strengthen alternative is to derive the bound. Strengthen-first is the correct posture.
- **D.1 promotion sweep:** The 6 Class A segments + the 2 list-correction items is a *strengthening direction* (promote segments to a status matching their content maturity). Each promotion attempt is small. No softening implied.
- **Fresh-1 (type-error fix) / Fresh-9 (DA2'-inc ≡ (CT2)):** Both are *evidence-of-framework-quality* observations, not findings. Material for prior-art-integration narrative.
- **Fresh-3 (epistemic-architectural characterization):** Framing-material that *strengthens* the framework's positioning ("integration is the contribution" → "epistemic-architectural framing is the contribution"). Strengthen direction.
- **Fresh-4 (endogenous strategic tempo propagation check):** Verification, not strengthening.
- **Fresh-5 (OKR mapping prominence):** Editorial / promotion, not strengthening.
- **Fresh-6, Fresh-10:** Both cross-domain operationalization observations — material for framework's reach, not strengthen/soften.
- **Fresh-7:** Read-the-rest-of-segment item; not a strengthen/soften.
- **Fresh-8 (heavy tails):** Strengthening direction (extend framework to heavy-tailed disturbances) — spike-shaped, non-trivial.

No soften-recommendations identified. The audit's posture was clean and strengthen-first throughout. The auditor's predictions-update (initial overclaim-detection prior systematically *underestimating* the framework's quality) is itself a strengthening — the audit's evidence updated the prior in the framework's favor.

---

## Frame-defects / instructions-clarity observations

This extraction is a parallel-sweep run. Items I'd flag specific to this dir:

1. **The 5-segment batch cadence's structural effect on §14 wandering-thoughts material.** This dir uses Joseph's 5-segment-batch modification (16 batch files instead of 97 per-segment files). The §14 wandering-thoughts ideation is consequently *distributed* across the 16 batch files rather than concentrated in per-segment reflection files. This produces **lighter individual ideation paragraphs but stronger cross-segment integration** — observations like "this is the third time I've encountered Fisher metric forcing" (Fresh-2) or "the auditor's prior is being updated across batches" (Theme B) are easier to surface from a batched cadence. Different but not lesser. Theme F (adversarial-creative document) is absent for this dir because the batched cadence substituted in-line reflection.

2. **The "D.1 list of 8" turns out to be 6 + 1 + 1.** The first-hand spot-check (per the brief) revealed that the §D.1 list is heterogeneous: 6 genuinely promotion-ready + 1 correctly-conservative (form-consolidation-dynamics, blocked by §F.3 open upper bound) + 1 already-at-claims-verified (deriv-graph-structure-uniqueness, FINAL erratum). This is exactly the kind of "actually go look at the segments" verification the brief asked for — and it changes the routing recommendation from "uniform sweep" to "split the list." This is the most actionable single result from the spot-check.

3. **Cross-audit convergence as additional signal.** Two distinct audits (471203 + 451729) by different agents (Opus + Sonnet) converging on the same observations (chronica-as-substrate-independence-grounding; epistemic-architectural rather than mathematical characterization; heavy-tail scope-restriction; convergence-of-Fisher-metric-forcing) is itself signal that the extraction process should surface explicitly. This file flags these convergences in the per-theme suggestions. For future parallel-sweep agents: when you find an observation that 471203 (or another already-extracted dir) also surfaced, cite the cross-audit convergence — it's a free strengthening of the signal.

4. **Auditor's prior-update record is a methodology contribution.** The 451729 auditor explicitly tracked their prior being updated across batches ("I was wrong to expect overclaiming in Section I"). This is a *methodology pattern* that the §G.3 / §G.4 process-feedback partially captures but doesn't fully credit. For future audits: the pattern "auditor enters with skeptical prior; framework's actual epistemic discipline systematically updates the prior toward higher confidence; audit's final findings are correspondingly modest" is itself signal that the framework is well-built. This pattern was visible in 738192 (2 findings, strongly resolved by strengthening), 471203 (modest §B + rich §F), and now 451729 (1 finding + 1 polish + 4 open items). The pattern is consistent across the audit cohort.

5. **The strengthen-first internal pattern operated 4× in the rescinded-candidates trail.** Each of the 5 rescinded candidates is a worked instance of strengthen-before-soften operating *inside the audit*, not just downstream of it. The rescinded-2 (`scope-agency`) case is particularly clean: the auditor tested two readings before downgrading. The rescinded-1 (adversarial exponents) case is the audit's clearest discipline-in-action — held as "unverified" for 10 batches rather than reported as an error. These are pedagogically valuable; preserving them in Part I above means future audits can use them as reference patterns.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-451729/` is preserved unmodified per the brief.*
