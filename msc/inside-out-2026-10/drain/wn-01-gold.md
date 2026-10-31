# Drain: the "Incidental audit gold" blocks in `01-aat-core` Working Notes

*Serves **I.9** (every backlog surface drained into the ledger, one disposition per source item), and through it I.10, I.5, C.1, C.4, G.2 and H.3. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Working file of the gold-lift drain, 2026-10-30, read at asf `86489b0b`. Written as it goes; the lead reads it whole.*

*In progress.*

## What the surface is (measured at `86489b0b`)

120 segments in `01-aat-core/src/` carry a `### Incidental audit gold` block (lifts dated 2026-05-30 and 2026-05-31, plus one 2026-08-22 extension). No segment in 02, 03 or 04 carries one; only `03-llm-core/OUTLINE.md` and `04-eli-core/OUTLINE.md` mention the phrase. The blocks total 757k characters. Split into items (top-level bullets under each sub-heading), they hold:

| kind | items | chars |
|---|---|---|
| block preamble (coverage notes, attribution) | 119 | 73k |
| 1. Candidate Brief prose | 202 | 83k |
| 2. Candidate Discussion | 263 | 174k |
| 3. Follow-up items (incl. candidate spikes, experiments, forward pointers) | 245 | 141k |
| 4. Readers often ask | 192 | 78k |
| 5. Candidate figures | 99 | 46k |
| Belongs elsewhere | 160 | 94k |
| Off-ramp (NOT gold), including six `> Off-ramp note:` blockquotes and two inline off-ramp bullets outside the `####` blocks | 57 | 40k |
| Regression guards inside gold | 7 | 2k |

The extraction script is `cats.py` in the session scratchpad. It splits on `####` and bold sub-headings and on top-level bullets, so a count can be off by a few where a block is formatted unusually.

## How each kind is disposed, and why it differs by kind

The kinds are different things to the theory, so the unit of disposition differs:

- **Off-ramp:** one disposition per finding, verified against the segment body at `86489b0b`. These are correctness findings. A Working Note's "resolved" or "routed" label is not trusted in either direction.
- **Follow-up items:** one disposition per bullet after dedupe. Where the same open question appears in several segments, it gets one item citing every source.
- **Belongs elsewhere:** grouped by *destination*, and checked for whether the content has already arrived there.
- **Readers often ask:** one item per segment listing the questions the body still leaves open. By project doctrine (the Codex open-questions rule) these are body edits, not log entries.
- **Candidate Brief, Discussion and figures:** disposed as a category to the pedagogy home (§ Pedagogy home below). I sampled them for theory claims or defects filed as pedagogy, and for pedagogy that rides on a superseded claim. These were not read whole; the read ledger says what was sampled.

Cross-surface: for each item I consulted a slug-to-mentions index over `audits/`, `spikes/`, `msc/` (including `influx-scout/`), `items/`, `questions/` and `reviews/`, and grepped key phrases where it mattered. A related source found there is cited in the same ledger item.

## Read ledger

The work was split four ways: this file (Off-ramp, Follow-ups, preambles, guards), and three forks of this agent, each writing a sibling file that is part of this drain's record: `wn-01-gold-belongs.md` (Belongs elsewhere), `wn-01-gold-readers.md` (Readers often ask, as H.4 items) and `wn-01-gold-pedagogy.md` (Candidate Brief, Discussion and figures, plus the 2026-08-22 teaching-frames block in `#impl-persistence-and-limits` that the extractor missed). Each sibling carries its own read ledger.

**Read whole, by me:**
- The 57 Off-ramp extracts, plus the two inline off-ramp bullets outside `####` blocks (`#disc-adversarial-coupling-pressure`:163, `#form-consolidation-dynamics`:186).
- All 245 Follow-up extracts.
- The 7 regression-guard extracts.
- The certified-stream sentences of the 119 preambles. The rest of each preamble (coverage and attribution) was skimmed, not read.
- `audits/AUDIT-WORKING-526815/00-running-outline.md` rows F182–F221.
- Every existing item I raised a source on: its title and restatement, not always the full body.

**Checked against the body:** each disposition marked in canon, present, superseded or gone was checked by reading or grepping the segment body (Working Notes excluded) at the line cited. Grep-negative verdicts ("phrase absent", "not found") are evidence, not proof: a reworded survival would be missed.

