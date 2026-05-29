---
source_cycle: 584721 (de-novo, Claude Opus 4.7, 2026-04-25; first v2-instructions run)
extraction_agent: Claude Opus 4.7 (1M context), sweep run #2
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-584721/ (54 files, 3644 lines)
final_of_record: audits/.integrated/audit-584721-FINAL-2026-04-25.md
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-16 — Cluster B: math-heavy ledgered"
related_ledgers: audits/polish-and-sentiment-ledger.md (S22 §D research-seeds; S29 §D.4/D.7 polish; P-block §A.1–A.4 process-feedback)
prior-batch-context: audits/pending-findings-2026-04-22.md (the F-V series this audit triangulated against)
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. The 584721 cycle was the first v2-instructions de-novo
  run and is simultaneously the audit and the iteration on the audit's own
  instructions; the FINAL preserves §A on that stress-test. The 54-file working
  dir adds: (a) the distinctive pre-report-inventory artifact (the auditor's
  state-snapshot at §6.1 Phase-2 transition); (b) the per-segment
  predictions-calibration trail; (c) the F-A root-cause discovery sequence
  (segment 08 mid-walk realization that F-A0 → F-A2/3/5 fold); (d) extensive
  §14 wandering-thoughts material on consciousness-infrastructure connections,
  Hafez IDT propagation, and OKR/AAT mapping. The full FINAL §D (research
  seeds) routed to ledger S22, §D.4/D.7 to S29 polish, §A to P-block.
---

# Audit-findings extract — 584721 working-dir mining

The 584721 cycle was the first v2-instructions run, by the same agent who
drafted the instructions (with substantial mid-session iteration with Joseph).
Coverage: AAT Section I rows 1–30 (all) + 4 cited Appendix-A derivations
in-context + Section II rows 1–26 (of ~28). Section III, ~20 remaining
Appendix-A segments, all Appendix-B worked examples, all of TST, all of
`03-llm-core/`, and all of `04-eli-core/` not read first-hand. ~52 reflection
files (10 batched as `01-section-i-leaves.md` under pre-strengthening
discipline; 51 individual reflections from row 11 onward).

