---
source_cycle: 742613 (de-novo, Codex / 2026-04-25)
extraction_agent: Claude Opus 4.7 (1M context), sweep run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-742613/ (39 files)
final_of_record: audits/.integrated/audit-742613-FINAL-2026-04-25.md
supplement_of_record: audits/.integrated/audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-16 — Cluster B: math-heavy ledgered"
durable_ledger: audits/pending-findings-2026-04-22.md
purpose: |
  Consolidated extraction from the WORKING dir for routing through the
  standard audit-routing process. The original WORKING dir is preserved
  separately; this file is the "what is in there worth processing" digest.
  742613 is the **partial-Section-I deep walk** whose F1 (score sign) and
  F2 (Model-S non-exit) became cluster-B's math-heavy headlines:
  F1 cleanly resolved by direct fix; F2 ≡ 613842-F2 the canonical
  worked example of strengthen-before-soften-then-no-go (Cor A.1S.1 +
  `#deriv-stochastic-non-exit`). Additionally distinctive in this dir:
  the auditor's running per-batch revision files (10/20/30) and the
  Phase-2 triage vocabulary they originated — direct ancestor of the
  routing-tracker disposition enum.
---

# Audit-findings extract — 742613 working-dir mining

The 742613 cycle is a **partial-Section-I de-novo walk by Codex** running the canonical-order discipline rigorously: 34 per-segment reflection files (segments 01-34, mainline `def-agent-environment` → `scope-agent-identity`, plus four appendix jumps to `deriv-recursive-update` / `deriv-sector-condition` / `deriv-gain-sector` / `result-sector-persistence-template`), three strategic-revision checkpoints (post-10/20/30 reflections), `00-initial-predictions.md` and `00-running-outline.md`. The auditor was explicit about partial coverage — Section II, Section III, remaining appendices, operational domains, TST, logogenic, and logozoetic components were not walked. The Phase-2 SUPPLEMENT triangulated each finding against active tracking after de-novo embargo lift.

What distinguishes this dir from neighbours (471203 wide / 613842 dense): 742613 has **per-batch strategic revisions** that operate the candidate-finding ledger across the walk — the auditor reads, flags, watches across segments, then consolidates at 10/20/30. This produced *both* very-high-confidence math findings (F1 sign error, F2 ever-exit conflation, F3 gradient iff overclaim, F4 tempo) *and* a coherent set of canonicalization issues (depends-order, primitive drift, ordering-debt). The Phase-2 SUPPLEMENT then triangulated against active tracking and originated the **durable triage vocabulary** (new / known-unintegrated / known-resolved / tooling-gap / scope-status-mismatch) that became this program's routing-tracker disposition enum.

Per MANIFEST 2026-05-16 (Cluster B) every numbered finding is dispositioned:

- **742613-F1** — score-sign (`def-mismatch-signal`) — *resolved* (direct fix; sign corrected).
- **742613-F2 ≡ 613842-F2** — Model-S non-exit — *resolved by strengthening-then-no-go* (state 3): Cor A.1S.1 + `#deriv-stochastic-non-exit` (canonical worked example).
- **742613-F3 / F5 / F8** + cluster-B siblings — *resolved, the majority by strengthening* (B.4 split into one-point ⇐ vs two-point ⇔; F5 lifted to complete-state argument; F8 well-definedness clause landed).
- **742613-F4 ≡ 613842-F1** — adaptive tempo — substance *resolved by strengthening* (matrix-Loewner canonical, scalar = special case); narrow frontmatter/status residue at TODO:395/126 — not a graduation blocker.
- **742613-F6** — Pearl-`do` before declaration — *duplicate* of 471203 §B F6 → FORMAT-TODO C12 (do not double-track).
- **742613-F7** (passive-observer primitive drift) — *known conceptual tension, integration debt*; tracked via 471203 §F-A cluster + PROPOSALS SP-6.
- **Process feedback** — themed P-block (471203 §G / 584721 §A.1-4 / 742613 partial-pass + appendix-tightening + machine-check + triage-vocabulary / 613842 / 829314 §8). The 742613 Phase-2 triage vocabulary is `superseded-by` the routing-tracker enum (absorbed, **not open**).

This file extracts at five weights: **(I) findings already adjudicated** (preserved with WORKING-dir provenance and the F2 strengthen-before-soften trail made fully visible); **(II) bigger-picture observations** (FINAL's *Other Observations* + *Process Feedback*); **(III) fresh material the FINAL didn't carry forward** (theme-grouped); **(IV) predictions calibration register** (the auditor's predictions-vs-evidence record, withdrawn-candidates trail); **(V) wandering thoughts / methodology themes** (this dir's distinctive cognitive signature is process-discipline rather than ideation breadth — different shape from 471203).

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/MANIFEST)

### F1-trail. Score-function mismatch sign reversed in `#def-mismatch-signal`

**WORKING-dir trail (where the finding crystallized):**

- Surfaced cleanly in segment 18 (`18-def-mismatch-signal.md:14-36`) on first read. The auditor did the Gaussian counterevidence calc inline: $\log P(o|M) = -(o-M)^2/(2\sigma^2)+c$ ⇒ $\nabla_M\log P = (o-M)/\sigma^2 = \delta/\sigma^2$, so the likelihood-increasing direction is $+\nabla_M\log P$, not the $-\nabla_M\log P$ written in the segment. The segment's prose ("points in the direction the model should move to increase the likelihood … coincides with $\delta_t$ up to scaling") is internally inconsistent with its own minus sign.
- Counterevidence search across the read corpus turned up *no* downstream propagation: segment 19 (`19-result-mismatch-decomposition.md:14`) uses the vector $\delta_t = o_t-\hat o_t$ not the score $\tilde\delta_t$; segment 20 (`20-emp-update-gain.md:30-31`) uses abstract $g(\delta_t)$; segment 24 (`24-deriv-sector-condition.md:46`) and segment 26 (`26-der-gain-sector-bridge.md:35`) use abstract $g(\delta)$ / B1 directional fidelity, insulated from the score-sign issue if $g$ is defined correctly. So the bug is **local**: the definition and its Gaussian-equivalence interpretation contradict each other; downstream usage didn't propagate the reversal.
- 20-segment strategic revision (`20-strategic-revision.md:5-8`) named it as "highest-confidence issue now."
- 30-segment strategic revision (`30-strategic-revision.md:8`) listed it as the lead high-confidence finding.
- Promoted to FINAL §"Finding 1" with full Gaussian derivation and explicit repair options.
- Phase-2 SUPPLEMENT §1: searched for prior tracking — *none found*; "appears to be a new durable finding" — was probably missed (a prior audit reflection at `msc/AUDIT-WORKING-849201/17-def-mismatch-signal.md` praised the score-function formulation without flagging the sign).

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-FINAL` — resolved (direct fix).** First-hand verified `01-aat-core/src/def-mismatch-signal.md:34` reads:

```
$$\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$
```

— minus sign removed; the prose at line 36 ("points in the direction the model should move to increase the likelihood … Under Gaussian models, they coincide up to scaling") is now consistent with the formula. The repair is exactly the SUPPLEMENT §1 recommended form.

**Strengthen-before-soften check:** there was no strengthening direction available here — this is a local sign-error category where "fix the sign" *is* the strengthening (the false claim deleted; the correct claim survives). No softened ghost.

### F2-trail. Model-S local stochastic persistence conflates fixed-time tail bounds with ever-exit probability *(the strengthen-before-soften canonical worked example)*

**WORKING-dir trail (where the finding crystallized):**

- Surfaced in the segment-24 appendix jump (`24-deriv-sector-condition.md:12-32`) on first read. The auditor did the Ornstein-Uhlenbeck counterevidence calc inline: $d\delta = -\alpha\delta\,dt + \sigma_w\,dW_t$ has stationary Gaussian distribution with unbounded support ⇒ for any finite $R$ and $\sigma_w \gt 0$, the process exits $[-R,R]$ eventually with probability 1 ⇒ $P(\tau_R \lt \infty) = 1$, while the segment's claimed bound (Prop A.1S, line 194) can be made arbitrarily small by taking $\alpha R^2 \gg \sigma_w^2$.
- The auditor cleanly distinguished the mathematical objects: "What Markov's inequality can bound is $P(\lVert\delta(t)\rVert \gt R)$ at a fixed time, or under a stationary distribution at a randomly sampled time. It does not bound the probability of ever exiting over an infinite horizon." (FINAL §"Finding 2" Counterevidence section + WORKING-dir segment 24).
- Followed through downstream consumers: segment 28 (`28-result-sector-condition-stability.md:11-23`) — "more cautious than the appendix's false ever-exit probability claim" but still depends on the template; segment 29 (`29-result-sector-persistence-template.md:11-31`) — "stochastic issue from `deriv-sector-condition` is repeated and amplified here" (the template imports the false non-exit inheritance for downstream Model-S instantiations); segment 30 (`30-result-persistence-condition.md:13-23`) — "inherits finding J" via the template at the central persistence result.
- 30-segment strategic revision (`30-strategic-revision.md:9`) listed it as a confirmed math finding with main-result impact.
- Promoted to FINAL §"Finding 2" with five problematic-passage lines (line 180 / 194 / 242 / 253 / 270 / 282 of `deriv-sector-condition.md` plus `result-sector-persistence-template.md:47, 90` and `result-persistence-condition.md`).
- Phase-2 SUPPLEMENT §2: "Relevant prior material exists, but it does not close the specific bug." Triangulated to TODO:311/687 ("Prop A.1S region condition lifted via stopping-time localization"), spike `spike-disturbance-model-split.md:157-167` (correctly uses fixed/stationary tail, not infinite-horizon), and `audits/pending-findings-2026-04-25.md:37-48` (tracking a different Model-S issue — variance gap). Classification: **"integration error from spike/cautious-localization material into source"** — the spike-level claim "at steady state, probability outside $R$ is small" became, in source, "probability of ever exiting is small." Different mathematical objects.

**Audit's proposed remediation (the softening ask):**

FINAL §"Finding 2" recommended a *softening* of the source statement: "State only the stopped bound; require global sector condition for unstopped mean-square convergence; use finite-horizon exit probability; use bounded stochastic disturbances; or frame $R_S^\ast \lt R$ as a typical-scale condition rather than an infinite-horizon persistence guarantee." SUPPLEMENT §2 endorsed similar softenings: "Replace $P(\tau_R \lt \infty)$ with a fixed-time, stationary, or finite-horizon probability statement," etc.

**Project response — the strengthen-before-soften move:**

Rather than execute these softening recommendations directly, the project (per MANIFEST 2026-05-16 + CHANGELOG 2026-05-16 + `spikes/.integrated/spike-stochastic-non-exit-strengthening-2026-05-16.md`) attempted to **strengthen the underlying theorem**. The strengthening question: *can the infinite-horizon non-exit object (the cleanest form the source statement was reaching for) be proved at all under Model S?*

The strengthening attempt **failed structurally**, and the failure was itself the result. The no-go: under additive stochastic forcing, $P(\tau_R \lt \infty) = 1$ for every correction strength $\alpha$ and every $\sigma_w \gt 0$, and **the natural maximal-inequality route (Ville/Doob on an Itô-Lyapunov supermartingale) provably cannot certify any horizon-independent non-exit bound**. The infinite-horizon containment object both the audit and the source segment were reaching for *does not exist mathematically*.

**The landing — replacement, not softened coexistence:**

Per the *integration-is-replacement* discipline (CLAUDE.md §"Landing a strengthened result"), the resolution landed as:

1. **Prop A.1S restructured to region-aware four-sub-result form** (first-hand-verified `deriv-sector-condition.md:178-206`):
   - **(i) Stopped bound** — Grönwall on $\mathbb{E}[\lVert\delta(t \wedge \tau_R)\rVert^2] \leq \lVert\delta(0)\rVert^2 e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$.
   - **(ii) Mean-square persistence condition** — $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)} \lt R$ iff $\alpha \gt n\sigma_w^2/(2R^2)$.
   - **(iii′) Fixed-time tail** — Markov on stopped second moment ⇒ $P(\lVert\delta(t)\rVert \gt R) \leq \mathbb{E}[\lVert\delta(t \wedge \tau_R)\rVert^2]/R^2 \xrightarrow{t\to\infty} n\sigma_w^2/(2\alpha R^2)$. Stationary-sharp.
   - **(iv) Finite-horizon sample-path bound** — additive first-exit bound $P(\sup_{0\leq s\leq T}\lVert\delta(s)\rVert \gt R) \leq (\lVert\delta(0)\rVert^2 + n\sigma_w^2 T)/R^2$, rigorous under (A2') alone, vacuous for $T \gtrsim R^2/(n\sigma_w^2)$, consistent with $P(\tau_R \lt \infty) = 1$.
   - Plus explicit prose at line 198 (verbatim, first-hand-verified): "*This controls the mismatch at any single time. It is not an infinite-horizon containment statement: under additive Brownian forcing the diffusion is recurrent on $\mathbb{R}^n$ … so $P(\tau_R \lt \infty) = 1$ over an unbounded horizon — there is no $P(\tau_R \lt \infty) \lt 1$ bound, and none is claimed. Pathwise containment of $\mathcal B_R$ is a Model-D guarantee only (Prop A.1's positive invariance); Model S controls the typical scale (ii) and the fixed-time tail (iii′), not the sample path over an unbounded horizon. The kind-of-guarantee dichotomy this exposes is itself a result — see the Discussion.*"

2. **Corollary A.1S.1 (Disturbance-Model Containment Dichotomy)** — new exact result (first-hand-verified `deriv-sector-condition.md:258-268`): $P(\tau_R \lt \infty)$ is **exactly the two-point set** $\{0, 1\}$ — 0 under Model D (positive invariance from Prop A.1), 1 under Model S (a.s. exit of a non-degenerate diffusion), **$\alpha$-invariant**: "which point obtains is fixed by the disturbance model's support structure (bounded vs. unbounded), not by the correction strength $\alpha$." Discussion: "This sharpens the hand-off into `#result-structural-adaptation-necessity` — in any genuinely stochastic environment region-exit is a certain eventual event, so the structural-adaptation trigger is *generic, not exceptional*, for a sufficiently long-lived agent."