**Not done, or only partly done:**
- F63–F65 on `#form-structural-change-as-parametric-limit` (follow-up #169).
- F60/F61 on `#disc-credit-assignment-boundary` (recorded in a raise, not verified).
- F207, F212, F218 (in the residue item, marked not verified).
- `#scope-adaptive-system` follow-up #222: the A.1 lane is editing that segment.
- The 526815 F53 claim (left to the audits drain's item).
- I did not run `memorata-search` over transcripts for each item. The cross-surface check was the slug index over `audits/`, `spikes/`, `msc/`, `items/`, `questions/` and `reviews/`, phrase greps of the ledger, and the other drains' files where they touched the same rows. That is mostly the `audits.md` F-row table and `wn-01-other.md`.

## Dispositions

### Off-ramp (57 items, read whole, each checked against the body at `86489b0b`)

Line numbers are the segment's at `86489b0b`. "Item" means a ledger item opened or extended by this drain unless marked *existing*.

| segment (WN line) | finding | disposition |
|---|---|---|
| `def-shared-intent` (79) | F157–F161: argmin over representations, not encoder; "full model sharing"; "minimal sufficient statistic"; ordering not derived | **defect present** (lines 26, 28, 30, 34) → `item:def-shared-intent-ib-formalization-f157-f161` (C.1) |
| `def-strategy-dag` (329) | blanket "overestimates" is topology-dependent | **in canon**: the sign table (88–91), the negative-correlation reversal (93) and line 97 scope overestimation to OR-near-root structures |
| `def-unity-dimensions` (154) | F146 $U_M$ normalization; F147–F150 | F146 **in canon** (line 34, the $(n-1)$ normalizer; landed `f8d9151a`). F147–F150 (zero-variance $U_O$, unbounded KL ratio, $U_{\text{obs}}$ synergy, normalized $d$) are soft metric conventions, still unstated at 40, 50, 56, 64–66 → added to *existing* `item:todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8` (C.1), which already holds F151–F156 |
| `der-agent-opacity` (232–241) | F246–F255, F256/F258, F257 | F246–F255 **defects present** (lines 101, 110, 113–116, 130, 148, 155, 157, 165) → `item:der-agent-opacity-overclaims-f246-f255` (C.1). F256/F258 → appended to *existing* `item:hafez-citations-der-agent-opacity-109-169-say-h` (F.3). F257 is a **regression guard**: keep it at I.5 |
| `der-chain-confidence-decay` (100) | "decays monotonically" vs non-increase | **in canon** (lines 12, 24, 40). The WN bullet is stale history |
| `der-class-coercion-in-composition` (123) | F132–F134 under-gated "valid composite" | *existing* `item:todo-der-class-coercion-in-composition-a12-f1-4890` (C.1) |
| `der-class-coercion-via-wrapping` (238) | $\kappa_{W_1}$ identically zero | **in canon**: $\kappa_{W_1}^{\text{sel}}$ (line 99) and `#disc-w1-structural-bound-boundary` exists. The vacuous form is a regression guard |
| `der-interaction-channel-classification` (213) | four regimes "forced" vs precedence convention | **defect present**: the body contradicts itself (23/46/76/149 vs 134) → `item:interaction-channel-four-regimes-forced-vs-precedence` (C.1) |
| `der-orient-cascade` (206) | F83/F84 step 4a proof target vs proxy | *existing* `item:todo-der-orient-cascade-a10-f83-f84-step-4a-d-5348` (C.1) |
| `deriv-critical-mass-composition` (253) | (UO-mult) conflates teleological unity with physical coupling (rivalry) | *existing* `item:spikes-proposed-u-o-sector-constant-uo-mult-derivation-fbb6` (derive $\gamma$ from target correlation *and* rivalry) |
| `deriv-discrete-sector-condition` (230) | the two step-size forms read as a contradiction | **mostly in canon** (scalar specialization line 77; "two forms" line 191). One sentence remains, that the general bound is conservative in 1D; it is a reader-clarity gap → H.4 readers-ask item for this segment |
| `deriv-gain-sector` (324) | B.4 "iff" | **in canon** (line 271, one-point ⇐ / two-point ⇔). **Regression guard**: keep |
| `deriv-gain-sector` (325) | exponential family "globally" | **in canon** in the proposition (183, 192); **residual defect** in Experiment 5 (line 256, "Confirms global strong convexity") → `item:deriv-gain-sector-exp5-global-and-fm3-force-cap` (C.1) |
| `deriv-gain-sector` (326) | F13 per-event vs per-time $\alpha$ | **in canon**: `#der-gain-sector-bridge` lines 35–51 separate $\alpha_{\text{event}}$ from $\alpha_{\text{time}}=\nu\eta^\ast c_{\min}$ |
| `deriv-gain-sector` (327) | FM-3 saturation caps the force | **true, not in canon** → same item, part (b) |
| `deriv-graph-structure` (267) | acyclicity is for the time-unrolled graph, not a state-folded policy | **in canon** in substance (line 146: each attempt a distinct node; line 148 on $\Sigma_t$ vs $M_t$). Stating "not a policy over states" at Step 1 is reader clarity → H.4 item for this segment |
| `deriv-persistence-cost` (187–188) | dimension bookkeeping; Landauer 0.35→½ | Landauer **in canon** (line 90). The per-dimension reading is *existing* `item:t1-persistence-cost-per-dimension-reading` (C.1) |
| `deriv-recursive-update` (243) | exact vs conditional status mismatch with `#der-recursive-update` | **superseded**: `#der-recursive-update`:41 now reads "Exact, with a partly definitional character", matching this appendix |
| `deriv-sector-condition` (452) | template insufficient for composition (DA2'-inc) | **in canon**: `#result-sector-persistence-template` lines 64 and 117 say (T2) is insufficient and composition needs DA2'-inc |
| `deriv-sector-condition` (453) | PID: only the I term breaks the static sector | **unverified** → `question:pid-subscope-which-term-breaks-the-static-sector`. True for P; for PD only on the augmented state |
| `deriv-strategic-composition` (260–265) | F234–F243; 193847 C-iv Class-3 poke | F234–F240 and F243 **defects present** (lines 48–52, 64, 68, 192; `depends` lacks `der-gain-sector-bridge`) → `item:strategic-composition-alpha-prime-transfer-overclaim` (C.1). F241 → *existing* `item:todo-613842-c-iv-idiom-drift-integration-debt-e3af` (C.3). C-iv→Class 3 **superseded** (line 181) |
| `detail-linear-ode-approximation` (236) | the Model D steady state is exactly tight for constant drift | **true, not stated**: with scalar correction $\mathcal T$, constant $w$ gives $\delta\to w/\mathcal T$ exactly, and line 68 calls $\rho/\mathcal T$ the worst case → `item:mismatch-dynamics-model-d-equality-scope` (C.1), together with the converse point on `#hyp-mismatch-dynamics` |
| `disc-adversarial-coupling-pressure` (163) | inline note: other items already tracked | **set aside**: the note itself says so; the items it names are WN items in the 01-other drain's surface |
| `disc-exploit-explore-deliberate` (232) | F85 FOC drops a term | *existing* `item:todo-der-orient-cascade-a10-f83-f84-step-4a-d-5348` |
| `disc-exploit-explore-deliberate` (233) | F86 ceiling ignores policy-class expansion | **defect present** (80–83) → `item:regret-ceiling-omits-policy-class-expansion` (C.1) |
| `disc-exploit-explore-deliberate` (234) | F87 $\lambda$ overload | **present** (100, 106) → appended to *existing* `item:lambda-names-at-least-five-objects-in-canon-and` (F.4) |
| `form-consolidation-dynamics` (186) | (i) topological mis-positioning; (ii) F74–F77; (iii) window existence sketch-grade | (i) **superseded**: the segment now sits in Part II (`OUTLINE.md`:182, after `schema-strategy-persistence`); its one remaining forward dependency, on Appendix `disc-compression-operations`, is ordinary appendix referencing and `bin/lint-outline`'s to report. (ii) *existing* `item:form-consolidation-dynamics-s-body-still-asserts`. (iii) *existing* `item:todo-stability-upper-bound-for-form-consolida-be13` |
| `hyp-auftragstaktik-principle` (86) | F162–F166 | F162/F165 *existing* `item:t1-auftragstaktik-allocation-and-conway` (C.1). F163/F164 are its marginal-and-conditional restatement, the same fix. F166 → `item:def-shared-intent-ib-formalization-f157-f161` |
| `hyp-communication-gain` (105) | F167–F172 | F167 **in canon** (47, 51). F168 *existing* `item:todo-communication-gain-adversarial-scope-hyp-e79c`. F171/F172 *existing* `question:how-should-the-null-distribution-p-0-of-hyp-comm`. F169, F170 **present** → `item:communication-gain-residual-floor-and-tempo-sum` (C.1) |
| `impl-composition-machinery` (81) | F139–F143 implications stated as settled | *existing* `item:todo-impl-series-status-tagging-pass-b-4-rema-11e6` (A.3), which names this segment's F139–F145. Lines 29–39 still read as settled ("now derived in closed form"; "Brooks's Law as a derived inequality") over conditional homes |
| `impl-persistence-and-limits` (96) | weakest-link geometry | → `item:weakest-link-needs-conjunctive-failure-boundary` |
| `impl-strategic-composition` (105) | Gemini "editorial bloat" of in-segment Findings | **set aside**: by design (`## Findings` is the source of `FINDINGS.md`). The signal that two fresh readers stumble on it is pedagogy and goes to the pedagogy home |
| `impl-strategic-composition` (106) | forward refs; TF-06/TF-11 footers; C-iv OUTLINE residue | Forward ref **resolved** (OUTLINE: channel classification at 282, before opacity at 300). TF-06/TF-11 **gone from bodies**; the mentions left are in WN only (`def-mismatch-signal` WN 95, this WN). C-iv residue → *existing* `item:todo-613842-c-iv-idiom-drift-integration-debt-e3af` |
| `obs-gated-tempo-advantage` (82) | $
u$ vs $\mathcal T$ collision | **defect present** (14, 42) → `item:gated-tempo-nu-versus-tempo-collision` (C.1) |
| `result-adversarial-exponent-regimes` (103–104) | "exponent" in the intermediate regime; OUTLINE says Observation | both **present** → `item:adversarial-exponent-local-elasticity-and-outline-label` (C.1; part (b) is H.2's) |
| `result-per-dimension-persistence` (165) | weakest link presupposes an $L_\infty$ boundary | **defect present** (14, 74, 110) → `item:weakest-link-needs-conjunctive-failure-boundary` (C.1) |
| `result-sector-persistence-template` (165) | template insufficient for compositional proofs | **in canon** (lines 64, 117) |
| `result-unity-closure-mapping` (161) | F151–F156 | *existing* `item:todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8` (F154 and the off-ramp named there). F151 is also *existing* `item:todo-c-iv-composite-route-count-mismatch-gem-bb4b` |
| `scope-and-or` (90–91) | k-of-n misclassified; completeness ≠ compactness | *existing* `item:scope-and-or-audit-finding-f41-still-open-in-its` (C.1) |
| `strategy-structure-intro` (71) | intro acyclicity wording | **in canon** (line 20: "propositions about time-indexed future events (a retried step is a new node at a later time)") |

*Count:* 57 extracted items (the extractor also catches footnote lines and the block lead-in paragraphs, which are not findings). Every finding bullet in the off-ramps has a row above.

### Follow-up items (245, read whole, each checked at HEAD)

Bodies were checked at `86489b0b`; the items opened in the second half were re-checked at `4175aae7` (no Part I segment body changed between them on main, though five lanes have work in flight on branches). "Raised on" means a `vsect raise` event on an existing item. "H.4" items are the readers drain's per-segment `item:readers-ask-<slug>` (see `wn-01-gold-readers.md`). Where another drain's item already holds a claim, the source is raised onto it rather than duplicated. The 01-other drain, working the same segments' non-gold notes, opened several items for ideas the gold also raises (`and-or-parsimony-uniqueness`, `transient-adequacy-third-persistence-condition`, `boundary-integrity-second-constitutive-commitment`, `strategy-compression-price-beta-sigma`, `continuity-stance-boundary-cases`); the gold sources are raised on those.

| # | segment | follow-up | disposition |
|---|---|---|---|
| 0 | `causal-access-intro` | opening over-read of Level-2 engine; three-way vocabulary | H.4 → raised on `item:readers-ask-causal-access-intro` |
| 1 | `causal-access-intro` | lambda(M_t) stale vs lambda(M_t,O_t,N_h) | **defect present** (line 29) → `item:causal-access-intro-stale-lambda-parameterization` |
| 2 | `def-action-transition` | hidden learnability/smoothness of T | **superseded** A.1 scope clause 1 (scope-adaptive-system:41, world can still reveal something; (e) constant channel outside); finite-rate learnability is tempo's job, not scope's |
| 3 | `def-action-transition` | practical Omega-sizing cost | **set aside** practical construction of Omega belongs to TST/LLM application; no claim in canon depends on it; 01 is WLOG by design |
| 4 | `def-action-transition` | eq-tag typing of transition opacity | **superseded** A.1 rewrite: line 37 'may not know T ... random under reference measure pi_0', tag still Definition; the typed anatomy is in scope-adaptive-system |
| 5 | `def-adaptive-tempo` | 'useful information' gloss loose | **present** (line 13) → `item:adaptive-tempo-gloss-and-substitutability-scope` |
| 6 | `def-adaptive-tempo` | regression guard: no general additive upper bound | **regression guard**: keep at I.5 — keep at I.5 |
| 7 | `def-adaptive-tempo` | speed-quality substitutability regime-bounded | **present** (lines 15, 50) → `item:adaptive-tempo-gloss-and-substitutability-scope` |
| 8 | `def-adaptive-tempo` | candidate experiment: oversight monitor channel correlation | → `item:agent-proposed-experiments-in-part-i-working-notes` (E.2) |
| 9 | `def-agent-environment` | boundary-integrity unnamed | **not in canon** → raised on *existing* `item:boundary-integrity-second-constitutive-commitment` |
| 10 | `def-agent-environment` | computational vs perceptual opacity | **in canon** annotated answered 2026-10-30 in scope-adaptive-system |
| 11 | `def-agent-environment` | 'maintains internal state' for feedforward/transformer | **set aside** here: a watch on Volume 3; no 03 segment was found to confront it (grep), and the belongs drain carries Volume 3 reach in `item:llm-instantiations-from-01-audit-gold` |
| 12 | `def-agent-spectrum` | grounding/intent reframe cross-substrate convergent | corroboration of the `#def-agent-spectrum` WN 81–85 reframe (01-other drain's surface); also pedagogy |
| 13 | `def-agent-spectrum` | decompose Miller two-state threshold | **set aside** conditional on #worked-example-cam, which does not exist; body uses Miller as grounding only (15, 48, 88) |
| 14 | `def-causal-information-yield` | CIY name vs distinguishability substance | naming → raised on `item:naming-seeds-from-01-audit-gold` (F.1); body already glosses "action-distinguishability" (line 13) |
| 15 | `def-causal-information-yield` | tier inheritance of CIY-as-exploration use | **in canon** disc-ciy-unified-objective:17,21,25 labels the use heuristic and superseded by deriv-causal-ib-lmi |
| 16 | `def-causal-information-yield` | reference distribution q degree of freedom | **in canon** line 43 |
| 17 | `def-causal-information-yield` | overstuffed Discussion with downstream material | H.4 → raised on `item:readers-ask-def-causal-information-yield` |
| 18 | `def-chronica` | 'duplicating an agent's state' wording | **present** (lines 16, 36) → `item:what-is-non-forkable-trajectory-not-record` |
| 19 | `def-chronica` | digital non-forkability | **in canon** scope-agent-identity:40 (each copy its own agent at its first distinct event), :15,:29 |
| 20 | `def-chronica` | priors/M_0 vs chronica-only raw material | **present** (def-chronica:28 vs def-action-transition:37) → `item:chronica-only-raw-material-vs-built-in-knowledge` |
| 21 | `def-chronica` | linear chronica vs concurrent histories; vector o_t; missing a_0 | **present** → `item:what-is-non-forkable-trajectory-not-record` |
| 22 | `def-chronica` | entropy-collision rationale | H.4 → raised on `item:readers-ask-def-chronica` |
| 23 | `def-control-regret` | opposite monotonicity directions side by side | H.4 → raised on `item:readers-ask-def-control-regret` |
| 24 | `def-control-regret` | C2 default rationale inline | H.4 → raised on `item:readers-ask-def-control-regret` |
| 25 | `def-mismatch-signal` | score sign | **in canon** line 55-57 positive sign with direction stated |
| 26 | `def-mismatch-signal` | axiomatic vs 'definitional' | **set aside** frontmatter status is shown as typed and never computed from (vsect); aligning words changes nothing about truth |
| 27 | `def-mismatch-signal` | Gaussian 'coincide up to scaling' needs predictive-mean param | **present** (line 57) → `item:mismatch-signal-gaussian-coincidence-scope` |
| 28 | `def-mismatch-signal` | g transform prominence; TF-06 | H.4 → raised on `item:readers-ask-def-mismatch-signal`; TF-06 gone from body |
| 29 | `def-model-class-fitness` | inheritance of S relativity | **present** → `item:model-class-fitness-relativity-and-ceiling` |
| 30 | `def-model-class-fitness` | current estimate vs asymptotic ceiling | **present** (line 28) → `item:model-class-fitness-relativity-and-ceiling` |
| 31 | `def-observation-function` | known-noise Kalman | **in canon** annotated resolved 2026-10-30 |
| 32 | `def-observation-function` | is a_{t-1} cashed in | **in canon** a_{t-1} argument used structurally in 11 Part I/II segments |
| 33 | `def-observation-function` | opacity triad | **superseded** annotated; scope-adaptive-system typed anatomy |
| 34 | `def-pearl-causal-hierarchy` | Bareinboim citation precision | **in canon** lines 13, 21, 53 cite Bareinboim-Correa-Ibeling-Icard 2022 Thm 1; the weaker 'in general' form is what canon uses and is true |
| 35 | `def-pearl-causal-hierarchy` | L2 query is model-conditioned (belief about L2) | **not in canon** → `item:l2-query-is-belief-about-l2` |
| 36 | `def-satisfaction-gap` | gaps sum to total shortfall | **in canon** def-control-regret:40 |
| 37 | `def-satisfaction-gap` | finite V^min terminates the cascade (safety) | **in canon** 04-eli-core der-bounded-objective-as-sanity-criterion |
| 38 | `def-shared-intent` | theory of mind / nested beliefs missing | → raised on *existing* `item:theory-of-mind-missing-from-communication` |
| 39 | `def-shared-intent` | richer relevance variable | **in canon** item:def-shared-intent-ib-formalization-f157-f161 (F158) |
| 40 | `def-strategic-calibration` | Findings block feels out of place | **set aside** by design (source of FINDINGS.md); stumble signal goes to the pedagogy home |
| 41 | `def-strategic-tempo` | gain collapse eta_edge=1/(n+1) over time | **in canon** schema-strategy-persistence:17-19 makes exponential forgetting the structural prerequisite |
| 42 | `def-strategic-tempo` | tempo-maximizing topology theorem (shallow OR) | **not in canon** → `item:strategy-dag-optimal-topology` (C.4) |
| 43 | `def-strategic-tempo` | F66-F68 sum vs bottleneck; Regime-C nothing; heterogeneous thresholds | F66 **in canon** (per-edge weakest-link persistence, line 20); F68 **gone** from the body; F67 → raised on *existing* `item:strategic-tempo-regime-c-overstated` (audits drain judges it a defect; this drain first read it as true by construction of $\iota$, and the raise asks the owner to settle which) |E|rho/R bound is gone from the body; F67 set aside: T_Sigma is interventional strategy-revision tempo (iota factor, line 42), associational gains accrue to M_t |
| 44 | `def-strategy-dag` | formalize terminal-alignment error delta_align (4 substrates) | **not in canon** → `item:terminal-alignment-error-diagnostic` (C.4) |
| 45 | `def-strategy-dag` | relocate Correlation Hierarchy to Discussion/own segment | H.4 → `item:gold-placement-edits-without-readers-item` (a) |
| 46 | `def-strategy-dag` | topology discovery (where nodes/edges come from) | **not in canon** → `item:strategy-dag-topology-acquisition` (C.4) |
| 47 | `def-strategy-dimension` | O/Sigma ascribed vs literal | **in canon** B.1 record line 59 ('not a claim that all agents maintain both; reactive agents ...'); def-strategy-dag:167 |
| 48 | `def-strategy-dimension` | 'update source' row is typical, not law | **present** (line 38) → raised on `item:readers-ask-def-strategy-dimension` |
| 49 | `def-strategy-dimension` | no beta_Sigma for strategy compression | → raised on *existing* `item:strategy-compression-price-beta-sigma` |
| 50 | `def-unity-dimensions` | mixed-motive U_O aggregation | → `question:unity-mixed-motive-u-o-aggregation` |
| 51 | `def-unity-dimensions` | C-iv ontology drift into unity machinery | *existing* item:todo-613842-c-iv-idiom-drift-integration-debt-e3af |
| 52 | `def-value-object` | C2 monotonicity rung | **in canon** annotated resolved; Monotonicity block + #deriv-convention-monotonicity |
| 53 | `def-value-object` | causal-validity rests on too little | **in canon** annotated resolved 2026-05-30 (C1-C3 triple in Formal Expression) |
| 54 | `def-value-object` | exploration weight lambda(M,O,N_h) underived | **in canon** disc-ciy-unified-objective:17 labels the scalar form heuristic and superseded by the tensor trace-product of #deriv-causal-ib-lmi |
| 55 | `der-action-selection` | exact a_t=pi(M_t) vs pi(X_t) | **in canon** 'Exact within Part I scope' (39) and the Part II lift (35) |
| 56 | `der-action-selection` | 'tend to internalize' near-empirical not tier-marked | **superseded** the selective-pressure sentence is gone; lines 19/53 keep only the derivable faster-mode-preferred claim |
| 57 | `der-action-selection` | fluency tag; eta* update gain vs action quality | **present** (line 17) → `item:deliberation-benefit-channel-update-gain-vs-action` |
| 58 | `der-adversarial-destabilization` | effects-spiral mechanism candidates | → raised on *existing* `item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7` |
| 59 | `der-agent-opacity` | effects-spiral functional form | → same raise as #58 |
| 60 | `der-agent-opacity` | 4th identifiability-floor instance via Fano | **regression guard**: keep at I.5 — resolved-negative in WN (two spikes); keep as regression guard at I.5 |
| 61 | `der-causal-hierarchy-requirement` | 'purely predictive' -> 'purely associational' | **superseded** phrase absent at HEAD |
| 62 | `der-causal-hierarchy-requirement` | scope-propagation watch (PID/LQR examples) | **set aside** a watch, no claim; the cut is item-checked by B.1 records |
| 63 | `der-causal-insufficiency-detection` | one non-shallow construction | **not in canon** → `item:causal-insufficiency-nogo-general-topology-construction` (C.4) |
| 64 | `der-chain-confidence-decay` | anchor-role subsections out-of-place density | H.4 → `item:gold-placement-edits-without-readers-item` |
| 65 | `der-deliberation-cost` | Delta-eta* (update gain) vs action value scope | **present** (lines 15 vs 39) → `item:deliberation-benefit-channel-update-gain-vs-action` (C.4, strengthen first) |
| 66 | `der-deliberation-cost` | counterfactual baseline in Net accounting | → same item (counterfactual baseline) |
| 67 | `der-deliberation-cost` | (1-Delta-eta*) FOC factor watch | **set aside** a downstream watch, confirmed correct by two substrates; no use found that drops it (not exhaustively checked) |
| 68 | `der-deliberation-cost` | 'Open questions' in claims-verified segment | **set aside** convention texture; stage gating is under reconsideration (project memory) |
| 69 | `der-deliberation-cost` | unified search-during-pause template | → `item:search-during-pause-formalize-or-retire` (C.4) |
| 70 | `der-directed-separation` | do-not-re-promote 'organizations natively Class 3' | **regression guard**: keep at I.5 — keep at I.5; canon line 181 of deriv-strategic-composition carries the corrected truth |
| 71 | `der-directed-separation` | bounded-signaling as named scope condition | **in canon** lines 28, 237 |
| 72 | `der-directed-separation` | kappa_processing denominator support convention | **present** (line 90) → `item:directed-separation-kappa-convention-and-estimator-confound` (B.2) |
| 73 | `der-directed-separation` | behavioral kappa-hat confounds M_tau- with goal priming | **present** (lines 102–106) → same item; E.1 runs this estimator |
| 74 | `der-directed-separation` | distribution-independent structural coupling (max-flow) | → kept inside the same item as an open idea |
| 75 | `der-gain-sector-bridge` | nu/time normalization | **in canon** lines 35-51 |
| 76 | `der-gain-sector-bridge` | one-point vs strong convexity iff wording | **in canon** resolved on read; #deriv-gain-sector:271 |
| 77 | `der-gain-sector-bridge` | propagate sub-scope alpha/beta and failure modes | **set aside** watch-items; B.1 records carry population per claim |
| 78 | `der-gain-sector-bridge` | (PI)-Cencov density/placement | H.4 → raised on `item:readers-ask-der-gain-sector-bridge` |
| 79 | `der-interaction-channel-classification` | II-a/II-b conflation boxed warning | H.4 → raised on `item:readers-ask-der-interaction-channel-classification` |
| 80 | `der-interaction-channel-classification` | sufficient-statistics-span replacement for I_max | **not in canon** (body line 86 points to WN) → `item:interaction-channel-sufficient-statistics-span` (C.4) |
| 81 | `der-loop-interventional-access` | Regime A needs identifiable | **in canon** annotated resolved 2026-05-30 |
| 82 | `der-loop-interventional-access` | theorem conditions only in WN | **in canon** annotated resolved; C1-C3 in Formal Expression |
| 83 | `der-observability-dominance` | observability-investment economics criterion; F53 alpha_Sigma improvement not transparent | → `item:observability-investment-criterion` (C.4), cross-raised on *existing* `item:observability-investment-threshold-unsupported` (F53, audits drain) |
| 84 | `der-observability-dominance` | instrument intermediate milestones (eval-harness rule) | → same item (practitioner corollary) |
| 85 | `der-orient-cascade` | mid-cascade arrival: restart vs pipeline | → `question:orient-cascade-mid-cascade-arrival` |
| 86 | `der-orient-cascade` | bootstrapping out of low-complexity attractor | → `question:orient-cascade-low-complexity-attractor-escape` |
| 87 | `der-orient-cascade` | fast-inner/slow-outer as token-budget principle | Volume 3 reach → raised on `item:llm-instantiations-from-01-audit-gold` |
| 88 | `der-orient-cascade` | migration-note hygiene in WN | **set aside** I.5's Working Notes cleanup removes it |
| 89 | `der-recursive-update` | status drift conditional vs exact | **in canon** annotated resolved 2026-08-12; verified: der-recursive-update:41 'Exact' |
| 90 | `der-recursive-update` | 'completeness' bundles predictive and behavioral completeness | naming → raised on `item:naming-seeds-from-01-audit-gold` (F.1) |
| 91 | `der-recursive-update` | g_M left open; consolidation paragraph dense | **set aside** g_M is deliberately agnostic (line 47 says what it includes); the event-time seam is item:influx-event-time-seam |
| 92 | `der-team-persistence` | name Brooks's Law where threshold introduced | H.4 → raised on `item:readers-ask-der-team-persistence` |
| 93 | `der-team-persistence` | OUTLINE row reads 'Composite persistence condition' | **in canon** OUTLINE:280 now 'Per-sub-agent persistence within a team' |
| 94 | `der-team-persistence` | lift communication/action distinction earlier | H.4 → same raise |
| 95 | `der-tempo-composition` | wrapping as Brooks's-Law instance cross-ref | H.4 → `item:gold-placement-edits-without-readers-item` |
| 96 | `der-temporal-nesting` | 'must approximately converge' too strong | **in canon** line 13 now 'operating on the quasi-steady-state output of the level below' |
| 97 | `der-temporal-nesting` | PID nesting is frequency-domain not architectural | **present** (line 51) → `item:temporal-nesting-pid-row-is-frequency-not-rate` |
| 98 | `der-temporal-nesting` | illustrative table not a fixed ontology | **set aside** watch; table is labeled illustrative |
| 99 | `der-temporal-nesting` | candidate experiment: supervisor cadence vs oscillation | → `item:agent-proposed-experiments-in-part-i-working-notes` (E.2) |
| 100 | `deriv-critical-mass-composition` | rivalrous caveat | *existing* item:spikes-proposed-u-o-sector-constant-uo-mult-derivation-fbb6 |
| 101 | `deriv-critical-mass-composition` | heterogeneous dyad; N-agent O(N^2) ceiling | **in canon** heterogeneous case marked Open at 127, 149, 178; N-agent scaling corroborates the segment's own WN open item (01-other drain's surface) |
| 102 | `deriv-discrete-sector-condition` | heavy-tailed => structural adaptation routing | → raised on *existing* `item:todo-heavy-tailed-disturbances-model-s-assume-f3de` |
| 103 | `deriv-gain-sector` | expected-bridge + stochastic disturbance composition meta-pattern | **set aside** true observation (Prop A.1S takes the residual as Model-S disturbance); no claim depends on naming it a meta-pattern |
| 104 | `deriv-gain-sector` | diagonal alpha=min K_i matches per-dimension; 72% from averaging | **in canon** result-per-dimension-persistence:74-96 carries the bottleneck and the 72% overestimate |
| 105 | `deriv-graph-structure` | AND/OR parsimony uniqueness | → raised on *existing* `item:and-or-parsimony-uniqueness` (opened by the 01-other drain) |
| 106 | `deriv-graph-structure` | necessity watched downstream | **in canon** def-strategy-dag:237 'necessity direction ... open'; B.1 record 167 says sufficiency only |
| 107 | `deriv-persistence-cost` | positive-dual of identifiability floor; theorem-import meta-segment | → raised on *existing* `item:proposals-sp-23-disc-theorem-import-architecture-f-a22e` |
| 108 | `deriv-persistence-cost` | channel bandwidth is not tempo | **in canon** lines 57-67 state capacity as a prerequisite (necessary floor), not a source of tempo |
| 109 | `deriv-recursive-update` | C3-circularity acknowledgment must survive downstream | **set aside** a watch; der-recursive-update:41 carries it; B.1 records check per claim |
| 110 | `deriv-recursive-update` | continuous-coupling caveat propagation to g_M corollary | *existing* `item:influx-event-time-seam` (the between-event flow seam); not separately raised |
| 111 | `deriv-recursive-update` | '(Descended from TFT Appendix ...)' diff-voice | **superseded** no TFT/Descended string in body at HEAD |
| 112 | `deriv-sector-condition` | local-only proofs: guard against global-stability creep | **regression guard**: keep at I.5 — keep at I.5; Cor A.1S.1 (exit certain under Model S) is the canon statement that forbids it |
| 113 | `deriv-sector-condition` | double-floor regime for rule-based agents | **set aside** a 'candidate to check' with no claim; rule-based agents are sub-scope beta (posited), so no canon result is at stake |
| 114 | `deriv-sector-condition` | anisotropic noise: R*_S = sqrt(tr Sigma/(2 alpha)) | **in canon** line 309 names isotropy as scope and anisotropic noise as not covered; line 189 shows tr(sigma_w^2 I_n) |
| 115 | `deriv-strategic-composition` | replicator/ESS correspondence | → raised on *existing* `item:spikes-proposed-advanced-14-aat-replicator-evolutionary-game-dyna-689c` |
| 116 | `detail-linear-ode-approximation` | nothing new | **set aside** the bullet says so |
| 117 | `disc-adversarial-coupling-pressure` | adversary as bias-bound optimizer | **in canon**: #disc-adversarial-coupling-pressure:91 ("the bias bound that adversarial pressure attempts to saturate"); the adversary-as-optimizer reading is pedagogy |
| 118 | `disc-adversarial-coupling-pressure` | inline off-ramp note | **set aside** (also the off-ramp row) self-declared already tracked |
| 119 | `disc-ciy-unified-objective` | stale forward ref verified clean | **in canon** annotated resolved 2026-05-30 |
| 120 | `disc-ciy-unified-objective` | Pinsker -> BH | **in canon** annotated resolved |
| 121 | `disc-ciy-unified-objective` | domain table 'Exactly derived' overstates for Gittins/IDS | **defect present** (lines 36, 39) → `item:ciy-unified-objective-domain-table-overstates` |
| 122 | `disc-composition-consistency` | boundary-choice rationality principle | → raised on *existing* `item:todo-disc-composition-consistency-does-direct-813e` |
| 123 | `disc-composition-consistency` | does directed separation compose | → same raise |
| 124 | `disc-composition-consistency` | redundancy correction for nested parallel sub-agents | **in canon** CC-parallel lambda_c = min_i (line 50) is the redundancy-free bound; a redundancy-raises-kappa claim would need a derivation; set aside as unasked theory |
| 125 | `disc-composition-consistency` | Tier names are placeholder numbering | naming → raised on `item:naming-seeds-from-01-audit-gold` (F.1) |
| 126 | `disc-composition-consistency` | birth-death of composite agents unmodeled | Volume 4 reach → raised on `item:eli-reach-from-01-audit-gold` |
| 127 | `disc-continuity-stance` | 'orthogonal' overstates | **in canon** annotated resolved 2026-05-30 (L1/L2/L3) |
| 128 | `disc-continuity-stance` | serverless boundary case | → raised on *existing* `item:continuity-stance-boundary-cases` |
| 129 | `disc-credit-assignment-boundary` | F60-F62 | F62 → raised on *existing* `item:credit-assignment-overestimate-sign-is-topology-dependent` (C.3; the segment still says it, against `#def-strategy-dag`'s sign table); F60 and F61 recorded in that raise, **not verified** here |
| 130 | `disc-exploit-explore-deliberate` | strategy-structured sim to show deliberation's value | → `item:agent-proposed-experiments-in-part-i-working-notes` (E.2) |
| 131 | `disc-exploit-explore-deliberate` | promote 'deliberation as internal exploration' out of Discussion | **in canon** now in the opening summary (line 18) and the key distinction (36) |
| 132 | `disc-identifiability-floor` | composition theorem for impossibilities | **not in canon** → `item:identifiability-floor-escapes-compose-and-cost` (C.4) |
| 133 | `disc-identifiability-floor` | escapes carry costs not surfaced | → same item |
| 134 | `disc-modularity-state-dynamics` | none | **set aside** the bullet says so |
| 135 | `disc-separability-pattern` | cross-ladder monotonicity / General Open infectious | **set aside** here: corroborates the segment's own WN cross-ladder bullet (01-other drain's surface); no body hit |
| 136 | `disc-separability-pattern` | necessity theorem for the pattern | **set aside** corroborates the segment's own WN item (01-other drain's surface); discussion-grade stands |
| 137 | `disc-stability-certificate` | accumulation-typing paragraph too dense | H.4 → `item:gold-placement-edits-without-readers-item` |
| 138 | `disc-strategic-self-coupling` | self-control as single-agent composition | → raised on *existing* `item:spikes-proposed-spike-strategic-self-coupling-p2-p4-appe-3163` |
| 139 | `disc-value-functional-grounding-floor` | three failed third-route attempts | → raised on *existing* `item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366` |
| 140 | `emp-update-gain` | U_o estimation tension | **in canon** lines 17, 50 'Resolving Epistemic Opacity' |
| 141 | `emp-update-gain` | U_M variance vs entropy cannot be added | **present** (line 29) → `item:update-gain-u-m-variance-or-entropy` |
| 142 | `emp-update-gain` | Open questions placement; TF-06 tag | **set aside** TF-06 gone from body; 'Open questions' (79) is reader-facing scope honesty |
| 143 | `emp-update-gain` | U_M symbol overload (model uncertainty vs epistemic unity) | → raised on *existing* `item:influx-part-i-symbol-and-term-collisions` (F.4) |
| 144 | `emp-update-gain` | 'any optimal adaptation process must approximate' universal | **superseded** phrase absent at HEAD |
| 145 | `emp-update-gain` | forward pointer: mood as slow modulator of gain | **regression guard**: keep at I.5 — legitimate forward pointer (#def-mood exists); keep at I.5 |
| 146 | `emp-update-gain` | candidate experiment: gain-collapse mode detection | → item:agent-proposed-experiments-in-part-i-working-notes |
| 147 | `form-agent-model` | where do priors/pretrained weights live | → item:chronica-only-raw-material-vs-built-in-knowledge |
| 148 | `form-agent-model` | chronica shorthand at line 28 | H.4 → raised on item:readers-ask-form-agent-model |
| 149 | `form-agent-model` | PID 'too impoverished' reads strong | **superseded** line 43 now 'A PID controller's M_t is degenerate' |
| 150 | `form-complete-agent-state` | 'single point of interaction' over-strong | → raised on *existing* `item:complete-agent-state-single-point-claim` (C.3) and on `item:readers-ask-form-complete-agent-state` |
| 151 | `form-complete-agent-state` | uniqueness conjecture | **in canon** annotated resolved 2026-08-24; #deriv-decomposition-uniqueness |
| 152 | `form-complete-agent-state` | backward compatibility assumes directed separation | H.4 → raised on `item:readers-ask-form-complete-agent-state` (line 46) |
| 153 | `form-composition-closure` | most modern composites are Tier 3 | **in canon** Tier 3 marked discussion-grade with per-domain verification (lines 176, 204) |
| 154 | `form-composition-closure` | (P1) computability narrow | **set aside** corroborates the segment's own WN open item (01-other drain's surface) |
| 155 | `form-consolidation-dynamics` | EWC as tensor gain; effect on scalar proofs | **in canon** line 135 (EWC reading); #deriv-matrix-persistence-condition carries the matrix-Loewner persistence condition |
| 156 | `form-consolidation-dynamics` | off-ramp flags (i)-(iii) | see same bullet as the Off-ramp row |
| 157 | `form-event-driven-dynamics` | nu_eff vs T two symbols | → raised on *existing* item:influx-part-i-symbol-and-term-collisions |
| 158 | `form-event-driven-dynamics` | MI vs realized surprise | → raised on *existing* item:expected-vs-realized-information-symbol |
| 159 | `form-event-driven-dynamics` | out-of-order / simultaneous events | → question:event-stream-out-of-order-arrival |
| 160 | `form-event-driven-dynamics` | stale Section IV ref; missing form-agent-model dep | **in canon** annotated resolved 2026-08-12 |
| 161 | `form-information-bottleneck` | defensive Discussion relocation | H.4 → raised on item:readers-ask-form-information-bottleneck |
| 162 | `form-information-bottleneck` | Tishby-Zaslavsky 2015 IB-VFE citation | **superseded** the VFE paragraph (line 56) now cites Friston 2010, Friston et al. 2017, Parr and Pezzulo 2022; T-Z 2015 not cited |
| 163 | `form-objective-functional` | revealed preference overstates | **in canon** annotated resolved 2026-05-30 |
| 164 | `form-objective-functional` | trajectory domain under-specified | **in canon** annotated resolved 2026-05-30 |
| 165 | `form-objective-functional` | AND-node workaround loses tradeoff magnitudes | **in canon** line 62: true Pareto structure requires a vector-valued extension |
| 166 | `form-sector-condition` | kappa(P-) caveat downstream | **set aside** a watch; no use without the caveat was searched for |
| 167 | `form-strategy-complexity-cost` | compression by convergence | **set aside** corroborates the segment's WN bullet (01-other drain's surface) |
| 168 | `form-strategy-complexity-cost` | F69 resolved; F70 C_revise; F71 deps | → F69 in canon; F70 item:strategy-complexity-revise-cost-rate; F71 raised on item:todo-lint-outline-eq-tag-topological-priority-646d |
| 169 | `form-structural-change-as-parametric-limit` | F63-F65 | **partly unverified**: line 38 states the continuity claim as a property of the representation ('adding or removing an edge is a boundary event'); whether an ambient supergraph is stated, and F64/F65, not checked at depth -> left open, see read ledger |
| 170 | `form-structural-change-as-parametric-limit` | stale TF-10 | **in canon** annotated resolved 2026-05-31 |
| 171 | `hyp-auftragstaktik-principle` | don't import human ordering to AI teams | **set aside** a watch; item:t1-auftragstaktik-allocation-and-conway restates the ordering as marginal and conditional, which carries it |
| 172 | `hyp-communication-gain` | theory of mind | → raised on *existing* item:theory-of-mind-missing-from-communication |
| 173 | `hyp-communication-gain` | Sybil attacks on transitive trust | → question:transitive-trust-sybil-resistance |
| 174 | `hyp-directed-separation-under-composition` | Case 1 needs goal-blind projection (F122) | → raised on *existing* item:todo-disc-composition-consistency-does-direct-813e |
| 175 | `hyp-edge-update-via-gain` | two log-odds coordinates; uncertainty ratio metric | → item:edge-update-two-log-odds-conflated |
| 176 | `hyp-mismatch-dynamics` | Model D equality vs ultimate bound | → item:mismatch-dynamics-model-d-equality-scope |
| 177 | `hyp-mismatch-dynamics` | visually separate Model D / Model S | H.4 → `item:gold-placement-edits-without-readers-item` |
| 178 | `hyp-mismatch-dynamics` | undeclared deriv-discrete-sector-condition | → raised on *existing* item:todo-lint-outline-eq-tag-topological-priority-646d |
| 179 | `hyp-symbiogenic-composition` | mu* from local-disturbance spectrum | → question:symbiogenic-retained-autonomy-from-disturbance-spectrum |
| 180 | `hyp-symbiogenic-composition` | transaction-cost framing | **set aside** corroborates the segment's WN 'Quantitative predictions' (01-other drain's surface); pedagogy |
| 181 | `impl-orient-cascade` | none | **set aside** bullet says so |
| 182 | `impl-strategy-structure` | L1' mixing weight | *existing* question:where-does-the-l1-mixing-weight-theta-c-for-a-so |
| 183 | `impl-strategy-structure` | three-layer causal sufficiency phrasing as model | **in canon** def-strategy-dag:245 now states the three requirements |
| 184 | `norm-explicit-strategy-condition` | 'loop learning does not inherit biases' | **superseded** line 44 now 'loop-based learning inherits a different bias' |
| 185 | `norm-explicit-strategy-condition` | persistence-margin grounding vs continuity stances | → item:explicit-strategy-norm-assumes-continuation |
| 186 | `norm-explicit-strategy-condition` | undeclared result-persistence-condition | → raised on *existing* item:todo-lint-outline-eq-tag-topological-priority-646d |
| 187 | `norm-explicit-strategy-condition` | common units / risk | **set aside** the body's caveat names it; reader-emphasis only |
| 188 | `persistence-and-limits-intro` | below-threshold phrasing | **in canon** annotated executed 2026-07-04 |
| 189 | `post-causal-structure` | 'Nominal' opposite meanings | *existing* item:todo-nominal-denotes-opposite-scope-membershi-c7a1 |
| 190 | `post-causal-structure` | TF-02 lineage | **superseded** no TF-02 in body |
| 191 | `post-causal-structure` | 'more weight to causally downstream observations' | → item:causally-downstream-weighting-not-derived |
| 192 | `post-causal-structure` | coupling taxonomy used downstream? | → raised on *existing* item:influx-agency-condition-4-two-readings |
| 193 | `result-adversarial-exponent-regimes` | optimal drift fraction | → question:adversary-optimal-drift-fraction |
| 194 | `result-adversarial-tempo-advantage` | Boyd class restriction | H.4 → raised on item:readers-ask-result-adversarial-tempo-advantage (line 90 already hedges 'empirical') |
| 195 | `result-adversarial-tempo-advantage` | lift 'two effects compound' | H.4 → same raise |
| 196 | `result-adversarial-tempo-advantage` | finite-nu reconciliation as exemplar | → pedagogy home (an exemplar of how the framework treats its discrepancies) |
| 197 | `result-mismatch-decomposition` | orthogonality not independence | **in canon** in the body (the bullet says so); pedagogy |
| 198 | `result-mismatch-decomposition` | GA-1 / def-action-transition deps | **in canon** def-action-transition now in depends (line 8) |
| 199 | `result-per-dimension-persistence` | coupled-correction regime | **in canon** #deriv-matrix-persistence-condition; the empirical question 'do highly coupled models survive better' set aside (no claim at stake) |
| 200 | `result-persistence-condition` | hysteresis | → raised on *existing* item:persistence-hysteresis-hypothesis |
| 201 | `result-persistence-condition` | transient adequacy | → raised on *existing* item:transient-adequacy-third-persistence-condition |
| 202 | `result-persistence-condition` | heavy-tailed disturbance | → raised on *existing* item:todo-heavy-tailed-disturbances-model-s-assume-f3de |
| 203 | `result-persistence-condition` | four-sense persistence taxonomy visible | *existing* item:terminology-todo-breakage-a-the-persistence-subgroup-mixe-2fb5 (LEXICON side); README visibility is A.2's |
| 204 | `result-persistence-condition` | Findings block out of place | **set aside** by design; stumble signal to the pedagogy home |
| 205 | `result-persistence-condition` | forward pointer: mood | **regression guard**: keep at I.5 — legitimate forward pointer; keep at I.5 |
| 206 | `result-persistence-condition` | candidate spike: R-dot vital sign; triage protocol | → item:agent-proposed-experiments-in-part-i-working-notes |
| 207 | `result-sector-condition-stability` | nu normalization | **in canon** annotated resolved 2026-05-30 |
| 208 | `result-sector-condition-stability` | heavy tails uncovered | → raised on *existing* item:todo-heavy-tailed-disturbances-model-s-assume-f3de |
| 209 | `result-sector-persistence-template` | fallacy of empty instantiation | **regression guard**: keep at I.5 — keep at I.5; the template states it |
| 210 | `result-structural-adaptation-necessity` | argsup attainment | → item:structural-adaptation-argsup-and-objective-relative-necessity |
| 211 | `result-structural-adaptation-necessity` | necessity relative to objective | → same item |
| 212 | `result-structural-adaptation-necessity` | alignment-assumption failure regime | **in canon** lines 19, 50 name it |
| 213 | `result-structural-adaptation-necessity` | search-during-pause analogy | → item:search-during-pause-formalize-or-retire |
| 214 | `result-structural-adaptation-necessity` | candidate experiment: residual-autocorrelation triage | → item:agent-proposed-experiments-in-part-i-working-notes |
| 215 | `result-unity-closure-mapping` | MZ non-Markovian consequence as Discussion | → pedagogy home; the MZ WN-only math is the 01-other drain's |
| 216 | `result-unity-closure-mapping` | non-stationary MZ | **set aside** curiosity attached to the segment's MZ WN note (01-other drain's surface) |
| 217 | `schema-strategy-persistence` | dynamic lambda tuning | → question:strategy-forgetting-rate-under-disturbance-spikes |
| 218 | `schema-strategy-persistence` | forgetting vs consolidation | → same question |
| 219 | `schema-strategy-persistence` | regression guard F72 | **regression guard**: keep at I.5 — keep at I.5 |
| 220 | `scope-adaptive-system` | temporal quantifier | **in canon** annotated resolved 2026-10-30 (A.1) |
| 221 | `scope-adaptive-system` | Agent set element vs passive observers | **in canon** resolved upstream in #def-agent-environment (the gold says so); A.1 rewrite since |
| 222 | `scope-adaptive-system` | C_t in depends; passive-observer degenerate C_t | **set aside** not checked: #scope-adaptive-system is being edited in the A.1 lane's worktree now |
| 223 | `scope-agency` | do(a) without depends; Part-I restatement | → raised on *existing* item:influx-agency-condition-4-two-readings |
| 224 | `scope-agency` | existential quantifier is one effective action | **set aside** a watch; the choice is deliberate |
| 225 | `scope-agent-identity` | (PI) placement | H.4 → raised on item:readers-ask-der-gain-sector-bridge (same placement question, both segments) |
| 226 | `scope-agent-identity` | (PI) depends/ordering | → raised on *existing* item:todo-lint-outline-eq-tag-topological-priority-646d |
| 227 | `scope-agent-identity` | record vs token chronica | → item:what-is-non-forkable-trajectory-not-record |
| 228 | `scope-agent-identity` | 'no generally optimal merge' depends on criterion | → same item |
| 229 | `scope-agent-identity` | form-objective-functional status axiomatic | **set aside** the status word is shown as typed and never computed from; #form-objective-functional is B.1's template record, which carries its register |
| 230 | `scope-and-or` | native k-of-n node under MDL pressure | → raised on *existing* item:and-or-parsimony-uniqueness |
| 231 | `scope-ciy-observational-proxy` | Omega_t in proxy | → item:ciy-proxy-omega-and-llm-agent-regime |
| 232 | `scope-ciy-observational-proxy` | Regime A wording | **in canon** annotated resolved; line 37 |
| 233 | `scope-ciy-observational-proxy` | LLM software agents Regime B | → same item |
| 234 | `scope-ciy-observational-proxy` | 'approximated' vs 'not an approximation' | **superseded** 'approximated from observational data' absent; line 53 stands alone |
| 235 | `scope-ciy-observational-proxy` | TF-08; reads before canonical CIY | **superseded** no TF-08 in body; OUTLINE puts #def-causal-information-yield (52) before the proxy (147) |
| 236 | `scope-composite-agent` | asymmetric composites | **set aside** corroborates the segment's WN 'Asymmetric unity' (01-other drain's surface) |
| 237 | `scope-composite-agent` | transitivity and coalition fragility | **set aside** corroborates the segment's WN 'Transitivity' (01-other); the coalition reading is pedagogy |
| 238 | `scope-edge-update-causal-validity` | Regime-C provenance metadata (LLMs start all-C) | Volume 3 reach → item:llm-instantiations-from-01-audit-gold (belongs drain), cited there as the same reach |
| 239 | `scope-multi-agent` | routes read before they are defined | H.4 → `item:gold-placement-edits-without-readers-item` |
| 240 | `scope-multi-agent` | C-iv needs careful prose | **set aside** pointer to the scope-composite-agent note |
| 241 | `strategy-structure-intro` | filename reads like a part entry point | **set aside** filenames are slugs by design (no ordering in filenames); OUTLINE is the entry |
| 242 | `the-cycle-in-motion-intro` | 'derived, not chosen' | **superseded** phrase absent at HEAD |
| 243 | `the-cycle-in-motion-intro` | Pearl-import convention stated late | → raised on *existing* item:influx-agency-condition-4-two-readings |
| 244 | `the-reality-model-intro` | 'central result' is a promissory note | **set aside** #result-structural-adaptation-necessity is conditional and says so; whether intros overstate is A.2's headline check |


