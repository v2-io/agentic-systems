# Item re-check pilot

KR **I.3** (one open ledger, keyed by claim), under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*, which serves TRUTH about agency. Rechecker: Claude Opus 5.5 (item rechecker, pilot), 2026-10-30. Readers: the I.3 coordinator, to set the shape of the bulk sweep (sections 3 to 5); the lead, for what the re-checks say about the theory (section 2).

## 1. What was judged

I judged 28 of the 371 imported items, drawn from all fourteen source files, and recorded each with `vsect recheck`. Each `--why` names what I read at HEAD and which commit, if any, did the work. The results: 16 `holds`, 3 `landed`, 4 `stale`, 5 `not-an-item`. I also opened two questions with `vsect ask`.

Read the ratio with care. I chose items on purpose. Most were theory-bearing TODO lines, because those are where the trackers could be hiding real open work or wrong claims. A random draw would give far more `not-an-item`. From the item titles of the 343 left (inference, not checked one by one), most of PRACTICA's 33, most of TODO-big-picture's 10, the remaining BIBLIOGRAPHY how-to sections and about 14 of PROPOSED.md's 39 rows are navigation, principles or duplicates.

| Source | Judged | Outcomes |
|---|---|---|
| TODO.md | 10 | 8 holds, 1 landed, 1 stale |
| PRACTICA.md | 2 | 1 holds, 1 not-an-item |
| BIBLIOGRAPHY-TODO.md | 2 | 1 holds, 1 not-an-item |
| TERMINOLOGY-TODO.md | 2 | 1 holds, 1 landed |
| FORMAT-TODO.md | 1 | landed |
| INTEGRATION-CLEANUP-TODO.md | 1 | holds |
| TODO-big-picture.md | 1 | not-an-item |
| PROPOSALS.md | 1 | holds |
| spikes/PROPOSED.md | 1 | not-an-item (a duplicate) |
| spikes/PROPOSED-ADVANCED.md | 1 | holds |
| spikes/PROPOSED-MISC.md | 3 | stale (three fragments of one proposal) |
| spikes/ROUTING.md | 1 | holds |
| audits/STATUS.md | 1 | not-an-item (a roll-up) |
| msc/decision-briefs-2026-07-15.md | 1 | holds |

The trackers' labels were wrong in both directions, as the 2026-05-29 pass found. Two items had landed months before and were never struck: FORMAT-TODO B8 landed eight hours after it was written, and TERMINOLOGY-TODO's stale cross-reference was fixed the next day. Going the other way, one item a Working Note calls RESOLVED is not resolved (2.1). Of the 16 `holds`, six turned out to be framed wrongly in ways that matter to whoever picks them up. The `--why` of each says how.

## 2. What the re-checks say about the theory

Below are what I found, roughly in order of consequence. Where I am stating my own inference rather than something I verified, I say so.

**2.1 `#deriv-persistence-cost`: the derivation is wrong, and canon says it was fixed** (C.1). The body (lines 39 to 43, unchanged since 9745397b) writes the rate-distortion function as $n\sigma_w^2/(4D^2)$ with the *total* distortion $D^2 = n\sigma_w^2/(2\alpha)$. That evaluates to $\alpha/2$. The same line then asserts "$= n\alpha/2$". The headline $\dot R_{\min} = n\alpha/2$ is right: it is $n$ copies of the per-dimension $\alpha/2$. But the displayed algebra does not produce it. A Working Note added by 134b5a4e (gold-lift A16) reads "RESOLVED — do not re-open … the current canonical derivation is the per-dimension form". That is false at HEAD, and it tells future auditors not to look. The channel-capacity floor $C \geq \mathcal T/2$ is derived from this segment, and PROPOSALS C.3 (SP-14) would elevate that floor further. Item: `todo-algebra-typo-in-01-aat-core-src-deriv-pe-2e58`.

