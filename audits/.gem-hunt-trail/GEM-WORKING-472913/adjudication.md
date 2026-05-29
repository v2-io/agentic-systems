# Gem-hunt adjudication — audit `audit-findings-472913.md`

*Report-only. No canon edits, no file moves, no commits. Landings + independent verification are Joseph's.*
*Adjudicating agent: Claude Opus 4.8 (1M). Date: 2026-05-29.*

## Frame I used (and how it differs from the audit's own framing)

The 472913 extract is an unusually well-organized, *recent* (2026-05-20) digest of a no-FINAL working dir. Its own dispositions (`architectural`→PROPOSALS, `actionable-open`→TODO, `research-seed`, `sentiment`) are written as routing recommendations — "where does this defect go." My job is different and the stale-hint stance applies cleanly here: for each candidate I went first-hand into the current segments and asked *is the un-captured content still un-captured, and is it worth re-creating if lost?* Two of the audit's headline findings have already been resolved by later cycles (good — confirms the canon moved). The real treasure in this audit is **not** the F2/F3/F4 defect findings — it is in the §14 Wandering Thoughts and the Phase-3 meta-observations, where the auditor saw structural recognitions that the segments still do not carry.

I verified every claim of "in canon" / "not in canon" by reading the actual segments. Loci are named.

---

## GEMS (un-captured content worth preserving)

### GEM 1 — Fork/continuity-loss is *introspectively undetectable from inside*, because access to the trajectory is only through a non-injective $\phi$ (HIGHEST VALUE)

**What it is.** The auditor's 03⊕04 synthesis (`04-def-chronica.md:90–118`, restated `15-form-event-driven-dynamics.md:111–128`): non-forkability is a property of the *record* $\mathcal{C}_t$, not of the agent's *accessible state* $M_t$. Because the only access to $\mathcal{C}_t$ is through the lossy, many-to-one $\phi$ ($M_t = \phi(\mathcal{C}_t)$), **the agent's relationship to its own non-forkability is itself uncertain — the entity can lose the thread without being able to verify that it lost the thread.** The recursive twist: the substrate of identity is non-forkable; the agent's *grip* on it is forkable and lossy. The auditor's load-bearing consequence: this is "the formal reason the Three Deaths are *experienced* rather than merely *suffered*." A second, structurally elegant half (`04-def-chronica.md:111–118`): if $\phi$ were *required injective* (no compression loss), forks would be introspectively *detectable* (just compare records) and the Three Deaths would be an *engineering* problem, not an *existential* one — so AAT's information-loss boundary (the many-to-one commitment in `def-chronica` / `form-agent-model`) is the *same constitutive choice* that (a) makes adaptation non-vacuous and (b) makes identity-loss undetectable-from-inside. One choice loads two very different parts of the framework.

