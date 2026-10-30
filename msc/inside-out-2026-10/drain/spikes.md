# Drain: the live spikes in `spikes/`

*Serves G.2 (stranded additions landed or set aside), C.1 and C.4 (defects and held strengthenings get an owner), D.2 (the three Aug-24 spikes waiting on an integrator that never launched), and I.3 (one ledger) of `../INTENT.md`. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Working file of the spike drain, 2026-10-30, at asf `cbd2f345`. Written as it goes; read it whole.*

*Complete for every live entry. Five forks of this agent each read one cluster and wrote `spikes-<cluster>.md` beside this file; I read each of their files whole, and their dispositions are merged below. The fork files carry the reasoning and the line-level evidence. This file carries the merge, my own row, and what the lead should route. Commits: 72947487 (my row, fork B2), 320cb47a (forks A, C), 69ff7be1 (forks B1, D).*

## What matters most

1. **Three spike results the routing record carried as landable are false; one canon body already leans on a fourth.** None of the false ones reached canon. Each was caught because a fork re-derived the result instead of checking whether it had landed, which is what every earlier routing pass did.
   - **Update-operator (O-A2′).** It claims per-edge credences converge to the truth from one plan-level outcome. That outcome identifies only the product of the credences, so the claim fails for two or more edges (fork A's algebra and simulation; my independent identifiability argument). Its item is closed as superseded.
   - **Temporal-nesting RG-0a.** It claims heterogeneous Kalman gains flow to $\varepsilon^\ast = 0$ as the timescale ratio grows. The spike's own formula keeps a term that does not depend on that ratio, and a simulation of the spike's setup shows a floor near 0.21 (fork B1). Warning blocks now head the spike files, and the corrected statement is a G.2 addition.
   - **The $\rho$ additive-variance theorem.** Its cross term double-counts (fork A). Canon's later correction stands; the theorem must not be re-landed.
   - **The leakage-locus lemma** (fork C) is the fourth. It is cited and typed "derived" in `#disc-partial-coupling-pathways`'s body, but exists only in its spike.
2. **The verified work no integrator was launched for now has owners.** That covers the 2026-08-24 decomposition cluster (D.2's three waiting spikes, plus the $\varepsilon$-programme) and honest activation (twice verified; it fills a `missing` Volume 4 row). The same goes for the "released to the standing cycle" and "Joseph's call" hand-offs in honest activation, tst-independent, partition-isolation and the TST cycle.
3. **New present-tense canon defects (C.1), each with an item:**
   - `#def-death-as-factor-loss:57`: the (D4) severing-source axis.
   - `#internal-external-decomposition:59`: the multiplicative no-go is stated more strongly than it is proved.
   - `#der-architecture-noidentifiability` and `#disc-identifiability-floor:111`: "$F$ Hurwitz" with drift $-F$, in an exact block.
   - `#der-directed-separation:108`: Boundary 2's "self-limiting" holds for process-form coupling only.
   - `#disc-identifiability-floor:143`: the catalog boundary.
   - `#hyp-solicitable-escape:44`.
   - Three body sentences still call `#disc-implementation-impossibility` "queued".
   - Two TST readings: weakest channel read as weakest direction, and bistability stated as settled.
   - `#der-gain-sector-bridge:76`: a PID row tagged Derived, carried on the CL-1 item.
4. **For the lead, already sent:** today's Part II landing cites spike paths in twelve canon bodies (fork C; re-checked by me; recorded on `item:canon-bodies-cite-local-working-paths`). The Part II check write-up (fb4a205a) has since added the same finding as its item 8.
5. **A drain lesson.** Two of the false results (RG-0a, update-operator) had passed a 2026-05-17 routing pass that checked presence and regression only. A third pattern, from fork D, is a TST synthesis whose "three-spike convergence" was one shared misreading of one segment. A routing step that does not re-derive, or that counts arrivals without checking whether they share a premise, reports what was written as if it were true.

## Ledger totals

33 new items, 2 new questions, 2 closes (`item:todo-spike-update-operator-sector-orphan-regr-b62b` superseded, on my second-mind route; `item:proposals-d-9-sp-22-operator-family-tier-2-backlog-0b44` as a duplicate of the single CL-1 item `…a707`, by fork A). About 40 existing items received a dated "Source added" paragraph. By owner: G.2 holds most of the new items, then C.1 (10), C.4 (5), F.3 (4), F.2 (1), G.0 (1) and H.3 (1). Each fork file ends with its exact list.

## Disposition of every live entry

| Entry | Disposition | Where |
|---|---|---|
| `spike-decomposition-uniqueness-2026-08-24.md` | in canon (core); novelty verdict found outside asf | lead; `item:the-prior-art-search-…` |
| `-distributional-` (+ suggestions), `belief-splintering-genericity`, `epsilon-programme/` | true, partly verified, unlanded | lead; `item:land-the-2026-08-24-…`, `item:apply-the-epsilon-programme-…` |
| `spike-honest-activation-2026-09-23/` | true, twice verified, unlanded | lead; five items/questions above |
| hard-ceiling 05-31 spike, verify-1, notes; `sim-forgetting-conventions.py` | landed today; 05-31 superseded | lead; `item:neurips-paper-2-…` |
| today's four (`epistemic-target-ontology/`, exit-time, loop-identification, allocation-vs-distortion) | live lanes, noted only | lead |
| `update-operator-sector` | false headline; set aside | A |
| `passivity-composition`, `pid-a2prime`, `bridge-lemma` | CL-1, defects to fix first; §7.1 in canon | A; `…a707` |
| `rho-additive-variance` | correctly superseded; exposes a C.1 | A |
| `neutral-drift` | mostly in canon; two sentences left | A |
| `kl-to-state`, `alignment-impossibility` §7 | set aside (own gate fired; overclaim) | A |
| `alignment-impossibility` core, `composition-scaling-N` framing | in canon | A |
| `transient-dependency-amplification` | true at conditional tier, unlanded | A; `…441c` |
| `aporia-sub-agent-adversarial` | brainstorm, held | A; `sp-18` |
| `class-coercion-wrapping/`, `track-a-intent-dag/` | in canon; file | B1; `…d206` |
| `temporal-nesting-rg/` | RG-0a false; RG-0c no-go unlanded; Moves A(half), C, D open | B1 |
| root sims and PNGs | three-way tradeoff unregistered (F.3); GUC toys expose a C.1 | B1 |
| `strategic-composition-class-3`, `class2-typology`, `cohen-2022`, `integration-reconciliation`, three plan files | in canon or spent; file | B2 |
| `leakage-locus` | true, unlanded, canon leans on it | C |
| `strategic-self-coupling`, `c2prime` | in canon (c2prime landed today); file | C |
| `goal-flow-duality`, `prospective-mood`, `escape-standpoint` | partly or wholly unlanded; items | C |
| `m4-worked-example-soviet` | argued; G.0 test case | C |
| `c2-star-to-integrate` | motivating claim deleted today; plan stale | C |
| attention pair | mostly absorbed; two speculative gaps; duplicate items to reconcile | C |
| `language-as-causal-substrate/` | Theorem 1 unlanded, narrowed to testimonial L2 | C |
| `meta-agi-sgi-etc.md` | not a spike; set aside | C |
| `neurips-back-integration` | map; the neurips influx drain's | C |
| `tst-ideas-cycle/`, `tst-mining/`, `tst-independent`, `partition-isolation` | unlanded, with three over-warrant corrections; items | D |
| `tst-regime-breakout-sims`, `local-embedding-benchmark` | set aside | D |
| `visual/` | partly in canon; three decisions now an H.3 item | D |
| `INDEX.md`, `README.md`, `.routing-trail/`, `__pycache__/` | instruments; see the lead's row | lead |

## Filing moves, not made

None of these is canon and each has had its content checked first-hand. I didn't make them because they need `spikes/.integrated/MANIFEST-<date>.md` and `INDEX.md` edits that I.3 may moot, and some paths are cited from `HANDOFF.md` and the scout maps. They are mechanical once the lead says go; I can do them.

- **To `.integrated/`:**
  - B2's seven entries: `strategic-composition-class-3-attempt-2026-05-21/`, `spike-class2-typology-2026-05-22/`, `spike-cohen-2022-strengthening-2026-05-22/`, `spike-integration-reconciliation-2026-05-22/`, and the three plan files.
  - From C: `spike-strategic-self-coupling.md`, `spike-c2prime-realization-spectrum-2026-05-31.md`.
  - From A: `spike-alignment-impossibility.md`, `spike-composition-scaling-N.md`.
  - From B1: `class-coercion-wrapping/`, `track-a-intent-dag/`.
  - The hard-ceiling verify-1 and its integration notes.
- **To `.archived/`, each with its reason:**
  - the 2026-05-31 hard-ceiling spike, with `sim-forgetting-conventions.py`;
  - `spike-update-operator-sector.md`;
  - `spike-kl-to-state-distance-template-extraction-2026-04-24.md`;
  - `meta-agi-sgi-etc.md`;
  - `spike-tst-regime-breakout-sims-2026-03/`;
  - `spike-local-embedding-benchmark/`;
  - `spike-rho-additive-variance-strengthening-2026-04-24.md`, after a second mind confirms the double count.
- **Stay live until their items land:** everything else.

After any move, Working Notes pointers into the moved paths go stale (B2 counts about fifteen for its seven). They are Working Notes, not canon, so the Working Notes drain re-points them.

## Partition

| Who | Spikes |
|---|---|
| this file (lead of the drain) | the 2026-08-24 cluster (`spike-decomposition-uniqueness-2026-08-24.md`, `-distributional-` and its integration suggestions, `spike-belief-splintering-genericity-2026-08-24.md`, `spike-epsilon-programme-2026-08-24/`); `spike-honest-activation-2026-09-23/`; the hard-ceiling trio; today's four lanes (noted only); `.routing-trail/`, `__pycache__/`, `INDEX.md`, `README.md` |
| fork A → `spikes-a-operator.md` | `spike-update-operator-sector.md`, `spike-passivity-composition.md`, `spike-pid-a2prime.md`, `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md`, `spike-rho-additive-variance-strengthening-2026-04-24.md`, `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md`, `spike-kl-to-state-distance-template-extraction-2026-04-24.md`, `spike-alignment-impossibility.md`, `spike-composition-scaling-N.md`, `spike-transient-dependency-amplification.md`, `spike-aporia-sub-agent-adversarial.md` |
| fork B1 → `spikes-b1-dirs.md` | `class-coercion-wrapping/`, `track-a-intent-dag/`, `temporal-nesting-rg/`, the loose root sims and PNGs (`sim_guc_boundaries.py`, `sim_guc_classes.py`, `sim-w1-w2-boundary.py`, `sim-forgetting-conventions.py`, `sim-three-way-tradeoff.py`, `guc_boundaries.png`, `w1-w2-boundary.png`) |
| fork B2 → `spikes-b2-composition.md` | `strategic-composition-class-3-attempt-2026-05-21/`, `spike-class2-typology-2026-05-22/`, `spike-cohen-2022-strengthening-2026-05-22/`, `spike-integration-reconciliation-2026-05-22/`, `identifiability-floor-integration-plan.md`, `implementation-impossibility-meta-segment-plan.md`, `meta-segment-narrative-ordering-sweep-plan.md` |
| fork C → `spikes-c-coupling-llm.md` | `spike-leakage-locus-2026-05-18.md`, `spike-strategic-self-coupling.md`, `spike-c2prime-realization-spectrum-2026-05-31.md`, `spike-goal-flow-duality-2026-05-31.md`, `spike-m4-worked-example-soviet-2026-05-24.md`, `spike-prospective-mood-two-channel-borrowing-2026-06-17.md`, `spike-escape-standpoint-axis-2026-07-29.md`, `spike-c2-star-to-integrate.md`, `spike-attention-governance.md`, `spike-attention-causal-graphs.md`, `spike-language-as-causal-substrate/`, `meta-agi-sgi-etc.md`, `neurips-back-integration-2026-05-08.md` |
| fork D → `spikes-d-tst-misc.md` | `tst-ideas-cycle-2026-05-21/`, `tst-mining-2026-05-21/`, `spike-tst-independent-derivations-2026-07-04.md`, `spike-partition-isolation-criterion-2026-07-28.md`, `spike-tst-regime-breakout-sims-2026-03/`, `visual/`, `spike-local-embedding-benchmark/` |

Two mid-run widenings, relayed to every fork: Joseph's instruction to check every other surface (audits and gold, Working Notes, other spikes, `msc/`, influx and its primaries) for material on the same claim and make one item citing all of it; and the mechanics for adding a source to an existing item (append a dated "Source added …" paragraph to the item body; items carry no checks, so `vsect revise --dry-run` finds nothing to take in).

## The lead's row

### What I read

- **Whole:** all four 2026-08-24 files (`spike-decomposition-uniqueness-2026-08-24.md`, `-distributional-` and its `-integration-suggestions.md`, `spike-belief-splintering-genericity-2026-08-24.md`); every markdown file in `spike-epsilon-programme-2026-08-24/`; in `spike-honest-activation-2026-09-23/`, the README, `01-neighborhood-map.md`, `03-derivations.md`, the integration plan, the outsider statement, the progress log and both feedback responses; `#deriv-decomposition-uniqueness` at HEAD from the Corollary 4 block onward; the hard-ceiling verify-1 verdict section and its integration notes; the external novelty report `~/src/arch/explication/essays/scratch/guc-intro/novelty-decomposition-uniqueness.md`.
- **Sampled:** the two honest-activation feedback files (finding headings, then the response tables that dispose of each); the honest-activation `debrief.md` and `02-literature.md` (not opened); the hard-ceiling verify-1 body past §2; the 2026-05-31 hard-ceiling spike itself (only its INDEX row and verify-1's account of it).
- **Re-run first-hand:** `spike-honest-activation-2026-09-23/sims/checks.py` at `cbd2f345`, whose output is byte-identical to the committed `checks-output.txt` (ALL PASS). By hand, the arithmetic of both 8-state witnesses (the distributional spike's symmetric one and the genericity spike's perturbed one): row sums, leak cancellations per block, base-mass equality, minimality, and the quotient kernels $K_A$, $K_B$ with second eigenvalues $0.2$ and $0$. Both hold.
- **Not reached:** `.routing-trail/` contents (process archaeology, frozen by SOP §5a); the honest-activation sims beyond the re-run.

### Dispositions

**`spike-decomposition-uniqueness-2026-08-24.md` — already in canon (core), with its open remainder correctly in Working Notes.** `#deriv-decomposition-uniqueness` at HEAD carries Proposition 1, Theorem 2, Proposition 3, Corollary 4 with the equinumerosity characterization and the $m$-independent trivialization, and Corollary 5. The refuted value-subset formalization survives only as a Working Notes regression guard. `#form-complete-agent-state` carries the replacement. The spike's §6 open lines are the segment's Working Notes. Two of them have since been answered elsewhere and never brought back: the distributional analog (by its sibling, below) and the novelty search (run the same day, outside asf). New item `item:the-prior-art-search-deriv-decomposition-uniquen` (F.2) carries the novelty verdict. The verdict: no hit; three literatures anticipate the underdetermination half; the claim should be scoped to canonicity, gauge and restricted access. The spike file can move to `.integrated/` once the cluster below lands, because its Working Notes pointer and `#form-complete-agent-state:100` name its path.

**`spike-decomposition-uniqueness-distributional-2026-08-24.md` (+ suggestions), `spike-belief-splintering-genericity-2026-08-24.md`, `spike-epsilon-programme-2026-08-24/` — true, partly verified, never reached canon.** Checked at HEAD: no lumpability, Dobrushin, carving or noise-privacy content in any `src/`. These are the D.2 "Aug-24 spikes waiting". They are one landing, recorded as `item:land-the-2026-08-24-decomposition-uniqueness-clu` (G.2). Two parts of that landing replace present canon text. Epistemic Status boundary (1) says the distributional version is "neither asserted nor refuted", and Theorem D asserts it. Corollary 5 states its $\kappa$-companion gap as a single number, which the splintering results show is well defined only per maximal carving. The $\varepsilon$-programme is verified (F1–F8 plus addendum). The distributional and genericity spikes are not; only their witnesses' arithmetic is checked, by me. One piece is a separate strengthening: the $\varepsilon$-programme's sketch aimed at `#impl-orient-cascade`'s open propagated-residual bound, recorded as `item:apply-the-epsilon-programme-s-telescoping-with-c` (C.4).

**`spike-honest-activation-2026-09-23/` — true, twice verified, nothing landed.** At HEAD there is no `norm-honest-activation.md`, the OUTLINE row (`04-eli-core/OUTLINE.md:125`) still says "mathematically guarantee" and is marked missing, and every target the plan names is in its pre-spike state: the (D4) Working Note (`#def-death-as-factor-loss:91`), the severing-source axis (:57), `#deriv-tempo-additivity:94`'s undrived Discussion sentence, `#der-interaction-channel-classification:201`'s readers-ask, and `#def-model-class-fitness:73`'s hook. Recorded as:
- `item:author-norm-honest-activation-and-its-derivation` (G.2; split `--from` the twelve-stubs roll-up). It carries the normative segment, the derivation, and plan landings 3, 5, 8, 9 and 10. It also resolves the two wordings the spike leaves to Joseph, on the evidence, as this effort's standing asks.
- `item:def-death-as-factor-loss-57-says-that-for-d4-tru` (C.1). A present canon defect: the (D4) severing-source axis maps the externally driven column only to coupling pressure, but trust-channel capture reaches truth death in a Class 1 agent (verifier F2). It must land with R5's terminal form.
- `item:derive-in-closed-form-the-escape-condition-for-t` (C.4). The closed-form escape condition and a Dawid–Skene version, plus R9 and R8d's extension. The spike "released [them] to the standing cycle", which does not exist.
- `question:does-the-honest-activation-spike-s-r3-r4-undercu`. The aux reader of 2026-09-25 says R3/R4 undercut `#def-model-class-fitness`'s body detection sentence. My unverified reading is that they undercut only the Working Notes hook, because class fitness is predictive sufficiency and an honest-input class can predict a deceiver's stream perfectly.
- Source notes appended to `item:todo-communication-gain-adversarial-scope-hyp-e79c` (R3 is the representational repair that item asks for), `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` (low $U_M$ protects whatever got in first; the protective quantity is trust-model calibration), `item:todo-deaths-taxonomy-released-follow-ons-cycl-a544`, `item:todo-eli-missing-stubs-twelve-genuinely-absen-4828` and `item:disc-sandbox-evaluation-ceiling-four-defects-fro`.

  Not in INDEX. The brief is outside asf (`~/src/aisi-eoi/spikes/briefs/`), on the aisi-eoi drain's surface.

**The hard-ceiling trio (`spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md`, `-verify-1.md`, `-verify-1-integration-notes.md`) — landed today; the original spike is correctly superseded.** Checked at HEAD: `deriv-strategic-persistence-hard-ceiling.md` is gone, `#deriv-evidence-allocation-ceiling` exists (`exact`, with the integrator's re-derivation recorded in vsect), and no `src/` file carries $(1-\lambda)/(2-\lambda)$ in the old sense (the one hit, `#der-mood-timescale:23`, is the EWMA variance). The integrator's open lines are already ledgered (`question:ea1-beyond-averaging-estimators`; §5.2 noise parked in the schema's Working Notes). The integration notes' outbound flag was not ledgered: NeurIPS Paper 2's residue says a "convention decision [is] owed", which today's correction makes moot. That is now `item:neurips-paper-2-says-something-about-canon-that` (F.3). I appended a source note to `item:canon-bodies-cite-local-working-paths`: `#schema-strategy-persistence:97`, a Claim Record line, points canon at the unpublished paper. Filing: the integrator left the moves to the coordinator because `msc/inside-out-2026-10/` cites the paths. The 05-31 spike goes to `.archived/`, verify-1 and its notes to `.integrated/`.

**Today's four lanes — noted only.** `epistemic-target-ontology/` (A.1), `spike-exit-time-model-s-2026-10-30/` (C.2/C1, Part I), `spike-loop-identification-decision-state-2026-10-30/` and `spike-allocation-vs-distortion-coupling-2026-10-30/` (C.2/C2, C3, Part II, whose checker has uncommitted work in both directories as I write).

**Instruments.**
- `INDEX.md`: no rows for `spike-epsilon-programme-2026-08-24/` or `spike-honest-activation-2026-09-23/` (grep count 0 at HEAD). Several rows are stale; fork B2's file lists four. I.3 already says the index files fold into the ledger or go, so this is evidence for that KR, not a new item.
- `README.md`: current.
- `.routing-trail/`: frozen process archaeology by SOP §5a. Set aside.
- `__pycache__/`: untracked bytecode from running the root sims. Set aside; it is not in git.
