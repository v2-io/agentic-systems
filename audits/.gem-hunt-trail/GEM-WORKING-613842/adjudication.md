# Gem-hunt adjudication — audit 613842

*Agent: general-purpose gem-hunt slice. Date: 2026-05-29. Report-only — no canon edits/moves/commits. Landings + verification are Joseph's.*

## Frame and what is special about this slice

`audits/audit-findings-613842.md` is **not a raw audit** — it is already a sophisticated *extraction* (2026-05-20, Opus 4.7) of the original `AUDIT-WORKING-613842/` gold dir, with embedded dispositions and a first-pass scrutiny table. So this slice's gem-hunt has a different shape than the five audits already mined in the 2026-05-29 cycle (472913/526815/963715/542891/184930, per `audits/STATUS.md`): the three headline findings (F1/F2/F3) are **already dispositioned in MANIFEST Cluster B** (2026-05-16) and the process-feedback already sits in the polish-and-sentiment ledger. 613842 is *not* in the STATUS.md gem-hunt list — it was mined for *findings* but never gem-mined for the **un-captured remainder**: the Fresh-1…6 items and the substantive (non-process) half of the bigger-picture observations, several of which the extraction itself flagged "deferred — not separately verified."

My job, fresh eyes: verify those deferred items against *current* canon, find what carries re-derivable content, and flag any already-routed disposition that now looks wrong. **Per the standing gate I did not open `AUDIT-WORKING-613842/`; I worked only from the FINAL extraction.**

**Headline drift-check result (the central confirmation):** every one of this audit's three flagship findings has already been resolved by a later cycle — F1 + F2 by the 2026-05-16 strengthen-then-no-go landings, F3 routed live to SP-21/TODO. First-hand re-verified (loci below). And *two* of the "fresh / soft-polish" deferrals (Fresh-3, Fresh-4) have **also** drifted into already-captured since the 2026-05-20 extraction. This is the same pattern the prior wave found: dispositions are drifted proxies; the labels lag the canon.

---

## (A) Ready-to-land

Nothing in this slice is a ready-to-land *theory or prose* gem that is both real and un-captured. The honest result for the (A) bucket is: **the high-value findings are already in canon, with loci below.** I surface one near-(A) item — a `depends:`-hygiene observation that is mechanically actionable and re-derivable — but its right home is a scoped first task (so it lands in (B) as a research-seed, not (A), because executing it correctly is judgment-bearing per-edge work, not a mechanical sweep). Manufacturing an (A) gem here would be exactly the failure the brief warns against.

---

## (B) Research-seeds (un-captured; concrete first task named)

### B1. The 7-segment strategic-tempo SCC is *spurious* — created by `depends:` conflating "logical prerequisite" with "where the strengthening appendix lives" — and a forward-reference field would dissolve it without losing a single cross-link. **(The real gem of this slice.)**

**What it is, actionably.** Audit Fresh-5 named a substantive question the project never routed: *is the 7-segment strategic-tempo dependency SCC the framework's actual logical structure (a feature — these segments genuinely co-define each other), or is it frontmatter design-debt (some `depends:` should drop/re-route)?* The extraction marked this `research-seed` and explicitly deferred the depends-edge walk. I walked the load-bearing edge first-hand and the answer is now concrete:

- **Confirmed a direct mutual 2-cycle in current canon:** `form-strategy-complexity-cost` ⟷ `deriv-strategy-cost-regret-bound` each list the other in `depends:` (verified: each file's frontmatter contains the other's slug). A `depends:` field that means "logical prerequisite" *cannot* be mutual; at least one edge is non-logical.
- **Diagnosed the edge semantics, both directions:**
  - `deriv-strategy-cost-regret-bound` → `form-strategy-complexity-cost` is **genuinely logical**: the appendix derives a *property of* the formulation (that the $\pi^\ast$-first reverse-KL direction is forced). You cannot state the property without the object it is a property of. Keep.
  - `form-strategy-complexity-cost` → `deriv-strategy-cost-regret-bound` is **motivational/forward-reference, not logical**: the formulation's load-bearing content (the strategy-IB objective) is *stateable at its base tier* without the appendix; the appendix *strengthens* it (discussion-grade → robust-qualitative, per the segment's own Epistemic Status at `form-strategy-complexity-cost.md:144,152`). The dependency points *forward* to its own strengthening, not *backward* to a prerequisite.
- **This is the mechanism of the whole SCC.** Main Section-II segments listing their own strengthening-appendices in `depends:` is what closes the cycle. The SCC is largely an artifact of the `depends:` field being asked to carry two distinct relations (logical-prerequisite *and* where-the-strengthening-lives) at once.

