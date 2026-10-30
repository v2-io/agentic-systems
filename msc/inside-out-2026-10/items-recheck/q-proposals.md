# Item re-check, proposals lane

KR **I.3** (one open ledger, keyed by claim), under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*, which serves TRUTH about agency. Rechecker: Claude Opus 5.5 (item rechecker, q-proposals lane), 2026-10-30. Readers: the lead, for the open theory work the proposals had buried and for proposals whose framing was wrong (input to C.2 and G.2) (sections 2 and 3); the vsect builder, for what the tool and the import got wrong (section 5); the I.5 lane, for the canon Working Notes that point at the deleted files (section 6).

## 1. What was judged, and what was deleted

All 75 items in the lane are judged and committed: 24 from `PROPOSALS.md`, 12 from `spikes/PROPOSED-ADVANCED.md` and 39 from `spikes/PROPOSED.md`. The pilot had already judged three more from these files (SP-14, ADV #11, the PROPOSED row for #11). Each `--why` names what I read at HEAD and, for anything landed, the commit that did it.

| Outcome | Count | Notes |
|---|---|---|
| holds | 46 | 8 owned by a KR (F.2 for the four survey rows and SP-23; E.1; F.1; F.3); 38 `unassigned`; 23 carry a `--restate` |
| duplicate | 19 | 13 PROPOSED rows onto their ADV entries; B.1 onto Bundle 1; B.2 and D.2 onto Bundle 2; the CL-1 row onto D.9; the update-operator-sector row and D.3 onto TODO-lane survivors |
| superseded | 6 | Bundle 1 (A.2, B.3), B.3 (B.1, B.2), D.7 (the certificate spine), ADV #4 (canon's scoping of constructive mechanism design), the opacity eq-tag row (A.1), the reciprocal-link row (the ledger) |
| stale | 4 | ADV #10 (premise), E.1 V-strong (its own spike said no), E.2 (its own expiry rule), the stability-certificate Brief row (premise) |
| landed | 0 | three entries were wholly or half landed (below), but each kept a live remainder, so each holds with the landed part named |

Three entries had landed months before and were never struck. SP-9's Legendre-Fenchel reframe of `#disc-additive-coordinate-forcing` landed on 2026-04-25 (8f9a3ca1), the day after the entry was written, and the entry was "reconciled" on 2026-08-22 still saying it waited on Bundle 1. SP-13's logozoetic half landed as `#scope-emergence-conditions` on 2026-05-01 (c741b6c6). G-BP3's "essential scoping question" was answered by the tensor tempo on 2026-05-12 (6c24bed9). The survey-derived PROPOSED rows of 2026-08-22 describe Virgo et al. as "unread" and propose adopting Richens et al., both cited with content in `#def-agent-spectrum` since 2026-05-22 (dfb70e83).

Questions and notes. One question: `effects-spiral-spectral-iff-vs-state-dependent` (section 2.3). Three notes for proposals the import never saw: `proposals-sp-18-internal-aporia` and `proposals-sp-20-dag-vulnerability-metrics` (bullets under PROPOSALS §G, which the section unit skipped), and `proposals-sp-29-infrastructure-as-active-monitor` (folded into SP-27's section; the section item now carries SP-27 only). Seven findings on segments, in `reviews/items-recheck-q.md` and `reviews/items-recheck-q-2.md`, all taken in.

Not yet deleted, and why. `PROPOSALS.md`, `spikes/PROPOSED.md`, `spikes/PROPOSED-ADVANCED.md` and `spikes/PROPOSED-MISC.md` (the pilot judged MISC's three items; it existed only as PROPOSED.md's residual detail file) are fully judged and ready to go, but the pre-commit hook runs `bin/check-links`, and nine links still name them: five in `TODO.md`, two in `PRACTICA.md` (both files had other lanes' edits in flight) and two in canon (`#der-class-coercion-via-wrapping`:222 and :224, for I.5). Each file now opens with a banner saying it is folded into the ledger and waiting for deletion. Once those nine links are re-pointed, the deletion is `git rm PROPOSALS.md spikes/PROPOSED.md spikes/PROPOSED-ADVANCED.md spikes/PROPOSED-MISC.md && git commit -m "…" -- PROPOSALS.md spikes/PROPOSED.md spikes/PROPOSED-ADVANCED.md spikes/PROPOSED-MISC.md`. Re-pointed already: `bin/extract-known-issues` (it raised without PROPOSALS.md; the README's "Architectural proposals under review" list is gone and the section now points at the ledger), `bin/refresh-all`, the four `doc/readme/src/` partials and the regenerated READMEs (`bin/refresh-all --check` is current), `doc/sop/spikes.sop.md` (spike proposals are ledger items), `doc/sop/audit.sop/de-novo.sop.md` (the ledger replaces PROPOSALS as priming-heavy tracking state), `spikes/README.md`, `spikes/INDEX.md`. The lead re-pointed `doc/sop/agents.sop.md`. What is left is in section 6.

## 2. What the proposals say about the theory

The short answer to which proposals are still live theory questions: most of the theory-edge ones are, and most of the architectural ones are not. The architectural portfolio was written in April for a framework that has since reorganized around the stability-certificate spine and, today, around INTENT; its bundles are now INTENT's KRs (A.2, B.1, B.2, B.3, F.2) or answered by the spine. The spike proposals, by contrast, are mostly real open derivations that nothing has touched, because nobody owns them. Below, the ones that matter, in order of consequence. Where I am inferring rather than reporting what I checked, I say so.

**2.1 Part III is the largest open program, and no KR owns it.** The four Part III GAP rows (`01-aat-core/OUTLINE.md`:304-307: latent structural diversity, endogenous coupling, transition dynamics, computational thresholds) are all still open; so are typed admissibility for `#form-composition-closure` and a first-class goal-information-leakage quantity. Upstream of all of it, `#scope-composite-agent` contradicts itself (finding F5 in `reviews/items-recheck-q.md`). It justifies being a scope condition by requiring a well-defined composite objective (:83), but two of its four routes, C-iii and C-iv, admit composites with none. The interim fix recommended on 2026-04-25 was never landed. Eight segments rest on that scope gate. Item: `proposals-bundle-2-section-iii-completion-cluster-50fe`, with SP-21 (`proposals-sp-21-composite-agent-scope-route-ontolo-4969`) as the decision that has to come first. This is a C.3 contradiction and a G-sized gap at once.

**2.2 Three proposals would derive the wrong object.**

- *(UO-mult).* The proposal is to derive $\gamma(U_O) = -\gamma_{\max} U_O$. The segment's own Working Note records that it fails under resource contention: identical targets on a rivalrous resource can maximize interference. Meanwhile the body tags the map `[Derived]` while its table and Epistemic Status call it discussion-grade (F3). The right target is $\gamma$ as a function of target correlation *and* rivalry.
- *The effects spiral.* `#deriv-strategic-composition`:179 says the spiral exists *iff* the joint Jacobian has an eigenvalue with positive real part at an equilibrium. `#der-adversarial-destabilization`:67 says the spiral needs coupling that depends on the state away from equilibrium. Linear instability at an equilibrium is neither necessary nor sufficient for that. ADV #12 would derive closed forms of the first condition. My inference, unverified: its second instance (two Kalman agents with linear coupling) has fixed coupling and should be a no-spiral case. Question opened.
- *Cox-parallel necessity.* `#deriv-graph-structure` proves sufficiency only, and its own text says causal sufficiency is a modeling ideal, not typical. My inference: the necessity direction probably fails without causal sufficiency, where ADMGs or chain graphs are the honest objects. So the expected result is a split characterization, not "DAG is necessary".

**2.3 Unmarked claims stated as fact.** The value-functional cluster's body says flatly that its two grounding routes exhaust the escapes ("There is no third route…", `#disc-value-functional-grounding-floor`:101 and :129). Nothing in the segment derives that, and its own Working Note calls it intuition-only (F6). The forcing table's chain row is listed as Cauchy-FE-forced while failing the segment's own definition of forced (F4); this was found on 2026-08-22, routed into a proposal, and never fixed. In both cases a defect had been routed into the proposal file, and routing it there was where it stopped.

**2.4 Overclaims in the proposals' own framing,** the pilot's ADV #11 pattern. ADV #2 sells a saddle-node threshold under a stipulated penalty as "a pure physics proof … hierarchy is a mathematical necessity". ADV #10's premise is a category error: a softmax is a classical distribution, so its density matrix is diagonal and its von Neumann entropy *is* its Shannon entropy; there is nothing for "interference between strategy branches" to act on. ADV #13 attributes the modularity claim to the wrong M4 operation. PROPOSED-ADVANCED's closing "Brief" (a Gemini reflection) said AAT proved "decentralized AI alignment *requires* transferable utility"; it was deleted with the file, and canon never said it. SP-27's "near-theorem" (lossy $\phi$ implies fork undetectability) does not follow: lossiness is necessary, not sufficient. It also used the retired "Three Deaths".

**2.5 Live theory questions with a clean exit, unowned.** These are real, small, and decidable either way, and nothing in INTENT will reach them: SCC-defect tightness and mixture-support dynamics (`#def-strategy-dag`); the quadratic penalty behind the symbiogenesis threshold; the derivation linking sub-scope $\alpha'$ to single-peaked preferences; R2 detection latency under misspecification; the adversarial meta-gain condition; the $\mathcal A_D$ novelty question for `#der-turnover-information-recursion`; the second continuity no-go (the row pointed at the wrong segment; it lives at `#der-turnover-information-recursion`:126); Roberts 1979 as a fourth charter instance (canon already judges the fit genuine); the Skalse designer-side pass. The moonshots (mean-field limit, percolation, categorical cybernetics, replicator correspondence) hold but are gated or exploratory.

**2.6 Where proposals touch live INTENT work.** Observability as one variable (D.1) is the working thesis's own variable ("a world it cannot fully see"), so its scoping is input to B.3's anchors test. The decorrelation and decomposed-estimator rows sit on the axis C.2's C3 spike is splitting (allocation vs distortion), and the estimator is E.1's. The do-surgery challenge to `#scope-agency` is adjacent to, not the same as, the C2 spike. SP-23 (a theorem-import meta-segment) should be a generated view once F.2/F.3 structure the citations, not a hand-written fourth meta-segment.

## 3. A red flag for the lead: 38 holds with no owner

INTENT says work that feeds no KR is a red flag: either the tree is stale, a finding is unrecorded, or the work has drifted. 38 of my 46 holds are `unassigned` because no KR owns theory-frontier work: strengthenings outside C1-C3, Part III completion, new derivations. C.2 covers three named spikes; G.2 covers stranded spike content, not undone derivations. I don't think the work has drifted: section 2 shows several of these are real defects or real gaps. So either INTENT wants a KR under C for open strengthenings and completion (Part III at least), or the lead decides these are set aside for this effort and says so. I would not resolve it by assigning them to C.2 silently.

## 4. Coordination done

CL-1 survives as `proposals-d-9-sp-22-operator-family-tier-2-backlog-0b44`, and the ROUTING lane closes its CL-1 item onto it. The update-operator-sector landing survives as the TODO lane's `todo-spike-update-operator-sector-orphan-regr-b62b`, and the tensor-tempo follow-on as `todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe`. The vsect builder relayed both to the other lanes.

## 5. What the tool and the import got wrong

- **The `sections` unit at level 3 lost content.** PROPOSALS §G's two bullets (SP-18, SP-20) were not imported at all, and two level-4 proposals (SP-27, SP-29) became one item. §F (retired) and §H (conventions) were rightly skipped, but nothing flagged that a level-2 section held real items above its first level-3 heading. A check would help: any text between a level-2 heading and its first level-3 heading that contains a bold proposal id becomes an item or a warning.
- **`duplicate` worked well;** the cycle guard the builder added after my message is the right fix.
- **Closing a proposal that holds while its landed half is named.** SP-9 and SP-13 both landed their main act and kept a live remainder; `holds` plus a `--restate` naming the commit carried it, but the dashboard counts them as plain open items. The pilot's suggestion of `narrowed` (or a split) would have fit both.
- **Owners.** `unassigned` is accepted and was the honest word 38 times, which is itself the signal in section 3. A way to say "no KR exists for this" distinctly from "nobody has picked it up" would let the dashboard show the gap.
- **A mistake of mine the tool let through.** I took `reviews/items-recheck-q-2.md` with a side-claim I had not checked (that a residue was still open; it was fixed). Since nothing was committed, I removed my two event files, corrected the review, and took it again. `vsect take --dry-run` would not have caught it; reading the cited line before writing about it would have. A `vsect take` that refuses while the review is uncommitted would not help either, since the error was in content; I mention it so the record is straight.
- **Concurrency.** A plain `git commit` failed on another agent's `index.lock` once; retrying `git commit -- <paths>` on the lock worked.

## 6. What is left for other owners

**Live files outside canon that still name the deleted files.** Their owners had uncommitted edits in them, so I did not edit them. The inline links among these are what block the deletion (section 1).

- `TODO.md`:9, :145, :212, :241, :467 (inline links to `PROPOSALS.md`), plus prose mentions; the TODO lanes. Two TODO items already concern PROPOSALS (`todo-j-7-known-issues-surfacing-depth-proposa-c9e1`, whose subject the README change removed; `todo-proposals-bundle-1-status-update-readme-a254`).
- `PRACTICA.md`:6, :10 (inline links), plus mentions; PRACTICA's owner, I.8.
- `doc/sop/audit.sop.md` and `doc/sop/audit.sop/routing.sop.md` (prose mentions of PROPOSALS as a routing destination); the s1 lane had them staged.
- `msc/inside-out-2026-10/INTENT.md` (F.2 names "the `ext:` rows of `spikes/PROPOSED.md`" as a source; they are now the five F.2-owned items in section 1); the lead.

Point-in-time records keep their mentions: dated audit findings, `AUDIT-WORKING-*` and `ADJUDICATION-WORKING-*` dirs, `msc/` memos and reviews, the effort's own review directories, spike reasoning trails, and Refinements 7 and 10 of `spikes.sop.md`, which narrate why the files existed. None of them has an inline link that `bin/check-links` checks.

**Canon referrers, for I.5 to relink** (Working Notes, plus one OUTLINE cell; I edited none):

| Location | Points at | Relink to |
|---|---|---|
| `01-aat-core/OUTLINE.md`:219 | PROPOSED (composition-consistency strengthening) | `item:spikes-proposed-composition-consistency-meta-segment-str-8fc7` |
| `def-strategy-dag`:276, :277 | PROPOSED Tier 1/2 | `item:spikes-proposed-scc-defect-constant-tightness-a1-q1-0815`, `item:spikes-proposed-mixture-support-dynamics-under-the-orien-ca66` |
| `der-adversarial-destabilization`:93, :111 | PROPOSED effects-spiral row | `item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7` (and the open question) |
| `der-class-coercion-via-wrapping`:222, :224 (inline links) | PROPOSED Tier 3 / Tier 2 | `item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e`, `item:spikes-proposed-decorrelation-by-construction-class-3-bu-f138` |
| `der-interaction-channel-classification`:178 | PROPOSED owned-elsewhere | its TODO item (not in this lane) |
| `deriv-adaptive-gain-dynamics`:187 | PROPOSED Tier 3 | `item:spikes-proposed-adversarial-adaptive-gain-meta-gain-temp-06a0` |
| `deriv-gain-sector`:326 | "tracked in PROPOSALS" (never was) | finding F1 of `reviews/items-recheck-q-2.md`; the note should go |
| `deriv-persistence-cost`:171; `deriv-sector-condition`:325; `deriv-stochastic-non-exit`:93 | PROPOSALS SP-23 | `item:proposals-sp-23-disc-theorem-import-architecture-f-a22e` |
| `deriv-reward-channel-learning-no-go`:169 | Skalse bridge | `item:spikes-proposed-advanced-17-skalse-2022-reward-hacking-unhackabil-8188` |
| `deriv-social-welfare-aggregation-impossibility`:124 | PROPOSED Tier 2 | `item:spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71` |
| `deriv-strategy-proofness-impossibility`:129 | PROPOSED Tier 3 | `item:spikes-proposed-sub-scope-alpha-single-peaked-preference-16d5` |
| `deriv-update-detection-latency`:117 | PROPOSED Tier 3 | `item:spikes-proposed-r2-detection-latency-sharpening-under-mo-d44a` |
| `disc-anti-collapse`:50; `disc-sandbox-evaluation-ceiling`:70 | executed SP-26, SP-25 (history) | CHANGELOG; history, not a forward pointer |
| `disc-composition-consistency`:104 | PROPOSED | `item:spikes-proposed-composition-consistency-meta-segment-str-8fc7` |
| `disc-dynamic-regime-axis`:197 | PROPOSED Tier 2 | `item:spikes-proposed-c-3-cost-asymmetry-derivation-structural-cdd1` |
| `disc-implementation-impossibility`:182 | ADV #16/#17 | `item:spikes-proposed-advanced-16-roberts-1979-affine-maximizers-as-can-0922`, `item:spikes-proposed-advanced-17-skalse-2022-reward-hacking-unhackabil-8188` |
| `disc-modularity-state-dynamics`:143 | "for PROPOSED consideration" (never filed) | a ledger note if the two Soviet-sketch sub-spikes are still wanted |
| `disc-stability-certificate`:113, :131 | PROPOSED Brief sharpening (stale) | finding F1 of `reviews/items-recheck-q.md`; the notes should go |
| `disc-stability-certificate`:121; `result-certificate-existence`:141 | PROPOSALS Bundle 1 / O-BP10 | Bundle 1 is superseded (A.2, B.3); the "Joseph confirms" step no longer exists |
| `disc-strategic-self-coupling`:169 | PROPOSED owned-elsewhere | `item:spikes-proposed-spike-strategic-self-coupling-p2-p4-appe-3163` |
| `disc-structural-imagination`:41 | PROPOSALS SP-30 (A.1's epistemic target) | A.1's landing (492a1492) |
| `disc-value-functional-grounding-floor`:162, :165, :178 | PROPOSED rows | `item:spikes-proposed-advanced-18-cross-agent-value-functional-narrowne-bf71`, `item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366` |
| `form-composition-closure`:367, :408 | PROPOSED categorical fit-check | `item:spikes-proposed-advanced-15-categorical-cybernetics-re-grounding-9642` |
| `form-consolidation-dynamics`:166 | PROPOSED Tier 3 | `item:spikes-proposed-quantitative-cls-instantiation-of-consol-6c13` |
| `impl-persistence-and-limits`:101 | "routed to PROPOSALS and never arrived" | already says it lives in TODO; drop the PROPOSALS clause |
| `result-unity-closure-mapping`:122 | PROPOSED UO-mult row | `item:spikes-proposed-u-o-sector-constant-uo-mult-derivation-fbb6` |
| `02-tst-core/…/der-code-quality-as-observation-infrastructure`:135 | PROPOSED Tier 3 | `item:spikes-proposed-code-quality-bistability-2d-dynamical-fo-0dc9` |
| `03-llm-core/…/der-turnover-information-recursion`:129 | PROPOSED C10 row | `item:spikes-proposed-der-turnover-novelty-vs-subsumed-c10-ce20` |

The generated `CURRENT-VOL1.md` carries one mention through a segment; it follows the segments on the next rebuild.

## 7. Not verified, and other limits

- The inferences in 2.2 (Kalman pair as a no-spiral case; necessity failing off causal sufficiency) and in the $\alpha'$ item (single-peaked preferences inducing a potential game only in median-type settings) are mine and unchecked.
- I did not check SP-6's residue line by line, or SP-29's constituents.
- ADV #10's judgment is a theory reading, not a test; I ran nothing.
- Every judgment is stamped at the commit it was made at (c772a6cf through 0dce6b67). Other lanes were editing canon during the sweep; a judgment that cites a line number cites it as of its stamp.