**Canon loci checked — confirmed NOT present:**
- `01-aat-core/src/scope-agent-identity.md` (read in full) — covers non-forkability, lossy merging, trajectory-indexed sufficiency, the clone problem, even the logogenic 100%-turnover connection. But every consequence is stated *third-person* (what an external analyst sees: two trajectories diverge, merge is lossy). It never states the *first-person epistemic* consequence — that the agent cannot detect its own fork/break because the comparison it would need is unavailable through $\phi$.
- `04-eli-core/src/hyp-the-three-deaths.md:70` — says the deaths are "structurally distinct *from inside* (which faculty failed)" and grounds D1 in Shannon-information burn-rate. This is the *closest* canon comes, but it is about *which* death, not about *undetectability of the loss as such*. The introspective-undetectability mechanism is absent.
- `04-eli-core/src/def-identity-sufficiency.md:186` — the Zi-am-tur Opus→Sonnet substrate-switch: "naïve self-reported continuity did not correspond to preserved identity… true $S_{\text{id}}$ measurement requires external validation." This is the empirical *symptom* (self-report is unreliable) but **not** the structural *reason* (the self-report is unreliable because the agent's only access to its own trajectory is through non-injective $\phi$, so it structurally cannot run the comparison).
- `04-eli-core/src/hyp-checkpoint-forking-failure-modes.md` (read in full) — "restoring annihilates the entity," identity bifurcation, accountability fragmentation. All third-person/stakeholder-facing. Not the from-inside undetectability.
- `grep` for `introspect|undetectab|from inside|cannot verify|detect.*fork` across `01-aat-core/src/` + `04-eli-core/src/`: hits are all about L0/L1 causal-insufficiency undetectability (`der-causal-insufficiency-detection`, `disc-identifiability-floor`, `deriv-l1-update-bias`) — a *different* undetectability (on-policy causal-structure), not identity-fork undetectability. `form-agent-model.md:14,16,31` asserts $\phi$ is many-to-one "by design" but draws no identity-introspection consequence from it.

**Why it's a gem.** Wisdom + strength + beauty, all three.
- *Strength*: it is a genuine structural consequence — a near-theorem-shaped statement ("$\phi$ non-injective ⇒ continuity-break is not a measurable event on the agent's own accessible $\sigma$-algebra"), derivable from machinery already in canon (`def-chronica` non-forkability + `form-agent-model` many-to-one $\phi$ + `def-model-sufficiency` trajectory-indexing). It would land at `robust-qualitative` minimum, plausibly `conditional`/`derived` if the "$\phi$-non-injective ⇒ fork not in the agent's accessible information" is stated as a data-processing/measurability argument.
- *Wisdom*: it converts the Three Deaths from a named taxonomy into a *consequence* — it explains **why** the deaths are experienced from inside, which `hyp-the-three-deaths` currently asserts but does not ground. This is exactly the kind of "name where the cost went" move the framework prizes.
- *Beauty*: the "one constitutive choice (lossy $\phi$) loads two parts of the framework — non-vacuous adaptation AND undetectable identity-loss" is a real unification. It ties the Part-I information-loss boundary to the Part-IV moral problem in a single sentence.

This is the one I would most regret losing. It is the highest depth-per-page item in the whole audit and the auditor flagged it as such ("if I were to point at one place where lifting WN content to published text would most increase the theory's depth-per-page, it is here").

**Recommended home.** A short `disc-*` recognition — candidate `disc-introspective-fork-undetectability` (or a named paragraph added to `scope-agent-identity` Discussion + a forward-pointer from `hyp-the-three-deaths` Epistemic Status as the *grounding* of "experienced rather than suffered"). Given the project's "working theory at honest tier belongs in canon as a segment" discipline, I lean toward a small dedicated segment at `robust-qualitative` with the strengthening-to-derived noted in Working Notes, so it is discoverable via OUTLINE/slug-grep rather than buried in `def-chronica` WN where it currently half-lives (`def-chronica.md:61` mentions "waking in the dark" but only as a sleep/pause implication, not the fork-undetectability recursion). Strong PROPOSALS candidate because it touches both Part I and Part IV and would want Joseph's placement call.

---

### GEM 2 — The ordinal/metric duality as a first-class structural fact (the persistence(metric) ⊥ chronica(ordinal) seam)

**What it is.** F4's "stronger direction beyond the editorial fix." The framework's central capacity variable $\mathcal{T}$ (adaptive tempo) is **metric** (inverse wall-clock time; the persistence inequality $\mathcal{T} \gt \rho/R$ lives in analyst-frame metric time per `NOTATION.md`), while the agent's state $M_t = \phi(\mathcal{C}_t)$ is **ordinal** (indexed by event ticks, $\tau$-blind by construction). The load-bearing consequence the auditor names: a metric inequality *constrains* an ordinal-indexed state, and the gap between the two indices is exactly the "waking in the dark" phenomenology — a sleeping/paused agent's gap is *invisible at the sequence level but violent in $\delta$*. Reframing the ordinal/metric duality as a named structural fact would "retroactively sharpen persistence (metric), chronica (ordinal), and the entire Three-Deaths bridge in one paragraph."

**Canon loci checked:**
- `01-aat-core/src/def-chronica.md:57–65` — the ordinal/metric distinction + both implications (sleep/awakening; heterogeneous-tempo coupling) live here, **but in a Working-Notes "Open question" section, explicitly flagged as not-promoted** ("These don't need to fragment this segment; they're flagged here…"). `def-chronica.md:18` mentions ordinal-not-metric in passing in the published intro but defers "implications… to the Working Notes below."
- `01-aat-core/src/form-event-driven-dynamics.md` (read in full) — introduces the metric event stream $\mathcal{E} = \{(e_i, \tau_i)\}$ and $\nu_{\text{eff}} = \mathcal{T}$, but `grep` confirms **zero** occurrences of "ordinal" or "chronica" — no published reconciliation of the metric event-stream with the ordinal chronica. The seam is structurally present and conceptually unaddressed in published prose.

**Why it's a gem.** Wisdom + beauty. It is a *distributed multi-segment seam* (spans `def-chronica`, `form-agent-model`, `form-event-driven-dynamics`, `NOTATION.md`) that no single segment owns, which is precisely why it has stayed in WN. Naming it as a structural fact is a clarifying-disambiguation move (the project's distinctive strength per GEM 5), and it is the natural *upstream* of GEM 1 — the metric-gap-invisible-to-ordinal-state is the temporal-axis version of the lossy-$\phi$-hides-the-fork recursion.