**What this category turned out to be.** Counted from the table (a row can carry two dispositions; the first is counted): 66 already in canon (many annotated in place as resolved) and 14 superseded; 32 point at a new item opened by this drain, of which 16 are present defects or precision gaps (C.1, one B.2) and the rest are C.4 theory edges (optimal topology, the terminal-alignment diagnostic, topology acquisition, the general-topology no-go construction, composition and cost of identifiability-floor escapes, the sufficient-statistics span, the observability-investment criterion, the deliberation benefit channel, search-during-pause); about 45 are raised on existing items, including the "same item" follow-on rows; 22 are reader-clarity edits under H.4; 8 are questions; 6 are agent-proposed experiments pooled in one E.2 item; 8 are regression guards to keep; 3 go to the pedagogy home; 37 are set aside with the reason in the row (watches with no claim at stake, corroboration of a segment's own Working Note, empty bullets, items the A.1 lane is editing now). One row (#169, F63–F65 on `#form-structural-change-as-parametric-limit`) is only partly checked.

**Two things the follow-ups show about the surface.** First, the gold's "resolved" annotations are unreliable in both directions. Some say resolved and are (`#der-recursive-update`'s status drift). Some resolved items carry no annotation (`#der-temporal-nesting`'s "approximately converge", `#emp-update-gain`'s universal-optimality sentence). And the same annotation pattern led a 2026-08-12 reader to write, twice, that "the gold contains resolved items that do not say so". Second, the follow-ups and the 01-other drain's non-gold notes overlap heavily: the gold is often a second, convergent statement of a Working Note's own open item. A WN cleanup that treats the two layers separately will leave duplicates.

