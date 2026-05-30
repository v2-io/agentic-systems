# G2 canon→artifact reference triage — captured 2026-05-30

Durable capture of three read-only triage agents (Explore) run during the 2026-05-30 cleanup pass, while the tool harness was intermittently dropping results. **Nothing here has been executed** — this is the input to the G2 per-segment triage (INTEGRATION-CLEANUP-TODO §G2), to be verified first-hand and landed by the lead agent + Joseph. Line numbers are agent-reported and may be slightly stale — re-grep before editing. **Non-loss:** the `land-content` rows are the ones where canon may actually depend on artifact content; do not delete or wipe any cited artifact until that content is verified present, self-contained, in canon.

Disposition vocabulary: **delete-vanity** (canon already self-contained; ref vestigial) · **demote-to-WN** (provenance breadcrumb, move to Working Notes) · **land-content** (load-bearing; the artifact holds something canon needs — quote it into canon before removing the ref) · **keep** (legitimate, e.g. forward-pointer to an open-problem register) · **ambiguous** (needs case-by-case verification).

## Headline pattern (gem-hunt drift, confirmed)

Most references are **vanity** — the empirical/structural claim is already stated self-contained in the segment body; the path ref is vestigial reproducibility metadata. The real work is a manageable set of **land-content** + **demote** + **delete**, plus fixing **~14 stale paths** where canon points at a `spikes/spike-X.md` that has since moved to `spikes/.integrated/spike-X.md` (active staleness — canon sends readers to a dead path). Agent 1 found **71 canon refs** in 01-aat-core (42 existing / 29 missing-path); Agent 2 found **~12 sim/empirical** refs (mostly vanity); Agent 3 found **8** in 02/03/04 (7 demote, 1 land).

## CRITICAL — land-content / non-loss items (verify first; do NOT wipe artifacts until landed)