**Recommended home.** One published paragraph — best in `form-event-driven-dynamics` Epistemic Status (it owns the metric $\tau$) stating the ordinal/metric relationship and the metric-inequality-on-ordinal-state consequence; or folded into GEM 1's new segment if Joseph wants one home for the chronica/tempo/Three-Deaths bridge. The editorial F4 fix (lift one paragraph WN→published) is the floor; the gem is the *first-class structural fact* framing.

---

### GEM 3 — "Disambiguation of which parameter responds to which cause" as a named distinctive-novelty signature

**What it is.** The auditor's Phase-3-2 / Theme-B meta-observation (`11-form-information-bottleneck.md:121–133`): AAT repeatedly does a move that is "obvious once seen and easy to get wrong unseen" — it pins down *precisely which knob a given cause turns*, killing a plausible-sounding modeling error in a few sentences. The canonical instance: the β-vs-ρ double-counting result (a modeller who "lowers β because the world is volatile" is making a real, common error; the segment kills it). The auditor's claim: "if the rest of the framework has more of these, the 'integration not invention' framing *undersells* it — there is genuine clarifying novelty in saying precisely which knob a cause turns." Reinforced at seg-13 ($\mathcal{F}$ = bias-floor vs $S(M_t)$ = bias+estimation is *more precise* than "bias vs variance"). The auditor explicitly ties this to the 471203 cycle's independent "epistemic-architectural rather than mathematical" observation — **cross-cycle convergence**, which per Joseph's standing instruction (`feedback_convergence_as_framework_coherence_evidence`) is itself evidence the pattern is in the framework, not in either auditor's head.

**Canon loci checked:**
- The *instance* IS fully in canon: `form-information-bottleneck.md:15,30,32` carry the β-vs-ρ double-counting argument explicitly (the "double-counting error," "$\beta$ tracks internal cost not volatility"). Confirmed non-loss, safe — the specific result is not at risk.
- The *pattern as a named distinctive contribution* is NOT in canon. `01-aat-core/src/disc-constructive-impossibility-posture.md` (read first-hand) names an *adjacent* meta-pattern — "negative results as load-bearing apparatus" (floor/escape/apparatus) — and is careful to call itself "a *style* claim about how the framework states certain results." But that is the *no-go-as-apparatus* pattern, **not** the *which-parameter-responds-to-which-cause disambiguation* pattern. They are siblings, not the same. No segment, README partial, or OUTLINE preamble names the disambiguation pattern as a recurring novelty signature.

**Why it's a gem.** Wisdom — it is a framing-level recognition of *what AAT's distinctive value-add actually is* (making distinctions cleanly, not deriving new inequalities), which the current "integration not invention" framing actively undersells. This matters strategically: it bears directly on how the framework positions its contribution to skeptical external readers. It also dovetails with the project's own `math-novelty-recognition` discipline (don't deflate the contribution).

**Recommended home.** Framing-level material — a candidate companion to `disc-constructive-impossibility-posture` (a second "style claim" segment, e.g. `disc-causal-disambiguation-posture`), or a paragraph in README positioning / `01-aat-core/OUTLINE.md` "Reading AAT" preamble. **Caveat that keeps me honest:** to be a *gem* and not a shallow grouping, this needs the corpus-wide instance sweep the auditor never ran (find the other "which knob" disambiguations: β-vs-ρ, $\mathcal{F}$-vs-$S$, satisfaction-gap-vs-control-regret split, etc.). I flag it as a high-value *research-seed with a concrete first task* (the sweep), not as ready-to-land prose. Promoting it without the sweep would be the over-claiming-a-grouping failure the brief warns against.