### Certified-track F-streams named only in gold preambles

Four gold preambles say a 526815 F-row stream "is certified-track and routed there, not here". No off-ramp carries them, and the audits drain left most of them "not dispositioned" for the Part III integrators. Checked at `4175aae7`:

| preamble (WN line) | stream | disposition |
|---|---|---|
| `der-team-persistence` (126) | F182, F189–F194 | F182, F194 the auditor's own resolved/watch rows; F189–F193 **present** → `item:team-persistence-526815-f189-f193` (C.1) |
| `der-adversarial-destabilization` (97) | F183, F185, F195–F202 | → `item:adversarial-cluster-526815-f195-f221-residue` (C.1), row by row: F195, F196, F201 present; F200 gone; F198, F199 not found; F183, F185, F202 resolved/watch |
| `der-interaction-channel-classification` (182) | F203–F213 | F203/F204 *existing* `item:expected-vs-realized-information-symbol`; F205 my Off-ramp item; F206, F210 present (same residue item); F209 *existing* `item:part-iii-unit-and-index-slips`; F211 raised on the lint item; F207, F212 not verified; F208 in canon (body calls the class boundary heuristic); F213 watch |
| `result-adversarial-tempo-advantage` (102) | F215–F221 | F215 resolved in substance; F216, F217, F219 present (residue item; deps raised on the lint item); F218 not verified; F220 not found; F221 watch |

The other 115 preambles are coverage and attribution notes (which audits were harvested, substrate attribution). They are provenance for the pedagogy home and are **set aside** as items; the home keeps them with their blocks.

### Regression guards inside gold (7)

`#impl-cooperative-adversarial`'s "Regression guards (526815 F222–F232 / audit 731548)" block: six forms the segment deliberately does not carry, each with why it is false. **Keep at I.5** (FORMAT's own criterion for a Working Note). Its second guard (one-sided noise prescription) is the same defect as *existing* `item:t1-gated-tempo-one-sided-noise-prescription`, which fixes it at the source segments.
