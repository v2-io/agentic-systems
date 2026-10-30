# Internal surface map — top-level `audits/` files, `aat-reboot-aux-supplemental/`, and the `audits/.integrated/` label

*Objectives tree: feeds **KR3.2** of `../INTENT.md` (live theory stranded inside asf is mapped), and through it KR3.3 and O1. Cross-surface synthesis: `00-cross-surface-map.md`.*

*Written 2026-10-30 (clock: 11:46 MDT) by a fork of the inside-out coordinator, at asf `7ad5cd34`. Scope: every file directly under `audits/`, the `audits/aat-reboot-aux-supplemental/` directory, and a sampled check of `audits/.integrated/`. The `AUDIT-WORKING-*`, `ADJUDICATION-WORKING-*` and `.gem-hunt-trail/` directories belong to a sibling map. Dates are from `git log` (first and last commit touching each path) unless marked otherwise. Where I say "verified" I re-checked the claim against current canon today; where I say "per the file" I am relaying its own claim unchecked.*

**Who reads this.** The coordinator first, then the goal-setting with Joseph and the owner review, then integration agents who need to know where to go. The ranked list in §1 is for the first two; the per-file map in §3 and the slug join in §7 are for integration agents.

## 1. What matters most here, ranked by how much it bears on what the theory says

### 1.1 One thread, five independent arrivals: whose quantity is it?