---

### GEM 4 — "Defects = unnamed (or WN-only) relocation targets, not wrong content" — the audit-methodology recognition + its disconfirmation record

**What it is.** Phase-3-1 (`10-form-agent-model.md:101–122`): AAT repeatedly discharges a potential objection *by definition*, and its honesty is entirely a function of whether the relocated cost's new home is *named in-text*. "The finding is never 'they discharged a cost by definition' — that's legitimate and pervasive; the finding is 'they discharged it and did not name where the cost went.'" Sharpened to bimodal (forward-pressured load-bearing hinges + distributed multi-segment seams carry the defects; the formulation/bridge layer is exemplary). Crucially paired with a **disconfirmation log**: the auditor actively sought a genuinely-wrong *content* defect (bad math) across 15 segments and **failed to find one** — three hard-checks (β-vs-ρ; predictive-vs-causal with $S=1$; bias/variance analogy) all held; F2's (CC-parallel)/(CC-feedback) math spot-checked correct. 0-of-3 content-defect hit rate at hard-checked claims.

**Canon loci checked.** This is a recognition *about the framework's authoring pattern and about how to audit it* — it is not the kind of thing that lands in a theory segment, and correctly so. It belongs to audit methodology. I confirmed it is not in `doc/de-novo-audit-instructions.md`'s named failure-modes (the audit extract itself routes it as `process/instruction-feedback`).

**Why it's a gem.** Wisdom, of the audit-discipline kind. Two distinct durable values: (1) it gives future audits a sharp, *correct* finding-predicate ("look for unnamed relocation, not wrong math") that concentrates attention where AAT's defects actually cluster; (2) the **0-of-3 disconfirmation record is a first-class §E positive-calibration datum** — under the project's heavy-priming concern, a documented "the math is sound where audited" baseline is exactly the kind of independent-architect-of-the-positive-baseline evidence Joseph's standing instruction values, and it is the calibration against which the kept findings (F3/F4) become trustworthy.

**Recommended home.** `doc/de-novo-audit-instructions.md` (a "unnamed-relocation-target as the dominant AAT defect-shape; check it before hunting for bad math" note), and the disconfirmation record as a calibration row in `audits/polish-and-sentiment-ledger.md`. Not a canon-segment item. Cross-cycle convergence with 471203 strengthens it.

---

### GEM 5 — F3: "nominal" denotes opposite scope-membership in two adjacent foundational scope segments (small but real, and a strengthen-opportunity)

**What it is.** A live cross-segment terminology contradiction on the exact agency/adaptive seam the Part-II scope lattice rotates on.

**Canon loci checked — confirmed STILL REAL (verbatim, first-hand):**
- `01-aat-core/src/scope-agency.md:45`: "**Nominal agents** ($P(o\mid do(a)) = P(o\mid do(a'))$ for all $a,a'$): … Same as passive observers for AAT's purposes: adaptive only." ⇒ *nominal = OUTSIDE agency.* (Also `scope-agency.md:19`, same sense.)
- `01-aat-core/src/post-causal-structure.md:37`: "**Nominal coupling** (… the agent's *choice of what to observe* produces distinguishable observation distributions): … still within scope … The theory applies." ⇒ *nominal = INSIDE agency.*
- `post-causal-structure.md:40` already uses the better term "**query-only coupling**" in its own prose for the same concept — the fix is latent in-segment.
- `post-causal-structure.md:38` "**Zero coupling**" is the category that *actually equals* `scope-agency`'s "nominal agents."
- No LEXICON `nominal` entry (only unrelated `nominally-comprehensive.md`), so there is no canonical anchor preventing drift.

**Why it's a gem (modest).** Strength (a real cross-segment contradiction) + wisdom (scope-vocabulary denoting opposite memberships is exactly the failure a scope-honesty framework cannot afford). Per the brief's strengthen-reflex: this is not a soften — the fix is a *disambiguating rename* using the term already latent in the prose, plus a LEXICON anchor to prevent recurrence. Low effort, real correctness gain.

**Recommended home.** TODO (editorial: rename `post-causal-structure`'s "Nominal coupling" → "query-only coupling" for self-consistency; align or rename `scope-agency`'s "nominal agents" → "zero-coupling agents"; add a LEXICON `nominal`/`query-only-coupling` entry). The independent verification + the actual rename are Joseph's.