**2.2 `#der-observability-dominance`: the investment tradeoff may be wrong-signed** (C.1 candidate; recorded as a question for an independent re-derivation). The segment says instrumenting an intermediate node raises the strategy sector parameter, from the plan-level $1/(n_\Phi+1)$ to the per-edge $\min(1/(n_1+1), \theta_1/(n_2+1))$, "positive whenever $\theta_1 \gt 1/2$". With equal counts the per-edge minimum is $\theta_1/(n+1) \lt 1/(n+1)$. With per-attempt counts ($n_2 \approx \theta_1 n_\Phi$) it is $1/(n_\Phi + 1/\theta_1) \lt 1/(n_\Phi+1)$. So under either reading the plan-level rate is the larger one for every $\theta_1 \lt 1$. The two $\alpha$s also measure different mismatch variables, and the $\theta_1 \gt 1/2$ condition does not appear in the cited source (`#deriv-edge-credence-dynamics` B.2/B.3). My guess is that the true value of instrumenting is diagnostic resolution and unbiasedness (B.3a), not a larger $\alpha$. In the same segment, $\text{conf}_{\text{obs}} = \text{conf}\cdot\text{obs}$ carries a `[Derived]` tag while the segment's own Epistemic Status calls it a first-order approximation, and no other segment uses it. Question: `is-der-observability-dominance-s-observability-i`. Item: `todo-observability-dominance-product-formula-b54f`.

**2.3 `#result-unity-closure-mapping`: a missing hypothesis, and six findings never adjudicated** (C.1). The statement "$\varepsilon_x = 0$ for linear-Gaussian dynamics with consistent linear projections" (lines 60 to 62) lacks the hypothesis it needs. The invariance condition appears only in the sentence after it. The repair is one line: move the condition into the statement. Audit 526815's F151 to F156 are still parked in this segment's off-ramp Working Note. F146, F151 and F154 reached TODO; F153, F155 and F156 never did. F146 (normalizing $U_M$) did land, in f8d9151a; I re-derived the bound $I \le (n-1)H$. The four-route count of C-iv lags in this segment's Working Notes. In the companion `#def-unity-dimensions`, a Working Note (line 138) says the opposite of its own body. Items: `todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8`, `todo-c-iv-composite-route-count-mismatch-gem-bb4b`.

**2.4 Volume 4: a front-door claim with no body, and a no-go that bounds less than it says** (A and E). In 04-eli-core's OUTLINE, row E1 asserts that identity survives substrate migration, "empirically validated across $\geq 4$ substrate families". The row cites `#obs-substrate-independence`, which has never existed (no file, nothing in git history). `#def-eli-cohort` leans on that row. TODO describes the item as promoting an exploratory entry, but the real work is authoring. Separately, `#hyp-substrate-transfer-asymmetry` derives only that the rate-distortion *ceiling* $\min(C_1,C_2)$ is symmetric in direction of transfer. An asymmetry in the $S_{\text{id}}$ actually achieved does not contradict a symmetric ceiling. The spike proposal that would explain it (PROPOSED-ADVANCED #11) says the observed asymmetry "contradicts" the no-go, which is false. The segment also says "the asymmetry is real (empirically)", while its own Epistemic Status says the support is an operational record, not a measurement. So the honest first step is measuring the asymmetry, not explaining it. Items: `todo-04-eli-core-src-obs-substrate-independen-f8a8`, `spikes-proposed-advanced-11-substrate-transfer-asymmetry-origin-d-9171`.

**2.5 Heavy tails: the scope statement is in canon, the strengthening is not** (C.2-adjacent). Three segments state that Models D and S exclude heavy tails. One Working Note (`#deriv-discrete-sector-condition`, line 222) goes further and says infinite-variance environments "cannot be survived by parametric adaptation" because the mean-square Lyapunov proof fails. A failed proof is not an impossibility. The live C1 spike cites the known replacement: under $\alpha$-stable forcing, exit is driven by one large jump and the expected exit time is polynomial in the noise amplitude, not exponential. That spike marks the citation as unverified. Item: `todo-heavy-tailed-disturbances-model-s-assume-f3de`.

**2.6 $\rho_\Sigma$: no estimator, but probably not the circularity the finding claims** (C.2 candidate; my inference, unverified). Two results depend on $\rho_\Sigma$: `#schema-strategy-persistence`'s forgetting prerequisite and the new `#deriv-evidence-allocation-ceiling` (`exact`). Yet no segment says how to estimate it. The source finding (F28 of the 2026-04-23 audit) calls the problem "closer to a circularity". I don't think it is. Drift can be estimated from the raw outcome stream rather than from the $\lambda$-calibrated credences, as in innovation-covariance matching. What remains is sample cost on rarely observed edges, which ties the estimator to EA.1's $1/\pi_i$ lag. That makes it a strengthening with a likely positive answer, not a scope narrowing. Item: `todo-f28-rho-sigma-operationalization-rho-sig-9829`.

