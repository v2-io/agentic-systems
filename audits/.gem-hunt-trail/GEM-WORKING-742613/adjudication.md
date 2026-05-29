# Gem-hunt adjudication — audit-findings-742613

*Gem-hunt cycle 2026-05-29. Report-only; no canon edits/moves/commits. Landings + verification are Joseph's.*

Slice: `audits/audit-findings-742613.md` (725 lines, read in full). Auditor: Codex, de-novo partial-Section-I walk (2026-04-25). This file is itself a **prior extraction** (2026-05-20, Opus 4.7) that routed and first-hand-verified every numbered finding; the audit is already graduated into `.integrated/MANIFEST.md` (Cluster B) with `audit-742613-FINAL` + SUPPLEMENT moved there.

## Orientation — what was already routed (do not re-surface)

Cross-checked against `audits/.integrated/MANIFEST.md` (Cluster B/C/D rows for 742613), `audits/polish-and-sentiment-ledger.md` (P-block), `audits/STATUS.md`, `TODO.md`, `PROPOSALS.md`:

- **F1–F8 (numbered findings):** all dispositioned in MANIFEST Cluster B and **first-hand re-verified resolved by the prior extraction** (I spot-confirmed F2/F4/F8 loci independently — see below). F2 (Model-S non-exit) is the canonical strengthen-before-soften-then-no-go worked example (Cor A.1S.1 + `#deriv-stochastic-non-exit`); F3 (B.4 split), F4 (matrix-Loewner tensor tempo), F5 (lift paragraph), F8 (well-definedness clause) all landed *strictly stronger* than the audit's softening ask. F1 sign fix landed. F6 mostly resolved; Pearl-`do` residue → FORMAT-TODO C12. F7 is tracked integration-debt (PROPOSALS SP-6 + 471203 §F-A).
- **Process/methodology (BP5–BP10, Themes A–G):** all in the ledger P-block as `process/instruction-feedback`; Phase-2 triage vocabulary is `superseded-by` the routing-tracker enum (absorbed). Not theory content. Correctly routed.
- **The prior extraction's bias warning was right:** 742613 was heavily *process*-routed. Its theory candidates (the Part III "Fresh" items) were dispositioned `soft-polish`/`research-seed`/`deferred` — and the extraction explicitly says "Did not separately re-read..." for most of them. **That is the under-mined remainder, and it is where I did first-hand canon checks.**

## Drift check on already-routed dispositions

I re-verified the flagship-class items against current `src/` first-hand; **no already-routed disposition is now wrong.** Specifically confirmed still-correct:
- F2 `01-aat-core/src/deriv-sector-condition.md` Prop A.1S four-sub-result form + Cor A.1S.1 + `deriv-stochastic-non-exit.md` present.
- F4 `def-adaptive-tempo.md` tensor/matrix-Loewner canonical, scalar = shared-eigenbasis collapse; narrow frontmatter residue still at TODO (still not a blocker).
- F8 `def-model-sufficiency.md:26-35` well-definedness clause present.
- BP3 `form-information-bottleneck.md:40` now explicitly partitions tiers ("exact for IB-core; robust-qualitative for $\beta(\rho,\pi)$") — fully strengthened, no open direction.
- BP1 `der-recursive-update.md` frontmatter now `status: exact`, harmonized with Epistemic Status.

---

## (A) Ready-to-land

### A1. Name AAT's agency boundary as *observation-mediated*, not environmental (Fresh-13)