3. **`#deriv-stochastic-non-exit`** — dedicated Model-S no-go appendix (first-hand-verified at `01-aat-core/src/deriv-stochastic-non-exit.md`, `status: exact`, `stage: draft`). Header verbatim: "*Under additive stochastic forcing there is no finite bound on the infinite-horizon first-exit probability — $P(\tau_R \lt \infty) = 1$ for every correction strength — and the natural maximal-inequality route to one provably cannot exist; this is the load-bearing proof step behind Prop A.1S(iii′)/(iv) and the Model-S half of Corollary A.1S.1.*" The "why the natural route cannot work" subsection answers the inevitable reader question — *"are you sure you can't just Doob/Ville this?"* — as part of the proof.

4. **Body + result tables state present truth only.** First-hand-verified `deriv-sector-condition.md:270-302` Summary of Results table carries the row for Cor A.1S.1 — labeled "**Proved** — new exact result." The What Is Derived vs Chosen table at line 280-301 carries Prop A.1S as "**Proved**; the infinite-horizon non-exit probability is structurally 1 for additive Model S (no-go, Khasminskii ch. 3-4) — pathwise containment is Model-D-only." The falsified ever-exit object is **deleted**, not kept-softened-with-a-pointer. The history (*"previously carried a false infinite-horizon ever-exit claim; the audit recommended a soften; the project pursued strengthening and found a no-go"*) lives **only** in CHANGELOG 2026-05-16 and the integrated spike file `spikes/.integrated/spike-stochastic-non-exit-strengthening-2026-05-16.md`.

**Cascade verified clean** (per MANIFEST + verifiable from segment depends-graph): every dependent consumer (`result-sector-persistence-template`, `result-sector-condition-stability`, `result-persistence-condition`, adversarial exponent regimes) now consumes the stopped bound / mean-square threshold / fixed-time tail — *not* the falsified infinite-horizon ever-exit object. The falsified object is propagated nowhere.

**Disposition (per MANIFEST 2026-05-16 Cluster B):**

**`subsumed-by-MANIFEST` — resolved by strengthening-then-no-go (state 3 per `doc/audit-routing-instructions.md` §8 enumerator).** The audit-asked softening was replaced with a no-go theorem **strictly stronger** than what the audit aimed at: not "the summary segments need more caveat," but "the cleanest form of the object the source segments were reaching for *cannot exist*, and the dichotomy is itself the result." The Model-S no-go is present truth on the spine (Cor A.1S.1 in the result table at `deriv-sector-condition.md:276`), demonstrated where non-obvious (`#deriv-stochastic-non-exit` appendix), and clean on every dependent path. The integration-is-replacement discipline operated exactly as CLAUDE.md describes: refuted claim deleted, label tracks current truth-status (`exact`, not down-tiered for being new), no-go demonstrated as present truth not softened ghost.

**Cross-cycle resonance — 742613-F2 ≡ 613842-F2:**

Per MANIFEST 2026-05-16 Cluster B: "*613842-F2 ≡ 742613-F2 — same segment-state; the precise ever-exit-conflation reading governs the dedup.*" Both audits surfaced the same segment-state from different angles — 742613 walked the source segment directly and caught the false claim in Prop A.1S inline; 613842 caught the *downstream-summary compression* of Prop A.1S into the result-template consumers. The dedup language is sharper than typical: it names *what made the dedup possible* (the precise reading of the ever-exit-conflation from 742613-F2 + the matched segment-state from 613842-F2). Two-cycle independent convergence on the same mathematical object is itself framework-coherence evidence — the bug was structural enough that two different reading-disciplines hit it.

**Pedagogical value (the canonical worked example, three teaching moments):**

- **The audit's "softer" recommendation was correct on its own terms** — the source segment did carry a false ever-exit bound that needed *something* done about it. The audit was not wrong to flag.
- **The strengthening attempt is what surfaces the no-go**, not the softening attempt. Had the project executed the audit's recommendations directly (state only the stopped bound; soften the language), the no-go would have remained hidden — the audit's repair would have been mathematically non-monotonic (more visible caveats around an object that cannot exist in its hoped-for form). The strengthen-first move pulled the underlying impossibility into view.
- **The no-go is itself a positive result** — the dichotomy $P(\tau_R \lt \infty) \in \{0,1\}$ with the value selected by disturbance-model support structure is *new*, *exact*, and *operationally important* (it sharpens the structural-adaptation trigger from "exceptional" to "generic" for sufficiently long-lived agents). What looked like a softening-job was really a *missing exact theorem* — visible only after attempting to strengthen.