**2.7 Smaller ones, each recorded in its item.**

- *"Nominal".* "Nominal" still has opposite scope memberships in `#scope-agency` and `#post-causal-structure`. It is now tracked in three places: TODO and two Working Notes.
- *The symbol $\mathcal C_t$.* It is not a collision in the mathematics. Continuity is a property *of* the chronica, so the `notation:` field on the continuity entry is wrongly assigned.
- *Separability-ladder names.* The leading option would name rung 3 "non-identifiable". Rung 3 is "general open", and impossibility results belong to `#disc-identifiability-floor`, so that name would assert a no-go no derivation supports.
- *Theorem-1 of the language-as-causal-substrate spike* (discourse act to Pearl level 2) still lives only in the spike, which makes it a G.2 item. I passed its C2★ half, and `~/src/behavioral-floor/`, to the C2 spiker through you.
- *An internal memo on the public surface.* `ref/Novelty_defense_and_integration.md` is still cited from 8 segments and from `FINDINGS.md`, and the citation reaches `CURRENT-VOL1*.md`.
- *Citations.* One of 173 Part I segments has a formal citation command. A rough regex finds about 1300 prose citations. This is the mechanism F.2 and F.3 need, and it has not started.
- *What kind of contribution ASF makes.* TODO-big-picture's "Armor" principle (no new mathematical machinery) contradicts the always-loaded SOP's math-novelty section. That is a B.3 question, recorded as `does-asf-introduce-new-mathematical-machinery-or`.

**2.8 A pattern worth naming for I.5.** Twice in 28 items, a Working Note was the false status signal. One says RESOLVED about an unresolved defect (2.1). One says the segment's own body says something it doesn't (2.3). Working Notes are where audit gold and status narration were lifted, and nothing re-checks them against the body. In the store's terms, a check binds to the body and lapses when the body changes, but a Working Note that comments on the body binds to nothing.

## 3. The outcome vocabulary

Most judgments fit one of the four words. Where none fit, I used the nearest word and put the truth in `--why`. That works for a reader of the event, but the dashboard can't see it. Here are the gaps, with the items that hit each one.