The single most important theory point stranded in this surface is not any one finding. It is a missing discipline that five separate sources reached independently: **every AAT quantity is stated from some standpoint (the theory's third-person capacity statement, the analyst estimating from traces, an external monitor, the designer, or the agent itself), and canon almost never says which.** Where the standpoint is unstated, a claim true for the analyst gets used as a premise about what the agent can do.

The arrivals, with dates:

- `audits/fix-adaptive-reserve.md` (2026-08-12, commit `3a705fe6`, 502 lines) and its independent audit `audits/fix-adaptive-reserve-AUDIT.md` (same day, 457 lines; 52 of 53 citations verified). The worked instance: the adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ is described from five standpoints. Four are consistent. The fifth, that the agent itself reads the reserve per step, is asserted in canon and nowhere derived, and it carries the constructive boundary of the self-actuation no-go.
- Ledger row S35 in `audits/polish-and-sentiment-ledger.md` (2026-05-29): "modeler-perspective vs agent-perspective framing … the persistence condition a *survival* condition, not the *optimality* condition of modeler-perspective RL/ML … never as a framework-wide framing."
- Parked candidate clarifications in Working Notes of `#def-observation-function` (four substrates: 526815, 742613, 829314, 849201) and `#scope-adaptive-system` ("the condition is evaluated from a God's-eye view, not the agent's"), quoted in `fix-adaptive-reserve.md` §2.
- `aat-reboot-aux-supplemental/03-def-observation-function.md` (2026-09-25), which tests that gold and finds its punchline proves too much (`#emp-update-gain` does state an optimal gain), so the distinction needs care, not just a slogan.
- The AUDIT's correction to the plan: the discipline is not missing everywhere. `#def-model-class-fitness` already states that $\mathcal F(\mathcal M)$ is not agent-computable and supplies an agent-available proxy. The framework knows how to say who holds a number; it never said it for the persistence parameters $(\alpha, R, \rho)$.

**Verified state today.** Canon still carries the underived agent-standpoint claim: `01-aat-core/src/deriv-self-actuation-grounding.md:25` and `:70` ("a finite local read the in-scope agent already maintains"), and `terminology/entries/adaptive-reserve.md:20` ("agents track the reserve to anticipate when persistence is about to fail"). No commit touched those files after the plan. Neither fix file is referenced by `TODO.md`, `PROPOSALS.md`, `audits/STATUS.md`, `JOSEPH-TODO.md` or any `spikes/` tracker (grep); the only inbound reference is from `aat-reboot-aux-supplemental/12-def-model-class-fitness.md`. It is fully orphaned.

**Why it matters to what the theory is.** The persistence condition is AAT's headline result. Whether it is a statement *about* agents (a survival certificate an analyst can check) or a quantity agents *use* (something an agent can steer by) changes what the theory claims agents can do, and it changes what the self-actuation result says about how an agent can ground its own objectives. The plan's options (A: land the standpoint discipline; B/C: spike the reserve's identifiability floor or derive an endogenous estimator, with the precedent that the framework already did this for the update gain; D: repair the corollary at the weakest sufficient burden, since it may need only a sign or gradient, not a value; E: soften only if B–D fail) and the AUDIT's Option F (apply `#def-model-class-fitness`'s existing template to $(\alpha, R, \rho)$) are a ready-made strengthen-first package. The AUDIT also names a fourth load-bearing site, `#disc-value-functional-grounding-floor:42` (per the file; not re-checked by me).

**A gate that has now lifted.** Both files deliberately did not read `01-aat-core/src/deriv-adaptive-gain-dynamics.md`, because another agent held a committed, unscored prediction about it. The plan's §8 says that file has become load-bearing for the repair and states the exact questions to ask of it (the AUDIT adds a fourth, Q4). Under today's lifted gates that read can happen.

### 1.2 SP-30: the broadest scope's exclusion is false for standard RL (open since 2026-07-03)

From `audits/audit-731548-FINAL-2026-07-02.md` §B-3 (Claude Fable 5, adversarially verified and *upgraded* by its verifier). `#scope-adaptive-system` excludes systems with $H(\Omega_t \mid \mathcal C_t) = 0$ as "a solved problem", but a fully observed MDP with an unknown transition kernel has zero state entropy and still needs the whole adaptive machinery. Canon's own RL examples survive only by unratified per-example choices of what $\Omega$ contains (`#example-bandit` silently puts the reward law in $\Omega$; `#disc-exploit-explore-deliberate` splits it the other way). The repair touches a `depends: []` root definition and two constitutive atoms (`#def-action-transition`, `#def-observation-function`), so it was routed to Joseph as `PROPOSALS.md` SP-30 (verified: line 389, status "Open — needs Joseph", line 399). The gate it waited on is lifted today. The live spike `spikes/epistemic-target-ontology/` (2026-07-04) reshapes it into a typed target $S_t = (\Omega_t, \theta)$ with law-content $\theta$ as a missing noun; that is the spikes map's territory. `aat-reboot-aux-supplemental/01`, `02`, `03` and `05` (2026-09-25) list the side effects on each atom; note especially that the pair $(h, \mu_\varepsilon)$ is never identifiable, so observation-law opacity should be stated on the induced kernel (aux 02).

This bears on the theory's first sentence: what an adaptive system is *uncertain about*.

### 1.3 The 2026-09-25 per-segment supplements: the freshest verified findings on Part I's front, none integrated

`audits/aat-reboot-aux-supplemental/` (17 files, 1,389 lines, one commit `a3db02ed` 2026-09-25, body: "Add several incidental audit findings resulting from the aat rewrite attempt"). Each file is a finder's long-form report on one Part I segment, from `01-aat-core/INTRODUCTION.md` through `#der-action-selection`, written by Claude Opus 5.5 for the aat-reboot walkthrough (now `~/src/aat-refactored/`). Each has the same parts: checks that held ("please add to the Working Notes of …"), history from commit bodies, slug-tagged notes for other segments, out-of-scope errors, worries, and process feedback. The companion slim versions are at `~/src/aat-refactored/scratch/aux/` (19 entries); the supplements' own paths still say `~/src/aat-reboot/`, which no longer exists.

They were written a month after canon last moved (no commit touches the four `*-core/` trees, `NOTATION.md` or `terminology/` after 2026-08-24, verified), so nothing in them has landed, including the "please add to Working Notes" checks. The integration value is high because each note is slug-tagged and line-referenced. What I'd put first:

- **"What are the three to five things this volume proves?" has no single answer in the repo** (aux 00 §9). The introduction's four anchors, the README Position & Lineage four, the external-reader consensus (ledger S9), a scout's proposed fifth anchor, and the Part II preface's "16/24" all differ. This is the concrete form of Joseph's "I don't even know what this theory is *trying* to illuminate."
- **A front-surface claim canon does not hold** (aux 00 §0.2): "active inference recoverable under three explicit restrictions" is stated in `01-aat-core/INTRODUCTION.md:50`, `HISTORICAL-CONTEXT.md:62` and `doc/readme/src/_position-and-lineage.md:18`, but lives only in `spikes/.integrated/spike-fep-suboptimal-approximation.md:57` as a "Candidate Hypothesis" whose own recommendation is not to promote it. Canon (`#disc-ciy-unified-objective:66`) holds a weaker shape-level isomorphism. Two honest routes: land the mapping at its true tier, or restate the fronts.
- **Three senses of "agent" on page 1** (aux 00 §9, aux 01, aux 05): the introduction requires acting; the umbrella since SP-24 includes passive observers; capitalized "Agent" is earned at the actuated lift. `LEXICON.md`'s *Agentic system* entry and `terminology/entries/adaptive-system.md` contradict `#scope-agency`'s causal-contrast definition. Flagged "[OPEN] … do not unilaterally rewrite" in `msc/scope-of-work-ontology-and-figure-2026-05-17.md:168–179`, still open.
- **731548 ledger item lxiii, never carried forward** (aux 00): `NOTATION.md:260` GA-2S ("zero-mean, finite second moment") does three inequivalent jobs; the containment dichotomy actually selects on bounded versus unbounded support. Verified unchanged today. The introduction's anchor 2 inherits it.
- **New derivations offered, unverified by anyone else**: a log-loss identity for class fitness, minimum regret $= (1-\mathcal F)\, I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty})$ (aux 08); an exact readout-plus-retention split of term (i) of `#result-mismatch-decomposition` (aux 12); an information-state lemma checked against Subramanian and Barnett–Crutchfield (aux 15).
- **Defects in heavily-used Part I segments**: stochastic update $f$ breaks "$M_t$ is a function of $\mathcal C_t$" and C3 read literally says $M_{\tau^-}$ determines the whole past (aux 09, on `#deriv-recursive-update`); `#example-kalman`, the flagship example, is a pure active-perception agent whose action only selects sensor noise and has an off-by-one action index (aux 02, 03, 07); passive observers defined as $\lvert\mathcal A\rvert \lt 2$ include $\lvert\mathcal A\rvert = 0$, which leaves $T$ and $h$ with no action argument (aux 05); `NOTATION.md:263` still lists GA-5 as live though `#deriv-discrete-sector-condition:187` closes it (aux 14); 526815 F75 and F204 still unfixed (aux 09, 14).
- **Honest-activation is not integrated**: aux 12 and 13 note that `spikes/spike-honest-activation-2026-09-23/` R1–R4 bear directly on `#emp-update-gain`, `#deriv-adaptive-gain-dynamics` and `#def-model-class-fitness`, and its integration plan under-describes this as a Working-Notes hook. (The spikes map owns the spike.)

### 1.4 Audit 731548's open residue: four theory-scale items with no segment

From `audit-731548-FINAL-2026-07-02.md` (Fable 5, Part I + all nine AAT `impl-*`, six-verifier round). `audits/STATUS.md` records B-1, B-2, B-4's Regime-III contradiction and the mood floor as executed 2026-07-03; I spot-checked B-1 (tightness language now in `#deriv-sector-condition` and `#result-persistence-condition`), B-2 (`#result-mismatch-decomposition` now carries the three-floor decomposition with the Bayes floor) and the Regime-III fix (`#impl-cooperative-adversarial:39`), and they hold. What remains has no segment:

- **The floor-routing diagnostic** ("persistent high mismatch: raise gain, keep learning, fix sensors, or change model class?"), which five auditor arrivals converged on. Staged only as a Working Note bullet, `#impl-persistence-and-limits:101` "Forward — the operator decision tree".
- **The Volume-4 shadow catalogue**: ten Part I theorems whose Volume 4 readings inherit Part I's tier (exit-certainty as resurrection-not-fortress; burn rate as starvation death; gain collapse as self-doubt-as-architecture; and so on). Staged in `#impl-persistence-and-limits:130` WN, tracked at `TODO.md:523`. The auditor judged this "would arguably do more for the ELI program's defensibility than most direct Volume-4 writing."
- **Missing-theorem candidates (§D)**: the Class-1 compression price (a goal-blind $\phi$ is generically IB-suboptimal, so there may be an optimal $\kappa^\ast \gt 0$, which would complicate "Class 1 is the clean case"; no canon home, re-raised by aux 10 with Still 2009 eq. 20 as a lead); an interior-dynamics calibration bound (the Part I ancestor of truth-death defenses; lives only in the FINAL); a compilation-cost axis (prices the costs of internalizing knowledge; lives only in reflections and aux 16).
- **The targeted-legacy quantifier sweep** (`TODO.md:521`): every correctness finding in 731548 was a statement-layer defect on correct algebra, concentrated in the oldest prose. Aux 00 shows the introduction already needs it ("loses bounded behavior", `INTRODUCTION.md:26`, still there).

### 1.5 The polish ledger's research seeds: about twenty open hypotheses, untouched since 2026-05-29

`audits/polish-and-sentiment-ledger.md` (2026-05-15 to 2026-05-29, 87 lines) is the durable home for soft findings and research seeds. Its open `research-seed` rows are the densest list of stranded theory hypotheses in this surface. Most bear on what the theory claims, not on presentation:

- S4: a uniqueness-of-coherent-statistical-geometry theorem from (PI) plus additivity (`#disc-additive-coordinate-forcing`).
- S5: when do escape mechanisms of composed impossibilities compose or interfere (`#disc-identifiability-floor`).
- S6: hysteresis, asymmetric loss and recovery thresholds in persistence.
- S11: the composition bridge is unavailable exactly where composition is most interesting (Tier-3 prevalence).
- S12: a sensitivity bound for the orient-cascade step-4c covariance test, the unique broadly available L0 to L1 escalation diagnostic.
- S13: three unclosed 2026-04-22 intuitions, among them that the orient cascade is itself an adaptive cycle.
- S14: Cox-style necessity for `#deriv-graph-structure-uniqueness` via Lauritzen (marked graduate-watch).
- S22 D.3: gain collapse, catastrophic forgetting, detection latency and stability myopia as one correction-capacity-collapse pathology.
- S24: is $k$-of-$n$ representable under the $DL(\Sigma)$ budget (attempt the no-go).
- S25: the missing upper bound of the stability–plasticity window in `#form-consolidation-dynamics`.
- S31: context window as a computable maximum planning depth.
- S32 + S40: goal-blind retrieval as the dual of goal-blind routing (two independent audits converge).
- S34: ordinal/metric duality ($M_t$ is event-indexed, the persistence inequality is wall-clock).
- S35: the standpoint thread of §1.1.
- S38: $U_M$ names two different quantities.
- S39: AI cognitive load may be step-shaped, not exponential.
- S41: a wave-2 bundle, including strategic ignorance as CIY's dual and Level-3 access as a bridge to moral weight.

Aux 14 notes S34 needs updating: the per-event to per-time conversion is now published in `#der-gain-sector-bridge` and `#deriv-discrete-sector-condition`.

## 2. External research and prior art to integrate (flagged for Joseph's "list in there somewhere")

There is no single queue of external research in the top-level audit files. There are four scattered kinds, and one of them points at a home that does not exist.

**(a) A citation-verification backlog nobody holds.** Two findings were dispositioned to a "Phase-3 citation verification backlog": 742613 Fresh-10, Bareinboim et al.'s strict-hierarchy claim (`#def-pearl-causal-hierarchy`; `audit-findings-742613.md:403–407, :629`), and 584721 Fresh-9, Aguilera 2022 on FEP-flow narrow validity (`audit-findings-584721.md:584–600, :1267`). Both dated 2026-05-20. No tracker holds that backlog: `grep "Phase-3"` over `TODO.md`, `BIBLIOGRAPHY-TODO.md`, `FORMAT-TODO.md` and `INTEGRATION-CLEANUP-TODO.md` finds nothing. Aux 06 (2026-09-25) has since checked the Bareinboim use in `#scope-agency` against relata and found it holds, which partly discharges Fresh-10.

**(b) Citations synthesized rather than read.** The `[^bg2-2026-05-21]` Undermind citations in `#disc-identifiability-floor` (Instance 3 escape (e)) are marked as needing primary-source verification (`audit-384279-FINAL-2026-05-27.md:199`). `spikes/spike-escape-standpoint-axis-2026-07-29.md` reports this surfaced a third time and that the citations are load-bearing for a softening.

**(c) Missing or wrong bibliography entries.** Miehling et al. 2025 (arXiv:2503.00237), the one external work the volume introduction names, is in neither relata nor any `mono/*.bib`; the local source is `ref/arXiv-2503.00237v1/agentic_systems_theory.tex` (aux 00, 2026-09-25). relata's author field for `hafez-2026-mathematical` disagrees with the paper's masthead (aux 00).

**(d) Uncited prior art, found 2026-09-25, by slug.**

| Prior art | Bears on | Where noted | relata state per the note |
|---|---|---|---|
| Still 2009, predictive information with feedback (exploration emerges as a term) | `#deriv-causal-ib-exploration`, `#deriv-causal-ib-lmi`, `#disc-ciy-unified-objective`, `#form-agent-model` (settles 526815 F3); lead for the Class-1 compression price | aux 10:39–48 | `still-2007-information-theoretic`, PDF registered, markdown queued |
| Creutzig 2009 and Amir 2015 past-future IB; Bialek–Nemenman–Tishby predictive information | `#form-information-bottleneck`, `#def-model-sufficiency` (its denominator) | aux 08:39–44 | entries exist, some without markdown |
| Richens et al. 2025, "General agents contain world models" (converse of the $M_t$ postulate) | `#form-agent-model`, `#def-agent-spectrum` | aux 08:45, aux 09; spike proposal `spikes/PROPOSED.md:36` | entry without document |
| Strouse & Schwab 2017, deterministic IB | `#form-agent-model` | aux 10:48 | not in relata |
| Bar-Shalom & Tse 1974 (no dual effect in LQG), Åström 1965, Smallwood & Sondik 1973, Littman PSR, Klenske 2015 | `#def-action-transition`, `#der-action-selection` | aux 02:42, aux 16:54 | no markdown (paywalled) |
| Kumar & Varaiya (information state), Subramanian, Barnett & Crutchfield | `#der-recursive-update`, `#def-model-sufficiency` | aux 11, aux 15 | Barnett converted late |
| Kleijn & van der Vaart 2006, Shalizi 2009 (misspecification) | `#def-model-class-fitness` | aux 12:41 | entries without documents |
| Ashby, Duff (BAMDP), Kaelbling | `#scope-adaptive-system` | aux 05:42 | no entries with markdown |

Seeds in the ledger that start with an external check: S14 (Lauritzen's characterization of Markov properties), S36 (verify that BNT/Netica default to noisy-OR before claiming it). Both fix-adaptive-reserve files say plainly they did no prior-art search outside the repo. `audit-findings-592047-commit-4add071.md:75` records that a novelty search for `#deriv-decomposition-uniqueness` is queued and is load-bearing given how close causal-abstraction intervention-commuting maps are; the INDEX row agrees (spikes map).

## 3. Per-file map

| Path | First / last commit | Lines | What it is | Live content for integration |
|---|---|---|---|---|
| `fix-adaptive-reserve.md` | 2026-08-13 / same | 502 | Repair plan, reserve standpoint (§1.1) | **High.** Unexecuted, orphaned. |
| `fix-adaptive-reserve-AUDIT.md` | 2026-08-13 / same | 457 | Independent audit of the plan | **High.** Adds Option F, a fourth site, corrects §6.1 (self-model canon exists, including `03-llm-core/src/hyp-behavioral-self-knowledge-insufficiency.md`). |
| `aat-reboot-aux-supplemental/` (17 files) | 2026-09-25 / same | 1,389 | Per-segment finder reports, Part I front (§1.3) | **High.** Newest verified material in asf; nothing landed. |
| `audit-731548-FINAL-2026-07-02.md` | 2026-07-03 / same | 164 | Fable de-novo, Part I + impl-* | **Medium-high.** B-3 = SP-30 open; §D and §F items (§1.4). Its reflections dir is the sibling map's. |
| `polish-and-sentiment-ledger.md` | 2026-05-15 / 2026-05-29 | 87 | Soft-finding and research-seed ledger | **Medium-high.** Open seeds (§1.5). |
| `audit-findings-592047-commit-4add071.md` | 2026-08-24 / same | 145 | Three-round independent verification of `#deriv-decomposition-uniqueness` | **History.** Closed CLEAN at `5ade664`. Useful as the model of verifier, author and integrator as three different agents; the remaining open edges are in the spike files. |
| `audit-384279-FINAL-2026-05-27.md` | 2026-05-28 / same | 257 | Opus 4.7 de-novo, AAT | **Low.** Structural findings landed; three spike proposals live in `spikes/PROPOSED.md:32–35` (two-routes-exhausts on `#disc-value-functional-grounding-floor` is the theory one). §F is a good outside description of the certificate-spine meta-architecture. |
| `audit-773921-FINAL-2026-05-28.md` | 2026-05-28 / same | 96 | Gemini 2.5 Pro de-novo | **Low.** F1 resolved by SP-24; F4 landed as `#disc-sandbox-evaluation-ceiling` (verified); §D went to ledger S31/S32. Graduation blocked only on its gold dir. |
| `audit-451729-FINAL-2026-05-10.md` | 2026-05-10 / 2026-05-15 | 185 | Sonnet 4.6 de-novo | **Low.** Kept open only on D.1, which asks for `stage:` promotions. Joseph's 2026-07-14 position is that `stage:` is known-problematic and ignored, so D.1 no longer blocks anything real (inference; not adjudicated). |
| `audit-findings-{184930,193847,451729,471203,472913,526815,542891,584721,613842,738192,742613,829314,849201,963715}.md` | 2026-05-20 / to 2026-06-11 | 7,419 total | Extraction digests of the working dirs, written 2026-05-20 by Opus 4.7 sweeps, then gem-hunted 2026-05-29 | **Per-slug lookup only.** The gem-hunt routed their gems (dispositions are in the sibling map's `.gem-hunt-trail/`). The gem-hunt agent warned that 526815's ~200 F-rows are stale until re-grepped. The aux files show that "stale" is not "resolved": 526815 F75 and F204 are still live defects. 193847's digest is the only record for that Gemini cycle (no FINAL); its Themes F1–F10 name proposed segments, some since lifted into Working Notes. |
| `pending-findings-2026-04-2{1,2,3,5}.md` | 2026-04-28 / to 2026-05-28 | 1,330 | Per-finding resolution ledgers of the April intakes | **History.** Mostly RESOLVED with commit hashes; the partials (2026-04-22 F5, F11) became ledger S12. The MANIFEST treats them as evidence infrastructure, deliberately not graduated. |
| `README.md`, `STATUS.md` | 2026-05-15 / 2026-08-22 | 108 | Orientation and live routing tracker | Accurate as of 2026-08-22 against what I checked. The README's consult-Joseph gate is lifted for this effort. STATUS's 731548 row is the best one-paragraph summary of what is open. |

## 4. Is the `audits/.integrated/` label true enough to skip?

**Yes for the files themselves, with one condition: follow the homes they point to.** The MANIFEST defines graduation as "every finding it raised has a verified disposition", where a disposition can be canon, the polish ledger, a `TODO.md` or `PROPOSALS.md` item, or (since 2026-08-22) an `impl-*` Working Note. So graduated does not mean the content is in canon; it means the content has a home. An integration agent can skip `audits/.integrated/*.md` but must read those homes, which is where §1.4 and §1.5 come from.

What I checked first-hand, spread across the clusters (2026-05-12, Clusters B–E, the 2026-08-22 lift):

- Cluster D, OUTLINE describes `#der-team-persistence` as stated: holds (`01-aat-core/OUTLINE.md:279`).
- Cluster D, 829314-core-F5 "0 `Descended from` footers": holds in substance. Four hits now exist, but all four are Working-Note text *describing* the resolved slip, brought back by the 2026-05-30 gold-lift (commits `b46c07a2`, `598631e1`, `46168faf`).
- Cluster B, P3 to Markov proved: holds (`#form-composition-closure`, `#deriv-graph-structure-uniqueness`).
- Cluster B, 742613-F4 residue tracked in TODO: holds (`TODO.md:173, :432`).
- Cluster D, opacity-gain tension resolved at `#emp-update-gain:44`: holds.
- 2026-08-22 lift, shadow catalogue and operator decision tree in `#impl-persistence-and-limits` WN: holds (`:101`, `:130`), as staging, not canon.
- 2026-08-22 lift, matrix information-rate floor marked conjecture: holds (`#impl-persistence-and-limits:95`).
- 2026-05-12 cluster, residual opens in `TODO.md` §2026-05-12: holds (`TODO.md:416–448`).
- Cluster B, the `#def-mismatch-signal:34` sign fix: line numbers have drifted; not confirmed either way.

No sampled claim was false. Two cautions. The partially lifted reflection dirs under `audits/.integrated/AUDIT-WORKING-*` are a different case and belong to the sibling map. And the gold-lift's habit of copying resolved findings back into Working Notes as "certified finding; recorded for texture" means a Working Notes reader can re-chase defects that are already fixed (see §6).

## 5. Things that are not theory but will cost integration agents time

- `aat-reboot-aux-supplemental/*` cite `~/src/aat-reboot/…`, renamed `~/src/aat-refactored/`.
- `fix-adaptive-reserve.md` cites `_obs/old-tf-appendix-a-lyapunov.md`; `_obs/` is now `.archive/`.
- `doc/sop/agents.sop.md` cites the `01-aat-core/OUTLINE.md` "Reading AAT" preamble as its worked example of respectful pedagogy; that preamble was deleted 2026-05-17 (`feccd0d2`) (aux 00 §9; not re-checked).
- `01-aat-core/src/img/agent-spectrum.svg` still says "Blind Pursuer" and "SECTION I / SECTION II" (aux 00).
- The relata conversion queue blocked several finders for an hour or more behind 500-plus-page books; `pdftotext` on the registered PDF was their workaround (aux 10, 11, 14, 15, 16).

## 6. Observations about the system, for the truthification-as-a-system question

- **Repairs that are fully worked out can still fall out of every tracker.** The reserve plan is the best-verified repair document in this surface and nothing points to it. 731548 ledger item lxiii fell between the working ledger and the FINAL. The Phase-3 citation backlog is a disposition target that does not exist. The common shape: a finding is "routed" when someone writes a destination, and nothing checks that the destination exists or is ever read. A cheap check would be: every disposition target named in an audit file must resolve to a live tracker line or a segment.
- **Front matter has no staleness mechanism** (aux 00). The introduction has no slug or `depends:` and sits outside the generators, so B-1, SP-24 and lxiii each left it stale without any signal. If front surfaces cited their anchors by slug, `bin/refresh-all --check` could flag drift.
- **The defect species is consistent.** 731548 (July), the reserve plan (August) and the aux reports (September) independently find the same thing: correct algebra under statement-layer drift (an "iff" where only "if" is proven, "is" where the source said "is the kind of", a gloss that outlived a redefinition). 731548's verifier traced the reserve claim's hardening to an 18-minute spike-to-segment landing that dropped a hedge. The sweep the FINAL recommended is the right instrument and is still undone.
- **Gold in Working Notes cuts both ways.** 731548 §G warns that lifting prior auditors' gold into segment bodies homogenizes later de-novo readers, and the aux reports find several gold items stale or wrong (aux 03 lists four in one segment). Because the 2026-05-30 lift also brought back resolved findings as texture, Working Notes now mix live leads, resolved history and wrong gold, with little marking to tell them apart.
- **The best audit pattern in this surface** is 592047: an independent verifier re-derives rather than follows, reports only, and the author repairs; three rounds to CLEAN, each round catching the same failure one ring further out (the conclusion was checked against the intended family, not the written generality). Its addendum is a good brief template for integration verifiers.

## 7. Slug join (for integration agents)

Each row: slug, then where in this surface it is touched, then kind. "aux NN" means `audits/aat-reboot-aux-supplemental/NN-*.md`.

| Slug | Source in this surface | Kind |
|---|---|---|
| `deriv-self-actuation-grounding` | fix-adaptive-reserve §3.2 B1; AUDIT §1 | live defect: underived premise (verified present) |
| `result-persistence-condition` | fix-adaptive-reserve §3.1, §7 (Option F target); aux 00; ledger S35 | standpoint paragraph owed |
| `disc-continuity-stance` | fix-adaptive-reserve §3.2 B3 | weaker sibling of the same defect |
| `disc-value-functional-grounding-floor` | AUDIT §2.4 (fourth load-bearing site); 384279 §D Hyp 2 | live defect (per the file); proposed spike |
| `detail-operationalization` | fix-adaptive-reserve §3.3 | mislabelled as agent-facing |
| `def-model-class-fitness` | AUDIT §2.2 (template for Option F); aux 08, 11, 12; 731548 B-2 companion | precedent; open ledger items xxix, xxxi, xxxii |
| `deriv-adaptive-gain-dynamics` | fix-adaptive-reserve §8 (blocked read, now unblocked); aux 13 | open question |
| terminology `adaptive-reserve`, `adaptive-system`, `model-sufficiency`, LEXICON *Agentic system* | fix-adaptive-reserve §3.2 B2; aux 05, 11, 00 | live wording defects |
| `scope-adaptive-system`, `def-agent-environment`, `def-action-transition`, `def-observation-function`, `example-bandit` | 731548 B-3 / SP-30; aux 01, 02, 03, 05 | root ontology, open, gate lifted |
| `scope-agency`, `post-causal-structure`, `der-loop-interventional-access`, `def-pearl-causal-hierarchy` | aux 05, 06, 07 | wording and scope defects |
| `example-kalman` | aux 02, 03, 06, 07 | flagship example is pure active perception; off-by-one |
| `def-chronica`, `form-agent-model`, `scope-agent-identity`, `obs-context-turnover`, `def-five-constitutive-factors` | aux 04, 09; 731548 §B.1 | staged clarifications; circular grounding |
| `deriv-recursive-update`, `form-event-driven-dynamics`, `der-action-selection`, `form-consolidation-dynamics` | aux 09, 14, 15, 16 | stochastic-update and C3 issues; F75 unfixed |
| `form-information-bottleneck`, `def-model-sufficiency`, `deriv-causal-ib-exploration`, `disc-ciy-unified-objective` | aux 08, 10, 11; §2(d) | uncited prior art; Class-1 compression price |
| `result-mismatch-decomposition`, `internal-external-decomposition`, `deriv-mismatch-budget-attribution` | aux 12; 731548 B-2 (landed) | offered exact split of term (i) |
| `der-interaction-channel-classification` | aux 12, 14 | 526815 F204 unfixed (rate compared with noise scale) |
| `deriv-sector-condition`, `result-sector-condition-stability`, `deriv-stochastic-non-exit`, NOTATION GA-2S, GA-5 | aux 00, 14; 731548 lxiii | GA-2S wording; GA-5 stale |
| `01-aat-core/INTRODUCTION.md`, `HISTORICAL-CONTEXT.md`, `doc/readme/src/_position-and-lineage.md` | aux 00 | front-surface overclaims; headline-results disagreement |
| `impl-persistence-and-limits` | 731548 §F; MANIFEST 2026-08-22 | staged floor-routing tree and shadow catalogue |
| `der-directed-separation`, `disc-modularity-state-dynamics` | 731548 §D, §F; aux 10 | Class-1 compression price; legibility priority |
| `deriv-decomposition-uniqueness`, `form-complete-agent-state` | 592047 | verified clean; novelty search queued |
| `disc-identifiability-floor`, `disc-additive-coordinate-forcing`, `deriv-graph-structure-uniqueness`, `form-consolidation-dynamics`, `def-unity-dimensions`, `def-adaptive-tempo` | ledger S4, S5, S14, S25, S38; §2(b) | research seeds; unverified citations |
| `disc-m-preservation`, `scope-multi-agent`, `impl-causal-access` | ledger S31, S32, S40 | goal-blind retrieval seed |
| `def-chronica`, `form-event-driven-dynamics` | ledger S34; aux 14 | ordinal/metric duality seed (needs update) |
| `04-eli-core` (proposed `norm-adaptive-reserve-as-ethical-floor`, `disc-agency-mechanism-boundary`, a Level-3 moral-weight segment) | `audit-findings-193847.md` Themes F2, F3, F5; ledger S41 | proposed segments, none exist (grep) |

## 8. What I did not do

I did not re-read the fourteen `audit-findings-*` digests row by row, and I did not re-verify the gem-hunt's dispositions; I read their frontmatter, sampled 193847's dispositions, and relied on `audits/STATUS.md` and the MANIFEST for routing state. I did not open the `AUDIT-WORKING-*` or `.gem-hunt-trail/` directories (sibling map). Of the aux supplements I read `00-introduction.md` through its §9 in full and only the section headers and note bullets of the other sixteen. I did not re-derive any of the new derivations they offer. My `memorata-search --no-rerank` query for an external-research list scoped to `audits/` returned nothing.