This trail (jointly with 613842-F2's WORKING-dir trail) is the durable evidence-material for the strengthen-before-soften discipline's onboarding documentation (`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md`, `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`). The 2026-05-16 cycle landing log + the two WORKING-dir trails together are the canonical worked example named in global-memory.

### F3-trail. Gradient "equivalence" overstates one-point sector as local strong convexity in `#deriv-gain-sector` / `#der-gain-sector-bridge`

**WORKING-dir trail (where the finding crystallized):**

- Predicted in segment 26 (`26-der-gain-sector-bridge.md:16-27`) on first reading of the bridge segment: "*This appears too strong … A radially inward gradient field can satisfy the one-point sector condition while the Hessian is negative in some directions away from the optimum.*" Flagged as "Potential finding" — auditor explicitly deferred elevation pending appendix read: "*I will check `deriv-gain-sector` before elevating this to a finding.*"
- Defended-on-the-appendix in segment 27 (`27-deriv-gain-sector.md:11-50`): the proof's reverse direction silently replaces a one-point inequality with full gradient monotonicity. The auditor provided a 1-D counterexample: $L'(x) = x(1+\tfrac12\sin(10x))$ satisfies the one-point sector condition with $\mu = 1/2$ globally, but $L''(x) = 1 + \tfrac12\sin(10x) + 5x\cos(10x)$ is negative for some $x$ in modest neighborhoods, so $L$ is not locally strongly convex there. **Strong convexity is sufficient, not equivalent to, the one-point sector condition.**
- Secondary issue named at segment 27 (`27-deriv-gain-sector.md:52-58`): the loss-function classification's "All exponential family models in natural parameter form satisfy GA-3 globally" overclaims globality. Poisson natural parameter $\theta$ has Fisher information $e^\theta$, whose infimum over $\mathbb R$ is 0 ⇒ no uniform global lower bound on $\lambda_{\min}(\text{Fisher})$.
- Cross-segment cross-check: `result-sector-persistence-template.md:72` correctly describes AAT's sector condition as one-point anchoring and strictly weaker than full two-point strong monotonicity. *That sentence actually supports the audit finding*: the bridge appendix's iff claim is stronger than the framework's own meta-description elsewhere in the corpus.
- 30-segment strategic revision (`30-strategic-revision.md:10`) listed it as confirmed high-confidence finding.
- Promoted to FINAL §"Finding 3" with the four problematic-passage lines (`deriv-gain-sector.md:127, 133, 149, 157, 261`) and the counterexample inline.
- Phase-2 SUPPLEMENT §3: "Known distinction, unrepaired offender." Triangulated to `result-sector-persistence-template.md:70-72`, TODO:181 (operator-sector unification as one-point reduction), `spikes/spike-jacobian-b1-strengthening.md:114-120, 195, 538, 558` (explicit discussion of the gap). Classification: **"not new as a conceptual distinction, still a real source bug"** — the correct distinction lives in `#result-sector-persistence-template` while the false iff lives in `#deriv-gain-sector` / `#der-gain-sector-bridge`.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-MANIFEST` — resolved by strengthening.** First-hand-verified `01-aat-core/src/deriv-gain-sector.md:129-169`: Proposition B.4 has been **split into B.4-i and B.4-ii**:

- **B.4-i: One-point sector ⇐ strong convexity (one direction only).** Local $(\alpha/\eta)$-strong convexity of $L$ on $\mathcal B_R(M^\ast)$ implies the one-point sector condition with $\alpha = \eta\mu$; *the converse fails* with the counterexample $L'(x) = x(1 + \tfrac12\sin(10x))$ embedded verbatim at line 161.
- **B.4-ii: Two-point sector ⇔ strong convexity (full equivalence).** Under the strengthened *two-point / incremental* sector condition (named DA2'-inc, formalized in `#deriv-discrete-sector-condition`, used as bridge-lemma precondition in `#form-composition-closure`), the iff holds bidirectionally by Nesterov 2004 Thm 2.1.10.
- Line 169 names *exactly where each direction lands in AAT*: one-point form for `#deriv-sector-condition`'s Lyapunov persistence (six persistence-flavored results inherit through `#result-sector-persistence-template` T2); two-point / incremental form for `#form-composition-closure`'s bridge lemma (DA2'-inc) for full-update-map contraction at the composite level. "Strong convexity sits at the strict end of this scale: it implies both."

The secondary Poisson Fisher overclaim is also fully resolved: line 188 (first-hand-verified) reads "*Exponential family models in natural parameter form satisfy GA-3 pointwise on the interior of the natural-parameter space, and uniformly on any compact subset of the interior. The Hessian is the Fisher information matrix $\mathbf{I}(\theta)$, which is positive definite in $\operatorname{int}(\Theta)$ — but pointwise positive definiteness does not imply a uniform global lower bound on $\lambda_{\min}(\mathbf{I}(\theta))$. The Poisson natural parameter is the canonical counterexample*…" — the audit's counterexample landed as a named exhibit in the segment's loss-function classification table.

**Strengthen-before-soften check (verification — strictly stronger than the audit's ask):** the audit FINAL §"Finding 3" recommended "replace iff with one-way implication, or strengthen GA-3 to an incremental/two-point condition if equivalence to strong convexity is required." The landing did **both** in a clean structural decomposition: one-way implication for the one-point form (B.4-i), full iff for the strengthened two-point form (B.4-ii). The auditor's counterexample is preserved verbatim as the exhibit demonstrating the one-point ⇏ strong-convexity direction. This is the strengthening direction the audit named as available, *executed cleanly without softening*.

### F4-trail. Adaptive tempo labeled `exact` while segment says additive formula overcounts (`#def-adaptive-tempo`)

**WORKING-dir trail (where the finding crystallized):**

- Surfaced in segment 22 (`22-def-adaptive-tempo.md:6-26`) on first read. The auditor named the internal contradiction: frontmatter `status: exact` + Formal Expression $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$ + Discussion explicitly saying additive tempo overcounts under correlated channels and overestimates under anisotropy. "*If $\mathcal T$ is defined as 'effective rate of useful information acquisition,' then an expression the same segment identifies as an upper bound under correlated channels is not exact generally. Similarly, scalar tempo cannot be exact in anisotropic systems if weak dimensions bottleneck persistence.*"
- Downstream-margin-impact warning: "*This is likely important because `result-persistence-condition`, adversarial advantage, and composition use $\mathcal T$ downstream. If downstream results rely on scalar additive tempo without repeating independence/isotropy assumptions, margins will be overestimated.*"
- Cross-verified in segment 30 (`30-result-persistence-condition.md:25-28`): the segment does carry a "Channel independence and scalar tempo" caveat in Discussion, but the linear operational forms remain prominently stated as forms "used throughout the theory." The caveat is in the right place at the consumer but the *definition* still presents the additive scalar formula as exact.
- 20-segment strategic revision noted it as one of the scope/status issues.
- Promoted to FINAL §"Finding 4" with line refs.
- Phase-2 SUPPLEMENT §4: "Known caveat, formal/status mismatch." Triangulated to existing caveat sites: `def-adaptive-tempo.md:44-50` itself; `disc-independence-audit.md:59` (additive formula is upper bound, equality iff channels independent); `result-persistence-condition.md:99`; `der-team-persistence.md:32`; `der-tempo-composition.md:94`; PROPOSALS:234 ("independence profile" inclusion). Classification: **"the caveat is not new, the finding is that the caveat is not integrated into the formal/status layer."**

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-MANIFEST` — substance resolved by strengthening; narrow frontmatter/status residue tracked TODO:395/126.** First-hand-verified `01-aat-core/src/def-adaptive-tempo.md` lines 1-65:

- Line 19 (the unrestricted additive scalar primary form) still appears.
- Lines 28-38 introduce the **tensor extension under Fisher-local invariance regime** as the canonical matrix-Loewner object: $\mathcal T = \sum_k \nu^{(k)} \cdot K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ (per-coordinate primitive). The scalar form is recovered as the **shared-eigenbasis collapse** — "*when all $H_M, \{H_L^{(k)}\}$ commute (always in 1-D; under (PI)/Čencov along the natural-gradient direction in higher dimensions), each $K^{(k)}$ acts as the eigenvalue $\eta^{(k)\ast} = U_M/(U_M + U_o^{(k)})$ on the shared natural-gradient direction and the matrix sum collapses to a scalar.*"
- Line 44 Epistemic Status explicitly names the scope dichotomy: "*The scalar form is exact in the isotropic / shared-eigenbasis / nonredundant-channel case … The tensor form is the natural object under anisotropic gains, Fisher-whitened updates ( #deriv-fisher-whitened-update-rule), LMI causal-IB ( #deriv-causal-ib-lmi), and per-dimension persistence ( #result-per-dimension-persistence) — regimes where scalar tempo overestimates effective adaptation along weak dimensions.*"
- Line 58 Discussion §"Channel independence assumption" keeps the redundancy-penalty acknowledgment intact (with the equality condition $\mathcal T \leq \sum_k \nu^{(k)}\eta^{(k)\ast}$, equality iff channels independent).
- Line 63 Discussion §"Scalar vs. vector tempo" points to `#deriv-matrix-persistence-condition` as the canonical form, with the per-coordinate form as its diagonal-axis-aligned special case; "matrix-Loewner is strictly sharper (the per-coordinate form is *unsafe* when $\mathcal{T}$'s eigenbasis misaligns with the coordinate axes — `#deriv-matrix-persistence-condition` §'Where per-coordinate is unsafe')."

**Strengthen-before-soften check:** the audit FINAL §"Finding 4" recommended *softenings* — "define $\mathcal T_{\text{add}}$ as nominal/additive tempo; make exactness conditional on channel independence and isotropy; or put the effective tempo definition in mutual-information / covariance-adjusted form with the additive expression as a special case." The project's resolution is **strictly stronger** than any of these: the tensor / matrix-Loewner form is the canonical object covering anisotropic and correlated regimes via the per-coordinate matrix gain primitive, with the scalar form recovered as the shared-eigenbasis collapse special case. The substance is honored, the surface is honored, and the project landed past what the audit asked for — exactly parallel to F3 (B.4 split).

**Cross-cycle resonance — 742613-F4 ≡ 613842-F1:** per MANIFEST 2026-05-16 Cluster B both are tracked together; the substance is the same, the segment-state is the same. 613842 caught it at the `def-adaptive-tempo` segment level (definition-scope mismatch), 742613 caught it at the same segment plus traced the downstream-margin impact through `result-persistence-condition`. Two-cycle convergence on the same definition-scope drift.

**Residue (not a graduation blocker):** the frontmatter still reads `status: exact` (line 4), and the Formal Expression at line 19 leads with the additive scalar form (not the tensor form). Per MANIFEST, this narrow frontmatter/status residue is tracked at TODO:395/126 — substance is resolved, the polish is whether the frontmatter should carry an explicit scope-tag noting that exactness is on the tensor object and the scalar is the special case. The MANIFEST's "not a graduation blocker" is the right disposition — the prose layer carries the scope honestly.

### F5-trail. `a_t = \pi(M_t)` exact only for a narrower state convention than AAT later uses (`#der-action-selection`)

**WORKING-dir trail (where the finding crystallized):**

- Surfaced in segment 17 (`17-der-action-selection.md:6-20`) on first read. The segment's own Discussion admits that for actuated agents action selection involves $G_t = (O_t, \Sigma_t)$ and the policy becomes $\pi(M_t, G_t)$. But the frontmatter says `status: exact` for $a_t = \pi(M_t)$. The auditor: "*`form-agent-model` defined $M_t$ as epistemic substate, not complete agent state once goals and strategy exist. So $a_t = \pi(M_t)$ is not exact for the broader AAT theory; it is exact only for agents whose non-epistemic purposeful state is absent, fixed, or folded into $M_t$.*"
- Three repair options named: scope explicitly to Section I; write as $a_t = \pi(X_t)$ for complete internal state with $X_t = M_t$ in Section I and $X_t = (M_t, G_t)$ in Section II; mark $\pi(M_t)$ as conditional on fixed/absorbed goals.
- Downstream propagation traced in segment 21 (`21-def-causal-information-yield.md:18-22`): CIY's default reference distribution $q(\cdot|M) = \pi(\cdot|M)$ inherits the $M$-only policy issue for actuated agents (would need $q(\cdot|M,G)$ or a continuation-policy convention).
- 20-segment strategic revision noted it as the secondary scope/status finding alongside the sign error.
- Promoted to FINAL §"Finding 5" — confidence "medium-high"; "Type: scope/status mismatch."
- Phase-2 SUPPLEMENT §5: "Known supersession / integration debt." Triangulated to `form-complete-agent-state.md:36, 52` (explicit supersession statement: "*`#der-action-selection` is superseded by $a_t = \pi(M_t, G_t)$ after the state lift, with $a_t = \pi(M_t)$ surviving for Section I agents where $G_t = \emptyset$*"), `def-model-sufficiency.md:40` (already uses the later $\pi(M_t,G_t)$ standard), `def-value-object.md:33-39` (compatible with the richer policy state when scoped carefully). Classification: **"known supersession, integration debt"** — the broader theory knows the right form; the early segment doesn't carry the forward-pointer to its own supersession.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-MANIFEST` — resolved by strengthening / lift-statement.** First-hand-verified `01-aat-core/src/der-action-selection.md`:

- Line 19 still reads "Action is a function of the agent's complete internal state. Under Section I scope ( #scope-adaptive-system) — where $M_t$ is the entire internal state — this gives: $a_t = \pi(M_t)$."
- Line 29 now carries an explicit lift paragraph (first-hand-verified verbatim): "*Section II lift. When the internal state lifts to $X_t = (M_t, G_t)$ for purposeful agents ( #form-complete-agent-state), the same structural argument gives $a_t = \pi(M_t, G_t)$ — action conditions on the complete internal state, which now includes the purposeful substate. The policy form here is the Section I instantiation $G_t = \emptyset$; the actuated-agent form is recovered by the same completeness argument applied to $X_t$.*"
- Line 33 Epistemic Status explicitly carries the scope: "*Exact within Section I scope. The derivation follows from `#form-agent-model`'s completeness commitment: if $M_t$ is the agent's complete internal state (by definition), then action — which depends on internal state — is a function of $M_t$. The Section II generalization $a_t = \pi(M_t, G_t)$ is exact within Section II scope by the same argument applied to the lifted state $X_t$ ( #form-complete-agent-state); see `#def-model-sufficiency` for the form already in use downstream.*"
- Line 51 Discussion §"Connection to Section II" unpacks the actuated-agent form coupled to directed separation.

**Strengthen-before-soften check:** the audit FINAL recommended writing the exact statement as "$a_t = \pi(X_t)$ for complete internal state; in Section I, $X_t = M_t$ or $G_t$ is fixed/implicit; in Section II, $X_t = (M_t, G_t)$." The landing keeps the segment scoped to Section I (preserving the layered presentation that the framework wants) but adds the explicit lift paragraph plus Section II forward-pointer in both Discussion and Epistemic Status, so a reader encountering this segment first knows immediately that the Section II generalization exists by the same completeness argument. This is the "make the layering explicit" repair option — neither softening nor false unification. The completeness-argument unification per MANIFEST: "*completeness-argument unification*" applied across F3/F5/F8 means the same structural argument (state completeness ⇒ function of state) is reused at each layer, and the segment now names the layered application.

### F6-trail. Early Section I canonical order is not a clean dependency linearization

**WORKING-dir trail (where the finding crystallized):**

- The longest-running candidate-finding in the dir — surfaced incrementally across multiple segments and consolidated at the 10/20/30 strategic revisions:
  - Segment 4 (`04-scope-adaptive-system.md:11-22`): `scope-adaptive-system` uses $\mathcal C_t$ in the formal scope condition before `def-chronica` appears in OUTLINE and without declaring it.
  - Segment 5 (`05-scope-agency.md:15-22`): `scope-agency` uses $do(a)$ in the formal scope condition before `def-pearl-causal-hierarchy` and without declaring it.
  - Segment 14 (`14-form-event-driven-dynamics.md:10-16`): formal expression conditions event information on $M_{\tau^-}$ without declaring `form-agent-model`.
  - Segment 23 (`23-hyp-mismatch-dynamics.md:20-29`): Epistemic Status says the fluid limit is formally justified by `#deriv-discrete-sector-condition` without declaring it, *and* the markdown link points to `discrete-sector-condition.md` (wrong filename) instead of `deriv-discrete-sector-condition.md`.
  - Segment 26 (`26-der-gain-sector-bridge.md:31`): repeats the wrong `discrete-sector-condition.md` link.
  - Segment 33 (`33-form-consolidation-dynamics.md:12-30`): declares downstream Appendix-A *discussion/meta* dependency on `disc-compression-operations` (not a proof-only appendix); uses `#schema-strategy-persistence` and `#form-structural-change-as-parametric-limit` in Formal Expression without declaring them.
  - Segment 6 (`06-post-composition-consistency.md:14-26`): imports Section III composition scope/closure/tier machinery before those terms are introduced (composite scope, closure admissibility, bridge lemma, tiers, etc.).
- 10-segment strategic revision (`10-strategic-revision.md:1-11`) and 30-segment strategic revision (`30-strategic-revision.md:15`) consolidated the pattern: "*the current OUTLINE row order is not a clean topological linearization of the formal objects used in segment bodies.*"
- Promoted to FINAL §"Finding 6" with full enumeration of the nine problematic-passage lines.
- Phase-2 SUPPLEMENT §6: "Mixed: tooling gap + prior-noted fragments." Triangulated: current `bin/lint-outline` reports 0 ordering violations and 0 missing dependencies — the issue is *body-level* hidden dependencies, wrong links, and non-proof appendix imports that lint doesn't inspect. Some sub-issues seen by prior audits (`msc/AUDIT-WORKING-584721/01-section-i-leaves.md:13-19` already identified `scope-adaptive-system` missing `def-chronica`; `msc/AUDIT-WORKING-584721/08-def-mismatch-signal.md:32` noted `form-event-driven-dynamics → form-agent-model` drift). Recommended repairs: second lint mode for body-level canonical symbols and slug links; split backmatter references into proof-only appendices vs conceptual/meta appendices; promote specific wrong-link and hidden-dependency cases.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification):**

**`subsumed-by-FINAL` — mostly resolved; F6 residue (Pearl-`do` before declaration) is `duplicate` of 471203 §B F6 → FORMAT-TODO C12 (existing home; do not double-track).** First-hand verifications:

- **`scope-adaptive-system.md` `def-chronica` dep**: first-hand-verified line 8 — `def-chronica` is declared in `depends:`. **Resolved.**
- **`scope-agency.md` Pearl-`do` dep**: first-hand-verified line 24 — Pearl `do(\cdot)` is still used with parenthetical reference "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)" but the dep is *not* in the `depends:` list. This is the FORMAT-TODO C12 residue — duplicate of 471203 §B F6. **Routed (not double-tracked).**
- **`form-event-driven-dynamics.md` `form-agent-model` dep**: first-hand-verified line 9 — `form-agent-model` is declared in `depends:`. **Resolved.**
- **`hyp-mismatch-dynamics.md` link**: first-hand-verified line 54 — link now correctly reads `[#deriv-discrete-sector-condition](deriv-discrete-sector-condition.md)` (the correct filename). **Resolved.**
- **`form-consolidation-dynamics.md` `disc-compression-operations` dep**: per SUPPLEMENT §6, `bin/lint-outline` classifies this as backmatter reference. Verified-still-classified-thus.
- **`post-composition-consistency` Section III machinery**: subsumed by F5 from 471203 (PROPOSALS SP-6 + TODO:149); per MANIFEST already-routed.

**Tooling-gap residue (the body-level lint gap):** the SUPPLEMENT §6 recommendation — "Add a second lint mode for body-level canonical symbols and slug links, not just declared dependencies" — is itself a `process/instruction-feedback` item carried in the P-block ("machine-check helper"). Not separately tracked as graduation work.

### F7-trail. Adaptive-system primitives are action-coupled while adaptive scope explicitly includes passive observers

**WORKING-dir trail (where the finding crystallized):**

- Surfaced earliest in segment 1 (`01-def-agent-environment.md:7-16`): the first primitive segment defines an agent as "produces actions that affect $\Omega$" — the auditor named the watch item: "*are passive adaptive systems outside this primitive definition until later repaired, or are 'actions' allowed to be null / ineffective at this stage?*"
- Reinforced in segment 4 (`04-scope-adaptive-system.md:9-15, 23-26`): `scope-adaptive-system` Discussion explicitly broadens to passive Bayesian learners and Kalman filters "with or without control inputs"; the formal object still uses `(Agent, Ω)` inheriting the action-coupled primitive. "*If `Agent` inherits `def-agent-environment`'s action-affecting condition, passive observers do not fit.*"
- Confirmed in segment 7 (`07-def-chronica.md:13-22`): chronica is defined as $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ — depends on `def-action-transition` and includes actions by construction; passive Bayesian learners would need a chronica with absent/null actions or an observation-only history.
- Strongest single statement at segment 8 (`08-post-causal-structure.md:11-19`): "*zero-coupling systems are outside agency but inside adaptive scope if they observe under residual uncertainty. This confirms the framework's intent and makes the earlier primitive issue sharper rather than dissolved. The theory intends passive estimators to be in Section I, but its first primitive segment and chronica definition are action-shaped.*"
- 10-segment strategic revision and 30-segment strategic revision both called it out as a primitive/scope drift pattern.
- Promoted to FINAL §"Finding 7" — confidence "medium-high"; Type: "scope/terminology inconsistency."
- Phase-2 SUPPLEMENT §7: "Known conceptual tension, integration debt." Triangulated to `scope-adaptive-system.md:41`, `post-causal-structure.md:36-38`, `def-agent-spectrum.md:44` (passive trackers "fully within Section I's scope"), and prior audit notes (`msc/AUDIT-WORKING-584721/01-section-i-leaves.md:19`; `msc/AUDIT-WORKING-742613/04-scope-adaptive-system.md`). Classification: **"terminology/primitive integration problem"** — not a newly discovered conceptual requirement, but the foundational definition uses action-affecting "agent" language too early.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-FINAL` — known conceptual tension, integration debt; tracked via 471203 §F-A cluster + PROPOSALS SP-6.** First-hand-verified `01-aat-core/src/def-agent-environment.md:11-23`: the primitive definition still reads "An agent is an entity that receives observations from an environment, maintains internal state, and produces actions that affect the environment" with condition 3 "It produces actions that affect $\Omega$ (action channel)." The repair proposed by SUPPLEMENT §7 ("introduce a neutral Section I primitive such as $(AdaptiveSystem, \Omega)$ or define an action channel as optional/degenerate until `#scope-agency`") has **not yet executed in `def-agent-environment.md`**.

The conceptual hierarchy is *repaired in prose* downstream (`scope-adaptive-system` Discussion + `post-causal-structure` + `def-agent-spectrum`), but the primitive segment still leads with the action-coupled definition. Per MANIFEST routing, this is the F-A-cluster integration-debt class with multiple-cycle convergence: 471203 + 584721 + 742613 all surfaced it. PROPOSALS SP-6 carries the structural-restructure option; the editorial-fix interim option lives in TODO.

**Strengthen-before-soften posture verification:** the audit recommended a *softening* ("introduce a neutral 'adaptive system / system-environment coupling' primitive for Section I, with action events optional/null"). The strengthening direction available — and not yet executed — would be to derive the passive-observer case as a structurally-meaningful limit of the agent definition (action channel as optional / degenerate), making the hierarchy more precise rather than softer. Currently the residue sits at the editorial-interim layer.

### F8-trail. Model sufficiency undefined when full history has zero predictive information (`#def-model-sufficiency`)

**WORKING-dir trail (where the finding crystallized):**

- Surfaced cleanly in segment 12 (`12-def-model-sufficiency.md:11-22`) on first read. The auditor named the edge case: $S(M_t) = 1 - I(\mathcal C_t; o_{t+1:\infty}|M_t, a_{t:\infty}) / I(\mathcal C_t; o_{t+1:\infty}|a_{t:\infty})$ is undefined when the denominator is zero (saturated-noise, iid, prediction-vacuous regimes). Boundary values for $S = 0, 1$ stated without a denominator-positive condition.
- Propagation traced in segment 13 (`13-def-model-class-fitness.md:10-12`): $\mathcal F(\mathcal M) = \sup_{M\in\mathcal M} S(M)$ inherits the denominator-zero issue; segment 31 (`31-result-structural-adaptation-necessity.md:22-26`) extends to `result-structural-adaptation-necessity` via the $\mathcal F$ definition.
- Promoted to FINAL §"Finding 8" — confidence "medium"; Type: "mathematical edge-case / missing well-definedness condition."
- Phase-2 SUPPLEMENT §8: "Likely new local well-definedness gap." Searched active tracking — *no entry found*. Classification: **"likely new local well-definedness gap"** — small but should be fixed because downstream ratios inherit the undefined case.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-MANIFEST` — resolved (direct fix / well-definedness clause).** First-hand-verified `01-aat-core/src/def-model-sufficiency.md:26-35`: the well-definedness clause has been added cleanly (verbatim from current `src/`):

> *"Well-definedness. $S(M_t)$ is defined when $I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \gt 0$ — when the chronica carries some predictive information about future observations beyond what the action sequence alone supplies. When the denominator vanishes (saturated-noise environments, prediction-vacuous regimes, fully iid observations independent of history), $S(M_t)$ is undefined: predictive sufficiency is a property of a prediction task, and there is no prediction task to be sufficient for. Downstream constructs that build on $S$ — `#def-model-class-fitness` and `#result-structural-adaptation-necessity` — inherit the same scope and are correspondingly inapplicable in predictively-vacuous regimes."*

Boundary values for $S = 1, 0$ now explicitly carry "(assuming the well-definedness clause holds)." Epistemic Status (line 35) elaborates: "*The scope clause ($I(\mathcal C_t; o_{t+1:\infty} | a_{t:\infty}) \gt 0$) is the natural domain for a predictive-sufficiency measure: a ratio whose denominator is zero is not a meaningful notion of 'fraction retained,' and 'any model is sufficient when there is nothing to predict' would smuggle structure into a regime that has none.*"

**Strengthen-before-soften check:** the SUPPLEMENT §8 recommended a softening choice ("define $S = 1$ by convention if the numerator is also 0, or mark the quantity undefined/not applicable"). The landing chose the **strengthening direction** — making the scope clause itself a *substantive epistemic statement* about what predictive sufficiency *is*, rather than a band-aid convention. The clause now does conceptual work: "predictive sufficiency is a property of a prediction task; there is no prediction task to be sufficient for." This is structurally cleaner than the convention path.

---

## Part II — Bigger-picture observations (FINAL §"Other Observations" + §"Process Feedback")

The FINAL doesn't number these as their own §F findings (unlike 471203); they live under *Other Observations* and *Process Feedback on the Instructions* + *Phase 2 Process Feedback*. Preserved here with WORKING-dir provenance and current dispositions.

### BP1. Recursive-update derivation is basically sound; status language harmonization needed

WORKING-dir provenance: segment 15 (`15-der-recursive-update.md:14-18`) and segment 16 (`16-deriv-recursive-update.md:26-29`). The auditor caught a frontmatter-vs-prose status mismatch — frontmatter `conditional`, Epistemic Status says "Exact, with a partly definitional character." After reading the appendix (Doob-Dynkin formalization + seven-attack defense), the auditor concluded: "*the strongest accurate label is 'exact conditional on C1-C3 and event-driven/sampled representation; continuous coupling generalizes the input form.'*" The continuous-coupling caveat from Attack 2 should be more visible in the main segment.

**Disposition:** `subsumed-by-FINAL "Other Observations"`. Did not separately verify current `src/` state of `der-recursive-update.md` frontmatter / Epistemic Status harmonization. Light editorial pass.

### BP2. Spike references outside Working Notes (FORMAT provenance violations)

WORKING-dir provenance: surfaced in segment 24 (`24-deriv-sector-condition.md:34-37`), segment 26 (`26-der-gain-sector-bridge.md:30`), segment 27 (`27-deriv-gain-sector.md:68-71`), segment 31 (`31-result-structural-adaptation-necessity.md:27-29`). FORMAT says spike references should live only in Working Notes after promotion; the auditor found multiple promoted segments citing `spikes/spike-*` files in Epistemic Status or main body.

**Disposition:** `subsumed-by-FINAL "Other Observations"` — classified as "process/format issue, not a theory finding." Material for project-wide cleanup pass; not a graduation blocker. The discipline is named in CLAUDE.md ("spike references only in Working Notes" + `feedback_spike_references_only_in_working_notes.md` in MEMORY).

### BP3. `form-information-bottleneck` mixed-tier compression

WORKING-dir provenance: segment 11 (`11-form-information-bottleneck.md:8-19`). `status: exact` on a segment whose Formal Expression includes robust-qualitative $\beta(\rho,\pi)$ claims. The auditor explicitly *did not* promote this to a defended finding because the Epistemic Status paragraph disambiguates tiers in prose; only the frontmatter aggregation is slightly tense.

**Disposition:** `subsumed-by-FINAL "Other Observations"` — *"did not promote this to a finding"* per FINAL. Same observation lives at Fresh-1 of `audits/audit-findings-613842.md` (cross-cycle convergence with 613842 — both auditors landed the same observation independently, both honestly classified it as `soft-polish` not promoting to a finding). Material for any future IB-area cycle.

### BP4. `result-structural-adaptation-necessity`: $M^\ast = \arg\sup$ attainment

WORKING-dir provenance: segment 31 (`31-result-structural-adaptation-necessity.md:17-21`). The supremum in $M^\ast = \arg\sup_{M\in\mathcal M} S(M)$ may not be attained — needs approximate optimizer or compactness/attainment assumption. Auditor classified as "minor mathematical precision, easy to fix, not high-severity."

**Disposition:** `subsumed-by-FINAL "Other Observations"`. Minor — light editorial fix. Did not separately verify current `src/` state.

### BP5. Partial-pass protocol needed in audit instructions

WORKING-dir provenance: distributed across the strategic-revision files; explicit at 30-segment revision (`30-strategic-revision.md`) and consolidated in FINAL §"Process Feedback": "*The strongest process tension is scope feasibility. The instructions are written for a very large context and a long-running audit. In this Codex environment, following the cadence faithfully through the whole framework would be a multi-turn effort. I recommend the instructions explicitly name a 'partial-pass protocol': how to stop honorably, how to label coverage, and whether to ask Joseph before switching to triage when the full outline is clearly larger than one turn.*"

**Disposition:** `process/instruction-feedback` — carried in P-block ("742613: partial-pass protocol"). Material for `doc/de-novo-audit-instructions.md` revision.

### BP6. Appendix exception needs tightening

WORKING-dir provenance: FINAL §"Process Feedback" — surfaced via segment 33 (`33-form-consolidation-dynamics.md:12-30`), where the auditor encountered a Section I formulation depending on a late Appendix-A *discussion/meta* segment (`disc-compression-operations`) rather than a proof appendix. The audit-instructions appendix exception is framed around Appendix A *derivations / proofs*; conceptual/meta appendices may spoil downstream reading.

Recommended three-way distinction:
- proof appendix dependency that can be read immediately;
- meta-pattern appendix dependency that may spoil future segments;
- downstream non-appendix dependency used in Formal Expression, which should remain a finding.

**Disposition:** `process/instruction-feedback` — carried in P-block ("742613: appendix-exception tightening"). Material for `doc/de-novo-audit-instructions.md` revision.

### BP7. Instruction conflict with CLAUDE.md should be made explicit

WORKING-dir provenance: `00-initial-predictions.md:11-12` and `00-running-outline.md:30-31` both log the conflict. The auditor (Codex) treated the de-novo audit instructions as task-specific override, deferring TODO.md. The FINAL §"Process Feedback" explicitly recommends: "*Future agents would benefit from a one-line override in the audit instructions: 'For this audit, this supersedes CLAUDE.md's normal TODO-first instruction.'*"

**Disposition:** `process/instruction-feedback` — carried in P-block ("742613: explicit CLAUDE.md↔TODO conflict override"). Note: CLAUDE.md has since (2026-05-19→20) added an active-reconsideration callout at the top; the audit-instructions side may still need its own one-line override, but the bleed problem is structurally acknowledged on CLAUDE.md's side.

### BP8. Machine-check helper for dependency-order auditing

WORKING-dir provenance: FINAL §"Process Feedback": "*A script that prints, for the current OUTLINE order, 'segment → declared dependencies not previously read' would help auditors catch dependency violations without reading future segment content. It should print only slugs/stages, not summaries, to preserve de-novo posture.*" The auditor specifically notes this would have caught `disc-compression-operations` before reading `form-consolidation-dynamics`. Also calls for a second lint mode for body-level canonical symbols and slug links (SUPPLEMENT §6).

**Disposition:** `process/instruction-feedback` — carried in P-block ("742613: machine-check helper"). Tooling-gap; not a framework finding. Material for `bin/`-level tooling work.

### BP9. "Consider writing" reflection prompts too soft

WORKING-dir provenance: FINAL §"Process Feedback": "*The reflection prompts are useful, but 'consider writing' is too soft for the experimental goal. For Codex, the tool cadence is the real enforcement point. The instruction's final reminder says per-segment files are expected; I recommend saying earlier: 'After each segment, write a reflection file before opening the next segment, unless explicitly documenting a deviation.'*"

**Disposition:** `process/instruction-feedback` — carried in P-block ("742613: 'consider writing' too soft"). Light editorial fix to `doc/de-novo-audit-instructions.md` framing of reflection-file cadence.

### BP10. Phase-2 triage vocabulary (the durable methodology contribution)

WORKING-dir provenance: FINAL §"Phase 2 Process Feedback" — *"I recommend adding a durable triage vocabulary: New / Known-unintegrated / Known-resolved / Tooling gap / Scope-status mismatch. That vocabulary would keep future Codex instances from treating every rediscovery as a fresh contradiction, while still preserving real source bugs that survive despite adjacent caveats."*

This is the **most consequential single methodology contribution from this dir**. The auditor's framing: without Phase-2 triangulation, the auditor would have over-classified the gradient-equivalence and adaptive-tempo findings as newly discovered — they are better understood as integration failures where the repo already contains the correct ideas in adjacent locations but not in the offending formal statements. The vocabulary makes this distinction surfaceable as a per-finding classification.

**Disposition (per polish-and-sentiment ledger P-block):** **`superseded-by` the routing-tracker enum** — absorbed, **not open**. The 742613 Phase-2 triage vocabulary is the direct ancestor of this program's routing-tracker disposition enum (`new` / `subsumed-by-FINAL` / `subsumed-by-MANIFEST` / `actionable-open` / `process/instruction-feedback` / `duplicate` / `superseded-by` / etc.) used in this very extraction file. The methodology contribution operated downstream as designed: it shaped how `doc/audit-routing-instructions.md` §8 enumerates dispositions, and it shaped how the MANIFEST per-cluster tables read. Worth recording explicitly because the lineage matters for any future revision of the enum.

---

## Part III — Fresh material the FINAL didn't carry forward

This dir is **deep but narrow** (partial Section I, 34 segment reflections, 8 numbered findings). The auditor was disciplined about not promoting weak candidates — most surfaced observations either survived burden of proof and made it into the FINAL §"Findings," or were honestly noted as "watch items"/"not yet a finding"/"minor" without promotion. The fresh material is correspondingly thinner than 471203's wide adversarial-creative residue, but several observations are worth surfacing as candidates the FINAL compressed past.

### Fresh-1. Action-fluency framing's $\Delta\eta^\ast(\Delta\tau) \approx 0$ marker may conflate update-gain improvement with action-quality improvement

Segment 17 (`17-der-action-selection.md:26-29`) — the auditor flagged the action-fluency framing's proposed formal marker $\Delta\eta^\ast(\Delta\tau) \approx 0$: "*This may conflate update-gain improvement with action-quality improvement unless `der-deliberation-cost` defines deliberation as improving update gain / model quality rather than decision quality.*" Reinforced in segment 25 (`25-der-deliberation-cost.md:19-23`): "*the prose starts by saying deliberation improves action quality through internal simulation, but the formal benefit term is improvement in update gain $\eta^\ast$. Those are not the same object. The Epistemic Status names this limitation, so I do not count it as a finding.*"

The auditor explicitly didn't promote — Epistemic Status names the limitation. But the *underlying conceptual gap* (deliberation-as-epistemic-gain vs deliberation-as-decision-quality) is interesting in its own right: the action-fluency vocabulary is about decision quality; the formal threshold is about epistemic gain. Whether these are the same object under specific assumptions, or genuinely two-track, is open.

**Suggested disposition:** `research-seed` — material for an `impl-*` chapter-end implications segment or a future action-fluency-formalization cycle. Not a defect; a candidate strengthening direction where the formal marker could be promoted to derived rather than discussion-grade if the conceptual gap closes under named conditions.

### Fresh-2. Mutual-information vs realized-surprisal distinction in `#form-event-driven-dynamics`

Segment 14 (`14-form-event-driven-dynamics.md:17-21`) — the segment defines event information as $\mathcal I(e_\tau) = I(e_\tau; \Omega_\tau | M_{\tau^-})$ (mutual information) but says "surprising events carry much information." The auditor: "*Mutual information is an expected reduction in uncertainty, not the realized surprise of a particular event. The intuition is close, but if the framework later treats $\mathcal I(e_\tau)$ as realized information content, it may need pointwise information / surprisal rather than MI.*" Watch item, not promoted.

**Suggested disposition:** `soft-polish` — candidate for an editorial pass clarifying expected-vs-realized in the Discussion. Distinct from MI per se; not a defect but worth surfacing because the prose-vs-formalism distinction propagates if downstream segments treat $\mathcal I(e_\tau)$ as realized content. Not spike-shaped; not a graduation blocker.

### Fresh-3. Stale "Section IV / AAD-FULL.md" migration language in `#form-event-driven-dynamics`

Segment 14 (`14-form-event-driven-dynamics.md:23-28`) — the segment's software discussion says the three-part tempo decomposition is "a Section IV gap" and refers to `AAD-FULL.md`. The current repo has TST as `02-tst-core/`, not AAD Section IV, and `AAD-FULL.md` doesn't exist in root orientation. Stale migration language.

**Suggested disposition:** `actionable-open` (light editorial / verification). Could be a one-shot grep-and-fix across segments for stale Section IV / AAD-FULL references. Not graduation-blocking but the kind of doc-rot that accumulates if not periodically swept.

### Fresh-4. Initial priors / pretrained structure not explicitly placed in `#form-agent-model`

Segment 10 (`10-form-agent-model.md:8-19`) — the auditor: "*This segment partially addresses the 'everything known comes from chronica' concern by making $M_t$ the complete retained epistemic state. But it does not explicitly place initial priors, pretrained weights, innate model class structure, or inherited architecture. Those can be hidden in $\phi$ and $\mathcal M$, but readers may need that said. Otherwise, logogenic and biological cases look under-described: a current LLM's model quality is mostly in pretrained parameters, not only 'context window contents plus retrieved memory.'*" Proposed clarification: $M_t = \phi(M_0, \mathcal C_t)$ or state that $M_0$ / model class is absorbed into $\phi$ and $\mathcal M$.

The auditor explicitly didn't promote — "possible clarification, not a finding yet."

**Suggested disposition:** `soft-polish` / candidate for `03-llm-core` framing material. *Especially relevant to logogenic agents* — a current LLM's model quality is mostly in pretrained parameters; a chronica-only framing under-describes the substrate. This is a candidate Brief / framing-level observation for the logogenic component when it matures. Cross-references the `03-llm-core/` register-openings work (see MEMORY's `project_modularity_state_dynamics_register_openings.md`).

### Fresh-5. PID/thermostat scope tension in `#form-agent-model`

Segment 10 (`10-form-agent-model.md:18-23`) — the segment's Discussion says a PID controller's $M_t$ is "too impoverished to support the adaptive dynamics of Section I," but orientation material and earlier scope discussions include PID controllers / thermostats as adaptive examples. The auditor flagged as a cross-segment consistency watch item.

**Suggested disposition:** `soft-polish` — could be addressed by a half-sentence clarifying whether PID is a degenerate-edge instance still fitting the machinery, or genuinely outside Section I's substantive content. Not promoted as a finding; light editorial.

### Fresh-6. "Agent knows neither $h$ nor distribution of $\varepsilon_t$ exactly" over-strong for known-Kalman cases

Segment 2 (`02-def-observation-function.md:9-15`) — the auditor: "*If taken literally as constitutive, this excludes common control / filtering cases where the observation operator or noise model is specified well enough for exact Kalman analysis. The framework may intend 'the agent lacks direct access to $\Omega_t$ and may have model uncertainty over $h$ or noise'; this segment says something stronger.*" Watch item; auditor noted later segments may relax this or treat known-$h$ cases as idealized instantiations.

**Suggested disposition:** `soft-polish` — minor scope-language adjustment. Distinguish "agent lacks direct access to $\Omega_t$" (the constitutive boundary) from "agent doesn't know $h$ or noise distribution exactly" (an additional epistemic-opacity commitment). Not a defect but worth tightening.

### Fresh-7. CIY zero-by-convention for passive observers

Segment 21 (`21-def-causal-information-yield.md:22-26`) — the segment claims "CIY $= 0$ for a passive observer," but the auditor notes this is a convention (passive observers lack the action/comparator distribution needed for the definition). Similarly, "CIY $\gt 0$ when actions causally alter what is observed" requires $q$ to put positive mass on alternatives whose distributions differ. The segment later acknowledges dependence on $q$, but the boundary statements could be tightened.

**Suggested disposition:** `soft-polish` — minor precision. Distinct from F8's well-definedness clause (different segment, different mechanism). Worth tightening the boundary-value statements with explicit scope when CIY is well-defined.

### Fresh-8. Predictive-power asymptotic vs current-empirical in `#def-model-class-fitness`

Segment 13 (`13-def-model-class-fitness.md:18-22`) — the auditor: "*'The gap … cannot be closed by better parameter estimation, more data, or longer training within the current class' is true if $\mathcal F$ is defined against the true data-generating process / asymptotic information available to the class. If $\mathcal F$ is computed relative to the current finite chronica, more data can change the relevant predictive-information landscape.*" Probably resolved downstream by `result-structural-adaptation-necessity`, but the definition could distinguish current empirical estimate from asymptotic class ceiling.

**Suggested disposition:** `soft-polish` — minor clarification of $\mathcal F$'s trajectory/policy/horizon relativity (the auditor's specific proposed line: "*relative to the same chronica, horizon, and generating policy as $S$*"). Light editorial.

### Fresh-9. Action-contingent observations vs causal-downstream-weighting in `#post-causal-structure`

Segment 8 (`08-post-causal-structure.md:25-30`) — *"The model should give more weight to observations that are causally downstream of the agent's actions" may overstate the relationship between interventional status and evidential reliability. Action-contingent observations can be high-CIY, but they can also be noisy or biased. This sentence probably becomes true only when weighted by CIY / uncertainty, not merely causal downstreamness.* Watch item, not promoted.

**Suggested disposition:** `soft-polish` — minor scope-tightening on the causal-downstream-weighting framing. Light editorial.

### Fresh-10. Bareinboim strict-hierarchy claim as Phase-3 citation-verification candidate

Segment 9 (`09-def-pearl-causal-hierarchy.md:30-31`) — flagged as "*candidate for sample citation verification later*" (the strict-hierarchy claim from Bareinboim et al.). Not promoted in this audit; Phase-3 work explicitly deferred.

**Suggested disposition:** `subsumed-by-Phase-3` (deferred external citation verification). Not unique to this dir; consistent with broader Phase-2/3 citation discipline tracked across cycles. Lives in the broader Phase-3 backlog if/when external citation verification cycles occur.

### Fresh-11. `git checkout` as Level 3 access — TST scope-narrowing watch item

Segment 9 (`09-def-pearl-causal-hierarchy.md:32-36`) — "*`git checkout` provides Level 3 access with ground-truth verification' is plausible for code behavior under tests, but not necessarily for product/user outcome counterfactuals. If this appears as a canonical TST claim, it may need scope narrowing.*" Watch item for when the audit reaches TST.

**Suggested disposition:** `subsumed-by-MANIFEST` — per MANIFEST 2026-05-16 Cluster B "SN-3 (`def-pearl-causal-hierarchy` bald `git checkout`→L3) | **resolved by strengthening** — scoped to the α/β/γ regime, downstream-deferred; landed `3072667` + `2666eca` (parent co-owner direct-fix), parent-verified." This is a clean cross-cycle resonance: 742613's watch item became the SN-3 finding that landed via parent co-owner direct-fix.

### Fresh-12. Open-questions sections in `claims-verified` segments — convention drift watch

Segments 20 (`20-emp-update-gain.md:35-37`) and 25 (`25-der-deliberation-cost.md:30-32`) — both `claims-verified` segments carry reader-facing "Open questions" sections not under Working Notes. The auditor: "*This may be intentional scope honesty rather than Working Notes, but repeated open-question sections in verified segments blur the project convention slightly.*"

**Suggested disposition:** `process/instruction-feedback` (FORMAT convention) — minor. If the convention is that promoted/verified segments should still carry forward-pointing open questions in a dedicated section (rather than only in Working Notes), it should be named explicitly in FORMAT.md. Otherwise the convention drifts on a segment-by-segment basis. Not graduation-blocking.

### Fresh-13. Possibility-of-action-without-observation-effect in `scope-agency`

Segment 5 (`05-scope-agency.md:25-30`) — the auditor noted the scope condition uses observation distributions $P(o|do(a))$ rather than state transitions $P(\Omega_{t+1}|do(a))$. "*That choice is defensible because AAT is observation-mediated, but it means actions that affect hidden state without any observation contrast are outside agency for AAT's purposes. That may be intended; if not, downstream causal machinery should clarify 'observable causal effect' vs 'environmental causal effect.'*"

**Suggested disposition:** `soft-polish` / candidate `disc-*`-level discussion — the observable-causal-effect-vs-environmental-causal-effect distinction is a candidate Brief field or short Discussion paragraph. Worth surfacing in `scope-agency` Discussion if not already there.

### Fresh-14. Continuous-coupling caveat from Attack 2 should be more visible in `#der-recursive-update`

Segment 16 (`16-deriv-recursive-update.md:20-26`) — Attack 2 of the appendix derivation surfaces a genuine limitation: continuous environmental influence is outside the event-driven formulation, with the more general form $\dot M = g(M, u)$. The auditor: "*The main segment's between-event corollary $dM/d\tau = g_M(M_\tau)$ should probably carry the same caveat more prominently.*"

**Suggested disposition:** `soft-polish` — main-segment-visibility of the continuous-coupling caveat. Light editorial.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes ~50 falsifiable predictions across §I/§II/§III/appendices/TST/logogenic/logozoetic, plus open-gap predictions, overclaim predictions, "most novel if it holds" candidates, and expected finding-type distribution. The per-segment reflections and strategic-revision files test these against evidence — partially, because coverage was Section-I-only. The calibration record:

### Predictions correctly anticipated (the framework matched the prior)

- **§I cleanest layer prediction** ✓ (segment 1-7, with caveats). The conceptual hierarchy is clear, but the *dependency-cadence level* was not as clean as predicted — the 10-segment strategic revision explicitly named this: "*The initial prediction that Section I would be cleanest was too optimistic at the dependency-cadence level.*"
- **Active sensing built in to `#def-observation-function`** ✓ (segment 2) — predicted; confirmed.
- **`scope-adaptive-system` broad inclusion by observation + residual uncertainty** ✓ (segment 4) — confirmed structurally; with the unexpected primitive-drift issue (F7).
- **`scope-agency` interventional contrast via $|\mathcal A|\geq 2$** ✓ (segment 5) — confirmed.
- **Pearl hierarchy mapping in `#def-pearl-causal-hierarchy`** ✓ (segment 9) — confirmed as adopted prior art with availability-vs-exploitation nuance.
- **`#der-recursive-update` among strongest formal results** ✓ (segments 15-16) — confirmed; the Doob-Dynkin formalization is strong, the seven-attack defense is honest, with status-language harmonization caveat.
- **`#emp-update-gain` empirical with Kalman / conjugate cases exact** ✓ (segment 20) — confirmed.
- **`#hyp-mismatch-dynamics` heuristic / fluid-limit** ✓ (segment 23) — confirmed; honest at `type: hypothesis`, `status: heuristic`.
- **Sector-condition / persistence machinery exact conditional on sector condition** ✓ (segments 24, 26-30) — confirmed *with* the F2 caveat that Model-S non-exit was overclaimed (now resolved by strengthening-then-no-go).
- **`#result-structural-adaptation-necessity` could overclaim necessity** ✓ (segment 31) — *prediction correct on shape, segment more careful than expected*: the segment honestly carries the alignment assumption and proper-scoring regret fallback.
- **`#form-consolidation-dynamics` draft / status pressure** ✓ (segment 33) — confirmed; canonicalization issue identified.

### Predictions confirmed substantively more than expected (positive surprises)

- **`#deriv-sector-condition` proof discipline** — predicted as "exact conditional on sector condition"; got A.1 (Lyapunov ultimate-boundedness) + A.1S region-aware four-sub-result form + Corollary A.1S.1 dichotomy + the dedicated no-go appendix (`#deriv-stochastic-non-exit`) once the F2 strengthening landed. The auditor's positive recalibration on the appendix at segment 24 (before catching the F2 issue): "*This appendix proves the sector-condition Lyapunov bounds … The deterministic Lyapunov proof (Prop A.1) looks sound under local A2', bounded disturbance, and initial condition inside $\mathcal B_R$. The adaptive reserve formula $\Delta\rho^\ast = \alpha R - \rho$ is a direct corollary and checks out.*"
- **`#deriv-recursive-update` appendix discipline** — predicted as "mostly sound"; got the appendix that "*is stronger and more honest than the main segment summary*" (segment 16), with explicit eliminative-vs-definitional decomposition and the Doob-Dynkin formalization. The auditor's calibration shift: "*The 'uniqueness' claim is valid in a representation-theoretic sense, not in an independently discovered dynamics sense. The appendix acknowledges this … That makes the result exact under the modeling commitment, but it should not be oversold as a physical theorem about all possible cognitive architectures.*"

### Predictions confirmed in less-strong form (negative calibration)

- **`#form-information-bottleneck` overclaim** — predicted possible status mismatch if labeled too strongly. **Direction-right but editorial-not-foundational**: the segment's prose Epistemic Status disambiguates tiers honestly, the auditor explicitly *didn't* promote (BP3 above). Cross-cycle convergence with 613842 Fresh-1.
- **`#post-composition-consistency` axiomatic / scale-invariance with overclaim vulnerability** — predicted. *Partially confirmed*: the segment was found to be doing more than the audit instructions warranted for a postulate (importing Section III machinery), but the core scale-invariance claim itself was not overclaimed; the issue was canonicalization (F6) not over-claim.
- **`#emp-update-gain` "any optimal adaptation process must approximate this functional dependence" overclaim** — predicted (segment 20 `20-emp-update-gain.md:20-23`). **Direction-right at the prose level**: the auditor flagged the "Any optimal adaptation process must approximate this functional dependence" sentence as overclaim, but didn't promote because the robust-qualitative status + open-questions framing soften it enough. Watch item.

### Predictions that proved correct but mid-process repositioned

- **`def-mismatch-signal` score-function** — *not predicted to have a sign error* (the prediction was for sector / persistence machinery to carry the math errors). The score-sign error was a positive-locus shift: a stronger math finding than predicted, in a *primitive-definition* segment rather than a *derivation* segment. Direction-wrong, severity-stronger.
- **Adaptive tempo definitional issue (F4)** — *not specifically predicted*. The F4 status-vs-scope mismatch was a positive-locus shift: predicted finding-types included "Status-label mismatches: `exact` where conditional / formulation / hypothesis would be more honest," and F4 is exactly this type, but the prediction didn't name `def-adaptive-tempo` as a specific candidate.
- **Gradient equivalence overclaim (F3)** — *partially predicted under "overclaim if not appropriately scoped"* but not specifically anticipated as `iff` overclaim. The audit's positive contribution: identifying *exactly which mathematical direction* fails (one-point ⇒ strong convexity is false; the other direction holds).

### Predictions about open gaps

The auditor's open-gap predictions (`00-initial-predictions.md:237-262`):
- **General contraction from sector-bounded correction** — predicted as "probably not proved if composition closure relies on it." Coverage was Section-I-only; not directly tested. Cross-references SP-21 and F-V3/F8 cluster.
- **Directed separation for transformer-style agents unavailable; logogenic coupled dynamics likely not yet mathematically mature** — predicted. Coverage was Section-I-only; not directly tested.
- **Finite-sample identifiability for strategic edge updates incomplete** — predicted. Coverage Section-I-only; not directly tested.
- **N-agent scaling and endogenous coupling in composition gaps by outline admission** — predicted; not directly tested.
- **TST empirical claims lack full validation in canonical src** — predicted; not directly tested.
- **Logozoetic formalization absent** — predicted; structurally confirmed by the canonical outline (logozoetic component is future work).

### Predictions about overclaim (`00-initial-predictions.md:264-282`)

- **"Agentic" as formal action-intervention boundary vs richer goal/model/adaptation agency** — predicted as overclaim risk. *Direction-right at the primitive level*: F7 carries this exactly (the primitive `def-agent-environment` is action-coupled, while scope is broader).
- **Universal update gain from uncertainty ratio outside Kalman / gradient / variational cases** — predicted. Direction-right (segment 20 watch item) but not promoted (robust-qualitative status soft-handles it).
- **Continuous-time mismatch ODE treated as exact when it is fluid-limit approximation** — predicted; *not confirmed*: `#hyp-mismatch-dynamics` is honest at `status: heuristic`.
- **Strategy DAG uniqueness if cycles handled by time-unrolling** — predicted; not tested (Section-II-only).
- **Edge-update validity under correlated failures / latent common causes** — predicted; not tested.
- **Composite-agent closure if projection admissibility and contraction assumptions insufficient** — predicted; not tested.
- **Logogenic "language as encoded reasoning" as more than hypothesis** — predicted; not tested.
- **TST least-time optimality if "equivalent outcomes" underspecified** — predicted; not tested.

### The auditor's predictive shape

Same general pattern as 613842 (cross-cycle convergence on predictive-shape level):
- **Component-level accuracy** — predictions about *what kind of issue each component would have* were strongly accurate for Section I (the predicted finding-types — dependency-order failures, missing dependencies, status-label mismatches, scope-propagation failures, mathematical edge-cases — all surfaced).
- **Specific-locus accuracy** — predictions about *which exact segments* would carry the issues were less accurate. F1 (score sign) was in a primitive-definition segment, not the persistence machinery. F2 (Model-S non-exit) was in the appendix as predicted but the *specific structure* (fixed-time vs ever-exit confusion) wasn't anticipated.
- **Severity-direction accuracy** — the actual findings were generally **more severe** than predicted at the math level (F1 sign error, F2 ever-exit conflation, F3 false iff are all true math errors, not just editorial issues), and **less severe** at the integration-debt level for the parts of the corpus the audit reached.

### Withdrawn-candidate trail (strengthen-before-soften / verification discipline internal to the audit)

Three candidates the auditor surfaced and *did not promote* under burden of proof — useful pedagogical instances of audit-internal discipline:

- **`#emp-update-gain` "any optimal adaptation process must approximate this functional dependence" overclaim** (segment 20) — surfaced as overclaim watch item, *not promoted* because the segment's robust-qualitative status + open-questions framing softens the claim adequately. The watch item is recorded so future agents don't re-flag.
- **`#form-information-bottleneck` mixed-tier compression** (segment 11) — surfaced as status-label pressure point, *not promoted* because the Epistemic Status paragraph disambiguates tiers in prose. Cross-cycle convergence with 613842 Fresh-1; both auditors landed the same observation and both honestly didn't promote.
- **Open-questions sections in `claims-verified` segments** (segments 20, 25) — surfaced as convention-drift observation, *not promoted* because the convention may be intentional. FORMAT-discipline question rather than a defect.

These withdrawn-trails are pedagogically important: they show the *burden-of-proof bar* operating at candidate-promotion stage, not just at routing-stage downstream. The Phase-2 SUPPLEMENT triage vocabulary (the new / known-unintegrated / known-resolved / tooling-gap / scope-status-mismatch enum) makes this discipline explicit as a downstream pass; the WORKING-dir candidate-promotion stage is where it *first* operates.

---

## Part V — Wandering thoughts / methodology themes, theme-grouped

This WORKING dir does **not** carry a `§14 Wandering Thoughts and Ideation` register in the explicit sense the 471203 cycle did. Like 613842, the per-segment reflections are tight burden-of-proof discipline; ideation is short, instrumental ("Prediction for next segment"; "Running report update"), and embedded inline. This dir's distinctive methodology signature is **per-batch strategic revisions** that operate the candidate-finding ledger across the walk, plus the **Phase-2 SUPPLEMENT** that originated the durable triage vocabulary. Themes:

### Theme A — The 10/20/30 strategic-revision cadence as a methodology pattern

The auditor wrote per-batch strategic revisions at 10, 20, and 30 reflection files (`10-strategic-revision.md`, `20-strategic-revision.md`, `30-strategic-revision.md`). Each:
1. Lists the high-priority candidate findings from the preceding batch
2. Compares against initial predictions (calibration shifts)
3. Names process-level adjustments (e.g., 10-revision: "*avoid over-reporting every downstream reference as a finding*")
4. Re-tunes audit strategy going forward

This three-checkpoint cadence is methodologically distinctive. It operationalizes Joseph's `metacognitive todo pattern` (using checkpoints as metacognitive triggers, not just task tracking) in audit form. Each revision served as a re-orientation event that prevented drift and surfaced cross-segment patterns earlier than a single end-of-audit synthesis would have.

**Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` §4 or §5 revision. The per-batch strategic-revision cadence (every 10 segments / every N batch checkpoint) is a transferable methodology contribution. Could be named explicitly as an expected pattern.

### Theme B — The Phase-2 triage vocabulary as the durable methodology contribution

Already detailed in BP10. Worth re-surfacing here in the methodology themes layer: the auditor's framing of Phase-2 was not "verify findings against tracking" but "*classify findings by their relationship to existing tracking*." The vocabulary (new / known-unintegrated / known-resolved / tooling-gap / scope-status-mismatch) makes this classification first-class.

The framing matters: without it, an auditor either (a) over-classifies every finding as new (treating rediscovery as fresh contradiction — the failure mode the audit's own FINAL §"Phase 2 Process Feedback" warns about), or (b) under-classifies by dropping findings that have *some* tracking even though the offending segment is still wrong. The five-category vocabulary lets *each category* graduate to its own routing-tracker disposition.

**Suggested disposition:** `superseded-by` the routing-tracker enum (per P-block). The vocabulary lives on as the conceptual ancestor of the disposition system. Worth recording the lineage for future revisions.

### Theme C — Counterevidence search as the candidate-promotion gate

Each candidate finding in the 742613 WORKING dir carries an explicit **counterevidence search** step. Visible in:
- Segment 18 (score sign): checked downstream propagation through `result-mismatch-decomposition`, `emp-update-gain`, gain-sector bridge, gradient-equivalence segments before promoting.
- Segment 24 (Model-S non-exit): checked the linear scalar special case ⇒ counter-evidence for the ever-exit claim is mathematical, not just rhetorical.
- Segment 27 (gradient equivalence): *constructed a counterexample* ($L'(x) = x(1+\tfrac12\sin(10x))$) as part of the candidate-promotion process.
- Segment 22 (adaptive tempo): cross-checked against `result-persistence-condition` Discussion caveat.
- Cross-segment counterevidence: segment 27 noted `result-sector-persistence-template.md:72` correctly describes the one-point sector condition's weakness — *the framework's own self-knowledge supports the finding*.

This is parallel to 613842's Theme B but operates *with stronger math construction*: when the finding is math-flavored (sign error, ever-exit, false iff), the auditor *built the explicit counterexample / counter-derivation* before promoting. Not just "I doubt this"; "*here is the explicit object that refutes it.*"

**Suggested disposition:** `process/instruction-feedback` — material for explicit callout in `doc/de-novo-audit-instructions.md`: when the candidate-finding is math-flavored, the burden-of-proof bar is "construct the explicit counterexample," not just "argue the claim is suspect." 742613's worked examples (the OU recurrence calc, the sin-perturbed gradient field) are durable training material.

### Theme D — Audit-instructions-vs-CLAUDE.md conflict as instruction-set bug-surface

The auditor (Codex) opened with `00-initial-predictions.md:11-12` and `00-running-outline.md:30-31` both logging the CLAUDE.md↔TODO conflict explicitly. The auditor's framing: this is an *instruction-set bug-surface*, not a personal disposition question — future agents working from these instructions need clarity on which document wins.

Distinctive about this framing: the conflict is treated as a *durable instruction-set issue* rather than an artifact of the specific audit. The auditor recommends a one-line override in `doc/de-novo-audit-instructions.md` so the conflict is named once and resolved permanently for future de-novo audits.

**Suggested disposition:** `process/instruction-feedback` — already carried in P-block; cross-references 613842 BP6 (similar CLAUDE.md-bleed observation from a different angle). The 2026-05-19→20 active-reconsideration callout on CLAUDE.md addresses part of this from the CLAUDE.md side; the audit-instructions side may still need its own callout.

### Theme E — Body-level lint gap as durable tooling-gap

Surfaced via Phase-2 SUPPLEMENT §6 (BP8 / machine-check helper). The current `bin/lint-outline` reports 0 ordering violations and 0 missing dependencies — *cleanly* — even though the F6 cluster identifies multiple body-level hidden dependencies, wrong links, and non-proof appendix imports that the lint doesn't inspect. This is a structural tooling-gap: the lint contract is frontmatter-graph-only, not body-level.

The auditor's specific recommendations:
1. Add a second lint mode for body-level canonical symbols and slug links (catches the F6 sub-issues).
2. Split backmatter references into proof-only vs conceptual/meta appendices (catches the `disc-compression-operations` class).
3. Promote specific wrong-link and hidden-dependency cases into TODO or a small cleanup batch.

**Suggested disposition:** `actionable-open` (tooling-gap) — `bin/lint-outline` enhancement. The first recommendation (body-level slug/symbol lint mode) is genuinely durable infrastructure work; not a graduation-blocker but real durability improvement.

### Theme F — Codex-environment scope-feasibility tension

The auditor wrote from Codex, with limited multi-turn budget. FINAL §"Process Feedback" point 1: *"The strongest process tension is scope feasibility. The instructions are written for a very large context and a long-running audit. In this Codex environment, following the cadence faithfully through the whole framework would be a multi-turn effort.*" The honest-partial-pass discipline operated: the auditor explicitly stopped at the end of Section I rather than degrading to skim-coverage for the rest.

**Suggested disposition:** `process/instruction-feedback` — partial-pass protocol (BP5). The honest-partial-coverage pattern is also a strength: 742613's eight findings (mostly resolved-by-strengthening per MANIFEST) are all from a partial pass that disciplined itself to depth-over-breadth.

### Theme G — The "audit as logocentric instance of the theory" framing (subtle, not explicit here)

The 742613 dir doesn't explicitly invoke `doc/de-novo-audit-instructions.md` §2's "audit as logocentric instance of the theory" framing. But the pattern *operates* in the audit's cognition:

- Segment 18 (score sign): the auditor's body-signal "*this object's prose says X, its formula says not-X*" is exactly the form-shaping-for-verification move the framework's own scope-honesty discipline operates by. The audit is doing locally what the theory does globally.
- Segment 24 (Model-S non-exit): the auditor's reach toward "*what is the cleanest mathematical object this segment seems to be reaching for, and does it exist?*" is the strengthening-direction move that the framework's strengthen-before-soften discipline names. The audit is, at the moment of catching the bug, doing exactly the cognitive operation the framework asks for.
- Segments 10/20/30 strategic revisions: the explicit re-orientation events parallel the framework's Orient cascade — observation → model update → strategy revision → feasibility re-check.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md` §2. The framing operates whether or not the auditor names it. Naming it explicitly may help calibrate future agents toward the body-signals of the discipline.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` I (extraction agent) read first-hand. Per-finding disposition using `doc/audit-routing-instructions.md` §8 enum. Honest "deferred" allowed.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1 (score-function sign) | `subsumed-by-FINAL — resolved (direct fix)` | **First-hand verified** `01-aat-core/src/def-mismatch-signal.md:30-37`: sign fix landed as the SUPPLEMENT §1 recommended form ($\tilde\delta_t = \nabla_M\log P$, no minus); prose now consistent with formula. |
| F2 (Model-S non-exit) | `subsumed-by-MANIFEST — resolved by strengthening-then-no-go` (state 3) | **First-hand verified extensively** — the load-bearing trail. Read `01-aat-core/src/deriv-sector-condition.md:175-302` first-hand: Prop A.1S region-aware four-sub-result form (i)/(ii)/(iii′)/(iv) landed with explicit prose at line 198 naming the no-go; Corollary A.1S.1 (containment dichotomy) at lines 258-268 stated as new exact result with $\alpha$-invariant 2-point set $\{0,1\}$; Summary of Results table at line 276 carries the Cor A.1S.1 row; What Is Derived vs Chosen table at line 294 carries Cor A.1S.1 as "**Proved** — new exact result." Read `01-aat-core/src/deriv-stochastic-non-exit.md` lines 1-25 first-hand: header states the no-go cleanly, Theorem (Model-S no-go) stated *[Derived]*. The strengthen-before-soften discipline operated correctly: refuted ever-exit claim deleted, the no-go demonstrated as present truth (not softened ghost), cascade clean. Cross-cycle 742613-F2 ≡ 613842-F2. |
| F3 (gradient equivalence iff) | `subsumed-by-MANIFEST — resolved by strengthening (B.4 split)` | **First-hand verified** `01-aat-core/src/deriv-gain-sector.md:127-188`: Prop B.4 split into B.4-i (one-point ⇐ strong convexity, one direction only) and B.4-ii (two-point ⇔ strong convexity, full equivalence); the auditor's counterexample $L'(x) = x(1 + \tfrac12\sin(10x))$ landed verbatim at line 161; line 169 names where each direction applies in AAT (one-point for `#deriv-sector-condition` Lyapunov persistence; two-point for `#form-composition-closure` bridge lemma DA2'-inc). Secondary Poisson Fisher fix also verified at line 188 (compact-scope-on-interior framing). Strictly stronger than the audit's ask. |
| F4 (adaptive tempo `exact` status) | `subsumed-by-MANIFEST — substance resolved by strengthening; narrow frontmatter residue TODO:395/126` | **First-hand verified** `01-aat-core/src/def-adaptive-tempo.md` lines 1-65: tensor extension under Fisher-local invariance regime landed (lines 28-38) as the canonical matrix-Loewner object; scalar form recovered as shared-eigenbasis collapse special case; line 44 Epistemic Status explicitly names the scope dichotomy; line 63 Discussion points to `#deriv-matrix-persistence-condition` as canonical, scalar form as diagonal-axis-aligned special case. Frontmatter `status: exact` (line 4) and Formal Expression leading with scalar form (line 19) is the narrow TODO:395/126 residue — not graduation-blocking. Cross-cycle 742613-F4 ≡ 613842-F1. |
| F5 (`a_t = \pi(M_t)` scope) | `subsumed-by-MANIFEST — resolved by strengthening / lift-statement` | **First-hand verified** `01-aat-core/src/der-action-selection.md`: line 19 retains the Section I form; line 29 carries the explicit Section II lift paragraph (same completeness argument applied to $X_t$); line 33 Epistemic Status states the scope explicitly; line 51 Discussion §"Connection to Section II" unpacks the actuated form. Completeness-argument unification per MANIFEST operates here cleanly. |
| F6 (canonical order / depends-graph) | `subsumed-by-FINAL — mostly resolved; Pearl-`do` residue is duplicate of 471203 §B F6 → FORMAT-TODO C12` | **First-hand verified** five sub-issues: `scope-adaptive-system.md:8` carries `def-chronica` dep (resolved); `scope-agency.md:24` still has Pearl `do` with parenthetical-cite-without-dep (FORMAT-TODO C12 residue, duplicate routing); `form-event-driven-dynamics.md:9` carries `form-agent-model` dep (resolved); `hyp-mismatch-dynamics.md:54` link correctly `[#deriv-discrete-sector-condition](deriv-discrete-sector-condition.md)` (resolved); `bin/lint-outline` body-level gap is durable tooling-gap (P-block / Theme E). |
| F7 (passive-observer primitive drift) | `subsumed-by-FINAL — known conceptual tension, integration debt; tracked 471203 §F-A cluster + PROPOSALS SP-6` | **First-hand verified** `01-aat-core/src/def-agent-environment.md:11-23`: primitive definition still leads with "produces actions that affect the environment" — the structural-restructure proposed by SUPPLEMENT §7 has not yet executed in this primitive segment. Prose-side repair downstream (`scope-adaptive-system` Discussion + `post-causal-structure` + `def-agent-spectrum`) handles the conceptual hierarchy; the primitive segment is the editorial-interim residue. |
| F8 (model-sufficiency well-definedness) | `subsumed-by-MANIFEST — resolved (well-definedness clause)` | **First-hand verified** `01-aat-core/src/def-model-sufficiency.md:26-35`: well-definedness clause `I(\mathcal C_t; o_{t+1:\infty}|a_{t:\infty}) > 0` landed cleanly with the substantive epistemic framing ("*predictive sufficiency is a property of a prediction task; there is no prediction task to be sufficient for*"); boundary values carry "(assuming the well-definedness clause holds)"; downstream propagation to `#def-model-class-fitness` and `#result-structural-adaptation-necessity` explicitly named. Strengthening direction chosen over the convention path. |

### Part II findings (bigger-picture observations)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| BP1 (recursive-update status harmonization) | `subsumed-by-FINAL "Other Observations"` | Did not separately re-read `01-aat-core/src/der-recursive-update.md` frontmatter / Epistemic Status to confirm harmonization. **Deferred — light editorial check.** |
| BP2 (spike refs outside Working Notes) | `subsumed-by-FINAL "Other Observations"` — project-wide cleanup material | Confirmed multiple instances per WORKING dir auditor reading. Did not run cross-corpus grep. **Deferred — light cleanup cycle.** |
| BP3 (IB mixed-tier compression) | `subsumed-by-FINAL "Other Observations"` (auditor explicitly didn't promote) + cross-cycle convergence with 613842 Fresh-1 | Did not separately re-read `01-aat-core/src/form-information-bottleneck.md`. **Deferred — minor editorial work; possibly strengthening direction available.** |
| BP4 (arg-sup attainment) | `subsumed-by-FINAL "Other Observations"` — minor precision | Did not separately re-read `01-aat-core/src/result-structural-adaptation-necessity.md`. **Deferred — light editorial.** |
| BP5 (partial-pass protocol) | `process/instruction-feedback` — P-block | Carried in `audits/polish-and-sentiment-ledger.md` P-block (verified). |
| BP6 (appendix-exception tightening) | `process/instruction-feedback` — P-block | Carried in P-block. The three-way distinction (proof / meta-pattern / downstream non-appendix) is durable methodology material. |
| BP7 (CLAUDE.md↔TODO conflict override) | `process/instruction-feedback` — P-block | Carried in P-block. Cross-cycle with 613842 BP6. |
| BP8 (machine-check helper) | `process/instruction-feedback` + `actionable-open` (tooling-gap) | Carried in P-block. The body-level lint mode is the genuinely durable tooling work. |
| BP9 ("consider writing" too soft) | `process/instruction-feedback` — P-block | Carried in P-block. Light editorial fix. |
| BP10 (Phase-2 triage vocabulary) | `superseded-by` the routing-tracker enum (P-block; **absorbed, not open**) | The durable methodology contribution from this dir. Verified the routing-tracker enum used throughout the disposition column above. |

### Part III findings (genuinely fresh)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (action-fluency formal marker conflation) | `research-seed` — possible `impl-*` chapter-end material | Did not separately re-read `01-aat-core/src/der-action-selection.md` and `der-deliberation-cost.md` for the action-fluency framing in current `src/`. **Deferred — research-seed; spike-shaped.** |
| Fresh-2 (MI vs realized-surprisal in event info) | `soft-polish` — light editorial | Did not separately re-read `01-aat-core/src/form-event-driven-dynamics.md`. **Deferred — light editorial.** |
| Fresh-3 (stale Section IV / AAD-FULL.md language) | `actionable-open` (verification / one-shot grep + fix) | Did not run cross-corpus grep for "Section IV" / "AAD-FULL.md" references. **Deferred — one-shot editorial sweep.** |
| Fresh-4 (initial priors / pretrained structure in `form-agent-model`) | `soft-polish` / candidate `03-llm-core` framing | Did not separately re-read `01-aat-core/src/form-agent-model.md`. **Deferred — substantively relevant for logogenic agents; surface to Joseph if priority.** |
| Fresh-5 (PID/thermostat scope tension) | `soft-polish` — half-sentence clarification | Did not separately re-read `01-aat-core/src/form-agent-model.md` Discussion section. **Deferred — light editorial.** |
| Fresh-6 (over-strong epistemic opacity in `def-observation-function`) | `soft-polish` — minor scope-language adjustment | Did not separately re-read `01-aat-core/src/def-observation-function.md`. **Deferred — light editorial.** |
| Fresh-7 (CIY zero-by-convention for passive observers) | `soft-polish` — boundary-value precision | Did not separately re-read `01-aat-core/src/def-causal-information-yield.md`. **Deferred — light editorial.** |
| Fresh-8 (asymptotic vs current-empirical in `def-model-class-fitness`) | `soft-polish` — clarification of $\mathcal F$ relativity | Did not separately re-read `01-aat-core/src/def-model-class-fitness.md`. **Deferred — light editorial.** |
| Fresh-9 (causal-downstream weighting in `post-causal-structure`) | `soft-polish` — scope-tightening | Did not separately re-read `01-aat-core/src/post-causal-structure.md`. **Deferred — light editorial.** |
| Fresh-10 (Bareinboim strict-hierarchy citation) | `subsumed-by-Phase-3` (deferred citation verification) | Citation work outside the audit's scope; Phase-3 backlog. No verification needed in this pass. |
| Fresh-11 (`git checkout` as L3 / TST watch) | `subsumed-by-MANIFEST` — SN-3 resolved by strengthening (`3072667` + `2666eca`) | Resolved per MANIFEST Cluster C; watch-item operated as cross-cycle anticipation; landed via parent co-owner direct-fix. No further work. |
| Fresh-12 (open-questions sections in `claims-verified`) | `process/instruction-feedback` (FORMAT convention) — minor | Did not check whether FORMAT.md names the convention. **Deferred — light editorial / FORMAT clarification.** |
| Fresh-13 (observable vs environmental causal effect in `scope-agency`) | `soft-polish` — candidate Discussion paragraph | Did not separately re-read `01-aat-core/src/scope-agency.md` Discussion. **Deferred — light editorial.** |
| Fresh-14 (continuous-coupling caveat visibility) | `soft-polish` — main-segment visibility | Did not separately re-read `01-aat-core/src/der-recursive-update.md`. **Deferred — light editorial.** |

### Part IV (predictions register) and Part V (wandering thoughts / methodology)

Not "findings" with `src/`-level dispositions — cognition-flow material:

- **Predictions register (Part IV)** — read first-hand against the auditor's per-segment reflections + strategic revisions. The auditor's calibration record is honest: most direction-level predictions confirmed; specific-locus predictions adjacent-but-not-exact; the score-sign error was a positive-locus surprise (stronger math finding in a primitive-definition segment than predicted in the appendix machinery). No additional `src/` verification needed for the record itself.
- **Wandering thoughts / methodology (Part V)** — Themes A through G are methodology observations. **A, B, C, D, F, G** are `process/instruction-feedback` (material for `doc/de-novo-audit-instructions.md` and `doc/audit-routing-instructions.md` revisions). **E** is `actionable-open` (`bin/lint-outline` enhancement, body-level lint mode). Theme B (Phase-2 triage vocabulary) is the durable methodology contribution and is `superseded-by` the routing-tracker enum.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 39 files read in full or substantively first-hand. The `00-initial-predictions.md` (~325 lines), `00-running-outline.md`, 10/20/30 strategic revisions, and segments 01-08 / 10-18 / 19-31 / 33-34 read with full depth; segments 32 (`der-temporal-nesting`) lighter-sampled (auditor's reading found "no finding; temporal nesting is honestly scoped"). The strategic-revision files were the key navigational artifacts.

**Read first-hand from `src/` for verification:**
- `01-aat-core/src/def-mismatch-signal.md:30-37` (F1 verification — sign fix)
- `01-aat-core/src/deriv-sector-condition.md:175-302` (F2 verification — Prop A.1S four-sub-result form, Cor A.1S.1, Summary table, Derived-vs-Chosen table)
- `01-aat-core/src/deriv-stochastic-non-exit.md:1-25` (F2 no-go appendix verification)
- `01-aat-core/src/deriv-gain-sector.md:127-188` (F3 verification — B.4 split + Poisson Fisher fix)
- `01-aat-core/src/def-adaptive-tempo.md:1-65` (F4 verification — tensor extension, scope dichotomy)
- `01-aat-core/src/der-action-selection.md` (F5 verification — lift paragraph, Epistemic Status scope)
- `01-aat-core/src/scope-adaptive-system.md:8` (F6 sub-issue verification — `def-chronica` dep)
- `01-aat-core/src/scope-agency.md:24` (F6 Pearl-`do` residue verification — FORMAT-TODO C12)
- `01-aat-core/src/form-event-driven-dynamics.md:9` (F6 sub-issue verification — `form-agent-model` dep)
- `01-aat-core/src/hyp-mismatch-dynamics.md:54` (F6 sub-issue verification — link fix)
- `01-aat-core/src/def-agent-environment.md:11-23` (F7 verification — primitive segment unchanged, integration-debt residue)
- `01-aat-core/src/def-model-sufficiency.md:26-35` (F8 verification — well-definedness clause)

**Read first-hand from `audits/`:**
- `audits/.integrated/audit-742613-FINAL-2026-04-25.md` (full)
- `audits/.integrated/audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md` (full)
- `audits/.integrated/MANIFEST.md` (Cluster B + Cluster C + Cluster D sections containing 742613 dispositions, plus surrounding context)
- `audits/audit-findings-471203.md` (pilot — full read for shape)
- `audits/audit-findings-613842.md` (F2 precedent — full read for the strengthen-before-soften trail shape)
- `audits/polish-and-sentiment-ledger.md` (P-block read for 742613 process-feedback dispositions)
- `audits/pending-findings-2026-04-22.md` (spot-checks for substrate context)

**Deferred verifications (honestly "didn't have time" — flagged for downstream routing):**

- Fresh-1 through Fresh-9, Fresh-12 through Fresh-14 — each would require re-reading specific segments. The judgments are mostly light-editorial; the cycle of reading + verifying would not change the disposition (`soft-polish` or `actionable-open` for most).
- BP1, BP2, BP3, BP4 — light editorial verifications of current `src/` state; deferred to routing.

**Strengthen-first integration recommendations** (per brief item 3):

- **F1 worked example of "no strengthening direction available — fix is fix"** — direct sign repair. No softening occurred. Clean resolution.
- **F2 is the headline strengthen-before-soften-then-no-go canonical example** (jointly with 613842-F2) — the audit asked softenings, the project pursued strengthening, the strengthening hit a no-go, the no-go landed as a new exact result (Cor A.1S.1) + dedicated appendix (`#deriv-stochastic-non-exit`). No softening performed; falsified ever-exit object deleted; no-go demonstrated as present truth. The integration-is-replacement discipline operated exactly as designed. Documented in CHANGELOG 2026-05-16; canonical worked example in `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`.
- **F3 worked example of strengthening past the audit's ask** — the audit recommended "replace iff with one-way implication, or strengthen GA-3 to incremental/two-point condition." The landing did **both** as a clean structural split (B.4-i + B.4-ii) with the counterexample preserved as exhibit. Strictly stronger than what was asked.
- **F4 worked example of strengthening at the framework level** — the audit recommended scope-conditioning of the additive scalar. The project landed the matrix-Loewner tensor form as the canonical object, with scalar as shared-eigenbasis collapse special case. Substance strictly stronger than what was asked; narrow frontmatter residue not graduation-blocking.
- **F5 worked example of completeness-argument unification across layers** — the audit recommended either scoping to Section I or generalizing to $X_t$. The landing kept the Section I scoping but added the explicit lift paragraph with the *same completeness argument* applied at the lifted state. Layering preserved, supersession named.
- **F8 worked example of strengthening the convention path** — the SUPPLEMENT recommended a band-aid convention. The landing chose the substantive-epistemic-statement path ("predictive sufficiency is a property of a prediction task"). Cleaner than the convention.
- **F6 — `scope-agency` Pearl-`do` residue is the duplicate-routing case** — handled via FORMAT-TODO C12. Other F6 sub-issues resolved.
- **F7 — known integration debt** — still has residue at the primitive segment; tracked through PROPOSALS SP-6 and 471203 §F-A cluster. The strengthening direction (derive passive-observer case as structural limit of agent definition) is available but not yet executed.
- **Fresh items** — mostly `soft-polish`. Most have **no strong strengthening direction available** (they're convention / clarity / editorial). Fresh-4 (initial priors in `form-agent-model`) has a strengthening direction: derive $M_t = \phi(M_0, \mathcal C_t)$ explicitly with $M_0$ as initial epistemic state — substantively relevant for `03-llm-core/` work.

No soften-recommendations identified that weren't replaced with strengthening-direction work where one was available. The audit's strengthen-before-soften posture was honored throughout (the audit's *recommendations* were largely softenings, but the project's *executions* of them were strengthenings whenever a strengthening direction was available).

---

## Cross-cycle convergence noted

Documented in the trail above:

- **742613-F2 ≡ 613842-F2** (Model-S non-exit) — already-noted by the brief; the canonical worked example of strengthen-before-soften-then-no-go. Two independent reading-disciplines hit the same structural bug; jointly drove the Cor A.1S.1 + `#deriv-stochastic-non-exit` landing.
- **742613-F4 ≡ 613842-F1** (adaptive tempo) — same segment-state from two angles. 613842 caught the definition-scope mismatch directly; 742613 caught the same plus traced downstream-margin impact through `result-persistence-condition`.
- **742613-F6 Pearl-`do` ≡ 471203 §B F6** — duplicate routing to FORMAT-TODO C12.
- **BP3 (IB mixed-tier) ≡ 613842 Fresh-1** — both auditors landed the same observation, both honestly didn't promote.
- **742613 F-A cluster ≡ 471203 + 584721 multi-cycle convergence on passive-observer primitive drift** — three-cycle convergence on the same integration-debt class.
- **Fresh-11 (`git checkout` as L3 watch) → SN-3 resolved by strengthening** — 742613's watch item became the SN-3 finding that landed via parent co-owner direct-fix at `3072667` + `2666eca`. Cross-cycle anticipation operated as designed.
- **Opacity-gain tension** — per MANIFEST Cluster D row 1 (851201 §"Opacity-gain tension"): the 742613 WORKING dir contributed a "flag" to a ≥3-cycle convergence (849201-F1 / extracted-gemini-2026-04-26-27 / **AUDIT-WORKING-742613 flag** → one shared `deriv-adaptive-gain-dynamics` strengthening; `emp-update-gain.md:44`). The 742613 contribution is named in the MANIFEST as one of three cycles that triangulated to the resolution.

The Phase-2 triage vocabulary lineage (742613 → routing-tracker enum) is itself a cross-cycle convergence at the methodology layer: the vocabulary the 742613 SUPPLEMENT proposed survived as the conceptual ancestor of the disposition system used in every cluster's MANIFEST tables and in this very extraction file.

---

## Frame-defects / instructions-clarity observations

This is the sweep run (not the pilot). The 471203 pilot raised ten frame-defect observations; 613842 added five more. 742613-specific additions:

1. **Multi-checkpoint strategic-revision files are themselves extraction signal.** The 10/20/30 strategic-revision files (`10-strategic-revision.md` etc.) are *condensation events* the auditor wrote — they consolidate per-segment findings into running candidate-finding ledgers with explicit re-orientation. These are higher-density than the per-segment reflections and should be treated as primary sources for the candidate-finding trail. **Suggest:** parallel extraction agents should be told that strategic-revision / running-outline / consolidated-state files in the WORKING dir often carry more synthesis than the per-segment reflections, and should be read first to orient before walking the per-segment reflections individually.

2. **Phase-2 SUPPLEMENT triangulation vocabulary becomes the disposition enum.** The 742613 SUPPLEMENT proposed the triage vocabulary that became this program's routing-tracker disposition enum. **Suggest:** parallel extraction agents should flag when an audit's process feedback proposes vocabulary or methodology that has *since become canonical* — those are the highest-signal feedback items, and the cycle-of-origin matters for the lineage. The polish-and-sentiment ledger P-block already does this naming; the extraction file should preserve the lineage explicitly.

3. **Counterevidence-search-with-explicit-counterexample is its own pattern.** 742613's F2 and F3 trails both include explicit mathematical counterexamples (the OU recurrence calc, the sin-perturbed gradient field) constructed *as part of* the candidate-promotion process. This is stronger than the 613842 pattern (counterevidence search via cross-segment cross-check). **Suggest:** when the extraction agent encounters a counterexample-construction trail in the WORKING dir, preserve the explicit object (formula / counterexample) in the F-N-trail summary, not just the assertion that the bug exists. The counterexample is durable training material for future audits.

4. **The "honest-partial-pass" framing operating in a Codex environment is a structural pattern.** 742613 was a Codex audit with limited multi-turn budget; the auditor disciplined themselves to Section-I-only depth rather than degrading to skim-coverage for the rest. **Suggest:** when the WORKING dir's coverage is bounded by environment constraints (Codex turn budget, single-session context limit), the extraction file should explicitly note the constraint as a structural feature rather than as a coverage failure. The honest-partial-pass discipline is a strength to encourage.

5. **Cross-cycle dedup signals can be inferred from MANIFEST language sharpness.** MANIFEST Cluster B rows for 742613-F2 / 613842-F2 ("*same segment-state; the precise ever-exit-conflation reading governs the dedup*") and 742613-F4 / 613842-F1 (paired) carry sharper-than-typical dedup language. **Suggest:** the extraction agent should look for sharper-than-typical dedup language in the MANIFEST as a signal of cross-cycle methodology-level convergence (not just two cycles seeing the same bug, but two cycles seeing the bug via *different reading disciplines*). The methodology-level convergence is worth preserving.

6. **Some "did not promote" candidate-findings are themselves the methodology contribution.** 742613's strategic revisions explicitly track candidate-findings the auditor *didn't* promote (the burden-of-proof bar operating internally). These are pedagogically valuable for showing the *not-promotion discipline* — the framework's strengthen-before-soften posture applied within the audit's own cognition. **Suggest:** parallel extraction agents should preserve these "withdrawn" or "watch item, not promoted" trails as their own register (Part IV's withdrawn-candidate trail). The discipline is harder to learn from positive examples alone.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-742613/` is preserved unmodified per the brief.*