- **`form-composition-closure.md`** — **~9** refs to projection/bridge/Kalman spikes, several **MISSING** as top-level paths. This is a major load-bearing result (composition-closure: defect bounds, bridge lemmas). Action: either quote the bound formulas in canon, or mark the result conditional/open. **Highest-priority land-content.** (Note: the `feedback_spike_references_only_in_working_notes` memory already names `form-composition-closure` Source-column cells as a known pre-existing instance — corpus-wide sweep is Joseph's call, not a unilateral purge.)
- **`deriv-critical-mass-composition.md:132,148,151,219`** — N>2 scaling + bridge lemma; refs `spike-composition-scaling-N.md`, `spike-bridge-lemma-contraction.md` (MISSING). Canonical bounds required for composition closure. land-content (or route N>2 to PROPOSED if genuinely open research).
- **`disc-identifiability-floor.md:80`** — Instance-1 bridge lemma certifying $\kappa_c \gt 0$; `spike-bridge-lemma-contraction.md` MISSING. Canon needs the bound. land-content.
- **`result-contraction-template.md:194,201,207`** (`result-`tier, ×3 in **Findings**) — differential & saddle-point contraction cases; `spike-contraction-metric-generalization.md` MISSING. Tier structure lists cases the spike defines. land-content.
- **`deriv-regime-marginal-indistinguishability.md:18`** — witness constructions are the core of the derivation; `spike-identifiability-floor-instance-6-2026-05-21.md` MISSING. ambiguous→land (segment may not stand without them — verify urgently).
- **`scope-observation-ambiguity-modulation.md:87`** (03-llm-core, Epistemic Status) — asserts the $\kappa \cdot \mathcal{A}$ product form "is structurally motivated by the survival analysis (`spikes/spike-coupled-survival-analysis.md`)" but does **not** give the structural argument in canon; the reasoning lives in the spike (now in `.integrated/`). Either land the motivation inline or restate as an honest caveat. land-content.

## Ambiguous — verify the verdict before disposing

- **`disc-stability-certificate.md:86`** & **`result-sector-persistence-template.md:112`** — both cite `spike-adjudicate-disc-m-preservation-operator.md` (MISSING; adjudication now in `.integrated/`) for the accumulation-typing / two-model-bridge dual. The structural claim ("two distinct operators, can't linearize across the pole") stands self-contained; the *parenthetical* "(independently adjudicated …)" is breadcrumb. Likely **delete-vanity / demote** per F1 of the cleanup TODO, but confirm the dual doesn't depend on the verdict.
- **`result-certificate-existence.md:134`** — R0-loss enrichment; `spike-enrichment-cluster1-…/02-r0-loss-derivation.md` MISSING-as-referenced (absorbed into canon). Verify absorbed, then delete/demote.

## Agent 1 — 01-aat-core markdown-spike/msc/audit refs (71 found; 42 exist / 29 missing-path)

delete-vanity (~9): `def-agent-spectrum.md:54` (Hafez results) · `def-value-object.md:45` (Class 3 coupling) · `der-directed-separation.md:140` ($\kappa$-scalar history) · `der-interaction-channel-classification.md:151` (Class 3 scope) · `deriv-l1-update-bias.md:94` (MC parameters; summary in canon) · `deriv-observation-ambiguity-bias-bound.md:239` (derivation history) · `form-objective-functional.md:58` (Pareto scope) · `deriv-edge-update-natural-parameter.md:131` (credit-assignment-boundary fix).

demote-to-WN (~11): `def-control-regret.md:53` (CPT verdict) · `deriv-edge-update-natural-parameter.md:115` (A2′ axiom scope), `:129` (G-BP1 log-odds design history) · `deriv-observation-ambiguity-bias-bound.md:207` (shared Pinsker machinery, future-extraction xref) · `form-composition-closure.md:177,248` (admissibility history) · others as design-history breadcrumbs.

keep (legitimate): `der-adversarial-destabilization.md:67` → `spikes/PROPOSED.md` (forward-pointer to open-problem register) · `disc-value-functional-grounding-floor.md:85,157,166` → PROPOSED + Cohen-2022 verdict (open-instance tracking) · `der-architecture-noidentifiability.md:129` (Fano-degenerates-at-I=0, load-bearing for the no-go) · `der-directed-separation.md:26,128,132,168,187` (Class-inheritance structure) · `disc-dynamic-regime-axis.md` & `disc-modularity-state-dynamics.md` (Soviet worked example; `msc/modularity-cycle-plan` cross-discipline — note: CLAUDE.md:28 forward-ref, F6-adjacent) · `obs-section-i-validation-simulations.md:52,84`.

**Stale-path fix (~14):** canon refs to `spikes/spike-X.md` that now live at `spikes/.integrated/spike-X.md`. Per `feedback_spike_references_only_in_working_notes` pt 5: **reduce-or-remove, do NOT repoint** to `.integrated/` (repointing was a prior corrected error). Examples named: `spike-4th-identifiability-floor-instance-2026-05-20`, `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24`, `spike-enrichment-cluster1-2026-05-21/*`.

## Agent 2 — sim/empirical refs (all volumes; mostly vanity)

delete-vanity (8): `obs-gated-tempo-advantage.md:55` · `deriv-causal-ib-exploration.md:105` (0% survival result in canon) · `disc-exploit-explore-deliberate.md:51` · `example-strategy.md:405` · `result-adversarial-exponent-regimes.md:70` · `result-per-dimension-persistence.md:134` (4-sig-fig / 72%-overestimate in canon) · `def-agent-spectrum.md:68` ($P$ monotonic in $\mathcal{T}$) · and `obs-section-i-validation-simulations.md:52` body table self-contained.

demote-to-WN (3, queued/future work): `deriv-causal-ib-lmi.md:165` (2D sim is queued, not landed) · `der-code-quality-as-observation-infrastructure.md:134` (`empirical-discontinuity/`, future operationalization) · `emp-changeset-size-principle.md:57` (proposed extension).

clarify-status (mixed landed+open): `hyp-exponential-cognitive-load.md:48` (file-level $\alpha \approx 0.118$ is landed → stays; per-level "untested" → WN) and `:74` (`spike-transient-dependency-amplification.md` is a *prospective* derivation path, not landed — mark as such).

**Canonical exception — KEEP:** `obs-section-i-validation-simulations.md:52` is a segment whose *subject is* the validation program; its file list is a reproducibility registry, not knowledge-injection, and all results are stated self-contained (lines ~30–93). Keep; flag the list explicitly as a reproducibility registry. (At publication: the registry becomes an external citable code release/DOI, not a local path.)

## Agent 3 — 02/03/04 markdown refs (8 found; very clean)

land-content (1): `scope-observation-ambiguity-modulation.md:87` (see Critical above).

demote-to-WN (7): all `audits/AUDIT-WORKING-193847/` citations in `disc-five-forcing-functions.md:29,34`, `scope-interiority-loop.md:45,47`, `def-auxilia-hierarchy.md:41,70,72`. The key audit quotes are already lifted verbatim into canon Discussion; the audit-file pointers are provenance → Working Notes. **Note the gold-dir gate:** `AUDIT-WORKING-193847` is de-novo-first-encounter cognition ("the gold") — demoting the *canon pointers* to WN is fine, but do not process/mine/move the AUDIT-WORKING dir itself without consulting Joseph.

## Suggested execution order when resumed (after harness fix)

1. **Stale-path reduce-or-remove (~14)** — pure staleness, lowest risk, highest "broken pointer" payoff.
2. **delete-vanity (~17 across agents)** — quick, canon already stands.
3. **demote-to-WN (~21)** — mechanical moves to Working Notes.
4. **land-content (~6, NON-LOSS)** — the careful work: `form-composition-closure` first, then the bridge-lemma / contraction / witness / $\kappa\cdot\mathcal{A}$-motivation cases. These may need new appendix content; do not rush, do not wipe sources until landed.
5. Re-run `bin/extract-findings` (the ~3 Findings-section refs roll into `FINDINGS.md`).