**Named canon loci checked.** `01-aat-core/src/form-strategy-complexity-cost.md` (frontmatter `depends:` includes `deriv-strategy-cost-regret-bound`; body lines 21, 53, 63, 144, 152 confirm the appendix is cited as a *strengthening* of an independently-stated formulation, not as a prerequisite); `01-aat-core/src/deriv-strategy-cost-regret-bound.md` (frontmatter `depends:` includes `form-strategy-complexity-cost`; body lines 16, 238 confirm it derives a property *of* the formulation); `01-aat-core/OUTLINE.md:170-171,401` (formulation in §II body, derivation in Appendix A — the canonical "appendix strengthens body" placement). All 7 SCC members exist with the depends-edges Fresh-5 reported.

**Why a gem — wisdom + beauty.** (i) *Wisdom:* this is a latent integrity question in the dependency graph of a load-bearing §II cluster. As long as `depends:` conflates the two relations, every future agent (and `bin/lint-outline`) reads a cycle that misrepresents the actual logical order, and the SCC keeps being treated as a "process inconvenience to manually break" rather than as a fixable modeling error. (ii) *Beauty:* the resolution is strengthen-first, not delete — it *adds* expressive precision rather than cutting content. A `strengthens:` (or `forward-ref:`) frontmatter field, distinct from `depends:` (reserved for logical prerequisite), would dissolve the spurious SCC, make the dependency DAG actually acyclic, keep every cross-link visible, and *encode* the strengthen-before-soften architecture structurally (a segment knows which appendix lifts its tier). Note the connection to audit Fresh-2 (`def-model-sufficiency` listing `form-information-bottleneck` as a motivational not-logical dependency) — same root pattern, different segment; the fix is general.

**Concrete first task.** A 45–90 min spike: (1) walk all 7 SCC members' `depends:` edges and classify each as *logical-prerequisite* vs *motivational/forward-reference (strengthening or citation)*; (2) confirm that re-routing the motivational edges out of `depends:` yields an acyclic graph (predict: yes); (3) propose the minimal frontmatter change — most likely a new `strengthens:`/`forward-ref:` field in `FORMAT.md` — that lets the cross-link survive without falsifying `depends:`. Output is a PROPOSALS entry (this is a FORMAT-level architectural move that cuts across segments, so it wants Joseph's call) plus the per-edge classification table. **Recommended home:** new spike → `spikes/PROPOSED.md` entry now, escalating to a PROPOSALS.md architectural-move entry once the per-edge walk confirms the acyclic result. *Do not* conflate with the existing `def-strategy-dag` composition-defect SCC entries in `PROPOSED.md:28,46` — those are a different SCC (intra-strategy-DAG coupling), unrelated to this dependency-graph SCC.

**Already-routed check.** The *process* flavor of this ("add an SCC/cycle-handling clause to `doc/de-novo-audit-instructions.md`") IS already routed — ledger line 78 attributes "SCC/cycle-handling clause" to 613842. But that captures only BP5 (the audit-methodology recommendation). The **substantive theory-graph question** (is the SCC real structure or design-debt) is captured *nowhere* — and it now has a concrete answer (design-debt, with a strengthen-first fix). This is the un-captured remainder.

### B2. Fresh-1 — `#form-information-bottleneck` mixed-tier: the *strengthening* direction (derive the volatility-with-policy subclaim under named conditions), not the audit's tier-split soften.

**What it is, actionably.** The IB segment carries `status: exact` while its body contains a weaker robust-qualitative volatility/policy-relativity subclaim alongside the exact imported-theorem core. The audit's proposed move was a *soften*: split into an exact formulation segment + a lower-tier discussion segment. The extraction itself (line 203, 406) flagged the **strengthen-first alternative**: if the volatility-with-policy claims can be *derived* under named conditions, the second tier *promotes* rather than separates — a strictly richer move.

**Named canon loci checked.** `01-aat-core/src/form-information-bottleneck.md:1-9` — frontmatter still `status: exact`, `stage: draft`; body (lines 11+) does carry the two-tier register (exact imported core + the "volatility natively degrades MI, optimal compression discards old info even at constant $\beta$" subclaim presented as a clarification). The mixed-tier tension the audit named is still present in current canon — *not* yet resolved either by split or by strengthening. So this is genuinely un-captured.

**Why a gem — strength.** The strengthening direction would *add a derived result* (volatility→MI-decay under named conditions) where today there is a prose clarification. That converts an editorial smell into a theorem opportunity — the strengthen-before-soften posture applied exactly where the audit reflexively reached for the soften.