- **Partly landed** (the $U_M$/F154 item: half landed, half open). I recorded `holds`. `vsect take --check` already has `narrowed`, and the same word fits here: the item holds, with the landed part named. A split (one item becomes one landed and one holds) would be better still, since the two halves have different owners.
- **Duplicate of another item** (PROPOSED.md row 26 is the index row for PROPOSED-ADVANCED #11; about 14 PROPOSED rows look like this). I recorded `not-an-item`, which loses the link. A `duplicate --of item:x` outcome would keep it.
- **Roll-up** (an audits/STATUS row lists work that is imported separately from TODO). I recorded `not-an-item`. The ledger could compute an audit's graduation from its children, so a roll-up row should never become an item.
- **Superseded by a mechanism** (PROPOSED-MISC's link checker is overtaken by I.3 itself). I recorded `stale`, but `superseded` is truer, and `close` already has it.
- **Real but misframed.** In six cases the item was real but described wrongly: "promote" when the work is "author", "contradicts" when it should be "bounds", or a "circularity" that isn't one. `holds` is correct, but the item's title still carries the wrong frame, and the owner reads the title first. A `--restate "…"` on recheck, kept beside the verbatim import, would let the rechecker's corrected wording travel with the item.
- **A not-an-item that carries a claim** (Armor). Closing it would have buried a real conflict, so I opened a question. Something like `--opens question` on recheck would make that the default move instead of a habit the rechecker has to remember.

The `--owner` field takes free text. I used KR ids ("F.4", "C.1 integrator (unassigned)") rather than agent names, because INTENT's table maps KRs to agents and agent names go stale. If owners are meant to be KR ids, the tool could check them against INTENT.

## 4. The import units (where the per-file unit was wrong)

This accounts for most of the noise. It is what the importer, or the bulk sweep's first pass, should fix before minds are spent on items.

- **BIBLIOGRAPHY-TODO** (`sections`). The unit imported the file's how-to manual (Querying, Adding entries, Registering a PDF, Verifying, Linting, Build-pipeline emit, Run-from-ASF note) as 7 of its 13 items. The real items are the W-n workstreams. There is also an importer bug: lines beginning with `#` *inside fenced code blocks* are parsed as headings. Line 80 (`# Per-paper claim verification`, a bash comment) became the section chain of the items at lines 87 and 97, and line 55 did the same for the item at 61.
- **PRACTICA** (`checkboxes`). Its checkboxes are area labels and links to other trackers (`- [ ] [TODO](TODO.md)`), not work owed. Judging by titles, about 25 of 35 are navigation.
- **TODO-big-picture** (`bullets`). Lines 32 to 33 and 43 to 47 are register principles and guards, and about 7 of its 11 items are not items. Its one real item is W3.
- **PROPOSED.md** (`rows`). 14 rows point to a PROPOSED-ADVANCED entry for their Details. Importing both files gives two items for one proposal. Import one side only.
- **PROPOSED-MISC** (`bullets`). One proposal under a `##` heading was split into its three sub-bullets, and the heading was lost. The `sections` unit at level 2 would have been right.
- **audits/STATUS** (`rows`). Its rows are roll-ups (see section 3).
- **TERMINOLOGY-TODO.** Lines 99 to 103 are pointers to files (`msc/naming/…`, CHANGELOG), not items.
- **TODO.md** (`bullets`). Bullets are mostly the right unit. Some bundle several findings (the A13 bullet holds F146 and F154), and some are scaffolding under a heading (lines 384 to 385, "High-priority next batch"). The titles are truncated mid-sentence (the algebra item's title ends "going from"), so a reader of `vsect open` can't tell what the item is without opening it.
- **Decision briefs** (`sections`) and **ROUTING** are the right units. Their "Joseph decides" framing is stale under this effort's lifted gates, and one ROUTING bullet bundles two items.

## 5. Suggestions for the bulk sweep

These are my guesses, not the sweep's design.

- **First, a cheap structural pass.** It would close navigation, principles, duplicates and roll-ups across PRACTICA, BIBLIOGRAPHY's manual, TODO-big-picture, PROPOSED.md/ADVANCED and STATUS before any reading. By the counts above, that is roughly 60 to 70 of the 343. A model below Opus could do it from the item text plus a glance at the source.
- **Then group by segment, not by file.** Items about the same segment share the expensive reads. Two of mine were on the unity pair, and two (the algebra item and SP-14) rested on `#deriv-persistence-cost`. The `concerns:` field already supports grouping: 123 of the 371 items name segments.
- **The two tools that made `landed` honest:** `git log -S'<distinctive phrase>' -- <segment>` finds the commit that did the work, and `git blame` on the tracker line dates the item. Together they showed both "landed long ago, never struck" cases within a minute each.
- **Treat findings as output.** Theory re-checks produce findings beyond the item: here two questions and several adjacent defects. The sweep should expect them and have somewhere to put them (`vsect ask`, or findings on the segment), not just verdicts on items.

## 6. Not verified, and other limits

I did not check these. Each is recorded as unverified in its event or question.

- The arithmetic in 2.2 needs an independent re-derivation.
- The heavy-tail citation (Imkeller–Pavlyukevich 2006) comes from the C1 spike, which marks it unverified.
- The "about 1300 prose citations" count is a regex over author-year patterns, not a census.
- The estimates in section 4 for the unjudged files come from titles.

Every judgment is stamped with HEAD as it was then. B.1's Part II records merged during the pilot (cd07df2e, 14:45 MDT). Of the segments I judged, the merge touched four: `#der-observability-dominance`, `#der-loop-interventional-access`, `#schema-strategy-persistence` and `#form-objective-functional`. Only two of those changes bear on a judgment. First, `#der-loop-interventional-access`:41 no longer says (C2) fails "generic for any agent whose action depends on internal state". It now names when (C2) fails: an unrecorded cause of the choice, or a decision input the learner's compression dropped. My ROUTING judgment quotes the old wording. It was recorded at 14:29, before the merge, and its stamp (82eac7d3) shows that. The C2★ half of that item is now narrower than the event says. Second, `#der-observability-dominance` gained 44 lines and changed nothing else. Its new claim record calls $\text{conf}\cdot\text{obs}$ "a first-order approximation; the freezing is the claim", which settles the register half of that item. But the body's `[Derived]` tag on the formula is unchanged, and the record does not touch the investment tradeoff in 2.2. So the item still holds as of that commit, narrowed to the tag and the tradeoff.

I edited no canon or item files and made no commits. The vsect builder committed my 28 events, the 16 moved items and the observability question; this file and the second question (`does-asf-introduce-new-mathematical-machinery-or`) were committed in `f6d0ce67`.