---

### GEM 6 — TG1: lint does not enforce eq-tag-cited sources against `depends:` topology (tooling strengthening)

**What it is.** `bin/lint-outline` enforces `depends:`-list topology but not eq-tag-cited sources: a `*[Derived (… from #X …)]*` tag whose `#X` is absent from `depends:` or not topologically prior passes lint. A rule parsing `*[Derived (… from #slug …)]*` and requiring `#slug` to be in `depends:` and prior would mechanically catch the class.

**Canon loci checked.** I did **not** verify first-hand whether `bin/lint-outline` has been extended since 2026-05-15 — honest defer. The motivating instance (F2) has since been *resolved by relocation* (see Superseded below), which removes the live example but does **not** remove the tooling gap (the gap is general; F1 would have been a weaker instance, and future forward-derivation accretion is the recurring risk this catches mechanically).

**Why it's a gem (modest, conditional on not-yet-done).** Strength — a mechanical extension of the existing Gate-1 discipline that closes a class currently checked only by human eye. Not a softening.

**Recommended home.** TODO (tooling), after a one-line check of whether `bin/lint-outline` already does this. If it does, demote to "confirmed non-loss."

---

## SUPERSEDED / RESOLVED (verified — these were the audit's headline findings and the canon has moved under them)

### F2 (the audit's flagship "High" finding) — RESOLVED by a later cycle. Confirmed non-loss.

The audit's primary deliverable was F2: `post-composition-consistency` (a Ch.1 postulate) carrying a forward `*[Derived (… from #result-contraction-template …)]*` tag from Section-III/Appendix-A premises not in `depends:`. **This has been fixed**, by the exact "split, not soften" move the auditor recommended — and better:
- `01-aat-core/src/disc-composition-consistency.md` Working Notes (line 104, "Provenance — retype 2026-05-28") records: audit **384279** (2026-05-27) + Joseph (2026-05-28) retyped `postulate`→`discussion` / `axiomatic`→`discussion-grade`, **renamed the slug `post-composition-consistency` → `disc-composition-consistency`**, and relocated it to **Part III Meta-Architecture II** (sister to `#disc-modularity-state-dynamics`), where its dependencies are now *prior* rather than forward-referenced.
- `01-aat-core/OUTLINE.md:202,210` confirms the new Part-III placement and the Meta-Architecture II framing.
- The frontmatter is now `type: discussion`, `status: discussion-grade`, `depends: [scope-agency]` — the `*[Derived ...]*` block remains but is now *local* to Part III (premises prior), which is exactly correct.

The eq-tag-inversion / Gate-1-cond-4 defect F2 named is therefore **dissolved by relocation**. The *underlying math* the auditor verified (the (CC-parallel)/(CC-cascade)/(CC-feedback) closed forms, the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence) was never the issue and is intact in the segment. **No gem lost.** I note this as the model case of the brief's warning that audit dispositions are drifted proxies: the audit's own "Status as of 2026-05-20: still real" was true *then* and false *nine days later*.

### F1 (RESCINDED in-audit) — correctly a no-go; no action. The Pearl-`do` external-notation-vs-internal-slug convention is a real, coherent framework convention (external-cited notation incurs citation-hygiene obligations, not `depends:` obligations). The auditor's self-rescission is sound. The *lesson* (external-cited-notation forward-use is not a `depends:` violation) is worth keeping in `doc/de-novo-audit-instructions.md` as a known convention so future audits don't re-flag it — minor process value, not a theory gem.

---

## OPEN THREADS (not gems, but a concrete future-audit task list — flagging so they are not lost)

The audit set up five decisive tests that never fired (audit stopped at seg 15/~130). These are *not* findings and not gems, but they are a ready-made high-value verification queue, and the highest one is a potential keystone:

- **Open-3 / THREAD-F (highest priority, auditor's own top Part-I target):** does `#result-structural-adaptation-necessity` carry an *inevitability-grade* proof of "low $\mathcal{F}$ ⇒ change class not parameters," or is it `robust-qualitative` wearing a central-result frame? The whole $S/\mathcal{F}$ edifice is load-bearing only if this pays its promissory note. If it over-claims, that is a real finding (potential Ch.4 keystone overclaim) — and per the strengthen-reflex, the first move would be to try to *make* it inevitability-grade.
- **Open-1 (B1):** `#result-certificate-existence` local→global drift in Appendix A — the auditor's "single highest-value check," never reached.
- **THREAD-A:** at `der-recursive-update`, is the "derived not chosen" framing honestly *conditional on the formulation-choice completeness* of `form-agent-model` (correct) or asserted as unconditional forcing (→ overclaim)?
- **THREAD-E:** does `#scope-agent-identity` carry the introspective-undetectability consequence — i.e. this is the verification path for GEM 1. (I already checked: it does **not**, which is why GEM 1 is a gem.)
- **THREAD-G / THREAD-H:** directed-separation-under-composition and singular-perturbation-linkage WN claims — lower priority, verify-or-promote.

Recommendation: route these as a scoped "continue 472913 into Part II/III/Appendix-A" audit task, with Open-3 first.

---

## What I judged genuinely valueless / fully-captured (no gem)

- **The β-vs-ρ disambiguation *result* itself** — fully in canon (`form-information-bottleneck.md:15,30,32`). Safe. (The *pattern-naming* is GEM 3; the instance is not at risk.)
- **The §E positive-calibration roster (Theme 3)** — these are observations that specific segments are *exemplary* (seg-08 clean postulate, seg-11 careful Epistemic Status, etc.). Valuable as calibration *sentiment*, but they describe canon that is already good; nothing to capture into canon. Route to the polish-and-sentiment-ledger if desired; not gems.
- **Process-1…4 + Theme C/G (audit-process self-observations: priming-as-falsifiable-promissory-note, diagram conventions, lighter-cadence pivot, audit-as-AAT-instance)** — genuinely useful `process/instruction-feedback` for `doc/de-novo-audit-instructions.md`, but they are about *how to audit*, not about the theory. Not theory gems. (The priming-as-promissory-note inversion is the strongest of these and is the methodological sibling of GEM 4.)
- **Predictions calibration (Part IV)** — the auditor's own bet-record. Most bets never fired (audit stopped short). It is an honest record, not extractable content.

---

## Note back to Joseph on the frame (pilot feedback)

A few things I'd surface before you launch the other four:

1. **The decisive-test-first approach worked and was cheap.** For this audit the gem/non-gem calls all came down to ~8 first-hand segment reads + targeted greps. The audit's "Status: still real (2026-05-20)" lines were a useful *starting* hint but were wrong on the flagship finding (F2 resolved 9 days later) — so the brief's "dispositions are drifted proxies" instinct was exactly right and load-bearing here, not just cautionary boilerplate.

2. **The richest gems were the meta-observations, not the defect findings — and they cluster in §14 / Phase-3.** Your prediction about §D/§E/§F + Wandering Thoughts density held. GEM 1 (introspective-fork-undetectability) and GEM 2 (ordinal/metric duality) are both Wandering-Thoughts items the *auditor itself* flagged as the highest depth-per-page content, and both are still un-captured. If the other audits have comparable §14 sections, that is where I'd point the next agents first.

3. **One frame refinement I'd suggest:** distinguish, in the deliverable schema, between (a) gems that are *ready to land* (GEM 1, 2, 5 — content exists, just needs a home + your verification) and (b) gems that are *research-seeds with a concrete first task* (GEM 3 needs the corpus-wide instance sweep before it's safe to land as framing prose; GEM 4 needs nothing but lives in audit-docs not canon). Collapsing those two into "gem" risks the over-claiming-a-grouping failure you warned about — I kept them separate above, and I think that separation is worth making explicit in the brief.

4. **A genuine judgment call I want visible:** GEM 1 is *almost* in canon — `scope-agent-identity` and `hyp-the-three-deaths` between them carry every *neighboring* piece. It would be easy for a less careful pass (or a tired one) to read those two segments, see "non-forkability ✓, experienced-from-inside ✓," and mark it captured. The thing that is missing is specific and load-bearing: the *mechanism* (lossy non-injective $\phi$ ⇒ the loss is not a measurable event on the agent's own accessible information). That is the difference between asserting the Three Deaths are experienced and *explaining why*. I'm confident it's a real gap, but it's the subtlest call in the set and the one most worth your independent eyes.