**(1) What it is, actionably.** `scope-agency` defines agency via $P(o \mid do(a)) \neq P(o \mid do(a'))$ — an *observational* interventional contrast. The un-captured point: this means **an action that changes hidden environment state but produces no observational contrast is outside AAT-agency by design.** The segment explains *why contrast matters* but never names that the contrast is specifically *observational* rather than *environmental/state* ($P(\Omega_{t+1}\mid do(a))$). The fix is a short Discussion paragraph (or one Epistemic-Status clause) making the choice explicit and owning it: AAT is observation-mediated, so "agency" is scoped to *observable* causal effect; effects on hidden state with no observational signature are real but outside this boundary unless/until they become observable.

**(2) Named canon loci checked.** `01-aat-core/src/scope-agency.md` (full, lines 1-49): formal expression line 25 uses $P(o\mid do(a))$; Discussion lines 40-47 motivate contrast but never name observational-vs-environmental. `def-pearl-causal-hierarchy` (referenced) is about the hierarchy, not this boundary. Not in PROPOSALS (SP-24 is a *different* axis — see below), TODO, or ledger.

**(3) Why a gem — wisdom + beauty.** It sharpens exactly what the framework's load-bearing scope condition *is*. AAT's whole posture is "observation-mediated agent" (cf. `def-observation-function`, `form-agent-model`); this is the place that commitment becomes a scope *decision* with a named excluded class, and right now it's silent. Naming it converts an implicit modeling choice into an explicit, defensible boundary — precisely the scope-precision-is-a-virtue CS norm the project prizes. Cheap to land; high legibility return.

**(4) Recommended home.** A Discussion paragraph in `scope-agency.md` (and a one-clause Epistemic-Status note that the contrast is observational by construction). **Interaction flag:** touches the same agency-boundary prose as **PROPOSALS SP-24** (the `def-agent-environment` action-channel-constitutive reframe). They are *different axes* — SP-24 = "is the action channel constitutive of *agent*"; A1 = "is the causal contrast *observational* vs *environmental*" — but if SP-24 executes, do A1 in the same pass so the boundary prose stays coherent. Not subsumed by SP-24.

---

## (B) Research-seeds

### B1. Initial-prior / pretrained structure ($M_0$) in the core reality-model formulation (Fresh-4)

**(1) What it is, actionably.** `form-agent-model` commits to $M_t = \phi(\mathcal{C}_t)$ — **chronica-only**. There is no $M_0$ / initial-prior / pretrained-parameter / innate-architecture term anywhere in the core segment. For a Kalman filter or developer this is fine; for a logogenic agent it is structurally incomplete — an LLM's model quality lives overwhelmingly in pretrained weights, not in the chronica. **Concrete first task:** decide whether the core formulation should carry $M_t = \phi(M_0, \mathcal{C}_t)$ (with $M_0$ the initial epistemic state / prior absorbed structure), or whether a one-paragraph Discussion note in `form-agent-model` stating "$M_0$ and model-class $\mathcal{M}$ absorb priors/pretrained structure; the logogenic instantiation makes this explicit" + a forward-pointer to the 03-llm-core effective-state decomposition is the right (cheaper) move.

**(2) Named canon loci checked.** `01-aat-core/src/form-agent-model.md` (full): $\phi(\mathcal{C}_t)$ throughout; `def-agent-spectrum` handles the impoverished-PID end but not $M_0$. **The pretrained-prior IS handled downstream in 03-llm-core** — `scope-logogenic-agent.md:70` defines $X_t^{\text{eff}} = (M_0^{\text{weights}}, X_t^{\text{context}})$; `obs-context-turnover.md:27-90` uses $M_0^{\text{weights}}$ as the frozen prior in the turnover kernel; `der-turnover-information-recursion.md:18`. So the auditor's "logogenic case looks under-described" is *over*-stated against current canon — 03-llm-core does this well. **The real gap is the core↔component seam:** the core formulation's $\phi(\mathcal{C}_t)$ doesn't carry the $M_0$ term its own logogenic specialization needs, so a reader walking Part I sees a chronica-only model and only later meets $M_0$. Not in PROPOSALS/TODO/ledger.

**(3) Why a gem — strength + wisdom.** It is the cleanest single point where Part I's adaptive-systems formalism connects to the logogenic substrate that motivates the whole program. Making $M_0$ first-class in the core (or at least pointing at it) is structural integration, not decoration — it closes a seam that currently makes the framework read as if "everything the agent knows comes from its chronica," which is false for the agents Joseph most cares about (ELIs). Strengthen-direction available: derive the chronica-only form as the $M_0$-trivial special case, exactly parallel to how the scalar tempo is recovered as a special case of the matrix-Loewner object (F4's pattern).

**(4) First task / home.** Decision-then-edit in `form-agent-model.md` Discussion + Epistemic Status; coordinate with 03-llm-core's existing $X_t^{\text{eff}}$ decomposition so the core forward-points to it rather than re-deriving. Worth Joseph's call on $\phi(M_0,\mathcal{C}_t)$-in-the-formula vs Discussion-only.

### B2. Deliberation: epistemic-gain vs decision-quality as a possibly-two-track object (Fresh-1)

**(1) What it is, actionably.** `der-deliberation-cost` formalizes the deliberation threshold purely through *update-gain* improvement ($\Delta\eta^\ast$). The auditor flagged that the action-fluency vocabulary is about *decision quality* while the formal benefit term is *epistemic gain* — different objects. **First task:** a spike asking whether the two collapse under named conditions (when does improving $\eta^\ast$ entail improving action-value, and when are they genuinely two-track?), with the deliverable being either a derived collapse-condition (promotes the action-fluency marker from discussion-grade to derived) or a clean two-track statement.

**(2) Named canon loci checked.** `01-aat-core/src/der-deliberation-cost.md` (full): **the conceptual gap is already named in canon** — Epistemic Status line 58: "*The result captures the epistemic benefit of deliberation (improving $\eta^\ast$); in practice, deliberation also provides a direct action-value benefit... which operates through $\rho$ reduction and immediate reward — a fuller formalization would incorporate the unified policy objective (`#def-causal-information-yield`) at significantly more complexity.*" Line 78 "Connection to Part II" extends to the three-way exploit/explore/deliberate allocation (`#disc-exploit-explore-deliberate`) and notes the unified objective outperforms the two-stage decomposition. So this is **not a defect** — the segment is honest. The *open derivation* (does the marker promote under named conditions?) is genuinely not done. Not in PROPOSALS/TODO/ledger.

**(3) Why a gem — strength.** The segment itself says "a fuller formalization would incorporate the unified policy objective at significantly more complexity" — that fuller formalization is the seed. If the collapse condition exists, the deliberation marker $\Delta\eta^\ast(\Delta\tau)\approx 0$ becomes a *derived* action-fluency criterion rather than a discussion-grade heuristic; if it doesn't, the two-track statement is itself a clean structural result. Either outcome is a real strengthening of a load-bearing trade-off segment.

**(4) First task / home.** A spike (`spike-deliberation-epistemic-vs-action-value`), landing in `der-deliberation-cost` Epistemic Status/Discussion or `#disc-exploit-explore-deliberate`. Lower priority than B1; the canon is already honest, so this is upside-not-repair. Candidate for `spikes/PROPOSED.md`.

---

## Valueless / superseded (with locus)

- **Fresh-3 (stale "Section IV" / "AAD-FULL.md" language)** — **superseded.** `grep -rln "AAD-FULL\|Section IV" 01-aat-core/src 02-tst-core/src 03-llm-core/src` returns **nothing**. The doc-rot was already swept project-wide. No action.
- **Fresh-9 (causal-downstream weighting overstates without CIY)** — **resolved/strengthened in canon.** `post-causal-structure.md:49` now reads "give more weight to observations that are *causally downstream*... **The formal measure of this distinction — causal information yield (CIY)** — is developed in `#def-causal-information-yield`." Exactly the CIY-qualification the auditor said it "probably becomes true only when weighted by." Done.
- **BP3 (IB mixed-tier compression)** — **resolved by strengthening.** `form-information-bottleneck.md:40` explicitly partitions "exact for the IB-as-applied-theorem core; robust-qualitative for $\beta(\rho,\pi)$." No open direction.
- **BP1 (recursive-update status harmonization)** — **resolved.** `der-recursive-update.md` frontmatter now `status: exact`, matching Epistemic Status.
- **Fresh-11 (`git checkout` as L3 / TST)** — superseded; landed as SN-3 strengthening (`3072667`/`2666eca`), per MANIFEST Cluster C.
- **Fresh-2 (MI vs realized-surprisal in `form-event-driven-dynamics`)** — near-valueless. `form-event-driven-dynamics.md:37-39` defines $\mathcal{I}(e_\tau)=I(e_\tau;\Omega_\tau\mid M_{\tau^-})$ (MI) and frames "surprising events carry much information" as a distribution-level property, consistently. No downstream segment found treating it as realized content. At most a one-clause editorial nicety; not a gem.
- **Fresh-5/6/7/8/12/14 + Fresh-10** — confirmed by the prior extraction as `soft-polish`/citation-deferred. I did not find theory content in these that would have to be re-derived later; Fresh-5 (PID/thermostat) is partly already handled in `form-agent-model.md:18` (blind-seeker / agent-spectrum tie-in). Left as light-editorial backlog, not gems.

## Already-routed-but-now-wrong dispositions

**None found.** Every numbered finding's MANIFEST disposition matches current `src/` first-hand. The only correction to the *prior extraction* is sharpening, not reversal: it dispositioned Fresh-4 as "candidate `03-llm-core` framing" — but 03-llm-core already has the $M_0$ machinery; the live gap is the **core-formulation seam** (B1 above), which is a stronger and more locatable framing than "surface to Joseph if priority."

## Coverage / honesty note

Read first-hand from `src/`: `scope-agency.md` (full), `form-agent-model.md` (full), `der-deliberation-cost.md` (full), `form-information-bottleneck.md` (1-48), `der-recursive-update.md` (frontmatter + Epistemic Status), `form-event-driven-dynamics.md` (event-info section), `post-causal-structure.md:49`, plus 03-llm-core `scope-logogenic-agent.md` / `obs-context-turnover.md` / `der-turnover-information-recursion.md` (grep-targeted), and `def-mismatch-signal`/`deriv-sector-condition`/`def-adaptive-tempo`/`def-model-sufficiency` spot-confirms for the drift check. Read the full 725-line audit + STATUS + MANIFEST(742613) + ledger(742613) + relevant TODO/PROPOSALS rows. The `AUDIT-WORKING-742613/` gold dir was **not** opened (standing consult-Joseph gate); worked only from the FINAL extraction as instructed.
