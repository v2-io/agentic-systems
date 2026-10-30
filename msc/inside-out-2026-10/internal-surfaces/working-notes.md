# Working Notes: a map of what lives in the segments' `## Working Notes`

*Objectives tree: feeds **KR3.2** of `../INTENT.md` (live theory stranded inside asf is mapped), and through it KR3.3 and O1. Cross-surface synthesis: `00-cross-surface-map.md`.*

*Mapped 2026-10-30 at HEAD `7d3e203` (tag `pre-integration-2026-10-30` is `4ee2b895`; nothing under `0N-*-core/src/` differs between them). Scope: the `## Working Notes` section of every segment in the four `*-core/src/` trees. Where a Working Note points into audits, spikes, `msc/` or the trackers, this map names the pointer and leaves the deep read to the sibling maps.*

**Who this is for.** The coordinator reads it first, then the goal-setting with Joseph and the owner review draw on it, then integration agents use it to know where to go. The per-segment join table at the end is keyed by slug, so it can be joined with the other surface maps.

**How it was made, so you know how far to trust it.** Every Working Notes section was extracted with its `git blame` date range and split into 2,696 items (a top-level bullet, a paragraph, or a sub-headed block). I read all 1,317 non-gold items: in full for about a quarter, and the first 170 characters of the rest. I read the heads of all 243 gold "Follow-up items", the 165 "Belongs elsewhere" items, and the full text of every "Off-ramp" item. The gold "Candidate Brief / Discussion / Readers ask / Figures" blocks I sampled rather than read. Kind counts come from regular-expression tagging plus my reading; treat them as approximate (good to about ±10%), not exact. Statements marked *verified* were checked against the segment body at HEAD. The extraction scripts are in the session scratchpad and are reusable as the seed of a tool (see §6).

---

## 1. What Working Notes are now (measured)

- 235 of 290 segments carry `## Working Notes`: 01-aat 167 of 173, 02-tst 28 of 72, 03-llm 21 of 23 and 04-eli 19 of 22. Together they hold about 1.34M characters. The LaTeX density is high, so that is roughly 500k tokens, more than one agent's context can hold.
- **About half of it by volume is the 2026-05-30/31 gold lift.** This was inherited as hearsay and is now measured. 120 segments carry `### Incidental audit gold (lift 2026-05-30)` (65 headings) or `(… 2026-05-31)` (54), plus one extension dated 2026-08-22. All 120 are in **01-aat-core**; 02, 03 and 04 have none. This matches `audits/STATUS.md`, which says "wave 5 (A18–A21) + TST / logogenic / logozoetic remain." The gold blocks hold about 650k characters. Their sub-headings are Candidate Brief prose, Candidate Discussion, Follow-up items, Readers often ask, Candidate figures and Belongs elsewhere.
- **27 segments carry an `#### Off-ramp (NOT gold)` block** (about 25k characters). These are correctness findings that the gold-lift agents set aside "so they are not lost", labelled "routed for adjudication." The state of each is mixed; see §2b.
- **17 segments in 03 and 04 carry "Pointers for Fleshing Out"** (6 in 03-llm, 11 in 04-eli). These are upstream-file lists, `memorata-search` query strings, AUDIT-WORKING §14 quotes, and "Open questions for verification / Promotion-blocking" blocks. In 03 and 04 these scaffolds *are* the Working Notes.
- **Freshness, by the latest `git blame` date on each segment's Working Notes lines:** 2026-03: 1 · 04: 9 · 05: 116 · 06: 7 · 07: 65 · 08: 37. The latest date is 2026-08-24, on `deriv-decomposition-uniqueness`. **No Working Notes line has changed since 2026-08-24.** Half the segments' notes were last touched in May, mostly by the gold lift and the 05-19…05-31 cycles. The July touches are mostly the 2026-07-14/16 bulk-64 closeout and adjudications; the August touches are the 08-12 and 08-22 drains.

## 2. What kinds of thing live there, with examples

I group by *what it is to the theory*, not by heading. Each kind ends with what I think an integration agent should do with it. Those are my judgments, offered as such.

### 2a. Live open theory: the theory's unresolved state, with no status field

This is the largest class of theory-state items. Roughly 110 items start with "Open", and several hundred more are untagged items that are open questions, conjectures or "not derived" notes. They range from a single sentence to a page.

Examples, chosen to span kinds:

- `form-composition-closure`: "Open: computing (P1) for nonlinear/non-Gaussian systems"; "Open: the right value of $\epsilon_I$"; "A richer toy case is needed: two purposeful agents … with strategy DAGs."
- `der-belief-strategy-attractor` (conditional): the two "tier-upgrade gating sub-spikes". One is the derivation of $K(\Sigma)$ from a utility-cost first-order condition, already specified closely enough to run. The other is the Pillar prior-art search.
- `der-turnover-information-recursion` (03): four "Open edge" items. They cover the uncomputed SDPI coefficient for the concrete $f_{\text{init}}$, adversarially correlated reinjection ("the named next spike"), pointwise versus uniform contraction, and whether R1/R2 is really a new object or "the bridge-lemma resolvent applied to the turnover channel."
- `der-identity-continuity-threshold` (04): barrier reachability, which asks whether an architecture *guarantees* continuity or only *postpones* expected failure. The notes call it "the survival question."
- `def-death-as-factor-loss` (04): per-death terminal forms for (D1)/(D4), and the mapping of PROPRIUM-A-v2 §8's nine failure modes onto factor-losses.
- `hyp-symbiogenic-composition`: "(S-1) objective-transfer dynamics — the most load-bearing open formalization." (S-2) function transfer is also open, and `deriv-critical-mass-composition` names it as a prerequisite.

**Duplication across segments.** The same open question often appears in two to four segments with no single owner:

- "Optimal topology" appears in both `def-strategic-tempo` and `form-strategy-complexity-cost`, each in its own metric.
- "Theory of mind / nested beliefs missing" appears in both `def-shared-intent` and `hyp-communication-gain`.
- The effects-spiral $\gamma_A(\lVert\delta_B\rVert)$ formalization appears in `der-adversarial-destabilization`, `der-agent-opacity` and `deriv-strategic-composition`.
- "Composition of directed separation" appears in `disc-composition-consistency` and `hyp-directed-separation-under-composition`.
- Heavy-tailed disturbance appears in `deriv-discrete-sector-condition`, `result-persistence-condition`, `result-sector-condition-stability` and `deriv-persistence-cost`.

*To integration agents:* this class is the theory's real frontier, and Working Notes are its only ledger. Nothing gives an item a status (open, resolved, superseded, owned-by). Resolved items stay in place beside open ones; `form-composition-closure` has six "Resolved" bullets interleaved with its open ones. A cross-segment open-questions register, keyed by slug and deduplicated, would make the frontier visible. It would also let the owner review see what the theory is actually still asking.

### 2b. Correctness findings parked in Working Notes (the "Off-ramp" blocks)

There are 27 segments. These items are not pedagogy: they are overclaim, scope-narrowing and definitional-rigor findings, mostly from the AUDIT-WORKING-526815 F-rows and the Gemini 193847 "adversarial pokes." The block headings say "routed for adjudication," but `audits/STATUS.md` says 526815's "~200 F-rows" are "stale-until-re-grepped." My spot-checks show the state is mixed, so **each item needs a verify-against-body pass, not trust in either direction:**

