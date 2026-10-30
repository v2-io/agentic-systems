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

*(filled as the work proceeds)*

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
| `detail-linear-ode-approximation` (236) | the Model D steady state is exactly tight for constant drift | **true, not stated**. With scalar correction $\mathcal T$, constant $w$ gives $\delta\to w/\mathcal T$ exactly. Line 192's "typical disturbances … lie below" is true for non-persistent ones. It is a one-sentence clarity → H.4 item for this segment |
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