**Concrete first task.** A spike: attempt to derive "under bounded-volatility / stationary-mixing conditions, $I(\mathcal{C}_{t-k}; o_{t+1:\infty}\mid a)$ decays at a rate that makes the IB optimum discard stale history at fixed $\beta$" as a named conditional result. If it derives → promote to a `der-*` segment, retire the mixed-tier tension by strengthening. If it doesn't → fall back to the audit's tier-split (the honest soften, now earned). **Recommended home:** `spikes/PROPOSED.md` entry; the next IB-area cycle. Note both moves are available — record that in the spike framing so a future agent doesn't default to the split.

### B3. Fresh-2 — `#def-model-sufficiency` lists `form-information-bottleneck` as a `depends:` edge that may be motivational, not logical (the converse depends-incompleteness; same root as B1).

**What it is, actionably.** Audit Fresh-2 watchpoint: the retained-predictive-information ratio $S(M_t)$ "does not appear to require `#form-information-bottleneck`; IB *motivates* why the quantity matters, but the quantity itself looks definable without committing to the IB optimum." `depends:` is for logical dependence, not citation-strength; a motivational edge here is the same conflation as B1.

**Named canon loci checked.** `01-aat-core/src/def-model-sufficiency.md:1-9` — `depends:` still lists `form-information-bottleneck` (alongside `form-agent-model`, `def-action-transition`). Body (line 12) confirms the framing: "*Having committed to … information-bottleneck pressure (#form-information-bottleneck) shaping it, the framework needs a measurable handle…*" — IB is invoked as motivation for *why* sufficiency matters; the *definition* of $S(M_t)$ (a conditional-MI ratio) does not invoke the IB optimum. So the edge does read as motivational. Un-captured.

**Why a gem — wisdom (graph hygiene) + feeds B1.** On its own this is a light one-edge call. Its value is as the **second confirmed instance** of the B1 pattern (`depends:` carrying motivational edges), which is what makes B1 a *general* FORMAT-level fix rather than a one-cluster patch. Bundle it into B1's per-edge audit as a worked second example.

**Concrete first task.** Decide the edge: if purely motivational, either drop it from `depends:` or (better, under the B1 fix) re-route to the proposed `forward-ref:`/citation field. Pairs with B1's FORMAT proposal. **Recommended home:** fold into B1's spike as a second worked instance; the FORMAT field-distinction proposal covers both.

---

## Confirmed non-losses (already in canon / already routed — with loci)

| Item | Why not a gem now | Locus proving captured |
|---|---|---|
| **F1** (`def-adaptive-tempo` scalar-overcount) | Resolved by strengthening (matrix-Loewner/tensor canonical, scalar = shared-eigenbasis special case). Strictly stronger than the audit's "scope or rename" soften. Narrow `status`-tag residue only, tracked TODO:395/126, not a blocker. | `01-aat-core/src/def-adaptive-tempo.md` (tensor extension + scalar-as-special-case framing + `#deriv-matrix-persistence-condition` pointer); MANIFEST Cluster B row "742613-F4 / 613842-F1". First-hand re-verified by the extraction; I accept its read (frontmatter line 19 + Epistemic Status). |
| **F2** (Model-S persistence summary compression) | The canonical strengthen-then-no-go. Audit asked for downstream caveating (soften); project found the infinite-horizon object *cannot exist*, landed Cor A.1S.1 (exact, $P(\tau_R\lt\infty)\in\{0,1\}$, $\alpha$-invariant) + `#deriv-stochastic-non-exit` (no-go demonstrated). Cascade clean. | `01-aat-core/src/deriv-sector-condition.md` (Prop A.1S four-sub-result form + Cor A.1S.1); `01-aat-core/src/deriv-stochastic-non-exit.md`; MANIFEST Cluster B; CHANGELOG 2026-05-16; global-memory `integration-is-replacement.md`. |
| **F3** (C-iv strategic-composite route partial integration) | Routed live and triple-tracked: TODO:95 + PROPOSALS SP-21 §G + ledger. The C-iv-vs-C-iii sub-distinction (C-iv = equilibrium-statistic-over-joint-policy, structurally further from closure-defect ontology than C-iii) is *already captured* in SP-21 §G (PROPOSALS:363-366). | `TODO.md:95-104`; `PROPOSALS.md:357-407` (SP-21 §G). **Standing-item note below.** |
| **Fresh-3** (`#post-causal-structure` Discussion doing more than time-arrow postulate names) | **Drifted to captured since the 2026-05-20 extraction.** The "extra work" — weighting updates by action-contingent informativeness — has been *extracted into its own derived segment*: the postulate now names the formal measure (**causal information yield, CIY**) and delegates it to `#def-causal-information-yield`. Exactly the strengthen-first resolution (promote to a derived segment, don't just leave it in the postulate's prose). | `01-aat-core/src/post-causal-structure.md:49` ("*The formal measure of this distinction — causal information yield (CIY) — is developed in #def-causal-information-yield*"); line 15 keeps the scope-clarifying coupling-magnitude point correctly in the postulate. **Disposition correction: was `soft-polish`; now already-in-canon.** |
| **Fresh-4** (`#der-action-selection` first-encounter miscue — no forward-pointer) | **Drifted to captured.** The segment now carries the forward-pointer to `#form-complete-agent-state` in *three* places (Formal Expression, Discussion, Epistemic Status), explicitly framing $a_t=\pi(M_t)$ as the Part-I special case $G_t=\emptyset$ of $a_t=\pi(M_t,G_t)$. The editorial miscue is fully addressed. | `01-aat-core/src/der-action-selection.md:13,35,39,57`. **Disposition correction: was `soft-polish`/`subsumed-by-audit-process`; now fully already-in-canon.** |
| **BP1–BP7, Fresh-6, Themes A–D** | Process/instruction-feedback for `doc/de-novo-audit-instructions.md` / `doc/audit-routing-instructions.md`. Already consolidated to the ledger. | `audits/polish-and-sentiment-ledger.md:78` (613842 block: SCC/cycle-handling clause; CLAUDE.md-bleed; appendix-examples-as-historical-calibration; component-local-lint caveat). Not theory gems; correctly themed. |