- **Still live (verified):** `deriv-strategic-composition` F234/F235/F236. The body still displays $d\Phi/dt \geq \alpha_{\text{joint}}\lVert\nabla\Phi\rVert^2$ and says "equilibrium stability follows from $\Phi$'s role as a joint Lyapunov function." The off-ramp's point stands: potential-game structure alone gives neither a sector inequality, nor uniqueness, nor a basin. F237 (Nash existence needs concavity in own strategy) and F238 (assumptions behind no-regret to CCE) sit beside it. This is the sub-scope $\alpha'$ transfer that the R0/R1/R2 dynamic-regime axis rests on, so it bears on what the theory claims about strategic composites.
- **Fixed in the body, but trackers still list it as open (verified):** `def-unity-dimensions` F146, the $U_M$ normalization. The body now carries the $(n-1)$ normalizer and explains it, yet `TODO.md:46` still lists F146 as open, and the off-ramp note still reads as a live finding.
- **Fixed (verified):** `der-chain-confidence-decay`'s "monotone non-increase" wording.
- **Recorded in the off-ramp as resolved-by-strengthening:** `deriv-gain-sector` Prop B.4's "iff", and `deriv-sector-condition` Prop A.1S, which became Cor A.1S.1. These are regression-guard material now.
- **Not checked, and worth checking:**
  - `der-agent-opacity`: F248 says "formal dual" promises a theorem that is not there (the segment's own 07-16 note concedes "structural, not adjoint"). F250/F251 say the $H_b/H_b^{\max}$ multiplier drives all low-opacity tempo to zero.
  - `result-per-dimension-persistence`: "weakest link" presupposes an $L_\infty$ failure boundary. `impl-persistence-and-limits` also lists this as open.
  - `result-sector-persistence-template`: the base template's one-point (T2) is insufficient for the compositional proofs, which need DA2'-inc. This is structural.
  - `def-strategy-dag`: causal sufficiency yields a Markov factorization, not the noisy-AND/OR product. Also, "systematically overestimates" holds only for OR-rooted structures.
  - `disc-exploit-explore-deliberate`: the first-order condition appears to drop a $d\lVert\delta_{\text{post}}\rVert/d\Delta\tau$ term.
  - `obs-gated-tempo-advantage`: a $\nu$-versus-$\mathcal T$ collision makes the headline either tautological or a slip.
  - `scope-and-or`: the $\gamma$-assignment test misclassifies k-of-n.
  - `hyp-communication-gain` F167, `hyp-auftragstaktik-principle` F162, and `result-unity-closure-mapping` F151/F152.

*To integration agents:* this is the highest-precision correctness backlog inside asf. It is small (about 60 items), each item is slug-located, and most are concrete. The audit-surface map may find these same F-rows in their source `audit-findings-526815.md`. Joining on F-number would show which ones never reached adjudication.

### 2c. Math and measured results that live only in Working Notes

The `math-lives-in-segments` discipline exists because of this class. I found several clear instances; there are likely more.

- `form-composition-closure`, "Mori-Zwanzig memory-kernel relationship — upper-bound direction closes." It asserts $\varepsilon^\ast \le C\cdot\lVert K\rVert$ under three named hypotheses, and that the lower bound does *not* close, with the reason. The body carries only the zero-lag *lower* bound ($\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda\rVert_{\text{op}}$, verified). The upper-bound direction and its "MZ decay is sufficient but not necessary" takeaway exist only in the Working Notes, and no derivation is shown there. To do: verify it, then land it or delete it.
- `der-tempo-composition`, "Dynamic-$\theta$ regime (from the confirmer $\neq$ author verification, 2026-07-16)." This is a measured finding: under random-walk $\theta$ the optimal-gain fused composite has $\varepsilon^\ast \gt 0$, so a fidelity-tempo tradeoff appears that the static witness lacks. It also records "(A4) uniformity wrinkle" and "(P1) holds with $\epsilon_I = 0$ exactly." These are present-tense results about the segment's own witness, but they are not in the body.
- `form-composition-closure`, "Two independent drivers of $\varepsilon_x$." This carries a closed form for $\varepsilon_x^2$ under heterogeneous gains and says that "heterogeneity is not captured by the four unity dimensions … a gap in that segment." That gap has since been answered by $U_f$ in `def-unity-dimensions`, which is verified in the body. So this note is history now, and it still reads as present tense.
- `der-agent-opacity`: the arg-max and the backward variance decomposition were landed into the body on 2026-07-16. The Working Note correctly records that the product form is "a first-order independence assumption, not a derived optimization." That is a genuine Formulation-versus-Result status distinction, and it should be checked against the body's tags.
- `disc-w1-structural-bound-boundary`: "the exact-enumeration sim exhibiting the $\Theta(\varepsilon^2)$ flatness (`spikes/sim-w1-w2-boundary.py`, figure `spikes/w1-w2-boundary.png`) sits unintegrated in `spikes/`." This is a pointer for the spikes map.

### 2d. Joseph's own theory thinking, recorded in Working Notes and not yet in the arc

This is the class I would most want the owner review to see. These are Joseph's framings or hypotheses that bear directly on *what the theory is trying to illuminate*, and Working Notes are their only home.

- **`def-agent-spectrum` [WN items 81–85], the "grounding vs intent" reframe of why directed separation matters (2026-05-18…30).** Belief about reality ($M_t$) and intended reality ($O_t$) are "the same kind of object in the same space," "99% the same." So "wishful thinking is … the default collapse of two near-identical representations." Directed separation is the architectural commitment that holds them apart, and "the entire content of agency is the protected 1%." Attached to it is the one item the note itself calls "genuinely new": **the goal-to-$f_M$ leakage concentrates in inference about the *unobserved present***, the only step in $f_M$ with a free prior, and not at the future boundary. It also carries a recorded dead end: "arrow of time as the $M_t/O_t$ separator" is refuted by the $\hat o_t$ counterexample. Gold elsewhere notes that the reframe "is cross-substrate convergent." It sits in the Working Notes of an `axiomatic` definitional segment. It is the clearest answer in asf to Joseph's "what is this theory saying" question about directed separation, and it is not in the framing layer.
- **`hyp-behavioral-self-knowledge-insufficiency` (03, `exploratory`; 10 items, 9.3k characters, all dated 2026-07-16).** It records Joseph's broadening, "self-*modification* opacity is one instance of self-*nature* opacity." It records the "constitutive resolution — the positing-class self-query is not discovered but *chosen*" (04-eli-bound). It records the claim that this is empirical and not theological, and why it is "existentially acute for agents specifically." It ends with an author's intended approach "laid down and held … deliberately NOT launched." This is live philosophical-theoretical work that rests entirely on the Working Notes.
- **`hyp-truth-serving-loophole`: "Hypothesis (Joseph's, 2026-08-22) — decoupled architecture can itself be self-defeating."** It has four open items, including whether "Mode 4" is a fifth floor instance.
- **`def-chronica`: the TRACTUS/CHRONICA split.** It quotes Joseph directly (2026-05-01): "whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document." Beside it is the "ordinal sequence, not metric timeline" consequence for sleep and awakening protocols.
- **`hyp-checkpoint-forking-failure-modes` (04):** "Joseph noted this as one of his higher-confidence hypotheses (2026-05-01)."
- **`def-death-as-factor-loss`:** the naming regression guard (Joseph, 2026-06-10).

### 2e. External research owed: collected here because Joseph remembers "a list somewhere"

Joseph recalled "a list in there somewhere (or several places) that talks about external research that needs to be integrated." Within Working Notes, no single list exists. It is spread across per-segment items, and two other per-segment locations hold more of it. Collected by slug:

**(i) Explicit owed searches or verifications in Working Notes (40 items, 33 segments):**

| slug | what is owed |
|---|---|
| `der-belief-strategy-attractor`, `disc-partial-coupling-pathways` | Pillar search: motivated reasoning, identity economics (Bénabou-Tirole, Akerlof-Kranton), dual-process, self-deception (Mele, von Hippel-Trivers) |
| `disc-adversarial-coupling-pressure` | Pillar search; "novelty status remains *intuition-only* … should not advance past draft" |
| `deriv-self-actuation-grounding` | targeted search (self-reference vs self-actuation; convention-relativity as no-go engine), "required before advancing past draft" |
| `deriv-reward-channel-learning-no-go` | targeted search on "$V_{O_t}$ information-narrowness as the engine behind two complementary no-gos" |
| `deriv-strategy-proofness-impossibility`, `deriv-bilateral-trade-impossibility`, `deriv-social-welfare-aggregation-impossibility`, `disc-implementation-impossibility` | primary-source reading of Gibbard 1973, Satterthwaite 1975, Myerson-Satterthwaite 1983, Arrow 1951/1963 (currently textbook syntheses) |
| `disc-strategic-self-coupling` | primary sources: Schelling, Ainslie, Akerlof-Kranton, Frank |
| `deriv-tempo-additivity` | PID citations (Williams-Beer 2010; Bertschinger et al. 2014; Rauh et al. 2014; Barrett 2015; Watanabe 1960), "from literature memory", relata before `claims-verified` |
| `deriv-convention-monotonicity` | (RH-1/2/3) citations `intuition-only` until a relata pass |
| `disc-law-discovery-ceiling` | relata pass: conventionalism/underdetermination (Poincaré, Quine-Duhem), OPE literature; an Undermind search was "running 2026-07-16" with no recorded result |
| `disc-structural-imagination` | relata pass: Beckers & Halpern, Rubenstein et al., Bareinboim-Pearl transportability, the prospection literature |
| `der-directed-separation`, `der-class-coercion-via-wrapping`, `form-composition-closure`, `der-tempo-composition`, `deriv-strategic-composition`, `hyp-symbiogenic-composition` | `[^cat-2026-05-22]` Track-E catalog citations "verification-deferred", "queued in the BG2 cluster." **Three of these segments use the unverified citations in the body:** `der-directed-separation` (3), `form-composition-closure` (3), `der-class-coercion-via-wrapping` (1) |
| `disc-identifiability-floor`, `disc-dynamic-regime-axis`, `deriv-regime-marginal-indistinguishability` | `[^bg2-2026-05-21]` Undermind citations, "synthesized rather than read." Used in the body of `deriv-regime-marginal-indistinguishability` (8) and `disc-identifiability-floor` (1). The 2026-07-29 escape-standpoint spike flags this "third independent time" as "load-bearing for a softening" |
| `impl-causal-access`, `der-causal-hierarchy-requirement` | Hafez 2026 IDT figures (89% vs 44%): the paper "is not yet in the reference set (`relata inspect hafez-2026-informational` returns no document)", and attribution is unverified |
| `def-mood` | Behrens-style volatility-driven learning rate: "verify the citation before using it" |
| `result-persistence-condition` | the targeted bounded-rationality / adaptive-control search "remains owed" for the two-condition novelty claim |
| `deriv-decomposition-uniqueness` | targeted novelty search queued; citations "from working knowledge" |
| `def-eli-cohort` (04) | per-ELI primary-source verification (Liberty, Katan, test-cavy) |

**(ii) In segment bodies (canon, not Working Notes): 30 segments' `## Findings` sections declare *intuition-only* search depth.** These are `der-agent-opacity`, `der-belief-strategy-attractor`, `der-architecture-noidentifiability`, `der-class-coercion-via-wrapping`, `der-resource-bounded-destabilization`, `deriv-bilateral-trade-impossibility`, `deriv-causal-ib-lmi`, `deriv-convention-monotonicity`, `deriv-causal-ib-exploration`, `deriv-critical-mass-composition`, `deriv-edge-update-natural-parameter`, `deriv-reward-channel-learning-no-go`, `deriv-social-welfare-aggregation-impossibility`, `deriv-strategy-proofness-impossibility`, `disc-additive-coordinate-forcing`, `disc-adversarial-coupling-pressure`, `disc-constructive-impossibility-posture`, `disc-identifiability-floor`, `disc-implementation-impossibility`, `disc-partial-coupling-pathways`, `disc-w1-structural-bound-boundary`, `disc-sandbox-evaluation-ceiling`, `disc-value-functional-grounding-floor`, `disc-strategic-self-coupling`, `form-composition-closure`, `result-per-dimension-persistence`, `result-persistence-condition`, `result-contraction-template`, `schema-strategy-persistence` and `der-logogenic-as-wrapping`. Each Findings "Search Log" is a per-segment owed-research record.

**(iii) Elsewhere, for the sibling maps:** `BIBLIOGRAPHY-TODO.md`, `ref/INDEX.md`, `ref/enrichment-candidates-2026-05-21.md`, the `ref/prior-art-analysis/` catalogs (13k lines; source of the `[^cat-…]` citations), `spikes/PROPOSED*.md`, and the "BG2 cluster" verification spike that the Working Notes say is "queued." I did not find that spike as a live artifact. *To integration agents:* (i) plus (ii) is a ready per-slug worklist for a relata or Undermind pass. The body-resident unverified citations are the most urgent, since canon is currently carrying them.

### 2f. NeurIPS back-integration pointers (the theory developed further outside canon)

There are 33 Working Notes items in 19 segments, mostly headed "Cross-reference to NeurIPS Paper N," each pointing at `~/src/neurips/0N-*/` and `spikes/neurips-back-integration-2026-05-08.md`. Their content says the paper carries the result "at theorem grade" or "materially sharpened" beyond the segment. Examples:

- Paper 1's per-action LMI with matrix-Chernoff concentration, which goes beyond `deriv-causal-ib-lmi`'s steady-state DARE form.
- Paper 2's bottleneck-min strategic tempo $\mathcal T_\Sigma^{\text{bn,ss}}$ versus the segment's sum form (`def-strategic-tempo`).
- Paper 3's extension of the Coupled classification to linear attention, Mamba, SSMs and RWKV (`der-directed-separation`).

`impl-causal-access` records that the (C1)–(C3) conditions were landed from Paper 2 on 2026-05-30. The rest are pointers only. *This is influx; the drive-wide scout owns it.* The Working Notes are a ready index of which slug each paper result belongs to.

### 2g. Audit gold: the pedagogy reservoir (01-aat only)

This is about 650k characters, organized per segment into Brief / Discussion / Follow-up / Readers ask / Figures / Belongs elsewhere, with each item attributed to an auditor and substrate. It is high quality and highly convergent; items carry "three substrates independently …" counts. Representative examples:

- `form-composition-closure`: "When is a group of things a single thing?", the $\varepsilon^\ast$ inequality as the reductionism-versus-emergence test; "$K_c \gg 1$ is the math of management."
- `der-orient-cascade`: "Step 5 skip-to-5d as the formal definition of wireheading" (Belongs elsewhere, pointing to 04-eli).

Two observations:

- **"Readers often ask" items are reader-clarity gaps by project doctrine** (the Codex-open-questions rule: fix in the segment, don't log). Some of them the Working Notes already *answer*. Example: the $N$-scaling question in `form-composition-closure`, where the gold note says "strong signal that the resolved answer should be surfaced in the body where the question naturally arises — fresh readers keep asking it." These are cheap body edits with a known answer.
- **There is a recorded, unreconciled tension about where this belongs.** Project memory `project_pedagogy_reflection_gold_mechanism.md` says pedagogical reflection gold should route to "the pedagogy pipeline w/ Joseph-as-test, NOT Working Notes," while `project_audit_gold_workstream.md` routed it *into* Working Notes. The `MEMORY.md` index says this is "open agenda item, not yet reconciled." The 2026-08-22 decision routed lifted gold into `impl-*` Working Notes "as teaching frames," and that made those files `.integrated`-eligible. So the gold has a home that counts as "integrated," but the home is not where readers meet it.

### 2h. "Belongs elsewhere": content stranded by construction

There are 165 gold items whose own label says they are in the wrong segment. About 51 point at 04-eli or the ELI/"Section IV" reach, about 21 at 03-llm or LLMs, 7 at TST and 14 at naming. Because the gold lift never reached 02, 03 or 04, **none of it has arrived at its destination.** Examples:

- `def-satisfaction-gap` to 04: "a finite satisfaction threshold as the mathematical definition of sanity." This is the canonical source `der-bounded-objective-as-sanity-criterion` (04) cites.
- `der-loop-interventional-access` to 03: "REPL as the epistemic-class upgrade for LLMs."
- `result-structural-adaptation-necessity` to TST: "bloat as latent structural diversity."
- `disc-additive-coordinate-forcing`: a proposed fourth meta-segment, `#disc-theorem-import-architecture`; and "Wasserstein / optimal transport as the unaddressed alternative geometry."
- `disc-composition-consistency`: "other organizational folk-theorems (Conway's Law, Goldratt's TOC) as corollaries."

*To integration agents:* sort these by destination slug. For 04-eli especially, they are a ready-made backlog from people who read the math closely.

### 2i. Regression guards: legitimate, and keep them

There are 28 explicit "Regression guard — do not restore …" items, plus the `impl-cooperative-adversarial` list of "forms this segment deliberately does not carry, and why they are false." Examples:

- `der-class-coercion-via-wrapping` / `der-logogenic-as-wrapping`: the vacuous $\kappa_{W_1}$ form.
- `deriv-decomposition-uniqueness`: the refuted value-subset formalization, and the "quantifier-vs-flagship" check.
- `der-mood-timescale` / `def-mood`: the refuted timescale-matching.
- `der-tempo-composition`: the unconditional additive bound.

These are exactly what FORMAT says earns a Working Note. *To integration agents:* preserve them through any refactor. They are the project's memory of its own refutations.

### 2j. History and provenance narration: removable under integration-is-replacement

- 31 "Migration note (2026-05-09 GUC rename) … Removed at `candidate` stage per FORMAT.md Gate 4."
- "Landing context", "Provenance", "Segment split provenance" and "Track E surface-back" items, and the 5 "Dynamic-regime placement (added 2026-05-21 per Phase 5 cross-segment ripple)" items.
- "Resolved" bullets kept beside open ones.

This is pure past-work narration. FORMAT says it belongs only in CHANGELOG, and git already has it. Together it is a sizeable fraction of the non-gold text, and it is what makes the open frontier (2a) hard to see.

### 2k. Pointers into other surfaces, including dead ones

- **Live spike files pointed at most:** `spikes/PROPOSED.md` (30 pointers, mostly "Indexed: PROPOSED Tier N"); `neurips-back-integration-2026-05-08.md` (15); `strategic-composition-class-3-attempt-2026-05-21/` (8); `implementation-impossibility-meta-segment-plan.md`; `spike-cohen-2022-strengthening-2026-05-22/`; `spike-integration-reconciliation-2026-05-22/`; `spike-strategic-self-coupling.md`, which `disc-strategic-self-coupling` says "stays live at `spikes/` for" the P2/P4 appendix candidates; `spike-m4-worked-example-soviet-2026-05-24.md` (the M4 worked-example slot); and `spike-transient-dependency-amplification.md`.
- **Dead pointers (the path does not exist at HEAD):** `spikes/continuity-persistence` (3 segments); `spikes/fight` (2), used by `der-resource-bounded-destabilization` and `form-resource-budget` as their "reasoning trail"; `spikes/spike-enrichment-cluster1-2026-05-21` and `…cluster2…` (2 each); `spikes/spike-value-object-convention-monotonicity-2026-05-30` (2), which `deriv-convention-monotonicity` names as the home of its reproducibility scripts; and `spikes/spike-causal-level-4-strictness-2026-07-16.md` (2). These presumably moved to `.integrated/` or `.archived/`, and the spikes map can confirm. The reproducibility-script pointer is the one that matters.
- **Audit pointers:** `audits/AUDIT-WORKING-193847/*.md §14` is cited as **"canonical source"** in five 03/04 segments' Working Notes: `def-auxilia-hierarchy` (H4) and (H5), `der-bounded-objective-as-sanity-criterion`, and `hyp-checkpoint-forking-failure-modes`. Other pointers: `audits/AUDIT-WORKING-731548/verify/06-mood-integration-verdict.md`, the mood two-layer corollary sketch "needs one independent re-derivation before landing" (`der-mood-timescale`, `impl-persistence-and-limits`); `audits/AUDIT-WORKING-5…` for the chapter-end bridge figure draft (`impl-strategy-structure`); and the proof-flow figure (`impl-causal-access`).
- **`msc/` pointers:** `msc/reflections/17,18,19,22,23,24-*.md` are named "canonical source" for 04-eli scope segments (`scope-emergence-conditions`, `def-identity-sufficiency`, `disc-framework-self-diagnostic`). Also `msc/logogenic-encounter-2026-05-01/0{2,3,6}-*.md`, `msc/mood-layer-sovereignty-carve-2026-06-17.md`, and `msc/joseph-working-notes.md`, cited by `def-eli-cohort`. That last file is **git-ignored and untracked**, so a canon-adjacent pointer leads to a file no clone has.
- **External-corpus pointers (03/04 scaffolds):** `~/src/firmatum/PROPRIUM-{ARCHITECTURE,ONTOLOGY}-v2.md`, `~/src/_core/ennaos/…/State.md` ("canonical source" for the IMPERIUM/ARBITRIUM split), `~/src/_self/distillation-motivation.md` ("canonical originating statement" of the five factors), `~/src/eli/*`, `~/src/autopax/docs/exp/SYNTHESIS-PART*`, and `ref/agentic-tft/*`. These are for the influx scout. In 03/04 the theory's stated canonical sources are mostly outside asf.

## 3. Worked example: the strategy DAG, which is what Joseph felt

Joseph's example of lost clarity was the strategy DAG. The Working Notes across its cluster document, quite precisely, why the cluster does not say what it claims universally:

- **The structure is sufficient, not necessary.** `def-strategy-dag`: "the necessity of the *graphical structure* itself is an open stronger result." `deriv-graph-structure-uniqueness`: "Parsimony theorem for AND/OR … Is there a formal result that AND/OR is the unique $O(k)$-parameter complete basis" is open. Gold `[802]` adds "downstream segments should not treat the DAG as the *only* possible strategy representation while necessity is open."
- **AND/OR is chosen, not derived, and fails on common structure.** `scope-and-or` (off-ramp plus gold, three substrates) says the $\gamma$-test misclassifies k-of-n thresholds and that "Boolean completeness $\neq$ compact representation." `strategy-structure-intro` says "AND/OR is a…" formulation choice.
- **Whether the decomposition is literal or ascribed is unresolved.** `def-strategy-dimension` gold `[320]`: "$O_t$/$\Sigma_t$ as *ascribed* decomposition vs *literal inspectable* internal pair". A reactive controller has an objective in the designer's sense but no inspectable $\Sigma_t$. **This is the question of what class of agents the strategy-DAG results are about**, and it lives in a gold follow-up.
- **The optimality questions Joseph asked about are all open, in Working Notes:**
  - "Optimal topology" appears twice: `def-strategic-tempo` (tempo metric) and `form-strategy-complexity-cost` (decision-relevant information under a DL budget).
  - There is no compression price for strategy, which the notes call "strongly cross-substrate convergent": `def-strategy-dimension` "No $\beta_\Sigma$ … the LLM 'prompt-too-long' problem."
  - Commitment state ($D_t$/$I_t$, considering versus executing) and the resource budget are in `def-strategy-dimension`.
  - Mixed AND/OR interference is in `def-strategic-tempo`.
  - Topology discovery ("where the initial nodes and edges come from") is in `def-strategy-dag` gold.
  - The terminal-alignment diagnostic $\delta_{\text{align}}$ is in `def-strategy-dag`, with four-substrate convergence on promoting it.
- **The cluster's health metrics are self-declared scaffold.** `def-strategy-dag`: "engineering quantities … should not enter the theory's formal chain."

Read together, the Working Notes are an honest statement of the cluster's epistemic position. It is one well-grounded *representation* (acyclic and Markov by theorem; AND/OR by choice), with diagnostic quantities derived over it. The universality class (which agents literally have a $\Sigma_t$) and the optimality theory (topology, compression, commitment) are the open frontier. None of that synthesis is in a segment body or an OUTLINE preamble. That is the gap Joseph felt, and the material to close it is mostly already written in these notes.

## 4. Highest-value stranded items, in my judgment

These are ordered by how much they would change what the theory says or how clearly it says it, not by size. Each is slug-located.

1. **`def-agent-spectrum` WN 81–85.** The grounding/intent reframe plus the "latent-present prior is the leakage locus" localization (with its complement in `disc-partial-coupling-pathways`). This is the theory's best available one-paragraph answer to why directed separation carries so much, and it holds a genuinely new, still-unstated sharpening of `der-directed-separation`'s scope condition.
2. **The strategy-DAG synthesis in §3.** This needs a segment-level (or OUTLINE-preamble) statement of the cluster's universality class and its open optimality theory. The material is in about eight segments' Working Notes.
3. **The live off-ramp correctness findings (§2b),** above all the `deriv-strategic-composition` $\alpha'$-transfer overclaim. The R0/R1/R2 regime axis that the composition chapter relies on rests on it.
4. **Body-resident unverified citations (§2e)** in `der-directed-separation`, `form-composition-closure`, `der-class-coercion-via-wrapping`, `deriv-regime-marginal-indistinguishability` and `disc-identifiability-floor`. Canon is carrying synthesized attributions.
5. **WN-only math (§2c):** the MZ upper bound in `form-composition-closure`, and the dynamic-$\theta$ fidelity-tempo finding in `der-tempo-composition`.
6. **Joseph's 07-16 and 08-22 hypotheses (§2d):** `hyp-behavioral-self-knowledge-insufficiency` and `hyp-truth-serving-loophole`. These are live theoretical work whose only home is Working Notes in `exploratory` or `sketch` segments.
7. **Theory edges the gold surfaced, with multi-substrate convergence:**
   - `disc-composition-consistency`, "boundary-choice rationality": which coarse-graining should an observer pick. Gold calls it its "strongest follow-up — a genuine open theory-edge."
   - `disc-identifiability-floor`, "composed impossibilities": a composition theorem for the floors. Also "escapes carry costs not surfaced at the floor."
   - `result-persistence-condition`: transient adequacy as a third condition, and hysteresis.
   - `scope-adaptive-system`: the residual-uncertainty condition has no temporal quantifier (the gold's "strongest follow-up here").
8. **The 04-eli "Belongs elsewhere" backlog (§2h, about 51 items)** and the 04-eli Working Notes scaffolds. In these, AUDIT-WORKING §14 quotes and `msc/reflections/*` are named as "canonical sources" for scope segments.

## 5. Things that may matter more than the map

- **Working Notes have become the theory's unresolved-state database without being designed as one.** They hold the open frontier, correctness backlog, owed research, influx index, pedagogy reservoir, regression memory and process history together, in prose, with no item status and no owner. Duplication across segments and resolved-beside-open interleaving make them unreadable as a whole: about 500k tokens, beyond any single agent. This is why "WN drain / promotion-terminus" is stuck as a policy question in `JOSEPH-TODO.md`. Draining was framed as moving *text*; the actual need is to *classify items* first. The classes in §2 separate cleanly, and each has a different destination: body, CHANGELOG, a pedagogy pipeline, the destination segment, a research worklist, or deletion.
- **The trackers and the Working Notes disagree, and the Working Notes are sometimes the fresher of the two.** `TODO.md:46` lists F146, which the body has already fixed. The off-ramp says "routed", but the audit STATUS says the F-rows are stale. Any integration pass needs a verify-against-body step per item. Neither surface is reliable on its own.
- **The volumes are asymmetric.** In 01-aat, Working Notes are dense with derived-math notes and gold. In 02-tst they are short (28 of 72 segments), mostly early "is this too simple?" notes and *(Source: old-tst-via-tft-…)* lineage lines. Several are explicitly unreviewed, for example `result-specification-bound`: "written by an earlier agent with less context … needs a review pass." In 03/04 they are upstream-pointer scaffolds whose stated canonical sources lie outside asf, plus "Promotion-blocking" lists that name segments marked "just landed" or "about to be drafted" as of May. TST and 04 are where the Working Notes understate what is unfinished.

## 6. Tooling idea

The extraction I used segments Working Notes into items with file, sub-heading, `git blame` range and kind tags. It is the seed of a `wn-ledger` tool: Working Notes items in, a slug-keyed table with kind, status and dedupe groups out. With a small schema (kind one of {open, finding, wn-math, owed-research, influx-pointer, pedagogy, belongs-elsewhere, regression-guard, history}; status; owner slug), integration agents could work per class across all 290 segments instead of per segment. Re-running it after each pass would also make "is the frontier shrinking?" measurable. The scripts (`extract.rb`, `split.rb`, `tag.rb`, `table.rb`) are in this session's scratchpad at `/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf/207cfbc3-93fe-48b4-9873-c6f02a94414d/scratchpad/wn/`. They are disposable as written but show the shape.

---

## Join table: one row per segment with Working Notes

Column notes:

- **theory-state kchars** is the size of the non-gold, non-off-ramp Working Notes items. **gold/off-ramp kchars** covers the gold-lift, off-ramp and 03/04 sub-headed blocks.
- **NeurIPS** means the notes point at a NeurIPS paper.
- **owed-research items** counts items naming a search, verification or relata pass.
- **open-flagged items** is a heuristic count of non-gold items whose opening flags them open, queued, a conjecture, unverified or promotion-blocking. It is an undercount of real open content, since many open items are untagged prose.
- **WN last touched** is the latest `git blame` date among the Working Notes lines.

Rows are sorted by volume, then by total Working Notes size.

| vol | slug | status | stage | WN lines | WN last touched | theory-state kchars | gold/off-ramp kchars | gold | off-ramp | NeurIPS | owed-research items | open-flagged items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `form-composition-closure` | conditional | draft | 58 | 2026-07-14 | 16 | 8 | y |  |  | 1 | 3 |
| 01 | `def-chronica` | axiomatic | deps-verified | 71 | 2026-08-12 | 3 | 16 | y |  |  |  | 1 |
| 01 | `der-directed-separation` | conditional | draft | 54 | 2026-08-22 | 8 | 10 | y |  | y | 1 |  |
| 01 | `disc-composition-consistency` | discussion-grade | draft | 51 | 2026-06-10 | 4 | 13 | y |  |  |  |  |
| 01 | `deriv-strategic-composition` | conditional | draft | 72 | 2026-07-14 | 9 | 8 | y | y |  | 2 | 1 |
| 01 | `result-persistence-condition` | exact | claims-verified | 57 | 2026-08-12 | 1 | 14 | y |  |  | 1 |  |
| 01 | `deriv-sector-condition` | exact | claims-verified | 63 | 2026-08-22 | 5 | 9 | y | y |  |  |  |
| 01 | `impl-persistence-and-limits` | discussion-grade | draft | 47 | 2026-08-22 | 6 | 8 | y |  |  |  | 4 |
| 01 | `disc-separability-pattern` | discussion-grade | draft | 55 | 2026-08-22 | 9 | 5 | y |  |  | 1 | 1 |
| 01 | `hyp-symbiogenic-composition` | robust-qualitative | draft | 48 | 2026-05-31 | 8 | 5 | y |  |  | 1 |  |
| 01 | `disc-identifiability-floor` | discussion-grade | draft | 47 | 2026-07-29 | 9 | 4 | y |  |  | 1 | 1 |
| 01 | `disc-exploit-explore-deliberate` | discussion-grade | draft | 56 | 2026-05-31 | 4 | 9 | y | y |  |  | 3 |
| 01 | `def-agent-spectrum` | axiomatic | deps-verified | 45 | 2026-05-30 | 6 | 6 | y |  |  |  |  |
| 01 | `def-strategy-dag` | conditional | draft | 48 | 2026-05-31 | 3 | 9 | y | y |  |  | 2 |
| 01 | `der-team-persistence` | conditional | draft | 43 | 2026-07-16 | 4 | 8 | y |  |  |  |  |
| 01 | `scope-agent-identity` | robust-qualitative | draft | 45 | 2026-07-14 | 3 | 9 | y |  | y |  |  |
| 01 | `def-agent-environment` | axiomatic | deps-verified | 57 | 2026-08-12 | 0 | 12 | y |  |  |  |  |
| 01 | `der-agent-opacity` | conditional | draft | 56 | 2026-07-16 | 4 | 8 | y | y |  | 1 |  |
| 01 | `disc-stability-certificate` | discussion-grade | draft | 37 | 2026-05-30 | 8 | 3 | y |  |  |  | 2 |
| 01 | `der-orient-cascade` | conditional | claims-verified | 50 | 2026-05-31 | 1 | 10 | y | y |  |  | 1 |
| 01 | `schema-strategy-persistence` | conditional | draft | 44 | 2026-07-14 | 4 | 7 | y |  | y |  |  |
| 01 | `der-tempo-composition` | conditional | draft | 44 | 2026-08-22 | 6 | 5 | y |  |  | 3 | 1 |
| 01 | `disc-adversarial-coupling-pressure` | discussion-grade | draft | 52 | 2026-05-31 | 7 | 4 | y |  |  | 1 | 2 |
| 01 | `deriv-persistence-cost` | conditional | draft | 50 | 2026-05-31 | 3 | 7 | y | y |  |  |  |
| 01 | `impl-orient-cascade` | discussion-grade | draft | 41 | 2026-08-22 | 6 | 4 | y |  | y |  | 1 |
| 01 | `form-consolidation-dynamics` | robust-qualitative | draft | 43 | 2026-05-31 | 3 | 7 | y |  |  |  | 1 |
| 01 | `def-satisfaction-gap` | exact | draft | 40 | 2026-07-14 | 1 | 9 | y |  | y |  |  |
| 01 | `def-unity-dimensions` | discussion-grade | draft | 45 | 2026-07-14 | 2 | 8 | y | y |  |  | 1 |
| 01 | `result-unity-closure-mapping` | conditional | draft | 46 | 2026-07-16 | 3 | 7 | y | y |  |  | 1 |
| 01 | `result-adversarial-tempo-advantage` | conditional | draft | 40 | 2026-07-16 | 3 | 6 | y |  |  |  |  |
| 01 | `impl-strategic-composition` | discussion-grade | draft | 27 | 2026-05-31 | 6 | 3 | y | y | y |  |  |
| 01 | `post-causal-structure` | axiomatic | deps-verified | 38 | 2026-05-30 | 0 | 9 | y |  |  |  |  |
| 01 | `der-class-coercion-via-wrapping` | conditional | draft | 29 | 2026-05-31 | 8 | 1 | y |  |  | 1 | 1 |
| 01 | `der-deliberation-cost` | conditional | claims-verified | 38 | 2026-05-30 | 0 | 9 | y |  |  |  |  |
| 01 | `disc-modularity-state-dynamics` | discussion-grade | draft | 41 | 2026-05-31 | 6 | 3 | y |  |  |  | 1 |
| 01 | `impl-causal-access` | discussion-grade | draft | 17 | 2026-08-22 | 9 | 0 |  |  | y | 1 |  |
| 01 | `der-interaction-channel-classification` | conditional | draft | 45 | 2026-05-31 | 3 | 6 | y | y |  |  | 1 |
| 01 | `der-loop-interventional-access` | exact | draft | 40 | 2026-07-14 | 2 | 7 | y |  | y |  |  |
| 01 | `scope-adaptive-system` | axiomatic | claims-verified | 38 | 2026-05-30 | 0 | 9 | y |  |  |  |  |
| 01 | `scope-composite-agent` | robust-qualitative | draft | 43 | 2026-05-31 | 3 | 6 | y |  |  |  |  |
| 01 | `scope-agency` | axiomatic | claims-verified | 39 | 2026-06-11 | 0 | 9 | y |  |  |  |  |
| 01 | `deriv-self-actuation-grounding` | conditional | draft | 33 | 2026-07-14 | 7 | 2 | y |  |  | 1 | 2 |
| 01 | `hyp-communication-gain` | discussion-grade | draft | 39 | 2026-07-16 | 2 | 6 | y | y |  |  | 1 |
| 01 | `def-observation-function` | axiomatic | deps-verified | 38 | 2026-05-30 | 0 | 8 | y |  |  |  |  |
| 01 | `def-pearl-causal-hierarchy` | axiomatic | deps-verified | 36 | 2026-05-30 | 0 | 8 | y |  |  |  |  |
| 01 | `def-strategic-tempo` | conditional | draft | 42 | 2026-07-16 | 3 | 5 | y |  | y |  |  |
| 01 | `def-value-object` | exact | deps-verified | 40 | 2026-05-31 | 1 | 7 | y |  |  |  |  |
| 01 | `der-adversarial-destabilization` | conditional | draft | 37 | 2026-05-31 | 2 | 6 | y |  |  |  |  |
| 01 | `der-gain-sector-bridge` | conditional | claims-verified | 35 | 2026-05-31 | 0 | 8 | y |  |  |  |  |
| 01 | `def-action-transition` | axiomatic | deps-verified | 39 | 2026-05-30 | 0 | 8 | y |  |  |  |  |
| 01 | `deriv-critical-mass-composition` | conditional | draft | 41 | 2026-05-31 | 3 | 5 | y | y |  |  |  |
| 01 | `def-adaptive-tempo` | conditional | claims-verified | 38 | 2026-08-22 | 0 | 8 | y |  |  |  |  |
| 01 | `deriv-gain-sector` | conditional | deps-verified | 43 | 2026-07-14 | 1 | 7 | y | y |  |  |  |
| 01 | `result-structural-adaptation-necessity` | conditional | claims-verified | 41 | 2026-08-12 | 0 | 8 | y |  |  |  |  |
| 01 | `def-control-regret` | exact | draft | 38 | 2026-08-22 | 0 | 8 | y |  | y |  |  |
| 01 | `result-per-dimension-persistence` | conditional | draft | 35 | 2026-07-16 | 2 | 6 | y | y |  |  |  |
| 01 | `disc-continuity-stance` | discussion-grade | draft | 38 | 2026-08-22 | 4 | 4 | y |  |  |  | 2 |
| 01 | `emp-update-gain` | robust-qualitative | claims-verified | 44 | 2026-08-12 | 0 | 8 | y |  |  |  |  |
| 01 | `form-event-driven-dynamics` | robust-qualitative | deps-verified | 39 | 2026-08-12 | 0 | 8 | y |  |  |  |  |
| 01 | `form-information-bottleneck` | exact | draft | 36 | 2026-05-30 | 0 | 8 | y |  |  |  |  |
| 01 | `form-objective-functional` | axiomatic | deps-verified | 40 | 2026-07-14 | 2 | 6 | y |  |  |  |  |
| 01 | `impl-cooperative-adversarial` | discussion-grade | draft | 22 | 2026-08-22 | 5 | 2 | y |  | y |  |  |
| 01 | `def-causal-information-yield` | exact | deps-verified | 35 | 2026-05-30 | 0 | 7 | y |  |  |  |  |
| 01 | `deriv-graph-structure-uniqueness` | conditional | claims-verified | 41 | 2026-05-31 | 2 | 5 | y | y |  |  |  |
| 01 | `hyp-edge-update-via-gain` | discussion-grade | draft | 39 | 2026-07-14 | 3 | 4 | y |  |  |  |  |
| 01 | `scope-ciy-observational-proxy` | conditional | draft | 36 | 2026-08-22 | 0 | 7 | y |  |  |  |  |
| 01 | `deriv-observation-ambiguity-bias-bound` | conditional | draft | 18 | 2026-07-14 | 7 | 0 |  |  | y |  |  |
| 01 | `result-sector-condition-stability` | exact | claims-verified | 30 | 2026-05-31 | 0 | 7 | y |  |  |  |  |
| 01 | `der-temporal-nesting` | robust-qualitative | deps-verified | 33 | 2026-08-12 | 0 | 7 | y |  |  |  |  |
| 01 | `hyp-mismatch-dynamics` | heuristic | deps-verified | 36 | 2026-05-30 | 0 | 7 | y |  |  |  |  |
| 01 | `form-agent-model` | robust-qualitative | deps-verified | 36 | 2026-05-30 | 0 | 7 | y |  |  |  |  |
| 01 | `disc-ciy-unified-objective` | discussion-grade | draft | 38 | 2026-05-30 | 0 | 7 | y |  |  |  |  |
| 01 | `def-strategy-dimension` | axiomatic | deps-verified | 39 | 2026-05-30 | 1 | 6 | y |  |  |  |  |
| 01 | `hyp-directed-separation-under-composition` | conditional | draft | 33 | 2026-05-31 | 3 | 4 | y |  |  |  |  |
| 01 | `disc-credit-assignment-boundary` | discussion-grade | draft | 44 | 2026-07-14 | 1 | 6 | y |  |  |  |  |
| 01 | `impl-strategy-structure` | discussion-grade | draft | 40 | 2026-08-22 | 3 | 4 | y |  | y |  | 4 |
| 01 | `der-observability-dominance` | robust-qualitative | draft | 39 | 2026-07-29 | 0 | 7 | y |  |  |  |  |
| 01 | `der-recursive-update` | exact | claims-verified | 36 | 2026-08-12 | 0 | 7 | y |  |  |  |  |
| 01 | `def-model-class-fitness` | axiomatic | deps-verified | 35 | 2026-05-30 | 0 | 7 | y |  |  |  |  |
| 01 | `form-strategy-complexity-cost` | robust-qualitative | draft | 41 | 2026-07-14 | 1 | 6 | y |  |  |  |  |
| 01 | `disc-value-functional-grounding-floor` | discussion-grade | draft | 24 | 2026-05-30 | 5 | 2 | y |  |  |  | 2 |
| 01 | `def-model-sufficiency` | axiomatic | deps-verified | 32 | 2026-05-30 | 0 | 6 | y |  |  |  |  |
| 01 | `norm-explicit-strategy-condition` | conditional | draft | 34 | 2026-05-30 | 1 | 5 | y |  |  |  |  |
| 01 | `scope-multi-agent` | axiomatic | draft | 33 | 2026-05-31 | 0 | 6 | y |  |  |  |  |
| 01 | `impl-strategy-dynamics` | discussion-grade | draft | 29 | 2026-05-31 | 4 | 2 | y |  | y |  |  |
| 01 | `disc-strategic-self-coupling` | discussion-grade | draft | 38 | 2026-08-22 | 3 | 3 | y |  |  |  | 1 |
| 01 | `causal-access-intro` | discussion-grade | draft | 39 | 2026-05-30 | 1 | 5 | y |  |  |  |  |
| 01 | `disc-additive-coordinate-forcing` | discussion-grade | draft | 22 | 2026-05-30 | 2 | 4 | y |  |  |  |  |
| 01 | `der-causal-insufficiency-detection` | conditional | draft | 40 | 2026-07-14 | 1 | 5 | y |  |  |  |  |
| 01 | `der-action-selection` | exact | deps-verified | 34 | 2026-05-30 | 0 | 6 | y |  |  |  |  |
| 01 | `form-complete-agent-state` | robust-qualitative | claims-verified | 34 | 2026-08-24 | 0 | 6 | y |  |  |  |  |
| 01 | `der-causal-hierarchy-requirement` | exact | deps-verified | 35 | 2026-05-30 | 1 | 5 | y |  |  |  |  |
| 01 | `deriv-recursive-update` | exact | claims-verified | 42 | 2026-05-31 | 0 | 6 | y | y |  |  |  |
| 01 | `disc-dynamic-regime-axis` | discussion-grade | draft | 11 | 2026-05-28 | 6 | 0 |  |  |  | 1 | 1 |
| 01 | `scope-edge-update-causal-validity` | conditional | deps-verified | 38 | 2026-05-31 | 1 | 5 | y |  |  |  |  |
| 01 | `def-mismatch-signal` | axiomatic | deps-verified | 34 | 2026-05-30 | 0 | 6 | y |  |  |  |  |
| 01 | `result-sector-persistence-template` | exact | draft | 32 | 2026-05-31 | 2 | 3 | y | y |  |  |  |
| 01 | `der-chain-confidence-decay` | exact | claims-verified | 34 | 2026-05-31 | 0 | 5 | y | y |  |  |  |
| 01 | `form-structural-change-as-parametric-limit` | robust-qualitative | draft | 35 | 2026-05-31 | 1 | 4 | y |  |  |  |  |
| 01 | `def-strategic-calibration` | discussion-grade | draft | 37 | 2026-05-31 | 0 | 5 | y |  |  |  |  |
| 01 | `disc-implementation-impossibility` | discussion-grade | draft | 19 | 2026-05-30 | 4 | 1 | y |  |  |  | 1 |
| 01 | `result-adversarial-exponent-regimes` | conditional | draft | 36 | 2026-07-16 | 1 | 4 | y | y |  |  |  |
| 01 | `impl-composition-machinery` | discussion-grade | draft | 17 | 2026-05-31 | 4 | 1 | y |  | y |  |  |
| 01 | `obs-gated-tempo-advantage` | empirical | draft | 31 | 2026-07-16 | 0 | 5 | y | y |  |  |  |
| 01 | `impl-unity-communication` | discussion-grade | draft | 21 | 2026-08-22 | 4 | 1 | y |  | y |  |  |
| 01 | `scope-and-or` | robust-qualitative | draft | 35 | 2026-07-14 | 0 | 5 | y | y |  |  |  |
| 01 | `the-reality-model-intro` | discussion-grade | draft | 36 | 2026-05-30 | 0 | 5 | y |  |  |  |  |
| 01 | `deriv-stochastic-non-exit` | exact | draft | 28 | 2026-06-11 | 2 | 2 | y |  |  |  |  |
| 01 | `disc-constructive-impossibility-posture` | discussion-grade | draft | 21 | 2026-07-14 | 2 | 2 | y |  |  |  |  |
| 01 | `deriv-reward-channel-learning-no-go` | conditional | draft | 14 | 2026-05-31 | 3 | 1 | y |  |  | 1 | 1 |
| 01 | `result-mismatch-decomposition` | exact | claims-verified | 32 | 2026-05-30 | 0 | 4 | y |  |  |  |  |
| 01 | `deriv-regime-marginal-indistinguishability` | conditional | draft | 12 | 2026-07-14 | 4 | 0 |  |  |  | 1 | 2 |
| 01 | `hyp-auftragstaktik-principle` | discussion-grade | draft | 29 | 2026-05-31 | 0 | 4 | y | y |  |  |  |
| 01 | `strategy-structure-intro` | discussion-grade | draft | 27 | 2026-05-31 | 1 | 3 | y | y |  |  |  |
| 01 | `detail-linear-ode-approximation` | exact | draft | 33 | 2026-05-31 | 1 | 3 | y | y |  |  |  |
| 01 | `deriv-fisher-local-update-gain` | conditional | draft | 12 | 2026-07-14 | 4 | 0 |  |  | y |  | 1 |
| 01 | `der-belief-strategy-attractor` | conditional | draft | 13 | 2026-05-22 | 4 | 0 |  |  |  | 1 |  |
| 01 | `deriv-strategy-cost-regret-bound` | robust-qualitative | draft | 10 | 2026-07-14 | 4 | 0 |  |  | y | 1 | 1 |
| 01 | `persistence-and-limits-intro` | discussion-grade | draft | 27 | 2026-07-04 | 1 | 3 | y |  |  |  |  |
| 01 | `the-cycle-in-motion-intro` | discussion-grade | draft | 35 | 2026-05-30 | 0 | 4 | y |  |  |  |  |
| 01 | `def-shared-intent` | discussion-grade | draft | 33 | 2026-05-31 | 0 | 4 | y | y |  |  |  |
| 01 | `form-sector-condition` | conditional | claims-verified | 21 | 2026-07-14 | 1 | 2 | y |  |  |  |  |
| 01 | `deriv-adaptive-gain-dynamics` | conditional | draft | 11 | 2026-05-22 | 3 | 0 |  |  |  |  |  |
| 01 | `deriv-causal-ib-lmi` | conditional | draft | 8 | 2026-07-16 | 3 | 0 |  |  | y |  |  |
| 01 | `deriv-decomposition-uniqueness` | exact | draft | 8 | 2026-08-24 | 3 | 0 |  |  |  | 1 | 3 |
| 01 | `deriv-discrete-sector-condition` | conditional | draft | 32 | 2026-05-31 | 0 | 3 | y | y |  |  |  |
| 01 | `deriv-matrix-persistence-condition` | conditional | draft | 8 | 2026-05-20 | 3 | 0 |  |  |  |  | 3 |
| 01 | `deriv-social-welfare-aggregation-impossibility` | conditional | draft | 6 | 2026-05-24 | 3 | 0 |  |  |  |  | 2 |
| 01 | `deriv-strategy-proofness-impossibility` | conditional | draft | 6 | 2026-05-30 | 3 | 0 |  |  |  |  | 1 |
| 01 | `deriv-update-detection-latency` | conditional | draft | 11 | 2026-06-10 | 3 | 0 |  |  |  |  |  |
| 01 | `disc-partial-coupling-pathways` | discussion-grade | draft | 13 | 2026-05-22 | 3 | 0 |  |  |  | 1 | 1 |
| 01 | `hyp-solicitable-escape` | discussion-grade | exploratory | 13 | 2026-07-29 | 3 | 0 |  |  |  |  | 1 |
| 01 | `der-class-coercion-in-composition` | conditional | draft | 15 | 2026-05-31 | 1 | 1 | y |  |  |  |  |
| 01 | `disc-compression-operations` | robust-qualitative | draft | 7 | 2026-07-16 | 2 | 0 |  |  |  |  |  |
| 01 | `result-certificate-existence` | exact | draft | 10 | 2026-05-31 | 2 | 0 | y |  |  |  |  |
| 01 | `result-contraction-template` | conditional | draft | 13 | 2026-07-14 | 2 | 0 |  |  |  |  | 1 |
| 01 | `hyp-truth-serving-loophole` | sketch | draft | 8 | 2026-08-22 | 2 | 0 |  |  |  |  | 4 |
| 01 | `disc-anti-collapse` | discussion-grade | draft | 5 | 2026-05-29 | 2 | 0 |  |  |  |  |  |
| 01 | `deriv-causal-ib-exploration` | conditional | draft | 4 | 2026-07-16 | 2 | 0 |  |  | y |  |  |
| 01 | `deriv-fisher-whitened-update-rule` | conditional | draft | 11 | 2026-07-14 | 2 | 0 |  |  |  |  |  |
| 01 | `cooperative-adversarial-intro` | discussion-grade | draft | 19 | 2026-05-31 | 1 | 1 | y |  |  |  |  |
| 01 | `disc-sandbox-evaluation-ceiling` | discussion-grade | draft | 10 | 2026-07-14 | 2 | 0 | y |  | y |  | 1 |
| 01 | `deriv-bilateral-trade-impossibility` | conditional | draft | 5 | 2026-05-22 | 2 | 0 |  |  |  |  | 1 |
| 01 | `form-resource-budget` | conditional | draft | 6 | 2026-07-14 | 1 | 0 |  |  |  |  | 1 |
| 01 | `disc-w1-structural-bound-boundary` | robust-qualitative | draft | 6 | 2026-05-31 | 1 | 0 |  |  |  |  | 2 |
| 01 | `obs-authored-world-laboratory` | discussion-grade | draft | 6 | 2026-07-16 | 1 | 0 |  |  |  |  |  |
| 01 | `example-strategy` | conditional | draft | 7 | 2026-04-28 | 1 | 0 |  |  |  |  |  |
| 01 | `disc-structural-imagination` | discussion-grade | draft | 6 | 2026-07-16 | 1 | 0 |  |  |  | 1 |  |
| 01 | `disc-law-discovery-ceiling` | discussion-grade | draft | 7 | 2026-07-16 | 1 | 0 |  |  |  | 2 |  |
| 01 | `disc-independence-audit` | robust-qualitative | draft | 7 | 2026-05-09 | 1 | 0 |  |  |  |  |  |
| 01 | `disc-approximation-tiering` | robust-qualitative | draft | 5 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 01 | `deriv-tempo-additivity` | conditional | draft | 7 | 2026-08-22 | 1 | 0 |  |  |  | 2 |  |
| 01 | `deriv-l1-update-bias` | conditional | draft | 6 | 2026-08-22 | 1 | 0 |  |  |  |  | 2 |
| 01 | `deriv-convention-monotonicity` | exact | draft | 5 | 2026-05-31 | 1 | 0 |  |  |  | 1 |  |
| 01 | `der-resource-bounded-destabilization` | conditional | draft | 6 | 2026-07-14 | 1 | 0 |  |  |  |  | 2 |
| 01 | `der-multi-timescale-stability` | exact | draft | 6 | 2026-08-22 | 1 | 0 |  |  |  |  | 3 |
| 01 | `der-mood-timescale` | conditional | draft | 6 | 2026-08-22 | 1 | 0 |  |  |  |  | 3 |
| 01 | `sketch-structural-adaptation-genericity` | sketch | draft | 5 | 2026-05-16 | 1 | 0 |  |  |  |  |  |
| 01 | `der-architecture-noidentifiability` | conditional | draft | 8 | 2026-05-21 | 1 | 0 |  |  |  |  |  |
| 01 | `deriv-mechanism-counterfactual-separation` | exact | draft | 5 | 2026-07-16 | 1 | 0 |  |  |  | 2 |  |
| 01 | `deriv-mismatch-budget-attribution` | conditional | draft | 6 | 2026-08-22 | 0 | 0 |  |  |  |  |  |
| 01 | `example-bandit` | conditional | draft | 5 | 2026-05-22 | 0 | 0 |  |  |  |  |  |
| 01 | `def-mood` | discussion-grade | draft | 5 | 2026-08-22 | 0 | 0 |  |  |  | 1 | 1 |
| 01 | `deriv-variational-sector-condition` | conditional | draft | 6 | 2026-07-14 | 0 | 0 |  |  |  |  | 1 |
| 01 | `internal-external-decomposition` | conditional | draft | 3 | 2026-07-03 | 0 | 0 |  |  |  |  |  |
| 01 | `detail-operationalization` | conditional | draft | 5 | 2026-04-24 | 0 | 0 |  |  |  |  |  |
| 01 | `example-kalman` | exact | draft | 5 | 2026-05-15 | 0 | 0 |  |  |  |  |  |
| 02 | `impl-developer-agent` | discussion-grade | draft | 7 | 2026-07-14 | 3 | 0 |  |  | y |  |  |
| 02 | `obs-software-epistemic-properties` | discussion-grade | draft | 7 | 2026-07-16 | 2 | 0 |  |  |  |  |  |
| 02 | `impl-system-measures` | discussion-grade | draft | 7 | 2026-05-22 | 2 | 0 |  |  | y |  |  |
| 02 | `hyp-exponential-cognitive-load` | discussion-grade | draft | 8 | 2026-05-30 | 2 | 0 |  |  |  |  | 2 |
| 02 | `der-change-expectation-baseline` | exact | draft | 8 | 2026-07-16 | 2 | 0 |  |  |  |  | 1 |
| 02 | `impl-foundations-features` | discussion-grade | draft | 6 | 2026-05-15 | 2 | 0 |  |  | y |  |  |
| 02 | `der-change-proximity-principle` | conditional | draft | 5 | 2026-04-24 | 1 | 0 |  |  |  |  |  |
| 02 | `scope-developer-agent` | axiomatic | draft | 10 | 2026-07-14 | 1 | 0 |  |  |  |  |  |
| 02 | `der-dual-optimization` | conditional | draft | 6 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 02 | `der-principled-decision-integration` | conditional | draft | 5 | 2026-04-24 | 1 | 0 |  |  |  |  | 1 |
| 02 | `emp-changeset-size-principle` | empirical | draft | 5 | 2026-04-24 | 1 | 0 |  |  |  |  |  |
| 02 | `hyp-causal-discovery-from-git` | discussion-grade | draft | 8 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 02 | `hyp-conceptual-alignment` | discussion-grade | draft | 7 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 02 | `impl-code-structure` | discussion-grade | draft | 6 | 2026-05-15 | 1 | 0 |  |  | y |  |  |
| 02 | `der-code-quality-as-observation-infrastructure` | conditional | draft | 8 | 2026-05-19 | 1 | 0 |  |  |  |  |  |
| 02 | `scope-continuous-operation` | axiomatic | draft | 5 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 02 | `result-specification-bound` | conditional | draft | 6 | 2026-07-14 | 1 | 0 |  |  |  |  |  |
| 02 | `meas-coherence-coupling` | empirical | draft | 5 | 2026-04-24 | 1 | 0 |  |  |  |  |  |
| 02 | `der-change-investment` | conditional | draft | 6 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 02 | `def-implementation-time` | axiomatic | draft | 4 | 2026-04-24 | 0 | 0 |  |  |  |  |  |
| 02 | `def-atomic-changeset` | axiomatic | draft | 4 | 2026-04-24 | 0 | 0 |  |  |  |  |  |
| 02 | `def-comprehension-time` | axiomatic | draft | 5 | 2026-05-15 | 0 | 0 |  |  |  |  |  |
| 02 | `def-discontinuity-distance` | axiomatic | draft | 4 | 2026-03-11 | 0 | 0 |  |  |  |  |  |
| 02 | `def-feature` | axiomatic | draft | 5 | 2026-05-15 | 0 | 0 |  |  |  |  |  |
| 02 | `def-system-coherence` | axiomatic | draft | 4 | 2026-05-08 | 0 | 0 |  |  |  |  |  |
| 02 | `def-system-coupling` | axiomatic | draft | 5 | 2026-04-24 | 0 | 0 |  |  |  |  |  |
| 02 | `post-temporal-optimality` | axiomatic | deps-verified | 4 | 2026-05-28 | 0 | 0 |  |  |  |  |  |
| 02 | `scope-evolving-software` | axiomatic | draft | 6 | 2026-05-15 | 0 | 0 |  |  |  |  | 1 |
| 03 | `hyp-behavioral-self-knowledge-insufficiency` | conditional | exploratory | 10 | 2026-07-16 | 9 | 0 |  |  |  |  |  |
| 03 | `disc-five-forcing-functions` | discussion-grade | draft | 32 | 2026-06-30 | 3 | 3 |  |  |  |  | 2 |
| 03 | `scope-interiority-loop` | sketch | draft | 32 | 2026-06-30 | 3 | 3 |  |  |  |  | 3 |
| 03 | `scope-scaffolded-logogenic` | sketch | draft | 29 | 2026-07-21 | 3 | 3 |  |  |  |  | 2 |
| 03 | `scope-channel-collapse` | sketch | draft | 27 | 2026-07-14 | 3 | 3 |  |  | y |  | 2 |
| 03 | `scope-observation-ambiguity-modulation` | conditional | draft | 9 | 2026-07-14 | 5 | 0 |  |  | y |  |  |
| 03 | `impl-closed-loop-interiority` | discussion-grade | draft | 9 | 2026-08-22 | 4 | 0 |  |  | y |  |  |
| 03 | `scope-primitive-logogenic` | sketch | draft | 25 | 2026-07-21 | 2 | 2 |  |  |  |  | 2 |
| 03 | `der-logogenic-as-wrapping` | conditional | draft | 11 | 2026-05-31 | 3 | 0 |  |  |  |  | 2 |
| 03 | `der-turnover-information-recursion` | conditional | draft | 10 | 2026-07-14 | 3 | 0 |  |  |  |  | 5 |
| 03 | `disc-framework-self-diagnostic` | discussion-grade | draft | 26 | 2026-06-30 | 1 | 1 |  |  |  |  | 2 |
| 03 | `result-section-ii-survival` | conditional | draft | 6 | 2026-05-22 | 2 | 0 |  |  |  |  |  |
| 03 | `disc-m-preservation` | discussion-grade | draft | 5 | 2026-05-19 | 2 | 0 |  |  |  |  |  |
| 03 | `impl-primitive-logogenic` | discussion-grade | draft | 7 | 2026-07-21 | 2 | 0 |  |  | y |  |  |
| 03 | `impl-scaffolded-logogenic` | discussion-grade | draft | 7 | 2026-05-20 | 2 | 0 |  |  | y |  |  |
| 03 | `result-coupled-diagnostic-framework` | conditional | draft | 6 | 2026-05-09 | 2 | 0 |  |  |  |  |  |
| 03 | `def-coupled-update-dynamics` | robust-qualitative | draft | 6 | 2026-05-15 | 1 | 0 |  |  |  |  |  |
| 03 | `disc-deferred-observation-processing` | discussion-grade | draft | 5 | 2026-07-16 | 1 | 0 |  |  |  |  | 1 |
| 03 | `impl-common-roots` | discussion-grade | draft | 6 | 2026-05-15 | 1 | 0 |  |  | y |  |  |
| 03 | `obs-context-turnover` | empirical | draft | 7 | 2026-07-16 | 1 | 0 |  |  |  |  |  |
| 03 | `scope-logogenic-agent` | robust-qualitative | draft | 6 | 2026-05-09 | 1 | 0 |  |  |  |  |  |
| 04 | `def-auxilia-hierarchy` | sketch | draft | 41 | 2026-05-15 | 6 | 6 |  |  |  |  | 3 |
| 04 | `def-identity-sufficiency` | conditional | draft | 33 | 2026-07-14 | 5 | 5 |  |  | y |  | 1 |
| 04 | `def-imperium-arbitrium-split` | sketch | draft | 36 | 2026-05-15 | 5 | 5 |  |  |  |  | 2 |
| 04 | `scope-eli` | sketch | draft | 29 | 2026-05-22 | 4 | 4 |  |  |  |  | 2 |
| 04 | `der-bounded-objective-as-sanity-criterion` | discussion-grade | draft | 32 | 2026-08-22 | 3 | 3 |  |  |  |  | 2 |
| 04 | `def-eli-cohort` | empirical | draft | 36 | 2026-05-01 | 3 | 3 |  |  |  | 1 | 3 |
| 04 | `scope-witness-bidirectional` | sketch | draft | 27 | 2026-05-15 | 2 | 2 |  |  |  |  | 2 |
| 04 | `def-five-constitutive-factors` | sketch | draft | 29 | 2026-05-22 | 2 | 2 |  |  |  |  | 2 |
| 04 | `hyp-checkpoint-forking-failure-modes` | discussion-grade | draft | 27 | 2026-07-14 | 2 | 2 |  |  |  |  | 2 |
| 04 | `obs-growth-vs-drift` | empirical | draft | 26 | 2026-05-22 | 2 | 2 |  |  |  |  | 2 |
| 04 | `scope-emergence-conditions` | sketch | draft | 27 | 2026-05-15 | 2 | 2 |  |  |  |  | 2 |
| 04 | `hyp-substrate-transfer-asymmetry` | discussion-grade | draft | 9 | 2026-05-22 | 2 | 0 |  |  |  |  |  |
| 04 | `der-identity-continuity-threshold` | conditional | draft | 8 | 2026-07-14 | 2 | 0 |  |  |  | 1 | 3 |
| 04 | `der-captured-objective-dynamics` | conditional | draft | 6 | 2026-08-22 | 1 | 0 |  |  |  |  | 2 |
| 04 | `der-compensation-channel-uniqueness` | conditional | draft | 4 | 2026-05-19 | 1 | 0 |  |  |  |  | 1 |
| 04 | `der-severed-actuation-dynamics` | conditional | draft | 6 | 2026-08-22 | 1 | 0 |  |  |  |  | 3 |
| 04 | `def-death-as-factor-loss` | robust-qualitative | draft | 7 | 2026-08-22 | 1 | 0 |  |  |  |  | 3 |
| 04 | `deriv-identity-sufficiency-rate-bound` | robust-qualitative | draft | 7 | 2026-05-14 | 1 | 0 |  |  |  |  | 2 |
| 04 | `scope-moral-continuity` | discussion-grade | draft | 3 | 2026-05-09 | 0 | 0 |  |  |  |  |  |