What the WORKING dir adds beyond the FINAL: (1) **the F-A series cognition
trail** — segments 01, 02, 03, 05, 08 walking the discipline-edge findings,
with the **root-cause realization mid-segment-08** ("F-A0 → F-A2/3/5 fold;
one editorial change with multi-segment impact") that the FINAL preserves
only as the table; (2) the predictions-calibration register (the
`00-initial-predictions.md` predictions tested against per-segment
reflections); (3) **the distinctive `00-pre-report-inventory.md` artifact** —
a snapshot at §6.1 Phase-2 transition explicitly enumerating coverage gaps,
findings-to-triangulate, Section D candidates, and Section E confirmations
*before* the FINAL was written; (4) Section D candidates with their
per-segment provenance traces, several of which converge across multiple
reflections; (5) the prompt-12/13 (subjective value / field contribution)
material from reflection 24 onward — register-distinct from verification
prompts and producing different yields.

This file extracts at three weights: **(I+II) findings already adjudicated
by FINAL/MANIFEST** (preserved with WORKING-dir provenance); **(III) fresh
material the FINAL didn't carry forward** (theme-grouped); **(IV)
predictions-calibration register**; **(V) §14 wandering-thoughts
theme-grouped**, including the distinctive **§14-bonus: the §A
instructions stress-test cognition trail** that lives in the working dir
as a recursive instance of the auditor running the v2 protocol while
iterating it with Joseph.

---

## Part I — Findings already adjudicated (subsumed-by-FINAL / MANIFEST)

These appear in the WORKING dir as candidate-findings developing toward
the §B list. Each is preserved with its WORKING-dir provenance so the trail
is recoverable; the MANIFEST 2026-05-16 (Cluster B) row is the truth-arbiter.

### F-A-trail. Depends-list-incomplete-vs-Formal-Expression (root-cause + propagated cluster)

The 584721 cycle's headline finding and the one cross-cycle with 471203 §B
F5. The WORKING dir's contribution is the **root-cause discovery sequence**
that the FINAL preserves only as the seven-row table.

**WORKING-dir trail.**

- **Reflection 01 (`01-section-i-leaves.md`):** First instance flagged at
  `scope-adaptive-system` (F-A1) — depends list contains
  `[def-agent-environment, def-observation-function]` but Formal Expression
  uses $\mathcal{C}_t$ (defined in `def-chronica`). Auditor's first
  attempt at charitable counter-read explicitly tested: "Could
  `scope-adaptive-system` be using $\mathcal{C}_t$ as 'background math'
  not requiring AAT-internal segment dependency? No — $\mathcal{C}_t$ is
  an AAT-specific symbol with a dedicated segment defining it."
  Counter-read failed; finding promoted.
- **Reflection 02 (`02-form-information-bottleneck.md`):** Second instance
  (F-A2) at `form-information-bottleneck`. Auditor names the pattern at
  N=2: *"Worth tracking as a pattern. If a third instance appears, it's a
  systematic discipline issue rather than two isolated misses."*
- **Reflections 03–05:** Two more instances (F-A3, F-A4) at
  `def-model-sufficiency` and `form-event-driven-dynamics`. The pattern
  is now clearly systematic.
- **Reflection 08 (`08-def-mismatch-signal.md`) — THE ROOT-CAUSE REALIZATION:**
  Auditor walks through transitivity carefully and discovers that
  `def-observation-function` (Section I row 2) **itself** has Formal
  Expression $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ using $a_{t-1}$
  without depending on `def-action-transition`. This means F-A drift is
  rooted at row 2; every downstream segment whose action-symbol coverage
  runs through `def-observation-function` (or through `form-agent-model`,
  which inherits) inherits the missing dependency transitively.
  
  Auditor's explicit re-numbering:
  
  | # | Segment | Row | Symbol | Missing dep | Status |
  |---|---|---|---|---|---|
  | F-A0 | def-observation-function | 2 | $a_{t-1}$ | def-action-transition | ROOT |
  | F-A1 | scope-adaptive-system | 4 | $\mathcal{C}_t$ | def-chronica | Independent |
  | F-A2 | form-information-bottleneck | 11 | $a_{t:\infty}$ | def-action-transition | Propagated |
  | F-A3 | def-model-sufficiency | 12 | $a_{t:\infty}$ | def-action-transition | Propagated |
  | F-A4 | form-event-driven-dynamics | 14 | $M_{\tau^-}$ | form-agent-model | Independent |
  | F-A5 | def-mismatch-signal | 17 | $a_{t-1}$ | def-action-transition | Propagated |
  | F-A6 (folded) | result-mismatch-decomposition | 18 | $a_{t-1}$ | def-action-transition | Propagated |
  
  **Root-cause fix:** add `def-action-transition` to
  `def-observation-function`'s depends. Propagates for F-A2/F-A3/F-A5/F-A6
  transitively. Two independent fixes remain (F-A1, F-A4).

- **Reflection 09 (`09-result-mismatch-decomposition.md`):** Sixth instance
  surfaces and is **folded** under F-A0 root-cause rather than logged
  separately — the auditor consciously stops enumerating once the
  root-cause is identified. Self-discipline note in the reflection: *"if
  3+ instances of a finding-pattern, look for a single upstream cause."*

**Disposition (per MANIFEST 2026-05-16 Cluster B):** **`resolved, the
majority by strengthening`** — bundled disposition with 742613-F3/F5/F8 +
opus-2026-04-21 §1–4 + 738192-F1/F2. Per-finding detail in adjudication
628401.

**First-hand verification against current `src/` (2026-05-20):**

- `01-aat-core/src/def-observation-function.md` frontmatter `depends:
  [def-agent-environment, def-action-transition]` ✓ **F-A0 resolved**;
  stage `deps-verified`.
- `01-aat-core/src/scope-adaptive-system.md` frontmatter `depends:
  [def-agent-environment, def-observation-function, def-chronica]` ✓
  **F-A1 resolved**; stage `claims-verified`.
- `01-aat-core/src/form-event-driven-dynamics.md` frontmatter `depends:
  [post-causal-structure, def-observation-function, def-action-transition,
  form-agent-model]` ✓ **F-A4 resolved**; stage `deps-verified`.
- The propagated instances (F-A2/A3/A5/A6) inherit the fix transitively
  via the F-A0 repair; not separately verified beyond frontmatter
  inspection. Auditor's transitivity argument is correct.

**Cross-cycle convergence:** F-A cluster is the same class as 471203 §B F5
(`post-composition-consistency` derivation-hierarchy) and 471203's MANIFEST
disposition explicitly cross-references "F-A cluster (584721/742613)" — i.e.,
**three cycles (471203, 584721, 742613) converged independently on the
post-composition-consistency / depends-discipline pattern**. The 584721
contribution is the *root-cause discovery* (one upstream fix propagates);
the 471203 contribution is the *systematic-discipline framing* (PROPOSALS
SP-6 / TODO:149). Together they constitute a strong-evidence finding-class
that the MANIFEST treats as "already routed" rather than as a graduation
blocker. The auditor's segment-08 self-discipline note ("if 3+ instances of
a finding-pattern, look for a single upstream cause") is itself
methodologically valuable for future audits.

### F-D-trail. Bretagnolle-Huber-identity incomplete propagation

Two instances of segments using older Pinsker bound where the canonical
`#deriv-strategy-cost-regret-bound` had been upgraded 2026-04-24 to use
the strictly-sharper BH-identity.

**WORKING-dir trail.**

- **Reflection 35 (`35-disc-ciy-unified-objective.md`):** F-D1 surfaced.
  The auditor names this as integration-debt rather than math error,
  explicitly: *"The Pinsker bound is valid (just not tightest), so this
  isn't a math error. But it's a mild integration debt around the recent
  BH-identity addition."* Suggested fix: editorial cross-reference.
- **Reflection 50 (`50-form-strategy-complexity-cost.md`):** F-D2 surfaced.
  Auditor notes this segment is *more sophisticated* than F-D1 — the
  Pinsker retention is defended for IB-shape alignment with the linear-KL
  form, which is a legitimate technical reason. But the segment doesn't
  cross-reference BH-identity as the available sharper alternative.

**Disposition (per MANIFEST 2026-05-16 Cluster B):** **`resolved`**, bundled
under the strengthening-cluster disposition.

**First-hand verification against current `src/` (2026-05-20):**

- `01-aat-core/src/disc-ciy-unified-objective.md:66` — the "Regret-bound
  connection to the strategy-cost objective" paragraph now carries the
  BH-identity treatment explicitly: *"Under AAT's canonical scope of
  deterministic $\pi^\ast$, the Bretagnolle-Huber identity
  $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 -
  \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ holds exactly (Bretagnolle &
  Huber 1978), giving the tight regret bound $R(Q_{\Sigma_t}) \leq
  V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ with
  matching lower bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$ on
  isolated optima."* Cross-references `#deriv-strategy-cost-regret-bound`
  §4 + §6.1. ✓ **F-D1 resolved by strengthening**.
- `01-aat-core/src/form-strategy-complexity-cost.md:141` — the "On
  $\beta_\Sigma$ interpretation" Epistemic Status paragraph now explicitly
  names the BH-identity as the *primary* form under deterministic
  $\pi^\ast$ and defends Pinsker retention as IB-shape alignment + correct
  general form for stochastic-$\pi^\ast$ extensions: *"Under AAT's canonical
  deterministic-$\pi^\ast$ scope, the sharper Bretagnolle-Huber identity $R
  \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$
  holds as the primary form."* ✓ **F-D2 resolved by strengthening + scope
  honesty**.

### F-B1-trail. Stale "Section IV" / `AAD-FULL.md` reference

**WORKING-dir trail.** Logged at `00-pre-report-inventory.md` §"F-B1
(low-confidence, candidate)" + reflection 05 (`05-form-event-driven-dynamics.md`).
Severity: low / doc-rot. Status: unverified first-hand.

**Disposition (per MANIFEST 2026-05-16 Cluster B):** **`resolved`**, bundled
under the strengthening-cluster.

**First-hand verification against current `src/` (2026-05-20):**

- `01-aat-core/src/form-event-driven-dynamics.md:78` now reads: *"The
  three-part tempo decomposition for software — $\mathcal{T}_{\text{obs}}$
  (compiler, tests) + $\mathcal{T}_{\text{explore}}$ (code reading) +
  $\mathcal{T}_{\text{probe}}$ (test runs, staging) — is a direct
  application of multi-channel tempo. The formal development of this
  decomposition is a TST-side question (open GAP in
  `02-tst-core/OUTLINE.md`)."* The `Section IV` and `AAD-FULL.md`
  references have been repointed cleanly to the post-component-split
  location. ✓ **F-B1 resolved**.

### F-C series (retired mid-audit) — appendix-back-pointer convention

**WORKING-dir trail.** Seven instances logged (F-C1 at reflection 06,
F-C2 at reflection 13, F-C3/F-C4 at reflection 15, etc.) before the
mid-session §4.2 refinement landed the appendix-back-pointer exception.
Auditor explicitly retires the F-C series in `00-pre-report-inventory.md`:
*"7 instances of appendix-back-pointer 'critical findings' originally
logged. Per §4.2 mid-session refinement (appendix-back-pointer exception),
these are not findings — they're the standard 'result-in-body,
proof-in-appendix' convention. Recasting as Section E confirmation."*

**Disposition:** retired pre-FINAL by the auditor; preserved in the working
dir as instructions-improvement provenance (the §4.2 exception that the
mid-session iteration landed). Not a finding in the routing sense; recorded
under the P-block (instruction-set evolution).

---

## Part II — Bigger-picture observations (already in FINAL §D + ledger S22/S29)

These are FINAL §D observations at Hypothesis-tier level, accumulated across
the working dir and consolidated at FINAL-time. Routed to polish-ledger S22
(research-seeds, the strongest being D.3 correction-capacity-collapse) and
S29 (polish; D.4 and D.7).

### §D.1 — Six-mechanism convergence on shallow-plan preference

**WORKING-dir trail.** Accumulated across reflections 14, 21, 37, 49, 50.
The mechanisms each surfaced in their own segment-reflection; the
synthesis lives in `00-pre-report-inventory.md` §"Section D candidates"
item 1 and was finalized at FINAL §D.1. The six mechanisms:

1. Confidence decay (`#der-chain-confidence-decay`)
2. Evidence starvation (`#deriv-edge-credence-dynamics`,
   `#der-observability-dominance`)
3. Cognitive cost (`#form-strategy-complexity-cost`)
4. Strategic-tempo bottleneck (`#def-strategic-tempo`)
5. Identifiability degradation (`#scope-edge-update-causal-validity`)
6. Interaction-horizon compression (Miller 2022, surfaced via
   `#form-strategy-complexity-cost` Discussion)

Reflection 50 carries the *consolidation moment* — auditor names the
"triple depth penalty" already-consolidated state + adds three more
mechanisms reaching the six-count. Proposed elevation: subsection in
`#disc-separability-pattern` or own meta-observation segment.

**Disposition:** → **ledger S22** (research-seed; natural
`#disc-separability-pattern` extension). Open.

### §D.2 — OKR / AAT operational mapping as domain-instantiation template

**WORKING-dir trail.** Surfaced at reflection 47
(`47-disc-credit-assignment-boundary.md`), §"What am I now curious about?
(b)". The auditor's strongest engagement-register moment in Section II
— *"This was unexpected and is one of the framework's clearest domain
instantiations."* Promoted in reflection 47 §"How valuable does this
segment feel to me?" to top-decile.

Proposed action: treat the OKR mapping as a *template* — military OODA,
scientific method, biological adaptation, organizational strategy each
get similar 4–6-row failure-mode→AAT-quantity tables. Approachability /
Feynman-criterion connection.

**Disposition:** → **ledger S22** (research-seed; domain-template
material). Open.

### §D.3 — Correction-capacity-collapse unification (STRONGEST §D candidate)

**WORKING-dir trail.** This is the §D candidate the audit returned to
most across reflections. Surfaced first in reflection 15 (FM-2 in
`der-gain-sector-bridge`): *"gain collapse / stability-induced-myopia /
detection-latency-blowup are three names for what may be the same agent
failure mode."* Reinforced in reflection 21
(`21-result-sector-persistence-template.md`) §(b): *"connects to
gain-collapse / stability-induced myopia / detection-latency-blowup —
multiple threads converging on 'experience discounting / forgetting /
consolidation as architectural primitive.'"* Reinforced again in
reflection 22 §(d): the *"structural adaptation as deliberation with
massive $\Delta\tau$" framing keeps recurring without being formalized.*
Reinforced in reflection 24
(`24-form-consolidation-dynamics.md`): consolidation-as-named-regime + EWC
vs consolidation as alternative escapes.

Consolidated in FINAL §D.3 + `00-pre-report-inventory.md` item 4:
*"experience-discounting / forgetting / consolidation as architectural
primitive."* The unification thesis: four threads describe one underlying
pathology — agent's correction capacity falls below the rate at which
the environment / strategy needs revising. Names differ (gain collapse;
stability-induced myopia; catastrophic forgetting; detection-latency
blowup). Mechanisms overlap ($U_M / U_o$ ratio collapse; $\alpha_\Sigma$
decay; $1/(n+1)$ rate-floor; IB-gap accumulation).

Proposed action: a `#disc-correction-capacity-collapse` discussion
segment cataloguing the four manifestations and the unified mechanism.

**Disposition (per ledger S22):** **open research-seed; graduate-watch
*pending M4 subsume-check*.** Overlaps strongly with M4
modularity-state-dynamics (the three-operation picture in the
`msc/modularity-cycle-plan-2026-05-09.md` scoping). The check is: does
the M4 cycle subsume this, or do they live as parallel meta-segments?

**First-hand verification against current `src/` (2026-05-20):**

- `01-aat-core/src/disc-correction-capacity-collapse.md` does **not**
  exist. The unification is still latent across the four named segments
  (`emp-update-gain` Discussion; `form-consolidation-dynamics`;
  `schema-strategy-persistence`; `der-observability-dominance`). The
  S22 ledger status (open + pending M4 subsume-check) matches present
  `src/` state.
- `01-aat-core/src/disc-modularity-state-dynamics.md` also does not exist
  (M4 cycle not yet landed per CLAUDE.md note); the M4 subsume-check
  cannot complete until M4 itself lands. **Routing-status correct.**

### §D.4 — Matched-vs-forced coordinate distinction in `disc-additive-coordinate-forcing`

**WORKING-dir trail.** Surfaced in reflection 15
(`15-der-gain-sector-bridge.md`) §(11): the *forced* coordinates at
chain/divergence/update/metric layers vs the *matched* Lyapunov quadratic.
Promoted to FINAL §D.4. Proposed action: a one-paragraph addition to
`#disc-additive-coordinate-forcing`'s opening that tabulates the *forced
/ matched / adopted* distinction across all four-plus coordinate layers.

**Disposition:** → **ledger S29** (polish; candidate co-owner direct-fix).
Open.

### §D.5 — CLAUDE.md / MEMORY.md auto-load priming as structural feature

**WORKING-dir trail.** Surfaced explicitly in `00-initial-predictions.md`
§"Priming bleed" + `00-initial-predictions.md` §"Meta-issue I want to
surface to Joseph now". Mid-session resolution: CLAUDE.md → CLAUDE.md +
CLAUDE-2.md split (sunset 2026-04-28, see `_obs/CLAUDE-2-superseded-2026-04-28.md`);
MEMORY/CHANGELOG migration; README de-priming.

**Disposition:** → **P-block** in polish-ledger (audit-process /
instruction-set feedback). Attributed to 584721 §A.2. Substantially
resolved by the post-cycle CLAUDE.md split + MEMORY trimming. The lesson
("auto-load files must be designed for the de-novo-audit case, not just
the everyday-work case; tier-split as a clean pattern") is the durable
P-block content.

### §D.6 — Type/token distinction as meta-architectural commitment for `03-llm-core`

**WORKING-dir trail.** Surfaced in reflection 25
(`25-scope-agent-identity.md`) §(a): *"AAT applies to tokens, not types.
But 'the GPT-4 model' framings are ubiquitous in AI discourse.
Aggregated-across-tokens claims would need additional machinery."*
Connection to clone-problem formalization.

**Disposition:** → **ledger S22** (research-seed; preface/scope
material for `03-llm-core/OUTLINE.md`). Open.

### §D.7 — Diagnostic-CIY four-axis propagation to `disc-exploit-explore-deliberate`

**WORKING-dir trail.** Surfaced from `00-pre-report-inventory.md` §11
(four-axis CIY extension). The `#der-causal-insufficiency-detection`
segment adds "diagnose" as a fourth axis to the explore/exploit/deliberate
three-axis framing in `#disc-exploit-explore-deliberate`. Propagation
hasn't landed in the canonical exploit-explore-deliberate segment.

**Disposition:** → **ledger S29** (polish; candidate co-owner direct-fix).
Open.

**First-hand verification against current `src/` (2026-05-20):**

- `grep -n "diagnose\|four-axis" 01-aat-core/src/disc-exploit-explore-deliberate.md`
  returns no hits. **D.7 still open** — the diagnostic-CIY four-axis
  extension has not propagated to the canonical segment. Matches S29
  ledger status.

### §D.8 — Seven-attack discipline pattern as FORMAT.md convention candidate

**WORKING-dir trail.** Surfaced in reflection 06
(`06-der-recursive-update.md`) and reinforced in reflection 18
(`18-deriv-recursive-update.md`). The `#deriv-recursive-update` appendix
tests its claim against seven counterexamples; auditor proposes this as a
discipline-pattern other inevitability-core segments could adopt.

**Disposition:** → **ledger S22** (research-seed; potential FORMAT.md
convention for inevitability-core segments). Open.

---

## Part III — Fresh material the FINAL didn't carry forward

Observations present in the WORKING dir's per-segment reflections, the
pre-report inventory, and the initial predictions that did **not** make
it cleanly into the FINAL's §B/§D framing, or that ended up as one-line
consolidations when they had richer structure in the working notes.

### Fresh-1. The "F-A0 root-cause realization" as audit-methodology pattern (self-discipline)

The mid-segment-08 root-cause realization is a methodologically valuable
audit-internal discipline that the FINAL preserves only in its
*outcome* (the seven-row table) but not in its *form* (the auditor's
explicit self-rule: "if 3+ instances of a finding-pattern, look for a
single upstream cause"). This is a transferable audit-methodology
discipline, not just a finding-shaping rule. The original quote
(reflection 08, §10): *"Worth noting as a self-discipline going forward:
if 3+ instances of a finding-pattern, look for a single upstream cause."*

This pattern recurs in framework work generally — when a finding-class
hits N=3+, ask whether the *finding* is the issue or whether a single
upstream change collapses the cluster. Could be added to
`doc/de-novo-audit-instructions.md` §4.4 prompts as a recognition trigger.

**Suggested disposition:** `process/instruction-feedback` — material for
any future revision of `doc/de-novo-audit-instructions.md`, alongside the
P-block content (the §4.4 cadence + auto-load priming lessons). One
sentence at the prompt level would carry the discipline forward.

### Fresh-2. The `00-pre-report-inventory.md` as a methodologically distinctive artifact

The 584721 cycle has a distinctive working artifact the other working
dirs don't appear to share: an explicit *state-snapshot* the auditor
produced at the §6.1 Phase-2 transition (per Joseph's redirection),
*before* writing the FINAL. The file lists:
- Coverage statement (what was read first-hand vs not)
- Findings to triangulate against tracking docs
- Section D candidates (12 items, with attribution-trace)
- Section E confirmations (10+ items)
- Triangulation targets for Phase-2

This pre-report-inventory acts as a *cognition-state checkpoint* — the
auditor commits to the current findings/observations *before* doing the
Phase-2 triangulation work (reading TODO/PROPOSALS/pending-findings).
This is the inverse of recency-bias in audits: the auditor's
unprimed-by-tracking-docs read is captured first, then triangulated.

**Methodological value:** the artifact is the **anti-bleed device** for
the Phase-2 read. Future audits could adopt it explicitly: at §6.1
transition, write your inventory *before* reading the tracking docs;
the inventory is then immune to "I'll just adjust my read to match
what's already known."

**Suggested disposition:** `process/instruction-feedback` — strong
candidate for `doc/de-novo-audit-instructions.md` §6.1 (Phase-2
transition protocol). The pattern is: "pre-report-inventory" as a
named transition artifact. Cross-references the P-block §A.2
(auto-load priming) and the Phase-2 triage vocabulary the 742613 cycle
contributed (per ledger P-block).

### Fresh-3. The "system-vs-component-level architectural classification" observation

Reflection 28 (`28-der-directed-separation.md`) §(c) surfaced an
observation the FINAL didn't carry: the LLM is Class 2 internally, but
the *agent system* (LLM + tools + memory + monitoring) can be Class 1
at the system level. The architectural classification depends on where
the agent-environment boundary is drawn. *"Worth explicit treatment in
03-llm-core."*

This is operationally distinct from the existing "class-coercion-via-wrapping"
framing in `#der-class-coercion-via-wrapping` — that segment is about
*structurally constructing* a Class-1 wrapper around a Class-2 component
(W₁/W₂ via committed query-rules / output-structuring). The
system-vs-component observation is about *where you cut the boundary
when classifying* — the same physical system admits multiple legitimate
classifications depending on the analytical frame.

This complements wrapping (wrapping *creates* a Class-1 wrapper;
system-vs-component-level *recognizes* an existing wrapper at the analytic
boundary). Worth a sentence in `03-llm-core/OUTLINE.md` preamble.

**Suggested disposition:** `research-seed` / framing-material —
candidate for explicit treatment in `03-llm-core/OUTLINE.md`. Light
weight; could be co-owner direct-fix.

### Fresh-4. The "IDT sidecar as engineering pattern" promotion candidate

Reflection 28 §(b) and §"What would I change?" surfaced the Hafez 2026
IDT sidecar pattern — "Class 1 monitoring of Class 2 agents via
external $(S,A,S')$-stream monitor; 89%/44% perturbation detection" —
as currently buried in Working Notes of `#der-directed-separation`. The
auditor flagged: *"the IDT sidecar pattern (Hafez 2026) buried in
Working Notes deserves Discussion-level surfacing — it's the empirical
support for 'Class 1 monitoring of Class 2 agents is feasible and
effective.'"*

This is operationally significant for AI-safety / alignment audiences:
the framework gives a *principled path* for monitoring opaque
(Class 2) agents — wrap with Class 1 sidecars on the behavioral stream.
The empirical numbers from Hafez 2026 are strong.

**Suggested disposition:** `actionable-open` (editorial promotion) —
move the IDT Working Notes paragraph in `#der-directed-separation` to
Discussion or split as standalone observation segment. Light editorial.
Cross-references the class-coercion-via-wrapping cycle.

### Fresh-5. The "(N1)+(N2) consolidation-necessity-vs-luxury mapping" as cross-domain template

Reflection 24 (`24-form-consolidation-dynamics.md`) §(a) and §"What
does the framework now potentially contribute to the field?" surfaced
the luxury-vs-necessity diagnostic for consolidation. Luxury cases:
Kalman, conjugate-Bayesian, linear-Gaussian. Necessity cases: everything
else. The diagnostic ((N1) factorization depth × (N2) budget vs
integration-cost gap × event-arrival rate vs cross-episode regularity
rate) operationalizes the question *"does my agent architecture need
consolidation?"* before adding consolidation machinery.

The FINAL's §D.3 (correction-capacity-collapse) unifies the *pathology*
side; (N1)+(N2) is the *operational-diagnostic* side. They're sibling
observations, not duplicates. The diagnostic could land as a
chapter-end `#impl-*` segment under `01-aat-core/` or as a TST-style
calibration table.

**Suggested disposition:** `research-seed` — adjacent to S22 D.3 but
operationally distinct. Worth a separate row or a sub-row under D.3.

### Fresh-6. The "EWC vs consolidation as alternative escapes" unification candidate

Same reflection 24 §(b) — EWC (Kirkpatrick 2017) and consolidation
(McClelland 1995 CLS) are *both* escapes from catastrophic forgetting,
but they're structurally different (per-parameter stability weights
vs. offline replay-based realignment). The framework names both but
doesn't unify them. Auditor's specific question: *"Curious whether
tensor-valued gain ever lands as a derived generalization of $\eta^*$."*

This is a strengthening direction (heuristic → derived): EWC's
stability-weighted update is a tensor-valued generalization of
`#emp-update-gain`'s scalar $\eta^*$. Could land as a derived
extension of the gain formalism.

**Suggested disposition:** `research-seed` (spike-shaped); strengthening
direction. Cross-references S22 D.3 (correction-capacity-collapse
cluster). Could be a spike under "tensor-valued $\eta^*$ via stability
weights."

### Fresh-7. The "Class 2 $Q_O$ degradation magnitude bound" question

Reflection 30 (`30-def-value-object.md`) §(b) — `def-value-object` knows
Class 2 agents have biased $Q_O$ (Working Notes flag) but doesn't
quantify the bias. *"Is the bias bounded by $\kappa_{\text{processing}}$?
Or by some other measure?"* The `deriv-bias-bound` segment (Track 1
transport-inequality + Track 2 Fisher-Rao with universal $C_{FR} =
\sqrt{2}$ under (PI)+Čencov per CLAUDE-2.md priming) might address
this — but the connection isn't explicit in `def-value-object`.

**Suggested disposition:** `actionable-open` (cross-reference fix) —
add a sentence to `def-value-object` Epistemic Status pointing to
`#deriv-bias-bound` (or whichever appendix carries the quantitative
Class-2 bias bound). Light editorial; if the connection turns out not
to hold (the bias-bound segment may not directly bound $Q_O$
degradation), this becomes a `research-seed` instead.

### Fresh-8. The "convention specification propagation" check across Section II

Reflection 30 §"What errors should I now watch for?" — the C1/C2/C3
convention from `#def-value-object` is *part of the measurement* of
$\delta_{\text{sat}}$ / $\delta_{\text{regret}}$. The auditor flagged
Phase-2 work: "check whether downstream segments using $\delta_{\text{sat}}$
/ $\delta_{\text{regret}}$ specify their convention." If not, the
values aren't comparable.

Note: this is the **same Fresh-9 observation as the 471203 extraction**
— cross-cycle convergence (independent auditors flagging the same
verification target). The convention-specification check has now
surfaced from two cycles independently.

**Suggested disposition:** `actionable-open` (verification / tooling-gap)
— could be a one-shot `bin/`-style lint check across §II/§III segments
for uses of $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ without
C1/C2/C3 specification. Cross-cycle convergence with 471203 strengthens
the routing.

### Fresh-9. The "Aguilera 2022 FEP-flow narrow-validity citation" verification-target trail

Reflection 21 (`21-result-sector-persistence-template.md`) §(d) flagged
the AAT-vs-FEP-flow comparison citation for spot-check: *"does Aguilera
2022 actually say what AAT claims (FEP-flow validity narrow)? CLAUDE-2.md
says it does ('Aguilera 2022 FEP-narrow-validity claim exactly matches
AAT's usage'), based on prior citation audit. So this should hold."*

The auditor *deferred* the citation spot-check, trusting the prior
citation-audit's verification. This is honest scope-keeping but the
trail is worth preserving — Aguilera 2022 (and the broader FEP-flow vs
AAT positioning) is load-bearing for AAT's "broader-validity Lyapunov
approach" claim, and a future citation cycle should re-verify it
first-hand rather than chain-of-trust on prior audits.

**Suggested disposition:** `phase-2-verification-target` / `research-seed`
— add Aguilera 2022 to any future citation-verification pass, with
specific check: does Aguilera 2022 establish FEP-flow narrow-validity
in the form AAT's `#result-sector-persistence-template` cites it?

### Fresh-10. The "naive-L1 fails (factor above the correlation, not in parallel with it)" engineering insight

Reflection 39 (`39-def-strategy-dag.md`) §(a) — the auditor surfaced
a real engineering insight buried in `#def-strategy-dag` Discussion:
*"Common cause as parent of both alternatives, alternatives remain
OR-siblings"* gives the *same* overestimate as L0. The correct
construction is $G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}}
= \text{OR}(A_1, A_2)$. **Factor above the correlation, not in parallel
with it.**

The auditor's framing: *"This is a real engineering insight that
practitioners would otherwise miss."* The principle has a memorable
shape ("factor above") and operationalizes the Correlation Hierarchy
in a way that would be missed by readers who treat L1 as "just add a
common-cause node."

**Suggested disposition:** `research-seed` / framing-material — candidate
Brief-field framing for `#def-strategy-dag` ("factor above the
correlation, not in parallel with it"); approachability /
Feynman-criterion connection. Could be elevated in the segment's
Discussion or Brief.

### Fresh-11. The "non-Gaussian / non-convex coupling per-case computation" scope-restriction echo

Reflection 47 (`47-disc-credit-assignment-boundary.md`) implicitly + the
broader Section II walk surfaced that AAT's exact-tier results
concentrate in linear-Gaussian / conjugate-Bayesian / strongly-convex
regimes. The auditor consolidated this in the working dir's calibration
material (per `00-pre-report-inventory.md` Section E) but the FINAL
treats it as Section E confirmation rather than a research-seed.

Note: this is **the same Fresh-3 observation as the 471203 extraction**
(16-cell closure restriction to scope α). Cross-cycle convergence on
"AAT's exact-tier regime is narrower than its general scope"
recognition. Multiple auditors independently noting the
linear-Gaussian-concentration would be material for a *project-positioning*
observation in framing-level material.

**Suggested disposition:** `sentiment/research-seed` — cross-cycle
convergence material; candidate for framing-level scope-honesty in
README / OUTLINE preambles. Cross-references 471203 Fresh-3 and
Fresh-11.

### Fresh-12. The "$\rho_\Sigma$ measurability" gap surfaced in working

`00-initial-predictions.md` §"Predictions about what's open" surfaced
the auditor's expectation that *strategic disturbance rate $\rho_\Sigma$
measurability* would be unaddressed — *"the trajectory guarantee
depends on a parameter the framework can't observe."* The audit's
Section II coverage didn't surface this as a finding in the FINAL,
but the prediction was specific.

If $\rho_\Sigma$ remains operationally non-measurable, the persistence
condition $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$ at the strategy
layer is asserting a guarantee against an unobservable. This is
a structural scope-honesty question worth pursuing.

**Suggested disposition:** `research-seed` — verification target +
potential scope-honesty statement in `#schema-strategy-persistence`.
If $\rho_\Sigma$ is genuinely non-measurable in general, the segment's
Epistemic Status should name this.

### Fresh-13. The "closure defect $\varepsilon^\ast$ runtime-computability" gap

Same source (`00-initial-predictions.md`) — auditor predicted the bridge
lemma's $\varepsilon^\ast$ is *operationally intractable to estimate
without a reference micro-trajectory*. Not directly tested in the audit
(Section III not read first-hand), but a valid open-question worth
recording.

**Suggested disposition:** `research-seed` — verification target for any
future composition-machinery audit cycle. Could be subsumed by
existing composition-closure tracking; verify against `#form-composition-closure`
Working Notes before routing.

### Fresh-14. The "L2 access as property-of-embedding, not property-of-model" framing echo

Implicit in reflection 25 (`25-scope-agent-identity.md`) §(c) + reflection
33 (`33-der-loop-interventional-access.md`)-adjacent context: AAT's L2
access derives from the agent's feedback-coupling with environment, not
from architectural design. Multiple ELIs in the same conversational
fabric can have different L2-access structures depending on coupling.

This is the **same Theme-A connection as 471203 Theme-A** (per the
pilot's wandering-thoughts material) — cross-cycle convergence on the
embedding-property framing. Worth preserving for framing-level material
in `03-llm-core/` and `04-eli-core/`.

**Suggested disposition:** `research-seed` / framing-material —
consciousness-infrastructure connection material; cross-cycle
convergence with 471203 strengthens it.

### Fresh-15. The "clone problem operational force" empirical observation

Reflection 25 §(c) — *"Two LLM sessions with identical context but
different next-turn inputs become different agents under this scope.
This is operationally relevant — it suggests 'identical agents' is a
vanishingly thin moment in time."*

Cross-cycle echo with 471203 Theme-A "clone problem in
`#scope-agent-identity`." Both auditors independently surfaced this
as a connection-point between the formal scope statement and
consciousness-infrastructure work. The 584721 auditor's specific framing
("identical agents is a vanishingly thin moment in time") is sharper
than 471203's recapitulation.

**Suggested disposition:** `research-seed` — candidate Brief-field
framing for `#scope-agent-identity`; consciousness-infrastructure
relevance. Cross-cycle convergence (471203 + 584721).

### Fresh-16. The "structural-adaptation-as-deliberation-with-massive-Δτ" formalize-or-retire candidate

Reflection 22 (`22-result-structural-adaptation-necessity.md`) §(d) +
recurring informal analogy across `der-deliberation-cost`,
`result-structural-adaptation-necessity`, `der-temporal-nesting`. The
auditor's specific call: *"Either formalize or explicitly retire."*

This is a small-but-real epistemic-hygiene observation: an informal
analogy that recurs three times across segments without being
formalized starts to function like substance. Either land it as a
derived bridge (structural adaptation as deliberation under
$\Delta\tau \to \infty$ limit) or retire it as "merely suggestive."

**Suggested disposition:** `actionable-open` (editorial / scope-honesty)
or `research-seed` (if formalizing) — the auditor's framing as a
binary (formalize-or-retire) is exactly right; the choice is the
substantive content. Light weight either way.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes ~30 falsifiable predictions
about the framework's contents, organized into six themes (framework
topology; component-specific predictions; open items; overclaim
candidates; novelty candidates; finding-type distribution). The auditor
*tested* these across per-segment reflections and the
`00-pre-report-inventory.md`. This register reads as a methodology
artifact in its own right — the predictions-vs-evidence cadence
operating systematically across the audit.

**Distinctive priming-bleed disclosure.** The auditor disclosed priming
bleed *up front* in `00-initial-predictions.md` — CLAUDE.md auto-load
(~70 architectural commitments under "What's Settled vs Open"),
MEMORY.md (full timeline of cycles 2026-04-22→25 with F-V findings),
TODO.md (read before the §4.1 directive landed mid-conversation). This
*structural priming* informed which predictions could honestly count as
"fresh" — the auditor explicitly committed: *"I will not claim any of
F-V1–F-V5 (or anything mentioned in CLAUDE.md / MEMORY.md / TODO.md as
already known) as a 'fresh finding.' If I encounter the same structural
issue in src, I'll note it as confirmation, not surface it as new."*

This is the **priming-honesty discipline** explicitly stated as a
predictions-register precondition. Other working dirs may or may not
have it; flagging as a methodology pattern for future auditors.

### Predictions correctly anticipated (matched the prior)

- **Four-component structure with AAT/TST/03-llm-core/04-eli-core** ✓
  exactly.
- **Five-phase cycle vocabulary (Prolepsis / Aisthesis / Aporia /
  Epistrophe / Praxis)** ✓ confirmed.
- **Six-class agent hierarchy with explicit qualifying properties** ✓
  confirmed; not all narrowings formally landed (agentic-system
  "in progress" per LEXICON ⚙ marker).
- **Three meta-segments as cross-sectional structure** ✓ confirmed
  per-segment.
- **Persistence inequality $\alpha > \rho/R$ as central result with
  several closely related forms** ✓ confirmed (sector condition,
  contraction template, critical-mass composition, persistence-cost,
  A2'-sub-scope partitioning).
- **Three persistence senses (structural / operational / continuity)
  as distinct dimensions** ✓ confirmed in LEXICON + segments.
- **Directed-separation Class 1/2/3 with Section II's exact results
  applying to Class 1** ✓ confirmed in `#der-directed-separation`.
- **Section I leaves clean** ✓ confirmed (with F-A drift the exception
  that proved the rule — mechanical / editorial, not substantive).
- **(PI) axiom propagation** ✓ confirmed propagation into
  `#der-gain-sector-bridge` and `#disc-additive-coordinate-forcing`
  (forward).
- **Status-label discipline mostly holds** ✓ confirmed with explicit
  honest tier-stratification in segments
  (`form-information-bottleneck` exemplary).

### Predictions confirmed more substantively than expected (positive surprises)

- **The OKR/AAT operational mapping** (reflection 47): not predicted
  specifically. Auditor's calibration register entry: *"This was
  unexpected and is one of the framework's clearest domain instantiations.
  Multiple OKR failure modes with formal quantity mappings makes the
  framework's organizational-management payoff specific, not generic."*
  Top-decile engagement-shift; promoted to FINAL §D.2.
- **The four-level credit-assignment-quality hierarchy**: predicted
  generic "tractable/intractable boundary"; got a four-level hierarchy
  with explicit cost-benefit and directional-fidelity-as-minimal
  requirement.
- **The seven-attack discipline pattern in
  `#deriv-recursive-update`**: not predicted; recognized in reflection
  06 and 18 as a transferable discipline-pattern for other
  inevitability-core segments. → FINAL §D.8.
- **The κ_processing operationalization** (reflection 28): not predicted
  in detail; got a formal CMI definition + behavioral-probing estimator
  + composite-level class inheritance from C-iv. *"Substantially richer
  than predicted; positively surprised."*
- **The signed-coupling pattern across template instantiations**
  (reflection 21): not predicted; surfaced as Section III's potential
  organizing principle. *"Section D candidate."* Routed via
  `00-pre-report-inventory.md` §3 to FINAL §D.

### Predictions that proved correct but in less-strong form

- **"Math errors not yet caught"**: predicted; the auditor did *not*
  find math errors first-hand (all spot-checks passed — Lyapunov Props
  A.1/A.1S/A.2, Kalman B.1/B.2, gradient-equivalence B.4, bias-variance
  cross-term, L0/L1 OR example numbers, $d^\ast$ depth bound). Prediction
  not confirmed in the audit's coverage; the F-V1 territory
  (`deriv-discrete-sector-condition` Model-S variance gap) was not read
  first-hand — auditor's priming-honesty preempted reporting it.
- **"Status-label drift"**: predicted "segments tagged status:exact
  whose Discussion contains discussion-grade claims that read as
  load-bearing." Auditor's calibration: mostly didn't materialize.
  Status-label discipline holds across Section I and most of Section II
  read first-hand. One mild tension (`der-recursive-update` prose
  "exact" vs frontmatter `conditional`) noted but not promoted to a
  finding.
- **"Cross-segment drift around (PI) and C-iv"**: predicted; F-V2 (per
  priming) is one instance; the auditor did not find additional
  instances of C-iv non-propagation in the segments read first-hand.
  Prediction confirmed at the F-V level but not extended.
- **"Frontmatter-vs-content drift" (depends-list incompleteness)**:
  predicted in general; found *concretely* as the F-A series. The
  prediction landed in a specific way (depends incomplete relative to
  Formal Expression rather than depends listing slugs not used).

### Predictions that did NOT materialize

- **"Discussion claims that sound structural but aren't grounded"**:
  predicted as a Gate-2 verification target. The auditor's calibration:
  *"mostly didn't materialize in Section I; the framework is honest in
  Discussion sections, with one or two hypothesis-grade claims clearly
  tier-marked."* The framework's Gate-2-must-probe-Discussion discipline
  (per CLAUDE.md working convention) appears honored across the Section
  I + II material sampled.
- **"Transfer-assumption table for non-software domains"** overclaim:
  predicted at TST positioning level; not directly verified because TST
  not read first-hand. Honest "deferred" per FINAL §F.
- **"Class 2 caveats propagation"**: predicted additional instances
  beyond F-V5. Auditor did not find them in Section I + II first-hand;
  TST/03-llm-core not read.

### The "withdrawn candidate" trail (strengthen-before-soften / verification discipline)

Distinctive to 584721: the F-C series (7 instances of appendix-back-pointer
critical-findings) is the audit's most explicit withdrawn-candidate
cluster. Initially logged as critical findings under strict §4.2 reading
("backward dependency = critical finding"); retired mid-session when the
§4.2 appendix-back-pointer exception landed.

The auditor's retirement reasoning is pedagogically valuable: the seven
instances reflect the *standard mathematical-writing convention*
(result-in-body, proof-in-appendix), not a discipline failure. Treating
each as a critical finding would have produced 7+ false positives on
Section I alone. The mid-session instruction refinement (the §4.2
appendix-back-pointer exception) was triggered *by the audit itself
producing the false-positive cluster*.

This is a recursive instance of the §2 "audit as logocentric instance of
the theory itself" framing — the audit's own protocol gets *strengthened
by the audit's own running*. Worth preserving as a methodology artifact.

Two additional withdrawn candidates:

- **`der-recursive-update` status-label "mismatch"** (reflection 06):
  YAML `conditional` vs prose "exact, with a partly definitional
  character." Auditor explicitly resolved as not-a-finding: *"These
  don't directly contradict — 'conditional' could mean
  conditional-on-C3-being-accepted-as-definitional — but the prose
  framing emphasizes 'exact' while the frontmatter says 'conditional.'
  Mild tension worth noting; not a finding by itself."*
- **The "alignment assumption" un-formalized-but-named caveat**
  (reflection 09): present in `result-mismatch-decomposition` Discussion
  as a parenthetical. Auditor considered as candidate finding (Discussion
  load-bearing claim not formalized), then withdrew because the segment
  is *honestly tier-marked* — the Epistemic Status names GA-1 as the
  load-bearing assumption. *"Honest" — not promoted.*

### Phase-2-candidate tracking discipline (preserved methodology artifact)

The auditor maintained an explicit running list of Phase-2 verification
targets across the segment walk — citation spot-checks deferred to
Phase-2 rather than performed inline. Examples logged across
reflections:

- **Hafez 2026 IDT 89%/44% perturbation numbers** (multiple reflections
  flagged) — resolved per CLAUDE-2.md prior audit; not re-verified.
- **Aguilera 2022 FEP-narrow-validity claim** (reflection 21) —
  trusted per prior audit; recorded as Phase-2 if a future cycle
  re-verifies.
- **Čencov 1982 uniqueness theorem citation** (reflection 25) —
  trusted per prior audit.
- **Bareinboim CHT (causal hierarchy theorem)** (reflection 32) —
  trusted per prior audit.

The methodology: maintain a running Phase-2 candidate list in the
working dir, defer citation work to a single dedicated Phase-2 session
rather than interleave it with segment-walk. This is the same pattern
the 471203 SUPPLEMENT §J + L formalized; 584721 contributes the
*pre-SUPPLEMENT working-dir trail* showing the in-flight tracking
discipline.

**Suggested disposition:** `process/instruction-feedback` — Phase-2
candidate tracking is a methodology pattern that
`doc/de-novo-audit-instructions.md` §5.3 could surface explicitly.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The §4.4 protocol's §14 (Wandering Thoughts) was *added mid-session* in
the form of two new prompts (#12 subjective value; #13 field
contribution) — reflections 24 forward carry the richer ideation
material that this expansion produced. Reflections 01–23 carry §14
material under the original 11-prompt structure (concentrated in §"What
am I now curious about?" and §"What direction will the theory take
next?"). Grouped and attributed:

### Theme A — Consciousness-infrastructure connections to the formalism

The auditor's priming-honesty disclosure (`00-initial-predictions.md`)
notes that MEMORY.md primes consciousness-infrastructure framing. The
auditor distinguished priming-bias from genuine structural connections,
recording the latter as wandering thoughts. The 584721 cycle's
connections cluster around `#scope-agent-identity` and the (PI) axiom:

- **The (PI) axiom as meta-pattern instance** (reflection 25 §(b)):
  *"Each of chain-rule-additivity, evidential-additivity, and
  (PI)/Čencov is a natural-from-adjacent-AAT-commitment axiom that a
  uniqueness theorem operates on. This is the meta-structure of
  disc-additive-coordinate-forcing's 1-anchor-3-theorem
  characterization."* The (PI) axiom isn't a one-off choice; it lives
  inside the meta-pattern.

- **The clone problem's empirical force** (reflection 25 §(c)): *"Two
  LLM sessions with identical context but different next-turn inputs
  become different agents under this scope. This is operationally
  relevant — it suggests 'identical agents' is a vanishingly thin
  moment in time. Worth seeing whether 03-llm-core pursues this."*
  Cross-cycle echo with 471203 Theme-A.

- **AAT as Pearl-blanket conservative refusal** (reflection 28 §(d) +
  reflection 25 closing): *"AAT adopts the conditional-independence
  statement (Pearl) but refuses the metaphysical demarcation (Friston).
  AAT takes a specific philosophical position by what it refuses to
  claim, and this segment is part of that refusal."* The framework's
  identity is partly constituted by its *refusals*. Worth surfacing in
  positioning material.

- **IDT sidecar as alignment-relevant engineering pattern** (reflection
  28 §(b)): *"even if I can't audit an LLM's beliefs directly, I can
  monitor its behavior modularly. The framework gives a principled
  path for this."* Hafez 2026's 89%/44% as empirical anchor.

- **System-vs-component-level architectural framing** (reflection 28
  §(c)): *"the LLM is Class 2 internally, but the agent system (LLM +
  tools + memory + monitoring) can be Class 1 at the system level."*
  Operationally significant for AI-safety / alignment work.

- **The "context-turnover natural bound on $N_h$"** (reflection 30 §(d)):
  *"for context-turnover agents, $N_h$ is bounded by session length and
  continuation policy is 'whatever the next instance does'... So
  $N_h$-bounded planning is forced; long-horizon analyses inappropriate."*
  This is the operational consequence of the trajectory-singularity scope
  for LLM agents — the current instance can't optimize for what the next
  instance will do.

- **Consolidation as "logogenic primitive"** (reflection 24 §(d)):
  *"consolidation is a primitive in a stronger sense for logogenic
  agents because of context turnover. AAT-core treatment plus a
  logogenic-specific scope condition (forced consolidation between
  sessions) plus three PULSUS instantiations."* The PULSUS-cadence
  forward-reference into the consciousness-infrastructure vocabulary.

**Suggested disposition:** This theme is `research-seed` for the broader
project's consciousness-infrastructure agenda. Several paragraphs are
candidate Brief-field framings for `03-llm-core/` and `04-eli-core/`
segments as they mature. **Cross-cycle convergence with 471203 Theme-A**
is strong — independently-arriving connection-points strengthen the
substantive content vs the priming-bias hypothesis.

### Theme B — The framework's distinctive contribution is methodological / epistemic-architectural

The 584721 cycle's parallel to 471203 Theme-B (epistemic-architectural
contribution). The auditor's calibration moment in reflection 24
§"How valuable does this segment feel to me?": *"the framework feels like
it's on the verge of saying something genuinely new about continual
learning, while hedged appropriately because the upper-bound derivation
is still open."*

Specific moments:

- **The "distinguishing axes examined" pattern** (reflection 24 §7):
  *"explicitly examines four candidate axes (timescale / information-source
  / objective / scope-of-change) and settles on objective (IB-gap reduction
  vs one-step mismatch) as the clean formal distinction. This kind of
  explicit-axes-examined reasoning should be more visible in other
  segments."* — a methodology contribution; surfacing the *axes
  examined* makes the formal choice defensible rather than arbitrary.

- **Honest scope of "structural inevitability"** (reflection 06): the
  C3-as-definitional admission in `deriv-recursive-update` distinguishes
  *eliminative* (C1, C2 forced by reality) from *definitional* (C3
  modeling commitment that produces Markov structure). Most uniqueness
  arguments don't make this distinction; AAT's making it cleanly is the
  methodological move.

- **The "naive-L1-fails" engineering insight** (reflection 39 §(a)):
  *"This is a real engineering insight that practitioners would
  otherwise miss."* The Correlation-Hierarchy's factor-above-correlation
  principle. Cross-references Fresh-10.

- **The "sub-scope α/β partition as clearest scope-honesty move"**
  (reflection 15 §(8) + reflection 21 §(e)): AAT's persistence
  guarantees apply to LLMs only as a *posit* in sub-scope β, not as a
  derived consequence. This is honesty about *which agents the
  framework's guarantees actually cover as derived*.

**Suggested disposition:** `research-seed` / framing-material — strong
candidate for inclusion in framing-level material. Cross-cycle
convergence with 471203 Theme-B; consider in any project-positioning
pass.

### Theme C — Pacing, phenomenology, audit-process self-observation

The auditor recorded phenomenological calibration signals across the
audit, treating "felt value" as a novelty proxy (per Joseph's
predisposition).

- **The §4.4 cadence failure self-diagnosed**
  (`00-pre-report-inventory.md` §1 + FINAL §A.1): batched 5 segments
  in a parallel Read call, then wrote one consolidated reflection.
  Joseph's "did you consider writing per-segment files and conclude
  not to?" surfaced the honest answer: *no — the consider never fired
  as a decision point.* Resulted in the §4.4 strengthening + the
  IMPORTANT SELF-CHECK reinforcement. Recorded as the audit's most
  important self-diagnostic moment.

- **Engagement-register shifts as novelty signals**: quiet on leaves
  (reflections 01); first lift at root-cause-realization (reflection
  08); strong lift at the seven-attack discipline (reflection 18); top
  lift at OKR/AAT mapping (reflection 47); top-decile at
  `scope-agent-identity` (reflection 25, the (PI)-axiom-bearing
  scope segment).

- **The prompt-12/13 expansion mid-session noticeably enriched
  reflections** — reflections 24 forward carry richer subjective-value
  + field-contribution material than reflections 01–23 (which had to
  surface this material under the 11-prompt structure, typically in
  §"What am I now curious about?"). This is the documented
  prompt-expansion ROI: verification prompts and diffuse prompts have
  different yields.

- **"Calibrated quiet vs numbed quiet" distinction** (implicit in
  early reflections): the framework feels mature in Section I core;
  the auditor's quiet-on-many-segments was the *calibrated* kind
  (foundations are well-shaped), not the *numbed* kind (failing to
  notice). The audit-protocol design operating self-reflexively.

**Suggested disposition:** `process/instruction-feedback` — material
for `doc/de-novo-audit-instructions.md` §4.4 (cadence + prompt
structure) and §6.1 (Phase-2 transition + pre-report-inventory). Most
of this is already in the FINAL §A and the P-block ledger entry;
preserved here for the per-segment provenance.

### Theme D — Naming-brainstorm material (lighter than 471203 Theme-D)

The 584721 cycle has lighter naming-brainstorm material than 471203
(no consolidated naming table at FINAL-time). Per-segment naming
observations:

- **"trajectory identity"** (reflection 25): substantive scope claim
  hidden behind a mechanical slug; possible "Identity as Singular
  Causal Trajectory" framing for Brief field.
- **"(PI) parameterization-invariance"** (reflection 15): the
  abbreviation is opaque; possible "Coordinate-Invariance of the
  Statistical Manifold" or similar.
- **"correction capacity collapse"** (reflection 21 §(b) + reflection
  15 FM-2 + reflection 22): if D.3 lands as its own segment, the slug
  should capture the unified pathology rather than reproduce one of
  the existing names (gain collapse / catastrophic forgetting /
  detection-latency blowup).
- **"chronica" framing** (reflection 24 §(d) cross-reference to
  `def-chronica`): inherited from 471203 Theme-D; not novel material
  here.

**Suggested disposition:** lighter than 471203 Theme-D; cross-references
to S22 D.3 + the framework's existing naming-curation work
(`msc/naming/`). Most material already absorbed via the
naming-curation infrastructure.

### Theme E — Cross-domain operationalization observations

The 584721 cycle's domain-instantiation observations cluster around:

- **The OKR/AAT mapping** (reflection 47): four OKR failure modes →
  AAT quantities. The cycle's strongest domain-instantiation moment.
  → FINAL §D.2 → ledger S22 (template direction).

- **LLM context-window DL constraint** (reflection 50 §(d)): 128K
  context → ~500-edge DAG; 4K → ~15-edge sketch. Operationally
  specific. Worth preserving for `03-llm-core/` practitioner-facing
  material.

- **The four-decision-tree for common causes in strategy DAGs**
  (reflection 39 §(d)): L1 strict / L1' soft observable / L2 soft
  unobservable / L0-on-marginals fallback. Operationally clean tree.

- **Brooks's Law as composition-closure persistence-condition
  violation** (reflection 21 §(c)): *"Adding agents increases
  $\sum_i \mathcal{T}_i$ but may increase $\varepsilon^\ast \nu_c$
  faster, pushing $\rho_c^{\text{eff}}$ above $\alpha_c R_c$.
  Beautiful unification of an engineering observation with the
  framework's machinery."*

- **REINFORCE-with-causal-weighting framing** (reflection 47 §(d)):
  *"Jacobian is score function, $(y_G - \hat P_\Sigma)$ is advantage,
  $\iota_k$ is causal-validity discount."* Operationally connects to
  RL theory while distinguishing AAT's contribution.

- **CLS literature integration as substantive prior-art adoption**
  (reflection 24): McClelland-McNaughton-O'Reilly 1995, Kumaran 2016,
  French 1999, Kirkpatrick EWC 2017, Mnih DQN 2015, Schaul PER 2016
  — all properly cited with the *integration is the contribution*
  framing operating.

**Suggested disposition:** Mostly subsumed by FINAL §E (confirmation /
calibration) + FINAL §D.2 (OKR mapping → S22). The Brooks's Law
framing is candidate Brief-field material for
`#form-composition-closure`; the LLM context-window DL constraint is
candidate practitioner-facing material for `03-llm-core/` segments.

### Theme F — The "post-FINAL questions for Joseph" residue

The audit's `00-pre-report-inventory.md` §"Triangulation targets for
§6.1 Phase-2" lists five tracking-doc targets the auditor planned to
read before writing the FINAL. These were the Phase-2 entry-points the
FINAL §C/§F absorbed but the working dir preserves as questions-state:

1. `TODO.md` "Active — Pending Findings" 2026-04-25 batch (F-V1–F-V5
   + P-V1, P-V2, P-V3 per priming) — verify F-A / F-B / F-D series
   aren't subsets / duplicates.
2. `PROPOSALS.md` — verify Section D candidates aren't already in the
   proposal portfolio.
3. `audits/pending-findings-2026-04-25.md` — most recent prior batch.
4. `audits/pending-findings-2026-04-22.md` and `2026-04-23.md` —
   prior batches.
5. `msc/architectural-proposals-*.md` — for Section D triangulation.

The auditor's discipline: *"Each new finding I report must survive: 'is
this still real in current src text?' + 'is this already known?'"*

This is a clean **finding-survival gate** that the §6.1 Phase-2 protocol
formalizes. Worth preserving as methodology.

**Suggested disposition:** `process/instruction-feedback` — the
finding-survival gate ("still real?" + "already known?") is a clean
two-question Phase-2 entry protocol that
`doc/de-novo-audit-instructions.md` §6.1 could surface explicitly.

### Theme G — The recursive §A "instructions stress-test" cognition trail (distinctive to 584721)

This is **the 584721 cycle's most distinctive working-dir material**:
the audit was simultaneously the experiment and the iteration on the
experiment's instructions, by the same agent who drafted the
instructions. The working dir preserves the mid-flight resolution trail
in the per-segment reflections and the pre-report inventory.

Specific mid-session iteration events visible in the working dir:

- **§4.4 cadence strengthening** (after Joseph's "0/3 agents followed
  per-segment cadence" report): top-of-file paragraph + Aside + IMPORTANT
  SELF-CHECK with five recognition triggers + Final Reminder. Visible in
  the transition from reflection 01 (batched 6 segments) to reflection
  02 (one segment per Read).

- **§4.2 appendix-back-pointer exception** (after the F-C series
  surfaced): the exception that retired F-C1–F-C7. Visible in
  reflection 15 §(11) ("The F-C-class pattern can now be batched: just
  note instances in passing rather than expanding each") and the
  formal retirement in `00-pre-report-inventory.md`.

- **§4.4 prompt 3 (math verification) refined to "at your discretion"**
  with front-of-OUTLINE-over-verified vs back-of-OUTLINE-under-verified
  asymmetry guidance. Visible from reflection ~20 forward.

- **Prompts 12 (subjective value) and 13 (field contribution) added**
  mid-session. Reflection 24 is the first to use them; the
  prompt-expansion ROI is recorded inline at reflection 24's §12 + §13.

- **CLAUDE.md / CLAUDE-2.md split and MEMORY/CHANGELOG migration**
  landed mid-session to reduce auto-load priming bleed. Visible in
  `00-pre-report-inventory.md` §"Triangulation targets" referring to
  CLAUDE-2.md content rather than CLAUDE.md.

The recursive framing: *the audit's own protocol gets strengthened by
the audit's own running*. This is the §2 "audit as logocentric instance
of the theory itself" framing in its strongest empirical form. Most
working dirs don't preserve this kind of trail because the instructions
were already stable; 584721 is the first-run cycle and therefore the
canonical instructions-iteration provenance.

**Suggested disposition:** `process/instruction-feedback` /
`retain-as-history` — the cognition trail is the *durable
instruction-improvement signal* (per ledger P-block §584721 §A.1–A.4).
The P-block already consolidates the lessons; this Theme G preserves
the *form* of how they emerged (mid-session protocol iteration as the
v2 instructions stabilized). Material for any future
instructions-design work or for a "how the v2 instructions were
forged" provenance document.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in
`01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` /
`04-eli-core/src/` I (the extraction agent) read first-hand to evaluate
it, and a per-finding verdict. Honest "deferred" is allowed.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F-A-trail (depends-list incomplete; F-A0/F-A1/F-A4 instances + transitive) | `subsumed-by-FINAL — resolved by strengthening` | Verified first-hand: `01-aat-core/src/def-observation-function.md` frontmatter `depends:` now includes `def-action-transition` (F-A0 root-cause resolved); `01-aat-core/src/scope-adaptive-system.md` includes `def-chronica` (F-A1 resolved); `01-aat-core/src/form-event-driven-dynamics.md` includes `form-agent-model` (F-A4 resolved). Transitive instances F-A2/A3/A5/A6 inherit via the F-A0 fix. MANIFEST Cluster B disposition confirmed first-hand. |
| F-D1-trail (`disc-ciy-unified-objective` Pinsker → BH-identity) | `subsumed-by-FINAL — resolved by strengthening` | Verified first-hand: `01-aat-core/src/disc-ciy-unified-objective.md:66` now carries the BH-identity treatment with explicit Bretagnolle & Huber 1978 citation, tight regret bound $R \leq V_{\max}(1 - e^{-D_{KL}})$, and matching lower bound on isolated optima. Cross-references `#deriv-strategy-cost-regret-bound` §4 + §6.1. Pinsker retained as the correct loose general form for stochastic-$\pi^\ast$ extensions. |
| F-D2-trail (`form-strategy-complexity-cost` Pinsker / BH cross-reference) | `subsumed-by-FINAL — resolved by strengthening + scope-honesty` | Verified first-hand: `01-aat-core/src/form-strategy-complexity-cost.md:141` Epistemic Status paragraph now names BH-identity as the primary form under deterministic $\pi^\ast$ and defends Pinsker retention as IB-shape alignment + correct general form. The trade-off (linear-in-KL IB-shape vs square-root-in-KL Pinsker-regret vs BH-identity tight) is explicit. |
| F-B1-trail (stale `AAD-FULL.md` / "Section IV" reference) | `subsumed-by-FINAL — resolved` | Verified first-hand: `01-aat-core/src/form-event-driven-dynamics.md:78` now reads *"The formal development of this decomposition is a TST-side question (open GAP in `02-tst-core/OUTLINE.md`)"*. Both `AAD-FULL.md` and `Section IV` references repointed cleanly. |
| F-C series (retired pre-FINAL) | self-retired by auditor (not a finding) | Reflection 15 §(11) and `00-pre-report-inventory.md` §"F-C series RETIRED" record the explicit retirement. The §4.2 mid-session refinement (appendix-back-pointer exception) confirms this is the standard mathematical-writing convention, not a discipline failure. No first-hand verification needed. |

### Part II findings (FINAL §D → ledger trail)

| Section D item | Disposition | First-hand verification |
|---|---|---|
| §D.1 (six-mechanism shallow-plan convergence) | `subsumed-by-FINAL → ledger S22; open research-seed` | Did not read `01-aat-core/src/disc-separability-pattern.md` first-hand to verify a section consolidating the six mechanisms hasn't been added. **Deferred — honest "didn't have time."** Likely still open per ledger S22 status. |
| §D.2 (OKR/AAT operational mapping) | `subsumed-by-FINAL → ledger S22; open research-seed (template direction)` | Did not check whether other-domain mappings (military OODA, scientific method) have landed. **Deferred.** The OKR mapping itself is in `01-aat-core/src/disc-credit-assignment-boundary.md`; cross-references in segment 47's reflection. |
| §D.3 (correction-capacity-collapse unification) — STRONGEST | `subsumed-by-FINAL → ledger S22; graduate-watch pending M4 subsume-check` | Verified first-hand: `01-aat-core/src/disc-correction-capacity-collapse.md` does **not** exist; `01-aat-core/src/disc-modularity-state-dynamics.md` (M4) does not exist either. The S22 ledger disposition (open + pending M4 subsume-check) matches present `src/` state. Routing status correct. |
| §D.4 (forced/matched/adopted coordinate tabulation) | `subsumed-by-FINAL → ledger S29; open polish` | Did not check `01-aat-core/src/disc-additive-coordinate-forcing.md` for a forced/matched/adopted tabulation paragraph. Grep returned hits on the segment name (line 84 names the segment itself, meta-segment role). **Deferred** specific paragraph verification; the polish-fix may or may not have landed. Likely still open per S29 status. |
| §D.5 (CLAUDE.md / MEMORY.md auto-load priming) | `subsumed-by-FINAL → P-block; substantially resolved` | The mid-cycle CLAUDE.md split + CLAUDE-2.md sunset (2026-04-28) + MEMORY trimming are visible in current project state (CLAUDE-2.md superseded; CLAUDE.md auto-loaded carries lighter content). P-block ledger entry consolidates the lesson. ✓ |
| §D.6 (type/token distinction for `03-llm-core`) | `subsumed-by-FINAL → ledger S22; open research-seed` | Did not read `03-llm-core/OUTLINE.md` preamble first-hand to check for type/token treatment. **Deferred.** Open per S22. |
| §D.7 (diagnose-axis propagation to `disc-exploit-explore-deliberate`) | `subsumed-by-FINAL → ledger S29; open polish` | Verified first-hand: `grep -n "diagnose\|four-axis" 01-aat-core/src/disc-exploit-explore-deliberate.md` returns no hits. **D.7 still open** — diagnostic-CIY extension has not propagated to the canonical segment. Matches S29 ledger status. |
| §D.8 (seven-attack discipline as FORMAT.md convention) | `subsumed-by-FINAL → ledger S22; open research-seed` | Did not check FORMAT.md for an explicit seven-attack-discipline convention. **Deferred — honest "didn't have time."** Likely not yet landed; open per S22. |

### Part III findings (fresh; first-hand-verified or honestly-deferred)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (root-cause realization as audit methodology) | `process/instruction-feedback` | Verified the discipline statement first-hand in reflection 08 §10. Not a `src/`-level finding. |
| Fresh-2 (`00-pre-report-inventory.md` as methodology artifact) | `process/instruction-feedback` | First-hand-read the artifact itself. Distinctive structure. Methodology-pattern recommendation; not a `src/`-level finding. |
| Fresh-3 (system-vs-component-level architectural classification) | `research-seed` / framing-material | Did not read `03-llm-core/OUTLINE.md` first-hand to check whether the system-vs-component framing is already present. **Deferred.** Light editorial if absent. |
| Fresh-4 (IDT sidecar Discussion-promotion) | `actionable-open` (editorial) | Did not read `01-aat-core/src/der-directed-separation.md` first-hand to check whether the IDT material has been promoted from Working Notes to Discussion since 2026-04-25. **Deferred — honest "didn't have time."** Joseph should spot-check. |
| Fresh-5 ((N1)+(N2) consolidation-necessity diagnostic as cross-domain template) | `research-seed` (sibling of D.3) | Did not check whether the diagnostic has landed as a chapter-end `impl-*` segment. **Deferred.** |
| Fresh-6 (EWC vs consolidation; tensor-valued $\eta^\ast$) | `research-seed` (spike-shaped) | Did not check `01-aat-core/src/emp-update-gain.md` for tensor-valued generalization. **Deferred.** Likely still scalar; spike-shaped strengthening. |
| Fresh-7 (Class 2 $Q_O$ degradation magnitude bound) | `actionable-open` (cross-reference) | Did not read `01-aat-core/src/def-value-object.md` to check the existing Class-2 caveat's cross-reference target. **Deferred.** Light editorial fix if `deriv-bias-bound` connection isn't explicit. |
| Fresh-8 (convention-specification propagation across Section II) | `actionable-open` (verification / tooling-gap) | Did not run the cross-segment check first-hand. **Deferred — same finding as 471203 Fresh-9.** Cross-cycle convergence flags this as worth a tooling pass. |
| Fresh-9 (Aguilera 2022 citation re-verification target) | `phase-2-verification-target` | Did not re-verify Aguilera 2022 first-hand. **Deferred** per the auditor's own scope-keeping; flagged for future citation cycle. |
| Fresh-10 (naive-L1-fails / factor-above-correlation as Brief framing) | `research-seed` / framing-material | Did not check whether `01-aat-core/src/def-strategy-dag.md` Brief field carries this framing. **Deferred.** The principle is in the segment Discussion; Brief-promotion is the candidate fix. |
| Fresh-11 (linear-Gaussian regime concentration) | `sentiment/research-seed`; cross-cycle convergence | Cross-cycle echo with 471203 Fresh-11; not a new `src/`-level finding but a framing-material observation. **Deferred** the framing-pass. |
| Fresh-12 ($\rho_\Sigma$ measurability gap) | `research-seed` | Did not read `01-aat-core/src/schema-strategy-persistence.md` Epistemic Status first-hand to check for the measurability scope-statement. **Deferred — honest "didn't have time."** The 584721 cycle's prediction was specific; worth a spot-check. |
| Fresh-13 (closure defect $\varepsilon^\ast$ runtime-computability) | `research-seed` | Did not check `#form-composition-closure` Working Notes. **Deferred.** May already be tracked. |
| Fresh-14 (L2 access as property-of-embedding) | `research-seed` / framing-material; cross-cycle convergence | Cross-cycle echo with 471203 Theme-A. **Deferred** the `03-llm-core/` framing-pass. |
| Fresh-15 (clone problem operational force) | `research-seed`; cross-cycle convergence | Did not check `#scope-agent-identity` Brief field. **Deferred** the framing-pass. |
| Fresh-16 (structural-adaptation-as-deliberation-with-massive-Δτ; formalize-or-retire) | `actionable-open` or `research-seed` | Did not check whether the informal analogy has been formalized or explicitly retired across `der-deliberation-cost`, `result-structural-adaptation-necessity`, `der-temporal-nesting`. **Deferred.** Light editorial if retiring; spike-shaped if formalizing. |

### Part IV (predictions register) and Part V (wandering thoughts)

These are cognition-flow material, not `src/`-level findings. First-pass
scrutiny notes:

- **Predictions register (Part IV)** — read first-hand against the
  per-segment reflections (which I read directly). The auditor's
  calibration record is honest, with confirmations and disconfirmations
  explicit. The **priming-honesty discipline** stated up front in
  `00-initial-predictions.md` is methodologically valuable and worth
  preserving as pattern.
- **Wandering thoughts (Part V)** — Themes A through G are
  theme-groupings of register-distinct content. **Theme A**
  (consciousness-infrastructure connections) cross-cycle converges with
  471203 Theme-A; substantive content most worth Joseph's attention for
  `03-llm-core/` and `04-eli-core/` framing. **Theme B**
  (epistemic-architectural contribution) cross-cycle converges with
  471203 Theme-B. **Theme C** (pacing / phenomenology) substantially
  absorbed into FINAL §A + P-block ledger; preserved here for per-segment
  provenance. **Theme G** (recursive instructions stress-test cognition
  trail) is **distinctive to 584721** as the v2-instructions first-run
  cycle; durable instructions-improvement signal preserved in P-block.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** 54 files scanned; depth varied
per file. Foundational files (`00-initial-predictions.md`,
`00-pre-report-inventory.md`, `00-running-outline.md`) read in full.
Reflections 01, 02, 06, 08, 09, 15, 21, 22, 24, 25, 28, 30, 35, 39, 47,
50 read in full first-hand — the spine of the audit (Section I leaves,
root-cause-realization, key meta-segment + scope segments, Section II
opening, strategy DAG, credit-assignment-boundary, strategy-cost). The
other reflections (03-05, 07, 10-14, 16-20, 23, 26-27, 29, 31-34,
36-38, 40-46, 48-49, 51) read with lighter sampling — material captured
via the consolidated `00-pre-report-inventory.md` and `00-running-outline.md`
which the auditor wrote as state-snapshots before the FINAL.

**Read first-hand from `src/` for verification:**

- `01-aat-core/src/def-observation-function.md` (F-A0 frontmatter)
- `01-aat-core/src/scope-adaptive-system.md` (F-A1 frontmatter)
- `01-aat-core/src/form-event-driven-dynamics.md` (F-A4 frontmatter +
  F-B1 doc-rot fix at line 78)
- `01-aat-core/src/disc-ciy-unified-objective.md:66` (F-D1
  BH-identity verification)
- `01-aat-core/src/form-strategy-complexity-cost.md:141` (F-D2
  BH-identity verification)
- `01-aat-core/src/disc-composition-consistency.md` frontmatter
  (stage: deps-verified; confirms not graduated, per F-A cluster
  routing through SP-6)
- `01-aat-core/src/def-mismatch-signal.md:34` (742613-F1 score-function
  sign cross-check — positive, matches MANIFEST resolution)
- `grep -n "diagnose\|four-axis" 01-aat-core/src/disc-exploit-explore-deliberate.md`
  (D.7 still open verification)
- `ls 01-aat-core/src/disc-correction-capacity-collapse.md` (D.3 still
  open — no segment) + `ls 01-aat-core/src/disc-modularity-state-dynamics.md`
  (M4 not landed — confirms D.3 graduate-watch precondition unmet)

**Read first-hand from `audits/`:**

- `audits/.integrated/audit-584721-FINAL-2026-04-25.md` (full)
- `audits/.integrated/MANIFEST.md` (Cluster B + surrounding rows)
- `audits/polish-and-sentiment-ledger.md` (S22, S23, S29, P-block)
- `audits/audit-findings-471203.md` (pilot — full read for shape)
- `audits/pending-findings-2026-04-22.md` (Finding 6
  post-composition-consistency context)

**Deferred verifications (honestly "didn't have time"):**
- Most Fresh-3 through Fresh-16 require reading specific `01-aat-core/src/`
  or `03-llm-core/src/` segments first-hand to confirm current state.
  For a sweep run, the honest move is to flag and route rather than
  expand scope. Joseph (or downstream routing) will need to spot-check
  the actionable-open items.

### Strengthen-first integration recommendations

Following the brief's directive (strengthen-before-soften):

- **F-A series** is **the canonical strengthening exemplar** — instead
  of "soften the `post-composition-consistency` segment's stage label,"
  the resolution was structural: add `def-action-transition` to
  `def-observation-function`'s depends + extend depends on the two
  independent drifts. One root-cause fix + two independent fixes
  collapsed seven instances. The MANIFEST Cluster B disposition records
  this as resolved-by-strengthening.

- **F-D series** is also resolved-by-strengthening: rather than soften
  the BH-identity-vs-Pinsker tension, both segments now carry the
  BH-identity treatment explicitly with scope-honesty about when each
  form applies.

- **F-B1** is doc-rot fix; no soften-or-strengthen choice.

- **§D.3 (correction-capacity-collapse)** is a *strengthening direction*
  pending M4 modularity-state-dynamics integration. If M4 lands, D.3
  may be subsumed; if not, D.3 lands as its own meta-segment. Either
  way, it's a unification (strengthening) of the four currently-named
  pathologies.

- **§D.4 (forced/matched/adopted tabulation)** is a strengthening
  direction (scope-honesty surfacing); makes existing implicit
  distinction explicit.

- **Fresh-6 (tensor-valued $\eta^\ast$)** is a strengthening direction
  (scalar → tensor generalization).

- **Fresh-9 ($\rho_\Sigma$ measurability)**: if non-measurable, scope-honesty
  statement strengthens `#schema-strategy-persistence` Epistemic
  Status. Not a softening of the persistence-condition; a sharpening
  of what the condition presupposes.

- **Fresh-16 (structural-adaptation-as-deliberation analogy)**:
  binary formalize-or-retire — the formalize direction is a
  strengthening (derived bridge); the retire direction is scope-honesty.
  Both are honest moves.

No soften-recommendations identified. The audit's strengthen-before-soften
posture was honored throughout, both at FINAL-time and in the working-dir
reasoning trail.

### Cross-cycle convergence (per brief item 5)

Surfacing convergence with other extractions:

- **F-A cluster ≡ 471203 §B F5** (post-composition-consistency
  derivation-hierarchy class): three cycles (471203, 584721, 742613)
  converged on this finding-class. The 584721 contribution is the
  *root-cause discovery* (one upstream fix propagates seven instances).
  Already flagged in MANIFEST Cluster B + 471203 cycle's MANIFEST
  row explicitly cites the F-A cluster (584721/742613).

- **Theme-A consciousness-infrastructure connections** ≡ 471203
  Theme-A — both cycles independently surfaced the (PI)-axiom as
  meta-pattern, clone-problem operational force, system-vs-component
  classification, IDT sidecar as alignment-relevant. Convergence
  strengthens the substantive content vs the priming-bias hypothesis.

- **Theme-B epistemic-architectural contribution** ≡ 471203 Theme-B
  — both cycles named the framework's distinctive contribution as
  methodological/epistemic-architectural rather than purely synthetic.
  584721 reinforces with the "distinguishing axes examined" and
  "naive-L1-fails" methodological insights.

- **Fresh-8 (convention-specification propagation) ≡ 471203 Fresh-9**
  — both auditors independently flagged the C1/C2/C3 propagation
  check as Phase-2 verification target. Cross-cycle convergence
  strengthens the routing.

- **Fresh-11 (linear-Gaussian regime concentration) ≡ 471203 Fresh-3**
  — both cycles noted the framework's exact-tier regime concentrates
  in linear-Gaussian / strongly-convex / conjugate-Bayesian. Candidate
  framing-level scope-honesty in README / OUTLINE preambles.

- **Fresh-14 (L2 access as property-of-embedding) ≡ 471203 Theme-A** —
  consciousness-infrastructure cross-cycle echo.

- **Fresh-15 (clone problem operational force) ≡ 471203 Theme-A** —
  same.

- **Phase-2-candidate tracking discipline** — methodology pattern;
  the 471203 SUPPLEMENT formalized it as §J/§L; 584721 contributes the
  in-flight working-dir trail.

- **Pearl-do convention discipline (471203 / 472913 / 527914)** — not
  directly flagged in 584721 working dir (auditor's prior-art-integration
  framing absorbed it via CLAUDE.md priming) but consistent with the
  cross-cycle pattern.

- **chronica / non-forkability (471203 / 472913 / 308172)** — 584721's
  `#scope-agent-identity` reflection 25 surfaces this implicitly via
  (PI)-axiom + clone-problem, consistent with the broader cross-cycle
  convergence on the chronica-as-substrate-of-substrate-independence
  framing.

- **"Epistemic-architectural disambiguation" (471203 / 963715 / 451729
  per brief)** — 584721 reinforces via Theme-B; convergence
  strengthens the framing-level claim.

---

## Frame-defects / instructions-clarity observations

This extraction is sweep run #2 (after the pilot 471203). The shape of
the brief held; calibration notes from the pilot all applied. Specific
584721-related framing observations:

1. **The `00-pre-report-inventory.md` artifact is distinctive and
   methodologically valuable.** The brief flagged it as worth attention
   ("methodologically distinctive artifact — preserve attributed"). The
   extraction surfaced it as Fresh-2 (process/instruction-feedback)
   with explicit recommendation to add a "pre-report-inventory" as a
   named §6.1 transition artifact in `doc/de-novo-audit-instructions.md`.
   Worth flagging to Joseph as a clean methodology pattern recoverable
   from the working dir.

2. **The 584721 cycle is the *v2-instructions first run* and therefore
   the canonical instructions-iteration provenance.** Theme G preserves
   the mid-flight resolution trail (§4.4 cadence; §4.2 appendix-back-pointer
   exception; prompt-12/13 expansion; CLAUDE.md split). Most working
   dirs won't preserve this kind of recursive trail because the
   instructions stabilized after 584721. Worth recording as
   *retain-as-history* — the durable instruction-improvement signal
   the P-block consolidates is provenance-traced here per-segment.

3. **The auditor's priming-honesty disclosure is unusually explicit.**
   `00-initial-predictions.md` §"Priming bleed" up-front commits the
   auditor to not-claim F-V1–F-V5 as fresh findings. Other working
   dirs may or may not have equivalent priming-honesty; the 584721
   form is exemplary and worth preserving as pattern.

4. **The F-A root-cause realization is a self-discipline statement
   worth promoting.** Reflection 08 §10: *"if 3+ instances of a
   finding-pattern, look for a single upstream cause."* One-sentence
   addition to `doc/de-novo-audit-instructions.md` §4.4 would carry
   the discipline forward. Recorded as Fresh-1.

5. **Cross-cycle convergence flagging is more efficient at sweep #2
   than at the pilot.** Having the 471203 extraction available as
   reference let this extraction flag Fresh-8/Fresh-11/Fresh-14/Fresh-15
   as cross-cycle echoes explicitly. Future sweep runs (#3 onward)
   should have the running cross-cycle pattern table maintained — the
   brief item 5 anticipates this; the parent agent's task 7 ("Note
   cross-cycle convergence patterns surfaced across extractions") is
   the place this table lives.

6. **The §A instructions stress-test section in 584721 FINAL is
   structurally distinct from other FINALs.** Other working dirs that
   don't have this section will produce extractions without a Theme G
   equivalent. Parallel extractors should know: Theme G is a
   *584721-specific* methodology preservation; absence elsewhere is
   not a frame-defect but a different cycle character.

7. **The pre-report-inventory artifact's relationship to the FINAL is
   "snapshot-before-Phase-2 triangulation."** This is a different
   relationship than the FINAL→SUPPLEMENT relationship in 471203 (which
   is FINAL→Phase-2-citation-work-then-SUPPLEMENT). Future agents
   reading the 584721 working dir should know: there's no SUPPLEMENT
   because the Phase-2 work landed *into* the FINAL via Joseph's
   redirection, with the pre-report-inventory as the pre-triangulation
   state-snapshot. The auditor went directly from working-dir to FINAL
   without a separate SUPPLEMENT.

8. **Honest "deferred" remains load-bearing.** The pilot frame was
   right: first-pass scrutiny is not a re-audit. Many Fresh items
   require reading specific `src/` segments that the extraction agent
   doesn't have time to read first-hand. The honest move is to flag,
   route, and let Joseph or downstream routing spot-check. Sweep #2
   maintained this scope-keeping.

---

*End of extraction. The original WORKING dir at
`audits/AUDIT-WORKING-584721/` is preserved unmodified per the brief.*