---

## Already-routed dispositions that now look wrong (flagged, not edited)

1. **Fresh-3 and Fresh-4 were dispositioned `soft-polish` / `subsumed-by-audit-process` ("deferred — light editorial check") in the extraction. Both are now fully resolved in canon** (CIY extraction for Fresh-3; triple forward-pointer for Fresh-4). Not "wrong" when written (2026-05-20) — they drifted to captured since. Flagging so no future agent re-opens them as live editorial debt. **No action needed; mark closed-by-canon with the loci above.**

2. **Fresh-5's *substantive* half is under-routed.** Ledger line 78 captured only the *process* flavor ("SCC/cycle-handling clause" → audit-instructions). The theory-graph question — is the SCC real structure or `depends:` design-debt — was never routed and now has a concrete answer (design-debt; B1 above). This is a routing *gap*, not a wrong disposition: the ledger entry is correct for what it covers, but it was mistaken to treat "SCC clause for the instructions" as fully discharging Fresh-5. **Recommend B1 as the corrective.**

3. **F3 standing-item.** The extraction's own first-pass scrutiny (audit file lines 339, 424) flagged that the **Path A narrow editorial fix has not executed** — `scope-composite-agent.md:79` ("composite is 'a fiction'") still stands per TODO:95. I did not re-verify line 79 first-hand this pass (accepting the extraction's read), but flag it as a standing `actionable-open` whose routed work has not landed since 2026-05-16. Per integration-is-replacement, when Path A lands it should *delete* the cross-segment contradictions, not soften them with cross-references. **No new gem; standing-item reminder.**

---

## Valueless / superseded (with locus)

- **Part IV predictions-calibration register and Part V wandering-thoughts** — cognition-flow material, no un-captured *theory* content; the methodology signal (Themes A–D, three-stage finding-progression) is already in the ledger P-block (line 78). No loss.
- **The extraction's own "First-Pass Scrutiny" tables (audit file §lines 329-410)** — these are the 2026-05-20 agent's verification log, superseded by the current first-hand re-verification above (which found two further drifts to captured). Preserve as trail; not a routing target.

---

## Bottom line

613842 is a *dense, math-heavy, already-well-mined* audit. Its three headline findings are correctly resolved in canon (F1/F2 by strengthening — F2 is the canonical no-go worked example; F3 live-tracked). The genuinely un-captured remainder is small and concentrated in the deferred "Fresh" items:

- **One real gem (B1):** the strategic-tempo SCC is spurious `depends:` design-debt, with a strengthen-first FORMAT-level fix (a `strengthens:`/`forward-ref:` field) that dissolves it without losing cross-links — confirmed first-hand via the `form-strategy-complexity-cost` ⟷ `deriv-strategy-cost-regret-bound` mutual 2-cycle. **Not captured anywhere** (only the process-clause flavor was routed). Carries re-derivable content; would be re-derived later if dropped.
- **Two feeder seeds (B2 IB-strengthening, B3 the converse depends-edge)** — B2 is a theorem opportunity hiding under a soft-polish label; B3 is the second instance that generalizes B1.
- **Two disposition drifts to flag** (Fresh-3 CIY, Fresh-4 forward-pointer) — both drifted into already-captured since 2026-05-20; close them.

No (A) ready-to-land theory/prose gem; manufacturing one would be dishonest. The careful "already in canon, here are the loci" is the honest result for the headline findings, and B1 is the honest gem.
